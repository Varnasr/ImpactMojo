#!/usr/bin/env python3
"""notebooklm-build-pack.py — build NotebookLM source packs for ImpactMojo flagships.

For each flagship course it emits, under notebooklm/:
  packs/<slug>-source-pack.md   full course text (all modules) — UPLOAD THIS to NotebookLM
                                 (git-ignored: course content is DB-backed / anti-fork)
  readings/<slug>.md            the cited open-access readings (URLs) — add via `add-source`
  prompts/<slug>.md             a ready-to-use study-companion + audio-overview prompt

Course content lives in Supabase (course_content); this pulls it with the
Management API and needs SUPABASE_PAT in the environment. Readings + prompts are
safe to commit (public URLs / prompt text); the full packs are git-ignored.

Usage:
  export SUPABASE_PAT=...                 # loaded from .claude/.env.keys at session start
  python3 scripts/notebooklm-build-pack.py            # all flagships
  python3 scripts/notebooklm-build-pack.py social-movements devecon   # specific slugs
"""
import os, re, sys, json, html, subprocess, pathlib

PROJECT = "ddyszmfffyedolkcugld"
ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "notebooklm"
TITLES = {
 "causal":"Causal Inference & Impact Evaluation","dataviz":"Data Visualization",
 "devai":"Development & AI","devecon":"Development Economics","gandhi":"Gandhi & Nonviolence",
 "gender":"Gender & Development","intervention":"Intervention Design","law":"Law & Justice",
 "livelihoods":"Livelihoods in India","media":"Media & Information",
 "mel":"Monitoring, Evaluation & Learning (MEAL)","nothing-about-us":"Nothing About Us Without Us (Disability)",
 "nvc-rj":"Nonviolent Communication & Restorative Justice","poa":"Policy & Advocacy",
 "powerBI":"Power BI for Development","pubchoice":"Public Choice","pubpol":"Public Policy",
 "SEL":"Social & Emotional Learning","social-movements":"Social Movements & Protests",
}

def q(sql):
    """Run a read query via the Supabase Management API (curl avoids the agent-proxy 403)."""
    pat = os.environ["SUPABASE_PAT"]
    r = subprocess.run(["curl","-s","-X","POST",
        f"https://api.supabase.com/v1/projects/{PROJECT}/database/query",
        "-H",f"Authorization: Bearer {pat}","-H","Content-Type: application/json",
        "-d",json.dumps({"query":sql})], capture_output=True, text=True)
    return json.loads(r.stdout)

def strip_html(s):
    s = re.sub(r"(?is)<svg.*?</svg>", "", s)
    s = re.sub(r"(?is)<style.*?</style>", "", s)
    s = re.sub(r"(?is)<script.*?</script>", "", s)
    s = re.sub(r"(?is)<h[23][^>]*>(.*?)</h[23]>", lambda m: "\n\n## "+re.sub(r"<[^>]+>","",m.group(1)).strip()+"\n", s)
    s = re.sub(r"(?is)<li[^>]*>(.*?)</li>", lambda m: "\n- "+re.sub(r"<[^>]+>","",m.group(1)).strip(), s)
    s = re.sub(r"(?is)<[^>]+>", " ", s)
    s = html.unescape(s)
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\n\s*\n\s*\n+", "\n\n", s)
    return s.strip()

def readings_from(content):
    urls = re.findall(r'href="(https?://[^"]+)"', content)
    seen, out = set(), []
    for u in urls:
        if u in seen: continue
        seen.add(u); out.append(u)
    return out

def build(slug):
    title = TITLES.get(slug, slug)
    rows = q("select module_number,module_title,content_html from course_content "
             f"where course_id='{slug}' order by module_number")
    if not isinstance(rows, list) or not rows:
        print(f"  ! no content for {slug}"); return
    (OUT/"packs").mkdir(parents=True, exist_ok=True)
    (OUT/"readings").mkdir(parents=True, exist_ok=True)
    (OUT/"prompts").mkdir(parents=True, exist_ok=True)
    # PACK
    pack = [f"# {title} — ImpactMojo Flagship Course\n", f"Source pack for a NotebookLM AI Study Companion. {len(rows)} modules.\n"]
    all_urls, mod_titles = [], []
    for r in rows:
        mt = (r.get("module_title") or f"Module {r['module_number']}").strip()
        mod_titles.append(re.sub(r"^Module\s*\d+[:.]?\s*","",mt))
        pack.append(f"\n\n# {mt}\n\n{strip_html(r['content_html'])}")
        all_urls += readings_from(r["content_html"])
    (OUT/"packs"/f"{slug}-source-pack.md").write_text("\n".join(pack), encoding="utf-8")
    # READINGS
    seen, uniq = set(), []
    for u in all_urls:
        if u not in seen: seen.add(u); uniq.append(u)
    rd = [f"# {title} — cited readings\n",
          "Open-access sources cited across the course. Add to the notebook with:\n",
          "```bash", f"# after `notebooklm login` and creating the notebook:",
          "\n".join(f"python3 scripts/notebooklm-manage.py add-source {slug} {u}" for u in uniq) or "# (none found)",
          "```\n", "## URLs", *[f"- {u}" for u in uniq]]
    (OUT/"readings"/f"{slug}.md").write_text("\n".join(rd), encoding="utf-8")
    # PROMPT
    topics = "; ".join(t for t in mod_titles[:12] if t)
    prompt = f"""# {title} — NotebookLM study-companion prompt

**Course:** {title} (ImpactMojo flagship, {len(rows)} modules). South Asia-first development education for practitioners, students and educators.

## 1. Sources to load
Upload `notebooklm/packs/{slug}-source-pack.md` and add the cited readings in `notebooklm/readings/{slug}.md`.

## 2. Audio Overview steering prompt (paste into NotebookLM's "Customise")
> Create a ~12-minute study-companion overview for a practitioner audience. Ground every concept in the course's South Asian examples and cited evidence — do not invent statistics or cases. Move module by module across: {topics}. For each, give the core idea, one concrete South Asian example from the sources, and one "use it in your work" takeaway. Close with the capstone challenge. Keep the tone rigorous but accessible; define jargon on first use.

## 3. Suggested questions to seed the notebook
- What is the single most important idea in this course, and what evidence supports it?
- Summarise each module in two sentences: the concept and its South Asian application.
- Which cited readings should I go to first, and why?
- Turn the capstone into a step-by-step plan I can apply to my own work.
- Quiz me with 10 questions across the whole course, then mark my answers.
- Where do the sources disagree or leave open questions?

## 4. Wire-up (maintainer)
After creating the notebook, register it: add `{slug}` -> notebook-id to `data/notebooklm-registry.json`,
put the share URL in the course shell's AI Study Companion button, then optionally
`python3 scripts/notebooklm-manage.py generate-audio {slug}`.
"""
    (OUT/"prompts"/f"{slug}.md").write_text(prompt, encoding="utf-8")
    print(f"  {slug}: {len(rows)} modules, {len(uniq)} readings")

def main():
    slugs = sys.argv[1:] or list(TITLES.keys())
    print(f"Building NotebookLM kit for {len(slugs)} flagship(s)...")
    for s in slugs: build(s)
    print("Done. Packs in notebooklm/packs/ (git-ignored); prompts + readings committed.")

if __name__ == "__main__":
    main()
