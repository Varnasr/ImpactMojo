/**
 * ImpactMojo Course Progress Tracking System
 * Version 1.1.0 - March 2026
 *
 * Tracks quiz completion per module, persists progress to localStorage
 * and syncs to Supabase user_progress table for authenticated users.
 * When all modules are complete, progress_percentage hits 100% and
 * the existing DB trigger auto-issues a certificate.
 *
 * Auth-aware completion flow:
 * - Anonymous users: prompted to sign up to claim certificate
 * - Explorer (free): certificate auto-issued, web-viewable
 * - Practitioner+: certificate + PDF download + portfolio display
 *
 * Progress migration: localStorage progress is synced to Supabase
 * when a user logs in, so anonymous progress is preserved.
 *
 * Usage: Add to any course page:
 *   <script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
 *   <script src="../../js/course-progress.js"></script>
 */

(function () {
    'use strict';

    // =========================================================
    // CONFIGURATION
    // =========================================================
    const SUPABASE_URL = window.ImpactMojoConfig.SUPABASE_URL;
    const SUPABASE_ANON_KEY = window.ImpactMojoConfig.SUPABASE_ANON_KEY;

    const COURSE_NAMES = {
        mel: 'Monitoring, Evaluation & Learning',
        dataviz: 'Data Visualization for Impact',
        devai: 'AI for Development',
        devecon: 'Development Economics',
        gandhi: "Gandhi's Political Thought",
        law: 'Law & Development',
        media: 'Media, Communication & Development',
        SEL: 'Social & Emotional Learning',
        sel: 'Social-Emotional Learning for Development Practice',
        poa: 'Politics of Aspiration',
        gender: 'Gender Studies: Feminisms, Power & Social Change',
        pubchoice: 'Public Choice: Decisions, Incentives & Institutions',
        pubpol: 'Public Policy: Process, Design & Governance in India',
        causal: 'Causal Inference for Development',
        livelihoods: 'Livelihoods in India: Rural, Urban, and Skills',
        powerBI: 'Power BI for Practitioners',
        intervention: 'Designing What Works: Development Interventions from Model to Scale',
        'nothing-about-us': 'Nothing About Us Without Us: Disability, Justice & Development',
        'nvc-rj': 'Nonviolence in Practice: Communication, Resistance & Repair'
    };

    // =========================================================
    // DETECT COURSE ID FROM URL
    // =========================================================
    function detectCourseId() {
        const path = window.location.pathname;
        const match = path.match(/\/courses\/([^/]+)/);
        return match ? match[1] : null;
    }

    const courseId = detectCourseId();
    if (!courseId || !COURSE_NAMES[courseId]) return;

    const STORAGE_KEY = 'impactmojo_course_progress_' + courseId;

    // =========================================================
    // STATE
    // =========================================================
    // How much of a module's quiz must be right for the module to count.
    //
    // This was a clean sweep: every graded question in the module correct.
    // With four questions per module across twelve modules, finishing a
    // course meant 48 correct answers with no allowance for one that simply
    // reads badly. A majority keeps the module meaningful without making a
    // single awkward question a wall.
    const PASS_RATIO = 0.75;                 // 3 of 4; 2 of 2; 5 of 6

    function questionsToPass(total) {
        return Math.max(1, Math.ceil(total * PASS_RATIO));
    }

    // Progress with partial credit inside a module.
    //
    // The headline number used to be completedModules / totalModules, which
    // moves only when a whole module lands — so a learner three questions
    // into a module saw nothing, and neither did their account page. This
    // gives each module a fractional score, capped at 1, and still reaches
    // 100 exactly when every module has passed. The certificate trigger fires
    // at >= 100, so the completion condition is unchanged.
    function overallPercentage() {
        var ids = Object.keys(moduleData);
        if (!ids.length) return 0;
        var earned = 0;
        for (var i = 0; i < ids.length; i++) {
            var m = moduleData[ids[i]];
            var need = questionsToPass(m.total);
            earned += Math.min(1, m.correct.size / need);
        }
        return Math.round((earned / ids.length) * 100);
    }

    let moduleData = {};    // { module1: { total: 4, correct: Set([0,1,2,3]) }, ... }
    let completedModules = new Set();
    let totalModules = 0;
    let supabaseClient = null;
    let syncTimeout = null;
    let currentUser = null;      // cached auth user
    let currentProfile = null;   // cached profile (for tier)

    // =========================================================
    // INIT SUPABASE (lazy, only if lib loaded)
    // =========================================================
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

    // =========================================================
    // AUTH HELPERS
    // =========================================================
    async function getAuthState() {
        var sb = getSupabase();
        if (!sb) return { user: null, profile: null };

        try {
            if (currentUser) return { user: currentUser, profile: currentProfile };

            var { data: { user } } = await sb.auth.getUser();
            if (!user) return { user: null, profile: null };

            currentUser = user;

            // Fetch profile for tier info
            var { data: profile } = await sb.from('profiles')
                .select('subscription_tier, display_name, full_name')
                .eq('id', user.id)
                .single();

            currentProfile = profile;
            return { user: user, profile: profile };
        } catch (e) {
            return { user: null, profile: null };
        }
    }

    function isPaidTier(tier) {
        return tier === 'practitioner' || tier === 'professional' || tier === 'organization';
    }

    // =========================================================
    // PROGRESS MIGRATION (localStorage → Supabase on login)
    // =========================================================
    async function migrateProgressOnLogin() {
        var sb = getSupabase();
        if (!sb) return;

        var { user } = await getAuthState();
        if (!user) return;

        // Check if we have local progress to migrate
        if (completedModules.size === 0) return;

        var percentage = overallPercentage();

        // Check if cloud already has progress for this course
        try {
            var { data: existing } = await sb.from('user_progress')
                .select('progress_percentage')
                .eq('user_id', user.id)
                .eq('course_id', courseId)
                .single();

            // Only migrate if local is ahead of cloud
            if (existing && existing.progress_percentage >= percentage) return;

            // Sync local progress to cloud
            await syncToSupabase();
        } catch (e) {
            // No existing record — sync will create one
            await syncToSupabase();
        }
    }

    // Listen for auth state changes (user logs in while on course page)
    function listenForAuthChanges() {
        var sb = getSupabase();
        if (!sb) return;

        sb.auth.onAuthStateChange(function (event) {
            if (event === 'SIGNED_IN') {
                // Reset cached auth state
                currentUser = null;
                currentProfile = null;
                // Migrate any localStorage progress to the new session
                migrateProgressOnLogin();
            } else if (event === 'SIGNED_OUT') {
                currentUser = null;
                currentProfile = null;
            }
        });
    }

    // =========================================================
    // SCAN DOM FOR MODULES & QUIZZES
    // =========================================================
    function scanModules() {
        const moduleSections = document.querySelectorAll('section[id^="module"]');
        moduleSections.forEach(function (section) {
            const id = section.id;  // e.g. "module1"
            const gradedQuestions = section.querySelectorAll('.quiz-question[data-correct]');
            if (gradedQuestions.length > 0) {
                moduleData[id] = {
                    total: gradedQuestions.length,
                    correct: new Set(),
                    element: section
                };
            }
        });
        totalModules = Object.keys(moduleData).length;
    }

    // =========================================================
    // LOCALSTORAGE PERSISTENCE
    // =========================================================
    function loadProgress() {
        try {
            var saved = JSON.parse(localStorage.getItem(STORAGE_KEY));
            if (saved && saved.completed) {
                saved.completed.forEach(function (id) {
                    if (moduleData[id]) {
                        completedModules.add(id);
                        // Fill all correct answers so UI shows as done
                        var mod = moduleData[id];
                        for (var i = 0; i < mod.total; i++) {
                            mod.correct.add(i);
                        }
                    }
                });
            }
        } catch (e) { /* ignore parse errors */ }
    }

    function saveProgress() {
        try {
            localStorage.setItem(STORAGE_KEY, JSON.stringify({
                courseId: courseId,
                completed: Array.from(completedModules),
                totalModules: totalModules,
                percentage: Math.round((completedModules.size / totalModules) * 100),
                updatedAt: new Date().toISOString()
            }));
        } catch (e) { /* ignore storage errors */ }
    }

    // =========================================================
    // SUPABASE SYNC (debounced)
    // =========================================================
    function queueSync() {
        if (syncTimeout) clearTimeout(syncTimeout);
        syncTimeout = setTimeout(syncToSupabase, 3000);
    }

    async function syncToSupabase() {
        var sb = getSupabase();
        if (!sb) return;

        try {
            var { data: { user } } = await sb.auth.getUser();
            if (!user) return;

            var percentage = overallPercentage();

            var isComplete = percentage >= 100;
            var now = new Date().toISOString();

            var { error: syncError } = await sb.from('user_progress').upsert({
                user_id: user.id,
                course_id: courseId,
                course_name: COURSE_NAMES[courseId],
                progress_percentage: percentage,
                last_accessed_at: now,
                started_at: now,
                completed_at: isComplete ? now : null,
                current_section: Array.from(completedModules).sort().pop() || null
            }, {
                onConflict: 'user_id,course_id'
            });

            // supabase-js RESOLVES with { data, error } rather than throwing, so
            // the catch below never saw a rejected write. Progress is still kept
            // in localStorage either way, but a cloud failure must be visible
            // somewhere or it stays invisible for months — which it did.
            if (syncError) {
                console.error('[CourseProgress] Cloud sync failed for ' + courseId +
                              ': ' + syncError.message);
            }
        } catch (e) {
            console.error('[CourseProgress] Cloud sync threw for ' + courseId + ':', e);
        }
    }

    // =========================================================
    // UI: PROGRESS BAR
    // =========================================================
    function createProgressBar() {
        var bar = document.createElement('div');
        bar.id = 'course-progress-bar';
        bar.innerHTML =
            '<div class="cpb-inner">' +
                '<div class="cpb-label">' +
                    '<span class="cpb-icon">' +
                        '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="16" height="16">' +
                            '<path d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>' +
                        '</svg>' +
                    '</span>' +
                    '<span class="cpb-text">Module Progress</span>' +
                    '<span class="cpb-count">0 / ' + totalModules + '</span>' +
                '</div>' +
                '<div class="cpb-track">' +
                    '<div class="cpb-fill" style="width: 0%"></div>' +
                '</div>' +
            '</div>';

        // Insert after reading-progress bar or at top of main-content
        var readingBar = document.getElementById('reading-progress');
        if (readingBar && readingBar.parentNode) {
            readingBar.parentNode.insertBefore(bar, readingBar.nextSibling);
        } else {
            var main = document.querySelector('.main-content');
            if (main) main.insertBefore(bar, main.firstChild);
        }
    }

    function updateProgressBar() {
        var count = completedModules.size;
        // The bar shows the same fractional figure that is written to the
        // database, so a learner mid-module sees the fill move rather than
        // nothing at all. The "n / total" count still reports whole modules
        // passed, which is what that label means.
        var pct = overallPercentage();

        var fill = document.querySelector('.cpb-fill');
        var countEl = document.querySelector('.cpb-count');

        if (fill) fill.style.width = pct + '%';
        if (countEl) countEl.textContent = count + ' / ' + totalModules + ' (' + pct + '%)';

        // Change color when complete
        if (pct >= 100) {
            var bar = document.getElementById('course-progress-bar');
            if (bar) bar.classList.add('cpb-complete');
        }
    }

    // =========================================================
    // UI: SIDEBAR CHECKMARKS
    // =========================================================
    function updateSidebarChecks() {
        completedModules.forEach(function (modId) {
            var link = document.querySelector('a.nav-link[href="#' + modId + '"]');
            if (link && !link.querySelector('.cpb-check')) {
                var check = document.createElement('span');
                check.className = 'cpb-check';
                check.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" width="14" height="14"><path d="M5 13l4 4L19 7"/></svg>';
                link.appendChild(check);
            }
        });
    }

    // =========================================================
    // UI: RESTORE QUIZ VISUAL STATE FOR COMPLETED MODULES
    // =========================================================
    function restoreQuizState() {
        completedModules.forEach(function (modId) {
            var section = document.getElementById(modId);
            if (!section) return;
            var questions = section.querySelectorAll('.quiz-question[data-correct]');
            questions.forEach(function (q) {
                var correct = q.dataset.correct;
                var options = q.querySelectorAll('.quiz-option');
                options.forEach(function (opt) {
                    if (opt.dataset.option === correct) {
                        opt.classList.add('correct');
                        var radio = opt.querySelector('input[type="radio"]');
                        if (radio) radio.checked = true;
                    }
                });
                var feedback = q.querySelector('.quiz-feedback');
                if (feedback) {
                    feedback.textContent = '\u2713 Correct! Well done.';
                    feedback.className = 'quiz-feedback show correct';
                }
                var btn = q.querySelector('.check-answer-btn');
                if (btn) {
                    btn.disabled = true;
                    btn.textContent = 'Completed';
                    btn.style.opacity = '0.6';
                }
            });
        });
    }

    // =========================================================
    // UI: TOAST NOTIFICATION
    // =========================================================
    function showToast(message, type) {
        var existing = document.getElementById('cpb-toast');
        if (existing) existing.remove();

        var toast = document.createElement('div');
        toast.id = 'cpb-toast';
        toast.className = 'cpb-toast' + (type === 'complete' ? ' cpb-toast-complete' : '');
        toast.innerHTML =
            '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="20" height="20">' +
                '<path d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>' +
            '</svg>' +
            '<span>' + message + '</span>';

        document.body.appendChild(toast);

        // Trigger animation
        requestAnimationFrame(function () {
            toast.classList.add('cpb-toast-show');
        });

        setTimeout(function () {
            toast.classList.remove('cpb-toast-show');
            setTimeout(function () { toast.remove(); }, 400);
        }, 3500);
    }

    // =========================================================
    // UI: COMPLETION MODAL (auth-aware)
    // =========================================================
    async function showCompletionModal() {
        var { user, profile } = await getAuthState();
        var tier = profile ? profile.subscription_tier : null;
        var name = profile ? (profile.display_name || profile.full_name || '') : '';

        var iconSvg =
            '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" width="64" height="64">' +
                '<path d="M4.26 10.147a60.436 60.436 0 00-.491 6.347A48.627 48.627 0 0112 20.904a48.627 48.627 0 018.232-4.41 60.46 60.46 0 00-.491-6.347m-15.482 0a50.57 50.57 0 00-2.658-.813A59.905 59.905 0 0112 3.493a59.902 59.902 0 0110.399 5.84c-.896.248-1.783.52-2.658.814m-15.482 0A50.697 50.697 0 0112 13.489a50.702 50.702 0 017.74-3.342M6.75 15a.75.75 0 100-1.5.75.75 0 000 1.5zm0 0v-3.675A55.378 55.378 0 0112 8.443m-7.007 11.55A5.981 5.981 0 006.75 15.75v-1.5"/>' +
            '</svg>';

        var body = '';

        if (!user) {
            // ── ANONYMOUS USER ──
            body =
                '<div class="cpb-completion-icon" style="color: #0EA5E9;">' + iconSvg + '</div>' +
                '<h3>Course Complete!</h3>' +
                '<p>Congratulations! You\'ve completed all modules in <strong>' + COURSE_NAMES[courseId] + '</strong>.</p>' +
                '<p class="cpb-completion-sub">Create a free account to claim your certificate. Your progress will be saved automatically.</p>' +
                '<a href="/signup.html" class="cpb-completion-btn cpb-btn-signup">Sign Up to Claim Certificate</a>' +
                '<button class="cpb-completion-btn cpb-btn-secondary" onclick="this.closest(\'#cpb-completion-overlay\').remove()">Maybe Later</button>' +
                '<p class="cpb-completion-login">Already have an account? <a href="/login.html">Log in</a></p>';
        } else if (isPaidTier(tier)) {
            // ── PRACTITIONER / PROFESSIONAL / ORGANIZATION ──
            body =
                '<div class="cpb-completion-icon">' + iconSvg + '</div>' +
                '<h3>Course Complete!</h3>' +
                '<p>' + (name ? 'Well done, <strong>' + name + '</strong>! ' : 'Congratulations! ') +
                    'You\'ve completed all modules in <strong>' + COURSE_NAMES[courseId] + '</strong>.</p>' +
                '<p class="cpb-completion-sub">Your certificate is being issued now. You can download the PDF and add it to your portfolio from your account page.</p>' +
                '<a href="/account.html" class="cpb-completion-btn">View Certificate</a>' +
                '<a href="/portfolio.html" class="cpb-completion-btn cpb-btn-secondary">Add to Portfolio</a>';
        } else {
            // ── EXPLORER (free tier) ──
            body =
                '<div class="cpb-completion-icon">' + iconSvg + '</div>' +
                '<h3>Course Complete!</h3>' +
                '<p>' + (name ? 'Well done, <strong>' + name + '</strong>! ' : 'Congratulations! ') +
                    'You\'ve completed all modules in <strong>' + COURSE_NAMES[courseId] + '</strong>.</p>' +
                '<p class="cpb-completion-sub">Your certificate has been issued! View it on your account page.</p>' +
                '<a href="/account.html" class="cpb-completion-btn">View Certificate</a>' +
                '<p class="cpb-completion-upgrade">Upgrade to <strong>Practitioner</strong> for PDF download & portfolio display. ' +
                    '<a href="/upgrade.html?from=course-completion">See what you unlock</a></p>';
        }

        var overlay = document.createElement('div');
        overlay.id = 'cpb-completion-overlay';
        overlay.innerHTML = '<div class="cpb-completion-modal">' + body + '</div>';

        // Close on overlay click (outside modal)
        overlay.addEventListener('click', function (e) {
            if (e.target === overlay) overlay.remove();
        });

        document.body.appendChild(overlay);
        requestAnimationFrame(function () {
            overlay.classList.add('cpb-overlay-show');
        });
    }

    // =========================================================
    // CORE: HANDLE QUIZ ANSWER (called from enhanced checkAnswer)
    // =========================================================
    function onQuizAnswered(questionEl, isCorrect) {
        if (!isCorrect) return;

        // Find which module this question belongs to
        var section = questionEl.closest('section[id^="module"]');
        if (!section) return;

        var modId = section.id;
        var mod = moduleData[modId];
        if (!mod || completedModules.has(modId)) return;

        // Find index of this question within the module's graded questions
        var gradedQuestions = Array.from(section.querySelectorAll('.quiz-question[data-correct]'));
        var idx = gradedQuestions.indexOf(questionEl);
        if (idx === -1) return;

        mod.correct.add(idx);

        // Record the answer even when the module is not finished. Progress is
        // fractional now, so a learner part-way through a module has something
        // real to show on /account.html, and we can see where people stop
        // rather than only who reached the end. queueSync debounces by 3s, so
        // a run of quick answers still costs one write.
        saveProgress();
        updateProgressBar();
        queueSync();

        // Module passed?
        if (mod.correct.size >= questionsToPass(mod.total)) {
            completedModules.add(modId);
            saveProgress();
            updateProgressBar();
            updateSidebarChecks();
            queueSync();

            var moduleNum = modId.replace('module', '');
            showToast('Module ' + moduleNum + ' complete!');

            // Check if entire course is done
            if (completedModules.size >= totalModules) {
                setTimeout(function () { showCompletionModal(); }, 1000);
            }
        }
    }

    // =========================================================
    // ENHANCE EXISTING checkAnswer FUNCTION
    // =========================================================
    function enhanceCheckAnswer() {
        var originalCheckAnswer = window.checkAnswer;

        window.checkAnswer = function (button) {
            var question = button.closest('.quiz-question');
            var correct = question ? question.dataset.correct : null;
            var selected = question ? question.querySelector('input[type="radio"]:checked') : null;

            // Call original function
            if (typeof originalCheckAnswer === 'function') {
                originalCheckAnswer(button);
            }

            // Notify progress system
            if (selected && correct && selected.value === correct) {
                onQuizAnswered(question, true);
            }
        };
    }

    // =========================================================
    // INJECT STYLES
    // =========================================================
    function injectStyles() {
        var style = document.createElement('style');
        style.textContent =
            /* Progress Bar */
            '#course-progress-bar {' +
                'position: fixed; top: 3px; left: 0; right: 0; z-index: 999;' +
                'padding: 8px 16px; background: rgba(15, 23, 42, 0.95);' +
                'border-bottom: 1px solid rgba(51, 65, 85, 0.5);' +
                'backdrop-filter: blur(12px); transition: all 0.3s ease;' +
            '}' +
            '.cpb-inner { max-width: 900px; margin: 0 auto; }' +
            '.cpb-label {' +
                'display: flex; align-items: center; gap: 8px;' +
                'margin-bottom: 6px; font-size: 0.75rem; color: #94A3B8;' +
            '}' +
            '.cpb-icon { display: flex; align-items: center; color: #0EA5E9; }' +
            '.cpb-text { flex: 1; font-weight: 500; }' +
            '.cpb-count { font-family: "JetBrains Mono", monospace; color: #0EA5E9; font-weight: 600; }' +
            '.cpb-track {' +
                'height: 4px; background: rgba(51, 65, 85, 0.8);' +
                'border-radius: 4px; overflow: hidden;' +
            '}' +
            '.cpb-fill {' +
                'height: 100%; border-radius: 4px;' +
                'background: linear-gradient(90deg, #0EA5E9, #6366F1);' +
                'transition: width 0.6s cubic-bezier(0.4, 0, 0.2, 1);' +
            '}' +
            '#course-progress-bar.cpb-complete .cpb-fill {' +
                'background: linear-gradient(90deg, #10B981, #0EA5E9);' +
            '}' +
            '#course-progress-bar.cpb-complete .cpb-count { color: #10B981; }' +

            /* Light mode */
            '[data-theme="light"] #course-progress-bar {' +
                'background: rgba(255, 255, 255, 0.95);' +
                'border-bottom-color: rgba(226, 232, 240, 0.8);' +
            '}' +
            '[data-theme="light"] .cpb-label { color: #64748B; }' +
            '[data-theme="light"] .cpb-track { background: #E2E8F0; }' +

            /* Sidebar checkmarks */
            '.cpb-check {' +
                'display: inline-flex; align-items: center; margin-left: auto;' +
                'color: #10B981; flex-shrink: 0;' +
            '}' +

            /* Reading-time estimates */
            '.cpb-time {' +
                'margin-left: 8px; font-size: 0.68rem; font-family: "JetBrains Mono", monospace;' +
                'opacity: 0.65; white-space: nowrap; flex-shrink: 0;' +
            '}' +
            '.cpb-total-time { font-weight: 500; opacity: 0.85; white-space: nowrap; }' +

            /* Toast */
            '.cpb-toast {' +
                'position: fixed; bottom: 24px; left: 50%; transform: translateX(-50%) translateY(80px);' +
                'display: flex; align-items: center; gap: 10px;' +
                'padding: 12px 24px; border-radius: 12px;' +
                'background: rgba(15, 23, 42, 0.95); color: #10B981;' +
                'font-size: 0.9rem; font-weight: 600;' +
                'border: 1px solid rgba(16, 185, 129, 0.3);' +
                'box-shadow: 0 8px 30px rgba(0,0,0,0.3);' +
                'backdrop-filter: blur(12px);' +
                'z-index: 10000; opacity: 0;' +
                'transition: transform 0.4s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.4s ease;' +
            '}' +
            '.cpb-toast-show { transform: translateX(-50%) translateY(0); opacity: 1; }' +
            '.cpb-toast-complete { color: #F59E0B; border-color: rgba(245, 158, 11, 0.3); }' +
            '[data-theme="light"] .cpb-toast { background: rgba(255,255,255,0.95); box-shadow: 0 8px 30px rgba(0,0,0,0.1); }' +

            /* Completion modal */
            '#cpb-completion-overlay {' +
                'position: fixed; inset: 0; z-index: 10001;' +
                'display: flex; align-items: center; justify-content: center;' +
                'background: rgba(0,0,0,0.6); backdrop-filter: blur(8px);' +
                'opacity: 0; transition: opacity 0.4s ease;' +
            '}' +
            '#cpb-completion-overlay.cpb-overlay-show { opacity: 1; }' +
            '.cpb-completion-modal {' +
                'background: #1E293B; border: 1px solid #334155;' +
                'border-radius: 20px; padding: 40px; text-align: center;' +
                'max-width: 440px; width: 90%; box-shadow: 0 20px 60px rgba(0,0,0,0.5);' +
                'transform: scale(0.9); transition: transform 0.4s cubic-bezier(0.4, 0, 0.2, 1);' +
            '}' +
            '.cpb-overlay-show .cpb-completion-modal { transform: scale(1); }' +
            '.cpb-completion-icon { color: #F59E0B; margin-bottom: 16px; }' +
            '.cpb-completion-modal h3 {' +
                'font-size: 1.5rem; color: #F1F5F9; margin: 0 0 12px; font-family: "Inter", sans-serif;' +
            '}' +
            '.cpb-completion-modal p { color: #94A3B8; line-height: 1.6; margin: 0 0 8px; }' +
            '.cpb-completion-sub { font-size: 0.85rem; color: #64748B; }' +
            '.cpb-completion-sub a { color: #0EA5E9; text-decoration: none; }' +
            '.cpb-completion-btn {' +
                'margin-top: 20px; padding: 10px 32px; border: none; border-radius: 10px;' +
                'background: linear-gradient(135deg, #0EA5E9, #6366F1);' +
                'color: white; font-weight: 600; font-size: 0.95rem;' +
                'cursor: pointer; transition: transform 0.2s ease;' +
            '}' +
            '.cpb-completion-btn:hover { transform: scale(1.05); }' +
            '.cpb-btn-signup {' +
                'background: linear-gradient(135deg, #10B981, #0EA5E9);' +
                'display: inline-block; text-decoration: none;' +
            '}' +
            '.cpb-btn-secondary {' +
                'background: transparent; border: 1px solid #334155;' +
                'color: #94A3B8; margin-top: 8px; font-size: 0.85rem;' +
            '}' +
            '.cpb-btn-secondary:hover { border-color: #475569; color: #F1F5F9; transform: none; }' +
            '.cpb-completion-login { font-size: 0.8rem; color: #64748B; margin-top: 16px; }' +
            '.cpb-completion-login a { color: #0EA5E9; text-decoration: none; }' +
            '.cpb-completion-upgrade {' +
                'font-size: 0.8rem; color: #64748B; margin-top: 16px;' +
                'padding-top: 16px; border-top: 1px solid #334155;' +
            '}' +
            '.cpb-completion-upgrade a { color: #F59E0B; text-decoration: none; font-weight: 500; }' +
            'a.cpb-completion-btn { display: inline-block; text-decoration: none; text-align: center; }' +
            '[data-theme="light"] .cpb-completion-modal { background: #fff; border-color: #E2E8F0; }' +
            '[data-theme="light"] .cpb-completion-modal h3 { color: #1E293B; }' +
            '[data-theme="light"] .cpb-completion-modal p { color: #64748B; }' +
            '[data-theme="light"] .cpb-btn-secondary { border-color: #E2E8F0; color: #64748B; }' +
            '[data-theme="light"] .cpb-btn-secondary:hover { border-color: #CBD5E1; color: #1E293B; }' +
            '[data-theme="light"] .cpb-completion-upgrade { border-top-color: #E2E8F0; }' +

            /* Offset main content for progress bar */
            '.main-content { padding-top: 48px !important; }' +

            /* Responsive */
            '@media (max-width: 900px) {' +
                '#course-progress-bar { padding: 6px 12px; }' +
                '.cpb-label { font-size: 0.7rem; }' +
                '.cpb-track { height: 3px; }' +
            '}';

        document.head.appendChild(style);
    }

    // =========================================================
    // UI: READING-TIME ESTIMATES
    // Computed from the actual injected module text (200 wpm), so they
    // stay correct as content changes. Locked modules are estimated at
    // the median of the readable ones.
    // =========================================================
    function computeReadingTimes() {
        var sections = document.querySelectorAll('section[id^="module"]');
        var minutes = [];
        var lockedCount = 0;

        sections.forEach(function (section) {
            var content = document.getElementById(section.id + '-content') || section;
            if (content.querySelector('.module-locked')) { lockedCount++; return; }
            if (content.querySelector('.content-loading')) return; // still loading
            var words = (content.innerText || '').trim().split(/\s+/).length;
            if (words < 50) return; // empty shell — no estimate
            var mins = Math.max(3, Math.round(words / 200));
            minutes.push(mins);

            var link = document.querySelector('a.nav-link[href="#' + section.id + '"]');
            if (link && !link.querySelector('.cpb-time')) {
                var chip = document.createElement('span');
                chip.className = 'cpb-time';
                chip.textContent = '~' + mins + ' min';
                link.appendChild(chip);
            }
        });

        if (minutes.length === 0) return;

        var total = minutes.reduce(function (a, b) { return a + b; }, 0);
        if (lockedCount > 0) {
            var sorted = minutes.slice().sort(function (a, b) { return a - b; });
            total += lockedCount * sorted[Math.floor(sorted.length / 2)];
        }
        var label = total >= 60
            ? '~' + (Math.round(total / 30) / 2) + ' hrs'
            : '~' + total + ' min';

        var labelEl = document.querySelector('.cpb-label');
        if (labelEl && !labelEl.querySelector('.cpb-total-time')) {
            var totalEl = document.createElement('span');
            totalEl.className = 'cpb-total-time';
            totalEl.textContent = '· ' + label + ' total';
            labelEl.appendChild(totalEl);
        }
    }

    // =========================================================
    // BOOT
    // Module content (incl. the graded quizzes scanModules needs) is
    // injected asynchronously by course-loader.js, so the DOMContentLoaded
    // pass usually finds nothing. We boot on whichever comes last:
    // DOM ready or the loader's courseContentLoaded event — and also
    // expose the reinit() hook course-loader.js already tries to call.
    // =========================================================
    var booted = false;
    function init() {
        if (booted) { computeReadingTimes(); return; }
        scanModules();
        if (totalModules === 0) return; // content not injected yet — wait for courseContentLoaded

        booted = true;
        injectStyles();
        loadProgress();
        createProgressBar();
        updateProgressBar();
        updateSidebarChecks();
        restoreQuizState();
        enhanceCheckAnswer();
        listenForAuthChanges();
        computeReadingTimes();

        // Migrate progress & sync for authenticated users
        setTimeout(migrateProgressOnLogin, 2000);

        // Pre-completion account nudge: signed-out learners with real progress
        // were never asked to create an account until the 100% modal.
        setTimeout(maybeShowSignupNudge, 3000);
    }

    function maybeShowSignupNudge() {
        try {
            if (localStorage.getItem('im-nudge-dismissed')) return;
            if (window.ImpactMojoAuth && ImpactMojoAuth.user) return;
            var pct = totalModules ? (completedModules.size / totalModules) : 0;
            if (pct < 0.15 || pct >= 1) return; // only mid-course, signed out
            if (document.getElementById('cpb-nudge')) return;
            var bar = document.createElement('div');
            bar.id = 'cpb-nudge';
            bar.setAttribute('role', 'note');
            bar.style.cssText = 'position:fixed;bottom:0;left:0;right:0;z-index:9990;background:var(--card-bg,#fff);color:var(--text-primary,#1a202c);border-top:1px solid var(--border-color,#e2e8f0);box-shadow:0 -4px 16px rgba(0,0,0,0.08);padding:10px 14px;display:flex;gap:12px;align-items:center;justify-content:center;flex-wrap:wrap;font-size:0.9rem;';
            bar.innerHTML = '<span>You’re making progress — sign in free to save it across devices and earn a verifiable certificate.</span>' +
                '<a href="/signup.html" style="font-weight:700;color:#4C51BF;text-decoration:none;white-space:nowrap;">Create free account →</a>' +
                '<button type="button" aria-label="Dismiss" style="background:none;border:none;cursor:pointer;font-size:1.1rem;color:inherit;opacity:0.6;">&times;</button>';
            bar.querySelector('button').addEventListener('click', function () {
                try { localStorage.setItem('im-nudge-dismissed', '1'); } catch (e) {}
                bar.remove();
            });
            document.body.appendChild(bar);
        } catch (e) { /* nudge is best-effort */ }
    }

    // Run when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }

    // Re-attempt once the dynamic course content lands
    document.addEventListener('courseContentLoaded', init);
    window.ImpactMojoCourseProgress = window.ImpactMojoCourseProgress || {};
    window.ImpactMojoCourseProgress.reinit = init;
})();
