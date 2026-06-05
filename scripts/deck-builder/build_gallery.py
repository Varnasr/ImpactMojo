#!/usr/bin/env python3
"""
Builds 101-courses/decks.html — a visual gallery landing page for the native
ImpactMojo 101 Series decks. On-brand cards, each with a Sargam line icon.

Run: python3 scripts/deck-builder/build_gallery.py
"""
import os, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "101-courses" / "decks.html"
SARGAM = "https://cdn.jsdelivr.net/npm/sargam-icons@1.6.6/Icons/Line/{}.svg"

# (slug, title, sargam-icon, accent[cyan|indigo|green|amber|red], blurb)
SECTIONS = [
 ("Foundations", "The flagship-depth native decks that started the series.", [
  ("dev-economics","Development Economics 101","si_Bar_chart","cyan","Poverty, growth & structural transformation in the Global South."),
  ("mel-basics","MEL Basics 101","si_Fact_check","green","Monitoring, Evaluation & Learning for development projects."),
  ("climate-essentials","Climate Essentials 101","si_Leaf","green","Climate science, justice & action for practitioners."),
  ("inequality-basics","Inequality Basics 101","si_Activity","red","Measuring and making sense of economic inequality."),
  ("public-finance-budgeting","Public Finance & Budgeting 101","si_Wallet","amber","How governments raise, allocate & account for money."),
  ("social-margins","Social Margins 101","si_Heart","indigo","Identity, inequality & justice across South Asia."),
  ("work-labour-livelihoods","Work, Labour & Livelihoods 101","si_Briefcase","amber","Work, the care economy & sustainable livelihoods."),
 ]),
 ("Data & Methods", "Read, analyse and evaluate evidence with confidence.", [
  ("data-lit","Data Literacy 101","si_Database","cyan","Read, question, visualise & use data responsibly."),
  ("bi-analysis","Bivariate Analysis 101","si_Bar_chart","cyan","Relationships between two variables."),
  ("multivariate-basics","Multivariate Analysis 101","si_Activity","indigo","Regression with many variables; controlling for confounders."),
  ("econometrics-101","Econometrics 101","si_Target","indigo","Causal inference: RCTs, IV, DiD, RDD and panels."),
  ("eda-hhs","Exploratory Data Analysis 101","si_Database","green","Making sense of household survey data."),
  ("irt-basics","Item Response Theory 101","si_Fact_check","indigo","Latent traits & measurement done right."),
  ("qual-methods","Qualitative Methods 101","si_Chat","amber","Interviews, focus groups, ethnography & coding."),
  ("obs2insight","Observation to Insight 101","si_Flare","amber","Turning field observation into insight."),
  ("research-ethics","Research Ethics 101","si_Lock","red","Consent, vulnerability, privacy & do-no-harm."),
  ("cost-effectiveness","Cost Effectiveness 101","si_Wallet","green","Doing the most good per rupee."),
  ("impact-eval","Impact Evaluation 101","si_Check_circle","cyan","Attribution, counterfactuals & rigorous evaluation."),
  ("mixed-methods","Mixed Methods 101","si_Arrow_right","amber","Combining quantitative & qualitative research."),
  ("survey-design","Survey Design 101","si_Fact_check","cyan","Questionnaires, sampling & fieldwork quality."),
 ]),
 ("Gender & Social", "Gender, care, learning and the social fabric.", [
  ("data-feminism","Data Feminism 101","si_Heart","red","Power & data through a feminist lens."),
  ("care-economy-101","Care Economy 101","si_Heart","indigo","The unpaid & paid care that holds up the economy."),
  ("sel-basics","SEL Basics 101","si_Heart","green","Social & emotional learning."),
  ("SRHR-basics","Sexual Health 101","si_Heart","red","Sexual & reproductive health and rights."),
  ("community-dev","Community Development 101","si_Chat","green","Participation, organising & asset-based development."),
  ("edu-pedagogy","Education & Pedagogy 101","si_Book","amber","How learning works; FLN & inclusive pedagogy."),
  ("feminist-research","Feminist Research 101","si_Flare","red","Power, reflexivity & voice in research."),
  ("gender-mainstreaming","Gender Mainstreaming 101","si_Target","indigo","Integrating gender across the programme cycle."),
  ("wee-studies","Women's Economic Empowerment 101","si_Briefcase","red","Resources, agency & achievements."),
 ]),
 ("Health & Childhood", "Public health, maternal care and early childhood.", [
  ("pub-health-basics","Public Health 101","si_Activity","green","Population health, epidemiology & UHC."),
  ("maternal-health","Maternal Health 101","si_Heart","red","Safe pregnancy, birth & the continuum of care."),
  ("child-development","Child Development 101","si_Heart","green","Early childhood development & the first 1,000 days."),
 ]),
 ("Governance & Economy", "The state, institutions and resources.", [
  ("ind-constitution","Indian Constitution 101","si_Flag","cyan","Rights, federalism, the judiciary & the basic structure."),
  ("dev-architecture","Global Development Governance 101","si_Globe_detailed","indigo","The global aid architecture & the SDGs."),
  ("fundraising-basics","Fundraising Basics 101","si_Wallet","amber","Resource mobilisation, CSR & compliance."),
  ("eng-dev","English for Development 101","si_Chat","cyan","Clear professional communication for the sector."),
  ("pol-economy","Political Economy 101","si_Briefcase","indigo","How politics & economics shape development."),
  ("toc-workbench","Theory of Change 101","si_Target","cyan","Causal maps from activity to impact."),
  ("advocacy-basics","Advocacy Basics 101","si_Flag","red","Influencing policy, power & norms."),
  ("bcc-comms","Behaviour Change Communication 101","si_Chat","green","From awareness to action."),
 ]),
 ("Critical & Digital", "Power, ethics, environment and the digital world.", [
  ("decolonize-dev","Decolonial Development 101","si_Globe_detailed","red","Decolonising development thought & practice."),
  ("digital-ethics","Digital Ethics 101","si_Lock","indigo","Data privacy, AI, bias & the digital divide."),
  ("env-justice","Environmental Justice 101","si_Leaf","green","The unequal distribution of environmental harm."),
  ("post-truth-101","Post-Truth Politics 101","si_Info","amber","Mis/disinformation, bias & resilience."),
  ("visual-eth","Visual Ethnography 101","si_Library_books","indigo","Studying culture through images."),
 ]),
]

ACCENT = {"cyan":"#0EA5E9","indigo":"#6366F1","green":"#10B981","amber":"#F59E0B","red":"#EF4444"}


def slide_count(slug):
    f = ROOT / "101-courses" / f"{slug}.html"
    if not f.exists():
        return 100  # 7 new decks: file lands shortly, all 100
    n = len(re.findall(r'id="s\d+"', f.read_text(encoding="utf-8", errors="ignore")))
    return n or 100


def card(slug, title, icon, accent, blurb):
    n = slide_count(slug)
    col = ACCENT[accent]
    return f"""    <a class="deck-card a-{accent}" href="/101-courses/{slug}.html">
      <div class="deck-ico" style="--c:{col}">
        <img src="{SARGAM.format(icon)}" alt="" aria-hidden="true" width="26" height="26">
      </div>
      <div class="deck-body">
        <div class="deck-title">{title}</div>
        <div class="deck-blurb">{blurb}</div>
      </div>
      <div class="deck-foot"><span class="deck-slides">{n} slides</span><span class="deck-cta">Open &rarr;</span></div>
    </a>"""


def main():
    total = sum(len(d) for _, _, d in SECTIONS)
    sections_html = []
    for name, sub, decks in SECTIONS:
        cards = "\n".join(card(*d) for d in decks)
        sections_html.append(
            f'  <section class="deck-section">\n'
            f'    <div class="sec-head"><h2>{name}</h2><span class="sec-count">{len(decks)}</span><p>{sub}</p></div>\n'
            f'    <div class="deck-grid">\n{cards}\n    </div>\n  </section>')
    body = "\n".join(sections_html)
    html = TEMPLATE.replace("{{TOTAL}}", str(total)).replace("{{SECTIONS}}", body)
    OUT.write_text(html, encoding="utf-8")
    print(f"[built] 101-courses/decks.html — {total} deck cards, {len(SECTIONS)} sections")


TEMPLATE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>The ImpactMojo 101 Deck Library — {{TOTAL}} Native Interactive Courses</title>
<meta name="description" content="The ImpactMojo 101 Deck Library — {{TOTAL}} free, native, ~100-slide interactive course decks on development methods, theory and practice for South Asia. CC BY-NC-ND, free forever.">
<meta name="robots" content="index, follow">
<link rel="canonical" href="https://www.impactmojo.in/101-courses/decks.html">
<meta property="og:type" content="website">
<meta property="og:title" content="The ImpactMojo 101 Deck Library">
<meta property="og:description" content="{{TOTAL}} free, native, ~100-slide interactive course decks for development practitioners across South Asia.">
<meta property="og:image" content="https://www.impactmojo.in/assets/images/ImpactMojo%20Logo.png">
<meta property="og:url" content="https://www.impactmojo.in/101-courses/decks.html">
<meta property="og:site_name" content="ImpactMojo">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="The ImpactMojo 101 Deck Library">
<meta name="twitter:description" content="{{TOTAL}} free, native, ~100-slide interactive course decks.">
<meta name="twitter:image" content="https://www.impactmojo.in/assets/images/ImpactMojo%20Logo.png">
<link rel="icon" type="image/png" href="/assets/images/favicon.png">
<script async src="https://www.googletagmanager.com/gtag/js?id=G-JRCMEB9TBW"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag('js',new Date());gtag('config','G-JRCMEB9TBW');</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Amaranth:wght@400;700&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<style>
*,*::before,*::after{margin:0;padding:0;box-sizing:border-box}
:root{
  --cyan:#0EA5E9;--indigo:#6366F1;--green:#10B981;--amber:#F59E0B;--red:#EF4444;
  --ink:#0F172A;--ink-mid:#1E293B;--ink-light:#475569;
  --paper:#FDF8F2;--paper-mid:#F1F5F9;--paper-soft:#FFFFFF;--border:#E2E8F0;
  --font-head:'Inter',system-ui,sans-serif;--font-body:'Amaranth',Georgia,serif;--font-mono:'JetBrains Mono',monospace;
}
@media(prefers-color-scheme:dark){:root{--paper:#0F172A;--paper-mid:#1E293B;--paper-soft:#1E293B;--ink:#F1F5F9;--ink-mid:#CBD5E1;--ink-light:#94A3B8;--border:#334155}}
html,body{font-family:var(--font-body);color:var(--ink);background:var(--paper);line-height:1.55;-webkit-font-smoothing:antialiased}
.im-topbar{position:sticky;top:0;z-index:50;background:var(--paper-soft);border-bottom:1px solid var(--border);padding:14px 28px;display:flex;align-items:center;justify-content:space-between;gap:16px;flex-wrap:wrap}
.im-logo{display:flex;align-items:center;gap:10px;text-decoration:none;color:var(--ink)}
.im-logo svg{width:32px;height:32px}
.im-logo-text{font-family:var(--font-head);font-weight:800;font-size:18px;background:linear-gradient(90deg,#0EA5E9,#6366F1);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;letter-spacing:-0.3px}
.im-nav{display:flex;gap:8px;align-items:center;flex-wrap:wrap}
.im-nav-btn{font-family:var(--font-head);font-size:13px;font-weight:600;color:var(--ink-mid);text-decoration:none;padding:8px 14px;border-radius:7px;border:1px solid transparent;transition:.15s}
.im-nav-btn:hover{background:var(--paper-mid);border-color:var(--border)}
.im-premium-btn{background:linear-gradient(135deg,#F59E0B,#EF4444);color:#fff;border-color:transparent}
.hero{position:relative;padding:74px 28px 56px;background:linear-gradient(135deg,var(--ink) 0%,var(--ink-mid) 100%);color:#fff;overflow:hidden}
.hero::before{content:"";position:absolute;inset:0;background-image:radial-gradient(circle at 22% 28%,rgba(14,165,233,.16) 1px,transparent 1px),radial-gradient(circle at 78% 72%,rgba(99,102,241,.13) 1px,transparent 1px);background-size:78px 78px;opacity:.5}
.hero-in{position:relative;z-index:2;max-width:1180px;margin:0 auto}
.hero-eyebrow{font-family:var(--font-mono);font-size:12px;letter-spacing:3px;text-transform:uppercase;color:#0EA5E9;margin-bottom:14px;font-weight:600}
.hero-title{font-family:var(--font-head);font-size:52px;font-weight:800;line-height:1.04;letter-spacing:-2px;margin-bottom:16px;background:linear-gradient(135deg,#fff 0%,#CBD5E1 100%);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}
.hero-sub{font-family:var(--font-body);font-size:18px;color:rgba(255,255,255,.78);max-width:760px;margin-bottom:26px}
.hero-stats{display:flex;gap:22px;flex-wrap:wrap}
.hstat{background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.14);padding:12px 20px;border-radius:10px;backdrop-filter:blur(10px)}
.hstat b{font-family:var(--font-head);font-size:28px;font-weight:800;color:#0EA5E9;display:block;line-height:1}
.hstat span{font-family:var(--font-mono);font-size:10.5px;letter-spacing:1.4px;text-transform:uppercase;color:rgba(255,255,255,.6)}
main{max-width:1180px;margin:0 auto;padding:44px 24px 20px}
.deck-section{margin-bottom:46px}
.sec-head{display:flex;align-items:baseline;gap:12px;flex-wrap:wrap;margin-bottom:18px;border-bottom:1px solid var(--border);padding-bottom:10px}
.sec-head h2{font-family:var(--font-head);font-size:21px;font-weight:800;letter-spacing:-.4px;color:var(--ink)}
.sec-count{font-family:var(--font-mono);font-size:11px;font-weight:600;color:#fff;background:linear-gradient(135deg,#0EA5E9,#6366F1);padding:2px 9px;border-radius:20px}
.sec-head p{font-family:var(--font-body);font-size:14px;color:var(--ink-light);margin-left:auto}
.deck-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:16px}
.deck-card{position:relative;display:flex;flex-direction:column;gap:12px;background:var(--paper-soft);border:1px solid var(--border);border-radius:14px;padding:18px 18px 14px;text-decoration:none;color:var(--ink);transition:transform .15s ease,box-shadow .15s ease,border-color .15s ease;overflow:hidden}
.deck-card::before{content:"";position:absolute;left:0;top:0;bottom:0;width:4px;background:var(--ac);opacity:.9}
.deck-card.a-cyan{--ac:var(--cyan)}.deck-card.a-indigo{--ac:var(--indigo)}.deck-card.a-green{--ac:var(--green)}.deck-card.a-amber{--ac:var(--amber)}.deck-card.a-red{--ac:var(--red)}
.deck-card:hover{transform:translateY(-3px);box-shadow:0 10px 26px rgba(15,23,42,.1);border-color:var(--ac)}
.deck-ico{width:46px;height:46px;border-radius:11px;display:flex;align-items:center;justify-content:center;background:color-mix(in srgb,var(--c) 14%,transparent);border:1px solid color-mix(in srgb,var(--c) 30%,transparent)}
.deck-ico img{filter:none;opacity:.95}
.deck-body{flex:1}
.deck-title{font-family:var(--font-head);font-size:16px;font-weight:700;letter-spacing:-.3px;line-height:1.25;margin-bottom:6px;color:var(--ink)}
.deck-blurb{font-family:var(--font-body);font-size:13.5px;line-height:1.5;color:var(--ink-mid)}
.deck-foot{display:flex;align-items:center;justify-content:space-between;border-top:1px dashed var(--border);padding-top:10px}
.deck-slides{font-family:var(--font-mono);font-size:10px;letter-spacing:.6px;text-transform:uppercase;color:var(--ink-light)}
.deck-cta{font-family:var(--font-head);font-size:12px;font-weight:700;color:var(--ac)}
.foot{padding:46px 28px 34px;border-top:1px solid var(--border);text-align:center;background:var(--paper-soft)}
.foot-links{display:flex;gap:18px;justify-content:center;flex-wrap:wrap;margin-bottom:18px}
.foot-links a{font-family:var(--font-head);font-size:13px;font-weight:600;color:var(--cyan);text-decoration:none}
.foot-meta{font-family:var(--font-mono);font-size:11px;letter-spacing:1px;color:var(--ink-light);text-transform:uppercase}
@media(max-width:720px){.hero{padding:48px 20px 38px}.hero-title{font-size:36px;letter-spacing:-1.4px}.sec-head p{margin-left:0;flex-basis:100%}main{padding:30px 16px 10px}}
</style>
</head>
<body>
<header class="im-topbar">
  <a href="https://www.impactmojo.in" class="im-logo">
    <svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><path d="M50,150 L150,50 L50,100 L80,130 Z" fill="none" stroke="#0EA5E9" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/><path d="M80,130 L150,50" stroke="#6366F1" stroke-width="2" stroke-dasharray="4,4"/><circle cx="150" cy="50" r="4" fill="#10B981"/></svg>
    <span class="im-logo-text">ImpactMojo</span>
  </a>
  <nav class="im-nav">
    <a class="im-nav-btn" href="https://www.impactmojo.in/">Home</a>
    <a class="im-nav-btn" href="/101-courses/">101 Series</a>
    <a class="im-nav-btn" href="https://www.impactmojo.in/catalog.html">Catalog</a>
    <a class="im-nav-btn im-premium-btn" href="https://www.impactmojo.in/premium.html">Premium</a>
  </nav>
</header>
<section class="hero">
  <div class="hero-in">
    <div class="hero-eyebrow">ImpactMojo 101 Series &middot; Free Forever</div>
    <h1 class="hero-title">The 101 Deck Library</h1>
    <p class="hero-sub">{{TOTAL}} native, interactive, ~100-slide course decks on development methods, theory and practice &mdash; built for South Asia, with charts, diagrams and cited sources throughout. No embeds, no logins, free forever.</p>
    <div class="hero-stats">
      <div class="hstat"><b>{{TOTAL}}</b><span>Native Decks</span></div>
      <div class="hstat"><b>~100</b><span>Slides Each</span></div>
      <div class="hstat"><b>Free</b><span>CC BY-NC-ND</span></div>
    </div>
  </div>
</section>
<main>
{{SECTIONS}}
</main>
<footer class="foot">
  <div class="foot-links">
    <a href="/101-courses/">101 Series Hub</a>
    <a href="https://www.impactmojo.in/#flagship-courses">Flagship Courses</a>
    <a href="https://www.impactmojo.in/catalog.html">Full Catalog</a>
    <a href="https://www.impactmojo.in/about.html">About</a>
  </div>
  <div class="foot-meta">CC BY-NC-ND 4.0 &middot; Free Forever &middot; ImpactMojo</div>
</footer>
</body>
</html>
"""

if __name__ == "__main__":
    main()
