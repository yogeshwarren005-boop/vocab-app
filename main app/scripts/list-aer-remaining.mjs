import fs from "fs";
import path from "path";

const dir = "App database/Greek roots/Cluster Nature & Cosmos/Dashboard — aer";
const files = fs.readdirSync(dir)
  .filter(f => f.endsWith('.md') && !f.startsWith('Dashboard') && !f.startsWith('Word Triage'))
  .sort();

console.log("Total aer words:", files.length);

// Check which files still have issues
import { execSync } from "child_process";
const audited = files.map(f => {
  const content = fs.readFileSync(path.join(dir, f), "utf8");
  const hasAcademic = content.includes("Academic Lexicon");
  const pMatch = content.match(/1\.\s*\*\*([^*]+)\*\*:\s*([^\r\n]+)/);
  const sMatch = content.match(/2\.\s*\*\*([^*]+)\*\*:\s*([^\r\n]+)/);
  const dupDef = pMatch && sMatch && pMatch[2].trim().toLowerCase() === sMatch[2].trim().toLowerCase();
  return { file: f, problem: hasAcademic || dupDef };
});

const uncurated = audited.filter(a => a.problem).map(a => a.file);
console.log("Uncurated count:", uncurated.length);
console.log("\nFirst 32 uncurated (Batch 9):");
console.log(uncurated.slice(0, 32).join("\n"));
console.log("\nRemaining 31 uncurated (Batch 10):");
console.log(uncurated.slice(32).join("\n"));
