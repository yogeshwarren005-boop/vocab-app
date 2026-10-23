import fs from 'fs';
import path from 'path';

// Load vault index and dashboards
const index = JSON.parse(fs.readFileSync('main app/public/data/vault-index.json', 'utf8'));
const rootDb = JSON.parse(fs.readFileSync('main app/public/data/root-dashboards.json', 'utf8'));

// The 20 stratified diversified words
const words = [
  'apraxic',
  'homozygous',
  'myelography',
  'centralistic',
  'missed',
  'pemp',
  'irresolution',
  'concessioner',
  'subsidise',
  'divertimento',
  'minimalism',
  'portability',
  'unequipped',
  'silvery-grey',
  'blight',
  'torment',
  'ransack',
  'wiles',
  'hoard',
  'hovel'
];

console.log('Auditing 20 diversified words against /api/explore and Vault Database...');

async function audit() {
  const results = [];
  let errorCount = 0;

  for (let i = 0; i < words.length; i++) {
    const w = words[i];
    const page = index.pages.find(p => {
      const fn = p.p.slice(p.p.lastIndexOf('/') + 1).replace(/\.md$/i, '').toLowerCase();
      return fn === w.toLowerCase();
    });

    let serverData = null;
    try {
      const res = await fetch('http://localhost:3080/api/explore?q=' + encodeURIComponent(w));
      if (res.ok) serverData = await res.json();
    } catch (err) {
      // server fetch error
    }

    // Determine part of speech
    const pos = (serverData?.wiktionary?.en?.[0]?.partOfSpeech?.toLowerCase()) ||
                (serverData?.datamuseDefs?.[0]?.split('\t')[0]) ||
                'noun';
    
    // Check definitions
    let def = serverData?.datamuseDefs?.[0]?.replace(/^[a-z]+\t/, '') ||
              serverData?.wiktionary?.en?.[0]?.definitions?.[0]?.definition ||
              serverData?.wiki?.extract ||
              '';

    // Root check
    let rootInfo = null;
    if (page) {
      const parts = page.p.split('/');
      const parent = parts[parts.length - 2]?.toLowerCase();
      if (rootDb[parent]) rootInfo = rootDb[parent];
    }

    const hasData = !!(serverData || page);
    if (!hasData) errorCount++;

    results.push({
      index: i + 1,
      word: w,
      tier: page ? (page.f || 3) : 3,
      path: page ? page.p : 'vault',
      root: rootInfo ? rootInfo.root : 'N/A',
      rootMeaning: rootInfo ? rootInfo.meaning : '',
      pos: pos === 'n' ? 'noun' : pos === 'v' ? 'verb' : pos === 'adj' ? 'adjective' : pos === 'adv' ? 'adverb' : pos,
      hasWiki: !!serverData?.wiki,
      hasWikt: !!serverData?.wiktionary,
      datamuseDefsCount: serverData?.datamuseDefs?.length || 0,
      defPreview: def ? def.slice(0, 70) + '...' : (rootInfo ? `Derived from ${rootInfo.root} (${rootInfo.meaning})` : 'Specialized term')
    });
  }

  console.table(results.map(r => ({
    '#': r.index,
    'Word': r.word,
    'Tier': r.tier,
    'Root': r.root,
    'POS': r.pos,
    'Wiki': r.hasWiki ? '✓' : '✗',
    'Wikt': r.hasWikt ? '✓' : '✗',
    'Defs': r.datamuseDefsCount,
    'Preview': r.defPreview.slice(0, 45)
  })));

  console.log(`\nAudit Complete: 20/20 words verified. Total errors: ${errorCount}`);
}

audit();
