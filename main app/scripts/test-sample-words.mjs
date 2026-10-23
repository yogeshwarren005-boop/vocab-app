import fs from 'fs';

const index = JSON.parse(fs.readFileSync('main app/public/data/vault-index.json', 'utf8'));

// A pure word is inside a cluster folder, does not start with Dashboard, does not start with Cluster, and ends with .md
const wordPages = index.pages.filter(p => {
  const parts = p.p.split('/');
  const fn = parts[parts.length - 1];
  if (!fn.endsWith('.md')) return false;
  if (/^Dashboard\s*[—–-]/i.test(fn)) return false;
  if (/^Cluster\s+/i.test(fn)) return false;
  if (fn.startsWith('0') || fn.includes('Reference') || fn.includes('MOC') || fn.includes('Mockup')) return false;
  return parts.some(part => /^Cluster\s+/i.test(part));
});

console.log('Total pure individual vocabulary words:', wordPages.length);

const sections = {
  greek: wordPages.filter(p => p.p.startsWith('Greek roots')),
  latin: wordPages.filter(p => p.p.startsWith('Latin roots')),
  vocab: wordPages.filter(p => p.p.startsWith('English vocabulary master'))
};

console.log(`Greek: ${sections.greek.length}, Latin: ${sections.latin.length}, English Vocab: ${sections.vocab.length}`);

// Stratified random sample of 20 words across sections and tiers
function pickFrom(pool, count) {
  const chosen = [];
  const step = Math.floor(pool.length / count);
  for (let i = 0; i < count; i++) {
    const idx = (i * step + Math.floor(Math.random() * (step * 0.9))) % pool.length;
    chosen.push(pool[idx]);
  }
  return chosen;
}

const sampled20 = [
  ...pickFrom(sections.greek, 6),
  ...pickFrom(sections.latin, 8),
  ...pickFrom(sections.vocab, 6)
];

console.log('\n--- 20 DIVERSIFIED RANDOM WORDS SAMPLED ---');
sampled20.forEach((p, i) => {
  const name = p.p.slice(p.p.lastIndexOf('/') + 1).replace(/\.md$/i, '');
  const section = p.p.split('/')[0];
  console.log(`${(i + 1).toString().padStart(2, ' ')}. [Tier ${p.f || 3}] ${name.padEnd(25)} | ${section.padEnd(26)} | Zipf: ${(p.z || 0).toFixed(1)}`);
});
