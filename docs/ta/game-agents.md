# AI விளையாட்டு ஏஜெண்டுகள் — MiroFish-உந்துதல் பெற்ற எதிராளிகள்

## கண்ணோட்டம்

ImpactMojo-வின் விளையாட்டுகளில் **AI-இயக்கப்படும் எதிராளிகள்** இடம்பெறுகின்றன, இவை [MiroFish](https://github.com/666ghj/MiroFish) என்ற திறந்த மூல திரள் நுண்ணறிவு இயந்திரத்தால் உந்துதல் பெற்றவை. எளிய விதி-அடிப்படையிலான பலன் கணக்கீடுகளுக்குப் பதிலாக, விளையாட்டுகளில் தனித்துவமான ஆளுமைகள், நினைவகங்கள் மற்றும் தகவமைப்பு உத்திகள் கொண்ட AI ஏஜெண்டுகள் இடம்பெறுகின்றன — இவை அனைத்தும் தெற்காசிய வளர்ச்சிச் சூழல்களில் வேரூன்றியவை.

ஒவ்வொரு விளையாட்டும் ஆறு பாரம்பரிய பாணிகளில் (வார்லி, மதுபனி, கோண்ட், கலம்காரி, பிச்வாய், பட்டச்சித்ரா) **இந்திய நாட்டுப்புற கலை கதை விளக்கப்படங்களால்** வளப்படுத்தப்பட்டுள்ளது, இவை கதை சூழலை வழங்குகின்றன மற்றும் வீரர் தேர்வுகளுக்கு ஏற்ப மாறுகின்றன. கலை பாணிகள் குறித்த விவரங்களுக்கு [Games Guide](games-guide.md) பார்க்கவும்.

## கட்டமைப்பு

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

### இரண்டு முறைகள்

1. **LLM Mode** (Professional/Organization அடுக்கு): ஒவ்வொரு ஏஜெண்ட் முடிவும் ஒரு LLM அழைப்பால் இயக்கப்படுகிறது. ஏஜெண்ட் தன் கதாபாத்திரத்தில் நிலைத்திருந்து, விளையாட்டு வரலாற்றை நினைவில் கொண்டு, இயற்கையான மொழியில் காரணங்களை உருவாக்குகிறது. செலவு: ஒரு விளையாட்டு அமர்வுக்கு ~$0.015.

2. **Fallback Mode** (Free/Practitioner அடுக்கு அல்லது இணைப்பில்லாமல்): ஒரு இலகுரக இயந்திரம் ஆளுமை எடைகளை (cooperation_bias, risk_tolerance, memory_weight) பயன்படுத்தி உலாவியிலேயே உள்ளூரில் முடிவுகளை உருவாக்குகிறது. எந்த API அழைப்புகளும் தேவையில்லை.

## கோப்புகள்

| கோப்பு | நோக்கம் |
|------|---------|
| `data/game-agents.json` | ஏஜெண்ட் ஆளுமைகள் — பெயர்கள், பின்னணிக் கதைகள், ஆளுமை எடைகள், உத்தி குறிப்புகள் |
| `supabase/functions/game-agent/index.ts` | Edge Function — prompt உருவாக்கி, LLM அழைப்பி, fallback இயந்திரம் |
| `js/game-agents.js` | வாங்கி நூலகம் — ஏஜெண்ட் முடிவுகளைப் பெற விளையாட்டுகள் இதைச் சேர்க்கின்றன |
| `js/state-manager.js` | நிலை — AI விளையாட்டு அமர்வுகளைக் கண்காணிக்க `gameSession` மற்றும் `gameHistory` |
| `catalog_data.json` | மெட்டாடேட்டா — ஒவ்வொரு விளையாட்டு உள்ளீட்டிலும் `ai_agents` புலம் |

## ஏஜெண்ட் ஆளுமைகள்

ஒவ்வொரு விளையாட்டிலும் தனித்துவமான வகைமாதிரிகள் கொண்ட 2–4 ஏஜெண்டுகள் உள்ளன:

### Public Good Game
| ஏஜெண்ட் | வகைமாதிரி | ஒத்துழைப்பு | விளக்கம் |
|-------|-----------|-------------|-------------|
| Meera | நிபந்தனை ஒத்துழைப்பாளர் | 0.8 | NGO மேலாளர், குழு நடத்தையைப் பிரதிபலிக்கிறார் |
| Arjun | உத்தி சார்ந்த இலவச சவாரியாளர் | 0.25 | ஆலோசகர், பங்களிப்பைக் குறைக்கிறார் |
| Fatima | பரஸ்பரக்காரர் | 0.6 | சுகாதாரப் பணியாளர், குழு சராசரியுடன் பொருந்துகிறார் |
| Ravi | நிபந்தனையற்ற ஒத்துழைப்பாளர் | 0.95 | விரிவுரையாளர், எதுவாக இருந்தாலும் பங்களிக்கிறார் |

### Prisoners' Dilemma
| ஏஜெண்ட் | வகைமாதிரி | உத்தி |
|-------|-----------|----------|
| Sunita | Tit-for-tat | முதலில் ஒத்துழைக்கிறார், எதிராளியைப் பிரதிபலிக்கிறார் |
| Vikram | Grudger | காட்டிக்கொடுக்கப்படும் வரை ஒத்துழைக்கிறார், பிறகு என்றென்றும் விலகுகிறார் |
| Lakshmi | Pavlov | வென்றால்-நில், தோற்றால்-மாறு |
| Deepak | கணிக்க முடியாதவர் | சீரற்ற கலவை, சுரண்ட கடினம் |

### Commons Crisis
| ஏஜெண்ட் | வகைமாதிரி | பிரித்தெடுக்கும் போக்கு |
|-------|-----------|-------------------|
| Priya | நிலைத்தன்மை-முதல் | குறைந்த பிரித்தெடுப்பு, வரம்புகளை ஆதரிக்கிறார் |
| Raj | குறுகிய கால உகந்தமயமாக்கி | அதிக பிரித்தெடுப்பு, தடைகளுக்கு மட்டுமே பதிலளிக்கிறார் |
| Ananya | நிறுவன கட்டமைப்பாளர் | மிதமான, ஆளுகைக்காக வலியுறுத்துகிறார் |
| Karthik | நெறி-பின்பற்றுபவர் | குழு சராசரியுடன் பொருந்துகிறார் |

(அனைத்து 10 AI-இயக்கப்பட்ட விளையாட்டுகளிலும் முழுமையான ஆளுமை வரையறைகளுக்கு `data/game-agents.json` பார்க்கவும்.)

## ஒருங்கிணைப்பு வழிகாட்டி (Game Frontends-க்காக)

### 1. வாங்கி நூலகத்தைச் சேர்க்கவும்

```html
<script src="https://www.impactmojo.in/js/game-agents.js"></script>
```

### 2. உங்கள் விளையாட்டுக்கு துவக்கவும்

```javascript
var agents = new IMGameAgents('public-good-game');
```

### 3. ஏஜெண்ட் பட்டியலைப் பெறவும் (UI-க்காக)

```javascript
agents.getRoster().then(function(roster) {
  roster.forEach(function(agent) {
    // Display agent name, role, location, personality in game UI
    addAgentCard(agent.name, agent.role, agent.location, agent.personality.archetype);
  });
});
```

### 4. ஒவ்வொரு சுற்றிலும் முடிவுகளைக் கோரவும்

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

### 5. அமர்வு நிலையைக் கண்காணிக்கவும்

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

## வரிசைப்படுத்தல்

### சூழல் மாறிகள்

இவற்றை `supabase secrets set` வழியாக அமைக்கவும்:

```bash
supabase secrets set LLM_API_KEY=sk-...
supabase secrets set LLM_BASE_URL=https://api.openai.com/v1
supabase secrets set LLM_MODEL=gpt-4o-mini
```

Anthropic Claude-க்கு (இணக்கமான முனைப்புள்ளி வழியாக):
```bash
supabase secrets set LLM_API_KEY=sk-ant-...
supabase secrets set LLM_BASE_URL=https://api.anthropic.com/v1
supabase secrets set LLM_MODEL=claude-haiku-4-5-20251001
```

### Edge Function-ஐ வரிசைப்படுத்தவும்

```bash
supabase functions deploy game-agent
```

### செலவு மேலாண்மை

- Free மற்றும் Practitioner அடுக்குகள் **fallback இயந்திரத்தை** பயன்படுத்துகின்றன (பூஜ்ஜிய LLM செலவு)
- Professional அடுக்கு LLM-இயக்கப்பட்ட ஏஜெண்டுகளைப் பெறுகிறது (GPT-4o-mini உடன் ~$0.015/அமர்வு)
- ஒரு பயனருக்கு நிமிடத்திற்கு 30 கோரிக்கைகள் என வீத வரம்பு உள்ளது
- மாதத்திற்கு 1,000 அமர்வுகளில்: மொத்த LLM செலவு ~$10–15/மாதம்

## விரிவாக்கம்

### புதிய ஏஜெண்டைச் சேர்த்தல்

பொருத்தமான விளையாட்டின் கீழ் `data/game-agents.json`-ல் ஒரு உள்ளீட்டைச் சேர்க்கவும்:

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

### புதிய விளையாட்டைச் சேர்த்தல்

1. `data/game-agents.json`-ல் `games` கீழ் ஒரு புதிய விளையாட்டு விசையைச் சேர்க்கவும்
2. தொடர்புடைய வகைமாதிரிகள் கொண்ட 2–4 ஏஜெண்டுகளை வரையறுக்கவும்
3. fallback இயந்திரத்தில் (Edge Function மற்றும் வாங்கி நூலகம் இரண்டிலும்) செயல் கையாளுதலைச் சேர்க்கவும்
4. `catalog_data.json`-ஐ `ai_agents` புலத்துடன் புதுப்பிக்கவும்

## வடிவமைப்புக் கொள்கைகள்

1. **தெற்காசிய சூழல்**: ஒவ்வொரு ஏஜெண்டும் இப்பகுதியைச் சேர்ந்த நிஜமான வளர்ச்சிப் பயிற்சியாளர், அதிகாரி, தொழில்முனைவோர் அல்லது சமூக உறுப்பினராக இருக்கிறார்.
2. **கற்பித்தல் ரீதியாக அர்த்தமுள்ளது**: ஏஜெண்ட் வகைமாதிரிகள், மாணவர்கள் விவாதத்தில் கற்கும் நிஜமான பொருளாதார நடத்தை வகைகளுடன் (tit-for-tat, free-rider, conditional cooperator) பொருந்துகின்றன.
3. **அழகான சீரழிவு**: விளையாட்டுகள் LLM இல்லாமல் (fallback இயந்திரம்), இணையம் இல்லாமல் (தற்காலிக சேமிப்பு ஏஜெண்ட் தரவு), மற்றும் உள்நுழைவு இல்லாமல் (இலவச முறைக்கு அங்கீகாரம் தேவையில்லை) வேலை செய்கின்றன.
4. **செலவு-உணர்வுள்ளது**: LLM அழைப்புகள் மலிவான போதிய மாதிரியைப் பயன்படுத்துகின்றன. பெரும்பாலான முடிவுகளை API அழைப்புகள் இல்லாமல் ஆளுமை எடைகள் கையாளுகின்றன.
