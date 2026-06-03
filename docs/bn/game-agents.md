# AI গেম এজেন্ট — MiroFish-অনুপ্রাণিত প্রতিপক্ষ

## সারসংক্ষেপ

ImpactMojo-র গেমগুলিতে **AI-চালিত প্রতিপক্ষ** রয়েছে, যা [MiroFish](https://github.com/666ghj/MiroFish) দ্বারা অনুপ্রাণিত — এটি একটি ওপেন-সোর্স ঝাঁক বুদ্ধিমত্তা ইঞ্জিন। সরল নিয়ম-ভিত্তিক প্রতিদান গণনার পরিবর্তে, গেমগুলিতে স্বতন্ত্র ব্যক্তিত্ব, স্মৃতি এবং অভিযোজনযোগ্য কৌশল সম্পন্ন AI এজেন্ট রয়েছে — যার সবকিছুই দক্ষিণ এশীয় উন্নয়ন প্রেক্ষাপটে প্রোথিত।

প্রতিটি গেম ছয়টি ঐতিহ্যবাহী শৈলীতে (ওয়ারলি, মধুবনী, গোন্ড, কলমকারি, পিছওয়াই, পট্টচিত্র) **ভারতীয় লোকশিল্প গল্পের চিত্রায়ণ** দিয়ে সমৃদ্ধ, যা আখ্যানগত প্রেক্ষাপট প্রদান করে এবং খেলোয়াড়ের পছন্দ অনুযায়ী মানিয়ে নেয়। শিল্প শৈলী সম্পর্কে বিস্তারিত জানতে [Games Guide](games-guide.md) দেখুন।

## স্থাপত্য

```
┌─────────────────────┐     POST /game-agent     ┌──────────────────────────┐
│  Game Frontend       │ ──────────────────────→  │  Supabase Edge Function   │
│  (impactmojo.in)     │ ←──────────────────────  │  game-agent/index.ts      │
│                       │    agent decision JSON   │                            │
│  Uses: game-agents.js │                          │  ┌─── LLM API ──────────┐ │
└─────────────────────┘                          │  │  (Haiku / GPT-4o-mini)│ │
                                                   │  └───────────────────────┘ │
                                                   │  ┌─── Fallback Engine ───┐ │
                                                   │  │  (personality weights) │ │
                                                   │  └───────────────────────┘ │
                                                   └──────────────────────────┘
```

### দুটি মোড

1. **LLM Mode** (Professional/Organization স্তর): প্রতিটি এজেন্ট সিদ্ধান্ত একটি LLM কল দ্বারা চালিত হয়। এজেন্ট চরিত্রে অটুট থাকে, গেমের ইতিহাস মনে রাখে, এবং স্বাভাবিক ভাষায় যুক্তি তৈরি করে। খরচ: প্রতি গেম সেশনে ~$0.015।

2. **Fallback Mode** (Free/Practitioner স্তর বা অফলাইন): একটি হালকা ইঞ্জিন ব্যক্তিত্বের ওজন (cooperation_bias, risk_tolerance, memory_weight) ব্যবহার করে ব্রাউজারেই স্থানীয়ভাবে সিদ্ধান্ত তৈরি করে। কোনো API কল প্রয়োজন নেই।

## ফাইল

| ফাইল | উদ্দেশ্য |
|------|---------|
| `data/game-agents.json` | এজেন্ট পার্সোনা — নাম, পটভূমির গল্প, ব্যক্তিত্বের ওজন, কৌশল ইঙ্গিত |
| `supabase/functions/game-agent/index.ts` | Edge Function — prompt নির্মাতা, LLM কলার, fallback ইঞ্জিন |
| `js/game-agents.js` | ক্লায়েন্ট লাইব্রেরি — এজেন্ট সিদ্ধান্ত পেতে গেমগুলি এটি অন্তর্ভুক্ত করে |
| `js/state-manager.js` | স্টেট — AI গেম সেশন ট্র্যাক করতে `gameSession` এবং `gameHistory` |
| `catalog_data.json` | মেটাডেটা — প্রতিটি গেম এন্ট্রিতে `ai_agents` ক্ষেত্র |

## এজেন্ট পার্সোনা

প্রতিটি গেমে স্বতন্ত্র আদিরূপ সম্পন্ন 2–4টি এজেন্ট রয়েছে:

### Public Good Game
| এজেন্ট | আদিরূপ | সহযোগিতা | বিবরণ |
|-------|-----------|-------------|-------------|
| Meera | শর্তসাপেক্ষ সহযোগী | 0.8 | NGO ম্যানেজার, দলের আচরণ প্রতিফলিত করেন |
| Arjun | কৌশলগত ফ্রি-রাইডার | 0.25 | পরামর্শদাতা, অবদান কমিয়ে রাখেন |
| Fatima | পারস্পরিকতাকারী | 0.6 | স্বাস্থ্যকর্মী, দলের গড়ের সাথে মেলান |
| Ravi | নিঃশর্ত সহযোগী | 0.95 | প্রভাষক, যাই হোক অবদান রাখেন |

### Prisoners' Dilemma
| এজেন্ট | আদিরূপ | কৌশল |
|-------|-----------|----------|
| Sunita | Tit-for-tat | প্রথমে সহযোগিতা করেন, প্রতিপক্ষকে প্রতিফলিত করেন |
| Vikram | Grudger | বিশ্বাসঘাতকতা না হওয়া পর্যন্ত সহযোগিতা করেন, তারপর চিরকালের জন্য সরে যান |
| Lakshmi | Pavlov | জিতলে-থাকো, হারলে-বদলাও |
| Deepak | অননুমেয় | এলোমেলো মিশ্রণ, শোষণ করা কঠিন |

### Commons Crisis
| এজেন্ট | আদিরূপ | আহরণের প্রবণতা |
|-------|-----------|-------------------|
| Priya | টেকসইতা-প্রথম | কম আহরণ, সীমার পক্ষে ওকালতি করেন |
| Raj | স্বল্পমেয়াদী অপ্টিমাইজার | উচ্চ আহরণ, কেবল নিষেধাজ্ঞায় সাড়া দেন |
| Ananya | প্রাতিষ্ঠানিক নির্মাতা | মধ্যম, শাসনব্যবস্থার জন্য চাপ দেন |
| Karthik | নিয়ম-অনুসরণকারী | দলের গড়ের সাথে মেলান |

(সমস্ত 10টি AI-সক্ষম গেম জুড়ে সম্পূর্ণ পার্সোনা সংজ্ঞার জন্য `data/game-agents.json` দেখুন।)

## ইন্টিগ্রেশন গাইড (Game Frontends-এর জন্য)

### 1. ক্লায়েন্ট লাইব্রেরি অন্তর্ভুক্ত করুন

```html
<script src="https://www.impactmojo.in/js/game-agents.js"></script>
```

### 2. আপনার গেমের জন্য আরম্ভ করুন

```javascript
var agents = new IMGameAgents('public-good-game');
```

### 3. এজেন্ট তালিকা পান (UI-এর জন্য)

```javascript
agents.getRoster().then(function(roster) {
  roster.forEach(function(agent) {
    // Display agent name, role, location, personality in game UI
    addAgentCard(agent.name, agent.role, agent.location, agent.personality.archetype);
  });
});
```

### 4. প্রতি রাউন্ডে সিদ্ধান্তের জন্য অনুরোধ করুন

```javascript
agents.getAllDecisions({
  round: currentRound,
  totalRounds: 10,
  history: gameHistory,          // array of past rounds
  availableActions: ['contribute'],
  context: { max_contribution: 100 }
}).then(function(decisions) {
  // decisions = { 'pg-altruist': { action, amount, reasoning }, ... }
  Object.keys(decisions).forEach(function(agentId) {
    var d = decisions[agentId];
    updateGameState(agentId, d.action, d.amount);
    showAgentReasoning(agentId, d.reasoning);  // optional: show why
  });
});
```

### 5. সেশন স্টেট ট্র্যাক করুন

```javascript
// Save session after each round (for resume capability)
IMState.gameSession.set('public-good-game', {
  round: currentRound,
  history: gameHistory,
  agentDecisions: allDecisions,
  playerScore: playerScore,
  timestamp: new Date().toISOString()
});

// On game completion, add to history
IMState.gameHistory.add({
  gameId: 'public-good-game',
  completedAt: new Date().toISOString(),
  rounds: 10,
  playerScore: finalScore,
  usedLLM: true
});
```

## ডিপ্লয়মেন্ট

### এনভায়রনমেন্ট ভেরিয়েবল

এগুলি `supabase secrets set` এর মাধ্যমে সেট করুন:

```bash
supabase secrets set LLM_API_KEY=sk-...
supabase secrets set LLM_BASE_URL=https://api.openai.com/v1
supabase secrets set LLM_MODEL=gpt-4o-mini
```

Anthropic Claude-এর জন্য (সামঞ্জস্যপূর্ণ এন্ডপয়েন্টের মাধ্যমে):
```bash
supabase secrets set LLM_API_KEY=sk-ant-...
supabase secrets set LLM_BASE_URL=https://api.anthropic.com/v1
supabase secrets set LLM_MODEL=claude-haiku-4-5-20251001
```

### Edge Function ডিপ্লয় করুন

```bash
supabase functions deploy game-agent
```

### খরচ ব্যবস্থাপনা

- Free এবং Practitioner স্তরগুলি **fallback ইঞ্জিন** ব্যবহার করে (শূন্য LLM খরচ)
- Professional স্তর LLM-চালিত এজেন্ট পায় (GPT-4o-mini সহ ~$0.015/সেশন)
- প্রতি ব্যবহারকারীর জন্য প্রতি মিনিটে 30টি অনুরোধে রেট সীমিত
- মাসে 1,000 সেশনে: মোট LLM খরচ ~$10–15/মাস

## সম্প্রসারণ

### একটি নতুন এজেন্ট যোগ করা

উপযুক্ত গেমের অধীনে `data/game-agents.json`-এ একটি এন্ট্রি যোগ করুন:

```json
{
  "id": "pg-new-agent",
  "name": "Devi",
  "role": "Village Sarpanch",
  "location": "Rajkot, Gujarat",
  "personality": {
    "archetype": "authority-figure",
    "cooperation_bias": 0.7,
    "risk_tolerance": 0.4,
    "memory_weight": 0.8,
    "description": "Uses positional authority to enforce cooperation norms."
  },
  "backstory": "Elected village leader who enforces social contracts.",
  "strategy_hint": "Contribute above average. Punish lowest contributors verbally."
}
```

### একটি নতুন গেম যোগ করা

1. `data/game-agents.json`-এ `games` এর অধীনে একটি নতুন গেম কী যোগ করুন
2. প্রাসঙ্গিক আদিরূপ সহ 2–4টি এজেন্ট সংজ্ঞায়িত করুন
3. fallback ইঞ্জিনে (Edge Function এবং ক্লায়েন্ট লাইব্রেরি উভয়েই) অ্যাকশন হ্যান্ডলিং যোগ করুন
4. `catalog_data.json`-কে `ai_agents` ক্ষেত্র দিয়ে আপডেট করুন

## নকশার নীতি

1. **দক্ষিণ এশীয় প্রেক্ষাপট**: প্রতিটি এজেন্ট এই অঞ্চলের একজন বাস্তব উন্নয়ন কর্মী, আমলা, উদ্যোক্তা বা সম্প্রদায়ের সদস্য।
2. **শিক্ষাগতভাবে অর্থপূর্ণ**: এজেন্ট আদিরূপগুলি বাস্তব অর্থনৈতিক আচরণের ধরন (tit-for-tat, free-rider, conditional cooperator) এর সাথে সঙ্গতিপূর্ণ, যা শিক্ষার্থীরা ডিব্রিফে শেখে।
3. **মার্জিত অবনমন**: গেমগুলি LLM ছাড়া (fallback ইঞ্জিন), ইন্টারনেট ছাড়া (ক্যাশড এজেন্ট ডেটা), এবং লগইন ছাড়া (বিনামূল্যের মোডে কোনো অথ প্রয়োজন নেই) কাজ করে।
4. **খরচ-সচেতন**: LLM কলগুলি সবচেয়ে সস্তা পর্যাপ্ত মডেল ব্যবহার করে। ব্যক্তিত্বের ওজন API কল ছাড়াই বেশিরভাগ সিদ্ধান্ত পরিচালনা করে।
