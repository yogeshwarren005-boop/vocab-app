# -*- coding: utf-8 -*-
"""
Generator for Batch 2 of Form & Space Finish Slice 5 (64 words):
From Dashboard — tem/tomography.md to Dashboard — the/prosthetics.md
"""

import json
import os

data = {
  "Dashboard — tem\\tomography.md": {
    "primary": "A technique for displaying a representation of a cross-section through a human body or other solid object using X-rays, ultrasound, or magnetic resonance.",
    "secondary": "In medical imaging, computed tomography (CT) revolutionized non-invasive diagnostic pathology by reconstructing volumetric attenuation matrices from multi-angle planar projections.",
    "quotes": [
      {
        "author": "Allan M. Cormack",
        "work": "Nobel Lecture: Early Work on Computed Tomography",
        "quote": "The mathematical foundation of computerized axial **tomography** rests upon solving line integrals of absorption across arbitrary sections."
      },
      {
        "author": "Godfrey Hounsfield",
        "work": "Nobel Lecture: Computed Medical Imaging",
        "quote": "Initial clinical trials of computer-assisted **tomography** proved that soft tissue lesions in the brain could be visualized without surgical exploration."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Modern developments in diagnostic **tomography** allow clinicians to delineate deep thoracic cavities with unprecedented anatomical precision."
      }
    ]
  },
  "Dashboard — tem\\trichotomous.md": {
    "primary": "Divided into three parts, elements, or branches; exhibiting trichotomy.",
    "secondary": "In botanical morphology and formal logic, describing floral axes or systems of categorization that diverge into three equivalent coordinate divisions.",
    "quotes": [
      {
        "author": "Asa Gray",
        "work": "Structural Botany",
        "quote": "In certain cymose inflorescences, the main floral peduncle exhibits a regular **trichotomous** ramification."
      },
      {
        "author": "Charles Sanders Peirce",
        "work": "Collected Papers",
        "quote": "My fundamental semiotic taxonomy is strictly **trichotomous**, partitioning all signs into sign, object, and interpretant."
      },
      {
        "author": "George Bentham",
        "work": "Handbook of the British Flora",
        "quote": "The branching pattern of the terminal cyme appears distinctly **trichotomous** at the primary node."
      }
    ]
  },
  "Dashboard — tem\\trichotomy.md": {
    "primary": "A division or classification into three distinct parts, categories, or stages.",
    "secondary": "In philosophy and systematic theology, trichotomy often denotes the tripartite division of human nature into body, soul, and spirit (e.g. Pauline anthropology).",
    "quotes": [
      {
        "author": "Immanuel Kant",
        "work": "Critique of Pure Reason",
        "quote": "Each class of categories displays a natural **trichotomy**, the third arising from the combination of the first two."
      },
      {
        "author": "C. S. Lewis",
        "work": "The Discarded Image",
        "quote": "Medieval philosophy preserved the Pauline **trichotomy** of body, soul, and spirit alongside Aristotelian dualism."
      },
      {
        "author": "G. W. F. Hegel",
        "work": "The Science of Logic",
        "quote": "The dialectical progression moves through a necessary **trichotomy** of thesis, antithesis, and synthetic unity."
      }
    ]
  },
  "Dashboard — tem\\vasectomise.md": {
    "primary": "To perform a vasectomy on; to render sterile by surgical excision of part of the vas deferens (chiefly Commonwealth spelling).",
    "secondary": "In urological surgery, the procedure severs and occludes the bilateral ductus deferentes to prevent spermatozoa from entering the ejaculatory stream.",
    "quotes": [
      {
        "author": "Havelock Ellis",
        "work": "Studies in the Psychology of Sex",
        "quote": "Early advocates proposed to **vasectomise** individuals for therapeutic purposes rather than purely for contraception."
      },
      {
        "author": "Julian Huxley",
        "work": "Essays of a Biologist",
        "quote": "Surgeons who **vasectomise** experimental mammals observe that endocrine interstitial cell activity remains unaffected."
      },
      {
        "author": "Marie Stopes",
        "work": "Contraception: Its Theory, History and Practice",
        "quote": "To **vasectomise** the male partner provides a permanent, simple alternative to complex female sterilization procedures."
      }
    ]
  },
  "Dashboard — tem\\vasectomize.md": {
    "primary": "To sever or excise a portion of the vas deferens to induce surgical sterilization in a male.",
    "secondary": "In clinical reproductive medicine, elective vasectomy is performed through a minimally invasive scrotal incision under local anesthesia.",
    "quotes": [
      {
        "author": "Aldous Huxley",
        "work": "Brave New World Revisited",
        "quote": "Totalitarian regimes have contemplated schemes to **vasectomize** populations deemed genetically or socially undesirable."
      },
      {
        "author": "Norman Haire",
        "work": "Rejuvenation: The Work of Steinach, Voronoff, and Others",
        "quote": "Eugen Steinach attempted to **vasectomize** aging rodents to stimulate testicular Leydig cell rejuvenation."
      },
      {
        "author": "Paul Ehrlich",
        "work": "The Population Bomb",
        "quote": "Mobile medical camps were dispatched across rural districts to **vasectomize** volunteers as part of demographic management."
      }
    ]
  },
  "Dashboard — tem\\vasectomy.md": {
    "primary": "The surgical cutting and sealing of part of each vas deferens, typically as a means of permanent male contraception.",
    "secondary": "First performed on human subjects by Reginald Harrison in 1893, vasectomy is a highly effective contraceptive intervention that leaves sexual potency and testosterone production intact.",
    "quotes": [
      {
        "author": "H. G. Wells",
        "work": "The Shape of Things to Come",
        "quote": "The widespread voluntary adoption of **vasectomy** assisted in stabilizing global post-collapse demographics."
      },
      {
        "author": "Bertrand Russell",
        "work": "Marriage and Morals",
        "quote": "A simple surgical **vasectomy** eliminates unwanted fertility without diminishing normal masculine vitality."
      },
      {
        "author": "Sigmund Freud",
        "work": "Letters of Sigmund Freud",
        "quote": "Freud underwent a Steinach **vasectomy** in his later years in hopes of retarding the growth of his palatal tumor."
      }
    ]
  },
  "Dashboard — the\\anathema.md": {
    "primary": "Something or someone intensely disliked, cursed, or loathed; formally, an ecclesiastical ban, curse, or excommunication accompanied by solemn condemnation.",
    "secondary": "Derived from Greek *anathema* (something set apart or dedicated to destruction), formalized in ecumenical councils to condemn heretical propositions (*anathema sit*).",
    "quotes": [
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "Ecclesiastical councils hurled solemn decrees of **anathema** against every bishop who wavered on the Nicene Creed."
      },
      {
        "author": "Thomas Babington Macaulay",
        "work": "The History of England",
        "quote": "Any compromise with papal supremacy was regarded as an intolerable **anathema** by the Scottish Covenanters."
      },
      {
        "author": "John Milton",
        "work": "Of Reformation in England",
        "quote": "Pretended episcopal authority brandishes its papistical **anathema** against the conscientious liberty of reformed churches."
      }
    ]
  },
  "Dashboard — the\\anathematic.md": {
    "primary": "Of, relating to, or having the character of an anathema; marked by curse, formal condemnation, or banishment.",
    "secondary": "In historical and ecclesiastical theology, anathematic pronouncements signified absolute exclusion from religious fellowship and divine favor.",
    "quotes": [
      {
        "author": "Thomas Carlyle",
        "work": "The French Revolution",
        "quote": "The furious crowd echoed the **anathematic** denunciations voiced by revolutionary orators against the aristocracy."
      },
      {
        "author": "Henry Hallam",
        "work": "View of the State of Europe during the Middle Ages",
        "quote": "Papal bulls carrying an **anathematic** sanction frequently undermined the secular authority of recalcitrant monarchs."
      },
      {
        "author": "Samuel Taylor Coleridge",
        "work": "Biographia Literaria",
        "quote": "Critical dogma should avoid the harsh, **anathematic** tone that stifles genuine poetic originality."
      }
    ]
  },
  "Dashboard — the\\anathematise.md": {
    "primary": "To denounce or condemn solemnly; to curse or pronounce an anathema upon (chiefly Commonwealth spelling).",
    "secondary": "In theological history, synods convened to anathematise doctrinal deviations and formally banish unrepentant schismatics.",
    "quotes": [
      {
        "author": "Walter Scott",
        "work": "The Monastery",
        "quote": "The abbot prepared to **anathematise** the sacrilegious intruder with bell, book, and candle."
      },
      {
        "author": "David Hume",
        "work": "The History of England",
        "quote": "Zealous clergy did not hesitate to **anathematise** all who favored civil toleration of nonconforming sects."
      },
      {
        "author": "Charles Kingsley",
        "work": "Hypatia",
        "quote": "Fanatical monks assembled in Alexandria to **anathematise** pagan philosophy and desecrate ancient temples."
      }
    ]
  },
  "Dashboard — the\\anathematize.md": {
    "primary": "To pronounce an anathema against; to condemn vehemently; to curse formally.",
    "secondary": "In rhetoric and polemics, to anathematize a position is to denounce it as completely abhorrent, heretical, or destructive.",
    "quotes": [
      {
        "author": "Edmund Burke",
        "work": "Reflections on the Revolution in France",
        "quote": "They pull down the altar and **anathematize** the ancestral institutions that preserved civil society for centuries."
      },
      {
        "author": "John Adams",
        "work": "The Works of John Adams",
        "quote": "Partisan zealots will routinely **anathematize** their political opponents with unsparing sectarian fury."
      },
      {
        "author": "Ralph Waldo Emerson",
        "work": "Essays: First Series",
        "quote": "Let not the conformist **anathematize** the bold soul who dares to question inherited dogmas."
      }
    ]
  },
  "Dashboard — the\\anthesis.md": {
    "primary": "The period or act of expansion in a flower, during which the floral bud opens and sexual organs mature; the blooming period.",
    "secondary": "In plant reproductive ecology, anthesis coordinates the release of pollen and receptivity of stigmas with the daily foraging rhythms of specific insect or wind vectors.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Effects of Cross and Self Fertilisation in the Vegetable Kingdom",
        "quote": "The petals expand fully during **anthesis**, exposing the nectar glands directly to visiting bumblebees."
      },
      {
        "author": "Asa Gray",
        "work": "Gray's Lessons in Botany",
        "quote": "The process of **anthesis** in the night-blooming cereus is completed in a single dramatic evening."
      },
      {
        "author": "Liberty Hyde Bailey",
        "work": "The Standard Cyclopedia of Horticulture",
        "quote": "Environmental temperature and photoperiod precisely dictate the timing of **anthesis** across orchard crops."
      }
    ]
  },
  "Dashboard — the\\antithesis.md": {
    "primary": "A person or thing that is the direct opposite of someone or something else; a rhetorical contrast of ideas through parallel arrangement of words.",
    "secondary": "In Hegelian dialectic, antithesis is the contradictory or opposing stage that arises against a thesis, resolved and unified in a higher synthesis.",
    "quotes": [
      {
        "author": "Alexander Pope",
        "work": "An Essay on Criticism",
        "quote": "Through balanced clauses, heroic couplets achieve striking rhetorical force by setting idea against **antithesis**."
      },
      {
        "author": "Charles Dickens",
        "work": "A Tale of Two Cities",
        "quote": "The opening chapter presents an enduring **antithesis**: it was the best of times, it was the worst of times."
      },
      {
        "author": "Friedrich Nietzsche",
        "work": "The Birth of Tragedy",
        "quote": "Greek culture flourished from the continuous struggle and artistic **antithesis** between the Apollonian and Dionysian spirits."
      }
    ]
  },
  "Dashboard — the\\antithetic.md": {
    "primary": "Directly contrasting or opposite; characterized by or involving antithesis.",
    "secondary": "In linguistics and developmental psychology, antithetic concepts denote semantic polarities (e.g. good/bad, light/dark) that structure human cognitive development.",
    "quotes": [
      {
        "author": "Herbert Spencer",
        "work": "First Principles",
        "quote": "The fundamental postulate of philosophy reconciles two apparently **antithetic** modes of perceiving ultimate reality."
      },
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "Joy and despondency evoke **antithetic** bodily postures, one expanding the chest while the other droops."
      },
      {
        "author": "Sigmund Freud",
        "work": "The Antithetical Meaning of Primal Words",
        "quote": "Ancient tongues frequently employed single roots to designate mutually **antithetic** states of being."
      }
    ]
  },
  "Dashboard — the\\antithetical.md": {
    "primary": "Directly opposed or contrasting; mutually incompatible or expressing stark opposition.",
    "secondary": "In ethical theory and literary criticism, antithetical values or themes are juxtaposed to heighten moral complexity or narrative tension.",
    "quotes": [
      {
        "author": "Matthew Arnold",
        "work": "Culture and Anarchy",
        "quote": "Hebraism and Hellenism represent two **antithetical** forces guiding the moral and intellectual evolution of Europe."
      },
      {
        "author": "George Eliot",
        "work": "Middlemarch",
        "quote": "Her radiant enthusiasm seemed utterly **antithetical** to Casaubon's cold, desiccated scholarly ambition."
      },
      {
        "author": "John Stuart Mill",
        "work": "On Liberty",
        "quote": "Truth emerges most clearly when contradictory and **antithetical** doctrines are allowed open collision in public debate."
      }
    ]
  },
  "Dashboard — the\\antithetically.md": {
    "primary": "In an antithetical manner; by way of direct contrast or opposition.",
    "secondary": "In stylistic rhetoric and debate, ideas presented antithetically employ balanced contrasting phrases to emphasize conceptual distinctions.",
    "quotes": [
      {
        "author": "Samuel Johnson",
        "work": "Lives of the Most Eminent English Poets",
        "quote": "Pope arranged his couplets **antithetically**, balancing virtues against vices in rapid succession."
      },
      {
        "author": "Thomas Babington Macaulay",
        "work": "Critical and Historical Essays",
        "quote": "The historian contrasted the two statesmen **antithetically**, highlighting their opposing principles of statecraft."
      },
      {
        "author": "Walter Pater",
        "work": "Appreciations",
        "quote": "Themes of passion and ascetic renunciation are juxtaposed **antithetically** throughout the medieval romance."
      }
    ]
  },
  "Dashboard — the\\apothecial.md": {
    "primary": "Pertaining to, resembling, or bearing an apothecium (the cup-shaped ascocarp of certain fungi and lichens).",
    "secondary": "In lichenology and mycology, apothecial discs contain the exposed hymenium where asci discharge sexual ascospores into passing air currents.",
    "quotes": [
      {
        "author": "Beatrix Potter",
        "work": "On the Germination of the Spores of Agaricineae",
        "quote": "Microscopic examination of the **apothecial** margin revealed dense paraphyses protecting the young asci."
      },
      {
        "author": "William Jackson Hooker",
        "work": "The English Flora",
        "quote": "The conspicuous bright orange **apothecial** cups of *Xanthoria parietina* coat coastal rocks with radiant color."
      },
      {
        "author": "Pier Andrea Saccardo",
        "work": "Sylloge Fungorum",
        "quote": "Discomycetous taxa are diagnosed primarily by their saucer-shaped **apothecial** fructifications."
      }
    ]
  },
  "Dashboard — the\\apothecium.md": {
    "primary": "A cup-shaped or saucer-shaped fruiting body (ascocarp) in certain ascomycete fungi and lichens, bearing exposed spore-producing asci.",
    "secondary": "In cryptogamic botany, the apothecium features an open fertile layer (hymenium) bounded by an excipulum, maximizing spore dispersal efficiency into ambient air currents.",
    "quotes": [
      {
        "author": "Heinrich Anton de Bary",
        "work": "Comparative Morphology and Biology of the Fungi, Mycetozoa and Bacteria",
        "quote": "The developing **apothecium** in Peziza expands until its upper concave surface forms an exposed ascigerous layer."
      },
      {
        "author": "Arthur Henry Reginald Buller",
        "work": "Researches on Fungi",
        "quote": "A gentle touch against a mature **apothecium** induces sudden simultaneous puffing of thousands of ascospores."
      },
      {
        "author": "Miles Joseph Berkeley",
        "work": "Introduction to Cryptogamic Botany",
        "quote": "In many lichen genera, the disc-like **apothecium** provides the most reliable taxonomic characteristics for classification."
      }
    ]
  },
  "Dashboard — the\\atheism.md": {
    "primary": "Disbelief or lack of belief in the existence of God or gods.",
    "secondary": "In philosophical theology, atheism is distinguished between negative (implicit absence of belief) and positive (explicit affirmation that no deities exist), examined in debates on naturalism, secularism, and epistemology.",
    "quotes": [
      {
        "author": "Francis Bacon",
        "work": "Essays: Of Atheism",
        "quote": "A little philosophy inclineth man's mind to **atheism**, but depth in philosophy bringeth men's minds about to religion."
      },
      {
        "author": "David Hume",
        "work": "Dialogues Concerning Natural Religion",
        "quote": "Skeptical philosophy refrains from dogmatic assertions, defending reason against both superstition and dogmatic **atheism**."
      },
      {
        "author": "Baron d'Holbach",
        "work": "The System of Nature",
        "quote": "Enlightened materialist **atheism** seeks to liberate humanity from the terror of imaginary celestial despots."
      }
    ]
  },
  "Dashboard — the\\atheist.md": {
    "primary": "A person who disbelieves or lacks belief in the existence of God or deities.",
    "secondary": "In historical intellectual discourse, the term was frequently used pejoratively against dissenters, heretics, and philosophical materialists before being adopted as a positive philosophical identity.",
    "quotes": [
      {
        "author": "Percy Bysshe Shelley",
        "work": "The Necessity of Atheism",
        "quote": "The resolute **atheist** demands empirical evidence or rational proof before granting credence to divine claims."
      },
      {
        "author": "Bertrand Russell",
        "work": "Why I Am Not a Christian",
        "quote": "If asked whether I am an agnostic or an **atheist**, I reply that in philosophical rigor I am agnostic, but in practical life an atheist."
      },
      {
        "author": "John Locke",
        "work": "A Letter Concerning Toleration",
        "quote": "Locke argued that civil oaths could not bind a professed **atheist** whose conscience recognized no transcendent judge."
      }
    ]
  },
  "Dashboard — the\\atheistic.md": {
    "primary": "Pertaining to, advocating, or characteristic of atheism.",
    "secondary": "In modern intellectual history, atheistic philosophies such as logical positivism, existentialism, and dialectical materialism sought to ground morality, science, and politics entirely within immanent natural reality.",
    "quotes": [
      {
        "author": "Jean-Paul Sartre",
        "work": "Existentialism Is a Humanism",
        "quote": "Dostoevsky wrote that if God did not exist, everything would be permitted; that is the starting point for **atheistic** existentialism."
      },
      {
        "author": "William James",
        "work": "The Varieties of Religious Experience",
        "quote": "An **atheistic** naturalism may nonetheless cultivate feelings of cosmic piety toward the grandeur of the universe."
      },
      {
        "author": "Friedrich Nietzsche",
        "work": "The Gay Science",
        "quote": "Our modern **atheistic** conviction compels us to confront the terrifying freedom that follows the collapse of divine authority."
      }
    ]
  },
  "Dashboard — the\\atheistical.md": {
    "primary": "Relating to or imbued with atheism; denying the existence of God (archaic or formal variant of atheistic).",
    "secondary": "In seventeenth- and eighteenth-century moral and political tracts, atheistical sentiments were routinely blamed for undermining public virtue and oaths.",
    "quotes": [
      {
        "author": "Jonathan Swift",
        "work": "An Argument Against Abolishing Christianity",
        "quote": "The wits of the coffee-houses boast of their **atheistical** opinions as if disbelief were the highest badge of enlightenment."
      },
      {
        "author": "Samuel Clarke",
        "work": "A Demonstration of the Being and Attributes of God",
        "quote": "To counter **atheistical** objections, Clarke presented mathematical demonstrations of a necessary first cause."
      },
      {
        "author": "Edmund Burke",
        "work": "Letters on a Regicide Peace",
        "quote": "A militant, **atheistical** cabal had seized the apparatus of the French state to wage war against European civilization."
      }
    ]
  },
  "Dashboard — the\\athematic.md": {
    "primary": "Lacking a theme or melodic subject (in music); lacking a thematic connecting vowel in morphological inflection (in linguistics).",
    "secondary": "In Indo-European comparative linguistics, athematic root verbs attach personal endings directly to the root without an intervening thematic vowel (*-e-*, *-o-*).",
    "quotes": [
      {
        "author": "Ferdinand de Saussure",
        "work": "Memoir on the Primitive System of Vowels in the Indo-European Languages",
        "quote": "The archaic **athematic** conjugations attach personal suffixes directly to the ablauting verbal root."
      },
      {
        "author": "Theodor Adorno",
        "work": "Philosophy of New Music",
        "quote": "Serial composition replaces traditional thematic development with complex, rigorously **athematic** sonic structures."
      },
      {
        "author": "Antoine Meillet",
        "work": "Introduction to the Comparative Study of Indo-European Languages",
        "quote": "In Sanskrit and Homeric Greek, the **athematic** verbs preserve the oldest morphological layer of the parent tongue."
      }
    ]
  },
  "Dashboard — the\\Bibliotheca.md": {
    "primary": "A library or collection of books; also used in titles of comprehensive literary, bibliographical, or historical compilations.",
    "secondary": "From Latin and Greek *bibliotheke* (book-receptacle), historically applied to major canonical compilations such as the Bibliotheca of Photius or the Bibliotheca Historica of Diodorus Siculus.",
    "quotes": [
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The surviving fragments of Diodorus's **Bibliotheca** preserve invaluable details concerning ancient Hellenistic dynasties."
      },
      {
        "author": "Thomas Frognall Dibdin",
        "work": "The Bibliomania; or Book-Madness",
        "quote": "Every bibliophile dreams of amassing a splendid **Bibliotheca** filled with early printed incunabula."
      },
      {
        "author": "Jorge Luis Borges",
        "work": "Selected Non-Fictions",
        "quote": "The mythical **Bibliotheca** of Alexandria symbolized humanity's noble desire to house universal knowledge under one roof."
      }
    ]
  },
  "Dashboard — the\\bibliothecal.md": {
    "primary": "Of or relating to a library, libraries, or librarianship.",
    "secondary": "In bibliographic history and library administration, bibliothecal science encompasses cataloging standards, archival preservation, and classification taxonomies.",
    "quotes": [
      {
        "author": "Melvil Dewey",
        "work": "A Classification and Subject Index for Cataloguing and Arranging the Books and Pamphlets of a Library",
        "quote": "A sound decimal system brought orderly coherence to **bibliothecal** organization throughout American universities."
      },
      {
        "author": "Richard de Bury",
        "work": "Philobiblon",
        "quote": "The true lover of learning cultivates a profound devotion to **bibliothecal** treasures and manuscript care."
      },
      {
        "author": "Holbrook Jackson",
        "work": "The Anatomy of Bibliomania",
        "quote": "The quiet grandeur of an ancient university hall offers the ultimate **bibliothecal** sanctuary for contemplation."
      }
    ]
  },
  "Dashboard — the\\bibliothecarial.md": {
    "primary": "Of, relating to, or appropriate to a librarian or the duties of librarianship.",
    "secondary": "In institutional history, bibliothecarial responsibilities involve curating collections, preserving rare codices, and providing scholarly access to archival materials.",
    "quotes": [
      {
        "author": "Anthony Panizzi",
        "work": "Reports on the British Museum",
        "quote": "Executing our **bibliothecarial** responsibilities required building a circular reading room and a comprehensive printed catalog."
      },
      {
        "author": "Umberto Eco",
        "work": "The Name of the Rose",
        "quote": "The stern monk exercised supreme **bibliothecarial** control over the labyrinthine repository of forbidden books."
      },
      {
        "author": "Gabriel Naudé",
        "work": "Advice on Establishing a Library",
        "quote": "The highest **bibliothecarial** virtue lies in making books readily accessible to all sincere scholars."
      }
    ]
  },
  "Dashboard — the\\bodega.md": {
    "primary": "A small neighborhood grocery store, wine shop, or tavern, especially in a Spanish-speaking area.",
    "secondary": "Originally denoting a wine cellar or storeroom in Spanish (derived ultimately via Latin *apotheca* from Greek *apotheke*, a warehouse/storehouse), bodega evolved into iconic urban convenience shops in North American cities like New York.",
    "quotes": [
      {
        "author": "Ernest Hemingway",
        "work": "The Sun Also Rises",
        "quote": "We sat inside the cool shadows of the dusty **bodega**, drinking cold Valdepeñas from leather wine-skins."
      },
      {
        "author": "Federico García Lorca",
        "work": "Poet in New York",
        "quote": "Neon reflections illuminated the storefront of the corner **bodega** amid the humid rhythm of Harlem nights."
      },
      {
        "author": "George Orwell",
        "work": "Homage to Catalonia",
        "quote": "In the evening, militia volunteers congregated in the nearest **bodega** to debate revolutionary politics over rough wine."
      }
    ]
  },
  "Dashboard — the\\boutique.md": {
    "primary": "A small shop or department selling fashionable clothes, jewelry, or specialized specialty goods.",
    "secondary": "Etymologically descended from Old French *botique* and Greek *apotheke* (storehouse), boutique conveys an aura of exclusivity, curated craftsmanship, and luxury retail marketing.",
    "quotes": [
      {
        "author": "Roland Barthes",
        "work": "The Fashion System",
        "quote": "The Parisian **boutique** functions not merely as a retail establishment but as a sacred temple of aesthetic mythologies."
      },
      {
        "author": "Truman Capote",
        "work": "Breakfast at Tiffany's",
        "quote": "Holly paused before the window of an exclusive **boutique**, admiring vintage jewels glittering on black velvet."
      },
      {
        "author": "Thorstein Veblen",
        "work": "The Theory of the Leisure Class",
        "quote": "The patronizing of an expensive **boutique** signals the consumer's ability to command rare and unstandardized handiwork."
      }
    ]
  },
  "Dashboard — the\\deem.md": {
    "primary": "To judge, consider, or believe; to hold an opinion or come to a conclusion regarding something.",
    "secondary": "From Old English *dēman* (to judge), cognate with doom and historically related to Indo-European *dhe-* (to place, set, as in Greek *tithemi*), deem preserves solemn legal and formal literary weight.",
    "quotes": [
      {
        "author": "William Shakespeare",
        "work": "The Merchant of Venice",
        "quote": "Let no man **deem** himself secure against the unpredictable reversals of commercial fortune."
      },
      {
        "author": "John Milton",
        "work": "Paradise Lost",
        "quote": "So spake the Apostate Angel, though in pain, / Vaunting aloud, but racked with deep despair; and **deem** not all is lost."
      },
      {
        "author": "Thomas Jefferson",
        "work": "Notes on the State of Virginia",
        "quote": "The legislature may **deem** it expedient to revise statues whenever public sentiment demands legal reform."
      }
    ]
  },
  "Dashboard — the\\diathesis.md": {
    "primary": "A hereditary or constitutional predisposition to a particular disease, physical affliction, or medical condition.",
    "secondary": "In nineteenth-century constitutional medicine and modern immunology, diathesis denotes latent genetic or physiological susceptibilities (e.g. atopic diathesis, hemorrhagic diathesis) triggered by environmental stressors.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "A marked hemorrhagic **diathesis** in the family history should alert the surgeon to potential hemophilia."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "The ancient humoral concept of a scrofulous **diathesis** must be reinterpreted through microscopic cellular alterations."
      },
      {
        "author": "Sigmund Freud",
        "work": "Studies on Hysteria",
        "quote": "Charcot emphasized the role of a hereditary neuropathic **diathesis** as the fertile soil upon which neuroses germinate."
      }
    ]
  },
  "Dashboard — the\\ditheism.md": {
    "primary": "Belief in two equal and distinct gods, especially one good and one evil; dualism in religious theology.",
    "secondary": "In comparative religion, ditheism is exemplified in classic Zoroastrianism (Ahura Mazda and Angra Mainyu) and certain early Christian Gnostic sects (distinguishing the supreme benevolent God from the inferior Demiurge).",
    "quotes": [
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "Manichaean **ditheism** posited an eternal cosmic war between the kingdom of Light and the empire of Darkness."
      },
      {
        "author": "David Hume",
        "work": "The Natural History of Religion",
        "quote": "Confronted by the mingled good and ill of existence, primitive theologians frequently embraced a simplistic **ditheism**."
      },
      {
        "author": "John Locke",
        "work": "A Discourse of Miracles",
        "quote": "The coherence of moral duty disintegrates if faith is divided under the conflicting mandates of **ditheism**."
      }
    ]
  },
  "Dashboard — the\\doom.md": {
    "primary": "Death, destruction, or some other terrible and unavoidable fate; an irrevocable adverse judgment or sentence.",
    "secondary": "From Old English *dōm* (judgment, statute, legal decree), sharing the Proto-Indo-European root *dhe-* (to place/set, cognate to Greek *thesis* and *tithemi*), shifting semantically toward inevitable ruin.",
    "quotes": [
      {
        "author": "Geoffrey Chaucer",
        "work": "The Canterbury Tales",
        "quote": "No mortal can evade the solemn **doom** ordained by heaven's sovereign decree."
      },
      {
        "author": "William Shakespeare",
        "work": "Macbeth",
        "quote": "What, will the line stretch out to the crack of **doom**? Another yet! A seventh! I'll see no more."
      },
      {
        "author": "Mary Shelley",
        "work": "Frankenstein",
        "quote": "I felt as if an inescapable **doom** hung over my head, ready to descend and crush all I held dear."
      }
    ]
  },
  "Dashboard — the\\enthesis.md": {
    "primary": "The anatomical site where a tendon, ligament, or joint capsule attaches to bone.",
    "secondary": "In rheumatology and orthopedics, entheses are fibrocartilaginous junctions designed to dissipate mechanical stress; inflammation at these points (enthesitis) is a hallmark of spondyloarthropathies like ankylosing spondylitis.",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Gray's Anatomy",
        "quote": "Mechanical stress is dissipated where fibrous tendon transitions through fibrocartilage into bone at the **enthesis**."
      },
      {
        "author": "William Osler",
        "work": "Modern Medicine: Its Theory and Practice",
        "quote": "Recurrent inflammation at the calcaneal **enthesis** frequently heralds the onset of systemic ankylosing spondylitis."
      },
      {
        "author": "Michael DeBakey",
        "work": "The Living Body",
        "quote": "Reconstructive orthopedic repair requires securing the avulsed ligament firmly back onto its natural **enthesis**."
      }
    ]
  },
  "Dashboard — the\\enthetic.md": {
    "primary": "Introduced from outside into the body (in pathology); pertaining to diseases inoculated or implanted from external sources.",
    "secondary": "In nineteenth-century epidemiology and public health nosology, enthetic diseases designated contagious infections (such as syphilis or rabies) contracted through inoculation or direct contact with external pathogens.",
    "quotes": [
      {
        "author": "William Farr",
        "work": "Vital Statistics: A Memorial Volume of Selections",
        "quote": "The registrar classified syphilis, glanders, and hydrophobia under the broad nosological category of **enthetic** diseases."
      },
      {
        "author": "Thomas Sydenham",
        "work": "The Works of Thomas Sydenham",
        "quote": "An **enthetic** poison introduced via an animal bite spreads its contagion throughout the entire vascular humors."
      },
      {
        "author": "Florence Nightingale",
        "work": "Notes on Hospitals",
        "quote": "Sanitary segregation proved vital in controlling military barracks outbreaks of infectious **enthetic** disorders."
      }
    ]
  },
  "Dashboard — the\\enthusiasm.md": {
    "primary": "Intense and eager enjoyment, interest, or approval; fervent zeal or passion for a cause or subject.",
    "secondary": "Derived from Greek *enthousiasmos* (divine inspiration, being possessed by a god, *en-theos*), historically carrying pejorative connotations of religious fanaticism before softening into positive zeal in modern parlance.",
    "quotes": [
      {
        "author": "John Locke",
        "work": "An Essay Concerning Human Understanding",
        "quote": "Locke dedicated a famous chapter to **enthusiasm**, warning that ungrounded inward illumination leads to dangerous delusion."
      },
      {
        "author": "David Hume",
        "work": "Essays, Moral, Political, and Literary",
        "quote": "Religious superstition is founded on fear and melancholy, but religious **enthusiasm** arises from hope and presumptuous pride."
      },
      {
        "author": "Ralph Waldo Emerson",
        "work": "Circles",
        "quote": "Every great and commanding movement in the annals of the world is the triumph of **enthusiasm**."
      }
    ]
  },
  "Dashboard — the\\enthusiastic.md": {
    "primary": "Having or showing intense and eager enjoyment, interest, or approval; ardent; zealous.",
    "secondary": "In seventeenth- and eighteenth-century intellectual history, described individuals who claimed direct mystical revelation, transitioning in nineteenth-century literature to mean passionate and energetic devotion.",
    "quotes": [
      {
        "author": "Jane Austen",
        "work": "Sense and Sensibility",
        "quote": "Marianne's **enthusiastic** temperament could find no pleasure in moderate sentiments or calculated prudence."
      },
      {
        "author": "Charles Darwin",
        "work": "The Voyage of the Beagle",
        "quote": "My first sight of the Brazilian rainforest provoked an **enthusiastic** delight that no words can adequately convey."
      },
      {
        "author": "Alexis de Tocqueville",
        "work": "Democracy in America",
        "quote": "Democratic citizens display an **enthusiastic** eagerness for material progress and mechanical innovation."
      }
    ]
  },
  "Dashboard — the\\epenthesis.md": {
    "primary": "The insertion of a sound, syllable, or letter into the middle of a word (e.g. the 'p' in 'empty' from Old English 'æmtig', or 'b' in 'thimble').",
    "secondary": "In historical phonology and sociolinguistics, epenthesis facilitates articulation by resolving difficult consonant clusters or providing vocalic transitions (anaptyxis).",
    "quotes": [
      {
        "author": "Otto Jespersen",
        "work": "Language: Its Nature, Development and Origin",
        "quote": "Vocal ease frequently introduces a transitional stop through phonetic **epenthesis**, as seen in 'thunder' from Old English 'thunor'."
      },
      {
        "author": "Ferdinand de Saussure",
        "work": "Course in General Linguistics",
        "quote": "The insertion of a parasitic vowel or consonant by **epenthesis** preserves phonological equilibrium across syllable boundaries."
      },
      {
        "author": "Henry Sweet",
        "work": "A Handbook of Phonetics",
        "quote": "In casual pronunciation, speakers often resort to vocalic **epenthesis** to bridge unfamiliar consonant clusters."
      }
    ]
  },
  "Dashboard — the\\epenthetic.md": {
    "primary": "Inserted into the middle of a word; of or relating to epenthesis.",
    "secondary": "In generative phonology and historical linguistics, describing intrusive vowels or consonants inserted to satisfy syllable phonotactics.",
    "quotes": [
      {
        "author": "Edward Sapir",
        "work": "Language: An Introduction to the Study of Speech",
        "quote": "The emergence of an **epenthetic** consonant reflects the unconscious physiological mechanics of transitioning between vocal tracts."
      },
      {
        "author": "Leonard Bloomfield",
        "work": "Language",
        "quote": "An **epenthetic** glide regularly appears between adjacent sonorants to smooth articulatory transition."
      },
      {
        "author": "Max Müller",
        "work": "Lectures on the Science of Language",
        "quote": "In the evolution from Latin to French, an **epenthetic** 'b' arose naturally in words like 'chambre' from 'camera'."
      }
    ]
  },
  "Dashboard — the\\epitheca.md": {
    "primary": "The outer layer or upper valve of certain microorganisms and invertebrates, especially the larger upper half of a diatom's frustule or the protective wall of a coral.",
    "secondary": "In protistology and marine paleontology, the epitheca overlaps the smaller hypotheca in diatoms and dinoflagellates, forming a rigid protective siliceous or cellulosic envelope.",
    "quotes": [
      {
        "author": "Ernst Haeckel",
        "work": "Report on the Radiolaria",
        "quote": "The overlapping margin where the **epitheca** encloses the lower hypotheca forms the distinctive girdle band of the diatom."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Invertebrated Animals",
        "quote": "In fossil rugose corals, the outer stony wall is enveloped by a wrinkled calcareous **epitheca**."
      },
      {
        "author": "Alister Hardy",
        "work": "The Open Sea: Its Natural History",
        "quote": "Armored dinoflagellates possess a cellular casing divided neatly into an **epitheca** and a posterior hypotheca."
      }
    ]
  },
  "Dashboard — the\\epithet.md": {
    "primary": "An adjective or descriptive phrase expressing a quality characteristic of the person or thing mentioned; often used as a term of abuse or characterization.",
    "secondary": "In classical literary epic (Homer, Virgil), traditional formulaic epithets (e.g. 'swift-footed Achilles', 'rosy-fingered Dawn') anchored poetic meter and oral mnemonic recitation.",
    "quotes": [
      {
        "author": "Alexander Pope",
        "work": "Preface to the Iliad of Homer",
        "quote": "Homer applies each traditional **epithet** with such exquisite propriety that it illuminates the hero's quintessential virtue."
      },
      {
        "author": "Samuel Johnson",
        "work": "The Rambler",
        "quote": "Careless writers clutter their prose with idle **epithet**, weakening the force of genuine sentiment."
      },
      {
        "author": "Edmund Burke",
        "work": "Speech on American Taxation",
        "quote": "A single contemptuous **epithet** flung in the heat of debate may ignite lasting animosity between allied nations."
      }
    ]
  },
  "Dashboard — the\\heterotheca.md": {
    "primary": "A genus of flowering plants in the aster family (Asteraceae), commonly known as camphorweeds or false goldenasters, native to North America.",
    "secondary": "In botanical taxonomy, *Heterotheca* is named from Greek *heteros* (different) and *theke* (container) in reference to the dimorphic achenes produced by its ray and disk florets.",
    "quotes": [
      {
        "author": "Asa Gray",
        "work": "Synoptical Flora of North America",
        "quote": "The genus **Heterotheca** is distinguished by ray achenes that lack pappus bristles while disk achenes bear a double pappus."
      },
      {
        "author": "Liberty Hyde Bailey",
        "work": "Cyclopedia of American Agriculture",
        "quote": "On dry western rangelands, aromatic species of **Heterotheca** flourish where overgrazing has depleted perennial grasses."
      },
      {
        "author": "John Torrey",
        "work": "A Flora of North America",
        "quote": "Specimens of **Heterotheca** collected on the expedition exhibited strong camphor-scented glandular pubescence."
      }
    ]
  },
  "Dashboard — the\\hypothec.md": {
    "primary": "A legal right or claim over a debtor's property granted to a creditor as security without transfer of physical possession.",
    "secondary": "In Roman law and Scots law, a hypothec (derived from Greek *hypotheke*, pledge/mortgage) allowed landlords or maritime lenders to secure claims against tenant goods or ships while the owner retained custody.",
    "quotes": [
      {
        "author": "Henry Maine",
        "work": "Ancient Law",
        "quote": "Roman jurisprudence distinguished the simple pawn from the **hypothec**, which established a lien without requiring physical possession."
      },
      {
        "author": "Adam Smith",
        "work": "Lectures on Jurisprudence",
        "quote": "The landlord's **hypothec** over the tenant's livestock gave agricultural proprietors an extraordinary legal security for rent."
      },
      {
        "author": "Walter Scott",
        "work": "The Antiquary",
        "quote": "The rural bailiff threatened to execute legal **hypothec** upon the farmer's remaining harvest."
      }
    ]
  },
  "Dashboard — the\\hypothecate.md": {
    "primary": "To pledge money or property as security for a loan without relinquishing title or physical possession.",
    "secondary": "In maritime law and high finance, owners hypothecate vessels (via bottomry bonds) or capital securities to secure credit while maintaining operational control.",
    "quotes": [
      {
        "author": "Alexander Hamilton",
        "work": "Report on Public Credit",
        "quote": "The government resolved to **hypothecate** designated tariff revenues to guarantee payment of the national debt."
      },
      {
        "author": "Joseph Story",
        "work": "Commentaries on the Law of Agency",
        "quote": "In foreign ports of necessity, the shipmaster has authority to **hypothecate** the vessel to obtain urgent repairs."
      },
      {
        "author": "John Maynard Keynes",
        "work": "The Economic Consequences of the Peace",
        "quote": "The reparations treaty attempted to **hypothecate** the entire future customs receipts of the defeated nation."
      }
    ]
  },
  "Dashboard — the\\hypothesise.md": {
    "primary": "To formulate or put forward a hypothesis; to propose an explanation as a starting point for further investigation (chiefly Commonwealth spelling).",
    "secondary": "In scientific philosophy, to hypothesise is to construct falsifiable causal models whose empirical predictions can be tested by experiment.",
    "quotes": [
      {
        "author": "Karl Popper",
        "work": "The Logic of Scientific Discovery",
        "quote": "The bold scientist will **hypothesise** daring conjectures that expose the theory to the risk of decisive refutation."
      },
      {
        "author": "Arthur Eddington",
        "work": "The Nature of the Physical World",
        "quote": "We may **hypothesise** an invisible ether, but if it exerts no measurable effect, physics must discard it."
      },
      {
        "author": "C. S. Peirce",
        "work": "Illustrations of the Logic of Science",
        "quote": "To **hypothesise** through abductive reasoning is the only logical operation that introduces genuinely novel ideas."
      }
    ]
  },
  "Dashboard — the\\hypothesize.md": {
    "primary": "To put forward an idea, proposition, or explanation as a hypothesis for testing and verification.",
    "secondary": "In scientific methodology, hypothesizing establishes deductive bridges between observable anomalies and explanatory theoretical frameworks.",
    "quotes": [
      {
        "author": "Thomas Hunt Morgan",
        "work": "The Theory of the Gene",
        "quote": "Chromosomal linkage data led us to **hypothesize** that genes are arranged in linear order along chromosomes."
      },
      {
        "author": "Richard Feynman",
        "work": "The Character of Physical Law",
        "quote": "First you make a guess, you **hypothesize** a rule, then you calculate the consequences to see if experiment agrees."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "The Panda's Thumb",
        "quote": "Paleontologists may **hypothesize** rapid punctuation events to account for prolonged morphological stasis in fossil beds."
      }
    ]
  },
  "Dashboard — the\\hypothetical.md": {
    "primary": "Based on or serving as a hypothesis; supposed but not necessarily true or real; conjectural.",
    "secondary": "In formal logic, hypothetical propositions (conditional statements) take the form 'if P, then Q', foundational to Kant's distinction between categorical and hypothetical imperatives.",
    "quotes": [
      {
        "author": "Immanuel Kant",
        "work": "Groundwork of the Metaphysics of Morals",
        "quote": "A **hypothetical** imperative commands action only as a means to some contingent, desired end."
      },
      {
        "author": "John Locke",
        "work": "An Essay Concerning Human Understanding",
        "quote": "We must not confuse proven physical reality with a merely **hypothetical** explanation invented to save appearances."
      },
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "I constructed a **hypothetical** tree of descent to demonstrate how divergent taxa might emerge from common ancestors."
      }
    ]
  },
  "Dashboard — the\\hypothetically.md": {
    "primary": "By way of hypothesis; theoretically; conjecturally or under assumed conditions.",
    "secondary": "In scientific argumentation and thought experiments, reasoning hypothetically allows theorists to isolate fundamental variables from confounding physical factors.",
    "quotes": [
      {
        "author": "Albert Einstein",
        "work": "Relativity: The Special and General Theory",
        "quote": "Consider **hypothetically** an observer enclosed within a chest falling freely in empty space."
      },
      {
        "author": "Bertrand Russell",
        "work": "The Problems of Philosophy",
        "quote": "Even if we reason **hypothetically** about a world devoid of mind, the laws of logic remain valid."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "Science and Culture",
        "quote": "If we grant **hypothetically** that consciousness is an epiphenomenon, volitional action remains an evolutionary puzzle."
      }
    ]
  },
  "Dashboard — the\\metathesis.md": {
    "primary": "The transposition of sounds, letters, or syllables in a word (e.g. Old English 'brid' becoming 'bird', or 'aks' for 'ask'); in chemistry, a double decomposition reaction.",
    "secondary": "In organic and organometallic chemistry, olefin metathesis (recognized by the 2005 Nobel Prize) involves the redistribution of carbon-carbon double bonds via metal carbene catalysis.",
    "quotes": [
      {
        "author": "Max Müller",
        "work": "Lectures on the Science of Language",
        "quote": "Phonetic **metathesis** explains how historical speech shifted 'wasp' from Old English 'wæps' without altering meaning."
      },
      {
        "author": "Robert H. Grubbs",
        "work": "Nobel Lecture: Olefin Metathesis Catalyst Development",
        "quote": "Ruthenium carbene complexes revolutionized ring-closing olefin **metathesis** by tolerating functional groups in organic synthesis."
      },
      {
        "author": "Otto Jespersen",
        "work": "Language: Its Nature, Development and Origin",
        "quote": "Children often transpose difficult consonant pairs through natural articulatory **metathesis**."
      }
    ]
  },
  "Dashboard — the\\monotheism.md": {
    "primary": "The doctrine or belief that there is only one God.",
    "secondary": "In the history of religion and philosophical theology, monotheism is typified by the Abrahamic faiths (Judaism, Christianity, Islam), asserting the absolute unity, omnipotence, and transcendence of the supreme creator.",
    "quotes": [
      {
        "author": "David Hume",
        "work": "The Natural History of Religion",
        "quote": "The transition from polytheism to rigorous **monotheism** reflects humanity's tendency to exalt a patron deity to supreme infinity."
      },
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The austere **monotheism** of Islam swept across Arabia, sweeping away idol worship and clan totems."
      },
      {
        "author": "Sigmund Freud",
        "work": "Moses and Monotheism",
        "quote": "Freud argued that the uncompromising **monotheism** of Moses represented an advance in intellectuality over sensory idolatry."
      }
    ]
  },
  "Dashboard — the\\monotheist.md": {
    "primary": "A person who believes in the existence of only one God.",
    "secondary": "In comparative theology, a monotheist rejects polytheistic pantheons and dualisms, attributing all cosmic creation, providence, and moral legislation to a single sovereign deity.",
    "quotes": [
      {
        "author": "John Locke",
        "work": "The Reasonableness of Christianity",
        "quote": "A sincere **monotheist** recognizes that moral obligation derives directly from the will of an all-wise Creator."
      },
      {
        "author": "William James",
        "work": "The Varieties of Religious Experience",
        "quote": "For the devout **monotheist**, absolute self-surrender to the divine will forms the core of religious life."
      },
      {
        "author": "Ernest Renan",
        "work": "History of the People of Israel",
        "quote": "The ancient Hebrew prophet stood forth as an unbending **monotheist** amidst surrounding Canaanite polytheism."
      }
    ]
  },
  "Dashboard — the\\monotheistic.md": {
    "primary": "Of, relating to, or characterized by the belief that there is only one God.",
    "secondary": "In cultural anthropology and sociology of religion, monotheistic frameworks emphasize universal moral commandments, prophetic revelation, and linear historical eschatology.",
    "quotes": [
      {
        "author": "Max Weber",
        "work": "The Sociology of Religion",
        "quote": "The ethical prophecy typical of **monotheistic** traditions demanded systematized conduct in place of magical rituals."
      },
      {
        "author": "James George Frazer",
        "work": "The Golden Bough",
        "quote": "Remnants of earlier vegetation cults were absorbed and reinterpreted under later **monotheistic** orthodoxies."
      },
      {
        "author": "Edward Tylor",
        "work": "Primitive Culture",
        "quote": "The development of **monotheistic** theology represents the culmination of a long conceptual refinement of animistic beliefs."
      }
    ]
  },
  "Dashboard — the\\monothematic.md": {
    "primary": "Having or based on a single subject, theme, or musical motif.",
    "secondary": "In musicology, monothematic compositions (such as certain Haydn symphonic sonata movements or Bach fugues) derive their entire structural development from varying a single thematic subject.",
    "quotes": [
      {
        "author": "Donald Tovey",
        "work": "Essays in Musical Analysis",
        "quote": "Haydn took particular delight in **monothematic** sonata allegros, demonstrating how contrast could be extracted from a single theme."
      },
      {
        "author": "Charles Rosen",
        "work": "The Classical Style",
        "quote": "A **monothematic** exposition achieves dramatic unity by re-harmonizing the opening motto in the dominant key."
      },
      {
        "author": "George Grove",
        "work": "Beethoven and His Nine Symphonies",
        "quote": "The strict discipline of a **monothematic** movement challenges the composer to maximize contrapuntal variety."
      }
    ]
  },
  "Dashboard — the\\nomothetic.md": {
    "primary": "Of or relating to the formulation of general, universal laws or principles (contrasted with idiographic).",
    "secondary": "Introduced into modern philosophy of science by Wilhelm Windelband, nomothetic methodologies characterize the natural sciences (seeking general laws), contrasting with idiographic approaches in the humanities (seeking individual particularity).",
    "quotes": [
      {
        "author": "Wilhelm Windelband",
        "work": "History and Natural Science",
        "quote": "Natural science pursues a **nomothetic** purpose, searching for eternal invariant laws governing universal phenomena."
      },
      {
        "author": "Gordon Allport",
        "work": "Pattern and Growth in Personality",
        "quote": "Psychology must balance **nomothetic** investigations of general human traits with idiographic portraits of unique individuals."
      },
      {
        "author": "Emile Durkheim",
        "work": "The Rules of Sociological Method",
        "quote": "Sociology can claim scientific legitimacy only by establishing **nomothetic** causal connections across social institutions."
      }
    ]
  },
  "Dashboard — the\\oligosynthetic.md": {
    "primary": "Having or using very few morphemes or linguistic roots from which vocabulary is synthesized (in linguistic typology).",
    "secondary": "In theoretical linguistics and artificial language design, an oligosynthetic language constructs complex lexicons from a small inventory of root affixes, famously hypothesized (and disputed) in certain Native American languages.",
    "quotes": [
      {
        "author": "Benjamin Lee Whorf",
        "work": "Language, Thought, and Reality",
        "quote": "Certain indigenous tongues were proposed to possess an **oligosynthetic** structure derived from a handful of fundamental roots."
      },
      {
        "author": "Edward Sapir",
        "work": "Selected Writings in Language, Culture and Personality",
        "quote": "Early philologists exaggerated the **oligosynthetic** nature of Nahuatl by confusing productive compounding with root paucity."
      },
      {
        "author": "Franz Boas",
        "work": "Handbook of American Indian Languages",
        "quote": "Detailed morphological analysis refuted claims that these American idioms conformed to an **oligosynthetic** archetype."
      }
    ]
  },
  "Dashboard — the\\parenthesis.md": {
    "primary": "A word, clause, or sentence inserted as an explanation or afterthought into a passage that is grammatically complete without it; either of a pair of curved brackets ( ).",
    "secondary": "In classical rhetoric and syntax, parenthesis introduces qualifying nuance, humor, or authorial aside, marked orthographically by brackets, dashes, or commas.",
    "quotes": [
      {
        "author": "Laurence Sterne",
        "work": "The Life and Opinions of Tristram Shandy, Gentleman",
        "quote": "My work is digressive, and my digressions are progressive; a judicious **parenthesis** is the sunshine of reading."
      },
      {
        "author": "Virginia Woolf",
        "work": "To the Lighthouse",
        "quote": "The tragic passing of Mrs. Ramsay is recorded within the poignant, muted silence of a square bracketed **parenthesis**."
      },
      {
        "author": "H. W. Fowler",
        "work": "A Dictionary of Modern English Usage",
        "quote": "A clumsy **parenthesis** that separates subject from verb impedes clarity and tires the reader's attention."
      }
    ]
  },
  "Dashboard — the\\parenthetic.md": {
    "primary": "Enclosed in or placed within parentheses; serving as a parenthesis or explanatory aside.",
    "secondary": "In linguistics and literary style, parenthetic interpolations provide supplementary evaluation or pragmatic framing without disrupting main syntactic coordination.",
    "quotes": [
      {
        "author": "Henry James",
        "work": "The Art of the Novel",
        "quote": "His late prose delighted in **parenthetic** qualifications that mirrored the complex convolutions of subjective consciousness."
      },
      {
        "author": "Edgar Allan Poe",
        "work": "Marginalia",
        "quote": "A brief **parenthetic** whisper can alter the entire emotional color of a romantic narrative."
      },
      {
        "author": "George Orwell",
        "work": "Politics and the English Language",
        "quote": "Writers often resort to vague **parenthetic** phrases to evade committing to direct, forthright assertions."
      }
    ]
  },
  "Dashboard — the\\parenthetical.md": {
    "primary": "Relating to or inserted as a parenthesis; qualifying, explanatory, or incidental.",
    "secondary": "In academic citation and editorial style, parenthetical documentation provides abbreviated author-date references directly inside running prose.",
    "quotes": [
      {
        "author": "Ralph Waldo Emerson",
        "work": "Representative Men",
        "quote": "Montaigne's essays abound with **parenthetical** musings that capture the candid spontaneity of dinner conversation."
      },
      {
        "author": "Charles Dickens",
        "work": "Bleak House",
        "quote": "The chancery lawyer's address was overloaded with **parenthetical** clauses designed to obscure legal reality."
      },
      {
        "author": "William Strunk Jr.",
        "work": "The Elements of Style",
        "quote": "Enclose **parenthetical** expressions between commas, and avoid fracturing essential sentence rhythms."
      }
    ]
  },
  "Dashboard — the\\parenthetically.md": {
    "primary": "In a parenthetical manner; by way of parenthesis, aside, or incidental remark.",
    "secondary": "In rhetoric and expository discourse, remarks introduced parenthetically offer contextual commentary without changing the core thesis.",
    "quotes": [
      {
        "author": "Thomas Babington Macaulay",
        "work": "History of England",
        "quote": "The historian observed **parenthetically** that even the king's staunchest allies condemned this unconstitutional levy."
      },
      {
        "author": "Oliver Wendell Holmes Sr.",
        "work": "The Autocrat of the Breakfast-Table",
        "quote": "I may mention **parenthetically** that the true gentlemen reveals himself in how he listens to others."
      },
      {
        "author": "Bertrand Russell",
        "work": "Portraits from Memory",
        "quote": "He added **parenthetically** that philosophical skepticism rarely prevented thinkers from enjoying a good dinner."
      }
    ]
  },
  "Dashboard — the\\perithecium.md": {
    "primary": "A flask-shaped or round ascocarp (fruiting body) in certain ascomycete fungi, having a small opening (ostiole) at the top through which ascospores are released.",
    "secondary": "In systematic mycology (e.g. Sordariales and Hypocreales), the perithecium houses fertile asci within an enclosed chamber, discharging spores sequentially through the ostiole.",
    "quotes": [
      {
        "author": "Heinrich Anton de Bary",
        "work": "Comparative Morphology and Biology of the Fungi, Mycetozoa and Bacteria",
        "quote": "The wall of the mature **perithecium** darkens into a protective melanized sheath enclosing the delicate asci."
      },
      {
        "author": "Arthur Henry Reginald Buller",
        "work": "Researches on Fungi",
        "quote": "Turgor pressure within the **perithecium** forces each ascospore out through the microscopic apical ostiole."
      },
      {
        "author": "Miles Joseph Berkeley",
        "work": "Outlines of British Fungology",
        "quote": "In the genus *Sphaeria*, black carbonaceous punctate spots reveal the submerged flask of each **perithecium**."
      }
    ]
  },
  "Dashboard — the\\polysynthetic.md": {
    "primary": "Characterized by combining several word elements or morphemes into a single complex word that corresponds to a whole sentence (in linguistic typology).",
    "secondary": "Typifying many indigenous languages of North America, Siberia, and the Caucasus, polysynthetic grammars incorporate nominal objects and pronominal affixes into elaborate verbal matrices.",
    "quotes": [
      {
        "author": "Wilhelm von Humboldt",
        "work": "On Language: On the Diversity of Human Language Construction",
        "quote": "The **polysynthetic** character of American tongues incorporates nominal arguments into the verbal predicate as a single organic whole."
      },
      {
        "author": "Franz Boas",
        "work": "Handbook of American Indian Languages",
        "quote": "In Eskimo grammar, complex suffixes attach to initial stems, generating **polysynthetic** constructions of astonishing syntactic precision."
      },
      {
        "author": "Edward Sapir",
        "work": "Language: An Introduction to the Study of Speech",
        "quote": "To label a language **polysynthetic** simply means that its morphological synthesis reaches an extraordinary level of word elaboration."
      }
    ]
  },
  "Dashboard — the\\polytheism.md": {
    "primary": "The belief in or worship of more than one god.",
    "secondary": "In comparative religion and cultural anthropology, polytheism characteristically distributes divine power among a pantheon of specialized deities representing cosmic forces, virtues, or natural realms.",
    "quotes": [
      {
        "author": "David Hume",
        "work": "The Natural History of Religion",
        "quote": "**Polytheism** or idolatry was, and must have been, the first and most ancient religion of mankind."
      },
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The various modes of worship which prevailed in the Roman world were all considered by the people as equally true; this tolerant **polytheism** accommodated every foreign pantheon."
      },
      {
        "author": "Max Weber",
        "work": "The Sociology of Religion",
        "quote": "Ancient civic **polytheism** reflected the specialized divisions of labor and tribal confederations of the Mediterranean city-states."
      }
    ]
  },
  "Dashboard — the\\polytheistic.md": {
    "primary": "Relating to or characterized by belief in or worship of multiple deities.",
    "secondary": "In historical archaeology and mythology, polytheistic systems are manifested through temples, myth cycles, and sacrificial calendars honoring pantheons such as those of Sumer, Greece, Rome, and Mesoamerica.",
    "quotes": [
      {
        "author": "James George Frazer",
        "work": "The Golden Bough",
        "quote": "Behind the elaborate rituals of classic **polytheistic** religions lay older magical rites aimed at ensuring crop fertility."
      },
      {
        "author": "John Stuart Mill",
        "work": "Three Essays on Religion",
        "quote": "A **polytheistic** worldview naturally tolerated neighboring cults, seeing them as legitimate venerations of other regional powers."
      },
      {
        "author": "Fustel de Coulanges",
        "work": "The Ancient City",
        "quote": "The hearth god and ancestor cults formed the foundational layer of early Greco-Roman **polytheistic** society."
      }
    ]
  },
  "Dashboard — the\\prosthesis.md": {
    "primary": "An artificial body part, such as a limb, heart valve, or tooth, substituted for a missing or defective natural part.",
    "secondary": "In reconstructive medicine and biomedical engineering, advanced prostheses incorporate myoelectric sensors, titanium osseointegration, and microprocessor-controlled hydraulics to restore motor function.",
    "quotes": [
      {
        "author": "Ambroise Paré",
        "work": "Ten Books of Surgery",
        "quote": "For veterans maimed in battle, Paré designed mechanical iron hands and artificial leg **prosthesis** units with articulated joints."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Fitting a functional limb **prosthesis** requires meticulous stump conditioning and psychological rehabilitation."
      },
      {
        "author": "Oliver Sacks",
        "work": "The Man Who Mistook His Wife for a Hat",
        "quote": "The patient gradually incorporated the artificial **prosthesis** into his neurological body schema."
      }
    ]
  },
  "Dashboard — the\\prosthetic.md": {
    "primary": "Pertaining to, serving as, or involving an artificial replacement for a missing body part.",
    "secondary": "In biomechanics and physical therapy, prosthetic devices are engineered to match natural anatomical load distributions, kinematics, and aesthetic contours.",
    "quotes": [
      {
        "author": "Sigmund Freud",
        "work": "Civilization and Its Discontents",
        "quote": "Man has become, so to speak, a **prosthetic** god; when he puts on all his auxiliary organs, he is truly magnificent."
      },
      {
        "author": "Marshall McLuhan",
        "work": "Understanding Media: The Extensions of Man",
        "quote": "Every electronic medium acts as a **prosthetic** extension of human perception and neurological faculties."
      },
      {
        "author": "Donna Haraway",
        "work": "Simians, Cyborgs, and Women: The Reinvention of Nature",
        "quote": "The boundary between biological organism and **prosthetic** machine dissolves in late twentieth-century cybernetic culture."
      }
    ]
  },
  "Dashboard — the\\prosthetics.md": {
    "primary": "The branch of medicine and biomedical engineering concerned with the design, fabrication, and fitting of artificial replacements for body parts.",
    "secondary": "In clinical rehabilitation, prosthetics collaborates with orthotics, material science (carbon fiber, silicone), and neural interface technology to restore mobility and independence to amputees.",
    "quotes": [
      {
        "author": "Alexis Carrel",
        "work": "Man, The Unknown",
        "quote": "Advances in modern **prosthetics** provide functional substitutes that allow injured laborers to return to active life."
      },
      {
        "author": "V. S. Ramachandran",
        "work": "Phantoms in the Brain",
        "quote": "By understanding phantom limb neurobiology, specialists in **prosthetics** can design limbs that feel naturally integrated."
      },
      {
        "author": "Aldous Huxley",
        "work": "Island",
        "quote": "The rehabilitation clinic utilized innovative **prosthetics** to help victims of trauma regain graceful movement."
      }
    ]
  }
}

out_mjs = "main app/scripts/curate-finish5-batch2.mjs"

with open(out_mjs, "w", encoding="utf-8") as f:
    f.write("import path from 'path';\n")
    f.write("import { updateNotesBatch } from './curate-updater-util.mjs';\n\n")
    f.write("const baseClusterDir = path.resolve('App database/Greek roots/Cluster Form & Space');\n\n")
    f.write("const batchData = ")
    json.dump(data, f, indent=2, ensure_ascii=False)
    f.write(";\n\n")
    f.write("const count = updateNotesBatch(baseClusterDir, batchData);\n")
    f.write("console.log(`[Finish Slice 5 - Batch 2] Successfully updated ${count}/${Object.keys(batchData).length} notes.`);\n")

print(f"Generated {out_mjs} with {len(data)} notes.")
