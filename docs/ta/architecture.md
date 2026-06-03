# கட்டமைப்பு (Architecture)

> **இந்தப் பக்கம் யாருக்கானது?** இந்தப் பக்கம் முதன்மையாக டெவலப்பர்களுக்கும் தொழில்நுட்பப் பங்களிப்பாளர்களுக்கும் ஆனது. நீங்கள் ஒரு கல்வியாளர் அல்லது பயிற்சியாளர் என்றால், முக்கியக் கருத்து கீழே "பயனர்களுக்கு இதன் அர்த்தம் என்ன" பகுதியில் உள்ளது — தொழில்நுட்ப விவரங்களைத் தவிர்க்கலாம்.

## பயனர்களுக்கு இதன் அர்த்தம் என்ன

ImpactMojo தென் ஆசியாவில் உள்ள பயிற்சியாளர்களுக்காக வடிவமைக்கப்பட்டுள்ளது, அவர்களில் பலர் மெதுவான இணைய இணைப்புகளிலோ அல்லது பழைய சாதனங்களிலோ உள்ளனர். எங்கள் தொழில்நுட்பத் தேர்வுகள் உங்கள் அனுபவத்திற்கு என்ன அர்த்தம் தருகின்றன என்பது இதோ:

- **வேகமான ஏற்றுதல்** — தளம் எளிமையான, இலகுவான குறியீட்டில் கட்டப்பட்டுள்ளது (கனமான frameworks இல்லை). 2G/3G இணைப்புகளிலும் பக்கங்கள் விரைவாக ஏற்றப்படுகின்றன.
- **ஆஃப்லைனில் வேலை செய்கிறது** — ஒரு பக்கத்தை நீங்கள் பார்வையிட்ட பிறகு, அது உங்கள் சாதனத்தில் சேமிக்கப்படுகிறது. இணைய இணைப்பு இல்லாமலேயே முதன்மை (flagship) பாடநெறிகளை அணுகலாம்.
- **நிறுவல் தேவையில்லை** — அனைத்தும் உங்கள் வலை உலாவியில் இயங்குகிறது. பதிவிறக்க எந்த ஆப்பும் இல்லை, நிறுவ எந்த மென்பொருளும் இல்லை.
- **உங்கள் தரவு பாதுகாப்பானது** — உள்நுழைவு மற்றும் கணக்குத் தரவை Supabase (ஒரு நம்பகமான தரவுத்தள சேவை) கையாள்கிறது. பிரீமியம் கருவிகள் கால-வரம்பிட்ட பாதுகாப்பு tokens பயன்படுத்துகின்றன, எனவே உங்கள் அணுகலைத் திருட முடியாது.
- **எந்தச் சாதனத்திலும் வேலை செய்கிறது** — தொலைபேசி, டேப்லெட், லேப்டாப், டெஸ்க்டாப் — பழையதாக இருந்தாலும் புதியதாக இருந்தாலும். நவீன வன்பொருள் தேவைப்படும் தொழில்நுட்பங்களை நாங்கள் வேண்டுமென்றே தவிர்க்கிறோம்.

## தொழில்நுட்ப மேலோட்டம்

ImpactMojo என்பது எந்த build step-ம் இல்லாத ஒரு static HTML/CSS/JS தளம் ஆகும், அங்கீகாரத்திற்காக Supabase மற்றும் ஹோஸ்டிங்கிற்காக Netlify ஆல் இயக்கப்படுகிறது. பிரீமியம் கருவிகள் தனித்தனி Netlify தளங்களாக வரிசைப்படுத்தப்படுகின்றன, அவை ஒவ்வொன்றும் ஒரு JWT auth-gate ஆல் பாதுகாக்கப்படுகின்றன.

## அமைப்பு வரைபடம் (System Diagram)

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

## முக்கிய வடிவமைப்பு முடிவுகள்

### ஏன் framework இல்லை?

ImpactMojo தென் ஆசியாவில் உள்ள பயிற்சியாளர்களுக்கு சேவை செய்கிறது, அவர்களில் பலர் குறைந்த-பேண்ட்விட்த் இணைப்புகளிலும் பழைய சாதனங்களிலும் உள்ளனர். ஒரு vanilla HTML/CSS/JS தளம்:
- பூஜ்ஜிய JS bundle மேல்நிலைச் சுமையுடன் வேகமாக ஏற்றுகிறது
- polyfills இல்லாமல் எந்த உலாவியிலும் வேலை செய்கிறது
- எந்த build step-ம் இல்லாமல் ஒரு static தளமாக வழங்கப்படலாம்
- புரிந்துகொள்ளவும் பங்களிக்கவும் எளிதானது

### பிரீமியம் கருவிகளுக்கு ஏன் தனித்தனி Netlify தளங்கள்?

ஒவ்வொரு பிரீமியம் கருவியும் (VaniScribe, Qual Lab, முதலியன) சுயாதீனமாகக் கட்டப்பட்டது. அவற்றைத் தனித்தனி தளங்களாக ஹோஸ்ட் செய்வது:
- சுயாதீனமான வரிசைப்படுத்தல் மற்றும் மறுசெயலாக்கத்தை அனுமதிக்கிறது
- தோல்விகளைத் தனிமைப்படுத்துகிறது — ஒரு கருவி செயலிழந்தால் மற்றவற்றைப் பாதிக்காது
- JWT auth-gate-ஐ எளிமையாக்குகிறது: தளத்திற்கு ஒரு edge function
- வெவ்வேறு குழுக்கள் வெவ்வேறு கருவிகளை சொந்தமாக்கிக்கொள்ள அனுமதிக்கிறது

### session-அடிப்படையிலான அங்கீகாரத்தை விட ஏன் JWT?

- **Stateless:** ஒவ்வொரு resource தள request-லும் தரவுத்தள lookup தேவையில்லை
- **Cross-domain:** முதன்மைத் தளமும் resource தளங்களும் வெவ்வேறு டொமைன்களில் உள்ளன
- **குறுகிய காலம்:** 5-நிமிட tokens இடைமறிக்கப்பட்டால் வெளிப்பாட்டைக் கட்டுப்படுத்துகின்றன
- **Session cookies:** ஆரம்ப JWT சரிபார்ப்புக்குப் பிறகு, 24h cookie மறு-அங்கீகாரத்தைத் தவிர்க்கிறது

### ஏன் Supabase?

- இலவச tier எங்கள் auth தேவைகளை உள்ளடக்குகிறது
- profiles-க்கு உள்ளமைந்த Row Level Security
- serverless JWT minting-க்கான Edge Functions
- கட்டமைக்கப்பட்ட தரவுக்கான PostgreSQL
- Google OAuth + Magic Links உடனடியாகக் கிடைக்கிறது

## சூழல் மாறிகள் (Environment Variables)

### முதன்மைத் தளம் (impactmojo.in)
எந்த server-side env vars-ம் தேவையில்லை — Supabase நற்சான்றுகள் `js/auth.js`-இல் உள்ளன (public anon key மட்டுமே).

### Supabase Edge Function (mint-resource-token)
| Variable | விளக்கம் |
|----------|-------------|
| `RESOURCE_TOKEN_SECRET` | JWTs-க்கான HMAC-SHA256 signing key |
| `SUPABASE_URL` | Supabase ஆல் தானாக வழங்கப்படுகிறது |
| `SUPABASE_ANON_KEY` | Supabase ஆல் தானாக வழங்கப்படுகிறது |
| `SUPABASE_SERVICE_ROLE_KEY` | தானாக வழங்கப்படுகிறது; RLS-ஐ புறக்கணித்து profiles படிக்கிறது |

### Resource Netlify தளங்கள் (தளத்திற்கு)
| Variable | விளக்கம் |
|----------|-------------|
| `RESOURCE_TOKEN_SECRET` | மேலே உள்ளதைப் போன்ற அதே HMAC key |
| `RESOURCE_ID` | தனிப்பட்ட slug: `rq-builder`, `toc-workbench-pro`, `code-convert-pro`, `qual-insights`, `vaniscribe`, `devdata-practice`, `viz-cookbook`, `devecon-toolkit`, `field-notes-pro`, `toc-workshop-pro`, `logframe-pro`, `chart-selector-pro`, `stakeholder-pro`, `empathy-pro`, `policy-canvas-pro`, `ai-canvas-pro` |

## Tier Access Control

```
explorer:      []  (free content only)
practitioner:  [rq-builder, toc-workbench-pro]
professional:  [rq-builder, toc-workbench-pro, code-convert-pro, qual-insights, vaniscribe,
                devdata-practice, viz-cookbook, devecon-toolkit,
                toc-workshop-pro, logframe-pro, chart-selector-pro, stakeholder-pro,
                empathy-pro, policy-canvas-pro, ai-canvas-pro, field-notes-pro]
organization:  [same as professional]
```

## Supabase Database Tables

| Table | நோக்கம் |
|-------|---------|
| `profiles` | பயனர் கணக்குகள், tier, streak, ஆர்வங்கள் |
| `user_progress` | பாடநெறிக்கான முன்னேற்றக் கண்காணிப்பு |
| `bookmarks` | பயனர் புத்தகக்குறிகள் |
| `user_notes` | தனிப்பட்ட குறிப்புகள் |
| `certificates` | badge metadata உடன் வழங்கப்பட்ட சான்றிதழ்கள் |
| `payments` | கட்டண வரலாறு |
| `coaching_bookings` | பயிற்சி அமர்வு முன்பதிவுகள் |
| `organizations` | நிறுவன பதிவுகள் |
| `organization_members` | பயனர் ↔ நிறுவன உறுப்பினர் |
| `learning_paths` | தனிப்பயன் நிறுவன கற்றல் பாதைகள் |
| `learning_path_assignments` | நிலுவைத் தேதிகளுடன் பாதை ↔ பயனர் ஒதுக்கீடுகள் |
| `portfolio_items` | பயனர் போர்ட்ஃபோலியோ உள்ளீடுகள் |
| `challenge_submissions` | நேரடி வழக்கு சவால் சமர்ப்பணங்கள் |
| `challenge_requests` | நிறுவனங்களிடமிருந்து தனிப்பயன் சவால் கோரிக்கைகள் |
| `cohorts` | தொடக்க/முடிவு தேதிகளுடன் பயிற்சி cohorts (v10.8.0) |
| `cohort_members` | Cohort சேர்க்கை + முன்னேற்றக் கண்காணிப்பு (v10.8.0) |
| `cohort_discussions` | cohorts-க்குள் கலந்துரையாடல் இழைகள் (v10.8.0) |
| `notifications` | இன்-ஆப் + மின்னஞ்சல் அறிவிப்பு பதிவு (v10.8.0) |
| `notification_preferences` | பயனருக்கான மின்னஞ்சல் opt-in/out (v10.8.0) |
| `course_content` | Edge Function மூலம் வழங்கப்படும் டைனமிக் பாடநெறி HTML |
| `badge_shares` | Badge பகிர்வுக் கண்காணிப்பு |

## Supabase Edge Functions

| Function | நோக்கம் |
|----------|---------|
| `mint-resource-token` | பிரீமியம் resource அணுகலுக்கான JWT minting |
| `issue-certificate` | பாடநெறி நிறைவின் போது சான்றிதழ் வழங்குதல் |
| `game-agent` | விளையாட்டுகளுக்கான MiroFish AI agent engine (multi-provider LLM) |
| `serve-course-content` | டைனமிக் பாடநெறி உள்ளடக்கம் வழங்குதல் |
| `send-notification` | மின்னஞ்சல் அறிவிப்புகள்: streak நினைவூட்டல்கள், cohort காலக்கெடுக்கள், மேன்வல் (v10.8.0) |

## கோப்பு அமைப்பு

முழு அடைவு தளவமைப்பிற்கு [README → Project Structure](https://github.com/ImpactMojo/ImpactMojo#project-structure) ஐப் பார்க்கவும்.
