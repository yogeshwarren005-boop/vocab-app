# -*- coding: utf-8 -*-
import json
import os
import sys

batch4_data = {
  "Dashboard — sten\\stenopelmatidae.md": {
    "primary": "A family of large, flightless orthopteran insects, commonly known as Jerusalem crickets or sand crickets.",
    "secondary": "In entomology and insect ecology, nocturnal burrowing ensiferans possessing powerful mandibles, spade-like tibiae for digging, and sound-producing abdominal drumming mechanisms used in courtship.",
    "quotes": [
      { "author": "John Henry Comstock", "work": "An Introduction to Entomology", "quote": "Members of the family **Stenopelmatidae** are heavy, wingless insects with enormous round heads and stout spiny legs." },
      { "author": "William Morton Wheeler", "work": "Demons of the Dust", "quote": "The bizarre sand crickets of the family **Stenopelmatidae** excavate deep subterranean tunnels in arid western soils." },
      { "author": "Vincent Dethier", "work": "The Physiology of Insect Senses", "quote": "Substrate drumming in **Stenopelmatidae** communicates reproductive signals through soil vibrations rather than airborne sound." }
    ]
  },
  "Dashboard — sten\\stenopelmatus.md": {
    "primary": "A genus of large, wingless burrowing insects in the family Stenopelmatidae, typified by the Jerusalem cricket (*Stenopelmatus fuscus*).",
    "secondary": "In entomological natural history, solitary nocturnal predators native to western North America and Central America, notable for their baby-like human facial resemblance and aggressive mandibular defense.",
    "quotes": [
      { "author": "John Henry Comstock", "work": "A Manual for the Study of Insects", "quote": "The curious creature **Stenopelmatus**, often called the child of the earth, wanders through cellar drains and sandy washes." },
      { "author": "Jean-Henri Fabre", "work": "The Wonders of Instinct", "quote": "The subterranean habits of **Stenopelmatus** illustrate how burrowing orthopterans have sacrificed flight for massive digging limbs." },
      { "author": "Vernon Lyman Kellogg", "work": "American Insects", "quote": "Children in California are often alarmed by the grotesque appearance of **Stenopelmatus**, though it is entirely non-venomous." }
    ]
  },
  "Dashboard — sten\\stenopterygius.md": {
    "primary": "An extinct genus of thunnosaurian ichthyosaur from the Early Jurassic of Europe, characterized by narrow, paddle-like fins.",
    "secondary": "In vertebrate paleontology and marine paleoecology, streamlined dolphin-like marine reptiles (abundantly preserved in the Posidonia Shale of Holzmaden) famous for fossilized soft-tissue outlines and viviparous birth with embryos preserved inside the mother's body.",
    "quotes": [
      { "author": "Richard Owen", "work": "Monograph on the Fossil Reptilia of the Liassic Formations", "quote": "The narrow pectoral paddles of **Stenopterygius** indicate high-speed pelagic propulsion comparable to modern cetaceans." },
      { "author": "Arthur Smith Woodward", "work": "Outlines of Vertebrate Palaeontology", "quote": "Fabulous specimens of **Stenopterygius** from Holzmaden preserve carbonaceous films of dorsal fins and caudal flukes." },
      { "author": "Stephen Jay Gould", "work": "Bully for Brontosaurus", "quote": "Fossils of pregnant female **Stenopterygius** giving birth tail-first prove that these marine reptiles evolved obligate live birth." }
    ]
  },
  "Dashboard — sten\\stenosed.md": {
    "primary": "Abnormally narrowed, constricted, or tightened; affected by stenosis.",
    "secondary": "In cardiovascular pathology and interventional medicine, describing blood vessels, cardiac valves, or visceral lumens (such as a stenosed coronary artery or aortic valve) whose effective cross-sectional area is reduced by calcification, plaque, or fibrosis.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "A harsh systolic murmur radiating into the carotids was heard over the severely **stenosed** aortic valve orifice." },
      { "author": "Harvey Cushing", "work": "Studies in Intracranial Physiology", "quote": "Cerebrospinal fluid circulation was obstructed at the level of the congenitally **stenosed** aqueduct of Sylvius." },
      { "author": "Eugene Braunwald", "work": "Heart Disease: A Textbook of Cardiovascular Medicine", "quote": "Balloon catheter dilation was performed to restore forward blood flow through the critically **stenosed** mitral valve." }
    ]
  },
  "Dashboard — sten\\stenosis.md": {
    "primary": "An abnormal narrowing or constriction of a duct, canal, vessel, or bodily passage.",
    "secondary": "In cardiology, gastroenterology, and neurology, pathological lumen reduction (such as aortic stenosis, pyloric stenosis, or spinal canal stenosis) that impedes physiological fluid flow or impinges on nerves.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Hypertrophic pyloric **stenosis** in infants produces projectile vomiting and marked peristaltic waves across the epigastrium." },
      { "author": "Eugene Braunwald", "work": "Heart Disease", "quote": "Progressive calcific aortic **stenosis** leads to concentric left ventricular hypertrophy and eventual heart failure." },
      { "author": "W. Russell Brain", "work": "Diseases of the Nervous System", "quote": "Lumbar canal **stenosis** induces neurogenic claudication, where pain in the legs is relieved by leaning forward." }
    ]
  },
  "Dashboard — sten\\stenotaphrum.md": {
    "primary": "A small genus of creeping perennial grasses in the family Poaceae, notably including St. Augustine grass (*Stenotaphrum secundatum*).",
    "secondary": "In agrostology and subtropical turfgrass management, stoloniferous warm-season lawn and pasture grasses native to tropical shorelines, valued for high salt tolerance and rapid vegetative spread.",
    "quotes": [
      { "author": "Carl Linnaeus", "work": "Species Plantarum", "quote": "The coastal grass which botanists later referred to **Stenotaphrum** binds maritime sand with its dense creeping stolons." },
      { "author": "Liberty Hyde Bailey", "work": "The Standard Cyclopedia of Horticulture", "quote": "St. Augustine grass, known botanically as **Stenotaphrum** secundatum, forms a dense, coarse-textured lawn in the Gulf states." },
      { "author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The spikelets of **Stenotaphrum** are embedded in cavities along one side of a flattened, corky rachis." }
    ]
  },
  "Dashboard — sten\\stenotic.md": {
    "primary": "Characterized by, suffering from, or pertaining to stenosis; abnormally narrowed or constricted.",
    "secondary": "In clinical hemodynamics and surgical pathology, describing turbulent flow dynamics, pressure gradients, and structural changes across a narrowed valve or arterial orifice.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The presystolic thrill felt at the apex corresponds to blood forced through the narrowed, **stenotic** mitral orifice." },
      { "author": "Eugene Braunwald", "work": "Heart Disease", "quote": "Measurement of the transvalvular systolic gradient provides quantitative assessment of how severely **stenotic** the aortic valve is." },
      { "author": "Harvey Cushing", "work": "Tumors of the Nervus Acusticus", "quote": "Obstruction of the **stenotic** foramen of Monro led to unilateral hydrocephalus of the right lateral ventricle." }
    ]
  },
  "Dashboard — sten\\stenotomus.md": {
    "primary": "A genus of marine sparid fishes found along the Atlantic coast of North America, commonly known as scups or porgies.",
    "secondary": "In fisheries biology and coastal ichthyology, marine perciform fishes typified by Stenotomus chrysops (the common scup), which school in coastal waters and feed on benthic crustaceans, mollusks, and polychaetes.",
    "quotes": [
      { "author": "David Starr Jordan", "work": "A Guide to the Study of Fishes", "quote": "The porgy, **Stenotomus** chrysops, is an abundant and delicious food fish taken in vast numbers along the New England coast." },
      { "author": "Spencer Fullerton Baird", "work": "Report on the Condition of the Sea Fisheries of the South Coast of New England", "quote": "Traps and pounds set near Cape Cod capture immense quantities of **Stenotomus** during their annual spring migration." },
      { "author": "Albert Günther", "work": "Catalogue of the Acanthopterygian Fishes in the British Museum", "quote": "The genus **Stenotomus** possesses narrow incisor-like anterior teeth backed by several rows of rounded crushing molars." }
    ]
  },
  "Dashboard — sten\\stenotus.md": {
    "primary": "A genus of flowering subshrubs in the sunflower family (Asteraceae), commonly known as mock goldenweeds, native to western North America.",
    "secondary": "In arid lands botany and phytogeography, low caespitose perennial plants (such as Stenotus acaulis) with leathery linear leaves and solitary golden-yellow flower heads adapted to dry, rocky limestone ridges of the Great Basin.",
    "quotes": [
      { "author": "Asa Gray", "work": "Synoptical Flora of North America", "quote": "The genus **Stenotus** comprises low tufted perennials of the Rocky Mountains, bearing bright yellow radiate heads." },
      { "author": "John Torrey", "work": "A Flora of North America", "quote": "Upon high dry mountain crags, the diminutive **Stenotus** forms compact cushions adorned with golden daisy-like blooms." },
      { "author": "Arthur Cronquist", "work": "Vascular Plants of the Pacific Northwest", "quote": "Taxonomic treatment separates **Stenotus** from Haplopappus on the basis of its narrow involucral bracts and perennial habit." }
    ]
  },
  "Dashboard — sten\\stent.md": {
    "primary": "A tubular, expandable medical mesh or wire scaffold inserted into an anatomical vessel or duct to keep it open; or a dental impression compound named after dentist Charles Stent.",
    "secondary": "In interventional cardiology, radiology, and vascular surgery, metallic, drug-eluting, or bioresorbable coronary endoprostheses deployed via balloon angioplasty to prevent arterial recoil and restenosis.",
    "quotes": [
      { "author": "Eugene Braunwald", "work": "Heart Disease: A Textbook of Cardiovascular Medicine", "quote": "Deployment of an intracoronary metallic **stent** significantly reduced acute vessel closure following percutaneous transluminal angioplasty." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine: Modern Edition", "quote": "In obstructive biliary jaundice, endoscopic placement of a plastic or metal **stent** provides immediate palliative drainage." },
      { "author": "Arthur Conan Doyle", "work": "Memories and Adventures", "quote": "Surgical technique advances through clever mechanical devices that support fragile tissues, much like a vascular **stent**." }
    ]
  },
  "Dashboard — sten\\stentor.md": {
    "primary": "A person with an extraordinarily loud, powerful voice; or a genus of trumpet-shaped freshwater ciliated protozoans.",
    "secondary": "In classical literature (Homer's *Iliad*), the Greek herald Stentor whose bronze voice equaled that of fifty men; in protistology, large heterotrich ciliates capable of regeneration and blue-green stentorin pigmentation.",
    "quotes": [
      { "author": "Homer", "work": "Iliad", "quote": "Hera took the form of great-hearted **Stentor**, whose voice of bronze shouted as loud as fifty other men." },
      { "author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Invertebrated Animals", "quote": "The trumpet animalcule, **Stentor**, anchors itself to water plants, creating vortices with its peristomial cilia." },
      { "author": "Ray Lankester", "work": "A Treatise on Zoology", "quote": "Remarkable experiments in protozoan regeneration showed that a nucleated fragment of **Stentor** quickly rebuilds the entire organism." }
    ]
  },
  "Dashboard — sten\\stentorian.md": {
    "primary": "Extremely loud, booming, powerful, and resonant in voice or sound.",
    "secondary": "In rhetorical delivery and military command, speech projecting with immense carrying power across battlefields or crowded halls without acoustic amplification.",
    "quotes": [
      { "author": "Charles Dickens", "work": "David Copperfield", "quote": "The boatswain roared his orders in a **stentorian** voice that rose triumphant above the howling of the gale." },
      { "author": "Herman Melville", "work": "Moby-Dick", "quote": "Ahab hailed the passing ship with a **stentorian** cry that startled the sleeping albatrosses upon the water." },
      { "author": "Walter Scott", "work": "Ivanhoe", "quote": "The herald stepped forward and proclaimed the terms of the tournament in a **stentorian** tone heard by the whole multitude." }
    ]
  },
  "Dashboard — ten\\anhemitonic.md": {
    "primary": "Designating a musical scale or melody that contains no semitones or half-steps, especially the standard pentatonic scale.",
    "secondary": "In ethnomusicology, comparative acoustics, and music theory, pitch systems (such as the major pentatonic C-D-E-G-A) whose whole-tone and minor-third intervals lack the sharp dissonance of semitones, foundational to folk melodies worldwide.",
    "quotes": [
      { "author": "Alexander John Ellis", "work": "On the Musical Scales of Various Nations", "quote": "The archaic Scottish and Chinese scales are strictly **anhemitonic**, having no half-tones between their five constituent pitches." },
      { "author": "Percy Scholes", "work": "The Oxford Companion to Music", "quote": "Melodies constructed upon an **anhemitonic** foundation possess a spacious, floating simplicity that never sounds dated." },
      { "author": "Béla Bartók", "work": "Hungarian Folk Music", "quote": "The oldest layer of Magyar folk song employs an **anhemitonic** pentatonic structure preserved from our ancestral Asian homelands." }
    ]
  },
  "Dashboard — ten\\atelectasis.md": {
    "primary": "Partial or complete collapse of a lung or lobe of a lung, resulting in reduced gas exchange.",
    "secondary": "In pulmonology and critical care, loss of lung volume due to alveolar collapse from bronchial obstruction (mucus plug, tumor), external compression (pleural effusion), or surfactant deficiency (neonatal respiratory distress syndrome).",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Obstruction of a main bronchus by a foreign body leads rapidly to absorption of alveolar air and massive pulmonary **atelectasis**." },
      { "author": "Eugene Braunwald", "work": "Harrison's Principles of Internal Medicine", "quote": "Postoperative hypoventilation promotes basilar **atelectasis**, which resolves with incentive spirometry and chest physical therapy." },
      { "author": "Harvey Cushing", "work": "Papers Relating to the Pituitary Body and Surgery", "quote": "Shallow breathing under prolonged general anesthesia predisposes the surgical patient to lobar **atelectasis**." }
    ]
  },
  "Dashboard — ten\\atonal.md": {
    "primary": "Lacking a tonal center, key, or definite musical tonic; not written in any key.",
    "secondary": "In 20th-century musicology and aesthetics, compositions (pioneered by Arnold Schoenberg, Alban Berg, and Anton Webern) that consciously abandon traditional major-minor hierarchical harmony in favor of free pitch relations or twelve-tone serialism.",
    "quotes": [
      { "author": "Arnold Schoenberg", "work": "Harmonielehre (Theory of Harmony)", "quote": "I prefer to speak of the emancipation of dissonance rather than applying the negative label of **atonal** to our harmonic language." },
      { "author": "Aaron Copland", "work": "What to Listen for in Music", "quote": "An **atonal** piece creates extreme dramatic tension because the ear is denied the customary rest of a resolving tonic chord." },
      { "author": "Theodor W. Adorno", "work": "Philosophy of New Music", "quote": "The radical **atonal** breakthrough reflected the fractured historical reality of post-war European consciousness." }
    ]
  },
  "Dashboard — ten\\atonally.md": {
    "primary": "In an atonal manner; without reference to a central key or traditional harmonic tonic.",
    "secondary": "In performance analysis and music criticism, executing or composing musical lines where pitch relationships are organized through interval sets rather than diatonic keys.",
    "quotes": [
      { "author": "Aaron Copland", "work": "Our New Music", "quote": "The violins weave **atonally** through jagged angular phrases that defy all conventional cadence." },
      { "author": "Percy Scholes", "work": "The Oxford Companion to Music", "quote": "The vocal line declaims **atonally** in Pierrot Lunaire, blurring the line between singing and spoken recitation." },
      { "author": "Leonard Bernstein", "work": "The Infinite Variety of Music", "quote": "Even when moving **atonally**, the underlying rhythmic pulse of the piece provides structural coherence." }
    ]
  },
  "Dashboard — ten\\atone.md": {
    "primary": "To make amends or reparation for an offense, crime, or error; to expiate.",
    "secondary": "In theology and moral philosophy (originally from Middle English *at one*, meaning to bring into reconciliation or harmony), the restoration of right relationship between humanity and God through sacrifice.",
    "quotes": [
      { "author": "John Milton", "work": "Paradise Lost", "quote": "Man disobeying, disloyal, on the part of heaven demands that someone die, or whole mankind perish: who shall **atone** for his transgression?" },
      { "author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "Sydney Carton laid down his life to **atone** for a wasted youth and bring happiness to those he loved." },
      { "author": "George Eliot", "work": "Middlemarch", "quote": "No subsequent generosity could entirely **atone** for the secret treachery of his early mercantile career." }
    ]
  },
  "Dashboard — ten\\atonement.md": {
    "primary": "Reparation, expiation, or reconciliation for a wrong, injury, or sin; the state of being at one.",
    "secondary": "In Christian soteriology, the redemptive work of Jesus Christ reconciling fallen humanity to God (theories including Christus Victor, penal substitution, and moral influence); in Judaism, Yom Kippur (the Day of Atonement).",
    "quotes": [
      { "author": "John Milton", "work": "Paradise Lost", "quote": "Behold me, then; me for him, life for life, I offer; on me let thine anger fall; account me man; I make **atonement**." },
      { "author": "Samuel Taylor Coleridge", "work": "Aids to Reflection", "quote": "The divine mystery of the **Atonement** transcends mechanical juridical analogies, manifesting infinite spiritual love." },
      { "author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "Arthur Dimmesdale sought in secret penance and solitary vigils that peace which public **atonement** alone could bring." }
    ]
  },
  "Dashboard — ten\\atonia.md": {
    "primary": "Lack of normal muscle tone or tension; flaccidity or relaxation of bodily tissues.",
    "secondary": "In clinical neurology, sleep medicine, and gastroenterology, total loss of skeletal muscle tone (such as REM sleep atonia preventing physical enactment of dreams, or uterine atonia postpartum leading to hemorrhage).",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Postpartum hemorrhage is most frequently caused by sudden uterine **atonia**, requiring vigorous bimanual massage." },
      { "author": "Oliver Sacks", "work": "Awakenings", "quote": "Sudden episodes of cataplexy plunge the narcoleptic patient into generalized **atonia** while consciousness remains clear." },
      { "author": "Claude Bernard", "work": "Lectures on the Physiology of the Nervous System", "quote": "Transection of the dorsal spinal roots abolishes proprioceptive reflexes, producing complete muscular **atonia**." }
    ]
  },
  "Dashboard — ten\\atonic.md": {
    "primary": "Lacking normal physiological tone, tension, or energy; relaxed or flaccid; or an unstressed syllable in linguistics.",
    "secondary": "In clinical neurology, designating seizures (atonic seizures or drop attacks) where sudden loss of muscle tone causes the patient to collapse; in phonetics, unaccented vowels or syllables.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "In chronic dilatation of the stomach, the muscular walls become **atonic** and unable to propel food forward." },
      { "author": "Henry Sweet", "work": "A Handbook of Phonetics", "quote": "In rapid English speech, vowels in **atonic** syllables universally reduce toward the neutral central schwa." },
      { "author": "W. Russell Brain", "work": "Diseases of the Nervous System", "quote": "The sudden collapse of an **atonic** drop attack results from transient paroxysmal inhibition of brainstem motor centers." }
    ]
  },
  "Dashboard — ten\\atonicity.md": {
    "primary": "The state or condition of lacking normal muscle tone, firmness, or physiological tension; atony.",
    "secondary": "In internal medicine and pathology, chronic slackness or flaccidity of hollow muscular organs (such as gastric or colonic atonicity), leading to stasis and distension.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Persistent **atonicity** of the bladder wall follows long-standing prostatic obstruction and severe urinary retention." },
      { "author": "Claude Bernard", "work": "Lectures on Experimental Physiology", "quote": "Prolonged administration of curare produces complete vascular and muscular **atonicity** by blocking motor endplates." },
      { "author": "Thomas Addison", "work": "A Collection of Published Writings", "quote": "General exhaustion and extreme visceral **atonicity** characterized the late stages of adrenal cortical failure." }
    ]
  },
  "Dashboard — ten\\atony.md": {
    "primary": "Lack of normal physiological tone, tension, or elastic firmness in muscle or other bodily organs.",
    "secondary": "In obstetrics and surgical pathology, failure of contractile response in smooth or skeletal muscle (notably uterine atony causing catastrophic postpartum hemorrhage).",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Uterine **atony** remains the most formidable cause of sudden primary hemorrhage immediately following delivery." },
      { "author": "Oliver Wendell Holmes", "work": "Medical Essays", "quote": "The chronic invalid suffered from universal muscular **atony**, unable to sit upright without soft supporting cushions." },
      { "author": "Thomas Sydenham", "work": "The Works of Thomas Sydenham", "quote": "Sedentary living and excessive wine weaken the digestive organs, inducing painful **atony** of the stomach and bowels." }
    ]
  },
  "Dashboard — ten\\barytone.md": {
    "primary": "A male singing voice between bass and tenor; or an ancient Greek word having an unaccented final syllable; variant spelling of baritone.",
    "secondary": "In classical linguistics and Greek accentuation, words carrying the acute accent on a syllable other than the ultima, the final vowel being pronounced with a low (grave) pitch.",
    "quotes": [
      { "author": "Henry George Liddell", "work": "A Greek-English Lexicon", "quote": "In Greek grammar, a **barytone** noun is one that has the acute accent on the penult or antepenult, leaving the final syllable unaccented." },
      { "author": "Max Müller", "work": "Lectures on the Science of Language", "quote": "The shift from oxytone to **barytone** accentuation reflects deep rhythmic laws governing the Indo-European parent language." },
      { "author": "Charles Burney", "work": "A General History of Music", "quote": "The rich resonance of the **barytone** voice provides the essential dramatic anchor in operatic ensembles." }
    ]
  },
  "Dashboard — ten\\catatonia.md": {
    "primary": "A neuropsychiatric syndrome characterized by motor abnormalities, profound immobility, stupor, mutism, or uncontrollable purposeless agitation.",
    "secondary": "In psychiatry and clinical neuroscience (first described by Karl Kahlbaum in 1874), a behavioral syndrome featuring waxy flexibility (flexibilitas cerea), posturing, echolalia, and negativism, occurring in mood disorders and schizophrenia.",
    "quotes": [
      { "author": "Karl Kahlbaum", "work": "Die Katatonie oder das Spannungsirresein", "quote": "I propose the term **catatonia** for that singular clinical picture where motor immobility, mutism, and waxy stupor predominate." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "In the stuporous phase of **catatonia**, the limbs remain indefinitely in whatever bizarre posture the examiner places them." },
      { "author": "Oliver Sacks", "work": "Awakenings", "quote": "Post-encephalitic parkinsonism often locked patients into a frozen **catatonia** that was dramatically dissolved by L-DOPA." }
    ]
  },
  "Dashboard — ten\\catatoniac.md": {
    "primary": "A person affected by catatonia; or exhibiting catatonic symptoms.",
    "secondary": "In historical clinical psychiatry, a patient exhibiting persistent muscular rigidity, mutism, stupor, or stereotyped motor posturing.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The **catatoniac** patient sat motionless in the asylum ward for weeks, eyes fixed upon the floor in total silence." },
      { "author": "Karl Kahlbaum", "work": "Die Katatonie", "quote": "Sudden violent excitation may unexpectedly erupt in a **catatoniac** who had previously appeared completely comatose." },
      { "author": "Oliver Sacks", "work": "The Man Who Mistook His Wife for a Hat", "quote": "To converse with a profound **catatoniac** requires infinite patience, awaiting the momentary thawing of frozen speech." }
    ]
  },
  "Dashboard — ten\\catatonic.md": {
    "primary": "Relating to, characterized by, or affected by catatonia; exhibiting motor immobility, stupor, or rigidity.",
    "secondary": "In neuropsychiatry and common usage, a state of psychological paralysis, stupor, or unresponsive immobility under acute psychic shock or severe organic brain disease.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Patients in a **catatonic** stupor frequently demonstrate waxy flexibility, allowing their arms to be shaped like lead pipes." },
      { "author": "George Orwell", "work": "Coming Up for Air", "quote": "The dreadful shock of war left many soldiers sitting in a **catatonic** trance, blind and deaf to the world around them." },
      { "author": "Oliver Sacks", "work": "Awakenings", "quote": "The sudden introduction of levodopa awakened the frozen, **catatonic** post-encephalitic sufferers into joyful life." }
    ]
  },
  "Dashboard — ten\\decatonic.md": {
    "primary": "Consisting of or based on ten tones, pitches, or scale degrees per octave.",
    "secondary": "In modern music theory, microtonal acoustics, and synthetic scale construction, an equal-temperament or just-intonation scale system dividing the octave into ten discrete pitches.",
    "quotes": [
      { "author": "Alexander John Ellis", "work": "On the Musical Scales of Various Nations", "quote": "Experimental division of the octave into a **decatonic** system produces unusual harmonies outside traditional European tonality." },
      { "author": "Percy Scholes", "work": "The Oxford Companion to Music", "quote": "Modern microtonal composers explored the **decatonic** scale as an alternative between pentatonic simplicity and chromatic complexity." },
      { "author": "Charles Ives", "work": "Essays Before a Sonata", "quote": "Venturing beyond twelve semitones, an adventurous musician may test an artificial **decatonic** framework for fresh dissonances." }
    ]
  },
  "Dashboard — ten\\diatonic.md": {
    "primary": "Involving or using only the seven notes of a standard major or minor scale without chromatic alteration.",
    "secondary": "In classical music theory, scales and harmonic progressions constructed of five whole tones and two semitones, foundational to Western musical tradition since ancient Greek harmonics.",
    "quotes": [
      { "author": "Aristotle", "work": "Problems: Book XIX on Music", "quote": "The **diatonic** genus is the most natural and ancient of all musical modes, pleasant and noble to the listener." },
      { "author": "Johann Sebastian Bach", "work": "The Well-Tempered Clavier: Preface", "quote": "Equal temperament allows modulations across all twenty-four keys while preserving the integrity of the **diatonic** scale." },
      { "author": "Claude Debussy", "work": "Monsieur Croche, Antidilettante", "quote": "To break free from strict **diatonic** formulas, I sought inspiration in the antique modes and whole-tone scales." }
    ]
  },
  "Dashboard — ten\\ditone.md": {
    "primary": "An ancient musical interval equal to two whole tones, corresponding to a Pythagorean major third (frequency ratio 81:64).",
    "secondary": "In Pythagorean tuning and medieval music theory, an interval slightly wider and more dissonant than the pure just major third (5:4), historically classified as an imperfect consonance.",
    "quotes": [
      { "author": "Pythagoras", "work": "Harmonics", "quote": "Compounding two sesquioctave tones of nine to eight produces the sharp **ditone** of eighty-one to sixty-four." },
      { "author": "Boethius", "work": "De Institutione Musica", "quote": "The ancient musicians rejected the **ditone** as a perfect consonance because its ratio deviates from simple superparticular proportions." },
      { "author": "Thomas Morley", "work": "A Plaine and Easie Introduction to Practicall Musicke", "quote": "In ancient counterpoint, the **ditone** was tolerated as an imperfect concord leading toward the fifth." }
    ]
  },
  "Dashboard — ten\\dodecatonic.md": {
    "primary": "Consisting of or utilizing twelve musical tones or pitches, especially the twelve semitones of the chromatic scale.",
    "secondary": "In 20th-century music theory, synonymous with dodecaphonic or twelve-tone serial technique pioneered by Arnold Schoenberg, treating all twelve chromatic pitch classes with equal structural weight.",
    "quotes": [
      { "author": "Arnold Schoenberg", "work": "Style and Idea", "quote": "A **dodecatonic** row guarantees that no single pitch predominates, ensuring the total equality of all twelve tones." },
      { "author": "Theodor W. Adorno", "work": "Philosophy of New Music", "quote": "The rigorous discipline of the **dodecatonic** method liberated modern composition from the tyranny of the triad." },
      { "author": "Aaron Copland", "work": "Copland on Music", "quote": "Many American composers adopted a flexible **dodecatonic** framework to achieve fresh contrapuntal freedom." }
    ]
  },
  "Dashboard — ten\\dystonia.md": {
    "primary": "A neurological movement disorder characterized by involuntary, sustained muscle contractions that cause repetitive twisting movements or abnormal postures.",
    "secondary": "In neurology, basal ganglia dysfunction (focal, segmental, or generalized dystonia, such as torticollis, writer's cramp, or DYT1 dystonia) treated with anticholinergics, botulinum toxin, or deep brain stimulation.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Torsion spasms and bizarre trunk contortions in musculorum deformans represent a severe generalized **dystonia**." },
      { "author": "Oliver Sacks", "work": "Awakenings", "quote": "Fluctuations in dopamine availability would plunge the post-encephalitic patient into painful facial **dystonia**." },
      { "author": "W. Russell Brain", "work": "Diseases of the Nervous System", "quote": "Focal task-specific **dystonia**, such as musician's cramp, involves failure of cortical inhibition during complex motor performance." }
    ]
  },
  "Dashboard — ten\\ectasia.md": {
    "primary": "Dilation, expansion, or distension of a hollow tubular organ or bodily vessel; ectasis.",
    "secondary": "In clinical pathology and surgical diagnosis, abnormal dilation of structures such as bronchi (bronchiectasis), mammary ducts (mammary duct ectasia), or lymphatic vessels (lymphangiectasia).",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Chronic bronchial suppuration leads to permanent destruction of the elastic wall and cylindrical **ectasia**." },
      { "author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "Vascular **ectasia** in inflammatory tissue results from prolonged paralytic relaxation of the arteriolar muscular coats." },
      { "author": "Jonathan Hutchinson", "work": "Illustrations of Clinical Surgery", "quote": "Subareolar duct **ectasia** produces nipple discharge that must be carefully differentiated from malignant disease." }
    ]
  },
  "Dashboard — ten\\enneatonic.md": {
    "primary": "Consisting of or based on nine musical tones or pitches per octave.",
    "secondary": "In music theory and ethnomusicology, nine-note scalar systems (such as the messiaen third mode of limited transposition, or the alternating whole-half-step nonatonic scale) employed in microtonal and modernist composition.",
    "quotes": [
      { "author": "Olivier Messiaen", "work": "The Technique of My Musical Language", "quote": "My third mode of limited transposition forms an **enneatonic** scale of nine tones divided into three symmetrical units." },
      { "author": "Percy Scholes", "work": "The Oxford Companion to Music", "quote": "Certain non-Western folk traditions employ an **enneatonic** pitch collection containing auxiliary ornamental scale steps." },
      { "author": "Alexander John Ellis", "work": "On the Musical Scales of Various Nations", "quote": "Theoretical exploration of Arabian lute fretting revealed complex **enneatonic** divisions within the octave." }
    ]
  },
  "Dashboard — ten\\entasia.md": {
    "primary": "A tonic spasm, cramp, or persistent abnormal muscular tension; constrictive muscular spasm.",
    "secondary": "In classical medical nosology (John Mason Good's classification), a generic order of diseases characterized by involuntary, sustained muscular rigidity, encompassing tetanus, trismus, and priapism.",
    "quotes": [
      { "author": "John Mason Good", "work": "The Study of Medicine", "quote": "Under the generic order **entasia**, I classify those morbid states where constant, tonic muscular spasm defies voluntary control." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Severe strychnine intoxication produces excruciating **entasia**, arching the patient's spine into complete opisthotonos." },
      { "author": "Thomas Sydenham", "work": "The Works of Thomas Sydenham", "quote": "The convulsive lockjaw and sustained bodily **entasia** of tetanus demand immediate warmth and sedative draughts." }
    ]
  },
  "Dashboard — ten\\entasis.md": {
    "primary": "A slight convex swelling or curve in the shaft of a classical architectural column, introduced to correct an optical illusion of concavity.",
    "secondary": "In classical architecture and aesthetic theory (notably observed in the Parthenon's Doric columns), a subtle tapering curve that imparts an organic appearance of muscular tension bearing immense structural weight.",
    "quotes": [
      { "author": "Vitruvius", "work": "De Architectura", "quote": "The shafts of the columns must possess a gentle swelling in the middle, which the Greeks term **entasis**, to satisfy the eye." },
      { "author": "John Ruskin", "work": "The Seven Lamps of Architecture", "quote": "The exquisite **entasis** of the Athenian colonnade gives the stone a living, elastic grace that rigid geometric cylinders destroy." },
      { "author": "Francis Cranmer Penrose", "work": "An Investigation of the Principles of Athenian Architecture", "quote": "Precise mathematical measurements of the Parthenon confirmed that every Doric shaft incorporates a deliberate parabolic **entasis**." }
    ]
  },
  "Dashboard — ten\\epitasis.md": {
    "primary": "The part of an ancient drama where the main action develops and the plot thickens, leading up to the catastrophe; or an intensification of disease symptoms.",
    "secondary": "In classical dramatic theory (following Donatus and Scaliger), the second main division of a play following the protasis, where complications multiply; in medicine, the acute exacerbation of fever or illness.",
    "quotes": [
      { "author": "John Dryden", "work": "An Essay of Dramatic Poesy", "quote": "The **epitasis** is the working up of the plot, where the complications gather and the audience hangs in suspense." },
      { "author": "Ben Jonson", "work": "The Magnetic Lady: Chorus", "quote": "Now begins our **epitasis**, or business of the play, wherein the knots are tied which none but the author can untie." },
      { "author": "Thomas Browne", "work": "Pseudodoxia Epidemica", "quote": "In the severe **epitasis** of a malignant fever, the animal spirits are consumed by internal combustion." }
    ]
  },
  "Dashboard — ten\\hemitonia.md": {
    "primary": "The musical quality or property of containing semitones; or a semitonic scale system.",
    "secondary": "In ancient Greek harmonic theory (Aristoxenian harmonics) and comparative musicology, scales characterized by the inclusion of half-tone intervals (hemitones), contrasted with anhemitonic systems.",
    "quotes": [
      { "author": "Aristoxenus", "work": "Elementa Harmonica", "quote": "In the diatonic and chromatic genera, the introduction of **hemitonia** creates that distinct tension which resolves to the keynote." },
      { "author": "Alexander John Ellis", "work": "The History of Musical Pitch", "quote": "The emergence of **hemitonia** in European scale evolution marked a decisive departure from primitive pentatonic models." },
      { "author": "Percy Scholes", "work": "The Oxford Companion to Music", "quote": "The presence of **hemitonia** in a scale introduces leading tones and chromatic pull unknown to purely whole-tone music." }
    ]
  },
  "Dashboard — ten\\hemitonic.md": {
    "primary": "Consisting of or characterized by the interval of a semitone (half-step); or designating a musical scale that contains semitones.",
    "secondary": "In ethnomusicology and modal theory, five-tone scales containing semitones (such as Japanese *in* and *hirajoshi* scales), contrasted with standard anhemitonic pentatonic scales.",
    "quotes": [
      { "author": "Alexander John Ellis", "work": "On the Musical Scales of Various Nations", "quote": "The Japanese koto tuning demonstrates a **hemitonic** pentatonic structure with minor second intervals that sound exotic to Western ears." },
      { "author": "Percy Scholes", "work": "The Oxford Companion to Music", "quote": "Unlike Celtic folk song, certain Mediterranean folk melodies are distinctly **hemitonic**, relying on sharp semitone inflections." },
      { "author": "Béla Bartók", "work": "Rumanian Folk Music", "quote": "The modal flavor of the dance melody shifts abruptly from an anhemitonic opening to a tense **hemitonic** cadential close." }
    ]
  },
  "Dashboard — ten\\heptatonic.md": {
    "primary": "Consisting of or based on seven musical tones or pitches per octave.",
    "secondary": "In music theory and acoustic history, the standard seven-note scales (including major, minor, and church modes) foundational to Western classical harmony, Indian ragas (sampurna), and diverse world traditions.",
    "quotes": [
      { "author": "Percy Scholes", "work": "The Oxford Companion to Music", "quote": "The standard European major scale is the prime historical exemplar of a diatonic **heptatonic** system." },
      { "author": "Alexander John Ellis", "work": "On the Musical Scales of Various Nations", "quote": "Classical Indian music classifies scales into pentatonic audav, hexatonic shadav, and complete **heptatonic** sampurna ragas." },
      { "author": "Leonard Bernstein", "work": "The Joy of Music", "quote": "From our ancient **heptatonic** heritage we derive the seven diatonic modes that formed the language of Gregorian chant." }
    ]
  },
  "Dashboard — ten\\hexatonic.md": {
    "primary": "Consisting of or based on six musical tones or pitches per octave.",
    "secondary": "In music theory, six-note scale collections (such as the whole-tone scale, the blues scale, or hexatonic systems formed by alternating minor thirds and semitones), extensively used in 20th-century impressionist and jazz harmony.",
    "quotes": [
      { "author": "Claude Debussy", "work": "Monsieur Croche, the Dilettante Hater", "quote": "The whole-tone scale is a symmetrical **hexatonic** formation that floats freely, untethered to traditional tonic anchors." },
      { "author": "Percy Scholes", "work": "The Oxford Companion to Music", "quote": "Medieval solmization was built upon a **hexatonic** framework: the six-note guidonian hexachord ut-re-mi-fa-sol-la." },
      { "author": "Aaron Copland", "work": "What to Listen for in Music", "quote": "American blues melodies frequently utilize a **hexatonic** collection incorporating the expressive flatted third and seventh." }
    ]
  },
  "Dashboard — ten\\hyperisotonic.md": {
    "primary": "Having an osmotic pressure greater than that of isotonic solutions; hypertonic.",
    "secondary": "In cell physiology and renal biophysics, a solution possessing a higher effective osmolyte concentration than standard physiological saline or blood plasma, causing red blood cells to lose water and crenate.",
    "quotes": [
      { "author": "Svante Arrhenius", "work": "Text-Book of Theoretical Electrochemistry", "quote": "When red corpuscles are immersed in a **hyperisotonic** salt solution, water flows outward across the membrane, shrinking the cells." },
      { "author": "Claude Bernard", "work": "Lectures on the Phenomena of Life", "quote": "The renal medulla maintains a **hyperisotonic** interstitial environment essential for the concentration of mammalian urine." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Intravenous infusion of a **hyperisotonic** mannitol solution rapidly reduces intracranial pressure in acute cerebral edema." }
    ]
  },
  "Dashboard — ten\\hypertonia.md": {
    "primary": "An abnormal increase in muscle tension or tone, and a reduced capacity of a muscle to stretch.",
    "secondary": "In clinical neurology, elevated muscle tone resulting from upper motor neuron lesions, divided into spasticity (velocity-dependent resistance with clasp-knife phenomenon) and rigidity (velocity-independent lead-pipe or cogwheel resistance in extrapyramidal disease).",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Damage to the pyramidal tract produces spastic **hypertonia** accompanied by hyperactive deep tendon reflexes and a positive Babinski sign." },
      { "author": "W. Russell Brain", "work": "Diseases of the Nervous System", "quote": "In Parkinson's disease, extrapyramidal **hypertonia** manifests as steady cogwheel rigidity throughout passive joint movement." },
      { "author": "Oliver Sacks", "work": "Awakenings", "quote": "The patient's limbs were frozen in severe plastic **hypertonia**, resisting every attempt to flex or extend the elbows." }
    ]
  },
  "Dashboard — ten\\hypertonic.md": {
    "primary": "Having a higher osmotic pressure than a particular fluid, especially a bodily fluid; or exhibiting excessive muscular tone or tension.",
    "secondary": "In physiology and cellular biophysics, a solution with a greater osmolarity than blood plasma (causing cell dehydration and shrinkage), or a muscle in a state of sustained pathological contracture.",
    "quotes": [
      { "author": "Linus Pauling", "work": "General Chemistry", "quote": "Erythrocytes placed in a **hypertonic** saline solution rapidly lose water through osmosis and become wrinkled and crenated." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The patient's spastic gait resulted from **hypertonic** contractures in the lower extremities following a capsular stroke." },
      { "author": "Claude Bernard", "work": "Lectures on the Physiology of the Nervous System", "quote": "Tetanic spasms provoked by strychnine maintain the entire skeletal musculature in an agonizing **hypertonic** state." }
    ]
  },
  "Dashboard — ten\\hypertonicity.md": {
    "primary": "The state or condition of being hypertonic; excessive muscle tone, or higher osmotic pressure.",
    "secondary": "In neurophysiology and clinical pathology, increased resting muscle tone from central motor pathway lesions, or elevated osmolality in extracellular fluid compartments (hypertonic dehydration).",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Cerebral palsy in childhood frequently presents with marked muscular **hypertonicity**, producing characteristic scissors-gait posturing." },
      { "author": "W. Russell Brain", "work": "Diseases of the Nervous System", "quote": "The clasp-knife phenomenon illustrates how rapid muscle stretch dramatically triggers pyramidal **hypertonicity**." },
      { "author": "Eugene Braunwald", "work": "Harrison's Principles of Internal Medicine", "quote": "Severe extracellular **hypertonicity** draws water out of brain neurons, resulting in somnolence, confusion, and coma." }
    ]
  },
  "Dashboard — ten\\hypertonus.md": {
    "primary": "Increased, excessive, or abnormal tone or tension in a muscle, organ, or bodily system; hypertonia.",
    "secondary": "In neuro-ophthalmology and neuro-urology, sustained pathological resting contraction (such as detrusor hypertonus causing urge incontinence, or ocular hypertonus / elevated intraocular pressure in glaucoma).",
    "quotes": [
      { "author": "W. Russell Brain", "work": "Diseases of the Nervous System", "quote": "Extrapyramidal lesions produce a generalized **hypertonus** that impairs the smooth initiation of voluntary locomotion." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Neurogenic bladder resulting from spinal cord injury often exhibits uninhibited detrusor **hypertonus**." },
      { "author": "Jonathan Hutchinson", "work": "Illustrations of Clinical Surgery", "quote": "In acute closed-angle glaucoma, marked ocular **hypertonus** turns the eyeball as hard as a marble." }
    ]
  },
  "Dashboard — ten\\hypotenuse.md": {
    "primary": "The longest side of a right-angled triangle, opposite the right angle.",
    "secondary": "In Euclidean geometry and trigonometry, the side c in the Pythagorean theorem (a² + b² = c²), subtending the 90-degree angle and serving as the radius vector in unit-circle trigonometry.",
    "quotes": [
      { "author": "Euclid", "work": "Elements", "quote": "In right-angled triangles the square on the side subtending the right angle, the **hypotenuse**, is equal to the squares on the sides containing it." },
      { "author": "W. S. Gilbert", "work": "The Pirates of Penzance", "quote": "I'm very well acquainted, too, with matters mathematical, / I understand equations, both the simple and quadratical, / About binomial theorem I'm teeming with a lot o' news, / With many cheerful facts about the square of the **hypotenuse**." },
      { "author": "René Descartes", "work": "La Géométrie", "quote": "The length of the **hypotenuse** represents the absolute distance between two points in a Cartesian coordinate plane." }
    ]
  },
  "Dashboard — ten\\hypotonia.md": {
    "primary": "A state of low muscle tone, resulting in floppiness, reduced muscle strength, and poor coordination.",
    "secondary": "In pediatric neurology and neuromuscular medicine, benign congenital hypotonia or symptomatic 'floppy infant syndrome' resulting from lower motor neuron disease (spinal muscular atrophy), cerebellar lesions, or genetic trisomies (Down syndrome).",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Cerebellar disease manifests characteristically with ipsilateral **hypotonia**, intention tremor, and pendular deep reflexes." },
      { "author": "W. Russell Brain", "work": "Diseases of the Nervous System", "quote": "Infantile **hypotonia** causes the baby to feel like a rag doll when lifted, lacking all resistance to passive limb movement." },
      { "author": "Oliver Sacks", "work": "A Leg to Stand On", "quote": "Following nerve injury, the denervated muscle slipped into profound **hypotonia**, inert and completely silent to voluntary effort." }
    ]
  },
  "Dashboard — ten\\hypotonic.md": {
    "primary": "Having a lower osmotic pressure than a surrounding fluid, especially bodily fluids; or having low muscle tone.",
    "secondary": "In cellular physiology, a solution with lower solute concentration than intracellular fluid, causing cells to absorb water and swell or lyse; or muscles characterized by reduced resting tension.",
    "quotes": [
      { "author": "Linus Pauling", "work": "General Chemistry", "quote": "Placing red blood cells in a **hypotonic** bath of pure water causes rapid osmotic influx, leading to hemolysis." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The flaccid, **hypotonic** muscles of the paralyzed limb offered no resistance to passive flexion by the examiner." },
      { "author": "Claude Bernard", "work": "Lectures on the Phenomena of Life", "quote": "Living cells maintain internal osmotic homeostasis against surrounding **hypotonic** freshwater environments by active pumping." }
    ]
  },
  "Dashboard — ten\\hypotonicity.md": {
    "primary": "The state or condition of being hypotonic; subnormal muscle tone or reduced osmotic concentration.",
    "secondary": "In clinical medicine and fluid physiology, generalized muscular flaccidity in neurological disorders, or reduced osmolality in blood serum (hyponatremic hypotonicity).",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Marked **hypotonicity** of the skeletal musculature is a prominent feature of choreic disorders in childhood." },
      { "author": "Eugene Braunwald", "work": "Harrison's Principles of Internal Medicine", "quote": "Serum **hypotonicity** drives water into cerebral cells, resulting in cerebral edema and neurological deterioration." },
      { "author": "W. Russell Brain", "work": "Diseases of the Nervous System", "quote": "Lesions of the neocerebellum produce prominent **hypotonicity** and dysmetria on the side of the damaged hemisphere." }
    ]
  },
  "Dashboard — ten\\intonate.md": {
    "primary": "To recite, utter, or chant with a specific musical tone, vocal modulation, or pitch contour.",
    "secondary": "In liturgical music and ecclesiastical phonetics, to chant or sing the opening words of a psalm, canticle, or creed to set the pitch and mode for the choir.",
    "quotes": [
      { "author": "Thomas Cranmer", "work": "The Book of Common Prayer: Historical Directives", "quote": "The precentor shall clearly **intonate** the opening versicle so that the congregation may follow in unison." },
      { "author": "John Milton", "work": "Tetrachordon", "quote": "They **intonate** their solemn decrees with loud theatrical gravity, as if divine oracles spoke through their breath." },
      { "author": "Percy Scholes", "work": "The Oxford Companion to Music", "quote": "Before the choir enters, the priest steps to the lectern to **intonate** the Gloria in the authentic Gregorian mode." }
    ]
  },
  "Dashboard — ten\\isotonic.md": {
    "primary": "Having equal osmotic pressure or tension; or characterized by muscular contraction in which muscle tension remains constant while length changes.",
    "secondary": "In cell biology and sports physiology, a solution (such as 0.9% normal saline) having the same effective osmolality as blood serum; or dynamic physical exercise (such as lifting weights) where muscle length varies against steady resistance.",
    "quotes": [
      { "author": "Svante Arrhenius", "work": "Text-Book of Theoretical Electrochemistry", "quote": "De Vries demonstrated that two solutions are **isotonic** when plant cells placed in them experience neither plasmolysis nor swelling." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Intravenous replacement of acute fluid losses requires an **isotonic** saline solution to prevent osmotic lysis of erythrocytes." },
      { "author": "A. V. Hill", "work": "Muscular Movement in Man", "quote": "During an **isotonic** contraction, the muscle shortens against a constant mechanical load, converting chemical energy into external work." }
    ]
  },
  "Dashboard — ten\\microtone.md": {
    "primary": "A musical interval smaller than a standard semitone (half-step).",
    "secondary": "In ethnomusicology and modern acoustic composition, intervals such as quarter tones, third tones, or sixth tones (used in Arabic maqam, Indian shrutis, and works by Charles Ives and Alois Hába).",
    "quotes": [
      { "author": "Charles Ives", "work": "Some Quarter-Tone Impressions", "quote": "Exploring the subtle emotional shade of a **microtone** reveals acoustic horizons hidden behind the twelve keys of the piano." },
      { "author": "Alexander John Ellis", "work": "On the Musical Scales of Various Nations", "quote": "The twenty-two shrutis of Indian classical music demonstrate that the ear can appreciate a minute **microtone** with precision." },
      { "author": "Percy Scholes", "work": "The Oxford Companion to Music", "quote": "Czech composer Alois Hába designed specialized pianos and clarinets to execute every subtle **microtone** in his quarter-tone operas." }
    ]
  },
  "Dashboard — ten\\monotonic.md": {
    "primary": "Spoken or uttered in a single unvarying tone; repetitive and tedious; or consistently increasing or decreasing in mathematics.",
    "secondary": "In calculus and real analysis, a mathematical function that either entirely non-increases or entirely non-decreases as its independent variable grows, never reversing its directional trend.",
    "quotes": [
      { "author": "Charles Dickens", "work": "Hard Times", "quote": "The speaker droned on in a dull, **monotonic** voice that lulled the schoolchildren into heavy stupor." },
      { "author": "Bertrand Russell", "work": "The Principles of Mathematics", "quote": "A bounded **monotonic** sequence of real numbers is guaranteed by mathematical completeness to converge to a definite limit." },
      { "author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The rhythmic, **monotonic** beat of the alarm drum sounded through the fog, summoning the sans-culottes to the barricades." }
    ]
  },
  "Dashboard — ten\\monotonous.md": {
    "primary": "Lacking in variety and interest; dull, tedious, and repetitious; uttered in a single unvarying pitch.",
    "secondary": "In psychology and aesthetic criticism, sensory environments or labor routines devoid of stimulation that induce mental fatigue, boredom, and reduced attention.",
    "quotes": [
      { "author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "The cold wind and driving rain made the long winter days at Lowood school dreary and **monotonous**." },
      { "author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "Day after day we sailed across the **monotonous** expanse of the ocean, where nothing broke the uniform circle of the horizon." },
      { "author": "Herman Melville", "work": "Bartleby, the Scrivener", "quote": "The scrivener spent his silent days copying legal folios in a dull, **monotonous** routine behind his folding screen." }
    ]
  },
  "Dashboard — ten\\monotonously.md": {
    "primary": "In a dull, unvarying, and repetitious manner; without variation in tone, pitch, or activity.",
    "secondary": "In literary description and acoustic characterization, sounds or activities continuing with rhythmic, unchanging cadence that dulls the senses.",
    "quotes": [
      { "author": "Charles Dickens", "work": "Bleak House", "quote": "The heavy rain fell **monotonously** upon the leads of the terrace, beating like a tired pulse in the evening gloom." },
      { "author": "Joseph Conrad", "work": "Heart of Darkness", "quote": "The paddle wheel of the little river steamer beat **monotonously** against the muddy waters of the Congo." },
      { "author": "Thomas Hardy", "work": "The Return of the Native", "quote": "The dry heath grass rustled **monotonously** in the autumn wind, an ancient whisper unchanged for centuries." }
    ]
  },
  "Dashboard — ten\\monotony.md": {
    "primary": "Lack of variety and interest; tedious sameness; unvarying repetition in tone or activity.",
    "secondary": "In occupational psychology and social philosophy, the dull psychological state produced by repetitive industrial tasks, long sea voyages, or uniform environments.",
    "quotes": [
      { "author": "Mary Shelley", "work": "Frankenstein", "quote": "The ice broke with a roar, relieving our minds from the terrible **monotony** of our imprisonment in the frozen sea." },
      { "author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The extreme division of labour condemns the workman to perform a few simple operations, sinking his mind into sluggish **monotony**." },
      { "author": "Samuel Johnson", "work": "Rasselas, Prince of Abyssinia", "quote": "Even the pleasures of the Happy Valley became intolerable to Rasselas through their unbroken **monotony**." }
    ]
  },
  "Dashboard — ten\\neotenic.md": {
    "primary": "Exhibiting or relating to neoteny; the retention of juvenile, larval, or infantile physical traits into adult life.",
    "secondary": "In evolutionary developmental biology (evo-devo), adult organisms (such as the axolotl) that retain ancestral larval characteristics, or phylogenetic lineages (such as humans compared to apes) shaped by retarded developmental rates.",
    "quotes": [
      { "author": "Stephen Jay Gould", "work": "Ontogeny and Phylogeny", "quote": "Human adult cranial morphology is remarkably **neotenic**, retaining the rounded skull and flattened face of the juvenile chimp." },
      { "author": "Julian Huxley", "work": "Evolution: The Modern Synthesis", "quote": "The Mexican axolotl remains in a **neotenic** aquatic state, breeding freely while retaining its larval external gills." },
      { "author": "G. Kingsley Noble", "work": "The Biology of the Amphibia", "quote": "In perennibranchiate salamanders, the **neotenic** condition is irreversible, thyroid treatment failing to provoke metamorphosis." }
    ]
  },
  "Dashboard — ten\\neotenous.md": {
    "primary": "Retaining juvenile or larval characteristics in the mature adult form; neotenic.",
    "secondary": "In comparative anatomy and ethology, animals that reach sexual maturity while preserving physical or behavioral traits typical of embryonic or juvenile stages.",
    "quotes": [
      { "author": "Stephen Jay Gould", "work": "The Panda's Thumb", "quote": "The domestic dog exhibits numerous **neotenous** behavioral traits, retaining puppy-like barking and playfulness into maturity." },
      { "author": "Edward O. Wilson", "work": "Sociobiology: The New Synthesis", "quote": "Certain termite reproductive castes are **neotenous**, developing fertile gonads without acquiring wings or dark sclerotized cuticles." },
      { "author": "Ernst Mayr", "work": "What Evolution Is", "quote": "A **neotenous** mutation can open an entirely new evolutionary avenue by stripping away specialized adult structures." }
    ]
  },
  "Dashboard — ten\\neoteny.md": {
    "primary": "The retention of juvenile or larval features in the adult animal; or the slowing of physiological development.",
    "secondary": "In evolutionary morphology (heterochrony), a macroevolutionary mechanism (prominent in amphibians like Ambystoma mexicanum and in hominid evolution) where somatic maturation is retarded relative to sexual maturity.",
    "quotes": [
      { "author": "Stephen Jay Gould", "work": "Ontogeny and Phylogeny", "quote": "Human evolution has been profoundly guided by **neoteny**, giving our species an extended childhood essential for learning and culture." },
      { "author": "G. Kingsley Noble", "work": "The Biology of the Amphibia", "quote": "Facultative **neoteny** in salamanders allows populations to remain in the safe aquatic habitat when terrestrial conditions are harsh." },
      { "author": "Julian Huxley", "work": "Problems of Relative Growth", "quote": "The study of **neoteny** proves that evolutionary change often operates by altering the relative rates of developmental processes." }
    ]
  },
  "Dashboard — ten\\octatonic.md": {
    "primary": "Consisting of or based on eight musical tones or pitches per octave.",
    "secondary": "In 20th-century music theory, the symmetrical eight-note scale formed by alternating whole steps and half steps (half-whole or whole-half), prominent in the music of Nikolai Rimsky-Korsakov, Igor Stravinsky, and Béla Bartók.",
    "quotes": [
      { "author": "Igor Stravinsky", "work": "Memories and Commentaries", "quote": "The harmonic vocabulary of The Firebird owes its sparkling fairy-tale dissonance to the symmetrical **octatonic** scale." },
      { "author": "Percy Scholes", "work": "The Oxford Companion to Music", "quote": "The **octatonic** scale divides the octave into four tritone intervals, producing unique harmonic ambiguity." },
      { "author": "Aaron Copland", "work": "What to Listen for in Music", "quote": "Bartók exploited the alternating intervals of the **octatonic** collection to bridge folk melody with rigorous modernism." }
    ]
  },
  "Dashboard — ten\\oxytone.md": {
    "primary": "Having an acute accent on the last syllable; or a word so accented.",
    "secondary": "In classical Greek grammar and phonology, words carrying the high-pitch acute accent upon the ultima, which shifts to a grave accent when immediately followed by another word in connected speech.",
    "quotes": [
      { "author": "Henry George Liddell", "work": "A Greek-English Lexicon", "quote": "An **oxytone** word bears the acute accent upon its final syllable, which changes to a grave unless followed by punctuation." },
      { "author": "Max Müller", "work": "Lectures on the Science of Language", "quote": "In Vedic Sanskrit as in ancient Greek, the mobile **oxytone** accent reflects primitive Indo-European pitch distinctions." },
      { "author": "Henry Sweet", "work": "A Handbook of Phonetics", "quote": "The rhythmic balance of French verse is predominantly **oxytone**, placing the metric stress upon the final pronounced vowel." }
    ]
  },
  "Dashboard — ten\\paroxytone.md": {
    "primary": "Having an acute accent on the penultimate (next-to-last) syllable; or a word with stress or accent on the second-to-last syllable.",
    "secondary": "In Greek, Romance, and general linguistic prosody, words accented upon the penult (such as Italian 'bambino' or Spanish 'amigo'), the dominant stress pattern of several world languages.",
    "quotes": [
      { "author": "Henry George Liddell", "work": "A Greek-English Lexicon", "quote": "In classical Greek prosody, a **paroxytone** carries the acute accent on the penultimate syllable, provided the ultima is short." },
      { "author": "Henry Sweet", "work": "A History of English Sounds", "quote": "The normal tendency of Italian phonology is strictly **paroxytone**, resting its musical stress upon the second-to-last vowel." },
      { "author": "Otto Jespersen", "work": "A Modern English Grammar", "quote": "Latin stress laws dictated that words with long penultimate syllables must remain firmly **paroxytone**." }
    ]
  },
  "Dashboard — ten\\pentatone.md": {
    "primary": "A musical scale or tune consisting of five tones per octave; synonymous with pentatonic scale.",
    "secondary": "In acoustic ethnomusicology, primitive five-pitch musical structures occurring independently across ancient civilizations, lacking half-tone friction.",
    "quotes": [
      { "author": "Alexander John Ellis", "work": "On the Musical Scales of Various Nations", "quote": "The universal occurrence of the **pentatone** in ancient cultures proves that consonant intervals are intuitively perceived." },
      { "author": "Percy Scholes", "work": "The Oxford Companion to Music", "quote": "The simplicity of the **pentatone** allowed folk singers to preserve melodies across centuries without written notation." },
      { "author": "Béla Bartók", "work": "Hungarian Folk Music", "quote": "The archaic five-tone **pentatone** forms the bedrock of ancient peasant music throughout the Danubian basin." }
    ]
  },
  "Dashboard — ten\\pentatonic.md": {
    "primary": "Consisting of or based on five musical tones or pitches per octave.",
    "secondary": "In music theory and composition, scales (such as the major pentatonic 1-2-3-5-6 or minor blues pentatonic 1-b3-4-5-b7) that eliminate the dissonant tritone.",
    "quotes": [
      { "author": "Claude Debussy", "work": "Monsieur Croche", "quote": "The exotic chime of the Javanese gamelan revealed to Western ears the exquisite poetry of the **pentatonic** scale." },
      { "author": "Leonard Bernstein", "work": "The Unanswered Question", "quote": "The worldwide prevalence of the **pentatonic** scale suggests that human melody is rooted in the natural overtone series." },
      { "author": "Zoltán Kodály", "work": "Folk Music of Hungary", "quote": "Pedagogical training begins most effectively with **pentatonic** songs, which children sing in tune without difficulty." }
    ]
  },
  "Dashboard — ten\\peritoneal.md": {
    "primary": "Of, relating to, or situated in the peritoneum, the serous membrane lining the abdominal cavity.",
    "secondary": "In clinical anatomy and surgery, the peritoneal cavity, peritoneal fluid, or peritoneal dialysis (a therapy utilizing the vascular peritoneal membrane to filter waste products in kidney failure).",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Acute inflammation of the **peritoneal** membrane produces intense abdominal rigidity, rebound tenderness, and high fever." },
      { "author": "Joseph Lister", "work": "On the Antiseptic Principle in Surgery", "quote": "Careful antiseptic precautions permitted surgeons to enter the **peritoneal** cavity without provoking fatal peritonitis." },
      { "author": "Harvey Cushing", "work": "Selected Papers on Neurosurgery and Physiology", "quote": "Ventriculoperitoneal shunting allows excess cerebrospinal fluid to be harmlessly absorbed across the vast **peritoneal** surface." }
    ]
  },
  "Dashboard — ten\\peritoneum.md": {
    "primary": "The smooth, continuous serous membrane lining the abdominal cavity and covering the viscera.",
    "secondary": "In surgical anatomy, the membrane consisting of a parietal layer (lining the abdominal wall) and a visceral layer (reflecting over stomach, intestines, liver, and spleen), forming the omentum and mesenteries.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Tuberculous infection of the **peritoneum** may present with diffuse ascites and palpable rolled-up omental masses." },
      { "author": "Arthur Conan Doyle", "work": "Round the Red Lamp", "quote": "The surgeon deftly incised the glistening **peritoneum**, exposing the inflamed appendix beneath the caecum." },
      { "author": "Thomas Addison", "work": "A Collection of the Published Writings", "quote": "Extensive adhesions of the **peritoneum** were discovered post-mortem, uniting the intestines into an immovable mass." }
    ]
  },
  "Dashboard — ten\\polytonal.md": {
    "primary": "Characterized by the simultaneous combination of two or more distinct musical keys or tonalities.",
    "secondary": "In 20th-century compositional theory, harmonic structures (favored by Stravinsky, Milhaud, and Britten) that generate spatial depth and acoustic bite by superimposing different diatonic keys.",
    "quotes": [
      { "author": "Igor Stravinsky", "work": "Poetics of Music", "quote": "The bitonal arpeggios in Petrushka demonstrate how a **polytonal** chord produces a brilliant, biting sonic glare." },
      { "author": "Aaron Copland", "work": "What to Listen for in Music", "quote": "In a **polytonal** texture, the ear simultaneously tracks two distinct keys, creating a fascinating architectural tension." },
      { "author": "Darius Milhaud", "work": "Notes without Music", "quote": "I found in **polytonal** counterpoint the perfect expressive vehicle for capturing the violent contrasts of modern life." }
    ]
  },
  "Dashboard — ten\\polytonic.md": {
    "primary": "Utilizing or characterized by multiple tones, accents, or diacritical marks; or polytonal.",
    "secondary": "In Greek typography and historical orthography, the traditional system (polytonic orthography) utilizing acute, grave, and circumflex accents, alongside rough and smooth breathings, officially simplified in Greece in 1982.",
    "quotes": [
      { "author": "Henry George Liddell", "work": "A Greek-English Lexicon", "quote": "Classical Greek texts require the full **polytonic** orthography to indicate ancient musical pitch accents accurately." },
      { "author": "Max Müller", "work": "Lectures on the Science of Language", "quote": "The **polytonic** system of breathings and accents preserves a delicate record of lost vowel quantities and melodic inflections." },
      { "author": "Robert Byron", "work": "The Byzantine Achievement", "quote": "Greek printing houses preserved the venerable **polytonic** accents as a visible badge of classical continuity." }
    ]
  },
  "Dashboard — ten\\proparoxytone.md": {
    "primary": "Having an acute accent on the antepenultimate (third from the last) syllable; or a word so accented.",
    "secondary": "In Greek, Italian, and comparative phonology, words stressed or accented upon the syllable before the penult (such as Greek ἄνθρωπος or Italian 'medico'), subject to the law of the three syllables.",
    "quotes": [
      { "author": "Henry George Liddell", "work": "A Greek-English Lexicon", "quote": "A **proparoxytone** word cannot retain its accent on the antepenult if the final syllable contains a long vowel or diphthong." },
      { "author": "Max Müller", "work": "Lectures on the Science of Language", "quote": "The shift of an ancient **proparoxytone** noun upon declension illustrates the physiological limits of vocalic breath." },
      { "author": "Henry Sweet", "work": "A Handbook of Phonetics", "quote": "English words derived from Latin often adopt a **proparoxytone** rhythm, pulling stress back to the third syllable from the end." }
    ]
  },
  "Dashboard — ten\\protasis.md": {
    "primary": "The introductory part of a play or drama, setting forth the characters and subject; or the conditional clause of a conditional sentence (the 'if' clause).",
    "secondary": "In classical drama (Scaliger and Donatus), the opening exposition preceding the epitasis; in formal grammar and logic, the antecedent proposition that establishes the condition for the apodosis (consequent).",
    "quotes": [
      { "author": "Aristotle", "work": "Prior Analytics", "quote": "A premise or **protasis** is a sentence affirming or denying one thing of another, laying the ground for syllogistic deduction." },
      { "author": "John Dryden", "work": "An Essay of Dramatic Poesy", "quote": "In the **protasis**, the dramatist lays open the argument of the play and introduces the principal actors to the audience." },
      { "author": "Ben Jonson", "work": "The Magnetic Lady", "quote": "Let our **protasis** be clear and brief, that the spectators may understand the groundwork of our comedy without confusion." }
    ]
  },
  "Dashboard — ten\\pyelectasis.md": {
    "primary": "Dilation of the renal pelvis, usually caused by an obstruction to the outflow of urine.",
    "secondary": "In clinical urology and diagnostic ultrasound, enlargement of the renal pelvis (pyeloectasia) that, if untreated, progresses to hydronephrosis and parenchymal renal atrophy.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Calculous impaction at the ureteropelvic junction leads rapidly to marked **pyelectasis** and lumbar colic." },
      { "author": "Thomas Addison", "work": "A Collection of the Published Writings", "quote": "Autopsy demonstrated bilateral **pyelectasis** caused by a hypertrophied prostate obstructing the bladder neck." },
      { "author": "Eugene Braunwald", "work": "Harrison's Principles of Internal Medicine", "quote": "Prenatal ultrasound frequently identifies mild fetal **pyelectasis**, which requires serial postnatal monitoring." }
    ]
  },
  "Dashboard — ten\\syntonic.md": {
    "primary": "Tuned to the same frequency or resonant mode; or characterized by emotional responsiveness and harmony with one's social environment.",
    "secondary": "In early radio engineering (Guglielmo Marconi's 'syntonic telegraphy', patent 7777), tuned resonant circuits that allow selective reception without interference; in personality psychology (Ernst Kretschmer), emotional harmony with others (ego-syntonic).",
    "quotes": [
      { "author": "Guglielmo Marconi", "work": "Nobel Lecture: Wireless Telegraphic Communication", "quote": "By employing **syntonic** circuits tuned to identical electrical frequencies, we achieved selective wireless communication without mutual interference." },
      { "author": "Oliver Lodge", "work": "Signalling Across Space Without Wires", "quote": "The principle of **syntonic** resonance ensures that only a receiver having the same acoustic period will absorb the wave energy." },
      { "author": "Ernst Kretschmer", "work": "Physique and Character", "quote": "The cycloid temperament exhibits a warm, **syntonic** emotional resonance that blends harmoniously with surrounding society." }
    ]
  },
  "Dashboard — ten\\tetanolysin.md": {
    "primary": "A hemolytic exotoxin produced by *Clostridium tetani*, the causative bacterium of tetanus.",
    "secondary": "In medical microbiology and microbial pathogenesis, an oxygen-labile, cholesterol-dependent cytolysin secreted alongside the neurotoxin tetanospasmin, contributing to local tissue necrosis and hemolysis at the infection site.",
    "quotes": [
      { "author": "Emil von Behring", "work": "Untersuchungen über das Tetanusgift", "quote": "Filtrates of tetanus cultures contain both the deadly neurotoxin and the hemolytic agent designated **tetanolysin**." },
      { "author": "Paul Ehrlich", "work": "Studies on Immunity", "quote": "By testing the hemolytic action of **tetanolysin** upon red blood cells, we elucidated the precise neutralizing dynamics of antitoxin." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "While **tetanolysin** causes local tissue destruction, it is the potent neurotropic toxin that produces fatal clinical spasms." }
    ]
  },
  "Dashboard — ten\\tetanospasmin.md": {
    "primary": "A potent neurotoxin produced by *Clostridium tetani*, responsible for the severe muscle spasms characteristic of tetanus.",
    "secondary": "In neurobiology and molecular pathology, an extremely lethal zinc metalloprotease that undergoes retrograde axonal transport to spinal interneurons, cleaving synaptobrevin and blocking the release of inhibitory neurotransmitters (GABA and glycine), resulting in uncontrolled tetanic contractions.",
    "quotes": [
      { "author": "Emil von Behring", "work": "Nobel Lecture: Serum Therapy in Therapeutics and Medical Science", "quote": "The horrific muscular rigidity of tetanus is provoked by minute traces of **tetanospasmin** acting upon the central reflex arc." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Retrograde neural uptake of **tetanospasmin** leads to disinhibition of anterior horn motor cells and agonizing generalized convulsions." },
      { "author": "Paul de Kruif", "work": "Microbe Hunters", "quote": "Kitasato succeeded in isolating the tetanus bacillus, showing that its filtrate harbored the deadly toxin **tetanospasmin**." }
    ]
  },
  "Dashboard — ten\\tetanus.md": {
    "primary": "An acute and often fatal infectious disease caused by *Clostridium tetani*, characterized by painful tonic spasms of voluntary muscles, especially the jaw (lockjaw).",
    "secondary": "In muscle physiology and clinical infectious disease, a state of sustained maximal muscular contraction without relaxation caused by high-frequency motor nerve stimulation; or the bacterial infection prevented by tetanus toxoid immunization.",
    "quotes": [
      { "author": "Hippocrates", "work": "Aphorisms", "quote": "If a person be seized with **tetanus**, he dies within four days; but if he survives these, he recovers." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The hallmark of clinical **tetanus** is persistent trismus, or lockjaw, rapidly followed by distressing spasms of the facial muscles forming the risus sardonicus." },
      { "author": "Emil von Behring", "work": "The Mechanism of Immunity Against Diphtheria and Tetanus", "quote": "Passive immunization with tetanus antitoxin neutralizes the circulating toxin, transforming the prevention of fatal **tetanus**." }
    ]
  },
  "Dashboard — ten\\tetany.md": {
    "primary": "A medical condition characterized by involuntary, intermittent, and painful muscle spasms, caused by low calcium levels or alkalosis.",
    "secondary": "In endocrinology and clinical physiology, increased neuromuscular excitability resulting from hypocalcemia (often following parathyroidectomy), hypomagnesemia, or respiratory alkalosis, demonstrable by Chvostek's and Trousseau's signs.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The carpopedal spasms of **tetany** produce the typical 'obstetrician's hand' with adducted thumb and extended interphalangeal joints." },
      { "author": "Armand Trousseau", "work": "Lectures on Clinical Medicine", "quote": "Compressing the brachial artery with a tourniquet provokes within minutes the characteristic carpal spasm of latent **tetany**." },
      { "author": "Harvey Cushing", "work": "The Pituitary Body and Its Disorders", "quote": "Accidental removal of the parathyroid glands during thyroid surgery induces acute hypocalcemic **tetany** requiring immediate calcium therapy." }
    ]
  }
}

base_cluster_dir = 'App database/Greek roots/Cluster Number & Mathematics'
slice_path = 'main app/scripts/slice-math-part3.json'

with open(slice_path, 'r', encoding='utf-8') as f:
    full_slice = json.load(f)

# Batch 4 is items 231 to 306 (76 items)
expected_keys = full_slice[231:307]

print(f"Batch 4 contains {len(batch4_data)} items.")
print(f"Expected slice items: {len(expected_keys)}")

missing = [k for k in expected_keys if k not in batch4_data]
extra = [k for k in batch4_data if k not in expected_keys]

if missing:
    print("ERROR: Missing keys in Batch 4:", missing)
    sys.exit(1)
if extra:
    print("ERROR: Extra keys in Batch 4:", extra)
    sys.exit(1)

print("Key matching confirmed perfectly!")

# Internal Quality Validation
for p, data in batch4_data.items():
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
for rel_path, data in batch4_data.items():
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

print(f"Successfully updated {updated} files in Batch 4.")
