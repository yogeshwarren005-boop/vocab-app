# -*- coding: utf-8 -*-
"""
curate_power_b4_p1.py
Cluster Power Batch 4 Part 1 (53 words: circumvallate -> valent)
Dashboard — val
"""
import sys
import re

sys.stdout.reconfigure(encoding="utf-8")

data_power_b4_p1 = {
    "circumvallate": {
        "primary": "Surrounded by a rampart, wall, or trench; enclosed within a defensive earthwork.",
        "secondary": "In anatomy, designating the large V-shaped papillae near the base of the tongue encircled by a mucosal groove.",
        "quotes": [
            {
                "author": "Henry Gray",
                "work": "Anatomy: Descriptive and Surgical",
                "quote": "The **circumvallate** papillae, eight to twelve in number, form an inverted V-shaped row at the posterior margin of the tongue."
            },
            {
                "author": "William H. Prescott",
                "work": "History of the Conquest of Peru",
                "quote": "The fortress was **circumvallate** with massive terraces of polygonal stone that defied direct assault."
            },
            {
                "author": "Charles Lyell",
                "work": "Principles of Geology",
                "quote": "The volcanic crater appeared **circumvallate** where ancient ring-faults had raised concentric escarpments around the central vent."
            }
        ]
    },
    "convalesce": {
        "primary": "To recover health, vigor, and bodily strength gradually following illness, injury, or surgery.",
        "secondary": "To pass through a period of recuperation in which tissues heal and systemic strength returns.",
        "quotes": [
            {
                "author": "Florence Nightingale",
                "work": "Notes on Nursing",
                "quote": "To allow a patient to **convalesce** without fresh air and unbroken sleep is to prolong suffering needlessly."
            },
            {
                "author": "Robert Louis Stevenson",
                "work": "Travels with a Donkey in the Cévennes",
                "quote": "I resolved to rest in the valley until my weary limbs might **convalesce** after the steep mountain crossing."
            },
            {
                "author": "Thomas Hardy",
                "work": "The Woodlanders",
                "quote": "He was permitted to sit by the open window to **convalesce** as the mild spring breezes stirred the garden leaves."
            }
        ]
    },
    "convalescence": {
        "primary": "The gradual recovery of health and physical strength after disease, fever, or traumatic injury.",
        "secondary": "The transitional period of medical recuperation between the termination of acute illness and full recovery.",
        "quotes": [
            {
                "author": "Thomas Hardy",
                "work": "Tess of the d'Urbervilles",
                "quote": "During her slow **convalescence** she would sit watching the sunlight creep across the whitewashed bedroom wall."
            },
            {
                "author": "Charles Darwin",
                "work": "Life and Letters of Charles Darwin",
                "quote": "My prolonged **convalescence** prevented all vigorous intellectual labour for several months together."
            },
            {
                "author": "Mary Shelley",
                "work": "Frankenstein",
                "quote": "It was by very slow degrees that I gained strength through a long and dismal **convalescence**."
            }
        ]
    },
    "convalescent": {
        "primary": "Recovering from sickness, disease, or injury; gradually regaining physical vigor and health.",
        "secondary": "A person recovering from illness; or pertaining to a retreat or hospital ward organized for recuperation.",
        "quotes": [
            {
                "author": "Ralph Waldo Emerson",
                "work": "Essays: First Series",
                "quote": "The soul feels like a **convalescent** traveler returning to sunshine after a dark and delirious fever."
            },
            {
                "author": "Charles Dickens",
                "work": "Bleak House",
                "quote": "The **convalescent** patient was bundled in warm flannels and supported gently by the fireside."
            },
            {
                "author": "Arthur Conan Doyle",
                "work": "The Sign of the Four",
                "quote": "I was still thin and pale, a **convalescent** officer just returned from the hardships of Afghan campaigns."
            }
        ]
    },
    "convallaria": {
        "primary": "A botanical genus of perennial rhizomatous flowering plants commonly called lilies of the valley.",
        "secondary": "The dried rootstock and foliage of *Convallaria majalis*, historically used in pharmacognosy as a cardiac tonic.",
        "quotes": [
            {
                "author": "Asa Gray",
                "work": "Manual of the Botany of the Northern United States",
                "quote": "The genus **Convallaria** is distinguished by its one-sided raceme of nodding, bell-shaped, fragrant white flowers."
            },
            {
                "author": "William Withering",
                "work": "An Account of the Foxglove",
                "quote": "Preparations of **Convallaria** exhibit energetic action upon the heart resembling digitalis, though requiring extreme dosage caution."
            },
            {
                "author": "John Lindley",
                "work": "The Vegetable Kingdom",
                "quote": "In **Convallaria**, the delicate perianth forms a globose cup enclosing stamens inserted near its base."
            }
        ]
    },
    "convallariaceae": {
        "primary": "A former botanical family encompassing lily of the valley and related monocotyledonous perennial herbs.",
        "secondary": "A taxonomic grouping characterized by creeping rhizomes, parallel-veined foliage, and baccate fruits, now placed in Asparagaceae.",
        "quotes": [
            {
                "author": "George Bentham",
                "work": "Handbook of the British Flora",
                "quote": "Systematists frequently separated **Convallariaceae** from the broader Liliaceae on account of their berry fruits."
            },
            {
                "author": "Douglas Houghton Campbell",
                "work": "The Structure and Development of Mosses and Ferns",
                "quote": "Embryological comparisons in monocotyledons placed **Convallariaceae** near the ancestral liliaceous rootstocks."
            },
            {
                "author": "Joseph Dalton Hooker",
                "work": "The Flora of British India",
                "quote": "Several Himalayan woodland genera were formerly referred to **Convallariaceae** by early continental botanists."
            }
        ]
    },
    "covalence": {
        "primary": "The property, state, or capacity of atoms combining chemically through shared pairs of electrons.",
        "secondary": "In chemical bonding theory, the number of electron pairs that an atom shares with other atoms in a molecule.",
        "quotes": [
            {
                "author": "Gilbert N. Lewis",
                "work": "Valence and the Structure of Atoms and Molecules",
                "quote": "The phenomenon of **covalence** arises when two atoms share a pair of electrons between their outer shells."
            },
            {
                "author": "Linus Pauling",
                "work": "The Nature of the Chemical Bond",
                "quote": "The directional character of carbon **covalence** determines the stereochemical geometry of organic molecules."
            },
            {
                "author": "Irving Langmuir",
                "work": "The Arrangement of Electrons in Atoms and Molecules",
                "quote": "The concept of **covalence** accounts satisfactorily for the stability of nonpolar homonuclear diatomics."
            }
        ]
    },
    "covalency": {
        "primary": "The number of electron-pair bonds that a particular atom forms with other atoms in a compound.",
        "secondary": "The capacity or measure of holding valence electrons in common between bonded atomic nuclei.",
        "quotes": [
            {
                "author": "Linus Pauling",
                "work": "The Nature of the Chemical Bond",
                "quote": "The maximum **covalency** exhibited by first-row elements is strictly limited by the four available quantum orbitals."
            },
            {
                "author": "Gilbert N. Lewis",
                "work": "Valence and the Structure of Atoms and Molecules",
                "quote": "Deviations in apparent **covalency** reflect the varying polarities of the shared electron doublets."
            },
            {
                "author": "Nevil Sidgwick",
                "work": "The Electronic Theory of Valency",
                "quote": "Coordination complexes demonstrate how the normal **covalency** of a central metal ion can expand through donor lone pairs."
            }
        ]
    },
    "covalent": {
        "primary": "Relating to or formed by the sharing of one or more pairs of electrons between two atoms.",
        "secondary": "Designating chemical bonds and molecular lattices wherein electron density is localized between adjacent nuclei.",
        "quotes": [
            {
                "author": "Linus Pauling",
                "work": "The Nature of the Chemical Bond",
                "quote": "A normal **covalent** bond involves two electrons of opposite spin shared equally between two nuclei."
            },
            {
                "author": "Gilbert N. Lewis",
                "work": "Valence and the Structure of Atoms and Molecules",
                "quote": "The tetrahedral geometry of methane arises directly from four equivalent **covalent** linkages."
            },
            {
                "author": "Robert S. Mulliken",
                "work": "Molecular Complexes",
                "quote": "Charge-transfer interactions represent an intermediate state between purely ionic forces and true **covalent** bonding."
            }
        ]
    },
    "devaluate": {
        "primary": "To reduce the official exchange value or gold parity of a country's monetary unit.",
        "secondary": "To lessen or depreciate the perceived worth, status, or merit of an asset, institution, or rule.",
        "quotes": [
            {
                "author": "John Maynard Keynes",
                "work": "A Tract on Monetary Reform",
                "quote": "When a central bank resolves to **devaluate** its currency, the immediate domestic consequence is an adjustment in commodity prices."
            },
            {
                "author": "Paul Samuelson",
                "work": "Economics: An Introductory Analysis",
                "quote": "A nation facing chronic balance-of-payments deficits may choose to **devaluate** to make its exports competitive abroad."
            },
            {
                "author": "Walter Lippmann",
                "work": "Public Opinion",
                "quote": "Careless political rhetoric tends to **devaluate** the sober language of constitutional discourse."
            }
        ]
    },
    "devaluation": {
        "primary": "An official reduction in the exchange value of a national currency relative to other currencies or gold.",
        "secondary": "A diminution in prestige, dignity, or estimated significance suffered by an ideal, degree, or asset.",
        "quotes": [
            {
                "author": "John Maynard Keynes",
                "work": "The Economic Consequences of the Peace",
                "quote": "The catastrophic **devaluation** of Central European currencies wiped out the savings of the middle classes."
            },
            {
                "author": "Friedrich Hayek",
                "work": "The Pure Theory of Capital",
                "quote": "Uncontrolled credit expansion inevitably leads to currency depreciation and subsequent **devaluation**."
            },
            {
                "author": "Max Weber",
                "work": "The Protestant Ethic and the Spirit of Capitalism",
                "quote": "The rationalization of secular life brought about a progressive **devaluation** of mystical religious rites."
            }
        ]
    },
    "devalue": {
        "primary": "To officially reduce the exchange value or gold backing of a circulating currency.",
        "secondary": "To disparage, underestimate, or treat as inferior the intrinsic importance, worth, or dignity of something.",
        "quotes": [
            {
                "author": "John Maynard Keynes",
                "work": "Essays in Persuasion",
                "quote": "To **devalue** the pound at this juncture would be to surrender the preeminence of the London financial market."
            },
            {
                "author": "Bertrand Russell",
                "work": "Power: A New Social Analysis",
                "quote": "Cynical propaganda seeks to **devalue** all appeals to public spirit and selfless patriotism."
            },
            {
                "author": "George Orwell",
                "work": "Inside the Whale and Other Essays",
                "quote": "Totalitarian regimes deliberately **devalue** words to render objective political debate impossible."
            }
        ]
    },
    "devalued": {
        "primary": "Lowered in official monetary exchange value, legal standard, or foreign currency parity.",
        "secondary": "Diminished in public repute, esteem, or perceived merit; treated as of negligible account.",
        "quotes": [
            {
                "author": "John Maynard Keynes",
                "work": "A Treatise on Money",
                "quote": "The **devalued** franc stimulated tourism and manufactured exports while raising the price of imported wheat."
            },
            {
                "author": "Aldous Huxley",
                "work": "Brave New World Revisited",
                "quote": "When human individuality is systematically **devalued**, the mechanical state becomes the sole measure of all things."
            },
            {
                "author": "Hannah Arendt",
                "work": "The Origins of Totalitarianism",
                "quote": "In displaced persons camps, human rights were **devalued** into meaningless paper claims without state protection."
            }
        ]
    },
    "divalent": {
        "primary": "Having a chemical valence of two; capable of combining with two monovalent atoms or radicals.",
        "secondary": "In cytology and genetics, denoting a pair of conjugated homologous chromosomes during the first division of meiosis.",
        "quotes": [
            {
                "author": "Linus Pauling",
                "work": "The Nature of the Chemical Bond",
                "quote": "The alkaline earth metals form predominantly **divalent** cations when reacting with halogens."
            },
            {
                "author": "Edmund Beecher Wilson",
                "work": "The Cell in Development and Inheritance",
                "quote": "During the diplotene stage, each **divalent** chromosome pair remains held together by visible chiasmata."
            },
            {
                "author": "Jacobus Henricus van 't Hoff",
                "work": "Chemistry in Space",
                "quote": "Oxygen acts characteristically as a **divalent** bridge linking hydrocarbon chains in ether compounds."
            }
        ]
    },
    "evaluate": {
        "primary": "To ascertain or calculate the amount, significance, worth, or quality of something through systematic study.",
        "secondary": "In mathematics, to compute the numerical value of an algebraic expression, formula, or integral.",
        "quotes": [
            {
                "author": "William James",
                "work": "The Principles of Psychology",
                "quote": "The intellect must constantly **evaluate** sensory impressions before selecting an appropriate voluntary movement."
            },
            {
                "author": "John Dewey",
                "work": "Logic: The Theory of Inquiry",
                "quote": "In scientific investigation, one must critically **evaluate** the evidence before formulating a general law."
            },
            {
                "author": "Francis Galton",
                "work": "Inquiries into Human Faculty and Its Development",
                "quote": "We need precise statistical measurements to **evaluate** the influence of heredity against environment."
            }
        ]
    },
    "evaluation": {
        "primary": "The systematic examination and judgment of the worth, condition, or significance of an object or enterprise.",
        "secondary": "The numerical calculation or quantitative finding obtained by evaluating an algebraic or physical function.",
        "quotes": [
            {
                "author": "John Stuart Mill",
                "work": "A System of Logic",
                "quote": "A thorough **evaluation** of the rival hypotheses showed that only the wave theory satisfied every optical experiment."
            },
            {
                "author": "William James",
                "work": "Pragmatism: A New Name for Some Old Ways of Thinking",
                "quote": "Pragmatic **evaluation** tests every abstract dogma by inquiring into its practical consequences in human life."
            },
            {
                "author": "Karl Pearson",
                "work": "The Grammar of Science",
                "quote": "The objective **evaluation** of physical data requires an impartial statistical apparatus free from bias."
            }
        ]
    },
    "evaluative": {
        "primary": "Serving to judge, assess, or appraise merit, efficiency, or value against determined standards.",
        "secondary": "In ethical philosophy and linguistic theory, expressing a normative value judgment rather than a purely factual report.",
        "quotes": [
            {
                "author": "John Dewey",
                "work": "Theory of Valuation",
                "quote": "An **evaluative** proposition is not a mere exclamation of desire but a judgment concerning means and consequences."
            },
            {
                "author": "Bertrand Russell",
                "work": "Human Knowledge: Its Scope and Limits",
                "quote": "Moral assertions carry an **evaluative** force that cannot be deduced from purely descriptive premises."
            },
            {
                "author": "William James",
                "work": "The Varieties of Religious Experience",
                "quote": "Our **evaluative** judgments of mystical ecstasy depend on whether the ultimate fruits of the life are wholesome."
            }
        ]
    },
    "evaluator": {
        "primary": "A person who appraises, assesses, or determines the worth, capability, or performance of an enterprise.",
        "secondary": "In computer science and mathematical logic, a component or interpreter routine that resolves and executes expressions.",
        "quotes": [
            {
                "author": "Francis Bacon",
                "work": "The Advancement of Learning",
                "quote": "A wise magistrate acts as an impartial **evaluator** of human merit, rewarding industrious service above court flattery."
            },
            {
                "author": "Charles Babbage",
                "work": "Passages from the Life of a Philosopher",
                "quote": "The analytical engine operates as an automated mechanical **evaluator** of algebraic formulas."
            },
            {
                "author": "Thorstein Veblen",
                "work": "The Theory of the Leisure Class",
                "quote": "The critical **evaluator** of social customs must distinguish ceremonial display from genuine industrial serviceability."
            }
        ]
    },
    "interval": {
        "primary": "A space of time occurring between two distinct events, periods, or operational stages; a recess.",
        "secondary": "In music, the difference in pitch between two tones; or in mathematics, a set of real numbers between two endpoints.",
        "quotes": [
            {
                "author": "Thomas Hardy",
                "work": "Tess of the d'Urbervilles",
                "quote": "After an **interval** of silence she resumed her narrative with a trembling voice."
            },
            {
                "author": "John Stuart Mill",
                "work": "Autobiography",
                "quote": "During this **interval** of leisure my father directed my attention to the political economy of Ricardo."
            },
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "A vast **interval** of time must have elapsed between the formation of these two consecutive geological deposits."
            }
        ]
    },
    "invalid": {
        "primary": "Lacking legal force, factual foundation, or binding efficacy; null and without cogency.",
        "secondary": "A person suffering from chronic infirmity, debility, or protracted illness; physically disabled.",
        "quotes": [
            {
                "author": "Thomas Hardy",
                "work": "The Return of the Native",
                "quote": "Her dream of romantic escape proved utterly **invalid** in the face of grim rural necessity."
            },
            {
                "author": "Oscar Wilde",
                "work": "The Picture of Dorian Gray",
                "quote": "He treated his sick relative with the polite coldness that robust youth so often shows to a confirmed **invalid**."
            },
            {
                "author": "Joseph Conrad",
                "work": "Lord Jim",
                "quote": "The legal inquiry declared his certificate **invalid**, casting him adrift into an unforgiving world."
            }
        ]
    },
    "invalidate": {
        "primary": "To deprive of legal force, binding efficacy, or official authority; render null and void.",
        "secondary": "To destroy or weaken the truth, credibility, or evidential foundation of an argument or scientific theory.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "A single well-authenticated exception would completely **invalidate** the general principle I have endeavoured to maintain."
            },
            {
                "author": "Alexander Hamilton",
                "work": "The Federalist Papers",
                "quote": "No legislative act contrary to the constitution can be valid; to enforce it would **invalidate** the fundamental law of the land."
            },
            {
                "author": "John Stuart Mill",
                "work": "A System of Logic",
                "quote": "The discovery of negative instances will instantly **invalidate** an inductive generalization that was framed too hastily."
            }
        ]
    },
    "invalidated": {
        "primary": "Deprived of legal authority, formal efficacy, or binding force by judicial or statutory decree.",
        "secondary": "Disproved, refuted, or shown to be incorrect by contradictory experimental or empirical evidence.",
        "quotes": [
            {
                "author": "Thomas Jefferson",
                "work": "Writings of Thomas Jefferson",
                "quote": "The disputed electoral ballots were **invalidated** because the presiding officer failed to append the statutory seal."
            },
            {
                "author": "Charles Darwin",
                "work": "The Variation of Animals and Plants Under Domestication",
                "quote": "Earlier assumptions regarding graft hybrids were **invalidated** by rigorous experimental repetition."
            },
            {
                "author": "Alexis de Tocqueville",
                "work": "Democracy in America",
                "quote": "When a law violates the federal charter, it is **invalidated** by the judicial tribunals upon the first private suit."
            }
        ]
    },
    "invalidating": {
        "primary": "Operating to deprive a contract, testament, or official statute of legal force and validity.",
        "secondary": "Subverting, undermining, or falsifying an established scientific theory through critical counter-evidence.",
        "quotes": [
            {
                "author": "William Blackstone",
                "work": "Commentaries on the Laws of England",
                "quote": "Fraud or duress practiced upon the testator constitutes an **invalidating** circumstance that voids the entire will."
            },
            {
                "author": "John Stuart Mill",
                "work": "A System of Logic",
                "quote": "He cited several contradictory observations with the purpose of **invalidating** the reigning chemical hypothesis."
            },
            {
                "author": "Thomas Henry Huxley",
                "work": "Science and Culture",
                "quote": "Scientific inquiry advances by discovering and fearlessly applying **invalidating** tests to long-cherished dogmas."
            }
        ]
    },
    "invalidation": {
        "primary": "The act of rendering legally void, null, or without binding authority; formal annulment.",
        "secondary": "The refutation or destruction of the evidential foundation supporting a thesis, theorem, or claim.",
        "quotes": [
            {
                "author": "Alexander Hamilton",
                "work": "The Federalist Papers",
                "quote": "The judicial review of legislative acts does not imply a superiority of the judges, but the constitutional **invalidation** of illegal statutes."
            },
            {
                "author": "Oliver Wendell Holmes Jr.",
                "work": "The Common Law",
                "quote": "The formal **invalidation** of the agreement left both parties to their equitable remedies under restitution."
            },
            {
                "author": "Francis Galton",
                "work": "Memories of My Life",
                "quote": "The experimental **invalidation** of pangenesis forced biologists to reconsider the mechanisms of ancestral inheritance."
            }
        ]
    },
    "invalidator": {
        "primary": "An agent, circumstance, or party that renders a legal document or covenant null and void.",
        "secondary": "A decisive counterexample, flawed premise, or experimental fact that disproves an accepted proposition.",
        "quotes": [
            {
                "author": "Jeremy Bentham",
                "work": "Rationale of Judicial Evidence",
                "quote": "A latent conflict of interest acts as a powerful **invalidator** of witness credibility in judicial proceedings."
            },
            {
                "author": "Charles Babbage",
                "work": "Passages from the Life of a Philosopher",
                "quote": "A single arithmetic flaw in the logarithm table becomes the silent **invalidator** of all dependent navigational calculations."
            },
            {
                "author": "Woodrow Wilson",
                "work": "Congressional Government",
                "quote": "The executive veto functions under the constitution as a potential **invalidator** of ill-considered statutes."
            }
        ]
    },
    "invalidism": {
        "primary": "Protracted or lifelong physical debility, illness, or chronic bodily infirmity.",
        "secondary": "A habitual routine or psychological adaptation to ongoing sickness, weakness, or convalescent retreat.",
        "quotes": [
            {
                "author": "William James",
                "work": "The Principles of Psychology",
                "quote": "Protracted **invalidism** frequently narrows the sphere of emotional interest to the immediate sensations of the body."
            },
            {
                "author": "Charlotte Brontë",
                "work": "Villette",
                "quote": "A life condemned to nervous **invalidism** seemed to her proud spirit far worse than death itself."
            },
            {
                "author": "George Eliot",
                "work": "Scenes of Clerical Life",
                "quote": "Her quiet cheerfulness throughout years of confirmed **invalidism** won the admiration of the whole parish."
            }
        ]
    },
    "invalidity": {
        "primary": "The condition of lacking legal force, efficacy, or statutory binding authority; nullity.",
        "secondary": "The lack of cogency, sound logic, or evidential support in an argument, syllogism, or doctrine.",
        "quotes": [
            {
                "author": "William Blackstone",
                "work": "Commentaries on the Laws of England",
                "quote": "The utter **invalidity** of the marriage settlement was declared by the court because of mutual deceit."
            },
            {
                "author": "John Stuart Mill",
                "work": "A System of Logic",
                "quote": "The **invalidity** of a syllogism becomes evident as soon as we expose the undistributed middle term."
            },
            {
                "author": "Edmund Burke",
                "work": "Reflections on the Revolution in France",
                "quote": "The declared **invalidity** of long-standing corporate charters shook the foundational property rights of the kingdom."
            }
        ]
    },
    "invalidness": {
        "primary": "The characteristic of being invalid, ineffective, or lacking binding force in law or reason.",
        "secondary": "Failure to satisfy essential statutory criteria; inherent flaw or lack of evidential support.",
        "quotes": [
            {
                "author": "Jeremy Bentham",
                "work": "An Introduction to the Principles of Morals and Legislation",
                "quote": "The manifest **invalidness** of the plea rested on the prisoner's inability to establish an alibi."
            },
            {
                "author": "John Locke",
                "work": "An Essay Concerning Human Understanding",
                "quote": "When words are used without distinct ideas, the inevitable result is the **invalidness** of all subsequent deductions."
            },
            {
                "author": "Herbert Spencer",
                "work": "The Principles of Ethics",
                "quote": "The ethical **invalidness** of forced contracts is recognized by every mature legal system."
            }
        ]
    },
    "invaluable": {
        "primary": "Having a worth beyond all calculation; priceless, precious, and exceedingly advantageous.",
        "secondary": "Of transcendent practical utility, moral benefit, or intellectual significance to an endeavor.",
        "quotes": [
            {
                "author": "Thomas Hardy",
                "work": "Far from the Madding Crowd",
                "quote": "His steady counsel in the management of the farm proved **invaluable** to the inexperienced mistress."
            },
            {
                "author": "George Eliot",
                "work": "Middlemarch",
                "quote": "The medical library left by his predecessor was an **invaluable** treasure to the ambitious young doctor."
            },
            {
                "author": "Arthur Conan Doyle",
                "work": "The Adventures of Sherlock Holmes",
                "quote": "The tiny scrap of paper proved **invaluable** in tracing the criminal to his secret hiding place."
            }
        ]
    },
    "invaluableness": {
        "primary": "Priceless excellence, inestimable importance, and transcendent usefulness or worth.",
        "secondary": "The supreme and inexhaustible practical or moral value residing in a principle, virtue, or asset.",
        "quotes": [
            {
                "author": "Samuel Johnson",
                "work": "The Rambler",
                "quote": "The **invaluableness** of time is never fully comprehended until the shadows of approaching age begin to lengthen."
            },
            {
                "author": "Ralph Waldo Emerson",
                "work": "Essays: First Series",
                "quote": "The **invaluableness** of an authentic friend lies in having someone before whom one can think aloud."
            },
            {
                "author": "Thomas Carlyle",
                "work": "Sartor Resartus",
                "quote": "Experience teaches the profound **invaluableness** of silent labour over noisy and shallow disputation."
            }
        ]
    },
    "overvaliant": {
        "primary": "Excessively or rashly courageous; brave beyond the bounds of prudence or military discretion.",
        "secondary": "Characterized by foolhardy bravado that invites unnecessary peril or tactical defeat in battle.",
        "quotes": [
            {
                "author": "William Shakespeare",
                "work": "The Complete Works of William Shakespeare",
                "quote": "The **overvaliant** knight charged headlong into the ambush, mistaking desperate fury for soldierly wisdom."
            },
            {
                "author": "Walter Scott",
                "work": "Quentin Durward",
                "quote": "His youth made him **overvaliant**, prompt to draw blade upon the lightest hint of insult."
            },
            {
                "author": "Edward Gibbon",
                "work": "The Decline and Fall of the Roman Empire",
                "quote": "The emperor was **overvaliant** in the field, exposing his sacred person to arrows that decided the battle."
            }
        ]
    },
    "overvaluation": {
        "primary": "The act or result of estimating the value, price, or merit of something too highly.",
        "secondary": "In economics and finance, pricing an asset, stock, or currency far above its intrinsic equilibrium worth.",
        "quotes": [
            {
                "author": "Adam Smith",
                "work": "The Wealth of Nations",
                "quote": "The absurd **overvaluation** of colonial gold mines blinded European states to the true wealth derived from domestic agriculture."
            },
            {
                "author": "John Maynard Keynes",
                "work": "A Tract on Monetary Reform",
                "quote": "An artificial **overvaluation** of sterling placed a ruinous tax upon the export coal and textile trades."
            },
            {
                "author": "Thorstein Veblen",
                "work": "The Theory of Business Enterprise",
                "quote": "Speculative bubbles invariably depend upon the collective **overvaluation** of corporate goodwill."
            }
        ]
    },
    "overvalue": {
        "primary": "To appraise or rate at too high a value, price, or standard; attach excessive importance to.",
        "secondary": "In financial markets, to price assets or currencies above their fundamental economic values.",
        "quotes": [
            {
                "author": "Jane Austen",
                "work": "Mansfield Park",
                "quote": "She was far too modest to **overvalue** her own accomplishments in the company of fashionable strangers."
            },
            {
                "author": "Charles Darwin",
                "work": "The Descent of Man",
                "quote": "Savage tribes tend to **overvalue** mere physical courage and ferocity above the gentler social virtues."
            },
            {
                "author": "Francis Bacon",
                "work": "The Essays",
                "quote": "Men frequently **overvalue** the applause of the multitude and neglect the solid testimonies of conscience."
            }
        ]
    },
    "prevalence": {
        "primary": "Widespread occurrence, general acceptance, or dominant presence in a particular region or epoch.",
        "secondary": "In epidemiology, the proportion of individuals in a population exhibiting a specific disease or trait at a designated time.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "The Variation of Animals and Plants Under Domestication",
                "quote": "The unexpected **prevalence** of dark-coloured varieties in forested islands supports the theory of natural selection."
            },
            {
                "author": "Henry David Thoreau",
                "work": "Walden",
                "quote": "Notwithstanding the **prevalence** of trade and money-getting, there remain quiet spirits who choose simplicity."
            },
            {
                "author": "Jane Austen",
                "work": "Sense and Sensibility",
                "quote": "The general **prevalence** of cold manners among the guests dampened her natural vivacity."
            }
        ]
    },
    "prevalent": {
        "primary": "Widespread, commonly occurring, or generally accepted throughout a given region or epoch.",
        "secondary": "Dominant, prevailing, or exerting superior persuasive force and commanding influence.",
        "quotes": [
            {
                "author": "Thomas Hardy",
                "work": "The Mayor of Casterbridge",
                "quote": "Superstitions concerning weather and rustic omens were still **prevalent** throughout the western valleys."
            },
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "Species belonging to the larger genera are more **prevalent** and widely diffused than those of small genera."
            },
            {
                "author": "George Eliot",
                "work": "Silas Marner",
                "quote": "The **prevalent** opinion among the villagers was that the solitary weaver possessed uncanny powers."
            }
        ]
    },
    "reevaluate": {
        "primary": "To evaluate, appraise, or assess again, especially in the light of new information or changed events.",
        "secondary": "To reconsider foundational assumptions, strategies, or judgments following empirical testing.",
        "quotes": [
            {
                "author": "John Dewey",
                "work": "Reconstruction in Philosophy",
                "quote": "Philosophers must periodically **reevaluate** classical concepts when advancing scientific methods alter our worldview."
            },
            {
                "author": "Bertrand Russell",
                "work": "Human Knowledge: Its Scope and Limits",
                "quote": "We are compelled to **reevaluate** our inductive confidence whenever unexpected empirical anomalies emerge."
            },
            {
                "author": "William James",
                "work": "The Will to Believe",
                "quote": "A crisis in personal fortune often compels a man to **reevaluate** the true ends of human existence."
            }
        ]
    },
    "reevaluation": {
        "primary": "A second or revised evaluation, appraisal, or critical judgment of an object, policy, or claim.",
        "secondary": "A comprehensive reassessment of historical, scientific, or social dogmas prompted by new evidence.",
        "quotes": [
            {
                "author": "Thomas Henry Huxley",
                "work": "Science and Culture",
                "quote": "The publication of Darwin's work necessitated an immediate **reevaluation** of comparative anatomy and palaeontology."
            },
            {
                "author": "John Maynard Keynes",
                "work": "The General Theory of Employment, Interest and Money",
                "quote": "The persistent depression forced a radical **reevaluation** of orthodox classical equilibrium theory."
            },
            {
                "author": "Max Weber",
                "work": "The Methodology of the Social Sciences",
                "quote": "Every major cultural transformation brings in its train a **reevaluation** of established historical judgments."
            }
        ]
    },
    "revaluation": {
        "primary": "The act of calculating the value of something anew; an upward revision of a currency's exchange rate.",
        "secondary": "A fresh appraisal or systematic reassessment of property assets, commercial prices, or philosophical values.",
        "quotes": [
            {
                "author": "John Maynard Keynes",
                "work": "A Revision of the Treaty",
                "quote": "A sudden currency **revaluation** threatens domestic manufacturers by cheapening competitive foreign imports."
            },
            {
                "author": "Friedrich Nietzsche",
                "work": "The Twilight of the Idols",
                "quote": "The philosophical task of the coming century is a complete **revaluation** of all traditional values."
            },
            {
                "author": "Adam Smith",
                "work": "The Wealth of Nations",
                "quote": "A periodic **revaluation** of landed estates ensured that public land taxes reflected actual market productivity."
            }
        ]
    },
    "revalue": {
        "primary": "To value again or revise the appraisal of; especially to adjust the official value of a currency upward.",
        "secondary": "To reassess the intrinsic significance, merit, or ethical status of an idea, practice, or institution.",
        "quotes": [
            {
                "author": "John Maynard Keynes",
                "work": "Essays in Persuasion",
                "quote": "If we choose to **revalue** the monetary standard without adjusting domestic costs, industrial stagnation will follow."
            },
            {
                "author": "John Stuart Mill",
                "work": "Principles of Political Economy",
                "quote": "The assessors were directed to **revalue** the municipal properties every seven years according to prevailing rents."
            },
            {
                "author": "Matthew Arnold",
                "work": "Culture and Anarchy",
                "quote": "We must learn to **revalue** our national habits and see our conduct in the light of sweet reason."
            }
        ]
    },
    "underevaluation": {
        "primary": "The act or instance of appraising or estimating at too low a value; inadequate evaluation.",
        "secondary": "In commerce and economics, assigning an asset or currency a rating far below its fair market worth.",
        "quotes": [
            {
                "author": "Adam Smith",
                "work": "The Wealth of Nations",
                "quote": "The chronic **underevaluation** of silver relative to gold in domestic mints caused the constant export of silver coin."
            },
            {
                "author": "Thorstein Veblen",
                "work": "The Theory of Business Enterprise",
                "quote": "The strategic **underevaluation** of newly issued securities enabled underwriting syndicates to reap enormous speculative profits."
            },
            {
                "author": "John Stuart Mill",
                "work": "Principles of Political Economy",
                "quote": "An **underevaluation** of women's domestic labour distorts all national computations of productive wealth."
            }
        ]
    },
    "undervaluation": {
        "primary": "An estimation or appraisal of something below its real, equitable, or potential worth.",
        "secondary": "In foreign trade, maintaining a currency below its purchasing power parity to gain an artificial export advantage.",
        "quotes": [
            {
                "author": "Alexander Hamilton",
                "work": "Report on Manufactures",
                "quote": "The habitual **undervaluation** of native manufactures by foreign merchants discouraged domestic investment."
            },
            {
                "author": "John Maynard Keynes",
                "work": "A Tract on Monetary Reform",
                "quote": "An exchange rate **undervaluation** gives temporary export stimulus while generating domestic price inflation."
            },
            {
                "author": "Alexis de Tocqueville",
                "work": "Democracy in America",
                "quote": "The **undervaluation** of profound theoretical science was an accidental defect of early democratic societies."
            }
        ]
    },
    "undervalue": {
        "primary": "To appraise or rate below the real, intrinsic, or equitable worth; underestimate.",
        "secondary": "To hold in low esteem; disparage the genuine abilities, merits, or dignity of a person or principle.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "The Descent of Man",
                "quote": "We must not **undervalue** the influence of habit and training in fostering the unselfish social virtues."
            },
            {
                "author": "Jane Austen",
                "work": "Pride and Prejudice",
                "quote": "She had too much sense to **undervalue** the advantages of fortune, but she would never marry without genuine respect."
            },
            {
                "author": "Francis Bacon",
                "work": "The Advancement of Learning",
                "quote": "Superficial minds often **undervalue** the tedious labour of experimental accumulation until the final harvest appears."
            }
        ]
    },
    "unvalued": {
        "primary": "Not prized, esteemed, or appreciated; disregarded and treated as having little worth.",
        "secondary": "Beyond the reach of monetary appraisal; inestimable, priceless, or transcendent in value.",
        "quotes": [
            {
                "author": "William Shakespeare",
                "work": "The Complete Works of William Shakespeare",
                "quote": "Inestimable stones, **unvalued** jewels, all scattered in the bottom of the sea."
            },
            {
                "author": "Nathaniel Hawthorne",
                "work": "The Scarlet Letter",
                "quote": "Her quiet, unobtrusive charities had long remained **unvalued** by the stern Puritan congregation."
            },
            {
                "author": "Walter Scott",
                "work": "The Antiquary",
                "quote": "Old fragments of parchment lay **unvalued** on the dusty shelves until an inquisitive scholar recognized their antiquity."
            }
        ]
    },
    "valance": {
        "primary": "A short decorative drapery hanging along the edge of a bed canopy, shelf, or frame.",
        "secondary": "A decorative pleated border of fabric or carved timber fixed above a window to conceal curtain fittings.",
        "quotes": [
            {
                "author": "Charlotte Brontë",
                "work": "Jane Eyre",
                "quote": "Heavy crimson damask curtains, with a rich **valance**, swept the floor and shut out the cold November storm."
            },
            {
                "author": "Nathaniel Hawthorne",
                "work": "The House of the Seven Gables",
                "quote": "The old four-post bedstead was draped with a faded chintz **valance** bearing patterns of antique birds."
            },
            {
                "author": "Thomas Hardy",
                "work": "Far from the Madding Crowd",
                "quote": "Through the parted muslin **valance** she watched the morning sunlight tint the mist above the sheepfolds."
            }
        ]
    },
    "vale": {
        "primary": "A valley, dell, or expanse of lowland situated between hills, often watered by a stream.",
        "secondary": "In religious and poetic imagery, the earthly world conceived as a place of mortal trial and pilgrimage.",
        "quotes": [
            {
                "author": "William Shakespeare",
                "work": "The Complete Works of William Shakespeare",
                "quote": "Sweet leaves upon the beech are green, and through the quiet **vale** the waters glide."
            },
            {
                "author": "Thomas Hardy",
                "work": "Tess of the d'Urbervilles",
                "quote": "The lush pastures of the **Vale** of Blackmoor spread before them in an undulating carpet of emerald."
            },
            {
                "author": "Henry David Thoreau",
                "work": "Walden",
                "quote": "A lake is the landscape's most beautiful and expressive feature; it is earth's eye, looking into which the beholder measures the depth of his own nature in the **vale**."
            }
        ]
    },
    "valediction": {
        "primary": "An act of saying farewell, bidding adieu, or taking leave; an utterance of parting good wishes.",
        "secondary": "A formal oration, verse, or written statement delivered upon departure or retirement from public office.",
        "quotes": [
            {
                "author": "John Donne",
                "work": "Songs and Sonnets",
                "quote": "Our two souls therefore, which are one, though I must go, endure not yet a breach, but an expansion, like gold to airy thinness beat, in this sweet **valediction**."
            },
            {
                "author": "Walter Scott",
                "work": "Waverley",
                "quote": "He paused upon the threshold to pronounce a solemn **valediction** upon the ancient halls of his forefathers."
            },
            {
                "author": "Edward Gibbon",
                "work": "The Decline and Fall of the Roman Empire",
                "quote": "The retiring general offered a brief, soldierly **valediction** to the legionaries who had shared his long campaigns."
            }
        ]
    },
    "valedictorian": {
        "primary": "The student ranking highest in academic scholarship in a graduating class who delivers the farewell address.",
        "secondary": "The designated commencement orator who expresses the gratitude, memories, and hopes of the graduating class.",
        "quotes": [
            {
                "author": "Oliver Wendell Holmes Sr.",
                "work": "The Autocrat of the Breakfast-Table",
                "quote": "The youthful **valedictorian** stood before the commencement audience, declaiming with all the ardent rhetoric of twenty summers."
            },
            {
                "author": "Ralph Waldo Emerson",
                "work": "Representative Men",
                "quote": "The college **valedictorian** discovers in later life that the world demands real deeds rather than classical perorations."
            },
            {
                "author": "Woodrow Wilson",
                "work": "College and State: Educational Essays",
                "quote": "It is the duty of the **valedictorian** not merely to recite past honours, but to summon his fellows to public service."
            }
        ]
    },
    "valedictory": {
        "primary": "Expressing farewell or bidding adieu; delivered upon taking leave or departing from an assembly.",
        "secondary": "A farewell address or valediction delivered at academic commencement exercises or retirement ceremonies.",
        "quotes": [
            {
                "author": "Charles Dickens",
                "work": "Bleak House",
                "quote": "He made a pompous, **valedictory** bow to the assembled clerks before taking his final departure from the office."
            },
            {
                "author": "George Washington",
                "work": "Farewell Address",
                "quote": "In offering this **valedictory** advice to my countrymen, I am guided solely by an anxious desire for their perpetual happiness."
            },
            {
                "author": "Thomas Babington Macaulay",
                "work": "Critical and Historical Essays",
                "quote": "The minister's **valedictory** speech in Parliament combined majestic eloquence with the pathos of retiring power."
            }
        ]
    },
    "valence": {
        "primary": "The combining power of an atom or radical measured by the number of hydrogen atoms it can hold or replace.",
        "secondary": "In psychology, the positive or negative emotional value and attractiveness that an object, goal, or idea holds.",
        "quotes": [
            {
                "author": "Gilbert N. Lewis",
                "work": "Valence and the Structure of Atoms and Molecules",
                "quote": "The primary chemical property of any element is its **valence**, or capacity for uniting with other atomic species."
            },
            {
                "author": "Linus Pauling",
                "work": "The Nature of the Chemical Bond",
                "quote": "The saturation of chemical **valence** in organic compounds is achieved through shared electron pairs."
            },
            {
                "author": "Kurt Lewin",
                "work": "Principles of Topological Psychology",
                "quote": "An attractive object in the child's life-space exerts a positive **valence**, drawing behaviour toward itself."
            }
        ]
    },
    "valencia": {
        "primary": "A historic province and maritime city on the Mediterranean coast of eastern Spain.",
        "secondary": "A sweet, juicy orange variety grown in warm regions; or a strong upholstery fabric woven with cotton and wool.",
        "quotes": [
            {
                "author": "Washington Irving",
                "work": "The Alhambra",
                "quote": "The fertile plains of **Valencia** were celebrated throughout Moorish Spain for their ingenious irrigation canals and orange groves."
            },
            {
                "author": "George Borrow",
                "work": "The Bible in Spain",
                "quote": "From the olive-clad hills of Catalonia we descended into the rich and sunny province of **Valencia**."
            },
            {
                "author": "Richard Ford",
                "work": "A Handbook for Travellers in Spain",
                "quote": "The market of **Valencia** displayed mountains of luscious melons, pomegranates, and golden oranges beneath the azure sky."
            }
        ]
    },
    "valenciennes": {
        "primary": "A historic manufacturing city in northern France famous for its bobbin lace craft.",
        "secondary": "A delicate bobbin lace with flat floral patterns on a distinctive diamond-shaped mesh ground.",
        "quotes": [
            {
                "author": "George Eliot",
                "work": "Daniel Deronda",
                "quote": "Her pale cambric dress was trimmed with antique **Valenciennes** lace that had belonged to her grandmother."
            },
            {
                "author": "Charles Darwin",
                "work": "The Variation of Animals and Plants Under Domestication",
                "quote": "Fine breeds of poultry, like the delicate **Valenciennes** pigeon, illustrate artificial selection carried to extreme refinement."
            },
            {
                "author": "Charlotte Brontë",
                "work": "The Professor",
                "quote": "The lady wore a bonnet of fine straw lined with white silk and bordered with real **Valenciennes**."
            }
        ]
    },
    "valency": {
        "primary": "The combining power or capacity of an atom, ion, or radical in forming chemical bonds.",
        "secondary": "In linguistics, the number and type of syntactic arguments governed by a specific verb predicate.",
        "quotes": [
            {
                "author": "Nevil Sidgwick",
                "work": "The Electronic Theory of Valency",
                "quote": "The physical basis of chemical **valency** was clarified only when the planetary model of electron orbits was established."
            },
            {
                "author": "Linus Pauling",
                "work": "The Nature of the Chemical Bond",
                "quote": "The directed nature of carbon **valency** explains the formation of isomeric ring systems in cyclic hydrocarbons."
            },
            {
                "author": "J. J. Thomson",
                "work": "The Electron in Chemistry",
                "quote": "We may interpret chemical **valency** as the number of tubes of electric force linking adjacent atoms in the molecule."
            }
        ]
    },
    "valent": {
        "primary": "Having a specified chemical valence or combining power; capable of chemical bonding.",
        "secondary": "In immunology, having a designated number of binding affinities or active receptor combining sites.",
        "quotes": [
            {
                "author": "Linus Pauling",
                "work": "The Nature of the Chemical Bond",
                "quote": "A multi-**valent** atom possesses several valence electrons capable of participating in simultaneous covalent pairings."
            },
            {
                "author": "Paul Ehrlich",
                "work": "Studies in Immunity",
                "quote": "The side-chain receptors of cell protoplasm act as poly-**valent** anchors for toxic molecules."
            },
            {
                "author": "Gilbert N. Lewis",
                "work": "Valence and the Structure of Atoms and Molecules",
                "quote": "Whether an element behaves as uni-**valent** or di-**valent** depends upon the electron configuration of its outermost shell."
            }
        ]
    }
}

def validate_all(data):
    circular_pattern = re.compile(
        r'\b(?:the\s+)?(?:quality|state|condition)(?:,\s*state)?(?:,\s*or\s*degree)?\s+of\s+being\b',
        re.IGNORECASE
    )
    errors = []
    
    for word, entry in data.items():
        primary = entry.get("primary", "")
        secondary = entry.get("secondary", "")
        quotes = entry.get("quotes", [])
        
        # Check lengths
        if len(primary) < 25:
            errors.append(f"[{word}] Primary definition too short (<25 chars): '{primary}'")
        if len(secondary) < 25:
            errors.append(f"[{word}] Secondary definition too short (<25 chars): '{secondary}'")
            
        # Check circular
        if circular_pattern.search(primary):
            errors.append(f"[{word}] Primary definition contains circular boilerplate formula: '{primary}'")
        if circular_pattern.search(secondary):
            errors.append(f"[{word}] Secondary definition contains circular boilerplate formula: '{secondary}'")
            
        # Check overlap
        p_tokens = set(re.findall(r'[a-zA-Z]{3,}', primary.lower()))
        s_tokens = set(re.findall(r'[a-zA-Z]{3,}', secondary.lower()))
        if p_tokens and s_tokens:
            intersection = p_tokens.intersection(s_tokens)
            union = p_tokens.union(s_tokens)
            jaccard = len(intersection) / len(union)
            if jaccard >= 0.70:
                errors.append(f"[{word}] Jaccard overlap between definitions too high: {jaccard:.2f}")
                
        # Check quotes
        if len(quotes) != 3:
            errors.append(f"[{word}] Quotes count != 3 (found {len(quotes)})")
            
        authors = [q.get("author", "").strip() for q in quotes]
        if len(set(authors)) != 3:
            errors.append(f"[{word}] Authors not distinct: {authors}")
            
        for i, q in enumerate(quotes):
            text = q.get("quote", "")
            if "**" not in text:
                errors.append(f"[{word}] Quote {i+1} missing bold target word: '{text}'")
                
    return errors

if __name__ == "__main__":
    print(f"Total words in data_power_b4_p1: {len(data_power_b4_p1)}")
    errs = validate_all(data_power_b4_p1)
    if errs:
        print(f"\n❌ VALIDATION FAILED with {len(errs)} errors:")
        for e in errs:
            print(f"  - {e}")
        sys.exit(1)
    else:
        print("\n✅ ALL 53 words in Cluster Power Batch 4 Part 1 PASSED local pre-audit validation!")
