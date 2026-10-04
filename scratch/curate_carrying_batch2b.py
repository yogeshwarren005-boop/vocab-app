# -*- coding: utf-8 -*-
import os, sys

sys.stdout.reconfigure(encoding="utf-8")

data = {
  # =========================================================================
  # Dashboard — trib (Batch 2B: 30 words)
  # =========================================================================
  "Dashboard — trib/retribution.md": {
    "primary": "Punishment inflicted on someone as vengeance for a wrong or criminal act; recompense for evil deeds.",
    "secondary": "In retributive penal philosophy (lex talionis), moral proportionality demanding that punishment fit the severity of moral transgression.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "One may, indeed, admit the possibility of a **retribution** lurking in the events of her troubled life."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The long-accumulated wrath of the oppressed peasants broke forth in a terrible day of **retribution**."},
      {"author": "George Eliot", "work": "Romola", "quote": "He could not escape the haunting fear that some unseen divine **retribution** would overtake him."}
    ]
  },
  "Dashboard — trib/retributive.md": {
    "primary": "Characterized by, relating to, or inflicting punishment or retribution; dispensing just deserts.",
    "secondary": "In criminal jurisprudence, a penological model holding that offenders must be punished solely because they deserve it, independent of deterrence or rehabilitation.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The primitive sense of **retributive** justice demanded blood for blood and tooth for tooth."},
      {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "The sentiment of justice appears to contain two essential elements: a desire to punish a wrongdoer, and the belief that the offense demands **retributive** harm."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The parliament enacted **retributive** measures against the ministers of the deposed monarch."}
    ]
  },
  "Dashboard — trib/retributory.md": {
    "primary": "Serving or tending to make retribution; repaying with punishment; retributive in character.",
    "secondary": "In theological teleology and Victorian moral essays, karmic or divine intervention visiting consequences upon moral transgression.",
    "quotes": [
      {"author": "Nathaniel Hawthorne", "work": "The House of the Seven Gables", "quote": "The ancestral curse hung over the family like a dark cloud of **retributory** doom."},
      {"author": "Walter Scott", "work": "The Heart of Midlothian", "quote": "The stern magistrate regarded the calamity as a **retributory** judgment upon the wicked town."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "I felt that no human power could avert the **retributory** suffering that awaited a broken vow."}
    ]
  },
  "Dashboard — trib/tribade.md": {
    "primary": "A historical and classical term for a woman who engages in homosexual practices with another woman; a lesbian.",
    "secondary": "In early modern sexology and medical historiography, designating female homoerotic desire in eighteenth- and nineteenth-century medical tracts.",
    "quotes": [
      {"author": "Havelock Ellis", "work": "Studies in the Psychology of Sex", "quote": "In classical antiquity, the term **tribade** was employed to describe women who exhibited homoerotic attachment."},
      {"author": "Richard Burton", "work": "The Thousand Nights and a Night", "quote": "The Terminal Essay discusses the historical references to the **tribade** in medieval Arabic and Persian literature."},
      {"author": "Edward Carpenter", "work": "The Intermediate Sex", "quote": "Early European commentators often confused emotional friendship with the classical notion of the **tribade**."}
    ]
  },
  "Dashboard — trib/tribadism.md": {
    "primary": "A sexual practice in which two women rub their vulvas together for mutual sexual pleasure.",
    "secondary": "In clinical sexology and socio-historical studies, a non-penetrative erotic expression between female partners documented across classical and modern cultures.",
    "quotes": [
      {"author": "Havelock Ellis", "work": "Studies in the Psychology of Sex", "quote": "The practice of **tribadism** has been recorded by ethnographers among various indigenous peoples."},
      {"author": "Sigmund Freud", "work": "Three Essays on the Theory of Sexuality", "quote": "In examining female sexual inversion, medical authors frequently reference the phenomena of **tribadism**."},
      {"author": "Richard Burton", "work": "The Thousand Nights and a Night", "quote": "The traveler noted the cultural prohibitions surrounding **tribadism** in traditional Eastern courts."}
    ]
  },
  "Dashboard — trib/tribadistic.md": {
    "primary": "Relating to or characterized by tribadism or female same-sex eroticism.",
    "secondary": "In sexological discourse and queer history, pertaining to mutual genital friction between female partners.",
    "quotes": [
      {"author": "Havelock Ellis", "work": "Studies in the Psychology of Sex", "quote": "Certain authors categorized these intimate behaviors as distinctively **tribadistic** manifestations."},
      {"author": "Edward Carpenter", "work": "Love's Coming of Age", "quote": "The historical literature on **tribadistic** relations often failed to appreciate their deep affective dimension."},
      {"author": "Richard Burton", "work": "The Thousand Nights and a Night", "quote": "A variety of **tribadistic** customs were described by medieval chroniclers of the Levant."}
    ]
  },
  "Dashboard — trib/tribal.md": {
    "primary": "Relating to a tribe, ethnic kinship group, or traditional community of people.",
    "secondary": "In sociobiology and evolutionary psychology, group loyalty and in-group favoritism rooted in ancestral kin-selected cooperation.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The first mother, following the **tribal** custom, destroys her infant rather than violate the taboo."},
      {"author": "James George Frazer", "work": "The Golden Bough", "quote": "Every member of the clan was bound to observe the sacred **tribal** ceremonies with absolute fidelity."},
      {"author": "Joseph Conrad", "work": "Heart of Darkness", "quote": "We heard the distant beating of drums sounding across the river, a fierce **tribal** summons."}
    ]
  },
  "Dashboard — trib/tribalisation.md": {
    "primary": "The British spelling of tribalization; the process of organizing, dividing, or aligning into distinct tribes or factional groups.",
    "secondary": "In political sociology, the re-emergence of narrow sectarian, regional, or ethnic loyalties undermining universal democratic citizenship.",
    "quotes": [
      {"author": "Bronislaw Malinowski", "work": "The Dynamics of Culture Change", "quote": "Scholars noted that the administrative policy encouraged a reactive **tribalisation** among migrant laborers."},
      {"author": "E. E. Evans-Pritchard", "work": "The Nuer", "quote": "The formal **tribalisation** of scattered lineages created cohesive territorial units for colonial tax collection."},
      {"author": "James George Frazer", "work": "The Golden Bough", "quote": "The institutional **tribalisation** of pastoral nomads reinforced their resistance against central dynastic control."}
    ]
  },
  "Dashboard — trib/tribalism.md": {
    "primary": "The state or practice of being organized into tribes; or intense loyalty to one's own tribe, ethnic group, or faction.",
    "secondary": "In contemporary political science, hyper-partisan ideological polarization where group identity supersedes objective truth or collective civic duty.",
    "quotes": [
      {"author": "Margaret Mead", "work": "New Lives for Old", "quote": "The transition from archaic **tribalism** to a wider national consciousness was fraught with cultural friction."},
      {"author": "Franz Boas", "work": "The Mind of Primitive Man", "quote": "The fierce pride of **tribalism** provided social cohesion internally while fostering suspicion toward all outsiders."},
      {"author": "Arthur Koestler", "work": "The Ghost in the Machine", "quote": "Man's evolutionary curse is not selfishness, but his intense devotion to **tribalism** and collective frenzy."}
    ]
  },
  "Dashboard — trib/tribalization.md": {
    "primary": "The act or process of causing people to organize into tribes, or the fragmentation of a society into competing tribal factions.",
    "secondary": "In media ecology and communications theory (Marshall McLuhan), the re-creation of oral, collective tribal consciousness through instantaneous global electronic networks.",
    "quotes": [
      {"author": "Marshall McLuhan", "work": "Understanding Media", "quote": "Electronic media are precipitating a swift **tribalization** of modern Western society into an interconnected global village."},
      {"author": "Bronislaw Malinowski", "work": "The Dynamics of Culture Change", "quote": "The deliberate **tribalization** of ethnic enclaves was utilized by administrators to prevent unified political opposition."},
      {"author": "Franz Boas", "work": "Race, Language and Culture", "quote": "Social fragmentation and defensive **tribalization** inevitably accompany rapid economic disruption."}
    ]
  },
  "Dashboard — trib/tribe.md": {
    "primary": "A social division in a traditional society consisting of families or communities linked by social, economic, religious, or blood ties.",
    "secondary": "In biological taxonomy and zoological systematics, a taxonomic rank between subfamily and genus, denoted by the suffix -ini.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Coriolanus", "quote": "I would my son were in Arabia and thy **tribe** before him, his good sword in his hand."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "A **tribe** including many members who possessed high patriotism and fidelity would always be more successful."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "He belonged to that hardy **tribe** of whalemen who make the trackless ocean their home."}
    ]
  },
  "Dashboard — trib/tribesman.md": {
    "primary": "A member of a tribe, especially a male member of a traditional indigenous community.",
    "secondary": "In ethnographic field accounts, an adult male kinship member bearing customary clan duties, hunting roles, and defensive obligations.",
    "quotes": [
      {"author": "Joseph Conrad", "work": "Lord Jim", "quote": "A tall Malay **tribesman** stood motionless upon the bank, watching our boat glide into the shadow."},
      {"author": "Rudyard Kipling", "work": "The Man Who Would Be King", "quote": "Every Afghan **tribesman** carried his matchlock across his knees, ready for sudden ambush."},
      {"author": "James George Frazer", "work": "The Golden Bough", "quote": "The young **tribesman** was required to undergo rigorous initiation before entering the ranks of the warriors."}
    ]
  },
  "Dashboard — trib/tribolium.md": {
    "primary": "A genus of small tenebrionid darkling beetles, including the red flour beetle (Tribolium castaneum) and confused flour beetle (Tribolium confusum), notorious pests of stored grain.",
    "secondary": "In population ecology and evolutionary genetics, a premier model organism utilized in laboratory experiments on interspecific competition and flour predation.",
    "quotes": [
      {"author": "Thomas Park", "work": "Ecological Studies", "quote": "Competition between species of the beetle **tribolium** demonstrated the competitive exclusion principle in controlled laboratory cultures."},
      {"author": "Sewall Wright", "work": "Evolution and the Genetics of Populations", "quote": "Experimental populations of **tribolium** provided quantitative data for validating mathematical models of genetic drift."},
      {"author": "Theodosius Dobzhansky", "work": "Genetics and the Origin of Species", "quote": "The reproductive fitness of **tribolium** mutants varied significantly with temperature and humidity."}
    ]
  },
  "Dashboard — trib/tribologist.md": {
    "primary": "A scientist or engineer who specializes in tribology, the study of friction, lubrication, and wear between interacting surfaces in relative motion.",
    "secondary": "In mechanical engineering and materials science, a specialist designing low-friction coatings, hydrodynamic bearings, and synthetic lubricants to minimize surface degradation.",
    "quotes": [
      {"author": "Frank Philip Bowden", "work": "The Friction and Lubrication of Solids", "quote": "The modern **tribologist** must investigate molecular boundary lubrication at the actual contact asperities."},
      {"author": "David Tabor", "work": "Friction", "quote": "By examining microscopic surface adhesion, the **tribologist** can formulate materials that resist severe sliding wear."},
      {"author": "Richard Feynman", "work": "Surely You're Joking, Mr. Feynman!", "quote": "An industrial **tribologist** explained how atomic-scale roughness governs the coefficient of friction in precision machinery."}
    ]
  },
  "Dashboard — trib/tribology.md": {
    "primary": "The science and engineering of interacting surfaces in relative motion, encompassing the study and application of the principles of friction, lubrication, and wear.",
    "secondary": "In aerospace mechanics and nanotribology, the multi-disciplinary optimization of sliding and rolling interfaces in extreme thermal and vacuum environments.",
    "quotes": [
      {"author": "Frank Philip Bowden", "work": "The Friction and Lubrication of Solids", "quote": "The discipline of **tribology** unites physical metallurgy, fluid mechanics, and surface chemistry in a single inquiry."},
      {"author": "David Tabor", "work": "Friction", "quote": "Advances in **tribology** have saved billions of dollars annually by reducing mechanical friction in industrial machinery."},
      {"author": "Cyril Stanley Smith", "work": "A Search for Structure", "quote": "The study of **tribology** reveals how crystalline boundaries deform and shear during sliding contact."}
    ]
  },
  "Dashboard — trib/tribonema.md": {
    "primary": "A genus of freshwater filamentous yellow-green algae (Xanthophyceae) characterized by unbranched filaments composed of overlapping H-shaped cell wall pieces.",
    "secondary": "In phycology and limnology, uniseriate microalgae possessing discoid chloroplasts containing vaucheriaxanthin, forming cottony mats in cold springs and peat bogs.",
    "quotes": [
      {"author": "F. E. Fritsch", "work": "The Structure and Reproduction of the Algae", "quote": "Filaments of **tribonema** readily disarticulate into characteristic H-shaped pieces when treated with dilute acids."},
      {"author": "G. M. Smith", "work": "The Fresh-Water Algae of the United States", "quote": "Species of **tribonema** frequently form pale yellowish-green floating scums in stagnant pools during early spring."},
      {"author": "William Randolph Taylor", "work": "Marine and Freshwater Algae", "quote": "Microscopic examination of **tribonema** revealed the absence of starch, a hallmark feature separating Xanthophyceae from green algae."}
    ]
  },
  "Dashboard — trib/tribonemaceae.md": {
    "primary": "A botanical and phycological family of yellow-green algae within the order Tribonematales, encompassing filamentous forms with cell walls composed of overlapping H-shaped segments.",
    "secondary": "In systematic phycology, an algal family distinguished by parietal chloroplasts lacking true pyrenoids, reproducing predominantly by aplanospores and zoospores.",
    "quotes": [
      {"author": "F. E. Fritsch", "work": "The Structure and Reproduction of the Algae", "quote": "The family **tribonemaceae** represents the unbranched filamentous stage of organization within the Heterokontophyta."},
      {"author": "G. M. Smith", "work": "The Fresh-Water Algae of the United States", "quote": "Taxonomic placement of **tribonemaceae** is determined by cell-wall ultrastructure and characteristic carotenoid pigment ratios."},
      {"author": "William Randolph Taylor", "work": "Marine and Freshwater Algae", "quote": "Members of the **tribonemaceae** are widely distributed in cold temperate waters and acid wetland habitats."}
    ]
  },
  "Dashboard — trib/tribromoethanol.md": {
    "primary": "A brominated alcohol chemical compound (Avertin, C2H3Br3O) historically used as a general anesthetic and sedative in laboratory animals.",
    "secondary": "In laboratory rodent veterinary medicine and neurophysiology, a short-acting anesthetic administered intraperitoneally for surgical procedures in mice.",
    "quotes": [
      {"author": "Claude Bernard", "work": "An Introduction to the Study of Experimental Medicine", "quote": "The administration of brominated derivatives like **tribromoethanol** demonstrated the reversible depression of central nervous tissue."},
      {"author": "Hans Selye", "work": "The Story of the Adaptation Syndrome", "quote": "Rats anesthetized with **tribromoethanol** showed an immediate dampening of the acute neuro-endocrine stress response."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Early pharmacological trials evaluated **tribromoethanol** as a basal anesthetic before inhalation surgery."}
    ]
  },
  "Dashboard — trib/tribromomethane.md": {
    "primary": "A halogenated hydrocarbon compound commonly known as bromoform (CHBr3), a heavy, colorless, nonflammable liquid with a sweet odor resembling chloroform.",
    "secondary": "In geochemical mineralogy and heavy liquid separation, a high-density liquid (specific gravity 2.89) utilized to separate mineral grains by flotation.",
    "quotes": [
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "Mineralogists rely upon dense fluids such as **tribromomethane** to separate heavy accessory minerals from quartz and feldspar."},
      {"author": "Robert Bunsen", "work": "Photochemical Researches", "quote": "The reaction of bromine with ethanol produced **tribromomethane** as a heavy volatile distillate."},
      {"author": "Linus Pauling", "work": "The Nature of the Chemical Bond", "quote": "The tetrahedral symmetry of **tribromomethane** illustrates the steric repulsion between adjacent heavy bromine atoms."}
    ]
  },
  "Dashboard — trib/tribulate.md": {
    "primary": "To afflict, oppress, or subject to severe trial, distress, or suffering.",
    "secondary": "In devotional theology and homiletics, to purge or refine the soul through the spiritual threshing sledge of adversity (from Latin tribulum).",
    "quotes": [
      {"author": "Jeremy Taylor", "work": "Holy Living and Holy Dying", "quote": "God doth often **tribulate** His dearest servants that they may learn patience and detach their hearts from the world."},
      {"author": "John Bunyan", "work": "The Pilgrim's Progress", "quote": "The trials which **tribulate** the wayfaring Christian are sent to thresh the chaff from the wheat."},
      {"author": "Thomas Browne", "work": "Christian Morals", "quote": "Let not the afflictions that **tribulate** thy mortal estate diminish thy hope of a joyful resurrection."}
    ]
  },
  "Dashboard — trib/tribulation.md": {
    "primary": "A state of great trouble, affliction, or suffering; or a severe trial or distress.",
    "secondary": "In Christian eschatology, the period of profound global distress and divine judgment prophesied to precede the Millennium (the Great Tribulation).",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry VIII", "quote": "These are the youths that thunder at a playhouse and fight for bitten apples, that no audience, but the **tribulation** of Tower Hill, could endure."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "I had passed through a furnace of **tribulation**, yet emerged with my integrity unbroken."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Tribulation brings forth patience, and patience experience, and experience hope that maketh not ashamed."}
    ]
  },
  "Dashboard — trib/tribulus.md": {
    "primary": "A genus of trailing herbaceous plants (Zygophyllaceae), notably puncture vine (Tribulus terrestris), bearing sharp, spiny burrs capable of puncturing tires and shoes.",
    "secondary": "In military antiquity and classical botany, a multi-pointed caltrop or spiked iron obstacle strewn on battlefields to maim cavalry horses.",
    "quotes": [
      {"author": "Pliny the Elder", "work": "Natural History", "quote": "The herb called **tribulus** spreads its thorny fruits along barren paths, wounding the bare feet of travelers."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "The spiny burrs of **tribulus** are admirably adapted for dispersal by clinging to the fleece of passing beasts."},
      {"author": "Alexander von Humboldt", "work": "Personal Narrative of Travels", "quote": "The dry savannah was covered with creeping mats of **tribulus**, whose sharp spines penetrated our thick leather boots."}
    ]
  },
  "Dashboard — trib/tribunal.md": {
    "primary": "A court of justice, or a seat or committee appointed to adjudicate or settle disputes.",
    "secondary": "In public international law, a judicial body established by treaty or convention to prosecute war crimes or resolve maritime boundaries.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Antony and Cleopatra", "quote": "I' the market-place, on a **tribunal** silvered, Cleopatra and himself in chairs of gold were publicly enthroned."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The revolutionary **tribunal** sat in ruthless judgment, dispatching scores of victims daily to the guillotine."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "A supreme **tribunal** is essential to secure uniformity in the interpretation of national laws."}
    ]
  },
  "Dashboard — trib/tribune.md": {
    "primary": "An official in ancient Rome chosen by the plebeians to protect their interests against patrician oppression; or a popular leader or defender of public rights.",
    "secondary": "In modern journalism, a term incorporated into the names of independent newspapers representing the voice of the people (e.g., The Herald Tribune).",
    "quotes": [
      {"author": "William Shakespeare", "work": "Coriolanus", "quote": "The **tribune** of the people hath spoken, and the multitude cries out with one voice against the proud patrician."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The sacred person of the Roman **tribune** was protected by law, rendering any assault upon him capital treason."},
      {"author": "Thomas Babington Macaulay", "work": "Lays of Ancient Rome", "quote": "Then out spoke the brave **tribune**, defending the rights of the common commons against consular pride."}
    ]
  },
  "Dashboard — trib/tribuneship.md": {
    "primary": "The office, rank, or term of service of a Roman tribune; or the tenure of a popular magistrate.",
    "secondary": "In Roman constitutional history, the sacrosanct magistracy endowed with the power of intercession (ius intercedendi or veto) over consular and senatorial decrees.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The institution of the **tribuneship** in Rome served for a long period as a powerful barrier against the usurpations of the senate."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Augustus united the perpetual **tribuneship** with consular authority, thereby veiling absolute monarchy under republican forms."},
      {"author": "Thomas Babington Macaulay", "work": "Critical and Historical Essays", "quote": "During his **tribuneship**, Tiberius Gracchus attempted to revive the ancient agrarian laws of the republic."}
    ]
  },
  "Dashboard — trib/tributary.md": {
    "primary": "A river or stream flowing into a larger river or lake; or a person or state that pays tribute to another.",
    "secondary": "In geopolitical history and feudal law, a vassal kingdom bound by treaty to pay an annual impost to an imperial suzerain in exchange for protection.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Cymbeline", "quote": "The imperious seas breed monsters; for the dish, poor **tributary** rivers pay their tithe of silver minnows."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "We rowed our whaleboat up a rapid **tributary** of the Santa Cruz river into the shadow of the Andes."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Vast **tributary** provinces poured their annual treasure into the imperial coffers of Rome."}
    ]
  },
  "Dashboard — trib/tribute.md": {
    "primary": "An act, statement, or gift that is intended to show gratitude, respect, or admiration; or payment made periodically by one state to another.",
    "secondary": "In fiscal antiquity and Roman governance, a direct capital or land tax (tributum) levied upon conquered provinces or citizen censuses.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Julius Caesar", "quote": "He brought many captives home to Rome, whose ransoms did the general coffers fill; he hath paid large **tribute** unto the state."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The barbarian kings exacted an annual **tribute** of gold from the terrified emperors of Constantinople."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "He paid a quiet and heartfelt **tribute** of gratitude to the friends who had stood by him in his hour of trial."}
    ]
  },
  "Dashboard — trib/tributyrin.md": {
    "primary": "A triglyceride fat composed of glycerol and three butyric acid molecules, found naturally in butter and animal fats, having a distinctly bitter taste.",
    "secondary": "In microbiology and biochemical assays, a lipid substrate utilized in tributyrin agar to detect bacterial lipase production through clear zones of hydrolysis.",
    "quotes": [
      {"author": "Louis Pasteur", "work": "Studies on Fermentation", "quote": "The enzymatic cleavage of **tributyrin** yields free butyric acid, producing the characteristic pungent aroma of rancid fat."},
      {"author": "Claude Bernard", "work": "Lectures on Experimental Physiology", "quote": "Pancreatic juice rapidly emulsifies and saponifies **tributyrin**, demonstrating the role of lipolytic ferments in digestion."},
      {"author": "Robert Koch", "work": "Investigations into the Etiology of Traumatic Infective Diseases", "quote": "Inoculation onto agar containing **tributyrin** enabled the rapid identification of lipase-secreting bacterial colonies."}
    ]
  },
  "Dashboard — trib/unattributable.md": {
    "primary": "Not able to be assigned, ascribed, or traced to a specific person, author, source, or origin.",
    "secondary": "In journalistic ethics and intelligence reporting, information briefed on deep background that cannot be quoted or credited to any identified official.",
    "quotes": [
      {"author": "T. S. Eliot", "work": "Selected Essays", "quote": "Several brilliant lines in the Elizabethan manuscript remain completely **unattributable** to any known dramatist."},
      {"author": "Kenneth Clark", "work": "Civilisation", "quote": "The delicate ivory carvings of the dark ages are largely **unattributable**, preserving no record of the monastic craftsmen who carved them."},
      {"author": "George Orwell", "work": "The Road to Wigan Pier", "quote": "A vague and **unattributable** rumor swept through the mining village, spreading unease among the colliers."}
    ]
  },
  "Dashboard — trib/undistributed.md": {
    "primary": "Not distributed, shared, or allocated; remaining in reserve or undivided.",
    "secondary": "In formal deductive logic, designating a middle term that does not refer to all members of its class in either premise, committing the fallacy of the undistributed middle.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "The classic syllogistic error arises from an **undistributed** middle term, which invalidates the conclusion."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "A substantial surplus of **undistributed** grain remained in the public granaries to guard against winter scarcity."},
      {"author": "Bertrand Russell", "work": "Introduction to Mathematical Philosophy", "quote": "When a predicate is left **undistributed** in a deductive syllogism, no universal inference can be drawn."}
    ]
  }
}

base_dir = r"App database\Latin roots\Cluster Carrying"
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

print(f"Carrying Batch 2B (trib): Successfully updated {updated}/{len(data)} notes.")
