import fs from 'fs';
import path from 'path';

const targetDir = process.argv[2] || 'App database/Latin roots/Cluster Action/Dashboard — act';

function walk(dir) {
  let res = [];
  const entries = fs.readdirSync(dir, { withFileTypes: true });
  for (const ent of entries) {
    const full = path.join(dir, ent.name);
    if (ent.isDirectory()) {
      if (ent.name === '03_Reference_and_Rules') continue;
      res.push(...walk(full));
    } else if (
      ent.name.endsWith('.md') &&
      !ent.name.startsWith('Dashboard —') &&
      !ent.name.startsWith('Word Triage —') &&
      !ent.name.startsWith('Cluster') &&
      !ent.name.startsWith('Semantic Field')
    ) {
      res.push(full);
    }
  }
  return res;
}

const files = walk(targetDir);
console.log(`========================================`);
console.log(`Enhanced Audit: Auditing ${files.length} word notes in:`);
console.log(`Target: ${targetDir}`);
console.log(`========================================\n`);

let problemCount = 0;
const knownBannedPhrases = [
  'In specialized and domain usage, denoting specific qualities',
  'In technical and systematic terminology, the action',
  'In functional and operational contexts, an agent',
  'The clinical presentation of',
  'Every pathological manifestation of',
  'The gradual evolutionary modification of',
  'In academic literature,',
  'Academic Lexicon',
  'Classic Author'
];

for (const filePath of files) {
  const content = fs.readFileSync(filePath, 'utf8');
  const fileName = path.basename(filePath);
  const word = fileName.replace('.md', '').toLowerCase().trim();
  
  let issues = [];

  // 1. Frontmatter
  if (!content.startsWith('---')) {
    issues.push('Missing frontmatter delimiter ---');
  } else {
    const fmEnd = content.indexOf('---', 3);
    if (fmEnd === -1) {
      issues.push('Unclosed frontmatter');
    } else {
      const fm = content.slice(0, fmEnd);
      if (!fm.includes('latin_root:')) issues.push('Frontmatter missing latin_root');
      if (!fm.includes('cluster:')) issues.push('Frontmatter missing cluster');
      if (!fm.includes('status:')) issues.push('Frontmatter missing status');
    }
  }

  // 2. Status toggle position and structure
  const statusPos = content.indexOf('> [!status]');
  const bookPos = content.indexOf('> [!book]');
  if (statusPos === -1) issues.push('Missing > [!status] block');
  if (bookPos === -1) issues.push('Missing > [!book] block');
  if (statusPos !== -1 && bookPos !== -1 && statusPos > bookPos) {
    issues.push('Status block must be positioned directly ABOVE > [!book]');
  }
  if (!content.includes('apple-toggle-css') || !content.includes('apple-c')) {
    issues.push('Missing Apple Glide Toggle DataviewJS code block');
  }

  // 3. Definitions Check
  const pMatch = content.match(/1\.\s*\*\*([^*]+)\*\*:\s*([^\r\n]+)/);
  const sMatch = content.match(/2\.\s*\*\*([^*]+)\*\*:\s*([^\r\n]+)/);
  if (!pMatch) {
    issues.push('Missing Primary Definition');
  } else {
    const pText = pMatch[2].trim();
    if (pText.length < 25) issues.push(`Primary definition too short (${pText.length} chars)`);
    if (/\b(?:the\s+)?(?:quality|state|condition)(?:,\s*state)?(?:,\s*or\s*degree)?\s+of\s+being\b/i.test(pText)) {
      issues.push(`Primary definition contains circular boilerplate formula ("quality/state of being...")`);
    }
  }

  if (!sMatch) {
    issues.push('Missing Secondary Definition');
  } else {
    const sText = sMatch[2].trim();
    if (sText.length < 25) issues.push(`Secondary definition too short (${sText.length} chars)`);
    if (/\b(?:the\s+)?(?:quality|state|condition)(?:,\s*state)?(?:,\s*or\s*degree)?\s+of\s+being\b/i.test(sText)) {
      issues.push(`Secondary definition contains circular boilerplate formula ("quality/state of being...")`);
    }
  }

  if (pMatch && sMatch) {
    const pText = pMatch[2].trim().toLowerCase();
    const sText = sMatch[2].trim().toLowerCase();
    if (pText === sText) {
      issues.push('Duplicate Definition (Primary == Secondary)');
    } else {
      // Token Jaccard check
      const pTokens = new Set(pText.match(/\w+/g) || []);
      const sTokens = new Set(sText.match(/\w+/g) || []);
      const intersect = new Set([...pTokens].filter(x => sTokens.has(x)));
      const union = new Set([...pTokens, ...sTokens]);
      const jaccard = intersect.size / Math.max(union.size, 1);
      if (jaccard >= 0.70) {
        issues.push(`Definitions excessively similar (Jaccard token overlap = ${jaccard.toFixed(2)})`);
      }
    }
  }

  // 4. Boilerplate / Template detection
  for (const phrase of knownBannedPhrases) {
    if (content.includes(phrase)) {
      issues.push(`Contains banned synthetic boilerplate / template phrase: "${phrase}"`);
    }
  }

  // 5. Quotes Check
  const quoteSection = content.split('> [!quote]')[1];
  if (!quoteSection) {
    issues.push('Missing > [!quote] section');
  } else {
    const quoteLines = quoteSection
      .split('\n')
      .map(l => l.trim())
      .filter(l => l.startsWith('>') && l.includes('📜'));

    if (quoteLines.length !== 3) {
      issues.push(`Expected exactly 3 quotes, found ${quoteLines.length}`);
    }

    let authors = [];
    for (const qLine of quoteLines) {
      // Match: > - 📜 **Author (*Work*):** or > - 📜 **Author** (*Work*):
      const authMatch = qLine.match(/📜\s*\*\*([^*]+?)\s*(?:\(\*([^*]+?)\*\):?\*\*|\*\*\s*\(\*([^*]+?)\*\):?)/);
      if (!authMatch) {
        issues.push(`Malformed citation format: "${qLine.slice(0, 60)}..."`);
      } else {
        const author = authMatch[1].trim();
        const work = (authMatch[2] || authMatch[3] || '').trim();
        authors.push(author);

        if (author.length < 3 || work.length < 2) {
          issues.push(`Suspiciously short author or work title: "${author}" / "${work}"`);
        }
      }

      // Check bolding in the passage text (after :**)
      const colonMatch = qLine.match(/:\*\*\s*(.+)$/);
      const quoteBody = colonMatch ? colonMatch[1] : qLine;
      if (!quoteBody.includes('**')) {
        issues.push(`Target word not bolded in quote: "${qLine.slice(0, 50)}..."`);
      }
    }

    const uniqueAuthors = new Set(authors);
    if (uniqueAuthors.size < quoteLines.length) {
      issues.push(`Duplicate author in quotes: (${authors.join(', ')})`);
    }
  }

  if (issues.length > 0) {
    problemCount++;
    console.log(`❌ ${path.relative(targetDir, filePath)}:`);
    issues.forEach(i => console.log(`   - ${i}`));
  }
}

console.log(`\n========================================`);
console.log(`Total words audited: ${files.length}`);
console.log(`Problem words: ${problemCount}`);
console.log(`Pristine words: ${files.length - problemCount}`);
console.log(`Audit Verdict: ${problemCount === 0 ? '✅ 100% PRISTINE (PASS)' : '❌ FAIL'}`);
console.log(`========================================`);

if (problemCount > 0) {
  process.exit(1);
} else {
  process.exit(0);
}
