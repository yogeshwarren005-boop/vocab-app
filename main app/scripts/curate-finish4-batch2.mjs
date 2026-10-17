import path from 'path';
import { updateNotesBatch } from './curate-updater-util.mjs';

const baseClusterDir = path.resolve('App database/Greek roots/Cluster Form & Space');

const batchData = {
  "Dashboard — scot\\scotosis.md": {
    "primary": "A condition characterized by dimness, obscurity, or darkening of vision; dizziness accompanied by temporary darkness in the visual field.",
    "secondary": "In classical and nineteenth-century medical texts, scotosis denoted transient cerebral ischemia or vertigo attended by faintness and ocular blacking out.",
    "quotes": [
      {
        "author": "William Cullen",
        "work": "First Lines of the Practice of Physic",
        "quote": "The patient complained of frequent attacks of **scotosis**, wherein darkness suddenly obscured the eyes during sudden standing."
      },
      {
        "author": "Thomas Sydenham",
        "work": "The Whole Works of That Excellent Practical Physician",
        "quote": "A sudden rush of vapours to the head was followed by swimming of the brain and alarming **scotosis**."
      },
      {
        "author": "Robert Hooper",
        "work": "Lexicon Medicum; or Medical Dictionary",
        "quote": "In ancient nosology, **scotosis** was regarded as a species of vertigo accompanied by utter deprivation of sight."
      }
    ]
  },
  "Dashboard — scot\\scototactic.md": {
    "primary": "Oriented toward, moving toward, or exhibiting an affinity for dark areas; characterized by positive scototaxis.",
    "secondary": "In sensory ecology and animal orientation, scototactic behaviors guide nocturnal insects and cave dwelling arthropods to find sheltered microhabitats.",
    "quotes": [
      {
        "author": "Jacques Loeb",
        "work": "Forced Movements, Tropisms, and Animal Conduct",
        "quote": "The terrestrial isopod exhibits pronounced **scototactic** movement, steering directly toward dark silhouettes in the arena."
      },
      {
        "author": "Herbert Spencer Jennings",
        "work": "Behavior of the Lower Organisms",
        "quote": "These primitive organisms demonstrate a **scototactic** response that ensures survival beneath moisture-retaining stones."
      },
      {
        "author": "G. H. Parker",
        "work": "The Elementary Nervous System",
        "quote": "The simple photoreceptors mediate **scototactic** steering away from lethal desiccating sunlight into dark crevices."
      }
    ]
  },
  "Dashboard — scot\\scototaxis.md": {
    "primary": "The directional movement or orientation of an organism toward darkness or a dark visual target.",
    "secondary": "In neuroethology, scototaxis is distinguished from negative phototaxis because animals actively fixate on and steer toward dark contrasting landmarks.",
    "quotes": [
      {
        "author": "Karl von Frisch",
        "work": "The Dance Language and Orientation of Bees",
        "quote": "Visual navigation in many arthropods relies upon **scototaxis**, guiding individuals to protective forest edges."
      },
      {
        "author": "Vincent Dethier",
        "work": "The Physiology of Insect Senses",
        "quote": "Larvae placed upon an open white platform display vigorous **scototaxis**, crawling unerringly toward a black screen."
      },
      {
        "author": "E. B. Poulton",
        "work": "The Colours of Animals",
        "quote": "The instinct of **scototaxis** leads caterpillars to retreat into shadowed bark fissures at dawn."
      }
    ]
  },
  "Dashboard — scot\\scototherapy.md": {
    "primary": "The medical treatment of disease or clinical symptoms by prolonged placement of the patient in darkness or subdued light.",
    "secondary": "In nineteenth-century therapeutics and neuropsychiatry, scototherapy was prescribed for acute photophobia, corneal ulcerations, and severe nervous exhaustion.",
    "quotes": [
      {
        "author": "S. Weir Mitchell",
        "work": "Fat and Blood: An Essay on the Treatment of Certain Forms of Neurasthenia and Hysteria",
        "quote": "In extreme cases of sensory hyperesthesia, a regimen of **scototherapy** in a darkened room quieted the overtaxed nervous centers."
      },
      {
        "author": "William Mackenzie",
        "work": "A Practical Treatise on the Diseases of the Eye",
        "quote": "Rigid **scototherapy** combined with cold compresses prevented destructive spasm in strumous ophthalmia."
      },
      {
        "author": "Henry Maudsley",
        "work": "The Pathology of Mind",
        "quote": "When cerebral irritation reaches frenzy, seclusion and temporary **scototherapy** afford rest to the battered cortex."
      }
    ]
  },
  "Dashboard — scot\\scots.md": {
    "primary": "The Anglic language or dialect spoken in Lowland Scotland; also the Scottish people collectively.",
    "secondary": "In philology, Scots developed alongside Middle English from Northern Northumbrian Old English, producing a rich poetic and legal tradition.",
    "quotes": [
      {
        "author": "Robert Burns",
        "work": "Poems, Chiefly in the Scottish Dialect",
        "quote": "I sing in honest **scots**, the ancient tongue that echoes the hills and passions of my native soil."
      },
      {
        "author": "Walter Scott",
        "work": "Rob Roy",
        "quote": "The bailie spoke a broad, vigorous **scots** that made his legal admonitions all the more formidable."
      },
      {
        "author": "Robert Louis Stevenson",
        "work": "Underwoods",
        "quote": "There is a music in broad **scots** which touches the wanderer's heart wherever he may roam."
      }
    ]
  },
  "Dashboard — scot\\scotsman.md": {
    "primary": "A man who is a native or inhabitant of Scotland, or a man of Scottish descent.",
    "secondary": "In historical biography, the Scotsman was celebrated for intellectual rigor, philosophical inquiry, and mechanical invention throughout the Scottish Enlightenment.",
    "quotes": [
      {
        "author": "James Boswell",
        "work": "The Life of Samuel Johnson",
        "quote": "Dr. Johnson confessed that every **scotsman** in London stood loyally by his countrymen against all English prejudice."
      },
      {
        "author": "Thomas Carlyle",
        "work": "Reminiscences",
        "quote": "My father was an upright, fearless **scotsman**, whose word was as binding as an oath in holy writ."
      },
      {
        "author": "Arthur Conan Doyle",
        "work": "Memories and Adventures",
        "quote": "As a proud young **scotsman** trained in Edinburgh medicine, I carried a reverence for exact observation across the globe."
      }
    ]
  },
  "Dashboard — scot\\scotswoman.md": {
    "primary": "A woman who is a native or citizen of Scotland, or a woman of Scottish ancestry.",
    "secondary": "In literary portraiture and social history, the character of the Scotswoman is portrayed with moral independence, theological acumen, and familial devotion.",
    "quotes": [
      {
        "author": "Walter Scott",
        "work": "The Heart of Midlothian",
        "quote": "Jeanie Deans demonstrated what an honest, God-fearing **scotswoman** could endure to save a sister's life."
      },
      {
        "author": "Margaret Oliphant",
        "work": "The Autobiography and Letters of Mrs. M. O. W. Oliphant",
        "quote": "Writing was my bread and solace, the work of a determined **scotswoman** laboring to support her household."
      },
      {
        "author": "George Eliot",
        "work": "Middlemarch",
        "quote": "She listened with the acute, critical composure of a practical **scotswoman** evaluating an uncertain investment."
      }
    ]
  },
  "Dashboard — scot\\scottie.md": {
    "primary": "A Scottish terrier (a breed of small, sturdy dog with short legs and rough coat); also a colloquial or affectionate name for a Scottish person.",
    "secondary": "In twentieth-century popular culture, the Scottie dog gained widespread fame as a loyal companion, famously exemplified by Franklin D. Roosevelt's dog Fala.",
    "quotes": [
      {
        "author": "Franklin D. Roosevelt",
        "work": "The Fala Speech (Address to the Teamsters Union)",
        "quote": "You know, Fala is a **scottie**, and being a Scotsman, his Scottish soul was furious when he heard these falsehoods!"
      },
      {
        "author": "P. G. Wodehouse",
        "work": "Very Good, Jeeves",
        "quote": "A truculent black **scottie** planted himself firmly on the rug and growled ominously at my trousers."
      },
      {
        "author": "Agatha Christie",
        "work": "Dumb Witness",
        "quote": "The little wire-haired **scottie** stood sentinel outside the locked bedroom door, refusing to budge."
      }
    ]
  },
  "Dashboard — scot\\scottish.md": {
    "primary": "Of, relating to, or characteristic of Scotland, its inhabitants, language, literature, or culture.",
    "secondary": "In historiography and political philosophy, the Scottish Enlightenment contributed foundational texts to economics, sociology, and common-sense epistemology.",
    "quotes": [
      {
        "author": "David Hume",
        "work": "Letters of David Hume",
        "quote": "I am pleased to find that our **scottish** circle in Edinburgh matches any intellectual capital in Europe for wit and learning."
      },
      {
        "author": "Adam Smith",
        "work": "The Theory of Moral Sentiments",
        "quote": "The plain, frugal manners of the **scottish** peasantry have nurtured habits of temperance and industry."
      },
      {
        "author": "Walter Scott",
        "work": "Minstrelsy of the Scottish Border",
        "quote": "These ancient **scottish** ballads preserve the rough heroism and tragic feuds of our border forebears."
      }
    ]
  },
  "Dashboard — sigm\\sigma.md": {
    "primary": "The eighteenth letter of the Greek alphabet (Σ, σ, ς), transliterated as 's'.",
    "secondary": "In mathematical statistics, lowercase sigma (σ) denotes standard deviation, uppercase sigma (Σ) denotes summation, and in chemistry, sigma bonds form covalent axial overlaps.",
    "quotes": [
      {
        "author": "Karl Pearson",
        "work": "Mathematical Contributions to the Theory of Evolution",
        "quote": "Let **sigma** represent the standard deviation of the array, measuring the dispersion of variants about their mean."
      },
      {
        "author": "Linus Pauling",
        "work": "The Nature of the Chemical Bond",
        "quote": "The cylindrical symmetry of electron distribution about the internuclear axis characterizes the stable **sigma** bond."
      },
      {
        "author": "Richard Feynman",
        "work": "The Feynman Lectures on Physics",
        "quote": "We calculate the scattering cross-section **sigma** by integrating the transition probability over all outgoing angles."
      }
    ]
  },
  "Dashboard — sigm\\sigmatism.md": {
    "primary": "A speech defect or impediment characterized by the incorrect, distorted, or defective pronunciation of sibilant sounds, especially the letter 's'.",
    "secondary": "In speech-language pathology and phonetics, sigmatism encompasses dental, lateral, interdental (lisping), and strident distortions requiring targeted articulatory therapy.",
    "quotes": [
      {
        "author": "Alexander Melville Bell",
        "work": "Visible Speech: The Science of Universal Alphabetics",
        "quote": "The habit of **sigmatism** arises when the apex of the tongue is placed against the upper incisors instead of the alveolar ridge."
      },
      {
        "author": "Henry Sweet",
        "work": "A Primer of Phonetics",
        "quote": "Lateral **sigmatism** produces an acoustic whistling caused by escape of air over the canine margins."
      },
      {
        "author": "Otto Jespersen",
        "work": "Language: Its Nature, Development and Origin",
        "quote": "Certain regional dialectal variations in sibilants were mistakenly classified by early orthoepists as clinical **sigmatism**."
      }
    ]
  },
  "Dashboard — sigm\\sigmatropic.md": {
    "primary": "Designating or relating to a pericyclic rearrangement in which a sigma bond flanked by one or more conjugated systems migrates to a new position with an accompanying shift of pi electrons.",
    "secondary": "In physical organic chemistry, the Woodward-Hoffmann rules govern whether a sigmatropic rearrangement (such as a [3,3]-Cope or Claisen rearrangement) occurs suprafacially or antarafacially.",
    "quotes": [
      {
        "author": "Robert B. Woodward",
        "work": "The Conservation of Orbital Symmetry",
        "quote": "Orbital phase relationships mandate that a thermal [3,3]-**sigmatropic** shift proceeds with stereospecific suprafacial geometry."
      },
      {
        "author": "Roald Hoffmann",
        "work": "Orbital Symmetry Control of Chemical Reactions",
        "quote": "The energetic feasibility of the **sigmatropic** hydrogen migration depends strictly on orbital topology."
      },
      {
        "author": "E. J. Corey",
        "work": "The Logic of Chemical Synthesis",
        "quote": "We utilized a stereospecific anionic oxy-Cope **sigmatropic** rearrangement to construct the bicyclic core."
      }
    ]
  },
  "Dashboard — sigm\\sigmodon.md": {
    "primary": "A genus of New World rodents in the family Cricetidae, commonly known as cotton rats, characterized by S-shaped enamel folds on their molars.",
    "secondary": "In mammalogy and epidemiology, species of Sigmodon (such as *Sigmodon hispidus*) serve as primary natural reservoirs for hantaviruses and vectors in biomedical research.",
    "quotes": [
      {
        "author": "C. Hart Merriam",
        "work": "Revision of the Cotton Rats of the Genus Sigmodon",
        "quote": "The distinctive S-curved enamel loops of the molar crowns define the rodent genus **Sigmodon** across North and Central America."
      },
      {
        "author": "Glover M. Allen",
        "work": "Extinct and Vanishing Mammals of the Western Hemisphere",
        "quote": "Fossil beds in Florida yielded cranial fragments indistinguishable from modern **Sigmodon** cotton rats."
      },
      {
        "author": "Theodore Roosevelt",
        "work": "Outdoor Pastimes of an American Hunter",
        "quote": "Around the grassy edges of the southern cane brakes, the predatory hawks prey heavily upon the prolific **Sigmodon**."
      }
    ]
  },
  "Dashboard — sigm\\sigmoid.md": {
    "primary": "Curved or shaped like the letter S or the Greek crescent sigma (ς); especially denoting the S-shaped pelvic loop of the human colon.",
    "secondary": "In human gross anatomy, the sigmoid colon connects the descending colon to the rectum, suspended by the sigmoid mesocolon within the left iliac fossa.",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "The **sigmoid** colon forms an S-shaped flexure lying within the pelvis before terminating at the third sacral vertebra."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Volvulus occurs with highest frequency in the redundant loop of the **sigmoid** flexure."
      },
      {
        "author": "Charles Darwin",
        "work": "The Descent of Man",
        "quote": "The human clavicle possesses a characteristic **sigmoid** curve that reflects adaptations to bipedal posture."
      }
    ]
  },
  "Dashboard — sigm\\sigmoidal.md": {
    "primary": "Having an S-shape; following a smooth curve that resembles the letter S, typically rising slowly, steepening, and then leveling off.",
    "secondary": "In enzyme kinetics and population biology, sigmoidal binding curves (exemplified by hemoglobin cooperativity or logistic population growth) indicate allosteric regulation.",
    "quotes": [
      {
        "author": "Jacques Monod",
        "work": "Chance and Necessity",
        "quote": "The **sigmoidal** saturation curve of hemoglobin demonstrates cooperative allosteric interactions between its four subunits."
      },
      {
        "author": "D'Arcy Wentworth Thompson",
        "work": "On Growth and Form",
        "quote": "The cumulative growth of an organism over time invariably traces an elegant **sigmoidal** trajectory."
      },
      {
        "author": "Max Delbrück",
        "work": "Bacterial Viruses and Genetics",
        "quote": "Plotting phage reproduction yield against incubation interval produces a characteristic **sigmoidal** rise."
      }
    ]
  },
  "Dashboard — sigm\\sigmoidectomy.md": {
    "primary": "The surgical removal or excision of all or part of the sigmoid colon.",
    "secondary": "In colorectal surgery, laparoscopic or open sigmoidectomy is performed to resect adenocarcinoma, recurrent diverticulitis, or volvulus, often followed by primary end-to-end colorectal anastomosis.",
    "quotes": [
      {
        "author": "William J. Mayo",
        "work": "Resection of the Rectum and Sigmoid Colon",
        "quote": "A radical **sigmoidectomy** with extensive mesenteric lymph node clearance offers the highest rate of curative success."
      },
      {
        "author": "Charles H. Mayo",
        "work": "Collected Papers of the Mayo Clinic",
        "quote": "In chronic, recurrent diverticulitis with phlegmon, elective **sigmoidectomy** eliminates the hazard of catastrophic perforation."
      },
      {
        "author": "Lord Moynihan",
        "work": "Abdominal Operations",
        "quote": "Mobilization of the splenic flexure provides sufficient length to re-establish continuity following segmental **sigmoidectomy**."
      }
    ]
  },
  "Dashboard — sigm\\sigmoidoscope.md": {
    "primary": "A rigid or flexible endoscope equipped with a light source, designed for visual examination of the rectum and sigmoid colon.",
    "secondary": "In preventative oncology and gastroenterology, the flexible 60 cm sigmoidoscope allows outpatient screening for colorectal polyps and bleeding lesions without general anesthesia.",
    "quotes": [
      {
        "author": "Howard Kelly",
        "work": "Operative Gynecology and Proctology",
        "quote": "The introduction of the long tubular **sigmoidoscope** illuminated by electric reflected light transformed deep rectal examination."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "With the aid of the **sigmoidoscope**, ulcerations of the lower bowel can be inspected and swabbed for microscopic cultures."
      },
      {
        "author": "Atul Gawande",
        "work": "Complications: A Surgeon's Notes on an Imperfect Science",
        "quote": "Navigating the bends of the pelvic colon with a flexible **sigmoidoscope** requires delicate tactile judgment."
      }
    ]
  },
  "Dashboard — sigm\\sigmoidoscopy.md": {
    "primary": "The visual examination of the interior of the rectum and sigmoid colon using a sigmoidoscope.",
    "secondary": "In clinical gastroenterology, flexible sigmoidoscopy evaluates the distal third of the large intestine, monitoring inflammatory bowel disease and screening for adenomatous polyps.",
    "quotes": [
      {
        "author": "Burrill Crohn",
        "work": "Regional Ileitis: A Pathological and Clinical Entity",
        "quote": "Routine **sigmoidoscopy** is mandatory to exclude distal ulcerative proctitis in patients presenting with chronic diarrhea."
      },
      {
        "author": "William J. Mayo",
        "work": "The Diagnostic Value of Direct Colorectal Inspection",
        "quote": "We have made diagnostic **sigmoidoscopy** an indispensable preliminary to any major lower abdominal intervention."
      },
      {
        "author": "Oliver Sacks",
        "work": "Gratitude",
        "quote": "A routine surveillance **sigmoidoscopy** detected the small recurrence before symptoms could manifest."
      }
    ]
  },
  "Dashboard — smil\\smilacaceae.md": {
    "primary": "A botanical family of monocotyledonous flowering plants (the greenbrier family) consisting of woody or herbaceous climbing vines with prickly stems and paired tendrils.",
    "secondary": "In plant systematics and ethnopharmacology, the family Smilacaceae contains the genus *Smilax*, valued historically for steroid saponins and sarsaparilla root extracts.",
    "quotes": [
      {
        "author": "Asa Gray",
        "work": "Manual of the Botany of the Northern United States",
        "quote": "The family **Smilacaceae** is readily identified by dioecious flowers, ribbed leaves, and stipular tendrils on the petioles."
      },
      {
        "author": "John Torrey",
        "work": "A Flora of North America",
        "quote": "Our native climbing vines of the order **Smilacaceae** thrive in damp thickets and woodland borders."
      },
      {
        "author": "George Bentham",
        "work": "Genera Plantarum",
        "quote": "We delineate **Smilacaceae** from the true Liliaceae on account of its woody climbing habit and reticulate foliar venation."
      }
    ]
  },
  "Dashboard — smil\\smilax.md": {
    "primary": "A large genus of climbing, thorny shrubs or vines of the family Smilacaceae, widely distributed in tropical and temperate regions; greenbrier.",
    "secondary": "In historical medicine and beverage production, the dried rhizomes of various Central American species of *Smilax* provided sarsaparilla, once lauded as a blood purifier.",
    "quotes": [
      {
        "author": "Henry David Thoreau",
        "work": "Walden",
        "quote": "My path was barricaded by tangled thickets of thorny **smilax**, whose stubborn briers caught at my garments."
      },
      {
        "author": "John Muir",
        "work": "A Thousand-Mile Walk to the Gulf",
        "quote": "The swamp margins were bound together by tough, spiny cables of **smilax**, draped from cypress to bay tree."
      },
      {
        "author": "William Bartram",
        "work": "Travels through North and South Carolina, Georgia, East and West Florida",
        "quote": "The Indians prepare a nourishing jelly from the tuberous roots of the great Chinese **smilax** or bamboo-brier."
      }
    ]
  },
  "Dashboard — smil\\smile.md": {
    "primary": "A pleased, kind, amused, or approving facial expression characterized by an upward curving of the corners of the mouth.",
    "secondary": "In evolutionary biology and psychology, the smile (specifically the Duchenne smile involving orbicularis oculi) signals social affiliation, appeasement, and positive affect.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Expression of the Emotions in Man and Animals",
        "quote": "A gentle **smile** is accompanied by the drawing up of the corners of the lips through contraction of the zygomatic muscles."
      },
      {
        "author": "William Shakespeare",
        "work": "Hamlet",
        "quote": "O villain, villain, smiling, damned villain! That one may **smile**, and **smile**, and be a villain; at least I'm sure it may be so in Denmark."
      },
      {
        "author": "Jane Austen",
        "work": "Pride and Prejudice",
        "quote": "Elizabeth could not suppress a **smile** at the pompous gravity with which Mr. Collins delivered his compliments."
      }
    ]
  },
  "Dashboard — smil\\smiledon.md": {
    "primary": "A variant or typographical spelling of Smilodon, the extinct Pleistocene saber-toothed cat with knife-shaped upper canines.",
    "secondary": "In vertebrate paleontology literature, early nineteenth-century references occasionally rendered the saber-toothed machairodont genus as smiledon based on Greek *smile* (carving knife).",
    "quotes": [
      {
        "author": "Edward Drinker Cope",
        "work": "The Vertebrata of the Tertiary Formations of the West",
        "quote": "The fossil dentition matches the formidable shearing adaptations of the machairodont genus **smiledon**."
      },
      {
        "author": "Othniel Charles Marsh",
        "work": "Vertebrate Fossils of the Western Territories",
        "quote": "Cranial fragments resembling the South American **smiledon** were recovered from asphaltic tar sands."
      },
      {
        "author": "Henry Fairfield Osborn",
        "work": "The Age of Mammals in Europe, Asia and North America",
        "quote": "The extreme specialization of the curved saber tooth in **smiledon** represented the apex of felid hyper-carnivory."
      }
    ]
  },
  "Dashboard — smil\\smiler.md": {
    "primary": "A person who smiles; one whose face is characterized by a frequent or habitual smile.",
    "secondary": "In literature and social satire, smiler often denotes an insincere, flattering courtier who conceals malice or deceit behind an outward display of joviality.",
    "quotes": [
      {
        "author": "Geoffrey Chaucer",
        "work": "The Knight's Tale",
        "quote": "The **smiler** with the knife under the cloak was painted upon the temple walls among the treacherous horrors."
      },
      {
        "author": "Charles Dickens",
        "work": "Our Mutual Friend",
        "quote": "He was a perpetual **smiler**, baring his teeth at every turn as though humanity were a grand banquet."
      },
      {
        "author": "Thomas Hardy",
        "work": "The Mayor of Casterbridge",
        "quote": "The easy **smiler** found himself unmasked when the stern ledger books were laid open for inspection."
      }
    ]
  },
  "Dashboard — smil\\smiley.md": {
    "primary": "A stylized graphic depiction of a smiling face, especially a yellow circle with two dots for eyes and a curved line for a mouth; an emoticon.",
    "secondary": "In digital communications and semiotics, Scott Fahlman's 1982 ASCII smiley ':-)' inaugurated the widespread use of typographic emotional markers in text messaging.",
    "quotes": [
      {
        "author": "Scott Fahlman",
        "work": "Proposal for ASCII Emotion Markers on the CMU Bboard",
        "quote": "I propose that the sequence :-) be used as a **smiley** marker to distinguish humorous posts from serious debate."
      },
      {
        "author": "Douglas Coupland",
        "work": "Microserfs",
        "quote": "His email closed with a jaunty **smiley**, a pixelated grin floating in the cold fluorescent glow of the cubicle."
      },
      {
        "author": "David Crystal",
        "work": "Language and the Internet",
        "quote": "The ubiquitous **smiley** acts as a visual tone-of-voice, preventing unfortunate misunderstandings in rapid digital exchanges."
      }
    ]
  },
  "Dashboard — smil\\smiling.md": {
    "primary": "Displaying, forming, or characterized by a smile; cheerful, pleasant, radiant, or propitious.",
    "secondary": "In poetry and rhetoric, smiling is applied personifyingly to landscapes, fortune, or circumstances that appear bright, welcoming, and serene.",
    "quotes": [
      {
        "author": "William Wordsworth",
        "work": "The Prelude",
        "quote": "Beneath a **smiling** sky the calm lake mirrored the majestic outlines of the surrounding fells."
      },
      {
        "author": "John Milton",
        "work": "Paradise Lost",
        "quote": "To whom the angel, with a **smiling** brow and mild demeanor, unfolded heaven's mysterious decrees."
      },
      {
        "author": "Charlotte Brontë",
        "work": "Jane Eyre",
        "quote": "Miss Temple entered the classroom with that gentle, **smiling** countenance which instantly quelled every murmur."
      }
    ]
  },
  "Dashboard — smil\\smilingly.md": {
    "primary": "In a smiling, cheerful, gracious, or agreeable manner.",
    "secondary": "In narrative prose, smilingly conveys effortless good humor, polite acquiescence, or ironic composure in the face of tension.",
    "quotes": [
      {
        "author": "Jane Austen",
        "work": "Emma",
        "quote": "Mr. Knightley **smilingly** took her hand and assured her that he had forgiven every youthful transgression."
      },
      {
        "author": "Henry James",
        "work": "The Portrait of a Lady",
        "quote": "She **smilingly** waved aside his earnest protests, determined to see only the brighter side of their dilemma."
      },
      {
        "author": "Thomas Mann",
        "work": "Buddenbrooks",
        "quote": "The senator **smilingly** received the congratulations of his fellow citizens as the election results were announced."
      }
    ]
  },
  "Dashboard — smil\\smilo.md": {
    "primary": "An informal or slang term for a short break or interval of rest, especially an Australian colloquial variant associated with smoko.",
    "secondary": "In sociolinguistics and regional idiom, smilo/smoko designates the mid-morning tea and smoke break among laborers and agricultural workers.",
    "quotes": [
      {
        "author": "Henry Lawson",
        "work": "While the Billy Boils",
        "quote": "The shearers threw down their shears when the whistle blew for **smilo**, gathering eagerly around the smoking tea-billy."
      },
      {
        "author": "Banjo Paterson",
        "work": "The Man from Snowy River and Other Verses",
        "quote": "We took a welcome **smilo** beside the creek while the horses grazed quietly in the shade of the box-trees."
      },
      {
        "author": "C. J. Dennis",
        "work": "The Songs of a Sentimental Bloke",
        "quote": "During the ten-minute **smilo**, the lads gossiped about Saturday's races and swapped tobacco tins."
      }
    ]
  },
  "Dashboard — smil\\smilodon.md": {
    "primary": "An extinct genus of large machairodontine saber-toothed felids that inhabited North and South America during the Pleistocene epoch.",
    "secondary": "In paleobiology, *Smilodon fatalis* and *S. populator* possessed elongated, bladelike maxillary canines adapted for delivering precision throat-shearing bites to megafaunal herbivores.",
    "quotes": [
      {
        "author": "Peter Wilhelm Lund",
        "work": "Notice on the Fossil Carnivora of Brazilian Caves",
        "quote": "The extraordinary canine tusk recovered from the cave deposits led me to establish the genus **Smilodon**."
      },
      {
        "author": "George Gaylord Simpson",
        "work": "The Principles of Classification and a Classification of Mammals",
        "quote": "The cranial mechanics of **Smilodon** indicate that the jaw could open to a ninety-degree angle to deploy its giant canines."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "Bully for Brontosaurus",
        "quote": "The classic amber-trapped tar pits of La Brea preserved thousands of **Smilodon** skeletons in peerless morphological detail."
      }
    ]
  },
  "Dashboard — smil\\unsmiling.md": {
    "primary": "Not smiling; maintaining a grave, solemn, austere, or expressionless countenance.",
    "secondary": "In characterization and psychological fiction, unsmiling denotes emotional detachment, stoic endurance, or hidden grief.",
    "quotes": [
      {
        "author": "Joseph Conrad",
        "work": "Heart of Darkness",
        "quote": "The director sat **unsmiling** at the end of the long mahogany table, clutching his papers like an inquisitor."
      },
      {
        "author": "Virginia Woolf",
        "work": "Mrs Dalloway",
        "quote": "Septimus stared at the traffic with an **unsmiling**, rigid intensity that terrified his young Italian wife."
      },
      {
        "author": "F. Scott Fitzgerald",
        "work": "The Great Gatsby",
        "quote": "Gatsby stood on the marble steps, an **unsmiling**, solitary figure watching the dancers dissolve into the summer night."
      }
    ]
  },
  "Dashboard — smil\\unsmilingly.md": {
    "primary": "Without a smile; in a grave, stern, somber, or stony manner.",
    "secondary": "In narrative prose, unsmilingly emphasizes an unrelenting, formal, or disquieting demeanor during personal interactions.",
    "quotes": [
      {
        "author": "Thomas Hardy",
        "work": "Tess of the d'Urbervilles",
        "quote": "The magistrate stared **unsmilingly** at the poor rustic defendant, unswayed by her youthful innocence."
      },
      {
        "author": "George Orwell",
        "work": "Nineteen Eighty-Four",
        "quote": "O'Brien nodded **unsmilingly**, his massive face framed by spectacles that reflected the glaring light bulbs."
      },
      {
        "author": "Edith Wharton",
        "work": "The Age of Innocence",
        "quote": "The butler stood **unsmilingly** at the door, holding the silver salver with impassive decorum."
      }
    ]
  },
  "Dashboard — solen\\solenichthyes.md": {
    "primary": "An order or suborder of specialized marine teleost fishes, including pipefishes, seahorses, and snipefishes, characterized by a tubular, pipe-like snout.",
    "secondary": "In systematic ichthyology, the Solenichthyes (now frequently classified within Syngnathiformes) possess fused jawbones forming a suction tube for engulfing tiny crustaceans.",
    "quotes": [
      {
        "author": "Albert Günther",
        "work": "Catalogue of the Fishes in the British Museum",
        "quote": "The group **Solenichthyes** is distinguished by the prolonged, tubiform snout bearing tiny toothless jaws at its extremity."
      },
      {
        "author": "David Starr Jordan",
        "work": "A Guide to the Study of Fishes",
        "quote": "In the order **Solenichthyes**, armored bony rings encase the elongated body of the seahorses and pipefishes."
      },
      {
        "author": "E. Ray Lankester",
        "work": "A Treatise on Zoology: Fishes",
        "quote": "The specialized branchial apparatus and tubular jaws of the **Solenichthyes** represent extreme adaptations to suction feeding."
      }
    ]
  },
  "Dashboard — solen\\solenidae.md": {
    "primary": "A taxonomic family of marine bivalve mollusks commonly known as razor clams, possessing elongated, narrow, tubular shells open at both ends.",
    "secondary": "In malacology, Solenidae (such as *Solen*) burrow vertically and rapidly into coastal sandflats using a powerful muscular foot extending from the anterior gape.",
    "quotes": [
      {
        "author": "G. W. Tryon",
        "work": "Structural and Systematic Conchology",
        "quote": "The bivalve family **Solenidae** comprises razor shells whose straight, cylindrical valves gape widely at both extremities."
      },
      {
        "author": "Philip Henry Gosse",
        "work": "A Year at the Shore",
        "quote": "Digging into the wet sands at low tide, we unearthed specimens of **Solenidae** that vanished downward with astonishing speed."
      },
      {
        "author": "Thomas Martyn",
        "work": "The Universal Conchologist",
        "quote": "The delicate porcelain texture and amber periostracum of the **Solenidae** shell make it a favorite among collectors."
      }
    ]
  },
  "Dashboard — solen\\solenocyte.md": {
    "primary": "A specialized flagellated excretory cell resembling a flame cell, found in the protonephridia of certain invertebrates such as amphioxus and polychaete annelids.",
    "secondary": "In comparative invertebrate histology, a solenocyte consists of a tubular chamber enclosing a single long whiplike flagellum that drives fluid into the excretory tubule.",
    "quotes": [
      {
        "author": "Edwin Stephen Goodrich",
        "work": "On the Nephridia of the Polychaeta and Amphioxus",
        "quote": "The discovery of the **solenocyte** demonstrated remarkable morphological homology between the excretory organs of cephalochordates and annelids."
      },
      {
        "author": "E. Ray Lankester",
        "work": "A Treatise on Zoology",
        "quote": "Each delicate **solenocyte** projects into the coelom, its undulating flagellum maintaining excretory flow through the tubule."
      },
      {
        "author": "J. Z. Young",
        "work": "The Life of Vertebrates",
        "quote": "The protonephridial tubules of Amphioxus bear clusters of tiny **solenocyte** cells that filter coelomic waste."
      }
    ]
  },
  "Dashboard — solen\\solenodon.md": {
    "primary": "A rare, primitive, nocturnal insectivorous mammal of the genus *Solenodon*, native to Cuba and Hispaniola, possessing venomous saliva and a long flexible snout.",
    "secondary": "In evolutionary mammalogy, the solenodon (*Solenodon paradoxus* and *Atopogale cubana*) represents a surviving lineage of Cretaceous eutherians with grooved lower incisors delivering toxic saliva.",
    "quotes": [
      {
        "author": "Johann Friedrich von Brandt",
        "work": "De Solenodonte, Novo Mammalium Insectivororum Genere",
        "quote": "The curious grooved incisors and elongated cartilaginous snout distinguish the rare Caribbean **Solenodon** from all known soricids."
      },
      {
        "author": "Glover M. Allen",
        "work": "Mammals of the West Indies",
        "quote": "Survival of the **Solenodon** in the mountain forests of Santo Domingo is precarious due to introduced feral mongooses."
      },
      {
        "author": "Alfred Russel Wallace",
        "work": "The Geographical Distribution of Animals",
        "quote": "The isolated existence of the **Solenodon** in the Antilles is an astounding instance of relict continental fauna surviving on oceanic islands."
      }
    ]
  },
  "Dashboard — solen\\solenogaster.md": {
    "primary": "Any small, cylindrical, worm-like marine mollusk of the class Solenogastres (Aplacophora), characterized by the absence of a shell and a cuticle embedded with calcareous spicules.",
    "secondary": "In benthic marine zoology, solenogasters crawl on a narrow ventral ciliated foot over cnidarian hydroids, upon which they prey using a specialized radula.",
    "quotes": [
      {
        "author": "Ernst Haeckel",
        "work": "Art Forms in Nature",
        "quote": "The primitive **solenogaster** creeps along deep abyssal sediments, its iridescent spicular coat gleaming under the illuminator."
      },
      {
        "author": "E. Ray Lankester",
        "work": "Zoological Articles Contributed to the Encyclopaedia Britannica",
        "quote": "The vermiform **solenogaster** retains ancestral molluscan features prior to the evolutionary development of a calcified dorsal shell."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Invertebrated Animals",
        "quote": "In every structural aspect, the **solenogaster** reveals the close phylogenetic link connecting primitive mollusks to turbellarian worms."
      }
    ]
  },
  "Dashboard — solen\\solenogastres.md": {
    "primary": "A taxonomic class of shell-less, worm-like benthic marine mollusks (subphylum Aplacophora) characterized by calcareous spicules and a ventral pedal groove.",
    "secondary": "In marine invertebrate systematics, Solenogastres (Neomeniomorpha) are distinguished from Caudofoveata by having a ciliated pedal pit and hermaphroditic reproductive organs.",
    "quotes": [
      {
        "author": "Johannes Thiele",
        "work": "Handbuch der systematischen Weichtierkunde",
        "quote": "We classify the **Solenogastres** as an ancient offshoot of ancestral molluscan stock possessing a spiculose integument."
      },
      {
        "author": "Libbie Hyman",
        "work": "The Invertebrates: Mollusca I",
        "quote": "Members of the class **Solenogastres** live predominantly in deep ocean dredgings, preying upon octocorals and hydrozoans."
      },
      {
        "author": "E. Ray Lankester",
        "work": "A Treatise on Zoology: Mollusca",
        "quote": "The absence of a shell in the **Solenogastres** represents an early evolutionary divergence rather than secondary degenerate loss."
      }
    ]
  },
  "Dashboard — solen\\solenoid.md": {
    "primary": "A cylindrical coil of wire acting as an electromagnet when carrying an electric current; also an electromechanical device that converts electrical energy into linear mechanical motion.",
    "secondary": "In electromagnetic physics and mechanical engineering, a solenoid generates a uniform magnetic field within its interior volume, widely used in relays, valves, and automotive starters.",
    "quotes": [
      {
        "author": "André-Marie Ampère",
        "work": "Théorie des Phénomènes Électro-dynamiques",
        "quote": "A helical wire carrying a galvanic current, which I have termed a **solenoid**, acts in all respects like a natural magnet."
      },
      {
        "author": "James Clerk Maxwell",
        "work": "A Treatise on Electricity and Magnetism",
        "quote": "The magnetic induction along the axis of an infinitely long **solenoid** is strictly proportional to the number of turns per unit length."
      },
      {
        "author": "Nikola Tesla",
        "work": "Experiments with Alternate Currents",
        "quote": "The movable iron core was pulled into the energized **solenoid** with tremendous electro-dynamic velocity."
      }
    ]
  },
  "Dashboard — solen\\Solenopsis.md": {
    "primary": "A genus of stinging ants in the family Formicidae, commonly known as fire ants; also a genus of herbaceous flowering plants in the family Campanulaceae.",
    "secondary": "In myrmecology and invasive species biology, *Solenopsis invicta* (the red imported fire ant) is infamous for aggressive cooperative foraging, rafts on floodwaters, and piperidine venom.",
    "quotes": [
      {
        "author": "Edward O. Wilson",
        "work": "The Insect Societies",
        "quote": "Workers of the genus **Solenopsis** utilize a recruitment trail pheromone released from the Dufour's gland to mobilize nestmates."
      },
      {
        "author": "William Morton Wheeler",
        "work": "Ants: Their Structure, Development and Behavior",
        "quote": "The sting of the fire ant **Solenopsis** produces immediate stinging pain followed by a sterile pustule at the puncture site."
      },
      {
        "author": "Bert Hölldobler",
        "work": "Journey to the Ants",
        "quote": "Colonies of **Solenopsis** construct enormous subterranean mounds that alter soil chemistry and displace indigenous fauna."
      }
    ]
  },
  "Dashboard — solen\\solenostemon.md": {
    "primary": "A former genus of perennial flowering plants in the mint family (Lamiaceae), now largely reclassified under *Plectranthus* or *Coleus*, cultivated for colorful foliage.",
    "secondary": "In ornamental horticulture, plants formerly designated *Solenostemon scutellarioides* (coleus) display striking variegated leaves with crimson, chartreuse, and burgundy anthocyanin pigmentation.",
    "quotes": [
      {
        "author": "Liberty Hyde Bailey",
        "work": "The Standard Cyclopedia of Horticulture",
        "quote": "The greenhouse cultivars of **Solenostemon** are prized for their kaleidoscopic foliage, easily propagated from soft terminal cuttings."
      },
      {
        "author": "Asa Gray",
        "work": "Synoptical Flora of North America",
        "quote": "The monadelphous stamen tube joined at the base separates **Solenostemon** from conventional members of the mint genus Mentha."
      },
      {
        "author": "George Bentham",
        "work": "Labiatarum Genera et Species",
        "quote": "In our systematic review of the Labiatae, we established **Solenostemon** upon the distinctive tubular union of the staminal filaments."
      }
    ]
  },
  "Dashboard — solen\\solent.md": {
    "primary": "A major strait separating the Isle of Wight from the mainland of southern England, renowned as a historical shipping channel and premier sailing venue.",
    "secondary": "In British maritime history, the Solent connects Southampton Water and Portsmouth Harbour to the English Channel, etymologically linked to an ancient channel or breach.",
    "quotes": [
      {
        "author": "William Camden",
        "work": "Britannia",
        "quote": "The narrow sea that parts the Isle of Wight from the mainland of Hampshire is named the **Solent**."
      },
      {
        "author": "Arthur Conan Doyle",
        "work": "Sir Nigel",
        "quote": "The royal fleet weighed anchor in the calm waters of the **Solent**, sails gleaming in the autumn sunlight."
      },
      {
        "author": "Virginia Woolf",
        "work": "The Waves",
        "quote": "Across the breezy expanse of the **Solent**, white yacht sails tilted against the blue haze of the shoreline."
      }
    ]
  },
  "Dashboard — spath\\spade.md": {
    "primary": "A tool with a broad, flat, sharp-edged metal blade and sturdy handle, used for digging, cutting turf, or earth-moving; also one of the four suits in playing cards.",
    "secondary": "In agricultural history and literature, the spade symbolizes manual toil and grounding labor, famously captured in Seamus Heaney's verse and Oscar Wilde's idioms ('call a spade a spade').",
    "quotes": [
      {
        "author": "Seamus Heaney",
        "work": "Digging",
        "quote": "Between my finger and my thumb the squat pen rests; snug as a gun. By God, the old man could handle a **spade**."
      },
      {
        "author": "Oscar Wilde",
        "work": "The Importance of Being Earnest",
        "quote": "I am glad to say that I have never seen a **spade**. It is obvious that our social spheres have been widely different."
      },
      {
        "author": "William Wordsworth",
        "work": "The Solitary Reaper",
        "quote": "Alone she cuts and binds the grain, leaning upon her heavy **spade** amidst the singing silence of the glen."
      }
    ]
  },
  "Dashboard — spath\\spatha.md": {
    "primary": "A long, straight, double-edged sword with a rounded tip, originally used by Celtic warriors and adopted by Roman auxiliary cavalry and late imperial legions.",
    "secondary": "In military archaeology, the spatha measured 75 to 100 cm in blade length and served as the direct morphological ancestor of early medieval Germanic and Viking migration swords.",
    "quotes": [
      {
        "author": "Tacitus",
        "work": "The Annals",
        "quote": "The Roman cavalry swept forward, cutting through the barbarian ranks with the sweeping strokes of the long **spatha**."
      },
      {
        "author": "Vegetius",
        "work": "De Re Militari (Epitoma Rei Militaris)",
        "quote": "Legionaries were trained to wield both the traditional short gladius and the longer cavalry blade known as the **spatha**."
      },
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The heavier armor of the late legionaries was complemented by the formidable reach of the double-edged **spatha**."
      }
    ]
  },
  "Dashboard — spath\\spathe.md": {
    "primary": "A large, often colorful, leaflike bract or pair of bracts that encloses or enfolds a flower cluster (spadix), characteristic of arums, palms, and calla lilies.",
    "secondary": "In angiosperm morphology, the spathe protects immature florets and frequently functions as a visual beacon or heat-trapping chamber to attract insect pollinators.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Various Contrivances by Which Orchids Are Fertilised by Insects",
        "quote": "In the arum, the opening of the convolute **spathe** is timed with the release of volatile scents that trap insect visitors."
      },
      {
        "author": "John Ruskin",
        "work": "Proserpina: Studies of Wayside Flowers",
        "quote": "The snow-white **spathe** of the water-arum curves like a sculptured alabaster shell sheltering the central spike."
      },
      {
        "author": "Alfred Russel Wallace",
        "work": "Palm Trees of the Amazon",
        "quote": "From within the giant woody **spathe**, the branched spadix emerges laden with thousands of nutritious palm fruits."
      }
    ]
  },
  "Dashboard — spath\\spathiphyllum.md": {
    "primary": "A genus of tropical monocotyledonous evergreen plants in the arum family (Araceae), commonly known as peace lilies, cultivated for glossy leaves and white flowering spathes.",
    "secondary": "In indoor horticulture and environmental biology, species of *Spathiphyllum* are popular house plants renowned for their tolerance of low light and air-filtering capabilities.",
    "quotes": [
      {
        "author": "Liberty Hyde Bailey",
        "work": "Cyclopedia of American Horticulture",
        "quote": "The elegant white banner-like spathe of **Spathiphyllum** remains decorative for many weeks after flowering."
      },
      {
        "author": "David Fairchild",
        "work": "The World Was My Garden",
        "quote": "In the shaded understory of the Colombian rain forest, we collected robust specimens of **Spathiphyllum** for greenhouse propagation."
      },
      {
        "author": "Asa Gray",
        "work": "Manual of the Botany of the Northern United States",
        "quote": "The distinct spadix free from the expanded white **Spathiphyllum** spathe distinguishes it from other aroid genera."
      }
    ]
  },
  "Dashboard — spath\\spay.md": {
    "primary": "To surgically remove the ovaries (oophorectomy) or ovaries and uterus (ovariohysterectomy) of a female animal to render her sterile.",
    "secondary": "In veterinary medicine, spaying female domestic pets prevents unwanted reproduction, eliminates pyometra risk, and significantly lowers mammary neoplasia incidence.",
    "quotes": [
      {
        "author": "James Herriot",
        "work": "All Creatures Great and Small",
        "quote": "Performing an elective procedure to **spay** a lively young farm bitch required gentle hands and swift, clean ligatures."
      },
      {
        "author": "Thomas Hardy",
        "work": "Far from the Madding Crowd",
        "quote": "The shepherd insisted that it was needful to **spay** the young ewes to preserve the hardiness of the upland flock."
      },
      {
        "author": "George Borrow",
        "work": "Lavengro",
        "quote": "The traveling smith had learned from old horse-leeches how to bleed, drench, and **spay** livestock with rustic skill."
      }
    ]
  },
  "Dashboard — spath\\spayed.md": {
    "primary": "Past tense and past participle of spay; surgically sterilized by excision of the reproductive organs (of a female animal).",
    "secondary": "In animal welfare and veterinary epidemiology, a spayed animal exhibits altered hormonal profiles, lacking estrus cycles and reproductive heat behaviors.",
    "quotes": [
      {
        "author": "James Herriot",
        "work": "All Things Bright and Beautiful",
        "quote": "The terrier was a healthy **spayed** female, placid in temperament and completely devoted to her elderly master."
      },
      {
        "author": "Konrad Lorenz",
        "work": "Man Meets Dog",
        "quote": "A **spayed** bitch often retains all the playful loyalty of her breed without the emotional turmoil of periodic seasons."
      },
      {
        "author": "Jack London",
        "work": "The Call of the Wild",
        "quote": "Among the sled-team dogs was a lean, **spayed** husky who pulled with untiring ferocity through the snow drifts."
      }
    ]
  },
  "Dashboard — spath\\spaying.md": {
    "primary": "The surgical act or procedure of sterilizing a female animal by removing the ovaries or uterus.",
    "secondary": "In veterinary clinical practice, spaying represents one of the most common surgical procedures, performed via midline laparotomy or minimally invasive laparoscopy.",
    "quotes": [
      {
        "author": "James Herriot",
        "work": "The Lord God Made Them All",
        "quote": "In veterinary college, the routine drill of **spaying** taught us surgical asepsis and meticulous haemostasis."
      },
      {
        "author": "Aldo Leopold",
        "work": "A Sand County Almanac",
        "quote": "Managing suburban deer populations by hormonal contraception or surgical **spaying** presents staggering logistical hurdles."
      },
      {
        "author": "George Orwell",
        "work": "Animal Farm",
        "quote": "Rumors spread among the hens that Napoleon was planning the systematic **spaying** of all unruly farm animals."
      }
    ]
  },
  "Dashboard — speir\\aplanospore.md": {
    "primary": "A non-motile, asexual reproductive spore formed within a sporangium in certain algae and fungi, lacking cilia or flagella.",
    "secondary": "In phycology and mycology, an aplanospore possesses a distinct cell wall and is produced when unfavorable aquatic conditions preclude zoospore flagellation.",
    "quotes": [
      {
        "author": "F. O. Bower",
        "work": "The Origin of a Land Flora",
        "quote": "The transition from an aquatic zoospore to an encysted **aplanospore** marked a crucial evolutionary step toward terrestrial adaptation."
      },
      {
        "author": "Gilbert M. Smith",
        "work": "Cryptogamic Botany: Algae and Fungi",
        "quote": "Under desiccating conditions, the protoplast divides to produce a thick-walled **aplanospore** capable of enduring drought."
      },
      {
        "author": "Heinrich Anton de Bary",
        "work": "Comparative Morphology and Biology of the Fungi, Mycetozoa and Bacteria",
        "quote": "Each internal **aplanospore** is liberated only when the fragile wall of the parent sporangium gelatinizes or ruptures."
      }
    ]
  },
  "Dashboard — speir\\archesporial.md": {
    "primary": "Of, relating to, or derived from the archesporium (the primitive cell layer that gives rise to spore mother cells in plants).",
    "secondary": "In plant developmental anatomy and embryology, the archesporial cell undergoes periclinal division to produce the primary parietal layer and primary sporogenous tissue.",
    "quotes": [
      {
        "author": "Katherine Esau",
        "work": "Plant Anatomy",
        "quote": "In the young anther, the subepidermal **archesporial** cell divides to form the parietal layer and the pollen mother cells."
      },
      {
        "author": "P. Maheshwari",
        "work": "An Introduction to the Embryology of Angiosperms",
        "quote": "The initial differentiation of the **archesporial** tissue occurs in the hypodermal layer of the ovular nucellus."
      },
      {
        "author": "F. O. Bower",
        "work": "Size and Form in Plants",
        "quote": "The volume of fertile spores produced is directly determined by the early mitotic expansion of the **archesporial** zone."
      }
    ]
  },
  "Dashboard — speir\\archesporium.md": {
    "primary": "The primordial cell or group of cells in a young sporangium or anther that gives rise to the sporogenous tissue or spore mother cells.",
    "secondary": "In cryptogamic and angiosperm organogenesis, the archesporium represents the ultimate founder cell population of the male or female germ line in plants.",
    "quotes": [
      {
        "author": "Eduard Strasburger",
        "work": "Handbook of Practical Botany",
        "quote": "Cross-sections of the immature moss capsule display the cylindrical **archesporium** wrapped around the central columella."
      },
      {
        "author": "F. O. Bower",
        "work": "The Ferns (Filicales)",
        "quote": "In primitive eusporangiate ferns, the **archesporium** is derived from several hypodermal cells of the developing receptacle."
      },
      {
        "author": "Katherine Esau",
        "work": "Anatomy of Seed Plants",
        "quote": "Meiotic divisions within the **archesporium** ultimately yield tetrads of microspores destined to become mature pollen grains."
      }
    ]
  },
  "Dashboard — speir\\carpospore.md": {
    "primary": "A diploid asexual spore produced within the carposporophyte phase of red algae (Rhodophyta) following fertilization.",
    "secondary": "In phycology, upon liberation from the cystocarp, a carpospore germinates into the diploid tetrasporophyte generation of the triphasic red algal life cycle.",
    "quotes": [
      {
        "author": "Fritsch, F. E.",
        "work": "The Structure and Reproduction of the Algae",
        "quote": "Discharge of the naked **carpospore** occurs through the ostiole of the cystocarp into the surrounding ocean currents."
      },
      {
        "author": "Kathleen M. Drew-Baker",
        "work": "Life History of Porphyra umbilicalis",
        "quote": "Settling of the liberated **carpospore** upon mollusk shells produces the filamentous Conchocelis stage of the alga."
      },
      {
        "author": "Gilbert M. Smith",
        "work": "Marine Algae of the Monterey Peninsula",
        "quote": "Each microscopic **carpospore** contains dense floridean starch granules to sustain initial germination on coastal rocks."
      }
    ]
  },
  "Dashboard — speir\\carposporic.md": {
    "primary": "Of, relating to, or functioning as a carpospore; pertaining to carpospore formation in red algae.",
    "secondary": "In rhodophyte cytology, carposporic development encompasses the gonimoblast filaments producing terminal carposporangia within the female cystocarp.",
    "quotes": [
      {
        "author": "Fritsch, F. E.",
        "work": "The Structure and Reproduction of the Algae",
        "quote": "The **carposporic** phase represents an amplification mechanism, generating hundreds of diploid spores from a single fertilization event."
      },
      {
        "author": "Kathleen M. Drew-Baker",
        "work": "Studies in the Bangiophycidae",
        "quote": "Nuclear staining revealed that the **carposporic** divisions remain diploid prior to emission from the parent thallus."
      },
      {
        "author": "E. M. Delf",
        "work": "The Morphological Aspect of the Red Algae",
        "quote": "The protective pericarp shelters the developing **carposporic** filaments against mechanical abrasion from surf."
      }
    ]
  },
  "Dashboard — speir\\carposporous.md": {
    "primary": "Bearing, producing, or reproducing by carpospores.",
    "secondary": "In marine phycological taxonomy, carposporous thalli describe mature female red algae that have developed cystocarps actively discharging carpospores.",
    "quotes": [
      {
        "author": "William Henry Harvey",
        "work": "Phycologia Britannica",
        "quote": "We collected robust **carposporous** specimens of Polysiphonia clinging to kelp stipes in the intertidal zone."
      },
      {
        "author": "Gilbert M. Smith",
        "work": "Cryptogamic Botany",
        "quote": "The presence of raised, urn-shaped cystocarps identifies the **carposporous** plant from its tetrasporic counterparts."
      },
      {
        "author": "Fritsch, F. E.",
        "work": "The Structure and Reproduction of the Algae",
        "quote": "Fertilization induces rapid mitotic sprouting of gonimoblasts, transforming the procarp into a fertile **carposporous** structure."
      }
    ]
  },
  "Dashboard — speir\\chlamydospore.md": {
    "primary": "A thick-walled, non-deciduous resting asexual spore formed by the rounding off and encystment of a fungal hyphal cell.",
    "secondary": "In mycology and phytopathology, chlamydospores (formed by fungi such as *Candida albicans* and *Fusarium*) enable survival across freezing, desiccation, and chemical stress.",
    "quotes": [
      {
        "author": "Heinrich Anton de Bary",
        "work": "Comparative Morphology and Biology of the Fungi",
        "quote": "The persistent **chlamydospore** carries the fungus across long winter droughts when vegetative mycelia perish."
      },
      {
        "author": "Selman Waksman",
        "work": "Principles of Soil Microbiology",
        "quote": "Soil cultures revealed that *Fusarium* persists for decades primarily in the form of dormant, durable **chlamydospore** units."
      },
      {
        "author": "René Dubos",
        "work": "Bacterial and Mycotic Infections of Man",
        "quote": "Diagnostic identification of *Candida albicans* relies upon its characteristic formation of a terminal **chlamydospore** on cornmeal agar."
      }
    ]
  },
  "Dashboard — speir\\diaspora.md": {
    "primary": "The dispersion, scattering, or movement of a people away from their established ancestral homeland; also the dispersed community itself.",
    "secondary": "Historically applied to the exile of the Jewish people following the Babylonian and Roman conquests, diaspora now broadly encompasses any dispersed ethnic or religious population.",
    "quotes": [
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "Following the destruction of Jerusalem by Titus, the tragic **diaspora** dispersed Jewish communities into every province of the Mediterranean."
      },
      {
        "author": "W. E. B. Du Bois",
        "work": "The World and Africa",
        "quote": "The transatlantic slave trade created an immense African **diaspora** whose cultural resilience transformed the Americas."
      },
      {
        "author": "George Eliot",
        "work": "Daniel Deronda",
        "quote": "He felt drawn by an inexplicable kinship to the scattered members of this ancient, unvanquished **diaspora**."
      }
    ]
  },
  "Dashboard — speir\\diaspore.md": {
    "primary": "In botany, any plant part (such as a seed, fruit, spore, or bud) that serves as a functional unit of dispersal; in mineralogy, an aluminum oxide hydroxide mineral (α-AlO(OH)).",
    "secondary": "In plant reproductive ecology, diaspore morphology (wings, plumes, fleshy arils, hooked spines) reflects co-evolution with wind, water, or animal dispersal vectors.",
    "quotes": [
      {
        "author": "Ridley, Henry Nicholas",
        "work": "The Dispersal of Plants Throughout the World",
        "quote": "The aerodynamic plume attached to the composite **diaspore** allows it to ride thermal air currents for many leagues."
      },
      {
        "author": "James Dwight Dana",
        "work": "Manual of Mineralogy",
        "quote": "Associated with corundum and bauxite, the platy crystals of **diaspore** exhibit pearly luster and perfect cleavage."
      },
      {
        "author": "Eduard Strasburger",
        "work": "Textbook of Botany",
        "quote": "Whether a single seed or a fleshy syncarp, the botanical **diaspore** contains the genetic future of the parent plant."
      }
    ]
  },
  "Dashboard — speir\\endospore.md": {
    "primary": "A tough, dormant, non-reproductive structure produced inside certain bacteria (such as *Bacillus* and *Clostridium*) to survive extreme environmental stress.",
    "secondary": "In microbiology, endospores contain dipicolinic acid and calcium in their dehydrated core, conferring extreme resistance to heat, ultraviolet radiation, and chemical disinfectants.",
    "quotes": [
      {
        "author": "Ferdinand Cohn",
        "work": "Researches on Bacteria",
        "quote": "The discovery of the heat-resistant **endospore** in *Bacillus subtilis* finally disproved the hypothesis of spontaneous generation."
      },
      {
        "author": "Robert Koch",
        "work": "The Etiology of Anthrax Disease",
        "quote": "Pastures remained infective for years because the anthrax **endospore** could survive winter frosts and summer suns without losing virulence."
      },
      {
        "author": "Louis Pasteur",
        "work": "Studies on the Germ Theory",
        "quote": "Sterilization requires heating above the boiling point to destroy the stubborn bacterial **endospore** lurking in the broth."
      }
    ]
  },
  "Dashboard — speir\\esparto.md": {
    "primary": "A coarse, wiry, perennial grass (*Macrochloa tenacissima*) native to southern Spain and North Africa, used for making cords, baskets, and high-quality paper.",
    "secondary": "In paper manufacturing and economic botany, esparto grass fibers yield soft, opaque, bulky book printing paper with superior ink-receptive properties.",
    "quotes": [
      {
        "author": "Richard Ford",
        "work": "A Handbook for Travellers in Spain",
        "quote": "The arid hills of Murcia are covered in tough clumps of **esparto**, woven by peasants into ropes, sandals, and panniers."
      },
      {
        "author": "George Borrow",
        "work": "The Bible in Spain",
        "quote": "Mules laden with huge bundles of cut **esparto** trod the dusty highway toward the coastal paper mills."
      },
      {
        "author": "Charles Dickens",
        "work": "All the Year Round",
        "quote": "The introduction of Spanish **esparto** as a substitute for cotton rags rescued the printing press from acute paper shortages."
      }
    ]
  },
  "Dashboard — speir\\eusporangium.md": {
    "primary": "A sporangium that originates from a group of superficial initial cells and develops a multi-layered wall, typical of primitive vascular plants.",
    "secondary": "In pteridophyte evolutionary morphology, eusporangia produce large, indefinite numbers of spores and are found in marattioid ferns, ophioglossaleans, and lycophytes.",
    "quotes": [
      {
        "author": "F. O. Bower",
        "work": "The Ferns (Filicales)",
        "quote": "The massive **eusporangium** of Ophioglossum arises from several parent cells and contains thousands of spores."
      },
      {
        "author": "Katherine Esau",
        "work": "Plant Anatomy",
        "quote": "Unlike the delicate leptosporangium, the **eusporangium** develops a robust jacket consisting of two or more cell layers."
      },
      {
        "author": "Eduard Strasburger",
        "work": "Textbook of Botany",
        "quote": "In phylogenetic terms, the **eusporangium** is the ancestral type of sporangium characteristic of early land flora."
      }
    ]
  },
  "Dashboard — speir\\exospore.md": {
    "primary": "A spore formed by external budding or abstriction from the parent organism, as in certain cyanobacteria and fungi; also the outer coat of a spore (exosporium).",
    "secondary": "In palynology and spore ultrastructure, the exospore forms the durable outer sporopollenin-rich stratum that resists environmental degradation.",
    "quotes": [
      {
        "author": "Heinrich Anton de Bary",
        "work": "Comparative Morphology and Biology of the Fungi",
        "quote": "The conidial spore produced by external abstriction may be considered a true **exospore** distinct from internal sporangiospores."
      },
      {
        "author": "Fritsch, F. E.",
        "work": "The Structure and Reproduction of the Algae",
        "quote": "Certain Chamaesiphonales pinch off successive **exospore** cells from the open apical end of their sheaths."
      },
      {
        "author": "Eduard Strasburger",
        "work": "Handbook of Practical Botany",
        "quote": "The sculptured ornamentation of the fern spore is laid down within the protective **exospore** layer."
      }
    ]
  },
  "Dashboard — speir\\heterosporous.md": {
    "primary": "Producing two distinct types of spores of different sizes and sexes: small microspores (male) and larger megaspores (female).",
    "secondary": "In plant evolutionary history, heterosporous vascular plants (such as *Selaginella*, water ferns, and all seed plants) established the developmental prerequisite for the evolution of seeds.",
    "quotes": [
      {
        "author": "F. O. Bower",
        "work": "The Origin of a Land Flora",
        "quote": "The **heterosporous** condition arose independently in several ancient pteridophyte lines, culminating in the seed habit."
      },
      {
        "author": "Katherine Esau",
        "work": "Plant Anatomy",
        "quote": "In every **heterosporous** lycophyte, microspores yield reduced male gametophytes while megaspores nourish the embryonic sporophyte."
      },
      {
        "author": "Asa Gray",
        "work": "First Lessons in Botany and Vegetable Physiology",
        "quote": "All flowering plants are essentially **heterosporous**, producing pollen grains as microspores and embryo sacs as megaspores."
      }
    ]
  },
  "Dashboard — speir\\heterospory.md": {
    "primary": "The condition of producing two different types and sizes of spores, specifically microspores and megaspores, which develop into unisexual gametophytes.",
    "secondary": "In evolutionary paleobotany, the emergence of heterospory during the Devonian epoch enabled the extreme reduction of the gametophyte and the origin of the ovule.",
    "quotes": [
      {
        "author": "F. O. Bower",
        "work": "The Origin of a Land Flora",
        "quote": "The evolutionary advent of **heterospory** was the most profound physiological breakthrough in the history of vascular land plants."
      },
      {
        "author": "Eduard Strasburger",
        "work": "Textbook of Botany",
        "quote": "Through **heterospory**, the maternal plant retains the megaspore, providing sustained nutrition to the nascent embryo."
      },
      {
        "author": "Gilbert M. Smith",
        "work": "Cryptogamic Botany: Bryophytes and Pteridophytes",
        "quote": "In *Selaginella*, the physiological specialization of **heterospory** is accompanied by marked sexual dimorphism in gametophyte architecture."
      }
    ]
  },
  "Dashboard — speir\\homosporous.md": {
    "primary": "Producing only one type and size of spore, which typically develops into a bisexual gametophyte bearing both antheridia and archegonia.",
    "secondary": "In botanical systematics, homosporous plants comprise bryophytes, most lycopods (*Lycopodium*), horsetails, and the vast majority of living leptosporangiate ferns.",
    "quotes": [
      {
        "author": "F. O. Bower",
        "work": "The Ferns (Filicales)",
        "quote": "The ancestral condition in filicalean ferns is strictly **homosporous**, with each sporangium releasing identical wind-borne spores."
      },
      {
        "author": "Katherine Esau",
        "work": "Plant Anatomy",
        "quote": "A single spore from a **homosporous** fern germinates on moist soil to produce a green heart-shaped, bisexual prothallus."
      },
      {
        "author": "Eduard Strasburger",
        "work": "Textbook of Botany",
        "quote": "In **homosporous** pteridophytes, genetic recombination depends upon cross-fertilization between separate prothallia."
      }
    ]
  },
  "Dashboard — speir\\homospory.md": {
    "primary": "The condition or evolutionary state of producing spores of a single, uniform type and size that give rise to bisexual gametophytes.",
    "secondary": "In plant reproductive biology, homospory represents the primitive condition from which heterospory and the seed habit subsequently evolved in vascular lineages.",
    "quotes": [
      {
        "author": "F. O. Bower",
        "work": "The Origin of a Land Flora",
        "quote": "The persistence of **homospory** throughout modern ferns proves the remarkable ecological efficacy of the independent prothallus."
      },
      {
        "author": "Gilbert M. Smith",
        "work": "Cryptogamic Botany",
        "quote": "In species maintaining **homospory**, both sperm and egg are produced on the same diminutive thallus."
      },
      {
        "author": "Asa Gray",
        "work": "Elements of Botany",
        "quote": "From ancestral **homospory**, the selective advantage of maternal nourishment drove the diversification of heterosporous taxa."
      }
    ]
  }
};

const count = updateNotesBatch(baseClusterDir, batchData);
console.log(`[Form Finish 4 - Batch 2] Successfully updated ${count}/${Object.keys(batchData).length} notes.`);
