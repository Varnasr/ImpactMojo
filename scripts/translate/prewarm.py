#!/usr/bin/env python3
"""Pre-warm the production translation cache for high-traffic pages so they
translate instantly. Extracts each page's translatable strings (same rules as
the client) and POSTs them to the live /api/translate for each language, which
populates the Netlify Blobs cache. Re-running is free (cache hits).
Usage: python3 scripts/translate/prewarm.py [page ...]"""
import sys, json, re, time, urllib.request
from bs4 import BeautifulSoup, NavigableString, Comment
BASE="https://www.impactmojo.in/api/translate"
LANGS=["hi","ta","bn","mr"]
SKIP={"script","style","svg","path","symbol","defs","canvas","noscript","code","pre","textarea"}
KEEP={"ImpactMojo","ImpactLex","VaniScribe","Mojini","PinPoint Ventures","Dataverse"}
def translatable(n):
    if not isinstance(n,NavigableString) or isinstance(n,Comment): return False
    s=str(n).strip()
    if len(s)<2 or s in KEEP or not re.search(r"[A-Za-z]",s): return False
    if re.match(r"^(https?://|www\.|\S+@\S+)",s): return False
    for p in n.parents:
        if p.name in SKIP: return False
        if p.has_attr and (p.get("data-no-translate") is not None or p.get("translate")=="no"): return False
    return True
def strings(path):
    soup=BeautifulSoup(open(path,encoding="utf-8",errors="ignore").read(),"html.parser")
    body=soup.body or soup
    seen=set(); out=[]
    for n in body.find_all(string=True):
        if translatable(n):
            s=str(n).strip()
            if s not in seen: seen.add(s); out.append(s)
    return out
def warm(lang,batch):
    body=json.dumps({"lang":lang,"q":batch}).encode()
    req=urllib.request.Request(BASE,data=body,method="POST",headers={"Content-Type":"application/json"})
    for a in range(4):
        try:
            with urllib.request.urlopen(req,timeout=120) as r: return len(json.loads(r.read()).get("t",{}))
        except Exception as e:
            if a==3: print("   ! batch failed:",str(e)[:60]); return 0
            time.sleep(2*(a+1))
PAGES=sys.argv[1:] or [
 "index.html","catalog.html","premium.html","about.html","faq.html","blog.html",
 "dojos.html","handouts.html","dataverse.html","podcast.html","contact.html","workshops.html",
 "101-courses/index.html","101-courses/decks.html","BookSummaries/index.html",
 "specials/marginalia/index.html","specials/the-indicator-ate-the-village/index.html",
 "courses/causal/index.html","courses/mel/index.html","101-courses/data-lit.html",
]
total=0
for pg in PAGES:
    try: ss=strings(pg)
    except FileNotFoundError: print("  (missing)",pg); continue
    print(f"{pg}: {len(ss)} unique strings × {len(LANGS)} langs")
    for lang in LANGS:
        for i in range(0,len(ss),12):
            warm(lang,ss[i:i+12]); total+=min(12,len(ss)-i); time.sleep(0.25)
print(f"\nwarmed ~{total} (string×lang) cache entries across {len(PAGES)} pages")
