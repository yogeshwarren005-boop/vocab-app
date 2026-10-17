import fs from 'fs';
import { execSync } from 'child_process';

const out = execSync('node "main app/scripts/audit-roots.mjs" "App database/Greek roots/Cluster Action"', { encoding: 'utf8' });
const lines = out.split('\n');
const problems = lines.filter(l => l.startsWith('❌ ')).map(l => l.replace('❌ ', '').replace(':', '').trim().replace(/\\/g, '/'));
console.log('Total problems found by audit-roots:', problems.length);
fs.writeFileSync('main app/scripts/current-audit-problems.json', JSON.stringify(problems, null, 2));

const remaining = JSON.parse(fs.readFileSync('main app/scripts/action-remaining-problems.json', 'utf8'));
const inAuditNotRemaining = problems.filter(p => !remaining.includes(p));
console.log('Problems in audit not in remaining (', inAuditNotRemaining.length, '):', inAuditNotRemaining);
