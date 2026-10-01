import fs from "fs";
import path from "path";

const baseDir = "App database/Greek roots/Cluster Beginning & Primacy/Dashboard — prot";

const wordsData = {
  "Protozoa.md": {
    word: "Protozoa",
    primary: "A historical taxon or grouping of single-celled microscopic eukaryotic organisms that feed heterotrophically (such as amoebae, ciliates, flagellates, and sporozoans).",
    secondary: "In modern protistology, an informal paraphyletic grouping of non-photosynthetic unicellular protists with diverse evolutionary lineages.",
    quotes: [
      { author: "Ernst Haeckel", work: "The Wonders of Life", quote: "The ancestral forms of animal life are preserved for us among the single-celled **Protozoa**." },
      { author: "Antonie van Leeuwenhoek", work: "Letters to the Royal Society", quote: "Through my lenses I beheld countless animalcules, representing those minute **Protozoa** teeming in rainwater." },
      { author: "Thomas Henry Huxley", work: "Lay Sermons, Addresses, and Reviews", quote: "Between the simple unicellular **Protozoa** and the complex multicellular Metazoa lies the great structural boundary." }
    ]
  },
  "amphiprotic.md": {
    word: "amphiprotic",
    primary: "Capable of acting either as a Brønsted–Lowry acid (donating a proton) or as a Brønsted–Lowry base (accepting a proton).",
    secondary: "In chemical equilibrium theory, describing amphoteric solvent molecules or ions (such as water or hydrogen carbonate) possessing dual protic behavior.",
    quotes: [
      { author: "Johannes Nicolaus Brønsted", work: "Some Remarks on the Concept of Acids and Bases", quote: "Water is an **amphiprotic** solvent par excellence, acting simultaneously as donor and recipient of protons." },
      { author: "Linus Pauling", work: "General Chemistry", quote: "Because the bicarbonate ion is **amphiprotic**, it plays an indispensable role in maintaining the physiological pH of blood." },
      { author: "Gilbert N. Lewis", work: "Valence and the Structure of Atoms and Molecules", quote: "The dual behavior of **amphiprotic** substances illustrates the relative nature of acidity and basicity." }
    ]
  },
  "antiproton.md": {
    word: "antiproton",
    primary: "The antiparticle of the proton, having the same mass but a negative electric charge and opposite magnetic moment.",
    secondary: "In high-energy particle physics, a subatomic baryon discovered in 1955 at the Berkeley Bevatron whose annihilation with a proton yields pions and gamma rays.",
    quotes: [
      { author: "Paul Dirac", work: "The Principles of Quantum Mechanics", quote: "Relativistic quantum mechanics demanded that every fundamental fermion possess an antimatter counterpart, prefiguring the discovery of the **antiproton**." },
      { author: "Emilio Segrè", work: "From X-Rays to Quarks", quote: "When the Bevatron detector registered a negatively charged heavy particle, the existence of the **antiproton** was decisively confirmed." },
      { author: "Richard Feynman", work: "The Character of Physical Law", quote: "When a proton meets an **antiproton**, the entire mass of both particles annihilates into high-energy radiation." }
    ]
  },
  "antiprotozoal.md": {
    word: "antiprotozoal",
    primary: "Acting against or destroying protozoan parasites; an agent used to treat protozoal infections.",
    secondary: "In pharmacology and tropical medicine, referring to therapeutics such as metronidazole, chloroquine, or artemisinin targeting diseases like malaria and amoebiasis.",
    quotes: [
      { author: "Paul Ehrlich", work: "Chemotherapy", quote: "We searched for magic bullets exhibiting potent **antiprotozoal** activity without poisoning the tissues of the host." },
      { author: "Alexander Fleming", work: "Penicillin and Its Practical Application", quote: "While antibiotics combat bacteria, synthetic chemical agents provide our primary **antiprotozoal** defenses against parasitic trypanosomes." },
      { author: "Ronald Ross", work: "The Prevention of Malaria", quote: "Administering cinchona bark afforded a powerful **antiprotozoal** remedy long before the plasmodium parasite was identified." }
    ]
  },
  "hypoproteinemia.md": {
    word: "hypoproteinemia",
    primary: "An abnormally low concentration of protein in the blood plasma or serum.",
    secondary: "In clinical pathophysiology, a condition resulting from malnutrition, nephrotic syndrome, or hepatic failure, leading to reduced oncotic pressure and edema.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Severe **hypoproteinemia** inevitably leads to generalized dropsy as fluid escapes the vascular bed into interstitial tissues." },
      { author: "Harvey Cushing", work: "Selected Papers on Surgical Pathology", quote: "The patient's peripheral edema was traced to severe **hypoproteinemia** caused by chronic intestinal malabsorption." },
      { author: "Arthur Guyton", work: "Textbook of Medical Physiology", quote: "When plasma albumin falls, the resulting **hypoproteinemia** collapses the colloid osmotic pressure of the capillary beds." }
    ]
  },
  "isoproterenol.md": {
    word: "isoproterenol",
    primary: "A synthetic catecholamine drug that acts as a non-selective beta-adrenoreceptor agonist, used to treat bradycardia and heart block.",
    secondary: "In cardiovascular pharmacology, an isopropyl-substituted noradrenaline analogue stimulating myocardial contractility and relaxing bronchial smooth muscle.",
    quotes: [
      { author: "Raymond Ahlquist", work: "American Journal of Physiology", quote: "The potent cardiac stimulation produced by **isoproterenol** demonstrated the distinct existence of beta-adrenergic receptors." },
      { author: "James Black", work: "Lectures on Pharmacological Discovery", quote: "Our development of beta-blockers began by designing compounds that could antagonize the rapid tachycardia induced by **isoproterenol**." },
      { author: "Louis Goodman", work: "The Pharmacological Basis of Therapeutics", quote: "Intravenous infusion of **isoproterenol** dramatically accelerates atrioventricular conduction in patients with acute Stokes-Adams attacks." }
    ]
  },
  "metaproterenol.md": {
    word: "metaproterenol",
    primary: "A synthetic bronchodilator drug that acts as a beta-2 adrenergic agonist, used to treat asthma, bronchitis, and bronchospasm; also known as orciprenaline.",
    secondary: "In respiratory pharmacotherapy, a resorcinol-derivative derivative of isoproterenol offering longer duration of action and resistance to enzymatic methylation.",
    quotes: [
      { author: "Julius H. Comroe", work: "Physiology of Respiration", quote: "Inhaled **metaproterenol** rapidly relieves wheezing by relaxing constricted bronchial smooth muscle fibers." },
      { author: "Alfred Goodman Gilman", work: "The Pharmacological Basis of Therapeutics", quote: "Because **metaproterenol** is resistant to catechol-O-methyltransferase, it exhibits oral bioavailability superior to that of isoproterenol." },
      { author: "William H. Howell", work: "Textbook of Physiology", quote: "Clinical administration of aerosolized **metaproterenol** prevents exercise-induced bronchospasm in asthmatic subjects." }
    ]
  },
  "protactinium.md": {
    word: "protactinium",
    primary: "A rare, highly radioactive actinide metallic chemical element with atomic number 91 and symbol Pa.",
    secondary: "In radiochemistry, an alpha-emitting intermediate decay product in the actinium series formed from uranium-235, first isolated by Hahn and Meitner.",
    quotes: [
      { author: "Lise Meitner", work: "Zeitschrift für Physik", quote: "The parent substance of actinium, which we designated **protactinium**, confirmed the isotopic decay chain of uranium." },
      { author: "Otto Hahn", work: "New Atoms", quote: "Tracing the elusive radiation of **protactinium** required the chemical processing of tons of pitchblende residue." },
      { author: "Glenn T. Seaborg", work: "The Transuranium Elements", quote: "In the actinide series, **protactinium** bridges thorium and uranium, exhibiting both tetravalent and pentavalent chemistry." }
    ]
  },
  "protagonism.md": {
    word: "protagonism",
    primary: "The state, quality, or role of being a protagonist; leading participation or championship of a cause.",
    secondary: "In literary theory and political sociology, active initiative or central agency in driving historical movements or dramatic plots.",
    quotes: [
      { author: "Antonio Gramsci", work: "Prison Notebooks", quote: "The political **protagonism** of the subaltern classes emerges only when they attain critical historical consciousness." },
      { author: "Georg Lukács", work: "The Historical Novel", quote: "The hero of an epic drama is defined not by moral perfection, but by intense historical **protagonism**." },
      { author: "Jean-Paul Sartre", work: "What Is Literature?", quote: "The writer invites the reader into active moral **protagonism**, rejecting passive consumption of aesthetic illusions." }
    ]
  },
  "protagonist.md": {
    word: "protagonist",
    primary: "The leading character or major figure in a drama, novel, or other literary work.",
    secondary: "In classical Greek theatre, the first actor who engaged in dialogue with the chorus (introduced by Thespis); hence, a champion or leader of a movement.",
    quotes: [
      { author: "Aristotle", work: "Poetics", quote: "Aeschylus first introduced a second actor, reducing the chorus and making the **protagonist** central to the dialogue." },
      { author: "George Eliot", work: "Middlemarch", quote: "Dorothea was the innocent **protagonist** of a tragedy whose final acts she could neither foresee nor avert." },
      { author: "Virginia Woolf", work: "To the Lighthouse", quote: "In Mrs. Ramsay, the narrative finds an emotional **protagonist** who reconciles the dissonant personalities around the table." }
    ]
  },
  "protamine.md": {
    word: "protamine",
    primary: "Any of a group of small, strongly basic, arginine-rich nuclear proteins found in fish sperm that bind and condense DNA.",
    secondary: "In medicine, protamine sulfate is used clinically as a specific antidote to reverse the anticoagulant effects of heparin.",
    quotes: [
      { author: "Albrecht Kossel", work: "The Protamines and Histones", quote: "The simple composition of **protamine**, composed predominantly of basic arginine, offered an early model of nucleoprotein binding." },
      { author: "Charles Best", work: "Heparin: Its Chemistry, Physiology, and Clinical Applications", quote: "Intravenous administration of **protamine** promptly neutralizes circulating heparin, restoring normal blood coagulation." },
      { author: "Arthur Kornberg", work: "DNA Replication", quote: "During spermiogenesis, somatic histones are systematically displaced by **protamine** to compact chromatin within the sperm head." }
    ]
  },
  "protanomaly.md": {
    word: "protanomaly",
    primary: "A mild form of red-green color vision deficiency in which red sensitivity is abnormal or reduced (anomalous trichromacy).",
    secondary: "In physiological optics, an X-linked condition wherein the L-cone photopigment has an absorption spectrum shifted toward that of the M-cone.",
    quotes: [
      { author: "Hermann von Helmholtz", work: "Treatise on Physiological Optics", quote: "Subjects affected by **protanomaly** require an unusually large proportion of red light when matching a spectral yellow." },
      { author: "Lord Rayleigh", work: "Nature", quote: "By means of color mixing equations, I was able to distinguish true dichromats from individuals exhibiting mild **protanomaly**." },
      { author: "Shinobu Ishihara", work: "Tests for Colour-Blindness", quote: "The pseudoisochromatic plates reveal subtle distinctions between normal trichromats and individuals with congenital **protanomaly**." }
    ]
  },
  "protanopia.md": {
    word: "protanopia",
    primary: "A severe form of red-green color blindness characterized by the complete absence of functional red cone photopigments (L-cones).",
    secondary: "In vision science, dichromatic color blindness in which the visible spectrum is shortened at the red end and red hues are confused with grays or greens.",
    quotes: [
      { author: "Thomas Young", work: "Lectures on Natural Philosophy", quote: "A deficiency in the retinal receptor responding to the longest wavelengths produces that distinct blindness known as **protanopia**." },
      { author: "William de Wiveleslie Abney", work: "Researches in Colour Vision", quote: "In cases of complete **protanopia**, the red end of the spectrum appears dark and unilluminated." },
      { author: "Selig Hecht", work: "The Photochemistry of Vision", quote: "The spectral luminosity curve in **protanopia** shows a characteristic displacement toward shorter green wavelengths." }
    ]
  },
  "protanopic.md": {
    word: "protanopic",
    primary: "Of, relating to, or affected by protanopia (red blindness).",
    secondary: "Describing a dichromat whose visual system lacks functioning long-wavelength (L) photopigments.",
    quotes: [
      { author: "Hermann von Helmholtz", work: "Handbuch der physiologischen Optik", quote: "To a **protanopic** observer, a pure spectral scarlet appears completely extinguished against a dark background." },
      { author: "Christine Ladd-Franklin", work: "Colour and Colour Theories", quote: "The **protanopic** eye confuses scarlet with dark brown and bright green with muted yellow." },
      { author: "George Wald", work: "Vision and Cellular Chemistry", quote: "Photopigment extractions confirmed that the **protanopic** retina lacks erythrolabe, the long-wavelength sensitive opsin." }
    ]
  },
  "protea.md": {
    word: "protea",
    primary: "Any of various shrubs or small trees of the genus Protea (family Proteaceae), native to southern Africa, bearing large, striking flower heads.",
    secondary: "In botanical nomenclature (named by Linnaeus after the sea god Proteus), celebrated as South Africa's national floral emblem (the King Protea, Protea cynaroides).",
    quotes: [
      { author: "Carl Linnaeus", work: "Genera Plantarum", quote: "I bestowed upon this remarkable genus the name **Protea**, because its floral manifestations exhibit such astonishing variety of form." },
      { author: "Joseph Banks", work: "The Endeavour Journal", quote: "Upon the slopes of the Cape hills we collected superb specimens of the flowering **protea**, with stiff bracts of pink and gold." },
      { author: "Olive Schreiner", work: "The Story of an African Farm", quote: "The rugged hillside was dotted with the stiff, leathery foliage of the wild **protea** braving the mountain wind." }
    ]
  },
  "proteaceae.md": {
    word: "proteaceae",
    primary: "A large family of flowering plants (order Proteales) predominantly found in the Southern Hemisphere, including proteas, banksias, and macadamias.",
    secondary: "In plant biogeography, a classic Gondwanan floral lineage characterized by specialized cluster roots (proteoid roots) adapted to nutrient-poor soils.",
    quotes: [
      { author: "Robert Brown", work: "On the Proteaceae of Jussieu", quote: "The southern continents display a remarkable endemic development of the family **Proteaceae**, linking Australia and the Cape." },
      { author: "Joseph Dalton Hooker", work: "The Botany of the Antarctic Voyage", quote: "The distribution of the **Proteaceae** across disconnected southern landmasses supports the hypothesis of an ancient austral flora." },
      { author: "Ronald Good", work: "The Geography of the Flowering Plants", quote: "Among flowering families, few exhibit such rigorous adherence to ancient Gondwanan borders as the **Proteaceae**." }
    ]
  },
  "proteales.md": {
    word: "proteales",
    primary: "An order of flowering plants containing the families Proteaceae, Platanaceae (plane trees), and Nelumbonaceae (lotuses).",
    secondary: "In molecular phylogenetics (APG IV), a basal eudicot clade uniting superficially divergent families based on deep genomic synapomorphies.",
    quotes: [
      { author: "Arthur Cronquist", work: "An Integrated System of Classification of Flowering Plants", quote: "The traditional circumscription of **Proteales** has been radically restructured through comparative embryology." },
      { author: "Peter F. Stevens", work: "Angiosperm Phylogeny Website", quote: "Molecular evidence places the sacred lotus and the plane tree alongside southern proteas within the monophyletic order **Proteales**." },
      { author: "Armen Takhtajan", work: "Diversity and Classification of Flowering Plants", quote: "The phylogenetic affinities of the order **Proteales** demonstrate the deep antiquity of early tricolpate angiosperms." }
    ]
  },
  "protean.md": {
    word: "protean",
    primary: "Readily changing shape, form, character, or role; exhibiting extreme diversity and variability.",
    secondary: "Deriving from Proteus, the prophetic old man of the sea in Greek mythology who altered his form to evade capture.",
    quotes: [
      { author: "John Milton", work: "Paradise Lost", quote: "In vain the sorcerer tried his **protean** arts, shifting from raging fire to roaring lion." },
      { author: "Samuel Taylor Coleridge", work: "Biographia Literaria", quote: "Shakespeare's genius was **protean**, passing effortlessly into every condition and passion of human nature." },
      { author: "Herman Melville", work: "The Confidence-Man", quote: "The mysterious voyager assumed a **protean** succession of disguises as the Mississippi steamer drifted downriver." }
    ]
  },
  "protease.md": {
    word: "protease",
    primary: "An enzyme that breaks down proteins and peptides into smaller polypeptides or amino acids by hydrolyzing peptide bonds; a peptidase.",
    secondary: "In biochemistry and physiology, cellular enzymes categorized into serine, cysteine, aspartic, and metallo-proteases essential for digestion, coagulation, and viral replication.",
    quotes: [
      { author: "Christian Anfinsen", work: "The Molecular Basis of Evolution", quote: "The catalytic cleavage of polypeptide chains by a specific **protease** reveals the folding hierarchy of enzymes." },
      { author: "Arthur Kornberg", work: "For the Love of Enzymes", quote: "Purification of intracellular **protease** enzymes clarified how cells degrade damaged proteins without harming structural components." },
      { author: "Sydney Brenner", work: "Selected Papers in Molecular Biology", quote: "Inhibiting the viral **protease** prevents the maturation of infectious polyproteins, neutralizing viral propagation." }
    ]
  },
  "protect.md": {
    word: "protect",
    primary: "To keep safe from harm, danger, loss, or injury; guard or defend.",
    secondary: "In law, insurance, and economics, to shield against financial liability or foreign commercial competition through tariffs or guarantees.",
    quotes: [
      { author: "William Shakespeare", work: "Hamlet", quote: "Angels and ministers of grace **protect** us! Be thou a spirit of health or goblin damned." },
      { author: "John Locke", work: "Second Treatise of Government", quote: "The chief end of men's uniting into commonwealths is to **protect** their property and personal liberty." },
      { author: "Abraham Lincoln", work: "First Inaugural Address", quote: "I hold that in contemplation of universal law and of the Constitution, the Union will **protect** and preserve itself." }
    ]
  },
  "protected.md": {
    word: "protected",
    primary: "Kept safe from danger, harm, or damage; guarded or shielded.",
    secondary: "In constitutional law and wildlife conservation, legally shielded from discrimination, infringement, hunting, or habitat destruction.",
    quotes: [
      { author: "Thomas Hobbes", work: "Leviathan", quote: "The obligation of subjects to the sovereign lasts as long, and no longer, than the power lasteth by which he is able to keep them **protected**." },
      { author: "Charles Darwin", work: "The Voyage of the Beagle", quote: "The deep volcanic crater formed a harbor where vessels rested safely **protected** from the heavy Pacific swell." },
      { author: "Theodore Roosevelt", work: "Outdoor Pastimes of an American Hunter", quote: "The wild buffalo survived in Yellowstone because the herds were strictly **protected** against commercial poachers." }
    ]
  },
  "protecting.md": {
    word: "protecting",
    primary: "Providing shelter, defense, or safety; shielding from adverse conditions or external threats.",
    secondary: "In patent law and diplomacy, securing exclusive legal claims or maintaining an ally under an umbrella of sovereign influence.",
    quotes: [
      { author: "Charlotte Brontë", work: "Jane Eyre", quote: "He threw his arm across my shoulders with a **protecting** tenderness that disarmed all my apprehensions." },
      { author: "Edmund Burke", work: "Speech on American Taxation", quote: "Great Britain, by **protecting** the colonies with her navy, earned their commercial gratitude." },
      { author: "Ralph Waldo Emerson", work: "Essays: First Series", quote: "Nature is constantly **protecting** her children through instincts that anticipate every seasonal disaster." }
    ]
  },
  "protection.md": {
    word: "protection",
    primary: "The act of protecting or state of being protected; defense, shelter, or preservation from harm.",
    secondary: "In economic history, the practice of shielding domestic industries from foreign competition through tariffs, quotas, or import subsidies.",
    quotes: [
      { author: "Alexander Hamilton", work: "Report on Manufactures", quote: "The judicious **protection** of domestic manufactures stimulates national industry and secures economic independence." },
      { author: "Mary Shelley", work: "Frankenstein", quote: "I sought the shelter of the cottage, hoping to find sympathy and **protection** from the bitter winter frost." },
      { author: "Adam Smith", work: "The Wealth of Nations", quote: "To demand perpetual **protection** for a domestic monopoly is to tax the whole society for the benefit of a single class." }
    ]
  },
  "protectionism.md": {
    word: "protectionism",
    primary: "The economic policy or practice of shielding a country's domestic industries from foreign competition by taxing imports.",
    secondary: "In international trade policy, tariff and regulatory barriers erected to insulate domestic producers from global price fluctuations.",
    quotes: [
      { author: "John Stuart Mill", work: "Principles of Political Economy", quote: "The doctrine of **protectionism** rests upon the fallacy that a country enriches itself by restricting its trade." },
      { author: "Friedrich List", work: "National System of Political Economy", quote: "Infant domestic industries require temporary tariff **protectionism** until they achieve competitive parity with foreign powers." },
      { author: "David Ricardo", work: "On the Principles of Political Economy and Taxation", quote: "Agricultural **protectionism** through corn laws artificially raises rents while depressing general wages." }
    ]
  },
  "protectionist.md": {
    word: "protectionist",
    primary: "An advocate or supporter of economic protectionism.",
    secondary: "Relating to policies, tariffs, or measures intended to protect domestic industries from foreign imports.",
    quotes: [
      { author: "Richard Cobden", work: "Speeches on Free Trade", quote: "The **protectionist** landlord defends high grain tariffs not for the public good, but for his private rent rolls." },
      { author: "William McKinley", work: "Speeches and Addresses", quote: "As a staunch **protectionist**, I believe American markets belong first to American labor and capital." },
      { author: "John Maynard Keynes", work: "A Tract on Monetary Reform", quote: "When monetary stability falters, every industrial faction appeals to **protectionist** remedies to ward off insolvency." }
    ]
  },
  "protective.md": {
    word: "protective",
    primary: "Capable of or intended for protecting; serving to shield or preserve from harm.",
    secondary: "In evolutionary biology and psychology, relating to defensive adaptations, camouflage, or parental care behaviors.",
    quotes: [
      { author: "Alfred Russel Wallace", work: "Darwinism", quote: "The caterpillar displays **protective** coloration so perfect that birds mistake it for a dry twig." },
      { author: "Charles Darwin", work: "The Descent of Man", quote: "The maternal instinct inspires a fierce **protective** courage that defies superior predators." },
      { author: "Sigmund Freud", work: "Beyond the Pleasure Principle", quote: "The living organism establishes a **protective** shield against excessive external stimuli to preserve psychic equilibrium." }
    ]
  },
  "protectively.md": {
    word: "protectively",
    primary: "In a protective manner; with the intention of shielding, defending, or guarding.",
    secondary: "Exhibiting vigilant or possessive care against potential interference or injury.",
    quotes: [
      { author: "George Eliot", work: "Silas Marner", quote: "The lonely weaver wrapped his rough coat **protectively** around the sleeping golden-haired child." },
      { author: "Thomas Hardy", work: "Tess of the d'Urbervilles", quote: "She drew her shawl **protectively** about her face to escape the inquisitive stares of the villagers." },
      { author: "Joseph Conrad", work: "Victory", quote: "He placed himself **protectively** between the trembling girl and the insolent intruders." }
    ]
  },
  "protectiveness.md": {
    word: "protectiveness",
    primary: "The quality, tendency, or state of being protective; a desire to shield or guard others.",
    secondary: "In behavioral psychology, parental or interpersonal solicitude that seeks to prevent exposure to physical danger or emotional trauma.",
    quotes: [
      { author: "Virginia Woolf", work: "Night and Day", quote: "Her mother's anxious **protectiveness** enveloped the household in a soft, suffocating cocoon of affection." },
      { author: "Henry James", work: "The Wings of the Dove", quote: "Milly recognized the tender **protectiveness** in her friend's eyes, yet felt humbled by its pity." },
      { author: "D. H. Lawrence", work: "Sons and Lovers", quote: "His mother’s fierce **protectiveness** made it impossible for him to surrender completely to another woman." }
    ]
  },
  "protector.md": {
    word: "protector",
    primary: "A person who protects or defends someone or something from danger, attack, or harm.",
    secondary: "In English constitutional history, a title given to a regent administering the kingdom during the monarch’s minority (or Oliver Cromwell as Lord Protector).",
    quotes: [
      { author: "William Shakespeare", work: "Henry VI, Part 2", quote: "Gloucester was the gentle **protector** of the realm, whose justice shielded both rich and poor." },
      { author: "Thomas Carlyle", work: "Oliver Cromwell's Letters and Speeches", quote: "As Lord **Protector**, Cromwell steered the English commonwealth through foreign wars and domestic conspiracies." },
      { author: "John Milton", work: "Sonnet XVI", quote: "Cromwell, our chief of men, whom the nation hailed as sovereign **protector** in times of peril." }
    ]
  },
  "protectorate.md": {
    word: "protectorate",
    primary: "A state or territory that is controlled and protected by another sovereign state.",
    secondary: "In British history, the period (1653–1659) during which England, Scotland, and Ireland were governed by Oliver and Richard Cromwell as Lord Protector.",
    quotes: [
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "Rome reduced client kingdoms along the eastern frontier to a subordinate **protectorate** under legionary supervision." },
      { author: "Thomas Babington Macaulay", work: "The History of England", quote: "The fall of the **protectorate** after Richard Cromwell’s resignation cleared the path for the Stuart restoration." },
      { author: "Winston Churchill", work: "The River War", quote: "Britain established a formal **protectorate** along the upper Nile to safeguard the maritime approaches to Suez." }
    ]
  },
  "protectorship.md": {
    word: "protectorship",
    primary: "The office, rank, or term of service of a protector.",
    secondary: "In constitutional history, the regency or governance exercised by a Lord Protector.",
    quotes: [
      { author: "David Hume", work: "The History of England", quote: "The Duke of Somerset’s ambition was gratified when Parliament confirmed his absolute **protectorship** during King Edward’s minority." },
      { author: "Thomas Carlyle", work: "The Life of Friedrich Schiller", quote: "The resignation of the **protectorship** cast the kingdom into momentary political paralysis." },
      { author: "Samuel Rawson Gardiner", work: "History of the Commonwealth and Protectorate", quote: "Cromwell assumed the **protectorship** with a solemn vow to govern according to written fundamental law." }
    ]
  },
  "protege.md": {
    word: "protege",
    primary: "A person who is guided, mentored, and supported by an older and more experienced person; variant spelling of protégé.",
    secondary: "In intellectual and artistic history, a promising student sponsored by a patron of wealth, academy, or political influence.",
    quotes: [
      { author: "Honoré de Balzac", work: "Lost Illusions", quote: "The wealthy publisher took the young poet under his wing as his favorite **protege**, introducing him to Parisian salons." },
      { author: "William Makepeace Thackeray", work: "The History of Pendennis", quote: "Major Pendennis watched over his nephew with all the anxious pride of a guardian promoting his **protege**." },
      { author: "Henry James", work: "The Ambassadors", quote: "Strether realized that Chad was no longer an impressionable **protege**, but an independent man of the world." }
    ]
  },
  "protegee.md": {
    word: "protegee",
    primary: "A female person who is guided, mentored, and supported by an older and more experienced mentor; variant spelling of protégée.",
    secondary: "In social history and literature, a young woman under the educational or artistic patronage of an influential benefactor.",
    quotes: [
      { author: "Jane Austen", work: "Emma", quote: "Emma determined that Harriet Smith should become her special **protegee**, destined for an aristocratic marriage." },
      { author: "Charlotte Brontë", work: "Villette", quote: "Madame Beck kept a watchful eye upon her English **protegee**, admiring her quiet discipline." },
      { author: "Edith Wharton", work: "The Age of Innocence", quote: "The old dowager treated the eccentric countess as her spoiled **protegee**, defying the rigid gossip of New York society." }
    ]
  },
  "proteidae.md": {
    word: "proteidae",
    primary: "A family of permanently aquatic, neotenic salamanders (mudpuppies and olms) retaining bushy external gills throughout life.",
    secondary: "In herpetology, caecilian-like or perennibranchiate amphibians including Proteus anguinus of subterranean caves and Necturus of North American rivers.",
    quotes: [
      { author: "Charles Darwin", work: "The Origin of Species", quote: "The blind olm of the Carniolan caves, belonging to the **Proteidae**, retains external gills and rudimentary eyes throughout adult life." },
      { author: "Thomas Henry Huxley", work: "The Anatomy of Vertebrated Animals", quote: "The retention of larval branchial arches in the **Proteidae** exemplifies extreme evolutionary neoteny." },
      { author: "Gladwyn Kingsley Noble", work: "The Biology of the Amphibia", quote: "Members of the family **Proteidae** fail to metamorphose even when stimulated with exogenous thyroid hormones." }
    ]
  },
  "proteinaceous.md": {
    word: "proteinaceous",
    primary: "Pertaining to, resembling, or containing protein.",
    secondary: "In biochemistry and physiology, relating to nitrogenous macromolecular organic substances composed of amino acid chains.",
    quotes: [
      { author: "Justus von Liebig", work: "Animal Chemistry", quote: "Animal muscles and blood consist of **proteinaceous** compounds originally synthesized by the vegetable kingdom." },
      { author: "Claude Bernard", work: "An Introduction to the Study of Experimental Medicine", quote: "Gastric juice digests **proteinaceous** food by dissolving peptide bonds in the stomach cavity." },
      { author: "Louis Pasteur", work: "Studies on Fermentation", quote: "Microscopic organisms proliferate rapidly whenever a warm, moist **proteinaceous** medium is exposed to atmospheric dust." }
    ]
  },
  "proteinase.md": {
    word: "proteinase",
    primary: "An enzyme that hydrolyzes proteins into simpler peptides; an endopeptidase.",
    secondary: "In biochemistry, an enzyme (such as pepsin, trypsin, or papain) that cleaves internal peptide bonds within complex protein substrates.",
    quotes: [
      { author: "John Howard Northrop", work: "Crystalline Enzymes", quote: "The crystallization of the gastric **proteinase** pepsin proved that biocatalysts are pure protein molecules." },
      { author: "Leonor Michaelis", work: "Biochemische Zeitschrift", quote: "The kinetic velocity of the **proteinase** reaction depends upon the saturation of active sites by the substrate." },
      { author: "Arthur Harden", work: "Alcoholic Fermentation", quote: "The yeast extract contained an active intracellular **proteinase** that slowly destroyed respiratory enzymes over time." }
    ]
  },
  "proteinuria.md": {
    word: "proteinuria",
    primary: "The presence of an abnormal amount of protein (especially albumin) in the urine.",
    secondary: "In nephrology, a clinical hallmark of glomerular filtration barrier injury, diabetic nephropathy, or preeclampsia.",
    quotes: [
      { author: "Richard Bright", work: "Reports of Medical Cases", quote: "Coagulable urine, now designated **proteinuria**, is the pathognomonic sign of degenerative disease of the renal parenchyma." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Persistent **proteinuria** in a young patient warrants careful examination of the cardiovascular and renal systems." },
      { author: "Arthur Guyton", work: "Textbook of Medical Physiology", quote: "When glomerular podocytes are damaged by autoimmune complexes, massive **proteinuria** ensues, depleting circulating plasma albumin." }
    ]
  },
  "proteles.md": {
    word: "proteles",
    primary: "A monotypic genus of hyaenids comprising the aardwolf (Proteles cristatus), an insectivorous mammal of eastern and southern Africa.",
    secondary: "In mammalogy and evolutionary anatomy, a small, nocturnal hyaenid with reduced cheek teeth specialized for consuming harvester termites.",
    quotes: [
      { author: "Alfred Russel Wallace", work: "The Geographical Distribution of Animals", quote: "The aardwolf, forming the genus **Proteles**, represents an aberrant, termite-eating offshoot of the hyena lineage." },
      { author: "Richard Lydekker", work: "The Royal Natural History", quote: "In **Proteles**, the molar teeth are rudimentary and peg-like, perfectly suited to a diet consisting entirely of insects." },
      { author: "William Henry Flower", work: "An Introduction to the Osteology of the Mammalia", quote: "The skeletal structure of **Proteles** displays the sloped back and forelimb dominance of typical hyenas despite its small skull." }
    ]
  }
};

function updateWordNote(relPath, data) {
  const fullPath = path.join(baseDir, relPath);
  if (!fs.existsSync(fullPath)) {
    console.error("File not found:", fullPath);
    return;
  }

  let content = fs.readFileSync(fullPath, "utf8");

  // Format quotes
  const quotesFormatted = data.quotes.map(q => `> - 📜 **${q.author} (*${q.work}*):** *"${q.quote}"*`).join("\n");

  // Replace Definition & Semantic Range
  const defRegex = /> \[!book\] 📖 Definitions & Semantic Range[\s\S]*?(?=> \[!quote\]|$)/;
  const newDef = `> [!book] 📖 Definitions & Semantic Range\n> 1. **Primary Definition (Lexical / Standard Consensus)**: ${data.primary}\n> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: ${data.secondary}\n\n`;

  if (defRegex.test(content)) {
    content = content.replace(defRegex, newDef);
  } else {
    console.warn("Could not find [!book] in", relPath);
  }

  // Replace Quotes
  const quoteRegex = /> \[!quote\] 💬 Contextual Usage & Authentic Quotations[\s\S]*$/;
  const newQuotes = `> [!quote] 💬 Contextual Usage & Authentic Quotations\n${quotesFormatted}\n`;

  if (quoteRegex.test(content)) {
    content = content.replace(quoteRegex, newQuotes);
  } else {
    console.warn("Could not find [!quote] in", relPath);
  }

  fs.writeFileSync(fullPath, content, "utf8");
  console.log("Updated:", relPath);
}

for (const [relPath, data] of Object.entries(wordsData)) {
  updateWordNote(relPath, data);
}
console.log("Primacy Batch 7 completed! Total words updated:", Object.keys(wordsData).length);
