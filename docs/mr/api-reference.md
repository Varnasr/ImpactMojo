# API संदर्भ

## Supabase Schema

### Tables

#### `profiles`

वापरकर्त्याचा प्रोफाइल आणि सदस्यता डेटा साठवते. साइनअपवेळी database trigger द्वारे आपोआप तयार होते.

| Column | Type | वर्णन |
|--------|------|-------------|
| `id` | uuid (PK, FK → auth.users) | वापरकर्ता ID |
| `email` | text | वापरकर्त्याचा ईमेल |
| `full_name` | text | प्रदर्शित नाव |
| `subscription_tier` | text | `explorer`, `practitioner`, `professional`, `organization` |
| `subscription_status` | text | `active`, `expired`, `cancelled` |
| `organization_id` | uuid (nullable) | organizations table कडे FK |
| `created_at` | timestamptz | खाते निर्मिती |
| `updated_at` | timestamptz | शेवटचे प्रोफाइल अद्यतन |

#### `organizations`

| Column | Type | वर्णन |
|--------|------|-------------|
| `id` | uuid (PK) | संस्था ID |
| `name` | text | संस्थेचे नाव |
| `admin_id` | uuid (FK → profiles) | संस्थेचा admin वापरकर्ता |
| `max_seats` | integer | परवाना seat संख्या |
| `created_at` | timestamptz | निर्मिती तारीख |

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

premium resource साइट्समध्ये प्रवेशासाठी अल्पायुषी JWT तयार करते.

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

प्रत्येक premium resource साइटवर तैनात केले जाते. JWT tokens सत्यापित करते आणि session cookies व्यवस्थापित करते.

**प्रवाह:**
1. `resource_session` cookie तपासा → वैध असल्यास, request ला परवानगी द्या
2. `?token=` query parameter तपासा → JWT signature सत्यापित करा
3. `resource` claim साइटच्या `RESOURCE_ID` शी जुळते का ते सत्यापित करा
4. 24-तासांचे `resource_session` cookie सेट करा
5. स्वच्छ URL कडे पुनर्निर्देशित करा (token parameter काढून टाका)
6. cookie नाही + token नाही → login page कडे पुनर्निर्देशित करा

## Tier Access Matrix

| Resource | Explorer | Practitioner | Professional | Organization |
|----------|----------|--------------|--------------|--------------|
| मोफत अभ्यासक्रम आणि आशय | होय | होय | होय | होय |
| RQ Builder | नाही | होय | होय | होय |
| Code Convert Pro | नाही | नाही | होय | होय |
| Qual Insights | नाही | नाही | होय | होय |
| VaniScribe | नाही | नाही | होय | होय |
| DevData Practice | नाही | नाही | होय | होय |
| Viz Cookbook | नाही | नाही | होय | होय |
| DevEcon Toolkit | नाही | नाही | होय | होय |

## Authentication Flow

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
