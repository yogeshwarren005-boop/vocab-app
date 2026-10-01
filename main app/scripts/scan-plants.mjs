import fs from 'fs';
import path from 'path';

const clusterDir = 'App database/Greek roots/Cluster Plants & Botany';
const dashboards = fs.readdirSync(clusterDir).filter(d => fs.statSync(path.join(clusterDir, d)).isDirectory());

let inventory = {};
let totalWords = 0;

dashboards.sort().forEach(d => {
  const dPath = path.join(clusterDir, d);
  const files = fs.readdirSync(dPath).filter(f => 
    f.endsWith('.md') && 
    !f.startsWith('Dashboard —') &&
    !f.startsWith('Word Triage —') &&
    !f.startsWith('Cluster') &&
    !f.startsWith('Semantic Field')
  );
  inventory[d] = files.map(f => f.replace(/\.md$/, ''));
  totalWords += files.length;
});

console.log('Total dashboards:', dashboards.length);
console.log('Total words:', totalWords);
dashboards.forEach(d => {
  console.log(`${d}: ${inventory[d].length} words`);
});
fs.writeFileSync('main app/scripts/plants-inventory.json', JSON.stringify(inventory, null, 2));
