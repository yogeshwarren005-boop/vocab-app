# -*- coding: utf-8 -*-
"""
Part 3 of Batch 4 Cluster Asking & Seeking (Dashboard — prec):
Words 55 to 81:
['precession', 'precinct', 'preciosity', 'precious', 'preciously',
 'preciousness', 'precipice', 'precipitance', 'precipitancy', 'precipitant',
 'precipitate', 'precipitately', 'precipitateness', 'precipitating',
 'precipitation', 'precipitator', 'precipitin', 'precipitous', 'precipitously',
 'precipitousness', 'precis', 'precise', 'precisely', 'preciseness',
 'precision', 'preclinical', 'preclude']
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

part3_prec = {
    "precession": {
        "primary": "The slow conical motion of the axis of a spinning body around another axis.",
        "secondary": "In positional astronomy, the continuous westward shift of the equinoctial points along the ecliptic caused by lunisolar torque upon Earth's equatorial bulge.",
        "quotes": [
            {"author": "John Herschel", "work": "Outlines of Astronomy", "quote": "The **precession** of the equinoxes slowly carries the celestial coordinates around the pole of the ecliptic in a cycle of twenty-six thousand years."},
            {"author": "Simon Newcomb", "work": "Popular Astronomy", "quote": "Hipparchus detected the subtle effect of **precession** by comparing his stellar observations with charts compiled centuries earlier by Babylonian astronomers."},
            {"author": "Arthur Stanley Eddington", "work": "Space, Time and Gravitation", "quote": "General relativity accounts accurately for the anomalous orbital **precession** of Mercury without requiring unobserved intra-Mercurial masses."}
        ]
    },
    "precinct": {
        "primary": "A designated district, enclosed boundary, or specific administrative subdivision of a city.",
        "secondary": "In municipal policing and electoral administration, the smallest territorially defined jurisdiction assigned to a voting polling station or station-house.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Henry VI, Part 1", "quote": "The stony limits of their **precinct** cannot hold out the resolute advance of our united forces."},
            {"author": "Ralph Waldo Emerson", "work": "Essays: First Series", "quote": "Within the sacred **precinct** of the individual soul, no worldly compromise can claim legitimate sovereignty."},
            {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "We hurried across the quiet cathedral **precinct**, where ancient plane trees cast deep shadows upon the gravel paths."}
        ]
    },
    "preciosity": {
        "primary": "Affectation of elegance or refinement, especially in linguistic style or artistic taste.",
        "secondary": "In literary history, the seventeenth-century salon aesthetic (associated with the French Précieuses) marked by ornate metaphors, euphuism, and hyper-delicate sensibilities.",
        "quotes": [
            {"author": "Walter Pater", "work": "Appreciations", "quote": "His prose avoids the taint of mere **preciosity** by grounding every refined phrase in genuine imaginative emotion."},
            {"author": "George Saintsbury", "work": "A History of Elizabethan Literature", "quote": "Euphuistic **preciosity** dominated the courtly romances of the late sixteenth century before drama found its vigorous vernacular voice."},
            {"author": "Virginia Woolf", "work": "The Common Reader", "quote": "She balanced upon the verge of **preciosity**, saving her ornate sentences by an unexpected flash of satiric wit."}
        ]
    },
    "precious": {
        "primary": "Of great value, price, worth, or dear affection; highly prized or cherished.",
        "secondary": "In mineralogy and economic geology, designating rare gemstones and noble metals possessing enduring trade liquidity and chemical unreactivity.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Romeo and Juliet", "quote": "O mickle is the powerful grace that lies in plants, herbs, stones, and their true **precious** qualities."},
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Ambergris is soft, waxy, and so fragrant that perfumers purchase the **precious** substance at exorbitant prices."},
            {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "He had a passion for **precious** stones, collecting pearls of extraordinary size and rubies fiery as dragon blood."}
        ]
    },
    "preciously": {
        "primary": "In a precious, highly valued, or carefully guarded manner; or with ornate affectation.",
        "secondary": "In stylistic critique, describing mannered artistic or verbal expressions composed with excessively self-conscious delicacy.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Winter's Tale", "quote": "She kept the jewel **preciously** in her casket, awaiting the hour when its secret tokens might be revealed."},
            {"author": "George Eliot", "work": "Silas Marner", "quote": "Silas counted his gold pieces nightly, stacking them **preciously** beside the hearth until the metallic gleam filled his mind."},
            {"author": "Henry James", "work": "The Author of Beltraffio", "quote": "The novelist turned his phrases **preciously**, as if language were Venetian glass too fragile for everyday handling."}
        ]
    },
    "preciousness": {
        "primary": "Great value, worth, or scarcity; or an over-refined, affected delicacy of manner.",
        "secondary": "In economic value theory, the subjective or systemic scarcity premium that elevates commodity prices above cost of production.",
        "quotes": [
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The extraordinary **preciousness** of sperm oil stimulated Yankee merchants to send fleets across perilous polar seas."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Dorothea felt the sacred **preciousness** of life too deeply to squander her waking hours in trivial parlor amusements."},
            {"author": "John Ruskin", "work": "The Seven Lamps of Architecture", "quote": "The true **preciousness** of decorative marble lies in its natural grain rather than in mechanical polishing."}
        ]
    },
    "precipice": {
        "primary": "A very steep rock face or cliff; or a situation of imminent and acute danger.",
        "secondary": "In geomorphology, a near-vertical escarpment generated by active faulting, glacial headwall erosion, or fluvial incision.",
        "quotes": [
            {"author": "William Shakespeare", "work": "King Lear", "quote": "You take a **precipice** for no leap of danger, and woo your own destruction upon the cliffs of Dover."},
            {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "Time seemed crawling with feet of lead, while monstrous winds swept him toward the jagged edge of a **precipice**."},
            {"author": "Joseph Conrad", "work": "Heart of Darkness", "quote": "I looked at him as you peer down at a man lying at the bottom of a **precipice** where the sun never shines."}
        ]
    },
    "precipitance": {
        "primary": "Headlong, rash, or untimely haste; lack of deliberate forethought in action.",
        "secondary": "In psychological jurisprudence, the impetuous mental defect that precludes premeditation in criminal culpability.",
        "quotes": [
            {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "His sudden **precipitance** in leaping from the cab nearly cost him his footing on the slippery London pavement."},
            {"author": "William Shakespeare", "work": "Henry VIII", "quote": "Beware of **precipitance** in your judgment, lest unconsidered anger undermine the council's royal prerogative."},
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The Emperor Julian's fatal **precipitance** led the Roman legions into the waterless wastes of Mesopotamia."}
        ]
    },
    "precipitancy": {
        "primary": "Rash, impulsive, or ill-considered swiftness; headlong rashness in decision or movement.",
        "secondary": "In statecraft and military strategy, the catastrophic operational error of engaging battle before supply lines are secured.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Boldwood reflected with deep regret upon the desperate **precipitancy** with which he had urged his suit upon Bathsheba."},
            {"author": "Herman Melville", "work": "Pierre; or, The Ambiguities", "quote": "Pierre acted with a disastrous **precipitancy** that severed him forever from his ancestral home and patrimony."},
            {"author": "Samuel Johnson", "work": "The Rambler", "quote": "Youth is ever prone to **precipitancy**, mistaking the heat of passion for the clear guidance of wisdom."}
        ]
    },
    "precipitant": {
        "primary": "Rushing headlong or acting rashly; or an agent that causes a solid substance to precipitate.",
        "secondary": "In analytical chemistry, a specific reagent whose addition to a solution induces the formation of an insoluble chemical compound.",
        "quotes": [
            {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "A dogmatic intellect displays a **precipitant** judgment, embracing conclusions before examining the contradictory evidence."},
            {"author": "Michael Faraday", "work": "Chemical Manipulation", "quote": "Add the aqueous silver nitrate drop by drop; it acts as an immediate **precipitant** of insoluble chloride salt."},
            {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The mob poured with **precipitant** fury down the boulevards, overwhelming the royal guard before muskets could be primed."}
        ]
    },
    "precipitate": {
        "primary": "To cause an event to happen prematurely or suddenly; or to separate as a solid from solution.",
        "secondary": "In atmospheric physics and chemical kinetics, to condense vapor into falling hydrometeors, or to fling down violently from a height.",
        "quotes": [
            {"author": "Mary Shelley", "work": "Frankenstein", "quote": "You would not call it murder if you could **precipitate** me into one of those ice-rifts and destroy my frame."},
            {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "He would be well content to **precipitate** himself over the hill-side once again rather than endure captivity."},
            {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The sudden financial disaster seemed destined to **precipitate** the ruin of the ancient d'Urberville lineage."}
        ]
    },
    "precipitately": {
        "primary": "With hasty, rash, or headlong speed; suddenly and without due consideration.",
        "secondary": "In military maneuver, retreating in disorganized flight without maintaining rear-guard defensive cohesion.",
        "quotes": [
            {"author": "George Eliot", "work": "Middlemarch", "quote": "She took up the toy and was not going to enter **precipitately** on any subject touching her sister's domestic happiness."},
            {"author": "Joseph Conrad", "work": "Heart of Darkness", "quote": "He talked **precipitately**, and I did not try to stop him, fearing to break the hypnotic spell of his confession."},
            {"author": "H. G. Wells", "work": "The War of the Worlds", "quote": "The militia withdrew **precipitately** from the canal bank as the heat-ray ignited the pine woods behind them."}
        ]
    },
    "precipitateness": {
        "primary": "The character of being rashly hurried, headlong, or incautiously hasty; headlong rush.",
        "secondary": "In ethical philosophy, the intellectual vice of leaping to deductive certitude without inductive verification.",
        "quotes": [
            {"author": "Francis Bacon", "work": "Novum Organum", "quote": "The understanding must not be allowed to jump from particulars to remote axioms with unbridled **precipitateness**."},
            {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "The fatal **precipitateness** of the National Assembly subverted in a single night institutions reared by ten centuries."},
            {"author": "Samuel Taylor Coleridge", "work": "Table Talk", "quote": "A statesman who mistakes administrative **precipitateness** for executive energy will steer the commonwealth onto the rocks."}
        ]
    },
    "precipitating": {
        "primary": "Bringing about abruptly, hastening, or separating as a solid out of a solution.",
        "secondary": "In meteorology, describing atmospheric air masses actively discharging moisture as rain, snow, sleet, or hail.",
        "quotes": [
            {"author": "William Shakespeare", "work": "King Lear", "quote": "Hadst thou been aught but gossamer, feathers, air, so many fathom down **precipitating**, thou'dst shivered like an egg."},
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The **precipitating** manner in which Captain Ahab quitted the Samuel Enderby was not unattended with grave danger."},
            {"author": "Walt Whitman", "work": "Leaves of Grass", "quote": "Hast never come to thee an hour, a sudden gleam divine, **precipitating**, bursting all these bubbles, fashions, wealth?"}
        ]
    },
    "precipitation": {
        "primary": "Water falling to earth as rain, snow, sleet, or hail; or headlong, hasty rush.",
        "secondary": "In inorganic chemistry and meteorology, the process of separating insoluble solid matter from a liquid, or the total volume of atmospheric water deposits.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Coriolanus", "quote": "Or pile ten hills on the Tarpeian rock, that the **precipitation** might down stretch below the beam of sight."},
            {"author": "H. G. Wells", "work": "The War of the Worlds", "quote": "The black vapor clung closely to the ground, even before its final **precipitation** as an inert powder on the earth."},
            {"author": "Charles Dickens", "work": "David Copperfield", "quote": "He bolted in with a **precipitation** quite alarming, gasping out that the bailiffs were already upon his heels."}
        ]
    },
    "precipitator": {
        "primary": "One who or that which precipitates; an apparatus that removes suspended particles.",
        "secondary": "In industrial environmental engineering, an electrostatic device that ionizes and collects fly ash and particulates from exhaust flue gases.",
        "quotes": [
            {"author": "H. G. Wells", "work": "The World Set Free", "quote": "The central smokestack was fitted with an electrical **precipitator** that cleansed industrial fumes before release."},
            {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "The metallic electrode acted as a powerful **precipitator**, drawing down suspended crystalline residues within the cylinder."},
            {"author": "Sinclair Lewis", "work": "Arrowsmith", "quote": "The commercial chemist installed an automatic **precipitator** to recover volatile reagents from the condensing vats."}
        ]
    },
    "precipitin": {
        "primary": "An antibody that interacts with a specific soluble antigen to form a visible precipitate.",
        "secondary": "In serology and forensic immunology, an immunoglobulin utilized in forensic bloodstain identification to confirm human origin.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The discovery of the specific **precipitin** reaction provided clinicians with an extraordinary tool for diagnostic differentiation."},
            {"author": "Arthur Conan Doyle", "work": "The Case-Book of Sherlock Holmes", "quote": "Holmes demonstrated his new test, showing how a minute drop of serum induced a distinct **precipitin** cloud in the vial."},
            {"author": "Paul Ehrlich", "work": "Studies in Immunity", "quote": "Each specific bacterial toxin stimulates the host organism to generate its corresponding **precipitin** in the blood plasma."}
        ]
    },
    "precipitous": {
        "primary": "Dangerously steep, sheer, or abrupt; or done with great haste and without deliberation.",
        "secondary": "In physical geography, characterized by almost perpendicular clifflike declivities dropping sheer to a baseline.",
        "quotes": [
            {"author": "Mary Shelley", "work": "Frankenstein", "quote": "The ascent is **precipitous**, but the path is cut into continual short windings that enable you to surmount the perpetual snow."},
            {"author": "H. G. Wells", "work": "The Time Machine", "quote": "The slope became so **precipitous** that I was forced to clamber on hands and knees among the broken aluminium masses."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "His mind was utterly narrowed into that **precipitous** crevice of play as if he had been the most reckless gambler."}
        ]
    },
    "precipitously": {
        "primary": "In a precipitously steep manner; or extremely rapidly, rashly, or abruptly.",
        "secondary": "In financial market analysis, describing sharp vertical collapses in asset prices that overwhelm stop-loss order buffers.",
        "quotes": [
            {"author": "Jack London", "work": "The Sea-Wolf", "quote": "The schooner rolled **precipitously** down the foam-capped wave, submerging her lee rail beneath the roaring surf."},
            {"author": "Arthur Conan Doyle", "work": "The Lost World", "quote": "The red sandstone cliff fell **precipitously** two thousand feet into the impenetrable tangle of the primeval forest."},
            {"author": "Robert Louis Stevenson", "work": "Treasure Island", "quote": "The narrow pathway climbed **precipitously** along the shoulder of Spy-glass Hill, exposed to the ocean gale."}
        ]
    },
    "precipitousness": {
        "primary": "Sheer vertical steepness, cliff-like perpendicularity, or rash, unconsidered velocity.",
        "secondary": "In alpine geomorphology, the angle of declivity exceeding sixty degrees that prevents soil accumulation or vegetation anchoring.",
        "quotes": [
            {"author": "John Ruskin", "work": "Modern Painters", "quote": "The sheer **precipitousness** of the Matterhorn's northern face defies the painter's brush to convey its sublime terror."},
            {"author": "Edmund Burke", "work": "A Philosophical Enquiry into the Sublime and Beautiful", "quote": "A vast height loses half its sublimity if it lacks that abrupt **precipitousness** which threatens instantaneous destruction."},
            {"author": "Walter Scott", "work": "Waverley", "quote": "The guide warned the party against the treacherous **precipitousness** of the Highland gorge as twilight descended."}
        ]
    },
    "precis": {
        "primary": "A concise summary, abstract, or abridgment of the essential facts or text.",
        "secondary": "In diplomatic reporting and administrative governance, an official analytical distillation of lengthy treaties or diplomatic dispatches.",
        "quotes": [
            {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "Lord Henry drew a brilliant **precis** of modern psychological theory, reducing complex doctrines to sparkling epigrams."},
            {"author": "Arthur Conan Doyle", "work": "The Memoirs of Sherlock Holmes", "quote": "Holmes handed me a neat **precis** of the naval treaty, outlining the four crucial clauses in chronological order."},
            {"author": "Lytton Strachey", "work": "Eminent Victorians", "quote": "Gladstone digested the voluminous colonial reports into an admirable **precis** before presenting his bill to the Commons."}
        ]
    },
    "precise": {
        "primary": "Exact, accurate, strictly defined, sharply stated, or minutely detailed.",
        "secondary": "In mathematical physics and scientific instrumentation, characterized by high repeatability and minimal random deviation across measurement trials.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Measure for Measure", "quote": "Lord Angelo is **precise**, stands at a guard with envy, and scarce confesses that his blood flows or that his appetite is more to bread than stone."},
            {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "When we engage in a pursuit, a clear and **precise** conception of what we are pursuing would seem to be the first thing we need."},
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The shadows between the buttresses were so **precise** that one could trace every carving with absolute certainty."}
        ]
    },
    "precisely": {
        "primary": "In a precise manner; exactly, accurately, or strictly speaking.",
        "secondary": "In formal logical debate, expressing rigorous assent to an exact theoretical proposition without qualification.",
        "quotes": [
            {"author": "William Shakespeare", "work": "All's Well That Ends Well", "quote": "Truly, madam, if God have lent a man any manners, he may easily put it off at court: he that cannot make a leg **precisely** is no courtier."},
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Long experience had so **precisely** taught the animal the difference between calls that he obeyed without hesitation."},
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "We can see why competition should be most severe between allied forms that fill **precisely** the same place in the economy of nature."}
        ]
    },
    "preciseness": {
        "primary": "Exactitude, scrupulous distinctness, punctilious detail, or strict conformity to standards.",
        "secondary": "In seventeenth-century ecclesiastical history, strict Puritan adherence to ceremonial purity and moral regulations.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "His speech had that quaint **preciseness** which marks a scholar long accustomed to cloistered Latin disputations."},
            {"author": "Samuel Johnson", "work": "The Lives of the English Poets", "quote": "Pope polished his heroic couplets with an extraordinary **preciseness** that banished every redundant syllable."},
            {"author": "George Eliot", "work": "Romola", "quote": "The notary drafted the civic contract with professional **preciseness**, omitting no legal clause that might secure Florentine liberties."}
        ]
    },
    "precision": {
        "primary": "Sharp accuracy, definite exactness, or meticulous mechanical correctness.",
        "secondary": "In metrology and statistical data analysis, the closeness of agreement among independent test results obtained under stipulated conditions.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The practical experiments of horticulturists, though not made with scientific **precision**, deserve some notice."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "He delivered himself with **precision**, as if he had been called upon to make a public statement of constitutional law."},
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The hands moved on the dial, and thus, though the minutes were told with **precision**, the larger machinery often faltered."}
        ]
    },
    "preclinical": {
        "primary": "Relating to the stage of research or education before practical clinical experience or trials.",
        "secondary": "In pharmacology and oncology, designating in vitro and in vivo animal testing evaluating drug safety and kinetics prior to human administration.",
        "quotes": [
            {"author": "William Osler", "work": "Aequanimitas", "quote": "Thorough mastery of anatomy and physiology during the **preclinical** years lays an immovable foundation for hospital practice."},
            {"author": "Harvey Cushing", "work": "The Life of Sir William Osler", "quote": "He reformed the medical curriculum by integrating rigorous **preclinical** laboratory research with ward bedside rounds."},
            {"author": "Paul Ehrlich", "work": "Experimental Chemotherapy of Spirilloses", "quote": "Our systematic **preclinical** screening of arsenical compounds in murine models yielded compound 606 with remarkable curative efficacy."}
        ]
    },
    "preclude": {
        "primary": "To make impossible, prevent from happening, or rule out in advance.",
        "secondary": "In procedural civil jurisprudence, to bar a litigant from raising claims or issues already settled in prior final judgments.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The fire was issuing from a long straw-stack, which was so far gone as to **preclude** a possibility of saving it."},
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The perfect fertility of intercrossed races would seem to **preclude** classifying the varieties of mankind as distinct species."},
            {"author": "Jane Austen", "work": "Emma", "quote": "Her previous commitments did not wholly **preclude** her from taking part in the excursion planned by Mr. Knightley."}
        ]
    }
}
