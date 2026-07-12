/**
 * ImpactMojo — GA4 → Supabase bridge (Google Apps Script)
 * =======================================================
 *
 * Pulls GA4 numbers daily under YOUR Google login (no service-account key, so it
 * works even when the org disables downloadable keys) and pushes them to
 * impactmojo.in/api/ga4-ingest, which stores a snapshot the admin dashboard reads.
 * Result: the admin Analytics tab shows data with no per-admin sign-in.
 *
 * ONE-TIME SETUP (~2 min):
 *   1. Go to https://script.google.com → New project. Delete the sample code and
 *      paste this whole file.
 *   2. Left sidebar → Services (the + next to "Services") → find
 *      "Google Analytics Data API" → Add. (Its identifier must be AnalyticsData.)
 *   3. Put your ingest token in INGEST_TOKEN below (Claude will give it to you).
 *   4. Select pushGA4Snapshot in the function dropdown → Run. Authorize when
 *      prompted (your own Google account). Check the Execution log ends in "200".
 *   5. Left sidebar → Triggers (clock icon) → Add Trigger →
 *      function: pushGA4Snapshot, event source: Time-driven, type: Day timer.
 *      Save. Done — it now refreshes daily.
 */

var PROPERTY_ID  = '514001382';
var INGEST_URL   = 'https://www.impactmojo.in/api/ga4-ingest';
var INGEST_TOKEN = 'PASTE_YOUR_TOKEN_HERE';   // <-- replace with the token Claude gives you

function pushGA4Snapshot() {
  var range = [{ startDate: '30daysAgo', endDate: 'today' }];

  var overview = AnalyticsData.Properties.runReport({
    dateRanges: range,
    metrics: [
      { name: 'totalUsers' }, { name: 'newUsers' }, { name: 'sessions' },
      { name: 'screenPageViews' }, { name: 'averageSessionDuration' },
      { name: 'bounceRate' }, { name: 'engagedSessions' }
    ]
  }, 'properties/' + PROPERTY_ID);

  var geo = AnalyticsData.Properties.runReport({
    dateRanges: range,
    dimensions: [{ name: 'country' }],
    metrics: [{ name: 'totalUsers' }, { name: 'sessions' }],
    orderBys: [{ metric: { metricName: 'totalUsers' }, desc: true }],
    limit: 30
  }, 'properties/' + PROPERTY_ID);

  var names = ['Total Users', 'New Users', 'Sessions', 'Pageviews',
               'Avg Session Duration', 'Bounce Rate', 'Engaged Sessions'];
  var ov = {};
  if (overview.rows && overview.rows[0]) {
    overview.rows[0].metricValues.forEach(function (v, i) { ov[names[i]] = parseFloat(v.value); });
  }
  var geography = (geo.rows || []).map(function (r) {
    return {
      country: r.dimensionValues[0].value,
      users: parseFloat(r.metricValues[0].value),
      sessions: parseFloat(r.metricValues[1].value)
    };
  });

  var resp = UrlFetchApp.fetch(INGEST_URL, {
    method: 'post',
    contentType: 'application/json',
    headers: { Authorization: 'Bearer ' + INGEST_TOKEN },
    payload: JSON.stringify({ overview: ov, geography: geography }),
    muteHttpExceptions: true
  });
  Logger.log(resp.getResponseCode() + ' ' + resp.getContentText());
}
