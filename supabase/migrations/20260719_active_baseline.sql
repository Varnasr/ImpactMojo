-- Active-learners floor. last_active_at only began being written on
-- 2026-07-19, so the live 30-day count reads ~0 for pre-existing accounts
-- even though the founder's analytics show ~35 currently active. Store that
-- as an owner-provided floor; the RPC returns GREATEST(live, floor) so the
-- number is honest today and the live count takes over automatically once
-- daily activity pings accumulate past 35.
--
-- To update the floor: UPDATE public_stats_baseline SET value = <n>
--   WHERE metric = 'active_learners_floor';

INSERT INTO public.public_stats_baseline (metric, value, as_of, note) VALUES
  ('active_learners_floor', 35, '2026-07-19', 'Owner analytics (GA) — floor until live last_active_at tracking catches up')
ON CONFLICT (metric) DO UPDATE SET value = EXCLUDED.value, note = EXCLUDED.note;

CREATE OR REPLACE FUNCTION public.get_public_stats()
RETURNS json
LANGUAGE sql STABLE SECURITY DEFINER
SET search_path = public
AS $$
  WITH base AS (SELECT metric, value FROM public_stats_baseline),
  b AS (
    SELECT
      coalesce((SELECT value FROM base WHERE metric = 'practitioners_reached'), 0)  AS practitioners,
      coalesce((SELECT value FROM base WHERE metric = 'courses_started'), 0)         AS started,
      coalesce((SELECT value FROM base WHERE metric = 'courses_completed'), 0)       AS completed,
      coalesce((SELECT value FROM base WHERE metric = 'certificates_issued'), 0)     AS certs,
      coalesce((SELECT value FROM base WHERE metric = 'learning_minutes'), 0)        AS minutes,
      coalesce((SELECT value FROM base WHERE metric = 'active_learners_floor'), 0)   AS active_floor,
      (SELECT as_of FROM public_stats_baseline WHERE metric = 'practitioners_reached') AS base_date
  )
  SELECT json_build_object(
    'registered_learners',  (SELECT count(*) FROM profiles),
    'active_learners_30d',  GREATEST(
                              (SELECT count(*) FROM profiles WHERE last_active_at > now() - interval '30 days'),
                              (SELECT active_floor FROM b)),
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
