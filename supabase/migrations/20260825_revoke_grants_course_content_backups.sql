-- Daily Supabase health & privacy routine (2026-08-25) found two tables with RLS
-- disabled AND the default Supabase blanket GRANT to anon/authenticated never
-- revoked: course_content_backup_20260821 and course_content_backup_20260821b
-- (259 rows each, ad-hoc pre-edit snapshots of course_content taken during the
-- 2026-08-21 bulk content pass — see .claude/memory.md session log for that date,
-- and docs/flagship-course-standard.md:335).
--
-- Because RLS is OFF on these tables, there is no policy layer at all: the grant
-- IS the access control. Confirmed live via a read-only anon-key probe (no write
-- attempted): GET .../course_content_backup_20260821?select=id,course_id&limit=1
-- returned 200 with a live row. anon and authenticated both also held INSERT,
-- UPDATE, DELETE, TRUNCATE, REFERENCES and TRIGGER on both tables -- an
-- unauthenticated caller could have altered or wiped either backup via the
-- public REST API.
--
-- No frontend code references either table name (grepped *.js/*.html) -- these
-- are backup artifacts, not consumed by any anon or signed-in user flow, so a
-- full REVOKE (not a column-level carve-out) is safe. Same pattern as
-- 20260803_revoke_anon_grants_flagged_tables.sql and
-- 20260719_fix_profiles_public_exposure.sql. service_role (used by admin
-- tooling/migrations) is unaffected -- REVOKE ALL only touches anon/authenticated.

REVOKE ALL ON public.course_content_backup_20260821 FROM anon, authenticated;
REVOKE ALL ON public.course_content_backup_20260821b FROM anon, authenticated;

-- Belt-and-braces: enable RLS with no policies, so even if a future migration
-- re-grants table privileges to anon/authenticated, there is a policy layer
-- (default-deny) in the way rather than nothing at all.
ALTER TABLE public.course_content_backup_20260821 ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.course_content_backup_20260821b ENABLE ROW LEVEL SECURITY;
