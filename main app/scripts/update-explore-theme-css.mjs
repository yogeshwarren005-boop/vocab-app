import fs from 'fs';

const newCss = `/* ==========================================================================
   GOOGLE CHROME SERP & GEMINI AI OVERVIEW EXPLORE TAB STYLES
   Authentic Dual-Theme Architecture: Volcanic Dark SERP & Scandinavian Light SERP
   ========================================================================== */

/* --------------------------------------------------------------------------
   THEME PALETTE SYSTEM (DARK & LIGHT MODE SYNCHRONIZATION)
   -------------------------------------------------------------------------- */
#view-explore,
.theme-dark #view-explore,
[data-theme="dark"] #view-explore {
  --google-bg: #202124;
  --google-header-bg: #202124;
  --google-card-bg: #303134;
  --google-card-bg-elevated: #3c4043;
  --google-border: #3c4043;
  --google-border-subtle: rgba(255, 255, 255, 0.08);
  --google-text-primary: #e8eaed;
  --google-text-secondary: #bdc1c6;
  --google-text-muted: #9aa0a6;
  --google-link: #8ab4f8;
  --google-link-hover: #aecbfa;
  --google-search-bg: #303134;
  --google-search-border: #5f6368;
  --google-search-focus: #8ab4f8;
  --google-ai-bg: radial-gradient(100% 100% at 0% 0%, rgba(66, 133, 244, 0.22) 0%, rgba(147, 51, 234, 0.14) 45%, #202124 100%);
  --google-ai-border: rgba(138, 180, 248, 0.45);
  --google-ai-box: rgba(66, 133, 244, 0.12);
  --google-ai-box-border: rgba(138, 180, 248, 0.22);
  --google-chip-bg: #303134;
  --google-chip-border: #3c4043;
  --google-chip-hover: #3c4043;
  --google-chip-text: #e8eaed;
  --google-tab-text: #9aa0a6;
  --google-tab-active-text: #8ab4f8;
  --google-tab-active-bg: rgba(138, 180, 248, 0.14);
  --google-tab-active-bar: #8ab4f8;
  --google-shimmer-bg: #303134;
  --google-shimmer-wave: rgba(255, 255, 255, 0.08);
  --google-card-shadow: 0 1px 6px rgba(0, 0, 0, 0.35);
  --google-pill-border: rgba(255, 255, 255, 0.12);
}

.theme-light #view-explore,
[data-theme="light"] #view-explore {
  --google-bg: #ffffff;
  --google-header-bg: #ffffff;
  --google-card-bg: #ffffff;
  --google-card-bg-elevated: #f8f9fa;
  --google-border: #dadce0;
  --google-border-subtle: #ebebeb;
  --google-text-primary: #202124;
  --google-text-secondary: #4d5156;
  --google-text-muted: #70757a;
  --google-link: #1a0dab;
  --google-link-hover: #174ea6;
  --google-search-bg: #ffffff;
  --google-search-border: #dfe1e5;
  --google-search-focus: #1a73e8;
  --google-ai-bg: linear-gradient(135deg, rgba(232, 240, 254, 0.85) 0%, rgba(243, 232, 255, 0.6) 45%, #ffffff 100%);
  --google-ai-border: rgba(66, 133, 244, 0.35);
  --google-ai-box: rgba(66, 133, 244, 0.07);
  --google-ai-box-border: rgba(66, 133, 244, 0.18);
  --google-chip-bg: #f1f3f4;
  --google-chip-border: #dadce0;
  --google-chip-hover: #e8eaed;
  --google-chip-text: #3c4043;
  --google-tab-text: #5f6368;
  --google-tab-active-text: #1a73e8;
  --google-tab-active-bg: rgba(26, 115, 232, 0.1);
  --google-tab-active-bar: #1a73e8;
  --google-shimmer-bg: #e8eaed;
  --google-shimmer-wave: rgba(255, 255, 255, 0.6);
  --google-card-shadow: 0 1px 6px rgba(32, 33, 36, 0.12);
  --google-pill-border: rgba(0, 0, 0, 0.1);
}

/* --------------------------------------------------------------------------
   VIEW CONTAINER
   -------------------------------------------------------------------------- */
#view-explore {
  display: none;
  flex-direction: column;
  height: 100%;
  width: 100%;
  position: relative;
  overflow: hidden;
  background-color: var(--google-bg);
  color: var(--google-text-primary);
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Google Sans", sans-serif;
  -webkit-font-smoothing: antialiased;
  transition: background-color 0.25s ease, color 0.25s ease;
}

#view-explore.is-active-tab {
  display: flex !important;
}

/* --------------------------------------------------------------------------
   1. STICKY TOP GOOGLE CHROME SEARCH HEADER
   -------------------------------------------------------------------------- */
.google-chrome-header {
  position: sticky;
  top: 0;
  z-index: 50;
  background-color: var(--google-header-bg);
  border-bottom: 1px solid var(--google-border);
  padding: 8px 12px 6px 12px;
  display: flex;
  flex-direction: column;
  gap: 8px;
  box-shadow: var(--google-card-shadow);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  flex-shrink: 0;
  transition: background-color 0.25s ease, border-color 0.25s ease;
}

.google-brand-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 2px 4px 0 4px;
}

/* Authentic Google Colorful Logo */
.google-logo-text {
  font-family: 'Google Sans', 'Product Sans', 'Roboto', sans-serif;
  font-size: 22px;
  font-weight: 700;
  letter-spacing: -0.5px;
  user-select: none;
  display: inline-flex;
  align-items: center;
}

.google-logo-text .g-blue { color: #4285F4; }
.google-logo-text .g-red { color: #EA4335; }
.google-logo-text .g-yellow { color: #FBBC05; }
.google-logo-text .g-green { color: #34A853; }

.google-account-pill {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  background: var(--google-chip-bg);
  border: 1px solid var(--google-border);
  padding: 3px 8px;
  border-radius: 9999px;
  font-size: 11px;
  font-weight: 600;
  color: var(--google-text-secondary);
}

.google-live-toolbar-actions {
  display: flex;
  align-items: center;
  gap: 6px;
}

.google-live-tool-btn {
  background: var(--google-chip-bg);
  border: 1px solid var(--google-border);
  color: var(--google-text-secondary);
  font-size: 11px;
  font-weight: 600;
  padding: 4px 9px;
  border-radius: 9999px;
  display: inline-flex;
  align-items: center;
  gap: 4px;
  text-decoration: none;
  cursor: pointer;
  transition: all 0.15s ease;
}

.google-live-tool-btn:hover {
  background: var(--google-chip-hover);
  color: var(--google-text-primary);
  border-color: var(--google-link);
}

/* Pinned Google Search Capsule */
.google-search-capsule-form {
  background: var(--google-search-bg);
  border: 1px solid var(--google-search-border);
  border-radius: 9999px;
  display: flex;
  align-items: center;
  padding: 5px 12px;
  gap: 8px;
  transition: all 0.2s ease;
  box-shadow: 0 1px 4px rgba(0, 0, 0, 0.12);
}

.google-search-capsule-form:focus-within {
  border-color: var(--google-search-focus);
  box-shadow: 0 0 0 1px var(--google-search-focus), 0 2px 8px rgba(0, 0, 0, 0.18);
}

.google-search-lens-icon {
  font-size: 13px;
  color: var(--google-text-muted);
  flex-shrink: 0;
}

/* THE LOCKED WORD TOKEN: Anchor that cannot be removed */
.google-locked-word-token {
  background: rgba(16, 185, 129, 0.14);
  border: 1px solid rgba(16, 185, 129, 0.4);
  color: #10B981;
  padding: 3px 9px;
  border-radius: 9999px;
  font-size: 12px;
  font-weight: 700;
  display: inline-flex;
  align-items: center;
  gap: 4px;
  white-space: nowrap;
  user-select: none;
  flex-shrink: 0;
  cursor: default;
  transition: transform 0.15s ease;
}

.google-locked-word-token.shake {
  animation: tokenShake 0.4s ease;
}

@keyframes tokenShake {
  0%, 100% { transform: translateX(0); }
  20%, 60% { transform: translateX(-4px); }
  40%, 80% { transform: translateX(4px); }
}

/* Modifier input */
.google-search-modifier-input {
  flex: 1;
  background: transparent;
  border: none;
  outline: none;
  font-size: 13.5px;
  color: var(--google-text-primary);
  font-family: inherit;
  min-width: 0;
}

.google-search-modifier-input::placeholder {
  color: var(--google-text-muted);
}

.google-search-tools {
  display: flex;
  align-items: center;
  gap: 4px;
  flex-shrink: 0;
}

.google-btn-clear {
  background: transparent;
  border: none;
  color: var(--google-text-muted);
  font-size: 12px;
  cursor: pointer;
  padding: 2px 4px;
  border-radius: 50%;
  display: inline-flex;
  align-items: center;
  justify-content: center;
}

.google-btn-clear:hover {
  color: var(--google-text-primary);
}

.google-tool-icon {
  background: transparent;
  border: none;
  font-size: 14px;
  cursor: pointer;
  padding: 3px;
  border-radius: 50%;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  transition: transform 0.12s ease;
}

.google-tool-icon:active {
  transform: scale(0.9);
}

.google-search-submit-btn {
  background: #1a73e8;
  color: #fff;
  border: none;
  padding: 4px 10px;
  border-radius: 9999px;
  font-size: 11px;
  font-weight: 600;
  cursor: pointer;
  transition: background 0.15s ease;
}

.google-search-submit-btn:hover {
  background: #1557b0;
}

/* Native Google Sub-Tabs Navigation */
.google-serp-nav-tabs {
  display: flex;
  gap: 4px;
  overflow-x: auto;
  scrollbar-width: none;
  padding: 2px 0 0 0;
  border-top: 1px solid var(--google-border-subtle);
}

.google-serp-nav-tabs::-webkit-scrollbar {
  display: none;
}

.google-nav-tab {
  background: transparent;
  border: none;
  padding: 6px 10px;
  font-size: 12px;
  font-weight: 600;
  color: var(--google-tab-text);
  border-radius: 9999px;
  cursor: pointer;
  white-space: nowrap;
  display: inline-flex;
  align-items: center;
  gap: 4px;
  position: relative;
  transition: all 0.15s ease;
}

.google-nav-tab:hover {
  color: var(--google-text-primary);
  background: var(--google-tab-active-bg);
}

.google-nav-tab.active {
  color: var(--google-tab-active-text);
  background: var(--google-tab-active-bg);
  font-weight: 700;
}

.google-nav-tab.active::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 12px;
  right: 12px;
  height: 2.5px;
  background: var(--google-tab-active-bar);
  border-radius: 2px;
}

/* --------------------------------------------------------------------------
   2. CONTENT CONTAINER & PANEL ARCHITECTURE
   -------------------------------------------------------------------------- */
.explore-content-container {
  flex: 1;
  overflow-y: auto;
  -webkit-overflow-scrolling: touch;
  padding: 12px 14px 80px 14px;
  background-color: var(--google-bg);
  display: block;
  transition: background-color 0.25s ease;
}

.explore-panel {
  display: none;
  flex-direction: column;
  gap: 12px;
  opacity: 0;
  transition: opacity 0.18s ease;
}

.explore-panel.is-active-panel {
  display: flex;
  opacity: 1;
}

/* Shimmer Loading Card */
.google-shimmer-card {
  background: var(--google-card-bg);
  border: 1px solid var(--google-border);
  border-radius: 18px;
  padding: 16px;
  display: flex;
  flex-direction: column;
  gap: 10px;
  margin-bottom: 12px;
}

.google-shimmer-line {
  height: 12px;
  background: var(--google-shimmer-bg);
  border-radius: 6px;
  position: relative;
  overflow: hidden;
}

.google-shimmer-line::after {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(90deg, transparent, var(--google-shimmer-wave), transparent);
  animation: shimmerAnim 1.4s infinite;
}

@keyframes shimmerAnim {
  0% { transform: translateX(-100%); }
  100% { transform: translateX(100%); }
}

/* --------------------------------------------------------------------------
   3. PANEL 1: ✦ AI OVERVIEW (GEMINI STAR FEATURE)
   -------------------------------------------------------------------------- */
.google-ai-overview-card {
  background: var(--google-ai-bg);
  border: 1px solid var(--google-ai-border);
  border-radius: 20px;
  padding: 16px;
  display: flex;
  flex-direction: column;
  gap: 12px;
  box-shadow: var(--google-card-shadow);
  position: relative;
  overflow: hidden;
}

.google-ai-overview-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 2.5px;
  background: linear-gradient(90deg, #4285F4 0%, #9b72cb 50%, #EA4335 100%);
}

.google-ai-header-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.google-ai-title-wrap {
  display: flex;
  align-items: center;
  gap: 8px;
}

.google-ai-sparkle-icon {
  font-size: 16px;
  color: var(--google-link);
  animation: aiSparklePulse 2.5s infinite ease-in-out;
}

@keyframes aiSparklePulse {
  0%, 100% { transform: scale(1); filter: drop-shadow(0 0 2px rgba(66, 133, 244, 0.6)); }
  50% { transform: scale(1.15); filter: drop-shadow(0 0 6px rgba(155, 114, 203, 0.8)); }
}

.google-ai-title {
  font-family: 'Google Sans', 'Roboto', sans-serif;
  font-size: 15px;
  font-weight: 700;
  color: var(--google-text-primary);
  letter-spacing: -0.2px;
}

.google-ai-subtext {
  font-size: 11px;
  color: var(--google-text-muted);
  margin-top: 1px;
}

.google-ai-action-buttons {
  display: flex;
  align-items: center;
  gap: 4px;
}

.google-ai-action-btn {
  background: var(--google-chip-bg);
  border: 1px solid var(--google-border);
  color: var(--google-text-primary);
  border-radius: 50%;
  width: 28px;
  height: 28px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  font-size: 12px;
  transition: all 0.15s ease;
}

.google-ai-action-btn:hover {
  background: var(--google-chip-hover);
  border-color: var(--google-link);
}

.google-ai-body-content {
  font-size: 13.5px;
  line-height: 1.6;
  color: var(--google-text-primary);
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.google-ai-body-content p {
  margin: 0;
}

.google-ai-body-content strong {
  color: var(--google-text-primary);
}

/* Key Takeaways List */
.google-ai-takeaways-list {
  display: flex;
  flex-direction: column;
  gap: 6px;
  margin-top: 4px;
}

.google-ai-takeaway-item {
  background: var(--google-ai-box);
  border: 1px solid var(--google-ai-box-border);
  border-radius: 12px;
  padding: 8px 12px;
  font-size: 12.5px;
  line-height: 1.45;
  color: var(--google-text-primary);
}

.google-ai-takeaway-item strong {
  color: var(--google-text-primary);
  font-weight: 700;
}

/* Source Citations Carousel */
.google-ai-sources-slider {
  display: flex;
  gap: 8px;
  overflow-x: auto;
  scrollbar-width: none;
  padding: 4px 0 2px 0;
}

.google-ai-sources-slider::-webkit-scrollbar {
  display: none;
}

.google-ai-source-chip {
  background: var(--google-chip-bg);
  border: 1px solid var(--google-chip-border);
  border-radius: 16px;
  padding: 5px 10px;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-size: 11.5px;
  color: var(--google-text-primary);
  text-decoration: none;
  white-space: nowrap;
  flex-shrink: 0;
  transition: all 0.15s ease;
}

.google-ai-source-chip:hover {
  background: var(--google-chip-hover);
  border-color: var(--google-link);
}

.google-ai-source-favicon {
  font-size: 12px;
}

.google-ai-source-domain {
  font-weight: 600;
  color: var(--google-text-secondary);
}

/* Interactive Follow-up Bar & Response */
.google-ai-followup-bar {
  display: flex;
  align-items: center;
  gap: 8px;
  background: var(--google-card-bg-elevated);
  border: 1px solid var(--google-border);
  border-radius: 9999px;
  padding: 5px 12px;
  margin-top: 6px;
}

.google-ai-followup-input {
  flex: 1;
  background: transparent;
  border: none;
  outline: none;
  font-size: 12.5px;
  color: var(--google-text-primary);
  font-family: inherit;
}

.google-ai-followup-input::placeholder {
  color: var(--google-text-muted);
}

/* Suggested Follow-up Prompt Chips */
.google-ai-prompt-chips {
  display: flex;
  gap: 6px;
  overflow-x: auto;
  scrollbar-width: none;
  padding: 2px 0;
}
.google-ai-prompt-chips::-webkit-scrollbar { display: none; }

.google-ai-prompt-chip {
  background: var(--google-chip-bg);
  border: 1px solid var(--google-border);
  color: var(--google-link);
  padding: 4px 10px;
  border-radius: 9999px;
  font-size: 11px;
  font-weight: 600;
  cursor: pointer;
  white-space: nowrap;
  transition: all 0.15s ease;
}

.google-ai-prompt-chip:hover {
  background: var(--google-chip-hover);
  border-color: var(--google-link);
}

/* Follow-up Interactive Answer Box */
.google-ai-answer-box {
  background: var(--google-card-bg-elevated);
  border: 1px solid var(--google-ai-border);
  border-radius: 14px;
  padding: 12px;
  margin-top: 8px;
  display: flex;
  flex-direction: column;
  gap: 6px;
  animation: answerSlideIn 0.25s ease;
}

@keyframes answerSlideIn {
  from { opacity: 0; transform: translateY(-6px); }
  to { opacity: 1; transform: translateY(0); }
}

.google-ai-answer-header {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 12px;
  font-weight: 700;
  color: var(--google-link);
}

.google-ai-answer-text {
  font-size: 13px;
  line-height: 1.55;
  color: var(--google-text-primary);
}

/* --------------------------------------------------------------------------
   4. PANEL 2: 📖 DICTIONARY & ALL (HEADWORD CARD, PAA, ORGANIC LINKS)
   -------------------------------------------------------------------------- */
.google-dict-card {
  background: var(--google-card-bg);
  border: 1px solid var(--google-border);
  border-radius: 18px;
  padding: 16px;
  display: flex;
  flex-direction: column;
  gap: 12px;
  box-shadow: var(--google-card-shadow);
}

.google-dict-headword-row {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 10px;
}

.google-dict-word-title {
  font-family: 'Google Sans', 'Roboto', sans-serif;
  font-size: 24px;
  font-weight: 700;
  color: var(--google-text-primary);
  line-height: 1.2;
}

.google-dict-phonetic-row {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-top: 3px;
  color: var(--google-text-muted);
  font-size: 13px;
}

.google-dict-speaker-btn {
  background: transparent;
  border: none;
  font-size: 15px;
  cursor: pointer;
  padding: 2px 4px;
  border-radius: 50%;
  transition: transform 0.12s ease;
}

.google-dict-speaker-btn:active {
  transform: scale(0.9);
}

.google-dict-pos-tag {
  background: var(--google-chip-bg);
  border: 1px solid var(--google-border);
  padding: 3px 8px;
  border-radius: 6px;
  font-size: 11px;
  font-style: italic;
  font-weight: 600;
  color: var(--google-text-secondary);
}

.google-dict-definition-list {
  padding-left: 20px;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.google-dict-definition-list li {
  font-size: 13px;
  line-height: 1.5;
  color: var(--google-text-primary);
}

.google-dict-origin-box {
  background: var(--google-card-bg-elevated);
  border: 1px solid var(--google-border);
  border-radius: 12px;
  padding: 10px 12px;
  font-size: 12px;
  line-height: 1.45;
  color: var(--google-text-secondary);
}

.google-dict-origin-box strong {
  color: var(--google-link);
}

.google-dict-synonyms-row {
  display: flex;
  gap: 6px;
  flex-wrap: wrap;
  margin-top: 4px;
}

.google-dict-syn-chip {
  background: var(--google-chip-bg);
  border: 1px solid var(--google-border);
  border-radius: 9999px;
  padding: 4px 10px;
  font-size: 11.5px;
  color: var(--google-link);
  cursor: pointer;
  transition: all 0.15s ease;
}

.google-dict-syn-chip:hover {
  background: var(--google-chip-hover);
  border-color: var(--google-link);
}

/* People Also Ask (PAA) Accordion */
.google-paa-section {
  background: var(--google-card-bg);
  border: 1px solid var(--google-border);
  border-radius: 18px;
  overflow: hidden;
  box-shadow: var(--google-card-shadow);
}

.google-paa-header {
  padding: 14px 16px 10px 16px;
  font-family: 'Google Sans', sans-serif;
  font-size: 15px;
  font-weight: 700;
  color: var(--google-text-primary);
  border-bottom: 1px solid var(--google-border);
}

.google-paa-item {
  border-bottom: 1px solid var(--google-border);
}

.google-paa-item:last-child {
  border-bottom: none;
}

.google-paa-question-btn {
  width: 100%;
  background: transparent;
  border: none;
  padding: 12px 16px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  font-size: 13px;
  font-weight: 600;
  color: var(--google-text-primary);
  cursor: pointer;
  text-align: left;
}

.google-paa-chevron {
  font-size: 10px;
  color: var(--google-text-muted);
  transition: transform 0.2s ease;
}

.google-paa-item.is-open .google-paa-chevron {
  transform: rotate(180deg);
}

.google-paa-answer-panel {
  display: none;
  padding: 10px 16px 14px 16px;
  font-size: 12.5px;
  line-height: 1.55;
  color: var(--google-text-secondary);
  border-top: 1px dashed var(--google-border);
  background: var(--google-card-bg-elevated);
}

.google-paa-item.is-open .google-paa-answer-panel {
  display: block;
}

/* Organic Search Results */
.google-organic-card {
  background: var(--google-card-bg);
  border: 1px solid var(--google-border);
  border-radius: 16px;
  padding: 14px;
  display: flex;
  flex-direction: column;
  gap: 6px;
  box-shadow: var(--google-card-shadow);
}

.google-result-breadcrumb {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 11.5px;
  color: var(--google-text-secondary);
}

.google-result-title {
  font-family: 'Google Sans', 'Roboto', sans-serif;
  font-size: 15px;
  font-weight: 600;
  color: var(--google-link);
  text-decoration: none;
  line-height: 1.35;
}

.google-result-title:hover {
  text-decoration: underline;
}

.google-result-snippet {
  font-size: 12.5px;
  line-height: 1.5;
  color: var(--google-text-secondary);
}

.google-result-sitelinks {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  margin-top: 4px;
}

.google-sitelink-chip {
  font-size: 11px;
  color: var(--google-link);
}

/* Related Searches */
.google-related-section {
  display: flex;
  flex-direction: column;
  gap: 8px;
  padding: 6px 0;
}

.google-related-pills-wrap {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.google-related-pill {
  background: var(--google-chip-bg);
  border: 1px solid var(--google-border);
  border-radius: 9999px;
  padding: 6px 12px;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-size: 12px;
  color: var(--google-text-primary);
  cursor: pointer;
  transition: all 0.15s ease;
}

.google-related-pill:hover {
  background: var(--google-chip-hover);
  border-color: var(--google-link);
}

/* --------------------------------------------------------------------------
   5. PANEL 3: 🖼️ IMAGES
   -------------------------------------------------------------------------- */
.google-images-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 10px;
}

.google-image-cell {
  background: var(--google-card-bg);
  border: 1px solid var(--google-border);
  border-radius: 14px;
  overflow: hidden;
  cursor: pointer;
  display: flex;
  flex-direction: column;
  box-shadow: var(--google-card-shadow);
  transition: transform 0.2s ease, border-color 0.2s ease;
}

.google-image-cell:hover {
  transform: translateY(-2px);
  border-color: var(--google-link);
}

.google-image-img-wrap {
  width: 100%;
  aspect-ratio: 4 / 3;
  background: var(--google-card-bg-elevated);
  position: relative;
  overflow: hidden;
}

.google-image-img-wrap img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s ease;
}

.google-image-cell:hover img {
  transform: scale(1.05);
}

.google-image-caption-box {
  padding: 8px 10px;
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.google-image-caption-title {
  font-size: 11.5px;
  color: var(--google-text-primary);
  font-weight: 600;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.google-image-caption-sub {
  font-size: 10px;
  color: var(--google-text-muted);
}

/* --------------------------------------------------------------------------
   6. PANEL 4: 🎬 VIDEOS
   -------------------------------------------------------------------------- */
.google-videos-list {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.google-video-item {
  background: var(--google-card-bg);
  border: 1px solid var(--google-border);
  border-radius: 14px;
  padding: 10px;
  display: flex;
  gap: 12px;
  cursor: pointer;
  box-shadow: var(--google-card-shadow);
  transition: all 0.2s ease;
}

.google-video-item:hover {
  border-color: var(--google-link);
  transform: translateY(-1.5px);
}

.google-video-thumb-wrap {
  width: 120px;
  height: 75px;
  border-radius: 8px;
  background: var(--google-card-bg-elevated);
  position: relative;
  overflow: hidden;
  flex-shrink: 0;
}

.google-video-thumb-wrap img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.google-video-duration-pill {
  position: absolute;
  bottom: 4px;
  right: 4px;
  background: rgba(0, 0, 0, 0.85);
  color: #fff;
  font-size: 9.5px;
  font-weight: 700;
  padding: 2px 5px;
  border-radius: 4px;
}

.google-video-meta {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 4px;
  min-width: 0;
}

.google-video-title {
  font-size: 13.5px;
  font-weight: 600;
  color: var(--google-link);
  line-height: 1.35;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.google-video-source-text {
  font-size: 11px;
  color: var(--google-text-muted);
}

/* --------------------------------------------------------------------------
   7. PANEL 5: 📚 BOOKS & CITATIONS
   -------------------------------------------------------------------------- */
.google-books-list {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.google-book-item {
  background: var(--google-card-bg);
  border: 1px solid var(--google-border);
  border-radius: 14px;
  padding: 14px;
  display: flex;
  flex-direction: column;
  gap: 8px;
  box-shadow: var(--google-card-shadow);
}

.google-book-quote-text {
  font-style: italic;
  font-size: 13px;
  line-height: 1.55;
  color: var(--google-text-primary);
}

.google-book-author-row {
  font-size: 11px;
  color: var(--google-text-secondary);
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 6px;
  margin-top: 2px;
}

.google-book-cta-btn {
  background: var(--google-chip-bg);
  border: 1px solid var(--google-border);
  color: var(--google-link);
  padding: 3px 8px;
  border-radius: 9999px;
  font-size: 10.5px;
  font-weight: 600;
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  gap: 4px;
}

.google-book-cta-btn:hover {
  background: var(--google-chip-hover);
}

/* --------------------------------------------------------------------------
   8. TOAST ALERTS & LIGHTBOX MODAL
   -------------------------------------------------------------------------- */
.google-locked-toast-alert {
  position: absolute;
  bottom: 80px;
  left: 50%;
  transform: translateX(-50%) translateY(20px);
  background: rgba(16, 185, 129, 0.95);
  color: #fff;
  padding: 9px 18px;
  border-radius: 9999px;
  font-size: 12.5px;
  font-weight: 600;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.3);
  pointer-events: none;
  opacity: 0;
  transition: all 0.25s ease;
  z-index: 999;
  white-space: nowrap;
}

.google-locked-toast-alert.show {
  transform: translateX(-50%) translateY(0);
  opacity: 1;
}

.explore-media-modal {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.75);
  backdrop-filter: blur(8px);
  display: none;
  align-items: center;
  justify-content: center;
  z-index: 1000;
  padding: 16px;
}

.explore-media-modal.is-open {
  display: flex;
}

.explore-modal-content {
  background: var(--google-card-bg);
  border: 1px solid var(--google-border);
  border-radius: 16px;
  max-width: 500px;
  width: 100%;
  overflow: hidden;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5);
}

.explore-modal-header {
  padding: 12px 16px;
  border-bottom: 1px solid var(--google-border);
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-weight: 700;
  font-size: 14px;
  color: var(--google-text-primary);
}

.explore-modal-close-btn {
  background: transparent;
  border: none;
  font-size: 16px;
  color: var(--google-text-muted);
  cursor: pointer;
  padding: 2px 6px;
}

.explore-modal-close-btn:hover {
  color: var(--google-text-primary);
}
`;

fs.writeFileSync('main app/public/styles/explore-tab.css', newCss, 'utf8');
console.log('Successfully wrote dual-theme explore-tab.css!');
