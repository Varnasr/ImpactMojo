// supabase/functions/issue-certificate/index.ts
// Supabase Edge Function — issues a certificate when a course is completed.
//
// Called by: database trigger on user_progress (progress_percentage = 100)
//            OR directly via POST from the client.
//
// Env (auto-provided by Supabase):
//   SUPABASE_URL, SUPABASE_ANON_KEY, SUPABASE_SERVICE_ROLE_KEY

import { serve } from "https://deno.land/std@0.177.0/http/server.ts";
import { createClient } from "https://esm.sh/@supabase/supabase-js@2.39.3";

// ── Course catalog (certificate-eligible courses) ─────────────────────
const COURSE_NAMES: Record<string, string> = {
  mel: "Monitoring, Evaluation & Learning",
  dataviz: "Data Visualization for Impact",
  devai: "AI for Development",
  devecon: "Development Economics",
  gandhi: "Gandhi & Contemporary Development",
  law: "Law & Development",
  media: "Media, Communication & Development",
  SEL: "Social & Emotional Learning",
  poa: "Philosophy of Action",
};

// ── CORS headers ──────────────────────────────────────────────────────
const CORS_HEADERS = {
  "Access-Control-Allow-Origin": "https://www.impactmojo.in",
  "Access-Control-Allow-Headers":
    "authorization, x-client-info, apikey, content-type",
  "Access-Control-Allow-Methods": "POST, OPTIONS",
};

// ── Generate certificate number: IM-DEVECON-2026-A3F7 ─────────────────
function generateCertificateNumber(courseId: string): string {
  const prefix = "IM";
  const courseCode = courseId.toUpperCase().slice(0, 8);
  const year = new Date().getFullYear();
  const hex = crypto.getRandomValues(new Uint8Array(4));
  const suffix = Array.from(hex)
    .map((b) => b.toString(16).padStart(2, "0"))
    .join("")
    .toUpperCase()
    .slice(0, 6);
  return `${prefix}-${courseCode}-${year}-${suffix}`;
}

serve(async (req: Request) => {
  if (req.method === "OPTIONS") {
    return new Response("ok", { headers: CORS_HEADERS });
  }

  try {
    // ── Auth: accept either service-role (trigger) or user JWT ──────
    const authHeader = req.headers.get("Authorization");
    if (!authHeader?.startsWith("Bearer ")) {
      return new Response(
        JSON.stringify({ error: "Missing Authorization header" }),
        {
          status: 401,
          headers: { ...CORS_HEADERS, "Content-Type": "application/json" },
        }
      );
    }
    const accessToken = authHeader.replace("Bearer ", "");

    const supabaseUrl = Deno.env.get("SUPABASE_URL")!;
    const supabaseAnonKey = Deno.env.get("SUPABASE_ANON_KEY")!;
    const serviceRoleKey = Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!;

    // Determine caller: if the token equals the service role key it's a
    // trigger / internal call; otherwise verify the user session.
    let userId: string;

    if (accessToken === serviceRoleKey) {
      // Called from DB trigger / webhook — user_id comes in the body
      const body = await req.json();
      userId = body.user_id;
      if (!userId) {
        return new Response(
          JSON.stringify({ error: "user_id required for service-role calls" }),
          {
            status: 400,
            headers: { ...CORS_HEADERS, "Content-Type": "application/json" },
          }
        );
      }
      // course_id also comes from body for trigger calls
      const courseId = body.course_id;
      if (!courseId) {
        return new Response(
          JSON.stringify({ error: "course_id required" }),
          {
            status: 400,
            headers: { ...CORS_HEADERS, "Content-Type": "application/json" },
          }
        );
      }

      return await issueCertificate(
        supabaseUrl,
        serviceRoleKey,
        userId,
        courseId
      );
    } else {
      // Called from client — verify session
      const userClient = createClient(supabaseUrl, supabaseAnonKey, {
        global: { headers: { Authorization: `Bearer ${accessToken}` } },
      });
      const {
        data: { user },
        error: userError,
      } = await userClient.auth.getUser();
      if (userError || !user) {
        return new Response(
          JSON.stringify({ error: "Invalid session" }),
          {
            status: 401,
            headers: { ...CORS_HEADERS, "Content-Type": "application/json" },
          }
        );
      }
      userId = user.id;

      const body = await req.json();
      const courseId = body.course_id;
      if (!courseId) {
        return new Response(
          JSON.stringify({ error: "course_id required" }),
          {
            status: 400,
            headers: { ...CORS_HEADERS, "Content-Type": "application/json" },
          }
        );
      }

      // ── Admin path: issue a certificate that this service did not award.
      //
      // The assessed tracks sold on the site (mel-assessed-certificate and
      // the others, INR 2,499) are marked by a human and delivered by email.
      // Those learners have no user_progress row and never will, and their
      // track is not in COURSE_NAMES — so the self-service path below
      // refuses them twice over. Their certificate was still promised as
      // "independently checkable", and verify-certificate.html checks by
      // querying this table, so without this branch that promise cannot be
      // kept for anyone who paid.
      //
      // Guarded by the caller's OWN role, read with the service-role client:
      // never a flag from the request body, and never the caller's claim
      // about themselves.
      if (body.target_user_id || body.course_name) {
        const adminClient = createClient(supabaseUrl, serviceRoleKey);
        const { data: callerProfile } = await adminClient
          .from("profiles")
          .select("role")
          .eq("id", userId)
          .single();

        if (callerProfile?.role !== "admin") {
          return new Response(
            JSON.stringify({ error: "Admin role required to issue on behalf of a user" }),
            {
              status: 403,
              headers: { ...CORS_HEADERS, "Content-Type": "application/json" },
            }
          );
        }

        const targetUserId = body.target_user_id || userId;
        const courseName = body.course_name;
        if (!courseName) {
          return new Response(
            JSON.stringify({ error: "course_name required for an admin-issued certificate" }),
            {
              status: 400,
              headers: { ...CORS_HEADERS, "Content-Type": "application/json" },
            }
          );
        }

        return await issueCertificate(
          supabaseUrl,
          serviceRoleKey,
          targetUserId,
          courseId,
          { courseName, skipProgressCheck: true }
        );
      }

      return await issueCertificate(
        supabaseUrl,
        serviceRoleKey,
        userId,
        courseId
      );
    }
  } catch (err) {
    console.error("issue-certificate error:", err);
    return new Response(
      JSON.stringify({ error: "Internal server error" }),
      {
        status: 500,
        headers: { ...CORS_HEADERS, "Content-Type": "application/json" },
      }
    );
  }
});

// ── Core logic ─────────────────────────────────────────────────────────
async function issueCertificate(
  supabaseUrl: string,
  serviceRoleKey: string,
  userId: string,
  courseId: string,
  adminOverride?: { courseName: string; skipProgressCheck: boolean }
) {
  const adminClient = createClient(supabaseUrl, serviceRoleKey);

  // 1. Resolve the course name.
  //
  // An admin-issued certificate carries its own name, because the assessed
  // tracks are products rather than site courses and are deliberately absent
  // from COURSE_NAMES. Every other caller must name a known course.
  const courseName = adminOverride?.courseName ?? COURSE_NAMES[courseId];
  if (!courseName) {
    return new Response(
      JSON.stringify({ error: "Unknown course", course_id: courseId }),
      {
        status: 400,
        headers: { ...CORS_HEADERS, "Content-Type": "application/json" },
      }
    );
  }

  // 2. Check progress is actually 100% — unless an admin is recording an
  //    award that was assessed off-platform, where no progress row exists.
  if (!adminOverride?.skipProgressCheck) {
    const { data: progress } = await adminClient
      .from("user_progress")
      .select("progress_percentage")
      .eq("user_id", userId)
      .eq("course_id", courseId)
      .single();

    if (!progress || progress.progress_percentage < 100) {
      return new Response(
        JSON.stringify({
          error: "Course not yet completed",
          progress: progress?.progress_percentage ?? 0,
        }),
        {
          status: 403,
          headers: { ...CORS_HEADERS, "Content-Type": "application/json" },
        }
      );
    }
  }

  // 3. Check if certificate already exists (idempotent)
  const { data: existing } = await adminClient
    .from("certificates")
    .select("id, certificate_number")
    .eq("user_id", userId)
    .eq("course_id", courseId)
    .single();

  if (existing) {
    return new Response(
      JSON.stringify({
        message: "Certificate already issued",
        certificate_number: existing.certificate_number,
        certificate_id: existing.id,
      }),
      {
        status: 200,
        headers: { ...CORS_HEADERS, "Content-Type": "application/json" },
      }
    );
  }

  // 4. Get user profile for the certificate
  const { data: profile } = await adminClient
    .from("profiles")
    .select("full_name, display_name, email")
    .eq("id", userId)
    .single();

  const recipientName =
    profile?.full_name || profile?.display_name || "Learner";
  const recipientEmail = profile?.email;

  // 5. Generate certificate number
  const certificateNumber = generateCertificateNumber(courseId);
  const verificationUrl = `https://www.impactmojo.in/verify-certificate.html?cert=${certificateNumber}`;

  // 6. Insert certificate record
  const { data: cert, error: insertError } = await adminClient
    .from("certificates")
    .insert({
      user_id: userId,
      course_id: courseId,
      course_name: courseName,
      certificate_number: certificateNumber,
      verification_url: verificationUrl,
    })
    .select()
    .single();

  if (insertError) {
    console.error("Certificate insert error:", insertError);
    return new Response(
      JSON.stringify({ error: "Failed to issue certificate" }),
      {
        status: 500,
        headers: { ...CORS_HEADERS, "Content-Type": "application/json" },
      }
    );
  }

  // 7. Update profile's certificates_earned array
  const { data: currentProfile } = await adminClient
    .from("profiles")
    .select("certificates_earned")
    .eq("id", userId)
    .single();

  const currentCerts = currentProfile?.certificates_earned || [];
  if (!currentCerts.includes(cert.id)) {
    await adminClient
      .from("profiles")
      .update({
        certificates_earned: [...currentCerts, cert.id],
      })
      .eq("id", userId);
  }

  // 8. Send certificate congratulations + premium upsell notification
  try {
    const { data: profile } = await admin
      .from("profiles")
      .select("subscription_tier")
      .eq("id", userId)
      .single();

    // In-app notification for everyone
    await admin.rpc("notify_user", {
      p_user_id: userId,
      p_type: "certificate",
      p_title: `Congratulations! You earned your ${courseName} certificate`,
      p_body: `Certificate ${certificateNumber} is ready. Share it on LinkedIn or download it from your account.`,
      p_link: "/account.html",
      p_metadata: { course_id: courseId, certificate_number: certificateNumber },
    });

    // Email — congrats + soft premium pitch for explorer-tier users
    const resendKey = Deno.env.get("RESEND_API_KEY");
    if (resendKey && recipientEmail) {
      const isExplorer = profile?.subscription_tier === "explorer";
      const premiumPitch = isExplorer
        ? `<hr style="border:none;border-top:1px solid #E2E8F0;margin:24px 0">
<p style="color:#64748B;font-size:14px"><strong>Want to keep the momentum going?</strong> ImpactMojo Premium gives you professional-grade tools like VaniScribe AI transcription, realistic datasets, and workshop templates — starting at just \u20B9399/month. <a href="https://www.impactmojo.in/premium-letter.html" style="color:#F59E0B">Learn more</a></p>`
        : "";

      const html = `<!DOCTYPE html>
<html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width"></head>
<body style="font-family:'Amaranth',Helvetica,Arial,sans-serif;background:#F8FAFC;margin:0;padding:0">
<div style="max-width:560px;margin:0 auto;padding:32px 24px">
<div style="text-align:center;margin-bottom:24px">
<img src="https://www.impactmojo.in/assets/images/favicon.png" width="40" height="40" alt="ImpactMojo" style="border-radius:8px">
<h2 style="font-family:Inter,Helvetica,sans-serif;color:#0F172A;margin:12px 0 0">You did it!</h2>
</div>
<div style="background:#fff;border:1px solid #E2E8F0;border-radius:12px;padding:24px;color:#334155;line-height:1.6;font-size:15px">
<p>Hi ${recipientName},</p>
<p>Huge congratulations — you've completed <strong>${courseName}</strong> and earned your ImpactMojo certificate!</p>
<p style="background:#FFFBEB;border:1px solid #FDE68A;border-radius:8px;padding:16px;text-align:center;margin:16px 0">
<strong style="font-size:18px;color:#92400E">Certificate ${certificateNumber}</strong><br>
<a href="https://www.impactmojo.in${verificationUrl}" style="color:#F59E0B;font-size:13px">Verify &amp; share this certificate</a>
</p>
<p>You can download it, share it on LinkedIn, or add the verification link to your CV. It's yours — you earned it.</p>
<p>Now that you've finished one course, why not try another? Each one earns you a new certificate and builds on what you've learned.</p>
${premiumPitch}
</div>
<p style="text-align:center;color:#94A3B8;font-size:12px;margin-top:24px">
ImpactMojo &middot; Free Development Education for South Asia<br>
<a href="https://www.impactmojo.in/account.html#notifications" style="color:#94A3B8">Manage notification preferences</a>
</p>
</div></body></html>`;

      await fetch("https://api.resend.com/emails", {
        method: "POST",
        headers: {
          Authorization: `Bearer ${resendKey}`,
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          from: "ImpactMojo <notifications@impactmojo.in>",
          to: [recipientEmail],
          subject: `You earned your ${courseName} certificate! \uD83C\uDF89`,
          html,
        }),
      });
    }
  } catch (notifErr) {
    console.error("Certificate notification failed (non-fatal):", notifErr);
  }

  return new Response(
    JSON.stringify({
      message: "Certificate issued successfully",
      certificate_id: cert.id,
      certificate_number: certificateNumber,
      course_name: courseName,
      recipient_name: recipientName,
      verification_url: verificationUrl,
      issued_at: cert.issued_at,
    }),
    {
      status: 201,
      headers: { ...CORS_HEADERS, "Content-Type": "application/json" },
    }
  );
}
