// supabase/functions/send-push/index.ts
// Supabase Edge Function — web push: store browser subscriptions and deliver
// push notifications. Companion to send-notification (email + in-app).
//
// Endpoints:
//   POST /send-push/save     (user JWT)  Body: { subscription, user_agent? }
//     Upserts the caller's PushSubscription, flips push_enabled = true.
//   POST /send-push/delete   (user JWT)  Body: { endpoint }
//     Removes one subscription for the caller.
//   POST /send-push/send     (service role)  Body: { user_id|user_ids, title, body?, link?, tag? }
//     Sends a push to every subscription of the target user(s); prunes dead ones.
//
// Env: SUPABASE_URL, SUPABASE_ANON_KEY, SUPABASE_SERVICE_ROLE_KEY,
//      VAPID_PUBLIC_KEY, VAPID_PRIVATE_KEY, VAPID_SUBJECT (mailto:…)

import { serve } from "https://deno.land/std@0.177.0/http/server.ts";
import { createClient } from "https://esm.sh/@supabase/supabase-js@2.112.3";
import webpush from "npm:web-push@3.6.7";

const CORS_HEADERS = {
  "Access-Control-Allow-Origin": "https://www.impactmojo.in",
  "Access-Control-Allow-Headers": "authorization, x-client-info, apikey, content-type",
  "Access-Control-Allow-Methods": "POST, OPTIONS",
};

const VAPID_PUBLIC = Deno.env.get("VAPID_PUBLIC_KEY") || "";
const VAPID_PRIVATE = Deno.env.get("VAPID_PRIVATE_KEY") || "";
const VAPID_SUBJECT = Deno.env.get("VAPID_SUBJECT") || "mailto:hello@impactmojo.in";
if (VAPID_PUBLIC && VAPID_PRIVATE) {
  webpush.setVapidDetails(VAPID_SUBJECT, VAPID_PUBLIC, VAPID_PRIVATE);
}

function json(data: unknown, status = 200) {
  return new Response(JSON.stringify(data), {
    status,
    headers: { ...CORS_HEADERS, "Content-Type": "application/json" },
  });
}

// Deliver to all of a user's subscriptions; delete any that are gone (404/410).
async function pushToUser(
  admin: ReturnType<typeof createClient>,
  userId: string,
  payload: Record<string, unknown>
): Promise<{ sent: number; pruned: number }> {
  const { data: subs } = await admin
    .from("push_subscriptions")
    .select("id, endpoint, p256dh, auth")
    .eq("user_id", userId);

  let sent = 0;
  let pruned = 0;
  for (const s of subs || []) {
    const subscription = {
      endpoint: s.endpoint,
      keys: { p256dh: s.p256dh, auth: s.auth },
    };
    try {
      await webpush.sendNotification(subscription, JSON.stringify(payload));
      sent++;
    } catch (err: unknown) {
      const code = (err as { statusCode?: number })?.statusCode;
      if (code === 404 || code === 410) {
        await admin.from("push_subscriptions").delete().eq("id", s.id);
        pruned++;
      } else {
        console.error("push send error:", code, err);
      }
    }
  }
  return { sent, pruned };
}

serve(async (req: Request) => {
  if (req.method === "OPTIONS") return new Response("ok", { headers: CORS_HEADERS });

  const supabaseUrl = Deno.env.get("SUPABASE_URL")!;
  const serviceRoleKey = Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!;
  const admin = createClient(supabaseUrl, serviceRoleKey);

  const action = new URL(req.url).pathname.split("/").pop();

  try {
    if (!VAPID_PUBLIC || !VAPID_PRIVATE) {
      return json({ error: "Push not configured (missing VAPID keys)" }, 503);
    }

    // ── service-role: send a push ──
    if (action === "send") {
      const authHeader = req.headers.get("Authorization") || "";
      const token = authHeader.replace("Bearer ", "");
      if (token !== serviceRoleKey) return json({ error: "Service role required" }, 403);

      const { user_id, user_ids, title, body, link, tag } = await req.json();
      if (!title) return json({ error: "title required" }, 400);
      const targets: string[] = user_ids || (user_id ? [user_id] : []);
      if (targets.length === 0) return json({ error: "user_id or user_ids required" }, 400);

      let sent = 0, pruned = 0;
      for (const uid of targets) {
        // Respect the per-user opt-in flag.
        const { data: prefs } = await admin
          .from("notification_preferences")
          .select("push_enabled")
          .eq("user_id", uid)
          .single();
        if (prefs && prefs.push_enabled === false) continue;

        const r = await pushToUser(admin, uid, {
          title,
          body: body || "",
          link: link || "/",
          tag: tag || undefined,
        });
        sent += r.sent;
        pruned += r.pruned;
      }
      return json({ message: "Push sent", sent, pruned });
    }

    // ── user JWT required for save / delete ──
    const authHeader = req.headers.get("Authorization");
    if (!authHeader?.startsWith("Bearer ")) return json({ error: "Missing Authorization" }, 401);
    const token = authHeader.replace("Bearer ", "");
    const userClient = createClient(supabaseUrl, Deno.env.get("SUPABASE_ANON_KEY")!, {
      global: { headers: { Authorization: `Bearer ${token}` } },
    });
    const { data: { user } } = await userClient.auth.getUser();
    if (!user) return json({ error: "Invalid session" }, 401);

    if (action === "save") {
      const { subscription, user_agent } = await req.json();
      if (!subscription?.endpoint || !subscription?.keys?.p256dh || !subscription?.keys?.auth) {
        return json({ error: "Valid PushSubscription required" }, 400);
      }
      await admin.from("push_subscriptions").upsert({
        user_id: user.id,
        endpoint: subscription.endpoint,
        p256dh: subscription.keys.p256dh,
        auth: subscription.keys.auth,
        user_agent: user_agent || null,
        last_used_at: new Date().toISOString(),
      }, { onConflict: "endpoint" });

      await admin.from("notification_preferences").upsert(
        { user_id: user.id, push_enabled: true, updated_at: new Date().toISOString() },
        { onConflict: "user_id" }
      );
      return json({ message: "Subscription saved" });
    }

    if (action === "delete") {
      const { endpoint } = await req.json();
      if (!endpoint) return json({ error: "endpoint required" }, 400);
      await admin.from("push_subscriptions").delete()
        .eq("user_id", user.id).eq("endpoint", endpoint);
      return json({ message: "Subscription removed" });
    }

    return json({ error: "Unknown action" }, 404);
  } catch (err) {
    console.error("send-push error:", err);
    return json({ error: "Internal server error" }, 500);
  }
});
