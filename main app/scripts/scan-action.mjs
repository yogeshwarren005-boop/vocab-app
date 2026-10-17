import fs from 'fs';
import path from 'path';

const targetDir = 'App database/Greek roots/Cluster Action';
const dashboards = fs.readdirSync(targetDir, { withFileTypes: true })
  .filter(d => d.isDirectory())
  .map(d => d.name)
  .sort();

console.log('Dashboards found:', dashboards.length);
let totalWords = 0;
const inventory = {};
const flatList = [];

for (const d of dashboards) {
  const dPath = path.join(targetDir, d);
  const files = fs.readdirSync(dPath)
    .filter(f => f.endsWith('.md') && !f.startsWith('Dashboard —') && !f.startsWith('Word Triage —'))
    .sort();
  inventory[d] = files;
  totalWords += files.length;
  for (const f of files) {
    flatList.push({
      dashboard: d,
      file: f,
      relPath: `${d}/${f}`,
      lemma: f.replace(/\.md$/, '')
    });
  }
  console.log(`${d}: ${files.length} words`);
}
console.log('Total words:', totalWords);
fs.writeFileSync('main app/scripts/action-inventory.json', JSON.stringify(inventory, null, 2));
fs.writeFileSync('main app/scripts/action-flat.json', JSON.stringify(flatList, null, 2));
