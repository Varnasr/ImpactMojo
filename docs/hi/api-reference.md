# API संदर्भ

## Supabase Schema

### Tables

#### `profiles`

उपयोगकर्ता प्रोफ़ाइल और सब्सक्रिप्शन डेटा संग्रहीत करता है। साइनअप पर डेटाबेस ट्रिगर के माध्यम से स्वतः बनता है।

| Column | Type | विवरण |
|--------|------|-------------|
| `id` | uuid (PK, FK → auth.users) | उपयोगकर्ता ID |
| `email` | text | उपयोगकर्ता ईमेल |
| `full_name` | text | प्रदर्शन नाम |
| `subscription_tier` | text | `explorer`, `practitioner`, `professional`, `organization` |
| `subscription_status` | text | `active`, `expired`, `cancelled` |
| `organization_id` | uuid (nullable) | organizations table से FK |
| `created_at` | timestamptz | खाता निर्माण |
| `updated_at` | timestamptz | अंतिम प्रोफ़ाइल अपडेट |

#### `organizations`

| Column | Type | विवरण |
|--------|------|-------------|
| `id` | uuid (PK) | संगठन ID |
| `name` | text | संगठन का नाम |
| `admin_id` | uuid (FK → profiles) | संगठन का admin उपयोगकर्ता |
| `max_seats` | integer | लाइसेंस सीट संख्या |
| `created_at` | timestamptz | निर्माण तिथि |

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

प्रीमियम संसाधन साइटों तक पहुँच के लिए एक अल्पकालिक JWT जारी करता है।

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

प्रत्येक प्रीमियम संसाधन साइट पर तैनात। JWT टोकन सत्यापित करता है और सत्र कुकीज़ का प्रबंधन करता है।

**प्रवाह:**
1. `resource_session` कुकी की जाँच करें → यदि वैध है, तो अनुरोध की अनुमति दें
2. `?token=` query parameter की जाँच करें → JWT signature सत्यापित करें
3. सत्यापित करें कि `resource` claim साइट के `RESOURCE_ID` से मेल खाता है
4. 24-घंटे की `resource_session` कुकी सेट करें
5. स्वच्छ URL पर रीडायरेक्ट करें (token parameter हटाएँ)
6. कोई कुकी नहीं + कोई token नहीं → लॉगिन पृष्ठ पर रीडायरेक्ट करें

## Tier Access Matrix

| संसाधन | Explorer | Practitioner | Professional | Organization |
|----------|----------|--------------|--------------|--------------|
| निःशुल्क पाठ्यक्रम और सामग्री | हाँ | हाँ | हाँ | हाँ |
| RQ Builder | नहीं | हाँ | हाँ | हाँ |
| Code Convert Pro | नहीं | नहीं | हाँ | हाँ |
| Qual Insights | नहीं | नहीं | हाँ | हाँ |
| VaniScribe | नहीं | नहीं | हाँ | हाँ |
| DevData Practice | नहीं | नहीं | हाँ | हाँ |
| Viz Cookbook | नहीं | नहीं | हाँ | हाँ |
| DevEcon Toolkit | नहीं | नहीं | हाँ | हाँ |

## प्रमाणीकरण प्रवाह

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
