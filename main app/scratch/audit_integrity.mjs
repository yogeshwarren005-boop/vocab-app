import fs from 'fs';
import path from 'path';

const DB_ROOT = path.resolve('../App database');

// Import or copy exact extractCardDetails & cleanDefinitionText from mobile-app.js
function cleanDefinitionText(raw) {
  if (!raw) return '';
  return raw
    .replace(/\[\[|\]\]/g, '')
    .replace(/;\s*;\s*-\s*[a-zA-Z\s.-]+$/g, '')
    .replace(/;\s*-\s*[a-zA-Z\s.-]+$/g, '')
    .replace(/;\s*;+/g, ';')
    .trim();
}

function extractCardDetails(card, rawContent) {
  let primaryDef = '';
  let secondaryDef = '';
  let pos = '';
  const quotes = [];

  if (rawContent) {
    const fmMatch = rawContent.match(/^---\r?\n([\s\S]*?)\r?\n---/);
    if (fmMatch) {
      const posMatch = fmMatch[1].match(/(?:pos|part_of_speech)\s*:\s*["']?([A-Za-z]+)["']?/i);
      if (posMatch) pos = posMatch[1].toLowerCase();
    }

    const lines = rawContent.split(/\r?\n/);
    let currentSection = null;

    for (let i = 0; i < lines.length; i++) {
      const line = lines[i];

      if (line.match(/>\s*\[!(?:book|definition|summary|note|lexicon|meaning)[^\]]*\]/i)) {
        currentSection = 'def';
        continue;
      } else if (line.match(/>\s*\[!(?:quote|cite|example|citation)[^\]]*\]/i)) {
        currentSection = 'quote';
        continue;
      } else if (line.match(/>\s*\[!/i) || (!line.startsWith('>') && line.trim().startsWith('#'))) {
        currentSection = null;
      }

      if (currentSection === 'def') {
        const clean = line.replace(/^>\s*(?:-\s*)?/, '').trim();
        if (!clean) continue;

        const pMatch = clean.match(/(?:1\.\s*)?\*\*(?:1\.\s*)?(?:Primary|Concise)[^*]*\*\*:\s*(.*)/i);
        if (pMatch && !primaryDef) {
          primaryDef = cleanDefinitionText(pMatch[1]);
        }

        const sMatch = clean.match(/(?:2\.\s*)?\*\*(?:2\.\s*)?(?:Secondary|Nuanced|Nuance)[^*]*\*\*:\s*(.*)/i);
        if (sMatch && !secondaryDef) {
          secondaryDef = cleanDefinitionText(sMatch[1]);
        }

        if (!primaryDef && clean.startsWith('1.')) {
          primaryDef = cleanDefinitionText(clean.replace(/^1\.\s*/, '').replace(/\*\*[^*]+\*\*:\s*/, ''));
        }
      } else if (currentSection === 'quote') {
        const clean = line.replace(/^>\s*-\s*(?:📜|📚|🔬|🌐|🗣️|💬)?\s*/, '').replace(/^>\s*/, '').trim();
        if (!clean) continue;

        const m = clean.match(/^\*\*([^*]+?)\s*\(\*?([^*)]+?)\*?\):?\*\*:?\s*\*?["“]([^"”]+)["”]\*?/) ||
                  clean.match(/^\*\*([^*]+?)(?:\s*\(([^)]+)\))?:?\*\*:?\s*\*?["“]([^"”]+)["”]\*?/);
        if (m) {
          const author = (m[1] || '').replace(/[:*]/g, '').trim();
          const work = (m[2] || '').replace(/[:*]/g, '').trim();
          quotes.push({ author, work, quote: m[3].trim() });
        } else {
          const qm = clean.match(/["“]([^"”]+)["”]/);
          if (qm) {
            quotes.push({ author: '', work: '', quote: qm[1].trim() });
          }
        }
      }
    }

    if (!primaryDef) {
      const lineMatch = rawContent.match(/\*\*Definition:\*\*\s*([^\n]+)/i) || rawContent.match(/#+\s*Definition\s*\n+([^\n#]+)/i);
      if (lineMatch) primaryDef = cleanDefinitionText(lineMatch[1]);
    }
  }

  return { primaryDef, secondaryDef, quotes, pos };
}

console.log('--- SCANNING ALL FILES IN APP DATABASE ---');

const allFiles = [];
function walk(dir, relDir = '') {
  const entries = fs.readdirSync(dir, { withFileTypes: true });
  for (const e of entries) {
    const full = path.join(dir, e.name);
    const rel = relDir ? `${relDir}/${e.name}` : e.name;
    if (e.isDirectory()) {
      walk(full, rel);
    } else if (e.isFile()) {
      allFiles.push({ full, rel, name: e.name });
    }
  }
}

walk(DB_ROOT);
console.log(`Total files discovered: ${allFiles.length}`);

// Audit frontmatter and markdown corruption
let zeroByteFiles = [];
let utf8Errors = [];
let brokenYamlFiles = [];
let missingFrontmatterFiles = [];

const mdFiles = allFiles.filter(f => f.name.endsWith('.md'));
console.log(`Total markdown files: ${mdFiles.length}`);

for (const f of mdFiles) {
  let content = '';
  try {
    content = fs.readFileSync(f.full, 'utf8');
  } catch (err) {
    utf8Errors.push({ file: f.rel, err: err.message });
    continue;
  }

  if (content.length === 0) {
    zeroByteFiles.push(f.rel);
    continue;
  }

  // Check YAML frontmatter
  if (!content.startsWith('---')) {
    missingFrontmatterFiles.push(f.rel);
  } else {
    const closingIdx = content.indexOf('\n---', 3);
    if (closingIdx === -1) {
      brokenYamlFiles.push({ file: f.rel, reason: 'Unclosed frontmatter (missing closing ---)' });
    } else {
      const fmContent = content.substring(3, closingIdx);
      // Basic check of YAML key-value pairs
      const lines = fmContent.split(/\r?\n/).filter(l => l.trim() && !l.trim().startsWith('#'));
      for (const line of lines) {
        if (!line.includes(':') && !line.startsWith('- ') && !line.startsWith('  ')) {
          brokenYamlFiles.push({ file: f.rel, reason: `Invalid YAML line: "${line}"` });
          break;
        }
      }
    }
  }
}

console.log(`\nAudit Results for Markdown Integrity:`);
console.log(`- 0-byte files: ${zeroByteFiles.length}`);
if (zeroByteFiles.length > 0) console.log(zeroByteFiles.slice(0, 10));
console.log(`- UTF-8 Read Errors: ${utf8Errors.length}`);
console.log(`- Missing Frontmatter: ${missingFrontmatterFiles.length}`);
if (missingFrontmatterFiles.length > 0) console.log('Sample missing frontmatter:', missingFrontmatterFiles.slice(0, 10));
console.log(`- Broken YAML Frontmatter: ${brokenYamlFiles.length}`);
if (brokenYamlFiles.length > 0) console.log('Sample broken YAML:', brokenYamlFiles.slice(0, 10));

