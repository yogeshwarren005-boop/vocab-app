import fs from 'fs';
import path from 'path';

const clusterTime = path.resolve('../App database/Latin roots/Cluster Time');
const entries = fs.readdirSync(clusterTime);
console.log('Entries in Cluster Time:');
for (const e of entries) {
  const p = path.join(clusterTime, e);
  const isDir = fs.statSync(p).isDirectory();
  if (isDir) {
    const files = fs.readdirSync(p);
    console.log(`  [DIR] ${e} (${files.length} items):`, files.slice(0, 5));
  } else {
    console.log(`  [FILE] ${e}`);
  }
}
