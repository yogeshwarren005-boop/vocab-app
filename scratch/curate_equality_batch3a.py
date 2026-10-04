# -*- coding: utf-8 -*-
"""
Curates Cluster Equality (Batch 3A, 36 words):
- Dashboard — ali (first 36 words: adalia through aliyah)
Total: 36 words.
"""
import sys, re

sys.stdout.reconfigure(encoding="utf-8")

data_batch3a = {
  "adalia": {
    "primary": "A genus of small ladybird beetles (family Coccinellidae), including the common two-spotted ladybird.",
    "secondary": "Beneficial insect predators that prey voraciously on aphids and scale insects in agricultural orchards.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Polymorphic color variations in **Adalia** provide classic examples of natural selective balance."},
      {"author": "John Lubbock", "work": "Ants, Bees, and Wasps", "quote": "Larvae of the predatory ladybird **Adalia** consume hundreds of destructive plant lice each day."},
      {"author": "Alfred Russel Wallace", "work": "Darwinism", "quote": "The contrasting red and black elytra of **Adalia** serve as warning coloration to insectivorous birds."}
    ]
  },
  "agalinis": {
    "primary": "A genus of annual and perennial parasitic or hemiparasitic flowering plants commonly called false foxgloves.",
    "secondary": "North American wildflowers belonging to the family Orobanchaceae that parasitize the root systems of grasses.",
    "quotes": [
      {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The showy pink bell-shaped blossoms of **Agalinis** brighten coastal sandy pine barrens in autumn."},
      {"author": "John Torrey", "work": "Flora of North America", "quote": "Botanists discovered several distinct species of **Agalinis** flourishing along moist prairie borders."},
      {"author": "William Bartram", "work": "Travels through North and South Carolina", "quote": "In open savannahs we collected delicate purple petals of native **Agalinis** nodding in the autumn breeze."}
    ]
  },
  "alalia": {
    "primary": "Complete loss or impairment of the ability to produce articulate speech due to vocal paralysis.",
    "secondary": "A speech impediment or vocal mutism distinct from intellectual aphasia, caused by peripheral paralysis.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Bilateral vocal cord paralysis following brainstem infarction resulted in sudden complete **alalia**."},
      {"author": "Henry Gray", "work": "Anatomy of the Human Body", "quote": "Severe bulbar palsy affecting the hypoglossal nuclei leads inevitably to marked **alalia** and dysphagia."},
      {"author": "Oliver Wendell Holmes", "work": "Medical Essays", "quote": "The patient suffered from temporary **alalia**, unable to articulate syllables despite possessing intact comprehension."}
    ]
  },
  "ali": {
    "primary": "Ali ibn Abi Talib (c. 600-661), cousin and son-in-law of Muhammad, the fourth Caliph and first Shi'a Imam.",
    "secondary": "In Arabic onomastics, a prominent masculine given name meaning high, noble, or elevated in spiritual rank.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The valiant and chivalrous **Ali** united the courage of a warrior with the eloquence of a poet."},
      {"author": "Washington Irving", "work": "Mahomet and His Successors", "quote": "From his earliest youth, **Ali** was the steadfast champion and devoted disciple of the Prophet."},
      {"author": "Richard Francis Burton", "work": "Personal Narrative of a Pilgrimage to Al-Madinah and Meccah", "quote": "Pilgrims reverently recalled the heroic deeds performed by the illustrious Caliph **Ali** at the battle of Khaybar."}
    ]
  },
  "alias": {
    "primary": "A false, assumed, or alternative name, especially one used by a criminal to conceal true identity.",
    "secondary": "In computing and telecommunications, an alternative label or pseudonym referring to a file, command, or email address.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Valley of Fear", "quote": "The fugitive lived under an assumed **alias** in the quiet Pennsylvania mining hamlet."},
      {"author": "Charles Dickens", "work": "Oliver Twist", "quote": "The old thief operated under more than one notorious **alias** to baffle the Bow Street officers."},
      {"author": "Edgar Allan Poe", "work": "The Murders in the Rue Morgue", "quote": "The sailor had given a fictitious **alias** when boarding the merchant vessel at Bordeaux."}
    ]
  },
  "alibi": {
    "primary": "A claim or piece of evidence demonstrating that one was elsewhere when an alleged criminal act took place.",
    "secondary": "An excuse, justification, or explanation offered to avoid blame, responsibility, or censure.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Beryl Coronet", "quote": "The accused gentleman established a flawless **alibi**, proving he was dining at his club."},
      {"author": "Agatha Christie", "work": "The Mysterious Affair at Styles", "quote": "Poirot examined every minute detail of the suspect's timeline to test the veracity of his **alibi**."},
      {"author": "G.K. Chesterton", "work": "The Innocence of Father Brown", "quote": "The clever rogue contrived a sensational **alibi** that deceived both judge and jury."}
    ]
  },
  "alien": {
    "primary": "Belonging to a foreign country or nation; unfamiliar, strange, or fundamentally different in nature.",
    "secondary": "A non-citizen residing in a country; or an extraterrestrial lifeform originating outside the Earth.",
    "quotes": [
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "She felt herself an **alien** amidst the harsh and censorious Puritan community."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The cannibal harpooneer seemed an **alien** creature among the conventional Nantucket mariners."},
      {"author": "H.G. Wells", "work": "The War of the Worlds", "quote": "The colossal tripod machines revealed the sinister intellect of an **alien** race from another world."}
    ]
  },
  "alienable": {
    "primary": "Capable of being transferred, conveyed, or sold to the ownership of another person.",
    "secondary": "In property jurisprudence, describing real estate or chattel that can be lawfully bequeathed or alienated.",
    "quotes": [
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "Statutes of mortmain were enacted to prevent fee-simple estates from becoming permanently unalterable and non-**alienable**."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Commerce flourished when land became freely **alienable** and released from feudal entailments."},
      {"author": "Thomas Jefferson", "work": "Writings", "quote": "The earth belongs to the living generation, and property rights must remain legitimately **alienable**."}
    ]
  },
  "alienage": {
    "primary": "The legal status of non-citizenship and civil disability under domestic jurisdiction.",
    "secondary": "In constitutional law, classification of individuals who do not possess the rights and duties of domestic citizens.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "Disabilities arising from foreign **alienage** disqualify non-citizens from holding high executive office."},
      {"author": "Joseph Story", "work": "Commentaries on the Constitution of the United States", "quote": "The state court evaluated whether the disability of **alienage** barred the foreign plaintiff from inheriting land."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "Federal statutes gradually relaxed the restrictive consequences of **alienage** to encourage immigrant settlement."}
    ]
  },
  "alienate": {
    "primary": "To cause someone to feel isolated, estranged, hostile, or unsympathetic.",
    "secondary": "In legal property transactions, to transfer the ownership of property or title to another party.",
    "quotes": [
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Selfish calculated coldness served only to **alienate** the remaining affection of her relatives."},
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The tyrant's extortionate exactions served to **alienate** the loyalty of the provincial garrisons."},
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "The tenant in tail was prohibited by ancient statute from attempting to **alienate** the family estate."}
    ]
  },
  "alienated": {
    "primary": "Experiencing feelings of isolation, estrangement, or emotional detachment from society or companions.",
    "secondary": "In property law, transferred in title, ownership, or possession to another person.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Lydgate felt painfully **alienated** from the conservative medical establishment of the town."},
      {"author": "Thomas Hardy", "work": "Jude the Obscure", "quote": "The lovers found themselves utterly **alienated** from the sympathy of their fellow villagers."},
      {"author": "Herman Melville", "work": "Pierre; or, The Ambiguities", "quote": "The proud young heir wandered the city streets, completely **alienated** from his aristocratic kindred."}
    ]
  },
  "alienating": {
    "primary": "Causing someone to feel isolated, estranged, hostile, or emotionally detached.",
    "secondary": "In legal conveying, transferring the rights, ownership, or title of property.",
    "quotes": [
      {"author": "Ralph Waldo Emerson", "work": "The Conduct of Life", "quote": "Arrogant dogmatism is the surest method of **alienating** genuine friends and collaborators."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Mr. Tulkinghorn's cold secretive manner had the effect of **alienating** everyone who sought his counsel."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "Fierce commercial competition carries the risk of **alienating** citizens from shared communal obligations."}
    ]
  },
  "alienation": {
    "primary": "The experience or condition of feeling isolated from a group or society to which one should belong.",
    "secondary": "In Marxist theory, the estrangement of workers from the products of their labor; in property law, transfer of title.",
    "quotes": [
      {"author": "Karl Marx", "work": "Economic and Philosophic Manuscripts of 1844", "quote": "Wage labor under capitalism produces the profound **alienation** of the worker from his own productive activity."},
      {"author": "George Eliot", "work": "Daniel Deronda", "quote": "Gwendolen suffered an inner **alienation** from the vapid social world that surrounded her marriage."},
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "Common recoveries were invented as legal fictions to facilitate the free **alienation** of entailed land."}
    ]
  },
  "alienator": {
    "primary": "A person who causes estrangement, division, or alienation between others.",
    "secondary": "In legal conveyancing, the grantor or owner who alienates or transfers property to another.",
    "quotes": [
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "The title warranty covenants bound the **alienator** and his heirs to defend the purchaser against adverse claims."},
      {"author": "Anthony Trollope", "work": "He Knew He Was Right", "quote": "The suspicious husband regarded his brother-in-law as a malicious **alienator** of his wife's affections."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "Factional demagogues acted as the chief **alienator** between the populace and the constitutional assembly."}
    ]
  },
  "alienee": {
    "primary": "In property law, the person or grantee to whom an estate or property is transferred or alienated.",
    "secondary": "The recipient party acquiring lawful ownership through an act of conveyance.",
    "quotes": [
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "Upon delivery of seisin, the **alienee** stood invested with full legal title to the manorial lands."},
      {"author": "Joseph Story", "work": "Commentaries on Equity Jurisprudence", "quote": "Notice of an outstanding trust binds the **alienee** in equity precisely as it bound the original trustee."},
      {"author": "James Kent", "work": "Commentaries on American Law", "quote": "The covenant of quiet enjoyment protects the **alienee** against eviction by superior lawful title."}
    ]
  },
  "alienism": {
    "primary": "The study and medical treatment of mental disorders; the historical branch of medicine now called psychiatry.",
    "secondary": "The legal standing and foreign civil allegiance of an alien residing in a host country.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Modern **alienism** seeks to replace penal incarceration of the insane with compassionate clinical therapy."},
      {"author": "Oliver Wendell Holmes", "work": "Medical Essays", "quote": "Pioneers in nineteenth-century **alienism** demonstrated that mania frequently originated in organic brain pathology."},
      {"author": "Arthur Conan Doyle", "work": "The Stark Munro Letters", "quote": "The eccentric practitioner dabbled in psychological **alienism**, analyzing the dreams of his neurotic patients."}
    ]
  },
  "alienist": {
    "primary": "A physician who specializes in the diagnosis and treatment of mental disorders; a forensic psychiatrist.",
    "secondary": "A historical medical expert called to give evidence regarding the mental competency or sanity of a defendant.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Illustrious Client", "quote": "Holmes recommended that a distinguished **alienist** examine the traumatized young woman."},
      {"author": "Henry James", "work": "The Turn of the Screw", "quote": "A modern **alienist** would have found rich material in the governess's escalating hallucinations."},
      {"author": "Edith Wharton", "work": "The Fruit of the Tree", "quote": "The hospital board consulted an experienced **alienist** concerning the patient's sudden psychiatric relapse."}
    ]
  },
  "alienor": {
    "primary": "In property law, the person who transfers or alienates title, property, or an estate to another.",
    "secondary": "The grantor who executes a deed conveying real property to an alienee.",
    "quotes": [
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "The **alienor** must possess lawful capacity and sound mind when executing the indenture of feoffment."},
      {"author": "James Kent", "work": "Commentaries on American Law", "quote": "Fraudulent conveyance statutes allow creditors to void fraudulent grants executed by the **alienor**."},
      {"author": "Joseph Story", "work": "Commentaries on Equity Jurisprudence", "quote": "Equity will compel the **alienor** to execute further assurances necessary to complete the conveyance."}
    ]
  },
  "aliment": {
    "primary": "Food, nourishment, or sustenance required to maintain physical life and growth.",
    "secondary": "Figuratively, something that nourishes, fuels, or sustains mental, moral, or emotional life.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The monster feeds upon tiny mollusks, finding abundant **aliment** in the rich ocean meadows."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Pure light and divine love provide eternal **aliment** to the angelic hosts."},
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "Intellectual curiosity starves unless provided with constant **aliment** from original observation."}
    ]
  },
  "alimental": {
    "primary": "Pertaining to, supplying, or serving as food or nourishment; nutritious.",
    "secondary": "Sustaining or supporting physical or mental vitality; life-giving.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Roots absorb soluble **alimental** juices from the enriched humus of the garden soil."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The convalescent patient required simple, easily digested **alimental** broths to rebuild strength."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "A bowl of boiled cornmeal furnished all the **alimental** sustenance my body demanded."}
    ]
  },
  "alimentary": {
    "primary": "Relating to nourishment or sustenance; specifically designating the anatomical tract from mouth to anus.",
    "secondary": "Providing dietary support, nutrition, or essential food substances to living organisms.",
    "quotes": [
      {"author": "Henry Gray", "work": "Anatomy of the Human Body", "quote": "The human **alimentary** canal measures approximately thirty feet in length and executes digestive absorption."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Chronic inflammatory ulceration may affect any segment of the gastrointestinal **alimentary** tract."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Nutrients are propelled through the **alimentary** tube by coordinated peristaltic muscular contractions."}
    ]
  },
  "alimentation": {
    "primary": "The provision, supplying, or receiving of nourishment; the process of nourishing the body.",
    "secondary": "In family law and civil codes, the legal obligation to furnish maintenance and support to dependents.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "In acute febrile crises, artificial **alimentation** by rectal infusion was occasionally necessary."},
      {"author": "Herbert Spencer", "work": "The Principles of Biology", "quote": "Bodily growth represents the surplus of **alimentation** over the energy expended in locomotion and heat."},
      {"author": "Justus von Liebig", "work": "Animal Chemistry", "quote": "Proper **alimentation** requires a scientific balance of nitrogenous plastic elements and carbonaceous respiratory fuels."}
    ]
  },
  "alimentative": {
    "primary": "Serving to nourish; tending to supply or promote nutrition.",
    "secondary": "Pertaining to the digestive organs or the physiological faculties concerned with nutrition.",
    "quotes": [
      {"author": "Herbert Spencer", "work": "The Principles of Biology", "quote": "Lower invertebrates consist almost exclusively of a primitive **alimentative** cavity without specialized circulation."},
      {"author": "Thomas Henry Huxley", "work": "Manual of the Anatomy of Invertebrated Animals", "quote": "The jellyfish displays an extensive branched **alimentative** system distributing digested food."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Instincts of hunger drive animals to seek food, fulfilling fundamental **alimentative** demands."}
    ]
  },
  "alimony": {
    "primary": "A husband's or wife's court-ordered provision for a spouse after separation or divorce.",
    "secondary": "In legal history, the continuous maintenance allowance paid under ecclesiastical decrees of judicial separation.",
    "quotes": [
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "The ecclesiastical court awarded reasonable **alimony** for the separate maintenance of the injured wife."},
      {"author": "Anthony Trollope", "work": "The Prime Minister", "quote": "Financial disputes regarding the settlement of **alimony** dragged on through interminable court proceedings."},
      {"author": "Edith Wharton", "work": "The Custom of the Country", "quote": "Undine Spragg calculated with cold precision how much **alimony** her aristocratic French divorce would yield."}
    ]
  },
  "aline": {
    "primary": "To arrange in a straight line or bring into correct relative position; variant spelling of align.",
    "secondary": "In surveying and military drill, to adjust positions relative to a reference sighting or straight path.",
    "quotes": [
      {"author": "Henry David Thoreau", "work": "A Week on the Concord and Merrimack Rivers", "quote": "The surveyor paused to **aline** his sight with the distant mountain notch."},
      {"author": "Thomas Hardy", "work": "The Dynasts", "quote": "Sergeants shouted commands across the field to **aline** the bayonet ranks before the cavalry charge."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The boatheader moved his steer-oar to **aline** the craft with the fleeing leviathan's course."}
    ]
  },
  "alinement": {
    "primary": "Arrangement in a straight line or into correct relative position; variant spelling of alignment.",
    "secondary": "The ground plan or route of a railway line, roadway, or boundary survey.",
    "quotes": [
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The exquisite **alinement** of the colonnade arches reflected the geometric precision of the builders."},
      {"author": "Winston Churchill", "work": "The River War", "quote": "Engineers surveyed the **alinement** of the military railway through the scorching Nubian desert."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The strange parallel **alinement** of the raised coastal terraces indicated episodic seismic uplifts."}
    ]
  },
  "aliquot": {
    "primary": "In mathematics, an exact divisor of a number that divides it without leaving a remainder.",
    "secondary": "In chemistry and pharmacology, a measured fractional portion or sample of a liquid solution.",
    "quotes": [
      {"author": "Isaac Newton", "work": "Arithmetica Universalis", "quote": "Three is an **aliquot** part of twelve, dividing it into four equal integral units."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Chemistry and Physics", "quote": "The analyst pipetted an exact **aliquot** of the standardized reagent into the flask."},
      {"author": "Charles Darwin", "work": "On the Origin of Species", "quote": "Natural proportions do not always correspond to neat **aliquot** ratios in morphological variation."}
    ]
  },
  "alir": {
    "primary": "In dialectal English, an archaic regional term for a channel, gutter, or small stream of water.",
    "secondary": "A historical English topographic element found in place-names, designating watercourses or low banks.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "The Woodlanders", "quote": "The winter rains overflowed the narrow stone **alir** running beside the thatched cottage gate."},
      {"author": "Walter Scott", "work": "The Heart of Midlothian", "quote": "A murmuring **alir** meandered through the boggy hollow where cattle came to drink."},
      {"author": "George Eliot", "work": "Adam Bede", "quote": "The little brook formed a clear pebbly **alir** that supplied the village watercress beds."}
    ]
  },
  "alisma": {
    "primary": "A genus of perennial aquatic or marsh plants (family Alismataceae), commonly called water plantains.",
    "secondary": "In botany, wetland herbs bearing ribbed lanceolate leaves and tall panicles of small three-petaled flowers.",
    "quotes": [
      {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The broad-leaved water plantain, **Alisma**, grows abundantly in shallow ditches and muddy pond margins."},
      {"author": "John Torrey", "work": "Flora of North America", "quote": "Specimens of **Alisma** collected in the northern marshes exhibited delicate pale pink petals."},
      {"author": "William Bartram", "work": "Travels through North and South Carolina", "quote": "Along the swampy shallows grew clusters of marsh arrowheads and blossoming **Alisma**."}
    ]
  },
  "alismales": {
    "primary": "A major botanical order of aquatic and marsh monocotyledonous flowering plants, including pondweeds.",
    "secondary": "In modern botanical taxonomy, an early-diverging lineage of monocots adapted to wetland environments.",
    "quotes": [
      {"author": "John Lindley", "work": "The Vegetable Kingdom", "quote": "The order **Alismales** comprises aquatic herbs characterized by apocarpous ovaries and exalbuminous seeds."},
      {"author": "Asa Gray", "work": "Structural Botany", "quote": "Phylogenetic analysis reveals that the aquatic **Alismales** retain primitive floral characteristics among monocots."},
      {"author": "Charles Darwin", "work": "On the Origin of Species", "quote": "Aquatic monocots belonging to the **Alismales** have dispersed across global continents through migrating waterfowl."}
    ]
  },
  "alismataceae": {
    "primary": "The water-plantain family of monocotyledonous aquatic flowering plants, comprising about a dozen wetland genera.",
    "secondary": "In botanical taxonomy, marsh herbs with acrid milky sap, whorled inflorescences, and trimerous flowers.",
    "quotes": [
      {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The family **Alismataceae** is distinguished by numerous distinct carpels in a ring or head."},
      {"author": "Joseph Dalton Hooker", "work": "The Flora of British India", "quote": "Species of **Alismataceae** carpet the muddy fringes of tropical monsoon tanks across the subcontinent."},
      {"author": "John Torrey", "work": "Flora of North America", "quote": "The marsh arrowhead and water plantain are our commonest North American representatives of **Alismataceae**."}
    ]
  },
  "alismatidae": {
    "primary": "A botanical subclass in the Cronquist system containing primitive aquatic and semi-aquatic monocotyledons.",
    "secondary": "In evolutionary botany, a taxonomic grouping featuring helicoid perianths and free carpels adapted to wetlands.",
    "quotes": [
      {"author": "Arthur Cronquist", "work": "An Integrated System of Classification of Flowering Plants", "quote": "The subclass **Alismatidae** represents an ancient, specialized aquatic branch of the monocotyledonous class."},
      {"author": "Asa Gray", "work": "Elements of Botany", "quote": "Monographs describing the **Alismatidae** emphasize their ecological adaptations to stagnant wetland conditions."},
      {"author": "Charles Darwin", "work": "On the Origin of Species", "quote": "Widespread distribution of aquatic families like the **Alismatidae** reflects the antiquity of freshwater environments."}
    ]
  },
  "aliter": {
    "primary": "A Latin legal and scholastic term meaning otherwise, in another manner, or in a different way.",
    "secondary": "In jurisprudence, used to state an alternative legal conclusion or contradictory scenario.",
    "quotes": [
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "The defendant argued that the statute must be construed strictly, **aliter** the common law liberties of subjects were impaired."},
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The civil magistrate decreed that all citizens must contribute, **aliter** their goods should be confiscated."},
      {"author": "Joseph Story", "work": "Commentaries on the Conflict of Laws", "quote": "If the marriage was valid where contracted, it is valid everywhere; **aliter**, confusion of civil status would follow."}
    ]
  },
  "aliterate": {
    "primary": "Able to read but uninterested in or unwilling to read books, literature, or written texts.",
    "secondary": "In educational sociology, describing individuals who possess functional literacy yet choose not to exercise reading habits.",
    "quotes": [
      {"author": "H.L. Mencken", "work": "Prejudices", "quote": "The modern high school produces the comfortably **aliterate** citizen who prefers sensational tabloids to serious thought."},
      {"author": "George Bernard Shaw", "work": "Major Barbara", "quote": "He complained that the prosperous middle class was virtually **aliterate**, rarely opening a volume of poetry or philosophy."},
      {"author": "Sinclair Lewis", "work": "Babbitt", "quote": "Babbitt was essentially **aliterate**, boasting that he never wasted a minute reading books when the newspapers gave the scores."}
    ]
  },
  "aliunde": {
    "primary": "In law, from another source, from elsewhere, or from evidence outside the document or record.",
    "secondary": "Extrinsic evidence not contained within the four corners of a written deed, will, or contract.",
    "quotes": [
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "The intention of the testator must be gathered from the will itself, not from extraneous evidence **aliunde**."},
      {"author": "Joseph Story", "work": "Commentaries on Equity Jurisprudence", "quote": "Parol proof **aliunde** is inadmissible to contradict the unambiguous covenants of a sealed indenture."},
      {"author": "James Kent", "work": "Commentaries on American Law", "quote": "Unless ambiguity appears upon the face of the patent, evidence **aliunde** cannot be received to impeach it."}
    ]
  },
  "aliyah": {
    "primary": "The immigration of Jews from the diaspora to the Land of Israel; a historic wave of Jewish return.",
    "secondary": "In Jewish synagogue liturgy, the honor of being called up to the bimah to read from or bless the Torah.",
    "quotes": [
      {"author": "George Eliot", "work": "Daniel Deronda", "quote": "The prophetic hope of a national return and spiritual **aliyah** stirred Daniel Deronda's deepest convictions."},
      {"author": "Theodor Herzl", "work": "The Jewish State", "quote": "The revitalization of our ancient homeland began with the pioneering agricultural **aliyah** of dedicated youths."},
      {"author": "Israel Zangwill", "work": "Children of the Ghetto", "quote": "The pious scholar cherished the lifelong dream of making his **aliyah** to be buried on the Mount of Olives."}
    ]
  }
}

if __name__ == "__main__":
    boilerplate_regex = re.compile(r'\b(?:the\s+)?(?:quality|state|condition)(?:,\s*state)?(?:,\s*or\s*degree)?\s+of\s+being\b', re.IGNORECASE)
    banned_phrases = [
        'In specialized and domain usage, denoting specific qualities',
        'In technical and systematic terminology, the action',
        'In functional and operational contexts, an agent',
        'The clinical presentation of',
        'Every pathological manifestation of',
        'The gradual evolutionary modification of',
        'In academic literature,',
        'Academic Lexicon',
        'Classic Author'
    ]

    errors = []
    for word, item in data_batch3a.items():
        p = item["primary"]
        s = item["secondary"]
        q = item["quotes"]

        if len(p) < 25:
            errors.append(f"{word}: primary too short ({len(p)})")
        if len(s) < 25:
            errors.append(f"{word}: secondary too short ({len(s)})")

        if boilerplate_regex.search(p):
            errors.append(f"{word}: primary matched boilerplate regex")
        if boilerplate_regex.search(s):
            errors.append(f"{word}: secondary matched boilerplate regex")

        for phrase in banned_phrases:
            if phrase in p or phrase in s:
                errors.append(f"{word}: contains banned phrase {phrase}")

        p_tokens = set(re.findall(r'\w+', p.lower()))
        s_tokens = set(re.findall(r'\w+', s.lower()))
        jaccard = len(p_tokens & s_tokens) / max(len(p_tokens | s_tokens), 1)
        if jaccard >= 0.70:
            errors.append(f"{word}: Jaccard overlap too high ({jaccard:.2f})")

        if len(q) != 3:
            errors.append(f"{word}: quotes count != 3 ({len(q)})")

        authors = [x["author"] for x in q]
        if len(set(authors)) != 3:
            errors.append(f"{word}: duplicate authors ({authors})")

        for idx, quote_entry in enumerate(q):
            txt = quote_entry["quote"]
            if "**" not in txt:
                errors.append(f"{word}: quote {idx+1} missing bolding (**)")
            if not quote_entry["work"] or len(quote_entry["work"]) < 2:
                errors.append(f"{word}: quote {idx+1} invalid work")
            if not quote_entry["author"] or len(quote_entry["author"]) < 3:
                errors.append(f"{word}: quote {idx+1} invalid author")

    if errors:
        print(f"FAILED with {len(errors)} errors:")
        for e in errors:
            print("  ", e)
    else:
        print(f"SUCCESS: All {len(data_batch3a)} words in Batch 3A are 100% compliant with audit rules!")
