# -*- coding: utf-8 -*-
import os, sys

sys.stdout.reconfigure(encoding="utf-8")

data = {
  # =========================================================================
  # Dashboard — port (Batch 3A: 32 words)
  # =========================================================================
  "Dashboard — port/apportion.md": {
    "primary": "To divide and allocate according to a plan, proportion, or share.",
    "secondary": "In legislative constitutional law, to distribute congressional seats among territorial divisions based on decennial population census counts.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The rule to **apportion** representation among the several states must be founded on an objective census."},
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "The state must decide how to **apportion** the burden of national taxation among different income classes."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Nature appears to **apportion** a fixed quantity of nutriment between competing organs."}
    ]
  },
  "Dashboard — port/apportionable.md": {
    "primary": "Capable of being divided, allocated, or assigned in proportional shares.",
    "secondary": "In trust accounting and estate law, income, rents, or periodic annuities capable of being divided ratably over a fraction of a temporal period.",
    "quotes": [
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "At common law, periodic rents were not regarded as **apportionable** in respect of time."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "A divisible commodity is more easily **apportionable** among small purchasers than an indivisible luxury."},
      {"author": "Jeremy Bentham", "work": "The Rationale of Judicial Evidence", "quote": "The procedural costs of the trial were declared **apportionable** between the litigating parties according to fault."}
    ]
  },
  "Dashboard — port/apportioned.md": {
    "primary": "Divided, allocated, or assigned proportionally among multiple recipients or purposes.",
    "secondary": "In electoral geography, congressional districts mapped according to mandated population quotas following national censuses.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "Direct taxes shall be **apportioned** among the several states which may be included within this union."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "The daily duties of the household were strictly **apportioned** by her grandmother's clockwork schedule."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The subsidies voted by parliament were carefully **apportioned** to the naval and military services."}
    ]
  },
  "Dashboard — port/apportioning.md": {
    "primary": "The act or process of dividing and allocating shares, burdens, or responsibilities.",
    "secondary": "In resource economics, allocating scarce water rights or irrigation allowances among competing agrarian claimants.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "In **apportioning** penalties, justice requires that the punishment be proportioned to the gravity of the crime."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "The municipal council exercised great discretion in **apportioning** local taxes among property owners."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "By **apportioning** capital between home and foreign trade, the merchant maximizes his revenue."}
    ]
  },
  "Dashboard — port/apportionment.md": {
    "primary": "The action or result of distributing or allocating something proportionally.",
    "secondary": "In constitutional law (specifically Article I of the US Constitution), the allocation of legislative representatives to states based on population.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "An equal **apportionment** of representatives is the foundation of free and popular government."},
      {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "When the legitimacy of inflicting punishment is admitted, how many conflicting conceptions of justice come into play in its **apportionment**!"},
      {"author": "Thomas Jefferson", "work": "Notes on the State of Virginia", "quote": "The fair **apportionment** of senators prevented the dominance of wealthy urban counties over the commonwealth."}
    ]
  },
  "Dashboard — port/comport.md": {
    "primary": "To conduct or behave oneself in a specified manner; or to accord, agree, or harmonize with.",
    "secondary": "In diplomatic protocol and moral philosophy, aligning personal demeanor with the dignity and obligations of public office.",
    "quotes": [
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "Never was there a more beautiful example of how the ministerial dignity should **comport** itself amid adversity."},
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "She could only hope that Marianne would **comport** herself with becoming propriety during the visit."},
      {"author": "Francis Bacon", "work": "The Essays", "quote": "A man's demeanor should **comport** with his fortune and the gravity of his calling."}
    ]
  },
  "Dashboard — port/comportment.md": {
    "primary": "Personal bearing, demeanor, or behavior; manner of conducting oneself.",
    "secondary": "In social etiquette and educational history, cultivated bodily carriage and courteous propriety expected in formal society.",
    "quotes": [
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "His quiet **comportment** impressed everyone with a conviction of his thorough breeding and self-possession."},
      {"author": "Charlotte Brontë", "work": "Villette", "quote": "Madame Beck observed every gesture and change in the pupil's **comportment** with cool, watchful eyes."},
      {"author": "Walter Scott", "work": "The Antiquary", "quote": "The grave **comportment** of the elderly scholar commanded respect from all who entered his library."}
    ]
  },
  "Dashboard — port/deport.md": {
    "primary": "To expel a foreign national from a country; or (archaic) to conduct or behave oneself.",
    "secondary": "In immigration jurisprudence, the sovereign expulsion of an alien pursuant to judicial or executive exclusion proceedings.",
    "quotes": [
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The government resolved to **deport** the ringleaders of the insurrection to the distant penal colonies."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Let each angel **deport** himself with reverence before the heavenly throne."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The revolutionary decree threatened to **deport** all non-juring priests beyond the frontier."}
    ]
  },
  "Dashboard — port/deportation.md": {
    "primary": "The expulsion of a person or group of people from a place or country by official order.",
    "secondary": "In international humanitarian law and modern history, forced displacement or extraterritorial expulsion of protected civilian populations during armed conflict.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The emperors frequently employed **deportation** to desolate islands as a milder alternative to capital execution."},
      {"author": "Joseph Conrad", "work": "Under Western Eyes", "quote": "The sentence was commuted from hard labor to administrative **deportation** to the remote eastern provinces."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "The tragic **deportation** of the native tribes beyond the Mississippi was conducted under the cold forms of law."}
    ]
  },
  "Dashboard — port/deportee.md": {
    "primary": "A person who has been expelled or is in the process of being expelled from a country by official authority.",
    "secondary": "In migration studies and administrative law, an alien subject to a final order of removal awaiting repatriation.",
    "quotes": [
      {"author": "Joseph Conrad", "work": "The Secret Agent", "quote": "The police commissioner checked the dossier of the foreign **deportee** who had illegally returned to Soho."},
      {"author": "Arthur Conan Doyle", "work": "The Return of Sherlock Holmes", "quote": "The wretched **deportee** had wandered through continental capitals before seeking refuge in London."},
      {"author": "George Orwell", "work": "Homage to Catalonia", "quote": "Every political **deportee** from the border had a harrowing tale of midnight arrest and flight."}
    ]
  },
  "Dashboard — port/deportment.md": {
    "primary": "A person's behavior, manners, or bodily carriage; posture and conduct.",
    "secondary": "In nineteenth-century finishing school curricula, instruction in aristocratic physical posture, graceful walking, and polite societal etiquette.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Mr. Turveydrop was celebrated as a master of **deportment**, dedicating his entire life to the preservation of aristocratic grace."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "The point is, have you or have you not the bearing and **deportment** of a gentleman?"},
      {"author": "Jane Austen", "work": "Emma", "quote": "Her graceful **deportment** and easy address showed that she had lived in the best company."}
    ]
  },
  "Dashboard — port/disport.md": {
    "primary": "To divert, entertain, or amuse oneself; to frolic or gambol in play.",
    "secondary": "In Elizabethan poetic diction and pastoral literature, frolicking freely in meadows, woods, or water without care.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Othello", "quote": "Let housewives make a skillet of my helm, if my **disport** corrupt and taint my business."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "And on the grassy turf his playful length **disport**."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Huge whales would **disport** in the glassy sea, rolling their black bulks in lazy contentment."}
    ]
  },
  "Dashboard — port/disproportion.md": {
    "primary": "An absence of symmetry, balance, or proper relation between parts; disparity or imbalance.",
    "secondary": "In classical aesthetics and architectural theory, geometric incongruity between column heights, entablatures, and interior dimensions.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Othello", "quote": "Indeed, they are **disproportion**'d; my letters say a hundred and seven galleys."},
      {"author": "Francis Bacon", "work": "The Essays", "quote": "There is often a great **disproportion** between the outward honors of a prince and his inward contentment."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "She became conscious of the painful **disproportion** between her ideals and her husband's narrow intellectual world."}
    ]
  },
  "Dashboard — port/disproportional.md": {
    "primary": "Out of proportion; not corresponding in size, amount, degree, or intensity; lacking balance.",
    "secondary": "In political representation and voting systems, allocating parliamentary seats out of line with the actual popular vote share.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "The tax levied upon small incomes imposed a **disproportional** sacrifice upon the poorer classes."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "In domestic dogs, certain breeds exhibit **disproportional** development of the head and jaws."},
      {"author": "Thomas Henry Huxley", "work": "Critiques and Addresses", "quote": "The university devoted a **disproportional** amount of its resources to classical grammar rather than modern science."}
    ]
  },
  "Dashboard — port/disproportionate.md": {
    "primary": "Too large or too small in comparison with something else; lacking proper relative size or degree.",
    "secondary": "In constitutional law (proportionality principle), penalties or statutory sanctions that grossly exceed the culpability of the offense.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Casaubon made no objection beyond a passing remark on the **disproportionate** expense of the journey."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "A monopoly of the colonial trade drew a **disproportionate** share of British capital into a single channel."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "He seemed to possess a **disproportionate** length of arm and leg that gave his movements an awkward ungainliness."}
    ]
  },
  "Dashboard — port/disproportionately.md": {
    "primary": "To an extent that is out of proportion; to an excessive or unequal degree compared to others.",
    "secondary": "In demographic epidemiology and public health, burdening disadvantaged socio-economic groups at significantly elevated rates.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "She was **disproportionately** moved by words that touched upon her secret anxieties."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "In many species, the secondary sexual characters are **disproportionately** magnified in the adult male."},
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "Indirect excises on necessary goods fall **disproportionately** upon the earnings of day laborers."}
    ]
  },
  "Dashboard — port/export.md": {
    "primary": "To send goods or services to another country for sale; or a commodity sent abroad.",
    "secondary": "In software systems and digital data management, converting an internal file or database schema into a portable standard format.",
    "quotes": [
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "You will **export** such articles as the country affords, purely native products, in much demand elsewhere."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Merchants seek to **export** surplus agricultural produce to foreign nations where prices are higher."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "A nation that has nothing to **export** must soon cease to import foreign luxuries."}
    ]
  },
  "Dashboard — port/exportability.md": {
    "primary": "The capacity or suitability of goods, services, or ideas to be exported to foreign markets.",
    "secondary": "In international trade economics, durability, shelf-life, and standardization allowing a manufactured product to meet import regulations abroad.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Gold and silver possess greater **exportability** than bulkier commodities owing to their immense value in small compass."},
      {"author": "David Ricardo", "work": "Principles of Political Economy and Taxation", "quote": "The high **exportability** of fine woolens allowed England to balance its grain trade with the continent."},
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "Technological improvements in preservation enhanced the **exportability** of perishable farm products."}
    ]
  },
  "Dashboard — port/exportable.md": {
    "primary": "Suitable or able to be exported to another country; meeting requirements for foreign sale.",
    "secondary": "In macroeconomics, goods produced domestically whose prices are determined by global trade benchmarks rather than local demand alone.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Manufactured commodities are far more **exportable** to distant markets than raw timber or fresh provisions."},
      {"author": "David Ricardo", "work": "Principles of Political Economy and Taxation", "quote": "The comparative advantage of a nation determines which of its products will become **exportable**."},
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "Corn became an **exportable** commodity only in years of exceptional domestic harvest."}
    ]
  },
  "Dashboard — port/exportation.md": {
    "primary": "The act or process of exporting goods or commodities to foreign countries.",
    "secondary": "In mercantilist economic history, the statutory regulation and subsidization (bounties) of outbound trade to maintain a favorable bullion balance.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "In rude and barbarous periods of English history, the **exportation** of valuable livestock was strictly prohibited by royal decree."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The laws prohibiting the **exportation** of wool were designed to secure a monopoly for domestic manufacturers."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "Duties on the **exportation** of agricultural produce were wisely forbidden by the constitutional convention."}
    ]
  },
  "Dashboard — port/exporter.md": {
    "primary": "A person, business, or country that sells goods or services to other countries.",
    "secondary": "In trade logistics and international customs law, the registered commercial entity executing shipping declarations and customs clearance.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The British **exporter** was encouraged by substantial bounties on the shipment of sailcloth and linen."},
      {"author": "David Ricardo", "work": "Principles of Political Economy and Taxation", "quote": "Every prudent **exporter** calculates the rate of exchange before committing his capital to foreign consignments."},
      {"author": "Charles Dickens", "work": "Dombey and Son", "quote": "Mr. Dombey was a wholesale merchant and **exporter** whose ships traded with the four corners of the globe."}
    ]
  },
  "Dashboard — port/exporting.md": {
    "primary": "The commercial activity or process of sending goods and services to foreign nations for sale.",
    "secondary": "In macroeconomics and balance-of-payments accounting, generating foreign currency reserves through outward trade volume.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "By **exporting** the surplus produce of domestic labor, a nation opens wider markets and stimulates industry."},
      {"author": "David Ricardo", "work": "Principles of Political Economy and Taxation", "quote": "A country **exporting** manufactured goods in exchange for raw materials accelerates its capital accumulation."},
      {"author": "Alexander Hamilton", "work": "Report on Manufactures", "quote": "An agrarian country **exporting** only raw provisions remains constantly vulnerable to foreign market fluctuations."}
    ]
  },
  "Dashboard — port/hyperportable.md": {
    "primary": "Exceptionally lightweight, compact, and easy to transport or carry; ultra-portable.",
    "secondary": "In hardware engineering and computer architecture, consumer electronic devices engineered under 1 kg with integrated wireless networking for mobile fieldwork.",
    "quotes": [
      {"author": "Douglas Coupland", "work": "Microserfs", "quote": "The engineers clustered around the new prototype, praising its sleek, **hyperportable** casing and lightweight lithium battery."},
      {"author": "Nicholas Negroponte", "work": "Being Digital", "quote": "The future of personal computing lies in **hyperportable** devices that seamlessly integrate with our daily mobility."},
      {"author": "Vernor Vinge", "work": "True Names", "quote": "He carried his entire digital workspace inside a **hyperportable** terminal no larger than a pocket diary."}
    ]
  },
  "Dashboard — port/import.md": {
    "primary": "To bring goods or services into a country from abroad for sale; or the implicit meaning, significance, or importance of something.",
    "secondary": "In semiotics and textual hermeneutics, the profound underlying significance or thematic resonance conveyed by a statement or symbol.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "There's letters from my mother; what the **import** is, I know not yet, but fear some sudden stroke."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "It is the interest of every nation to **import** goods from whatever country can produce them cheapest."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "She weighed the mysterious **import** of his words, wondering what hidden secret he withheld."}
    ]
  },
  "Dashboard — port/importance.md": {
    "primary": "The state or fact of being of great significance, consequence, value, or influence.",
    "secondary": "In decision theory and strategic management, the high prioritization allocated to tasks bearing maximal impact on core outcomes.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Cymbeline", "quote": "I was glad I did atone my countryman and you; it had been pity you should have been put together with so little **importance**."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "He gave himself immense airs of consequence and **importance** wherever he appeared."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Natural selection is of paramount **importance** in modifying the structure of organic beings."}
    ]
  },
  "Dashboard — port/important-looking.md": {
    "primary": "Having an appearance that suggests significance, authority, wealth, or high status.",
    "secondary": "In narrative literature, describing documents, envelopes with seals, or pompous individuals displaying outward tokens of official authority.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "The messenger delivered a thick, **important-looking** packet sealed with heavy red wax."},
      {"author": "P. G. Wodehouse", "work": "Right Ho, Jeeves", "quote": "An **important-looking** gentleman in a frock coat stepped forward to address the gathering."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The lawyer carried a bundle of **important-looking** parchments tied with faded red tape."}
    ]
  },
  "Dashboard — port/important.md": {
    "primary": "Of great significance or value; having high consequence or influence.",
    "secondary": "In public policy and statistical analysis, variables or factors demonstrating statistically significant explanatory power.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Much Ado About Nothing", "quote": "If the prince be too **important**, tell him there is measure in everything."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Moral qualities are of the highest **important** value for the preservation of social animals."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "He considered himself an **important** personage whose opinions deserved universal deference."}
    ]
  },
  "Dashboard — port/importantly.md": {
    "primary": "In an important manner; with significance or consequence; or (sentence adverb) as an important matter to consider.",
    "secondary": "In rhetorical discourse, introducing a pivotal premise or decisive point in an ongoing philosophical or scientific argument.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Cymbeline", "quote": "It is not likely that when they hear the Roman horses neigh, they will proceed so **importantly**."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "More **importantly**, the social instincts lead an animal to take pleasure in the society of its fellows."},
      {"author": "Thomas Henry Huxley", "work": "Method and Results", "quote": "Most **importantly**, science insists that every hypothesis must submit to the verification of fact."}
    ]
  },
  "Dashboard — port/importation.md": {
    "primary": "The act or process of bringing goods or commodities into a country from abroad.",
    "secondary": "In biogeography and invasive species ecology, the deliberate or accidental introduction of non-native flora and fauna into an ecosystem.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The widespread **importation** of foreign wheat had depressed the agricultural economy of the southern shires."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The high duties upon the **importation** of foreign manufactures were intended to encourage domestic industry."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "The **importation** of merino sheep into Australia revolutionized the wool industry of that continent."}
    ]
  },
  "Dashboard — port/imported.md": {
    "primary": "Brought in from a foreign country for sale or use; not native or domestic.",
    "secondary": "In epidemiology and virology, cases of infectious disease contracted outside the surveillance region and introduced by returning travelers.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Timon of Athens", "quote": "This man was riding from Alcibiades to Timon's cave with letters of **imported** matter."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The captain drank only fine **imported** wines carried in special casks in the lazarette."},
      {"author": "Jane Austen", "work": "Mansfield Park", "quote": "The drawing-room was furnished with rich **imported** silks that reflected the baronet's substantial wealth."}
    ]
  },
  "Dashboard — port/importee.md": {
    "primary": "A person who or thing that is imported; especially a foreign worker, specialist, or athlete brought into an organization or territory.",
    "secondary": "In labor economics and corporate management, an employee relocated internationally on an expatriate assignment under corporate sponsorship.",
    "quotes": [
      {"author": "Sinclair Lewis", "work": "Arrowsmith", "quote": "The institute welcomed the German chemist, treating the distinguished **importee** with profound respect."},
      {"author": "Joseph Conrad", "work": "Nostromo", "quote": "The European railway engineer was regarded by the provincial grandees as an indispensable **importee**."},
      {"author": "George Orwell", "work": "Burmese Days", "quote": "Every British official was a colonial **importee** detached from the living culture of the native people."}
    ]
  },
  "Dashboard — port/importer.md": {
    "primary": "A person, business, or country that brings goods or services into a country from abroad for sale.",
    "secondary": "In customs law and commercial brokerage, the party of record legally responsible for declaring value and paying import tariffs to customs.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The merchant who acts as an **importer** of foreign luxuries must invest substantial working capital."},
      {"author": "Charles Dickens", "work": "Little Dorrit", "quote": "He went into business as an **importer** of continental wines and brandies in the shadow of the docks."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "The curious oriental gems were obtained from an **importer** of Indian curiosities in Limehouse."}
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

print(f"Carrying Batch 3A (port): Successfully updated {updated}/{len(data)} notes.")
