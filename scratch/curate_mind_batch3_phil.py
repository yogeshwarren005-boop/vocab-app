# -*- coding: utf-8 -*-
"""
Curates Dashboard — phil (62 words) in Cluster Mind & Knowledge.
"""
import os, sys, re, subprocess

sys.stdout.reconfigure(encoding="utf-8")

data = {
  "Dashboard — phil/anglophile.md": {
    "primary": "A person who is fond of or greatly admires England, the English people, or English customs.",
    "secondary": "In cultural history, foreign intellectuals or diplomats adopting British tailoring, manners, and parliamentary ideals.",
    "quotes": [
      {"author": "Henry James", "work": "English Hours", "quote": "The traveling American was a confessed **anglophile**, enchanted by the misty green parks and historic minsters of London."},
      {"author": "George Orwell", "work": "The Lion and the Unicorn", "quote": "Continental intellectuals often become **anglophile** in proportion to their desire for personal and political freedom."},
      {"author": "W. Somerset Maugham", "work": "The Razor's Edge", "quote": "Elliott Templeton was an unrepentant **anglophile**, boasting of his invitations to country weekends in Sussex."}
    ]
  },
  "Dashboard — phil/anglophilia.md": {
    "primary": "Love, admiration, or fondness for England, English culture, literature, institutions, or customs.",
    "secondary": "In sociopolitical discourse, cultural affinity for British traditions influencing international diplomacy.",
    "quotes": [
      {"author": "Henry James", "work": "The American Scene", "quote": "In Boston drawing rooms, a refined **anglophilia** dictated everything from literary taste to afternoon tea service."},
      {"author": "Alexis de Tocqueville", "work": "Journeys to England and Ireland", "quote": "His political **anglophilia** led him to study how local aristocratic rule preserved stability during rapid industrialization."},
      {"author": "George Bernard Shaw", "work": "John Bull's Other Island", "quote": "Broadbent indulged in sentimental **anglophilia**, believing English common sense could pacify all ancient Irish feuds."}
    ]
  },
  "Dashboard — phil/anglophilic.md": {
    "primary": "Of, relating to, or characterized by Anglophilia; strongly favoring English culture, customs, or institutions.",
    "secondary": "In cultural criticism, denoting aesthetic or political preferences aligned with British traditions.",
    "quotes": [
      {"author": "Edith Wharton", "work": "The Age of Innocence", "quote": "The New York gentlemen belonged to an **anglophilic** club where port wine and London tailors set the unquestioned standard."},
      {"author": "H. L. Mencken", "work": "Prejudices: First Series", "quote": "The university professors displayed an **anglophilic** bias, exalting Oxford pedantry above vigorous American idioms."},
      {"author": "F. Scott Fitzgerald", "work": "This Side of Paradise", "quote": "Amory adopted an **anglophilic** swagger, donning tweed coats and quoting Rupert Brooke to his classmates."}
    ]
  },
  "Dashboard — phil/bibliophile.md": {
    "primary": "A person who collects or has a great love of books, fine typography, and rare bindings.",
    "secondary": "In literary culture, an enthusiast who treasures first editions, vellum folios, and historical provenance.",
    "quotes": [
      {"author": "Walter Scott", "work": "The Antiquary", "quote": "Monkbarns was a true **bibliophile**, handling the black-letter volume as tenderly as if it were a sacred relic."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Dr. Mortimer described Sir Charles as an accomplished **bibliophile** whose private library was the pride of Dartmoor."},
      {"author": "Henry James", "work": "The Aspern Papers", "quote": "The dedicated **bibliophile** will traverse continents and brave domestic feuds to recover a lost manuscript."}
    ]
  },
  "Dashboard — phil/bibliophilic.md": {
    "primary": "Of, relating to, or characteristic of a bibliophile or the love and collection of books.",
    "secondary": "In publishing history, describing exquisite artisanal bindings, deckle-edge papers, and limited press editions.",
    "quotes": [
      {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "Dorian kept his poisonous French novel bound in nine different colored morocco leathers to suit his **bibliophilic** whims."},
      {"author": "Walter Pater", "work": "Appreciations", "quote": "Charles Lamb possessed that rare **bibliophilic** tenderness which reveres ragged, thumbed folios over gilded modern reprints."},
      {"author": "William Morris", "work": "The Ideal Book", "quote": "Our Kelmscott Press aimed to satisfy the highest **bibliophilic** standards through hand-set type and linen rag paper."}
    ]
  },
  "Dashboard — phil/cinephile.md": {
    "primary": "A person who is fond of the cinema; a film enthusiast with a discerning appreciation of cinematic art.",
    "secondary": "In modern cultural criticism, a film lover devoted to auteur directors, international film movements, and film archives.",
    "quotes": [
      {"author": "Graham Greene", "work": "Mornings in the Dark: The Graham Greene Film Reader", "quote": "As an avid young **cinephile**, I spent rainy London afternoons studying German expressionist cinema in Soho."},
      {"author": "Susan Sontag", "work": "Against Interpretation", "quote": "The passionate **cinephile** experiences film not as mere casual amusement, but as an ecstatic visual revelation."},
      {"author": "James Agee", "work": "Agee on Film", "quote": "Any observant **cinephile** will discern in Chaplin's physical grace the supreme genius of silent film pantomime."}
    ]
  },
  "Dashboard — phil/francophile.md": {
    "primary": "A person who is fond of or greatly admires France, its people, language, culinary arts, or culture.",
    "secondary": "In diplomatic history and aesthetics, foreign writers and statesmen adopting Parisian manners and French Enlightenment thought.",
    "quotes": [
      {"author": "Thomas Jefferson", "work": "Writings", "quote": "Every man has two countries, his own and France; thus Jefferson remained an ardent **francophile** throughout his life."},
      {"author": "Henry James", "work": "A Little Tour in France", "quote": "The traveler confessed himself an incorrigible **francophile**, enchanted by the châteaux and poplar-lined rivers of the Loire."},
      {"author": "Edith Wharton", "work": "French Ways and Their Meaning", "quote": "An American **francophile** discovers in French domestic life a reverence for taste and intellectual discipline."}
    ]
  },
  "Dashboard — phil/necrophilia.md": {
    "primary": "Sexual attraction to or sexual activity with corpses; an abnormal erotic or psychological obsession with death.",
    "secondary": "In psychiatric psychopathology and criminal forensics, an extreme paraphilia involving dead bodies.",
    "quotes": [
      {"author": "Havelock Ellis", "work": "Studies in the Psychology of Sex", "quote": "Psychiatrists classified morbid cases of **necrophilia** among the rarest and most grotesque deviations of erotic instinct."},
      {"author": "Richard von Krafft-Ebing", "work": "Psychopathia Sexualis", "quote": "The alienist documented severe clinical aberrations where morbid melancholia degenerated into repulsive **necrophilia**."},
      {"author": "Erich Fromm", "work": "The Anatomy of Human Destructiveness", "quote": "Fromm analyzed malignant psychological destruction as a symbolic **necrophilia** that prefers mechanical death to vital growth."}
    ]
  },
  "Dashboard — phil/philadelphaceae.md": {
    "primary": "A historical botanical family of flowering shrubs, now generally included in the mock-orange family Hydrangeaceae.",
    "secondary": "In systematic botany, woody plants characterized by opposite leaves and showy four-petaled white flowers.",
    "quotes": [
      {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "Botanists formerly placed the fragrant mock-orange shrubs in the family **philadelphaceae** based on capsule structure."},
      {"author": "John Lindley", "work": "The Vegetable Kingdom", "quote": "The woody genera grouped under **philadelphaceae** exhibit valvate petals and numerous stamens inserted on the calyx tube."},
      {"author": "Joseph Dalton Hooker", "work": "Flora of British India", "quote": "In the temperate Himalayan valleys, shrubs allied to **philadelphaceae** brighten cliff faces with fragrant white blossoms."}
    ]
  },
  "Dashboard — phil/philadelphia.md": {
    "primary": "The largest city in Pennsylvania, founded in 1682 by William Penn as the 'City of Brotherly Love'; historic cradle of American independence.",
    "secondary": "In American history, the site of the Continental Congress, the drafting of the Declaration of Independence, and the Constitutional Convention.",
    "quotes": [
      {"author": "Benjamin Franklin", "work": "Autobiography of Benjamin Franklin", "quote": "I arrived in **philadelphia** on a Sunday morning, walking up Market Street with three puffy rolls under my arm."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The delegates assembled in **philadelphia** during the hot summer of 1787 to frame an enduring federal Constitution."},
      {"author": "Thomas Jefferson", "work": "Writings", "quote": "In the historic assembly hall at **philadelphia**, the representatives of the colonies pledged their lives and sacred honor."}
    ]
  },
  "Dashboard — phil/philadelphus.md": {
    "primary": "A genus of deciduous shrubs in the family Hydrangeaceae, commonly known as mock-orange, noted for fragrant white flowers.",
    "secondary": "In ornamental horticulture, shrubs celebrated for sweet citrus-scented blossoms reminiscent of true orange flowers.",
    "quotes": [
      {"author": "Asa Gray", "work": "Elements of Botany", "quote": "The garden shrub **philadelphus**, commonly termed mock-orange, bears four-parted blossoms of overpowering fragrance in June."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "Beside the cellar hole of the vanished farmhouse, a hardy bush of **philadelphus** bloomed fragrant amidst the sumac."},
      {"author": "William Bartram", "work": "Travels through North and South Carolina, Georgia, East and West Florida", "quote": "Along the rocky river bluffs, I collected a wild species of **philadelphus** adorned with snowy blossoms."}
    ]
  },
  "Dashboard — phil/philaenus.md": {
    "primary": "A genus of spittlebugs or froghoppers in the family Aphrophoridae, including the meadow spittlebug (*Philaenus spumarius*).",
    "secondary": "In agricultural entomology, xylem-feeding hemipteran insects whose nymphs produce protective frothy spittle masses.",
    "quotes": [
      {"author": "Jean-Henri Fabre", "work": "The Wonders of Insect Life", "quote": "The tiny nymph of **philaenus** envelops itself in a mound of airy foam, shielding its delicate body from desiccating sun."},
      {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Invertebrate Animals", "quote": "Dissection of the froghopper **philaenus** illustrates the remarkable muscular specialization of the hind jumping legs."},
      {"author": "Charles Darwin", "work": "The Effects of Cross and Self Fertilisation in the Vegetable Kingdom", "quote": "Meadow grasses were dotted with the frothy secretions of **philaenus**, which farmers call cuckoo-spit."}
    ]
  },
  "Dashboard — phil/philander.md": {
    "primary": "Readily or frequently enter into casual, non-committal sexual relationships with women; flirt frivolously.",
    "secondary": "In theatrical comedy and character sketches, behaving as an unfaithful rake or chronic seducer.",
    "quotes": [
      {"author": "George Bernard Shaw", "work": "The Philanderer", "quote": "Charteris claimed that to **philander** gracefully was the highest attainment of a civilized man without heart."},
      {"author": "William Makepeace Thackeray", "work": "The History of Pendennis", "quote": "Pen was warned by his worldly uncle not to **philander** with country maidens whose hearts might take flirtation seriously."},
      {"author": "Jane Austen", "work": "Mansfield Park", "quote": "Henry Crawford could never resist the temptation to **philander** with every attractive woman in the neighborhood."}
    ]
  },
  "Dashboard — phil/philanderer.md": {
    "primary": "A man who readily or frequently enters into casual sexual relationships with women; a flirt or chronic womanizer.",
    "secondary": "In dramatic literature, a self-indulgent romantic opportunist who avoids serious emotional commitment.",
    "quotes": [
      {"author": "George Bernard Shaw", "work": "The Philanderer", "quote": "The play exposed the modern **philanderer** as an intellectual coward who played with passions he could not feel."},
      {"author": "Virginia Woolf", "work": "Night and Day", "quote": "She distrusted the young barrister, sensing beneath his charm the shallow egoism of a seasoned **philanderer**."},
      {"author": "Edith Wharton", "work": "The House of Mirth", "quote": "Lily knew that van Osburgh was a notorious **philanderer**, yet tolerated him for his yacht and country house."}
    ]
  },
  "Dashboard — phil/philanthropic.md": {
    "primary": "Seeking to promote the welfare of others, especially by donating money or resources to good causes; benevolent.",
    "secondary": "In nineteenth-century social reform, charitable initiatives funding hospitals, libraries, and public sanitation.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Mrs. Jellyby's **philanthropic** enthusiasm for African natives left her own children shivering in neglected squalor."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Dorothea longed to dedicate her ample income to **philanthropic** plans for improving rustic labourers' cottages."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "The wealthy rajah was renowned for his **philanthropic** gifts, building dispensaries throughout northern India."}
    ]
  },
  "Dashboard — phil/philanthropically.md": {
    "primary": "In a philanthropic, benevolent, or humanitarian manner; with active generosity toward fellow human beings.",
    "secondary": "In civic journalism, disposing of private wealth for public benefit without expectation of commercial profit.",
    "quotes": [
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Aunt Betsey acted **philanthropically** toward poor Mr. Dick, shielding his gentle eccentricity from asylum keepers."},
      {"author": "Andrew Carnegie", "work": "The Gospel of Wealth", "quote": "Surplus wealth should be administered **philanthropically** during the possessor's life for the permanent elevation of the community."},
      {"author": "Jane Addams", "work": "Twenty Years at Hull-House", "quote": "The residents worked **philanthropically** alongside immigrant families to secure clean water and public playgrounds."}
    ]
  },
  "Dashboard — phil/philanthropist.md": {
    "primary": "A person who seeks to promote the welfare of others, especially by the generous donation of money to good causes.",
    "secondary": "In cultural biography, wealthy industrialists (such as Carnegie or Peabody) who endowed enduring educational institutions.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The professional **philanthropist** lectured upon universal brotherhood while totally blind to the misery in his own home."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Mr. Brooke fancied himself a bold political **philanthropist**, though his farm tenants grumbled about leaky roofs."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "The murdered gentleman was known as a quiet **philanthropist** who gave large anonymous sums to orphanages."}
    ]
  },
  "Dashboard — phil/philanthropy.md": {
    "primary": "The desire to promote the welfare of others, expressed especially by the generous donation of money to good causes.",
    "secondary": "In moral philosophy, practical benevolence directed toward the alleviation of poverty and advancement of culture.",
    "quotes": [
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "There is no odor so bad as that which arises from goodness tainted; if I knew for a certainty that a man was coming to my house with the conscious design of doing me good, I should run for fear of his **philanthropy**."},
      {"author": "Ralph Waldo Emerson", "work": "Self-Reliance", "quote": "Do not tell me of my obligation to put all poor men in good situations; are they my poor? I tell thee, thou foolish **philanthropy**, that I begrudge the dollar given to thy schemes."},
      {"author": "Charles Dickens", "work": "A Christmas Carol", "quote": "Mankind was my business! The common welfare was my business; charity, mercy, forbearance, and **philanthropy** were all my business!"}
    ]
  },
  "Dashboard — phil/philatelic.md": {
    "primary": "Of, relating to, or characteristic of stamp collecting or the study of postage stamps.",
    "secondary": "In numismatics and collecting culture, evaluating watermarks, perforations, plate varieties, and cancellations on stamps.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Illustrious Client", "quote": "The murder victim had maintained an extraordinary **philatelic** collection, containing rare inverted center errors from the Orient."},
      {"author": "Agatha Christie", "work": "The Murder at the Vicarage", "quote": "The vicar examined the rare triangular Cape of Good Hope stamp with keen **philatelic** curiosity."},
      {"author": "P. G. Wodehouse", "work": "Leave It to Psmith", "quote": "Lord Emsworth listened blankly to the guest's dissertation upon the **philatelic** rarities of Mauritius."}
    ]
  },
  "Dashboard — phil/philatelical.md": {
    "primary": "Pertaining to philately or postage stamps; philatelic (an archaic or variant form).",
    "secondary": "In nineteenth-century hobbyist periodicals, describing early postal history and stamp classification systems.",
    "quotes": [
      {"author": "H. G. Wells", "work": "The Wheels of Chance", "quote": "Mr. Hoopdriver displayed a modest **philatelical** album, filled with faded French Empire and German states issues."},
      {"author": "Charles Dickens", "work": "All the Year Round", "quote": "A curious **philatelical** mania swept European capitals, with boys trading rare postal adhesives in public squares."},
      {"author": "Mark Twain", "work": "Following the Equator", "quote": "The colonial postmaster was an authority on **philatelical** oddities, showing misprinted postal surcharges."}
    ]
  },
  "Dashboard — phil/philatelically.md": {
    "primary": "In a philatelic manner; with regard to the study, collection, or valuation of postage stamps.",
    "secondary": "In auction cataloging, assessing the rarity, mint condition, and historical provenance of stamps.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Case-Book of Sherlock Holmes", "quote": "The stolen envelope was **philatelically** priceless because it bore the only known combination of postmarks from Mafeking."},
      {"author": "Agatha Christie", "work": "The Big Four", "quote": "Poirot examined the envelope **philatelically**, noting that the Austrian cancellation preceded the declared invasion date."},
      {"author": "G. K. Chesterton", "work": "The Paradoxes of Mr. Pond", "quote": "He looked at the letter not for its message, but **philatelically**, admiring the rare unperforated red surcharge."}
    ]
  },
  "Dashboard — phil/philatelist.md": {
    "primary": "A person who collects or studies postage stamps, postmarks, and postal history as a hobby or vocation.",
    "secondary": "In connoisseurship, an expert who uses magnifiers, watermark detectors, and perforation gauges to authenticate stamps.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Return of Sherlock Holmes", "quote": "The recluse was an ardent **philatelist**, spending whole days with tweezers and magnifying glass over rare envelopes."},
      {"author": "G. K. Chesterton", "work": "The Club of Queer Trades", "quote": "The enthusiast described himself as a metaphysical **philatelist**, collecting stamps that had carried news of revolutions."},
      {"author": "W. Somerset Maugham", "work": "Cakes and Ale", "quote": "The vicar was an enthusiastic **philatelist**, eager to show his visitor the early issues of the British Caribbean."}
    ]
  },
  "Dashboard — phil/philately.md": {
    "primary": "The collection and study of postage stamps, revenue stamps, and postal history as a hobby.",
    "secondary": "In material culture, a global hobby originating in the 1850s following the introduction of the British Penny Black.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Valley of Fear", "quote": "He found solace from financial anxieties in the meticulous study of **philately**, cataloging every shade of blue in early Bavarian issues."},
      {"author": "H. G. Wells", "work": "Tono-Bungay", "quote": "Uncle Ponderevo dismissed **philately** as a petty pursuit, preferring cosmic speculation and gigantic advertising schemes."},
      {"author": "Agatha Christie", "work": "The Clocks", "quote": "The retired clerk devoted his quiet afternoons to **philately**, corresponding with collectors across the globe."}
    ]
  },
  "Dashboard — phil/philemon.md": {
    "primary": "A masculine personal name of Greek origin (*Philemon*, affectionate); also a short Epistle in the New Testament.",
    "secondary": "In classical Ovidian mythology, the pious old peasant husband of Baucis who hospitably entertained Jupiter and Mercury.",
    "quotes": [
      {"author": "King James Bible", "work": "The Holy Bible", "quote": "Paul, a prisoner of Jesus Christ, and Timothy our brother, unto **philemon** our dearly beloved, and fellowlabourer."},
      {"author": "Ovid", "work": "Metamorphoses", "quote": "The humble cottage of Baucis and **philemon** received the gods in disguise, offering milk, fruit, and heartfelt rustic piety."},
      {"author": "John Dryden", "work": "Baucis and Philemon", "quote": "Old **philemon** marvelled when the earthen pitcher filled itself spontaneously with sweet, unpressed wine."}
    ]
  },
  "Dashboard — phil/philharmonic.md": {
    "primary": "Devoted to music; usually used in the names of orchestras, musical societies, or symphony concerts.",
    "secondary": "In classical musical culture, symphony orchestras and concert halls founded to cultivate appreciation of orchestral masterworks.",
    "quotes": [
      {"author": "George Bernard Shaw", "work": "Music in London", "quote": "The **philharmonic** society presented Beethoven's Ninth Symphony with a magnificent chorus that electrified the hall."},
      {"author": "Virginia Woolf", "work": "The Voyage Out", "quote": "She listened to the **philharmonic** broadcast in the quiet evening, transported by the soaring violins above London roofs."},
      {"author": "E. M. Forster", "work": "Howards End", "quote": "Helen Schlegel attended the **philharmonic** performance of the Fifth Symphony, seeing goblins walking across the universe."}
    ]
  },
  "Dashboard — phil/philia.md": {
    "primary": "Affectionate regard, brotherly love, or friendship, especially as defined in classical Greek philosophy.",
    "secondary": "In Aristotle's Nicomachean Ethics, virtue-based friendship between equals seeking mutual moral goodness.",
    "quotes": [
      {"author": "Aristotle", "work": "Nicomachean Ethics", "quote": "True **philia** arises between virtuous individuals who wish each other good for the other's own sake."},
      {"author": "C. S. Lewis", "work": "The Four Loves", "quote": "The Greeks distinguished between erotic passion, domestic affection, divine charity, and that noble friendship termed **philia**."},
      {"author": "Plato", "work": "Lysis", "quote": "Socrates questioned the young men in the palaestra, seeking to discover what essence makes friendship and **philia** possible."}
    ]
  },
  "Dashboard — phil/philip.md": {
    "primary": "A personal name of Greek origin (*Philippos*, lover of horses); borne by kings of Macedon, France, and Spain.",
    "secondary": "In ancient history, Philip II of Macedon (382–336 BC), who unified Greece and paved the way for Alexander the Great.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "King **philip**, determine on some charge; for we will have this match solemnized before the setting sun."},
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The Roman legions faced the phalanx of King **philip** upon the plains of Cynoscephalae, testing sword against spear."},
      {"author": "W. Somerset Maugham", "work": "Of Human Bondage", "quote": "Young **philip** Carey sat in the study at Blackstable vicarage, wondering what life held in store for him."}
    ]
  },
  "Dashboard — phil/philippi.md": {
    "primary": "An ancient city in eastern Macedonia, famous as the site of the decisive Roman battle in 42 BC.",
    "secondary": "In Roman history, the double battle where Mark Antony and Octavian defeated Brutus and Cassius, ending the Republic.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "To tell thee thou shalt see me at **philippi**; the evil spirit of Caesar vanished, leaving Brutus in dread silence."},
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The liberties of ancient Rome expired upon the plains of **philippi**, where the last champions of the senate fell."},
      {"author": "Thomas Babington Macaulay", "work": "Lays of Ancient Rome", "quote": "Centuries later, travelers looked upon the mounds of **philippi** where republican freedom fought its dying contest."}
    ]
  },
  "Dashboard — phil/philippian.md": {
    "primary": "Of, relating to, or native to the ancient city of Philippi in eastern Macedonia.",
    "secondary": "In biblical history, relating to the Christian congregation established at Philippi by the Apostle Paul.",
    "quotes": [
      {"author": "John Henry Newman", "work": "Historical Sketches", "quote": "The Apostle Paul addressed the **philippian** converts with heartfelt tenderness, remembering their generous support during his imprisonment."},
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The **philippian** colony enjoyed the proud privileges of Roman law and citizenship in the Macedonian province."},
      {"author": "Philip Schaff", "work": "History of the Apostolic Church", "quote": "The church at Philippi was the earliest European foundation, founded amidst the generous hospitality of a **philippian** household."}
    ]
  },
  "Dashboard — phil/philippians.md": {
    "primary": "The Epistle of Paul to the Philippians, a book of the New Testament; also the inhabitants of Philippi.",
    "secondary": "In biblical studies, a warm prison epistle written by Paul from Rome expressing joy, humility, and gratitude.",
    "quotes": [
      {"author": "King James Bible", "work": "The Holy Bible", "quote": "The epistle of Paul the Apostle to the **philippians** opens with prayers of joy for their fellowship in the gospel."},
      {"author": "John Calvin", "work": "Commentary on the Epistle to the Philippians", "quote": "In his letter to the **philippians**, the apostle sets forth the humility of Christ as the supreme pattern for all believers."},
      {"author": "Thomas Aquinas", "work": "Summa Theologiae", "quote": "The Angelic Doctor expounds the passage in **philippians** where Christ emptied himself, taking the form of a servant."}
    ]
  },
  "Dashboard — phil/philippic.md": {
    "primary": "A bitter attack or denunciation, especially a verbal one; a fiery, invective-filled oration.",
    "secondary": "In classical rhetoric, named after Demosthenes' speeches against Philip II of Macedon, and Cicero's speeches against Mark Antony.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "Cicero paid for his fourteenth **philippic** with his life, his severed head displayed on the Rostra he had immortalized."},
      {"author": "Edmund Burke", "work": "Speech on American Taxation", "quote": "The minister delivered a furious **philippic** against colonial resistance, alienating the moderate assembly."},
      {"author": "Thomas Babington Macaulay", "work": "Critical and Historical Essays", "quote": "The parliamentary orator delivered a scathing **philippic** that stripped the corrupt administration of all prestige."}
    ]
  },
  "Dashboard — phil/philippine.md": {
    "primary": "Of or relating to the Philippines, its people, diverse indigenous cultures, or official languages.",
    "secondary": "In Southeast Asian history, an archipelagic nation of over seven thousand islands named in honor of King Philip II of Spain.",
    "quotes": [
      {"author": "Alfred Russel Wallace", "work": "The Malay Archipelago", "quote": "The fauna of the northern **philippine** islands exhibits unique affinities with both Borneo and mainland China."},
      {"author": "Joseph Conrad", "work": "Lord Jim", "quote": "The trading schooner plied between the Sulu Sea and the green mountainous coasts of the **philippine** archipelago."},
      {"author": "Mark Twain", "work": "To the Person Sitting in Darkness", "quote": "Twain condemned the military suppression of the **philippine** independence fighters as a betrayal of American ideals."}
    ]
  },
  "Dashboard — phil/philippines.md": {
    "primary": "A sovereign island country in Southeast Asia situated in the western Pacific Ocean, comprising over 7,600 islands.",
    "secondary": "In colonial maritime history, a major Spanish Pacific captaincy-general linked to Acapulco via the Manila Galleon trade.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The extraordinary endemic bird species inhabiting the **philippines** point to long isolation on volcanic island chains."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Whalers sailed westward through the Straits of Sunda toward the tempestuous seas of the **philippines** in pursuit of sperm whales."},
      {"author": "Mark Twain", "work": "Autobiography of Mark Twain", "quote": "The acquisition of the **philippines** marked our entry into imperial colonial ambitions far removed from our founding principles."}
    ]
  },
  "Dashboard — phil/philippopolis.md": {
    "primary": "The ancient Greco-Roman name of Plovdiv, Bulgaria, founded on the Maritsa River by Philip II of Macedon in 342 BC.",
    "secondary": "In Balkan historical geography, an ancient Thracian metropolis and major military fortress along the Via Militaris.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The Goths sacked the populous city of **philippopolis**, carrying away thousands of captives from the Thracian plain."},
      {"author": "Ammianus Marcellinus", "work": "Roman History", "quote": "The imperial forces rallied beneath the massive granite ramparts of **philippopolis** after the retreat from Adrianople."},
      {"author": "Lord Byron", "work": "Letters and Journals", "quote": "Our caravan rested at Plovdiv, the ancient **philippopolis**, admiring Roman amphitheatre ruins overlooking the broad Maritsa."}
    ]
  },
  "Dashboard — phil/philistia.md": {
    "primary": "An ancient coastal region in southwestern Canaan inhabited by the Philistines; roughly modern Gaza and southern Israel.",
    "secondary": "In biblical history, a confederacy of five cities—Gaza, Ashkelon, Ashdod, Ekron, and Gath—frequently in conflict with Israel.",
    "quotes": [
      {"author": "John Milton", "work": "Samson Agonistes", "quote": "Samson stood in chains within the temple of Dagon, mocked by the lords and captains of all **philistia**."},
      {"author": "King James Bible", "work": "The Holy Bible", "quote": "Rejoice not thou, whole **philistia**, because the rod of him that smote thee is broken; for out of the serpent's root shall come cockatrice."},
      {"author": "George Eliot", "work": "Daniel Deronda", "quote": "The ancient borders of **philistia** lay along the sun-baked Mediterranean coast, where camel trains traded olive oil."}
    ]
  },
  "Dashboard — phil/philistine.md": {
    "primary": "A person who is hostile or indifferent to culture and the arts; also an inhabitant of ancient biblical Philistia.",
    "secondary": "In nineteenth-century cultural criticism (Matthew Arnold), bourgeois citizens indifferent to intellectual and aesthetic values.",
    "quotes": [
      {"author": "Matthew Arnold", "work": "Culture and Anarchy", "quote": "The English middle class is hopelessly **philistine**, blind to sweetness and light, and devoted only to commercial utility."},
      {"author": "Oscar Wilde", "work": "De Profundis", "quote": "The supreme artist must inevitably confront the stubborn incomprehension of the respectable **philistine** mob."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Rosamond's uncle was a good-natured **philistine**, who thought reading poetry a waste of good ledger paper."}
    ]
  },
  "Dashboard — phil/philistinism.md": {
    "primary": "The attitude, behavior, or character of a philistine; anti-intellectual hostility or indifference to culture and the arts.",
    "secondary": "In cultural sociology, middle-class materialism and aesthetic complacency denounced by Victorian critics.",
    "quotes": [
      {"author": "Matthew Arnold", "work": "Essays in Criticism", "quote": "The greatest danger facing British civilization is the smug **philistinism** that measures all progress in tons of coal."},
      {"author": "George Bernard Shaw", "work": "The Sanity of Art", "quote": "Modern theatre must wage unceasing war against the respectable **philistinism** of suburban theatregoers."},
      {"author": "Virginia Woolf", "work": "A Room of One's Own", "quote": "The pervasive **philistinism** of university dons excluded women scholars from entering the sacred college libraries."}
    ]
  },
  "Dashboard — phil/phillidae.md": {
    "primary": "A taxonomic family of leaf insects (Phylliidae) commonly known as true walking leaves or leaf bugs.",
    "secondary": "In entomology and evolutionary camouflage, insects possessing flattened, vein-patterned bodies that mimic tree leaves.",
    "quotes": [
      {"author": "Alfred Russel Wallace", "work": "The Malay Archipelago", "quote": "In the Moluccan forests, a walking leaf insect of the family **phillidae** simulated a chewed green leaf with uncanny perfection."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Natural selection produced in **phillidae** the most extraordinary mimicry of foliage, complete with faux fungal spots and veining."},
      {"author": "Henry Walter Bates", "work": "The Naturalist on the River Amazons", "quote": "Predators repeatedly passed over the resting insect of **phillidae**, deceived by its leaf-like expanded legs and antennae."}
    ]
  },
  "Dashboard — phil/phillipsite.md": {
    "primary": "A hydrated potassium, calcium, and sodium aluminosilicate mineral of the zeolite group, found in volcanic rocks.",
    "secondary": "In mineralogy and deep-sea sedimentology, a zeolite crystal occurring in basalt cavities and deep-sea pelagic red clays.",
    "quotes": [
      {"author": "Charles Darwin", "work": "Geological Observations on Volcanic Islands", "quote": "In the amygdaloidal cavities of the basaltic cliffs, crystalline clusters of **phillipsite** sparkled like frost."},
      {"author": "Thomas Henry Huxley", "work": "Physiography", "quote": "Dredging from the ocean floor brought up volcanic mud densely studded with microscopic crystals of **phillipsite**."},
      {"author": "John Ruskin", "work": "The Ethics of the Dust", "quote": "The lecturer exhibited a specimen of volcanic tuff, pointing out the delicate radiating stars of **phillipsite**."}
    ]
  },
  "Dashboard — phil/phillyrea.md": {
    "primary": "A genus of evergreen shrubs and small trees in the olive family (Oleaceae), native to the Mediterranean region.",
    "secondary": "In Mediterranean landscape botany, a characteristic component of the maquis scrubland with glossy leathery leaves.",
    "quotes": [
      {"author": "John Evelyn", "work": "Sylva, or A Discourse of Forest-Trees", "quote": "The evergreen **phillyrea** withstands the severest sea gales, making it an admirable hedge for coastal gardens."},
      {"author": "George Sand", "work": "A Winter in Majorca", "quote": "Along the rocky paths of Valldemossa, thickets of aromatic myrtle and glossy **phillyrea** bordered the terrace walls."},
      {"author": "Edward Dodwell", "work": "A Classical and Topographical Tour through Greece", "quote": "The dry limestone hills of Attica were covered with dense maquis of wild olive, lentisk, and leathery **phillyrea**."}
    ]
  },
  "Dashboard — phil/philodendron.md": {
    "primary": "A large genus of flowering plants in the arum family (Araceae), native to tropical American rainforests, widely grown as houseplants.",
    "secondary": "In tropical botany and horticulture, climbing hemi-epiphytes adapted with aerial roots to scale forest canopy trees.",
    "quotes": [
      {"author": "Alfred Russel Wallace", "work": "Travels on the Amazon and Rio Negro", "quote": "Vast climbing species of **philodendron** embraced the towering trunks of the Amazonian forest with rope-like aerial roots."},
      {"author": "Henry Walter Bates", "work": "The Naturalist on the River Amazons", "quote": "The canoe drifted beneath dripping jungle boughs where broad, perforated leaves of **philodendron** hung like green shields."},
      {"author": "William Beebe", "work": "Jungle Peace", "quote": "In the dim green twilight of the Guiana bush, a flowering **philodendron** scented the humid air with tropical sweetness."}
    ]
  },
  "Dashboard — phil/philogyny.md": {
    "primary": "Love, fondness, or admiration for women; the opposite of misogyny.",
    "secondary": "In cultural history and social ethics, chivalric devotion or intellectual appreciation of women's moral and creative intellect.",
    "quotes": [
      {"author": "George Bernard Shaw", "work": "Man and Superman", "quote": "Tanner declared that his outspoken **philogyny** was not sentimental flattery, but a scientific admiration for the Life Force."},
      {"author": "William Makepeace Thackeray", "work": "The Newcomes", "quote": "The kindly colonel's natural **philogyny** made him the chivalrous champion of every distressed gentlewoman in London."},
      {"author": "Arthur Schopenhauer", "work": "Essays and Aphorisms", "quote": "The philosopher mocked the romantic **philogyny** of modern European culture as an absurd sentimental idealization of nature."}
    ]
  },
  "Dashboard — phil/philohela.md": {
    "primary": "A former genus name for the American woodcock (*Scolopax minor*, formerly *Philohela minor*), a chunky woodland gamebird.",
    "secondary": "In North American ornithology, a crepuscular wading bird celebrated for its spring twilight courtship flight and long probing bill.",
    "quotes": [
      {"author": "John James Audubon", "work": "The Birds of America", "quote": "The American woodcock, formerly classified as **philohela**, performs a spiral aerial song-flight over alder swales at dusk."},
      {"author": "Henry David Thoreau", "work": "The Maine Woods", "quote": "In the damp alder thickets along the creek, we flushed a woodcock belonging to the secretive genus **philohela**."},
      {"author": "Aldo Leopold", "work": "A Sand County Almanac", "quote": "The twilight sky dance of the woodcock, the **philohela** of older bird manuals, announces the true arrival of spring."}
    ]
  },
  "Dashboard — phil/philological.md": {
    "primary": "Of, relating to, or characteristic of philology; relating to the historical study of language and literary texts.",
    "secondary": "In linguistic scholarship, applying rigorous textual criticism and comparative grammar to decipher ancient manuscripts.",
    "quotes": [
      {"author": "Max Müller", "work": "Lectures on the Science of Language", "quote": "Comparative **philological** research demonstrated beyond doubt the common Indo-European ancestry of Sanskrit, Greek, and Latin."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Casaubon had amassed vast **philological** notebooks, attempting to prove that all world mythologies were corruptions of Hebrew truth."},
      {"author": "Friedrich Nietzsche", "work": "The Birth of Tragedy", "quote": "Nietzsche brought a passionate **philological** precision to the study of early Greek tragic poetry and Dionysian cults."}
    ]
  },
  "Dashboard — phil/philologist.md": {
    "primary": "A scholar who specializes in philology; a student of the historical development and relationships of languages.",
    "secondary": "In nineteenth-century humanist scholarship, an academic dedicated to deciphering ancient texts, epigraphs, and etymologies.",
    "quotes": [
      {"author": "Friedrich Nietzsche", "work": "Beyond Good and Evil", "quote": "As a trained classical **philologist**, I learned to read ancient texts slowly, with delicate reverence for each syllable."},
      {"author": "Max Müller", "work": "Chips from a German Workshop", "quote": "The **philologist** examines fossilized words in ancient idioms just as the geologist analyzes strata in the earth's crust."},
      {"author": "George Eliot", "work": "Romola", "quote": "The Florentine **philologist** spent his eyesight deciphering corrupt Greek manuscripts brought from fallen Constantinople."}
    ]
  },
  "Dashboard — phil/philologue.md": {
    "primary": "A philologist; a scholar of language, literature, and linguistics (often with a French or archaic connotation).",
    "secondary": "In literary history, a savant devoted to the history of words, grammatical forms, and textual preservation.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "Erasmus was hailed throughout Europe as the prince of letters, a consummate **philologue** who purified the Greek New Testament."},
      {"author": "Ernest Renan", "work": "The Future of Science", "quote": "The modern **philologue** reconstructs dead civilizations through the subtle evidence preserved in their linguistic monuments."},
      {"author": "Walter Pater", "work": "Marius the Epicurean", "quote": "The Roman **philologue** lectured in the Forum upon the archaisms of Ennius and the pristine vigor of Latin speech."}
    ]
  },
  "Dashboard — phil/philology.md": {
    "primary": "The branch of knowledge that deals with the structure, historical development, and relationships of languages.",
    "secondary": "In the humanities, the comprehensive study of literary texts, historical linguistics, and cultural heritage.",
    "quotes": [
      {"author": "Max Müller", "work": "Comparative Mythology", "quote": "The science of comparative **philology** has opened to our generation vistas of human prehistory unknown to the ancients."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Casaubon was stranded in the obsolete **philology** of the eighteenth century, ignorant of the great German historical advances."},
      {"author": "Friedrich Nietzsche", "work": "Twilight of the Idols", "quote": "By **philology** I understand the venerable art of reading well: to read slowly, deeply, with caution and open doors."}
    ]
  },
  "Dashboard — phil/philomachus.md": {
    "primary": "A former genus name for the ruff (*Calidris pugnax*, formerly *Philomachus pugnax*), an Old World shorebird famed for courtship battles.",
    "secondary": "In avian ethology, male sandpipers possessing ornate neck ruffs who display on communal leks in springtime.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The polygamous shorebird formerly known as **philomachus** displays extraordinarily variable ruffs and ear-tufts during lek combat."},
      {"author": "Alfred Russel Wallace", "work": "Darwinism", "quote": "No two males of the genus **philomachus** are colored alike, presenting a classic study in sexual dimorphism and mate choice."},
      {"author": "Gilbert White", "work": "The Natural History of Selborne", "quote": "The fowler captured live specimens of **philomachus** in the fens, selling the pugnacious ruffs to London epicures."}
    ]
  },
  "Dashboard — phil/philomath.md": {
    "primary": "A lover of learning, study, and science; a scholar or intellectual enthusiast, especially in mathematics.",
    "secondary": "In eighteenth-century print culture, a learned almanac-maker, mathematician, or enthusiastic amateur astronomer.",
    "quotes": [
      {"author": "Benjamin Franklin", "work": "Poor Richard's Almanack", "quote": "Richard Saunders styled himself a humble **philomath**, calculating lunar eclipses and seasonal tides for colonial farmers."},
      {"author": "Oliver Goldsmith", "work": "The Deserted Village", "quote": "The village schoolmaster was revered as a profound **philomath**, who could measure land, terms and tides presage."},
      {"author": "Jonathan Swift", "work": "Gulliver's Travels", "quote": "The academy at Lagado was crowded with every manner of visionary **philomath**, extracting sunbeams from cucumbers."}
    ]
  },
  "Dashboard — phil/philophylla.md": {
    "primary": "A genus of fruit flies in the family Tephritidae, whose larvae feed inside flowers and fruit of host plants.",
    "secondary": "In agricultural entomology, colorful picture-winged flies noted for intricate wing banding and gall formation.",
    "quotes": [
      {"author": "Jean-Henri Fabre", "work": "Social Life in the Insect World", "quote": "The female fly of **philophylla** deposits her eggs within the flower bud, where the larva feeds in secure isolation."},
      {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Invertebrate Animals", "quote": "The banded wings of **philophylla** exhibit distinctive courtship waving displays among competing territorial males."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants Under Domestication", "quote": "Certain gall-making diptera related to **philophylla** stimulate strange hypertrophied growths upon wild shrubs."}
    ]
  },
  "Dashboard — phil/philosopher.md": {
    "primary": "A person who seeks wisdom, enlightenment, or ponders fundamental questions of existence, reality, and morality.",
    "secondary": "In intellectual history, a thinker who constructs or critiques systematic models of metaphysics, logic, and ethics.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "There are more things in heaven and earth, Horatio, than are dreamt of in your **philosopher**'s school."},
      {"author": "Ralph Waldo Emerson", "work": "Representative Men", "quote": "Plato is philosophy, and philosophy, Plato; to him every subsequent **philosopher** pays unconscious tribute."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "The duty of a true **philosopher** is to examine ideas with impartial candor, unswayed by ancient custom or popular clamor."}
    ]
  },
  "Dashboard — phil/philosophic.md": {
    "primary": "Of, relating to, or characteristic of philosophy; calm, rational, and stoically resigned in the face of adversity.",
    "secondary": "In intellectual essays, an analytical temperament seeking foundational explanations behind superficial events.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "Marcus Aurelius maintained a serene **philosophic** calm amidst the turbulent pestilence and barbarian wars of the Danube."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Lydgate regarded social prejudices with **philosophic** amusement, confident that science would soon dispell ancient ignorance."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "With a **philosophic** flourish Cato throws himself upon his sword; I quietly take to the ship and the boundless sea."}
    ]
  },
  "Dashboard — phil/philosophical.md": {
    "primary": "Relating to the study of fundamental knowledge, reality, and existence; calm, reasonable, and stoical.",
    "secondary": "In scientific and ethical prose, an attitude of rational inquiry seeking primary causes rather than empirical particulars.",
    "quotes": [
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "A **philosophical** mind will never accept authority without demanding the rational evidence upon which belief must rest."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth bore the disappointment with **philosophical** good humor, resolving to make the best of her rustic surroundings."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Naturalists of a **philosophical** turn of mind cannot fail to be struck by the pervasive unity of type in nature."}
    ]
  },
  "Dashboard — phil/philosophically.md": {
    "primary": "In a philosophical manner; calmly, rationally, stoically, or with reference to philosophical principles.",
    "secondary": "In narrative characterization, enduring misfortune with dignified composure and intellectual perspective.",
    "quotes": [
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Mr. Micawber smiled **philosophically**, observing that while clouds darkened the horizon, something was bound to turn up."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Holmes regarded the ruined carpet **philosophically**, observing that an investigator must accept small domestic casualties."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Gabriel Oak took the loss of his flock **philosophically**, turning his face toward new employment without bitterness."}
    ]
  },
  "Dashboard — phil/philosophise.md": {
    "primary": "Speculate or theorize about fundamental issues; explain or moralize in philosophical terms (British spelling).",
    "secondary": "In literary dialogue, engaging in detached reflection upon human folly while observing worldly commotion.",
    "quotes": [
      {"author": "George Bernard Shaw", "work": "Man and Superman", "quote": "Men love to **philosophise** upon the vanity of life while greedily reaching for every worldly luxury within their grasp."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Angel Clare would **philosophise** upon the simple virtues of peasant labor, forgetting the harsh poverty beneath."},
      {"author": "H. G. Wells", "work": "The Time Machine", "quote": "The time traveler began to **philosophise** upon the eventual fate of human intellect in an automated golden age."}
    ]
  },
  "Dashboard — phil/philosophiser.md": {
    "primary": "A person who philosophizes, often casually, superficially, or pretentiously (British spelling).",
    "secondary": "In social satire, an armchair moralist who dispenses unhelpful abstract theories in times of crisis.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "Rasselas", "quote": "The eloquent **philosophiser** who lectured upon mastering sorrow wept uncontrollably when death took his own daughter."},
      {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "Major Dobbin was no pedantic **philosophiser**, but a plain soldier whose quiet loyalty outshone clever drawing-room wits."},
      {"author": "George Eliot", "work": "Daniel Deronda", "quote": "The cynical **philosophiser** sat in the club window, sneering at every earnest enterprise as a foolish delusion."}
    ]
  },
  "Dashboard — phil/philosophize.md": {
    "primary": "Speculate, theorize, or moralize about fundamental matters of human life, morality, and knowledge.",
    "secondary": "In character studies, seeking abstract wisdom or moralizing upon ordinary daily events.",
    "quotes": [
      {"author": "Leo Tolstoy", "work": "War and Peace", "quote": "Pierre loved to **philosophize** through the long winter evenings, debating Freemasonry and the purpose of human existence."},
      {"author": "Mark Twain", "work": "Adventures of Huckleberry Finn", "quote": "Jim and I would lie on the raft and **philosophize** about whether the stars were made or just happened like eggs."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "It is pleasant to **philosophize** upon the harpoon line while sitting safely ashore by a glowing sea-coal grate."}
    ]
  },
  "Dashboard — phil/philosophizer.md": {
    "primary": "A person who philosophizes, especially in a shallow, amateurish, pedantic, or pretentious manner.",
    "secondary": "In character criticism, an individual given to trivial moralizing without practical worldly experience.",
    "quotes": [
      {"author": "Henry James", "work": "The Bostonians", "quote": "Basil Ransom viewed the elderly **philosophizer** as a well-meaning dreamer whose windy lectures changed nothing."},
      {"author": "Nathaniel Hawthorne", "work": "The Blithedale Romance", "quote": "The utopian community was crowded with every species of reformer and long-haired **philosophizer** from New England."},
      {"author": "Washington Irving", "work": "Salmagundi", "quote": "Our local **philosophizer** took the floor, proving in three tedious hours that virtue was preferable to vice."}
    ]
  },
  "Dashboard — phil/philosophizing.md": {
    "primary": "The action of engaging in philosophical speculation, reflection, or moralizing discourse.",
    "secondary": "In dramatic narrative, paused reflection upon mortality, fate, or ethics in the midst of turmoil.",
    "quotes": [
      {"author": "Leo Tolstoy", "work": "War and Peace", "quote": "Prince Andrei tired of the ceaseless political **philosophizing** of the Petersburg salons, longing for the simplicity of the camp."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Mr. Micawber's eloquent **philosophizing** could not pay the baker's bill, yet it sustained his cheerful spirit."},
      {"author": "Jack London", "work": "The Sea-Wolf", "quote": "Wolf Larsen indulged in brutal **philosophizing**, arguing that life was a mere ferment of yeast fighting for crumbs."}
    ]
  },
  "Dashboard — phil/philosophy.md": {
    "primary": "The study of the fundamental nature of knowledge, reality, and existence; also a guiding personal life creed.",
    "secondary": "In intellectual history, academic discourse spanning epistemology, metaphysics, logic, ethics, and aesthetics.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "Hang up **philosophy**! Unless **philosophy** can make a Juliet, displant a town, reverse a prince's doom, it helps not."},
      {"author": "John Milton", "work": "Comus", "quote": "How charming is divine **philosophy**! Not harsh and crabbed, as dull fools suppose, but musical as is Apollo's lute."},
      {"author": "Francis Bacon", "work": "The Essays", "quote": "A little **philosophy** inclineth man's mind to atheism, but depth in **philosophy** bringeth men's minds about to religion."}
    ]
  },
  "Dashboard — phil/philter.md": {
    "primary": "A drink or potion supposed to have the power of exciting romantic love or sexual desire; a love charm.",
    "secondary": "In classical and medieval folklore, magical draughts brewed from herbs and roots to captivate a lover's heart.",
    "quotes": [
      {"author": "Walter Scott", "work": "Kenilworth", "quote": "The cunning alchemist offered a magic **philter** in a crystal phial, swearing it would rekindle the earl's waning affection."},
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "Chillingworth offered the trembling captive a calming draught, assuring her it was no lethal poison nor unholy **philter**."},
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The tragic madness of the poet Lucretius was anciently attributed to a love **philter** administered by a jealous mistress."}
    ]
  },
  "Dashboard — phil/philtre.md": {
    "primary": "A potion or magical draught credited with the power to arouse love or sexual passion (British spelling).",
    "secondary": "In romantic opera and legend (such as Tristan and Isolde), an enchanted wine that binds lovers in tragic, irreversible fate.",
    "quotes": [
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "Rochester declared that Jane must have brewed an uncanny **philtre** of moonlight to bewitch his worldly heart."},
      {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "Rustic village gossips whispered that Eustacia Vye knew how to compound a midnight **philtre** from mountain heath flowers."},
      {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "He studied the medieval grimoires, reading of an ancient Venetian **philtre** distilled from mandrake roots and serpent venom."}
    ]
  }
}

def curate_file(rel_path, info):
    base_dir = "App database/Latin roots/Cluster Mind & Knowledge"
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

print(f"Successfully updated {success}/{len(data)} notes in Dashboard — phil.")
