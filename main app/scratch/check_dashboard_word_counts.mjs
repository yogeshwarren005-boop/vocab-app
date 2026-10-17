import fs from 'fs';
import path from 'path';

const indexPath = 'public/data/vault-index.json';
const index = JSON.parse(fs.readFileSync(indexPath, 'utf8'));

function isStudyPage(notePath) {
  if (!notePath || !notePath.endsWith('.md')) return false;
  if (notePath.includes('_assets') || notePath.includes('Templates')) return false;
  if (notePath === '00 Language Hub.md') return true;

  const baseName = notePath.slice(notePath.lastIndexOf('/') + 1).replace(/\.md$/i, '');
  const lowerBase = baseName.toLowerCase();

  if (baseName.startsWith('Dashboard —') || baseName.startsWith('Master Table') || baseName.startsWith('Word Triage')) return true;
  if (baseName.endsWith('Progress') || baseName.endsWith('MOC') || baseName.endsWith('Dashboards')) return true;
  if (baseName.startsWith('Semantic Field —') || baseName.startsWith('Concept —') || baseName.startsWith('Overview —') || baseName.startsWith('Table —')) return true;
  if (baseName.startsWith('00_') || baseName.startsWith('01_') || baseName.startsWith('02_') || baseName.startsWith('03_')) return true;
  if (notePath.includes('03_Reference_and_Rules') || notePath.includes('01_Root_Dashboards')) return true;

  if (lowerBase.startsWith('prefix') || lowerBase.startsWith('suffix')) return true;
  if (baseName.includes('Rules') || baseName.includes('Atlas') || baseName.includes('Method') || baseName.includes('Formula')) return true;

  const dirParts = notePath.split('/');
  if (dirParts.length >= 2 && dirParts[dirParts.length - 2] === baseName) return true;
  if (baseName.startsWith('Cluster ') && baseName === dirParts[dirParts.length - 1].replace(/\.md$/i, '')) return true;

  return false;
}

function isWordCard(notePath) {
  if (!notePath || !notePath.endsWith('.md')) return false;
  if (!notePath.startsWith('Greek roots/') && !notePath.startsWith('Latin roots/') && !notePath.startsWith('English vocabulary master/')) return false;
  return !isStudyPage(notePath);
}

const wordCards = index.pages.filter(p => isWordCard(p.p));
const dashboards = index.pages.filter(p => {
  const fn = p.p.split('/').pop();
  return fn.startsWith('Dashboard —') && !fn.includes('Roots') && !p.p.includes('Derived Words');
});

const ROOT_ALIASES = {
  'aev': ['ev', 'Dashboard — ev'],
  'ev': ['aev', 'Dashboard — aev']
};

function getWordsForDashboard(d, useAlias = false) {
  const parts = d.p.split('/');
  const folder = parts.slice(0, -1).join('/');
  const fileName = parts[parts.length - 1];
  const dashName = fileName.replace(/\.md$/, '').trim();
  const rootName = dashName.replace(/^Dashboard\s+—\s+/, '').trim();

  const aliases = useAlias ? (ROOT_ALIASES[rootName] || []) : [];
  const aliasFolders = aliases.map(a => folder.replace(`Dashboard — ${rootName}`, `Dashboard — ${a}`));

  return wordCards.filter(c => {
    if (c.p === d.p) return false;
    if (folder && c.p.startsWith(folder + '/')) {
      const fn = c.p.split('/').pop();
      if (!fn.startsWith('Dashboard') && !fn.startsWith('Cluster') && !fn.startsWith('Word Triage')) return true;
    }
    for (const af of aliasFolders) {
      if (af && c.p.startsWith(af + '/')) {
        const fn = c.p.split('/').pop();
        if (!fn.startsWith('Dashboard') && !fn.startsWith('Cluster') && !fn.startsWith('Word Triage')) return true;
      }
    }
    const p = c;
    if (p) {
      if (p.lr && (p.lr === `[[${rootName}]]` || p.lr === `[[${dashName}]]` || p.lr === `[[Dashboard — ${rootName}]]`)) return true;
      if (p.gr && (p.gr === `[[${rootName}]]` || p.gr === `[[${dashName}]]` || p.gr === `[[Dashboard — ${rootName}]]`)) return true;
      for (const a of aliases) {
        if (p.lr && (p.lr === `[[${a}]]` || p.lr === `[[Dashboard — ${a}]]`)) return true;
        if (p.gr && (p.gr === `[[${a}]]` || p.gr === `[[Dashboard — ${a}]]`)) return true;
      }
    }
    return false;
  });
}

console.log(`Total Dashboards: ${dashboards.length}`);
let withoutAliasPopulated = 0;
let withAliasPopulated = 0;

const distribution = [];
for (const d of dashboards) {
  const wWithout = getWordsForDashboard(d, false);
  const wWith = getWordsForDashboard(d, true);
  if (wWithout.length > 0) withoutAliasPopulated++;
  if (wWith.length > 0) withAliasPopulated++;
  distribution.push({ dash: d.p, count: wWith.length });
}

console.log(`Without Alias: ${withoutAliasPopulated} / ${dashboards.length} (${(withoutAliasPopulated/dashboards.length*100).toFixed(2)}%)`);
console.log(`With Alias:    ${withAliasPopulated} / ${dashboards.length} (${(withAliasPopulated/dashboards.length*100).toFixed(2)}%)`);

distribution.sort((a, b) => a.count - b.count);
console.log('Lowest 5 word counts per dashboard:');
for (const item of distribution.slice(0, 5)) {
  console.log(`  ${item.dash}: ${item.count} words`);
}
console.log('Highest 5 word counts per dashboard:');
for (const item of distribution.slice(-5)) {
  console.log(`  ${item.dash}: ${item.count} words`);
}
