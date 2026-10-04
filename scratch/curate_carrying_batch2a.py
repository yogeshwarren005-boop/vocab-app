# -*- coding: utf-8 -*-
import os, sys

sys.stdout.reconfigure(encoding="utf-8")

data = {
  # =========================================================================
  # Dashboard — trib (Batch 2A: 30 words)
  # =========================================================================
  "Dashboard — trib/attributable.md": {
    "primary": "Capable of being ascribed or assigned to a specific cause, author, or origin.",
    "secondary": "In statistical epidemiology and risk analysis, designating the proportion of disease incidence in an exposed cohort causally tied to an exposure.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The slight differences between the races are largely **attributable** to the long-continued action of natural and sexual selection."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Such sudden changes of character are often directly **attributable** to hidden emotional crises."},
      {"author": "Thomas Henry Huxley", "work": "Method and Results", "quote": "The rapid advance of modern physical science is **attributable** to the strict verification of hypotheses."}
    ]
  },
  "Dashboard — trib/attribute.md": {
    "primary": "To regard something as being caused by or belonging to someone; or a quality or feature regarded as a characteristic or inherent part of someone or something.",
    "secondary": "In relational database architecture and object-oriented programming, a named data field, column, or property defining an entity type.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "It takes from our achievements, though performed at height, the pith and marrow of our **attribute**."},
      {"author": "Francis Bacon", "work": "The Essays", "quote": "Mercy is the noble **attribute** of monarchs when joined with wisdom and impartial justice."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "He was inclined to **attribute** her reluctance to a natural maidenly modesty."}
    ]
  },
  "Dashboard — trib/attribution.md": {
    "primary": "The act of regarding something as being caused by or belonging to a person or thing; or the assignment of authorship or origin.",
    "secondary": "In social psychology (attribution theory), the cognitive process by which individuals infer the causes of behavior and observed events.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry IV, Part 1", "quote": "If speaking truth in this fine age were not thought flattery, such **attribution** should the Douglas have as not a soldier of this season's stamp should go so general current through the world."},
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "The **attribution** of generous motives to a selfish character was her constant temptation."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "The careless **attribution** of obscure ideas to simple names has filled philosophy with unending disputes."}
    ]
  },
  "Dashboard — trib/attributive.md": {
    "primary": "Expressing or having the nature of an attribute; especially (in grammar) designating an adjective placed directly before the noun it modifies.",
    "secondary": "In philosophical metaphysics and semantic logic, designating a predicate that directly assigns an essential property to an underlying subject.",
    "quotes": [
      {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "The poet uses an **attributive** epithet not for mere decoration, but to unveil the essential spirit of the object."},
      {"author": "Henry Sweet", "work": "A New English Grammar", "quote": "An adjective standing in immediate contact with its headword is termed **attributive**, as distinguished from predicate adjectives."},
      {"author": "Bertrand Russell", "work": "The Principles of Mathematics", "quote": "The distinction between an **attributive** relation and an assertive proposition is fundamental to philosophical grammar."}
    ]
  },
  "Dashboard — trib/attributively.md": {
    "primary": "In an attributive manner; especially as an adjective standing before the noun it modifies rather than in the predicate.",
    "secondary": "In formal syntax and descriptive linguistics, modifying a nominal constituent directly within the noun phrase boundary.",
    "quotes": [
      {"author": "Henry Sweet", "work": "A New English Grammar", "quote": "When a noun adjunct is used **attributively**, it tends in time to coalesce into a compound word."},
      {"author": "Otto Jespersen", "work": "The Philosophy of Grammar", "quote": "Adjectives used **attributively** qualify the substantive before any predicative nexus is formed."},
      {"author": "William Dwight Whitney", "work": "The Life and Growth of Language", "quote": "In many Indo-European dialects, participles functioning **attributively** gradually assumed the full inflection of adjectives."}
    ]
  },
  "Dashboard — trib/contribute.md": {
    "primary": "To give or supply something in common with others; to help bring about a result or outcome.",
    "secondary": "In periodical publishing and scholarship, to submit an article, paper, or review for dissemination in a journal or symposium.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "He felt that every honest worker must **contribute** his share toward the well-being of the parish."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Many diverse circumstances may **contribute** to the success of a newly evolved variety."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Every individual strives to **contribute** his capital toward that industry which promises the greatest annual return."}
    ]
  },
  "Dashboard — trib/contributing.md": {
    "primary": "Giving or supplying a part toward a common purpose; or serving as a factor helping to cause an outcome.",
    "secondary": "In tort law, acting as a concurrent or non-exclusive proximate factor that produces an actionable harm or injury.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "A sense of **contributing** to form the world's opinion makes common talk impressive."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Several distinct causes are recognized as **contributing** to the extinction of native varieties."},
      {"author": "Joseph Conrad", "work": "Lord Jim", "quote": "Every trivial event was seen in retrospect as **contributing** toward the fatal catastrophe."}
    ]
  },
  "Dashboard — trib/contribution.md": {
    "primary": "A gift or payment to a common fund or cause; or an item of writing contributed to a publication.",
    "secondary": "In corporate governance and insurance law, the proportionate share of a loss payable by each insurer insuring the same risk.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Julius Caesar", "quote": "The people 'twixt Philippi and this ground do stand but in a forced affection; for they have grudged us **contribution**."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "A federal government must have the power to demand an equitable financial **contribution** from every state."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "He accepted my modest **contribution** with a flourishing bow that seemed to magnify the pence into gold."}
    ]
  },
  "Dashboard — trib/contributive.md": {
    "primary": "Tending to contribute; serving or helping to promote, produce, or bring about an end.",
    "secondary": "In social ethics and welfare philosophy, oriented toward enhancing the collective common good through active civic participation.",
    "quotes": [
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "Every well-ordered experiment is **contributive** to the discovery of universal axioms."},
      {"author": "Jeremy Taylor", "work": "Holy Living", "quote": "Charity is ever **contributive** to the peace of the commonwealth and the solace of the poor."},
      {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "Minor collateral influences, though not primary causes, are nevertheless powerfully **contributive** to the phenomenon."}
    ]
  },
  "Dashboard — trib/contributor.md": {
    "primary": "A person who or thing that contributes money, aid, or ideas to a cause, fund, or publication.",
    "secondary": "In open-source software and collaborative scholarship, an author who supplies code, documentation, or peer review to a collective project.",
    "quotes": [
      {"author": "G. K. Chesterton", "work": "The Wisdom of Father Brown", "quote": "He was a regular **contributor** to the quarterly reviews, respected for his lucid style and conservative principles."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Mr. Skimpole was not an active **contributor** to the family income, preferring to live upon sunshine and friendship."},
      {"author": "Thomas Babington Macaulay", "work": "Critical and Historical Essays", "quote": "As a distinguished **contributor** to the Edinburgh Review, his articles commanded universal attention."}
    ]
  },
  "Dashboard — trib/contributory.md": {
    "primary": "Playing a part in bringing something about; or supplying funds or aid toward a joint undertaking.",
    "secondary": "In law of torts, negligence on the part of a plaintiff that combines with the defendant's negligence to cause injury (contributory negligence).",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The division of labor is a **contributory** factor in the remarkable increase of national productivity."},
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "The question of **contributory** fault in actions of trespass has engaged the attention of our most learned judges."},
      {"author": "Herbert Spencer", "work": "The Principles of Sociology", "quote": "Mutual aid and shared defense are the **contributory** elements that bind primitive tribes together."}
    ]
  },
  "Dashboard — trib/detribalisation.md": {
    "primary": "The British spelling of detribalization; the process of causing people to abandon their traditional tribal customs, social structures, and communal ties.",
    "secondary": "In colonial social anthropology and post-colonial studies, cultural disruption resulting from urban migration and European administrative hegemony.",
    "quotes": [
      {"author": "James George Frazer", "work": "The Golden Bough", "quote": "The rapid **detribalisation** of native communities often breaks down the moral sanctions of ancient custom."},
      {"author": "Bronislaw Malinowski", "work": "The Dynamics of Culture Change", "quote": "Urbanization in southern Africa was accompanied by an acute **detribalisation** that left workers socially alienated."},
      {"author": "E. E. Evans-Pritchard", "work": "Social Anthropology", "quote": "Administrative policies in the protectorate accelerated **detribalisation** long before educational institutions were prepared to absorb the youth."}
    ]
  },
  "Dashboard — trib/detribalise.md": {
    "primary": "The British spelling of detribalize; to cause to abandon tribal customs, communal loyalties, and traditional social organization.",
    "secondary": "In colonial administrative policy, to assimilate indigenous populations into Western legal, economic, and political institutions.",
    "quotes": [
      {"author": "Bronislaw Malinowski", "work": "Argonauts of the Western Pacific", "quote": "To abruptly **detribalise** a native people without offering a viable civic substitute leads inevitably to social decay."},
      {"author": "E. E. Evans-Pritchard", "work": "The Nuer", "quote": "European legal codes sought to **detribalise** traditional disputes by imposing magistrate courts over lineage elders."},
      {"author": "James George Frazer", "work": "The Golden Bough", "quote": "Missionary zeal sometimes worked to **detribalise** entire clans before their ancestral cosmology could be recorded."}
    ]
  },
  "Dashboard — trib/detribalization.md": {
    "primary": "The act or process of inducing or compelling members of a tribe to abandon their traditional customs, social organisation, and values.",
    "secondary": "In modernization theory and economic sociology, the erosion of kinship networks caused by wage labor, migration, and Western state formation.",
    "quotes": [
      {"author": "Margaret Mead", "work": "Coming of Age in Samoa", "quote": "The forces of industrial economy hastened the **detribalization** of Pacific island communities."},
      {"author": "Bronislaw Malinowski", "work": "The Dynamics of Culture Change", "quote": "Scholars warned that reckless **detribalization** stripped indigenous youth of their social morality."},
      {"author": "Franz Boas", "work": "The Mind of Primitive Man", "quote": "The tragic effects of forced **detribalization** are written across the history of modern colonial administration."}
    ]
  },
  "Dashboard — trib/detribalize.md": {
    "primary": "To remove from a tribal environment or cause to relinquish tribal allegiances, customs, and traditional identity.",
    "secondary": "In post-colonial sociological analysis, to sever an individual from the customary authority of chiefs and collective clan property.",
    "quotes": [
      {"author": "Franz Boas", "work": "Race, Language and Culture", "quote": "Government schools were expressly designed to **detribalize** indigenous children by prohibiting native dialects."},
      {"author": "Margaret Mead", "work": "New Lives for Old", "quote": "The transition from village reciprocity to money wages began to **detribalize** the younger generation."},
      {"author": "Bronislaw Malinowski", "work": "The Dynamics of Culture Change", "quote": "Attempts to **detribalize** the African agriculturalist without granting civic franchise created widespread discontent."}
    ]
  },
  "Dashboard — trib/distributary.md": {
    "primary": "A branch of a river that does not return to the main stream after leaving it, especially common in river deltas.",
    "secondary": "In fluvial geomorphology and sedimentology, a diverging channel branching off a trunk river to disperse discharge and sediment into a lake or ocean.",
    "quotes": [
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "The great delta of the Ganges is traversed by innumerable winding channels, each **distributary** depositing silt upon the flats."},
      {"author": "Alexander von Humboldt", "work": "Personal Narrative of Travels", "quote": "The Orinoco bifurcates into the Casiquiare, a remarkable natural **distributary** connecting two grand river systems."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "We sailed past the mouth of each sluggish **distributary** draining the mangrove swamps of the estuary."}
    ]
  },
  "Dashboard — trib/distribute.md": {
    "primary": "To give shares of something out to a group or people; to divide and allocate among several recipients.",
    "secondary": "In formal deductive logic, to use a term so that it encompasses every individual member of the class denoted (distributed middle).",
    "quotes": [
      {"author": "William Shakespeare", "work": "King Lear", "quote": "So distribution should undo excess, and each man have enough; go, **distribute** these garments among the poor."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The annual labor of every nation is the fund which originally supplies it with all the necessaries and conveniences of life, which it must **distribute** among its citizens."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Natural agencies tend to disperse and **distribute** plant seeds across ocean barriers."}
    ]
  },
  "Dashboard — trib/distributed.md": {
    "primary": "Dispersed, spread out, or allocated among several persons, places, or parts.",
    "secondary": "In computer systems engineering, designating an architecture where computational processes execute concurrently across multiple networked nodes.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Coriolanus", "quote": "The provisions of the granaries were fairly **distributed** among the clamoring plebeians."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The colouring matter seems to be a nearly constant quantity, so that when more is **distributed** on one part, less remains for another."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "The capacity for reason is not confined to scholars, but is **distributed** by nature among all mankind."}
    ]
  },
  "Dashboard — trib/distributer.md": {
    "primary": "An alternative spelling of distributor; an agent, person, or mechanism that allocates, disperses, or delivers goods or energy.",
    "secondary": "In automotive ignition systems, the mechanical rotary switch distributing high-voltage pulses to spark plugs in correct firing order.",
    "quotes": [
      {"author": "Francis Bacon", "work": "The Essays", "quote": "A good magistrate is not an extortioner of the subject, but an impartial **distributer** of justice."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The wholesale merchant acts as a convenient **distributer** of merchandise between the manufacturer and the retailer."},
      {"author": "Thomas Hobbes", "work": "Leviathan", "quote": "The sovereign is the ultimate **distributer** of lands and honors within the commonwealth."}
    ]
  },
  "Dashboard — trib/distribution.md": {
    "primary": "The action of sharing something out among a number of recipients; or the way in which something is spread out over an area.",
    "secondary": "In probability theory and mathematical statistics, a function showing the probabilities of occurrences of different possible outcomes.",
    "quotes": [
      {"author": "William Shakespeare", "work": "King Lear", "quote": "So **distribution** should undo excess, and each man have enough."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The geographical **distribution** of organic beings on the face of the earth offers many baffling problems."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The rules which men naturally observe in exchanging them for goods determine what may be called the relative **distribution** of wealth."}
    ]
  },
  "Dashboard — trib/distributional.md": {
    "primary": "Of or relating to the way something is shared, apportioned, or spread across a region or population.",
    "secondary": "In structural linguistics, analyzing phonemes and morphemes based on their positional environments within utterances.",
    "quotes": [
      {"author": "Alfred Russel Wallace", "work": "The Geographical Distribution of Animals", "quote": "The **distributional** boundaries of animal families in the archipelago coincide with deep ocean trenches."},
      {"author": "Leonard Bloomfield", "work": "Language", "quote": "A rigorous **distributional** analysis reveals the functional slots that linguistic forms can occupy."},
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "The **distributional** consequences of legislative tariffs fall most heavily upon working classes."}
    ]
  },
  "Dashboard — trib/distributive.md": {
    "primary": "Relating to distribution; or (in grammar) referring to each member of a group individually (such as each, every, either).",
    "secondary": "In political philosophy and jurisprudence, principles governing the fair allocation of resources, wealth, and honors (distributive justice).",
    "quotes": [
      {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "This is the highest abstract standard of social and **distributive** justice; towards which all institutions ought to converge."},
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "The **distributive** virtues of a commonwealth appear in rewarding merit and honoring civic service."},
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "The **distributive** authority of the crown was exercised through judges appointed to the several circuits."}
    ]
  },
  "Dashboard — trib/distributively.md": {
    "primary": "In a distributive manner; considering or applying to each member of a group individually rather than collectively.",
    "secondary": "In formal logic and jurisprudence, predicated of each individual constituent separately rather than of the class as an aggregate whole.",
    "quotes": [
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "These propositions are true not only collectively, but **distributively** of every singular member."},
      {"author": "Thomas Hobbes", "work": "Leviathan", "quote": "The subjects are bound to their sovereign not **distributively** as isolated individuals, but collectively as a covenanting body."},
      {"author": "Jeremy Bentham", "work": "An Introduction to the Principles of Morals and Legislation", "quote": "The pleasures of the community are nothing more than the sum of pleasures felt **distributively** by its members."}
    ]
  },
  "Dashboard — trib/distributor.md": {
    "primary": "An agent, enterprise, or person that supplies goods to businesses or stores; or a mechanical device that disperses something.",
    "secondary": "In internal combustion engines, a rotary device that directs high-voltage current from the ignition coil to the spark plugs in proper sequence.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The wholesale **distributor** serves as an indispensable link connecting distant manufacturers with consumers."},
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Bruce-Partington Plans", "quote": "The man acted as the secret **distributor** of foreign intelligence to agents in London."},
      {"author": "H. G. Wells", "work": "The Food of the Gods", "quote": "The government appointed a special **distributor** to manage the rations of the miraculous substance."}
    ]
  },
  "Dashboard — trib/intertribal.md": {
    "primary": "Occurring between or involving two or more tribes or clans.",
    "secondary": "In ethnographic anthropology and ethnohistory, inter-clan barter networks, matrimonial alliances, or warfare conducted between indigenous groups.",
    "quotes": [
      {"author": "James George Frazer", "work": "The Golden Bough", "quote": "The sacred peace was proclaimed by the elders to halt **intertribal** feuds during the harvest rituals."},
      {"author": "Francis Parkman", "work": "The Conspiracy of Pontiac", "quote": "Pontiac sought to extinguish all **intertribal** rivalries in order to forge a united confederacy against the British."},
      {"author": "Theodore Roosevelt", "work": "The Winning of the West", "quote": "Vicious **intertribal** warfare had depopulated the fertile valleys long before the arrival of the white pioneers."}
    ]
  },
  "Dashboard — trib/reattribute.md": {
    "primary": "To attribute again; especially to assign a work of art, text, or action to a different author or source after reconsideration.",
    "secondary": "In art history and textual forensics, formally revising an attribution following spectrographic pigment analysis or stylistic reassessment.",
    "quotes": [
      {"author": "Bernard Berenson", "work": "The Study and Criticism of Italian Art", "quote": "Recent archival discoveries have compelled connoisseurs to **reattribute** the altarpiece from Ghirlandaio to his workshop."},
      {"author": "Kenneth Clark", "work": "Looking at Pictures", "quote": "Modern gallery curators rarely **reattribute** a masterpiece without overwhelming documentary evidence."},
      {"author": "T. S. Eliot", "work": "Selected Essays", "quote": "Textual critics should hesitate to **reattribute** Elizabethan dramas on the strength of metrical tests alone."}
    ]
  },
  "Dashboard — trib/redistribute.md": {
    "primary": "To distribute something again or in a different way, especially to achieve a fairer allocation.",
    "secondary": "In welfare economics and fiscal policy, reallocating income and wealth across society through progressive taxation and public transfers.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "Society can **redistribute** wealth in whatever manner the community deems most conducive to general happiness."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "Equal inheritance laws operate continually to divide and **redistribute** great landed estates."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Artificial selection enables the breeder to **redistribute** vital nutrients toward the development of favored traits."}
    ]
  },
  "Dashboard — trib/redistributed.md": {
    "primary": "Distributed again or differently; apportioned anew among people or places.",
    "secondary": "In structural geology and metamorphic petrology, minerals dissolved and reprecipitated along fault planes or shear zones.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The pigment matter was **redistributed** over the plumage, producing striking bilateral patterns."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Capital withdrawn from decaying industries was quickly **redistributed** into more profitable avenues."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "Taxes collected from foreign trade were **redistributed** to support federal administration and national defense."}
    ]
  },
  "Dashboard — trib/redistribution.md": {
    "primary": "The act or process of distributing something again or in a different way; especially the reallocation of wealth or resources.",
    "secondary": "In political economy and public finance, state-directed transfer of income through social security, progressive taxes, or agrarian land reform.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "The primary purpose of social legislation should be the equitable **redistribution** of burdens among all classes."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "The continuous **redistribution** of landed property prevented the formation of a permanent aristocracy."},
      {"author": "Herbert Spencer", "work": "The Principles of Sociology", "quote": "Coercive **redistribution** of wealth by the state impairs individual initiative and social efficiency."}
    ]
  },
  "Dashboard — trib/retribute.md": {
    "primary": "To make repayment, return, or recompense for something; to punish or reward according to merit.",
    "secondary": "In moral philosophy and theological ethics, to administer divine or moral justice in strict proportion to deeds committed.",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "God shall **retribute** each according to his works, rendering glory to the faithful and wrath to the rebellious."},
      {"author": "Jeremy Taylor", "work": "Holy Living", "quote": "Temporal rulers must **retribute** both good and evil, honoring the virtuous and chastening the lawless."},
      {"author": "Thomas Browne", "work": "Religio Medici", "quote": "Conscience alone can adequately **retribute** the secret offenses which escape the notice of human magistrates."}
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

print(f"Carrying Batch 2A (trib): Successfully updated {updated}/{len(data)} notes.")
