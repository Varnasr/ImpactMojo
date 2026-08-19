-- Allow anonymous challenge submissions to be stored.
--
-- Why this is needed
-- ------------------
-- challenge_submissions has held 0 rows since it was created. js/challenges.js
-- calls syncSubmission(), which returns early on `if (!user) return`, so nothing
-- was ever written for a signed-out submitter -- and user_id was NOT NULL with no
-- email column, so there was nowhere to put an anonymous submission anyway.
--
-- That left Netlify Forms as the only path. Of the 5 challenge submissions it has
-- ever received, Akismet classified 3 as spam (all used disposable-email domains).
-- A spam-filtered submission still returns HTTP 200 to the browser, so the learner
-- saw "Submitted" and the submission was never delivered.
--
-- Additive only: no column is dropped, no existing row is modified.

alter table public.challenge_submissions
  alter column user_id drop not null;

alter table public.challenge_submissions
  add column if not exists email           text,
  add column if not exists challenge_title text,
  add column if not exists attachment_name text,
  add column if not exists source          text default 'web';

-- The (challenge_id, user_id) unique constraint cannot dedupe anonymous rows:
-- in Postgres every NULL is distinct, so each anonymous submission becomes its
-- own row. Signed-in upserts via onConflict are unaffected.

-- An anonymous row must carry a reachable address -- email is the only way to
-- return feedback when there is no account attached to the submission.
alter table public.challenge_submissions
  drop constraint if exists challenge_submissions_identified;
alter table public.challenge_submissions
  add constraint challenge_submissions_identified
  check (user_id is not null or email is not null) not valid;

create index if not exists challenge_submissions_submitted_at_idx
  on public.challenge_submissions (submitted_at desc);

-- Deliberately NOT granted to anon. Writes arrive through
-- netlify/functions/challenge-submit.mjs using the service role, so the table
-- keeps the anon-denied contract that scripts/check-supabase-anon.py asserts
-- (a 401 on select is still the expected result after this migration).
