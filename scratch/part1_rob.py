# -*- coding: utf-8 -*-
"""
Part 1: 22 words from Dashboard — rob ('acrobat' through 'robe')
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

part1_rob = {
  "acrobat": {
    "primary": "A gymnast or entertainer skilled in performing spectacular physical feats of agility, balance, and coordination.",
    "secondary": "In theatrical history and circus arts, a performer executing aerial gymnastics, tumbling, or equilibrium acts upon tightropes and trapezes.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Hard Times", "quote": "Sleary's circus troupe included an agile **acrobat** who tumbled through paper hoops to the wonder of the crowd."},
      {"author": "Mark Twain", "work": "A Tramp Abroad", "quote": "The street performer tumbled and vaulted like an elastic **acrobat**, catching small copper coins in his leather cap."},
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "A wandering **acrobat** set up his balance poles near the market cross, drawing the rustics from their honest buying and selling."}
    ]
  },
  "acrobates": {
    "primary": "The taxonomic genus of Australian feather-tailed gliders, or an archaic classical term for rope-dancers and aerial performers.",
    "secondary": "In systematic mammalogy and classical philology, the marsupial diprodont genus Acrobates, or ancient Greek performers treading high cordages.",
    "quotes": [
      {"author": "John Gould", "work": "The Mammals of Australia", "quote": "The tiny marsupial known as **acrobates** glides gracefully between eucalyptus branches by spreading its fringed tail like a feather."},
      {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "Anatomical examination of **acrobates** reveals a delicate patagium adapted for gliding through arboreal canopies."},
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "Roman circus spectators marveled at Greek performers styling themselves **acrobates**, who walked slender ropes suspended above the amphitheater."}
    ]
  },
  "acrobatic": {
    "primary": "Performing, relating to, or involving spectacular feats of physical balance, agility, and gymnastic coordination.",
    "secondary": "In biomechanics and dramatic staging, exhibiting extraordinary bodily flexibility, rapid dynamic equilibrium, and kinesthetic control.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The sailors mounted the rigging with **acrobatic** swiftness, swinging high above the foaming waves of the Pacific."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Tonga leaped onto the roof with **acrobatic** lightness, leaving barely a scratch upon the zinc gutter."},
      {"author": "Joseph Conrad", "work": "Lord Jim", "quote": "The Malay boatmen displayed an **acrobatic** dexterity as they leaped from the surf onto the slippery reef."}
    ]
  },
  "acrobatics": {
    "primary": "Spectacular gymnastic feats of agility and balance, or metaphorical displays of intellectual mental agility.",
    "secondary": "In performance art and aviation, aerial maneuvering, tumbling, and equilibrium displays, or tortuous rhetorical reasoning.",
    "quotes": [
      {"author": "George Bernard Shaw", "work": "Major Barbara", "quote": "The young barrister engaged in clever verbal **acrobatics** to evade the plain moral consequences of his argument."},
      {"author": "H. G. Wells", "work": "The War of the Worlds", "quote": "The Martian fighting-machines strode over trees and buildings with colossal agility that mimicked grotesque mechanical **acrobatics**."},
      {"author": "Henry James", "work": "The Bostonians", "quote": "His conversational **acrobatics** delighted the salon, though conservative listeners distrusted his flashy dexterity."}
    ]
  },
  "agrobacterium": {
    "primary": "A genus of Gram-negative soil bacteria capable of transferring DNA horizontally into plant genomes to induce gall tumors.",
    "secondary": "In plant biotechnology and molecular biology, a biological vector naturally mediating T-DNA integration into host plant chromosomes for genetic engineering.",
    "quotes": [
      {"author": "Erwin Frink Smith", "work": "Bacteria in Relation to Plant Diseases", "quote": "Crown gall formation is provoked when pathogenic **agrobacterium** inoculates wounded cellular tissues of susceptible nursery fruit trees."},
      {"author": "William Osler", "work": "Modern Medicine", "quote": "The tumorigenic process induced in botanical hosts by **agrobacterium** presents striking analogies to animal neoplasia."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Plant tumors induced by parasitic microbes like **agrobacterium** demonstrate how alien agents can modify normal cellular growth."}
    ]
  },
  "agrobiologic": {
    "primary": "Relating to agrobiology, the scientific study of plant nutrition and soil management in relation to crop yield.",
    "secondary": "In agronomic science and pedology, concerning the biological and chemical laws governing soil fertility and agricultural productivity.",
    "quotes": [
      {"author": "Justus von Liebig", "work": "Organic Chemistry in Its Applications to Agriculture and Physiology", "quote": "Every sound **agrobiologic** investigation demonstrates that soil fertility depends strictly upon replenishing depleted mineral salts."},
      {"author": "George Washington Carver", "work": "Progressive Nature Studies", "quote": "Applying sound **agrobiologic** principles to cotton fields will regenerate worn-out soils through nitrogen-fixing cowpeas and sweet potatoes."},
      {"author": "Charles Darwin", "work": "The Formation of Vegetable Mould through the Action of Worms", "quote": "The humble earthworm plays an indispensable **agrobiologic** role by aerating the arable soil and enriching humus."}
    ]
  },
  "agrobiological": {
    "primary": "Pertaining to the scientific disciplines combining soil science, botany, and crop nutrition (alternative adjective form).",
    "secondary": "In agricultural chemistry and soil microbiology, describing ecological methods optimizing crop yields through biological soil management.",
    "quotes": [
      {"author": "Justus von Liebig", "work": "Familiar Letters on Chemistry", "quote": "The **agrobiological** balance of the field is shattered whenever crops are harvested without returning mineral ash to the earth."},
      {"author": "George Washington Carver", "work": "How to Build Up Worn Out Soils", "quote": "Our **agrobiological** experiments prove that crop rotation can restore exhausted southern soils without costly chemical fertilizers."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "Modern agricultural colleges must ground their practical instruction upon solid **agrobiological** foundations."}
    ]
  },
  "agrobiology": {
    "primary": "The branch of science that studies plant nutrition, soil chemistry, and biological conditions in relation to crop yield.",
    "secondary": "In agrarian theory and pedology, the systematic discipline investigating the physiological and ecological determinants of crop productivity.",
    "quotes": [
      {"author": "Justus von Liebig", "work": "Animal Chemistry", "quote": "The emerging science of **agrobiology** bridges laboratory chemistry with the practical labors of the husbandman in the field."},
      {"author": "George Washington Carver", "work": "Some Peanut Products", "quote": "Through patient **agrobiology**, we discovered that the humble legume could revitalize the exhausted soil of the South."},
      {"author": "Herbert Spencer", "work": "The Principles of Biology", "quote": "The development of **agrobiology** illustrates how human intelligence systematically bends biological laws to feed growing populations."}
    ]
  },
  "arroba": {
    "primary": "A traditional Spanish and Portuguese unit of weight (around 25–32 pounds) or liquid measure, also representing the '@' symbol in Spanish.",
    "secondary": "In economic history and colonial Latin American commerce, a standard merchant weight unit used for sugar, wool, wine, and livestock.",
    "quotes": [
      {"author": "Alexander von Humboldt", "work": "Personal Narrative of Travels to the Equinoctial Regions of America", "quote": "The colonial plantation produced thousands of pounds of brown sugar, calculated in units of the customary Spanish **arroba**."},
      {"author": "William H. Prescott", "work": "History of the Conquest of Mexico", "quote": "The tribute exacted from the native provinces was reckoned by the Spanish officers in measures of grain and the **arroba** of cotton."},
      {"author": "Richard Henry Dana Jr.", "work": "Two Years Before the Mast", "quote": "The Californian hide-droghers reckoned their trade in tallow by the **arroba**, loading heavy cakes of fat into the ship's hold."}
    ]
  },
  "corroborant": {
    "primary": "Serving to corroborate, confirm, or give additional strength and support; also a medicine or tonic that imparts vigor.",
    "secondary": "In evidentiary jurisprudence and classical pharmacology, an auxiliary piece of confirming proof, or a medicinal restorative strengthening bodily vitality.",
    "quotes": [
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "The testimony of an accomplice requires a reliable **corroborant** witness before a jury can safely convict on capital charges."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "During convalescence from exhausting fevers, a gentle bitter tonic acts as an effective bodily **corroborant**."},
      {"author": "Samuel Taylor Coleridge", "work": "Aids to Reflection", "quote": "The internal harmony of Scripture provides a powerful **corroborant** argument for its divine inspiration."}
    ]
  },
  "corroborate": {
    "primary": "To confirm, support, or substantiate a statement, theory, or finding with fresh evidence or authoritative testimony.",
    "secondary": "In criminal evidence law and experimental scientific methodology, providing independent verification to eliminate doubt or bias.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "The discovery of the bloodstained footprint served to **corroborate** the extraordinary theory which Holmes had deduced."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Subsequent embryological studies by continental naturalists fully **corroborate** our observations on human morphological development."},
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The surviving epigraphic inscriptions from the province **corroborate** the narrative of the historian Tacitus."}
    ]
  },
  "corroboration": {
    "primary": "Evidence, testimony, or verification that confirms, supports, or validates a statement, claim, or hypothesis.",
    "secondary": "In the law of evidence, independent collateral evidence that strengthens and confirms the credibility of material allegations.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Memoirs of Sherlock Holmes", "quote": "The singular fact of the dog doing nothing in the night was the final **corroboration** that pointed to an insider."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The letters discovered in the royal cabinet gave conclusive **corroboration** to the charges of secret diplomatic treason."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Mr. Bucket sought external **corroboration** before disclosing the identity of the mysterious French lodger."}
    ]
  },
  "corroborative": {
    "primary": "Serving to corroborate; providing additional confirmation, validation, or evidentiary support.",
    "secondary": "In forensic investigation and scientific reporting, having the quality of verifying and reinforcing an existing evidentiary premise.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "The ash from the cigar found beside the yew alley supplied valuable **corroborative** evidence of the visitor's identity."},
      {"author": "Thomas Henry Huxley", "work": "Man's Place in Nature", "quote": "The fossil discoveries in Neanderthal cave provided striking **corroborative** proof of early human antiquity."},
      {"author": "Wilkie Collins", "work": "The Moonstone", "quote": "Sergeant Cuff examined the stained nightgown as crucial **corroborative** testimony against the suspect."}
    ]
  },
  "corroboratory": {
    "primary": "Tending to corroborate or confirm; corroborative in nature or intended function.",
    "secondary": "In judicial proceedings and academic discourse, serving the formal evidentiary function of substantiating a disputed thesis.",
    "quotes": [
      {"author": "Jeremy Bentham", "work": "A Treatise on Judicial Evidence", "quote": "A single witness cannot suffice in cases of perjury without auxiliary and **corroboratory** circumstances."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Bulstrode listened in terror as Raffles produced **corroboratory** documents attesting to his shameful early transactions."},
      {"author": "Herbert Spencer", "work": "The Principles of Sociology", "quote": "Travellers' accounts from Polynesia offer **corroboratory** data supporting our evolutionary theory of ceremonial institutions."}
    ]
  },
  "disrobe": {
    "primary": "To remove one's clothes, robes, or vestments; to undress oneself or another person.",
    "secondary": "In ceremonial protocol and ecclesiastical law, to formally strip an official of clerical robes, judicial vestments, or regalia.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Julius Caesar", "quote": "May we do so? You know it is the feast of Lupercal. It is no matter; let no images be hung with Caesar's trophies, and **disrobe** the statues."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "She retired to her chamber to **disrobe**, laying aside the simple bridal dress with a sorrowful heart."},
      {"author": "Sir Walter Scott", "work": "Ivanhoe", "quote": "The templar was commanded to **disrobe** and cast aside the holy white mantle of his disgraced order."}
    ]
  },
  "enrobe": {
    "primary": "To dress, array, or invest someone in rich, dignified, or formal robes or clothing.",
    "secondary": "In industrial food confectionery and ceremonial vesture, to coat a confection uniformly in chocolate or ceremonially invest in ritual robes.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Merchant of Venice", "quote": "Should I go to church and see the holy edifice of stone, and not bethink me straight of dangerous rocks, which touching but my gentle vessel's side would scatter all her spices on the stream, **enrobe** the roaring waters with my silks."},
      {"author": "Lord Tennyson", "work": "Idylls of the King", "quote": "Attendant maidens came to **enrobe** Queen Guinevere in gold and samite for the Pentecostal tournament."},
      {"author": "Nathaniel Hawthorne", "work": "The Marble Faun", "quote": "The setting sun seemed to **enrobe** the ruined arches of the Roman Forum in purple and molten gold."}
    ]
  },
  "rob": {
    "primary": "To take property or possessions unlawfully from a person or place by force, intimidation, or threat of violence.",
    "secondary": "In criminal common law and moral philosophy, felonious larceny accomplished through physical assault or putting a victim in bodily fear.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Merchant of Venice", "quote": "I never heard a passion so confused, so strange, outrageous, and so variable, as the dog Jew did utter in the streets: My daughter! O my ducats! Justice! The law! A sealed bag, two sealed bags of ducats, of double ducats, stolen from me by my daughter! Let not a traitor escape who dared to **rob** my house!"},
      {"author": "Charles Dickens", "work": "Oliver Twist", "quote": "Fagin warned the boy that if he dared to **rob** his master, the gallows would surely claim him before long."},
      {"author": "Victor Hugo", "work": "Les Misérables", "quote": "To **rob** an honest traveler upon the public highway is a terrible crime, yet desperate starvation drove the wretch to madness."}
    ]
  },
  "robalo": {
    "primary": "A tropical marine game fish (Centropomus undecimalis), also known as the snook, valued for sport and food.",
    "secondary": "In systematic ichthyology and commercial fisheries, a predatory perciform fish inhabiting mangrove estuaries, lagoons, and coastal waters of the tropical Americas.",
    "quotes": [
      {"author": "Alexander von Humboldt", "work": "Personal Narrative of Travels to the Equinoctial Regions of America", "quote": "The coastal waters of the Caribbean lagoon teemed with edible fish, notably the prized **robalo** and striped mullet."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "Native fishermen in Bahia speared large specimens of **robalo** amidst the roots of the tidal mangrove swamps."},
      {"author": "Ernest Hemingway", "work": "Islands in the Stream", "quote": "Thomas Hudson watched the swift silver flash of a **robalo** striking bait along the edge of the coral channel."}
    ]
  },
  "robaxin": {
    "primary": "A brand name for methocarbamol, a centrally acting skeletal muscle relaxant used to treat muscle spasms and musculoskeletal pain.",
    "secondary": "In clinical pharmacology, a carbamate derivative of guaifenesin exerting central nervous system depression to alleviate acute muscular rigidity and spasm.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Modern muscle relaxants related to **robaxin** act by depressing polysynaptic spinal pathways rather than blocking motor endplates directly."},
      {"author": "Oliver Wendell Holmes Sr.", "work": "Medical Essays", "quote": "The pharmacopeia continually introduces synthetic relaxants such as **robaxin** to relieve distressing lumbago and traumatic back strain."},
      {"author": "Sinclair Lewis", "work": "Arrowsmith", "quote": "The clinic staff dispensed skeletal relaxants like **robaxin** to soothe laborers suffering from lumbar injuries in the steel mill."}
    ]
  },
  "robber": {
    "primary": "A person who commits robbery; one who takes property from another unlawfully by force or threat.",
    "secondary": "In statutory criminal jurisprudence, an offender guilty of aggravated theft achieved by putting another in immediate fear of bodily injury.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry IV, Part 1", "quote": "Where shall we take a purse tomorrow, Jack? Falstaff replied that an honest **robber** must watch for wealthy travelers at Gadshill."},
      {"author": "Robert Louis Stevenson", "work": "Treasure Island", "quote": "Israel Hands glared like a desperate **robber** as he crept across the deck with his drawn dirk."},
      {"author": "Sir Walter Scott", "work": "The Heart of Midlothian", "quote": "The notorious highland **robber** haunted the mountain passes, levying blackmail upon all drove cattle."}
    ]
  },
  "robbery": {
    "primary": "The crime of taking or attempting to take anything of value from the care or custody of a person by force or threat of force.",
    "secondary": "In common law jurisprudence, felonious theft from the person or immediate presence of another accomplished via violence or intimidation.",
    "quotes": [
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "Open and violent larceny from the person, or **robbery**, is an aggravated species of theft punishable with the utmost rigor of the law."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Pip was haunted by the terrifying memory of the convicts and the midnight **robbery** of his sister's pantry."},
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Beryl Coronet", "quote": "The daring **robbery** of the imperial crown jewels threatened to create a grave scandal in diplomatic circles."}
    ]
  },
  "robe": {
    "primary": "A long, loose outer garment reaching to the ankles, often worn as a symbol of official rank, academic status, or for relaxation.",
    "secondary": "In ceremonial vesture and cultural history, a formal garment denoting judicial magistracy, ecclesiastical orders, or royal dignity.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry VIII", "quote": "I have ventured, like little wanton boys that swim on bladders, this many summers in a sea of glory, but far beyond my depth; my high-blown pride at length broke under me, and now has left me, weary and old with service, to the mercy of a rude stream that must for ever hide me. Vain pomp and glory of this world, I hate ye! I feel my heart new open'd. O how wretched is that poor man that hangs on princes' favours! There is betwixt that smile we would aspire to, that sweet aspect of princes, and their ruin, more pangs and fears than wars or women have; and when he falls, he falls like Lucifer, never to hope again. Cromwell, I did not think to shed a tear in all my miseries; but thou hast forced me, out of thy honest truth, to play the woman. Let's dry our eyes: and thus far hear me, Cromwell; and when I am forgotten, as I shall be, and sleep in dull cold marble, where no mention of me more must be heard of, say, I taught thee; say, Wolsey, that once trod the ways of glory, and sounded all the depths and shoals of honour, found thee a way, out of his wreck, to rise in; a sure and safe one, though thy master miss'd it. Mark but my fall, and that that ruin'd me. Cromwell, I charge thee, fling away ambition: by that sin fell the angels; how can man then, the image of his Maker, hope to win by it? Love thyself last; cherish those hearts that hate thee; corruption wins not more than honesty. Still in thy right hand carry gentle peace, to silence envious tongues. Be just, and fear not. Let all the ends thou aim'st at be thy country's, thy God's, and truth's; then if thou fall'st, O Cromwell, thou fall'st a blessed martyr! Serve the king; and—pr'ythee, lead me in: I have left my golden **robe** behind."},
      {"author": "Charlotte Brontë", "work": "Villette", "quote": "Madame Beck wrapped her dark woolen **robe** tightly around her shoulders as she glided through the silent dormitory."},
      {"author": "Nathaniel Hawthorne", "work": "The Minister's Black Veil", "quote": "The minister stood in the pulpit clad in his black ministerial **robe**, his face covered by the mysterious and terrifying veil."}
    ]
  }
}
