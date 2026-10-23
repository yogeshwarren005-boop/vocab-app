async function test() {
  const word = 'independently';
  console.log('Testing live APIs for word:', word);

  // 1. Free Dictionary API (Real Oxford/Wiktionary definitions, phonetics, audio, examples)
  try {
    const res = await fetch('https://api.dictionaryapi.dev/api/v2/entries/en/' + word);
    const json = await res.json();
    console.log('DictionaryAPI:', Array.isArray(json) ? 'SUCCESS: ' + json[0]?.meanings?.length + ' meanings, phonetic: ' + json[0]?.phonetic : 'FAILED');
    if (Array.isArray(json) && json[0]?.meanings?.[0]) {
      console.log('  Part of speech:', json[0].meanings[0].partOfSpeech);
      console.log('  First definition:', json[0].meanings[0].definitions?.[0]?.definition);
      console.log('  Example:', json[0].meanings[0].definitions?.[0]?.example);
    }
  } catch(e) { console.log('DictionaryAPI ERR:', e.message); }

  // 2. Google Suggest / Autocomplete (Real Google search predictions)
  try {
    const res = await fetch('https://suggestqueries.google.com/complete/search?client=chrome&q=' + encodeURIComponent(word));
    const json = await res.json();
    console.log('Google Real Autocomplete Queries:', json[1]?.slice(0, 5));
  } catch(e) { console.log('Google Suggest ERR:', e.message); }

  // 3. Google Books API (Real Google Books search results with real titles, authors, descriptions, links)
  try {
    const res = await fetch('https://www.googleapis.com/books/v1/volumes?q=' + encodeURIComponent(word) + '&maxResults=4');
    const json = await res.json();
    console.log('Google Books Live API:', json.items?.length ? `Found ${json.items.length} books` : 'NONE');
    if (json.items?.[0]) {
      const b = json.items[0].volumeInfo;
      console.log(`  Top Book: "${b.title}" by ${b.authors?.join(', ')} (${b.publishedDate})`);
      console.log(`  Snippet/Description: ${b.description?.slice(0, 100)}...`);
      console.log(`  Preview Link: ${b.previewLink?.slice(0, 80)}...`);
    }
  } catch(e) { console.log('Google Books ERR:', e.message); }

  // 4. DuckDuckGo HTML Search Scraper (Real live organic search results with real titles, real links, real snippets!)
  try {
    const res = await fetch('https://html.duckduckgo.com/html/?q=' + encodeURIComponent(word + ' definition'), {
      headers: {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
      }
    });
    const html = await res.text();
    const results = [];
    const linkRegex = /<a class="result__snippet[^"]*"[^>]*href="([^"]*)"[^>]*>([\s\S]*?)<\/a>/g;
    const titleRegex = /<a class="result__url[^"]*"[^>]*href="([^"]*)"[^>]*>([\s\S]*?)<\/a>/g;
    console.log('DuckDuckGo HTML Search:', html.length > 5000 ? `SUCCESS (${html.length} bytes returned)` : 'SHORT');
  } catch(e) { console.log('DuckDuckGo HTML ERR:', e.message); }
}

test();
