/**
 * ImpactMojo Authentication System
 * Powered by Supabase
 * Version 2.3.0 - March 20, 2026
 *
 * FEATURES:
 * - Cloud sync for bookmarks, notes, compare list, streak data
 * - Auto-sync on login/logout
 * - Manual sync function
 * - Intelligent data merging (newer/more complete wins)
 *
 * FIXED in v2.3.0:
 * - Migrates sessions from old default Supabase key (sb-*-auth-token) to 'impactmojo-auth'
 *   so existing users don't lose their session after the storageKey change
 * - course-progress.js and challenges.js now reuse window.supabaseClient from auth.js
 *   instead of creating their own GoTrueClient (prevents token refresh races)
 *
 * FIXED in v2.2.0:
 * - Supabase client now uses explicit storageKey ('impactmojo-auth') for consistent
 *   session persistence across all scripts (auth.js, course-progress.js, challenges.js)
 * - isLoggedIn() now checks localStorage as fallback when in-memory state is lost
 * - Added 3-second safety net to recover session if onAuthStateChange didn't fire
 * - persistSession, autoRefreshToken, detectSessionInUrl explicitly enabled
 *
 * FIXED in v2.1.0:
 * - TOKEN_REFRESHED now restores profile after transient SIGNED_OUT (fixes wrong tier)
 * - SIGNED_OUT debounced 500ms to prevent false logouts during token refresh
 * - signIn() deduped with SIGNED_IN handler to prevent double fetch/sync race
 * - fetchProfile() now has 8-second timeout to prevent infinite spinner
 *
 * FIXED in v2.0.2:
 * - Fixed "Identifier 'supabase' has already been declared" error
 * - Renamed client variable to avoid conflict with window.supabase library
 *
 * FIXED in v2.0.1:
 * - Storage keys now match index.html (impactmojo_bookmarks, etc.)
 * 
 * Include this file in your HTML pages:
 * <script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2.112.3"></script>
 * <script src="js/auth.js"></script>
 */

// =====================================================
// SUPABASE CONFIGURATION (loaded from js/config.js)
// =====================================================
const SUPABASE_URL = window.ImpactMojoConfig.SUPABASE_URL;
const SUPABASE_ANON_KEY = window.ImpactMojoConfig.SUPABASE_ANON_KEY;

// Migrate session from old default Supabase storage key to 'impactmojo-auth'.
// Before v2.2.0 each script used the default key (sb-<ref>-auth-token) or its own
// key, so existing users may still have a valid session stored there.
(function migrateOldSession() {
    try {
        // Already have a session under the new key — nothing to migrate
        var existing = localStorage.getItem('impactmojo-auth');
        if (existing) {
            var parsed = JSON.parse(existing);
            if (parsed && parsed.access_token) return;
        }

        // Look for a session under the old default key pattern (sb-<ref>-auth-token)
        var keys = Object.keys(localStorage);
        for (var i = 0; i < keys.length; i++) {
            var k = keys[i];
            if (k.indexOf('sb-') === 0 && k.indexOf('-auth-token') !== -1 && k !== 'impactmojo-auth') {
                var val = localStorage.getItem(k);
                if (val) {
                    var obj = JSON.parse(val);
                    if (obj && (obj.access_token || (obj.currentSession && obj.currentSession.access_token))) {
                        // Copy to new key and remove old one so there's only one source of truth
                        localStorage.setItem('impactmojo-auth', val);
                        localStorage.removeItem(k);
                        console.log('Migrated auth session from', k, 'to impactmojo-auth');
                        break;
                    }
                }
            }
        }
    } catch (e) { /* ignore migration errors */ }
})();

// Initialize Supabase client (using different name to avoid conflict with window.supabase library)
const supabaseClient = window.supabase.createClient(SUPABASE_URL, SUPABASE_ANON_KEY, {
    auth: {
        persistSession: true,
        autoRefreshToken: true,
        detectSessionInUrl: true,
        storageKey: 'impactmojo-auth',
        storage: window.localStorage
    }
});

// =====================================================
// LOCALSTORAGE KEYS
// Prefer using IMState (state-manager.js) when available.
// These constants remain as a fallback if state-manager.js
// hasn't loaded yet (e.g. on pages that don't include it).
// =====================================================
const STORAGE_KEYS = (typeof window.IMState !== 'undefined')
    ? window.IMState.KEYS
    : {
        BOOKMARKS:  'impactmojo_bookmarks',
        NOTES:      'impactmojo_notes',
        COMPARE:    'impactmojo_compare',
        STREAK:     'impactmojo_streak',
        ANALYTICS:  'impactmojo_analytics',
        LAST_SYNC:  'impactmojo_last_sync'
      };

// =====================================================
// AUTH STATE MANAGEMENT
// =====================================================
const ImpactMojoAuth = {
    user: null,
    profile: null,
    isInitialized: false,
    isAuthReady: false,
    _authReadyPromise: null,
    _authReadyResolve: null,
    isSyncing: false,
    _initialSessionHadUser: false,
    _processingAuthEvent: false,
    _signInProcessed: false,
    _signOutDebounce: null,

    // Initialize auth and check session
    async init() {
        if (this.isInitialized) return;

        // Create a promise that resolves when auth state is fully determined
        // This is critical for OAuth redirects where tokens are in the URL hash
        this._authReadyPromise = new Promise(resolve => {
            this._authReadyResolve = resolve;
        });

        try {
            // Listen for auth changes FIRST - this is what processes OAuth callbacks
            // Supabase fires INITIAL_SESSION first, then SIGNED_IN if OAuth tokens are in URL
            supabaseClient.auth.onAuthStateChange(async (event, session) => {
                console.log('Auth state changed:', event, 'hasSession:', !!session, 'hasUser:', !!session?.user);

                if (event === 'INITIAL_SESSION') {
                    this._processingAuthEvent = true;
                    if (session?.user) {
                        this.user = session.user;
                        // Restore cached profile — this has tier/role from last successful fetch
                        if (typeof window.IMState !== 'undefined') {
                            var cached = window.IMState.cachedProfile.get();
                            if (cached && cached.id === session.user.id) {
                                this.profile = cached;
                            }
                        }
                        this._initialSessionHadUser = true;
                    }
                    this._processingAuthEvent = false;
                    this.isAuthReady = true;
                    if (this._authReadyResolve) this._authReadyResolve();
                    // Render immediately with whatever we have (user + cached profile)
                    this.updateUI();
                    // Fetch fresh profile in BACKGROUND — don't block page load
                    if (session?.user) {
                        var self = this;
                        this.fetchProfile().then(function () {
                            self.updateUI(); // re-render with fresh data
                        }).catch(function (e) {
                            console.error('Background profile fetch failed:', e);
                        });
                    }
                    // Sync from cloud in background (non-blocking)
                    if (session?.user) {
                        this.syncFromCloud().catch(function (e) {
                            console.error('Background sync failed:', e);
                        });
                        this.pingActivity(session.user.id);
                    }
                } else if (event === 'SIGNED_IN' && session?.user) {
                    // Skip redundant work if INITIAL_SESSION already handled this user
                    // (happens on OAuth redirects where both events fire)
                    if (this._initialSessionHadUser && this.user?.id === session.user.id) {
                        return;
                    }
                    // Skip if signIn() method already processed this sign-in
                    if (this._signInProcessed && this.user?.id === session.user.id) {
                        return;
                    }
                    // If INITIAL_SESSION hasn't fired yet, defer to it —
                    // SIGNED_IN can fire first on page load when restoring a
                    // session from localStorage, but the token may not be
                    // fully refreshed yet, causing profile queries to hang.
                    if (!this.isAuthReady && !this._initialSessionHadUser) {
                        this.user = session.user;
                        // Restore cached profile for instant UI
                        if (typeof window.IMState !== 'undefined') {
                            var cached = window.IMState.cachedProfile.get();
                            if (cached && cached.id === session.user.id) {
                                this.profile = cached;
                            }
                        }
                        this.updateUI(); // show logged-in state immediately
                        return; // let INITIAL_SESSION handle profile fetch
                    }
                    this._processingAuthEvent = true;
                    this.user = session.user;
                    try {
                        await this.fetchProfile();
                    } catch (e) {
                        console.error('Profile fetch failed during sign-in:', e);
                    }
                    this._processingAuthEvent = false;
                    // If auth wasn't ready yet (OAuth callback), mark it ready now
                    if (!this.isAuthReady) {
                        this.isAuthReady = true;
                        if (this._authReadyResolve) this._authReadyResolve();
                    }
                    this.updateUI();
                    // Sync data in background (non-blocking)
                    this.syncAll().catch(function (e) {
                        console.error('Background sync failed:', e);
                    });
                } else if (event === 'TOKEN_REFRESHED' && session?.user) {
                    // Token was refreshed successfully — restore state if it was
                    // cleared by a transient SIGNED_OUT during refresh
                    // Cancel any pending sign-out debounce
                    if (this._signOutDebounce) {
                        clearTimeout(this._signOutDebounce);
                        this._signOutDebounce = null;
                    }
                    this.user = session.user;
                    // Restore profile if it was lost during a transient SIGNED_OUT
                    if (!this.profile) {
                        if (typeof window.IMState !== 'undefined') {
                            var cached = window.IMState.cachedProfile.get();
                            if (cached && cached.id === session.user.id) {
                                this.profile = cached;
                            }
                        }
                        // Re-fetch fresh profile in background
                        this.fetchProfile().then(() => {
                            this.updateUI();
                        }).catch(function (e) {
                            console.error('Profile re-fetch after token refresh failed:', e);
                        });
                    }
                    this.updateUI();
                } else if (event === 'SIGNED_OUT') {
                    // Guard: ignore transient SIGNED_OUT fired while we are still
                    // processing INITIAL_SESSION or SIGNED_IN (race during token refresh)
                    if (this._processingAuthEvent) {
                        console.warn('Ignoring transient SIGNED_OUT during auth processing');
                        return;
                    }

                    // If auth hasn't resolved yet (initial load, no session),
                    // resolve immediately — no need to debounce
                    if (!this.isAuthReady) {
                        this.user = null;
                        this.profile = null;
                        this.isAuthReady = true;
                        if (this._authReadyResolve) this._authReadyResolve();
                        this.updateUI();
                        return;
                    }

                    // Debounce: wait 1000ms before processing sign-out.
                    // TOKEN_REFRESHED fires shortly after a transient SIGNED_OUT
                    // during token refresh and will cancel this timer.
                    // Increased from 500ms to 1000ms to better handle slow networks.
                    var self = this;
                    if (this._signOutDebounce) clearTimeout(this._signOutDebounce);
                    this._signOutDebounce = setTimeout(async function () {
                        self._signOutDebounce = null;
                        // Double-check with Supabase before clearing state
                        try {
                            var check = await supabaseClient.auth.getSession();
                            if (check?.data?.session?.user) {
                                console.warn('SIGNED_OUT fired but session still valid — ignoring');
                                self.user = check.data.session.user;
                                // Restore profile if it was lost
                                if (!self.profile) {
                                    if (typeof window.IMState !== 'undefined') {
                                        var cached = window.IMState.cachedProfile.get();
                                        if (cached && cached.id === check.data.session.user.id) {
                                            self.profile = cached;
                                        }
                                    }
                                    self.fetchProfile().catch(function (e) {
                                        console.error('Profile re-fetch after SIGNED_OUT recovery failed:', e);
                                    });
                                }
                                self.updateUI();
                                return;
                            }
                        } catch (_) { /* proceed with sign-out */ }

                        self.user = null;
                        self.profile = null;
                        self._signInProcessed = false;
                        // Clear cached profile on sign-out
                        if (typeof window.IMState !== 'undefined') {
                            window.IMState.cachedProfile.clear();
                        }
                        self.updateUI();
                    }, 1000);
                }
            });

            this.isInitialized = true;

            // Safety net: if after 1.5 seconds auth is ready but user is null,
            // try to recover from Supabase session (handles edge cases where
            // onAuthStateChange didn't fire properly or token refresh caused
            // a transient SIGNED_OUT)
            var self = this;
            setTimeout(async function () {
                if (!self.user) {
                    try {
                        var session = await supabaseClient.auth.getSession();
                        if (session?.data?.session?.user) {
                            console.log('Recovering session from Supabase after init gap');
                            self.user = session.data.session.user;
                            await self.fetchProfile().catch(function () {});
                            if (!self.isAuthReady) {
                                self.isAuthReady = true;
                                if (self._authReadyResolve) self._authReadyResolve();
                            }
                            self.updateUI();
                        }
                    } catch (_) {}
                }
            }, 1500);

            // Second safety net at 4 seconds for slow connections
            setTimeout(async function () {
                if (!self.user) {
                    try {
                        var session = await supabaseClient.auth.getSession();
                        if (session?.data?.session?.user) {
                            console.log('Late session recovery (4s)');
                            self.user = session.data.session.user;
                            await self.fetchProfile().catch(function () {});
                            self.updateUI();
                        }
                    } catch (_) {}
                }
            }, 4000);

            // Re-fetch profile when page becomes visible again (back/forward navigation)
            // This fixes stale tier state when navigating back from org-dashboard
            // Throttled: only re-fetch if last fetch was >30 seconds ago
            document.addEventListener('visibilitychange', () => {
                if (document.visibilityState === 'visible' && this.user) {
                    if ((Date.now() - this._lastProfileFetchTime) < 30000) return;
                    this.fetchProfile().then(() => {
                        this.updateUI();
                    }).catch(e => {
                        console.error('Profile re-fetch on visibility change failed:', e);
                    });
                }
            });

        } catch (err) {
            console.error('Auth initialization failed:', err);
            // Ensure auth ready resolves even on error
            this.isAuthReady = true;
            if (this._authReadyResolve) this._authReadyResolve();
        }
    },

    // Wait for auth to be fully ready (use this before redirecting based on auth state)
    waitForAuthReady() {
        if (this.isAuthReady) return Promise.resolve();
        return this._authReadyPromise || Promise.resolve();
    },

    // Fetch user profile from database (with 8-second timeout)
    // Deduplicates concurrent calls — multiple callers share one in-flight request
    _profileFetchPromise: null,
    _lastProfileFetchTime: 0,
    _profileRetryTimer: null,

    // Schedule a background retry after a failed profile fetch.
    // This prevents stale cached profiles (e.g. wrong tier) from persisting.
    _scheduleProfileRetry() {
        if (this._profileRetryTimer) return; // already scheduled
        var self = this;
        this._profileRetryTimer = setTimeout(async function () {
            self._profileRetryTimer = null;
            if (!self.user) return;
            console.log('Retrying profile fetch...');
            // Clear the dedup guard so a fresh fetch runs
            self._profileFetchPromise = null;
            self._lastProfileFetchTime = 0;
            try {
                await self.fetchProfile();
                self.updateUI();
            } catch (_) { /* give up silently after retry */ }
        }, 5000);
    },

    async fetchProfile() {
        if (!this.user) return null;

        // If a fetch is already in flight, piggyback on it
        if (this._profileFetchPromise) return this._profileFetchPromise;

        // Skip if fetched very recently (within 2 seconds) — prevents redundant DB hits
        var now = Date.now();
        if (this.profile && (now - this._lastProfileFetchTime) < 2000) {
            return this.profile;
        }

        // Helper: fall back to cached profile if available
        var self = this;
        function fallbackToCache() {
            if (!self.profile && typeof window.IMState !== 'undefined') {
                var cached = window.IMState.cachedProfile.get();
                if (cached && cached.id === self.user.id) {
                    self.profile = cached;
                    return cached;
                }
            }
            return null;
        }

        this._profileFetchPromise = (async () => {
            try {
                // Ensure session is valid before querying — on page load the
                // Supabase client may fire SIGNED_IN before the token is fully
                // restored, causing RLS to reject/hang the profiles query.
                try {
                    var sess = await supabaseClient.auth.getSession();
                    console.log('[Auth] fetchProfile session check:', !!sess?.data?.session, 'userId:', sess?.data?.session?.user?.id?.substring(0,8) || 'none');
                    if (!sess?.data?.session) {
                        console.warn('fetchProfile: no active session, skipping');
                        var cached = fallbackToCache();
                        this._scheduleProfileRetry();
                        return cached;
                    }
                } catch (_) { /* proceed anyway */ }

                var profilePromise = supabaseClient
                    .from('profiles')
                    .select('id, display_name, full_name, email, avatar_url, subscription_tier, subscription_status, organization, role, resource_grants')
                    .eq('id', this.user.id)
                    .single();

                var timeoutPromise = new Promise(function (_, reject) {
                    setTimeout(function () { reject(new Error('Profile fetch timed out')); }, 15000);
                });

                const { data, error } = await Promise.race([profilePromise, timeoutPromise]);

                if (error) {
                    console.error('Error fetching profile:', error);
                    var cached = fallbackToCache();
                    // Schedule a retry so stale cache doesn't persist
                    this._scheduleProfileRetry();
                    return cached;
                }

                this.profile = data;
                this._lastProfileFetchTime = Date.now();
                if (typeof window.IMState !== 'undefined') {
                    window.IMState.cachedProfile.set(data);
                }

                // Update learning streak (fire-and-forget)
                supabaseClient.rpc('update_streak', { p_user_id: data.id }).catch(function() {});

                return data;
            } catch (err) {
                console.error('Profile fetch failed:', err);
                var cached = fallbackToCache();
                // Schedule a retry so stale cache doesn't persist
                this._scheduleProfileRetry();
                return cached;
            } finally {
                this._profileFetchPromise = null;
            }
        })();

        return this._profileFetchPromise;
    },

    // =====================================================
    // DATA SYNC METHODS
    // =====================================================

    // Get data from localStorage
    // Uses IMState (state-manager.js) when available for canonical key access
    getLocalData() {
        if (typeof window.IMState !== 'undefined') {
            return window.IMState.getSyncableData();
        }
        return {
            bookmarks: JSON.parse(localStorage.getItem(STORAGE_KEYS.BOOKMARKS) || '[]'),
            notes: JSON.parse(localStorage.getItem(STORAGE_KEYS.NOTES) || '[]'),
            compare_list: JSON.parse(localStorage.getItem(STORAGE_KEYS.COMPARE) || '[]'),
            streak_data: JSON.parse(localStorage.getItem(STORAGE_KEYS.STREAK) || '{"currentStreak":0,"longestStreak":0,"lastVisit":null}'),
            progress: JSON.parse(localStorage.getItem(STORAGE_KEYS.ANALYTICS) || '{}')
        };
    },

    // Save data to localStorage
    setLocalData(data) {
        if (typeof window.IMState !== 'undefined') {
            window.IMState.setSyncableData(data);
            return;
        }
        if (data.bookmarks !== undefined) {
            localStorage.setItem(STORAGE_KEYS.BOOKMARKS, JSON.stringify(data.bookmarks));
        }
        if (data.notes !== undefined) {
            localStorage.setItem(STORAGE_KEYS.NOTES, JSON.stringify(data.notes));
        }
        if (data.compare_list !== undefined) {
            localStorage.setItem(STORAGE_KEYS.COMPARE, JSON.stringify(data.compare_list));
        }
        if (data.streak_data !== undefined) {
            localStorage.setItem(STORAGE_KEYS.STREAK, JSON.stringify(data.streak_data));
        }
        if (data.progress !== undefined) {
            localStorage.setItem(STORAGE_KEYS.ANALYTICS, JSON.stringify(data.progress));
        }
    },

    // Merge local and cloud data (newer/more complete wins)
    mergeData(localData, cloudData) {
        const merged = {};

        // Merge bookmarks (combine unique items by ID)
        const allBookmarks = [...(cloudData.bookmarks || []), ...(localData.bookmarks || [])];
        const bookmarkMap = new Map();
        allBookmarks.forEach(item => {
            const key = item.id || item.name || JSON.stringify(item);
            if (!bookmarkMap.has(key) || (item.addedAt && item.addedAt > bookmarkMap.get(key).addedAt)) {
                bookmarkMap.set(key, item);
            }
        });
        merged.bookmarks = Array.from(bookmarkMap.values());

        // Merge notes (combine unique by ID, newer timestamp wins)
        const allNotes = [...(cloudData.notes || []), ...(localData.notes || [])];
        const notesMap = new Map();
        allNotes.forEach(note => {
            const key = note.id || note.timestamp;
            if (!notesMap.has(key) || (note.updatedAt && note.updatedAt > notesMap.get(key).updatedAt)) {
                notesMap.set(key, note);
            }
        });
        merged.notes = Array.from(notesMap.values()).sort((a, b) => 
            (b.timestamp || 0) - (a.timestamp || 0)
        );

        // Merge compare list (combine unique items)
        const allCompare = [...(cloudData.compare_list || []), ...(localData.compare_list || [])];
        const compareMap = new Map();
        allCompare.forEach(item => {
            const key = item.id || item.name || JSON.stringify(item);
            compareMap.set(key, item);
        });
        merged.compare_list = Array.from(compareMap.values());

        // Merge streak data (keep higher values)
        const localStreak = localData.streak_data || { currentStreak: 0, longestStreak: 0, lastVisit: null };
        const cloudStreak = cloudData.streak_data || { currentStreak: 0, longestStreak: 0, lastVisit: null };
        merged.streak_data = {
            currentStreak: Math.max(localStreak.currentStreak || 0, cloudStreak.currentStreak || 0),
            longestStreak: Math.max(localStreak.longestStreak || 0, cloudStreak.longestStreak || 0),
            lastVisit: localStreak.lastVisit && cloudStreak.lastVisit 
                ? (localStreak.lastVisit > cloudStreak.lastVisit ? localStreak.lastVisit : cloudStreak.lastVisit)
                : (localStreak.lastVisit || cloudStreak.lastVisit),
            // Keep additional streak fields
            totalVisits: Math.max(localStreak.totalVisits || 0, cloudStreak.totalVisits || 0)
        };

        // Merge progress/analytics (combine all data)
        merged.progress = {
            ...(cloudData.progress || {}),
            ...(localData.progress || {})
        };

        return merged;
    },

    // Sync local data TO cloud (push)
    async syncToCloud() {
        if (!this.user || this.isSyncing) {
            return { success: false, message: 'Not logged in or sync in progress' };
        }

        this.isSyncing = true;

        try {
            const localData = this.getLocalData();

            const { data, error } = await supabaseClient
                .from('profiles')
                .update({
                    bookmarks: localData.bookmarks,
                    notes: localData.notes,
                    compare_list: localData.compare_list,
                    streak_data: localData.streak_data,
                    progress: localData.progress,
                    last_synced_at: new Date().toISOString(),
                    updated_at: new Date().toISOString()
                })
                .eq('id', this.user.id)
                .select()
                .single();

            if (error) throw error;

            // Update local last sync time
            localStorage.setItem(STORAGE_KEYS.LAST_SYNC, new Date().toISOString());
            
            this.profile = data;
            this.isSyncing = false;

            console.log('✅ Data synced to cloud');
            return { success: true, message: 'Data synced to cloud', data };

        } catch (err) {
            console.error('Sync to cloud failed:', err);
            this.isSyncing = false;
            return { success: false, message: err.message, error: err };
        }
    },

    // Sync cloud data TO local (pull)
    async syncFromCloud() {
        if (!this.user || this.isSyncing) {
            return { success: false, message: 'Not logged in or sync in progress' };
        }

        this.isSyncing = true;

        try {
            // Fetch latest profile with sync data
            const { data, error } = await supabaseClient
                .from('profiles')
                .select('bookmarks, notes, compare_list, streak_data, progress, last_synced_at')
                .eq('id', this.user.id)
                .single();

            if (error) throw error;

            const cloudData = {
                bookmarks: data.bookmarks || [],
                notes: data.notes || [],
                compare_list: data.compare_list || [],
                streak_data: data.streak_data || { currentStreak: 0, longestStreak: 0, lastVisit: null },
                progress: data.progress || {}
            };

            const localData = this.getLocalData();
            
            // Merge data (handles conflicts)
            const mergedData = this.mergeData(localData, cloudData);
            
            // Save merged data locally
            this.setLocalData(mergedData);
            
            // Update last sync time
            localStorage.setItem(STORAGE_KEYS.LAST_SYNC, new Date().toISOString());

            this.isSyncing = false;

            console.log('✅ Data synced from cloud');
            
            // Dispatch event for UI updates (IMX can listen to this)
            window.dispatchEvent(new CustomEvent('dataSynced', { detail: mergedData }));

            return { success: true, message: 'Data synced from cloud', data: mergedData };

        } catch (err) {
            console.error('Sync from cloud failed:', err);
            this.isSyncing = false;
            return { success: false, message: err.message, error: err };
        }
    },

    // Full two-way sync (merge local + cloud, then push)
    async syncAll() {
        if (!this.user) {
            return { success: false, message: 'Not logged in' };
        }

        // Prevent overlapping full syncs
        if (this.isSyncing) {
            return { success: false, message: 'Sync already in progress' };
        }

        console.log('🔄 Starting full sync...');

        // Set the flag once for the entire operation so individual
        // syncFromCloud / syncToCloud calls don't block each other
        this.isSyncing = true;

        try {
            // --- Pull from cloud and merge ---
            var pullResult = { success: false, message: 'skipped' };
            try {
                const { data, error } = await supabaseClient
                    .from('profiles')
                    .select('bookmarks, notes, compare_list, streak_data, progress, last_synced_at')
                    .eq('id', this.user.id)
                    .single();

                if (error) throw error;

                const cloudData = {
                    bookmarks: data.bookmarks || [],
                    notes: data.notes || [],
                    compare_list: data.compare_list || [],
                    streak_data: data.streak_data || { currentStreak: 0, longestStreak: 0, lastVisit: null },
                    progress: data.progress || {}
                };
                const localData = this.getLocalData();
                const mergedData = this.mergeData(localData, cloudData);
                this.setLocalData(mergedData);
                localStorage.setItem(STORAGE_KEYS.LAST_SYNC, new Date().toISOString());
                window.dispatchEvent(new CustomEvent('dataSynced', { detail: mergedData }));
                pullResult = { success: true, message: 'Data synced from cloud', data: mergedData };
            } catch (pullErr) {
                console.warn('Pull failed, attempting push anyway:', pullErr.message);
                pullResult = { success: false, message: pullErr.message };
            }

            // --- Push merged data back to cloud ---
            var pushResult = { success: false, message: 'skipped' };
            try {
                const localData = this.getLocalData();
                const { data, error } = await supabaseClient
                    .from('profiles')
                    .update({
                        bookmarks: localData.bookmarks,
                        notes: localData.notes,
                        compare_list: localData.compare_list,
                        streak_data: localData.streak_data,
                        progress: localData.progress,
                        last_synced_at: new Date().toISOString(),
                        updated_at: new Date().toISOString()
                    })
                    .eq('id', this.user.id)
                    .select()
                    .single();

                if (error) throw error;

                localStorage.setItem(STORAGE_KEYS.LAST_SYNC, new Date().toISOString());
                this.profile = data;
                pushResult = { success: true, message: 'Data synced to cloud', data };
            } catch (pushErr) {
                console.error('Push failed:', pushErr.message);
                pushResult = { success: false, message: pushErr.message };
            }

            console.log('✅ Full sync complete');

            // Dispatch sync complete event
            window.dispatchEvent(new CustomEvent('syncComplete', {
                detail: { pullResult, pushResult }
            }));

            return {
                success: pullResult.success || pushResult.success,
                message: 'Full sync complete',
                pullResult,
                pushResult
            };

        } catch (err) {
            console.error('Full sync failed:', err);
            return { success: false, message: err.message, error: err };
        } finally {
            this.isSyncing = false;
        }
    },

    // Debounced sync - call this after data changes
    // Waits 3 seconds of inactivity before syncing
    _syncTimeout: null,
    queueSync() {
        if (!this.user) return;
        
        // Clear existing timeout
        if (this._syncTimeout) {
            clearTimeout(this._syncTimeout);
        }
        
        // Set new timeout
        this._syncTimeout = setTimeout(() => {
            this.syncToCloud();
        }, 3000);
    },

    // Get last sync time
    getLastSyncTime() {
        const lastSync = localStorage.getItem(STORAGE_KEYS.LAST_SYNC);
        return lastSync ? new Date(lastSync) : null;
    },

    // Get formatted last sync time for display
    getLastSyncDisplay() {
        const lastSync = this.getLastSyncTime();
        if (!lastSync) return 'Never synced';
        
        const now = new Date();
        const diffMs = now - lastSync;
        const diffMins = Math.floor(diffMs / 60000);
        const diffHours = Math.floor(diffMs / 3600000);
        const diffDays = Math.floor(diffMs / 86400000);

        if (diffMins < 1) return 'Just now';
        if (diffMins < 60) return `${diffMins} minute${diffMins > 1 ? 's' : ''} ago`;
        if (diffHours < 24) return `${diffHours} hour${diffHours > 1 ? 's' : ''} ago`;
        return `${diffDays} day${diffDays > 1 ? 's' : ''} ago`;
    },

    // =====================================================
    // AUTHENTICATION METHODS
    // =====================================================

    // Sign up with email and password
    async signUp(email, password, fullName = '') {
        try {
            const { data, error } = await supabaseClient.auth.signUp({
                email: email,
                password: password,
                options: {
                    data: {
                        full_name: fullName,
                        display_name: fullName || email.split('@')[0]
                    },
                    emailRedirectTo: window.location.origin + '/account.html'
                }
            });

            if (error) throw error;

            return {
                success: true,
                message: 'Account created! Please check your email to verify your account.',
                data: data
            };
        } catch (err) {
            console.error('Sign up error:', err);
            return {
                success: false,
                message: err.message || 'Sign up failed. Please try again.',
                error: err
            };
        }
    },

    // Sign in with email and password
    async signIn(email, password) {
        try {
            const { data, error } = await supabaseClient.auth.signInWithPassword({
                email: email,
                password: password
            });

            if (error) throw error;

            this.user = data.user;
            this._signInProcessed = true;
            await this.fetchProfile();

            // Ensure cached profile is set for next page load
            if (this.profile && typeof window.IMState !== 'undefined') {
                window.IMState.cachedProfile.set(this.profile);
            }
            // Update UI immediately so auth classes are applied
            this.updateUI();

            // Sync data after login (non-blocking — don't delay redirect)
            this.syncAll().catch(function (e) {
                console.error('Post-login sync failed:', e);
            });

            return {
                success: true,
                message: 'Welcome back!',
                data: data
            };
        } catch (err) {
            console.error('Sign in error:', err);
            return {
                success: false,
                message: err.message || 'Sign in failed. Please check your credentials.',
                error: err
            };
        }
    },

    // Sign in with Google
    async signInWithGoogle() {
        try {
            const { data, error } = await supabaseClient.auth.signInWithOAuth({
                provider: 'google',
                options: {
                    redirectTo: window.location.origin + '/account.html'
                }
            });

            if (error) throw error;

            return { success: true, data: data };
        } catch (err) {
            console.error('Google sign in error:', err);
            return {
                success: false,
                message: err.message || 'Google sign in failed.',
                error: err
            };
        }
    },

    // Sign in with magic link (passwordless)
    async signInWithMagicLink(email) {
        try {
            const { data, error } = await supabaseClient.auth.signInWithOtp({
                email: email,
                options: {
                    emailRedirectTo: window.location.origin + '/account.html'
                }
            });

            if (error) throw error;

            return {
                success: true,
                message: 'Check your email for the login link!',
                data: data
            };
        } catch (err) {
            console.error('Magic link error:', err);
            return {
                success: false,
                message: err.message || 'Failed to send magic link.',
                error: err
            };
        }
    },

    // Sign out
    async signOut() {
        try {
            // Sync before logout (save any unsaved data)
            if (this.user) {
                await this.syncToCloud();
            }

            const { error } = await supabaseClient.auth.signOut();
            
            if (error) throw error;

            this.user = null;
            this.profile = null;
            this._signInProcessed = false;
            // Clear cached profile
            if (typeof window.IMState !== 'undefined') {
                window.IMState.cachedProfile.clear();
            }

            // Redirect to home page
            window.location.href = '/';

            return { success: true };
        } catch (err) {
            console.error('Sign out error:', err);
            return {
                success: false,
                message: err.message || 'Sign out failed.',
                error: err
            };
        }
    },

    // Reset password
    // Keep profiles.last_active_at truthful (feeds the transparency page's
    // "Active in last 30 days"). Fire-and-forget, throttled to once per day.
    pingActivity(userId) {
        try {
            var key = 'im-activity-ping';
            var last = localStorage.getItem(key);
            var today = new Date().toISOString().slice(0, 10);
            if (last === today) return;
            supabaseClient.from('profiles')
                .update({ last_active_at: new Date().toISOString() })
                .eq('id', userId)
                .then(function (result) {
                    if (result && result.error) {
                        console.warn('[Auth] last_active_at not recorded:', result.error.message);
                        return;   // do not mark today as done — let it retry
                    }
                    try { localStorage.setItem(key, today); } catch (e) {}
                });
        } catch (e) { /* best-effort */ }
    },

    async resetPassword(email) {
        try {
            const { data, error } = await supabaseClient.auth.resetPasswordForEmail(email, {
                redirectTo: window.location.origin + '/reset-password.html'
            });

            if (error) throw error;

            return {
                success: true,
                message: 'Password reset email sent! Check your inbox.',
                data: data
            };
        } catch (err) {
            console.error('Password reset error:', err);
            return {
                success: false,
                message: err.message || 'Failed to send reset email.',
                error: err
            };
        }
    },

    // Update password (when user has reset token)
    async updatePassword(newPassword) {
        try {
            const { data, error } = await supabaseClient.auth.updateUser({
                password: newPassword
            });

            if (error) throw error;

            return {
                success: true,
                message: 'Password updated successfully!',
                data: data
            };
        } catch (err) {
            console.error('Update password error:', err);
            return {
                success: false,
                message: err.message || 'Failed to update password.',
                error: err
            };
        }
    },

    // =====================================================
    // PROFILE MANAGEMENT
    // =====================================================

    // Update user profile
    async updateProfile(updates) {
        if (!this.user) {
            return { success: false, message: 'Not logged in' };
        }

        try {
            const { data, error } = await supabaseClient
                .from('profiles')
                .update({
                    ...updates,
                    updated_at: new Date().toISOString()
                })
                .eq('id', this.user.id)
                .select()
                .single();

            if (error) throw error;

            this.profile = data;

            return {
                success: true,
                message: 'Profile updated successfully!',
                data: data
            };
        } catch (err) {
            console.error('Profile update error:', err);
            return {
                success: false,
                message: err.message || 'Failed to update profile.',
                error: err
            };
        }
    },

    // =====================================================
    // SUBSCRIPTION HELPERS
    // =====================================================

    // Check if user has active premium subscription
    isPremium() {
        if (!this.profile) return false;
        return ['practitioner', 'professional', 'organization'].includes(this.profile.subscription_tier);
    },

    // Check specific tier access
    hasTierAccess(requiredTier) {
        const tierHierarchy = ['explorer', 'practitioner', 'professional', 'organization'];
        const userTierIndex = tierHierarchy.indexOf(this.profile?.subscription_tier || 'explorer');
        const requiredTierIndex = tierHierarchy.indexOf(requiredTier);
        return userTierIndex >= requiredTierIndex;
    },

    // Check standalone per-resource access (e.g. a single Practice Pack
    // bought for a one-time fee). Granted via the profile's resource_grants
    // column — an array of resource slugs, or an object keyed by slug.
    hasResourceAccess(slug) {
        const grants = this.profile?.resource_grants;
        if (!grants || !slug) return false;
        if (Array.isArray(grants)) return grants.indexOf(slug) !== -1;
        if (typeof grants === 'object') return !!grants[slug];
        return false;
    },

    // Get subscription tier display name
    getTierDisplayName() {
        const tierNames = {
            'explorer': 'Explorer (Free)',
            'practitioner': 'Practitioner',
            'professional': 'Professional',
            'organization': 'Organization'
        };
        return tierNames[this.profile?.subscription_tier] || 'Explorer (Free)';
    },

    // =====================================================
    // UI UPDATE METHODS
    // =====================================================

    // Auto-inject auth buttons into .im-topbar-right on any page
    _injectTopbarAuth() {
        var topbarRight = document.querySelector('.im-topbar-right');
        if (!topbarRight || topbarRight.querySelector('.topbar-auth-injected')) return;
        // Skip injection if the page already has its own auth buttons (e.g. account.html, premium.html)
        if (document.querySelector('header .auth-logged-out, header .auth-logged-in, .nav-buttons .auth-logged-out')) return;

        // WCAG AA: fallback colors must pass 4.5:1 even when --text-secondary
        // is unset. #475569 (slate-600) = 7.58:1 on white.
        var loginBtn = document.createElement('a');
        loginBtn.href = '/login.html';
        loginBtn.className = 'auth-logged-out topbar-auth-injected';
        loginBtn.style.cssText = 'color:var(--text-secondary,#475569);text-decoration:none;font-size:0.85rem;margin-right:0.5rem;';
        loginBtn.textContent = 'Log In';

        // WCAG AA: white on indigo-600 #4f46e5 = 5.18:1 (was indigo-500 #6366f1 = 4.04:1).
        var signupBtn = document.createElement('a');
        signupBtn.href = '/signup.html';
        signupBtn.className = 'auth-logged-out topbar-auth-injected';
        signupBtn.style.cssText = 'background:#4f46e5;color:#fff;text-decoration:none;font-size:0.8rem;padding:0.3rem 0.75rem;border-radius:6px;margin-right:0.75rem;';
        signupBtn.textContent = 'Sign Up';

        var accountBtn = document.createElement('a');
        accountBtn.href = '/account.html';
        accountBtn.className = 'auth-logged-in topbar-auth-injected';
        accountBtn.style.cssText = 'color:var(--text-secondary,#475569);text-decoration:none;font-size:0.85rem;margin-right:0.5rem;align-items:center;gap:0.25rem;';
        accountBtn.innerHTML =
            '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align:middle;margin-right:0.25rem;">' +
            '<path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>' +
            '<span class="auth-user-name">Account</span>';

        var logoutBtn = document.createElement('a');
        logoutBtn.href = '#';
        logoutBtn.className = 'auth-logged-in topbar-auth-injected';
        logoutBtn.style.cssText = 'color:var(--text-secondary,#475569);text-decoration:none;font-size:0.8rem;margin-right:0.75rem;opacity:0.7;';
        logoutBtn.textContent = 'Log Out';
        logoutBtn.addEventListener('click', function (e) {
            e.preventDefault();
            ImpactMojoAuth.signOut().then(function () {
                window.location.href = '/';
            });
        });

        var firstChild = topbarRight.firstChild;
        topbarRight.insertBefore(logoutBtn, firstChild);
        topbarRight.insertBefore(accountBtn, logoutBtn);
        topbarRight.insertBefore(signupBtn, accountBtn);
        topbarRight.insertBefore(loginBtn, signupBtn);
    },

    // Update UI based on auth state
    updateUI() {
        const isLoggedIn = !!this.user;
        console.log('[Auth] updateUI called — isLoggedIn:', isLoggedIn, 'tier:', this.profile?.subscription_tier || 'none', 'user:', this.user?.email || 'null');

        // Inject auth buttons into topbar if not already present
        this._injectTopbarAuth();

        // Inject auth CSS if not already present
        if (!document.getElementById('auth-topbar-styles')) {
            var style = document.createElement('style');
            style.id = 'auth-topbar-styles';
            style.textContent =
                '.auth-logged-in { display: none !important; }' +
                'body.user-authenticated .auth-logged-in { display: inline-flex !important; }' +
                'body.user-authenticated .auth-logged-out { display: none !important; }' +
                // Mobile de-clutter: the injected auth chip + language globe + Browse +
                // Premium + theme selector all share .im-topbar-right and overflow on
                // phones. Tighten and trim on small screens (content-page topbars only).
                '@media (max-width:600px){' +
                '.im-topbar{gap:.4rem;row-gap:.4rem}' +
                '.im-topbar-right{gap:.4rem;row-gap:.4rem;flex-wrap:wrap}' +
                '.im-browse-btn{font-size:0 !important;padding:.4rem !important;gap:0 !important}' +
                '.im-browse-btn svg{width:16px;height:16px}' +
                '.im-premium-btn{font-size:.72rem !important;padding:.3rem .6rem !important}' +
                'a.auth-logged-in.topbar-auth-injected[href="#"]{display:none !important}' +
                '#im-lang-switch.im-lang-innav .im-fab{width:32px !important;height:32px !important}' +
                '}';
            document.head.appendChild(style);
        }

        // Add/remove body class for CSS-based auth display (handles !important)
        if (isLoggedIn) {
            document.body.classList.add('user-authenticated');
        } else {
            document.body.classList.remove('user-authenticated');
        }

        // Update login/signup buttons visibility
        document.querySelectorAll('.auth-logged-out').forEach(el => {
            el.style.display = isLoggedIn ? 'none' : '';
        });

        document.querySelectorAll('.auth-logged-in').forEach(el => {
            el.style.display = isLoggedIn ? '' : 'none';
        });

        // Update user name displays
        document.querySelectorAll('.auth-user-name').forEach(el => {
            el.textContent = this.profile?.display_name || this.profile?.full_name || this.user?.email?.split('@')[0] || 'User';
        });

        // Update user email displays
        document.querySelectorAll('.auth-user-email').forEach(el => {
            el.textContent = this.user?.email || '';
        });

        // Update subscription tier displays
        document.querySelectorAll('.auth-user-tier').forEach(el => {
            el.textContent = this.getTierDisplayName();
        });

        // Update avatar displays
        document.querySelectorAll('.auth-user-avatar').forEach(el => {
            if (this.profile?.avatar_url) {
                el.src = this.profile.avatar_url;
            } else {
                // Generate initials avatar
                const name = this.profile?.display_name || this.profile?.full_name || this.user?.email || 'U';
                el.src = `https://ui-avatars.com/api/?name=${encodeURIComponent(name)}&background=6366f1&color=fff`;
            }
        });

        // Update sync status displays
        document.querySelectorAll('.auth-sync-status').forEach(el => {
            el.textContent = this.getLastSyncDisplay();
        });

        // Handle premium-only content
        document.querySelectorAll('.premium-only').forEach(el => {
            if (this.isPremium()) {
                el.classList.remove('premium-locked');
            } else {
                el.classList.add('premium-locked');
            }
        });

        // Dispatch custom event for other scripts to listen to
        window.dispatchEvent(new CustomEvent('authStateChanged', {
            detail: { user: this.user, profile: this.profile, isLoggedIn }
        }));
    },

    // =====================================================
    // UTILITY METHODS
    // =====================================================

    // Check Supabase for a valid session (bypasses in-memory state)
    async getSession() {
        try {
            var result = await supabaseClient.auth.getSession();
            return result?.data?.session || null;
        } catch (_) {
            return null;
        }
    },

    // Check if user is logged in (checks in-memory state + localStorage fallback)
    isLoggedIn() {
        if (this.user) return true;
        // Fallback: check if Supabase has a session in localStorage
        // This handles cases where in-memory state was lost during token refresh
        try {
            var stored = localStorage.getItem('impactmojo-auth');
            if (stored) {
                var val = JSON.parse(stored);
                if (val && val.access_token) {
                    // Session exists in storage — trigger async recovery
                    this._recoverSessionFromStorage();
                    return true;
                }
            }
            // Legacy key check
            var keys = Object.keys(localStorage);
            for (var i = 0; i < keys.length; i++) {
                if (keys[i].indexOf('sb-') === 0 && keys[i].indexOf('-auth-token') !== -1) {
                    var val2 = JSON.parse(localStorage.getItem(keys[i]));
                    if (val2 && (val2.access_token || (val2.currentSession && val2.currentSession.access_token))) {
                        return true;
                    }
                }
            }
        } catch (_) {}
        return false;
    },

    // Async session recovery when isLoggedIn() finds a stored session but user is null
    async _recoverSessionFromStorage() {
        if (this.user || this._recoveringSession) return;
        this._recoveringSession = true;
        try {
            var session = await supabaseClient.auth.getSession();
            if (session?.data?.session?.user) {
                this.user = session.data.session.user;
                await this.fetchProfile().catch(function () {});
                this.updateUI();
            }
        } catch (_) {} finally {
            this._recoveringSession = false;
        }
    },

    // Get current user
    getUser() {
        return this.user;
    },

    // Get current profile
    getProfile() {
        return this.profile;
    },

    // Redirect to login if not authenticated
    requireAuth(redirectUrl = '/login.html') {
        if (!this.user) {
            // Store intended destination
            sessionStorage.setItem('authRedirect', window.location.href);
            window.location.href = redirectUrl;
            return false;
        }
        return true;
    },

    // Redirect after successful login
    redirectAfterLogin() {
        const redirectUrl = sessionStorage.getItem('authRedirect');
        sessionStorage.removeItem('authRedirect');
        window.location.href = redirectUrl || '/account.html';
    }
};

// =====================================================
// AUTO-INITIALIZE ON PAGE LOAD
// =====================================================
document.addEventListener('DOMContentLoaded', () => {
    ImpactMojoAuth.init();
});

// Also try to initialize immediately if DOM is already ready
if (document.readyState === 'complete' || document.readyState === 'interactive') {
    ImpactMojoAuth.init();
}

// Extra recovery: when page fully loads, if no user but localStorage has session,
// aggressively retry auth recovery. Handles the case where defer scripts on the
// homepage cause auth to not be ready when premium.js or UI code runs.
window.addEventListener('load', function () {
    if (!ImpactMojoAuth.user) {
        try {
            var stored = localStorage.getItem('impactmojo-auth');
            if (stored && JSON.parse(stored).access_token) {
                ImpactMojoAuth._recoverSessionFromStorage();
            }
        } catch (_) {}
    }
});

// =====================================================
// AUTO-SYNC ON PAGE VISIBILITY CHANGE
// (Profile re-fetch is handled by the visibilitychange
//  listener inside init(). This listener only triggers
//  a background data sync if the last sync was stale.)
// =====================================================
document.addEventListener('visibilitychange', () => {
    if (document.visibilityState === 'visible' && ImpactMojoAuth.user) {
        const lastSync = ImpactMojoAuth.getLastSyncTime();
        if (!lastSync || (new Date() - lastSync) > 5 * 60 * 1000) {
            // Only sync data — do NOT re-fetch profile here (init() handler does that)
            ImpactMojoAuth.syncToCloud().catch(function (e) {
                console.error('Background visibility sync failed:', e);
            });
        }
    }
});

// =====================================================
// AUTO-SYNC BEFORE PAGE UNLOAD
// =====================================================
window.addEventListener('beforeunload', () => {
    if (ImpactMojoAuth.user && !ImpactMojoAuth.isSyncing) {
        console.log('📤 Page unload - data will sync on next visit');
    }
});

// Export for use in other scripts
window.ImpactMojoAuth = ImpactMojoAuth;
window.supabaseClient = supabaseClient;

// Inject auth CSS immediately so .auth-logged-in elements are hidden
// by default (prevents flash of both logged-in and logged-out buttons)
(function () {
    if (document.getElementById('auth-topbar-styles')) return;
    var style = document.createElement('style');
    style.id = 'auth-topbar-styles';
    style.textContent =
        '.auth-logged-in { display: none !important; }' +
        'body.user-authenticated .auth-logged-in { display: inline-flex !important; }' +
        'body.user-authenticated .auth-logged-out { display: none !important; }';
    (document.head || document.documentElement).appendChild(style);
})();

// SYNCHRONOUS auth state recovery from localStorage.
// This runs BEFORE any async Supabase events fire, so the user sees
// their logged-in state instantly on every page — no waiting for
// network calls or event callbacks.
(function () {
    try {
        var sessionRaw = localStorage.getItem('impactmojo-auth');
        if (!sessionRaw) return;
        var session = JSON.parse(sessionRaw);
        if (!session || !session.access_token) return;

        // Session exists — user is logged in. Add class immediately.
        document.body.classList.add('user-authenticated');

        // Restore cached profile for tier/name display
        var cachedRaw = localStorage.getItem('impactmojo_cached_profile');
        if (cachedRaw) {
            try {
                var cached = JSON.parse(cachedRaw);
                if (cached) {
                    ImpactMojoAuth.profile = cached;
                    // Update tier/name displays if they exist
                    document.querySelectorAll('.auth-user-name').forEach(function (el) {
                        el.textContent = cached.display_name || cached.full_name || 'Account';
                    });
                    document.querySelectorAll('.auth-user-tier').forEach(function (el) {
                        var tierNames = { explorer: 'Explorer (Free)', practitioner: 'Practitioner', professional: 'Professional', organization: 'Organization' };
                        el.textContent = tierNames[cached.subscription_tier] || 'Explorer (Free)';
                    });
                }
            } catch (_) {}
        }
    } catch (_) {}
})();
