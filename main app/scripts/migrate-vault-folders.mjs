/**
 * migrate-vault-folders.mjs
 * Migrates physical folders in App database/ into 3 frequency tiers:
 *   - Tier 1 — Words to Learn First
 *   - Tier 2 — Words to Learn Later
 *   - Tier 3 — Words to Learn Last
 * 
 * Updates status-db.json and root-dashboards.json with the new paths.
 */

import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { CLUSTER_TIER_MAP, TIER_FOLDER_NAMES } from './cluster-tier-map.mjs';
import { getRootFrequencyTier } from './frequency-engine.mjs';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT_DIR = path.resolve(__dirname, '..', '..');
const APP_DB = path.join(ROOT_DIR, 'App database');
const STATUS_DB_PATH = path.join(ROOT_DIR, 'main app', 'public', 'data', 'status-db.json');
const ROOT_DASHBOARDS_PATH = path.join(ROOT_DIR, 'main app', 'public', 'data', 'root-dashboards.json');

console.log('🚀 Starting physical vault folder migration into 3 tiers...');
console.log(`Database root: ${APP_DB}`);

const SECTIONS = [
  { key: 'english', folder: 'English vocabulary master' },
  { key: 'greek', folder: 'Greek roots' },
  { key: 'latin', folder: 'Latin roots' }
];

let totalMoved = 0;
const pathReplacements = new Map();

for (const sec of SECTIONS) {
  const secDir = path.join(APP_DB, sec.folder);
  if (!fs.existsSync(secDir)) {
    console.warn(`Section dir not found: ${secDir}`);
    continue;
  }

  // 1. Ensure tier folders exist
  for (const tierNum of [1, 2, 3]) {
    const tierFolderName = TIER_FOLDER_NAMES[tierNum];
    const tierDir = path.join(secDir, tierFolderName);
    if (!fs.existsSync(tierDir)) {
      fs.mkdirSync(tierDir, { recursive: true });
      console.log(`📁 Created tier folder: ${sec.folder}/${tierFolderName}`);
    }
  }

  // 2. Scan cluster directories
  const clusterMap = CLUSTER_TIER_MAP[sec.key];
  const entries = fs.readdirSync(secDir, { withFileTypes: true });

  for (const entry of entries) {
    if (!entry.isDirectory() || !entry.name.startsWith('Cluster ')) continue;
    const clusterName = entry.name;
    const tier = clusterMap[clusterName];
    if (!tier) {
      console.warn(`⚠️ Warning: No tier found for cluster: ${clusterName} in ${sec.folder}`);
      continue;
    }

    const tierFolderName = TIER_FOLDER_NAMES[tier];
    const srcDir = path.join(secDir, clusterName);
    const destDir = path.join(secDir, tierFolderName, clusterName);

    if (fs.existsSync(destDir)) {
      console.log(`ℹ️ Cluster already in destination: ${sec.folder}/${tierFolderName}/${clusterName}`);
    } else {
      try {
        fs.renameSync(srcDir, destDir);
        totalMoved++;
        console.log(`✅ Moved: ${sec.folder}/${clusterName} ➔ ${sec.folder}/${tierFolderName}/${clusterName}`);
      } catch (err) {
        console.error(`❌ Failed to move ${clusterName}:`, err.message);
      }
    }

    // Record path replacement for statusDb & rootDashboards
    const oldRelPrefix = `${sec.folder}/${clusterName}`;
    const newRelPrefix = `${sec.folder}/${tierFolderName}/${clusterName}`;
    pathReplacements.set(oldRelPrefix, newRelPrefix);
  }
}

console.log(`\n🎉 Total cluster folders migrated: ${totalMoved}`);

// 3. Migrate status-db.json paths
if (fs.existsSync(STATUS_DB_PATH)) {
  console.log('\n📝 Updating status-db.json keys...');
  const oldDb = JSON.parse(fs.readFileSync(STATUS_DB_PATH, 'utf8'));
  const newDb = {};
  let statusUpdates = 0;

  for (const [key, val] of Object.entries(oldDb)) {
    let updatedKey = key;
    for (const [oldPrefix, newPrefix] of pathReplacements.entries()) {
      if (key.startsWith(oldPrefix + '/') || key === oldPrefix) {
        updatedKey = newPrefix + key.slice(oldPrefix.length);
        statusUpdates++;
        break;
      }
    }
    newDb[updatedKey] = val;
  }

  fs.writeFileSync(STATUS_DB_PATH, JSON.stringify(newDb, null, 2), 'utf8');
  console.log(`✅ Updated ${statusUpdates} keys in status-db.json`);
}

// 4. Update root-dashboards.json paths & enrich with frequency tiers
if (fs.existsSync(ROOT_DASHBOARDS_PATH)) {
  console.log('\n📊 Updating and enriching root-dashboards.json...');
  const dashboards = JSON.parse(fs.readFileSync(ROOT_DASHBOARDS_PATH, 'utf8'));
  let dashUpdates = 0;

  for (const rootKey of Object.keys(dashboards)) {
    const d = dashboards[rootKey];
    let pathUpdated = false;

    for (const [oldPrefix, newPrefix] of pathReplacements.entries()) {
      if (d.path && (d.path.startsWith(oldPrefix + '/') || d.path === oldPrefix)) {
        d.path = newPrefix + d.path.slice(oldPrefix.length);
        pathUpdated = true;
        break;
      }
    }
    if (pathUpdated) dashUpdates++;

    // Compute root frequency tier & metrics from derived words
    const freq = getRootFrequencyTier(d.words || []);
    d.tier = freq.tier;
    d.tierLabel = freq.tierLabel;
    d.frequencyScore = freq.score;
    d.t1Count = freq.t1Count;
    d.t2Count = freq.t2Count;
    d.t3Count = freq.t3Count;
  }

  fs.writeFileSync(ROOT_DASHBOARDS_PATH, JSON.stringify(dashboards, null, 2), 'utf8');
  console.log(`✅ Updated ${dashUpdates} paths and enriched ${Object.keys(dashboards).length} dashboards in root-dashboards.json`);
}

console.log('\n✨ Migration phase 1 completed successfully!');
