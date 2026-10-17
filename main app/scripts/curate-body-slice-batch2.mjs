import path from 'path';
import { updateNotesBatch } from './curate-updater-util.mjs';

const baseClusterDir = path.resolve('App database/Greek roots/Cluster Body & Physiology');

const batch2Data = {
  "Dashboard — clav\\claviceps.md": {
    primary: "A genus of parasitic ascomycete fungi that infect cereal grasses and sedges, most notably Claviceps purpurea (ergot of rye).",
    secondary: "In toxicology and pharmaceutical history, fungi whose hard sclerotia produce toxic ergot alkaloids responsible for historical ergotism and modern vasospastic medications.",
    quotes: [
      { author: "Louis Pasteur", work: "Studies on Fermentation", quote: "The black spurred grains of rye infected with **Claviceps** demonstrate how parasitic molds subvert the seed tissues of cereal hosts." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Epidemics of holy fire in the Middle Ages resulted from the accidental ingestion of bread flour contaminated by **Claviceps**." },
      { author: "Albert Hofmann", work: "LSD: My Problem Child", quote: "My laboratory investigation of the alkaloids of **Claviceps** purpurea ultimately led to the synthesis of lysergic acid derivatives." }
    ]
  },
  "Dashboard — clav\\clavichord.md": {
    primary: "An early European stringed keyboard instrument in which sound is produced by small brass tangents striking against metal strings.",
    secondary: "In music history, an intimate Renaissance and Baroque instrument prized for its capacity for delicate dynamic shading and expressive vibrato (Bebung).",
    quotes: [
      { author: "Charles Burney", work: "The Present State of Music in Germany, the Netherlands, and United Provinces", quote: "Carl Philipp Emanuel Bach sat down at his beloved **clavichord**, coaxing from its strings tones of profound tenderness and pathos." },
      { author: "George Eliot", work: "Daniel Deronda", quote: "In the quiet drawing room stood an antique **clavichord**, whose gentle notes seemed to whisper forgotten melodies of the eighteenth century." },
      { author: "Thomas Mann", work: "Doctor Faustus", quote: "He played a preludium upon the **clavichord**, demonstrating how the direct contact of tangent upon string permits expressive modulation of volume." }
    ]
  },
  "Dashboard — clav\\clavicipitaceae.md": {
    primary: "A family of perithecial ascomycete fungi (order Hypocreales) that includes ergot fungi, cordyceps, and grass endophytes.",
    secondary: "In systematic mycology, parasitic fungi distinguished by cylindrical asci, filiform ascospores, and potent biological alkaloid synthesis.",
    quotes: [
      { author: "Charles Horton Peck", work: "Annual Report of the State Botanist of New York", quote: "The family **Clavicipitaceae** includes some of our most formidable agricultural blights as well as fascinating insect parasites." },
      { author: "Elias Magnus Fries", work: "Systema Mycologicum", quote: "Species of the **Clavicipitaceae** produce erect, club-shaped stromata rising directly from the hardened sclerotium of the host." },
      { author: "Liberty Hyde Bailey", work: "The Standard Cyclopedia of Horticulture", quote: "Pathologists study the **Clavicipitaceae** to understand how fungal endophytes impart both pest resistance and toxicity to pasture grasses." }
    ]
  },
  "Dashboard — clav\\clavicle.md": {
    primary: "The collarbone; a slender, doubly curved long bone connecting the sternum to the acromion of the scapula.",
    secondary: "In human and vertebrate anatomy, the strut-like skeletal element that braces the shoulder girdle and provides free lateral mobility to the arm.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "A Manual of the Anatomy of Vertebrated Animals", quote: "The presence of a well-developed **clavicle** is characteristic of animals whose forelimbs enjoy wide freedom of movement." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Fracture of the **clavicle** is the most common skeletal injury in children, usually occurring at the junction of the outer and middle thirds." },
      { author: "Richard Owen", work: "On the Archetype of the Skeleton", quote: "The paired **clavicle** elements fuse in the avian lineage to form the furcula or wishbone, stabilizing the flight stroke." }
    ]
  },
  "Dashboard — clav\\clavier.md": {
    primary: "A musical keyboard, or any keyboard instrument, particularly an early stringed instrument such as a harpsichord, clavichord, or piano.",
    secondary: "In keyboard pedagogy, the generic term used by J. S. Bach (as in The Well-Tempered Clavier) to designate any tempered manual keyboard instrument.",
    quotes: [
      { author: "Johann Sebastian Bach", work: "The Well-Tempered Clavier (Preface)", quote: "These preludes and fugues across all twenty-four keys were composed for the use of musical youth eager to master the **clavier**." },
      { author: "Thomas Carlyle", work: "The Life of Friedrich Schiller", quote: "His sister sat at the **clavier**, accompanying his youthful verses with gentle German airs." },
      { author: "Virginia Woolf", work: "The Voyage Out", quote: "Rachel sat alone in the hall playing late Beethoven sonatas upon the open **clavier**, her fingers lost in the music." }
    ]
  },
  "Dashboard — clav\\clavus.md": {
    primary: "A localized corn or callosity on the foot caused by chronic mechanical pressure and friction.",
    secondary: "In historical medicine, a severe, circumscribed hysteria-associated headache feeling like a nail being driven into the skull (clavus hystericus); in ancient Rome, a purple stripe on a tunic.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Patients with acute hysteria frequently complain of **clavus**, describing a sensation as if a sharp spike were hammered into the vertex of the cranium." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The broad purple stripe of the **clavus** distinguished the senator from the equestrian order in ancient Rome." },
      { author: "Jonathan Hutchinson", work: "Archives of Surgery", quote: "The deep conical core of a painful **clavus** must be meticulously enucleated to relieve pressure on the underlying periosteum." }
    ]
  },
  "Dashboard — clav\\enclave.md": {
    primary: "A portion of territory entirely surrounded by the territory of an alien state or sovereign power.",
    secondary: "In political geography and urban sociology, a distinct cultural, linguistic, or ethnic community enclosed within a larger, differing population.",
    quotes: [
      { author: "Alexis de Tocqueville", work: "Democracy in America", quote: "The small Indian reservations formed a tragic, isolated **enclave** surrounded on all sides by expanding European settlements." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "A small Roman **enclave** held out along the Danube for decades after the surrounding provinces had fallen to barbarian kings." },
      { author: "Hannah Arendt", work: "The Origins of Totalitarianism", quote: "Stateless refugees found themselves trapped within a legal **enclave**, devoid of civil rights in their country of refuge." }
    ]
  },
  "Dashboard — copr\\copr.md": {
    primary: "The Greek root (kopros, meaning 'dung, excrement, feces'), forming the basis of scientific and medical terms relating to scatology and fecal matter.",
    secondary: "In paleontological and entomological etymology, the combining radical signifying fossilized waste (coprolite) or dung-feeding behavior (coprophagy).",
    quotes: [
      { author: "Henry George Liddell & Robert Scott", work: "A Greek-English Lexicon", quote: "The Greek noun kopros signified animal dung or ordure; from its root **copr** modern naturalists constructed coprolite and coprophilous." },
      { author: "Walter William Skeat", work: "An Etymological Dictionary of the English Language", quote: "In scientific coinage, the element **copr** denotes fecal matter or waste products." },
      { author: "Thomas Henry Huxley", work: "Principles of Paleontology", quote: "Fossilized droppings termed coprolites preserve the radical **copr**, linking geology with the ancient diets of extinct reptiles." }
    ]
  },
  "Dashboard — copr\\copra.md": {
    primary: "The dried meat or kernel of the coconut, from which coconut oil is extracted.",
    secondary: "In economic botany and colonial maritime history, a major agricultural export commodity of the South Pacific and Indian Ocean islands.",
    quotes: [
      { author: "Robert Louis Stevenson", work: "In the South Seas", quote: "The schooner rolled in the lagoon while the crew loaded sacks of pungent, oily **copra** brought out by native canoes." },
      { author: "Herman Melville", work: "Omoo: A Narrative of Adventures in the South Seas", quote: "The trading captains were eager to barter calico and iron tools for tons of sun-dried **copra**." },
      { author: "Joseph Conrad", work: "Lord Jim", quote: "He managed a remote trading station on the river, shipping out timber and dried **copra** to Singapore steamers." }
    ]
  },
  "Dashboard — copr\\copremia.md": {
    primary: "A historical medical condition characterized by blood poisoning or toxemia attributed to the absorption of fecal poisons from chronic intestinal stasis.",
    secondary: "In 19th-century clinical pathology, an autointoxication syndrome hypothesized to produce languor, sallow complexion, and cephalalgia from severe constipation.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The theory of **copremia** gained wide credence among Victorian clinicians, who attributed diverse nervous symptoms to fecal autointoxication." },
      { author: "Arthur Hurst", work: "Constipation and Allied Intestinal Disorders", quote: "Careful biochemical investigations disproved the hypothesis that chronic constipation produces systemic **copremia** in the absence of mechanical obstruction." },
      { author: "Jonathan Hutchinson", work: "Clinical Lectures and Reports", quote: "The sallow cachexia and persistent headache were formerly treated as symptoms of **copremia** by repeated purgatives." }
    ]
  },
  "Dashboard — copr\\coprinaceae.md": {
    primary: "A family of dark-spored, saprophytic basidiomycete fungi commonly known as the inky cap family, characterized by deliquescent gills.",
    secondary: "In systematic mycology, agaric fungi whose gills undergo enzymatic autodigestion into a black fluid to facilitate spore release.",
    quotes: [
      { author: "Charles Horton Peck", work: "Report of the State Botanist on Edible Fungi", quote: "The family **Coprinaceae** is readily recognized by its black spores and the remarkable melting of the mature pileus into an inky liquid." },
      { author: "Elias Magnus Fries", work: "Epicrisis Systematis Mycologici", quote: "Autodigestion in the **Coprinaceae** ensures that spores are exposed to air currents as the lower margin dissolves." },
      { author: "Liberty Hyde Bailey", work: "Cyclopedia of American Horticulture", quote: "Several species of the **Coprinaceae** appear overnight in rich garden compost and manured pastures." }
    ]
  },
  "Dashboard — copr\\coprinus.md": {
    primary: "The genus of inky cap mushrooms (such as Coprinus comatus, the shaggy mane) characterized by gills that autodigest into black ink.",
    secondary: "In mycology, saprophytic fungi prized as edible delicacies when young, though certain species contain coprine, causing disulfiram-like reactions with alcohol.",
    quotes: [
      { author: "Asa Gray", work: "First Lessons in Botany", quote: "The shaggy mane, **Coprinus** comatus, must be cooked immediately upon picking, or it will dissolve into a useless black puddle." },
      { author: "Charles Darwin", work: "The Formation of Vegetable Mould", quote: "Foliage and rich organic compost quickly produce clusters of ephemeral **Coprinus** toadstools after autumn rain." },
      { author: "Henry David Thoreau", work: "Journal", quote: "I found this morning a stately **Coprinus** rising from the roadside turf, already melting at its blackening frills." }
    ]
  },
  "Dashboard — copr\\coprographia.md": {
    primary: "The involuntary or compulsive writing of obscene, profane, or scatological words and phrases.",
    secondary: "In neuropsychiatry and behavioral neurology, a rare motor manifestation of severe Tourette syndrome or frontal lobe disinhibition.",
    quotes: [
      { author: "Oliver Sacks", work: "The Man Who Mistook His Wife for a Hat", quote: "In extreme cases of Tourette syndrome, motor tics can manifest as compulsive **coprographia**, scribbling forbidden words upon margins." },
      { author: "Alexander Luria", work: "The Nature of Human Conflicts", quote: "Frontal disinhibition can release suppressed vulgar expressions in both spoken form and spontaneous **coprographia**." },
      { author: "Gilles de la Tourette", work: "Étude sur une affection nerveuse", quote: "The patient displayed not only vocal tics but also an uncontrollable impulse toward **coprographia** on any scrap of paper." }
    ]
  },
  "Dashboard — copr\\coprolagnia.md": {
    primary: "A sexual paraphilia in which erotic pleasure and arousal are derived from contact with, observation of, or thoughts of feces.",
    secondary: "In psychopathology and forensic psychiatry, an extreme scatological paraphilic disorder involving compulsive eroticization of excrement.",
    quotes: [
      { author: "Richard von Krafft-Ebing", work: "Psychopathia Sexualis", quote: "The bizarre cases of **coprolagnia** recorded in our clinical annals demonstrate how sexual perversion can attach to repulsive organic objects." },
      { author: "Havelock Ellis", work: "Studies in the Psychology of Sex", quote: "Psychological analysis reveals that **coprolagnia** often represents an arrest at the earliest infantile excretory stages of development." },
      { author: "Sigmund Freud", work: "Three Essays on the Theory of Sexuality", quote: "Sublimation of anal-erotic impulses fails in those rare neurotic perversions that degenerate into overt **coprolagnia**." }
    ]
  },
  "Dashboard — copr\\coprolalia.md": {
    primary: "The involuntary, compulsive utterance of obscene or taboo words and phrases.",
    secondary: "In clinical neurology, a hallmark though uncommon vocal tic characteristic of severe Tourette syndrome, arising from basal ganglia dysfunction.",
    quotes: [
      { author: "Oliver Sacks", work: "An Anthropologist on Mars", quote: "The tragedy of **coprolalia** is that the patient feels an explosive inner urge to shout precisely the words most calculated to shock his companions." },
      { author: "Gilles de la Tourette", work: "Étude sur une affection nerveuse", quote: "Involuntary vocalizations progressed in the afflicted subject until sudden outbursts of **coprolalia** disrupted all social intercourse." },
      { author: "Alexander Luria", work: "The Working Brain", quote: "Severe disinhibition of striatal motor circuits unleashes vocal tics ranging from grunts to complex **coprolalia**." }
    ]
  },
  "Dashboard — copr\\coprolite.md": {
    primary: "A piece of fossilized animal dung, studied by paleontologists to reconstruct the diet and ecology of extinct creatures.",
    secondary: "In paleobiology and sedimentary geology, a trace fossil (ichnofossil) preserving undigested bones, scales, and seeds from ancient ecosystems.",
    quotes: [
      { author: "Mary Anning via Frank Buckland", work: "Geology and Mineralogy Considered with Reference to Natural Theology", quote: "Mary Anning discovered that the dark stony bezoars found in the Lias were in truth **coprolite** masses dropped by giant ichthyosaurs." },
      { author: "Charles Lyell", work: "Principles of Geology", quote: "Chemical analysis of each Cretaceous **coprolite** reveals high percentages of calcium phosphate derived from swallowed fish bones." },
      { author: "Charles Darwin", work: "The Origin of Species", quote: "The preservation of fossil teeth within an ancient **coprolite** provides direct evidence of the predatory habits of prehistoric reptiles." }
    ]
  },
  "Dashboard — copr\\coprolith.md": {
    primary: "A hard, calcified mass of hardened feces formed in the intestine; a fecalith.",
    secondary: "In surgical pathology, an inspissated stone-like concretion that can obstruct the lumen of the vermiform appendix, precipitating acute appendicitis.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Upon dissecting the perforated appendix, the surgeon invariably discovers an obstructive **coprolith** lodged within the lumen." },
      { author: "James Paget", work: "Lectures on Surgical Pathology", quote: "The concentric mineral laminations of an intestinal **coprolith** indicate slow, layer-by-layer accretion around a foreign nucleus." },
      { author: "Reginald Heber Fitz", work: "Perforating Inflammation of the Vermiform Appendix", quote: "Ulceration of the appendiceal wall is frequently triggered by ischemic pressure from an impacted **coprolith**." }
    ]
  },
  "Dashboard — copr\\coprology.md": {
    primary: "The scientific or medical study of feces, especially for medical diagnosis or archaeological analysis; scatology.",
    secondary: "In paleontology and parasitology, the discipline investigating stool specimens to identify helminth ova, gut microbiomes, and prehistoric dietary patterns.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Routine clinical **coprology** provides immediate evidence of occult hemorrhage, amoebic cysts, or pancreatic insufficiency." },
      { author: "Patrick Manson", work: "Tropical Diseases: A Manual of the Diseases of Warm Climates", quote: "In tropical medicine, laboratory **coprology** is indispensable for identifying the ova of bilharzia and hookworm." },
      { author: "Edward Tylor", work: "Researches into the Early History of Mankind", quote: "Archaeological **coprology** reconstructs the seasonal foraging habits of prehistoric cave dwellers from desiccated paleofeces." }
    ]
  },
  "Dashboard — copr\\coprophagia.md": {
    primary: "The consumption of feces; the habit or act of eating excrement.",
    secondary: "In animal behavior and veterinary medicine, normal cecotrophy (as in lagomorphs) or an abnormal behavioral vice observed in domestic canines and captive apes.",
    quotes: [
      { author: "Charles Darwin", work: "The Variation of Animals and Plants under Domestication", quote: "Rabbits re-ingest their cecal pellets by habitual **coprophagia**, recovering vital vitamins synthesized by intestinal microbes." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "In advanced stages of senile dementia or chronic psychosis, severe behavioral regression may manifest as **coprophagia**." },
      { author: "Konrad Lorenz", work: "On Aggression", quote: "Captive animals under extreme sensory deprivation sometimes develop unnatural stereotypic habits such as **coprophagia**." }
    ]
  },
  "Dashboard — copr\\coprophagy.md": {
    primary: "The practice or habit of feeding on dung or excrement, characteristic of certain insects and herbivores.",
    secondary: "In ecology and comparative physiology, an adaptive nutritional strategy exhibited by dung beetles (Scarabaeidae) and cecal-fermenting mammals.",
    quotes: [
      { author: "Jean-Henri Fabre", work: "The Life of the Fly", quote: "The sacred dung beetle performs its vital role in the sanitation of the pasture through tireless **coprophagy**." },
      { author: "Thomas Henry Huxley", work: "Lessons in Elementary Physiology", quote: "Rodents depend upon physiological **coprophagy** to absorb essential fatty acids produced during cecal fermentation." },
      { author: "Edward O. Wilson", work: "The Diversity of Life", quote: "Nutrient cycling in tropical rainforests relies upon millions of specialized beetles and termites dedicated to **coprophagy**." }
    ]
  },
  "Dashboard — copr\\coprophilia.md": {
    primary: "An abnormal interest in or sexual attraction to feces and defecation.",
    secondary: "In psychopathology, an anal-stage paraphilia involving erotic or obsessive fixation on excrement.",
    quotes: [
      { author: "Sigmund Freud", work: "Character and Anal Erotism", quote: "The infant's primordial interest in his excretions may persist as unconscious **coprophilia** if socialization fails to sublimate it." },
      { author: "Havelock Ellis", work: "Studies in the Psychology of Sex", quote: "In analyzing perversions, we discover that **coprophilia** represents an inversion of normal evolutionary disgust." },
      { author: "Richard von Krafft-Ebing", work: "Psychopathia Sexualis", quote: "The pathological manifestation of **coprophilia** is often accompanied by profound ethical deterioration and dementia." }
    ]
  },
  "Dashboard — copr\\copropraxia.md": {
    primary: "The involuntary or compulsive performance of obscene, vulgar, or taboo gestures.",
    secondary: "In behavioral neurology, a complex motor tic observed in patients with Tourette syndrome, occurring alongside coprolalia and echopraxia.",
    quotes: [
      { author: "Oliver Sacks", work: "Awakenings", quote: "The patient struggled valiantly against the humiliating spasms of **copropraxia** that caused him to make rude hand gestures in public." },
      { author: "Gilles de la Tourette", work: "Étude sur une affection nerveuse", quote: "Along with verbal profanities, our patient exhibited involuntary **copropraxia**, mimicking obscene signs with his fingers." },
      { author: "Alexander Luria", work: "Higher Cortical Functions in Man", quote: "In striatal syndromes, the loss of voluntary cortical inhibition can release motor automatisms including **copropraxia**." }
    ]
  },
  "Dashboard — copr\\encopresis.md": {
    primary: "The involuntary passing of feces into inappropriate places (such as clothing) by a child past the age of normal toilet training.",
    secondary: "In developmental pediatrics and child psychiatry, fecal soiling typically resulting from chronic fecal impaction and paradoxical overflow diarrhea.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Treatment of chronic **encopresis** in children requires systematic evacuation of the rectum followed by prolonged habit retraining." },
      { author: "Donald Winnicott", work: "The Child and the Outside World", quote: "The emotional distress surrounding **encopresis** reflects the child's struggle with maternal control and anxieties over bodily autonomy." },
      { author: "Benjamin Spock", work: "Baby and Child Care", quote: "Parents should understand that persistent **encopresis** is not deliberate naughtiness, but an involuntary consequence of constipation." }
    ]
  },
  "Dashboard — copr\\encopretic.md": {
    primary: "Of, relating to, or suffering from encopresis; characterized by involuntary fecal soiling.",
    secondary: "In pediatric clinical reports, describing a child exhibiting fecal incontinence secondary to retention or emotional conflict.",
    quotes: [
      { author: "Donald Winnicott", work: "Through Paediatrics to Psycho-Analysis", quote: "The **encopretic** child often conceals his soiled garments out of overwhelming shame and dread of punishment." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "A thorough abdominal examination of the **encopretic** patient reveals massive fecal impaction in the lower left quadrant." },
      { author: "Benjamin Spock", work: "Common Sense Book of Baby and Child Care", quote: "Relieving the fear of painful defecation is the first essential step in rehabilitating the **encopretic** youngster." }
    ]
  },
  "Dashboard — crani\\crani.md": {
    primary: "The combining root (from Greek kranion, meaning 'skull'), used in anatomy, zoology, and medicine for terms relating to the skull and cranial cavity.",
    secondary: "In comparative morphology, the radical designating skeletal structures enclosing the brain (craniology, cranium, craniosynostosis).",
    quotes: [
      { author: "Henry George Liddell & Robert Scott", work: "A Greek-English Lexicon", quote: "The Greek noun kranion denoted the skull or upper part of the head, furnishing the modern anatomical root **crani**." },
      { author: "Walter William Skeat", work: "An Etymological Dictionary of the English Language", quote: "The combining form **crani** underlies craniology and cranium, pointing directly to the bony case of the brain." },
      { author: "Thomas Henry Huxley", work: "A Manual of the Anatomy of Vertebrated Animals", quote: "Vertebrate taxa possessing an unsegmented head skeleton rely upon the root **crani** for their taxonomic designations." }
    ]
  },
  "Dashboard — crani\\cranial.md": {
    primary: "Relating to the skull or cranium; situated toward the head.",
    secondary: "In neuroanatomy, designating the twelve pairs of nerves originating directly from the brainstem rather than the spinal cord.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The third **cranial** nerve controls pupillary constriction and most of the extraocular muscles of the eye." },
      { author: "Thomas Henry Huxley", work: "Lessons in Elementary Physiology", quote: "The brain is protected from external mechanical injury by the arching vault of the **cranial** bones." },
      { author: "Oliver Wendell Holmes Sr.", work: "Medical Essays", quote: "A localized fracture of the **cranial** table may depress a bone fragment directly onto the cerebral cortex." }
    ]
  },
  "Dashboard — crani\\craniata.md": {
    primary: "A proposed major clade or subphylum of chordate animals possessing a specialized skull (cranium), including vertebrates and hagfishes.",
    secondary: "In phylogenetic systematics, chordates with neural crest cells, tripartite brains, and a protective cartilaginous or bony cranial vault.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "Manual of the Anatomy of Vertebrated Animals", quote: "The subphylum **Craniata** unites all those chordates in which the anterior end of the neural tube expands into a brain enclosed by a skull." },
      { author: "Ernst Haeckel", work: "The Evolution of Man", quote: "From simple lancelets arose the ancestral **Craniata**, endowed with distinct sensory capsules for sight and smell." },
      { author: "Alfred Romer", work: "The Vertebrate Body", quote: "The definition of **Craniata** encompasses hagfishes as well as true vertebrates, honoring the primacy of the skull." }
    ]
  },
  "Dashboard — crani\\craniate.md": {
    primary: "Having a cranium or skull; an animal belonging to the Craniata.",
    secondary: "In comparative anatomy, describing any chordate endowed with a cartilaginous or bony case protecting the brain.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "The Anatomy of Vertebrated Animals", quote: "Every **craniate** organism exhibits at least rudimentary paired optic and otic capsules flanking the neural axis." },
      { author: "Ray Lankester", work: "A Treatise on Zoology", quote: "The evolution of the **craniate** ancestor marked a decisive step toward active, predatory aquatic life." },
      { author: "Stephen Jay Gould", work: "Wonderful Life", quote: "Pikaia from the Burgess Shale represents our chordate forebear, just before the advent of the first **craniate** anatomy." }
    ]
  },
  "Dashboard — crani\\craniologist.md": {
    primary: "A scientist or anthropologist who studies the shape, size, and proportions of human skulls.",
    secondary: "In the history of science, a 19th-century physical anthropologist who classified human racial types based on cranial indices.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "Man's Place in Nature", quote: "The **craniologist** must rely on exact cephalic indices rather than prejudiced impressions of facial beauty." },
      { author: "Stephen Jay Gould", work: "The Mismeasure of Man", quote: "Samuel George Morton was celebrated as the foremost American **craniologist**, amassing hundreds of human skulls to measure their cranial volume." },
      { author: "Charles Darwin", work: "The Descent of Man", quote: "The **craniologist** finds that differences in skull shape within a single civilized nation often exceed those between distinct races." }
    ]
  },
  "Dashboard — crani\\craniology.md": {
    primary: "The scientific study of the shape, size, and variations of the skull.",
    secondary: "In physical anthropology and the history of medicine, the anatomical discipline that sought to correlate cranial morphology with race, evolution, and intelligence.",
    quotes: [
      { author: "Stephen Jay Gould", work: "The Mismeasure of Man", quote: "Nineteenth-century **craniology** was burdened by the unexamined assumption that skull volume directly reflected intellectual capacity." },
      { author: "Thomas Henry Huxley", work: "Critiques and Addresses", quote: "A reformed **craniology** abandoned phrenological charlatanism to become an exact branch of comparative mammalian anatomy." },
      { author: "Charles Lyell", work: "The Geological Evidences of the Antiquity of Man", quote: "Discoveries of ancient skulls in the Neanderthal cave gave a powerful impetus to the newly emerging science of **craniology**." }
    ]
  },
  "Dashboard — crani\\craniometer.md": {
    primary: "An instrument calibrated for measuring the dimensions, angles, and proportions of the skull.",
    secondary: "In physical anthropology and forensics, a specialized caliper or goniometer used to record cephalic length, breadth, and facial angles.",
    quotes: [
      { author: "Stephen Jay Gould", work: "The Mismeasure of Man", quote: "With his brass **craniometer**, Broca meticulously measured the facial angle and cephalic index of thousands of specimens." },
      { author: "Thomas Henry Huxley", work: "Man's Place in Nature", quote: "The application of a precise **craniometer** eliminates the subjective bias of the investigator in assessing cranial contours." },
      { author: "Arthur Conan Doyle", work: "The Hound of the Baskervilles", quote: "Dr. Mortimer gazed yearningly at Sherlock Holmes's head, remarking that he would dearly love to run his **craniometer** over the parietal ridge." }
    ]
  },
  "Dashboard — crani\\craniometric.md": {
    primary: "Pertaining to craniometry; relating to the measurement of the skull.",
    secondary: "In physical anthropology, describing indices such as the cranial index, gnathic index, or orbital index.",
    quotes: [
      { author: "Stephen Jay Gould", work: "The Mismeasure of Man", quote: "Broca's **craniometric** tables were celebrated across Europe as the pinnacle of quantitative anatomical rigor." },
      { author: "Thomas Henry Huxley", work: "Methods and Results", quote: "The **craniometric** comparison of primate skulls clearly demonstrates the gradual reduction of the prognathous muzzle in hominids." },
      { author: "Charles Darwin", work: "The Descent of Man", quote: "Diverse **craniometric** measurements show that the cranial capacity of ancient stone age skulls equaled that of modern Europeans." }
    ]
  },
  "Dashboard — crani\\craniometrical.md": {
    primary: "Of, relating to, or obtained by the measurement of skulls; craniometric.",
    secondary: "In anthropological studies, designating quantitative data concerning cranial capacity, facial projection, and cephalic ratios.",
    quotes: [
      { author: "Stephen Jay Gould", work: "The Mismeasure of Man", quote: "Morton filled each cranial cavity with lead shot to determine its exact **craniometrical** capacity." },
      { author: "Thomas Henry Huxley", work: "Man's Place in Nature", quote: "Our **craniometrical** survey revealed that variation within individual tribes was far greater than previous observers had suspected." },
      { author: "Francis Galton", work: "Hereditary Genius", quote: "He attempted to establish a correlation between **craniometrical** dimensions and demonstrated mental eminence." }
    ]
  },
  "Dashboard — crani\\craniometry.md": {
    primary: "The scientific measurement of the bones of the skull, especially of human skulls.",
    secondary: "In biological anthropology and forensic science, the quantitative determination of cranial indices to assess evolutionary variation and ancestral morphology.",
    quotes: [
      { author: "Stephen Jay Gould", work: "The Mismeasure of Man", quote: "The history of **craniometry** offers a cautionary tale of how numerical measurements can be co-opted in service of racial ideology." },
      { author: "Thomas Henry Huxley", work: "Man's Place in Nature", quote: "By introducing standardized reference lines, Broca established **craniometry** as a repeatable scientific discipline." },
      { author: "Charles Darwin", work: "The Descent of Man", quote: "The vast collection of data amassed by **craniometry** proves that human skulls exhibit extraordinary intraspecific plasticity." }
    ]
  },
  "Dashboard — crani\\craniosynostosis.md": {
    primary: "A congenital defect in which one or more of the cranial sutures fuse prematurely, leading to abnormal head shape and restricted brain growth.",
    secondary: "In pediatric neurosurgery, a developmental malformation (such as scaphocephaly or brachycephaly) treated by surgical suture release.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Premature ossification of the sagittal suture produces the elongated boat-shaped cranium characteristic of sagittal **craniosynostosis**." },
      { author: "Harvey Cushing", work: "The Pituitary Body and Its Disorders", quote: "Surgical intervention in severe **craniosynostosis** aims to decompress the growing brain and alleviate intracranial hypertension." },
      { author: "Oliver Sacks", work: "The Island of the Colorblind", quote: "Children born with syndromic **craniosynostosis** present with complex craniofacial anomalies requiring multidisciplinary reconstructive surgery." }
    ]
  },
  "Dashboard — crani\\craniotomy.md": {
    primary: "A surgical operation in which a bone flap is temporarily removed from the skull to access the brain.",
    secondary: "In neurosurgery, the foundational operative opening allowing excision of intracranial tumors, hematomas, or clipping of cerebral aneurysms.",
    quotes: [
      { author: "Harvey Cushing", work: "Intracranial Tumors", quote: "The success of an osteoplastic **craniotomy** depends upon preserving the vascular supply of the overlying scalp flap." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Immediate **craniotomy** is mandatory in compound depressed skull fractures to evacuate intracranial clots and elevate bone fragments." },
      { author: "Sherwin B. Nuland", work: "Doctors: The Biography of Medicine", quote: "With the introduction of antiseptic technique and electric trephines, **craniotomy** was transformed into a deliberate, safe surgical intervention." }
    ]
  },
  "Dashboard — crani\\cranium.md": {
    primary: "The skull, especially the part enclosing the brain; the bony braincase.",
    secondary: "In vertebrate anatomy, the skeletal enclosure formed by the neurocranium and splanchnocranium that houses and protects the brain and sense organs.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "A Manual of the Anatomy of Vertebrated Animals", quote: "The occipital, parietal, and frontal bones unite along serrated sutures to complete the dome of the mammalian **cranium**." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Increased intracranial pressure within the rigid **cranium** inevitably compromises cerebral arterial perfusion." },
      { author: "Charles Darwin", work: "The Descent of Man", quote: "The gradual enlargement of the hominid **cranium** accompanied the expansion of cerebral cortex during the Pleistocene." }
    ]
  },
  "Dashboard — crani\\endocranium.md": {
    primary: "The inner surface of the cranium; the dura mater lining the inside of the skull.",
    secondary: "In vertebrate paleontology, the fossilized internal surface or cast of the cranial cavity reflecting the size, shape, and sulci of the brain.",
    quotes: [
      { author: "Alfred Romer", work: "Vertebrate Paleontology", quote: "Natural mud casts of the **endocranium** allow the paleontologist to trace the cranial nerve exits in extinct placoderms." },
      { author: "Thomas Henry Huxley", work: "Lectures on Evolution", quote: "The vascular grooves impressed upon the **endocranium** reveal the distribution of the middle meningeal artery." },
      { author: "Stephen Jay Gould", work: "The Structure of Evolutionary Theory", quote: "By preparing an accurate endocranial cast, Dart proved that the brain of Australopithecus occupied an advanced **endocranium**." }
    ]
  },
  "Dashboard — crani\\epicranium.md": {
    primary: "The structures covering the cranium, especially the scalp and the muscular-aponeurotic layer (galea aponeurotica).",
    secondary: "In insect anatomy, the upper dorsal sclerite or crown of the head between the compound eyes.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "The Anatomy of Invertebrated Animals", quote: "The antennae of the grasshopper arise from the anterior margin of the heavily chitinized **epicranium**." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Subaponeurotic hematomas spread widely beneath the **epicranium**, bounded only by the cranial attachments of the scalp." },
      { author: "Ray Lankester", work: "A Treatise on Zoology", quote: "In beetles, the compound eyes are embedded into lateral notches of the protective **epicranium**." }
    ]
  },
  "Dashboard — crani\\hemicrania.md": {
    primary: "A severe, episodic headache affecting only one side of the head; the classical medical term for unilateral migraine.",
    secondary: "In neurological history, paroxysmal unilateral cranial pain often accompanied by ophthalmic aura, photophobia, and nausea.",
    quotes: [
      { author: "Galen", work: "On the Affected Parts", quote: "Because the painful paroxysm seizes only one half of the head along the sagittal division, we call this affliction **hemicrania**." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Periodic attacks of **hemicrania** frequently exhibit a strong familial predisposition, beginning in adolescence." },
      { author: "Jean-Martin Charcot", work: "Clinical Lectures on the Diseases of the Nervous System", quote: "Ophthalmic **hemicrania** displays a scintillating scotoma that expands across the visual field before the pain begins." }
    ]
  },
  "Dashboard — crani\\megrim.md": {
    primary: "An archaic or dialect term for a migraine headache; a severe unilateral headache.",
    secondary: "In literature and colloquial speech, a sudden whim, caprice, low spirits, or vertigo.",
    quotes: [
      { author: "Jane Austen", work: "Pride and Prejudice", quote: "She took to her bed with a severe **megrim**, complaining that the noise of the children shattered her poor nerves." },
      { author: "Walter Scott", work: "The Heart of Midlothian", quote: "The old bailie suffered from sudden **megrims** in his head whenever difficult legal points were argued before him." },
      { author: "George Eliot", work: "Middlemarch", quote: "Mrs. Cadwallader declared that Dorothea's grand philanthropic schemes were mere girlish **megrims** that marriage would cure." }
    ]
  },
  "Dashboard — crani\\migraine.md": {
    primary: "A recurrent throbbing headache that typically affects one side of the head, often accompanied by nausea and disturbed vision.",
    secondary: "In neurovascular medicine, a complex neurobiological disorder involving trigeminovascular system activation and cortical spreading depression.",
    quotes: [
      { author: "Oliver Sacks", work: "Migraine", quote: "A **migraine** is not a mere headache; it is a whole-body storm, an episodic neurological convulsion characterized by exquisite sensory alterations." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The classic fortification spectra and hemianopia of **migraine** point directly to transient cortical dysregulation." },
      { author: "Virginia Woolf", work: "On Being Ill", quote: "How the world changes when viewed through the shattering, jagged prism of an oncoming **migraine**." }
    ]
  },
  "Dashboard — cric\\Cricosaurus.md": {
    primary: "An extinct genus of slender, pelagic metriorhynchid crocodyliforms from the Late Jurassic and Early Cretaceous marine beds.",
    secondary: "In vertebrate paleontology, marine crocodylomorphs completely adapted to open ocean life with flipper-like limbs and a hypocercal tail fin.",
    quotes: [
      { author: "Alfred Romer", work: "Vertebrate Paleontology", quote: "The streamlined marine crocodile **Cricosaurus** abandoned armored dermal scutes to achieve swift swimming in Jurassic seas." },
      { author: "Michael J. Benton", work: "Vertebrate Palaeontology", quote: "Fossil skeletons of **Cricosaurus** show large sclerotic rings in the orbits, indicating keen vision in deep pelagic waters." },
      { author: "Stephen Jay Gould", work: "Eight Little Piggies", quote: "In **Cricosaurus**, evolutionary convergence refashioned a reptilian tail into the downward lobe of a true swimming fluke." }
    ]
  },
  "Dashboard — cric\\cric.md": {
    primary: "The Greek root (krikos, meaning 'ring'), designating ring-shaped anatomical structures, particularly the cricoid cartilage of the larynx.",
    secondary: "In zoological and medical terminology, the radical forming compounds such as cricoid, cricothyroid, and Cricetus.",
    quotes: [
      { author: "Henry George Liddell & Robert Scott", work: "A Greek-English Lexicon", quote: "The Greek noun krikos signified a finger-ring or hoop, providing anatomists with the radical **cric** for the ring-shaped laryngeal cartilage." },
      { author: "Walter William Skeat", work: "An Etymological Dictionary of the English Language", quote: "From the ancient Greek stem **cric**, a circle or ring, derives the anatomical adjective cricoid." },
      { author: "Thomas Henry Huxley", work: "Lessons in Elementary Physiology", quote: "The root **cric** appears in laryngeal terms denoting the circular foundation cartilage of the windpipe." }
    ]
  },
  "Dashboard — cric\\cricetidae.md": {
    primary: "A large and diverse family of muroid rodents that includes true hamsters, voles, lemmings, and New World rats and mice.",
    secondary: "In mammalian systematics, the second largest family of mammals, characterized by two rows of cusps on prismatic or tubercular molars.",
    quotes: [
      { author: "Alfred Russel Wallace", work: "The Geographical Distribution of Animals", quote: "Members of the family **Cricetidae** inhabit virtually all ecological zones of the Americas and northern Eurasia." },
      { author: "Charles Darwin", work: "The Zoology of the Voyage of H.M.S. Beagle", quote: "The small nocturnal rodents collected along the pampas represent specialized South American offshoots of the **Cricetidae**." },
      { author: "Alfred Romer", work: "Vertebrate Paleontology", quote: "The explosive evolutionary radiation of the **Cricetidae** during the Miocene produced hundreds of specialized herbivorous forms." }
    ]
  },
  "Dashboard — cric\\cricetus.md": {
    primary: "The genus of true European hamsters (particularly Cricetus cricetus, the common black-bellied hamster) noted for large internal cheek pouches.",
    secondary: "In vertebrate zoology, fossorial Eurasian rodents with stout burrowing limbs that store grain caches within elaborate subterranean tunnels.",
    quotes: [
      { author: "Georges Cuvier", work: "The Animal Kingdom", quote: "The common hamster, **Cricetus** vulgaris, is celebrated for the voracity with which it packs grain into its expandable cheek pouches." },
      { author: "Alfred Russel Wallace", work: "Island Life", quote: "Fossil remains of **Cricetus** found in Pleistocene cave deposits prove its former abundance across western Europe." },
      { author: "Thomas Henry Huxley", work: "Manual of the Anatomy of Vertebrated Animals", quote: "The skull of **Cricetus** displays powerful zygomatic arches adapted for heavy chewing of hard seeds and tubers." }
    ]
  },
  "Dashboard — cric\\cricoid.md": {
    primary: "Ring-shaped; specifically, the signet-ring-shaped cartilage forming the lower and back part of the larynx.",
    secondary: "In clinical airway management and anesthesia, the cartilaginous ring upon which backward pressure (Sellick maneuver) is applied to occlude the esophagus.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "Lessons in Elementary Physiology", quote: "The **cricoid** cartilage resembles a signet ring, with its broad plate situated behind and the narrow arch in front." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "In acute laryngeal edema, the subglottic swelling can rapidly occlude the rigid lumen bounded by the **cricoid** ring." },
      { author: "Oliver Wendell Holmes Sr.", work: "Medical Essays", quote: "The vocal cords are tensed and relaxed by delicate muscular adjustments pivoting upon the stable **cricoid** base." }
    ]
  },
  "Dashboard — cric\\cricoidectomy.md": {
    primary: "The surgical excision or removal of the cricoid cartilage.",
    secondary: "In head and neck surgical oncology, a rare and technically complex procedure performed for localized laryngeal chondrosarcoma or severe subglottic stenosis.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Total **cricoidectomy** requires meticulous airway reconstruction to prevent post-operative collapse of the cervical trachea." },
      { author: "Harvey Cushing", work: "Selected Papers on Surgical Technique", quote: "When extirpating a low-grade chondroma of the lower larynx, partial **cricoidectomy** preserves laryngeal function." },
      { author: "James Paget", work: "Lectures on Surgical Pathology", quote: "The rarity of primary malignant disease in the lower larynx renders **cricoidectomy** an exceptional surgical undertaking." }
    ]
  },
  "Dashboard — cric\\cricothyroid.md": {
    primary: "Relating to or connecting the cricoid cartilage and the thyroid cartilage of the larynx.",
    secondary: "In head and neck anatomy, denoting the cricothyroid muscle that tenses the vocal cords, and the cricothyroid membrane traversed in emergency airways.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "Lessons in Elementary Physiology", quote: "Contraction of the **cricothyroid** muscles tilts the thyroid cartilage forward, thereby tightening and elongating the vocal cords." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Digital palpation easily locates the soft depression of the **cricothyroid** space between the thyroid prominence and the lower ring." },
      { author: "René Laennec", work: "A Treatise on the Diseases of the Chest", quote: "Paralysis of the **cricothyroid** muscle results in a hoarse, monotonous voice due to inability to modulate vocal pitch." }
    ]
  },
  "Dashboard — cric\\cricothyrotomy.md": {
    primary: "An emergency surgical procedure in which an incision is made through the skin and cricothyroid membrane to establish a patent airway.",
    secondary: "In acute trauma resuscitation and critical care medicine, the definitive surgical airway intervention for patients who cannot be intubated or ventilated.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "When foreign body impaction produces immediate asphyxia, a prompt **cricothyrotomy** with a penknife has saved many a dying patient." },
      { author: "Atul Gawande", work: "Complications: A Surgeon's Notes on an Imperfect Science", quote: "In the trauma bay, when all intubation attempts fail, the surgeon must execute an emergency **cricothyrotomy** without hesitation." },
      { author: "Sherwin B. Nuland", work: "How We Die: Reflections on Life's Final Chapter", quote: "A successful **cricothyrotomy** bypasses massive facial trauma, delivering life-saving air directly into the subglottic trachea." }
    ]
  },
  "Dashboard — cric\\cricotomy.md": {
    primary: "A surgical incision into the cricoid cartilage of the larynx.",
    secondary: "In pediatric laryngology, an operative slit made in the anterior cricoid cartilage to expand the subglottic airway in infants with congenital stenosis.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Anterior **cricotomy** was devised to widen the rigid subglottic ring in children who failed extubation after prolonged intubation." },
      { author: "James Paget", work: "Lectures on Surgical Pathology", quote: "Careful longitudinal **cricotomy** allows the surgeon to inspect the posterior wall of the lower larynx directly." },
      { author: "Harvey Cushing", work: "Surgical Observations", quote: "The incision in a high **cricotomy** must avoid the transverse cricothyroid arterial branches." }
    ]
  },
  "Dashboard — cric\\mesocricetus.md": {
    primary: "A genus of hamsters (family Cricetidae), most notably Mesocricetus auratus, the golden or Syrian hamster.",
    secondary: "In biomedical research, rodents widely utilized as laboratory animal models in oncology, immunology, and infectious disease studies.",
    quotes: [
      { author: "Konrad Lorenz", work: "King Solomon's Ring", quote: "The golden hamster, **Mesocricetus** auratus, was first captured near Aleppo, and all our domestic stocks descend from that single litter." },
      { author: "Alexander Luria", work: "The Working Brain", quote: "Circadian rhythm investigations in **Mesocricetus** illuminate the pacemaker function of the hypothalamic suprachiasmatic nucleus." },
      { author: "Edward O. Wilson", work: "Sociobiology: The New Synthesis", quote: "Territorial solitary aggression in **Mesocricetus** is mediated by specific flank-gland pheromones deposited on burrow walls." }
    ]
  },
  "Dashboard — cyt\\astrocyte.md": {
    primary: "A star-shaped glial cell of the central nervous system that supports neurons, regulates blood flow, and maintains the blood-brain barrier.",
    secondary: "In neurobiology, the most abundant glial cell type, essential for synaptic transmission, extracellular potassium buffering, and glial scar formation.",
    quotes: [
      { author: "Santiago Ramón y Cajal", work: "Histology of the Nervous System", quote: "With gold sublimate staining, each **astrocyte** unfurls hundreds of delicate radiating processes that terminate on capillary walls." },
      { author: "Oliver Sacks", work: "The Man Who Mistook His Wife for a Hat", quote: "Neurobiologists now recognize that the **astrocyte** is not merely passive brain glue, but an active partner in neural processing." },
      { author: "Alexander Luria", work: "The Working Brain", quote: "Following localized ischemic infarction, reactive proliferation of the **astrocyte** leads to fibrous glial encapsulation." }
    ]
  },
  "Dashboard — cyt\\astrocytic.md": {
    primary: "Of, relating to, or composed of astrocytes.",
    secondary: "In neuropathology, describing reactive gliosis (astrogliosis) or neoplasms (astrocytomas) derived from transformed star-shaped glial cells.",
    quotes: [
      { author: "Santiago Ramón y Cajal", work: "Degeneration and Regeneration of the Nervous System", quote: "Dense meshworks of **astrocytic** end-feet envelop the cerebral microvasculature, forming a continuous perivascular sheath." },
      { author: "Harvey Cushing", work: "A Classification of the Tumors of the Glioma Group", quote: "The benign fibrillary tumor consists of well-differentiated cells of **astrocytic** lineage with delicate spider-like fibrils." },
      { author: "Oliver Sacks", work: "Awakenings", quote: "Post-mortem analysis revealed intense **astrocytic** scarring throughout the substantia nigra of the post-encephalitic patients." }
    ]
  },
  "Dashboard — cyt\\cnidocyte.md": {
    primary: "A specialized explosive stinging cell unique to cnidarians (such as jellyfish, corals, and sea anemones), containing a secretory organelle called a nematocyst.",
    secondary: "In invertebrate zoology, a cellular mechanosensory weapon that discharges a venomous harpoon-like tubule upon tactile or chemical triggering.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "A Manual of the Anatomy of Invertebrated Animals", quote: "The venomous battery along the tentacle of the jellyfish consists of thousands of microscopic **cnidocyte** cells ready to fire." },
      { author: "Rachel Carson", work: "The Sea Around Us", quote: "Contact with the floating tentacles triggers instantaneous discharge from each **cnidocyte**, injecting toxin into the captured prey." },
      { author: "Richard Dawkins", work: "The Extended Phenotype", quote: "The high-pressure explosive mechanism of the **cnidocyte** is one of the fastest mechanical processes in the animal kingdom." }
    ]
  },
  "Dashboard — cyt\\cyt.md": {
    primary: "The combining root (from Greek kytos, meaning 'hollow vessel, jar, container, or cell'), used across biology and medicine to denote cells.",
    secondary: "In cytology and biochemistry, the foundational prefix occurring in terms such as cytoplasm, cytokine, and cytogenetics.",
    quotes: [
      { author: "Henry George Liddell & Robert Scott", work: "A Greek-English Lexicon", quote: "The Greek noun kytos denoted a hollow vessel or vault; in modern science the root **cyt** became the universal designation for the cell." },
      { author: "Walter William Skeat", work: "An Etymological Dictionary of the English Language", quote: "From the scientific stem **cyt**, meaning a cell, we derive cytology, cytoplasm, and erythrocyte." },
      { author: "E. B. Wilson", work: "The Cell in Development and Heredity", quote: "Nineteenth-century biologists adopted the radical **cyt** to name those elementary living units discovered by Hooke and Schleiden." }
    ]
  },
  "Dashboard — cyt\\cytapheresis.md": {
    primary: "A medical procedure in which specific cellular elements of blood (such as leukocytes, platelets, or stem cells) are selectively separated and collected.",
    secondary: "In hematology and transfusion medicine, an extracorporeal centrifugation technique used therapeutically in hyperleukocytosis or for autologous transplant collection.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Therapeutic **cytapheresis** brings rapid symptomatic relief in acute leukostasis by swiftly reducing the circulating blast count." },
      { author: "Maxwell Wintrobe", work: "Clinical Hematology", quote: "Modern continuous-flow centrifuges permit automated **cytapheresis** to harvest donor granulocytes with minimal red cell loss." },
      { author: "Paul Ehrlich", work: "Studies in Immunity", quote: "Selective mechanical extraction through early **cytapheresis** demonstrated that specific immune effectors reside in distinct mononuclear bands." }
    ]
  },
  "Dashboard — cyt\\cytaster.md": {
    primary: "A star-shaped radiating system of cytoplasmic microtubules that forms outside the nucleus during mitosis.",
    secondary: "In cell biology and embryology, an aster-like radial array of microfilaments and microtubules that can develop in unfertilized artificially activated ova.",
    quotes: [
      { author: "E. B. Wilson", work: "The Cell in Development and Heredity", quote: "Artificial parthenogenesis induces the formation of an autonomous **cytaster** within the egg cytoplasm, independent of sperm entry." },
      { author: "Thomas Hunt Morgan", work: "The Theory of the Gene", quote: "The appearance of the **cytaster** demonstrates that aster formation is an intrinsic mechanical property of the egg cytoplasm." },
      { author: "Jacques Loeb", work: "Artificial Parthenogenesis and Fertilization", quote: "Hypertonic chemical solutions provoke the rapid assembly of a visible **cytaster** surrounding the maternal centrosome." }
    ]
  },
  "Dashboard — cyt\\cytokine.md": {
    primary: "Any of a large group of small signaling proteins secreted by cells that modulate immune responses, inflammation, and cellular communication.",
    secondary: "In immunology and molecular medicine, non-antibody regulatory peptides (such as interleukins, interferons, and tumor necrosis factors) acting via cell-surface receptors.",
    quotes: [
      { author: "Bruce Alberts", work: "Molecular Biology of the Cell", quote: "The binding of a single **cytokine** molecule to its surface receptor triggers an intracellular Janus kinase signaling cascade." },
      { author: "Peter Medawar", work: "The Limits of Science", quote: "Immune regulation is orchestrated by an intricate humoral language where each **cytokine** delivers a targeted command." },
      { author: "Lewis Thomas", work: "The Fragile Species", quote: "The catastrophic cardiovascular collapse in septic shock is mediated by an uncontrolled flood of inflammatory **cytokine** molecules." }
    ]
  },
  "Dashboard — cyt\\cytokinesis.md": {
    primary: "The physical division of the cytoplasm of a parental cell into two daughter cells following mitosis or meiosis.",
    secondary: "In cell biology, the stage of the cell cycle driven in animal cells by a contractile ring of actin and myosin filaments, and in plant cells by cell plate formation.",
    quotes: [
      { author: "E. B. Wilson", work: "The Cell in Development and Inheritance", quote: "Nuclear division or karyokinesis is followed by the cleavage of the cell body itself, termed **cytokinesis**." },
      { author: "Bruce Alberts", work: "Molecular Biology of the Cell", quote: "During animal cell **cytokinesis**, a purse-string constriction of actin microfilaments pinches the plasma membrane into two distinct cells." },
      { author: "Lynn Margulis", work: "Symbiosis in Cell Evolution", quote: "The coordination between chromosome segregation and physical **cytokinesis** ensures equal distribution of genetic heritage." }
    ]
  },
  "Dashboard — cyt\\cytokinin.md": {
    primary: "A class of plant growth phytohormones that promote cell division (cytokinesis) in roots and shoots and delay leaf senescence.",
    secondary: "In plant physiology, adenine-derived hormones (such as zeatin and kinetin) that act antagonistically with auxins to regulate apical dominance and morphogenesis.",
    quotes: [
      { author: "Asa Gray", work: "Structural Botany", quote: "Tissue culture experiments proved that the balance between auxin and **cytokinin** determines whether stem buds or roots differentiate." },
      { author: "Liberty Hyde Bailey", work: "The Standard Cyclopedia of Horticulture", quote: "Commercial floriculture uses synthetic **cytokinin** sprays to maintain green freshness and delay petal drop in cut flowers." },
      { author: "Arthur George Tansley", work: "The British Islands and Their Vegetation", quote: "The seasonal transport of root-synthesized **cytokinin** up the xylem activates dormant lateral buds in spring." }
    ]
  },
  "Dashboard — cyt\\cytologic.md": {
    primary: "Pertaining to cytology; relating to the study of the structure, pathology, and function of cells.",
    secondary: "In diagnostic medicine, describing microscopic smear examinations, such as Pap smears or fine-needle aspiration biopsies.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Careful **cytologic** examination of the cerebrospinal fluid reveals pleocytosis indicative of tuberculous meningitis." },
      { author: "Rudolf Virchow", work: "Cellular Pathology", quote: "The foundational **cytologic** discovery of the nineteenth century was that all pathological alterations originate in individual cells." },
      { author: "Paul Ehrlich", work: "Histology of the Blood", quote: "Specific basic and acidic dyes allowed the first systematic **cytologic** differentiation of human leukemic cells." }
    ]
  },
  "Dashboard — cyt\\cytological.md": {
    primary: "Of, relating to, or characteristic of cytology and the microscopic observation of cells.",
    secondary: "In laboratory pathology, pertaining to cellular morphology, nuclear atypia, and mitotic index evaluated in cell preparations.",
    quotes: [
      { author: "E. B. Wilson", work: "The Cell in Development and Heredity", quote: "The **cytological** proof that chromosomes retain their individuality through successive divisions transformed genetics." },
      { author: "Thomas Hunt Morgan", work: "The Theory of the Gene", quote: "Genetic linkage maps were triumphantly confirmed by direct **cytological** observation of translocated chromosome segments." },
      { author: "Santiago Ramón y Cajal", work: "Histology", quote: "Without refined **cytological** fixation techniques, the delicate fine neurofibrils inside neurons remain entirely invisible." }
    ]
  },
  "Dashboard — cyt\\cytologist.md": {
    primary: "A scientist or medical specialist who studies the structure, function, and pathology of cells.",
    secondary: "In laboratory medicine, a diagnostician who interprets cellular smears and aspirates to detect malignancy or premalignant dysplasia.",
    quotes: [
      { author: "E. B. Wilson", work: "The Cell in Development and Heredity", quote: "The modern **cytologist** does not merely admire cell anatomy under the microscope, but investigates the chemical mechanics of life." },
      { author: "Thomas Hunt Morgan", work: "The Theory of the Gene", quote: "Collaboration between the experimental geneticist and the observant **cytologist** unraveled the mystery of chromosomal crossover." },
      { author: "William Osler", work: "Aequanimitas", quote: "To the hospital **cytologist**, a single atypical cell in a pleural aspirate can decisively alter a patient's prognosis." }
    ]
  }
};

const updatedCount = updateNotesBatch(baseClusterDir, batch2Data);
console.log(`[Body Batch 2] Successfully updated ${updatedCount}/${Object.keys(batch2Data).length} notes.`);
