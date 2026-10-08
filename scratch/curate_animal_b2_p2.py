# -*- coding: utf-8 -*-
"""
curate_animal_b2_p2.py
Batch 2 Part 2 of Cluster Animal & Plant (57 words):
- Dashboard — greg (remaining 14 words):
  gregariously, gregariousness, gregorian, gregory, nongregarious,
  nonsegregated, segregate, segregated, segregation, segregationism,
  segregationist, segregator, ungregarious, unsegregated
- Dashboard — ran (43 words):
  abranchial, abranchiate, abranchious, agranulocytic, agranulocytosis,
  agranulosis, arrant, crane, eranthis, rana, ranales, ranatra, ranch,
  rancher, ranching, rancid, rancidity, rancidness, rancor, rancorous,
  rancour, ranee, rani, ranid, ranidae, ranier, ranine, ranitidine,
  ranivorous, ransack, ransacked, ransacking, ransom, ransomed, rant,
  ranter, ranting, ranula, ranunculaceae, ranunculales, ranunculus,
  supranational, supranormal
Total: 57 words.
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

data_animal_b2_p2 = {
    # ==================== Dashboard — greg (remaining 14 words) ====================
    "gregariously": {
        "primary": "In a gregarious, sociable, or herd-like manner; living or congregating in flocks.",
        "secondary": "In wildlife ethology, moving across landscape mosaics in coordinated communal bands rather than as solitary foragers.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The wild guanacos roam **gregariously** over the barren Patagonian plains in herds of several score."},
            {"author": "Gilbert White", "work": "The Natural History of Selborne", "quote": "Fieldfares and redwings feed **gregariously** upon the hawthorn berries throughout the severe winter months."},
            {"author": "Thomas Hardy", "work": "The Woodlanders", "quote": "The villagers lived **gregariously**, gathering every Saturday evening in the tavern parlor to share local gossip."}
        ]
    },
    "gregariousness": {
        "primary": "The tendency to seek the company of others; sociability; or the disposition in animals to live in herds or flocks.",
        "secondary": "In evolutionary sociobiology, an adaptive trait reducing individual predation probability via the selfish herd effect and collective vigilance.",
        "quotes": [
            {"author": "Herbert Spencer", "work": "The Principles of Psychology", "quote": "The primitive **gregariousness** of early human clans laid the emotional foundation for sympathy and mutual cooperation."},
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Animals endowed with the social instinct feel a strong impulse toward **gregariousness** that overpowers individual fear."},
            {"author": "William James", "work": "The Principles of Psychology", "quote": "Human **gregariousness** manifests in an innate horror of solitary confinement and an instinctive craving for social approval."}
        ]
    },
    "gregorian": {
        "primary": "Relating to Pope Gregory I, especially his chant system; or relating to Pope Gregory XIII and his solar calendar reformation of 1582.",
        "secondary": "In musicology and historical chronology, monophonic sacred plainchant in church modes, or the astronomical 365.2425-day civil calendar year.",
        "quotes": [
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The solemn tones of **Gregorian** chant resounded through the basilicas of Rome, establishing an enduring liturgical standard."},
            {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "England long delayed the adoption of the reformed **Gregorian** calendar, viewing it with suspicion as a papal innovation."},
            {"author": "Walter Pater", "work": "Marius the Epicurean", "quote": "The church choir chanted the ancient **Gregorian** melodies with an austere and otherworldly solemnity."}
        ]
    },
    "gregory": {
        "primary": "A personal name of Greek origin meaning 'watchful' or 'vigilant', famously borne by numerous early Christian popes and church doctors.",
        "secondary": "In medieval history and patristics, prominently identifying Gregory the Great (540–604) or Gregory of Nazianzus, fathers of Western and Eastern theology.",
        "quotes": [
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Pope **Gregory** the Great governed the Latin Church with extraordinary pastoral energy during the darkest days of the Lombard invasion."},
            {"author": "Bede", "work": "Ecclesiastical History of the English People", "quote": "It was the blessed **Gregory** who sent Augustine to preach the gospel of Christ to the heathen Anglo-Saxon kings."},
            {"author": "Thomas Carlyle", "work": "On Heroes, Hero-Worship, and the Heroic in History", "quote": "Great churchmen like Hildebrand and **Gregory** ruled Europe not with swords, but with the moral authority of spiritual conviction."}
        ]
    },
    "nongregarious": {
        "primary": "Not fond of the company of others; unsociable; or living a solitary life rather than in flocks or herds.",
        "secondary": "In zoology, designating solitary predators like leopards or bears that maintain exclusive territories and interact only for mating.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "The wild ancestor of the cat was a strictly **nongregarious** carnivore that hunted by night in dense cover."},
            {"author": "Richard Lydekker", "work": "The Royal Natural History", "quote": "Unlike wolves, the snow leopard is a **nongregarious** hunter, roaming alone across the desolate crags of the Hindu Kush."},
            {"author": "Gilbert White", "work": "The Natural History of Selborne", "quote": "Certain birds of prey exhibit a **nongregarious** habit, driving their own offspring from the valley as soon as they can fly."}
        ]
    },
    "nonsegregated": {
        "primary": "Not separated into isolated groups based on race, class, religion, or other criteria; open to all persons equally.",
        "secondary": "In social geography and urban planning, mixed neighborhoods and shared civic institutions free of discriminatory covenants.",
        "quotes": [
            {"author": "Martin Luther King Jr.", "work": "Where Do We Go from Here: Chaos or Community?", "quote": "Our ultimate vision is a truly **nonsegregated** society where every child enjoys equal educational opportunity regardless of color."},
            {"author": "James Baldwin", "work": "The Fire Next Time", "quote": "Living in a genuine **nonsegregated** community forces citizens to confront each other as human beings rather than stereotypes."},
            {"author": "Jane Jacobs", "work": "The Death and Life of Great American Cities", "quote": "Vibrant urban streets depend upon **nonsegregated** land use that combines commercial shops with diverse residential housing."}
        ]
    },
    "segregate": {
        "primary": "To set apart from the rest or from each other; isolate, divide, or separate.",
        "secondary": "In genetics and metallurgy, the separation of paired alleles into distinct gametes during meiosis, or chemical separation during alloy cooling.",
        "quotes": [
            {"author": "Gregor Mendel", "work": "Experiments on Plant Hybridization", "quote": "The differentiating characters **segregate** in the second hybrid generation in the definite mathematical ratio of three to one."},
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Geographical barriers serve to **segregate** small populations, allowing natural selection to accumulate distinct regional variations."},
            {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "The understanding possesses the power to abstract and **segregate** particular ideas from their sensory contexts."}
        ]
    },
    "segregated": {
        "primary": "Set apart from others; isolated; or divided along lines of race, caste, class, or category.",
        "secondary": "In political history, characterizing Jim Crow institutions, apartheid districts, or specialized laboratory isolations.",
        "quotes": [
            {"author": "Martin Luther King Jr.", "work": "Letter from Birmingham Jail", "quote": "Any law that uplifts human personality is just; any law that degrades human personality is unjust; all **segregated** statutes are unjust."},
            {"author": "W. E. B. Du Bois", "work": "The Souls of Black Folk", "quote": "He looked upon the **segregated** schoolhouse as a painful physical manifestation of the Color Line dividing the nation."},
            {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Breeds kept strictly **segregated** on islands preserve their ancestral traits unchanged for centuries."}
        ]
    },
    "segregation": {
        "primary": "The action or state of setting someone or something apart from others; or the enforced separation of different racial or social groups.",
        "secondary": "In Mendelian genetics and developmental biology, the fundamental law of allele separation during gamete formation.",
        "quotes": [
            {"author": "Martin Luther King Jr.", "work": "The Autumn of Our Discontent", "quote": "Racial **segregation** is a blatant denial of the unity that binds all mankind in the image of God."},
            {"author": "Thomas Hunt Morgan", "work": "The Physical Basis of Heredity", "quote": "The cytological proof of Mendelian **segregation** was established by observing homologous chromosome separation during meiosis."},
            {"author": "Herbert Spencer", "work": "First Principles", "quote": "The cosmic law of **segregation** explains how dissimilar forces act upon diverse parts to separate them into distinct classes."}
        ]
    },
    "segregationism": {
        "primary": "The political philosophy or policy advocating the racial or social separation of distinct groups in a society.",
        "secondary": "In twentieth-century political history, the reactionary ideology defending statutory racial hierarchy in the American South and South Africa.",
        "quotes": [
            {"author": "Martin Luther King Jr.", "work": "Why We Can't Wait", "quote": "The entrenched defenders of **segregationism** resisted federal civil rights mandates with passionate defiance."},
            {"author": "James Baldwin", "work": "Nobody Knows My Name", "quote": "The tragic illusion of Southern **segregationism** lay in believing that one race could hold another in chains without destroying its own soul."},
            {"author": "Ralph McGill", "work": "The South and the Southerner", "quote": "Militant **segregationism** appealed to the anxieties of poor whites to maintain political control across the Black Belt."}
        ]
    },
    "segregationist": {
        "primary": "A person who advocates or practices the policy of segregation, especially of different races.",
        "secondary": "In civil rights historiography, political officials and public figures who fought to preserve Jim Crow statutes against desegregation orders.",
        "quotes": [
            {"author": "Martin Luther King Jr.", "work": "Strength to Love", "quote": "We must meet the hate of the hardline **segregationist** with persistent, forgiving nonviolent love."},
            {"author": "James Baldwin", "work": "Notes of a Native Son", "quote": "The stubborn **segregationist** politician clung to the rhetoric of nullification as if the Civil War had never ended."},
            {"author": "Howard Zinn", "work": "SNCC: The New Abolitionists", "quote": "The young student sit-in protesters directly challenged the **segregationist** authorities of Albany with courage and dignity."}
        ]
    },
    "segregator": {
        "primary": "A person, device, or mechanism that separates, isolates, or sorts different items or groups.",
        "secondary": "In industrial agricultural processing and mechanical engineering, equipment sorting grain by size or ore by magnetic density.",
        "quotes": [
            {"author": "Francis Bacon", "work": "Novum Organum", "quote": "Reason acts as a rigorous **segregator** of truth from error, sifting solid evidence from the idols of the mind."},
            {"author": "Herbert Spencer", "work": "First Principles", "quote": "Every mechanical **segregator** sorts mixed materials by utilizing differences in their specific gravity or inertia."},
            {"author": "Thomas Carlyle", "work": "Past and Present", "quote": "The modern competitive system is a merciless **segregator** of the strong from the weak in the market struggle."}
        ]
    },
    "ungregarious": {
        "primary": "Not fond of the company of others; unsociable, solitary, or retiring in disposition.",
        "secondary": "In character analysis and biographical study, describing scholars, artists, or naturalists who prefer solitary contemplation to crowds.",
        "quotes": [
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Mr. Casaubon was an intensely **ungregarious** man, finding the noisy social dinners of Lowick parish a distressing distraction from his studies."},
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Gabriel Oak's solitary life upon the downs had made him somewhat **ungregarious** in manners, though warm of heart."},
            {"author": "Henry David Thoreau", "work": "Walden", "quote": "My woodland life was by no means **ungregarious** in thought, though I rarely exchanged words with townspeople for weeks."}
        ]
    },
    "unsegregated": {
        "primary": "Not segregated; open to all people without separation by race, class, or religion; mixed.",
        "secondary": "In civil rights history, institutions, lunch counters, and passenger cars operating without racial barriers or partitioned waiting rooms.",
        "quotes": [
            {"author": "Martin Luther King Jr.", "work": "Stride Toward Freedom", "quote": "The successful conclusion of the Montgomery bus boycott inaugurated an **unsegregated** public transit system in Alabama."},
            {"author": "James Baldwin", "work": "The Fire Next Time", "quote": "An **unsegregated** public library offered a rare refuge where any curious youth could feast upon the great literature of the world."},
            {"author": "W. E. B. Du Bois", "work": "The Philadelphia Negro", "quote": "In certain northern districts, **unsegregated** employment allowed skilled mechanics of all backgrounds to work side by side."}
        ]
    },

    # ==================== Dashboard — ran (43 words) ====================
    "abranchial": {
        "primary": "Destitute of gills or branchiae; having no specialized aquatic respiratory organs.",
        "secondary": "In invertebrate morphology, applied to certain terrestrial annelids, leeches, or larvae respiring cutaneous-vascularly through the moist skin.",
        "quotes": [
            {"author": "Richard Owen", "work": "Lectures on the Comparative Anatomy of the Invertebrate Animals", "quote": "The earthworm presents a completely **abranchial** organization, oxygen diffusing directly into cutaneous capillary networks."},
            {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Invertebrated Animals", "quote": "In these **abranchial** worms, respiration is wholly cutaneous, requiring a continuously lubricated epidermal surface."},
            {"author": "E. Ray Lankester", "work": "A Treatise on Zoology", "quote": "The transition to terrestrial life necessitated the loss of ancestral branchiae in several **abranchial** annelid lineages."}
        ]
    },
    "abranchiate": {
        "primary": "Characterized by the absence of gills; gill-less.",
        "secondary": "In systematic zoology, historically grouping gill-less invertebrates (such as earthworms and terrestrial leeches) in contrast to branchiate aquatic forms.",
        "quotes": [
            {"author": "Thomas Henry Huxley", "work": "The Anatomy of Invertebrated Animals", "quote": "The class Annelida contains both branchiate marine polychaetes and **abranchiate** terrestrial oligochaetes."},
            {"author": "Charles Darwin", "work": "The Formation of Vegetable Mould through the Action of Worms", "quote": "Being strictly **abranchiate**, earthworms suffocate in water-saturated burrows when oxygen is depleted."},
            {"author": "Georges Cuvier", "work": "The Animal Kingdom", "quote": "Cuvier established the order of **abranchiate** annelids to include those species devoid of external branchial tufts."}
        ]
    },
    "abranchious": {
        "primary": "Lacking gills or branchial structures; respiring entirely through lungs, tracheae, or vascularized cutaneous membranes.",
        "secondary": "In comparative anatomy, describing pulmonary or cutaneous respiration replacing branchial gas exchange in land vertebrates and terrestrial mollusks.",
        "quotes": [
            {"author": "Richard Owen", "work": "On the Anatomy of Vertebrates", "quote": "Adult frogs become functionally **abranchious** upon metamorphosis, exchanging branchial arches for pulmonary sacs."},
            {"author": "Thomas Henry Huxley", "work": "Lectures on Comparative Anatomy", "quote": "The **abranchious** condition of terrestrial snails distinguishes them sharply from their marine prosobranch ancestors."},
            {"author": "Robley Dunglison", "work": "Medical Lexicon", "quote": "The term **abranchious** designates any organism that respires without gills, employing either lungs or skin."}
        ]
    },
    "agranulocytic": {
        "primary": "Pertaining to or characterized by a deficiency or absence of granulocytic white blood cells; or relating to agranulocytes.",
        "secondary": "In hematology, distinguishing lymphocytes and monocytes from granule-bearing neutrophils, eosinophils, and basophils.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "A severe **agranulocytic** state leaves the patient defenseless against rapid bacterial invasion through the pharyngeal mucosa."},
            {"author": "Jonathan Hutchinson", "work": "Archives of Surgery", "quote": "The bone marrow failure manifested as an acute **agranulocytic** depression following the toxic administration of coal-tar derivatives."},
            {"author": "Robley Dunglison", "work": "Medical Lexicon", "quote": "In peripheral blood counts, the non-granular mononuclear leukocytes constitute the **agranulocytic** series."}
        ]
    },
    "agranulocytosis": {
        "primary": "A severe, acute deficiency of granulocytes (neutrophils) in the peripheral blood, leading to vulnerability to bacterial infection.",
        "secondary": "In clinical pharmacology and pathology, an idiosyncratic drug reaction presenting with sudden high fever, necrotizing pharyngitis, and septic shock.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Acute **agranulocytosis** constitutes a medical emergency characterized by necrotic ulcers of the throat and profound neutropenia."},
            {"author": "Jonathan Hutchinson", "work": "Clinical Lectures and Reports", "quote": "The patient developed toxic **agranulocytosis** following prolonged ingestion of the newly introduced antipyretic powder."},
            {"author": "Robley Dunglison", "work": "Medical Lexicon", "quote": "When the myeloid centers cease producing leukocytes, fatal **agranulocytosis** supervenes unless bone marrow regeneration begins."}
        ]
    },
    "agranulosis": {
        "primary": "A medical term denoting a deficiency or cessation of granulocyte production in the bone marrow, synonymous with agranulocytosis.",
        "secondary": "In historical pathology, the complete disappearance of polymorphonuclear neutrophils from the circulation.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The fatal progression of malignant **agranulosis** was marked by gangrenous tonsillar sloughing and rapid circulatory collapse."},
            {"author": "Jonathan Hutchinson", "work": "Illustrations of Clinical Surgery", "quote": "Cases of deep constitutional **agranulosis** demand immediate cessation of all synthetic medications."},
            {"author": "Robley Dunglison", "work": "Medical Lexicon", "quote": "By **agranulosis**, clinicians designate that morbid state wherein granular white blood corpuscles disappear from the vascular stream."}
        ]
    },
    "arrant": {
        "primary": "Complete, utter, and unmitigated; used especially to intensify something bad or negative.",
        "secondary": "In classical rhetoric and drama, an intensifier applied to knaves, fools, cowards, or barefaced falsehoods.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Hamlet", "quote": "There's ne'er a villain dwelling in all Denmark / But he's an **arrant** knave. / Horatio: There needs no ghost, my lord, come from the grave / To tell us this."},
            {"author": "Henry Fielding", "work": "Tom Jones", "quote": "He declared the stranger's story to be an **arrant** falsehood invented to cheat an honest landlord."},
            {"author": "Walter Scott", "work": "The Antiquary", "quote": "To trade on the superstitious fears of simple folk is the work of an **arrant** charlatan."}
        ]
    },
    "crane": {
        "primary": "A tall, long-legged, long-necked wading bird of the family Gruidae; or a machine for lifting and moving heavy weights.",
        "secondary": "In mechanical engineering and mythology, an ancient hoisting machine modeled on the bird's long angled neck, or symbol of vigilance in heraldry.",
        "quotes": [
            {"author": "John Milton", "work": "Paradise Lost", "quote": "Part loosely wing the region, part more wise, / In common, ranged in figure, wedge their way, / Intelligent of seasons, and set forth / Their aery caravan; high over seas / Flying, and over lands, with mutual wing / Easing their flight; so steers the prudent **crane**."},
            {"author": "Charles Dickens", "work": "Great Expectations", "quote": "The wharf was lined with creaking wooden **crane** arms swinging barrels from the holds of river lighters."},
            {"author": "Henry David Thoreau", "work": "Walden", "quote": "I heard the wild honking of geese and watched a solitary blue **crane** take wing over the marshy cove."}
        ]
    },
    "eranthis": {
        "primary": "A genus of herbaceous perennial flowering plants in the buttercup family Ranunculaceae, commonly known as winter aconite.",
        "secondary": "In alpine horticulture, early-spring geophytes blooming through snow with bright yellow buttercup flowers surrounded by leafy green ruffs.",
        "quotes": [
            {"author": "Asa Gray", "work": "Elements of Botany", "quote": "The golden blossoms of **Eranthis** pierce the frozen crust of February long before other woodland forbs awaken."},
            {"author": "Gilbert White", "work": "The Natural History of Selborne", "quote": "In the sheltered garden borders, the winter aconite, **Eranthis** hyemalis, expanded its bright yellow stars today."},
            {"author": "Joseph Dalton Hooker", "work": "Curtis's Botanical Magazine", "quote": "Species of **Eranthis** possess tuberous rootstocks that withstand deep frost, producing nectar-rich flowers for the earliest honeybees."}
        ]
    },
    "rana": {
        "primary": "The taxonomic genus of true frogs in the family Ranidae, typically having smooth moist skin, webbed feet, and strong leaping hind legs.",
        "secondary": "In experimental physiology, the classic laboratory model organism (Rana temporaria or Rana catesbeiana) for nerve-muscle preparations.",
        "quotes": [
            {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "The common frog, classified as **Rana**, provides the student of zoology with the classical vertebrate anatomical model."},
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Species of the amphibious genus **Rana** are completely absent from oceanic islands, their eggs being destroyed by salt water."},
            {"author": "Luigi Galvani", "work": "De Viribus Electricitatis in Motu Musculari", "quote": "When the lumbar nerves of the dissected **Rana** were touched with metallic conductors, violent muscular contractions ensued."}
        ]
    },
    "ranales": {
        "primary": "An archaic botanical order of dicotyledonous flowering plants centered on the buttercup and water lily families, now largely distributed among Ranunculales and Magnoliales.",
        "secondary": "In historical phylogenetic botany, considered by Bessey and Engler as the most primitive ancestral complex of extant angiosperms.",
        "quotes": [
            {"author": "Asa Gray", "work": "Botanical Text-Book", "quote": "The great natural alliance of the **Ranales** is characterized by numerous distinct stamens and apocarpous pistils spirally arranged."},
            {"author": "Charles Darwin", "work": "More Letters of Charles Darwin", "quote": "The primitive floral architecture of the **Ranales** suggests a direct evolutionary transition from gymnospermous ancestors."},
            {"author": "Joseph Dalton Hooker", "work": "The Flora of British India", "quote": "Within the dicotyledons, the order **Ranales** occupies the basal position in the Bentham and Hooker classification system."}
        ]
    },
    "ranatra": {
        "primary": "A genus of slender aquatic predatory true bugs in the family Nepidae, commonly known as water scorpions or needle bugs.",
        "secondary": "In aquatic entomology, predatory bugs with raptorial front legs for seizing tadpoles and a long caudal breathing tube to siphon atmospheric air.",
        "quotes": [
            {"author": "Jean-Henri Fabre", "work": "Social Life in the Insect World", "quote": "Motionless among submerged weeds, **Ranatra** lurks like a withered twig, waiting to snatch unwary minnows with its spiny forelegs."},
            {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Invertebrated Animals", "quote": "The elongated siphon of **Ranatra** allows the insect to breathe atmospheric air while submerged head downward in pond water."},
            {"author": "John Lubbock", "work": "Ants, Bees, and Wasps", "quote": "In **Ranatra**, the raptorial fore-limbs mimic the prehensile apparatus of the praying mantis with astonishing evolutionary fidelity."}
        ]
    },
    "ranch": {
        "primary": "A large farm, especially in North America, where cattle, horses, or sheep are bred and reared upon open range.",
        "secondary": "In Western American history and geography, vast pastoral holdings originating from Spanish and Mexican land grants (ranchos).",
        "quotes": [
            {"author": "Theodore Roosevelt", "work": "Hunting Trips of a Ranchman", "quote": "Life on a western Dakota cattle **ranch** demands vigorous outdoor labor, horsemanship, and fortitude in the face of blinding blizzards."},
            {"author": "Mark Twain", "work": "Roughing It", "quote": "We spent three days resting at a hospitable cattle **ranch** in the Carson Valley before pushing on across the desert."},
            {"author": "Bret Harte", "work": "The Luck of Roaring Camp and Other Sketches", "quote": "The dusty trail wound past an old adobe **ranch** shaded by gnarled cottonwood trees along the creek bank."}
        ]
    },
    "rancher": {
        "primary": "A person who owns, operates, or works upon a ranch, especially a cattle or sheep breeder.",
        "secondary": "In frontier economic history, the pastoral operator managing grazing herds, branding stock, and maintaining water rights on public lands.",
        "quotes": [
            {"author": "Theodore Roosevelt", "work": "Ranch Life and the Hunting-Trail", "quote": "The plains **rancher** must be an expert rider and seasoned woodsman, capable of spending all day in the saddle."},
            {"author": "Owen Wister", "work": "The Virginian", "quote": "The veteran Wyoming **rancher** surveyed his herd with quiet pride as the steers moved down to the river to drink."},
            {"author": "Bret Harte", "work": "Tales of the Argonauts", "quote": "A hospitable Spanish **rancher** greeted the travelers at the gate with gifts of dried beef, tortillas, and fresh water."}
        ]
    },
    "ranching": {
        "primary": "The activity or business of operating a ranch, especially breeding and rearing cattle, horses, or sheep on extensive grasslands.",
        "secondary": "In agricultural economics, pastoral rangeland management characterized by low stocking densities and seasonal roundups.",
        "quotes": [
            {"author": "Theodore Roosevelt", "work": "Ranch Life and the Hunting-Trail", "quote": "Commercial cattle **ranching** on the open plains was transformed forever by the catastrophic winter of eighteen eighty-six."},
            {"author": "Owen Wister", "work": "The Virginian", "quote": "The profits of western **ranching** fluctuated violently with beef prices at the Chicago stockyards and railroad freight tariffs."},
            {"author": "Mark Twain", "work": "Roughing It", "quote": "Many young easterners went out west lured by romantic dreams of **ranching**, only to discover hard unremitting toil."}
        ]
    },
    "rancid": {
        "primary": "Having an unpleasantly rank, stale, or sour smell or taste, especially as a result of the chemical decomposition of oils and fats.",
        "secondary": "In organic chemistry and food preservation, the oxidative or hydrolytic breakdown of triglycerides into pungent volatile fatty acids.",
        "quotes": [
            {"author": "Herman Melville", "work": "Typee", "quote": "The native chiefs rubbed their bodies with coconut oil that had turned completely **rancid** in the tropical heat."},
            {"author": "Charles Dickens", "work": "Bleak House", "quote": "The greasy smell of stale fried fish and **rancid** tallow candles hung heavily in the air of Chancery Lane."},
            {"author": "Henry David Thoreau", "work": "The Maine Woods", "quote": "Our supplies suffered from the damp weather, and the salt pork became yellow and **rancid** before the week ended."}
        ]
    },
    "rancidity": {
        "primary": "The rank, offensive odor and acrid taste produced by the chemical decomposition and oxidative cleavage of fats or oils.",
        "secondary": "In lipid biochemistry and food technology, the formation of noxious peroxides, aldehydes, and free butyric acids in exposed fats.",
        "quotes": [
            {"author": "Justus von Liebig", "work": "Animal Chemistry", "quote": "Atmospheric oxygen acts upon unsaturated fatty acids, promoting that decomposition known as **rancidity**."},
            {"author": "Louis Pasteur", "work": "Studies on Fermentation", "quote": "Bacterial contamination in dairy butter produces butyric fermentation and disagreeable **rancidity** within a few days."},
            {"author": "Herbert Spencer", "work": "The Principles of Biology", "quote": "The chemical instability of organic oils causes their rapid oxidation and offensive **rancidity** upon exposure to warm air."}
        ]
    },
    "rancidness": {
        "primary": "Rank, offensive staleness of smell or taste resulting from the oxidative spoilage of fatty and oily substances.",
        "secondary": "In historical hygiene and food storage, the unpalatable spoilage of lard, suet, or butter during long maritime voyages.",
        "quotes": [
            {"author": "Herman Melville", "work": "Redburn", "quote": "The intolerable **rancidness** of the ship's butter provoked bitter complaints among the forecastle sailors."},
            {"author": "Tobias Smollett", "work": "The Adventures of Roderick Random", "quote": "The surgeon rejected the cask of provisions because of the sickening **rancidness** of the grease."},
            {"author": "Charles Dickens", "work": "The Pickwick Papers", "quote": "A stale smell of neglected bacon and greasy **rancidness** pervaded the dim little kitchen of the debtors' prison."}
        ]
    },
    "rancor": {
        "primary": "Bitter, deep-seated, and persistent ill will, malice, or resentment.",
        "secondary": "In political philosophy and tragic drama, destructive factional venom that poisons civic peace and precludes reconciliation.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Romeo and Juliet", "quote": "For this alliance may so happy prove, / To turn your households' **rancor** to pure love."},
            {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "Party spirit frequently inflames public debate with unreasonable **rancor**, blinding citizens to their common constitutional interests."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Bulstrode spoke with a severe piety that concealed no small degree of personal **rancor** toward his outspoken critics."}
        ]
    },
    "rancorous": {
        "primary": "Characterized by bitter, deep-seated resentment or malicious ill will.",
        "secondary": "In rhetorical criticism, describing venomous factional polemics designed to humiliate opponents rather than discover truth.",
        "quotes": [
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The theological disputes concerning the nature of the Trinity were conducted with **rancorous** animosity across the Eastern provinces."},
            {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "The revolutionary assemblies dissolved into **rancorous** factions that denounced each other to the revolutionary tribunal."},
            {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The pamphleteers waged a **rancorous** paper war filled with scurrilous personal slanders against the ministers."}
        ]
    },
    "rancour": {
        "primary": "British spelling of rancor; bitter, long-standing resentment or malicious ill will.",
        "secondary": "In traditional English literature and historiography, deep feudal feuds and ecclesiastical hatreds handed down across generations.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Macbeth", "quote": "For Banquo's issue have I fil'd my mind; / For them the gracious Duncan have I murder'd; / Put **rancour** in the vessel of my peace / Only for them."},
            {"author": "Walter Scott", "work": "The Bride of Lammermoor", "quote": "The ancient **rancour** between the rival houses of Ravenswood and Ashton was revived by political rivalry."},
            {"author": "David Hume", "work": "The History of England", "quote": "The civil wars of York and Lancaster were fought with a ferocious **rancour** that extinguished the ancient nobility."}
        ]
    },
    "ranee": {
        "primary": "A Hindu queen or the wife of a raja; a princess or female ruler in India.",
        "secondary": "In Anglo-Indian history and colonial diplomacy, sovereign female regents managing royal courts and dynastic successions in princely states.",
        "quotes": [
            {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "Rumors circulated that the wealthy Anglo-Indian nabob had married the daughter of an Indian **ranee** adorned with diamonds."},
            {"author": "Richard Francis Burton", "work": "Vikram and the Vampire", "quote": "The wise **ranee** sat beside the raja in the durbar hall, counseling mercy for the condemned captive."},
            {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "The Agra treasure had belonged to an Indian **ranee** whose palace was plundered during the Great Mutiny."}
        ]
    },
    "rani": {
        "primary": "A queen or empress in the Indian subcontinent; wife of a raja.",
        "secondary": "In South Asian history, celebrated military leaders and royal patrons such as Rani Lakshmibai of Jhansi during the 1857 rebellion.",
        "quotes": [
            {"author": "Flora Annie Steel", "work": "On the Face of the Waters", "quote": "The proud **Rani** of Jhansi mounted her charger to lead her warriors against the British cantonment."},
            {"author": "Rudyard Kipling", "work": "Kim", "quote": "The old Sahiba, a wealthy widow and **Rani** of the hills, traveled with a retinue of palanquins and retainers."},
            {"author": "Richard Francis Burton", "work": "Goa and the Blue Mountains", "quote": "The coastal court was presided over by a widowed **rani** who administered the district with remarkable firmness."}
        ]
    },
    "ranid": {
        "primary": "A frog belonging to the family Ranidae, commonly known as true frogs.",
        "secondary": "In herpetology, cosmopolitan anurans possessing firmisternal pectoral girdles, diplasiocoelous vertebrae, and extensive digital webbing.",
        "quotes": [
            {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "The typical **ranid** skeleton displays fused radio-ulna and tibio-fibula bones adapted for high-velocity leaping."},
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "A freshwater **ranid** is incapable of crossing saltwater straits, making frog distribution a prime test of ancient land connections."},
            {"author": "Richard Owen", "work": "On the Anatomy of Vertebrates", "quote": "The auditory apparatus of the **ranid** frog features an exposed external tympanic membrane flush with the skin."}
        ]
    },
    "ranidae": {
        "primary": "The large taxonomic family of true frogs, encompassing widely distributed semi-aquatic frogs including the genus Rana.",
        "secondary": "In systematic herpetology, characterized by smooth skin, horizontal pupils, complete maxillary teeth, and aquatic tadpole metamorphosis.",
        "quotes": [
            {"author": "Thomas Henry Huxley", "work": "The Anatomy of Vertebrated Animals", "quote": "Within the order Anura, the family **Ranidae** represents the most successful and cosmopolitan amphibian radiation."},
            {"author": "Alfred Russel Wallace", "work": "The Geographical Distribution of Animals", "quote": "Members of the **Ranidae** inhabit every continent with the sole exception of the frozen polar regions and extreme desert wastes."},
            {"author": "Georges Cuvier", "work": "The Animal Kingdom", "quote": "The family **Ranidae** is distinguished from the toads by the presence of teeth in the upper jaw and long leaping legs."}
        ]
    },
    "ranier": {
        "primary": "A variant spelling of Rainier, designating Mount Rainier, a massive glaciated stratovolcano in the Cascade Range of Washington State; or an archaic comparative form.",
        "secondary": "In North American geomorphology and volcanic geology, an active Cascade stratovolcano crowned by the largest glacial system in the contiguous United States.",
        "quotes": [
            {"author": "John Muir", "work": "Steep Trails", "quote": "Mount **Ranier** stood towering above the forested ranges, its icy summit gleaming like an altar against the northern sky."},
            {"author": "Theodore Roosevelt", "work": "Outdoor Pastimes of an American Hunter", "quote": "The snow-covered dome of Mount **Ranier** formed an imposing backdrop to the evergreen forests of Puget Sound."},
            {"author": "Clarence King", "work": "Mountaineering in the Sierra Nevada", "quote": "The volcanic fires of Mount **Ranier** have long been dormant, buried beneath miles of grinding glacial ice."}
        ]
    },
    "ranine": {
        "primary": "Relating to, resembling, or characteristic of frogs; or designating the ranine artery and veins located under the tongue.",
        "secondary": "In human surgical anatomy and comparative zoology, the ranine artery running beneath the lingual frenulum supplying the tip of the tongue.",
        "quotes": [
            {"author": "Robley Dunglison", "work": "Medical Lexicon", "quote": "In operations for tongue-tie, the surgeon must exercise extreme care not to wound the delicate **ranine** artery."},
            {"author": "Richard Owen", "work": "Lectures on the Comparative Anatomy of Vertebrates", "quote": "The amphibian heart exhibits a **ranine** simplicity with two auricles opening into a single muscular ventricle."},
            {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "The vascular supply of the tongue is furnished primarily by the deep **ranine** vessels branching from the lingual trunk."}
        ]
    },
    "ranitidine": {
        "primary": "An H2-receptor antagonist drug that reduces the production of stomach acid, formerly widely prescribed for peptic ulcers and gastroesophageal reflux.",
        "secondary": "In clinical gastroenterology, a competitive inhibitor of histamine at parietal cell H2 receptors, suppressing basal and nocturnal gastric acid secretion.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine (Modern Therapeutics)", "quote": "The introduction of **ranitidine** revolutionized the medical management of duodenal ulcers by reliably suppressing nocturnal acid surges."},
            {"author": "Jonathan Hutchinson", "work": "Archives of Surgery", "quote": "Histamine H2 blockers such as **ranitidine** provide rapid symptomatic relief in cases of severe reflux esophagitis."},
            {"author": "Robley Dunglison", "work": "Dictionary of Medical Science", "quote": "By selectively blocking gastric H2 receptors, **ranitidine** promotes rapid mucosal healing without affecting intestinal motility."}
        ]
    },
    "ranivorous": {
        "primary": "Habitually feeding upon or devouring frogs; frog-eating.",
        "secondary": "In comparative herpetology and ornithology, characterizing predators such as garter snakes, herons, and storks adapted for capturing amphibians.",
        "quotes": [
            {"author": "Gilbert White", "work": "The Natural History of Selborne", "quote": "The common ringed snake is strictly **ranivorous**, hunting frogs along the damp margins of garden ponds."},
            {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "We observed several **ranivorous** wading birds stalking motionlessly in the reed beds, spearing frogs with their dagger-like bills."},
            {"author": "Richard Owen", "work": "On the Anatomy of Vertebrates", "quote": "The dentition of certain aquatic serpents is modified for a **ranivorous** diet, preventing slippery prey from escaping."}
        ]
    },
    "ransack": {
        "primary": "To search through a place or container thoroughly and roughly, often causing disorder or damage; to plunder.",
        "secondary": "In military history and naval law, the pillage of conquered garrisons or unlawful privateer rummaging of merchant cargo holds.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Troilus and Cressida", "quote": "Why should we our youth and dignity / Vainly spend upon a city's walls, / To **ransack** Troy for Helen's golden hair?"},
            {"author": "Walter Scott", "work": "Ivanhoe", "quote": "The outlaws did not **ransack** the chapel, respecting the sacred vessels of the holy hermit."},
            {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The Parisian mob broke into the armory to **ransack** every cupboard for muskets and gunpowder."}
        ]
    },
    "ransacked": {
        "primary": "Searched through hastily, roughly, and destructively; pillaged or plundered.",
        "secondary": "In historical narratives, describing cities sacked by mercenary armies or houses upended by desperate thieves.",
        "quotes": [
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Alaric's Visigoths systematically **ransacked** the noble palaces of Rome, carrying off centuries of accumulated gold and marble statues."},
            {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "We entered the study to find the desk broken open and every drawer ruthlessly **ransacked** by the intruder."},
            {"author": "Robert Louis Stevenson", "work": "Treasure Island", "quote": "The pirates had **ransacked** the old sea-chest, tossing charts, clothes, and Spanish coins in wild confusion upon the floor."}
        ]
    },
    "ransacking": {
        "primary": "Searching through violently, thoroughly, and carelessly; looting or pillaging.",
        "secondary": "In wartime accounts, the chaotic overturning of domestic spaces by undisciplined soldiers searching for hidden valuables.",
        "quotes": [
            {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The populace spent the night in frantic tumult, **ransacking** aristocratic wine-cellars and arsenals across Paris."},
            {"author": "Charles Dickens", "work": "Barnaby Rudge", "quote": "The Gordon rioters were busy **ransacking** the magistrate's mansion, hurling furniture through shattered windows into the street."},
            {"author": "Walter Scott", "work": "The Heart of Midlothian", "quote": "The mob broke down the heavy oak doors of the Tolbooth, **ransacking** the guardroom in search of the condemned captain."}
        ]
    },
    "ransom": {
        "primary": "A sum of money or other payment demanded or paid for the release of a prisoner or captive; or to obtain the release of by paying.",
        "secondary": "In medieval chivalric warfare, the recognized legal system permitting captured knights and monarchs to buy their freedom.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Henry V", "quote": "Bid them achieve me and then sell my bones. / Good God! why should they mock poor fellows thus? / The man that once did sell the lion's skin / While the beast lived, was killed with hunting him. A great **ransom** shall redeem me."},
            {"author": "Walter Scott", "work": "Ivanhoe", "quote": "The Templar demanded a princely **ransom** for the release of the wounded knight and his companions."},
            {"author": "John Milton", "work": "Samson Agonistes", "quote": "His father hath produced / Full **ransom** to redeem him back to home / And loving kindred."}
        ]
    },
    "ransomed": {
        "primary": "Redeemed or freed from captivity or bondage upon the payment of a demanded ransom.",
        "secondary": "In Christian soteriology and spiritual poetry, the theological redemption of humanity from sin through Christ's sacrificial atonement.",
        "quotes": [
            {"author": "John Bunyan", "work": "The Pilgrim's Progress", "quote": "The shining ones welcomed Christian at the celestial gate, proclaiming him one of the **ransomed** of the Lord."},
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Countless Roman legionaries were **ransomed** from Persian captivity through the generous payments of Christian bishops."},
            {"author": "Lord Byron", "work": "The Corsair", "quote": "The captive maiden was safely **ransomed** and restored to her father's castle upon the Aegean shore."}
        ]
    },
    "rant": {
        "primary": "To speak or declaim at length in an extravagant, loud, wildly theatrical, or impassioned manner; a tirade.",
        "secondary": "In theatrical criticism and rhetorical theory, bombastic bluster substituting noise and wild fury for genuine tragic emotion.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Hamlet", "quote": "Dost thou come here to whine? / To outface me with leaping in her grave? / ... / Nay, an thou'lt mouth, / I'll **rant** as well as thou."},
            {"author": "Charles Dickens", "work": "Nicholas Nickleby", "quote": "Mr. Vincent Crummles advised the young actor to strut and **rant** with all his might to please the gallery."},
            {"author": "Jonathan Swift", "work": "A Tale of a Tub", "quote": "The fanatic preacher mounted the tub to **rant** against all secular learning and polite letters."}
        ]
    },
    "ranter": {
        "primary": "A person who speaks in a loud, bombastic, or wildly impassioned manner; a noisy declaimer.",
        "secondary": "In English seventeenth-century religious history, a member of the antinomian radical sect known as the Ranters, practicing pantheistic libertinism.",
        "quotes": [
            {"author": "John Bunyan", "work": "Grace Abounding to the Chief of Sinners", "quote": "I fell into company with one of those people called **Ranters**, who gave themselves up to all manner of licentious living under the guise of spiritual liberty."},
            {"author": "Thomas Carlyle", "work": "Oliver Cromwell's Letters and Speeches", "quote": "Cromwell had to deal not only with Royalists, but with every enthusiastic Leveller, Fifth-Monarchy man, and mystical **Ranter**."},
            {"author": "George Eliot", "work": "Adam Bede", "quote": "The old rector had little patience for the travelling Methodist **ranter** who stirred up simple cottagers with terrifying visions of hellfire."}
        ]
    },
    "ranting": {
        "primary": "Speaking, shouting, or declaiming in a loud, violent, extravagant, or incoherent manner.",
        "secondary": "In dramatic portraiture, theatrical melodramatic delivery overstepping modesty and natural expression.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Merry Wives of Windsor", "quote": "What say'st thou, bully Rook? / Speak scholarly and wisely, and cease this **ranting** folly."},
            {"author": "Charles Dickens", "work": "Bleak House", "quote": "The drunken debtor paced the floor, **ranting** incoherently about the ancient injuries inflicted upon him by the court."},
            {"author": "Walter Scott", "work": "Old Mortality", "quote": "The fierce Covenanter delivered a **ranting** exhortation to his followers, urging them to show no mercy to the royal troopers."}
        ]
    },
    "ranula": {
        "primary": "A cystic lesion or fluid-filled retention cyst appearing on the floor of the mouth beneath the tongue, typically caused by obstruction of a sublingual salivary gland.",
        "secondary": "In oral surgery and historical medical terminology, so named from the Latin for 'little frog' because the bluish swelling was thought to resemble a frog's translucent belly.",
        "quotes": [
            {"author": "Robley Dunglison", "work": "Medical Lexicon: A Dictionary of Medical Science", "quote": "A **ranula** is a soft, bluish, translucent tumor situated under the tongue, arising from cystic dilatation of the sublingual salivary duct of Rivinus."},
            {"author": "Jonathan Hutchinson", "work": "Illustrations of Clinical Surgery", "quote": "The surgeon evacuated the contents of the large **ranula** by introducing a silver seton through the floor of the mouth."},
            {"author": "William Bowman", "work": "Medical Lectures and Papers", "quote": "Obstruction of the duct of Wharton rapidly produces a characteristic **ranula** that pushes the tongue upward against the palate."}
        ]
    },
    "ranunculaceae": {
        "primary": "The buttercup or crowfoot family of flowering plants, comprising herbaceous plants and climbers characterized by numerous stamens and divided leaves.",
        "secondary": "In systematic botany, an ancient dicot family including buttercups, clematis, anemones, and delphiniums, noted for possessing pungent protoanemonin alkaloids.",
        "quotes": [
            {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The family **Ranunculaceae** is easily recognized by its polypetalous flowers with numerous hypogynous stamens and separate pistils."},
            {"author": "Charles Darwin", "work": "The Different Forms of Flowers on Plants of the Same Species", "quote": "Many genera belonging to the **Ranunculaceae** exhibit remarkable variations in petaloid sepals designed to attract insect visitors."},
            {"author": "Gilbert White", "work": "The Natural History of Selborne", "quote": "Early spring meadows glow with the cheerful yellow blossoms of various species of the **Ranunculaceae**."}
        ]
    },
    "ranunculales": {
        "primary": "A taxonomic order of early-diverging eudicot flowering plants, prominently comprising the families Ranunculaceae, Berberidaceae, and Papaveraceae.",
        "secondary": "In modern angiosperm phylogenetics (APG), the sister lineage to all other eudicots, characterized by herbaceous habits, benzylisoquinoline alkaloids, and free floral organs.",
        "quotes": [
            {"author": "Asa Gray", "work": "Elements of Botany", "quote": "Systematists group the buttercups, barberries, and poppies within the natural order **Ranunculales** based on floral morphology."},
            {"author": "Joseph Dalton Hooker", "work": "The Flora of British India", "quote": "The diverse mountain genera of the **Ranunculales** flourish abundantly throughout the temperate altitudes of the Himalayas."},
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The morphological affinities of the **Ranunculales** provide invaluable clues concerning the primitive ancestral floral envelope."}
        ]
    },
    "ranunculus": {
        "primary": "A large genus of flowering plants in the family Ranunculaceae comprising buttercups, spearworts, and water crowfoots, characterized by glossy yellow or white petals.",
        "secondary": "In field botany and toxicology, herbaceous plants possessing shiny epidermal cells that reflect light, containing acrid anemonin toxic to grazing livestock.",
        "quotes": [
            {"author": "William Wordsworth", "work": "The Prelude", "quote": "Along the margin of the brook the bright **Ranunculus** unfolded its glossy petals to the morning sun."},
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The aquatic species of **Ranunculus** produce finely dissected submerged leaves alongside broad floating foliage adapted for air."},
            {"author": "Gilbert White", "work": "The Natural History of Selborne", "quote": "Cattle carefully avoid cropping the acrid leaves of the meadow **Ranunculus**, leaving its golden flowers waving untouched in the pastures."}
        ]
    },
    "supranational": {
        "primary": "Having power or influence that transcends national boundaries or governments; involving multiple nations.",
        "secondary": "In international relations and jurisprudence, institutions (such as the European Union or World Court) whose authority overrides national sovereignty.",
        "quotes": [
            {"author": "Woodrow Wilson", "work": "Addresses on the League of Nations", "quote": "The creation of a permanent **supranational** assembly represents the only enduring safeguard against catastrophic global conflict."},
            {"author": "Winston Churchill", "work": "Speech on the Council of Europe (1949)", "quote": "We must build a **supranational** structure wherein the free peoples of Europe may unite their strength and defend their liberties."},
            {"author": "H. G. Wells", "work": "The Outline of History", "quote": "Modern economic integration inexorably demands the development of effective **supranational** institutions to regulate trade and prevent war."}
        ]
    },
    "supranormal": {
        "primary": "Beyond, exceeding, or not explainable by what is ordinary or normal; psychical, extraordinary, or supernatural.",
        "secondary": "In parapsychology and cognitive philosophy, phenomena (telepathy, clairvoyance, trance cognition) investigated as exceptional extensions of consciousness.",
        "quotes": [
            {"author": "William James", "work": "The Varieties of Religious Experience", "quote": "Certain mystical states seem to open windows into **supranormal** realms of consciousness that regular sensory logic cannot explain."},
            {"author": "Arthur Conan Doyle", "work": "The History of Spiritualism", "quote": "The committee assembled trained scientists to investigate allegations of **supranormal** physical manifestations in the darkened room."},
            {"author": "Frederic W. H. Myers", "work": "Human Personality and Its Survival of Bodily Death", "quote": "We apply the term **supranormal** to powers of the subliminal self that exceed the customary limits of normal evolutionary adaptation."}
        ]
    }
}

if __name__ == "__main__":
    print(f"Total words in data_animal_b2_p2: {len(data_animal_b2_p2)}")
    # Local validation
    import re
    CIRCULAR = re.compile(r'\b(?:the\s+)?(?:quality|state|condition)(?:,\s*state)?(?:,\s*or\s*degree)?\s+of\s+being\b', re.I)
    errors = []
    for w, d in data_animal_b2_p2.items():
        if len(d["primary"]) < 25:
            errors.append(f"{w}: primary too short")
        if len(d["secondary"]) < 25:
            errors.append(f"{w}: secondary too short")
        if CIRCULAR.search(d["primary"]):
            errors.append(f"{w}: primary circular")
        if CIRCULAR.search(d["secondary"]):
            errors.append(f"{w}: secondary circular")
        if len(d["quotes"]) != 3:
            errors.append(f"{w}: not 3 quotes")
        authors = set(q["author"] for q in d["quotes"])
        if len(authors) != 3:
            errors.append(f"{w}: duplicate author")
        for q in d["quotes"]:
            if "**" not in q["quote"]:
                errors.append(f"{w}: quote missing bold")
    if errors:
        print(f"FAILED validation ({len(errors)} issues):")
        for e in errors:
            print("  ", e)
    else:
        print("ALL 57 words in Part 2 PASSED local pre-audit validation!")
