import fs from 'fs';
import path from 'path';

const clusterDir = 'App database/Greek roots/Cluster Time & Chronology';
const dashboards = fs.readdirSync(clusterDir, { withFileTypes: true })
  .filter(d => d.isDirectory() && d.name.startsWith('Dashboard — '));

const problemsByDashboard = {};

for (const dash of dashboards) {
  const dashPath = path.join(clusterDir, dash.name);
  const files = fs.readdirSync(dashPath).filter(f => f.endsWith('.md'));
  for (const file of files) {
    const filePath = path.join(dashPath, file);
    const content = fs.readFileSync(filePath, 'utf8');

    let isProblem = false;
    const reasons = [];

    // Check 1: status before book
    const statusIdx = content.indexOf('> [!status]');
    const bookIdx = content.indexOf('> [!book]');
    if (statusIdx === -1 || bookIdx === -1 || statusIdx > bookIdx) {
      isProblem = true;
      reasons.push('status after book or missing');
    }

    // Check 2: definitions
    const def1Match = content.match(/> 1\.\s+\*\*Primary Definition[^*]*\*\*:\s*([^\n\r]+)/);
    const def2Match = content.match(/> 2\.\s+\*\*Secondary[^*]*\*\*:\s*([^\n\r]+)/);
    if (!def1Match || !def2Match) {
      isProblem = true;
      reasons.push('missing defs');
    } else if (def1Match[1].trim().toLowerCase() === def2Match[1].trim().toLowerCase()) {
      isProblem = true;
      reasons.push('duplicate defs');
    }

    // Check 3: quotes
    const quoteMatches = [...content.matchAll(/>\s*-\s*📜\s*\*\*([^*]+)\s*\(\*([^*]+)\*\)\:\*\*\s*(\*?"[^"]+"\*?)/g)];
    if (quoteMatches.length < 3) {
      isProblem = true;
      reasons.push(`only ${quoteMatches.length} quotes`);
    } else {
      const authors = quoteMatches.map(m => m[1].trim());
      if (new Set(authors).size < quoteMatches.length) {
        isProblem = true;
        reasons.push('duplicate author');
      }
      if (authors.some(a => a.toLowerCase().includes('academic lexicon') || a.toLowerCase().includes('classic author'))) {
        isProblem = true;
        reasons.push('placeholder author');
      }
    }

    if (isProblem) {
      if (!problemsByDashboard[dash.name]) {
        problemsByDashboard[dash.name] = [];
      }
      problemsByDashboard[dash.name].push({ file, reasons });
    }
  }
}

console.log('Problem summary by dashboard:');
let totalProblems = 0;
for (const [dash, list] of Object.entries(problemsByDashboard)) {
  console.log(`${dash}: ${list.length} problems`);
  totalProblems += list.length;
}
console.log(`Total problems: ${totalProblems}`);

fs.writeFileSync('main app/scripts/time-problems.json', JSON.stringify(problemsByDashboard, null, 2), 'utf8');
