#!/usr/bin/env node
/**
 * ImpactLex migration: parse course lexicons + external Varnasr/ImpactLex
 * into a unified `terms` dataset plus `caseStudies` and `formulae` sidecar
 * collections. Writes impactlex/data/seed-snapshot.json.
 *
 * Usage:
 *   node scripts/impactlex-migrate.mjs                    # local only (courses)
 *   node scripts/impactlex-migrate.mjs --with-external    # also pull external ImpactLex
 *   node scripts/impactlex-migrate.mjs --push             # also push to InstantDB
 *
 * Env (required for --push):
 *   INSTANTDB_APP_ID, INSTANTDB_ADMIN_TOKEN
 */

import { readFileSync, writeFileSync, existsSync, readdirSync } from 'node:fs';
import { resolve, join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';
import { createHash } from 'node:crypto';

const __dirname = dirname(fileURLToPath(import.meta.url));
const ROOT = resolve(__dirname, '..');
const COURSES_DIR = join(ROOT, 'courses');
const OUT = join(ROOT, 'impactlex/data/seed-snapshot.json');
const EXTERNAL_URL = 'https://raw.githubusercontent.com/Varnasr/ImpactLex/main/index.html';

const args = process.argv.slice(2);
const hasFlag = (f) => args.includes(f);

function slugify(s) {
  return String(s).toLowerCase()
    .replace(/\([^)]*\)/g, '')
    .replace(/[^a-z0-9\s-]/g, '')
    .trim().replace(/\s+/g, '-')
    .replace(/-+/g, '-')
    .slice(0, 80);
}

function inferCategory(label) {
  const l = (label || '').toLowerCase();
  if (/acronym|abbrev/.test(l)) return 'acronym';
  if (/formula|coefficient|calculation|measure/.test(l)) return 'formula';
  if (/framework|approach|model|logframe|toc/.test(l)) return 'framework';
  if (/method|design|technique|sampling|experiment|research/.test(l)) return 'method';
  if (/institution|donor|agency|organization|governance/.test(l)) return 'institution';
  if (/meal|m&e|monitoring|evaluation/.test(l)) return 'method';
  if (/climate/.test(l)) return 'concept';
  if (/economics|economic/.test(l)) return 'concept';
  if (/gender/.test(l)) return 'concept';
  return 'concept';
}

/**
 * Extract the first matching `const NAME = [ ... ];` array from an HTML blob,
 * respecting quoted strings and bracket depth. Returns the evaluated array or null.
 */
function extractArray(html, regex) {
  const start = html.search(regex);
  if (start === -1) return null;
  const bracketStart = html.indexOf('[', start);
  let depth = 0, i = bracketStart, inStr = false, strCh = '';
  for (; i < html.length; i++) {
    const ch = html[i];
    if (inStr) {
      if (ch === '\\') { i++; continue; }
      if (ch === strCh) inStr = false;
      continue;
    }
    if (ch === '"' || ch === "'" || ch === '`') { inStr = true; strCh = ch; continue; }
    if (ch === '[') depth++;
    else if (ch === ']') { depth--; if (depth === 0) { i++; break; } }
  }
  const src = html.slice(bracketStart, i);
  try {
    return new Function(`return ${src};`)();
  } catch (err) {
    console.warn(`[warn] failed to eval array for ${regex}: ${err.message}`);
    return null;
  }
}

function parseCourseLexicon(courseSlug) {
  const path = join(COURSES_DIR, courseSlug, 'lexicon.html');
  if (!existsSync(path)) return [];
  const html = readFileSync(path, 'utf8');
  const arr =
    extractArray(html, /const\s+lexiconData\s*=\s*\[/) ||
    extractArray(html, /const\s+LEXICON\s*=\s*\[/) ||
    extractArray(html, /const\s+TERMS\s*=\s*\[/) ||
    extractArray(html, /const\s+\w*[Ll]exicon\w*\s*=\s*\[/) ||
    extractArray(html, /const\s+\w*[Tt]erms\w*\s*=\s*\[/);
  if (!arr) { console.warn(`[warn] no lexicon array found in ${courseSlug}`); return []; }
  return arr.map((row) => ({
    term: row.term,
    category: inferCategory(row.category),
    seedCategory: row.category,
    definition: row.definition,
    example: row.example || '',
    courses: [courseSlug],
    source: 'course-lexicon',
  }));
}

function listCoursesWithLexicons() {
  return readdirSync(COURSES_DIR, { withFileTypes: true })
    .filter((d) => d.isDirectory())
    .map((d) => d.name)
    .filter((name) => existsSync(join(COURSES_DIR, name, 'lexicon.html')));
}

/**
 * Merge rows by lowercased term. Union courses, aliases, related, sources.
 * Keep longest definition; prefer non-empty example; prefer richer fields.
 */
function mergeByTerm(rows) {
  const map = new Map();
  for (const r of rows) {
    const key = (r.term || '').trim().toLowerCase();
    if (!key) continue;
    const existing = map.get(key);
    if (!existing) {
      map.set(key, {
        id: slugify(r.term),
        term: r.term,
        acronym: r.acronym || null,
        aliases: r.aliases || [],
        category: r.category,
        definition: r.definition || '',
        example: r.example || '',
        formula: r.formula || null,
        caseStudy: r.caseStudy || null,
        related: [...(r.related || [])],
        sources: [...(r.sources || [])],
        courses: [...(r.courses || [])],
        status: 'seed',
        source: r.source || 'seed',
        seedCategory: r.seedCategory,
        createdAt: new Date().toISOString(),
        updatedAt: new Date().toISOString(),
      });
      continue;
    }
    existing.courses = Array.from(new Set([...existing.courses, ...(r.courses || [])]));
    existing.related = Array.from(new Set([...existing.related, ...(r.related || [])]));
    existing.sources = Array.from(new Set([...existing.sources, ...(r.sources || [])]));
    if ((r.definition || '').length > existing.definition.length) existing.definition = r.definition;
    if (!existing.example && r.example) existing.example = r.example;
    if (!existing.acronym && r.acronym) existing.acronym = r.acronym;
    if (!existing.formula && r.formula) existing.formula = r.formula;
    if (!existing.caseStudy && r.caseStudy) existing.caseStudy = r.caseStudy;
    existing.updatedAt = new Date().toISOString();
  }
  return [...map.values()];
}

/**
 * Second-pass dedupe by id. mergeByTerm keys on the term string, but the id is
 * slugify(term) with acronyms stripped — so "Foo" and "Foo (F)" survive as two
 * rows that collide on one id. Collapse them: union list fields, keep the longest
 * definition, prefer a filled example/acronym/formula, prefer a 'published'
 * status and an acronym-bearing display term.
 */
function dedupeById(rows) {
  const map = new Map();
  for (const r of rows) {
    const existing = map.get(r.id);
    if (!existing) { map.set(r.id, { ...r }); continue; }
    existing.courses = Array.from(new Set([...(existing.courses || []), ...(r.courses || [])]));
    existing.related = Array.from(new Set([...(existing.related || []), ...(r.related || [])]));
    existing.sources = Array.from(new Set([...(existing.sources || []), ...(r.sources || [])]));
    existing.aliases = Array.from(new Set([...(existing.aliases || []), ...(r.aliases || [])]));
    if ((r.definition || '').length > (existing.definition || '').length) existing.definition = r.definition;
    if (!existing.example && r.example) existing.example = r.example;
    if (!existing.acronym && r.acronym) existing.acronym = r.acronym;
    if (!existing.formula && r.formula) existing.formula = r.formula;
    if (!existing.caseStudy && r.caseStudy) existing.caseStudy = r.caseStudy;
    if (existing.status !== 'published' && r.status === 'published') existing.status = 'published';
    if (!/\(/.test(existing.term || '') && /\(/.test(r.term || '')) existing.term = r.term;
    existing.updatedAt = new Date().toISOString();
  }
  return [...map.values()];
}

async function loadExternal() {
  let html;
  try {
    const res = await fetch(EXTERNAL_URL);
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    html = await res.text();
  } catch (err) {
    console.warn(`[warn] external fetch failed: ${err.message}`);
    return { terms: [], caseStudies: [], formulae: [] };
  }
  const glossary = extractArray(html, /const\s+GLOSSARY_DATA\s*=\s*\[/) || [];
  const caseStudies = extractArray(html, /const\s+CASE_STUDIES_DATA\s*=\s*\[/) || [];
  const formulae = extractArray(html, /const\s+FORMULAE_DATA\s*=\s*\[/) || [];
  console.log(`[info] external: ${glossary.length} terms, ${caseStudies.length} case studies, ${formulae.length} formulae`);

  const terms = glossary.map((g) => ({
    term: g.term,
    acronym: g.acronym,
    category: inferCategory(g.category),
    seedCategory: g.category,
    definition: g.definition,
    example: '',
    formula: g.formula || null,
    caseStudy: g.caseStudy || null,
    related: g.relatedTerms || [],
    sources: g.sources || [],
    courses: [],
    source: 'external-impactlex',
  }));

  return {
    terms,
    caseStudies: caseStudies.map((c) => ({ ...c, source: 'external-impactlex' })),
    formulae: formulae.map((f) => ({ ...f, source: 'external-impactlex' })),
  };
}

/**
 * Deterministic UUID v4-formatted string derived from a slug.
 * Same slug always yields the same UUID → re-pushes are idempotent upserts.
 * InstantDB requires UUIDs as entity IDs; we keep the slug queryable in `slug`.
 */
function slugToUuid(slug, namespace = 'impactlex') {
  const h = createHash('sha256').update(`${namespace}:${slug}`).digest('hex');
  const variant = (parseInt(h.slice(16, 17), 16) & 0x3 | 0x8).toString(16);
  return `${h.slice(0, 8)}-${h.slice(8, 12)}-4${h.slice(13, 16)}-${variant}${h.slice(17, 20)}-${h.slice(20, 32)}`;
}

async function pushToInstantDB(snapshot) {
  const appId = process.env.INSTANTDB_APP_ID;
  const adminToken = process.env.INSTANTDB_ADMIN_TOKEN;
  if (!appId || !adminToken) {
    console.error('[err] --push requires INSTANTDB_APP_ID and INSTANTDB_ADMIN_TOKEN');
    process.exit(1);
  }
  const endpoint = `https://api.instantdb.com/admin/transact`;
  const pushCollection = async (collection, rows, slugField = 'slug') => {
    for (let i = 0; i < rows.length; i += 100) {
      const chunk = rows.slice(i, i + 100);
      const steps = chunk.map((row) => {
        const slug = row.id; // original slug
        const uuid = slugToUuid(`${collection}:${slug}`);
        const { id, ...rest } = row;
        return ['update', collection, uuid, { ...rest, [slugField]: slug }];
      });
      const res = await fetch(endpoint, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${adminToken}`,
          'App-Id': appId,
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ steps }),
      });
      if (!res.ok) throw new Error(`InstantDB push ${collection} failed (${res.status}): ${await res.text()}`);
      console.log(`[push] ${collection} ${i + chunk.length}/${rows.length}`);
    }
  };
  await pushCollection('terms', snapshot.terms);
  if (snapshot.caseStudies.length) await pushCollection('caseStudies', snapshot.caseStudies);
  if (snapshot.formulae.length) await pushCollection('formulae', snapshot.formulae);
}

async function main() {
  const courses = listCoursesWithLexicons();
  console.log(`[info] found ${courses.length} course lexicons: ${courses.join(', ')}`);

  const courseRows = courses.flatMap(parseCourseLexicon);
  console.log(`[info] parsed ${courseRows.length} course-lexicon entries`);

  let external = { terms: [], caseStudies: [], formulae: [] };
  if (hasFlag('--with-external')) {
    external = await loadExternal();
  }

  const merged = dedupeById(mergeByTerm([...external.terms, ...courseRows]));
  merged.sort((a, b) => a.term.localeCompare(b.term));

  const snapshot = {
    generatedAt: new Date().toISOString(),
    count: merged.length,
    counts: {
      terms: merged.length,
      caseStudies: external.caseStudies.length,
      formulae: external.formulae.length,
    },
    courses,
    terms: merged,
    caseStudies: external.caseStudies,
    formulae: external.formulae,
  };

  writeFileSync(OUT, JSON.stringify(snapshot, null, 2));
  console.log(`[ok] wrote ${merged.length} terms + ${external.caseStudies.length} case studies + ${external.formulae.length} formulae to ${OUT}`);

  if (hasFlag('--push')) await pushToInstantDB(snapshot);
}

main().catch((err) => { console.error(err); process.exit(1); });
