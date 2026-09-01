-- Fixes #1052. Reported by a Supabase advisor email on 2026-09-01
-- (rls_disabled_in_public, ERROR) against project ddyszmfffyedolkcugld.
--
-- course_content_backup_20260821 and course_content_backup_20260821b (259 rows
-- each, taken 2026-08-21) sat in the public schema with row level security OFF
-- and the default anon/authenticated grants intact. They were made with
-- CREATE TABLE AS, which copies rows but inherits neither the source table's
-- RLS nor its policies, so neither copy carried any of course_content's
-- protection.
--
-- course_content is service-role-only: its single policy is
-- auth.role() = 'service_role'. Measured against the live REST API with the
-- anon key published in js/config.js:
--
--     course_content                       0 rows readable by anon
--     course_content_backup_20260821     259 rows readable by anon
--       of which is_preview = false      217 rows, the gated module bodies
--
-- so the full content_html of 217 non-preview modules was readable by anyone
-- who viewed source. Writes were authorised too: a PATCH with a zero-matching
-- filter returned 204 rather than 401, meaning update and delete were open as
-- well. Exposure window 2026-08-21 to 2026-09-01.
--
-- The fix mirrors course_content's own posture rather than inventing a new one:
-- RLS on with no policy denies every request except the service role, which
-- bypasses RLS. The REVOKE is the second layer, so that a permissive policy
-- added later cannot silently re-open the tables the way an inherited grant
-- did here. No rows are changed or dropped; the snapshots stay intact and
-- readable through the service role.
--
-- Same shape as 20260803_revoke_anon_grants_flagged_tables.sql, with one
-- difference worth stating plainly: that migration was defence in depth
-- against an exposure no one could confirm had been reachable. This one closes
-- an exposure that was measured, with the row counts above.

ALTER TABLE public.course_content_backup_20260821  ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.course_content_backup_20260821b ENABLE ROW LEVEL SECURITY;

REVOKE ALL ON public.course_content_backup_20260821  FROM anon, authenticated;
REVOKE ALL ON public.course_content_backup_20260821b FROM anon, authenticated;
