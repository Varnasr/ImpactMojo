-- Permanent home for legacy platform metrics (pre-database era: Google-Sheets
-- backfill + GA4, accurate as of April 2026 per the founder). The site pulls
-- headline numbers from get_public_stats() instead of hardcoding them, so
-- updating a row here updates every page.
--
-- Methodology (documented on /transparency.html): Total = Legacy + Current.
-- To avoid double-counting, "current" contributions only count database rows
-- created AFTER the baseline's as_of date.

CREATE TABLE IF NOT EXISTS public.public_stats_baseline (
    metric text PRIMARY KEY,
    value  bigint NOT NULL,
    as_of  date NOT NULL,
    note   text
);

ALTER TABLE public.public_stats_baseline ENABLE ROW LEVEL SECURITY;

DROP POLICY IF EXISTS "Baseline is public" ON public.public_stats_baseline;
CREATE POLICY "Baseline is public" ON public.public_stats_baseline
  FOR SELECT USING (true);
-- No insert/update/delete policies: writes go through the service role only.

INSERT INTO public.public_stats_baseline (metric, value, as_of, note) VALUES
  ('practitioners_reached', 13000, '2026-04-30', 'Legacy Google-Sheets records + GA4 unique users, April 2026 backfill'),
  ('course_users',         120700, '2026-04-30', 'Cumulative course users, legacy enrolment records + GA4'),
  ('game_users',            35400, '2026-04-30', 'Cumulative game users, GA4'),
  ('tool_users',            43880, '2026-04-30', 'Cumulative studio/tool users, GA4')
ON CONFLICT (metric) DO UPDATE
  SET value = EXCLUDED.value, as_of = EXCLUDED.as_of, note = EXCLUDED.note;

-- v2: returns baseline + live database counts + the combined headline.
-- practitioners_total auto-grows: baseline + profiles created after as_of.
CREATE OR REPLACE FUNCTION public.get_public_stats()
RETURNS json
LANGUAGE sql STABLE SECURITY DEFINER
SET search_path = public
AS $$
  WITH base AS (
    SELECT coalesce((SELECT value FROM public_stats_baseline WHERE metric = 'practitioners_reached'), 0) AS practitioners,
           (SELECT as_of FROM public_stats_baseline WHERE metric = 'practitioners_reached') AS base_date
  )
  SELECT json_build_object(
    'registered_learners', (SELECT count(*) FROM profiles),
    'active_learners_30d', (SELECT count(*) FROM profiles WHERE last_active_at > now() - interval '30 days'),
    'courses_started',     (SELECT count(*) FROM user_progress),
    'courses_completed',   (SELECT count(*) FROM user_progress WHERE completed_at IS NOT NULL),
    'certificates_issued', (SELECT count(*) FROM certificates),
    'learning_minutes',    (SELECT coalesce(sum(time_spent_minutes),0) FROM user_progress),
    'baseline', (SELECT json_object_agg(metric, json_build_object('value', value, 'as_of', as_of)) FROM public_stats_baseline),
    'practitioners_total', (SELECT practitioners FROM base)
      + (SELECT count(*) FROM profiles p, base b
         WHERE b.base_date IS NULL OR p.created_at::date > b.base_date),
    'as_of', now());
$$;

REVOKE ALL ON FUNCTION public.get_public_stats() FROM public;
GRANT EXECUTE ON FUNCTION public.get_public_stats() TO anon, authenticated;
