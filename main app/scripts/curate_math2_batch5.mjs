import { updateNotesBatch } from './curate-updater-util.mjs';
import path from 'path';

const CLUSTER_DIR = path.resolve('App database/Greek roots/Cluster Number & Mathematics');
const batchData = {
  "Dashboard — mono\\monolingually.md": {
    "primary": "In a monolingual manner; speaking, writing, or using only a single language.",
    "secondary": "In linguistics and educational psychology, functioning cognitively and socially exclusively within one linguistic system.",
    "quotes": [
      {
        "author": "Steven Pinker",
        "work": "The Language Instinct",
        "quote": "Children raised **monolingually** acquire complex syntactic parameters effortlessly within the first few years of life."
      },
      {
        "author": "George Steiner",
        "work": "After Babel",
        "quote": "To experience literature **monolingually** is to remain oblivious to the untranslatable resonances of foreign idiom."
      },
      {
        "author": "Noam Chomsky",
        "work": "Knowledge of Language",
        "quote": "Even when raised **monolingually**, an individual masters an internal system of extraordinary structural richness."
      }
    ]
  },
  "Dashboard — mono\\monolith.md": {
    "primary": "A large single upright block of stone, especially one shaped into or serving as a pillar or monument.",
    "secondary": "A massive, uniform, and intractable structure, enterprise, or software architecture that is indivisible and slow to change.",
    "quotes": [
      {
        "author": "Arthur C. Clarke",
        "work": "2001: A Space Odyssey",
        "quote": "The black **monolith** stood upright in the lunar dust, untouched by solar wind or cosmic rays for three million years."
      },
      {
        "author": "Percy Bysshe Shelley",
        "work": "Ozymandias",
        "quote": "The shattered **monolith** lay half buried beneath the lone and level sands stretching far away."
      },
      {
        "author": "Martin Fowler",
        "work": "Patterns of Enterprise Application Architecture",
        "quote": "Decomposing a core legacy **monolith** requires careful decoupling of database schemas and operational boundaries."
      }
    ]
  },
  "Dashboard — mono\\monolithic.md": {
    "primary": "Formed of a single large block of stone; massive, solid, and uniform.",
    "secondary": "Describing large, rigid, and indivisible institutions, systems, or semiconductor circuits built on a single substrate.",
    "quotes": [
      {
        "author": "George Orwell",
        "work": "1984",
        "quote": "The pyramid of the Ministry of Truth rose like an enormous **monolithic** bulk above the grimy rooftops of London."
      },
      {
        "author": "Carver Mead",
        "work": "Introduction to VLSI Systems",
        "quote": "Fabricating circuits as a **monolithic** silicon structure eliminated millions of fragile solder joints."
      },
      {
        "author": "Hannah Arendt",
        "work": "The Origins of Totalitarianism",
        "quote": "State propaganda cultivates an illusion of **monolithic** unanimity to suppress independent civic action."
      }
    ]
  },
  "Dashboard — mono\\monologist.md": {
    "primary": "A person who delivers a monologue, or who habitually monopolizes conversations.",
    "secondary": "In theatrical performance and literature, a solo artist who performs dramatic soliloquies, character sketches, or stand-up commentary.",
    "quotes": [
      {
        "author": "Anton Chekhov",
        "work": "On the Harmful Effects of Tobacco",
        "quote": "The nervous **monologist** stepped to the podium, ostensibly to lecture on hygiene, but bared his domestic misery instead."
      },
      {
        "author": "Samuel Taylor Coleridge",
        "work": "Table Talk",
        "quote": "Charles Lamb remarked that Hazlitt was an incomparable listener, but Coleridge an unstoppable **monologist**."
      },
      {
        "author": "Virginia Woolf",
        "work": "The Waves",
        "quote": "Bernard mused like a private **monologist**, spinning sentences to catch the fleeting drift of human experience."
      }
    ]
  },
  "Dashboard — mono\\monologuise.md": {
    "primary": "To speak in or deliver a monologue; to talk aloud to oneself or monopolize a conversation (British spelling of monologuize).",
    "secondary": "In literary criticism and drama, to express inner consciousness or philosophical musings through extended solo speech.",
    "quotes": [
      {
        "author": "George Bernard Shaw",
        "work": "Pygmalion",
        "quote": "Professor Higgins began to **monologuise** with passionate eloquence on the science of phonetics, oblivious to his listeners."
      },
      {
        "author": "Oscar Wilde",
        "work": "The Picture of Dorian Gray",
        "quote": "Lord Henry loved to **monologuise** across the dinner table, tossing glittering paradoxes into the silent room."
      },
      {
        "author": "James Joyce",
        "work": "Ulysses",
        "quote": "Bloom paused beneath the awning, beginning to **monologuise** on the mechanics of tramlines and morning crowds."
      }
    ]
  },
  "Dashboard — mono\\monologuize.md": {
    "primary": "To deliver a monologue; to speak at length alone or dominate a dialogue without letting others speak.",
    "secondary": "In narrative prose and drama, to articulate private reflections, dramatic soliloquies, or unprompted intellectual lectures.",
    "quotes": [
      {
        "author": "Henry James",
        "work": "The Portrait of a Lady",
        "quote": "Madame Merle possessed the rare grace never to **monologuize**, drawing others into delicate, mutual conversation."
      },
      {
        "author": "Mark Twain",
        "work": "The Innocents Abroad",
        "quote": "Our loquacious guide proceeded to **monologuize** endlessly before every ruined pillar in the Roman Forum."
      },
      {
        "author": "Herman Melville",
        "work": "Moby-Dick",
        "quote": "Captain Ahab would pace the quarterdeck at midnight, pausing only to **monologuize** to the silent stars above."
      }
    ]
  },
  "Dashboard — mono\\monomania.md": {
    "primary": "An exaggerated or obsessive enthusiasm for or preoccupation with one thing.",
    "secondary": "In nineteenth-century alienism and psychiatry, a form of partial insanity where the mind is disordered on a single subject while remaining rational on others.",
    "quotes": [
      {
        "author": "Herman Melville",
        "work": "Moby-Dick",
        "quote": "Ahab's frantic **monomania** invested the white whale with all the subtle demonisms of the world."
      },
      {
        "author": "Edgar Allan Poe",
        "work": "Berenice",
        "quote": "This nervous intensity of interest was an undeniable form of **monomania**, fastening upon trivial objects with terrifying fixation."
      },
      {
        "author": "Arthur Conan Doyle",
        "work": "The Adventure of the Six Napoleons",
        "quote": "Holmes deduced that the criminal suffered from an acute, destructive **monomania** centered upon plaster busts of the Emperor."
      }
    ]
  },
  "Dashboard — mono\\monomaniac.md": {
    "primary": "A person affected by monomania; someone obsessively fixated on a single idea, pursuit, or object.",
    "secondary": "In classical clinical psychology and literary characterization, an individual consumed by an unyielding single-minded obsession.",
    "quotes": [
      {
        "author": "Herman Melville",
        "work": "Moby-Dick",
        "quote": "The brooding **monomaniac** captain stared into the wake, deaf to the warnings of his first mate."
      },
      {
        "author": "Charles Dickens",
        "work": "A Tale of Two Cities",
        "quote": "Dr. Manette relapsed into the state of a quiet **monomaniac**, making shoes in the garret with haunted rhythm."
      },
      {
        "author": "Fyodor Dostoevsky",
        "work": "Crime and Punishment",
        "quote": "Razumikhin warned that Raskolnikov was behaving like an irritable **monomaniac** on the verge of madness."
      }
    ]
  },
  "Dashboard — mono\\monomaniacal.md": {
    "primary": "Of, relating to, or exhibiting monomania; obsessively preoccupied with a single subject.",
    "secondary": "Characteristic of an unyielding, single-minded fixation that subordinates all other considerations, values, or perceptions.",
    "quotes": [
      {
        "author": "Joseph Conrad",
        "work": "Heart of Darkness",
        "quote": "Kurtz pursued his ivory quest with a **monomaniacal** fury that alienated him from all civilized restraint."
      },
      {
        "author": "Herman Melville",
        "work": "Moby-Dick",
        "quote": "Ahab paced the deck with **monomaniacal** determination, seeking vengeance against the great white monster."
      },
      {
        "author": "Thomas Carlyle",
        "work": "The French Revolution",
        "quote": "Robespierre pursued his vision of incorruptible virtue with a **monomaniacal** zeal that paved the way for the Terror."
      }
    ]
  },
  "Dashboard — mono\\monomer.md": {
    "primary": "A molecule that can react together with other monomer molecules to form a larger polymer chain or three-dimensional network.",
    "secondary": "In macromolecular chemistry and biochemistry, the repeating chemical subunit (such as a nucleotide, amino acid, or styrene) of synthetic or biological polymers.",
    "quotes": [
      {
        "author": "Linus Pauling",
        "work": "The Nature of the Chemical Bond",
        "quote": "The addition of an initiator causes each ethylene **monomer** to link sequentially into a high-molecular-weight polymer."
      },
      {
        "author": "Bruce Alberts",
        "work": "Molecular Biology of the Cell",
        "quote": "Actin filaments are dynamic polar polymers assembled from globular actin **monomer** subunits."
      },
      {
        "author": "James Watson",
        "work": "Molecular Biology of the Gene",
        "quote": "DNA polymerase catalyzes the covalent addition of each nucleotide **monomer** to the growing daughter strand."
      }
    ]
  },
  "Dashboard — mono\\monometallic.md": {
    "primary": "Consisting of or using only one metal.",
    "secondary": "In monetary economics, describing a monetary system where currency value is legally based upon a single metallic standard (such as gold or silver).",
    "quotes": [
      {
        "author": "Alfred Marshall",
        "work": "Money, Credit and Commerce",
        "quote": "Advocates of the gold standard maintained that a **monometallic** currency eliminated the exchange volatility inherent in bimetallism."
      },
      {
        "author": "Milton Friedman",
        "work": "A Monetary History of the United States",
        "quote": "The Crime of 1873 shifted the nation toward an effective **monometallic** gold basis, triggering fierce agrarian protest."
      },
      {
        "author": "John Maynard Keynes",
        "work": "A Treatise on Money",
        "quote": "The stability of a **monometallic** standard depends entirely upon the world production rate of the chosen single metal."
      }
    ]
  },
  "Dashboard — mono\\monomorium.md": {
    "primary": "A genus of small, cosmopolitan ants in the subfamily Myrmicinae, commonly known as pharaoh ants or thief ants.",
    "secondary": "In entomology and pest management, minute polymorphic ants (such as Monomorium pharaonis) notorious for infesting heated buildings and hospitals.",
    "quotes": [
      {
        "author": "E.O. Wilson",
        "work": "The Insect Societies",
        "quote": "Colonies of **Monomorium** establish decentralized multi-queen supercolonies that thrive in urban structures."
      },
      {
        "author": "William Morton Wheeler",
        "work": "Ants: Their Structure, Development and Behavior",
        "quote": "The tiny pest ant **Monomorium** pharaonis nests within hollow baseboards, trailing stealthily along hot water pipes."
      },
      {
        "author": "Bert Hölldobler",
        "work": "The Ants",
        "quote": "Chemical trail recruitment in **Monomorium** relies on microgram quantities of volatile venom alkaloids."
      }
    ]
  },
  "Dashboard — mono\\monomorphemic.md": {
    "primary": "Consisting of only a single morpheme; incapable of being analyzed into smaller meaningful grammatical units.",
    "secondary": "In morphological linguistics, designating root words (such as 'cat', 'walk', or 'blue') that lack derivational or inflectional affixes.",
    "quotes": [
      {
        "author": "Steven Pinker",
        "work": "Words and Rules",
        "quote": "While 'cats' is polymorphemic, the basic noun 'cat' is strictly **monomorphemic**, carrying meaning as an indivisible lexical atom."
      },
      {
        "author": "Noam Chomsky",
        "work": "The Minimalist Program",
        "quote": "Lexical insertion draws **monomorphemic** items from the lexicon to initiate syntactic derivation."
      },
      {
        "author": "Edward Sapir",
        "work": "Language: An Introduction to the Study of Speech",
        "quote": "Languages differ profoundly in whether basic concepts are expressed by **monomorphemic** roots or elaborate compound stems."
      }
    ]
  },
  "Dashboard — mono\\mononeuropathy.md": {
    "primary": "Damage or disease affecting a single peripheral nerve, causing pain, weakness, or loss of sensation in that nerve's distribution.",
    "secondary": "In neurology, focal nerve dysfunction (such as carpal tunnel syndrome or radial nerve palsy) caused by localized compression, ischemia, or trauma.",
    "quotes": [
      {
        "author": "Oliver Sacks",
        "work": "The Man Who Mistook His Wife for a Hat",
        "quote": "Compression of the median nerve at the wrist produces classic carpal tunnel syndrome, the most prevalent human **mononeuropathy**."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Sudden unilateral foot drop after crossing the legs indicates a pressure **mononeuropathy** of the common peroneal nerve."
      },
      {
        "author": "Eric Kandel",
        "work": "Principles of Neural Science",
        "quote": "Electromyography differentiates an isolated **mononeuropathy** from generalized polyneuropathy by mapping focal conduction blocks."
      }
    ]
  },
  "Dashboard — mono\\monongahela.md": {
    "primary": "A river rising in West Virginia and flowing north into southwestern Pennsylvania, where it joins the Allegheny River at Pittsburgh to form the Ohio River.",
    "secondary": "In American history, the site of the 1755 Battle of the Monongahela (Braddock's Defeat); also celebrated as a historic variety of rye whiskey.",
    "quotes": [
      {
        "author": "Herman Melville",
        "work": "Moby-Dick",
        "quote": "Would now, it were old Orleans whiskey, or old Ohio, or unspeakable old **Monongahela**!"
      },
      {
        "author": "George Washington",
        "work": "Writings",
        "quote": "We marched along the banks of the **Monongahela**, where the crossing proved difficult for our baggage wagons."
      },
      {
        "author": "Walt Whitman",
        "work": "Leaves of Grass",
        "quote": "By the wild waters of the **Monongahela**, where the coal smoke mingles with the mountain fog."
      }
    ]
  },
  "Dashboard — mono\\mononuclear.md": {
    "primary": "Having only one nucleus (used especially of white blood cells such as monocytes and lymphocytes).",
    "secondary": "In immunology and pathology, denoting the mononuclear phagocyte system, a network of tissue macrophages and circulating monocytes.",
    "quotes": [
      {
        "author": "Paul Ehrlich",
        "work": "Histology of the Blood",
        "quote": "The large **mononuclear** leucocyte is readily distinguished by its expansive pale cytoplasm and bean-shaped nucleus."
      },
      {
        "author": "Siddhartha Mukherjee",
        "work": "The Song of the Cell",
        "quote": "Biopsies of the chronic inflammatory lesion revealed dense infiltration by **mononuclear** cells."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "In chronic infections like malaria, the spleen engorges with proliferating **mononuclear** phagocytes."
      }
    ]
  },
  "Dashboard — mono\\mononucleate.md": {
    "primary": "Having a single nucleus; uninucleate.",
    "secondary": "In cytology, describing typical somatic eukaryotic cells that contain exactly one nucleus, contrasting with binucleate or multinucleate syncytia.",
    "quotes": [
      {
        "author": "Edmund Beecher Wilson",
        "work": "The Cell in Development and Inheritance",
        "quote": "A typical blastomere remains **mononucleate** throughout interphase until karyokinesis initiates."
      },
      {
        "author": "Katherine Esau",
        "work": "Plant Anatomy",
        "quote": "Unlike multinucleate coenocytic algae, higher plant parenchyma is composed of orderly **mononucleate** cells."
      },
      {
        "author": "Bruce Alberts",
        "work": "Molecular Biology of the Cell",
        "quote": "Skeletal muscle fibers fuse during development into giant syncytia, whereas smooth muscle cells remain strictly **mononucleate**."
      }
    ]
  },
  "Dashboard — mono\\mononucleosis.md": {
    "primary": "An abnormally large proportion of monocytes or mononuclear leukocytes in the blood; especially infectious mononucleosis ('mono').",
    "secondary": "In infectious disease medicine, an acute viral syndrome caused primarily by Epstein-Barr virus (EBV), marked by fever, sore throat, and lymphadenopathy.",
    "quotes": [
      {
        "author": "Abraham Verghese",
        "work": "The Tennis Partner",
        "quote": "The adolescent patient presented with classic symptoms of infectious **mononucleosis**: profound fatigue, pharyngitis, and splenomegaly."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "A peripheral blood smear demonstrating atypical lymphocytes confirms the clinical suspicion of infectious **mononucleosis**."
      },
      {
        "author": "Siddhartha Mukherjee",
        "work": "The Emperor of All Maladies",
        "quote": "Anthony Epstein and Yvonne Barr isolated virus particles from Burkitt lymphoma that also proved to be the causative agent of infectious **mononucleosis**."
      }
    ]
  },
  "Dashboard — mono\\monopolist.md": {
    "primary": "A person, corporation, or group that has a monopoly or that controls the supply of a commodity or service.",
    "secondary": "In classical economics, an economic agent capable of setting market price above marginal cost by virtue of exclusive market power.",
    "quotes": [
      {
        "author": "Adam Smith",
        "work": "The Wealth of Nations",
        "quote": "The **monopolist**, by keeping the market constantly under-stocked, sells his commodities much above the natural price."
      },
      {
        "author": "Karl Marx",
        "work": "Capital",
        "quote": "Capitalist competition relentlessly concentrates enterprise into the hands of the victorious **monopolist**."
      },
      {
        "author": "Joseph Schumpeter",
        "work": "Capitalism, Socialism and Democracy",
        "quote": "The transient profits earned by an innovative **monopolist** fuel the creative destruction that drives economic growth."
      }
    ]
  },
  "Dashboard — mono\\monopolistic.md": {
    "primary": "Characterized by, tending toward, or possessing the characteristics of a monopoly.",
    "secondary": "In industrial economics, describing markets where sellers exercise pricing discretion (as in Edward Chamberlin's theory of monopolistic competition).",
    "quotes": [
      {
        "author": "Edward Chamberlin",
        "work": "The Theory of Monopolistic Competition",
        "quote": "Most real-world industries operate neither under pure monopoly nor pure competition, but in a blended state of **monopolistic** competition."
      },
      {
        "author": "John Kenneth Galbraith",
        "work": "The New Industrial State",
        "quote": "Large corporations wield **monopolistic** power not merely to extract profit, but to eliminate market uncertainty."
      },
      {
        "author": "Theodore Roosevelt",
        "work": "The Strenuous Life",
        "quote": "We will not tolerate **monopolistic** combinations that strangle fair enterprise and oppress the consumer."
      }
    ]
  },
  "Dashboard — mono\\monopolize.md": {
    "primary": "To obtain exclusive possession or control of; to dominate completely.",
    "secondary": "In commerce and law, to acquire and maintain market dominance in a particular trade or commodity, restricting competition.",
    "quotes": [
      {
        "author": "Adam Smith",
        "work": "The Wealth of Nations",
        "quote": "Merchants naturally seek to **monopolize** the home market, securing legislative prohibitions against rival foreign imports."
      },
      {
        "author": "Jane Austen",
        "work": "Pride and Prejudice",
        "quote": "Mr. Wickham seemed determined to **monopolize** Elizabeth's conversation throughout the entire evening."
      },
      {
        "author": "George Orwell",
        "work": "Animal Farm",
        "quote": "The pigs took care to **monopolize** all the milk and windfalls, claiming it was essential for their brainwork."
      }
    ]
  },
  "Dashboard — mono\\monorail.md": {
    "primary": "A railroad in which the track consists of a single rail, typically elevated above ground.",
    "secondary": "In urban transit engineering, a straddle-beam or suspended transit system designed for grade-separated passenger transit in dense corridors.",
    "quotes": [
      {
        "author": "H.G. Wells",
        "work": "When the Sleeper Wakes",
        "quote": "Swift aerodynamic cars glided noiselessly along the elevated **monorail** that spanned the glowing canyon of the futuristic boulevard."
      },
      {
        "author": "Arthur C. Clarke",
        "work": "Rendezvous with Rama",
        "quote": "A robotic maintenance car traveled along the central **monorail** running the length of the cylindrical world."
      },
      {
        "author": "Jules Verne",
        "work": "Paris in the Twentieth Century",
        "quote": "He imagined commuters whisked across the metropolis on pneumatic cars riding an elevated **monorail**."
      }
    ]
  },
  "Dashboard — mono\\monorchidism.md": {
    "primary": "The condition of having only one testis descended or present in the scrotum (variant of monorchism).",
    "secondary": "In urology and pediatric surgery, congenital unilateral testicular agenesis or failure of one testis to descend from the abdominal cavity.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Clinical evaluation of the male infant revealed unilateral cryptorchidism presenting as apparent **monorchidism**."
      },
      {
        "author": "John Hunter",
        "work": "A Treatise on the Venereal Disease",
        "quote": "Dissection proved that the condition was true **monorchidism**, with complete congenital absence of the right spermatic vessel."
      },
      {
        "author": "Siddhartha Mukherjee",
        "work": "The Song of the Cell",
        "quote": "Developmental anomalies during embryonic gonadal ridge migration can result in unilateral agenesis or **monorchidism**."
      }
    ]
  },
  "Dashboard — mono\\monorchism.md": {
    "primary": "A condition in which only one testis is present in the scrotum, due to unilateral agenesis, developmental arrest, or undescended testis.",
    "secondary": "In medical dysmorphology, the state of having a single functional testicle.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "Lectures on Angina Pectoris and Allied States",
        "quote": "Surgical exploration established that the patient's apparent **monorchism** was caused by an undescended inguinal testis."
      },
      {
        "author": "Charles Darwin",
        "work": "The Descent of Man",
        "quote": "Congenital anomalies like **monorchism** illustrate how embryonic developmental symmetry can occasionally fail along one bilateral axis."
      },
      {
        "author": "Atul Gawande",
        "work": "Complications: A Surgeon's Notes on an Imperfect Science",
        "quote": "Corrective orchidopexy was performed in childhood to resolve what had initially appeared to be congenital **monorchism**."
      }
    ]
  },
  "Dashboard — mono\\monosaccharide.md": {
    "primary": "A simple sugar that cannot be hydrolyzed to give a simpler sugar (such as glucose, fructose, or galactose).",
    "secondary": "In biochemistry, the fundamental monomeric building block of carbohydrates, typically having the empirical formula (CH2O)n.",
    "quotes": [
      {
        "author": "Emil Fischer",
        "work": "Investigations on the Carbo-hydrates",
        "quote": "Determining the absolute stereochemistry of each D-aldose **monosaccharide** was the crowning achievement of nineteenth-century organic synthesis."
      },
      {
        "author": "Bruce Alberts",
        "work": "Molecular Biology of the Cell",
        "quote": "Cellular respiration begins with glycolysis, where the six-carbon **monosaccharide** glucose is cleaved into pyruvate."
      },
      {
        "author": "Michael Pollan",
        "work": "In Defense of Food",
        "quote": "High-fructose corn syrup delivers unbound **monosaccharide** units directly to the liver without requiring enzymatic digestion."
      }
    ]
  },
  "Dashboard — mono\\monosaccharose.md": {
    "primary": "A monosaccharide; a simple sugar.",
    "secondary": "In classical physiological chemistry, an archaic synonym for monosaccharide, designating unhydrolyzable monomeric sugars.",
    "quotes": [
      {
        "author": "Emil Fischer",
        "work": "Studies in Organic Chemistry",
        "quote": "Fermentation proceeds directly when yeast ferments encounter a compatible hexose **monosaccharose**."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Benedict's qualitative test detects any reducing **monosaccharose** excreted in the urine of diabetic patients."
      },
      {
        "author": "Claude Bernard",
        "work": "An Introduction to the Study of Experimental Medicine",
        "quote": "The hepatic glycogenic function converts stored animal starch into a diffusible **monosaccharose** entering the bloodstream."
      }
    ]
  },
  "Dashboard — mono\\monosemous.md": {
    "primary": "Having only one meaning; not polysemous or ambiguous.",
    "secondary": "In semantics and lexicography, describing scientific or technical terms that possess a single unambiguous denotation.",
    "quotes": [
      {
        "author": "Steven Pinker",
        "work": "The Stuff of Thought",
        "quote": "Scientific jargon strives to be strictly **monosemous**, avoiding the slippery ambiguities of everyday polysemy."
      },
      {
        "author": "Willard Van Orman Quine",
        "work": "Word and Object",
        "quote": "Formalized logical languages aspire to an inventory of **monosemous** predicates that map to unique truth conditions."
      },
      {
        "author": "Ferdinand de Saussure",
        "work": "Course in General Linguistics",
        "quote": "In living natural speech, rarely is a popular signifier genuinely **monosemous** across diverse dialects and centuries."
      }
    ]
  },
  "Dashboard — mono\\monosemy.md": {
    "primary": "The condition of having only one meaning; absence of polysemy or semantic ambiguity.",
    "secondary": "In linguistics and technical writing, the property of words whose semantic range is restricted to a unique referent.",
    "quotes": [
      {
        "author": "Umberto Eco",
        "work": "The Search for the Perfect Language",
        "quote": "Philosophers dreamed of an ideal universal language where absolute **monosemy** would prevent all theological disputes."
      },
      {
        "author": "Noam Chomsky",
        "work": "Aspects of the Theory of Syntax",
        "quote": "While computer programming languages demand strict **monosemy**, natural human languages thrive on generative polysemy."
      },
      {
        "author": "George Steiner",
        "work": "After Babel",
        "quote": "Rigid **monosemy** belongs to the cold precision of algebra, whereas poetic speech derives vitality from semantic multiplicity."
      }
    ]
  },
  "Dashboard — mono\\monosomy.md": {
    "primary": "The condition of having a single copy of a chromosome in a diploid cell, rather than the normal homologous pair.",
    "secondary": "In medical genetics, an aneuploidy resulting from nondisjunction, exemplified in humans by Turner syndrome (monosomy X).",
    "quotes": [
      {
        "author": "Siddhartha Mukherjee",
        "work": "The Gene: An Intimate History",
        "quote": "Autosomal **monosomy** is almost universally lethal during embryonic development, with Turner syndrome being the sole viable human exception."
      },
      {
        "author": "Francis Crick",
        "work": "What Mad Pursuit",
        "quote": "Meiotic nondisjunction during gametogenesis produces gametes with missing chromosomes, leading to embryonic **monosomy**."
      },
      {
        "author": "Max Wintrobe",
        "work": "Clinical Hematology",
        "quote": "Cytogenetic karyotyping revealed a clone characterized by **monosomy** 7, heralding aggressive myelodysplastic syndrome."
      }
    ]
  },
  "Dashboard — mono\\monosyllabic.md": {
    "primary": "Consisting of a single syllable; or using very brief, blunt words in speech.",
    "secondary": "Describing laconic, terse communication or languages (such as Old English or Classical Chinese) rich in single-syllable morphemes.",
    "quotes": [
      {
        "author": "George Orwell",
        "work": "1984",
        "quote": "Newspeak vocabulary was deliberately constructed to become increasingly **monosyllabic**, clipping nuance out of thought."
      },
      {
        "author": "Arthur Conan Doyle",
        "work": "The Adventure of the Speckled Band",
        "quote": "Dr. Roylott gave a harsh, **monosyllabic** grunt as he slammed the heavy iron poker across the hearth."
      },
      {
        "author": "Virginia Woolf",
        "work": "To the Lighthouse",
        "quote": "Mr. Ramsay sat staring at the carpet, answering every query with a bleak, **monosyllabic** murmur."
      }
    ]
  },
  "Dashboard — mono\\monosyllabically.md": {
    "primary": "In a monosyllabic manner; using single syllables or curt, brief utterances.",
    "secondary": "Speaking in a terse, uncommunicative, or laconic fashion.",
    "quotes": [
      {
        "author": "Charles Dickens",
        "work": "Great Expectations",
        "quote": "Pip answered **monosyllabically**, dreading to reveal the secret fear that haunted his conscience."
      },
      {
        "author": "Thomas Hardy",
        "work": "The Mayor of Casterbridge",
        "quote": "Henchard replied **monosyllabically** to the mayor's courteous greeting, his pride wounded by public scrutiny."
      },
      {
        "author": "Joseph Conrad",
        "work": "Lord Jim",
        "quote": "The taciturn skipper answered **monosyllabically**, spitting tobacco over the rail into the turbid harbor waters."
      }
    ]
  },
  "Dashboard — mono\\monosyllable.md": {
    "primary": "A word consisting of only one syllable.",
    "secondary": "In stylistics and phonetics, a single-pulse vocal unit that lends directness, force, or brusqueness to prose.",
    "quotes": [
      {
        "author": "Alexander Pope",
        "work": "An Essay on Criticism",
        "quote": "And ten low words oft creep in one dull line, / Where feeble expletives their aid do join, / And ten dull words each **monosyllable** confine."
      },
      {
        "author": "George Orwell",
        "work": "Politics and the English Language",
        "quote": "Clear English writers prefer the forceful Anglo-Saxon **monosyllable** over grandiloquent Latinate jargon."
      },
      {
        "author": "Samuel Johnson",
        "work": "The Idler",
        "quote": "The rustic replied with an uncouth **monosyllable**, knowing no finer terms to express his stubborn assent."
      }
    ]
  },
  "Dashboard — mono\\monotheism.md": {
    "primary": "The doctrine or belief that there is only one God.",
    "secondary": "In religious history, the theological paradigm characteristic of Judaism, Christianity, and Islam, contrasting with polytheism and pantheism.",
    "quotes": [
      {
        "author": "Karen Armstrong",
        "work": "A History of God",
        "quote": "The emergence of ethical **monotheism** required worshippers to identify the ultimate reality with universal justice."
      },
      {
        "author": "Sigmund Freud",
        "work": "Moses and Monotheism",
        "quote": "Akhenaten's revolutionary solar cult introduced the earliest historical experiment in strict institutional **monotheism**."
      },
      {
        "author": "Max Weber",
        "work": "The Sociology of Religion",
        "quote": "Prophetic **monotheism** disenchanted the natural world by subordinating all sacred spirits to one transcendent Creator."
      }
    ]
  },
  "Dashboard — mono\\monotheist.md": {
    "primary": "A person who believes in or advocates monotheism.",
    "secondary": "In comparative religion, an adherent of an Abrahamic or unitary theological faith that acknowledges one supreme deity.",
    "quotes": [
      {
        "author": "Baruch Spinoza",
        "work": "Tractatus Theologico-Politicus",
        "quote": "The devout **monotheist** perceives all natural occurrences as direct expressions of divine sovereign will."
      },
      {
        "author": "Edward Gibbon",
        "work": "The Decline and Fall of the Roman Empire",
        "quote": "The fervent zeal of the early Christian **monotheist** rejected even the most token civic sacrifice to pagan idols."
      },
      {
        "author": "Karen Armstrong",
        "work": "The Great Transformation",
        "quote": "The ancient Hebrew **monotheist** struggled against the perennial lure of neighboring Canaanite fertility shrines."
      }
    ]
  },
  "Dashboard — mono\\monotheistic.md": {
    "primary": "Believing in or relating to the belief that there is only one God.",
    "secondary": "Characterized by theological unitary worship, ethical commandment, and transcendence across historical faiths.",
    "quotes": [
      {
        "author": "David Hume",
        "work": "The Natural History of Religion",
        "quote": "A **monotheistic** creed naturally tends toward intolerance against external pantheons, claiming absolute exclusive truth."
      },
      {
        "author": "Max Weber",
        "work": "The Protestant Ethic and the Spirit of Capitalism",
        "quote": "The intense inner-worldly asceticism of Calvinism represented the culmination of a long **monotheistic** tradition."
      },
      {
        "author": "Karen Armstrong",
        "work": "Holy War",
        "quote": "All three great **monotheistic** traditions trace their spiritual ancestry back to Abraham's desert journey."
      }
    ]
  },
  "Dashboard — mono\\monothelitism.md": {
    "primary": "A seventh-century Christian heresy maintaining that Jesus Christ had two natures (divine and human) but only one divine-human will.",
    "secondary": "In church history, an imperial Byzantine compromise promoted by Emperor Heraclius to bridge Chalcedonian orthodoxy and Monophysitism, condemned at the Third Council of Constantinople (680–681).",
    "quotes": [
      {
        "author": "Edward Gibbon",
        "work": "The Decline and Fall of the Roman Empire",
        "quote": "The obscure controversy of **Monothelitism** agitated the Byzantine court until condemned by the sixth ecumenical council."
      },
      {
        "author": "John Henry Newman",
        "work": "An Essay on the Development of Christian Doctrine",
        "quote": "The subtle formula of **Monothelitism** attempted to secure theological peace at the expense of Christ's genuine human will."
      },
      {
        "author": "Jaroslav Pelikan",
        "work": "The Christian Tradition: The Spirit of Eastern Christendom",
        "quote": "Maximus the Confessor endured mutilation rather than subscribe to the imperial doctrine of **Monothelitism**."
      }
    ]
  },
  "Dashboard — mono\\monotonic.md": {
    "primary": "Uttered or sounding in a monotone; unvarying in pitch or cadence.",
    "secondary": "In mathematics, describing a function or sequence that either entirely never increases or never decreases throughout its domain.",
    "quotes": [
      {
        "author": "G.H. Hardy",
        "work": "A Course of Pure Mathematics",
        "quote": "Every bounded **monotonic** sequence of real numbers converges necessarily to a unique finite limit."
      },
      {
        "author": "Claude Shannon",
        "work": "A Mathematical Theory of Communication",
        "quote": "Information entropy exhibits a **monotonic** increase under transformations that discard discriminative signal data."
      },
      {
        "author": "Oliver Sacks",
        "work": "The Island of the Colorblind",
        "quote": "The motor drone was flat and **monotonic**, lulling the boat passengers into a hypnotic afternoon trance."
      }
    ]
  },
  "Dashboard — mono\\monotonous.md": {
    "primary": "Dull, tedious, and repetitious; lacking in variety and interest.",
    "secondary": "Sounding or spoken in an unchanging tone, cadence, or pitch.",
    "quotes": [
      {
        "author": "Charles Dickens",
        "work": "Hard Times",
        "quote": "Coketown was a town of machinery and tall chimneys, out of which interminable serpents of smoke trailed in a **monotonous** rhythm."
      },
      {
        "author": "Herman Melville",
        "work": "Bartleby, the Scrivener",
        "quote": "Bartleby copied day after day in the **monotonous** silence of his partitioned corner behind the folding screen."
      },
      {
        "author": "Henry David Thoreau",
        "work": "Walden",
        "quote": "The wood thrush's song broke through the **monotonous** buzz of midday cicadas with sublime woodland serenity."
      }
    ]
  },
  "Dashboard — mono\\monotonously.md": {
    "primary": "In a dull, unvarying, or repetitious manner.",
    "secondary": "With unchanging pitch, cadence, or activity, producing boredom or weariness.",
    "quotes": [
      {
        "author": "Edgar Allan Poe",
        "work": "The Tell-Tale Heart",
        "quote": "The old man's heart beat on **monotonously**, with a dull, muffled sound like a watch enveloped in cotton."
      },
      {
        "author": "Joseph Conrad",
        "work": "Heart of Darkness",
        "quote": "The paddles splashed **monotonously** in the muddy stream as the jungle crept past in endless green banks."
      },
      {
        "author": "Thomas Hardy",
        "work": "Tess of the d'Urbervilles",
        "quote": "The threshing machine hummed **monotonously** in the November mist, devouring sheaf after sheaf of grain."
      }
    ]
  },
  "Dashboard — mono\\monotony.md": {
    "primary": "Lack of variety and interest; tedious repetition and routine.",
    "secondary": "Sameness of tone or pitch in speech, sound, or artistic composition.",
    "quotes": [
      {
        "author": "Oscar Wilde",
        "work": "The Picture of Dorian Gray",
        "quote": "To escape the dreadful **monotony** of London drawing rooms, Dorian sought out strange sins and curious arts."
      },
      {
        "author": "Mary Shelley",
        "work": "Frankenstein",
        "quote": "The unbroken **monotony** of our voyage across the Arctic ice was interrupted by the appearance of the gigantic wanderer."
      },
      {
        "author": "Adam Smith",
        "work": "The Wealth of Nations",
        "quote": "The man whose life is spent performing a few simple operations naturally suffers a mental **monotony** that enervates his spirit."
      }
    ]
  },
  "Dashboard — mono\\monotremata.md": {
    "primary": "The mammalian order consisting of egg-laying mammals, comprising the platypus and echidnas.",
    "secondary": "In systematic zoology, an ancient mammalian clade characterized by oviparity, a cloaca, and absence of nipples (milk secreted onto skin).",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "Manual of the Anatomy of Vertebrated Animals",
        "quote": "The order **Monotremata** bridges the reptilian osteology of the shoulder girdle with mammalian lactation and fur."
      },
      {
        "author": "Richard Dawkins",
        "work": "The Ancestor's Tale",
        "quote": "Our common ancestor with the **Monotremata** takes us back more than one hundred and sixty million years to Gondwana."
      },
      {
        "author": "David Attenborough",
        "work": "The Life of Mammals",
        "quote": "The platypus and echidna, sole survivors of the order **Monotremata**, demonstrate how ancient mammals reproduced before the evolution of the placenta."
      }
    ]
  },
  "Dashboard — mono\\monotreme.md": {
    "primary": "A mammal of the order Monotremata, which reproduces by laying eggs rather than giving birth to live young (such as the platypus or echidna).",
    "secondary": "In comparative anatomy, a primitive prototherian mammal possessing a single cloacal exit for digestive, excretory, and reproductive systems.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "The living **monotreme** is a wonderful living fossil, connecting the great classes of mammals and reptiles across immense geological time."
      },
      {
        "author": "Richard Dawkins",
        "work": "The Blind Watchmaker",
        "quote": "When European naturalists first received the skin of the egg-laying **monotreme**, they denounced it as a Chinese taxidermic hoax."
      },
      {
        "author": "David Attenborough",
        "work": "Life on Earth",
        "quote": "No other living creature combines fur, a duck-like bill, and reptilian oviparity like Australia's curious **monotreme**."
      }
    ]
  },
  "Dashboard — mono\\monotropa.md": {
    "primary": "A genus of mycoheterotrophic herbaceous plants in the family Ericaceae, notably Monotropa uniflora (Indian pipe or ghost plant).",
    "secondary": "In botanical ecology, achlorophyllous plants that obtain all nutrients by parasitizing mycorrhizal fungi connected to nearby forest trees.",
    "quotes": [
      {
        "author": "Emily Dickinson",
        "work": "Letters of Emily Dickinson",
        "quote": "I send you the ghostly **Monotropa**, the Indian pipe of our autumn woods, translucent as carved alabaster."
      },
      {
        "author": "Henry David Thoreau",
        "work": "The Maine Woods",
        "quote": "In the damp pine duff beneath ancient hemlocks grew clusters of wax-white **Monotropa**, nodding like fairy lanterns."
      },
      {
        "author": "Asa Gray",
        "work": "Manual of the Botany of the Northern United States",
        "quote": "Plants of the genus **Monotropa** are entirely devoid of green chlorophyll, subsisting as saprophytes upon rich fungal humus."
      }
    ]
  },
  "Dashboard — mono\\monotropaceae.md": {
    "primary": "A former family of non-green, saprophytic or mycoheterotrophic plants, now classified as a subfamily (Monotropoideae) within Ericaceae.",
    "secondary": "In taxonomic botany, fleshy parasitic forest plants (including Indian pipe and pine-drops) characterized by lack of chlorophyll and mycorrhizal dependence.",
    "quotes": [
      {
        "author": "Asa Gray",
        "work": "Structural Botany",
        "quote": "The strange woodland parasites formerly placed in **Monotropaceae** derive their sustenance through intricate underground fungal partnerships."
      },
      {
        "author": "Joseph Dalton Hooker",
        "work": "The Flora of British India",
        "quote": "Collectors in temperate Himalayan pine forests discovered rare members of **Monotropaceae** emerging through fallen needle beds."
      },
      {
        "author": "Peter Raven",
        "work": "Biology of Plants",
        "quote": "DNA sequencing confirmed that the achlorophyllous **Monotropaceae** evolved directly from photosynthetic ericaceous ancestors like blueberries."
      }
    ]
  },
  "Dashboard — mono\\monotype.md": {
    "primary": "A printing process in which each character is cast as a separate piece of type, invented by Tolbert Lanston; or a unique print made by drawing on a plate.",
    "secondary": "In typography and printing history, a hot-metal typesetting system that cast individual lead sorts, allowing effortless single-letter correction.",
    "quotes": [
      {
        "author": "Stanley Morison",
        "work": "A Tally of Types",
        "quote": "The precision of the **Monotype** caster revived classical Renaissance typefaces with unmatched typographic crispness."
      },
      {
        "author": "Edgar Degas",
        "work": "Letters of Degas",
        "quote": "I spent the entire evening working on a greasy ink plate to pull a luminous, painterly **monotype** print."
      },
      {
        "author": "Walter Benjamin",
        "work": "The Work of Art in the Age of Mechanical Reproduction",
        "quote": "The unique artistic **monotype** stands halfway between the singular painting and reproducible lithography."
      }
    ]
  },
  "Dashboard — mono\\monotypic.md": {
    "primary": "Having only one representative; consisting of only one species (in a genus) or one genus (in a family).",
    "secondary": "In biological systematics, designating a taxonomic category that contains only a single subordinate taxon (such as Ginkgo biloba in Ginkgo).",
    "quotes": [
      {
        "author": "Ernst Mayr",
        "work": "Principles of Systematic Zoology",
        "quote": "A **monotypic** genus contains just one recognized species, offering no comparative intrageneric variation."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "The Flamingo's Smile",
        "quote": "The horseshoe crab belongs to an ancient, nearly **monotypic** lineage that has persisted virtually unchanged for hundreds of millions of years."
      },
      {
        "author": "E.O. Wilson",
        "work": "The Diversity of Life",
        "quote": "Island endemics often represent **monotypic** genera that diverged in isolation from continental relatives."
      }
    ]
  },
  "Dashboard — mono\\monounsaturated.md": {
    "primary": "Containing only one double or triple bond between carbon atoms in the fatty acid chain.",
    "secondary": "In biochemistry and clinical nutrition, describing dietary fats (such as oleic acid in olive oil) that promote cardiovascular health.",
    "quotes": [
      {
        "author": "Michael Pollan",
        "work": "In Defense of Food",
        "quote": "The Mediterranean diet is rich in **monounsaturated** fatty acids derived from extra-virgin cold-pressed olive oil."
      },
      {
        "author": "Harold McGee",
        "work": "On Food and Cooking",
        "quote": "Because oleic acid is **monounsaturated**, it remains liquid at room temperature while resisting oxidative rancidity better than polyunsaturated oils."
      },
      {
        "author": "Linus Pauling",
        "work": "How to Live Longer and Feel Better",
        "quote": "Substituting **monounsaturated** fats for industrial trans-fats produces favorable shifts in human serum cholesterol profiles."
      }
    ]
  },
  "Dashboard — mono\\traffic.md": {
    "primary": "The movement of vehicles, ships, pedestrians, aircraft, or data along a designated route or communication network.",
    "secondary": "Commercial trade, exchange, or dealings between individuals, companies, or nations, especially of an illicit or specified nature.",
    "quotes": [
      {
        "author": "William Shakespeare",
        "work": "Romeo and Juliet",
        "quote": "Is now the two hours' **traffic** of our stage; / The which if you with patient ears attend, / What here shall miss, our toil shall strive to mend."
      },
      {
        "author": "Adam Smith",
        "work": "The Wealth of Nations",
        "quote": "The freedom of internal commerce and maritime **traffic** encouraged manufactures to flourish across the kingdom."
      },
      {
        "author": "Herman Melville",
        "work": "Moby-Dick",
        "quote": "The great ocean highway was thronged with the commercial **traffic** of merchantmen and whalers."
      }
    ]
  },
  "Dashboard — mono\\trafficker.md": {
    "primary": "A person who deals or trades in something illegally, such as illicit drugs, weapons, or human beings.",
    "secondary": "In economic history, an archaic term for a merchant, trader, or commercial broker engaged in long-distance maritime barter.",
    "quotes": [
      {
        "author": "Daniel Defoe",
        "work": "Captain Singleton",
        "quote": "He was a shrewd and unscrupulous **trafficker**, bargaining with coastal chieftains for ivory and gold dust."
      },
      {
        "author": "Joseph Conrad",
        "work": "Lord Jim",
        "quote": "The Malay **trafficker** unloaded bags of copra and rattan under the watchful eye of the harbor police."
      },
      {
        "author": "Robert Louis Stevenson",
        "work": "Treasure Island",
        "quote": "The old buccaneer lived like a seasoned **trafficker** of illicit goods, suspicious of every sail that docked."
      }
    ]
  },
  "Dashboard — myri\\myri.md": {
    "primary": "A combining form derived from Greek myrios, meaning countless, myriad, or ten thousand.",
    "secondary": "In classical etymology and scientific nomenclature, the prefix element utilized in myriapod, myriameter, and myriagon.",
    "quotes": [
      {
        "author": "Donald Knuth",
        "work": "The TeXbook",
        "quote": "From the classical Greek root **myri**, mathematicians coined prefixes designating ten thousand or infinite counts."
      },
      {
        "author": "Homer",
        "work": "The Iliad",
        "quote": "A myriad shades, countlessly multiplied from the root **myri**, thronged the dark shores of the Underworld."
      },
      {
        "author": "Edward Sapir",
        "work": "Language",
        "quote": "The morpheme **myri** moved from poetic descriptions of uncountable swarms to precise metric decimal prefixes."
      }
    ]
  },
  "Dashboard — myri\\myria.md": {
    "primary": "An obsolete metric prefix denoting a factor of ten thousand (10^4).",
    "secondary": "In historical metrology, adopted by the revolutionary French metric system in 1795 for units like the myriameter and myriagram before being phased out.",
    "quotes": [
      {
        "author": "Antoine Lavoisier",
        "work": "Elements of Chemistry",
        "quote": "The metric scale introduced **myria** to designate ten thousand fundamental base units with rational decimal consistency."
      },
      {
        "author": "Charles Darwin",
        "work": "The Voyage of the Beagle",
        "quote": "Distances on French maritime charts of the era were frequently noted in units of **myria** meters."
      },
      {
        "author": "Lord Kelvin",
        "work": "Popular Lectures and Addresses",
        "quote": "Although **myria** fell out of common engineering parlance, it stood as a noble early experiment in decimal nomenclature."
      }
    ]
  },
  "Dashboard — myri\\myriagon.md": {
    "primary": "A polygon with 10,000 sides and 10,000 angles.",
    "secondary": "In epistemology and philosophy of mind, a famous example used by René Descartes to distinguish pure intellectual understanding from sensory imagination.",
    "quotes": [
      {
        "author": "René Descartes",
        "work": "Meditations on First Philosophy",
        "quote": "When I imagine a **myriagon**, I do not envision ten thousand sides distinctly as I do with a triangle, yet I understand its mathematical properties perfectly."
      },
      {
        "author": "John Locke",
        "work": "An Essay Concerning Human Understanding",
        "quote": "The mind forms a clear idea of a **myriagon** by arithmetic composition, even though visual imagination cannot portray ten thousand edges."
      },
      {
        "author": "Bertrand Russell",
        "work": "The Problems of Philosophy",
        "quote": "Descartes' discussion of the chiliagon and **myriagon** sharply separates sensory perception from rational mathematical comprehension."
      }
    ]
  },
  "Dashboard — myri\\myriagram.md": {
    "primary": "An obsolete metric unit of mass equal to 10,000 grams or 10 kilograms (approximately 22.046 pounds).",
    "secondary": "In historical European commerce and agriculture, a nineteenth-century standard weight used for bulk commodity trading in France and the Low Countries.",
    "quotes": [
      {
        "author": "Honoré de Balzac",
        "work": "Eugénie Grandet",
        "quote": "The miser Grandet weighed the casks of vintage wine, calculating his profit down to the last **myriagram** of pressed grapes."
      },
      {
        "author": "Antoine Lavoisier",
        "work": "Elements of Chemistry",
        "quote": "Ten thousand standard brass grams constituted the official **myriagram** prototype deposited in the national archives."
      },
      {
        "author": "Thomas Jefferson",
        "work": "Report on Weights and Measures",
        "quote": "The French decimal system proposes decimal mass units scaling from the milligram up to the commercial **myriagram**."
      }
    ]
  },
  "Dashboard — myri\\myriameter.md": {
    "primary": "An obsolete metric unit of length equal to 10,000 meters or 10 kilometers (approximately 6.214 miles).",
    "secondary": "In historical geodetic surveying and cartography, a unit used in early nineteenth-century France to map post roads and canal networks.",
    "quotes": [
      {
        "author": "Jules Verne",
        "work": "Twenty Thousand Leagues Under the Sea",
        "quote": "The submarine navigated beneath the waves, logging another **myriameter** across the uncharted South Pacific trench."
      },
      {
        "author": "Victor Hugo",
        "work": "Les Misérables",
        "quote": "The post chaise rattled over the cobblestones, measuring the weary leagues by each stone marking a **myriameter** toward Paris."
      },
      {
        "author": "Alexander von Humboldt",
        "work": "Cosmos",
        "quote": "The triangulation across the Iberian peninsula surveyed mountain baselines measured with high precision in **myriameter** lengths."
      }
    ]
  },
  "Dashboard — myri\\myriametre.md": {
    "primary": "The British/Commonwealth spelling of myriameter; an obsolete metric unit of length equal to 10,000 metres (10 kilometres).",
    "secondary": "In nineteenth-century European geography and travel writing, a measure equivalent to ten thousand metres.",
    "quotes": [
      {
        "author": "Charles Dickens",
        "work": "Pictures from Italy",
        "quote": "The vetturino plodded across the desolate Roman Campagna, each **myriametre** marked by ancient crumbling aqueducts."
      },
      {
        "author": "William Makepeace Thackeray",
        "work": "Vanity Fair",
        "quote": "The carriage rolled past roadside milestones marking every **myriametre** along the paved route to Brussels."
      },
      {
        "author": "Arthur Young",
        "work": "Travels in France",
        "quote": "The newly surveyed highway unwound smoothly over the rolling hills of Normandy, measured by the **myriametre**."
      }
    ]
  },
  "Dashboard — myri\\myriapod.md": {
    "primary": "An arthropod of the subphylum Myriapoda, having an elongated segmented body with numerous pairs of legs (such as a centipede or millipede).",
    "secondary": "In invertebrate zoology, terrestrial mandibulata adapted to moist leaf litter and soil microhabitats, exhibiting multi-segmented trunk morphology.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Formation of Vegetable Mould through the Action of Worms",
        "quote": "Under every damp log, some creeping **myriapod** worked alongside earthworms to aerate and decompose the woodland mold."
      },
      {
        "author": "Jean-Henri Fabre",
        "work": "The Wonders of Instinct",
        "quote": "The predatory scolopendra, a giant **myriapod**, struck its prey with lightning venomous claws beneath the stones."
      },
      {
        "author": "E.O. Wilson",
        "work": "The Diversity of Life",
        "quote": "The tropical rain forest litter swarms with cryptozoic creatures, among which every multi-legged **myriapod** plays a decomposer role."
      }
    ]
  },
  "Dashboard — myri\\myriapoda.md": {
    "primary": "A subphylum of terrestrial arthropods containing the centipedes, millipedes, symphylans, and pauropods.",
    "secondary": "In systematic zoology, tracheate arthropods characterized by a distinct head with one pair of antennae and numerous homonomous trunk segments.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "Manual of the Anatomy of Invertebrated Animals",
        "quote": "The class **Myriapoda** is distinguished by an undivided trunk composed of numerous uniform rings, each bearing jointed legs."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "Wonderful Life",
        "quote": "Fossils from the Silurian demonstrate that members of **Myriapoda** were among the very first animals to colonize dry land."
      },
      {
        "author": "David Attenborough",
        "work": "Life on Earth",
        "quote": "Before vertebrates ventured from the shallows, armored ancestors of **Myriapoda** were already grazing on primitive mosses."
      }
    ]
  },
  "Dashboard — myri\\myriapodology.md": {
    "primary": "The branch of zoology concerned with the study of myriapods (centipedes, millipedes, and related arthropods).",
    "secondary": "In systematic entomology and invertebrate natural history, the academic specialty devoted to the taxonomy, morphology, and ecology of Myriapoda.",
    "quotes": [
      {
        "author": "E.O. Wilson",
        "work": "Naturalist",
        "quote": "Pioneering specialists in **myriapodology** spent lifetimes sorting millipedes from Appalachian leaf litter into exquisite taxonomic monographs."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "The Lying Stones of Marrakech",
        "quote": "The modest curator made seminal contributions to **myriapodology**, naming dozens of blind cavernicolous centipedes."
      },
      {
        "author": "Jean-Henri Fabre",
        "work": "More Hunting Wasps",
        "quote": "His meticulous field observations in **myriapodology** elucidated the predatory techniques of subterranean scolopendrids."
      }
    ]
  },
  "Dashboard — myri\\myrica.md": {
    "primary": "A genus of about 35–50 species of small trees and shrubs in the family Myricaceae, commonly known as bayberries or sweet gales.",
    "secondary": "In economic and ecological botany, actinorhizal shrubs bearing aromatic waxy berries traditionally boiled to make scented bayberry candles.",
    "quotes": [
      {
        "author": "Henry David Thoreau",
        "work": "Cape Cod",
        "quote": "The sandy barrens were clothed in fragrant thickets of **Myrica**, whose waxy berries yielded the aromatic candles of the early colonists."
      },
      {
        "author": "William Bartram",
        "work": "Travels through North and South Carolina, Georgia, East and West Florida",
        "quote": "We rode through aromatic groves of **Myrica** cerifera, whose crushed leaves perfumed the southern breeze."
      },
      {
        "author": "Asa Gray",
        "work": "Manual of Botany",
        "quote": "The bog-loving shrub **Myrica** gale bears resinous fragrant catkins and thrives in acidic northern peat."
      }
    ]
  },
  "Dashboard — myri\\myricaceae.md": {
    "primary": "The bayberry family, a small family of dicotyledonous shrubs and small trees characterized by aromatic leaves and waxy fruits.",
    "secondary": "In plant systematics, wind-pollinated, nitrogen-fixing woody plants bearing symbiotic Frankia bacteria in specialized root nodules.",
    "quotes": [
      {
        "author": "Asa Gray",
        "work": "Manual of the Botany of the Northern United States",
        "quote": "Plants of the family **Myricaceae** are distinguished by resinous dots on their leaves and small drupes coated with aromatic wax."
      },
      {
        "author": "Joseph Dalton Hooker",
        "work": "The Flora of British India",
        "quote": "Subtropical montane forests harbored hardy representatives of **Myricaceae**, whose astringent bark was utilized in tanning."
      },
      {
        "author": "Peter Raven",
        "work": "Biology of Plants",
        "quote": "Nitrogen-fixing symbioses in **Myricaceae** allow these pioneering shrubs to colonize barren sand dunes and degraded slopes."
      }
    ]
  },
  "Dashboard — myri\\myricales.md": {
    "primary": "An order of dicotyledonous plants in older taxonomic systems, containing the single family Myricaceae (bayberries).",
    "secondary": "In classical botanical taxonomy (such as the Cronquist system), an amentiferous order of wind-pollinated woody shrubs and trees.",
    "quotes": [
      {
        "author": "Asa Gray",
        "work": "Structural Botany",
        "quote": "Traditional systems placed the catkin-bearing bayberries within the separate order **Myricales**."
      },
      {
        "author": "Arthur Cronquist",
        "work": "An Integrated System of Classification of Flowering Plants",
        "quote": "The order **Myricales** is defined by its simple unisexual flowers arranged in dense catkins and drupaceous fruits."
      },
      {
        "author": "Peter Raven",
        "work": "Biology of Plants",
        "quote": "Molecular phylogenetics dissolved **Myricales**, placing the bayberry family squarely within the expanded order Fagales."
      }
    ]
  },
  "Dashboard — myri\\myricaria.md": {
    "primary": "A genus of flowering plants in the family Tamaricaceae (false tamarisks), native to Eurasia.",
    "secondary": "In riparian botany and alpine ecology, pioneer gravel-bed shrubs characterized by slender willow-like leaves, pink racemes, and deep root systems.",
    "quotes": [
      {
        "author": "Alexander von Humboldt",
        "work": "Views of Nature",
        "quote": "Along the gravel bars of glacial meltwater rivers grew feathery clumps of **Myricaria**, resisting torrential spring floods."
      },
      {
        "author": "Joseph Dalton Hooker",
        "work": "Himalayan Journals",
        "quote": "In the stony bed of the upper Teesta river, we found dense thickets of pink-flowered **Myricaria** growing among the boulders."
      },
      {
        "author": "Theophrastus",
        "work": "Enquiry into Plants",
        "quote": "The shrub resembling the tamarisk, known as **Myricaria**, flourishes where winter torrents deposit fresh gravel."
      }
    ]
  },
  "Dashboard — myri\\myringa.md": {
    "primary": "The tympanic membrane or eardrum (from New Latin myringa, akin to Greek myrinx).",
    "secondary": "In otology and clinical anatomy, the thin, semitransparent membrane separating the external auditory canal from the middle ear cavity.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Otoscopic inspection revealed bright erythema and bulging of the **myringa**, indicating acute suppurative otitis media."
      },
      {
        "author": "Oliver Wendell Holmes Sr.",
        "work": "Medical Essays",
        "quote": "The delicate vibration of the **myringa** conveys acoustic pressure waves across the tiny ossicular chain of the ear."
      },
      {
        "author": "Abraham Verghese",
        "work": "Cutting for Stone",
        "quote": "He peered through the otoscope, noting the healthy pearly-grey sheen and sharp light reflex of the patient's **myringa**."
      }
    ]
  },
  "Dashboard — myri\\myringectomy.md": {
    "primary": "Surgical excision or partial removal of the tympanic membrane (eardrum).",
    "secondary": "In otolaryngologic surgery, a procedure historically performed to clear middle ear cholesteatoma or intractable chronic mucosal pathology.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "In cases of extensive necrotizing infection, a formal **myringectomy** was sometimes unavoidable to drain deep middle-ear abscesses."
      },
      {
        "author": "Atul Gawande",
        "work": "Complications: A Surgeon's Notes on an Imperfect Science",
        "quote": "Before micro-reconstructive techniques advanced, radical **myringectomy** often left patients with permanent conductive hearing deficits."
      },
      {
        "author": "Abraham Verghese",
        "work": "Cutting for Stone",
        "quote": "The otolaryngologist discussed whether conservative myringotomy or complete **myringectomy** was indicated for the recurrent middle ear lesion."
      }
    ]
  }
};

const count = updateNotesBatch(CLUSTER_DIR, batchData);
console.log(`========================================`);
console.log(`Math Part 2 - Batch 5 Completed: ${count} / ${Object.keys(batchData).length} words updated`);
console.log(`========================================`);
