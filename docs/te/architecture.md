# ఆర్కిటెక్చర్

> **ఈ పేజీ ఎవరి కోసం?** ఈ పేజీ ప్రధానంగా డెవలపర్‌లు మరియు సాంకేతిక సహకారుల కోసం. మీరు ఉపాధ్యాయుడు లేదా అభ్యాసకుడైతే, కీలక అంశం కింద "ఇది వినియోగదారులకు ఏమి అర్థం" విభాగంలో ఉంది — మీరు సాంకేతిక వివరాలను దాటవేయవచ్చు.

## ఇది వినియోగదారులకు ఏమి అర్థం

ImpactMojo దక్షిణాసియాలోని అభ్యాసకుల కోసం రూపొందించబడింది, వీరిలో చాలా మంది నెమ్మదైన ఇంటర్నెట్ కనెక్షన్లు లేదా పాత పరికరాలలో ఉన్నారు. మా సాంకేతిక ఎంపికలు మీ అనుభవానికి ఏమి అర్థమో ఇక్కడ ఉంది:

- **వేగవంతమైన లోడింగ్** — సైట్ సరళమైన, తేలికపాటి కోడ్‌తో నిర్మించబడింది (భారీ చట్రాలు లేవు). 2G/3G కనెక్షన్లలో కూడా పేజీలు త్వరగా లోడ్ అవుతాయి.
- **ఆఫ్‌లైన్‌లో పనిచేస్తుంది** — మీరు ఒక పేజీని సందర్శించిన తర్వాత, అది మీ పరికరంలో సేవ్ చేయబడుతుంది. మీరు ఇంటర్నెట్ కనెక్షన్ లేకుండా ఫ్లాగ్‌షిప్ కోర్సులను యాక్సెస్ చేయవచ్చు.
- **ఇన్‌స్టాలేషన్ అవసరం లేదు** — ప్రతిదీ మీ వెబ్ బ్రౌజర్‌లో నడుస్తుంది. డౌన్‌లోడ్ చేయడానికి యాప్‌లు లేవు, ఇన్‌స్టాల్ చేయడానికి సాఫ్ట్‌వేర్ లేదు.
- **మీ డేటా సురక్షితం** — లాగిన్ మరియు ఖాతా డేటా Supabase (ఒక నమ్మదగిన డేటాబేస్ సేవ) చే నిర్వహించబడతాయి. ప్రీమియం సాధనాలు సమయ-పరిమిత భద్రతా టోకెన్లను ఉపయోగిస్తాయి, కాబట్టి మీ యాక్సెస్ దొంగిలించబడదు.
- **ఏ పరికరంలోనైనా పనిచేస్తుంది** — ఫోన్, టాబ్లెట్, ల్యాప్‌టాప్, డెస్క్‌టాప్ — పాత లేదా కొత్త. ఆధునిక హార్డ్‌వేర్ అవసరమైన సాంకేతికతలను మేము ఉద్దేశపూర్వకంగా నివారిస్తాము.

## సాంకేతిక అవలోకనం

ImpactMojo ఒక బిల్డ్ దశ లేని స్టాటిక్ HTML/CSS/JS సైట్, ప్రామాణీకరణ కోసం Supabase మరియు హోస్టింగ్ కోసం Netlify చే మద్దతు ఇవ్వబడుతుంది. ప్రీమియం సాధనాలు ప్రత్యేక Netlify సైట్‌లుగా విస్తరించబడ్డాయి, ప్రతి ఒక్కటి ఒక JWT auth-gate చే రక్షించబడింది.

## సిస్టమ్ రేఖాచిత్రం

```
┌──────────────────────────────────────────────────────────┐
│                    impactmojo.in                         │
│                  (Netlify — main site)                   │
│                                                          │
│  index.html ─── js/auth.js ──── Supabase Auth            │
│                 js/router.js    (login, signup, profiles) │
│                 js/premium.js                             │
│                 js/resource-launch.js                     │
└──────────┬───────────────────────────────────────────────┘
           │
           │ User clicks premium tool
           ▼
┌──────────────────────────────────────────────────────────┐
│        Supabase Edge Function                            │
│        mint-resource-token                               │
│                                                          │
│  1. Verify user session (access_token)                   │
│  2. Check subscription_tier in profiles table            │
│  3. Check subscription_status = 'active'                 │
│  4. Verify tier permits requested resource               │
│  5. Mint short-lived JWT (5 min, HMAC-SHA256)            │
└──────────┬───────────────────────────────────────────────┘
           │
           │ window.open(resourceUrl + '?token=...')
           ▼
┌──────────────────────────────────────────────────────────┐
│        Resource Site (private Netlify deployment)          │
│        Netlify Edge Function: auth-gate.ts               │
│                                                          │
│  1. Check for resource_session cookie                     │
│  2. If no cookie, check ?token= query parameter          │
│  3. Verify JWT signature (same HMAC secret)              │
│  4. Verify resource claim matches RESOURCE_ID            │
│  5. Set 24h session cookie, redirect to clean URL        │
│                                                          │
│  No cookie + no token → redirect to login                │
└──────────────────────────────────────────────────────────┘
```

## కీలక రూపకల్పన నిర్ణయాలు

### చట్రం ఎందుకు లేదు?

ImpactMojo దక్షిణాసియాలోని అభ్యాసకులకు సేవలందిస్తుంది, చాలా మంది తక్కువ-బ్యాండ్‌విడ్త్ కనెక్షన్లు మరియు పాత పరికరాలలో ఉన్నారు. ఒక వానిలా HTML/CSS/JS సైట్:
- సున్నా JS బండిల్ ఓవర్‌హెడ్‌తో వేగంగా లోడ్ అవుతుంది
- పాలీఫిల్‌లు లేకుండా ఏ బ్రౌజర్‌లోనైనా పనిచేస్తుంది
- బిల్డ్ దశ లేకుండా ఒక స్టాటిక్ సైట్‌గా అందించవచ్చు
- అర్థం చేసుకోవడం మరియు సహకరించడం సులభం

### ప్రీమియం సాధనాల కోసం ప్రత్యేక Netlify సైట్‌లు ఎందుకు?

ప్రతి ప్రీమియం సాధనం (VaniScribe, Qual Lab, మొదలైనవి) స్వతంత్రంగా నిర్మించబడింది. వాటిని ప్రత్యేక సైట్‌లుగా హోస్ట్ చేయడం:
- స్వతంత్ర విస్తరణ మరియు మెరుగుదలను అనుమతిస్తుంది
- వైఫల్యాలను వేరు చేస్తుంది — ఒక సాధనం డౌన్ కావడం ఇతరులను ప్రభావితం చేయదు
- JWT auth-gate ను సరళంగా చేస్తుంది: ఒక్కో సైట్‌కు ఒక ఎడ్జ్ ఫంక్షన్
- వేర్వేరు బృందాలు వేర్వేరు సాధనాలను కలిగి ఉండటానికి అనుమతిస్తుంది

### సెషన్-ఆధారిత ప్రామాణీకరణ కంటే JWT ఎందుకు?

- **స్టేట్‌లెస్:** ప్రతి వనరు సైట్ అభ్యర్థనపై డేటాబేస్ శోధన లేదు
- **క్రాస్-డొమైన్:** ప్రధాన సైట్ మరియు వనరు సైట్‌లు వేర్వేరు డొమైన్లలో ఉన్నాయి
- **స్వల్ప-కాలం:** 5-నిమిషాల టోకెన్లు అడ్డగించబడితే బహిర్గతతను పరిమితం చేస్తాయి
- **సెషన్ కుకీలు:** ప్రారంభ JWT ధృవీకరణ తర్వాత, ఒక 24h కుకీ మళ్లీ-ప్రామాణీకరణను నివారిస్తుంది

### Supabase ఎందుకు?

- ఉచిత శ్రేణి మా ప్రామాణీకరణ అవసరాలను కవర్ చేస్తుంది
- ప్రొఫైల్‌ల కోసం అంతర్నిర్మిత Row Level Security
- సర్వర్‌లెస్ JWT మింటింగ్ కోసం Edge Functions
- నిర్మాణాత్మక డేటా కోసం PostgreSQL
- Google OAuth + Magic Links ప్రారంభంలోనే

## పర్యావరణ వేరియబుల్స్

### ప్రధాన సైట్ (impactmojo.in)
సర్వర్-సైడ్ env వేరియబుల్స్ అవసరం లేదు — Supabase ఆధారాలు `js/auth.js` లో ఉన్నాయి (పబ్లిక్ anon key మాత్రమే).

### Supabase Edge Function (mint-resource-token)
| వేరియబుల్ | వివరణ |
|----------|-------------|
| `RESOURCE_TOKEN_SECRET` | JWTల కోసం HMAC-SHA256 సంతకం కీ |
| `SUPABASE_URL` | Supabase చే స్వయంచాలకంగా అందించబడింది |
| `SUPABASE_ANON_KEY` | Supabase చే స్వయంచాలకంగా అందించబడింది |
| `SUPABASE_SERVICE_ROLE_KEY` | స్వయంచాలకంగా అందించబడింది; RLS ను దాటవేసి profiles ను చదువుతుంది |

### వనరు Netlify సైట్‌లు (ఒక్కో సైట్‌కు)
| వేరియబుల్ | వివరణ |
|----------|-------------|
| `RESOURCE_TOKEN_SECRET` | పైన ఉన్న అదే HMAC కీ |
| `RESOURCE_ID` | ప్రత్యేక స్లగ్: `rq-builder`, `toc-workbench-pro`, `code-convert-pro`, `qual-insights`, `vaniscribe`, `devdata-practice`, `viz-cookbook`, `devecon-toolkit`, `field-notes-pro`, `toc-workshop-pro`, `logframe-pro`, `chart-selector-pro`, `stakeholder-pro`, `empathy-pro`, `policy-canvas-pro`, `ai-canvas-pro` |

## శ్రేణి యాక్సెస్ నియంత్రణ

```
explorer:      []  (free content only)
practitioner:  [rq-builder, toc-workbench-pro]
professional:  [rq-builder, toc-workbench-pro, code-convert-pro, qual-insights, vaniscribe,
                devdata-practice, viz-cookbook, devecon-toolkit,
                toc-workshop-pro, logframe-pro, chart-selector-pro, stakeholder-pro,
                empathy-pro, policy-canvas-pro, ai-canvas-pro, field-notes-pro]
organization:  [same as professional]
```

## Supabase డేటాబేస్ పట్టికలు

| పట్టిక | ప్రయోజనం |
|-------|---------|
| `profiles` | వినియోగదారు ఖాతాలు, శ్రేణి, స్ట్రీక్, ఆసక్తులు |
| `user_progress` | ఒక్కో-కోర్సు పురోగతి ట్రాకింగ్ |
| `bookmarks` | వినియోగదారు బుక్‌మార్క్‌లు |
| `user_notes` | వ్యక్తిగత గమనికలు |
| `certificates` | బ్యాడ్జ్ మెటాడేటాతో జారీ చేసిన సర్టిఫికెట్లు |
| `payments` | చెల్లింపు చరిత్ర |
| `coaching_bookings` | కోచింగ్ సెషన్ బుకింగ్‌లు |
| `organizations` | సంస్థ రికార్డులు |
| `organization_members` | వినియోగదారు ↔ సంస్థ సభ్యత్వం |
| `learning_paths` | అనుకూల సంస్థ అభ్యాస మార్గాలు |
| `learning_path_assignments` | గడువు తేదీలతో మార్గం ↔ వినియోగదారు కేటాయింపులు |
| `portfolio_items` | వినియోగదారు పోర్ట్‌ఫోలియో ఎంట్రీలు |
| `challenge_submissions` | లైవ్ కేస్ ఛాలెంజ్ సమర్పణలు |
| `challenge_requests` | సంస్థల నుండి అనుకూల ఛాలెంజ్ అభ్యర్థనలు |
| `cohorts` | ప్రారంభ/ముగింపు తేదీలతో శిక్షణా కోహోర్ట్‌లు (v10.8.0) |
| `cohort_members` | కోహోర్ట్ నమోదు + పురోగతి ట్రాకింగ్ (v10.8.0) |
| `cohort_discussions` | కోహోర్ట్‌లలో చర్చా థ్రెడ్‌లు (v10.8.0) |
| `notifications` | యాప్-లోపల + ఇమెయిల్ నోటిఫికేషన్ లాగ్ (v10.8.0) |
| `notification_preferences` | ఒక్కో-వినియోగదారు ఇమెయిల్ ఆప్ట్-ఇన్/అవుట్ (v10.8.0) |
| `course_content` | Edge Function ద్వారా అందించబడే డైనమిక్ కోర్సు HTML |
| `badge_shares` | బ్యాడ్జ్ పంచుకోవడం ట్రాకింగ్ |

## Supabase Edge Functions

| ఫంక్షన్ | ప్రయోజనం |
|----------|---------|
| `mint-resource-token` | ప్రీమియం వనరు యాక్సెస్ కోసం JWT మింటింగ్ |
| `issue-certificate` | కోర్సు పూర్తిపై సర్టిఫికెట్ జారీ |
| `game-agent` | గేమ్‌ల కోసం MiroFish AI ఏజెంట్ ఇంజిన్ (బహుళ-ప్రొవైడర్ LLM) |
| `serve-course-content` | డైనమిక్ కోర్సు కంటెంట్ సర్వింగ్ |
| `send-notification` | ఇమెయిల్ నోటిఫికేషన్లు: స్ట్రీక్ రిమైండర్లు, కోహోర్ట్ గడువులు, మాన్యువల్ (v10.8.0) |

## ఫైల్ నిర్మాణం

పూర్తి డైరెక్టరీ లేఅవుట్ కోసం [README → Project Structure](https://github.com/ImpactMojo/ImpactMojo#project-structure) చూడండి.
