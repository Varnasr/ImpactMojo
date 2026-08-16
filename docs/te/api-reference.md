# API సూచన

## Supabase స్కీమా

### పట్టికలు

#### `profiles`

వినియోగదారు ప్రొఫైల్ మరియు సబ్‌స్క్రిప్షన్ డేటాను నిల్వ చేస్తుంది. డేటాబేస్ ట్రిగ్గర్ ద్వారా సైన్అప్‌లో స్వయంచాలకంగా సృష్టించబడుతుంది.

| నిలువు వరుస | రకం | వివరణ |
|--------|------|-------------|
| `id` | uuid (PK, FK → auth.users) | వినియోగదారు ID |
| `email` | text | వినియోగదారు ఇమెయిల్ |
| `full_name` | text | ప్రదర్శన పేరు |
| `subscription_tier` | text | `explorer`, `practitioner`, `professional`, `organization` |
| `subscription_status` | text | `active`, `expired`, `cancelled` |
| `organization_id` | uuid (nullable) | organizations పట్టికకు FK |
| `created_at` | timestamptz | ఖాతా సృష్టి |
| `updated_at` | timestamptz | చివరి ప్రొఫైల్ నవీకరణ |

#### `organizations`

| నిలువు వరుస | రకం | వివరణ |
|--------|------|-------------|
| `id` | uuid (PK) | సంస్థ ID |
| `name` | text | సంస్థ పేరు |
| `admin_id` | uuid (FK → profiles) | సంస్థ అడ్మిన్ వినియోగదారు |
| `max_seats` | integer | లైసెన్స్ సీట్ల సంఖ్య |
| `created_at` | timestamptz | సృష్టి తేదీ |

### Row Level Security (RLS)

```sql
-- Users can read their own profile
CREATE POLICY "Users can view own profile"
  ON profiles FOR SELECT
  USING (auth.uid() = id);

-- Users can update their own profile
CREATE POLICY "Users can update own profile"
  ON profiles FOR UPDATE
  USING (auth.uid() = id);
```

## Edge Functions

### `mint-resource-token`

ప్రీమియం వనరు సైట్‌లను యాక్సెస్ చేయడానికి ఒక స్వల్ప-కాల JWT ను మింట్ చేస్తుంది.

**అభ్యర్థన:**
```
POST /functions/v1/mint-resource-token
Authorization: Bearer <supabase_access_token>
Content-Type: application/json

{
  "resource_id": "rq-builder"
}
```

**ప్రతిస్పందన (200):**
```json
{
  "token": "eyJhbGciOiJIUzI1NiIs...",
  "url": "https://<resource-site>/?token=eyJhbGciOiJIUzI1NiIs..."
}
```

**ప్రతిస్పందన (403):**
```json
{
  "error": "Your subscription tier does not include this resource"
}
```

**JWT క్లెయిమ్‌లు:**
```json
{
  "sub": "user-uuid",
  "resource": "rq-builder",
  "tier": "professional",
  "iat": 1710000000,
  "exp": 1710000300
}
```

### `auth-gate.ts` (Netlify Edge Function)

ప్రతి ప్రీమియం వనరు సైట్‌లో విస్తరించబడింది. JWT టోకెన్లను ధృవీకరిస్తుంది మరియు సెషన్ కుకీలను నిర్వహిస్తుంది.

**ప్రవాహం:**
1. `resource_session` కుకీ కోసం తనిఖీ చేయండి → చెల్లుబాటైతే, అభ్యర్థనను అనుమతించండి
2. `?token=` క్వెరీ పారామితర్ కోసం తనిఖీ చేయండి → JWT సంతకాన్ని ధృవీకరించండి
3. `resource` క్లెయిమ్ సైట్ యొక్క `RESOURCE_ID` తో సరిపోతుందో ధృవీకరించండి
4. 24-గంటల `resource_session` కుకీని సెట్ చేయండి
5. క్లీన్ URL కు మళ్లించండి (token పారామితర్‌ను తీసివేయండి)
6. కుకీ లేదు + టోకెన్ లేదు → లాగిన్ పేజీకి మళ్లించండి

## శ్రేణి యాక్సెస్ మ్యాట్రిక్స్

| వనరు | Explorer | Practitioner | Professional | Organization |
|----------|----------|--------------|--------------|--------------|
| ఉచిత కోర్సులు & కంటెంట్ | Yes | Yes | Yes | Yes |
| RQ Builder | No | Yes | Yes | Yes |
| Code Convert Pro | No | No | Yes | Yes |
| Qual Insights | No | No | Yes | Yes |
| VaniScribe | No | No | Yes | Yes |
| DevData Practice | No | No | Yes | Yes |
| Viz Cookbook | No | No | Yes | Yes |
| DevEcon Toolkit | No | No | Yes | Yes |

## ప్రామాణీకరణ ప్రవాహం

```
User clicks "Login" → Supabase Auth (Google OAuth / Magic Link)
                     → Profile auto-created via DB trigger
                     → JWT issued by Supabase
                     → Client stores session in localStorage

User clicks premium tool → js/resource-launch.js
                         → POST mint-resource-token with Supabase JWT
                         → Receives resource JWT
                         → window.open(resourceUrl + '?token=...')
                         → Resource site auth-gate validates token
                         → Sets session cookie, serves tool
```
