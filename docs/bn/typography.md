# টাইপোগ্রাফি

## ফন্ট স্ট্যাক

ImpactMojo সমস্ত 242+ পৃষ্ঠা জুড়ে একটি প্রমিত তিন-ফন্ট ব্যবস্থা ব্যবহার করে:

| ভূমিকা | ফন্ট | ওজন | ফলব্যাক |
|------|------|---------|----------|
| **শিরোনাম** | Inter | 400, 500, 600, 700, 800 | sans-serif |
| **মূল লেখা** | Amaranth | 400, 700 | sans-serif |
| **কোড / monospace** | JetBrains Mono | 400 | monospace |
| **বহুভাষিক** | Noto Sans (দেবনাগরী, বাংলা, তামিল, তেলুগু) | 400, 700 | sans-serif |

## Google Fonts লোডিং

সমস্ত পৃষ্ঠা একটি একক Google Fonts URL-এর মাধ্যমে ফন্ট লোড করে:

```html
<link href="https://fonts.googleapis.com/css2?family=Amaranth:wght@400;700&family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono&family=Noto+Sans:wght@400;700&display=swap" rel="stylesheet">
```

## ডিজাইন টোকেন

### ফন্ট পরিবার

```css
--font-heading: 'Inter', sans-serif;
--font-body: 'Amaranth', sans-serif;
--font-mono: 'JetBrains Mono', monospace;
```

### ফন্টের আকার

| টোকেন | আকার | ব্যবহার |
|-------|------|-------|
| `--text-xs` | 0.75rem | লেবেল, ক্যাপশন |
| `--text-sm` | 0.875rem | গৌণ লেখা, মেটাডেটা |
| `--text-base` | 1rem | মূল লেখা |
| `--text-lg` | 1.125rem | লিড অনুচ্ছেদ |
| `--text-xl` | 1.25rem | বিভাগ শিরোনাম (h3) |
| `--text-2xl` | 1.5rem | পৃষ্ঠা শিরোনাম (h2) |
| `--text-3xl` | 1.875rem | হিরো শিরোনাম (h1) |

### ফন্টের ওজন

| টোকেন | ওজন | ব্যবহার |
|-------|--------|-------|
| `--font-normal` | 400 | মূল লেখা |
| `--font-medium` | 500 | নেভিগেশন, বোতাম |
| `--font-semibold` | 600 | উপশিরোনাম |
| `--font-bold` | 700 | শিরোনাম, জোর |
| `--font-extrabold` | 800 | হিরো লেখা |

## এনকোডিং

সমস্ত HTML ফাইল UTF-8 এনকোডিং ব্যবহার করে:

```html
<meta charset="UTF-8">
```

এটি নিম্নলিখিতগুলির সঠিক রেন্ডারিং নিশ্চিত করে:
- হিন্দি (हिन्दी), বাংলা (বাংলা), তামিল (தமிழ்), তেলুগু (తెలుగు)
- শিক্ষামূলক বিষয়বস্তুতে বিশেষ অক্ষর (em-dashes, smart quotes, ইত্যাদি)

## পূর্ববর্তী ফন্ট (v10.0.0-এ সরানো হয়েছে)

v10.0.0 টাইপোগ্রাফি প্রমিতকরণের সময় নিম্নলিখিত ফন্টগুলি সরানো হয়েছিল:

- Poppins (শিরোনামের জন্য Inter দ্বারা প্রতিস্থাপিত)
- Fraunces (সরানো হয়েছে)
- Merriweather (সরানো হয়েছে)
- Source Serif 4 (সরানো হয়েছে)
- Source Sans 3 (সরানো হয়েছে)
- Cormorant Garamond (সরানো হয়েছে)
- Georgia (ফলব্যাক চেইন থেকে সরানো হয়েছে)
