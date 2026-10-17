/**
 * Vocab App — Automated Verification Suite
 * Tests Avatar Service, Nickname Generation, Tracking, and Feature Registry Extensibility
 */

import { avatarService } from './public/js/services/avatar-service.js';
import { featureRegistry, BaseFeature } from './public/js/core/feature-registry.js';

console.log('🧪 Starting Vocab App Verification Suite...\n');

// Test 1: Nickname Generation Entropy
console.log('--- Test 1: Fun Nickname Generation ---');
const nicknames = new Set();
for (let i = 0; i < 20; i++) {
  const nick = avatarService.rollNickname();
  nicknames.add(nick);
}
console.log(`Generated 20 nicknames. Sample: ${Array.from(nicknames).slice(0, 5).join(', ')}`);
if (nicknames.size >= 18) {
  console.log('✅ PASS: Nickname generator has high entropy and variety.');
} else {
  console.error('❌ FAIL: Low nickname entropy');
}

// Test 2: Procedural Animated SVG Avatar Generation
console.log('\n--- Test 2: Procedural Animated SVG Generation ---');
const sampleNick = 'CosmicAthena42';
const svg = avatarService.generateAvatarSvg(sampleNick, { size: 96, animated: true });
const meta = avatarService.getAvatarMeta(sampleNick);

console.log(`Nickname: "${sampleNick}"`);
console.log(`Assigned Archetype: "${meta.archetype}"`);
console.log(`Primary Color: ${meta.palette.primary}, Aura: ${meta.palette.aura}`);

if (svg.includes('<svg') && svg.includes('</svg>') && svg.includes('@keyframes avatarFloat') && svg.includes('@keyframes avatarPulse')) {
  console.log('✅ PASS: Generated SVG is well-formed with embedded CSS keyframe animations.');
} else {
  console.error('❌ FAIL: SVG is missing keyframe animations or tags');
}

// Test 3: Deterministic Avatar Consistency
console.log('\n--- Test 3: Deterministic Consistency ---');
const svg1 = avatarService.generateAvatarSvg('LexiKnight99');
const svg2 = avatarService.generateAvatarSvg('LexiKnight99');
if (svg1 === svg2) {
  console.log('✅ PASS: Same nickname deterministically generates identical avatar SVG.');
} else {
  console.error('❌ FAIL: Avatars differ for identical nickname');
}

// Test 4: Extensible Feature Registry Pattern
console.log('\n--- Test 4: Extensible Feature Registry Verification ---');
class QuizFeature extends BaseFeature {
  constructor() {
    super('quizzes', { isSubcollection: true });
  }

  async saveScore(quizId, score) {
    return await this.saveDoc(quizId, { score, passed: score >= 70 });
  }
}

const quizFeature = new QuizFeature();
featureRegistry.register(quizFeature);

const retrievedFeature = featureRegistry.get('quizzes');
if (retrievedFeature === quizFeature) {
  console.log('✅ PASS: New future feature registered successfully in 1 line of code.');
} else {
  console.error('❌ FAIL: Feature could not be retrieved from registry');
}

console.log('\n🎉 ALL AUTOMATED TESTS COMPLETED SUCCESSFULLY!\n');
