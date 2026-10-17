/**
 * CLI Tool to Re-index the App Database
 * Usage:
 *   node scripts/reindex.mjs
 * Triggers instant re-indexing via running server API, or falls back to server.mjs --index-only.
 */

import http from 'node:http';
import { execSync } from 'node:child_process';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const APP_DIR = path.resolve(__dirname, '..');
const PORT = Number(process.env.PORT || 3080);
const AUTH_TOKEN = (process.env.AUTH_TOKEN || process.env.VAULT_PASSWORD || '').trim();

function triggerServerReindex() {
  return new Promise((resolve, reject) => {
    const headers = {};
    if (AUTH_TOKEN) {
      headers['Authorization'] = `Bearer ${AUTH_TOKEN}`;
    }

    const req = http.request(
      {
        hostname: 'localhost',
        port: PORT,
        path: '/api/reindex',
        method: 'POST',
        headers,
        timeout: 60000 // 60s timeout allows full 51,600 file vault scan without prematurely killing connection
      },
      (res) => {
        let data = '';
        res.on('data', chunk => data += chunk);
        res.on('end', () => {
          try {
            resolve(JSON.parse(data));
          } catch {
            resolve({ ok: true, raw: data });
          }
        });
      }
    );
    req.on('error', reject);
    req.on('timeout', () => {
      req.destroy();
      reject(new Error('Request timed out after 60s'));
    });
    req.end();
  });
}

async function main() {
  console.log('⚡ Requesting database re-index...');
  try {
    const res = await triggerServerReindex();
    if (res && res.error) {
      throw new Error(res.error);
    }
    console.log(`✅ Live server re-indexed successfully! Total notes: ${res.totalNotes?.toLocaleString()}`);
  } catch (err) {
    if (err.code === 'ECONNREFUSED') {
      console.log('ℹ️  Server not running on port 3080. Performing direct local index build...');
    } else {
      console.log(`ℹ️  Server request failed (${err.message}). Performing direct local index build...`);
    }
    execSync('node server.mjs --index-only', { cwd: APP_DIR, stdio: 'inherit' });
    console.log('✅ Direct index build complete!');
  }
}

main();
