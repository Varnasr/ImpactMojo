-- Durable store for every consequential form on the site.
--
-- Why
-- ---
-- Netlify Forms is the only path most forms have, and Akismet sits in front of
-- it. A submission it classifies as spam is still accepted with HTTP 200, so the
-- browser cannot tell it apart from a delivered one and the submitter is shown a
-- success message either way.
--
-- That is not hypothetical. Six genuine event registrations were lost this way:
-- Dr Apoorva (Gujarat National Law University) and Navaindu Joshi each signed up
-- for three events in under a minute, and the burst rate alone was enough to get
-- all six classified as spam. Neither was ever contacted.
--
-- Writes arrive only through netlify/functions/form-submit.mjs using the service
-- role, so this table is never granted to anon -- same contract as
-- challenge_submissions, which scripts/check-supabase-anon.py asserts.

create table if not exists public.form_submissions (
  id           uuid primary key default uuid_generate_v4(),
  form_name    text        not null,
  data         jsonb       not null default '{}'::jsonb,
  email        text,
  submitted_at timestamptz not null default now(),
  source       text        not null default 'web',
  status       text        not null default 'new',
  notes        text
);

comment on table public.form_submissions is
  'Durable copy of site form submissions. Written only by the form-submit Netlify Function (service role); never granted to anon. Exists because Netlify Forms silently discards spam-classified submissions with a 200.';

create index if not exists form_submissions_form_name_idx
  on public.form_submissions (form_name, submitted_at desc);
create index if not exists form_submissions_submitted_at_idx
  on public.form_submissions (submitted_at desc);
create index if not exists form_submissions_email_idx
  on public.form_submissions (email) where email is not null;

alter table public.form_submissions enable row level security;

-- No policies and no grants: RLS with zero policies denies everything to anon
-- and authenticated. The service role bypasses RLS, which is the only intended
-- writer. Reads happen from the Supabase dashboard or a service-role tool.
revoke all on public.form_submissions from anon, authenticated;
