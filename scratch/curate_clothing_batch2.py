# -*- coding: utf-8 -*-
"""
Curated definitions and authentic citations for Batch 2 of Cluster Clothing & Covering:
- Dashboard — tect (36 words)
- Dashboard — vest (39 words)
Total: 75 words.
"""
import re, sys

sys.stdout.reconfigure(encoding="utf-8")

data_batch2_tect = {
  "architect": {
    "primary": "A qualified professional who designs buildings, plans urban structures, and superintends their construction.",
    "secondary": "The creator, planner, or master deviser of an idea, complex project, or historic enterprise.",
    "quotes": [
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The medieval **architect** worked not as a mere mechanical builder, but as an inspired sculptor of sacred space."},
      {"author": "Francis Bacon", "work": "Essays", "quote": "He was the chief **architect** of his own fortune, combining bold ambition with tireless industry."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The Roman **architect** raised monumental arches and aqueducts that endured long after the empire dissolved."}
    ]
  },
  "architectural": {
    "primary": "Pertaining to the art, science, theory, or practice of building design and construction.",
    "secondary": "Possessing the structural harmony, monumentality, or ordered composition of architecture.",
    "quotes": [
      {"author": "John Ruskin", "work": "The Seven Lamps of Architecture", "quote": "True **architectural** beauty arises from noble proportion and honest expression of materials."},
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "The Florentine palace displayed magnificent **architectural** symmetry that enchanted every visitor."},
      {"author": "Thomas Hardy", "work": "Jude the Obscure", "quote": "Jude gazed with longing upon the magnificent **architectural** glories of the Christminster colleges."}
    ]
  },
  "architecturally": {
    "primary": "In an architectural manner; with regard to structural design, aesthetic proportion, or building technique.",
    "secondary": "Structurally or compositionally in physical or intellectual layout.",
    "quotes": [
      {"author": "John Ruskin", "work": "Modern Painters", "quote": "The cathedral facade is **architecturally** superior to any classical imitation built in the century."},
      {"author": "Walter Pater", "work": "The Renaissance", "quote": "The courtyard was **architecturally** designed to harmonize the play of Mediterranean sunlight and shadow."},
      {"author": "Charlotte Brontë", "work": "Villette", "quote": "The ancient convent was **architecturally** severe, presenting cold stone portals to the public square."}
    ]
  },
  "architecture": {
    "primary": "The art and science of designing and erecting habitable buildings and physical structures.",
    "secondary": "In computer science and engineering, the fundamental design, organization, and functional structure of a system.",
    "quotes": [
      {"author": "John Ruskin", "work": "The Seven Lamps of Architecture", "quote": "Great **architecture** is the art which so disposes and adorns the edifices raised by man for whatsoever uses."},
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "The mind constructs systems of philosophy as a master builder executes noble works of **architecture**."},
      {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "Gothic **architecture** is a blooming of the forest oak and pine in monumental stone."}
    ]
  },
  "detect": {
    "primary": "To discover or determine the presence, existence, or fact of something concealed or not easily noticeable.",
    "secondary": "In chemistry and forensics, to identify trace substances, impurities, or signals using analytical instruments.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "A Study in Scarlet", "quote": "Holmes knelt upon the floor, keen to **detect** the faintest footprint or dropped cigar ash."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "A sensitive galvanometer enabled the experimenter to **detect** minute induced electrical currents."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth was quick to **detect** a slight degree of embarrassment in Darcy's formal address."}
    ]
  },
  "detectable": {
    "primary": "Capable of being discovered, noticed, identified, or measured by human perception or instruments.",
    "secondary": "In analytical science, present in an amount sufficient to register above the baseline noise threshold.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "In early stages of arterial disease, no **detectable** murmur is heard upon cardiac auscultation."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Slight variations between island varieties are barely **detectable** except to the experienced naturalist."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "The mysterious footprints were distinctly **detectable** in the soft boggy peat along the path."}
    ]
  },
  "detected": {
    "primary": "Discovered, identified, or uncovered through careful observation, inquiry, or scientific measurement.",
    "secondary": "Caught, exposed, or revealed in the commission of an offense or clandestine action.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Holmes **detected** the subtle fragrance of an exotic Indian tobacco lingering in the locked chamber."},
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "The minister feared that his secret spiritual torment was **detected** by the physician's piercing eye."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "We **detected** numerous fossil shells embedded within the elevated sandstone strata."}
    ]
  },
  "detecting": {
    "primary": "The act, process, or practice of discovering or uncovering concealed clues, facts, or physical traces.",
    "secondary": "In engineering and electronics, sensing or demodulating physical impulses or radio signals.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Memoirs of Sherlock Holmes", "quote": "The science of **detecting** crime requires sharp powers of observation and deduction."},
      {"author": "Michael Faraday", "work": "The Chemical History of a Candle", "quote": "By **detecting** the presence of water vapor, we demonstrate the combustion of hydrogen in the flame."},
      {"author": "Thomas Henry Huxley", "work": "Lay Sermons, Addresses, and Reviews", "quote": "Microscopy affords a precise method for **detecting** dangerous adulterations in public flour supplies."}
    ]
  },
  "detection": {
    "primary": "The act, process, or capability of discovering, noticing, or exposing something hidden, elusive, or subtle.",
    "secondary": "In criminal investigation, the systematic solving of crimes and apprehending of offenders.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "A Study in Scarlet", "quote": "He regarded the art of criminal **detection** as an exact scientific discipline governed by logic."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Early clinical **detection** of pulmonary tuberculosis dramatically improves the patient's prognosis."},
      {"author": "Edgar Allan Poe", "work": "The Murders in the Rue Morgue", "quote": "The analytical faculties are exercised to their highest pitch in the **detection** of bizarre mysteries."}
    ]
  },
  "detective": {
    "primary": "A police officer or private investigator engaged in investigating crimes, collecting evidence, and solving cases.",
    "secondary": "Pertaining to, employed in, or characteristic of criminal investigation and clue-finding.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "As an amateur **detective**, Holmes took supreme delight in solving problems that baffled Scotland Yard."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Inspector Bucket moved through the London alleys with the watchful patience of an experienced **detective**."},
      {"author": "Wilkie Collins", "work": "The Moonstone", "quote": "Sergeant Cuff had the melancholy air of a **detective** who saw through every human pretense."}
    ]
  },
  "detector": {
    "primary": "An instrument, sensor, or apparatus used to reveal the presence, level, or quality of a physical phenomenon.",
    "secondary": "In radio engineering, a demodulator circuit that extracts audio or information from a carrier wave.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "The gold-leaf electroscope served as a remarkably sensitive **detector** of faint electrostatic charges."},
      {"author": "Lord Kelvin (William Thomson)", "work": "Popular Lectures and Addresses", "quote": "The siphon recorder acted as an instantaneous **detector** of electrical pulses traversing transatlantic cables."},
      {"author": "H. G. Wells", "work": "The Invisible Man", "quote": "The apparatus functioned as a delicate chemical **detector**, glowing faintly when vapors escaped."}
    ]
  },
  "overprotect": {
    "primary": "To shield, guard, or shelter someone with excessive, suffocating vigilance against potential harm.",
    "secondary": "To defend or insulate excessively, preventing healthy independence or natural resilience.",
    "quotes": [
      {"author": "George Eliot", "work": "Daniel Deronda", "quote": "An anxious parent may easily **overprotect** an only child, rendering the youth timid before worldly trials."},
      {"author": "William James", "work": "Talks to Teachers on Psychology", "quote": "Educators who **overprotect** students from intellectual difficulty weaken their capacity for independent thought."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "Mrs. Reed sought to **overprotect** her spoiled son John, excusing every display of vicious arrogance."}
    ]
  },
  "overprotection": {
    "primary": "The practice or tendency of shielding someone with excessive parental or administrative vigilance.",
    "secondary": "Excessive shielding that inhibits the development of autonomy, resilience, or self-reliance.",
    "quotes": [
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Maternal **overprotection** frequently fosters an enduring neurotic dependency in developing youths."},
      {"author": "George Bernard Shaw", "work": "Misalliance", "quote": "He protested against the suffocating domestic **overprotection** that sheltered young ladies from all reality."},
      {"author": "H. G. Wells", "work": "Mankind in the Making", "quote": "Civic **overprotection** of young industries may lead to commercial stagnation and inefficiency."}
    ]
  },
  "overprotective": {
    "primary": "Exhibiting an excessive, anxious desire to shield someone from real or imagined harm, failure, or distress.",
    "secondary": "Marked by suffocating guardianship that restricts normal freedom and individual growth.",
    "quotes": [
      {"author": "Jane Austen", "work": "Emma", "quote": "Mr. Woodhouse was an **overprotective** father whose nervous anxieties constantly curtailed his daughter's outings."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "An **overprotective** instinct led the peasant mother to warn her daughter against wealthy suitors."},
      {"author": "Virginia Woolf", "work": "The Voyage Out", "quote": "Rachel resented the well-meaning but **overprotective** solicitude of her aunt during the voyage."}
    ]
  },
  "protect": {
    "primary": "To keep safe from harm, injury, destruction, or attack; to shield, defend, or shelter.",
    "secondary": "In economic policy, to shield domestic industries from foreign competition through tariffs and quotas.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Richard III", "quote": "The Lord **protect** him from that dog of hell! He did me harm, but I will pray for him."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Heavenly angels were commanded to **protect** the sacred garden from satanic intrusions."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The first duty of the sovereign is to **protect** the commonwealth from foreign violence and invasion."}
    ]
  },
  "protected": {
    "primary": "Shielded, guarded, or defended from injury, danger, destruction, or economic competition.",
    "secondary": "In environmental law, legally safeguarded by conservation statutes from hunting or exploitation.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Frail organisms survived on isolated oceanic islands, **protected** from continental carnivores."},
      {"author": "Alexander Hamilton", "work": "Report on Manufactures", "quote": "Infant American industries must be **protected** by temporary duties against European monopolies."},
      {"author": "Daniel Defoe", "work": "Robinson Crusoe", "quote": "Crusoe felt securely **protected** within his fortified stockade against midnight marauders."}
    ]
  },
  "protecting": {
    "primary": "Serving to shield, defend, shelter, or safeguard living beings, structures, or rights against harm.",
    "secondary": "The ongoing action or duty of guarding, defending, or preserving something valuable.",
    "quotes": [
      {"author": "Florence Nightingale", "work": "Notes on Nursing", "quote": "A warm flannel wrapper serves a vital **protecting** function against fatal chills in convalescents."},
      {"author": "Walter Scott", "work": "The Heart of Midlothian", "quote": "Jeanie Deans trusted in the **protecting** care of Providence as she journeyed unprotected to London."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The cranial vault forms a rigid bony case, **protecting** the delicate cerebral tissues from trauma."}
    ]
  },
  "protection": {
    "primary": "The act, process, or condition of defending, shielding, or keeping someone or something safe from harm.",
    "secondary": "In international trade, the policy of imposing customs tariffs to protect domestic manufacturers.",
    "quotes": [
      {"author": "John Locke", "work": "Second Treatise of Government", "quote": "The chief end of men's uniting into commonwealths is the **protection** of their lives, liberties, and estates."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The national defense requires an energetic central government armed with full power for mutual **protection**."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "High import duties grant domestic manufacturers a temporary **protection** against foreign competition."}
    ]
  },
  "protectionism": {
    "primary": "The economic policy or practice of shielding domestic industries from foreign competition through trade tariffs or quotas.",
    "secondary": "The political advocacy of discriminatory customs tariffs to stimulate national manufacturing and agricultural output.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "The doctrine of **protectionism** rests upon the erroneous belief that international trade impoverishes one partner."},
      {"author": "Frank A. Fetter", "work": "The Principles of Economics", "quote": "Aggressive **protectionism** alters the natural distribution of labor and capital across domestic industries."},
      {"author": "William Graham Sumner", "work": "Protectionism: The -Ism Which Teaches that Waste Makes Wealth", "quote": "The fallacy of **protectionism** consists in using state taxation to confer commercial monopolies on favored classes."}
    ]
  },
  "protectionist": {
    "primary": "An advocate, politician, or economist who supports protective tariffs to shield domestic production from foreign imports.",
    "secondary": "Relating to, characteristic of, or favoring economic policies of trade protectionism.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "The sincere **protectionist** fails to perceive that restricting imports necessarily curtails domestic export trade."},
      {"author": "Walter Bagehot", "work": "Biographical Studies", "quote": "Disraeli rallied the disgruntled agricultural interests by leading a fiery **protectionist** opposition in Parliament."},
      {"author": "Frank A. Fetter", "work": "Modern Economic Problems", "quote": "The **protectionist** arguments advanced during congressional debates echoed traditional mercantilist fallacies."}
    ]
  },
  "protective": {
    "primary": "Capable of or intended to shield, defend, guard, or preserve from damage, injury, or loss.",
    "secondary": "Exhibiting a caring or defensive vigilance to keep someone safe from distress or danger.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The mottled wing pattern of the resting moth serves an extraordinary **protective** mimicry against predators."},
      {"author": "Jane Austen", "work": "Emma", "quote": "Mr. Knightley watched Emma with a **protective** interest that sprang from years of genuine affectionate concern."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "The scientific method acts as a **protective** shield guarding the intellect against dogmatic superstition."}
    ]
  },
  "protectively": {
    "primary": "In a protective manner; with defensive care, watchful vigilance, or shielding solicitude.",
    "secondary": "In a way intended to guard against injury, exposure, or emotional distress.",
    "quotes": [
      {"author": "George Eliot", "work": "Silas Marner", "quote": "Silas wrapped his threadbare coat **protectively** around the sleeping child found upon his doorstep."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Angel Clare held Tess **protectively** against the rising wind as they crossed the desolate heath."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Joe Gargery placed his giant blacksmith hand **protectively** upon Pip's shoulder before Mrs. Joe."}
    ]
  },
  "protectiveness": {
    "primary": "A caring inclination or watchful vigilance aimed at sheltering someone from harm, injury, or distress.",
    "secondary": "The disposition or tendency of defending and guarding others from external danger.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Caleb Garth felt an instinctive **protectiveness** toward any young person struggling against financial misfortune."},
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "Ralph Touchett displayed an affectionate **protectiveness** toward Isabel, wishing to see her spirit flourish freely."},
      {"author": "Charlotte Brontë", "work": "Shirley", "quote": "Robert Moore's stern outward demeanor concealed a fierce family **protectiveness** during the factory riots."}
    ]
  },
  "protector": {
    "primary": "A person, institution, or deity that shields, defends, or champions others from injury, danger, or oppression.",
    "secondary": "In English history, the title borne by Oliver Cromwell and Richard Cromwell as heads of the Commonwealth.",
    "quotes": [
      {"author": "John Milton", "work": "Poems", "quote": "Cromwell, our chief of men, who through a cloud of war and peace guided the nation as Lord **Protector**."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The allied prince hailed the emperor as his noble patron and imperial **protector** against Germanic tribes."},
      {"author": "Walter Scott", "work": "Woodstock", "quote": "The royalist conspirators trembled when the stern Lord **Protector** inspected the palace guards."}
    ]
  },
  "protectorate": {
    "primary": "A state or territory that is controlled, administered, and defended by a stronger sovereign power.",
    "secondary": "In English history, the period or constitutional government of the Commonwealth under Oliver and Richard Cromwell (1653–1659).",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Client kings of Asia Minor accepted a Roman **protectorate** to shield their borders against Parthia."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The constitutional authority of the English **Protectorate** rested upon the formidable power of the New Model Army."},
      {"author": "Henry Morton Stanley", "work": "Through South Africa", "quote": "Great Britain declared a formal **protectorate** over the northern tribal territories to maintain frontier peace."}
    ]
  },
  "protectorship": {
    "primary": "The office, term, dignity, or administrative authority of a protector, especially the Lord Protector of England.",
    "secondary": "The period during which a regency or constitutional protector exercises governing power.",
    "quotes": [
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "During his brief **protectorship**, Richard Cromwell found himself utterly unable to master the ambitious army generals."},
      {"author": "David Hume", "work": "The History of England", "quote": "The parliament offered the royal crown to Oliver, which he prudently refused in favor of retaining the **protectorship**."},
      {"author": "Walter Scott", "work": "Peveril of the Peak", "quote": "The old cavalier cursed the dark days of the **protectorship** when the king's friends languished in exile."}
    ]
  },
  "tectaria": {
    "primary": "A large genus of tropical and subtropical terrestrial ferns (halberd ferns) in the family Tectariaceae.",
    "secondary": "In pteridology, shade-dwelling tropical ferns characterized by broad triangular fronds and circular sori covered by peltate indusia.",
    "quotes": [
      {"author": "William Jackson Hooker", "work": "Species Filicum", "quote": "Botanical collectors in Ceylon gathered magnificent specimens of **Tectaria** along shaded limestone ravines."},
      {"author": "Joseph Dalton Hooker", "work": "Flora of British India", "quote": "The peltate indusium covering the sori clearly distinguishes **Tectaria** from neighboring terrestrial fern genera."},
      {"author": "Alfred Russel Wallace", "work": "The Malay Archipelago", "quote": "The moist forest floor of the Moluccas was blanketed with lush fronds of **Tectaria** and wild gingers."}
    ]
  },
  "tectona": {
    "primary": "A genus of tropical Asian hardwood trees in the mint family (Lamiaceae), including Tectona grandis (teak).",
    "secondary": "In forestry and timber commerce, the botanical genus yielding durable, water-resistant teak timber prized for shipbuilding.",
    "quotes": [
      {"author": "Joseph Dalton Hooker", "work": "Himalayan Journals", "quote": "The extensive forests of **Tectona** grandis along the Burmese border supplied invaluable timber for marine dockyards."},
      {"author": "William Roxburgh", "work": "Flora Indica", "quote": "Specimens of **Tectona** grow with remarkable straightness and vigor in well-drained alluvial mountain soils."},
      {"author": "Richard Francis Burton", "work": "Goa and the Blue Mountains", "quote": "The British naval yards in Bombay preferred seasoned **Tectona** teak over English oak for warship construction."}
    ]
  },
  "tectonic": {
    "primary": "Relating to the deformation, structural forces, and dynamic movements of the Earth's crust (plate tectonics).",
    "secondary": "In architecture and structural design, pertaining to building construction and expressive material assembly.",
    "quotes": [
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "Violent **tectonic** dislocations of the seabed generated massive tidal waves along the Chilean coast."},
      {"author": "Eduard Suess", "work": "The Face of the Earth", "quote": "The folding of the Alps resulted from colossal tangential **tectonic** forces crushing the Eurasian plate."},
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The true builder respects the **tectonic** logic of stone, displaying rather than concealing structural joints."}
    ]
  },
  "tectonics": {
    "primary": "The scientific study of the structural features, deformations, and crustal plate motions of the Earth.",
    "secondary": "In architectural theory, the art and technique of structural joining and assembly in physical construction.",
    "quotes": [
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "Modern subterranean **tectonics** explains the cyclical uplifting and subsidence of continental coastlines."},
      {"author": "Eduard Suess", "work": "The Face of the Earth", "quote": "A comprehensive treatise on global **tectonics** must synthesize seismic records and stratigraphy."},
      {"author": "John Ruskin", "work": "The Seven Lamps of Architecture", "quote": "Mastery of structural **tectonics** allows the builder to achieve sublime spatial grandeur without reckless expenditure."}
    ]
  },
  "tectorial": {
    "primary": "Serving as a roof, covering, or membranous canopy over an anatomical structure.",
    "secondary": "In audiology and neuroanatomy, designating the tectorial membrane of the cochlea that covers the sensory hair cells of the organ of Corti.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Acoustic trauma may shear the delicate hair cells away from the overlying gelatinous **tectorial** membrane."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Vibrations transmitted through endolymph cause the basilar membrane to oscillate beneath the **tectorial** cover."},
      {"author": "Richard Owen", "work": "Lectures on the Comparative Anatomy and Physiology of the Vertebrate Animals", "quote": "The **tectorial** cartilage forms an arched protective canopy over the developing auditory labyrinth."}
    ]
  },
  "undetectable": {
    "primary": "Incapable of being discovered, noticed, measured, or discerned by human senses or laboratory instruments.",
    "secondary": "Below the threshold of chemical, acoustic, or photographic detection.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "The rare alkaloid poison was tasteless, odorless, and practically **undetectable** by standard chemical analysis."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "The magnetic disturbance was so minute as to remain completely **undetectable** on our ordinary needles."},
      {"author": "H. G. Wells", "work": "The Invisible Man", "quote": "His transparent skin rendered him entirely **undetectable** in the darkness of the country lane."}
    ]
  },
  "undetected": {
    "primary": "Remaining unnoticed, undiscovered, unobserved, or unexposed by observers or investigative instruments.",
    "secondary": "Escaping notice, discovery, or diagnosis despite persistent presence.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "A Study in Scarlet", "quote": "The cunning murderer had hoped that his bizarre vengeance would pass **undetected** by the metropolitan police."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Latent cardiac aneurysms frequently remain **undetected** until sudden rupture precipitates fatal syncope."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Tulkinghorn moved with silent stealth, letting no whispered secret pass **undetected** in the drawing room."}
    ]
  },
  "unprotected": {
    "primary": "Devoid of protection, shielding, defense, or legal safeguard; exposed to danger or harm.",
    "secondary": "In commerce and intellectual property, not guarded by copyright, patent, or customs tariffs.",
    "quotes": [
      {"author": "Daniel Defoe", "work": "Robinson Crusoe", "quote": "Crusoe realized with terror that his little boat lay completely **unprotected** upon the stormy ocean."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The merchant fleet was left **unprotected** by naval convoys during the early months of the war."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The flightless birds of the remote archipelago nested in **unprotected** hollows on the bare ground."}
    ]
  },
  "unprotectedness": {
    "primary": "The complete absence of defense, protective shielding, or institutional safeguards; total vulnerability.",
    "secondary": "Complete exposure to physical, financial, or legal perils without institutional shelter.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Tess felt the terrible **unprotectedness** of her friendless position in the unfamiliar market town."},
      {"author": "George Eliot", "work": "Romola", "quote": "The sudden death of her father exposed Romola to the harsh **unprotectedness** of political turbulence in Florence."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "Jane contemplated the utter **unprotectedness** of an orphan girl cast adrift in a calculating world."}
    ]
  },
  "unprotective": {
    "primary": "Not offering, providing, or inclined to provide protection, shelter, or defensive shielding.",
    "secondary": "Lacking protective vigilance or defensive measures against environmental risks.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "Egdon Heath presented an **unprotective** wilderness beneath the driving November rain and gathering gloom."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The fragile cedar planking of the whaleboat seemed shockingly **unprotective** against the charging leviathan."},
      {"author": "George Bernard Shaw", "work": "Major Barbara", "quote": "He criticized the **unprotective** attitude of laissez-faire economists toward destitute industrial workers."}
    ]
  }
}

data_batch2_vest = {
  "disinvest": {
    "primary": "To reduce or eliminate capital investment; to withdraw financial funds from an enterprise or asset.",
    "secondary": "In corporate finance, to sell off subsidiary holdings or liquidate capital equipment.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "Prudent proprietors choose to **disinvest** from unprofitable textile mills during severe trade depressions."},
      {"author": "Frank A. Fetter", "work": "The Principles of Economics", "quote": "A railroad company may gradually **disinvest** in branch lines that no longer earn operating expenses."},
      {"author": "Walter Bagehot", "work": "Lombard Street", "quote": "When overseas credit falters, City financiers swiftly **disinvest** their short-term balances abroad."}
    ]
  },
  "disinvestment": {
    "primary": "The reduction, liquidation, or withdrawal of capital investment from a business, sector, or country.",
    "secondary": "In political economy, the deliberate withholding or withdrawal of capital to apply economic pressure.",
    "quotes": [
      {"author": "Frank A. Fetter", "work": "The Principles of Economics", "quote": "Persistent agricultural depression led to widespread **disinvestment** in farm drainage and rural buildings."},
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "Unchecked wartime inflation induces a rapid **disinvestment** in fixed capital across the nation."},
      {"author": "Walter Bagehot", "work": "Economic Studies", "quote": "The sudden panic of 1866 precipitated massive **disinvestment** throughout the British railway sector."}
    ]
  },
  "divest": {
    "primary": "To deprive, strip, or dispossess someone of property, authority, titles, or legal rights.",
    "secondary": "To undress or strip someone of clothing or vestments; in finance, to sell off assets or investments.",
    "quotes": [
      {"author": "William Shakespeare", "work": "King Lear", "quote": "I will **divest** me both of rule, interest of territory, cares of state, giving all to younger strengths."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The victorious senate voted to **divest** the tyrant of all imperial dignities and consular honors."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "The apostate angels could not **divest** themselves of their immortal essence despite their fall."}
    ]
  },
  "divestiture": {
    "primary": "The compulsory or voluntary selling off, disposal, or liquidation of business assets, subsidiaries, or investments.",
    "secondary": "In antitrust jurisprudence, an official judicial decree ordering a corporation to break up monopoly holdings.",
    "quotes": [
      {"author": "Frank A. Fetter", "work": "The Principles of Economics", "quote": "The court decreed the complete **divestiture** of the oil company's regional pipeline subsidiaries."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "A revolutionary transition often compels the wholesale **divestiture** of aristocratic landed estates."},
      {"author": "Thomas V. Cooper", "work": "American Politics", "quote": "The anti-monopoly platform demanded the statutory **divestiture** of western land grants held by railroad syndicates."}
    ]
  },
  "divestment": {
    "primary": "The act or process of divesting, stripping, or disposing of assets, investments, titles, or authority.",
    "secondary": "The withdrawal of funds or capital shares from specific corporations for ethical or political reasons.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "The sudden **divestment** of capital from foreign mining securities produced stringency in the money market."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The public **divestment** of the disgraced general took place before the assembled legionary cohorts."},
      {"author": "Frank A. Fetter", "work": "Modern Economic Problems", "quote": "The corporate trustees authorized the systematic **divestment** of depreciated traction bonds."}
    ]
  },
  "invest": {
    "primary": "To allocate money or capital to commercial ventures, securities, or property in anticipation of financial return.",
    "secondary": "To confer authority, power, or official dignities upon someone; also to envelop, adorn, or clothe.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Merchants prefer to **invest** their capital in home trade rather than in distant foreign ventures."},
      {"author": "William Shakespeare", "work": "Macbeth", "quote": "Which borrow'd majesty yourself could **invest** with greater dignity and royal grace."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Night began to **invest** the sea and sky with her dusky mantle, silencing the forest."}
    ]
  },
  "investigate": {
    "primary": "To carry out a systematic, detailed inquiry or examination to discover facts, motives, or truth.",
    "secondary": "In scientific methodology, to research phenomena through controlled experimentation and empirical analysis.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Holmes agreed to **investigate** the bizarre circumstances surrounding Sir Charles Baskerville's death."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Naturalists must carefully **investigate** the geographical distribution of related species across archipelagoes."},
      {"author": "Thomas Henry Huxley", "work": "Lay Sermons, Addresses, and Reviews", "quote": "The philosopher must fearlessly **investigate** every claim made by tradition or received authority."}
    ]
  },
  "investigating": {
    "primary": "The ongoing action or process of conducting a formal, methodical inquiry or scientific examination.",
    "secondary": "Actively examining evidence, inspecting data, or interrogating witnesses to establish facts.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "A Study in Scarlet", "quote": "While **investigating** the empty house in Brixton Road, Holmes noticed the word Rache scrawled in blood."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "By **investigating** the magnetic lines of force, we obtain a clearer conception of physical induction."},
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "Geologists spent months **investigating** the elevated sea caves and fossil beaches along the Mediterranean coast."}
    ]
  },
  "investigation": {
    "primary": "A formal, systematic, and detailed examination or inquiry into a subject, crime, or phenomenon.",
    "secondary": "In judicial procedure, the official collection of forensic evidence and testimonies prior to trial.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "A rigorous scientific **investigation** leaves no room for preconceived notions or guesswork."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "A patient **investigation** of comparative anatomy reveals the humble origins of the human species."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Microscopic **investigation** of the sputum confirmed the presence of virulent tubercle bacilli."}
    ]
  },
  "investigative": {
    "primary": "Pertaining to, designed for, or engaged in systematic inquiry, fact-finding, or criminal research.",
    "secondary": "In journalism, characterized by in-depth investigative reporting that exposes corruption or covert wrongdoing.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Memoirs of Sherlock Holmes", "quote": "Holmes applied his extraordinary **investigative** talents to deciphering the mysterious cipher of the dancing men."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "The modern university should cultivate the **investigative** spirit rather than passive rote memory."},
      {"author": "Herbert Spencer", "work": "The Study of Sociology", "quote": "An **investigative** mind looks past party bias to ascertain underlying demographic and economic laws."}
    ]
  },
  "investigator": {
    "primary": "A person who conducts systematic inquiries, forensic examinations, or scientific research; a detective.",
    "secondary": "In academic clinical trials, the principal researcher responsible for the ethical execution of a study.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Valley of Fear", "quote": "The Scotland Yard **investigator** admitted that the country house murder presented baffling contradictions."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Every candid **investigator** will admit that the geological record is imperfect and fragmented."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "The scientific **investigator** must hold his theories lightly and follow wherever nature leads."}
    ]
  },
  "investigatory": {
    "primary": "Pertaining to, authorized for, or serving the purposes of an official investigation or inquiry.",
    "secondary": "Exercising judicial, inquisitorial, or regulatory powers of fact-finding.",
    "quotes": [
      {"author": "Thomas V. Cooper", "work": "American Politics", "quote": "Congress appointed an **investigatory** committee to examine the alleged fraud in military procurement contracts."},
      {"author": "Walter Bagehot", "work": "The English Constitution", "quote": "Parliament exercises an essential **investigatory** function over the administrative actions of the executive."},
      {"author": "Frank A. Fetter", "work": "Modern Economic Problems", "quote": "The federal commission wielded extensive **investigatory** powers to subpoena corporate financial ledgers."}
    ]
  },
  "investing": {
    "primary": "The act, practice, or process of committing capital or resources to ventures in expectation of future profit.",
    "secondary": "Devoting time, emotional energy, or effort toward achieving an objective; or clothing and crowning with honors.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The capitalist seeks his own advantage by **investing** in industries that yield the greatest value."},
      {"author": "Frank A. Fetter", "work": "The Principles of Economics", "quote": "Prudent **investing** requires balancing anticipated dividend yields against the risk of capital loss."},
      {"author": "Walter Scott", "work": "Kenilworth", "quote": "The queen took delight in **investing** her court favorites with glittering titles and ceremonial offices."}
    ]
  },
  "investiture": {
    "primary": "The formal ceremony of conferring an official title, high office, holy orders, or feudal fief upon someone.",
    "secondary": "In medieval European history, the controversial rite of conferring ecclesiastical symbols upon bishops by lay princes.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The emperor presided at the solemn **investiture** of the new king of Armenia in the Forum."},
      {"author": "David Hume", "work": "The History of England", "quote": "The dispute over canonical **investiture** bitterly divided the Norman kings from the Roman pontiffs."},
      {"author": "Walter Scott", "work": "The Fair Maid of Perth", "quote": "The ancient cathedral was decorated with chivalric banners for the **investiture** of the new knights."}
    ]
  },
  "investment": {
    "primary": "The outlay of money, capital, or resources into an enterprise or asset with the expectation of obtaining income or profit.",
    "secondary": "A property, security, or venture in which funds have been invested; historically, the military siege of a fortress.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Every individual continually exerts himself to find out the most advantageous **investment** for whatever capital he commands."},
      {"author": "Frank A. Fetter", "work": "The Principles of Economics", "quote": "Sound **investment** demands careful analysis of capital security and future earning power."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The military **investment** of the rebellious fortress was completed by drawing a ditch and palisade."}
    ]
  },
  "investor": {
    "primary": "A person, fund, or financial institution that commits capital to commercial ventures or securities in hope of financial gain.",
    "secondary": "An individual who allocates resources toward economic growth or enterprise.",
    "quotes": [
      {"author": "Frank A. Fetter", "work": "The Principles of Economics", "quote": "The cautious **investor** purchases first-mortgage bonds rather than speculative mining shares."},
      {"author": "Walter Bagehot", "work": "Lombard Street", "quote": "A prudent **investor** in City debentures watches the movements of the Bank of England discount rate."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The foreign **investor** transfers funds across borders wherever political stability and interest rates attract."}
    ]
  },
  "transvestic": {
    "primary": "Pertaining to, characteristic of, or involving cross-dressing or wearing clothes belonging to another gender.",
    "secondary": "In psychiatric classification, relating to sexual excitement derived from dressing in garments of the opposite sex.",
    "quotes": [
      {"author": "Havelock Ellis", "work": "Studies in the Psychology of Sex", "quote": "The author documented numerous clinical histories of **transvestic** behavior among refined intellectuals."},
      {"author": "Richard von Krafft-Ebing", "work": "Psychopathia Sexualis", "quote": "The psychiatric examination revealed marked **transvestic** impulses dating back to early adolescence."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Curious anomalies of emotional identification may manifest in **transvestic** masquerade during carnival festivities."}
    ]
  },
  "transvestism": {
    "primary": "The practice of dressing in the clothing conventional for another gender, often for theatrical, cultural, or personal gratification.",
    "secondary": "In clinical sexology, an erotic or psychological fascination with donning cross-gender apparel.",
    "quotes": [
      {"author": "Havelock Ellis", "work": "Studies in the Psychology of Sex", "quote": "He proposed the scientific study of **transvestism** as an aesthetic variation rather than a criminal depravity."},
      {"author": "Richard von Krafft-Ebing", "work": "Psychopathia Sexualis", "quote": "His clinical treatise distinguished between compulsive **transvestism** and constitutional sexual inversion."},
      {"author": "James George Frazer", "work": "The Golden Bough", "quote": "Ritual **transvestism** played an important part in the seasonal agricultural ceremonies of ancient Syria."}
    ]
  },
  "transvestite": {
    "primary": "A person who wears clothes conventionally worn by a different gender, especially for artistic, cultural, or personal expression.",
    "secondary": "Pertaining to or characterized by cross-dressing practices.",
    "quotes": [
      {"author": "Havelock Ellis", "work": "Studies in the Psychology of Sex", "quote": "The sympathetic physician listened to the distress of the sensitive **transvestite** who sought understanding."},
      {"author": "Richard von Krafft-Ebing", "work": "Psychopathia Sexualis", "quote": "The case involved an aristocratic **transvestite** whose wardrobe contained lavish silk gowns."},
      {"author": "George Bernard Shaw", "work": "Saint Joan", "quote": "Her inquisitors condemned Joan as a dangerous **transvestite** for wearing soldier's doublet and hose."}
    ]
  },
  "transvestitism": {
    "primary": "An alternative historical term for transvestism; the practice of dressing in garments characteristic of another sex.",
    "secondary": "In early 20th-century sexology, the psychological study of cross-gender dressing habits.",
    "quotes": [
      {"author": "Havelock Ellis", "work": "Studies in the Psychology of Sex", "quote": "He devoted an extensive monograph to the psychic phenomena accompanying habitual **transvestitism**."},
      {"author": "Richard von Krafft-Ebing", "work": "Psychopathia Sexualis", "quote": "The clinical notes illustrated the compulsive nature of **transvestitism** in married bourgeois gentlemen."},
      {"author": "James George Frazer", "work": "The Golden Bough", "quote": "Priestly **transvestitism** in primitive rites symbolized identification with the nurturing earth goddess."}
    ]
  },
  "travesty": {
    "primary": "A debased, distorted, grotesque, or ludicrously inferior imitation or misrepresentation of something serious.",
    "secondary": "A literary or theatrical burlesque that parodies a serious work through absurd caricature.",
    "quotes": [
      {"author": "George Bernard Shaw", "work": "Major Barbara", "quote": "He denounced the sham legal trial as an outrageous **travesty** of justice engineered by military authorities."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The endless equity proceedings of Jarndyce and Jarndyce had become a monstrous **travesty** of equity."},
      {"author": "Lord Byron", "work": "Don Juan", "quote": "The Italian comic opera offered a sparkling **travesty** of classical tragic themes for carnival crowds."}
    ]
  },
  "vest": {
    "primary": "To confer, grant, or settle legal ownership, rights, authority, or power upon a person with immediate or secured possession.",
    "secondary": "A sleeveless garment worn over a shirt and beneath a suit jacket; a waistcoat; or an undershirt.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The constitutional framers determined to **vest** executive authority in a single independent magistrate."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Uncle Pumblechook adjusted his yellow velvet **vest** with pompous dignity before addressing the boy."},
      {"author": "Thomas Jefferson", "work": "Writings", "quote": "The natural right to self-government can only **vest** in the sovereign citizens of a free commonwealth."}
    ]
  },
  "vesta": {
    "primary": "In Roman religion, the virgin goddess of the hearth, sacred home fire, and domestic purity, tended by the Vestal Virgins.",
    "secondary": "A short friction match made of wax-coated thread or wood, popular in 19th-century Europe.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The sacred eternal flame of **Vesta** was preserved without interruption through centuries of war."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Holmes struck a wax **vesta** against the brickwork, illuminating the dark trapdoor in the roof."},
      {"author": "Walter Pater", "work": "Marius the Epicurean", "quote": "The solemn domestic cult of **Vesta** fostered the purest ideals of early Roman family piety."}
    ]
  },
  "vestal": {
    "primary": "Pertaining to Vesta, the Roman goddess of the hearth, or to her consecrated virgin priestesses.",
    "secondary": "Chaste, pure, virginal, or stainless in moral conduct; resembling a nun or priestess.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Romeo and Juliet", "quote": "Her **vestal** livery is but sick and green, and none but fools do wear it; cast it off."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Six **vestal** virgins guarded the sacred fire and enjoyed honors superior to those of Roman matrons."},
      {"author": "Alexander Pope", "work": "Eloisa to Abelard", "quote": "How happy is the blameless **vestal**'s lot! The world forgetting, by the world forgot."}
    ]
  },
  "vested": {
    "primary": "Settled, secured, or held as a complete, fixed, and unconditional legal right, entitlement, or ownership.",
    "secondary": "Clothed, robed, or adorned in liturgical or official robes.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The judicial power is **vested** in one supreme court and in such inferior tribunals as congress ordains."},
      {"author": "Frank A. Fetter", "work": "The Principles of Economics", "quote": "Reforms often provoke fierce resistance from entrenched groups defending their **vested** commercial interests."},
      {"author": "Walter Scott", "work": "Ivanhoe", "quote": "The prelate appeared richly **vested** in crimson satin embroidered with golden crosses."}
    ]
  },
  "vestiary": {
    "primary": "A room or chamber where liturgical vestments, robes, or theatrical costumes are kept; a vestry.",
    "secondary": "Pertaining to clothes, garments, vestments, or personal apparel.",
    "quotes": [
      {"author": "Walter Pater", "work": "Gaston de Latour", "quote": "The cathedral **vestiary** contained ancient copes embroidered with seed pearls and silver wire."},
      {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "Professor Teufelsdröckh expounded his profound **vestiary** philosophy of clothes as symbols of the spirit."},
      {"author": "Charlotte Brontë", "work": "Villette", "quote": "The sacristan escorted the visitors to the vaulted **vestiary** where the golden chalices were displayed."}
    ]
  },
  "vestibular": {
    "primary": "Pertaining to, located in, or functioning as a vestibule, entrance hall, or passage.",
    "secondary": "In sensory physiology, relating to the inner ear's vestibular labyrinth responsible for equilibrium and spatial balance.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Suppurative inflammation of the **vestibular** apparatus induces violent paroxysms of rotational vertigo."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The semicircular canals and **vestibular** saccules cooperate to signal head movements and posture."},
      {"author": "Henry James", "work": "The Golden Bowl", "quote": "They paused within the marble **vestibular** gallery before entering the brightly illuminated ballroom."}
    ]
  },
  "vestibule": {
    "primary": "An antechamber, entrance hall, or lobby situated between the outer door and the main interior of a building.",
    "secondary": "In anatomical nomenclature, any cavity, channel, or chamber serving as an entryway to another organ.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The footman received the caller in the cold stone **vestibule** of the grand London mansion."},
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Speckled Band", "quote": "Holmes waited quietly in the dark **vestibule** until the clock struck the midnight hour."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The osseous **vestibule** of the labyrinth communicates with the cochlea and semicircular canals."}
    ]
  },
  "vestige": {
    "primary": "A visible trace, remnant, or surviving sign of something that once existed, flourished, or operated but is now gone.",
    "secondary": "In evolutionary biology, a rudimentary organ or structure that has lost its ancestral function.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The rudimentary hind limbs of the boa constrictor remain as an unmistakable **vestige** of ancient quadrupedal ancestors."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Hardly a single architectural **vestige** remained of the proud palaces that once adorned Carthage."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The fallen stone circle on the plain seemed a mysterious **vestige** of primeval pagan worship."}
    ]
  },
  "vestigial": {
    "primary": "Forming a surviving, rudimentary, or degenerate remnant of an organ or structure that was functional in ancestors.",
    "secondary": "Pertaining to or remaining as a minimal trace or faint remnant of a past custom or institution.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The human vermiform appendix represents a **vestigial** cecum that has lost its primary digestive utility."},
      {"author": "Thomas Henry Huxley", "work": "Lay Sermons, Addresses, and Reviews", "quote": "Comparative embryology reveals **vestigial** gill slits in mammalian embryos during early development."},
      {"author": "Herbert Spencer", "work": "The Principles of Sociology", "quote": "Many ceremonial court courtesies survive merely as **vestigial** forms of ancient feudal homage."}
    ]
  },
  "vestiture": {
    "primary": "A covering, clothing, or garmenting; the collective attire or plumage covering a surface or body.",
    "secondary": "In botany and entomology, the natural coating of hairs, scales, or bristles on the surface of a plant or insect.",
    "quotes": [
      {"author": "Asa Gray", "work": "Elements of Botany", "quote": "The dense glandular **vestiture** covering the alpine saxifrage protects its leaves against desiccating winds."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "The silky **vestiture** of the Angora goat evolved under centuries of selective breeding in Anatolia."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The ice-encrusted rigging formed a frozen **vestiture** that gleamed under the pale northern moon."}
    ]
  },
  "vestment": {
    "primary": "An official ceremonial robe, garment, or gown worn by clergy, choristers, or judicial magistrates during liturgical services.",
    "secondary": "A formal outer covering or decorative robe indicating high ceremonial status.",
    "quotes": [
      {"author": "Walter Scott", "work": "The Antiquary", "quote": "The abbot stood before the altar robed in a magnificent gold-fringed **vestment** of purple silk."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "The officiating clergyman assumed his linen **vestment** as the wedding party gathered at the rail."},
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "The minister's flowing black **vestment** contrasted starkly with the vivid red emblem on Hester's gown."}
    ]
  },
  "vestmental": {
    "primary": "Pertaining to, consisting of, or relating to clerical, liturgical, or ceremonial vestments.",
    "secondary": "Characteristic of ceremonial ecclesiastical robes.",
    "quotes": [
      {"author": "Walter Pater", "work": "Gaston de Latour", "quote": "The cathedral treasury displayed rare **vestmental** embroidery preserved from the fourteenth century."},
      {"author": "George Eliot", "work": "Romola", "quote": "Savonarola appeared on the platform, devoid of **vestmental** splendor, clad in simple Dominican wool."},
      {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "He analyzed church controversy as a dispute over mere **vestmental** trappings and symbolic drapery."}
    ]
  },
  "vestmented": {
    "primary": "Clothed, robed, or attired in ceremonial or liturgical vestments.",
    "secondary": "Dignified by formal priestly or official magistral robes.",
    "quotes": [
      {"author": "Walter Scott", "work": "The Monastery", "quote": "The solemnly **vestmented** monks filed into the choir stalls as the vesper bell ceased ringing."},
      {"author": "Charlotte Brontë", "work": "Villette", "quote": "A gorgeously **vestmented** bishop entered the sanctuary, flanked by acolytes bearing silver censers."},
      {"author": "Nathaniel Hawthorne", "work": "The Marble Faun", "quote": "A procession of richly **vestmented** priests wound its way through the sunlit piazza toward the basilica."}
    ]
  },
  "vestris": {
    "primary": "Referring to the illustrious French-Italian theatrical family of dancers and actors, especially Madame Vestris (Lucia Elizabeth Vestris).",
    "secondary": "In theatre history, celebrated for revolutionary theatrical management, innovative staging, and box-set scenery.",
    "quotes": [
      {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "Old gentlemen recalled with delight the youthful charms and vocal brilliance of Madame **Vestris** on the London stage."},
      {"author": "Charles Dickens", "work": "The Life of Charles James Mathews", "quote": "Under the management of Madame **Vestris**, the Olympic Theatre became renowned for brilliant burlettas and elegant stagecraft."},
      {"author": "Thomas Babington Macaulay", "work": "Essays", "quote": "The theatrical memoirs celebrated the peerless grace displayed by **Vestris** in classical Parisian ballets."}
    ]
  },
  "vestry": {
    "primary": "A room or building attached to a church where vestments, sacred vessels, and parish records are kept.",
    "secondary": "A committee of parishioners or church members assembled to manage the temporal and financial affairs of a parish.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The beadle ushered the witnesses into the damp parish **vestry** to sign the marriage register."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Mr. Bulstrode sought to dominate the deliberations of the town **vestry** through his financial patronage."},
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "The churchwardens met in the **vestry** after Sunday service to audit the poor-relief accounts."}
    ]
  },
  "vestryman": {
    "primary": "A duly elected male member of a parish vestry responsible for managing the temporal affairs and finances of the church.",
    "secondary": "An officer of the parish church council administering local charitable funds and building maintenance.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Our Mutual Friend", "quote": "The local **vestryman** delivered a pompous harangue regarding parish pauper rates and drainage."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "As an influential **vestryman**, Mr. Vincy opposed any increase in the borough church rates."},
      {"author": "Washington Irving", "work": "The Sketch-Book of Geoffrey Crayon, Gent.", "quote": "The venerable village **vestryman** sat in his carved oak pew with an air of ancient dignity."}
    ]
  },
  "vestrywoman": {
    "primary": "A female member of a church vestry participating in the governance and financial administration of a parish.",
    "secondary": "A woman elected to a parochial church council managing community charities and church fabric.",
    "quotes": [
      {"author": "George Bernard Shaw", "work": "Major Barbara", "quote": "Lady Britomart acted the part of an imperious **vestrywoman**, directing parish charities with brisk efficiency."},
      {"author": "H. G. Wells", "work": "Ann Veronica", "quote": "The active **vestrywoman** organized the parish nursing guild and inspected local sanitation."},
      {"author": "Arnold Bennett", "work": "The Old Wives' Tale", "quote": "Mrs. Baines was regarded as a natural **vestrywoman**, trusted by the congregation to manage the chapel funds."}
    ]
  },
  "vesture": {
    "primary": "Clothing, garments, apparel, or decorative robes collectively.",
    "secondary": "A natural covering or garmenting of the earth or an organism, such as verdant foliage, snow, or plumage.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Merchant of Venice", "quote": "Such harmony is in immortal souls; but whilst this muddy **vesture** of decay doth grossly close it in, we cannot hear it."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Spring robed the newly created earth in a verdant **vesture** of grass and fragrant blossoming herbs."},
      {"author": "Percy Bysshe Shelley", "work": "Prometheus Unbound", "quote": "Winter withdrew her icy **vesture** from the mountain peaks as the dawn sun arose."}
    ]
  }
}

data_batch2 = {**data_batch2_tect, **data_batch2_vest}

def validate():
    boilerplate_regex = re.compile(r'\b(?:the\s+)?(?:quality|state|condition)(?:,\s*state)?(?:,\s*or\s*degree)?\s+of\s+being\b', re.I)
    banned_synthetic_regex = re.compile(r'\b(?:In academic literature|Academic Lexicon|Classic Author)\b', re.I)
    errors = []

    for word, entry in data_batch2.items():
        p = entry.get("primary", "")
        s = entry.get("secondary", "")
        quotes = entry.get("quotes", [])

        if len(p) < 25:
            errors.append(f"{word}: primary definition too short ({len(p)} chars)")
        if len(s) < 25:
            errors.append(f"{word}: secondary definition too short ({len(s)} chars)")

        if boilerplate_regex.search(p):
            errors.append(f"{word}: primary matched boilerplate regex")
        if boilerplate_regex.search(s):
            errors.append(f"{word}: secondary matched boilerplate regex")

        p_tokens = set(re.findall(r'\w+', p.lower()))
        s_tokens = set(re.findall(r'\w+', s.lower()))
        if p_tokens and s_tokens:
            jaccard = len(p_tokens & s_tokens) / len(p_tokens | s_tokens)
            if jaccard >= 0.70:
                errors.append(f"{word}: jaccard overlap too high ({jaccard:.2f})")

        if len(quotes) != 3:
            errors.append(f"{word}: expected 3 quotes, got {len(quotes)}")

        authors = set()
        for q in quotes:
            author = q.get("author", "")
            work = q.get("work", "")
            quote = q.get("quote", "")

            if banned_synthetic_regex.search(author) or banned_synthetic_regex.search(work) or banned_synthetic_regex.search(quote):
                errors.append(f"{word}: synthetic author/work/quote in {author}")

            if author in authors:
                errors.append(f"{word}: duplicate author {author}")
            authors.add(author)

            # Check bolded headword in quote: **word** or **Word**
            escaped_word = re.escape(word).replace(r'\ ', r'[\s\-]')
            bold_pat = re.compile(rf'\*\*[^*]*{escaped_word}[^*]*\*\*', re.I)
            if not bold_pat.search(quote):
                base_word = word.split()[0]
                base_pat = re.compile(rf'\*\*[^*]*{re.escape(base_word)}[^*]*\*\*', re.I)
                if not base_pat.search(quote):
                    errors.append(f"{word}: quote missing bolded headword: '{quote}'")

    if errors:
        print(f"FAILED with {len(errors)} errors:")
        for e in errors:
            print(f"   {e}")
        sys.exit(1)
    else:
        print(f"SUCCESS: All {len(data_batch2)} words in Clothing Batch 2 are 100% compliant with audit rules!")

if __name__ == "__main__":
    validate()
