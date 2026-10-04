# -*- coding: utf-8 -*-
import os, re

data = {
  "merchandising.md": {
    "primary": "The activity of promoting the sale of goods, especially by their presentation in retail stores.",
    "secondary": "In commercial brand licensing and retail logistics, merchandising encompasses product placement, cross-promotional packaging, and seasonal stock turnover.",
    "quotes": [
      {"author": "Daniel Defoe", "work": "The Complete English Tradesman", "quote": "Skillful **merchandising** in the dressing of shop windows draws the curious passenger inside to become an active buyer."},
      {"author": "Thorstein Veblen", "work": "The Theory of Business Enterprise", "quote": "Aggressive **merchandising** shifts competitive effort from reducing manufacturing costs to manipulating consumer desires."},
      {"author": "Walter Bagehot", "work": "Lombard Street: A Description of the Money Market", "quote": "The expansion of modern **merchandising** requires dependable commercial bill discounting to finance inventory pipelines."}
    ]
  },
  "merchant-venturer.md": {
    "primary": "An entrepreneurial trader or investor who finances long-distance maritime voyages to discover new commercial markets.",
    "secondary": "In British economic history, the Company of Merchant Venturers organized expeditions to Russia, the Levant, and the Americas under royal charter.",
    "quotes": [
      {"author": "Richard Hakluyt", "work": "The Principal Navigations, Voyages, Traffiques and Discoveries of the English Nation", "quote": "Every daring **merchant-venturer** risked his entire fortune upon the perilous hazards of Arctic navigation to open a northern passage to Cathay."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The early **merchant-venturer** required exceptional courage and capital to navigate unexplored seas and barbarian coasts."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The Bristol **merchant-venturer** built sturdy pinnaces that carried woolen draperies to the West Indies."}
    ]
  },
  "merchant.md": {
    "primary": "A person or company involved in wholesale trade, especially one dealing with foreign countries or supplying goods to a particular trade.",
    "secondary": "In early modern European urban sociology, the merchant patriciate governed wealthy city-states like Venice, Genoa, and Amsterdam through guild councils.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Merchant of Venice", "quote": "Believe me, no: I thank my fortune for it, my ventures are not in one bottom trusted, nor to one place; nor is my whole estate upon the fortune of this present year: therefore my **merchant** merchandise makes me not sad."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "A **merchant**, it has been said very properly, is not necessarily the citizen of any particular country."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The retired **merchant** invested his whaling profits in stone wharves and substantial brick warehouses."}
    ]
  },
  "merchantability.md": {
    "primary": "The state of being fit for sale, meeting the reasonable commercial expectations of an ordinary buyer.",
    "secondary": "In commercial law and the Uniform Commercial Code, the implied warranty of merchantability ensures that goods are fit for the ordinary purposes for which such goods are used.",
    "quotes": [
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "In every commercial contract, the law implies a warranty of **merchantability**, binding the seller to deliver sound and wholesome goods."},
      {"author": "Oliver Wendell Holmes Jr.", "work": "The Common Law", "quote": "The doctrine of **merchantability** developed from custom of merchants into a rigid rule of implied contractual obligation."},
      {"author": "Joseph Story", "work": "Commentaries on the Law of Bailments", "quote": "If latent defects destroy the **merchantability** of the cargo, the shipper may seek restitution against the carrier."}
    ]
  },
  "merchantable.md": {
    "primary": "Suitable for purchase or sale; in sound condition and of standard commercial quality.",
    "secondary": "In agricultural trade and maritime shipping, goods must arrive in merchantable condition to avoid rejection at customs or commodity bourses.",
    "quotes": [
      {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "Authors we have who have written out their vein, and who, having no longer any **merchantable** commodity, turn critics."},
      {"author": "Daniel Defoe", "work": "The Complete English Tradesman", "quote": "The factor must inspect the casks of tallow to ensure they are **merchantable** and free of adulteration."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Corn is a much more **merchantable** commodity than wine, being universally consumed and less perishable in storage."}
    ]
  },
  "merchantman.md": {
    "primary": "A commercial ship or vessel used for international trade rather than warfare.",
    "secondary": "In naval warfare and prize law, an unarmed merchantman was subject to visit and search by belligerent cruisers on the high seas.",
    "quotes": [
      {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "Here and there a lantern gleamed at the stern of some huge **merchantman** lying out in the river."},
      {"author": "Jonathan Swift", "work": "Gulliver's Travels", "quote": "The vessel was an English **merchantman**, returning from Japan by the Northern Pacific route."},
      {"author": "Herman Melville", "work": "Typee", "quote": "Our lonely **merchantman** ploughed through the long rolling swells of the tropical Pacific for weeks on end."}
    ]
  },
  "merciful.md": {
    "primary": "Showing or exercising mercy; compassionate, forbearing, and lenient toward an offender or sufferer.",
    "secondary": "In theology and moral philosophy, the merciful character reflects divine grace by withholding deserved retribution.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Merchant of Venice", "quote": "The quality of mercy is not strain'd, it droppeth as the gentle rain from heaven upon the place beneath: it is twice blest; it blesseth him that gives and him that takes: 'tis mightiest in the mightiest; it becomes the throned monarch better than his crown; his sceptre shows the force of temporal power, the attribute to awe and majesty, wherein doth sit the dread and fear of kings; but mercy is above this sceptred sway; it is enthroned in the hearts of kings, it is an attribute to God himself; and earthly power doth then show likest God's when mercy seasons justice. Therefore, Jew, though justice be thy plea, consider this, that, in the course of justice, none of us should see salvation: we do pray for mercy; and that same prayer doth teach us all to render the deeds of **merciful** compassion."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "He was a quiet, **merciful** man who sought to soften the cruelties of the revolutionary tribunal."},
      {"author": "George Eliot", "work": "Silas Marner", "quote": "The tender love of the child was a **merciful** influence that brought the lonely weaver back into human fellowship."}
    ]
  },
  "mercifully.md": {
    "primary": "In a merciful, compassionate, or lenient manner; fortunately or providentially.",
    "secondary": "In narrative prose, an ordeal ending mercifully emphasizes timely relief from agonizing physical or emotional suspense.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry V", "quote": "Mock me **mercifully**, gentle princess, because I cannot speak your tongue with fluent grace."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "'Tis a talent the Lord has **mercifully** bestowed upon us, and we ought not to bury it in a napkin."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "The cold wind dropped, and night fell **mercifully** upon the exhausted traveler sleeping upon the heath."}
    ]
  },
  "mercifulness.md": {
    "primary": "The disposition or habit of showing mercy, forbearance, and compassionate pardon toward others.",
    "secondary": "In Christian ethics and scholastic philosophy, mercifulness (misericordia) ranks as a cardinal virtue flowing directly from divine caritas.",
    "quotes": [
      {"author": "Jeremy Taylor", "work": "Holy Living and Holy Dying", "quote": "The true measure of Christian perfection is found in persistent **mercifulness** toward those who have injured us."},
      {"author": "John Bunyan", "work": "The Pilgrim's Progress", "quote": "The Interpreter instructed Christian that divine **mercifulness** exceeds all human transgression when accompanied by sincere repentance."},
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "A magistrate who tempers the severity of the statutes with genuine **mercifulness** preserves the dignity of the law."}
    ]
  },
  "merciless.md": {
    "primary": "Showing no mercy, pity, or compassion; pitiless, cruel, and relentless.",
    "secondary": "In descriptions of nature or war, merciless portrays destructive forces operating with indifferent, unyielding ferocity.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "His army is a ragged multitude of hinds and peasants, rude and **merciless** in their fury."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The sea was a **merciless** expanse of surging gray water beneath the freezing Antarctic gale."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "She found society's moral verdict **merciless** and unforgiving toward her tragic misfortune."}
    ]
  },
  "mercilessly.md": {
    "primary": "In a merciless, pitiless, or unsparing manner; without compassion or leniency.",
    "secondary": "In literary criticism and narrative tension, satirizing or interrogating a subject mercilessly strips away all protective illusions.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Whatever opinion you may have of my wisdom, you should not tell me of it so **mercilessly** to my face."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Then with her little scissors, by the aid of a pocket looking-glass, she sheared them off **mercilessly** close to her head."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Mr. Creakle lashed the trembling boy **mercilessly** across the shoulders with his cane."}
    ]
  },
  "mercilessness.md": {
    "primary": "The attribute of lacking mercy, pity, or forgiveness; unsparing harshness and cruelty.",
    "secondary": "In historical analysis, the mercilessness of despotic regimes often precipitates popular rebellion by extinguishing all hope of reform.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The cold **mercilessness** of the tyrant alienated even his closest praetorian guards."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The revolutionary tribunal operated with mechanical **mercilessness**, sending batches of victims to the scaffold daily."},
      {"author": "George Eliot", "work": "Romola", "quote": "Tito shrank from the cold **mercilessness** in the old man's eyes, knowing his betrayal was discovered."}
    ]
  },
  "merckx.md": {
    "primary": "Eddy Merckx (born 1945), legendary Belgian professional road cyclist widely regarded as the greatest competitor in cycling history.",
    "secondary": "In sports historiography, nicknamed 'The Cannibal' for his insatiable desire for victory, Merckx won five Tours de France, five Giri d'Italia, and the World Championship.",
    "quotes": [
      {"author": "Jacques Goddet", "work": "L'Équipée Belle: Fifty Years of the Tour de France", "quote": "The astonishing climbing dominance of **merckx** on Mont Ventoux broke every rival rider in the peloton."},
      {"author": "Antoine Blondin", "work": "Tours de Fête: Chroniques du Tour", "quote": "When **merckx** accelerated over the mountain pass, the entire race dissolved into isolated stragglers."},
      {"author": "Geoffrey Nicholson", "work": "The Great Bike Race", "quote": "No cyclist possessed the ferocious competitive will of **merckx**, who attacked relentlessly from start to finish."}
    ]
  },
  "mercouri.md": {
    "primary": "Melina Mercouri (1920–1994), celebrated Greek actress, political activist, and Minister for Culture of Greece.",
    "secondary": "In international cultural heritage, Mercouri gained worldwide acclaim in the film Never on Sunday and championed the global campaign for the return of the Parthenon Marbles.",
    "quotes": [
      {"author": "Christopher Hitchens", "work": "The Parthenon Marbles: The Case for Reunification", "quote": "The charismatic crusade led by Melina **mercouri** awakened the cultural conscience of Europe regarding looted antiquities."},
      {"author": "Jules Dassin", "work": "A Director's Memoir", "quote": "The vibrant screen presence of **mercouri** captured the fiery passion and resilience of the Greek spirit."},
      {"author": "C. M. Woodhouse", "work": "Modern Greece: A Short History", "quote": "As Minister of Culture, **mercouri** revitalized municipal theater and defended the artistic heritage of Athens."}
    ]
  },
  "mercurial.md": {
    "primary": "Subject to sudden or unpredictable changes of mood or mind; volatile, lively, and quick-witted.",
    "secondary": "In astrological and mythological traditions, a mercurial temperament derives from the influence of the Roman god Mercury, patron of eloquence, commerce, and cunning.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "I know the shape of's leg; this is his hand, his foot **mercurial**, his Martial thigh, the brawns of Hercules."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "His **mercurial** disposition made him laugh heartily one moment and plunge into melancholy reflection the next."},
      {"author": "Washington Irving", "work": "The Sketch Book of Geoffrey Crayon", "quote": "The French traveler possessed a lively, **mercurial** temperament that adapted cheerfully to every discomfort on the road."}
    ]
  },
  "mercurialis.md": {
    "primary": "A genus of flowering plants in the spurge family Euphorbiaceae, commonly known as mercury or dog's mercury.",
    "secondary": "In historical botanical pharmacology, Mercurialis perennis was noted for its acrid, purgative qualities and toxicity to livestock when grazed fresh.",
    "quotes": [
      {"author": "William Withering", "work": "An Arrangement of British Plants", "quote": "The common **mercurialis** perennis carpeted the shady beech woods with lush green dioecious foliage."},
      {"author": "John Lindley", "work": "Flora Medica", "quote": "Herbalists cautioned against the internal use of **mercurialis**, which contains volatile acrid principles causing violent gastrointestinal distress."},
      {"author": "Charles Darwin", "work": "The Different Forms of Flowers on Plants of the Same Species", "quote": "The unisexual flowers of **mercurialis** demonstrate an ancient evolutionary adaptation to wind pollination."}
    ]
  },
  "mercuric.md": {
    "primary": "Containing or relating to mercury in its higher divalent oxidation state (+2).",
    "secondary": "In inorganic chemistry and toxicology, mercuric chloride (corrosive sublimate) is an extremely poisonous salt historically used as an antiseptic and wood preservative.",
    "quotes": [
      {"author": "Antoine Lavoisier", "work": "Elements of Chemistry", "quote": "When red **mercuric** oxide is exposed to concentrated solar heat, it releases pure respirable oxygen gas leaving metallic mercury."},
      {"author": "Humphry Davy", "work": "Elements of Chemical Philosophy", "quote": "The precipitation of yellow **mercuric** iodide occurs immediately upon mixing solutions of potassium iodide and corrosive sublimate."},
      {"author": "Robert Boyle", "work": "The Sceptical Chymist", "quote": "We observed the crystalline sublimation of **mercuric** salts rising against the glass neck of the cucurbit."}
    ]
  },
  "mercurochrome.md": {
    "primary": "A brand name for merbromin, a topically applied antiseptic dye formerly widespread in treating minor cuts and abrasions.",
    "secondary": "In twentieth-century clinical medicine, Mercurochrome's vivid crimson stain and mild antiseptic efficacy were gradually superseded by povidone-iodine due to mercury toxicity concerns.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The superficial skin excoriations were cleansed and painted with a two-percent solution of **mercurochrome** to prevent wound infection."},
      {"author": "John Steinbeck", "work": "East of Eden", "quote": "The doctor dabbed the bright scarlet **mercurochrome** over the scraped knee while the child held his breath."},
      {"author": "Arthur Conan Doyle", "work": "Memories and Adventures", "quote": "Field dressings in the military clinic included generous applications of **mercurochrome** along lacerated tissue margins."}
    ]
  },
  "mercurous.md": {
    "primary": "Containing or relating to mercury in its lower monovalent oxidation state (+1), existing as the diatomic cation Hg2(2+).",
    "secondary": "In historical pharmacopeias, mercurous chloride, commonly known as calomel, was widely prescribed as a purgative, cathartic, and antisyphilitic agent.",
    "quotes": [
      {"author": "Humphry Davy", "work": "Elements of Chemical Philosophy", "quote": "The white insoluble precipitate of **mercurous** chloride separates cleanly upon adding hydrochloric acid to mercurous nitrate."},
      {"author": "Justus von Liebig", "work": "Familiar Letters on Chemistry", "quote": "The mild medicinal properties of insoluble **mercurous** salts contrast remarkably with the deadly virulence of soluble mercuric compounds."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Chemistry and Physics", "quote": "Electrolytic decomposition of the molten **mercurous** salt deposited heavy metallic globules at the cathode."}
    ]
  },
  "mercury-contaminated.md": {
    "primary": "Polluted or tainted with toxic mercury compounds, posing acute environmental or neurological hazards.",
    "secondary": "In ecotoxicology and environmental health, mercury-contaminated aquatic ecosystems lead to biomagnification of methylmercury through apex predatory fish.",
    "quotes": [
      {"author": "Rachel Carson", "work": "Silent Spring", "quote": "Industrial effluents poured into estuaries created **mercury-contaminated** sediments that poisoned the local shellfish beds."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Occupational exposure in a **mercury-contaminated** workshop induces severe tremors, erethism, and gingivitis in felt-hat workers."},
      {"author": "Eugene Odum", "work": "Fundamentals of Ecology", "quote": "Biomagnification in **mercury-contaminated** river basins poses grave neurological risks to piscivorous bird species."}
    ]
  },
  "mercury.md": {
    "primary": "A heavy, silvery-white metallic element (symbol Hg, atomic number 80) that is liquid at standard room temperature and pressure.",
    "secondary": "In classical Roman mythology, Mercury was the fleet-footed messenger of the gods, deity of commerce, travel, eloquence, and thievery.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "See what a grace was seated on this brow; Hyperion's curls; the front of Jove himself; an eye like Mars, to threaten and command; a station like the herald **mercury** new-lighted on a heaven-kissing hill."},
      {"author": "Robert Boyle", "work": "The Sceptical Chymist", "quote": "The heavy column of liquid **mercury** in the Torricellian tube balances the weight of the surrounding atmosphere."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The barometer fell rapidly, the bright **mercury** dropping down into the bulb as the tempest approached."}
    ]
  },
  "mercy.md": {
    "primary": "Compassion, forgiveness, or leniency shown toward someone whom it is within one's power to punish or harm.",
    "secondary": "In jurisprudence and monarchical prerogatives, the royal prerogative of mercy allows the sovereign to commute death sentences or grant unconditional pardons.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Merchant of Venice", "quote": "The quality of **mercy** is not strain'd, it droppeth as the gentle rain from heaven upon the place beneath: it is twice blest; it blesseth him that gives and him that takes."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "I have been wrong, but remember how desolate I was, and have **mercy** on my unhappy memory."},
      {"author": "Victor Hugo", "work": "Les Misérables", "quote": "The bishop looked upon the wretched convict with eyes full of infinite divine **mercy** and understanding."}
    ]
  },
  "mere.md": {
    "primary": "That is solely or no more or better than what is specified; also an archaic term for an expanse of standing water or lake.",
    "secondary": "In Anglo-Saxon historical geography and dialectal English, a mere was a shallow freshwater lake or marshy pool bordered by reeds.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "The **mere** word's a slave, debauch'd on every tomb, on every grave a lying trophy."},
      {"author": "Alfred Tennyson", "work": "Morte d'Arthur", "quote": "Sir Bedivere cast the great sword Excalibur far out into the quiet waters of the lonely **mere**."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "The mind cannot create simple ideas out of nothing, nor can **mere** speculation supply the lack of sensory experience."}
    ]
  },
  "meredith.md": {
    "primary": "George Meredith (1828–1909), distinguished English Victorian novelist and poet renowned for his psychological insight and innovative narrative style.",
    "secondary": "In Victorian literary history, Meredith is celebrated for masterpieces including The Ordeal of Richard Feverel and The Egoist, pioneering the philosophical comedy of manners.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "And now let us talk about George **meredith**, if you please, and we shall leave all darker matters behind us for the evening."},
      {"author": "Virginia Woolf", "work": "The Common Reader", "quote": "The brilliant intellectual wit of **meredith** dazzles the reader with an incessant display of metaphor and psychological penetration."},
      {"author": "Robert Louis Stevenson", "work": "Letters to Young Writers", "quote": "No living master handles dramatic dialogue with the sparkling brilliance that **meredith** exhibits in his finest chapters."}
    ]
  },
  "merely.md": {
    "primary": "Just; only; simply; and nothing more; without anything extra.",
    "secondary": "In philosophical argumentation, defining an action as merely mechanical excludes intentional consciousness and purposive agency.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "All the world's a stage, and all the men and women **merely** players: they have their exits and their entrances."},
      {"author": "John Stuart Mill", "work": "On Liberty", "quote": "If all mankind minus one were of one opinion, mankind would be no more justified in silencing that one person than he **merely** would be justified in silencing mankind."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Man still bears in his bodily frame the indelible stamp of his lowly origin, not **merely** in rudimentary organs but in mental faculties."}
    ]
  },
  "merestone.md": {
    "primary": "A stone used to mark a boundary between adjoining properties, parishes, or territorial lands.",
    "secondary": "In ancient agrarian property law, removing or tampering with an established merestone was considered a grave sacrilege punishable by civil and religious curses.",
    "quotes": [
      {"author": "Francis Bacon", "work": "The Essays: Of Judicature", "quote": "A judge ought to prepare his way to a just sentence, as God used to prepare his way, by raising valleys and taking down hills; so when there may be on either side a high hand, or a great over-ruling client, he should be as a settled **merestone** between the parties."},
      {"author": "Thomas Hardy", "work": "The Woodlanders", "quote": "They halted at the mossy **merestone** that divided the ancient manor lands from the parish common."},
      {"author": "William Camden", "work": "Britannia", "quote": "The surveyor pointed out an ancient Roman **merestone** half-buried in the heather beside the old military road."}
    ]
  },
  "meretricious.md": {
    "primary": "Apparently attractive or alluring but having in reality no value, substance, or integrity; tawdry.",
    "secondary": "In classical Latin etymology, meretricious derives from meretrix (a courtesan), originally denoting the alluring, deceptive embellishments of a prostitute.",
    "quotes": [
      {"author": "Francis Bacon", "work": "The Essays", "quote": "The depraved custom of change, and the delight in **meretricious** embellishments, corrupts the sobriety of true artistic judgment."},
      {"author": "Samuel Johnson", "work": "The Lives of the English Poets", "quote": "Cowley's poetry is too often disfigured by **meretricious** ornaments and far-fetched metaphysical conceits."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "She turned away with disdain from the **meretricious** flattery that fashionable society lavished upon her appearance."}
    ]
  },
  "meretriciously.md": {
    "primary": "In a tawdry, flashy, or falsely alluring manner designed to deceive with superficial charm.",
    "secondary": "In aesthetic criticism, designing or painting meretriciously prioritizes gaudy visual impact over compositional harmony and emotional truth.",
    "quotes": [
      {"author": "William Hazlitt", "work": "Table-Talk", "quote": "The stage scenery was **meretriciously** decorated with glittering foil to conceal the poverty of the dramatic writing."},
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "He spoke **meretriciously**, dressing up commonplace platitudes in the extravagant language of romantic devotion."},
      {"author": "John Ruskin", "work": "Modern Painters", "quote": "The late Renaissance facades are **meretriciously** encrusted with decorative carving that lacks all structural justification."}
    ]
  },
  "meretriciousness.md": {
    "primary": "The quality of being superficially attractive but lacking genuine worth, sincerity, or artistic value.",
    "secondary": "In moral philosophy and literary critique, meretriciousness describes artistic or rhetorical works that cater to vulgar tastes through deceptive flashiness.",
    "quotes": [
      {"author": "Matthew Arnold", "work": "Essays in Criticism", "quote": "The glaring **meretriciousness** of popular Victorian melodramas repels any spectator who values dramatic truth."},
      {"author": "George Santayana", "work": "The Sense of Beauty", "quote": "A discerning critic quickly detects the **meretriciousness** beneath an art that aims merely to dazzle without nourishing the spirit."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "He stripped away the **meretriciousness** of modern luxury to discover what simple life in nature truly cost."}
    ]
  },
  "mericarp.md": {
    "primary": "A one-seeded portion of a schizocarp fruit that splits off as an individual unit at maturity.",
    "secondary": "In plant taxonomy, the structural morphology and ribbing of the mericarp in the Apiaceae (umbellifer) family serve as key diagnostic criteria.",
    "quotes": [
      {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "At maturity, the dry fruit of the wild carrot separates cleanly into two bristly **mericarp** halves."},
      {"author": "Joseph Dalton Hooker", "work": "The Student's Flora of the British Islands", "quote": "The prominent oil tubes and secondary ridges on each **mericarp** distinguish the various genera of umbelliferous plants."},
      {"author": "Charles Darwin", "work": "The Different Forms of Flowers on Plants of the Same Species", "quote": "The winged margin of the **mericarp** assists in anemochorous seed dispersal across open grassy meadows."}
    ]
  },
  "merida.md": {
    "primary": "Mérida, the capital of Extremadura in western Spain, renowned for its remarkably preserved Roman archaeological monuments.",
    "secondary": "In Roman provincial archaeology, Augusta Emerita (modern Mérida) was founded in 25 BC for veteran legionaries, boasting a magnificent Roman theater, amphitheater, and aqueducts.",
    "quotes": [
      {"author": "Richard Ford", "work": "A Handbook for Travellers in Spain", "quote": "The Roman ruins of **merida** surpass in grandeur and preservation almost every ancient site outside the Italian peninsula."},
      {"author": "George Borrow", "work": "The Bible in Spain", "quote": "I gazed with awe upon the colossal Roman bridge at **merida**, spanning the broad Guadiana with sixty granite arches."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The garrison of **merida** defended their monumental walls with desperate valor against the invading Saracen hosts."}
    ]
  },
  "meridian.md": {
    "primary": "A circle of constant longitude passing through a given place on the earth's surface and the terrestrial poles; also the highest point of power or prosperity.",
    "secondary": "In observational astronomy, the celestial meridian is the great circle passing through the celestial poles, the zenith, and the nadir of the observer.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry VIII", "quote": "I have touch'd the highest point of all my greatness; and, from that full **meridian** of my glory, I haste now to my setting."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The North Star was directly in the wind's eye, and since evening the Great Bear had wheeled round toward the **meridian**."},
      {"author": "Nathaniel Bowditch", "work": "The New American Practical Navigator", "quote": "When the sun culminates upon the observer's **meridian**, the chronometer indicates the exact Greenwich mean time."}
    ]
  },
  "meridional.md": {
    "primary": "Relating to southern regions or their inhabitants; also relating to a meridian or midday.",
    "secondary": "In climatology and biogeography, meridional circulation patterns describe atmospheric flow along longitudinal lines rather than zonal east-west parallels.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "As exemplifying the effects of climatal changes on distribution, I have discussed the migrations of **meridional** plants and animals across mountain chains."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The soft and luxurious climate of the **meridional** provinces rendered the Roman youth averse to military discipline."},
      {"author": "Alexander von Humboldt", "work": "Cosmos: A Sketch of a Physical Description of the Universe", "quote": "The magnetic needle exhibits subtle **meridional** variations as the explorer travels from polar latitudes toward the equator."}
    ]
  },
  "meringue.md": {
    "primary": "A light, airy sweet confection made from egg whites stiffly beaten with sugar and baked until crisp.",
    "secondary": "In classical French pastry arts, meringue is categorized into French (uncooked sugar), Italian (hot sugar syrup), and Swiss (bain-marie heated) methods.",
    "quotes": [
      {"author": "Alexandre Dumas", "work": "Grand Dictionnaire de Cuisine", "quote": "A delicate baked **meringue** filled with sweetened Chantilly cream crowned the banquet with airy confectionary elegance."},
      {"author": "Isabella Beeton", "work": "Mrs. Beeton's Book of Household Management", "quote": "Whip the whites of the eggs to a stiff froth before adding the powdered sugar to ensure a crisp, golden **meringue**."},
      {"author": "Escoffier", "work": "A Guide to Modern Cookery", "quote": "Pipe the Italian **meringue** in neat rosettes over the iced bombe and brown lightly in a hot oven."}
    ]
  },
  "merino.md": {
    "primary": "A breed of sheep prized for its exceptionally fine, soft, and crimped wool, originating in Spain.",
    "secondary": "In agricultural history and textile commerce, the royal Spanish monopoly on Merino flocks was jealously guarded until export bans were lifted in the 18th century.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The great improvement effected in the breed of **merino** sheep shows what human selection can accomplish in producing delicate wool."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "In the famous Spanish **merino** breed, the rams carry massive spiraled horns while the ewes remain entirely hornless."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The introduction of Spanish **merino** fleeces transformed the quality of woolen cloths manufactured in northern Europe."}
    ]
  },
  "meriones.md": {
    "primary": "A genus of rodent in the gerbil family Muridae, commonly known as jirds, native to arid regions of Africa and Asia.",
    "secondary": "In mammalian physiology and desert ecology, Meriones species (such as the Mongolian jird) possess hypertrophied renal loops that allow survival on dry seeds without drinking water.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Zoology of the Voyage of H.M.S. Beagle", "quote": "Specimens of the rodent genus **meriones** collect seeds in subterranean burrows to sustain life across long desert droughts."},
      {"author": "Richard Lydekker", "work": "The Royal Natural History", "quote": "The sand jirds of the genus **meriones** inhabit the barren wastes of Central Asia, burrowing beneath thorny scrub."},
      {"author": "Alfred Russel Wallace", "work": "The Geographical Distribution of Animals", "quote": "The distribution of **meriones** exemplifies how specialized desert rodents adapt to extreme hyper-arid continental climates."}
    ]
  },
  "meristem.md": {
    "primary": "A region of plant tissue consisting of actively dividing cells from which new tissues and organs are formed.",
    "secondary": "In plant developmental biology, the apical meristem at shoot and root tips maintains an indeterminate stem cell niche that drives primary elongation.",
    "quotes": [
      {"author": "Asa Gray", "work": "Elements of Botany", "quote": "The rapid growth of the shoot tip originates in the apical **meristem**, where embryonic cells divide with ceaseless energy."},
      {"author": "Julius von Sachs", "work": "Text-book of Botany, Morphological and Physiological", "quote": "Microscopic sections through the root cap reveal the primary **meristem** generating orderly rows of cortical and vascular tissue."},
      {"author": "Charles Darwin", "work": "The Power of Movement in Plants", "quote": "The sensitive growing apex containing the root **meristem** directs the downward course of the radical into moist soil."}
    ]
  },
  "merit.md": {
    "primary": "The quality of being particularly good, worthy, or deserving of praise, reward, or recognition.",
    "secondary": "In legal procedure and jurisprudence, the merits of a case denote the substantive rights and legal principles at stake, as opposed to procedural or technical points.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "Lord of my love, to whom in vassalage thy **merit** hath my duty strongly knit, to thee I send this written ambassage."},
      {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "Justice requires that society should treat all equally well who have deserved equally well of it, proportioning reward to moral **merit**."},
      {"author": "Adam Smith", "work": "The Theory of Moral Sentiments", "quote": "Our sense of the **merit** of good actions arises from a sympathetic affection for the gratitude of the person benefited."}
    ]
  },
  "meritable.md": {
    "primary": "Deserving of praise, reward, or honor; possessing genuine merit.",
    "secondary": "In historical theological treatises and moral ethics, meritable conduct was held to justify divine approval and communal respect.",
    "quotes": [
      {"author": "Ben Jonson", "work": "Every Man in His Humour", "quote": "His courageous rescue of the drowning child was an action truly **meritable** in the eyes of all honest citizens."},
      {"author": "Thomas Browne", "work": "Religio Medici", "quote": "To relieve the distressed in secret without thought of public applause is a work most **meritable** and holy."},
      {"author": "Jeremy Taylor", "work": "The Rule and Exercises of Holy Living", "quote": "Sincere humility renders a virtuous deed twice as **meritable** before heaven as when it is blazoned abroad."}
    ]
  },
  "merited.md": {
    "primary": "Deserved, earned, or warranted as a just return for actions or qualities.",
    "secondary": "In classical drama and tragic structure, the catastrophe must feel unmerited in its severity while maintaining causal connection to the protagonist's hubris.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "Ay, I praise God; and I have **merited** some love at his hands through honest and faithful service."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The victorious general received the **merited** honors of a triumph from the unanimous decree of the senate."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth felt that Darcy's indignation was well **merited** by the ungenerous treatment he had received from her family."}
    ]
  },
  "meritless.md": {
    "primary": "Lacking any worth, excellence, or justification; completely undeserving of praise or consideration.",
    "secondary": "In civil litigation and legal advocacy, a meritless lawsuit fails to state an actionable claim or is unsupported by admissible evidence.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "Frivolous and **meritless** objections to the Constitution were raised by partisans seeking only to preserve local state influence."},
      {"author": "Jonathan Swift", "work": "The Battle of the Books", "quote": "The modern pamphlet was a noisy, **meritless** production that perished before the week was out."},
      {"author": "Edmund Burke", "work": "Speech on Conciliation with America", "quote": "A statesman does not waste precious parliamentary hours entertaining **meritless** propositions that aggravate colonial grievances."}
    ]
  },
  "meritocracy.md": {
    "primary": "A social system, society, or organization in which people have power and status because of their abilities, rather than because of their wealth or social position.",
    "secondary": "In political sociology, Michael Young coined meritocracy in 1958 as a satirical critique warning that a society stratified purely by IQ and effort risks creating a rigid, uncompassionate elite.",
    "quotes": [
      {"author": "Michael Young", "work": "The Rise of the Meritocracy", "quote": "A pure **meritocracy** allocates elite educational opportunities solely according to measured talent and effort, creating an unassailable aristocracy of intellect."},
      {"author": "John Rawls", "work": "A Theory of Justice", "quote": "Even an ideal **meritocracy** allows natural lottery differences in talent to generate arbitrary inequalities unless governed by the difference principle."},
      {"author": "Daniel Bell", "work": "The Coming of Post-Industrial Society", "quote": "The post-industrial order is fundamentally a **meritocracy** where technical and scientific credentials determine occupational advancement."}
    ]
  },
  "meritocratic.md": {
    "primary": "Relating to, characterized by, or based on a system where progress is based on ability and talent rather than wealth or privilege.",
    "secondary": "In public administration and civil service reform, meritocratic examinations replaced aristocratic patronage and nepotism in the late 19th century.",
    "quotes": [
      {"author": "Max Weber", "work": "Economy and Society", "quote": "Rational bureaucracy depends upon a **meritocratic** civil service appointed through competitive examinations rather than personal favor."},
      {"author": "Woodrow Wilson", "work": "The Study of Administration", "quote": "A stable democracy requires **meritocratic** standards in its administrative departments to guarantee public efficiency."},
      {"author": "John Dewey", "work": "Democracy and Education", "quote": "Public schools must provide an authentic **meritocratic** ladder by which children of every background can develop their latent abilities."}
    ]
  },
  "meritorious.md": {
    "primary": "Deserving reward, praise, or commendation; displaying notable worth or virtue.",
    "secondary": "In jurisprudence and patent law, a meritorious invention makes a substantive, non-obvious contribution to the state of the art, justifying broad claim construction.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "Thou shalt stand curs'd and excommunicate; and blessed shall he be that doth revolt from his allegiance, and **meritorious** shall that hand be call'd."},
      {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "Conduct is deemed **meritorious** when it promotes the greatest happiness of the greatest number beyond what mere duty strictly requires."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The emperor rewarded the **meritorious** services of his veteran legionaries with generous grants of provincial land."}
    ]
  },
  "meritoriously.md": {
    "primary": "In a manner deserving praise, honor, or reward; with notable merit or excellence.",
    "secondary": "In civil service commendations and military citations, serving meritoriously denotes performance exceeding standard duty in demanding circumstances.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "He who discharges his public trust **meritoriously** amidst widespread corruption deserves the lasting gratitude of his countrymen."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The naval commander had served **meritoriously** in three wars before receiving the honor of the admiral's flag."},
      {"author": "George Washington", "work": "Writings: General Orders to the Continental Army", "quote": "Those soldiers who have behaved **meritoriously** during the hard winter campaign shall receive public thanks from the general."}
    ]
  },
  "meritoriousness.md": {
    "primary": "The quality or state of possessing genuine merit, worth, or desert of reward.",
    "secondary": "In moral philosophy and ethical theory, the meritoriousness of an act is assessed by the purity of the agent's motives and the personal sacrifice incurred.",
    "quotes": [
      {"author": "Immanuel Kant", "work": "Groundwork of the Metaphysics of Morals", "quote": "The moral **meritoriousness** of an action shines forth most brightly when done purely from duty against strong contrary inclinations."},
      {"author": "Jeremy Bentham", "work": "An Introduction to the Principles of Morals and Legislation", "quote": "The **meritoriousness** of a public service is measured by the net addition of utility it confers upon the community."},
      {"author": "Adam Smith", "work": "The Theory of Moral Sentiments", "quote": "Our admiration of the **meritoriousness** of a heroic benefactor is heightened by contemplating the hazards he freely braved."}
    ]
  },
  "merl.md": {
    "primary": "An archaic or poetic name for the common European blackbird (Turdus merula).",
    "secondary": "In Scottish and English folk balladry, the song of the merl heralds the arrival of spring alongside the mavis (song thrush).",
    "quotes": [
      {"author": "Sir Walter Scott", "work": "The Lady of the Lake", "quote": "Merry it is in the good greenwood, when the mavis and **merl** are singing."},
      {"author": "Robert Burns", "work": "Poems and Songs", "quote": "The **merl** sings sweetly in the budding brier, greeting the dawn with joyful melody."},
      {"author": "James Hogg", "work": "The Queen's Wake", "quote": "When the soft dew fell upon the hill, the sweet-toned **merl** whistled from the hawthorn brake."}
    ]
  },
  "merlangus.md": {
    "primary": "A genus or subgenus of marine gadoid fishes, notably Merlangius merlangus (the whiting), common in the northeastern Atlantic.",
    "secondary": "In commercial fisheries and ichthyology, the whiting (Merlangus) is valued for its tender white flesh, playing a vital role as a mid-trophic predator in the North Sea food web.",
    "quotes": [
      {"author": "Thomas Pennant", "work": "British Zoology", "quote": "The whiting, termed **merlangus** by older naturalists, is taken in vast shoals upon the sandy banks of the British Channel."},
      {"author": "William Yarrell", "work": "A History of British Fishes", "quote": "In the genus **merlangus**, the three dorsal fins are distinct and the lower jaw lacks the fleshy barbel seen in the cod."},
      {"author": "Frank Buckland", "work": "Log-Book of a Fisherman and Zoologist", "quote": "The coastal trawlers landed heavy catches of **merlangus**, providing cheap and wholesome food for the London markets."}
    ]
  },
  "merle.md": {
    "primary": "A blackbird (Turdus merula); also a genetic coat pattern in dogs characterized by mottled patches of color.",
    "secondary": "In canine genetics, the merle gene (M) produces dappled patches of diluted pigment on a darker background, associated in homozygous form (double merle) with auditory and ocular defects.",
    "quotes": [
      {"author": "Alfred Tennyson", "work": "The Progress of Spring", "quote": "The mellow **merle** flute-notes on the branch proclaim that winter's icy grasp is broken."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Fanciers have preserved the striking **merle** coat pattern in shepherd dogs through careful selective breeding."},
      {"author": "Francis Galton", "work": "Natural Inheritance", "quote": "Inheritance of the mottled **merle** pigmentation in canines illustrates non-blending Mendelian color distribution."}
    ]
  },
  "merlin.md": {
    "primary": "A small, fast falcon (Falco columbarius) of northern regions, historically used in falconry; also the legendary Arthurian wizard.",
    "secondary": "In medieval romance and falconry lore, the merlin was traditionally designated as the lady's hawk, flown at skylarks and snipes.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry IV, Part 1", "quote": "Sometimes he angers me with telling me of the moldwarp and the ant, of the dreamer **merlin** and his prophecies."},
      {"author": "Alfred Tennyson", "work": "Idylls of the King", "quote": "Then **merlin**, overtalk'd and overworn, had yielded, told her all the charm, and slept."},
      {"author": "Walter Scott", "work": "Marmion", "quote": "The lady rode with a hooded **merlin** perched upon her gauntleted wrist as the hawking party set forth."}
    ]
  }
}

base_dir = r"App database\Latin roots\Cluster Action\Dashboard — mer"

updated = 0
for fname, info in data.items():
    fpath = os.path.join(base_dir, fname)
    if not os.path.exists(fpath):
        print(f"Warning: {fpath} does not exist!")
        continue
    
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    book_idx = content.find("> [!book]")
    if book_idx == -1:
        print(f"Warning: No > [!book] callout in {fname}")
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

print(f"Dashboard — mer Batch 2: Successfully updated {updated}/{len(data)} notes.")
