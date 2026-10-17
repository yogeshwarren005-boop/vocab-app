import fs from 'fs';
import path from 'path';

const DB_ROOT = path.resolve('../App database');
const indexPath = 'public/data/vault-index.json';
const index = JSON.parse(fs.readFileSync(indexPath, 'utf8'));

// 1. Scan the tree exactly like verify-database-tree.mjs
const treeWords = [];
const dashboardsList = [];

for (const pillar of ['Latin roots', 'Greek roots']) {
  const pillarDir = path.join(DB_ROOT, pillar);
  if (!fs.existsSync(pillarDir)) continue;
  const clusters = fs.readdirSync(pillarDir, { withFileTypes: true });
  for (const c of clusters) {
    if (c.isDirectory() && c.name.startsWith('Cluster ')) {
      const clusterPath = path.join(pillarDir, c.name);
      const subs = fs.readdirSync(clusterPath, { withFileTypes: true });
      for (const s of subs) {
        if (s.isDirectory() && s.name.startsWith('Dashboard — ')) {
          const dashPath = path.join(clusterPath, s.name);
          const words = fs.readdirSync(dashPath, { withFileTypes: true });
          dashboardsList.push({
            pillar,
            cluster: c.name,
            dashDir: s.name,
            dashRel: `${pillar}/${c.name}/${s.name}.md`,
            wordCount: 0,
            words: []
          });
          const currDash = dashboardsList[dashboardsList.length - 1];
          for (const w of words) {
            if (w.isFile() && w.name.endsWith('.md')) {
              const rel = `${pillar}/${c.name}/${s.name}/${w.name}`;
              treeWords.push({ pillar, rel, cluster: c.name, dash: s.name, file: w.name });
              currDash.words.push(rel);
              currDash.wordCount++;
            }
          }
        }
      }
    }
  }
}

const vocabDir = path.join(DB_ROOT, 'English vocabulary master');
if (fs.existsSync(vocabDir)) {
  const clusters = fs.readdirSync(vocabDir, { withFileTypes: true });
  for (const c of clusters) {
    if (c.isDirectory() && c.name.startsWith('Cluster ')) {
      const clusterPath = path.join(vocabDir, c.name);
      const subs = fs.readdirSync(clusterPath, { withFileTypes: true });
      for (const s of subs) {
        if (s.isFile() && s.name.endsWith('.md')) {
          if (!s.name.startsWith('Cluster ') && !s.name.startsWith('Semantic Field — ')) {
            const rel = `English vocabulary master/${c.name}/${s.name}`;
            treeWords.push({ pillar: 'English vocabulary master', rel, cluster: c.name, dash: 'N/A', file: s.name });
          }
        }
      }
    }
  }
}

console.log(`Total tree individual words counted: ${treeWords.length}`);
console.log(`Total dashboards in tree: ${dashboardsList.length}`);

// Check which tree words are classified as study pages by mobile-app logic
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

const excludedWords = treeWords.filter(w => isStudyPage(w.rel));
console.log(`Tree words excluded by isStudyPage: ${excludedWords.length}`);
if (excludedWords.length > 0) {
  console.log(`Sample excluded tree words (first 20):`);
  for (const ew of excludedWords.slice(0, 20)) {
    console.log(`  - ${ew.rel}`);
  }
}

// Check which dashboards have 0 words in tree
const emptyDashboards = dashboardsList.filter(d => d.wordCount === 0);
console.log(`Dashboards in tree with 0 words: ${emptyDashboards.length}`);
if (emptyDashboards.length > 0) {
  for (const ed of emptyDashboards) {
    console.log(`  - ${ed.dashRel} (0 words in folder)`);
  }
}
