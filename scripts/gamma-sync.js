#!/usr/bin/env node
/**
 * gamma-sync.js — Regenerate all ImpactMojo 101 courses via Gamma API
 * with consistent branding, fonts, imagery, and footer.
 *
 * Usage:
 *   GAMMA_API_KEY=sk-gamma-... node scripts/gamma-sync.js [--dry-run] [--course mel-basics]
 *
 * Options:
 *   --dry-run       Print payloads without calling the API
 *   --course SLUG   Regenerate a single course by slug
 *   --delay MS      Delay between API calls in ms (default: 5000)
 *   --resume        Skip courses already completed in gamma-sync-results.json
 *   --force         Regenerate ALL courses, even previously completed ones
 */

const { execSync } = require("child_process");
const fs = require("fs");
const path = require("path");
const os = require("os");

// ─── Config ──────────────────────────────────────────────────────────────────

const API_BASE = "https://public-api.gamma.app/v1.0";
const API_KEY = process.env.GAMMA_API_KEY;
const FOLDER_ID = "fw1e4twcu3rypew"; // "101 Decks" folder
const POLL_INTERVAL = 5000; // 5s between status checks
const POLL_TIMEOUT = 900000; // 15min max wait per generation (60-slide decks can take 10min+)

// Closest built-in theme: clean, light, blue — matches ImpactMojo palette
const THEME_ID = "cornflower";

// ─── Art style per category ─────────────────────────────────────────────────

const ART_STYLES = {
  "MEL & Research": "STRICTLY MONOCHROME sepia-toned photograph (zero color, only brown/cream/black tones like a 1920s film photo). Show South Asian people as dark SILHOUETTES (no facial detail, no fingers, no teeth — only solid dark human shapes in profile or action poses). Scene: rural Indian villages, fields, community meetings, data collection. Framed with a VISIBLE Warli tribal art decorative border — geometric white dot-patterns on earthy terracotta edges surrounding the entire image",
  "Data & Technology": "STRICTLY MONOCHROME sepia-toned photograph (zero color, only brown/cream/black tones like a 1920s film photo). Show South Asian people as dark SILHOUETTES (no facial detail, no fingers, no teeth — only solid dark human shapes in profile or action poses). Scene: Indian village technology use, notebooks, chalkboards, radio towers, mobile phones. Framed with a VISIBLE Gond art decorative border — intricate dot-and-line nature patterns on dark edges surrounding the entire image",
  "Policy & Economics": "STRICTLY MONOCHROME sepia-toned photograph (zero color, only brown/cream/black tones like a 1920s film photo). Show South Asian people as dark SILHOUETTES (no facial detail, no fingers, no teeth — only solid dark human shapes in profile or action poses). Scene: Indian governance, markets, panchayat meetings, public life. Framed with a VISIBLE Kalamkari art decorative border — flowing hand-drawn textile patterns in terracotta and indigo edges surrounding the entire image",
  "Gender & Equity": "STRICTLY MONOCHROME sepia-toned photograph (zero color, only brown/cream/black tones like a 1920s film photo). Show South Asian people as dark SILHOUETTES — women in sarees, men in kurtas, children, transgender individuals (hijra) — (no facial detail, no fingers, no teeth — only solid dark human shapes in profile or action poses). Scene: Indian village schools, SHG meetings, handlooms, community spaces. Framed with a VISIBLE Madhubani art decorative border — bold crosshatched patterns in primary colors on edges surrounding the entire image",
  "Health & Communication": "STRICTLY MONOCHROME sepia-toned photograph (zero color, only brown/cream/black tones like a 1920s film photo). Show South Asian people as dark SILHOUETTES — health workers, mothers, children — (no facial detail, no fingers, no teeth — only solid dark human shapes in profile or action poses). Scene: Indian primary health centers, anganwadis, community health settings. Framed with a VISIBLE Pattachitra art decorative border — ornamental narrative panels in jewel tones on edges surrounding the entire image",
  "Philosophy & Governance": "STRICTLY MONOCHROME sepia-toned photograph (zero color, only brown/cream/black tones like a 1920s film photo). Show South Asian people as dark SILHOUETTES (no facial detail, no fingers, no teeth — only solid dark human shapes in profile or action poses). Scene: Indian democratic institutions, community gatherings, temples, village assemblies. Framed with a VISIBLE Pichwai art decorative border — lotus and nature motifs in deep green and gold edges surrounding the entire image",
};

// ─── Shared image & content style ───────────────────────────────────────────

const IMAGE_STYLE_BASE = [
  "CRITICAL RULE — HUMANS AS SILHOUETTES ONLY: Show people as solid dark silhouettes — no visible facial features, no teeth, no detailed fingers, no skin texture. Just dark human shapes in profile, walking, working, gathering, or in action poses. This avoids grotesque AI-generated faces. Show diverse silhouettes: women in sarees and salwar kameez, men in kurtas and dhotis, children, elders, transgender individuals (hijra community). Mixed ages and genders.",
  "CRITICAL RULE — STRICTLY MONOCHROME SEPIA: Every photograph MUST be fully desaturated sepia-toned (brown/cream/black only, like a 1920s archival photograph). ZERO color anywhere. No blue skies, no green trees, no colored clothing. Only warm brown/cream/black tones with soft grain.",
  "CRITICAL RULE — EVERY IMAGE MUST HAVE A THICK DECORATIVE BORDER: Every generated image MUST be surrounded by a clearly visible, thick folk art decorative border/frame (at least 5% of image width on each side) from the specified Indian art tradition. The border must be unmistakable. No borderless images allowed. If you generate an image without a folk art border, regenerate it.",
  "CRITICAL RULE — PHOTOREALISTIC ONLY: All images must look like real sepia photographs, not illustrations, not cartoons, not drawings, not digital art. Photorealistic with film grain.",
  "MANDATORY: Settings must be rural Indian villages, peri-urban small towns, fields, mandis (markets), anganwadis, primary health centers, gram panchayat offices, temples, river banks, farms. NEVER show glass offices, luxury interiors, Western cities, or affluent urban settings.",
  "Scenes: farming, hand-pumping water, SHG meetings, mid-day meals, ASHA workers visiting homes, children studying under trees, panchayat meetings, market days, handloom weaving, fishing. With animals: cows, buffaloes, goats, bullocks with carts.",
  "Emotional tone: dignity, agency, warmth, resilience, beauty. NOT poverty-porn. Silhouettes should convey purposeful action and community.",
].join(" ");

// ─── Footer config ──────────────────────────────────────────────────────────

const HEADER_FOOTER = {
  bottomLeft: {
    type: "cardNumber",
  },
  bottomCenter: {
    type: "text",
    value: "www.impactmojo.in",
  },
  bottomRight: {
    type: "text",
    value: "CC BY-NC-ND 4.0",
  },
  hideFromFirstCard: false,
  hideFromLastCard: false,
};

// ─── Additional instructions for font & style enforcement ───────────────────

const ADDITIONAL_INSTRUCTIONS = [
  "CRITICAL FONT RULES:",
  "- ALL headings, titles, and section headers MUST use the font 'Inter' (bold or semibold weight).",
  "- ALL body text, descriptions, bullet points, and captions MUST use the font 'Amaranth' (regular weight).",
  "- Do NOT use any other fonts. Only Inter for headings and Amaranth for body text throughout the entire deck.",
  "",
  "BRANDING: This is an ImpactMojo course — a free development education platform for South Asia.",
  "AUDIENCE: Development professionals, students, researchers, and practitioners in South Asia.",
  "TONE: Educational, accessible, warm, rigorous but not academic. Avoid jargon where possible.",
  "",
  "NOTE: Slide numbers, website URL, and license are already handled by the deck footer — do NOT duplicate them in the slide body content.",
  "",
  "STRUCTURE (follow this order strictly):",
  "1. TITLE CARD — Course name, subtitle, 'ImpactMojo 101 Series' branding, category label, www.impactmojo.in",
  "2. AGENDA / OUTLINE CARD — Numbered list of all sections covered in the deck, styled as a visual table of contents",
  "3-N. CONTENT SECTIONS (10-12 major sections) — Each major topic gets:",
  "   - A SECTION SEPARATOR CARD with the section number, title, and a relevant folk art illustration (full-bleed)",
  "   - 4-6 content cards for that section with concepts, case studies, diagrams, exercises",
  "CLOSING: Quiz/Self-Assessment, Key Takeaways, Glossary, Further Reading",
  "",
  "FINAL SLIDE (MANDATORY — DO NOT SKIP):",
  "The very last slide (slide 60) MUST be a 'Thank You' branded closing card with:",
  "  - Large heading: 'Thank You for Learning with ImpactMojo'",
  "  - Subheading: 'Keep exploring. Keep questioning. Keep building.'",
  "  - Contact: hello@impactmojo.in",
  "  - Website: www.impactmojo.in",
  "  - License: CC BY-NC-ND 4.0",
  "  - '🎓 Explore More ImpactMojo 101 Courses:' followed by 2-3 related course suggestions",
  "  - A sepia silhouette image with folk art border as the background",
  "This Thank You slide is REQUIRED. Do not end the deck without it.",
  "",
  "TARGET: 60 slides (the maximum). Do NOT compress. Every concept deserves its own slide.",
  "",
  "DIAGRAMS & CHARTS: Use plenty of diagrams, flowcharts, comparison tables, process flows, frameworks, and data visualizations.",
  "Make charts beautiful, colorful, and non-boring — use creative layouts like radial diagrams, Sankey flows, pyramid charts, matrix grids.",
  "Every section should have at least one visual framework, diagram, or chart. Never have 3+ text-only slides in a row.",
  "",
  "SECTION SEPARATORS: Use bold, visually distinct separator cards between major sections. Full-width background color or illustration. Section number + title only, no body text.",
  "",
  "LAYOUT: Clean layouts with generous whitespace. Use card-based sections.",
  "",
  "IMAGE RULES (CRITICAL — READ CAREFULLY):",
  "1. Show people ONLY as dark SILHOUETTES — no facial features, no teeth, no detailed fingers, no skin. Solid dark human shapes in profile or action. Diverse: women in sarees, men in kurtas, children, elders, hijra community.",
  "2. ALL images must be FULLY SEPIA MONOCHROME — brown/cream/black tones only, zero color. Like a 1920s archival photograph.",
  "3. ALL images must be PHOTOREALISTIC photographs, not illustrations or drawings or cartoons.",
  "4. EVERY image MUST have a VISIBLE, THICK decorative Indian folk art border/frame around it. The border must be clearly visible — at least 5% of the image width on each side. No borderless images. If an image does not have a folk art border, it is WRONG.",
  "",
  "CONTEXT: Rural India, community development, grassroots settings. Democratic and inclusive.",
  "ACCESSIBILITY: High contrast text. No text over busy backgrounds.",
].join("\n");

// ─── Course catalog ─────────────────────────────────────────────────────────
// 26/38 completed — only the 12 remaining courses below need generation.
// Completed slugs (for reference): mel-basics, research-ethics, visual-eth,
// qual-methods, obs2insight, eng-dev, data-lit, data-feminism, eda-hhs,
// bi-analysis, multivariate-basics, irt-basics, econometrics-101, digital-ethics,
// climate-essentials, dev-economics, pol-economy, cost-effectiveness,
// livelihood-basics, advocacy-basics, fundraising-basics, post-truth-101,
// dev-architecture, edu-pedagogy, SRHR-basics, wee-studies

const COURSES = [
  // Gender & Equity (remaining)
  { slug: "social-margins", title: "Marginalised Identities 101", category: "Gender & Equity", description: "Examine how caste, ethnicity, disability, sexuality, and other identity markers create overlapping systems of marginalization." },
  { slug: "decent-work", title: "Decent Work For All 101", category: "Gender & Equity", description: "Explore ILO frameworks for promoting productive employment, labor rights, social protection, and social dialogue." },
  { slug: "care-economy-101", title: "Care Economy 101", category: "Gender & Equity", description: "Understand the economic value of unpaid care work and explore policies that support care workers while redistributing care responsibilities." },
  { slug: "sel-basics", title: "Social and Emotional Learning 101", category: "Gender & Equity", description: "Understand SEL frameworks and their application in education and youth development programs worldwide." },

  // Health & Communication (remaining)
  { slug: "pub-health-basics", title: "Public Health 101", category: "Health & Communication", description: "Navigate fundamentals of epidemiology, health systems, and disease prevention strategies that underpin global health interventions." },
  { slug: "bcc-comms", title: "Behaviour Change Communications 101", category: "Health & Communication", description: "Master the psychology and practice of designing communication interventions that shift behaviors, from health to environmental conservation." },

  // Philosophy & Governance (remaining)
  { slug: "ind-constitution", title: "Indian Constitution 101", category: "Philosophy & Governance", description: "Examine the constitutional framework guiding India's democracy, including fundamental rights, directive principles, and federal structure." },
  { slug: "inequality-basics", title: "Poverty and Inequality 101", category: "Philosophy & Governance", description: "Examine multidimensional poverty measurement, inequality indices, and structural drivers of economic disparities." },
  { slug: "decolonize-dev", title: "Decolonial Development 101", category: "Philosophy & Governance", description: "Challenge dominant development paradigms through postcolonial and decolonial frameworks questioning Western-centric approaches." },
  { slug: "community-dev", title: "Community Development 101", category: "Philosophy & Governance", description: "Master participatory approaches to community mobilization, from asset-based development to collective action and social capital." },
  { slug: "env-justice", title: "Environmental Justice 101", category: "Philosophy & Governance", description: "Explore how environmental degradation disproportionately impacts marginalized communities and frameworks for equitable environmental governance." },

  // MEL & Research (remaining)
  { slug: "toc-workbench", title: "Theory of Change Workbench 101", category: "MEL & Research", description: "Build and test Theories of Change for development programs using logical frameworks and results chains." },

  // Phase II regenerations — recovered decks missing PDFs/latest branding
  { slug: "edu-pedagogy", title: "Education and Pedagogy 101", category: "Health & Communication", description: "Discover evidence-based teaching methodologies, learning theories, and pedagogical approaches for development education contexts." },
  { slug: "SRHR-basics", title: "Sexual and Reproductive Health and Rights 101", category: "Health & Communication", description: "Navigate SRHR frameworks, rights-based approaches, and evidence-based programming for sexual and reproductive health." },
  { slug: "wee-studies", title: "Women's Economic Empowerment 101", category: "Gender & Equity", description: "Understand frameworks, evidence, and interventions for advancing women's economic participation, agency, and empowerment." },

  // Phase II — decks with broken PDF export URLs needing fresh generation
  { slug: "fundraising-basics", title: "Fundraising Basics 101", category: "Policy & Economics", description: "Develop essential skills for resource mobilization, donor engagement, and sustainable funding strategies in the development sector." },
  { slug: "post-truth-101", title: "Post-Truth Politics 101", category: "Philosophy & Governance", description: "Analyze how misinformation, polarization, and post-truth narratives shape public discourse and development outcomes." },
  { slug: "dev-architecture", title: "Global Development Governance 101", category: "Policy & Economics", description: "Navigate the complex ecosystem of multilateral development institutions, bilateral aid, and global governance frameworks." },
];

// ─── HTTP helpers (using curl for DNS reliability) ───────────────────────────

function apiRequestOnce(method, apiPath, body) {
  const url = API_BASE + apiPath;
  const curlArgs = [
    "curl", "-s", "-w", "'\\n%{http_code}'",
    "-X", method,
    "-H", `'X-API-KEY: ${API_KEY}'`,
    "-H", "'Content-Type: application/json'",
    "--connect-timeout", "30",
    "--max-time", "120",
  ];

  let tmpFile;
  if (body) {
    tmpFile = path.join(os.tmpdir(), `gamma-payload-${Date.now()}.json`);
    fs.writeFileSync(tmpFile, JSON.stringify(body));
    curlArgs.push("-d", `@${tmpFile}`);
  }

  curlArgs.push(`'${url}'`);

  let raw;
  try {
    raw = execSync(curlArgs.join(" "), {
      encoding: "utf8",
      timeout: 120000,
      shell: "/bin/bash",
      maxBuffer: 10 * 1024 * 1024,
    }).trim();
  } finally {
    if (tmpFile && fs.existsSync(tmpFile)) fs.unlinkSync(tmpFile);
  }

  const lines = raw.split("\n");
  const statusCode = parseInt(lines.pop(), 10);
  const responseBody = lines.join("\n");

  let data;
  try {
    data = JSON.parse(responseBody);
  } catch {
    data = responseBody;
  }
  return { status: statusCode, data };
}

const MAX_RETRIES = 4;
const RETRY_BACKOFF = [2000, 4000, 8000, 16000];

async function apiRequest(method, apiPath, body) {
  for (let attempt = 0; attempt <= MAX_RETRIES; attempt++) {
    try {
      return apiRequestOnce(method, apiPath, body);
    } catch (err) {
      if (attempt === MAX_RETRIES) {
        throw new Error(`API ${method} ${apiPath} failed after ${MAX_RETRIES + 1} attempts: ${err.message}`);
      }
      const backoff = RETRY_BACKOFF[attempt] || 16000;
      console.log(`  ⚠ Network error (attempt ${attempt + 1}/${MAX_RETRIES + 1}), retrying in ${backoff / 1000}s...`);
      await sleep(backoff);
    }
  }
}

function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

// ─── Build generation payload for a course ──────────────────────────────────

function buildPayload(course) {
  const artStyle = ART_STYLES[course.category] || ART_STYLES["MEL & Research"];

  const inputText = [
    `# ${course.title}`,
    "",
    `## ImpactMojo 101 Course`,
    "",
    course.description,
    "",
    `Category: ${course.category}`,
    "",
    "Create a comprehensive, visually rich educational deck covering key concepts, frameworks, case studies, and practical applications for this topic in the South Asian development context.",
    "",
    "Structure (follow strictly):",
    "1. TITLE CARD — Course name, subtitle, 'ImpactMojo 101 Series', category badge",
    "2. AGENDA CARD — Visual outline/table of contents listing all sections",
    "3. LEARNING OBJECTIVES — What participants will be able to do after this course",
    "",
    "Then 10-12 MAJOR SECTIONS, each with:",
    "  - A bold SECTION SEPARATOR card (section number + title, full visual, no body text)",
    "  - 4-6 content cards per section covering:",
    "    * Core concepts and definitions",
    "    * A diagram, flowchart, or framework visual (EVERY section must have at least one)",
    "    * A real-world case study from India, Bangladesh, Nepal, Sri Lanka, or Pakistan",
    "    * Practical exercise, reflection prompt, or discussion question",
    "    * Comparison tables, matrix grids, or data visualizations where relevant",
    "  - Use flowcharts, process diagrams, matrix grids, radial charts, pyramid models, Venn diagrams, timelines — make them beautiful and non-boring",
    "",
    "Then closing cards:",
    "  - QUIZ / SELF-ASSESSMENT — 5-8 multiple choice or reflection questions to test understanding",
    "  - KEY TAKEAWAYS — Bullet summary of core learnings from all sections",
    "  - GLOSSARY — Key terms and definitions introduced in the course",
    "  - FURTHER READING — Books, papers, websites, and resources for deeper study",
    "  - THANK YOU — 'Thank You for Learning with ImpactMojo' / hello@impactmojo.in / www.impactmojo.in / suggest 2-3 related ImpactMojo 101 courses to explore next",
    "",
    "IMPORTANT: This deck MUST use all 60 slides. Do not compress content. Each concept deserves its own slide. Use generous visual slides between text-heavy ones. Fill every available slide.",
  ].join("\n");

  const imageStyle = `${artStyle}. ${IMAGE_STYLE_BASE}`;

  return {
    inputText,
    textMode: "generate",
    format: "presentation",
    numCards: 60,
    themeId: THEME_ID,
    additionalInstructions: ADDITIONAL_INSTRUCTIONS,
    imageOptions: {
      source: "aiGenerated",
      style: imageStyle,
    },
    textOptions: {
      amount: "medium",
      tone: "Educational, accessible, warm. Rigorous but approachable. South Asian development context.",
      audience: "Development professionals, students, researchers, and practitioners in South Asia. Beginner to intermediate level.",
      language: "en",
    },
    cardOptions: {
      dimensions: "16x9",
      headerFooter: HEADER_FOOTER,
    },
    folderIds: [FOLDER_ID],
    exportAs: "pdf",
  };
}

// ─── Poll for generation completion ─────────────────────────────────────────

async function pollGeneration(generationId) {
  const startTime = Date.now();
  let consecutiveErrors = 0;
  const MAX_CONSECUTIVE_ERRORS = 5;

  while (Date.now() - startTime < POLL_TIMEOUT) {
    await sleep(POLL_INTERVAL);

    let res;
    try {
      res = await apiRequest("GET", `/generations/${generationId}`);
    } catch (err) {
      consecutiveErrors++;
      console.error(`  Poll network error (${consecutiveErrors}/${MAX_CONSECUTIVE_ERRORS}): ${err.message}`);
      if (consecutiveErrors >= MAX_CONSECUTIVE_ERRORS) {
        throw new Error(`Polling abandoned after ${MAX_CONSECUTIVE_ERRORS} consecutive network failures`);
      }
      continue;
    }

    consecutiveErrors = 0; // reset on successful request

    if (res.status !== 200) {
      console.error(`  Poll HTTP error (${res.status}):`, JSON.stringify(res.data));
      continue;
    }

    const { status, gammaUrl, exportUrl } = res.data;
    console.log(`  Status: ${status}`);

    if (status === "completed") {
      return { gammaUrl, exportUrl };
    }
    if (status === "failed") {
      throw new Error(`Generation failed: ${JSON.stringify(res.data)}`);
    }
  }

  throw new Error(`Generation timed out after ${POLL_TIMEOUT / 1000}s`);
}

// ─── Main ───────────────────────────────────────────────────────────────────

async function main() {
  const args = process.argv.slice(2);
  const dryRun = args.includes("--dry-run");
  const courseIdx = args.indexOf("--course");
  const singleSlug = courseIdx !== -1 ? args[courseIdx + 1] : null;
  const delayIdx = args.indexOf("--delay");
  const delay = delayIdx !== -1 ? parseInt(args[delayIdx + 1], 10) : 5000;

  const resume = args.includes("--resume");
  const force = args.includes("--force");

  if (!API_KEY) {
    console.error("Error: GAMMA_API_KEY environment variable not set");
    process.exit(1);
  }

  // Load existing results for resume and merge
  const resultsPath = path.join(__dirname, "..", "data", "gamma-sync-results.json");
  let existingResults = { results: [] };
  if (fs.existsSync(resultsPath)) {
    try {
      existingResults = JSON.parse(fs.readFileSync(resultsPath, "utf8"));
    } catch { /* start fresh */ }
  }
  const completedSlugs = new Set(
    existingResults.results
      .filter((r) => r.status === "completed")
      .map((r) => r.slug)
  );

  let courses = COURSES;
  if (singleSlug) {
    courses = COURSES.filter((c) => c.slug === singleSlug);
    if (courses.length === 0) {
      console.error(`No course found with slug: ${singleSlug}`);
      console.error("Available slugs:", COURSES.map((c) => c.slug).join(", "));
      process.exit(1);
    }
  }

  if (force) {
    console.log(`\n🔁 Force mode: regenerating ALL courses (ignoring previous completions)`);
  } else if (resume) {
    const before = courses.length;
    courses = courses.filter((c) => !completedSlugs.has(c.slug));
    console.log(`\n🔄 Resume mode: skipping ${before - courses.length} already-completed courses`);
  }

  const modeLabel = dryRun ? "DRY RUN" : "LIVE";
  const flagLabel = force ? " (FORCE)" : resume ? " (RESUME)" : "";
  console.log(`\n🎓 ImpactMojo Gamma Sync`);
  console.log(`   Courses: ${courses.length}`);
  console.log(`   Theme: ${THEME_ID}`);
  console.log(`   Folder: ${FOLDER_ID} (101 Decks)`);
  console.log(`   Mode: ${modeLabel}${flagLabel}\n`);

  const results = [];

  for (let i = 0; i < courses.length; i++) {
    const course = courses[i];
    console.log(`[${i + 1}/${courses.length}] ${course.title} (${course.slug})`);
    console.log(`   Category: ${course.category}`);

    const payload = buildPayload(course);

    if (dryRun) {
      console.log(`   Payload preview:`);
      console.log(`     textMode: ${payload.textMode}`);
      console.log(`     numCards: ${payload.numCards}`);
      console.log(`     theme: ${payload.themeId}`);
      console.log(`     imageStyle: ${payload.imageOptions.style.substring(0, 80)}...`);
      console.log(`     footer: ${JSON.stringify(HEADER_FOOTER.bottomCenter)} | ${JSON.stringify(HEADER_FOOTER.bottomRight)}`);
      console.log("");
      results.push({ slug: course.slug, status: "dry-run" });
      continue;
    }

    try {
      // Start generation
      const res = await apiRequest("POST", "/generations", payload);

      if (res.status !== 201 && res.status !== 200) {
        console.error(`   API error (${res.status}):`, JSON.stringify(res.data));
        results.push({ slug: course.slug, status: "error", error: res.data });
        continue;
      }

      const { generationId } = res.data;
      console.log(`   Generation started: ${generationId}`);

      // Poll for completion
      const { gammaUrl, exportUrl } = await pollGeneration(generationId);
      console.log(`   Done: ${gammaUrl}`);
      if (exportUrl) console.log(`   PDF: ${exportUrl}`);

      results.push({
        slug: course.slug,
        status: "completed",
        gammaUrl,
        exportUrl,
        generationId,
      });

      // Rate-limit delay between courses
      if (i < courses.length - 1) {
        console.log(`   Waiting ${delay / 1000}s before next...\n`);
        await sleep(delay);
      }
    } catch (err) {
      console.error(`   Failed: ${err.message}`);
      results.push({ slug: course.slug, status: "failed", error: err.message });
    }
  }

  // ─── Summary ────────────────────────────────────────────────────────────

  console.log("\n═══ Summary ═══");
  const completed = results.filter((r) => r.status === "completed");
  const failed = results.filter((r) => r.status === "failed" || r.status === "error");

  console.log(`Completed: ${completed.length}/${results.length}`);
  if (failed.length) {
    console.log(`Failed: ${failed.length}`);
    failed.forEach((f) => console.log(`  - ${f.slug}: ${f.error}`));
  }

  // Merge results into existing file (don't overwrite previous completions)
  if (!dryRun && results.length > 0) {
    const outputDir = path.dirname(resultsPath);
    if (!fs.existsSync(outputDir)) fs.mkdirSync(outputDir, { recursive: true });

    // Merge: update existing entries or add new ones
    for (const result of results) {
      const idx = existingResults.results.findIndex((r) => r.slug === result.slug);
      if (idx >= 0) {
        // Only overwrite if new result is completed, or old was not completed
        if (result.status === "completed" || existingResults.results[idx].status !== "completed") {
          existingResults.results[idx] = result;
        }
      } else {
        existingResults.results.push(result);
      }
    }

    existingResults.syncDate = new Date().toISOString();
    existingResults.theme = THEME_ID;

    fs.writeFileSync(resultsPath, JSON.stringify(existingResults, null, 2));

    const totalCompleted = existingResults.results.filter((r) => r.status === "completed").length;
    console.log(`\nResults merged to: ${resultsPath}`);
    console.log(`Total completed across all runs: ${totalCompleted}/${COURSES.length}`);
  }
}

main().catch((err) => {
  console.error("Fatal error:", err);
  process.exit(1);
});
