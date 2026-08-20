// supabase/functions/serve-course-content/index.ts
// Supabase Edge Function — serves course content from the database.
//
// Fork protection: only serves content to requests from allowed origins.
// Module 1 of each course is a free preview; remaining modules require auth.
//
// Env (auto-provided by Supabase):
//   SUPABASE_URL
//   SUPABASE_ANON_KEY
//   SUPABASE_SERVICE_ROLE_KEY

import { serve } from "https://deno.land/std@0.177.0/http/server.ts";
import { createClient } from "https://esm.sh/@supabase/supabase-js@2.112.3";

// ── Allowed origins ─────────────────────────────────────────────────
const ALLOWED_ORIGINS = [
  "https://www.impactmojo.in",
  "https://impactmojo.in",
];

function corsHeaders(req: Request): Record<string, string> {
  const origin = req.headers.get("Origin") || "";
  const allowed = ALLOWED_ORIGINS.includes(origin) ? origin : ALLOWED_ORIGINS[0];
  return {
    "Access-Control-Allow-Origin": allowed,
    "Access-Control-Allow-Headers": "authorization, x-client-info, apikey, content-type",
    "Access-Control-Allow-Methods": "POST, OPTIONS",
    "Vary": "Origin",
  };
}

// ── Rate limiter (per IP, per edge instance) ────────────────────────
const RATE_WINDOW_MS = 60_000;
const RATE_MAX = 30; // 30 requests/minute — generous for page loads
const rateMap = new Map<string, { count: number; resetAt: number }>();

function isRateLimited(key: string): boolean {
  const now = Date.now();
  const entry = rateMap.get(key);
  if (!entry || now > entry.resetAt) {
    rateMap.set(key, { count: 1, resetAt: now + RATE_WINDOW_MS });
    return false;
  }
  entry.count++;
  return entry.count > RATE_MAX;
}

serve(async (req: Request) => {
  const cors = corsHeaders(req);

  if (req.method === "OPTIONS") {
    return new Response("ok", { headers: cors });
  }

  if (req.method !== "POST") {
    return new Response(
      JSON.stringify({ error: "Method not allowed" }),
      { status: 405, headers: { ...cors, "Content-Type": "application/json" } },
    );
  }

  // Reject disallowed origins
  const origin = req.headers.get("Origin") || "";
  if (origin && !ALLOWED_ORIGINS.includes(origin)) {
    return new Response(
      JSON.stringify({ error: "Origin not allowed" }),
      { status: 403, headers: { ...cors, "Content-Type": "application/json" } },
    );
  }

  try {
    const { course_id, modules } = await req.json();

    // Validate inputs
    if (!course_id || typeof course_id !== "string") {
      return new Response(
        JSON.stringify({ error: "Missing course_id" }),
        { status: 400, headers: { ...cors, "Content-Type": "application/json" } },
      );
    }

    // Rate limit by IP or fallback
    const clientIP = req.headers.get("x-forwarded-for")?.split(",")[0]?.trim()
      || req.headers.get("cf-connecting-ip")
      || "unknown";
    if (isRateLimited(clientIP)) {
      return new Response(
        JSON.stringify({ error: "Too many requests" }),
        { status: 429, headers: { ...cors, "Content-Type": "application/json", "Retry-After": "60" } },
      );
    }

    // Check if user is authenticated (optional — determines which modules they can access)
    let isAuthenticated = false;
    const authHeader = req.headers.get("Authorization");
    if (authHeader?.startsWith("Bearer ")) {
      const supabaseUrl = Deno.env.get("SUPABASE_URL")!;
      const supabaseAnonKey = Deno.env.get("SUPABASE_ANON_KEY")!;
      const userClient = createClient(supabaseUrl, supabaseAnonKey, {
        global: { headers: { Authorization: authHeader } },
      });
      const { data: { user } } = await userClient.auth.getUser();
      isAuthenticated = !!user;
    }

    // Fetch content using service role (bypasses RLS)
    const supabaseUrl = Deno.env.get("SUPABASE_URL")!;
    const serviceRoleKey = Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!;
    const adminClient = createClient(supabaseUrl, serviceRoleKey);

    let query = adminClient
      .from("course_content")
      .select("module_number, module_title, module_intro, content_html, quiz_html, is_preview")
      .eq("course_id", course_id)
      .order("module_number", { ascending: true });

    // If specific modules requested, filter
    if (Array.isArray(modules) && modules.length > 0) {
      query = query.in("module_number", modules);
    }

    const { data, error } = await query;

    if (error) {
      console.error("DB error:", error);
      return new Response(
        JSON.stringify({ error: "Failed to fetch content" }),
        { status: 500, headers: { ...cors, "Content-Type": "application/json" } },
      );
    }

    if (!data || data.length === 0) {
      return new Response(
        JSON.stringify({ error: "Course not found" }),
        { status: 404, headers: { ...cors, "Content-Type": "application/json" } },
      );
    }

    // All course content is free — no auth gating on modules.
    // Premium gating applies to tools/templates on the homepage, not courses.
    const responseModules = data.map((mod) => {
      return {
        module_number: mod.module_number,
        module_title: mod.module_title,
        module_intro: mod.module_intro,
        content_html: mod.content_html,
        quiz_html: mod.quiz_html,
        locked: false,
      };
    });

    return new Response(
      JSON.stringify({ course_id, modules: responseModules }),
      {
        status: 200,
        headers: {
          ...cors,
          "Content-Type": "application/json",
          "Cache-Control": isAuthenticated
            ? "private, max-age=300"   // 5 min for logged-in users
            : "public, max-age=3600",  // 1 hour for preview content
        },
      },
    );
  } catch (err) {
    console.error("serve-course-content error:", err);
    return new Response(
      JSON.stringify({ error: "Internal server error" }),
      { status: 500, headers: { ...cors, "Content-Type": "application/json" } },
    );
  }
});
