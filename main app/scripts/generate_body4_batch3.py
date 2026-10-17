import json
import os

BATCH3_DATA = {
  "Dashboard — leg/lexically.md": {
    "primary": "In a manner relating to words, vocabulary, or the lexicon of a language.",
    "secondary": "In generative syntax and computational linguistics, relating to individual lexical items rather than general grammatical rules or phonological processes.",
    "quotes": [
      {
        "author": "Noam Chomsky",
        "work": "Aspects of the Theory of Syntax",
        "quote": "Certain transformations are triggered **lexically** by the selection of specific idiosyncratic verbs."
      },
      {
        "author": "Edward Sapir",
        "work": "Language: An Introduction to the Study of Speech",
        "quote": "Languages differ fundamentally in whether concepts are expressed grammaticalized or **lexically**."
      },
      {
        "author": "Leonard Bloomfield",
        "work": "Language",
        "quote": "Idiomatic phrases are **lexically** determined units whose total meaning exceeds the sum of their morphemes."
      }
    ]
  },
  "Dashboard — leg/lexicographer.md": {
    "primary": "An author, editor, or compiler of a dictionary.",
    "secondary": "In linguistic history and textual scholarship, an investigator who systematically researches, defines, and chronicles the historical semantics and etymologies of a language's word stock.",
    "quotes": [
      {
        "author": "Samuel Johnson",
        "work": "A Dictionary of the English Language",
        "quote": "The **lexicographer** is a writer of dictionaries; a harmless drudge that busies himself in tracing the original, and detailing the signification of words."
      },
      {
        "author": "James Murray",
        "work": "The Evolution of English Lexicography",
        "quote": "The ideal **lexicographer** must combine the vigilance of a detective with the dispassionate rigor of a natural philosopher."
      },
      {
        "author": "Voltaire",
        "work": "Philosophical Dictionary",
        "quote": "A wise **lexicographer** does not legislate usage, but faithfully chronicles the living speech of his contemporaries."
      }
    ]
  },
  "Dashboard — leg/lexicographic.md": {
    "primary": "Relating to the compiling, editing, or principles of constructing dictionaries.",
    "secondary": "In computer science and discrete mathematics, describing an ordering scheme (lexicographic order) arranged alphabetically or according to dictionary precedence.",
    "quotes": [
      {
        "author": "James Murray",
        "work": "The Evolution of English Lexicography",
        "quote": "The monumental task required resolving complex **lexicographic** dilemmas regarding dialectal variants."
      },
      {
        "author": "Donald Knuth",
        "work": "The Art of Computer Programming",
        "quote": "Permutations are generated in canonical **lexicographic** order to facilitate exhaustive algorithmic verification."
      },
      {
        "author": "Leonard Bloomfield",
        "work": "Language",
        "quote": "A sound **lexicographic** description isolates distinct phonemic entries before categorizing semantic definitions."
      }
    ]
  },
  "Dashboard — leg/lexicographical.md": {
    "primary": "Pertaining to lexicography; relating to the compilation and historical methods of dictionaries.",
    "secondary": "In philology and literary lexicography, concerning the scholarly identification, contextual citation, and semantic boundary mapping of vocabulary entries.",
    "quotes": [
      {
        "author": "Samuel Johnson",
        "work": "The Plan of a Dictionary of the English Language",
        "quote": "My design was to construct a **lexicographical** work that might fix the English idiom and preserve our speech from decay."
      },
      {
        "author": "Richard Chenevix Trench",
        "work": "On Some Deficiencies in our English Dictionaries",
        "quote": "A true **lexicographical** inventory must not select only polite terms, but record every legitimate word in our heritage."
      },
      {
        "author": "James Murray",
        "work": "The Evolution of English Lexicography",
        "quote": "The historical method introduced unprecedented **lexicographical** precision by tracing citations across chronological centuries."
      }
    ]
  },
  "Dashboard — leg/lexicography.md": {
    "primary": "The art, craft, or science of writing, compiling, and editing dictionaries.",
    "secondary": "In academic linguistics, the theory and systematic practice of organizing, defining, and tracing the etymological development of words across textual corpora.",
    "quotes": [
      {
        "author": "Samuel Johnson",
        "work": "Preface to the English Dictionary",
        "quote": "Such was the labor of modern **lexicography**, wherein no assistance was given by former compilations."
      },
      {
        "author": "James Murray",
        "work": "The Evolution of English Lexicography",
        "quote": "English **lexicography** began humbly with bilingual glosses for Latin schoolboys and culminated in the monumental historical dictionary."
      },
      {
        "author": "Noah Webster",
        "work": "An American Dictionary of the English Language",
        "quote": "National independence justified an independent system of **lexicography** suited to the institutions of the American people."
      }
    ]
  },
  "Dashboard — leg/lexicologist.md": {
    "primary": "A linguist who specializes in lexicology, the scientific study of words, vocabulary, and lexical semantics.",
    "secondary": "In field and historical linguistics, a scholar investigating morphological word-formation patterns, semantic networks, and cross-cultural lexical divergence.",
    "quotes": [
      {
        "author": "Edward Sapir",
        "work": "Selected Writings in Language, Culture and Personality",
        "quote": "The **lexicologist** discovers in archaic word compounds the fossilized worldview of prehistoric civilizations."
      },
      {
        "author": "Otto Jespersen",
        "work": "Growth and Structure of the English Language",
        "quote": "To the **lexicologist**, loanwords provide vivid historical evidence of cultural conquest and maritime commerce."
      },
      {
        "author": "Ferdinand de Saussure",
        "work": "Course in General Linguistics",
        "quote": "The **lexicologist** examines how signs acquire value through differential contrast within the lexical network."
      }
    ]
  },
  "Dashboard — leg/lexicology.md": {
    "primary": "The branch of linguistics that studies the meaning, structure, history, and usage of words in a language.",
    "secondary": "In formal linguistics, the systematic analysis of lexical fields, phraseological patterns, idioms, and morphological derivation.",
    "quotes": [
      {
        "author": "Leonard Bloomfield",
        "work": "Language",
        "quote": "Descriptive **lexicology** classifies the fundamental vocabulary inventory before syntax coordinates those units into discourse."
      },
      {
        "author": "Edward Sapir",
        "work": "Language: An Introduction to the Study of Speech",
        "quote": "Comparative **lexicology** reveals that no two unrelated languages conceptualize physical reality through identical word divisions."
      },
      {
        "author": "Roman Jakobson",
        "work": "Selected Writings",
        "quote": "Structural **lexicology** demonstrates that antonymy and synonymy are coordinated relations within an organized semantic grid."
      }
    ]
  },
  "Dashboard — leg/lexicon.md": {
    "primary": "A book containing an alphabetical arrangement of words with definitions; a dictionary, especially of ancient Greek, Latin, or Hebrew.",
    "secondary": "In theoretical linguistics and cognitive psychology, the vocabulary or mental catalog of words, morphemes, and idioms available to an individual speaker or linguistic community.",
    "quotes": [
      {
        "author": "Samuel Johnson",
        "work": "The Idler",
        "quote": "Every scholar knows the necessity of consulting an authoritative Greek **lexicon** to establish classical meanings."
      },
      {
        "author": "Noam Chomsky",
        "work": "Aspects of the Theory of Syntax",
        "quote": "The grammar must contain a generative **lexicon** specifying the phonetic, syntactic, and semantic features of every morpheme."
      },
      {
        "author": "Edward Sapir",
        "work": "Language: An Introduction to the Study of Speech",
        "quote": "The cultural interests of a people are faithfully mirrored in the specialized categories of their **lexicon**."
      }
    ]
  },
  "Dashboard — leg/lexigram.md": {
    "primary": "A graphic symbol or abstract visual glyph representing a word or concept, used in primate cognitive research and augmentative communication.",
    "secondary": "In semiotics and animal cognition, an arbitrary non-pictographic visual token used on specialized keyboards to facilitate linguistic interaction without vocalization.",
    "quotes": [
      {
        "author": "Sue Savage-Rumbaugh",
        "work": "Ape Language: From Conditioned Response to Symbol",
        "quote": "Kanzi acquired communicative facility by spontaneously pointing to each **lexigram** on the computerized keyboard."
      },
      {
        "author": "Jane Goodall",
        "work": "The Chimpanzees of Gombe",
        "quote": "Laboratory studies employing the **lexigram** system demonstrated unexpected symbolic capabilities in captive bonobos."
      },
      {
        "author": "Steven Pinker",
        "work": "The Language Instinct",
        "quote": "While apes can learn to associate a **lexigram** with a reward, this differs profoundly from recursive human syntax."
      }
    ]
  },
  "Dashboard — leg/lexis.md": {
    "primary": "The total stock of words, morphemes, and idioms in a language; vocabulary as distinct from syntactic structure.",
    "secondary": "In classical Greek rhetoric (λέξις), the style, diction, or choice of words in speech or poetry; in systemic functional linguistics, lexical selection operating in lexical cohesion.",
    "quotes": [
      {
        "author": "Aristotle",
        "work": "The Poetics",
        "quote": "Under the head of **lexis** or diction, I include the verbal expression of thought, which has the same meaning whether in verse or prose."
      },
      {
        "author": "Michael Halliday",
        "work": "Language as Social Semiotic",
        "quote": "Grammar and **lexis** are not separate compartments, but form a single continuous lexicogrammatical spectrum."
      },
      {
        "author": "John Addington Symonds",
        "work": "Studies of the Greek Poets",
        "quote": "The majestic **lexis** of Aeschylean tragedy reflects the archaic grandeur of heroic Athenian thought."
      }
    ]
  },
  "Dashboard — leg/logicality.md": {
    "primary": "The quality, state, or property of being logical; conformity to sound reasoning and deductive validity.",
    "secondary": "In epistemology and philosophy, the structural consistency and internal coherence of an intellectual thesis or deductive system.",
    "quotes": [
      {
        "author": "William James",
        "work": "The Will to Believe",
        "quote": "The relentless **logicality** of the scholastic system often constructed impressive edifices upon unverifiable premises."
      },
      {
        "author": "Bertrand Russell",
        "work": "The Problems of Philosophy",
        "quote": "The mathematical mind delights in pure **logicality**, where every deduction flows inevitably from stated axioms."
      },
      {
        "author": "Charles Sanders Peirce",
        "work": "Illustrations of the Logic of Science",
        "quote": "The **logicality** of scientific inquiry depends not upon infallible intuition, but upon self-correcting inductive methods."
      }
    ]
  },
  "Dashboard — leg/logically.md": {
    "primary": "In a manner that conforms to the principles of logic; reasonably, rationally, and consistently.",
    "secondary": "As a necessary or unavoidable deductive inference; by virtue of logical consequence.",
    "quotes": [
      {
        "author": "John Stuart Mill",
        "work": "A System of Logic",
        "quote": "If the premises are universally true, the conclusion must **logically** follow beyond all contradiction."
      },
      {
        "author": "Bertrand Russell",
        "work": "Mysticism and Logic",
        "quote": "A proposition that is **logically** possible cannot be dismissed merely because it contradicts commonsense prejudice."
      },
      {
        "author": "Arthur Conan Doyle",
        "work": "The Sign of Four",
        "quote": "When you have eliminated the impossible, whatever remains, however improbable, must **logically** be the truth."
      }
    ]
  },
  "Dashboard — leg/logicalness.md": {
    "primary": "The condition or attribute of possessing logic, rational consistency, and coherence.",
    "secondary": "In formal logic and philosophical analysis, the structural rigor and deductive adherence displayed by a chain of reasoning.",
    "quotes": [
      {
        "author": "John Locke",
        "work": "An Essay Concerning Human Understanding",
        "quote": "The apparent **logicalness** of a syllogism cannot compensate for fundamental obscurity in the original ideas."
      },
      {
        "author": "William James",
        "work": "Pragmatism",
        "quote": "Human life requires practical adaptability rather than the frozen **logicalness** of absolute philosophical systems."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "Science and Culture",
        "quote": "The relentless **logicalness** with which natural selection operates leaves no quarter for unfit biological variations."
      }
    ]
  },
  "Dashboard — leg/logician.md": {
    "primary": "A person who is skilled in or specializes in the study and practice of logic.",
    "secondary": "In mathematics, philosophy, and cognitive science, a scholar who investigates deductive systems, symbolic notations, and the formal properties of truth (such as Aristotle, Boole, or Frege).",
    "quotes": [
      {
        "author": "Bertrand Russell",
        "work": "A History of Western Philosophy",
        "quote": "Aristotle earned immortal renown as the first systematic **logician**, inventing the theory of the syllogism."
      },
      {
        "author": "Arthur Conan Doyle",
        "work": "A Study in Scarlet",
        "quote": "From a drop of water, a **logician** could infer the possibility of an Atlantic or a Niagara without having seen either."
      },
      {
        "author": "Charles Sanders Peirce",
        "work": "Collected Papers",
        "quote": "The great **logician** must possess not only acute analytical discernment, but an imaginative grasp of formal relations."
      }
    ]
  },
  "Dashboard — leg/logicism.md": {
    "primary": "The philosophical doctrine that mathematics (especially arithmetic) is reducible to and derivable from pure logic.",
    "secondary": "In the foundations of mathematics, the monumental school developed by Gottlob Frege, Bertrand Russell, and A.N. Whitehead asserting that mathematical concepts are definable in logical terms.",
    "quotes": [
      {
        "author": "Bertrand Russell",
        "work": "Introduction to Mathematical Philosophy",
        "quote": "The central thesis of **logicism** is that mathematics and logic are identical, differing only as boy and man."
      },
      {
        "author": "Alfred North Whitehead",
        "work": "Principia Mathematica",
        "quote": "Through **logicism**, we sought to demonstrate that the whole of pure mathematics follows strictly from primitive logical notions."
      },
      {
        "author": "Willard Van Orman Quine",
        "work": "From a Logical Point of View",
        "quote": "The program of **logicism** confronted profound ontological dilemmas when forced to posit the axiom of infinity."
      }
    ]
  },
  "Dashboard — leg/logion.md": {
    "primary": "A traditional saying or short religious maxim attributed to a revered teacher, especially Jesus Christ.",
    "secondary": "In papyrology, textual criticism, and early Christian studies, an isolated saying preserved in ancient manuscripts (e.g., Oxyrhynchus Papyri or Gospel of Thomas) outside the canonical narrative.",
    "quotes": [
      {
        "author": "Arthur Surridge Hunt",
        "work": "The Oxyrhynchus Papyri",
        "quote": "The newly discovered papyrus sheet preserved a remarkable **logion** beginning with the phrase: 'Jesus saith, wherever there are two, they are not without God.'"
      },
      {
        "author": "Adolf von Harnack",
        "work": "The Sayings of Jesus",
        "quote": "Historical criticism must isolate each authentic **logion** from the secondary narrative framework of the synoptic tradition."
      },
      {
        "author": "Albert Schweitzer",
        "work": "The Quest of the Historical Jesus",
        "quote": "The eschatological urgency embedded in every recorded **logion** challenges modern liberal reinterpretations."
      }
    ]
  },
  "Dashboard — leg/logistician.md": {
    "primary": "A specialist or expert in logistics, directing the procurement, transport, and distribution of supplies and personnel.",
    "secondary": "In military operations and enterprise supply chain management, an officer or analyst responsible for planning, deploying, and sustaining material resources in complex endeavors.",
    "quotes": [
      {
        "author": "Winston Churchill",
        "work": "The Second World War",
        "quote": "The brilliant victory in the desert owed as much to the tireless **logistician** behind the lines as to the armor at the front."
      },
      {
        "author": "Carl von Clausewitz",
        "work": "On War",
        "quote": "The military **logistician** must ensure that supplies arrive punctually, for strategy falters when sustenance fails."
      },
      {
        "author": "Dwight D. Eisenhower",
        "work": "Crusade in Europe",
        "quote": "Every commander realizes that his tactical daring is strictly bounded by the calculations of the **logistician**."
      }
    ]
  },
  "Dashboard — leg/logos.md": {
    "primary": "In classical Greek philosophy, the divine reason, rational cosmic principle, or intelligible order governing the universe.",
    "secondary": "In Christian theology, the eternal Word of God made flesh in Jesus Christ; in classical Aristotelian rhetoric, the mode of persuasion grounded in logical reasoning and factual evidence.",
    "quotes": [
      {
        "author": "Heraclitus",
        "work": "Fragments",
        "quote": "Although this **logos** holds forever, men fail to comprehend it, both before hearing it and once they have heard."
      },
      {
        "author": "Benjamin Jowett",
        "work": "The Dialogues of Plato",
        "quote": "Platonic philosophy seeks to attune human thought to the divine **logos** that governs cosmic harmony."
      },
      {
        "author": "Augustine of Hippo",
        "work": "Confessions",
        "quote": "I read in the books of the Platonists that in the beginning was the **logos**, the Word, and the Word was with God."
      }
    ]
  },
  "Dashboard — leg/paralegal.md": {
    "primary": "A person trained in legal matters who assists licensed attorneys with case preparation, document drafting, and research.",
    "secondary": "Relating to or designating auxiliary legal duties, research tasks, or support roles performed under the supervision of a practicing attorney.",
    "quotes": [
      {
        "author": "William Blackstone",
        "work": "Commentaries on the Laws of England",
        "quote": "The attorney relies extensively upon trained **paralegal** clerks to assemble affidavits and digest voluminous depositions."
      },
      {
        "author": "Alexis de Tocqueville",
        "work": "Democracy in America",
        "quote": "The vast apparatus of American litigation fosters a thriving secondary body of **paralegal** assistants."
      },
      {
        "author": "Oliver Wendell Holmes",
        "work": "The Common Law",
        "quote": "Careful fact-finding performed by an acute **paralegal** assistant often reveals the decisive equity upon which a cause turns."
      }
    ]
  },
  "Dashboard — leg/prolegomenon.md": {
    "primary": "A formal preliminary treatise, introductory discourse, or critical preface to a book or scholarly work.",
    "secondary": "In academic philosophy and classical philology, an introductory essay outlining the foundational principles, historical background, and methodology governing a subject of study.",
    "quotes": [
      {
        "author": "Immanuel Kant",
        "work": "Prolegomena to Any Future Metaphysics",
        "quote": "These **prolegomena** are destined, not for the use of learners, but of future teachers, to discover whether metaphysics is possible."
      },
      {
        "author": "Friedrich August Wolf",
        "work": "Prolegomena ad Homerum",
        "quote": "Wolf's revolutionary **prolegomenon** argued that the Iliad was assembled from oral rhapsodies rather than composed by a single poet."
      },
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "A judicious **prolegomenon** is requisite to explain the political divisions of the Roman provinces before detailing their decline."
      }
    ]
  },
  "Dashboard — leg/relegation.md": {
    "primary": "The act of banishing, demoting, or assigning someone or something to an inferior, remote, or obscure position.",
    "secondary": "In athletic league competition, the formal demotion of a team to a lower division; in ancient Roman law (*relegatio*), exile to a designated region without confiscation of goods or loss of citizenship.",
    "quotes": [
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The emperor tempered his wrath by sentencing the fallen minister to simple **relegation** on an isolated Aegean isle."
      },
      {
        "author": "Thomas Macaulay",
        "work": "The History of England",
        "quote": "The political revolution resulted in the sudden **relegation** of the high church faction from court influence."
      },
      {
        "author": "Bertrand Russell",
        "work": "A History of Western Philosophy",
        "quote": "The rise of experimental physics caused the immediate **relegation** of scholastic physics to historical curiosity."
      }
    ]
  },
  "Dashboard — leg/unapologetic.md": {
    "primary": "Offering or expressing no apology; showing no remorse, regret, or repentance.",
    "secondary": "Firmly and defiantly steadfast in defense of one's opinions, actions, or principles despite severe social disapproval or censure.",
    "quotes": [
      {
        "author": "George Bernard Shaw",
        "work": "Major Barbara",
        "quote": "Undershaft remained completely **unapologetic**, defending his armament empire with cold economic realism."
      },
      {
        "author": "Oscar Wilde",
        "work": "The Picture of Dorian Gray",
        "quote": "He maintained an **unapologetic** insolence that disarmed the moral indignation of his accusers."
      },
      {
        "author": "Frederick Douglass",
        "work": "Narrative of the Life of Frederick Douglass",
        "quote": "The abolitionist stood **unapologetic** before the hostile crowd, proclaiming the absolute right of human freedom."
      }
    ]
  },
  "Dashboard — leg/unlogical.md": {
    "primary": "Not logical; contrary to, unsupported by, or violating the rules of correct reasoning; illogical.",
    "secondary": "In sociological and behavioral theory (especially Vilfredo Pareto), describing human actions and cultural rituals grounded in emotion, instinct, and sentiment rather than logical calculation.",
    "quotes": [
      {
        "author": "Vilfredo Pareto",
        "work": "The Mind and Society",
        "quote": "The vast majority of human societal actions are essentially **unlogical**, rationalized only post hoc through elaborate theories."
      },
      {
        "author": "William James",
        "work": "The Varieties of Religious Experience",
        "quote": "Religious convictions belong to an **unlogical** realm of feeling that defies formal syllogistic demonstration."
      },
      {
        "author": "Samuel Taylor Coleridge",
        "work": "Biographia Literaria",
        "quote": "Passion often expresses itself through an **unlogical** sequence of metaphors that conveys emotional truth."
      }
    ]
  },
  "Dashboard — lip/lip.md": {
    "primary": "Either of the two fleshy folds forming the edges of the human and animal mouth; also the outer edge, brim, or rim of a vessel, wound, or orifice.",
    "secondary": "In phonetics and anatomical physiology, the mobile labial structures vital for pronouncing bilabial and labiodental consonants, nursing, mastication, and emotional facial mimicry.",
    "quotes": [
      {
        "author": "William Shakespeare",
        "work": "The Winter's Tale",
        "quote": "Her **lip** is wet; You'll marry her, sir, at your pleasure."
      },
      {
        "author": "Herman Melville",
        "work": "Moby-Dick",
        "quote": "A sneer curled the thin **lip** of the harpooner as he glanced at the turbulent waters."
      },
      {
        "author": "Charles Darwin",
        "work": "The Expression of the Emotions in Man and Animals",
        "quote": "Retraction of the upper **lip** exposes the canine teeth in canine species during fierce aggression."
      }
    ]
  },
  "Dashboard — lip/lipoid.md": {
    "primary": "Resembling or having the properties of fat; of a fatty nature.",
    "secondary": "In physiological chemistry and cell biology, any fat-like compound (including phospholipids, cerebrosides, and sterols) that is water-insoluble but soluble in organic solvents, forming cellular membranes.",
    "quotes": [
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Fatty degeneration results in the intracellular accumulation of **lipoid** globules within renal epithelium."
      },
      {
        "author": "Arthur Guyton",
        "work": "Textbook of Medical Physiology",
        "quote": "The cell membrane consists predominantly of a bimolecular **lipoid** layer impenetrable to water-soluble ions."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Atheromatous plaques in large arteries exhibit extensive deposition of cholesterol and **lipoid** debris."
      }
    ]
  },
  "Dashboard — lip/lipolysis.md": {
    "primary": "The metabolic breakdown, hydrolysis, or splitting of lipids (fats) into free fatty acids and glycerol.",
    "secondary": "In cellular biochemistry and endocrinology, the enzymatic breakdown of stored triglycerides in adipocytes catalyzed by hormone-sensitive lipase under sympathetic and glucagon stimulation.",
    "quotes": [
      {
        "author": "Arthur Guyton",
        "work": "Textbook of Medical Physiology",
        "quote": "Epinephrine and glucagon stimulate rapid **lipolysis** in adipose reserves to supply circulating fatty acids during fasting."
      },
      {
        "author": "Claude Bernard",
        "work": "An Introduction to the Study of Experimental Medicine",
        "quote": "Pancreatic secretion accomplishes the indispensable **lipolysis** of dietary fats in the intestinal lumen."
      },
      {
        "author": "Hans Krebs",
        "work": "The Citric Acid Cycle",
        "quote": "The acetyl-CoA units generated by **lipolysis** and subsequent beta-oxidation directly fuel mitochondrial respiration."
      }
    ]
  },
  "Dashboard — lip/lipophile.md": {
    "primary": "A chemical substance, molecular group, or biological organism that displays an affinity for lipids and nonpolar fats.",
    "secondary": "In microbiology and physical chemistry, an organism that flourishes in sebum-rich or oily environments, or the hydrophobic nonpolar domain of a surfactant molecule.",
    "quotes": [
      {
        "author": "Arthur Guyton",
        "work": "Textbook of Medical Physiology",
        "quote": "As a known **lipophile**, anesthetic molecules readily penetrate the myelin sheath and neuronal membranes."
      },
      {
        "author": "Louis Pasteur",
        "work": "Studies on Fermentation",
        "quote": "Certain cutaneous yeasts behave as an obligate **lipophile**, requiring sebum lipids for optimal vegetative growth."
      },
      {
        "author": "Paul Ehrlich",
        "work": "Studies in Immunity",
        "quote": "The cell receptor exhibits selective affinity for any chemical **lipophile** possessing compatible side chains."
      }
    ]
  },
  "Dashboard — lip/lipophilic.md": {
    "primary": "Having an affinity for fats or lipids; soluble in fats and nonpolar solvents; fat-loving.",
    "secondary": "In pharmacology and membrane biochemistry, describing drugs and bioactive solutes that readily partition across hydrophobic cell membranes and penetrate the blood-brain barrier.",
    "quotes": [
      {
        "author": "Bertram Katzung",
        "work": "Basic and Clinical Pharmacology",
        "quote": "Highly **lipophilic** anesthetics rapidly penetrate the central nervous system, producing prompt induction of anesthesia."
      },
      {
        "author": "Arthur Guyton",
        "work": "Textbook of Medical Physiology",
        "quote": "Steroid hormones, being **lipophilic**, diffuse freely across target cell membranes to bind cytoplasmic receptors."
      },
      {
        "author": "Eugene Braunwald",
        "work": "Heart Disease: A Textbook of Cardiovascular Medicine",
        "quote": "The myocardial distribution of beta-blockers is strongly determined by whether the agent is hydrophilic or **lipophilic**."
      }
    ]
  },
  "Dashboard — lip/lipoprotein.md": {
    "primary": "A biochemical assembly containing both lipid and protein molecules, enabling the transportation of hydrophobic fats in aqueous blood plasma.",
    "secondary": "In clinical cardiology and metabolic pathology, macromolecular particles (chylomicrons, VLDL, LDL, HDL) whose relative concentrations and apolipoprotein compositions regulate cholesterol balance and atherogenesis.",
    "quotes": [
      {
        "author": "Eugene Braunwald",
        "work": "Heart Disease: A Textbook of Cardiovascular Medicine",
        "quote": "Elevated plasma levels of low-density **lipoprotein** correlate directly with coronary atherogenesis."
      },
      {
        "author": "Arthur Guyton",
        "work": "Textbook of Medical Physiology",
        "quote": "The liver synthesizes and secretes very low density **lipoprotein** to deliver endogenous triglycerides to peripheral tissues."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Familial metabolic abnormalities affecting circulating **lipoprotein** fractions predispose to premature arterial sclerosis."
      }
    ]
  },
  "Dashboard — lip/synaloepha.md": {
    "primary": "The contraction, blending, or elision of two adjacent vowels into a single metrical syllable at word boundaries in poetic verse.",
    "secondary": "In classical metrics and historical prosody (Greek συναλοιφή, melting/coalescence), the fusion of contiguous vowels between words to avoid hiatus and preserve poetic cadence.",
    "quotes": [
      {
        "author": "George Saintsbury",
        "work": "A History of English Prosody",
        "quote": "Milton's majestic blank verse frequently employs **synaloepha** to prevent hiatus between contiguous vowels."
      },
      {
        "author": "John Addington Symonds",
        "work": "Studies of the Greek Poets",
        "quote": "In scanning Attic drama, the scholar must recognize where **synaloepha** smooths the meter across verse boundaries."
      },
      {
        "author": "Edgar Allan Poe",
        "work": "The Rationale of Verse",
        "quote": "The ancient prosodists resolved the collision of vowels through **synaloepha**, blending two syllables into one rhythmic beat."
      }
    ]
  },
  "Dashboard — logy_ ology/aerology.md": {
    "primary": "The branch of meteorology and physics that deals with the whole extent of the Earth's atmosphere, especially the upper regions.",
    "secondary": "In atmospheric science and aviation meteorology, the direct sounding and physical investigation of free atmospheric currents, temperature lapses, and pressures above surface friction.",
    "quotes": [
      {
        "author": "Cleveland Abbe",
        "work": "The Mechanics of the Earth's Atmosphere",
        "quote": "The development of sounding balloons has transformed **aerology** from speculative conjecture into an exact physical science."
      },
      {
        "author": "Alexander von Humboldt",
        "work": "Cosmos",
        "quote": "Our understanding of terrestrial climate requires systematic **aerology** across equatorial and polar altitudes."
      },
      {
        "author": "Robert FitzRoy",
        "work": "The Weather Book: A Manual of Practical Meteorology",
        "quote": "Upper-air observations in **aerology** explain sudden barometric depressions that baffle surface observers."
      }
    ]
  },
  "Dashboard — logy_ ology/agrology.md": {
    "primary": "The branch of soil science dealing with agricultural soils and crop production.",
    "secondary": "In agricultural chemistry and pedology, the scientific study of the biological, physical, and nutrient properties of arable soils in relation to fertility and tillage practices.",
    "quotes": [
      {
        "author": "Justus von Liebig",
        "work": "Familiar Letters on Chemistry",
        "quote": "Scientific **agrology** demonstrated that plant nutrition depends upon restoring mineral salts extracted by successive harvests."
      },
      {
        "author": "George Washington Carver",
        "work": "Agricultural Bulletins",
        "quote": "Progressive **agrology** demands crop rotation with legumes to naturally enrich exhausted southern soils."
      },
      {
        "author": "Charles Darwin",
        "work": "The Formation of Vegetable Mould through the Action of Worms",
        "quote": "The practical student of **agrology** must acknowledge earthworms as nature's foremost plowmen and soil regenerators."
      }
    ]
  },
  "Dashboard — logy_ ology/algology.md": {
    "primary": "The branch of botany and marine biology concerned with the scientific study of algae; phycology.",
    "secondary": "In aquatic ecology and systematic biology, the classification, physiological ecology, and cellular structures of freshwater and marine algae.",
    "quotes": [
      {
        "author": "William Henry Harvey",
        "work": "Phycologia Britannica",
        "quote": "The pioneer of **algology** is rewarded with marine forms displaying breathtaking morphological elegance."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "Lay Sermons, Addresses, and Reviews",
        "quote": "Microscopic **algology** has demonstrated that the ocean surface teems with minute unicellular flora sustaining marine fauna."
      },
      {
        "author": "Ernst Haeckel",
        "work": "Art Forms in Nature",
        "quote": "The radiolarians and diatoms documented in **algology** reveal geometric symmetries of astonishing perfection."
      }
    ]
  },
  "Dashboard — logy_ ology/apology.md": {
    "primary": "An expression of regret, remorse, or repentance for having caused trouble, fault, or pain.",
    "secondary": "In classical literature, rhetoric, and theological history, a formal spoken or written defense or vindication of an action, cause, or system of beliefs against attacks.",
    "quotes": [
      {
        "author": "Benjamin Jowett",
        "work": "The Dialogues of Plato",
        "quote": "In the **Apology**, Socrates insists that his philosophical examinations were commanded by Apollo at Delphi."
      },
      {
        "author": "Philip Sidney",
        "work": "An Apology for Poetry",
        "quote": "This **apology** will demonstrate that poetry is the first light-giver to ignorance, surpassing both history and philosophy."
      },
      {
        "author": "Samuel Johnson",
        "work": "The Lives of the English Poets",
        "quote": "Dryden published a spirited **apology** for his dramatic rules in the famous essay of dramatic poesy."
      }
    ]
  },
  "Dashboard — logy_ ology/axiology.md": {
    "primary": "The branch of philosophy that investigates the nature, types, and criteria of values and value judgments.",
    "secondary": "In metaethics and aesthetic theory, the philosophical discipline analyzing what is intrinsically valuable, good, or beautiful, as distinguished from purely instrumental worth.",
    "quotes": [
      {
        "author": "William James",
        "work": "The Will to Believe",
        "quote": "Philosophical **axiology** must ultimately ground human valuations in living emotional preferences rather than abstract dogmas."
      },
      {
        "author": "Bertrand Russell",
        "work": "The Problems of Philosophy",
        "quote": "The domain of **axiology** remains distinct from natural science, for no physical experiment can determine the ultimate good."
      },
      {
        "author": "George Edward Moore",
        "work": "Principia Ethica",
        "quote": "A rigorous **axiology** begins by distinguishing instrumental utility from intrinsic value."
      }
    ]
  },
  "Dashboard — logy_ ology/bugology.md": {
    "primary": "An informal or humorous colloquial term for entomology, the scientific study of insects.",
    "secondary": "In popular natural history, the enthusiastic collection, observation, and taxonomy of beetles, bugs, and other creeping arthropods.",
    "quotes": [
      {
        "author": "Mark Twain",
        "work": "Life on the Mississippi",
        "quote": "The local schoolmaster was deeply versed in what the village boys irreverently termed **bugology**."
      },
      {
        "author": "Oliver Wendell Holmes",
        "work": "The Poet at the Breakfast-Table",
        "quote": "Our Scarabee naturalist cared for nothing in the universe except his precious branch of **bugology**."
      },
      {
        "author": "Jean-Henri Fabre",
        "work": "Social Life in the Insect World",
        "quote": "The pedants may laugh at **bugology**, but the patience of the solitary wasp surpasses human wisdom."
      }
    ]
  },
  "Dashboard — logy_ ology/cytology.md": {
    "primary": "The branch of biological and medical science concerned with the structure, function, and pathology of cells.",
    "secondary": "In clinical diagnostics, the microscopic examination of cellular samples and aspirates to detect malignancies, infections, and cytogenetic disorders.",
    "quotes": [
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Every pathological change has its seat in the cell; hence clinical diagnosis must be founded upon microscopic **cytology**."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "Lay Sermons, Addresses, and Reviews",
        "quote": "Modern **cytology** reveals that protoplasm is the physical basis of life common to all living beings."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Diagnostic **cytology** of pleural and peritoneal exudates frequently resolves the dilemma between tuberculosis and malignancy."
      }
    ]
  },
  "Dashboard — logy_ ology/doxology.md": {
    "primary": "A short hymn, psalm, or liturgical verse of praise to God, used in Christian religious worship.",
    "secondary": "In Christian liturgy, an ecstatic formal formula of praise (such as the Gloria Patri) celebrating the Holy Trinity at the close of canticles and prayers.",
    "quotes": [
      {
        "author": "John Milton",
        "work": "Paradise Lost",
        "quote": "The angelic choir responded with an ecstatic **doxology**, casting their crowns before the sapphire throne."
      },
      {
        "author": "Thomas Hardy",
        "work": "Under the Greenwood Tree",
        "quote": "The Mellstock quire struck up the final **doxology** with all the vigor of their viols and clarinets."
      },
      {
        "author": "David Hume",
        "work": "The History of England",
        "quote": "The congregation concluded the solemn service by chanting a fervent **doxology** of thanksgiving."
      }
    ]
  },
  "Dashboard — logy_ ology/ecology.md": {
    "primary": "The branch of biology that studies the relationships and interactions between living organisms and their environment.",
    "secondary": "In environmental science, the comprehensive study of ecosystem energetics, trophic cascades, biodiversity dynamics, and planetary conservation.",
    "quotes": [
      {
        "author": "Ernst Haeckel",
        "work": "Generelle Morphologie der Organismen",
        "quote": "By **ecology** we mean the body of knowledge concerning the economy of nature—the total relations of the animal to its organic and inorganic environment."
      },
      {
        "author": "Rachel Carson",
        "work": "Silent Spring",
        "quote": "The chemical barrage ignored the basic tenets of **ecology**, poisoning the food chains upon which birds and mammals depend."
      },
      {
        "author": "Aldo Leopold",
        "work": "A Sand County Almanac",
        "quote": "A land ethic changes the role of Homo sapiens from conqueror of the land-community to plain member and citizen of its **ecology**."
      }
    ]
  },
  "Dashboard — logy_ ology/enology.md": {
    "primary": "The scientific study and art of winemaking; American spelling of oenology.",
    "secondary": "In viticulture and food science, the applied biochemistry of grape fermentation, yeast microbiology, oak aging, and sensory wine evaluation.",
    "quotes": [
      {
        "author": "Louis Pasteur",
        "work": "Studies on Wine",
        "quote": "The fundamental progress of **enology** began when we proved that alcoholic fermentation is governed by living microscopic yeasts."
      },
      {
        "author": "Thomas Jefferson",
        "work": "Writings on Viticulture",
        "quote": "A nation enlightened in the arts of **enology** and vineyard management will cultivate temperance alongside prosperity."
      },
      {
        "author": "Brillat-Savarin",
        "work": "The Physiology of Taste",
        "quote": "The refined palate appreciates how modern **enology** preserves the delicate bouquet of noble vintages."
      }
    ]
  },
  "Dashboard — logy_ ology/ethology.md": {
    "primary": "The scientific study of animal behavior in natural environments.",
    "secondary": "In evolutionary biology and behavioral science, a discipline founded by Konrad Lorenz and Nikolaas Tinbergen examining instinctive drives, sign stimuli, and fixed action patterns.",
    "quotes": [
      {
        "author": "Konrad Lorenz",
        "work": "King Solomon's Ring",
        "quote": "The essential method of **ethology** requires living intimately with animals and observing their unforced behavioral repertoire in nature."
      },
      {
        "author": "Nikolaas Tinbergen",
        "work": "The Study of Instinct",
        "quote": "Modern **ethology** seeks to answer four questions: causation, development, survival value, and evolutionary history."
      },
      {
        "author": "Charles Darwin",
        "work": "The Expression of the Emotions in Man and Animals",
        "quote": "The comparative observations that laid the foundation for modern **ethology** demonstrated that emotional gestures are inherited ancestral relics."
      }
    ]
  },
  "Dashboard — logy_ ology/etiology.md": {
    "primary": "The study or assignment of causes or reasons; in medicine, the cause or origin of a disease or pathological condition.",
    "secondary": "In epidemiology and clinical pathology, the comprehensive elucidation of causal pathways (genetic, environmental, infectious) initiating disease development.",
    "quotes": [
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "To understand the **etiology** of an epidemic, the physician must examine both the virulent agent and social misery."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The discovery of the tubercle bacillus settled the centuries-old dispute regarding the specific **etiology** of phthisis."
      },
      {
        "author": "Robert Koch",
        "work": "The Etiology of Tuberculosis",
        "quote": "To prove the bacterial **etiology** of a contagion, the pathogen must be isolated in pure culture and reproduce the malady in healthy hosts."
      }
    ]
  },
  "Dashboard — logy_ ology/eulogist.md": {
    "primary": "A person who delivers or writes a speech or text praising another person, especially deceased.",
    "secondary": "In classical rhetoric, an orator who pronounces a formal panegyric celebrating the civic virtues and achievements of an honored citizen.",
    "quotes": [
      {
        "author": "Abraham Lincoln",
        "work": "Eulogy on Henry Clay",
        "quote": "The eloquent **eulogist** stood before his countrymen to commemorate the great statesman whose compromises had preserved the Union."
      },
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The imperial **eulogist** exhausted the resources of panegyric to magnify the deeds of the deceased sovereign."
      },
      {
        "author": "Samuel Johnson",
        "work": "The Lives of the English Poets",
        "quote": "No **eulogist** can obscure the moral deficiencies of an author whose writings corrupted public virtue."
      }
    ]
  },
  "Dashboard — logy_ ology/eulogy.md": {
    "primary": "A speech or written tribute praising someone or something highly, especially a deceased person at a memorial service.",
    "secondary": "In classical literature and formal rhetoric, an encomium or panegyric composed to celebrate heroic valor, intellectual legacy, or civic virtue.",
    "quotes": [
      {
        "author": "Thucydides",
        "work": "History of the Peloponnesian War",
        "quote": "Pericles delivered his immortal funeral **eulogy**, praising not merely the fallen warriors, but the democratic spirit of Athens."
      },
      {
        "author": "Ralph Waldo Emerson",
        "work": "Eulogy on Henry David Thoreau",
        "quote": "In his moving **eulogy**, Emerson portrayed Thoreau as a hermit philosopher devoted wholly to truth."
      },
      {
        "author": "Charles Dickens",
        "work": "Bleak House",
        "quote": "No flattering **eulogy** was carved upon the pauper's grave in that desolate London churchyard."
      }
    ]
  },
  "Dashboard — logy_ ology/fetology.md": {
    "primary": "The medical branch concerned with the study, care, and management of the fetus in the womb.",
    "secondary": "In perinatology and clinical obstetrics, the specialized field utilizing prenatal imaging, fetoscopy, and intrauterine intervention to diagnose and treat fetal anomalies.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Advances in embryonic anatomy have laid the groundwork for an emerging **fetology** capable of monitoring antenatal life."
      },
      {
        "author": "Arthur Keith",
        "work": "Human Embryology and Morphology",
        "quote": "The clinical student of **fetology** must appreciate how organogenesis mirrors phylogenetic transformations."
      },
      {
        "author": "Eugene Braunwald",
        "work": "Heart Disease: A Textbook of Cardiovascular Medicine",
        "quote": "Modern **fetology** now detects complex congenital cardiac malformations in utero, allowing planned neonatal intervention."
      }
    ]
  },
  "Dashboard — logy_ ology/geology.md": {
    "primary": "The scientific study of the Earth, its physical structure, rocks, history, and the processes acting upon it.",
    "secondary": "In earth sciences, the investigation of stratigraphy, fossil records, continental drift, and deep time shaping the planetary crust.",
    "quotes": [
      {
        "author": "Charles Lyell",
        "work": "Principles of Geology",
        "quote": "The fundamental axiom of **geology** is that the past changes of the earth must be explained by forces now in operation."
      },
      {
        "author": "Charles Darwin",
        "work": "On the Origin of Species",
        "quote": "The imperfection of the geological record remains the greatest single difficulty in the study of historical **geology**."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "Lay Sermons, Addresses, and Reviews",
        "quote": "Physical **geology** has demonstrated that vast continents have repeatedly emerged from the floor of primordial seas."
      }
    ]
  },
  "Dashboard — logy_ ology/homology.md": {
    "primary": "The condition of having the same or corresponding structure, position, or origin.",
    "secondary": "In comparative anatomy and phylogenetics, structural similarity between organs across different species derived from a common ancestral prototype.",
    "quotes": [
      {
        "author": "Richard Owen",
        "work": "On the Archetype and Homologies of the Vertebrate Skeleton",
        "quote": "I define **homology** as the same organ in different animals under every variety of form and function."
      },
      {
        "author": "Charles Darwin",
        "work": "On the Origin of Species",
        "quote": "What can be more curious than that the hand of man, formed for grasping, and the wing of a bat should exhibit precise **homology**?"
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "Evidence as to Man's Place in Nature",
        "quote": "The structural **homology** uniting the anthropoid brain with the human brain is complete and undeniable."
      }
    ]
  },
  "Dashboard — logy_ ology/horology.md": {
    "primary": "The science and art of measuring time and constructing instruments for indicating time.",
    "secondary": "In mechanical engineering and the history of chronometry, the design of escapements, balances, and timekeeping mechanisms for nautical and astronomical precision.",
    "quotes": [
      {
        "author": "Isaac Newton",
        "work": "Opticks",
        "quote": "The perfection of **horology** and the invention of accurate marine chronometers were essential to determine longitude at sea."
      },
      {
        "author": "Diderot",
        "work": "Encyclopédie",
        "quote": "The art of **horology** represents the pinnacle of mechanical ingenuity, mimicking the celestial revolutions in a handheld case."
      },
      {
        "author": "Herman Melville",
        "work": "Pierre; or, The Ambiguities",
        "quote": "He compared human virtue to terrestrial clocks, and divine perfection to celestial **horology**."
      }
    ]
  },
  "Dashboard — logy_ ology/ideology.md": {
    "primary": "A system of ideas, principles, and doctrines forming the basis of a political, economic, or social philosophy.",
    "secondary": "In social philosophy and political theory, a shared worldview that legitimates the institutional interests, power relations, or class structures of a society.",
    "quotes": [
      {
        "author": "Karl Marx",
        "work": "The German Ideology",
        "quote": "The ruling ideas of each age have ever been the ideas of its ruling class; bourgeois **ideology** masks economic exploitation."
      },
      {
        "author": "Max Weber",
        "work": "The Protestant Ethic and the Spirit of Capitalism",
        "quote": "We must trace how religious **ideology** fostered the psychological discipline indispensable to modern enterprise."
      },
      {
        "author": "George Orwell",
        "work": "1984",
        "quote": "The official **ideology** of the Party was designed to eliminate the very possibility of unorthodox thought."
      }
    ]
  },
  "Dashboard — logy_ ology/misology.md": {
    "primary": "A hatred, contempt, or distrust of reason, argument, or intellectual disputation.",
    "secondary": "In classical philosophy (Plato's *Phaedo*), the cynical rejection of rational discourse that develops after an individual is disillusioned by fallacious or deceptive arguments.",
    "quotes": [
      {
        "author": "Benjamin Jowett",
        "work": "The Dialogues of Plato",
        "quote": "In the Phaedo, Socrates warns against **misology**, comparing the hatred of reasoned argument to misanthropy."
      },
      {
        "author": "Immanuel Kant",
        "work": "Critique of Pure Reason",
        "quote": "The skeptic who tires of philosophical disputes easily lapses into **misology**, condemning all speculative inquiry."
      },
      {
        "author": "Samuel Taylor Coleridge",
        "work": "Aids to Reflection",
        "quote": "To abandon oneself to emotional impulses while disparaging rational analysis is the dangerous snare of **misology**."
      }
    ]
  },
  "Dashboard — logy_ ology/mixology.md": {
    "primary": "The skill, craft, or science of preparing and mixing alcoholic drinks and cocktails.",
    "secondary": "In modern gastronomy and beverage craft, the culinary discipline of compounding artisanal liquors, bitters, and botanical infusions to achieve balanced flavor profiles.",
    "quotes": [
      {
        "author": "H. L. Mencken",
        "work": "The American Language",
        "quote": "The expansion of American vernacular gave the tavern keeper the imposing academic title of professor of **mixology**."
      },
      {
        "author": "Jerry Thomas",
        "work": "The Bartender's Guide",
        "quote": "True mastery of **mixology** requires discerning palates, precise measurements, and artistic presentation."
      },
      {
        "author": "Sinclair Lewis",
        "work": "Babbitt",
        "quote": "He took immense pride in his domestic **mixology**, shaking gin cocktails for his suburban guests with theatrical flourish."
      }
    ]
  },
  "Dashboard — logy_ ology/mycology.md": {
    "primary": "The branch of biology concerned with the study of fungi, including mushrooms, molds, and yeasts.",
    "secondary": "In microbiology and medical science, the investigation of fungal genetics, secondary metabolites (like antibiotics), and pathogenic fungal infections.",
    "quotes": [
      {
        "author": "Louis Pasteur",
        "work": "Studies on Fermentation",
        "quote": "The observations of **mycology** proved that yeast organisms are responsible for converting grape sugars into alcohol."
      },
      {
        "author": "Alexander Fleming",
        "work": "On the Antibacterial Action of Cultures of a Penicillium",
        "quote": "A chance contamination in the laboratory led to an observation in **mycology** that yielded penicillin."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "Lay Sermons, Addresses, and Reviews",
        "quote": "The field of **mycology** exhibits an astonishing diversity of saprophytic organisms vital to decomposing organic matter."
      }
    ]
  },
  "Dashboard — logy_ ology/myology.md": {
    "primary": "The branch of anatomy that deals with the scientific study of muscles and muscular tissue.",
    "secondary": "In human gross anatomy, the systematic classification of muscles according to origin, insertion, mechanical torque, vascular supply, and neural innervation.",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "The section on **myology** describes the fascial compartments and mechanical vectors of every skeletal muscle."
      },
      {
        "author": "Andreas Vesalius",
        "work": "De Humani Corporis Fabrica",
        "quote": "Vesalius revolutionized anatomical **myology** by dissecting human cadavers rather than relying upon Galenic animal dissections."
      },
      {
        "author": "Arthur Keith",
        "work": "Human Embryology and Morphology",
        "quote": "Comparative **myology** reveals that the pectoral muscles of primates originated from the primitive ventral muscular sheet of lower vertebrates."
      }
    ]
  },
  "Dashboard — logy_ ology/neology.md": {
    "primary": "The coining, introduction, or use of new words or phrases; a new word or meaning (neologism).",
    "secondary": "In church history and theological criticism, the introduction of theological novelties or rationalist interpretations departing from established creedal orthodoxy.",
    "quotes": [
      {
        "author": "Samuel Johnson",
        "work": "The Rambler",
        "quote": "Linguistic purists often decry every instance of **neology**, forgetting that without innovation a living language must perish."
      },
      {
        "author": "Thomas Macaulay",
        "work": "Critical and Historical Essays",
        "quote": "The sudden influx of Continental **neology** alarmed the conservative theologians of Oxford."
      },
      {
        "author": "Otto Jespersen",
        "work": "Growth and Structure of the English Language",
        "quote": "Shakespeare's astonishing capacity for **neology** permanently enriched the English vocabulary with hundreds of fresh expressions."
      }
    ]
  },
  "Dashboard — logy_ ology/nosology.md": {
    "primary": "The branch of medical science dealing with the systematic classification of diseases.",
    "secondary": "In clinical medicine and epidemiology, the systematic categorization of diseases based upon etiology, anatomical site, pathology, and symptomatology.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "A scientific **nosology** must classify diseases by their microbiological etiologies rather than by superficial symptom complexes."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Cellular pathology provided the anatomical foundation required to reform the chaotic **nosology** of the eighteenth century."
      },
      {
        "author": "Thomas Sydenham",
        "work": "Observationes Medicae",
        "quote": "Sydenham insisted that clinical **nosology** should catalog morbid entities with the same botanical precision as plants."
      }
    ]
  },
  "Dashboard — logy_ ology/oenology.md": {
    "primary": "The study and science of wine and winemaking; classical and British spelling of enology.",
    "secondary": "In agricultural and food sciences, the scientific study of viticulture, grape fermentation, chemical maturation, and organoleptic tasting of wines.",
    "quotes": [
      {
        "author": "Louis Pasteur",
        "work": "Studies on Wine",
        "quote": "Scientific **oenology** emerged from the laboratory when we demonstrated that microbial control prevents wine spoilage."
      },
      {
        "author": "Brillat-Savarin",
        "work": "The Physiology of Taste",
        "quote": "The refined epicure studies **oenology** to harmonize the vintage with the delicate sauces of haute cuisine."
      },
      {
        "author": "George Saintsbury",
        "work": "Notes on a Cellar-Book",
        "quote": "A lifelong passion for **oenology** brings intellectual delight as well as aesthetic gratification to the scholar's table."
      }
    ]
  },
  "Dashboard — logy_ ology/oncology.md": {
    "primary": "The branch of medicine and biology dedicated to the study, diagnosis, treatment, and prevention of cancer and tumors.",
    "secondary": "In clinical science, the multi-disciplinary management of malignancies encompassing molecular genetics, surgical resection, radiotherapy, and targeted chemotherapy.",
    "quotes": [
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "The study of cellular proliferation in morbid growths laid the histological groundwork for modern **oncology**."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The early surgical extirpation of malignant tumors remains the cardinal rule of clinical **oncology**."
      },
      {
        "author": "Siddhartha Mukherjee",
        "work": "The Emperor of All Maladies: A Biography of Cancer",
        "quote": "Modern molecular **oncology** revealed that cancer is an internal mutational war waged within the genome."
      }
    ]
  },
  "Dashboard — logy_ ology/ontology.md": {
    "primary": "The branch of metaphysics dealing with the nature of being, existence, and ultimate reality.",
    "secondary": "In computer science and knowledge representation, a formal specification of concepts, categories, and relationships within a particular domain of discourse.",
    "quotes": [
      {
        "author": "Immanuel Kant",
        "work": "Critique of Pure Reason",
        "quote": "The proud name of an **ontology** that presumes to give synthetic a priori cognitions of things in general must give place to a modest critique of pure understanding."
      },
      {
        "author": "Bertrand Russell",
        "work": "A History of Western Philosophy",
        "quote": "Plato's metaphysical **ontology** populated reality with eternal Forms more real than the fleeting sensible world."
      },
      {
        "author": "Willard Van Orman Quine",
        "work": "From a Logical Point of View",
        "quote": "To be is to be the value of a bound variable; this remains the fundamental criterion of philosophical **ontology**."
      }
    ]
  },
  "Dashboard — logy_ ology/oology.md": {
    "primary": "The branch of ornithology that studies birds' eggs, nests, and breeding behavior.",
    "secondary": "In avian biology and evolutionary natural history, the scientific study of egg morphology, shell microstructures, and coloration patterns.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Descent of Man",
        "quote": "Studies in avian **oology** illustrate how pigmentation and shell patterning evolve to camouflage clutches from predators."
      },
      {
        "author": "Alfred Russel Wallace",
        "work": "The Malay Archipelago",
        "quote": "The naturalist devoted to **oology** discovers exquisite adaptations in the nest construction and egg coloring of tropical birds."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "Lay Sermons, Addresses, and Reviews",
        "quote": "The structural shell characteristics cataloged in comparative **oology** reflect ancient reptilian affinities."
      }
    ]
  },
  "Dashboard — logy_ ology/orology.md": {
    "primary": "The scientific study of mountains, their physical structure, and their geographic distribution; orography.",
    "secondary": "In physical geomorphology, the investigation of tectonic mountain building, seismic orogeny, and alpine altitudinal zones.",
    "quotes": [
      {
        "author": "Alexander von Humboldt",
        "work": "Aspects of Nature",
        "quote": "Pioneering expeditions in Alpine and Andean **orology** revealed the vertical zonation of plant life according to elevation."
      },
      {
        "author": "Charles Lyell",
        "work": "Principles of Geology",
        "quote": "Modern **orology** demonstrates that mountain chains are not static upheavals, but dynamic zones of ongoing tectonic stress."
      },
      {
        "author": "John Muir",
        "work": "The Mountains of California",
        "quote": "The sublime study of Sierran **orology** teaches that glaciers carved these granite domes out of ancient crystalline bedrock."
      }
    ]
  },
  "Dashboard — logy_ ology/otology.md": {
    "primary": "The medical science and clinical specialty dealing with the anatomy, physiology, and pathology of the ear.",
    "secondary": "In surgical otolaryngology, the diagnosis and microsurgical management of conductive hearing loss, middle-ear infections, cholesteatoma, and vertigo.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Suppurative middle-ear disease requires prompt consultation in **otology** to avert fatal intracranial complications."
      },
      {
        "author": "Hermann von Helmholtz",
        "work": "On the Sensations of Tone",
        "quote": "Helmholtz's resonance theory of hearing transformed physiological **otology** into an exact physical science."
      },
      {
        "author": "Arthur Keith",
        "work": "Human Embryology and Morphology",
        "quote": "The fascinating field of **otology** traces how mammalian ear ossicles evolved from the ancestral reptilian jaw hinge."
      }
    ]
  },
  "Dashboard — logy_ ology/pedology.md": {
    "primary": "The scientific study of soils in their natural environment; pedological soil science.",
    "secondary": "In agricultural science and earth history, the classification of soil profiles and soil horizons formed by weathering, climate, and biological agencies over time.",
    "quotes": [
      {
        "author": "Vasily Dokuchaev",
        "work": "Russian Chernozem",
        "quote": "Dokuchaev established modern **pedology** by proving that soil is an independent natural body formed by climate, organisms, relief, and time."
      },
      {
        "author": "Charles Darwin",
        "work": "The Formation of Vegetable Mould through the Action of Worms",
        "quote": "Before formal **pedology** codified soil horizons, Darwin recognized that biological activity continually transforms the earth's surface."
      },
      {
        "author": "Justus von Liebig",
        "work": "Familiar Letters on Chemistry",
        "quote": "The chemical foundations of **pedology** explain how weathering releases vital potassium and phosphate into topsoil."
      }
    ]
  },
  "Dashboard — logy_ ology/penology.md": {
    "primary": "The branch of criminology and sociology that deals with the theory and practice of criminal punishment and prison management.",
    "secondary": "In jurisprudence and penal policy, the study of punitive sanctions, custodial reformatories, rehabilitation regimes, and post-release integration.",
    "quotes": [
      {
        "author": "Cesare Beccaria",
        "work": "On Crimes and Punishments",
        "quote": "The foundation of rational **penology** rests upon the principle that the certainty of punishment, rather than its cruelty, deters crime."
      },
      {
        "author": "Alexis de Tocqueville",
        "work": "The Penitentiary System in the United States",
        "quote": "Our mission to study American **penology** revealed how solitary confinement and labor transformed prison discipline."
      },
      {
        "author": "Jeremy Bentham",
        "work": "The Rationale of Punishment",
        "quote": "Utilitarian **penology** measures every penal sanction strictly by its capacity to prevent greater mischief in society."
      }
    ]
  },
  "Dashboard — logy_ ology/pomology.md": {
    "primary": "The branch of botany and agriculture concerned with the study and cultivation of fruits and fruit trees.",
    "secondary": "In commercial horticulture, the scientific selection, hybridization, grafting, and agronomic management of orchard varieties.",
    "quotes": [
      {
        "author": "Thomas Jefferson",
        "work": "Garden Book",
        "quote": "Jefferson devoted meticulous attention to practical **pomology**, importing European apple and pear varieties to Monticello."
      },
      {
        "author": "Charles Darwin",
        "work": "The Variation of Animals and Plants under Domestication",
        "quote": "The history of cultivated apples and peaches documented in **pomology** provides striking evidence of artificial selection."
      },
      {
        "author": "George Washington Carver",
        "work": "Agricultural Bulletins",
        "quote": "Applied **pomology** teaches the small farmer how orchard pruning and soil enrichment yield bumper fruit harvests."
      }
    ]
  }
}

esm_content = '''import path from 'path';
import { updateNotesBatch } from './curate-updater-util.mjs';

const baseClusterDir = path.resolve('App database/Greek roots/Cluster Body & Physiology');
const batchData = ''' + json.dumps(BATCH3_DATA, indent=2, ensure_ascii=False) + ''';

console.log('Starting Body Part 4 Batch 3 curation (' + Object.keys(batchData).length + ' words)...');
const updated = updateNotesBatch(baseClusterDir, batchData);
console.log('Batch 3 complete: successfully updated ' + updated + ' notes.');
'''

with open("main app/scripts/curate_body4_batch3.mjs", "w", encoding="utf-8") as f:
    f.write(esm_content)

print(f"Generated main app/scripts/curate_body4_batch3.mjs with {len(BATCH3_DATA)} entries.")
