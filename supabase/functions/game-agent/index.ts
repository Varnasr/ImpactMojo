// supabase/functions/game-agent/index.ts
// MiroFish-inspired AI Agent Engine for ImpactMojo Games.
//
// Accepts game state + agent ID, returns the agent's next decision via LLM.
// Supports multiple LLM providers with automatic fallback.
//
// Env secrets (set via `supabase secrets set`):
//   LLM_PROVIDER       — Provider priority list, comma-separated
//                         (default: "deepseek,groq,gemini,together,openai")
//   LLM_API_KEY        — Default API key (legacy, used if provider-specific key missing)
//   LLM_BASE_URL       — Default base URL (legacy fallback)
//   LLM_MODEL          — Default model (legacy fallback)
//
//   Provider-specific keys (set only those you want to use):
//   DEEPSEEK_API_KEY   — DeepSeek API key  (cheapest quality option)
//   GROQ_API_KEY       — Groq API key      (free tier, rate-limited, fast)
//   GEMINI_API_KEY     — Google Gemini key  (free tier available)
//   TOGETHER_API_KEY   — Together AI key    (cheap, reliable)
//   OPENAI_API_KEY     — OpenAI API key     (premium fallback)
//   ANTHROPIC_API_KEY  — Anthropic API key  (premium)
//
//   SUPABASE_URL       — auto-provided
//   SUPABASE_ANON_KEY  — auto-provided

import { serve } from "https://deno.land/std@0.177.0/http/server.ts";
import { createClient } from "https://esm.sh/@supabase/supabase-js@2.112.3";

// ── Types ────────────────────────────────────────────────────────────

interface AgentPersona {
  id: string;
  name: string;
  role: string;
  location: string;
  personality: {
    archetype: string;
    cooperation_bias: number;
    risk_tolerance: number;
    memory_weight: number;
    description: string;
  };
  backstory: string;
  strategy_hint: string;
}

interface RoundEvent {
  round: number;
  player_action: string;
  player_amount?: number;
  agent_actions: Record<string, { action: string; amount?: number }>;
  outcome?: string;
}

interface GameAgentRequest {
  game_id: string;
  agent_id: string;
  round: number;
  total_rounds: number;
  history: RoundEvent[];
  available_actions: string[];
  context?: Record<string, unknown>;
}

interface AgentDecision {
  action: string;
  amount: number | null;
  reasoning: string;
  agent_id: string;
  agent_name: string;
  personality: string;
}

// ── CORS ─────────────────────────────────────────────────────────────

const ALLOWED_ORIGINS = [
  "https://www.impactmojo.in",
  "https://impactmojo.in",
  "https://101.impactmojo.in",
];

function corsHeaders(req: Request): Record<string, string> {
  const origin = req.headers.get("Origin") || "";
  const allowed = ALLOWED_ORIGINS.includes(origin) ? origin : ALLOWED_ORIGINS[0];
  return {
    "Access-Control-Allow-Origin": allowed,
    "Access-Control-Allow-Headers":
      "authorization, x-client-info, apikey, content-type",
    "Access-Control-Allow-Methods": "POST, OPTIONS",
    Vary: "Origin",
  };
}

// ── Rate limiter (per-user, per edge instance) ───────────────────────
// 30 requests per minute (generous enough for a 10-round game with 4 agents)
const RATE_WINDOW_MS = 60_000;
const RATE_MAX = 30;
const rateMap = new Map<string, { count: number; resetAt: number }>();

function isRateLimited(key: string): boolean {
  const now = Date.now();
  const entry = rateMap.get(key);
  if (!entry || now > entry.resetAt) {
    rateMap.set(key, { count: 1, resetAt: now + RATE_WINDOW_MS });
    return false;
  }
  entry.count++;
  return entry.count > RATE_MAX;
}

// ── Agent persona loader ─────────────────────────────────────────────

let agentData: Record<string, Record<string, AgentPersona>> | null = null;

async function loadAgents(): Promise<
  Record<string, Record<string, AgentPersona>>
> {
  if (agentData) return agentData;

  // Load from bundled data (deployed alongside the function)
  const resp = await fetch(
    new URL("../../data/game-agents.json", import.meta.url)
  ).catch(() => null);

  if (resp && resp.ok) {
    const raw = await resp.json();
    agentData = {};
    for (const [gameId, gameConfig] of Object.entries(
      raw.games as Record<string, { agents: AgentPersona[] }>
    )) {
      agentData[gameId] = {};
      for (const agent of gameConfig.agents) {
        agentData[gameId][agent.id] = agent;
      }
    }
    return agentData;
  }

  // Fallback: return empty (will 404 on agent lookup)
  agentData = {};
  return agentData;
}

// ── Prompt builder ───────────────────────────────────────────────────

function buildPrompt(
  agent: AgentPersona,
  req: GameAgentRequest
): string {
  const historyText =
    req.history.length === 0
      ? "No rounds played yet. This is the first round."
      : req.history
          .map((r) => {
            const agentMoves = Object.entries(r.agent_actions)
              .map(([id, a]) => `  ${id}: ${a.action}${a.amount != null ? ` (${a.amount})` : ""}`)
              .join("\n");
            return `Round ${r.round}:\n  Player: ${r.player_action}${r.player_amount != null ? ` (${r.player_amount})` : ""}\n${agentMoves}${r.outcome ? `\n  Outcome: ${r.outcome}` : ""}`;
          })
          .join("\n\n");

  const actionsStr = req.available_actions.join(", ");

  return `You are ${agent.name}, a ${agent.role} based in ${agent.location}.

${agent.backstory}

You are playing the "${req.game_id.replace(/-/g, " ")}", an economics simulation.

Your personality: ${agent.personality.description}
Your archetype: ${agent.personality.archetype}
Cooperation tendency: ${agent.personality.cooperation_bias}/1.0
Risk tolerance: ${agent.personality.risk_tolerance}/1.0

This is round ${req.round} of ${req.total_rounds}.

Game history so far:
${historyText}

Available actions: ${actionsStr}

Based on your personality and the game history, decide your action for this round.

Strategic guidance: ${agent.strategy_hint}

${req.context ? `Additional context: ${JSON.stringify(req.context)}` : ""}

Respond ONLY with a JSON object (no markdown, no explanation outside JSON):
{
  "action": "<one of: ${actionsStr}>",
  "amount": <numeric value if applicable, or null>,
  "reasoning": "<1-2 sentence explanation in character as ${agent.name}>"
}`;
}

// ── LLM Provider Registry ────────────────────────────────────────────
// Each provider defines how to call its API. All use OpenAI-compatible
// chat/completions format except Gemini which needs translation.

interface LLMProvider {
  name: string;
  envKey: string;         // env var name for the API key
  baseUrl: string;        // API base URL
  defaultModel: string;   // default model ID
  format: "openai" | "gemini";  // API format
}

const PROVIDERS: Record<string, LLMProvider> = {
  deepseek: {
    name: "DeepSeek",
    envKey: "DEEPSEEK_API_KEY",
    baseUrl: "https://api.deepseek.com/v1",
    defaultModel: "deepseek-chat",
    format: "openai",
  },
  groq: {
    name: "Groq",
    envKey: "GROQ_API_KEY",
    baseUrl: "https://api.groq.com/openai/v1",
    defaultModel: "llama-3.1-70b-versatile",
    format: "openai",
  },
  gemini: {
    name: "Google Gemini",
    envKey: "GEMINI_API_KEY",
    baseUrl: "https://generativelanguage.googleapis.com/v1beta",
    defaultModel: "gemini-2.0-flash",
    format: "gemini",
  },
  together: {
    name: "Together AI",
    envKey: "TOGETHER_API_KEY",
    baseUrl: "https://api.together.xyz/v1",
    defaultModel: "meta-llama/Llama-3.1-70B-Instruct-Turbo",
    format: "openai",
  },
  openai: {
    name: "OpenAI",
    envKey: "OPENAI_API_KEY",
    baseUrl: "https://api.openai.com/v1",
    defaultModel: "gpt-4o-mini",
    format: "openai",
  },
  anthropic: {
    name: "Anthropic",
    envKey: "ANTHROPIC_API_KEY",
    baseUrl: "https://api.anthropic.com/v1",
    defaultModel: "claude-haiku-4-5-20251001",
    format: "openai", // Uses Messages API but we adapt below
  },
};

// Default provider priority — cheapest first
const DEFAULT_PROVIDER_CHAIN = "deepseek,groq,gemini,together,openai";

function getProviderChain(preferred?: string): LLMProvider[] {
  // If a specific provider is requested, try it first then fall through
  const chainStr = Deno.env.get("LLM_PROVIDER") || DEFAULT_PROVIDER_CHAIN;
  const chainIds = chainStr.split(",").map((s) => s.trim().toLowerCase());

  // If caller requested a specific provider, put it first
  if (preferred && PROVIDERS[preferred]) {
    const idx = chainIds.indexOf(preferred);
    if (idx > 0) {
      chainIds.splice(idx, 1);
      chainIds.unshift(preferred);
    } else if (idx === -1) {
      chainIds.unshift(preferred);
    }
  }

  return chainIds
    .filter((id) => PROVIDERS[id])
    .map((id) => PROVIDERS[id])
    .filter((p) => Deno.env.get(p.envKey)); // Only include providers with keys set
}

// ── LLM call with provider fallback ─────────────────────────────────

const SYSTEM_MSG =
  "You are an AI agent playing an economics simulation game. You must respond with ONLY valid JSON. No markdown fences, no extra text. Stay in character.";

async function callOpenAIFormat(
  provider: LLMProvider,
  prompt: string
): Promise<string> {
  const apiKey = Deno.env.get(provider.envKey)!;
  const response = await fetch(`${provider.baseUrl}/chat/completions`, {
    method: "POST",
    headers: {
      Authorization: `Bearer ${apiKey}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      model: provider.defaultModel,
      messages: [
        { role: "system", content: SYSTEM_MSG },
        { role: "user", content: prompt },
      ],
      temperature: 0.7,
      max_tokens: 200,
    }),
  });

  if (!response.ok) {
    const errText = await response.text();
    throw new Error(`${provider.name} API error (${response.status}): ${errText}`);
  }

  const data = await response.json();
  const content = data.choices?.[0]?.message?.content?.trim();
  if (!content) throw new Error(`Empty response from ${provider.name}`);
  return content;
}

async function callGeminiFormat(
  provider: LLMProvider,
  prompt: string
): Promise<string> {
  const apiKey = Deno.env.get(provider.envKey)!;
  const model = provider.defaultModel;
  const url = `${provider.baseUrl}/models/${model}:generateContent?key=${apiKey}`;

  const response = await fetch(url, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      system_instruction: { parts: [{ text: SYSTEM_MSG }] },
      contents: [{ parts: [{ text: prompt }] }],
      generationConfig: { temperature: 0.7, maxOutputTokens: 200 },
    }),
  });

  if (!response.ok) {
    const errText = await response.text();
    throw new Error(`Gemini API error (${response.status}): ${errText}`);
  }

  const data = await response.json();
  const content = data.candidates?.[0]?.content?.parts?.[0]?.text?.trim();
  if (!content) throw new Error("Empty response from Gemini");
  return content;
}

async function callLLM(prompt: string, preferredProvider?: string): Promise<AgentDecision> {
  const chain = getProviderChain(preferredProvider);

  // Legacy fallback: if no provider-specific keys, check LLM_API_KEY
  if (chain.length === 0) {
    const legacyKey = Deno.env.get("LLM_API_KEY");
    if (!legacyKey) throw new Error("No LLM provider configured");
    chain.push({
      name: "Legacy",
      envKey: "LLM_API_KEY",
      baseUrl: Deno.env.get("LLM_BASE_URL") || "https://api.openai.com/v1",
      defaultModel: Deno.env.get("LLM_MODEL") || "gpt-4o-mini",
      format: "openai",
    });
  }

  let lastError: Error | null = null;

  for (const provider of chain) {
    try {
      const callFn = provider.format === "gemini" ? callGeminiFormat : callOpenAIFormat;
      const content = await callFn(provider, prompt);

      // Parse JSON — strip markdown fences if the model adds them
      const cleaned = content.replace(/^```json?\s*/, "").replace(/\s*```$/, "");
      const result = JSON.parse(cleaned);
      // Tag which provider was used (useful for analytics)
      result._provider = provider.name;
      return result;
    } catch (err) {
      console.error(`[${provider.name}] failed:`, err);
      lastError = err instanceof Error ? err : new Error(String(err));
    }
  }

  throw lastError || new Error("All LLM providers failed");
}

// ── Fallback engine (no LLM, uses personality weights) ───────────────
// Used when LLM is unavailable or for free-tier users.

function fallbackDecision(
  agent: AgentPersona,
  req: GameAgentRequest
): AgentDecision {
  const p = agent.personality;
  const actions = req.available_actions;

  // Simple heuristic: cooperation_bias determines action choice
  // For binary games (cooperate/defect)
  if (actions.includes("cooperate") && actions.includes("defect")) {
    let cooperateProb = p.cooperation_bias;

    // Adjust based on history (memory_weight)
    if (req.history.length > 0 && p.memory_weight > 0) {
      const lastRound = req.history[req.history.length - 1];
      const playerDefected = lastRound.player_action === "defect";
      if (playerDefected) {
        cooperateProb -= 0.3 * p.memory_weight;
      }
    }

    // Late-game defection (risk_tolerance drives end-game strategy)
    if (req.round > req.total_rounds * 0.8) {
      cooperateProb -= 0.15 * p.risk_tolerance;
    }

    cooperateProb = Math.max(0.05, Math.min(0.95, cooperateProb));
    const action = Math.random() < cooperateProb ? "cooperate" : "defect";

    return {
      action,
      amount: null,
      reasoning: action === "cooperate"
        ? `${agent.name} decides to cooperate based on their ${p.archetype} approach.`
        : `${agent.name} decides to defect — ${p.archetype} instincts kick in.`,
      agent_id: agent.id,
      agent_name: agent.name,
      personality: p.archetype,
    };
  }

  // For contribution games (amount-based)
  if (actions.includes("contribute")) {
    const maxContribution = (req.context?.max_contribution as number) || 100;
    let baseAmount = maxContribution * p.cooperation_bias;

    // Adjust based on group history
    if (req.history.length > 0 && p.memory_weight > 0) {
      const lastRound = req.history[req.history.length - 1];
      const contributions = Object.values(lastRound.agent_actions)
        .map((a) => a.amount || 0);
      const avgContribution =
        contributions.reduce((s, v) => s + v, 0) / Math.max(contributions.length, 1);
      const groupRatio = avgContribution / maxContribution;
      baseAmount = baseAmount * (1 - p.memory_weight) + maxContribution * groupRatio * p.memory_weight;
    }

    // Add noise based on risk_tolerance
    const noise = (Math.random() - 0.5) * maxContribution * 0.2 * p.risk_tolerance;
    const amount = Math.round(Math.max(0, Math.min(maxContribution, baseAmount + noise)));

    return {
      action: "contribute",
      amount,
      reasoning: `${agent.name} contributes ${amount} — reflecting their ${p.archetype} stance.`,
      agent_id: agent.id,
      agent_name: agent.name,
      personality: p.archetype,
    };
  }

  // For extraction games (commons)
  if (actions.includes("extract")) {
    const maxExtraction = (req.context?.max_extraction as number) || 100;
    let baseAmount = maxExtraction * (1 - p.cooperation_bias);

    // Resource scarcity awareness
    const resourceLevel = (req.context?.resource_level as number) ?? 1.0;
    if (resourceLevel < 0.4) {
      baseAmount *= 0.6 + 0.4 * p.risk_tolerance;
    }

    const noise = (Math.random() - 0.5) * maxExtraction * 0.15 * p.risk_tolerance;
    const amount = Math.round(Math.max(0, Math.min(maxExtraction, baseAmount + noise)));

    return {
      action: "extract",
      amount,
      reasoning: `${agent.name} extracts ${amount} — ${resourceLevel < 0.4 ? "resource is running low" : "balancing need with sustainability"}.`,
      agent_id: agent.id,
      agent_name: agent.name,
      personality: p.archetype,
    };
  }

  // For bid games
  if (actions.includes("bid")) {
    const estimatedValue = (req.context?.estimated_value as number) || 100;
    const bidRatio = 0.5 + p.risk_tolerance * 0.5;
    const noise = (Math.random() - 0.5) * estimatedValue * 0.2;
    const amount = Math.round(Math.max(1, estimatedValue * bidRatio + noise));

    return {
      action: "bid",
      amount,
      reasoning: `${agent.name} bids ${amount} — ${p.risk_tolerance > 0.6 ? "aggressive strategy" : "conservative approach"}.`,
      agent_id: agent.id,
      agent_name: agent.name,
      personality: p.archetype,
    };
  }

  // For join/wait games (network effects)
  if (actions.includes("join") && actions.includes("wait")) {
    const networkSize = (req.context?.network_size as number) ?? 0;
    const threshold = 1 - p.risk_tolerance;
    const action = networkSize >= threshold || Math.random() < p.risk_tolerance * 0.5
      ? "join"
      : "wait";

    return {
      action,
      amount: null,
      reasoning: `${agent.name} decides to ${action} — ${action === "join" ? "seeing enough momentum" : "waiting for more adoption"}.`,
      agent_id: agent.id,
      agent_name: agent.name,
      personality: p.archetype,
    };
  }

  // Default: pick first available action
  return {
    action: actions[0],
    amount: null,
    reasoning: `${agent.name} chooses ${actions[0]}.`,
    agent_id: agent.id,
    agent_name: agent.name,
    personality: p.archetype,
  };
}

// ── Main handler ─────────────────────────────────────────────────────

serve(async (req: Request) => {
  const cors = corsHeaders(req);

  if (req.method === "OPTIONS") {
    return new Response("ok", { headers: cors });
  }

  if (req.method !== "POST") {
    return new Response(JSON.stringify({ error: "Method not allowed" }), {
      status: 405,
      headers: { ...cors, "Content-Type": "application/json" },
    });
  }

  const origin = req.headers.get("Origin") || "";
  if (origin && !ALLOWED_ORIGINS.includes(origin)) {
    return new Response(JSON.stringify({ error: "Origin not allowed" }), {
      status: 403,
      headers: { ...cors, "Content-Type": "application/json" },
    });
  }

  try {
    const body: GameAgentRequest & { use_llm?: boolean } = await req.json();

    // Validate required fields
    if (!body.game_id || !body.agent_id || !body.round || !body.available_actions) {
      return new Response(
        JSON.stringify({
          error: "Missing required fields: game_id, agent_id, round, available_actions",
        }),
        { status: 400, headers: { ...cors, "Content-Type": "application/json" } }
      );
    }

    // Rate limit by IP or auth token
    const rateLimitKey =
      req.headers.get("Authorization")?.slice(0, 20) ||
      req.headers.get("X-Forwarded-For") ||
      "anonymous";
    if (isRateLimited(rateLimitKey)) {
      return new Response(
        JSON.stringify({ error: "Too many requests. Please wait." }),
        {
          status: 429,
          headers: { ...cors, "Content-Type": "application/json", "Retry-After": "60" },
        }
      );
    }

    // Load agent persona
    const agents = await loadAgents();
    const gameAgents = agents[body.game_id];
    if (!gameAgents) {
      return new Response(
        JSON.stringify({ error: `Unknown game: ${body.game_id}` }),
        { status: 404, headers: { ...cors, "Content-Type": "application/json" } }
      );
    }

    const agent = gameAgents[body.agent_id];
    if (!agent) {
      return new Response(
        JSON.stringify({ error: `Unknown agent: ${body.agent_id}` }),
        { status: 404, headers: { ...cors, "Content-Type": "application/json" } }
      );
    }

    let decision: AgentDecision;

    // Use LLM if requested and available, otherwise use fallback engine
    const hasAnyProvider = getProviderChain().length > 0 || Deno.env.get("LLM_API_KEY");
    const useLLM = body.use_llm !== false && hasAnyProvider;

    if (useLLM) {
      try {
        const prompt = buildPrompt(agent, body);
        const llmResult = await callLLM(prompt, (body as any).provider);
        decision = {
          ...llmResult,
          agent_id: agent.id,
          agent_name: agent.name,
          personality: agent.personality.archetype,
        };
      } catch (llmError) {
        console.error("LLM call failed, using fallback:", llmError);
        decision = fallbackDecision(agent, body);
      }
    } else {
      decision = fallbackDecision(agent, body);
    }

    // Validate action is in available_actions
    if (!body.available_actions.includes(decision.action)) {
      decision.action = body.available_actions[0];
      decision.reasoning += " (action corrected to valid option)";
    }

    return new Response(JSON.stringify(decision), {
      status: 200,
      headers: { ...cors, "Content-Type": "application/json" },
    });
  } catch (err) {
    console.error("game-agent error:", err);
    return new Response(JSON.stringify({ error: "Internal server error" }), {
      status: 500,
      headers: { ...cors, "Content-Type": "application/json" },
    });
  }
});
