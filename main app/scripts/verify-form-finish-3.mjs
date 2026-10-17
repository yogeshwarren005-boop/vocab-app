import fs from 'fs';
import path from 'path';

const slice = JSON.parse(fs.readFileSync('main app/scripts/slice-form-finish-3.json', 'utf8'));
const base = path.resolve('App database/Greek roots/Cluster Form & Space');

let issues = 0;
let checked = 0;
const issueList = [];

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
  if (!primaryMatch || primaryMatch[1].trim().length < 15) {
    issueList.push(`[PRIMARY DEF] Invalid or too short in ${relPath}`);
    issues++;
  }

  // Check secondary definition
  const secondaryMatch = content.match(/> 2\. \*\*Secondary \/ Nuanced Definition \(Specialized \/ Domain \/ Encyclopedic\)\*\*: (.*)/);
  if (!secondaryMatch || secondaryMatch[1].trim().length < 15) {
    issueList.push(`[SECONDARY DEF] Invalid or too short in ${relPath}`);
    issues++;
  }

  // Check definitions distinction
  if (primaryMatch && secondaryMatch && primaryMatch[1].trim().toLowerCase() === secondaryMatch[1].trim().toLowerCase()) {
    issueList.push(`[DEF DUPLICATION] Primary equals secondary in ${relPath}`);
    issues++;
  }

  // Check quote callout
  if (!content.includes('> [!quote] 💬 Contextual Usage & Authentic Quotations')) {
    issueList.push(`[QUOTE CALLOUT] Missing in ${relPath}`);
    issues++;
  }

  // Check for placeholder author
  const placeholders = [
    'Academic Lexicon',
    'Classic Author',
    'Etymological Dictionary',
    'Standard Consensus',
    'Unknown Author',
    'Traditional Grammar',
    'Anonymous'
  ];
  for (const ph of placeholders) {
    if (content.includes(ph)) {
      issueList.push(`[PLACEHOLDER AUTHOR] Found "${ph}" in ${relPath}`);
      issues++;
      break;
    }
  }

  // Extract headword from filename
  const headword = path.basename(relPath, '.md').toLowerCase();

  // Count quotes
  const quoteLines = content.split('\n').filter(line => line.startsWith('> - 📜 **'));
  if (quoteLines.length !== 3) {
    issueList.push(`[QUOTE COUNT] Found ${quoteLines.length} quotes in ${relPath}`);
    issues++;
  }

  // Check 3 distinct authors
  const authors = quoteLines.map(line => {
    const m = line.match(/> - 📜 \*\*(.*?)\s*\(/);
    return m ? m[1].trim().toLowerCase() : '';
  });
  const uniqueAuthors = new Set(authors.filter(a => a.length > 0));
  if (uniqueAuthors.size !== 3) {
    issueList.push(`[DUPLICATE AUTHORS] In ${relPath}: ${Array.from(uniqueAuthors).join(', ')}`);
    issues++;
  }

  // Check bolded word in quotes
  for (const ql of quoteLines) {
    const boldMatches = ql.match(/\*\*(.*?)\*\*/g);
    // There must be the author (**Author (Work):**) AND at least one bolded word in the quote
    if (!boldMatches || boldMatches.length < 2) {
      issueList.push(`[BOLDING MISSING] In ${relPath}: ${ql}`);
      issues++;
    } else {
      // Check that the headword (or root form) appears bolded
      const quoteTextBolded = boldMatches.slice(1).map(b => b.replace(/\*\*/g, '').toLowerCase());
      const baseClean = headword.replace(/[-_]/g, ' ').trim();
      const hasHeadword = quoteTextBolded.some(b => {
        const bClean = b.replace(/[-_]/g, ' ').trim();
        return bClean.includes(baseClean) || baseClean.includes(bClean);
      });
      if (!hasHeadword) {
        issueList.push(`[BOLDING TARGET MISMATCH] Headword '${headword}' not bolded in: ${ql}`);
        issues++;
      }
    }
  }
}

console.log('========================================');
console.log('Verification Audit for Finish Slice 3:');
console.log('Total notes checked:', checked);
console.log('Total issues found:', issues);
if (issueList.length > 0) {
  console.log('Sample issues (first 20):');
  issueList.slice(0, 20).forEach(i => console.log('  ', i));
} else {
  console.log('ALL 384 NOTES PERFECTLY COMPLIANT WITH STRICT STANDARDS!');
}
console.log('========================================');
process.exit(issues > 0 ? 1 : 0);
