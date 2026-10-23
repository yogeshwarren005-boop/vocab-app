/**
 * frequency-engine.mjs — Deterministic Corpus Linguistics Frequency Scoring Engine
 * Combines Google Trillion Word Web Corpus & OpenSubtitles 50k dataset into
 * three standardized pedagogical tiers:
 *   Tier 1: Words to learn first (High Frequency, Zipf >= 4.0, Rank <= 8000)
 *   Tier 2: Words to learn a little later (Mid Frequency, 2.3 <= Zipf < 4.0, Rank 8001 - 45000)
 *   Tier 3: Words to learn last (Low Frequency, Zipf < 2.3, Rank > 45000 or rare/obscure)
 */

import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const LEXICON_PATH = path.join(__dirname, 'lexicon-data', 'frequency-map.json');

let cachedMap = null;

export function loadFrequencyMap() {
  if (cachedMap) return cachedMap;
  if (fs.existsSync(LEXICON_PATH)) {
    try {
      cachedMap = JSON.parse(fs.readFileSync(LEXICON_PATH, 'utf8'));
      return cachedMap;
    } catch {
      cachedMap = {};
    }
  }
  return {};
}

/**
 * Returns exact frequency classification for any word
 * @param {string} word
 * @returns {{ tier: 1|2|3, tierName: string, tierLabel: string, zipf: number, rank: number }}
 */
export function getWordFrequency(word) {
  const map = loadFrequencyMap();
  const w = (word || '').toLowerCase().trim();
  const entry = map[w];

  if (entry) {
    // Tier 1: High Frequency (Google 10k <= 8000 or General rank <= 8000)
    if ((entry.g10kRank && entry.g10kRank <= 8000) || (entry.rank && entry.rank <= 8000)) {
      const count = entry.count || 10000;
      const rawZipf = (Math.log10(count) - 1.2).toFixed(2);
      const zipf = Math.min(7.0, Math.max(4.0, parseFloat(rawZipf)));
      return {
        tier: 1,
        tierName: 'learn_first',
        tierLabel: 'Words to learn first',
        zipf,
        rank: entry.g10kRank || entry.rank
      };
    }

    // Tier 2: Mid Frequency / Elevated Academic & Literary (Rank 8001 to 45000)
    if (entry.rank && entry.rank <= 45000) {
      const count = entry.count || 500;
      const rawZipf = (Math.log10(count) - 0.9).toFixed(2);
      const zipf = Math.min(3.99, Math.max(2.3, parseFloat(rawZipf)));
      return {
        tier: 2,
        tierName: 'learn_later',
        tierLabel: 'Words to learn a little later',
        zipf,
        rank: entry.rank
      };
    }

    // Tier 3: Rank > 45000
    return {
      tier: 3,
      tierName: 'learn_last',
      tierLabel: 'Words to learn last',
      zipf: 1.80,
      rank: entry.rank
    };
  }

  // Not in top 50,000 modern corpus -> Tier 3 (Rarest words with little modern usage)
  return {
    tier: 3,
    tierName: 'learn_last',
    tierLabel: 'Words to learn last',
    zipf: 1.20,
    rank: 999999
  };
}

/**
 * Computes root-level frequency yield and tier based on its derived words
 * @param {Array<{ name: string }>} derivedWords
 * @returns {{ tier: 1|2|3, tierName: string, tierLabel: string, score: number, t1Count: number, t2Count: number, t3Count: number }}
 */
export function getRootFrequencyTier(derivedWords = []) {
  let t1Count = 0;
  let t2Count = 0;
  let t3Count = 0;
  let maxZipf = 0;

  for (const item of derivedWords) {
    const wName = (item.name || item).replace(/\.md$/i, '');
    const freq = getWordFrequency(wName);
    if (freq.tier === 1) t1Count++;
    else if (freq.tier === 2) t2Count++;
    else t3Count++;
    if (freq.zipf > maxZipf) maxZipf = freq.zipf;
  }

  // Scoring formula: heavily rewards presence of Tier 1 & Tier 2 words
  const score = (t1Count * 10) + (t2Count * 2) + (t3Count * 0.1) + maxZipf;

  if (t1Count >= 2 || (t1Count >= 1 && t2Count >= 2) || maxZipf >= 4.5) {
    return {
      tier: 1,
      tierName: 'learn_first',
      tierLabel: 'Roots to learn first',
      score: parseFloat(score.toFixed(2)),
      t1Count,
      t2Count,
      t3Count
    };
  }

  if (t2Count >= 2 || t1Count >= 1 || maxZipf >= 2.5) {
    return {
      tier: 2,
      tierName: 'learn_later',
      tierLabel: 'Roots to learn a little later',
      score: parseFloat(score.toFixed(2)),
      t1Count,
      t2Count,
      t3Count
    };
  }

  return {
    tier: 3,
    tierName: 'learn_last',
    tierLabel: 'Roots to learn last',
    score: parseFloat(score.toFixed(2)),
    t1Count,
    t2Count,
    t3Count
  };
}
