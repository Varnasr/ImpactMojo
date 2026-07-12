-- Fix profiles.role default + harden the signup trigger (2026-07-12)
--
-- The public.profiles.role column DEFAULT had drifted to the literal string
--   'admin'::text   (stored as '''admin''::text'::text)
-- so every signup whose row was created by handle_new_user() — which does NOT
-- set role — inherited an admin-implying value. ~25 ordinary explorer-tier
-- signups (Apr–Jul 2026) ended up with it. This was corrected ad hoc in
-- production; the statements below capture that change so a fresh environment
-- reproduces it, and so the default can't silently regress unnoticed again.
-- Everything here is idempotent and safe to re-run against production.

-- 1. Correct the column default (root cause).
alter table public.profiles alter column role set default 'learner';

-- 2. Normalise any lingering corrupted / unknown role values down to the
--    least-privileged 'learner'. Clean values (admin/instructor/learner) are
--    left untouched, so real admins keep their role.
update public.profiles
   set role = 'learner'
 where role is null
    or role not in ('admin', 'instructor', 'learner');

-- 3. Harden the signup trigger to set role explicitly, so new accounts never
--    depend on the column default again (belt-and-suspenders).
create or replace function public.handle_new_user()
returns trigger language plpgsql security definer as $function$
begin
  insert into public.profiles (id, email, full_name, display_name, referral_code, role)
  values (
    new.id,
    new.email,
    coalesce(new.raw_user_meta_data->>'full_name', ''),
    coalesce(new.raw_user_meta_data->>'display_name', split_part(new.email, '@', 1)),
    upper(substring(md5(new.id::text) from 1 for 8)),
    'learner'
  )
  on conflict (id) do nothing;
  return new;
end;
$function$;
