// Netlify Edge Function: proxy a GitHub-Pages-hosted external page so
// it appears at /devdiscourses on impactmojo.in. Injects a <base> tag
// so the page's relative asset URLs (css/, js/) resolve correctly under
// the proxied base path — fixing the "blank/unstyled page" problem you
// can't solve with _redirects alone (Netlify normalises trailing slashes
// when matching, so the no-slash form silently serves the page with
// broken relative paths).
//
// Routes (self-registered via the exported config below):
//   /devdiscourses        → varnasr.github.io/development-discourses/
//   /devdiscourses/       → varnasr.github.io/development-discourses/
//   /devdiscourses/*      → varnasr.github.io/development-discourses/<splat>

import type { Context } from "https://edge.netlify.com";

const UPSTREAM = "https://varnasr.github.io/development-discourses";
const BASE_PATH = "/devdiscourses/";

export default async (request: Request, context: Context) => {
    const url = new URL(request.url);
    let path = url.pathname;

    // Strip our base prefix to find the upstream path.
    if (path === "/devdiscourses" || path === "/devdiscourses/") {
        path = "/";
    } else if (path.startsWith("/devdiscourses/")) {
        path = path.slice("/devdiscourses".length); // keeps leading slash
    } else {
        return context.next();
    }

    const upstreamUrl = UPSTREAM + path + url.search;
    const upstream = await fetch(upstreamUrl, {
        headers: { "User-Agent": "ImpactMojo/devdiscourses-proxy" },
        redirect: "follow",
    });

    const ct = upstream.headers.get("content-type") || "";
    // Pass through everything except HTML unchanged.
    if (!ct.includes("text/html")) {
        const headers = new Headers(upstream.headers);
        headers.delete("content-security-policy");
        headers.delete("x-frame-options");
        return new Response(upstream.body, { status: upstream.status, headers });
    }

    // HTML: inject <base> so relative asset paths resolve against /devdiscourses/.
    let body = await upstream.text();
    if (!/<base\s/i.test(body)) {
        body = body.replace(/<head([^>]*)>/i, `<head$1><base href="${BASE_PATH}">`);
    }
    const headers = new Headers(upstream.headers);
    headers.set("content-type", "text/html; charset=utf-8");
    headers.delete("content-length");
    headers.delete("content-security-policy");
    headers.delete("x-frame-options");
    return new Response(body, { status: upstream.status, headers });
};

export const config = { path: ["/devdiscourses", "/devdiscourses/*"] };
