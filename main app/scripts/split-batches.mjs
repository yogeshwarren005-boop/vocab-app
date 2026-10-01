import fs from 'fs';
import path from 'path';

const inventory = JSON.parse(fs.readFileSync('main app/scripts/plants-inventory.json', 'utf8'));

let allWords = [];
for (const [dash, words] of Object.entries(inventory)) {
  for (const w of words) {
    allWords.push({ dashboard: dash, file: w });
  }
}

console.log('Total entries:', allWords.length);

const numBatches = 9;
const batchSize = Math.ceil(allWords.length / numBatches);

let batches = [];
for (let i = 0; i < numBatches; i++) {
  batches.push(allWords.slice(i * batchSize, (i + 1) * batchSize));
}

batches.forEach((b, idx) => {
  console.log('Batch ' + (idx + 1) + ': ' + b.length + ' words (' + b[0].dashboard + ' / ' + b[0].file + ' -> ' + b[b.length-1].dashboard + ' / ' + b[b.length-1].file + ')');
});

fs.writeFileSync('main app/scripts/plants-batch-splits.json', JSON.stringify(batches, null, 2));
