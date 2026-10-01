import fs from 'fs';
import path from 'path';

const baseDir = 'App database/Greek roots/Cluster Physics & Chemistry';
const entries = fs.readdirSync(baseDir, { withFileTypes: true });
const dashboards = {};

for (const ent of entries) {
  if (ent.isDirectory() && ent.name.startsWith('Dashboard — ')) {
    const dashDir = path.join(baseDir, ent.name);
    const files = fs.readdirSync(dashDir).filter(f => f.endsWith('.md') && !f.startsWith('Dashboard —') && !f.startsWith('Word Triage'));
    dashboards[ent.name] = files;
  }
}

let total = 0;
for (const [dash, files] of Object.entries(dashboards)) {
  console.log(`${dash}: ${files.length} words`);
  total += files.length;
}
console.log('Total dashboards:', Object.keys(dashboards).length);
console.log('Total words:', total);

fs.writeFileSync('main app/scripts/physics-inventory.json', JSON.stringify(dashboards, null, 2));

let allWords = [];
for (const [dash, words] of Object.entries(dashboards)) {
  for (const w of words) {
    allWords.push({ dashboard: dash, file: w, relPath: path.join(dash, w).replace(/\\/g, '/') });
  }
}

const numBatches = 9;
const batchSize = Math.ceil(allWords.length / numBatches);

let batches = [];
for (let i = 0; i < numBatches; i++) {
  batches.push(allWords.slice(i * batchSize, (i + 1) * batchSize));
}

batches.forEach((b, idx) => {
  console.log(`Batch ${idx + 1}: ${b.length} words (${b[0].dashboard}/${b[0].file} -> ${b[b.length-1].dashboard}/${b[b.length-1].file})`);
});

fs.writeFileSync('main app/scripts/physics-batch-splits.json', JSON.stringify(batches, null, 2));
