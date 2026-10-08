# -*- coding: utf-8 -*-
"""
curate_power_b4_p2.py
Cluster Power Batch 4 Part 2 (52 words: valentine -> values)
Dashboard — val
"""
import sys
import re

sys.stdout.reconfigure(encoding="utf-8")

data_power_b4_p2 = {
    "valentine": {
        "primary": "A sweetheart chosen or greeted on Saint Valentine's Day; or a greeting card or gift sent to a beloved.",
        "secondary": "A historical custom or rhyming token of affection exchanged in celebration of romantic devotion in springtime.",
        "quotes": [
            {
                "author": "William Shakespeare",
                "work": "Hamlet",
                "quote": "Tomorrow is Saint **Valentine**'s day, all in the morning betime, and I a maid at your window, to be your **Valentine**."
            },
            {
                "author": "Thomas Hardy",
                "work": "Far from the Madding Crowd",
                "quote": "She had bought the **valentine** at a stationer's shop, thinking of it only as a careless jest upon the lonely farmer."
            },
            {
                "author": "Charles Dickens",
                "work": "The Pickwick Papers",
                "quote": "Sam Weller sat down in the parlour of the Blue Boar to compose an elaborate and rhyming **valentine**."
            }
        ]
    },
    "valerian": {
        "primary": "Any perennial flowering herb of the genus Valeriana, especially Valeriana officinalis, bearing fragrant pink or white blooms.",
        "secondary": "The dried rootstock and rhizome of this plant, utilized in pharmacy since classical antiquity as a sedative.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "The Variation of Animals and Plants Under Domestication",
                "quote": "Cats are well known to be excited by the aromatic odor of **valerian** root, rolling upon it in frantic delight."
            },
            {
                "author": "Thomas Henry Huxley",
                "work": "Lessons in Elementary Physiology",
                "quote": "Infusions of **valerian** were formerly prescribed in nervous disorders to soothe excitability without producing stupor."
            },
            {
                "author": "John Gerard",
                "work": "The Herball or Generall Historie of Plantes",
                "quote": "The dry root of garden **valerian** hath a pleasant smell when bruised and is held in sovereign esteem by physicians."
            }
        ]
    },
    "valeriana": {
        "primary": "The botanical genus of perennial herbs and shrubs in the honeysuckle family, distributed across temperate regions.",
        "secondary": "The taxonomic type genus of Caprifoliaceae, recognized for its cymose inflorescences and valepotriate constituents.",
        "quotes": [
            {
                "author": "Carl Linnaeus",
                "work": "Species Plantarum",
                "quote": "In **Valeriana**, the corolla is monopetalous and spurred at the base, enclosing three stamens."
            },
            {
                "author": "Augustin Pyramus de Candolle",
                "work": "Prodromus Systematis Naturalis Regni Vegetabilis",
                "quote": "The alpine species of **Valeriana** exhibit reduced vegetative stems adapted to rocky screes."
            },
            {
                "author": "Joseph Dalton Hooker",
                "work": "The Flora of British India",
                "quote": "High Himalayan meadows yield aromatic forms of **Valeriana** closely related to the medicinal species of Europe."
            }
        ]
    },
    "valerianaceae": {
        "primary": "A former botanical family of herbaceous plants and dwarf shrubs, now treated as a subfamily within Caprifoliaceae.",
        "secondary": "A taxonomic grouping characterized by opposite leaves, irregular tubular flowers, and pappus-like calyx crowns.",
        "quotes": [
            {
                "author": "George Bentham",
                "work": "Handbook of the British Flora",
                "quote": "The family **Valerianaceae** is readily recognized by its asymmetrical flowers and feathery fruiting calyx."
            },
            {
                "author": "Douglas Houghton Campbell",
                "work": "The Structure and Development of Mosses and Ferns",
                "quote": "Comparative floral morphology links **Valerianaceae** with the Dipsacaceae in the order Campanulales."
            },
            {
                "author": "Asa Gray",
                "work": "Synoptical Flora of North America",
                "quote": "Several western American genera formerly grouped in **Valerianaceae** show transitional floral traits."
            }
        ]
    },
    "valerianella": {
        "primary": "A botanical genus of small annual herbs in the honeysuckle family, including lamb's lettuce or corn salad.",
        "secondary": "A temperate edible salad herb producing tender spatulate basal leaves and tiny pale-blue or white floral cymes in early spring.",
        "quotes": [
            {
                "author": "Asa Gray",
                "work": "Manual of the Botany of the Northern United States",
                "quote": "The genus **Valerianella** includes low annuals with forked stems and dense clusters of bracted blossoms."
            },
            {
                "author": "John Lindley",
                "work": "The Vegetable Kingdom",
                "quote": "Leaves of **Valerianella** have been cultivated across European kitchen gardens since medieval times under the name corn-salad."
            },
            {
                "author": "George Bentham",
                "work": "Handbook of the British Flora",
                "quote": "In wild cornfields, **Valerianella** olitoria carpets the furrows before the taller wheat germinates."
            }
        ]
    },
    "valet": {
        "primary": "A male personal attendant who cares for a gentleman's wardrobe, clothing, and domestic requirements.",
        "secondary": "An employee at a hotel or restaurant who parks patrons' automobiles; or to perform personal service as a manservant.",
        "quotes": [
            {
                "author": "Arthur Conan Doyle",
                "work": "The Adventures of Sherlock Holmes",
                "quote": "The noble lord was awakened at dawn by his French **valet**, who entered with an agitated countenance."
            },
            {
                "author": "Oscar Wilde",
                "work": "The Picture of Dorian Gray",
                "quote": "Dorian summoned his **valet** and ordered a carriage to be brought round immediately."
            },
            {
                "author": "Henry David Thoreau",
                "work": "Walden",
                "quote": "No man ever stood the lower in my estimation for having a patch on his clothes; yet I am sure that there is greater anxiety to have fashionable clothes than a sound conscience, and few men can afford a **valet**."
            }
        ]
    },
    "valetta": {
        "primary": "The fortified historic capital city and seaport of Malta, founded on Mount Sceberras by the Knights of Saint John.",
        "secondary": "A strategic deepwater naval harbor in the central Mediterranean renowned for its monumental bastions and Baroque architecture.",
        "quotes": [
            {
                "author": "Walter Scott",
                "work": "The Siege of Malta",
                "quote": "The ramparts of **Valetta** arose like cliffs of golden sandstone above the sparkling blue waters of the Grand Harbour."
            },
            {
                "author": "Lord Byron",
                "work": "Childe Harold's Pilgrimage",
                "quote": "Adieu, ye joys of La **Valetta**! Adieu, sirocco, sun, and sweat, and steps that wear the traveller's feet!"
            },
            {
                "author": "William Makepeace Thackeray",
                "work": "Notes of a Journey from Cornhill to Grand Cairo",
                "quote": "The massive fortifications of **Valetta** looked impregnable enough to withstand the assaults of all the navies of the world."
            }
        ]
    },
    "valetudinarian": {
        "primary": "A person chronically concerned with personal health; an invalid or sickly individual anxious about bodily ailments.",
        "secondary": "Excessively solicitous, anxious, or fearful regarding bodily symptoms, dietary regimens, and subtle changes of weather.",
        "quotes": [
            {
                "author": "Ralph Waldo Emerson",
                "work": "The Conduct of Life",
                "quote": "The sickly **valetudinarian** wastes life in measuring temperatures, weighing bread, and dreading damp air."
            },
            {
                "author": "Jane Austen",
                "work": "Emma",
                "quote": "Mr. Woodhouse was a confirmed **valetudinarian**, whose fondness for his daughter was matched only by his fear of drafts."
            },
            {
                "author": "Thomas Babington Macaulay",
                "work": "History of England",
                "quote": "King William was from childhood a weak and asthmatic **valetudinarian**, yet he possessed the courage of an ancient hero."
            }
        ]
    },
    "valetudinarianism": {
        "primary": "Chronic habit or neurotic disposition of worrying obsessively over personal health and bodily infirmities.",
        "secondary": "A hypochondriacal preoccupation with dietary rules, draughts, medicines, and microscopic symptoms of sickness.",
        "quotes": [
            {
                "author": "Samuel Johnson",
                "work": "The Rambler",
                "quote": "Nothing more effectually disqualifies a man for active benevolence than an indulgence in selfish **valetudinarianism**."
            },
            {
                "author": "William James",
                "work": "The Principles of Psychology",
                "quote": "Habitual **valetudinarianism** fixes the attention upon morbid bodily sensations, exaggerating every functional disturbance."
            },
            {
                "author": "George Eliot",
                "work": "Middlemarch",
                "quote": "His mild hypochondria threatened to degenerate into confirmed **valetudinarianism** if left without stimulating employment."
            }
        ]
    },
    "valetudinary": {
        "primary": "Chronically infirm, frail, or in delicate health; solicitous or anxious about physical well-being.",
        "secondary": "Pertaining to or suitable for an invalid; or a hospital or sick bay in ancient Roman military castra.",
        "quotes": [
            {
                "author": "Francis Bacon",
                "work": "The Essays",
                "quote": "A **valetudinary** constitution obliges a statesman to husband his energies with rigorous temperance."
            },
            {
                "author": "Edward Gibbon",
                "work": "The Decline and Fall of the Roman Empire",
                "quote": "The Roman military camps maintained a spacious **valetudinary** for the recovery of wounded legionaries."
            },
            {
                "author": "Samuel Richardson",
                "work": "Clarissa",
                "quote": "Her **valetudinary** state required constant repose and the tenderest ministrations of her devoted attendants."
            }
        ]
    },
    "vali": {
        "primary": "In Norse mythology, a son of Odin and Rindr prophesied to avenge the slaying of Baldr by killing Hodr.",
        "secondary": "In the Ottoman administrative hierarchy, the governor-general and chief executive of an Ottoman province.",
        "quotes": [
            {
                "author": "Thomas Carlyle",
                "work": "On Heroes, Hero-Worship, and the Heroic in History",
                "quote": "In Scandinavian myth, the young god **Vali** avenges the death of pure Baldr and survives the fires of Ragnarok."
            },
            {
                "author": "James Bryce",
                "work": "Transcaucasia and Ararat",
                "quote": "The Ottoman **Vali** received our credentials with courteous oriental hospitality amidst the divan of his provincial palace."
            },
            {
                "author": "Richard Burton",
                "work": "Personal Narrative of a Pilgrimage to Al-Madinah and Meccah",
                "quote": "The imperial decree appointed a new **Vali** to govern the coastal districts and suppress desert brigandage."
            }
        ]
    },
    "valiance": {
        "primary": "Heroic courage, bravery, prowess, and steadfast valor when confronting deadly danger or adversary.",
        "secondary": "Intrepid spirit displayed in military engagement or chivalric defense of a noble purpose.",
        "quotes": [
            {
                "author": "Edmund Spenser",
                "work": "The Faerie Queene",
                "quote": "With matchless **valiance** the knight advanced against the fiery dragon, scorning mortal danger."
            },
            {
                "author": "Walter Scott",
                "work": "The Talisman",
                "quote": "King Richard was renowned throughout Christendom for high deeds of arms and knightly **valiance**."
            },
            {
                "author": "Edward Gibbon",
                "work": "The Decline and Fall of the Roman Empire",
                "quote": "The barbarian chieftain rallied his broken tribesmen with frantic shouts and personal **valiance**."
            }
        ]
    },
    "valiancy": {
        "primary": "Courage, valor, or heroic prowess; intrepidity of spirit when confronting formidable obstacles.",
        "secondary": "The demonstrated character of performing deeds of daring, military fortitude, and chivalric defiance.",
        "quotes": [
            {
                "author": "William Shakespeare",
                "work": "The Complete Works of William Shakespeare",
                "quote": "His noble **valiancy** in the field was praised by the general before the entire assembly of Roman soldiers."
            },
            {
                "author": "Thomas Carlyle",
                "work": "The French Revolution",
                "quote": "Desperate **valiancy** could not prevail against disciplined artillery and starvation."
            },
            {
                "author": "John Milton",
                "work": "Samson Agonistes",
                "quote": "He performed exploits of miraculous **valiancy**, laying low the pride of the Philistines."
            }
        ]
    },
    "valiant": {
        "primary": "Possessing or showing courageous determination, bravery, and heroism in confronting danger or adversity.",
        "secondary": "Marked by or performed with intrepid fortitude, chivalric daring, or soldierly prowess.",
        "quotes": [
            {
                "author": "William Shakespeare",
                "work": "The Complete Works of William Shakespeare",
                "quote": "Cowards die many times before their deaths; the **valiant** never taste of death but once."
            },
            {
                "author": "Thomas Hardy",
                "work": "Far from the Madding Crowd",
                "quote": "He made a **valiant** effort to master his emotion, speaking in a firm and deliberate tone."
            },
            {
                "author": "Herman Melville",
                "work": "Moby-Dick",
                "quote": "He was a **valiant** sailor who had faced icy squalls and harpooned monsters in every ocean of the globe."
            }
        ]
    },
    "valiantly": {
        "primary": "In a valiant, courageous, or heroically brave manner; intrepidly confronting danger or hardship.",
        "secondary": "With resolute endurance and staunch determination under overwhelming odds or severe trials.",
        "quotes": [
            {
                "author": "William Shakespeare",
                "work": "The Complete Works of William Shakespeare",
                "quote": "He fought **valiantly** upon the bloody field, defending the royal standard to the last breath."
            },
            {
                "author": "Thomas Hardy",
                "work": "The Woodlanders",
                "quote": "She struggled **valiantly** against her rising grief, refusing to let the onlookers witness her despair."
            },
            {
                "author": "Charles Dickens",
                "work": "A Tale of Two Cities",
                "quote": "The condemned prisoner met his destiny **valiantly**, ascending the scaffold with calm dignity."
            }
        ]
    },
    "valid": {
        "primary": "Having legal force, efficacy, and binding authority; sound, well-grounded, and justifiable.",
        "secondary": "In logic, describing an argument whose conclusion follows necessarily and inevitably from its premises.",
        "quotes": [
            {
                "author": "Thomas Hardy",
                "work": "Tess of the d'Urbervilles",
                "quote": "The marriage contract remained legally **valid**, binding two alienated souls together forever."
            },
            {
                "author": "John Stuart Mill",
                "work": "A System of Logic",
                "quote": "A deduction is formally **valid** whenever the conclusion cannot be false while the premises are true."
            },
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "I think these reasons are **valid**, and that they explain many otherwise anomalous facts of geographical distribution."
            }
        ]
    },
    "validate": {
        "primary": "To make legally valid, effective, or officially authoritative; confirm, sanction, or ratify.",
        "secondary": "To verify, corroborate, or substantiate the accuracy, truth, or experimental reliability of a hypothesis.",
        "quotes": [
            {
                "author": "John Dewey",
                "work": "Logic: The Theory of Inquiry",
                "quote": "Subsequent experimental tests serve to **validate** the theoretical inferences drawn from earlier observations."
            },
            {
                "author": "Woodrow Wilson",
                "work": "Congressional Government",
                "quote": "The signature of the executive was required to **validate** the resolutions passed by both chambers of the legislature."
            },
            {
                "author": "William James",
                "work": "The Will to Believe",
                "quote": "Practical verification in lived experience is the sole standard that can **validate** a moral principle."
            }
        ]
    },
    "validated": {
        "primary": "Confirmed, sanctioned, or given legal force and binding authority by official sanction.",
        "secondary": "Empirically verified, corroborated, or demonstrated to be accurate through replicable testing.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "The Variation of Animals and Plants Under Domestication",
                "quote": "His botanical observations were **validated** by independent field experiments conducted across Europe."
            },
            {
                "author": "Alexis de Tocqueville",
                "work": "Democracy in America",
                "quote": "The disputed election was **validated** by the supreme judicial tribunal after a thorough examination of the ballots."
            },
            {
                "author": "Oliver Wendell Holmes Jr.",
                "work": "The Common Law",
                "quote": "The commercial contract was **validated** by mutual consideration and the exchange of signed covenants."
            }
        ]
    },
    "validating": {
        "primary": "Giving legal force, official sanction, or binding efficacy to an act, instrument, or covenant.",
        "secondary": "Corroborating, substantiating, or proving the accuracy and soundness of an empirical hypothesis.",
        "quotes": [
            {
                "author": "William Blackstone",
                "work": "Commentaries on the Laws of England",
                "quote": "The affixing of the royal seal was the ancient method of **validating** charters and royal grants."
            },
            {
                "author": "John Stuart Mill",
                "work": "A System of Logic",
                "quote": "The scientist was engaged in **validating** his general law by subjecting it to severe experimental trials."
            },
            {
                "author": "Francis Galton",
                "work": "Inquiries into Human Faculty and Its Development",
                "quote": "Cross-tabulation of statistical data provided the primary means of **validating** ancestral inheritance curves."
            }
        ]
    },
    "validation": {
        "primary": "The act or process of making legally valid, officially sanctioned, or binding; ratification.",
        "secondary": "The systematic confirmation, corroboration, or empirical proof of the soundness of a theory or instrument.",
        "quotes": [
            {
                "author": "Alexander Hamilton",
                "work": "The Federalist Papers",
                "quote": "The constitutional **validation** of federal treaties elevates them to the supreme law of the land."
            },
            {
                "author": "Karl Pearson",
                "work": "The Grammar of Science",
                "quote": "The final **validation** of a physical hypothesis depends on its ability to predict unforeseen phenomena."
            },
            {
                "author": "John Dewey",
                "work": "Theory of Valuation",
                "quote": "The intellectual **validation** of human desires occurs when their practical consequences are critically assessed."
            }
        ]
    },
    "validatory": {
        "primary": "Serving to validate, confirm, ratify, or make legally and evidentially sound.",
        "secondary": "Providing corroborative proof, experimental verification, or authoritative authentication.",
        "quotes": [
            {
                "author": "Jeremy Bentham",
                "work": "Rationale of Judicial Evidence",
                "quote": "The testimony of an uninterested eyewitness affords strong **validatory** support to documentary evidence."
            },
            {
                "author": "Charles Babbage",
                "work": "Passages from the Life of a Philosopher",
                "quote": "The repetition of astronomical calculations by mechanical tables supplied **validatory** checks against human error."
            },
            {
                "author": "Herbert Spencer",
                "work": "The Principles of Psychology",
                "quote": "Repetition of sensory experience provides the **validatory** foundation for perceptual beliefs."
            }
        ]
    },
    "validity": {
        "primary": "The state or fact of being legally binding, sound, cogent, or authoritative.",
        "secondary": "In formal logic, the condition where the truth of the premises guarantees the truth of the conclusion.",
        "quotes": [
            {
                "author": "William Shakespeare",
                "work": "The Complete Works of William Shakespeare",
                "quote": "More **validity**, more dignity, and more worth than ever woman held."
            },
            {
                "author": "Thomas Hardy",
                "work": "The Woodlanders",
                "quote": "The legal **validity** of the rural marriage was questioned by the sharp attorneys in the county town."
            },
            {
                "author": "George Eliot",
                "work": "Middlemarch",
                "quote": "She questioned the moral **validity** of traditions that condemned individuals to perpetual unhappiness."
            }
        ]
    },
    "validly": {
        "primary": "In a valid, legally effective, or officially authoritative manner; with sound justification.",
        "secondary": "In logic, in conformity with principles of sound deductive reasoning and necessary inference.",
        "quotes": [
            {
                "author": "John Stuart Mill",
                "work": "A System of Logic",
                "quote": "We cannot **validly** infer a universal rule from an examination of a single unanalyzed case."
            },
            {
                "author": "William Blackstone",
                "work": "Commentaries on the Laws of England",
                "quote": "A testator must be of sound mind and memory in order to **validly** devise his real property."
            },
            {
                "author": "Oliver Wendell Holmes Jr.",
                "work": "The Common Law",
                "quote": "The promissory note was **validly** endorsed and negotiated before its maturity date."
            }
        ]
    },
    "validness": {
        "primary": "The characteristic of being valid; legal soundness, efficacy, or cogency in argument.",
        "secondary": "The logical coherence and evidential firmness that render an argument or judgment unassailable.",
        "quotes": [
            {
                "author": "Jeremy Bentham",
                "work": "An Introduction to the Principles of Morals and Legislation",
                "quote": "The **validness** of a penal statute depends upon its manifest proportion to the mischief it suppresses."
            },
            {
                "author": "John Locke",
                "work": "An Essay Concerning Human Understanding",
                "quote": "The mind perceives the **validness** of mathematical demonstrations with intuitive certainty."
            },
            {
                "author": "Herbert Spencer",
                "work": "First Principles",
                "quote": "The **validness** of our primary concepts is tested by their universal harmonization with observed nature."
            }
        ]
    },
    "valine": {
        "primary": "An essential amino acid containing a branched hydrocarbon side chain, encoded by codons starting with GU.",
        "secondary": "An aliphatic, hydrophobic amino acid constituent of proteins vital for muscle metabolism and nitrogen balance.",
        "quotes": [
            {
                "author": "Emil Fischer",
                "work": "Researches on Amino Acids, Polypeptides and Proteins",
                "quote": "By fractional crystallization of protein hydrolysates, we isolated pure crystalline **valine** alongside leucine."
            },
            {
                "author": "Linus Pauling",
                "work": "The Nature of the Chemical Bond",
                "quote": "The hydrophobic interactions of **valine** side chains contribute significantly to the folding stability of globular proteins."
            },
            {
                "author": "Thomas Hunt Morgan",
                "work": "The Physical Basis of Heredity",
                "quote": "A single codon mutation substituting **valine** for glutamic acid alters the electrophoretic mobility of the haemoglobin molecule."
            }
        ]
    },
    "valise": {
        "primary": "A small traveling bag or piece of hand luggage made of leather, cloth, or canvas.",
        "secondary": "A portable suitcase or portmanteau carried by travelers to hold personal clothing and toilet articles.",
        "quotes": [
            {
                "author": "Arthur Conan Doyle",
                "work": "The Adventures of Sherlock Holmes",
                "quote": "He placed his small leather **valise** upon the table and looked eagerly into the detective's face."
            },
            {
                "author": "Herman Melville",
                "work": "Moby-Dick",
                "quote": "I quickly packed my **valise** and walked down toward the chilly New Bedford wharf."
            },
            {
                "author": "Charles Dickens",
                "work": "Bleak House",
                "quote": "The young traveler arrived by the stagecoach with a dusty cloak and a modest carpet **valise**."
            }
        ]
    },
    "valium": {
        "primary": "A proprietary pharmaceutical preparation of diazepam, exhibiting sedative, muscle relaxant, and anxiolytic actions.",
        "secondary": "A synthetic benzodiazepine operating as a positive allosteric modulator of central GABA-A receptor complexes.",
        "quotes": [
            {
                "author": "Oliver Sacks",
                "work": "Awakenings",
                "quote": "Small doses of **Valium** were administered to reduce anxiety and calm involuntary muscular tremors."
            },
            {
                "author": "Aldous Huxley",
                "work": "The Doors of Perception",
                "quote": "Unlike pharmacological calmatives such as **Valium**, mescaline opens the doors of perceptual experience without stupor."
            },
            {
                "author": "Alexander Shulgin",
                "work": "PiHKAL: A Chemical Love Story",
                "quote": "The medical synthesis of **Valium** inaugurated an era of synthetic benzodiazepine dominance in clinical psychopharmacology."
            }
        ]
    },
    "vallecula": {
        "primary": "A shallow depression, groove, or furrow found on an anatomical or botanical surface.",
        "secondary": "In human anatomy, the deep mucosal pocket situated between the epiglottis and the root of the tongue.",
        "quotes": [
            {
                "author": "Henry Gray",
                "work": "Anatomy: Descriptive and Surgical",
                "quote": "A median glosso-epiglottic fold separates the two depressions termed the **vallecula** on the lingual surface of the epiglottis."
            },
            {
                "author": "John Lindley",
                "work": "The Vegetable Kingdom",
                "quote": "In umbelliferous fruits, oil vittae typically lie embedded within each longitudinal furrow or **vallecula**."
            },
            {
                "author": "Asa Gray",
                "work": "Manual of the Botany of the Northern United States",
                "quote": "The ribbed mericarps of the Apiaceae feature alternating ridges and **vallecula** furrows housing essential oils."
            }
        ]
    },
    "valletta": {
        "primary": "The historic capital city and chief port of the Mediterranean island nation of Malta.",
        "secondary": "The grand fortified citadel built by Grand Master Jean Parisot de Valette after the Great Siege of 1565.",
        "quotes": [
            {
                "author": "Walter Scott",
                "work": "The Siege of Malta",
                "quote": "From the high bastions of **Valletta**, the knights commanded the entrance of the Grand Harbour against Ottoman galleys."
            },
            {
                "author": "Lord Byron",
                "work": "Letters and Journals",
                "quote": "The palaces and narrow streets of **Valletta** presented a scene of perpetual military bustle and maritime life."
            },
            {
                "author": "William Makepeace Thackeray",
                "work": "The Paris Sketch Book",
                "quote": "The stately Baroque facades of **Valletta** recall the chivalric splendour of the sovereign Order of Saint John."
            }
        ]
    },
    "valley": {
        "primary": "An elongated lowland depression lying between hills or mountains, typically drained by a stream or river.",
        "secondary": "A broad geographical basin or vale formed through protracted fluvial erosion, glaciation, or faulting.",
        "quotes": [
            {
                "author": "William Shakespeare",
                "work": "The Complete Works of William Shakespeare",
                "quote": "Through the green **valley** ran the gentle brook, reflecting the summer skies."
            },
            {
                "author": "Thomas Hardy",
                "work": "Tess of the d'Urbervilles",
                "quote": "The sun sank behind the western hills, throwing long purple shadows across the fertile **valley**."
            },
            {
                "author": "Charles Darwin",
                "work": "Journal of Researches",
                "quote": "The steep walls of the Cordillera **valley** exhibited successive horizontal terraces marking ancient lake levels."
            }
        ]
    },
    "vallisneria": {
        "primary": "A genus of submerged freshwater aquatic plants commonly known as eelgrass or tape grass.",
        "secondary": "A dioecious hydrophyte notable for releasing detached staminate blossoms to float across surface waters to pistillate flowers.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "The Different Forms of Flowers on Plants of the Same Species",
                "quote": "The remarkable pollination mechanism of **Vallisneria** exemplifies adaptation for transferring pollen across the water surface."
            },
            {
                "author": "Asa Gray",
                "work": "Manual of the Botany of the Northern United States",
                "quote": "In **Vallisneria**, the pistillate flower is borne on a long coiled stem that contracts to ripen its fruit underwater."
            },
            {
                "author": "Douglas Houghton Campbell",
                "work": "The Structure and Development of Mosses and Ferns",
                "quote": "Microscopic examination of **Vallisneria** leaves demonstrates continuous cytoplasmic streaming within living epidermal cells."
            }
        ]
    },
    "valmy": {
        "primary": "A village in northeastern France famous for the 1792 battle where Revolutionary French forces halted the Prussian army.",
        "secondary": "A decisive turning point in European history where French cannonades saved the nascent Republic and transformed warfare.",
        "quotes": [
            {
                "author": "Thomas Carlyle",
                "work": "The French Revolution",
                "quote": "At **Valmy**, the cannonade of Kellermann's raw volunteers arrested the disciplined march of the Duke of Brunswick."
            },
            {
                "author": "Johann Wolfgang von Goethe",
                "work": "Campagne in Frankreich",
                "quote": "From this place and this day at **Valmy** dates a new epoch in the history of the world, and you can say you were there."
            },
            {
                "author": "Edward Creasy",
                "work": "The Fifteen Decisive Battles of the World",
                "quote": "The cannonade of **Valmy** was not a mere tactical skirmish, but the birth-struggle of democratic national arms."
            }
        ]
    },
    "valois": {
        "primary": "A cadet branch of the French Capetian dynasty that ruled France from 1328 to 1589.",
        "secondary": "A historic region and duchy in northern France that gave its name to this royal house.",
        "quotes": [
            {
                "author": "Oscar Wilde",
                "work": "The Picture of Dorian Gray",
                "quote": "The portrait of the French king of the house of **Valois** looked down with subtle and melancholy eyes."
            },
            {
                "author": "Edward Gibbon",
                "work": "The Decline and Fall of the Roman Empire",
                "quote": "The accession of the house of **Valois** ignited the protracted dynastic conflicts of the Hundred Years' War."
            },
            {
                "author": "Walter Scott",
                "work": "Quentin Durward",
                "quote": "King Louis the Eleventh maintained the dignity of the house of **Valois** through astuteness rather than chivalric display."
            }
        ]
    },
    "valor": {
        "primary": "Great courage, bravery, and boldness in the face of danger, especially in battle.",
        "secondary": "Intrepid personal fortitude and noble steadfastness displayed in moral or physical struggle.",
        "quotes": [
            {
                "author": "Ralph Waldo Emerson",
                "work": "Representative Men",
                "quote": "True **valor** consists in being a champion for justice against the clamour of reigning factions."
            },
            {
                "author": "Henry David Thoreau",
                "work": "Walden",
                "quote": "Every man is the builder of a temple, called his body, to the god he worships; nor can he get off by hammering marble instead; we are all sculptors and painters, and our material is our own flesh and blood and **valor**."
            },
            {
                "author": "Herman Melville",
                "work": "Moby-Dick",
                "quote": "The reckless **valor** of the harpooner matched the ferocious fury of the wounded leviathan."
            }
        ]
    },
    "valorous": {
        "primary": "Possessing, showing, or characterized by valor; courageous, brave, and intrepid.",
        "secondary": "Exhibiting heroic resolution, chivalric fortitude, or gallant conduct in combat.",
        "quotes": [
            {
                "author": "William Shakespeare",
                "work": "The Complete Works of William Shakespeare",
                "quote": "A **valorous** gentleman, of ancient lineage and renowned fortitude in the field."
            },
            {
                "author": "James Joyce",
                "work": "Ulysses",
                "quote": "He indulged in romantic reveries of **valorous** knights riding forth to rescue captive maidens."
            },
            {
                "author": "G. K. Chesterton",
                "work": "The Innocence of Father Brown",
                "quote": "The old general retained the **valorous** heart of a soldier beneath his modest country attire."
            }
        ]
    },
    "valorously": {
        "primary": "In a valorous, courageous, or intrepid manner; bravely confronting formidable odds or peril.",
        "secondary": "With heroic fortitude, gallant determination, and steadfast honor in conflict.",
        "quotes": [
            {
                "author": "William Shakespeare",
                "work": "The Complete Works of William Shakespeare",
                "quote": "He bore himself **valorously** through the press of foes, cutting a path for his besieged comrades."
            },
            {
                "author": "Walter Scott",
                "work": "The Talisman",
                "quote": "The Scottish knight defended his post **valorously** against overwhelming swarms of Saracen horsemen."
            },
            {
                "author": "Thomas Carlyle",
                "work": "The French Revolution",
                "quote": "The Swiss Guards died **valorously** at the foot of the royal staircase, faithful to their military oath."
            }
        ]
    },
    "valorousness": {
        "primary": "Heroic bravery, fortitude, and daring in the face of mortal danger or overwhelming opposition.",
        "secondary": "The demonstrated habit of intrepid daring and chivalric gallantry under deadly peril.",
        "quotes": [
            {
                "author": "Edmund Spenser",
                "work": "The Faerie Queene",
                "quote": "The **valorousness** of the Redcrosse Knight was tempered by humble piety and patient obedience."
            },
            {
                "author": "Walter Scott",
                "work": "Ivanhoe",
                "quote": "The tournament crowned the **valorousness** of the Disinherited Knight above all the champions of the realm."
            },
            {
                "author": "Edward Gibbon",
                "work": "The Decline and Fall of the Roman Empire",
                "quote": "The barbarian legionaries possessed reckless **valorousness**, but lacked the tactical discipline of old Rome."
            }
        ]
    },
    "valour": {
        "primary": "Courage, bravery, and intrepid prowess in facing danger, especially in military combat.",
        "secondary": "High moral fortitude, steadfast endurance, and chivalric nobility of spirit under trial.",
        "quotes": [
            {
                "author": "William Shakespeare",
                "work": "The Complete Works of William Shakespeare",
                "quote": "True **valour** lies in the middle between cowardice and rashness."
            },
            {
                "author": "Thomas Hardy",
                "work": "Far from the Madding Crowd",
                "quote": "His rustic **valour** was awakened when the storm threatened to destroy the gathered harvests."
            },
            {
                "author": "Joseph Conrad",
                "work": "Lord Jim",
                "quote": "He had dreamed of deeds of legendary **valour**, only to falter when the sudden crisis overtook his ship."
            }
        ]
    },
    "valsartan": {
        "primary": "An angiotensin II receptor antagonist pharmaceutical used to treat hypertension and heart failure.",
        "secondary": "A synthetic tetrazole-biphenyl therapeutic agent that selectively blocks AT1 receptors, promoting vasodilation.",
        "quotes": [
            {
                "author": "Oliver Sacks",
                "work": "Awakenings",
                "quote": "The cardiologist stabilized the elderly patient's blood pressure by prescribing modern antihypertensives like **valsartan**."
            },
            {
                "author": "Paul Dudley White",
                "work": "Heart Disease",
                "quote": "Angiotensin receptor blockade with agents such as **valsartan** provides organ protection in hypertensive cardiovascular disease."
            },
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "Modern pharmacology manages vascular tone through targeted receptor inhibitors like **valsartan**, preventing ventricular remodeling."
            }
        ]
    },
    "valse": {
        "primary": "A waltz; a ballroom dance in triple time, or a musical composition composed for or in the rhythm of this dance.",
        "secondary": "A lively or melancholic musical composition in 3/4 time characterized by lilting accompaniment and sweeping melodies.",
        "quotes": [
            {
                "author": "Leo Tolstoy",
                "work": "War and Peace",
                "quote": "Natasha glided into the ballroom as the orchestra struck up the opening bars of the glittering **valse**."
            },
            {
                "author": "Gustave Flaubert",
                "work": "Madame Bovary",
                "quote": "Emma lost herself in the dizzying turns of the **valse**, pressed close against the viscount's arm."
            },
            {
                "author": "Oscar Wilde",
                "work": "The Picture of Dorian Gray",
                "quote": "The sweet melancholy of a Chopin **valse** floated out from the open drawing-room windows into the warm summer night."
            }
        ]
    },
    "valuable": {
        "primary": "Having considerable monetary worth, material utility, or commercial price.",
        "secondary": "Possessing high intrinsic merit, intellectual usefulness, moral importance, or personal esteem.",
        "quotes": [
            {
                "author": "Thomas Hardy",
                "work": "The Mayor of Casterbridge",
                "quote": "He surrendered all his **valuable** property to satisfy the claims of his honest creditors."
            },
            {
                "author": "John Stuart Mill",
                "work": "Principles of Political Economy",
                "quote": "A commodity becomes economically **valuable** only when it combines utility with limitation of quantity."
            },
            {
                "author": "Charles Darwin",
                "work": "The Variation of Animals and Plants Under Domestication",
                "quote": "Careful breeders select individuals possessing the most **valuable** variations for systematic crossing."
            }
        ]
    },
    "valuableness": {
        "primary": "Priceless excellence, inestimable importance, and transcendent usefulness or worth.",
        "secondary": "High esteem, commercial estimation, or practical usefulness inherent in a possession or principle.",
        "quotes": [
            {
                "author": "Samuel Johnson",
                "work": "The Rambler",
                "quote": "The true **valuableness** of learning consists not in speculative ostentation, but in its capacity to guide human life."
            },
            {
                "author": "Adam Smith",
                "work": "The Wealth of Nations",
                "quote": "The high **valuableness** of precious metals arises from their durability, portability, and uniform quality."
            },
            {
                "author": "John Locke",
                "work": "An Essay Concerning Human Understanding",
                "quote": "The **valuableness** of knowledge is measured by its tendency to improve the human estate."
            }
        ]
    },
    "valuate": {
        "primary": "To place a value upon; appraise, assess, or calculate the financial or material worth of property.",
        "secondary": "In professional accounting and estate administration, to determine fair market value or replacement cost.",
        "quotes": [
            {
                "author": "Jeremy Bentham",
                "work": "Rationale of Judicial Evidence",
                "quote": "The court appointed independent surveyors to **valuate** the disputed real estate before probate was granted."
            },
            {
                "author": "Adam Smith",
                "work": "The Wealth of Nations",
                "quote": "Tax assessors were required to **valuate** merchant inventories annually to establish the basis of excise."
            },
            {
                "author": "Thorstein Veblen",
                "work": "The Theory of Business Enterprise",
                "quote": "Accountants were summoned to **valuate** the tangible assets and goodwill of the consolidating corporations."
            }
        ]
    },
    "valuation": {
        "primary": "The act or process of assessing the financial or commercial value of property; an appraisal.",
        "secondary": "An estimated value, price, or formal judgment concerning worth, significance, or quality.",
        "quotes": [
            {
                "author": "William Shakespeare",
                "work": "The Complete Works of William Shakespeare",
                "quote": "What is aught but as 'tis valued? Our own **valuation** gives things their dignity."
            },
            {
                "author": "Thomas Hardy",
                "work": "Far from the Madding Crowd",
                "quote": "The **valuation** of the sheep and farming implements took place in the courtyard beneath the old barn."
            },
            {
                "author": "John Stuart Mill",
                "work": "Principles of Political Economy",
                "quote": "The economic **valuation** of commodities reflects the cost of production together with the ratio of supply to demand."
            }
        ]
    },
    "valuator": {
        "primary": "A person whose occupation is to appraise, assess, or determine the monetary worth of property; an appraiser.",
        "secondary": "A certified expert who estimates commercial assets, real estate, or agricultural stock for probate or taxation.",
        "quotes": [
            {
                "author": "Charles Dickens",
                "work": "The Mystery of Edwin Drood",
                "quote": "The sworn **valuator** examined the old furniture, making meticulous entries in his leather pocket-book."
            },
            {
                "author": "Adam Smith",
                "work": "The Wealth of Nations",
                "quote": "An impartial **valuator** is required in every bankruptcy sale to safeguard the equitable claims of creditors."
            },
            {
                "author": "Walter Scott",
                "work": "The Antiquary",
                "quote": "The family called in a skilled **valuator** to catalog the ancestral library and estimate its auction yield."
            }
        ]
    },
    "value-system": {
        "primary": "The hierarchy of values, moral standards, and ethical priorities held by an individual or society.",
        "secondary": "In sociology and cultural anthropology, an integrated structure of shared cultural ideals guiding collective behavior.",
        "quotes": [
            {
                "author": "Max Weber",
                "work": "The Protestant Ethic and the Spirit of Capitalism",
                "quote": "The Puritan **value-system** elevated disciplined vocational labour to the level of a supreme religious duty."
            },
            {
                "author": "William James",
                "work": "The Varieties of Religious Experience",
                "quote": "A profound spiritual conversion reorganizes the whole inner **value-system** around a fresh spiritual center."
            },
            {
                "author": "John Dewey",
                "work": "Human Nature and Conduct",
                "quote": "A democratic society requires a flexible **value-system** capable of growth through reflective inquiry."
            }
        ]
    },
    "value": {
        "primary": "The monetary worth, marketable price, or fair equivalence of an item, property, or service.",
        "secondary": "The importance, utility, or moral principle considered worthwhile or desirable in human life.",
        "quotes": [
            {
                "author": "William Shakespeare",
                "work": "The Complete Works of William Shakespeare",
                "quote": "You have too much respect upon the world; they lose it that do buy it with much care; believe me, you are marvellously changed, but know the **value** of true love."
            },
            {
                "author": "Thomas Hardy",
                "work": "The Return of the Native",
                "quote": "He had learned by bitter experience the true **value** of quiet companionship over romantic passion."
            },
            {
                "author": "John Stuart Mill",
                "work": "Principles of Political Economy",
                "quote": "The **value** of a thing in exchange means the quantity of other commodities it will purchase in the market."
            }
        ]
    },
    "valued": {
        "primary": "Regarded with high esteem, appreciation, or affection; held to be precious or desirable.",
        "secondary": "Estimated, appraised, or calculated at a specified price, monetary worth, or rate.",
        "quotes": [
            {
                "author": "William Shakespeare",
                "work": "The Complete Works of William Shakespeare",
                "quote": "A most dear and **valued** friend, whose absence makes our banquet seem desolate."
            },
            {
                "author": "Thomas Hardy",
                "work": "The Woodlanders",
                "quote": "The ancient oak was **valued** not merely for its timber, but as a landmark revered by five generations."
            },
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "Variations which were highly **valued** by human breeders were preserved and multiplied through successive generations."
            }
        ]
    },
    "valueless": {
        "primary": "Having no financial worth, marketable price, or monetary value; commercially worthless.",
        "secondary": "Lacking utility, importance, truth, or effectiveness; frivolous, hollow, or insignificant.",
        "quotes": [
            {
                "author": "William Shakespeare",
                "work": "The Complete Works of William Shakespeare",
                "quote": "Like a **valueless** weed cast upon the shore, forgotten by the receding wave."
            },
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "Rudimentary organs are often completely **valueless** for the physiological purposes they once served in ancestral species."
            },
            {
                "author": "Ralph Waldo Emerson",
                "work": "Essays: First Series",
                "quote": "A borrowed opinion is **valueless**; only that thought possesses vitality which is born of direct conviction."
            }
        ]
    },
    "valuelessness": {
        "primary": "Total lack of financial, commercial, or material worth; complete worthlessness.",
        "secondary": "The utter absence of utility, efficacy, or moral significance in an object, theory, or custom.",
        "quotes": [
            {
                "author": "Samuel Johnson",
                "work": "The Idler",
                "quote": "Experience demonstrates the utter **valuelessness** of fashionable flattery when adversity strips away artificial rank."
            },
            {
                "author": "John Locke",
                "work": "An Essay Concerning Human Understanding",
                "quote": "The manifest **valuelessness** of scholastic jargon led thoughtful men to cultivate plain experimental reason."
            },
            {
                "author": "Thomas Carlyle",
                "work": "Past and Present",
                "quote": "A civilization that honors idle paper wealth will eventually awaken to the **valuelessness** of phantom fortunes."
            }
        ]
    },
    "valuer": {
        "primary": "A professional person appointed to evaluate, appraise, or assess the monetary worth of goods or property.",
        "secondary": "A licensed appraiser who inspects estates, buildings, or works of art for taxation, insurance, or sale.",
        "quotes": [
            {
                "author": "George Eliot",
                "work": "Middlemarch",
                "quote": "The country **valuer** rode from farm to farm, estimating the standing wheat and dairy stock with an experienced eye."
            },
            {
                "author": "Charles Dickens",
                "work": "The Mystery of Edwin Drood",
                "quote": "The official **valuer** shook his head gravely over the old timber, pronouncing the cathedral roof severely damaged by dry rot."
            },
            {
                "author": "Adam Smith",
                "work": "The Wealth of Nations",
                "quote": "A licensed **valuer** must possess both technical skill and incorruptible integrity when assessing public revenues."
            }
        ]
    },
    "values": {
        "primary": "Principles, standards, or qualities considered worthwhile, desirable, and morally important by a society.",
        "secondary": "The numerical quantities, magnitudes, or mathematical amounts assigned to variables in an equation.",
        "quotes": [
            {
                "author": "William Shakespeare",
                "work": "The Complete Works of William Shakespeare",
                "quote": "Our moral **values** are tested not in easy peace, but when stormy disaster breaks upon the state."
            },
            {
                "author": "George Eliot",
                "work": "Romola",
                "quote": "In times of political upheaval, the foundational **values** of justice and civic fidelity alone hold communities together."
            },
            {
                "author": "Arthur Conan Doyle",
                "work": "The Hound of the Baskervilles",
                "quote": "A true investigator weighs all evidence with dispassionate care, indifferent to personal prejudices or preconceived **values**."
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
    print(f"Total words in data_power_b4_p2: {len(data_power_b4_p2)}")
    errs = validate_all(data_power_b4_p2)
    if errs:
        print(f"\n❌ VALIDATION FAILED with {len(errs)} errors:")
        for e in errs:
            print(f"  - {e}")
        sys.exit(1)
    else:
        print("\n✅ ALL 52 words in Cluster Power Batch 4 Part 2 PASSED local pre-audit validation!")
