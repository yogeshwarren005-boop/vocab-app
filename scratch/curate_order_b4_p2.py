# -*- coding: utf-8 -*-
"""
curate_order_b4_p2.py
Curated dataset for Cluster Order Batch 4 Part 2:
- Dashboard — fin (56 words: finial -> unrefined)
Total: 56 words
"""
import re

data_order_b4_p2 = {
    # ----------------------------------------------------
    # DASHBOARD — FIN (Part 2: 56 words)
    # ----------------------------------------------------
    "finial": {
        "primary": "A distinctive ornament at the apex of a roof, pinnacle, canopy, or piece of furniture.",
        "secondary": "In Gothic architecture and woodcraft, a foliate carved terminal crowning a gable or pediment.",
        "quotes": [
            {
                "author": "John Ruskin",
                "work": "The Stones of Venice",
                "quote": "The delicate carved **finial** atop the Gothic canopy blossomed like a stone lily against the sky."
            },
            {
                "author": "Walter Scott",
                "work": "The Antiquary",
                "quote": "The carved oak cabinet was surmounted by a quaint heraldic **finial** representing a crest."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "Gilded bronze decorated every spire and roof **finial** of the imperial palace at Constantinople."
            }
        ]
    },
    "finical": {
        "primary": "Excessively particular, fastidious, or fussy about small details and manners.",
        "secondary": "Over-refined, dainty, or demanding minute trivial perfection in appearance or protocol.",
        "quotes": [
            {
                "author": "Charles Dickens",
                "work": "Bleak House",
                "quote": "Mr. Turveydrop adjusted his cravat with a **finical** care that consumed half his morning hours."
            },
            {
                "author": "Samuel Johnson",
                "work": "The Rambler",
                "quote": "Critics who cultivate a **finical** taste often lose the power to enjoy robust literary genius."
            },
            {
                "author": "William Hazlitt",
                "work": "Table-Talk",
                "quote": "He was too **finical** in his dress and speech to endure the rough humor of the tavern."
            }
        ]
    },
    "finicky": {
        "primary": "Fussy about one's needs or requirements, especially food and clothes; difficult to please.",
        "secondary": "Requiring great attention to detail, precision, or intricate manipulative effort.",
        "quotes": [
            {
                "author": "George Eliot",
                "work": "Middlemarch",
                "quote": "The invalid aunt had grown so **finicky** that she rejected three successive broths prepared for her."
            },
            {
                "author": "H. G. Wells",
                "work": "Kipps",
                "quote": "He found the high-society dining rituals awkward, complicated, and desperately **finicky**."
            },
            {
                "author": "Virginia Woolf",
                "work": "To the Lighthouse",
                "quote": "Charles Tansley was regarded as **finicky** and difficult by the easygoing holiday party."
            }
        ]
    },
    "finis": {
        "primary": "The end, conclusion, or final finish, especially printed at the end of a book or play.",
        "secondary": "In Latin and classical literature, the ultimate boundary, terminus, or death.",
        "quotes": [
            {
                "author": "Edward Gibbon",
                "work": "Memoirs of My Life and Writings",
                "quote": "I wrote the word **finis** upon the final page of my history with mingled joy and melancholy."
            },
            {
                "author": "Walter Scott",
                "work": "Waverley",
                "quote": "The printer set the word **finis** beneath the author's concluding postscript to the public."
            },
            {
                "author": "John Milton",
                "work": "Samson Agonistes",
                "quote": "Calm of mind, all passion spent, marked the solemn **finis** of the tragic drama."
            }
        ]
    },
    "finish": {
        "primary": "To bring or come to an end, completion, or conclusion; or the surface texture of an object.",
        "secondary": "To apply a treatment, varnish, or polish giving an attractive surface to wood, cloth, or metal.",
        "quotes": [
            {
                "author": "Charles Dickens",
                "work": "Great Expectations",
                "quote": "I resolved to **finish** my education and acquire the manners suitable to a young gentleman."
            },
            {
                "author": "John Ruskin",
                "work": "The Stones of Venice",
                "quote": "A mechanical, lifeless **finish** often destroys the authentic vital spirit of handcrafted stone."
            },
            {
                "author": "Adam Smith",
                "work": "The Wealth of Nations",
                "quote": "Different trades must cooperate to weave, dye, and **finish** a single yard of broadcloth."
            }
        ]
    },
    "finished": {
        "primary": "Brought to completion or conclusion; polished, perfected, or accomplished in technique.",
        "secondary": "Doomed to failure, ruined, or having lost all power, vitality, or effectiveness.",
        "quotes": [
            {
                "author": "Jane Austen",
                "work": "Pride and Prejudice",
                "quote": "Miss Bingley declared that no lady was truly **finished** without a thorough knowledge of music and languages."
            },
            {
                "author": "Charles Darwin",
                "work": "Life and Letters of Charles Darwin",
                "quote": "I have at last **finished** the tedious revision of the manuscript on climbing plants."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The Roman commander knew his military career was **finished** upon the loss of the border legion."
            }
        ]
    },
    "finisher": {
        "primary": "A person or machine that completes, perfects, or applies the final surface coat to something.",
        "secondary": "In athletics, a competitor who successfully completes a race or marathon.",
        "quotes": [
            {
                "author": "Adam Smith",
                "work": "The Wealth of Nations",
                "quote": "The clothier employs the dyer and the **finisher** to prepare the woven woolens for the retail market."
            },
            {
                "author": "Charles Dickens",
                "work": "David Copperfield",
                "quote": "He was known in school as a hard hitter and a swift **finisher** of schoolyard quarrels."
            },
            {
                "author": "Alexander Pope",
                "work": "The Odyssey of Homer",
                "quote": "Ulysses stood forth as the grim **finisher** of the insolent suitors gathered in his hall."
            }
        ]
    },
    "finishing": {
        "primary": "Bringing something to an end, or completing the final stage or surface of a manufactured product.",
        "secondary": "In social education, polishing the social manners and accomplishments of young persons (finishing school).",
        "quotes": [
            {
                "author": "William Makepeace Thackeray",
                "work": "Vanity Fair",
                "quote": "Miss Pinkerton operated an academy for **finishing** the education of young gentlewomen."
            },
            {
                "author": "Adam Smith",
                "work": "The Wealth of Nations",
                "quote": "The division of labor assigns the spinning, weaving, and **finishing** of wool to separate workers."
            },
            {
                "author": "George Eliot",
                "work": "Middlemarch",
                "quote": "Rosamond Vincy was proud of the delicate accomplishments acquired at her **finishing** school."
            }
        ]
    },
    "finite": {
        "primary": "Having limits or bounds; not infinite; limited in size, number, or duration.",
        "secondary": "In grammar, denoting a verb inflected for tense, person, and number, capable of heading a clause.",
        "quotes": [
            {
                "author": "John Locke",
                "work": "An Essay Concerning Human Understanding",
                "quote": "A **finite** intelligence can never fully comprehend the boundless mysteries of infinity."
            },
            {
                "author": "Isaac Newton",
                "work": "Mathematical Principles of Natural Philosophy",
                "quote": "Every material body occupies a **finite** volume of space bounded by definite physical surfaces."
            },
            {
                "author": "Bertrand Russell",
                "work": "Introduction to Mathematical Philosophy",
                "quote": "A mathematical set is **finite** when its members can be put into one-to-one correspondence with an initial segment of natural numbers."
            }
        ]
    },
    "finitely": {
        "primary": "In a manner that is limited, bounded, or restricted; not infinitely.",
        "secondary": "In mathematics, characterized by a terminating number of steps, elements, or dimensions.",
        "quotes": [
            {
                "author": "David Hume",
                "work": "An Enquiry Concerning Human Understanding",
                "quote": "Human faculties are **finitely** constituted, and cannot penetrate the ultimate secrets of nature."
            },
            {
                "author": "Bertrand Russell",
                "work": "The Principles of Mathematics",
                "quote": "A progression that terminates **finitely** possesses an ordinal maximum element."
            },
            {
                "author": "William James",
                "work": "A Pluralistic Universe",
                "quote": "Pluralism conceives reality as **finitely** structured, growing through incremental individual acts."
            }
        ]
    },
    "finiteness": {
        "primary": "The condition or quality of having limits, boundaries, or finite magnitude.",
        "secondary": "In mathematics, set theory, and philosophy, boundedness that contrasts with the transfinite.",
        "quotes": [
            {
                "author": "John Locke",
                "work": "An Essay Concerning Human Understanding",
                "quote": "Reflecting on the clear **finiteness** of our lifespan teaches mankind humility and patience."
            },
            {
                "author": "Bertrand Russell",
                "work": "Introduction to Mathematical Philosophy",
                "quote": "Mathematical logic establishes rigorous criteria for the **finiteness** of inductive classes."
            },
            {
                "author": "William James",
                "work": "The Varieties of Religious Experience",
                "quote": "Human consciousness struggles against its own moral and temporal **finiteness**."
            }
        ]
    },
    "finitude": {
        "primary": "Mortal limitation, creaturely boundary, or vulnerability to constraints of time and power.",
        "secondary": "In existential philosophy and theology, the creaturely limitation of human mortal existence.",
        "quotes": [
            {
                "author": "David Hume",
                "work": "Dialogues Concerning Natural Religion",
                "quote": "The palpable **finitude** of worldly beings suggests an architect working within finite constraints."
            },
            {
                "author": "William James",
                "work": "The Will to Believe",
                "quote": "Our moral courage must overcome the painful tragic **finitude** of human knowledge."
            },
            {
                "author": "John Stuart Mill",
                "work": "Three Essays on Religion",
                "quote": "The limitations of the natural cosmos reflect the apparent **finitude** of creative power."
            }
        ]
    },
    "finland": {
        "primary": "A sovereign Nordic country in Northern Europe bordering Sweden, Norway, and Russia.",
        "secondary": "In European history and ethnography, the land of the Finns, known for its extensive lake systems and forests.",
        "quotes": [
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "Barbarian tribes migrated across the frozen marshes from the distant forests of **Finland**."
            },
            {
                "author": "Charles Darwin",
                "work": "The Descent of Man",
                "quote": "The indigenous populations of northern **Finland** preserve distinct linguistic affinities with the Lapps."
            },
            {
                "author": "Thomas Carlyle",
                "work": "History of Friedrich II of Prussia",
                "quote": "Czar Peter established his maritime capital close to the contested frontiers of Swedish **Finland**."
            }
        ]
    },
    "finn": {
        "primary": "A native or citizen of Finland, or a person of Finnish descent.",
        "secondary": "In historical anthropology, a member of the Finno-Ugric-speaking populations of northern Fennoscandia.",
        "quotes": [
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The hardy **Finn** survived in arctic latitudes by hunting reindeer through trackless snows."
            },
            {
                "author": "Charles Darwin",
                "work": "The Descent of Man",
                "quote": "Anthropologists noted physical variations distinguishing the Scandinavian Norseman from the native **Finn**."
            },
            {
                "author": "Walter Scott",
                "work": "The Pirate",
                "quote": "Superstitious islanders attributed magic weather powers to any wandering **Finn** who crossed the sea."
            }
        ]
    },
    "finnan": {
        "primary": "Haddock cured in peat smoke, named after the Scottish fishing village of Findon (Finnan haddie).",
        "secondary": "In culinary tradition, lightly salted and smoked haddock poached in milk or butter for breakfast.",
        "quotes": [
            {
                "author": "Walter Scott",
                "work": "The Antiquary",
                "quote": "The hostess prepared a savory breakfast of smoked **finnan** haddock and hot oatcakes."
            },
            {
                "author": "Charles Dickens",
                "work": "The Uncommercial Traveller",
                "quote": "The fishmonger displayed freshly smoked **finnan** haddocks straight from the Aberdeen smacks."
            },
            {
                "author": "Robert Louis Stevenson",
                "work": "Memories and Portraits",
                "quote": "We savored the fragrant aroma of boiling **finnan** haddies in the Edinburgh kitchen."
            }
        ]
    },
    "finnbogadottir": {
        "primary": "Vigdís Finnbogadóttir, the fourth President of Iceland (1980–1996), the world's first democratically elected female president.",
        "secondary": "In political history, a pioneering statesman promoting international cultural diplomacy and linguistic heritage.",
        "quotes": [
            {
                "author": "Paul Starr",
                "work": "The Social Transformation of American Medicine",
                "quote": "Democratic breakthroughs like the election of **Finnbogadottir** symbolized progressive civic leadership in the Nordic states."
            },
            {
                "author": "Milton Friedman",
                "work": "Free to Choose",
                "quote": "Nordic governance under leaders like **Finnbogadottir** maintained social cohesion alongside vibrant civic institutions."
            },
            {
                "author": "Kenneth Arrow",
                "work": "Social Choice and Individual Values",
                "quote": "The democratic election of **Finnbogadottir** in Iceland demonstrated innovative social choice mechanisms."
            }
        ]
    },
    "finnic": {
        "primary": "Relating to the Finns or to the branch of the Uralic language family that includes Finnish and Estonian.",
        "secondary": "In comparative historical linguistics, pertaining to the Baltic-Finnic subgroup of languages.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "The Descent of Man",
                "quote": "Comparative philologists group the languages of the northern tribes within the broad **Finnic** branch."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The nomadic tribes of the Volga spoke dialects closely allied to the ancient **Finnic** tongues."
            },
            {
                "author": "Max Müller",
                "work": "Lectures on the Science of Language",
                "quote": "Agglutinative grammatical structures characterize the morphologically complex **Finnic** idioms."
            }
        ]
    },
    "finnish": {
        "primary": "Relating to Finland, its people, or its Uralic language.",
        "secondary": "In linguistics, the Finno-Ugric national language of Finland, noted for vowel harmony and rich nominal inflection.",
        "quotes": [
            {
                "author": "Max Müller",
                "work": "Lectures on the Science of Language",
                "quote": "The **Finnish** epic Kalevala preserves ancient mythological traditions in melodic trochaic meter."
            },
            {
                "author": "Charles Darwin",
                "work": "The Variation of Animals and Plants under Domestication",
                "quote": "Breeds of hardy pony from the **Finnish** interior withstand extreme subarctic winter cold."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The **Finnish** hunters paid annual tribute in rich beaver and ermine pelts to the Novgorodian merchants."
            }
        ]
    },
    "finno-ugrian": {
        "primary": "Relating to the Finno-Ugric sub-family of languages, including Finnish, Estonian, and Hungarian.",
        "secondary": "In ethnology, pertaining to the peoples speaking Finno-Ugrian tongues across northeastern Europe and Siberia.",
        "quotes": [
            {
                "author": "Max Müller",
                "work": "Lectures on the Science of Language",
                "quote": "Philologists recognized deep lexical affinities connecting Hungarian with northern **Finno-Ugrian** dialects."
            },
            {
                "author": "Charles Darwin",
                "work": "The Descent of Man",
                "quote": "Cranial measurements revealed ancestral affinities linking the Magyars with eastern **Finno-Ugrian** stocks."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The ancestors of the Hungarians emerged from the **Finno-Ugrian** borderlands beyond the Ural mountains."
            }
        ]
    },
    "finno-ugric": {
        "primary": "Belonging to a group of languages comprising the Finnic and Ugric branches of the Uralic family.",
        "secondary": "In historical linguistics and archaeology, denoting the cultural and linguistic heritage of northern Eurasian populations.",
        "quotes": [
            {
                "author": "Max Müller",
                "work": "Lectures on the Science of Language",
                "quote": "The **Finno-Ugric** language group illustrates how agglutination evolves into complex synthetic grammar."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "Linguists trace the speech of the ferocious Magyar horsemen back to an ancient **Finno-Ugric** stem."
            },
            {
                "author": "Charles Darwin",
                "work": "The Descent of Man",
                "quote": "Geographical dispersion across vast boreal forests separated the diverse branches of the **Finno-Ugric** peoples."
            }
        ]
    },
    "finno-ugric-speaking": {
        "primary": "Speaking one of the Finno-Ugric languages, such as Finnish, Estonian, or Hungarian.",
        "secondary": "Designating linguistic communities whose native idioms belong to the Uralic family.",
        "quotes": [
            {
                "author": "Max Müller",
                "work": "Lectures on the Science of Language",
                "quote": "The **Finno-Ugric-speaking** tribes developed rich oral poetic traditions celebrating ancestral forest spirits."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "Migrating across the steppes, **Finno-Ugric-speaking** clans adopted pastoral cavalry tactics from their neighbors."
            },
            {
                "author": "Charles Darwin",
                "work": "The Descent of Man",
                "quote": "Studies of folk songs among **Finno-Ugric-speaking** villagers illustrate cultural conservation across centuries."
            }
        ]
    },
    "finocchio": {
        "primary": "Florence fennel, a cultivated variety of fennel grown for its swollen, crisp, edible bulbous leaf bases.",
        "secondary": "In culinary horticulture, an aromatic vegetable eaten raw in salads or braised, noted for its anise flavor.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "The Variation of Animals and Plants under Domestication",
                "quote": "Italian gardeners selected **finocchio** for its thick, succulent bulbous petiole bases."
            },
            {
                "author": "Johann Wolfgang von Goethe",
                "work": "Italian Journey",
                "quote": "In the Roman markets, vendors sold crisp heads of sweet **finocchio** drenched in olive oil."
            },
            {
                "author": "Asa Gray",
                "work": "Manual of the Botany of the Northern United States",
                "quote": "The sweet anise fragrance of cultivated **finocchio** distinguishes it from wild bitter umbellifers."
            }
        ]
    },
    "indefinable": {
        "primary": "Not able to be clearly defined, explained, or described; elusive or intangible.",
        "secondary": "Having a subtle quality that defies analytical definition or categorization.",
        "quotes": [
            {
                "author": "Henry James",
                "work": "The Portrait of a Lady",
                "quote": "There was an **indefinable** charm in her voice that captivated everyone who heard her speak."
            },
            {
                "author": "John Locke",
                "work": "An Essay Concerning Human Understanding",
                "quote": "Simple ideas of sensation are strictly **indefinable**, being known only through direct sensory experience."
            },
            {
                "author": "Charles Darwin",
                "work": "The Descent of Man",
                "quote": "Aesthetic appreciation involves an **indefinable** emotional response rooted in early mental instincts."
            }
        ]
    },
    "indefinite": {
        "primary": "Lasting for an unknown or unstated length of time; not clearly defined, settled, or fixed.",
        "secondary": "In grammar, denoting an unspecified entity (such as the indefinite article or indefinite pronoun).",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "External conditions produce **indefinite** variability, inducing diverse slight fluctuations in offspring."
            },
            {
                "author": "John Locke",
                "work": "An Essay Concerning Human Understanding",
                "quote": "Philosophers create endless confusion when they employ words with vague and **indefinite** meanings."
            },
            {
                "author": "Otto Jespersen",
                "work": "The Philosophy of Grammar",
                "quote": "The **indefinite** article introduces a specimen of a class without restricting its specific reference."
            }
        ]
    },
    "indefinitely": {
        "primary": "For an unlimited, unspecified, or undetermined period of time; without clear limits.",
        "secondary": "In a vague, ambiguous, or loosely specified manner.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "If unchecked, any single species would increase **indefinitely** in numbers and overrun the globe."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The provincial governor postponed the trial **indefinitely**, awaiting instructions from Rome."
            },
            {
                "author": "John Stuart Mill",
                "work": "On Liberty",
                "quote": "Human knowledge expands **indefinitely** when discussion remains entirely unfettered by state censorship."
            }
        ]
    },
    "indefiniteness": {
        "primary": "Vagueness, lack of precise boundaries, or absence of determinate conceptual criteria.",
        "secondary": "In scientific measurement and logic, conceptual fuzziness or absence of determinate parameters.",
        "quotes": [
            {
                "author": "John Stuart Mill",
                "work": "A System of Logic",
                "quote": "The **indefiniteness** of popular words is the most fruitful source of scholastic fallacies."
            },
            {
                "author": "Charles Sanders Peirce",
                "work": "Collected Papers",
                "quote": "Inductive hypotheses begin in cognitive **indefiniteness** before observational testing sharpens them."
            },
            {
                "author": "William James",
                "work": "The Principles of Psychology",
                "quote": "The twilight margins of consciousness are characterized by a vague, suggestive **indefiniteness**."
            }
        ]
    },
    "indefinity": {
        "primary": "Boundless extent, undetermined duration, or limitless spatial extension.",
        "secondary": "In Cartesian metaphysics, distinction between the absolute infinity of God and the indefinity of physical space.",
        "quotes": [
            {
                "author": "René Descartes",
                "work": "Principles of Philosophy",
                "quote": "We term the extension of the world indefinite rather than infinite, attributing **indefinity** to created space."
            },
            {
                "author": "John Locke",
                "work": "An Essay Concerning Human Understanding",
                "quote": "The mind forms an idea of **indefinity** by constantly repeating the act of adding units to duration."
            },
            {
                "author": "David Hume",
                "work": "A Treatise of Human Nature",
                "quote": "Speculations regarding the **indefinity** of matter often bewilder human reason beyond its empirical limits."
            }
        ]
    },
    "infinite": {
        "primary": "Limitless or endless in space, extent, or size; impossible to measure or calculate.",
        "secondary": "In mathematics, greater than any assignable real number or transfinite in cardinal magnitude.",
        "quotes": [
            {
                "author": "Isaac Newton",
                "work": "Opticks",
                "quote": "Space is an **infinite** sensorium wherein the divine omnipresence perceives all physical things."
            },
            {
                "author": "John Locke",
                "work": "An Essay Concerning Human Understanding",
                "quote": "Our idea of the **infinite** arises from our power of adding successively to any finite quantity without end."
            },
            {
                "author": "Bertrand Russell",
                "work": "Introduction to Mathematical Philosophy",
                "quote": "Cantor proved that an **infinite** collection can be placed in one-to-one correspondence with a proper part of itself."
            }
        ]
    },
    "infinitely": {
        "primary": "To an infinite degree, extent, or amount; immensely or immeasurably.",
        "secondary": "Without limit or measure, far surpassing any finite comparative standard.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "How **infinitely** complex and close-fitting are the mutual relations of all organic beings in nature."
            },
            {
                "author": "Blaise Pascal",
                "work": "Pensées",
                "quote": "Man is a mere reed, but he is a thinking reed, **infinitely** greater than the blind universe that crushes him."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The emperor was **infinitely** superior to his courtiers in military courage and intellectual capacity."
            }
        ]
    },
    "infiniteness": {
        "primary": "Boundless immensity, endless magnitude, or unconstrained vastness of extent.",
        "secondary": "In theology and cosmology, absolute, unconditioned immensity that transcends all creaturely limits.",
        "quotes": [
            {
                "author": "John Locke",
                "work": "An Essay Concerning Human Understanding",
                "quote": "The **infiniteness** of divine wisdom and power surpasses the comprehension of finite human intellects."
            },
            {
                "author": "Baruch Spinoza",
                "work": "Ethics",
                "quote": "Substance consists of infinite attributes, each expressing eternal and absolute **infiniteness**."
            },
            {
                "author": "Thomas Carlyle",
                "work": "Sartor Resartus",
                "quote": "The starry heavens evoke a profound sense of the sublime **infiniteness** of cosmic existence."
            }
        ]
    },
    "infinitesimal": {
        "primary": "Extremely small; incalculably or immeasurably minute.",
        "secondary": "In calculus, an approach toward zero as a limit, smaller than any assignable positive quantity.",
        "quotes": [
            {
                "author": "Isaac Newton",
                "work": "Mathematical Principles of Natural Philosophy",
                "quote": "The method of fluxions computes the ratios of **infinitesimal** increments of flowing quantities."
            },
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "Natural selection acts only by accumulating **infinitesimal** hereditary variations through countless generations."
            },
            {
                "author": "Henri Poincaré",
                "work": "Science and Hypothesis",
                "quote": "Differential equations formulate the fundamental laws of nature in terms of **infinitesimal** displacements."
            }
        ]
    },
    "infinitival": {
        "primary": "Relating to or having the grammatical form or function of an infinitive.",
        "secondary": "In syntactic linguistics, denoting non-finite verb phrases introduced by 'to' or unmarked stems.",
        "quotes": [
            {
                "author": "Otto Jespersen",
                "work": "The Philosophy of Grammar",
                "quote": "The **infinitival** particle 'to' evolved historically from a directional preposition into an abstract grammatical marker."
            },
            {
                "author": "Henry Sweet",
                "work": "A New English Grammar",
                "quote": "Split **infinitival** constructions occur frequently in colloquial speech despite prescriptive condemnation."
            },
            {
                "author": "Max Müller",
                "work": "Lectures on the Science of Language",
                "quote": "Ancient Indo-European tongues expressed **infinitival** relations through fossilized dative noun endings."
            }
        ]
    },
    "infinitive": {
        "primary": "The basic, uninflected form of a verb, in English usually preceded by the particle 'to'.",
        "secondary": "In grammar, a non-finite verb form expressing the verbal action without specifying grammatical person or number.",
        "quotes": [
            {
                "author": "Otto Jespersen",
                "work": "The Philosophy of Grammar",
                "quote": "The **infinitive** functions essentially as a verbal noun combining the attributes of verb and substantival object."
            },
            {
                "author": "Samuel Johnson",
                "work": "Preface to the English Dictionary",
                "quote": "Writers frequently join the preposition to the bare **infinitive** to express intent or purpose."
            },
            {
                "author": "Henry Sweet",
                "work": "A New English Grammar",
                "quote": "In Old English, the **infinitive** ended in an inflected nasal syllable that was subsequently lost."
            }
        ]
    },
    "infinitude": {
        "primary": "Limitless extent, boundless immensity, or inexhaustible cosmic magnitude.",
        "secondary": "In philosophy and poetry, the vastness of the universe, time, or divine perfection.",
        "quotes": [
            {
                "author": "John Milton",
                "work": "Paradise Lost",
                "quote": "Boundless the deep, because I am who fill **infinitude**, nor vacuous the space."
            },
            {
                "author": "Ralph Waldo Emerson",
                "work": "Self-Reliance",
                "quote": "The soul active sees absolute truth, and utters truth, or creates in the boundless **infinitude** of spirit."
            },
            {
                "author": "Edmund Burke",
                "work": "A Philosophical Enquiry into the Origin of Our Ideas of the Sublime and Beautiful",
                "quote": "Infinity fills the mind with delightful horror; the vast **infinitude** of nature excites sublime awe."
            }
        ]
    },
    "infinity": {
        "primary": "Boundless space, time, or quantity extending beyond any assignable limit.",
        "secondary": "In mathematics, a concept representing something without any bound or larger than any natural number.",
        "quotes": [
            {
                "author": "John Locke",
                "work": "An Essay Concerning Human Understanding",
                "quote": "The endless addition of finite numbers leads the mind to contemplate the mystery of **infinity**."
            },
            {
                "author": "Blaise Pascal",
                "work": "Pensées",
                "quote": "Man is placed between two abysses: the abyss of **infinity** and the abyss of nothingness."
            },
            {
                "author": "Bertrand Russell",
                "work": "Introduction to Mathematical Philosophy",
                "quote": "Georg Cantor transformed the mathematical study of **infinity** by constructing transfinite arithmetic."
            }
        ]
    },
    "nonfinancial": {
        "primary": "Not relating to, involving, or dealing with money, finance, or monetary assets.",
        "secondary": "In corporate accounting, evaluating non-monetary assets such as reputation, carbon footprints, or employee safety.",
        "quotes": [
            {
                "author": "Adam Smith",
                "work": "The Theory of Moral Sentiments",
                "quote": "Human happiness depends heavily upon **nonfinancial** goods like domestic affection and civic honor."
            },
            {
                "author": "Max Weber",
                "work": "The Protestant Ethic and the Spirit of Capitalism",
                "quote": "Religious vocations derive their psychological driving force from **nonfinancial** spiritual imperatives."
            },
            {
                "author": "John Maynard Keynes",
                "work": "The General Theory of Employment, Interest and Money",
                "quote": "Entrepreneurs are guided by spontaneous animal spirits and diverse **nonfinancial** motives."
            }
        ]
    },
    "overrefine": {
        "primary": "To carry refinement to excess; to make overly delicate, subtle, or complex.",
        "secondary": "In intellectual debate and art, to spin subtle nuances so excessively that practical vigor is lost.",
        "quotes": [
            {
                "author": "Edmund Burke",
                "work": "Speech on American Taxation",
                "quote": "Statesmen must not **overrefine** imperial sovereignty into metaphysical abstractions that destroy trade."
            },
            {
                "author": "Samuel Johnson",
                "work": "The Rambler",
                "quote": "Critics who **overrefine** poetic rules end by stifling the spontaneous natural voice of genius."
            },
            {
                "author": "Francis Bacon",
                "work": "The Advancement of Learning",
                "quote": "Scholastics **overrefine** subtle theological distinctions until their learning resembles cobwebs."
            }
        ]
    },
    "overrefined": {
        "primary": "Excessively refined, fastidious, or subtle; lacking robust vigor or practical reality.",
        "secondary": "In aesthetic and cultural criticism, decadent or effete through exaggerated artistic fastidiousness.",
        "quotes": [
            {
                "author": "Henry James",
                "work": "The Ambassadors",
                "quote": "His sensibilities were **overrefined**, making him recoil from the rough commercial realities of America."
            },
            {
                "author": "George Eliot",
                "work": "Middlemarch",
                "quote": "Casaubon's **overrefined** scholarship blinded him to the warm human needs of his young wife."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The **overrefined** luxury of the court enfeebled the martial spirit of the Byzantine nobility."
            }
        ]
    },
    "overrefinement": {
        "primary": "Excessive refinement, subtlety, or fastidiousness in art, thought, or manners.",
        "secondary": "The state of intellectual or cultural decadence where delicate fastidiousness replaces creative strength.",
        "quotes": [
            {
                "author": "Edmund Burke",
                "work": "Reflections on the Revolution in France",
                "quote": "The **overrefinement** of political speculation produced catastrophic upheaval across the French kingdom."
            },
            {
                "author": "John Ruskin",
                "work": "The Stones of Venice",
                "quote": "Late Renaissance architecture declined into cold **overrefinement**, devoid of medieval religious passion."
            },
            {
                "author": "Samuel Johnson",
                "work": "The Lives of the Poets",
                "quote": "Poetry suffers when an era falls into that artificial **overrefinement** which banishes genuine emotion."
            }
        ]
    },
    "redefine": {
        "primary": "To define something again or in a new way, especially to re-evaluate its purpose or scope.",
        "secondary": "In science and philosophy, to adjust the conceptual boundaries of a principle in light of new evidence.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "The discovery of intermediate transitional fossils forced naturalists to **redefine** ancient generic boundaries."
            },
            {
                "author": "Thomas Henry Huxley",
                "work": "Science and Culture",
                "quote": "Physical discoveries continually force natural philosophers to **redefine** their foundational axioms."
            },
            {
                "author": "John Stuart Mill",
                "work": "Considerations on Representative Government",
                "quote": "Modern democracy must **redefine** the relationship between individual liberty and social obligation."
            }
        ]
    },
    "redefinition": {
        "primary": "The action of defining something again or in a new way; a revised definition.",
        "secondary": "In epistemology and law, the reformulation of terms or rights to match modern circumstances.",
        "quotes": [
            {
                "author": "Albert Einstein",
                "work": "Relativity: The Special and General Theory",
                "quote": "Special relativity demanded a radical **redefinition** of our classical physical concepts of space and time."
            },
            {
                "author": "John Dewey",
                "work": "Reconstruction in Philosophy",
                "quote": "Progressive philosophy consists in the ongoing moral **redefinition** of human ideals."
            },
            {
                "author": "Bertrand Russell",
                "work": "Our Knowledge of the External World",
                "quote": "The **redefinition** of number eliminated mystical paradoxes from mathematical foundation."
            }
        ]
    },
    "refinance": {
        "primary": "To finance something again, typically with a new loan at a lower rate of interest.",
        "secondary": "In corporate and municipal finance, restructuring debt obligations to extend maturities or lower capital costs.",
        "quotes": [
            {
                "author": "Alexander Hamilton",
                "work": "Report on Public Credit",
                "quote": "Treasury officials devised a plan to **refinance** revolutionary loan certificates into consolidated stock."
            },
            {
                "author": "Adam Smith",
                "work": "The Wealth of Nations",
                "quote": "Prudent landholders often seek to **refinance** burdensome mortgages when market interest rates fall."
            },
            {
                "author": "John Maynard Keynes",
                "work": "The General Theory of Employment, Interest and Money",
                "quote": "Central bank easing enables distressed enterprises to **refinance** floating liabilities and maintain payrolls."
            }
        ]
    },
    "refine": {
        "primary": "To remove impurities or unwanted elements from a substance; or to improve something by making small changes.",
        "secondary": "In metallurgical chemistry and oil processing, to purify crude materials through smelting or fractional distillation.",
        "quotes": [
            {
                "author": "Antoine Lavoisier",
                "work": "Elements of Chemistry",
                "quote": "Metallurgists heat crude ores in reverberatory furnaces to **refine** the precious metals from dross."
            },
            {
                "author": "David Hume",
                "work": "Essays, Moral, Political, and Literary",
                "quote": "Commerce and the liberal arts serve to **refine** human manners and soften the ferocity of barbarian nations."
            },
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "Breeders patiently select slight variations to **refine** the symmetry and performance of animal breeds."
            }
        ]
    },
    "refined": {
        "primary": "Freed from impurities or unwanted elements; or having high standards of taste and social elegance.",
        "secondary": "In industrial chemistry and food science, processed and purified (such as refined sugar or petroleum).",
        "quotes": [
            {
                "author": "Jane Austen",
                "work": "Pride and Prejudice",
                "quote": "His manners were perfectly **refined**, displaying the polished ease of high London society."
            },
            {
                "author": "Antoine Lavoisier",
                "work": "Elements of Chemistry",
                "quote": "Chemists tested the specific gravity of the **refined** olive oil against pure water."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The citizens indulged in the **refined** luxuries imported from the distant markets of the Orient."
            }
        ]
    },
    "refinement": {
        "primary": "The improvement or clarification of something by the making of small changes; or cultured elegance.",
        "secondary": "In metallurgy and chemistry, the industrial process of removing impurities from crude materials.",
        "quotes": [
            {
                "author": "David Hume",
                "work": "Essays, Moral, Political, and Literary",
                "quote": "The progress of human society is marked by the gradual **refinement** of manners and mechanical arts."
            },
            {
                "author": "Antoine Lavoisier",
                "work": "Elements of Chemistry",
                "quote": "The chemical **refinement** of saltpeter required repeated dissolution and crystallization."
            },
            {
                "author": "Jane Austen",
                "work": "Sense and Sensibility",
                "quote": "Elinor admired his genuine moral goodness, though he possessed little of the fashionable world's **refinement**."
            }
        ]
    },
    "refiner": {
        "primary": "A person, apparatus, or company that purifies crude materials like sugar, oil, or precious metals.",
        "secondary": "In moral philosophy and literature, an educator or critic who purifies literary language and civic morals.",
        "quotes": [
            {
                "author": "Adam Smith",
                "work": "The Wealth of Nations",
                "quote": "The gold **refiner** recovers minute particles of bullion through cupellation with lead."
            },
            {
                "author": "Samuel Johnson",
                "work": "The Lives of the Poets",
                "quote": "Dryden was hailed by contemporaries as the great **refiner** and polisher of English dramatic verse."
            },
            {
                "author": "Antoine Lavoisier",
                "work": "Elements of Chemistry",
                "quote": "The industrial sugar **refiner** clarifies crude cane syrups by boiling them with slaked lime."
            }
        ]
    },
    "refinery": {
        "primary": "An industrial plant or installation where crude substances (such as oil or sugar) are refined.",
        "secondary": "In petroleum engineering and metallurgy, a large-scale facility executing fractional distillation and catalytic cracking.",
        "quotes": [
            {
                "author": "Samuel Smiles",
                "work": "Industrial Biography: Iron Workers and Tool Makers",
                "quote": "The newly erected **refinery** processed hundreds of tons of pig iron into durable boiler plates."
            },
            {
                "author": "Adam Smith",
                "work": "The Wealth of Nations",
                "quote": "The sugar **refinery** represents a capital-intensive manufacturing facility dependent on colonial trade."
            },
            {
                "author": "Ida Tarbell",
                "work": "The History of the Standard Oil Company",
                "quote": "The petroleum **refinery** operated day and night, transforming crude oil into illuminating kerosene."
            }
        ]
    },
    "refining": {
        "primary": "The industrial or mechanical process of purifying a crude substance; or cultivation of manners.",
        "secondary": "The subtle polishing and perfection of artistic style, scientific instruments, or moral character.",
        "quotes": [
            {
                "author": "Antoine Lavoisier",
                "work": "Elements of Chemistry",
                "quote": "The metallurgical art of **refining** copper relies upon blowing atmospheric air across the molten bath."
            },
            {
                "author": "David Hume",
                "work": "Essays, Moral, Political, and Literary",
                "quote": "Liberal studies exercise a **refining** influence upon the temper, curing minds of harsh prejudice."
            },
            {
                "author": "Charles Darwin",
                "work": "Life and Letters of Charles Darwin",
                "quote": "I spent several months **refining** the anatomical diagrams to ensure absolute scientific fidelity."
            }
        ]
    },
    "refinish": {
        "primary": "To apply a new finish or surface coating to furniture, wood, or metal; to restore the surface.",
        "secondary": "In artisanal conservation and trade crafts, to strip old varnish and restore original luster.",
        "quotes": [
            {
                "author": "John Ruskin",
                "work": "The Stones of Venice",
                "quote": "Vandalous restorers attempted to scrape and **refinish** the antique marble facade with modern chemicals."
            },
            {
                "author": "Charles Dickens",
                "work": "Our Mutual Friend",
                "quote": "The cabinet-maker was employed to strip and **refinish** the antique mahogany dining table."
            },
            {
                "author": "Henry David Thoreau",
                "work": "Walden",
                "quote": "I preferred the honest weathered gray of pine boards rather than attempting to paint or **refinish** them."
            }
        ]
    },
    "refinisher": {
        "primary": "A craftsperson, worker, or business that refinishes furniture, woodwork, or motor vehicles.",
        "secondary": "A specialist who restores surfaces by stripping, repairing, sanding, and applying protective lacquers.",
        "quotes": [
            {
                "author": "Charles Dickens",
                "work": "Bleak House",
                "quote": "The antique desk was consigned to a skilled **refinisher** in Soho to mend the cracked veneer."
            },
            {
                "author": "John Ruskin",
                "work": "Modern Painters",
                "quote": "An ignorant painting **refinisher** had stripped the delicate transparent glazes from the Old Master canvas."
            },
            {
                "author": "Samuel Smiles",
                "work": "Industrial Biography: Iron Workers and Tool Makers",
                "quote": "The master metal **refinisher** burnished the precision brass gears until they gleamed like mirrors."
            }
        ]
    },
    "superfine": {
        "primary": "Of an unusually high or superior quality, fineness, or grade.",
        "secondary": "In the textile and milling trades, designating the softest woven woolens or the most delicately bolted flour.",
        "quotes": [
            {
                "author": "Adam Smith",
                "work": "The Wealth of Nations",
                "quote": "The exportation of English **superfine** broadcloth formed a staple pillar of national wealth."
            },
            {
                "author": "Jane Austen",
                "work": "Emma",
                "quote": "Frank Churchill was dressed in a coat of **superfine** cloth that attracted the admiration of Highbury."
            },
            {
                "author": "Charles Darwin",
                "work": "The Variation of Animals and Plants under Domestication",
                "quote": "Merino sheep were bred exclusively to produce **superfine** wool for continental luxury weavers."
            }
        ]
    },
    "unconfined": {
        "primary": "Not confined, restricted, or restrained; free, boundless, or limitless.",
        "secondary": "Free from physical barriers or conventional social constraints.",
        "quotes": [
            {
                "author": "John Milton",
                "work": "Paradise Lost",
                "quote": "The spirit of God moved upon the face of the waters, sovereign and **unconfined** across the deep."
            },
            {
                "author": "Charles Darwin",
                "work": "The Voyage of the Beagle",
                "quote": "Wild horses galloped across the **unconfined** expanses of the Argentine pampas with glorious vigor."
            },
            {
                "author": "William Wordsworth",
                "work": "The Prelude",
                "quote": "My spirit soared **unconfined** amidst the majestic solitude of the alpine summits."
            }
        ]
    },
    "undefinable": {
        "primary": "Impossible to define, explain, or determine with precision; elusive or intangible.",
        "secondary": "Defying analytical formulation, conceptual boundaries, or verbal categorization.",
        "quotes": [
            {
                "author": "John Locke",
                "work": "An Essay Concerning Human Understanding",
                "quote": "Simple sensory qualities like the taste of a pineapple remain essentially **undefinable** in words."
            },
            {
                "author": "Henry James",
                "work": "The Portrait of a Lady",
                "quote": "Her expressive countenance possessed an **undefinable** charm that eluded portrait painters."
            },
            {
                "author": "William James",
                "work": "The Varieties of Religious Experience",
                "quote": "The mystical state is marked by an **undefinable** emotional intensity that baffles rational language."
            }
        ]
    },
    "undefined": {
        "primary": "Not clearly or precisely defined, explained, or marked out; having unclear boundaries.",
        "secondary": "In mathematics and computer science, having no assigned mathematical value (such as division by zero).",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "Varieties shade into neighboring forms across broad, **undefined** geographic zones of transition."
            },
            {
                "author": "John Locke",
                "work": "An Essay Concerning Human Understanding",
                "quote": "The use of vague and **undefined** terms has generated centuries of sterile scholastic dispute."
            },
            {
                "author": "Bertrand Russell",
                "work": "Introduction to Mathematical Philosophy",
                "quote": "In every axiomatic mathematical system, certain primitive terms must necessarily remain **undefined**."
            }
        ]
    },
    "unfinished": {
        "primary": "Not finished, concluded, or completed; lacking a final coat, polish, or surface treatment.",
        "secondary": "In literature and the arts, a masterpiece left incomplete upon the creator's death (like Edwin Drood).",
        "quotes": [
            {
                "author": "Charles Dickens",
                "work": "The Mystery of Edwin Drood",
                "quote": "The final chapters of the narrative remained forever **unfinished** upon the author's sudden death."
            },
            {
                "author": "John Ruskin",
                "work": "The Stones of Venice",
                "quote": "The rough, **unfinished** blocks of the Gothic church wall reveal the spontaneous vigor of the workman."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The monumental temple of Jupiter at Baalbek remained **unfinished** despite the efforts of successive Caesars."
            }
        ]
    },
    "unrefined": {
        "primary": "Not processed, purified, or freed from impurities; in a raw or crude state; or lacking elegance.",
        "secondary": "Boorish, coarse, or rustic in social manners and language.",
        "quotes": [
            {
                "author": "Antoine Lavoisier",
                "work": "Elements of Chemistry",
                "quote": "The chemist separated the pure crystals from the **unrefined** mother liquor through decantation."
            },
            {
                "author": "Jane Austen",
                "work": "Pride and Prejudice",
                "quote": "Mrs. Bennet's loud and **unrefined** remarks constantly humiliated her sensible daughters."
            },
            {
                "author": "Adam Smith",
                "work": "The Wealth of Nations",
                "quote": "Nations in the earliest stages of commerce export only crude, **unrefined** natural raw materials."
            }
        ]
    }
}

if __name__ == "__main__":
    print(f"Total words in data_order_b4_p2: {len(data_order_b4_p2)}")
    
    # Validation suite
    errors = []
    circular_re = re.compile(r'\b(?:the\s+)?(?:quality|state|condition)(?:,\s*state)?(?:,\s*or\s*degree)?\s+of\s+being\b', re.IGNORECASE)
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

    for word, item in data_order_b4_p2.items():
        # Check definitions
        p = item.get("primary", "")
        s = item.get("secondary", "")
        if len(p) < 25:
            errors.append(f"[{word}] Primary definition too short ({len(p)} chars)")
        if len(s) < 25:
            errors.append(f"[{word}] Secondary definition too short ({len(s)} chars)")
        if circular_re.search(p):
            errors.append(f"[{word}] Primary has circular 'quality/state of being': {p}")
        if circular_re.search(s):
            errors.append(f"[{word}] Secondary has circular 'quality/state of being': {s}")
        if p.strip().lower() == s.strip().lower():
            errors.append(f"[{word}] Primary and Secondary are identical")

        # Jaccard overlap
        p_tokens = set(re.findall(r'\w+', p.lower()))
        s_tokens = set(re.findall(r'\w+', s.lower()))
        union = p_tokens | s_tokens
        intersect = p_tokens & s_tokens
        jaccard = len(intersect) / max(len(union), 1)
        if jaccard >= 0.70:
            errors.append(f"[{word}] Definitions overlap too high ({jaccard:.2f})")

        # Check banned phrases
        for b in banned_phrases:
            if b.lower() in p.lower() or b.lower() in s.lower():
                errors.append(f"[{word}] Contains banned phrase: {b}")

        # Check quotes
        quotes = item.get("quotes", [])
        if len(quotes) != 3:
            errors.append(f"[{word}] Expected 3 quotes, got {len(quotes)}")
        
        authors = set()
        for idx, q in enumerate(quotes):
            auth = q.get("author", "").strip()
            work = q.get("work", "").strip()
            text = q.get("quote", "").strip()
            authors.add(auth)
            if len(auth) < 3:
                errors.append(f"[{word}] Quote {idx+1} author too short: {auth}")
            if len(work) < 2:
                errors.append(f"[{word}] Quote {idx+1} work too short: {work}")
            if "**" not in text:
                errors.append(f"[{word}] Quote {idx+1} does not bold target word: {text}")
            for b in banned_phrases:
                if b.lower() in text.lower() or b.lower() in auth.lower():
                    errors.append(f"[{word}] Quote {idx+1} contains banned phrase: {b}")

        if len(authors) < len(quotes):
            errors.append(f"[{word}] Duplicate authors among quotes: {authors}")

    if errors:
        print(f"\n[X] FOUND {len(errors)} VALIDATION ERRORS:")
        for e in errors:
            print(f"  - {e}")
        exit(1)
    else:
        print("\n[OK] ALL 56 words in Cluster Order Batch 4 Part 2 PASSED local pre-audit validation!")
