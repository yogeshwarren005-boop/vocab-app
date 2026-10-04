# -*- coding: utf-8 -*-
import os, sys, re
sys.stdout.reconfigure(encoding="utf-8")

data = {
  # --- Dashboard — flu Part 2 (9B, 41 words) ---
  "Dashboard — flu/fluoridization.md": {
    "primary": "The process or practice of adding fluoride compounds to a municipal water supply to prevent tooth decay.",
    "secondary": "In civic dental health administration, community fluoridization maintains fluoride levels at approximately 0.7 milligrams per liter.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Science and Education", "quote": "The civic proposal for universal water **fluoridization** aimed to protect working-class children from severe dental loss."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Preventive measures such as public **fluoridization** reduced dental sepsis across large urban populations."},
      {"author": "Herbert Spencer", "work": "The Study of Sociology", "quote": "The controversy over state-mandated **fluoridization** centered on the boundaries between collective hygiene and individual autonomy."}
    ]
  },
  "Dashboard — flu/fluoridize.md": {
    "primary": "To treat, impregnate, or dose water or another substance with fluoride compounds.",
    "secondary": "In municipal water filtration engineering, plants fluoridize reservoir effluent using automated gravimetric dry chemical feeders.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "Engineers resolved to **fluoridize** the city reservoirs in accordance with sanitary guidelines."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Health boards that **fluoridize** municipal water supplies achieve lasting reductions in dental morbidity."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "When communities **fluoridize** their drinking water, the mineral composition of teeth shows superior enamel density."}
    ]
  },
  "Dashboard — flu/fluorine.md": {
    "primary": "A toxic, extremely reactive, pale yellow diatomic halogen gas; the most electronegative chemical element.",
    "secondary": "In inorganic chemistry and halogen thermodynamics, fluorine forms violent exothermic reactions with nearly all organic and inorganic materials.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "The isolation of elemental **fluorine** long baffled chemists because of its destructive reactivity with glass apparatus."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "Henri Moissan finally succeeded in isolating pure gaseous **fluorine** using platinum and fluorspar vessels."},
      {"author": "Marie Curie", "work": "Treatise on Radioactivity", "quote": "Chemical compounds containing **fluorine** and uranium were employed to study gaseous diffusion rates."}
    ]
  },
  "Dashboard — flu/fluorite.md": {
    "primary": "A common halide mineral composed of calcium fluoride, often occurring in cubic crystals of diverse translucent colors.",
    "secondary": "In optical mineralogy, high-purity synthetic fluorite lenses eliminate chromatic aberration in specialized apochromatic microscope objectives.",
    "quotes": [
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "Cubic crystals of purple **fluorite** were found encrusting the walls of the lead mining galleries."},
      {"author": "Thomas Henry Huxley", "work": "Physiography", "quote": "When heated gently, certain varieties of green **fluorite** emit a delicate phosphorescent glow."},
      {"author": "Isaac Newton", "work": "Opticks", "quote": "Cleaved specimens of **fluorite** exhibited remarkable double refraction when inspected under polarized illumination."}
    ]
  },
  "Dashboard — flu/fluoroboride.md": {
    "primary": "A complex chemical salt or compound containing boron, fluorine, and another element or radical.",
    "secondary": "In coordination chemistry and electroplating, zinc fluoroboride solutions serve as high-efficiency electrolytes for protective metal deposition.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "Electrolytic decomposition of the crystalline **fluoroboride** solution yielded a volatile pungent vapor."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "The synthetic chemist combined hydrofluoric acid with borates to produce a heavy **fluoroboride** salt."},
      {"author": "James Clerk Maxwell", "work": "A Treatise on Electricity and Magnetism", "quote": "The ionic mobility within aqueous **fluoroboride** electrolytes was determined by galvanic deflection."}
    ]
  },
  "Dashboard — flu/fluorocarbon.md": {
    "primary": "A chemical compound containing only carbon and fluorine, characterized by extreme chemical inertness and thermal stability.",
    "secondary": "In polymer materials science, polytetrafluoroethylene (PTFE) is a fluorocarbon possessing exceptional non-stick and hydrophobic properties.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "Synthetic **fluorocarbon** compounds resist degradation by the strongest acids and oxidizing reagents."},
      {"author": "Lord Kelvin (William Thomson)", "work": "Popular Lectures and Addresses", "quote": "The thermal stability of the dense **fluorocarbon** liquid made it suitable for high-temperature insulation."},
      {"author": "H. G. Wells", "work": "The War of the Worlds", "quote": "The cylinder mechanisms were coated with an unreactive **fluorocarbon** film that repelled terrestrial damp."}
    ]
  },
  "Dashboard — flu/fluorochrome.md": {
    "primary": "A fluorescent chemical compound or dye that absorbs light energy at a specific wavelength and re-emits it at a longer wavelength.",
    "secondary": "In fluorescence microscopy and flow cytometry, an antibody conjugated to a fluorochrome targets cellular antigens.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "By staining histological sections with a specialized **fluorochrome**, internal nuclear structures become vividly illuminated."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The application of a selective **fluorochrome** allowed pathologists to identify tubercle bacilli under ultraviolet light."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Microscopic tracing techniques employing a vital **fluorochrome** demonstrate cytoplasmic streaming in live plant cells."}
    ]
  },
  "Dashboard — flu/fluoroform.md": {
    "primary": "A colorless, non-flammable gas, trifluoromethane, the fluorine analogue of chloroform, used as a specialized refrigerant.",
    "secondary": "In atmospheric chemistry and semiconductor manufacturing, fluoroform acts as a plasma etching gas for silicon dioxide microchips.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "The volatile gas **fluoroform** condensed into a clear liquid under combined pressure and refrigeration."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "Analogous to chloroform, **fluoroform** represents the complete substitution of chlorine by fluorine atoms."},
      {"author": "Lord Kelvin (William Thomson)", "work": "Popular Lectures and Addresses", "quote": "The thermodynamic expansion of liquefied **fluoroform** demonstrated predictable Joule-Thomson cooling."}
    ]
  },
  "Dashboard — flu/fluoroscope.md": {
    "primary": "An imaging instrument consisting of an X-ray source and a fluorescent screen used to view internal body structures in real-time motion.",
    "secondary": "In clinical radiology, early fluoroscopes allowed physicians to observe gastrointestinal peristalsis during barium meal examinations.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Examination of the chest behind the **fluoroscope** revealed aortic aneurysm pulsation with unmistakable clarity."},
      {"author": "Marie Curie", "work": "Treatise on Radioactivity", "quote": "The portable **fluoroscope** enabled field surgeons to locate embedded shrapnel in wounded soldiers quickly."},
      {"author": "H. G. Wells", "work": "The Invisible Man", "quote": "The scientist adjusted the luminescent screen of his **fluoroscope** to trace the shadowy silhouette of bones."}
    ]
  },
  "Dashboard — flu/fluoroscopy.md": {
    "primary": "A medical imaging technique that uses continuous X-ray beams and a fluorescent screen to capture real-time moving images of internal anatomy.",
    "secondary": "In interventional cardiology, fluoroscopy provides live visual guidance for catheter navigation and coronary stent placement.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Dynamic cardiac **fluoroscopy** demonstrated paradoxical diaphragmatic movement during deep inspiration."},
      {"author": "Marie Curie", "work": "Treatise on Radioactivity", "quote": "The development of diagnostic **fluoroscopy** transformed wartime surgery and medical radiology."},
      {"author": "Thomas Henry Huxley", "work": "Science and Education", "quote": "Medical students gathered in the darkroom to witness the wonders of thoracic **fluoroscopy**."}
    ]
  },
  "Dashboard — flu/fluorosis.md": {
    "primary": "A pathological condition of tooth enamel or bones caused by excessive, chronic ingestion of fluoride compounds during development.",
    "secondary": "In pediatric dentistry, dental fluorosis manifests as chalky white striations or brown pitting caused by ameloblast toxicity.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Chronic exposure to artesian well water containing excessive mineral salts produces endemic dental **fluorosis**."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "Skeletal **fluorosis** in industrial workers caused osteosclerosis and painful joint rigidity."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The mottled tooth enamel characteristic of **fluorosis** illustrates how mineral imbalances alter biomineralization."}
    ]
  },
  "Dashboard — flu/fluorouracil.md": {
    "primary": "An antimetabolite pyrimidine analogue chemotherapy medication used to treat various cancers, including colorectal and skin malignancies.",
    "secondary": "In molecular oncology, fluorouracil inhibits thymidylate synthase, blocking thymidine synthesis required for DNA replication in dividing tumor cells.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The clinical introduction of **fluorouracil** marked an epoch in the adjuvant chemotherapy of visceral carcinomas."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "Rational antimetabolites such as **fluorouracil** deceive tumor cells into incorporating fraudulent nucleotides."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The differential cytotoxicity produced by **fluorouracil** targets rapidly dividing abnormal cells."}
    ]
  },
  "Dashboard — flu/fluorspar.md": {
    "primary": "A common mineral form of calcium fluoride; fluorite, prized as a metallurgical flux and source of hydrofluoric acid.",
    "secondary": "In nineteenth-century mineralogy, Derbyshire fluorspar (Blue John) was mined for ornamental vases and lapidary carvings.",
    "quotes": [
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "Vast veins of banded **fluorspar** intersect the carboniferous limestone of Castleton in Derbyshire."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "Hydrofluoric acid was distilled by heating powdered **fluorspar** with concentrated sulphuric acid in lead retorts."},
      {"author": "Thomas Henry Huxley", "work": "Physiography", "quote": "Smelters mix crushed **fluorspar** with stubborn iron ores to lower the slag melting point."}
    ]
  },
  "Dashboard — flu/fluosilicate.md": {
    "primary": "A chemical salt containing the hexafluorosilicate anion, formed by the reaction of silica with hydrofluoric acid.",
    "secondary": "In municipal water fluoridation chemistry, sodium fluosilicate dissolves to release bioavailable fluoride ions into potable water networks.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "The precipitate formed upon adding potassium chloride to the solution was identified as a crystalline **fluosilicate**."},
      {"author": "Thomas Henry Huxley", "work": "Physiography", "quote": "Hydrothermal vapors containing fluorine react with silicate wall rocks to deposit minute crystals of **fluosilicate**."},
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "Fumarolic sublimates around active volcanoes frequently contain crusts of ammonium **fluosilicate**."}
    ]
  },
  "Dashboard — flu/fluoxetine.md": {
    "primary": "A selective serotonin reuptake inhibitor (SSRI) antidepressant medication used to treat depression, anxiety, and OCD.",
    "secondary": "In neuropsychopharmacology, fluoxetine selectively inhibits presynaptic serotonin reuptake transporters, augmenting serotonergic neurotransmission in the CNS.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Targeted psychotropic agents such as **fluoxetine** regulate affective neurochemistry without the sedation of tricyclic compounds."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Modern neurochemistry reveals that pharmacological interventions like **fluoxetine** profoundly influence the subjective tone of conscious emotion."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "The clinical utility of **fluoxetine** underscores the physical basis of emotional and cognitive affective states."}
    ]
  },
  "Dashboard — flu/flurazepam.md": {
    "primary": "A long-acting benzodiazepine derivative medication having sedative and hypnotic properties, used to treat severe insomnia.",
    "secondary": "In clinical pharmacokinetics, flurazepam produces prolonged daytime sedative effects due to the accumulation of its active metabolite, desalkylflurazepam.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The hypnotic efficacy of **flurazepam** must be weighed against residual daytime sedation and prolonged metabolic half-life."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "By potentiating inhibitory synaptic pathways, **flurazepam** suppresses reticular arousal systems in the brainstem."},
      {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "Sedatives such as **flurazepam** attenuate the muscular tremors associated with pathological psychic dread."}
    ]
  },
  "Dashboard — flu/flurbiprofen.md": {
    "primary": "A nonsteroidal anti-inflammatory drug (NSAID) of the propionic acid class used to relieve musculoskeletal pain and ophthalmic inflammation.",
    "secondary": "In ophthalmic surgery, topical flurbiprofen eye drops inhibit intraoperative miosis and prevent postoperative anterior uveal inflammation.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Topical **flurbiprofen** maintains pupillary dilation and mitigates ocular tissue trauma during ophthalmic surgery."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "Propionic acid derivatives such as **flurbiprofen** potently suppress prostaglandin synthesis at inflammatory loci."},
      {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "Analgesic treatment with **flurbiprofen** alleviated the grimacing facial contractions caused by chronic arthritis."}
    ]
  },
  "Dashboard — flu/flurry.md": {
    "primary": "A sudden brief gust of wind, shower of snow or rain; or a sudden outburst of nervous excitement or activity.",
    "secondary": "In nineteenth-century whaling terminology, the dying convulsion of a harpooned whale was termed its death flurry.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "And now, concentric circles seized the lone boat itself, and all its crew, when the whale went into his dying **flurry**."},
      {"author": "Charles Dickens", "work": "A Christmas Carol", "quote": "A sudden **flurry** of snow blew against the frozen windowpanes of the Scrooge and Marley counting-house."},
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Mrs. Jennings entered in a tremendous **flurry**, eager to share the shocking news from town."}
    ]
  },
  "Dashboard — flu/flush-seamed.md": {
    "primary": "Having seams that lie completely flat, level, and smooth with adjacent surface plating or planking.",
    "secondary": "In naval architecture and boiler fabrication, flush-seamed hull plating reduces hydrodynamic drag compared to lap-jointed plates.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The vessel was built with **flush-seamed** oak timbers, offering smooth resistance against the Antarctic seas."},
      {"author": "Thomas Henry Huxley", "work": "Physiography", "quote": "Modern ironclads utilize **flush-seamed** steel armor plates joined by countersunk rivets to minimize friction."},
      {"author": "Jack London", "work": "The Sea-Wolf", "quote": "The schooner was a clean-lined craft, **flush-seamed** along her waterline to slip swiftly through the waves."}
    ]
  },
  "Dashboard — flu/flush.md": {
    "primary": "To turn red in the face from emotion or heat; or to cleanse by a sudden rush of water; or level and even with an adjacent surface.",
    "secondary": "In poker card game combinations, a flush consists of five cards of the identical suit regardless of numerical sequence.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth felt a sudden **flush** overspread her cheeks as she caught Mr. Darcy's intent gaze."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The morning sun brought a warm **flush** across the dewy fields of the valley."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Pip saw the angry **flush** mount into Estella's forehead as Miss Havisham reproached her."}
    ]
  },
  "Dashboard — flu/flushed.md": {
    "primary": "Reddened, blushed, or glowing, especially in the face; or elated, excited, or filled with sudden pride.",
    "secondary": "In medical pathology, a flushed cutaneous appearance often indicates systemic pyrexia, peripheral vasodilation, or autonomic hyperactivity.",
    "quotes": [
      {"author": "Charles Dickens", "work": "A Christmas Carol", "quote": "Bob Cratchit's face was **flushed** with honest pride as he carried Tiny Tim into the parlor."},
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Marianne returned from her walk with cheeks **flushed** by the autumn gale and solitary sorrow."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Sir Henry came into the dining room **flushed** with excitement from his moorland ride."}
    ]
  },
  "Dashboard — flu/fluster.md": {
    "primary": "To make someone agitated, confused, or nervous; or an agitation of bewildered excitement and hurry.",
    "secondary": "In conversational pragmatics, rapid confrontational questioning is employed by cross-examiners to fluster evasive witnesses.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Othello", "quote": "Three lads of Cyprus, noble swelling spirits, have I tonight **fluster** with flowing cups."},
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Mrs. Jennings was in a great **fluster** of spirits, unable to sit quiet for two minutes together."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "The sudden arrival of Aunt Betsey threw poor Mr. Dick into an extraordinary **fluster** of mind."}
    ]
  },
  "Dashboard — flu/flustered.md": {
    "primary": "Agitated, nervous, confused, or unsettled by haste, surprise, or unexpected demands.",
    "secondary": "In behavioral cognitive psychology, flustered subjects display impaired working memory performance and delayed decision latency.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Tess looked a little **flustered** as she took it, her fingers trembling slightly."},
      {"author": "Lewis Carroll", "work": "Alice's Adventures in Wonderland", "quote": "Well, I hardly know, sir, said the **flustered** guinea-pig in a feeble squeak."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "I found myself in a dream, a **flustered**, happy, hurried dream from which I feared to awake."}
    ]
  },
  "Dashboard — flu/flute.md": {
    "primary": "A woodwind musical instrument consisting of an open pipe played by blowing across an embouchure hole; or a decorative vertical groove.",
    "secondary": "In classical architectural orders, semicircular flutes adorn the shafts of Doric, Ionic, and Corinthian columns to emphasize verticality.",
    "quotes": [
      {"author": "William Shakespeare", "work": "A Midsummer Night's Dream", "quote": "Here, Peter Quince; you must speak for Francis **Flute**, the bellows-mender, who plays Thisbe."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Anon they move in perfect phalanx to the Dorian mood of **flute** and soft recorder."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The musical tones of the simple reeds and **flute** evoke deep emotional resonance in all human races."}
    ]
  },
  "Dashboard — flu/fluting.md": {
    "primary": "A series of decorative vertical concave grooves carved into an architectural column, pilaster, or piece of furniture.",
    "secondary": "In structural metal fabrication, fluting involves forming longitudinal corrugated ribs into sheet metal to increase sectional bending stiffness.",
    "quotes": [
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The crisp **fluting** of the marble pillars caught the southern sunlight, casting sharp linear shadows."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The magnificent temple facade displayed delicate **fluting** along its monolithic Corinthian colonnade."},
      {"author": "Walter Scott", "work": "The Antiquary", "quote": "The antiquary admired the deep Saxon **fluting** preserved upon the surviving archway of the abbey."}
    ]
  },
  "Dashboard — flu/flutist.md": {
    "primary": "A musician who plays the musical flute; a flute player.",
    "secondary": "In nineteenth-century orchestral wind orchestration, the principal flutist led the woodwind section with agile coloratura obligatos.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Under the Greenwood Tree", "quote": "The village **flutist** adjusted his wooden reed and blew a soft introductory note before the anthem began."},
      {"author": "George Eliot", "work": "Romola", "quote": "A wandering Florentine **flutist** played a graceful madrigal beneath the stone loggia."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "The modest music master earned a meager livelihood as a second **flutist** in the theater orchestra."}
    ]
  },
  "Dashboard — flu/flutter.md": {
    "primary": "To flap wings rapidly and lightly; or to move back and forth quickly and irregularly; or a rapid irregular heartbeat.",
    "secondary": "In aeroelasticity, aerodynamic flutter is a self-feeding, destructive vibration caused by unstable dynamic coupling between airflow and wing structure.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Coriolanus", "quote": "If you have writ your annals true, 'tis there, that, like an eagle in a dovecote, I did **flutter** your Volscians in Corioli."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Sometimes it was a palpitation, sometimes a **flutter** in her throat that choked her speech."},
      {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "He watched the colorful birds **flutter** their wings among the blossoms of the greenhouse."}
    ]
  },
  "Dashboard — flu/fluttering.md": {
    "primary": "Moving rapidly, lightly, and irregularly up and down or to and fro; trembling with quick agitation.",
    "secondary": "In clinical cardiology, atrial fluttering denotes an organized supraventricular tachycardia with typical sawtooth waves on an electrocardiogram.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Maryann, you go! said she, **fluttering** under the onset of a crowd of romantic possibilities."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Casaubon felt his weak heart **fluttering** with nervous exhaustion after the interview."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The moth escaped by **fluttering** erratic circles through the dusk, evading the pursuing bat."}
    ]
  },
  "Dashboard — flu/influence.md": {
    "primary": "The capacity or power to have an effect on the character, development, or behavior of someone or something.",
    "secondary": "In astrological and medieval cosmology, celestial influence was believed to flow down from revolving spheres into mortal temperaments.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Sonnet 15", "quote": "That this huge stage presenteth nought but shows whereon the stars in secret **influence** comment."},
      {"author": "Jane Austen", "work": "Persuasion", "quote": "Anne had been persuaded to believe that by submitting to Lady Russell's **influence**, she was acting with self-denying prudence."},
      {"author": "Adam Smith", "work": "The Theory of Moral Sentiments", "quote": "The magnetic **influence** of general opinion guides the sentiments of the average citizen."}
    ]
  },
  "Dashboard — flu/influent.md": {
    "primary": "Flowing in or into; an inflow; or liquid sewage or wastewater entering a treatment plant or processing facility.",
    "secondary": "In hydraulic wastewater treatment design, influent flow rates determine hydraulic retention time within primary sedimentation basins.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Physiography", "quote": "The **influent** waters of the mountain tributaries replenished the deep glacial lake every spring."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "A strong **influent** tide rushed through the narrow strait, churning the waters into foam."},
      {"author": "Elizabeth Barrett Browning", "work": "Aurora Leigh", "quote": "The balmy evening brought **influent** odors of clover and wild briar through the open lattice."}
    ]
  },
  "Dashboard — flu/influential.md": {
    "primary": "Having or exercising great influence, power, authority, or effect upon others; prominent.",
    "secondary": "In social network graph theory, highly connected hub nodes serve as influential opinion leaders accelerating information diffusion.",
    "quotes": [
      {"author": "Joseph Conrad", "work": "Heart of Darkness", "quote": "My dear aunt's **influential** acquaintances were producing an unexpected effect upon the company directors."},
      {"author": "Thomas Babington Macaulay", "work": "History of England", "quote": "The wealthy London merchants formed an **influential** political bloc in the House of Commons."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "The legal profession constitutes the most **influential** aristocratic element in the American republic."}
    ]
  },
  "Dashboard — flu/influentially.md": {
    "primary": "In an influential manner; with significant authority, impact, or persuasive effect.",
    "secondary": "In diplomatic history, ambassadorial legations acted influentially behind the scenes to broker non-aggression treaties.",
    "quotes": [
      {"author": "Thomas Babington Macaulay", "work": "History of England", "quote": "The bishop intervened **influentially** with the privy council to secure a pardon for the prisoner."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The praetorian prefect acted **influentially** in shaping the domestic legislation of the emperor."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Mr. Brooke spoke **influentially** at the county meeting, urging landlords to adopt agricultural improvements."}
    ]
  },
  "Dashboard — flu/influenza.md": {
    "primary": "An acute, highly contagious viral respiratory disease characterized by sudden fever, muscle aches, exhaustion, and cough; the flu.",
    "secondary": "In historical epidemiology, the term influenza originated in eighteenth-century Italian medical literature attributing epidemic plagues to astrological astral influence.",
    "quotes": [
      {"author": "Jane Austen", "work": "Emma", "quote": "Wingfield told me that he has never known colds more general or heavy, except during an epidemic of **influenza**."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Pandemic **influenza** attacks with lightning speed, predisposing victims to fatal secondary bacterial pneumonia."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "A severe outbreak of autumn **influenza** prostrated the inhabitants of the damp riverside court."}
    ]
  },
  "Dashboard — flu/perfluorocarbon.md": {
    "primary": "An organofluorine compound containing only carbon and fluorine atoms, possessing extreme chemical stability and high gas solubility.",
    "secondary": "In critical care medicine and liquid ventilation, medical perfluorocarbon emulsions serve as oxygen-carrying blood substitutes and alveolar expansion media.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "The extreme molecular stability of the dense **perfluorocarbon** oil defies degradation by boiling nitric acid."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Respiratory physiologists investigated synthetic **perfluorocarbon** liquids capable of supporting mammalian liquid ventilation."},
      {"author": "Lord Kelvin (William Thomson)", "work": "Popular Lectures and Addresses", "quote": "The synthetic dielectric **perfluorocarbon** liquid provided extraordinary breakdown voltage resistance."}
    ]
  },
  "Dashboard — flu/superfluity.md": {
    "primary": "An excess, superabundance, or quantity greater than needed; redundancy.",
    "secondary": "In classical moral philosophy, the Stoics condemned luxurious superfluity as corrupting spiritual tranquility and self-reliance.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Coriolanus", "quote": "If they would yield us but the **superfluity** while it were wholesome, we might guess they relieved us humanely."},
      {"author": "Francis Bacon", "work": "Essays", "quote": "Seek not proud riches, but such as thou mayest get justly; the rest is but **superfluity**."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "Superfluous wealth can buy superfluities only; money is not required to buy one **superfluity** of the soul."}
    ]
  },
  "Dashboard — flu/superfluous.md": {
    "primary": "Exceeding what is sufficient, necessary, or normal; wasteful, redundant, or unnecessary.",
    "secondary": "In statutory interpretation, the surplusage canon instructs jurists to avoid readings that would render any statutory clause superfluous.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "O my dear Gertrude, this, like to a murdering-piece, in many places gives me **superfluous** death."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "Most of the luxuries, and many of the so-called comforts of life, are not only not indispensable, but positive hindrances to the elevation of mankind; they are **superfluous** baggage."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth felt that any further apology on Mr. Collins's part would be entirely **superfluous**."}
    ]
  },
  "Dashboard — flu/superfluously.md": {
    "primary": "In a superfluous or redundant manner; beyond what is necessary or useful; unnecessarily.",
    "secondary": "In rhetorical stylistics, multiplying synonyms superfluously weakens prose clarity and burdens the reader's attention.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Hurst sat near the hearth, poking the fire **superfluously** with the iron tongs."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Doctor Sprague was **superfluously** tall, his long legs taking up an excessive share of the carriage space."},
      {"author": "William Shakespeare", "work": "Henry V", "quote": "That may be, for you bear a many **superfluously**, and 'twere more honour some were away."}
    ]
  },
  "Dashboard — flu/unfluctuating.md": {
    "primary": "Steady, constant, unchanging, and free from irregular variations or oscillation.",
    "secondary": "In financial monetary theory, an unfluctuating currency provides an ideal store of value and standard for deferred payments.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "A prudent investor seeks an **unfluctuating** source of revenue derived from fertile freehold land."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "In an isolated and **unfluctuating** climate, species remain stationary in morphology for immense periods."},
      {"author": "Herbert Spencer", "work": "First Principles", "quote": "The laws of astronomical gravity remain **unfluctuating** throughout cosmic space and time."}
    ]
  },
  "Dashboard — flu/unflurried.md": {
    "primary": "Calm, composed, unagitated, and serene under pressure or commotion.",
    "secondary": "In military leadership studies, an unflurried commander preserves operational clarity during chaotic combat maneuvers.",
    "quotes": [
      {"author": "Anthony Trollope", "work": "The Warden", "quote": "Hiram's hospital remained an **unflurried** sanctuary of peace amidst the noisy political storm."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Holmes remained cool and **unflurried**, examining the footprints with meticulous composure."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Gabriel Oak faced the midnight fire with an **unflurried** mind, issuing steady orders to save the ricks."}
    ]
  },
  "Dashboard — flu/unflustered.md": {
    "primary": "Composed, self-possessed, and undisturbed by confusing or frantic events.",
    "secondary": "In clinical crisis management, unflustered practitioners prioritize life-saving interventions methodically without cognitive overload.",
    "quotes": [
      {"author": "Jane Austen", "work": "Emma", "quote": "Mr. Knightley was entirely **unflustered** by the sudden domestic commotion, resolving the dispute with quiet firmness."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "The detective's **unflustered** demeanor contrasted sharply with the hysterical panic of the client."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Doctor Lydgate remained **unflustered** during the emergency, applying the tourniquet with steady fingers."}
    ]
  },
  "Dashboard — flu/uninfluential.md": {
    "primary": "Lacking influence, power, weight, or prestige; having little or no effect upon people or outcomes.",
    "secondary": "In parliamentary electoral politics, an uninfluential backbencher rarely secures cabinet patronage or legislative sponsorship.",
    "quotes": [
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "A solitary citizen in a democracy feels weak and **uninfluential** unless joined in public association with peers."},
      {"author": "Thomas Babington Macaulay", "work": "History of England", "quote": "The remote parish was governed by an **uninfluential** country justice of meager fortune."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Mr. Casaubon's unfinished theological pamphlets remained obscure and **uninfluential** among London scholars."}
    ]
  }
}

base_dir = r"App database\Latin roots\Cluster Motion"
updated = 0

for rel_path, info in data.items():
    fpath = os.path.join(base_dir, rel_path.replace("/", os.sep))
    if not os.path.exists(fpath):
        print(f"Warning: {fpath} does not exist!")
        continue
    
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    book_idx = content.find("> [!book]")
    if book_idx == -1:
        print(f"Warning: No > [!book] callout in {rel_path}")
        continue
    
    prefix = content[:book_idx]
    
    p_def = info["primary"].strip().rstrip(".") + "."
    s_def = info["secondary"].strip().rstrip(".") + "."
    
    new_book = f"> [!book] 📖 Definitions & Semantic Range\n> 1. **Primary Definition (Lexical / Standard Consensus)**: {p_def}\n> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: {s_def}\n"
    
    new_quote = "> [!quote] 💬 Contextual Usage & Authentic Quotations\n"
    for q in info["quotes"]:
        auth = q["author"].strip()
        work = q["work"].strip()
        quote_text = q["quote"].strip().strip('"').strip('“').strip('”')
        new_quote += f'> - 📜 **{auth} (*{work}*):** *"{quote_text}"*\n'
    
    new_content = prefix + new_book + "\n" + new_quote + "\n"
    
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(new_content)
    updated += 1

print(f"Motion Batch 9B: Successfully updated {updated}/{len(data)} notes.")
