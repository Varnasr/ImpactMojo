/* Checks the LMS export's manifests and SCORM wrapper without a browser.
 *
 * The failure this exists to prevent is silent and remote: a manifest that is
 * malformed, or carries an identifier that is not a valid XML NCName, is
 * accepted by nothing and rejected by the LMS at import -- on an instructor's
 * machine, days later, with an error message that says nothing useful. Course
 * slugs like "101-csr-esg" start with a digit, which is exactly the case an
 * NCName forbids, so this is a live hazard rather than a theoretical one.
 */
import fs from 'node:fs';
import vm from 'node:vm';

const src = fs.readFileSync('js/lms-export.js', 'utf8');
const sandbox = { window: {}, location: { origin: 'https://www.impactmojo.in', href: 'https://www.impactmojo.in/' },
                  document: {}, fetch: () => Promise.reject(new Error('no network in test')),
                  DOMParser: function () {}, Blob: function () {}, URL, Date, console };
sandbox.self = sandbox;
vm.createContext(sandbox);
vm.runInContext(src, sandbox);
const X = sandbox.window.IMLmsExport;

let fails = 0;
const ok = (cond, msg) => { if (!cond) { console.log('  FAIL ' + msg); fails++; } };

// 1. NCName: must never start with a digit, must contain no illegal chars.
const NCNAME = /^[A-Za-z_][A-Za-z0-9._-]*$/;
for (const slug of ['101-csr-esg', 'mel', '2026-thing', 'a b/c', '---', 'çourse']) {
  const v = X._ncname(slug);
  ok(NCNAME.test(v), `ncname(${JSON.stringify(slug)}) -> ${JSON.stringify(v)} is not a valid NCName`);
}

// 2. Manifests must be well-formed XML, declare their schema, and use the NCName id.
const meta = { slug: '101-csr-esg', title: 'CSR & ESG 101 <yes> "quoted"', description: "It's fine & good",
               url: 'https://www.impactmojo.in/101-courses/csr-esg.html' };
const expectId = X._ncname(meta.slug);

for (const [name, fn, schema] of [
  ['scorm12', X._manifests.scorm12, '1.2'],
  ['scorm2004', X._manifests.scorm2004, '2004'],
  ['cc', X._manifests.cc, 'IMS Common Cartridge'],
]) {
  const xml = fn(meta);
  ok(xml.startsWith('<?xml'), `${name}: missing XML declaration`);
  ok(xml.includes(schema), `${name}: missing schema marker ${schema}`);
  ok(xml.includes(`identifier="${expectId}"`), `${name}: manifest id is not the NCName-safe id`);
  // Raw title contains & < > " ' -- none may survive unescaped into the XML.
  // Check for a bare ampersand that does not begin an entity; a bare '<' cannot
  // be told from real markup by regex, and the escape assertion below covers it.
  ok(!/&(?!amp;|lt;|gt;|quot;|apos;|#)/.test(xml), `${name}: bare ampersand in manifest`);
  ok(xml.includes('CSR &amp; ESG 101 &lt;yes&gt;'), `${name}: title not escaped as expected`);
  ok(xml.includes('href="index.html"'), `${name}: does not point at index.html`);
  // Balanced tags: every opening tag has a close (crude but catches truncation).
  const opens = (xml.match(/<manifest[\s>]/g) || []).length;
  const closes = (xml.match(/<\/manifest>/g) || []).length;
  ok(opens === 1 && closes === 1, `${name}: manifest element not balanced`);
}

// 3. SCORM wrapper: correct API name and verbs per version, and no syntax errors.
for (const [v, api, init] of [['1.2', 'window.API', 'LMSInitialize'], ['2004', 'API_1484_11', 'Initialize']]) {
  const w = X._wrapper(v);
  ok(w.includes(api.replace('window.', '')), `wrapper ${v}: wrong API global`);
  ok(w.includes(init), `wrapper ${v}: wrong init verb`);
  ok(w.includes('beforeunload'), `wrapper ${v}: never commits on unload`);
  try { new Function(w); } catch (e) { ok(false, `wrapper ${v}: syntax error — ${e.message}`); }
}
// 1.2 and 2004 use different completion keys; mixing them silently breaks reporting.
ok(X._wrapper('1.2').includes('cmi.core.lesson_status'), 'wrapper 1.2: wrong completion key');
ok(X._wrapper('2004').includes('cmi.completion_status'), 'wrapper 2004: wrong completion key');
ok(!X._wrapper('1.2').includes('cmi.completion_status'), 'wrapper 1.2: leaked a 2004 key');

// 4. Runtime behaviour against a mock LMS. The manifest being well-formed only
// gets the package accepted; this is the part that decides whether an instructor
// sees who finished. Completion must fire once, at the last slide -- not on open
// (everyone passes) and not on every navigation (a commit storm).
{
  const wrapper = X._wrapper('1.2');
  const calls = [];
  const API = {
    LMSInitialize: () => (calls.push(['init']), 'true'),
    LMSSetValue: (k, v) => (calls.push(['set', k, v]), 'true'),
    LMSCommit: () => (calls.push(['commit']), 'true'),
    LMSFinish: () => (calls.push(['finish']), 'true'),
  };
  let unload = null;
  const total = 5, deck = { cur: 0 };
  const win = {
    API, slides: new Array(total),
    get cur() { return deck.cur; },
    showSlide(n) { deck.cur = n; },
    addEventListener: (ev, fn) => { if (ev === 'beforeunload') unload = fn; },
  };
  win.parent = win;
  const ctx = { window: win, console };
  vm.createContext(ctx);
  vm.runInContext(wrapper, ctx);

  ok(calls.some(c => c[0] === 'init'), 'wrapper never called LMSInitialize');
  ok(calls.some(c => c[1] === 'cmi.core.lesson_status' && c[2] === 'incomplete'),
     'wrapper did not mark the course incomplete on open');

  win.showSlide(2);
  ok(!calls.some(c => c[2] === 'completed'), 'wrapper marked completed before the final slide');

  win.showSlide(total - 1);
  ok(calls.filter(c => c[2] === 'completed').length === 1,
     'wrapper did not report completed exactly once at the final slide');

  win.showSlide(total - 1);
  ok(calls.filter(c => c[2] === 'completed').length === 1,
     'wrapper re-reported completion on revisiting the last slide');

  if (unload) unload();
  ok(calls.some(c => c[0] === 'finish'), 'wrapper never called LMSFinish on unload');
}

console.log(fails ? `FAIL — ${fails} problem(s) in the LMS export` : 'PASS — LMS export manifests and SCORM wrapper are well-formed.');
process.exit(fails ? 1 : 0);
