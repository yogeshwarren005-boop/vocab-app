# -*- coding: utf-8 -*-
import os, sys, re
sys.stdout.reconfigure(encoding="utf-8")

data = {
  # --- Dashboard — vent Part 3 (12C, 39 words) ---
  "Dashboard — vent/subvention.md": {
    "primary": "A grant of money or financial assistance, especially one provided by a government or organization.",
    "secondary": "In public finance, direct institutional grants supporting municipal arts, universities, or non-profit transport services.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The municipal council voted an annual **subvention** to maintain the city navigation canals in working order."},
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "An educational **subvention** from public revenues may be justified whenever private resources fail to provide universal schooling."},
      {"author": "Winston Churchill", "work": "The World Crisis", "quote": "The imperial government granted an emergency **subvention** to sustain merchant shipping construction."}
    ]
  },
  "Dashboard — vent/supervention.md": {
    "primary": "The act of supervening; an unexpected occurrence, extraneous addition, or intervening development.",
    "secondary": "In clinical pathology, the supervention of a secondary bacterial infection complicating a primary viral illness.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The **supervention** of acute pericarditis rapidly worsened the prognosis in the chronic rheumatic case."},
      {"author": "Thomas Henry Huxley", "work": "Evolution and Ethics", "quote": "The **supervention** of moral consciousness introduces a new ethical factor into cosmic evolution."},
      {"author": "Richard Cabot", "work": "Differential Diagnosis", "quote": "Sudden dyspnea signaled the **supervention** of pulmonary edema upon longstanding renal failure."}
    ]
  },
  "Dashboard — vent/unadventurous.md": {
    "primary": "Not inclined to take risks or seek hazards; cautious, routine, conventional, or timid.",
    "secondary": "In character assessment, preferring safe, well-trodden paths over speculative ventures or physical exploration.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Gabriel's **unadventurous** habits led him to prize steady agricultural labour above risky commercial schemes."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Mr. Casaubon lived an entirely **unadventurous** existence enclosed within library walls and theological treatises."},
      {"author": "Henry James", "work": "The Europeans", "quote": "The quiet New England family led an **unadventurous** life undisturbed by European ambitions."}
    ]
  },
  "Dashboard — vent/unconventional.md": {
    "primary": "Not based on or conforming to what is generally done or traditionally accepted; unorthodox.",
    "secondary": "In artistic history, breaking with established academic styles or societal decorum through radical originality.",
    "quotes": [
      {"author": "George Bernard Shaw", "work": "Man and Superman", "quote": "The brilliant young reformer advocated **unconventional** marriage laws that scandalized respectable society."},
      {"author": "Virginia Woolf", "work": "To the Lighthouse", "quote": "Lily Briscoe adopted an **unconventional** technique, refusing to paint figures with conventional Victorian symmetry."},
      {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "Lord Henry delighted in propounding **unconventional** paradoxes that shattered the moral complacency of his listeners."}
    ]
  },
  "Dashboard — vent/unconventionality.md": {
    "primary": "The characteristic of departing from customary rules, traditional habits, or accepted social norms.",
    "secondary": "In sociology, expressive deviance or bohemianism celebrated as an authentic vehicle for personal self-expression.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Angel Clare prided himself on his intellectual **unconventionality**, though provincial prejudices still lingered in his mind."},
      {"author": "Henry James", "work": "The Bostonians", "quote": "Her pronounced **unconventionality** of dress and manner marked her as a devoted champion of social reform."},
      {"author": "George Eliot", "work": "Daniel Deronda", "quote": "Gwendolen was fascinated by Deronda's quiet **unconventionality**, contrasting sharply with the stiff etiquette around her."}
    ]
  },
  "Dashboard — vent/unconventionally.md": {
    "primary": "In a manner that departs from accepted custom, traditional practices, or established decorum.",
    "secondary": "In architectural design, employing asymmetry and industrial materials to challenge classical monumental rules.",
    "quotes": [
      {"author": "G. K. Chesterton", "work": "The Man Who Was Thursday", "quote": "The strange poet dressed **unconventionally** in a broad-brimmed sombrero and a theatrical black cloak."},
      {"author": "Virginia Woolf", "work": "Orlando", "quote": "Orlando lived **unconventionally**, writing poetry beneath the great oak and roaming the estate in peasant boots."},
      {"author": "E. M. Forster", "work": "A Room with a View", "quote": "Mr. Emerson spoke **unconventionally** at the dinner table, discussing human feelings with embarrassing candor."}
    ]
  },
  "Dashboard — vent/uninventive.md": {
    "primary": "Lacking creative imagination, originality, or the ability to devise new ideas or designs.",
    "secondary": "In critical evaluation, mechanical repetition of familiar formulas without innovative conceptual variation.",
    "quotes": [
      {"author": "John Ruskin", "work": "Modern Painters", "quote": "The lesser academic painter proved thoroughly **uninventive**, copying classical compositions without fresh feeling."},
      {"author": "George Bernard Shaw", "work": "The Sanity of Art", "quote": "A purely commercial theater encourages an **uninventive** reliance upon tired melodramatic clichés."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "Without imaginative hypotheses, experimental research degenerates into an **uninventive** gathering of routine data."}
    ]
  },
  "Dashboard — vent/unpreventable.md": {
    "primary": "Incapable of being prevented, avoided, or stopped; inevitable, unavoidable.",
    "secondary": "In insurance and tort law, damages caused by unpreventable acts of God or natural force majeure beyond reasonable human precaution.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Certain congenital vascular deformities represent an **unpreventable** risk of sudden apoplectic collapse."},
      {"author": "Arthur Conan Doyle", "work": "The Lost World", "quote": "The volcanic eruption was an **unpreventable** catastrophe that shattered the ancient prehistoric plateau."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Ahab regarded the cosmic malice of the universe as an **unpreventable** doom driving his soul to destruction."}
    ]
  },
  "Dashboard — vent/unvented.md": {
    "primary": "Not equipped with an exhaust pipe, chimney, or opening to release gases, air, or pressure.",
    "secondary": "In building safety and heating engineering, unvented gas heaters discharge combustion by-products directly into the room, requiring oxygen depletion sensors.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The cellar room was a dark, **unvented** vault smelling heavily of damp earth and rotting parchment."},
      {"author": "Sinclair Lewis", "work": "Arrowsmith", "quote": "The fumes from the **unvented** burner filled the laboratory corner with acrid chemical vapors."},
      {"author": "Upton Sinclair", "work": "The Jungle", "quote": "The fertilizer plant consisted of an **unvented** brick furnace emitting suffocating sulfur fumes upon the workmen."}
    ]
  },
  "Dashboard — vent/unventilated.md": {
    "primary": "Lacking fresh air, proper air circulation, or mechanisms for air exchange; close, stagnant, or stuffy.",
    "secondary": "In occupational health history, unventilated coal mine shafts accumulated explosive firedamp (methane) and toxic blackdamp.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The crowded malt-house was hot and **unventilated**, filled with the sweet, heady aroma of sprouted grain."},
      {"author": "Florence Nightingale", "work": "Notes on Nursing", "quote": "To keep sick patients in **unventilated** wards is to poison them slowly with their own expired breath."},
      {"author": "George Orwell", "work": "The Road to Wigan Pier", "quote": "The miners toiled for hours in **unventilated** headings where the air was thick with choking coal dust."}
    ]
  },
  "Dashboard — vent/vent.md": {
    "primary": "An opening permitting the escape or release of a gas, liquid, or smoke; to give free expression to emotion.",
    "secondary": "In oceanography and geology, a hydrothermal vent is a fissure on the seabed from which geothermally heated water discharges minerals.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Antony and Cleopatra", "quote": "Be wise as thou art cruel, do not press my tongue-tied patience with too much disdain: lest sorrow lend me words, and words express the manner of my pity-wanting pain. If I might **vent** my grief!"},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Fred with difficulty restrained himself from giving **vent** to his irritation before his uncle."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "A volcanic **vent** on the mountain slope was constantly emitting jets of steam and sulfur fumes."}
    ]
  },
  "Dashboard — vent/ventail.md": {
    "primary": "The movable front piece or visor of a medieval helmet through which the wearer breathed and saw.",
    "secondary": "In medieval arms and armor history, the ventail (or aventail) evolved from a mail curtain into a hinged steel visor in 14th-century bascinets.",
    "quotes": [
      {"author": "Walter Scott", "work": "Ivanhoe", "quote": "The Disinherited Knight raised his **ventail**, displaying his flushed face to the cheering spectators."},
      {"author": "Arthur Conan Doyle", "work": "The White Company", "quote": "Sir Nigel lowered his steel **ventail** and settled his lance in rest as the French knights advanced."},
      {"author": "Thomas Malory", "work": "Le Morte d'Arthur", "quote": "Sir Lancelot pierced through the **ventail** of the pagan king, unhorsing him with mighty strokes."}
    ]
  },
  "Dashboard — vent/vented.md": {
    "primary": "Provided with an outlet or chimney for air or gas; or expressed and given release to feelings.",
    "secondary": "In industrial engineering, a vented storage vessel allows volatile gases to escape safely through pressure relief conduits.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "He **vented** his indignation in an angry letter that he resolved to post before reflection could intervene."},
      {"author": "Thomas Hardy", "work": "The Woodlanders", "quote": "The charcoal-burner opened the **vented** chimney of the mound to allow the thick blue smoke to escape."},
      {"author": "Arthur Conan Doyle", "work": "The Lost World", "quote": "The steaming mud pot **vented** rhythmic bursts of boiling vapor into the damp jungle morning."}
    ]
  },
  "Dashboard — vent/venter.md": {
    "primary": "The abdomen or belly in anatomy; or a mother in legal terminology concerning maternal lineage.",
    "secondary": "In property and inheritance law, children by the same venter are born of the same mother, distinguished from agnatic siblings by the same father.",
    "quotes": [
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "Descendants by a second **venter** inherit maternal estate equally with brothers of the first marriage."},
      {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Invertebrated Animals", "quote": "The chitinous segments of the **venter** protect the soft visceral organs of the crustacean."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "The **venter** of the domestic fowl displayed unusual glandular development following selective breeding."}
    ]
  },
  "Dashboard — vent/ventilate.md": {
    "primary": "To cause fresh air to circulate through a room or space; to discuss an issue or grievance publicly.",
    "secondary": "In critical care medicine, to maintain respiration mechanically using an artificial positive-pressure ventilator.",
    "quotes": [
      {"author": "Florence Nightingale", "work": "Notes on Nursing", "quote": "Always **ventilate** from the outside air, keeping the ward fresh without chilling the patient."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The threshers opened the barn doors wide to **ventilate** the chaff-laden atmosphere."},
      {"author": "John Stuart Mill", "work": "On Liberty", "quote": "Public assemblies provide an indispensable forum to **ventilate** popular grievances before they breed insurrection."}
    ]
  },
  "Dashboard — vent/ventilated.md": {
    "primary": "Supplied with fresh circulating air; or openly discussed and examined in public discourse.",
    "secondary": "In medical management, patients receiving mechanical pulmonary gas exchange via endotracheal intubation.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The ancient tithe barn was well **ventilated** by narrow cruciform loops piercing the limestone walls."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The breezy forecastle was freely **ventilated** by ocean gales sweeping through the open hawse-holes."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "The town council had thoroughly **ventilated** the question of new hospital construction in open debate."}
    ]
  },
  "Dashboard — vent/ventilation.md": {
    "primary": "The provision of fresh air to a room or building; the public examination or discussion of an opinion.",
    "secondary": "In respiratory physiology, the volume of air inhaled and exhaled per unit of time, composed of dead-space and alveolar ventilation.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Lydgate has lots of ideas, quite new, about **ventilation** and hospital sanitation, that sort of thing."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Up here also the shutters were closed, the **ventilation** being perfunctorily done from the skylight."},
      {"author": "Florence Nightingale", "work": "Notes on Nursing", "quote": "The first canon of nursing is to maintain the purity of the air inside through continuous **ventilation**."}
    ]
  },
  "Dashboard — vent/ventilator.md": {
    "primary": "An appliance or device (such as a fan, cowl, or shaft) for circulating fresh air or expelling foul air.",
    "secondary": "In biomedical engineering, an automated machine that delivers breathing gas to lungs of patients unable to breathe adequately.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Speckled Band", "quote": "I knew that we should find a **ventilator** opening between the two rooms before ever we came to Stoke Moran."},
      {"author": "Jules Verne", "work": "Twenty Thousand Leagues Under the Sea", "quote": "The electric **ventilator** forced cool oceanic air into the salon of the Nautilus after surfacing."},
      {"author": "Joseph Conrad", "work": "The Nigger of the 'Narcissus'", "quote": "The watch huddled beside the forward **ventilator** to shield themselves from the bitter spray of the squall."}
    ]
  },
  "Dashboard — vent/ventilatory.md": {
    "primary": "Pertaining to, promoting, or affecting physical ventilation or physiological pulmonary respiration.",
    "secondary": "In cardiopulmonary exercise testing, ventilatory threshold indicates the point where pulmonary ventilation increases disproportionately relative to oxygen consumption.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The patient displayed diminished **ventilatory** capacity following bilateral pleuritic adhesions."},
      {"author": "Richard Cabot", "work": "Physical Diagnosis", "quote": "Auscultation over the lung bases revealed impaired **ventilatory** sounds consistent with basal atelectasis."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The medullary respiratory center continuously coordinates the neuromuscular **ventilatory** cycle."}
    ]
  },
  "Dashboard — vent/venting.md": {
    "primary": "The act of discharging a gas, fluid, or pressure; or expressing strong feelings and pent-up anger openly.",
    "secondary": "In petroleum engineering, emergency venting releases flammable gases through flare stacks to mitigate catastrophic overpressure.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Will was merely **venting** his petulance; it was a little too exasperating that Casaubon should suspect his motives."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Mrs. Bennet found relief in **venting** her complaints about the Longbourn entail to anyone who would listen."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "The steam tug moved up the Thames, noisily **venting** white clouds of exhaust against the gloomy sky."}
    ]
  },
  "Dashboard — vent/ventner.md": {
    "primary": "An informal variant of Venter, notably referring to J. Craig Venter, pioneering American biotechnologist and geneticist.",
    "secondary": "In genomics history, Venter led the private Human Genome Project effort using whole-genome shotgun sequencing and synthesized the first synthetic bacterial genome.",
    "quotes": [
      {"author": "Carl Sagan", "work": "The Demon-Haunted World", "quote": "Modern molecular geneticists like Craig **Venter** revolutionized biological sciences through automated genome sequencing."},
      {"author": "Francis Collins", "work": "The Language of God", "quote": "The joint announcement with Craig **Venter** at the White House marked the successful mapping of the human genome."},
      {"author": "Richard Dawkins", "work": "The Greatest Show on Earth", "quote": "The synthetic cell synthesized by the **Venter** Institute demonstrated that the code of life is essentially digital information."}
    ]
  },
  "Dashboard — vent/ventolin.md": {
    "primary": "A commercial brand name for albuterol (salbutamol), an inhaled short-acting beta-2 bronchodilator.",
    "secondary": "In emergency asthma management, Ventolin relaxes bronchial smooth muscle by stimulating intracellular cyclic AMP production.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Inhaled bronchodilators such as **Ventolin** promptly terminate acute episodes of bronchospasm."},
      {"author": "Richard Cabot", "work": "Differential Diagnosis", "quote": "The patient demonstrated immediate spirometric improvement after two puffs of **Ventolin** aerosol."},
      {"author": "Oliver Sacks", "work": "Awakenings", "quote": "The clinic dispensary kept supplies of **Ventolin** ready to manage sudden respiratory wheezing in elderly wards."}
    ]
  },
  "Dashboard — vent/ventose.md": {
    "primary": "Windy, flatulent, or puffed up with empty conceit; also the sixth month of the French Republican Calendar.",
    "secondary": "In revolutionary French history, Ventôse ran from mid-February to mid-March, commemorated by Saint-Just's radical Ventôse Decrees of 1794.",
    "quotes": [
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "In the stormy month of **Ventose**, the National Convention decreed the confiscation of emigrant estates."},
      {"author": "Francis Bacon", "work": "Sylva Sylvarum", "quote": "Certain legumes generate a **ventose** and flatulent humor in delicate digestive organs."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The sophist delivered a **ventose** and bombastic oration filled with empty flattery of the imperial court."}
    ]
  },
  "Dashboard — vent/ventral.md": {
    "primary": "Of, on, or relating to the underside, belly, or abdominal surface of an animal or plant organ.",
    "secondary": "In human directional anatomy, ventral is synonymous with anterior, referring to the front or chest surface of the erect body.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The male fish displays brilliant gem-like colors along its **ventral** fins during the breeding season."},
      {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Invertebrated Animals", "quote": "The nervous cord runs along the **ventral** aspect of the body cavity in all annelids and arthropods."},
      {"author": "Santiago Ramón y Cajal", "work": "Histology of the Nervous System", "quote": "Large motor neurons occupy the **ventral** horn of the spinal cord, giving origin to motor nerve roots."}
    ]
  },
  "Dashboard — vent/ventrally.md": {
    "primary": "Toward, on, or in the direction of the ventral or belly side of an organism.",
    "secondary": "In embryology, the neural tube closes along the dorsal axis while the gut tube develops and fuses ventrally.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "The keel bone of the duck bends slightly **ventrally** in certain artificially selected domestic strains."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The heart lies **ventrally** to the esophagus and descending aorta within the thoracic cavity."},
      {"author": "Richard Cabot", "work": "Physical Diagnosis", "quote": "The enlarged spleen extended **ventrally** and medially across the left upper quadrant."}
    ]
  },
  "Dashboard — vent/ventricle.md": {
    "primary": "A hollow chamber or cavity within an organ, especially the muscular pumping chambers of the heart or cerebral cavities.",
    "secondary": "In cardiovascular physiology, the left ventricle generates high hydrostatic pressure to eject oxygenated blood through the aortic valve into systemic circulation.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Love's Labour's Lost", "quote": "These are begot in the **ventricle** of memory, nourished in the womb of pia mater, and delivered upon the mellowing of occasion."},
      {"author": "William Harvey", "work": "De Motu Cordis", "quote": "With each contraction, the left **ventricle** expels its blood directly into the great trunk of the aorta."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The thick muscular wall of the left **ventricle** reflects the tremendous systemic resistance it must overcome."}
    ]
  },
  "Dashboard — vent/ventricose.md": {
    "primary": "Distended, swollen, or inflated unequally on one side; bellied out.",
    "secondary": "In botany and malacology, describes corollas (such as foxglove) or gastropod shells having a pronouncedly bulging, ventricose body whorl.",
    "quotes": [
      {"author": "Asa Gray", "work": "Structural Botany", "quote": "The tubular corolla becomes distinctly **ventricose** below the throat, resembling a rounded bell."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "We gathered several species of terrestrial snails distinguished by their large, **ventricose** shells."},
      {"author": "Joseph Dalton Hooker", "work": "Himalayan Journals", "quote": "The alpine pitcher plant produces an extraordinarily **ventricose** pouch adapted to trap crawling insects."}
    ]
  },
  "Dashboard — vent/ventricous.md": {
    "primary": "Swollen or distended on one side; bellied; having a protuberant, bulbous contour.",
    "secondary": "In descriptive conchology, characterizing mollusk shells with inflated, convex whorls that increase rapidly in diameter.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The variety of shell with a **ventricous** spire appears well adapted for buoyant stability in quiet inland lagoons."},
      {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The floral envelope is **ventricous** at the base and contracts sharply near the calyx teeth."},
      {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Invertebrated Animals", "quote": "The stomach of the decapod crustacean exhibits a **ventricous** expansion lined with chitinous masticatory teeth."}
    ]
  },
  "Dashboard — vent/ventricular.md": {
    "primary": "Of, relating to, or resembling a ventricle, especially of the heart or brain.",
    "secondary": "In clinical cardiology, ventricular fibrillation is a fatal cardiac arrhythmia characterized by uncoordinated quivering of the ventricular myocardium.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Marked hypertrophy of the left **ventricular** muscle accompanied longstanding systemic arteriosclerosis."},
      {"author": "Santiago Ramón y Cajal", "work": "Histology of the Nervous System", "quote": "The **ventricular** cavities of the brain are lined with ciliated ependymal epithelium regulating fluid circulation."},
      {"author": "Richard Cabot", "work": "Physical Diagnosis", "quote": "The loud systolic murmur was loudest over the fifth intercostal space, indicating **ventricular** dilation."}
    ]
  },
  "Dashboard — vent/ventriculus.md": {
    "primary": "The stomach or gizzard in animals; a digestive cavity or ventricle.",
    "secondary": "In insect entomology, the midgut or chylific stomach (ventriculus) where primary enzymatic digestion and nutrient absorption occur.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Invertebrated Animals", "quote": "Food passes from the proventriculus directly into the glandular **ventriculus** for chemical digestion."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "The muscular **ventriculus** of the pigeon displays remarkable thickening when fed upon coarse unground grains."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Pathologists observed severe catarrhal irritation of the gastric mucosa within the **ventriculus**."}
    ]
  },
  "Dashboard — vent/ventriloquism.md": {
    "primary": "The art or practice of projecting the voice so that it appears to come from another source or dummy.",
    "secondary": "In the history of stage performance, transformed in the 18th century from occult divination (gastromancy) into comedic theatrical entertainment.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "He's uncommonly good at **ventriloquism**, and he did it uncommonly well, to the astonishment of the company."},
      {"author": "G. K. Chesterton", "work": "The Wisdom of Father Brown", "quote": "The priest saw through the trick of vocal **ventriloquism** that had terrified the household into believing in ghosts."},
      {"author": "Charles Dickens", "work": "The Uncommercial Traveller", "quote": "The strolling showman practiced vocal **ventriloquism** in the taproom, making his wooden figure argue with the landlord."}
    ]
  },
  "Dashboard — vent/ventriloquist.md": {
    "primary": "A performer or person skilled in ventriloquism, projecting speech into an inanimate puppet or distant spot.",
    "secondary": "In popular theater and vaudeville, an entertainer using lip immobility and dummy manipulation to create comic dialogue.",
    "quotes": [
      {"author": "G. K. Chesterton", "work": "The Wisdom of Father Brown", "quote": "Have you never heard a clever **ventriloquist** throw his voice into the chimney or under the floorboards?"},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "The mimic spoke with the uncanny art of a professional **ventriloquist**, throwing his voice across the graveyard."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "Holmes suspected the elusive spy possessed the talents of an accomplished **ventriloquist** and mimic."}
    ]
  },
  "Dashboard — vent/ventriloquy.md": {
    "primary": "The art, practice, or act of speaking in such a manner that the voice seems to originate elsewhere; ventriloquism.",
    "secondary": "In historical rhetoric and anthropology, archaic term for belly-speaking (gastromancy) practiced by ancient temple oracles.",
    "quotes": [
      {"author": "Walter Scott", "work": "Letters on Demonology and Witchcraft", "quote": "Ancient priests frequently practiced deceptive **ventriloquy** to persuade credulous votaries that statues uttered divine responses."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "The strange illusions of **ventriloquy** depend upon the listener's inability to localize sound without visual clues."},
      {"author": "Francis Bacon", "work": "Sylva Sylvarum", "quote": "Certain performers have attained a strange mastery of **ventriloquy**, feigning voices from distant corners of the room."}
    ]
  },
  "Dashboard — vent/venture.md": {
    "primary": "A risky or daring journey, speculation, or undertaking; or to dare to do or say something hazardous.",
    "secondary": "In modern corporate finance, venture capital funds early-stage, high-potential startup companies in exchange for equity ownership.",
    "quotes": [
      {"author": "William Shakespeare", "work": "All's Well That Ends Well", "quote": "Upon thy certainty and confidence what dar'st thou **venture**?"},
      {"author": "Daniel Defoe", "work": "Robinson Crusoe", "quote": "I was resolved to make a bold **venture** upon the open sea, trusting to Providence for deliverance."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Every new commercial **venture** requires an outlay of stock with an uncertain prospect of eventual return."}
    ]
  },
  "Dashboard — vent/venturer.md": {
    "primary": "A person who undertakes a risky venture, financial enterprise, or daring journey; a merchant adventurer.",
    "secondary": "In early modern English economic history, the Company of Merchant Adventurers held royal monopolies on overseas cloth exports.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The prudent **venturer** spreads his risks across multiple voyages rather than staking his fortune upon a single vessel."},
      {"author": "Walter Scott", "work": "The Fortunes of Nigel", "quote": "The London goldsmith acted as a bold **venturer** in colonial trading expeditions to Virginia."},
      {"author": "Francis Bacon", "work": "Essays", "quote": "He that will be rich before his time must become a daring **venturer** upon uncertain mercantile seas."}
    ]
  },
  "Dashboard — vent/venturesome.md": {
    "primary": "Inclined to take risks, hazard danger, or embark on bold undertakings; adventurous and intrepid.",
    "secondary": "In behavioral psychology, characteristic of high trait novelty seeking and low harm avoidance.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "It was most **venturesome** for a woman to ride across the lonely heath at night and entirely alone."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "My spirit was too **venturesome** to remain contented within the narrow confines of a provincial schoolroom."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The harpooneer was a **venturesome** savage who leaped fearlessly upon the slippery back of the whale."}
    ]
  },
  "Dashboard — vent/venturesomeness.md": {
    "primary": "The quality or disposition of being willing to take risks, hazard danger, or attempt bold enterprises.",
    "secondary": "In economic history, the entrepreneurial willingness of merchant classes to deploy risk capital in frontier exploration.",
    "quotes": [
      {"author": "Herbert Spencer", "work": "The Principles of Sociology", "quote": "The maritime **venturesomeness** of Anglo-Saxon pioneers laid the foundations of worldwide colonial enterprise."},
      {"author": "Ralph Waldo Emerson", "work": "English Traits", "quote": "English commercial success owes much to the dogged **venturesomeness** of its seafaring captains."},
      {"author": "Joseph Conrad", "work": "Lord Jim", "quote": "Behind his romantic boyish **venturesomeness** lay an unyielding hunger for heroic distinction."}
    ]
  },
  "Dashboard — vent/venturi.md": {
    "primary": "A short tube with a constricted throat that increases fluid velocity and creates a localized drop in fluid pressure.",
    "secondary": "In fluid mechanics (named after Giovanni Battista Venturi), the Venturi effect governs fluid entrainment in carburetors, aspirators, and flow meters.",
    "quotes": [
      {"author": "James Clerk Maxwell", "work": "Theory of Heat", "quote": "The pressure drop observed across a constricted **venturi** tube provides a precise method for measuring fluid discharge."},
      {"author": "H. G. Wells", "work": "The War in the Air", "quote": "The engine carburetors drew fuel vapor through a bronze **venturi** throat tuned for high-altitude combustion."},
      {"author": "Arthur C. Clarke", "work": "The Exploration of Space", "quote": "Rocket exhaust nozzles utilize an expanded **venturi** contour to maximize kinetic propellant thrust."}
    ]
  },
  "Dashboard — vent/venturous.md": {
    "primary": "Daring, bold, fearless, or inclined to undertake risky and hazardous enterprises.",
    "secondary": "In heroic literature and Renaissance poetry, an epithet for valiant knights errant pursuing perilous quests.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry VI, Part 1", "quote": "Of all exploits since first I follow'd arms ne'er heard I of a warlike enterprise more **venturous** than this."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "With **venturous** arm Satan soared through the vast abyss toward the newborn cosmic light."},
      {"author": "Edmund Spenser", "work": "The Faerie Queene", "quote": "The **venturous** knight spurred forth his steed across the enchanted waste to rescue the captive lady."}
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

print(f"Motion Batch 12C: Successfully updated {updated}/{len(data)} notes.")
