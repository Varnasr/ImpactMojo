#!/usr/bin/env python3
"""Deploy the causal course seed to the production Supabase course_content table.

Runs the generated migration SQL via the Supabase Management API.
Requires $SUPABASE_PAT. Project ref is fixed to the ImpactMojo prod project.

Usage:
  python3 scripts/deploy-causal.py            # deploy all (DELETE+INSERT from migration)
  python3 scripts/deploy-causal.py --verify   # just print per-module lengths
"""
import json, os, sys, subprocess, tempfile

PROJECT_REF = 'ddyszmfffyedolkcugld'
API = f'https://api.supabase.com/v1/projects/{PROJECT_REF}/database/query'
ROOT = os.path.join(os.path.dirname(__file__), '..')
MIGRATION = os.path.join(ROOT, 'supabase', 'migrations', '20260604_seed_causal_content.sql')

def run(query):
    pat = os.environ.get('SUPABASE_PAT')
    if not pat:
        sys.exit('SUPABASE_PAT not set')
    # Use curl (the sandbox proxy permits it; urllib is blocked) with the
    # JSON payload written to a temp file to avoid arg-length limits.
    with tempfile.NamedTemporaryFile('w', suffix='.json', delete=False) as f:
        json.dump({'query': query}, f)
        payload = f.name
    try:
        out = subprocess.run(
            ['curl', '-s', '-w', '\n%{http_code}', '-X', 'POST', API,
             '-H', f'Authorization: Bearer {pat}',
             '-H', 'Content-Type: application/json',
             '-d', f'@{payload}'],
            capture_output=True, text=True, timeout=180,
        )
    finally:
        os.unlink(payload)
    body, _, code = out.stdout.rpartition('\n')
    if code.strip() not in ('200', '201'):
        sys.exit(f'HTTP {code.strip()} from Management API: {body[:500]}')
    return json.loads(body) if body.strip() else []

def verify():
    q = ("select module_number, length(content_html) content_len, "
         "length(coalesce(quiz_html,'')) quiz_len, is_preview "
         "from course_content where course_id='causal' order by module_number;")
    for row in run(q):
        print(f"  M{row['module_number']:>2}  content={row['content_len']:>6}  "
              f"quiz={row['quiz_len']:>5}  preview={row['is_preview']}")

def deploy():
    sql = open(MIGRATION).read()
    res = run(sql)
    print('deploy result:', json.dumps(res)[:300])
    print('--- verify ---')
    verify()

if __name__ == '__main__':
    if '--verify' in sys.argv:
        verify()
    else:
        deploy()
