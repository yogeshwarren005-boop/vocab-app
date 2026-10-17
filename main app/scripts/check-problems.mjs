import fs from 'fs';
import path from 'path';

const targetDir = 'App database/Greek roots/Cluster Action';

function walk(dir) {
  let res = [];
  const entries = fs.readdirSync(dir, { withFileTypes: true });
  for (const ent of entries) {
    const full = path.join(dir, ent.name);
    if (ent.isDirectory()) {
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
const problems = [];
for (const filePath of files) {
  const content = fs.readFileSync(filePath, 'utf8');
  let issues = [];

  const statusPos = content.indexOf('> [!status]');
  const bookPos = content.indexOf('> [!book]');
  if (statusPos === -1 || bookPos === -1 || statusPos > bookPos) issues.push('status');

  const pMatch = content.match(/1\.\s*\*\*([^*]+)\*\*:\s*([^\r\n]+)/);
  const sMatch = content.match(/2\.\s*\*\*([^*]+)\*\*:\s*([^\r\n]+)/);
  if (!pMatch || !sMatch || (pMatch && sMatch && pMatch[2].trim().toLowerCase() === sMatch[2].trim().toLowerCase())) issues.push('def');

  const quoteSection = content.split('> [!quote]')[1];
  if (!quoteSection) {
    issues.push('quote');
  } else {
    const lines = quoteSection.split('\n').filter(l => l.trim().match(/^(?:>\s*)?-\s*📜/));
    if (lines.length < 3) issues.push('num_quotes');
    let authors = [];
    let hasPlaceholder = false;
    for (const line of lines) {
      if (line.includes('Academic Lexicon')) hasPlaceholder = true;
      const authMatch = line.match(/-\s*📜\s*\*\*([^*(:]+)/);
      if (authMatch) authors.push(authMatch[1].trim());
    }
    if (hasPlaceholder) issues.push('placeholder');
    if (new Set(authors).size < lines.length) issues.push('dup_author');
  }

  if (issues.length > 0) {
    problems.push(path.relative(targetDir, filePath).replace(/\\/g, '/'));
  }
}

console.log("Current problems count:", problems.length);
if (fs.existsSync('main app/scripts/action-remaining-problems.json')) {
  const saved = JSON.parse(fs.readFileSync('main app/scripts/action-remaining-problems.json', 'utf8'));
  console.log("Saved problems count:", saved.length);
  const diff = problems.filter(p => !saved.includes(p));
  console.log("Problems in audit but not in saved:", diff);
}
