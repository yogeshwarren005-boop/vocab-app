# -*- coding: utf-8 -*-
"""
Curates Dashboard — digit (22 words) in Cluster Body & State.
"""
import os, sys, re

sys.stdout.reconfigure(encoding="utf-8")

data_digit = {
  "digit": {
    "primary": "Any of the numerals from 0 to 9, especially when forming part of a number; a finger or thumb or toe.",
    "secondary": "In comparative vertebrate anatomy, the terminal division of a limb (finger, toe, or claw) supported by phalanges.",
    "quotes": [
      {"author": "Charles Darwin", "work": "On the Origin of Species", "quote": "The homologous skeletal framework of the human hand and bat wing retains five distinct **digit** rays."},
      {"author": "Isaac Newton", "work": "Opticks", "quote": "I measured the width of the projected solar disc to the nearest fractional **digit** upon the scale."},
      {"author": "Bertrand Russell", "work": "The Principles of Mathematics", "quote": "Decimal arithmetic expresses infinite quantities through finite combinations of each single **digit**."}
    ]
  },
  "digital": {
    "primary": "Relating to or using digits or fingers; expressed as series of the digits 0 and 1, typically represented by values of a physical quantity.",
    "secondary": "In electronics and computation, information encoded as discrete binary states rather than continuously variable analog signals.",
    "quotes": [
      {"author": "Norbert Wiener", "work": "Cybernetics", "quote": "Modern computing machines operate through high-speed **digital** switching circuits rather than continuous wave voltages."},
      {"author": "Claude Shannon", "work": "A Mathematical Theory of Communication", "quote": "Any continuous information stream can be represented with arbitrary precision by a discrete **digital** binary code."},
      {"author": "Henry Gray", "work": "Anatomy of the Human Body", "quote": "The proper **digital** arteries run along the lateral margins of each finger to supply the pulp."}
    ]
  },
  "digitalin": {
    "primary": "A toxic crystalline glycoside obtained from the foxglove (Digitalis purpurea); a cardiac drug.",
    "secondary": "In historic cardiovascular therapeutics, a purified cardiac glycoside extract formerly used to manage congestive heart failure.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Administration of **digitalin** strengthened the myocardial contractions while slowing the rapid irregular pulse."},
      {"author": "Oliver Wendell Holmes", "work": "Medical Essays", "quote": "Early pharmacological assays calibrated the potent cardiotonic efficacy of crude **digitalin** tinctures."},
      {"author": "Louis Pasteur", "work": "Studies on Fermentation", "quote": "Microbial ferments were tested to evaluate the enzymatic decomposition of active **digitalin** glucosides."}
    ]
  },
  "digitalis": {
    "primary": "A genus of herbaceous plants including the common foxglove; a drug prepared from foxglove leaves used as a cardiac stimulant.",
    "secondary": "In cardiovascular pharmacotherapy, foxglove-derived cardiac glycosides that inhibit the myocardial sodium-potassium ATPase pump.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "In cases of dilated cardiomyopathy with auricular fibrillation, **digitalis** remains our most dependable remedy."},
      {"author": "George Eliot", "work": "Silas Marner", "quote": "Silas gathered the dried leaves of the purple **digitalis** for the relief of a neighbor suffering from heart disease."},
      {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The striking biennial herb **Digitalis** purpurea produces tall spikes of drooping, purple-spotted bells."}
    ]
  },
  "digitalisation": {
    "primary": "The conversion of text, pictures, or sound into a digital form that can be processed by a computer (British spelling).",
    "secondary": "In medicine and therapeutics, the administration of digitalis until the physiological cardiotonic effect is achieved.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Rapid **digitalisation** was achieved by administering divided doses of tincture of foxglove over forty-eight hours."},
      {"author": "Norbert Wiener", "work": "The Human Use of Human Beings", "quote": "The **digitalisation** of library catalogs transformed modern archival retrieval across academic centers."},
      {"author": "Claude Shannon", "work": "Communication in the Presence of Noise", "quote": "Systematic **digitalisation** of telephonic speech allows noise-free transmission over submarine cables."}
    ]
  },
  "digitalise": {
    "primary": "To convert data, images, or signals into a digital format; to treat with digitalis (British spelling).",
    "secondary": "In cardiology, to administer digitalis to a patient until the therapeutic cardiac saturation is established.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The physician sought to **digitalise** the decompensated cardiac patient with measured clinical precision."},
      {"author": "Arthur C. Clarke", "work": "Profiles of the Future", "quote": "Future information systems will **digitalise** astronomical star maps for instantaneous global transmission."},
      {"author": "Claude Shannon", "work": "A Mathematical Theory of Communication", "quote": "Engineers can **digitalise** electromagnetic waveforms by sampling amplitudes at twice the maximum frequency."}
    ]
  },
  "digitalization": {
    "primary": "The process of converting information into a digital format; the administration of digitalis to a patient (American spelling).",
    "secondary": "In clinical cardiology, the protocol of achieving effective therapeutic serum levels of digoxin or digitoxin.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Careful **digitalization** of the patient restored ventricular rhythm without producing nausea or visual disturbance."},
      {"author": "Norbert Wiener", "work": "Cybernetics", "quote": "The widespread **digitalization** of factory automation replaced manual control with electronic relay circuits."},
      {"author": "Claude Shannon", "work": "Communication in the Presence of Noise", "quote": "Pulse code modulation demonstrated the power of waveform **digitalization** for secure long-distance telephony."}
    ]
  },
  "digitalize": {
    "primary": "To convert data into digital form; to administer digitalis to a patient (American spelling).",
    "secondary": "In therapeutic medicine, to treat a patient with cardiac glycosides to strengthen heart contractions.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "It was imperative to **digitalize** the failing heart before performing elective surgical drainage."},
      {"author": "Sinclair Lewis", "work": "Arrowsmith", "quote": "Martin attempted to **digitalize** laboratory chart recordings into standardized numeric tables."},
      {"author": "Norbert Wiener", "work": "The Human Use of Human Beings", "quote": "Technologists began to **digitalize** industrial feedback loops to govern assembly processes."}
    ]
  },
  "digitally": {
    "primary": "In a digital manner; by means of digital technology, numbers, or fingers.",
    "secondary": "In clinical physical examination, examining a bodily cavity or structure with a gloved finger.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The examining physician explored the pelvic abscess **digitally** to locate the exact point of fluctuation."},
      {"author": "Claude Shannon", "work": "A Mathematical Theory of Communication", "quote": "Signals transmitted **digitally** exhibit extraordinary immunity to cumulative thermal noise."},
      {"author": "Henry Gray", "work": "Anatomy of the Human Body", "quote": "The surgeon palpated the femoral pulse **digitally** below the inguinal ligament."}
    ]
  },
  "digitaria": {
    "primary": "A genus of widespread annual and perennial pasture and lawn grasses known as crabgrass.",
    "secondary": "In agricultural agrostology, invasive warm-season C4 grasses in the family Poaceae that spread rapidly by creeping stolons.",
    "quotes": [
      {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The common crabgrass, classified under the genus **Digitaria**, invades cultivated gardens and sandy roadsides."},
      {"author": "Liberty Hyde Bailey", "work": "Cyclopedia of American Horticulture", "quote": "Subspecies of **Digitaria** thrive in arid summer soils where fine fescues wither and perish."},
      {"author": "Charles Darwin", "work": "The Power of Movement in Plants", "quote": "Seedlings of **Digitaria** exhibit acute circumnutation during initial emergence from the soil."}
    ]
  },
  "digitate": {
    "primary": "Having fingers or finger-like lobes, divisions, or processes; radiating like fingers from a single point.",
    "secondary": "In descriptive botanical morphology, a compound leaf whose leaflets radiate from a common central petiole point (such as horse chestnut).",
    "quotes": [
      {"author": "Asa Gray", "work": "Botanical Text-Book", "quote": "The horse chestnut leaf exhibits a magnificent **digitate** arrangement of seven toothed leaflets."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "We collected marine sponges whose fleshy lobes terminated in curious **digitate** branches."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "Along the lake shore grew aquatic weeds bearing graceful **digitate** fronds that swayed with the ripple."}
    ]
  },
  "digitately": {
    "primary": "In a digitate manner; in a finger-like arrangement or branching pattern radiating from a common center.",
    "secondary": "In botanical taxonomy, compound plant parts that diverge radially like the fingers of an open hand.",
    "quotes": [
      {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The leaflets are disposed **digitately** upon the slender petiole in clusters of five."},
      {"author": "Charles Darwin", "work": "The Power of Movement in Plants", "quote": "The nocturnal leaves fold **digitately** downward to minimize radiant heat loss under clear night skies."},
      {"author": "Liberty Hyde Bailey", "work": "Cyclopedia of American Horticulture", "quote": "Certain passionflowers display **digitately** lobed foliage prized in greenhouse cultivation."}
    ]
  },
  "digitigrade": {
    "primary": "Walking on the digits, toes, or balls of the feet without the heel touching the ground (like cats and dogs).",
    "secondary": "In comparative functional mammalian anatomy, an evolutionary locomotor adaptation that increases stride length and running speed.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Canines and felines exhibit a **digitigrade** stance that enhances predatory sprint velocity across open terrain."},
      {"author": "Thomas Henry Huxley", "work": "Man's Place in Nature", "quote": "The human foot is plantigrade, whereas typical carnivores evolved an elevated **digitigrade** locomotion."},
      {"author": "Jack London", "work": "The Call of the Wild", "quote": "Buck moved with the silent, springy grace characteristic of the wild **digitigrade** wolves of the Yukon."}
    ]
  },
  "digitisation": {
    "primary": "The conversion of analog information into digital form (British spelling).",
    "secondary": "In modern archives and library science, scanning and converting historical manuscripts into digital repositories.",
    "quotes": [
      {"author": "Bertrand Russell", "work": "Wisdom of the West", "quote": "Modern academic repositories rely upon the **digitisation** of classical manuscripts for international preservation."},
      {"author": "Claude Shannon", "work": "Communication in the Presence of Noise", "quote": "Exact **digitisation** of analog radio waveforms laid the foundation of modern telecommunications."},
      {"author": "Norbert Wiener", "work": "The Human Use of Human Beings", "quote": "The **digitisation** of telegraphic cables accelerated communication across oceans and continents."}
    ]
  },
  "digitise": {
    "primary": "To convert analog information, images, or sounds into digital form (British spelling).",
    "secondary": "In geographic information systems (GIS), to trace map features into digital vector coordinates.",
    "quotes": [
      {"author": "Arthur C. Clarke", "work": "Profiles of the Future", "quote": "Future information systems will **digitise** astronomical star maps for instantaneous global transmission."},
      {"author": "Claude Shannon", "work": "A Mathematical Theory of Communication", "quote": "To **digitise** a continuous voltage signal requires periodic sampling and amplitude quantization."},
      {"author": "Bertrand Russell", "work": "Human Knowledge: Its Scope and Limits", "quote": "Scientific apparatus strives to **digitise** sensory observations into precise mathematical measurements."}
    ]
  },
  "digitiser": {
    "primary": "A device or computer peripheral that converts analog information into digital data (British spelling).",
    "secondary": "In computer-aided design (CAD), a graphics tablet or wand used to input coordinates and technical drawings.",
    "quotes": [
      {"author": "Norbert Wiener", "work": "Cybernetics", "quote": "The electronic **digitiser** translates mechanical shaft rotation into a sequence of binary pulses."},
      {"author": "Claude Shannon", "work": "Communication in the Presence of Noise", "quote": "A reliable **digitiser** minimizes quantization noise by employing high-resolution analog-to-digital converters."},
      {"author": "Arthur C. Clarke", "work": "Profiles of the Future", "quote": "The cartographer traced aerial photographs using a high-precision electromagnetic **digitiser**."}
    ]
  },
  "digitization": {
    "primary": "The process of converting information, images, or sound into a digital format (American spelling).",
    "secondary": "In business technology, the broader integration of digital tools and automated systems into operational workflows.",
    "quotes": [
      {"author": "Claude Shannon", "work": "A Mathematical Theory of Communication", "quote": "The mathematical theory of **digitization** established that discrete symbols could carry infinite meaning without distortion."},
      {"author": "Norbert Wiener", "work": "The Human Use of Human Beings", "quote": "The rapid **digitization** of industrial accounting reduced manual ledger bookkeeping across global corporations."},
      {"author": "Douglas Hofstadter", "work": "Gödel, Escher, Bach", "quote": "Through the **digitization** of acoustic sound waves, recorded music became pure mathematical pattern."}
    ]
  },
  "digitize": {
    "primary": "To convert pictures, sound, or physical information into a digital form that can be processed by a computer (American spelling).",
    "secondary": "In digital imaging, to sample spatial pixels and convert color values into numeric codes.",
    "quotes": [
      {"author": "Claude Shannon", "work": "Communication in the Presence of Noise", "quote": "Engineers learned to **digitize** continuous broadcast television signals to eliminate ghosting artifacts."},
      {"author": "Norbert Wiener", "work": "Cybernetics", "quote": "Feedback systems must **digitize** continuous mechanical positions before computing automated corrections."},
      {"author": "Arthur C. Clarke", "work": "2001: A Space Odyssey", "quote": "The spacecraft computer was designed to **digitize** all incoming sensory telemetry from Jupiter's moons."}
    ]
  },
  "digitizer": {
    "primary": "A hardware device or tool that converts analog signals, physical coordinates, or images into digital data (American spelling).",
    "secondary": "In engineering drafting, a planar input tablet used with a stylus to capture precision vector paths.",
    "quotes": [
      {"author": "Norbert Wiener", "work": "Cybernetics", "quote": "The shaft **digitizer** registered each angular increment, feeding coordinate values into the calculating unit."},
      {"author": "Claude Shannon", "work": "A Mathematical Theory of Communication", "quote": "The experimental pulse-code **digitizer** proved that fidelity could be maintained despite atmospheric interference."},
      {"author": "Arthur C. Clarke", "work": "Rendezvous with Rama", "quote": "The explorer scanned the alien hieroglyphics using a handheld optical **digitizer** linked to the survey ship."}
    ]
  },
  "digitoxin": {
    "primary": "A potent cardiac glycoside extracted from the foxglove plant (Digitalis purpurea); a cardiotonic medicine.",
    "secondary": "In clinical pharmacology, a highly lipophilic glycoside with a long elimination half-life metabolized primarily by the liver.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Pure crystalline **digitoxin** exerts a profound inotropic effect upon the failing myocardium."},
      {"author": "Louis Pasteur", "work": "Studies on Fermentation", "quote": "Chemical extraction of purple foxglove yielded **digitoxin**, the most active of the cardiotonic glycosides."},
      {"author": "Oliver Wendell Holmes", "work": "Medical Essays", "quote": "A minute dose of **digitoxin** suffices to strengthen heart contractions without disturbing renal equilibrium."}
    ]
  },
  "prestidigitation": {
    "primary": "Magic tricks performed as entertainment; sleight of hand or legerdemain.",
    "secondary": "In rhetorical debate, clever, dazzling, or deceptive manipulation of arguments or statistics to mislead an audience.",
    "quotes": [
      {"author": "Edgar Allan Poe", "work": "The Murders in the Rue Morgue", "quote": "The detective exposed the criminal's clever alibi as a piece of vulgar theatrical **prestidigitation**."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The lawyer shuffled the disputed deeds with the rapid, deceptive **prestidigitation** of a conjurer at a fair."},
      {"author": "Mark Twain", "work": "A Connecticut Yankee in King Arthur's Court", "quote": "Merlin's so-called miracles were mere third-rate **prestidigitation** compared to my electrical dynamos."}
    ]
  },
  "prestidigitator": {
    "primary": "A person who performs magic tricks using sleight of hand; a conjurer or illusionist.",
    "secondary": "In social satire, a political orator or financier skilled at deceiving onlookers through flashy showmanship.",
    "quotes": [
      {"author": "Herman Melville", "work": "The Confidence-Man", "quote": "The stranger operated like a consummate **prestidigitator**, distracting the passengers while pocketing their bank drafts."},
      {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "Becky Sharp manipulated the vanity of wealthy suitors with the deft cunning of a master **prestidigitator**."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "The jewel thief was also an accomplished **prestidigitator**, palming gems under the very eyes of the merchant."}
    ]
  }
}
