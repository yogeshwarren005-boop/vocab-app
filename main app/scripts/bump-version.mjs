#!/usr/bin/env node
/**
 * Automated Version Management Script for Obsidian Vocab Mobile App
 * 
 * Synchronizes version across:
 *   1. main app/public/version.json (Single source of truth)
 *   2. main app/package.json
 *   3. android/app/build.gradle (dynamic from version.json)
 *   4. android/app/src/main/assets/public/ (via cap:sync)
 * 
 * Usage:
 *   node scripts/bump-version.mjs 1.1.0
 *   node scripts/bump-version.mjs patch
 *   node scripts/bump-version.mjs minor
 *   node scripts/bump-version.mjs major
 */

import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { execSync } from 'node:child_process';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const MAIN_APP_DIR = path.resolve(__dirname, '..');
const VERSION_JSON_PATH = path.join(MAIN_APP_DIR, 'public', 'version.json');
const PACKAGE_JSON_PATH = path.join(MAIN_APP_DIR, 'package.json');

function parseSemVer(v) {
  const match = v.trim().replace(/^v/, '').match(/^(\d+)\.(\d+)\.(\d+)(?:-([0-9A-Za-z.-]+))?$/);
  if (!match) {
    throw new Error(`Invalid SemVer format: "${v}". Expected format: X.Y.Z (e.g. 1.0.1)`);
  }
  return {
    major: parseInt(match[1], 10),
    minor: parseInt(match[2], 10),
    patch: parseInt(match[3], 10),
    prerelease: match[4] || null,
    raw: match[0]
  };
}

function bumpSemVer(current, bumpType) {
  const parsed = parseSemVer(current);
  switch (bumpType.toLowerCase()) {
    case 'major':
      return `${parsed.major + 1}.0.0`;
    case 'minor':
      return `${parsed.major}.${parsed.minor + 1}.0`;
    case 'patch':
      return `${parsed.major}.${parsed.minor}.${parsed.patch + 1}`;
    default:
      // Direct version string provided
      return parseSemVer(bumpType).raw;
  }
}

function main() {
  const arg = process.argv[2];
  if (!arg) {
    console.error('❌ Error: Missing version argument.');
    console.log('\nUsage:');
    console.log('  npm run version:bump 1.1.0');
    console.log('  npm run version:bump patch   (e.g. 1.0.0 -> 1.0.1)');
    console.log('  npm run version:bump minor   (e.g. 1.0.0 -> 1.1.0)');
    console.log('  npm run version:bump major   (e.g. 1.0.0 -> 2.0.0)');
    process.exit(1);
  }

  // 1. Read current version.json
  let versionData = {
    version: "1.0.0",
    versionCode: 1,
    name: "Obsidian Vocab",
    releaseDate: new Date().toISOString().slice(0, 10),
    githubRepo: "yorren005/vocab-app"
  };

  if (fs.existsSync(VERSION_JSON_PATH)) {
    try {
      versionData = JSON.parse(fs.readFileSync(VERSION_JSON_PATH, 'utf-8'));
    } catch (e) {
      console.warn(`⚠️ Warning reading version.json: ${e.message}`);
    }
  }

  const oldVersion = versionData.version || "1.0.0";
  const oldCode = parseInt(versionData.versionCode || 1, 10);

  // 2. Compute new version and code
  const newVersion = bumpSemVer(oldVersion, arg);
  const newCode = oldCode + 1;
  const today = new Date().toISOString().slice(0, 10);

  versionData.version = newVersion;
  versionData.versionCode = newCode;
  versionData.releaseDate = today;

  // 3. Write public/version.json
  fs.writeFileSync(VERSION_JSON_PATH, JSON.stringify(versionData, null, 2) + '\n', 'utf-8');
  console.log(`✅ Updated ${path.relative(MAIN_APP_DIR, VERSION_JSON_PATH)} -> v${newVersion} (code: ${newCode})`);

  // 4. Update package.json
  if (fs.existsSync(PACKAGE_JSON_PATH)) {
    const pkg = JSON.parse(fs.readFileSync(PACKAGE_JSON_PATH, 'utf-8'));
    pkg.version = newVersion;
    fs.writeFileSync(PACKAGE_JSON_PATH, JSON.stringify(pkg, null, 2) + '\n', 'utf-8');
    console.log(`✅ Updated package.json -> v${newVersion}`);
  }

  // 5. Sync Capacitor Android Assets
  console.log('🔄 Syncing assets to native Android container...');
  try {
    execSync('npx cap sync android', { cwd: MAIN_APP_DIR, stdio: 'inherit' });
    console.log('✅ Native Android assets synchronized successfully!');
  } catch (err) {
    console.warn('⚠️ Capacitor sync failed or was skipped:', err.message);
  }

  console.log('\n======================================================');
  console.log(` 🎉 Version Bump Complete: v${oldVersion} (${oldCode}) ➔ v${newVersion} (${newCode})`);
  console.log('======================================================');
  console.log('Next release steps:');
  console.log(`  1. git add -A`);
  console.log(`  2. git commit -m "chore(release): v${newVersion}"`);
  console.log(`  3. git tag v${newVersion}`);
  console.log(`  4. git push origin main --tags`);
  console.log('======================================================\n');
}

main();
