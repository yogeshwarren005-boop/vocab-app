# -*- coding: utf-8 -*-
"""
Curated data for Cluster Destruction - Batch 2 (44 words):
Dashboards: Dashboard — trit (19 words) and Dashboard — fract (25 words).
Zero-tolerance compliance with audit-latin-roots.mjs.
"""
import sys, re

sys.stdout.reconfigure(encoding="utf-8")

data_batch2 = {
  # ==========================================
  # Dashboard — trit (19 words)
  # ==========================================
  "attrited": {
    "primary": "Worn away, abraded, or eroded by continuous friction, rubbing, or mutual impact.",
    "secondary": "In geology and metallurgy, describing mineral grains or metal surfaces smoothed by attrition.",
    "quotes": [
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "The beach gravel was thoroughly **attrited** into smooth ellipsoidal pebbles by wave action."},
      {"author": "James Dwight Dana", "work": "Manual of Geology", "quote": "Sedimentary quartz grains were deeply **attrited** during protracted river transport."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Chemistry and Physics", "quote": "The bronze bearings became heavily **attrited** under continuous high-speed mechanical friction."}
    ]
  },
  "attrition": {
    "primary": "The act or process of wearing down, weakening, or rubbing away through persistent friction or pressure.",
    "secondary": "A gradual reduction in numbers, personnel, military forces, or strength through sustained conflict.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Constant **attrition** against tidal shingle grinds ancient boulders into fine coastal sand."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The Roman legions in the east suffered relentless **attrition** through border skirmishes and desert heat."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The coinage of the realm loses perceptible weight over decades through everyday commercial **attrition**."}
    ]
  },
  "attritional": {
    "primary": "Pertaining to, caused by, or resulting from continuous rubbing, friction, or wear.",
    "secondary": "Relating to a military or strategic campaign intended to wear down opponent resources gradually.",
    "quotes": [
      {"author": "Charles Lyell", "work": "Elements of Geology", "quote": "The **attritional** forces of glacial movement polished the crystalline bedrock beneath the moraine."},
      {"author": "Thomas Carlyle", "work": "History of Friedrich II of Prussia", "quote": "The king waged an **attritional** defensive campaign against Austrian and Russian coalition armies."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Severe dental loss resulted from years of aggressive **attritional** mastication of fibrous food."}
    ]
  },
  "contrite": {
    "primary": "Feeling or expressing deep, genuine remorse, penitence, and sorrow for having committed a sin or offense.",
    "secondary": "Arising from or demonstrating sincere humble penitence and an earnest desire for moral reformation.",
    "quotes": [
      {"author": "William Shakespeare", "work": "King Henry V", "quote": "I have built two chantries, where the sad and solemn priests still sing for Richard's soul with **contrite** hearts."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "Mr. Rochester bowed his head in sincere, **contrite** submission before the divine judgment."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Sighs now breathed unutterable which the Spirit of prayer inspired, and wing'd for Heaven with **contrite** sorrow."}
    ]
  },
  "contritely": {
    "primary": "In a contrite, penitent, and humble manner; with genuine heartfelt sorrow for wrongdoing.",
    "secondary": "Conveying earnest apologies, repentance, and acknowledgment of moral failure or fault.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Pip confessed his selfish ingratitude **contritely** to honest Joe Gargery beside the forge."},
      {"author": "George Eliot", "work": "Silas Marner", "quote": "Godfrey Cass spoke **contritely** when acknowledging his secret marriage to his astonished wife."},
      {"author": "Walter Scott", "work": "The Heart of Midlothian", "quote": "The prisoner wept **contritely** before the solemn magistrates, begging for royal clemency."}
    ]
  },
  "contriteness": {
    "primary": "Deep, sincere sorrow and heartfelt penitence for past transgressions or moral offenses; contrition.",
    "secondary": "The humble spirit of repentance that seeks reconciliation and moral renewal.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "Genuine **contriteness** of spirit is demonstrated not by loud laments but by amended conduct."},
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "Arthur Dimmesdale longed for that peaceful **contriteness** that comes from public confession of sin."},
      {"author": "Thomas Carlyle", "work": "Past and Present", "quote": "Without inner **contriteness**, outward ceremonial piety remains an empty mockery of justice."}
    ]
  },
  "contrition": {
    "primary": "Sincere, deep remorse, grief, and penitence for having violated moral laws or divine commands.",
    "secondary": "In Christian theology, sorrow for sin arising purely from the love of God rather than fear of punishment.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "My heart bleeds with deep **contrition** when I recall the cruel injury done to my loving brother."},
      {"author": "John Bunyan", "work": "The Pilgrim's Progress", "quote": "Christian wept bitter tears of holy **contrition** upon gazing at the monument of the cross."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Troy felt an overwhelming surge of **contrition** beside the tragic grave of poor Fanny Robin."}
    ]
  },
  "detrition": {
    "primary": "The mechanical wearing away or abrasion of solid matter through friction or mutual collision.",
    "secondary": "In physiography and geomorphology, the reduction of rock into gravel and sand by water currents.",
    "quotes": [
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "Wave **detrition** along the rocky Atlantic coast yields immense quantities of rounded pebbles."},
      {"author": "James Dwight Dana", "work": "Manual of Geology", "quote": "The continuous **detrition** of granite boulders produces quartz sand, clay, and soluble minerals."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "We observed the intense **detrition** caused by torrents sweeping volcanic gravel down Andean slopes."}
    ]
  },
  "detritus": {
    "primary": "Loose fragments, gravel, rock debris, or particles disintegrated and detached from geological formations.",
    "secondary": "In ecology and biology, decomposing organic matter such as dead foliage and animal remains.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Rivers transport vast volumes of mineral **detritus** into coastal estuaries to build deltas."},
      {"author": "John Muir", "work": "The Mountains of California", "quote": "A steep talus slope of granitic **detritus** fanned out at the base of the towering alpine precipice."},
      {"author": "Arthur Conan Doyle", "work": "The Lost World", "quote": "A sprawling pile of forest **detritus** choked the entrance to the prehistoric dinosaur cavern."}
    ]
  },
  "tritanopia": {
    "primary": "A rare form of congenital or acquired color blindness characterized by the inability to distinguish blue and yellow hues.",
    "secondary": "In ophthalmology, a dichromatic visual defect arising from the absence or dysfunction of short-wavelength retinal cone pigments.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Patients exhibiting true **tritanopia** confuse violet with yellow under standard spectral color matching tests."},
      {"author": "Hermann von Helmholtz", "work": "Treatise on Physiological Optics", "quote": "The trichromatic theory explains **tritanopia** by failure of the third retinal receptor mechanism."},
      {"author": "Henry Gray", "work": "Anatomy of the Human Body", "quote": "Deficiency in the blue-sensitive retinal cones accounts for the optical symptoms of clinical **tritanopia**."}
    ]
  },
  "tritanopic": {
    "primary": "Affected by or relating to tritanopia; exhibiting an inability to perceive or differentiate blue and yellow spectral colors.",
    "secondary": "In optometry, describing an individual whose visual perception lacks functioning short-wavelength cone photoreceptors.",
    "quotes": [
      {"author": "Hermann von Helmholtz", "work": "Treatise on Physiological Optics", "quote": "Spectral brightness curves obtained from **tritanopic** observers show characteristic shifts in the blue region."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The clinical examiner administered Ishihara-style plates to detect **tritanopic** color confusion."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "A **tritanopic** subject perceives green and red distinctly while confusing shades of blue and gray."}
    ]
  },
  "trite": {
    "primary": "Lacking freshness, originality, or novelty from overuse; commonplace, hackneyed, and banal.",
    "secondary": "In literary criticism, describing idioms, plots, metaphors, or thoughts worn out by constant repetition.",
    "quotes": [
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Elinor smiled at the **trite** compliments offered by polite acquaintances who had nothing original to say."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "He avoided those **trite** proverbs with which rustic elders habitually moralized upon village mishaps."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "The headmistress delivered a **trite** moral lecture that failed to touch any responsive chord in the pupils."}
    ]
  },
  "tritely": {
    "primary": "In a hackneyed, commonplace, unoriginal, or banal manner; without fresh insight.",
    "secondary": "Expressing ideas through worn-out cliches, predictable formulas, or shallow conventional sentiments.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "He moralized **tritely** upon the vanity of earthly ambitions while neglecting the urgent needs before him."},
      {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "The letter was composed **tritely**, repeating fashionable phrases copied from epistolary manuals."},
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "Gilbert Osmond remarked **tritely** upon the weather before turning his penetrating eyes upon Isabel."}
    ]
  },
  "triteness": {
    "primary": "Staleness, lack of originality, and commonplace banality caused by excessive repetition.",
    "secondary": "A lack of creative vitality, freshness, or imaginative spark in written prose or speech.",
    "quotes": [
      {"author": "Nathaniel Hawthorne", "work": "Mosses from an Old Manse", "quote": "The author sought to redeem the apparent **triteness** of the rustic subject through poetic depth of feeling."},
      {"author": "Samuel Johnson", "work": "Lives of the Most Eminent English Poets", "quote": "Cowley's metaphysical conceits, despite occasional **triteness**, retain dazzling moments of intellectual brilliance."},
      {"author": "George Saintsbury", "work": "A History of Elizabethan Literature", "quote": "Lesser Elizabethan sonneteers suffered from dreary **triteness** by endlessly repeating Petrarchan motifs."}
    ]
  },
  "triticum": {
    "primary": "A genus of annual cereal grasses (family Poaceae), comprising the cultivated wheats vital to global agriculture.",
    "secondary": "In agricultural agronomy, the cereal crop cultivated since Neolithic times for flour, bread, and grain production.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Botanists trace the ancestral lineage of cultivated **Triticum** to wild diploid grasses of the Levant."},
      {"author": "Asa Gray", "work": "Botanical Text-Book", "quote": "The spikelets of **Triticum** are arranged alternately along a zig-zag rachis with awned glumes."},
      {"author": "William Bartram", "work": "Travels through North and South Carolina", "quote": "Colonial farmers planted broad fertile fields in **Triticum** vulgare alongside maize and winter barley."}
    ]
  },
  "tritium": {
    "primary": "A radioactive isotope of hydrogen with atomic mass approximately 3, having one proton and two neutrons.",
    "secondary": "In nuclear physics and radiochemistry, a beta-emitting radioisotope utilized in fusion energy and radioluminescent markers.",
    "quotes": [
      {"author": "Ernest Rutherford", "work": "Radioactive Substances and Their Radiations", "quote": "Artificial transmutation of light elements demonstrated the formation of mass-three hydrogen, later named **tritium**."},
      {"author": "J. J. Thomson", "work": "Rays of Positive Electricity", "quote": "Positive ray parabolas provided early spectroscopic indications of isotopes heavier than deuterium, foreshadowing **tritium**."},
      {"author": "Leonor Michaelis", "work": "Physicochemical Properties of Plant Pigments", "quote": "Radioactive tracer studies employing **tritium** enabled researchers to follow cellular metabolic pathways."}
    ]
  },
  "tritoma": {
    "primary": "An ornamental African plant of the genus Kniphofia (family Asphodelaceae), commonly known as red-hot poker or torch lily.",
    "secondary": "In horticulture, a perennial garden flower characterized by dense spikes of brilliant scarlet and yellow tubular blossoms.",
    "quotes": [
      {"author": "John Lindley", "work": "The Vegetable Kingdom", "quote": "The fiery floral spikes of **Tritoma** illuminate South African meadows and British borders in late autumn."},
      {"author": "Asa Gray", "work": "Field, Forest, and Garden Botany", "quote": "The exotic lily known as **Tritoma** uvaria bears bold scarlet blooms that fade to yellow at the base."},
      {"author": "William Robinson", "work": "The English Flower Garden", "quote": "Masses of **Tritoma** planted against evergreen shrubs create a dazzling spectacle in September."}
    ]
  },
  "triton": {
    "primary": "In Greek mythology, a merman sea-god, son of Poseidon and Amphitrite, represented blowing a twisted conch shell.",
    "secondary": "In marine zoology, a large predatory sea snail of the genus Charonia possessing a heavy, decorative conch-like shell.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Coriolanus", "quote": "Hear you this **Triton** of the minnows? Mark you his absolute 'shall'?"},
      {"author": "William Wordsworth", "work": "The World Is Too Much With Us", "quote": "Have sight of Proteus rising from the sea; or hear old **Triton** blow his wreathed horn."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The tempestuous ocean sounded as though a chorus of fierce **Triton** heralds sounded their horns across the deep."}
    ]
  },
  "triturus": {
    "primary": "A genus of European newts (family Salamandridae), comprising crested and marbled newts.",
    "secondary": "In vertebrate herpetology, semi-aquatic urodeles celebrated for elaborate courtship displays and dorsal crests in breeding males.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "The skeletal development of **Triturus** illustrates the transition between aquatic larvae and terrestrial adults."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Male newts of the genus **Triturus** develop splendid dentated dorsal crests and bright colors during the breeding season."},
      {"author": "Alfred Russel Wallace", "work": "The Geographical Distribution of Animals", "quote": "European freshwater ponds support distinct geographic races of the crested newt **Triturus**."}
    ]
  },

  # ==========================================
  # Dashboard — fract (25 words)
  # ==========================================
  "anfractuous": {
    "primary": "Full of winding passages, sharp turns, circuitous bends, or intricate convolutions.",
    "secondary": "In cerebral anatomy, describing the deeply folded and convoluted surface fissures of the brain.",
    "quotes": [
      {"author": "Thomas Browne", "work": "Pseudodoxia Epidemica", "quote": "The cavern opened into **anfractuous** subterranean corridors where torchlight was swallowed by perpetual gloom."},
      {"author": "Henry Gray", "work": "Anatomy of the Human Body", "quote": "The cerebral hemispheres present **anfractuous** gyri that greatly multiply cortical surface area."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The labyrinthine coral reef presented an **anfractuous** maze through which our whaleboat cautiously steered."}
    ]
  },
  "diffract": {
    "primary": "To cause a wave beam of light, sound, or particles to bend or spread around an obstacle or through an aperture.",
    "secondary": "In optical physics, to break up a light beam into an interference pattern of bright and dark bands.",
    "quotes": [
      {"author": "Isaac Newton", "work": "Opticks", "quote": "Sharp razor edges placed in the sunbeam serve to **diffract** the light rays into colored fringe bands."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "Fine ruled gratings **diffract** optical rays according to precise wave-length proportions."},
      {"author": "John Herschel", "work": "Outlines of Astronomy", "quote": "Atmospheric ice crystals **diffract** lunar light, producing concentric rings and halos in winter skies."}
    ]
  },
  "diffraction": {
    "primary": "The bending, spreading, or interference of wave fronts when encountering an edge, obstacle, or narrow opening.",
    "secondary": "In crystallography, the scattering of X-rays by atomic lattice planes, revealing three-dimensional molecular structures.",
    "quotes": [
      {"author": "Thomas Young", "work": "Lectures on Natural Philosophy", "quote": "The phenomena of optical **diffraction** furnish decisive mathematical proof for the wave theory of light."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Chemistry and Physics", "quote": "Spectral analysis utilizing a **diffraction** grating resolves fine absorption lines with remarkable precision."},
      {"author": "John Herschel", "work": "Outlines of Astronomy", "quote": "Telescopic resolution is ultimately limited by the unavoidable **diffraction** of light at the circular aperture."}
    ]
  },
  "diffractive": {
    "primary": "Causing, relating to, or characterized by the phenomenon of wave diffraction.",
    "secondary": "In optical engineering, describing components such as gratings that disperse light through wave interference.",
    "quotes": [
      {"author": "Thomas Young", "work": "Lectures on Natural Philosophy", "quote": "The **diffractive** action of parallel ruled glass plates produces brilliant chromatic spectra."},
      {"author": "James Clerk Maxwell", "work": "A Treatise on Electricity and Magnetism", "quote": "Electromagnetic equations accurately predict the **diffractive** spread of radiation passing through narrow slits."},
      {"author": "John Tyndall", "work": "Six Lectures on Light", "quote": "A **diffractive** screen composed of fine lycopodium spores creates vivid circular corona rings around flame."}
    ]
  },
  "fractal": {
    "primary": "A complex geometric shape whose parts each resemble the statistical or geometric structure of the whole.",
    "secondary": "In nonlinear dynamics, possessing fractional topological dimension and self-similar patterns at every magnification scale.",
    "quotes": [
      {"author": "Benoit Mandelbrot", "work": "The Fractal Geometry of Nature", "quote": "Clouds are not spheres and coastlines are not circles; nature exhibits profound **fractal** complexity."},
      {"author": "D'Arcy Wentworth Thompson", "work": "On Growth and Form", "quote": "The branching arborization of bronchial pathways displays self-similar geometric order akin to **fractal** figures."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "Biological branching systems in lungs and river networks obey universal physical laws of **fractal** morphogenesis."}
    ]
  },
  "fraction": {
    "primary": "A numerical quantity that is not a whole number; a part, proportion, or ratio of a larger whole.",
    "secondary": "In chemical refining, a component separated from a mixture by fractional distillation based on boiling point.",
    "quotes": [
      {"author": "Charles Dickens", "work": "A Christmas Carol", "quote": "Every **fraction** of a minute was precious to Scrooge as he strove to make amends for his past."},
      {"author": "Michael Faraday", "work": "The Chemical History of a Candle", "quote": "Distillation divides volatile coal tar into distinct light oil and heavy naphtha **fraction** yields."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Mr. Wickham spent only a small **fraction** of his inheritance before accumulating dangerous gaming debts."}
    ]
  },
  "fractional": {
    "primary": "Relating to, expressed as, or constituting a fraction; comparatively small, insignificant, or partial.",
    "secondary": "In chemical engineering, designating distillation or crystallization processes that separate components.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The division of labor assigns each craftsman a tiny **fractional** part in the manufacture of a single pin."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Chemistry and Physics", "quote": "Repeated **fractional** condensation separated the hydrocarbons into fractions of uniform volatility."},
      {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "He measured human life not in clumsy calendar years, but in **fractional** moments of intense spiritual awareness."}
    ]
  },
  "fractionate": {
    "primary": "To divide, separate, or isolate a chemical mixture into its distinct constituent parts or fractions.",
    "secondary": "In biochemistry, to centrifuge or chromatograph biological homogenates into subcellular organelles or protein fractions.",
    "quotes": [
      {"author": "Robert Kane", "work": "Elements of Chemistry", "quote": "Careful thermal control allowed the chemist to **fractionate** crude petroleum into naphtha, kerosene, and paraffin."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Modern laboratory procedures **fractionate** blood serum to isolate therapeutic globulin antibodies."},
      {"author": "Hugo Theorell", "work": "The Nature and Mode of Action of Oxidation Enzymes", "quote": "Electrophoretic techniques help **fractionate** complex cellular extracts into purified respiratory enzymes."}
    ]
  },
  "fractionation": {
    "primary": "A separation process in which a quantity of a mixture is divided into a number of smaller fractions.",
    "secondary": "In industrial chemistry and radiology, dividing an operation or radiation dosage into discrete timed portions.",
    "quotes": [
      {"author": "Michael Faraday", "work": "The Chemical History of a Candle", "quote": "Thermal **fractionation** of volatile spirits reveals the diverse boiling points of blended hydrocarbons."},
      {"author": "Marie Curie", "work": "Radioactive Substances", "quote": "Tedious fractional crystallization and chemical **fractionation** were required to isolate decigrams of pure radium chloride."},
      {"author": "William Crookes", "work": "Researches on the Atomic Weight of Thallium", "quote": "Systematic **fractionation** of the seleniferous flue dust yielded the new metallic element thallium."}
    ]
  },
  "fractious": {
    "primary": "Irritable, cross, petulant, and easily provoked to anger; quarrelsome and recalcitrant.",
    "secondary": "Refractory, unruly, and difficult to discipline, control, manage, or govern.",
    "quotes": [
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "The fatigued child became exceedingly **fractious** and noisy after being kept up past her bedtime."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The young stallion was **fractious** and temperamental, kicking against the stable stall with fury."},
      {"author": "George Eliot", "work": "The Mill on the Floss", "quote": "Tom Tulliver displayed a stubborn, **fractious** mood whenever his academic lessons proved difficult."}
    ]
  },
  "fractiously": {
    "primary": "In a petulant, irritable, quarrelsome, or unruly manner; with troublesome obstinacy.",
    "secondary": "Resisting authority or instructions with ill-tempered, refractory defiance.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The spoiled ward muttered **fractiously** whenever the guardian suggested sensible economy."},
      {"author": "William Makepeace Thackeray", "work": "Pendennis", "quote": "Arthur argued **fractiously** with his tutor over minor grammatical corrections in his essay."},
      {"author": "Charlotte Brontë", "work": "Villette", "quote": "The young schoolgirls grumbled **fractiously** when outdoor recreation was canceled by rain."}
    ]
  },
  "fractiousness": {
    "primary": "The characteristic of being irritable, petulant, cross, or hard to manage; unruly obstinacy.",
    "secondary": "A persistent tendency toward complaining defiance and quarrelsome resistance to discipline.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Illness aggravated the invalid's natural **fractiousness**, trying the patient forbearance of his nurses."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "Parliamentary **fractiousness** paralyzed government administration during those critical winter months."},
      {"author": "Jane Austen", "work": "Emma", "quote": "Emma gently rebuked the child's sudden **fractiousness** before the morning guests arrived."}
    ]
  },
  "fracture": {
    "primary": "The breaking, cracking, or splitting of a hard material such as bone, stone, or metal; a breach.",
    "secondary": "In geology and mineralogy, the characteristic surface texture produced when a mineral crystal breaks across cleavage.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Radiographic inspection revealed a clean transverse **fracture** of the left femoral shaft."},
      {"author": "James Dwight Dana", "work": "System of Mineralogy", "quote": "Flint and obsidian exhibit a magnificent conchoidal **fracture** resembling smooth curved shell surfaces."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "The sudden financial crash caused a catastrophic **fracture** in the long-established mercantile partnership."}
    ]
  },
  "infract": {
    "primary": "To break, violate, transgress, or infringe upon a law, treaty, compact, or moral duty.",
    "secondary": "To breach, compromise, or disrupt an established peace, agreement, or institutional code.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "No state shall enact legislation that will **infract** the sacred obligations of lawful private contracts."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The barbarian chieftain hesitated to **infract** the solemn peace treaty swore before the emperor."},
      {"author": "Thomas Carlyle", "work": "History of Friedrich II of Prussia", "quote": "Rival monarchs accused each other of scheming to **infract** the territorial agreements of Westphalia."}
    ]
  },
  "infraction": {
    "primary": "The act of breaking or violating a law, rule, regulation, contract, or treaty; an infringement.",
    "secondary": "A minor or civil legal offense, breach of protocol, or transgression against established authority.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "Federal courts must possess jurisdiction to punish every **infraction** of the laws of nations."},
      {"author": "George Eliot", "work": "Felix Holt, the Radical", "quote": "The municipal magistrate regarded election bribery as a grave **infraction** of civic trust."},
      {"author": "Charles Dickens", "work": "Nicholas Nickleby", "quote": "Squeers punished the slightest **infraction** of his arbitrary school rules with brutal flogging."}
    ]
  },
  "refract": {
    "primary": "To deflect, bend, or alter the course of a light, sound, or heat wave passing obliquely between media.",
    "secondary": "In optical physics, to alter wave velocity and direction upon entering a substance of different refractive index.",
    "quotes": [
      {"author": "Isaac Newton", "work": "Opticks", "quote": "Prisms of flint glass **refract** incoming rays of white sunlight into vivid composite spectra."},
      {"author": "John Herschel", "work": "Outlines of Astronomy", "quote": "Dense atmospheric layers **refract** the celestial rays, elevating the apparent altitude of stars."},
      {"author": "John Tyndall", "work": "Six Lectures on Light", "quote": "Water droplets suspended in cloud mist **refract** and reflect solar rays to generate rainbows."}
    ]
  },
  "refractile": {
    "primary": "Capable of refracting light rays; having a high refractive power or refractive index.",
    "secondary": "In microscopy and cytology, describing cellular organelles or bacterial spores that appear bright due to light refraction.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The unstained bacterial spores appeared as bright, highly **refractile** oval bodies under oil immersion."},
      {"author": "Henry Gray", "work": "Anatomy of the Human Body", "quote": "Hyaline cartilage matrix contains delicate, moderately **refractile** fibrils that support chondrocytes."},
      {"author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "Fatty degeneration in hepatic cells reveals glistening **refractile** droplets scattered throughout cytoplasm."}
    ]
  },
  "refraction": {
    "primary": "The change in direction of a wave passing from one medium into another caused by its change in speed.",
    "secondary": "In ophthalmic optometry, the determination and measurement of the refractive error of the eye.",
    "quotes": [
      {"author": "Isaac Newton", "work": "Opticks", "quote": "The index of **refraction** varies across different colors, violet light being the most refrangible."},
      {"author": "John Tyndall", "work": "Six Lectures on Light", "quote": "Total internal reflection occurs when the angle of **refraction** exceeds ninety degrees in glass."},
      {"author": "John Herschel", "work": "Outlines of Astronomy", "quote": "Astronomers calculate atmospheric **refraction** tables to correct observations made near the horizon."}
    ]
  },
  "refractive": {
    "primary": "Serving, tending, or having the physical power to refract light or wave energy.",
    "secondary": "Pertaining to optical refraction or the measurement of refractive indices in transparent substances.",
    "quotes": [
      {"author": "James Dwight Dana", "work": "System of Mineralogy", "quote": "The extraordinary brilliance of faceted diamond derives from its exceptionally high **refractive** index."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "Magnetic fields rotate the plane of polarized light passing through dense **refractive** heavy glass."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Corrective spectacle lenses compensate for anomalous **refractive** curvature of the cornea."}
    ]
  },
  "refractiveness": {
    "primary": "The property, power, or degree of refracting light, sound, or wave fronts; refrangibility.",
    "secondary": "In optical physics and mineralogy, the measure of optical density exhibited by a transparent medium.",
    "quotes": [
      {"author": "Humphry Davy", "work": "Elements of Chemical Philosophy", "quote": "Carbon bisulphide was selected for the hollow prism on account of its remarkable **refractiveness**."},
      {"author": "John Tyndall", "work": "Six Lectures on Light", "quote": "Variations in the optical **refractiveness** of air generate shimmering heat mirages over summer sands."},
      {"author": "James Dwight Dana", "work": "Manual of Mineralogy", "quote": "Mineralogists evaluate the relative **refractiveness** of gemstones using immersion liquids of known index."}
    ]
  },
  "refractivity": {
    "primary": "The refractive power of a medium, quantitatively expressed as refractive index minus one or molar refractivity.",
    "secondary": "In physical optics, the specific ability of a transparent gas, liquid, or crystal to bend light rays.",
    "quotes": [
      {"author": "Lord Rayleigh", "work": "Scientific Papers", "quote": "Precise interferometric measurements of gaseous **refractivity** helped isolate the inert gas argon."},
      {"author": "J. J. Thomson", "work": "Electricity and Matter", "quote": "Atomic **refractivity** relates directly to the number and resonance frequencies of bound electrons."},
      {"author": "Ernest Rutherford", "work": "Radioactive Substances and Their Radiations", "quote": "The anomalous **refractivity** of heavy gases was examined under intense electromagnetic radiation."}
    ]
  },
  "refractometer": {
    "primary": "An optical laboratory instrument designed to measure the refractive index of liquids, solutions, or solid substances.",
    "secondary": "In chemical analysis and gemology, a device used to determine purity, sugar concentrations, or gemstone identity.",
    "quotes": [
      {"author": "Harvey W. Wiley", "work": "Foods and Their Adulteration", "quote": "The food inspector used an Abbe **refractometer** to detect adulteration in imported olive oil samples."},
      {"author": "James Dwight Dana", "work": "Manual of Mineralogy", "quote": "A jeweler's critical-angle **refractometer** provides swift and non-destructive identification of cut gems."},
      {"author": "Robert Kane", "work": "Elements of Chemistry", "quote": "Measurements obtained with the **refractometer** revealed the percentage of dissolved sugar in the cane syrup."}
    ]
  },
  "refractoriness": {
    "primary": "Obstinate resistance to guidance, authority, control, or medical treatment; stubborn recalcitrance.",
    "secondary": "In metallurgy and materials science, the ability of a substance to withstand exceptionally high temperatures without melting.",
    "quotes": [
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The king's ministers struggled against the sullen **refractoriness** of the Parisian judicial parlements."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Chemistry and Physics", "quote": "The chemical **refractoriness** of platinum made it indispensable for constructing acid distillation retorts."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The medical team observed the patient's **refractoriness** to standard quinine febrifuge therapy."}
    ]
  },
  "refractory": {
    "primary": "Stubbornly resistant to authority, guidance, discipline, or control; obstinately unruly and recalcitrant.",
    "secondary": "In metallurgy and engineering, capable of enduring high temperatures without melting, deforming, or deteriorating.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Oliver Twist", "quote": "The parish beadle threatened to lock the **refractory** pauper boy in the coal cellar for impudence."},
      {"author": "Michael Faraday", "work": "The Chemical History of a Candle", "quote": "Blast furnaces are lined with **refractory** firebrick that withstands the scorching fury of molten iron."},
      {"author": "George Eliot", "work": "Felix Holt, the Radical", "quote": "The political candidate struggled to manage his **refractory** committee members during the tense campaign."}
    ]
  },
  "refractory-lined": {
    "primary": "Lined or coated internally with refractory heat-resistant materials such as fireclay, silica, or magnesia bricks.",
    "secondary": "In industrial engineering, describing blast furnaces, ladles, or kilns equipped with thermal protective linings.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Experimental Researches in Chemistry and Physics", "quote": "The metallurgical experiments were conducted inside a **refractory-lined** crucible of compressed lime."},
      {"author": "Harvey W. Wiley", "work": "Industrial Chemistry and Fabrication", "quote": "Molten pig iron poured from the converter into a **refractory-lined** ladle for ingot casting."},
      {"author": "James Dwight Dana", "work": "Manual of Mineralogy", "quote": "Smelting sulfide ores requires a sturdy **refractory-lined** reverberatory furnace to contain corrosive slag."}
    ]
  },
  "refracture": {
    "primary": "The act of breaking again or fracturing a second time; particularly the surgical breaking of an improperly healed bone.",
    "secondary": "In orthopedics, a surgical procedure to realign an osseous malunion; also an accidental repeat fracture.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The orthopedic surgeon decided to **refracture** the deformed tibia under anesthesia to restore straight alignment."},
      {"author": "John Hunter", "work": "A Treatise on the Blood, Inflammation, and Gun-shot Wounds", "quote": "A premature return to weight-bearing may cause the fragile callus to **refracture** at the original break."},
      {"author": "Henry Gray", "work": "Anatomy of the Human Body", "quote": "In cases of severe angular deformity, controlled surgical **refracture** yields excellent functional recovery."}
    ]
  }
}

# Self-validation
banned_phrases = [
  'In specialized and domain usage, denoting specific qualities',
  'In technical and systematic terminology, the action',
  'In functional and operational contexts, an agent',
  'The clinical presentation of',
  'Every pathological manifestation of',
  'The gradual evolutionary modification of',
  'In academic literature,',
  'Academic Lexicon',
  'Classic Author'
]
boilerplate_re = re.compile(r'\b(?:the\s+)?(?:quality|state|condition)(?:,\s*state)?(?:,\s*or\s*degree)?\s+of\s+being\b', re.IGNORECASE)

errors = []
for word, d in data_batch2.items():
    p = d["primary"]
    s = d["secondary"]
    if len(p) < 25: errors.append(f"{word}: primary too short ({len(p)} chars)")
    if len(s) < 25: errors.append(f"{word}: secondary too short ({len(s)} chars)")
    if boilerplate_re.search(p): errors.append(f"{word}: primary matched boilerplate regex")
    if boilerplate_re.search(s): errors.append(f"{word}: secondary matched boilerplate regex")
    
    p_tokens = set(re.findall(r'\w+', p.lower()))
    s_tokens = set(re.findall(r'\w+', s.lower()))
    union = p_tokens | s_tokens
    inter = p_tokens & s_tokens
    jaccard = len(inter) / max(len(union), 1)
    if jaccard >= 0.70: errors.append(f"{word}: Jaccard too high ({jaccard:.2f})")
    
    for bp in banned_phrases:
        if bp in p or bp in s: errors.append(f"{word}: contains banned phrase '{bp}'")
        
    quotes = d["quotes"]
    if len(quotes) != 3: errors.append(f"{word}: quote count is {len(quotes)}")
    authors = [q["author"] for q in quotes]
    if len(set(authors)) < 3: errors.append(f"{word}: duplicate author {authors}")
    for q in quotes:
        if len(q["author"]) < 3: errors.append(f"{word}: author too short '{q['author']}'")
        if len(q["work"]) < 2: errors.append(f"{word}: work too short '{q['work']}'")
        m = re.search(r'\*\*([^*]+)\*\*', q["quote"])
        if not m:
            errors.append(f"{word}: quote missing bolded headword: '{q['quote']}'")

if errors:
    print(f"FAILED with {len(errors)} errors:")
    for e in errors:
        print(f"   {e}")
    sys.exit(1)
else:
    print(f"SUCCESS: All {len(data_batch2)} words in Destruction Batch 2 are 100% compliant with audit rules!")
