/**
 * ImpactMojo Live Case Challenges
 * Loads challenges from data/challenges.json, renders cards with filters,
 * detail view with case context + rubric, and a submission form.
 * Submissions stored in localStorage with optional Supabase sync.
 */
(function () {
    'use strict';

    var SUPABASE_URL = window.ImpactMojoConfig.SUPABASE_URL;
    var SUPABASE_ANON_KEY = window.ImpactMojoConfig.SUPABASE_ANON_KEY;
    var STORAGE_KEY = 'impactmojo_challenge_submissions';
    var DRAFT_KEY = 'impactmojo_challenge_drafts';
    var SELF_ASSESS_KEY = 'impactmojo_challenge_selfassess';

    var challenges = [];
    var submissions = {};
    var drafts = {};
    var currentFilter = 'all';
    var supabaseClient = null;
    var currentUser = null;

    var TRACK_COLORS = {
        mel: '#10B981',
        data_technology: '#6366F1',
        gender_equity: '#EC4899',
        policy_economics: '#F59E0B',
        philosophy_law: '#8B5CF6',
        health_comm: '#0EA5E9'
    };

    var TRACK_ICONS = {
        mel: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="20" height="20"><path d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>',
        data_technology: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="20" height="20"><path d="M9 17v-2m3 2v-4m3 4v-6m2 10H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>',
        gender_equity: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="20" height="20"><path d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0z"/></svg>',
        policy_economics: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="20" height="20"><path d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"/></svg>',
        philosophy_law: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="20" height="20"><path d="M3 6l3 1m0 0l-3 9a5.002 5.002 0 006.001 0M6 7l3 9M6 7l6-2m6 2l3-1m-3 1l-3 9a5.002 5.002 0 006.001 0M18 7l3 9m-3-9l-6-2m0-2v2m0 16V5m0 16H9m3 0h3"/></svg>',
        health_comm: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="20" height="20"><path d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/></svg>'
    };

    var TIER_HIERARCHY = { explorer: 0, practitioner: 1, professional: 2, organization: 3 };

    // ---- Supabase (optional) ----
    function getSupabase() {
        if (supabaseClient) return supabaseClient;
        // Reuse the shared client created by auth.js to avoid multiple
        // GoTrueClient instances racing on token refresh
        if (window.supabaseClient) {
            supabaseClient = window.supabaseClient;
            return supabaseClient;
        }
        // Fallback: create our own only if auth.js hasn't loaded yet
        if (window.supabase && window.supabase.createClient) {
            supabaseClient = window.supabase.createClient(SUPABASE_URL, SUPABASE_ANON_KEY, {
                auth: { persistSession: true, storageKey: 'impactmojo-auth', storage: window.localStorage }
            });
        }
        return supabaseClient;
    }

    async function getUser() {
        if (currentUser) return currentUser;
        var sb = getSupabase();
        if (!sb) return null;
        try {
            var result = await sb.auth.getUser();
            currentUser = result.data.user;
            return currentUser;
        } catch (e) { return null; }
    }

    async function getUserTier() {
        var sb = getSupabase();
        var user = await getUser();
        if (!sb || !user) return null;
        try {
            var result = await sb.from('profiles').select('subscription_tier').eq('id', user.id).single();
            return result.data ? result.data.subscription_tier : 'explorer';
        } catch (e) { return 'explorer'; }
    }

    function hasTierAccess(requiredTier, userTier) {
        if (!requiredTier || requiredTier === 'explorer') return true;
        if (!userTier) return false;
        return (TIER_HIERARCHY[userTier] || 0) >= (TIER_HIERARCHY[requiredTier] || 0);
    }

    // ---- Local Storage ----
    function loadLocal() {
        try {
            submissions = JSON.parse(localStorage.getItem(STORAGE_KEY)) || {};
            drafts = JSON.parse(localStorage.getItem(DRAFT_KEY)) || {};
        } catch (e) {
            submissions = {};
            drafts = {};
        }
    }

    var selfAssessments = {};
    try { selfAssessments = JSON.parse(localStorage.getItem(SELF_ASSESS_KEY)) || {}; } catch (e) { selfAssessments = {}; }
    function saveSelfAssessments() {
        try { localStorage.setItem(SELF_ASSESS_KEY, JSON.stringify(selfAssessments)); } catch (e) { /* quota */ }
    }

    function saveSubmissions() {
        try { localStorage.setItem(STORAGE_KEY, JSON.stringify(submissions)); } catch (e) { /* quota */ }
    }

    function saveDrafts() {
        try { localStorage.setItem(DRAFT_KEY, JSON.stringify(drafts)); } catch (e) { /* quota */ }
    }

    // ---- Load Challenges ----
    function loadChallenges() {
        var controller = window.AbortController ? new AbortController() : null;
        var timeoutId = controller ? setTimeout(function () { controller.abort(); }, 10000) : null;

        fetch('data/challenges.json', controller ? { signal: controller.signal } : {})
            .then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); })
            .then(function (data) {
                challenges = data;
                renderGrid();
                setupFilters();
            })
            .catch(function (e) {
                var grid = document.getElementById('challengeGrid');
                if (grid) {
                    grid.innerHTML = '<div class="ch-empty"><div class="ch-empty-icon">⚠️</div><div class="ch-empty-text">Could not load challenges. Please refresh.</div></div>';
                }
            })
            .finally(function () { if (timeoutId) clearTimeout(timeoutId); });
    }

    // ---- Render Cards ----
    function renderGrid() {
        var grid = document.getElementById('challengeGrid');
        if (!grid) return;

        var filtered = challenges.filter(function (ch) {
            if (currentFilter === 'all') return true;
            if (currentFilter === ch.difficulty) return true;
            if (currentFilter === ch.track) return true;
            if (currentFilter === ch.requiredTier) return true;
            return false;
        });

        if (filtered.length === 0) {
            grid.innerHTML = '<div class="ch-empty"><div class="ch-empty-icon">🔍</div><div class="ch-empty-text">No challenges match this filter.</div></div>';
            return;
        }

        // On the unfiltered view, group by difficulty with section headers so
        // the page reads as a laddered path instead of one uniform card wall.
        if (currentFilter === 'all') {
            var LEVELS = [
                ['beginner', 'Start here', 'Scoped, confidence-building cases — a first rep for each skill.'],
                ['intermediate', 'Build range', 'Messier briefs with competing constraints, like the real thing.'],
                ['advanced', 'Test yourself', 'High-ambiguity cases that reward judgement, not templates.']
            ];
            var html = '';
            LEVELS.forEach(function (lv) {
                var group = filtered.filter(function (ch) { return ch.difficulty === lv[0]; });
                if (!group.length) return;
                html += '<div class="ch-group-head ch-group-' + lv[0] + '">' +
                    '<h2>' + lv[1] + ' <span class="ch-group-count">' + group.length + '</span></h2>' +
                    '<p>' + lv[2] + '</p></div>' +
                    '<div class="ch-group-grid">' + group.map(renderCard).join('') + '</div>';
            });
            var rest = filtered.filter(function (ch) {
                return ['beginner', 'intermediate', 'advanced'].indexOf(ch.difficulty) === -1;
            });
            if (rest.length) html += '<div class="ch-group-grid">' + rest.map(renderCard).join('') + '</div>';
            grid.innerHTML = html;
        } else {
            grid.innerHTML = '<div class="ch-group-grid">' + filtered.map(renderCard).join('') + '</div>';
        }

        // Bind click handlers
        grid.querySelectorAll('.ch-card').forEach(function (card) {
            card.addEventListener('click', function () {
                var id = card.getAttribute('data-id');
                openDetail(id);
            });
        });
    }

    function renderCard(ch) {
        var color = TRACK_COLORS[ch.track] || '#64748B';
        var icon = TRACK_ICONS[ch.track] || '';
        var isSubmitted = !!submissions[ch.id];
        var tierLabel = ch.requiredTier === 'explorer' ? 'Free' : ch.requiredTier.charAt(0).toUpperCase() + ch.requiredTier.slice(1) + '+';
        var tierBadgeClass = ch.requiredTier === 'explorer' ? 'ch-badge-free' : 'ch-badge-practitioner';
        var lockHtml = ch.requiredTier !== 'explorer'
            ? '<div class="ch-card-lock"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0110 0v4"/></svg></div>'
            : '';

        return '<div class="ch-card' + (isSubmitted ? ' ch-card-submitted' : '') + '" data-id="' + ch.id + '">' +
            lockHtml +
            '<div class="ch-card-header">' +
                '<div class="ch-card-icon" style="background:' + color + '">' + icon + '</div>' +
                '<div class="ch-card-title">' + escapeHTML(ch.title) + '</div>' +
            '</div>' +
            '<div class="ch-card-badges">' +
                '<span class="ch-badge ch-badge-track">' + escapeHTML(ch.trackLabel) + '</span>' +
                '<span class="ch-badge ch-badge-' + ch.difficulty + '">' + ch.difficulty + '</span>' +
                '<span class="ch-badge ' + tierBadgeClass + '">' + tierLabel + '</span>' +
                (isSubmitted ? '<span class="ch-badge ch-badge-free">✓ Submitted</span>' : '') +
            '</div>' +
            '<div class="ch-card-desc">' + escapeHTML(ch.description) + '</div>' +
            '<div class="ch-card-meta">' +
                '<span><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg> ' + ch.durationMinutes + ' min</span>' +
                '<span><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 12l2 2 4-4"/><rect x="3" y="3" width="18" height="18" rx="2"/></svg> ' + ch.rubric.length + ' criteria</span>' +
            '</div>' +
            (ch.partnerOrg ? '<div class="ch-card-partner">Case setting: ' + escapeHTML(ch.partnerOrg) + '</div>' : '') +
        '</div>';
    }

    // ---- Filters ----
    function setupFilters() {
        var container = document.getElementById('challengeFilters');
        if (!container) return;

        container.querySelectorAll('.ch-filter-btn').forEach(function (btn) {
            btn.addEventListener('click', function () {
                container.querySelectorAll('.ch-filter-btn').forEach(function (b) { b.classList.remove('active'); });
                btn.classList.add('active');
                currentFilter = btn.getAttribute('data-filter');
                renderGrid();
            });
        });
    }

    // ---- Detail View ----
    function openDetail(challengeId) {
        var ch = challenges.find(function (c) { return c.id === challengeId; });
        if (!ch) return;

        var overlay = document.getElementById('challengeDetail');
        var content = document.getElementById('challengeDetailContent');
        if (!overlay || !content) return;

        var color = TRACK_COLORS[ch.track] || '#64748B';
        var isSubmitted = !!submissions[ch.id];
        var draft = drafts[ch.id] || '';
        var tierLabel = ch.requiredTier === 'explorer' ? 'Free' : ch.requiredTier.charAt(0).toUpperCase() + ch.requiredTier.slice(1) + '+';

        var rubricRows = ch.rubric.map(function (r) {
            return '<tr><td>' + escapeHTML(r.criterion) + '</td><td class="ch-rubric-weight">' + r.weight + '%</td></tr>';
        }).join('');

        var resourceIcon = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>';
        var resourceItems = (ch.resources || []).map(function (r) {
            var hasLink = r.url && r.url !== '#';
            if (hasLink) {
                return '<li><a href="' + escapeHTML(r.url) + '" target="_blank" rel="noopener noreferrer">' + resourceIcon + ' ' + escapeHTML(r.label) + '</a></li>';
            }
            // Placeholder resource — render as non-clickable so users aren't sent to a dead link.
            return '<li><span class="ch-resource-pending">' + resourceIcon + ' ' + escapeHTML(r.label) + ' <em>(coming soon)</em></span></li>';
        }).join('');

        var outcomeItems = ch.learningOutcomes.map(function (o) {
            return '<li>' + escapeHTML(o) + '</li>';
        }).join('');

        var submissionHtml = '';
        if (isSubmitted) {
            var sa = selfAssessments[ch.id];
            var saRows = ch.rubric.map(function (r, i) {
                var current = sa && sa.levels ? (sa.levels[i] || 0) : 0;
                var opts = ['Not yet addressed', 'Partially addressed', 'Addressed well', 'Addressed excellently'].map(function (label, v) {
                    return '<option value="' + v + '"' + (v === current ? ' selected' : '') + '>' + label + '</option>';
                }).join('');
                return '<tr><td>' + escapeHTML(r.criterion) + '</td><td style="white-space:nowrap">' + r.weight + '%</td>' +
                    '<td><select class="ch-sa-select" data-idx="' + i + '" aria-label="Self-rating for ' + escapeHTML(r.criterion) + '">' + opts + '</select></td></tr>';
            }).join('');
            var saScoreHtml = sa && typeof sa.score === 'number'
                ? '<p class="ch-sa-score" id="chSaScore">Your self-assessment: <strong>' + sa.score + '/100</strong> (saved on this device)</p>'
                : '<p class="ch-sa-score" id="chSaScore" style="display:none"></p>';
            submissionHtml =
                '<div class="ch-submitted-state">' +
                    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>' +
                    '<h4>Challenge Submitted!</h4>' +
                    '<p>Your response was submitted on ' + escapeHTML(submissions[ch.id].submittedAt) + '.</p>' +
                    '<p id="chCloudStatus" style="font-size:0.85rem;opacity:0.8"></p>' +
                    '<button class="ch-btn ch-btn-secondary" style="margin-top:1rem" onclick="window._challengeViewSubmission(\'' + ch.id + '\')">View My Submission</button>' +
                '</div>' +
                '<div class="ch-detail-section" id="chSelfAssess">' +
                    '<h3><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"/></svg> Score Yourself Against the Rubric</h3>' +
                    '<p style="font-size:0.9rem;opacity:0.85;margin:0 0 0.75rem">Re-read your submission with the evaluator’s eyes. Honest self-scoring is the fastest feedback loop there is — it saves to this device so you can compare attempts.</p>' +
                    '<table class="ch-rubric-table"><thead><tr><th>Criterion</th><th>Weight</th><th>Your rating</th></tr></thead><tbody>' + saRows + '</tbody></table>' +
                    saScoreHtml +
                    '<button class="ch-btn ch-btn-primary" style="margin-top:0.75rem" onclick="window._challengeSelfAssess(\'' + ch.id + '\')">Save Self-Assessment</button>' +
                '</div>';
        } else {
            submissionHtml =
                '<div class="ch-submit-section">' +
                    '<h3><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="18" height="18"><path d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"/></svg> Your Response</h3>' +
                    // Prefill the scaffold as the textarea's value (not placeholder) so learners
                    // can fill it in directly — but only when there is no saved draft to preserve.
                    '<textarea class="ch-textarea" id="challengeResponse" placeholder="Write your response here...">' + escapeHTML(draft || ch.submissionTemplate || '') + '</textarea>' +
                    '<div class="ch-char-count"><span id="charCount">' + ((draft || ch.submissionTemplate || '').length) + '</span> characters (min 200)</div>' +
                    '<label class="ch-email-label" for="challengeEmail">Your email <span>(required — it is the only way we can send your feedback back)</span></label>' +
                    '<input type="email" class="ch-email-input" id="challengeEmail" placeholder="you@example.org" autocomplete="email" required aria-required="true" value="' + escapeHTML(getSavedEmail()) + '">' +
                    '<label class="ch-email-label" for="challengeFile">Attach your work <span>(optional — PDF, Word, Excel, PowerPoint or an image, up to 8&nbsp;MB)</span></label>' +
                    '<input type="file" class="ch-file-input" id="challengeFile" accept="' + ACCEPT_TYPES + '">' +
                    '<div class="ch-file-name" id="challengeFileName" hidden></div>' +
                    '<p class="ch-submit-error" id="challengeError" role="alert" hidden></p>' +
                    '<div class="ch-submit-actions">' +
                        '<button class="ch-btn ch-btn-primary" id="submitChallengeBtn" onclick="window._challengeSubmit(\'' + ch.id + '\')">' +
                            '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="16" height="16"><path d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8"/></svg> Submit Response' +
                        '</button>' +
                        '<button class="ch-btn ch-btn-secondary" onclick="window._challengeSaveDraft(\'' + ch.id + '\')">Save Draft</button>' +
                    '</div>' +
                '</div>';
        }

        content.innerHTML =
            '<div class="ch-detail-header">' +
                '<button class="ch-detail-close" onclick="window._challengeClose()" aria-label="Close">&times;</button>' +
                '<div class="ch-card-badges" style="margin-bottom:0.75rem">' +
                    '<span class="ch-badge ch-badge-track">' + escapeHTML(ch.trackLabel) + '</span>' +
                    '<span class="ch-badge ch-badge-' + ch.difficulty + '">' + ch.difficulty + '</span>' +
                    '<span class="ch-badge ' + (ch.requiredTier === 'explorer' ? 'ch-badge-free' : 'ch-badge-practitioner') + '">' + tierLabel + '</span>' +
                '</div>' +
                '<div class="ch-detail-title">' + escapeHTML(ch.title) + '</div>' +
                (ch.partnerOrg ? '<div class="ch-card-partner" style="margin-top:0.25rem">Case setting: ' + escapeHTML(ch.partnerOrg) + '</div>' : '') +
                '<div class="ch-card-meta" style="margin-top:0.75rem;border:none;padding:0">' +
                    '<span><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="14" height="14"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg> ' + ch.durationMinutes + ' min</span>' +
                    '<span>' + ch.rubric.length + ' evaluation criteria</span>' +
                '</div>' +
            '</div>' +
            '<div class="ch-detail-body">' +
                '<div class="ch-detail-section">' +
                    '<h3><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg> Case Context</h3>' +
                    '<div class="ch-detail-context">' + escapeHTML(ch.caseContext) + '</div>' +
                '</div>' +

                '<div class="ch-detail-section">' +
                    '<h3><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M13 10V3L4 14h7v7l9-11h-7z"/></svg> Learning Outcomes</h3>' +
                    '<ul class="ch-detail-outcomes">' + outcomeItems + '</ul>' +
                '</div>' +

                (resourceItems ? '<div class="ch-detail-section"><h3><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg> Resources</h3><ul class="ch-resources-list">' + resourceItems + '</ul></div>' : '') +

                '<div class="ch-detail-section">' +
                    '<h3><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"/></svg> Evaluation Rubric</h3>' +
                    '<table class="ch-rubric-table"><thead><tr><th>Criterion</th><th>Weight</th></tr></thead><tbody>' + rubricRows + '</tbody></table>' +
                '</div>' +

                submissionHtml +
            '</div>';

        overlay.classList.add('open');
        document.body.style.overflow = 'hidden';

        // Prefill the optional feedback email from the signed-in account
        // (only when the field is empty — never overwrite a typed/saved value)
        if (!isSubmitted) {
            (async function () {
                var input = document.getElementById('challengeEmail');
                if (!input || input.value) return;
                var user = await getUser();
                if (user && user.email && input && !input.value) input.value = user.email;
            })();
        }

        // Cloud read-back: show that the submission is recorded to the account
        if (isSubmitted) {
            (async function () {
                var el = document.getElementById('chCloudStatus');
                if (!el) return;
                var sb = getSupabase();
                if (!sb) return;
                var user = await getUser();
                if (!user) {
                    el.textContent = 'Saved on this device. Sign in to record it to your account.';
                    return;
                }
                try {
                    var res = await sb.from('challenge_submissions')
                        .select('submission_status, submitted_at')
                        .eq('challenge_id', ch.id).eq('user_id', user.id).maybeSingle();
                    if (res && res.data) {
                        var when = res.data.submitted_at ? new Date(res.data.submitted_at).toLocaleDateString('en-IN', { year: 'numeric', month: 'long', day: 'numeric' }) : '';
                        el.textContent = 'Recorded to your account' + (when ? ' on ' + when : '') + ' — part of your challenge portfolio.';
                    } else {
                        el.textContent = 'Saved on this device (not yet synced to your account).';
                    }
                } catch (e) { /* status line is best-effort */ }
            })();
        }

        // Bind textarea autosave
        var textarea = document.getElementById('challengeResponse');
        if (textarea) {
            textarea.addEventListener('input', function () {
                var count = document.getElementById('charCount');
                if (count) count.textContent = textarea.value.length;
                // Autosave draft
                drafts[ch.id] = textarea.value;
                saveDrafts();
            });
        }
    }

    function closeDetail() {
        var overlay = document.getElementById('challengeDetail');
        if (overlay) {
            overlay.classList.remove('open');
            document.body.style.overflow = '';
        }
    }

    // ---- Submit ----
    var NETLIFY_FORM_NAME = 'challenge-submission';
    var EMAIL_STORAGE_KEY = 'im-challenge-email';
    var MAX_FILE_BYTES = 8 * 1024 * 1024;
    var ACCEPT_TYPES = '.pdf,.doc,.docx,.odt,.xls,.xlsx,.ppt,.pptx,.png,.jpg,.jpeg,.webp';
    var ALLOWED_EXT = /\.(pdf|docx?|odt|xlsx?|pptx?|png|jpe?g|webp)$/i;

    function getSavedEmail() {
        try { return localStorage.getItem(EMAIL_STORAGE_KEY) || ''; } catch (e) { return ''; }
    }

    /**
     * Show the chosen filename. Delegated from document rather than bound on
     * render, because the detail view is rebuilt from an HTML string each time
     * it opens, which would discard any listener attached to the input.
     */
    document.addEventListener('change', function (e) {
        if (!e.target || e.target.id !== 'challengeFile') return;
        var out = document.getElementById('challengeFileName');
        if (!out) return;
        var f = e.target.files && e.target.files[0];
        if (!f) { out.hidden = true; out.textContent = ''; return; }
        out.textContent = f.name + ' (' + (f.size / 1048576).toFixed(1) + ' MB)';
        out.hidden = false;
    });

    function showSubmitError(msg) {
        var el = document.getElementById('challengeError');
        if (el) { el.textContent = msg; el.hidden = false; }
        else { alert(msg); }
    }

    function resetSubmitButton() {
        var btn = document.getElementById('submitChallengeBtn');
        if (!btn) return;
        btn.disabled = false;
        btn.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="16" height="16">' +
            '<path d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8"/></svg> Submit Response';
    }

    function submitChallenge(challengeId) {
        var textarea = document.getElementById('challengeResponse');
        if (!textarea) return;

        var errEl = document.getElementById('challengeError');
        if (errEl) errEl.hidden = true;

        var text = textarea.value.trim();
        if (text.length < 200) {
            showSubmitError('Please write at least 200 characters before submitting.');
            return;
        }
        // The scaffold is prefilled as the textarea value, so it clears the 200
        // character minimum on its own -- both submissions received before this
        // check existed were the untouched template.
        var ch = challenges.find(function (c) { return c.id === challengeId; });
        if (ch && ch.submissionTemplate && text === ch.submissionTemplate.trim()) {
            showSubmitError('This is still the blank template — fill it in with your own response before submitting.');
            return;
        }

        var emailInput = document.getElementById('challengeEmail');
        var email = emailInput ? emailInput.value.trim() : '';
        if (!email) {
            showSubmitError('Please add your email — it is the only way we can send your feedback back.');
            if (emailInput) emailInput.focus();
            return;
        }
        if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
            showSubmitError('That email address doesn\'t look right — please check it.');
            if (emailInput) emailInput.focus();
            return;
        }
        try { localStorage.setItem(EMAIL_STORAGE_KEY, email); } catch (e) { /* private mode */ }

        var fileInput = document.getElementById('challengeFile');
        var file = fileInput && fileInput.files && fileInput.files[0] ? fileInput.files[0] : null;
        if (file) {
            if (file.size > MAX_FILE_BYTES) {
                showSubmitError('That file is ' + (file.size / 1048576).toFixed(1) + ' MB — the limit is 8 MB.');
                return;
            }
            if (!ALLOWED_EXT.test(file.name)) {
                showSubmitError('That file type is not accepted. Use a PDF, Word, Excel, PowerPoint or image file.');
                return;
            }
        }

        var btn = document.getElementById('submitChallengeBtn');
        if (btn) {
            btn.disabled = true;
            btn.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="16" height="16" style="animation:spin 1s linear infinite"><path d="M12 2v4m0 12v4m-7.07-3.93l2.83-2.83m8.48-8.48l2.83-2.83M2 12h4m12 0h4m-3.93 7.07l-2.83-2.83M7.76 7.76L4.93 4.93"/></svg> Submitting...';
        }

        var formData = new FormData();
        formData.append('form-name', NETLIFY_FORM_NAME);
        formData.append('challenge_id', challengeId);
        formData.append('challenge_title', ch ? ch.title : '');
        formData.append('challenge_track', ch ? ch.trackLabel : '');
        formData.append('challenge_difficulty', ch ? ch.difficulty : '');
        formData.append('submission_text', text);
        // Netlify sets the notification's Reply-To from a field named "email",
        // so replies from the inbox reach the submitter directly.
        formData.append('email', email);
        formData.append('submitted_at', new Date().toISOString());
        if (file) formData.append('attachment', file, file.name);

        // Two independent paths, because neither alone is sufficient. Netlify
        // Forms sends the notification email but runs submissions through a spam
        // filter that returns 200 on the ones it discards; /api/challenge-submit
        // writes the durable row and is not filtered. The submission counts as
        // delivered if either succeeds.
        var netlify = window.imxSubmitForm
            ? window.imxSubmitForm(formData, { multipart: !!file })
            : Promise.reject(new Error('form-submit helper not loaded'));

        var durable = storeSubmission(challengeId, ch, text, email, file);

        Promise.allSettled([netlify, durable]).then(function (results) {
            var delivered = results.some(function (r) { return r.status === 'fulfilled'; });

            if (!delivered) {
                resetSubmitButton();
                showSubmitError(
                    'We could not save your submission just now. Your text is kept in this browser — ' +
                    'please try again in a moment, or email it to hello@impactmojo.in.'
                );
                return;
            }

            // Only record it locally as submitted once something actually took it.
            submissions[challengeId] = { text: text, submittedAt: new Date().toLocaleString(), status: 'pending' };
            saveSubmissions();
            delete drafts[challengeId];
            saveDrafts();

            closeDetail();
            renderGrid();
            setTimeout(function () { openDetail(challengeId); }, 300);
        });
    }

    /**
     * Durable path: writes the row through the Netlify Function, which holds the
     * service role. challenge_submissions stays anon-denied, so the browser is
     * never given write access to it directly.
     */
    async function storeSubmission(challengeId, ch, text, email, file) {
        var payload = {
            challenge_id: challengeId,
            challenge_title: ch ? ch.title : '',
            submission_text: text,
            email: email,
            attachment_name: file ? file.name : null
        };
        // Resolve the session rather than reading the cached currentUser: it is
        // populated by an async call that may not have run yet, which would file
        // a signed-in learner's work as anonymous and break their upsert.
        var user = null;
        try { user = await getUser(); } catch (e) { user = null; }
        if (user && user.id) payload.user_id = user.id;

        return fetch('/api/challenge-submit', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        }).then(function (res) {
            if (!res.ok) throw new Error('challenge-submit returned ' + res.status);
            return res;
        });
    }

    function saveDraft(challengeId) {
        var textarea = document.getElementById('challengeResponse');
        if (!textarea) return;
        drafts[challengeId] = textarea.value;
        saveDrafts();

        var btn = event.target;
        var original = btn.textContent;
        btn.textContent = '✓ Draft Saved';
        setTimeout(function () { btn.textContent = original; }, 1500);
    }

    function viewSubmission(challengeId) {
        var sub = submissions[challengeId];
        if (!sub) return;

        var overlay = document.getElementById('challengeDetail');
        var content = document.getElementById('challengeDetailContent');
        var ch = challenges.find(function (c) { return c.id === challengeId; });
        if (!overlay || !content || !ch) return;

        content.innerHTML =
            '<div class="ch-detail-header">' +
                '<button class="ch-detail-close" onclick="window._challengeClose()" aria-label="Close">&times;</button>' +
                '<div class="ch-detail-title">My Submission: ' + escapeHTML(ch.title) + '</div>' +
                '<div class="ch-card-meta" style="margin-top:0.5rem;border:none;padding:0">' +
                    '<span>Submitted: ' + escapeHTML(sub.submittedAt) + '</span>' +
                    '<span>Status: ' + escapeHTML(sub.status) + '</span>' +
                '</div>' +
            '</div>' +
            '<div class="ch-detail-body">' +
                '<div class="ch-detail-context" style="white-space:pre-wrap;font-family:\'JetBrains Mono\',monospace;font-size:0.85rem">' + escapeHTML(sub.text) + '</div>' +
            '</div>';

        overlay.classList.add('open');
        document.body.style.overflow = 'hidden';
    }

    // ---- Utilities ----
    function escapeHTML(str) {
        var map = { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' };
        return String(str || '').replace(/[&<>"']/g, function (c) { return map[c]; });
    }

    // ---- Global Handlers ----
    window._challengeClose = closeDetail;
    window._challengeSelfAssess = function (challengeId) {
        var ch = challenges.find(function (c) { return c.id === challengeId; });
        if (!ch) return;
        var selects = document.querySelectorAll('#chSelfAssess .ch-sa-select');
        var levels = [];
        selects.forEach(function (s) { levels[parseInt(s.getAttribute('data-idx'), 10)] = parseInt(s.value, 10) || 0; });
        var score = 0;
        ch.rubric.forEach(function (r, i) { score += r.weight * ((levels[i] || 0) / 3); });
        score = Math.round(score);
        selfAssessments[challengeId] = { levels: levels, score: score, at: new Date().toISOString() };
        saveSelfAssessments();
        var el = document.getElementById('chSaScore');
        if (el) {
            el.style.display = '';
            el.innerHTML = 'Your self-assessment: <strong>' + score + '/100</strong> (saved on this device)';
        }
    };

    window._challengeSubmit = submitChallenge;
    window._challengeSaveDraft = saveDraft;
    window._challengeViewSubmission = viewSubmission;

    // Close overlay on backdrop click
    document.addEventListener('click', function (e) {
        var overlay = document.getElementById('challengeDetail');
        if (overlay && overlay.classList.contains('open') && e.target === overlay) {
            closeDetail();
        }
    });

    // Close on Escape
    document.addEventListener('keydown', function (e) {
        if (e.key === 'Escape') closeDetail();
    });

    // ---- Spin animation ----
    var spinStyle = document.createElement('style');
    spinStyle.textContent = '@keyframes spin{from{transform:rotate(0)}to{transform:rotate(360deg)}}';
    document.head.appendChild(spinStyle);

    // ---- Init ----
    function init() {
        loadLocal();
        loadChallenges();
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
