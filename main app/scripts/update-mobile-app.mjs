import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const JS_PATH = path.resolve(__dirname, '..', 'public', 'js', 'mobile-app.js');

let js = fs.readFileSync(JS_PATH, 'utf8').replace(/\r\n/g, '\n');

// 1. Add this.dashboardsFilterTier & this.cardsFilterTier to constructor
if (!js.includes('this.cardsFilterTier')) {
  js = js.replace(
    "this.dashboardsFilterCategory = 'all';",
    "this.dashboardsFilterCategory = 'all';\n    this.dashboardsFilterTier = 'all';"
  );
  js = js.replace(
    "this.cardsFilterCategory = 'all';",
    "this.cardsFilterCategory = 'all';\n    this.cardsFilterTier = 'all';"
  );
  console.log('✅ Added tier filter state to constructor');
}

// 2. Update prepareWordCards to set tier, zipf, rank, and sort High-Frequency first
const oldPrepareCards = `      // Strictly include only individual vocabulary words
      if (this.isWordCard(notePath)) {
        const cleanName = notePath.slice(notePath.lastIndexOf('/') + 1).replace(/\\.md$/i, '');
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

    this.applyCardsFilter();`;

const newPrepareCards = `      // Strictly include only individual vocabulary words
      if (this.isWordCard(notePath)) {
        const cleanName = notePath.slice(notePath.lastIndexOf('/') + 1).replace(/\\.md$/i, '');
        const category = this.getCategoryFromPath(notePath);
        const cluster = this.getClusterFromPath(notePath);
        const status = this.getStatus(notePath);
        const tier = p.f || (category === 'vocab' ? 1 : 3);
        const zipf = p.z || (tier === 1 ? 4.0 : tier === 2 ? 2.5 : 1.2);
        const rank = p.rk || 999999;
        const tierLabel = tier === 1 ? 'Words to learn first' : tier === 2 ? 'Words to learn a little later' : 'Words to learn last';

        this.allWordCards.push({
          path: notePath,
          name: cleanName,
          category,
          cluster,
          status,
          tier,
          zipf,
          rank,
          tierLabel,
          rawPage: p
        });
      }
    }

    // Deterministic Pedagogical Frequency Sorting (Learn First words at the top):
    // 1. Tier 1 (High frequency core)
    // 2. Tier 2 (Academic & elevated)
    // 3. Tier 3 (Archaic & specialized)
    // Within each tier: Higher Zipf score / lower rank first
    this.allWordCards.sort((a, b) => {
      if (a.tier !== b.tier) return a.tier - b.tier;
      if (b.zipf !== a.zipf) return b.zipf - a.zipf;
      if (a.rank !== b.rank) return a.rank - b.rank;
      return a.name.localeCompare(b.name);
    });

    this.applyCardsFilter();`;

if (js.includes(oldPrepareCards)) {
  js = js.replace(oldPrepareCards, newPrepareCards);
  console.log('✅ Updated prepareWordCards with tier assignment & high-frequency sorting');
} else {
  console.warn('Could not find exact oldPrepareCards block');
}

// 3. Update applyCardsFilter to filter by tier
const oldCardsFilterLogic = `      // Category filter (only active if not scoped)
      if (!this.activeScope && cat !== 'all' && c.category !== cat) return false;

      // Status filter
      if (status !== 'all' && c.status !== status) return false;`;

const newCardsFilterLogic = `      // Category filter (only active if not scoped)
      if (!this.activeScope && cat !== 'all' && c.category !== cat) return false;

      // Frequency Tier filter (Tier 1: Learn First, Tier 2: Learn Later, Tier 3: Learn Last)
      if (this.cardsFilterTier !== 'all' && String(c.tier) !== String(this.cardsFilterTier)) return false;

      // Status filter
      if (status !== 'all' && c.status !== status) return false;`;

if (js.includes(oldCardsFilterLogic)) {
  js = js.replace(oldCardsFilterLogic, newCardsFilterLogic);
  console.log('✅ Updated applyCardsFilter with tier filtering');
} else {
  console.warn('Could not find oldCardsFilterLogic');
}

// 4. Update renderFeedCard to display frequency tier badge on Word Cards
const oldWordTitleGroup = `          <div class="clean-word-title-group">
            <div class="clean-word-title">\${escapeHtml(card.name)}</div>
            \${pos ? \`<span class="clean-pos-badge">\${escapeHtml(pos)}</span>\` : ''}
          </div>`;

const newWordTitleGroup = `          <div class="clean-word-title-group">
            <div class="clean-word-title">\${escapeHtml(card.name)}</div>
            <div class="clean-word-meta-badges">
              \${pos ? \`<span class="clean-pos-badge">\${escapeHtml(pos)}</span>\` : ''}
              <span class="frequency-tier-badge tier-\${card.tier || 3}" title="\${card.tier === 1 ? '⭐ Words to learn first (High Frequency)' : card.tier === 2 ? '📈 Words to learn later (Academic/Elevated)' : '🏛️ Words to learn last (Rare/Obsolete)'}">
                \${card.tier === 1 ? '⭐ Learn First' : card.tier === 2 ? '📈 Learn Later' : '🏛️ Learn Last'}
                \${card.zipf && card.zipf >= 2 ? \`<small style="opacity:0.75; font-size:10px; margin-left:3px;">Zipf \${card.zipf.toFixed(1)}</small>\` : ''}
              </span>
            </div>
          </div>`;

if (js.includes(oldWordTitleGroup)) {
  js = js.replace(oldWordTitleGroup, newWordTitleGroup);
  console.log('✅ Added frequency tier badge to clean-word-header');
} else {
  console.warn('Could not find oldWordTitleGroup');
}

// 5. Wire click listeners for cards-tier-filter-bar
const oldScopeUnlock = `    // 4. Scoped Session Unlock Button
    document.getElementById('btn-clear-scope')?.addEventListener('click', () => {
      this.activeScope = null;
      this.feedWordIndex = 0;
      this.applyCardsFilter();
      this.renderFeedCard('none');
      const banner = document.getElementById('cards-scope-banner');
      if (banner) banner.style.display = 'none';
      this.showToast('🔓 Scope unlocked: Showing all vocabulary words');
    });`;

const newScopeUnlock = `    // 4. Scoped Session Unlock Button
    document.getElementById('btn-clear-scope')?.addEventListener('click', () => {
      this.activeScope = null;
      this.feedWordIndex = 0;
      this.applyCardsFilter();
      this.renderFeedCard('none');
      const banner = document.getElementById('cards-scope-banner');
      if (banner) banner.style.display = 'none';
      this.showToast('🔓 Scope unlocked: Showing all vocabulary words');
    });

    // 4b. Frequency Tier Filter Pills Bar (Tab 2)
    document.querySelectorAll('#cards-tier-filter-bar .tier-pill-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        document.querySelectorAll('#cards-tier-filter-bar .tier-pill-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        this.cardsFilterTier = btn.dataset.tier;
        this.feedWordIndex = 0;
        this.applyCardsFilter();
        this.renderFeedCard('none');
        const tierName = btn.dataset.tier === '1' ? '⭐ Tier 1: Learn First' : btn.dataset.tier === '2' ? '📈 Tier 2: Learn Later' : btn.dataset.tier === '3' ? '🏛️ Tier 3: Learn Last' : 'All Tiers';
        this.showToast(\`Showing \${this.filteredCards.length.toLocaleString()} words (\${tierName})\`);
      });
    });`;

if (js.includes(oldScopeUnlock)) {
  js = js.replace(oldScopeUnlock, newScopeUnlock);
  console.log('✅ Wired listeners for cards-tier-filter-bar');
} else {
  console.warn('Could not find oldScopeUnlock');
}

// 6. Update renderRootDashboardsExplorer filter and UI cards
const oldDashboardsFilter = `    const allDashboards = Object.values(this.rootDashboardsDb || {});
    const q = (this.dashboardsSearchQuery || '').toLowerCase().trim();
    const cat = this.dashboardsFilterCategory || 'all';

    const filtered = allDashboards.filter(d => {
      if (cat !== 'all' && d.category !== cat) return false;`;

const newDashboardsFilter = `    const allDashboards = Object.values(this.rootDashboardsDb || {});
    const q = (this.dashboardsSearchQuery || '').toLowerCase().trim();
    const cat = this.dashboardsFilterCategory || 'all';
    const tier = this.dashboardsFilterTier || 'all';

    const filtered = allDashboards.filter(d => {
      if (cat !== 'all' && d.category !== cat) return false;
      if (tier !== 'all' && String(d.tier) !== String(tier)) return false;`;

if (js.includes(oldDashboardsFilter)) {
  js = js.replace(oldDashboardsFilter, newDashboardsFilter);
  console.log('✅ Added tier filter to renderRootDashboardsExplorer');
} else {
  console.warn('Could not find oldDashboardsFilter');
}

// 7. Update dashboard card header in renderRootDashboardsExplorer
const oldRootCardHeader = `        <div class="root-card-header">
          <div class="root-card-name">
            <span>\${catEmoji}</span>
            <span>\${escapeHtml(d.root)}</span>
            \${d.script ? \`<span class="root-card-script">(\${escapeHtml(d.script)})</span>\` : ''}
          </div>
          <span class="root-discipline-tag">\${d.category === 'greek' ? 'Greek' : d.category === 'latin' ? 'Latin' : 'Vocab'}</span>
        </div>`;

const newRootCardHeader = `        <div class="root-card-header">
          <div class="root-card-name">
            <span>\${catEmoji}</span>
            <span>\${escapeHtml(d.root)}</span>
            \${d.script ? \`<span class="root-card-script">(\${escapeHtml(d.script)})</span>\` : ''}
          </div>
          <div style="display:flex; align-items:center; gap:6px;">
            <span class="frequency-tier-badge tier-\${d.tier || 2}" style="font-size:10px; padding:2px 7px;">
              \${d.tier === 1 ? '⭐ Learn First' : d.tier === 2 ? '📈 Learn Later' : '🏛️ Rare'}
            </span>
            <span class="root-discipline-tag">\${d.category === 'greek' ? 'Greek' : d.category === 'latin' ? 'Latin' : 'Vocab'}</span>
          </div>
        </div>`;

if (js.includes(oldRootCardHeader)) {
  js = js.replace(oldRootCardHeader, newRootCardHeader);
  console.log('✅ Added tier badge to root dashboard cards');
} else {
  console.warn('Could not find oldRootCardHeader');
}

// 8. Add dashboards-tier-chips to renderHomeSections
const oldDashChipsHtml = `        <div class="dashboards-filter-chips" id="dashboards-category-chips">
          <button class="filter-chip active" data-cat="all">All Dashboards</button>
          <button class="filter-chip" data-cat="greek">🏛️ Greek Roots (810)</button>
          <button class="filter-chip" data-cat="latin">📜 Latin Roots (782)</button>
          <button class="filter-chip" data-cat="vocab">👑 Vocab Clusters (30)</button>
        </div>`;

const newDashChipsHtml = `        <div class="dashboards-filter-chips" id="dashboards-category-chips">
          <button class="filter-chip active" data-cat="all">All Dashboards</button>
          <button class="filter-chip" data-cat="greek">🏛️ Greek Roots (810)</button>
          <button class="filter-chip" data-cat="latin">📜 Latin Roots (782)</button>
          <button class="filter-chip" data-cat="vocab">👑 Vocab Clusters (30)</button>
        </div>
        <div class="dashboards-filter-chips" id="dashboards-tier-chips" style="margin-top: 6px;">
          <button class="filter-chip active" data-tier="all">🌐 All Tiers</button>
          <button class="filter-chip" data-tier="1">⭐ Tier 1: Learn First</button>
          <button class="filter-chip" data-tier="2">📈 Tier 2: Learn Later</button>
          <button class="filter-chip" data-tier="3">🏛️ Tier 3: Learn Last</button>
        </div>`;

if (js.includes(oldDashChipsHtml)) {
  js = js.replace(oldDashChipsHtml, newDashChipsHtml);
  console.log('✅ Added dashboards-tier-chips HTML');
} else {
  console.warn('Could not find oldDashChipsHtml');
}

// 9. Wire click listeners for dashboards-tier-chips
const oldDashChipListeners = `    document.querySelectorAll('#dashboards-category-chips .filter-chip').forEach(chip => {
      chip.addEventListener('click', () => {
        document.querySelectorAll('#dashboards-category-chips .filter-chip').forEach(c => c.classList.remove('active'));
        chip.classList.add('active');
        this.dashboardsFilterCategory = chip.dataset.cat;
        this.renderRootDashboardsExplorer();
      });
    });`;

const newDashChipListeners = `    document.querySelectorAll('#dashboards-category-chips .filter-chip').forEach(chip => {
      chip.addEventListener('click', () => {
        document.querySelectorAll('#dashboards-category-chips .filter-chip').forEach(c => c.classList.remove('active'));
        chip.classList.add('active');
        this.dashboardsFilterCategory = chip.dataset.cat;
        this.renderRootDashboardsExplorer();
      });
    });

    document.querySelectorAll('#dashboards-tier-chips .filter-chip').forEach(chip => {
      chip.addEventListener('click', () => {
        document.querySelectorAll('#dashboards-tier-chips .filter-chip').forEach(c => c.classList.remove('active'));
        chip.classList.add('active');
        this.dashboardsFilterTier = chip.dataset.tier;
        this.renderRootDashboardsExplorer();
      });
    });`;

if (js.includes(oldDashChipListeners)) {
  js = js.replace(oldDashChipListeners, newDashChipListeners);
  console.log('✅ Wired listeners for dashboards-tier-chips');
} else {
  console.warn('Could not find oldDashChipListeners');
}

fs.writeFileSync(JS_PATH, js, 'utf8');
console.log('All mobile-app.js updates applied successfully.');
