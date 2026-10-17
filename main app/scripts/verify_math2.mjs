import fs from 'fs';
import path from 'path';

const slice = JSON.parse(fs.readFileSync('main app/scripts/slice-math-part2.json', 'utf8'));
const base = path.resolve('App database/Greek roots/Cluster Number & Mathematics');

let issues = 0;
let checked = 0;

for (const relPath of slice) {
  checked++;
  const fullPath = path.join(base, relPath);
  if (!fs.existsSync(fullPath)) {
    console.error('File not found:', relPath);
    issues++;
    continue;
  }
  const content = fs.readFileSync(fullPath, 'utf8');

  // Check frontmatter
  if (!content.startsWith('---')) {
    console.error('Missing frontmatter in:', relPath);
    issues++;
  }
  // Check dataviewjs
  if (!content.includes('```dataviewjs')) {
    console.error('Missing dataviewjs in:', relPath);
    issues++;
  }
  // Check book callout
  if (!content.includes('> [!book] 📖 Definitions & Semantic Range')) {
    console.error('Missing [!book] in:', relPath);
    issues++;
  }
  // Check quote callout
  if (!content.includes('> [!quote] 💬 Contextual Usage & Authentic Quotations')) {
    console.error('Missing [!quote] in:', relPath);
    issues++;
  }
  // Check for placeholder author
  if (content.includes('Academic Lexicon') || content.includes('Classic Author')) {
    console.error('Found placeholder author in:', relPath);
    issues++;
  }

  // Count quotes
  const quoteLines = content.split('\n').filter(line => line.startsWith('> - 📜 **'));
  if (quoteLines.length !== 3) {
    console.error(`Quote count mismatch in ${relPath}: found ${quoteLines.length}`);
    issues++;
  }

  // Check 3 distinct authors
  const authors = quoteLines.map(line => {
    const m = line.match(/> - 📜 \*\*(.*?)\s*\(/);
    return m ? m[1].trim() : '';
  });
  const uniqueAuthors = new Set(authors);
  if (uniqueAuthors.size !== 3) {
    console.error(`Duplicate authors in ${relPath}:`, authors);
    issues++;
  }

  // Check bolded word in quotes
  for (const ql of quoteLines) {
    // The quote line format is: > - 📜 **Author (*Work*):** *" ... **word** ... "*
    // It should have at least 3 occurrences of '**' (author name start/end, colon bold, and target word bold)
    const boldMatches = ql.match(/\*\*/g);
    if (!boldMatches || boldMatches.length < 4) {
      console.error(`Missing target word bolding in ${relPath}:`, ql);
      issues++;
    }
  }
}

console.log('========================================');
console.log('Verification Finished!');
console.log('Total notes checked:', checked);
console.log('Total issues found:', issues);
console.log('========================================');
