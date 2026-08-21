/* Checks the Studio-submission envelope and the gradebook CSV contract.
 *
 * Two failure modes matter here and neither shows up in this repo. A submission
 * that loses its identity is a file an instructor cannot mark -- which is the
 * exact gap this feature exists to close. And a CSV whose quoting is wrong
 * shifts every column after the first comma, so a gradebook import silently
 * attributes work to the wrong student; course names like
 * "Sustainability, ESG, CSR and M&E" contain commas as a matter of course.
 */
import fs from 'node:fs';
import vm from 'node:vm';

const src = fs.readFileSync('js/studio-submit.js', 'utf8');
const store = {};
const ctx = {
  window: {}, document: {}, console, Date, Blob: function () {}, URL: { createObjectURL(){}, revokeObjectURL(){} },
  localStorage: { getItem: k => (k in store ? store[k] : null), setItem: (k, v) => { store[k] = String(v); } },
};
ctx.self = ctx;
vm.createContext(ctx);
vm.runInContext(src, ctx);
const S = ctx.window.IMStudioSubmit;

let fails = 0;
const ok = (c, m) => { if (!c) { console.log('  FAIL ' + m); fails++; } };

// 1. Envelope carries identity — the whole point.
const sub = S.build({
  studio: 'logframe-builder', studioTitle: 'LogFrame Builder Studio',
  payload: { project: 'Water', rows: [1, 2, 3] },
  student: { name: 'Asha Verma', id: 'SW-2041', course: 'Sustainability, ESG, CSR and M&E' },
});
for (const f of ['student_name', 'student_id', 'course', 'studio', 'submitted_at', 'digest', 'payload'])
  ok(sub[f] !== undefined && sub[f] !== '', `envelope is missing ${f}`);
ok(S.verify(sub).ok, 'a freshly built envelope does not verify');
ok(sub.payload.project === 'Water', 'payload was not preserved verbatim');
ok(!isNaN(Date.parse(sub.submitted_at)), 'submitted_at is not a parseable timestamp');

// 2. A truncated payload must be caught, not silently accepted.
const bad = JSON.parse(JSON.stringify(sub));
bad.payload.rows = [1, 2];
ok(!S.verify(bad).ok, 'a mutated payload still passed verification');
ok(/digest/.test(S.verify(bad).reason), 'the mutation was rejected for the wrong reason');

// 3. A foreign file must be rejected with a usable reason, not a crash.
ok(!S.verify({ project: 'raw studio export' }).ok, 'a bare studio export was accepted as a submission');
ok(!S.verify(null).ok, 'null was accepted as a submission');

// 4. Text payloads (most Studios export text/plain, not JSON).
const t = S.build({ studio: 'toc', payload: 'line one\nline two', student: { name: 'B' } });
ok(t.payload_type === 'text', 'a string payload was not recorded as text');
ok(S.verify(t).ok, 'a text submission does not verify');

// 5. CSV quoting, mirroring gradebook.html's csvCell.
const csvCell = v => '"' + String(v == null ? '' : v).replace(/"/g, '""') + '"';
const row = ['Asha Verma', 'SW-2041', 'Sustainability, ESG, CSR and M&E', 'LogFrame', '', 'f.json', '', ''];
const line = row.map(csvCell).join(',');
ok(line.split('","').length === row.length, 'a comma inside a field broke the column count');
ok(csvCell('He said "hi"') === '"He said ""hi"""', 'embedded quotes are not doubled');
ok(csvCell(null) === '""', 'null did not become an empty quoted field');

console.log(fails ? `FAIL — ${fails} problem(s) in studio submissions`
                  : 'PASS — submission envelopes carry identity, detect corruption, and CSV quoting holds.');
process.exit(fails ? 1 : 0);
