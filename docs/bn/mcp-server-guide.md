# MCP Server নির্দেশিকা

ImpactMojo-র একটি **Model Context Protocol (MCP) server** আছে যা যেকোনো AI সহকারীকে সম্পূর্ণ জ্ঞানভাণ্ডার প্রোগ্রাম্যাটিকভাবে অনুসন্ধান ও কোয়েরি করতে দেয়।

## MCP কী?

[Model Context Protocol](https://modelcontextprotocol.io/) হল একটি ওপেন স্ট্যান্ডার্ড যা AI সহকারীদের বাহ্যিক ডেটা উৎস ও টুলের সাথে সংযোগ করতে দেয়। একে AI-এর জন্য একটি USB পোর্ট হিসেবে ভাবুন — ImpactMojo MCP server প্লাগ ইন করুন, এবং আপনার AI সহকারী আমাদের কোর্স, BCTs, Dataverse, জলবায়ু ডেটা এবং আরও অনেক কিছু অনুসন্ধান করতে পারবে।

## উপলব্ধ টুল (11)

| Tool | এটি যা করে |
|------|-------------|
| `search_content` | 700+ কন্টেন্ট আইটেম জুড়ে ফুল-টেক্সট অনুসন্ধান |
| `lookup_bct` | সম্পূর্ণ BCT কৌশল বিবরণ পান (দক্ষিণ এশীয় প্রেক্ষাপট, case studies) |
| `search_bcts` | 203টি Behavior Change Techniques অনুসন্ধান/ফিল্টার করুন |
| `list_bct_categories` | সংখ্যাসহ সব 26টি BCT বিভাগ তালিকাভুক্ত করুন |
| `browse_dataverse` | বিভাগ অনুসারে 270টি টুল, ডেটাসেট, APIs ব্রাউজ করুন |
| `search_dataverse` | dataverse আইটেম জুড়ে কীওয়ার্ড অনুসন্ধান |
| `list_challenges` | track/কঠিনতা অনুসারে অনুশীলন চ্যালেঞ্জ তালিকাভুক্ত করুন |
| `get_challenge` | case প্রেক্ষাপট ও রুব্রিক সহ সম্পূর্ণ চ্যালেঞ্জ |
| `list_courses` | 6টি learning track জুড়ে 53টি কোর্স |
| `get_game_info` | AI agent persona সহ 16টি অর্থনীতি games |
| `query_climate_data` | Climate TRACE থেকে India GHG নির্গমন |

## উপলব্ধ রিসোর্স (3)

| URI | কন্টেন্ট |
|-----|---------|
| `impactmojo://overview` | কন্টেন্ট সংখ্যাসহ প্ল্যাটফর্ম সারসংক্ষেপ |
| `impactmojo://catalog` | সম্পূর্ণ কন্টেন্ট ক্যাটালগ (courses, games, challenges) |
| `impactmojo://tracks` | Learning track বিবরণ |

## ইনস্টল

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

আপনার `claude_desktop_config.json`-এ যোগ করুন:

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

Config অবস্থান:
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Linux**: `~/.config/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

### 4. Test with MCP Inspector

```bash
npx @modelcontextprotocol/inspector node dist/index.js
```

## উদাহরণ কোয়েরি

সংযুক্ত হলে, আপনার AI সহকারীকে জিজ্ঞাসা করুন:

- "Search ImpactMojo for gender equity content"
- "Look up BCT001 — what's the South Asian context?"
- "Find BCTs related to nutrition with strong evidence"
- "What tools does the Dataverse have for climate data?"
- "List all practice challenges for the MEL track"
- "Show me India's power sector emissions"

## আর্কিটেকচার

- **Stack**: stdio transport-এর উপর TypeScript + `@modelcontextprotocol/sdk`
- **Data**: শুরুতে `/data/` থেকে সমস্ত JSON লোড করে (~750KB মেমরিতে)
- **No network calls**: বিশুদ্ধ লোকাল ডেটা পরিবেশন, কোনো ডেটাবেস সংযোগ নেই
- **Source**: [`/mcp-server/`](https://github.com/ImpactMojo/ImpactMojo/tree/main/mcp-server)
