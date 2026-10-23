import fs from 'fs';

const html = fs.readFileSync('C:/Users/yoges/.gemini/antigravity/brain/4078b0bb-809e-4104-b910-2690ae88fce7/.system_generated/steps/3412/output.txt', 'utf8');

console.log('HTML size:', html.length);

// Extract main organic results
const regex = /<div class="[^"]*MjjYud[^"]*"[\s\S]*?<\/div>\s*<\/div>\s*<\/div>/g;
const titles = [...html.matchAll(/<h3[^>]*>(.*?)<\/h3>/gi)].map(m => m[1].replace(/<[^>]+>/g, '').trim()).filter(Boolean);
console.log('Titles found (' + titles.length + '):');
titles.slice(0, 8).forEach((t, i) => console.log(`  ${i + 1}. ${t}`));

// Extract snippets and links
const links = [...html.matchAll(/<a [^>]*href="(https:\/\/[^"]+)"[^>]*>[\s\S]*?<h3[^>]*>(.*?)<\/h3>/gi)].map(m => ({
  url: m[1],
  title: m[2].replace(/<[^>]+>/g, '').trim()
}));
console.log('\nTop links:');
links.slice(0, 6).forEach((l, i) => console.log(`  ${i + 1}. [${l.title}](${l.url})`));
