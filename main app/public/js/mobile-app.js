/**
 * Obsidian Vocab — Mobile Native Application Engine
 * Optimized for Pure Vocabulary Mastery (Greek Roots, Latin Roots, English Vocabulary Master).
 * Features:
 * - 4-Tab Bottom Bar: Home Hub, Word Cards (TikTok-Style Vertical Feed), Daily Random Word, Settings HUD
 * - Full-Stack Subpage Navigation with Horizontal Swipe & Breadcrumbs on Home Tab
 * - DataviewJS Execution for Live Morphological Dashboards & Word Tables
 * - TikTok-Style Vertical Snap/Swipe Feed for 49,000+ Individual Vocabulary Words
 * - SpeechSynthesis Audio Pronunciation Engine
 * - 3-State Reactive Tracking System (🔴 Unread, 🟡 Studying, 🟢 Learned)
 * - Offline-First Native Architecture (Capacitor & Android APK Ready)
 */

import { renderObsidianMarkdown, extractFrontmatterAndBody, createAppleStatusToggle } from './markdown-engine.js';
import { VaultRuntime } from './dataview-engine.js';
import { MobileUpdateManager } from './mobile-updater.js';
import { initFirebase } from './core/firebase.js';
import { authService } from './services/auth-service.js';
import { trackingService } from './services/tracking-service.js';
import { avatarService } from './services/avatar-service.js';
import { topBar } from './components/top-bar.js';
import { profileHUD } from './components/profile-hud.js';
import { authModal } from './components/auth-modal.js';
import { eventBus } from './core/event-bus.js';

class MobileVocabApp {
  constructor() {
    this.activeTab = 'home'; // 'home' | 'cards' | 'daily' | 'settings'

    // Data Stores (Strictly Pure Vocabulary: Greek Roots, Latin Roots, Vocab Master)
    this.vaultIndex = { pages: [], totalNotes: 0 };
    this.coreNotes = {};
    this.statusDb = {};
    this.allWordCards = [];
    this.filteredCards = [];

    // Home Navigation Stack (Subpages, Dashboards, Clusters, Reference)
    this.homeStack = []; // Stack of { path, title, isHomeRoot }
    this.currentHomeNote = null;

    // Root & Cluster Dashboards Store (Loaded from data/root-dashboards.json)
    this.rootDashboardsDb = {};
    this.dashboardsFilterCategory = 'all';
    this.dashboardsSearchQuery = '';

    // Word Cards State (TikTok-Style Vertical Swipable Feed)
    this.feedWordIndex = 0;
    this.returnToFeedIndex = 0;
    this.activeScope = null; // Linked Root Dashboard or Vocab Master Cluster { type, title, path, words: [] }
    this.cardsFilterCategory = 'all'; // 'all' | 'greek' | 'latin' | 'vocab'
    this.cardsFilterStatus = 'all';   // 'all' | 'unread' | 'learning' | 'learned'
    this.cardsSearchQuery = '';
    this.cardsViewMode = 'feed';      // 'feed' | 'list'
    this.pendingCardPath = null;

    // List View Pagination & Virtual Chunking (Batches of 50 items)
    this.cardListRenderedCount = 0;
    this.cardListObserver = null;

    // Daily Word State (Random word drawn from pure vocabulary pool)
    this.dailyCurrentCard = null;
    this.dailyRevealed = false;
    this.dailyReviewedCount = 0;

    // Settings & Appearance
    this.theme = localStorage.getItem('vocab_theme') || 'dark';
    this.typography = JSON.parse(localStorage.getItem('vocab_typography') || '{"font":"sans","size":16,"lineHeight":1.6}');

    // Touch gesture tracking & physics
    this.touchStartX = 0;
    this.touchStartY = 0;
    this.touchStartTime = 0;
    this.touchLastY = 0;
    this.touchLastTime = 0;
    this.touchMoved = false;
    this._renderFeedSeq = 0;
    this.isSlideTransitioning = false;

    // Dataview + Markdown Runtime
    this.runtime = new VaultRuntime(this);

    // Audio Speech Pronunciation Engine State
    this.speechVoices = [];
    this.activeSpeechButton = null;
    this.currentUtterance = null;
    this.isSpeaking = false;

    // In-App APK Updater
    this.updateManager = new MobileUpdateManager(this);
  }

  async init() {
    this.applyTheme(this.theme);
    this.applyTypography();

    // 0. Initialize Firebase, Multi-Provider Auth, and UI HUDs
    try {
      await initFirebase();
      await authService.init();
      topBar.mount();
      profileHUD.mount();

      eventBus.on('tracking:synced', ({ statusDb }) => {
        if (statusDb) {
          this.statusDb = { ...this.statusDb, ...statusDb };
          this.prepareWordCards();
          this.updateTrackingHUD();
          if (this.cardsViewMode === 'feed') this.renderFeedCard('none');
          else this.renderCardList();
        }
      });
    } catch (authErr) {
      console.warn('Firebase / Auth setup note:', authErr);
    }

    this.loadStatusDb();
    this.loadDailyStats();

    this.bindDOMEvents();
    this.bindTouchGestures();
    this.bindHardwareBack();
    this.initSpeechEngine();

    // Render Home Root
    this.renderHomeRoot();

    // Load Vault Data (Preloaded bundle + static index)
    await this.loadVaultData();

    // Hydrate Dataview Runtime with vault index pages
    if (this.vaultIndex.pages && this.vaultIndex.pages.length > 0) {
      this.runtime.hydrateIndex(this.vaultIndex.pages, this.statusDb);
    }

    // Initialize Card Views & Telemetry
    this.prepareWordCards();
    this.renderFeedCard('none');
    if (window.innerWidth >= 900) {
      this.renderCardList();
      this.syncCardListHighlight();
    }
    this.renderDailyCard(true);
    this.updateTrackingHUD();

    // Initialize In-App APK Update Manager
    if (this.updateManager) {
      await this.updateManager.init();
    }

    // Register Service Worker for PWA Offline Support
    this.registerServiceWorker();

    // Check PWA URL parameters (e.g. ?tab=cards from manifest shortcuts)
    const urlParams = new URLSearchParams(window.location.search);
    const initialTab = urlParams.get('tab');
    if (initialTab && ['home', 'cards', 'daily', 'settings'].includes(initialTab)) {
      this.switchTab(initialTab);
    }
  }

  registerServiceWorker() {
    if ('serviceWorker' in navigator) {
      window.addEventListener('load', () => {
        navigator.serviceWorker.register('/sw.js')
          .then(reg => {
            console.log('[SW] Service worker registered with scope:', reg.scope);
          })
          .catch(err => {
            console.warn('[SW] Service worker registration failed:', err);
          });
      });
    }
  }

  getCoreNote(notePath) {
    if (!notePath || !this.coreNotes) return '';
    if (this.coreNotes[notePath]) return this.coreNotes[notePath];
    const baseName = notePath.slice(notePath.lastIndexOf('/') + 1);
    if (this.coreNotes[baseName]) return this.coreNotes[baseName];
    const clean = notePath.replace(/\\/g, '/').replace(/^\.?\//, '');
    if (this.coreNotes[clean]) return this.coreNotes[clean];
    const matchKey = Object.keys(this.coreNotes).find(k => k.endsWith('/' + baseName));
    if (matchKey && this.coreNotes[matchKey]) return this.coreNotes[matchKey];
    return '';
  }

  async fetchNoteWithFallback(notePath) {
    // 1. Check pre-bundled in-memory core notes first
    let rawContent = this.getCoreNote(notePath);
    if (rawContent) return rawContent;

    // 2. Fetch from /api/note (routed through Service Worker RUNTIME_CACHE)
    try {
      const res = await fetch(`/api/note?path=${encodeURIComponent(notePath)}`);
      if (res.ok) {
        const data = await res.json();
        rawContent = data.content || '';
        if (rawContent) {
          this.coreNotes[notePath] = rawContent;
          return rawContent;
        }
      }
    } catch (e) {
      console.warn('Network fetch failed for note, checking pre-bundled core notes:', e);
    }

    // 3. Final fallback to core notes (e.g. if loaded after initial failure)
    return this.getCoreNote(notePath) || '';
  }

  bindHardwareBack() {
    const registerBackButton = () => {
      try {
        if (window.Capacitor && window.Capacitor.Plugins && window.Capacitor.Plugins.App && !this._backButtonBound) {
          this._backButtonBound = true;
          window.Capacitor.Plugins.App.addListener('backButton', () => {
            this.handleHardwareBack();
          });
        }
      } catch (e) {
        console.warn('Capacitor App listener unavailable', e);
      }
    };

    registerBackButton();
    setTimeout(registerBackButton, 500);

    window.addEventListener('popstate', (e) => {
      if (this.activeTab === 'home' && this.homeStack.length > 0) {
        this.goBackHome(false);
      }
    });
  }

  handleHardwareBack() {
    // 1. Close any open modal dialogs first
    if (this.updateManager && typeof this.updateManager.hideUpdateModal === 'function') {
      const updateModal = document.getElementById('update-modal');
      if (updateModal && updateModal.style.display !== 'none' && window.getComputedStyle(updateModal).display !== 'none') {
        this.updateManager.hideUpdateModal();
        return;
      }
    }
    const openModal = Array.from(document.querySelectorAll('.modal-backdrop, .modal, [role="dialog"], .prompt-modal, #update-modal')).find(el => {
      return el.style.display !== 'none' && window.getComputedStyle(el).display !== 'none';
    });
    if (openModal) {
      openModal.style.display = 'none';
      return;
    }

    // 2. Home Tab: Pop Home navigation stack first before exiting
    if (this.activeTab === 'home') {
      if (this.homeStack.length > 0) {
        this.goBackHome(true);
        return;
      }
      // Only exit app when at Home root
      try {
        window.Capacitor?.Plugins?.App?.exitApp();
      } catch (e) {
        console.warn('exitApp failed', e);
      }
      return;
    }

    // 3. Word Cards Tab: close search, revert List to Feed, or return to Home
    if (this.activeTab === 'cards') {
      const searchInput = document.getElementById('cards-search-input');
      const clearBtn = document.getElementById('cards-search-clear');

      // Closes active search if query entered or focused
      if (this.cardsSearchQuery || (searchInput && searchInput.value)) {
        this.cardsSearchQuery = '';
        if (searchInput) {
          searchInput.value = '';
          searchInput.blur();
        }
        if (clearBtn) clearBtn.style.display = 'none';
        this.feedWordIndex = 0;
        this.applyCardsFilter();
        if (this.cardsViewMode === 'feed') this.renderFeedCard('none');
        else this.renderCardList();
        return;
      }

      if (searchInput && document.activeElement === searchInput) {
        searchInput.blur();
        return;
      }

      // Revert List mode to Feed mode
      if (this.cardsViewMode === 'list') {
        this.cardsViewMode = 'feed';
        this.updateCardsViewMode();
        return;
      }

      // Revert to Home tab
      this.switchTab('home');
      return;
    }

    // 4. Daily Word and Settings tabs: Revert to Home tab
    if (this.activeTab === 'daily' || this.activeTab === 'settings') {
      this.switchTab('home');
      return;
    }

    // Fallback: exit app only when at root
    try {
      window.Capacitor?.Plugins?.App?.exitApp();
    } catch {}
  }

  /* ========================================================================
     DATA LOADING & STATUS TRACKING
     ======================================================================== */

  loadStatusDb() {
    try {
      const saved = localStorage.getItem('vocab_status_db');
      if (saved) {
        this.statusDb = JSON.parse(saved);
      }
    } catch (e) {
      this.statusDb = {};
    }
  }

  saveStatusDb() {
    try {
      localStorage.setItem('vocab_status_db', JSON.stringify(this.statusDb));
    } catch (e) {
      console.warn('LocalStorage save failed', e);
    }
  }

  loadDailyStats() {
    const today = new Date().toISOString().slice(0, 10);
    const savedDate = localStorage.getItem('vocab_daily_date');
    if (savedDate === today) {
      this.dailyReviewedCount = Number(localStorage.getItem('vocab_daily_count') || 0);
    } else {
      this.dailyReviewedCount = 0;
      localStorage.setItem('vocab_daily_date', today);
      localStorage.setItem('vocab_daily_count', '0');
    }
    this.updateDailyHeader();
  }

  incrementDailyCount() {
    this.dailyReviewedCount++;
    const today = new Date().toISOString().slice(0, 10);
    localStorage.setItem('vocab_daily_date', today);
    localStorage.setItem('vocab_daily_count', String(this.dailyReviewedCount));
    this.updateDailyHeader();
  }

  updateDailyHeader() {
    const badge = document.getElementById('daily-reviewed-badge');
    if (badge) {
      badge.textContent = `${this.dailyReviewedCount} words reviewed today`;
    }
  }

  async loadVaultData() {
    try {
      // 1. Fetch pre-bundled core notes
      const coreRes = await fetch('data/core-notes.json');
      if (coreRes.ok) {
        this.coreNotes = await coreRes.json();
      }
    } catch (e) {
      console.warn('Could not load core-notes.json', e);
    }

    try {
      // 2. Fetch status-db.json defaults if local is empty
      if (Object.keys(this.statusDb).length === 0) {
        const stRes = await fetch('data/status-db.json');
        if (stRes.ok) {
          const defaults = await stRes.json();
          this.statusDb = { ...defaults };
          this.saveStatusDb();
        }
      }
    } catch (e) {
      console.warn('Could not load status-db.json', e);
    }

    try {
      // 3. Fetch full pure vocabulary index
      let idxData = null;
      try {
        const apiRes = await fetch('/api/vault-index');
        if (apiRes.ok) idxData = await apiRes.json();
      } catch {}

      if (!idxData) {
        const staticRes = await fetch('data/vault-index.json');
        if (staticRes.ok) idxData = await staticRes.json();
      }

      if (idxData) {
        // Enforce pure vocabulary filter (Greek roots, Latin roots, English vocabulary master)
        const purePages = (idxData.pages || []).filter(p =>
          p.p.startsWith('Greek roots/') ||
          p.p.startsWith('Latin roots/') ||
          p.p.startsWith('English vocabulary master/') ||
          p.p === '00 Language Hub.md'
        );
        this.vaultIndex = { ...idxData, pages: purePages, totalNotes: purePages.length };
        this.runtime.hydrateIndex(purePages, this.statusDb);
      }
    } catch (e) {
      console.warn('Could not load vault-index.json', e);
    }

    try {
      // 4. Fetch pre-bundled root & cluster dashboards directory
      const dashRes = await fetch('data/root-dashboards.json');
      if (dashRes.ok) {
        this.rootDashboardsDb = await dashRes.json();
      }
    } catch (e) {
      console.warn('Could not load root-dashboards.json', e);
    }
  }

  /* ========================================================================
     NOTE CLASSIFICATION (STUDY PAGES vs INDIVIDUAL WORD NOTES)
     ======================================================================== */

  /**
   * Study pages belong on the Home Tab Stack (Dashboards, Clusters, MOCs, Prefixes, Suffixes, Rules).
   */
  isStudyPage(notePath) {
    if (!notePath || !notePath.endsWith('.md')) return false;
    if (notePath.includes('_assets') || notePath.includes('Templates')) return false;
    if (notePath === '00 Language Hub.md') return true;

    const baseName = notePath.slice(notePath.lastIndexOf('/') + 1).replace(/\.md$/i, '');
    const lowerBase = baseName.toLowerCase();

    // Dashboards, Master tables, MOCs, Triage, Rules, References
    if (baseName.startsWith('Dashboard —') || baseName.startsWith('Master Table') || baseName.startsWith('Word Triage')) return true;
    if (baseName.endsWith('Progress') || baseName.endsWith('MOC') || baseName.endsWith('Dashboards')) return true;
    if (baseName.startsWith('Semantic Field —') || baseName.startsWith('Concept —') || baseName.startsWith('Overview —') || baseName.startsWith('Table —')) return true;
    if (baseName.startsWith('00_') || baseName.startsWith('01_') || baseName.startsWith('02_') || baseName.startsWith('03_')) return true;
    if (notePath.includes('03_Reference_and_Rules') || notePath.includes('01_Root_Dashboards')) return true;

    // Prefixes, Suffixes, Rules, Atlas, Methods
    if (lowerBase.startsWith('prefix') || lowerBase.startsWith('suffix')) return true;
    if (baseName.includes('Rules') || baseName.includes('Atlas') || baseName.includes('Method') || baseName.includes('Formula')) return true;

    // Folder root notes where folder name equals note name (e.g. "Greek roots/Greek roots.md" or "Cluster .../Cluster ....md")
    const dirParts = notePath.split('/');
    if (dirParts.length >= 2 && dirParts[dirParts.length - 2] === baseName) return true;
    if (baseName.startsWith('Cluster ') && baseName === dirParts[dirParts.length - 1].replace(/\.md$/i, '')) return true;

    return false;
  }

  /**
   * Individual vocabulary word notes belong in Tab 2 (Word Cards TikTok feed) and Tab 3 (Daily Word).
   */
  isWordCard(notePath) {
    if (!notePath || !notePath.endsWith('.md')) return false;
    // Pure vocabulary vault folders only:
    if (!notePath.startsWith('Greek roots/') && !notePath.startsWith('Latin roots/') && !notePath.startsWith('English vocabulary master/')) {
      return false;
    }
    return !this.isStudyPage(notePath);
  }

  getCategoryFromPath(path) {
    if (path.startsWith('Greek roots')) return 'greek';
    if (path.startsWith('Latin roots')) {
      // Check for misplaced Greek roots in Latin folders
      if (path.includes('Cluster Greek-Latin Hybrid')) return 'greek';
      const GREEK_IN_LATIN = [
        'psych', 'phil', 'phon', 'path', 'arch', 'zo', 'crani', 'chir',
        'xyl', 'arct', 'crypt', 'tele', 'bio', 'chron', 'cosm', 'cycl',
        'dem', 'hier', 'hydr', 'morph', 'nom_law', 'scop', 'theo', 'therm',
        'top', 'petr', 'phor', 'trop', 'taur', 'brachi', 'phys', 'soph'
      ];
      for (const r of GREEK_IN_LATIN) {
        if (path.includes(`Dashboard — ${r}`) || path.includes(`Dashboard - ${r}`)) {
          return 'greek';
        }
      }
      return 'latin';
    }
    if (path.startsWith('English vocabulary master')) return 'vocab';
    return 'other';
  }

  getCardCategoryBadge(card) {
    if (!card) return '👑 VOCAB MASTER';
    const isRootDash = card.rawPage?.t === 'root_dashboard' || /^Dashboard\s*[—–-]/i.test(card.name);
    if (card.category === 'greek') {
      return isRootDash ? '🏛️ GREEK ROOT' : '🏛️ GREEK DERIVATIVE';
    }
    if (card.category === 'latin') {
      return isRootDash ? '📜 LATIN ROOT' : '📜 LATIN DERIVATIVE';
    }
    return '👑 VOCAB MASTER';
  }

  getCardCategoryLabel(card) {
    if (!card) return 'Vocab Master';
    const isRootDash = card.rawPage?.t === 'root_dashboard' || /^Dashboard\s*[—–-]/i.test(card.name);
    if (card.category === 'greek') {
      return isRootDash ? 'Greek Root' : 'Greek Derivative';
    }
    if (card.category === 'latin') {
      return isRootDash ? 'Latin Root' : 'Latin Derivative';
    }
    return 'Vocab Master';
  }

  getClusterFromPath(path) {
    const parts = path.split('/');
    for (const part of parts) {
      if (/^Cluster\s+/i.test(part) || /^Dashboard\s*[—–-]\s*/i.test(part)) {
        return part.replace(/^Cluster\s+/i, '').replace(/^Dashboard\s*[—–-]\s*/i, '');
      }
    }
    return parts[1] || '';
  }

  findRootDashboardForWord(wordPath) {
    if (!wordPath) return null;
    const parts = wordPath.split('/');
    const dashPart = parts.find(p => /^Dashboard\s*[—–-]/i.test(p));
    let cleanRoot = '';
    if (dashPart) {
      cleanRoot = dashPart.replace(/^Dashboard\s*[—–-]\s*/i, '').trim().toLowerCase();
    } else {
      const clusterPart = parts.find(p => p.startsWith('Cluster '));
      if (clusterPart) {
        cleanRoot = clusterPart.replace(/^Cluster\s+/i, '').trim().toLowerCase();
      }
    }

    if (cleanRoot && this.rootDashboardsDb && this.rootDashboardsDb[cleanRoot]) {
      return this.rootDashboardsDb[cleanRoot];
    }

    // Secondary scan across rootDashboardsDb
    if (this.rootDashboardsDb) {
      for (const k in this.rootDashboardsDb) {
        const rd = this.rootDashboardsDb[k];
        if (rd.path && wordPath.startsWith(rd.path.slice(0, rd.path.lastIndexOf('/') + 1))) {
          return rd;
        }
      }
    }

    // Fallback lookup in vaultIndex
    if (cleanRoot) {
      const match = (this.vaultIndex.pages || []).find(p => {
        if (p.t === 'root_dashboard' || /^Dashboard\s*[—–-]/i.test(p.p.split('/').pop())) {
          const pFn = p.p.split('/').pop().replace(/\.md$/i, '');
          const pRoot = pFn.replace(/^Dashboard\s*[—–-]\s*/i, '').replace(/^Cluster\s+/i, '').trim().toLowerCase();
          return pRoot === cleanRoot;
        }
        return false;
      });
      if (match) {
        return {
          root: cleanRoot,
          path: match.p,
          title: match.p.split('/').pop().replace(/\.md$/i, ''),
          category: match.p.startsWith('Greek') ? 'greek' : match.p.startsWith('Latin') ? 'latin' : 'vocab',
          cluster: match.c ? match.c.replace(/^\[\[|\]\]$/g, '') : '',
          meaning: '',
          script: '',
          anchor: '',
          wordCount: 1
        };
      }
    }
    return null;
  }

  /**
   * Find all verified exhaustive derivative words for a specific Root Dashboard, Vocab Master Cluster, or Discipline Section.
   */
  getWordsForScope(scopePath) {
    if (!scopePath || !this.allWordCards || this.allWordCards.length === 0) return [];
    const parts = scopePath.split('/');
    const fileName = parts[parts.length - 1];
    const isDash = /^Dashboard\s*[—–-]/i.test(fileName) || parts.some(p => /^Dashboard\s*[—–-]/i.test(p));
    const isCluster = fileName.startsWith('Cluster ') || parts.some(p => p.startsWith('Cluster '));
    const isVocabSection = scopePath.startsWith('English vocabulary master') && (
      fileName === 'English vocabulary master.md' ||
      fileName === '000_Vocabulary_Master_MOC.md' ||
      fileName === 'Vocabulary Learning Progress.md' ||
      parts.length <= 2
    );
    const isGreekSection = scopePath.startsWith('Greek roots') && (
      fileName === 'Greek roots.md' ||
      /^Dashboard\s*[—–-]\s*Greek Roots\.md$/i.test(fileName) ||
      /^Master Table\s*[—–-]\s*Greek Roots\.md$/i.test(fileName) ||
      parts.length <= 2
    );
    const isLatinSection = scopePath.startsWith('Latin roots') && (
      fileName === 'Latin roots.md' ||
      /^Dashboard\s*[—–-]\s*Latin Roots\.md$/i.test(fileName) ||
      /^Master Table\s*[—–-]\s*Latin Roots\.md$/i.test(fileName) ||
      parts.length <= 2
    );

    // 1. Full Discipline Section Scope (Tab 1 Master Section opened)
    if (isVocabSection) {
      return this.allWordCards.filter(c => c.category === 'vocab');
    }
    if (isGreekSection) {
      return this.allWordCards.filter(c => c.category === 'greek');
    }
    if (isLatinSection) {
      return this.allWordCards.filter(c => c.category === 'latin');
    }

    // 2. Classical Root Dashboard (Latin / Greek individual root)
    if (isDash && !fileName.toLowerCase().includes('roots')) {
      const dashMatch = fileName.match(/^Dashboard\s*[—–-]\s*(.+?)(?:\.md)?$/i) ||
                        (parts.find(p => /^Dashboard\s*[—–-]/i.test(p)) || '').match(/^Dashboard\s*[—–-]\s*(.+?)$/i);
      const rootName = dashMatch ? dashMatch[1].trim() : '';
      const rootFolder = scopePath.endsWith('.md') ? parts.slice(0, -1).join('/') : scopePath;

      const ROOT_ALIASES = {
        'aev': ['ev'],
        'ev': ['aev']
      };
      const aliases = ROOT_ALIASES[rootName.toLowerCase()] || [];

      return this.allWordCards.filter(c => {
        if (c.path === scopePath || (c.path.endsWith('.md') && /^Dashboard\s*[—–-]/i.test(c.path.split('/').pop()))) return false;
        // Direct folder matching: Latin roots/.../Dashboard — root/<word>.md
        if (rootFolder && c.path.startsWith(rootFolder + '/')) {
          const fn = c.path.split('/').pop();
          if (!/^Dashboard\s*[—–-]/i.test(fn) && !fn.startsWith('Cluster') && !fn.startsWith('Word Triage')) return true;
        }
        for (const a of aliases) {
          if (c.path.includes('/Dashboard — ' + a + '/') || c.path.includes('/Dashboard - ' + a + '/')) return true;
        }
        // Frontmatter metadata link matching
        const p = c.rawPage;
        if (p) {
          const cleanLr = p.lr ? p.lr.replace(/[\u2013\u2014]/g, '-').replace(/^\[\[/, '').replace(/\]\]$/, '').trim() : '';
          const cleanGr = p.gr ? p.gr.replace(/[\u2013\u2014]/g, '-').replace(/^\[\[/, '').replace(/\]\]$/, '').trim() : '';
          const checkTarget = (val, target) => {
            const v = val.toLowerCase();
            const t = target.toLowerCase();
            return v === t || v === 'dashboard - ' + t || v === 'dashboard — ' + t;
          };
          if (cleanLr && checkTarget(cleanLr, rootName)) return true;
          if (cleanGr && checkTarget(cleanGr, rootName)) return true;
          for (const a of aliases) {
            if (cleanLr && checkTarget(cleanLr, a)) return true;
            if (cleanGr && checkTarget(cleanGr, a)) return true;
          }
        }
        return false;
      });
    }

    // 3. Cluster Scope (either Cluster Dashboard or Semantic Field inside a cluster)
    if (isCluster) {
      const clusterFolderIndex = parts.findIndex(p => p.startsWith('Cluster '));
      const clusterFolderPart = clusterFolderIndex !== -1 ? parts[clusterFolderIndex] : '';
      const clusterName = clusterFolderPart ? clusterFolderPart.trim() : fileName.replace(/\.md$/, '').trim();
      const clusterFolder = clusterFolderIndex !== -1 ? parts.slice(0, clusterFolderIndex + 1).join('/') : parts.slice(0, -1).join('/');

      return this.allWordCards.filter(c => {
        if (c.path === scopePath) return false;
        if (clusterFolder && c.path.startsWith(clusterFolder + '/')) {
          const fn = c.path.split('/').pop();
          if (!fn.startsWith('Cluster') && !fn.startsWith('Semantic Field') && !fn.startsWith('Dashboard')) return true;
        }
        if (c.cluster === clusterName || (c.rawPage && c.rawPage.c && (c.rawPage.c === clusterName || c.rawPage.c === `[[${clusterName}]]`))) return true;
        return false;
      });
    }

    return [];
  }

  /**
   * Dynamically link Tab 2 (TikTok Word Feed) to the active Root Dashboard or Cluster from Tab 1.
   */
  openScopeInFeed(scope) {
    if (!scope || !scope.words || scope.words.length === 0) return;
    this.activeScope = { ...scope, isLocked: true };
    this.cardsFilterCategory = 'all';
    this.cardsFilterStatus = 'all';
    this.cardsSearchQuery = '';
    this.feedWordIndex = 0;

    const banner = document.getElementById('cards-scope-banner');
    const scopeText = document.getElementById('scope-banner-text');
    if (banner) {
      banner.style.display = 'flex';
      if (scopeText) {
        scopeText.innerHTML = `🔒 <strong>Locked:</strong> ${escapeHtml(scope.title)} <span style="opacity:0.85;">(${scope.words.length} derived words)</span>`;
      }
    }

    this.switchTab('cards');
    this.cardsViewMode = 'feed';
    this.updateCardsViewMode();
    this.applyCardsFilter();
    this.renderFeedCard('none');
    this.showToast(`🔒 Locked to: ${scope.title} (${this.filteredCards.length} derived words)`);
  }

  /**
   * Mobile-Optimized "Original" Button: opens full original markdown note in reader view.
   */
  openOriginalNoteView(notePath) {
    if (!notePath) return;
    this.returnToFeedIndex = this.feedWordIndex;
    this.switchTab('home');
    this.openHomeSection(notePath, '', true);
  }

  prepareWordCards() {
    const pages = this.vaultIndex.pages || [];
    this.allWordCards = [];

    for (let i = 0; i < pages.length; i++) {
      const p = pages[i];
      const notePath = p.p;

      // Strictly include only individual vocabulary words
      if (this.isWordCard(notePath)) {
        const cleanName = notePath.slice(notePath.lastIndexOf('/') + 1).replace(/\.md$/i, '');
        const category = this.getCategoryFromPath(notePath);
        const cluster = this.getClusterFromPath(notePath);
        const status = this.getStatus(notePath);

        this.allWordCards.push({
          path: notePath,
          name: cleanName,
          category,
          cluster,
          status,
          rawPage: p
        });
      }
    }

    this.applyCardsFilter();

    if (this.pendingCardPath) {
      const pending = this.pendingCardPath;
      this.pendingCardPath = null;
      this.openWordCardByPath(pending);
    }
  }

  getStatus(notePath) {
    if (this.statusDb[notePath]) return this.statusDb[notePath];
    return 'unread';
  }

  setStatus(notePath, newStatus) {
    this.statusDb[notePath] = newStatus;
    this.saveStatusDb();

    // Sync with Firebase Cloud Tracking Engine
    try {
      trackingService.setStatus(notePath, newStatus);
    } catch {}

    // Haptic touch feedback if supported
    if (navigator.vibrate) navigator.vibrate(15);

    // Sync in card array
    const card = this.allWordCards.find(c => c.path === notePath);
    if (card) card.status = newStatus;

    // Send to backend if online
    fetch('/api/frontmatter', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ path: notePath, updates: { status: newStatus } })
    }).catch(() => {});

    // Refresh UI indicators
    this.updateTopStatusBadge(newStatus);
    this.updateTrackingHUD();
    this.showToast(`Marked ${newStatus === 'learned' ? '🟢 Learned' : newStatus === 'learning' ? '🟡 Studying' : '🔴 Unread'}`);
  }

  cycleStatus(notePath) {
    const current = this.getStatus(notePath);
    const next = current === 'unread' ? 'learning' : current === 'learning' ? 'learned' : 'unread';
    this.setStatus(notePath, next);
    return next;
  }

  resolveLinkPath(target, currentPath = '') {
    const withoutHash = target.split('#')[0].trim();
    const clean = withoutHash.replace(/\\/g, '/').replace(/^\.?\//, '').trim();
    if (this.vaultIndex && this.vaultIndex.pages) {
      const match = this.vaultIndex.pages.find(p =>
        p.p.toLowerCase() === clean.toLowerCase() ||
        p.p.toLowerCase() === (clean.toLowerCase() + '.md') ||
        p.p.toLowerCase().endsWith('/' + clean.toLowerCase()) ||
        p.p.toLowerCase().endsWith('/' + clean.toLowerCase() + '.md') ||
        p.p.slice(p.p.lastIndexOf('/') + 1).replace(/\.md$/i, '').toLowerCase() === clean.toLowerCase()
      );
      if (match) return match.p;
    }
    return clean.endsWith('.md') ? clean : `${clean}.md`;
  }

  /* ========================================================================
     NAVIGATION & TAB SWITCHING
     ======================================================================== */

  switchTab(tabName) {
    if (this.activeTab === tabName) return;

    this.cancelSpeech();
    this.activeTab = tabName;

    // Update Bottom Nav Buttons
    document.querySelectorAll('.mobile-tab-btn').forEach(btn => {
      btn.classList.toggle('is-active', btn.dataset.tab === tabName);
    });

    // Update Screen Visibility
    document.querySelectorAll('.mobile-view-screen').forEach(screen => {
      screen.classList.remove('is-active-tab');
    });

    const activeScreen = document.getElementById(`view-${tabName}`);
    if (activeScreen) {
      activeScreen.classList.add('is-active-tab');
    }

    // Update Top Navigation Bar Context
    this.updateTopBar();

    // Trigger tab-specific refreshes
    if (tabName === 'cards') {
      this.applyCardsFilter();
      if (this.cardsViewMode === 'feed') this.renderFeedCard('none');
      else this.renderCardList();
    } else if (tabName === 'daily') {
      if (!this.dailyCurrentCard) this.renderDailyCard(true);
    } else if (tabName === 'settings') {
      this.updateTrackingHUD();
    }
  }

  updateTopBar() {
    const backBtn = document.getElementById('top-back-btn');
    const breadcrumbs = document.getElementById('top-breadcrumbs');
    const statusBadge = document.getElementById('top-status-badge');

    if (this.activeTab === 'home') {
      if (this.homeStack.length > 0) {
        backBtn.style.display = 'inline-flex';
        let crumbsHtml = `<span class="crumb-link" data-depth="-1">Dashboards</span>`;
        for (let i = 0; i < this.homeStack.length; i++) {
          const item = this.homeStack[i];
          const isLast = i === this.homeStack.length - 1;
          crumbsHtml += ` <span style="opacity:0.4;">/</span> `;
          if (isLast) {
            crumbsHtml += `<span class="crumb-active">${escapeHtml(item.title)}</span>`;
          } else {
            crumbsHtml += `<span class="crumb-link" data-depth="${i}">${escapeHtml(item.title)}</span>`;
          }
        }
        breadcrumbs.innerHTML = crumbsHtml;
        breadcrumbs.querySelectorAll('.crumb-link').forEach(link => {
          link.addEventListener('click', () => {
            const depth = Number(link.dataset.depth);
            if (depth === -1) {
              this.renderHomeRoot();
            } else {
              while (this.homeStack.length > depth + 1) {
                this.goBackHome(false);
              }
            }
          });
        });

        const current = this.homeStack[this.homeStack.length - 1];
        if (current.path && !current.isHomeRoot) {
          const st = this.getStatus(current.path);
          this.updateTopStatusBadge(st);
        } else {
          statusBadge.style.display = 'none';
        }
      } else {
        backBtn.style.display = 'none';
        breadcrumbs.innerHTML = `<span class="crumb-active">🏛️ Classical Dashboards & Root Hub</span>`;
        statusBadge.style.display = 'none';
      }
    } else if (this.activeTab === 'cards') {
      backBtn.style.display = 'none';
      breadcrumbs.innerHTML = `<span class="crumb-active">📖 Word Card</span>`;
      statusBadge.style.display = 'none';
    } else if (this.activeTab === 'daily') {
      backBtn.style.display = 'none';
      breadcrumbs.innerHTML = `<span class="crumb-active">🎲 Daily Random Discovery</span>`;
      statusBadge.style.display = 'none';
    } else if (this.activeTab === 'settings') {
      backBtn.style.display = 'none';
      breadcrumbs.innerHTML = `<span class="crumb-active">⚙️ Settings & Tracking HUD</span>`;
      statusBadge.style.display = 'none';
    }
  }

  updateTopStatusBadge(status) {
    const badge = document.getElementById('top-status-badge');
    const dot = document.getElementById('top-status-dot');
    const text = document.getElementById('top-status-text');

    if (!badge || !dot || !text) return;

    badge.className = `status-indicator-pill ${status}`;
    badge.style.display = 'inline-flex';
    dot.textContent = status === 'learned' ? '🟢' : status === 'learning' ? '🟡' : '🔴';
    text.textContent = status === 'learned' ? 'Learned' : status === 'learning' ? 'Studying' : 'Unread';
  }

  /* ========================================================================
     TAB 1: HOME HUB & STUDY SUBPAGE STACK
     ======================================================================== */

  renderHomeRoot() {
    this.homeStack = [];
    this.currentHomeNote = null;
    this.activeScope = null;
    this.updateTopBar();

    const container = document.getElementById('home-page-container');
    container.innerHTML = '';

    const rootCard = document.createElement('div');
    rootCard.className = 'home-page-card-stack home-root-pane';

    // Calculate quick counts for pure vocabulary
    let totalLearned = 0;
    let totalStudying = 0;
    for (const p in this.statusDb) {
      if (this.statusDb[p] === 'learned') totalLearned++;
      else if (this.statusDb[p] === 'learning') totalStudying++;
    }

    rootCard.innerHTML = `
      <div class="home-hero-card">
        <div class="home-hero-pre">CLASSICAL MORPHOLOGY &amp; VOCABULARY DASHBOARDS</div>
        <div class="home-hero-title">Master Dashboards Hub</div>
        <div class="home-hero-subtitle">Explore 810 Greek root dashboards, 782 Latin root dashboards, and 30 Vocab Master clusters with cognitive anchors and morphological rules.</div>

        <div class="home-quick-stats-row">
          <div class="quick-stat-box">
            <div class="quick-stat-num" id="home-stat-learned" style="color:var(--web-success,#30D158);">${totalLearned.toLocaleString()}</div>
            <div class="quick-stat-lbl">Learned</div>
          </div>
          <div class="quick-stat-box">
            <div class="quick-stat-num" id="home-stat-studying" style="color:var(--web-amber,#FF9F0A);">${totalStudying.toLocaleString()}</div>
            <div class="quick-stat-lbl">Studying</div>
          </div>
          <div class="quick-stat-box">
            <div class="quick-stat-num" id="home-stat-dashboards" style="color:var(--web-accent,#d4a359);">1,543</div>
            <div class="quick-stat-lbl">Root Dashboards</div>
          </div>
        </div>
      </div>

      <div class="home-section-title">
        <span>ESSENTIAL MASTER DASHBOARDS</span>
        <span style="font-size:11px; opacity:0.8;">Tap to open</span>
      </div>

      <div class="category-card-list">
        <div class="category-card" data-open-path="Greek roots/01_Root_Dashboards/Dashboard — Greek Roots.md" data-title="Dashboard — Greek Roots">
          <div class="category-icon-box">🏛️</div>
          <div class="category-meta">
            <div class="category-meta-title">
              <span>Greek Roots Master Dashboard</span>
              <span style="font-size:12px; color:var(--web-text-muted);">810 Roots · 17,987 words</span>
            </div>
            <div class="category-meta-desc">Comprehensive directory of Greek root dashboards, 30 semantic clusters &amp; cognitive anchors</div>
          </div>
          <div class="category-chevron">›</div>
        </div>

        <div class="category-card" data-open-path="Latin roots/Master Table — Latin Roots.md" data-title="Master Table — Latin Roots">
          <div class="category-icon-box">📜</div>
          <div class="category-meta">
            <div class="category-meta-title">
              <span>Latin Roots Master Table (1–782)</span>
              <span style="font-size:12px; color:var(--web-text-muted);">782 Roots · 33,028 words</span>
            </div>
            <div class="category-meta-desc">782 canonical Latin roots directory with instant root dashboard links</div>
          </div>
          <div class="category-chevron">›</div>
        </div>

        <div class="category-card" data-open-path="English vocabulary master/000_Vocabulary_Master_MOC.md" data-title="Vocabulary Master MOC">
          <div class="category-icon-box">👑</div>
          <div class="category-meta">
            <div class="category-meta-title">
              <span>English Vocabulary Master MOC</span>
              <span style="font-size:12px; color:var(--web-text-muted);">30 Clusters · 583 words</span>
            </div>
            <div class="category-meta-desc">Semantic clusters across Anglo-Saxon kennings, phonaesthemes &amp; non-classical strata</div>
          </div>
          <div class="category-chevron">›</div>
        </div>

        <div class="category-card" data-open-path="Latin roots/03_Reference_and_Rules/Prefix latin.md" data-title="Prefix Latin — Morphological Rules">
          <div class="category-icon-box">🔤</div>
          <div class="category-meta">
            <div class="category-meta-title">
              <span>Prefix Latin — Morphological Rules</span>
            </div>
            <div class="category-meta-desc">Assimilation rules, directionals, intensives &amp; euphonic prefix shifts</div>
          </div>
          <div class="category-chevron">›</div>
        </div>

        <div class="category-card" data-open-path="Greek roots/03_Reference_and_Rules/Prefix Greek.md" data-title="Prefix Greek — Morphological Rules">
          <div class="category-icon-box">🔤</div>
          <div class="category-meta">
            <div class="category-meta-title">
              <span>Prefix Greek — Morphological Rules</span>
            </div>
            <div class="category-meta-desc">Alpha privative, prepositional compounding &amp; classical Greek prefixes</div>
          </div>
          <div class="category-chevron">›</div>
        </div>
      </div>

      <div class="home-section-title" style="margin-top:26px;">
        <span>ROOT &amp; CLUSTER DASHBOARDS EXPLORER</span>
        <span style="font-size:11px; opacity:0.8;" id="dashboards-count-badge">1,543 Dashboards</span>
      </div>

      <!-- Dashboards Search & Discipline Filter Bar -->
      <div class="dashboards-search-container">
        <div class="dashboards-search-box">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <circle cx="11" cy="11" r="8"></circle>
            <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
          </svg>
          <input id="dashboards-search-input" type="text" placeholder="Search 1,540+ roots, classical stems, or meanings..." autocomplete="off" spellcheck="false" />
          <button id="dashboards-search-clear" class="top-bar-btn" style="display: none; width: 22px; height: 22px; font-size: 13px;">✕</button>
        </div>

        <div class="dashboards-filter-chips" id="dashboards-category-chips">
          <button class="filter-chip active" data-cat="all">All Dashboards</button>
          <button class="filter-chip" data-cat="greek">🏛️ Greek Roots (810)</button>
          <button class="filter-chip" data-cat="latin">📜 Latin Roots (782)</button>
          <button class="filter-chip" data-cat="vocab">👑 Vocab Clusters (30)</button>
        </div>
      </div>

      <div id="root-dashboards-container" class="root-dashboards-grid">
        <!-- Rendered dynamically by this.renderRootDashboardsExplorer() -->
      </div>
    `;

    // Event listeners on static master dashboard cards
    rootCard.querySelectorAll('[data-open-path]').forEach(el => {
      el.addEventListener('click', () => {
        const path = el.dataset.openPath;
        const title = el.dataset.title || path;
        this.openHomeSection(path, title);
      });
    });

    container.appendChild(rootCard);

    // Mount interactive root & cluster dashboards explorer
    this.renderRootDashboardsExplorer();
    this.bindDashboardsSearchEvents();
  }

  renderRootDashboardsExplorer() {
    const container = document.getElementById('root-dashboards-container');
    if (!container) return;

    container.innerHTML = '';

    const allDashboards = Object.values(this.rootDashboardsDb || {});
    const q = (this.dashboardsSearchQuery || '').toLowerCase().trim();
    const cat = this.dashboardsFilterCategory || 'all';

    const filtered = allDashboards.filter(d => {
      if (cat !== 'all' && d.category !== cat) return false;
      if (q) {
        const rootMatch = (d.root || '').toLowerCase().includes(q);
        const scriptMatch = (d.script || '').toLowerCase().includes(q);
        const meaningMatch = (d.meaning || '').toLowerCase().includes(q);
        const anchorMatch = (d.anchor || '').toLowerCase().includes(q);
        const clusterMatch = (d.cluster || '').toLowerCase().includes(q);
        return rootMatch || scriptMatch || meaningMatch || anchorMatch || clusterMatch;
      }
      return true;
    });

    const badge = document.getElementById('dashboards-count-badge');
    if (badge) {
      badge.textContent = `${filtered.length.toLocaleString()} Dashboards`;
    }

    if (filtered.length === 0) {
      container.innerHTML = `
        <div style="grid-column: 1 / -1; text-align: center; padding: 36px 16px; color: var(--web-text-muted);">
          <div style="font-size: 32px; margin-bottom: 8px;">🔍</div>
          <div style="font-size: 15px; font-weight: 700; color: var(--web-text-primary);">No Dashboards Found</div>
          <div style="font-size: 12px; margin-top: 4px;">Try searching for another root stem, meaning, or clear filters.</div>
        </div>
      `;
      return;
    }

    const fragment = document.createDocumentFragment();
    const renderLimit = Math.min(filtered.length, 60);

    for (let i = 0; i < renderLimit; i++) {
      const d = filtered[i];
      const cardEl = document.createElement('div');
      cardEl.className = 'root-dashboard-card';
      const catEmoji = d.category === 'greek' ? '🏛️' : d.category === 'latin' ? '📜' : '👑';

      cardEl.innerHTML = `
        <div class="root-card-header">
          <div class="root-card-name">
            <span>${catEmoji}</span>
            <span>${escapeHtml(d.root)}</span>
            ${d.script ? `<span class="root-card-script">(${escapeHtml(d.script)})</span>` : ''}
          </div>
          <span class="root-discipline-tag">${d.category === 'greek' ? 'Greek' : d.category === 'latin' ? 'Latin' : 'Vocab'}</span>
        </div>
        <div class="root-card-meaning">“${escapeHtml(d.meaning || d.root)}”</div>
        ${d.anchor ? `<div class="root-card-anchor">💡 ${escapeHtml(d.anchor)}</div>` : ''}
        <div class="root-card-footer">
          <span class="root-card-words-badge">${d.wordCount || 1} derived words</span>
          <div class="root-card-actions">
            <button class="root-card-study-btn" data-action="study" title="Study this root's cards in Word Cards">📖 Study Words</button>
          </div>
        </div>
      `;

      cardEl.addEventListener('click', (e) => {
        if (e.target.closest('[data-action="study"]')) return;
        this.openHomeSection(d.path, `Dashboard — ${d.root}`);
      });

      cardEl.querySelector('[data-action="study"]')?.addEventListener('click', (e) => {
        e.stopPropagation();
        const scopeWords = this.getWordsForScope(d.path);
        this.openScopeInFeed({
          type: 'root',
          title: `${catEmoji} Root: ${d.root}`,
          path: d.path,
          words: scopeWords.length > 0 ? scopeWords : (d.words ? d.words.map(w => ({ name: w, path: `${d.path.slice(0, d.path.lastIndexOf('/'))}/${w}.md` })) : []),
          isLocked: true
        });
      });

      fragment.appendChild(cardEl);
    }

    container.appendChild(fragment);

    if (filtered.length > 60) {
      const moreBtn = document.createElement('div');
      moreBtn.style = "grid-column: 1 / -1; text-align: center; padding: 12px 0;";
      moreBtn.innerHTML = `
        <button class="settings-action-btn" style="max-width: 240px; margin: 0 auto;">
          <span>Load More (+${Math.min(filtered.length - 60, 60)})</span>
        </button>
      `;
      moreBtn.querySelector('button').addEventListener('click', () => {
        moreBtn.remove();
        for (let i = 60; i < filtered.length; i++) {
          const d = filtered[i];
          const cardEl = document.createElement('div');
          cardEl.className = 'root-dashboard-card';
          const catEmoji = d.category === 'greek' ? '🏛️' : d.category === 'latin' ? '📜' : '👑';
          cardEl.innerHTML = `
            <div class="root-card-header">
              <div class="root-card-name">
                <span>${catEmoji}</span>
                <span>${escapeHtml(d.root)}</span>
                ${d.script ? `<span class="root-card-script">(${escapeHtml(d.script)})</span>` : ''}
              </div>
              <span class="root-discipline-tag">${d.category === 'greek' ? 'Greek' : d.category === 'latin' ? 'Latin' : 'Vocab'}</span>
            </div>
            <div class="root-card-meaning">“${escapeHtml(d.meaning || d.root)}”</div>
            ${d.anchor ? `<div class="root-card-anchor">💡 ${escapeHtml(d.anchor)}</div>` : ''}
            <div class="root-card-footer">
              <span class="root-card-words-badge">${d.wordCount || 1} derived words</span>
              <div class="root-card-actions">
                <button class="root-card-study-btn" data-action="study" title="Study this root's cards in Word Cards">📖 Study Words</button>
              </div>
            </div>
          `;
          cardEl.addEventListener('click', (e) => {
            if (e.target.closest('[data-action="study"]')) return;
            this.openHomeSection(d.path, `Dashboard — ${d.root}`);
          });
          cardEl.querySelector('[data-action="study"]')?.addEventListener('click', (e) => {
            e.stopPropagation();
            const scopeWords = this.getWordsForScope(d.path);
            this.openScopeInFeed({
              type: 'root',
              title: `${catEmoji} Root: ${d.root}`,
              path: d.path,
              words: scopeWords.length > 0 ? scopeWords : (d.words ? d.words.map(w => ({ name: w, path: `${d.path.slice(0, d.path.lastIndexOf('/'))}/${w}.md` })) : []),
              isLocked: true
            });
          });
          container.appendChild(cardEl);
        }
      });
      container.appendChild(moreBtn);
    }
  }

  bindDashboardsSearchEvents() {
    const input = document.getElementById('dashboards-search-input');
    const clearBtn = document.getElementById('dashboards-search-clear');
    let timer = null;

    input?.addEventListener('input', (e) => {
      this.dashboardsSearchQuery = e.target.value;
      if (clearBtn) clearBtn.style.display = this.dashboardsSearchQuery ? 'inline-flex' : 'none';
      clearTimeout(timer);
      timer = setTimeout(() => {
        this.renderRootDashboardsExplorer();
      }, 120);
    });

    clearBtn?.addEventListener('click', () => {
      if (input) input.value = '';
      this.dashboardsSearchQuery = '';
      clearBtn.style.display = 'none';
      this.renderRootDashboardsExplorer();
    });

    document.querySelectorAll('#dashboards-category-chips .filter-chip').forEach(chip => {
      chip.addEventListener('click', () => {
        document.querySelectorAll('#dashboards-category-chips .filter-chip').forEach(c => c.classList.remove('active'));
        chip.classList.add('active');
        this.dashboardsFilterCategory = chip.dataset.cat;
        this.renderRootDashboardsExplorer();
      });
    });
  }

  async openHomeSection(notePath, noteTitle = '', isDirectOriginalView = false) {
    // If the note is an individual word card and not opened via Original button, ROUTE TO TAB 2!
    if (!isDirectOriginalView && this.isWordCard(notePath)) {
      this.switchTab('cards');
      this.openWordCardByPath(notePath);
      return;
    }

    // It's a Study Page or Direct Original Note View -> Open in Home Stack!
    const title = noteTitle || notePath.slice(notePath.lastIndexOf('/') + 1).replace(/\.md$/i, '');

    // Highlight category card in root navigation pane
    document.querySelectorAll('.home-root-pane [data-open-path]').forEach(el => {
      const isMatch = el.dataset.openPath === notePath;
      el.classList.toggle('is-active', isMatch);
    });

    const container = document.getElementById('home-page-container');

    // On wide screens (desktop monitors >= 900px), if navigating from root list, replace existing reader pane
    if (window.innerWidth >= 900 && container) {
      const isFromRoot = Array.from(container.querySelectorAll('.home-root-pane [data-open-path]')).some(el => el.dataset.openPath === notePath);
      if (isFromRoot && !isDirectOriginalView) {
        container.querySelectorAll('.home-reader-pane').forEach(r => r.remove());
        this.homeStack = [];
      }
    }

    this.homeStack.push({ path: notePath, title, isHomeRoot: false, isOriginalNoteView: isDirectOriginalView });
    this.updateTopBar();

    try {
      window.history.pushState({ notePath, depth: this.homeStack.length }, '');
    } catch {}

    // Create new page element with reader pane class
    const pageEl = document.createElement('div');
    pageEl.className = 'home-page-card-stack page-enter-right home-reader-pane';

    pageEl.innerHTML = `
      <div class="note-page-reader">
        <div class="note-page-header">
          <h1 class="note-page-title">${escapeHtml(title)}</h1>
          <div class="note-page-meta-row">
            <span style="font-size:12px; color:var(--web-text-muted);">${escapeHtml(notePath)}</span>
          </div>
        </div>
        <div class="note-body-content markdown-reading-view">
          <div style="padding:20px; text-align:center; color:var(--web-text-muted);">Loading note content...</div>
        </div>
      </div>
    `;

    container.appendChild(pageEl);

    // Fetch note content with robust pre-bundled core notes fallback
    const rawContent = await this.fetchNoteWithFallback(notePath);

    const bodyContainer = pageEl.querySelector('.note-body-content');
    if (rawContent) {
      const rendered = renderObsidianMarkdown(rawContent, notePath, this.runtime);
      bodyContainer.innerHTML = rendered.html;

      // A. If opened via [📄 Original Note], prepend smooth return to feed bar
      if (isDirectOriginalView) {
        const returnBar = document.createElement('div');
        returnBar.className = 'return-to-feed-bar';
        returnBar.innerHTML = `
          <span>‹ Return to Word Feed</span>
          <span>Card #${(this.returnToFeedIndex + 1).toLocaleString()} ›</span>
        `;
        returnBar.addEventListener('click', () => {
          this.switchTab('cards');
          this.renderFeedCard('none');
        });
        bodyContainer.prepend(returnBar);
      }

      // B. If a Root Dashboard, Vocab Master Cluster, or Discipline Section is opened, link Tab 2 and inject study CTA banner
      if (!isDirectOriginalView) {
        const scopeWords = this.getWordsForScope(notePath);
        if (scopeWords.length > 0) {
          const isDash = /^Dashboard\s*[—–-]/i.test(notePath.split('/').pop()) || notePath.includes('Dashboard —') || notePath.includes('Dashboard -');
          const isVocab = notePath.startsWith('English vocabulary master');
          const isCluster = notePath.includes('Cluster ') || notePath.includes('Semantic Field');
          const scopeType = isDash ? 'root' : isCluster ? 'cluster' : 'discipline';

          this.activeScope = {
            type: scopeType,
            title: title,
            path: notePath,
            words: scopeWords,
            isLocked: true
          };
          this.feedWordIndex = 0;
          this.cardsFilterCategory = 'all';
          this.cardsFilterStatus = 'all';
          this.cardsSearchQuery = '';
          this.applyCardsFilter();

          const ctaEl = document.createElement('div');
          ctaEl.className = 'home-study-feed-cta';
          ctaEl.innerHTML = `
            <div class="cta-left">
              <div class="cta-title">🔒 Locked to Word Cards: ${scopeWords.length} ${isDash ? 'Derived Words' : 'Words'}</div>
              <div class="cta-sub">${escapeHtml(title)} scoped into Tab 2 Word Cards feed</div>
            </div>
            <div class="cta-btn-pill">Study Word Cards ›</div>
          `;
          ctaEl.addEventListener('click', () => {
            this.openScopeInFeed(this.activeScope);
          });
          bodyContainer.prepend(ctaEl);
        } else {
          // If viewing general reference rules or files without vocabulary words, clear activeScope only if not locked to a dashboard
          if (!notePath.includes('00 Language Hub') && !notePath.includes('Progress') && !this.activeScope?.isLocked) {
            this.activeScope = null;
          }
        }
      }

      // 1. Execute all ```dataviewjs blocks in this note!
      const dvSlots = bodyContainer.querySelectorAll('.dataviewjs-container');
      dvSlots.forEach(slot => {
        const idx = Number(slot.getAttribute('data-dv-index'));
        const code = rendered.dataviewBlocks[idx];
        if (code && this.runtime && this.runtime.executeDataviewJS) {
          try {
            this.runtime.executeDataviewJS(code, slot, notePath);
          } catch (err) {
            console.warn('Dataview execution error in note:', notePath, err);
          }
        }
      });

      // 1b. Mount Meta Bind status toggles (`INPUT[inlineSelect(...):status]`)
      const metaMounts = bodyContainer.querySelectorAll('.meta-bind-status-mount');
      metaMounts.forEach(mount => {
        const row = mount.closest('tr');
        const rowLink = row ? row.querySelector('a.internal-link[data-href]') : null;
        const targetPath = rowLink
          ? this.resolveLinkPath(rowLink.getAttribute('data-href'), notePath)
          : notePath;
        const currentStatus = this.getStatus(targetPath);
        const toggle = createAppleStatusToggle(currentStatus, async (nextStatus) => {
          this.setStatus(targetPath, nextStatus);
        });
        mount.replaceWith(toggle);
      });

      // 2. Wire up all internal links (from Markdown & Dataview)
      bodyContainer.querySelectorAll('a.internal-link').forEach(link => {
        link.addEventListener('click', (e) => {
          e.preventDefault();
          const target = link.dataset.href;
          if (target) {
            const resolved = this.resolveLinkPath(target, notePath);
            if (this.isWordCard(resolved)) {
              this.switchTab('cards');
              this.openWordCardByPath(resolved);
            } else {
              this.openHomeSection(resolved);
            }
          }
        });
      });
    } else {
      // Fallback: list child words & dashboards in this folder
      const folder = notePath.slice(0, notePath.lastIndexOf('/') + 1);
      const childWords = (this.vaultIndex.pages || []).filter(p => p.p.startsWith(folder) && p.p !== notePath && !p.p.endsWith('Dashboard — ' + title + '.md'));

      if (childWords.length > 0) {
        let listHtml = `
          <div style="margin-bottom:16px;">
            <div style="font-size:11px; font-weight:800; letter-spacing:1px; color:var(--web-accent); text-transform:uppercase; margin-bottom:4px;">CLASSICAL ROOT DASHBOARD</div>
            <h2 style="font-size:20px; font-weight:800; color:var(--web-text-primary); margin-bottom:6px;">${escapeHtml(title)}</h2>
            <p style="font-size:13px; color:var(--web-text-secondary); margin-bottom:14px;">${childWords.length} vocabulary notes in this section. Tap any card below to study:</p>
          </div>
          <div class="category-card-list">
        `;

        for (const cw of childWords) {
          const wName = cw.p.slice(cw.p.lastIndexOf('/') + 1).replace(/\.md$/i, '');
          const st = this.getStatus(cw.p);
          const badge = st === 'learned' ? '🟢 Learned' : st === 'learning' ? '🟡 Studying' : '🔴 Unread';
          const badgeCls = st;
          listHtml += `
            <div class="category-card" data-card-path="${escapeAttr(cw.p)}" style="padding:12px 14px;">
              <div class="category-meta">
                <div class="category-meta-title">
                  <span>${escapeHtml(wName)}</span>
                  <span class="status-indicator-pill ${badgeCls}" style="font-size:10px; padding:2px 8px;">${badge}</span>
                </div>
              </div>
              <div class="category-chevron">›</div>
            </div>
          `;
        }

        listHtml += `</div>`;
        bodyContainer.innerHTML = listHtml;

        bodyContainer.querySelectorAll('[data-card-path]').forEach(cardEl => {
          cardEl.addEventListener('click', () => {
            const cPath = cardEl.dataset.cardPath;
            if (this.isWordCard(cPath)) {
              this.switchTab('cards');
              this.openWordCardByPath(cPath);
            } else {
              this.openHomeSection(cPath);
            }
          });
        });
      } else {
        bodyContainer.innerHTML = `
          <div style="padding:24px 10px; text-align:center;">
            <p style="color:var(--web-text-secondary); margin-bottom:12px;">This study dashboard is ready in your vault.</p>
            <button class="settings-action-btn" style="max-width:240px; margin:0 auto;" id="btn-open-category-cards">
              📱 View Vocabulary Words in Feed Tab
            </button>
          </div>
        `;
        pageEl.querySelector('#btn-open-category-cards')?.addEventListener('click', () => {
          this.switchTab('cards');
        });
      }
    }
  }

  goBackHome(updateHistory = true) {
    if (this.homeStack.length === 0) return;

    const container = document.getElementById('home-page-container');
    const pages = container.querySelectorAll('.home-page-card-stack');

    if (pages.length > 1) {
      const topPage = pages[pages.length - 1];
      topPage.classList.add('page-exit-right');
      setTimeout(() => {
        topPage.remove();
      }, 250);
    }

    this.homeStack.pop();
    this.updateTopBar();

    if (this.homeStack.length === 0) {
      this.renderHomeRoot();
    }
  }

  advanceHomeNext() {
    // If reading a section, find next logical study page or child cluster
    const current = this.homeStack[this.homeStack.length - 1];
    if (!current || !current.path) return;

    const currentPath = current.path;
    const parentFolder = currentPath.slice(0, currentPath.lastIndexOf('/'));
    const peers = (this.vaultIndex.pages || []).filter(p =>
      p.p.startsWith(parentFolder) &&
      this.isStudyPage(p.p) &&
      p.p !== currentPath
    );

    if (peers.length > 0) {
      const nextNote = peers[0];
      this.openHomeSection(nextNote.p);
    }
  }

  /* ========================================================================
     TAB 2: WORD CARDS (TIKTOK-STYLE VERTICAL SWIPABLE FEED)
     ======================================================================== */

  applyCardsFilter() {
    const q = (this.cardsSearchQuery || '').toLowerCase().trim();
    const cat = this.cardsFilterCategory;
    const status = this.cardsFilterStatus;
    const scopeBanner = document.getElementById('cards-scope-banner');
    const scopeText = document.getElementById('scope-banner-text');

    let pool = this.allWordCards;

    // A. Apply Root Dashboard, Cluster, or Discipline Scope (Tab 1 <-> Tab 2 link)
    if (this.activeScope && this.activeScope.words && this.activeScope.words.length > 0) {
      const scopeSet = new Set(this.activeScope.words.map(w => w.path || w.p));
      pool = this.allWordCards.filter(c => scopeSet.has(c.path));
      if (scopeBanner) {
        scopeBanner.style.display = 'flex';
        if (scopeText) {
          scopeText.innerHTML = `🔒 <strong>Locked:</strong> ${escapeHtml(this.activeScope.title)} <span style="opacity:0.85;">(${pool.length} derived words)</span>`;
        }
      }
    } else {
      if (scopeBanner) scopeBanner.style.display = 'none';
    }

    this.filteredCards = pool.filter(c => {
      // Category filter (only active if not scoped)
      if (!this.activeScope && cat !== 'all' && c.category !== cat) return false;

      // Status filter
      if (status !== 'all' && c.status !== status) return false;

      // Query filter
      if (q) {
        const nameMatch = c.name.toLowerCase().includes(q);
        const clusterMatch = (c.cluster || '').toLowerCase().includes(q);
        return nameMatch || clusterMatch;
      }
      return true;
    });

    if (this.feedWordIndex >= this.filteredCards.length) {
      this.feedWordIndex = Math.max(0, this.filteredCards.length - 1);
    }
    if (this.cardsViewMode === 'list' || window.innerWidth >= 900) {
      this.renderCardList();
    }
  }

  async renderFeedCard(direction = 'none') {
    this.cancelSpeech();
    const container = document.getElementById('tiktok-feed-wrapper');
    if (!container) return;

    this._renderFeedSeq = (this._renderFeedSeq || 0) + 1;
    const currentSeq = this._renderFeedSeq;

    if (this.filteredCards.length === 0) {
      container.innerHTML = `
        <div class="tiktok-slide" style="align-items:center; justify-content:center; text-align:center;">
          <div style="font-size: 38px; margin-bottom: 12px;">🔍</div>
          <div style="font-size: 18px; font-weight: 800; color: var(--web-text-primary);">No Vocabulary Words Found</div>
          <div style="font-size: 13px; color: var(--web-text-muted); margin-top: 6px; max-width: 260px;">
            ${this.activeScope ? `No words in ${escapeHtml(this.activeScope.title)} match your filter.` : 'No individual words match your active category or status filter.'}
          </div>
          <button class="settings-action-btn" id="btn-reset-feed-filters" style="margin-top: 16px; max-width: 180px;">
            ${this.activeScope ? 'Clear Scope & Reset' : 'Reset Filters'}
          </button>
        </div>
      `;
      container.querySelector('#btn-reset-feed-filters')?.addEventListener('click', () => {
        this.activeScope = null;
        this.cardsSearchQuery = '';
        this.cardsFilterCategory = 'all';
        this.cardsFilterStatus = 'all';
        const searchInput = document.getElementById('cards-search-input');
        if (searchInput) searchInput.value = '';
        document.querySelectorAll('#cards-category-chips .filter-chip').forEach(c => c.classList.toggle('active', c.dataset.cat === 'all'));
        document.querySelectorAll('#cards-status-chips .filter-chip').forEach(c => c.classList.toggle('active', c.dataset.status === 'all'));
        this.applyCardsFilter();
        this.renderFeedCard('none');
      });
      return;
    }

    if (this.feedWordIndex >= this.filteredCards.length) this.feedWordIndex = this.filteredCards.length - 1;
    if (this.feedWordIndex < 0) this.feedWordIndex = 0;

    const card = this.filteredCards[this.feedWordIndex];
    const status = this.getStatus(card.path);

    // Update position pill
    const posPill = document.getElementById('feed-position-pill');
    if (posPill) {
      posPill.textContent = `${(this.feedWordIndex + 1).toLocaleString()} / ${this.filteredCards.length.toLocaleString()}`;
    }

    // Fetch card content with robust pre-bundled core notes fallback
    const rawContent = await this.fetchNoteWithFallback(card.path);

    if (currentSeq !== this._renderFeedSeq) return;

    const { definitions, quotes, usages, pos } = this.extractCardDetails(card, rawContent);
    const rootDetails = this.findRootDashboardForWord(card.path);

    const slideEl = document.createElement('div');
    slideEl.className = 'tiktok-slide';
    if (direction === 'up') slideEl.classList.add('slide-up-in');
    else if (direction === 'down') slideEl.classList.add('slide-down-in');

    slideEl.innerHTML = `
      <div class="clean-card-surface">
        <!-- 1. ROOT DASHBOARD KEYSTONE (Prominent Dashboard & Root details right on the card!) -->
        ${rootDetails ? `
          <div class="card-root-keystone" data-root-path="${escapeAttr(rootDetails.path || '')}" title="Tap to view full Root Dashboard and cognate family">
            <div class="root-keystone-top">
              <span class="root-discipline-tag">${rootDetails.category === 'greek' ? '🏛️ Greek Root' : rootDetails.category === 'latin' ? '📜 Latin Root' : '👑 Vocab Cluster'}</span>
              ${rootDetails.script ? `<span class="root-script">${escapeHtml(rootDetails.script)}</span>` : ''}
              <span class="root-cluster-tag">${escapeHtml(rootDetails.cluster || '')}</span>
            </div>
            <div class="root-meaning-row">
              <span class="root-meaning-label">Root Meaning:</span>
              <span class="root-meaning-val">“${escapeHtml(rootDetails.meaning || rootDetails.root)}”</span>
            </div>
            ${rootDetails.anchor ? `
              <div class="root-anchor-text">💡 <strong>Cognitive Anchor:</strong> ${escapeHtml(rootDetails.anchor)}</div>
            ` : ''}
            <div class="root-view-cta-link">🏛️ View Full Root Dashboard (${rootDetails.wordCount || 1} derived words) ›</div>
          </div>
        ` : ''}

        <!-- 2. CLEAN WORD HEADER & JUST THE BUTTON -->
        <div class="clean-word-header">
          <div class="clean-word-title-group">
            <div class="clean-word-title">${escapeHtml(card.name)}</div>
            ${pos ? `<span class="clean-pos-badge">${escapeHtml(pos)}</span>` : ''}
          </div>
          <div class="clean-buttons-group">
            <button class="clean-pronounce-btn" id="btn-pronounce-word" title="Pronounce Word">
              <span class="pronounce-icon">🔊</span>
            </button>
            <div id="feed-card-apple-toggle-mount"></div>
          </div>
        </div>

        <!-- 3. THE NOTES: FULL DEFINITIONS & FULL EXAMPLE PHRASES -->
        <div class="clean-notes-body">
          <!-- Full Definitions -->
          <div class="clean-def-card">
            <div class="clean-def-heading">
              <span>📖</span> <span>Definitions &amp; Semantic Range</span>
            </div>
            <div class="clean-def-list">
              ${definitions.map(d => `
                <div class="clean-def-item">
                  ${d.label ? `<span class="clean-def-label">${escapeHtml(d.label)}</span>` : ''}
                  <span class="clean-def-text">${escapeHtml(d.text)}</span>
                </div>
              `).join('')}
            </div>
          </div>

          <!-- Full Authentic Example Phrases & Literary Quotations -->
          ${quotes.length > 0 ? `
            <div class="clean-quotes-card">
              <div class="clean-quotes-heading">
                <span>💬</span> <span>Authentic Context &amp; Example Phrases (${quotes.length})</span>
              </div>
              ${quotes.map(q => `
                <div class="clean-quote-bubble">
                  <div class="clean-quote-text">“${this.formatQuoteHtml(q.quote, card.name)}”</div>
                  ${(q.author || q.work) ? `
                    <div class="clean-quote-author">
                      — ${escapeHtml(q.author)}${q.work ? ` <em>(${escapeHtml(q.work)})</em>` : ''}
                    </div>
                  ` : ''}
                </div>
              `).join('')}
            </div>
          ` : ''}

          <!-- Full Usage & Syntactic Application (if present) -->
          ${usages.length > 0 ? `
            <div class="clean-usage-card">
              <div class="clean-usage-heading">🎯 Usage &amp; Syntactic Application</div>
              ${usages.map(u => `
                <div class="clean-usage-item">${u}</div>
              `).join('')}
            </div>
          ` : ''}

          <div class="clean-swipe-cue">
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="18 15 12 9 6 15"></polyline></svg>
            <span>Swipe up for next word</span>
          </div>
        </div>
      </div>
    `;

    // Mount Apple Glide Toggle directly in the header
    const appleMount = slideEl.querySelector('#feed-card-apple-toggle-mount');
    if (appleMount) {
      const appleToggleEl = createAppleStatusToggle(status, async (nextStatus) => {
        this.setStatus(card.path, nextStatus);
      });
      appleMount.appendChild(appleToggleEl);
    }

    // Audio Speech Pronunciation
    const pronounceBtn = slideEl.querySelector('#btn-pronounce-word');
    pronounceBtn?.addEventListener('click', (e) => {
      e.stopPropagation();
      this.playPronunciation(card.name, pronounceBtn);
    });

    // Root Dashboard Keystone Link -> opens full root dashboard on Dashboards tab
    slideEl.querySelector('.card-root-keystone')?.addEventListener('click', (e) => {
      e.stopPropagation();
      const rPath = e.currentTarget.dataset.rootPath;
      if (rPath) {
        this.switchTab('home');
        this.openHomeSection(rPath);
      }
    });

    const existingSlides = Array.from(container.querySelectorAll('.tiktok-slide'));
    if (existingSlides.length > 0 && direction !== 'none') {
      for (let i = 0; i < existingSlides.length - 1; i++) {
        existingSlides[i].remove();
      }
      const activeOldSlide = existingSlides[existingSlides.length - 1];
      activeOldSlide.classList.remove('slide-up-in', 'slide-down-in');
      activeOldSlide.classList.add(direction === 'up' ? 'slide-up-out' : 'slide-down-out');
      slideEl.scrollTop = 0;
      container.appendChild(slideEl);
      this.isSlideTransitioning = true;

      const cleanup = () => {
        if (activeOldSlide.parentNode === container) {
          activeOldSlide.remove();
        }
        this.isSlideTransitioning = false;
      };
      activeOldSlide.addEventListener('animationend', cleanup, { once: true });
      setTimeout(cleanup, 280);
    } else {
      container.innerHTML = '';
      slideEl.scrollTop = 0;
      container.appendChild(slideEl);
      this.isSlideTransitioning = false;
    }
    this.syncCardListHighlight();
  }

  nextFeedWord() {
    this.cancelSpeech();
    if (this.isSlideTransitioning) return;
    if (this.feedWordIndex < this.filteredCards.length - 1) {
      this.feedWordIndex++;
      this.renderFeedCard('up');
    } else {
      this.showToast('Reached end of vocabulary deck');
    }
  }

  prevFeedWord() {
    this.cancelSpeech();
    if (this.isSlideTransitioning) return;
    if (this.feedWordIndex > 0) {
      this.feedWordIndex--;
      this.renderFeedCard('down');
    } else {
      this.showToast('At the beginning of vocabulary deck');
    }
  }

  /* ========================================================================
     AUDIO SPEECH SYNTHESIS ENGINE (WEB SPEECH API)
     ======================================================================== */

  initSpeechEngine() {
    if (typeof window !== 'undefined' && 'speechSynthesis' in window) {
      const loadVoices = () => {
        try {
          const list = window.speechSynthesis.getVoices();
          if (list && list.length > 0) {
            this.speechVoices = list;
          }
        } catch (e) {
          console.warn('Error loading speech voices:', e);
        }
      };

      loadVoices();
      try {
        if ('onvoiceschanged' in window.speechSynthesis) {
          window.speechSynthesis.onvoiceschanged = loadVoices;
        }
        window.speechSynthesis.addEventListener?.('voiceschanged', loadVoices);
      } catch (e) {
        window.speechSynthesis.onvoiceschanged = loadVoices;
      }
    }
  }

  getOptimalVoice() {
    if (!this.speechVoices || this.speechVoices.length === 0) {
      if (typeof window !== 'undefined' && 'speechSynthesis' in window) {
        try {
          this.speechVoices = window.speechSynthesis.getVoices() || [];
        } catch {}
      }
    }
    const voices = this.speechVoices || [];
    if (voices.length === 0) return null;

    // Filter English voices (en-US, en-GB, en-AU, etc.)
    const enVoices = voices.filter(v => v.lang && /^en[-_]/i.test(v.lang));
    if (enVoices.length === 0) return voices[0];

    const qualityKeywords = [
      'natural', 'neural', 'premium', 'enhanced', 'google',
      'samantha', 'daniel', 'karen', 'oliver', 'serena', 'moira', 'alex', 'ava', 'allison'
    ];

    // Priority 1: High-quality / Neural en-US voice
    const premiumEnUs = enVoices.find(v => {
      const normLang = (v.lang || '').replace('_', '-').toLowerCase();
      const name = (v.name || '').toLowerCase();
      return normLang === 'en-us' && qualityKeywords.some(kw => name.includes(kw));
    });
    if (premiumEnUs) return premiumEnUs;

    // Priority 2: High-quality / Neural en-GB voice
    const premiumEnGb = enVoices.find(v => {
      const normLang = (v.lang || '').replace('_', '-').toLowerCase();
      const name = (v.name || '').toLowerCase();
      return normLang === 'en-gb' && qualityKeywords.some(kw => name.includes(kw));
    });
    if (premiumEnGb) return premiumEnGb;

    // Priority 3: Default system en-US voice
    const defaultEnUs = enVoices.find(v => {
      const normLang = (v.lang || '').replace('_', '-').toLowerCase();
      return normLang === 'en-us' && v.default;
    });
    if (defaultEnUs) return defaultEnUs;

    // Priority 4: Any standard en-US voice
    const standardEnUs = enVoices.find(v => {
      const normLang = (v.lang || '').replace('_', '-').toLowerCase();
      return normLang === 'en-us';
    });
    if (standardEnUs) return standardEnUs;

    // Priority 5: Any standard en-GB voice
    const standardEnGb = enVoices.find(v => {
      const normLang = (v.lang || '').replace('_', '-').toLowerCase();
      return normLang === 'en-gb';
    });
    if (standardEnGb) return standardEnGb;

    // Priority 6: Fallback to first available English voice
    return enVoices[0];
  }

  playPronunciation(word, buttonEl = null) {
    if (typeof window === 'undefined' || !('speechSynthesis' in window) || typeof SpeechSynthesisUtterance === 'undefined') {
      this.showToast('Speech pronunciation is unsupported on this browser');
      return;
    }

    const cleanWord = (word || '').replace(/[\[\]*_`#]/g, '').trim();
    if (!cleanWord) {
      this.showToast('No word available for pronunciation');
      return;
    }

    // Toggle off if currently speaking from the same button
    if (this.isSpeaking && buttonEl && this.activeSpeechButton === buttonEl) {
      this.cancelSpeech();
      return;
    }

    // Identify target button if not explicitly passed
    const targetBtn = buttonEl || (
      this.activeTab === 'cards'
        ? document.getElementById('btn-pronounce-word')
        : (this.activeTab === 'daily' ? document.getElementById('btn-daily-pronounce') : null)
    );

    // Cancel any previous stuck utterance queues (crucial for iOS & Android WebView)
    try {
      if (window.speechSynthesis.paused) {
        window.speechSynthesis.resume();
      }
      window.speechSynthesis.cancel();
    } catch (e) {
      console.warn('speechSynthesis cancel error:', e);
    }

    this.clearSpeechVisualFeedback();

    const utter = new SpeechSynthesisUtterance(cleanWord);
    utter.rate = 0.9;
    utter.pitch = 1.0;
    utter.volume = 1.0;

    const voice = this.getOptimalVoice();
    if (voice) {
      utter.voice = voice;
      utter.lang = voice.lang || 'en-US';
    } else {
      utter.lang = 'en-US';
    }

    // Retain global reference to protect against garbage collection prematurely cutting speech
    this.currentUtterance = utter;
    this.isSpeaking = true;

    utter.onstart = () => {
      this.isSpeaking = true;
      if (targetBtn) {
        this.setSpeechVisualFeedback(targetBtn);
      }
    };

    utter.onend = () => {
      this.isSpeaking = false;
      this.currentUtterance = null;
      this.clearSpeechVisualFeedback();
    };

    utter.onerror = (event) => {
      this.isSpeaking = false;
      this.currentUtterance = null;
      this.clearSpeechVisualFeedback();
      if (event && event.error && event.error !== 'canceled' && event.error !== 'interrupted') {
        console.warn('SpeechSynthesis error:', event);
        this.showToast('Pronunciation playback failed');
      }
    };

    try {
      window.speechSynthesis.speak(utter);
      if (targetBtn) {
        this.setSpeechVisualFeedback(targetBtn);
      }
    } catch (err) {
      console.error('SpeechSynthesis speak failed:', err);
      this.showToast('Pronunciation playback failed');
      this.clearSpeechVisualFeedback();
    }
  }

  speakWord(text, buttonEl = null) {
    return this.playPronunciation(text, buttonEl);
  }

  stopPronunciation() {
    this.cancelSpeech();
  }

  cancelSpeech() {
    if (typeof window !== 'undefined' && 'speechSynthesis' in window) {
      try {
        window.speechSynthesis.cancel();
      } catch (e) {
        console.warn('Speech cancellation error:', e);
      }
    }
    this.isSpeaking = false;
    this.currentUtterance = null;
    this.clearSpeechVisualFeedback();
  }

  setSpeechVisualFeedback(buttonEl) {
    if (!buttonEl) return;
    this.clearSpeechVisualFeedback();
    this.activeSpeechButton = buttonEl;
    buttonEl.classList.add('speaking');
    const label = buttonEl.querySelector('.pronounce-label') || buttonEl.querySelectorAll('span')[1];
    if (label && !label.dataset.originalLabel) {
      label.dataset.originalLabel = label.textContent;
      label.textContent = 'Playing...';
    }
  }

  clearSpeechVisualFeedback() {
    if (this.activeSpeechButton) {
      this.activeSpeechButton.classList.remove('speaking');
      const label = this.activeSpeechButton.querySelector('.pronounce-label') || this.activeSpeechButton.querySelectorAll('span')[1];
      if (label && label.dataset.originalLabel) {
        label.textContent = label.dataset.originalLabel;
        delete label.dataset.originalLabel;
      }
      this.activeSpeechButton = null;
    }
    document.querySelectorAll('.tiktok-pronounce-btn.speaking').forEach(btn => {
      btn.classList.remove('speaking');
      const lbl = btn.querySelector('.pronounce-label') || btn.querySelectorAll('span')[1];
      if (lbl && lbl.dataset.originalLabel) {
        lbl.textContent = lbl.dataset.originalLabel;
        delete lbl.dataset.originalLabel;
      }
    });
  }

  openWordCardByPath(notePath) {
    if (!notePath) return;
    this.cancelSpeech();

    // If activeScope doesn't contain this word, clear activeScope so target word is visible
    if (this.activeScope && this.activeScope.words) {
      const inScope = this.activeScope.words.some(w => (w.path || w.p) === notePath);
      if (!inScope) {
        this.activeScope = null;
      }
    }

    // Reset filters if necessary so the target word is visible
    this.cardsSearchQuery = '';
    this.cardsFilterCategory = 'all';
    this.cardsFilterStatus = 'all';
    this.applyCardsFilter();

    let idx = this.filteredCards.findIndex(c => c.path === notePath || c.path.toLowerCase() === notePath.toLowerCase());
    if (idx === -1) {
      const baseName = notePath.slice(notePath.lastIndexOf('/') + 1).replace(/\.md$/i, '').toLowerCase();
      idx = this.filteredCards.findIndex(c => c.name.toLowerCase() === baseName);
    }

    if (idx !== -1) {
      this.feedWordIndex = idx;
    } else {
      this.feedWordIndex = 0;
    }

    this.cardsViewMode = 'feed';
    this.updateCardsViewMode();
    this.renderFeedCard('none');
  }

  updateCardsViewMode() {
    const feedEl = document.getElementById('cards-feed-view');
    if (feedEl) feedEl.style.display = 'flex';
  }

  syncCardListHighlight() {
    const listEl = document.getElementById('cards-list-view');
    if (!listEl) return;
    const activeItem = listEl.querySelector(`.card-list-item[data-card-index="${this.feedWordIndex}"]`);
    listEl.querySelectorAll('.card-list-item').forEach(el => el.classList.remove('is-active'));
    if (activeItem) {
      activeItem.classList.add('is-active');
      if (window.innerWidth >= 900) {
        activeItem.scrollIntoView({ block: 'nearest', behavior: 'smooth' });
      }
    }
  }

  renderCardList() {
    const listEl = document.getElementById('cards-list-view');
    if (!listEl) return;

    if (this.cardListObserver) {
      this.cardListObserver.disconnect();
      this.cardListObserver = null;
    }

    listEl.innerHTML = '';
    this.cardListRenderedCount = 0;

    if (!this.filteredCards || this.filteredCards.length === 0) {
      listEl.innerHTML = `
        <div style="text-align: center; padding: 40px 20px; color: var(--web-text-muted);">
          <div style="font-size: 32px; margin-bottom: 8px;">🔍</div>
          <div style="font-size: 15px; font-weight: 700; color: var(--web-text-primary);">No Vocabulary Words Found</div>
          <div style="font-size: 12px; margin-top: 4px;">Try adjusting your search query or filter chips.</div>
        </div>
      `;
      return;
    }

    const itemsContainer = document.createElement('div');
    itemsContainer.className = 'cards-list-items-container';
    listEl.appendChild(itemsContainer);

    const footerEl = document.createElement('div');
    footerEl.className = 'cards-list-footer';
    listEl.appendChild(footerEl);

    // Initial batch of 50
    this.loadMoreCardListChunk(itemsContainer, footerEl);

    // Progressive virtual loading sentinel
    if ('IntersectionObserver' in window) {
      this.cardListObserver = new IntersectionObserver((entries) => {
        if (entries[0] && entries[0].isIntersecting) {
          if (this.cardListRenderedCount < this.filteredCards.length) {
            this.loadMoreCardListChunk(itemsContainer, footerEl);
          }
        }
      }, {
        root: listEl,
        rootMargin: '250px 0px',
        threshold: 0.05
      });

      this.cardListObserver.observe(footerEl);
    }
  }

  loadMoreCardListChunk(itemsContainer, footerEl) {
    const CHUNK_SIZE = 50;
    const total = this.filteredCards.length;
    const startIndex = this.cardListRenderedCount;
    if (startIndex >= total) return;

    const endIndex = Math.min(startIndex + CHUNK_SIZE, total);
    const chunk = this.filteredCards.slice(startIndex, endIndex);

    const fragment = document.createDocumentFragment();

    for (let i = 0; i < chunk.length; i++) {
      const card = chunk[i];
      const cardIndex = startIndex + i;
      const st = this.getStatus(card.path);
      const badge = st === 'learned' ? '🟢' : st === 'learning' ? '🟡' : '🔴';

      const isActive = cardIndex === this.feedWordIndex;
      const item = document.createElement('div');
      item.className = 'card-list-item' + (isActive ? ' is-active' : '');
      item.setAttribute('data-card-index', cardIndex);
      item.innerHTML = `
        <div style="min-width: 0; flex: 1; padding-right: 12px;">
          <div class="card-list-item-title">${escapeHtml(card.name)}</div>
          <div class="card-list-item-cluster">${escapeHtml(card.cluster || 'Cluster')} · ${escapeHtml(this.getCardCategoryLabel(card))}</div>
        </div>
        <div style="font-size: 16px; flex-shrink: 0;">${badge}</div>
      `;

      item.addEventListener('click', () => {
        this.feedWordIndex = cardIndex;
        if (window.innerWidth < 900) {
          this.cardsViewMode = 'feed';
          this.updateCardsViewMode();
        }
        this.renderFeedCard('none');
        this.syncCardListHighlight();
      });

      fragment.appendChild(item);
    }

    itemsContainer.appendChild(fragment);
    this.cardListRenderedCount = endIndex;

    if (footerEl) {
      if (this.cardListRenderedCount < total) {
        const remaining = total - this.cardListRenderedCount;
        const nextBatch = Math.min(remaining, CHUNK_SIZE);
        footerEl.innerHTML = `
          <div style="display: flex; flex-direction: column; align-items: center; gap: 8px; padding: 14px 0;">
            <div style="font-size: 12px; color: var(--web-text-muted);">
              Showing ${this.cardListRenderedCount.toLocaleString()} of ${total.toLocaleString()} words
            </div>
            <button class="settings-action-btn card-list-load-more-btn" style="max-width: 220px; padding: 8px 14px; font-size: 12.5px;">
              <span>⬇️ Load More (+${nextBatch})</span>
            </button>
          </div>
        `;
        const btn = footerEl.querySelector('.card-list-load-more-btn');
        if (btn) {
          btn.addEventListener('click', () => {
            this.loadMoreCardListChunk(itemsContainer, footerEl);
          });
        }
      } else {
        footerEl.innerHTML = `
          <div style="text-align: center; padding: 18px 0; font-size: 12px; color: var(--web-text-muted);">
            ✨ Showing all ${total.toLocaleString()} vocabulary words
          </div>
        `;
        if (this.cardListObserver) {
          this.cardListObserver.disconnect();
          this.cardListObserver = null;
        }
      }
    }
  }

  cleanDefinitionText(raw) {
    if (!raw) return '';
    return raw
      .replace(/\[\[|\]\]/g, '')
      .replace(/;\s*;\s*-\s*[a-zA-Z\s.-]+$/g, '')
      .replace(/;\s*-\s*[a-zA-Z\s.-]+$/g, '')
      .replace(/;\s*;+/g, ';')
      .trim();
  }

  formatQuoteHtml(quoteStr, wordName) {
    if (!quoteStr) return '';
    let safe = escapeHtml(quoteStr.replace(/^\*+|\*+$/g, '').trim());
    // Convert ***word*** or **word** into highlighted strong tags
    safe = safe.replace(/\*{2,3}([^*]+)\*{2,3}/g, '<strong class="quote-word-hl">$1</strong>');
    if (!safe.includes('quote-word-hl') && wordName && wordName.length >= 3) {
      const escapedWord = wordName.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
      const re = new RegExp(`\\b(${escapedWord}[a-z]*)\\b`, 'gi');
      safe = safe.replace(re, '<strong class="quote-word-hl">$1</strong>');
    }
    return safe;
  }

  extractCardDetails(card, rawContent) {
    const definitions = [];
    const quotes = [];
    const usages = [];
    let primaryDef = '';
    let secondaryDef = '';
    let pos = '';

    if (rawContent) {
      // 1. Check frontmatter for pos or part_of_speech
      const fmMatch = rawContent.match(/^---\r?\n([\s\S]*?)\r?\n---/);
      if (fmMatch) {
        const posMatch = fmMatch[1].match(/(?:pos|part_of_speech)\s*:\s*["']?([A-Za-z]+)["']?/i);
        if (posMatch) pos = posMatch[1].toLowerCase();
      }

      const lines = rawContent.split(/\r?\n/);
      let currentSection = null;

      for (let i = 0; i < lines.length; i++) {
        const line = lines[i];

        if (line.match(/>\s*\[!(?:book|definition|summary|note|lexicon|meaning)[^\]]*\]/i)) {
          currentSection = 'def';
          continue;
        } else if (line.match(/>\s*\[!(?:quote|cite|example|citation)[^\]]*\]/i)) {
          currentSection = 'quote';
          continue;
        } else if (line.match(/>\s*\[!(?:tip|usage|syntax|grammar|application)[^\]]*\]/i)) {
          currentSection = 'usage';
          continue;
        } else if (line.match(/>\s*\[!/i) || (!line.startsWith('>') && line.trim().startsWith('#'))) {
          currentSection = null;
        }

        if (currentSection === 'def') {
          const clean = line.replace(/^>\s*(?:-\s*)?/, '').trim();
          if (!clean) continue;

          // Match labeled senses: "1. **Primary Meaning**: text" or "**Nuance**: text"
          const senseMatch = clean.match(/(?:(?:[0-9]+\.|\*|-)\s*)?\*\*([^*]+)\*\*:\s*(.*)/i);
          if (senseMatch) {
            const label = senseMatch[1].replace(/^[0-9]+\.\s*/, '').trim();
            const text = this.cleanDefinitionText(senseMatch[2]);
            if (text) {
              definitions.push({ label, text });
              if (!primaryDef) primaryDef = text;
              else if (!secondaryDef) secondaryDef = text;
            }
          } else if (clean.match(/^[0-9]+\.\s+/)) {
            const text = this.cleanDefinitionText(clean.replace(/^[0-9]+\.\s*/, ''));
            if (text) {
              definitions.push({ label: `Sense ${definitions.length + 1}`, text });
              if (!primaryDef) primaryDef = text;
              else if (!secondaryDef) secondaryDef = text;
            }
          } else if (clean.length > 5 && !clean.startsWith('#')) {
            const text = this.cleanDefinitionText(clean);
            if (text) {
              definitions.push({ label: '', text });
              if (!primaryDef) primaryDef = text;
            }
          }
        } else if (currentSection === 'quote') {
          const clean = line.replace(/^>\s*-\s*(?:📜|📚|🔬|🌐|🗣️|💬)?\s*/, '').replace(/^>\s*/, '').trim();
          if (!clean) continue;

          // Match: **Author (*Work*):** *"Quote text..."* or **Author (*Work (Subtitle)*):** *"Quote..."*
          const headerQuoteMatch = clean.match(/^\*\*([\s\S]+?)\*\*:?\s*\*?["“]([\s\S]+?)["”]\*?$/) ||
                                   clean.match(/^\*\*([\s\S]+?)\*\*:?\s*\*?["“]([\s\S]+)$/) ||
                                   clean.match(/^\*\*([^*]+?)\s*\(\*?([\s\S]+?)\*?\):?\*\*:?\s*\*?["“]([\s\S]+?)["”]\*?/);

          if (headerQuoteMatch) {
            let rawHeader = headerQuoteMatch[1].trim();
            rawHeader = rawHeader.replace(/[:*]+$/, '').trim();
            const quoteText = (headerQuoteMatch[2] || '').replace(/["”*]+$/g, '').trim();

            const parenMatch = rawHeader.match(/^(.+?)\s*\(\*?([\s\S]+?)\*?\)$/);
            if (parenMatch) {
              const author = parenMatch[1].replace(/[:*]/g, '').trim();
              const work = parenMatch[2].replace(/[:*]/g, '').trim();
              quotes.push({ author, work, quote: quoteText });
            } else {
              const author = rawHeader.replace(/[:*]/g, '').trim();
              quotes.push({ author, work: '', quote: quoteText });
            }
          } else {
            const qm = clean.match(/["“]([^"”]+)["”]/);
            if (qm) {
              quotes.push({ author: '', work: '', quote: qm[1].trim() });
            } else if (clean.length > 10) {
              quotes.push({ author: '', work: '', quote: clean });
            }
          }
        } else if (currentSection === 'usage') {
          const clean = line.replace(/^>\s*(?:-\s*)?/, '').trim();
          if (clean && clean.length > 3) {
            const formatted = escapeHtml(clean).replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>');
            usages.push(formatted);
          }
        }
      }

      // Fallbacks if no callout was present
      if (definitions.length === 0) {
        const lineMatch = rawContent.match(/\*\*Definition:\*\*\s*([^\n]+)/i) || rawContent.match(/#+\s*Definition\s*\n+([^\n#]+)/i);
        if (lineMatch) {
          const text = this.cleanDefinitionText(lineMatch[1]);
          definitions.push({ label: 'Definition', text });
          primaryDef = text;
        }
      }
    }

    if (definitions.length === 0) {
      primaryDef = 'A fundamental classical vocabulary entry with rich etymological history and derived English usage.';
      definitions.push({
        label: 'Core Lexical Entry',
        text: primaryDef
      });
    }

    const primaryQuote = quotes[0] || null;

    return {
      definitions, // All definitions in full!
      quotes,      // All quotes in full!
      usages,      // All syntactic notes in full!
      defText: primaryDef,
      secondaryDef: secondaryDef && secondaryDef !== primaryDef ? secondaryDef : '',
      quoteText: primaryQuote ? primaryQuote.quote : '',
      quoteAuthor: primaryQuote ? primaryQuote.author : '',
      quoteWork: primaryQuote ? primaryQuote.work : '',
      pos: pos || (card.category === 'latin' ? 'Latin derivative' : card.category === 'greek' ? 'Greek derivative' : 'Vocabulary')
    };
  }

  /* ========================================================================
     TAB 3: DAILY WORD (RANDOM CARD SELECTION FROM PURE WORD POOL)
     ======================================================================== */

  async renderDailyCard(pickNew = false) {
    this.cancelSpeech();
    const contentEl = document.getElementById('daily-card-content');

    if (this.allWordCards.length === 0) {
      if (contentEl) {
        contentEl.innerHTML = `
          <div style="text-align:center; padding:30px 10px;">
            <div style="font-size:32px; margin-bottom:10px;">⏳</div>
            <p style="color:var(--web-text-secondary); font-size:14px;">Preparing random words from vault...</p>
          </div>
        `;
      }
      return;
    }

    if (pickNew || !this.dailyCurrentCard) {
      const randIdx = Math.floor(Math.random() * this.allWordCards.length);
      this.dailyCurrentCard = this.allWordCards[randIdx];
      this.dailyRevealed = false;
    }

    const card = this.dailyCurrentCard;
    if (!contentEl || !card) return;

    const status = this.getStatus(card.path);

    // Fetch content with robust pre-bundled core notes fallback
    const rawContent = await this.fetchNoteWithFallback(card.path);

    const { defText, secondaryDef, quotes, quoteText, quoteAuthor, quoteWork, pos } = this.extractCardDetails(card, rawContent);
    const quoteList = quotes && quotes.length > 0
      ? quotes
      : (quoteText ? [{ quote: quoteText, author: quoteAuthor, work: quoteWork }] : []);

    contentEl.innerHTML = `
      <div>
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px; gap:8px;">
          <span class="card-category-pill">${escapeHtml(this.getCardCategoryBadge(card))}</span>
          <div style="display:flex; align-items:center; gap:6px;">
            <button class="tiktok-pronounce-btn" id="btn-daily-pronounce" title="Pronounce Word" style="padding:3px 9px; font-size:11px;">
              <span class="pronounce-icon">🔊</span> <span class="pronounce-label">Listen</span>
            </button>
            <button class="tiktok-original-btn" id="btn-daily-original" title="View Full Original Markdown Note" style="padding:3px 9px; font-size:11px;">
              <span>📄</span> <span>Original</span>
            </button>
          </div>
        </div>

        <div class="daily-word-prominent">${escapeHtml(card.name)}</div>
        <div class="tiktok-morph-row" style="margin-bottom:12px;">
          <span class="tiktok-pos-pill">${escapeHtml(pos || 'vocabulary')}</span>
          <span class="tiktok-exhaustive-badge">
            <span>✅</span> <span>Exhaustive Permutation</span>
          </span>
        </div>

        <div class="daily-hint-blur ${this.dailyRevealed ? 'revealed' : ''}">
          <div class="tiktok-def-box" style="margin-top:10px;">
            <div class="tiktok-def-header-row">
              <div class="tiktok-def-title">📖 Core Definition</div>
              <div class="tiktok-def-status-mount" id="daily-card-apple-toggle-mount"></div>
            </div>
            <div class="tiktok-def-text">${escapeHtml(defText)}</div>
            ${secondaryDef ? `
              <div class="tiktok-def-secondary">
                <div class="tiktok-def-secondary-label">💡 Nuance / Specialized Register</div>
                <div class="tiktok-def-secondary-text">${escapeHtml(secondaryDef)}</div>
              </div>
            ` : ''}
          </div>

          ${quoteList.length > 0 ? `
            <div class="tiktok-quotes-stack" style="margin-top:10px;">
              <div class="tiktok-quotes-header">💬 Literary & Contextual Citations (${quoteList.length})</div>
              ${quoteList.map((q) => `
                <div class="tiktok-quote-box">
                  <div class="tiktok-quote-text">“${this.formatQuoteHtml(q.quote, card.name)}”</div>
                  ${(q.author || q.work) ? `
                    <div class="tiktok-quote-author">
                      <span>— ${escapeHtml(q.author)}${q.work ? ` <em>(${escapeHtml(q.work)})</em>` : ''}</span>
                    </div>
                  ` : ''}
                </div>
              `).join('')}
            </div>
          ` : ''}
        </div>

        ${!this.dailyRevealed ? `
          <div class="daily-reveal-btn-cue">
            <span>👆 Tap card to reveal definition & examples</span>
          </div>
        ` : ''}
      </div>

      <div style="margin-top:20px;">
        <div style="font-size:11.5px; font-weight:700; color:var(--web-text-muted); margin-bottom:8px; text-align:center;">
          Rate your mastery:
        </div>
        <div class="card-status-btn-group">
          <button class="card-status-btn ${status === 'unread' ? 'active unread' : ''}" data-daily-status="unread">
            <span>🔴 Need Review</span>
          </button>
          <button class="card-status-btn ${status === 'learning' ? 'active learning' : ''}" data-daily-status="learning">
            <span>🟡 Studying</span>
          </button>
          <button class="card-status-btn ${status === 'learned' ? 'active learned' : ''}" data-daily-status="learned">
            <span>🟢 Got It!</span>
          </button>
        </div>
      </div>
    `;

    // Mount Apple Glide status toggle at top of daily definition
    const dailyAppleMount = contentEl.querySelector('#daily-card-apple-toggle-mount');
    if (dailyAppleMount) {
      const dailyToggle = createAppleStatusToggle(status, async (nextStatus) => {
        this.setStatus(card.path, nextStatus);
        contentEl.querySelectorAll('[data-daily-status]').forEach(b => {
          const isMatch = b.dataset.dailyStatus === nextStatus;
          b.className = isMatch ? `card-status-btn active ${nextStatus}` : 'card-status-btn';
        });
      });
      dailyAppleMount.appendChild(dailyToggle);
    }

    // Pronounce audio
    const dailyPronounceBtn = contentEl.querySelector('#btn-daily-pronounce');
    dailyPronounceBtn?.addEventListener('click', (e) => {
      e.stopPropagation();
      this.playPronunciation(card.name, dailyPronounceBtn);
    });

    // Original note button
    contentEl.querySelector('#btn-daily-original')?.addEventListener('click', (e) => {
      e.stopPropagation();
      this.openOriginalNoteView(card.path);
    });

    // Status clicks with smooth auto-advance
    contentEl.querySelectorAll('[data-daily-status]').forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.stopPropagation();
        const st = btn.dataset.dailyStatus;
        this.setStatus(card.path, st);
        this.incrementDailyCount();
        this.showToast(st === 'learned' ? '🟢 Got It! Drawing next...' : st === 'learning' ? '🟡 Studying! Drawing next...' : '🔴 Marked for review');
        setTimeout(() => {
          this.renderDailyCard(true);
        }, 320);
      });
    });

    // Reveal toggle
    const wrapper = document.getElementById('daily-card-wrapper');
    wrapper.onclick = (e) => {
      if (e.target.closest('button, .card-status-btn-group')) return;
      this.dailyRevealed = !this.dailyRevealed;
      const blurEl = contentEl.querySelector('.daily-hint-blur');
      if (blurEl) blurEl.classList.toggle('revealed', this.dailyRevealed);
      const cue = contentEl.querySelector('.daily-reveal-btn-cue');
      if (cue) cue.style.display = this.dailyRevealed ? 'none' : 'flex';
    };
  }

  /* ========================================================================
     TAB 4: SETTINGS & TRACKING SYSTEM HUD
     ======================================================================== */

  updateTrackingHUD() {
    let learned = 0;
    let learning = 0;
    let unread = 0;

    const total = 51598; // Pure Vocabulary Vault Total

    const disciplineStats = {
      greek: { learned: 0, total: 17987 },
      latin: { learned: 0, total: 33028 },
      vocab: { learned: 0, total: 583 }
    };

    for (const p in this.statusDb) {
      const st = this.statusDb[p];
      if (st === 'learned') {
        learned++;
        if (p.startsWith('Greek roots/')) disciplineStats.greek.learned++;
        else if (p.startsWith('Latin roots/')) disciplineStats.latin.learned++;
        else if (p.startsWith('English vocabulary master/')) disciplineStats.vocab.learned++;
      } else if (st === 'learning') {
        learning++;
      } else if (st === 'unread') {
        unread++;
      }
    }

    const unreadCalculated = Math.max(0, total - learned - learning);

    const learnedPct = ((learned / total) * 100).toFixed(1);
    const learningPct = ((learning / total) * 100).toFixed(1);
    const unreadPct = Math.max(0, 100 - learnedPct - learningPct);

    // 1. Update Tab 4 (Settings) HUD numbers
    const elLearned = document.getElementById('hud-count-learned');
    const elLearning = document.getElementById('hud-count-learning');
    const elUnread = document.getElementById('hud-count-unread');

    if (elLearned) elLearned.textContent = learned.toLocaleString();
    if (elLearning) elLearning.textContent = learning.toLocaleString();
    if (elUnread) elUnread.textContent = unreadCalculated.toLocaleString();

    // 2. Update Tab 4 (Settings) Segmented Bar
    const segLearned = document.getElementById('hud-seg-learned');
    const segLearning = document.getElementById('hud-seg-learning');
    const segUnread = document.getElementById('hud-seg-unread');

    if (segLearned) segLearned.style.width = `${Math.max(1, learnedPct)}%`;
    if (segLearning) segLearning.style.width = `${Math.max(1, learningPct)}%`;
    if (segUnread) segUnread.style.width = `${unreadPct}%`;

    // 3. Update Tab 1 (Home) Hero Quick Stats
    const homeLearned = document.getElementById('home-stat-learned');
    const homeStudying = document.getElementById('home-stat-studying');
    if (homeLearned) homeLearned.textContent = learned.toLocaleString();
    if (homeStudying) homeStudying.textContent = learning.toLocaleString();

    // 4. Update Tab 1 (Home) Category Card Progress Bars & Counts
    for (const [disc, data] of Object.entries(disciplineStats)) {
      const fillEl = document.getElementById(`prog-fill-${disc}`);
      const textEl = document.getElementById(`prog-text-${disc}`);
      const pct = Math.min(100, (data.learned / data.total) * 100);
      if (fillEl) fillEl.style.width = `${Math.max(data.learned > 0 ? 3 : 0, pct.toFixed(1))}%`;
      if (textEl && data.learned > 0) {
        textEl.textContent = `${data.learned} / ${data.total} (${pct.toFixed(0)}%)`;
      }
    }

    // 5. Update Tab 2 (Cards) Status Filter Chip Badges
    const chipUnread = document.querySelector('#cards-status-chips [data-status="unread"]');
    const chipLearning = document.querySelector('#cards-status-chips [data-status="learning"]');
    const chipLearned = document.querySelector('#cards-status-chips [data-status="learned"]');
    if (chipUnread) chipUnread.textContent = `🔴 Unread (${unreadCalculated > 1000 ? Math.round(unreadCalculated/1000) + 'k' : unreadCalculated})`;
    if (chipLearning) chipLearning.textContent = `🟡 Studying (${learning})`;
    if (chipLearned) chipLearned.textContent = `🟢 Learned (${learned})`;
  }

  applyTheme(theme) {
    this.theme = theme;
    localStorage.setItem('vocab_theme', theme);
    document.documentElement.setAttribute('data-theme', theme);
    document.body.className = `theme-${theme}`;

    // Meta theme-color for iOS/Android status bar
    const metaTheme = document.querySelector('meta[name="theme-color"]');
    if (metaTheme) {
      metaTheme.content = theme === 'light' ? '#F4F1EA' : '#100F0E';
    }

    // Update buttons in settings
    document.querySelectorAll('.theme-pick-card').forEach(card => {
      card.classList.toggle('active', card.dataset.theme === theme);
    });
  }

  applyTypography() {
    localStorage.setItem('vocab_typography', JSON.stringify(this.typography));
    const root = document.documentElement;

    const fontMap = {
      sans: "'Plus Jakarta Sans', 'Manrope', -apple-system, sans-serif",
      serif: "Georgia, 'Times New Roman', serif",
      mono: "'JetBrains Mono', 'Fira Sans', monospace"
    };

    root.style.setProperty('--web-font-sans', fontMap[this.typography.font] || fontMap.sans);
    root.style.setProperty('--web-font-body', fontMap[this.typography.font] || fontMap.sans);
    document.body.style.fontSize = `${this.typography.size}px`;
    document.body.style.lineHeight = String(this.typography.lineHeight);

    // Update settings labels & inputs
    const sizeLbl = document.getElementById('label-font-size');
    const heightLbl = document.getElementById('label-line-height');
    const sizeSlider = document.getElementById('slider-font-size');
    const heightSlider = document.getElementById('slider-line-height');

    if (sizeLbl) sizeLbl.textContent = `${this.typography.size}px`;
    if (heightLbl) heightLbl.textContent = String(this.typography.lineHeight);
    if (sizeSlider) sizeSlider.value = this.typography.size;
    if (heightSlider) heightSlider.value = this.typography.lineHeight;

    document.querySelectorAll('.typo-font-btn').forEach(btn => {
      btn.classList.toggle('active', btn.dataset.font === this.typography.font);
    });
  }

  /* ========================================================================
     GESTURE RECOGNITION (HORIZONTAL SWIPE FOR HOME, VERTICAL FOR FEED)
     ======================================================================== */

  bindTouchGestures() {
    let ignoreSwipe = false;
    let touchStartX = 0;
    let touchStartY = 0;
    let touchStartTime = 0;
    let lastTouchY = 0;
    let lastTouchTime = 0;
    let touchMoved = false;

    // 1. TouchStart — passive listener for optimal scrolling initiation
    document.addEventListener('touchstart', (e) => {
      if (e.touches.length !== 1) {
        ignoreSwipe = true;
        return;
      }

      // Ignore gesture initiation if touching interactive elements or text selection areas
      if (e.target.closest('input, textarea, select, button, a, .apple-c, .card-status-btn, .tiktok-pronounce-btn, .tiktok-original-btn, .filter-chip, .filter-chips-scroll, .table-scroll-wrapper, pre, code')) {
        ignoreSwipe = true;
        return;
      }

      ignoreSwipe = false;
      touchStartX = e.touches[0].clientX;
      touchStartY = e.touches[0].clientY;
      touchStartTime = performance.now();
      lastTouchY = touchStartY;
      lastTouchTime = touchStartTime;
      touchMoved = false;
    }, { passive: true });

    // 2. TouchMove — non-passive listener to prevent scroll bouncing, rubber-banding, and pull-to-refresh jitter
    document.addEventListener('touchmove', (e) => {
      if (ignoreSwipe || e.touches.length !== 1) return;

      const currentX = e.touches[0].clientX;
      const currentY = e.touches[0].clientY;
      const now = performance.now();

      const deltaX = currentX - touchStartX;
      const deltaY = currentY - touchStartY;
      const absX = Math.abs(deltaX);
      const absY = Math.abs(deltaY);

      lastTouchY = currentY;
      lastTouchTime = now;
      touchMoved = true;

      // Text selection guard: don't preventDefault or swipe if user is selecting text
      if (window.getSelection && window.getSelection().toString().trim().length > 0) {
        ignoreSwipe = true;
        return;
      }

      // Vertical swipe on TikTok Feed
      if (this.activeTab === 'cards' && this.cardsViewMode === 'feed') {
        const isVertical = absY > absX && absY > 6;
        if (isVertical) {
          const activeSlide = document.querySelector('#tiktok-feed-wrapper .tiktok-slide');
          if (activeSlide) {
            const isScrollable = activeSlide.scrollHeight - activeSlide.clientHeight > 10;
            const isAtTop = activeSlide.scrollTop <= 4;
            const isAtBottom = activeSlide.scrollTop + activeSlide.clientHeight >= activeSlide.scrollHeight - 6;

            // When card does not scroll internally, or has reached boundary limits,
            // intercepting default scroll eliminates iOS/Android rubber-band bounce and jitter
            if (!isScrollable) {
              if (e.cancelable) e.preventDefault();
            } else if (isAtTop && deltaY > 0) {
              if (e.cancelable) e.preventDefault();
            } else if (isAtBottom && deltaY < 0) {
              if (e.cancelable) e.preventDefault();
            }
            // If inside scrollable quotes/text, allow native momentum scroll
          }
        }
      }
      // Horizontal swipe on Home or Daily Tab: lock vertical wobble during page swipe
      else if ((this.activeTab === 'home' || this.activeTab === 'daily') && absX > absY && absX > 10) {
        if (e.cancelable) e.preventDefault();
      }
    }, { passive: false });

    // 3. TouchEnd — passive listener with robust velocity calculation, flick detection & scroll collision guards
    document.addEventListener('touchend', (e) => {
      if (ignoreSwipe || !touchMoved) return;
      if (e.changedTouches.length !== 1) return;

      // Do NOT trigger slide change if user has selected text
      if (window.getSelection && window.getSelection().toString().trim().length > 0) {
        return;
      }

      const endX = e.changedTouches[0].clientX;
      const endY = e.changedTouches[0].clientY;
      const totalDeltaX = endX - touchStartX;
      const totalDeltaY = endY - touchStartY;
      const absX = Math.abs(totalDeltaX);
      const absY = Math.abs(totalDeltaY);
      const totalElapsed = Math.max(1, performance.now() - touchStartTime);

      // Instantaneous flick velocity & overall swipe velocity (px/ms)
      const overallVelocityY = absY / totalElapsed;
      const recentElapsed = Math.max(1, performance.now() - lastTouchTime);
      const recentDeltaY = Math.abs(endY - lastTouchY);
      const recentVelocityY = recentDeltaY / recentElapsed;
      const velocityY = Math.max(overallVelocityY, recentVelocityY);

      // (1) Horizontal swipe on Home Tab -> navigate subpage stack
      if (this.activeTab === 'home') {
        const isHorizontal = absX > 60 && absX > absY * 1.3 && totalElapsed < 600;
        if (isHorizontal) {
          if (totalDeltaX > 0) {
            this.goBackHome(true);
          } else {
            this.advanceHomeNext();
          }
        }
      }
      // (2) Vertical swipe on Word Cards Feed -> TikTok snap transition
      else if (this.activeTab === 'cards' && this.cardsViewMode === 'feed') {
        const isVerticalDominant = absY > absX * 1.25;
        if (!isVerticalDominant) return;

        const activeSlide = document.querySelector('#tiktok-feed-wrapper .tiktok-slide');
        const isScrollable = activeSlide ? (activeSlide.scrollHeight - activeSlide.clientHeight > 10) : false;
        const isAtTop = activeSlide ? (activeSlide.scrollTop <= 6) : true;
        const isAtBottom = activeSlide ? (activeSlide.scrollTop + activeSlide.clientHeight >= activeSlide.scrollHeight - 8) : true;

        // High velocity flick detection: quick flick with high velocity
        const isFlick = velocityY >= 0.55 && absY >= 40 && totalElapsed < 380;
        // Standard swipe threshold: clear intentional displacement
        const isSwipeThreshold = absY >= 70 && totalElapsed < 700;

        if (totalDeltaY < 0) {
          // SWIPE UP -> Advance to Next Word
          if (isScrollable) {
            // Guard: don't skip quotes if user is just reading through them, unless they are at bottom or do an intentional high-speed flick
            if (isAtBottom && (isSwipeThreshold || isFlick)) {
              this.nextFeedWord();
            } else if (isFlick && velocityY >= 0.85 && absY >= 60) {
              this.nextFeedWord();
            }
          } else {
            if (isFlick || isSwipeThreshold) {
              this.nextFeedWord();
            }
          }
        } else if (totalDeltaY > 0) {
          // SWIPE DOWN -> Return to Previous Word
          if (isScrollable) {
            // Guard: only flip back if user is already at the top of the card (prevents flipping while scrolling quotes back up)
            if (isAtTop && (isSwipeThreshold || isFlick)) {
              this.prevFeedWord();
            }
          } else {
            if (isFlick || isSwipeThreshold) {
              this.prevFeedWord();
            }
          }
        }
      }
      // (3) Horizontal swipe on Daily Word -> draw next random word
      else if (this.activeTab === 'daily') {
        const isHorizontal = absX > 60 && absX > absY * 1.3 && totalElapsed < 600;
        if (isHorizontal && totalDeltaX < 0) {
          this.renderDailyCard(true);
        }
      }
    }, { passive: true });

    // 4. Mouse wheel / trackpad scroll on TikTok Feed
    const feedContainer = document.getElementById('cards-feed-view');
    let lastWheelTime = 0;
    feedContainer?.addEventListener('wheel', (e) => {
      if (this.activeTab !== 'cards' || this.cardsViewMode !== 'feed') return;
      if (Math.abs(e.deltaY) < 25) return;

      const activeSlide = feedContainer.querySelector('.tiktok-slide');
      if (activeSlide) {
        const isScrollable = activeSlide.scrollHeight - activeSlide.clientHeight > 8;
        if (isScrollable) {
          const isAtTop = activeSlide.scrollTop <= 4;
          const isAtBottom = activeSlide.scrollTop + activeSlide.clientHeight >= activeSlide.scrollHeight - 6;
          // Allow native wheel scrolling inside long quotes / citations
          if (e.deltaY > 0 && !isAtBottom) return;
          if (e.deltaY < 0 && !isAtTop) return;
        }
      }

      const now = Date.now();
      if (now - lastWheelTime < 320) return;
      lastWheelTime = now;
      if (e.deltaY > 0) this.nextFeedWord();
      else this.prevFeedWord();
    }, { passive: true });
  }

  /* ========================================================================
     DOM EVENT BINDINGS
     ======================================================================== */

  bindDOMEvents() {
    // 1. Bottom Tab Bar Clicks
    document.querySelectorAll('.mobile-tab-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        const tab = btn.dataset.tab;
        this.switchTab(tab);
      });
    });

    // 2. Top Navigation Bar Back Button
    document.getElementById('top-back-btn')?.addEventListener('click', () => {
      if (this.activeTab === 'home') {
        this.goBackHome();
      }
    });

    // 3. Top Status Badge Click
    document.getElementById('top-status-badge')?.addEventListener('click', () => {
      if (this.activeTab === 'home' && this.homeStack.length > 0) {
        const current = this.homeStack[this.homeStack.length - 1];
        if (current.path) {
          this.cycleStatus(current.path);
        }
      }
    });

    // 4. Scoped Session Unlock Button
    document.getElementById('btn-clear-scope')?.addEventListener('click', () => {
      this.activeScope = null;
      this.feedWordIndex = 0;
      this.applyCardsFilter();
      this.renderFeedCard('none');
      const banner = document.getElementById('cards-scope-banner');
      if (banner) banner.style.display = 'none';
      this.showToast('🔓 Scope unlocked: Showing all vocabulary words');
    });

    // Daily Word Shuffle
    document.getElementById('btn-daily-shuffle')?.addEventListener('click', () => {
      this.renderDailyCard(true);
    });

    // Settings Themes
    document.querySelectorAll('.theme-pick-card').forEach(card => {
      card.addEventListener('click', () => {
        const theme = card.dataset.theme;
        this.applyTheme(theme);
      });
    });

    // Settings Typography
    document.querySelectorAll('.typo-font-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        this.typography.font = btn.dataset.font;
        this.applyTypography();
      });
    });

    document.getElementById('slider-font-size')?.addEventListener('input', (e) => {
      this.typography.size = Number(e.target.value);
      this.applyTypography();
    });

    document.getElementById('slider-line-height')?.addEventListener('input', (e) => {
      this.typography.lineHeight = Number(e.target.value);
      this.applyTypography();
    });

    // Cloud Git Sync
    document.getElementById('btn-sync-now')?.addEventListener('click', async () => {
      this.showToast('Initiating Git sync...');
      try {
        const res = await fetch('/api/sync', { method: 'POST' });
        if (res.ok) {
          const data = await res.json();
          this.showToast(data.message || 'Sync completed successfully');
          await this.loadVaultData();
          this.updateTrackingHUD();
        } else {
          this.showToast('Sync request failed');
        }
      } catch (e) {
        this.showToast('Cloud sync offline');
      }
    });

    // Export Progress
    document.getElementById('btn-export-progress')?.addEventListener('click', () => {
      const dataStr = 'data:text/json;charset=utf-8,' + encodeURIComponent(JSON.stringify(this.statusDb, null, 2));
      const a = document.createElement('a');
      a.setAttribute('href', dataStr);
      a.setAttribute('download', `vocab-progress-${new Date().toISOString().slice(0, 10)}.json`);
      document.body.appendChild(a);
      a.click();
      a.remove();
      this.showToast('Study progress exported');
    });

    // Import Progress
    const fileInput = document.getElementById('file-import-progress');
    document.getElementById('btn-import-progress')?.addEventListener('click', () => {
      fileInput?.click();
    });

    fileInput?.addEventListener('change', (e) => {
      const file = e.target.files?.[0];
      if (!file) return;
      const reader = new FileReader();
      reader.onload = (event) => {
        try {
          const imported = JSON.parse(event.target.result);
          if (typeof imported === 'object' && imported !== null) {
            this.statusDb = { ...this.statusDb, ...imported };
            this.saveStatusDb();
            this.prepareWordCards();
            this.updateTrackingHUD();
            this.showToast('Progress imported successfully');
          }
        } catch {
          this.showToast('Invalid JSON file format');
        }
      };
      reader.readAsText(file);
    });

    // Keyboard Shortcuts (ArrowDown, ArrowUp, Space, PageDown/Up, Status Keys)
    window.addEventListener('keydown', (e) => {
      if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA' || e.target.isContentEditable) return;

      if (this.activeTab === 'cards' && this.cardsViewMode === 'feed') {
        if (e.key === 'ArrowDown' || e.key === 'PageDown' || (e.key === ' ' && !e.shiftKey) || e.key === 'j') {
          e.preventDefault();
          this.nextFeedWord();
        } else if (e.key === 'ArrowUp' || e.key === 'PageUp' || (e.key === ' ' && e.shiftKey) || e.key === 'k') {
          e.preventDefault();
          this.prevFeedWord();
        } else if (e.key === '1') {
          e.preventDefault();
          const card = this.filteredCards[this.feedWordIndex];
          if (card) {
            this.setStatus(card.path, 'unread');
            this.renderFeedCard('none');
          }
        } else if (e.key === '2') {
          e.preventDefault();
          const card = this.filteredCards[this.feedWordIndex];
          if (card) {
            this.setStatus(card.path, 'learning');
            this.renderFeedCard('none');
          }
        } else if (e.key === '3') {
          e.preventDefault();
          const card = this.filteredCards[this.feedWordIndex];
          if (card) {
            this.setStatus(card.path, 'learned');
            this.renderFeedCard('none');
          }
        } else if (e.key.toLowerCase() === 'p') {
          e.preventDefault();
          const card = this.filteredCards[this.feedWordIndex];
          if (card) this.speakWord(card.name);
        } else if (e.key.toLowerCase() === 'o') {
          e.preventDefault();
          const card = this.filteredCards[this.feedWordIndex];
          if (card) this.openOriginalNoteView(card.path);
        }
      } else if (this.activeTab === 'daily') {
        if (e.key === 'ArrowRight' || e.key === 'ArrowDown' || e.key === ' ' || e.key === 'Enter') {
          e.preventDefault();
          this.renderDailyCard(true);
        } else if (e.key.toLowerCase() === 'p') {
          e.preventDefault();
          if (this.dailyCurrentCard) this.speakWord(this.dailyCurrentCard.name);
        }
      }
    });

    document.getElementById('btn-reset-progress')?.addEventListener('click', () => {
      if (confirm('Reset your local vocabulary study progress?')) {
        this.statusDb = {};
        this.saveStatusDb();
        this.updateTrackingHUD();
        this.showToast('Progress reset');
      }
    });

    // Responsive Desktop Window Resize Handler
    window.addEventListener('resize', () => {
      if (this.activeTab === 'cards') {
        this.updateCardsViewMode();
      }
    });
  }

  showToast(msg) {
    const toast = document.getElementById('mobile-toast');
    if (!toast) return;
    toast.textContent = msg;
    toast.classList.add('show');
    clearTimeout(this.toastTimer);
    this.toastTimer = setTimeout(() => {
      toast.classList.remove('show');
    }, 2400);
  }
}

function escapeHtml(str) {
  return String(str ?? '')
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}

function escapeAttr(str) {
  return String(str ?? '').replace(/"/g, '&quot;');
}

// Bootstrap application safely
function bootstrapMobileApp() {
  if (window.mobileVocabApp) return;
  const app = new MobileVocabApp();
  window.mobileVocabApp = app;
  app.init().catch(err => {
    console.error('Fatal initialization error in MobileVocabApp:', err);
  });
}

if (document.readyState === 'loading') {
  window.addEventListener('DOMContentLoaded', bootstrapMobileApp);
} else {
  bootstrapMobileApp();
}
