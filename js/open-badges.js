/**
 * ImpactMojo Open Badges System
 * W3C Open Badges 3.0 / Verifiable Credentials
 *
 * Provides:
 *  - Badge class definitions per course and track
 *  - OB3.0 JSON-LD credential builder
 *  - SVG badge image generator
 *  - Badge wallet renderer (account page)
 *  - LinkedIn / social share helpers
 */

(function () {
  'use strict';

  var ISSUER = {
    id: 'https://www.impactmojo.in',
    type: ['Profile'],
    name: 'ImpactMojo',
    url: 'https://www.impactmojo.in',
    description: 'Open learning platform for international development professionals.',
    image: 'https://www.impactmojo.in/assets/logo.png',
    email: 'hello@impactmojo.in'
  };

  // ── Badge class definitions ─────────────────────────────────────────
  // Each course maps to a BadgeClass with competency tags and track
  var BADGE_CLASSES = {
    mel: {
      name: 'MEL Practitioner',
      description: 'Demonstrated mastery of Monitoring, Evaluation & Learning frameworks, qualitative methods, and research ethics.',
      track: 'Monitoring, Evaluation & Learning',
      competencies: ['MEL Frameworks', 'Theory of Change', 'Qualitative Methods', 'Research Ethics'],
      color: '#10B981',
      icon: 'crosshair'
    },
    dataviz: {
      name: 'Data Visualization Specialist',
      description: 'Proficient in visual encoding, chart selection, Tufte principles, and building M&E dashboards.',
      track: 'Data & Technology',
      competencies: ['Visual Encoding', 'Chart Selection', 'Dashboard Design', 'Data Storytelling'],
      color: '#0EA5E9',
      icon: 'bar-chart'
    },
    devai: {
      name: 'AI for Impact Practitioner',
      description: 'Skilled in applying ML, NLP, and computer vision to development monitoring and evaluation.',
      track: 'Data & Technology',
      competencies: ['Machine Learning', 'NLP for Development', 'Algorithmic Bias', 'AI Ethics'],
      color: '#0EA5E9',
      icon: 'cpu'
    },
    devecon: {
      name: 'Development Economics Analyst',
      description: 'Comprehensive understanding of development economics, poverty analysis, and impact evaluation methods.',
      track: 'Policy & Economics',
      competencies: ['Development Economics', 'Poverty Analysis', 'Impact Evaluation', 'Cost-Effectiveness'],
      color: '#6366F1',
      icon: 'globe'
    },
    gandhi: {
      name: 'Gandhian Thought Scholar',
      description: 'Deep engagement with Gandhi\'s political philosophy and its application to contemporary development.',
      track: 'Philosophy, Law & Governance',
      competencies: ['Political Philosophy', 'Nonviolent Praxis', 'Ethical Leadership', 'Social Movements'],
      color: '#8B5CF6',
      icon: 'book'
    },
    law: {
      name: 'Law & Development Practitioner',
      description: 'Proficient in constitutional law, rights-based approaches, and legal frameworks for development.',
      track: 'Philosophy, Law & Governance',
      competencies: ['Constitutional Law', 'Rights-Based Approach', 'Legal Frameworks', 'Justice Systems'],
      color: '#8B5CF6',
      icon: 'scale'
    },
    media: {
      name: 'Development Communication Specialist',
      description: 'Skilled in BCC, storytelling for impact, and media strategies for development programs.',
      track: 'Health, Communication & Wellbeing',
      competencies: ['BCC Strategy', 'Storytelling', 'Media for Development', 'Campaign Design'],
      color: '#F59E0B',
      icon: 'message'
    },
    SEL: {
      name: 'SEL Facilitator',
      description: 'Certified in Social & Emotional Learning facilitation for development practitioners.',
      track: 'Health, Communication & Wellbeing',
      competencies: ['Social-Emotional Learning', 'Facilitation', 'Wellbeing Frameworks', 'Group Dynamics'],
      color: '#F59E0B',
      icon: 'heart'
    },
    poa: {
      name: 'Politics of Aspiration Analyst',
      description: 'Understanding of political economy, aspiration theory, and development politics.',
      track: 'Policy & Economics',
      competencies: ['Political Economy', 'Aspiration Theory', 'Development Politics', 'Policy Analysis'],
      color: '#6366F1',
      icon: 'trending-up'
    },
    gender: {
      name: 'Gender & Equity Analyst',
      description: 'Grounded in feminist theory, intersectionality, and the political economy of gender in South Asia.',
      track: 'Gender, Equity & Inclusion',
      competencies: ['Feminist Frameworks', 'Intersectionality', 'Gender Analysis', 'Political Economy of Gender'],
      color: '#D53F8C',
      icon: 'heart'
    },
    pubchoice: {
      name: 'Public Choice Analyst',
      description: 'Applies decisions, incentives and institutional analysis to collective action and governance.',
      track: 'Policy & Economics',
      competencies: ['Incentive Analysis', 'Collective Action', 'Institutional Economics', 'Rent-Seeking & Reform'],
      color: '#6366F1',
      icon: 'scale'
    },
    pubpol: {
      name: 'Public Policy Practitioner',
      description: 'Skilled in policy process, design, and governance in the Indian context.',
      track: 'Policy & Economics',
      competencies: ['Policy Process', 'Policy Design', 'Governance', 'Implementation Analysis'],
      color: '#6366F1',
      icon: 'globe'
    },
    causal: {
      name: 'Causal Inference Practitioner',
      description: 'Competent in evaluation designs, estimators, and the judgement calls behind credible causal claims.',
      track: 'Monitoring, Evaluation & Learning',
      competencies: ['Counterfactual Reasoning', 'Experimental Design', 'Quasi-Experimental Methods', 'Evidence Appraisal'],
      color: '#10B981',
      icon: 'crosshair'
    },
    livelihoods: {
      name: 'Livelihoods Specialist',
      description: 'Understands rural and urban livelihoods, skills, and labour-market realities in India.',
      track: 'Policy & Economics',
      competencies: ['Livelihood Frameworks', 'Rural & Urban Labour', 'Skills & Employment', 'Programme Evidence'],
      color: '#6366F1',
      icon: 'trending-up'
    },
    powerBI: {
      name: 'Power BI Practitioner',
      description: 'Builds honest, working dashboards — Power Query, data models, DAX, and visualisation ethics.',
      track: 'Data & Technology',
      competencies: ['Power Query', 'Data Modelling', 'DAX', 'Dashboard Ethics'],
      color: '#0EA5E9',
      icon: 'bar-chart'
    },
    intervention: {
      name: 'Intervention Design Practitioner',
      description: 'Designs development interventions from model to scale with evidence and implementation judgement.',
      track: 'Monitoring, Evaluation & Learning',
      competencies: ['Programme Theory', 'Design Choices', 'Piloting & Iteration', 'Scale & Sustainability'],
      color: '#10B981',
      icon: 'crosshair'
    },
    'nothing-about-us': {
      name: 'Disability-Inclusive Development Practitioner',
      description: 'Grounded in disability models, the CRPD and RPwD Act, inclusive programming and MEL.',
      track: 'Gender, Equity & Inclusion',
      competencies: ['Disability Models & Justice', 'CRPD & Disability Law', 'Washington Group Questions', 'Inclusive Programming'],
      color: '#D53F8C',
      icon: 'heart'
    },
    'nvc-rj': {
      name: 'Nonviolent Practice Facilitator',
      description: 'Practices nonviolent communication, principled resistance, and restorative repair.',
      track: 'Philosophy, Law & Governance',
      competencies: ['Nonviolent Communication', 'Conflict Transformation', 'Restorative Justice', 'Repair & Accountability'],
      color: '#8B5CF6',
      icon: 'message'
    }
  };
  // URL slug for the SEL course is lowercase; keep both ids valid.
  BADGE_CLASSES.sel = BADGE_CLASSES.SEL;

  // ── Track-level badges (earned by completing all courses in a track) ──
  var TRACK_BADGES = {
    'Data & Technology': {
      name: 'Data & Technology Track Credential',
      description: 'Completed all courses in the Data & Technology learning track.',
      courseIds: ['dataviz', 'devai'],
      color: '#0EA5E9'
    },
    'Policy & Economics': {
      name: 'Policy & Economics Track Credential',
      description: 'Completed all courses in the Policy & Economics learning track.',
      courseIds: ['devecon', 'poa'],
      color: '#6366F1'
    },
    'Philosophy, Law & Governance': {
      name: 'Philosophy, Law & Governance Track Credential',
      description: 'Completed all courses in the Philosophy, Law & Governance track.',
      courseIds: ['gandhi', 'law'],
      color: '#8B5CF6'
    },
    'Health, Communication & Wellbeing': {
      name: 'Health, Communication & Wellbeing Track Credential',
      description: 'Completed all courses in the Health, Communication & Wellbeing track.',
      courseIds: ['SEL', 'media'],
      color: '#F59E0B'
    },
    'Monitoring, Evaluation & Learning': {
      name: 'MEL Track Credential',
      description: 'Completed all courses in the Monitoring, Evaluation & Learning track.',
      courseIds: ['mel'],
      color: '#10B981'
    }
  };

  // ── OB3.0 JSON-LD Credential Builder ────────────────────────────────
  function buildCredential(cert, recipientName) {
    var bc = BADGE_CLASSES[cert.course_id];
    if (!bc) return null;

    var issuedDate = cert.issued_at ? new Date(cert.issued_at).toISOString() : new Date().toISOString();

    return {
      '@context': [
        'https://www.w3.org/ns/credentials/v2',
        'https://purl.imsglobal.org/spec/ob/v3p0/context-3.0.3.json'
      ],
      type: ['VerifiableCredential', 'OpenBadgeCredential'],
      id: 'https://www.impactmojo.in/verify-certificate.html?cert=' + encodeURIComponent(cert.certificate_number),
      issuer: ISSUER,
      issuanceDate: issuedDate,
      name: bc.name,
      credentialSubject: {
        type: ['AchievementSubject'],
        name: recipientName || 'Verified Learner',
        achievement: {
          type: ['Achievement'],
          name: bc.name,
          description: bc.description,
          criteria: {
            narrative: 'Complete all modules and assessments in the ' + (cert.course_name || cert.course_id) + ' course with a passing score.'
          },
          tag: bc.competencies,
          alignment: [{
            type: ['Alignment'],
            targetName: bc.track,
            targetDescription: 'ImpactMojo Learning Track',
            targetFramework: 'ImpactMojo Competency Framework'
          }]
        }
      },
      credentialStatus: {
        type: 'StatusList2021Entry',
        statusPurpose: 'revocation',
        statusListIndex: '0',
        statusListCredential: 'https://www.impactmojo.in/api/badge-status'
      },
      evidence: [{
        type: ['Evidence'],
        name: 'Course Completion',
        description: 'Completed all modules and passed assessments for ' + (cert.course_name || cert.course_id) + '.',
        id: cert.verification_url || ('https://www.impactmojo.in/verify-certificate.html?cert=' + cert.certificate_number)
      }]
    };
  }

  // ── SVG Badge Generator ─────────────────────────────────────────────
  function generateBadgeSVG(courseId, recipientName, certNumber, size) {
    var bc = BADGE_CLASSES[courseId];
    if (!bc) return '';
    var s = size || 200;
    var half = s / 2;
    var r = half - 8;

    // Icon paths (simplified)
    var icons = {
      'crosshair': 'M12 2v4M12 18v4M2 12h4M18 12h4M12 8a4 4 0 100 8 4 4 0 000-8z',
      'bar-chart': 'M18 20V10M12 20V4M6 20v-6',
      'cpu': 'M4 4h16v16H4zM9 1v3M15 1v3M9 20v3M15 20v3M20 9h3M20 14h3M1 9h3M1 14h3',
      'globe': 'M12 2a10 10 0 100 20 10 10 0 000-20zM2 12h20M12 2a15 15 0 014 10 15 15 0 01-4 10 15 15 0 01-4-10A15 15 0 0112 2z',
      'book': 'M4 19.5A2.5 2.5 0 016.5 17H20M4 4.5A2.5 2.5 0 016.5 2H20v20H6.5A2.5 2.5 0 014 19.5z',
      'scale': 'M12 3v18M3 7l9-4 9 4M3 7v4a9 9 0 006 0V7M15 7v4a9 9 0 006 0V7',
      'message': 'M21 15a2 2 0 01-2 2H7l-4 4V5a2 2 0 012-2h14a2 2 0 012 2z',
      'heart': 'M20.84 4.61a5.5 5.5 0 00-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 00-7.78 7.78L12 21.23l8.84-8.84a5.5 5.5 0 000-7.78z',
      'trending-up': 'M23 6l-9.5 9.5-5-5L1 18'
    };

    var iconPath = icons[bc.icon] || icons['crosshair'];
    var displayName = recipientName ? escapeXml(recipientName) : '';
    var badgeName = escapeXml(bc.name);
    var certDisplay = certNumber ? escapeXml('#' + certNumber) : '';

    return '<svg xmlns="http://www.w3.org/2000/svg" width="' + s + '" height="' + s + '" viewBox="0 0 ' + s + ' ' + s + '">' +
      '<defs>' +
        '<linearGradient id="bg_' + courseId + '" x1="0" y1="0" x2="1" y2="1">' +
          '<stop offset="0%" stop-color="' + bc.color + '" stop-opacity="0.15"/>' +
          '<stop offset="100%" stop-color="' + bc.color + '" stop-opacity="0.05"/>' +
        '</linearGradient>' +
        '<linearGradient id="ring_' + courseId + '" x1="0" y1="0" x2="1" y2="1">' +
          '<stop offset="0%" stop-color="' + bc.color + '"/>' +
          '<stop offset="100%" stop-color="' + adjustColor(bc.color, -30) + '"/>' +
        '</linearGradient>' +
      '</defs>' +
      '<circle cx="' + half + '" cy="' + half + '" r="' + r + '" fill="url(#bg_' + courseId + ')" stroke="url(#ring_' + courseId + ')" stroke-width="3"/>' +
      '<circle cx="' + half + '" cy="' + half + '" r="' + (r - 6) + '" fill="none" stroke="' + bc.color + '" stroke-width="0.5" stroke-dasharray="4 3"/>' +
      '<g transform="translate(' + (half - 12) + ',' + (half - 40) + ')" stroke="' + bc.color + '" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">' +
        '<path d="' + iconPath + '"/>' +
      '</g>' +
      '<text x="' + half + '" y="' + (half + 10) + '" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" font-weight="700" fill="' + bc.color + '">' + badgeName + '</text>' +
      (displayName ? '<text x="' + half + '" y="' + (half + 26) + '" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" fill="#64748B">' + displayName + '</text>' : '') +
      (certDisplay ? '<text x="' + half + '" y="' + (half + 38) + '" text-anchor="middle" font-family="system-ui,sans-serif" font-size="6" fill="#94A3B8">' + certDisplay + '</text>' : '') +
      '<text x="' + half + '" y="' + (s - 14) + '" text-anchor="middle" font-family="system-ui,sans-serif" font-size="7" font-weight="600" fill="#94A3B8">ImpactMojo</text>' +
    '</svg>';
  }

  function escapeXml(s) {
    return (s || '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  }

  function adjustColor(hex, amount) {
    var num = parseInt(hex.replace('#', ''), 16);
    var r = Math.max(0, Math.min(255, (num >> 16) + amount));
    var g = Math.max(0, Math.min(255, ((num >> 8) & 0x00FF) + amount));
    var b = Math.max(0, Math.min(255, (num & 0x0000FF) + amount));
    return '#' + (0x1000000 + r * 0x10000 + g * 0x100 + b).toString(16).slice(1);
  }

  // ── LinkedIn Share ──────────────────────────────────────────────────
  function getLinkedInShareUrl(cert) {
    var bc = BADGE_CLASSES[cert.course_id];
    if (!bc) return null;

    var params = {
      name: bc.name + ' — ImpactMojo',
      organizationId: '104873498',
      issueYear: new Date(cert.issued_at).getFullYear(),
      issueMonth: new Date(cert.issued_at).getMonth() + 1,
      certUrl: cert.verification_url || ('https://www.impactmojo.in/verify-certificate.html?cert=' + cert.certificate_number),
      certId: cert.certificate_number
    };

    return 'https://www.linkedin.com/profile/add?startTask=CERTIFICATION_NAME' +
      '&name=' + encodeURIComponent(params.name) +
      '&organizationName=' + encodeURIComponent('ImpactMojo') +
      '&issueYear=' + params.issueYear +
      '&issueMonth=' + params.issueMonth +
      '&certUrl=' + encodeURIComponent(params.certUrl) +
      '&certId=' + encodeURIComponent(params.certId);
  }

  // ── Badge Wallet Renderer (for account page) ───────────────────────
  function renderBadgeWallet(certs, containerId) {
    var container = document.getElementById(containerId);
    if (!container || !certs || !certs.length) return;

    var html = '<div class="imx-badge-wallet">';

    certs.forEach(function (cert) {
      var bc = BADGE_CLASSES[cert.course_id];
      if (!bc) return;

      var date = new Date(cert.issued_at).toLocaleDateString('en-IN', { day: 'numeric', month: 'short', year: 'numeric' });
      var verifyUrl = cert.verification_url || ('https://www.impactmojo.in/verify-certificate.html?cert=' + cert.certificate_number);
      var linkedInUrl = getLinkedInShareUrl(cert);
      var badgeSvg = generateBadgeSVG(cert.course_id, null, cert.certificate_number, 120);

      html += '<div class="imx-badge-card" data-course="' + cert.course_id + '">' +
        '<div class="imx-badge-visual">' + badgeSvg + '</div>' +
        '<div class="imx-badge-info">' +
          '<div class="imx-badge-name" style="color:' + bc.color + '">' + escapeXml(bc.name) + '</div>' +
          '<div class="imx-badge-track">' + escapeXml(bc.track) + '</div>' +
          '<div class="imx-badge-date">Issued ' + date + '</div>' +
          '<div class="imx-badge-competencies">' +
            bc.competencies.map(function (c) { return '<span class="imx-competency-tag">' + escapeXml(c) + '</span>'; }).join('') +
          '</div>' +
          '<div class="imx-badge-actions">' +
            '<a href="' + verifyUrl + '" target="_blank" class="imx-badge-action-btn">Verify</a>' +
            (linkedInUrl ? '<a href="' + linkedInUrl + '" target="_blank" class="imx-badge-action-btn imx-badge-linkedin">Add to LinkedIn</a>' : '') +
            '<button class="imx-badge-action-btn imx-badge-download" data-course="' + cert.course_id + '" data-cert="' + cert.certificate_number + '">Download Badge</button>' +
            '<button class="imx-badge-action-btn imx-badge-json" data-cert-idx="' + cert.certificate_number + '">View Credential</button>' +
          '</div>' +
        '</div>' +
      '</div>';
    });

    html += '</div>';
    container.innerHTML = html;

    // Bind download handlers
    container.querySelectorAll('.imx-badge-download').forEach(function (btn) {
      btn.addEventListener('click', function () {
        var svg = generateBadgeSVG(btn.dataset.course, null, btn.dataset.cert, 400);
        var blob = new Blob([svg], { type: 'image/svg+xml' });
        var url = URL.createObjectURL(blob);
        var a = document.createElement('a');
        a.href = url;
        a.download = 'impactmojo-badge-' + btn.dataset.course + '.svg';
        a.click();
        URL.revokeObjectURL(url);
      });
    });

    // Bind JSON-LD viewer
    container.querySelectorAll('.imx-badge-json').forEach(function (btn) {
      btn.addEventListener('click', function () {
        var certNum = btn.dataset.certIdx;
        var cert = certs.find(function (c) { return c.certificate_number === certNum; });
        if (!cert) return;
        var credential = buildCredential(cert, null);
        var jsonStr = JSON.stringify(credential, null, 2);
        var modal = document.createElement('div');
        modal.className = 'imx-badge-json-modal';
        modal.innerHTML = '<div class="imx-badge-json-content">' +
          '<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:1rem;">' +
            '<h3 style="margin:0;font-size:1rem;">Open Badge 3.0 Credential</h3>' +
            '<button class="imx-badge-json-close" style="background:none;border:none;font-size:1.5rem;cursor:pointer;color:var(--text-secondary);">&times;</button>' +
          '</div>' +
          '<pre style="background:var(--hover-bg);padding:1rem;border-radius:8px;overflow:auto;max-height:60vh;font-size:0.8rem;line-height:1.5;">' + escapeXml(jsonStr) + '</pre>' +
          '<div style="display:flex;gap:0.5rem;margin-top:1rem;">' +
            '<button class="imx-badge-action-btn imx-copy-json">Copy JSON-LD</button>' +
          '</div>' +
        '</div>';
        document.body.appendChild(modal);
        modal.querySelector('.imx-badge-json-close').addEventListener('click', function () { modal.remove(); });
        modal.addEventListener('click', function (e) { if (e.target === modal) modal.remove(); });
        modal.querySelector('.imx-copy-json').addEventListener('click', function () {
          navigator.clipboard.writeText(jsonStr).then(function () {
            modal.querySelector('.imx-copy-json').textContent = 'Copied!';
            setTimeout(function () { modal.querySelector('.imx-copy-json').textContent = 'Copy JSON-LD'; }, 2000);
          });
        });
      });
    });
  }

  // ── Public API ──────────────────────────────────────────────────────
  window.IMPACTMOJO = window.IMPACTMOJO || {};
  window.IMPACTMOJO.badges = {
    BADGE_CLASSES: BADGE_CLASSES,
    TRACK_BADGES: TRACK_BADGES,
    ISSUER: ISSUER,
    buildCredential: buildCredential,
    generateBadgeSVG: generateBadgeSVG,
    getLinkedInShareUrl: getLinkedInShareUrl,
    renderBadgeWallet: renderBadgeWallet
  };
})();
