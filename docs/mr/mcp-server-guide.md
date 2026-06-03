# MCP Server मार्गदर्शक

ImpactMojo कडे एक **Model Context Protocol (MCP) server** आहे जो कोणत्याही AI असिस्टंटला संपूर्ण ज्ञानभांडार प्रोग्रामॅटिक पद्धतीने शोधण्याची आणि क्वेरी करण्याची सुविधा देतो.

## MCP म्हणजे काय?

[Model Context Protocol](https://modelcontextprotocol.io/) हे एक खुले मानक आहे जे AI असिस्टंटना बाह्य डेटा स्रोत आणि टूल्सशी जोडण्याची परवानगी देते. याला AI साठीचा USB पोर्ट समजा — ImpactMojo MCP server प्लग इन करा, आणि तुमचा AI असिस्टंट आमचे courses, BCTs, Dataverse, हवामान डेटा आणि बरेच काही शोधू शकतो.

## उपलब्ध Tools (11)

| Tool | हे काय करते |
|------|-------------|
| `search_content` | 700+ कंटेंट आयटम्समध्ये फुल-टेक्स्ट शोध |
| `lookup_bct` | संपूर्ण BCT तंत्राचा तपशील मिळवा (दक्षिण आशियाई संदर्भ, केस स्टडीज) |
| `search_bcts` | 203 Behavior Change Techniques शोधा/फिल्टर करा |
| `list_bct_categories` | सर्व 26 BCT श्रेणी मोजणीसह सूचीबद्ध करा |
| `browse_dataverse` | श्रेणीनुसार 270 टूल्स, डेटासेट, APIs ब्राउझ करा |
| `search_dataverse` | dataverse आयटम्समध्ये कीवर्ड शोध |
| `list_challenges` | track/कठीणतेनुसार practice challenges सूचीबद्ध करा |
| `get_challenge` | केस संदर्भ आणि रुब्रिकसह संपूर्ण challenge |
| `list_courses` | 6 learning tracks मध्ये 53 courses |
| `get_game_info` | AI एजंट पर्सोनासह 16 economics games |
| `query_climate_data` | Climate TRACE मधून भारताचे GHG उत्सर्जन |

## उपलब्ध Resources (3)

| URI | कंटेंट |
|-----|---------|
| `impactmojo://overview` | कंटेंट मोजणीसह प्लॅटफॉर्म सारांश |
| `impactmojo://catalog` | संपूर्ण कंटेंट कॅटलॉग (courses, games, challenges) |
| `impactmojo://tracks` | Learning track वर्णने |

## इन्स्टॉल करा

### पर्याय A: GitHub Packages वरून

```bash
npm install @impactmojo/impactmojo-mcp-server --registry=https://npm.pkg.github.com
```

### पर्याय B: सोर्सवरून

```bash
git clone https://github.com/ImpactMojo/ImpactMojo.git
cd ImpactMojo/mcp-server
npm install
npm run build
```

### 2. Claude Code शी जोडा

```bash
claude mcp add impactmojo -- node /path/to/ImpactMojo/mcp-server/dist/index.js
```

### 3. Claude Desktop शी जोडा

तुमच्या `claude_desktop_config.json` मध्ये जोडा:

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

Config स्थाने:
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Linux**: `~/.config/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

### 4. MCP Inspector ने चाचणी करा

```bash
npx @modelcontextprotocol/inspector node dist/index.js
```

## उदाहरण क्वेरीज

जोडल्यानंतर, तुमच्या AI असिस्टंटला विचारा:

- "Search ImpactMojo for gender equity content"
- "Look up BCT001 — what's the South Asian context?"
- "Find BCTs related to nutrition with strong evidence"
- "What tools does the Dataverse have for climate data?"
- "List all practice challenges for the MEL track"
- "Show me India's power sector emissions"

## आर्किटेक्चर

- **Stack**: stdio transport वर TypeScript + `@modelcontextprotocol/sdk`
- **Data**: स्टार्टअपवर `/data/` मधून सर्व JSON लोड करते (~750KB मेमरीमध्ये)
- **कोणतेही नेटवर्क कॉल नाहीत**: शुद्ध स्थानिक डेटा सर्व्हिंग, कोणतेही डेटाबेस कनेक्शन नाही
- **Source**: [`/mcp-server/`](https://github.com/ImpactMojo/ImpactMojo/tree/main/mcp-server)
