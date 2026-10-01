import fs from "fs";
import path from "path";

const baseDir = "App database/Greek roots/Cluster Speech & Language";
const entries = fs.readdirSync(baseDir, { withFileTypes: true });
let totalWords = 0;
const dashboards = [];

for (const entry of entries) {
  if (entry.isDirectory()) {
    const dashPath = path.join(baseDir, entry.name);
    const files = fs.readdirSync(dashPath).filter(f =>
      f.endsWith(".md") &&
      !f.startsWith("Dashboard —") &&
      !f.startsWith("Word Triage —") &&
      !f.startsWith("Cluster") &&
      !f.startsWith("Semantic Field")
    );
    dashboards.push({ name: entry.name, count: files.length, files });
    totalWords += files.length;
  }
}

dashboards.sort((a, b) => a.count - b.count);
for (const d of dashboards) {
  console.log(`${d.name}: ${d.count} words`);
}
console.log(`\nTotal dashboards: ${dashboards.length}`);
console.log(`Total words: ${totalWords}`);
