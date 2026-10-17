/**
 * Vocab App — Fun Nickname & Unique Animated SVG Avatar Service
 * 
 * Features:
 * 1. Procedural Animated SVG Avatar Generation:
 *    - Pure vector graphics (0ms latency, zero external asset downloads).
 *    - Embedded CSS keyframe animations (floating bob, glowing aura pulse, eye blinking, cosmic shimmer).
 *    - Deterministic seed generation: Every unique nickname gets a unique, reproducible avatar!
 * 2. Fun Nickname Generator:
 *    - Generates delightful classical, mythological, and philological usernames (e.g. CosmicAthena, PolyglotOwl).
 */

const ADJECTIVES = [
  'Cosmic', 'Verbal', 'Astute', 'Mythic', 'Radiant', 'Nimble', 'Lexical',
  'Spartan', 'Quantum', 'Mystic', 'Polyglot', 'Golden', 'Arcane', 'Stellar',
  'Brave', 'Keen', 'Wise', 'Solar', 'Velvet', 'Swift', 'Curious', 'Epic',
  'Sonic', 'Vivid', 'Echoing', 'Runic', 'Cerebral', 'Infinite', 'Lucid'
];

const NOUNS = [
  'Athena', 'Sphinx', 'Falcon', 'Oracle', 'Viking', 'Sage', 'Hermes',
  'Owl', 'Scholar', 'Titan', 'Phoenix', 'Griffin', 'Bard', 'Nomad',
  'Fox', 'Dragon', 'Seeker', 'Knight', 'Muse', 'Alchemist', 'Cipher',
  'Herald', 'Voyager', 'Scribe', 'Zephyr', 'Orion', 'Centaur', 'Monk'
];

const COLOR_PALETTES = [
  { primary: '#7C3AED', secondary: '#EC4899', aura: '#8B5CF6', bg: '#1E1B4B' }, // Neon Violet & Pink
  { primary: '#0284C7', secondary: '#06B6D4', aura: '#38BDF8', bg: '#082F49' }, // Oceanic Cyan & Azure
  { primary: '#059669', secondary: '#10B981', aura: '#34D399', bg: '#064E3B' }, // Emerald Jade
  { primary: '#D97706', secondary: '#F59E0B', aura: '#FBBF24', bg: '#451A03' }, // Magma Gold & Amber
  { primary: '#DC2626', secondary: '#F43F5E', aura: '#FB7185', bg: '#4C0519' }, // Crimson Rose
  { primary: '#4F46E5', secondary: '#818CF8', aura: '#A5B4FC', bg: '#1E1B4B' }, // Royal Indigo
  { primary: '#0D9488', secondary: '#14B8A6', aura: '#2DD4BF', bg: '#134E4A' }, // Aegean Teal
  { primary: '#9333EA', secondary: '#C084FC', aura: '#E9D5FF', bg: '#3B0764' }  // Astral Purple
];

class AvatarService {
  constructor() {
    this._cache = new Map();
  }

  /**
   * Generates a random fun nickname
   */
  rollNickname() {
    const adj = ADJECTIVES[Math.floor(Math.random() * ADJECTIVES.length)];
    const noun = NOUNS[Math.floor(Math.random() * NOUNS.length)];
    const suffix = Math.floor(Math.random() * 90) + 10;
    return `${adj}${noun}${suffix}`;
  }

  /**
   * Computes a deterministic 32-bit integer hash from any string
   */
  hashString(str) {
    let hash = 0;
    const cleanStr = String(str || 'guest').trim().toLowerCase();
    for (let i = 0; i < cleanStr.length; i++) {
      hash = ((hash << 5) - hash) + cleanStr.charCodeAt(i);
      hash |= 0;
    }
    return Math.abs(hash);
  }

  /**
   * Returns palette and archetype data for a nickname
   */
  getAvatarMeta(nickname) {
    const hash = this.hashString(nickname);
    const paletteIndex = hash % COLOR_PALETTES.length;
    const archetypeIndex = Math.floor(hash / 7) % 4; // 4 distinct character styles
    const archetypes = ['The Philologist Owl', 'The Cosmic Scholar', 'The Mystic Sphinx', 'The Neon Athena'];

    return {
      hash,
      palette: COLOR_PALETTES[paletteIndex],
      archetype: archetypes[archetypeIndex],
      archetypeIndex
    };
  }

  /**
   * Generates a unique, animated SVG avatar as an HTML/SVG string
   */
  generateAvatarSvg(nickname, options = {}) {
    const cacheKey = `${nickname}_${options.size || 80}_${options.animated !== false}`;
    if (this._cache.has(cacheKey)) {
      return this._cache.get(cacheKey);
    }

    const size = options.size || 80;
    const isAnimated = options.animated !== false;
    const meta = this.getAvatarMeta(nickname);
    const { hash, palette, archetypeIndex } = meta;
    const id = `av_${hash}_${size}`;

    // Deterministic accessories
    const hasCrown = (hash % 3 === 0);
    const hasGlasses = (hash % 2 === 0);
    const eyeVariation = hash % 3;

    const animCss = isAnimated ? `
      <style>
        #${id} .avatar-pulse-ring {
          animation: avatarPulse 3.5s ease-in-out infinite;
          transform-origin: 50px 50px;
        }
        #${id} .avatar-floating-body {
          animation: avatarFloat 4s ease-in-out infinite;
          transform-origin: 50px 50px;
        }
        #${id} .avatar-blink-eye {
          animation: avatarBlink 5s ease-in-out infinite;
          transform-origin: 50px 48px;
        }
        #${id} .avatar-sparkle {
          animation: avatarSparkle 2.5s ease-in-out infinite alternate;
          transform-origin: 50px 50px;
        }
        @keyframes avatarPulse {
          0%, 100% { transform: scale(1); opacity: 0.35; }
          50% { transform: scale(1.08); opacity: 0.7; }
        }
        @keyframes avatarFloat {
          0%, 100% { transform: translateY(0px) rotate(0deg); }
          50% { transform: translateY(-3.5px) rotate(0.8deg); }
        }
        @keyframes avatarBlink {
          0%, 94%, 98%, 100% { transform: scaleY(1); }
          96% { transform: scaleY(0.1); }
        }
        @keyframes avatarSparkle {
          0% { opacity: 0.2; transform: rotate(0deg) scale(0.9); }
          100% { opacity: 0.9; transform: rotate(180deg) scale(1.1); }
        }
      </style>
    ` : '';

    let characterFeatures = '';

    if (archetypeIndex === 0) {
      // 🦉 Archetype: The Philologist Owl
      characterFeatures = `
        <!-- Owl Ears/Tufts -->
        <polygon points="30,30 20,12 40,24" fill="${palette.primary}" />
        <polygon points="70,30 80,12 60,24" fill="${palette.primary}" />
        <!-- Head -->
        <circle cx="50" cy="52" r="32" fill="${palette.primary}" />
        <!-- Face Mask -->
        <ellipse cx="40" cy="50" rx="12" ry="14" fill="#FFFFFF" opacity="0.95" />
        <ellipse cx="60" cy="50" rx="12" ry="14" fill="#FFFFFF" opacity="0.95" />
        <!-- Eyes with Blink Animation -->
        <g class="avatar-blink-eye">
          <circle cx="40" cy="50" r="6" fill="${palette.bg}" />
          <circle cx="60" cy="50" r="6" fill="${palette.bg}" />
          <circle cx="42" cy="48" r="2.2" fill="#FFFFFF" />
          <circle cx="62" cy="48" r="2.2" fill="#FFFFFF" />
        </g>
        <!-- Beak -->
        <polygon points="46,55 54,55 50,65" fill="${palette.secondary}" />
        ${hasGlasses ? `
          <!-- Golden Scholar Spectacles -->
          <circle cx="40" cy="50" r="13" fill="none" stroke="${palette.aura}" stroke-width="2" />
          <circle cx="60" cy="50" r="13" fill="none" stroke="${palette.aura}" stroke-width="2" />
          <line x1="53" y1="50" x2="47" y2="50" stroke="${palette.aura}" stroke-width="2" />
        ` : ''}
      `;
    } else if (archetypeIndex === 1) {
      // 🔮 Archetype: The Cosmic Scholar
      characterFeatures = `
        <!-- Astral Hood/Helm -->
        <path d="M 20 65 C 16 35, 30 18, 50 18 C 70 18, 84 35, 80 65 Z" fill="${palette.primary}" />
        <!-- Face Void -->
        <circle cx="50" cy="50" r="24" fill="${palette.bg}" />
        <!-- Starlight Eyes with Blink Animation -->
        <g class="avatar-blink-eye">
          <ellipse cx="41" cy="48" rx="4" ry="6" fill="${palette.aura}" />
          <ellipse cx="59" cy="48" rx="4" ry="6" fill="${palette.aura}" />
          <circle cx="41" cy="46" r="1.8" fill="#FFFFFF" />
          <circle cx="59" cy="46" r="1.8" fill="#FFFFFF" />
        </g>
        <!-- Third Eye / Crystal -->
        <polygon class="avatar-sparkle" points="50,28 53,34 50,40 47,34" fill="${palette.secondary}" />
        <!-- Arcane Scarf -->
        <path d="M 26 64 Q 50 76 74 64 Q 50 82 26 64 Z" fill="${palette.secondary}" />
      `;
    } else if (archetypeIndex === 2) {
      // 🏛️ Archetype: The Mystic Sphinx
      characterFeatures = `
        <!-- Nemes Headdress -->
        <polygon points="18,34 32,16 68,16 82,34 76,72 24,72" fill="${palette.primary}" />
        <path d="M 28 16 L 36 70 M 64 70 L 72 16" stroke="${palette.secondary}" stroke-width="2" opacity="0.6" />
        <!-- Sphinx Face -->
        <circle cx="50" cy="48" r="22" fill="#FFFFFF" opacity="0.92" />
        <!-- Cat-like Eyes -->
        <g class="avatar-blink-eye">
          <polygon points="37,46 45,43 43,51 36,50" fill="${palette.primary}" />
          <polygon points="63,46 55,43 57,51 64,50" fill="${palette.primary}" />
        </g>
        <!-- Sphinx Mark -->
        <circle cx="50" cy="34" r="3" fill="${palette.secondary}" />
        <!-- Mouth -->
        <path d="M 46 58 Q 50 62 54 58" fill="none" stroke="${palette.bg}" stroke-width="2" stroke-linecap="round" />
      `;
    } else {
      // ⚡ Archetype: The Neon Athena
      characterFeatures = `
        <!-- Athena Crested Helm -->
        <path d="M 46 8 L 54 8 L 56 26 L 44 26 Z" fill="${palette.secondary}" />
        <path d="M 22 46 C 22 24, 78 24, 78 46 L 76 68 L 24 68 Z" fill="${palette.primary}" />
        <!-- Winged Visor -->
        <polygon points="26,36 12,24 24,48" fill="${palette.aura}" opacity="0.8" />
        <polygon points="74,36 88,24 76,48" fill="${palette.aura}" opacity="0.8" />
        <!-- Face -->
        <circle cx="50" cy="50" r="23" fill="#FFFFFF" opacity="0.95" />
        <!-- Radiant Eyes -->
        <g class="avatar-blink-eye">
          <circle cx="41" cy="48" r="5" fill="${palette.primary}" />
          <circle cx="59" cy="48" r="5" fill="${palette.primary}" />
          <circle cx="43" cy="46" r="1.8" fill="#FFFFFF" />
          <circle cx="61" cy="46" r="1.8" fill="#FFFFFF" />
        </g>
        <path d="M 45 59 Q 50 64 55 59" fill="none" stroke="${palette.bg}" stroke-width="2" stroke-linecap="round" />
      `;
    }

    const svg = `
      <svg id="${id}" class="animated-avatar-svg" width="${size}" height="${size}" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Avatar for ${nickname}">
        ${animCss}
        <defs>
          <linearGradient id="aura_grad_${hash}" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="${palette.primary}" />
            <stop offset="100%" stop-color="${palette.secondary}" />
          </linearGradient>
          <filter id="glow_${hash}" x="-20%" y="-20%" width="140%" height="140%">
            <feGaussianBlur stdDeviation="3.5" result="blur" />
            <feComposite in="SourceGraphic" in2="blur" operator="over" />
          </filter>
        </defs>

        <!-- Outer Animated Energy Aura -->
        <circle class="avatar-pulse-ring" cx="50" cy="50" r="44" fill="url(#aura_grad_${hash})" filter="url(#glow_${hash})" />

        <!-- Floating Character Body -->
        <g class="avatar-floating-body">
          ${characterFeatures}
        </g>
      </svg>
    `.trim();

    this._cache.set(cacheKey, svg);
    return svg;
  }

  /**
   * Generates a base64 Data URI for use in standard img src attributes
   */
  generateAvatarDataUri(nickname, options = {}) {
    const svg = this.generateAvatarSvg(nickname, options);
    return `data:image/svg+xml;utf8,${encodeURIComponent(svg)}`;
  }
}

export const avatarService = new AvatarService();
