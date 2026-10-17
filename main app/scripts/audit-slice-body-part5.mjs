import fs from 'fs';
import path from 'path';

const baseDir = path.resolve('App database/Greek roots/Cluster Body & Physiology');
const slice = JSON.parse(fs.readFileSync('main app/scripts/slice-body-part5.json', 'utf8'));

export function auditSlice(sliceIndices = null) {
  const problems = [];
  const list = sliceIndices 
    ? slice.map((p, idx) => ({ p, idx })).filter(item => sliceIndices.includes(item.idx))
    : slice.map((p, idx) => ({ p, idx }));

  for (const { p, idx } of list) {
    const fullPath = path.join(baseDir, p);
    if (!fs.existsSync(fullPath)) {
      problems.push({ idx, file: p, issues: ['File does not exist'] });
      continue;
    }
    const content = fs.readFileSync(fullPath, 'utf8');
    const issues = [];

    const statusPos = content.indexOf('> [!status]');
    const bookPos = content.indexOf('> [!book]');
    if (statusPos === -1) issues.push('Missing [!status] block');
    if (bookPos === -1) issues.push('Missing [!book] block');
    if (statusPos !== -1 && bookPos !== -1 && statusPos > bookPos) {
      issues.push('Status block is below [!book]');
    }

    const pMatch = content.match(/1\.\s*\*\*Primary Definition[^:]*\*\*:\s*([^\r\n]+)/);
    const sMatch = content.match(/2\.\s*\*\*Secondary \/ Nuanced Definition[^:]*\*\*:\s*([^\r\n]+)/);
    if (!pMatch) issues.push('Missing Primary Definition');
    if (!sMatch) issues.push('Missing Secondary Definition');
    if (pMatch && sMatch) {
      if (pMatch[1].trim().toLowerCase() === sMatch[1].trim().toLowerCase()) {
        issues.push('Duplicate Definition');
      }
    }

    if (!content.includes('> [!quote]')) {
      issues.push('Missing [!quote] section');
    } else {
      const quoteSection = content.split('> [!quote]')[1];
      const quoteLines = quoteSection.split('\n')
        .map(l => l.trim())
        .filter(l => l.startsWith('> - 📜') || l.startsWith('- 📜'));
      
      if (quoteLines.length < 3) {
        issues.push(`Only ${quoteLines.length} quotes (expected 3)`);
      }

      const authors = [];
      let hasPlaceholder = false;
      let hasUnbolded = false;

      for (const line of quoteLines) {
        if (/Academic Lexicon|Classic Author|Unknown Author|Placeholder/i.test(line)) {
          hasPlaceholder = true;
        }
        const authMatch = line.match(/-\s*📜\s*\*\*([^*(:]+)/);
        if (authMatch) {
          authors.push(authMatch[1].trim());
        }
        // Check if there is bold text inside the quotation
        const quoteTextMatch = line.match(/"([^"]+)"/);
        if (quoteTextMatch) {
          if (!quoteTextMatch[1].includes('**')) {
            hasUnbolded = true;
          }
        } else if (!line.includes('**')) {
          hasUnbolded = true;
        }
      }

      if (hasPlaceholder) issues.push('Contains placeholder author');
      if (new Set(authors).size < quoteLines.length) {
        issues.push(`Duplicate authors: ${authors.join(', ')}`);
      }
      if (hasUnbolded) {
        issues.push('Quotation missing bold target word');
      }
    }

    if (issues.length > 0) {
      problems.push({ idx, file: p, issues });
    }
  }
  return problems;
}

if (process.argv[1] && process.argv[1].endsWith('audit-slice-body-part5.mjs')) {
  const problems = auditSlice();
  console.log(`Audited ${slice.length} files in slice-body-part5. Problems found: ${problems.length}`);
  if (problems.length > 0) {
    console.log('Sample problems (first 5):');
    problems.slice(0, 5).forEach(p => console.log(`[${p.idx}] ${p.file}: ${p.issues.join('; ')}`));
  }
}
