-- ============================================================
-- WEB PUSH NOTIFICATIONS
-- Browser push subscriptions + per-user opt-in flag.
-- Additive and reversible: one new table + one new column.
-- ============================================================

-- Stores one row per browser/device the user has granted push permission on.
CREATE TABLE IF NOT EXISTS public.push_subscriptions (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    user_id UUID REFERENCES public.profiles(id) ON DELETE CASCADE NOT NULL,
    endpoint TEXT NOT NULL UNIQUE,           -- push service endpoint (the unique key)
    p256dh TEXT NOT NULL,                     -- client public key (for payload encryption)
    auth TEXT NOT NULL,                       -- client auth secret
    user_agent TEXT,                          -- best-effort device label
    created_at TIMESTAMPTZ DEFAULT NOW(),
    last_used_at TIMESTAMPTZ DEFAULT NOW()
);

ALTER TABLE public.push_subscriptions ENABLE ROW LEVEL SECURITY;

-- Users manage only their own subscriptions. The service role (used by the
-- send-push function) bypasses RLS to read all subscriptions when delivering.
CREATE POLICY "Users can manage own push subscriptions" ON public.push_subscriptions
    FOR ALL USING (auth.uid() = user_id) WITH CHECK (auth.uid() = user_id);

CREATE INDEX IF NOT EXISTS idx_push_subscriptions_user_id ON public.push_subscriptions(user_id);

-- Opt-in flag. Default FALSE — web push always requires an explicit, per-browser
-- permission grant, so it is never on until the user enables it.
ALTER TABLE public.notification_preferences
    ADD COLUMN IF NOT EXISTS push_enabled BOOLEAN DEFAULT FALSE;
