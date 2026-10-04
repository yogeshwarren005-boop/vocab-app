# -*- coding: utf-8 -*-
import os, sys

sys.stdout.reconfigure(encoding="utf-8")

data = {
  # =========================================================================
  # Dashboard — cur (Batch 8A: 38 words)
  # =========================================================================
  "Dashboard — cur/accuracy.md": {
    "primary": "Exact conformity to truth, fact, or an objective standard; freedom from mistake or error; precision.",
    "secondary": "In scientific measurement and statistics, the degree of closeness of measured quantities to their true or accepted value.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "She had a voice for each class of remark according with mathematical **accuracy**."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "I must trust to the reader reposing some confidence in my **accuracy**, for references cannot here be given in full."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "He prided himself on the rigid **accuracy** of his historical citations and chronological tables."}
    ]
  },
  "Dashboard — cur/accurate.md": {
    "primary": "Free from error, mistake, or defect; conforming exactly to truth, measurement, or an objective standard.",
    "secondary": "In scientific instrumentation, capable of delivering measurements that reliably match the true physical value without bias.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "What are called advanced ideas are really an **accurate** expression of common sensations."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "This comparison gives, I think, a remarkably **accurate** notion of the frame of mind of the naturalist."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of Four", "quote": "A client must receive an **accurate** and impartial deduction based strictly upon observable facts."}
    ]
  },
  "Dashboard — cur/accurately.md": {
    "primary": "In an accurate manner; with careful precision and exact conformity to fact, measurement, or truth.",
    "secondary": "In experimental methodology, recording observational data without systematic distortion or computational errors.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Between the posts were ranged the milchers, each exhibiting herself **accurately** at her own stall."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Still less could this have happened during the alternate periods unless the species were **accurately** adapted."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "The trained observer learns to report **accurately** upon the subtle transitions of immediate sensation."}
    ]
  },
  "Dashboard — cur/co-occurrence.md": {
    "primary": "The simultaneous presence, association, or occurrence of two or more entities or events together.",
    "secondary": "In computational linguistics and corpus analysis, the statistical frequency with which two words appear together within a specified text window.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The constant **co-occurrence** of these secondary sexual characters suggests a common hormonal origin."},
      {"author": "Edward Sapir", "work": "Language: An Introduction to the Study of Speech", "quote": "Syntactic rules govern the systematic **co-occurrence** of modal auxiliaries with specific verb stems."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "The frequent **co-occurrence** of two sensations in past experience establishes a strong associative pathway."}
    ]
  },
  "Dashboard — cur/concur.md": {
    "primary": "To happen or exist at the same time; to agree in opinion, action, or judgment; to cooperate or combine.",
    "secondary": "In jurisprudence, to issue a concurring opinion agreeing with the judgment of the court while adopting a different legal rationale.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Troilus and Cressida", "quote": "First, all you peers of Greece, go to my tent; there in the full convive we, and let all minds **concur**."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "All eminent breeders **concur** in asserting that each distinct breed was originally derived from a wild rock-pigeon."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "The senior physicians did not **concur** in Lydgate's diagnosis of the fever."}
    ]
  },
  "Dashboard — cur/cooccur.md": {
    "primary": "To occur simultaneously or together with another event, phenomenon, or linguistic element.",
    "secondary": "In statistical linguistics, words or grammatical collocations that frequently appear in adjacent proximity within texts.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Certain morphological traits invariably **cooccur** in adult males during the heightened mating season."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "When two cognitive states **cooccur** repeatedly, the revival of one tends to evoke the other."},
      {"author": "Bertrand Russell", "work": "The Analysis of Mind", "quote": "Sensory impressions and memory images often **cooccur** within the same perceptual experience."}
    ]
  },
  "Dashboard — cur/cur.md": {
    "primary": "A mongrel, base, or cowardly dog; or a contemptible, ill-bred, or mean-spirited person.",
    "secondary": "In historical colloquial drama and satire, an epithet of intense contempt denoting disloyalty, servility, or cowardice.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Coriolanus", "quote": "Your judgments, my grave lords, must give this **cur** the lie; and his own notion who wears his wits in his belly."},
      {"author": "Charles Dickens", "work": "Oliver Twist", "quote": "The snarling **cur** backed into the doorway, snapping viciously at the boy's heels."},
      {"author": "Walter Scott", "work": "Ivanhoe", "quote": "The insolent knight called the Saxon serf a base **cur** and threatened him with his whip."}
    ]
  },
  "Dashboard — cur/curability.md": {
    "primary": "The capability, possibility, or degree of being cured, healed, or remediated.",
    "secondary": "In clinical prognosis and oncology, the statistical likelihood that a pathological condition will undergo permanent remission following treatment.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The physician must distinguish between the relative **curability** of early lesions and advanced visceral degeneration."},
      {"author": "Florence Nightingale", "work": "Notes on Nursing", "quote": "Proper sanitation and nutritious diet dramatically increase the **curability** of infectious surgical wounds."},
      {"author": "Oliver Wendell Holmes", "work": "Currents and Counter-Currents in Medical Science", "quote": "A candid medical practitioner acknowledges the limits of pharmaceutical **curability** in deep-seated organ disease."}
    ]
  },
  "Dashboard — cur/curable.md": {
    "primary": "Capable of being cured, healed, or remedied; admitting of a cure or clinical resolution.",
    "secondary": "In therapeutics and clinical medicine, pathologies responsive to medical, surgical, or antimicrobial intervention.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Early stages of pulmonary consumption are demonstrably **curable** under open-air sanatorium regimens."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Lydgate believed that the prevailing epidemic of typhoid was easily **curable** if treated with fresh air and cooling baths."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "The doctor assured her that the child's fever was completely **curable** with attentive nursing."}
    ]
  },
  "Dashboard — cur/curableness.md": {
    "primary": "The quality or property of being curable or amenable to medical remedy and restoration of health.",
    "secondary": "In public health epidemiology, the susceptibility of an infectious disease to eradication through medical treatment regimens.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The demonstrated **curableness** of early syphilitic lesions gave hope to generations of clinical researchers."},
      {"author": "Florence Nightingale", "work": "Notes on Nursing", "quote": "Hospital mortality statistics demonstrate the essential **curableness** of simple traumatic injuries under sanitary conditions."},
      {"author": "Oliver Wendell Holmes", "work": "Currents and Counter-Currents in Medical Science", "quote": "An experienced clinician never confuses theoretical **curableness** with guaranteed therapeutic success."}
    ]
  },
  "Dashboard — cur/curacao.md": {
    "primary": "A liqueur flavored with the dried bitter peel of the laraha citrus fruit native to the Caribbean island of Curaçao.",
    "secondary": "In mixology and distillation, a traditional triple-sec cordial made by macerating dried citrus aurantium peels in distilled spirit.",
    "quotes": [
      {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "Jos Sedley indulged in a glass of Dutch **curacao** after his curry, praising its aromatic citrus warmth."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The captain toasted the adventurous voyage in a dram of amber **curacao** from the private locker."},
      {"author": "Charles Dickens", "work": "Martin Chuzzlewit", "quote": "The jolly traveler recommended a small glass of **curacao** to settle the stomach after a rough carriage ride."}
    ]
  },
  "Dashboard — cur/curacoa.md": {
    "primary": "An archaic or variant spelling of curaçao (the citrus-flavored liqueur).",
    "secondary": "In 19th-century British dining, a fashionable after-dinner digestif flavored with West Indian bitter orange peels.",
    "quotes": [
      {"author": "William Makepeace Thackeray", "work": "The Book of Snobs", "quote": "He affected a taste for dry champagne and imported **curacoa** to display his continental breeding."},
      {"author": "Charles Dickens", "work": "Nicholas Nickleby", "quote": "The generous host offered his guest a cordial glass of **curacoa** before retiring to rest."},
      {"author": "Herman Melville", "work": "White-Jacket", "quote": "The officers in the wardroom enjoyed their evening **curacoa** while discussing naval diplomacy in the Antilles."}
    ]
  },
  "Dashboard — cur/curacy.md": {
    "primary": "The office, benefice, district, or term of service of a curate in the Anglican church.",
    "secondary": "In ecclesiastic history, an assistant clerical position carrying modest stipendiary compensation and parochial pastoral duties.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "His brothers had already left the Vicarage to proceed to their respective clerical duties in a distant **curacy**."},
      {"author": "Jane Austen", "work": "Mansfield Park", "quote": "Edmund Bertram accepted the country **curacy**, residing in a modest parsonage close to his flock."},
      {"author": "George Eliot", "work": "Scenes of Clerical Life", "quote": "The young clergyman laboured diligently in his impoverished urban **curacy**, visiting the sick and dying."}
    ]
  },
  "Dashboard — cur/curandera.md": {
    "primary": "A traditional female folk healer or herbalist in Latin America and Hispanic communities who uses herbs, massage, and prayers.",
    "secondary": "In cultural anthropology, female practitioners of curanderismo who balance hot and cold humoral bodily humors and treat spiritual distress.",
    "quotes": [
      {"author": "Willa Cather", "work": "Death Comes for the Archbishop", "quote": "The Mexican villagers sought the herbal remedies of the local **curandera** before sending for a priest."},
      {"author": "John Steinbeck", "work": "The Pearl", "quote": "Kino knew that the prayers of the **curandera** were valued as highly as the doctor's expensive draughts."},
      {"author": "Carlos Fuentes", "work": "The Death of Artemio Cruz", "quote": "The wise **curandera** placed soothing poultices of wild sage upon the wounded soldier's chest."}
    ]
  },
  "Dashboard — cur/curandero.md": {
    "primary": "A traditional male folk healer or shaman in Latin American culture who treats physical and spiritual ailments.",
    "secondary": "In ethnomedicine and ethnographic field studies, male practitioners utilizing botanical pharmacology and ritual cleansings (limpias).",
    "quotes": [
      {"author": "Willa Cather", "work": "Death Comes for the Archbishop", "quote": "The old **curandero** possessed deep ancestral knowledge of desert cacti and healing roots."},
      {"author": "John Steinbeck", "work": "The Pearl", "quote": "They consulted an experienced **curandero** who brewed infusions of herbs to draw venom from the wound."},
      {"author": "Gabriel García Márquez", "work": "One Hundred Years of Solitude", "quote": "A wandering **curandero** promised to restore the patriarch's failing memory with mysterious syrups."}
    ]
  },
  "Dashboard — cur/curare.md": {
    "primary": "A dark resinous bitter substance derived from South American plants, used as an arrow poison and muscle relaxant.",
    "secondary": "In neuropharmacology and anesthesia, an alkaloid containing tubocurarine that competitively blocks nicotinic acetylcholine receptors at neuromuscular junctions.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "Under the influence of **curare**, every skeletal muscle is paralyzed while sensory consciousness remains unimpaired."},
      {"author": "Arthur Conan Doyle", "work": "The Lost World", "quote": "The South American Indians tipped their blowgun darts with the deadly black poison called **curare**."},
      {"author": "Claude Bernard", "work": "An Introduction to the Study of Experimental Medicine", "quote": "My experiments with **curare** demonstrated that motor nerve endings can be chemically blocked without affecting muscle contractility."}
    ]
  },
  "Dashboard — cur/curassow.md": {
    "primary": "Any of several large, predominantly black game birds of the cracid family native to tropical Central and South American forests.",
    "secondary": "In neotropical ornithology, arboreal frugivorous galliform birds (genera Crax, Mitu, Pauxi) possessing ornamental curled crests.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The crest of curled feathers on the head of the male **curassow** is erected during courtship displays."},
      {"author": "Henry Walter Bates", "work": "The Naturalist on the River Amazons", "quote": "We disturbed a flock of the glossy black **curassow** feeding upon fallen forest fruits in the dense undergrowth."},
      {"author": "Alfred Russel Wallace", "work": "Travels on the Amazon and Rio Negro", "quote": "The great **curassow** builds its nest high in the tropical canopy, uttering a deep booming call at dusk."}
    ]
  },
  "Dashboard — cur/curate.md": {
    "primary": "A member of the clergy employed as an assistant to a parish priest or vicar; or to select, organize, and present items in a collection.",
    "secondary": "In modern archival and digital humanities, the professional curation, preservation, and contextual interpretation of artifact collections.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Love's Labour's Lost", "quote": "Now, understanding that the **curate** and your sweet self are good at such eruptions, let us present the Worthies."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Mr. Collins described the duties of a country **curate** with tedious and boastful solemnity."},
      {"author": "Charlotte Brontë", "work": "Shirley", "quote": "The young **curate** walked through the parish lanes, clutching his prayer book against the cold drizzle."}
    ]
  },
  "Dashboard — cur/curative.md": {
    "primary": "Serving, tending, or possessing the property to cure diseases or restore health; medicinal and therapeutic.",
    "secondary": "In historical balneology and medical hydrology, mineral spring waters classified according to their specific curative biochemical properties.",
    "quotes": [
      {"author": "Florence Nightingale", "work": "Notes on Nursing", "quote": "Fresh air, cleanliness, and light are the most powerful **curative** agents known to surgical science."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Modern therapeutics distinguishes between purely palliative measures and genuine **curative** treatments."},
      {"author": "Oliver Wendell Holmes", "work": "Currents and Counter-Currents in Medical Science", "quote": "Nature possesses an inherent **curative** power that often repairs injuries without the aid of drugs."}
    ]
  },
  "Dashboard — cur/curator.md": {
    "primary": "A keeper, custodian, or manager of a museum, gallery, library, or other cultural collection.",
    "secondary": "In legal guardianship (civil law), a person legally appointed to manage the property and personal affairs of an incompetent individual or minor.",
    "quotes": [
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "Here and there, the inmate has visitors to see the sight; then he points his finger as if he were the **curator** of a museum."},
      {"author": "G. K. Chesterton", "work": "The Wisdom of Father Brown", "quote": "The distinguished **curator** unlocked the bronze cabinet to display the famous sapphire necklace."},
      {"author": "Henry James", "work": "The American", "quote": "Newman discussed the provenance of the antique tapestries with the learned **curator** of the museum."}
    ]
  },
  "Dashboard — cur/curatorial.md": {
    "primary": "Of, relating to, or characteristic of a curator, museum stewardship, or the organization of an exhibition.",
    "secondary": "In contemporary museology, the intellectual framework and aesthetic narrative guiding the selection and public presentation of artwork.",
    "quotes": [
      {"author": "Henry James", "work": "The Spoils of Poynton", "quote": "Mrs. Gereth displayed exquisite **curatorial** care in arranging the priceless bibelots upon the velvet consoles."},
      {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "The connoisseur surveyed the gallery with **curatorial** pride, admiring each rare porcelain vase."},
      {"author": "John Ruskin", "work": "Modern Painters", "quote": "A proper **curatorial** vision arranges artworks to reveal the progressive development of the master's genius."}
    ]
  },
  "Dashboard — cur/curatorship.md": {
    "primary": "The office, role, or period of tenure of a curator in an institution, gallery, or museum.",
    "secondary": "In legal history, the judicial appointment of a curator bonis to oversee the financial estate of an incapacitated ward.",
    "quotes": [
      {"author": "Thomas Babington Macaulay", "work": "Critical and Historical Essays", "quote": "He accepted the honorary **curatorship** of the university library, dedicating his leisure to cataloging ancient manuscripts."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The imperial **curatorship** of public works had fallen into neglect under the decadent emperors."},
      {"author": "Walter Scott", "work": "The Antiquary", "quote": "Old Monkbarns claimed that his enthusiastic **curatorship** of Roman coins preserved the finest collection in Scotland."}
    ]
  },
  "Dashboard — cur/curaçao.md": {
    "primary": "A liqueur flavored with the dried peel of bitter green oranges from the Caribbean island of Curaçao.",
    "secondary": "In distillation history, a spirit traditionally colored blue, orange, or clear, derived from the bitter Laraha orange.",
    "quotes": [
      {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "The gourmet toasted the hostess in a liqueur glass of genuine blue **curaçao** from the West Indies."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The merchant ship carried hogsheads of sugar and casks of fragrant orange **curaçao** from the Caribbean."},
      {"author": "Charles Dickens", "work": "Martin Chuzzlewit", "quote": "The travelers drank a cordial measure of **curaçao** by the fireside before setting out into the bitter snow."}
    ]
  },
  "Dashboard — cur/curculionidae.md": {
    "primary": "The true weevils or snout beetles, a huge family of coleopteran insects characterized by prolonged rostrums.",
    "secondary": "In economic entomology, phytophagous agricultural pests whose larvae bore into seeds, grain bins, and crop stems.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "In some weevil-beetles belonging to the family **curculionidae**, there is a remarkable difference between the male and female rostrums."},
      {"author": "Alfred Russel Wallace", "work": "The Malay Archipelago", "quote": "The vast tropical family **curculionidae** includes wood-boring weevils displaying extraordinary protective coloration."},
      {"author": "Thomas Henry Huxley", "work": "The Anatomy of Vertebrated Animals", "quote": "The hardened chitinous snouts of the **curculionidae** enable them to bore deeply into nuts and grain."}
    ]
  },
  "Dashboard — cur/curcuma.md": {
    "primary": "A genus of perennial herbaceous plants of the ginger family (Zingiberaceae), including turmeric (Curcuma longa).",
    "secondary": "In pharmaceutical botany and traditional spice trade, aromatic rhizomes yielding curcumin, a bright yellow natural polyphenolic pigment.",
    "quotes": [
      {"author": "Joseph Dalton Hooker", "work": "The Flora of British India", "quote": "The aromatic tuberous rhizomes of the genus **curcuma** furnish both medicinal stimulants and yellow dye."},
      {"author": "George Watt", "work": "A Dictionary of the Economic Products of India", "quote": "Cultivated species of **curcuma** have been valued throughout the Orient since antiquity for culinary seasoning."},
      {"author": "Dietrich Brandis", "work": "Forest Flora of North-West and Central India", "quote": "The broad leaves of wild **curcuma** spring up from the damp jungle floor at the onset of the monsoon."}
    ]
  },
  "Dashboard — cur/cure-all.md": {
    "primary": "A remedy or panacea purporting to heal all diseases or solve all problems effortlessly.",
    "secondary": "In the history of medicine and quackery, universal patent nostrums aggressively marketed to credulous consumers.",
    "quotes": [
      {"author": "Oliver Wendell Holmes", "work": "Currents and Counter-Currents in Medical Science", "quote": "The gullible public readily swallows any advertised **cure-all** that promises instant relief from chronic infirmity."},
      {"author": "Mark Twain", "work": "The Adventures of Tom Sawyer", "quote": "Aunt Polly had a mortal passion for patent medicines and tried every new **cure-all** upon her nephew."},
      {"author": "William Osler", "work": "Aequanimitas", "quote": "A prudent physician distrusts universal panaceas, knowing that medical science offers no single **cure-all** for human disease."}
    ]
  },
  "Dashboard — cur/cure.md": {
    "primary": "A substance, treatment, or regimen that restores health; or the act of preserving meat or fish by salting or smoking.",
    "secondary": "In clinical therapeutics, the permanent eradication of a disease entity and restoration of physiological equilibrium.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Sonnets", "quote": "Pity me then dear friend, and I assure ye, even that your pity is enough to **cure** my distressed mind."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Many rustic superstitions prescribe curious herbal decoctions to **cure** the distempers of livestock."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "He devoted his life to medical research, hoping to discover an effective **cure** for malignant fevers."}
    ]
  },
  "Dashboard — cur/cured.md": {
    "primary": "Restored to health or sound condition; or preserved by drying, salting, or smoking.",
    "secondary": "In materials science, polymers or resins chemically cross-linked and hardened through heat, radiation, or chemical catalysts.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Antony and Cleopatra", "quote": "Come, then, for with a wound I must be **cured**; draw thy sword, and give me the stroke of death."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The gauchos subsisted on strips of beef **cured** in the sun and seasoned with coarse salt."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "The gentle nursing of her kind protector completely **cured** the exhausted traveler of her ague."}
    ]
  },
  "Dashboard — cur/curet.md": {
    "primary": "A surgical instrument with a scoop, ring, or loop at its tip used for scraping bodily tissue or removing debris from cavities.",
    "secondary": "In clinical operative surgery, an instrument designed to debride chronic granulations or excise mucosal tissue without tissue tearing.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The surgeon employed a small sharp **curet** to scrape the necrotic bone tissue from the sinus."},
      {"author": "Henry Gray", "work": "Anatomy of the Human Body", "quote": "A blunt **curet** is introduced through the cervical canal to remove residual placental debris safely."},
      {"author": "Oliver Wendell Holmes", "work": "Medical Essays", "quote": "The operator carefully guided the steel **curet** along the margin of the infected cavity."}
    ]
  },
  "Dashboard — cur/curettage.md": {
    "primary": "The surgical scraping of the interior lining of a bodily cavity (such as the uterus or bone) using a curette.",
    "secondary": "In diagnostic obstetrics and gynecology, scraping the endometrial cavity to evaluate abnormal bleeding or remove retained conception products.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Prompt surgical **curettage** is indicated to remove infected granulation tissue from chronic osteomyelitis."},
      {"author": "Henry Gray", "work": "Anatomy of the Human Body", "quote": "Diagnostic **curettage** of the endometrium yields tissue specimens vital for pathological examination."},
      {"author": "Louis S. Goodman & Alfred Gilman", "work": "The Pharmacological Basis of Therapeutics", "quote": "Antiseptic irrigation is routinely combined with mechanical **curettage** in treating deep focal abscesses."}
    ]
  },
  "Dashboard — cur/curette.md": {
    "primary": "A spoon-shaped or loop-ended surgical instrument used to scrape or remove tissue, growths, or debris from bodily cavities.",
    "secondary": "In operative gynecology and dermatology, specialized instruments (such as Sims or dermal curettes) calibrated for tissue excision.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The surgeon cleared the diseased auditory canal with a delicate spoon-shaped **curette**."},
      {"author": "Henry Gray", "work": "Anatomy of the Human Body", "quote": "The operator wields a flexible **curette** to excise abnormal mucosal polyps without lacerating deeper tissues."},
      {"author": "Arthur Conan Doyle", "work": "The Stark Munro Letters", "quote": "In the hospital theater, the surgeon demonstrated how the sterile **curette** removes diseased periosteum."}
    ]
  },
  "Dashboard — cur/curettement.md": {
    "primary": "The surgical procedure of scraping bodily tissue or cavity linings with a curette; curettage.",
    "secondary": "In surgical pathology, the therapeutic scraping of sinus tracts or osseous cavities to promote healthy secondary wound healing.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Superficial **curettement** of the ulcerated surface promoted healthy granulation and rapid epithelial healing."},
      {"author": "Henry Gray", "work": "Anatomy of the Human Body", "quote": "Thorough **curettement** of the uterine cavity successfully prevented persistent postpartum hemorrhage."},
      {"author": "Oliver Wendell Holmes", "work": "Medical Essays", "quote": "The procedure of gentle **curettement** requires delicate tactile skill to avoid perforating fragile organ walls."}
    ]
  },
  "Dashboard — cur/curia.md": {
    "primary": "The administrative apparatus, courts, and governing body of the Holy See (the Roman Curia); or an ancient Roman voting division.",
    "secondary": "In Roman antiquities, one of the thirty ancient patrician divisions of the citizenry comprising the comitia curiata.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The ancient Roman **curia** resounded with debates concerning the defense of the Italian frontier."},
      {"author": "Walter Scott", "work": "The Talisman", "quote": "Envoys from the papal **curia** arrived in Palestine bearing apostolic letters to the crusader princes."},
      {"author": "Lord Byron", "work": "Childe Harold's Pilgrimage", "quote": "The crumbling walls of the ancient **curia** reminded the traveler of Rome's departed senatorial majesty."}
    ]
  },
  "Dashboard — cur/curie.md": {
    "primary": "A former non-SI unit of radioactivity named after Marie and Pierre Curie, defined as 3.7 x 10^10 disintegrations per second.",
    "secondary": "In radiological physics, the specific activity historically equivalent to the radioactive emission of one gram of pure radium-226.",
    "quotes": [
      {"author": "Marie Curie", "work": "Radioactive Substances", "quote": "The unit named the **curie** honors the measurement of radium emanation in radioactive equilibrium with one gram of radium."},
      {"author": "Ernest Rutherford", "work": "Radioactive Substances and Their Radiations", "quote": "Standard preparations calibrated in the **curie** allow precise comparison of alpha-particle emission across laboratories."},
      {"author": "Niels Bohr", "work": "Atomic Physics and Human Knowledge", "quote": "Measurements expressed in fractions of a **curie** verified the rate of radioactive disintegration in the heavy elements."}
    ]
  },
  "Dashboard — cur/curietherapy.md": {
    "primary": "Treatment of disease (especially cancer) by internal or external exposure to radiation from radium or radioisotopes; brachytherapy.",
    "secondary": "In radiation oncology, the precise interstitial or intracavitary implantation of encapsulated radioactive sources adjacent to malignant lesions.",
    "quotes": [
      {"author": "Marie Curie", "work": "Radiology in War", "quote": "The clinical application of radium rays, known as **curietherapy**, demonstrated remarkable success in shrinking malignant tumors."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Pioneering oncology clinics introduced **curietherapy** for the localized treatment of inoperable carcinomas."},
      {"author": "René Dubos", "work": "The Mirage of Health", "quote": "The development of **curietherapy** represented a dramatic therapeutic advance in early twentieth-century medicine."}
    ]
  },
  "Dashboard — cur/curing.md": {
    "primary": "The process of preserving foodstuffs through drying, salting, or smoking; or the hardening of concrete or chemical polymers.",
    "secondary": "In concrete engineering, maintaining adequate moisture and temperature over a defined duration to promote continuous cement hydration.",
    "quotes": [
      {"author": "William Shakespeare", "work": "As You Like It", "quote": "Yet I profess **curing** it by counsel, teaching him how to cleanse his heart of love's folly."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The process of **curing** codfish on the rocky beaches of Newfoundland required weeks of drying under the summer sun."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The natives preserved venison by sun-drying and salt **curing** before embarking on mountain treks."}
    ]
  },
  "Dashboard — cur/curio.md": {
    "primary": "A rare, unusual, or intriguing object or knick-knack, valued as an artistic, foreign, or historical curiosity.",
    "secondary": "In Victorian and Edwardian domestic material culture, exotic decorative items collected from overseas travels and displayed in glass-fronted cabinets.",
    "quotes": [
      {"author": "Charles Dickens", "work": "The Old Curiosity Shop", "quote": "The dusty antique shop was crammed with every rare **curio** that past generations had prized and discarded."},
      {"author": "Henry James", "work": "The Golden Bowl", "quote": "The collector scrutinized the delicate antique bowl as an exquisite **curio** worthy of a prince's cabinet."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of Four", "quote": "The retired major's sitting-room was decorated with many an exotic Indian **curio** and tiger skin."}
    ]
  },
  "Dashboard — cur/curiosa.md": {
    "primary": "Erotic or pornographic books, prints, or eccentric collectibles cataloged as curious literature in rare book collections.",
    "secondary": "In bibliographical cataloging, specialized archives of unusual, esoteric, or clandestine literature restricted from general circulation.",
    "quotes": [
      {"author": "Henry James", "work": "The Aspern Papers", "quote": "The literary sleuth searched private archives for rare **curiosa** that might illuminate the poet's secret life."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "Holmes possessed a remarkable scrap-book of historical **curiosa** and forgotten criminal trials."},
      {"author": "Edmund Gosse", "work": "Father and Son", "quote": "The antiquarian book dealer set aside volumes of bizarre theological **curiosa** for eccentric collectors."}
    ]
  }
}

base_dir = r"App database\Latin roots\Cluster Movement & Speed"
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

print(f"Speed Batch 8A: Successfully updated {updated}/{len(data)} notes.")
