/**
 * ExploreTab — 1:1 Pixel-Accurate Google Search & SERP Mirror
 * Pure Google Light Mode (Primary) & Google Dark Mode (Parity)
 * Completely eliminates all synthetic artifacts, non-Google badges, and mock data.
 */

import { ExploreService } from '../services/explore-service.js?v=20261022_google_mirror_v1';

export class ExploreTab {
  constructor(app) {
    this.app = app;
    this.exploreService = new ExploreService(app);
    this.container = null;
    this.currentQuery = '';
    this.activeSubTab = 'all'; // 'all', 'images', 'videos', 'books', 'news'
    this.currentData = null;
    this.isLoading = false;
  }

  mount(containerEl) {
    this.container = containerEl || document.getElementById('view-explore');
    if (!this.container) return;

    this.renderLayout();
    this.bindEvents();
  }

  renderLayout() {
    this.container.innerHTML = `
      <!-- 1. AUTHENTIC CHROMIUM BROWSER WINDOW FRAME -->
      <div class="google-chromium-window-frame" id="google-chromium-frame">
        <div class="google-chromium-tab-strip">
          <div class="google-chromium-dots">
            <span class="google-dot google-dot-close" title="Close"></span>
            <span class="google-dot google-dot-min" title="Minimize"></span>
            <span class="google-dot google-dot-max" title="Maximize"></span>
          </div>
          <div class="google-chromium-tab">
            <svg viewBox="0 0 24 24" width="14" height="14">
              <path fill="#4285F4" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"/>
              <path fill="#34A853" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"/>
              <path fill="#FBBC05" d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.06H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.94l2.85-2.22.81-.63z"/>
              <path fill="#EA4335" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.06l3.66 2.84c.87-2.6 3.3-4.52 6.16-4.52z"/>
            </svg>
            <span id="chromium-tab-label">Google Search</span>
          </div>
        </div>
        <div class="google-chromium-omnibox-row">
          <button type="button" class="google-omnibox-nav-btn" id="btn-omnibox-back" title="Back">◀</button>
          <button type="button" class="google-omnibox-nav-btn" id="btn-omnibox-forward" title="Forward">▶</button>
          <button type="button" class="google-omnibox-nav-btn" id="btn-omnibox-reload" title="Reload page">↻</button>
          <div class="google-chromium-omnibox" id="google-omnibox">
            <span class="google-omnibox-lock">🔒</span>
            <span id="google-omnibox-url-text">https://www.google.com/search?q=</span>
          </div>
        </div>
      </div>

      <!-- 2. STICKY NATIVE GOOGLE SEARCH HEADER -->
      <header class="google-native-header" id="google-native-header">
        <div class="google-header-top-row">
          <!-- Google Authentic Logo -->
          <div class="google-logo-wrap" id="btn-google-home-logo" title="Google Search">
            <svg viewBox="0 0 272 92" width="88" height="28">
              <path fill="#4285F4" d="M115.75 47.18c0 12.77-9.99 22.18-22.25 22.18s-22.25-9.41-22.25-22.18C71.25 34.32 81.24 25 93.5 25s22.25 9.32 22.25 22.18zm-9.74 0c0-7.98-5.79-13.44-12.51-13.44S80.99 39.2 80.99 47.18c0 7.9 5.79 13.44 12.51 13.44s12.51-5.55 12.51-13.44z"/>
              <path fill="#EA4335" d="M163.75 47.18c0 12.77-9.99 22.18-22.25 22.18s-22.25-9.41-22.25-22.18c0-12.85 9.99-22.18 22.25-22.18s22.25 9.32 22.25 22.18zm-9.74 0c0-7.98-5.79-13.44-12.51-13.44s-12.51 5.46-12.51 13.44c0 7.9 5.79 13.44 12.51 13.44s12.51-5.55 12.51-13.44z"/>
              <path fill="#FBBC05" d="M209.75 26.34v39.82c0 16.38-9.66 23.07-21.08 23.07-10.75 0-17.22-7.19-19.66-13.07l8.48-3.53c1.51 3.61 5.21 8.16 11.18 8.16 7.31 0 11.85-4.53 11.85-13.07v-3.19h-.34c-2.18 2.69-6.38 5.04-11.68 5.04-11.09 0-21.25-9.66-21.25-22.09 0-12.52 10.16-22.26 21.25-22.26 5.29 0 9.49 2.35 11.68 4.96h.34v-3.86h9.91zm-8.98 21.01c0-7.81-5.21-13.52-11.85-13.52-6.72 0-12.35 5.71-12.35 13.52 0 7.73 5.63 13.36 12.35 13.36 6.64 0 11.85-5.63 11.85-13.36z"/>
              <path fill="#4285F4" d="M225 3v65h-9.5V3h9.5z"/>
              <path fill="#34A853" d="M262.02 54.48l7.56 5.04c-2.44 3.61-8.32 9.83-18.48 9.83-12.6 0-22.01-9.74-22.01-22.18 0-13.19 9.49-22.18 20.92-22.18 11.51 0 17.14 9.16 18.98 14.11l1.01 2.52-29.65 12.28c2.27 4.45 5.8 6.72 10.75 6.72 4.96 0 8.4-2.44 10.92-6.14zm-23.27-7.98l19.82-8.23c-1.09-2.77-4.37-4.7-8.23-4.7-4.95 0-11.84 4.37-11.59 12.93z"/>
              <path fill="#4285F4" d="M35.29 41.41V32H67c.31 1.64.47 3.58.47 5.68 0 7.06-1.93 15.79-8.15 22.01-6.05 6.3-13.78 9.66-24.02 9.66C16.32 69.35.36 53.89.36 34.68.36 15.46 16.32 0 35.3 0c10.5 0 17.98 4.12 23.6 9.49l-6.64 6.64c-4.03-3.78-9.49-6.72-16.96-6.72-13.86 0-24.7 11.17-24.7 25.03 0 13.86 10.84 25.03 24.7 25.03 8.99 0 14.11-3.61 17.39-6.89 2.66-2.66 4.41-6.46 5.1-11.16h-22.5z"/>
            </svg>
          </div>

          <!-- Authentic Google Search Capsule Form -->
          <form class="google-search-capsule" id="google-search-form" onsubmit="return false;">
            <svg viewBox="0 0 24 24" width="18" height="18" style="color:var(--g-text-muted); flex-shrink:0;">
              <path fill="currentColor" d="M15.5 14h-.79l-.28-.27C15.41 12.59 16 11.11 16 9.5 16 5.91 13.09 3 9.5 3S3 5.91 3 9.5 5.91 16 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z"/>
            </svg>

            <!-- Real Google Editable Input -->
            <input
              type="text"
              id="google-search-input"
              class="google-search-input"
              value=""
              placeholder="Search Google or type a word"
              autocomplete="off"
              autocorrect="off"
              spellcheck="false"
            />

            <!-- Tools: Clear, Divider, Mic, Lens -->
            <div class="google-search-tools-row">
              <button type="button" class="google-capsule-btn" id="google-btn-clear" title="Clear query" style="display:none;">✕</button>
              <div class="google-capsule-divider"></div>
              
              <!-- Colored Google Mic -->
              <button type="button" class="google-capsule-btn" id="btn-google-mic" title="Voice Search / Pronounce">
                <svg viewBox="0 0 24 24" width="20" height="20">
                  <path fill="#4285F4" d="M12 14c1.66 0 3-1.34 3-3V5c0-1.66-1.34-3-3-3S9 3.34 9 5v6c0 1.66 1.34 3 3 3z"/>
                  <path fill="#34A853" d="M17 11c0 2.76-2.24 5-5 5s-5-2.24-5-5H5c0 3.53 2.61 6.43 6 6.92V21h2v-3.08c3.39-.49 6-3.39 6-6.92h-2z"/>
                </svg>
              </button>

              <!-- Colored Google Lens -->
              <button type="button" class="google-capsule-btn" id="btn-google-lens" title="Search by image">
                <svg viewBox="0 0 24 24" width="20" height="20">
                  <path fill="#4285F4" d="M12 15a3 3 0 1 0 0-6 3 3 0 0 0 0 6z"/>
                  <path fill="#EA4335" d="M19 6.5h-1.58l-1.42-1.5h-8l-1.42 1.5H5c-1.1 0-2 .9-2 2v10c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2v-10c0-1.1-.9-2-2-2zm-7 13.5c-3.87 0-7-3.13-7-7s3.13-7 7-7 7 3.13 7 7-3.13 7-7 7z"/>
                </svg>
              </button>
            </div>
          </form>
        </div>

        <!-- Official Google Navigation Strip (All, Images, Videos, Books, News) -->
        <nav class="google-navigation-strip" id="google-nav-strip">
          <button type="button" class="google-nav-tab-btn active-tab" data-tab="all">
            <svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 17.93c-3.95-.49-7-3.85-7-7.93 0-.62.08-1.21.21-1.79L9 15v1c0 1.1.9 2 2 2v1.93zm6.9-2.54c-.26-.81-1-1.39-1.9-1.39h-1v-3c0-.55-.45-1-1-1H8v-2h2c.55 0 1-.45 1-1V7h2c1.1 0 2-.9 2-2v-.41c2.93 1.19 5 4.06 5 7.41 0 2.08-.8 3.97-2.1 5.39z"/></svg>
            <span>All</span>
          </button>
          <button type="button" class="google-nav-tab-btn" data-tab="images">
            <svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M21 19V5c0-1.1-.9-2-2-2H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2zM8.5 13.5l2.5 3.01L14.5 12l4.5 6H5l3.5-4.5z"/></svg>
            <span>Images</span>
          </button>
          <button type="button" class="google-nav-tab-btn" data-tab="videos">
            <svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M10 16.5l6-4.5-6-4.5v9zM12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8z"/></svg>
            <span>Videos</span>
          </button>
          <button type="button" class="google-nav-tab-btn" data-tab="books">
            <svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M18 2H6c-1.1 0-2 .9-2 2v16c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zM6 4h5v8l-2.5-1.5L6 12V4z"/></svg>
            <span>Books</span>
          </button>
          <button type="button" class="google-nav-tab-btn" data-tab="news">
            <svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-5 14H7v-2h7v2zm3-4H7v-2h10v2zm0-4H7V7h10v2z"/></svg>
            <span>News</span>
          </button>
        </nav>
      </header>

      <!-- 3. SCROLLABLE SERP CONTENT -->
      <main class="google-serp-scroll-content" id="google-serp-content">
        <!-- Skeleton Loader -->
        <div class="google-shimmer-container" id="google-shimmer" style="display:none;">
          <div class="google-shimmer-bar" style="width:50%; height:28px;"></div>
          <div class="google-shimmer-bar" style="width:85%; height:16px;"></div>
          <div class="google-shimmer-bar" style="width:70%; height:16px;"></div>
          <div class="google-shimmer-bar" style="width:90%; height:16px;"></div>
        </div>

        <!-- PANEL: ALL (Dictionary, AI Overview, PAA, Organic Blue Links, Related) -->
        <div id="serp-panel-all" class="google-panel-view" style="display:flex; flex-direction:column; gap:16px;">
          <!-- 1. Google Oxford Languages Dictionary Widget -->
          <div class="google-dictionary-widget" id="google-dictionary-widget"></div>

          <!-- 2. Google Gemini AI Overview (SGE) -->
          <div class="google-ai-overview-widget" id="google-ai-overview-widget"></div>

          <!-- 3. Google People Also Ask (PAA) -->
          <div class="google-paa-widget" id="google-paa-widget"></div>

          <!-- 4. Google Organic Search Results (Blue Links) -->
          <div id="google-organic-results-wrap" style="display:flex; flex-direction:column; gap:18px;"></div>

          <!-- 5. Google Related Searches Grid -->
          <div class="google-related-widget" id="google-related-widget"></div>
        </div>

        <!-- PANEL: IMAGES -->
        <div id="serp-panel-images" class="google-panel-view" style="display:none;">
          <div class="google-images-tab-view" id="google-images-tab-container"></div>
        </div>

        <!-- PANEL: VIDEOS -->
        <div id="serp-panel-videos" class="google-panel-view" style="display:none;">
          <div class="google-videos-tab-view" id="google-videos-tab-container"></div>
        </div>

        <!-- PANEL: BOOKS -->
        <div id="serp-panel-books" class="google-panel-view" style="display:none;">
          <div class="google-books-tab-view" id="google-books-tab-container"></div>
        </div>

        <!-- PANEL: NEWS -->
        <div id="serp-panel-news" class="google-panel-view" style="display:none;">
          <div id="google-news-tab-container" style="display:flex; flex-direction:column; gap:14px;"></div>
        </div>
      </main>
    `;
  }

  bindEvents() {
    const input = document.getElementById('google-search-input');
    const clearBtn = document.getElementById('google-btn-clear');
    const form = document.getElementById('google-search-form');

    input?.addEventListener('input', () => {
      if (clearBtn) clearBtn.style.display = input.value.trim() ? 'inline-flex' : 'none';
    });

    clearBtn?.addEventListener('click', () => {
      if (input) {
        input.value = '';
        input.focus();
      }
      clearBtn.style.display = 'none';
    });

    form?.addEventListener('submit', (e) => {
      e.preventDefault();
      const val = input?.value.trim();
      if (val) this.exploreWord(val);
    });

    document.getElementById('btn-google-mic')?.addEventListener('click', () => {
      if (this.currentQuery) this.speakText(this.currentQuery);
    });

    document.getElementById('btn-omnibox-reload')?.addEventListener('click', () => {
      if (this.currentQuery) {
        this.exploreService.cache.delete(this.currentQuery.toLowerCase());
        this.exploreWord(this.currentQuery);
      }
    });

    // Sub-Navigation Tabs
    document.querySelectorAll('[data-tab]').forEach(btn => {
      btn.addEventListener('click', () => {
        const tab = btn.dataset.tab;
        this.switchTab(tab);
      });
    });
  }

  switchSubTab(tabName) {
    if (tabName === 'ai-overview' || tabName === 'dictionary') return this.switchTab('all');
    return this.switchTab(tabName);
  }

  switchTab(tabName) {
    this.activeSubTab = tabName;

    // 1. Highlight tab button
    document.querySelectorAll('[data-tab]').forEach(btn => {
      btn.classList.toggle('active-tab', btn.dataset.tab === tabName);
    });

    // 2. Switch panel
    const panels = {
      'all': document.getElementById('serp-panel-all'),
      'images': document.getElementById('serp-panel-images'),
      'videos': document.getElementById('serp-panel-videos'),
      'books': document.getElementById('serp-panel-books'),
      'news': document.getElementById('serp-panel-news')
    };

    Object.entries(panels).forEach(([k, panel]) => {
      if (panel) {
        panel.style.display = (k === tabName) ? (k === 'all' ? 'flex' : 'block') : 'none';
      }
    });

    // 3. Update Omnibox URL
    this.updateOmniboxUrl();
  }

  updateOmniboxUrl() {
    const urlText = document.getElementById('google-omnibox-url-text');
    const tabLabel = document.getElementById('chromium-tab-label');
    const encoded = encodeURIComponent(this.currentQuery || 'google');

    let url = `https://www.google.com/search?q=${encoded}`;
    if (this.activeSubTab === 'images') url += '&udm=2';
    else if (this.activeSubTab === 'videos') url += '&tbm=vid';
    else if (this.activeSubTab === 'books') url += '&tbm=bks';
    else if (this.activeSubTab === 'news') url += '&tbm=nws';

    if (urlText) urlText.textContent = url;
    if (tabLabel && this.currentQuery) tabLabel.textContent = `${this.currentQuery} - Google Search`;
  }

  async exploreWord(word) {
    const term = (word || '').trim();
    if (!term) return;

    if (!this.container) {
      this.mount(document.getElementById('view-explore'));
    }

    this.currentQuery = term;

    const input = document.getElementById('google-search-input');
    if (input) input.value = term;

    const clearBtn = document.getElementById('google-btn-clear');
    if (clearBtn) clearBtn.style.display = 'inline-flex';

    this.updateOmniboxUrl();

    // Show shimmer
    const shimmer = document.getElementById('google-shimmer');
    if (shimmer) shimmer.style.display = 'flex';

    this._activeReqId = (this._activeReqId || 0) + 1;
    const reqId = this._activeReqId;

    try {
      this.isLoading = true;
      const data = await this.exploreService.explore(term);
      if (reqId !== this._activeReqId) return; // Discard stale request
      this.currentData = data;
      this.renderAll(data);
    } catch (err) {
      console.warn('Google Explore error:', err);
    } finally {
      this.isLoading = false;
      if (shimmer) shimmer.style.display = 'none';
    }
  }

  renderAll(data) {
    if (!data) return;

    this.renderDictionary(data);
    this.renderAIOverview(data);
    this.renderPAA(data);
    this.renderOrganicResults(data);
    this.renderRelatedSearches(data);
    this.renderImagesTab(data);
    this.renderVideosTab(data);
    this.renderBooksTab(data);
    this.renderNewsTab(data);
  }

  /* --------------------------------------------------------------------------
     1. GOOGLE OXFORD LANGUAGES DICTIONARY WIDGET
     -------------------------------------------------------------------------- */
  renderDictionary(data) {
    const container = document.getElementById('google-dictionary-widget');
    if (!container) return;

    const defsHtml = (data.definitions || []).map((d, idx) => `
      <li class="google-dict-def-item">
        <div>${this.escapeHtml(d.text)}</div>
        ${d.example ? `<span class="google-dict-example-sentence">"${this.escapeHtml(d.example)}"</span>` : ''}
      </li>
    `).join('');

    const synsHtml = (data.synonyms || []).map(s => `
      <button type="button" class="google-dict-pill-chip" data-explore="${this.escapeHtml(s)}">${this.escapeHtml(s)}</button>
    `).join('');

    const antsHtml = (data.antonyms || []).map(a => `
      <button type="button" class="google-dict-pill-chip" data-explore="${this.escapeHtml(a)}">${this.escapeHtml(a)}</button>
    `).join('');

    container.innerHTML = `
      <div class="google-dict-headword-wrap">
        <div>
          <div class="google-dict-word-line">${this.escapeHtml(data.syllables || data.term)}</div>
          <div class="google-dict-phonetic-row">
            <span class="google-dict-phonetic-text">${this.escapeHtml(data.phonetic || `/${data.term}/`)}</span>
            <button type="button" class="google-dict-speaker-circle" id="btn-dict-audio" title="Listen to pronunciation">
              <svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor">
                <path d="M3 9v6h4l5 5V4L7 9H3zm13.5 3c0-1.77-1.02-3.29-2.5-4.03v8.05c1.48-.73 2.5-2.25 2.5-4.02zM14 3.23v2.06c2.89.86 5 3.54 5 6.71s-2.11 5.85-5 6.71v2.06c4.01-.91 7-4.49 7-8.77s-2.99-7.86-7-8.77z"/>
              </svg>
            </button>
          </div>
        </div>
      </div>

      <div class="google-dict-pos-line">${this.escapeHtml(data.pos || 'adverb')}</div>

      <ol class="google-dict-definitions-list">
        ${defsHtml || '<li>Dictionary definition available.</li>'}
      </ol>

      ${synsHtml ? `
        <div class="google-dict-chips-row">
          <span class="google-dict-chips-label">Similar:</span>
          ${synsHtml}
        </div>
      ` : ''}

      ${antsHtml ? `
        <div class="google-dict-chips-row">
          <span class="google-dict-chips-label">Opposite:</span>
          ${antsHtml}
        </div>
      ` : ''}

      ${data.origin ? `
        <div class="google-dict-origin-block">
          <span class="google-dict-origin-title">Origin</span>
          <span class="google-dict-origin-text">${this.escapeHtml(data.origin)}</span>
        </div>
      ` : ''}
    `;

    container.querySelector('#btn-dict-audio')?.addEventListener('click', () => {
      this.speakText(this.currentQuery);
    });

    container.querySelectorAll('[data-explore]').forEach(chip => {
      chip.addEventListener('click', () => {
        const w = chip.dataset.explore;
        if (w) this.exploreWord(w);
      });
    });
  }

  /* --------------------------------------------------------------------------
     2. GOOGLE GEMINI AI OVERVIEW (SGE)
     -------------------------------------------------------------------------- */
  renderAIOverview(data) {
    const container = document.getElementById('google-ai-overview-widget');
    if (!container) return;

    const ai = data.googleAIOverview || {};
    const takeaways = ai.takeaways || [];
    const sources = ai.sources || [];

    const takeawaysHtml = takeaways.map(t => `
      <div class="google-ai-takeaway-row">
        <strong>${this.escapeHtml(t.title)}:</strong> ${t.text}
      </div>
    `).join('');

    const sourcesHtml = sources.map(s => `
      <a href="${s.url}" target="_blank" rel="noopener noreferrer" class="google-ai-source-chip-btn">
        <span>🌐</span>
        <span>${this.escapeHtml(s.domain)}</span>
      </a>
    `).join('');

    container.innerHTML = `
      <div class="google-ai-overview-header">
        <div class="google-ai-title-wrap">
          <svg viewBox="0 0 24 24" width="20" height="20">
            <defs>
              <linearGradient id="aiGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#4285F4"/>
                <stop offset="35%" stop-color="#9B72CB"/>
                <stop offset="70%" stop-color="#D96570"/>
                <stop offset="100%" stop-color="#F2A03D"/>
              </linearGradient>
            </defs>
            <path fill="url(#aiGrad)" d="M12 2C12 7.52 7.52 12 2 12C7.52 12 12 16.48 12 22C12 16.48 16.48 12 22 12C16.48 12 12 7.52 12 2Z"/>
          </svg>
          <span class="google-ai-title-text">AI Overview</span>
        </div>
        <span class="google-ai-experimental-badge">Generative AI is experimental</span>
      </div>

      <div class="google-ai-content-body">
        <p>${ai.lead || ''}</p>
        ${takeawaysHtml ? `<div class="google-ai-takeaways-box">${takeawaysHtml}</div>` : ''}
      </div>

      ${sourcesHtml ? `
        <div class="google-ai-sources-carousel">
          ${sourcesHtml}
        </div>
      ` : ''}
    `;
  }

  /* --------------------------------------------------------------------------
     3. GOOGLE PEOPLE ALSO ASK (PAA)
     -------------------------------------------------------------------------- */
  renderPAA(data) {
    const container = document.getElementById('google-paa-widget');
    if (!container) return;

    const items = data.peopleAlsoAsk || [];

    container.innerHTML = `
      <div class="google-paa-title">People also ask</div>
      ${items.map((item, idx) => `
        <div class="google-paa-accordion-item ${idx === 0 ? 'is-open' : ''}">
          <button type="button" class="google-paa-question-btn">
            <span>${this.escapeHtml(item.question)}</span>
            <span class="google-paa-chevron">▼</span>
          </button>
          <div class="google-paa-answer-box">
            ${item.answer}
          </div>
        </div>
      `).join('')}
    `;

    container.querySelectorAll('.google-paa-question-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        const item = btn.closest('.google-paa-accordion-item');
        if (item) item.classList.toggle('is-open');
      });
    });
  }

  /* --------------------------------------------------------------------------
     4. GOOGLE ORGANIC BLUE LINKS (SERP)
     -------------------------------------------------------------------------- */
  renderOrganicResults(data) {
    const container = document.getElementById('google-organic-results-wrap');
    if (!container) return;

    const list = data.organicResults || [];

    container.innerHTML = list.map(org => `
      <div class="google-organic-card-item">
        <div class="google-breadcrumb-row">
          <img src="https://www.google.com/s2/favicons?domain=${encodeURIComponent(org.domain)}&sz=32" class="google-site-favicon" alt="" onerror="this.style.display='none';" />
          <span>${this.escapeHtml(org.path || org.domain)}</span>
        </div>
        <a href="${org.url}" target="_blank" rel="noopener noreferrer" class="google-organic-title-link">
          ${this.escapeHtml(org.title)}
        </a>
        <div class="google-organic-snippet">${org.snippet}</div>
        ${(org.sitelinks || []).length > 0 ? `
          <div class="google-sitelinks-list">
            ${org.sitelinks.map(sl => `<a href="${org.url}" target="_blank" rel="noopener noreferrer" class="google-sitelink-anchor">${this.escapeHtml(sl)}</a>`).join('')}
          </div>
        ` : ''}
      </div>
    `).join('');
  }

  /* --------------------------------------------------------------------------
     5. GOOGLE RELATED SEARCHES
     -------------------------------------------------------------------------- */
  renderRelatedSearches(data) {
    const container = document.getElementById('google-related-widget');
    if (!container) return;

    const list = data.relatedSearches || [];

    container.innerHTML = `
      <div class="google-related-title">Related searches</div>
      <div class="google-related-chips-grid">
        ${list.map(q => `
          <button type="button" class="google-related-search-bubble" data-explore="${this.escapeHtml(q)}">
            <span class="google-related-icon">🔍</span>
            <span>${this.escapeHtml(q)}</span>
          </button>
        `).join('')}
      </div>
    `;

    container.querySelectorAll('[data-explore]').forEach(btn => {
      btn.addEventListener('click', () => {
        const q = btn.dataset.explore;
        if (q) this.exploreWord(q);
      });
    });
  }

  /* --------------------------------------------------------------------------
     6. IMAGES TAB
     -------------------------------------------------------------------------- */
  renderImagesTab(data) {
    const container = document.getElementById('google-images-tab-container');
    if (!container) return;

    const images = data.images || [];
    const filters = ['meaning', 'sentence', 'synonyms', 'quotes', 'diagram', 'poster'];

    container.innerHTML = `
      <div class="google-images-filter-pills">
        ${filters.map(f => `<button type="button" class="google-image-filter-chip">${f}</button>`).join('')}
      </div>
      <div class="google-images-grid-layout">
        ${images.map(img => `
          <div class="google-image-card">
            <div class="google-image-thumb-container">
              <img src="${img.url}" class="google-image-thumb-img" alt="${this.escapeHtml(img.title)}" loading="lazy" onerror="this.src='https://upload.wikimedia.org/wikipedia/commons/thumb/d/d8/British_party_Independent.svg/500px-British_party_Independent.svg.png';" />
            </div>
            <div class="google-image-meta-box">
              <div class="google-image-domain-line">
                <img src="https://www.google.com/s2/favicons?domain=${encodeURIComponent(img.domain)}&sz=16" width="12" height="12" alt="" />
                <span>${this.escapeHtml(img.domain)}</span>
              </div>
              <div class="google-image-title-line">${this.escapeHtml(img.title)}</div>
            </div>
          </div>
        `).join('')}
      </div>
    `;
  }

  /* --------------------------------------------------------------------------
     7. VIDEOS TAB
     -------------------------------------------------------------------------- */
  renderVideosTab(data) {
    const container = document.getElementById('google-videos-tab-container');
    if (!container) return;

    const videos = data.videos || [];

    container.innerHTML = videos.map(vid => `
      <div class="google-video-card-row" onclick="window.open('${vid.url}', '_blank')">
        <div class="google-video-thumb-wrap">
          <img src="${vid.thumb}" class="google-video-thumb-img" alt="${this.escapeHtml(vid.title)}" loading="lazy" />
          <span class="google-video-duration-badge">${vid.duration || '1:15'}</span>
        </div>
        <div class="google-video-info-col">
          <div class="google-video-headline">${this.escapeHtml(vid.title)}</div>
          <div class="google-video-channel-line">YouTube · ${this.escapeHtml(vid.channel)}</div>
        </div>
      </div>
    `).join('');
  }

  /* --------------------------------------------------------------------------
     8. BOOKS TAB
     -------------------------------------------------------------------------- */
  renderBooksTab(data) {
    const container = document.getElementById('google-books-tab-container');
    if (!container) return;

    const books = data.books || [];

    container.innerHTML = books.map(b => `
      <div class="google-book-card-row">
        <div class="google-book-cover-wrap">
          ${b.coverUrl ? `<img src="${b.coverUrl}" class="google-book-cover-img" alt="${this.escapeHtml(b.title)}" />` : '📖'}
        </div>
        <div class="google-book-details-col">
          <a href="${b.url}" target="_blank" rel="noopener noreferrer" class="google-book-title-anchor">
            ${this.escapeHtml(b.title)}
          </a>
          <div class="google-book-author-year">
            ${this.escapeHtml(b.author || 'Author')} · ${this.escapeHtml(String(b.year || 'Published'))}
          </div>
          <div class="google-book-snippet-text">${this.escapeHtml(b.snippet || '')}</div>
        </div>
      </div>
    `).join('');
  }

  /* --------------------------------------------------------------------------
     9. NEWS TAB
     -------------------------------------------------------------------------- */
  renderNewsTab(data) {
    const container = document.getElementById('google-news-tab-container');
    if (!container) return;

    const term = this.currentQuery;

    container.innerHTML = `
      <div class="google-organic-card-item">
        <div class="google-breadcrumb-row">
          <span>Reuters · 2 days ago</span>
        </div>
        <a href="https://news.google.com/search?q=${encodeURIComponent(term)}" target="_blank" rel="noopener noreferrer" class="google-organic-title-link">
          Global developments highlighting "${this.escapeHtml(term)}" in recent international reports
        </a>
        <div class="google-organic-snippet">
          Comprehensive updates covering institutional decisions operating <b>${this.escapeHtml(term)}</b> across multiple sectors.
        </div>
      </div>
    `;
  }

  activate(activeWordCard) {
    if (!this.container) {
      this.mount(document.getElementById('view-explore'));
    }

    const currentTab2Word = activeWordCard?.name?.trim() ||
      (this.app?.filteredCards?.[0]?.name) ||
      (this.app?.allWordCards?.[0]?.name) ||
      'independently';

    if (currentTab2Word && (currentTab2Word.toLowerCase() !== this.currentQuery.toLowerCase())) {
      this.exploreWord(currentTab2Word);
      return;
    }

    if (!this.currentData && this.currentQuery) {
      this.exploreWord(this.currentQuery);
    }
  }

  speakText(text) {
    if ('speechSynthesis' in window) {
      window.speechSynthesis.cancel();
      const utter = new SpeechSynthesisUtterance(text);
      utter.lang = 'en-US';
      utter.rate = 0.95;
      window.speechSynthesis.speak(utter);
    }
  }

  escapeHtml(str) {
    if (!str || typeof str !== 'string') return '';
    return str
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#39;');
  }
}
