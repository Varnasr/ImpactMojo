# API குறிப்பு

## Supabase Schema

### Tables

#### `profiles`

பயனர் சுயவிவரம் மற்றும் சந்தா தரவைச் சேமிக்கிறது. பதிவு செய்யும்போது டேட்டாபேஸ் ட்ரிக்கர் மூலம் தானாகவே உருவாக்கப்படுகிறது.

| Column | Type | விளக்கம் |
|--------|------|-------------|
| `id` | uuid (PK, FK → auth.users) | பயனர் ID |
| `email` | text | பயனர் மின்னஞ்சல் |
| `full_name` | text | காட்சிப் பெயர் |
| `subscription_tier` | text | `explorer`, `practitioner`, `professional`, `organization` |
| `subscription_status` | text | `active`, `expired`, `cancelled` |
| `organization_id` | uuid (nullable) | organizations table-க்கான FK |
| `created_at` | timestamptz | கணக்கு உருவாக்கம் |
| `updated_at` | timestamptz | கடைசி சுயவிவர புதுப்பிப்பு |

#### `organizations`

| Column | Type | விளக்கம் |
|--------|------|-------------|
| `id` | uuid (PK) | நிறுவன ID |
| `name` | text | நிறுவனப் பெயர் |
| `admin_id` | uuid (FK → profiles) | நிறுவன admin பயனர் |
| `max_seats` | integer | உரிம இருக்கைகளின் எண்ணிக்கை |
| `created_at` | timestamptz | உருவாக்கிய தேதி |

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

பிரீமியம் வள தளங்களை அணுகுவதற்கான குறுகிய கால JWT-ஐ உருவாக்குகிறது.

**Request:**
```
POST /functions/v1/mint-resource-token
Authorization: Bearer <supabase_access_token>
Content-Type: application/json

{
  "resource_id": "rq-builder"
}
```

**Response (200):**
```json
{
  "token": "eyJhbGciOiJIUzI1NiIs...",
  "url": "https://<resource-site>/?token=eyJhbGciOiJIUzI1NiIs..."
}
```

**Response (403):**
```json
{
  "error": "Your subscription tier does not include this resource"
}
```

**JWT Claims:**
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

ஒவ்வொரு பிரீமியம் வள தளத்திலும் பயன்படுத்தப்படுகிறது. JWT டோக்கன்களைச் சரிபார்த்து, அமர்வு குக்கீகளை நிர்வகிக்கிறது.

**ஓட்டம்:**
1. `resource_session` குக்கீயைச் சரிபார்க்கவும் → செல்லுபடியாகுமானால், கோரிக்கையை அனுமதிக்கவும்
2. `?token=` query parameter-ஐச் சரிபார்க்கவும் → JWT signature-ஐ சரிபார்க்கவும்
3. `resource` claim தளத்தின் `RESOURCE_ID`-உடன் பொருந்துகிறதா எனச் சரிபார்க்கவும்
4. 24-மணிநேர `resource_session` குக்கீயை அமைக்கவும்
5. சுத்தமான URL-க்கு திருப்பிவிடவும் (token parameter-ஐ நீக்கவும்)
6. குக்கீ இல்லை + token இல்லை → உள்நுழைவு பக்கத்திற்கு திருப்பிவிடவும்

## Tier Access Matrix

| வளம் | Explorer | Practitioner | Professional | Organization |
|----------|----------|--------------|--------------|--------------|
| இலவச பாடநெறிகள் & உள்ளடக்கம் | ஆம் | ஆம் | ஆம் | ஆம் |
| RQ Builder | இல்லை | ஆம் | ஆம் | ஆம் |
| Code Convert Pro | இல்லை | இல்லை | ஆம் | ஆம் |
| Qual Insights | இல்லை | இல்லை | ஆம் | ஆம் |
| VaniScribe | இல்லை | இல்லை | ஆம் | ஆம் |
| DevData Practice | இல்லை | இல்லை | ஆம் | ஆம் |
| Viz Cookbook | இல்லை | இல்லை | ஆம் | ஆம் |
| DevEcon Toolkit | இல்லை | இல்லை | ஆம் | ஆம் |

## அங்கீகார ஓட்டம்

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
