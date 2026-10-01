import fs from "fs";
import path from "path";

const baseDir = "App database/Greek roots/Cluster Speech & Language";
function walk(dir) {
  let res = [];
  const entries = fs.readdirSync(dir, { withFileTypes: true });
  for (const ent of entries) {
    const full = path.join(dir, ent.name);
    if (ent.isDirectory()) {
      res.push(...walk(full));
    } else if (
      ent.name.endsWith('.md') &&
      !ent.name.startsWith('Dashboard —') &&
      !ent.name.startsWith('Word Triage —') &&
      !ent.name.startsWith('Cluster') &&
      !ent.name.startsWith('Semantic Field')
    ) {
      res.push(full);
    }
  }
  return res;
}

const files = walk(baseDir);
console.log(`Total words: ${files.length}`);

// Group by dashboard
const groups = {};
for (const f of files) {
  const dash = path.basename(path.dirname(f));
  if (!groups[dash]) groups[dash] = [];
  groups[dash].push(path.basename(f, '.md'));
}

for (const [dash, words] of Object.entries(groups).sort((a,b) => a[1].length - b[1].length)) {
  console.log(`\n### ${dash} (${words.length} words):`);
  console.log(words.join(", "));
}
