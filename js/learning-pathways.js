/**
 * ImpactMojo Learning Pathways
 * Structured credential tracks with prerequisites, milestones, and visual progress.
 *
 * Builds on:
 *  - learning-tracks.js (TRACKS data, track modal)
 *  - course-progress.js (localStorage per-course progress)
 *  - open-badges.js (badge definitions, track badges)
 */

(function () {
  'use strict';

  var STORAGE_KEY = 'impactmojo_pathway_state';

  // ── Pathway Definitions ─────────────────────────────────────────────
  // Each pathway is a structured journey through a track with ordered
  // steps, prerequisites, and milestone markers.
  var PATHWAYS = {
    'mel-practitioner': {
      name: 'MEL Practitioner',
      track: 'Monitoring, Evaluation & Learning',
      description: 'Master MEL frameworks, qualitative methods, and research design through courses, labs, and hands-on practice.',
      audience: 'M&E officers, program managers, researchers',
      color: '#10B981',
      steps: [
        { id: 'mel-course', type: 'course', courseId: 'mel', title: 'MEL Flagship Course', description: 'Complete all modules in Monitoring, Evaluation & Learning.' },
        { id: 'toc-lab', type: 'lab', title: 'TOC Lab', description: 'Build a Theory of Change for a real program.' },
        { id: 'mle-lab', type: 'lab', title: 'MLE Lab', description: 'Design monitoring indicators and a learning agenda.' },
        { id: 'mel-planning-lab', type: 'lab', title: 'MEL Planning Lab', description: 'Develop a complete MEL plan with data collection tools.' },
        { id: 'survey-lab', type: 'lab', title: 'Survey Design Lab', description: 'Design and pilot a household survey instrument.' }
      ],
      milestones: [
        { afterStep: 'mel-course', label: 'MEL Foundations', badge: true },
        { afterStep: 'mel-planning-lab', label: 'MEL Practitioner', badge: true, credential: true }
      ]
    },
    'data-analyst': {
      name: 'Development Data Analyst',
      track: 'Data & Technology',
      description: 'Build comprehensive data skills from visualization and AI to advanced statistical analysis for development work.',
      audience: 'Data analysts, researchers, M&E specialists',
      color: '#0EA5E9',
      steps: [
        { id: 'dataviz-course', type: 'course', courseId: 'dataviz', title: 'Data Visualization for Impact', description: 'Master visual encoding, chart selection, and M&E dashboards.' },
        { id: 'devai-course', type: 'course', courseId: 'devai', title: 'AI for Impact', description: 'Apply ML, NLP, and computer vision to development monitoring.' },
        { id: 'viz-lab', type: 'lab', title: 'Visualization Lab', description: 'Create publication-quality visualizations from real datasets.' },
        { id: 'lorenz-game', type: 'game', title: 'Lorenz Curve Game', description: 'Practice inequality measurement interactively.' },
        { id: 'sampling-game', type: 'game', title: 'Sampling Strategy Game', description: 'Design sampling strategies for field surveys.' }
      ],
      milestones: [
        { afterStep: 'dataviz-course', label: 'Data Viz Certified', badge: true },
        { afterStep: 'devai-course', label: 'AI Certified', badge: true },
        { afterStep: 'sampling-game', label: 'Data Analyst', badge: true, credential: true }
      ]
    },
    'dev-economist': {
      name: 'Development Economist',
      track: 'Policy & Economics',
      description: 'From foundational economics through policy analysis, impact evaluation, and cost-effectiveness.',
      audience: 'Economists, policy analysts, program designers',
      color: '#6366F1',
      steps: [
        { id: 'devecon-course', type: 'course', courseId: 'devecon', title: 'Development Economics', description: 'Master development economics theory and empirical methods.' },
        { id: 'poa-course', type: 'course', courseId: 'poa', title: 'Politics of Aspiration', description: 'Understand political economy and aspiration theory.' },
        { id: 'cea-lab', type: 'lab', title: 'CEA Lab', description: 'Conduct a cost-effectiveness analysis.' },
        { id: 'ie-lab', type: 'lab', title: 'Impact Evaluation Lab', description: 'Design a randomized or quasi-experimental evaluation.' },
        { id: 'budget-game', type: 'game', title: 'Budget Trade-offs Game', description: 'Allocate scarce resources across competing programs.' },
        { id: 'targeting-game', type: 'game', title: 'Targeting Game', description: 'Design targeting criteria for social programs.' }
      ],
      milestones: [
        { afterStep: 'devecon-course', label: 'Economics Foundations', badge: true },
        { afterStep: 'targeting-game', label: 'Development Economist', badge: true, credential: true }
      ]
    },
    'governance-scholar': {
      name: 'Governance & Rights Scholar',
      track: 'Philosophy, Law & Governance',
      description: 'Gandhian political thought, constitutional law, and rights-based approaches to development.',
      audience: 'Governance professionals, advocates, academics',
      color: '#8B5CF6',
      steps: [
        { id: 'gandhi-course', type: 'course', courseId: 'gandhi', title: "Gandhi's Political Thought", description: "Engage with Gandhi's philosophy and contemporary relevance." },
        { id: 'law-course', type: 'course', courseId: 'law', title: 'Law & Development', description: 'Constitutional law, rights, and legal frameworks.' },
        { id: 'advocacy-lab', type: 'lab', title: 'Policy and Advocacy Lab', description: 'Design an evidence-based advocacy campaign.' }
      ],
      milestones: [
        { afterStep: 'gandhi-course', label: 'Gandhian Scholar', badge: true },
        { afterStep: 'advocacy-lab', label: 'Governance Scholar', badge: true, credential: true }
      ]
    },
    'health-comms': {
      name: 'Health & Communication Specialist',
      track: 'Health, Communication & Wellbeing',
      description: 'SEL facilitation, media for development, and public health communication skills.',
      audience: 'Health communicators, BCC designers, wellbeing practitioners',
      color: '#F59E0B',
      steps: [
        { id: 'sel-course', type: 'course', courseId: 'SEL', title: 'Social & Emotional Learning', description: 'Master SEL facilitation for development contexts.' },
        { id: 'media-course', type: 'course', courseId: 'media', title: 'Media, Communication & Development', description: 'BCC strategy, storytelling, and campaign design.' },
        { id: 'epi-lab', type: 'lab', title: 'Epidemiology Lab', description: 'Analyze disease surveillance data.' },
        { id: 'outbreak-game', type: 'game', title: 'Outbreak Simulation Game', description: 'Respond to a public health emergency scenario.' }
      ],
      milestones: [
        { afterStep: 'sel-course', label: 'SEL Certified', badge: true },
        { afterStep: 'outbreak-game', label: 'Health & Comms Specialist', badge: true, credential: true }
      ]
    }
  };

  // ── Progress Reading ────────────────────────────────────────────────
  // Read completion state from localStorage (course-progress.js format)
  function getCourseProgress(courseId) {
    try {
      var raw = localStorage.getItem('impactmojo_course_progress_' + courseId);
      if (!raw) return 0;
      var data = JSON.parse(raw);
      return data.percentage || 0;
    } catch (e) { return 0; }
  }

  // Lab/game completion tracked separately
  function getStepCompletion(stepId) {
    try {
      var state = JSON.parse(localStorage.getItem(STORAGE_KEY) || '{}');
      return state[stepId] === true;
    } catch (e) { return false; }
  }

  function markStepComplete(stepId) {
    try {
      var state = JSON.parse(localStorage.getItem(STORAGE_KEY) || '{}');
      state[stepId] = true;
      localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
    } catch (e) {}
  }

  // ── Pathway Progress Calculator ─────────────────────────────────────
  function getPathwayProgress(pathwayId) {
    var pw = PATHWAYS[pathwayId];
    if (!pw) return { completed: 0, total: 0, percentage: 0, steps: [], currentStep: null, milestones: [] };

    var total = pw.steps.length;
    var completed = 0;
    var stepStates = [];
    var currentStep = null;

    pw.steps.forEach(function (step) {
      var done = false;
      if (step.courseId) {
        done = getCourseProgress(step.courseId) >= 100;
      } else {
        done = getStepCompletion(step.id);
      }
      if (done) completed++;
      else if (!currentStep) currentStep = step;
      stepStates.push({ id: step.id, title: step.title, type: step.type, done: done });
    });

    // Calculate milestone states
    var milestoneStates = [];
    pw.milestones.forEach(function (m) {
      var stepIdx = pw.steps.findIndex(function (s) { return s.id === m.afterStep; });
      var allDone = stepIdx >= 0 && stepStates.slice(0, stepIdx + 1).every(function (s) { return s.done; });
      milestoneStates.push({ label: m.label, earned: allDone, credential: m.credential || false, afterStep: m.afterStep });
    });

    return {
      completed: completed,
      total: total,
      percentage: total ? Math.round((completed / total) * 100) : 0,
      steps: stepStates,
      currentStep: currentStep,
      milestones: milestoneStates
    };
  }

  // ── Pathway Card Renderer ───────────────────────────────────────────
  function renderPathwayCard(pathwayId) {
    var pw = PATHWAYS[pathwayId];
    if (!pw) return '';

    var progress = getPathwayProgress(pathwayId);
    var pct = progress.percentage;
    var earnedMilestones = progress.milestones.filter(function (m) { return m.earned; }).length;

    var stepIcons = { course: '📖', lab: '🔬', game: '🎮' };

    var stepsHtml = progress.steps.map(function (s, i) {
      var icon = stepIcons[s.type] || '•';
      var cls = s.done ? 'imx-pw-step-done' : 'imx-pw-step-pending';
      return '<div class="imx-pw-step ' + cls + '">' +
        '<span class="imx-pw-step-num">' + (i + 1) + '</span>' +
        '<span class="imx-pw-step-icon">' + icon + '</span>' +
        '<span class="imx-pw-step-title">' + s.title + '</span>' +
        (s.done ? '<svg class="imx-pw-check" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#10B981" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg>' : '') +
      '</div>';
    }).join('');

    var milestonesHtml = progress.milestones.map(function (m) {
      var cls = m.earned ? 'imx-pw-milestone-earned' : 'imx-pw-milestone-locked';
      return '<span class="imx-pw-milestone ' + cls + '">' +
        (m.earned ? '★ ' : '☆ ') + m.label +
        (m.credential ? ' (Credential)' : '') +
      '</span>';
    }).join('');

    return '<div class="imx-pw-card" data-pathway="' + pathwayId + '" style="--pw-color:' + pw.color + ';">' +
      '<div class="imx-pw-card-header">' +
        '<div class="imx-pw-card-title">' + pw.name + '</div>' +
        '<div class="imx-pw-card-track">' + pw.track + '</div>' +
      '</div>' +
      '<p class="imx-pw-card-desc">' + pw.description + '</p>' +
      '<div class="imx-pw-card-audience"><strong>For:</strong> ' + pw.audience + '</div>' +
      '<div class="imx-pw-progress-bar"><div class="imx-pw-progress-fill" style="width:' + pct + '%;background:' + pw.color + ';"></div></div>' +
      '<div class="imx-pw-progress-label">' + pct + '% complete · ' + progress.completed + '/' + progress.total + ' steps · ' + earnedMilestones + ' milestones</div>' +
      '<div class="imx-pw-steps">' + stepsHtml + '</div>' +
      '<div class="imx-pw-milestones">' + milestonesHtml + '</div>' +
      (progress.currentStep ? '<div class="imx-pw-next"><strong>Next:</strong> ' + progress.currentStep.title + '</div>' : '<div class="imx-pw-complete-badge" style="color:' + pw.color + ';">✔ Pathway Complete!</div>') +
    '</div>';
  }

  // ── Featured paid track (assessed, verifiable credential) ───────────
  // A pre-built, paid journey shown alongside the free credential pathways.
  // No progress UI — it links out to the product page.
  function renderPaidCard() {
    return '<a class="imx-pw-paid-card" href="/ai-for-me-certificate.html" ' +
      'style="display:flex;flex-direction:column;text-decoration:none;color:var(--text-primary);' +
      'background:var(--card-bg);border:1px solid #F59E0B;border-radius:14px;padding:1.25rem 1.5rem;position:relative;">' +
      '<span style="position:absolute;top:1rem;right:1.1rem;font-size:0.58rem;font-weight:700;letter-spacing:0.6px;text-transform:uppercase;background:#B45309;color:#fff;padding:0.2rem 0.55rem;border-radius:5px;">Paid · Verified</span>' +
      '<div style="font-weight:700;font-size:1.05rem;margin-bottom:0.15rem;color:var(--text-primary);">AI for M&E — Assessed Track</div>' +
      '<div style="font-size:0.78rem;color:var(--text-secondary);margin-bottom:0.6rem;">Monitoring, Evaluation & Learning</div>' +
      '<p style="font-size:0.85rem;color:var(--text-secondary);line-height:1.5;margin:0 0 0.75rem;">A pre-built, assessed path — the AI for Impact course, the Counterfactual game, the Critiquing Evidence pack and the AI Agents module — capstone-reviewed, with a verifiable credential you can prove online.</p>' +
      '<div style="margin-top:auto;display:flex;align-items:center;justify-content:space-between;gap:0.5rem;">' +
        '<span style="font-weight:700;color:var(--text-primary);">₹2,499 <span style="font-weight:400;font-size:0.75rem;color:var(--text-secondary);">one-time</span></span>' +
        '<span style="font-size:0.8rem;font-weight:600;color:#fff;background:#B45309;padding:0.3rem 0.7rem;border-radius:6px;">View the track →</span>' +
      '</div>' +
    '</a>';
  }

  // ── Render All Pathways ─────────────────────────────────────────────
  function renderPathways(containerId) {
    var container = document.getElementById(containerId);
    if (!container) return;

    var html = renderPaidCard();
    Object.keys(PATHWAYS).forEach(function (id) {
      html += renderPathwayCard(id);
    });
    container.innerHTML = html;

    // Add click-to-expand for step details
    container.querySelectorAll('.imx-pw-card').forEach(function (card) {
      var steps = card.querySelector('.imx-pw-steps');
      if (steps) {
        steps.style.display = 'none';
        card.querySelector('.imx-pw-card-header').style.cursor = 'pointer';
        card.querySelector('.imx-pw-card-header').addEventListener('click', function () {
          steps.style.display = steps.style.display === 'none' ? 'block' : 'none';
        });
      }
    });
  }

  // ── Pathway Recommendation ──────────────────────────────────────────
  // Returns sorted pathways based on existing progress (most started first)
  function recommendPathways() {
    var scored = Object.keys(PATHWAYS).map(function (id) {
      var p = getPathwayProgress(id);
      return { id: id, pathway: PATHWAYS[id], progress: p, score: p.percentage > 0 && p.percentage < 100 ? 100 + p.percentage : p.percentage };
    });
    scored.sort(function (a, b) { return b.score - a.score; });
    return scored;
  }

  // ── Inject Pathway Progress into Track Modal ────────────────────────
  function enhanceTrackModal() {
    var origOpen = window.IMPACTMOJO && window.IMPACTMOJO.openTrack;
    if (!origOpen) return;

    window.IMPACTMOJO.openTrack = function (trackName) {
      origOpen(trackName);

      // Find pathways for this track
      var trackPathways = Object.keys(PATHWAYS).filter(function (id) {
        return PATHWAYS[id].track === trackName;
      });
      if (!trackPathways.length) return;

      // Inject pathway progress into modal
      var modal = document.getElementById('imxTrackModal');
      if (!modal) return;
      var body = modal.querySelector('.modal-body');
      if (!body) return;

      // Remove old pathway section if exists
      var old = body.querySelector('.imx-pw-modal-section');
      if (old) old.remove();

      var section = document.createElement('div');
      section.className = 'imx-pw-modal-section';
      section.innerHTML = '<div style="margin-top:1.5rem;padding-top:1rem;border-top:1px solid var(--border-color);">' +
        '<div style="font-size:0.7rem;text-transform:uppercase;letter-spacing:0.08em;color:var(--text-muted);font-weight:600;margin-bottom:0.75rem;">Learning Pathways</div>' +
        '<div id="imxModalPathways"></div>' +
      '</div>';
      body.appendChild(section);

      var html = '';
      trackPathways.forEach(function (id) {
        var pw = PATHWAYS[id];
        var p = getPathwayProgress(id);
        html += '<div style="padding:0.75rem;background:var(--hover-bg);border-radius:8px;margin-bottom:0.5rem;">' +
          '<div style="display:flex;justify-content:space-between;align-items:center;">' +
            '<div><strong style="font-size:0.9rem;">' + pw.name + '</strong>' +
            '<div style="font-size:0.75rem;color:var(--text-muted);">' + pw.audience + '</div></div>' +
            '<span style="font-size:0.8rem;font-weight:600;color:' + pw.color + ';">' + p.percentage + '%</span>' +
          '</div>' +
          '<div style="height:3px;background:var(--border-color);border-radius:2px;margin-top:0.5rem;"><div style="height:100%;border-radius:2px;background:' + pw.color + ';width:' + p.percentage + '%;transition:width 0.3s;"></div></div>' +
          '<div style="display:flex;gap:0.3rem;flex-wrap:wrap;margin-top:0.5rem;">' +
            p.milestones.map(function (m) {
              return '<span style="font-size:0.65rem;padding:0.15rem 0.4rem;border-radius:10px;background:' + (m.earned ? pw.color + '20' : 'var(--hover-bg)') + ';color:' + (m.earned ? pw.color : 'var(--text-muted)') + ';font-weight:600;">' + (m.earned ? '★ ' : '☆ ') + m.label + '</span>';
            }).join('') +
          '</div>' +
        '</div>';
      });
      section.querySelector('#imxModalPathways').innerHTML = html;
    };
  }

  // ── Init ────────────────────────────────────────────────────────────
  function imxPathwaysInit() {
    // Enhance track modal with pathway progress
    enhanceTrackModal();

    // Render pathways section if container exists (for dedicated page)
    renderPathways('pathwaysContainer');

    // Inject pathway progress summary into homepage track cards
    document.querySelectorAll('.imx-track-card[data-track]').forEach(function (card) {
      var trackName = card.getAttribute('data-track');
      var trackPathways = Object.keys(PATHWAYS).filter(function (id) {
        return PATHWAYS[id].track === trackName;
      });
      if (!trackPathways.length) return;

      // Show first pathway progress on card
      var pw = PATHWAYS[trackPathways[0]];
      var p = getPathwayProgress(trackPathways[0]);
      if (p.percentage === 0) return;

      var existing = card.querySelector('.imx-pw-card-mini');
      if (existing) return;

      var mini = document.createElement('div');
      mini.className = 'imx-pw-card-mini';
      mini.innerHTML = '<div style="font-size:0.7rem;font-weight:600;color:' + pw.color + ';">' + pw.name + '</div>' +
        '<div style="display:flex;gap:0.3rem;margin-top:0.25rem;">' +
        p.milestones.map(function (m) {
          return '<span style="font-size:0.6rem;color:' + (m.earned ? pw.color : 'var(--text-muted)') + ';">' + (m.earned ? '★' : '☆') + '</span>';
        }).join('') +
        '</div>';
      card.appendChild(mini);
    });
  }
  // Lazy-loaded after DOMContentLoaded, so run now if the DOM is already ready.
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', imxPathwaysInit);
  else imxPathwaysInit();

  // ── Public API ──────────────────────────────────────────────────────
  window.IMPACTMOJO = window.IMPACTMOJO || {};
  window.IMPACTMOJO.pathways = {
    PATHWAYS: PATHWAYS,
    getPathwayProgress: getPathwayProgress,
    renderPathways: renderPathways,
    renderPathwayCard: renderPathwayCard,
    recommendPathways: recommendPathways,
    markStepComplete: markStepComplete
  };
})();
