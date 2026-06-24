-- ============================================================
-- Peer Review System
-- Date: 2026-06-24
--
-- Roadmap: "Peer review system — Learners review each other's
-- assignments and case analyses."
--
-- Learners write reviews of OTHER learners' challenge submissions
-- (public.challenge_submissions). Each review carries three 1–5
-- ratings (clarity, rigor, usefulness) plus free-text feedback.
--
-- Self-review is prevented two ways:
--   1. In the application (the page filters out the user's own
--      submissions and never offers a review form for them).
--   2. At the DB level via a BEFORE INSERT/UPDATE trigger that
--      raises if reviewer_id == the submission owner's user_id.
-- (A pure column CHECK cannot reference another table, hence the
--  trigger.)
--
-- Apply via the Supabase migration flow (supabase db push /
-- migration apply) — do NOT run ad-hoc in the SQL editor without
-- recording it as a migration.
-- ============================================================

-- ============================================================
-- TABLE: peer_reviews
-- ============================================================
CREATE TABLE IF NOT EXISTS public.peer_reviews (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    submission_id UUID REFERENCES public.challenge_submissions(id) ON DELETE CASCADE NOT NULL,
    reviewer_id UUID REFERENCES auth.users(id) ON DELETE CASCADE NOT NULL,
    rating_clarity INTEGER NOT NULL CHECK (rating_clarity BETWEEN 1 AND 5),
    rating_rigor INTEGER NOT NULL CHECK (rating_rigor BETWEEN 1 AND 5),
    rating_usefulness INTEGER NOT NULL CHECK (rating_usefulness BETWEEN 1 AND 5),
    review_text TEXT NOT NULL,
    status TEXT DEFAULT 'submitted',
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW(),
    -- One review per reviewer per submission
    UNIQUE(submission_id, reviewer_id)
);

ALTER TABLE public.peer_reviews ENABLE ROW LEVEL SECURITY;

-- ============================================================
-- SELF-REVIEW GUARD
-- A reviewer must not be the submission's own author.
-- ============================================================
CREATE OR REPLACE FUNCTION public.prevent_self_peer_review()
RETURNS TRIGGER AS $$
DECLARE
    owner_id UUID;
BEGIN
    SELECT user_id INTO owner_id
    FROM public.challenge_submissions
    WHERE id = NEW.submission_id;

    IF owner_id IS NOT NULL AND owner_id = NEW.reviewer_id THEN
        RAISE EXCEPTION 'A learner cannot peer-review their own submission';
    END IF;

    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS peer_reviews_prevent_self ON public.peer_reviews;
CREATE TRIGGER peer_reviews_prevent_self
    BEFORE INSERT OR UPDATE ON public.peer_reviews
    FOR EACH ROW EXECUTE FUNCTION public.prevent_self_peer_review();

-- ============================================================
-- RLS POLICIES — peer_reviews
-- (style matches 20260315_challenge_tables.sql /
--  20260320_cohorts_and_notifications.sql)
-- ============================================================

-- Reviewers can read their own reviews
DROP POLICY IF EXISTS "Reviewers can view own reviews" ON public.peer_reviews;
CREATE POLICY "Reviewers can view own reviews" ON public.peer_reviews
    FOR SELECT USING (auth.uid() = reviewer_id);

-- Submission owners can read reviews left on their own submissions
DROP POLICY IF EXISTS "Owners can view reviews of their submissions" ON public.peer_reviews;
CREATE POLICY "Owners can view reviews of their submissions" ON public.peer_reviews
    FOR SELECT USING (
        EXISTS (
            SELECT 1 FROM public.challenge_submissions s
            WHERE s.id = peer_reviews.submission_id AND s.user_id = auth.uid()
        )
    );

-- Reviewers can insert their own reviews (self-review still blocked by trigger)
DROP POLICY IF EXISTS "Reviewers can insert own reviews" ON public.peer_reviews;
CREATE POLICY "Reviewers can insert own reviews" ON public.peer_reviews
    FOR INSERT WITH CHECK (auth.uid() = reviewer_id);

-- Reviewers can update their own reviews
DROP POLICY IF EXISTS "Reviewers can update own reviews" ON public.peer_reviews;
CREATE POLICY "Reviewers can update own reviews" ON public.peer_reviews
    FOR UPDATE USING (auth.uid() = reviewer_id)
    WITH CHECK (auth.uid() = reviewer_id);

-- ============================================================
-- RLS POLICY — challenge_submissions (additive)
-- Let learners SELECT OTHER learners' submissions so they can
-- pick something to review. The existing
-- "Users can view own submissions" policy (20260315) only
-- covers a learner's own rows; this adds peer visibility.
-- Policies are permissive/OR-combined, so own-row access is
-- preserved.
-- ============================================================
DROP POLICY IF EXISTS "Learners can view peers' submissions for review" ON public.challenge_submissions;
CREATE POLICY "Learners can view peers' submissions for review" ON public.challenge_submissions
    FOR SELECT USING (
        auth.uid() IS NOT NULL AND auth.uid() <> user_id
    );

-- ============================================================
-- INDEXES
-- ============================================================
CREATE INDEX IF NOT EXISTS idx_peer_reviews_submission_id ON public.peer_reviews(submission_id);
CREATE INDEX IF NOT EXISTS idx_peer_reviews_reviewer_id ON public.peer_reviews(reviewer_id);
