-- =====================================================
-- ImpactMojo Supabase Database Schema
-- Run this in your Supabase SQL Editor
-- Go to: SQL Editor (left sidebar) → New Query → Paste this → Run
-- =====================================================

-- Enable UUID extension (usually already enabled)
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- =====================================================
-- 1. USER PROFILES TABLE
-- Stores additional user information beyond auth
-- =====================================================
CREATE TABLE IF NOT EXISTS public.profiles (
    id UUID REFERENCES auth.users(id) ON DELETE CASCADE PRIMARY KEY,
    email TEXT,
    full_name TEXT,
    display_name TEXT,
    avatar_url TEXT,
    organization TEXT,
    role TEXT DEFAULT 'learner', -- learner, practitioner, professional, organization_admin
    subscription_tier TEXT DEFAULT 'explorer', -- explorer (free), practitioner, professional, organization
    subscription_status TEXT DEFAULT 'active', -- active, cancelled, expired, trial
    subscription_start DATE,
    subscription_end DATE,
    resource_grants TEXT[], -- standalone one-time purchases (e.g. Practice Pack slugs) granted outside a subscription tier
    upi_vpa TEXT,  -- user's UPI VPA for payment tracking
    phone TEXT,
    country TEXT DEFAULT 'India',
    city TEXT,
    linkedin_url TEXT,
    bio TEXT,
    interests TEXT[], -- Array of interest areas
    courses_completed TEXT[], -- Array of completed course IDs
    certificates_earned TEXT[], -- Array of certificate IDs
    total_learning_hours DECIMAL DEFAULT 0,
    streak_days INTEGER DEFAULT 0,
    last_active_at TIMESTAMPTZ,
    referral_code TEXT UNIQUE,
    referred_by UUID REFERENCES public.profiles(id),
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- =====================================================
-- 2. USER PROGRESS TABLE
-- Tracks learning progress across courses
-- =====================================================
CREATE TABLE IF NOT EXISTS public.user_progress (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    user_id UUID REFERENCES public.profiles(id) ON DELETE CASCADE,
    course_id TEXT NOT NULL,
    course_name TEXT,
    progress_percentage INTEGER DEFAULT 0,
    started_at TIMESTAMPTZ DEFAULT NOW(),
    completed_at TIMESTAMPTZ,
    last_accessed_at TIMESTAMPTZ DEFAULT NOW(),
    time_spent_minutes INTEGER DEFAULT 0,
    current_section TEXT,
    notes TEXT,
    UNIQUE(user_id, course_id)
);

-- =====================================================
-- 3. USER BOOKMARKS TABLE
-- Stores user bookmarks from the site
-- =====================================================
CREATE TABLE IF NOT EXISTS public.bookmarks (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    user_id UUID REFERENCES public.profiles(id) ON DELETE CASCADE,
    item_type TEXT NOT NULL, -- course, deck, tool, blog, resource
    item_id TEXT NOT NULL,
    item_title TEXT,
    item_url TEXT,
    notes TEXT,
    tags TEXT[],
    created_at TIMESTAMPTZ DEFAULT NOW(),
    UNIQUE(user_id, item_type, item_id)
);

-- =====================================================
-- 4. USER NOTES TABLE
-- Personal notes system
-- =====================================================
CREATE TABLE IF NOT EXISTS public.user_notes (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    user_id UUID REFERENCES public.profiles(id) ON DELETE CASCADE,
    title TEXT,
    content TEXT,
    related_course TEXT,
    related_url TEXT,
    tags TEXT[],
    is_pinned BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- =====================================================
-- 5. CERTIFICATES TABLE
-- Issued certificates for completed courses
-- =====================================================
CREATE TABLE IF NOT EXISTS public.certificates (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    user_id UUID REFERENCES public.profiles(id) ON DELETE CASCADE,
    course_id TEXT NOT NULL,
    course_name TEXT NOT NULL,
    certificate_number TEXT UNIQUE NOT NULL,
    issued_at TIMESTAMPTZ DEFAULT NOW(),
    verification_url TEXT,
    pdf_url TEXT,
    UNIQUE(user_id, course_id)
);

-- =====================================================
-- 6. PAYMENT HISTORY TABLE
-- Tracks all payments
-- =====================================================
CREATE TABLE IF NOT EXISTS public.payments (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    user_id UUID REFERENCES public.profiles(id) ON DELETE CASCADE,
    upi_transaction_id TEXT,
    upi_reference TEXT,
    amount DECIMAL NOT NULL,
    currency TEXT DEFAULT 'INR',
    status TEXT DEFAULT 'pending', -- pending, completed, failed, refunded
    payment_method TEXT, -- upi, card, netbanking, wallet
    description TEXT,
    subscription_tier TEXT,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- =====================================================
-- 7. COACHING BOOKINGS TABLE
-- For coaching session bookings
-- =====================================================
CREATE TABLE IF NOT EXISTS public.coaching_bookings (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    user_id UUID REFERENCES public.profiles(id) ON DELETE CASCADE,
    coach_type TEXT NOT NULL, -- career, research, workshop
    session_date DATE,
    session_time TIME,
    duration_minutes INTEGER DEFAULT 60,
    status TEXT DEFAULT 'pending', -- pending, confirmed, completed, cancelled
    notes TEXT,
    payment_id UUID REFERENCES public.payments(id),
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- =====================================================
-- 8. ORGANIZATIONS TABLE
-- For Organization tier team management
-- =====================================================
CREATE TABLE IF NOT EXISTS public.organizations (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    name TEXT NOT NULL,
    slug TEXT UNIQUE,
    admin_id UUID REFERENCES public.profiles(id) ON DELETE SET NULL,
    logo_url TEXT,
    domain TEXT,
    max_seats INTEGER DEFAULT 10,
    billing_email TEXT,
    billing_address TEXT,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- =====================================================
-- 9. ORGANIZATION MEMBERS TABLE
-- Links users to organizations
-- =====================================================
CREATE TABLE IF NOT EXISTS public.organization_members (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    org_id UUID REFERENCES public.organizations(id) ON DELETE CASCADE,
    user_id UUID REFERENCES public.profiles(id) ON DELETE CASCADE,
    role TEXT DEFAULT 'member', -- admin, manager, member
    invited_by UUID REFERENCES public.profiles(id),
    invited_at TIMESTAMPTZ DEFAULT NOW(),
    joined_at TIMESTAMPTZ,
    status TEXT DEFAULT 'invited', -- invited, active, removed
    UNIQUE(org_id, user_id)
);

-- =====================================================
-- 10. LEARNING PATHS TABLE
-- Custom learning paths for organizations
-- =====================================================
CREATE TABLE IF NOT EXISTS public.learning_paths (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    org_id UUID REFERENCES public.organizations(id) ON DELETE CASCADE,
    title TEXT NOT NULL,
    description TEXT,
    course_ids TEXT[] NOT NULL, -- ordered array of course IDs
    created_by UUID REFERENCES public.profiles(id),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- =====================================================
-- 11. LEARNING PATH ASSIGNMENTS TABLE
-- Assigns learning paths to org members
-- =====================================================
CREATE TABLE IF NOT EXISTS public.learning_path_assignments (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    path_id UUID REFERENCES public.learning_paths(id) ON DELETE CASCADE,
    user_id UUID REFERENCES public.profiles(id) ON DELETE CASCADE,
    assigned_by UUID REFERENCES public.profiles(id),
    assigned_at TIMESTAMPTZ DEFAULT NOW(),
    due_date DATE,
    status TEXT DEFAULT 'assigned', -- assigned, in_progress, completed
    completed_at TIMESTAMPTZ,
    UNIQUE(path_id, user_id)
);

-- =====================================================
-- 12. PORTFOLIO ITEMS TABLE
-- User-curated portfolio entries (Premium feature)
-- =====================================================
CREATE TABLE IF NOT EXISTS public.portfolio_items (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    user_id UUID REFERENCES public.profiles(id) ON DELETE CASCADE,
    item_type TEXT NOT NULL, -- certificate, project, case_study, custom
    title TEXT NOT NULL,
    description TEXT,
    course_id TEXT,
    tags TEXT[],
    display_order INTEGER DEFAULT 0,
    is_visible BOOLEAN DEFAULT true,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Add portfolio fields to profiles
-- ALTER TABLE profiles ADD COLUMN IF NOT EXISTS portfolio_headline TEXT;
-- ALTER TABLE profiles ADD COLUMN IF NOT EXISTS portfolio_public BOOLEAN DEFAULT false;

-- =====================================================
-- ROW LEVEL SECURITY (RLS) POLICIES
-- Ensures users can only access their own data
-- =====================================================

-- Enable RLS on all tables
ALTER TABLE public.profiles ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.user_progress ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.bookmarks ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.user_notes ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.certificates ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.payments ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.coaching_bookings ENABLE ROW LEVEL SECURITY;

-- Profiles: Users can view and update their own profile
CREATE POLICY "Users can view own profile" ON public.profiles
    FOR SELECT USING (auth.uid() = id);

CREATE POLICY "Users can update own profile" ON public.profiles
    FOR UPDATE USING (auth.uid() = id);

CREATE POLICY "Users can insert own profile" ON public.profiles
    FOR INSERT WITH CHECK (auth.uid() = id);

-- User Progress: Users can manage their own progress
CREATE POLICY "Users can manage own progress" ON public.user_progress
    FOR ALL USING (auth.uid() = user_id);

-- Bookmarks: Users can manage their own bookmarks
CREATE POLICY "Users can manage own bookmarks" ON public.bookmarks
    FOR ALL USING (auth.uid() = user_id);

-- User Notes: Users can manage their own notes
CREATE POLICY "Users can manage own notes" ON public.user_notes
    FOR ALL USING (auth.uid() = user_id);

-- Certificates: Users can view their own certificates
CREATE POLICY "Users can view own certificates" ON public.certificates
    FOR SELECT USING (auth.uid() = user_id);

-- Payments: Users can view their own payments
CREATE POLICY "Users can view own payments" ON public.payments
    FOR SELECT USING (auth.uid() = user_id);

-- Coaching Bookings: Users can manage their own bookings
CREATE POLICY "Users can manage own bookings" ON public.coaching_bookings
    FOR ALL USING (auth.uid() = user_id);

-- Portfolio Items: Users can manage their own portfolio
ALTER TABLE public.portfolio_items ENABLE ROW LEVEL SECURITY;
CREATE POLICY "Users can manage own portfolio" ON public.portfolio_items
    FOR ALL USING (auth.uid() = user_id);

-- Enable RLS on organization tables
ALTER TABLE public.organizations ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.organization_members ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.learning_paths ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.learning_path_assignments ENABLE ROW LEVEL SECURITY;

-- Organizations: Admins can manage, members can view
CREATE POLICY "Org admins can manage org" ON public.organizations
    FOR ALL USING (auth.uid() = admin_id);

CREATE POLICY "Org members can view org" ON public.organizations
    FOR SELECT USING (
        EXISTS (SELECT 1 FROM public.organization_members WHERE org_id = id AND user_id = auth.uid() AND status = 'active')
    );

-- Organization Members: Admins can manage, members can view their own org
CREATE POLICY "Org admins can manage members" ON public.organization_members
    FOR ALL USING (
        EXISTS (SELECT 1 FROM public.organizations WHERE id = org_id AND admin_id = auth.uid())
    );

CREATE POLICY "Users can view own membership" ON public.organization_members
    FOR SELECT USING (auth.uid() = user_id);

-- Learning Paths: Org admins can manage, members can view
CREATE POLICY "Org admins can manage learning paths" ON public.learning_paths
    FOR ALL USING (
        EXISTS (SELECT 1 FROM public.organizations WHERE id = org_id AND admin_id = auth.uid())
    );

CREATE POLICY "Org members can view learning paths" ON public.learning_paths
    FOR SELECT USING (
        EXISTS (SELECT 1 FROM public.organization_members WHERE org_id = learning_paths.org_id AND user_id = auth.uid() AND status = 'active')
    );

-- Learning Path Assignments: Admins can manage, users can view own
CREATE POLICY "Admins can manage assignments" ON public.learning_path_assignments
    FOR ALL USING (
        EXISTS (
            SELECT 1 FROM public.learning_paths lp
            JOIN public.organizations o ON o.id = lp.org_id
            WHERE lp.id = path_id AND o.admin_id = auth.uid()
        )
    );

CREATE POLICY "Users can view own assignments" ON public.learning_path_assignments
    FOR SELECT USING (auth.uid() = user_id);

-- =====================================================
-- FUNCTIONS AND TRIGGERS
-- =====================================================

-- Function to automatically create profile on signup
CREATE OR REPLACE FUNCTION public.handle_new_user()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO public.profiles (id, email, full_name, display_name, referral_code)
    VALUES (
        NEW.id,
        NEW.email,
        COALESCE(NEW.raw_user_meta_data->>'full_name', ''),
        COALESCE(NEW.raw_user_meta_data->>'display_name', SPLIT_PART(NEW.email, '@', 1)),
        UPPER(SUBSTRING(MD5(NEW.id::TEXT) FROM 1 FOR 8))
    )
    ON CONFLICT (id) DO NOTHING;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

-- Trigger to create profile on new user signup
DROP TRIGGER IF EXISTS on_auth_user_created ON auth.users;
CREATE TRIGGER on_auth_user_created
    AFTER INSERT ON auth.users
    FOR EACH ROW EXECUTE FUNCTION public.handle_new_user();

-- Function to update updated_at timestamp
CREATE OR REPLACE FUNCTION public.update_updated_at()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Triggers for updated_at
CREATE TRIGGER profiles_updated_at
    BEFORE UPDATE ON public.profiles
    FOR EACH ROW EXECUTE FUNCTION public.update_updated_at();

CREATE TRIGGER user_notes_updated_at
    BEFORE UPDATE ON public.user_notes
    FOR EACH ROW EXECUTE FUNCTION public.update_updated_at();

-- =====================================================
-- INDEXES FOR PERFORMANCE
-- =====================================================
CREATE INDEX IF NOT EXISTS idx_profiles_email ON public.profiles(email);
CREATE INDEX IF NOT EXISTS idx_profiles_subscription_tier ON public.profiles(subscription_tier);
CREATE INDEX IF NOT EXISTS idx_user_progress_user_id ON public.user_progress(user_id);
CREATE INDEX IF NOT EXISTS idx_bookmarks_user_id ON public.bookmarks(user_id);
CREATE INDEX IF NOT EXISTS idx_certificates_user_id ON public.certificates(user_id);
CREATE INDEX IF NOT EXISTS idx_payments_user_id ON public.payments(user_id);
CREATE INDEX IF NOT EXISTS idx_org_members_org_id ON public.organization_members(org_id);
CREATE INDEX IF NOT EXISTS idx_org_members_user_id ON public.organization_members(user_id);
CREATE INDEX IF NOT EXISTS idx_learning_paths_org_id ON public.learning_paths(org_id);
CREATE INDEX IF NOT EXISTS idx_learning_path_assignments_user_id ON public.learning_path_assignments(user_id);
CREATE INDEX IF NOT EXISTS idx_coaching_bookings_user_id ON public.coaching_bookings(user_id);
CREATE INDEX IF NOT EXISTS idx_portfolio_items_user_id ON public.portfolio_items(user_id);

-- =====================================================
-- 12. CHALLENGE SUBMISSIONS TABLE
-- Stores user submissions to Live Case Challenges
-- =====================================================
CREATE TABLE IF NOT EXISTS public.challenge_submissions (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    challenge_id TEXT NOT NULL,
    user_id UUID REFERENCES auth.users(id) ON DELETE CASCADE NOT NULL,
    submission_text TEXT NOT NULL,
    submission_status TEXT DEFAULT 'pending', -- pending, reviewed, graded
    submitted_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW(),
    UNIQUE(challenge_id, user_id)
);

ALTER TABLE public.challenge_submissions ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Users can view own submissions" ON public.challenge_submissions
    FOR SELECT USING (auth.uid() = user_id);

CREATE POLICY "Users can insert own submissions" ON public.challenge_submissions
    FOR INSERT WITH CHECK (auth.uid() = user_id);

CREATE POLICY "Users can update own submissions" ON public.challenge_submissions
    FOR UPDATE USING (auth.uid() = user_id);

CREATE INDEX IF NOT EXISTS idx_challenge_submissions_user_id ON public.challenge_submissions(user_id);
CREATE INDEX IF NOT EXISTS idx_challenge_submissions_challenge_id ON public.challenge_submissions(challenge_id);

-- =====================================================
-- 13. CHALLENGE REQUESTS TABLE (Team Plan)
-- Stores custom challenge requests from organisations
-- =====================================================
CREATE TABLE IF NOT EXISTS public.challenge_requests (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    org_id UUID REFERENCES public.organizations(id) ON DELETE CASCADE NOT NULL,
    requested_by UUID REFERENCES auth.users(id) ON DELETE SET NULL,
    topic TEXT NOT NULL,
    track TEXT NOT NULL,
    description TEXT NOT NULL,
    participants INTEGER,
    difficulty TEXT DEFAULT 'intermediate',
    status TEXT DEFAULT 'pending', -- pending, in_progress, completed, declined
    admin_notes TEXT,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

ALTER TABLE public.challenge_requests ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Org members can view their org requests" ON public.challenge_requests
    FOR SELECT USING (
        org_id IN (SELECT org_id FROM public.organization_members WHERE user_id = auth.uid())
    );

CREATE POLICY "Org members can insert requests" ON public.challenge_requests
    FOR INSERT WITH CHECK (
        org_id IN (SELECT org_id FROM public.organization_members WHERE user_id = auth.uid())
    );

CREATE INDEX IF NOT EXISTS idx_challenge_requests_org_id ON public.challenge_requests(org_id);

-- =====================================================
-- SUCCESS MESSAGE
-- =====================================================
-- If you see this without errors, your database is ready!
-- Next: Set up authentication in your Supabase dashboard
