/**
 * Netlify Function — Partner REST API (read-only)
 *
 * A public, key-free, read-only JSON API for organizations to integrate
 * ImpactMojo's open content catalog.
 *
 * Base URL: https://www.impactmojo.in/api/v1
 *
 * Endpoints (all GET, JSON, CORS *, Cache-Control public max-age=300):
 *   GET /api/v1                 -> API index (name, version, endpoints, license, rate-limit note)
 *   GET /api/v1/catalog         -> full content catalog (courses+labs+games+book companions+handouts)
 *                                  filters: ?type=course|game|lab|handout|book  ?q=<substr>  ?limit=<1..500>
 *   GET /api/v1/courses         -> courses only (101 + flagship), enriched from decks/catalog data
 *   GET /api/v1/courses/:slug   -> single course detail by slug (404 JSON if not found)
 *   GET /api/v1/stats           -> counts by type
 *
 * Data is loaded at runtime from the deployed static assets (search-index.json,
 * decks.json, catalog_data.json) with a short in-memory cache. A fetch failure
 * yields a 502 JSON error.
 *
 * License: content is CC BY-NC-ND 4.0. Attribution to ImpactMojo (impactmojo.in)
 * is required. No commercial redistribution. This API exposes metadata only.
 */

const SITE = "https://www.impactmojo.in";
const VERSION = "1.0";
const LICENSE = "CC BY-NC-ND 4.0 — attribution to ImpactMojo (impactmojo.in) required; non-commercial; no derivatives.";
const RATE_LIMIT_NOTE = "No API key required. Read-only. Please cache responses (Cache-Control: public, max-age=300) and avoid more than ~60 requests/min. Contact hello@impactmojo.in for higher-volume access.";

const CORS = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Methods": "GET, OPTIONS",
  "Access-Control-Allow-Headers": "Content-Type",
};
const JSON_HEADERS = {
  "Content-Type": "application/json; charset=utf-8",
  "Cache-Control": "public, max-age=300",
  ...CORS,
};

// ---- in-memory cache (per warm function instance) ---------------------------
const CACHE_TTL_MS = 5 * 60 * 1000;
const _cache = { at: 0, data: null };

async function fetchJson(path) {
  const res = await fetch(`${SITE}${path}`, { headers: { Accept: "application/json" } });
  if (!res.ok) throw new Error(`Upstream ${path} returned ${res.status}`);
  return res.json();
}

async function loadData() {
  const now = Date.now();
  if (_cache.data && now - _cache.at < CACHE_TTL_MS) return _cache.data;
  const [searchIndex, decks, catalog] = await Promise.all([
    fetchJson("/data/search-index.json"),
    fetchJson("/data/decks.json"),
    fetchJson("/catalog_data.json"),
  ]);
  const data = { searchIndex, decks, catalog };
  _cache.data = data;
  _cache.at = now;
  return data;
}

// ---- helpers ----------------------------------------------------------------

// Map a public ?type= filter value to the search-index `type` values it covers.
const TYPE_ALIASES = {
  course: ["course"],
  game: ["game"],
  lab: ["lab"],
  book: ["book-summary"],
  handout: ["handout", "practice-pack"], // search-index has no "handout"; practice-packs are the closest downloadable analogue
};

function normalizeItem(it) {
  return {
    id: it.id,
    title: it.title,
    description: it.description || "",
    type: it.type,
    category: it.category || null,
    url: it.url ? `${SITE}${it.url}` : null,
    tags: Array.isArray(it.tags) ? it.tags : [],
  };
}

function slugFromUrl(url) {
  if (!url) return null;
  // /courses/mel/  -> mel ; /101-courses/dev-economics.html -> dev-economics
  const clean = url.replace(/[#?].*$/, "").replace(/\/+$/, "");
  const last = clean.split("/").pop() || "";
  return last.replace(/\.html$/, "") || null;
}

// Build the enriched course list from search-index + decks + catalog_data.
function buildCourses(data) {
  const { searchIndex, decks, catalog } = data;
  const deckBySlug = new Map();
  for (const d of (decks?.decks || [])) deckBySlug.set(d.slug, d);

  // catalog_data META is keyed by title; DATA has level/track per title
  const catalogByTitle = new Map();
  for (const row of (catalog?.DATA || [])) catalogByTitle.set(row.title, row);

  const courses = [];
  for (const it of searchIndex) {
    if (it.type !== "course") continue;
    const slug = slugFromUrl(it.url);
    const deck = slug ? deckBySlug.get(slug) : null;
    const cat = catalogByTitle.get(it.title);
    const isFlagship = (it.url || "").startsWith("/courses/");
    courses.push({
      slug,
      id: it.id,
      title: it.title,
      description: it.description || deck?.desc || "",
      url: it.url ? `${SITE}${it.url}` : null,
      track: cat?.track || it.category || null,
      level: deck?.level || cat?.level || null,
      format: deck?.format || (isFlagship ? "Flagship course" : null),
      tier: isFlagship ? "flagship" : "101",
      slides: deck?.slides ?? null,
      license: deck?.license || "CC BY-NC-ND 4.0",
      features: deck?.features || null,
      sections: deck?.sections || null,
      tags: Array.isArray(it.tags) ? it.tags : [],
    });
  }
  return courses;
}

function jsonResponse(payload, status = 200) {
  return new Response(JSON.stringify(payload, null, 2), { status, headers: JSON_HEADERS });
}

function errorResponse(message, status = 500) {
  return new Response(JSON.stringify({ error: message }, null, 2), { status, headers: JSON_HEADERS });
}

// ---- route handlers ---------------------------------------------------------

function handleIndex() {
  return jsonResponse({
    name: "ImpactMojo Partner API",
    version: VERSION,
    base_url: `${SITE}/api/v1`,
    description: "Read-only REST API for organizations to integrate ImpactMojo's open development-education content.",
    endpoints: [
      { method: "GET", path: "/api/v1", description: "This index." },
      { method: "GET", path: "/api/v1/catalog", description: "Full content catalog. Filters: ?type=course|game|lab|handout|book, ?q=<substring>, ?limit=<1..500>." },
      { method: "GET", path: "/api/v1/courses", description: "Courses only (101 foundational + flagship), enriched with slides/level/format/features." },
      { method: "GET", path: "/api/v1/courses/{slug}", description: "Single course detail by slug. 404 if not found." },
      { method: "GET", path: "/api/v1/stats", description: "Content counts by type." },
    ],
    license: LICENSE,
    rate_limit: RATE_LIMIT_NOTE,
    contact: "hello@impactmojo.in",
  });
}

async function handleCatalog(url, data) {
  const KNOWN = new Set(["course", "game", "lab", "book-summary", "practice-pack"]);
  let items = data.searchIndex
    .filter((it) => KNOWN.has(it.type))
    .map(normalizeItem);

  const typeParam = (url.searchParams.get("type") || "").trim().toLowerCase();
  if (typeParam) {
    const allowed = TYPE_ALIASES[typeParam];
    if (!allowed) {
      return errorResponse(`Unknown type "${typeParam}". Valid: ${Object.keys(TYPE_ALIASES).join(", ")}.`, 400);
    }
    const allowedSet = new Set(allowed);
    items = items.filter((it) => allowedSet.has(it.type));
  }

  const q = (url.searchParams.get("q") || "").trim().toLowerCase();
  if (q) {
    items = items.filter(
      (it) =>
        (it.title || "").toLowerCase().includes(q) ||
        (it.description || "").toLowerCase().includes(q)
    );
  }

  let limit = parseInt(url.searchParams.get("limit") || "100", 10);
  if (!Number.isFinite(limit) || limit < 1) limit = 100;
  if (limit > 500) limit = 500;

  const total = items.length;
  const sliced = items.slice(0, limit);

  return jsonResponse({
    count: sliced.length,
    total,
    limit,
    filters: { type: typeParam || null, q: q || null },
    items: sliced,
    license: LICENSE,
    attribution: "Content © ImpactMojo, CC BY-NC-ND 4.0 — https://impactmojo.in",
  });
}

function handleCourses(data) {
  const courses = buildCourses(data);
  return jsonResponse({
    count: courses.length,
    courses,
    license: LICENSE,
    attribution: "Content © ImpactMojo, CC BY-NC-ND 4.0 — https://impactmojo.in",
  });
}

function handleCourseDetail(slug, data) {
  const courses = buildCourses(data);
  const course = courses.find((c) => c.slug === slug);
  if (!course) {
    return errorResponse(`No course found with slug "${slug}".`, 404);
  }
  return jsonResponse({ course, license: LICENSE });
}

function handleStats(data) {
  const counts = {};
  for (const it of data.searchIndex) {
    const t = it.type || "unknown";
    counts[t] = (counts[t] || 0) + 1;
  }
  const courses = buildCourses(data);
  const flagship = courses.filter((c) => c.tier === "flagship").length;
  return jsonResponse({
    total_items: data.searchIndex.length,
    by_type: counts,
    courses: { total: courses.length, flagship, foundational_101: courses.length - flagship },
    license: LICENSE,
  });
}

// ---- entrypoint -------------------------------------------------------------

export default async (req) => {
  if (req.method === "OPTIONS") {
    return new Response(null, { status: 204, headers: CORS });
  }
  if (req.method !== "GET") {
    return errorResponse("Method not allowed. This API is read-only (GET).", 405);
  }

  const url = new URL(req.url);
  // Normalize: strip trailing slash (except root), strip the /api/v1 prefix.
  let path = url.pathname.replace(/\/+$/, "") || "/api/v1";
  // path is one of: /api/v1, /api/v1/catalog, /api/v1/courses, /api/v1/courses/<slug>, /api/v1/stats
  const sub = path.replace(/^\/api\/v1/, "") || "/"; // "" -> "/"

  // Index needs no data.
  if (sub === "/" || sub === "") return handleIndex();

  let data;
  try {
    data = await loadData();
  } catch (e) {
    return errorResponse(`Failed to load catalog data: ${e.message}`, 502);
  }

  if (sub === "/catalog") return handleCatalog(url, data);
  if (sub === "/courses") return handleCourses(data);
  if (sub.startsWith("/courses/")) {
    const slug = decodeURIComponent(sub.slice("/courses/".length).replace(/\/+$/, ""));
    if (!slug) return handleCourses(data);
    return handleCourseDetail(slug, data);
  }
  if (sub === "/stats") return handleStats(data);

  return errorResponse(`Unknown endpoint "${url.pathname}". See ${SITE}/api/v1 for the endpoint list.`, 404);
};

export const config = {
  path: [
    "/api/v1",
    "/api/v1/catalog",
    "/api/v1/courses",
    "/api/v1/courses/:slug",
    "/api/v1/stats",
  ],
};
