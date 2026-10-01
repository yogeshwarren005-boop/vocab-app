import fs from 'fs';
import path from 'path';

const baseDir = 'App database/Greek roots';
const dirs = fs.readdirSync(baseDir, { withFileTypes: true })
  .filter(d => d.isDirectory() && d.name.startsWith('Cluster '))
  .map(d => d.name);

console.log('Total Greek clusters found:', dirs.length);
let grandTotal = 0;
for (const dir of dirs) {
  let count = 0;
  const clusterPath = path.join(baseDir, dir);
  const dashboards = fs.readdirSync(clusterPath, { withFileTypes: true })
    .filter(d => d.isDirectory() && d.name.startsWith('Dashboard — '));
  for (const dash of dashboards) {
    const files = fs.readdirSync(path.join(clusterPath, dash.name))
      .filter(f => f.endsWith('.md'));
    count += files.length;
  }
  grandTotal += count;
  console.log(`${dir}: ${count} words across ${dashboards.length} dashboards`);
}
console.log('Grand total words in Greek clusters:', grandTotal);
