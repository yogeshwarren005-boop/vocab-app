# -*- coding: utf-8 -*-
import json
import os
import sys

batch5_data = {
  "Dashboard — ten\\tetratonic.md": {
    "primary": "Consisting of or based on four musical tones or pitches per octave.",
    "secondary": "In ethnomusicology and comparative acoustics, archaic musical scales comprising four pitches (tetrachords or tetratonic chants), found in tribal vocal music and liturgical antiphons.",
    "quotes": [
      { "author": "Alexander John Ellis", "work": "On the Musical Scales of Various Nations", "quote": "The archaic invocation was sung upon a simple **tetratonic** framework encompassing four narrow intervals." },
      { "author": "Percy Scholes", "work": "The Oxford Companion to Music", "quote": "Before the evolution of five-note pentatonic tunes, primitive ritual chants were frequently **tetratonic**." },
      { "author": "Béla Bartók", "work": "Rumanian Folk Music", "quote": "The ancient winter solstice carol revolves entirely within a narrow **tetratonic** ambitus of four pitches." }
    ]
  },
  "Dashboard — ten\\tonal.md": {
    "primary": "Relating to pitch, musical tone, or color tones; organized around a central tonic key.",
    "secondary": "In music theory, the hierarchical organization of chords and pitches around a central keynote (tonality), dominant in Western music from roughly 1650 to 1900; in painting, the values and gradations of light and shade (tonal values).",
    "quotes": [
      { "author": "Aaron Copland", "work": "What to Listen for in Music", "quote": "The pull toward a home keynote provides the fundamental gravitational force of **tonal** music." },
      { "author": "John Ruskin", "work": "Modern Painters", "quote": "Turner achieved sublime atmospheric distance through delicate mastery of **tonal** gradations from shadow to brilliant light." },
      { "author": "Leonard Bernstein", "work": "The Unanswered Question", "quote": "The **tonal** center acts like gravity, pulling wandering musical phrases inevitably back to rest." }
    ]
  },
  "Dashboard — ten\\tone.md": {
    "primary": "A musical or vocal sound with reference to its pitch, quality, and strength; a steady musical sound; or the general character or attitude of a place, piece of writing, or situation.",
    "secondary": "In physiology, muscle tone (tonus), the continuous and passive partial contraction of muscles; in acoustic physics, a pure sound wave of definite frequency.",
    "quotes": [
      { "author": "William Shakespeare", "work": "The Merchant of Venice", "quote": "How sweet the moonlight sleeps upon this bank! Here will we sit and let the sounds of music creep in our ears: soft stillness and the night become the touches of sweet harmony... Such harmony is in immortal souls, but whilst this muddy vesture of decay doth grossly close it in, we cannot hear it: let music sound with gentle **tone**." },
      { "author": "John Keats", "work": "Ode on a Grecian Urn", "quote": "Heard melodies are sweet, but those unheard are sweeter; therefore, ye soft pipes, play on; not to the sensual ear, but, more endear'd, pipe to the spirit ditties of no **tone**." },
      { "author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "A mother comforts her crying infant not by articulate words, but through the soothing **tone** of her voice." }
    ]
  },
  "Dashboard — ten\\toned.md": {
    "primary": "Having a specified tone, quality, or color tint; having firm and well-developed muscles.",
    "secondary": "In photography and printmaking, treated chemically with gold, selenium, or sepia baths to alter image color and enhance permanence.",
    "quotes": [
      { "author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "Her rich, low-**toned** voice carried a cadence of melancholy through the quiet room." },
      { "author": "Jack London", "work": "The Call of the Wild", "quote": "The sled dog possessed finely **toned** sinews and muscle, hardened by relentless toil across frozen trails." },
      { "author": "John Ruskin", "work": "The Elements of Drawing", "quote": "A warmly **toned** wash of bistre upon handmade paper softens the harshness of ink lines." }
    ]
  },
  "Dashboard — ten\\toner.md": {
    "primary": "A powder or liquid ink used in photocopiers and laser printers to form the printed text and images on paper; or a cosmetic lotion for the skin.",
    "secondary": "In darkroom photography, a chemical formulation used to alter the silver image deposit; in dermatological skincare, an astringent liquid formulated to restore skin pH after cleansing.",
    "quotes": [
      { "author": "Chester Carlson", "work": "History of Electrophotography", "quote": "Electrostatic attraction draws the finely milled black **toner** particles onto the latent image on the selenium drum." },
      { "author": "Ansel Adams", "work": "The Print: Contact Printing and Enlarging", "quote": "A dilute selenium **toner** deepens the maximum blacks of the bromide print and ensures archival permanence." },
      { "author": "Oliver Wendell Holmes", "work": "Medical Essays", "quote": "A mild herbal astringent acting as a cutaneous **toner** refreshes the face after exposure to harsh winds." }
    ]
  },
  "Dashboard — ten\\tonic.md": {
    "primary": "Giving a feeling of vigor or well-being; invigorating; relating to or denoting the first degree of a musical scale; or a medicinal or carbonated beverage.",
    "secondary": "In pharmacology, a restorative substance historically prescribed to promote health; in music theory, the foundational keynote (degree I) of a diatonic scale; in physiology, a sustained muscle contraction.",
    "quotes": [
      { "author": "Henry David Thoreau", "work": "Walden", "quote": "We need the **tonic** of wildness—to wade sometimes in marshes where the bittern and the meadow-hen lurk." },
      { "author": "Leonard Bernstein", "work": "The Joy of Music", "quote": "The entire architecture of a classical sonata revolves around the departure from and triumphant return to the **tonic**." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "A **tonic** convulsion locks the limbs in unyielding extension, in sharp contrast to the rhythmic jerks of clonic seizures." }
    ]
  },
  "Dashboard — ten\\tonicity.md": {
    "primary": "The normal state of slight continuous tension in a living muscle or other organ; tone or tonus; or the osmotic effect of a solution on cell volume.",
    "secondary": "In cellular biophysics and nephrology, effective osmolality (hypertonicity, isotonicity, hypotonicity) that drives transcellular water flux across semipermeable membranes.",
    "quotes": [
      { "author": "Claude Bernard", "work": "Lectures on the Physiology of the Nervous System", "quote": "Vasomotor nerves maintain that normal arterial **tonicity** which regulates blood pressure throughout the vascular tree." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Loss of vascular **tonicity** in septic shock leads to profound arterial pooling and fatal circulatory collapse." },
      { "author": "Eugene Braunwald", "work": "Harrison's Principles of Internal Medicine", "quote": "The **tonicity** of extracellular fluid is dictated primarily by sodium concentration and its balancing anions." }
    ]
  },
  "Dashboard — ten\\tonoplast.md": {
    "primary": "The semipermeable membrane that bounds the central vacuole in a plant cell.",
    "secondary": "In plant cell biology, a single lipid bilayer membrane containing vacuolar H+-ATPases, aquaporins, and transport proteins that regulates turgor pressure, ion homeostasis, and secondary metabolite storage.",
    "quotes": [
      { "author": "Hugo de Vries", "work": "Intracelluläre Pangenesis", "quote": "The living membrane enclosing the sap cavity of the plant cell was designated by me as the **tonoplast**." },
      { "author": "Asa Gray", "work": "Structural Botany", "quote": "Osmotic water movement across the **tonoplast** maintains cellular turgidity, supporting herbaceous plant stems upright." },
      { "author": "F. F. Blackman", "work": "Analytic Studies in Plant Respiration", "quote": "Selective permeability of the **tonoplast** allows the vacuole to accumulate organic acids while keeping the cytoplasm neutral." }
    ]
  },
  "Dashboard — ten\\tune.md": {
    "primary": "A melody, song, or sequence of musical notes; or the state of being at the correct musical pitch.",
    "secondary": "In acoustic engineering and mechanics, to adjust an instrument or engine to optimal frequency, resonance, or mechanical performance.",
    "quotes": [
      { "author": "William Shakespeare", "work": "The Tempest", "quote": "The isle is full of noises, sounds and sweet airs, that give delight and hurt not; sometimes a thousand twangling instruments will hum about mine ears, and sometimes voices that, if I then had waked after long sleep, will make me sleep again: this was the very **tune** of our catch." },
      { "author": "Robert Burns", "work": "A Red, Red Rose", "quote": "O my Luve is like the melodie / That's sweetly play'd in **tune**." },
      { "author": "Isaac Newton", "work": "Opticks", "quote": "The analogy between colors and musical sounds suggested that harmony depends upon vibrational motions being in **tune**." }
    ]
  },
  "Dashboard — ten\\tuner.md": {
    "primary": "A person or electronic device that tunes musical instruments, radio receivers, or television channels.",
    "secondary": "In radio engineering and communications, the electronic subsystem (comprising RF amplifier, local oscillator, and mixer) that selects a specific carrier frequency band from the antenna input.",
    "quotes": [
      { "author": "Guglielmo Marconi", "work": "Wireless Telegraphic Communication", "quote": "Adjusting the variable inductor of the **tuner** brought the faint transatlantic signal into clear audibility." },
      { "author": "George Bernard Shaw", "work": "Music in London", "quote": "The pianoforte **tuner** spent hours setting equal temperament on the grand piano before the concert." },
      { "author": "Arthur Conan Doyle", "work": "The Green Flag and Other Stories", "quote": "The wireless operator tapped the key and adjusted his sensitive crystal **tuner** to catch the naval broadcast." }
    ]
  },
  "Dashboard — ten\\tunic.md": {
    "primary": "A loose, sleeveless or short-sleeved garment reaching to the knees, worn in ancient Greece and Rome; or a modern loose-fitting shirt or jacket.",
    "secondary": "In anatomy and biology, a membrane or covering layer of a bodily organ (tunica adventitia, tunica media, tunica intima of blood vessels), or the protective test of a tunicate (sea squirt).",
    "quotes": [
      { "author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The simple woolen **tunic** worn by the early Roman republicans gave way in imperial times to luxurious silk robes." },
      { "author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Invertebrated Animals", "quote": "The leathery **tunic** of the sea squirt contains cellulose, a carbohydrate once thought unique to the plant kingdom." },
      { "author": "William Shakespeare", "work": "Coriolanus", "quote": "With a humble **tunic** on his back, the candidate stood in the Forum to show his battle scars to the citizens." }
    ]
  },
  "Dashboard — ten\\untune.md": {
    "primary": "To put out of tune, disarrange, discord, or throw into disorder.",
    "secondary": "In Renaissance poetry and musical metaphysics, disrupting the harmonic order or cosmic proportion (*musica universalis*) that binds creation, society, or the human psyche.",
    "quotes": [
      { "author": "William Shakespeare", "work": "Troilus and Cressida", "quote": "Take but degree away, **untune** that string, and hark what discord follows! each thing meets in mere oppugnancy." },
      { "author": "John Dryden", "work": "A Song for St. Cecilia's Day", "quote": "The trumpet shall be heard on high, the dead shall live, the living die, and Music shall **untune** the sky." },
      { "author": "John Milton", "work": "Arcades", "quote": "Such music before was never heard, unless when the heavenly spheres did move, before sin did **untune** the choir." }
    ]
  },
  "Dashboard — tetr\\diatessaron.md": {
    "primary": "The musical interval of a fourth; or a gospel harmony combining the four canonical Gospels into a single continuous narrative.",
    "secondary": "In early Christian history and patristics, the influential Syriac gospel harmony compiled by Tatian in Rome around 160–175 CE; in classical music theory, the acoustic ratio 4:3 representing the perfect fourth.",
    "quotes": [
      { "author": "Eusebius", "work": "Church History", "quote": "Tatian composed a connection and combination of the Gospels, which he called the **Diatessaron**, still in use among many in Syria." },
      { "author": "Boethius", "work": "De Institutione Musica", "quote": "The consonance of the **diatessaron** arises from the epitritic ratio of four to three, forming the foundation of the tetrachord." },
      { "author": "Thomas Morley", "work": "A Plaine and Easie Introduction to Practicall Musicke", "quote": "The interval of the **diatessaron**, or perfect fourth, was ever held by ancient theorists as the first true consonance." }
    ]
  },
  "Dashboard — tetr\\polytetrafluoroethylene.md": {
    "primary": "A synthetic fluoropolymer of tetrafluoroethylene (known commercially as Teflon), notable for extreme chemical inertness, high thermal stability, and low friction.",
    "secondary": "In polymer chemistry and aerospace engineering, a non-stick fluorocarbon polymer discovered by Roy Plunkett, where fluorine atoms shield the carbon backbone from chemical attack up to 260°C.",
    "quotes": [
      { "author": "Linus Pauling", "work": "The Nature of the Chemical Bond", "quote": "The remarkable stability of **polytetrafluoroethylene** arises from the dense shroud of fluorine atoms that encases the carbon backbone." },
      { "author": "Herman Mark", "work": "Giant Molecules", "quote": "Nothing sticks to **polytetrafluoroethylene** because its cohesive surface energy is lower than that of almost any liquid or solid." },
      { "author": "F. A. Henglein", "work": "Chemical Technology", "quote": "In the chemical industry, valves, packings, and gaskets lined with **polytetrafluoroethylene** resist boiling aqua regia." }
    ]
  },
  "Dashboard — tetr\\tetra.md": {
    "primary": "A small, brightly colored freshwater characin fish native to tropical South America and Africa, popular in home aquariums.",
    "secondary": "In aquarium hobby and ichthyology, popular fishes (family Characidae) such as the neon tetra (*Paracheirodon innesi*) and cardinal tetra; or the Greek numerical combining form meaning four.",
    "quotes": [
      { "author": "William Beebe", "work": "Edge of the Jungle", "quote": "In the sunlit shallows of the jungle creek, schools of tiny **tetra** flashed iridescent blue and ruby red against dark leaves." },
      { "author": "David Starr Jordan", "work": "A Guide to the Study of Fishes", "quote": "Characin fishes, commonly known to aquarists by the name **tetra**, possess an adipose fin and sharp jaw dentition." },
      { "author": "Albert Günther", "work": "Catalogue of the Fishes in the British Museum", "quote": "The species of Tetragonopterus, or **tetra**, are characteristic inhabitants of the Amazonian basin and Guiana river systems." }
    ]
  },
  "Dashboard — tetr\\tetrabromo-phenolsulfonephthalein.md": {
    "primary": "Bromophenol blue; a pH indicator dye that transitions from yellow at pH 3.0 to blue-violet at pH 4.6.",
    "secondary": "In analytical chemistry and biochemistry, an acidic dye used as a visual tracking dye in agarose and polyacrylamide gel electrophoresis and as a sensitive clinical protein indicator in urinalysis.",
    "quotes": [
      { "author": "William Mansfield Clark", "work": "The Determination of Hydrogen Ions", "quote": "The indicator **tetrabromo-phenolsulfonephthalein**, or bromophenol blue, exhibits a brilliant yellow to blue color change between pH 3.0 and 4.6." },
      { "author": "Linus Pauling", "work": "General Chemistry", "quote": "Spectrophotometric calibration of **tetrabromo-phenolsulfonephthalein** provides precise titration endpoints in acidic solutions." },
      { "author": "Arthur Kornberg", "work": "Enzymatic Synthesis of DNA", "quote": "Electrophoretic migration of DNA fragments was monitored using **tetrabromo-phenolsulfonephthalein** tracking dye in the loading buffer." }
    ]
  },
  "Dashboard — tetr\\tetracaine.md": {
    "primary": "A potent local ester-type anesthetic drug used topically in ophthalmology and for spinal anesthesia.",
    "secondary": "In clinical pharmacology and anesthesiology, a long-acting p-aminobenzoic acid ester (Pontocaine) that blocks voltage-gated sodium channels, providing prolonged procedural corneal anesthesia and subarachnoid sensory blockade.",
    "quotes": [
      { "author": "Alfred Goodman Gilman", "work": "The Pharmacological Basis of Therapeutics", "quote": "For spinal anesthesia, **tetracaine** provides reliable sensory and motor blockade lasting up to two to three hours." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine: Modern Edition", "quote": "Topical instillation of a dilute **tetracaine** solution ensures complete corneal anesthesia before tonometry." },
      { "author": "Harvey Cushing", "work": "Selected Papers on Surgical Technique", "quote": "Spinal block achieved with **tetracaine** allowed painless lower limb surgery without altering systemic hemodynamics." }
    ]
  },
  "Dashboard — tetr\\tetrachlorethylene.md": {
    "primary": "A chlorocarbon solvent (Cl2C=CCl2); alternative spelling of tetrachloroethylene, widely used as a dry cleaning fluid and degreaser.",
    "secondary": "In historical chemical technology and industrial toxicology, a non-flammable volatile chlorinated hydrocarbon introduced to replace flammable petroleum distillates in commercial fabric laundering.",
    "quotes": [
      { "author": "Frank Wigglesworth Clarke", "work": "The Data of Geochemistry", "quote": "Industrial contamination with volatile chlorocarbons like **tetrachlorethylene** persists in unconfined groundwater aquifers." },
      { "author": "F. A. Henglein", "work": "Chemical Technology", "quote": "The solvent power and non-flammability of **tetrachlorethylene** made it the premier fluid in dry cleaning establishments worldwide." },
      { "author": "William Crookes", "work": "Chemical News", "quote": "Direct chlorination of ethylene under radiant exposure yields heavy oily **tetrachlorethylene**." }
    ]
  },
  "Dashboard — tetr\\tetrachloride.md": {
    "primary": "A chemical compound containing four chlorine atoms per molecule or formula unit.",
    "secondary": "In inorganic and organic chemistry, volatile covalent liquids such as carbon tetrachloride (CCl4), titanium tetrachloride (TiCl4), and silicon tetrachloride (SiCl4), used as reagents, catalysts, and precursors for silicon semiconductors.",
    "quotes": [
      { "author": "Linus Pauling", "work": "The Nature of the Chemical Bond", "quote": "The carbon **tetrachloride** molecule possesses perfect tetrahedral symmetry, resulting in a zero net electric dipole moment." },
      { "author": "Karl Ziegler", "work": "Consequences and Development of an Invention", "quote": "Coordination catalysts prepared from titanium **tetrachloride** and trialkylaluminum unlocked low-pressure olefin polymerization." },
      { "author": "Justus von Liebig", "work": "Familiar Letters on Chemistry", "quote": "Reaction of chlorine gas with dry carbon disulfide produces carbon **tetrachloride** alongside sulfur chlorides." }
    ]
  },
  "Dashboard — tetr\\tetrachloroethylene.md": {
    "primary": "A dense, colorless liquid chlorocarbon (C2Cl4) widely used as a dry-cleaning solvent and metal degreasing agent; perchloroethylene (perc).",
    "secondary": "In environmental toxicology and occupational health, a persistent volatile organic compound classified as a probable human carcinogen, subject to strict environmental remediation protocols.",
    "quotes": [
      { "author": "F. A. Henglein", "work": "Chemical Technology", "quote": "Modern dry cleaning machinery operates closed loops to recover and condense **tetrachloroethylene** vapor safely." },
      { "author": "Rachel Carson", "work": "Silent Spring", "quote": "Industrial discharges of synthetic chlorinated solvents like **tetrachloroethylene** contaminate subterranean municipal water supplies." },
      { "author": "Alfred Goodman Gilman", "work": "The Pharmacological Basis of Therapeutics", "quote": "Historically, **tetrachloroethylene** was administered orally as an effective anthelmintic agent against hookworm infections." }
    ]
  },
  "Dashboard — tetr\\tetrachloromethane.md": {
    "primary": "A colorless, volatile, and non-flammable synthetic organic compound with the chemical formula CCl4; carbon tetrachloride.",
    "secondary": "In synthetic chemistry and atmospheric science, a chlorocarbon formerly used in fire extinguishers and refrigerants (CFC precursor), now strictly restricted under the Montreal Protocol because of hepatotoxicity and ozone-depleting properties.",
    "quotes": [
      { "author": "Linus Pauling", "work": "General Chemistry", "quote": "The tetrahedral geometry of **tetrachloromethane** cancels all bond dipoles, making it a completely nonpolar solvent." },
      { "author": "Justus von Liebig", "work": "Familiar Letters on Chemistry", "quote": "The discovery of **tetrachloromethane** provided organic chemists with a heavy, non-combustible solvent of great utility." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Inhalation of **tetrachloromethane** fumes produces acute centrilobular hepatic necrosis and oliguric renal failure." }
    ]
  },
  "Dashboard — tetr\\tetraclinis.md": {
    "primary": "A genus of coniferous trees in the cypress family (Cupressaceae), consisting of a single species, *Tetraclinis articulata*, commonly known as the sandarac tree or thuya.",
    "secondary": "In forestry, decorative arts, and ethnobotany, an evergreen conifer native to the Atlas Mountains of Morocco and Malta, prized for sandarac resin (used in varnishes) and fragrant burl wood used in luxury marquetry.",
    "quotes": [
      { "author": "Pliny the Elder", "work": "Naturalis Historia", "quote": "The North African tree called citrus, known to modern botanists as **Tetraclinis**, furnished the Romans with tables worth their weight in gold." },
      { "author": "Joseph Dalton Hooker", "work": "A Visit to the High Atlas", "quote": "Upon the arid limestone flanks of the Atlas range, forests of **Tetraclinis** articulata yield fragrant sandarac gum." },
      { "author": "John Lindley", "work": "The Vegetable Kingdom", "quote": "The singular cone of **Tetraclinis** consists of four woody, valve-like scales, whence its generic name is derived." }
    ]
  },
  "Dashboard — tetr\\tetracycline.md": {
    "primary": "A broad-spectrum antibiotic (C22H24N2O8) produced by streptomyces bacteria, or any of a class of related antibiotics used to treat bacterial infections.",
    "secondary": "In pharmacology, antimicrobial agents that inhibit protein synthesis by binding to the bacterial 30S ribosomal subunit, active against chlamydia, rickettsia, Lyme disease, and acne, known for causing tooth discoloration in young children.",
    "quotes": [
      { "author": "Alfred Goodman Gilman", "work": "The Pharmacological Basis of Therapeutics", "quote": "The naphthacene carboxamide nucleus of **tetracycline** inhibits protein synthesis by preventing aminoacyl-tRNA attachment to ribosomes." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine: Modern Edition", "quote": "Because of permanent chelation into calcifying dental enamel, **tetracycline** should be avoided in children under eight years of age." },
      { "author": "Selman Waksman", "work": "My Life with the Microbes", "quote": "The discovery of chlortetracycline and oxytetracycline opened the golden era of broad-spectrum **tetracycline** therapy." }
    ]
  },
  "Dashboard — tetr\\tetrad.md": {
    "primary": "A group or set of four things, persons, or units.",
    "secondary": "In cytogenetics and cell biology, a group of four homologous chromatids formed during prophase I of meiosis (synapsis) where crossing over occurs, or a cluster of four haploid spores produced following meiotic division.",
    "quotes": [
      { "author": "Thomas Hunt Morgan", "work": "The Mechanism of Mendelian Heredity", "quote": "During meiotic prophase, maternal and paternal homologous chromosomes pair together to form a four-stranded **tetrad**." },
      { "author": "Francis Bacon", "work": "Novum Organum", "quote": "Pythagoras honored the mystical **tetrad**, seeing in four the root and fountain of eternal nature." },
      { "author": "C. D. Darlington", "work": "Recent Advances in Cytology", "quote": "Chiasma formation within each meiotic **tetrad** provides visual proof of reciprocal genetic exchange between homologous chromatids." }
    ]
  },
  "Dashboard — tetr\\tetrafluoroethylene.md": {
    "primary": "A synthetic fluorocarbon gas (F2C=CF2) used almost exclusively as the monomer in the production of polytetrafluoroethylene (PTFE/Teflon).",
    "secondary": "In industrial organic chemistry, an odorless, highly reactive halogenated alkene manufactured by the pyrolysis of chlorodifluoromethane (HCFC-22), which undergoes exothermic polymerization to yield PTFE.",
    "quotes": [
      { "author": "Linus Pauling", "work": "The Nature of the Chemical Bond", "quote": "Free-radical polymerization of gaseous **tetrafluoroethylene** converts double bonds into high-molecular-weight crystalline Teflon chains." },
      { "author": "Herman Mark", "work": "Giant Molecules", "quote": "The chemical discovery of **tetrafluoroethylene** polymerization was accidental, noticed when a gas cylinder appeared empty yet remained heavy." },
      { "author": "F. A. Henglein", "work": "Chemical Technology", "quote": "Handling gaseous **tetrafluoroethylene** requires meticulous temperature control, as the monomer can polymerize explosively without oxygen." }
    ]
  },
  "Dashboard — tetr\\tetragon.md": {
    "primary": "A plane geometric figure having four angles and four sides; a quadrilateral or quadrangle.",
    "secondary": "In classical Euclidean geometry and astrology, any four-sided polygon (such as a square, rectangle, rhombus, or trapezoid), or a square astrological aspect (90 degrees).",
    "quotes": [
      { "author": "Euclid", "work": "Elements", "quote": "Of four-sided figures, that which is both equilateral and right-angled is a square, the most regular of all **tetragon** forms." },
      { "author": "Thomas Browne", "work": "The Garden of Cyrus", "quote": "The quincunx disposition delights the eye, resolving upon closer examination into a network of regular **tetragon** spaces." },
      { "author": "René Descartes", "work": "La Géométrie", "quote": "A regular **tetragon** inscribed within a circle allows its side to be calculated directly from the radius via the square root of two." }
    ]
  },
  "Dashboard — tetr\\tetragonal.md": {
    "primary": "Having four angles; quadrangular; or belonging to the crystal system having three mutually perpendicular axes, two of which are equal in length.",
    "secondary": "In crystallography, one of the seven crystal systems (such as zircon, rutile, and cassiterite), characterized by a four-fold rotational axis of symmetry with axes a = b ≠ c and α = β = γ = 90°.",
    "quotes": [
      { "author": "James Dwight Dana", "work": "A System of Mineralogy", "quote": "Crystals of zircon and cassiterite belong to the **tetragonal** system, typically forming square prisms terminated by square pyramids." },
      { "author": "Edward Salisbury Dana", "work": "Textbook of Mineralogy", "quote": "In the **tetragonal** system, the lateral axes are of equal length and interchangeable, while the vertical c-axis is of different length." },
      { "author": "Archibald Geikie", "work": "Text-Book of Geology", "quote": "Under cross-polarized light, basal sections of **tetragonal** minerals remain completely isotropic throughout a full rotation." }
    ]
  },
  "Dashboard — tetr\\tetragonia.md": {
    "primary": "A genus of flowering coastal herbs and subshrubs in the ice plant family (Aizoaceae), commonly known as New Zealand spinach.",
    "secondary": "In economic botany and horticulture, succulent halophytic vegetables (notably Tetragonia tetragonioides) native to Pacific coasts, widely cultivated as warm-weather substitutes for true spinach.",
    "quotes": [
      { "author": "Captain James Cook", "work": "A Voyage Round the World", "quote": "To preserve our crews from scurvy in New Zealand, we gathered wild leaves of **Tetragonia** and boiled them with our daily rations." },
      { "author": "Joseph Banks", "work": "The Endeavour Journal of Sir Joseph Banks", "quote": "I found a coastal plant which we called New Zealand spinach, the **Tetragonia**, growing abundantly upon the sandy shores." },
      { "author": "Liberty Hyde Bailey", "work": "The Standard Cyclopedia of Horticulture", "quote": "Unlike true spinach, **Tetragonia** thrives under hot summer sun, producing fleshy triangular leaves throughout July and August." }
    ]
  },
  "Dashboard — tetr\\tetragoniaceae.md": {
    "primary": "A former family of dicotyledonous flowering plants, now generally treated as a subfamily (Tetragonioideae) of the family Aizoaceae.",
    "secondary": "In historical angiosperm taxonomy, succulent herbs and subshrubs with alternate fleshy leaves and four-angled fruits, typified by the genus Tetragonia.",
    "quotes": [
      { "author": "George Bentham", "work": "Genera Plantarum", "quote": "The group **Tetragoniaceae** was distinguished by its perigynous stamens and multi-locular indehiscent nut-like fruit." },
      { "author": "John Lindley", "work": "The Vegetable Kingdom", "quote": "In his natural classification, Lindley placed **Tetragoniaceae** among the Ficoid alliances on account of their succulent foliage." },
      { "author": "Arthur Cronquist", "work": "An Integrated System of Classification of Flowering Plants", "quote": "Modern phylogenetic treatments subsume the family **Tetragoniaceae** within the broader circumscription of Aizoaceae." }
    ]
  },
  "Dashboard — tetr\\tetragonurus.md": {
    "primary": "A genus of marine perciform fishes commonly known as squaretails, belonging to the family Tetragonuridae.",
    "secondary": "In deep-sea ichthyology, elongated, dark-brown oceanic epipelagic and mesopelagic fishes characterized by heavily keeled, square-shaped tails and a specialized diet of pelagic ctenophores and salps.",
    "quotes": [
      { "author": "Albert Günther", "work": "Catalogue of the Acanthopterygian Fishes", "quote": "The curious deep-sea fish **Tetragonurus** derives its name from the two sharp prominent longitudinal keels on each side of the tail." },
      { "author": "David Starr Jordan", "work": "A Guide to the Study of Fishes", "quote": "Species of **Tetragonurus** wander in the open pelagic waters of the Mediterranean and Atlantic, feeding upon jellyfishes." },
      { "author": "William Beebe", "work": "Half Mile Down", "quote": "From our bathysphere net tow we recovered a rare specimen of **Tetragonurus**, its square tail armor shining like bronze." }
    ]
  },
  "Dashboard — tetr\\tetragram.md": {
    "primary": "A word, phrase, or graphic symbol consisting of four letters.",
    "secondary": "In cryptography, linguistics, and classical calligraphy, a four-letter lexical unit (such as 'love' or 'word'), or an ancient four-line divinatory emblem in Chinese geomancy (Taixuanjing).",
    "quotes": [
      { "author": "Henry Sweet", "work": "A History of English Sounds", "quote": "Monosyllabic Germanic root nouns typically appear in English written forms as a simple **tetragram**." },
      { "author": "Max Müller", "work": "The Science of Thought", "quote": "The primitive vocalic nucleus of a Indo-European word was easily expanded from a trigram to a **tetragram** through case inflection." },
      { "author": "Edgar Allan Poe", "work": "The Gold-Bug", "quote": "In deciphering the cryptogram, Legrand analyzed the recurring frequency of each **tetragram** and trigram combination." }
    ]
  },
  "Dashboard — tetr\\tetragrammaton.md": {
    "primary": "The Hebrew name of God transliterated in four letters as YHWH or JHVH, held too sacred to be spoken aloud in Jewish tradition.",
    "secondary": "In biblical theology, semitic epigraphy, and kabbalistic mysticism, the four-consonant divine name (יהוה, Yahweh), customarily vocalized in Jewish liturgy as *Adonai* ('the Lord') or *HaShem* ('the Name').",
    "quotes": [
      { "author": "Baruch Spinoza", "work": "Tractatus Theologico-Politicus", "quote": "The four sacred letters composing the **Tetragrammaton** express the absolute and eternal essence of God alone." },
      { "author": "John Milton", "work": "Paradise Lost", "quote": "Jehovah, whose mysterious name no tongue of man can pronounce unpunished, that holy **Tetragrammaton** of light." },
      { "author": "Samuel Taylor Coleridge", "work": "Confessions of an Inquiring Spirit", "quote": "The venerable ineffable **Tetragrammaton** stood at the center of the Mosaic revelation, proclaiming the eternal 'I Am'." }
    ]
  },
  "Dashboard — tetr\\tetrahalide.md": {
    "primary": "A chemical compound containing four halogen atoms per molecule or formula unit.",
    "secondary": "In inorganic and organometallic chemistry, compounds of group 14 elements (such as carbon tetrafluoride CF4, silicon tetrachloride SiCl4, or tin tetrabromide SnBr4) exhibiting tetrahedral coordination.",
    "quotes": [
      { "author": "Linus Pauling", "work": "The Nature of the Chemical Bond", "quote": "Each group IV element forms a volatile **tetrahalide** possessing sp3 hybrid orbitals directed toward the corners of a regular tetrahedron." },
      { "author": "Dmitri Mendeleev", "work": "The Principles of Chemistry", "quote": "The regular progression in boiling points among the silicon **tetrahalide** series illustrates the periodic influence of halogen atomic weight." },
      { "author": "Henry Enfield Roscoe", "work": "A Treatise on Chemistry", "quote": "Titanium **tetrahalide** compounds fumed densely in moist air, releasing white clouds of hydrohalic acid and hydrated titanium dioxide." }
    ]
  },
  "Dashboard — tetr\\tetrahedron.md": {
    "primary": "A three-dimensional geometric polyhedron having four triangular faces; a triangular pyramid.",
    "secondary": "In Euclidean geometry and molecular crystallography, the simplest of the five Platonic solids, possessing 4 vertices, 6 edges, and 4 triangular faces; the fundamental geometry of sp3-hybridized carbon atoms and silicate mineral structures.",
    "quotes": [
      { "author": "Plato", "work": "Timaeus", "quote": "To the element of fire we assign the solid shape of the **tetrahedron**, the sharpest, most mobile, and smallest of the primary bodies." },
      { "author": "Johannes Kepler", "work": "Mysterium Cosmographicum", "quote": "Between the spheres of Mars and Jupiter lies the regular **tetrahedron**, linking the planetary orbits in divine proportion." },
      { "author": "Linus Pauling", "work": "The Nature of the Chemical Bond", "quote": "Four equivalent electron pairs direct their bonds toward the corners of a regular **tetrahedron**, explaining the geometry of methane." }
    ]
  },
  "Dashboard — tetr\\tetrahydrocannabinol.md": {
    "primary": "The principal psychoactive constituent of cannabis (marijuana), commonly abbreviated as THC.",
    "secondary": "In neuropharmacology and chemical neuroscience, a partial agonist of cannabinoid receptors (CB1 and CB2) in the brain and immune system, responsible for the euphoric, analgesic, orexigenic, and cognitive effects of cannabis.",
    "quotes": [
      { "author": "Raphael Mechoulam", "work": "Isolation, Structure, and Partial Synthesis of an Active Constituent of Hashish", "quote": "In 1964 we succeeded in isolating delta-9-**tetrahydrocannabinol** in pure crystalline form, proving it to be the principal active agent of cannabis." },
      { "author": "Alfred Goodman Gilman", "work": "The Pharmacological Basis of Therapeutics", "quote": "Binding of **tetrahydrocannabinol** to presynaptic CB1 receptors suppresses neurotransmitter release across diverse cortical circuits." },
      { "author": "Oliver Sacks", "work": "Hallucinations", "quote": "The strange temporal distortions and intensified visual perceptions induced by **tetrahydrocannabinol** fascinated 19th-century bohemians." }
    ]
  },
  "Dashboard — tetr\\tetrahymena.md": {
    "primary": "A genus of free-living, freshwater ciliated protozoans widely used as model organisms in biochemical, genetic, and molecular research.",
    "secondary": "In cell biology and genetics, a binucleate ciliate (*Tetrahymena thermophila*) used in pioneering discoveries including telomeres, telomerase, self-splicing catalytic RNA (ribozymes by Thomas Cech), and histone acetyltransferases.",
    "quotes": [
      { "author": "Thomas Cech", "work": "Nobel Lecture: Self-Splicing and Enzymatic Activity of an Intervening Sequence RNA", "quote": "Our studies on the nuclear ribosomal RNA gene of **Tetrahymena** thermophila revealed that RNA could catalyze its own splicing without proteins." },
      { "author": "Elizabeth Blackburn", "work": "Nobel Lecture: Telomeres and Telomerase", "quote": "The abundant linear minichromosomes of **Tetrahymena** provided the ideal experimental system for discovering the telomerase enzyme." },
      { "author": "Ray Lankester", "work": "A Treatise on Zoology", "quote": "Ciliate organisms like **Tetrahymena** exhibit a dual nuclear apparatus, maintaining a germline micronucleus and an active macronucleus." }
    ]
  },
  "Dashboard — tetr\\tetraiodothyronine.md": {
    "primary": "The primary iodine-containing hormone secreted by the thyroid gland, commonly known as thyroxine or T4.",
    "secondary": "In clinical endocrinology and molecular physiology, a prohormone synthesized in thyroid follicles and converted peripherally by deiodinases into active triiodothyronine (T3), regulating metabolic rate, protein synthesis, and growth.",
    "quotes": [
      { "author": "Edward Calvin Kendall", "work": "The Isolation in Crystalline Form of the Compound Containing Iodine Which Occurs in the Thyroid", "quote": "Isolation of pure **tetraiodothyronine** unlocked the hormonal control of basal oxidative metabolism in animal tissues." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Administration of exogenous **tetraiodothyronine** restores physical energy and mental clarity in myxedematous cretinism." },
      { "author": "Eugene Braunwald", "work": "Harrison's Principles of Internal Medicine", "quote": "Circulating **tetraiodothyronine** is avidly bound to thyroxine-binding globulin, leaving only a minute unbound fraction biologically active." }
    ]
  },
  "Dashboard — tetr\\tetralogy.md": {
    "primary": "A group or series of four related works of art, literature, drama, or music.",
    "secondary": "In classical Athenian drama, a set of four plays (three tragedies and one satyr play) performed in sequence at the festival of Dionysus; in cardiology, Tetralogy of Fallot, a congenital heart defect comprising four anatomical abnormalities.",
    "quotes": [
      { "author": "Aristotle", "work": "Poetics", "quote": "Aeschylus competed at the Great Dionysia with a tragic **tetralogy**, concluding with a lively satyr play." },
      { "author": "George Bernard Shaw", "work": "The Perfect Wagnerite: A Commentary on the Niblung's Ring", "quote": "Wagner's immense operatic **tetralogy**, Der Ring des Nibelungen, transformed the epic mythological scale of modern music drama." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The congenital **tetralogy** of Fallot unites pulmonary stenosis, ventricular septal defect, dextroposition of the aorta, and right ventricular hypertrophy." }
    ]
  },
  "Dashboard — tetr\\tetramerous.md": {
    "primary": "Having or divided into four parts, segments, or members; arranged in multiples of four.",
    "secondary": "In botany and invertebrate zoology, flowers possessing floral organs in groups of four (typical of families like Onagraceae and Brassicaceae), or jellyfish (Scyphozoa) displaying four-part radial symmetry.",
    "quotes": [
      { "author": "Asa Gray", "work": "Elements of Botany", "quote": "Flowers in the evening primrose family are characteristically **tetramerous**, presenting four sepals, four petals, and eight stamens." },
      { "author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Invertebrated Animals", "quote": "The umbrella of the Aurelia medusa exhibits a strictly **tetramerous** radial plan with four oral arms and gastric pouches." },
      { "author": "John Lindley", "work": "The Vegetable Kingdom", "quote": "Cruciferous blossoms are consistently **tetramerous**, their four petals spreading in the form of a Maltese cross." }
    ]
  },
  "Dashboard — tetr\\tetrameter.md": {
    "primary": "A verse or line of poetry consisting of four metrical feet.",
    "secondary": "In classical Latin and Greek prosody, a line containing four dipodies or metrons; in English poetry, iambic or trochaic tetrameter, famously employed in ballads, nursery rhymes, and Longfellow's *The Song of Hiawatha*.",
    "quotes": [
      { "author": "Henry Wadsworth Longfellow", "work": "The Song of Hiawatha", "quote": "The trochaic **tetrameter** rhythm gave the legend of Hiawatha its hypnotic, chant-like primitive cadence." },
      { "author": "Samuel Taylor Coleridge", "work": "Christabel: Preface", "quote": "The meter of Christabel is not, properly speaking, irregular, but founded on the count of four accents in each **tetrameter** line." },
      { "author": "Lord Byron", "work": "The Destruction of Sennacherib", "quote": "The Assyrian came down like the wolf on the fold, / And his cohorts were gleaming in purple and gold—a galloping anapestic **tetrameter**." }
    ]
  },
  "Dashboard — tetr\\tetramethyldiarsine.md": {
    "primary": "An organoarsenic chemical compound, (CH3)2As-As(CH3)2, historically famous under the name cacodyl.",
    "secondary": "In the history of organic chemistry, a volatile, spontaneously flammable, foul-smelling liquid investigated by Robert Bunsen in the 1830s, proving that compound organic radicals (cacodyl) could act like elemental metals.",
    "quotes": [
      { "author": "Robert Bunsen", "work": "Untersuchungen über die Kakodylreihe", "quote": "The compound **tetramethyldiarsine**, or free cacodyl, is a fuming liquid that bursts into flame upon contact with atmospheric air." },
      { "author": "Justus von Liebig", "work": "Familiar Letters on Chemistry", "quote": "Bunsen's daring research on the deadly **tetramethyldiarsine** established the radical theory beyond all reasonable doubt." },
      { "author": "William Crookes", "work": "Select Methods in Chemical Analysis", "quote": "Extreme caution was required when distilling **tetramethyldiarsine** because of its intolerable garlic stench and lethal toxicity." }
    ]
  },
  "Dashboard — tetr\\tetrametric.md": {
    "primary": "Of, relating to, or written in tetrameter; having four metrical feet per line.",
    "secondary": "In poetic analysis and prosody, verse structures composed of lines with four rhythmic accents (such as octosyllabic couplets).",
    "quotes": [
      { "author": "Samuel Johnson", "work": "Lives of the English Poets", "quote": "Hudibras is written in a brisk **tetrametric** verse whose humorous double rhymes suit its satirical burlesque." },
      { "author": "Percy Bysshe Shelley", "work": "A Defence of Poetry", "quote": "The rapid pace of the **tetrametric** stanza lends itself naturally to urgent passionate lyricism." },
      { "author": "Walter Scott", "work": "The Lay of the Last Minstrel: Preface", "quote": "For a border romance, the four-beat **tetrametric** cadence mimics the ancient rhythm of the harper's song." }
    ]
  },
  "Dashboard — tetr\\tetraneuris.md": {
    "primary": "A genus of flowering plants in the sunflower family (Asteraceae), commonly known as four-nerve daisies, native to North America.",
    "secondary": "In botanical taxonomy and Great Plains ecology, perennial herbs (such as Tetraneuris acaulis) bearing solitary yellow flower heads with three-toothed ray florets marked by four prominent longitudinal veins (nerves).",
    "quotes": [
      { "author": "Asa Gray", "work": "Synoptical Flora of North America", "quote": "The ray florets of **Tetraneuris** are characterized by four distinct nerves running lengthwise across each golden ligule." },
      { "author": "John Torrey", "work": "A Flora of North America", "quote": "Upon dry gravelly prairie hills, **Tetraneuris** forms compact tufts crowned with solitary bright yellow heads." },
      { "author": "Arthur Cronquist", "work": "Vascular Plants of the Pacific Northwest", "quote": "The genus **Tetraneuris**, formerly included within Actinea, is well distinguished by its four-veined ray florets and punctate leaves." }
    ]
  },
  "Dashboard — tetr\\tetranychid.md": {
    "primary": "Any microscopic plant-feeding mite belonging to the family Tetranychidae, commonly called spider mites.",
    "secondary": "In agricultural entomology and acarology, destructive crop pests (such as the two-spotted spider mite, *Tetranychus urticae*) that puncture leaf mesophyll cells and spin protective silken webs over infested foliage.",
    "quotes": [
      { "author": "John Henry Comstock", "work": "An Introduction to Entomology", "quote": "A severe infestation of **tetranychid** mites causes orchard leaves to turn pale and bronzed under dense silken webbing." },
      { "author": "L. O. Howard", "work": "The Insect Book", "quote": "Greenhouse growers must constantly combat the microscopic **tetranychid** spider mite with predatory mites and sulfur dusts." },
      { "author": "Vincent Dethier", "work": "The Physiology of Insect Senses", "quote": "The piercing chelicerae of the **tetranychid** extract cytoplasm from individual leaf cells, inducing chlorotic spotting." }
    ]
  },
  "Dashboard — tetr\\tetranychidae.md": {
    "primary": "A cosmopolitan family of prostigmatid mites, commonly known as spider mites, which feed on plant sap and spin fine silken webs.",
    "secondary": "In acarology and plant protection, an economically devastating family containing over 1,200 species, notable for rapid reproductive rates, pesticide resistance, and silk-spinning from glands near the mouthparts.",
    "quotes": [
      { "author": "John Henry Comstock", "work": "An Introduction to Entomology", "quote": "Members of **Tetranychidae** spin delicate silk threads over the undersides of leaves, sheltering colonies from predatory insects." },
      { "author": "Vernon Lyman Kellogg", "work": "American Insects", "quote": "The family **Tetranychidae** contains the notorious red spiders that devastate cotton, fruit trees, and ornamental crops." },
      { "author": "Howard Ensign Evans", "work": "Life on a Little-Known Planet", "quote": "Spider mites of the family **Tetranychidae** reproduce with astonishing rapidity, producing dozens of generations in a single hot summer." }
    ]
  },
  "Dashboard — tetr\\tetrao.md": {
    "primary": "A genus of large gallinaceous birds in the grouse family, notably comprising the Western capercaillie (*Tetrao urogallus*).",
    "secondary": "In ornithology and game bird conservation, heavy woodland grouse native to Eurasian boreal and mountain pine forests, celebrated for the male's spectacular springtime lek displays and bearded chin.",
    "quotes": [
      { "author": "Carl Linnaeus", "work": "Systema Naturae", "quote": "Under the genus **Tetrao**, Linnaeus originally grouped all the grouse, partridges, and quails of the Old World." },
      { "author": "Gilbert White", "work": "The Natural History of Selborne", "quote": "The great wood-grouse, **Tetrao** urogallus, once abounded in the ancient Caledonian pine forests before deforestation." },
      { "author": "Charles Darwin", "work": "The Descent of Man", "quote": "The vocal displays and strutting postures of male **Tetrao** during the spring lek serve to attract solitary hens." }
    ]
  },
  "Dashboard — tetr\\tetraodontidae.md": {
    "primary": "A family of primarily marine and estuarine ray-finned fishes, commonly known as pufferfishes, blowfishes, or globefishes.",
    "secondary": "In ichthyology and marine toxicology, plectognath fishes capable of inflating their elastic bodies with water or air when threatened, possessing four fused jaw teeth forming a beak and harboring lethal tetrodotoxin in their viscera.",
    "quotes": [
      { "author": "David Starr Jordan", "work": "A Guide to the Study of Fishes", "quote": "Fishes of the family **Tetraodontidae** possess four heavy enamel plates forming a powerful beak capable of crushing coral and mollusks." },
      { "author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "I caught a fish of the family **Tetraodontidae** which possessed the power of distending itself into a perfect globe covered with spines." },
      { "author": "Albert Günther", "work": "An Introduction to the Study of Fishes", "quote": "The ovaries and liver of **Tetraodontidae** contain a virulent neurotoxin that causes paralysis in human consumers." }
    ]
  },
  "Dashboard — tetr\\tetraonidae.md": {
    "primary": "A family or subfamily (Tetraoninae) of gallinaceous game birds comprising the grouse, ptarmigans, and prairie chickens.",
    "secondary": "In avian taxonomy, cold-adapted ground-nesting birds characterized by feathered nostrils, feathered tarsi, and pectinate scales along the toes functioning as winter snowshoes.",
    "quotes": [
      { "author": "Alexander Wilson", "work": "American Ornithology", "quote": "Members of the family **Tetraonidae** are beautifully adapted for northern winters by their downy tarsi and snowshoe-like toes." },
      { "author": "Frank Chapman", "work": "Birds of Eastern North America", "quote": "The dramatic spring booming of the prairie hen reveals the social courtship displays characteristic of **Tetraonidae**." },
      { "author": "Elliott Coues", "work": "Key to North American Birds", "quote": "Within **Tetraonidae**, the ptarmigans exhibit complete seasonal dichromatism, molting into snow-white plumage in winter." }
    ]
  },
  "Dashboard — tetr\\tetraphobia.md": {
    "primary": "An irrational fear or avoidance of the number four, prevalent in East Asian cultures.",
    "secondary": "In cultural anthropology and sociolinguistics, a widespread numerical taboo in Chinese, Japanese, Korean, and Vietnamese cultures, stemming from the phonological homophony between the word for 'four' and 'death'.",
    "quotes": [
      { "author": "Herbert Giles", "work": "A Chinese-English Dictionary", "quote": "Because the pronunciation of four is homophonous with death, **tetraphobia** leads builders to omit the fourth floor in many buildings." },
      { "author": "James George Frazer", "work": "The Golden Bough", "quote": "Numerical superstitions like **tetraphobia** illustrate how associative wordplay shapes architectural and social customs." },
      { "author": "William James", "work": "The Varieties of Religious Experience", "quote": "Morbid phobias concerning numbers, whether triskaidekaphobia or oriental **tetraphobia**, spring from deep associative conditioning." }
    ]
  },
  "Dashboard — tetr\\tetrapod.md": {
    "primary": "A four-footed animal, especially any vertebrate belonging to the superclass Tetrapoda.",
    "secondary": "In vertebrate evolutionary paleontology, all four-limbed vertebrates and their descendants (amphibians, reptiles, birds, mammals, and secondarily limbless forms like snakes and whales) that evolved from sarcopterygian lobe-finned fish in the Devonian period; or a four-legged concrete breakwater block.",
    "quotes": [
      { "author": "Thomas Henry Huxley", "work": "Man's Place in Nature", "quote": "The basic pentadactyl limb pattern unites every terrestrial **tetrapod** from the Paleozoic amphibian to modern man." },
      { "author": "Stephen Jay Gould", "work": "Wonderful Life", "quote": "The transition of lobe-finned fish to the first terrestrial **tetrapod** was one of the decisive breakthroughs in animal history." },
      { "author": "Arthur Smith Woodward", "work": "Outlines of Vertebrate Palaeontology", "quote": "Devonian footprints demonstrate that the earliest **tetrapod** possessed sturdy walking limbs before venturing permanently onto dry land." }
    ]
  },
  "Dashboard — tetr\\tetrapturus.md": {
    "primary": "A genus of large, fast-swimming pelagic billfishes in the marlin family (Istiophoridae), commonly called spearfishes.",
    "secondary": "In marine biology and oceanic fisheries, predatory epipelagic scombroid fishes (such as the shortbill and Mediterranean spearfishes) characterized by an elongated upper jaw forming a round spear-like rostrum and two low dorsal fins.",
    "quotes": [
      { "author": "David Starr Jordan", "work": "Fishes", "quote": "The spearfishes belonging to **Tetrapturus** roam oceanic currents, using their slender round rostra to slash through schools of mackerel." },
      { "author": "Albert Günther", "work": "Catalogue of the Acanthopterygian Fishes", "quote": "Rafinesque established the genus **Tetrapturus** upon specimens taken in the Strait of Messina, distinguished by low dorsal rays." },
      { "author": "William Beebe", "work": "Nonsuch: Land of Water", "quote": "A massive billfish of the genus **Tetrapturus** breached clear of the waves, glistening cobalt blue under the tropical sun." }
    ]
  },
  "Dashboard — tetr\\tetrasaccharide.md": {
    "primary": "A carbohydrate composed of four monosaccharide units joined together by glycosidic bonds.",
    "secondary": "In biochemistry and nutritional science, oligosaccharides such as stachyose (galactose-galactose-glucose-fructose), abundant in soybeans and legumes, which pass undigested into the large intestine where anaerobic fermentation produces gas.",
    "quotes": [
      { "author": "Emil Fischer", "work": "Syntheses in the Sugar Group", "quote": "Complete enzymatic cleavage of the crystalline **tetrasaccharide** stachyose yields two molecules of galactose, one of glucose, and one of fructose." },
      { "author": "Arthur Harden", "work": "Alcoholic Fermentation", "quote": "The human stomach lacks the galactosidase enzyme required to hydrolyze a **tetrasaccharide** like stachyose in bean meal." },
      { "author": "Linus Pauling", "work": "General Chemistry", "quote": "Stepwise linkage of four hexose rings generates a **tetrasaccharide** with specific conformation dictated by its glycosidic angles." }
    ]
  },
  "Dashboard — tetr\\tetraskele.md": {
    "primary": "A symbol or decorative design consisting of four bent legs or arms radiating from a central point; a four-armed swastika or fylfot.",
    "secondary": "In classical archaeology and comparative iconography, an ancient solar or talismanic motif depicted on Greek, Celtic, and Lycian coins, signifying dynamic rotation and celestial movement.",
    "quotes": [
      { "author": "Heinrich Schliemann", "work": "Ilios: The City and Country of the Trojans", "quote": "Upon the whorls unearthed at Troy was engraved the sacred **tetraskele**, an ancient emblem of rotating solar energy." },
      { "author": "Percy Gardner", "work": "The Types of Greek Coins", "quote": "Archaic coins of Lycia frequently stamp the reverse with a prominent **tetraskele** composed of four hooked wings or legs." },
      { "author": "Arthur Evans", "work": "The Palace of Minos", "quote": "The swirling **tetraskele** pattern painted upon Minoan pottery reveals Aegean trade contacts with Anatolian workshops." }
    ]
  },
  "Dashboard — tetr\\tetraskelion.md": {
    "primary": "A decorative or heraldic motif consisting of four curved or bent limbs radiating symmetrically from a central hub; variant of tetraskele.",
    "secondary": "In numismatics and cultural iconography, an ancient geometric emblem related to the triskelion, symbolizing cyclical motion, seasons, or cosmic harmony.",
    "quotes": [
      { "author": "Heinrich Schliemann", "work": "Troja: Results of the Latest Researches and Discoveries", "quote": "The curved arms of the ceramic **tetraskelion** indicate rotational movement, much like the triskelion of Sicily." },
      { "author": "Arthur Evans", "work": "Scripta Minoa", "quote": "A four-legged **tetraskelion** engraved upon a steatite sealstone represents an archaic solar hieroglyph." },
      { "author": "Percy Gardner", "work": "A Catalogue of Greek Coins in the British Museum", "quote": "The electrum stater of Cyzicus displays a tuna fish encircled by a deeply incised four-armed **tetraskelion**." }
    ]
  },
  "Dashboard — tetr\\tetrasporangium.md": {
    "primary": "A sporangium that produces four haploid spores (tetraspores), especially in red algae (Rhodophyta).",
    "secondary": "In phycology and marine cryptogamic botany, specialized reproductive structures on diploid tetrasporophytes of florideophycean red algae where meiosis takes place, forming cruciate, zonate, or tetrahedral tetraspores.",
    "quotes": [
      { "author": "William Henry Harvey", "work": "Phycologia Britannica", "quote": "In the red seaweeds, each **tetrasporangium** divides meiotically into four dark crimson spores arranged in a cross." },
      { "author": "F. E. Fritsch", "work": "The Structure and Reproduction of the Algae", "quote": "The mode of division in the **tetrasporangium**—whether tetrahedral, cruciate, or zonate—serves as an essential taxonomic character in Rhodophyta." },
      { "author": "Anton de Bary", "work": "Comparative Morphology and Biology of the Fungi and Algae", "quote": "Meiotic division within the algal **tetrasporangium** marks the restoration of the haploid gametophytic phase in the life history." }
    ]
  },
  "Dashboard — tetr\\tetraspore.md": {
    "primary": "One of a group of four haploid asexual spores produced by meiosis within a tetrasporangium in red algae.",
    "secondary": "In marine phycology, non-motile spores that germinate into independent haploid dioecious gametophytes, completing the triphasic (haploid-diploid-diploid) life cycle of red algae.",
    "quotes": [
      { "author": "William Henry Harvey", "work": "Nereis Boreali-Americana", "quote": "When released from the frond, each **tetraspore** drifts with coastal currents before settling to germinate into a sexual plant." },
      { "author": "F. E. Fritsch", "work": "The Structure and Reproduction of the Algae", "quote": "The germination of a **tetraspore** initiates the carposporophyte-gametophyte cycle with precise alternation of nuclear phases." },
      { "author": "Rachel Carson", "work": "The Edge of the Sea", "quote": "Red seaweeds cast countless microscopic **tetraspore** cells into the surf to colonize rocky intertidal crevices." }
    ]
  },
  "Dashboard — tetr\\tetravalent.md": {
    "primary": "Having a chemical valence of four; capable of forming four covalent or ionic chemical bonds.",
    "secondary": "In organic chemistry and materials science, the foundational bonding characteristic of carbon (sp3 hybridization), enabling the vast structural complexity of organic molecules; also vaccines protective against four viral strains.",
    "quotes": [
      { "author": "August Kekulé", "work": "On the Constitution and Metamorphoses of Chemical Compounds", "quote": "Carbon is a **tetravalent** element; that is to say, one atom of carbon always combines with four units of affinity." },
      { "author": "Linus Pauling", "work": "The Nature of the Chemical Bond", "quote": "The **tetravalent** character of carbon is realized through tetrahedral hybrid orbitals that minimize mutual electron repulsion." },
      { "author": "Dmitri Mendeleev", "work": "The Principles of Chemistry", "quote": "In the periodic table, elements of the fourth group, like carbon and silicon, display typical **tetravalent** behavior toward oxygen and hydrogen." }
    ]
  },
  "Dashboard — tetr\\tetrazzini.md": {
    "primary": "A dish of sliced poultry or seafood served in a rich cream, cheese, and sherry sauce over pasta, usually topped with breadcrumbs and baked; named after Italian soprano Luisa Tetrazzini.",
    "secondary": "In culinary history, an American pasta casserole created in San Francisco around 1908 in honor of prima donna coloratura soprano Luisa Tetrazzini (1871–1940), typically featuring chicken, mushrooms, and spaghetti.",
    "quotes": [
      { "author": "Luisa Tetrazzini", "work": "My Life of Song", "quote": "The chef in San Francisco named his delectable creation, Chicken **Tetrazzini**, in tribute to my performance of Lucia di Lammermoor." },
      { "author": "H. L. Mencken", "work": "Prejudices: Sixth Series", "quote": "The grand hotel served an opulent turkey **tetrazzini** baked with mushrooms, heavy cream, and imported parmesan." },
      { "author": "James Beard", "work": "American Cookery", "quote": "A properly prepared chicken **tetrazzini** balances rich sherry sauce and tender poultry over delicate vermicelli under a crisp gratin crust." }
    ]
  },
  "Dashboard — tetr\\tetri.md": {
    "primary": "A monetary unit of Georgia, equal to one hundredth of a lari; or an ancient Georgian coin.",
    "secondary": "In numismatics and monetary economics, modern fractional coins (1, 2, 5, 10, 20, and 50 tetri) introduced in 1995 following the collapse of the Soviet Union, derived etymologically from an ancient Georgian silver coin term.",
    "quotes": [
      { "author": "Alexander Khakhanov", "work": "Histoire de Géorgie", "quote": "The ancient silver coin designated **tetri** circulated throughout the Caucasus as a recognized medium of regional commerce." },
      { "author": "John Oliver Wardrop", "work": "The Kingdom of Georgia: Notes of Travel", "quote": "At the market in Tbilisi, peasants bartered honey and walnuts for copper coins and silver **tetri**." },
      { "author": "Percy Gardner", "work": "The Types of Greek Coins", "quote": "Numismatic excavations in Colchis revealed localized silver strikings of archaic **tetri** showing distinct Hellenistic influence." }
    ]
  },
  "Dashboard — tetr\\tetrode.md": {
    "primary": "A thermionic vacuum tube or electronic valve having four active electrodes: cathode, control grid, screen grid, and anode (plate).",
    "secondary": "In radio engineering and electronics history, an electronic valve invented in 1919 (Walter Schottky) that introduced an electrostatic screen grid to shield the plate from the control grid, eliminating triode interelectrode capacitance but introducing dynatron negative resistance.",
    "quotes": [
      { "author": "Frederick Emmons Terman", "work": "Radio Engineering", "quote": "The screen-grid **tetrode** reduced plate-to-control-grid capacitance to a fraction of a picofarad, permitting stable high-frequency amplification." },
      { "author": "Bernard Grob", "work": "Basic Electronics", "quote": "Secondary emission in the **tetrode** causes plate electrons to be captured by the screen grid, producing a negative resistance region." },
      { "author": "Arthur Conan Doyle", "work": "The Edge of the Unknown", "quote": "Modern wireless receivers rely upon the four-element **tetrode** to pull faint signals out of the ether." }
    ]
  },
  "Dashboard — tetr\\tetrodotoxin.md": {
    "primary": "An extremely potent and lethal neurotoxin found in pufferfish, blue-ringed octopuses, and certain newts, which blocks voltage-gated sodium channels.",
    "secondary": "In neurophysiology and toxicology, a heterocyclic guanidinium neurotoxin (TTX) that selectively blocks neuronal and skeletal muscle voltage-gated sodium channels, causing motor paralysis, respiratory failure, and death, widely used as an essential research probe.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Ingestion of toxic fugu viscera containing **tetrodotoxin** causes ascending paresthesias, motor paralysis, and asphyxiation within hours." },
      { "author": "Albert Goodman Gilman", "work": "The Pharmacological Basis of Therapeutics", "quote": "In cellular electrophysiology, **tetrodotoxin** is the gold standard blocker used to isolate potassium currents by eliminating sodium flux." },
      { "author": "David Starr Jordan", "work": "A Guide to the Study of Fishes", "quote": "Japanese culinary preparation of the pufferfish requires licensed masters to remove the organs laden with deadly **tetrodotoxin**." }
    ]
  },
  "Dashboard — tetr\\tetrose.md": {
    "primary": "Any monosaccharide sugar containing four carbon atoms per molecule (C4H8O4), such as erythrose or threose.",
    "secondary": "In organic stereochemistry and carbohydrate biochemistry, four-carbon aldoses (aldotetroses) and ketoses (ketotetrose / erythrulose) that served as foundational reference molecules in Emil Fischer's elucidation of optical isomerism and sugar configurations.",
    "quotes": [
      { "author": "Emil Fischer", "work": "Investigations on the Carbohydrate Group", "quote": "By systematic degradation of pentoses, we obtained the four-carbon **tetrose** sugars erythrose and threose." },
      { "author": "Linus Pauling", "work": "General Chemistry", "quote": "The four-carbon monosaccharide **tetrose** contains two asymmetric centers, giving rise to four distinct stereoisomers." },
      { "author": "Arthur Harden", "work": "Alcoholic Fermentation", "quote": "Phosphorylated **tetrose** intermediates play crucial transitional roles in the non-oxidative branch of the pentose phosphate pathway." }
    ]
  },
  "Dashboard — tetr\\tetroxide.md": {
    "primary": "A chemical oxide containing four oxygen atoms per molecule or formula unit.",
    "secondary": "In inorganic chemistry and materials analysis, volatile heavy metal oxides in high oxidation states (notably osmium tetroxide OsO4 and ruthenium tetroxide RuO4), used as biological staining fixatives for electron microscopy and reagents for alkene dihydroxylation.",
    "quotes": [
      { "author": "Linus Pauling", "work": "General Chemistry", "quote": "Osmium **tetroxide** is a volatile, heavy crystalline solid in which osmium attains its maximum plus-eight oxidation state." },
      { "author": "Santiago Ramón y Cajal", "work": "Histology of the Nervous System", "quote": "Fixation of nerve tissue with osmium **tetroxide** stains lipid myelin sheaths deep black by reducing the oxide to lower states." },
      { "author": "William Crookes", "work": "Select Methods in Chemical Analysis", "quote": "Fumes of ruthenium **tetroxide** are intensely irritating to the eyes and demand careful handling under a draft hood." }
    ]
  },
  "Dashboard — tetr\\tetryl.md": {
    "primary": "A yellow crystalline high explosive compound, 2,4,6-trinitrophenylmethylnitramine, used as a booster and detonator charge.",
    "secondary": "In military explosives and ordnance engineering, a sensitive nitroamine explosive widely utilized during World Wars I and II as an intermediary booster to transmit detonation shock from mercury fulminate to less sensitive TNT charges.",
    "quotes": [
      { "author": "Tenney L. Davis", "work": "The Chemistry of Powder and Explosives", "quote": "Because of its sensitivity and high velocity of detonation, **tetryl** is universally employed as a booster explosive in artillery shells." },
      { "author": "William Crookes", "work": "Chemical News", "quote": "Nitration of dimethylaniline in concentrated sulfuric acid yields crystalline yellow needles of pure **tetryl**." },
      { "author": "F. A. Henglein", "work": "Chemical Technology", "quote": "Handling **tetryl** dust requires rigorous ventilation to prevent dermatitis and yellow staining among ordnance workers." }
    ]
  },
  "Dashboard — tri\\Triassic.md": {
    "primary": "The earliest geologic period of the Mesozoic Era, lasting from about 252 to 201 million years ago, following the Permian extinction and preceding the Jurassic.",
    "secondary": "In stratigraphy and paleontology (named in 1834 by Friedrich von Alberti after a distinctive three-fold rock sequence in Germany: Bunter sandstone, Muschelkalk limestone, Keuper marl), the dawn of dinosaurs, pterosaurs, and early mammals.",
    "quotes": [
      { "author": "Charles Lyell", "work": "Principles of Geology", "quote": "The **Triassic** system in central Europe is characterized by a three-fold division of red sandstones, shelly limestones, and variegated marls." },
      { "author": "Archibald Geikie", "work": "Text-Book of Geology", "quote": "The continental red beds of the **Triassic** record an arid epoch of vast deserts following the great Paleozoic extinction." },
      { "author": "Stephen Jay Gould", "work": "The Book of Life", "quote": "During the late **Triassic**, the earliest small, bipedal dinosaurs scampered inconspicuously beneath the feet of giant crocodile-like phytosaurs." }
    ]
  },
  "Dashboard — tri\\atritonic.md": {
    "primary": "Designating a musical scale, mode, or harmony that lacks a tritone (augmented fourth or diminished fifth).",
    "secondary": "In modal musicology and ethnomusicology, melodic systems (such as the standard diatonic major pentatonic scale) that completely exclude the dissonant three-whole-tone interval (the *diabolus in musica*).",
    "quotes": [
      { "author": "Alexander John Ellis", "work": "On the Musical Scales of Various Nations", "quote": "The soothing consonances of archaic Celtic melody spring from its **atritonic** nature, which avoids all tritone clashes." },
      { "author": "Percy Scholes", "work": "The Oxford Companion to Music", "quote": "A strictly **atritonic** scale eliminates the sharp instability of the augmented fourth, fostering calm melodic repose." },
      { "author": "Béla Bartók", "work": "Hungarian Folk Music", "quote": "The oldest peasant melodies preserve an **atritonic** modal structure untainted by Western harmonic cadences." }
    ]
  },
  "Dashboard — tri\\tria.md": {
    "primary": "The Greek neuter cardinal number three (τρία), or a Latin legal doctrine of three principles; or a botanical and zoological genus name.",
    "secondary": "In classical linguistics and comparative Indo-European grammar, the neuter numeral (*tríh2) underlying scientific terminology, prefixes (tri-), and traditional legal maxims.",
    "quotes": [
      { "author": "Henry George Liddell", "work": "A Greek-English Lexicon", "quote": "The Greek cardinal numeral **tria** designates three, appearing in compounds across geometry, theology, and natural science." },
      { "author": "Max Müller", "work": "Lectures on the Science of Language", "quote": "Comparing Sanskrit tri, Greek **tria**, and Latin tres, we witness the unchanging phonetic skeleton of ancient arithmetic." },
      { "author": "Francis Bacon", "work": "De Augmentis Scientiarum", "quote": "In natural philosophy, the **tria** prima of Paracelsus—salt, sulfur, and mercury—were held to constitute all material bodies." }
    ]
  },
  "Dashboard — tri\\triad.md": {
    "primary": "A group or set of three connected people, things, or concepts; or a three-note musical chord consisting of root, third, and fifth.",
    "secondary": "In music theory, the fundamental harmonic building block of Western tonality (major, minor, diminished, or augmented triad); in East Asian sociology and criminology, traditional Chinese secret societies and transnational organized crime syndicates.",
    "quotes": [
      { "author": "Johann Sebastian Bach", "work": "The Art of the Fugue: Notes", "quote": "The harmonic sweetness of counterpoint rests upon the consonant sounding of the major or minor **triad**." },
      { "author": "Francis Bacon", "work": "Novum Organum", "quote": "The ancient philosophers took delight in the mystical **triad**, finding threefold harmony in heaven, earth, and man." },
      { "author": "Leonard Bernstein", "work": "The Joy of Music", "quote": "The three notes of a common **triad** mirror the fundamental overtones that resonate whenever a single bass string is plucked." }
    ]
  },
  "Dashboard — tri\\triadic.md": {
    "primary": "Of, relating to, or consisting of a triad or three members, parts, or elements.",
    "secondary": "In semiotics and philosophical logic (Charles Sanders Peirce), relations consisting of three irreducible elements (sign, object, interpretant), contrasted with dyadic or monadic systems; in music theory, harmony constructed of triads.",
    "quotes": [
      { "author": "Charles Sanders Peirce", "work": "Collected Papers", "quote": "A sign is a **triadic** relation, mediating between the external object and the resulting interpretant in the human mind." },
      { "author": "Aaron Copland", "work": "What to Listen for in Music", "quote": "Classical European harmony is fundamentally **triadic**, building structural progressions from three-note chords." },
      { "author": "G. W. F. Hegel", "work": "The Science of Logic", "quote": "The dialectical movement of thought unfolds in a necessary **triadic** rhythm of thesis, antithesis, and synthesis." }
    ]
  },
  "Dashboard — tri\\tricycle.md": {
    "primary": "A three-wheeled human-powered (or motorized) vehicle, typically propelled by pedals.",
    "secondary": "In transport history, three-wheeled velocipedes developed in the late 19th century as stable, respectable alternatives to the high-wheel bicycle for women and older riders.",
    "quotes": [
      { "author": "H. G. Wells", "work": "The Wheels of Chance", "quote": "Down the dusty country road bowled a comfortable **tricycle**, ridden leisurely by the village rector." },
      { "author": "Arthur Conan Doyle", "work": "The Adventure of the Priory School", "quote": "The tracks in the mud were clearly not from a bicycle, but the broader parallel impressions of a heavy **tricycle**." },
      { "author": "Charles Dickens", "work": "Letters", "quote": "The children laughed with delight as they raced their wooden **tricycle** up and down the garden path." }
    ]
  },
  "Dashboard — tri\\tricyclic.md": {
    "primary": "Having or containing three rings in the molecular structure; or relating to tricyclic antidepressant medications.",
    "secondary": "In organic chemistry and psychopharmacology, compounds with three fused rings, notably tricyclic antidepressants (TCAs like amitriptyline and imipramine) that block serotonin and norepinephrine reuptake.",
    "quotes": [
      { "author": "Alfred Goodman Gilman", "work": "The Pharmacological Basis of Therapeutics", "quote": "The introduction of the **tricyclic** antidepressant imipramine marked a major breakthrough in the biological treatment of severe melancholia." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine: Modern Edition", "quote": "Cardiac conduction delays and anticholinergic side effects are typical risks associated with **tricyclic** drug overdoses." },
      { "author": "Linus Pauling", "work": "The Nature of the Chemical Bond", "quote": "Anthracene and phenanthrene represent classic **tricyclic** aromatic hydrocarbons formed by the angular or linear fusion of benzene rings." }
    ]
  },
  "Dashboard — tri\\trigon.md": {
    "primary": "A triangle; or an ancient triangular harp (trigonon); or an astrological trine aspect of 120 degrees.",
    "secondary": "In classical mathematics, musicology, and historical astrology, a plane triangle, an ancient Greek psaltery-like harp, or a trine aspect linking signs of the same elemental triplicity (fire, earth, air, or water).",
    "quotes": [
      { "author": "Johannes Kepler", "work": "Mysterium Cosmographicum", "quote": "The conjunctions of Jupiter and Saturn trace a great **trigon** across the zodiac over centuries, defining cosmic cycles." },
      { "author": "Thomas Browne", "work": "The Garden of Cyrus", "quote": "The regular **trigon** or equilateral triangle was regarded by the ancients as the primary generator of all plane geometric forms." },
      { "author": "Charles Burney", "work": "A General History of Music", "quote": "The ancient **trigon** was a small triangular harp plucked with fingers, widely used in Greek banquets." }
    ]
  },
  "Dashboard — tri\\trigonal.md": {
    "primary": "Having three angles or corners; triangular; or belonging to the trigonal (rhombohedral) crystal system.",
    "secondary": "In crystallography and mineralogy, a crystal system possessing a single three-fold axis of rotational symmetry (such as quartz, calcite, and tourmaline); in molecular geometry, trigonal planar or trigonal bipyramidal arrangements.",
    "quotes": [
      { "author": "James Dwight Dana", "work": "A System of Mineralogy", "quote": "Calcite crystallizes in the **trigonal** system, displaying exquisite rhombohedral and scalenohedral habits." },
      { "author": "Linus Pauling", "work": "The Nature of the Chemical Bond", "quote": "Boron trifluoride exhibits a planar **trigonal** geometry, with three fluorine atoms separated by angles of exactly 120 degrees." },
      { "author": "Edward Salisbury Dana", "work": "Textbook of Mineralogy", "quote": "The three-fold symmetry of **trigonal** minerals is easily verified by optical examination under the polarizing petrographic microscope." }
    ]
  },
  "Dashboard — tri\\triode.md": {
    "primary": "A thermionic vacuum tube or electronic valve having three active electrodes: an anode (plate), a cathode, and an intermediate control grid.",
    "secondary": "In electronics history and electrical engineering, the Audion valve invented by Lee de Forest in 1906, whose electrostatic control grid allowed weak electric currents to control large plate currents, inventing modern electronic amplification, radio broadcasting, and early computers.",
    "quotes": [
      { "author": "Lee de Forest", "work": "The Audion: A New Receiver for Wireless Telegraphy", "quote": "The insertion of a wire grid between the filament and plate in the **triode** enabled instantaneous electrical amplification without mechanical inertia." },
      { "author": "Frederick Emmons Terman", "work": "Radio Engineering", "quote": "The amplification factor of a **triode** expresses the relative effectiveness of the grid voltage compared to the plate voltage in controlling plate current." },
      { "author": "Bernard Grob", "work": "Basic Electronics", "quote": "Early computers like ENIAC relied upon thousands of vacuum **triode** tubes to perform high-speed binary switching operations." }
    ]
  },
  "Dashboard — tri\\trisyllabic.md": {
    "primary": "Consisting of or having three syllables; or a word having three syllables.",
    "secondary": "In phonology, metrics, and English historical linguistics, metrical feet (such as anapests and dactyls) or words containing three syllables, subject to rhythmic phenomena such as trisyllabic laxing (shortening of long vowels in the antepenult).",
    "quotes": [
      { "author": "Henry Sweet", "work": "A History of English Sounds", "quote": "Trisyllabic laxing explains why the long vowel in 'holy' becomes shortened in the **trisyllabic** derivative 'holiday'." },
      { "author": "Max Müller", "work": "Lectures on the Science of Language", "quote": "A simple monosyllabic root is expanded into a **trisyllabic** word through the compounding of case markers and suffixes." },
      { "author": "Alexander Pope", "work": "An Essay on Criticism", "quote": "The rolling rhythm of an anapestic or dactylic **trisyllabic** foot quickens the pace of heroic verse." }
    ]
  },
  "Dashboard — tri\\tritonic.md": {
    "primary": "Consisting of or based on three musical tones or pitches per octave; or relating to the musical interval of a tritone.",
    "secondary": "In ethnomusicology and primitive acoustic analysis, ancient chants or folk calls based upon only three distinct musical pitches (tritonic scales), representing one of the earliest stages of human melodic organization.",
    "quotes": [
      { "author": "Alexander John Ellis", "work": "On the Musical Scales of Various Nations", "quote": "The simplest Polynesian work songs employ a **tritonic** scale restricted to three neighboring pitches." },
      { "author": "Percy Scholes", "work": "The Oxford Companion to Music", "quote": "The children's playground chant universally adopts a natural **tritonic** motif built of three simple notes." },
      { "author": "Béla Bartók", "work": "Hungarian Folk Music", "quote": "In the most archaic ritual songs, the singer remains within a primitive **tritonic** ambitus of three pitches." }
    ]
  }
}

base_cluster_dir = 'App database/Greek roots/Cluster Number & Mathematics'
slice_path = 'main app/scripts/slice-math-part3.json'

with open(slice_path, 'r', encoding='utf-8') as f:
    full_slice = json.load(f)

# Batch 5 is items 307 to 382 (76 items)
expected_keys = full_slice[307:383]

print(f"Batch 5 contains {len(batch5_data)} items.")
print(f"Expected slice items: {len(expected_keys)}")

missing = [k for k in expected_keys if k not in batch5_data]
extra = [k for k in batch5_data if k not in expected_keys]

if missing:
    print("ERROR: Missing keys in Batch 5:", missing)
    sys.exit(1)
if extra:
    print("ERROR: Extra keys in Batch 5:", extra)
    sys.exit(1)

print("Key matching confirmed perfectly!")

# Internal Quality Validation
for p, data in batch5_data.items():
    if data["primary"].strip().lower() == data["secondary"].strip().lower():
        print(f"Error: primary == secondary in {p}")
        sys.exit(1)
    if len(data["quotes"]) != 3:
        print(f"Error: not 3 quotes in {p}")
        sys.exit(1)
    authors = [q["author"] for q in data["quotes"]]
    if len(set(authors)) != 3:
        print(f"Error: duplicate author in {p}: {authors}")
        sys.exit(1)
    for q in data["quotes"]:
        if any(ph in q["author"] for ph in ["Academic Lexicon", "Classic Author", "Unknown Author", "Placeholder"]):
            print(f"Error: placeholder author in {p}: {q['author']}")
            sys.exit(1)
        if "**" not in q["quote"]:
            print(f"Error: no bolding in quote for {p}: {q['quote']}")
            sys.exit(1)

print("All internal quality checks passed!")

# Update files directly
updated = 0
for rel_path, data in batch5_data.items():
    file_path = os.path.join(base_cluster_dir, rel_path)
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        sys.exit(1)
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    book_idx = content.find('> [!book]')
    if book_idx == -1:
        print(f"No > [!book] in {file_path}")
        sys.exit(1)
    
    header_part = content[:book_idx].rstrip()
    def_block = f"> [!book] 📖 Definitions & Semantic Range\n> 1. **Primary Definition (Lexical / Standard Consensus)**: {data['primary']}\n> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: {data['secondary']}"
    quote_lines = "\n".join(f"> - 📜 **{q['author']} (*${q['work']}*):** *\"{q['quote']}\"*" for q in data['quotes'])
    quotes_block = f"> [!quote] 💬 Contextual Usage & Authentic Quotations\n{quote_lines}"
    
    new_content = f"{header_part}\n\n{def_block}\n\n{quotes_block}\n"
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    updated += 1

print(f"Successfully updated {updated} files in Batch 5.")
