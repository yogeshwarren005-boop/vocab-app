import fs from 'fs';

async function run() {
  const headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1'
  };

  const r = await fetch('https://www.google.com/search?q=independently&hl=en&gl=us', { headers });
  console.log('Status:', r.status);
  const text = await r.text();
  console.log('Length:', text.length);
  console.log('Has enablejs:', text.includes('enablejs'));
  console.log('Title:', text.match(/<title>(.*?)<\/title>/)?.[1]);
  fs.writeFileSync('main app/test-google-result.html', text);
}
run();
