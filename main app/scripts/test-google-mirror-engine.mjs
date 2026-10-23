import fs from 'fs';

async function testWord(w) {
  const res = await fetch(`http://localhost:3080/api/explore?q=${encodeURIComponent(w)}&nocache=1`);
  if (!res.ok) {
    console.error(`Failed to fetch ${w}: ${res.status}`);
    return;
  }
  const data = await res.json();
  console.log(`\n=================== [ ${w.toUpperCase()} ] ===================`);
  console.log('Query:', data.query);
  console.log('Syllables count:', data.datamuseSyllables);
  console.log('Pronunciation:', data.datamusePron);
  console.log('Suggestions:', data.googleSuggestions?.slice(0, 4));
  console.log('Videos count:', data.youtubeVideos?.length, data.youtubeVideos?.[0]?.title);
  console.log('Images count:', data.wikiImages?.length, data.wikiImages?.[0]?.title);
  console.log('Books count:', data.openLibraryBooks?.length, data.openLibraryBooks?.[0]?.title);
}

async function run() {
  await testWord('independently');
  await testWord('portability');
  await testWord('blight');
}

run();
