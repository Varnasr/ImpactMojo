# AI गेम एजंट — MiroFish-प्रेरित प्रतिस्पर्धी

## आढावा

ImpactMojo च्या गेम्समध्ये **AI-चालित प्रतिस्पर्धी** आहेत, जे [MiroFish](https://github.com/666ghj/MiroFish) या ओपन-सोर्स स्वार्म इंटेलिजन्स इंजिनने प्रेरित आहेत. साध्या नियम-आधारित परतावा गणनेऐवजी, गेम्समध्ये वेगळी व्यक्तिमत्त्वे, स्मृती आणि अनुकूल रणनीती असलेले AI एजंट आहेत — हे सर्व दक्षिण आशियाई विकास संदर्भांत रुजलेले आहेत.

प्रत्येक गेम सहा पारंपरिक शैलींमध्ये (वारली, मधुबनी, गोंड, कलमकारी, पिछवाई, पट्टचित्र) **भारतीय लोककला कथा चित्रणाने** समृद्ध केला आहे, जे कथानक संदर्भ पुरवतात आणि खेळाडूच्या निवडींनुसार जुळवून घेतात. कला शैलींबद्दल तपशीलांसाठी [Games Guide](games-guide.md) पाहा.

## स्थापत्य

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

### दोन मोड

1. **LLM Mode** (Professional/Organization स्तर): प्रत्येक एजंट निर्णय एका LLM कॉलने चालवला जातो. एजंट आपल्या भूमिकेत राहतो, गेमचा इतिहास लक्षात ठेवतो आणि नैसर्गिक भाषेत तर्क तयार करतो. खर्च: प्रति गेम सत्र ~$0.015.

2. **Fallback Mode** (Free/Practitioner स्तर किंवा ऑफलाइन): एक हलके इंजिन व्यक्तिमत्त्व वजने (cooperation_bias, risk_tolerance, memory_weight) वापरून ब्राउझरमध्येच स्थानिक पातळीवर निर्णय तयार करते. कोणत्याही API कॉलची गरज नाही.

## फायली

| फाईल | उद्देश |
|------|---------|
| `data/game-agents.json` | एजंट व्यक्तिरेखा — नावे, पार्श्वकथा, व्यक्तिमत्त्व वजने, रणनीती संकेत |
| `supabase/functions/game-agent/index.ts` | Edge Function — prompt निर्माता, LLM कॉलर, fallback इंजिन |
| `js/game-agents.js` | क्लायंट लायब्ररी — एजंट निर्णय मिळवण्यासाठी गेम्स हे समाविष्ट करतात |
| `js/state-manager.js` | स्थिती — AI गेम सत्रांचा मागोवा घेण्यासाठी `gameSession` आणि `gameHistory` |
| `catalog_data.json` | मेटाडेटा — प्रत्येक गेम नोंदीवर `ai_agents` फील्ड |

## एजंट व्यक्तिरेखा

प्रत्येक गेममध्ये वेगळ्या आदिप्रकारांचे 2–4 एजंट आहेत:

### Public Good Game
| एजंट | आदिप्रकार | सहकार्य | वर्णन |
|-------|-----------|-------------|-------------|
| Meera | सशर्त सहकारी | 0.8 | NGO व्यवस्थापक, गटाच्या वर्तनाचे प्रतिबिंब |
| Arjun | धोरणात्मक फ्री-रायडर | 0.25 | सल्लागार, योगदान कमी ठेवतो |
| Fatima | परस्परवादी | 0.6 | आरोग्यसेविका, गट सरासरीशी जुळवते |
| Ravi | बिनशर्त सहकारी | 0.95 | व्याख्याता, काहीही असो योगदान देतो |

### Prisoners' Dilemma
| एजंट | आदिप्रकार | रणनीती |
|-------|-----------|----------|
| Sunita | Tit-for-tat | प्रथम सहकार्य करते, प्रतिस्पर्ध्याचे प्रतिबिंब |
| Vikram | Grudger | विश्वासघात होईपर्यंत सहकार्य, मग कायमचे माघार |
| Lakshmi | Pavlov | जिंकल्यास राहा, हरल्यास बदला |
| Deepak | अप्रत्याशित | यादृच्छिक मिश्रण, शोषण करणे कठीण |

### Commons Crisis
| एजंट | आदिप्रकार | उत्खनन प्रवृत्ती |
|-------|-----------|-------------------|
| Priya | शाश्वतता-प्रथम | कमी उत्खनन, मर्यादांचे समर्थन |
| Raj | अल्प-मुदत अनुकूलक | जास्त उत्खनन, फक्त निर्बंधांना प्रतिसाद |
| Ananya | संस्थात्मक निर्माता | मध्यम, प्रशासनासाठी आग्रह |
| Karthik | नियम-पालक | गट सरासरीशी जुळवतो |

(सर्व 10 AI-सक्षम गेम्समधील संपूर्ण व्यक्तिरेखा व्याख्यांसाठी `data/game-agents.json` पाहा.)

## एकत्रीकरण मार्गदर्शक (Game Frontends साठी)

### 1. क्लायंट लायब्ररी समाविष्ट करा

```html
<script src="https://www.impactmojo.in/js/game-agents.js"></script>
```

### 2. तुमच्या गेमसाठी आरंभ करा

```javascript
var agents = new IMGameAgents('public-good-game');
```

### 3. एजंट यादी मिळवा (UI साठी)

```javascript
agents.getRoster().then(function(roster) {
  roster.forEach(function(agent) {
    // Display agent name, role, location, personality in game UI
    addAgentCard(agent.name, agent.role, agent.location, agent.personality.archetype);
  });
});
```

### 4. प्रत्येक फेरीत निर्णयांची विनंती करा

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

### 5. सत्र स्थितीचा मागोवा घ्या

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

## डिप्लॉयमेंट

### एन्व्हायर्नमेंट व्हेरिएबल्स

हे `supabase secrets set` द्वारे सेट करा:

```bash
supabase secrets set LLM_API_KEY=sk-...
supabase secrets set LLM_BASE_URL=https://api.openai.com/v1
supabase secrets set LLM_MODEL=gpt-4o-mini
```

Anthropic Claude साठी (सुसंगत एंडपॉइंटद्वारे):
```bash
supabase secrets set LLM_API_KEY=sk-ant-...
supabase secrets set LLM_BASE_URL=https://api.anthropic.com/v1
supabase secrets set LLM_MODEL=claude-haiku-4-5-20251001
```

### Edge Function डिप्लॉय करा

```bash
supabase functions deploy game-agent
```

### खर्च व्यवस्थापन

- Free आणि Practitioner स्तर **fallback इंजिन** वापरतात (शून्य LLM खर्च)
- Professional स्तराला LLM-चालित एजंट मिळतात (GPT-4o-mini सह ~$0.015/सत्र)
- प्रति वापरकर्ता प्रति मिनिट 30 विनंत्या असा दर मर्यादित
- दरमहा 1,000 सत्रांवर: एकूण LLM खर्च ~$10–15/महिना

## विस्तार

### नवीन एजंट जोडणे

योग्य गेमखाली `data/game-agents.json` मध्ये एक नोंद जोडा:

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

### नवीन गेम जोडणे

1. `data/game-agents.json` मध्ये `games` खाली नवीन गेम की जोडा
2. संबंधित आदिप्रकारांसह 2–4 एजंट परिभाषित करा
3. fallback इंजिनमध्ये (Edge Function आणि क्लायंट लायब्ररी दोन्हीमध्ये) अॅक्शन हाताळणी जोडा
4. `catalog_data.json` ला `ai_agents` फील्डसह अद्यतनित करा

## रचना तत्त्वे

1. **दक्षिण आशियाई संदर्भ**: प्रत्येक एजंट या प्रदेशातील एक वास्तविक विकास व्यावसायिक, नोकरशहा, उद्योजक किंवा समुदाय सदस्य आहे.
2. **शैक्षणिकदृष्ट्या अर्थपूर्ण**: एजंट आदिप्रकार वास्तविक आर्थिक वर्तन प्रकारांशी (tit-for-tat, free-rider, conditional cooperator) जुळतात, जे विद्यार्थी डिब्रीफमध्ये शिकतात.
3. **सुंदर अवनती**: गेम्स LLM शिवाय (fallback इंजिन), इंटरनेटशिवाय (कॅश्ड एजंट डेटा), आणि लॉगिनशिवाय (मोफत मोडसाठी प्रमाणीकरण आवश्यक नाही) कार्य करतात.
4. **खर्च-जागरूक**: LLM कॉल सर्वात स्वस्त पुरेसे मॉडेल वापरतात. बहुतेक निर्णय व्यक्तिमत्त्व वजने API कॉलशिवाय हाताळतात.
