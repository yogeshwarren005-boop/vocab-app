# -*- coding: utf-8 -*-
import json
import os
import sys

batch3_data = {
  "Dashboard — poly\\polyuria.md": {
    "primary": "The production or passage of abnormally large volumes of urine.",
    "secondary": "In clinical nephrology and endocrinology, excessive urinary excretion (typically exceeding 3 liters daily in adults) classically signaling uncontrolled diabetes mellitus, diabetes insipidus, or psychogenic polydipsia.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The hallmark symptoms of onset diabetes are polydipsia, unquenchable hunger, and persistent, copious **polyuria**." },
      { "author": "Thomas Addison", "work": "A Collection of the Published Writings of the Late Thomas Addison", "quote": "In diabetes insipidus, the **polyuria** is clear and of low specific gravity, without the presence of glucose." },
      { "author": "Claude Bernard", "work": "Lectures on the Physiology of the Nervous System", "quote": "Puncture of the fourth ventricle in rabbits induces immediate transient glycosuria accompanied by intense **polyuria**." }
    ]
  },
  "Dashboard — psall\\psalm.md": {
    "primary": "A sacred song, hymn, or lyric poem used in Christian or Jewish religious worship, especially one of the 150 biblical psalms.",
    "secondary": "In religious liturgy and biblical Hebrew poetry, sacred lyrics (Tehillim) marked by semantic parallelism and historically chanted to the accompaniment of plucked string instruments.",
    "quotes": [
      { "author": "John Milton", "work": "Paradise Lost", "quote": "Hymns and heavenly **psalms** they sang, echoing through the wide crystalline spheres of heaven." },
      { "author": "William Shakespeare", "work": "Henry V", "quote": "Do we all holy rites: let there be sung 'Non nobis' and 'Te Deum', the dead with charity enclos'd in clay, and every solemn **psalm**." },
      { "author": "George Herbert", "work": "The Temple", "quote": "A verse may find him who a sermon flies, and a sweet **psalm** turn mourning into praise." }
    ]
  },
  "Dashboard — psall\\psalmist.md": {
    "primary": "A composer, writer, or singer of sacred songs or psalms; specifically King David, traditionally credited with the biblical Psalms.",
    "secondary": "In biblical hermeneutics and liturgical history, an inspired devotional poet whose verses articulate the full gamut of human spiritual longing, penitence, and thanksgiving.",
    "quotes": [
      { "author": "Samuel Johnson", "work": "The Rambler", "quote": "As the sweet **psalmist** of Israel observed, our days on earth are as a shadow that passes away." },
      { "author": "Thomas Browne", "work": "Religio Medici", "quote": "With the inspired **psalmist**, I marvel at the wonder of our creation, curiously and wonderfully made in secret." },
      { "author": "John Bunyan", "work": "Grace Abounding to the Chief of Sinners", "quote": "The words of the holy **psalmist** broke into my heart like a beam of celestial light, dissolving my despair." }
    ]
  },
  "Dashboard — psall\\psalmodicon.md": {
    "primary": "A single-stringed bowed zither or musical instrument developed in 19th-century Scandinavia to accompany church psalm-singing.",
    "secondary": "In organology and hymnology, an educational folk instrument invented by Swedish clergyman Johannes Dillner in 1829, utilizing a fretted fingerboard and numerical tablature (sifferskrift) to teach sacred choral melody without pipe organs.",
    "quotes": [
      { "author": "Johannes Dillner", "work": "Melodier till Swenska Kyrkans Psalmer", "quote": "With the simple wooden **psalmodicon**, every rural parish congregation can learn the sacred chorales with true pitch." },
      { "author": "Percy Scholes", "work": "The Oxford Companion to Music", "quote": "The single-stringed **psalmodicon** spread across Scandinavian and immigrant American settlements as an economical substitute for church organs." },
      { "author": "Alexander John Ellis", "work": "On the History of Musical Pitch", "quote": "The fretted fingerboard of the **psalmodicon** provided a reliable empirical standard for measuring traditional Nordic vocal intervals." }
    ]
  },
  "Dashboard — psall\\psalmody.md": {
    "primary": "The act, practice, or art of singing psalms or sacred hymns in religious worship; or a collection of psalms set to music.",
    "secondary": "In church music history, the communal chanting or singing of metrical psalms, central to Reformed, Puritan, and Anglican worship since the Geneva Psalter of the 16th century.",
    "quotes": [
      { "author": "Herman Melville", "work": "Moby-Dick", "quote": "The solemn sound of their **psalmody** floated across the water, rising and falling with the rhythm of the waves." },
      { "author": "Washington Irving", "work": "The Sketch Book of Geoffrey Crayon", "quote": "The village choir opened the Christmas service with a vigorous burst of rustic **psalmody** led by the parish clerk." },
      { "author": "Jonathan Edwards", "work": "A Faithful Narrative of the Surprising Work of God", "quote": "Our public assemblies were enlivened with harmonious **psalmody**, each singer pouring forth heartfelt devotion." }
    ]
  },
  "Dashboard — psall\\psalter.md": {
    "primary": "A volume containing the biblical Book of Psalms, often arranged for liturgical, devotional, or choral use.",
    "secondary": "In medieval codicology and manuscript illumination, a richly decorated prayer book containing liturgical calendars, canticles, and the litany of saints, serving as the central personal devotional text for nobility.",
    "quotes": [
      { "author": "Geoffrey Chaucer", "work": "The Canterbury Tales", "quote": "And on her arm she bore a rosary of coral beads, and in her hand an illuminated **psalter** bound in silk." },
      { "author": "John Ruskin", "work": "The Bible of Amiens", "quote": "The 13th-century illuminated **psalter** preserves the purest medieval Gothic drawing in its vibrant marginal vignettes." },
      { "author": "Thomas More", "work": "Dialogue Concerning Heresies", "quote": "Devout layfolk found solace in reciting the seven penitential psalms from the Latin **psalter** during morning prayer." }
    ]
  },
  "Dashboard — psall\\psaltery.md": {
    "primary": "An ancient and medieval musical instrument consisting of strings stretched across a flat soundboard, played by plucking with fingers or plectra.",
    "secondary": "In music history and biblical organology, a stringed instrument (derived from Greek *psalterion*) representing a precursor to the harpsichord and dulcimer, widely depicted in Romanesque and Gothic sacred art.",
    "quotes": [
      { "author": "Geoffrey Chaucer", "work": "The Canterbury Tales", "quote": "And all above there lay a gay **psaltery**, on which he made at night melodious minstrelsy." },
      { "author": "John Milton", "work": "Samson Agonistes", "quote": "Praise him with the sound of the trumpet, praise him with the lute and the sweet **psaltery**." },
      { "author": "Charles Burney", "work": "A General History of Music", "quote": "The triangular medieval **psaltery** was plucked with quill plectra, producing a bright and silvery resonance." }
    ]
  },
  "Dashboard — psall\\psaltikon.md": {
    "primary": "A liturgical choirbook of the Byzantine rite containing the florid, melismatic solo chants for the soloist (psaltes).",
    "secondary": "In Byzantine musicology and paleography, a medieval music manuscript (developed between the 10th and 14th centuries) containing the elaborate musical notation for prokeimena, alleluiaria, and kontakia.",
    "quotes": [
      { "author": "Egon Wellesz", "work": "A History of Byzantine Music and Hymnography", "quote": "The ornate melodies preserved in the **psaltikon** were reserved for the virtuosic soloist standing upon the ambo." },
      { "author": "Oliver Strunk", "work": "Essays on Music in the Byzantine World", "quote": "Neumatic notation in the medieval **psaltikon** records the precise melismatic ornamentation practiced in Hagia Sophia." },
      { "author": "Percy Scholes", "work": "The Oxford Companion to Music", "quote": "While the asmatikon contained simple choral responses, the **psaltikon** preserved the elaborate chants of the precentor." }
    ]
  },
  "Dashboard — pto\\anaptotic.md": {
    "primary": "Characterized by the loss, shedding, or simplification of grammatical inflections or case endings; analytic.",
    "secondary": "In historical and comparative linguistics, evolutionary language change whereby synthetic, inflected tongues (like Old English or Latin) evolve into analytic, uninflected systems relying on word order and prepositions.",
    "quotes": [
      { "author": "Max Müller", "work": "Lectures on the Science of Language", "quote": "The transition of synthetic tongues into an **anaptotic** condition demonstrates the triumph of grammatical economy." },
      { "author": "Henry Sweet", "work": "A New English Grammar", "quote": "Modern English is a thoroughly **anaptotic** language, having replaced complex noun declensions with auxiliary prepositions." },
      { "author": "Otto Jespersen", "work": "Progress in Language", "quote": "The progress of Indo-European tongues toward an **anaptotic** structure is not decay, but a rationalization of syntax." }
    ]
  },
  "Dashboard — pto\\apoptosis.md": {
    "primary": "The death of cells that occurs as a normal and controlled part of an organism's growth or development; programmed cell death.",
    "secondary": "In cellular biology and oncology, a genetically regulated suicide cascade characterized by cell shrinkage, membrane blebbing, nuclear fragmentation, and caspase activation, preventing inflammation in adjacent tissues.",
    "quotes": [
      { "author": "Sydney Brenner", "work": "Nobel Lecture: Nature's Gift to Science", "quote": "Mapping the exact genetic lineage of Caenorhabditis elegans revealed how precisely programmed **apoptosis** sculpts developing tissues." },
      { "author": "Lewis Thomas", "work": "The Fragile Species", "quote": "Cellular suicide through **apoptosis** is nature's quiet, tidy way of eliminating damaged or redundant cells without harm." },
      { "author": "Robert A. Weinberg", "work": "The Biology of Cancer", "quote": "Evasion of **apoptosis** is one of the essential hallmarks acquired by cells during the process of malignant transformation." }
    ]
  },
  "Dashboard — pto\\asymptomatic.md": {
    "primary": "Producing or showing no symptoms of disease or infection.",
    "secondary": "In epidemiology, public health, and diagnostic medicine, individuals carrying a pathogen or harboring pathology (such as hypertension or subclinical viral infection) without clinical illness, while remaining capable of transmission.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Renal arteriolosclerosis may remain entirely **asymptomatic** for decades until discovered during routine physical examination." },
      { "author": "Paul de Kruif", "work": "Microbe Hunters", "quote": "Mary Mallon was a perfectly healthy, **asymptomatic** typhoid carrier, scattering virulent bacilli wherever she cooked." },
      { "author": "Eugene Braunwald", "work": "Heart Disease", "quote": "Silent myocardial ischemia presents an **asymptomatic** electrocardiographic warning that demands proactive clinical intervention." }
    ]
  },
  "Dashboard — pto\\peripeteia.md": {
    "primary": "A sudden reversal of fortune or change in circumstances, especially in a dramatic or narrative work.",
    "secondary": "In Aristotelian poetics and literary criticism, the critical turning point (*peripeteia*) in a tragedy where an action produces the exact opposite of its intended result, ideally accompanied by anagnorisis (recognition).",
    "quotes": [
      { "author": "Aristotle", "work": "Poetics", "quote": "A **peripeteia** is a change by which the action veers round to its opposite, subject always to our rule of probability." },
      { "author": "Samuel Taylor Coleridge", "work": "Lectures on Shakespeare", "quote": "In the catastrophe of Othello, the **peripeteia** overwhelms the spectator with an agonizing realization of fatal deception." },
      { "author": "George Steiner", "work": "The Death of Tragedy", "quote": "Classical tragedy pivots upon that swift, merciless **peripeteia** which hurls the sovereign from his throne into blind exile." }
    ]
  },
  "Dashboard — pto\\peripety.md": {
    "primary": "A sudden and unexpected change of fortune or dramatic reversal of circumstances; anglicized form of peripeteia.",
    "secondary": "In narrative theory and dramatic composition, the crucial structural pivot in a plot where the protagonist's fortunes precipitously reverse from prosperity to downfall.",
    "quotes": [
      { "author": "John Dryden", "work": "An Essay of Dramatic Poesy", "quote": "The sudden **peripety** in the fourth act shifts the whole sympathy of the audience toward the fallen prince." },
      { "author": "Henry James", "work": "The Art of the Novel", "quote": "The story gathers its suspense toward a quiet moral **peripety** where all former relationships are inverted." },
      { "author": "Thomas De Quincey", "work": "Biographical Essays", "quote": "History affords no more astonishing **peripety** than the fall of Napoleon from the mastery of Europe to St. Helena." }
    ]
  },
  "Dashboard — pto\\polyptoton.md": {
    "primary": "A rhetorical figure of speech in which words derived from the same root are repeated in different grammatical forms or cases.",
    "secondary": "In classical rhetoric and stylistics, an emphatic device (such as 'with eager feeding food doth choke the feeder') that exploits morphological variations of a common lexeme to underline irony, antithesis, or intensification.",
    "quotes": [
      { "author": "Quintilian", "work": "Institutio Oratoria", "quote": "In **polyptoton**, the repetition of the same root in varied cases lends elegance and lively variety to the sentence." },
      { "author": "William Shakespeare", "work": "Richard II", "quote": "The line 'with eager feeding food doth choke the feeder' exemplifies the concentrated force of rhetorical **polyptoton**." },
      { "author": "George Puttenham", "work": "The Arte of English Poesie", "quote": "Our poets use **polyptoton**, which we call the traducer, turning one word into diverse cases and endings to grace the verse." }
    ]
  },
  "Dashboard — pto\\proptosis.md": {
    "primary": "An abnormal protrusion or forward displacement of an organ, especially the eyeball.",
    "secondary": "In ophthalmology and endocrinology, forward protrusion of the globe (exophthalmos) caused by thyroid eye disease (Graves' orbitopathy), orbital tumors, retrobulbar hematoma, or cavernous sinus thrombosis.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Bilateral **proptosis** accompanied by fine finger tremors and tachycardia forms the hallmark of Graves' disease." },
      { "author": "Harvey Cushing", "work": "Meningiomas: Their Classification and Surgical Pathology", "quote": "Slowly progressive unilateral **proptosis** directed our surgical approach toward the sphenoid ridge meningioma." },
      { "author": "Jonathan Hutchinson", "work": "Illustrations of Clinical Surgery", "quote": "Severe orbital cellulitis induces marked **proptosis** and chemosis, endangering vision if decompression is delayed." }
    ]
  },
  "Dashboard — pto\\proptotic.md": {
    "primary": "Pertaining to, affected by, or exhibiting proptosis; protruding forward abnormally.",
    "secondary": "In clinical ophthalmology and maxillofacial surgery, describing an eyeball or orbital tissue displaced anteriorly due to space-occupying lesions or inflammatory edema.",
    "quotes": [
      { "author": "Harvey Cushing", "work": "Intracranial Tumours", "quote": "The patient presented with a markedly **proptotic** left eye displaced downward by a fronto-orbital osteoma." },
      { "author": "William Osler", "work": "Modern Medicine", "quote": "Exposure keratitis frequently develops in a severely **proptotic** globe because the eyelids cannot fully close." },
      { "author": "W. Russell Brain", "work": "Diseases of the Nervous System", "quote": "A pulsating **proptotic** eye with an audible orbital bruit is pathognomonic of a carotid-cavernous fistula." }
    ]
  },
  "Dashboard — pto\\ptomaine.md": {
    "primary": "Any of various basic nitrogenous organic compounds produced by the bacterial decomposition of proteins; historically associated with food poisoning.",
    "secondary": "In 19th-century toxicology and organic chemistry, foul-smelling polyamines (such as putrescine and cadaverine) erroneously believed to be the primary pathogenic agents in spoiled food intoxications.",
    "quotes": [
      { "author": "Arthur Conan Doyle", "work": "The Adventure of the Devil's Foot", "quote": "The chemist suggested a mysterious vegetable alkaloid or some deadly animal **ptomaine** generated in putrefaction." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Many cases formerly diagnosed as **ptomaine** poisoning are now recognized as acute Salmonella or botulinum toxin infections." },
      { "author": "Paul de Kruif", "work": "Microbe Hunters", "quote": "Bacteriologists proved that living bacterial toxins, rather than harmless cadaveric **ptomaine** bases, caused epidemic dysentery." }
    ]
  },
  "Dashboard — pto\\ptosis.md": {
    "primary": "An abnormal drooping or falling of the upper eyelid; or the prolapse of an internal organ.",
    "secondary": "In neuro-ophthalmology, drooping of the palpebra superioris due to third cranial nerve palsy, Horner syndrome (sympathetic denervation), or myasthenia gravis.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Bilateral fluctuating **ptosis** that worsens toward evening is an early and characteristic sign of myasthenia gravis." },
      { "author": "W. Russell Brain", "work": "Diseases of the Nervous System", "quote": "In Horner's syndrome, sympathetic paralysis produces partial **ptosis** accompanied by pupillary miosis and facial anhidrosis." },
      { "author": "Jonathan Hutchinson", "work": "Clinical Lectures on Rare Diseases of the Skin and Eye", "quote": "Complete unilateral **ptosis** with pupil dilation strongly points to compression of the third nerve by an intracranial aneurysm." }
    ]
  },
  "Dashboard — pto\\ptotic.md": {
    "primary": "Affected by or exhibiting ptosis; drooping or prolapsed.",
    "secondary": "In clinical neurology and ophthalmology, designating a drooping eyelid or downwardly displaced anatomic structure (such as a ptotic kidney / nephroptosis).",
    "quotes": [
      { "author": "W. Russell Brain", "work": "Diseases of the Nervous System", "quote": "The patient attempted to compensate for the **ptotic** eyelid by wrinkling the frontalis muscle and tilting the chin upward." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Palpation in the right flank easily demonstrated a mobile, **ptotic** kidney in the thin young woman." },
      { "author": "Harvey Cushing", "work": "The Pituitary Body and Its Disorders", "quote": "Improvement in the **ptotic** eye followed immediately upon surgical decompression of the superior orbital fissure." }
    ]
  },
  "Dashboard — pto\\symptom.md": {
    "primary": "A physical or mental feature indicating a condition of disease, perceived and reported by the patient; an indicator of something.",
    "secondary": "In diagnostic semiotics and medical philosophy, subjective evidence of illness experienced by the patient, contrasted with objective clinical signs discovered by physical examination.",
    "quotes": [
      { "author": "William Osler", "work": "Aequanimitas", "quote": "Listen to the patient; he is telling you the diagnosis, for every **symptom** has its anatomical or physiological meaning." },
      { "author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "A single isolated **symptom** may mislead, but a coherent constellation of facts points unfailingly to the truth." },
      { "author": "Thomas Sydenham", "work": "The Works of Thomas Sydenham", "quote": "Nature in the production of disease is uniform and consistent, so that each specific **symptom** recurs with admirable regularity." }
    ]
  },
  "Dashboard — pto\\symptosis.md": {
    "primary": "A gradual wasting, emaciation, or atrophy of the entire body or a part; or the recession of a symptom.",
    "secondary": "In classical medical pathology and Galenic nosology, generalized systemic wasting (tabes or cachexia) resulting from chronic consumptive illness.",
    "quotes": [
      { "author": "Thomas Browne", "work": "Pseudodoxia Epidemica", "quote": "In chronic hectic fevers, there succeeds a gradual **symptosis** or collapse of the fleshy substance of the limbs." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The progressive **symptosis** and loss of subcutaneous fat in malignant cachexia reflects profound metabolic reprogramming." },
      { "author": "Galen", "work": "On the Natural Faculties", "quote": "When the innate heat fails to assimilate nourishment, the bodily tissues fall into cold **symptosis** and decay." }
    ]
  },
  "Dashboard — sapr\\sapraemia.md": {
    "primary": "A condition in which the toxic products of putrefactive bacteria enter the bloodstream without the bacteria themselves multiplying in the blood; British spelling of sapremia.",
    "secondary": "In 19th-century surgical pathology, systemic toxic fever resulting from the absorption of decomposition products from necrotic tissues, retained placental fragments, or gangrenous wounds.",
    "quotes": [
      { "author": "Joseph Lister", "work": "The Collected Papers of Joseph Lister", "quote": "Antiseptic cleansing of the putrid cavity arrested the absorption of toxins, quickly subduing the dangerous **sapraemia**." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Puerperal **sapraemia** subsides rapidly once retained necrotic lochia are thoroughly evacuated from the uterus." },
      { "author": "Robert Koch", "work": "Investigations into the Etiology of Traumatic Infective Diseases", "quote": "We must differentiate true progressive septicemia from simple **sapraemia** caused by absorption of dead putrefactive chemicals." }
    ]
  },
  "Dashboard — sapr\\sapremia.md": {
    "primary": "Blood poisoning caused by the absorption of toxins produced by saprophytic or putrefactive bacteria in necrotic tissue.",
    "secondary": "In obstetrical and surgical medicine, systemic toxicosis arising from decomposition of retained placental tissue or devitalized surgical debris, resolving once the septic nidus is removed.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The high fever and bounding pulse of surgical **sapremia** promptly subside when necrotic tissue is debrided." },
      { "author": "Joseph Lister", "work": "On the Antiseptic Principle in the Practice of Surgery", "quote": "By preventing the putrefaction of wound fluids, the carbolic dressing protects the patient from debilitating **sapremia**." },
      { "author": "Alexander Fleming", "work": "Historical Perspectives on Wound Sepsis", "quote": "Before the bacteriological era, clinicians struggled to distinguish transient **sapremia** from fatal bloodstream invasion." }
    ]
  },
  "Dashboard — sapr\\saprobe.md": {
    "primary": "An organism, especially a fungus or bacterium, that derives its nourishment from decaying organic matter.",
    "secondary": "In microbial ecology and environmental mycology, decomposer organisms essential for recycling carbon and nitrogen in forest soils, compost, and freshwater ecosystems.",
    "quotes": [
      { "author": "Eugene Odum", "work": "Fundamentals of Ecology", "quote": "The microbial **saprobe** plays an indispensable role in closing the ecosystem loop by mineralizing dead leaf litter." },
      { "author": "Selman Waksman", "work": "Principles of Soil Microbiology", "quote": "Every soil fungus acting as a **saprobe** produces extracellular cellulases to break down plant cell wall residues." },
      { "author": "Rachel Carson", "work": "The Edge of the Sea", "quote": "In the murky sediment floor, myriads of **saprobe** bacteria break down the organic drift of dying surface plankton." }
    ]
  },
  "Dashboard — sapr\\saprobic.md": {
    "primary": "Living on or obtaining nourishment from decaying organic matter; relating to a saprobe.",
    "secondary": "In limnology, water quality assessment, and saprobic zonation, designating aquatic ecological zones (polysaprobic to oligosaprobic) based on organic pollution levels and indicator microorganisms.",
    "quotes": [
      { "author": "Robert Kolkwitz", "work": "Oekologie der pflanzlichen Saprobien", "quote": "The **saprobic** system classifies river waters into distinct zones based upon the presence of specific decomposing microflora." },
      { "author": "Eugene Odum", "work": "Fundamentals of Ecology", "quote": "Discharge of raw sewage creates a polysaprobic river reach where obligate **saprobic** bacteria dominate the biota." },
      { "author": "Selman Waksman", "work": "The Soil and the Microbe", "quote": "Fungi of the **saprobic** guild are the primary agents responsible for degrading complex lignified plant matter." }
    ]
  },
  "Dashboard — sapr\\saprogenic.md": {
    "primary": "Producing, causing, or arising from decay, putrefaction, or decomposition.",
    "secondary": "In bacteriology and sanitation science, micro-organisms (such as Clostridium and Proteus species) that enzymatically break down complex animal and plant proteins into putrid amines, indoles, and hydrogen sulfide.",
    "quotes": [
      { "author": "Louis Pasteur", "work": "Studies on Fermentation", "quote": "Anaerobic organisms possessing **saprogenic** power ferment nitrogenous matters into foul gases in the absence of air." },
      { "author": "Robert Koch", "work": "The Etiology of Tuberculosis", "quote": "The culture became contaminated with aggressive **saprogenic** bacilli that rapidly liquefied the gelatin substrate." },
      { "author": "Justus von Liebig", "work": "Familiar Letters on Chemistry", "quote": "Putrefaction is maintained by **saprogenic** ferments that transfer their molecular instability to surrounding proteins." }
    ]
  },
  "Dashboard — sapr\\saprolegnia.md": {
    "primary": "A genus of freshwater water molds in the family Saprolegniaceae, commonly growing as white cottony tufts on decaying matter and living fish.",
    "secondary": "In aquaculture, fish pathology, and oomycete biology, an aquatic oomycete causing saprolegniasis in salmonids and fish eggs, reproducing via biflagellate heterokont zoospores and thick-walled sexual oospores.",
    "quotes": [
      { "author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Invertebrated Animals", "quote": "The salmon disease is caused by the parasitic growth of **Saprolegnia**, which covers the skin with a white cottony mycelium." },
      { "author": "Anton de Bary", "work": "Comparative Morphology and Biology of the Fungi, Mycetozoa and Bacteria", "quote": "In **Saprolegnia**, sexual reproduction occurs inside oogonia where multiple spherical oospheres are fertilized by antheridial tubes." },
      { "author": "Francis Day", "work": "British and Irish Salmonidae", "quote": "The fungal mycelium of **Saprolegnia** suffocates developing trout roe in the hatchery troughs unless water is actively treated." }
    ]
  },
  "Dashboard — sapr\\saprolegniales.md": {
    "primary": "An order of aquatic eukaryotic microorganisms in the phylum Oomycota, commonly known as water molds.",
    "secondary": "In mycology and protistology, diploid filamentous heterokonts with cellulosic cell walls and coenocytic hyphae, containing both saprotrophs of submerged organic matter and destructive pathogens of aquatic animals and amphibians.",
    "quotes": [
      { "author": "Anton de Bary", "work": "Morphology of the Fungi and Allied Groups", "quote": "Members of **Saprolegniales** are distinguished by their biflagellate zoospores that undergo a remarkable dimorphic encystment." },
      { "author": "F. E. Fritsch", "work": "The Structure and Reproduction of the Algae", "quote": "Though traditionally studied by mycologists, **Saprolegniales** belong to the stramenopiles, sharing evolutionary affinities with brown algae." },
      { "author": "David Starr Jordan", "work": "A Guide to the Study of Fishes", "quote": "Fungal epizootics among pond fish are predominantly initiated by water molds of the order **Saprolegniales**." }
    ]
  },
  "Dashboard — sapr\\saprolite.md": {
    "primary": "Chemically weathered rock that remains in its original place, retaining the original fabric and structure of the parent rock but softened and clay-rich.",
    "secondary": "In geomorphology, pedology, and regolith geology, deep weathering profiles (often dozens of meters thick in humid tropical and subtropical terrains) where silicate minerals have hydrolyzed into kaolinite and iron oxides.",
    "quotes": [
      { "author": "George Perkins Merrill", "work": "Rocks, Rock-Weathering and Soils", "quote": "Becker introduced the term **saprolite** for thoroughly decomposed crystalline rock which still preserves its original granitic texture." },
      { "author": "Archibald Geikie", "work": "Text-Book of Geology", "quote": "In the southern Piedmont, deep excavation reveals thick beds of soft **saprolite** that can be cut with a common spade." },
      { "author": "Charles Lyell", "work": "Principles of Geology", "quote": "Subaerial chemical weathering in tropical latitudes reduces solid basalt to a porous crumbly **saprolite** without disturbing the bedding planes." }
    ]
  },
  "Dashboard — sapr\\sapropel.md": {
    "primary": "A dark-colored, organic-rich sediment or slime formed on the bottoms of quiet bodies of water under oxygen-depleted (anoxic) conditions.",
    "secondary": "In paleoceanography and petroleum geology, discrete organic-rich marine sedimentary layers (such as Mediterranean sapropel beds) formed during episodes of water column stratification and stagnation, serving as prime petroleum source rocks.",
    "quotes": [
      { "author": "Archibald Geikie", "work": "Text-Book of Geology", "quote": "Under the stagnant waters of stagnant fjords, decaying planktonic ooze consolidates into a black, sulfurous **sapropel**." },
      { "author": "Rachel Carson", "work": "The Sea Around Us", "quote": "In the deep anoxic basins of the Black Sea, organic remains settle into thick beds of bituminous **sapropel** untouched by scavengers." },
      { "author": "Frank Wigglesworth Clarke", "work": "The Data of Geochemistry", "quote": "The anaerobic decomposition of lacustrine algae yields that peculiar fatty mud which limnologists designate as **sapropel**." }
    ]
  },
  "Dashboard — sapr\\saprophagous.md": {
    "primary": "Feeding or subsisting on dead, decaying, or putrefying organic matter.",
    "secondary": "In entomology and vertebrate ecology, scavenger animals (such as carrion beetles, blowfly larvae, and vultures) that consume decomposing animal carcasses and plant residues, accelerating nutrient turnover.",
    "quotes": [
      { "author": "Jean-Henri Fabre", "work": "The Life of the Fly", "quote": "The **saprophagous** larvae of the blowfly descend upon the carcass with unbelievable haste, clearing away putrid flesh." },
      { "author": "Charles Darwin", "work": "On the Origin of Species", "quote": "The keen olfactory senses of **saprophagous** beetles enable them to locate a dead animal from miles across the forest." },
      { "author": "William Morton Wheeler", "work": "Ants: Their Structure, Development and Behavior", "quote": "Many primitive ponerine ants lead a **saprophagous** life, scavenging dead arthropods and decaying organic crumbs from the forest litter." }
    ]
  },
  "Dashboard — sapr\\saprophyte.md": {
    "primary": "A plant, fungus, or microorganism that lives on dead or decaying organic matter.",
    "secondary": "In classical botany and mycology, organisms lacking photosynthetic chlorophyll (historically including non-green plants like Monotropa and Indian pipe, now known to be mycoheterotrophs, as well as wood-decay fungi) that absorb dissolved nutrients from organic substrates.",
    "quotes": [
      { "author": "Asa Gray", "work": "Elements of Botany", "quote": "The ghost-like Indian pipe is a **saprophyte**, absorbing its nourishment from the leaf mould of dark woods without green leaves." },
      { "author": "Charles Darwin", "work": "The Various Contrivances by Which Orchids Are Fertilised by Insects", "quote": "Certain leafless orchids function as a **saprophyte**, their root systems intimately intertwined with decomposing fungal humus." },
      { "author": "Anton de Bary", "work": "Comparative Morphology and Biology of the Fungi", "quote": "The bracket fungus living upon a fallen birch trunk is a typical lignicolous **saprophyte**, breaking down the heartwood." }
    ]
  },
  "Dashboard — sapr\\saprophytic.md": {
    "primary": "Obtaining nourishment from dead or decaying organic matter; relating to a saprophyte.",
    "secondary": "In medical microbiology and environmental biology, non-pathogenic environmental organisms that live in soil and water on rotting material, occasionally causing opportunistic infections in immunocompromised hosts.",
    "quotes": [
      { "author": "Louis Pasteur", "work": "Studies on Fermentation", "quote": "The atmosphere is loaded with spores of **saprophytic** yeasts and molds ready to settle upon any unprotected nutrient broth." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Harmless **saprophytic** organisms inhabiting the mucous membranes may become invasive when systemic immunity collapses." },
      { "author": "Selman Waksman", "work": "Mycology and Soil Microbiology", "quote": "The breakdown of forest foliage is carried out by a succession of **saprophytic** fungi possessing distinct enzymatic specializations." }
    ]
  },
  "Dashboard — sapr\\saprotrophic.md": {
    "primary": "Feeding on decaying organic matter; obtaining nutrients by extracellular digestion of dead organic material.",
    "secondary": "In modern ecological terminology (the preferred scientific term replacing 'saprophytic' for fungi and bacteria), describing heterotrophic nutrition involving the secretion of hydrolytic enzymes and subsequent absorption of soluble products.",
    "quotes": [
      { "author": "Eugene Odum", "work": "Fundamentals of Ecology", "quote": "The **saprotrophic** decomposers of the forest floor mineralize organic compounds and restore vital nutrients to living tree roots." },
      { "author": "Selman Waksman", "work": "The Actinomycetes", "quote": "A robust **saprotrophic** microflora suppresses fungal plant pathogens by aggressively competing for free nutrients in the soil." },
      { "author": "Arthur Tansley", "work": "The British Islands and Their Vegetation", "quote": "The **saprotrophic** fungal guild in pine litter rapidly colonizes dead needle fall, releasing stored phosphate and potash." }
    ]
  },
  "Dashboard — sapr\\saprozoic.md": {
    "primary": "Feeding on dead or decaying animal matter; or obtaining nutrition by the direct absorption of dissolved organic compounds (in protozoa or invertebrates).",
    "secondary": "In protozoology and invertebrate physiology, animals or protozoans that absorb nutrients through the body surface from surrounding nutrient-rich fluid environments, contrasted with holozoic phagotrophy.",
    "quotes": [
      { "author": "Ray Lankester", "work": "A Treatise on Zoology", "quote": "Certain parasitic flagellates have lost the cytostome entirely, subsisting by purely **saprozoic** absorption of host serum." },
      { "author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Invertebrated Animals", "quote": "The tapeworm exemplifies a strictly **saprozoic** nutrition, bathing in the predigested intestinal fluids of its vertebrate host." },
      { "author": "Libbie Hyman", "work": "The Invertebrates", "quote": "In sewage-polluted streams, free-living ciliates may switch to a **saprozoic** habit when dissolved amino acids are abundant." }
    ]
  },
  "Dashboard — scen\\ascension.md": {
    "primary": "The act of rising, climbing, or ascending; specifically, the bodily ascent of Jesus Christ into heaven.",
    "secondary": "In observational astronomy, right ascension (RA), the celestial coordinate angularly measured eastward along the celestial equator from the vernal equinox to the object's hour circle.",
    "quotes": [
      { "author": "John Milton", "work": "Paradise Lost", "quote": "So he told them, and then his **ascension** followed, received into a cloud that carried him up from their sight." },
      { "author": "Simon Newcomb", "work": "Popular Astronomy", "quote": "The position of a star on the celestial sphere is determined by its right **ascension** and declination." },
      { "author": "Percy Bysshe Shelley", "work": "Prometheus Unbound", "quote": "The slow **ascension** of the morning sun dispelled the sullen vapors that veiled the precipitous mountain gorge." }
    ]
  },
  "Dashboard — scen\\ascensional.md": {
    "primary": "Of, relating to, or causing ascension or rising.",
    "secondary": "In meteorology, aeronautics, and physical geography, relating to the vertical upward movement of heated air masses (ascensional thermal currents) or lifting over mountain barriers.",
    "quotes": [
      { "author": "Alexander von Humboldt", "work": "Personal Narrative of Travels to the Equinoctial Regions", "quote": "The intense solar heating of the llanos produces powerful **ascensional** air currents that generate afternoon thunderstorms." },
      { "author": "Camille Flammarion", "work": "The Atmosphere", "quote": "The balloonist relied upon the **ascensional** force of heated gas to carry his basket above the storm clouds." },
      { "author": "John Tyndall", "work": "The Glaciers of the Alps", "quote": "Warm moist air driven up the alpine slopes undergoes adiabatic cooling, its **ascensional** movement resulting in dense clouds." }
    ]
  },
  "Dashboard — scen\\ascensive.md": {
    "primary": "Rising or tending to rise; progressive, uplifting, or characterized by upward movement.",
    "secondary": "In grammar, rhetoric, and theology, expressing an intensification or advance in degree (an ascensive conjunction or ascensive clause), leading to a higher climax of thought.",
    "quotes": [
      { "author": "Samuel Taylor Coleridge", "work": "Aids to Reflection", "quote": "Human contemplation possesses an **ascensive** power that lifts the soul from sensible creatures to the eternal Creator." },
      { "author": "Max Müller", "work": "Lectures on the Science of Language", "quote": "The Hebrew conjunction 'af' is used with an **ascensive** force, intensifying the statement into an emphatic climax." },
      { "author": "Thomas Carlyle", "work": "Heroes and Hero-Worship", "quote": "The life of mankind is an **ascensive** march through centuries of trial, climbing slowly toward spiritual freedom." }
    ]
  },
  "Dashboard — scen\\ascent.md": {
    "primary": "The act of rising, climbing, or mounting upward; an upward slope or climb.",
    "secondary": "In mountaineering, aviation, and evolutionary history, the physical climb up a mountain face, the climb of an aircraft to cruising altitude, or the genealogical rise of an organism or humanity.",
    "quotes": [
      { "author": "William Wordsworth", "work": "The Prelude", "quote": "In the dark night we climbed, and on our arduous **ascent** the moon suddenly broke forth over Snowdon's head." },
      { "author": "Charles Darwin", "work": "The Descent of Man", "quote": "Man with all his noble qualities still bears in his bodily frame the indelible stamp of his lowly **ascent**." },
      { "author": "John Ruskin", "work": "Modern Painters", "quote": "The steep **ascent** to the alpine ridge led us through groves of larch and pine up into the desolate realm of ice." }
    ]
  },
  "Dashboard — scen\\descensus.md": {
    "primary": "A descent, downward movement, or falling; specifically, the descent of Christ into Limbo/Hell (Descensus Christi ad Inferos).",
    "secondary": "In anatomical pathology, gynecology, and surgical nosology, the downward displacement or prolapse of an internal organ (such as descensus uteri / uterine prolapse).",
    "quotes": [
      { "author": "Virgil", "work": "Aeneid", "quote": "Facilis **descensus** Averno: smooth is the descent to the underworld, but to recall one's step to the sweet air of heaven is the arduous task." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Pelvic relaxation in multiparous women frequently results in **descensus** of the bladder and anterior vaginal wall." },
      { "author": "Thomas Aquinas", "work": "Summa Theologiae", "quote": "The holy fathers teach that the **descensus** of Christ delivered the souls of the just who waited in the bosom of Abraham." }
    ]
  },
  "Dashboard — scen\\descent.md": {
    "primary": "The action of moving downward, falling, or dropping; a downward slope; or a person's lineage or ancestry.",
    "secondary": "In evolutionary biology, descent with modification, Charles Darwin's foundational principle explaining biodiversity through common genealogical ancestry and natural selection.",
    "quotes": [
      { "author": "Charles Darwin", "work": "On the Origin of Species", "quote": "All the organic beings which have ever lived on this earth have descended from some one primordial form: this is **descent** with modification." },
      { "author": "John Milton", "work": "Paradise Lost", "quote": "From morn to noon he fell, from noon to dewy eve, a summer's day; and with the setting sun dropped from the zenith, in headlong **descent**." },
      { "author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The rapid **descent** of the Roman empire from Marcus Aurelius to Commodus illustrates the fragility of hereditary virtue." }
    ]
  },
  "Dashboard — scen\\parascenium.md": {
    "primary": "Either of two flanking wings or projecting side structures adjacent to the stage in an ancient Greek or Roman theatre.",
    "secondary": "In classical architectural history and theater archaeology, the lateral projecting wings that bounded the proscenium (skene), providing storage for theatrical machinery, entrances for actors, and acoustic amplification.",
    "quotes": [
      { "author": "Vitruvius", "work": "De Architectura", "quote": "On either side of the stage the **parascenium** projects outward, providing entrance doors for actors representing foreign travelers." },
      { "author": "Margarete Bieber", "work": "The History of the Greek and Roman Theater", "quote": "In Hellenistic playhouses, the colonnaded **parascenium** framed the acting space, creating an imposing architectural backdrop." },
      { "author": "Arthur Elam Haigh", "work": "The Attic Theatre", "quote": "Remains of the Dionysus theatre at Athens clearly show where the stone **parascenium** was added during the Lycurgan rebuilding." }
    ]
  },
  "Dashboard — scen\\proscenium.md": {
    "primary": "The part of a theater stage in front of the curtain; or the proscenium arch that frames the stage opening.",
    "secondary": "In theatrical architecture and stagecraft, the structural arch or decorative border that frames the performance area and separates the stage illusion from the auditorium seating.",
    "quotes": [
      { "author": "Charles Dickens", "work": "Nicholas Nickleby", "quote": "The footlights flickered upon the gilded mouldings of the **proscenium**, across which Mr. Crummles looked with managerial pride." },
      { "author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "The tiny playhouse was dingy, with a tarnished **proscenium** and painted drop-curtains depicting a Venetian canal." },
      { "author": "George Bernard Shaw", "work": "Dramatic Opinions and Essays", "quote": "Modern realistic drama demands that the actor step behind the **proscenium** arch and maintain the illusion of a fourth wall." }
    ]
  },
  "Dashboard — scen\\scenario.md": {
    "primary": "A written outline of the plot, characters, and scenes of a play, film, or opera; a postulated sequence or development of events.",
    "secondary": "In military strategy, futurology, and decision science (developed notably by Herman Kahn at the RAND Corporation), systematic narrative forecasts exploring alternative geopolitical, economic, or environmental futures.",
    "quotes": [
      { "author": "Herman Kahn", "work": "Thinking about the Unthinkable", "quote": "Policy planners construct an artificial **scenario** of escalating crisis in order to test military and diplomatic options." },
      { "author": "Virginia Woolf", "work": "Between the Acts", "quote": "Miss La Trobe paced behind the barn, consulting the handwritten **scenario** for her village pageant." },
      { "author": "Igor Stravinsky", "work": "Chronicles of My Life", "quote": "Diaghilev accepted my **scenario** for Petrushka the moment he heard the rhythmic opening chord on the piano." }
    ]
  },
  "Dashboard — scen\\scenarist.md": {
    "primary": "A writer who prepares or develops scenarios, especially for theatrical productions or motion picture films; a screenwriter.",
    "secondary": "In film history and dramaturgy, the specialized craft professional in early cinema who translated literary plots or original concepts into scene-by-scene shooting scripts.",
    "quotes": [
      { "author": "F. Scott Fitzgerald", "work": "The Last Tycoon", "quote": "In the studio conference room, the veteran **scenarist** pitched a fresh angle on the second-act romantic crisis." },
      { "author": "Virginia Woolf", "work": "The Captain's Death Bed and Other Essays", "quote": "The modern **scenarist** must think in swift visual images rather than literary sentences to capture the camera's eye." },
      { "author": "George Bernard Shaw", "work": "Shaw on Cinema", "quote": "No mechanical **scenarist** can improve upon Shakespeare by chopping his five-act tragedies into disconnected film scenes." }
    ]
  },
  "Dashboard — scen\\scene-stealer.md": {
    "primary": "An actor or performer who dominates a performance or scene, drawing audience attention away from the primary leads; or something strikingly captivating.",
    "secondary": "In dramatic criticism and performance arts, a secondary or character actor whose charisma, physical humor, or emotional intensity effortlessly commands the spectator's gaze.",
    "quotes": [
      { "author": "H. L. Mencken", "work": "Prejudices: Fourth Series", "quote": "The veteran character comic proved an irrepressible **scene-stealer**, pulling the entire audience's gaze with a single twitch of his brow." },
      { "author": "George Bernard Shaw", "work": "Our Theatres in the Nineties", "quote": "The gravedigger was a notorious **scene-stealer**, delaying Hamlet's soliloquy with outrageous comic business." },
      { "author": "Max Beerbohm", "work": "Around Theatres", "quote": "Every leading lady dreads playing opposite a natural **scene-stealer** whose quietest whisper eclipses her grandest speech." }
    ]
  },
  "Dashboard — scen\\scene.md": {
    "primary": "The place where an action, event, or incident occurs; a division of an act in a play; or a display of emotion or anger in public.",
    "secondary": "In theatrical staging, literary narration, and cinematography, a continuous unit of dramatic action defined by unity of time, place, and characters.",
    "quotes": [
      { "author": "William Shakespeare", "work": "As You Like It", "quote": "All the world's a stage, and all the men and women merely players; they have their exits and their entrances, and one man in his time plays many parts, his acts being seven ages... a strange eventful **scene**." },
      { "author": "Edgar Allan Poe", "work": "The Fall of the House of Usher", "quote": "I looked upon the **scene** before me—with an utter depression of soul which I can compare to no earthly sensation." },
      { "author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth was resolved to prevent any painful **scene** between her mother and Mr. Darcy at the dinner table." }
    ]
  },
  "Dashboard — scen\\scenery.md": {
    "primary": "The natural features of a landscape considered in terms of their appearance; or the painted backdrops and hangings of a stage.",
    "secondary": "In theatrical stagecraft and aesthetic landscape philosophy, the constructed backdrops, flats, and mechanical sets that represent the physical setting of a drama.",
    "quotes": [
      { "author": "William Wordsworth", "work": "Lines Composed a Few Miles above Tintern Abbey", "quote": "These plots of cottage-ground, these orchard-tufts, which at this season with their unripe fruits are clad in one green hue, and lose themselves mid groves and copses... sublime wild **scenery** of the mind." },
      { "author": "Charles Dickens", "work": "Nicholas Nickleby", "quote": "The canvas **scenery** smelled powerfully of size and turpentine, shivering whenever a door was slammed in the wings." },
      { "author": "John Ruskin", "work": "Modern Painters", "quote": "Mountain **scenery** produces a solemn impression of eternal power upon the human heart that no flat plain can awaken." }
    ]
  },
  "Dashboard — scen\\sceneshifter.md": {
    "primary": "A stagehand who moves and changes the scenery, sets, and props between acts or scenes in a theater.",
    "secondary": "In theater history and backstage labor, members of the technical crew whose coordinated mechanical operations operated pulleys, fly lines, and groove flats to transform scenic illusions rapidly.",
    "quotes": [
      { "author": "Charles Dickens", "work": "The Old Curiosity Shop", "quote": "Behind the curtain, the bustling **sceneshifter** trundled painted groves of trees and pasteboard castles into place." },
      { "author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "When the play is done, the **sceneshifter** rolls up the painted canvas and puts out the guttering tallow candles." },
      { "author": "George Bernard Shaw", "work": "Our Theatres in the Nineties", "quote": "The heavy set took so long to change that the audience grew weary listening to the clatter of the **sceneshifter** behind the drop." }
    ]
  },
  "Dashboard — scen\\scenic.md": {
    "primary": "Providing or relating to views of natural landscapes; or of or relating to stage scenery or dramatic representation.",
    "secondary": "In aesthetic theory and tourism history, natural vistas (the 'picturesque') characterized by visual variety, elevation, and pleasing compositional balance.",
    "quotes": [
      { "author": "Henry James", "work": "The Scenic Art: Notes on Acting and the Drama", "quote": "The actor must master the **scenic** art of making artificial dialogue appear as natural as breathing." },
      { "author": "John Muir", "work": "My First Summer in the Sierra", "quote": "The **scenic** splendor of the Yosemite valley surpasses all human imagination with its soaring granite walls." },
      { "author": "William Wordsworth", "work": "A Guide through the District of the Lakes", "quote": "Travelers seeking the finest **scenic** effects will find them where mountain crags meet the peaceful waters of the lake." }
    ]
  },
  "Dashboard — scen\\scenically.md": {
    "primary": "In a scenic manner; with regard to natural scenery or dramatic stage presentation.",
    "secondary": "In visual criticism and topography, evaluated according to picturesque qualities, landscape aesthetics, or stage design excellence.",
    "quotes": [
      { "author": "Henry James", "work": "Transatlantic Sketches", "quote": "The city of Florence is **scenically** situated in a fertile basin surrounded by olive-mantled Apennine foothills." },
      { "author": "George Bernard Shaw", "work": "Dramatic Opinions", "quote": "The opera was mounted **scenically** with lavish splendour, though the singing left much to be desired." },
      { "author": "Archibald Geikie", "work": "The Scenery of Scotland", "quote": "The western fjords are **scenically** the most magnificent feature of the coast, gouged out by ancient glacial streams." }
    ]
  },
  "Dashboard — scen\\scenography.md": {
    "primary": "The design and painting of theatrical scenery; the comprehensive visual, spatial, and material design of a stage production.",
    "secondary": "In classical architecture (Vitruvian *scaenographia*) and modern performance theory, perspective architectural drawing and the integrated holistic design of stage space, costume, lighting, and sound.",
    "quotes": [
      { "author": "Vitruvius", "work": "De Architectura", "quote": "The third branch of architectural drawing is **scenography**, which presents the facade and sides receding into proper perspective." },
      { "author": "Inigo Jones", "work": "Designs for Masques and Plays at Court", "quote": "By coordinating perspective shutters with hidden footlights, our **scenography** transformed the royal banquet hall into an enchanted palace." },
      { "author": "Edward Gordon Craig", "work": "On the Art of the Theatre", "quote": "True modern **scenography** is not mere backdrop painting, but the dynamic mastery of light, space, and movement." }
    ]
  },
  "Dashboard — scen\\scent.md": {
    "primary": "A distinctive odor, smell, or fragrance; or an odor trail left by an animal by which it can be tracked.",
    "secondary": "In canine hunting, animal ecology, and sensory biology, chemical olfactory cues (volatile organic compounds) emitted by an organism, allowing tracking dogs and predators to follow trails.",
    "quotes": [
      { "author": "William Shakespeare", "work": "Hamlet", "quote": "I find thee apt; and duller shouldst thou be than the fat weed that roots itself in ease on Lethe wharf, wouldst thou not stir in this... Methinks I **scent** the morning air; brief let me be." },
      { "author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "The hound follows the faint **scent** of the hare across damp turf with unerring olfactory sensitivity." },
      { "author": "Henry David Thoreau", "work": "Walden", "quote": "The warm spring rain brought forth the pungent **scent** of wet pine needles and thawing pitch." }
    ]
  },
  "Dashboard — scen\\scentless.md": {
    "primary": "Having no smell, odor, or fragrance; odorless.",
    "secondary": "In botanical pollination ecology, plant species with flowers lacking aromatic volatile emissions, commonly adapted for pollination by birds or wind rather than nocturnal scent-seeking moths or bees.",
    "quotes": [
      { "author": "Charles Darwin", "work": "The Various Contrivances by Which Orchids Are Fertilised by Insects", "quote": "Brightly colored scarlet flowers are frequently **scentless**, being pollinated by hummingbirds that possess keen vision but little sense of smell." },
      { "author": "Percy Bysshe Shelley", "work": "The Sensitive Plant", "quote": "Broad water lilies lay upon the stream, their blossoms **scentless** beneath the midday glare." },
      { "author": "John Tyndall", "work": "Essays on the Floating-Matter of the Air", "quote": "Pure distilled water and filtered air are completely **scentless** to the most delicate human nostrils." }
    ]
  },
  "Dashboard — steat\\stearic acid.md": {
    "primary": "A saturated 18-carbon fatty acid, CH3(CH2)16COOH, found in animal fats and plant oils, used in soaps, cosmetics, and candles.",
    "secondary": "In lipid biochemistry and chemical manufacturing, an essential long-chain saturated fatty acid synthesized from tallow or palm oil, whose sodium salt acts as a primary surfactant in traditional soap-making.",
    "quotes": [
      { "author": "Michel Eugène Chevreul", "work": "Recherches chimiques sur les corps gras", "quote": "By saponification of mutton tallow followed by acidulation, I succeeded in isolating pure crystalline **stearic acid**." },
      { "author": "Justus von Liebig", "work": "Familiar Letters on Chemistry", "quote": "The manufacture of composite candles from purified **stearic acid** replaced smoking tallow dips with bright, smokeless light." },
      { "author": "Linus Pauling", "work": "General Chemistry", "quote": "In the crystal lattice of **stearic acid**, nonpolar hydrocarbon tails pack together closely in parallel layers." }
    ]
  },
  "Dashboard — steat\\steatite.md": {
    "primary": "A soft, talc-rich metamorphic rock commonly known as soapstone, having a soapy or greasy feel and easily carved.",
    "secondary": "In petrology, archaeology, and ceramic engineering, an impure massive talcose rock historically carved into cooking pots, amulets, and hearth linings because of its high heat capacity and chemical resistance.",
    "quotes": [
      { "author": "James Dwight Dana", "work": "A System of Mineralogy", "quote": "The massive variety of talc known as **steatite** or soapstone is easily cut with a knife and greasy to the touch." },
      { "author": "Charles Lyell", "work": "Principles of Geology", "quote": "Ancient Native American tribes carved heavy cooking pots and pipes from quarries of soft metamorphic **steatite**." },
      { "author": "Archibald Geikie", "work": "Text-Book of Geology", "quote": "Hydrothermal alteration of ultramafic serpentine bodies commonly results in dense formations of gray **steatite**." }
    ]
  },
  "Dashboard — steat\\steatocystoma.md": {
    "primary": "A benign skin condition characterized by multiple sebum-containing cysts formed within sebaceous duct junctions; steatocystoma multiplex.",
    "secondary": "In clinical dermatology and dermatopathology, an autosomal dominant disorder (frequently associated with keratin 17 gene mutations) characterized by yellowish subcutaneous cystic nodules lined by an undulating, sebaceous-gland-bearing epithelial wall.",
    "quotes": [
      { "author": "Jonathan Hutchinson", "work": "Clinical Lectures on Rare Diseases of the Skin", "quote": "The patient presented multiple yellowish cutaneous nodules over the chest, typical of that condition known as **steatocystoma**." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Histological section of a **steatocystoma** demonstrates a true sebaceous cyst containing oily fluid and hair fragments." },
      { "author": "Thomas Addison", "work": "Observations on Cutaneous Diseases", "quote": "The soft consistency and clear sebaceous contents distinguish the lesions of **steatocystoma** from fibromata." }
    ]
  },
  "Dashboard — steat\\steatolysis.md": {
    "primary": "The chemical breakdown, digestion, or emulsification of fats into glycerol and fatty acids; lipolysis.",
    "secondary": "In physiological chemistry and gastroenterology, the enzymatic hydrolysis of dietary triglycerides by pancreatic and gastric lipases in the small intestine.",
    "quotes": [
      { "author": "Claude Bernard", "work": "Memoir on the Pancreas", "quote": "The clear pancreatic juice possesses an extraordinary power of **steatolysis**, rapidly splitting neutral fats into free fatty acids." },
      { "author": "Russell Henry Chittenden", "work": "Studies in Physiological Chemistry", "quote": "Bile salts accelerate the process of intestinal **steatolysis** by emulsifying insoluble lipid globules into micro-droplets." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Deficiency in pancreatic secretions leads to impaired **steatolysis**, resulting in the excretion of unhydrolyzed fat in the stool." }
    ]
  },
  "Dashboard — steat\\steatolytic.md": {
    "primary": "Capable of breaking down, digesting, or hydrolyzing fats; lipolytic.",
    "secondary": "In gastrointestinal enzymology and pharmacology, enzymes or digestive agents (especially pancreatic lipase) that catalyze the hydrolytic cleavage of ester bonds in triglycerides.",
    "quotes": [
      { "author": "Claude Bernard", "work": "Lectures on Experimental Physiology", "quote": "We demonstrated the **steatolytic** action of the pancreatic fluid by observing the rapid acidification of olive oil mixtures." },
      { "author": "William Beaumont", "work": "Experiments and Observations on the Gastric Juice", "quote": "Gastric secretion displays slight **steatolytic** activity, which is enormously augmented once chyme enters the duodenum." },
      { "author": "Justus von Liebig", "work": "Animal Chemistry", "quote": "The digestive juices exert a specific **steatolytic** power that prepares insoluble dietary lipids for lymphatic absorption." }
    ]
  },
  "Dashboard — steat\\steatopygia.md": {
    "primary": "An excessive, localized accumulation of subcutaneous fat in the buttocks, producing marked prominence.",
    "secondary": "In physical anthropology and human physiology, a genetic trait historically prominent among the Khoisan peoples of southern Africa, functioning as an adaptive metabolic energy and water reserve in arid climates without insulating the rest of the body.",
    "quotes": [
      { "author": "Charles Darwin", "work": "The Descent of Man", "quote": "The remarkable condition of **steatopygia** found among the women of the Bushmen is regarded by them as a great beauty." },
      { "author": "Thomas Henry Huxley", "work": "Man's Place in Nature", "quote": "Skeletal and fleshy traits like **steatopygia** evolved as localized fat deposits comparable to the camel's hump." },
      { "author": "James Cowles Prichard", "work": "Researches into the Physical History of Mankind", "quote": "Early travelers to the Cape described the extraordinary **steatopygia** of the Hottentot women with astonishment." }
    ]
  },
  "Dashboard — steat\\steatornis.md": {
    "primary": "A genus of nocturnal fruit-eating birds comprising the oilbird (*Steatornis caripensis*), native to northern South America.",
    "secondary": "In ornithology, the sole genus of the family Steatornithidae, inhabiting dark caves and navigating by echolocation, famously harvested by Indigenous peoples and early colonists for the copious fat rendered from nestling chicks.",
    "quotes": [
      { "author": "Alexander von Humboldt", "work": "Personal Narrative of Travels to the Equinoctial Regions of America", "quote": "The cavern of Caripe was inhabited by thousands of the nocturnal bird which I described under the name **Steatornis** caripensis." },
      { "author": "Alfred Russel Wallace", "work": "The Geographical Distribution of Animals", "quote": "The oilbird, **Steatornis**, represents a unique isolated family among birds, combining nightjar habits with a purely frugivorous diet." },
      { "author": "Richard Lydekker", "work": "The Royal Natural History", "quote": "The young of **Steatornis** are so enormously fat that the Indians boil them down into a pure, odorless cooking oil." }
    ]
  },
  "Dashboard — steat\\steatornithidae.md": {
    "primary": "A family of nocturnal birds in the order Caprimulgiformes, comprising the oilbird or guácharo.",
    "secondary": "In avian taxonomy, a monotypic Neotropical family (*Steatornis caripensis*) notable for its cave-nesting habits, vegetarian diet of palm and laurel fruits, and acoustic echolocation navigation.",
    "quotes": [
      { "author": "Alexander von Humboldt", "work": "Personal Narrative of Travels", "quote": "The singular anatomical characteristics of the guácharo place it in the distinct family **Steatornithidae**, allied to the nightjars." },
      { "author": "Arthur Thomson", "work": "Outlines of Zoology", "quote": "Within the order Caprimulgiformes, the family **Steatornithidae** is unique in feeding exclusively upon fatty oily fruits." },
      { "author": "Frank Chapman", "work": "Birds of Trinidad", "quote": "Caves in the Northern Range shelter colonies of **Steatornithidae**, filling the subterranean gloom with harsh guttural croaks." }
    ]
  },
  "Dashboard — steat\\steatorrhea.md": {
    "primary": "The presence of excess fat in the feces, resulting in pale, bulky, foul-smelling, and greasy stools that float.",
    "secondary": "In gastroenterology, an indicator of lipid malabsorption or maldigestion resulting from exocrine pancreatic insufficiency, celiac disease, bile acid deficiency, or cystic fibrosis.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Chronic diarrhea accompanied by pale, frothy, offensive stools containing undigested fat indicates marked **steatorrhea**." },
      { "author": "Thomas Addison", "work": "On the Symptoms and Treatment of Spondylitis", "quote": "Pancreatic obstruction manifests classically through progressive emaciation and copious greasy **steatorrhea**." },
      { "author": "Eugene Braunwald", "work": "Harrison's Principles of Internal Medicine", "quote": "A 72-hour fecal fat determination provides quantitative confirmation of **steatorrhea** in malabsorption syndromes." }
    ]
  },
  "Dashboard — steat\\steatosis.md": {
    "primary": "An abnormal accumulation of lipids or triglycerides within parenchymal cells, especially liver cells (hepatic steatosis / fatty liver).",
    "secondary": "In pathology and hepatology, intracellular lipid vacuolization (macrovesicular or microvesicular steatosis) resulting from metabolic dysfunction-associated steatotic liver disease (MASLD), alcohol toxicity, or mitochondrial impairment.",
    "quotes": [
      { "author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "In physiological fatty infiltration or pathological **steatosis**, the hepatic cells become distended with clear lipid droplets." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Chronic alcohol abuse leads progressively from simple hepatic **steatosis** to alcoholic hepatitis and irreversible cirrhosis." },
      { "author": "Eugene Braunwald", "work": "Harrison's Principles of Internal Medicine", "quote": "Non-alcoholic hepatic **steatosis** is strongly correlated with obesity, insulin resistance, and the metabolic syndrome." }
    ]
  },
  "Dashboard — sten\\apostasy.md": {
    "primary": "The formal abandonment, renunciation, or desertion of a religious belief, political principle, or allegiance.",
    "secondary": "In theological jurisprudence and intellectual history, the total repudiation of the Christian faith by a baptized believer, or defection from a party or cause.",
    "quotes": [
      { "author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The emperor Julian's celebrated **apostasy** from Christianity was nurtured by his secret devotion to the Neoplatonic mysteries." },
      { "author": "John Milton", "work": "Paradise Lost", "quote": "So spake the Seraph Abdiel, faithful found; among the faithless, faithful only he; among innumerable false, unmoved by **apostasy**." },
      { "author": "Thomas More", "work": "The Debellation of Salem and Bizance", "quote": "The canonical penalty for obstinate **apostasy** was total exclusion from the communion of the faithful." }
    ]
  },
  "Dashboard — sten\\apostate.md": {
    "primary": "A person who renounces, abandons, or deserts a religious belief, political party, or cause.",
    "secondary": "In historical biography (famously Julian the Apostate, Roman Emperor 361–363 CE), an individual who rejects former doctrines and actively opposes them.",
    "quotes": [
      { "author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Julian the **Apostate** sought to restore the ancient polytheism of Greece and Rome with all the zeal of a philosopher." },
      { "author": "John Milton", "work": "Paradise Lost", "quote": "Him the Almighty Power hurled headlong flaming from the ethereal sky, down to bottomless perdition, that **apostate** angel." },
      { "author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The revolutionary tribunal showed no mercy to the political **apostate** who deserted his principles when danger threatened." }
    ]
  },
  "Dashboard — sten\\apostatise.md": {
    "primary": "To abandon, renounce, or desert one's religious faith, principles, or allegiance; British spelling of apostatize.",
    "secondary": "In ecclesiastical history, to commit formal apostasy through public defection or recantation of holy orders.",
    "quotes": [
      { "author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Many Roman citizens chose to **apostatise** during the persecutions of Decius rather than face imprisonment or exile." },
      { "author": "Samuel Johnson", "work": "Lives of the English Poets", "quote": "Dryden was accused by his political enemies of being ready to **apostatise** whenever court patronage shifted." },
      { "author": "Walter Scott", "work": "Old Mortality", "quote": "The stern Covenanter vowed that he would rather perish upon the scaffold than **apostatise** from the solemn league." }
    ]
  },
  "Dashboard — sten\\apostatize.md": {
    "primary": "To abandon or renounce a religious belief, political conviction, or cause.",
    "secondary": "In theology and political ethics, the deliberate, overt rejection of an oath, creed, or ideological alliance.",
    "quotes": [
      { "author": "John Locke", "work": "A Letter Concerning Toleration", "quote": "No civil magistrate has the moral authority to compel any subject to **apostatize** from his religious convictions." },
      { "author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "King James attempted to bribe and intimidate his officers to **apostatize** from the Protestant communion." },
      { "author": "Jonathan Swift", "work": "A Tale of a Tub", "quote": "To **apostatize** from truth for worldly advancement has ever been the shortest road to ecclesiastical favor." }
    ]
  },
  "Dashboard — sten\\stench.md": {
    "primary": "A strong and very unpleasant smell; a foul, offensive stink.",
    "secondary": "In forensic medicine and historical descriptions of epidemic plagues, the noxious putrid effluvia arising from decomposing organic matter or unhygienic urban waste.",
    "quotes": [
      { "author": "Daniel Defoe", "work": "A Journal of the Plague Year", "quote": "The dreadful **stench** from the mass burial pits was so intolerable that the searchers were forced to breathe through vinegar cloths." },
      { "author": "Charles Dickens", "work": "Bleak House", "quote": "A pestilential **stench** rose from the sodden ground of the pauper cemetery in the heart of London." },
      { "author": "Mary Shelley", "work": "Frankenstein", "quote": "I collected bones from charnel-houses and disturbed, with profane fingers, the tremendous **stench** of the human frame." }
    ]
  },
  "Dashboard — sten\\stencil.md": {
    "primary": "A thin sheet of cardboard, metal, or plastic in which a design or lettering is cut, through which ink or paint is applied to an underlying surface.",
    "secondary": "In printmaking, signwriting, and mimeography, a printing technique where ink or dye is pressed through open cut-outs or perforated membranes onto paper, cloth, or walls.",
    "quotes": [
      { "author": "John Ruskin", "work": "The Stones of Venice", "quote": "Mechanical copying by **stencil** can never replace the living vitality and subtle variations of the human hand." },
      { "author": "William Morris", "work": "Some Hints on Pattern-Designing", "quote": "In wall decoration, a simple repeat pattern produced with a **stencil** should celebrate its flat graphic constraints." },
      { "author": "George Orwell", "work": "Nineteen Eighty-Four", "quote": "Across the hallway, the word MINITRUE was marked upon the wall in clumsy **stencil** lettering." }
    ]
  },
  "Dashboard — sten\\stenocarpus.md": {
    "primary": "A genus of woody trees and shrubs in the protea family (Proteaceae), native to eastern Australia, New Caledonia, and New Guinea.",
    "secondary": "In Australian botany and horticulture, trees typified by Stenocarpus sinuatus (the Firewheel Tree), celebrated for vibrant umbels of scarlet flowers and narrow, woody, elongated follicles containing winged seeds.",
    "quotes": [
      { "author": "Robert Brown", "work": "On the Proteaceae of Jussieu", "quote": "The genus **Stenocarpus** is characterized by its narrow, elongated follicular fruit opening on one side to release winged seeds." },
      { "author": "Ferdinand von Mueller", "work": "Fragmenta Phytographiae Australiae", "quote": "In the rainforests of Queensland, the majestic **Stenocarpus** sinuatus presents a glorious spectacle with its circular wheel of scarlet blossoms." },
      { "author": "Joseph Dalton Hooker", "work": "Curtis's Botanical Magazine", "quote": "The brilliant firewheel tree, **Stenocarpus**, flourishes in temperate conservatories, bearing umbels of vivid orange-red flowers." }
    ]
  },
  "Dashboard — sten\\stenochlaena.md": {
    "primary": "A genus of climbing or scrambling ferns in the family Blechnaceae, native to tropical Asia, Africa, and the Pacific.",
    "secondary": "In pteridology and tropical wetland ecology, epiphytic or terrestrial climbing ferns (such as Stenochlaena palustris) with dimorphic fronds, whose young coiled croziers are harvested as wild edible greens in Southeast Asia.",
    "quotes": [
      { "author": "Carl Linnaeus", "work": "Species Plantarum: Second Edition", "quote": "The tropical climbing fern **Stenochlaena** scales mangrove trunks, producing narrow fertile fronds high in the canopy." },
      { "author": "William Jackson Hooker", "work": "Species Filicum", "quote": "In **Stenochlaena**, the sterile fronds are pinnate and glossy, while the contracted fertile pinnae are covered beneath with sori." },
      { "author": "Liberty Hyde Bailey", "work": "Cyclopedia of American Horticulture", "quote": "For subtropical greenhouses, **Stenochlaena** palustris makes an attractive climber with its glossy foliage and reddish young fronds." }
    ]
  },
  "Dashboard — sten\\stenograph.md": {
    "primary": "A machine for writing shorthand; or a document written in shorthand.",
    "secondary": "In legal reporting and court recording, a specialized chorded keyboard machine (such as the Stenotype machine invented by Miles Bartholomew) used by court reporters to transcribe spoken testimony at high speeds.",
    "quotes": [
      { "author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "The clerk recorded every answer in rapid shorthand upon his portable **stenograph**." },
      { "author": "H. G. Wells", "work": "The Sleeper Awakes", "quote": "Across the desk lay the printed paper tape of the **stenograph**, transcribing the deliberations of the Council." },
      { "author": "Charles Dickens", "work": "David Copperfield", "quote": "The mechanical marvel of the **stenograph** was yet unknown when David struggled with the tortures of Gurney's shorthand." }
    ]
  },
  "Dashboard — sten\\stenographer.md": {
    "primary": "A person whose job is to transcribe spoken speech, dictation, or courtroom proceedings in shorthand or on a shorthand machine.",
    "secondary": "In legal and commercial history, professional transcriptionists who ensured verbatim documentation of trials, legislative debates, and corporate correspondence.",
    "quotes": [
      { "author": "Charles Dickens", "work": "David Copperfield", "quote": "I was a parliamentary **stenographer**, taking down the debates in the gallery of the House of Commons until four in the morning." },
      { "author": "Arthur Conan Doyle", "work": "The Adventure of the Red Circle", "quote": "The quiet **stenographer** sat in the corner of the office, her fingers flying across the shorthand notepad." },
      { "author": "H. L. Mencken", "work": "Prejudices: Sixth Series", "quote": "No official committee hearing can begin without the calm, cynical **stenographer** adjusting his machine at the table's end." }
    ]
  },
  "Dashboard — sten\\stenographic.md": {
    "primary": "Of, relating to, or written in shorthand (stenography).",
    "secondary": "In commercial and judicial documentation, rapid symbolic writing or keyboard chord systems designed to capture spoken discourse verbatim in real time.",
    "quotes": [
      { "author": "Charles Dickens", "work": "David Copperfield", "quote": "I plunged into a sea of **stenographic** mysteries, where every dot, dash, and curve seemed designed to drive me mad." },
      { "author": "Edgar Allan Poe", "work": "The Murders in the Rue Morgue", "quote": "The police retained a **stenographic** transcript of the witnesses' conflicting depositions taken at the scene." },
      { "author": "Max Müller", "work": "The Science of Thought", "quote": "Human speech is itself a species of natural **stenographic** code, condensing vast realms of thought into fleeting sounds." }
    ]
  },
  "Dashboard — sten\\stenographical.md": {
    "primary": "Pertaining to or accomplished by stenography; stenographic.",
    "secondary": "In historical reporting and court archives, describing transcripts, reports, or skills involving verbatim shorthand recording.",
    "quotes": [
      { "author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The trial of the Seven Bishops was recorded in full **stenographical** notes that circulated rapidly among the populace." },
      { "author": "Charles Dickens", "work": "The Posthumous Papers of the Pickwick Club", "quote": "The court was silenced while the clerk read from his **stenographical** notes of the morning's cross-examination." },
      { "author": "William Makepeace Thackeray", "work": "Pendennis", "quote": "Pen attempted to master the art of shorthand, but found the **stenographical** symbols hopelessly baffling." }
    ]
  },
  "Dashboard — sten\\stenography.md": {
    "primary": "The art or practice of writing in shorthand; quick, abbreviated symbolic writing.",
    "secondary": "In historical communication and commercial administration, standardized shorthand systems (such as Pitman, Gregg, and Gurney) that transformed news reporting, parliamentary recording, and secretarial science.",
    "quotes": [
      { "author": "Charles Dickens", "work": "David Copperfield", "quote": "The great task of mastering **stenography** was about equal in difficulty to learning six languages at once." },
      { "author": "Samuel Pepys", "work": "The Diary of Samuel Pepys", "quote": "I wrote down my daily secrets in Thomas Shelton's system of **stenography**, secure that no idle eye could decipher it." },
      { "author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "The art of **stenography** or short-writing is of great use for celerity in recording the fleeting thoughts of men." }
    ]
  }
}

base_cluster_dir = 'App database/Greek roots/Cluster Number & Mathematics'
slice_path = 'main app/scripts/slice-math-part3.json'

with open(slice_path, 'r', encoding='utf-8') as f:
    full_slice = json.load(f)

# Batch 3 is items 154 to 230 (77 items)
expected_keys = full_slice[154:231]

print(f"Batch 3 contains {len(batch3_data)} items.")
print(f"Expected slice items: {len(expected_keys)}")

missing = [k for k in expected_keys if k not in batch3_data]
extra = [k for k in batch3_data if k not in expected_keys]

if missing:
    print("ERROR: Missing keys in Batch 3:", missing)
    sys.exit(1)
if extra:
    print("ERROR: Extra keys in Batch 3:", extra)
    sys.exit(1)

print("Key matching confirmed perfectly!")

# Internal Quality Validation
for p, data in batch3_data.items():
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
for rel_path, data in batch3_data.items():
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

print(f"Successfully updated {updated} files in Batch 3.")
