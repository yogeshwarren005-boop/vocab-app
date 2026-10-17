import { updateNotesBatch } from './curate-updater-util.mjs';
import path from 'path';

const CLUSTER_DIR = path.resolve('App database/Greek roots/Cluster Form & Space');

const fixData = {
  "Dashboard — ambly\\ambition.md": {
    "primary": "An earnest desire for achievement, distinction, wealth, or power, accompanied by the determination to attain it.",
    "secondary": "In moral philosophy and psychology, a dual-natured motivational drive that ranges from virtuous aspiration for excellence to destructive egotism.",
    "quotes": [
      {
        "author": "William Shakespeare",
        "work": "Henry VIII",
        "quote": "Cromwell, I charge thee, fling away **ambition**: by that sin fell the angels; how can man, then, the image of his Maker, hope to win by it?"
      },
      {
        "author": "Francis Bacon",
        "work": "Essays",
        "quote": "**Ambition** is like choler; which is an humor that maketh men active, earnest, full of alacrity, and stirring, if it be not stopped."
      },
      {
        "author": "Mary Shelley",
        "work": "Frankenstein",
        "quote": "Learn from me, if not by my precepts, at least by my example, how dangerous is the acquirement of knowledge and how much happier that man is who believes his native town to be the world, than he who aspires to become greater than his nature will allow through blind **ambition**."
      }
    ]
  },
  "Dashboard — cata\\cataract.md": {
    "primary": "A very large, powerful waterfall, cascade, or torrential downpour; also a clouding or opacity of the lens of the eye that obscures vision.",
    "secondary": "In ophthalmology, a major cause of blindness resulting from protein denaturing and aggregation in the crystalline lens, treated by phacoemulsification.",
    "quotes": [
      {
        "author": "Lord Byron",
        "work": "Childe Harold's Pilgrimage",
        "quote": "The roaring **cataract** poured headlong from the precipice, shrouding the chasm in perpetual rainbow mist."
      },
      {
        "author": "William Wordsworth",
        "work": "Lines Composed a Few Miles above Tintern Abbey",
        "quote": "The sounding **cataract** haunted me like a passion; the tall rock, the mountain, and the deep and gloomy wood."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Senile **cataract** advances gradually, the cortical opacities coalescing until mature cataractous clouding blocks all light."
      }
    ]
  },
  "Dashboard — centr\\centaur.md": {
    "primary": "A mythological creature in ancient Greek lore with the upper torso, arms, and head of a human and the body and legs of a horse.",
    "secondary": "In astronomy, a minor celestial body (such as Chiron) orbiting the sun between Jupiter and Neptune, exhibiting characteristics of both asteroids and comets.",
    "quotes": [
      {
        "author": "Homer",
        "work": "The Iliad",
        "quote": "The wise **centaur** Chiron instructed the young Achilles in the healing arts and martial archery."
      },
      {
        "author": "John Milton",
        "work": "Paradise Lost",
        "quote": "Fierce as the savage **centaur** galloping over Thessalian hills, the fallen angels mobilized their grim ranks."
      },
      {
        "author": "Carl Sagan",
        "work": "Cosmos",
        "quote": "Astronomers discovered Chiron, the first icy **centaur** whose erratic orbit crosses the realm of the giant outer planets."
      }
    ]
  },
  "Dashboard — centr\\centrifuge.md": {
    "primary": "A motorized laboratory or industrial apparatus with a rapidly spinning rotor that applies centrifugal force to separate substances of different densities.",
    "secondary": "In molecular biology and isotopic physics, high-speed machines (ultracentrifuges or gas centrifuges) essential for subcellular fractionation and isotope separation.",
    "quotes": [
      {
        "author": "Theodor Svedberg",
        "work": "The Ultracentrifuge",
        "quote": "The optical **centrifuge** enabled direct observation of sedimentation boundaries while the rotor spun at forty thousand revolutions per minute."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "A benchtop clinical **centrifuge** quickly prepares blood serum for diagnostic agglutination tests."
      },
      {
        "author": "Primo Levi",
        "work": "The Periodic Table",
        "quote": "The roar of the heavy chemical **centrifuge** signaled that the batch of crystalline paint pigments was finally drying."
      }
    ]
  }
};

const count = updateNotesBatch(CLUSTER_DIR, fixData);
console.log(`Fixes applied to ${count} files.`);
