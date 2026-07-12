-- GA4 snapshot store (2026-07-12)
--
-- Holds a single 'latest' row of GA4 numbers pushed daily by the Apps Script
-- bridge (admin/ga4-bridge.gs) via netlify/functions/ga4-ingest.mjs, and read
-- back by netlify/functions/ga4.mjs for the admin dashboard — so live-ish GA4
-- data shows with no per-admin Google sign-in and no service-account key.
-- Only the service role (via those functions) touches this table; RLS is on
-- with no public policies. Created ad hoc in production; captured here so a
-- fresh environment reproduces it. Idempotent.

create table if not exists public.ga4_snapshot (
  id text primary key default 'latest',
  data jsonb not null,
  updated_at timestamptz not null default now()
);

alter table public.ga4_snapshot enable row level security;
