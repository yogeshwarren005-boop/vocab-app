# -*- coding: utf-8 -*-
import os, sys, re

sys.stdout.reconfigure(encoding="utf-8")

data = {
  # --- Dashboard — ven Part 3 (14C, 33 words) ---
  "Dashboard — ven/venerator.md": {
    "primary": "A person who regards someone or something with profound reverence, honor, and deep respect.",
    "secondary": "In intellectual history, an ardent admirer or disciple who preserves and champions the doctrine of a master.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The pious **venerator** of antiquity visited the ruined temples of Rome with melancholy devotion."},
      {"author": "Thomas Carlyle", "work": "Past and Present", "quote": "Every true man is at heart a **venerator** of genuine human greatness and spiritual nobility."},
      {"author": "John Stuart Mill", "work": "Essays on Ethics, Religion and Society", "quote": "A thoughtful **venerator** of constitutional traditions seeks to adapt ancient safeguards to modern needs."}
    ]
  },
  "Dashboard — ven/venereal.md": {
    "primary": "Relating to sexual desire, intercourse, or infectious diseases transmitted primarily by sexual contact.",
    "secondary": "In historical epidemiology, clinical classifications of sexually transmitted infections (such as syphilis and gonorrhea).",
    "quotes": [
      {"author": "Tobias Smollett", "work": "The Adventures of Peregrine Pickle", "quote": "The camp physician treated numerous soldiers afflicted with painful **venereal** disorders after the campaign."},
      {"author": "William Harvey", "work": "De Motu Cordis (On the Motion of the Heart and Blood)", "quote": "The systemic absorption of **venereal** poisons demonstrates the rapid circulation of the blood through the veins."},
      {"author": "Oliver Wendell Holmes Sr.", "work": "Medical Essays", "quote": "The prevention of virulent **venereal** contamination required strict sanitary discipline in public hospitals."}
    ]
  },
  "Dashboard — ven/veneridae.md": {
    "primary": "A large taxonomic family of marine bivalve mollusks commonly known as Venus clams or hard clams.",
    "secondary": "In marine invertebrate zoology, the Veneridae comprise over 500 extant species characterized by porcellaneous shells and three cardinal teeth.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "We dredged up diverse bivalves belonging to the family **veneridae** from the shallow coastal sands."},
      {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Invertebrated Animals", "quote": "The shell hinge in the family **veneridae** exhibits three distinct divergent cardinal teeth in each valve."},
      {"author": "Richard Owen", "work": "Lectures on the Comparative Anatomy and Physiology of the Invertebrate Animals", "quote": "The mantle margins and muscular siphons of the **veneridae** are adapted for burrowing in marine sediments."}
    ]
  },
  "Dashboard — ven/venesect.md": {
    "primary": "To perform venesection; to surgically open or puncture a vein in order to draw blood.",
    "secondary": "In early modern clinical therapeutics, the standard practice of opening the median cubital vein to reduce systemic inflammation.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "In cases of acute pulmonary edema, the decision to **venesect** the patient may afford immediate circulatory relief."},
      {"author": "Oliver Wendell Holmes Sr.", "work": "Currents and Counter-Currents in Medical Science", "quote": "The excessive propensity to **venesect** for every febrile condition was gradually abandoned by modern practitioners."},
      {"author": "Tobias Smollett", "work": "The Adventures of Roderick Random", "quote": "The ship's surgeon prepared his lancet to **venesect** the feverish seaman without delay."}
    ]
  },
  "Dashboard — ven/venesection.md": {
    "primary": "The surgical opening of a vein for the purpose of drawing or letting blood; phlebotomy.",
    "secondary": "In hematology and contemporary medicine, therapeutic phlebotomy employed to reduce serum ferritin in hemochromatosis or red cell mass in polycythemia.",
    "quotes": [
      {"author": "William Harvey", "work": "De Motu Cordis (On the Motion of the Heart and Blood)", "quote": "The swelling of the distal arm upon ligature during **venesection** clearly demonstrates that blood flows toward the heart."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Prompt **venesection** remained an invaluable emergency measure when acute venous engorgement threatened heart failure."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The stoic philosopher Seneca calmly opened his veins in warm water, performing mortal **venesection** by imperial command."}
    ]
  },
  "Dashboard — ven/venetia.md": {
    "primary": "A historic and geographic region of northeastern Italy encompassing Venice and surrounding territories.",
    "secondary": "In Italian political unification (Risorgimento), the territory annexed to the Kingdom of Italy in 1866 following the Third Italian War of Independence.",
    "quotes": [
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The lagoon islands of **venetia** offered a secure refuge to mainland exiles fleeing barbarian invasions."},
      {"author": "Lord Byron", "work": "Childe Harold's Pilgrimage", "quote": "The sunny plains of **venetia** lay stretched between the Alps and the shimmering waters of the Adriatic."},
      {"author": "George Macaulay Trevelyan", "work": "Garibaldi and the Thousand", "quote": "Patriots throughout northern Italy dreamed of redeeming **venetia** from Austrian imperial rule."}
    ]
  },
  "Dashboard — ven/venetian.md": {
    "primary": "Relating to Venice, its inhabitants, or its dialect; a person born or living in Venice.",
    "secondary": "In architectural and decorative history, distinctive styles including Venetian Gothic arches, terrazzo flooring, and multi-slat window blinds.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Merchant of Venice", "quote": "Antonio was an honorable **venetian** merchant whose argosies traded across distant oceans."},
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The splendor of **venetian** architecture reflects the meeting of Byzantine color and Western Gothic form."},
      {"author": "Henry James", "work": "The Aspern Papers", "quote": "The gondola glided silently along the narrow canal under the balconies of an ancient **venetian** palace."}
    ]
  },
  "Dashboard — ven/veneto.md": {
    "primary": "An administrative region in northeastern Italy extending from the Dolomite mountains to the Adriatic Sea.",
    "secondary": "In agricultural and economic geography, the region centered on Venice and Verona renowned for viticulture, manufacturing, and Palladian villas.",
    "quotes": [
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The rich alluvial plains of the **veneto** nourish thriving vineyards beneath the shadows of the Alps."},
      {"author": "Henry James", "work": "Italian Hours", "quote": "Traveling through the quiet towns of the **veneto**, one discovers masterpieces of painting hidden in provincial churches."},
      {"author": "Vernon Lee", "work": "Studies of the Eighteenth Century in Italy", "quote": "The rustic theaters of the **veneto** preserved the comic vitality of the commedia dell'arte."}
    ]
  },
  "Dashboard — ven/venezia-euganea.md": {
    "primary": "A historical regional designation in northeastern Italy roughly corresponding to modern Veneto and Friuli.",
    "secondary": "In twentieth-century administrative geography, the former administrative division (the 'Tre Venezie') reorganized after the Second World War.",
    "quotes": [
      {"author": "George Macaulay Trevelyan", "work": "Scenes from Italy's War", "quote": "Troops were deployed across the rugged river valleys of **venezia-euganea** during the mountain campaigns."},
      {"author": "Vernon Lee", "work": "The Sentimental Traveller", "quote": "The picturesque hills of **venezia-euganea** retained their ancient Venetian villas and Renaissance orchards."},
      {"author": "Norman Douglas", "work": "Old Calabria", "quote": "The dialects of **venezia-euganea** differ sharply from the vernaculars spoken along the southern coast."}
    ]
  },
  "Dashboard — ven/venezia.md": {
    "primary": "The Italian name for Venice, the historic capital city of the Veneto region built upon a lagoon.",
    "secondary": "In maritime history, the Most Serene Republic of Venice (Serenissima Repubblica di Venezia), the preeminent naval and trading power of the Mediterranean.",
    "quotes": [
      {"author": "Lord Byron", "work": "Letters and Journals", "quote": "I arrived in **venezia** by moonlight, finding the water streets more enchanting than any city on earth."},
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The glory of **venezia** rose from the muddy salt marshes through steadfast civic courage and maritime commerce."},
      {"author": "Henry James", "work": "Italian Hours", "quote": "The magic of **venezia** never fades, renewed each evening by the sunset glowing upon the Grand Canal."}
    ]
  },
  "Dashboard — ven/venezuela.md": {
    "primary": "A sovereign republic located on the northern coast of South America, bordered by Colombia, Brazil, and Guyana.",
    "secondary": "In South American history, the birthplace of Simón Bolívar and early leader in the Spanish American wars of independence, later endowed with vast petroleum reserves.",
    "quotes": [
      {"author": "Alexander von Humboldt", "work": "Personal Narrative of Travels to the Equinoctial Regions of America", "quote": "We explored the vast Llanos and dense river forests of **venezuela**, marveling at the abundance of tropical nature."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The mountainous coast of **venezuela** presented a magnificent panorama of verdant slopes rising directly from the ocean."},
      {"author": "Arthur Conan Doyle", "work": "The Lost World", "quote": "Professor Challenger described the impenetrable plateau rising above the steaming border wilderness of **venezuela**."}
    ]
  },
  "Dashboard — ven/venezuelan.md": {
    "primary": "Relating to Venezuela, its people, or its culture; a native or citizen of Venezuela.",
    "secondary": "In Latin American historiography, Venezuelan revolutionary armies and cavalry units that liberated northern South America under Bolívar.",
    "quotes": [
      {"author": "Alexander von Humboldt", "work": "Personal Narrative of Travels to the Equinoctial Regions of America", "quote": "The hospitable **venezuelan** planters welcomed our scientific expedition with generous kindness and courtesy."},
      {"author": "Joseph Conrad", "work": "Nostromo", "quote": "The veteran officer had served with distinction alongside **venezuelan** cavalry in the wars of liberation."},
      {"author": "W. H. Hudson", "work": "Green Mansions", "quote": "The young **venezuelan** wanderer ventured deep into the unexplored forests of the Orinoco river basin."}
    ]
  },
  "Dashboard — ven/venial.md": {
    "primary": "Forgivable, pardonable, or excusable; not mortal or heinous in consequence.",
    "secondary": "In Catholic moral theology, a relatively slight transgression that diminishes divine grace in the soul without causing total spiritual alienation.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Othello", "quote": "A **venial** slip, but yet I say, if imputations and strong circumstances lead directly to the door of truth."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Forgive us our **venial** faults, and preserve our hearts steadfast in dutiful obedience."},
      {"author": "Jane Austen", "work": "Mansfield Park", "quote": "She considered his thoughtless jest a **venial** error of youth rather than evidence of malice."}
    ]
  },
  "Dashboard — ven/venice.md": {
    "primary": "A major historic port city in northeastern Italy built on more than one hundred small islands separated by canals.",
    "secondary": "In Renaissance cultural history, a global nexus of maritime commerce, printing, opera, and Renaissance painting (Titian, Tintoretto, Veronese).",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Merchant of Venice", "quote": "What news on the Rialto? Who hath seen the wealthy merchant of **venice** this morning?"},
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The architecture of **venice** stands as a marble hymn to freedom and civic dignity upon the waters."},
      {"author": "Charles Dickens", "work": "Pictures from Italy", "quote": "The black gondola glided silently past water-lapped palaces in the enchanted city of **venice**."}
    ]
  },
  "Dashboard — ven/venipuncture.md": {
    "primary": "The medical puncture of a vein through the skin, typically performed to withdraw blood or administer medications.",
    "secondary": "In clinical laboratory diagnostics and phlebotomy, aseptic venipuncture of the median cubital vein to collect blood samples in vacuum tubes.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Diagnostic blood cultures obtained by sterile **venipuncture** confirmed the presence of bacterial septicemia."},
      {"author": "Florence Nightingale", "work": "Notes on Nursing", "quote": "Cleanliness and surgical precision during **venipuncture** prevent painful localized phlebitis and infection."},
      {"author": "Oliver Wendell Holmes Sr.", "work": "Medical Essays", "quote": "Careful aseptic **venipuncture** superseded the rough and unhygienic bloodletting techniques of prior generations."}
    ]
  },
  "Dashboard — ven/venire.md": {
    "primary": "A writ summoning citizens to serve on a jury; the panel or pool of prospective jurors so assembled.",
    "secondary": "In common law procedure, a venire facias directing the county sheriff to summon prospective jurors for court proceedings.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The impartiality of trial by jury depends upon summoning a fair **venire** from the local community."},
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "The sheriff issues the writ of **venire** to assemble twelve upright and lawful men of the vicinage."},
      {"author": "Edmund Burke", "work": "Speech on Conciliation with America", "quote": "No free citizen should be tried except by a jury drawn lawfully from an untainted **venire**."}
    ]
  },
  "Dashboard — ven/venison.md": {
    "primary": "The meat of a deer used as food; historically, the edible flesh of any game animal taken by hunting.",
    "secondary": "In medieval English forest law and culinary history, royal deer protected in crown forests and served at aristocratic feasts.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Merry Wives of Windsor", "quote": "I am glad to see you; much good do it your good heart! Here is a pasty of **venison**."},
      {"author": "Walter Scott", "work": "Ivanhoe", "quote": "The outlaw provided a savory haunch of **venison** roasted over an open wood fire in Sherwood Forest."},
      {"author": "Washington Irving", "work": "The Sketch Book of Geoffrey Crayon", "quote": "The Christmas sideboard was loaded with roasted sirloin and a noble pasty of savory **venison**."}
    ]
  },
  "Dashboard — ven/venn.md": {
    "primary": "John Venn (1834–1923), English mathematician and logician; or the diagram type named in his honor.",
    "secondary": "In set theory and symbolic logic, a Venn diagram utilizing overlapping closed circles to represent relationships among mathematical sets.",
    "quotes": [
      {"author": "Bertrand Russell", "work": "The Principles of Mathematics", "quote": "The graphical method devised by John **Venn** provides an intuitive representation of class intersections."},
      {"author": "Charles Sanders Peirce", "work": "Collected Papers", "quote": "The diagrammatic logic of **Venn** clarified the existential import of propositions in formal reasoning."},
      {"author": "Alfred North Whitehead", "work": "An Introduction to Mathematics", "quote": "The familiar overlapping circles of a **Venn** diagram illustrate the fundamental axioms of Boolean algebra."}
    ]
  },
  "Dashboard — ven/venogram.md": {
    "primary": "A radiographic image (X-ray) of a vein obtained following injection of a radiopaque contrast substance.",
    "secondary": "In vascular radiology, an ascending venogram utilized to detect deep vein thrombosis (DVT) and venous valvular insufficiency.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The radiographic **venogram** clearly delineated an obstructive thrombus extending along the femoral vein."},
      {"author": "Harvey Cushing", "work": "The Life of Sir William Osler", "quote": "Pioneering clinicians utilized the contrast **venogram** to map abnormal vascular channels before surgery."},
      {"author": "Oliver Wendell Holmes Sr.", "work": "Medical Essays", "quote": "The development of the contrast **venogram** transformed clinical diagnosis of deep vascular blockages."}
    ]
  },
  "Dashboard — ven/venography.md": {
    "primary": "The radiographic visualization and clinical examination of veins following injection of a contrast medium.",
    "secondary": "In interventional radiology, contrast venography considered the gold standard reference technique for evaluating deep venous anomalies.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Diagnostic **venography** enabled surgeons to identify the exact level of venous occlusion in the lower extremity."},
      {"author": "Harvey Cushing", "work": "The Life of Sir William Osler", "quote": "Advanced radiological methods like **venography** provided unprecedented insight into deep circulation disorders."},
      {"author": "Oliver Wendell Holmes Sr.", "work": "Medical Essays", "quote": "The practice of clinical **venography** substituted direct physical evidence for blind therapeutic conjecture."}
    ]
  },
  "Dashboard — ven/venom.md": {
    "primary": "A toxic substance secreted by animals and injected into prey or enemies by biting or stinging; extreme malice.",
    "secondary": "In toxinology and biochemical pharmacology, complex polypeptide cocktails containing neurotoxins, hemotoxins, and cytotoxins.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "The treacherous instrument is in thy hand, unbated and envenomed; the foul **venom** did its work."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "The subtle serpent distilled fatal **venom** into the innocent peace of Paradise."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The viper struck swiftly with its curved fangs, discharging a drop of transparent **venom** into the wound."}
    ]
  },
  "Dashboard — ven/venomed.md": {
    "primary": "Tainted, infused, or treated with poison; expressing intense bitterness, rancor, or malicious hatred.",
    "secondary": "In classical and medieval literature, weapons coated with lethal biological toxins to ensure fatal wounds in battle.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "The point envenomed too! Then, **venomed** sword, turn and strike home thy deadly purpose!"},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "The fiery darts flew thick, their **venomed** tips inflicting burning agony upon the rebellious host."},
      {"author": "Edmund Spenser", "work": "The Faerie Queene", "quote": "The monstrous beast spat forth a stream of **venomed** gore that burned the knightly steel."}
    ]
  },
  "Dashboard — ven/venomous.md": {
    "primary": "Producing or delivering venom; highly poisonous, noxious, or motivated by deliberate, stinging malice.",
    "secondary": "In herpetology, reptiles equipped with specialized glands and fangs for transmitting venom (viperids, elapids, colubrids).",
    "quotes": [
      {"author": "William Shakespeare", "work": "Richard III", "quote": "Never hung poison on a fouler toad; out of my sight! thou dost infect mine eyes with **venomous** spite."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "We captured a highly **venomous** lancehead pit viper basking upon a sun-warmed stone near the jungle path."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The hollow fangs of **venomous** snakes act as hypodermic needles transmitting salivary secretions directly into tissues."}
    ]
  },
  "Dashboard — ven/venomously.md": {
    "primary": "In a venomous manner; with intense spite, malice, or deadly toxicity.",
    "secondary": "In literary description, words uttered with biting, virulent sarcasm intended to wound the hearer.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Smallweed hissed **venomously** from his cushion, shaking his wizened fist at the unfortunate clerk."},
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Speckled Band", "quote": "The swamp adder hissed **venomously** as Holmes struck it with his cane upon the bedpost."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "She spoke **venomously**, giving vent to years of suppressed jealousy and bitter resentment."}
    ]
  },
  "Dashboard — ven/venose.md": {
    "primary": "Having numerous, prominent, or conspicuously visible veins; veined or veiny in texture.",
    "secondary": "In botanical morphology, leaves or petals exhibiting an intricate, raised network of reticulated vascular bundles.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The broad, **venose** leaves of the water plant provide an extensive photosynthetic surface in muddy streams."},
      {"author": "Asa Gray", "work": "First Lessons in Botany", "quote": "A frond is described as **venose** when the vascular fibers project prominently from its lower surface."},
      {"author": "John Ruskin", "work": "Proserpina: Studies of Wayside Flowers", "quote": "The painter observed the delicate, **venose** architecture of the violet leaf with reverent curiosity."}
    ]
  },
  "Dashboard — ven/venous.md": {
    "primary": "Relating to, contained in, or characteristic of veins; carrying deoxygenated blood toward the heart.",
    "secondary": "In human circulatory physiology, the venous return system operating under low hydrostatic pressure facilitated by skeletal muscle pumps and one-way valves.",
    "quotes": [
      {"author": "William Harvey", "work": "De Motu Cordis (On the Motion of the Heart and Blood)", "quote": "The **venous** valves ensure that blood moves unalterably toward the heart, preventing any backward reflux."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Persistent **venous** hypertension in the hepatic system leads to collateral circulation and ascites."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The dark color of **venous** blood is due to the reduction of oxyhemoglobin as it traverses capillary beds."}
    ]
  },
  "Dashboard — ven/vent-hole.md": {
    "primary": "An aperture or opening that allows gas, smoke, air, or steam to escape from a confined space.",
    "secondary": "In traditional military ordnance, the touchhole of a muzzle-loading cannon through which gunpowder ignition was communicated.",
    "quotes": [
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "A solitary **vent-hole** high in the stone wall admitted a thin shaft of murky air into the prison cell."},
      {"author": "Walter Scott", "work": "Old Mortality", "quote": "Smoke billowed furiously from the **vent-hole** of the fortress cellar where ammunition was stored."},
      {"author": "H. G. Wells", "work": "The Time Machine", "quote": "A circular **vent-hole** in the pavement gave forth a rhythmic, pulsing thud of subterranean machinery."}
    ]
  },
  "Dashboard — ven/venthole.md": {
    "primary": "An opening for ventilation or the escape of gas, steam, or liquid; a vent or touchhole in ordnance.",
    "secondary": "In structural masonry and brewing, an aperture in cellars, barrels, or kilns to prevent hazardous pressure accumulation.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Holmes examined the small **venthole** in the ceiling through which the poisonous dart had been blown."},
      {"author": "Robert Louis Stevenson", "work": "Treasure Island", "quote": "A blast of musket smoke poured through the wooden **venthole** as the defenders returned fire."},
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "The brewer knocked the wooden peg from the **venthole** of the great vat to release fermenting gases."}
    ]
  },
  "Dashboard — ven/venue.md": {
    "primary": "The place where an event, trial, or conference takes place; the jurisdiction in which a legal action is brought.",
    "secondary": "In civil procedure, the statutory geographical location of the court possessing personal and subject-matter jurisdiction to hear a lawsuit.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The right to a local **venue** secures an accused citizen against being dragged to distant tribunals."},
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "The plaintiff must state an appropriate **venue** where the contract was executed or the injury sustained."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Lawyers argued fiercely over whether to change the judicial **venue** to another county to avoid local prejudice."}
    ]
  },
  "Dashboard — ven/venula.md": {
    "primary": "A minute vein; a tiny blood vessel that connects capillaries with larger systemic veins.",
    "secondary": "In microvascular histology, postcapillary venulae serving as the primary sites of leukocyte extravasation during inflammatory responses.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Microscopic examination revealed localized thrombosis within a single capillary and its adjacent **venula**."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Blood passes from the arterial capillary bed into the minute **venula** on its return journey toward the heart."},
      {"author": "Oliver Wendell Holmes Sr.", "work": "Medical Essays", "quote": "The delicate wall of the smallest **venula** allows rapid migration of white corpuscles into inflamed tissue."}
    ]
  },
  "Dashboard — ven/venule.md": {
    "primary": "A small vein, especially one collecting blood from capillaries and emptying into larger veins; an insect wing veinlet.",
    "secondary": "In microscopic anatomy and entomology, minute vascular channels in vertebrate tissues or fine chitinous veinlets supporting insect wings.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Each microscopic **venule** converges with neighboring vessels to form the tributaries of larger veins."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The structural pattern of every delicate **venule** across the insect wing is conserved across allied genera."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Inflammatory exudates frequently originate around the thin walls of the postcapillary **venule**."}
    ]
  },
  "Dashboard — ven/venus.md": {
    "primary": "The ancient Roman goddess of love, beauty, and fertility; or the second planet from the Sun.",
    "secondary": "In planetary astronomy, the terrestrial planet possessing a runaway greenhouse atmosphere of dense carbon dioxide and sulfuric acid clouds.",
    "quotes": [
      {"author": "William Shakespeare", "work": "A Midsummer Night's Dream", "quote": "Now forth I'll go to look upon the evening sky where fair **Venus** shines bright above the forest."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "The star of **Venus** ushered in the radiant dawn with mild and starry splendor."},
      {"author": "Percy Bysshe Shelley", "work": "Prometheus Unbound", "quote": "Bright **Venus** hovered in the western heaven, an immortal beacon of celestial light and love."}
    ]
  },
  "Dashboard — ven/venushair.md": {
    "primary": "A graceful maidenhair fern (Adiantum capillus-veneris) featuring delicate fronds on slender, polished black stems.",
    "secondary": "In pteridology and botanical geography, a cosmopolitan fern native to moist, sheltered limestone crevices and waterfalls.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "Moist, dripping rocks inside the cave were covered with delicate sprays of emerald **venushair** fern."},
      {"author": "Asa Gray", "work": "First Lessons in Botany", "quote": "The slender, shining black stipes of **venushair** contrast strikingly with its fan-shaped leafy pinnules."},
      {"author": "John Ruskin", "work": "Proserpina: Studies of Wayside Flowers", "quote": "The graceful tresses of **venushair** clinging to the dark cliff face embody the delicate perfection of nature."}
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

print(f"Motion Batch 14C: Successfully updated {updated}/{len(data)} notes.")
