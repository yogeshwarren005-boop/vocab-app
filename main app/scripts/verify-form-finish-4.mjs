import fs from 'fs';
import path from 'path';

const slice = JSON.parse(fs.readFileSync('main app/scripts/slice-form-finish-4.json', 'utf8'));
const base = path.resolve('App database/Greek roots/Cluster Form & Space');

let issues = 0;
let checked = 0;
const issueList = [];

const badAuthorPatterns = [
  /academic lexicon/i,
  /classic author/i,
  /unknown/i,
  /anonymous/i,
  /various/i,
  /etymological lexicon/i,
  /etymological dictionary/i,
  /dictionary of/i,
  /standard consensus/i,
  /lexical survey/i,
  /morphological/i,
  /traditional grammar/i
];

for (const relPath of slice) {
  checked++;
  const fullPath = path.join(base, relPath);
  if (!fs.existsSync(fullPath)) {
    issueList.push(`[NOT FOUND] ${relPath}`);
    issues++;
    continue;
  }
  const content = fs.readFileSync(fullPath, 'utf8');

  // Check frontmatter
  if (!content.startsWith('---')) {
    issueList.push(`[FRONTMATTER] Missing in ${relPath}`);
    issues++;
  }

  // Check dataviewjs
  if (!content.includes('```dataviewjs')) {
    issueList.push(`[DATAVIEWJS] Missing in ${relPath}`);
    issues++;
  }

  // Check status toggle callout
  if (!content.includes('> [!status] 🎯 **Status:**')) {
    issueList.push(`[STATUS CALLOUT] Missing in ${relPath}`);
    issues++;
  }

  // Check book callout
  if (!content.includes('> [!book] 📖 Definitions & Semantic Range')) {
    issueList.push(`[BOOK CALLOUT] Missing in ${relPath}`);
    issues++;
  }

  // Check primary definition
  const primaryMatch = content.match(/> 1\. \*\*Primary Definition \(Lexical \/ Standard Consensus\)\*\*: (.*)/);
  if (!primaryMatch || primaryMatch[1].trim().length < 15 || primaryMatch[1].includes('A term designating an entity')) {
    issueList.push(`[PRIMARY DEF] Invalid or too short in ${relPath}`);
    issues++;
  }

  // Check secondary definition
  const secondaryMatch = content.match(/> 2\. \*\*Secondary \/ Nuanced Definition \(Specialized \/ Domain \/ Encyclopedic\)\*\*: (.*)/);
  if (!secondaryMatch || secondaryMatch[1].trim().length < 15 || secondaryMatch[1].includes('Specialized application within')) {
    issueList.push(`[SECONDARY DEF] Invalid or too short in ${relPath}`);
    issues++;
  }

  // Check definitions distinction
  if (primaryMatch && secondaryMatch && primaryMatch[1].trim() === secondaryMatch[1].trim()) {
    issueList.push(`[DEF DUPLICATION] Primary equals secondary in ${relPath}`);
    issues++;
  }

  // Check quote callout
  if (!content.includes('> [!quote] 💬 Contextual Usage & Authentic Quotations')) {
    issueList.push(`[QUOTE CALLOUT] Missing in ${relPath}`);
    issues++;
  }

  // Extract headword from filename
  const headword = path.basename(relPath, '.md').toLowerCase();

  // Count quotes
  const quoteLines = content.split('\n').filter(line => line.startsWith('> - 📜 **'));
  if (quoteLines.length !== 3) {
    issueList.push(`[QUOTE COUNT] Found ${quoteLines.length} quotes in ${relPath}`);
    issues++;
  }

  const authors = [];
  for (const line of quoteLines) {
    const match = line.match(/^> - 📜 \*\*(.+?)\s+\(\*(.+?)\*\):\*\*\s+\*"(.*)"\*$/);
    if (!match) {
      issueList.push(`[MALFORMED QUOTE] In ${relPath}: ${line}`);
      issues++;
      continue;
    }
    const [, author, work, quoteText] = match;
    const authorClean = author.trim();
    authors.push(authorClean.toLowerCase());

    for (const pat of badAuthorPatterns) {
      if (pat.test(authorClean)) {
        issueList.push(`[PLACEHOLDER AUTHOR] Found "${authorClean}" in ${relPath}`);
        issues++;
        break;
      }
    }

    if (!quoteText.includes('**')) {
      issueList.push(`[BOLDING MISSING] In ${relPath}: ${quoteText}`);
      issues++;
    }
  }

  // Check 3 distinct authors
  const uniqueAuthors = new Set(authors);
  if (uniqueAuthors.size !== quoteLines.length) {
    issueList.push(`[DUPLICATE AUTHORS] In ${relPath}: ${authors.join(', ')}`);
    issues++;
  }
}

console.log('========================================');
console.log('Verification Audit for Finish Slice 4:');
console.log('Total notes checked:', checked);
console.log('Total issues found:', issues);
if (issueList.length > 0) {
  console.log(`Sample issues (first 20 of ${issueList.length}):`);
  issueList.slice(0, 20).forEach(i => console.log('  ', i));
} else {
  console.log('ALL 384 NOTES PERFECTLY COMPLIANT WITH STRICT STANDARDS!');
}
console.log('========================================');
process.exit(issues > 0 ? 1 : 0);
