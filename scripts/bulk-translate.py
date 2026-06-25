#!/usr/bin/env python3
"""Bulk pre-translate page text through the deployed /api/translate endpoint
(Sarvam Mayura, Netlify-Blobs-cached) and store the results as PER-PAGE static
dictionaries at i18n/pages/<lang>/<pageKey>.json.

Each unique string is translated once (server-side Blobs cache dedups across
runs too, so re-running is cheap). The client (js/translate-sarvam.js) loads the
shared common dict i18n/<lang>.json plus the page's own file, so no page ever
downloads more than its own strings.

Usage:
  python3 scripts/bulk-translate.py <glob> [<glob> ...]
  e.g. python3 scripts/bulk-translate.py index.html 'courses/**/*.html'

Resumable: strings already present in a per-page file (or the common dict) are
skipped. Identity "translations" (Sarvam returned the source unchanged) are not
stored, so they get retried on a later run / by the live fallback.
"""
import sys, os, re, glob, json, time, urllib.request, urllib.error
from concurrent.futures import ThreadPoolExecutor
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
API = "https://www.impactmojo.in/api/translate"
LANGS = ["hi", "ta", "bn", "mr", "te"]
BATCH = 12
WORKERS = 3        # keep total Sarvam concurrency modest to avoid rate limits
PASSES = 3         # re-attempt strings that came back untranslated (rate-limited)

SKIP = {"script","style","noscript","svg","code","pre","kbd","samp","canvas","textarea","option"}
KEEP = {"ImpactMojo","ImpactLex","VaniScribe","Mojini","PinPoint Ventures","DevDiscourses","Dataverse","Bulbul","Mayura","Saaras"}


class Ex(HTMLParser):
    def __init__(self):
        super().__init__(); self.skip = 0; self.out = []
    def handle_starttag(self, t, a):
        if t in SKIP: self.skip += 1
        d = dict(a)
        if d.get("data-no-translate") is not None or d.get("translate") == "no": self.skip += 1
    def handle_endtag(self, t):
        if t in SKIP and self.skip > 0: self.skip -= 1
    def handle_data(self, d):
        if self.skip > 0: return
        x = d.strip()
        if len(x) < 2 or x in KEEP or not re.search(r"[A-Za-z]", x) or re.match(r"^(https?://|www\.|\S+@)", x):
            return
        self.out.append(x)


def page_key(relpath):
    p = relpath.replace(os.sep, "/")
    p = re.sub(r"/index\.html?$", "", p, flags=re.I)
    p = re.sub(r"\.html?$", "", p, flags=re.I)
    p = p.strip("/")
    if not p:
        p = "index"
    return re.sub(r"[^A-Za-z0-9._-]+", "__", p)


def extract(path):
    p = Ex()
    try:
        p.feed(open(path, encoding="utf-8", errors="ignore").read())
    except Exception:
        return []
    seen, out = set(), []
    for s in p.out:
        if s not in seen:
            seen.add(s); out.append(s)
    return out


def api_call(lang, batch):
    body = json.dumps({"lang": lang, "q": batch}).encode()
    req = urllib.request.Request(API, data=body, headers={"Content-Type": "application/json"}, method="POST")
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.loads(r.read().decode()).get("t", {})
        except Exception:
            time.sleep(1.5 * (attempt + 1))
    return {}


def main():
    globs = sys.argv[1:] or ["index.html"]
    pages = []
    for g in globs:
        for f in glob.glob(os.path.join(ROOT, g), recursive=True):
            rel = os.path.relpath(f, ROOT)
            if rel.startswith("Backups/") or rel.startswith("Handouts/"):
                continue
            if rel.endswith(".html"):
                pages.append(rel)
    pages = sorted(set(pages))
    print(f"Target pages: {len(pages)}")

    # common dict keys (loaded everywhere by the client) — skip these per-page
    common = set(json.load(open(os.path.join(ROOT, "i18n", "hi.json"), encoding="utf-8")).keys())

    page_strings = {}
    allstr = set()
    for rel in pages:
        ss = [s for s in extract(os.path.join(ROOT, rel)) if s not in common]
        page_strings[rel] = ss
        allstr.update(ss)
    print(f"Unique strings to cover (excl. common): {len(allstr):,}")

    for lang in LANGS:
        tr = {}  # src -> translation (seed from existing per-page files = resume)
        pdir = os.path.join(ROOT, "i18n", "pages", lang)
        os.makedirs(pdir, exist_ok=True)
        for rel in pages:
            fp = os.path.join(pdir, page_key(rel) + ".json")
            if os.path.exists(fp):
                try: tr.update(json.load(open(fp, encoding="utf-8")))
                except Exception: pass
        print(f"[{lang}] {len(tr):,} known, {len(allstr) - len(tr):,} to translate")
        for p in range(PASSES):
            missing = [s for s in allstr if s not in tr]
            if not missing:
                break
            batches = [missing[i:i + BATCH] for i in range(0, len(missing), BATCH)]
            done = 0
            with ThreadPoolExecutor(max_workers=WORKERS) as ex:
                for b, t in ex.map(lambda b: (b, api_call(lang, b)), batches):
                    for k in b:
                        v = t.get(k)
                        if v and v != k:   # store only real translations
                            tr[k] = v
                    done += 1
                    if done % 25 == 0:
                        print(f"  [{lang}] pass {p+1}: {done}/{len(batches)} batches")
            print(f"  [{lang}] pass {p+1} done — {len(tr):,}/{len(allstr):,} translated")
            time.sleep(2)

        # write per-page files (only this page's strings, only what we have)
        written = 0
        for rel in pages:
            out = {s: tr[s] for s in page_strings[rel] if s in tr}
            if not out:
                continue
            fp = os.path.join(pdir, page_key(rel) + ".json")
            with open(fp, "w", encoding="utf-8") as f:
                json.dump(out, f, ensure_ascii=False, separators=(",", ":"), sort_keys=True)
            written += 1
        print(f"[{lang}] wrote {written} per-page files")


if __name__ == "__main__":
    main()
