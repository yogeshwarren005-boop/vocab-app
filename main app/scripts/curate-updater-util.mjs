import fs from 'fs';
import path from 'path';

/**
 * Updates an array or dictionary of word notes with pristine definitions and quotes.
 * @param {string} baseClusterDir - Absolute or relative path to the cluster root
 * @param {Record<string, {primary: string, secondary: string, quotes: Array<{author: string, work: string, quote: string}>}>} batchData
 * @returns {number} count of successfully updated notes
 */
export function updateNotesBatch(baseClusterDir, batchData) {
  let updated = 0;
  for (const [relPath, data] of Object.entries(batchData)) {
    const filePath = path.join(baseClusterDir, relPath);
    if (!fs.existsSync(filePath)) {
      console.error(`[updater] File not found: ${filePath}`);
      continue;
    }
    const content = fs.readFileSync(filePath, 'utf8');
    const bookIdx = content.indexOf('> [!book]');
    if (bookIdx === -1) {
      console.error(`[updater] No '> [!book]' block found in: ${filePath}`);
      continue;
    }
    const headerPart = content.slice(0, bookIdx).trimEnd();
    const defBlock = `> [!book] 📖 Definitions & Semantic Range\n> 1. **Primary Definition (Lexical / Standard Consensus)**: ${data.primary}\n> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: ${data.secondary}`;
    const quoteLines = data.quotes.map(q => `> - 📜 **${q.author} (*${q.work}*):** *"${q.quote}"*`).join('\n');
    const quotesBlock = `> [!quote] 💬 Contextual Usage & Authentic Quotations\n${quoteLines}`;

    const newContent = `${headerPart}\n\n${defBlock}\n\n${quotesBlock}\n`;
    fs.writeFileSync(filePath, newContent, 'utf8');
    updated++;
  }
  return updated;
}
