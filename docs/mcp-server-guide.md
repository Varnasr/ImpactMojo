# MCP Server Guide

ImpactMojo has a **Model Context Protocol (MCP) server** that lets any AI assistant search and query the entire knowledge base programmatically.

## What is MCP?

[Model Context Protocol](https://modelcontextprotocol.io/) is an open standard that lets AI assistants connect to external data sources and tools. Think of it as a USB port for AI — plug in the ImpactMojo MCP server, and your AI assistant can search our courses, BCTs, Dataverse, climate data, and more.

## Available Tools (11)

| Tool | What it does |
|------|-------------|
| `search_content` | Full-text search across 700+ content items |
| `lookup_bct` | Get full BCT technique details (South Asian context, case studies) |
| `search_bcts` | Search/filter 203 Behavior Change Techniques |
| `list_bct_categories` | List all 26 BCT categories with counts |
| `browse_dataverse` | Browse 270 tools, datasets, APIs by category |
| `search_dataverse` | Keyword search across dataverse items |
| `list_challenges` | List practice challenges by track/difficulty |
| `get_challenge` | Full challenge with case context and rubric |
| `list_courses` | 53 courses across 6 learning tracks |
| `get_game_info` | 16 economics games with AI agent personas |
| `query_climate_data` | India GHG emissions from Climate TRACE |

## Available Resources (3)

| URI | Content |
|-----|---------|
| `impactmojo://overview` | Platform summary with content counts |
| `impactmojo://catalog` | Full content catalog (courses, games, challenges) |
| `impactmojo://tracks` | Learning track descriptions |

## Install

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

Add to your `claude_desktop_config.json`:

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

Config locations:
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Linux**: `~/.config/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

### 4. Test with MCP Inspector

```bash
npx @modelcontextprotocol/inspector node dist/index.js
```

## Example Queries

Once connected, ask your AI assistant:

- "Search ImpactMojo for gender equity content"
- "Look up BCT001 — what's the South Asian context?"
- "Find BCTs related to nutrition with strong evidence"
- "What tools does the Dataverse have for climate data?"
- "List all practice challenges for the MEL track"
- "Show me India's power sector emissions"

## Architecture

- **Stack**: TypeScript + `@modelcontextprotocol/sdk` over stdio transport
- **Data**: Loads all JSON from `/data/` at startup (~750KB in memory)
- **No network calls**: Pure local data serving, no database connections
- **Source**: [`/mcp-server/`](https://github.com/ImpactMojo/ImpactMojo/tree/main/mcp-server)
