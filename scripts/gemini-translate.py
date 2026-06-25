#!/usr/bin/env python3
"""Glossary-aware machine translation of per-page i18n dictionaries via Gemini.

A fallback/companion to bulk-translate.py (which uses the Sarvam-backed
/api/translate endpoint). When Sarvam is unavailable, this generates the same
per-page static dictionaries — i18n/pages/<lang>/<pageKey>.json — by mirroring
the source-string keys of a reference language (default: hi) and translating
each English key into the target language with Gemini.

Quality controls:
  * Protected-terms glossary (data/i18n-glossary.json keep_verbatim) is injected
    into the prompt so brand names, software, acronyms and author surnames pass
    through verbatim in Latin script.
  * Batched JSON-array output with strict length validation; any batch whose
    shape doesn't match falls back to one-string-at-a-time.
  * Resumable: keys already present in the target file are skipped, and a global
    in-run cache dedups strings repeated across pages.
  * Output is checked by scripts/check-i18n-quality.py downstream.

The GEMINI_API_KEY is read from the environment — never hard-code it.

Usage:
  GEMINI_API_KEY=... python3 scripts/gemini-translate.py te --ref hi
  GEMINI_API_KEY=... python3 scripts/gemini-translate.py te --ref hi --only index
"""
import os, sys, json, glob, time, argparse, urllib.request, urllib.error

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KEY = os.environ.get("GEMINI_API_KEY", "")
MODELS = ["gemini-2.5-flash", "gemini-2.5-flash-lite"]  # primary, fallback
LANG_NAME = {"te": "Telugu", "hi": "Hindi", "ta": "Tamil", "bn": "Bengali", "mr": "Marathi"}
MAX_BATCH_N = 18
MAX_BATCH_CHARS = 1400
RPM_SLEEP = 6.0  # stay under the ~10 req/min free-tier limit of gemini-2.5-flash


def glossary_terms():
    try:
        g = json.load(open(os.path.join(ROOT, "data", "i18n-glossary.json"), encoding="utf-8"))
    except Exception:
        return []
    kv = g.get("keep_verbatim", {})
    terms = []
    for v in kv.values():
        if isinstance(v, list):
            terms += [t for t in v if isinstance(t, str)]
    # de-dup, keep order
    seen, out = set(), []
    for t in terms:
        if t not in seen:
            seen.add(t); out.append(t)
    return out


def call(model, prompt):
    url = ("https://generativelanguage.googleapis.com/v1beta/models/"
           f"{model}:generateContent?key={KEY}")
    data = {"contents": [{"parts": [{"text": prompt}]}],
            "generationConfig": {"temperature": 0.2}}
    req = urllib.request.Request(url, data=json.dumps(data).encode(),
                                 headers={"Content-Type": "application/json"})
    # Fail-fast: at most 3 attempts with short backoff. A 429/503 storm must NOT
    # turn into a multi-minute stall — give up quickly and let the key be retried
    # on a later run (omitted keys, not English, are written).
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=45) as r:
                d = json.load(r)
            return d["candidates"][0]["content"]["parts"][0]["text"]
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 503) and attempt < 2:
                time.sleep(5); continue
            return None
        except Exception:
            if attempt < 2:
                time.sleep(3); continue
    return None


GLOSS = glossary_terms()


def prompt_for(strings, lang):
    name = LANG_NAME.get(lang, lang)
    keep = ", ".join(GLOSS)
    arr = json.dumps(strings, ensure_ascii=False)
    return (
        f"You are a professional {name} translator localizing a development-education "
        f"website for South Asian learners. Translate each English string in the JSON "
        f"array below into natural, fluent {name}.\n"
        f"RULES:\n"
        f"- Keep these terms EXACTLY as written, in Latin script, never translated or "
        f"transliterated: {keep}.\n"
        f"- Also keep verbatim: the brand 'ImpactMojo', any author surnames, acronyms "
        f"(MEL, NGO, UPI, FAQ, UN, IT, AI, PDF), URLs, emails, numbers and the '101' label.\n"
        f"- Preserve leading/trailing punctuation and symbols (:, →, ←, •, ·, ©, ✓, %) and "
        f"any &amp; entities exactly.\n"
        f"- Use only {name} script for translated words; do not mix other Indic scripts.\n"
        f"- Do NOT add notes, quotes, or a 'text:' prefix.\n"
        f"Return ONLY a JSON array of the translations, same length and order as the input.\n"
        f"INPUT:\n{arr}"
    )


def parse_array(txt, n):
    if txt is None:
        return None
    s = txt.strip()
    if s.startswith("```"):
        s = s.split("\n", 1)[1] if "\n" in s else s
        s = s.rsplit("```", 1)[0]
    i, j = s.find("["), s.rfind("]")
    if i < 0 or j < 0:
        return None
    try:
        arr = json.loads(s[i:j + 1])
    except Exception:
        return None
    if isinstance(arr, list) and len(arr) == n and all(isinstance(x, str) for x in arr):
        return [x.strip() for x in arr]
    return None


FAILED = set()  # strings that failed this run — omitted (retried on a later run)


def translate_many(strings, lang, cache, log):
    todo = [s for s in strings if s not in cache and s not in FAILED]
    # batch by count + char budget
    batches, cur, curlen = [], [], 0
    for s in todo:
        if cur and (len(cur) >= MAX_BATCH_N or curlen + len(s) > MAX_BATCH_CHARS):
            batches.append(cur); cur, curlen = [], 0
        cur.append(s); curlen += len(s)
    if cur:
        batches.append(cur)

    for bi, batch in enumerate(batches):
        out = None
        for model in MODELS:
            res = parse_array(call(model, prompt_for(batch, lang)), len(batch))
            if res:
                out = res; break
        if out is None:
            # per-string fallback (single attempt per model); on failure OMIT the
            # string (record in FAILED) rather than baking in English.
            out = []
            for s in batch:
                r = None
                for model in MODELS:
                    r = parse_array(call(model, prompt_for([s], lang)), 1)
                    if r:
                        break
                out.append(r[0] if r else None)
                time.sleep(RPM_SLEEP)
        for s, t in zip(batch, out):
            if t is None:
                FAILED.add(s)
            else:
                cache[s] = t
        if bi % 5 == 0:
            log(f"  batch {bi+1}/{len(batches)} ({len(cache)} cached, {len(FAILED)} failed)")
        time.sleep(RPM_SLEEP)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("lang")
    ap.add_argument("--ref", default="hi")
    ap.add_argument("--only", default=None, help="only this pageKey")
    args = ap.parse_args()
    if not KEY:
        print("ERROR: GEMINI_API_KEY not set in environment"); sys.exit(2)

    def log(m):
        print(m, flush=True)

    ref_dir = os.path.join(ROOT, "i18n", "pages", args.ref)
    out_dir = os.path.join(ROOT, "i18n", "pages", args.lang)
    os.makedirs(out_dir, exist_ok=True)
    files = sorted(glob.glob(os.path.join(ref_dir, "*.json")))
    if args.only:
        files = [f for f in files if os.path.basename(f) == args.only + ".json"]

    cache = {}
    # seed cache from common dict + already-built target page files (resume)
    common = os.path.join(ROOT, "i18n", args.lang + ".json")
    if os.path.exists(common):
        cache.update(json.load(open(common, encoding="utf-8")))
    for f in glob.glob(os.path.join(out_dir, "*.json")):
        try:
            cache.update(json.load(open(f, encoding="utf-8")))
        except Exception:
            pass

    for f in files:
        name = os.path.basename(f)
        src = json.load(open(f, encoding="utf-8"))
        keys = list(src.keys())
        log(f"[{name}] {len(keys)} strings")
        translate_many(keys, args.lang, cache, log)
        # Only write keys we actually translated; omit failures so a later run
        # retries them (and the runtime live-fallback covers them meanwhile).
        out = {k: cache[k] for k in keys if k in cache}
        json.dump(out, open(os.path.join(out_dir, name), "w", encoding="utf-8"),
                  ensure_ascii=False, indent=2, sort_keys=True)
        missing = sum(1 for k in keys if k not in cache)
        log(f"[{name}] wrote {len(out)}" + (f" ({missing} deferred)" if missing else ""))
    log("DONE")


if __name__ == "__main__":
    main()
