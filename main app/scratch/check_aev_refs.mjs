import fs from 'fs';

const index = JSON.parse(fs.readFileSync('public/data/vault-index.json', 'utf8'));
const refs = index.pages.filter(p => (p.lr && p.lr.includes('aev')) || (p.p && p.p.includes('aev')));
console.log('Pages referencing or named aev:');
for (const r of refs) {
  console.log(' ', r.p, 'lr:', r.lr);
}
