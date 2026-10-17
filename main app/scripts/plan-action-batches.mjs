import fs from 'fs';

const flat = JSON.parse(fs.readFileSync('main app/scripts/action-flat.json', 'utf8'));

console.log(`Total words: ${flat.length}`);

// We want ~11-12 batches. 778 / 11 ~= 70.7 words per batch. 778 / 12 ~= 64.8 words per batch.
// Let's create 12 batches of ~65 words each.
const BATCH_COUNT = 12;
const targetBatchSize = Math.ceil(flat.length / BATCH_COUNT);

const batches = [];
for (let i = 0; i < BATCH_COUNT; i++) {
  const start = i * targetBatchSize;
  const end = Math.min(start + targetBatchSize, flat.length);
  batches.push(flat.slice(start, end));
}

batches.forEach((b, idx) => {
  const dashboards = [...new Set(b.map(w => w.dashboard))];
  console.log(`Batch ${idx + 1}: ${b.length} words (Dashboards: ${dashboards.map(d => d.replace('Dashboard — ', '')).join(', ')})`);
});

fs.writeFileSync('main app/scripts/action-batches.json', JSON.stringify(batches, null, 2));
