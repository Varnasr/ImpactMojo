-- ============================================================
-- Add resource_grants to profiles
-- Date: 2026-06-02
--
-- Enables standalone, one-time purchases that grant access to a single
-- premium resource OUTSIDE the subscription-tier ladder — the first use
-- case being Practice Packs sold individually for ₹299.
--
-- resource_grants holds an array of resource slugs (e.g. the Practice Pack
-- directory name: 'tor-writing', 'logframe-building', ...). The client gate
-- (js/practice-pack-gate.js + ImpactMojoAuth.hasResourceAccess) unlocks a
-- resource if the user's tier qualifies OR the slug is present here.
--
-- Granting flow (matches the existing manual-UPI model): after a buyer pays
-- via UPI and submits the premium registration form with their pack, an admin
-- appends the slug:
--   UPDATE public.profiles
--   SET resource_grants = array_append(coalesce(resource_grants, '{}'), 'tor-writing')
--   WHERE email = 'buyer@example.com';
-- ============================================================

ALTER TABLE public.profiles
    ADD COLUMN IF NOT EXISTS resource_grants TEXT[];

COMMENT ON COLUMN public.profiles.resource_grants IS
    'Standalone one-time purchases (e.g. individually-bought Practice Pack slugs) granted outside the subscription tier ladder.';

-- GIN index so "does this user own slug X" stays fast as grants grow.
CREATE INDEX IF NOT EXISTS idx_profiles_resource_grants
    ON public.profiles USING GIN (resource_grants);
