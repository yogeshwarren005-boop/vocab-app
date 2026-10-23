/**
 * inject-word-frontmatter.mjs
 * Injects deterministic frequency tier properties into the YAML frontmatter
 * of all individual word notes across English vocabulary master, Greek roots, and Latin roots.
 */

import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { getWordFrequency } from './frequency-engine.mjs';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT_DIR = path.resolve(__dirname, '..', '..');
const APP_DB = path.join(ROOT_DIR, 'App database');

console.log('🚀 Injecting frequency tier frontmatter into individual word files...');

const SECTIONS = ['English vocabulary master', 'Greek roots', 'Latin roots'];

function findWordFiles(dir) {
  let list = [];
  try {
    for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
      const fullPath = path.join(dir, entry.name);
      if (entry.isDirectory()) {
        if (entry.name === '03_Reference_and_Rules' || entry.name === '01_Root_Dashboards' || entry.name.startsWith('.')) continue;
        list = list.concat(findWordFiles(fullPath));
      } else if (entry.name.endsWith('.md')) {
        const n = entry.name;
        if (n.startsWith('Dashboard') || n.startsWith('Cluster') || n.startsWith('Master Table') || n.startsWith('Word Triage') || n.startsWith('00') || n.includes('Progress') || n.includes('MOC')) continue;
        list.push(fullPath);
      }
    }
  } catch {}
  return list;
}

let allWordFiles = [];
for (const s of SECTIONS) {
  const sPath = path.join(APP_DB, s);
  if (fs.existsSync(sPath)) {
    allWordFiles = allWordFiles.concat(findWordFiles(sPath));
  }
}

console.log(`Found ${allWordFiles.length.toLocaleString()} individual word files to update.`);

const t0 = Date.now();
let updatedCount = 0;

for (let i = 0; i < allWordFiles.length; i++) {
  const fp = allWordFiles[i];
  const word = path.basename(fp, '.md');
  const freq = getWordFrequency(word);

  try {
    const content = fs.readFileSync(fp, 'utf8');
    if (!content.startsWith('---')) continue;

    const fEnd = content.indexOf('---', 3);
    if (fEnd === -1) continue;

    let fm = content.slice(3, fEnd)
      .replace(/\ntier:\s*\d+/g, '')
      .replace(/\ntier_label:[^\n]+/g, '')
      .replace(/\nzipf:[^\n]+/g, '')
      .replace(/\nrank:[^\n]+/g, '')
      .trim();

    fm += `\ntier: ${freq.tier}\ntier_label: "${freq.tierLabel}"\nzipf: ${freq.zipf}\nrank: ${freq.rank}`;
    const newContent = `---\n${fm}\n---` + content.slice(fEnd + 3);

    fs.writeFileSync(fp, newContent, 'utf8');
    updatedCount++;

    if (updatedCount % 10000 === 0) {
      console.log(`Updated ${updatedCount.toLocaleString()} / ${allWordFiles.length.toLocaleString()} files...`);
    }
  } catch (err) {
    // ignore individual file read errors
  }
}

const elapsed = ((Date.now() - t0) / 1000).toFixed(2);
console.log(`✅ Successfully injected frequency metadata into ${updatedCount.toLocaleString()} word files in ${elapsed}s!`);
