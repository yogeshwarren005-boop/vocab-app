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

const latinWords = index.pages.filter(p => isWordCard(p.p) && p.p.startsWith('Latin roots/'));
const greekWords = index.pages.filter(p => isWordCard(p.p) && p.p.startsWith('Greek roots/'));
const evmWords = index.pages.filter(p => isWordCard(p.p) && p.p.startsWith('English vocabulary master/'));

const dashboards = index.pages.filter(p => {
  const fn = p.p.split('/').pop();
  return fn.startsWith('Dashboard —') && !fn.includes('Roots') && !p.p.includes('Derived Words');
});

const wordsByFolder = new Map();
const wordsByRootLink = new Map();

for (const c of [...latinWords, ...greekWords, ...evmWords]) {
  const lastSlash = c.p.lastIndexOf('/');
  const folder = lastSlash !== -1 ? c.p.slice(0, lastSlash) : '';
  if (!wordsByFolder.has(folder)) wordsByFolder.set(folder, []);
  wordsByFolder.get(folder).push(c);

  if (c.lr) {
    if (!wordsByRootLink.has(c.lr)) wordsByRootLink.set(c.lr, []);
    wordsByRootLink.get(c.lr).push(c);
  }
  if (c.gr) {
    if (!wordsByRootLink.has(c.gr)) wordsByRootLink.set(c.gr, []);
    wordsByRootLink.get(c.gr).push(c);
  }
}

const unlinkedDashboards = [];

for (const d of dashboards) {
  const parts = d.p.split('/');
  const folder = parts.slice(0, -1).join('/');
  const fileName = parts[parts.length - 1];
  const dashName = fileName.replace(/\.md$/, '').trim();
  const rootName = dashName.replace(/^Dashboard\s+—\s+/, '').trim();

  const folderWords = (wordsByFolder.get(folder) || []).filter(c => c.p !== d.p);
  const matchSet = new Set(folderWords.map(c => c.p));
  const linkKeys = ['[[' + rootName + ']]', '[[' + dashName + ']]', '[[Dashboard — ' + rootName + ']]'];
  for (const k of linkKeys) {
    const matched = wordsByRootLink.get(k) || [];
    for (const m of matched) {
      if (m.p !== d.p) matchSet.add(m.p);
    }
  }
  if (matchSet.size === 0) {
    unlinkedDashboards.push({ d: d.p, folder, rootName });
  }
}

console.log(`Unlinked dashboards count: ${unlinkedDashboards.length}`);
for (const u of unlinkedDashboards) {
  console.log(`Unlinked: ${u.d}`);
  console.log(`Folder: ${u.folder}`);
  console.log(`Root Name: ${u.rootName}`);
  const fsList = fs.readdirSync(path.join('../App database', u.folder));
  console.log(`Files in folder:`, fsList);
}
