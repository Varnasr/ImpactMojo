/**
 * Contract test for netlify/functions/form-submit.mjs.
 *
 * The endpoint holds the service-role key and writes to a table anon cannot
 * touch, so its allowlist and size caps are the whole security boundary.
 *
 * Run: node scripts/test-form-submit-endpoint.mjs
 */
process.env.SUPABASE_SERVICE_ROLE_KEY = 'test-key';
const { default: h } = await import(new URL('../netlify/functions/form-submit.mjs', import.meta.url));

let calls = [];
global.fetch = async (u, o) => { calls.push({ u, o: JSON.parse(o.body) }); return { ok: true, status: 201, json: async () => [{ id: 'r1' }] }; };
const post = (b) => h(new Request('http://x/api/form-submit', { method: 'POST', body: JSON.stringify(b) }));

let pass = 0, fail = 0;
const ck = (n, c) => { c ? (pass++, console.log('  PASS ' + n)) : (fail++, console.log('  FAIL ' + n)); };

ck('GET rejected', (await h(new Request('http://x', { method: 'GET' }))).status === 405);
ck('malformed json rejected', (await h(new Request('http://x', { method: 'POST', body: '{oops' }))).status === 400);
ck('unknown form rejected', (await post({ form_name: 'not-a-form', data: { a: 'b' } })).status === 400);
ck('missing data rejected', (await post({ form_name: 'event-registration' })).status === 400);
ck('empty data rejected', (await post({ form_name: 'event-registration', data: {} })).status === 400);
ck('too many fields rejected',
   (await post({ form_name: 'contact', data: Object.fromEntries(Array.from({length:50},(_,i)=>['k'+i,'v'])) })).status === 400);
ck('oversized payload rejected',
   (await post({ form_name: 'contact', data: { a: 'x'.repeat(19000), b: 'y'.repeat(19000), c: 'z'.repeat(19000),
                                               d: 'w'.repeat(19000), e: 'v'.repeat(19000), f: 'u'.repeat(19000) } })).status === 413);

calls = [];
let r = await post({ form_name: 'event-registration', data: { name: 'Dr Apoorva', email: 'a@gnlu.ac.in', event_title: 'Dev econ', 'form-name': 'x', 'bot-field': '' } });
ck('valid event registration accepted', r.status === 200);
ck('email lifted to its own column', calls[0] && calls[0].o.email === 'a@gnlu.ac.in');
ck('form-name stripped from payload', calls[0] && !('form-name' in calls[0].o.data));
ck('bot-field stripped from payload', calls[0] && !('bot-field' in calls[0].o.data));
ck('form_name recorded', calls[0] && calls[0].o.form_name === 'event-registration');

calls = [];
r = await post({ form_name: 'contact', data: { name: 'bot', email: 'b@c.co', 'bot-field': 'filled' } });
ck('honeypot returns 200 (learns nothing)', r.status === 200);
ck('honeypot writes nothing', calls.length === 0);

calls = [];
r = await post({ form_name: 'contact', data: { name: 'x', email: 'not-an-email' } });
ck('malformed email stored as null, not rejected', r.status === 200 && calls[0].o.email === null);

global.fetch = async () => ({ ok: false, status: 400, text: async () => 'boom' });
ck('supabase failure surfaces as 502', (await post({ form_name: 'contact', data: { a: 'b' } })).status === 502);

console.log('\n' + pass + ' passed, ' + fail + ' failed');
console.log(fail ? 'FAIL - form-submit endpoint contract broken' : 'PASS - form-submit endpoint enforces its allowlist and caps');
process.exit(fail ? 1 : 0);
