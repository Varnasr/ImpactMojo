# MCP సర్వర్ మార్గదర్శి

ImpactMojo కు ఏదైనా AI అసిస్టెంట్‌ను మొత్తం విజ్ఞాన స్థావరాన్ని ప్రోగ్రామాటిక్‌గా శోధించి ప్రశ్నించనిచ్చే ఒక **మోడల్ కాంటెక్స్ట్ ప్రోటోకాల్ (MCP) సర్వర్** ఉంది.

## MCP అంటే ఏమిటి?

[Model Context Protocol](https://modelcontextprotocol.io/) అనేది AI అసిస్టెంట్లను బాహ్య డేటా మూలాలు మరియు సాధనాలకు అనుసంధానించనిచ్చే ఒక తెరిచిన ప్రమాణం. దీన్ని AI కోసం ఒక USB పోర్ట్ లాగా భావించండి — ImpactMojo MCP సర్వర్‌ను ప్లగ్ చేయండి, మరియు మీ AI అసిస్టెంట్ మా కోర్సులు, BCTలు, Dataverse, వాతావరణ డేటా, మరియు మరిన్నింటిని శోధించగలదు.

## అందుబాటులో ఉన్న సాధనాలు (11)

| సాధనం | ఇది ఏమి చేస్తుంది |
|------|-------------|
| `search_content` | 700+ కంటెంట్ అంశాల అంతటా పూర్తి-పాఠ శోధన |
| `lookup_bct` | పూర్తి BCT పద్ధతి వివరాలను పొందండి (దక్షిణాసియా సందర్భం, కేస్ స్టడీలు) |
| `search_bcts` | 203 ప్రవర్తనా మార్పు పద్ధతులను శోధించండి/ఫిల్టర్ చేయండి |
| `list_bct_categories` | లెక్కలతో అన్ని 26 BCT వర్గాలను జాబితా చేయండి |
| `browse_dataverse` | 296 సాధనాలు, డేటాసెట్‌లు, APIలను వర్గం వారీగా బ్రౌజ్ చేయండి |
| `search_dataverse` | dataverse అంశాల అంతటా కీవర్డ్ శోధన |
| `list_challenges` | ట్రాక్/కష్టం వారీగా అభ్యాస ఛాలెంజ్‌లను జాబితా చేయండి |
| `get_challenge` | కేస్ సందర్భం మరియు రూబ్రిక్‌తో పూర్తి ఛాలెంజ్ |
| `list_courses` | 6 అభ్యాస ట్రాక్‌ల అంతటా 62 కోర్సులు |
| `get_game_info` | AI ఏజెంట్ వ్యక్తిత్వాలతో 16 ఆర్థికశాస్త్ర గేమ్‌లు |
| `query_climate_data` | Climate TRACE నుండి భారత GHG ఉద్గారాలు |

## అందుబాటులో ఉన్న వనరులు (3)

| URI | కంటెంట్ |
|-----|---------|
| `impactmojo://overview` | కంటెంట్ లెక్కలతో ప్లాట్‌ఫారమ్ సారాంశం |
| `impactmojo://catalog` | పూర్తి కంటెంట్ కేటలాగ్ (కోర్సులు, గేమ్‌లు, ఛాలెంజ్‌లు) |
| `impactmojo://tracks` | అభ్యాస ట్రాక్ వివరణలు |

## ఇన్‌స్టాల్

### ఎంపిక A: GitHub Packages నుండి

```bash
npm install @impactmojo/impactmojo-mcp-server --registry=https://npm.pkg.github.com
```

### ఎంపిక B: సోర్స్ నుండి

```bash
git clone https://github.com/ImpactMojo/ImpactMojo.git
cd ImpactMojo/mcp-server
npm install
npm run build
```

### 2. Claude Code కు అనుసంధానించండి

```bash
claude mcp add impactmojo -- node /path/to/ImpactMojo/mcp-server/dist/index.js
```

### 3. Claude Desktop కు అనుసంధానించండి

మీ `claude_desktop_config.json` కు జోడించండి:

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

కాన్ఫిగ్ ప్రదేశాలు:
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Linux**: `~/.config/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

### 4. MCP Inspector తో పరీక్షించండి

```bash
npx @modelcontextprotocol/inspector node dist/index.js
```

## ఉదాహరణ ప్రశ్నలు

ఒకసారి అనుసంధానించిన తర్వాత, మీ AI అసిస్టెంట్‌ను అడగండి:

- "Search ImpactMojo for gender equity content"
- "Look up BCT001 — what's the South Asian context?"
- "Find BCTs related to nutrition with strong evidence"
- "What tools does the Dataverse have for climate data?"
- "List all practice challenges for the MEL track"
- "Show me India's power sector emissions"

## ఆర్కిటెక్చర్

- **స్టాక్**: stdio ట్రాన్స్‌పోర్ట్‌పై TypeScript + `@modelcontextprotocol/sdk`
- **డేటా**: ప్రారంభంలో `/data/` నుండి అన్ని JSON ను లోడ్ చేస్తుంది (మెమరీలో ~750KB)
- **నెట్‌వర్క్ కాల్‌లు లేవు**: స్వచ్ఛమైన స్థానిక డేటా సర్వింగ్, డేటాబేస్ కనెక్షన్లు లేవు
- **సోర్స్**: [`/mcp-server/`](https://github.com/ImpactMojo/ImpactMojo/tree/main/mcp-server)
