import fs from "fs";
import path from "path";

const baseDir = "App database/Greek roots";
const clusters = fs.readdirSync(baseDir, { withFileTypes: true })
  .filter(d => d.isDirectory() && d.name.startsWith("Cluster"))
  .map(d => d.name);

function countWords(dir) {
  let count = 0;
  for (const ent of fs.readdirSync(dir, { withFileTypes: true })) {
    const full = path.join(dir, ent.name);
    if (ent.isDirectory()) {
      count += countWords(full);
    } else if (
      ent.name.endsWith('.md') &&
      !ent.name.startsWith('Dashboard —') &&
      !ent.name.startsWith('Word Triage —') &&
      !ent.name.startsWith('Cluster') &&
      !ent.name.startsWith('Semantic Field')
    ) {
      count++;
    }
  }
  return count;
}

const checkpoint = JSON.parse(fs.readFileSync("Instructions for Agent/checkpoint_state.json", "utf8"));
const completed = checkpoint.completedClusters;

const results = [];
for (const c of clusters) {
  const isDone = completed.includes(`Greek roots: ${c}`);
  const wCount = countWords(path.join(baseDir, c));
  results.push({ name: c, count: wCount, isDone });
}

results.sort((a, b) => a.count - b.count);

console.log("=== GREEK ROOT CLUSTERS SUMMARY ===");
for (const r of results) {
  console.log(`${r.isDone ? "✅" : "⏳"} ${r.name}: ${r.count} words`);
}
