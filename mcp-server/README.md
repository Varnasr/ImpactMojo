# ImpactMojo MCP Server

MCP (Model Context Protocol) server that exposes ImpactMojo's development education knowledge base to any MCP-compatible AI client.

## What's available

**11 tools:**

| Tool | Description |
|------|-------------|
| `search_content` | Full-text search across 700+ content items |
| `lookup_bct` | Get full BCT technique details (South Asian context, case studies) |
| `search_bcts` | Search/filter 203 Behavior Change Techniques |
| `list_bct_categories` | List all 26 BCT categories |
| `browse_dataverse` | Browse 296 tools, datasets, APIs, MCP servers |
| `search_dataverse` | Keyword search across dataverse items |
| `list_challenges` | List practice challenges |
| `get_challenge` | Full challenge with case context and rubric |
| `list_courses` | 68 courses across 6 learning tracks |
| `get_game_info` | 18 simulation games with AI agent personas |
| `query_climate_data` | India GHG emissions from Climate TRACE |

**3 resources:**

| URI | Content |
|-----|---------|
| `impactmojo://overview` | Platform overview with content counts |
| `impactmojo://catalog` | Full content catalog (courses, games, challenges) |
| `impactmojo://tracks` | Learning track descriptions |

## Install

**From GitHub Packages:**
```bash
npm install @varnasr/impactmojo-mcp-server --registry=https://npm.pkg.github.com
```

**From source:**
```bash
cd mcp-server
npm install
npm run build
```

## Use with Claude Code

```bash
claude mcp add impactmojo -- node /path/to/ImpactMojo/mcp-server/dist/index.js
```

Or add to `.claude/settings.json`:

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

## Use with Claude Desktop

Add to `claude_desktop_config.json`:

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

Config file locations:
- macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
- Linux: `~/.config/Claude/claude_desktop_config.json`
- Windows: `%APPDATA%\Claude\claude_desktop_config.json`

## Test with MCP Inspector

```bash
npx @modelcontextprotocol/inspector node dist/index.js
```

## Architecture

- Reads JSON data files from `../data/` at startup (~750KB total)
- All data held in memory for instant queries
- TypeScript + `@modelcontextprotocol/sdk` over stdio transport
- No external network calls, no database connections
