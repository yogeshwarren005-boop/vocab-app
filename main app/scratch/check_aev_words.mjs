import fs from 'fs';

const words = ['coevalities', 'coevality', 'coevals', 'longevities', 'mediaeval', 'mediaevals', 'medievally', 'medievals', 'primevally', 'sempervivum'];
const index = JSON.parse(fs.readFileSync('public/data/vault-index.json', 'utf8'));

for (const w of words) {
  const match = index.pages.filter(p => p.p.toLowerCase().includes(w));
  console.log(w, ':', match.map(m => m.p));
}
