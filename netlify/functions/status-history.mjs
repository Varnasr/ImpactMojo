/**
 * Netlify Function — Status History reader
 *
 * Serves the cross-visitor status history that status-probe.mjs writes to the
 * "status" Netlify Blobs store, so /status.html can render a TRUE 90-day uptime
 * view aggregated across all visitors (not just the viewer's localStorage).
 *
 * GET /api/status-history  ->  { updatedAt, days: {YYYY-MM-DD: {overall, components}}, components: {...} }
 *
 * Returns an empty payload (200) until the scheduled probe has run at least
 * once, so the page can fall back to its local history without erroring.
 */
export default async () => {
  const headers = {
    "Content-Type": "application/json",
    "Access-Control-Allow-Origin": "*",
    "Cache-Control": "public, max-age=60, must-revalidate",
  };
  try {
    const { getStore } = await import("@netlify/blobs");
    const store = getStore("status");
    const [history, state] = await Promise.all([
      store.get("history", { type: "json" }),
      store.get("state", { type: "json" }),
    ]);
    return new Response(JSON.stringify({
      updatedAt: state?.updatedAt || null,
      days: history || {},
      components: state?.components || {},
    }), { headers });
  } catch (e) {
    return new Response(JSON.stringify({ updatedAt: null, days: {}, components: {}, error: e.message }), { headers });
  }
};

export const config = { path: "/api/status-history" };
