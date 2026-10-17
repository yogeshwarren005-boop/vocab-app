import fs from 'fs';
import path from 'path';

const DB_ROOT = path.resolve('../App database');

function cleanDefinitionText(raw) {
  if (!raw) return '';
  return raw
    .replace(/\[\[|\]\]/g, '')
    .replace(/;\s*;\s*-\s*[a-zA-Z\s.-]+$/g, '')
    .replace(/;\s*-\s*[a-zA-Z\s.-]+$/g, '')
    .replace(/;\s*;+/g, ';')
    .trim();
}

function extractCardDetails(rawContent, filePath) {
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

// Collect all 50,630 word cards exactly as defined in the tree
console.log('Auditing card details parsing on all 50,630 words...');
const wordCards = [];

for (const pillar of ['Latin roots', 'Greek roots']) {
  const pillarDir = path.join(DB_ROOT, pillar);
  if (!fs.existsSync(pillarDir)) continue;
  const clusters = fs.readdirSync(pillarDir, { withFileTypes: true });
  for (const c of clusters) {
    if (c.isDirectory() && c.name.startsWith('Cluster ')) {
      const clusterPath = path.join(pillarDir, c.name);
      const subs = fs.readdirSync(clusterPath, { withFileTypes: true });
      for (const s of subs) {
        if (s.isDirectory() && s.name.startsWith('Dashboard — ')) {
          const dashPath = path.join(clusterPath, s.name);
          const words = fs.readdirSync(dashPath, { withFileTypes: true });
          for (const w of words) {
            if (w.isFile() && w.name.endsWith('.md')) {
              // Note: Dashboard — <root>.md and Word Triage — <root>.md are study files inside this dir
              const isStudy = w.name.startsWith('Dashboard — ') || w.name.startsWith('Word Triage — ');
              if (!isStudy) {
                wordCards.push({
                  pillar,
                  cluster: c.name,
                  dash: s.name,
                  name: w.name,
                  rel: `${pillar}/${c.name}/${s.name}/${w.name}`,
                  full: path.join(dashPath, w.name)
                });
              }
            }
          }
        }
      }
    }
  }
}

const vocabDir = path.join(DB_ROOT, 'English vocabulary master');
if (fs.existsSync(vocabDir)) {
  const clusters = fs.readdirSync(vocabDir, { withFileTypes: true });
  for (const c of clusters) {
    if (c.isDirectory() && c.name.startsWith('Cluster ')) {
      const clusterPath = path.join(vocabDir, c.name);
      const subs = fs.readdirSync(clusterPath, { withFileTypes: true });
      for (const s of subs) {
        if (s.isFile() && s.name.endsWith('.md') && !s.name.startsWith('Cluster ') && !s.name.startsWith('Semantic Field — ')) {
          wordCards.push({
            pillar: 'English vocabulary master',
            cluster: c.name,
            dash: 'N/A',
            name: s.name,
            rel: `English vocabulary master/${c.name}/${s.name}`,
            full: path.join(clusterPath, s.name)
          });
        }
      }
    }
  }
}

console.log(`Total word cards to audit: ${wordCards.length}`);

let defMissing = [];
let secondaryDefMissing = [];
let quotesMissing = [];
let lessThan3Quotes = [];
let authorMissingInQuote = [];

const startTime = Date.now();
for (let i = 0; i < wordCards.length; i++) {
  const card = wordCards[i];
  const content = fs.readFileSync(card.full, 'utf8');
  const details = extractCardDetails(content, card.rel);

  if (!details.primaryDef) {
    defMissing.push(card.rel);
  }
  if (!details.secondaryDef) {
    secondaryDefMissing.push(card.rel);
  }
  if (details.quotes.length === 0) {
    quotesMissing.push(card.rel);
  } else if (details.quotes.length < 3) {
    lessThan3Quotes.push({ file: card.rel, count: details.quotes.length });
  }

  for (const q of details.quotes) {
    if (!q.author || !q.work) {
      authorMissingInQuote.push({ file: card.rel, quote: q });
    }
  }

  if ((i + 1) % 10000 === 0) {
    console.log(`Audited ${i + 1} / ${wordCards.length} cards... (${((Date.now() - startTime) / 1000).toFixed(1)}s)`);
  }
}

console.log(`\nAudit Complete in ${((Date.now() - startTime) / 1000).toFixed(1)}s!`);
console.log(`Total Word Cards: ${wordCards.length}`);
console.log(`Definitions Parsed: ${wordCards.length - defMissing.length} / ${wordCards.length} (${((wordCards.length - defMissing.length) / wordCards.length * 100).toFixed(2)}%)`);
console.log(`Missing Primary Defs: ${defMissing.length}`);
if (defMissing.length > 0) console.log('Sample missing defs:', defMissing.slice(0, 10));

console.log(`Secondary Defs Parsed: ${wordCards.length - secondaryDefMissing.length} / ${wordCards.length} (${((wordCards.length - secondaryDefMissing.length) / wordCards.length * 100).toFixed(2)}%)`);
if (secondaryDefMissing.length > 0) console.log('Sample missing secondary defs:', secondaryDefMissing.slice(0, 10));

console.log(`Full 3-Quote Stacks: ${wordCards.length - lessThan3Quotes.length - quotesMissing.length} / ${wordCards.length} (${((wordCards.length - lessThan3Quotes.length - quotesMissing.length) / wordCards.length * 100).toFixed(2)}%)`);
console.log(`Notes with 0 Quotes: ${quotesMissing.length}`);
if (quotesMissing.length > 0) console.log('Sample 0 quotes:', quotesMissing.slice(0, 10));
console.log(`Notes with < 3 Quotes: ${lessThan3Quotes.length}`);
if (lessThan3Quotes.length > 0) console.log('Sample < 3 quotes:', lessThan3Quotes.slice(0, 10));
console.log(`Quotes with missing author/work: ${authorMissingInQuote.length}`);
if (authorMissingInQuote.length > 0) console.log('Sample quotes missing author/work:', authorMissingInQuote.slice(0, 10));
