// ImpactMojo Bookmarks, Compare, and Lo-Fi Features
// Direct global attachment (no IIFE to avoid scoping issues)

var IMX = window.IMX || {};
window.IMX = IMX;

// ========================================
// RICH COURSE DATA FOR COMPARISON
// ========================================
var IMPACTMOJO_COURSE_DATA = {
    'gender-101': {
        name: 'Gender 101',
        type: 'Course',
        rating: '4.8',
        learners: '250+',
        description: 'Comprehensive exploration of gender theory, intersectionality, and social implications in development contexts',
        objectives: ['Understand foundational gender concepts', 'Analyze intersectionality in practice', 'Apply gender analysis frameworks', 'Develop gender-sensitive designs'],
        audience: 'Beginners to Intermediate',
        duration: '4-6 hours',
        format: 'Self-paced online',
        url: '/courses/gender/'
    },
    'meal-101': {
        name: 'MEAL 101',
        type: 'Course',
        rating: '4.9',
        learners: '350+',
        description: 'Monitoring, Evaluation, Accountability and Learning frameworks for impact measurement',
        objectives: ['Design robust M&E frameworks', 'Create effective indicators', 'Implement accountability mechanisms', 'Build learning loops'],
        audience: 'All levels',
        duration: '6-8 hours',
        format: 'Self-paced online',
        url: '/101-courses/mel-basics.html'
    },
    'climate-101': {
        name: 'Climate 101',
        type: 'Course',
        rating: '4.7',
        learners: '180+',
        description: 'Understanding climate change science, impacts, and resilience strategies for development',
        objectives: ['Understand climate science', 'Analyze climate impacts', 'Design climate-resilient interventions', 'Integrate climate into programs'],
        audience: 'Beginners to Intermediate',
        duration: '5-7 hours',
        format: 'Self-paced online',
        url: '/101-courses/climate-essentials.html'
    },
    'toc-workbench': {
        name: 'Theory of Change Workbench',
        type: 'Lab',
        rating: '4.8',
        learners: '420+',
        description: 'Interactive tool for developing and visualizing theory of change',
        objectives: ['Build comprehensive theories of change', 'Map assumptions and evidence', 'Create visual TOC diagrams', 'Export and share documents'],
        audience: 'Intermediate to Advanced',
        duration: '2-4 hours per project',
        format: 'Interactive web tool',
        url: '/Labs/toc-lab.html'
    },
    'logframe-lab': {
        name: 'LogFrame Lab',
        type: 'Lab',
        rating: '4.7',
        learners: '380+',
        description: 'Design monitoring, evaluation, and learning frameworks',
        objectives: ['Create logical frameworks', 'Define SMART indicators', 'Build results chains', 'Export professional documents'],
        audience: 'Intermediate',
        duration: '3-5 hours per project',
        format: 'Interactive web tool',
        url: '/Labs/mel-plan-lab.html'
    },
    'storytelling-lab': {
        name: 'Storytelling Lab',
        type: 'Lab',
        rating: '4.8',
        learners: '290+',
        description: 'Craft compelling narratives for social impact',
        objectives: ['Structure impactful stories', 'Use data visualization', 'Create multimedia stories', 'Apply ethical storytelling'],
        audience: 'All levels',
        duration: '2-3 hours',
        format: 'Interactive exercises',
        url: '/Labs/storytelling-lab.html'
    },
    'middle-class-game': {
        name: 'The Middle Class Game',
        type: 'Game',
        rating: '4.6',
        learners: '520+',
        description: 'Understand who the middle-class really is in India through wealth inequality dynamics',
        objectives: ['Explore income distribution', 'Understand wealth inequality', 'Challenge economic assumptions', 'Apply economic thinking'],
        audience: 'All levels',
        duration: '30-45 minutes',
        format: 'Interactive simulation',
        url: '/Games/real-middle-india.html'
    },
    'prospect-theory': {
        name: 'Prospect Theory Game',
        type: 'Game',
        rating: '4.7',
        learners: '340+',
        description: 'Experience behavioral economics through prospect theory and cognitive biases',
        objectives: ['Understand loss aversion', 'Recognize framing effects', 'Apply behavioral insights', 'Analyze decision-making'],
        audience: 'Intermediate',
        duration: '20-30 minutes',
        format: 'Interactive simulation',
        url: '/Games/risk-reward-game.html'
    },
    'public-good-game': {
        name: 'Public Good Game',
        type: 'Game',
        rating: '4.8',
        learners: '450+',
        description: 'Experience the free-rider problem and public goods dilemma',
        objectives: ['Understand public goods economics', 'Experience free-rider dynamics', 'Analyze collective action', 'Explore cooperation mechanisms'],
        audience: 'All levels',
        duration: '20-30 minutes',
        format: 'Interactive simulation',
        url: '/Games/public-good-game.html'
    },
    'prisoners-dilemma': {
        name: 'Prisoners Dilemma',
        type: 'Game',
        rating: '4.8',
        learners: '380+',
        description: 'Navigate strategic decisions where individual rationality conflicts with collective benefit',
        objectives: ['Understand the classic dilemma', 'Explore cooperation strategies', 'Analyze repeated games', 'Apply to coordination problems'],
        audience: 'All levels',
        duration: '15-25 minutes',
        format: 'Interactive simulation',
        url: '/Games/prisoners-dilemma-game.html'
    }
};

// ========================================
// LEARNING ANALYTICS (localStorage-based)
// ========================================
IMX.Analytics = {
    STORAGE_KEY: 'impactmojo_analytics',
    
    getData: function() {
        try {
            return JSON.parse(localStorage.getItem(this.STORAGE_KEY)) || this.getDefaultData();
        } catch(e) {
            return this.getDefaultData();
        }
    },
    
    getDefaultData: function() {
        return {
            totalViews: 0,
            totalTimeSeconds: 0,
            sessions: 0,
            firstVisit: null,
            lastVisit: null,
            viewsByItem: {},
            recentItems: [],
            currentSessionStart: null
        };
    },
    
    saveData: function(data) {
        localStorage.setItem(this.STORAGE_KEY, JSON.stringify(data));
    },
    
    trackView: function(itemId, itemName, itemType) {
        var data = this.getData();
        data.totalViews++;
        data.lastVisit = new Date().toISOString();
        if (!data.firstVisit) data.firstVisit = data.lastVisit;
        
        // Track by item
        if (!data.viewsByItem[itemId]) {
            data.viewsByItem[itemId] = { name: itemName, type: itemType, views: 0 };
        }
        data.viewsByItem[itemId].views++;
        data.viewsByItem[itemId].lastViewed = data.lastVisit;
        
        // Track recent items (keep last 10)
        data.recentItems = data.recentItems.filter(function(i) { return i.id !== itemId; });
        data.recentItems.unshift({ id: itemId, name: itemName, type: itemType, time: data.lastVisit });
        if (data.recentItems.length > 10) data.recentItems = data.recentItems.slice(0, 10);
        
        this.saveData(data);
    },
    
    startSession: function() {
        var data = this.getData();
        data.sessions++;
        data.currentSessionStart = Date.now();
        this.saveData(data);
    },
    
    endSession: function() {
        var data = this.getData();
        if (data.currentSessionStart) {
            var sessionTime = Math.floor((Date.now() - data.currentSessionStart) / 1000);
            data.totalTimeSeconds += sessionTime;
            data.currentSessionStart = null;
            this.saveData(data);
        }
    },
    
    getSummary: function() {
        var data = this.getData();
        var topItems = Object.keys(data.viewsByItem)
            .map(function(key) { return Object.assign({ id: key }, data.viewsByItem[key]); })
            .sort(function(a, b) { return b.views - a.views; })
            .slice(0, 5);
        
        var totalMinutes = Math.floor(data.totalTimeSeconds / 60);
        var hours = Math.floor(totalMinutes / 60);
        var mins = totalMinutes % 60;
        var timeStr = hours > 0 ? hours + 'h ' + mins + 'm' : mins + ' minutes';
        
        return {
            totalViews: data.totalViews,
            totalTime: timeStr,
            totalTimeSeconds: data.totalTimeSeconds,
            sessions: data.sessions,
            firstVisit: data.firstVisit ? new Date(data.firstVisit).toLocaleDateString() : 'Never',
            lastVisit: data.lastVisit ? new Date(data.lastVisit).toLocaleDateString() : 'Never',
            topItems: topItems,
            recentItems: data.recentItems.slice(0, 5)
        };
    },
    
    clear: function() {
        localStorage.removeItem(this.STORAGE_KEY);
        IMX.showToast('Analytics data cleared');
    }
};

// Start session on page load
IMX.Analytics.startSession();

// End session when leaving
window.addEventListener('beforeunload', function() {
    IMX.Analytics.endSession();
});

// ========================================
// SPEED DIAL MENU
// ========================================
IMX.SpeedDial = {
    isOpen: false,
    
    toggle: function() {
        if (this.isOpen) {
            this.close();
        } else {
            this.open();
        }
    },
    
    open: function() {
        var dial = document.getElementById('imxSpeedDial');
        if (dial) {
            dial.classList.add('open');
            this.isOpen = true;
        }
    },
    
    close: function() {
        var dial = document.getElementById('imxSpeedDial');
        if (dial) {
            dial.classList.remove('open');
            this.isOpen = false;
        }
    }
};

// Close speed dial on Escape key
document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape' && IMX.SpeedDial.isOpen) {
        IMX.SpeedDial.close();
    }
});

// ========================================
// DAILY LEARNING TIPS
// ========================================
IMX.DailyTip = {
    tips: [
        "Theory of Change is not just a document. It's a living roadmap. Review and update yours quarterly as you learn what works.",
        "The best M&E systems are designed WITH communities, not FOR them. Participatory approaches increase data quality and ownership.",
        "Disaggregate your data by gender, age, and location. Averages often hide who's being left behind.",
        "Qualitative data is not 'soft' data. Stories and context explain the 'why' behind the numbers.",
        "Baseline data isn't just a requirement. It's your starting point for measuring real change. Don't skip it!",
        "The Sustainable Development Goals are interconnected. Solving one problem often requires addressing multiple SDGs.",
        "Cost-effectiveness analysis helps donors compare impact across programs. Learn to calculate and communicate yours.",
        "Adaptive management means being willing to change course when evidence shows a better path.",
        "The 'Do No Harm' principle should guide every intervention. Always assess potential negative consequences.",
        "Capacity building isn't just training. It's about creating systems that sustain after the project ends.",
        "Mixed methods research combines the best of quantitative and qualitative. Use them together for richer insights.",
        "Randomized Controlled Trials (RCTs) are the gold standard, but not always feasible. Know your alternatives.",
        "Social accountability mechanisms empower communities to hold service providers responsible.",
        "Gender analysis should happen at design stage, not be retrofitted later.",
        "Systems thinking helps you see the interconnections that simple logic models miss.",
        "Behavior change takes time. Design your program timelines and expectations accordingly.",
        "Local ownership is the key to sustainability. Build it from day one.",
        "Data visualization can tell a story that numbers alone cannot. Learn the basics.",
        "Ethical considerations in research protect vulnerable populations. Never compromise on informed consent.",
        "Network effects can amplify your impact. Think about how change spreads through communities."
    ],
    
    currentIndex: 0,
    
    init: function() {
        // Check if element exists before initializing
        var tipEl = document.getElementById('imxDailyTipText');
        if (!tipEl) {
            console.warn('Daily Tip element not found. Skipping initialization.');
            return;
        }
        
        // Show a tip based on the day of year for consistency
        var dayOfYear = Math.floor((new Date() - new Date(new Date().getFullYear(), 0, 0)) / (1000 * 60 * 60 * 24));
        this.currentIndex = dayOfYear % this.tips.length;
        this.display(this.tips[this.currentIndex]);
    },
    
    showRandom: function() {
        var newIndex;
        do {
            newIndex = Math.floor(Math.random() * this.tips.length);
        } while (newIndex === this.currentIndex && this.tips.length > 1);
        
        this.currentIndex = newIndex;
        this.display(this.tips[this.currentIndex]);
        
        // Add a little animation
        var tipEl = document.getElementById('imxDailyTipText');
        if (tipEl) {
            tipEl.style.opacity = '0';
            setTimeout(function() {
                tipEl.style.opacity = '1';
            }, 150);
        }
    },
    
    display: function(tip) {
        var tipEl = document.getElementById('imxDailyTipText');
        if (tipEl) {
            tipEl.textContent = tip;
            tipEl.style.transition = 'opacity 0.3s ease';
        }
    }
};

// Initialize daily tip on page load
document.addEventListener('DOMContentLoaded', function() {
    // Try to initialize immediately
    if (typeof IMX !== 'undefined' && IMX.DailyTip) {
        IMX.DailyTip.init();
        
        // If element still shows "Loading tip...", retry after a brief delay
        setTimeout(function() {
            var tipEl = document.getElementById('imxDailyTipText');
            if (tipEl && tipEl.textContent === 'Loading tip...') {
                IMX.DailyTip.init();
            }
        }, 500);
    }
});

// ========================================
// SURPRISE ME (Random Content Picker)
// ========================================
IMX.surpriseMe = function() {
    // Collect all content cards
    var cards = document.querySelectorAll('.card');
    if (cards.length === 0) {
        alert('No content found!');
        return;
    }
    
    // Pick a random card
    var randomIndex = Math.floor(Math.random() * cards.length);
    var randomCard = cards[randomIndex];
    
    // Scroll to it
    randomCard.scrollIntoView({ behavior: 'smooth', block: 'center' });
    
    // Add a highlight effect
    randomCard.style.transition = 'all 0.3s ease';
    randomCard.style.boxShadow = '0 0 0 4px #EC4899, 0 0 30px rgba(236, 72, 153, 0.5)';
    randomCard.style.transform = 'scale(1.02)';
    
    // Remove highlight after 2 seconds
    setTimeout(function() {
        randomCard.style.boxShadow = '';
        randomCard.style.transform = '';
    }, 2000);
    
    // Get the card title for feedback
    var titleEl = randomCard.querySelector('.card-title, h3');
    var title = titleEl ? titleEl.textContent : 'content';
    
    // Show a toast notification (simple)
    IMX.showToast('Discovered: ' + title);
};

// Simple toast notification
IMX.showToast = function(message) {
    // Remove existing toast
    var existing = document.getElementById('imxToast');
    if (existing) existing.remove();
    
    // Create toast
    var toast = document.createElement('div');
    toast.id = 'imxToast';
    toast.style.cssText = 'position: fixed; bottom: 100px; left: 50%; transform: translateX(-50%); background: var(--card-bg); color: var(--text-primary); padding: 1rem 1.5rem; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.3); z-index: 9999; font-weight: 500; border: 1px solid var(--border-color); animation: toastIn 0.3s ease;';
    toast.textContent = message;
    document.body.appendChild(toast);
    
    // Add animation styles if not present
    if (!document.getElementById('toastStyles')) {
        var style = document.createElement('style');
        style.id = 'toastStyles';
        style.textContent = '@keyframes toastIn { from { opacity: 0; transform: translateX(-50%) translateY(20px); } to { opacity: 1; transform: translateX(-50%) translateY(0); } }';
        document.head.appendChild(style);
    }
    
    // Remove after 3 seconds
    setTimeout(function() {
        toast.style.opacity = '0';
        toast.style.transition = 'opacity 0.3s ease';
        setTimeout(function() { toast.remove(); }, 300);
    }, 3000);
};

// ========================================
// POMODORO TIMER
// ========================================
IMX.Pomodoro = {
    timer: null,
    timeLeft: 25 * 60, // seconds
    totalTime: 25 * 60,
    isRunning: false,
    currentLabel: 'Focus Time',
    
    STORAGE_KEY: 'imx_pomodoro_stats',
    
    init: function() {
        this.loadStats();
        this.updateDisplay();
    },
    
    openModal: function() {
        document.getElementById('imxPomodoroModal').style.display = 'flex';
        this.loadStats();
    },
    
    closeModal: function() {
        document.getElementById('imxPomodoroModal').style.display = 'none';
    },
    
    start: function() {
        if (this.isRunning) return;
        this.isRunning = true;
        
        document.getElementById('imxPomodoroStart').style.display = 'none';
        document.getElementById('imxPomodoroPause').style.display = 'inline-flex';
        document.getElementById('imxPomodoroFab').classList.add('active');
        
        var self = this;
        this.timer = setInterval(function() {
            self.timeLeft--;
            self.updateDisplay();
            
            if (self.timeLeft <= 0) {
                self.complete();
            }
        }, 1000);
    },
    
    pause: function() {
        this.isRunning = false;
        clearInterval(this.timer);
        
        document.getElementById('imxPomodoroStart').style.display = 'inline-flex';
        document.getElementById('imxPomodoroPause').style.display = 'none';
        document.getElementById('imxPomodoroFab').classList.remove('active');
    },
    
    reset: function() {
        this.pause();
        this.timeLeft = this.totalTime;
        this.updateDisplay();
    },
    
    setPreset: function(minutes, label) {
        this.pause();
        this.totalTime = minutes * 60;
        this.timeLeft = this.totalTime;
        this.currentLabel = label;
        this.updateDisplay();
        document.getElementById('imxPomodoroLabel').textContent = label;
        
        // Update active preset button
        document.querySelectorAll('.imx-pomodoro-preset').forEach(function(btn) {
            btn.classList.remove('active');
            if (btn.textContent.includes(minutes + ' min')) {
                btn.classList.add('active');
            }
        });
    },
    
    complete: function() {
        this.pause();
        this.playSound();
        
        // Save stats
        var stats = this.getStats();
        stats.sessions++;
        stats.totalMinutes += Math.floor(this.totalTime / 60);
        stats.lastDate = new Date().toDateString();
        this.saveStats(stats);
        this.displayStats(stats);
        
        // Show notification
        if (Notification.permission === 'granted') {
            new Notification('Pomodoro Complete!', {
                body: this.currentLabel + ' session finished. Great work!',
                icon: '/favicon.ico'
            });
        }
        
        alert('' + this.currentLabel + ' complete! Take a break.');
        this.reset();
    },
    
    playSound: function() {
        try {
            var audio = new Audio('data:audio/wav;base64,UklGRl9vT19XQVZFZm10IBAAAAABAAEAQB8AAEAfAAABAAgAZGF0YU');
            audio.volume = 0.5;
            audio.play().catch(function() {});
        } catch(e) {}
    },
    
    updateDisplay: function() {
        var mins = Math.floor(this.timeLeft / 60);
        var secs = this.timeLeft % 60;
        var display = (mins < 10 ? '0' : '') + mins + ':' + (secs < 10 ? '0' : '') + secs;
        document.getElementById('imxPomodoroTime').textContent = display;
    },
    
    getStats: function() {
        try {
            var stored = localStorage.getItem(this.STORAGE_KEY);
            if (stored) {
                var stats = JSON.parse(stored);
                // Reset if different day
                if (stats.lastDate !== new Date().toDateString()) {
                    stats.sessions = 0;
                }
                return stats;
            }
        } catch(e) {}
        return { sessions: 0, totalMinutes: 0, lastDate: new Date().toDateString() };
    },
    
    saveStats: function(stats) {
        try {
            localStorage.setItem(this.STORAGE_KEY, JSON.stringify(stats));
        } catch(e) {}
    },
    
    loadStats: function() {
        var stats = this.getStats();
        this.displayStats(stats);
    },
    
    displayStats: function(stats) {
        document.getElementById('imxPomodoroSessions').textContent = stats.sessions;
        var hours = Math.floor(stats.totalMinutes / 60);
        var mins = stats.totalMinutes % 60;
        document.getElementById('imxPomodoroTotal').textContent = hours + 'h ' + mins + 'm';
    }
};

// Request notification permission on load
if ('Notification' in window && Notification.permission === 'default') {
    Notification.requestPermission();
}

// ========================================
// SMART READING LISTS (Curated Resources)
// ========================================
IMX.ReadingLists = {
    // SVG icons for reading list categories
    icons: {
        chart: '<svg viewBox="0 0 24 24" width="24" height="24"><line x1="18" y1="20" x2="18" y2="10" stroke="currentColor" stroke-width="1.5" fill="none"></line><line x1="12" y1="20" x2="12" y2="4" stroke="currentColor" stroke-width="1.5" fill="none"></line><line x1="6" y1="20" x2="6" y2="14" stroke="currentColor" stroke-width="1.5" fill="none"></line></svg>',
        target: '<svg viewBox="0 0 24 24" width="24" height="24"><circle cx="12" cy="12" r="10" stroke="currentColor" stroke-width="1.5" fill="none"></circle><circle cx="12" cy="12" r="6" stroke="currentColor" stroke-width="1.5" fill="none"></circle><circle cx="12" cy="12" r="2" stroke="currentColor" stroke-width="1.5" fill="none"></circle></svg>',
        balance: '<svg viewBox="0 0 24 24" width="24" height="24"><path d="M12 3v18M3 9l3-3 3 3M3 9v3c0 2 2 3 5 3M21 9l-3-3-3 3M21 9v3c0 2-2 3-5 3" stroke="currentColor" stroke-width="1.5" fill="none"></path></svg>',
        flask: '<svg viewBox="0 0 24 24" width="24" height="24"><path d="M9 3h6M10 3v6l-5 8.5c-.5.8.2 1.5 1 1.5h12c.8 0 1.5-.7 1-1.5L14 9V3" stroke="currentColor" stroke-width="1.5" fill="none"></path></svg>',
        brain: '<svg viewBox="0 0 24 24" width="24" height="24"><path d="M12 4.5a2.5 2.5 0 0 0-4.96-.46 2.5 2.5 0 0 0-1.98 3 2.5 2.5 0 0 0 .47 4.96 2.5 2.5 0 0 0 2.97 2.97 2.5 2.5 0 0 0 3.5 0 2.5 2.5 0 0 0 2.97-2.97 2.5 2.5 0 0 0 .47-4.96 2.5 2.5 0 0 0-1.98-3A2.5 2.5 0 0 0 12 4.5" stroke="currentColor" stroke-width="1.5" fill="none"></path><path d="M12 12v8" stroke="currentColor" stroke-width="1.5" fill="none"></path></svg>'
    },
    
    lists: {
        'meal-essentials': {
            name: 'MEAL Essentials',
            icon: 'chart',
            description: 'Core resources for Monitoring, Evaluation, Accountability & Learning',
            items: [
                { title: 'BetterEvaluation Rainbow Framework', url: 'https://www.betterevaluation.org/frameworks-guides/rainbow-framework', type: 'Framework' },
                { title: 'USAID Evaluation Toolkit', url: 'https://www.usaid.gov/evaluation', type: 'Toolkit' },
                { title: 'World Bank Impact Evaluation Guide', url: 'https://dimewiki.worldbank.org/Impact_Evaluation', type: 'Guide' },
                { title: 'ODI Results-Based Management', url: 'https://odi.org/en/publications/results-based-management-in-development-cooperation/', type: 'Publication' },
                { title: 'ALNAP Evaluation Resources', url: 'https://www.alnap.org/help-library/evaluation', type: 'Library' }
            ]
        },
        'theory-of-change': {
            name: 'Theory of Change',
            icon: 'target',
            description: 'Master the art of designing theories of change',
            items: [
                { title: 'Center for Theory of Change', url: 'https://www.theoryofchange.org/', type: 'Hub' },
                { title: 'UNDP Theory of Change Guide', url: 'https://www.undp.org/publications/undp-guidance-note-theory-change', type: 'Guide' },
                { title: 'Nesta Theory of Change', url: 'https://www.nesta.org.uk/toolkit/theory-change/', type: 'Toolkit' },
                { title: 'Comic Relief TOC Guidance', url: 'https://www.comicrelief.com/our-approach/how-we-measure-our-impact/', type: 'Guide' },
                { title: 'DIY Theory of Change Toolkit', url: 'https://diytoolkit.org/tools/theory-of-change/', type: 'Tool' }
            ]
        },
        'gender-development': {
            name: 'Gender in Development',
            icon: 'balance',
            description: 'Essential readings on gender analysis and mainstreaming',
            items: [
                { title: 'UN Women Training Centre', url: 'https://trainingcentre.unwomen.org/', type: 'Courses' },
                { title: 'BRIDGE Gender & Development', url: 'https://www.bridge.ids.ac.uk/', type: 'Research' },
                { title: 'Gender Analysis Toolkit (USAID)', url: 'https://www.usaid.gov/engendering-industries', type: 'Toolkit' },
                { title: 'CARE Gender Toolkit', url: 'https://www.care.org/our-work/womens-economic-justice/', type: 'Resources' },
                { title: 'World Bank Gender Data Portal', url: 'https://genderdata.worldbank.org/', type: 'Data' }
            ]
        },
        'research-methods': {
            name: 'Research Methods',
            icon: 'flask',
            description: 'Qualitative and quantitative research resources',
            items: [
                { title: 'J-PAL Research Resources', url: 'https://www.povertyactionlab.org/research-resources', type: 'Library' },
                { title: 'SAGE Research Methods', url: 'https://methods.sagepub.com/', type: 'Database' },
                { title: 'Qualitative Research Guidelines (CDC)', url: 'https://www.cdc.gov/healthyyouth/evaluation/pdf/brief19.pdf', type: 'Guide' },
                { title: 'IPA Best Practices', url: 'https://www.poverty-action.org/researchers', type: 'Resources' },
                { title: '3ie Systematic Reviews', url: 'https://www.3ieimpact.org/evidence-hub/systematic-review-repository', type: 'Repository' }
            ]
        },
        'behavioral-economics': {
            name: 'Behavioral Economics',
            icon: 'brain',
            description: 'Apply behavioral insights to development programs',
            items: [
                { title: 'ideas42 Behavioral Design', url: 'https://www.ideas42.org/learn/', type: 'Learning' },
                { title: 'Behavioral Insights Team', url: 'https://www.bi.team/publications/', type: 'Publications' },
                { title: 'World Bank Mind, Behavior, Development', url: 'https://www.worldbank.org/en/programs/embed', type: 'Program' },
                { title: 'Busara Center Resources', url: 'https://busaracenter.org/resources/', type: 'Resources' },
                { title: 'OECD Behavioral Insights', url: 'https://www.oecd.org/gov/regulatory-policy/behavioural-insights.htm', type: 'Policy' }
            ]
        }
    },
    
    getList: function(listId) {
        return this.lists[listId] || null;
    },
    
    getAllLists: function() {
        var self = this;
        return Object.keys(this.lists).map(function(key) {
            return Object.assign({ id: key }, self.lists[key]);
        });
    }
};



// ========================================
// Storage Functions
// ========================================

IMX.getBookmarks = function() {
    try {
        return JSON.parse(localStorage.getItem('impactmojo_bookmarks') || '[]');
    } catch(e) {
        return [];
    }
};

IMX.saveBookmarks = function(bookmarks) {
    localStorage.setItem('impactmojo_bookmarks', JSON.stringify(bookmarks));
    IMX.updateBadges();
};

IMX.getCompareItems = function() {
    try {
        return JSON.parse(localStorage.getItem('impactmojo_compare') || '[]');
    } catch(e) {
        return [];
    }
};

IMX.saveCompareItems = function(items) {
    localStorage.setItem('impactmojo_compare', JSON.stringify(items));
    IMX.updateBadges();
};

// ========================================
// Bookmark Functions
// ========================================

IMX.addBookmark = function(item) {
    var bookmarks = IMX.getBookmarks();
    if (!bookmarks.find(function(b) { return b.id === item.id; })) {
        item.addedAt = new Date().toISOString();
        bookmarks.push(item);
        IMX.saveBookmarks(bookmarks);
        IMX.showToast('Bookmarked: ' + item.name);
    }
    IMX.injectCardButtons();
};

IMX.removeBookmark = function(id) {
    var bookmarks = IMX.getBookmarks().filter(function(b) { return b.id !== id; });
    IMX.saveBookmarks(bookmarks);
    IMX.renderBookmarksList();
    IMX.injectCardButtons();
};

IMX.isBookmarked = function(id) {
    return IMX.getBookmarks().some(function(b) { return b.id === id; });
};

IMX.clearAllBookmarks = function() {
    if (confirm('Clear all bookmarks? This cannot be undone.')) {
        IMX.saveBookmarks([]);
        IMX.renderBookmarksList();
        IMX.injectCardButtons();
        IMX.showToast('All bookmarks cleared');
    }
};

IMX.exportBookmarksCSV = function() {
    var bookmarks = IMX.getBookmarks();
    if (bookmarks.length === 0) {
        IMX.showToast('No bookmarks to export');
        return;
    }
    
    var csv = 'Name,Type,URL,Rating,Learners,Added\n';
    bookmarks.forEach(function(b) {
        csv += '"' + (b.name || '').replace(/"/g, '""') + '",';
        csv += '"' + (b.type || '') + '",';
        csv += '"' + (b.url || '') + '",';
        csv += '"' + (b.rating || '') + '",';
        csv += '"' + (b.learners || '') + '",';
        csv += '"' + (b.addedAt || '') + '"\n';
    });
    
    var blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
    var link = document.createElement('a');
    link.href = URL.createObjectURL(blob);
    link.download = 'impactmojo_bookmarks_' + new Date().toISOString().split('T')[0] + '.csv';
    link.click();
    IMX.showToast('Bookmarks exported!');
};

IMX.renderBookmarksList = function() {
    var container = document.getElementById('imxBookmarksList');
    if (!container) return;
    
    var bookmarks = IMX.getBookmarks();
    
    if (bookmarks.length === 0) {
        container.innerHTML = '<div class="imx-empty">' +
            '<svg viewBox="0 0 24 24"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z" fill="none" stroke="currentColor" stroke-width="1.5"></path></svg>' +
            '<p>No bookmarks yet</p>' +
            '<small>Click "Save" on any course or lab to add it here</small>' +
            '</div>';
        return;
    }
    
    container.innerHTML = bookmarks.map(function(b) {
        return '<div class="imx-bookmark-item">' +
            '<div class="imx-bookmark-info">' +
            '<div class="imx-bookmark-name">' + (b.name || 'Untitled') + '</div>' +
            '<div class="imx-bookmark-meta">' +
            '<span>' + (b.type || 'Item') + '</span>' +
            (b.rating ? '<span><svg class="inline-star" viewBox="0 0 24 24" width="12" height="12" fill="#FCD34D" stroke="#FCD34D"><use href="#imx-star"/></svg> ' + b.rating + '</span>' : '') +
            '</div>' +
            '</div>' +
            '<div class="imx-bookmark-actions">' +
            '<a href="' + (b.url || '#') + '" class="imx-bookmark-btn" title="Open">' +
            '<svg viewBox="0 0 24 24"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6" fill="none" stroke="currentColor" stroke-width="2"></path><polyline points="15 3 21 3 21 9" fill="none" stroke="currentColor" stroke-width="2"></polyline><line x1="10" y1="14" x2="21" y2="3" fill="none" stroke="currentColor" stroke-width="2"></line></svg>' +
            '</a>' +
            '<button class="imx-bookmark-btn delete" onclick="IMX.removeBookmark(\'' + b.id + '\')" title="Remove">' +
            '<svg viewBox="0 0 24 24"><polyline points="3 6 5 6 21 6" fill="none" stroke="currentColor" stroke-width="2"></polyline><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2" fill="none" stroke="currentColor" stroke-width="2"></path></svg>' +
            '</button>' +
            '</div>' +
            '</div>';
    }).join('');
};

// ========================================
// Compare Functions
// ========================================

IMX.addToCompare = function(item) {
    var items = IMX.getCompareItems();
    if (items.length >= 3) {
        IMX.showToast('Maximum 3 items for comparison');
        return;
    }
    if (!items.find(function(i) { return i.id === item.id; })) {
        items.push(item);
        IMX.saveCompareItems(items);
        IMX.showToast('Added to compare: ' + item.name);
    }
    IMX.injectCardButtons();
};

IMX.removeFromCompare = function(id) {
    var items = IMX.getCompareItems().filter(function(i) { return i.id !== id; });
    IMX.saveCompareItems(items);
    IMX.renderCompareGrid();
    IMX.injectCardButtons();
};

IMX.isInCompare = function(id) {
    return IMX.getCompareItems().some(function(i) { return i.id === id; });
};

IMX.clearAllCompare = function() {
    IMX.saveCompareItems([]);
    IMX.renderCompareGrid();
    IMX.injectCardButtons();
    IMX.showToast('Comparison cleared');
};

// Get rich data for an item from course database
IMX.getRichItemData = function(basicItem) {
    var urlKey = basicItem.url ? basicItem.url.split('/').pop().toLowerCase() : '';
    for (var key in IMPACTMOJO_COURSE_DATA) {
        var course = IMPACTMOJO_COURSE_DATA[key];
        if (course.url === basicItem.url || course.name.toLowerCase() === basicItem.name.toLowerCase()) {
            return Object.assign({}, course, { id: basicItem.id });
        }
    }
    return basicItem;
};

IMX.renderCompareGrid = function() {
    var container = document.getElementById('imxCompareGrid');
    if (!container) return;
    
    var items = IMX.getCompareItems();
    
    if (items.length === 0) {
        container.innerHTML = '<div class="imx-empty">' +
            '<svg viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="18" rx="2" ry="2" fill="none" stroke="currentColor" stroke-width="1.5"></rect><line x1="9" y1="9" x2="15" y2="9" fill="none" stroke="currentColor" stroke-width="1.5"></line><line x1="9" y1="15" x2="15" y2="15" fill="none" stroke="currentColor" stroke-width="1.5"></line></svg>' +
            '<p>No items to compare</p>' +
            '<small>Click "Compare" on up to 3 courses, labs, or games</small>' +
            '</div>';
        return;
    }
    
    // Enrich items with full course data
    var richItems = items.map(function(item) { return IMX.getRichItemData(item); });
    
    container.innerHTML = richItems.map(function(item) {
        var objectivesHtml = '';
        if (item.objectives && item.objectives.length > 0) {
            objectivesHtml = '<div class="imx-compare-section">' +
                '<div class="imx-compare-section-title">Learning Objectives</div>' +
                '<ul class="imx-compare-objectives">' +
                item.objectives.map(function(obj) { return '<li>' + obj + '</li>'; }).join('') +
                '</ul></div>';
        }
        
        var typeClass = 'imx-type-' + (item.type || 'course').toLowerCase();
        
        return '<div class="imx-compare-card imx-compare-card-rich">' +
            '<button class="imx-compare-remove" onclick="IMX.removeFromCompare(\'' + item.id + '\')" title="Remove">' +
            '<svg viewBox="0 0 24 24"><line x1="18" y1="6" x2="6" y2="18" fill="none" stroke="currentColor" stroke-width="2"></line><line x1="6" y1="6" x2="18" y2="18" fill="none" stroke="currentColor" stroke-width="2"></line></svg>' +
            '</button>' +
            '<div class="imx-compare-name">' + (item.name || 'Untitled') + '</div>' +
            '<div class="imx-compare-type-badge ' + typeClass + '">' + (item.type || 'Course') + '</div>' +
            '<div class="imx-compare-row"><span class="imx-compare-label">Rating</span><span class="imx-compare-value">' + (item.rating ? '<svg class="inline-star" viewBox="0 0 24 24" width="12" height="12" fill="#FCD34D" stroke="#FCD34D"><use href="#imx-star"/></svg> ' + item.rating : '""') + '</span></div>' +
            '<div class="imx-compare-row"><span class="imx-compare-label">Learners</span><span class="imx-compare-value">' + (item.learners || '""') + '</span></div>' +
            '<div class="imx-compare-row"><span class="imx-compare-label">Audience</span><span class="imx-compare-value">' + (item.audience || '""') + '</span></div>' +
            '<div class="imx-compare-row"><span class="imx-compare-label">Duration</span><span class="imx-compare-value">' + (item.duration || '""') + '</span></div>' +
            '<div class="imx-compare-row"><span class="imx-compare-label">Format</span><span class="imx-compare-value">' + (item.format || '""') + '</span></div>' +
            (item.description ? '<div class="imx-compare-description">' + item.description + '</div>' : '') +
            objectivesHtml +
            '<a href="' + (item.url || '#') + '" target="_blank" rel="noopener" class="imx-compare-link">Open -></a>' +
            '</div>';
    }).join('');
};

// Enhanced CSV export with all rich comparison data
IMX.exportCompareToCSV = function() {
    var items = IMX.getCompareItems().map(function(item) { return IMX.getRichItemData(item); });
    if (items.length === 0) { IMX.showToast('No items to export'); return; }
    
    var headers = ['Name', 'Type', 'Rating', 'Learners', 'Audience', 'Duration', 'Format', 'Description', 'Objectives', 'URL'];
    var rows = items.map(function(item) {
        return [
            '"' + (item.name || '').replace(/"/g, '""') + '"',
            '"' + (item.type || '') + '"',
            '"' + (item.rating || '') + '"',
            '"' + (item.learners || '') + '"',
            '"' + (item.audience || '') + '"',
            '"' + (item.duration || '') + '"',
            '"' + (item.format || '') + '"',
            '"' + (item.description || '').replace(/"/g, '""') + '"',
            '"' + (item.objectives ? item.objectives.join('; ') : '') + '"',
            '"' + (item.url || '') + '"'
        ].join(',');
    });
    
    var csv = headers.join(',') + '\n' + rows.join('\n');
    var blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
    var link = document.createElement('a');
    link.href = URL.createObjectURL(blob);
    link.download = 'impactmojo-comparison-' + new Date().toISOString().slice(0, 10) + '.csv';
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    IMX.showToast('Rich comparison exported to CSV');
};

// ========================================
// Modal Functions
// ========================================

IMX.openBookmarksModal = function() {
    IMX.renderBookmarksList();
    var modal = document.getElementById('imxBookmarksModal');
    if (modal) {
        modal.classList.add('active');
    } else {
        console.error('Bookmarks modal not found');
    }
};

IMX.closeBookmarksModal = function() {
    var modal = document.getElementById('imxBookmarksModal');
    if (modal) modal.classList.remove('active');
};

IMX.openCompareModal = function() {
    IMX.renderCompareGrid();
    var modal = document.getElementById('imxCompareModal');
    if (modal) {
        modal.classList.add('active');
    }
};

IMX.closeCompareModal = function() {
    var modal = document.getElementById('imxCompareModal');
    if (modal) modal.classList.remove('active');
};

IMX.openLofiModal = function() {
    var modal = document.getElementById('imxLofiModal');
    if (modal) {
        modal.classList.add('active');
    }
};

IMX.closeLofiModal = function() {
    var modal = document.getElementById('imxLofiModal');
    if (modal) modal.classList.remove('active');
};

// Analytics Modal Functions
IMX.openAnalyticsModal = function() {
    IMX.renderAnalyticsSummary();
    var modal = document.getElementById('imxAnalyticsModal');
    if (modal) {
        modal.classList.add('active');
    }
};

IMX.closeAnalyticsModal = function() {
    var modal = document.getElementById('imxAnalyticsModal');
    if (modal) modal.classList.remove('active');
};

IMX.renderAnalyticsSummary = function() {
    var container = document.getElementById('imxAnalyticsContent');
    if (!container) return;
    
    var summary = IMX.Analytics.getSummary();
    
    var statsHtml = '<div class="imx-analytics-stats">' +
        '<div class="imx-analytics-stat"><div class="imx-analytics-stat-value">' + summary.totalViews + '</div><div class="imx-analytics-stat-label">Total Views</div></div>' +
        '<div class="imx-analytics-stat"><div class="imx-analytics-stat-value">' + summary.sessions + '</div><div class="imx-analytics-stat-label">Sessions</div></div>' +
        '<div class="imx-analytics-stat"><div class="imx-analytics-stat-value">' + summary.totalTime + '</div><div class="imx-analytics-stat-label">Time Learning</div></div>' +
        '</div>';
    
    var topItemsHtml = '';
    if (summary.topItems.length > 0) {
        topItemsHtml = '<div class="imx-analytics-section"><h4>Most Viewed</h4><ul class="imx-analytics-list">' +
            summary.topItems.map(function(item) {
                return '<li><span class="imx-analytics-item-name">' + item.name + '</span><span class="imx-analytics-item-badge">' + item.views + ' views</span></li>';
            }).join('') + '</ul></div>';
    }
    
    var recentHtml = '';
    if (summary.recentItems.length > 0) {
        recentHtml = '<div class="imx-analytics-section"><h4>Recently Viewed</h4><ul class="imx-analytics-list">' +
            summary.recentItems.map(function(item) {
                var timeAgo = item.time ? new Date(item.time).toLocaleDateString() : '';
                return '<li><span class="imx-analytics-item-name">' + item.name + '</span><span class="imx-analytics-item-time">' + timeAgo + '</span></li>';
            }).join('') + '</ul></div>';
    }
    
    var dateInfo = '<div class="imx-analytics-dates">' +
        '<small>First visit: ' + summary.firstVisit + ' | Last visit: ' + summary.lastVisit + '</small>' +
        '</div>';
    
    container.innerHTML = statsHtml + topItemsHtml + recentHtml + dateInfo;
    
    if (summary.totalViews === 0) {
        container.innerHTML = '<div class="imx-empty">' +
            '<svg viewBox="0 0 24 24"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5" fill="none" stroke="currentColor" stroke-width="1.5"></path></svg>' +
            '<p>No learning activity yet</p>' +
            '<small>Start exploring courses, labs, and games!</small>' +
            '</div>';
    }
};

// Reading Lists Modal Functions
IMX.openReadingListsModal = function() {
    IMX.renderReadingLists();
    var modal = document.getElementById('imxReadingListsModal');
    if (modal) {
        modal.classList.add('active');
    }
};

IMX.closeReadingListsModal = function() {
    var modal = document.getElementById('imxReadingListsModal');
    if (modal) modal.classList.remove('active');
};

IMX.renderReadingLists = function() {
    var container = document.getElementById('imxReadingListsContent');
    if (!container) return;
    
    var lists = IMX.ReadingLists.getAllLists();
    
    container.innerHTML = lists.map(function(list) {
        // Get SVG icon from icons object
        var iconSvg = IMX.ReadingLists.icons[list.icon] || '';
        
        return '<div class="imx-reading-list">' +
            '<div class="imx-reading-list-header" onclick="IMX.toggleReadingList(\'' + list.id + '\')">' +
            '<span class="imx-reading-list-icon">' + iconSvg + '</span>' +
            '<div class="imx-reading-list-info">' +
            '<div class="imx-reading-list-name">' + list.name + '</div>' +
            '<div class="imx-reading-list-desc">' + list.description + '</div>' +
            '</div>' +
            '<span class="imx-reading-list-toggle" id="toggle-' + list.id + '">▼</span>' +
            '</div>' +
            '<div class="imx-reading-list-items" id="items-' + list.id + '" style="display:none;">' +
            list.items.map(function(item) {
                return '<a href="' + item.url + '" target="_blank" rel="noopener" class="imx-reading-item">' +
                    '<span class="imx-reading-item-title">' + item.title + '</span>' +
                    '<span class="imx-reading-item-type">' + item.type + '</span>' +
                    '</a>';
            }).join('') +
            '</div>' +
            '</div>';
    }).join('');
};

IMX.toggleReadingList = function(listId) {
    var items = document.getElementById('items-' + listId);
    var toggle = document.getElementById('toggle-' + listId);
    if (items && toggle) {
        if (items.style.display === 'none') {
            items.style.display = 'block';
            toggle.innerHTML = '▲';
        } else {
            items.style.display = 'none';
            toggle.innerHTML = '▼';
        }
    }
};

// ========================================
// PERSONAL NOTES FEATURE
// ========================================
IMX.Notes = {
    STORAGE_KEY: 'impactmojo_notes',
    editingId: null,
    
    // Get all notes from storage
    getAll: function() {
        try {
            return JSON.parse(localStorage.getItem(this.STORAGE_KEY)) || [];
        } catch(e) {
            return [];
        }
    },
    
    // Save notes to storage
    saveAll: function(notes) {
        localStorage.setItem(this.STORAGE_KEY, JSON.stringify(notes));
        this.updateBadge();
    },
    
    // Generate unique ID
    generateId: function() {
        return 'note_' + Date.now() + '_' + Math.random().toString(36).substr(2, 9);
    },
    
    // Format date nicely
    formatDate: function(timestamp) {
        var date = new Date(timestamp);
        var now = new Date();
        var diff = now - date;
        
        if (diff < 60000) return 'Just now';
        if (diff < 3600000) return Math.floor(diff / 60000) + ' min ago';
        if (diff < 86400000) return Math.floor(diff / 3600000) + ' hours ago';
        if (diff < 604800000) return Math.floor(diff / 86400000) + ' days ago';
        
        return date.toLocaleDateString('en-IN', { day: 'numeric', month: 'short', year: 'numeric' });
    },
    
    // Show editor for new note
    showEditor: function(noteId) {
        var editor = document.getElementById('imxNotesEditor');
        var toolbar = document.getElementById('imxNotesToolbar');
        var titleInput = document.getElementById('imxNoteTitle');
        var contentInput = document.getElementById('imxNoteContent');
        
        if (noteId) {
            // Editing existing note
            var notes = this.getAll();
            var note = notes.find(function(n) { return n.id === noteId; });
            if (note) {
                titleInput.value = note.title;
                contentInput.value = note.content;
                this.editingId = noteId;
            }
        } else {
            // New note
            titleInput.value = '';
            contentInput.value = '';
            this.editingId = null;
        }
        
        toolbar.style.display = 'none';
        editor.classList.add('active');
        titleInput.focus();
    },
    
    // Hide editor
    hideEditor: function() {
        var editor = document.getElementById('imxNotesEditor');
        var toolbar = document.getElementById('imxNotesToolbar');
        
        editor.classList.remove('active');
        toolbar.style.display = 'flex';
        this.editingId = null;
    },
    
    // Save note
    saveNote: function() {
        var titleInput = document.getElementById('imxNoteTitle');
        var contentInput = document.getElementById('imxNoteContent');
        
        var title = titleInput.value.trim();
        var content = contentInput.value.trim();
        
        if (!title && !content) {
            IMX.showToast('Please enter a title or content');
            return;
        }
        
        var notes = this.getAll();
        var now = Date.now();
        
        if (this.editingId) {
            // Update existing note
            var index = notes.findIndex(function(n) { return n.id === IMX.Notes.editingId; });
            if (index !== -1) {
                notes[index].title = title || 'Untitled';
                notes[index].content = content;
                notes[index].updated = now;
            }
            IMX.showToast('Note updated!');
        } else {
            // Create new note
            notes.unshift({
                id: this.generateId(),
                title: title || 'Untitled',
                content: content,
                created: now,
                updated: now
            });
            IMX.showToast('Note saved!');
        }
        
        this.saveAll(notes);
        this.hideEditor();
        this.render();
    },
    
    // Delete note
    deleteNote: function(noteId) {
        if (!confirm('Delete this note?')) return;
        
        var notes = this.getAll();
        notes = notes.filter(function(n) { return n.id !== noteId; });
        this.saveAll(notes);
        this.render();
        IMX.showToast('Note deleted');
    },
    
    // Clear all notes
    clearAll: function() {
        if (!confirm('Delete ALL notes? This cannot be undone.')) return;
        
        localStorage.removeItem(this.STORAGE_KEY);
        this.updateBadge();
        this.render();
        IMX.showToast('All notes cleared');
    },
    
    // Filter notes by search
    filterNotes: function(query) {
        this.render(query.toLowerCase());
    },
    
    // Export notes as text file
    exportNotes: function() {
        var notes = this.getAll();
        if (notes.length === 0) {
            IMX.showToast('No notes to export');
            return;
        }
        
        var text = 'ImpactMojo Personal Notes\n';
        text += 'Exported: ' + new Date().toLocaleString() + '\n';
        text += '='.repeat(40) + '\n\n';
        
        notes.forEach(function(note, i) {
            text += (i + 1) + '. ' + note.title + '\n';
            text += 'Created: ' + new Date(note.created).toLocaleString() + '\n';
            text += '-'.repeat(30) + '\n';
            text += note.content + '\n\n';
        });
        
        var blob = new Blob([text], { type: 'text/plain' });
        var url = URL.createObjectURL(blob);
        var a = document.createElement('a');
        a.href = url;
        a.download = 'impactmojo_notes_' + new Date().toISOString().split('T')[0] + '.txt';
        a.click();
        URL.revokeObjectURL(url);
        
        IMX.showToast('Notes exported!');
    },
    
    // Update badge count
    updateBadge: function() {
        var badge = document.getElementById('imxNotesBadge');
        if (badge) {
            var count = this.getAll().length;
            badge.textContent = count > 0 ? count : '';
        }
    },
    
    // Render notes list
    render: function(filterQuery) {
        var container = document.getElementById('imxNotesList');
        if (!container) return;
        
        var notes = this.getAll();
        
        // Apply filter if provided
        if (filterQuery) {
            notes = notes.filter(function(n) {
                return n.title.toLowerCase().includes(filterQuery) || 
                       n.content.toLowerCase().includes(filterQuery);
            });
        }
        
        if (notes.length === 0) {
            container.innerHTML = 
                '<div class="imx-notes-empty">' +
                '<svg viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline></svg>' +
                '<p>' + (filterQuery ? 'No notes match your search' : 'No notes yet') + '</p>' +
                '<p style="font-size:0.85rem">Click "New Note" to get started!</p>' +
                '</div>';
            return;
        }
        
        var self = this;
        container.innerHTML = notes.map(function(note) {
            var preview = note.content.length > 150 ? note.content.substring(0, 150) + '...' : note.content;
            return '<div class="imx-note-card">' +
                '<div class="imx-note-header">' +
                '<span class="imx-note-title">' + self.escapeHtml(note.title) + '</span>' +
                '<span class="imx-note-date">' + self.formatDate(note.updated) + '</span>' +
                '</div>' +
                '<div class="imx-note-content">' + self.escapeHtml(preview) + '</div>' +
                '<div class="imx-note-actions">' +
                '<button class="imx-note-edit" onclick="IMX.Notes.showEditor(\'' + note.id + '\')">Edit</button>' +
                '<button class="imx-note-delete" onclick="IMX.Notes.deleteNote(\'' + note.id + '\')">Delete</button>' +
                '</div>' +
                '</div>';
        }).join('');
    },
    
    // Escape HTML for safety
    escapeHtml: function(text) {
        var div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }
};

// Notes modal functions
IMX.openNotesModal = function() {
    IMX.Notes.render();
    var modal = document.getElementById('imxNotesModal');
    if (modal) modal.classList.add('active');
};

IMX.closeNotesModal = function() {
    var modal = document.getElementById('imxNotesModal');
    if (modal) modal.classList.remove('active');
    IMX.Notes.hideEditor();
};

// ========================================
// LEARNING STREAK FEATURE
// ========================================
IMX.Streak = {
    STORAGE_KEY: 'impactmojo_streak',
    
    // Milestones with emojis
    milestones: [
        { days: 3, icon: 'sprout', label: '3 Days' },
        { days: 7, icon: 'flame', label: '1 Week' },
        { days: 14, icon: 'star', label: '2 Weeks' },
        { days: 30, icon: 'trophy', label: '1 Month' },
        { days: 60, icon: 'diamond', label: '2 Months' },
        { days: 100, icon: 'trophy', label: '100 Days' }
    ],
    
    // Get streak data from storage
    getData: function() {
        try {
            var data = JSON.parse(localStorage.getItem(this.STORAGE_KEY));
            return data || this.getDefaultData();
        } catch(e) {
            return this.getDefaultData();
        }
    },
    
    // Default data structure
    getDefaultData: function() {
        return {
            currentStreak: 0,
            longestStreak: 0,
            totalDays: 0,
            lastVisit: null,
            visitDates: [],
            celebratedMilestone: 0
        };
    },
    
    // Save streak data
    saveData: function(data) {
        localStorage.setItem(this.STORAGE_KEY, JSON.stringify(data));
        this.updateBadge();
    },
    
    // Get today's date string (YYYY-MM-DD)
    getTodayString: function() {
        return new Date().toISOString().split('T')[0];
    },
    
    // Record today's visit
    recordVisit: function() {
        var data = this.getData();
        var today = this.getTodayString();
        
        // Already recorded today
        if (!data.visitDates) data.visitDates = [];
        if (data.visitDates.includes(today)) {
            return;
        }
        
        // Add today to visit dates
        data.visitDates.push(today);
        
        // Keep only last 365 days of data
        if (data.visitDates.length > 365) {
            data.visitDates = data.visitDates.slice(-365);
        }
        
        // Calculate streak
        var yesterday = new Date();
        yesterday.setDate(yesterday.getDate() - 1);
        var yesterdayStr = yesterday.toISOString().split('T')[0];
        
        if (data.lastVisit === yesterdayStr) {
            // Continuing streak
            data.currentStreak++;
        } else if (data.lastVisit === today) {
            // Same day, no change
        } else {
            // Streak broken, start new
            data.currentStreak = 1;
            data.celebratedMilestone = 0; // allow milestones to celebrate again on the new streak
        }
        
        // Update records
        data.lastVisit = today;
        data.totalDays = data.visitDates.length;
        
        if (data.currentStreak > data.longestStreak) {
            data.longestStreak = data.currentStreak;
        }
        
        this.saveData(data);
        
        // Show celebration for milestone
        this.checkMilestone(data.currentStreak);
    },
    
    // Emoji for each milestone icon keyword (the toast is plain text)
    milestoneEmoji: { sprout: '🌱', flame: '🔥', star: '⭐', trophy: '🏆', diamond: '💎' },

    // Celebrate a milestone at most once per streak (no repeat on revisits or re-syncs)
    checkMilestone: function(streak) {
        var milestone = this.milestones.find(function(m) { return m.days === streak; });
        if (!milestone) return;
        var data = this.getData();
        if ((data.celebratedMilestone || 0) >= milestone.days) return; // already celebrated this milestone
        data.celebratedMilestone = milestone.days;
        this.saveData(data);
        var emoji = this.milestoneEmoji[milestone.icon] || '🎉';
        setTimeout(function() {
            IMX.showToast(emoji + ' ' + milestone.label + ' streak! Keep it up!');
        }, 1000);
    },
    
    // Update badge on speed dial
    updateBadge: function() {
        var badge = document.getElementById('imxStreakBadge');
        if (badge) {
            var data = this.getData();
            badge.textContent = data.currentStreak > 0 ? data.currentStreak : '';
        }
    },
    
    // Render the streak modal content
    render: function() {
        var container = document.getElementById('imxStreakContainer');
        if (!container) return;
        
        var data = this.getData();
        var self = this;
        
        // Build HTML
        var html = '';
        
        // Hero section
        html += '<div class="imx-streak-hero">';
        html += '<div class="imx-streak-fire">' + (data.currentStreak > 0 ? '<svg class="streak-icon" viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2c.5 5-2 8-2 8s3 2 3 6c0 2.5-2 4-4 4s-4-2-4-4c0-2 1-3 2-4-1-2-1-4 0-6 1.5 2 3 2 5-4z"/></svg>' : '<svg class="streak-icon muted" viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>') + '</div>';
        html += '<div class="imx-streak-count">' + data.currentStreak + '</div>';
        html += '<div class="imx-streak-label">Day Streak</div>';
        html += '</div>';
        
        // Stats
        html += '<div class="imx-streak-stats">';
        html += '<div class="imx-streak-stat"><div class="imx-streak-stat-value">' + data.longestStreak + '</div><div class="imx-streak-stat-label">Best Streak</div></div>';
        html += '<div class="imx-streak-stat"><div class="imx-streak-stat-value">' + data.totalDays + '</div><div class="imx-streak-stat-label">Total Days</div></div>';
        html += '<div class="imx-streak-stat"><div class="imx-streak-stat-value">' + this.getThisMonthDays(data) + '</div><div class="imx-streak-stat-label">This Month</div></div>';
        html += '</div>';
        
        // Calendar
        html += this.renderCalendar(data);
        
        // Milestones
        html += '<div class="imx-streak-milestones">';
        html += '<div class="imx-streak-milestones-title">Milestones</div>';
        html += '<div class="imx-streak-badges">';
        this.milestones.forEach(function(m) {
            var earned = data.longestStreak >= m.days;
            html += '<div class="imx-streak-badge' + (earned ? ' earned' : '') + '">';
            html += '<span class="imx-streak-badge-icon">' + m.icon + '</span>';
            html += '<span class="imx-streak-badge-label">' + m.label + '</span>';
            html += '</div>';
        });
        html += '</div></div>';
        
        container.innerHTML = html;
    },
    
    // Get days visited this month
    getThisMonthDays: function(data) {
        var now = new Date();
        var yearMonth = now.getFullYear() + '-' + String(now.getMonth() + 1).padStart(2, '0');
        return data.visitDates.filter(function(d) { return d.startsWith(yearMonth); }).length;
    },
    
    // Render calendar for current month
    renderCalendar: function(data) {
        var now = new Date();
        var year = now.getFullYear();
        var month = now.getMonth();
        
        var monthNames = ['January', 'February', 'March', 'April', 'May', 'June', 
                          'July', 'August', 'September', 'October', 'November', 'December'];
        
        var html = '<div class="imx-streak-calendar">';
        html += '<div class="imx-streak-calendar-header">';
        html += '<span class="imx-streak-calendar-title">' + monthNames[month] + ' ' + year + '</span>';
        html += '</div>';
        
        // Weekday headers
        html += '<div class="imx-streak-weekdays">';
        ['S', 'M', 'T', 'W', 'T', 'F', 'S'].forEach(function(d) {
            html += '<div class="imx-streak-weekday">' + d + '</div>';
        });
        html += '</div>';
        
        // Days grid
        html += '<div class="imx-streak-days">';
        
        var firstDay = new Date(year, month, 1).getDay();
        var daysInMonth = new Date(year, month + 1, 0).getDate();
        var today = now.getDate();
        var todayStr = this.getTodayString();
        
        // Empty cells for days before month starts
        for (var i = 0; i < firstDay; i++) {
            html += '<div class="imx-streak-day"></div>';
        }
        
        // Days of month
        for (var d = 1; d <= daysInMonth; d++) {
            var dateStr = year + '-' + String(month + 1).padStart(2, '0') + '-' + String(d).padStart(2, '0');
            var hasActivity = data.visitDates.includes(dateStr);
            var isToday = dateStr === todayStr;
            
            var classes = 'imx-streak-day current-month';
            if (hasActivity) classes += ' has-activity';
            if (isToday) classes += ' today';
            
            html += '<div class="' + classes + '">' + d + '</div>';
        }
        
        html += '</div></div>';
        
        return html;
    }
};

// Streak modal functions
IMX.openStreakModal = function() {
    IMX.Streak.render();
    var modal = document.getElementById('imxStreakModal');
    if (modal) modal.classList.add('active');
};

IMX.closeStreakModal = function() {
    var modal = document.getElementById('imxStreakModal');
    if (modal) modal.classList.remove('active');
};

// ========================================
// UI Functions
// ========================================

IMX.showToast = function(message) {
    var existing = document.querySelector('.imx-toast');
    if (existing) existing.remove();
    
    var toast = document.createElement('div');
    toast.className = 'imx-toast';
    toast.textContent = message;
    document.body.appendChild(toast);
    
    setTimeout(function() {
        toast.classList.add('fade-out');
        setTimeout(function() { toast.remove(); }, 300);
    }, 2500);
};

IMX.updateBadges = function() {
    var bookmarkBadge = document.getElementById('imxBookmarkBadge');
    var compareBadge = document.getElementById('imxCompareBadge');
    
    if (bookmarkBadge) {
        var bookmarkCount = IMX.getBookmarks().length;
        bookmarkBadge.textContent = bookmarkCount > 0 ? bookmarkCount : '';
    }
    
    if (compareBadge) {
        var compareCount = IMX.getCompareItems().length;
        compareBadge.textContent = compareCount > 0 ? compareCount : '';
    }
    
    // Update Notes and Streak badges
    if (IMX.Notes && IMX.Notes.updateBadge) {
        IMX.Notes.updateBadge();
    }
    if (IMX.Streak && IMX.Streak.updateBadge) {
        IMX.Streak.updateBadge();
    }
};

// ========================================
// Card Button Injection
// ========================================

IMX.injectCardButtons = function() {
    var cards = document.querySelectorAll('.card');
    
    cards.forEach(function(card) {
        // Skip premium/gated cards - they should not have Save/Compare buttons
        if (card.hasAttribute('data-required-tier')) return;

        // Remove existing buttons to refresh state
        var existing = card.querySelector('.imx-card-actions');
        if (existing) existing.remove();
        
        // Extract card data
        var link = card.querySelector('a[href]');
        var titleEl = card.querySelector('h3, .card-title');
        var ratingEl = card.querySelector('.rating-text');
        var learnersEl = card.querySelector('.learner-badge');
        var numberEl = card.querySelector('.card-number');
        
        var url = link ? link.href : '#';
        var name = titleEl ? titleEl.textContent.trim() : 'Untitled';
        var rating = ratingEl ? ratingEl.textContent.trim() : '';
        var learners = learnersEl ? learnersEl.textContent.trim() : '';
        
        // Determine type
        var type = 'Item';
        if (numberEl) {
            var num = numberEl.textContent.trim();
            if (num.startsWith('C')) type = 'Course';
            else if (num.startsWith('L')) type = 'Lab';
            else if (num.startsWith('G')) type = 'Game';
            else if (num.startsWith('P')) type = 'Premium';
        }
        
        // Create unique ID
        var id = 'imx_' + name.toLowerCase().replace(/[^a-z0-9]/g, '_').substring(0, 30);
        
        var item = {
            id: id,
            name: name,
            url: url,
            type: type,
            rating: rating,
            learners: learners
        };
        
        var itemJson = JSON.stringify(item).replace(/'/g, "\\'");
        
        // Create action buttons
        var actions = document.createElement('div');
        actions.className = 'imx-card-actions';
        
        var isBookmarked = IMX.isBookmarked(id);
        var isCompared = IMX.isInCompare(id);
        
        var saveBtn = document.createElement('button');
        saveBtn.className = 'imx-card-btn' + (isBookmarked ? ' active' : '');
        saveBtn.innerHTML = '<svg viewBox="0 0 24 24"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z" fill="none" stroke="currentColor" stroke-width="2"></path></svg>' + (isBookmarked ? 'Saved' : 'Save');
        saveBtn.onclick = function(e) {
            e.preventDefault();
            e.stopPropagation();
            if (IMX.isBookmarked(id)) {
                IMX.removeBookmark(id);
            } else {
                IMX.addBookmark(item);
            }
        };
        
        var compareBtn = document.createElement('button');
        compareBtn.className = 'imx-card-btn' + (isCompared ? ' active' : '');
        compareBtn.innerHTML = '<svg viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="18" rx="2" ry="2" fill="none" stroke="currentColor" stroke-width="2"></rect><line x1="9" y1="9" x2="15" y2="9" fill="none" stroke="currentColor" stroke-width="2"></line><line x1="9" y1="15" x2="15" y2="15" fill="none" stroke="currentColor" stroke-width="2"></line></svg>' + (isCompared ? 'Added' : 'Compare');
        compareBtn.onclick = function(e) {
            e.preventDefault();
            e.stopPropagation();
            if (IMX.isInCompare(id)) {
                IMX.removeFromCompare(id);
            } else {
                IMX.addToCompare(item);
            }
        };
        
        actions.appendChild(saveBtn);
        actions.appendChild(compareBtn);
        
        // Track clicks for analytics
        if (link) {
            link.addEventListener('click', function() {
                IMX.Analytics.trackView(id, name, type);
            });
        }
        
        // Insert after card content
        var cardBody = card.querySelector('.card-body, .card-content');
        if (cardBody) {
            cardBody.appendChild(actions);
        } else {
            card.appendChild(actions);
        }
    });
};

// ========================================
// Initialize on DOM Ready
// ========================================

document.addEventListener('DOMContentLoaded', function() {
    IMX.updateBadges();
    
    // Delay card injection slightly to ensure all cards are loaded
    setTimeout(function() {
        IMX.injectCardButtons();
    }, 500);
    
    // Close modals on backdrop click
    document.querySelectorAll('.imx-modal').forEach(function(modal) {
        modal.addEventListener('click', function(e) {
            if (e.target === modal) {
                modal.classList.remove('active');
            }
        });
    });
    
    // Close modals on Escape key
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') {
            document.querySelectorAll('.imx-modal.active').forEach(function(modal) {
                modal.classList.remove('active');
            });
            // Close Intro.js tour if active
            if (typeof introJs !== 'undefined') {
                try { introJs.tour().exit(true); } catch(e) {}
            }
        }
    });
});

// Also run injection after a longer delay for dynamically loaded content
window.addEventListener('load', function() {
    setTimeout(function() {
        IMX.injectCardButtons();
        
        // Record streak visit and update all badges
        if (IMX.Streak && IMX.Streak.recordVisit) {
            IMX.Streak.recordVisit();
        }
        IMX.updateBadges();
    }, 1000);
});

// ========================================
// SPOTLIGHT TOUR — now handled by Intro.js (js/tours.js)
// Legacy IMX.Tour stub kept for backwards compatibility
// ========================================
IMX.Tour = {
    isActive: false,
    restart: function() {
        if (window.ImpactMojoTour) {
            window.ImpactMojoTour.reset('index');
            window.ImpactMojoTour.start('index');
        }
    },
    start: function() { this.restart(); },
    showWelcome: function() { this.restart(); },
    end: function() {},
    skip: function() {},
    forceShow: function() { this.restart(); }
};

