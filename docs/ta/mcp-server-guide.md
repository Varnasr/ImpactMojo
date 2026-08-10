# MCP Server வழிகாட்டி

ImpactMojo-வில் ஒரு **Model Context Protocol (MCP) server** உள்ளது, இது எந்த AI உதவியாளரும் முழு அறிவுத் தளத்தையும் நிரல்வழியில் தேடவும் வினவவும் அனுமதிக்கிறது.

## MCP என்றால் என்ன?

[Model Context Protocol](https://modelcontextprotocol.io/) என்பது AI உதவியாளர்களை வெளிப்புற தரவு மூலங்கள் மற்றும் கருவிகளுடன் இணைக்க அனுமதிக்கும் ஒரு திறந்த தரநிலையாகும். இதை AI-க்கான ஒரு USB போர்ட் போல நினைத்துப் பாருங்கள் — ImpactMojo MCP server-ஐ செருகவும், உங்கள் AI உதவியாளர் எங்கள் படிப்புகள், BCTs, Dataverse, காலநிலைத் தரவு மற்றும் பலவற்றைத் தேட முடியும்.

## கிடைக்கக்கூடிய கருவிகள் (11)

| Tool | இது என்ன செய்கிறது |
|------|-------------|
| `search_content` | 700+ உள்ளடக்க உருப்படிகள் முழுவதும் முழு-உரை தேடல் |
| `lookup_bct` | முழு BCT நுட்ப விவரங்களைப் பெறுங்கள் (தெற்காசிய சூழல், case studies) |
| `search_bcts` | 203 Behavior Change Techniques-ஐ தேடல்/வடிகட்டல் |
| `list_bct_categories` | அனைத்து 26 BCT வகைகளையும் எண்ணிக்கைகளுடன் பட்டியலிடுங்கள் |
| `browse_dataverse` | வகையின் அடிப்படையில் 270 கருவிகள், தரவுத்தொகுப்புகள், APIs-ஐ உலாவுங்கள் |
| `search_dataverse` | dataverse உருப்படிகள் முழுவதும் முக்கிய சொல் தேடல் |
| `list_challenges` | track/சிரம அளவின் அடிப்படையில் பயிற்சி சவால்களைப் பட்டியலிடுங்கள் |
| `get_challenge` | case சூழல் மற்றும் மதிப்பீட்டுத் திட்டத்துடன் முழு சவால் |
| `list_courses` | 6 learning tracks முழுவதும் 70 படிப்புகள் |
| `get_game_info` | AI agent personas கொண்ட 16 பொருளாதார games |
| `query_climate_data` | Climate TRACE-இலிருந்து India GHG உமிழ்வுகள் |

## கிடைக்கக்கூடிய வளங்கள் (3)

| URI | உள்ளடக்கம் |
|-----|---------|
| `impactmojo://overview` | உள்ளடக்க எண்ணிக்கைகளுடன் தளச் சுருக்கம் |
| `impactmojo://catalog` | முழு உள்ளடக்க பட்டியல் (courses, games, challenges) |
| `impactmojo://tracks` | Learning track விளக்கங்கள் |

## நிறுவல்

### Option A: From GitHub Packages

```bash
npm install @impactmojo/impactmojo-mcp-server --registry=https://npm.pkg.github.com
```

### Option B: From source

```bash
git clone https://github.com/ImpactMojo/ImpactMojo.git
cd ImpactMojo/mcp-server
npm install
npm run build
```

### 2. Connect to Claude Code

```bash
claude mcp add impactmojo -- node /path/to/ImpactMojo/mcp-server/dist/index.js
```

### 3. Connect to Claude Desktop

உங்கள் `claude_desktop_config.json`-இல் சேர்க்கவும்:

```json
{
  "mcpServers": {
    "impactmojo": {
      "command": "node",
      "args": ["/absolute/path/to/ImpactMojo/mcp-server/dist/index.js"]
    }
  }
}
```

Config இடங்கள்:
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Linux**: `~/.config/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

### 4. Test with MCP Inspector

```bash
npx @modelcontextprotocol/inspector node dist/index.js
```

## எடுத்துக்காட்டு வினவல்கள்

இணைக்கப்பட்டவுடன், உங்கள் AI உதவியாளரிடம் கேளுங்கள்:

- "Search ImpactMojo for gender equity content"
- "Look up BCT001 — what's the South Asian context?"
- "Find BCTs related to nutrition with strong evidence"
- "What tools does the Dataverse have for climate data?"
- "List all practice challenges for the MEL track"
- "Show me India's power sector emissions"

## கட்டமைப்பு

- **Stack**: stdio transport மீது TypeScript + `@modelcontextprotocol/sdk`
- **Data**: தொடக்கத்தில் `/data/`-இலிருந்து அனைத்து JSON-ஐயும் ஏற்றுகிறது (~750KB நினைவகத்தில்)
- **No network calls**: தூய்மையான உள்ளூர் தரவு வழங்கல், எந்த தரவுத்தள இணைப்புகளும் இல்லை
- **Source**: [`/mcp-server/`](https://github.com/ImpactMojo/ImpactMojo/tree/main/mcp-server)
