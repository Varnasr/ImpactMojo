#!/usr/bin/env python3
"""Reorder a studio's tabs so the BUILD tab is tab 1 (build-first).

Reuses the DPI approach: make switchTab resolve by data-panel/data-target
(not DOM order) via a minimal `i = <data-attr>` rebind injected into the two
existing forEach loops, then reorder the tab BUTTONS, renumber data-panel,
and remap nav switchTab() targets. Panels stay physically in place.

Usage: reorder-studio.py <file> <build_old_idx> [--keep-last N]
  build_old_idx : the current data-panel index of the build/make tab
  --keep-last N : old index of a wrap-up tab (e.g. Done) to keep last
"""
import re, sys

def main():
    f=sys.argv[1]; build=int(sys.argv[2])
    keep_last=None
    if "--keep-last" in sys.argv:
        keep_last=int(sys.argv[sys.argv.index("--keep-last")+1])
    s=open(f,encoding="utf-8").read()

    # discover tab buttons in order -> (label_html, old_idx)
    btn_re=re.compile(r'<button[^>]*class="tab-btn[^"]*"[^>]*onclick="switchTab\((\d+)\)"[^>]*>(.*?)</button>', re.S)
    btns=[(int(m.group(1)), m.group(2)) for m in btn_re.finditer(s)]
    N=len(btns)
    if N<2: sys.exit("no tab buttons found")
    old_order=[b[0] for b in btns]
    label={i:re.sub(r'<span class="tab-num">.*?</span>\s*','',lab,flags=re.S).strip() for i,lab in btns}

    # new order: build first, then the rest in original order, keep_last last
    rest=[i for i in old_order if i!=build and i!=keep_last]
    new_order=[build]+rest+([keep_last] if keep_last is not None else [])
    assert sorted(new_order)==sorted(old_order), (new_order, old_order)
    o2n={old:new for new,old in enumerate(new_order)}   # old idx -> new idx

    # 1) make button matching data-driven via a minimal i-rebind (both fn and arrow forms)
    before=s
    for pat in (r"(querySelectorAll\('\.tab-btn'\)[.\s\S]{0,40}?\.forEach\(function\(b,\s*i\)\s*\{)",
                r"(querySelectorAll\('\.tab-btn'\)[.\s\S]{0,40}?\.forEach\(\(b,\s*i\)\s*=>\s*\{)",
                r"(\bbtns\.forEach\(\(b,\s*i\)\s*=>\s*\{)",
                r"(\bbtns\.forEach\(function\(b,\s*i\)\s*\{)"):
        s2=re.sub(pat, r"\1 i = parseInt(b.getAttribute('data-target'),10);", s, count=1)
        if s2!=s: s=s2; break
    btn_ok = s!=before
    # panel matching: inject rebind if it iterates panels by index; skip if it already
    # selects panels by [data-panel="..."] (already data-driven)
    already_panel = "tab-panel[data-panel=" in s
    if not already_panel:
        for pat in (r"(querySelectorAll\('\.tab-panel'\)\.forEach\(function\(p,\s*i\)\s*\{)",
                    r"(querySelectorAll\('\.tab-panel'\)\.forEach\(\(p,\s*i\)\s*=>\s*\{)"):
            s2=re.sub(pat, r"\1 i = parseInt(p.getAttribute('data-panel'),10);", s, count=1)
            if s2!=s: s=s2; break
    if not btn_ok and not already_panel:
        sys.exit("ERROR: could not make switchTab data-driven (shape differs) — handle manually")

    # 2) rebuild the tab buttons block in NEW order (tab-num, switchTab, data-target, active on build)
    tabs_block=re.search(r'(<div class="tabs"[^>]*>)(.*?)(</div>)', s, re.S)
    head,_,tail=tabs_block.group(1),tabs_block.group(2),tabs_block.group(3)
    new_btns=[]
    for new_idx,old_idx in enumerate(new_order):
        lab=label[old_idx]
        active=" active" if new_idx==0 else ""
        new_btns.append(f'        <button class="tab-btn{active}" data-target="{new_idx}" onclick="switchTab({new_idx})"><span class="tab-num">{new_idx+1}</span> {lab}</button>')
    s=s[:tabs_block.start()]+head+"\n"+"\n".join(new_btns)+"\n    "+tail+s[tabs_block.end():]

    # 3) renumber data-panel via o2n (simultaneous)
    s=re.sub(r'data-panel="(\d+)"', lambda m:f'data-panel="{o2n[int(m.group(1))]}"', s)

    # 4) set active class on the build panel, remove from others
    def panel_active(m):
        cls=m.group(1); dp=int(m.group(2))
        cls=re.sub(r'\s*active','',cls)
        if dp==0: cls=cls+" active"
        return f'class="{cls.strip()}" data-panel="{dp}"'
    s=re.sub(r'class="(tab-panel[^"]*)"\s+data-panel="(\d+)"', panel_active, s)

    # 5) remap nav-row switchTab() calls (buttons NOT in the tabs bar) via o2n
    #    (the tabs bar buttons were rebuilt with explicit new indices already)
    tabs_now=re.search(r'<div class="tabs"[^>]*>.*?</div>', s, re.S).span()
    def remap_nav(m):
        start=m.start()
        if tabs_now[0]<=start<tabs_now[1]: return m.group(0)   # skip the tab bar
        return f'switchTab({o2n[int(m.group(1))]})'
    s=re.sub(r'switchTab\((\d+)\)', remap_nav, s)

    open(f,"w",encoding="utf-8").write(s)
    print(f"OK {f}: build '{label[build]}' -> tab 1. new order:",
          [label[i][:22] for i in new_order])

if __name__=="__main__":
    main()
