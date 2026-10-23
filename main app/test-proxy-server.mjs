import http from 'node:http';

const PORT = 3089;

const server = http.createServer(async (req, res) => {
  const url = new URL(req.url, `http://localhost:${PORT}`);
  
  if (url.pathname === '/embed-test') {
    res.writeHead(200, { 'Content-Type': 'text/html' });
    res.end(`
      <!DOCTYPE html>
      <html>
      <head>
        <title>Google Embed Test</title>
        <style>
          body { margin: 0; background: #202124; color: #fff; font-family: sans-serif; display: flex; flex-direction: column; height: 100vh; }
          .header { padding: 10px 20px; background: #303134; display: flex; align-items: center; gap: 12px; }
          iframe { flex: 1; border: none; width: 100%; height: calc(100vh - 60px); }
        </style>
      </head>
      <body>
        <div class="header">
          <span>🔒 Locked Word: <b>bonny</b></span>
          <span>Google Mirror Iframe:</span>
        </div>
        <iframe src="/proxy?q=bonny"></iframe>
      </body>
      </html>
    `);
    return;
  }

  if (url.pathname === '/proxy') {
    const q = url.searchParams.get('q') || 'test';
    const targetUrl = `https://www.google.com/search?q=${encodeURIComponent(q)}&hl=en&gl=us`;

    try {
      const googleRes = await fetch(targetUrl, {
        headers: {
          'User-Agent': req.headers['user-agent'] || 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
          'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
          'Accept-Language': req.headers['accept-language'] || 'en-US,en;q=0.9',
        }
      });

      let html = await googleRes.text();

      // Inject base tag so all assets load from google.com
      html = html.replace(/<head[^>]*>/i, `$&
        <base href="https://www.google.com/">
        <script>
          // Catch clicks on links to prevent escaping the frame if desired
          window.addEventListener('DOMContentLoaded', () => {
            console.log('Google proxied page loaded');
          });
        </script>
      `);

      res.writeHead(200, {
        'Content-Type': 'text/html; charset=utf-8',
        'Access-Control-Allow-Origin': '*',
        // DO NOT set X-Frame-Options or CSP so this page CAN be embedded in an iframe
      });
      res.end(html);
    } catch (err) {
      res.writeHead(500, { 'Content-Type': 'text/plain' });
      res.end('Proxy error: ' + err.message);
    }
    return;
  }

  res.writeHead(404);
  res.end('Not found');
});

server.listen(PORT, () => {
  console.log(`Test proxy server running on http://localhost:${PORT}`);
});
