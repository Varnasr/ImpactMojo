-- Capture-from-code migration (2026-07-06)
-- These objects already exist in the production project (created ad hoc when the
-- gateway-less UPI subscription flow shipped) but were never committed, so a fresh
-- environment could not reproduce the backend. Definitions below are derived from
-- the code that uses them:
--   netlify/functions/subscribe.mjs / subscription-billing.mjs / confirm.mjs / sub-admin.mjs
--   js/auth.js (profiles cloud-sync columns)
-- Everything is IF NOT EXISTS / ADD COLUMN IF NOT EXISTS so re-running against
-- production is a no-op.

-- ── Subscriptions (UPI, no payment gateway) ────────────────────────────────
create table if not exists public.subscriptions (
  id          uuid primary key default gen_random_uuid(),
  name        text,
  email       text not null,
  plan        text not null,
  cadence     text not null default 'monthly' check (cadence in ('monthly', 'annual')),
  amount      integer not null,                -- rupees
  status      text not null default 'pending'  -- pending | active | cancelled
              check (status in ('pending', 'active', 'cancelled')),
  next_due    date,
  last_paid   date,
  created_at  timestamptz not null default now()
);

create table if not exists public.subscription_payments (
  id              uuid primary key default gen_random_uuid(),
  subscription_id uuid not null references public.subscriptions (id) on delete cascade,
  period          text not null,               -- 'YYYY-MM'
  amount          integer not null,            -- rupees
  reference       text not null unique,        -- 'IMX-<PLAN>-<YYYYMM>-<ID6>' (UPI note / reconciliation key)
  status          text not null default 'invoiced' check (status in ('invoiced', 'paid')),
  created_at      timestamptz not null default now()
);

create index if not exists subscription_payments_subscription_id_idx
  on public.subscription_payments (subscription_id);
create index if not exists subscriptions_next_due_idx
  on public.subscriptions (next_due) where status <> 'cancelled';

-- Service-role access only: RLS on with no policies. All four Netlify functions
-- use SUPABASE_SERVICE_ROLE_KEY, which bypasses RLS; anon/authenticated get nothing.
alter table public.subscriptions enable row level security;
alter table public.subscription_payments enable row level security;

-- ── Profiles cloud-sync columns (used by js/auth.js) ───────────────────────
alter table public.profiles add column if not exists bookmarks      jsonb;
alter table public.profiles add column if not exists notes          jsonb;
alter table public.profiles add column if not exists compare_list   jsonb;
alter table public.profiles add column if not exists streak_data    jsonb;
alter table public.profiles add column if not exists progress       jsonb;
alter table public.profiles add column if not exists last_synced_at timestamptz;
