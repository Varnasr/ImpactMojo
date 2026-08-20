-- auto_issue_certificate() had never issued a certificate. Two silent faults:
--
-- 1. It called uuid_generate_v4(). uuid-ossp IS installed, but in the
--    `extensions` schema, while this function pins
--    SET search_path TO 'public','pg_temp' -- so the call could never resolve.
--    Every write pushing progress_percentage to 100 was REJECTED outright
--    ("function uuid_generate_v4() does not exist"), so the learner lost the
--    completion as well as the certificate. gen_random_uuid() is core Postgres
--    and lives in pg_catalog, so it resolves under any search_path.
--
-- 2. The course map covered 9 ids; js/course-progress.js knows 20 (19 plus
--    social-movements). The rest hit `IF v_course_name IS NULL THEN RETURN NEW`
--    and completed with no certificate and no error. Two of the nine also
--    carried names disagreeing with the client's ('gandhi', 'poa').
--
-- The map stays server-side rather than trusting NEW.course_name: RLS lets a
-- user write their own progress rows, so a client-supplied name would let
-- anyone mint a publicly verifiable certificate for a course that does not
-- exist.
CREATE OR REPLACE FUNCTION public.auto_issue_certificate()
 RETURNS trigger
 LANGUAGE plpgsql
 SECURITY DEFINER
 SET search_path TO 'public', 'pg_temp'
AS $function$
DECLARE
  v_course_name TEXT;
  v_cert_number TEXT;
  v_existing_id UUID;
  v_hex TEXT;
BEGIN
  IF NEW.progress_percentage < 100 THEN
    RETURN NEW;
  END IF;

  IF OLD IS NOT NULL AND OLD.progress_percentage >= 100 THEN
    RETURN NEW;
  END IF;

  v_course_name := CASE NEW.course_id
    WHEN 'mel'              THEN 'Monitoring, Evaluation & Learning'
    WHEN 'dataviz'          THEN 'Data Visualization for Impact'
    WHEN 'devai'            THEN 'AI for Development'
    WHEN 'devecon'          THEN 'Development Economics'
    WHEN 'gandhi'           THEN 'Gandhi''s Political Thought'
    WHEN 'law'              THEN 'Law & Development'
    WHEN 'media'            THEN 'Media, Communication & Development'
    WHEN 'SEL'              THEN 'Social & Emotional Learning'
    WHEN 'sel'              THEN 'Social-Emotional Learning for Development Practice'
    WHEN 'poa'              THEN 'Politics of Aspiration'
    WHEN 'gender'           THEN 'Gender Studies: Feminisms, Power & Social Change'
    WHEN 'pubchoice'        THEN 'Public Choice: Decisions, Incentives & Institutions'
    WHEN 'pubpol'           THEN 'Public Policy: Process, Design & Governance in India'
    WHEN 'causal'           THEN 'Causal Inference for Development'
    WHEN 'livelihoods'      THEN 'Livelihoods in India: Rural, Urban, and Skills'
    WHEN 'powerBI'          THEN 'Power BI for Practitioners'
    WHEN 'intervention'     THEN 'Designing What Works: Development Interventions from Model to Scale'
    WHEN 'nothing-about-us' THEN 'Nothing About Us Without Us: Disability, Justice & Development'
    WHEN 'nvc-rj'           THEN 'Nonviolence in Practice: Communication, Resistance & Repair'
    WHEN 'social-movements' THEN 'Social Movements & Protests: Theory and South Asian Practice'
    ELSE NULL
  END;

  IF v_course_name IS NULL THEN
    RETURN NEW;
  END IF;

  SELECT id INTO v_existing_id
  FROM public.certificates
  WHERE user_id = NEW.user_id AND course_id = NEW.course_id;

  IF v_existing_id IS NOT NULL THEN
    RETURN NEW;
  END IF;

  v_hex := UPPER(SUBSTRING(MD5(gen_random_uuid()::TEXT || NOW()::TEXT) FROM 1 FOR 6));
  v_cert_number := 'IM-' || UPPER(LEFT(NEW.course_id, 8)) || '-' || EXTRACT(YEAR FROM NOW())::TEXT || '-' || v_hex;

  INSERT INTO public.certificates (
    user_id, course_id, course_name, certificate_number, verification_url
  ) VALUES (
    NEW.user_id, NEW.course_id, v_course_name, v_cert_number,
    'https://www.impactmojo.in/verify-certificate.html?cert=' || v_cert_number
  );

  NEW.completed_at := NOW();

  UPDATE public.profiles
  SET certificates_earned = COALESCE(certificates_earned, '{}') || ARRAY[v_cert_number],
      courses_completed    = COALESCE(courses_completed, '{}') || ARRAY[NEW.course_id]
  WHERE id = NEW.user_id
    AND NOT (COALESCE(courses_completed, '{}') @> ARRAY[NEW.course_id]);

  RETURN NEW;
END;
$function$;
