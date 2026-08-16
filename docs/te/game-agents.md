# AI గేమ్ ఏజెంట్లు — MiroFish-ప్రేరిత ప్రత్యర్థులు

## అవలోకనం

ImpactMojo యొక్క గేమ్‌లు ఓపెన్-సోర్స్ స్వార్మ్ ఇంటెలిజెన్స్ ఇంజిన్ అయిన [MiroFish](https://github.com/666ghj/MiroFish) చే ప్రేరణ పొందిన **AI-ఆధారిత ప్రత్యర్థులను** కలిగి ఉంటాయి. సరళమైన నియమ-ఆధారిత పేఆఫ్ లెక్కల కాకుండా, గేమ్‌లు విభిన్న వ్యక్తిత్వాలు, జ్ఞాపకాలు, మరియు అనుకూల వ్యూహాలతో కూడిన AI ఏజెంట్లను కలిగి ఉంటాయి — అన్నీ దక్షిణాసియా అభివృద్ధి సందర్భాలలో ఆధారపడి ఉంటాయి.

ప్రతి గేమ్ కూడా కథన సందర్భాన్ని అందించి, ఆటగాడి ఎంపికలకు అనుగుణంగా మారే ఆరు సంప్రదాయ శైలులలో (Warli, Madhubani, Gond, Kalamkari, Pichwai, Pattachitra) **భారతీయ జానపద కళ కథా చిత్రాలతో** సమృద్ధం చేయబడింది. కళా శైలులపై వివరాల కోసం [గేమ్‌ల మార్గదర్శి](games-guide.md) చూడండి.

## ఆర్కిటెక్చర్

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

### రెండు మోడ్‌లు

1. **LLM మోడ్** (Professional/Organization శ్రేణి): ప్రతి ఏజెంట్ నిర్ణయం ఒక LLM కాల్ చే శక్తిపొందుతుంది. ఏజెంట్ పాత్రలో ఉంటుంది, గేమ్ చరిత్రను గుర్తుంచుకుంటుంది, మరియు సహజ-భాషా తార్కికాన్ని ఉత్పత్తి చేస్తుంది. ఖర్చు: ఒక్కో గేమ్ సెషన్‌కు ~$0.015.

2. **ఫాల్‌బ్యాక్ మోడ్** (Free/Practitioner శ్రేణి లేదా ఆఫ్‌లైన్): ఒక తేలికపాటి ఇంజిన్ వ్యక్తిత్వ బరువులను (cooperation_bias, risk_tolerance, memory_weight) ఉపయోగించి బ్రౌజర్‌లో స్థానికంగా నిర్ణయాలను ఉత్పత్తి చేస్తుంది. API కాల్‌లు అవసరం లేదు.

## ఫైల్‌లు

| ఫైల్ | ప్రయోజనం |
|------|---------|
| `data/game-agents.json` | ఏజెంట్ వ్యక్తిత్వాలు — పేర్లు, నేపథ్య కథలు, వ్యక్తిత్వ బరువులు, వ్యూహ సూచనలు |
| `supabase/functions/game-agent/index.ts` | Edge Function — ప్రాంప్ట్ బిల్డర్, LLM కాలర్, ఫాల్‌బ్యాక్ ఇంజిన్ |
| `js/game-agents.js` | క్లయింట్ లైబ్రరీ — ఏజెంట్ నిర్ణయాలను పొందడానికి గేమ్‌లు దీన్ని కలిగి ఉంటాయి |
| `js/state-manager.js` | స్టేట్ — AI గేమ్ సెషన్లను ట్రాక్ చేయడానికి `gameSession` మరియు `gameHistory` |
| `catalog_data.json` | మెటాడేటా — ప్రతి గేమ్ ఎంట్రీపై `ai_agents` ఫీల్డ్ |

## ఏజెంట్ వ్యక్తిత్వాలు

ప్రతి గేమ్‌కు విభిన్న ఆర్కిటైప్‌లతో 2–4 ఏజెంట్లు ఉన్నారు:

### Public Good Game
| ఏజెంట్ | ఆర్కిటైప్ | సహకారం | వివరణ |
|-------|-----------|-------------|-------------|
| Meera | షరతుబద్ధ సహకారి | 0.8 | NGO మేనేజర్, సమూహ ప్రవర్తనను ప్రతిబింబిస్తారు |
| Arjun | వ్యూహాత్మక ఫ్రీ-రైడర్ | 0.25 | సలహాదారు, సహకారాన్ని కనిష్టీకరిస్తారు |
| Fatima | ప్రతిఫలదారు | 0.6 | ఆరోగ్య కార్యకర్త, సమూహ సగటుకు సరిపోతారు |
| Ravi | షరతులేని సహకారి | 0.95 | ఉపన్యాసకుడు, ఎలాగైనా సహకరిస్తారు |

### Prisoners' Dilemma
| ఏజెంట్ | ఆర్కిటైప్ | వ్యూహం |
|-------|-----------|----------|
| Sunita | Tit-for-tat | మొదట సహకరిస్తారు, ప్రత్యర్థిని ప్రతిబింబిస్తారు |
| Vikram | పగబట్టేవారు | మోసం చేసే వరకు సహకరిస్తారు, ఆపై శాశ్వతంగా వదిలేస్తారు |
| Lakshmi | Pavlov | గెలిస్తే-ఉండు, ఓడితే-మారు |
| Deepak | అనూహ్యమైనవారు | యాదృచ్ఛిక మిశ్రమం, వినియోగించుకోవడం కష్టం |

### Commons Crisis
| ఏజెంట్ | ఆర్కిటైప్ | వెలికితీత ధోరణి |
|-------|-----------|-------------------|
| Priya | నిలకడ-మొదట | తక్కువ వెలికితీత, పరిమితులను సమర్థిస్తారు |
| Raj | స్వల్ప-కాల ఆప్టిమైజర్ | అధిక వెలికితీత, ఆంక్షలకు మాత్రమే స్పందిస్తారు |
| Ananya | సంస్థాగత నిర్మాత | మధ్యస్థం, పాలన కోసం నెట్టుతారు |
| Karthik | నిబంధన-అనుసరించేవారు | సమూహ సగటుకు సరిపోతారు |

(అన్ని 10 AI-ప్రారంభిత గేమ్‌ల అంతటా పూర్తి వ్యక్తిత్వ నిర్వచనాల కోసం `data/game-agents.json` చూడండి.)

## అనుసంధాన మార్గదర్శి (గేమ్ ఫ్రంటెండ్‌ల కోసం)

### 1. క్లయింట్ లైబ్రరీని చేర్చండి

```html
<script src="https://www.impactmojo.in/js/game-agents.js"></script>
```

### 2. మీ గేమ్ కోసం ప్రారంభించండి

```javascript
var agents = new IMGameAgents('public-good-game');
```

### 3. ఏజెంట్ రోస్టర్‌ను పొందండి (UI కోసం)

```javascript
agents.getRoster().then(function(roster) {
  roster.forEach(function(agent) {
    // Display agent name, role, location, personality in game UI
    addAgentCard(agent.name, agent.role, agent.location, agent.personality.archetype);
  });
});
```

### 4. ప్రతి రౌండ్‌లో నిర్ణయాలను అభ్యర్థించండి

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

### 5. సెషన్ స్టేట్‌ను ట్రాక్ చేయండి

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

## విస్తరణ

### పర్యావరణ వేరియబుల్స్

వీటిని `supabase secrets set` ద్వారా సెట్ చేయండి:

```bash
supabase secrets set LLM_API_KEY=sk-...
supabase secrets set LLM_BASE_URL=https://api.openai.com/v1
supabase secrets set LLM_MODEL=gpt-4o-mini
```

Anthropic Claude కోసం (అనుకూల ఎండ్‌పాయింట్ ద్వారా):
```bash
supabase secrets set LLM_API_KEY=sk-ant-...
supabase secrets set LLM_BASE_URL=https://api.anthropic.com/v1
supabase secrets set LLM_MODEL=claude-haiku-4-5-20251001
```

### Edge Function ను విస్తరించండి

```bash
supabase functions deploy game-agent
```

### ఖర్చు నిర్వహణ

- Free మరియు Practitioner శ్రేణులు **ఫాల్‌బ్యాక్ ఇంజిన్**ను ఉపయోగిస్తాయి (సున్నా LLM ఖర్చు)
- Professional శ్రేణి LLM-ఆధారిత ఏజెంట్లను పొందుతుంది (GPT-4o-mini తో ~$0.015/సెషన్)
- ఒక్కో వినియోగదారుకు నిమిషానికి 30 అభ్యర్థనలకు రేట్ పరిమితం చేయబడింది
- నెలకు 1,000 సెషన్లలో: మొత్తం ~$10–15/నెల LLM ఖర్చు

## విస్తరించడం

### కొత్త ఏజెంట్‌ను జోడించడం

తగిన గేమ్ కింద `data/game-agents.json` కు ఒక ఎంట్రీని జోడించండి:

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

### కొత్త గేమ్‌ను జోడించడం

1. `data/game-agents.json` లో `games` కింద ఒక కొత్త గేమ్ కీని జోడించండి
2. సంబంధిత ఆర్కిటైప్‌లతో 2–4 ఏజెంట్లను నిర్వచించండి
3. ఫాల్‌బ్యాక్ ఇంజిన్‌లో యాక్షన్ నిర్వహణను జోడించండి (Edge Function మరియు క్లయింట్ లైబ్రరీ రెండింటిలో)
4. `catalog_data.json` ను `ai_agents` ఫీల్డ్‌తో నవీకరించండి

## రూపకల్పన సూత్రాలు

1. **దక్షిణాసియా సందర్భం**: ప్రతి ఏజెంట్ ఈ ప్రాంతం నుండి ఒక వాస్తవిక అభివృద్ధి అభ్యాసకుడు, అధికారి, వ్యవస్థాపకుడు, లేదా సమాజ సభ్యుడు.
2. **బోధనాత్మకంగా అర్థవంతమైనది**: ఏజెంట్ ఆర్కిటైప్‌లు విద్యార్థులు విశ్లేషణలో నేర్చుకునే నిజమైన ఆర్థిక ప్రవర్తన రకాలకు (tit-for-tat, free-rider, షరతుబద్ధ సహకారి) మ్యాప్ అవుతాయి.
3. **సున్నితమైన క్షీణత**: గేమ్‌లు LLM లేకుండా (ఫాల్‌బ్యాక్ ఇంజిన్), ఇంటర్నెట్ లేకుండా (క్యాష్ చేసిన ఏజెంట్ డేటా), మరియు లాగిన్ లేకుండా (ఉచిత మోడ్‌కు ప్రామాణీకరణ అవసరం లేదు) పనిచేస్తాయి.
4. **ఖర్చు-స్పృహ**: LLM కాల్‌లు చౌకైన తగిన నమూనాను ఉపయోగిస్తాయి. వ్యక్తిత్వ బరువులు API కాల్‌లు లేకుండా చాలా నిర్ణయాలను నిర్వహిస్తాయి.
