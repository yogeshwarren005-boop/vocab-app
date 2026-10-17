import fs from 'fs';
import path from 'path';

const CLUSTER_DIR = path.resolve('App database/Greek roots/Cluster Form & Space');
const SLICE_FILE = path.resolve('main app/scripts/slice-form-finish-5.json');

const files = JSON.parse(fs.readFileSync(SLICE_FILE, 'utf8'));
console.log(`Starting verification of ${files.length} notes in Form Finish Slice 5...`);

let errorCount = 0;
const errors = [];

const SYNTHETIC_AUTHORS = [
  'academic lexicon',
  'classical author',
  'etymological dictionary',
  'morphological survey',
  'standard lexicon',
  'historical lexicon',
  'linguistic survey',
  'unknown',
  'anonymous',
  'various',
  'dictionary of',
  'standard consensus'
];

for (let i = 0; i < files.length; i++) {
  const relPath = files[i];
  const fullPath = path.join(CLUSTER_DIR, relPath);

  if (!fs.existsSync(fullPath)) {
    errors.push(`[${relPath}] File does not exist`);
    errorCount++;
    continue;
  }

  const content = fs.readFileSync(fullPath, 'utf8');

  // 1. Check Frontmatter
  if (!content.startsWith('---') || !content.includes('status:') || !content.includes('cluster:')) {
    errors.push(`[${relPath}] Invalid or missing YAML frontmatter`);
    errorCount++;
  }

  // 2. Check title
  const titleMatch = content.match(/^#\s+(.+)$/m);
  if (!titleMatch) {
    errors.push(`[${relPath}] Missing title (# <word>)`);
    errorCount++;
  }
  const headword = titleMatch ? titleMatch[1].trim() : '';

  // 3. Check DataviewJS status toggle
  if (!content.includes('> [!status] 🎯 **Status:**') || !content.includes('```dataviewjs')) {
    errors.push(`[${relPath}] Missing dataviewjs status block`);
    errorCount++;
  }

  // 4. Check Definitions
  if (!content.includes('> [!book] 📖 Definitions & Semantic Range')) {
    errors.push(`[${relPath}] Missing definitions block`);
    errorCount++;
  }

  const def1Match = content.match(/> 1\.\s+\*\*Primary Definition \(Lexical \/ Standard Consensus\)\*\*:\s*(.+)/);
  const def2Match = content.match(/> 2\.\s+\*\*Secondary \/ Nuanced Definition \(Specialized \/ Domain \/ Encyclopedic\)\*\*:\s*(.+)/);

  if (!def1Match || !def1Match[1].trim() || def1Match[1].trim().length < 15) {
    errors.push(`[${relPath}] Invalid primary definition`);
    errorCount++;
  }
  if (!def2Match || !def2Match[1].trim() || def2Match[1].trim().length < 15) {
    errors.push(`[${relPath}] Invalid secondary definition`);
    errorCount++;
  }
  if (def1Match && def2Match && def1Match[1].trim().toLowerCase() === def2Match[1].trim().toLowerCase()) {
    errors.push(`[${relPath}] Duplicate definitions (primary == secondary)`);
    errorCount++;
  }

  // 5. Check Quotes Block
  if (!content.includes('> [!quote] 💬 Contextual Usage & Authentic Quotations')) {
    errors.push(`[${relPath}] Missing quotes block`);
    errorCount++;
  }

  const quoteLines = content.split('\n').filter(l => l.startsWith('> - 📜'));
  if (quoteLines.length !== 3) {
    errors.push(`[${relPath}] Expected exactly 3 quotes, found ${quoteLines.length}`);
    errorCount++;
    continue;
  }

  const authors = new Set();
  quoteLines.forEach((qLine, qIdx) => {
    const match = qLine.match(/> - 📜 \*\*([^*]+)\s+\(\*([^*]+)\*\):\*\*\s+\*(.+)\*/);
    if (!match) {
      errors.push(`[${relPath}] Quote ${qIdx + 1} does not match required format: ${qLine}`);
      errorCount++;
      return;
    }

    const author = match[1].trim();
    const work = match[2].trim();
    const quoteText = match[3].trim();

    if (SYNTHETIC_AUTHORS.some(sa => author.toLowerCase().includes(sa))) {
      errors.push(`[${relPath}] Quote ${qIdx + 1} has synthetic author: ${author}`);
      errorCount++;
    }

    authors.add(author.toLowerCase());

    if (!quoteText.includes('**')) {
      errors.push(`[${relPath}] Quote ${qIdx + 1} does not contain bold headword: ${quoteText}`);
      errorCount++;
    }
  });

  if (authors.size < 3) {
    errors.push(`[${relPath}] Expected 3 distinct authors, got ${authors.size}: ${[...authors].join(', ')}`);
    errorCount++;
  }
}

console.log('========================================');
console.log(`Form Finish Slice 5 Verification Results:`);
console.log(`Total files checked: ${files.length}`);
console.log(`Total errors: ${errorCount}`);
if (errorCount > 0) {
  console.log(`First 20 errors:`);
  console.log(errors.slice(0, 20).join('\n'));
} else {
  console.log(`ALL ${files.length} NOTES PASSED STRICT VERIFICATION WITH ZERO ERRORS!`);
}
console.log('========================================');
if (errorCount > 0) process.exit(1);
