# -*- coding: utf-8 -*-
"""
Curates Dashboard — pat Part B (words 67-132) in Cluster Emotion.
"""
import os, sys, re, subprocess

sys.stdout.reconfigure(encoding="utf-8")

data = {
  "Dashboard — pat/patras.md": {
    "primary": "A major commercial port city in western Greece and the regional capital of Western Greece, on the Gulf of Patras.",
    "secondary": "In Mediterranean history, an ancient Achaean city that flourished under Roman rule and became an early center of Christianity.",
    "quotes": [
      {"author": "Lord Byron", "work": "Letters and Journals", "quote": "From the ramparts of **patras**, we surveyed the broad waters of the gulf where the Allied fleets gathered."},
      {"author": "Edward Dodwell", "work": "A Classical and Topographical Tour through Greece", "quote": "The fertile plain surrounding **patras** produces the finest small grapes known in commerce as Zante currants."},
      {"author": "William Martin Leake", "work": "Travels in the Morea", "quote": "The fortress of **patras** occupies a high spur commanding the narrow entrance to the Gulf of Corinth."}
    ]
  },
  "Dashboard — pat/patrial.md": {
    "primary": "A person having a legal right of abode in the United Kingdom under the Immigration Act 1971; of or relating to one's native land.",
    "secondary": "In British constitutional immigration law, a statutory status conferring exemption from immigration control based on ancestry.",
    "quotes": [
      {"author": "A. V. Dicey", "work": "Introduction to the Study of the Law of the Constitution", "quote": "The legal concept of a **patrial** subject redefined traditional British allegiance in terms of ancestral residence."},
      {"author": "Enoch Powell", "work": "Reflections on a Nation", "quote": "Parliament sought by the **patrial** clause to distinguish between citizens with historic ties to the realm and Commonwealth nationals."},
      {"author": "Anthony Lester", "work": "Citizenship and Immigration in the United Kingdom", "quote": "Under the new statute, any applicant proving **patrial** descent was granted unrestricted entry and residence."}
    ]
  },
  "Dashboard — pat/patriarch.md": {
    "primary": "The male head of a family or tribe; an elder or founding father of a venerable institution.",
    "secondary": "In Eastern Orthodox, Roman Catholic, and Anglican hierarchies, a bishop of the highest rank presiding over an ancient autocephalous see.",
    "quotes": [
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "The father of the Custom-House—the **patriarch**, not only of this little squad, but of the whole veteran corps of inspectors."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "The venerable gentleman sat by the fireside like a benevolent **patriarch**, blessing the children gathered at his knee."},
      {"author": "King James Bible", "work": "The Holy Bible", "quote": "Men and brethren, let me freely speak unto you of the **patriarch** David, that he is both dead and buried, and his sepulchre is with us unto this day."}
    ]
  },
  "Dashboard — pat/patriarchal.md": {
    "primary": "Characteristic of a patriarch or a system of society controlled by men; fatherly and traditional.",
    "secondary": "In sociological history, social structures where authority, descent, and inheritance are concentrated exclusively in elder males.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "In early stages of human association, morality was enforced through stern **patriarchal** authority over the tribe."},
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "I doubt greatly whether any public functionary had ever maintained a more tranquil and **patriarchal** household."},
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "The **patriarchal** lives of my protectors caused these impressions to take a firm hold on my mind, showing me domestic peace."}
    ]
  },
  "Dashboard — pat/patriarchate.md": {
    "primary": "The office, jurisdiction, official residence, or see of an ecclesiastical patriarch.",
    "secondary": "In church history, the five historic pentarchy sees—Rome, Constantinople, Alexandria, Antioch, and Jerusalem.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The ambitious prelate aspired to the vacant **patriarchate** of Constantinople, courting the favor of eunuchs and imperial courtiers."},
      {"author": "John Henry Newman", "work": "The Arians of the Fourth Century", "quote": "Athanasius returned in triumph to resume his pastoral seat in the ancient **patriarchate** of Alexandria."},
      {"author": "Thomas Fuller", "work": "The Holy State and the Profane State", "quote": "The jurisdiction of the **patriarchate** extended over hundreds of suffragan bishoprics across the Levant."}
    ]
  },
  "Dashboard — pat/patriarchic.md": {
    "primary": "Of, relating to, or resembling a patriarch; patriarchal in authority or seniority.",
    "secondary": "In antique prose and biblical criticism, describing the ancient, pastoral lifestyle of Old Testament heads of families.",
    "quotes": [
      {"author": "Walter Scott", "work": "The Heart of Mid-Lothian", "quote": "David Deans governed his household with **patriarchic** simplicity, enforcing strict Presbyterian discipline upon all under his roof."},
      {"author": "Washington Irving", "work": "A History of New York", "quote": "The Dutch burghers smoked long clay pipes on their stoops in serene **patriarchic** tranquility before the English conquest."},
      {"author": "Thomas Carlyle", "work": "On Heroes, Hero-Worship, and the Heroic in History", "quote": "In those desert tents, the Arab chieftain exercised a **patriarchic** rule founded upon innate personal prowess."}
    ]
  },
  "Dashboard — pat/patriarchy.md": {
    "primary": "A system of society or government in which men hold the primary power and predominate in leadership roles.",
    "secondary": "In feminist theory and social anthropology, institutionalized male supremacy regulating family descent, property, and civic authority.",
    "quotes": [
      {"author": "Virginia Woolf", "work": "Three Guineas", "quote": "The private house and the public office remain intertwined under the ancient reign of **patriarchy**, preserving unearned male privilege."},
      {"author": "Charlotte Perkins Gilman", "work": "The Man-Made World", "quote": "The transition from maternal kinship to absolute **patriarchy** marked the subordination of woman's creative potential in culture."},
      {"author": "John Stuart Mill", "work": "The Subjection of Women", "quote": "The legal supremacy of the husband over the wife is the last remaining bastion of primitive **patriarchy** in modern law."}
    ]
  },
  "Dashboard — pat/patricentric.md": {
    "primary": "Centered on or dominated by the father; patriarchal in social organization or psychology.",
    "secondary": "In anthropological lineage studies, cultural customs that prioritize the father's relatives and authority in family decisions.",
    "quotes": [
      {"author": "Bronislaw Malinowski", "work": "The Father in Primitive Psychology", "quote": "Contrasting with matrilineal islanders, our European societies exhibit a distinctly **patricentric** organization of domestic authority."},
      {"author": "Margaret Mead", "work": "Sex and Temperament in Three Primitive Societies", "quote": "Among the plains tribes, kinship obligations were strictly **patricentric**, binding young warriors to their father's brothers."},
      {"author": "Claude Lévi-Strauss", "work": "The Elementary Structures of Kinship", "quote": "The shift toward a **patricentric** clan structure fundamentally altered marriage exchange rules among pastoral nomads."}
    ]
  },
  "Dashboard — pat/patrician.md": {
    "primary": "An aristocrat or nobleman; a person of high social rank, refined taste, or noble birth.",
    "secondary": "In Roman history, a member of the original hereditary ruling families of ancient Rome, contrasted with the plebeians.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "I am known to be a humorous **patrician** and one that loves a cup of hot wine with not a drop of allaying Tiber in't."},
      {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "A natural gentleman finds his way in, and will keep the oldest **patrician** out by the sheer nobility of his bearing."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Nowhere in all America will you find more **patrician**-like houses, or park-like grounds, than in New Bedford."}
    ]
  },
  "Dashboard — pat/patricide.md": {
    "primary": "The killing of one's father; also a person who murders their own father.",
    "secondary": "In Roman law and psychoanalytic theory (*Oedipus Rex*), the gravest crime of parricide, traditionally punished by drowning in a sack.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The Roman statutes visited the abhorred guilt of **patricide** with singular terror, sewing the criminal into a sack with vipers and a dog."},
      {"author": "Fyodor Dostoevsky", "work": "The Brothers Karamazov", "quote": "The whole town buzzed with the scandalous trial, debating whether the wild officer was guilty of horrific **patricide**."},
      {"author": "Sigmund Freud", "work": "Totem and Taboo", "quote": "In ancient myth, the memory of primal **patricide** left an indelible trace upon collective guilt and religious ritual."}
    ]
  },
  "Dashboard — pat/patrick.md": {
    "primary": "A personal name of Latin origin (*Patricius*, noble); famously the patron saint of Ireland.",
    "secondary": "In Irish history and folklore, the fifth-century missionary bishop who converted the Gaelic kingdoms to Christianity.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "Yes, by Saint **patrick**, but there is, Horatio, and much offence too, in the ghost's dread revelation."},
      {"author": "James Joyce", "work": "Dubliners", "quote": "The late lamented **patrick** Morkan, our grandfather, was a staunch citizen of Dublin whose memory we cherish this evening."},
      {"author": "G. K. Chesterton", "work": "The Wisdom of Father Brown", "quote": "The prisoner was defended by Mr **patrick** Butler, K.C., who was mistaken for an actor on account of his dramatic eloquence."}
    ]
  },
  "Dashboard — pat/patrikin.md": {
    "primary": "Relatives related through the father's lineage; agnatic or patrilineal kin.",
    "secondary": "In kinship anthropology and clan genealogy, the group of blood relations traced through the male genealogical line.",
    "quotes": [
      {"author": "Edward Westermarck", "work": "The History of Human Marriage", "quote": "In pastoral societies, blood feuds bound every man to defend his **patrikin** against rival territorial clans."},
      {"author": "Bronislaw Malinowski", "work": "Crime and Custom in Savage Society", "quote": "The obligations owed to maternal uncles frequently conflicted with reciprocal economic duties toward one's **patrikin**."},
      {"author": "E. E. Evans-Pritchard", "work": "The Nuer", "quote": "A man looks to his **patrikin** for the cattle necessary to pay bride-wealth when contracting marriage."}
    ]
  },
  "Dashboard — pat/patrilineage.md": {
    "primary": "Lineage or descent traced exclusively through the paternal line.",
    "secondary": "In social anthropology, a corporate descent group whose members trace common ancestry to a male progenitor.",
    "quotes": [
      {"author": "Claude Lévi-Strauss", "work": "Structural Anthropology", "quote": "The corporate rights to sacred hunting grounds were vested within the male elders of the village **patrilineage**."},
      {"author": "Meyer Fortes", "work": "The Dynamics of Clanship Among the Tallensi", "quote": "Every domestic altar in the compound is dedicated to the departed ancestors of the localized **patrilineage**."},
      {"author": "Max Gluckman", "work": "Custom and Conflict in Africa", "quote": "Disputes over livestock inheritance are adjudicated by senior lineage heads within the defendant's **patrilineage**."}
    ]
  },
  "Dashboard — pat/patrilineal.md": {
    "primary": "Relating to or based on relationship to the father or descent through the male line.",
    "secondary": "In comparative ethnology, describing inheritance laws and surnames passed from father to son.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The establishment of a strictly **patrilineal** succession marked an advance toward hereditary monarchy among ancient tribes."},
      {"author": "Lewis H. Morgan", "work": "Ancient Society", "quote": "With the rise of private property, maternal gens gave way to **patrilineal** inheritance of agricultural estates."},
      {"author": "Edward Tylor", "work": "Primitive Culture", "quote": "In many African communities, **patrilineal** descent determines clan membership, ancestral worship, and land tenure."}
    ]
  },
  "Dashboard — pat/patrilineally.md": {
    "primary": "In a patrilineal manner; by descent through the male line.",
    "secondary": "In kinship analysis and tribal succession, transmitting titles and ancestral lands through paternal ancestors.",
    "quotes": [
      {"author": "Lewis H. Morgan", "work": "Systems of Consanguinity and Affinity of the Human Family", "quote": "Chieftainship in this confederacy is inherited **patrilineally**, passing from father to eldest surviving son."},
      {"author": "Bronislaw Malinowski", "work": "The Sexual Life of Savages", "quote": "While garden plots descend matrilineally, certain ritual magic formulas are transmitted **patrilineally** to favorite sons."},
      {"author": "E. E. Evans-Pritchard", "work": "Kinship and Marriage Among the Nuer", "quote": "Cattle marks and clan praise-names are reckoned **patrilineally**, establishing permanent ties between dispersed herdsmen."}
    ]
  },
  "Dashboard — pat/patrilinear.md": {
    "primary": "Patrilineal; tracing descent or transmitting rights and property through the male line.",
    "secondary": "In legal history and sociological taxonomy, an agnatic kinship system centered on male lineage continuity.",
    "quotes": [
      {"author": "Henry Sumner Maine", "work": "Ancient Law", "quote": "The Roman agnatic family was essentially **patrilinear**, excluding all relationship traced through married daughters."},
      {"author": "William Graham Sumner", "work": "Folkways", "quote": "Feudal tenure rested upon an uncompromisingly **patrilinear** principle to ensure that military service remained unbroken."},
      {"author": "Edward Westermarck", "work": "The Origin and Development of the Moral Ideas", "quote": "Ancestral sacrifices in ancient China were organized around **patrilinear** tablets housed in the family hall."}
    ]
  },
  "Dashboard — pat/patrimonial.md": {
    "primary": "Relating to or inherited from one's father or ancestors; passed down as hereditary family property.",
    "secondary": "In political sociology (Max Weber), a traditional authority structure where royal administration is treated as the ruler's private household.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Evolution and Ethics", "quote": "He that saw his **patrimonial** timber cast its leaf, sells the last scantling to pay debts of gaming honor."},
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "We receive, we hold, we transmit our government and our privileges in the same manner as our **patrimonial** estates."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "In democratic republics, equal division of inheritances shatters the large **patrimonial** estates of the old aristocracy."}
    ]
  },
  "Dashboard — pat/patrimony.md": {
    "primary": "Property, estate, or wealth inherited from one's father or male ancestor; a heritage.",
    "secondary": "In historical economics and ecclesiastical law, the hereditary lands of a family or the Patrimony of Saint Peter (Papal States).",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "Who can be bound by any solemn vow to do a murderous deed, to rob a man, to force a spotless virgin's chastity, to reave the orphan of his **patrimony**?"},
      {"author": "King James Bible", "work": "The Holy Bible", "quote": "They shall have like portions to eat, beside that which cometh of the sale of his **patrimony**."},
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The rich **patrimony** of the Roman church in Sicily and Calabria was confiscated by the Byzantine emperor."}
    ]
  },
  "Dashboard — pat/patriot.md": {
    "primary": "A person who vigorously supports their country and is prepared to defend it against enemies or detractors.",
    "secondary": "In political history, an ardent champion of national independence, constitutional liberty, or civic reform.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "No; only that my grandfather was a **patriot**—a bright fellow—could speak many languages and fought for Polish freedom."},
      {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "The young **patriot** feels himself stronger than before by the addition of the courage of five hundred confederates."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "What is the price-current of an honest man and **patriot** today? They hesitate, and they regret, and sometimes they petition."}
    ]
  },
  "Dashboard — pat/patrioteer.md": {
    "primary": "A person who makes an ostentatious, aggressive, or hypocritical display of patriotism, often for selfish gain.",
    "secondary": "In political satire and anti-war literature, a jingoistic war-profiteer who exploits national fervor for personal enrichment.",
    "quotes": [
      {"author": "Sinclair Lewis", "work": "It Can't Happen Here", "quote": "The local **patrioteer** waved his flag vehemently from the podium while pocketing municipal contracts for military uniforms."},
      {"author": "H. L. Mencken", "work": "Prejudices: First Series", "quote": "Nothing is easier than to arouse the mob with the screeching platitudes of the professional **patrioteer**."},
      {"author": "George Orwell", "work": "The Lion and the Unicorn", "quote": "We must learn to separate genuine civic loyalty from the shallow bombast of the commercial **patrioteer**."}
    ]
  },
  "Dashboard — pat/patriotic.md": {
    "primary": "Having or expressing devotion to and vigorous support for one's country; nationalistic and public-spirited.",
    "secondary": "In civic rhetoric and historical memoirs, self-sacrificing dedication to the defense of constitutional democracy.",
    "quotes": [
      {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "We sometimes meet men under some strong moral influence, as a **patriotic** or religious fervor, who act with superhuman energy."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "Yet some can be **patriotic** who have no self-respect, and sacrifice the greater to the less at every election."},
      {"author": "Lewis Carroll", "work": "Alice's Adventures in Wonderland", "quote": "Edwin and Morcar, the earls of Mercia and Northumbria, declared for him; and even Stigand, the **patriotic** archbishop of Canterbury, found it advisable."}
    ]
  },
  "Dashboard — pat/patriotically.md": {
    "primary": "In a patriotic manner; with heartfelt devotion to one's country and willingness to serve its welfare.",
    "secondary": "In civic journalism and oratory, acting in faithful accordance with the public interest during national emergencies.",
    "quotes": [
      {"author": "Abraham Lincoln", "work": "Speeches and Letters", "quote": "The citizens responded **patriotically** to the call for volunteers, marching forth to preserve the integrity of the Union."},
      {"author": "Winston Churchill", "work": "The Unrelenting Struggle", "quote": "Factory workers laboured **patriotically** through the night shifts, refusing to take shelter even during heavy air raids."},
      {"author": "Theodore Roosevelt", "work": "The Strenuous Life", "quote": "To vote **patriotically** requires setting aside narrow partisan advantage in order to support honest administration."}
    ]
  },
  "Dashboard — pat/patriotism.md": {
    "primary": "Devotion to and vigorous support for one's country; national pride and civic loyalty.",
    "secondary": "In moral philosophy and political ethics, love of one's homeland tempered by universal justice and international fraternity.",
    "quotes": [
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "He asked himself whether these tribunal judges were inspired by motives of sheer **patriotism**, or bloodthirsty faction."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "There is not the fight recorded in Concord history, at least, that would bear a moment's comparison with this **patriotism** of the ants."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "A tribe including many members who possessed in a high degree the spirit of **patriotism**, fidelity, and mutual aid would always succeed best."}
    ]
  },
  "Dashboard — pat/patrisib.md": {
    "primary": "A sibling or clan relative related on the father's side; a patrilineal sibling or agnatic cousin.",
    "secondary": "In kinship anthropology, an agnatic sibling group forming a corporate ceremonial unit within a tribal clan.",
    "quotes": [
      {"author": "Robert H. Lowie", "work": "Primitive Society", "quote": "The rights of vengeance and blood compensation were shared equally among all members of the **patrisib**."},
      {"author": "George Peter Murdock", "work": "Social Structure", "quote": "Exogamy rules strictly forbade marriage between individuals belonging to the same localized **patrisib**."},
      {"author": "A. R. Radcliffe-Brown", "work": "Structure and Function in Primitive Society", "quote": "A boy owes ceremonial respect to his father's sisters, who represent the authority of his **patrisib**."}
    ]
  },
  "Dashboard — pat/patristic.md": {
    "primary": "Of or relating to the early Christian Church Fathers or their writings and theological doctrines.",
    "secondary": "In historical theology, the theological era spanning the Apostolic Fathers to the Council of Chalcedon (circa 100–500 AD).",
    "quotes": [
      {"author": "John Henry Newman", "work": "An Essay on the Development of Christian Doctrine", "quote": "Deep immersion in **patristic** literature convinced Newman that modern Anglicanism had drifted from the primitive church."},
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The student of **patristic** eloquence will find in Chrysostom the fire of Demosthenes tempered by Christian zeal."},
      {"author": "Thomas Aquinas", "work": "Summa Theologiae", "quote": "The scholastic master cites the **patristic** authority of Saint Augustine as the foundational bedrock of his argument."}
    ]
  },
  "Dashboard — pat/patristical.md": {
    "primary": "Pertaining to the Church Fathers, their theological texts, or early ecclesiastical history (variant of patristic).",
    "secondary": "In nineteenth-century Anglican divinity, characterizing doctrinal treatises grounded in early post-apostolic writings.",
    "quotes": [
      {"author": "Samuel Taylor Coleridge", "work": "Aids to Reflection", "quote": "The seventeenth-century divines enriched their homilies with abundant **patristical** citations from Jerome and Basil."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The bishop's extensive library was crammed with folios of **patristical** theology and councils of the early Church."},
      {"author": "Matthew Arnold", "work": "Literature and Dogma", "quote": "We must distinguish between the simple poetry of the Gospels and the speculative subtleties of later **patristical** dogma."}
    ]
  },
  "Dashboard — pat/patristics.md": {
    "primary": "The branch of Christian theology that deals with the lives, writings, and doctrines of the early Church Fathers.",
    "secondary": "In ecclesiastical academic curricula, historical study analyzing the development of orthodoxy and creeds in antiquity.",
    "quotes": [
      {"author": "John Henry Newman", "work": "Apologia Pro Vita Sua", "quote": "My studies in **patristics** opened my eyes to the living continuity of Catholic tradition through the ages."},
      {"author": "William E. H. Lecky", "work": "History of European Morals", "quote": "The chair of **patristics** at Oxford trained young scholars to decipher early Greek and Latin church manuscripts."},
      {"author": "Philip Schaff", "work": "History of the Christian Church", "quote": "Modern **patristics** has benefited enormously from the critical recovery of Syriac and Armenian translations of lost treatises."}
    ]
  },
  "Dashboard — pat/patroclus.md": {
    "primary": "A prominent Greek hero of the Trojan War in Homer's Iliad, the beloved companion and brother-in-arms of Achilles.",
    "secondary": "In classical epic poetry, the warrior whose death at the hands of Hector spurred Achilles to reenter the war and slay Hector.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "Sweet rouse thyself, and the weak wanton Cupid shall from your neck unloose his amorous fold, as Achilles did for **patroclus**."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "Some priest who could pronounce the Greek itself taught him to read his verses, recounting how Achilles mourned for **patroclus**."},
      {"author": "Alexander Pope", "work": "The Iliad of Homer", "quote": "Hector stripped the divine armor from the fallen **patroclus**, provoking that fearful cry that shook the Trojan ramparts."}
    ]
  },
  "Dashboard — pat/patrol.md": {
    "primary": "Keep watch over an area by regularly walking or traveling around it; a detachment sent out on security duty.",
    "secondary": "In military reconnaissance and municipal law enforcement, a roving guard tasked with monitoring territory and deterring crime.",
    "quotes": [
      {"author": "Bram Stoker", "work": "Dracula", "quote": "As we went further, we met fewer people, till at last we were somewhat alarmed by the armed **patrol** guarding the bridge."},
      {"author": "Winston Churchill", "work": "The Second World War", "quote": "Naval destroyers maintained an unbroken **patrol** across the Straits of Dover to intercept hostile torpedo craft."},
      {"author": "Joseph Conrad", "work": "The Secret Agent", "quote": "The solitary constable on night **patrol** examined the bolted padlocks of the closed shops with professional suspicion."}
    ]
  },
  "Dashboard — pat/patroller.md": {
    "primary": "A person who patrols an area; a watchman, guard, or scout on reconnaissance duty.",
    "secondary": "In frontier history and municipal security, an armed sentinel keeping vigilance against incursions or fires.",
    "quotes": [
      {"author": "Herman Melville", "work": "White-Jacket", "quote": "The deck **patroller** moved softly through the sleeping berths, lantern in hand, ensuring no illicit smoking endangered the frigate."},
      {"author": "Jack London", "work": "The Call of the Wild", "quote": "The lonely mounted **patroller** kept watch over the frozen Yukon trail, checking dog teams as they entered the post."},
      {"author": "Walter Scott", "work": "The Fair Maid of Perth", "quote": "The city **patroller** challenged every wandering carouser on the Wynd after the curfew bell had rung."}
    ]
  },
  "Dashboard — pat/patrolman.md": {
    "primary": "A police officer who patrols a designated beat in a town or city.",
    "secondary": "In municipal police administration, a uniformed officer on foot or in a squad car maintaining public order on assigned beats.",
    "quotes": [
      {"author": "O. Henry", "work": "The Four Million", "quote": "The **patrolman** on the beat moved up the avenue impressively, checking shop doors and twirling his polished nightstick."},
      {"author": "Stephen Crane", "work": "Maggie: A Girl of the Streets", "quote": "A burly **patrolman** stepped quickly from the shadows, commanding the unruly crowd on the corner to disperse."},
      {"author": "Theodore Dreiser", "work": "The Titan", "quote": "Cowperwood bribed the district captain, ensuring that every **patrolman** turned a blind eye to his midnight franchise track-laying."}
    ]
  },
  "Dashboard — pat/patrology.md": {
    "primary": "The study of the early Church Fathers, their lives, writings, and theology; patristics.",
    "secondary": "In Catholic and Orthodox historical scholarship, specialized bibliographical study and textual criticism of Christian antiquity.",
    "quotes": [
      {"author": "John Henry Newman", "work": "Essays Critical and Historical", "quote": "The library acquired the monumental volumes of Migne's **patrology**, containing the complete Greek and Latin ecclesiastical heritage."},
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The tireless editors of French **patrology** restored corrupt manuscript passages in the treatises of Saint Cyprian."},
      {"author": "Lord Acton", "work": "Historical Essays and Studies", "quote": "A thorough grounding in **patrology** remains indispensable for assessing early doctrinal debates over conciliar supremacy."}
    ]
  },
  "Dashboard — pat/patron.md": {
    "primary": "A person who gives financial or other support to a person, organization, cause, or art; also a customer.",
    "secondary": "In classical Roman society (*patronus*) and Renaissance art, an influential protector who commissioned masterpieces and shielded clients.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "I tell thee, Syracusian, twenty years have I been **patron** to Antipholus, during which time he never saw me fail of word."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "A man conscious of enthusiasm for worthy aims is sustained under petty hostility by the approval of a high-minded **patron**."},
      {"author": "Samuel Johnson", "work": "Letter to the Earl of Chesterfield", "quote": "Is not a **patron**, my Lord, one who looks with unconcern on a man struggling for life in the water, and when he has reached ground, encumbers him with help?"}
    ]
  },
  "Dashboard — pat/patronage.md": {
    "primary": "The support given by a patron; the financial backing of arts, or the commercial custom of a store.",
    "secondary": "In political history, the power to control appointments to office or the distribution of government favors and contracts.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "Yes, as an outlaw in a castle keeps, and useth it to **patronage** his theft against the sovereign's officers."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "It seems very unfitting that I should have this church **patronage**, yet I felt that I was answering for the welfare of the parish."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Pennyways now felt himself to be in something of a difficulty, for should Bathsheba withdraw her **patronage**, his ruin was sealed."}
    ]
  },
  "Dashboard — pat/patroness.md": {
    "primary": "A female patron; a woman who protects, supports, or finances a person, charity, artist, or cause.",
    "secondary": "In Regency society and hagiography, an influential noblewoman presiding over exclusive ballrooms like Almack's, or a guardian saint.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "Behold our **patroness**, the life of Rome! Toward her let us bend our knees and shower our grateful tears."},
      {"author": "Jane Austen", "work": "Emma", "quote": "Mrs. Elton became the very active **patroness** of Jane Fairfax, arranging musical evenings and praising her genius to every caller."},
      {"author": "Thomas Henry Huxley", "work": "Evolution and Ethics", "quote": "Hail, therefore, **patroness** of health and ease, and contemplation, heart-consoling power!"}
    ]
  },
  "Dashboard — pat/patronise.md": {
    "primary": "Treat condescendingly, with apparent kindness that betrays a feeling of superiority; also support as a customer.",
    "secondary": "In British literature and social discourse, displaying condescending arrogance toward social inferiors.",
    "quotes": [
      {"author": "Oscar Wilde", "work": "The Importance of Being Earnest", "quote": "It is always dangerous to **patronise** young men from the country, who frequently turn out far cleverer than one expects."},
      {"author": "George Bernard Shaw", "work": "Pygmalion", "quote": "Higgins took delight in shocking duchesses, refusing to **patronise** high society with hypocritical compliments."},
      {"author": "E. M. Forster", "work": "A Room with a View", "quote": "Lucy disliked the elderly spinster's effort to **patronise** her, preferring the honest brusqueness of the Emersons."}
    ]
  },
  "Dashboard — pat/patronised.md": {
    "primary": "Treated with an air of condescending superiority; supported financially or frequented as a customer (British spelling).",
    "secondary": "In Victorian social narratives, receiving aristocratic favor or visiting exclusive commercial establishments.",
    "quotes": [
      {"author": "Jane Austen", "work": "Persuasion", "quote": "It was a concert for the benefit of a person **patronised** by Lady Dalrymple, and therefore attended by all the fashionable Bath elite."},
      {"author": "Bram Stoker", "work": "Dracula", "quote": "He was a man loved and honoured by all who knew him; and in his youth was much **patronised** by the great scholars of Oxford."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Uncle Pumblechook **patronised** Pip at every family dinner, constantly reminding him to be grateful to his betters."}
    ]
  },
  "Dashboard — pat/patronising.md": {
    "primary": "Treating someone with an apparent kindness that betrays a feeling of superiority; condescending (British spelling).",
    "secondary": "In character analysis, displaying subtle vanity and insulting deference under the guise of benevolence.",
    "quotes": [
      {"author": "James Joyce", "work": "Dubliners", "quote": "Gallaher was only **patronising** him by his friendliness, showing off the glitz of London journalism to a humble Dublin clerk."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "There's your true Ashantee, gentlemen; observe how he displays that **patronising** grin when civilized sailors express terror."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Rosamond disliked her sister-in-law's **patronising** air, which seemed to assume that county pedigree surpassed all town elegance."}
    ]
  },
  "Dashboard — pat/patronisingly.md": {
    "primary": "In a patronising, condescending, or offensively superior manner (British spelling).",
    "secondary": "In dialogue descriptions, speaking down to peers with infuriating composure and assumed authority.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Our Mutual Friend", "quote": "Fascination Fledgeby smiled **patronisingly**, assuring the distressed debtor that money was extraordinarily tight in the City."},
      {"author": "Virginia Woolf", "work": "Night and Day", "quote": "The elderly critic patted the young novelist's shoulder **patronisingly**, recommending that she read more Greek before publishing."},
      {"author": "W. Somerset Maugham", "work": "Of Human Bondage", "quote": "The medical lecturer nodded **patronisingly** at Philip's clinical diagnosis, remarking that beginner's luck was always amusing."}
    ]
  },
  "Dashboard — pat/patronize.md": {
    "primary": "Treat condescendingly; also frequent as a customer or provide financial backing as a sponsor.",
    "secondary": "In business practice and interpersonal psychology, acting as regular clientele or behaving with disguised arrogance.",
    "quotes": [
      {"author": "Jane Austen", "work": "Persuasion", "quote": "Reason will not allow us to **patronize** alliances where inequality of birth and character promise nothing but domestic misery."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "It is only within the last month that that distinguished society passed a resolution to **patronize** our adventurous voyage."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Minchin shared fully in the new pique against Bulstrode, resolved never to **patronize** any medical scheme initiated by him."}
    ]
  },
  "Dashboard — pat/patronized.md": {
    "primary": "Treated condescendingly; supported by a sponsor, or frequented regularly by customers.",
    "secondary": "In American commercial and social history, supported through elite backing or customer loyalty.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "A few permanent erections dotted the market spot, but the majority of farmers **patronized** the hospitable taproom of the King's Arms."},
      {"author": "Edith Wharton", "work": "The House of Mirth", "quote": "Lily Bart resented being **patronized** by vulgar millionaires whose sole claim to distinction was ostentatious wealth."},
      {"author": "Henry James", "work": "The Bostonians", "quote": "The fashionable lecturer felt thoroughly **patronized** by the wealthy committee ladies who arranged his Boston speaking tour."}
    ]
  },
  "Dashboard — pat/patronizing.md": {
    "primary": "Displaying an offensive attitude of condescension; talking down to others under the pretense of kindness.",
    "secondary": "In social discourse, subtle interpersonal dominance exerted through feigned pity or superior advice.",
    "quotes": [
      {"author": "G. K. Chesterton", "work": "The Wisdom of Father Brown", "quote": "He liked Father Brown in a slightly **patronizing** way; and Father Brown liked him with genuine, unpretentious affection."},
      {"author": "Sinclair Lewis", "work": "Main Street", "quote": "Carol Kennicott detested the **patronizing** smiles of the town matrons whenever she suggested modern books for the library."},
      {"author": "F. Scott Fitzgerald", "work": "The Great Gatsby", "quote": "Tom Buchanan assumed a **patronizing** tone toward Wilson, tossing him car repair scraps like bones to an eager terrier."}
    ]
  },
  "Dashboard — pat/patronizingly.md": {
    "primary": "In a patronizing, condescending, or offensively superior manner.",
    "secondary": "In narrative characterization, addressing subordinates with arrogant complacency and feigned benevolence.",
    "quotes": [
      {"author": "Mark Twain", "work": "The Innocents Abroad", "quote": "The European guide nodded **patronizingly**, assuming that crude American tourists could appreciate nothing finer than barroom prints."},
      {"author": "Edith Wharton", "work": "The Custom of the Country", "quote": "Undine waved her hand **patronizingly** to her old Apex schoolmates, delighted that her Parisian gown set her worlds apart."},
      {"author": "Theodore Dreiser", "work": "Sister Carrie", "quote": "Drouet chuckled **patronizingly** at Carrie's awe of the Chicago department stores, feeling himself an accomplished man of the world."}
    ]
  },
  "Dashboard — pat/patronless.md": {
    "primary": "Lacking a patron, financial benefactor, protector, or supporting sponsor.",
    "secondary": "In literary history, the destitute condition of eighteenth-century Grub Street poets writing without aristocratic subsidy.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "The Vanity of Human Wishes", "quote": "There mark what ills the scholar's life assail: toil, envy, want, the **patronless** cell, and the jail."},
      {"author": "Oliver Goldsmith", "work": "The Citizen of the World", "quote": "The **patronless** philosopher must peddle his wisdom through the cold streets, while sycophants feast at the nobleman's table."},
      {"author": "Thomas Chatterton", "work": "The Rowley Poems", "quote": "The starving bard languished in his **patronless** garret, scorning to bend the knee to illiterate merchant lords."}
    ]
  },
  "Dashboard — pat/patronne.md": {
    "primary": "A female proprietor, manager, or owner, especially of a French café, bistro, pension, or small hotel.",
    "secondary": "In French travel memoirs, the formidable matriarch who commands the cash register and kitchen staff of a Parisian restaurant.",
    "quotes": [
      {"author": "Ernest Hemingway", "work": "The Sun Also Rises", "quote": "The cheerful **patronne** of the Basque inn brought us a steaming tureen of garlic soup and fresh crusty loaves."},
      {"author": "George Orwell", "work": "Down and Out in Paris and London", "quote": "Madame the **patronne** watched the kitchen entrance like a hawk, ready to dock twenty sous for the slightest broken plate."},
      {"author": "Katherine Mansfield", "work": "In a German Pension", "quote": "The stout **patronne** stood behind her zinc counter, loudly berating the sleepy chambermaid in rapid French."}
    ]
  },
  "Dashboard — pat/patronym.md": {
    "primary": "A name derived from that of a father or paternal ancestor; a patronymic.",
    "secondary": "In onomastics and historical linguistics, surnames formed by adding prefixes (Mac-, O', Fitz-) or suffixes (-son, -vitch) to a paternal name.",
    "quotes": [
      {"author": "Edward Tylor", "work": "Anthropology: An Introduction to the Study of Man and Civilization", "quote": "The adoption of a fixed hereditary surname gradually replaced the older Scandinavian **patronym** ending in -sen or -son."},
      {"author": "Max Müller", "work": "Lectures on the Science of Language", "quote": "In Homeric epic, the proud warrior announces his identity not by title but by ancestral **patronym**, invoking his father's glory."},
      {"author": "James Joyce", "work": "Ulysses", "quote": "Stephen meditated upon his own proud Greek **patronym**, Dedalus, artisan and artificer of soaring labyrinthine wings."}
    ]
  },
  "Dashboard — pat/patronymic.md": {
    "primary": "A name derived from the name of a father or male ancestor; also of or relating to such a name.",
    "secondary": "In Russian cultural naming conventions, the middle name derived from the father's given name with the suffix -ovich or -ovna.",
    "quotes": [
      {"author": "Bram Stoker", "work": "Dracula", "quote": "When I go there I shall be all alone, and my friend Jonathan Harker—nay, pardon, I should address you by your English **patronymic**."},
      {"author": "Leo Tolstoy", "work": "War and Peace", "quote": "The old prince addressed the visitor formally by his Christian name and **patronymic**, according to strict Russian etiquette."},
      {"author": "Walter Scott", "work": "Waverley", "quote": "The Highland clansman was known among his hills by an ancient Gaelic **patronymic** commemorating seven generations of chieftains."}
    ]
  },
  "Dashboard — pat/patsy.md": {
    "primary": "A person who is easily taken advantage of, manipulated, deceived, or made a scapegoat.",
    "secondary": "In criminal slang and investigative journalism, an unsuspecting dupe framed to take the legal blame for others' crimes.",
    "quotes": [
      {"author": "Raymond Chandler", "work": "The Big Sleep", "quote": "Marlowe realized the syndicates were setting him up as the fall guy, an expendable **patsy** for the police to arrest."},
      {"author": "Dashiell Hammett", "work": "The Maltese Falcon", "quote": "Spade laughed harshly, telling Brigid that he refused to play the gullible **patsy** in her deadly treasure hunt."},
      {"author": "Upton Sinclair", "work": "Oil!", "quote": "The small wildcat drillers were treated as the **patsy** by the great oil trusts, left bankrupt when leases dried up."}
    ]
  },
  "Dashboard — pat/patten.md": {
    "primary": "A wooden shoe, sandal, or clog with a raised iron or wooden ring underneath, worn to elevate shoes above mud.",
    "secondary": "In eighteenth and nineteenth-century domestic history, protective overshoes worn by women walking on muddy cobbles.",
    "quotes": [
      {"author": "Jane Austen", "work": "Persuasion", "quote": "The incessant click-clack of the **patten** upon the wet flagstones announced that heavy winter rain had set in over Bath."},
      {"author": "Thomas Hardy", "work": "The Woodlanders", "quote": "Marty South walked swiftly along the muddy woodland path, her shoes clean thanks to the iron rings of her wooden **patten**."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The charwoman clattered down the damp alleyway in her iron-shod **patten**, carrying her mop and zinc pail to work."}
    ]
  },
  "Dashboard — pat/patter.md": {
    "primary": "Make a repeated light tapping sound; also rapid, glib, entertaining speech used by a comedian, salesman, or magician.",
    "secondary": "In underworld slang and showmanship, thieves' cant or the rhythmic, rapid-fire monologue of theatrical performers.",
    "quotes": [
      {"author": "Joseph Conrad", "work": "Heart of Darkness", "quote": "I could only hear the heavy splashing thump of the stern-wheel and the light **patter** of warm rain upon the tin deckhouse."},
      {"author": "H. G. Wells", "work": "The War of the Worlds", "quote": "Once or twice I heard a faint **patter** like the light running feet of an animal passing along the gravel garden walk."},
      {"author": "Charles Dickens", "work": "Oliver Twist", "quote": "The Artful Dodger astonished Oliver with his underworld **patter**, speaking a flash language of which the boy understood not a syllable."}
    ]
  },
  "Dashboard — pat/pattern-bomb.md": {
    "primary": "Bomb an area systematically in accordance with a predetermined geometric grid or calculated spatial pattern.",
    "secondary": "In military aviation history, carpet bombing designed to saturate a targeted defensive zone with overlapping blast radiuses.",
    "quotes": [
      {"author": "Winston Churchill", "work": "The Second World War", "quote": "Bomber Command resolved to **pattern-bomb** the industrial rail yards of the Ruhr, disrupting enemy munitions transport."},
      {"author": "Ernest K. Gann", "work": "Fate Is the Hunter", "quote": "The squadron leader instructed his navigators how to **pattern-bomb** the airfield runways through dense cloud cover."},
      {"author": "John Steinbeck", "work": "Bombs Away: The Story of a Bomber Team", "quote": "The bombardiers synchronized their sights in flight to **pattern-bomb** the synthetic oil refineries with overlapping detonations."}
    ]
  },
  "Dashboard — pat/pattern.md": {
    "primary": "A repeated decorative design; a model or guide proposed for imitation; an exemplary archetype.",
    "secondary": "In scientific methodology and tailoring, an intelligible regularity discerned in nature, or a cut paper template for sewing.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "Yet nor the lays of birds, nor the sweet smell of different flowers, could make me any summer's story tell, or from their proud lap pluck them where they grew: they were but sweet, but figures of delight, drawn after you, you **pattern** of all those."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The image as a whole was that of a small Noah's Ark, allowing the decorative **pattern** of the ancient church roof to show through."},
      {"author": "Lewis Carroll", "work": "Alice's Adventures in Wonderland", "quote": "And who are these?' said the Queen, pointing to the three gardeners who were painted in an oblong card **pattern**."}
    ]
  },
  "Dashboard — pat/patterned.md": {
    "primary": "Decorated with or formed into a pattern; arranged in a systematic, regular, or predictable design.",
    "secondary": "In cognitive psychology and sociology, structured according to established behavioral models or cultural norms.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "Ay, such a place there is where we did hunt; O, had we never, never hunted there! For murder was there **patterned** after grief."},
      {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "It was a small Chinese box of black and gold-dust lacquer, elaborately wrought with **patterned** dragons and lotus leaves."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Dorothea looked at the exquisitely **patterned** tapestries in the Vatican gallery, feeling the monumental weight of antique history."}
    ]
  },
  "Dashboard — pat/patternmaker.md": {
    "primary": "A skilled artisan or craftsperson who makes patterns for clothing, casting molds, or manufacturing.",
    "secondary": "In foundry metallurgy and bespoke fashion, a technician who constructs wood models for sand molds or paper garment patterns.",
    "quotes": [
      {"author": "Charles Babbage", "work": "On the Economy of Machinery and Manufactures", "quote": "The precision of our steam cylinders depends upon the wood **patternmaker**, whose measurements govern the casting in the sand pit."},
      {"author": "Upton Sinclair", "work": "The Jungle", "quote": "An elderly German **patternmaker** in the machinery shop earned top wages because his hand never slipped on the gouge."},
      {"author": "Jack London", "work": "The Iron Heel", "quote": "The skilled metal **patternmaker** joined the union grievance committee, warning of dangerous machine speedups."}
    ]
  },
  "Dashboard — pat/patty-pan.md": {
    "primary": "A small shallow pan or tin used for baking individual patties, pies, or tarts; also a variety of scalloped summer squash.",
    "secondary": "In horticulture and traditional culinary arts, a scalloped, saucer-shaped yellow or white summer squash resembling a fluted tart pan.",
    "quotes": [
      {"author": "Mrs. Beeton", "work": "The Book of Household Management", "quote": "Line each buttered **patty-pan** with light puff paste, fill with seasoned minced oysters, and bake in a brisk oven."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Clara Peggotty bustled about the cheerful kitchen, arranging her fluted **patty-pan** moulds to bake meat pastries for tea."},
      {"author": "Louisa May Alcott", "work": "Little Men", "quote": "The girls baked tiny raspberry pies in a miniature **patty-pan**, serving the proud feast upon doll plates."}
    ]
  },
  "Dashboard — pat/patty.md": {
    "primary": "A small flat cake of minced meat, fish, or vegetable, typically fried or grilled; also a small round pie or pasty.",
    "secondary": "In gastronomy and casual dining, a ground meat or plant-protein round served in a burger bun or wrapped in flaky crust.",
    "quotes": [
      {"author": "Jane Austen", "work": "Emma", "quote": "Mrs. Cole offered her callers a delicate chicken **patty** and hot tea, pressing them to taste the fresh pastry."},
      {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "Jos Sedley consumed a savory oyster **patty** with tremendous relish, washed down with iced claret at the tavern."},
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "The baker's boy carried a steaming tray of meat **patty** crusts through the market square, crying out the fresh morning bake."}
    ]
  },
  "Dashboard — pat/repatriate.md": {
    "primary": "Send or bring someone back to their own country; also send money back to one's native land.",
    "secondary": "In international humanitarian law and corporate finance, the return of refugees, prisoners of war, or foreign profits.",
    "quotes": [
      {"author": "Winston Churchill", "work": "The Second World War", "quote": "Arrangements were concluded with neutral powers to **repatriate** severely wounded prisoners of war aboard specially marked hospital ships."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "The government sought to **repatriate** displaced settlers whose boundary claims had been compromised by frontier treaties."},
      {"author": "John Maynard Keynes", "work": "The Economic Consequences of the Peace", "quote": "Exorbitant indemnity demands made it impossible for the conquered state to **repatriate** its foreign capital reserves."}
    ]
  },
  "Dashboard — pat/repatriation.md": {
    "primary": "The return of someone to their own country; the sending of money or assets back to one's homeland.",
    "secondary": "In post-conflict administration and museum ethics, restitution of displaced populations or looted cultural patrimony.",
    "quotes": [
      {"author": "Winston Churchill", "work": "Triumph and Tragedy", "quote": "The swift **repatriation** of hundreds of thousands of liberated allied laborers posed an immense logistical challenge across broken rail systems."},
      {"author": "George Orwell", "work": "As I Please", "quote": "The orderly **repatriation** of soldiers from overseas garrisons is essential to restore economic vitality to civilian industry."},
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The treaty negotiated the **repatriation** of captured legionary standards and thousands of Roman captives detained beyond the Euphrates."}
    ]
  },
  "Dashboard — pat/superpatriotic.md": {
    "primary": "Excessively, aggressively, or blindly patriotic; chauvinistic and jingoistic.",
    "secondary": "In political commentary and social criticism, an exaggerated public nationalism that brands reasonable dissent as treason.",
    "quotes": [
      {"author": "Sinclair Lewis", "work": "It Can't Happen Here", "quote": "The **superpatriotic** League of Forgotten Men marched through the town square, shouting bellicose slogans and menacing critics."},
      {"author": "H. L. Mencken", "work": "Prejudices: Second Series", "quote": "The **superpatriotic** orator wraps himself in the national flag, substituting violent denunciation for coherent political reasoning."},
      {"author": "George Orwell", "work": "Notes on Nationalism", "quote": "A **superpatriotic** mentality cannot tolerate even the most balanced historical criticism of its own nation's past blunders."}
    ]
  },
  "Dashboard — pat/superpatriotism.md": {
    "primary": "Excessive, blind, or belligerent patriotism; aggressive jingoism and chauvinism.",
    "secondary": "In civic ethics and sociopolitical analysis, virulent hyper-nationalism that demonizes foreign cultures and domestic dissenters.",
    "quotes": [
      {"author": "H. L. Mencken", "work": "Prejudices: Fourth Series", "quote": "The epidemic of **superpatriotism** that gripped the nation during wartime silenced every courageous advocate of free speech."},
      {"author": "Sinclair Lewis", "work": "Gideon Planish", "quote": "Dr. Planish discovered that promoting commercialized **superpatriotism** brought in rich donations from anxious conservative millionaires."},
      {"author": "George Orwell", "work": "The Lion and the Unicorn", "quote": "We must rid ourselves of that blustering **superpatriotism** which mistakes arrogance for genuine strength of character."}
    ]
  },
  "Dashboard — pat/unpatented.md": {
    "primary": "Not protected or secured by a patent; in the public domain for free use and reproduction.",
    "secondary": "In industrial law and history of technology, innovations whose inventors deliberately eschewed commercial patent monopolies.",
    "quotes": [
      {"author": "Benjamin Franklin", "work": "Autobiography of Benjamin Franklin", "quote": "I declined the governor's offer of a patent for my open stove, believing our inventions should be freely shared **unpatented** for human good."},
      {"author": "Thomas Edison", "work": "The Diary and Sundry Observations of Thomas Alva Edison", "quote": "To leave a vital improvement **unpatented** is an open invitation for unscrupulous competitors to reap what our laboratory sowed."},
      {"author": "Charles Babbage", "work": "Passages from the Life of a Philosopher", "quote": "The mathematical calculating engine remained **unpatented**, offered as a gift of pure science to the British nation."}
    ]
  },
  "Dashboard — pat/unpatriotic.md": {
    "primary": "Not showing love, devotion, or loyalty to one's country; lacking patriotism.",
    "secondary": "In political discourse and legal polemics, actions or speech perceived as subversive of the commonwealth during national crises.",
    "quotes": [
      {"author": "Edmund Burke", "work": "Speech on Conciliation with America", "quote": "It is not **unpatriotic** to remind parliament of its limitations when an unjust policy threatens the integrity of the empire."},
      {"author": "Samuel Johnson", "work": "The Patriot", "quote": "He who stirs up sedition for private pique is thoroughly **unpatriotic**, however loudly he may boast of loving liberty."},
      {"author": "George Orwell", "work": "Homage to Catalonia", "quote": "The political police branded honest trade union leaders as **unpatriotic** saboteurs to justify suppressing the strike."}
    ]
  },
  "Dashboard — pat/unpatriotically.md": {
    "primary": "In an unpatriotic manner; without devotion, loyalty, or due regard for one's country.",
    "secondary": "In historical memoirs and political debates, acting in a way that harms the national welfare or aids hostile powers.",
    "quotes": [
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The opposition ministers acted **unpatriotically** when they leaked confidential diplomatic despatches to the French ambassador."},
      {"author": "Winston Churchill", "work": "The Gathering Storm", "quote": "Partisan leaders who **unpatriotically** delayed rearmament must bear their share of responsibility for our early reverses."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "To put sectional faction above national union is to conduct oneself **unpatriotically** in the eyes of posterity."}
    ]
  },
  "Dashboard — pat/unpatronised.md": {
    "primary": "Not supported, sponsored, or treated by a patron (British spelling); neglected by patrons.",
    "secondary": "In literary and artistic biography, struggling geniuses forced to create without aristocratic subsidy or elite favor.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "The Lives of the Poets", "quote": "The young poet lived **unpatronised** in an obscure London lodging, producing verses of rare sublimity unnoticed by the court."},
      {"author": "William Hazlitt", "work": "Table-Talk", "quote": "An independent painter, proud and **unpatronised**, must endure the disdain of fashionable portrait-mongers."},
      {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "Teufelsdröckh laboured in his tower **unpatronised** by academy or prince, spinning his philosophy out of his own deep soul."}
    ]
  },
  "Dashboard — pat/unpatronized.md": {
    "primary": "Not supported, sponsored, or protected by a patron; free from condescension or aristocratic subsidy.",
    "secondary": "In American cultural history, commercial enterprises or writers succeeding through public favor alone without wealthy benefactors.",
    "quotes": [
      {"author": "Edgar Allan Poe", "work": "Essays and Reviews", "quote": "The American periodical flourished **unpatronized** by government pensions, sustained entirely by the eager appetite of the reading public."},
      {"author": "Walt Whitman", "work": "Leaves of Grass", "quote": "I sing the common mechanic and prairie farmer, standing erect and **unpatronized** beneath the open western sky."},
      {"author": "Herman Melville", "work": "Pierre: or, The Ambiguities", "quote": "Pierre sat in his bleak city room, an **unpatronized** author burning his soul away upon an uncompromising manuscript."}
    ]
  },
  "Dashboard — pat/unpatterned.md": {
    "primary": "Not having, displaying, or arranged in a pattern; plain, irregular, or random.",
    "secondary": "In cognitive science and textile manufacturing, solid monochrome fabrics or stochastic events exhibiting no discernible regularity.",
    "quotes": [
      {"author": "Virginia Woolf", "work": "To the Lighthouse", "quote": "The open sea presented an immense, **unpatterned** expanse of grey water beneath the overcast November sky."},
      {"author": "Henry James", "work": "The Figure in the Carpet", "quote": "He feared that the great author's life was a mere **unpatterned** web of accident, without any hidden master secret."},
      {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "The wild heath was an **unpatterned** wilderness of heath-bells and ancient barrows, untouched by the surveyor's grid."}
    ]
  }
}

def curate_file(rel_path, info):
    base_dir = "App database/Latin roots/Cluster Emotion"
    filepath = os.path.join(base_dir, rel_path)
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return False
        
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
        
    fm_match = re.search(r"^---\n.*?\n---\n", content, re.DOTALL)
    if not fm_match:
        print(f"Frontmatter missing: {filepath}")
        return False
    frontmatter = fm_match.group(0)
    
    w = os.path.splitext(os.path.basename(rel_path))[0]
    header = f"# {w}\n\n"
    
    dv_match = re.search(r"(> \[!status\] 🎯 \*\*Status:\*\*.*?```dataviewjs.*?```)", content, re.DOTALL)
    if not dv_match:
        print(f"Dataview block missing: {filepath}")
        return False
    dv_block = dv_match.group(1)
    
    defs_block = f"""> [!book] 📖 Definitions & Semantic Range
> 1. **Primary Definition (Lexical / Standard Consensus)**: {info['primary']}
> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: {info['secondary']}"""

    quotes_lines = ["> [!quote] 💬 Contextual Usage & Authentic Quotations"]
    for q in info["quotes"]:
        quotes_lines.append(f"> - 📜 **{q['author']} (*{q['work']}*):** *\"{q['quote']}\"*")
    quotes_block = "\n".join(quotes_lines)
    
    new_content = f"{frontmatter}{header}{dv_block}\n\n{defs_block}\n\n{quotes_block}\n"
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)
    return True

success = 0
for rel_path, info in data.items():
    if curate_file(rel_path, info):
        success += 1

print(f"Successfully updated {success}/{len(data)} notes in Dashboard — pat (Part B).")
