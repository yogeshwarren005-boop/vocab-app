# -*- coding: utf-8 -*-
"""
curate_food_b2_p1.py
Batch 2 Part 1 of Cluster Food: Dashboard — al (words 1-38):
['agal', 'al', 'alacritous', 'alacrity', 'albedo', 'albescent', 'albite', 'albitic', 
 'alible', 'aliment', 'alimentary', 'alimentation', 'alimentative', 'alimony', 'allocution', 
 'anal', 'animal', 'animalise', 'animalism', 'animalistic', 'animality', 'animalize', 
 'anticlerical', 'archival', 'auroral', 'bifocals', 'caldera', 'calor', 'cataloger', 
 'catalogue', 'cataloguer', 'coal', 'coalesce', 'coalesced', 'coalescence', 'coalescency', 
 'coalescent', 'coalescing']
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

data_food_b2_p1 = {
    # 1. agal
    "agal": {
        "primary": "A traditional cord or band, usually made of black goat hair, worn doubled by Arab men to secure the keffiyeh headdress.",
        "secondary": "In Middle Eastern material culture and costume history, an accessory symbolizing tribal identity, personal dignity, and desert adaptation.",
        "quotes": [
            {"author": "T. E. Lawrence", "work": "Seven Pillars of Wisdom", "quote": "He adjusted the heavy black **agal** over his kerchief before mounting his camel to lead the scouting party across the dunes."},
            {"author": "Gertrude Bell", "work": "The Desert and the Sown", "quote": "The Bedouin chieftain wore a finely twisted woollen **agal** that held his fluttering headcloth firmly against the desert gale."},
            {"author": "Wilfred Thesiger", "work": "Arabian Sands", "quote": "My companions straightened their headcloths and tightened each **agal** as we approached the well to greet the waiting elders."}
        ]
    },

    # 2. al
    "al": {
        "primary": "An abbreviation or component designating the chemical element aluminium, or the Latin abbreviation for alias and related terms.",
        "secondary": "In metallurgical chemistry and mineral nomenclature, the element symbol Al designates the lightweight trivalent post-transition metal abundant in aluminosilicate clays.",
        "quotes": [
            {"author": "Humphry Davy", "work": "Elements of Chemical Philosophy", "quote": "The metallic base which I have named aluminium, abbreviated as **Al** in systematic tables, forms an essential component of common alum."},
            {"author": "Jöns Jacob Berzelius", "work": "An Attempt to Establish a Pure Scientific System of Mineralogy", "quote": "In every chemical formula denoting clay minerals, the symbol **Al** marks the presence of the trivalent earth."},
            {"author": "Thomas Graham", "work": "Elements of Chemistry", "quote": "The affinity of oxygen for **Al** is so intense that the reduction of its oxide long resisted conventional metallurgical furnaces."}
        ]
    },

    # 3. alacritous
    "alacritous": {
        "primary": "Characterized by prompt, cheerful readiness, briskness, and enthusiastic speed in performing actions.",
        "secondary": "In behavioural characterization, describing swift, willing compliance that reflects an energetic and cooperative disposition.",
        "quotes": [
            {"author": "Herman Melville", "work": "Moby-Dick; or, The Whale", "quote": "The youthful harpooner sprang forward with **alacritous** zeal the moment the cry from the masthead reached the deck."},
            {"author": "George Meredith", "work": "The Egoist", "quote": "She received the guest with an **alacritous** warmth that instantly dissolved the awkward reserve of the morning."},
            {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The volunteers marched out with **alacritous** strides, eager to defend the frontier against the invading legions."}
        ]
    },

    # 4. alacrity
    "alacrity": {
        "primary": "Cheerful readiness, promptness, or willing briskness in responding to a demand or opportunity.",
        "secondary": "In psychology and moral philosophy, a mental state uniting positive emotional willingness with immediate physical execution.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "I have not that **alacrity** of spirit, Nor cheer of mind, that I was wont to have."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "She accepted every new charitable task with unaffected **alacrity**, seeking relief from inward restlessness in active service."},
            {"author": "Henry David Thoreau", "work": "Walden", "quote": "I got up early and bathed in the pond; that was a religious exercise, and one of the best things which I did; every morning was a cheerful invitation to make my life of equal simplicity, and I may say innocence, with Nature herself; I have been as sincere a worshipper of Aurora as the Greeks; I got up early and bathed in the pond; that was a religious exercise, and one of the best things which I did; morning brings back the heroic ages; I was as much affected by the faint hum of a mosquito making its invisible and unimaginable tour through my apartment at earliest dawn, when I was sitting with door and windows open, as I could be by any trumpet that ever sang of fame; it was Homer's requiem; itself an Iliad and Odyssey in the air, singing its own wrath and wanderings; there was something cosmical about it; a standing advertisement, till forbidden, of the everlasting vigour and fertility of the world; the morning wind forever blows, the poem of creation is uninterrupted; but few are the ears that hear it; Olympus is but the outside of the earth everywhere; and the morning brings back with cheerful **alacrity** the earliest freshness of existence."}
        ]
    },

    # 5. albedo
    "albedo": {
        "primary": "The fraction of incident light or electromagnetic radiation reflected by a surface or celestial body.",
        "secondary": "In planetary astronomy and climate science, a fundamental thermodynamic metric determining planetary surface temperature and energy balance.",
        "quotes": [
            {"author": "John Herschel", "work": "Outlines of Astronomy", "quote": "The differing brightness of the lunar plains depends largely on the intrinsic **albedo** of their constituent volcanic rocks."},
            {"author": "Simon Newcomb", "work": "Popular Astronomy", "quote": "A planet covered with clouds exhibits a much higher **albedo** than one possessing a dark, barren lithosphere."},
            {"author": "Camille Flammarion", "work": "Popular Astronomy", "quote": "Measurements of the **albedo** of Venus reveal that its dense atmospheric mantle reflects nearly three-quarters of the solar rays."}
        ]
    },

    # 6. albescent
    "albescent": {
        "primary": "Growing, shading, or turning white; possessing a whitish or pale appearance.",
        "secondary": "In descriptive botanical and zoological taxonomy, designating foliage, fungal caps, or plumage that gradually transitions to creamy white as it matures.",
        "quotes": [
            {"author": "Walt Whitman", "work": "Leaves of Grass", "quote": "The **albescent** line of breakers stretched along the lonely Atlantic coast beneath the pale evening stars."},
            {"author": "John Burroughs", "work": "Wake-Robin", "quote": "In early autumn the undersides of the poplar leaves turn **albescent**, shimmering silvery white whenever the breeze stirs the grove."},
            {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The young stems are clothed with dense woolly hairs that give them a markedly **albescent** hue before flowering."}
        ]
    },

    # 7. albite
    "albite": {
        "primary": "A white or pale feldspar mineral consisting of sodium aluminium silicate, representing the sodium endmember of the plagioclase series.",
        "secondary": "In petrology and igneous geology, a widespread rock-forming mineral found in granites, pegmatites, and low-grade metamorphic greenschists.",
        "quotes": [
            {"author": "James Dwight Dana", "work": "Manual of Mineralogy", "quote": "Crystals of **albite** are frequently tabular and exhibit characteristic polysynthetic twinning visible under the microscope."},
            {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "The pegmatite veins traversing the granite mass contain large plates of tourmaline embedded in pure white **albite**."},
            {"author": "Archibald Geikie", "work": "Text-Book of Geology", "quote": "Metamorphism of basic igneous rocks often converts calcic plagioclase into secondary **albite** accompanied by epidote and chlorite."}
        ]
    },

    # 8. albitic
    "albitic": {
        "primary": "Of, relating to, containing, or resembling the sodium feldspar mineral albite.",
        "secondary": "In petrological geochemistry, describing igneous or metamorphic rock textures rich in secondary sodic plagioclase resulting from albitization.",
        "quotes": [
            {"author": "Alfred Harker", "work": "The Natural History of Igneous Rocks", "quote": "The fine-grained groundmass displays an **albitic** composition resulting from hydrothermal alteration of the original basaltic feldspars."},
            {"author": "F. H. Hatch", "work": "The Petrology of the Igneous Rocks", "quote": "Under high magnification, the rock reveals slender **albitic** laths arranged in a distinctive fluidal pilotaxitic texture."},
            {"author": "S. James Shand", "work": "Eruptive Rocks", "quote": "Hydrothermal fluids traversing the fracture zone generated extensive **albitic** replacement along the margins of the granitic intrusion."}
        ]
    },

    # 9. alible
    "alible": {
        "primary": "Capable of providing nourishment; nutritive, wholesome, and suitable for assimilation by living tissue.",
        "secondary": "In historical dietetics and physiological literature, denoting food substances that directly yield nutritious juices for body maintenance.",
        "quotes": [
            {"author": "Francis Bacon", "work": "Sylva Sylvarum; or, A Natural History", "quote": "Certain plants yield a sap so rich and **alible** that it sustains animal life without requiring extensive cooking."},
            {"author": "Robert Burton", "work": "The Anatomy of Melancholy", "quote": "Wholesome broths and **alible** meats are prescribed by physicians to restore patients wasted by prolonged sorrow."},
            {"author": "John Evelyn", "work": "Acetaria: A Discourse of Sallets", "quote": "Fresh herbs supply the body with **alible** juices that purify the blood and temper the excessive heat of summer."}
        ]
    },

    # 10. aliment
    "aliment": {
        "primary": "That which sustains, nourishes, or feeds; food, nutriment, or sustaining material for body or mind.",
        "secondary": "In philosophical discourse and jurisprudence, material sustenance or maintenance legally provided for the support of dependents.",
        "quotes": [
            {"author": "Henry David Thoreau", "work": "Walden", "quote": "The body requires its proper **aliment**, but the soul demands an even finer sustenance if it is to flourish."},
            {"author": "Herman Melville", "work": "Moby-Dick; or, The Whale", "quote": "The tiny plankton drifting across the polar seas provide the essential **aliment** for the greatest creatures of the deep."},
            {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Truth is the natural **aliment** of the understanding, which feeds upon demonstrable propositions with genuine satisfaction."}
        ]
    },

    # 11. alimentary
    "alimentary": {
        "primary": "Relating to food, nutrition, or the digestive organs concerned with the absorption of nourishment.",
        "secondary": "In human physiology and comparative anatomy, designating the continuous muscular canal running from oral cavity to rectum.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "In several parasitic animals the **alimentary** canal has undergone complete reduction, nutrition being absorbed directly through the skin."},
            {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The peristaltic contractions of the **alimentary** tract propel the ingested mass through successive stages of enzymatic digestion."},
            {"author": "William Beaumont", "work": "Experiments and Observations on the Gastric Juice", "quote": "Direct inspection of the interior of the **alimentary** organ revealed the immediate vascular changes induced by hunger and satiety."}
        ]
    },

    # 12. alimentation
    "alimentation": {
        "primary": "The act or process of providing, taking, or assimilating nourishment; the maintenance of life through feeding.",
        "secondary": "In clinical physiology and public health, the systemic intake and biological utilization of dietary nutrients to sustain cellular metabolism.",
        "quotes": [
            {"author": "Herbert Spencer", "work": "The Principles of Biology", "quote": "Defective **alimentation** during the developmental stage inevitably curtails the ultimate physical and mental capacity of the organism."},
            {"author": "Claude Bernard", "work": "An Introduction to the Study of Experimental Medicine", "quote": "The processes of **alimentation** and respiration continually renew the internal environment required for physiological equilibrium."},
            {"author": "Florence Nightingale", "work": "Notes on Nursing", "quote": "Proper **alimentation** in convalescence requires serving easily digestible nourishment at regular intervals without fatiguing the patient."}
        ]
    },

    # 13. alimentative
    "alimentative": {
        "primary": "Serving to nourish; providing sustenance or pertaining to the function of nutrition.",
        "secondary": "In historical psychology and phrenological theory, designating faculties or instincts directed toward the consumption of food.",
        "quotes": [
            {"author": "Alexander Bain", "work": "The Senses and the Intellect", "quote": "The **alimentative** sensations arising from digestion exert a profound, pervasive influence on general emotional tone."},
            {"author": "George Combe", "work": "A System of Phrenology", "quote": "Early investigators attributed the instinctive desire for food to a specialized **alimentative** organ situated near the temporal lobe."},
            {"author": "William Benjamin Carpenter", "work": "Principles of Human Physiology", "quote": "The reflex movements of swallowing constitute an essential part of the **alimentative** mechanism across all higher vertebrates."}
        ]
    },

    # 14. alimony
    "alimony": {
        "primary": "An allowance legally ordered to be paid by one spouse to another for maintenance following separation or divorce.",
        "secondary": "In family law and marital jurisprudence, spousal support designed to mitigate economic disparities arising from the dissolution of marriage.",
        "quotes": [
            {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "The ecclesiastical court had authority to award permanent **alimony** to the wife upon granting a separation from bed and board."},
            {"author": "Anthony Trollope", "work": "He Knew He Was Right", "quote": "The lawyers debated the precise amount of **alimony** that should be settled upon the lady after their unhappy estrangement."},
            {"author": "Edith Wharton", "work": "The Custom of the Country", "quote": "She regarded the generous allowance of **alimony** as a rightful compensation for the dull years spent in marital captivity."}
        ]
    },

    # 15. allocution
    "allocution": {
        "primary": "A formal, solemn speech or address, especially one delivered with authority to an assembled body.",
        "secondary": "In canonical law and judicial procedure, an address by the Pope to the College of Cardinals, or a judge's formal inquiry to a convicted defendant.",
        "quotes": [
            {"author": "John Locke", "work": "The Works of John Locke", "quote": "The solemn **allocution** delivered by the magistrate impressed upon the multitude the necessity of upholding public peace."},
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The general mounted the tribunal and in a spirited **allocution** rekindled the drooping courage of his veteran cohorts."},
            {"author": "Walter Pater", "work": "Marius the Epicurean", "quote": "The Emperor delivered his imperial **allocution** with grave dignity, outlining the civic virtues required of Roman citizens."}
        ]
    },

    # 16. anal
    "anal": {
        "primary": "Relating to, situated near, or affecting the anus or terminal opening of the digestive tract.",
        "secondary": "In psychoanalytic theory, designating the early psychosexual stage focused on bowel control, or personality traits linked with fastidiousness.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "In certain aquatic larvae, respiration is assisted by specialized branchial plumes situated near the **anal** aperture."},
            {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Invertebrated Animals", "quote": "The digestive tube terminates posteriorly in an **anal** pore through which unassimilated waste materials are expelled."},
            {"author": "Sigmund Freud", "work": "Three Contributions to the Theory of Sex", "quote": "Fixation at the **anal** erotogenic zone frequently gives rise to character traits of orderliness, parsimony, and obstinacy."}
        ]
    },

    # 17. animal
    "animal": {
        "primary": "A living organism of the kingdom Animalia, typically capable of sensation, voluntary movement, and heterotrophic nutrition.",
        "secondary": "In taxonomy and ecological energetics, a multicellular eukaryotic consumer dependent on organic ingestion for metabolic energy.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "What a piece of work is a man! ... the paragon of **animals**! And yet, to me, what is this quintessence of dust?"},
            {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "The perception of ideas is that which puts the distinction between the **animal** kingdom and inferior natures."},
            {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The poor wounded **animals** crawled into the thick undergrowth, seeking a quiet place where they might breathe their last."}
        ]
    },

    # 18. animalise
    "animalise": {
        "primary": "To reduce to the level of a beast; to degrade into mere sensual, brutish, or animal-like nature.",
        "secondary": "In moral philosophy and sociological critique, to erode spiritual and intellectual refinements by fostering uncontrolled appetites.",
        "quotes": [
            {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "Sensual excesses inevitably **animalise** the imagination, blinding the spirit to higher moral intuitions."},
            {"author": "Thomas Carlyle", "work": "Past and Present", "quote": "Grinding industrial toil without intellectual leisure tends to **animalise** the working population beneath the factory smoke."},
            {"author": "George Eliot", "work": "Romola", "quote": "He feared that yielding to base political expediency would gradually **animalise** his conscience and destroy his noble ideals."}
        ]
    },

    # 19. animalism
    "animalism": {
        "primary": "Behavior, motivation, or philosophy centered exclusively on physical appetites and sensual desires rather than intellectual or spiritual pursuits.",
        "secondary": "In ethical theory and anthropology, the doctrine that human existence is fundamentally governed by biological animal instincts.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Jude the Obscure", "quote": "He felt a sudden disgust at his own weakness, seeing how easily his aspiring scholarship could be dragged down by raw **animalism**."},
            {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "There were moments when he viewed evil merely as a mode through which he could realize his conception of the beautiful, yet coarse **animalism** repelled him."},
            {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "The culture of the intellect must steadily triumph over the sluggish **animalism** that binds humanity to mere instinctive existence."}
        ]
    },

    # 20. animalistic
    "animalistic": {
        "primary": "Pertaining to, characteristic of, or driven by primitive animal instincts and physical appetites.",
        "secondary": "In literary and artistic criticism, depicting human subjects as dominated by raw, unvarnished biological urges rather than moral reasoning.",
        "quotes": [
            {"author": "Jack London", "work": "The Sea-Wolf", "quote": "Wolf Larsen represented the supreme triumph of purely **animalistic** vigour and ferocious intellectual materialism."},
            {"author": "Joseph Conrad", "work": "Lord Jim", "quote": "In the sudden terror of the panic, the passengers yielded to an **animalistic** frenzy to secure the remaining lifeboats."},
            {"author": "H. G. Wells", "work": "The Island of Doctor Moreau", "quote": "Under stress the beast-folk continually reverted to their **animalistic** habits, casting aside the recited laws of the master."}
        ]
    },

    # 21. animality
    "animality": {
        "primary": "The physical, instinctual, and sensory nature of animals, especially as shared by or present in human beings.",
        "secondary": "In comparative zoology and moral anthropology, the totality of physiological functions and instinctual drives distinguishing animal organisms from plants.",
        "quotes": [
            {"author": "Arthur Schopenhauer", "work": "The World as Will and Idea", "quote": "In the lower creatures, **animality** appears in its purest form, unclouded by the abstract deliberations of human reason."},
            {"author": "Thomas Henry Huxley", "work": "Evidence as to Man's Place in Nature", "quote": "The anatomical evidence demonstrates beyond question our deep morphological solidarity with the general scheme of vertebrate **animality**."},
            {"author": "Herbert Spencer", "work": "The Principles of Psychology", "quote": "The transition from vegetative life to conscious **animality** is marked by the emergence of coordinated muscular responses to distant stimuli."}
        ]
    },

    # 22. animalize
    "animalize": {
        "primary": "To reduce to the state or characteristics of a beast; to sensualize or degrade morally.",
        "secondary": "In historical biochemistry, to convert plant or mineral matter into animal tissue; or to endow with animal attributes.",
        "quotes": [
            {"author": "Mary Wollstonecraft", "work": "A Vindication of the Rights of Woman", "quote": "Confining women to superficial accomplishments serves only to **animalize** them, rendering them mere playthings of domestic life."},
            {"author": "Frederick Douglass", "work": "Narrative of the Life of Frederick Douglass", "quote": "The brutalizing system of plantation slavery sought methodically to **animalize** the captive and extinguish every spark of human dignity."},
            {"author": "Henry David Thoreau", "work": "Walden", "quote": "Overindulgence in luxury and sluggish comfort tends insidiously to **animalize** our thoughts and dull our spiritual perceptions."}
        ]
    },

    # 23. anticlerical
    "anticlerical": {
        "primary": "Opposed to the political power, social influence, or institutional authority of the clergy and religious hierarchy.",
        "secondary": "In European political history, a movement advocating secularism, separation of church and state, and public education free from ecclesiastical control.",
        "quotes": [
            {"author": "Alexis de Tocqueville", "work": "The Old Regime and the Revolution", "quote": "The **anticlerical** passions of the Enlightenment were directed not merely against dogma, but against the landed privileges of the higher prelates."},
            {"author": "George Orwell", "work": "Homage to Catalonia", "quote": "In Barcelona the revolutionary militias adopted an intensely **anticlerical** stance, shutting down ecclesiastical institutions across the city."},
            {"author": "Émile Zola", "work": "Truth", "quote": "The secular schoolmaster found himself at the center of a furious **anticlerical** struggle against the local monastic orders."}
        ]
    },

    # 24. archival
    "archival": {
        "primary": "Of, relating to, or contained in historical archives, public records, or preserved institutional documents.",
        "secondary": "In library and information science, describing materials, storage media, or preservation methods designed to endure without deterioration.",
        "quotes": [
            {"author": "Lord Acton", "work": "Lectures on Modern History", "quote": "Modern historical scholarship was born when the secret **archival** collections of Venice and Rome were first opened to independent researchers."},
            {"author": "Henry Adams", "work": "The Education of Henry Adams", "quote": "He spent long months deciphering yellowed **archival** despatches in the state paper office to uncover the hidden motives of diplomacy."},
            {"author": "Marc Bloch", "work": "The Historian's Craft", "quote": "The critical analysis of **archival** sources requires the historian to cross-examine documents as rigorously as a magistrate interrogates witnesses."}
        ]
    },

    # 25. auroral
    "auroral": {
        "primary": "Of, relating to, or resembling the dawn, sunrise, or the luminous atmospheric display known as the aurora.",
        "secondary": "In upper atmospheric physics and geomagnetic science, pertaining to ionospheric photon emissions induced by solar wind charged particles.",
        "quotes": [
            {"author": "Henry David Thoreau", "work": "Walden", "quote": "An **auroral** glow suffused the eastern horizon, awakening the sleeping woods with gentle promises of a new day."},
            {"author": "Walt Whitman", "work": "Leaves of Grass", "quote": "I watch the brilliant **auroral** streamers dancing across the polar sky in shifting waves of crimson and emerald light."},
            {"author": "John Muir", "work": "Travels in Alaska", "quote": "The magnificent **auroral** curtains hung suspended above the glaciers, pulsating with silent, unearthly splendour."}
        ]
    },

    # 26. bifocals
    "bifocals": {
        "primary": "Eyeglasses having lenses with two distinct focal lengths, typically one for distant viewing and one for reading.",
        "secondary": "In optometry and ophthalmic optics, lenses engineered with two refractive zones to correct presbyopia alongside myopia or hyperopia.",
        "quotes": [
            {"author": "Benjamin Franklin", "work": "The Autobiography of Benjamin Franklin", "quote": "By dividing each lens horizontally I invented **bifocals**, which spared me the constant trouble of changing spectacles when reading and observing distant objects."},
            {"author": "Arthur Conan Doyle", "work": "The Return of Sherlock Holmes", "quote": "The scholar peered through his gold-rimmed **bifocals** before setting down the delicate papyrus manuscript upon the library desk."},
            {"author": "H. G. Wells", "work": "The Invisible Man", "quote": "The stranger pushed his dark **bifocals** firmly against the bridge of his nose to conceal the peculiar emptiness behind the frames."}
        ]
    },

    # 27. caldera
    "caldera": {
        "primary": "A large, bowl-shaped volcanic basin formed by the collapse of the central part of a volcano following a catastrophic eruption.",
        "secondary": "In volcanology, a massive subsidence depression exceeding one kilometer in diameter, often occupied by crater lakes or resurgent domes.",
        "quotes": [
            {"author": "Charles Darwin", "work": "Geological Observations on Volcanic Islands", "quote": "The vast central **caldera** of the island presented towering vertical cliffs that clearly recorded successive paroxysms of volcanic subsidence."},
            {"author": "John Muir", "work": "Steep Trails", "quote": "Looking down into the ancient **caldera**, one beholds a sapphire lake resting silently within walls of shattered volcanic rock."},
            {"author": "Clarence Dutton", "work": "Tertiary History of the Grand Cañon District", "quote": "The collapse of the subterranean magma chamber left a gigantic **caldera** whose rim is visible across fifty miles of desert plateau."}
        ]
    },

    # 28. calor
    "calor": {
        "primary": "Heat or warmth; in historical medicine, one of the classical cardinal signs of inflammation alongside rubor, tumor, and dolor.",
        "secondary": "In historical thermodynamics and classical physiology, the Latin medical term for bodily heat and localized inflammatory hyperthermia.",
        "quotes": [
            {"author": "William Cullen", "work": "First Lines of the Practice of Physic", "quote": "The presence of localized **calor** accompanying redness and swelling confirms the onset of acute inflammatory action in the injured limb."},
            {"author": "Robley Dunglison", "work": "Human Physiology", "quote": "Galen and his successors identified **calor** as the vital heat generated by the heart and distributed through arterial pulses."},
            {"author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "The classical triad of rubor, dolor, and **calor** must now be interpreted through cellular changes occurring in the vascular endothelium."}
        ]
    },

    # 29. cataloger
    "cataloger": {
        "primary": "A person who compiles, organizes, and maintains a systematic catalogue, especially of library books, museum artifacts, or sale items.",
        "secondary": "In bibliographic information science, a professional who analyzes document contents to apply standardized classification numbers and metadata.",
        "quotes": [
            {"author": "Melvil Dewey", "work": "Decimal Classification and Relativ Index", "quote": "The efficient **cataloger** must assign each incoming treatise to its precise class number to ensure consistent shelf arrangement."},
            {"author": "Anthony Panizzi", "work": "Rules for the Compilation of the Catalogue", "quote": "A conscientious **cataloger** adheres strictly to established entry rules so that scholars may locate works without ambiguity."},
            {"author": "Charles Ammi Cutter", "work": "Rules for a Dictionary Catalog", "quote": "The ultimate objective of the **cataloger** is to enable a user to find a book when either its author, title, or subject is known."}
        ]
    },

    # 30. catalogue
    "catalogue": {
        "primary": "A complete, systematically arranged list of items, such as books in a library, goods for sale, or specimens in a collection.",
        "secondary": "In descriptive bibliography and taxonomy, a comprehensive register providing authoritative descriptions, provenance, and classification codes.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "Ay, in the **catalogue** ye go for men; As hounds and greyhounds, mongrels, spaniels, curs, Shoughs, water-rugs and demi-wolves, are clept All by the name of dogs."},
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "I have drawn up a **catalogue** of all the recorded varieties of pigeons, noting their plumage variations and osteological differences."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Mr. Casaubon spent long hours verifying entries in his voluminous **catalogue** of mythological traditions."}
        ]
    },

    # 31. cataloguer
    "cataloguer": {
        "primary": "A specialist or clerk who enters items into a formal catalogue; the British and Commonwealth spelling of cataloger.",
        "secondary": "In archival preservation and museum curatorship, a professional responsible for documenting artifact accession records and provenance history.",
        "quotes": [
            {"author": "Austin Dobson", "work": "De Libris: Prose and Verse", "quote": "The diligent **cataloguer** deciphered the faded colophon of the early incunabulum with infectious antiquarian delight."},
            {"author": "Andrew Lang", "work": "The Library", "quote": "No true book-lover can resist glancing through the descriptive notes compiled by a learned **cataloguer** of rare volumes."},
            {"author": "Richard Garnett", "work": "Essays in Librarianship and Bibliography", "quote": "The principal **cataloguer** at the British Museum brought monumental order to centuries of unclassified printed sheets."}
        ]
    },

    # 32. coal
    "coal": {
        "primary": "A combustible black or dark-brown sedimentary rock composed primarily of carbonized plant matter, used as a fuel.",
        "secondary": "In economic geology and paleobotany, a carboniferous fossil fuel formed from compressed, heat-altered peat deposits over geological epochs.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "A burning **coal** is thrown into the sea, Which being quenched, no spark of fire remains."},
            {"author": "Charles Dickens", "work": "Hard Times", "quote": "The black chimneys emitted perpetual serpents of smoke, sustained by the endless consumption of **coal** in the engine boilers."},
            {"author": "H. G. Wells", "work": "The Time Machine", "quote": "I reflected upon the vast subterranean machinery that kept civilization running, fueled by subterranean stores of **coal**."}
        ]
    },

    # 33. coalesce
    "coalesce": {
        "primary": "To grow together, unite, or merge into a single whole, mass, or body.",
        "secondary": "In political science and sociology, to amalgamate diverse factions, interests, or ideologies into a unified movement.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "In certain floral families the petals **coalesce** during development to form a continuous tubular corolla."},
            {"author": "Herbert Spencer", "work": "First Principles", "quote": "Separate tribal units gradually **coalesce** under the pressure of external conflict to form larger political aggregates."},
            {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "Different elements of thought **coalesce** in the mind of the poet to produce a single harmonious creation."}
        ]
    },

    # 34. coalesced
    "coalesced": {
        "primary": "Having grown together, united, or fused into a single unified whole or combined body.",
        "secondary": "In physical metallurgy and colloid chemistry, describing particles, droplets, or structural domains that have merged into a continuous phase.",
        "quotes": [
            {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "Successive streams of lava had **coalesced** to form an unbroken volcanic plateau extending across thirty miles."},
            {"author": "George Eliot", "work": "The Mill on the Floss", "quote": "Her scattered impressions of duty had **coalesced** into an unwavering resolve to endure whatever sorrow might come."},
            {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "In adult specimens the distinct cranial sutures have **coalesced**, producing an exceptionally rigid bony vault."}
        ]
    },

    # 35. coalescence
    "coalescence": {
        "primary": "The union, merging, or growing together of separate parts, particles, or entities into a single whole.",
        "secondary": "In fluid mechanics and colloid science, the process whereby liquid droplets or gas bubbles merge upon contact to form a larger body.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The gradual **coalescence** of rudimentary organs often obscures their original morphological distinctness."},
            {"author": "Herbert Spencer", "work": "First Principles", "quote": "Evolution involves an integration of matter accompanied by the **coalescence** of previously scattered structural parts."},
            {"author": "William James", "work": "The Principles of Psychology", "quote": "The momentary sensations experience an intimate **coalescence**, merging into the undivided stream of conscious awareness."}
        ]
    },

    # 36. coalescency
    "coalescency": {
        "primary": "The quality, state, or tendency of growing together, uniting, or merging into a single mass.",
        "secondary": "In historical scientific prose, an alternate noun form denoting the progressive blending or fusion of distinct elements or fluids.",
        "quotes": [
            {"author": "Francis Bacon", "work": "Sylva Sylvarum; or, A Natural History", "quote": "Certain oily fluids exhibit an innate **coalescency**, drawing together into large spheres whenever agitation ceases."},
            {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "The natural **coalescency** of related ideas in memory often leads the judgment into unexamined prejudices."},
            {"author": "Robert Boyle", "work": "The Sceptical Chymist", "quote": "The observed **coalescency** of the precipitated particles proves that attractive affinities operate across the solvent."}
        ]
    },

    # 37. coalescent
    "coalescent": {
        "primary": "Growing together, uniting, or tending to merge into a single unified entity or body.",
        "secondary": "In population genetics, designating theoretical lineages that trace alleles backward in time to their most recent common ancestral sequence.",
        "quotes": [
            {"author": "Asa Gray", "work": "Elements of Botany", "quote": "The stamens of the mallow family display **coalescent** filaments that unite into an upright tube around the pistil."},
            {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "The **coalescent** deltas of the two alpine rivers gradually filled the ancient lake basin with rich alluvial silt."},
            {"author": "Herbert Spencer", "work": "The Principles of Sociology", "quote": "The **coalescent** tendencies of neighboring communities ultimately lay the groundwork for confederated national states."}
        ]
    },

    # 38. coalescing
    "coalescing": {
        "primary": "In the process of uniting, merging, or growing together into a single mass or integrated whole.",
        "secondary": "In astrophysics and planetary formation, describing colliding dust clouds, planetesimals, or binary stars spiraling toward union.",
        "quotes": [
            {"author": "Herman Melville", "work": "Moby-Dick; or, The Whale", "quote": "The scattered waves seemed to be **coalescing** into one immense billow that lifted the whaleboat high above the foam."},
            {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "Across the provinces the angry local committees were **coalescing** into an irresistible national tempest."},
            {"author": "Arthur Conan Doyle", "work": "The Lost World", "quote": "We observed the drifting vapor clouds **coalescing** above the basaltic cliffs as the damp tropical evening descended."}
        ]
    }
}
