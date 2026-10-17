// scripts/sync-and-broadcast.mjs
import { initializeApp, cert } from 'firebase-admin/app';
import { getFirestore, FieldValue } from 'firebase-admin/firestore';
import fs from 'fs';

const serviceAccount = JSON.parse(process.env.FIREBASE_SERVICE_ACCOUNT);
initializeApp({ credential: cert(serviceAccount) });
const db = getFirestore();

async function run() {
  const pkg = JSON.parse(fs.readFileSync('./package.json', 'utf8'));
  const version = pkg.version;
  const rawRepo = process.env.GITHUB_REPOSITORY || 'yogeshwarren005-boop/vocab-app';
  const repo = rawRepo.replace(/^https?:\/\/github\.com\//, '').replace(/\.git$/, '');
  const apkUrl = `https://github.com/${repo}/releases/download/v${version}/app-release.apk`;

  // 1. Ensure required collections/schema defaults exist non-destructively
  const configRef = db.collection('app_config').doc('schema_state');
  await configRef.set({
    schemaVersion: version,
    lastMigratedAt: FieldValue.serverTimestamp()
  }, { merge: true });

  // 2. Broadcast new release to trigger instant popup on all connected phones
  await db.collection('app_meta').doc('mobile_release').set({
    version: version,
    downloadUrl: apkUrl,
    releaseNotes: process.env.RELEASE_NOTES || `Automated build v${version}`,
    publishedAt: FieldValue.serverTimestamp()
  });

  console.log(`Successfully synced Firebase and broadcasted v${version} for ${repo}`);
}

run().catch((err) => { console.error(err); process.exit(1); });
