# MCP Server गाइड

ImpactMojo में एक **Model Context Protocol (MCP) server** है जो किसी भी AI असिस्टेंट को पूरे ज्ञान-भंडार को प्रोग्रामेटिक रूप से खोजने और क्वेरी करने देता है।

## MCP क्या है?

[Model Context Protocol](https://modelcontextprotocol.io/) एक खुला मानक है जो AI असिस्टेंट को बाहरी डेटा स्रोतों और टूल्स से जोड़ने देता है। इसे AI के लिए USB पोर्ट की तरह समझें — ImpactMojo MCP server को प्लग इन करें, और आपका AI असिस्टेंट हमारे courses, BCTs, Dataverse, जलवायु डेटा और बहुत कुछ खोज सकता है।

## उपलब्ध Tools (11)

| Tool | यह क्या करता है |
|------|-------------|
| `search_content` | 700+ कंटेंट आइटम्स में फुल-टेक्स्ट खोज |
| `lookup_bct` | पूरी BCT तकनीक का विवरण प्राप्त करें (दक्षिण एशियाई संदर्भ, केस स्टडीज़) |
| `search_bcts` | 203 Behavior Change Techniques खोजें/फ़िल्टर करें |
| `list_bct_categories` | सभी 26 BCT श्रेणियाँ गिनती सहित सूचीबद्ध करें |
| `browse_dataverse` | श्रेणी के अनुसार 270 टूल्स, डेटासेट, APIs ब्राउज़ करें |
| `search_dataverse` | dataverse आइटम्स में कीवर्ड खोज |
| `list_challenges` | track/कठिनाई के अनुसार practice challenges सूचीबद्ध करें |
| `get_challenge` | केस संदर्भ और रूब्रिक सहित पूरा challenge |
| `list_courses` | 6 learning tracks में 64 courses |
| `get_game_info` | AI एजेंट पर्सोना सहित 16 economics games |
| `query_climate_data` | Climate TRACE से भारत के GHG उत्सर्जन |

## उपलब्ध Resources (3)

| URI | कंटेंट |
|-----|---------|
| `impactmojo://overview` | कंटेंट गिनती सहित प्लेटफ़ॉर्म सारांश |
| `impactmojo://catalog` | पूरा कंटेंट कैटलॉग (courses, games, challenges) |
| `impactmojo://tracks` | Learning track विवरण |

## इंस्टॉल करें

### विकल्प A: GitHub Packages से

```bash
npm install @impactmojo/impactmojo-mcp-server --registry=https://npm.pkg.github.com
```

### विकल्प B: सोर्स से

```bash
git clone https://github.com/ImpactMojo/ImpactMojo.git
cd ImpactMojo/mcp-server
npm install
npm run build
```

### 2. Claude Code से कनेक्ट करें

```bash
claude mcp add impactmojo -- node /path/to/ImpactMojo/mcp-server/dist/index.js
```

### 3. Claude Desktop से कनेक्ट करें

अपने `claude_desktop_config.json` में जोड़ें:

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

Config स्थान:
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Linux**: `~/.config/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

### 4. MCP Inspector से परीक्षण करें

```bash
npx @modelcontextprotocol/inspector node dist/index.js
```

## उदाहरण क्वेरीज़

कनेक्ट होने के बाद, अपने AI असिस्टेंट से पूछें:

- "Search ImpactMojo for gender equity content"
- "Look up BCT001 — what's the South Asian context?"
- "Find BCTs related to nutrition with strong evidence"
- "What tools does the Dataverse have for climate data?"
- "List all practice challenges for the MEL track"
- "Show me India's power sector emissions"

## आर्किटेक्चर

- **Stack**: stdio transport पर TypeScript + `@modelcontextprotocol/sdk`
- **Data**: स्टार्टअप पर `/data/` से सभी JSON लोड करता है (~750KB मेमोरी में)
- **कोई नेटवर्क कॉल नहीं**: शुद्ध स्थानीय डेटा सर्विंग, कोई डेटाबेस कनेक्शन नहीं
- **Source**: [`/mcp-server/`](https://github.com/ImpactMojo/ImpactMojo/tree/main/mcp-server)
