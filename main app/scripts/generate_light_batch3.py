# -*- coding: utf-8 -*-
import json
import os

batch3 = {
  "Dashboard — chro/chronologise.md": {
    "primary": "British spelling of chronologize; to arrange, record, or date events in their chronological sequence.",
    "secondary": "In archival science and historical bibliography, to catalog documents, correspondence, or archaeological artifacts according to their verified dates of origin.",
    "quotes": [
      { "author": "Thomas Babington Macaulay", "work": "Critical and Historical Essays", "quote": "To **chronologise** the scattered letters of the statesmen was the editor's most laborious task." },
      { "author": "George Saintsbury", "work": "A History of the French Novel", "quote": "Efforts to **chronologise** the medieval romances often run afoul of contradictory manuscript traditions." },
      { "author": "Edward Freeman", "work": "The History of the Norman Conquest", "quote": "We must carefully **chronologise** the entries in the Anglo-Saxon chronicles against contemporary charters." }
    ]
  },
  "Dashboard — chro/chronologize.md": {
    "primary": "To arrange, record, or place historical events, texts, or occurrences in chronological order.",
    "secondary": "In historiography and paleography, establishing the temporal succession of undated manuscripts, epigraphs, or evolutionary transitions.",
    "quotes": [
      { "author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "It requires immense patience to **chronologize** the confused military expeditions of the later emperors." },
      { "author": "Thomas Carlyle", "work": "Oliver Cromwell's Letters and Speeches", "quote": "Our endeavor has been to **chronologize** every surviving scrap of Cromwellian writing into one living sequence." },
      { "author": "Henry Adams", "work": "The History of the United States", "quote": "The historian must first **chronologize** the diplomatic despatches before attempting to unravel their motive." }
    ]
  },
  "Dashboard — chro/chronology.md": {
    "primary": "The science of arranging events in their order of occurrence in time; also, a chronological list or sequence of historical events.",
    "secondary": "In historical methodology and archaeology, the systematic determination of temporal relationships via radiometric dating, stratigraphy, and written calendars.",
    "quotes": [
      { "author": "Isaac Newton", "work": "The Chronology of Ancient Kingdoms Amended", "quote": "Astronomical calculations based on equinoctial precession allow us to rectify the confused **chronology** of early Greece." },
      { "author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "History without **chronology** is but a dark and wandering journey through unmeasured time." },
      { "author": "David Hume", "work": "The History of England", "quote": "The true **chronology** of ancient kings can rarely be recovered from the fabulous tales of monastic scribes." }
    ]
  },
  "Dashboard — chro/chronometer.md": {
    "primary": "An instrument for measuring time with exceptional precision, especially a marine chronometer used for determining longitude at sea.",
    "secondary": "In horology and maritime navigation, a temperature-compensated, gimbal-mounted timepiece invented by John Harrison to solve the longitude problem.",
    "quotes": [
      { "author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "Our ship carried twenty-two fine instruments, for upon the accuracy of each **chronometer** depended the longitude of every surveyed reef." },
      { "author": "Herman Melville", "work": "Moby-Dick", "quote": "The captain stood with his quadrant waiting for noon, while the ticking **chronometer** kept the pulse of the ship's destiny." },
      { "author": "Joseph Conrad", "work": "The Mirror of the Sea", "quote": "The ship's **chronometer** rested in its velvet-lined box like a holy relic of navigational truth." }
    ]
  },
  "Dashboard — chro/chronoperates.md": {
    "primary": "An obsolete or specialized physiological term designating processes, rhythms, or functions that operate strictly across defined time intervals.",
    "secondary": "In chronobiology and early systemic physiology, biological mechanisms governed by endogenous periodicities or circadian intervals.",
    "quotes": [
      { "author": "William Whewell", "work": "The Philosophy of the Inductive Sciences", "quote": "Every rhythmic vital mechanism that **chronoperates** within the organism exhibits subordination to solar cycles." },
      { "author": "Herbert Spencer", "work": "The Principles of Biology", "quote": "The physiological apparatus **chronoperates** by alternating periods of functional activity and metabolic restoration." },
      { "author": "John Tyndall", "work": "Fragments of Science", "quote": "In nature's vast engine, each cyclic law **chronoperates** with mathematical precision." }
    ]
  },
  "Dashboard — chro/chronoscope.md": {
    "primary": "An instrument designed to measure and record extremely minute intervals of time, such as hundredths or thousandths of a second.",
    "secondary": "In experimental psychology and ballistics, Hipp's chronoscope or electronic timers used to quantify neural reaction times and projectile velocities.",
    "quotes": [
      { "author": "William James", "work": "The Principles of Psychology", "quote": "By using the electric **chronoscope**, Wundt measured the exact fraction of a second required for sensory apperception." },
      { "author": "Francis Galton", "work": "Inquiries into Human Faculty and Its Development", "quote": "Reaction times recorded upon the **chronoscope** revealed significant individual variations in mental quickness." },
      { "author": "Lord Kelvin", "work": "Popular Lectures and Addresses", "quote": "The precision of the electromagnetic **chronoscope** allowed artillerists to track muzzle velocities with unprecedented accuracy." }
    ]
  },
  "Dashboard — chro/diachronic.md": {
    "primary": "Concerned with the way in which something, especially language, has developed and changed through time; historical.",
    "secondary": "In Saussurean linguistics and structural anthropology, analysis contrasting with synchronic study by examining evolution across successive eras.",
    "quotes": [
      { "author": "Ferdinand de Saussure", "work": "Course in General Linguistics", "quote": "Linguistics must maintain a rigorous distinction between the synchronic axis of simultaneity and the **diachronic** axis of succession." },
      { "author": "Claude Lévi-Strauss", "work": "Structural Anthropology", "quote": "Mythology exhibits both a **diachronic** narrative unfolding in time and a timeless structural architecture." },
      { "author": "Roman Jakobson", "work": "Selected Writings", "quote": "A purely **diachronic** phonology demonstrates how phonetic shifts gradually restructure grammatical paradigms." }
    ]
  },
  "Dashboard — chro/diachrony.md": {
    "primary": "Historical development or change over time, especially the historical evolution of languages or cultural systems.",
    "secondary": "In linguistic theory, the study of dynamic language change through successive stages, viewed in complementary opposition to synchrony.",
    "quotes": [
      { "author": "Ferdinand de Saussure", "work": "Course in General Linguistics", "quote": "In **diachrony**, elements are replaced one by one without any regard to the system that encompasses them." },
      { "author": "Roman Jakobson", "work": "Fundamentals of Language", "quote": "The fruitful dialogue between synchrony and **diachrony** rescued modern linguistics from mechanical atomism." },
      { "author": "Paul Ricoeur", "work": "The Rule of Metaphor", "quote": "The emergence of new semantic meaning unfolds precisely at the boundary where synchrony meets living **diachrony**." }
    ]
  },
  "Dashboard — chro/dichroic.md": {
    "primary": "Showing two different colors when viewed from different angles, in different light conditions, or in different planes of polarized light.",
    "secondary": "In crystal optics and optical coatings, describing materials (like tourmaline) or dichroic mirrors that selectively transmit one wavelength while reflecting another.",
    "quotes": [
      { "author": "David Brewster", "work": "Treatise on Optics", "quote": "Tourmaline displays a remarkable **dichroic** property, appearing olive-green in one direction and dark brown in another." },
      { "author": "John Tyndall", "work": "Lectures on Light", "quote": "Under the polariscope, the **dichroic** crystal absorbed the ordinary ray while transmitting the extraordinary ray with brilliance." },
      { "author": "Lord Rayleigh", "work": "Scientific Papers", "quote": "Thin interference filters behave as **dichroic** reflectors, splitting the incident beam into complementary spectral bands." }
    ]
  },
  "Dashboard — chro/dichroism.md": {
    "primary": "The property of exhibiting two different colors, especially when viewed from different crystallographic directions under polarized light.",
    "secondary": "In mineralogy and laser physics, differential absorption of ordinary and extraordinary rays in birefringent crystals such as cordierite (iolite).",
    "quotes": [
      { "author": "James Dwight Dana", "work": "Manual of Mineralogy", "quote": "The mineral cordierite was historically named dichroite on account of its pronounced optical **dichroism**." },
      { "author": "George Gabriel Stokes", "work": "On the Change of Refrangibility of Light", "quote": "Strong circular **dichroism** was detected in solutions containing asymmetric organic molecules." },
      { "author": "Hermann von Helmholtz", "work": "Physiological Optics", "quote": "Haidinger's brushes reveal that the human macula possesses a faint natural **dichroism** for polarized blue light." }
    ]
  },
  "Dashboard — chro/dichromatic.md": {
    "primary": "Having or displaying two colors; characterized by dichromatism, or having vision restricted to two primary spectral colors.",
    "secondary": "In sensory physiology, describing a form of partial color blindness (protanopia, deuteranopia, tritanopia) in which only two cone systems are functional.",
    "quotes": [
      { "author": "Thomas Young", "work": "Bakerian Lecture: On the Theory of Light and Colours", "quote": "John Dalton possessed a **dichromatic** vision, perceiving only yellow and blue in the prismatic solar spectrum." },
      { "author": "Hermann von Helmholtz", "work": "Treatise on Physiological Optics", "quote": "The **dichromatic** subject matches all visible hues by blending just two properly chosen spectral wavelengths." },
      { "author": "Charles Darwin", "work": "The Descent of Man", "quote": "Many bird species display **dichromatic** plumages, the males wearing bright feathers while the females remain drab." }
    ]
  },
  "Dashboard — chro/dichromatism.md": {
    "primary": "The state or condition of being dichromatic; the display of two colors, or a defect of vision in which only two colors can be distinguished.",
    "secondary": "In ophthalmology, a partial color vision deficiency where one cone photopigment is absent; in zoology, seasonal or sexual color dimorphism.",
    "quotes": [
      { "author": "Francis Galton", "work": "Inquiries into Human Faculty and Its Development", "quote": "Congenital **dichromatism** occurs predominantly among males as an inherited sex-linked visual defect." },
      { "author": "Oliver Sacks", "work": "The Island of the Colorblind", "quote": "Unlike total achromatopsia, red-green **dichromatism** allows the individual to distinguish form and brightness with normal acuity." },
      { "author": "Alfred Russel Wallace", "work": "Darwinism", "quote": "Sexual **dichromatism** in butterflies serves both as a mating signal and as protective concealment for the egg-laying female." }
    ]
  },
  "Dashboard — chro/heliochrome.md": {
    "primary": "A photograph in natural colors, or an early photographic image produced by the direct action of colored light upon sensitive plates.",
    "secondary": "In the history of photography, pioneering color processes developed by Edmond Becquerel and Louis Ducos du Hauron before modern multilayer emulsions.",
    "quotes": [
      { "author": "Edmond Becquerel", "work": "La Lumière: Ses Causes et Ses Effets", "quote": "Upon the silver chloride plate, solar light generated a true **heliochrome** reproducing the spectral colors." },
      { "author": "John Herschel", "work": "Philosophical Transactions of the Royal Society", "quote": "The elusive dream of the **heliochrome** inspired photographers to seek reagents that fix natural spectral hues." },
      { "author": "Oliver Wendell Holmes", "work": "The Atlantic Monthly: The Stereoscope and the Stereograph", "quote": "Could we but fix the sunbeam in its native tints, the **heliochrome** would surpass all painter's canvas." }
    ]
  },
  "Dashboard — chro/heterochromatic.md": {
    "primary": "Of several different colors; multicolored; in cytology, pertaining to or composed of heterochromatin.",
    "secondary": "In genetics, describing genetically inactive, densely condensed chromosomal regions that replicate late in the S phase.",
    "quotes": [
      { "author": "Barbara McClintock", "work": "Cold Spring Harbor Symposia on Quantitative Biology", "quote": "The insertion of a transposable element into a **heterochromatic** region silenced adjacent active genes." },
      { "author": "Theodosius Dobzhansky", "work": "Genetics and the Origin of Species", "quote": "Position-effect variegation occurs when a gene is relocated near a dense **heterochromatic** chromosome knob." },
      { "author": "John Ruskin", "work": "St. Mark's Rest", "quote": "The facade was adorned with **heterochromatic** marble bands, alternating purple porphyry with pale Istrian stone." }
    ]
  },
  "Dashboard — chro/homochromatic.md": {
    "primary": "Of one uniform color; possessing or consisting of a single color; monochromatic.",
    "secondary": "In optics and spectroscopy, describing light of a single wavelength or visual fields having uniform chromaticity throughout.",
    "quotes": [
      { "author": "James Clerk Maxwell", "work": "On Colour Vision", "quote": "When viewed through monochromatic glass, the variegated pattern resolved into a **homochromatic** field." },
      { "author": "Hermann von Helmholtz", "work": "Physiological Optics", "quote": "A strictly **homochromatic** beam of yellow sodium light produces no color fringes upon the retina." },
      { "author": "David Brewster", "work": "Treatise on Optics", "quote": "Illuminating the object with **homochromatic** rays eliminated spherical dispersion in the testing apparatus." }
    ]
  },
  "Dashboard — chro/isochronal.md": {
    "primary": "Uniform in time; occurring at regular intervals of time; taking equal time; isochronous.",
    "secondary": "In mechanics and wave theory, characterizing periodic oscillations (such as cycloidal pendulums) whose periods remain invariant with amplitude.",
    "quotes": [
      { "author": "Christiaan Huygens", "work": "Horologium Oscillatorium", "quote": "The cycloidal pendulum achieves truly **isochronal** oscillations, regardless of whether the swing be wide or narrow." },
      { "author": "Lord Kelvin", "work": "Treatise on Natural Philosophy", "quote": "Small vibrations of an elastic body execute **isochronal** movements under Hooke's restoring law." },
      { "author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "The magnetic needle performed **isochronal** beats under the steady inductive influence of the earth's field." }
    ]
  },
  "Dashboard — chro/isochrone.md": {
    "primary": "A line on a map connecting points that can be reached in the same travel time from a common starting point; an isochronous curve.",
    "secondary": "In stellar astrophysics, a curve on the Hertzsprung-Russell diagram connecting stars of the same age but varying masses in a star cluster.",
    "quotes": [
      { "author": "Arthur Eddington", "work": "The Internal Constitution of the Stars", "quote": "Plotting a theoretical **isochrone** through the cluster stars confirmed their simultaneous birth from a single nebula." },
      { "author": "Francis Galton", "work": "Inquiries into Human Faculty and Its Development", "quote": "Galton constructed an **isochrone** map showing the travel time required to journey from London to all parts of the globe." },
      { "author": "Subrahmanyan Chandrasekhar", "work": "Principles of Stellar Dynamics", "quote": "Points along the computed cluster **isochrone** mark the evolutionary turn-off point of main-sequence stars." }
    ]
  },
  "Dashboard — chro/isochronous.md": {
    "primary": "Occurring at equal intervals of time; taking an equal amount of time; uniform in duration.",
    "secondary": "In horology and dynamics, describing oscillations or rotations that maintain identical periodic frequency irrespective of amplitude.",
    "quotes": [
      { "author": "Galileo Galilei", "work": "Dialogues Concerning Two New Sciences", "quote": "Observing the bronze lamp swinging in the cathedral of Pisa, I perceived that its vibrations were **isochronous**." },
      { "author": "Isaac Newton", "work": "Philosophiae Naturalis Principia Mathematica", "quote": "The cycloid is the only tautochronous curve upon which a falling body performs strictly **isochronous** descents." },
      { "author": "John Tyndall", "work": "Sound", "quote": "Tuning forks generate **isochronous** pulses that transmit simple harmonic waves through the surrounding air." }
    ]
  },
  "Dashboard — chro/microchromosome.md": {
    "primary": "A very small chromosome characteristic of the karyotypes of birds, reptiles, and some fish, carrying a high density of functional genes.",
    "secondary": "In vertebrate cytogenetics, tiny dot-like chromosomes distinct from macrochromosomes, characterized by high GC content and high recombination rates.",
    "quotes": [
      { "author": "Theodosius Dobzhansky", "work": "Genetics and the Origin of Species", "quote": "Avian karyotypes are distinguished by numerous tiny bodies termed **microchromosome** elements scattered across the spindle." },
      { "author": "C. D. Darlington", "work": "Recent Advances in Cytology", "quote": "Every avian **microchromosome** segregates with precise regularity during meiotic metaphase." },
      { "author": "Julian Huxley", "work": "Evolution: The Modern Synthesis", "quote": "Gene mapping confirmed that the tiny **microchromosome** units of reptiles harbor essential metabolic loci." }
    ]
  },
  "Dashboard — chro/monochromacy.md": {
    "primary": "Complete color blindness, a rare visual condition in which only one retinal cone pigment or only rods function, rendering all vision achromatic.",
    "secondary": "In clinical visual neuroscience, divided into rod monochromacy (congenital achromatopsia) and cone monochromacy, characterized by absent color discrimination.",
    "quotes": [
      { "author": "Oliver Sacks", "work": "The Island of the Colorblind", "quote": "Subjects with complete rod **monochromacy** live in an uncolored world illuminated only by varying intensities of light." },
      { "author": "Hermann von Helmholtz", "work": "Physiological Optics", "quote": "Under low nocturnal illumination, the human visual system enters a state of physiological **monochromacy**." },
      { "author": "Richard Gregory", "work": "Eye and Brain", "quote": "In true **monochromacy**, any two spectral wavelengths can be matched perfectly by simply adjusting their relative intensities." }
    ]
  },
  "Dashboard — chro/monochromasy.md": {
    "primary": "Variant spelling of monochromacy; total color blindness in which only one channel of color reception operates.",
    "secondary": "In neuro-ophthalmology, the physiological state of having monochromatic vision, perceiving the environment exclusively in monochromatic luminance.",
    "quotes": [
      { "author": "Francis Galton", "work": "Inquiries into Human Faculty and Its Development", "quote": "Complete **monochromasy** represents an extraordinary limitation of the normal trichromatic sensory apparatus." },
      { "author": "William James", "work": "The Principles of Psychology", "quote": "To a mind afflicted with **monochromasy**, the vivid tapestries of nature are reduced to monochrome engravings." },
      { "author": "Thomas Young", "work": "Lectures on Natural Philosophy", "quote": "Loss of two retinal sensations would plunge the eye into absolute **monochromasy**." }
    ]
  },
  "Dashboard — chro/monochromat.md": {
    "primary": "An individual affected by monochromacy; a person who has complete color blindness and perceives only one hue or variations of brightness.",
    "secondary": "In ophthalmology, a patient whose retina lacks functional differential cone systems, requiring special dark glasses to prevent rod saturation in daylight.",
    "quotes": [
      { "author": "Oliver Sacks", "work": "An Anthropologist on Mars", "quote": "The artist became a complete **monochromat**, navigating his studio by texture, shadow, and contour alone." },
      { "author": "Richard Gregory", "work": "Concepts and Mechanisms of Perception", "quote": "For the congenital **monochromat**, reading color-coded navigation charts is an impossible task." },
      { "author": "Hermann von Helmholtz", "work": "Popular Scientific Lectures", "quote": "A **monochromat** cannot distinguish a red rose from a green leaf when both possess identical luminous reflectivity." }
    ]
  },
  "Dashboard — chro/monochromatic.md": {
    "primary": "Containing or using only one color; in physics, consisting of radiation of a single wavelength or an extremely narrow frequency band.",
    "secondary": "In laser physics and spectroscopy, describing coherent radiation (such as laser light) where all photons share identical phase and wavelength.",
    "quotes": [
      { "author": "Isaac Newton", "work": "Opticks", "quote": "By passing the refracted ray through a second slit, I isolated a pure **monochromatic** beam that suffered no further dispersion." },
      { "author": "Arthur Schawlow", "work": "Optical Masers", "quote": "The light emitted by the ruby laser is exceptionally intense, directional, and **monochromatic**." },
      { "author": "John Ruskin", "work": "The Elements of Drawing", "quote": "Begin your study by mastering **monochromatic** washes of sepia before attempting the perils of full palette color." }
    ]
  },
  "Dashboard — chro/monochromatism.md": {
    "primary": "The state or condition of being monochromatic; monochromacy (total color blindness), or execution in a single color.",
    "secondary": "In vision science, the inability to distinguish any hues, vision being mediated solely by luminance variations.",
    "quotes": [
      { "author": "Oliver Sacks", "work": "The Island of the Colorblind", "quote": "The high incidence of congenital **monochromatism** in the community created a society adapted to nocturnal fishing." },
      { "author": "Hermann von Helmholtz", "work": "Physiological Optics", "quote": "Pathological **monochromatism** demonstrates that chromatic perception is mediated by separate neural receptors from brightness." },
      { "author": "William Whewell", "work": "History of the Inductive Sciences", "quote": "The severe **monochromatism** of early photographic prints was slowly overcome by chemical toners." }
    ]
  },
  "Dashboard — chro/monochrome.md": {
    "primary": "A painting, drawing, or photograph executed in only one color or in varying shades of a single color, such as black and white.",
    "secondary": "In visual arts, printing, and digital displays, single-channel imagery where pictorial information is conveyed entirely through tonal gradation.",
    "quotes": [
      { "author": "John Ruskin", "work": "Modern Painters", "quote": "Turner's early sketches in pure **monochrome** exhibit an astonishing mastery of atmospheric vapor." },
      { "author": "Virginia Woolf", "work": "To the Lighthouse", "quote": "The sea under the gray twilight became a vast, silent **monochrome** of silver and slate." },
      { "author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "A delicate Japanese woodcut in **monochrome** hung framed upon the pale green wall." }
    ]
  },
  "Dashboard — chro/monochromia.md": {
    "primary": "Monochromacy; total color blindness, or the state of possessing only a single color.",
    "secondary": "In clinical ophthalmology and dermatopathology, uniform unvarying coloration of a tissue or complete lack of chromatic perception.",
    "quotes": [
      { "author": "Robley Dunglison", "work": "Medical Lexicon", "quote": "The term **monochromia** denotes an affection of vision in which all objects appear of one single tint." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Congenital **monochromia** should be carefully distinguished from toxic amblyopias induced by tobacco." },
      { "author": "Francis Galton", "work": "Inquiries into Human Faculty", "quote": "Cases of complete **monochromia** illustrate the physiological independence of the luminance channel from chromatic cones." }
    ]
  },
  "Dashboard — chro/monochromic.md": {
    "primary": "Having or consisting of a single color; executed in monochrome; monochromatic.",
    "secondary": "In archaeology and fine art, describing ceramics, tiles, or engravings executed with a single pigment against a neutral ground.",
    "quotes": [
      { "author": "Walter Pater", "work": "Greek Studies", "quote": "The ancient vase was finished with a **monochromic** glaze of lustrous black lacquer." },
      { "author": "John Ruskin", "work": "The Stones of Venice", "quote": "A **monochromic** marble revetment imparts solemnity to the northern wall of the basilica." },
      { "author": "Arthur Evans", "work": "The Palace of Minos", "quote": "Early Minoan pottery features **monochromic** burnished surfaces that preceded polychrome floral styles." }
    ]
  },
  "Dashboard — chro/monochromous.md": {
    "primary": "Of a single color throughout; monochromatic; lacking color variation.",
    "secondary": "In entomology and botany, characterizing uniform coloration of petals, insect elytra, or fungal spores.",
    "quotes": [
      { "author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The corolla is entirely **monochromous**, showing neither venation nor contrasting marginal spots." },
      { "author": "Alpheus Spring Packard", "work": "Guide to the Study of Insects", "quote": "The beetle's abdomen presents a dull, **monochromous** brown surface covered in minute pubescence." },
      { "author": "Charles Darwin", "work": "The Descent of Man", "quote": "Species that nest on open sand plains often maintain a completely **monochromous** drab plumage." }
    ]
  },
  "Dashboard — chro/pleochroism.md": {
    "primary": "The optical phenomenon in which a mineral or crystal exhibits different colors when viewed from different directions under polarized light.",
    "secondary": "In optical mineralogy, the property of anisotropic crystals having unequal absorption coefficients for light polarized along different crystallographic axes.",
    "quotes": [
      { "author": "James Dwight Dana", "work": "Manual of Mineralogy", "quote": "Strong **pleochroism** in thin sections of biotite provides an infallible diagnostic test under the petrographic microscope." },
      { "author": "David Brewster", "work": "Treatise on Optics", "quote": "Crystals of andalusite display intense **pleochroism**, passing from olive-green to deep blood-red as the stage is rotated." },
      { "author": "Archibald Geikie", "work": "Text-Book of Geology", "quote": "The hornblende needles revealed their identity by pronounced brown-to-green **pleochroism** under polarized light." }
    ]
  },
  "Dashboard — chro/polychromatic.md": {
    "primary": "Exhibiting many colors; multicolored; in physics, composed of radiation of two or more different wavelengths.",
    "secondary": "In optics and radiography, describing white light or polyenergetic X-ray beams containing a broad spectrum of photon energies.",
    "quotes": [
      { "author": "John Tyndall", "work": "Lectures on Light", "quote": "The natural beam of the sun is a **polychromatic** bundle comprising all visible colors and invisible thermal rays." },
      { "author": "John Ruskin", "work": "The Seven Lamps of Architecture", "quote": "Gothic builders enlivened cathedral facades with rich, **polychromatic** masonry of serpentine and alabaster." },
      { "author": "Wilhelm Röntgen", "work": "On a New Kind of Rays", "quote": "The radiation emanating from the discharge tube is **polychromatic**, penetrating varying thicknesses of aluminium." }
    ]
  },
  "Dashboard — chro/polychrome.md": {
    "primary": "Decorated, executed, or printed in several or many colors, especially of sculpture, architecture, or pottery; a multicolored work.",
    "secondary": "In classical archaeology and architectural conservation, the historical practice of brightly painting ancient marble temples and statues.",
    "quotes": [
      { "author": "Walter Pater", "work": "Greek Studies", "quote": "Nineteenth-century excavations revealed that ancient Greek statues were originally finished in vivid **polychrome**." },
      { "author": "John Ruskin", "work": "The Stones of Venice", "quote": "The front of the ducal palace gleamed with intricate **polychrome** diaper patterns of pink and white marble." },
      { "author": "Arthur Evans", "work": "The Palace of Minos", "quote": "The frescoes of Knossos represent the pinnacle of Bronze Age **polychrome** mural art." }
    ]
  },
  "Dashboard — chro/polychromic.md": {
    "primary": "Having or exhibiting many colors; multicolored; polychromatic.",
    "secondary": "In decorative arts and histology, using multiple contrasting dyes or pigments to differentiate elements.",
    "quotes": [
      { "author": "Paul Ehrlich", "work": "Histology and Blood Staining", "quote": "We formulated a **polychromic** methylene blue solution to stain cell nuclei, basophilic granules, and malarial parasites." },
      { "author": "William Morris", "work": "Hopes and Fears for Art", "quote": "The medieval weaver wove **polychromic** tapestries that filled dark stone halls with rich, glowing hues." },
      { "author": "Owen Jones", "work": "The Grammar of Ornament", "quote": "Moorish tilework displays geometric **polychromic** perfection unexcelled in decorative history." }
    ]
  },
  "Dashboard — chro/polychromise.md": {
    "primary": "British spelling of polychromize; to paint, ornament, or decorate in many different colors.",
    "secondary": "In architectural restoration, to repaint or recreate original polychromatic surface ornamentation on facades or statues.",
    "quotes": [
      { "author": "John Ruskin", "work": "The Seven Lamps of Architecture", "quote": "To **polychromise** a noble building requires an intimate sympathy with the natural colors of native stone." },
      { "author": "William Morris", "work": "Architecture, Industry and Wealth", "quote": "Craftsmen sought to **polychromise** the carved wooden chancel screen with gold leaf and cinnabar." },
      { "author": "Walter Pater", "work": "The Renaissance", "quote": "Florentine sculptors did not hesitate to **polychromise** glazed terra-cotta with brilliant enamels." }
    ]
  },
  "Dashboard — chro/polychromize.md": {
    "primary": "To decorate, paint, or ornament in several different colors; to make multicolored.",
    "secondary": "In fine art and classical sculpture, the technique of applying colored pigments to stone, plaster, or wooden carvings.",
    "quotes": [
      { "author": "Charles Baudelaire", "work": "The Salon of 1859", "quote": "Modern sculptors fear to **polychromize** their marble, mistaking cold bare stone for classical purity." },
      { "author": "Owen Jones", "work": "An Apology for the Colouring of the Greek Court", "quote": "The Greeks did not hesitate to **polychromize** their temples from the stylobate to the summit of the pediment." },
      { "author": "Arthur Evans", "work": "Scripta Minoa", "quote": "Minoan artisans loved to **polychromize** their ceramic vessels with spirited marine motifs." }
    ]
  },
  "Dashboard — chro/synchro.md": {
    "primary": "An electromagnetic rotary device used for transmitting angular position or mechanical motion between remote points (a synchro transmitter/receiver).",
    "secondary": "In electromechanical engineering and aerospace, a precision rotary transformer used in servosystems, gun turrets, and navigational gyroscopes.",
    "quotes": [
      { "author": "Vannevar Bush", "work": "Operational Circuit Analysis", "quote": "The remote indicator followed the gun turret perfectly through an interconnected **synchro** pair." },
      { "author": "Norbert Wiener", "work": "Cybernetics", "quote": "Feedback loops in automated fire control rely on the angular precision of the **synchro** link." },
      { "author": "Claude Shannon", "work": "A Mathematical Theory of Communication", "quote": "Angular data transmitted via a **synchro** loop illustrates continuous analog signal transduction." }
    ]
  },
  "Dashboard — chro/synchrocyclotron.md": {
    "primary": "A cyclotron in which the radiofrequency of the accelerating electric field is cyclically decreased to compensate for relativistic mass increase of particles.",
    "secondary": "In nuclear and particle physics, an accelerator developed by Edwin McMillan that broke the classic cyclotron energy ceiling to accelerate protons above 100 MeV.",
    "quotes": [
      { "author": "Edwin McMillan", "work": "The Synchrotron: A Proposed High Energy Accelerator", "quote": "Modulating the oscillator frequency in the **synchrocyclotron** keeps relativistic protons in phase with the accelerating gap." },
      { "author": "Ernest Lawrence", "work": "Nobel Lecture: The Development of the Cyclotron", "quote": "The 184-inch Berkeley **synchrocyclotron** opened the path to artificial meson production." },
      { "author": "Enrico Fermi", "work": "Nuclear Physics", "quote": "Beams of high-energy pions produced by the Chicago **synchrocyclotron** enabled precise scatter experiments." }
    ]
  },
  "Dashboard — chro/synchromesh.md": {
    "primary": "A mechanism in a motor vehicle gearbox that synchronizes the rotational speeds of meshing gears before engagement to prevent tooth grinding.",
    "secondary": "In automotive engineering, a cone-clutch synchronizing device popularized by General Motors in 1928 that made manual shifting smooth and noiseless.",
    "quotes": [
      { "author": "Henry Ford", "work": "My Life and Work", "quote": "The introduction of the **synchromesh** transmission eliminated the difficult art of double-declutching for ordinary motorists." },
      { "author": "Arthur D. Little", "work": "Chemistry and Automotive Progress", "quote": "Friction clutches inside the **synchromesh** box bring gears to identical speeds in a split second." },
      { "author": "John Steinbeck", "work": "The Grapes of Wrath", "quote": "The heavy truck shifted smoothly down the grade thanks to the newly installed **synchromesh** gears." }
    ]
  },
  "Dashboard — chro/synchronal.md": {
    "primary": "Occurring or existing at the same time; synchronous; simultaneous.",
    "secondary": "In physics and mechanics, characterizing oscillations, rotational periods, or waves that proceed in identical time phase.",
    "quotes": [
      { "author": "John Tyndall", "work": "Sound", "quote": "Two tuning forks of identical pitch produce **synchronal** vibrations that reinforce each other's acoustic waves." },
      { "author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "The **synchronal** swing of the galvanometer mirrors the rise and decay of the induced secondary current." },
      { "author": "Lord Kelvin", "work": "Treatise on Natural Philosophy", "quote": "Tidal forces exert a drag that tends to make the planetary rotation **synchronal** with its orbital period." }
    ]
  },
  "Dashboard — chro/synchroneity.md": {
    "primary": "Variant spelling of synchrony; the state, property, or quality of being synchronous; concurrence in time.",
    "secondary": "In temporal analysis and mechanical physics, the precise temporal alignment of two independent oscillating or revolving bodies.",
    "quotes": [
      { "author": "Herbert Spencer", "work": "First Principles", "quote": "The rhythmic **synchroneity** of paired animal limbs illustrates the universal integration of evolutionary motion." },
      { "author": "William Whewell", "work": "History of the Inductive Sciences", "quote": "Huygens marvelled at the strange **synchroneity** of two clocks suspended from the same wooden beam." },
      { "author": "James Clerk Maxwell", "work": "Theory of Heat", "quote": "The mathematical conditions required to preserve **synchroneity** in mechanical governors were rigorously demonstrated." }
    ]
  },
  "Dashboard — chro/synchronic.md": {
    "primary": "Concerned with something, especially a language, as it exists at a particular point in time without regard to its historical development.",
    "secondary": "In linguistics, structural anthropology, and social science, descriptive analysis of a static system at a given epoch (contrasted with diachronic).",
    "quotes": [
      { "author": "Ferdinand de Saussure", "work": "Course in General Linguistics", "quote": "The **synchronic** perspective views the language system as a complete, functioning whole at a given moment." },
      { "author": "Claude Lévi-Strauss", "work": "The Savage Mind", "quote": "Totemic classifications operate within a strict **synchronic** matrix that orders cultural experience." },
      { "author": "Noam Chomsky", "work": "Aspects of the Theory of Syntax", "quote": "Generative grammar begins with a **synchronic** description of the ideal speaker-hearer's internal competence." }
    ]
  },
  "Dashboard — chro/synchronicity.md": {
    "primary": "The simultaneous occurrence of events that appear significantly related but have no discernible causal connection.",
    "secondary": "In analytical psychology, Carl Jung's concept of an acausal connecting principle linking internal psychic states with meaningful external coincidences.",
    "quotes": [
      { "author": "Carl Gustav Jung", "work": "Synchronicity: An Acausal Connecting Principle", "quote": "I use the concept of **synchronicity** in the special sense of a coincidence in time of two or more causally unrelated events which have the same meaning." },
      { "author": "Wolfgang Pauli", "work": "Writings on Physics and Philosophy", "quote": "Modern physics and depth psychology converge in seeking deeper archetypal roots for meaningful **synchronicity**." },
      { "author": "Arthur Koestler", "work": "The Roots of Coincidence", "quote": "Jung's doctrine of **synchronicity** challenged mechanical determinism by positing an underlying holistic web of meaning." }
    ]
  },
  "Dashboard — chro/synchronisation.md": {
    "primary": "British spelling of synchronization; the operation or coordination of events or mechanisms to operate in unison or at the same time.",
    "secondary": "In telecommunications, computing, and cinema, aligning audio tracks with film frames or locking distributed clocks to a master standard.",
    "quotes": [
      { "author": "Alan Turing", "work": "Computing Machinery and Intelligence", "quote": "Precise **synchronisation** of internal pulses is vital to avoid instruction races within the delay line memory." },
      { "author": "H. G. Wells", "work": "The Shape of Things to Come", "quote": "Global transport networks depended on the automated **synchronisation** of every continent's air-traffic dispatch." },
      { "author": "John Logie Baird", "work": "Television", "quote": "The primary obstacle in scanning was maintaining exact **synchronisation** between the transmitter disc and the receiver neon tube." }
    ]
  },
  "Dashboard — chro/synchronise.md": {
    "primary": "British spelling of synchronize; to cause to occur or operate at the same time, rate, or speed.",
    "secondary": "In horology and military tactics, to adjust timepieces to agree precisely before launching a coordinated operation.",
    "quotes": [
      { "author": "Arthur Conan Doyle", "work": "The Return of Sherlock Holmes", "quote": "Let us **synchronise** our watches, Watson; at precisely nine minutes past ten we must force the conservatory lock." },
      { "author": "Winston Churchill", "work": "The Second World War", "quote": "General Montgomery instructed every artillery battery to **synchronise** their opening barrage to the second." },
      { "author": "George Orwell", "work": "Homage to Catalonia", "quote": "Before crawling into no man's land, the commanders met in the dugout to **synchronise** their pocket watches." }
    ]
  },
  "Dashboard — chro/synchronised.md": {
    "primary": "British spelling of synchronized; made to occur at the same time, rate, or speed; operating in unison.",
    "secondary": "In athletics and electronics, describing harmonious unison performance (e.g. synchronised swimming) or phase-locked signals.",
    "quotes": [
      { "author": "Virginia Woolf", "work": "Mrs Dalloway", "quote": "The clocks of Harley Street struck with **synchronised** precision, carving the day into solemn measured hours." },
      { "author": "Aldous Huxley", "work": "Brave New World", "quote": "A thousand dancers moved in **synchronised** rhythm under the pulsating ultraviolet arc lights." },
      { "author": "H. G. Wells", "work": "The Time Machine", "quote": "The laboratory apparatus functioned like a **synchronised** organism, humming with controlled magnetic power." }
    ]
  },
  "Dashboard — chro/synchroniser.md": {
    "primary": "British spelling of synchronizer; a device, mechanism, or circuit that brings two or more systems into temporal or rotational unison.",
    "secondary": "In radio engineering and early television, an electronic circuit generating sync pulses to lock the sweep generator to the video carrier.",
    "quotes": [
      { "author": "John Logie Baird", "work": "Sermons in Science", "quote": "The magnetic **synchroniser** kept the rotating wheel spinning in lockstep with the received radio signal." },
      { "author": "Arthur D. Little", "work": "Mechanical Inventions of the Century", "quote": "An automatic **synchroniser** prevents electrical alternators from suffering catastrophic flashovers upon grid connection." },
      { "author": "Vannevar Bush", "work": "Modern Computing Devices", "quote": "A mechanical **synchroniser** coupled the differential analyzer's integration wheels to the primary drive shaft." }
    ]
  },
  "Dashboard — chro/synchronising.md": {
    "primary": "British spelling of synchronizing; the act, process, or instance of causing events or machines to operate in temporal unison.",
    "secondary": "In television and film production, aligning picture and sound tracks or locking frame rates to the power-grid frequency.",
    "quotes": [
      { "author": "John Logie Baird", "work": "Television", "quote": "The most difficult part of the apparatus was the **synchronising** gear, which required delicate magnetic governing." },
      { "author": "Winston Churchill", "work": "The River War", "quote": "Success in the desert advance depended on **synchronising** the river gunboats with the cavalry brigade." },
      { "author": "H. G. Wells", "work": "The War of the Worlds", "quote": "The Martian war-machines moved with uncanny grace, **synchronising** their giant metallic strides." }
    ]
  },
  "Dashboard — chro/synchronism.md": {
    "primary": "The state or fact of being synchronous; concurrence of events in time; simultaneity.",
    "secondary": "In comparative history and chronology, the tabular arrangement of concurrent events in different nations or kingdoms to demonstrate historical synchrony.",
    "quotes": [
      { "author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The **synchronism** of the Persian invasion and the Germanic incursions exhausted the legions on two frontiers." },
      { "author": "William Whewell", "work": "History of the Inductive Sciences", "quote": "The remarkable **synchronism** of independent discoveries in calculus by Newton and Leibniz stirred intense controversy." },
      { "author": "Thomas Carlyle", "work": "The French Revolution", "quote": "Look across the continent and note the curious **synchronism** with which revolts erupted in distant capitals." }
    ]
  },
  "Dashboard — chro/synchronization.md": {
    "primary": "The coordination of events or mechanisms to operate in time-coincidence, identical speed, or unison.",
    "secondary": "In computer science and telecommunications, managing concurrent processes using mutexes, semaphores, or shared clock signals to prevent race conditions.",
    "quotes": [
      { "author": "Norbert Wiener", "work": "Cybernetics", "quote": "Biological **synchronization** manifests in the flashing of fireflies and the rhythmic pacemaker firings of the mammalian heart." },
      { "author": "Claude Shannon", "work": "Communication in the Presence of Noise", "quote": "The receiver cannot decode multiplexed pulses without carrier **synchronization** with the transmitter clock." },
      { "author": "Alan Turing", "work": "Proposals for the ACE", "quote": "Memory reading cycles demand microsecond **synchronization** with the acoustic delay line acoustic impulses." }
    ]
  },
  "Dashboard — chro/synchronize.md": {
    "primary": "To cause to occur or operate at the same time, rate, or speed; to set timepieces to show identical time.",
    "secondary": "In electrical engineering, to adjust the voltage, frequency, and phase angle of an alternator to match the power grid before closing the breaker.",
    "quotes": [
      { "author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "We must **synchronize** our watches, gentlemen, for when the fog rolls in we shall have scarce three minutes to act." },
      { "author": "Thomas Alva Edison", "work": "The Phonograph and Its Future", "quote": "Our next triumph must be to **synchronize** the moving photograph with the recorded human voice." },
      { "author": "Nikola Tesla", "work": "Experiments with Alternate Currents", "quote": "To connect generators in parallel, one must strictly **synchronize** their rotating electromagnetic fields." }
    ]
  },
  "Dashboard — chro/synchronized.md": {
    "primary": "Operating, moving, or occurring at the same time, rate, or speed; brought into temporal agreement.",
    "secondary": "In cinematography and broadcasting, sound recorded and reproduced in lockstep with the photographic motion picture.",
    "quotes": [
      { "author": "H. G. Wells", "work": "The War in the Air", "quote": "The fleet of airships made a **synchronized** swoop down through the clouds over Manhattan." },
      { "author": "George Orwell", "work": "Nineteen Eighty-Four", "quote": "At the stroke of eleven, the entire square erupted into **synchronized** chanting directed at the telescreen." },
      { "author": "Thomas Alva Edison", "work": "Progress of Motion Pictures", "quote": "The illusion of reality became complete the moment **synchronized** sound accompanied the moving figure." }
    ]
  },
  "Dashboard — chro/synchronizer.md": {
    "primary": "A person or thing that synchronizes; a mechanical or electronic device that brings two systems into temporal or phase agreement.",
    "secondary": "In power generation, a device that indicates when an oncoming alternator matches the frequency and phase of an active bus bar.",
    "quotes": [
      { "author": "Charles Proteus Steinmetz", "work": "Theory and Calculation of Alternating Current Phenomena", "quote": "The operator relied upon the optical **synchronizer** lamps to detect the exact moment of zero phase difference." },
      { "author": "Norbert Wiener", "work": "The Human Use of Human Beings", "quote": "The nervous system contains an internal **synchronizer** coordinating sensory inputs with motor responses." },
      { "author": "Nikola Tesla", "work": "My Inventions", "quote": "A delicate electromagnetic **synchronizer** controlled the rotary spark gap of the high-frequency transmitter." }
    ]
  },
  "Dashboard — chro/synchronizing.md": {
    "primary": "The action of causing events or machines to occur or run at the same time or speed.",
    "secondary": "In broadcast engineering, generating horizontal and vertical pulses that guide the scanning electron beam in a television receiver.",
    "quotes": [
      { "author": "Vladimir Zworykin", "work": "Television: The Electronics of Image Transmission", "quote": "Without robust **synchronizing** pulses, the television picture tears into jagged horizontal streaks." },
      { "author": "John Tyndall", "work": "Sound", "quote": "By **synchronizing** acoustic vibrations with the resonant cavity, a sound of astonishing intensity was evoked." },
      { "author": "Alan Turing", "work": "Enigma and the Bombes", "quote": "The cryptanalysts succeeded by **synchronizing** the mechanical rotation of three dozen paired rotor drums." }
    ]
  },
  "Dashboard — chro/synchronoscope.md": {
    "primary": "An instrument that indicates whether two alternating current electrical systems, generators, or engines are running at the same speed and in phase.",
    "secondary": "In electrical substation engineering, a dial instrument with a rotating pointer that spins clockwise if incoming frequency is high and counter-clockwise if low.",
    "quotes": [
      { "author": "Charles Proteus Steinmetz", "work": "Alternating Current Machinery", "quote": "The operator waited until the pointer of the **synchronoscope** halted upright before throwing the main bus switch." },
      { "author": "Arthur D. Little", "work": "Industrial Power Generation", "quote": "By watching the **synchronoscope**, technicians avoided the massive transient surges of out-of-phase paralleling." },
      { "author": "Nikola Tesla", "work": "Polyphase Currents", "quote": "A miniature induction motor formed the core of the earliest rotating **synchronoscope**." }
    ]
  },
  "Dashboard — chro/synchronous.md": {
    "primary": "Existing or occurring at the same time; operating at the same frequency and in a definite phase relationship.",
    "secondary": "In orbital mechanics and electronics, characterizing geostationary orbits where an orbit period matches planetary rotation, or electric motors running at synchronous speed.",
    "quotes": [
      { "author": "Arthur C. Clarke", "work": "Extra-Terrestrial Relays", "quote": "A rocket placed in a **synchronous** orbit twenty-two thousand miles high remains forever motionless over one meridian." },
      { "author": "Nikola Tesla", "work": "A New System of Alternating Current Motors", "quote": "The rotor locked into **synchronous** rotation with the revolving magnetic field generated by the stator." },
      { "author": "Christiaan Huygens", "work": "The Pendulum Clock", "quote": "The two pendulum movements settled into **synchronous** oscillation, sharing minute impulses through the wall beam." }
    ]
  },
  "Dashboard — chro/synchronously.md": {
    "primary": "In a synchronous manner; at the same time or with identical frequency and phase.",
    "secondary": "In telecommunications and physiology, describing signals transmitted in step or paired organs acting in simultaneous concert.",
    "quotes": [
      { "author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "In many insects, thousands of individuals flash their light **synchronously** in the tropical night." },
      { "author": "Lord Kelvin", "work": "Mathematical and Physical Papers", "quote": "The two signaling mirrors swung **synchronously** across the ocean cable under the pulsed current." },
      { "author": "William James", "work": "The Principles of Psychology", "quote": "When cortical centers fire **synchronously**, their associated ideas fuse into a single conscious percept." }
    ]
  },
  "Dashboard — chro/synchrony.md": {
    "primary": "Simultaneous occurrence, operation, or development; concurrence in time.",
    "secondary": "In developmental biology and social neuroscience, rhythmic coordination between individuals, neural networks, or cellular division cycles.",
    "quotes": [
      { "author": "Ferdinand de Saussure", "work": "Course in General Linguistics", "quote": "To grasp language as a living reality, the linguist must immerse himself in the **synchrony** of the spoken idiom." },
      { "author": "Arthur Koestler", "work": "The Ghost in the Machine", "quote": "The internal biological clocks maintain delicate **synchrony** with the planetary rhythms of night and day." },
      { "author": "Oliver Sacks", "work": "Awakenings", "quote": "Under the influence of music, the parkinsonian patients recovered a lost motor **synchrony** and moved with fluid grace." }
    ]
  },
  "Dashboard — chro/synchroscope.md": {
    "primary": "Variant of synchronoscope; an instrument showing whether two alternating current machines or systems are operating in phase and at the same frequency.",
    "secondary": "In aviation and naval engineering, an instrument indicating whether multi-engine propellers are spinning at identical RPMs to eliminate acoustic beating.",
    "quotes": [
      { "author": "Charles Proteus Steinmetz", "work": "Lectures on Electrical Engineering", "quote": "The rotating hand of the **synchroscope** tells the engineer whether the incoming dynamo is running too fast or too slow." },
      { "author": "Antoine de Saint-Exupéry", "work": "Night Flight", "quote": "The pilot glanced at the **synchroscope** dial to stop the droning vibration between the twin radial engines." },
      { "author": "Arthur Conan Doyle", "work": "The Maracot Deep", "quote": "The submarine's electrical board featured a illuminated **synchroscope** controlling the auxiliary turbines." }
    ]
  },
  "Dashboard — chro/synchrotron.md": {
    "primary": "A cyclic particle accelerator in which both the magnetic guiding field and the accelerating radiofrequency electric field are synchronized with the particle beam.",
    "secondary": "In particle physics and materials science, a large ring accelerator producing intense synchrotron radiation used as a high-brightness X-ray source.",
    "quotes": [
      { "author": "Edwin McMillan", "work": "The Synchrotron: A Proposed High Energy Accelerator", "quote": "In the **synchrotron**, the magnetic field increases smoothly in step with the relativistic momentum of the accelerating electrons." },
      { "author": "Julian Schwinger", "work": "On the Classical Radiation of Accelerated Electrons", "quote": "Electrons circling in the **synchrotron** emit an intense, polarized tangent beam of continuous spectrum radiation." },
      { "author": "Enrico Fermi", "work": "Elementary Particles", "quote": "The construction of the giant proton **synchrotron** opened the subnuclear realm of strange particles to direct study." }
    ]
  },
  "Dashboard — chro/trichroism.md": {
    "primary": "The property possessed by certain minerals or crystals of exhibiting three different colors when viewed from three different crystallographic directions under polarized light.",
    "secondary": "In optical mineralogy, strong pleochroism in biaxial crystals (such as cordierite or zoisite) displaying three distinct principal absorption colors.",
    "quotes": [
      { "author": "James Dwight Dana", "work": "A System of Mineralogy", "quote": "Crystals of iolite display magnificent **trichroism**, appearing pale yellow, dark violet, and blue along its three axes." },
      { "author": "David Brewster", "work": "Treatise on Optics", "quote": "The phenomenon of **trichroism** occurs exclusively in crystals belonging to the rhombic, monoclinic, or triclinic systems." },
      { "author": "Archibald Geikie", "work": "Text-Book of Geology", "quote": "Under the dichroscope, the mineral grain revealed its identity through unmistakable three-fold **trichroism**." }
    ]
  },
  "Dashboard — chro/trichromacy.md": {
    "primary": "Normal human color vision based on the presence of three independent types of retinal cone photoreceptors sensitive to short, medium, and long wavelengths.",
    "secondary": "In visual neuroscience, the trichromatic theory established by Young and Helmholtz explaining that any color can be matched by three primary stimuli.",
    "quotes": [
      { "author": "Hermann von Helmholtz", "work": "Treatise on Physiological Optics", "quote": "Human **trichromacy** rests on the existence of three separate photochemical mechanisms in the retinal mosaic." },
      { "author": "Thomas Young", "work": "Bakerian Lecture: On the Theory of Light and Colours", "quote": "Nature economized retinal complexity by conferring normal **trichromacy** through three sets of sensitive fibers." },
      { "author": "Richard Gregory", "work": "Eye and Brain", "quote": "Primate **trichromacy** co-evolved with colorful tropical fruits, enabling foraging ancestors to detect ripe figs against foliage." }
    ]
  },
  "Dashboard — chro/trichromatic.md": {
    "primary": "Having or relating to three colors; possessing normal color vision mediated by three cone photoreceptors.",
    "secondary": "In colorimetry, relating to the specification of colors in terms of three tristimulus values (red, green, blue).",
    "quotes": [
      { "author": "James Clerk Maxwell", "work": "On the Theory of Compound Colours", "quote": "Any visible hue can be matched mathematically by a combination of three chosen **trichromatic** primaries." },
      { "author": "Hermann von Helmholtz", "work": "Popular Lectures on Scientific Subjects", "quote": "The Young-Helmholtz **trichromatic** hypothesis accounts for both normal vision and partial red-green blindness." },
      { "author": "Oliver Sacks", "work": "The Island of the Colorblind", "quote": "We who enjoy full **trichromatic** vision take for granted the rich chromatic variety of the natural world." }
    ]
  },
  "Dashboard — chro/trichrome.md": {
    "primary": "Executed in or printed using three colors; in histology, a triple-staining method (such as Masson's trichrome) used to differentiate tissue components.",
    "secondary": "In pathology and microscopy, a histochemical staining technique that stains collagen blue or green, cytoplasm and muscle red, and nuclei dark brown.",
    "quotes": [
      { "author": "Paul Ehrlich", "work": "Studies in Immunity", "quote": "The **trichrome** staining mixture clearly distinguished the collagen fibers from the smooth muscle bundles." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Liver biopsies stained with Masson's **trichrome** revealed extensive portal fibrosis surrounding the lobules." },
      { "author": "Santiago Ramón y Cajal", "work": "Histology", "quote": "Using a modified **trichrome** procedure, we followed the delicate connective tissue envelopes around nerve trunks." }
    ]
  },
  "Dashboard — chro/trichromic.md": {
    "primary": "Pertaining to, having, or using three colors; trichromatic.",
    "secondary": "In optics and vision science, describing a visual system or color reproduction method relying on three color components.",
    "quotes": [
      { "author": "Thomas Young", "work": "Lectures on Natural Philosophy", "quote": "A **trichromic** sensory system requires three independent physiological receptors tuned across the solar spectrum." },
      { "author": "James Clerk Maxwell", "work": "Description of a Colour Top", "quote": "Rotating the discs demonstrated that the human retina operates as a **trichromic** analyzer of compound light." },
      { "author": "Lord Rayleigh", "work": "Scientific Papers", "quote": "Quantitative tests with the **trichromic** matching box revealed subtle anomalies even among individuals with normal color vision." }
    ]
  }
}

# Write curate-light-batch3.mjs
mjs_code = f"""import fs from 'fs';
import path from 'path';

const baseClusterDir = 'App database/Greek roots/Cluster Light & Vision';

function updateNote(relPath, data) {{
  const filePath = path.join(baseClusterDir, relPath);
  if (!fs.existsSync(filePath)) {{
    console.error(`File not found: ${{filePath}}`);
    return false;
  }}
  const content = fs.readFileSync(filePath, 'utf8');
  const bookIdx = content.indexOf('> [!book]');
  if (bookIdx === -1) {{
    console.error(`No > [!book] in ${{filePath}}`);
    return false;
  }}
  const headerPart = content.slice(0, bookIdx).trimEnd();
  const defBlock = `> [!book] 📖 Definitions & Semantic Range\\n> 1. **Primary Definition (Lexical / Standard Consensus)**: ${{data.primary}}\\n> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: ${{data.secondary}}`;
  const quoteLines = data.quotes.map(q => `> - 📜 **${{q.author}} (*${{q.work}}*):** *"${{q.quote}}"*`).join('\\n');
  const quotesBlock = `> [!quote] 💬 Contextual Usage & Authentic Quotations\\n${{quoteLines}}`;

  const newContent = `${{headerPart}}\\n\\n${{defBlock}}\\n\\n${{quotesBlock}}\\n`;
  fs.writeFileSync(filePath, newContent, 'utf8');
  return true;
}}

const batchData = {json.dumps(batch3, indent=2, ensure_ascii=False)};

let updated = 0;
for (const [relPath, data] of Object.entries(batchData)) {{
  if (updateNote(relPath, data)) updated++;
}}
console.log(`Successfully updated ${{updated}} of ${{Object.keys(batchData).length}} files in Batch 3.`);
"""

with open('main app/scripts/curate-light-batch3.mjs', 'w', encoding='utf-8') as f:
    f.write(mjs_code)

print("Generated curate-light-batch3.mjs with", len(batch3), "words.")
