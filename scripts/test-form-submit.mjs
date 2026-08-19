/**
 * Contract test for js/form-submit.js.
 *
 * Guards the bug this helper exists to prevent: `fetch()` resolves on 404 and
 * 500, so every handler that did `.then(showSuccess).catch(showError)` reported
 * a rejected submission as received. These assertions fail if that behaviour
 * ever comes back.
 *
 * Run: node scripts/test-form-submit.mjs
 */
import fs from 'node:fs';
const src = fs.readFileSync(new URL('../js/form-submit.js', import.meta.url), 'utf8');

function makeEnv(fetchImpl) {
  const store = {};
  const win = { localStorage: { getItem:k=>store[k]||null, setItem:(k,v)=>store[k]=v }, fetch: fetchImpl };
  global.window = win; global.localStorage = win.localStorage; global.fetch = fetchImpl;
  global.FormData = class { constructor(){this.m=new Map();} append(k,v){this.m.set(k,v);} get(k){return this.m.get(k);} forEach(f){this.m.forEach((v,k)=>f(v,k));} };
  global.URLSearchParams = class { constructor(fd){this.fd=fd;} toString(){let p=[];this.fd.forEach((v,k)=>p.push(k+'='+encodeURIComponent(v)));return p.join('&');} };
  global.File = class {};
  eval(src);
  return win;
}
function fd(win){ const f = new global.FormData(); f.append('form-name','test'); f.append('email','a@b.co'); return f; }

let pass=0, fail=0;
const check=(n,c)=>{ c?(pass++,console.log('  PASS',n)):(fail++,console.log('  FAIL',n)); };

// 200
let w = makeEnv(async()=>({ok:true,status:200}));
try { await w.imxSubmitForm(fd(w)); check('200 resolves', true); } catch(e){ check('200 resolves', false); }

// 404 -> must reject, no retry
let calls=0;
w = makeEnv(async()=>{calls++;return {ok:false,status:404};});
try { await w.imxSubmitForm(fd(w)); check('404 rejects', false); }
catch(e){ check('404 rejects with status', e.status===404); check('404 does not retry', calls===1); }

// 500 -> rejects after one retry
calls=0;
w = makeEnv(async()=>{calls++;return {ok:false,status:500};});
try { await w.imxSubmitForm(fd(w)); check('500 rejects', false); }
catch(e){ check('500 rejects', e.status===500); check('500 retried once (2 calls)', calls===2); }

// network error -> retries then rejects, and queues
calls=0;
w = makeEnv(async()=>{calls++;throw new Error('offline');});
try { await w.imxSubmitForm(fd(w)); check('network rejects', false); }
catch(e){ check('network rejects', true); check('network retried once', calls===2); }
check('failure was queued', w.imxFailedSubmissions().length===1);
check('queued entry keeps the text', w.imxFailedSubmissions()[0].data.email==='a@b.co');

// multipart chosen when a File is present
let usedMultipart=null;
w = makeEnv(async(url,opts)=>{ usedMultipart = !opts.headers; return {ok:true,status:200}; });
const f2 = new global.FormData(); f2.append('form-name','t'); const file=new global.File(); file.size=10; f2.append('doc',file);
await w.imxSubmitForm(f2);
check('file present -> multipart (no urlencoded header)', usedMultipart===true);

// --- dual path: Netlify + /api/form-submit ---
// Either landing counts as delivered; only a double failure is a real loss.
async function dual(netlifyStatus, apiStatus) {
  let seen = [];
  const w = makeEnv(async (url, opts) => {
    const isApi = String(url).includes('/api/form-submit');
    seen.push(isApi ? 'api' : 'netlify');
    const st = isApi ? apiStatus : netlifyStatus;
    if (st === 0) throw new Error('offline');
    return { ok: st >= 200 && st < 300, status: st };
  });
  const f = new global.FormData();
  f.append('form-name', 'event-registration');
  f.append('email', 'a@b.co');
  let ok = true;
  try { await w.imxSubmitBoth(f); } catch (e) { ok = false; }
  return { ok, seen };
}

let d = await dual(200, 200);
check('dual: both OK -> delivered', d.ok);
check('dual: both endpoints hit', d.seen.includes('api') && d.seen.includes('netlify'));

d = await dual(404, 200);
check('dual: netlify rejects, durable OK -> delivered', d.ok);

d = await dual(200, 500);
check('dual: durable fails, netlify OK -> delivered', d.ok);

d = await dual(500, 500);
check('dual: both fail -> rejected', !d.ok);

console.log(`\n${pass} passed, ${fail} failed`);
console.log(fail ? 'FAIL - form-submit contract broken' : 'PASS - form-submit rejects non-2xx, retries 5xx only, and queues failures');
process.exit(fail?1:0);
