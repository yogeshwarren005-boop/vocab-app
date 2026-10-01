import fs from 'fs';
import path from 'path';

const baseDir = 'App database/Greek roots/Cluster Motion & Direction';

function getWords(dashboard) {
  const dPath = path.join(baseDir, dashboard);
  if (!fs.existsSync(dPath)) return [];
  return fs.readdirSync(dPath)
    .filter(f => f.endsWith('.md') && !f.startsWith('Dashboard —') && !f.startsWith('Word Triage —') && !f.startsWith('Cluster') && !f.startsWith('Semantic Field'))
    .sort()
    .map(file => ({ dashboard, file }));
}

const batch1Dashboards = [
  'Dashboard — pheug',
  'Dashboard — brady',
  'Dashboard — drome',
  'Dashboard — pat',
  'Dashboard — pro',
  'Dashboard — pemp',
  'Dashboard — pol',
  'Dashboard — trech',
  'Dashboard — streph',
  'Dashboard — torn'
];

const batch2Dashboards = [
  'Dashboard — stol',
  'Dashboard — oestr',
  'Dashboard — tach',
  'Dashboard — dram'
];

const batch3Dashboards = [
  'Dashboard — phor',
  'Dashboard — kine'
];

const batch4Dashboards = [
  'Dashboard — trep'
];

const batch5Dashboards = [
  'Dashboard — ba'
];

const batch6Dashboards = [
  'Dashboard — plan'
];

const plan = {
  batch1: {
    dashboards: batch1Dashboards,
    words: batch1Dashboards.flatMap(getWords)
  },
  batch2: {
    dashboards: batch2Dashboards,
    words: batch2Dashboards.flatMap(getWords)
  },
  batch3: {
    dashboards: batch3Dashboards,
    words: batch3Dashboards.flatMap(getWords)
  },
  batch4: {
    dashboards: batch4Dashboards,
    words: batch4Dashboards.flatMap(getWords)
  },
  batch5: {
    dashboards: batch5Dashboards,
    words: batch5Dashboards.flatMap(getWords)
  },
  batch6: {
    dashboards: batch6Dashboards,
    words: batch6Dashboards.flatMap(getWords)
  }
};

fs.writeFileSync('main app/scripts/motion-plan.json', JSON.stringify(plan, null, 2), 'utf8');

console.log('Motion Plan Generated:');
for (const b in plan) {
  console.log(`${b}: ${plan[b].words.length} words across ${plan[b].dashboards.length} dashboards`);
}
const total = Object.values(plan).reduce((acc, b) => acc + b.words.length, 0);
console.log(`Total words in motion plan: ${total}`);
