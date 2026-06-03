# আর্কিটেকচার

> **এই পৃষ্ঠাটি কাদের জন্য?** এই পৃষ্ঠাটি মূলত ডেভেলপার এবং প্রযুক্তিগত অবদানকারীদের জন্য। আপনি যদি একজন শিক্ষক বা প্র্যাকটিশনার হন, তাহলে মূল বিষয়টি নিচের "ব্যবহারকারীদের জন্য এর অর্থ কী" বিভাগে রয়েছে — আপনি প্রযুক্তিগত বিবরণ এড়িয়ে যেতে পারেন।

## ব্যবহারকারীদের জন্য এর অর্থ কী

ImpactMojo দক্ষিণ এশিয়ার প্র্যাকটিশনারদের জন্য তৈরি, যাঁদের অনেকেই ধীর ইন্টারনেট সংযোগ বা পুরোনো ডিভাইসে আছেন। আমাদের প্রযুক্তিগত পছন্দগুলির আপনার অভিজ্ঞতার জন্য অর্থ এই:

- **দ্রুত লোডিং** — সাইটটি সরল, হালকা কোড দিয়ে তৈরি (কোনো ভারী framework নেই)। 2G/3G সংযোগেও পৃষ্ঠাগুলি দ্রুত লোড হয়।
- **অফলাইনে কাজ করে** — একবার আপনি কোনো পৃষ্ঠা পরিদর্শন করলে, এটি আপনার ডিভাইসে সংরক্ষিত হয়। আপনি ইন্টারনেট সংযোগ ছাড়াই ফ্ল্যাগশিপ কোর্সগুলি অ্যাক্সেস করতে পারেন।
- **কোনো ইনস্টলেশনের প্রয়োজন নেই** — সবকিছু আপনার ওয়েব ব্রাউজারে চলে। ডাউনলোড করার মতো কোনো অ্যাপ নেই, ইনস্টল করার মতো কোনো সফটওয়্যার নেই।
- **আপনার ডেটা নিরাপদ** — লগইন এবং অ্যাকাউন্ট ডেটা Supabase (একটি বিশ্বস্ত ডেটাবেস পরিষেবা) দ্বারা পরিচালিত হয়। প্রিমিয়াম টুলগুলি সময়-সীমিত নিরাপত্তা tokens ব্যবহার করে, যাতে আপনার অ্যাক্সেস চুরি না হয়।
- **যেকোনো ডিভাইসে কাজ করে** — ফোন, ট্যাবলেট, ল্যাপটপ, ডেস্কটপ — পুরোনো বা নতুন। আমরা ইচ্ছাকৃতভাবে এমন প্রযুক্তি এড়িয়ে চলি যেগুলির জন্য আধুনিক হার্ডওয়্যার প্রয়োজন।

## প্রযুক্তিগত সংক্ষিপ্তসার

ImpactMojo হল একটি static HTML/CSS/JS সাইট, যাতে কোনো build step নেই, এর পেছনে প্রমাণীকরণের জন্য Supabase এবং হোস্টিংয়ের জন্য Netlify আছে। প্রিমিয়াম টুলগুলি পৃথক Netlify সাইট হিসেবে স্থাপন করা হয়, প্রতিটি একটি JWT auth-gate দ্বারা সুরক্ষিত।

## সিস্টেম ডায়াগ্রাম

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

## মূল ডিজাইন সিদ্ধান্ত

### কেন কোনো framework নেই?

ImpactMojo দক্ষিণ এশিয়ার প্র্যাকটিশনারদের সেবা দেয়, যাঁদের অনেকেই কম-ব্যান্ডউইথ সংযোগ এবং পুরোনো ডিভাইসে আছেন। একটি vanilla HTML/CSS/JS সাইট:
- শূন্য JS bundle ওভারহেড নিয়ে দ্রুত লোড হয়
- polyfills ছাড়াই যেকোনো ব্রাউজারে কাজ করে
- কোনো build step ছাড়াই একটি static সাইট হিসেবে পরিবেশন করা যায়
- বোঝা এবং অবদান রাখা সহজ

### প্রিমিয়াম টুলের জন্য কেন পৃথক Netlify সাইট?

প্রতিটি প্রিমিয়াম টুল (VaniScribe, Qual Lab, ইত্যাদি) স্বাধীনভাবে তৈরি হয়েছিল। সেগুলিকে পৃথক সাইট হিসেবে হোস্ট করা:
- স্বাধীন স্থাপনা এবং পুনরাবৃত্তির অনুমতি দেয়
- ব্যর্থতাগুলিকে বিচ্ছিন্ন করে — একটি টুল বন্ধ হলে অন্যগুলিতে প্রভাব পড়ে না
- JWT auth-gate-কে সরল করে: প্রতি সাইটে একটি edge function
- বিভিন্ন দলকে বিভিন্ন টুলের মালিকানা নিতে দেয়

### session-ভিত্তিক প্রমাণীকরণের পরিবর্তে কেন JWT?

- **Stateless:** প্রতিটি resource সাইট request-এ কোনো ডেটাবেস lookup নেই
- **Cross-domain:** মূল সাইট এবং resource সাইট ভিন্ন ডোমেনে আছে
- **স্বল্পস্থায়ী:** 5-মিনিটের tokens আটকানো হলে এক্সপোজার সীমিত করে
- **Session cookies:** প্রাথমিক JWT যাচাইয়ের পরে, একটি 24h cookie পুনঃ-প্রমাণীকরণ এড়ায়

### কেন Supabase?

- ফ্রি tier আমাদের auth চাহিদা পূরণ করে
- profiles-এর জন্য অন্তর্নির্মিত Row Level Security
- serverless JWT minting-এর জন্য Edge Functions
- কাঠামোবদ্ধ ডেটার জন্য PostgreSQL
- Google OAuth + Magic Links সরাসরি উপলব্ধ

## এনভায়রনমেন্ট ভেরিয়েবল (Environment Variables)

### মূল সাইট (impactmojo.in)
কোনো server-side env vars প্রয়োজন নেই — Supabase শংসাপত্রগুলি `js/auth.js`-এ আছে (শুধুমাত্র public anon key)।

### Supabase Edge Function (mint-resource-token)
| Variable | বিবরণ |
|----------|-------------|
| `RESOURCE_TOKEN_SECRET` | JWTs-এর জন্য HMAC-SHA256 signing key |
| `SUPABASE_URL` | Supabase দ্বারা স্বয়ংক্রিয়ভাবে প্রদত্ত |
| `SUPABASE_ANON_KEY` | Supabase দ্বারা স্বয়ংক্রিয়ভাবে প্রদত্ত |
| `SUPABASE_SERVICE_ROLE_KEY` | স্বয়ংক্রিয়ভাবে প্রদত্ত; RLS এড়িয়ে profiles পড়ে |

### Resource Netlify সাইট (প্রতি সাইট)
| Variable | বিবরণ |
|----------|-------------|
| `RESOURCE_TOKEN_SECRET` | উপরের মতোই একই HMAC key |
| `RESOURCE_ID` | অনন্য slug: `rq-builder`, `toc-workbench-pro`, `code-convert-pro`, `qual-insights`, `vaniscribe`, `devdata-practice`, `viz-cookbook`, `devecon-toolkit`, `field-notes-pro`, `toc-workshop-pro`, `logframe-pro`, `chart-selector-pro`, `stakeholder-pro`, `empathy-pro`, `policy-canvas-pro`, `ai-canvas-pro` |

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

| Table | উদ্দেশ্য |
|-------|---------|
| `profiles` | ব্যবহারকারী অ্যাকাউন্ট, tier, streak, আগ্রহ |
| `user_progress` | প্রতি-কোর্স অগ্রগতি ট্র্যাকিং |
| `bookmarks` | ব্যবহারকারী বুকমার্ক |
| `user_notes` | ব্যক্তিগত নোট |
| `certificates` | badge metadata সহ জারি করা সার্টিফিকেট |
| `payments` | পেমেন্ট ইতিহাস |
| `coaching_bookings` | কোচিং সেশন বুকিং |
| `organizations` | সংস্থার রেকর্ড |
| `organization_members` | ব্যবহারকারী ↔ সংস্থা সদস্যপদ |
| `learning_paths` | কাস্টম সংস্থা শেখার পথ |
| `learning_path_assignments` | নির্ধারিত তারিখ সহ পথ ↔ ব্যবহারকারী অ্যাসাইনমেন্ট |
| `portfolio_items` | ব্যবহারকারী পোর্টফোলিও এন্ট্রি |
| `challenge_submissions` | লাইভ কেস চ্যালেঞ্জ জমা |
| `challenge_requests` | সংস্থাগুলির থেকে কাস্টম চ্যালেঞ্জ অনুরোধ |
| `cohorts` | শুরু/শেষের তারিখ সহ প্রশিক্ষণ cohorts (v10.8.0) |
| `cohort_members` | Cohort নথিভুক্তি + অগ্রগতি ট্র্যাকিং (v10.8.0) |
| `cohort_discussions` | cohorts-এর মধ্যে আলোচনা থ্রেড (v10.8.0) |
| `notifications` | ইন-অ্যাপ + ইমেল বিজ্ঞপ্তি লগ (v10.8.0) |
| `notification_preferences` | প্রতি-ব্যবহারকারী ইমেল opt-in/out (v10.8.0) |
| `course_content` | Edge Function-এর মাধ্যমে পরিবেশিত ডায়নামিক কোর্স HTML |
| `badge_shares` | Badge শেয়ারিং ট্র্যাকিং |

## Supabase Edge Functions

| Function | উদ্দেশ্য |
|----------|---------|
| `mint-resource-token` | প্রিমিয়াম resource অ্যাক্সেসের জন্য JWT minting |
| `issue-certificate` | কোর্স সম্পূর্ণ হওয়ায় সার্টিফিকেট জারি |
| `game-agent` | গেমের জন্য MiroFish AI agent engine (multi-provider LLM) |
| `serve-course-content` | ডায়নামিক কোর্স কনটেন্ট পরিবেশন |
| `send-notification` | ইমেল বিজ্ঞপ্তি: streak রিমাইন্ডার, cohort ডেডলাইন, ম্যানুয়াল (v10.8.0) |

## ফাইল কাঠামো

সম্পূর্ণ ডিরেক্টরি লেআউটের জন্য [README → Project Structure](https://github.com/ImpactMojo/ImpactMojo#project-structure) দেখুন।
