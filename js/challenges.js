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
            (ch.partnerOrg ? '<div class="ch-card-partner">Partner: ' + escapeHTML(ch.partnerOrg) + '</div>' : '') +
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
            submissionHtml =
                '<div class="ch-submitted-state">' +
                    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>' +
                    '<h4>Challenge Submitted!</h4>' +
                    '<p>Your response was submitted on ' + escapeHTML(submissions[ch.id].submittedAt) + '.</p>' +
                    '<button class="ch-btn ch-btn-secondary" style="margin-top:1rem" onclick="window._challengeViewSubmission(\'' + ch.id + '\')">View My Submission</button>' +
                '</div>';
        } else {
            submissionHtml =
                '<div class="ch-submit-section">' +
                    '<h3><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="18" height="18"><path d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"/></svg> Your Response</h3>' +
                    '<textarea class="ch-textarea" id="challengeResponse" placeholder="' + escapeHTML(ch.submissionTemplate || 'Write your response here...') + '">' + escapeHTML(draft) + '</textarea>' +
                    '<div class="ch-char-count"><span id="charCount">' + (draft ? draft.length : 0) + '</span> characters (min 200)</div>' +
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
                (ch.partnerOrg ? '<div class="ch-card-partner" style="margin-top:0.25rem">Partner: ' + escapeHTML(ch.partnerOrg) + '</div>' : '') +
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

    function submitChallenge(challengeId) {
        var textarea = document.getElementById('challengeResponse');
        if (!textarea) return;

        var text = textarea.value.trim();
        if (text.length < 200) {
            alert('Please write at least 200 characters before submitting.');
            return;
        }

        var ch = challenges.find(function (c) { return c.id === challengeId; });
        var btn = document.getElementById('submitChallengeBtn');
        if (btn) {
            btn.disabled = true;
            btn.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="16" height="16" style="animation:spin 1s linear infinite"><path d="M12 2v4m0 12v4m-7.07-3.93l2.83-2.83m8.48-8.48l2.83-2.83M2 12h4m12 0h4m-3.93 7.07l-2.83-2.83M7.76 7.76L4.93 4.93"/></svg> Submitting...';
        }

        var now = new Date().toLocaleString();
        submissions[challengeId] = {
            text: text,
            submittedAt: now,
            status: 'pending'
        };
        saveSubmissions();

        // Clear draft
        delete drafts[challengeId];
        saveDrafts();

        // Submit to Netlify Forms (email notification)
        var formData = new FormData();
        formData.append('form-name', NETLIFY_FORM_NAME);
        formData.append('challenge_id', challengeId);
        formData.append('challenge_title', ch ? ch.title : '');
        formData.append('challenge_track', ch ? ch.trackLabel : '');
        formData.append('challenge_difficulty', ch ? ch.difficulty : '');
        formData.append('submission_text', text);
        formData.append('submitted_at', new Date().toISOString());

        fetch('/', {
            method: 'POST',
            body: new URLSearchParams(formData).toString(),
            headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
        }).catch(function () { /* silent — localStorage is primary fallback */ });

        // Sync to Supabase (DB record)
        syncSubmission(challengeId, text);

        // Show success
        setTimeout(function () {
            closeDetail();
            renderGrid();
            // Reopen to show submitted state
            setTimeout(function () { openDetail(challengeId); }, 300);
        }, 800);
    }

    async function syncSubmission(challengeId, text) {
        var sb = getSupabase();
        if (!sb) return;
        var user = await getUser();
        if (!user) return;

        try {
            await sb.from('challenge_submissions').upsert({
                challenge_id: challengeId,
                user_id: user.id,
                submission_text: text,
                submission_status: 'pending',
                submitted_at: new Date().toISOString()
            }, { onConflict: 'challenge_id,user_id' });
        } catch (e) {
            // Silent — local storage is primary
        }
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
