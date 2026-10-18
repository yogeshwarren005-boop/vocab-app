import fs from 'node:fs';
import path from 'node:path';

const APP_DB = path.resolve('App database');
const VAULT_INDEX_PATH = path.resolve('main app/public/data/vault-index.json');
const OUTPUT_PATH = path.resolve('main app/public/data/root-dashboards.json');
const DIST_OUTPUT_PATH = path.resolve('main app/dist/data/root-dashboards.json');

console.time('Generate Root Dashboards');
const vaultIndex = JSON.parse(fs.readFileSync(VAULT_INDEX_PATH, 'utf8'));

// Pre-index pages by folder in O(N)
const pagesByFolder = new Map();
for (const p of vaultIndex.pages) {
  const norm = p.p.replace(/\\/g, '/');
  const lastSlash = norm.lastIndexOf('/');
  const folder = lastSlash !== -1 ? norm.slice(0, lastSlash) : '';
  if (!pagesByFolder.has(folder)) {
    pagesByFolder.set(folder, []);
  }
  pagesByFolder.get(folder).push(p);
}

// Find all root dashboard pages
const rootDashPages = vaultIndex.pages.filter(p => {
  const fn = p.p.split('/').pop();
  return (
    p.t === 'root_dashboard' ||
    (fn.startsWith('Dashboard — ') && !fn.includes('derived') && !fn.includes('Derived') && !fn.includes('Roots'))
  );
});

console.log(`Found ${rootDashPages.length} candidate root dashboard pages in vault index.`);

const dashboards = {};

for (const dp of rootDashPages) {
  const fullPath = path.join(APP_DB, dp.p);
  if (!fs.existsSync(fullPath)) continue;

  const content = fs.readFileSync(fullPath, 'utf8');

  // Extract root name
  const fn = dp.p.split('/').pop().replace(/\.md$/i, '');
  const rootName = fn.replace(/^Dashboard\s*[—–-]\s*/i, '').trim();

  // Extract Greek/Latin script, core meaning, and cognitive anchor
  const scriptMatch = content.match(/<span class=["']cm-script["']>([\s\S]*?)<\/span>/i);
  const defMatch = content.match(/<span class=["']cm-definition["']>([\s\S]*?)<\/span>/i);
  const anchorMatch = content.match(/Cognitive Anchor:<\/b>([\s\S]*?)<\/span>/i);

  // Extract cluster from path or frontmatter
  let cluster = '';
  const parts = dp.p.split('/');
  for (const part of parts) {
    if (part.startsWith('Cluster ')) {
      cluster = part.replace(/^Cluster\s+/i, '').trim();
      break;
    }
  }

  const category = dp.p.startsWith('Greek roots') ? 'greek' : dp.p.startsWith('Latin roots') ? 'latin' : 'vocab';

  // Fast O(1) folder lookup
  const folder = dp.p.slice(0, dp.p.lastIndexOf('/'));
  const folderPages = pagesByFolder.get(folder) || [];
  const words = folderPages
    .filter(p => p.p !== dp.p && !p.p.endsWith('.md.bak') && !p.p.split('/').pop().startsWith('Dashboard — ') && !p.p.split('/').pop().startsWith('Word Triage'))
    .map(p => p.p.split('/').pop().replace(/\.md$/i, ''));

  dashboards[rootName.toLowerCase()] = {
    root: rootName,
    path: dp.p,
    category,
    cluster: cluster ? `Cluster ${cluster}` : (dp.c ? dp.c.replace(/^\[\[|\]\]$/g, '') : ''),
    script: scriptMatch ? scriptMatch[1].trim() : '',
    meaning: defMatch ? defMatch[1].replace(/^[“"']+|[”"']+$/g, '').trim() : '',
    anchor: anchorMatch ? anchorMatch[1].trim() : '',
    status: dp.s || 'unread',
    wordCount: words.length,
    words: words
  };
}

// Add English Vocabulary Master clusters
const vocabClusters = vaultIndex.pages.filter(p => {
  return p.p.startsWith('English vocabulary master/Cluster ') && p.p.endsWith('.md') && p.p.split('/').pop().startsWith('Cluster ');
});

for (const vp of vocabClusters) {
  const fullPath = path.join(APP_DB, vp.p);
  if (!fs.existsSync(fullPath)) continue;

  const content = fs.readFileSync(fullPath, 'utf8');
  const clusterName = vp.p.split('/').pop().replace(/\.md$/i, '').replace(/^Cluster\s+/i, '').trim();
  const themeMatch = content.match(/theme:\s*["']?([^"'\n\r]+)["']?/i);
  const catMatch = content.match(/category:\s*["']?([^"'\n\r]+)["']?/i);

  const folder = vp.p.slice(0, vp.p.lastIndexOf('/'));
  const folderPages = pagesByFolder.get(folder) || [];
  const words = folderPages
    .filter(p => p.p !== vp.p && !p.p.endsWith('.md.bak') && !p.p.split('/').pop().startsWith('Cluster '))
    .map(p => p.p.split('/').pop().replace(/\.md$/i, ''));

  dashboards[clusterName.toLowerCase()] = {
    root: clusterName,
    path: vp.p,
    category: 'vocab',
    cluster: `Cluster ${clusterName}`,
    script: 'Evocative English',
    meaning: themeMatch ? themeMatch[1].trim() : 'Expressive Anglo-Saxon, Old Norse, Celtic & non-classical vocabulary.',
    anchor: catMatch ? catMatch[1].trim() : 'Master Cluster',
    status: vp.s || 'unread',
    wordCount: words.length,
    words: words
  };
}

const count = Object.keys(dashboards).length;
console.log(`Successfully extracted ${count} root & cluster dashboards.`);

const jsonStr = JSON.stringify(dashboards);
fs.writeFileSync(OUTPUT_PATH, jsonStr, 'utf8');

if (fs.existsSync(path.dirname(DIST_OUTPUT_PATH))) {
  fs.writeFileSync(DIST_OUTPUT_PATH, jsonStr, 'utf8');
}

const stat = fs.statSync(OUTPUT_PATH);
console.log(`Written to ${OUTPUT_PATH} (${(stat.size / 1024).toFixed(1)} KB)`);
console.timeEnd('Generate Root Dashboards');
