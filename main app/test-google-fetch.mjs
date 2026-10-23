async function testFollow() {
  const url1 = 'https://www.google.com/search?q=bonny&hl=en&gl=us';
  const res1 = await fetch(url1, {
    headers: {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    }
  });
  const cookie = res1.headers.get('set-cookie');
  console.log('Cookies from res1:', cookie);
  const text1 = await res1.text();
  const match = text1.match(/\/httpservice\/retry\/enablejs\?sei=[^"'\s>]+/);
  console.log('Redirect url match:', match?.[0]);
  if (match) {
    const url2 = 'https://www.google.com' + match[0];
    const res2 = await fetch(url2, {
      headers: {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Cookie': cookie || ''
      }
    });
    console.log('Res2 status:', res2.status);
    const text2 = await res2.text();
    console.log('Res2 length:', text2.length);
    console.log('Res2 includes search results:', text2.includes('bonny') && (text2.includes('attractive') || text2.includes('results') || text2.includes('Dictionary')));
    console.log('Res2 preview:', text2.slice(0, 400));
  }
}
testFollow();
