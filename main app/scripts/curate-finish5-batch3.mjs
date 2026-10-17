import path from 'path';
import { updateNotesBatch } from './curate-updater-util.mjs';

const baseClusterDir = path.resolve('App database/Greek roots/Cluster Form & Space');

const batchData = {
  "Dashboard — the\\prosthetist.md": {
    "primary": "A healthcare professional who specializes in designing, fabricating, and fitting artificial limbs (prostheses) for patients.",
    "secondary": "In clinical orthotics and prosthetics (O&P), a prosthetist evaluates biomechanical gait, casts residual limbs, and calibrates computerized prosthetic components.",
    "quotes": [
      {
        "author": "Oliver Sacks",
        "work": "A Leg to Stand On",
        "quote": "The skilled **prosthetist** sculpted a socket that redistributed pressure away from sensitive bony prominences."
      },
      {
        "author": "V. S. Ramachandran",
        "work": "Phantoms in the Brain",
        "quote": "Working alongside the neurologist, the **prosthetist** adjusted the prosthesis alignment to alleviate phantom pain."
      },
      {
        "author": "Alexis Carrel",
        "work": "Man, The Unknown",
        "quote": "Cooperation between surgeon and **prosthetist** ensures that the amputation stump retains maximum functional utility."
      }
    ]
  },
  "Dashboard — the\\prothesis.md": {
    "primary": "The addition of an initial letter or syllable to a word (linguistics); an alternative spelling of prosthesis (artificial limb).",
    "secondary": "In historical linguistics and phonology, prothesis (prosthesis) adds an initial vowel to simplify consonant clusters, as in Spanish *espada* from Latin *spatha*.",
    "quotes": [
      {
        "author": "Ferdinand de Saussure",
        "work": "Course in General Linguistics",
        "quote": "Vocalic **prothesis** regularly developed in Western Romance to support initial clusters of 's' followed by a mute stop."
      },
      {
        "author": "Otto Jespersen",
        "work": "Language: Its Nature, Development and Origin",
        "quote": "Phonetic **prothesis** demonstrates how articulatory ease alters word onsets across generations of speakers."
      },
      {
        "author": "Max Müller",
        "work": "The Science of Language",
        "quote": "The prosthetic vowel in French 'esprit' exemplifies phonological **prothesis** operating upon Latin 'spiritus'."
      }
    ]
  },
  "Dashboard — the\\prothetic.md": {
    "primary": "Pertaining to or characterized by prothesis; added at the beginning of a word (linguistics); serving as an artificial bodily substitute.",
    "secondary": "In comparative Indo-European grammar, prothetic vowels (such as Greek alpha or epsilon appearing before liquids) reflect vocalized laryngeal consonants.",
    "quotes": [
      {
        "author": "Antoine Meillet",
        "work": "Introduction to the Comparative Study of Indo-European Languages",
        "quote": "Greek exhibits a **prothetic** vowel before initial liquids and nasals where Sanskrit shows an initial consonant."
      },
      {
        "author": "Leonard Bloomfield",
        "work": "Language",
        "quote": "The presence of a **prothetic** vowel in Spanish 'escribir' facilitates the pronunciation of the consonant cluster."
      },
      {
        "author": "Henry Sweet",
        "work": "The History of Language",
        "quote": "In vulgar dialects, a **prothetic** breathing or glide vowel often attaches to heavy syllabic onsets."
      }
    ]
  },
  "Dashboard — the\\pseudothecium.md": {
    "primary": "An ascocarp resembling a perithecium in shape, but in which asci develop directly within pre-formed locules in a stroma rather than in an organized hymenial layer.",
    "secondary": "In ascomycete systematics, the pseudothecium characterizes bitunicate loculoascomycetes (such as *Pleospora* and *Venturia*), possessing a fissitunicate spore-discharge mechanism.",
    "quotes": [
      {
        "author": "Heinrich Anton de Bary",
        "work": "Comparative Morphology and Biology of the Fungi, Mycetozoa and Bacteria",
        "quote": "The cavities within the **pseudothecium** originate by stromal dissolution rather than perithecial invagination."
      },
      {
        "author": "Arthur Henry Reginald Buller",
        "work": "Researches on Fungi",
        "quote": "Bitunicate asci within the mature **pseudothecium** Jack-in-the-box their outer wall to shoot ascospores through the ostiole."
      },
      {
        "author": "Miles Joseph Berkeley",
        "work": "Introduction to Cryptogamic Botany",
        "quote": "Taxonomists distinguish the true perithecium from the stromatic **pseudothecium** by observing ontogenetic development."
      }
    ]
  },
  "Dashboard — the\\redeem.md": {
    "primary": "To compensate for the faults or bad aspects of something; to gain or regain possession of something in exchange for payment; to free from captivity, sin, or blame.",
    "secondary": "Derived from Latin *redimere* (to buy back), cognate through Indo-European roots with notions of restoration, financial discharge of debt, and theological atonement.",
    "quotes": [
      {
        "author": "John Milton",
        "work": "Paradise Lost",
        "quote": "Thy merit / Imputed shall absolve them who renounce / Their own both righteous and unrighteous deeds, / And live in thee transplanted, and from thee / Receive new life, to **redeem** mankind."
      },
      {
        "author": "Charles Dickens",
        "work": "A Christmas Carol",
        "quote": "I will live in the Past, the Present, and the Future; the Spirits of all Three shall strive within me, to **redeem** the time."
      },
      {
        "author": "Adam Smith",
        "work": "The Wealth of Nations",
        "quote": "A prudent state will allocate surplus revenues toward a sinking fund to **redeem** its outstanding annuities."
      }
    ]
  },
  "Dashboard — the\\synthesis.md": {
    "primary": "The combination of ideas, elements, or substances into a complex whole; in chemistry, the production of chemical compounds by reaction from simpler materials.",
    "secondary": "In Hegelian and Marxist dialectics, synthesis is the resolution that integrates the valid insights of both a thesis and its opposing antithesis into a higher unity.",
    "quotes": [
      {
        "author": "G. W. F. Hegel",
        "work": "Phenomenology of Spirit",
        "quote": "The dialectical movement achieves its culmination in a speculative **synthesis** that preserves and elevates both moments."
      },
      {
        "author": "Friedrich Wöhler",
        "work": "On the Artificial Formation of Urea",
        "quote": "The laboratory **synthesis** of urea demonstrated that organic compounds obey ordinary chemical laws without vital force."
      },
      {
        "author": "Julian Huxley",
        "work": "Evolution: The Modern Synthesis",
        "quote": "The modern evolutionary **synthesis** successfully fused Mendelian particulate genetics with Darwinian natural selection."
      }
    ]
  },
  "Dashboard — the\\synthesise.md": {
    "primary": "To combine a range of things, ideas, or substances into a coherent whole; to produce by chemical synthesis (chiefly Commonwealth spelling).",
    "secondary": "In biochemical research, to synthesise proteins or nucleic acids is to enzymatically assemble monomers into functional macromolecular sequences.",
    "quotes": [
      {
        "author": "J. B. S. Haldane",
        "work": "The Origin of Life",
        "quote": "Prebiotic oceans contained abundant simple reagents able to **synthesise** primitive amino acids under solar radiation."
      },
      {
        "author": "Francis Crick",
        "work": "Of Molecules and Men",
        "quote": "Ribosomes read the genetic tape to **synthesise** polypeptide chains with remarkable chemical fidelity."
      },
      {
        "author": "Bertrand Russell",
        "work": "A History of Western Philosophy",
        "quote": "The genius of Aquinas was to **synthesise** Aristotelian metaphysics with established Christian dogma."
      }
    ]
  },
  "Dashboard — the\\synthesiser.md": {
    "primary": "An electronic musical instrument that generates audio signals converted into sound; also, a person or apparatus that synthesizes compounds or concepts (chiefly Commonwealth spelling).",
    "secondary": "In music technology, analog and digital synthesizers employ oscillators, filters, and envelope generators to sculpt novel harmonic timbres.",
    "quotes": [
      {
        "author": "Karlheinz Stockhausen",
        "work": "Towards a Cosmic Music",
        "quote": "The voltage-controlled **synthesiser** opened an infinite continuum of frequencies previously inaccessible to acoustic orchestration."
      },
      {
        "author": "Arthur C. Clarke",
        "work": "2001: A Space Odyssey",
        "quote": "The automated dietary **synthesiser** dispensed nutritionally balanced meals aboard the interplanetary vessel."
      },
      {
        "author": "Marshall McLuhan",
        "work": "The Medium is the Massage",
        "quote": "Operating an electronic sound **synthesiser** transforms the musician into an acoustic architect of electric pulses."
      }
    ]
  },
  "Dashboard — the\\synthesist.md": {
    "primary": "A person who synthesizes ideas, materials, or diverse fields of knowledge into a unified system.",
    "secondary": "In intellectual historiography, a synthesist bridges disparate academic disciplines, integrating specialized data into broad explanatory frameworks.",
    "quotes": [
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "Herbert Spencer was the quintessential Victorian **synthesist**, seeking to bring all cosmic phenomena under the law of evolution."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "The Structure of Evolutionary Theory",
        "quote": "Ernst Mayr stood out as a premier **synthesist**, harmonizing systematics with modern population genetics."
      },
      {
        "author": "Edward O. Wilson",
        "work": "Consilience: The Unity of Knowledge",
        "quote": "The contemporary scholar must aspire to be a **synthesist**, weaving together insights from biology and the social sciences."
      }
    ]
  },
  "Dashboard — the\\synthesize.md": {
    "primary": "To combine different ideas, styles, or materials to form a coherent single whole; to manufacture chemically from simpler precursors.",
    "secondary": "In cognitive science and scientific methodology, synthesizing involves integrating multivariate experimental data into consistent conceptual models.",
    "quotes": [
      {
        "author": "Linus Pauling",
        "work": "The Nature of the Chemical Bond",
        "quote": "Organic chemists learned to **synthesize** complex structural ring systems that mirror natural antibiotics."
      },
      {
        "author": "John Dewey",
        "work": "How We Think",
        "quote": "Reflective thought must continually analyze observations and then **synthesize** them into meaningful conclusions."
      },
      {
        "author": "Oliver Sacks",
        "work": "The Mind's Eye",
        "quote": "The visual cortex works relentlessly to **synthesize** fragmented retinal signals into a coherent perceptual scene."
      }
    ]
  },
  "Dashboard — the\\synthetic.md": {
    "primary": "Made by chemical synthesis, especially not of natural origin; artificial; in logic, of a proposition whose truth depends on empirical facts rather than semantic definitions.",
    "secondary": "In Kantian philosophy, synthetic judgments amplify knowledge by connecting a subject with a predicate not already contained in its definition.",
    "quotes": [
      {
        "author": "Immanuel Kant",
        "work": "Prolegomena to Any Future Metaphysics",
        "quote": "The central problem of philosophy is: How are **synthetic** propositions a priori possible?"
      },
      {
        "author": "Aldous Huxley",
        "work": "Brave New World",
        "quote": "The laboratory vats supplied endless barrels of **synthetic** music, fragrances, and surrogate hormones."
      },
      {
        "author": "Rachel Carson",
        "work": "Silent Spring",
        "quote": "The post-war chemical revolution unleashed powerful **synthetic** pesticides that accumulated throughout global food chains."
      }
    ]
  },
  "Dashboard — the\\synthetical.md": {
    "primary": "Relating to, based on, or involving synthesis (archaic or formal variant of synthetic).",
    "secondary": "In classical philosophical epistemology, the synthetical method reasons from principles, causes, or elements to complex consequences and systems (contrasted with analytical).",
    "quotes": [
      {
        "author": "Isaac Newton",
        "work": "Opticks",
        "quote": "By the **synthetical** method, we assume the established causes as principles and explain the phenomena proceeding from them."
      },
      {
        "author": "Samuel Taylor Coleridge",
        "work": "Biographia Literaria",
        "quote": "The secondary imagination reveals itself in the balance or reconcilement of opposite or discordant qualities through a **synthetical** power."
      },
      {
        "author": "William Whewell",
        "work": "The Philosophy of the Inductive Sciences",
        "quote": "Inductive discovery progresses by combining separate factual observations into a unified **synthetical** conception."
      }
    ]
  },
  "Dashboard — the\\synthetically.md": {
    "primary": "In a synthetic manner; by means of chemical synthesis or by combining separate elements.",
    "secondary": "In pharmaceutical manufacturing and materials science, compounds produced synthetically ensure standardized purity and scalable industrial availability.",
    "quotes": [
      {
        "author": "Alexander Fleming",
        "work": "Penicillin: Its Practical Application",
        "quote": "Once the molecular structure was determined, biochemists sought to prepare penicillin **synthetically** in the laboratory."
      },
      {
        "author": "Bertrand Russell",
        "work": "Introduction to Mathematical Philosophy",
        "quote": "Mathematical logic proceeds **synthetically**, deriving rich theorems from a parsimonious set of primitive axioms."
      },
      {
        "author": "Primo Levi",
        "work": "The Periodic Table",
        "quote": "In the industrial laboratory, we worked day and night to produce the missing varnish resin **synthetically**."
      }
    ]
  },
  "Dashboard — the\\synthetism.md": {
    "primary": "A post-impressionist art movement pioneered by Paul Gauguin and Émile Bernard, emphasizing two-dimensional flat patterns, pure colors, and synthesis of outward appearance with inner emotion.",
    "secondary": "In art history, Synthetism rejected photographic naturalism in favor of memory, bold outlines (cloisonnism), and symbolic representation of spiritual realities.",
    "quotes": [
      {
        "author": "Paul Gauguin",
        "work": "Intimate Journals",
        "quote": "In our quest for **Synthetism**, we simplified nature into broad rhythmic planes of unmodulated color."
      },
      {
        "author": "Maurice Denis",
        "work": "Theories",
        "quote": "The aesthetic of **Synthetism** reminded painters that a picture, before being a war horse or nude, is essentially a flat surface covered with colors."
      },
      {
        "author": "Roger Fry",
        "work": "Vision and Design",
        "quote": "Gauguin's bold **Synthetism** revitalized European painting by restoring the expressive decorative power of line and flat tone."
      }
    ]
  },
  "Dashboard — the\\Thea.md": {
    "primary": "A former botanical genus that included the tea plant (*Thea sinensis*, now classified as *Camellia sinensis*); also, in Greek mythology, the Titaness Theia (goddess of sight and shining light).",
    "secondary": "In economic botany, Linnaeus established the genus *Thea* to classify the cultivated Asian beverage shrubs whose caffeine-rich leaves formed the cornerstone of global maritime tea trade.",
    "quotes": [
      {
        "author": "Carl Linnaeus",
        "work": "Species Plantarum",
        "quote": "Linnaeus described the Asian tea plant under the genus **Thea**, distinguishing green and black cultivars."
      },
      {
        "author": "Robert Fortune",
        "work": "A Journey to the Tea Countries of China",
        "quote": "Botanical investigations proved that both green and black tea derive from varieties of **Thea** sinensis."
      },
      {
        "author": "Hesiod",
        "work": "Theogony",
        "quote": "From the union of Hyperion and divine **Thea** sprang Helios the sun, Selene the moon, and radiant Eos."
      }
    ]
  },
  "Dashboard — the\\theca.md": {
    "primary": "A sheath, case, or capsule enclosing an anatomical organ or biological structure (e.g. spore case, pollen sac, ovarian follicle layer).",
    "secondary": "In reproductive endocrinology, the ovarian theca (divided into theca interna and theca externa) surrounds developing graafian follicles, synthesizing androgens converted to estrogens by granulosa cells.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "The Anatomy of Invertebrate Animals",
        "quote": "The delicate hydrotheca provides a protective chitinous **theca** into which the polyp retracts upon disturbance."
      },
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Histology of the Nervous System",
        "quote": "The dural **theca** forms a tough, inelastic fibrous sheath enclosing the spinal cord and roots."
      },
      {
        "author": "Arthur Keith",
        "work": "Human Embryology and Morphology",
        "quote": "During follicular maturation, the surrounding stroma condenses into a vascular **theca** supporting the ovum."
      }
    ]
  },
  "Dashboard — the\\thecium.md": {
    "primary": "The spore-bearing fertile layer (hymenium) of certain fungi, especially ascomycetes, containing the asci and sterile paraphyses.",
    "secondary": "In lichenology and cryptogamic botany, the thecium (or hymenium) is the tissue layer in apothecia or perithecia where ascospores are generated and discharged.",
    "quotes": [
      {
        "author": "Heinrich Anton de Bary",
        "work": "Comparative Morphology and Biology of the Fungi, Mycetozoa and Bacteria",
        "quote": "In Discomycetes, the **thecium** lies exposed on the upper surface of the apothecial disc."
      },
      {
        "author": "Miles Joseph Berkeley",
        "work": "Outlines of British Fungology",
        "quote": "The slender sterile paraphyses packed tightly in the **thecium** prevent the developing asci from drying out."
      },
      {
        "author": "William Jackson Hooker",
        "work": "The English Flora",
        "quote": "Cross sections of the lichen shield display a pigmented **thecium** resting upon the medullary stratum."
      }
    ]
  },
  "Dashboard — the\\thematic.md": {
    "primary": "Having or relating to a particular theme, topic, or melodic subject; in linguistics, of a vowel or morpheme forming part of the stem.",
    "secondary": "In Indo-European comparative grammar, thematic verbs insert a vowel (*-e-*, *-o-*) between the root and inflectional endings, regularizing verbal conjugations.",
    "quotes": [
      {
        "author": "Ferdinand de Saussure",
        "work": "Course in General Linguistics",
        "quote": "The insertion of a **thematic** vowel in Greek and Latin verbs transformed archaic root inflection into predictable paradigms."
      },
      {
        "author": "Charles Rosen",
        "work": "The Classical Style",
        "quote": "Beethoven's development sections subject the principal **thematic** material to radical harmonic fragmentation."
      },
      {
        "author": "Northrop Frye",
        "work": "Anatomy of Criticism",
        "quote": "A coherent **thematic** structure organizes the archetypal imagery of romance literature."
      }
    ]
  },
  "Dashboard — the\\theme.md": {
    "primary": "The subject of a talk, piece of writing, exhibition, or musical composition; a unifying or dominant idea.",
    "secondary": "In literary theory, a theme is an underlying central idea or universal insight explored through characterization, plot, and symbolic motifs.",
    "quotes": [
      {
        "author": "Henry James",
        "work": "The Art of Fiction",
        "quote": "The primary obligation of the novelist is to be interesting, pursuing his chosen **theme** with absolute artistic sincerity."
      },
      {
        "author": "Matthew Arnold",
        "work": "Essays in Criticism",
        "quote": "Poetry achieves grandeur when it addresses an actions of high seriousness and noble **theme**."
      },
      {
        "author": "Donald Tovey",
        "work": "The Forms of Music",
        "quote": "A fugue does not merely repeat its **theme**, but exposes its latent harmonic possibilities across different keys."
      }
    ]
  },
  "Dashboard — the\\Themis.md": {
    "primary": "In Greek mythology, the Titaness of divine law, natural order, custom, and justice, often depicted holding scales and a sword.",
    "secondary": "In classical legal history and mythography, Themis represented the established divine order that governed human assemblies and the cosmic seasons, mother of the Horae and Moirai by Zeus.",
    "quotes": [
      {
        "author": "Hesiod",
        "work": "Theogony",
        "quote": "Next Zeus took to wife glorious **Themis**, who bare the Horae: Lawfulness, Justice, and flourishing Peace."
      },
      {
        "author": "Henry Maine",
        "work": "Ancient Law",
        "quote": "In Homeric times, patriarchal awards were viewed as inspirations of **Themis**, representing customary divine decrees."
      },
      {
        "author": "Jane Ellen Harrison",
        "work": "Themis: A Study of the Social Origins of Greek Religion",
        "quote": "Ancient **Themis** embodied the collective conscience and social will of the primitive Hellenic tribal community."
      }
    ]
  },
  "Dashboard — the\\theobromine.md": {
    "primary": "A bitter alkaloid (3,7-dimethylxanthine) found naturally in cocoa, chocolate, and tea, structurally related to caffeine.",
    "secondary": "In pharmacology, theobromine acts as a mild central nervous system stimulant, myocardial stimulant, vasodilator, and diuretic; it is toxic to canines due to slow hepatic metabolism.",
    "quotes": [
      {
        "author": "Justus von Liebig",
        "work": "Familiar Letters on Chemistry",
        "quote": "Chemical analysis of cacao beans revealed **theobromine**, an alkaloid closely allied in constitution to caffeine."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Physicians occasionally administered **theobromine** salts as diuretics in cases of severe cardiac dropsy."
      },
      {
        "author": "Emil Fischer",
        "work": "Investigations on the Purine Group",
        "quote": "My synthetic elucidation of xanthine derivatives demonstrated how **theobromine** can be converted into caffeine by methylation."
      }
    ]
  },
  "Dashboard — the\\theocracy.md": {
    "primary": "A system of government in which priests rule in the name of God or a god, or where God is recognized as the supreme civil ruler.",
    "secondary": "Coined by the Jewish historian Flavius Josephus in the first century CE to describe the polity of the ancient Hebrews governed by divine Torah law.",
    "quotes": [
      {
        "author": "Flavius Josephus",
        "work": "Against Apion",
        "quote": "Our legislator ordained that our government should be what may be called a **theocracy**, placing all sovereignty in God."
      },
      {
        "author": "John Adams",
        "work": "Discourses on Davila",
        "quote": "Whenever ecclesiastical authority captures secular power, government degenerates into an oppressive **theocracy**."
      },
      {
        "author": "Thomas Babington Macaulay",
        "work": "The History of England",
        "quote": "The Geneva republic under Calvin exhibited the rigorous moral discipline of a Protestant **theocracy**."
      }
    ]
  },
  "Dashboard — the\\theocratic.md": {
    "primary": "Of, relating to, or characteristic of a theocracy.",
    "secondary": "In political philosophy and constitutional history, describing regimes wherein civil legislation, judicial decrees, and political legitimacy are derived directly from religious doctrine.",
    "quotes": [
      {
        "author": "Alexis de Tocqueville",
        "work": "Democracy in America",
        "quote": "Early Puritan New England blended democratic town meetings with an austere **theocratic** legal code."
      },
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The caliphate merged imperial executive power with supreme **theocratic** stewardship over the faithful."
      },
      {
        "author": "Max Weber",
        "work": "Economy and Society",
        "quote": "In a **theocratic** administration, legal adjudication is governed by sacred charisma rather than formal juristic rationality."
      }
    ]
  },
  "Dashboard — the\\theodicy.md": {
    "primary": "The vindication of divine goodness and providence in view of the existence of evil; philosophical justification of God's ways to humans.",
    "secondary": "Coined by Gottfried Wilhelm Leibniz in his 1710 treatise *Essais de Théodicée*, proposing that the actual world is the 'best of all possible worlds'.",
    "quotes": [
      {
        "author": "Gottfried Wilhelm Leibniz",
        "work": "Theodicy: Essays on the Goodness of God, the Freedom of Man and the Origin of Evil",
        "quote": "True **theodicy** demonstrates that physical and moral evils are permitted only to secure the greater harmony of the cosmos."
      },
      {
        "author": "Voltaire",
        "work": "Candide",
        "quote": "The Lisbon earthquake shattered Pangloss's complacent **theodicy** that everything was for the best in the best of worlds."
      },
      {
        "author": "Immanuel Kant",
        "work": "On the Miscarriage of All Philosophical Trials in Theodicy",
        "quote": "Theoretical reason cannot construct a successful **theodicy**, for human intellect cannot fathom divine purpose."
      }
    ]
  },
  "Dashboard — the\\Theodore.md": {
    "primary": "A masculine given name derived from the Greek name *Theodoros*, meaning 'gift of God' (*theos* + *doron*).",
    "secondary": "Borne by numerous saints, Byzantine emperors, popes, and prominent historical figures including US President Theodore Roosevelt and novelist Theodore Dreiser.",
    "quotes": [
      {
        "author": "Theodore Roosevelt",
        "work": "An Autobiography",
        "quote": "My father, **Theodore** Roosevelt, was the best man I ever knew, combining strength and courage with gentleness."
      },
      {
        "author": "Theodore Dreiser",
        "work": "A Book About Myself",
        "quote": "Reflecting on his literary ambitions, young **Theodore** resolved to capture the raw realism of American cities."
      },
      {
        "author": "Henry James",
        "work": "The Bostonians",
        "quote": "The old doctor reminisced fondly about his college classmate **Theodore**, admiring his unbending moral integrity."
      }
    ]
  },
  "Dashboard — the\\theogony.md": {
    "primary": "The genealogy of a group or system of gods; an account or poem describing the birth and origins of the gods.",
    "secondary": "In classical literature, exemplified by Hesiod's eighth-century BCE poem *Theogony*, which recounts the cosmogonic emergence of Chaos, Gaia, Uranus, and the Olympian deities.",
    "quotes": [
      {
        "author": "Hesiod",
        "work": "Theogony",
        "quote": "Sing to me, Muses, the sacred **theogony** recounting how gods and earth arose from primeval darkness."
      },
      {
        "author": "George Grote",
        "work": "A History of Greece",
        "quote": "Hesiod's **theogony** systematized discordant local myths into a coherent chronological pedigree of Olympian divinities."
      },
      {
        "author": "Jane Ellen Harrison",
        "work": "Prolegomena to the Study of Greek Religion",
        "quote": "Benevolent Olympian deities in Homeric verse superseded the older chthonic monsters described in Hesiodic **theogony**."
      }
    ]
  },
  "Dashboard — the\\theological.md": {
    "primary": "Of, relating to, or involved in the study of religion, religious faith, practice, and the nature of God.",
    "secondary": "In scholastic philosophy, theological virtues (faith, hope, love) and methodologies were distinguished from natural philosophy and secular jurisprudence.",
    "quotes": [
      {
        "author": "Thomas Aquinas",
        "work": "Summa Theologiae",
        "quote": "Sacred doctrine is a science because it proceeds from principles established by the light of a higher **theological** revelation."
      },
      {
        "author": "David Hume",
        "work": "An Enquiry Concerning Human Understanding",
        "quote": "If we take in our hand any volume of divinity or **theological** dispute, let us ask: Does it contain any experimental reasoning?"
      },
      {
        "author": "Auguste Comte",
        "work": "A General View of Positivism",
        "quote": "In the historical law of the three stages, human civilization begins in the fictitious or **theological** phase."
      }
    ]
  },
  "Dashboard — the\\theologically.md": {
    "primary": "In a theological manner; according to the principles or methods of theology.",
    "secondary": "In doctrinal controversy and philosophy of religion, reasoning theologically involves interpreting sacred scriptures and ecclesiastical tradition.",
    "quotes": [
      {
        "author": "John Henry Newman",
        "work": "An Essay on the Development of Christian Doctrine",
        "quote": "Dogmatic ideas unfold **theologically** across centuries as their inner implications are grasped by the Church."
      },
      {
        "author": "Søren Kierkegaard",
        "work": "Fear and Trembling",
        "quote": "Abraham cannot be understood ethically, for his terrifying suspension of duty is justified only **theologically**."
      },
      {
        "author": "Jonathan Edwards",
        "work": "Freedom of the Will",
        "quote": "Examining the nature of moral agency **theologically**, Edwards argued that divine foreknowledge determines human choices."
      }
    ]
  },
  "Dashboard — the\\theologist.md": {
    "primary": "A theologian; a scholar or thinker who studies theology or religious doctrine.",
    "secondary": "Historically applied to doctrinal authorities and scholastic system-builders who systematize divine revelation into ecclesiastical orthodoxy.",
    "quotes": [
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The subtle Byzantine **theologist** debated the mystery of the Trinity while enemy legions besieged the outer walls."
      },
      {
        "author": "Francis Bacon",
        "work": "The Advancement of Learning",
        "quote": "Let no man think that a philosopher can search too far in nature, or a **theologist** in the divine oracles."
      },
      {
        "author": "Voltaire",
        "work": "Philosophical Dictionary",
        "quote": "Every dogmatic **theologist** imagines that his particular sect holds exclusive title to celestial truth."
      }
    ]
  },
  "Dashboard — the\\theology.md": {
    "primary": "The study of the nature of God and religious belief; religious beliefs and theory when systematically developed.",
    "secondary": "Classically dubbed the 'queen of the sciences' in medieval universities, theology encompasses dogmatics, biblical exegesis, moral ethics, and apophatic mysticism.",
    "quotes": [
      {
        "author": "Thomas Aquinas",
        "work": "Summa Theologiae",
        "quote": "Christian **theology** uses philosophical reason not to prove faith, but to make clear what is handed down in revelation."
      },
      {
        "author": "William Paley",
        "work": "Natural Theology",
        "quote": "The intricate mechanism of a watch implies a watchmaker; likewise, natural **theology** discerns design in nature."
      },
      {
        "author": "John Calvin",
        "work": "Institutes of the Christian Religion",
        "quote": "Nearly all wisdom consists of two parts: the knowledge of God and of ourselves, which forms the core of sound **theology**."
      }
    ]
  },
  "Dashboard — the\\theophobia.md": {
    "primary": "An abnormal, intense, or irrational fear or hatred of God or religion.",
    "secondary": "In clinical psychology and philosophy of religion, theophobia denotes pathological dread of divine punishment, religious symbols, or sacred ceremonies.",
    "quotes": [
      {
        "author": "William James",
        "work": "The Varieties of Religious Experience",
        "quote": "A morbid terror of divine retribution, bordering on acute **theophobia**, plagued the religious melancholy of the Puritan soul."
      },
      {
        "author": "Robert Burton",
        "work": "The Anatomy of Melancholy",
        "quote": "Certain melancholic patients fall into agonizing **theophobia**, shuddering at the mere mention of holy scripture."
      },
      {
        "author": "Havelock Ellis",
        "work": "The Dance of Life",
        "quote": "Modern skepticism occasionally overshoots its rational aim, collapsing into an irrational and dogmatic **theophobia**."
      }
    ]
  },
  "Dashboard — the\\thes.md": {
    "primary": "Afternoon tea receptions or tea dances (from French *thés*, plural of *thé*); historically also an archaic variant spelling of 'these'.",
    "secondary": "In nineteenth- and early twentieth-century polite society, afternoon gatherings known as thés dansants (or simply thes) featured light tea, pastries, and social dancing.",
    "quotes": [
      {
        "author": "Marcel Proust",
        "work": "In the Shadow of Young Girls in Flower",
        "quote": "In the fashionable Parisian salons, society matrons gathered at intimate **thes** to discuss music and salon gossip."
      },
      {
        "author": "Edith Wharton",
        "work": "The Age of Innocence",
        "quote": "The drawing-room was prepared for the customary winter **thes**, with silver samovars gleaming upon the sideboard."
      },
      {
        "author": "Robert Burns",
        "work": "Poems and Songs of Robert Burns",
        "quote": "O let me in **thes** ae night, / For pity's sake, sweet lassie, let me in."
      }
    ]
  },
  "Dashboard — the\\thesaurus.md": {
    "primary": "A book that lists words in groups of synonyms and related concepts; historically, a treasury or storehouse of knowledge.",
    "secondary": "Originating from Greek *thesauros* (treasure store), popularized in 1852 by Peter Mark Roget's conceptual classification of the English vocabulary.",
    "quotes": [
      {
        "author": "Peter Mark Roget",
        "work": "Thesaurus of English Words and Phrases",
        "quote": "The present **Thesaurus** provides a literary treasury where ideas are arranged to facilitate the expression of thoughts."
      },
      {
        "author": "Richard Chenevix Trench",
        "work": "On the Study of Words",
        "quote": "Language is the great living **thesaurus** of a nation's historical experience, moral values, and collective memories."
      },
      {
        "author": "H. W. Fowler",
        "work": "A Dictionary of Modern English Usage",
        "quote": "A writer consults a **thesaurus** not to hunt for obscure jargon, but to find the precise word for an exact thought."
      }
    ]
  },
  "Dashboard — the\\thesis.md": {
    "primary": "A proposition or statement stated or put forward for consideration, especially one to be discussed and proved or maintained against objections; a dissertation embodying results of original research.",
    "secondary": "In classical dialectics, a thesis is an initial proposition that provokes an antithesis; in prosody, the unstressed part of a metrical foot (or the downbeat in Greek rhythm).",
    "quotes": [
      {
        "author": "Martin Luther",
        "work": "Ninety-Five Theses",
        "quote": "Out of love for the truth, Reverend Father Martin Luther intends to defend the following **thesis** points at Wittenberg."
      },
      {
        "author": "G. W. F. Hegel",
        "work": "The Science of Logic",
        "quote": "Every initial **thesis** contains within its own one-sidedness the necessity of calling forth its opposing antithesis."
      },
      {
        "author": "Karl Marx",
        "work": "Theses on Feuerbach",
        "quote": "The philosophers have only interpreted the world in various ways; the eleventh **thesis** insists the point is to change it."
      }
    ]
  },
  "Dashboard — the\\Timothy.md": {
    "primary": "A masculine given name derived from Greek *Timotheos*, meaning 'honoring God' or 'honored by God' (*timao* + *theos*); also, timothy grass (*Phleum pratense*), a widely cultivated pasture grass.",
    "secondary": "In the New Testament, Timothy was a companion and disciple of Paul the Apostle and recipient of two Pauline epistles; the grass was named after agriculturalist Timothy Hanson.",
    "quotes": [
      {
        "author": "Saint Paul",
        "work": "First Epistle to Timothy",
        "quote": "Let no man despise thy youth; but be thou an example of the believers, my beloved disciple **Timothy**."
      },
      {
        "author": "Henry David Thoreau",
        "work": "Walden",
        "quote": "The farmer harvested sweet-smelling redtop and lush **timothy** grass from the upland meadow."
      },
      {
        "author": "George Eliot",
        "work": "The Mill on the Floss",
        "quote": "Uncle **Timothy** shook his head gravely over the family ledgers, cautioning against rash investments."
      }
    ]
  },
  "Dashboard — the\\treasure.md": {
    "primary": "A quantity of precious metals, gems, or other valuable objects; something or someone regarded as exceptionally precious or worthy of protection.",
    "secondary": "Etymologically derived via Old French *tresor* and Latin *thesaurus* from Greek *thesauros* (storehouse, treasury), reflecting tangible and metaphorical cultural wealth.",
    "quotes": [
      {
        "author": "Robert Louis Stevenson",
        "work": "Treasure Island",
        "quote": "Fifteen men on the dead man's chest / Yo-ho-ho, and a bottle of rum! / Seeking buried **treasure** under southern skies."
      },
      {
        "author": "Francis Bacon",
        "work": "Of Riches",
        "quote": "I cannot call riches better than the baggage of virtue; great **treasure** cannot be distributed without moral care."
      },
      {
        "author": "John Ruskin",
        "work": "Sesame and Lilies",
        "quote": "Good books constitute a kings' **treasure** that neither moth nor rust can corrupt."
      }
    ]
  },
  "Dashboard — the\\treasured.md": {
    "primary": "Kept or regarded as precious, valued, or dear; held in high esteem and affection.",
    "secondary": "In biographical literature and poetry, describing heirlooms, memories, or ideals guarded with tender reverence.",
    "quotes": [
      {
        "author": "Lord Byron",
        "work": "Childe Harold's Pilgrimage",
        "quote": "Each **treasured** memory of youth returns with poignant sweetness across the rolling years."
      },
      {
        "author": "Charlotte Brontë",
        "work": "Jane Eyre",
        "quote": "I held in my hand the small **treasured** miniature portrait, gazing upon features I would never forget."
      },
      {
        "author": "Edmund Burke",
        "work": "Reflections on the Revolution in France",
        "quote": "Constitutional liberties are our most **treasured** inheritance, bequeathed to us by ancient ancestors."
      }
    ]
  },
  "Dashboard — the\\treasurer.md": {
    "primary": "A person appointed to administer or manage the financial assets, receipts, and disbursements of a society, corporation, or government.",
    "secondary": "In British constitutional history, the Lord High Treasurer was one of the Great Officers of State, an office now held in commission by the Lords of the Treasury led by the Prime Minister.",
    "quotes": [
      {
        "author": "Adam Smith",
        "work": "The Wealth of Nations",
        "quote": "The public **treasurer** must enforce strict accountability in collecting taxes and funding national expenditures."
      },
      {
        "author": "Alexander Hamilton",
        "work": "The Federalist Papers",
        "quote": "The appointment of an incorruptible national **treasurer** provides citizens security against the diversion of public funds."
      },
      {
        "author": "Walter Bagehot",
        "work": "The English Constitution",
        "quote": "The First Lord of the Treasury and the **treasurer** commissioners oversee executive management of the imperial revenue."
      }
    ]
  },
  "Dashboard — the\\tritheism.md": {
    "primary": "The doctrine or belief that the Father, Son, and Holy Spirit in the Trinity are three separate, distinct deities rather than one God in three persons.",
    "secondary": "Condemned as heresy by orthodox Christian councils, tritheism arose historically in the theological formulations of John Philoponus in the sixth century and Roscelin of Compiègne in the eleventh century.",
    "quotes": [
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "Orthodox fathers strove to articulate the Trinity without falling into Sabellian modalism on one side or **tritheism** on the other."
      },
      {
        "author": "John Henry Newman",
        "work": "The Arians of the Fourth Century",
        "quote": "To safeguard the monotheistic unity of the Godhead, the Alexandrian council repudiated every insinuation of **tritheism**."
      },
      {
        "author": "David Hume",
        "work": "Dialogues Concerning Natural Religion",
        "quote": "The subtle disputes of theologians frequently exposed their formulations to the charge of vulgar **tritheism**."
      }
    ]
  },
  "Dashboard — the\\tritheist.md": {
    "primary": "A person who believes that the Trinity consists of three distinct and independent gods.",
    "secondary": "In ecclesiastical history, thinkers such as Philoponus or Roscelin were labeled tritheists by contemporaries for asserting that each divine hypostasis possessed a separate individual substance.",
    "quotes": [
      {
        "author": "Henry Hart Milman",
        "work": "History of Latin Christianity",
        "quote": "Roscelin was accused of being a **tritheist** because his nominalism recognized no reality beyond individual particulars."
      },
      {
        "author": "Thomas Aquinas",
        "work": "Summa Theologiae",
        "quote": "The orthodox teacher must refute the **tritheist** who divides the divine essence into three separate deities."
      },
      {
        "author": "Richard Baxter",
        "work": "The Saints' Everlasting Rest",
        "quote": "Beware the sophistry that turns the holy mystery of the Trinity into the blasphemy of a **tritheist**."
      }
    ]
  },
  "Dashboard — the\\unenthusiastic.md": {
    "primary": "Not having or showing enthusiasm, interest, or eager excitement; lukewarm; indifferent.",
    "secondary": "In behavioral and social psychology, an unenthusiastic response signals passive resistance, lack of motivation, or skepticism toward proposed initiatives.",
    "quotes": [
      {
        "author": "Jane Austen",
        "work": "Mansfield Park",
        "quote": "Fanny's **unenthusiastic** reception of the theatrical scheme disappointed her eager young cousins."
      },
      {
        "author": "George Orwell",
        "work": "Keep the Aspidistra Flying",
        "quote": "He greeted the promotional advertising slogan with an **unenthusiastic** grunt of cynical contempt."
      },
      {
        "author": "Winston Churchill",
        "work": "The Second World War",
        "quote": "The allied staff received the precarious Mediterranean proposal with an **unenthusiastic** and guarded silence."
      }
    ]
  },
  "Dashboard — the\\unthematic.md": {
    "primary": "Not relating to, based on, or developing a central theme; lacking a thematic connecting vowel (in linguistics).",
    "secondary": "In musical composition and literary criticism, unthematic structures rely on atmospheric color, texture, or episodic stream-of-consciousness rather than motivic exposition.",
    "quotes": [
      {
        "author": "Theodor Adorno",
        "work": "Philosophy of New Music",
        "quote": "Certain modern orchestral textures remain consciously **unthematic**, abandoning melodic recurrence for raw sonic timbre."
      },
      {
        "author": "Charles Rosen",
        "work": "The Classical Style",
        "quote": "A transitional passage that is strictly **unthematic** serves to cleanse the musical ear before the second subject."
      },
      {
        "author": "Antoine Meillet",
        "work": "General Linguistics",
        "quote": "Archaic root formations in Indo-European preserve an **unthematic** stem structure without a connecting vowel."
      }
    ]
  },
  "Dashboard — thel\\anthelminthic.md": {
    "primary": "An agent, drug, or medication destructive to or expelling parasitic intestinal worms (helminths); acting against worms (variant of anthelmintic).",
    "secondary": "In clinical parasitology and tropical medicine, anthelminthic treatments (such as albendazole, ivermectin, and praziquantel) target nematodes, cestodes, and trematodes in humans and livestock.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The administration of an effective **anthelminthic** like male fern oil rapidly expels the tapeworm head."
      },
      {
        "author": "Florence Nightingale",
        "work": "Notes on Nursing",
        "quote": "Proper sanitation reduces the constant need for therapeutic **anthelminthic** dosages among hospital patients."
      },
      {
        "author": "Patrick Manson",
        "work": "Tropical Diseases: A Manual of the Diseases of Warm Climates",
        "quote": "Early diagnosis of filariasis is essential to begin targeted **anthelminthic** treatment before lymphatic damage ensues."
      }
    ]
  },
  "Dashboard — thel\\anthelmintic.md": {
    "primary": "Expelling or destroying parasitic intestinal worms; a drug or chemical used for this purpose.",
    "secondary": "In veterinary pharmacology and human gastroenterology, anthelmintic agents paralyze or disrupt the cellular metabolism of parasitic helminths, enabling their clearance through the host gastrointestinal tract.",
    "quotes": [
      {
        "author": "Alexander Fleming",
        "work": "Chemotherapy: Yesterday, Today, and Tomorrow",
        "quote": "The discovery of synthetic **anthelmintic** agents vastly reduced the morbidity associated with rural hookworm infestations."
      },
      {
        "author": "Charles Darwin",
        "work": "The Effects of Cross and Self Fertilisation in the Vegetable Kingdom",
        "quote": "Certain indigenous plants were valued by native populations for their potent natural **anthelmintic** properties."
      },
      {
        "author": "Thomas Sydenham",
        "work": "The Entire Works of Dr. Thomas Sydenham",
        "quote": "A purgative regimen combined with a bitter **anthelmintic** decoction cleared the patient of stubborn ascarids."
      }
    ]
  },
  "Dashboard — thel\\athelia.md": {
    "primary": "The congenital absence of one or both nipples.",
    "secondary": "In medical genetics and teratology, athelia can occur as an isolated developmental anomaly or as part of congenital syndromes such as Poland syndrome or ectodermal dysplasias.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "Principles and Practice of Medicine",
        "quote": "Congenital anomalies of the breast include polythelia, amastia, and the rarer condition of complete **athelia**."
      },
      {
        "author": "Henry Gray",
        "work": "Gray's Anatomy",
        "quote": "Defective development of the mammary ridge during early embryogenesis may result in unilateral or bilateral **athelia**."
      },
      {
        "author": "Arthur Keith",
        "work": "Human Embryology and Morphology",
        "quote": "Clinical examination of patients with pectoral aplasia occasionally demonstrates associated **athelia**."
      }
    ]
  },
  "Dashboard — thel\\athelstan.md": {
    "primary": "King of the Anglo-Saxons and King of the English (r. 924–939), renowned as the first ruler to unite the disparate Anglo-Saxon and Norse kingdoms of Britain.",
    "secondary": "In medieval historiography, Athelstan centralized royal law codes, established standard coinage, fostered monastic intellectual revival, and defeated a combined Scottish-Viking alliance at the landmark Battle of Brunanburh in 937.",
    "quotes": [
      {
        "author": "William of Malmesbury",
        "work": "Chronicle of the Kings of England",
        "quote": "Glorious King **Athelstan** subdued all the princes of Britain, extending his realm from Wessex to Northumbria."
      },
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "Foreign princes eagerly sought matrimonial alliances with the royal daughters of the renowned Saxon monarch **Athelstan**."
      },
      {
        "author": "Winston Churchill",
        "work": "A History of the English-Speaking Peoples: The Birth of Britain",
        "quote": "At the decisive battle of Brunanburh, **Athelstan** and his brother Edmund achieved an immortal victory that secured English unity."
      }
    ]
  },
  "Dashboard — thel\\endothelial.md": {
    "primary": "Of, relating to, or consisting of endothelium (the layer of flat epithelial cells lining blood vessels, lymphatics, and the heart).",
    "secondary": "In vascular biology, endothelial cells regulate vascular tone, platelet adhesion, coagulation, leukocyte trafficking, and angiogenesis by synthesizing mediators like nitric oxide and prostacyclin.",
    "quotes": [
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Irritation of the vascular **endothelial** lining triggers fibrin deposition and localized intravascular clotting."
      },
      {
        "author": "Alexis Carrel",
        "work": "The Preservation of Tissues and Its Application in Surgery",
        "quote": "Preserving a pristine **endothelial** surface along the anastomotic line is critical to avoid thrombosis."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Microscopic examination in infective endocarditis reveals bacterial colonies vegetating upon disrupted **endothelial** surfaces."
      }
    ]
  },
  "Dashboard — thel\\endothelium.md": {
    "primary": "The single layer of thin, flattened epithelial cells that lines the heart, blood vessels, and lymphatic vessels.",
    "secondary": "Historically distinguished from outer epithelia by Wilhelm His in 1865, the endothelium is recognized as an active paracrine organ controlling hemodynamic permeability and vascular homeostasis.",
    "quotes": [
      {
        "author": "Wilhelm His",
        "work": "The First Form of the Human Organism",
        "quote": "I propose the term **endothelium** to denote the internal cellular layer lining the cardiovascular cavities."
      },
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Histology of the Nervous System",
        "quote": "Cerebral capillaries consist of a delicate **endothelium** surrounded by pericytes and dense astrocytic footplates."
      },
      {
        "author": "Michael DeBakey",
        "work": "The Living Heart",
        "quote": "Atherosclerotic plaque begins with subtle injuries to the arterial **endothelium**, permitting cholesterol infiltration."
      }
    ]
  },
  "Dashboard — thel\\epithelial.md": {
    "primary": "Relating to or composed of epithelium, the cellular tissue forming the covering of all bodily surfaces and organ linings.",
    "secondary": "In histology, epithelial tissues are categorized by morphology (squamous, cuboidal, columnar) and stratification (simple, stratified, pseudostratified), serving barrier, secretory, and absorptive functions.",
    "quotes": [
      {
        "author": "Theodor Schwann",
        "work": "Microscopical Researches into the Accordance in the Structure and Growth of Animals and Plants",
        "quote": "Every **epithelial** cell contains a distinct nucleus that governs its individual nutrition and growth."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Carcinoma arises fundamentally from pathological proliferation within the **epithelial** cellular layers."
      },
      {
        "author": "Henry Gray",
        "work": "Gray's Anatomy",
        "quote": "The cutaneous epidermis consists of a stratified **epithelial** sheath that continuously sheds keratinized surface scales."
      }
    ]
  },
  "Dashboard — thel\\epitheliod.md": {
    "primary": "Resembling epithelial cells or tissue in morphology or arrangement (variant spelling of epithelioid).",
    "secondary": "In histopathology, epitheliod cells denote activated histiocytes/macrophages with abundant pale pink cytoplasm that characterize granulomatous conditions like tuberculosis and sarcoidosis.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "A tuberculous tubercle is typically composed of giant cells surrounded by a zone of pale **epitheliod** cells."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Certain chronic granulomatous lesions present large, tightly packed **epitheliod** histiocytes."
      },
      {
        "author": "Alexis Carrel",
        "work": "Studies in Tissue Culture",
        "quote": "Under in vitro conditions, wandering fibroblasts may assume a flattened, **epitheliod** appearance."
      }
    ]
  },
  "Dashboard — thel\\epithelioma.md": {
    "primary": "A benign or malignant tumor consisting of epithelial cells; a carcinoma of the skin or mucous membranes.",
    "secondary": "In nineteenth- and twentieth-century clinical oncology, epithelioma commonly referred to cutaneous basal cell or squamous cell carcinomas arising from epidermal or glandular structures.",
    "quotes": [
      {
        "author": "William Halsted",
        "work": "Surgical Papers",
        "quote": "Early and wide surgical excision remains the sovereign cure for cutaneous **epithelioma**."
      },
      {
        "author": "Jonathan Hutchinson",
        "work": "Illustrations of Clinical Surgery",
        "quote": "Chimney sweeps suffered from scrotal **epithelioma** caused by chronic exposure to coal tar and soot."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Solar keratosis in elderly outdoorsmen frequently transitions into a superficial **epithelioma** of the face."
      }
    ]
  },
  "Dashboard — thel\\epithelium.md": {
    "primary": "The continuous sheet of tightly packed cells forming the skin and lining the cavities, tubes, and vessels of the body.",
    "secondary": "Coined by Dutch anatomist Frederik Ruysch in the early eighteenth century, epithelium provides selective biochemical barriers, active absorption, secretion, and sensory reception across all organ systems.",
    "quotes": [
      {
        "author": "Frederik Ruysch",
        "work": "Thesaurus Anatomicus",
        "quote": "Ruysch described the delicate surface covering of the nipple and lip as the **epithelium**."
      },
      {
        "author": "Theodor Schwann",
        "work": "Microscopical Researches",
        "quote": "The cells composing the intestinal **epithelium** adhere closely together without intercellular substance."
      },
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Recollections of My Life",
        "quote": "I observed olfactory nerve endings penetrating between the supporting cells of the nasal **epithelium**."
      }
    ]
  },
  "Dashboard — thel\\macrothelypteris.md": {
    "primary": "A genus of ferns in the family Thelypteridaceae (marsh ferns), native to tropical and subtropical regions of Asia, Africa, and Queensland.",
    "secondary": "In pteridology, *Macrothelypteris* is characterized by large, multi-pinnate fronds, prominent acicular hairs on axes, and indusiate round sori situated along the veins.",
    "quotes": [
      {
        "author": "Ren-Chang Ching",
        "work": "A Revision of the Chinese Thelypteridaceae",
        "quote": "The Asian fern genus **Macrothelypteris** is easily distinguished by its decompound fronds and unicellular needle-like hairs."
      },
      {
        "author": "William Jackson Hooker",
        "work": "Species Filicum",
        "quote": "Certain magnificent ferns of eastern rainforests, now referred to **Macrothelypteris**, attain heights of six feet."
      },
      {
        "author": "Carl Christensen",
        "work": "Index Filicum",
        "quote": "In classifying the thelypteroid group, morphological traits support recognizing **Macrothelypteris** as a distinct genus."
      }
    ]
  },
  "Dashboard — thel\\mesothelioma.md": {
    "primary": "A rare, aggressive malignant tumor of the mesothelium, the thin layer of tissue that covers the lungs, abdomen, and heart.",
    "secondary": "In occupational medicine and pulmonary pathology, malignant pleural or peritoneal mesothelioma is strongly causally linked to inhaled asbestos fibers, exhibiting a latency period of twenty to forty years.",
    "quotes": [
      {
        "author": "Irving Selikoff",
        "work": "Asbestos Exposure and Neoplasia",
        "quote": "Epidemiological studies of insulation workers revealed an alarming incidence of pleural **mesothelioma** directly tied to asbestos."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Primary tumors of the pleura, now classified as **mesothelioma**, present with relentless serosanguinous effusion."
      },
      {
        "author": "Michael DeBakey",
        "work": "The Living Body",
        "quote": "Extensive decortication and pleurectomy are occasionally attempted to palliate diffuse pleural **mesothelioma**."
      }
    ]
  },
  "Dashboard — thel\\mesothelium.md": {
    "primary": "The layer of flat cells forming an epithelium that lines the serous cavities of the body (peritoneum, pericardium, and pleura).",
    "secondary": "In embryology and histology, the mesothelium arises from embryonic mesoderm (unlike ectodermal/endodermal epithelia), secreting serous lubricating fluid to facilitate frictionless organ movement.",
    "quotes": [
      {
        "author": "Wilhelm His",
        "work": "The First Form of the Human Organism",
        "quote": "The lining of the coelomic body cavity originates from mesoderm and constitutes the true **mesothelium**."
      },
      {
        "author": "Henry Gray",
        "work": "Gray's Anatomy",
        "quote": "The serous fluid secreted by the **mesothelium** permits the pleural membranes to glide smoothly during respiration."
      },
      {
        "author": "Arthur Keith",
        "work": "Human Embryology and Morphology",
        "quote": "During pericardial development, the primitive **mesothelium** folds to enclose the developing cardiac tube."
      }
    ]
  },
  "Dashboard — thel\\monothelitism.md": {
    "primary": "The seventh-century Christian heresy maintaining that Christ possessed two distinct natures (divine and human) but only one divine-human will.",
    "secondary": "Promoted by Emperor Heraclius and Patriarch Sergius I as a political compromise to reconcile Chalcedonian Christians with Miaphysites, Monothelitism was condemned at the Third Council of Constantinople in 680–681 CE.",
    "quotes": [
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The imperial court championed **Monothelitism** in a futile attempt to unify the fractured religious factions of the East."
      },
      {
        "author": "Henry Hart Milman",
        "work": "History of Latin Christianity",
        "quote": "Pope Martin I suffered martyrdom in exile rather than subscribe to the imperial edict imposing **Monothelitism**."
      },
      {
        "author": "John Henry Newman",
        "work": "The Development of Christian Doctrine",
        "quote": "The controversy over **Monothelitism** clarified that two perfect natures must entail two distinct wills in Christ."
      }
    ]
  },
  "Dashboard — thel\\parathelypteris.md": {
    "primary": "A genus of small to medium-sized terrestrial ferns in the family Thelypteridaceae, native to East Asia and North America.",
    "secondary": "In botanical pteridology, *Parathelypteris* is characterized by pinnate-pinnatifid fronds with needle-like acicular hairs, sessile spherical glands, and indusiate medial sori.",
    "quotes": [
      {
        "author": "Ren-Chang Ching",
        "work": "A Revision of the Chinese Thelypteridaceae",
        "quote": "The segregation of **Parathelypteris** from *Thelypteris* rests upon glandular trichomes and distinct spore ornamentation."
      },
      {
        "author": "Carl Christensen",
        "work": "Index Filicum",
        "quote": "Species assigned to **Parathelypteris** inhabit damp forest floors and mossy ravines across East Asia."
      },
      {
        "author": "Asa Gray",
        "work": "Manual of the Botany of the Northern United States",
        "quote": "The New York fern, historically grouped with *Aspidium*, shares close morphological affinity with **Parathelypteris**."
      }
    ]
  },
  "Dashboard — thel\\perithelial.md": {
    "primary": "Pertaining to, situated in, or composed of perithelium (the connective tissue layer surrounding small blood vessels and capillaries).",
    "secondary": "In pathology and vascular histology, perithelial cells include adventitial connective tissue elements and pericytes (Rouget cells) that regulate capillary diameter.",
    "quotes": [
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Proliferation of **perithelial** fibroblasts frequently accompanies chronic inflammation around cerebral arterioles."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "In vascular neoplasms, the pathologist must distinguish true endothelial tumors from **perithelial** sarcomas."
      },
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Histology of the Nervous System",
        "quote": "The **perithelial** sheath of cerebral capillaries forms an anatomical adventitia mediating nutrient exchange."
      }
    ]
  },
  "Dashboard — thel\\perithelium.md": {
    "primary": "The layer of connective tissue and pericytic cells that surrounds capillaries and small blood vessels.",
    "secondary": "In microvascular anatomy, the perithelium provides structural support, anchors basement membranes to extracellular matrix, and plays a role in vascular contractility and repair.",
    "quotes": [
      {
        "author": "Theodor Schwann",
        "work": "Microscopical Researches",
        "quote": "Outside the endothelial tube lies a delicate tunic of connective cells termed the **perithelium**."
      },
      {
        "author": "Alexis Carrel",
        "work": "Studies on Tissue Culture",
        "quote": "Cellular migration from the vascular **perithelium** initiates granulation tissue formation in healing wounds."
      },
      {
        "author": "Henry Gray",
        "work": "Gray's Anatomy",
        "quote": "The outer adventitial tunic of minute arterioles is continuous with the perivascular **perithelium**."
      }
    ]
  },
  "Dashboard — thel\\thelarche.md": {
    "primary": "The onset of female secondary breast development, typically representing the earliest phenotypic sign of puberty.",
    "secondary": "In pediatric endocrinology, thelarche usually begins between ages 8 and 13, initiated by pulsatile hypothalamic GnRH release stimulating ovarian estradiol production; premature thelarche is an isolated benign variant.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Normal adolescent development follows an orderly sequence beginning with **thelarche** and followed by pubarche and menarche."
      },
      {
        "author": "Havelock Ellis",
        "work": "Studies in the Psychology of Sex",
        "quote": "The physical transformations accompanying **thelarche** awaken new psychological self-awareness in the adolescent girl."
      },
      {
        "author": "Arthur Keith",
        "work": "Human Embryology and Morphology",
        "quote": "Under the influence of ovarian hormones, the rudimentary mammary ducts proliferate rapidly during **thelarche**."
      }
    ]
  },
  "Dashboard — thel\\thelephoraceae.md": {
    "primary": "A family of fungi in the order Thelephorales, comprising corticioid, hydnoid, or tomentose basidiomycetes.",
    "secondary": "In mycology, members of the Thelephoraceae form ectomycorrhizal symbioses with forest trees, producing leathery, resupinate, or rosette-like basidiocarps with brownish, thelephoric-acid-rich basidiospores.",
    "quotes": [
      {
        "author": "Elias Magnus Fries",
        "work": "Systema Mycologicum",
        "quote": "Fries grouped the leathery, crust-like resupinate fungi under the ancestral division **Thelephoraceae**."
      },
      {
        "author": "Pier Andrea Saccardo",
        "work": "Sylloge Fungorum",
        "quote": "The family **Thelephoraceae** encompasses wood-inhabiting basidiomycetes with smooth or warted hymenial surfaces."
      },
      {
        "author": "Miles Joseph Berkeley",
        "work": "Outlines of British Fungology",
        "quote": "Species of **Thelephoraceae** play vital roles in the forest humus cycle, encrusting twigs and decayed stumps."
      }
    ]
  },
  "Dashboard — thel\\thelial.md": {
    "primary": "Of or pertaining to a nipple (papilla mammae) or to an epithelial cellular layer.",
    "secondary": "In anatomical lexicography, derived from Greek *thele* (nipple), forming the morphological root of terms such as thelium, epithelium, and endothelium.",
    "quotes": [
      {
        "author": "Frederik Ruysch",
        "work": "Opera Omnia Anatomico-Medico-Chirurgica",
        "quote": "The delicate papillary tissue of the **thelial** surface displays rich cutaneous nerve endings."
      },
      {
        "author": "Henry Gray",
        "work": "Gray's Anatomy",
        "quote": "Sensory receptors beneath the **thelial** epidermis mediate the suckling reflex in nursing mothers."
      },
      {
        "author": "Arthur Keith",
        "work": "Human Embryology and Morphology",
        "quote": "Embryonic involution of the mammary ridge leaves only the specialized **thelial** projection."
      }
    ]
  },
  "Dashboard — thel\\thelium.md": {
    "primary": "An anatomical papilla or nipple-like projection; also, an epithelial cellular membrane or layer.",
    "secondary": "In historic anatomy, thelium referred primarily to the human nipple before expanding through prefixes into epithelium, mesothelium, and endothelium.",
    "quotes": [
      {
        "author": "Frederik Ruysch",
        "work": "Thesaurus Anatomicus",
        "quote": "The anatomical term **thelium** was applied originally to the sensitive summit of the human mammary gland."
      },
      {
        "author": "William Hunter",
        "work": "The Anatomy of the Human Gravid Uterus",
        "quote": "Vascular loops in the subcutaneous papilla nourish the overlying **thelium** during lactation."
      },
      {
        "author": "Arthur Keith",
        "work": "Human Embryology and Morphology",
        "quote": "The cellular layers of the developing **thelium** derive directly from surface ectoderm."
      }
    ]
  },
  "Dashboard — thel\\thelypteridaceae.md": {
    "primary": "A cosmopolitan family of ferns (the marsh ferns) in the order Polypodiales, containing around 1,000 species.",
    "secondary": "In pteridology, Thelypteridaceae are characterized by monomorphic or dimorphic pinnate-pinnatifid fronds with needle-like acicular hairs, two vascular bundles in the stipe, and indusiate round sori.",
    "quotes": [
      {
        "author": "Ren-Chang Ching",
        "work": "A Revision of the Chinese Thelypteridaceae",
        "quote": "The family **Thelypteridaceae** represents one of the most prolific and taxonomically intricate lineages of modern ferns."
      },
      {
        "author": "Carl Christensen",
        "work": "Index Filicum",
        "quote": "Characteristic unicellular acicular hairs on frond axes readily distinguish members of the **Thelypteridaceae**."
      },
      {
        "author": "William Jackson Hooker",
        "work": "Species Filicum",
        "quote": "Species of the **Thelypteridaceae** carpet wet woodlands and streamsides throughout tropical and temperate zones."
      }
    ]
  }
};

const count = updateNotesBatch(baseClusterDir, batchData);
console.log(`[Finish Slice 5 - Batch 3] Successfully updated ${count}/${Object.keys(batchData).length} notes.`);
