-- Owner-supplied legacy baseline (2026-07-19, via founder): pre-database
-- totals up to end-April 2026 from the legacy Excel + GA4 records.
-- learning_minutes is an ESTIMATE the founder asked us to derive:
-- 727 completions x ~18h average course length (the site's stated
-- time-to-complete median) x 60 = 785,160 minutes.

UPDATE public.public_stats_baseline SET value = 120700,
  note = 'Legacy cumulative course users (Sheets + GA4), to Apr 2026'
  WHERE metric = 'courses_started';

UPDATE public.public_stats_baseline SET value = 727,
  note = 'Legacy Excel records, to Apr 2026'
  WHERE metric = 'courses_completed';

UPDATE public.public_stats_baseline SET value = 468,
  note = 'Legacy Excel records, to Apr 2026'
  WHERE metric = 'certificates_issued';

UPDATE public.public_stats_baseline SET value = 785160,
  note = 'Estimated: 727 completions x ~18h avg course length (owner-approved method)'
  WHERE metric = 'learning_minutes';
