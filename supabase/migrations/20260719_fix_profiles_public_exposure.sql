-- Close the public profiles exposure introduced by the certificate-verification
-- policy (20260314_certificate_trigger.sql:100). That policy was
-- FOR SELECT USING (true) with no role restriction and no column restriction,
-- which let the anon key read every user's phone, address, bio, tier and role.
--
-- What each consumer actually needs:
--   * verify-certificate.html + cert-og edge function (anon):
--       full_name / display_name by id  -> column-limited anon grant
--   * org-dashboard member lists (authenticated org peers):
--       member profiles incl. email/hours -> shares_org_with() policy
--   * org-dashboard invite-by-email (authenticated):
--       email -> id only                 -> lookup_profile_id_by_email() RPC
--   * account/self flows: unchanged ("Users can view own profile" remains)

DROP POLICY IF EXISTS "Public can view profile names for verification" ON public.profiles;

-- Anon: rows visible, but only these columns are selectable.
REVOKE SELECT ON public.profiles FROM anon;
GRANT SELECT (id, full_name, display_name) ON public.profiles TO anon;

CREATE POLICY "Anon can view display names" ON public.profiles
  FOR SELECT TO anon USING (true);

-- Authenticated: own profile (existing policy) plus profiles of people who
-- share an organization. SECURITY DEFINER helper avoids RLS recursion through
-- organization_members' own policies.
CREATE OR REPLACE FUNCTION public.shares_org_with(target uuid)
RETURNS boolean
LANGUAGE sql STABLE SECURITY DEFINER
SET search_path = public
AS $$
  SELECT EXISTS (
    SELECT 1
    FROM organization_members a
    JOIN organization_members b ON a.org_id = b.org_id
    WHERE a.user_id = auth.uid() AND b.user_id = target
  );
$$;
REVOKE ALL ON FUNCTION public.shares_org_with(uuid) FROM public, anon;
GRANT EXECUTE ON FUNCTION public.shares_org_with(uuid) TO authenticated;

DROP POLICY IF EXISTS "Org peers can view member profiles" ON public.profiles;
CREATE POLICY "Org peers can view member profiles" ON public.profiles
  FOR SELECT TO authenticated
  USING (auth.uid() = id OR public.shares_org_with(id));

-- Admin panel (admin/index.html, admin/learner-analytics.html) lists all
-- profiles and updates role/subscription_status. Until now the list rode on
-- the public USING(true) policy, and the updates were silently blocked by the
-- own-row-only update policy. Give role='admin' users explicit read/update.
CREATE OR REPLACE FUNCTION public.is_admin()
RETURNS boolean
LANGUAGE sql STABLE SECURITY DEFINER
SET search_path = public
AS $$
  SELECT EXISTS (SELECT 1 FROM profiles WHERE id = auth.uid() AND role = 'admin');
$$;
REVOKE ALL ON FUNCTION public.is_admin() FROM public, anon;
GRANT EXECUTE ON FUNCTION public.is_admin() TO authenticated;

DROP POLICY IF EXISTS "Admins can view all profiles" ON public.profiles;
CREATE POLICY "Admins can view all profiles" ON public.profiles
  FOR SELECT TO authenticated USING (public.is_admin());

DROP POLICY IF EXISTS "Admins can update profiles" ON public.profiles;
CREATE POLICY "Admins can update profiles" ON public.profiles
  FOR UPDATE TO authenticated
  USING (public.is_admin()) WITH CHECK (public.is_admin());

-- Invite flow: email -> user id, nothing else. Definer function so the invite
-- works without exposing arbitrary profile rows to every signed-in user.
CREATE OR REPLACE FUNCTION public.lookup_profile_id_by_email(p_email text)
RETURNS uuid
LANGUAGE sql STABLE SECURITY DEFINER
SET search_path = public
AS $$
  SELECT id FROM profiles WHERE lower(email) = lower(p_email) LIMIT 1;
$$;
REVOKE ALL ON FUNCTION public.lookup_profile_id_by_email(text) FROM public, anon;
GRANT EXECUTE ON FUNCTION public.lookup_profile_id_by_email(text) TO authenticated;
