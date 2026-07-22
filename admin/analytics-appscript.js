/**
 * ImpactMojo Analytics Reconciliation — Google Apps Script
 * ========================================================
 *
 * This script connects to Google Analytics 4 (GA4) and reconciles
 * current live data with legacy metrics reconstructed from the website.
 *
 * SETUP INSTRUCTIONS:
 * 1. Create a new Google Sheet
 * 2. Open Extensions > Apps Script
 * 3. Paste this entire script
 * 4. Update the CONFIG section below with your GA4 property ID
 * 5. Enable the Google Analytics Data API:
 *    - In Apps Script, click + next to "Services"
 *    - Add "Google Analytics Data API" (AnalyticsData)
 * 6. Run setupSheetStructure() first to create all tabs
 * 7. Run populateLegacyData() to load historical metrics
 * 8. Run pullGA4Data() to fetch current analytics
 * 9. Set up a daily trigger: Run > Triggers > Add > pullGA4Data > Daily
 *
 * GA4 PROPERTY SETUP:
 * - Your GA4 Measurement ID is G-JRCMEB9TBW
 * - You need the numeric Property ID from GA4 Admin > Property Settings
 */

// ============================================================
// CONFIG — Update these values
// ============================================================
var CONFIG = {
  GA4_PROPERTY_ID: 'YOUR_GA4_PROPERTY_ID',  // Numeric ID, e.g., '123456789'
  LEGACY_TRANSITION_DATE: '2025-06-01',       // Approximate date you switched GA accounts
  SITE_LAUNCH_DATE: '2024-01-01',             // Approximate ImpactMojo launch date
  TIMEZONE: 'Asia/Kolkata'
};

// ============================================================
// SHEET SETUP
// ============================================================

/**
 * Creates all required tabs with headers. Run this once.
 */
function setupSheetStructure() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();

  // Tab 1: Legacy Metrics
  var legacy = getOrCreateSheet(ss, 'Legacy Metrics');
  legacy.getRange('A1:F1').setValues([['Category', 'Metric Name', 'Value', 'Source Page', 'As Of Date', 'Notes']]);
  legacy.getRange('A1:F1').setFontWeight('bold').setBackground('#1E293B').setFontColor('#F1F5F9');
  legacy.setColumnWidth(1, 160);
  legacy.setColumnWidth(2, 280);
  legacy.setColumnWidth(3, 120);
  legacy.setColumnWidth(4, 200);
  legacy.setColumnWidth(5, 120);
  legacy.setColumnWidth(6, 250);

  // Tab 2: GA4 Live Data
  var ga4 = getOrCreateSheet(ss, 'GA4 Live Data');
  ga4.getRange('A1:H1').setValues([['Date Pulled', 'Metric', 'Value', 'Dimension', 'Dimension Value', 'Period', 'Start Date', 'End Date']]);
  ga4.getRange('A1:H1').setFontWeight('bold').setBackground('#0EA5E9').setFontColor('#FFFFFF');

  // Tab 3: Reconciled Dashboard
  var reconciled = getOrCreateSheet(ss, 'Reconciled Dashboard');
  reconciled.getRange('A1:G1').setValues([['Metric', 'Legacy Value', 'Legacy Period', 'Current GA4 Value', 'GA4 Period', 'Combined Total', 'Trend']]);
  reconciled.getRange('A1:G1').setFontWeight('bold').setBackground('#6366F1').setFontColor('#FFFFFF');

  // Tab 4: Feature Adoption
  var features = getOrCreateSheet(ss, 'Feature Adoption');
  features.getRange('A1:F1').setValues([['Feature', 'Type', 'Legacy Users', 'Current Users (GA4)', 'Total Users', 'Status']]);
  features.getRange('A1:F1').setFontWeight('bold').setBackground('#10B981').setFontColor('#FFFFFF');

  // Tab 5: Content Performance
  var content = getOrCreateSheet(ss, 'Content Performance');
  content.getRange('A1:H1').setValues([['Page Path', 'Page Title', 'Legacy Pageviews', 'GA4 Pageviews (30d)', 'GA4 Avg Duration', 'GA4 Bounce Rate', 'Total Pageviews', 'Notes']]);
  content.getRange('A1:H1').setFontWeight('bold').setBackground('#F59E0B').setFontColor('#1E293B');

  // Tab 6: Geography
  var geo = getOrCreateSheet(ss, 'Geography');
  geo.getRange('A1:E1').setValues([['Country', 'GA4 Users (30d)', 'GA4 Sessions (30d)', 'GA4 Pageviews (30d)', 'Last Updated']]);
  geo.getRange('A1:E1').setFontWeight('bold').setBackground('#EF4444').setFontColor('#FFFFFF');

  // Tab 7: Monthly Snapshots
  var monthly = getOrCreateSheet(ss, 'Monthly Snapshots');
  monthly.getRange('A1:G1').setValues([['Month', 'Total Users', 'New Users', 'Sessions', 'Pageviews', 'Avg Session Duration', 'Source']]);
  monthly.getRange('A1:G1').setFontWeight('bold').setBackground('#334155').setFontColor('#F1F5F9');

  SpreadsheetApp.flush();
  SpreadsheetApp.getUi().alert('Sheet structure created successfully. Now run populateLegacyData().');
}

function getOrCreateSheet(ss, name) {
  var sheet = ss.getSheetByName(name);
  if (!sheet) {
    sheet = ss.insertSheet(name);
  } else {
    // Clear existing data below headers
    if (sheet.getLastRow() > 1) {
      sheet.getRange(2, 1, sheet.getLastRow() - 1, sheet.getLastColumn()).clearContent();
    }
  }
  return sheet;
}

// ============================================================
// LEGACY DATA — Reconstructed from ImpactMojo website
// ============================================================

/**
 * Populates the Legacy Metrics tab with data extracted from the website.
 * Run this once, then manually adjust if needed.
 */
function populateLegacyData() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var legacy = ss.getSheetByName('Legacy Metrics');
  var features = ss.getSheetByName('Feature Adoption');
  var content = ss.getSheetByName('Content Performance');

  // ---- Platform Overview ----
  var platformMetrics = [
    ['Platform', 'Flagship Courses', 7, 'catalog.html', CONFIG.LEGACY_TRANSITION_DATE, 'Major structured courses with full curriculum'],
    ['Platform', 'Total Free Courses', 39, 'catalog.html', CONFIG.LEGACY_TRANSITION_DATE, 'All free course offerings including 101-level'],
    ['Platform', 'Interactive Labs', 10, 'catalog.html', CONFIG.LEGACY_TRANSITION_DATE, 'Hands-on simulation labs'],
    ['Platform', 'Educational Games', 12, 'catalog.html', CONFIG.LEGACY_TRANSITION_DATE, 'Economics and development games'],
    ['Platform', 'Premium Tools', 7, 'catalog.html', CONFIG.LEGACY_TRANSITION_DATE, 'Paid tier tools and resources'],
    ['Platform', 'Live Case Challenges', 9, 'challenges.html', CONFIG.LEGACY_TRANSITION_DATE, 'Real-world case challenges'],
    ['Platform', 'Learning Tracks', 6, 'challenges.html', CONFIG.LEGACY_TRANSITION_DATE, 'Challenge difficulty tracks'],
    ['Content', 'ImpactLex Terms', 500, 'index.html', CONFIG.LEGACY_TRANSITION_DATE, '500+ development terms'],
    ['Content', 'Open-Access Papers & Books', 500, 'index.html', CONFIG.LEGACY_TRANSITION_DATE, '500+ curated papers'],
    ['Content', 'Case Studies', 200, 'premium.html', CONFIG.LEGACY_TRANSITION_DATE, 'Covering 117 countries'],
    ['Content', 'Countries in Case Studies', 117, 'premium.html', CONFIG.LEGACY_TRANSITION_DATE, ''],
    ['Content', 'Dataset Generators', 36, 'index.html', CONFIG.LEGACY_TRANSITION_DATE, '840k+ rows of realistic data'],
    ['Content', 'Dataset Rows Generated', 840000, 'index.html', CONFIG.LEGACY_TRANSITION_DATE, 'LSMS, RCT, DHS and more'],
    ['Content', 'Chart Types (Viz Cookbook)', 14, 'index.html', CONFIG.LEGACY_TRANSITION_DATE, ''],
    ['Content', 'Interactive Shiny Apps', 11, 'index.html', CONFIG.LEGACY_TRANSITION_DATE, 'DevEconomics visualizations'],
    ['Content', 'VaniScribe Languages', 10, 'premium.html', CONFIG.LEGACY_TRANSITION_DATE, 'AI transcription languages'],
    ['Content', 'Handouts', 200, 'handouts.html', CONFIG.LEGACY_TRANSITION_DATE, 'Downloadable reference materials'],
    ['Content', 'Dataverse Tools', 215, 'dataverse.html', CONFIG.LEGACY_TRANSITION_DATE, 'Curated tools, datasets, APIs'],
  ];

  // ---- Course User Counts (from catalog_data.json) ----
  var courseUsers = [
    ['Course Users', 'Development Economics', 3600, 'catalog_data.json', CONFIG.LEGACY_TRANSITION_DATE, 'Flagship course'],
    ['Course Users', 'Economics 101: A Policy Primer', 3500, 'catalog_data.json', CONFIG.LEGACY_TRANSITION_DATE, ''],
    ['Course Users', 'Climate Essentials', 3400, 'catalog_data.json', CONFIG.LEGACY_TRANSITION_DATE, ''],
    ['Course Users', 'Political Economy', 3400, 'catalog_data.json', CONFIG.LEGACY_TRANSITION_DATE, ''],
    ['Course Users', 'Data Literacy for Development', 3400, 'catalog_data.json', CONFIG.LEGACY_TRANSITION_DATE, ''],
    ['Course Users', 'Public Health 101', 3300, 'catalog_data.json', CONFIG.LEGACY_TRANSITION_DATE, ''],
    ['Course Users', 'MEL Fundamentals', 3300, 'catalog_data.json', CONFIG.LEGACY_TRANSITION_DATE, ''],
    ['Course Users', 'English for Development', 3200, 'catalog_data.json', CONFIG.LEGACY_TRANSITION_DATE, ''],
    ['Course Users', 'Community-Led Development', 3200, 'catalog_data.json', CONFIG.LEGACY_TRANSITION_DATE, ''],
    ['Course Users', 'Poverty and Inequality', 3200, 'catalog_data.json', CONFIG.LEGACY_TRANSITION_DATE, ''],
    ['Course Users', 'Social Emotional Learning', 3200, 'catalog_data.json', CONFIG.LEGACY_TRANSITION_DATE, ''],
    ['Course Users', 'Education and Pedagogy', 3100, 'catalog_data.json', CONFIG.LEGACY_TRANSITION_DATE, ''],
    ['Course Users', 'Fundraising Fundamentals', 3100, 'catalog_data.json', CONFIG.LEGACY_TRANSITION_DATE, ''],
    ['Course Users', 'Livelihoods Fundamentals', 3100, 'catalog_data.json', CONFIG.LEGACY_TRANSITION_DATE, ''],
    ['Course Users', 'Digital Development Ethics', 3100, 'catalog_data.json', CONFIG.LEGACY_TRANSITION_DATE, ''],
    ['Course Users', 'Data Feminism', 3000, 'catalog_data.json', CONFIG.LEGACY_TRANSITION_DATE, ''],
    ['Course Users', 'Gender Studies 101', 3000, 'catalog_data.json', CONFIG.LEGACY_TRANSITION_DATE, ''],
    ['Course Users', 'Advocacy Fundamentals', 3000, 'catalog_data.json', CONFIG.LEGACY_TRANSITION_DATE, ''],
    ['Course Users', 'Marginalized Identities', 3000, 'catalog_data.json', CONFIG.LEGACY_TRANSITION_DATE, ''],
    ['Course Users', 'Decolonizing Development', 3000, 'catalog_data.json', CONFIG.LEGACY_TRANSITION_DATE, ''],
    ['Course Users', 'Observation to Insight', 2900, 'catalog_data.json', CONFIG.LEGACY_TRANSITION_DATE, ''],
    ['Course Users', 'Environmental Justice', 2900, 'catalog_data.json', CONFIG.LEGACY_TRANSITION_DATE, ''],
    ['Course Users', 'Global Dev Architecture', 2900, 'catalog_data.json', CONFIG.LEGACY_TRANSITION_DATE, ''],
    ['Course Users', 'Womens Economic Empowerment', 2900, 'catalog_data.json', CONFIG.LEGACY_TRANSITION_DATE, ''],
    ['Course Users', 'Multivariate Analysis', 2900, 'catalog_data.json', CONFIG.LEGACY_TRANSITION_DATE, ''],
    ['Course Users', 'Indian Constitution', 2800, 'catalog_data.json', CONFIG.LEGACY_TRANSITION_DATE, ''],
    ['Course Users', 'Sexual Rights and Health', 2800, 'catalog_data.json', CONFIG.LEGACY_TRANSITION_DATE, ''],
    ['Course Users', 'Post-Truth Politics', 2800, 'catalog_data.json', CONFIG.LEGACY_TRANSITION_DATE, ''],
    ['Course Users', 'BCC and Communications', 2800, 'catalog_data.json', CONFIG.LEGACY_TRANSITION_DATE, ''],
    ['Course Users', 'Research Ethics', 2700, 'catalog_data.json', CONFIG.LEGACY_TRANSITION_DATE, ''],
    ['Course Users', 'Care Economy', 2700, 'catalog_data.json', CONFIG.LEGACY_TRANSITION_DATE, ''],
    ['Course Users', 'Visual Ethnography', 2600, 'catalog_data.json', CONFIG.LEGACY_TRANSITION_DATE, ''],
    ['Course Users', 'IRT and Assessment', 2600, 'catalog_data.json', CONFIG.LEGACY_TRANSITION_DATE, ''],
    ['Course Users', 'Econometrics 101', 3500, 'catalog_data.json', CONFIG.LEGACY_TRANSITION_DATE, ''],
    ['Course Users', 'Qualitative Research Methods', 3500, 'catalog_data.json', CONFIG.LEGACY_TRANSITION_DATE, ''],
    ['Course Users', 'Decent Work for All', 3000, 'catalog_data.json', CONFIG.LEGACY_TRANSITION_DATE, ''],
    ['Course Users', 'EDA for Impact Data', 3000, 'catalog_data.json', CONFIG.LEGACY_TRANSITION_DATE, ''],
    ['Course Users', 'Bivariate Analysis', 3000, 'catalog_data.json', CONFIG.LEGACY_TRANSITION_DATE, ''],
    ['Course Users', 'Cost Effectiveness 101', 2100, 'catalog_data.json', CONFIG.LEGACY_TRANSITION_DATE, 'Newer course'],
    ['Course Users', 'Media for Development', 1200, 'catalog_data.json', CONFIG.LEGACY_TRANSITION_DATE, 'Flagship course'],
  ];

  // ---- Game User Counts ----
  var gameUsers = [
    ['Game Users', 'Public Good Game', 3700, 'index.html', CONFIG.LEGACY_TRANSITION_DATE, 'Most popular game'],
    ['Game Users', 'Prisoners Dilemma', 3500, 'index.html', CONFIG.LEGACY_TRANSITION_DATE, ''],
    ['Game Users', 'Commons Crisis', 3400, 'index.html', CONFIG.LEGACY_TRANSITION_DATE, ''],
    ['Game Users', 'Network Effects', 3300, 'index.html', CONFIG.LEGACY_TRANSITION_DATE, ''],
    ['Game Users', 'Opportunity Cost', 3200, 'index.html', CONFIG.LEGACY_TRANSITION_DATE, ''],
    ['Game Users', 'Information Asymmetry', 3200, 'index.html', CONFIG.LEGACY_TRANSITION_DATE, ''],
    ['Game Users', 'Cooperation Paradox', 3100, 'index.html', CONFIG.LEGACY_TRANSITION_DATE, ''],
    ['Game Users', 'Economics Concepts', 3100, 'index.html', CONFIG.LEGACY_TRANSITION_DATE, ''],
    ['Game Users', 'Risk and Reward', 3000, 'index.html', CONFIG.LEGACY_TRANSITION_DATE, ''],
    ['Game Users', 'Bidding Wars', 3000, 'index.html', CONFIG.LEGACY_TRANSITION_DATE, ''],
    ['Game Users', 'Externality Game', 2900, 'index.html', CONFIG.LEGACY_TRANSITION_DATE, ''],
  ];

  // ---- Lab/Tool User Counts ----
  var toolUsers = [
    ['Tool Users', 'Code Convert Pro', 3500, 'catalog_data.json', CONFIG.LEGACY_TRANSITION_DATE, 'Premium tool'],
    ['Tool Users', 'Theory of Change Workbench', 3400, 'catalog_data.json', CONFIG.LEGACY_TRANSITION_DATE, ''],
    ['Tool Users', 'Cost-Effectiveness Tool', 3400, 'catalog_data.json', CONFIG.LEGACY_TRANSITION_DATE, ''],
    ['Tool Users', 'Policy Advocacy Lab', 3200, 'catalog_data.json', CONFIG.LEGACY_TRANSITION_DATE, ''],
    ['Tool Users', 'MEL Design Lab', 3100, 'catalog_data.json', CONFIG.LEGACY_TRANSITION_DATE, ''],
    ['Tool Users', 'Real Middle India', 3000, 'catalog_data.json', CONFIG.LEGACY_TRANSITION_DATE, ''],
    ['Tool Users', 'MEL Plan Lab', 3000, 'catalog_data.json', CONFIG.LEGACY_TRANSITION_DATE, ''],
    ['Tool Users', 'Design Thinking Lab', 3000, 'catalog_data.json', CONFIG.LEGACY_TRANSITION_DATE, ''],
    ['Tool Users', 'Resource Sustainability Lab', 2900, 'catalog_data.json', CONFIG.LEGACY_TRANSITION_DATE, ''],
    ['Tool Users', 'Risk Mitigation Lab', 2900, 'catalog_data.json', CONFIG.LEGACY_TRANSITION_DATE, ''],
    ['Tool Users', 'Community Engagement Lab', 2900, 'catalog_data.json', CONFIG.LEGACY_TRANSITION_DATE, ''],
    ['Tool Users', 'Storytelling Lab', 2800, 'catalog_data.json', CONFIG.LEGACY_TRANSITION_DATE, ''],
    ['Tool Users', 'Qual Insights Lab', 2800, 'catalog_data.json', CONFIG.LEGACY_TRANSITION_DATE, ''],
    ['Tool Users', 'Impact Partnerships', 2700, 'catalog_data.json', CONFIG.LEGACY_TRANSITION_DATE, ''],
    ['Tool Users', 'VaniScribe AI Transcription', 280, 'catalog_data.json', CONFIG.LEGACY_TRANSITION_DATE, 'Newest tool'],
  ];

  // ---- Flagship Course Hero Metrics ----
  var heroMetrics = [
    ['Hero Metrics', 'Gandhian Philosophy Learners', 2300, 'index.html', CONFIG.LEGACY_TRANSITION_DATE, 'Displayed on homepage'],
    ['Hero Metrics', 'DevEcon Learners', 3100, 'index.html', CONFIG.LEGACY_TRANSITION_DATE, 'Displayed on homepage'],
    ['Hero Metrics', 'DataViz Learners', 1800, 'index.html', CONFIG.LEGACY_TRANSITION_DATE, 'Displayed on homepage'],
    ['Hero Metrics', 'MEL Users', 1500, 'index.html', CONFIG.LEGACY_TRANSITION_DATE, 'Displayed on homepage'],
    ['Hero Metrics', 'Politics of Aspiration Users', 2100, 'index.html', CONFIG.LEGACY_TRANSITION_DATE, 'Displayed on homepage'],
    ['Hero Metrics', 'Impact Storytelling Users', 890, 'index.html', CONFIG.LEGACY_TRANSITION_DATE, 'Lab tool'],
    ['Hero Metrics', 'Storytelling Game Players', 920, 'index.html', CONFIG.LEGACY_TRANSITION_DATE, 'Game'],
    ['Hero Metrics', 'Qual Research Lab Users', 680, 'index.html', CONFIG.LEGACY_TRANSITION_DATE, ''],
    ['Hero Metrics', 'Statistical Analysis Users', 920, 'index.html', CONFIG.LEGACY_TRANSITION_DATE, ''],
  ];

  var allData = platformMetrics.concat(courseUsers, gameUsers, toolUsers, heroMetrics);
  if (allData.length > 0) {
    legacy.getRange(2, 1, allData.length, 6).setValues(allData);
  }

  // ---- Feature Adoption Tab ----
  var featureData = [];
  // Sum up course users
  var totalCourseUsers = courseUsers.reduce(function(sum, row) { return sum + row[2]; }, 0);
  var totalGameUsers = gameUsers.reduce(function(sum, row) { return sum + row[2]; }, 0);
  var totalToolUsers = toolUsers.reduce(function(sum, row) { return sum + row[2]; }, 0);

  featureData.push(
    ['Courses (70 total)', 'Learning', totalCourseUsers, '', '', 'Active'],
    ['Games (16 total)', 'Engagement', totalGameUsers, '', '', 'Active'],
    ['Labs & Tools (15 total)', 'Hands-on', totalToolUsers, '', '', 'Active'],
    ['Live Case Challenges', 'Assessment', '', '', '', 'Active'],
    ['Portfolio Builder', 'Credentialing', '', '', '', 'Active'],
    ['Certificate Verification', 'Credentialing', '', '', '', 'Active'],
    ['ImpactLex Glossary', 'Reference', '', '', '', 'Active'],
    ['Dataverse (215+ tools)', 'Reference', '', '', '', 'Active'],
    ['NudgeKit (BCT Repository)', 'Reference', '', '', '', 'Active'],
    ['Podcast', 'Content', '', '', '', 'Active'],
    ['Blog', 'Content', '', '', '', 'Active'],
    ['Workshops', 'Training', '', '', '', 'Active'],
    ['Dojos (Peer Learning)', 'Community', '', '', '', 'Active'],
    ['VaniScribe Transcription', 'AI Tool', 280, '', '', 'Active'],
    ['Coaching (1:1)', 'Services', '', '', '', 'Active'],
    ['Org Dashboard', 'Enterprise', '', '', '', 'Active']
  );
  features.getRange(2, 1, featureData.length, 6).setValues(featureData);

  SpreadsheetApp.flush();
  SpreadsheetApp.getUi().alert(
    'Legacy data populated!\n\n' +
    'Total legacy metrics: ' + allData.length + '\n' +
    'Total course users (legacy): ' + totalCourseUsers.toLocaleString() + '\n' +
    'Total game users (legacy): ' + totalGameUsers.toLocaleString() + '\n' +
    'Total tool users (legacy): ' + totalToolUsers.toLocaleString() + '\n\n' +
    'Next: Run pullGA4Data() to fetch current analytics.'
  );
}

// ============================================================
// GA4 DATA PULL — Requires Google Analytics Data API
// ============================================================

/**
 * Pulls key metrics from GA4 for the last 30 days.
 * Requires the Analytics Data API service to be enabled.
 */
function pullGA4Data() {
  if (CONFIG.GA4_PROPERTY_ID === 'YOUR_GA4_PROPERTY_ID') {
    SpreadsheetApp.getUi().alert(
      'Please update CONFIG.GA4_PROPERTY_ID with your numeric GA4 Property ID.\n\n' +
      'Find it at: GA4 Admin > Property Settings > Property ID'
    );
    return;
  }

  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var ga4Sheet = ss.getSheetByName('GA4 Live Data');
  var geoSheet = ss.getSheetByName('Geography');
  var contentSheet = ss.getSheetByName('Content Performance');
  var monthlySheet = ss.getSheetByName('Monthly Snapshots');

  var now = new Date();
  var dateStr = Utilities.formatDate(now, CONFIG.TIMEZONE, 'yyyy-MM-dd HH:mm');
  var property = 'properties/' + CONFIG.GA4_PROPERTY_ID;

  // Clear previous GA4 data (keep headers)
  clearSheetData(ga4Sheet);
  clearSheetData(geoSheet);

  var allRows = [];

  // ---- Overall metrics (last 30 days) ----
  try {
    var overviewResponse = AnalyticsData.Properties.runReport({
      dateRanges: [{ startDate: '30daysAgo', endDate: 'today' }],
      metrics: [
        { name: 'totalUsers' },
        { name: 'newUsers' },
        { name: 'sessions' },
        { name: 'screenPageViews' },
        { name: 'averageSessionDuration' },
        { name: 'bounceRate' },
        { name: 'engagedSessions' }
      ]
    }, property);

    if (overviewResponse.rows && overviewResponse.rows.length > 0) {
      var row = overviewResponse.rows[0];
      var metricNames = ['Total Users', 'New Users', 'Sessions', 'Pageviews', 'Avg Session Duration (s)', 'Bounce Rate', 'Engaged Sessions'];
      for (var i = 0; i < metricNames.length; i++) {
        allRows.push([dateStr, metricNames[i], parseFloat(row.metricValues[i].value), 'Overall', 'All', 'Last 30 days', '30daysAgo', 'today']);
      }
    }
  } catch (e) {
    Logger.log('Error fetching overview: ' + e.message);
    allRows.push([dateStr, 'ERROR: Overview', e.message, '', '', '', '', '']);
  }

  // ---- Top pages (last 30 days) ----
  try {
    var pagesResponse = AnalyticsData.Properties.runReport({
      dateRanges: [{ startDate: '30daysAgo', endDate: 'today' }],
      dimensions: [{ name: 'pagePath' }, { name: 'pageTitle' }],
      metrics: [
        { name: 'screenPageViews' },
        { name: 'averageSessionDuration' },
        { name: 'bounceRate' }
      ],
      orderBys: [{ metric: { metricName: 'screenPageViews' }, desc: true }],
      limit: 50
    }, property);

    if (pagesResponse.rows) {
      // Also populate Content Performance tab
      var contentRows = [];
      pagesResponse.rows.forEach(function(row) {
        var pagePath = row.dimensionValues[0].value;
        var pageTitle = row.dimensionValues[1].value;
        var views = parseFloat(row.metricValues[0].value);
        var avgDuration = parseFloat(row.metricValues[1].value).toFixed(1);
        var bounce = (parseFloat(row.metricValues[2].value) * 100).toFixed(1) + '%';

        allRows.push([dateStr, 'Pageviews', views, 'Page', pagePath, 'Last 30 days', '30daysAgo', 'today']);
        contentRows.push([pagePath, pageTitle, '', views, avgDuration, bounce, '', '']);
      });

      if (contentRows.length > 0) {
        // Preserve legacy pageview data in column C
        var existingContent = contentSheet.getDataRange().getValues();
        var legacyMap = {};
        for (var c = 1; c < existingContent.length; c++) {
          if (existingContent[c][2]) {
            legacyMap[existingContent[c][0]] = existingContent[c][2];
          }
        }

        clearSheetData(contentSheet);
        contentRows.forEach(function(row) {
          if (legacyMap[row[0]]) {
            row[2] = legacyMap[row[0]];
            row[6] = legacyMap[row[0]] + row[3]; // Combined total
          }
        });
        contentSheet.getRange(2, 1, contentRows.length, 8).setValues(contentRows);
      }
    }
  } catch (e) {
    Logger.log('Error fetching pages: ' + e.message);
    allRows.push([dateStr, 'ERROR: Pages', e.message, '', '', '', '', '']);
  }

  // ---- Geography (last 30 days) ----
  try {
    var geoResponse = AnalyticsData.Properties.runReport({
      dateRanges: [{ startDate: '30daysAgo', endDate: 'today' }],
      dimensions: [{ name: 'country' }],
      metrics: [
        { name: 'totalUsers' },
        { name: 'sessions' },
        { name: 'screenPageViews' }
      ],
      orderBys: [{ metric: { metricName: 'totalUsers' }, desc: true }],
      limit: 50
    }, property);

    if (geoResponse.rows) {
      var geoRows = [];
      geoResponse.rows.forEach(function(row) {
        var country = row.dimensionValues[0].value;
        geoRows.push([country, parseFloat(row.metricValues[0].value), parseFloat(row.metricValues[1].value), parseFloat(row.metricValues[2].value), dateStr]);
        allRows.push([dateStr, 'Users by Country', parseFloat(row.metricValues[0].value), 'Country', country, 'Last 30 days', '30daysAgo', 'today']);
      });

      if (geoRows.length > 0) {
        geoSheet.getRange(2, 1, geoRows.length, 5).setValues(geoRows);
      }
    }
  } catch (e) {
    Logger.log('Error fetching geo: ' + e.message);
    allRows.push([dateStr, 'ERROR: Geography', e.message, '', '', '', '', '']);
  }

  // ---- Device category (last 30 days) ----
  try {
    var deviceResponse = AnalyticsData.Properties.runReport({
      dateRanges: [{ startDate: '30daysAgo', endDate: 'today' }],
      dimensions: [{ name: 'deviceCategory' }],
      metrics: [{ name: 'totalUsers' }, { name: 'sessions' }]
    }, property);

    if (deviceResponse.rows) {
      deviceResponse.rows.forEach(function(row) {
        allRows.push([dateStr, 'Users by Device', parseFloat(row.metricValues[0].value), 'Device', row.dimensionValues[0].value, 'Last 30 days', '30daysAgo', 'today']);
      });
    }
  } catch (e) {
    Logger.log('Error fetching devices: ' + e.message);
  }

  // ---- Traffic sources (last 30 days) ----
  try {
    var sourceResponse = AnalyticsData.Properties.runReport({
      dateRanges: [{ startDate: '30daysAgo', endDate: 'today' }],
      dimensions: [{ name: 'sessionDefaultChannelGroup' }],
      metrics: [{ name: 'totalUsers' }, { name: 'sessions' }],
      orderBys: [{ metric: { metricName: 'totalUsers' }, desc: true }]
    }, property);

    if (sourceResponse.rows) {
      sourceResponse.rows.forEach(function(row) {
        allRows.push([dateStr, 'Users by Channel', parseFloat(row.metricValues[0].value), 'Channel', row.dimensionValues[0].value, 'Last 30 days', '30daysAgo', 'today']);
      });
    }
  } catch (e) {
    Logger.log('Error fetching sources: ' + e.message);
  }

  // ---- Language (last 30 days) ----
  try {
    var langResponse = AnalyticsData.Properties.runReport({
      dateRanges: [{ startDate: '30daysAgo', endDate: 'today' }],
      dimensions: [{ name: 'language' }],
      metrics: [{ name: 'totalUsers' }],
      orderBys: [{ metric: { metricName: 'totalUsers' }, desc: true }],
      limit: 20
    }, property);

    if (langResponse.rows) {
      langResponse.rows.forEach(function(row) {
        allRows.push([dateStr, 'Users by Language', parseFloat(row.metricValues[0].value), 'Language', row.dimensionValues[0].value, 'Last 30 days', '30daysAgo', 'today']);
      });
    }
  } catch (e) {
    Logger.log('Error fetching languages: ' + e.message);
  }

  // Write all GA4 rows
  if (allRows.length > 0) {
    ga4Sheet.getRange(2, 1, allRows.length, 8).setValues(allRows);
  }

  // ---- Update Monthly Snapshot ----
  appendMonthlySnapshot(monthlySheet, allRows, dateStr);

  // ---- Update Reconciled Dashboard ----
  updateReconciledDashboard(ss);

  SpreadsheetApp.flush();
  Logger.log('GA4 data pull complete: ' + allRows.length + ' rows');
}

/**
 * Appends a monthly snapshot row if we haven't recorded this month yet.
 */
function appendMonthlySnapshot(sheet, ga4Rows, dateStr) {
  var now = new Date();
  var monthKey = Utilities.formatDate(now, CONFIG.TIMEZONE, 'yyyy-MM');

  // Check if this month already exists
  var existing = sheet.getDataRange().getValues();
  for (var i = 1; i < existing.length; i++) {
    if (existing[i][0] === monthKey) return; // Already recorded
  }

  // Extract overview metrics from ga4Rows
  var totalUsers = '', newUsers = '', sessions = '', pageviews = '', avgDuration = '';
  ga4Rows.forEach(function(row) {
    if (row[3] === 'Overall') {
      switch (row[1]) {
        case 'Total Users': totalUsers = row[2]; break;
        case 'New Users': newUsers = row[2]; break;
        case 'Sessions': sessions = row[2]; break;
        case 'Pageviews': pageviews = row[2]; break;
        case 'Avg Session Duration (s)': avgDuration = row[2]; break;
      }
    }
  });

  var nextRow = sheet.getLastRow() + 1;
  sheet.getRange(nextRow, 1, 1, 7).setValues([[monthKey, totalUsers, newUsers, sessions, pageviews, avgDuration, 'GA4']]);
}

/**
 * Updates the Reconciled Dashboard tab by merging legacy totals with GA4 current data.
 */
function updateReconciledDashboard(ss) {
  var reconciled = ss.getSheetByName('Reconciled Dashboard');
  var legacy = ss.getSheetByName('Legacy Metrics');
  var ga4 = ss.getSheetByName('GA4 Live Data');

  clearSheetData(reconciled);

  // Sum legacy metrics by category
  var legacyData = legacy.getDataRange().getValues();
  var totalLegacyCourseUsers = 0, totalLegacyGameUsers = 0, totalLegacyToolUsers = 0;
  for (var i = 1; i < legacyData.length; i++) {
    var cat = legacyData[i][0];
    var val = legacyData[i][2];
    if (cat === 'Course Users') totalLegacyCourseUsers += val;
    if (cat === 'Game Users') totalLegacyGameUsers += val;
    if (cat === 'Tool Users') totalLegacyToolUsers += val;
  }

  // Extract GA4 overview
  var ga4Data = ga4.getDataRange().getValues();
  var ga4Users = '', ga4NewUsers = '', ga4Sessions = '', ga4Pageviews = '';
  for (var j = 1; j < ga4Data.length; j++) {
    if (ga4Data[j][3] === 'Overall') {
      switch (ga4Data[j][1]) {
        case 'Total Users': ga4Users = ga4Data[j][2]; break;
        case 'New Users': ga4NewUsers = ga4Data[j][2]; break;
        case 'Sessions': ga4Sessions = ga4Data[j][2]; break;
        case 'Pageviews': ga4Pageviews = ga4Data[j][2]; break;
      }
    }
  }

  var reconciledRows = [
    ['Total Course Users', totalLegacyCourseUsers, 'Pre-' + CONFIG.LEGACY_TRANSITION_DATE, ga4Users || 'Run pullGA4Data()', 'Last 30 days', ga4Users ? totalLegacyCourseUsers + ga4Users : '', ''],
    ['Total Game Users', totalLegacyGameUsers, 'Pre-' + CONFIG.LEGACY_TRANSITION_DATE, '', 'N/A (page-level)', totalLegacyGameUsers, ''],
    ['Total Tool Users', totalLegacyToolUsers, 'Pre-' + CONFIG.LEGACY_TRANSITION_DATE, '', 'N/A (page-level)', totalLegacyToolUsers, ''],
    ['GA4 Total Users (30d)', '', '', ga4Users, 'Last 30 days', '', ''],
    ['GA4 New Users (30d)', '', '', ga4NewUsers, 'Last 30 days', '', ''],
    ['GA4 Sessions (30d)', '', '', ga4Sessions, 'Last 30 days', '', ''],
    ['GA4 Pageviews (30d)', '', '', ga4Pageviews, 'Last 30 days', '', ''],
    ['Free Courses Available', 39, 'Current', 39, 'Current', 39, 'Stable'],
    ['Flagship Courses', 7, 'Current', 7, 'Current', 7, 'Stable'],
    ['Interactive Labs', 10, 'Current', 10, 'Current', 10, 'Stable'],
    ['Educational Games', 12, 'Current', 12, 'Current', 12, 'Stable'],
    ['Handouts', 200, 'Current', 200, 'Current', 200, 'Growing'],
    ['Dataverse Tools', 215, 'Current', 215, 'Current', 215, 'Growing'],
    ['Case Studies', 200, 'Current', 200, 'Current', 200, 'Stable'],
    ['Dataset Rows', 840000, 'Current', 840000, 'Current', 840000, 'Stable'],
    ['Live Challenges', 9, 'Current', 9, 'Current', 9, 'New'],
  ];

  reconciled.getRange(2, 1, reconciledRows.length, 7).setValues(reconciledRows);
}

function clearSheetData(sheet) {
  if (sheet.getLastRow() > 1) {
    sheet.getRange(2, 1, sheet.getLastRow() - 1, sheet.getLastColumn()).clearContent();
  }
}

// ============================================================
// MENU — Adds custom menu to the spreadsheet
// ============================================================

function onOpen() {
  SpreadsheetApp.getUi().createMenu('ImpactMojo Analytics')
    .addItem('Setup Sheet Structure', 'setupSheetStructure')
    .addItem('Load Legacy Data', 'populateLegacyData')
    .addSeparator()
    .addItem('Pull GA4 Data (Last 30 days)', 'pullGA4Data')
    .addItem('Update Reconciled Dashboard', 'updateReconciledDashboardWrapper')
    .addSeparator()
    .addItem('Export Summary as JSON', 'exportSummaryJSON')
    .addToUi();
}

function updateReconciledDashboardWrapper() {
  updateReconciledDashboard(SpreadsheetApp.getActiveSpreadsheet());
  SpreadsheetApp.getUi().alert('Reconciled Dashboard updated.');
}

// ============================================================
// JSON EXPORT — For the web dashboard
// ============================================================

/**
 * Generates a JSON summary suitable for the web admin dashboard.
 * Copy/paste this output or serve it via Apps Script Web App.
 */
function exportSummaryJSON() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();

  // Legacy totals
  var legacy = ss.getSheetByName('Legacy Metrics').getDataRange().getValues();
  var legacySummary = { platform: {}, courseUsers: {}, gameUsers: {}, toolUsers: {} };
  for (var i = 1; i < legacy.length; i++) {
    var cat = legacy[i][0], name = legacy[i][1], val = legacy[i][2];
    if (cat === 'Platform' || cat === 'Content') legacySummary.platform[name] = val;
    else if (cat === 'Course Users') legacySummary.courseUsers[name] = val;
    else if (cat === 'Game Users') legacySummary.gameUsers[name] = val;
    else if (cat === 'Tool Users') legacySummary.toolUsers[name] = val;
  }

  // GA4 overview
  var ga4 = ss.getSheetByName('GA4 Live Data').getDataRange().getValues();
  var ga4Summary = { overview: {}, geography: [], channels: [], devices: [] };
  for (var j = 1; j < ga4.length; j++) {
    var metric = ga4[j][1], value = ga4[j][2], dim = ga4[j][3], dimVal = ga4[j][4];
    if (dim === 'Overall') ga4Summary.overview[metric] = value;
    else if (dim === 'Country') ga4Summary.geography.push({ country: dimVal, users: value });
    else if (dim === 'Channel') ga4Summary.channels.push({ channel: dimVal, users: value });
    else if (dim === 'Device') ga4Summary.devices.push({ device: dimVal, users: value });
  }

  var summary = {
    exportDate: new Date().toISOString(),
    legacy: legacySummary,
    ga4: ga4Summary
  };

  var json = JSON.stringify(summary, null, 2);
  Logger.log(json);

  // Show in a dialog
  var html = HtmlService.createHtmlOutput(
    '<pre style="font-size:11px; max-height:500px; overflow:auto;">' +
    json.replace(/</g, '&lt;') +
    '</pre><br><p>Copy this JSON and paste it into <code>admin/analytics-data.json</code> in your repo, ' +
    'or set up the Web App deploy to serve it automatically.</p>'
  ).setWidth(700).setHeight(600).setTitle('Analytics JSON Export');

  SpreadsheetApp.getUi().showModalDialog(html, 'Analytics Summary JSON');
}

// ============================================================
// WEB APP DEPLOY (optional)
// ============================================================

/**
 * If you deploy this as a Web App (Deploy > New Deployment > Web App),
 * this function serves the JSON summary via HTTP GET.
 * The admin dashboard can fetch it directly.
 */
function doGet(e) {
  var ss = SpreadsheetApp.openById(SpreadsheetApp.getActiveSpreadsheet().getId());

  var legacy = ss.getSheetByName('Legacy Metrics').getDataRange().getValues();
  var ga4 = ss.getSheetByName('GA4 Live Data').getDataRange().getValues();
  var features = ss.getSheetByName('Feature Adoption').getDataRange().getValues();

  var summary = {
    exportDate: new Date().toISOString(),
    legacy: sheetToObjects(legacy),
    ga4: sheetToObjects(ga4),
    features: sheetToObjects(features)
  };

  return ContentService.createTextOutput(JSON.stringify(summary))
    .setMimeType(ContentService.MimeType.JSON);
}

function sheetToObjects(data) {
  var headers = data[0];
  var result = [];
  for (var i = 1; i < data.length; i++) {
    var obj = {};
    for (var j = 0; j < headers.length; j++) {
      obj[headers[j]] = data[i][j];
    }
    result.push(obj);
  }
  return result;
}
