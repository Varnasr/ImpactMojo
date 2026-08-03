-- Close the anon-role exposure the daily Supabase health & privacy routine has
-- flagged every run from 2026-07-21 through 2026-08-03 (11 consecutive days):
-- push_subscriptions, challenge_submissions, organizations, and organization_members
-- all still carry Supabase's default blanket GRANT to anon (SELECT/INSERT/UPDATE/
-- DELETE/TRUNCATE/REFERENCES/TRIGGER, inherited from table creation and never
-- revoked) plus RLS policies scoped to `public` (which includes anon) instead of
-- `authenticated`. Every policy's USING/WITH CHECK clause is auth.uid()-based, so
-- anon (auth.uid() IS NULL) has never actually been able to read or write a row --
-- this is a defense-in-depth fix, not a response to a confirmed data leak.
--
-- Confirmed no legitimate anon consumer exists for any of the four tables:
--   * push_subscriptions: no frontend/anon code path at all; only touched by the
--     send-push edge function, which uses the service role (bypasses RLS/grants).
--   * challenge_submissions: every frontend read/write (js/challenges.js,
--     peer-review.html, admin/learner-analytics.html) is gated behind a signed-in
--     user check.
--   * organizations / organization_members: every frontend read/write
--     (org-dashboard.html) runs inside AuthGate.protect(), which redirects
--     unauthenticated visitors to /login.html before any query fires.
--
-- Same pattern as 20260719_fix_profiles_public_exposure.sql, minus the column-level
-- carve-out that migration needed (profiles has a legitimate anon consumer;
-- these four tables don't, so a full REVOKE is safe).

REVOKE ALL ON public.push_subscriptions FROM anon;
REVOKE ALL ON public.challenge_submissions FROM anon;
REVOKE ALL ON public.organizations FROM anon;
REVOKE ALL ON public.organization_members FROM anon;

-- Belt-and-braces: scope the RLS policies themselves to authenticated so a future
-- GRANT to anon (e.g. from a schema-wide `GRANT ALL ... TO anon` migration) can't
-- silently reopen access. USING/WITH CHECK clauses are unchanged.
ALTER POLICY "Users can manage own push subscriptions" ON public.push_subscriptions TO authenticated;

ALTER POLICY "Learners can view peers' submissions for review" ON public.challenge_submissions TO authenticated;
ALTER POLICY "Users can insert own submissions" ON public.challenge_submissions TO authenticated;
ALTER POLICY "Users can update own submissions" ON public.challenge_submissions TO authenticated;
ALTER POLICY "Users can view own submissions" ON public.challenge_submissions TO authenticated;

ALTER POLICY "org_admin_delete" ON public.organizations TO authenticated;
ALTER POLICY "org_admin_insert" ON public.organizations TO authenticated;
ALTER POLICY "org_admin_select" ON public.organizations TO authenticated;
ALTER POLICY "org_admin_update" ON public.organizations TO authenticated;

ALTER POLICY "org_members_admin_delete" ON public.organization_members TO authenticated;
ALTER POLICY "org_members_admin_insert" ON public.organization_members TO authenticated;
ALTER POLICY "org_members_admin_select" ON public.organization_members TO authenticated;
ALTER POLICY "org_members_admin_update" ON public.organization_members TO authenticated;
