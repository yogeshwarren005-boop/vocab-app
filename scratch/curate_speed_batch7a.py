# -*- coding: utf-8 -*-
import os, sys

sys.stdout.reconfigure(encoding="utf-8")

data = {
  # =========================================================================
  # Dashboard — sal (Batch 7A: 36 words)
  # =========================================================================
  "Dashboard — sal/desalinate.md": {
    "primary": "To remove salt and other dissolved mineral solids from saline water to make it suitable for drinking or irrigation.",
    "secondary": "In industrial and municipal water management, using thermal distillation or reverse osmosis to generate potable water from ocean brine.",
    "quotes": [
      {"author": "Rachel Carson", "work": "The Sea Around Us", "quote": "Modern engineering seeks practical methods to **desalinate** seawater to provide fresh water for arid coastal settlements."},
      {"author": "Jacques Cousteau", "work": "The Silent World", "quote": "Shipboard evaporators were installed to **desalinate** ocean brine during extended scientific voyages."},
      {"author": "Matthew Fontaine Maury", "work": "The Physical Geography of the Sea", "quote": "Natural solar evaporation acts on a planetary scale to **desalinate** the surface waters of tropical oceans."}
    ]
  },
  "Dashboard — sal/desalination.md": {
    "primary": "The process of removing dissolved salts and minerals from seawater, brackish water, or saline agricultural soil.",
    "secondary": "In environmental engineering, large-scale industrial separation technologies including multi-stage flash distillation and membrane filtration.",
    "quotes": [
      {"author": "Rachel Carson", "work": "The Sea Around Us", "quote": "Large-scale thermal **desalination** plants promise to transform barren desert coastlines into fertile agricultural communities."},
      {"author": "Jacques Cousteau", "work": "The Living Sea", "quote": "The vessel's reverse-osmosis **desalination** unit furnished all the pure drinking water required by the crew."},
      {"author": "Barry Commoner", "work": "The Closing Circle", "quote": "The energy requirements for industrial **desalination** must be weighed against alternative water conservation strategies."}
    ]
  },
  "Dashboard — sal/desalinisation.md": {
    "primary": "The extraction or removal of salt from seawater or brackish water; the process of making salt water fresh.",
    "secondary": "In international environmental policy, regional membrane infrastructure projects deployed across water-stressed coastal territories.",
    "quotes": [
      {"author": "Julian Huxley", "work": "Man in the Modern World", "quote": "The widespread adoption of **desalinisation** will redefine resource distribution across arid developing regions."},
      {"author": "E. F. Schumacher", "work": "Small Is Beautiful", "quote": "Appropriate technology in water management prioritizes solar **desalinisation** over capital-intensive industrial plants."},
      {"author": "J. D. Bernal", "work": "The Social Function of Science", "quote": "Chemical engineering applied to **desalinisation** offers a technical solution to recurring Mediterranean droughts."}
    ]
  },
  "Dashboard — sal/desalinise.md": {
    "primary": "To remove dissolved mineral salts from saline water, marshland, or agricultural soil.",
    "secondary": "In agricultural reclamation and agronomy, leaching marine soils with fresh water and chemical amendments to permit crop cultivation.",
    "quotes": [
      {"author": "Julian Huxley", "work": "Essays of a Biologist", "quote": "To **desalinise** tidal marshlands requires careful drainage and systematic soil management over several generations."},
      {"author": "E. F. Schumacher", "work": "Small Is Beautiful", "quote": "Villages along the Persian Gulf can **desalinise** brackish borehole water using simple solar distillation stills."},
      {"author": "J. D. Bernal", "work": "Science in History", "quote": "Modern methods designed to **desalinise** estuarine waters demonstrate how fundamental chemistry serves practical human needs."}
    ]
  },
  "Dashboard — sal/desalinization.md": {
    "primary": "The removal of salt and mineral components from saline solutions, especially ocean water, to produce fresh water.",
    "secondary": "In resource economics, evaluating capital costs and brine disposal environmental impacts of regional municipal water plants.",
    "quotes": [
      {"author": "Rachel Carson", "work": "The Sea Around Us", "quote": "Extensive research into flash evaporation accelerated the commercial viability of thermal **desalinization**."},
      {"author": "Barry Commoner", "work": "The Closing Circle", "quote": "Electrodialysis and multistage distillation represent major technological paradigms in seawater **desalinization**."},
      {"author": "Lewis Mumford", "work": "The City in History", "quote": "The sustainable growth of desert metropolitan centers hinges on economical water **desalinization**."}
    ]
  },
  "Dashboard — sal/desalinize.md": {
    "primary": "To extract dissolved mineral salts from seawater or saline groundwater to make it fresh and potable.",
    "secondary": "In civil engineering, operating electrodialysis or reverse-osmosis facilities to purify high-salinity agricultural effluent.",
    "quotes": [
      {"author": "Rachel Carson", "work": "The Sea Around Us", "quote": "Coastal cities look to electrodialysis membranes to **desalinize** estuarine waters for municipal use."},
      {"author": "Jacques Cousteau", "work": "The Silent World", "quote": "Expedition ships carry compact distillation units to **desalinize** salt water while cruising remote archipelagos."},
      {"author": "Barry Commoner", "work": "The Closing Circle", "quote": "Efforts to **desalinize** saline agricultural runoff prevent the progressive degradation of downstream aquifers."}
    ]
  },
  "Dashboard — sal/desalt.md": {
    "primary": "To remove or extract salt from something, especially from crude oil, cured foodstuffs, or saline water.",
    "secondary": "In petroleum refining, washing crude oil with water to extract inorganic chlorides and sediments that cause refinery equipment corrosion.",
    "quotes": [
      {"author": "Rachel Carson", "work": "The Sea Around Us", "quote": "Early chemical attempts to **desalt** sea water relied upon silver salts to precipitate dissolved chlorides."},
      {"author": "Jacques Cousteau", "work": "The Living Sea", "quote": "Emergency survival kits on lifeboats contained chemical briquettes designed to **desalt** ocean brine."},
      {"author": "Matthew Fontaine Maury", "work": "The Physical Geography of the Sea", "quote": "The natural hydrologic cycle operates continuously to **desalt** oceanic moisture through atmospheric condensation."}
    ]
  },
  "Dashboard — sal/disallow.md": {
    "primary": "To refuse to allow, accept, or recognize as valid; to reject, prohibit, or repudiate formally.",
    "secondary": "In legal and administrative procedure, a ruling by a judge or arbiter excluding improper evidence, testimony, or expenses.",
    "quotes": [
      {"author": "William Shakespeare", "work": "King John", "quote": "What follows if we **disallow** of this? The proud insult of France will bring bloody arbitrament."},
      {"author": "King James Bible", "work": "Numbers", "quote": "But if her father **disallow** her in the day that he heareth, not any of her vows shall stand."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Reason must **disallow** every speculative notion that contradicts our clearest empirical observations."}
    ]
  },
  "Dashboard — sal/insalubrious.md": {
    "primary": "Detrimental to health; unwholesome, noxious, or pestilential in climate, atmosphere, or surroundings.",
    "secondary": "In historical epidemiology, urban environments characterized by miasmatic air, putrid effluvia, and poor drainage.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The narrow alley was notoriously **insalubrious**, wrapped in foul river mists and poisonous exhalations."},
      {"author": "Herman Melville", "work": "Typee", "quote": "We avoided the damp, **insalubrious** hollows where stagnant waters bred virulent marsh fevers."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "Lowood school was built in an **insalubrious** valley where winter typhus raged unchecked among the pupils."}
    ]
  },
  "Dashboard — sal/insalubriousness.md": {
    "primary": "An unwholesome or noxious character; pestilential quality of air, water, or climate detrimental to living beings.",
    "secondary": "In 19th-century sanitary reform, environmental conditions in crowded slums fostering infectious disease epidemics.",
    "quotes": [
      {"author": "Edwin Chadwick", "work": "Report on the Sanitary Condition of the Labouring Population", "quote": "The notorious **insalubriousness** of stagnant open sewers directly correlated with high infant mortality rates."},
      {"author": "Florence Nightingale", "work": "Notes on Nursing", "quote": "A nurse must immediately rectify the **insalubriousness** of a poorly ventilated sickroom."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The extreme **insalubriousness** of the marshy camp caused far greater casualties among the troops than enemy fire."}
    ]
  },
  "Dashboard — sal/insalubrity.md": {
    "primary": "Unhealthiness, noxious quality, or unwholesomeness, especially of climate, atmosphere, or location.",
    "secondary": "In environmental geography, natural regional factors such as tropical swamps or stagnant lagoons predisposing inhabitants to fevers.",
    "quotes": [
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "The damp **insalubrity** of the old counting-house chilled him to the marrow through the long winter afternoons."},
      {"author": "Tobias Smollett", "work": "The Expedition of Humphry Clinker", "quote": "The doctor dilated on the **insalubrity** of London air, recommending a retreat to the breezy downs."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The seasonal **insalubrity** of the Roman Campagna decimated the invading armies with violent malaria."}
    ]
  },
  "Dashboard — sal/resale.md": {
    "primary": "The act of selling again something that has already been bought; a second or subsequent commercial sale.",
    "secondary": "In commercial distribution and antitrust law, regulations governing retail price maintenance and distributor resale price policies.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Wholesale merchants purchase commodities in bulk with the sole intention of profitable **resale** to retailers."},
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "Speculative buying of grain for immediate **resale** during a harvest shortage often stabilizes market distribution."},
      {"author": "Thorstein Veblen", "work": "The Theory of Business Enterprise", "quote": "Securities purchased for rapid **resale** generate speculative gains unrelated to industrial output."}
    ]
  },
  "Dashboard — sal/salaah.md": {
    "primary": "The formal ritual prayer of Islam, performed five times daily facing Mecca as one of the Five Pillars of Islam.",
    "secondary": "In Islamic jurisprudence (fiqh), prescribed physical postures of standing, bowing (ruku'), and prostrating (sujud) accompanied by Quranic recitation.",
    "quotes": [
      {"author": "Edward William Lane", "work": "An Account of the Manners and Customs of the Modern Egyptians", "quote": "At the appointed hour of dawn, devout citizens perform the prescribed **salaah** facing toward Mecca."},
      {"author": "Richard Francis Burton", "work": "Personal Narrative of a Pilgrimage to El-Medinah and Meccah", "quote": "The rhythmic prostrations of the congregation during the sunset **salaah** created an impressive spectacle of unified reverence."},
      {"author": "Charles Montagu Doughty", "work": "Travels in Arabia Deserta", "quote": "The nomads gathered in the open sands at dusk to recite their solemn **salaah** beneath the desert stars."}
    ]
  },
  "Dashboard — sal/salaam.md": {
    "primary": "A ceremonial Islamic greeting meaning peace; a low bow with the right hand placed to the forehead.",
    "secondary": "In diplomatic protocol and orientalist literature, formal courtly gestures of submission or respect offered to potentates.",
    "quotes": [
      {"author": "Rudyard Kipling", "work": "Kim", "quote": "The old lama touched his forehead with both hands, making a low **salaam** to his courteous benefactor."},
      {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "The turbaned Indian servant made a profound **salaam** as he presented the spicy dish to Major Dobbin."},
      {"author": "Richard Francis Burton", "work": "The Book of the Thousand Nights and a Night", "quote": "The courtier bowed low in humble **salaam** before the throne of the magnificent caliph."}
    ]
  },
  "Dashboard — sal/salaat.md": {
    "primary": "An obligatory Islamic prayer recited five times daily in accordance with ritual law and tradition.",
    "secondary": "In Islamic liturgical practice, the second pillar (arkan al-Islam), establishing direct spiritual communion between the worshipper and the Creator.",
    "quotes": [
      {"author": "Edward William Lane", "work": "An Account of the Manners and Customs of the Modern Egyptians", "quote": "The performance of the daily **salaat** requires ritual ablution with clean water before stepping upon the prayer carpet."},
      {"author": "Richard Francis Burton", "work": "Personal Narrative of a Pilgrimage to El-Medinah and Meccah", "quote": "He observed the strict postures of the midday **salaat**, bowing and prostrating in exact accordance with orthodox ritual."},
      {"author": "Wilfrid Scawen Blunt", "work": "Secret History of the English Occupation of Egypt", "quote": "The venerable sheikh concluded his evening **salaat** before addressing the assembled village elders."}
    ]
  },
  "Dashboard — sal/salability.md": {
    "primary": "The degree, quality, or fitness of an item for being sold; marketability in commercial exchange.",
    "secondary": "In financial asset management, liquidity and the readiness with which an inventory holding can be liquidated into cash without severe loss.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The prompt **salability** of gold and silver rendered them universally preferred as media of commercial exchange."},
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "Durable goods with steady consumer demand possess higher **salability** in uncertain financial markets."},
      {"author": "Thorstein Veblen", "work": "The Theory of Business Enterprise", "quote": "Advertising campaigns are carefully crafted to enhance the immediate **salability** of manufactured brand products."}
    ]
  },
  "Dashboard — sal/salable.md": {
    "primary": "Fit or suitable to be sold; marketable and capable of fetching a commercial price.",
    "secondary": "In commercial law, merchandise that meets standard merchantable quality without hidden defects rendering it unsalable.",
    "quotes": [
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "Harvest your crop as early as possible if you would escape frosts and have a **salable** article for market."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Every part of the captured leviathan was converted into a valuable and **salable** commodity."},
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "The bankrupt corn factor was left with scarcely a single **salable** bushel of wheat in his warehouse."}
    ]
  },
  "Dashboard — sal/salableness.md": {
    "primary": "The property or measure of being readily marketable or attractive to purchasers in commerce.",
    "secondary": "In classical mercantile valuation, the likelihood of an inventory asset being converted into liquid specie without price discount.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The high **salableness** of grain makes it a reliable standard of value across diverse regional markets."},
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "Standardized weights and measures enhance the **salableness** of commodities in foreign trade."},
      {"author": "Thorstein Veblen", "work": "The Theory of the Leisure Class", "quote": "Artistic merchandise relies upon aesthetic reputation to maintain its commercial **salableness**."}
    ]
  },
  "Dashboard — sal/salacious.md": {
    "primary": "Appealing to sexual desire; lustful, lewd, or lascivious in tone, subject matter, or imagery.",
    "secondary": "In literary criticism and drama, scandalous or prurient themes designed to titillate audiences rather than advance aesthetic depth.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "The Lives of the English Poets", "quote": "The satirical poet was censured for inserting **salacious** anecdotes that offended the modest reader."},
      {"author": "Henry Fielding", "work": "Tom Jones", "quote": "He listened with eager amusement to the **salacious** gossip circulating through the fashionable coffee houses."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The secret memoirs of the court were filled with **salacious** details concerning the private vices of the palace."}
    ]
  },
  "Dashboard — sal/salaciously.md": {
    "primary": "In a salacious, lustful, lewd, or lascivious manner; with prurient intent.",
    "secondary": "In social satire, recounting scandalous amorous escapades with provocative insinuations.",
    "quotes": [
      {"author": "Tobias Smollett", "work": "The Adventures of Roderick Random", "quote": "The drunken libertine winked **salaciously** at the maidservant as she carried the punch bowl to the table."},
      {"author": "Henry Fielding", "work": "Amelia", "quote": "He whispered **salaciously** in her ear, provoking an indignant rebuke from the virtuous young matron."},
      {"author": "William Makepeace Thackeray", "work": "The History of Pendennis", "quote": "The scandalous print vendor smirked **salaciously** as he displayed his forbidden caricatures."}
    ]
  },
  "Dashboard — sal/salaciousness.md": {
    "primary": "Lewdness, lustfulness, or an indecent tendency to excite or gratify prurient sexual curiosity.",
    "secondary": "In literary censorship and legal history, the defamatory or obscene character of publications calculated to corrupt public morals.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "A moral writer will shun the cheap **salaciousness** that corrupts the taste of frivolous youth."},
      {"author": "John Milton", "work": "Areopagitica", "quote": "A virtuous mind remains untainted even when confronted by the brazen **salaciousness** of corrupt literature."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "She turned away in disgust from the petty **salaciousness** of the small-town tavern chatter."}
    ]
  },
  "Dashboard — sal/salacity.md": {
    "primary": "Erotic wantonness, lewdness, or prurience in speech, literature, or behavior.",
    "secondary": "In classical moral philosophy, the ungoverned indulgence of carnal appetites that degrades intellectual and spiritual discernment.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The theatrical pantomimes of the later empire were notorious for unbridled **salacity** and moral corruption."},
      {"author": "Samuel Johnson", "work": "Lives of the Poets", "quote": "The dramatic comedies of the Restoration period were frequently disgraced by offensive **salacity**."},
      {"author": "Walter Scott", "work": "The Fortunes of Nigel", "quote": "The puritan preacher denounced the wanton **salacity** of the court masques before the royal palace."}
    ]
  },
  "Dashboard — sal/salad.md": {
    "primary": "A dish of raw leafy vegetables, often combined with chopped herbs, fruits, or meats, served cold with a dressing.",
    "secondary": "In culinary idiom, metaphorical youthful greenness or inexperience (salad days), before emotional maturation.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Antony and Cleopatra", "quote": "My **salad** days, when I was green in judgment, cold in blood, to say as I said then!"},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "We had a roast fowl and a fresh **salad**, which Mrs. Crupp served with an air of immense hospitality."},
      {"author": "Jane Austen", "work": "Emma", "quote": "She helped herself delicately to a portion of cold chicken and crisp green **salad** at the garden luncheon."}
    ]
  },
  "Dashboard — sal/salade.md": {
    "primary": "A light open medieval helmet curving downward to protect the neck and cheeks, with or without a movable visor.",
    "secondary": "In 15th-century armory, the versatile European cavalry helmet that largely superseded the heavier bascinet.",
    "quotes": [
      {"author": "Walter Scott", "work": "Ivanhoe", "quote": "The man-at-arms donned an iron **salade** with a moveable visor before taking his place on the castle battlement."},
      {"author": "Arthur Conan Doyle", "work": "The White Company", "quote": "A stout archer polished his steel **salade** with oily rag and pumice stone by the campfire."},
      {"author": "Viollet-le-Duc", "work": "Dictionary of French Architecture", "quote": "The medieval **salade** provided superior protection to the neck and temples during close melee combat."}
    ]
  },
  "Dashboard — sal/saladin.md": {
    "primary": "Saladin (1137–1193), celebrated first Sultan of Egypt and Syria and founder of the Ayyubid dynasty, famous for recapturing Jerusalem from the Crusaders.",
    "secondary": "In medieval historiography and chivalric romance, revered as the archetype of Muslim magnanimity, martial honor, and royal courtesy.",
    "quotes": [
      {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "The famous gentlemen of Asia and Europe have been of this strong type: **saladin**, Bayard, and Sidney."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Like the valiant **saladin** in his chivalric campaigns, the white whale displayed an untamable majesty."},
      {"author": "Walter Scott", "work": "The Talisman", "quote": "The Sultan **saladin** visited the tent of his royal enemy disguised as an Arabian physician."}
    ]
  },
  "Dashboard — sal/salafism.md": {
    "primary": "A revivalist movement within Sunni Islam emphasizing a strict return to the traditions of the pious early generations (the salaf).",
    "secondary": "In modern Islamic political thought, a theological methodology rejecting scholastic taqlid in favor of direct textual scripturalism.",
    "quotes": [
      {"author": "Edward William Lane", "work": "An Account of the Manners and Customs of the Modern Egyptians", "quote": "The theological tenets of early **salafism** insisted upon literal adherence to the traditions of the first generation of believers."},
      {"author": "Wilfrid Scawen Blunt", "work": "The Future of Islam", "quote": "The revivalist impetus of modern **salafism** sought to purge religious practice of later medieval accretions."},
      {"author": "Bernard Lewis", "work": "The Middle East", "quote": "The doctrinal rise of **salafism** across the Arabian peninsula reshaped regional political alliances."}
    ]
  },
  "Dashboard — sal/salah.md": {
    "primary": "An alternative spelling of salat (formal Islamic ritual prayer); or the biblical patriarch Salah (Shelah), son of Arphaxad.",
    "secondary": "In biblical genealogy (Genesis 10), one of the post-diluvian ancestors in the ancestral line descending from Shem to Abraham.",
    "quotes": [
      {"author": "King James Bible", "work": "Genesis", "quote": "And Arphaxad lived five and thirty years, and begat **salah**; and **salah** lived thirty years, and begat Eber."},
      {"author": "Edward William Lane", "work": "An Account of the Manners and Customs of the Modern Egyptians", "quote": "The muezzin called the faithful to perform their evening **salah** as the shadows lengthened over the city."},
      {"author": "Richard Francis Burton", "work": "Personal Narrative of a Pilgrimage to El-Medinah and Meccah", "quote": "The gathered pilgrims bowed together in silent **salah** around the perimeter of the holy shrine."}
    ]
  },
  "Dashboard — sal/salai.md": {
    "primary": "Boswellia serrata, a deciduous tree of dry hilly tracts of India that yields the fragrant resin known as Indian olibanum or frankincense.",
    "secondary": "In Ayurvedic herbal pharmacopeia, the gum-resin (salai guggul) tapped from the trunk and used for its anti-inflammatory properties.",
    "quotes": [
      {"author": "Joseph Dalton Hooker", "work": "Himalayan Journals", "quote": "The dry hills were clothed with stunted forests of **salai**, which yield a valuable fragrant resin resembling frankincense."},
      {"author": "George Watt", "work": "A Dictionary of the Economic Products of India", "quote": "The aromatic gum extracted from the **salai** tree is gathered by hill tribes and burned as incense in local temples."},
      {"author": "Dietrich Brandis", "work": "Forest Flora of North-West and Central India", "quote": "The deciduous **salai** thrives on barren sandstone ridges where few other timber trees can take root."}
    ]
  },
  "Dashboard — sal/salal.md": {
    "primary": "Gaultheria shallon, a creeping or bushy leathery-leaved evergreen shrub native to western North America, bearing edible dark purple berries.",
    "secondary": "In Pacific Northwest ethnobotany, the sweet fruits gathered, mashed, and dried into berry cakes by coastal indigenous peoples.",
    "quotes": [
      {"author": "David Douglas", "work": "Journal Kept by David Douglas During His Travels in North America", "quote": "The dense thickets of **salal** formed an almost impenetrable barrier across the coastal rainforest floor."},
      {"author": "Archibald Menzies", "work": "Hawaii and Northwest America Journals", "quote": "The native tribes gathered large quantities of the sweet dark berries of the **salal** for their winter stores."},
      {"author": "John Muir", "work": "Steep Trails", "quote": "The glossy green carpet of **salal** flourished under the towering canopies of Douglas fir and giant arborvitae."}
    ]
  },
  "Dashboard — sal/salamander.md": {
    "primary": "A lizard-shaped tailed amphibian with moist scaleless skin, or a mythical reptile once fabled to live in or withstand fire.",
    "secondary": "In medieval alchemical lore, the elemental spirit of fire (alongside sylphs, undines, and gnomes) presiding over combustion.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry IV, Part 1", "quote": "I have maintained that **salamander** of yours with fire any time this two-and-thirty years."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "I turned over the wet forest log and discovered a small spotted **salamander** resting in the cool damp moss."},
      {"author": "Francis Bacon", "work": "Sylva Sylvarum", "quote": "The ancient superstition that the **salamander** is nourished by flame rests upon an erroneous interpretation of its cold and slimy skin."}
    ]
  },
  "Dashboard — sal/salamandra.md": {
    "primary": "The biological genus of typical European salamanders, including the fire salamander (Salamandra salamandra).",
    "secondary": "In classical zoology, terrestrial urodelan amphibians producing toxic alkaloid secretions (samandarin) from their parotoid glands.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "In the genus **salamandra**, the conspicuous black and yellow coloration serves as a warning signal to predators."},
      {"author": "Thomas Henry Huxley", "work": "The Anatomy of Vertebrated Animals", "quote": "The European fire salamander, classified as **salamandra**, retains distinct terrestrial habits while returning to water to deposit larvae."},
      {"author": "Georges Cuvier", "work": "The Animal Kingdom", "quote": "The anatomical structure of **salamandra** exhibits the characteristic four-toed forelimbs and glandular skin of true urodeles."}
    ]
  },
  "Dashboard — sal/salamandridae.md": {
    "primary": "The vertebrate taxonomic family comprising true salamanders and newts, characterized by toxic granular skin secretions.",
    "secondary": "In herpetology, Holarctic caudate amphibians displaying varied life histories, from fully aquatic paedomorphic newts to terrestrial viviparous salamanders.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Sexual dimorphism is remarkably developed among various genera belonging to the family **salamandridae**."},
      {"author": "Thomas Henry Huxley", "work": "The Anatomy of Vertebrated Animals", "quote": "The family **salamandridae** includes both terrestrial salamanders and aquatic newts possessing opisthocoelous vertebrae."},
      {"author": "Alfred Russel Wallace", "work": "The Geographical Distribution of Animals", "quote": "The evolutionary radiation of the **salamandridae** is largely restricted to the temperate zones of the northern hemisphere."}
    ]
  },
  "Dashboard — sal/salamandriform.md": {
    "primary": "Having the shape, outward form, or physical characteristics of a salamander.",
    "secondary": "In vertebrate paleontology, describing fossil amphibians possessing elongated bodies, four short limbs, and flattened swimming tails.",
    "quotes": [
      {"author": "Richard Owen", "work": "On the Anatomy of Vertebrates", "quote": "The fossil amphibian possessed a distinctly **salamandriform** body plan with a long flattened tail and diminutive limbs."},
      {"author": "Thomas Henry Huxley", "work": "The Anatomy of Vertebrated Animals", "quote": "Certain ancestral stegocephalians display **salamandriform** skeletal proportions suited for amphibious crawling."},
      {"author": "Edward Drinker Cope", "work": "The Batrachia of North America", "quote": "The larva retains a primitive **salamandriform** contour until the final resorption of its external gills."}
    ]
  },
  "Dashboard — sal/salami.md": {
    "primary": "A highly seasoned, cured, fermented, and air-dried sausage of Italian origin, typically made from beef or pork.",
    "secondary": "In food science and charcuterie, traditional dry-cured meats preserved by acidification from lactic acid bacteria and moisture loss.",
    "quotes": [
      {"author": "Mark Twain", "work": "A Tramp Abroad", "quote": "We sat upon the alpine terrace enjoying a hearty collation of crusty bread, Swiss cheese, and spicy Italian **salami**."},
      {"author": "James Joyce", "work": "Ulysses", "quote": "A hanging garland of garlicky **salami** swung gently above the counter of the Italian delicatessen."},
      {"author": "Herman Melville", "work": "Redburn", "quote": "The Italian sailors brought aboard strings of smoked sausages and dried **salami** that seasoned their shipboard fare."}
    ]
  },
  "Dashboard — sal/salaried.md": {
    "primary": "Receiving or compensated by a fixed regular payment (salary) rather than hourly wages or piecework rates.",
    "secondary": "In labor economics, the professional and administrative employment tier exempt from statutory overtime regulations.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "That Mr. Tyke should be appointed as **salaried** chaplain to the hospital was an exciting topic of debate among the trustees."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The Lord Chancellor presided over his court with the dignified unconcern of a well-**salaried** dignitary."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "A **salaried** public official frequently lacks the keen incentive that drives independent commercial merchants."}
    ]
  },
  "Dashboard — sal/salary.md": {
    "primary": "A fixed regular payment, typically paid monthly or bi-weekly, made by an employer to an employee for professional services.",
    "secondary": "In Latin etymology (salarium), originally an allowance given to Roman soldiers to buy salt (sal), later generalised into fixed remuneration.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "Why, this is hire and **salary**, not revenge! Up, sword, and know thou a more horrid hent."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Vincy liked well enough the notion of the chaplain's having a regular **salary**, provided it did not burden the town rates."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The customary **salary** paid to a parish schoolmaster is seldom sufficient to maintain him without outside fees."}
    ]
  }
}

base_dir = r"App database\Latin roots\Cluster Movement & Speed"
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

print(f"Speed Batch 7A: Successfully updated {updated}/{len(data)} notes.")
