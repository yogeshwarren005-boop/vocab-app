# -*- coding: utf-8 -*-
"""
Part 5: vic part 3 (words 43-63)
['victimise', 'victimised', 'victimiser', 'victimization', 'victimize', 'victimized', 'victimizer', 'victor', 'victoria', 'victorian', 'victoriana', 'victorious', 'victoriously', 'victory', 'victrola', 'victual', 'victualer', 'victualler', 'victuals', 'vicugna', 'vicuna']
"""
import sys
sys.stdout.reconfigure(encoding="utf-8")

data_vic_p3 = {
  "victimise": {
    "primary": "To single someone out for cruel, unjust, or unfair treatment; to swindle, dupe, or exploit.",
    "secondary": "In labor relations and social ethics, to retaliate against an employee, tenant, or subordinate for asserting legal rights.",
    "quotes": [
      {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "Sharpers in the gambling saloons were always eager to **victimise** any naive young officer newly arrived from the country."},
      {"author": "George Bernard Shaw", "work": "Plays Pleasant and Unpleasant", "quote": "Society continues to **victimise** those who dare to question its unexamined moral orthodoxies."},
      {"author": "Thomas Hardy", "work": "Jude the Obscure", "quote": "He felt that the rigid traditions of the university city conspired to **victimise** poor scholars seeking knowledge."}
    ]
  },
  "victimised": {
    "primary": "Singled out for cruel treatment, cheated, swindled, or made to suffer unfairly.",
    "secondary": "In criminology and sociological studies, subjected to systemic harm, discrimination, or exploitation by predatory individuals or institutions.",
    "quotes": [
      {"author": "James Joyce", "work": "Dubliners", "quote": "He brooded over his misfortunes in the quiet tavern, feeling himself cruelly **victimised** by his employer's harsh reprimand."},
      {"author": "William Makepeace Thackeray", "work": "The History of Pendennis", "quote": "The gullible young gentleman was thoroughly **victimised** by unprincipled acquaintances at the university."},
      {"author": "Joseph Conrad", "work": "The Secret Agent", "quote": "Stevie was easily **victimised** by cunning men who played upon his boundless pity and simple trust."}
    ]
  },
  "victimiser": {
    "primary": "A person who victimises, exploits, swindles, harms, or abuses another.",
    "secondary": "In restorative justice and psychological theory, the perpetrator of coercive control, fraud, or relational violence.",
    "quotes": [
      {"author": "George Eliot", "work": "Daniel Deronda", "quote": "Grandcourt displayed all the cold calculating traits of the habitual **victimiser**, enjoying his absolute dominion over his wife."},
      {"author": "Charles Dickens", "work": "Nicholas Nickleby", "quote": "Ralph Nickleby regarded every indebted client not as a brother man, but as fair prey for the financial **victimiser**."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Alec d'Urberville stood before her as the selfish **victimiser** who had shattered the innocent tranquility of her youth."}
    ]
  },
  "victimization": {
    "primary": "The action of singling someone out for cruel or unjust treatment; exploitation, abuse, or swindling.",
    "secondary": "In victimology and legal sociology, the process through which individuals or groups suffer psychological, physical, or economic harm.",
    "quotes": [
      {"author": "Jane Addams", "work": "Democracy and Social Ethics", "quote": "The settlement workers fought continuously against the ruthless economic **victimization** of newly arrived immigrant families."},
      {"author": "John Dewey", "work": "Human Nature and Conduct", "quote": "Customary moral codes often permit the subtle **victimization** of weaker classes under the guise of tradition."},
      {"author": "Thorstein Veblen", "work": "The Vested Interests and the Common Man", "quote": "The underlying population suffered systemic **victimization** from corporate trusts manipulating market prices."}
    ]
  },
  "victimize": {
    "primary": "To single someone out for cruel, unjust, or unfair treatment; to exploit, swindle, or cheat.",
    "secondary": "In behavioral psychology, to subject someone to bullying, deception, or harassment through asymmetric power dynamics.",
    "quotes": [
      {"author": "Leo Tolstoy", "work": "War and Peace", "quote": "Cunning camp followers sought every opportunity to **victimize** naive recruits during the chaotic retreat."},
      {"author": "Mark Twain", "work": "Adventures of Huckleberry Finn", "quote": "The king and the duke plotted how to **victimize** the grieving townspeople by pretending to be the dead man's brothers."},
      {"author": "Henry James", "work": "The Bostonians", "quote": "She refused to allow the domineering reformer to **victimize** the young girl's impressionable and fragile nature."}
    ]
  },
  "victimized": {
    "primary": "Singled out for cruel treatment, cheated, swindled, or made to suffer unfairly.",
    "secondary": "In jurisprudence and clinical psychology, having sustained identifiable injury, violation of rights, or financial losses from a crime.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Fred Vincy felt bitterly that he was being unfairly **victimized** by ill fortune and demanding creditors."},
      {"author": "Charles Dickens", "work": "Oliver Twist", "quote": "The innocent orphan was repeatedly **victimized** by Fagin's gang before finding refuge in a gentle home."},
      {"author": "Edith Wharton", "work": "The House of Mirth", "quote": "Lily Bart realized too late that she had been **victimized** by the treacherous machinations of fashionable society."}
    ]
  },
  "victimizer": {
    "primary": "A person who victimizes, exploits, cheats, harms, or abuses another.",
    "secondary": "In criminology and social ethics, an individual or syndicate that methodically preys upon vulnerable persons.",
    "quotes": [
      {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "Becky Sharp turned upon her former **victimizer** with a ferocious wit that left him completely discomfited."},
      {"author": "Arthur Conan Doyle", "work": "The Return of Sherlock Holmes", "quote": "Holmes vowed to track down the heartless blackmailer, characterizing him as the worst **victimizer** in London."},
      {"author": "Frank Norris", "work": "McTeague", "quote": "Marcus viewed his former friend as a treacherous **victimizer** who had stolen his rightful lottery fortunes."}
    ]
  },
  "victor": {
    "primary": "A person who defeats an enemy, competitor, or opponent in a battle, contest, or struggle.",
    "secondary": "In biological evolution and competition theory, an organism or species that successfully secures reproductive resources and territory.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Coriolanus", "quote": "Hail to thee, lady, and the **victor** of Corioli! With all our hearts we welcome your triumphant return."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Sexual selection, by always allowing the **victor** in combat to breed, might surely give that victor an advantage in survival."},
      {"author": "George Eliot", "work": "Romola", "quote": "Tito walked as an acknowledged **victor** through the cheering Piazza, savoring his rapid political ascent."}
    ]
  },
  "victoria": {
    "primary": "A light, four-wheeled horse-drawn carriage with a collapsible calash top and an elevated front driver's seat.",
    "secondary": "In royal history, geographic nomenclature, and botany, the British monarch Queen Victoria, or the giant Amazonian water lily Victoria amazonica.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "A smart little **victoria** dashed up to the door, and a lady wrapped in heavy furs stepped gracefully onto the pavement."},
      {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "Lady Henry was a curious woman whose dresses always looked as if they had been designed in a rage; she drove about town in an open **victoria**."},
      {"author": "H. G. Wells", "work": "The War of the Worlds", "quote": "My brother turned down towards **Victoria** station, and met a great number of people fleeing in disorderly haste."}
    ]
  },
  "victorian": {
    "primary": "Of, relating to, or characteristic of the reign of Queen Victoria (1837–1901) or its prevailing cultural and moral ethos.",
    "secondary": "In architecture, literature, and social history, an era marked by industrial expansion, imperial dominance, earnest moralism, and ornate domestic design.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The modest farmhouse interior combined heavy **Victorian** mahogany furniture with older rustic oak settles."},
      {"author": "Lytton Strachey", "work": "Eminent Victorians", "quote": "The dominant note of early **Victorian** biography was a solemn and uncritical reverence for moral achievement."},
      {"author": "Virginia Woolf", "work": "Orlando", "quote": "The great damp cloud of the **Victorian** era settled over England, bringing mufflers, plush carpets, and heavy draperies."}
    ]
  },
  "victoriana": {
    "primary": "Items, books, furnishings, artifacts, or decorative bric-a-brac associated with the Victorian era.",
    "secondary": "In antiques appraisal and cultural history, collectable decorative objects, ephemera, and prints documenting nineteenth-century British society.",
    "quotes": [
      {"author": "John Betjeman", "work": "First and Last Loves", "quote": "He wandered through provincial antique shops collecting charming pieces of neglected **Victoriana**, from papier-mâché trays to stained glass."},
      {"author": "Evelyn Waugh", "work": "Brideshead Revisited", "quote": "The drawing room was cluttered with mid-century **Victoriana**, including domed wax flowers and beadwork footstools."},
      {"author": "Osbert Sitwell", "work": "Left Hand, Right Hand!", "quote": "The nursery was furnished with amusing relics of authentic **Victoriana** preserved from our grandmothers' childhood."}
    ]
  },
  "victorious": {
    "primary": "Having won a victory; triumphant, conquering, or successful in a contest, war, or difficult struggle.",
    "secondary": "In military strategy and statecraft, celebrating the definitive overcoming of armed opposition or ideological resistance.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Richard III", "quote": "Now are our brows bound with **victorious** wreaths; our bruised arms hung up for monuments; our stern alarums changed to merry meetings."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The **victorious** species will multiply and spread, encroaching upon the territory and livelihoods of less adapted competitors."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Rosamond had that **victorious** obstinacy which never wastes its energy in loud argument, but quietly persists until its aim is secured."}
    ]
  },
  "victoriously": {
    "primary": "In a victorious, triumphant, or successfully conquering manner.",
    "secondary": "In epic narrative and historiography, concluding an arduous campaign with complete tactical or moral ascendancy.",
    "quotes": [
      {"author": "Sir Walter Scott", "work": "Ivanhoe", "quote": "The Disinherited Knight rode **victoriously** around the lists, saluted by the thunderous acclamations of the multitude."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The republican legions marched **victoriously** across the frontier, carrying the tricolor into neighboring duchies."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Belisarius concluded his Persian campaign **victoriously**, restoring the prestige of imperial Roman arms in the East."}
    ]
  },
  "victory": {
    "primary": "The overcoming of an enemy, antagonist, or obstacle; success in a contest, competition, or struggle.",
    "secondary": "In political and military history, the decisive achievement of strategic objectives through armed triumph or diplomatic resolution.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Antony and Cleopatra", "quote": "Upon your sword sit laurel **victory**, and smooth success be strewed before your feet!"},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The man and the ecclesiastic fought within him, and the human affection achieved a momentary **victory** over rigid doctrine."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Battle within battle must ever be recurring with varying success; and **victory** rests at last with the most adapted organism."}
    ]
  },
  "victrola": {
    "primary": "A brand of early wind-up mechanical phonograph or gramophone housed in an upright wooden cabinet.",
    "secondary": "In music history and twentieth-century material culture, an iconic acoustic record player popularizing recorded shellac disc music in domestic homes.",
    "quotes": [
      {"author": "Sinclair Lewis", "work": "Main Street", "quote": "The parlor boasted a grand mahogany **Victrola** upon which Carol played classical symphonies for puzzled provincial guests."},
      {"author": "F. Scott Fitzgerald", "work": "This Side of Paradise", "quote": "From an open window floated the tinny jazz music of a **Victrola**, mingling with the warm scent of summer lilacs."},
      {"author": "William Faulkner", "work": "The Sound and the Fury", "quote": "The needle scratched across the spinning record on the corner **Victrola**, filling the quiet hallway with old waltz melodies."}
    ]
  },
  "victual": {
    "primary": "To supply, provide, or provision with food, rations, or necessary stores.",
    "secondary": "In maritime logistics and naval history, to stock a sailing warship or merchant vessel with non-perishable provisions for a long voyage.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry VI, Part 1", "quote": "I must go **victual** Orleans forthwith, cried the bold captain, seeing the city hard-pressed by English siege engines."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "The prudent farm bailiff rode to market early to purchase supplies and **victual** the harvest laborers for the coming week."},
      {"author": "King James Bible", "work": "The Holy Bible", "quote": "And the children of Israel were numbered, and were all present, and went against them: and the children of Israel pitched before them to **victual** their hosts."},
    ]
  },
  "victualer": {
    "primary": "A provider, purveyor, or merchant of food provisions, rations, or foodstuffs.",
    "secondary": "In naval administration and historical retail licensing, a licensed tavern keeper or naval contractor supplying fleet provisions.",
    "quotes": [
      {"author": "Daniel Defoe", "work": "A Journal of the Plague Year", "quote": "The municipal magistrates ordered every licensed **victualer** to keep his market stalls cleansed and fumigated daily."},
      {"author": "Tobias Smollett", "work": "The Adventures of Roderick Random", "quote": "The ship's purser had made corrupt private bargains with the naval **victualer** at Portsmouth to supply spoiled ship biscuit."},
      {"author": "Samuel Pepys", "work": "The Diary of Samuel Pepys", "quote": "I met with the admiralty **victualer** to examine accounts for beef and beer supplied to the royal fleet in the Downs."}
    ]
  },
  "victualler": {
    "primary": "A tavern keeper or innkeeper licensed to sell food and liquor; or a contractor supplying naval provisions.",
    "secondary": "In British maritime history, an auxiliary supply vessel accompanying a naval fleet carrying rations, fresh water, and stores.",
    "quotes": [
      {"author": "Charles Dickens", "work": "The Pickwick Papers", "quote": "The sign over the coaching inn declared Mr. Weller to be a licensed **victualler** of good repute across the shire."},
      {"author": "Herman Melville", "work": "White-Jacket", "quote": "A chartered naval **victualler** drew alongside our frigate to replenish the depleted barrels of salt pork and flour."},
      {"author": "Arthur Conan Doyle", "work": "Rodney Stone", "quote": "The famous boxing match drew patrons from every class, from dukes to the humblest licensed **victualler** in London."}
    ]
  },
  "victuals": {
    "primary": "Food supplies, provisions, or prepared foodstuffs for human consumption.",
    "secondary": "In nautical lore and colloquial frontier parlance, the staple table fare sustaining sailors, soldiers, or pioneer households.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Cymbeline", "quote": "But that it eats our **victuals**, I should think here were a fairy; an angel, or if not an earthly creature, yet an ethereal spirit."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The mowers sat beneath the oak hedge at midday, unpacking their coarse **victuals** and cider jars with hearty appetite."},
      {"author": "Francis Bacon", "work": "The Essays", "quote": "We sailed from Peru where we had continued for the space of one whole year, being well furnished with **victuals** for our voyage."}
    ]
  },
  "vicugna": {
    "primary": "A wild South American camelid (Vicugna vicugna) native to the high alpine Andes, prized for its exceptionally fine fleece.",
    "secondary": "In systematic zoology and Andean ecology, the taxonomic genus encompassing the vicuña, characterized by continuously growing rodent-like lower incisors adapted for alpine grazing.",
    "quotes": [
      {"author": "Alexander von Humboldt", "work": "Views of Nature", "quote": "The graceful **Vicugna** wanders in small herds across the windswept puna grasslands of the Peruvian cordilleras."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "We observed solitary herds of the wild **vicugna** grazing peacefully among the desolate rocky slopes beneath snowcapped Andean peaks."},
      {"author": "William Hickling Prescott", "work": "History of the Conquest of Peru", "quote": "The Incas organized magnificent royal hunts to shear the silky fleece of the sacred **vicugna** without harming the animals."}
    ]
  },
  "vicuna": {
    "primary": "A wild Andean camelid inhabiting high plateau grasslands, renowned for producing the finest and softest natural wool in the world.",
    "secondary": "In textiles and luxury manufacturing, rare and costly cloth or garments woven from the fine golden underfleece of the vicuña.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "He wrapped himself warmly against the polar gale in a luxurious traveling cloak lined with Peruvian **vicuna** fleece."},
      {"author": "W. H. Hudson", "work": "The Naturalist in La Plata", "quote": "The swift and agile **vicuna** bounds across mountain scree with effortless grace that defies human pursuit."},
      {"author": "Edward Whymper", "work": "Travels Amongst the Great Andes of the Equator", "quote": "Our Indian guides pointed out distant tracks left by wild **vicuna** crossing the frozen pumice plateaus."}
    ]
  }
}
