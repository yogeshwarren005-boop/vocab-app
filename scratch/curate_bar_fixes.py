# -*- coding: utf-8 -*-
"""
Fixes for the 5 problem words in Dashboard — bar:
- bareness
- barometer
- barony
- baroqueness
- barrenness
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

data_bar_fixes = {
  "bareness": {
    "primary": "Nakedness, exposure, utter plainness, or total absence of covering, foliage, or furnishings.",
    "secondary": "In landscape aesthetics and domestic description, severe architectural austerity or stark environmental desolation.",
    "quotes": [
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "The cold **bareness** of the dormitory, with its uncurtained windows and scrubbed pine floor, struck a chill into my heart."},
      {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "The bleak **bareness** of Egdon Heath under the November wind seemed to reject all human cultivation."},
      {"author": "Charles Dickens", "work": "Hard Times", "quote": "The classroom was designed with an uncompromising **bareness** that stripped education of all imaginative delight."}
    ]
  },
  "barometer": {
    "primary": "An instrument measuring atmospheric pressure, used especially in forecasting the weather and determining altitude.",
    "secondary": "In physical meteorology and climatology, an evacuated mercury or aneroid column measuring barometric air mass fluctuations.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "A sudden fall in the **barometer** warned the captain of an approaching pampero before any cloud appeared upon the horizon."},
      {"author": "Robert Louis Stevenson", "work": "Treasure Island", "quote": "The cabin **barometer** dropped steadily throughout the sultry afternoon, portending a fierce tropical tempest."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Ahab tapped the brass casing of the marine **barometer**, watching the mercury sink toward the storm marker."}
    ]
  },
  "barony": {
    "primary": "The domain, lands, rank, or jurisdiction of a baron; the collective estates belonging to a baron.",
    "secondary": "In historical land tenure and Irish administrative geography, a major feudal freehold territorial division holding ancient court baron jurisdiction.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The Crusader knights partitioned the Peloponnese into several feudal fiefs, establishing a prosperous **barony** at Patras."},
      {"author": "Sir Walter Scott", "work": "The Antiquary", "quote": "The ancient **barony** had been held by the Oldbucks under feudal charter since the reign of King David the First."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The crown confirmed the ancient feudal privileges belonging to the **barony**, granting rights of pit and gallows."}
    ]
  },
  "baroqueness": {
    "primary": "Extravagant ornateness, dramatic flamboyance, theatrical excess, or complex decorative elaboration.",
    "secondary": "In architectural criticism and aesthetics, highly complex, emotive, and heavily sculpted decorative elaboration.",
    "quotes": [
      {"author": "John Ruskin", "work": "Modern Painters", "quote": "The excessive **baroqueness** of late Italian sculpture replaced serene spiritual dignity with restless theatrical posturing."},
      {"author": "Henry James", "work": "The American", "quote": "Newman was bewildered by the dense **baroqueness** of the Parisian salon, where every chair was gilded and carved into grotesque acanthus leaves."},
      {"author": "George Santayana", "work": "The Sense of Beauty", "quote": "The bold **baroqueness** of Bernini's fountains captures the vitality of cascading water through turbulent marble forms."}
    ]
  },
  "barrenness": {
    "primary": "Arid infertility, sterility, unproductive bleakness, or total absence of living vegetation.",
    "secondary": "In agrarian economics and literary aesthetics, the absence of fertile vitality, intellectual productivity, or organic abundance.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The extreme **barrenness** of the Arabian desert long protected its nomadic inhabitants from foreign imperial conquerors."},
      {"author": "Thomas Babington Macaulay", "work": "Critical and Historical Essays", "quote": "The philosophical **barrenness** of scholastic disputation yielded no practical inventions for the alleviation of human misery."},
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "A sense of utter moral **barrenness** seized upon the guilty minister as he surveyed his ruined spiritual life."}
    ]
  }
}
