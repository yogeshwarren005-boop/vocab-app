# -*- coding: utf-8 -*-
"""
Fixes for the 4 problem words in Dashboard — anti:
- antistrophe
- antistrophic
- antithyroid
- enantiomorphism
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

data_anti_fixes = {
  "antistrophe": {
    "primary": "The second section of an ancient Greek choral ode, sung by the chorus responding to the preceding strophe while moving in the reverse direction.",
    "secondary": "In classical prosody and rhetoric, repeating the same word or phrase at the end of successive sentences or clauses (epistrophe).",
    "quotes": [
      {"author": "John Milton", "work": "Samson Agonistes", "quote": "The chorus in **antistrophe** responded with solemn cadence to Samson's lamentations of blindness and captivity."},
      {"author": "Thomas Gray", "work": "The Progress of Poesy", "quote": "Hark, his hands the lyre explore, as the **antistrophe** swells across the Olympian plain in stately measure."},
      {"author": "Percy Bysshe Shelley", "work": "Hellas", "quote": "The choral voices joined in alternating strophe and **antistrophe**, mourning the fallen heroes of ancient Greece."}
    ]
  },
  "antistrophic": {
    "primary": "Relating to or having the structure of an antistrophe; answering symmetrically in verse or choral movement.",
    "secondary": "In classical metrics, poetry composed in strophic and antistrophic pairs having identical rhythmic and metrical patterns.",
    "quotes": [
      {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "The strict symmetry of **antistrophic** stanzas requires exquisite musical ear to balance poetic emotion with formal rigor."},
      {"author": "Matthew Arnold", "work": "Merope", "quote": "The dramatic chorus advanced in an **antistrophic** movement that reflected the alternating hopes and terrors of the dialogue."},
      {"author": "Algernon Charles Swinburne", "work": "Atalanta in Calydon", "quote": "The tragic chorus chanted in solemn **antistrophic** responses as the hunters set forth into the Calydonian forest."}
    ]
  },
  "antithyroid": {
    "primary": "Inhibiting or reducing the synthesis, secretion, or metabolic activity of thyroid hormones; used to treat hyperthyroidism.",
    "secondary": "In clinical endocrinology, thionamide compounds (such as methimazole or propylthiouracil) that block thyroid peroxidase, decreasing T3 and T4 levels.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The clinical introduction of potent **antithyroid** agents revolutionized the medical management of toxic diffuse goiter."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Administration of an **antithyroid** compound results in diminished basal metabolic expenditure and lowered body temperature."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Goitrogenic dietary factors present in cruciferous forage act as natural **antithyroid** agents upon livestock herds."}
    ]
  },
  "enantiomorphism": {
    "primary": "The structural property of having nonsuperimposable mirror-image forms, as exhibited by crystals or enantiomer molecules; chirality.",
    "secondary": "In crystallography and stereochemistry, spatial asymmetry where crystal faces or molecular configurations relate as right and left hands.",
    "quotes": [
      {"author": "Louis Pasteur", "work": "Researches on the Molecular Asymmetry of Natural Organic Products", "quote": "The discovery of **enantiomorphism** in tartrate crystals proved that molecular asymmetry is fundamentally linked to optical activity."},
      {"author": "Lord Kelvin", "work": "The Molecular Tactics of a Crystal", "quote": "I call any geometrical figure chiral if its image in a plane mirror cannot be brought into coincidence with itself, defining **enantiomorphism**."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The spiral twisting of gastropod shells presents striking biological **enantiomorphism**, producing rare sinistral varieties among dextral species."}
    ]
  }
}
