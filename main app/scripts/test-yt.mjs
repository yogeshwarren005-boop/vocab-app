async function test() {
  const r = await fetch('https://www.youtube.com/results?search_query=how+to+pronounce+independently', {
    headers: { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36' }
  });
  const t = await r.text();
  const vids = [];
  const regex = /"videoId":"([a-zA-Z0-9_-]{11})"[\s\S]*?"title":\{"runs":\[\{"text":"(.*?)"/g;
  let m;
  while ((m = regex.exec(t)) !== null && vids.length < 5) {
    if (!vids.some(v => v.id === m[1])) {
      vids.push({ id: m[1], title: m[2] });
    }
  }
  console.log('Videos found:', vids);
}
test();
