-- v3 of get_public_stats(): every engagement metric follows the documented
-- methodology (Total = Legacy baseline + live database) instead of showing
-- bare database zeros while the live tracking matures.
--
-- Baseline rows for engagement metrics are seeded at 0 with note 'awaiting
-- owner backfill' — the founder supplies the pre-database numbers from the
-- legacy Excel/GA4 records, and a simple UPDATE on public_stats_baseline
-- makes the site correct everywhere with no redeploy:
--   UPDATE public_stats_baseline SET value = <n>, note = 'Legacy Excel + GA4'
--   WHERE metric = 'courses_completed';

INSERT INTO public.public_stats_baseline (metric, value, as_of, note) VALUES
  ('courses_started',     0, '2026-04-30', 'awaiting owner backfill'),
  ('courses_completed',   0, '2026-04-30', 'awaiting owner backfill'),
  ('certificates_issued', 0, '2026-04-30', 'awaiting owner backfill'),
  ('learning_minutes',    0, '2026-04-30', 'awaiting owner backfill')
ON CONFLICT (metric) DO NOTHING;

CREATE OR REPLACE FUNCTION public.get_public_stats()
RETURNS json
LANGUAGE sql STABLE SECURITY DEFINER
SET search_path = public
AS $$
  WITH base AS (
    SELECT metric, value FROM public_stats_baseline
  ),
  b AS (
    SELECT
      coalesce((SELECT value FROM base WHERE metric = 'practitioners_reached'), 0) AS practitioners,
      coalesce((SELECT value FROM base WHERE metric = 'courses_started'), 0)       AS started,
      coalesce((SELECT value FROM base WHERE metric = 'courses_completed'), 0)     AS completed,
      coalesce((SELECT value FROM base WHERE metric = 'certificates_issued'), 0)   AS certs,
      coalesce((SELECT value FROM base WHERE metric = 'learning_minutes'), 0)      AS minutes,
      (SELECT as_of FROM public_stats_baseline WHERE metric = 'practitioners_reached') AS base_date
  )
  SELECT json_build_object(
    'registered_learners',  (SELECT count(*) FROM profiles),
    'active_learners_30d',  (SELECT count(*) FROM profiles WHERE last_active_at > now() - interval '30 days'),
    'courses_started',      (SELECT count(*) FROM user_progress),
    'courses_completed',    (SELECT count(*) FROM user_progress WHERE completed_at IS NOT NULL),
    'certificates_issued',  (SELECT count(*) FROM certificates),
    'learning_minutes',     (SELECT coalesce(sum(time_spent_minutes),0) FROM user_progress),
    'courses_started_total',     (SELECT started   FROM b) + (SELECT count(*) FROM user_progress),
    'courses_completed_total',   (SELECT completed FROM b) + (SELECT count(*) FROM user_progress WHERE completed_at IS NOT NULL),
    'certificates_issued_total', (SELECT certs     FROM b) + (SELECT count(*) FROM certificates),
    'learning_minutes_total',    (SELECT minutes   FROM b) + (SELECT coalesce(sum(time_spent_minutes),0) FROM user_progress),
    'baseline', (SELECT json_object_agg(metric, json_build_object('value', value, 'as_of', as_of)) FROM public_stats_baseline),
    'practitioners_total', (SELECT practitioners FROM b)
      + (SELECT count(*) FROM profiles p, b WHERE b.base_date IS NULL OR p.created_at::date > b.base_date),
    'as_of', now());
$$;

REVOKE ALL ON FUNCTION public.get_public_stats() FROM public;
GRANT EXECUTE ON FUNCTION public.get_public_stats() TO anon, authenticated;
