# AI गेम एजेंट — MiroFish से प्रेरित प्रतिद्वंद्वी

## अवलोकन

ImpactMojo के गेम्स में **AI-संचालित प्रतिद्वंद्वी** शामिल हैं, जो एक ओपन-सोर्स स्वार्म इंटेलिजेंस इंजन [MiroFish](https://github.com/666ghj/MiroFish) से प्रेरित हैं। साधारण नियम-आधारित पेऑफ गणनाओं के बजाय, इन गेम्स में अलग-अलग व्यक्तित्व, स्मृति और अनुकूली रणनीतियों वाले AI एजेंट होते हैं — ये सभी दक्षिण एशियाई विकास संदर्भों पर आधारित हैं।

हर गेम को छह पारंपरिक शैलियों (वारली, मधुबनी, गोंड, कलमकारी, पिछवाई, पट्टचित्र) में बनी **भारतीय लोक कला कहानी चित्रों** से भी समृद्ध किया गया है, जो कथात्मक संदर्भ प्रदान करते हैं और खिलाड़ी के विकल्पों के अनुसार ढल जाते हैं। कला शैलियों के विवरण के लिए [Games Guide](games-guide.md) देखें।

## आर्किटेक्चर

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

### दो मोड

1. **LLM मोड** (Professional/Organization टियर): हर एजेंट का निर्णय एक LLM कॉल द्वारा संचालित होता है। एजेंट अपने किरदार में बना रहता है, गेम का इतिहास याद रखता है, और स्वाभाविक भाषा में तर्क प्रस्तुत करता है। लागत: प्रति गेम सत्र ~$0.015।

2. **Fallback मोड** (Free/Practitioner टियर या ऑफ़लाइन): एक हल्का इंजन व्यक्तित्व भारों (cooperation_bias, risk_tolerance, memory_weight) का उपयोग करके ब्राउज़र में ही स्थानीय रूप से निर्णय लेता है। किसी API कॉल की आवश्यकता नहीं।

## फ़ाइलें

| फ़ाइल | उद्देश्य |
|------|---------|
| `data/game-agents.json` | एजेंट व्यक्तित्व — नाम, पृष्ठभूमि कथाएँ, व्यक्तित्व भार, रणनीति संकेत |
| `supabase/functions/game-agent/index.ts` | Edge Function — प्रॉम्प्ट बिल्डर, LLM कॉलर, fallback इंजन |
| `js/game-agents.js` | क्लाइंट लाइब्रेरी — एजेंट निर्णय प्राप्त करने के लिए गेम इसे शामिल करते हैं |
| `js/state-manager.js` | स्टेट — AI गेम सत्रों को ट्रैक करने के लिए `gameSession` और `gameHistory` |
| `catalog_data.json` | मेटाडेटा — प्रत्येक गेम प्रविष्टि पर `ai_agents` फ़ील्ड |

## एजेंट व्यक्तित्व

हर गेम में अलग-अलग आदर्श रूपों (archetypes) वाले 2–4 एजेंट होते हैं:

### Public Good Game
| एजेंट | आदर्श रूप | सहयोग | विवरण |
|-------|-----------|-------------|-------------|
| Meera | सशर्त सहयोगी | 0.8 | NGO प्रबंधक, समूह के व्यवहार का अनुसरण करती है |
| Arjun | रणनीतिक फ्री-राइडर | 0.25 | परामर्शदाता, योगदान न्यूनतम रखता है |
| Fatima | प्रत्युपकारी | 0.6 | स्वास्थ्य कार्यकर्ता, समूह औसत से मेल खाती है |
| Ravi | बिना शर्त सहयोगी | 0.95 | व्याख्याता, चाहे कुछ भी हो योगदान देता है |

### Prisoners' Dilemma
| एजेंट | आदर्श रूप | रणनीति |
|-------|-----------|----------|
| Sunita | टिट-फॉर-टैट | पहले सहयोग करती है, प्रतिद्वंद्वी का अनुसरण करती है |
| Vikram | द्वेषधारी | विश्वासघात तक सहयोग करता है, फिर हमेशा के लिए मुकर जाता है |
| Lakshmi | पावलोव | जीतो तो टिके रहो, हारो तो बदलो |
| Deepak | अप्रत्याशित | यादृच्छिक मिश्रण, जिसका लाभ उठाना कठिन है |

### Commons Crisis
| एजेंट | आदर्श रूप | निष्कर्षण प्रवृत्ति |
|-------|-----------|-------------------|
| Priya | स्थिरता-प्रथम | कम निष्कर्षण, सीमाओं की वकालत करती है |
| Raj | अल्पकालिक अनुकूलक | अधिक निष्कर्षण, केवल प्रतिबंधों पर प्रतिक्रिया देता है |
| Ananya | संस्था निर्माता | मध्यम, अभिशासन के लिए दबाव डालती है |
| Karthik | मानदंड-अनुयायी | समूह औसत से मेल खाता है |

(सभी 10 AI-सक्षम गेम्स के पूर्ण व्यक्तित्व परिभाषाओं के लिए `data/game-agents.json` देखें।)

## एकीकरण मार्गदर्शिका (गेम फ्रंटएंड के लिए)

### 1. क्लाइंट लाइब्रेरी शामिल करें

```html
<script src="https://www.impactmojo.in/js/game-agents.js"></script>
```

### 2. अपने गेम के लिए आरंभ करें

```javascript
var agents = new IMGameAgents('public-good-game');
```

### 3. एजेंट रोस्टर प्राप्त करें (UI के लिए)

```javascript
agents.getRoster().then(function(roster) {
  roster.forEach(function(agent) {
    // Display agent name, role, location, personality in game UI
    addAgentCard(agent.name, agent.role, agent.location, agent.personality.archetype);
  });
});
```

### 4. हर राउंड में निर्णय का अनुरोध करें

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

### 5. सत्र स्टेट ट्रैक करें

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

## परिनियोजन (Deployment)

### एनवायरनमेंट वेरिएबल्स

इन्हें `supabase secrets set` के माध्यम से सेट करें:

```bash
supabase secrets set LLM_API_KEY=sk-...
supabase secrets set LLM_BASE_URL=https://api.openai.com/v1
supabase secrets set LLM_MODEL=gpt-4o-mini
```

Anthropic Claude के लिए (एक संगत एंडपॉइंट के माध्यम से):
```bash
supabase secrets set LLM_API_KEY=sk-ant-...
supabase secrets set LLM_BASE_URL=https://api.anthropic.com/v1
supabase secrets set LLM_MODEL=claude-haiku-4-5-20251001
```

### Edge Function परिनियोजित करें

```bash
supabase functions deploy game-agent
```

### लागत प्रबंधन

- Free और Practitioner टियर **fallback इंजन** का उपयोग करते हैं (शून्य LLM लागत)
- Professional टियर को LLM-संचालित एजेंट मिलते हैं (GPT-4o-mini के साथ ~$0.015/सत्र)
- प्रति उपयोगकर्ता 30 अनुरोध/मिनट तक सीमित
- 1,000 सत्र/माह पर: कुल LLM लागत ~$10–15/माह

## विस्तार करना

### नया एजेंट जोड़ना

उपयुक्त गेम के अंतर्गत `data/game-agents.json` में एक प्रविष्टि जोड़ें:

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

### नया गेम जोड़ना

1. `data/game-agents.json` में `games` के अंतर्गत एक नई गेम कुंजी जोड़ें
2. प्रासंगिक आदर्श रूपों के साथ 2–4 एजेंट परिभाषित करें
3. fallback इंजन में एक्शन हैंडलिंग जोड़ें (Edge Function और क्लाइंट लाइब्रेरी दोनों में)
4. `catalog_data.json` को `ai_agents` फ़ील्ड के साथ अपडेट करें

## डिज़ाइन सिद्धांत

1. **दक्षिण एशियाई संदर्भ**: प्रत्येक एजेंट क्षेत्र का एक यथार्थवादी विकास व्यवसायी, नौकरशाह, उद्यमी या समुदाय सदस्य है।
2. **शैक्षणिक रूप से सार्थक**: एजेंट आदर्श रूप वास्तविक आर्थिक व्यवहार प्रकारों (टिट-फॉर-टैट, फ्री-राइडर, सशर्त सहयोगी) से मेल खाते हैं, जिन्हें छात्र डीब्रीफ में सीखते हैं।
3. **सुगठित ह्रास (graceful degradation)**: गेम बिना LLM के (fallback इंजन), बिना इंटरनेट के (कैश किया गया एजेंट डेटा), और बिना लॉगिन के (मुफ़्त मोड के लिए कोई auth आवश्यक नहीं) काम करते हैं।
4. **लागत के प्रति सजग**: LLM कॉल सबसे सस्ते पर्याप्त मॉडल का उपयोग करते हैं। व्यक्तित्व भार अधिकांश निर्णयों को बिना API कॉल के संभालते हैं।
