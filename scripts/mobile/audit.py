#!/usr/bin/env python3
"""
Mobile-first audit for ImpactMojo. Renders pages in headless Chromium at a
phone viewport and flags horizontal overflow (the #1 "ugly on mobile" killer).

Usage:
  pip install playwright && python3 -m playwright install chromium
  python3 scripts/mobile/audit.py [glob ...]        # default: key pages
Exit code 1 if any page overflows — suitable as a CI gate.
"""
import sys, os, glob, threading, functools, http.server, socketserver
from playwright.sync_api import sync_playwright

def _serve(port):
    class Q(http.server.SimpleHTTPRequestHandler):
        def log_message(self,*a):pass
    h=Q
    httpd=socketserver.TCPServer(('127.0.0.1',port),h); httpd.daemon_threads=True
    threading.Thread(target=httpd.serve_forever,daemon=True).start(); return httpd

DEFAULT = [
 'index.html','catalog.html','premium.html','about.html','blog.html','dojos.html',
 'handouts.html','dataverse.html','faq.html','contact.html','game-library.html',
 'workshops.html','testimonials.html','login.html','signup.html','account.html',
 'upgrade.html','portfolio.html','coaching.html','sitemap.html','fundamentals/wheel.html','fundamentals/index.html',
 '101-courses/index.html','101-courses/decks.html',
 'courses/causal/index.html','courses/mel/index.html','courses/gender/index.html',
 'BookSummaries/index.html','specials/marginalia/index.html',
 'specials/the-indicator-ate-the-village/index.html',
]
VIEWPORT={'width':390,'height':844}
PORT=8137
BASE='http://127.0.0.1:%d/'%PORT

def audit(pages):
    bad=[]
    httpd=_serve(PORT)
    with sync_playwright() as p:
        b=p.chromium.launch()
        for rel in pages:
            if not os.path.exists(rel): continue
            pg=b.new_page(viewport=VIEWPORT, device_scale_factor=2)
            try:
                try:
                    pg.goto(BASE+rel, wait_until='load', timeout=15000)
                except Exception:
                    pg.goto(BASE+rel, wait_until='domcontentloaded', timeout=15000)
                pg.wait_for_timeout(1200)
                d=pg.evaluate("""()=>{const iw=innerWidth,dw=document.documentElement.scrollWidth,o=[];
                  if(dw>iw+2){document.querySelectorAll('body *').forEach(el=>{const r=el.getBoundingClientRect();
                    if(r.right>iw+2&&r.width>40){const c=getComputedStyle(el);if(c.display==='none')return;
                    o.push((el.tagName+(el.id?'#'+el.id:'')+(typeof el.className==='string'&&el.className?'.'+el.className.trim().split(/\\s+/)[0]:'')).toLowerCase())}})}
                  return {dw,iw,over:[...new Set(o)].slice(0,5)}}""")
                status='ok' if d['dw']<=d['iw']+2 else 'OVERFLOW'
                print(f"  {'❌' if status=='OVERFLOW' else '·'} {rel:44s} scrollW={d['dw']}  {d['over'] if status=='OVERFLOW' else ''}")
                if status=='OVERFLOW': bad.append(rel)
            finally:
                pg.close()
        b.close()
    return bad

if __name__=='__main__':
    pats=sys.argv[1:] or DEFAULT
    pages=[]
    for pat in pats: pages += sorted(glob.glob(pat)) if any(c in pat for c in '*?[') else [pat]
    print(f"Mobile overflow audit @ {VIEWPORT['width']}px — {len(pages)} pages")
    bad=audit(pages)
    print(f"\n{'❌ '+str(len(bad))+' page(s) overflow' if bad else '✅ no horizontal overflow'}")
    sys.exit(1 if bad else 0)
