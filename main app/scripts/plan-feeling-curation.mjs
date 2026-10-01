import fs from 'fs';
import path from 'path';

const targetDir = 'App database/Greek roots/Cluster Feeling & Sensation';
const dashboards = fs.readdirSync(targetDir, { withFileTypes: true })
  .filter(d => d.isDirectory() && d.name.startsWith('Dashboard —'))
  .map(d => d.name)
  .sort();

console.log('Total dashboards:', dashboards.length);
let grandTotal = 0;
const inventory = {};

for (const db of dashboards) {
  const dbPath = path.join(targetDir, db);
  const files = fs.readdirSync(dbPath)
    .filter(f => f.endsWith('.md') && !f.startsWith('Dashboard —') && !f.startsWith('Word Triage —'))
    .sort();
  inventory[db] = files;
  grandTotal += files.length;
  console.log(db + ': ' + files.length + ' words');
}
console.log('Grand total words:', grandTotal);

// Output inventory as JSON for reference
fs.writeFileSync('main app/scripts/feeling-inventory.json', JSON.stringify(inventory, null, 2), 'utf8');
