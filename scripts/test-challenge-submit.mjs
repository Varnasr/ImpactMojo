/**
 * Contract test for netlify/functions/challenge-submit.mjs.
 *
 * This endpoint holds the service-role key, so its validation gate is the only
 * thing between the public internet and a privileged write. These assertions
 * cover what it must reject, and that a Supabase failure surfaces as a 502
 * rather than a silent success -- the failure mode that hid the original bug.
 *
 * Run: node scripts/test-challenge-submit.mjs
 */
process.env.SUPABASE_SERVICE_ROLE_KEY = 'test-key';
const { default: h } = await import(new URL('../netlify/functions/challenge-submit.mjs', import.meta.url));

let calls = [];
global.fetch = async (u, o) => { calls.push({ u, o }); return { ok: true, status: 201, json: async () => [{ id: 'row-1' }] }; };
const post = (b) => h(new Request('http://x/api/challenge-submit', { method: 'POST', body: JSON.stringify(b) }));
const long = 'x'.repeat(250);

let pass = 0, fail = 0;
const ck = (n, c) => { c ? (pass++, console.log('  PASS ' + n)) : (fail++, console.log('  FAIL ' + n)); };

ck('GET rejected', (await h(new Request('http://x', { method: 'GET' }))).status === 405);
ck('malformed json rejected', (await h(new Request('http://x', { method: 'POST', body: '{oops' }))).status === 400);
ck('missing challenge_id rejected', (await post({ submission_text: long, email: 'a@b.co' })).status === 400);
ck('under 200 chars rejected', (await post({ challenge_id: 'c', submission_text: 'short', email: 'a@b.co' })).status === 400);
ck('over 60k rejected', (await post({ challenge_id: 'c', submission_text: 'x'.repeat(60001), email: 'a@b.co' })).status === 400);
ck('anonymous without email rejected', (await post({ challenge_id: 'c', submission_text: long })).status === 400);
ck('anonymous with malformed email rejected', (await post({ challenge_id: 'c', submission_text: long, email: 'nope' })).status === 400);

calls = [];
ck('valid anonymous accepted', (await post({ challenge_id: 'c', submission_text: long, email: 'a@b.co' })).status === 200);
ck('anonymous insert does not upsert', calls[0] && !calls[0].u.includes('on_conflict'));

calls = [];
ck('signed-in without email accepted', (await post({ challenge_id: 'c', submission_text: long, user_id: 'u-1' })).status === 200);
ck('signed-in resubmission upserts', calls[0] && calls[0].u.includes('on_conflict=challenge_id,user_id'));

global.fetch = async () => ({ ok: false, status: 400, text: async () => 'boom' });
ck('supabase failure surfaces as 502', (await post({ challenge_id: 'c', submission_text: long, email: 'a@b.co' })).status === 502);

console.log('\n' + pass + ' passed, ' + fail + ' failed');
console.log(fail ? 'FAIL - challenge-submit contract broken' : 'PASS - challenge-submit validates before any privileged write');
process.exit(fail ? 1 : 0);
