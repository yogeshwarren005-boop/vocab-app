import fs from 'fs';

const html = fs.readFileSync('C:/Users/yoges/.gemini/antigravity/brain/4078b0bb-809e-4104-b910-2690ae88fce7/.system_generated/steps/3508/output.txt', 'utf8');

const idx = html.indexOf('id="google-serp-content"');
console.log('google-serp-content idx:', idx);
if (idx !== -1) {
  console.log(html.slice(idx, idx + 2500));
}
