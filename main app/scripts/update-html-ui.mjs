import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const HTML_PATH = path.resolve(__dirname, '..', 'public', 'index.html');

let html = fs.readFileSync(HTML_PATH, 'utf8');

// 1. Add Tier Filter Bar in #view-cards
const tierBarHtml = `        <!-- Frequency Tier Quick-Filter Chips Bar -->
        <div class="cards-tier-filter-bar" id="cards-tier-filter-bar">
          <button class="tier-pill-btn active" data-tier="all">
            <span>🌐 All Words</span>
          </button>
          <button class="tier-pill-btn t1" data-tier="1">
            <span>⭐ Learn First</span>
          </button>
          <button class="tier-pill-btn t2" data-tier="2">
            <span>📈 Learn Later</span>
          </button>
          <button class="tier-pill-btn t3" data-tier="3">
            <span>🏛️ Learn Last</span>
          </button>
        </div>\n\n`;

if (!html.includes('id="cards-tier-filter-bar"')) {
  const target1 = '<!-- Clean Word Card Swipable Container -->';
  if (html.includes(target1)) {
    html = html.replace(target1, tierBarHtml + '        ' + target1);
    console.log('✅ Added cards-tier-filter-bar to index.html');
  } else {
    console.warn('Target 1 not found');
  }
}

// 2. Add 3-Tier HUD stats grid in Settings Tracking card
const tierHudHtml = `              <!-- 3-Tier Pedagogical Frequency Breakdown -->
              <div class="tier-hud-grid">
                <div class="tier-hud-card">
                  <div class="tier-hud-title">⭐ Tier 1: First</div>
                  <div class="tier-hud-val" id="hud-tier1-count">5,171</div>
                  <div class="tier-hud-sub" id="hud-tier1-sub">High-Frequency Core</div>
                </div>
                <div class="tier-hud-card">
                  <div class="tier-hud-title">📈 Tier 2: Later</div>
                  <div class="tier-hud-val" id="hud-tier2-count">9,340</div>
                  <div class="tier-hud-sub" id="hud-tier2-sub">Academic &amp; Elevated</div>
                </div>
                <div class="tier-hud-card">
                  <div class="tier-hud-title">🏛️ Tier 3: Last</div>
                  <div class="tier-hud-val" id="hud-tier3-count">37,088</div>
                  <div class="tier-hud-sub" id="hud-tier3-sub">Rare &amp; Specialized</div>
                </div>
              </div>\n`;

if (!html.includes('id="hud-tier1-count"')) {
  const target2 = 'Tracking 51,598 vocabulary & classical root notes across your vault';
  if (html.includes(target2)) {
    html = html.replace(target2, 'Tracking 51,599 vocabulary & classical root notes across your vault\n' + tierHudHtml);
    console.log('✅ Added tier-hud-grid to index.html');
  } else {
    console.warn('Target 2 not found');
  }
}

fs.writeFileSync(HTML_PATH, html, 'utf8');
console.log('HTML updates complete.');
