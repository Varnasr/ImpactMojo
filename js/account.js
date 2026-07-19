/**
 * ImpactMojo Account Page Logic
 * Version: 1.0.0
 * Date: March 16, 2026
 *
 * Extracted from account.html inline <script>.
 * Uses IMState (state-manager.js) for all localStorage access
 * and AuthGate (auth-gate.js) for the authentication gate.
 *
 * PREREQUISITES (loaded before this file):
 *   js/state-manager.js
 *   @supabase/supabase-js (CDN)
 *   js/config.js
 *   js/auth.js
 *   js/auth-gate.js
 */

(function () {
  'use strict';

  // =========================================================================
  // THEME
  // =========================================================================

  // Canonical key is 'im-theme' (matches handouts + cookie-ui.js).
  // Fall back to legacy keys on first read so existing users keep their pick.
  function getPreferredTheme() {
    return localStorage.getItem('im-theme')
        || localStorage.getItem('impactmojo-theme')
        || localStorage.getItem('theme')
        || localStorage.getItem('imx_theme')
        || 'system';
  }
  function applyTheme(theme) {
    var resolved = theme;
    if (theme === 'system') {
      resolved = (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) ? 'dark' : 'light';
    }
    document.documentElement.setAttribute('data-theme', resolved);
    document.body.classList.toggle('light-mode', resolved === 'light');
    document.body.classList.toggle('dark-mode', resolved === 'dark');
    localStorage.setItem('im-theme', theme);
    // Mirror to legacy keys so any page still reading them stays in sync
    localStorage.setItem('impactmojo-theme', theme);
    localStorage.setItem('theme', theme);
    localStorage.setItem('imx_theme', theme);
    document.querySelectorAll('.theme-btn').forEach(function(btn) {
      btn.classList.toggle('active', btn.getAttribute('data-theme') === theme);
    });
  }
  function initTheme() {
    applyTheme(getPreferredTheme());
    document.querySelectorAll('.theme-btn').forEach(function(btn) {
      btn.addEventListener('click', function() { applyTheme(btn.getAttribute('data-theme')); });
    });
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', function() {
      if (getPreferredTheme() === 'system') applyTheme('system');
    });
  }

  // =========================================================================
  // CHATBOT
  // =========================================================================

  function openChatbot() {
    document.getElementById('chatbotModal').classList.add('open');
  }

  function closeChatbot() {
    document.getElementById('chatbotModal').classList.remove('open');
  }

  function selectOption(option) {
    var messages = document.getElementById('chatMessages');
    var response = '';
    switch (option) {
      case 'courses':
        response = 'We offer free courses on MEAL, Theory of Change, Research Methods, Gender Studies, and more! Visit our <a href="catalog.html">Catalog</a> to browse all courses.';
        break;
      case 'contact':
        response = 'You can reach us at <a href="mailto:hello@impactmojo.in">hello@impactmojo.in</a> or visit our <a href="contact.html">Contact page</a>.';
        break;
      case 'feedback':
        response = 'We love hearing from you! Please share your feedback, suggestions, or bug reports. Your input helps us improve ImpactMojo for everyone.';
        break;
      default:
        response = 'How can I help you today?';
    }
    var userMsg = document.createElement('div');
    userMsg.className = 'message';
    userMsg.innerHTML = '<div class="bot-bubble" style="margin-left:auto;background:var(--gradient-primary);color:white;border-radius:12px;border-top-right-radius:4px;">' + (option.charAt(0).toUpperCase() + option.slice(1)) + '</div>';
    messages.appendChild(userMsg);
    setTimeout(function () {
      var botMsg = document.createElement('div');
      botMsg.className = 'message bot-message';
      botMsg.innerHTML = '<div class="bot-avatar"><svg viewBox="0 0 24 24"><rect x="3" y="11" width="18" height="10" rx="2"></rect><circle cx="12" cy="5" r="2"></circle><path d="M12 7v4"></path></svg></div><div class="bot-bubble">' + response + '</div>';
      messages.appendChild(botMsg);
      messages.scrollTop = messages.scrollHeight;
    }, 500);
  }

  function handleChatKeyPress(event) {
    if (event.key === 'Enter') sendChatMessage();
  }

  function sendChatMessage() {
    var input = document.getElementById('chatInput');
    var message = input.value.trim();
    if (!message) return;
    var messages = document.getElementById('chatMessages');
    var userMsg = document.createElement('div');
    userMsg.className = 'message';
    userMsg.innerHTML = '<div class="bot-bubble" style="margin-left:auto;background:var(--gradient-primary);color:white;border-radius:12px;border-top-right-radius:4px;">' + message + '</div>';
    messages.appendChild(userMsg);
    input.value = '';
    setTimeout(function () {
      var response = "Thanks for your message! For detailed assistance, please email us at <a href='mailto:hello@impactmojo.in'>hello@impactmojo.in</a> or visit our <a href='faq.html'>FAQ page</a>.";
      var lowerMsg = message.toLowerCase();
      if (lowerMsg.indexOf('course') !== -1 || lowerMsg.indexOf('learn') !== -1) {
        response = "We offer free courses on MEAL, Theory of Change, Research Methods, and more! Check our <a href='catalog.html'>Catalog</a> for all courses.";
      } else if (lowerMsg.indexOf('password') !== -1 || lowerMsg.indexOf('reset') !== -1) {
        response = "To reset your password, click the 'Change Password' button in Account Settings. We'll send you an email with reset instructions.";
      } else if (lowerMsg.indexOf('premium') !== -1 || lowerMsg.indexOf('upgrade') !== -1) {
        response = "Interested in Premium? Visit our <a href='/premium.html'>Premium page</a> to see all the benefits and features available.";
      }
      var botMsg = document.createElement('div');
      botMsg.className = 'message bot-message';
      botMsg.innerHTML = '<div class="bot-avatar"><svg viewBox="0 0 24 24"><rect x="3" y="11" width="18" height="10" rx="2"></rect><circle cx="12" cy="5" r="2"></circle><path d="M12 7v4"></path></svg></div><div class="bot-bubble">' + response + '</div>';
      messages.appendChild(botMsg);
      messages.scrollTop = messages.scrollHeight;
    }, 800);
  }

  // =========================================================================
  // ALERTS
  // =========================================================================

  function showAlert(message, type) {
    type = type || 'error';
    var alertEl = document.getElementById(type === 'success' ? 'successAlert' : 'errorAlert');
    if (!alertEl) return;
    alertEl.textContent = message;
    alertEl.classList.add('show');
    setTimeout(function () { alertEl.classList.remove('show'); }, 5000);
  }

  // =========================================================================
  // GAMIFICATION CARD
  // =========================================================================

  function updateGamificationCard() {
    var streak = IMState.streak.get();
    var bookmarks = IMState.bookmarks.get();
    var progress = IMState.courseProgress.getAllPercentages();
    var analytics = IMState.analytics.get();

    // --- Streak display ---
    var currentStreak = streak.currentStreak || 0;
    var longestStreak = streak.longestStreak || 0;
    document.getElementById('gamifStreakNum').textContent = currentStreak;
    document.getElementById('gamifBestStreak').textContent = longestStreak;
    var streakEl = document.getElementById('gamifStreak');
    if (currentStreak > 0) {
      streakEl.classList.remove('inactive');
      streakEl.classList.add('active');
    } else {
      streakEl.classList.remove('active');
      streakEl.classList.add('inactive');
    }

    // --- Activity Heatmap (last 84 days / 12 weeks) ---
    var heatmapEl = document.getElementById('gamifHeatmap');
    heatmapEl.innerHTML = '';
    var viewsByItem = (analytics && analytics.viewsByItem) ? analytics.viewsByItem : {};
    var dayCounts = {};
    Object.values(viewsByItem).forEach(function (item) {
      if (item.lastViewed) {
        var dayKey = item.lastViewed.slice(0, 10);
        dayCounts[dayKey] = (dayCounts[dayKey] || 0) + (item.views || 1);
      }
    });
    if (analytics.recentItems && Array.isArray(analytics.recentItems)) {
      analytics.recentItems.forEach(function (ri) {
        if (ri.time) {
          var dayKey = ri.time.slice(0, 10);
          dayCounts[dayKey] = (dayCounts[dayKey] || 0) + 1;
        }
      });
    }
    var today = new Date();
    var startDate = new Date(today);
    startDate.setDate(startDate.getDate() - 83);
    startDate.setDate(startDate.getDate() - startDate.getDay());
    var totalDays = 7 * 12;
    for (var i = 0; i < totalDays; i++) {
      var d = new Date(startDate);
      d.setDate(d.getDate() + i);
      var key = d.toISOString().slice(0, 10);
      var count = dayCounts[key] || 0;
      var cell = document.createElement('div');
      cell.className = 'heatmap-cell';
      cell.title = key + ': ' + count + ' activities';
      if (d > today) { cell.style.opacity = '0.3'; }
      else if (count >= 5) cell.setAttribute('data-level', '4');
      else if (count >= 3) cell.setAttribute('data-level', '3');
      else if (count >= 2) cell.setAttribute('data-level', '2');
      else if (count >= 1) cell.setAttribute('data-level', '1');
      heatmapEl.appendChild(cell);
    }

    // --- Milestone Badges ---
    var badgesEl = document.getElementById('gamifBadges');
    var completedCourses = Object.keys(progress).filter(function (k) { return progress[k] === 100; }).length;
    var bookmarkCount = bookmarks.length;
    var totalViews = analytics.totalViews || 0;
    var labGameCount = Object.values(viewsByItem).filter(function (v) { return v.type === 'lab' || v.type === 'game'; }).length;

    var milestones = [
      { id: '7streak',     label: '7-Day Streak',  earned: currentStreak >= 7 || longestStreak >= 7,     icon: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2L15.09 8.26L22 9.27L17 14.14L18.18 21.02L12 17.77L5.82 21.02L7 14.14L2 9.27L8.91 8.26L12 2z"/></svg>' },
      { id: '30streak',    label: '30-Day Streak', earned: currentStreak >= 30 || longestStreak >= 30,   icon: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 23c-3.866 0-7-3.134-7-7 0-3.107 2.476-6.236 4.5-8.3A16.85 16.85 0 0 1 12 5.3a16.85 16.85 0 0 1 2.5 2.4C16.524 9.764 19 12.893 19 16c0 3.866-3.134 7-7 7z"/></svg>' },
      { id: '100streak',   label: '100-Day Streak', earned: currentStreak >= 100 || longestStreak >= 100, icon: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="8" r="6"/><path d="M15.477 12.89L17 22l-5-3-5 3 1.523-9.11"/></svg>' },
      { id: '5courses',    label: '5 Courses Done', earned: completedCourses >= 5,                       icon: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>' },
      { id: '10bookmarks', label: '10 Bookmarks',   earned: bookmarkCount >= 10,                         icon: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m19 21-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/></svg>' },
      { id: 'labexplorer', label: 'Lab Explorer',   earned: labGameCount >= 3,                           icon: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 3h6v7l4 8H5l4-8V3z"/><line x1="9" y1="3" x2="15" y2="3"/></svg>' },
      { id: '50views',     label: '50 Views',       earned: totalViews >= 50,                             icon: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/></svg>' }
    ];
    badgesEl.innerHTML = '<h4>Milestones</h4>';
    milestones.forEach(function (m) {
      var el = document.createElement('span');
      el.className = 'badge-item' + (m.earned ? ' earned' : '');
      el.innerHTML = m.icon + ' ' + m.label;
      badgesEl.appendChild(el);
    });

    // --- Points Display ---
    var ptsModules = totalViews * 10;
    var ptsCourses = completedCourses * 50;
    var ptsBookmarks = bookmarkCount * 5;
    var ptsLabs = labGameCount * 25;
    var totalPoints = ptsModules + ptsCourses + ptsBookmarks + ptsLabs;
    document.getElementById('gamifPointsTotal').textContent = totalPoints.toLocaleString();
    document.getElementById('gamifPointsBreakdown').innerHTML =
      '<span>' + ptsModules + ' views</span>' +
      '<span>' + ptsCourses + ' courses</span>' +
      '<span>' + ptsBookmarks + ' bookmarks</span>' +
      '<span>' + ptsLabs + ' labs</span>';
  }

  // =========================================================================
  // SAVED ITEMS DISPLAY
  // =========================================================================

  function updateSavedItemsDisplay() {
    try { _updateSavedItemsInner(); } catch (e) {
      console.error('[Account] updateSavedItemsDisplay error:', e);
    }
  }

  function _updateSavedItemsInner() {
    var bookmarks = IMState.bookmarks.get();
    var notes     = IMState.notes.get();
    var progress  = IMState.courseProgress.getAllPercentages();
    var streak    = IMState.streak.get();

    document.getElementById('bookmarkCount').textContent = bookmarks.length;
    document.getElementById('notesCount').textContent = Array.isArray(notes) ? notes.length : Object.keys(notes).length;
    document.getElementById('progressCount').textContent = Object.keys(progress).filter(function (k) { return progress[k] > 0 && progress[k] < 100; }).length;
    document.getElementById('totalBookmarks').textContent = bookmarks.length;
    document.getElementById('streakDays').textContent = streak.currentStreak || 0;
    document.getElementById('coursesCompleted').textContent = Object.keys(progress).filter(function (k) { return progress[k] === 100; }).length;

    updateGamificationCard();
  }

  // =========================================================================
  // COMMUNITY ACCESS
  // =========================================================================

  function updateCommunityAccess(isPremium) {
    var platforms = document.getElementById('communityPlatforms');
    var locked    = document.getElementById('communityLocked');
    if (isPremium) {
      platforms.style.display = 'grid';
      locked.style.display = 'none';
    } else {
      platforms.style.display = 'none';
      locked.style.display = 'block';
    }
  }

  // =========================================================================
  // PAGE DATA UPDATE (called after auth resolves)
  // =========================================================================

  function updatePageData() {
    try { _updatePageDataInner(); } catch (e) {
      console.error('[Account] updatePageData error:', e);
    }
  }

  function _updatePageDataInner() {
    var profile = ImpactMojoAuth.profile || {};
    var user    = ImpactMojoAuth.user || {};

    // Profile display
    document.getElementById('profileName').textContent = profile.full_name || profile.display_name || 'User';
    document.getElementById('profileEmail').textContent = user.email || '';
    document.getElementById('profileOrg').textContent = profile.organization || '';

    // Profile avatar
    var avatarEl = document.getElementById('profileAvatar');
    if (profile.avatar_url) {
      avatarEl.innerHTML = '<img src="' + profile.avatar_url + '" alt="Profile picture">';
    }

    // Profile details display
    _showDetailIf('detailPhone', 'detailPhoneText', profile.phone);
    _showDetailIf('detailBio', 'detailBioText', profile.bio);

    var locationParts = [profile.city, profile.country].filter(Boolean);
    var addressParts = [profile.address].concat(locationParts).filter(Boolean);
    _showDetailIf('detailAddress', 'detailAddressText', addressParts.join(', '));

    if (profile.linkedin_url) {
      document.getElementById('detailLinkedin').style.display = '';
      var linkEl = document.getElementById('detailLinkedinLink');
      linkEl.href = profile.linkedin_url;
      linkEl.textContent = 'LinkedIn Profile';
    }

    if (profile.interests) {
      var tags = profile.interests.split(',').map(function(s) { return s.trim(); }).filter(Boolean);
      if (tags.length > 0) {
        document.getElementById('detailInterests').style.display = '';
        document.getElementById('detailInterestsTags').innerHTML = tags.map(function(t) {
          return '<span class="interest-tag">' + t + '</span>';
        }).join('');
      }
    }

    // Form fields
    document.getElementById('editName').value        = profile.full_name || '';
    document.getElementById('editDisplayName').value  = profile.display_name || '';
    document.getElementById('editOrg').value          = profile.organization || '';
    document.getElementById('editCity').value         = profile.city || '';
    document.getElementById('editCountry').value      = profile.country || '';
    document.getElementById('editLinkedin').value     = profile.linkedin_url || '';
    document.getElementById('editBio').value          = profile.bio || '';
    document.getElementById('editPhone').value        = profile.phone || '';
    document.getElementById('editAddress').value      = profile.address || '';
    document.getElementById('editInterests').value    = profile.interests || '';

    // Subscription display
    var tier      = profile.subscription_tier || 'explorer';
    var isPremium = tier && tier !== 'explorer';
    var tierBadge       = document.getElementById('tierBadge');
    var tierName        = document.getElementById('tierName');
    var tierDescription = document.getElementById('tierDescription');
    var upgradeBanner   = document.getElementById('upgradeBanner');

    if (isPremium) {
      tierBadge.className = 'tier-badge tier-' + tier;
      tierBadge.innerHTML = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg> ' + tier.charAt(0).toUpperCase() + tier.slice(1);
      tierName.textContent = tier.charAt(0).toUpperCase() + tier.slice(1) + ' Tier';
      tierDescription.textContent = 'Full access to premium features';
      upgradeBanner.style.display = 'none';
      var subManage = document.getElementById('subscriptionManage');
      if (subManage) {
        subManage.style.display = 'block';
        var start = profile.subscription_start ? new Date(profile.subscription_start).toLocaleDateString('en-IN', { day: 'numeric', month: 'short', year: 'numeric' }) : 'Active';
        var end   = profile.subscription_end   ? new Date(profile.subscription_end).toLocaleDateString('en-IN', { day: 'numeric', month: 'short', year: 'numeric' })   : 'Ongoing';
        document.getElementById('subPeriod').textContent = start + ' — ' + end;
        if (tier === 'organization') {
          document.getElementById('orgDashLink').style.display = 'inline-block';
        }
      }
    } else {
      upgradeBanner.style.display = 'flex';
    }

    // Certificates
    document.getElementById('certificatesCard').style.display = 'block';
    loadCertificates(user.id);

    // Community
    updateCommunityAccess(isPremium);

    // Sync status
    var syncBadge   = document.getElementById('syncStatusBadge');
    var syncMessage = document.getElementById('syncStatusMessage');
    var syncText    = document.getElementById('syncStatusText');
    var syncBtn     = document.getElementById('syncNowBtn');

    if (ImpactMojoAuth.isLoggedIn()) {
      var lastSync = ImpactMojoAuth.getLastSyncDisplay();
      syncBadge.innerHTML = '<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 10h-1.26A8 8 0 1 0 9 20h9a5 5 0 0 0 0-10z"/></svg> Synced to Cloud';
      syncBadge.className = 'badge badge-premium';
      syncText.textContent = 'Your data is synced across devices. Last sync: ' + lastSync;
      syncMessage.className = 'sync-status synced';
      syncBtn.style.display = 'inline-flex';
    } else {
      syncBtn.style.display = 'none';
    }
  }

  // =========================================================================
  // CERTIFICATES
  // =========================================================================

  async function loadCertificates(userId) {
    try {
      var result = await supabaseClient
        .from('certificates')
        .select('*')
        .eq('user_id', userId)
        .order('issued_at', { ascending: false });
      var certs = result.data;
      var error = result.error;
      if (error || !certs || certs.length === 0) return;

      if (window.IMPACTMOJO && window.IMPACTMOJO.badges && window.IMPACTMOJO.badges.renderBadgeWallet) {
        window.IMPACTMOJO.badges.renderBadgeWallet(certs, 'badgeWalletContainer');
      } else {
        var container = document.getElementById('certificatesList');
        container.style.display = 'flex';
        container.innerHTML = certs.map(function (cert) {
          var date = new Date(cert.issued_at).toLocaleDateString('en-IN', { day: 'numeric', month: 'short', year: 'numeric' });
          var issued = new Date(cert.issued_at);
          var certUrl = cert.verification_url || ('https://www.impactmojo.in/verify-certificate.html?cert=' + cert.certificate_number);
          var linkedInUrl = 'https://www.linkedin.com/profile/add?startTask=CERTIFICATION_NAME' +
            '&name=' + encodeURIComponent((cert.course_name || cert.course_id) + ' — ImpactMojo') +
            '&organizationName=' + encodeURIComponent('ImpactMojo') +
            '&issueYear=' + issued.getFullYear() +
            '&issueMonth=' + (issued.getMonth() + 1) +
            '&certUrl=' + encodeURIComponent(certUrl) +
            '&certId=' + encodeURIComponent(cert.certificate_number);
          return '<div style="display:flex;align-items:center;gap:1rem;padding:0.75rem;background:var(--hover-bg);border-radius:8px;">' +
            '<svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="#10B981" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>' +
            '<div style="flex:1;"><div style="font-weight:500;font-size:0.9rem;">' + (cert.course_name || cert.course_id) + '</div>' +
            '<div style="font-size:0.75rem;color:var(--text-muted);">Issued ' + date + ' &middot; #' + cert.certificate_number + '</div></div>' +
            '<a href="' + linkedInUrl + '" target="_blank" rel="noopener" style="font-size:0.75rem;color:var(--accent-color);white-space:nowrap;">Add to LinkedIn</a>' +
            (cert.verification_url ? '<a href="' + cert.verification_url + '" target="_blank" style="font-size:0.75rem;color:var(--accent-color);">Verify</a>' : '') +
            '</div>';
        }).join('');
      }
    } catch (e) {
      console.error('Failed to load certificates:', e);
    }
  }

  // =========================================================================
  // SYNC NOW
  // =========================================================================

  async function handleSyncNow() {
    var syncBtn     = document.getElementById('syncNowBtn');
    var syncText    = document.getElementById('syncStatusText');
    var syncMessage = document.getElementById('syncStatusMessage');

    if (!ImpactMojoAuth.isLoggedIn()) {
      showAlert('Please log in to sync your data', 'error');
      return;
    }

    syncBtn.disabled = true;
    syncBtn.innerHTML = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="spinning"><polyline points="23 4 23 10 17 10"/><polyline points="1 20 1 14 7 14"/><path d="M3.51 9a9 9 0 0 1 14.85-3.36L23 10M1 14l4.64 4.36A9 9 0 0 0 20.49 15"/></svg> Syncing...';
    syncMessage.className = 'sync-status syncing';
    syncText.textContent = 'Syncing your data...';

    try {
      var result = await ImpactMojoAuth.syncAll();
      if (result.success) {
        showAlert('Data synced successfully!', 'success');
        syncText.textContent = 'Your data is synced across devices. Last sync: ' + ImpactMojoAuth.getLastSyncDisplay();
        syncMessage.className = 'sync-status synced';
        updateSavedItemsDisplay();
      } else {
        showAlert('Sync failed: ' + result.message, 'error');
        syncMessage.className = 'sync-status local';
        syncText.textContent = 'Sync failed. Please try again.';
      }
    } catch (err) {
      showAlert('Sync error: ' + err.message, 'error');
      syncMessage.className = 'sync-status local';
    }

    syncBtn.disabled = false;
    syncBtn.innerHTML = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="23 4 23 10 17 10"/><polyline points="1 20 1 14 7 14"/><path d="M3.51 9a9 9 0 0 1 14.85-3.36L23 10M1 14l4.64 4.36A9 9 0 0 0 20.49 15"/></svg> Sync Now';
  }

  // =========================================================================
  // ACCOUNT ACTIONS
  // =========================================================================

  async function changePassword() {
    var email = ImpactMojoAuth.user ? ImpactMojoAuth.user.email : null;
    if (!email) { showAlert('Please log in first'); return; }
    if (confirm('We will send a password reset link to your email. Continue?')) {
      var result = await ImpactMojoAuth.resetPassword(email);
      showAlert(result.message, result.success ? 'success' : 'error');
    }
  }

  function exportData() {
    var data = {
      profile: ImpactMojoAuth.profile || {},
      localData: {
        bookmarks: IMState.bookmarks.get(),
        notes: IMState.notes.get(),
        progress: IMState.courseProgress.getAllPercentages(),
        streak: IMState.streak.get()
      },
      exportedAt: new Date().toISOString(),
      exportedFrom: 'ImpactMojo Account Dashboard'
    };
    var blob = new Blob([JSON.stringify(data, null, 2)], { type: 'application/json' });
    var url = URL.createObjectURL(blob);
    var a = document.createElement('a');
    a.href = url;
    a.download = 'impactmojo-data-' + new Date().toISOString().split('T')[0] + '.json';
    a.click();
    URL.revokeObjectURL(url);
    showAlert('Your data has been exported!', 'success');
  }

  function clearLocalData() {
    if (confirm('This will clear all your bookmarks, notes, and progress saved in this browser. This cannot be undone. Continue?')) {
      try {
        IMState.clearAllSyncedData();
        showAlert('Browser data cleared successfully!', 'success');
        updateSavedItemsDisplay();
      } catch (e) {
        showAlert('Error clearing data: ' + e.message);
      }
    }
  }

  async function signOut() {
    if (confirm('Are you sure you want to sign out?')) {
      await ImpactMojoAuth.signOut();
    }
  }

  // =========================================================================
  // AUTH STATE LISTENER
  // =========================================================================

  window.addEventListener('authStateChanged', function (e) {
    if (!ImpactMojoAuth.isAuthReady) return;
    if (e.detail && e.detail.isLoggedIn) {
      // Check for signup extras stored during registration
      var signupExtras = localStorage.getItem('impactmojo_signup_extras') || sessionStorage.getItem('impactmojo_signup_extras');
      if (signupExtras) {
        try {
          var extras = JSON.parse(signupExtras);
          localStorage.removeItem('impactmojo_signup_extras'); sessionStorage.removeItem('impactmojo_signup_extras');
          ImpactMojoAuth.updateProfile(extras).then(function () { updatePageData(); });
        } catch (err) {
          console.error('Failed to apply signup extras:', err);
        }
      }
      updatePageData();
      updateSavedItemsDisplay();
    }
  });

  // Note: profile re-fetch on tab focus is handled by auth.js's
  // visibilitychange listener, which dispatches authStateChanged.
  // The authStateChanged listener above calls updatePageData().

  // =========================================================================
  // INITIALIZATION
  // =========================================================================

  document.addEventListener('DOMContentLoaded', function () {
    initTheme();
    updateSavedItemsDisplay();

    // Profile form submit handler
    var profileForm = document.getElementById('profileForm');
    if (profileForm) {
      profileForm.addEventListener('submit', async function (e) {
        e.preventDefault();
        var btn = document.getElementById('saveProfileBtn');
        btn.disabled = true;
        btn.innerHTML = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="spinning"><line x1="12" y1="2" x2="12" y2="6"/><line x1="12" y1="18" x2="12" y2="22"/><line x1="4.93" y1="4.93" x2="7.76" y2="7.76"/><line x1="16.24" y1="16.24" x2="19.07" y2="19.07"/><line x1="2" y1="12" x2="6" y2="12"/><line x1="18" y1="12" x2="22" y2="12"/><line x1="4.93" y1="19.07" x2="7.76" y2="16.24"/><line x1="16.24" y1="7.76" x2="19.07" y2="4.93"/></svg> Saving...';
        var updates = {
          full_name: document.getElementById('editName').value.trim(),
          display_name: document.getElementById('editDisplayName').value.trim(),
          organization: document.getElementById('editOrg').value.trim(),
          city: document.getElementById('editCity').value.trim(),
          country: document.getElementById('editCountry').value.trim(),
          linkedin_url: document.getElementById('editLinkedin').value.trim(),
          bio: document.getElementById('editBio').value.trim(),
          phone: document.getElementById('editPhone').value.trim(),
          address: document.getElementById('editAddress').value.trim(),
          interests: document.getElementById('editInterests').value.trim()
        };
        var result = await ImpactMojoAuth.updateProfile(updates);
        if (result.success) { showAlert('Profile updated successfully!', 'success'); updatePageData(); }
        else { showAlert(result.message || 'Failed to update profile'); }
        btn.disabled = false;
        btn.innerHTML = 'Save Changes';
      });
    }

    // Close dropdowns when clicking outside
    document.addEventListener('click', function (e) {
      if (!e.target.closest('.has-dropdown') && window.innerWidth <= 768) {
        document.querySelectorAll('.has-dropdown.open').forEach(function (el) { el.classList.remove('open'); });
      }
    });

    // Spinning animation style
    var style = document.createElement('style');
    style.textContent = '@keyframes spin{to{transform:rotate(360deg)}}.spinning{animation:spin 1s linear infinite}';
    document.head.appendChild(style);

    // --- Auth Gate ---
    AuthGate.protect({
      loadingEl: document.getElementById('loadingOverlay'),
      redirectUrl: '/login.html',
      timeoutMs: 5000,
      onReady: function (user, profile) {
        updatePageData();
        updateSavedItemsDisplay();
        if (typeof DashboardTabs !== 'undefined') DashboardTabs.init('account', profile);
      }
    });
  });

  // =========================================================================
  // PROFILE HELPERS
  // =========================================================================

  function _showDetailIf(wrapperId, textId, value) {
    var wrapper = document.getElementById(wrapperId);
    var text = document.getElementById(textId);
    if (value) {
      wrapper.style.display = '';
      text.textContent = value;
    } else {
      wrapper.style.display = 'none';
    }
  }

  async function handleAvatarUpload(input) {
    if (!input.files || !input.files[0]) return;
    var file = input.files[0];

    // Validate file
    if (!file.type.startsWith('image/')) {
      showAlert('Please select an image file.', 'error');
      return;
    }
    if (file.size > 2 * 1024 * 1024) {
      showAlert('Image must be under 2MB.', 'error');
      return;
    }

    var user = ImpactMojoAuth.user;
    if (!user) return;

    // Read as data URL for immediate preview
    var reader = new FileReader();
    reader.onload = function (e) {
      var avatarEl = document.getElementById('profileAvatar');
      avatarEl.innerHTML = '<img src="' + e.target.result + '" alt="Profile picture">';
    };
    reader.readAsDataURL(file);

    // Upload to Supabase Storage
    try {
      var supabase = window.supabase ? null : null; // Use the global client
      var client = (typeof ImpactMojoAuth !== 'undefined' && ImpactMojoAuth._supabase) ? ImpactMojoAuth._supabase : null;
      if (!client && window.ImpactMojoConfig) {
        // Fall back: get the client from the global scope
        client = window._supabaseClient || null;
      }

      if (client) {
        var ext = file.name.split('.').pop();
        var filePath = 'avatars/' + user.id + '.' + ext;

        var uploadResult = await client.storage.from('avatars').upload(filePath, file, { upsert: true });
        if (uploadResult.error) {
          console.warn('[Account] Avatar upload failed:', uploadResult.error.message);
          // Still save the data URL as fallback
          var dataUrl = document.querySelector('#profileAvatar img');
          if (dataUrl) {
            await ImpactMojoAuth.updateProfile({ avatar_url: dataUrl.src });
          }
          return;
        }

        var publicUrl = client.storage.from('avatars').getPublicUrl(filePath);
        if (publicUrl.data && publicUrl.data.publicUrl) {
          await ImpactMojoAuth.updateProfile({ avatar_url: publicUrl.data.publicUrl });
          showAlert('Profile picture updated!', 'success');
        }
      } else {
        // No Supabase storage available — store as data URL in profile
        var imgEl = document.querySelector('#profileAvatar img');
        if (imgEl && imgEl.src.startsWith('data:')) {
          await ImpactMojoAuth.updateProfile({ avatar_url: imgEl.src });
          showAlert('Profile picture saved!', 'success');
        }
      }
    } catch (err) {
      console.error('[Account] Avatar upload error:', err);
      showAlert('Could not upload picture. Changes saved locally.', 'info');
    }
  }

  // =========================================================================
  // EXPOSE GLOBALS (required for onclick="" attributes in HTML)
  // =========================================================================

  window.applyTheme        = applyTheme;
  window.openChatbot       = openChatbot;
  window.closeChatbot      = closeChatbot;
  window.selectOption      = selectOption;
  window.handleChatKeyPress = handleChatKeyPress;
  window.sendChatMessage   = sendChatMessage;
  window.handleSyncNow     = handleSyncNow;
  window.changePassword    = changePassword;
  window.exportData        = exportData;
  window.clearLocalData    = clearLocalData;
  window.signOut           = signOut;
  window.showAlert         = showAlert;
  window.handleAvatarUpload = handleAvatarUpload;

})();
