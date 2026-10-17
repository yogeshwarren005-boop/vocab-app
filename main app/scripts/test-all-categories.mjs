import fs from 'fs';
import path from 'path';

const index = JSON.parse(fs.readFileSync('public/data/vault-index.json', 'utf8'));

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

        const m = clean.match(/^\*\*([^*]+?)(?:\s*\(([^)]+)\))?:?\*\*:?\s*\*?["“]([^"”]+)["”]\*?/);
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

  return { primaryDef, secondaryDef, quotes };
}

// Sample across Latin, Greek, and EVM
const greekSample = '../App database/Greek roots/Cluster Action/Dashboard — actin/actin.md';
const evmSample = '../App database/English vocabulary master/Cluster Beauty and Ugliness/bonny.md';

console.log('Greek actin:');
console.log(extractCardDetails({ category: 'greek' }, fs.readFileSync(greekSample, 'utf8')));

console.log('\nEVM bonny:');
console.log(extractCardDetails({ category: 'vocab' }, fs.readFileSync(evmSample, 'utf8')));
