# API রেফারেন্স

## Supabase Schema

### Tables

#### `profiles`

ব্যবহারকারীর প্রোফাইল এবং সাবস্ক্রিপশন ডেটা সংরক্ষণ করে। সাইনআপের সময় ডেটাবেস ট্রিগারের মাধ্যমে স্বয়ংক্রিয়ভাবে তৈরি হয়।

| Column | Type | বিবরণ |
|--------|------|-------------|
| `id` | uuid (PK, FK → auth.users) | ব্যবহারকারী ID |
| `email` | text | ব্যবহারকারীর ইমেল |
| `full_name` | text | প্রদর্শন নাম |
| `subscription_tier` | text | `explorer`, `practitioner`, `professional`, `organization` |
| `subscription_status` | text | `active`, `expired`, `cancelled` |
| `organization_id` | uuid (nullable) | organizations table-এর FK |
| `created_at` | timestamptz | অ্যাকাউন্ট তৈরি |
| `updated_at` | timestamptz | সর্বশেষ প্রোফাইল আপডেট |

#### `organizations`

| Column | Type | বিবরণ |
|--------|------|-------------|
| `id` | uuid (PK) | প্রতিষ্ঠানের ID |
| `name` | text | প্রতিষ্ঠানের নাম |
| `admin_id` | uuid (FK → profiles) | প্রতিষ্ঠানের admin ব্যবহারকারী |
| `max_seats` | integer | লাইসেন্স সিট সংখ্যা |
| `created_at` | timestamptz | তৈরির তারিখ |

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

প্রিমিয়াম রিসোর্স সাইট অ্যাক্সেস করার জন্য একটি স্বল্পমেয়াদী JWT তৈরি করে।

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

প্রতিটি প্রিমিয়াম রিসোর্স সাইটে স্থাপন করা হয়। JWT টোকেন যাচাই করে এবং সেশন কুকি পরিচালনা করে।

**প্রবাহ:**
1. `resource_session` কুকি পরীক্ষা করুন → বৈধ হলে, অনুরোধ অনুমোদন করুন
2. `?token=` query parameter পরীক্ষা করুন → JWT signature যাচাই করুন
3. যাচাই করুন যে `resource` claim সাইটের `RESOURCE_ID`-এর সাথে মেলে
4. ২৪-ঘণ্টার `resource_session` কুকি সেট করুন
5. পরিষ্কার URL-এ রিডাইরেক্ট করুন (token parameter সরিয়ে দিন)
6. কোনো কুকি নেই + কোনো token নেই → লগইন পৃষ্ঠায় রিডাইরেক্ট করুন

## Tier Access Matrix

| রিসোর্স | Explorer | Practitioner | Professional | Organization |
|----------|----------|--------------|--------------|--------------|
| বিনামূল্যের কোর্স ও বিষয়বস্তু | হ্যাঁ | হ্যাঁ | হ্যাঁ | হ্যাঁ |
| RQ Builder | না | হ্যাঁ | হ্যাঁ | হ্যাঁ |
| Code Convert Pro | না | না | হ্যাঁ | হ্যাঁ |
| Qual Insights | না | না | হ্যাঁ | হ্যাঁ |
| VaniScribe | না | না | হ্যাঁ | হ্যাঁ |
| DevData Practice | না | না | হ্যাঁ | হ্যাঁ |
| Viz Cookbook | না | না | হ্যাঁ | হ্যাঁ |
| DevEcon Toolkit | না | না | হ্যাঁ | হ্যাঁ |

## প্রমাণীকরণ প্রবাহ

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
