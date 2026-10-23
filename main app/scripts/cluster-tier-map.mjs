/**
 * cluster-tier-map.mjs — Comprehensive 3-Tier Cluster Categorization Map
 * Maps each of the 120 clusters across English Vocabulary Master, Greek Roots, and Latin Roots
 * to its designated Frequency & Pedagogical Priority Tier.
 */

export const TIER_FOLDER_NAMES = {
  1: 'Tier 1 — Words to Learn First',
  2: 'Tier 2 — Words to Learn Later',
  3: 'Tier 3 — Words to Learn Last'
};

export const CLUSTER_TIER_MAP = {
  english: {
    // Tier 1: Core Human Experience & Universal Dynamics (10 clusters)
    'Cluster Mind and Emotion': 1,
    'Cluster Speech and Lore': 1,
    'Cluster Motion and Force': 1,
    'Cluster Time and Seasons': 1,
    'Cluster Light and Darkness': 1,
    'Cluster Growth and Decay': 1,
    'Cluster Sight and Vision': 1,
    'Cluster Sound and Silence': 1,
    'Cluster Pain and Healing': 1,
    'Cluster Friendship and Enmity': 1,

    // Tier 2: Elevated Aesthetic, Social & Moral Registers (11 clusters)
    'Cluster Beauty and Ugliness': 2,
    'Cluster Pride and Humility': 2,
    'Cluster Bound and Restraint': 2,
    'Cluster Conflict and Strife': 2,
    'Cluster Craft and Shaping': 2,
    'Cluster Journey and Travel': 2,
    'Cluster Trade and Barter': 2,
    'Cluster Wealth and Poverty': 2,
    'Cluster Shadow and Secrecy': 2,
    'Cluster Stealth and Cunning': 2,
    'Cluster Speed and Haste': 2,

    // Tier 3: Archaic Realia, Mythic Lore & Naturalistic Realia (9 clusters)
    'Cluster Magic and Spell': 3,
    'Cluster Fate and Fortune': 3,
    'Cluster Feast and Hunger': 3,
    'Cluster Sleep and Waking': 3,
    'Cluster Shelter and Abode': 3,
    'Cluster Fire and Heat': 3,
    'Cluster Water and Liquid': 3,
    'Cluster Earth and Stone': 3,
    'Cluster Weather and Wilderness': 3
  },

  greek: {
    // Tier 1: Foundational Classical Roots (8 clusters)
    'Cluster Action': 1,
    'Cluster Beginning & Primacy': 1,
    'Cluster Cognition & Mind': 1,
    'Cluster Speech & Language': 1,
    'Cluster Time & Chronology': 1,
    'Cluster Light & Vision': 1,
    'Cluster Life & Vitality': 1,
    'Cluster Number & Mathematics': 1,

    // Tier 2: Academic, Cultural & Scientific Inquiry (12 clusters)
    'Cluster Feeling & Sensation': 2,
    'Cluster Society & Governance': 2,
    'Cluster Structure & Form': 2,
    'Cluster Physics & Chemistry': 2,
    'Cluster Turning & Transformation': 2,
    'Cluster Self & Identity': 2,
    'Cluster Sound & Auditory': 2,
    'Cluster Art, Craft & Design': 2,
    'Cluster Nature & Cosmos': 2,
    'Cluster War & Conflict': 2,
    'Cluster Power, Strength & Dominion': 2,
    'Cluster Law & Order': 2,

    // Tier 3: Hyper-Specialized Taxonomy & Archaic Realia (10 clusters)
    'Cluster Animals & Zoology': 3,
    'Cluster Plants & Botany': 3,
    'Cluster Medicine & Pathology': 3,
    'Cluster Body & Physiology': 3,
    'Cluster Earth & Geology': 3,
    'Cluster Form & Space': 3,
    'Cluster Motion & Direction': 3,
    'Cluster Water & Hydrology': 3,
    'Cluster Writing & Script': 3,
    'Cluster Science & Inquiry': 3
  },

  latin: {
    // Tier 1: Core Action, Motion & Social Infrastructure (18 clusters)
    'Cluster Action': 1,
    'Cluster Action & State': 1,
    'Cluster Motion': 1,
    'Cluster Placing': 1,
    'Cluster Structure': 1,
    'Cluster Speech & Communication': 1,
    'Cluster Mind & Knowledge': 1,
    'Cluster Number & Measure': 1,
    'Cluster Sending': 1,
    'Cluster Holding': 1,
    'Cluster Carrying': 1,
    'Cluster Order': 1,
    'Cluster Life': 1,
    'Cluster Society': 1,
    'Cluster Truth, Deception & Error': 1,
    'Cluster Good & Bad': 1,
    'Cluster Turning': 1,
    'Cluster Movement & Speed': 1,

    // Tier 2: Law, Literature, Ethics & Governance (22 clusters)
    'Cluster Law': 2,
    'Cluster Law, Justice & Feudal': 2,
    'Cluster Virtue': 2,
    'Cluster Thought': 2,
    'Cluster Asking & Seeking': 2,
    'Cluster Emotion': 2,
    'Cluster Time': 2,
    'Cluster Speech': 2,
    'Cluster Writing': 2,
    'Cluster Senses & Perception': 2,
    'Cluster Sight': 2,
    'Cluster Light': 2,
    'Cluster Power': 2,
    'Cluster Binding': 2,
    'Cluster Separation & Loosening': 2,
    'Cluster Quantity': 2,
    'Cluster Space & Environment': 2,
    'Cluster Objects & Forms': 2,
    'Cluster Weight': 2,
    'Cluster Nature': 2,
    'Cluster War': 2,
    'Cluster Destruction': 2,

    // Tier 3: Obscure Biological, Archaic & Dead Nomenclature (20 clusters)
    'Cluster Animal Adjectives & Biological': 3,
    'Cluster Animal & Plant': 3,
    'Cluster Anatomy & Clinical Medicine': 3,
    'Cluster Botany, Minerals & Elements': 3,
    'Cluster Fire, Heat & Ash': 3,
    'Cluster Food, Eating & Drink': 3,
    'Cluster Clothing & Covering': 3,
    'Cluster Color & Appearance': 3,
    'Cluster Touch': 3,
    'Cluster Building & Dwelling': 3,
    'Cluster Body': 3,
    'Cluster Body & State': 3,
    'Cluster Death': 3,
    'Cluster Sacred': 3,
    'Cluster Faith': 3,
    'Cluster Equality': 3,
    'Cluster General': 3,
    'Cluster Giving & Receiving': 3,
    'Cluster Sleep, Rest & Stillness': 3,
    'Cluster Greek-Latin Hybrid': 3
  }
};

/**
 * Returns the tier (1, 2, or 3) for a given cluster
 * @param {string} section - 'english' | 'greek' | 'latin'
 * @param {string} clusterName
 * @returns {1|2|3}
 */
export function getClusterTier(section, clusterName) {
  const normSec = (section || '').toLowerCase();
  const c = clusterName.startsWith('Cluster ') ? clusterName : `Cluster ${clusterName}`;
  if (normSec.includes('greek')) return CLUSTER_TIER_MAP.greek[c] || 2;
  if (normSec.includes('latin')) return CLUSTER_TIER_MAP.latin[c] || 2;
  return CLUSTER_TIER_MAP.english[c] || 2;
}
