import fs from 'fs';
import path from 'path';

const DB_ROOT = path.resolve('../App database');

function parseQuoteLine(clean) {
  // Line format:
  // **Author (*Work*):** *"Quote..."*
  // **Author (*Work (Subtitle)*):** *"Quote..."*
  // **Author (Work):** "Quote..."
  // **Author:** "Quote..."

  const headerQuoteMatch = clean.match(/^\*\*([\s\S]+?)\*\*:?\s*\*?["“]([\s\S]+?)["”]\*?$/) ||
                           clean.match(/^\*\*([\s\S]+?)\*\*:?\s*\*?["“]([\s\S]+)$/);

  if (headerQuoteMatch) {
    let rawHeader = headerQuoteMatch[1].trim();
    rawHeader = rawHeader.replace(/[:*]+$/, '').trim();

    const quoteText = (headerQuoteMatch[2] || '').replace(/["”*]+$/g, '').trim();

    const parenMatch = rawHeader.match(/^(.+?)\s*\(\*?([\s\S]+?)\*?\)$/);

    if (parenMatch) {
      const author = parenMatch[1].replace(/[:*]/g, '').trim();
      const work = parenMatch[2].replace(/[:*]/g, '').trim();
      return { author, work, quote: quoteText };
    } else {
      const author = rawHeader.replace(/[:*]/g, '').trim();
      return { author, work: '', quote: quoteText };
    }
  }

  const qm = clean.match(/["“]([^"”]+)["”]/);
  if (qm) {
    return { author: '', work: '', quote: qm[1].trim() };
  }

  return null;
}

// Read the files that had missing author/work in previous run
const filesToTest = [
  'Latin roots/Cluster Action/Dashboard — fac/fictionalization.md',
  'Latin roots/Cluster Action/Dashboard — fict/fictionalization.md',
  'Latin roots/Cluster Action/Dashboard — lav/elavil.md',
  'Latin roots/Cluster Action/Dashboard — orn/ornery.md',
  'Latin roots/Cluster Animal & Plant/Dashboard — avi/aviary.md',
  'Latin roots/Cluster Animal & Plant/Dashboard — avi/avitaminosis.md',
  'Latin roots/Cluster Animal & Plant/Dashboard — can_dog/cannoneer.md',
  'Latin roots/Cluster Animal & Plant/Dashboard — can_dog/canonization.md',
  'Latin roots/Cluster Animal & Plant/Dashboard — can_dog/canuck.md',
  'Latin roots/Cluster Animal & Plant/Dashboard — can_dog/uncanny.md'
];

for (const rel of filesToTest) {
  const full = path.join(DB_ROOT, rel);
  const content = fs.readFileSync(full, 'utf8');
  const lines = content.split(/\r?\n/);
  let inQuote = false;
  console.log(`\n--- Testing ${path.basename(rel)} ---`);
  for (const line of lines) {
    if (line.match(/>\s*\[!(?:quote|cite|example|citation)[^\]]*\]/i)) {
      inQuote = true;
      continue;
    } else if (line.match(/>\s*\[!/i) || (!line.startsWith('>') && line.trim().startsWith('#'))) {
      inQuote = false;
    }
    if (inQuote) {
      const clean = line.replace(/^>\s*-\s*(?:📜|📚|🔬|🌐|🗣️|💬)?\s*/, '').replace(/^>\s*/, '').trim();
      if (!clean) continue;
      const res = parseQuoteLine(clean);
      if (res) {
        console.log(`  ✓ Author: "${res.author}" | Work: "${res.work}" | Quote: "${res.quote.slice(0, 35)}..."`);
      } else {
        console.log(`  ❌ Failed line: ${clean}`);
      }
    }
  }
}
