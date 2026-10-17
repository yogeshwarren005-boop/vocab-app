import fs from 'fs';
import path from 'path';

const targetDir = 'App database/Greek roots/Cluster Action';
const batches = JSON.parse(fs.readFileSync('main app/scripts/action-batches.json', 'utf8'));
const batch3 = batches[2];

for (const item of batch3) {
  const filePath = path.join(targetDir, item.relPath);
  const content = fs.readFileSync(filePath, 'utf8');
  const issues = [];

  const statusPos = content.indexOf('> [!status]');
  const bookPos = content.indexOf('> [!book]');
  if (statusPos === -1) issues.push('Missing [!status] block');
  if (bookPos === -1) issues.push('Missing [!book] block');
  if (statusPos !== -1 && bookPos !== -1 && statusPos > bookPos) issues.push('Status block is below [!book]');

  const pMatch = content.match(/1\.\s*\*\*([^*]+)\*\*:\s*([^\r\n]+)/);
  const sMatch = content.match(/2\.\s*\*\*([^*]+)\*\*:\s*([^\r\n]+)/);
  if (!pMatch) issues.push('Missing Primary Definition');
  if (!sMatch) issues.push('Missing Secondary Definition');
  if (pMatch && sMatch && pMatch[2].trim().toLowerCase() === sMatch[2].trim().toLowerCase()) {
    issues.push('Duplicate Definition (Primary == Secondary)');
  }

  const quoteSection = content.split('> [!quote]')[1];
  if (!quoteSection) {
    issues.push('Missing [!quote] section');
  } else {
    const lines = quoteSection.split('\n').filter(l => l.trim().match(/^(?:>\s*)?-\s*📜/));
    if (lines.length < 3) issues.push(`Only ${lines.length} quotes`);
    let authors = [];
    let hasPlaceholder = false;
    for (const line of lines) {
      if (line.includes('Academic Lexicon')) hasPlaceholder = true;
      const authMatch = line.match(/-\s*📜\s*\*\*([^*(:]+)/);
      if (authMatch) authors.push(authMatch[1].trim());
    }
    if (hasPlaceholder) issues.push('Placeholder author');
    if (new Set(authors).size < lines.length) issues.push(`Duplicate author: ${authors.join(', ')}`);
  }

  if (issues.length > 0) {
    console.log(`ISSUE: ${item.relPath} -> ${issues.join('; ')}`);
  }
}
console.log('Batch 3 check finished.');
