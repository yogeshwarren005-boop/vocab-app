import http from 'node:http';
import fs from 'node:fs';
import fsp from 'node:fs/promises';
import path from 'node:path';
import zlib from 'node:zlib';
import { fileURLToPath } from 'node:url';
import { gitSync } from './git-sync.mjs';
import { getWordFrequency } from './scripts/frequency-engine.mjs';
import { getClusterTier } from './scripts/cluster-tier-map.mjs';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const DEFAULT_APP_DB = path.resolve(__dirname, '..', 'App database');
const VAULT_ROOT = process.env.VAULT_PATH || (fs.existsSync(DEFAULT_APP_DB) ? DEFAULT_APP_DB : 'D:\\Language');
const PORT = Number(process.env.PORT || 3080);
const AUTH_TOKEN = (process.env.AUTH_TOKEN || process.env.VAULT_PASSWORD || '').trim();
const PUBLIC_DIR = path.join(__dirname, 'public');
const DATA_DIR = path.join(PUBLIC_DIR, 'data');
const STYLES_DIR = path.join(PUBLIC_DIR, 'styles');
const BANNERS_DIR = path.join(PUBLIC_DIR, 'assets', 'banners');
const STATUS_DB_PATH = path.join(DATA_DIR, 'status-db.json');
const exploreServerCache = new Map();

// Strictly exclude non-vocabulary roots and system directories (pure vocabulary vault only: Greek, Latin, Vocab Master)
const EXCLUDED_ROOT_DIRS = new Set([
  'Content',
  '_archive',
  '.obsidian',
  '.git',
  '.gemini',
  'Apps',
  'node_modules',
  'Basic English',
  'Advanced english',
  'Philosophy'
]);

const EXCLUDED_ROOT_FILES = new Set([
  'Untitled.md',
  'Kernel Expansion.md',
  'Notion Superpowers & Fast Reading Guide.md',
  '.gitignore'
]);

// Core vault structure — these top-level folders cannot be deleted from the web app
const PROTECTED_ROOT_FOLDERS = new Set([
  'English vocabulary master',
  'Greek roots',
  'Latin roots'
]);

// Case-insensitive lookups for Windows filesystem security
const EXCLUDED_ROOT_DIRS_LOWER = new Set(
  Array.from(EXCLUDED_ROOT_DIRS).map(d => d.toLowerCase())
);
const EXCLUDED_ROOT_FILES_LOWER = new Set(
  Array.from(EXCLUDED_ROOT_FILES).map(f => f.toLowerCase())
);
const PROTECTED_ROOT_FOLDERS_LOWER = new Set(
  Array.from(PROTECTED_ROOT_FOLDERS).map(f => f.toLowerCase())
);

// Reserved Windows DOS device names
const DOS_DEVICE_REGEX = /^(CON|PRN|AUX|NUL|COM[1-9]|LPT[1-9])(\..*)?$/i;

// Top-level safety handlers to prevent unhandled rejections from crashing the server
process.on('uncaughtException', (err) => {
  console.error('💥 Uncaught Exception caught by server safety handler:', err);
});
process.on('unhandledRejection', (reason) => {
  console.error('💥 Unhandled Rejection caught by server safety handler:', reason);
});

/**
 * Safe URI decoder that handles single and double-encoded URIs,
 * Unicode/Greek/Latin characters, spaces, and catches URIError safely.
 */
function safeUriDecode(str) {
  if (!str || typeof str !== 'string') return '';
  let decoded = str;
  for (let i = 0; i < 2; i++) {
    if (!decoded.includes('%')) break;
    try {
      const next = decodeURIComponent(decoded);
      if (next === decoded) break;
      decoded = next;
    } catch {
      // String contains literal '%' not representing valid escape sequence
      break;
    }
  }
  return decoded;
}

/**
 * Robust CORS headers accommodating Capacitor Android (capacitor://localhost, http://localhost)
 * and web/desktop origins.
 */
function getCorsHeaders(req) {
  const origin = req?.headers?.origin;
  const isSpecificOrigin = Boolean(origin && origin !== 'null');
  const headers = {
    'Access-Control-Allow-Origin': isSpecificOrigin ? origin : '*',
    'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, PATCH, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type, Authorization, X-Requested-With, Accept, Origin',
    'Access-Control-Max-Age': '86400',
    'Vary': 'Origin, Accept-Encoding'
  };
  if (isSpecificOrigin) {
    headers['Access-Control-Allow-Credentials'] = 'true';
  }
  return headers;
}

// Pre-compiled regexes for maximum frontmatter & link extraction throughput
const LIST_ITEM_REGEX = /^\s+-\s+(.*)$/;
const KEY_VAL_REGEX = /^([A-Za-z0-9_.-]+)\s*:\s*(.*)$/;
const NUMERIC_REGEX = /^[\d.]+$/;
const WIKILINK_REGEX = /\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]/g;

/**
 * Fast frontmatter parser reading only the header block of a markdown string
 */
function parseFrontmatter(rawHeader) {
  if (!rawHeader) return {};
  let h = rawHeader;
  if (h.charCodeAt(0) === 0xFEFF) h = h.slice(1);
  if (!h.startsWith('---')) return {};
  const endIdx = h.indexOf('\n---', 3);
  if (endIdx === -1) return {};
  const yamlBlock = h.slice(3, endIdx).replace(/\r/g, '');
  const lines = yamlBlock.split('\n');
  const fm = {};
  let currentKey = null;
  let currentList = null;

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    const trimmed = line.trim();
    if (!trimmed || trimmed.startsWith('#')) continue;

    const listMatch = line.match(LIST_ITEM_REGEX);
    if (listMatch && currentKey) {
      if (!currentList) {
        currentList = [];
        fm[currentKey] = currentList;
      }
      currentList.push(cleanYamlVal(listMatch[1]));
      continue;
    }

    const kvMatch = line.match(KEY_VAL_REGEX);
    if (kvMatch) {
      currentKey = kvMatch[1];
      const val = kvMatch[2].trim();
      if (val === '') {
        currentList = [];
        fm[currentKey] = currentList;
      } else {
        currentList = null;
        fm[currentKey] = cleanYamlVal(val);
      }
    }
  }
  return fm;
}

function cleanYamlVal(val) {
  let v = val.trim();
  if ((v.startsWith('"') && v.endsWith('"')) || (v.startsWith("'") && v.endsWith("'"))) {
    v = v.slice(1, -1);
  }
  if (v === 'true') return true;
  if (v === 'false') return false;
  if (v !== '' && !Number.isNaN(Number(v)) && NUMERIC_REGEX.test(v)) return Number(v);
  return v;
}

/**
 * Update or insert a frontmatter key in a Markdown file content string
 */
function updateMarkdownFrontmatter(content, updates) {
  const hasCrlf = content.includes('\r\n');
  const nl = hasCrlf ? '\r\n' : '\n';
  if (content.startsWith('---')) {
    const match = content.match(/^---\r?\n([\s\S]*?)\r?\n---(\r?\n|$)/);
    if (match) {
      let yamlLines = match[1].split(/\r?\n/);
      for (const [k, v] of Object.entries(updates)) {
        const keyRegex = new RegExp(`^${k}\\s*:`);
        const idx = yamlLines.findIndex(l => keyRegex.test(l));
        const formattedVal = typeof v === 'string' && (v.includes('[[') || v.includes(':')) ? `"${v}"` : v;
        if (idx !== -1) {
          yamlLines[idx] = `${k}: ${formattedVal}`;
        } else {
          yamlLines.push(`${k}: ${formattedVal}`);
        }
      }
      const rest = content.slice(match[0].length);
      return `---${nl}${yamlLines.join(nl)}${nl}---${nl}${rest}`;
    }
  }
  const yamlLines = Object.entries(updates).map(([k, v]) => `${k}: ${v}`);
  return `---${nl}${yamlLines.join(nl)}${nl}---${nl}${nl}${content}`;
}

/**
 * Copy and sanitize user's custom CSS snippets & banner assets from D:\Language
 */
async function syncVaultDesignAssets() {
  await fsp.mkdir(STYLES_DIR, { recursive: true });
  await fsp.mkdir(BANNERS_DIR, { recursive: true });
  await fsp.mkdir(DATA_DIR, { recursive: true });

  const snippetsDir = path.join(VAULT_ROOT, '.obsidian', 'snippets');
  const snippetFiles = [
    'web-colors.css',
    'web-layout.css',
    'web-typography.css',
    'web-components.css',
    'web-interactive.css',
    'web-reading-view.css',
    'language-folders-highlight.css',
    'vault-theme.css',
    'apple-toggle.css'
  ];

  for (const file of snippetFiles) {
    const srcPath = path.join(snippetsDir, file);
    if (fs.existsSync(srcPath)) {
      let css = await fsp.readFile(srcPath, 'utf8');
      if (file === 'language-folders-highlight.css') {
        css = css.replace(/\/\* =+\s*SECTION 3:.*?\/\* Ensure folder titles/s, '/* Ensure folder titles');
      }
      await fsp.writeFile(path.join(STYLES_DIR, file), css, 'utf8');
    }
  }

  const vaultBannersDir = path.join(VAULT_ROOT, '_assets', 'banners');
  if (fs.existsSync(vaultBannersDir)) {
    const entries = await fsp.readdir(vaultBannersDir, { withFileTypes: true });
    for (const entry of entries) {
      if (entry.isFile() && /\.(jpg|jpeg|png|webp)$/i.test(entry.name) && !entry.name.toLowerCase().includes('content')) {
        await fsp.copyFile(
          path.join(vaultBannersDir, entry.name),
          path.join(BANNERS_DIR, entry.name)
        );
      }
    }
  }
}

/**
 * Filter out Content Studio references from note markdown (e.g., 00 Language Hub.md line 357)
 */
function sanitizeNoteContent(relPath, markdown) {
  if (relPath === '00 Language Hub.md') {
    return markdown
      .split('\n')
      .filter(line => !line.includes('Content Studio') && !line.includes('[[Content/'))
      .join('\n');
  }
  return markdown;
}

// Persistent status overrides map synced with disk files
let statusDb = {};
let vaultIndex = {
  generatedAt: '',
  totalNotes: 0,
  pages: [],
  links: [],
  coreNotes: {}
};
let pageMapByPath = new Map();

/**
 * Safely writes a file atomically via a temporary file in the same directory,
 * followed by an atomic rename with retries for Windows file lock tolerance.
 */
async function writeFileAtomic(targetPath, data, encoding = 'utf8') {
  const dir = path.dirname(targetPath);
  await fsp.mkdir(dir, { recursive: true });
  const tempPath = path.join(dir, `.${path.basename(targetPath)}.${Date.now()}.${Math.random().toString(36).slice(2, 8)}.tmp`);

  await fsp.writeFile(tempPath, data, encoding);

  let retries = 5;
  while (retries > 0) {
    try {
      await fsp.rename(tempPath, targetPath);
      return;
    } catch (err) {
      retries--;
      if (retries === 0) {
        try {
          await fsp.copyFile(tempPath, targetPath);
          await fsp.unlink(tempPath).catch(() => {});
          return;
        } catch {
          await fsp.unlink(tempPath).catch(() => {});
          throw err;
        }
      }
      await new Promise(r => setTimeout(r, 25));
    }
  }
}

async function loadStatusDb() {
  if (fs.existsSync(STATUS_DB_PATH)) {
    try {
      const diskData = JSON.parse(await fsp.readFile(STATUS_DB_PATH, 'utf8'));
      // Merge disk data with in-memory overrides so active session updates are preserved
      statusDb = { ...diskData, ...statusDb };
    } catch (e) {
      console.warn('Status DB load notice:', e.message);
    }
  }
}

let statusDbSaveQueue = Promise.resolve();

function saveStatusDb() {
  statusDbSaveQueue = statusDbSaveQueue.then(async () => {
    try {
      await writeFileAtomic(STATUS_DB_PATH, JSON.stringify(statusDb, null, 2), 'utf8');
    } catch (err) {
      console.warn('Failed to save status-db:', err.message);
    }
  });
  return statusDbSaveQueue;
}

let activeIndexBuildPromise = null;

/**
 * Mutex-protected vault indexer entrypoint: ensures multiple concurrent rebuild requests
 * (e.g. from watcher + API) share a single in-flight build rather than overlapping.
 */
async function buildVaultIndex(forceRebuild = false) {
  if (activeIndexBuildPromise) {
    return activeIndexBuildPromise;
  }
  activeIndexBuildPromise = _executeVaultIndex(forceRebuild);
  try {
    return await activeIndexBuildPromise;
  } finally {
    activeIndexBuildPromise = null;
  }
}

/**
 * Ultra-fast Vault Indexer:
 * Scans vault hierarchy with hoisted directory checks, infers deterministic metadata
 * for ~50,000 classical root files, and reads ~1,480 core notes with a concurrent I/O pool.
 */
async function _executeVaultIndex(forceRebuild = false) {
  await loadStatusDb();
  const indexCachePath = path.join(DATA_DIR, 'vault-index.json');
  const coreNotesCachePath = path.join(DATA_DIR, 'core-notes.json');

  if (!forceRebuild && fs.existsSync(indexCachePath) && fs.existsSync(coreNotesCachePath)) {
    try {
      console.log('⚡ Loading cached vault index...');
      const cachedIndex = JSON.parse(await fsp.readFile(indexCachePath, 'utf8'));
      const cachedCore = JSON.parse(await fsp.readFile(coreNotesCachePath, 'utf8'));
      cachedIndex.pages = (cachedIndex.pages || []).filter(p => !p.p.includes('/scripts/'));
      cachedIndex.totalNotes = cachedIndex.pages.length;
      vaultIndex = { ...cachedIndex, coreNotes: cachedCore };
      pageMapByPath.clear();
      for (const p of vaultIndex.pages) {
        if (statusDb[p.p]) p.s = statusDb[p.p];
        pageMapByPath.set(p.p, p);
      }
      console.log(`✅ Loaded ${vaultIndex.totalNotes.toLocaleString()} vault notes from cache.`);
      return;
    } catch (e) {
      console.warn('Cache read failed, rebuilding index...', e.message);
    }
  }

  console.log(`🔍 Scanning Obsidian vault at ${VAULT_ROOT} (excluding Content Studio)...`);
  const t0 = Date.now();
  const pages = [];
  const coreNotes = {};
  const rawLinks = [];
  const coreNotesToRead = [];

  function walkDir(absDir, relDir, dirParts = null) {
    let entries;
    try {
      entries = fs.readdirSync(absDir, { withFileTypes: true });
    } catch {
      return;
    }

    const parts = dirParts !== null ? dirParts : (relDir ? relDir.split('/') : []);
    const topFolder = parts[0] || '';
    const isClassicalRoot = topFolder === 'Greek roots' || topFolder === 'Latin roots';
    const clusterIdx = parts.findIndex(p => p.startsWith('Cluster '));
    const isDeepClassical = isClassicalRoot && clusterIdx !== -1;
    const clusterName = isDeepClassical ? parts[clusterIdx] : '';
    const rootFolderName = isDeepClassical ? (parts[clusterIdx + 1] || '') : '';
    const isClusterMocDir = isDeepClassical && parts.length === clusterIdx + 1;
    const clusterTier = isDeepClassical ? getClusterTier(topFolder, clusterName) : null;

    for (const entry of entries) {
      const name = entry.name;
      if (name.startsWith('.')) continue;
      const relPath = relDir ? `${relDir}/${name}` : name;
      const absPath = path.join(absDir, name);

      if (entry.isDirectory()) {
        if ((!relDir && (EXCLUDED_ROOT_DIRS.has(name) || EXCLUDED_ROOT_DIRS_LOWER.has(name.toLowerCase()))) || name === 'scripts') continue;
        const nextParts = parts.length === 0 ? [name] : [...parts, name];
        walkDir(absPath, relPath, nextParts);
      } else if (entry.isFile() && name.endsWith('.md')) {
        if (!relDir && (EXCLUDED_ROOT_FILES.has(name) || EXCLUDED_ROOT_FILES_LOWER.has(name.toLowerCase()))) continue;

        const baseName = name.slice(0, -3);
        const freq = getWordFrequency(baseName);

        if (isDeepClassical) {
          const pageObj = {
            p: relPath,
            s: statusDb[relPath] || 'unread',
            f: freq.tier,
            z: freq.zipf,
            rk: freq.rank
          };

          if (isClusterMocDir && baseName.startsWith('Cluster ')) {
            pageObj.f = clusterTier || 2;
            coreNotesToRead.push({ absPath, relPath, pageObj, isClusterMoc: true, parts, clusterTier });
          } else if (baseName.startsWith('Dashboard')) {
            pageObj.t = 'root_dashboard';
            pageObj.c = `[[${clusterName}]]`;
            pageObj.f = clusterTier || 2;
            const clusterRelDir = parts.slice(0, clusterIdx + 1).join('/');
            rawLinks.push([`${clusterRelDir}/${clusterName}.md`, relPath]);
            pages.push(pageObj);
          } else if (baseName.startsWith('Word Triage')) {
            pageObj.t = 'word_triage';
            pageObj.c = `[[${clusterName}]]`;
            pageObj.f = clusterTier || 2;
            pages.push(pageObj);
          } else {
            pageObj.c = `[[${clusterName}]]`;
            const rootLink = `[[${rootFolderName || baseName}]]`;
            if (topFolder === 'Latin roots') {
              pageObj.lr = rootLink;
            } else {
              pageObj.gr = rootLink;
            }
            pages.push(pageObj);
          }
          continue;
        }

        const clusterPart = parts.find(p => p.startsWith('Cluster '));
        const nonClassicalClusterTier = clusterPart ? getClusterTier(topFolder, clusterPart) : (freq.tier || 2);
        const pageObj = {
          p: relPath,
          f: freq.tier,
          z: freq.zipf,
          rk: freq.rank
        };
        coreNotesToRead.push({ absPath, relPath, pageObj, isClusterMoc: false, parts, clusterTier: nonClassicalClusterTier });
      }
    }
  }

  walkDir(VAULT_ROOT, '');

  // Concurrency pool for reading core notes
  const CONCURRENCY = 48;
  let idx = 0;
  async function worker() {
    while (idx < coreNotesToRead.length) {
      const item = coreNotesToRead[idx++];
      try {
        const fullText = await fsp.readFile(item.absPath, 'utf8');
        if (item.isClusterMoc) {
          const fm = parseFrontmatter(fullText.slice(0, 800));
          if (fm.status) item.pageObj.s = statusDb[item.relPath] || String(fm.status);
          if (fm.type) item.pageObj.t = String(fm.type);
          item.coreText = fullText;
        } else {
          const fm = parseFrontmatter(fullText.slice(0, 1200));
          item.coreText = sanitizeNoteContent(item.relPath, fullText);

          const linkRegex = new RegExp(WIKILINK_REGEX.source, 'g');
          let m;
          let count = 0;
          const noteLinks = [];
          while ((m = linkRegex.exec(fullText)) !== null && count < 45) {
            const target = m[1].trim();
            if (target && !target.startsWith('Content') && !target.endsWith('.jpg') && !target.endsWith('.png')) {
              noteLinks.push([item.relPath, target]);
              count++;
            }
          }
          item.noteLinks = noteLinks;

          if (statusDb[item.relPath]) {
            item.pageObj.s = statusDb[item.relPath];
          } else if (fm.status !== undefined) {
            item.pageObj.s = String(fm.status);
          }
          if (fm.type) item.pageObj.t = String(fm.type);
          if (fm.cluster) {
            item.pageObj.c = String(fm.cluster);
          } else {
            const clusterPart = item.parts.find(p => p.startsWith('Cluster '));
            if (clusterPart) item.pageObj.c = `[[${clusterPart}]]`;
          }
          if (fm.latin_root) item.pageObj.lr = String(fm.latin_root);
          if (fm.greek_root) item.pageObj.gr = String(fm.greek_root);
          if (fm.section) item.pageObj.sec = String(fm.section);
          if (fm.tags) item.pageObj.tg = Array.isArray(fm.tags) ? fm.tags : [String(fm.tags)];
          if (fm.aliases) item.pageObj.al = Array.isArray(fm.aliases) ? fm.aliases : [String(fm.aliases)];
          if (fm.cssclasses) item.pageObj.css = Array.isArray(fm.cssclasses) ? fm.cssclasses : [String(fm.cssclasses)];
          if (fm.banner) item.pageObj.b = String(fm.banner);
          if (fm.banner_icon) item.pageObj.bi = String(fm.banner_icon);
          if (fm.banner_y !== undefined) item.pageObj.by = fm.banner_y;
        }
      } catch {
        // ignore read errors on locked or unreadable files
      }
    }
  }

  const workers = Array.from({ length: CONCURRENCY }, () => worker());
  await Promise.all(workers);

  // Deterministically append collected core notes
  for (const item of coreNotesToRead) {
    pages.push(item.pageObj);
    if (item.coreText !== undefined) {
      coreNotes[item.relPath] = item.coreText;
    }
    if (item.noteLinks) {
      for (let i = 0; i < item.noteLinks.length; i++) {
        rawLinks.push(item.noteLinks[i]);
      }
    }
  }

  pages.sort((a, b) => a.p.localeCompare(b.p));
  pageMapByPath.clear();
  for (const p of pages) {
    if (statusDb[p.p]) p.s = statusDb[p.p];
    pageMapByPath.set(p.p, p);
  }

  const indexPayload = {
    generatedAt: new Date().toISOString(),
    totalNotes: pages.length,
    pages,
    links: rawLinks
  };

  vaultIndex = { ...indexPayload, coreNotes };

  await writeFileAtomic(indexCachePath, JSON.stringify(indexPayload), 'utf8');
  await writeFileAtomic(coreNotesCachePath, JSON.stringify(coreNotes), 'utf8');

  const elapsed = ((Date.now() - t0) / 1000).toFixed(2);
  console.log(`✅ Indexed ${pages.length.toLocaleString()} notes & ${Object.keys(coreNotes).length} preloaded core notes in ${elapsed}s.`);
}

const MIME_TYPES = {
  '.html': 'text/html; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.js': 'application/javascript; charset=utf-8',
  '.mjs': 'application/javascript; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.png': 'image/png',
  '.webp': 'image/webp',
  '.gif': 'image/gif',
  '.svg': 'image/svg+xml',
  '.ico': 'image/x-icon',
  '.woff': 'font/woff',
  '.woff2': 'font/woff2',
  '.ttf': 'font/ttf',
  '.otf': 'font/otf',
  '.mp3': 'audio/mpeg',
  '.wav': 'audio/wav',
  '.ogg': 'audio/ogg',
  '.mp4': 'video/mp4',
  '.webm': 'video/webm',
  '.txt': 'text/plain; charset=utf-8',
  '.md': 'text/markdown; charset=utf-8',
  '.webmanifest': 'application/manifest+json'
};

function sendJson(req, res, status, data, extraHeaders = {}) {
  if (res.writableEnded || res.destroyed) return;
  let json;
  try {
    json = JSON.stringify(data);
  } catch (err) {
    console.error('Failed to stringify JSON response:', err);
    json = JSON.stringify({ error: 'Serialization error' });
    status = 500;
  }

  const corsHeaders = getCorsHeaders(req);
  const acceptEncoding = req.headers?.['accept-encoding'] || '';

  if (acceptEncoding.includes('gzip') && json.length > 2048) {
    zlib.gzip(Buffer.from(json), (err, compressed) => {
      if (res.writableEnded || res.destroyed) return;
      if (err) {
        console.warn('Gzip compression error in sendJson, falling back to uncompressed:', err.message);
        res.writeHead(status, {
          'Content-Type': 'application/json; charset=utf-8',
          ...corsHeaders,
          ...extraHeaders
        });
        res.end(json);
        return;
      }
      res.writeHead(status, {
        'Content-Type': 'application/json; charset=utf-8',
        'Content-Encoding': 'gzip',
        ...corsHeaders,
        ...extraHeaders
      });
      res.end(compressed);
    });
  } else {
    res.writeHead(status, {
      'Content-Type': 'application/json; charset=utf-8',
      ...corsHeaders,
      ...extraHeaders
    });
    res.end(json);
  }
}

function readRequestBody(req) {
  return new Promise((resolve, reject) => {
    const chunks = [];
    let size = 0;
    req.on('data', chunk => {
      size += chunk.length;
      if (size > 25 * 1024 * 1024) { // 25MB safety limit
        req.destroy(new Error('Payload too large'));
        reject(new Error('Payload too large'));
        return;
      }
      chunks.push(chunk);
    });
    req.on('end', () => {
      try {
        const raw = Buffer.concat(chunks).toString('utf8');
        resolve(raw ? JSON.parse(raw) : {});
      } catch (e) {
        reject(new Error('Invalid JSON payload: ' + e.message));
      }
    });
    req.on('error', reject);
  });
}

function resolveSafeVaultPath(relPath) {
  if (!relPath || typeof relPath !== 'string') {
    const err = new Error('Invalid path: path must be a non-empty string');
    err.statusCode = 400;
    throw err;
  }

  // 1. Forbid null bytes immediately
  if (relPath.includes('\0')) {
    const err = new Error('Invalid path: null bytes are forbidden');
    err.statusCode = 400;
    throw err;
  }

  // 2. Decode URI components safely
  const decoded = safeUriDecode(relPath).trim();
  if (decoded.includes('\0')) {
    const err = new Error('Invalid path: null bytes are forbidden');
    err.statusCode = 400;
    throw err;
  }

  // 3. Normalize slashes and reject drive-letter/UNC paths on Windows
  let cleaned = decoded.replace(/\\/g, '/');
  if (/^[a-zA-Z]:/.test(cleaned) || cleaned.startsWith('//')) {
    const err = new Error('Path traversal forbidden: absolute or drive-specified path');
    err.statusCode = 403;
    throw err;
  }

  // Strip leading slashes
  cleaned = cleaned.replace(/^\/+/, '');

  // 4. Resolve absolute path strictly within VAULT_ROOT
  const resolvedRoot = path.resolve(VAULT_ROOT);
  const absPath = path.resolve(resolvedRoot, cleaned);

  // 5. Enforce boundary checking with trailing separator
  const rootWithSep = resolvedRoot.endsWith(path.sep) ? resolvedRoot : resolvedRoot + path.sep;
  const isWindows = process.platform === 'win32';

  const isWithinVault = isWindows
    ? (absPath.toLowerCase() === resolvedRoot.toLowerCase() || absPath.toLowerCase().startsWith(rootWithSep.toLowerCase()))
    : (absPath === resolvedRoot || absPath.startsWith(rootWithSep));

  if (!isWithinVault) {
    const err = new Error('Path traversal forbidden: outside vault root');
    err.statusCode = 403;
    throw err;
  }

  // 6. Compute exact relative path from VAULT_ROOT
  const relFromRoot = path.relative(resolvedRoot, absPath).replace(/\\/g, '/');
  if (relFromRoot.startsWith('..') || path.isAbsolute(relFromRoot)) {
    const err = new Error('Path traversal forbidden: relative traversal');
    err.statusCode = 403;
    throw err;
  }

  // 7. Check for forbidden/excluded top-level directories & files (case-insensitive)
  const topSegment = relFromRoot.split('/')[0] || '';
  if (topSegment && EXCLUDED_ROOT_DIRS_LOWER.has(topSegment.toLowerCase())) {
    const err = new Error(`Access to excluded directory "${topSegment}" is forbidden`);
    err.statusCode = 403;
    throw err;
  }
  if (relFromRoot && EXCLUDED_ROOT_FILES_LOWER.has(relFromRoot.toLowerCase())) {
    const err = new Error(`Access to excluded file "${relFromRoot}" is forbidden`);
    err.statusCode = 403;
    throw err;
  }

  // 8. Reject DOS reserved device names
  const segments = relFromRoot.split('/');
  for (const seg of segments) {
    if (DOS_DEVICE_REGEX.test(seg)) {
      const err = new Error(`Invalid path: "${seg}" is a reserved system device name`);
      err.statusCode = 400;
      throw err;
    }
  }

  return { normalized: relFromRoot, absPath };
}

/* ============================================================================
   INCREMENTAL VAULT INDEX UPDATES (create / rename / delete without full rescan)
   ============================================================================ */

function renamePathInIndex(from, to) {
  const isFolder = !from.endsWith('.md');
  const prefix = from + '/';
  const match = p => (isFolder ? p.startsWith(prefix) : p === from);
  const remap = p => (isFolder ? to + p.slice(from.length) : to);

  for (const entry of vaultIndex.pages) {
    if (match(entry.p)) {
      pageMapByPath.delete(entry.p);
      entry.p = remap(entry.p);
      pageMapByPath.set(entry.p, entry);
    }
  }
  for (const key of Object.keys(vaultIndex.coreNotes)) {
    if (match(key)) {
      vaultIndex.coreNotes[remap(key)] = vaultIndex.coreNotes[key];
      delete vaultIndex.coreNotes[key];
    }
  }
  for (const link of vaultIndex.links) {
    if (match(link[0])) link[0] = remap(link[0]);
    if (link[1] === from) link[1] = to;
  }
  let statusChanged = false;
  for (const key of Object.keys(statusDb)) {
    if (match(key)) {
      statusDb[remap(key)] = statusDb[key];
      delete statusDb[key];
      statusChanged = true;
    }
  }
  if (statusChanged) {
    return saveStatusDb();
  }
}

function removePathFromIndex(target) {
  const isFolder = !target.endsWith('.md');
  const prefix = target + '/';
  vaultIndex.pages = vaultIndex.pages.filter(p => {
    const hit = isFolder ? p.p.startsWith(prefix) : p.p === target;
    if (hit) pageMapByPath.delete(p.p);
    return !hit;
  });
  for (const key of Object.keys(vaultIndex.coreNotes)) {
    if (isFolder ? key.startsWith(prefix) : key === target) delete vaultIndex.coreNotes[key];
  }
  vaultIndex.links = vaultIndex.links.filter(l =>
    !(isFolder ? l[0].startsWith(prefix) : l[0] === target)
  );
  let statusChanged = false;
  for (const key of Object.keys(statusDb)) {
    if (isFolder ? key.startsWith(prefix) : key === target) {
      delete statusDb[key];
      statusChanged = true;
    }
  }
  if (statusChanged) {
    return saveStatusDb();
  }
}

function addPathToIndex(normalized, content) {
  if (pageMapByPath.has(normalized)) return;
  const entry = { p: normalized, s: statusDb[normalized] || 'unread' };
  vaultIndex.pages.push(entry);
  vaultIndex.pages.sort((a, b) => a.p.localeCompare(b.p));
  pageMapByPath.set(normalized, entry);
  vaultIndex.totalNotes = vaultIndex.pages.length;
  if (typeof content === 'string') {
    vaultIndex.coreNotes[normalized] = content;
  }
}

let indexRebuildTimer = null;
let indexRebuildRunning = false;
let indexRebuildPending = false;

/**
 * Structural changes (create/rename/delete) or external disk edits mutate the in-memory index,
 * with debounced full rebuild to refresh the on-disk cache.
 * Uses a state machine (running + pending flag) to guarantee:
 * 1. Debouncing of rapid bursts of events
 * 2. Never running overlapping index builds
 * 3. Never dropping change events that arrive while an index build is in progress
 */
function scheduleIndexRebuild(delay = 1200) {
  clearTimeout(indexRebuildTimer);
  indexRebuildTimer = setTimeout(() => {
    (async () => {
      if (indexRebuildRunning) {
        indexRebuildPending = true;
        return;
      }
      indexRebuildRunning = true;
      indexRebuildPending = false;
      try {
        await buildVaultIndex(true);
        console.log('♻️  Vault index rebuilt after vault change.');
      } catch (e) {
        console.warn('Index rebuild failed:', e.message);
      } finally {
        indexRebuildRunning = false;
        if (indexRebuildPending) {
          indexRebuildPending = false;
          scheduleIndexRebuild(500);
        }
      }
    })().catch(err => {
      console.warn('scheduleIndexRebuild background error:', err.message);
    });
  }, delay);
}

/**
 * Live File Watcher: monitors App database for additions, edits, and deletions
 * so any updates made via Obsidian, editors, or external scripts are reflected live.
 */
function setupVaultWatcher() {
  try {
    if (!fs.existsSync(VAULT_ROOT)) return;
    const watcher = fs.watch(VAULT_ROOT, { recursive: true }, (eventType, filename) => {
      if (!filename) return;
      const normalized = filename.replace(/\\/g, '/');
      if (normalized.startsWith('.') || normalized.includes('/.') || normalized.startsWith('_')) return;

      const topSegment = normalized.split('/')[0];
      const topSegmentLower = topSegment.toLowerCase();
      if (EXCLUDED_ROOT_DIRS.has(topSegment) || EXCLUDED_ROOT_DIRS_LOWER.has(topSegmentLower)) return;
      if (EXCLUDED_ROOT_FILES.has(normalized) || EXCLUDED_ROOT_FILES_LOWER.has(normalized.toLowerCase())) return;

      const isMd = normalized.endsWith('.md');
      const isJson = normalized.endsWith('.json');
      const isDirChange = !path.extname(normalized);

      if (!isMd && !isJson && !isDirChange) return;

      console.log(`📡 Vault change detected [${eventType}]: ${normalized}`);
      scheduleIndexRebuild();
    });
    watcher.on('error', (err) => {
      console.warn('Vault watcher notice:', err.message);
    });
    console.log(`👀 Live Vault Watcher active on: ${VAULT_ROOT}`);
  } catch (err) {
    console.warn('Could not setup recursive vault watcher:', err.message);
  }
}

async function startServer() {
  await syncVaultDesignAssets();
  await buildVaultIndex(process.argv.includes('--index-only') || process.argv.includes('--rebuild'));

  if (process.argv.includes('--index-only')) {
    console.log('Index build complete.');
    process.exit(0);
  }

  setupVaultWatcher();

  // Initialize Bi-directional Git Auto-Sync Engine
  try {
    await gitSync.init(VAULT_ROOT, {
      onNewCommits: () => {
        console.log('🔄 Rebuilding vault index after Git pull...');
        scheduleIndexRebuild();
      }
    });
  } catch (gitErr) {
    console.warn('⚠️ Git Auto-Sync initialization notice:', gitErr.message);
  }

  const server = http.createServer(async (req, res) => {
    req.on('error', (err) => {
      console.warn('HTTP request stream error:', err.message);
    });
    res.on('error', (err) => {
      console.warn('HTTP response stream error:', err.message);
    });

    try {
      if (req.method === 'OPTIONS') {
        res.writeHead(204, getCorsHeaders(req));
        res.end();
        return;
      }

      const urlObj = new URL(req.url, `http://${req.headers.host || 'localhost'}`);
      let pathname = urlObj.pathname;
      try {
        pathname = decodeURIComponent(urlObj.pathname);
      } catch {
        // Fallback to raw pathname if decodeURIComponent fails
      }

      // Auth Guard: Protect all /api/* endpoints (except auth routes) if AUTH_TOKEN is set
      if (AUTH_TOKEN && pathname.startsWith('/api/') && !pathname.startsWith('/api/auth/')) {
        const authHeader = req.headers['authorization'] || '';
        const tokenQuery = urlObj.searchParams.get('token');
        const tokenCookie = (req.headers.cookie || '')
          .split(';')
          .map(c => c.trim())
          .find(c => c.startsWith('auth_token='))
          ?.split('=')[1];
        const providedToken = authHeader.replace(/^Bearer\s+/i, '').trim() || tokenQuery || tokenCookie;

        if (providedToken !== AUTH_TOKEN) {
          sendJson(req, res, 401, { error: 'Unauthorized: Valid vault passcode or token required' });
          return;
        }
      }

      // 0. API: Auth Verification & Login
      if (pathname === '/api/auth/status' && req.method === 'GET') {
        sendJson(req, res, 200, {
          authRequired: Boolean(AUTH_TOKEN),
          authenticated: !AUTH_TOKEN
        });
        return;
      }

      if (pathname === '/api/auth/login' && req.method === 'POST') {
        const body = await readRequestBody(req);
        const inputPass = String(body.password || body.token || '').trim();
        if (!AUTH_TOKEN || inputPass === AUTH_TOKEN) {
          const corsHeaders = getCorsHeaders(req);
          res.writeHead(200, {
            'Content-Type': 'application/json; charset=utf-8',
            'Set-Cookie': `auth_token=${encodeURIComponent(AUTH_TOKEN || 'open')}; Path=/; HttpOnly; SameSite=Lax; Max-Age=31536000`,
            ...corsHeaders
          });
          res.end(JSON.stringify({ ok: true, token: AUTH_TOKEN || 'open' }));
        } else {
          sendJson(req, res, 401, { error: 'Invalid vault passcode' });
        }
        return;
      }

      // 0b. API: Git Sync Status & Manual Sync
      if (pathname === '/api/sync' && req.method === 'GET') {
        sendJson(req, res, 200, gitSync.getStatus());
        return;
      }

      if (pathname === '/api/sync' && req.method === 'POST') {
        const syncResult = await gitSync.manualSync();
        sendJson(req, res, 200, syncResult);
        return;
      }

      // 1. API: Vault Status & Index
      if (pathname === '/api/vault-index' && req.method === 'GET') {
        sendJson(req, res, 200, {
          generatedAt: vaultIndex.generatedAt,
          totalNotes: vaultIndex.totalNotes,
          pages: vaultIndex.pages,
          links: vaultIndex.links,
          liveSync: true
        });
        return;
      }

      // 2. API: Read Single Note Content
      if (pathname === '/api/note' && req.method === 'GET') {
        const rawQuery = urlObj.searchParams.get('path');
        const relQuery = rawQuery ? safeUriDecode(rawQuery) : '00 Language Hub.md';
        const { normalized, absPath } = resolveSafeVaultPath(relQuery);
        if (!fs.existsSync(absPath)) {
          sendJson(req, res, 404, { error: `Note not found: ${normalized}` });
          return;
        }
        const rawContent = await fsp.readFile(absPath, 'utf8');
        const content = sanitizeNoteContent(normalized, rawContent);
        const stat = await fsp.stat(absPath);
        sendJson(req, res, 200, {
          path: normalized,
          content,
          mtime: stat.mtimeMs
        });
        return;
      }

      // 2b. API: Explore Aggregator Proxy & Cache (Zero-CAPTCHA Fast-Path)
      if (pathname === '/api/explore' && req.method === 'GET') {
        const q = String(urlObj.searchParams.get('q') || '').trim().toLowerCase();
        if (!q) {
          sendJson(req, res, 400, { error: 'Query parameter q is required' });
          return;
        }

        const nocache = urlObj.searchParams.get('nocache') === '1' || urlObj.searchParams.get('refresh') === '1';
        if (!nocache && exploreServerCache.has(q)) {
          sendJson(req, res, 200, exploreServerCache.get(q));
          return;
        }

        try {
          const cleanCap = q.charAt(0).toUpperCase() + q.slice(1);
          const controller = new AbortController();
          const timeoutId = setTimeout(() => controller.abort(), 8000);
          const fetchOpt = {
            signal: controller.signal,
            headers: { 'Accept': 'application/json', 'User-Agent': 'VocabMasterMobile/2.0' }
          };

          const [wikiRes, dataSynRes, dataDefRes, dataRelatedRes, wiktRes, suggestRes, booksRes, ytRes, wikiImgsRes] = await Promise.all([
            fetch(`https://en.wikipedia.org/api/rest_v1/page/summary/${encodeURIComponent(cleanCap)}`, fetchOpt)
              .then(r => r.ok ? r.json() : null).catch(() => null),
            fetch(`https://api.datamuse.com/words?rel_syn=${encodeURIComponent(q)}&max=10`, fetchOpt)
              .then(r => r.ok ? r.json() : []).catch(() => []),
            fetch(`https://api.datamuse.com/words?sp=${encodeURIComponent(q)}&qe=sp&md=dprs&max=1`, fetchOpt)
              .then(r => r.ok ? r.json() : []).catch(() => []),
            fetch(`https://api.datamuse.com/words?ml=${encodeURIComponent(q)}&max=10`, fetchOpt)
              .then(r => r.ok ? r.json() : []).catch(() => []),
            fetch(`https://en.wiktionary.org/api/rest_v1/page/definition/${encodeURIComponent(q)}`, fetchOpt)
              .then(r => r.ok ? r.json() : null).catch(() => null),
            fetch(`https://suggestqueries.google.com/complete/search?client=chrome&q=${encodeURIComponent(q)}`, fetchOpt)
              .then(r => r.ok ? r.json() : null).catch(() => null),
            fetch(`https://openlibrary.org/search.json?q=${encodeURIComponent(q)}&limit=6&fields=title,author_name,first_publish_year,key,cover_i`, fetchOpt)
              .then(r => r.ok ? r.json() : null).catch(() => null),
            fetch(`https://www.youtube.com/results?search_query=how+to+pronounce+${encodeURIComponent(q)}`, {
              signal: controller.signal,
              headers: { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36' }
            }).then(r => r.text()).then(t => {
              const vids = [];
              const regex = /"videoId":"([a-zA-Z0-9_-]{11})"[\s\S]*?"title":\{"runs":\[\{"text":"(.*?)"/g;
              let m;
              while ((m = regex.exec(t)) !== null && vids.length < 5) {
                const title = m[2];
                if (title && !title.toLowerCase().includes('filter') && !vids.some(v => v.id === m[1])) {
                  vids.push({
                    id: m[1],
                    title,
                    channel: 'Pronunciation Guide',
                    thumb: `https://i.ytimg.com/vi/${m[1]}/hqdefault.jpg`,
                    url: `https://www.youtube.com/watch?v=${m[1]}`
                  });
                }
              }
              return vids;
            }).catch(() => []),
            fetch(`https://en.wikipedia.org/w/api.php?action=query&generator=search&gsrsearch=${encodeURIComponent(q)}&prop=pageimages|description&pithumbsize=400&format=json&origin=*`, fetchOpt)
              .then(r => r.ok ? r.json() : null).then(d => {
                if (!d || !d.query?.pages) return [];
                return Object.values(d.query.pages)
                  .filter(p => p.thumbnail?.source)
                  .map(p => ({
                    title: p.title,
                    url: p.thumbnail.source,
                    source: 'wikipedia.org',
                    description: p.description || p.title
                  }));
              }).catch(() => [])
          ]);
          clearTimeout(timeoutId);

          const payload = {
            query: q,
            wiki: wikiRes,
            synonyms: dataSynRes,
            datamuseDefs: dataDefRes?.[0]?.defs || [],
            datamusePron: dataDefRes?.[0]?.tags?.find(t => t.startsWith('pron:'))?.replace('pron:', '').trim() || '',
            datamuseSyllables: dataDefRes?.[0]?.numSyllables || 0,
            relatedTerms: dataRelatedRes || [],
            wiktionary: wiktRes,
            googleSuggestions: suggestRes?.[1] || [],
            openLibraryBooks: (booksRes?.docs || []).slice(0, 5).map(b => ({
              title: b.title,
              author: b.author_name ? b.author_name[0] : 'Classical Author',
              year: b.first_publish_year || b.publish_year?.[0] || 'Historical',
              key: b.key,
              coverId: b.cover_i,
              url: b.key ? `https://openlibrary.org${b.key}` : `https://www.google.com/search?tbm=bks&q=${encodeURIComponent(q)}`
            })),
            youtubeVideos: ytRes || [],
            wikiImages: wikiImgsRes || []
          };

          if (exploreServerCache.size > 200) {
            const firstKey = exploreServerCache.keys().next().value;
            exploreServerCache.delete(firstKey);
          }
          exploreServerCache.set(q, payload);

          sendJson(req, res, 200, payload);
        } catch (exploreErr) {
          sendJson(req, res, 500, { error: exploreErr.message });
        }
        return;
      }

      // 3. API: Update Frontmatter (e.g. Apple 3-state status toggle or Meta Bind)
      if (pathname === '/api/frontmatter' && req.method === 'POST') {
        const body = await readRequestBody(req);
        const { path: rawPath, updates } = body;
        if (!rawPath) throw new Error('Path is required');
        const relQuery = safeUriDecode(rawPath);
        const { normalized, absPath } = resolveSafeVaultPath(relQuery);
        if (!fs.existsSync(absPath)) {
          sendJson(req, res, 404, { error: `Note not found: ${normalized}` });
          return;
        }
        const currentContent = await fsp.readFile(absPath, 'utf8');
        const updatedContent = updateMarkdownFrontmatter(currentContent, updates || {});
        await fsp.writeFile(absPath, updatedContent, 'utf8');

        let pageEntry = pageMapByPath.get(normalized);
        if (pageEntry && updates) {
          if (updates.status !== undefined) {
            pageEntry.s = String(updates.status);
            statusDb[normalized] = String(updates.status);
            saveStatusDb().catch(e => console.warn('Failed to save status DB:', e.message));
          }
          if (updates.tags !== undefined) pageEntry.tg = Array.isArray(updates.tags) ? updates.tags : [String(updates.tags)];
        }
        if (vaultIndex.coreNotes[normalized]) {
          vaultIndex.coreNotes[normalized] = sanitizeNoteContent(normalized, updatedContent);
        }

        gitSync.queueChange(normalized, 'edit');
        sendJson(req, res, 200, { ok: true, path: normalized, updates });
        return;
      }

      // 4. API: Save / Create / Edit Note Content
      if (pathname === '/api/note' && req.method === 'POST') {
        const body = await readRequestBody(req);
        const { path: rawPath, content, append } = body;
        if (!rawPath) throw new Error('Path is required');
        const relQuery = safeUriDecode(rawPath);
        const { normalized, absPath } = resolveSafeVaultPath(relQuery);
        await fsp.mkdir(path.dirname(absPath), { recursive: true });

        let finalContent = String(content ?? '');
        if (append && fs.existsSync(absPath)) {
          const existing = await fsp.readFile(absPath, 'utf8');
          finalContent = existing + '\n\n' + finalContent;
        }
        await fsp.writeFile(absPath, finalContent, 'utf8');

        const fm = parseFrontmatter(finalContent.slice(0, 1000));
        let pageEntry = pageMapByPath.get(normalized);
        if (!pageEntry) {
          pageEntry = { p: normalized };
          vaultIndex.pages.push(pageEntry);
          pageMapByPath.set(normalized, pageEntry);
          vaultIndex.totalNotes = vaultIndex.pages.length;
        }
        if (fm.status) {
          pageEntry.s = String(fm.status);
          statusDb[normalized] = String(fm.status);
          saveStatusDb().catch(e => console.warn('Failed to save status DB:', e.message));
        }
        if (fm.tags) pageEntry.tg = Array.isArray(fm.tags) ? fm.tags : [String(fm.tags)];
        vaultIndex.coreNotes[normalized] = sanitizeNoteContent(normalized, finalContent);

        gitSync.queueChange(normalized, 'edit');
        sendJson(req, res, 200, { ok: true, path: normalized });
        return;
      }

      // 5. API: Delete Note OR Folder (recursive)
      if (pathname === '/api/note' && req.method === 'DELETE') {
        const rawQuery = urlObj.searchParams.get('path');
        if (!rawQuery) {
          const err = new Error('Path parameter is required');
          err.statusCode = 400;
          throw err;
        }
        const relQuery = safeUriDecode(rawQuery);
        const isFolder = urlObj.searchParams.get('type') === 'folder';
        const { normalized, absPath } = resolveSafeVaultPath(relQuery);
        if (fs.existsSync(absPath)) {
          if (isFolder) {
            if (!normalized || normalized === '.' || PROTECTED_ROOT_FOLDERS_LOWER.has(normalized.toLowerCase())) {
              const err = new Error(`"${normalized || 'Root'}" is protected vault structure and cannot be deleted`);
              err.statusCode = 403;
              throw err;
            }
            await fsp.rm(absPath, { recursive: true, force: true });
          } else {
            await fsp.unlink(absPath);
          }
        }
        if (isFolder) {
          removePathFromIndex(normalized);
          scheduleIndexRebuild();
        } else {
          removePathFromIndex(normalized);
        }
        gitSync.queueChange(normalized, isFolder ? 'folder-delete' : 'delete');
        sendJson(req, res, 200, { ok: true, path: normalized });
        return;
      }

      // 5b. API: Create Note or Folder
      if (pathname === '/api/create' && req.method === 'POST') {
        const body = await readRequestBody(req);
        const { path: rawPath, content = '', isFolder = false } = body;
        if (!rawPath) throw new Error('Path is required');
        const relPath = safeUriDecode(rawPath);
        const { normalized, absPath } = resolveSafeVaultPath(relPath);
        if (!normalized || normalized.endsWith('/')) throw new Error('Invalid path');
        if (fs.existsSync(absPath)) {
          sendJson(req, res, 409, { error: `Already exists: ${normalized}` });
          return;
        }
        if (isFolder) {
          await fsp.mkdir(absPath, { recursive: true });
        } else {
          await fsp.mkdir(path.dirname(absPath), { recursive: true });
          await fsp.writeFile(absPath, String(content ?? ''), 'utf8');
          addPathToIndex(normalized, String(content ?? ''));
          scheduleIndexRebuild();
        }
        gitSync.queueChange(normalized, isFolder ? 'folder-create' : 'create');
        sendJson(req, res, 200, { ok: true, path: normalized, isFolder });
        return;
      }

      // 5c. API: Rename / Move Note or Folder (drag & drop uses this too)
      if (pathname === '/api/rename' && req.method === 'POST') {
        const body = await readRequestBody(req);
        if (!body || !body.from || !body.to) throw new Error('Both "from" and "to" paths are required');
        const fromQuery = safeUriDecode(body.from);
        const toQuery = safeUriDecode(body.to);
        const from = resolveSafeVaultPath(fromQuery);
        const to = resolveSafeVaultPath(toQuery);
        if (!from.normalized || !to.normalized) throw new Error('Invalid paths');
        if (PROTECTED_ROOT_FOLDERS_LOWER.has(from.normalized.toLowerCase())) {
          const err = new Error(`Cannot rename protected root folder "${from.normalized}"`);
          err.statusCode = 403;
          throw err;
        }
        if (!fs.existsSync(from.absPath)) {
          sendJson(req, res, 404, { error: `Not found: ${from.normalized}` });
          return;
        }
        if (fs.existsSync(to.absPath)) {
          sendJson(req, res, 409, { error: `Target already exists: ${to.normalized}` });
          return;
        }
        // Block moving a folder into its own subtree
        if (to.normalized.toLowerCase().startsWith(from.normalized.toLowerCase() + '/')) {
          const err = new Error('Cannot move a folder into itself');
          err.statusCode = 400;
          throw err;
        }
        await fsp.mkdir(path.dirname(to.absPath), { recursive: true });
        await fsp.rename(from.absPath, to.absPath);
        renamePathInIndex(from.normalized, to.normalized);
        scheduleIndexRebuild();
        gitSync.queueChange(to.normalized, 'rename');
        sendJson(req, res, 200, { ok: true, from: from.normalized, to: to.normalized });
        return;
      }

      // 6. API: Serve Vault Images / Banners
      if (pathname === '/api/asset' && req.method === 'GET') {
        const rawQuery = urlObj.searchParams.get('path') || '';
        const relQuery = safeUriDecode(rawQuery);
        if (!relQuery) {
          sendJson(req, res, 400, { error: 'Path parameter required' });
          return;
        }
        const { absPath } = resolveSafeVaultPath(relQuery);
        if (fs.existsSync(absPath) && fs.statSync(absPath).isFile()) {
          const ext = path.extname(absPath).toLowerCase();
          const contentType = MIME_TYPES[ext] || 'application/octet-stream';
          const corsHeaders = getCorsHeaders(req);
          res.writeHead(200, {
            'Content-Type': contentType,
            'Cache-Control': 'public, max-age=3600',
            ...corsHeaders
          });
          const stream = fs.createReadStream(absPath);
          stream.on('error', (err) => {
            console.warn('Asset read stream error:', err.message);
            if (!res.headersSent) {
              sendJson(req, res, 500, { error: 'Failed to read asset' });
            } else if (!res.writableEnded) {
              res.end();
            }
          });
          res.on('close', () => {
            stream.destroy();
          });
          stream.pipe(res);
          return;
        }
        sendJson(req, res, 404, { error: 'Asset not found' });
        return;
      }

      // 7. API: Full-Text & Metadata Search
      if (pathname === '/api/search' && req.method === 'GET') {
        const q = (urlObj.searchParams.get('q') || '').trim().toLowerCase();
        const discipline = urlObj.searchParams.get('discipline') || '';
        const statusFilter = urlObj.searchParams.get('status') || '';
        const limit = Math.min(Number(urlObj.searchParams.get('limit') || 60), 200);

        const results = [];
        for (const p of vaultIndex.pages) {
          if (discipline && !p.p.startsWith(discipline + '/')) continue;
          const st = p.s || 'unread';
          if (statusFilter && st !== statusFilter) continue;

          const fileName = p.p.slice(p.p.lastIndexOf('/') + 1, -3);
          const lowerPath = p.p.toLowerCase();
          let score = 0;

          if (!q) {
            score = 1;
          } else if (fileName.toLowerCase() === q) {
            score = 100;
          } else if (fileName.toLowerCase().startsWith(q)) {
            score = 80;
          } else if (lowerPath.includes(q)) {
            score = 50;
          } else if (p.al && p.al.some(a => a.toLowerCase().includes(q))) {
            score = 60;
          } else if (p.tg && p.tg.some(t => t.toLowerCase().includes(q))) {
            score = 40;
          } else if (vaultIndex.coreNotes[p.p] && vaultIndex.coreNotes[p.p].toLowerCase().includes(q)) {
            score = 25;
          }

          if (score > 0) {
            let snippet = '';
            const body = vaultIndex.coreNotes[p.p];
            if (body && q) {
              const idx = body.toLowerCase().indexOf(q);
              if (idx !== -1) {
                snippet = body.slice(Math.max(0, idx - 45), idx + 95).replace(/\r?\n/g, ' ');
              }
            }
            results.push({ path: p.p, status: st, score, snippet, tags: p.tg || [] });
            if (!q && results.length >= limit) break;
          }
        }

        results.sort((a, b) => b.score - a.score || a.path.localeCompare(b.path));
        sendJson(req, res, 200, { results: results.slice(0, limit) });
        return;
      }

      // 8. API: Force Re-index Vault
      if (pathname === '/api/reindex' && (req.method === 'GET' || req.method === 'POST')) {
        await syncVaultDesignAssets();
        await buildVaultIndex(true);
        sendJson(req, res, 200, { ok: true, totalNotes: vaultIndex.totalNotes, generatedAt: vaultIndex.generatedAt });
        return;
      }

      // 8b. Dynamic Sitemap XML for CRW Map & Crawler Discovery
      if (pathname === '/sitemap.xml' && req.method === 'GET') {
        const baseUrl = `http://${req.headers.host || `localhost:${PORT}`}`;
        const urls = [
          `${baseUrl}/`,
          `${baseUrl}/?view=graph`,
          `${baseUrl}/?view=studio`,
          `${baseUrl}/?view=scratchpad`,
          ...Object.keys(vaultIndex.coreNotes).slice(0, 300).map(p => `${baseUrl}/?note=${encodeURIComponent(p)}`)
        ];
        const xml = `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n` +
          urls.map(u => `  <url><loc>${u.replace(/&/g, '&amp;')}</loc></url>`).join('\n') +
          `\n</urlset>`;
        const corsHeaders = getCorsHeaders(req);
        res.writeHead(200, { 'Content-Type': 'application/xml; charset=utf-8', ...corsHeaders });
        res.end(xml);
        return;
      }

      // 9. Static Files from public/
      let filePath = path.join(PUBLIC_DIR, pathname === '/' ? 'index.html' : pathname);
      const resolvedPublic = path.resolve(PUBLIC_DIR);
      const resolvedPublicWithSep = resolvedPublic.endsWith(path.sep) ? resolvedPublic : resolvedPublic + path.sep;
      const absFilePath = path.resolve(filePath);

      const isSubOfPublic = process.platform === 'win32'
        ? (absFilePath.toLowerCase() === resolvedPublic.toLowerCase() || absFilePath.toLowerCase().startsWith(resolvedPublicWithSep.toLowerCase()))
        : (absFilePath === resolvedPublic || absFilePath.startsWith(resolvedPublicWithSep));

      if (!isSubOfPublic) {
        const cors = getCorsHeaders(req);
        res.writeHead(403, { 'Content-Type': 'text/plain; charset=utf-8', ...cors });
        res.end('Forbidden');
        return;
      }

      let targetPath = absFilePath;
      if (fs.existsSync(targetPath) && fs.statSync(targetPath).isDirectory()) {
        targetPath = path.join(targetPath, 'index.html');
      }
      if (!fs.existsSync(targetPath)) {
        targetPath = path.join(PUBLIC_DIR, 'index.html');
      }

      if (!fs.existsSync(targetPath)) {
        sendJson(req, res, 404, { error: 'Not found' });
        return;
      }

      const ext = path.extname(targetPath).toLowerCase();
      const contentType = MIME_TYPES[ext] || 'application/octet-stream';
      const corsHeaders = getCorsHeaders(req);
      const revalidate = ext === '.html' || ext === '.js' || ext === '.mjs' || ext === '.css';
      const cacheControl = revalidate ? 'no-cache' : 'public, max-age=3600';

      let rawBuf;
      try {
        rawBuf = await fsp.readFile(targetPath);
      } catch (readErr) {
        console.warn(`Failed to read static file ${targetPath}:`, readErr.message);
        sendJson(req, res, 500, { error: 'Failed to read file' });
        return;
      }

      const acceptEncoding = req.headers?.['accept-encoding'] || '';
      const canGzip = acceptEncoding.includes('gzip') && rawBuf.length > 2048 &&
        (ext === '.json' || ext === '.js' || ext === '.mjs' || ext === '.css' || ext === '.html' || ext === '.svg');

      const responseHeaders = {
        'Content-Type': contentType,
        'Cache-Control': cacheControl,
        ...corsHeaders
      };

      if (canGzip) {
        zlib.gzip(rawBuf, (err, compressed) => {
          if (res.writableEnded || res.destroyed) return;
          if (err) {
            console.warn('Gzip static error, falling back to raw:', err.message);
            res.writeHead(200, responseHeaders);
            res.end(rawBuf);
            return;
          }
          res.writeHead(200, {
            ...responseHeaders,
            'Content-Encoding': 'gzip'
          });
          res.end(compressed);
        });
      } else {
        res.writeHead(200, responseHeaders);
        res.end(rawBuf);
      }
    } catch (err) {
      console.error(`[HTTP ${req.method} ${req.url}] Server error:`, err.message);
      if (res.headersSent || res.writableEnded) {
        try { res.end(); } catch { /* ignore */ }
        return;
      }
      let status = 500;
      if (err.statusCode) {
        status = err.statusCode;
      } else if (/forbidden/i.test(err.message)) {
        status = 403;
      } else if (/invalid path|bad request|null byte|required/i.test(err.message)) {
        status = 400;
      } else if (/not found/i.test(err.message)) {
        status = 404;
      } else if (/already exists/i.test(err.message)) {
        status = 409;
      }
      sendJson(req, res, status, { error: err.message || 'Internal Server Error' });
    }
  });

  server.listen(PORT, '0.0.0.0', () => {
    console.log(`\n🏛️  Obsidian Language & Philology Web App running at:`);
    console.log(`   ➜ Desktop: http://localhost:${PORT}`);
    console.log(`   ➜ Vault:   ${VAULT_ROOT} (${vaultIndex.totalNotes.toLocaleString()} notes indexed, Content Studio excluded)\n`);
  });
}

startServer();
