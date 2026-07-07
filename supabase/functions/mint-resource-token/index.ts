// supabase/functions/mint-resource-token/index.ts
// Supabase Edge Function — mints a short-lived JWT for premium resource access.
//
// Env secrets (set via `supabase secrets set`):
//   RESOURCE_TOKEN_SECRET  — HMAC-SHA256 signing key (same value in each Netlify resource site)
//   SUPABASE_URL           — auto-provided by Supabase
//   SUPABASE_ANON_KEY      — auto-provided by Supabase
//   SUPABASE_SERVICE_ROLE_KEY — auto-provided; used to read profiles bypassing RLS

import { serve } from "https://deno.land/std@0.177.0/http/server.ts";
import { createClient } from "https://esm.sh/@supabase/supabase-js@2.39.3";
import { create, getNumericDate } from "https://deno.land/x/djwt@v3.0.2/mod.ts";

// ── Tier → resource ACL ──────────────────────────────────────────────
// Matches existing tiers in profiles.subscription_tier.
// Resource IDs correspond to premium-only tools (NOT flagship courses,
// which are free for everyone).
const TIER_RESOURCES: Record<string, string[]> = {
  explorer: [],
  practitioner: [
    "rq-builder",
  ],
  professional: [
    "rq-builder",
    "code-convert-pro",
    "qual-insights",
    "vaniscribe",
    "devdata-practice",
    "viz-cookbook",
    "devecon-toolkit",
    // Workshop Pro templates
    "toc-workshop-pro",
    "logframe-pro",
    "chart-selector-pro",
    "stakeholder-pro",
    "empathy-pro",
    "policy-canvas-pro",
    "ai-canvas-pro",
    // Field Notes Pro
    "field-notes-pro",
  ],
  organization: [
    "rq-builder",
    "code-convert-pro",
    "qual-insights",
    "vaniscribe",
    "devdata-practice",
    "viz-cookbook",
    "devecon-toolkit",
    // Workshop Pro templates
    "toc-workshop-pro",
    "logframe-pro",
    "chart-selector-pro",
    "stakeholder-pro",
    "empathy-pro",
    "policy-canvas-pro",
    "ai-canvas-pro",
    // Field Notes Pro
    "field-notes-pro",
  ],
};

// ── Resource → Site RESOURCE_ID mapping ──────────────────────────────
// When multiple resources share a single Netlify site, the JWT `resource`
// claim must match that site's RESOURCE_ID env var.
const RESOURCE_SITE_ID: Record<string, string> = {
  "viz-cookbook":        "devdata-practice",   // same Netlify site as devdata-practice
  "toc-workshop-pro":   "workshop-pro",       // all workshop templates share one site
  "logframe-pro":       "workshop-pro",
  "chart-selector-pro": "workshop-pro",
  "stakeholder-pro":    "workshop-pro",
  "empathy-pro":        "workshop-pro",
  "policy-canvas-pro":  "workshop-pro",
  "ai-canvas-pro":      "workshop-pro",
};

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

// ── In-memory rate limiter (per-user, per edge instance) ────────────
// Limits each user to 10 token mints per minute.
const RATE_WINDOW_MS = 60_000;
const RATE_MAX = 10;
const rateMap = new Map<string, { count: number; resetAt: number }>();

function isRateLimited(userId: string): boolean {
  const now = Date.now();
  const entry = rateMap.get(userId);
  if (!entry || now > entry.resetAt) {
    rateMap.set(userId, { count: 1, resetAt: now + RATE_WINDOW_MS });
    return false;
  }
  entry.count++;
  return entry.count > RATE_MAX;
}

serve(async (req: Request) => {
  const cors = corsHeaders(req);

  // Pre-flight
  if (req.method === "OPTIONS") {
    return new Response("ok", { headers: cors });
  }

  // Reject non-POST methods
  if (req.method !== "POST") {
    return new Response(
      JSON.stringify({ error: "Method not allowed" }),
      { status: 405, headers: { ...cors, "Content-Type": "application/json" } },
    );
  }

  // Reject requests from disallowed origins
  const origin = req.headers.get("Origin") || "";
  if (origin && !ALLOWED_ORIGINS.includes(origin)) {
    return new Response(
      JSON.stringify({ error: "Origin not allowed" }),
      { status: 403, headers: { ...cors, "Content-Type": "application/json" } },
    );
  }

  try {
    // 1. Extract the user's Supabase access token from the Authorization header
    const authHeader = req.headers.get("Authorization");
    if (!authHeader?.startsWith("Bearer ")) {
      return new Response(
        JSON.stringify({ error: "Missing or malformed Authorization header" }),
        { status: 401, headers: { ...cors, "Content-Type": "application/json" } },
      );
    }
    const accessToken = authHeader.replace("Bearer ", "");

    // 2. Parse the requested resource ID from the body
    const { resource } = await req.json();
    if (!resource || typeof resource !== "string") {
      return new Response(
        JSON.stringify({ error: "Missing resource id in request body" }),
        { status: 400, headers: { ...cors, "Content-Type": "application/json" } },
      );
    }

    // Validate resource ID against known values
    const knownResources = new Set(Object.values(TIER_RESOURCES).flat());
    if (!knownResources.has(resource)) {
      return new Response(
        JSON.stringify({ error: "Unknown resource" }),
        { status: 400, headers: { ...cors, "Content-Type": "application/json" } },
      );
    }

    // 3. Verify the caller's session using the anon client + their JWT
    const supabaseUrl = Deno.env.get("SUPABASE_URL")!;
    const supabaseAnonKey = Deno.env.get("SUPABASE_ANON_KEY")!;
    const userClient = createClient(supabaseUrl, supabaseAnonKey, {
      global: { headers: { Authorization: `Bearer ${accessToken}` } },
    });
    // Pass the JWT explicitly: in an edge function there is no persisted
    // session for getUser() to read, and with the project's JWT signing keys
    // the token must be validated against the auth server directly.
    const { data: { user }, error: userError } = await userClient.auth.getUser(accessToken);
    if (userError || !user) {
      return new Response(
        JSON.stringify({ error: "Invalid session" }),
        { status: 401, headers: { ...cors, "Content-Type": "application/json" } },
      );
    }

    // 4. Rate limit per user
    if (isRateLimited(user.id)) {
      return new Response(
        JSON.stringify({ error: "Too many requests. Please wait a moment." }),
        {
          status: 429,
          headers: {
            ...cors,
            "Content-Type": "application/json",
            "Retry-After": "60",
          },
        },
      );
    }

    // 5. Fetch the user's subscription tier (use service role to bypass RLS)
    const serviceRoleKey = Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!;
    const adminClient = createClient(supabaseUrl, serviceRoleKey);
    const { data: profile, error: profileError } = await adminClient
      .from("profiles")
      .select("subscription_tier, subscription_status")
      .eq("id", user.id)
      .single();

    if (profileError || !profile) {
      return new Response(
        JSON.stringify({ error: "Profile not found" }),
        { status: 404, headers: { ...cors, "Content-Type": "application/json" } },
      );
    }

    // 6. Check subscription is active
    if (profile.subscription_status !== "active") {
      return new Response(
        JSON.stringify({ error: "Subscription inactive", code: "INACTIVE" }),
        { status: 403, headers: { ...cors, "Content-Type": "application/json" } },
      );
    }

    // 7. Check tier permits the requested resource
    const tier = (profile.subscription_tier || "explorer").toLowerCase();
    const allowed = TIER_RESOURCES[tier] ?? [];
    if (!allowed.includes(resource)) {
      return new Response(
        JSON.stringify({ error: "Your plan does not include this resource", code: "TIER" }),
        { status: 403, headers: { ...cors, "Content-Type": "application/json" } },
      );
    }

    // 8. Mint a short-lived JWT (5 min TTL)
    const secret = Deno.env.get("RESOURCE_TOKEN_SECRET");
    if (!secret) {
      console.error("RESOURCE_TOKEN_SECRET is not set");
      return new Response(
        JSON.stringify({ error: "Server configuration error" }),
        { status: 500, headers: { ...cors, "Content-Type": "application/json" } },
      );
    }

    // Import the HMAC key for djwt v3
    const encoder = new TextEncoder();
    const keyData = encoder.encode(secret);
    const cryptoKey = await crypto.subtle.importKey(
      "raw",
      keyData,
      { name: "HMAC", hash: "SHA-256" },
      false,
      ["sign", "verify"],
    );

    const now = Math.floor(Date.now() / 1000);
    const token = await create(
      { alg: "HS256", typ: "JWT" },
      {
        sub: user.id,
        resource: RESOURCE_SITE_ID[resource] ?? resource,
        iat: now,
        exp: getNumericDate(5 * 60), // 5 minutes from now
      },
      cryptoKey,
    );

    return new Response(
      JSON.stringify({ token }),
      { status: 200, headers: { ...cors, "Content-Type": "application/json" } },
    );
  } catch (err) {
    console.error("mint-resource-token error:", err);
    return new Response(
      JSON.stringify({ error: "Internal server error" }),
      { status: 500, headers: { ...cors, "Content-Type": "application/json" } },
    );
  }
});
