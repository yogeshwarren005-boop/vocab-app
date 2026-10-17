import fs from 'fs';
import path from 'path';

const baseClusterDir = path.resolve('App database/Greek roots/Cluster Body & Physiology');
const slicePath = 'main app/scripts/slice-body-part2.json';
const slice = JSON.parse(fs.readFileSync(slicePath, 'utf8'));

const badAuthorPatterns = [
  /academic lexicon/i,
  /classic author/i,
  /unknown/i,
  /anonymous/i,
  /various/i,
  /etymological lexicon/i,
  /dictionary of/i,
  /standard consensus/i
];

let errors = 0;
let checked = 0;

for (const relPath of slice) {
  const filePath = path.join(baseClusterDir, relPath);
  if (!fs.existsSync(filePath)) {
    console.error(`[ERROR] File missing: ${relPath}`);
    errors++;
    continue;
  }
  const content = fs.readFileSync(filePath, 'utf8');

  // Check frontmatter
  if (!content.startsWith('---')) {
    console.error(`[ERROR] Missing frontmatter in: ${relPath}`);
    errors++;
  }

  // Check status toggle block
  if (!content.includes('> [!status] 🎯 **Status:**') || !content.includes('```dataviewjs')) {
    console.error(`[ERROR] Missing status toggle block in: ${relPath}`);
    errors++;
  }

  // Check book definition block
  if (!content.includes('> [!book] 📖 Definitions & Semantic Range')) {
    console.error(`[ERROR] Missing book block in: ${relPath}`);
    errors++;
  }
  if (!content.includes('> 1. **Primary Definition (Lexical / Standard Consensus)**:')) {
    console.error(`[ERROR] Missing primary definition in: ${relPath}`);
    errors++;
  }
  if (!content.includes('> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**:')) {
    console.error(`[ERROR] Missing secondary definition in: ${relPath}`);
    errors++;
  }

  // Check quote block
  const quoteSection = content.split('> [!quote] 💬 Contextual Usage & Authentic Quotations\n')[1];
  if (!quoteSection) {
    console.error(`[ERROR] Missing quote section in: ${relPath}`);
    errors++;
    continue;
  }

  const quoteLines = quoteSection.trim().split('\n').filter(l => l.startsWith('> - 📜'));
  if (quoteLines.length !== 3) {
    console.error(`[ERROR] Expected 3 quotes, got ${quoteLines.length} in: ${relPath}`);
    errors++;
  }

  const authors = [];
  for (const line of quoteLines) {
    const match = line.match(/^> - 📜 \*\*(.+?)\s+\(\*(.+?)\*\):\*\*\s+\*"(.*)"\*$/);
    if (!match) {
      console.error(`[ERROR] Malformed quote line in: ${relPath}\n  Line: ${line}`);
      errors++;
      continue;
    }
    const [, author, work, quoteText] = match;
    authors.push(author.trim().toLowerCase());

    for (const pat of badAuthorPatterns) {
      if (pat.test(author)) {
        console.error(`[ERROR] Placeholder author '${author}' in: ${relPath}`);
        errors++;
      }
    }

    if (!quoteText.includes('**')) {
      console.error(`[ERROR] No bolded word in quote text in: ${relPath}\n  Quote: ${quoteText}`);
      errors++;
    }
  }

  if (new Set(authors).size !== quoteLines.length) {
    console.error(`[ERROR] Duplicate authors found in: ${relPath} (${authors.join(', ')})`);
    errors++;
  }

  checked++;
}

console.log(`Validation complete. Checked ${checked}/${slice.length} files. Total errors found: ${errors}`);
if (errors > 0) {
  process.exit(1);
}
