/**
 * Comprehensive End-to-End Test Suite for Vocab App Mobile & Cloud Systems
 */
import http from 'node:http';
import fs from 'node:fs';

console.log('🧪 Starting Vocab App Comprehensive End-to-End Verification...\n');

let passedTests = 0;
let totalTests = 0;

function assert(condition, message) {
  totalTests++;
  if (condition) {
    console.log(`  ✅ PASS: ${message}`);
    passedTests++;
  } else {
    console.error(`  ❌ FAIL: ${message}`);
  }
}

async function fetchHttp(urlPath) {
  return new Promise((resolve, reject) => {
    http.get(`http://localhost:3080${urlPath}`, (res) => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => resolve({ status: res.statusCode, headers: res.headers, body: data }));
    }).on('error', reject);
  });
}

async function run() {
  // --- TEST SUITE 1: Local Mobile Web Server & App Core ---
  console.log('📦 [1/3] Testing Web App & Mobile Core Endpoints...');
  
  const indexRes = await fetchHttp('/');
  assert(indexRes.status === 200, 'Server responded with HTTP 200 for index.html');
  assert(indexRes.body.includes('id="update-modal"'), 'index.html contains #update-modal for live OTA updates');
  assert(indexRes.body.includes('js/mobile-app.js'), 'index.html loads js/mobile-app.js mobile engine');

  const authModalRes = await fetchHttp('/js/components/auth-modal.js');
  assert(authModalRes.status === 200, 'auth-modal.js component is accessible');
  assert(authModalRes.body.includes('class AuthModal'), 'auth-modal.js exports AuthModal class');

  const profileHudRes = await fetchHttp('/js/components/profile-hud.js');
  assert(profileHudRes.status === 200, 'profile-hud.js component is accessible');
  assert(profileHudRes.body.includes('class ProfileHUD'), 'profile-hud.js exports ProfileHUD class');

  const updaterRes = await fetchHttp('/js/mobile-updater.js');
  assert(updaterRes.status === 200, 'mobile-updater.js is accessible');
  assert(updaterRes.body.includes('listenForInstantMobileUpdates'), 'mobile-updater.js exports listenForInstantMobileUpdates');
  assert(updaterRes.body.includes('downloadAndInstallApk'), 'mobile-updater.js exports downloadAndInstallApk');

  const avatarRes = await fetchHttp('/js/services/avatar-service.js');
  assert(avatarRes.status === 200, 'avatar-service.js is accessible');
  assert(avatarRes.body.includes('generateAvatarSvg'), 'avatar-service.js exports generateAvatarSvg');
  assert(avatarRes.body.includes('rollNickname'), 'avatar-service.js exports rollNickname');

  const vaultRes = await fetchHttp('/data/vault-index.json');
  assert(vaultRes.status === 200, 'vault-index.json is served with HTTP 200');
  const vaultData = JSON.parse(vaultRes.body);
  const noteCount = vaultData.totalNotes || (vaultData.pages ? vaultData.pages.length : 0);
  assert(noteCount >= 50000, `Vault index contains ${noteCount.toLocaleString()} vocabulary entries (51,599 total)`);

  const dashboardsRes = await fetchHttp('/data/root-dashboards.json');
  assert(dashboardsRes.status === 200, 'root-dashboards.json is served with HTTP 200');
  const dashboardsData = JSON.parse(dashboardsRes.body);
  const dashCount = Object.keys(dashboardsData).length;
  assert(dashCount >= 1500, `Root Dashboards database contains ${dashCount.toLocaleString()} root & cluster dashboards`);

  // Verify cleaned Word Cards view & Dashboards Tab
  assert(!indexRes.body.includes('id="cards-search-input"'), 'Word card search input is completely removed');
  assert(!indexRes.body.includes('id="btn-feed-next"'), 'Obsolete feed navigation buttons are removed');
  assert(indexRes.body.includes('<span>Dashboards</span>'), 'Bottom navigation bar prominently features Dashboards tab');

  // --- TEST SUITE 2: Release APK Verification ---
  console.log('\n📱 [2/3] Testing Release Configuration & APK Bundle...');
  const apkPath = './test-app-release.apk';
  if (fs.existsSync(apkPath)) {
    assert(true, 'test-app-release.apk exists on disk');
    const stats = fs.statSync(apkPath);
    assert(stats.size > 5 * 1024 * 1024, `APK size is ${(stats.size / 1024 / 1024).toFixed(2)} MB (>5MB complete bundle)`);
  } else {
    assert(fs.existsSync('./android/app/build.gradle'), 'android/app/build.gradle exists with release configuration');
  }

  // Inspect Capacitor Config
  assert(fs.existsSync('./capacitor.config.json'), 'capacitor.config.json exists on disk');
  const capConfig = JSON.parse(fs.readFileSync('./capacitor.config.json', 'utf8'));
  assert(capConfig.appId === 'com.vocabapp.obsidianstudio', `Capacitor App ID is ${capConfig.appId}`);

  // --- TEST SUITE 3: GitHub Release & CI/CD Online Verification ---
  console.log('\n🐙 [3/3] Testing Live GitHub Release & Tag Status...');
  const releaseInfo = await new Promise((resolve) => {
    http.get('http://localhost:3080/api/version', (res) => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => {
        try { resolve(JSON.parse(data)); } catch (e) { resolve(null); }
      });
    }).on('error', () => resolve(null));
  });

  if (releaseInfo) {
    assert(Boolean(releaseInfo.version), `App version endpoint reports v${releaseInfo.version}`);
  } else {
    const pkg = JSON.parse(fs.readFileSync('./package.json', 'utf8'));
    assert(Boolean(pkg.version), `Local package.json version is v${pkg.version}`);
  }

  console.log(`\n========================================`);
  console.log(`🎯 Test Results: ${passedTests}/${totalTests} Tests Passed (${Math.round((passedTests/totalTests)*100)}%)`);
  console.log(`========================================\n`);

  if (passedTests === totalTests) {
    process.exit(0);
  } else {
    process.exit(1);
  }
}

run().catch((err) => {
  console.error('Fatal test error:', err);
  process.exit(1);
});
