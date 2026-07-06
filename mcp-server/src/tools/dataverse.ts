import { z } from "zod";
import type { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import type { LoadedData } from "../data-loader.js";

export function registerDataverseTools(server: McpServer, data: LoadedData) {
  server.tool(
    "browse_dataverse",
    "Browse ImpactMojo's Dataverse catalog of 296 tools, datasets, APIs, and MCP servers for development research. Filter by category, type, or free-only.",
    {
      category: z.string().optional().describe("Category ID, e.g. 'india-gov-data', 'health-epi'. Omit to list all categories."),
      type: z.string().optional().describe("Filter by type: api, dataset, mcp-server, tool, platform, visualization"),
      freeOnly: z.boolean().optional().default(false).describe("Only show free resources"),
      limit: z.number().optional().default(20).describe("Max items (default 20)"),
    },
    async ({ category, type, freeOnly, limit }) => {
      const cap = Math.min(limit ?? 20, 50);

      // If no category specified, list all categories
      if (!category) {
        const cats = data.dataverseCategories.map((c) => ({
          id: c.id,
          name: c.name,
          items: c.itemCount,
        }));
        return {
          content: [{
            type: "text" as const,
            text: `Dataverse: ${data.dataverseItems.length} items across ${cats.length} categories.\n\nCall with a category ID to browse items:\n\n${JSON.stringify(cats, null, 2)}`,
          }],
        };
      }

      let items = data.dataverseItems.filter((i) => i.categoryId === category);
      if (type) items = items.filter((i) => i.type === type);
      if (freeOnly) items = items.filter((i) => i.free);
      items = items.slice(0, cap);

      if (items.length === 0) {
        return { content: [{ type: "text" as const, text: `No items found for category "${category}".` }] };
      }

      const output = items.map((i) => ({
        id: i.id,
        name: i.name,
        type: i.type,
        status: i.status,
        url: i.url,
        free: i.free,
        description: i.description.slice(0, 150),
      }));

      const catName = data.dataverseCategories.find((c) => c.id === category)?.name ?? category;
      return {
        content: [{
          type: "text" as const,
          text: `${catName}: ${items.length} item(s)\n\n${JSON.stringify(output, null, 2)}`,
        }],
      };
    }
  );

  server.tool(
    "search_dataverse",
    "Keyword search across 296 dataverse items — tools, datasets, APIs, and MCP servers for development research.",
    {
      query: z.string().describe("Search term (e.g. 'climate', 'health survey', 'india statistics')"),
      limit: z.number().optional().default(10).describe("Max results (default 10)"),
    },
    async ({ query, limit }) => {
      const tokens = query.toLowerCase().split(/\s+/).filter(Boolean);
      const cap = Math.min(limit ?? 10, 50);

      let results = data.dataverseItems.filter((item) => {
        const haystack = `${item.name} ${item.description} ${item.source ?? ""} ${item.tags.join(" ")}`.toLowerCase();
        return tokens.every((t) => haystack.includes(t));
      });

      results = results.slice(0, cap);

      if (results.length === 0) {
        return { content: [{ type: "text" as const, text: `No dataverse items found for "${query}".` }] };
      }

      const output = results.map((i) => ({
        id: i.id,
        name: i.name,
        type: i.type,
        category: i.categoryName,
        url: i.url,
        free: i.free,
        description: i.description.slice(0, 150),
      }));

      return {
        content: [{
          type: "text" as const,
          text: `Found ${results.length} dataverse item(s) for "${query}":\n\n${JSON.stringify(output, null, 2)}`,
        }],
      };
    }
  );
}
