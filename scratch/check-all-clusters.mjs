import fs from 'fs';
import path from 'path';

const baseDir = 'App database/Latin roots';

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

function auditCluster(clusterPath) {
  const files = walk(clusterPath);
  let problemCount = 0;

  for (const filePath of files) {
    const content = fs.readFileSync(filePath, 'utf8');
    let hasIssue = false;

    // 1. Frontmatter
    if (!content.startsWith('---')) {
      hasIssue = true;
    } else {
      const fmEnd = content.indexOf('---', 3);
      if (fmEnd === -1) {
        hasIssue = true;
      } else {
        const fm = content.slice(0, fmEnd);
        if (!fm.includes('latin_root:') || !fm.includes('cluster:') || !fm.includes('status:')) {
          hasIssue = true;
        }
      }
    }

    // 2. Status toggle
    const statusPos = content.indexOf('> [!status]');
    const bookPos = content.indexOf('> [!book]');
    if (statusPos === -1 || bookPos === -1 || statusPos > bookPos) hasIssue = true;
    if (!content.includes('apple-toggle-css') || !content.includes('apple-c')) hasIssue = true;

    // 3. Definitions
    const pMatch = content.match(/1\.\s*\*\*([^*]+)\*\*:\s*([^\r\n]+)/);
    const sMatch = content.match(/2\.\s*\*\*([^*]+)\*\*:\s*([^\r\n]+)/);
    if (!pMatch || !sMatch) {
      hasIssue = true;
    } else {
      const pText = pMatch[2].trim();
      const sText = sMatch[2].trim();
      if (pText.length < 25 || sText.length < 25) hasIssue = true;
      if (/\b(?:the\s+)?(?:quality|state|condition)(?:,\s*state)?(?:,\s*or\s*degree)?\s+of\s+being\b/i.test(pText)) hasIssue = true;
      if (/\b(?:the\s+)?(?:quality|state|condition)(?:,\s*state)?(?:,\s*or\s*degree)?\s+of\s+being\b/i.test(sText)) hasIssue = true;
      if (pText.toLowerCase() === sText.toLowerCase()) hasIssue = true;
    }

    // 4. Boilerplate
    for (const phrase of knownBannedPhrases) {
      if (content.includes(phrase)) hasIssue = true;
    }

    // 5. Quotes
    const quoteSection = content.split('> [!quote]')[1];
    if (!quoteSection) {
      hasIssue = true;
    } else {
      const quoteLines = quoteSection
        .split('\n')
        .map(l => l.trim())
        .filter(l => l.startsWith('>') && l.includes('📜'));
      if (quoteLines.length !== 3) {
        hasIssue = true;
      } else {
        let authors = [];
        for (const qLine of quoteLines) {
          const authMatch = qLine.match(/📜\s*\*\*([^*]+?)\s*(?:\(\*([^*]+?)\*\):?\*\*|\*\*\s*\(\*([^*]+?)\*\):?)/);
          if (!authMatch) {
            hasIssue = true;
          } else {
            authors.push(authMatch[1].trim());
          }
          const colonMatch = qLine.match(/:\*\*\s*(.+)$/);
          const quoteBody = colonMatch ? colonMatch[1] : qLine;
          if (!quoteBody.includes('**')) hasIssue = true;
        }
        if (new Set(authors).size < quoteLines.length) hasIssue = true;
      }
    }

    if (hasIssue) problemCount++;
  }

  return { total: files.length, problems: problemCount, pristine: files.length - problemCount };
}

const entries = fs.readdirSync(baseDir, { withFileTypes: true });
const clusters = entries.filter(e => e.isDirectory() && e.name.startsWith('Cluster ')).map(e => e.name).sort();

console.log(`Checking ${clusters.length} clusters...\n`);
let totalVaultWords = 0;
let totalVaultProblems = 0;
let passedClusters = [];
let remainingClusters = [];

for (const c of clusters) {
  const cPath = path.join(baseDir, c);
  const res = auditCluster(cPath);
  totalVaultWords += res.total;
  totalVaultProblems += res.problems;
  if (res.problems === 0) {
    passedClusters.push({ name: c, ...res });
  } else {
    remainingClusters.push({ name: c, ...res });
  }
}

console.log(`========================================`);
console.log(`VAULT AUDIT SUMMARY:`);
console.log(`Total Clusters: ${clusters.length}`);
console.log(`100% PRISTINE Clusters: ${passedClusters.length}`);
console.log(`Remaining Clusters: ${remainingClusters.length}`);
console.log(`Total Notes: ${totalVaultWords}`);
console.log(`Total Pristine Notes: ${totalVaultWords - totalVaultProblems}`);
console.log(`Total Problem Notes: ${totalVaultProblems}`);
console.log(`========================================\n`);

console.log(`REMAINING CLUSTERS (sorted by total word count ascending):`);
remainingClusters.sort((a, b) => a.total - b.total);
for (const r of remainingClusters) {
  console.log(`- ${r.name.padEnd(35)} : ${r.total.toString().padStart(4)} words | ${r.problems.toString().padStart(4)} problems`);
}
