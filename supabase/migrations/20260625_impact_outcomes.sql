-- ============================================================
-- Impact Measurement Dashboard
-- Date: 2026-06-25
--
-- Roadmap (Q4): "Track real-world outcomes from learners'
-- projects."
--
-- Learners log the real-world OUTCOMES that came out of applying
-- what they learned on ImpactMojo — a policy that changed, a
-- program that improved, funding that was secured, people who
-- were reached, etc. Each outcome optionally ties back to the
-- course/skill it came from (course_id) and can be marked public
-- so it feeds the platform-wide "Community impact" aggregate view.
--
-- Privacy model:
--   * A learner always sees and manages their OWN outcomes
--     (RLS: user_id = auth.uid()).
--   * Outcomes flagged is_public = true are readable by ANYONE,
--     including anonymous visitors, so the public aggregate
--     (totals + breakdown by type + recent list) works without a
--     login. Private outcomes never leak.
--
-- Apply via the Supabase migration flow (supabase db push /
-- migration apply) — do NOT run ad-hoc in the SQL editor without
-- recording it as a migration.
-- ============================================================

-- ============================================================
-- TABLE: impact_outcomes
-- ============================================================
CREATE TABLE IF NOT EXISTS public.impact_outcomes (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    user_id UUID REFERENCES auth.users(id) ON DELETE CASCADE NOT NULL,
    title TEXT NOT NULL,
    course_id TEXT,                       -- which course/skill it came from (nullable)
    outcome_type TEXT,                    -- 'policy_change' | 'program_improved' | 'funding_secured' | 'people_reached' | 'other'
    description TEXT NOT NULL,
    people_reached INTEGER CHECK (people_reached >= 0),
    location TEXT,
    occurred_on DATE,
    status TEXT DEFAULT 'shared',         -- 'shared' | 'verified'
    is_public BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

ALTER TABLE public.impact_outcomes ENABLE ROW LEVEL SECURITY;

-- ============================================================
-- KEEP updated_at FRESH ON UPDATE
-- ============================================================
CREATE OR REPLACE FUNCTION public.touch_impact_outcomes_updated_at()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS impact_outcomes_touch_updated_at ON public.impact_outcomes;
CREATE TRIGGER impact_outcomes_touch_updated_at
    BEFORE UPDATE ON public.impact_outcomes
    FOR EACH ROW EXECUTE FUNCTION public.touch_impact_outcomes_updated_at();

-- ============================================================
-- RLS POLICIES — impact_outcomes
-- (style matches 20260624_peer_review.sql /
--  20260315_challenge_tables.sql)
-- ============================================================

-- Owners can read their own outcomes (public OR private)
DROP POLICY IF EXISTS "Users can view own outcomes" ON public.impact_outcomes;
CREATE POLICY "Users can view own outcomes" ON public.impact_outcomes
    FOR SELECT USING (auth.uid() = user_id);

-- ANYONE (incl. anonymous visitors) can read public outcomes,
-- so the community aggregate view works logged-out.
DROP POLICY IF EXISTS "Anyone can view public outcomes" ON public.impact_outcomes;
CREATE POLICY "Anyone can view public outcomes" ON public.impact_outcomes
    FOR SELECT USING (is_public = TRUE);

-- Owners can insert their own outcomes
DROP POLICY IF EXISTS "Users can insert own outcomes" ON public.impact_outcomes;
CREATE POLICY "Users can insert own outcomes" ON public.impact_outcomes
    FOR INSERT WITH CHECK (auth.uid() = user_id);

-- Owners can update their own outcomes
DROP POLICY IF EXISTS "Users can update own outcomes" ON public.impact_outcomes;
CREATE POLICY "Users can update own outcomes" ON public.impact_outcomes
    FOR UPDATE USING (auth.uid() = user_id)
    WITH CHECK (auth.uid() = user_id);

-- Owners can delete their own outcomes
DROP POLICY IF EXISTS "Users can delete own outcomes" ON public.impact_outcomes;
CREATE POLICY "Users can delete own outcomes" ON public.impact_outcomes
    FOR DELETE USING (auth.uid() = user_id);

-- ============================================================
-- INDEXES
-- ============================================================
CREATE INDEX IF NOT EXISTS idx_impact_outcomes_user_id ON public.impact_outcomes(user_id);
CREATE INDEX IF NOT EXISTS idx_impact_outcomes_outcome_type ON public.impact_outcomes(outcome_type);
