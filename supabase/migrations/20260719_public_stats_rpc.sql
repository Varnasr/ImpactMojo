-- Public platform stats for the transparency page (/transparency.html).
-- Applied live on 2026-07-19 via the Management API; this file is the
-- versioned record so the function survives a project rebuild.
--
-- Anon-callable, aggregate-only (no row-level data leaves the database).
-- The transparency page renders these under "Live Database Numbers" with
-- the caveat that tracking started in 2026 (signed-in learners only).
--
-- Baseline note: pre-database totals (legacy Google-Sheets era) are NOT in
-- these counts. When the legacy baseline is backfilled, add a
-- public_stats_baseline table (or constants here) and surface both figures
-- per the documented methodology: Total = Legacy + Current.

CREATE OR REPLACE FUNCTION public.get_public_stats()
RETURNS json
LANGUAGE sql STABLE SECURITY DEFINER
SET search_path = public
AS $$
  SELECT json_build_object(
    'registered_learners', (SELECT count(*) FROM profiles),
    'active_learners_30d', (SELECT count(*) FROM profiles WHERE last_active_at > now() - interval '30 days'),
    'courses_started',     (SELECT count(*) FROM user_progress),
    'courses_completed',   (SELECT count(*) FROM user_progress WHERE completed_at IS NOT NULL),
    'certificates_issued', (SELECT count(*) FROM certificates),
    'learning_minutes',    (SELECT coalesce(sum(time_spent_minutes),0) FROM user_progress),
    'as_of', now());
$$;

REVOKE ALL ON FUNCTION public.get_public_stats() FROM public;
GRANT EXECUTE ON FUNCTION public.get_public_stats() TO anon, authenticated;
