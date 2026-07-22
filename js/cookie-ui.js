        // Cookie Consent
        window.addEventListener('DOMContentLoaded', () => {
            if (!localStorage.getItem('cookieConsent')) {
                document.getElementById('cookieConsent').style.display = 'block';
            } else {
                document.getElementById('cookieConsent').classList.add('hidden');
            }
            
            // Initialize Google Calendar buttons for coaching
            if (window.calendar && window.calendar.schedulingButton) {
                const bookingContainers = document.querySelectorAll('.booking-button-container');
                bookingContainers.forEach((container) => {
                    window.calendar.schedulingButton.load({
                        url: 'https://calendar.google.com/calendar/appointments/schedules/AcZssZ2DlCV8HgdkAK-Oyzi9PhKJ45eKo6026Ix1nEEH8Vcx_lxfaCAZlzkcBvptD2sZm1P4fvHjU_Cq?gv=true',
                        color: '#039BE5',
                        label: 'Book an appointment',
                        target: container,
                    });
                });
            }
        });

        // What's New Card Toggle
        function toggleWhatsNewCard(card) {
            // Close other expanded cards
            document.querySelectorAll('.whats-new-card.expanded').forEach(function(c) {
                if (c !== card) {
                    c.classList.remove('expanded');
                }
            });
            // Toggle this card
            card.classList.toggle('expanded');
        }

        // Copy UPI ID
        function copyUPI() {
            var upiId = document.getElementById('upiId');
            if (upiId) {
                var text = upiId.textContent || upiId.innerText;
                navigator.clipboard.writeText(text).then(function() {
                    var btn = document.querySelector('.upi-copy-btn');
                    var originalText = btn.textContent;
                    btn.textContent = 'Copied!';
                    btn.style.background = '#059669';
                    setTimeout(function() {
                        btn.textContent = originalText;
                        btn.style.background = '#10B981';
                    }, 2000);
                    
                    if (typeof IMX !== 'undefined' && IMX.showToast) {
                        IMX.showToast('UPI ID copied: ' + text);
                    }
                }).catch(function(err) {
                    // Fallback for older browsers
                    var tempInput = document.createElement('input');
                    tempInput.value = text;
                    document.body.appendChild(tempInput);
                    tempInput.select();
                    document.execCommand('copy');
                    document.body.removeChild(tempInput);
                    
                    var btn = document.querySelector('.upi-copy-btn');
                    btn.textContent = 'Copied!';
                    setTimeout(function() {
                        btn.textContent = 'Copy';
                    }, 2000);
                });
            }
        }

        // Copy UPI ID in Support Modal
        function copySupportUPI() {
            var upiId = document.getElementById('supportUpiId');
            if (upiId) {
                var text = upiId.textContent || upiId.innerText;
                navigator.clipboard.writeText(text).then(function() {
                    var btn = document.querySelector('.support-upi-copy');
                    var originalHTML = btn.innerHTML;
                    btn.innerHTML = '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg><span>Copied!</span>';
                    btn.style.background = '#059669';
                    setTimeout(function() {
                        btn.innerHTML = originalHTML;
                        btn.style.background = '#10B981';
                    }, 2000);
                    
                    if (typeof IMX !== 'undefined' && IMX.showToast) {
                        IMX.showToast('UPI ID copied: ' + text);
                    }
                }).catch(function(err) {
                    // Fallback for older browsers
                    var tempInput = document.createElement('input');
                    tempInput.value = text;
                    document.body.appendChild(tempInput);
                    tempInput.select();
                    document.execCommand('copy');
                    document.body.removeChild(tempInput);
                    
                    var btn = document.querySelector('.support-upi-copy span');
                    if (btn) btn.textContent = 'Copied!';
                    setTimeout(function() {
                        if (btn) btn.textContent = 'Copy';
                    }, 2000);
                });
            }
        }

        // Update file name display when file is selected
        function updateFileName(input) {
            var fileName = input.files[0] ? input.files[0].name : 'Click to upload screenshot';
            var display = document.getElementById('fileNameDisplay');
            var box = input.closest('.file-upload-box');
            
            if (input.files[0]) {
                display.textContent = fileName;
                box.classList.add('has-file');
            } else {
                display.textContent = 'Click to upload screenshot';
                box.classList.remove('has-file');
            }
        }

        // Form submission handling with success feedback
        document.addEventListener('DOMContentLoaded', function() {
            // Support Form
            var supportForm = document.getElementById('supportForm');
            if (supportForm) {
                supportForm.addEventListener('submit', function(e) {
                    var btn = this.querySelector('.form-submit-btn');
                    btn.innerHTML = '<svg class="spinner" viewBox="0 0 24 24" width="18" height="18"><circle cx="12" cy="12" r="10" stroke="currentColor" stroke-width="3" fill="none" stroke-dasharray="31.4 31.4" stroke-linecap="round"><animateTransform attributeName="transform" type="rotate" values="0 12 12;360 12 12" dur="1s" repeatCount="indefinite"/></circle></svg> Sending...';
                    btn.disabled = true;
                });
            }
            
            // Contact Form
            var contactForm = document.getElementById('contactForm');
            if (contactForm) {
                contactForm.addEventListener('submit', function(e) {
                    var btn = this.querySelector('.form-submit-btn');
                    btn.innerHTML = '<svg class="spinner" viewBox="0 0 24 24" width="18" height="18"><circle cx="12" cy="12" r="10" stroke="currentColor" stroke-width="3" fill="none" stroke-dasharray="31.4 31.4" stroke-linecap="round"><animateTransform attributeName="transform" type="rotate" values="0 12 12;360 12 12" dur="1s" repeatCount="indefinite"/></circle></svg> Sending...';
                    btn.disabled = true;
                });
            }
        });

        // Cookie Consent Functions
        function toggleCookieExpand() {
            var cookieEl = document.getElementById('cookieConsent');
            if (cookieEl) {
                cookieEl.classList.toggle('expanded');
            }
        }

        function acceptCookies() {
            localStorage.setItem('cookieConsent', 'true');
            var cookieEl = document.getElementById('cookieConsent');
            if (cookieEl) {
                cookieEl.classList.remove('expanded');
                cookieEl.classList.add('hidden');
            }
        }

        // Theme Toggle
        // Theme Selection System
        //
        // Canonical localStorage key is 'im-theme' (matches the 89 handout pages
        // and the handout template). On first read we migrate any value set by
        // the older keys ('theme', 'impactmojo-theme', 'imx_theme') so existing
        // users keep their preference when the site updates.
        function readTheme() {
            var t = localStorage.getItem('im-theme');
            if (t) return t;
            // Migrate legacy keys (one-shot, newest-first precedence)
            var legacy = localStorage.getItem('theme')
                      || localStorage.getItem('impactmojo-theme')
                      || localStorage.getItem('imx_theme');
            if (legacy) {
                localStorage.setItem('im-theme', legacy);
                return legacy;
            }
            return 'system';
        }
        function writeTheme(theme) {
            localStorage.setItem('im-theme', theme);
        }
        function initThemeSelector() {
            const themeBtns = document.querySelectorAll('.theme-btn');
            const currentTheme = readTheme();

            // Set initial active state
            updateActiveThemeButton(currentTheme);
            applyTheme(currentTheme);

            // Add click handlers
            themeBtns.forEach(btn => {
                btn.addEventListener('click', () => {
                    const theme = btn.dataset.theme;
                    writeTheme(theme);
                    updateActiveThemeButton(theme);
                    applyTheme(theme);
                });
            });
        }

        function updateActiveThemeButton(theme) {
            document.querySelectorAll('.theme-btn').forEach(btn => {
                btn.classList.toggle('active', btn.dataset.theme === theme);
            });
        }

        function applyTheme(theme) {
            if (theme === 'system') {
                const systemTheme = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
                document.body.classList.toggle('dark-mode', systemTheme === 'dark');
                document.documentElement.setAttribute('data-theme', systemTheme);
            } else {
                document.body.classList.toggle('dark-mode', theme === 'dark');
                document.documentElement.setAttribute('data-theme', theme);
            }
        }

        // Listen for system theme changes
        window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
            const currentTheme = readTheme();
            if (currentTheme === 'system') {
                applyTheme('system');
            }
        });

        // Load theme immediately to prevent flash
        (function() {
            var savedTheme = localStorage.getItem('im-theme')
                          || localStorage.getItem('theme')
                          || localStorage.getItem('impactmojo-theme')
                          || localStorage.getItem('imx_theme')
                          || 'system';
            var isDark;
            
            if (savedTheme === 'dark') {
                isDark = true;
            } else if (savedTheme === 'light') {
                isDark = false;
            } else {
                // System theme - check device preference
                isDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
            }
            
            if (isDark) {
                document.documentElement.classList.add('dark-mode');
                document.body.classList.add('dark-mode');
            }
        })();
        
        // Initialize theme selector when DOM is ready
        window.addEventListener('DOMContentLoaded', () => {
            initThemeSelector();
        });

        // NOTE: toggleMobileMenu() and closeMobileMenu() are defined in <head> section
        // Do not duplicate them here - the global definitions take precedence
        
        // Mobile menu touch handling is now in inline script in <head>
