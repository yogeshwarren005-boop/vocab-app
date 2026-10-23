/**
 * organize-dashboard-tables.mjs
 * Organizes Section 6 (Complete Derived Words Master List) in all root dashboards
 * into three distinct frequency tiers:
 *   - Tier 1: Words to Learn First (High Frequency)
 *   - Tier 2: Words to Learn Later (Elevated & Academic)
 *   - Tier 3: Words to Learn Last (Rare & Specialized)
 * 
 * Also enriches frontmatter with tier, tier_label, frequency_score, and tier word counts.
 */

import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { getWordFrequency, getRootFrequencyTier } from './frequency-engine.mjs';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT_DIR = path.resolve(__dirname, '..', '..');
const APP_DB = path.join(ROOT_DIR, 'App database');

console.log('🚀 Organizing root dashboard tables into 3 Frequency Tiers...');

function findDashboards(dir) {
  let list = [];
  try {
    for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
      const fullPath = path.join(dir, entry.name);
      if (entry.isDirectory()) {
        list = list.concat(findDashboards(fullPath));
      } else if (entry.name.startsWith('Dashboard — ') && entry.name.endsWith('.md')) {
        list.push(fullPath);
      }
    }
  } catch {}
  return list;
}

const allDashboards = [
  ...findDashboards(path.join(APP_DB, 'Greek roots')),
  ...findDashboards(path.join(APP_DB, 'Latin roots'))
];

console.log(`Found ${allDashboards.length} dashboards to process.`);

let processedCount = 0;
let modifiedCount = 0;

for (const filePath of allDashboards) {
  processedCount++;
  const raw = fs.readFileSync(filePath, 'utf8');

  // 1. Locate Section 6
  const s6Match = raw.match(/##\s+📚\s*6\.\s*Complete Derived Words Master List[^\n]*/i);
  if (!s6Match) continue;

  const s6Idx = s6Match.index;
  const beforeS6 = raw.slice(0, s6Idx + s6Match[0].length);
  const afterS6 = raw.slice(s6Idx + s6Match[0].length);

  // Parse table rows in afterS6
  const lines = afterS6.split(/\r?\n/);
  const tableRows = [];
  let lineIdx = 0;

  // Skip until table starts or next heading
  while (lineIdx < lines.length && !lines[lineIdx].trim().startsWith('|')) {
    if (lines[lineIdx].trim().startsWith('#')) break;
    lineIdx++;
  }

  // Collect table header and rows
  let headerSeen = false;
  let separatorSeen = false;
  let remainingContentLines = [];

  for (; lineIdx < lines.length; lineIdx++) {
    const line = lines[lineIdx];
    const trimmed = line.trim();

    if (trimmed.startsWith('#') && !trimmed.startsWith('### ⭐') && !trimmed.startsWith('### 📈') && !trimmed.startsWith('### 🏛️')) {
      remainingContentLines = lines.slice(lineIdx);
      break;
    }

    if (trimmed.startsWith('|')) {
      if (!headerSeen) {
        headerSeen = true;
        continue;
      }
      if (!separatorSeen && trimmed.includes('---')) {
        separatorSeen = true;
        continue;
      }

      // Check if it's a data row
      const cells = trimmed.split('|').map(c => c.trim()).filter((_, i, arr) => i > 0 && i < arr.length - 1);
      if (cells.length >= 3) {
        const wordMatch = cells[0].match(/\[\[([^\]|]+)(?:\|[^\]]+)?\]\]/);
        if (wordMatch) {
          const word = wordMatch[1].trim();
          const pos = cells[1];
          const defs = cells[2];
          const sentence = cells[3] || '';
          const freq = getWordFrequency(word);

          tableRows.push({
            rawWordCell: cells[0],
            word,
            pos,
            defs,
            sentence,
            tier: freq.tier,
            rank: freq.rank,
            zipf: freq.zipf
          });
        }
      }
    }
  }

  if (tableRows.length === 0) continue;

  // 2. Classify rows into 3 tiers
  const t1Rows = tableRows.filter(r => r.tier === 1).sort((a, b) => a.rank - b.rank);
  const t2Rows = tableRows.filter(r => r.tier === 2).sort((a, b) => a.rank - b.rank);
  const t3Rows = tableRows.filter(r => r.tier === 3).sort((a, b) => a.word.localeCompare(b.word));

  // Sanity check: Ensure zero rows lost
  if (t1Rows.length + t2Rows.length + t3Rows.length !== tableRows.length) {
    console.error(`Row count mismatch in ${filePath}`);
    continue;
  }

  // Format Tier Table Markdown
  function formatTierTable(title, rows, emoji) {
    if (rows.length === 0) return '';
    let out = `\n\n### ${emoji} ${title} (${rows.length} ${rows.length === 1 ? 'word' : 'words'})\n\n`;
    out += `| Word | POS | Frequency / Rank | Authoritative Definitions | Authentic Illustrative Sentence |\n`;
    out += `| :--- | :--- | :--- | :--- | :--- |\n`;
    for (const r of rows) {
      let freqBadge = '';
      if (r.tier === 1) freqBadge = `⭐ Zipf ${r.zipf.toFixed(1)} (#${r.rank.toLocaleString()})`;
      else if (r.tier === 2) freqBadge = `📈 Zipf ${r.zipf.toFixed(1)} (#${r.rank.toLocaleString()})`;
      else freqBadge = `🏛️ Rare / Obsolete`;

      out += `| ${r.rawWordCell} | ${r.pos} | ${freqBadge} | ${r.defs} | ${r.sentence} |\n`;
    }
    return out;
  }

  let newS6Body = '';
  newS6Body += formatTierTable('Tier 1: Words to Learn First (High Frequency)', t1Rows, '⭐');
  newS6Body += formatTierTable('Tier 2: Words to Learn a Little Later (Elevated & Academic)', t2Rows, '📈');
  newS6Body += formatTierTable('Tier 3: Words to Learn Last (Rare & Specialized)', t3Rows, '🏛️');

  if (remainingContentLines.length > 0) {
    newS6Body += '\n' + remainingContentLines.join('\n');
  }

  // 3. Update Frontmatter with Tier & Metrics
  const rootMetrics = getRootFrequencyTier(tableRows.map(r => r.word));
  let updatedContent = beforeS6 + newS6Body;

  // Update YAML frontmatter
  if (updatedContent.startsWith('---')) {
    const fEnd = updatedContent.indexOf('---', 3);
    if (fEnd !== -1) {
      const existingFm = updatedContent.slice(3, fEnd);
      // Remove previous tier keys if present
      let cleanFm = existingFm
        .replace(/\ntier:\s*\d+/g, '')
        .replace(/\nfrequency_score:\s*[\d.]+/g, '')
        .replace(/\ntier_label:[^\n]+/g, '')
        .replace(/\ntier1_words:\s*\d+/g, '')
        .replace(/\ntier2_words:\s*\d+/g, '')
        .replace(/\ntier3_words:\s*\d+/g, '')
        .trim();

      cleanFm += `\ntier: ${rootMetrics.tier}\nfrequency_score: ${rootMetrics.score}\ntier_label: "${rootMetrics.tierLabel}"\ntier1_words: ${rootMetrics.t1Count}\ntier2_words: ${rootMetrics.t2Count}\ntier3_words: ${rootMetrics.t3Count}`;
      updatedContent = `---\n${cleanFm}\n---` + updatedContent.slice(fEnd + 3);
    }
  }

  fs.writeFileSync(filePath, updatedContent, 'utf8');
  modifiedCount++;
}

console.log(`\n🎉 Successfully organized ${modifiedCount} / ${processedCount} root dashboards into 3 Frequency Tiers!`);
