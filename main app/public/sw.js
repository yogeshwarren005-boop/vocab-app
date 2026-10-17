/**
 * Obsidian Vocab — Service Worker (PWA offline support)
 * Version: v4
 *
 * Strategies:
 *  - App navigations:            network-first, fall back to cached shell (offline)
 *  - Vault API reads (GET):      network-first, cache successful reads (offline reading)
 *  - Vault API /api/note:        network-first, fall back to cached core-notes or structured note
 *  - Vault API writes (POST...): always pass through to the network
 *  - Data assets (/data/*):      network-first with runtime cache fallback
 *  - Static assets:              stale-while-revalidate (instant + self-updating)
 */

const SHELL_CACHE = 'obsidian-vocab-shell-v4';
const RUNTIME_CACHE = 'obsidian-vocab-runtime-v4';

const SHELL_ASSETS = [
  '/',
  '/index.html',
  '/manifest.webmanifest',
  '/js/mobile-app.js',
  '/js/mobile-updater.js',
  '/js/dataview-engine.js',
  '/js/markdown-engine.js',
  '/js/graph-view.js',
  '/js/vault-apps.js',
  '/styles/mobile-app.css',
  '/styles/obsidian-core.css',
  '/styles/web-colors.css',
  '/styles/web-layout.css',
  '/styles/web-typography.css',
  '/styles/web-components.css',
  '/styles/web-interactive.css',
  '/styles/web-reading-view.css',
  '/styles/language-folders-highlight.css',
  '/styles/vault-theme.css',
  '/styles/apple-toggle.css',
  '/icons/icon-192.png',
  '/icons/icon-512.png',
  '/icons/apple-touch-icon.png',
  '/version.json',
  '/data/status-db.json'
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(SHELL_CACHE)
      .then(cache => cache.addAll(SHELL_ASSETS))
      .then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys()
      .then(keys => Promise.all(
        keys
          .filter(k => k !== SHELL_CACHE && k !== RUNTIME_CACHE)
          .map(k => {
            console.log('[SW v4] Deleting obsolete cache:', k);
            return caches.delete(k);
          })
      ))
      .then(() => self.clients.claim())
  );
});

async function networkFirst(request, cacheName) {
  const cache = await caches.open(cacheName);
  try {
    const fresh = await fetch(request);
    if (fresh && fresh.ok) cache.put(request, fresh.clone());
    return fresh;
  } catch {
    const cached = await cache.match(request);
    if (cached) return cached;
    throw new Error('offline and not cached');
  }
}

async function staleWhileRevalidate(request) {
  const cache = await caches.open(SHELL_CACHE);
  const cached = await cache.match(request);
  const network = fetch(request)
    .then(fresh => {
      if (fresh && fresh.ok) cache.put(request, fresh.clone());
      return fresh;
    })
    .catch(() => cached);
  return cached || network;
}

self.addEventListener('fetch', (event) => {
  const { request } = event;
  if (request.method !== 'GET') return; // writes go straight to the network

  const url = new URL(request.url);
  if (url.origin !== self.location.origin) return; // let CDN fonts/external assets use standard HTTP cache

  // 1. App shell navigation
  if (request.mode === 'navigate') {
    event.respondWith(
      networkFirst(request, SHELL_CACHE)
        .catch(() => caches.match('/index.html'))
        .then(res => res || caches.match('/'))
    );
    return;
  }

  // 2. Specific API route: /api/note (Individual note content)
  if (url.pathname === '/api/note') {
    event.respondWith(
      networkFirst(request, RUNTIME_CACHE).catch(async () => {
        const notePath = url.searchParams.get('path') || '00 Language Hub.md';

        // Check if pre-bundled core-notes.json is present in cache
        try {
          const coreRes = await caches.match('/data/core-notes.json') ||
                          await caches.match('data/core-notes.json');
          if (coreRes) {
            const coreData = await coreRes.clone().json();
            if (coreData && coreData[notePath]) {
              return new Response(JSON.stringify({
                path: notePath,
                content: coreData[notePath],
                offline: true,
                source: 'core-notes'
              }), {
                status: 200,
                headers: { 'Content-Type': 'application/json', 'X-Offline-Fallback': 'true' }
              });
            }
          }
        } catch (e) {
          console.warn('[SW v4] Core notes fallback lookup failed:', e);
        }

        // Return structured fallback response for offline viewing
        const noteTitle = notePath.split('/').pop().replace(/\.md$/i, '') || 'Vocabulary Note';
        const fallbackContent = [
          `# ${noteTitle}`,
          '',
          `> [!note] Offline Mode`,
          `> This note is not currently stored in your local offline cache. Reconnect to the network to view complete dynamic content, or explore pre-bundled study cards in Tab 2.`,
          '',
          `## Vocabulary Overview`,
          `- **Entry**: ${noteTitle}`,
          `- **Vault Path**: \`${notePath}\``,
          `- **Status**: Offline placeholder`
        ].join('\n');

        return new Response(JSON.stringify({
          path: notePath,
          content: fallbackContent,
          offline: true,
          fallback: true
        }), {
          status: 200,
          headers: { 'Content-Type': 'application/json', 'X-Offline-Fallback': 'true' }
        });
      })
    );
    return;
  }

  // 3. Other Vault API endpoints (/api/vault-index, /api/status, etc.)
  if (url.pathname.startsWith('/api/')) {
    event.respondWith(
      networkFirst(request, RUNTIME_CACHE).catch(() =>
        new Response(JSON.stringify({ error: 'offline', message: 'You are currently offline' }), {
          status: 503,
          headers: { 'Content-Type': 'application/json' }
        })
      )
    );
    return;
  }

  // 4. Large Data Bundles (/data/core-notes.json, /data/vault-index.json)
  if (url.pathname.startsWith('/data/') || url.pathname === '/version.json') {
    event.respondWith(networkFirst(request, RUNTIME_CACHE));
    return;
  }

  // 5. Static assets: serve instantly, refresh in the background
  if (/\.(css|js|mjs|png|jpg|jpeg|webp|svg|ico|woff2?|json)$/i.test(url.pathname) || url.pathname === '/manifest.webmanifest') {
    event.respondWith(staleWhileRevalidate(request));
  }
});
