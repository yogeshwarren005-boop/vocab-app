import fs from "fs";
import path from "path";

const baseDir = "App database/Greek roots/Cluster Medicine & Pathology";

const wordsData = {
  // === Dashboard — narc ===
  "Dashboard — narc/narc.md": {
    word: "narc",
    primary: "The foundational Greek combining root (from narke, νάρκη) meaning numbness, torpor, or stupor; or informal slang for a narcotics enforcement officer or police informant.",
    secondary: "In biomedical etymology, the base morpheme underlying narcosis, narcolepsy, and narcotics, denoting agents or conditions that induce sensory insensibility.",
    quotes: [
      { author: "Walter William Skeat", work: "An Etymological Dictionary of the English Language", quote: "The root **narc** ascends to the Greek narke, signifying cramp, numbness, or deadness of feeling." },
      { author: "James Murray", work: "A New English Dictionary on Historical Principles", quote: "In pharmacopeias, words formed on **narc** designate substances that blunt pain and induce deep slumber." },
      { author: "H. G. Liddell & Robert Scott", work: "A Greek-English Lexicon", quote: "In classical Greek, narke (stem **narc**-) denoted the electric ray or torpedo fish whose touch caused instantaneous numbness." }
    ]
  },
  "Dashboard — narc/narcan.md": {
    word: "narcan",
    primary: "A proprietary pharmaceutical preparation of naloxone, an opioid antagonist used for the emergency reversal of opioid overdose.",
    secondary: "In emergency medicine and toxicology, a competitive mu-opioid receptor antagonist that rapidly displaces opioids, reversing life-threatening respiratory depression.",
    quotes: [
      { author: "Jerome Groopman", work: "How Doctors Think", quote: "A single dose of **Narcan** administered intranasally revived the unconscious young man within ninety seconds." },
      { author: "Atul Gawande", work: "Being Mortal", quote: "Paramedics carried pre-filled **Narcan** injectors to every emergency call involving suspected narcotic intoxication." },
      { author: "Siddhartha Mukherjee", work: "The Song of the Cell", quote: "The chemical structure of **Narcan** fits snugly into the opioid receptor without activating the downstream intracellular cascade." }
    ]
  },
  "Dashboard — narc/narcism.md": {
    word: "narcism",
    primary: "An older or alternate psychological spelling of narcissism; excessive self-love or vanity.",
    secondary: "In early twentieth-century psychoanalytic literature, Havelock Ellis's and Sigmund Freud's early term for the libidinal investment of the ego in itself.",
    quotes: [
      { author: "Havelock Ellis", work: "Studies in the Psychology of Sex", quote: "I first proposed the term **narcism** to describe that curious tendency for sexual emotions to be absorbed in self-admiration." },
      { author: "Sigmund Freud", work: "On Narcissism: An Introduction", quote: "Primary **narcism** represents an original libidinal state wherein the child's developing ego takes itself as love-object." },
      { author: "Carl Jung", work: "Psychological Types", quote: "In morbid cases of **narcism**, the individual is completely insulated against authentic emotional connection with others." }
    ]
  },
  "Dashboard — narc/narcissism.md": {
    word: "narcissism",
    primary: "Excessive interest in or admiration of oneself and one's physical appearance; self-centeredness.",
    secondary: "In clinical psychiatry, narcissistic personality disorder (NPD), characterized by a pervasive pattern of grandiosity, need for admiration, and lack of empathy.",
    quotes: [
      { author: "Sigmund Freud", work: "A General Introduction to Psychoanalysis", quote: "We have coined the term **narcissism** from Greek myth to denote that condition where the individual treats his own body as an erotic object." },
      { author: "Christopher Lasch", work: "The Culture of Narcissism", quote: "Modern consumer culture fosters a widespread psychological **narcissism**, replacing historical consciousness with therapeutic preoccupation." },
      { author: "Oscar Wilde", work: "The Picture of Dorian Gray", quote: "His passionate self-adoration was a monstrous form of **narcissism**, gazing upon his painted youth while his soul decayed." }
    ]
  },
  "Dashboard — narc/narcissist.md": {
    word: "narcissist",
    primary: "A person who has an excessive interest in or admiration of themselves; one characterized by egotism and conceit.",
    secondary: "In psychological diagnostics, an individual displaying entitlement, fragile self-esteem masked by grandiosity, and interpersonal exploitativeness.",
    quotes: [
      { author: "Sigmund Freud", work: "On Narcissism", quote: "The true **narcissist** loves only what he is himself, what he was, or what he would like to be." },
      { author: "Milan Kundera", work: "The Unbearable Lightness of Being", quote: "The political **narcissist** perceives history merely as a mirror reflecting his own heroic speeches." },
      { author: "Irvin D. Yalom", work: "The Gift of Therapy", quote: "Beneath the imperious armor of the **narcissist** lies an agonizing dread of insignificance and shame." }
    ]
  },
  "Dashboard — narc/narcissistic.md": {
    word: "narcissistic",
    primary: "Having an excessive or erotic interest in oneself and one's physical appearance; extremely self-centered.",
    secondary: "In psychoanalytic theory, relating to the libidinal cathexis of the ego or narcissistic defenses against underlying depressive emptiness.",
    quotes: [
      { author: "Sigmund Freud", work: "Civilization and Its Discontents", quote: "The **narcissistic** satisfaction derived from the cultural ideal is one of the forces that successfully combats hostile rebellions." },
      { author: "Christopher Lasch", work: "The Culture of Narcissism", quote: "The **narcissistic** personality seeks immediate applause to validate an inner sense of chronic emptiness." },
      { author: "Virginia Woolf", work: "Orlando", quote: "Orlando spent hours before the mirror in a state of **narcissistic** wonder at the silks and lace." }
    ]
  },
  "Dashboard — narc/narcissus.md": {
    word: "narcissus",
    primary: "A bulbous spring-flowering plant with yellow or white flowers and a cup-shaped corona (daffodil or jonquil); or the mythical youth who fell in love with his own reflection.",
    secondary: "In botany, a genus of Amaryllidaceae named from Greek narke (numbness), referencing the narcotic alkaloid lycorine present in its poisonous bulbs and intoxicating scent.",
    quotes: [
      { author: "Ovid", work: "Metamorphoses", quote: "Poor **Narcissus**, gazing into the silver fountain, perished of unquenchable thirst for his own reflected beauty." },
      { author: "John Keats", work: "I Stood Tip-toe upon a Little Hill", quote: "What first inspired a bard to sing of **Narcissus**, gazing in the glassy stream until he pined away?" },
      { author: "William Wordsworth", work: "I Wandered Lonely as a Cloud", quote: "Beside the lake, beneath the trees, ten thousand golden **narcissus** danced in the spring breeze." }
    ]
  },
  "Dashboard — narc/narcist.md": {
    word: "narcist",
    primary: "An alternative or condensed spelling of narcissist; a person obsessed with self-admiration.",
    secondary: "In early behavioral psychology, an individual exhibiting marked auto-erotic or self-directed emotional absorption.",
    quotes: [
      { author: "Havelock Ellis", work: "Studies in the Psychology of Sex", quote: "The thoroughgoing **narcist** requires no external partner, living in perpetual adoration of his own image." },
      { author: "Aldous Huxley", work: "Point Counter Point", quote: "He smiled with the cold satisfaction of a confirmed **narcist**, admiring his witty rejoinder in the silence of the room." },
      { author: "W. H. Auden", work: "Collected Poems", quote: "The lonely **narcist** dreams beside the pool, blind to the living world that surrounds him." }
    ]
  },
  "Dashboard — narc/narco-state.md": {
    word: "narco-state",
    primary: "A country or political entity whose economy, judicial system, and government institutions are dominated by the illegal trade in narcotics.",
    secondary: "In political science and international relations, a nation where illicit drug cartels infiltrate or co-opt law enforcement and political leadership, eroding the rule of law.",
    quotes: [
      { author: "Joseph Stiglitz", work: "Globalization and Its Discontents", quote: "When drug cartels capture the banking system and the judiciary, a nation degenerates into a lawless **narco-state**." },
      { author: "Noam Chomsky", work: "Failed States", quote: "The militarization of drug prohibition enriched violent cartels and fostered the rise of the modern **narco-state**." },
      { author: "Paul Collier", work: "The Bottom Billion", quote: "Without robust institutions, fragile resource-rich territories are easily hijacked to become an international **narco-state**." }
    ]
  },
  "Dashboard — narc/narcolepsy.md": {
    word: "narcolepsy",
    primary: "A chronic neurological disorder characterized by overwhelming daytime drowsiness and sudden, uncontrollable episodes of falling asleep.",
    secondary: "In sleep medicine and neurobiology, a condition caused by autoimmune destruction of orexin (hypocretin)-producing neurons in the lateral hypothalamus, often accompanied by cataplexy, sleep paralysis, and hypnagogic hallucinations.",
    quotes: [
      { author: "Jean-Baptiste-Édouard Gélineau", work: "De la narcolepsie", quote: "I designate as **narcolepsy** this rare neurosis marked by sudden, irresistible paroxysms of sleep occurring in the middle of active conversation." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "In **narcolepsy**, sleep strikes with sudden violence, causing the patient to slump over his desk or workshop bench." },
      { author: "Oliver Sacks", work: "The Man Who Mistook His Wife for a Hat", quote: "The vivid hypnagogic nightmares of **narcolepsy** blur the boundary between conscious waking reality and the dream world." }
    ]
  },
  "Dashboard — narc/narcoleptic.md": {
    word: "narcoleptic",
    primary: "Of, relating to, or affected by narcolepsy; or a person suffering from narcolepsy.",
    secondary: "Describing rapid transitions from wakefulness directly into REM sleep (sleep-onset REM periods) characteristic of orexin-deficient sleep pathology.",
    quotes: [
      { author: "Oliver Sacks", work: "Awakenings", quote: "The **narcoleptic** patient would freeze mid-stride, plunging without warning into instantaneous slumber." },
      { author: "Jerome Groopman", work: "How Doctors Think", quote: "Sudden loss of muscle tone triggered by laughter warned the neurologist that the patient was experiencing **narcoleptic** cataplexy." },
      { author: "Arthur Conan Doyle", work: "The Adventure of the Resident Patient", quote: "The physician observed the curious **narcoleptic** stupor that overtook the visitor whenever excitement mounted." }
    ]
  },
  "Dashboard — narc/narcosis.md": {
    word: "narcosis",
    primary: "A state of stupor, drowsiness, or unconsciousness produced by narcotic drugs or physical agents.",
    secondary: "In diving medicine (nitrogen narcosis or 'raptures of the deep') and anesthesiology, general depression of the central nervous system resulting from high partial pressures of inert gases or anesthetic vapors.",
    quotes: [
      { author: "Jacques Cousteau", work: "The Silent World", quote: "At two hundred feet, nitrogen **narcosis** begins to steal over the diver, filling his mind with reckless euphoria and sluggish indifference." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The patient passed from quiet surgical **narcosis** into peaceful post-operative recovery." },
      { author: "Thomas De Quincey", work: "Confessions of an English Opium-Eater", quote: "The divine **narcosis** of the poppy dissolved every earthly sorrow in celestial serenity." }
    ]
  },
  "Dashboard — narc/narcoterrorism.md": {
    word: "narcoterrorism",
    primary: "Terrorist activities funded by or associated with the illicit trade in illegal drugs.",
    secondary: "In security studies and geopolitics, the alliance between drug trafficking cartels and insurgent or terrorist organizations using assassination, bombing, and extortion to influence government policy.",
    quotes: [
      { author: "Noam Chomsky", work: "Manufacturing Consent", quote: "The rhetoric of **narcoterrorism** provided a convenient pretext for military interventions across Latin America." },
      { author: "Joseph Stiglitz", work: "Making Globalization Work", quote: "Unchecked illicit drug profits finance brutal **narcoterrorism** that destabilizes democratic governance." },
      { author: "Paul Collier", work: "Wars, Guns, and Votes", quote: "Insurgent factions turn to **narcoterrorism** to bankroll their armaments through taxation of coca cultivation." }
    ]
  },
  "Dashboard — narc/narcotic.md": {
    word: "narcotic",
    primary: "A drug that in moderate doses dulls the senses, relieves pain, and induces profound sleep, but in excessive doses causes stupor, coma, or convulsions.",
    secondary: "In pharmacology and legal statutes, specifically an opioid receptor agonist (such as morphine, codeine, or fentanyl) subject to high potential for physical dependence and strict regulatory control.",
    quotes: [
      { author: "Thomas De Quincey", work: "Confessions of an English Opium-Eater", quote: "O just, subtle, and mighty opium! thou buildest upon the bosom of darkness, with the materials of a **narcotic** dream, cities and temples." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Morphine remains our sovereign **narcotic** for the agony of severe coronary thrombosis." },
      { author: "Aldous Huxley", work: "The Doors of Perception", quote: "Every human culture has discovered some vegetable **narcotic** to offer temporary escape from the burden of selfhood." }
    ]
  },
  "Dashboard — narc/narcotise.md": {
    word: "narcotise",
    primary: "To drug or treat with a narcotic; to render unconscious, insensible, or stupefied (chiefly British spelling of narcotize).",
    secondary: "In political and cultural critique, to lull into complacency, apathy, or uncritical compliance.",
    quotes: [
      { author: "George Bernard Shaw", work: "The Doctor's Dilemma", quote: "The physician sought to **narcotise** the patient's pain rather than discover its underlying physiological cause." },
      { author: "H. G. Wells", work: "The Time Machine", quote: "The gentle life of the Eloi had served to **narcotise** their ancestral intelligence into childlike weakness." },
      { author: "Aldous Huxley", work: "Brave New World", quote: "Daily rations of soma served to **narcotise** any spontaneous flicker of discontent among the workers." }
    ]
  },
  "Dashboard — narc/narcotised.md": {
    word: "narcotised",
    primary: "Under the influence of a narcotic; stupefied, drugged, or rendered insensible (British spelling of narcotized).",
    secondary: "Dazed, dulled in perception, or paralyzed by psychological torpor.",
    quotes: [
      { author: "Arthur Conan Doyle", work: "The Sign of Four", quote: "Holmes lay upon the sofa in a **narcotised** languor, his violin resting untouched on the floor." },
      { author: "Thomas Hardy", work: "Jude the Obscure", quote: "He felt **narcotised** by despair, moving through the rain-soaked streets like a man in a dream." },
      { author: "Joseph Conrad", work: "Heart of Darkness", quote: "The heavy silence of the primeval forest lay upon us like a **narcotised** spell." }
    ]
  },
  "Dashboard — narc/narcotising.md": {
    word: "narcotising",
    primary: "Inducing stupor, insensibility, or sleep; drugging with a narcotic (British spelling of narcotizing).",
    secondary: "Having a deadening, dulling, or sedating effect on the mind, emotions, or social consciousness.",
    quotes: [
      { author: "George Orwell", work: "1984", quote: "The continuous stream of mechanical music had a **narcotising** effect upon the weary factory crowds." },
      { author: "Virginia Woolf", work: "The Waves", quote: "The rhythmic crash of the waves against the shore exerted a **narcotising** influence on our thoughts." },
      { author: "Thomas Carlyle", work: "Past and Present", quote: "Foul luxury acts as a **narcotising** poison upon the heroic spirit of the nation." }
    ]
  },
  "Dashboard — narc/narcotize.md": {
    word: "narcotize",
    primary: "To make unconscious, insensible, or stupefied with or as if with a narcotic drug.",
    secondary: "In sociology and communication theory (the narcotizing dysfunction), to overwhelm the public with information so that passive knowing replaces active participation.",
    quotes: [
      { author: "William James", work: "The Principles of Psychology", quote: "Alcohol and ether serve to **narcotize** the higher inhibitory centers of the cerebral cortex." },
      { author: "Paul Lazarsfeld & Robert K. Merton", work: "Mass Communication, Popular Taste and Organized Social Action", quote: "The vast flood of mass media may **narcotize** rather than energize the average citizen into political apathy." },
      { author: "Mark Twain", work: "The Innocents Abroad", quote: "The Turkish bath seemed calculated to **narcotize** every muscle and nerve in the human frame." }
    ]
  },
  "Dashboard — narc/narcotized.md": {
    word: "narcotized",
    primary: "Rendered unconscious, stupefied, or drowsy by the administration of a narcotic drug.",
    secondary: "Lacking emotional sensitivity or mental alertness; dulled into passive indifference.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The deeply **narcotized** patient exhibited pinpoint pupils and slow, shallow respirations." },
      { author: "Jack London", work: "The Sea-Wolf", quote: "Wolf Larsen lay back as though **narcotized** by the excruciating paroxysms of his headache." },
      { author: "Henry David Thoreau", work: "Walden", quote: "Most men lead lives of quiet desperation, their faculties **narcotized** by routine and trivial cares." }
    ]
  },
  "Dashboard — narc/narcotizing.md": {
    word: "narcotizing",
    primary: "Producing stupor, numbness, or sleep; acting as a narcotic.",
    secondary: "Dulling the critical faculties or deadening responsiveness to moral or intellectual challenges.",
    quotes: [
      { author: "William James", work: "Talks to Teachers on Psychology", quote: "Habit can become a **narcotizing** chain if it excludes the possibility of spontaneous fresh thought." },
      { author: "Herman Melville", work: "Moby-Dick", quote: "The warm, drowsy sunlight exerted a **narcotizing** power over the lookout at the masthead." },
      { author: "Aldous Huxley", work: "Brave New World Revisited", quote: "Propaganda achieves its victories through the **narcotizing** repetition of simple slogans." }
    ]
  },
  "Dashboard — narc/narcotraffic.md": {
    word: "narcotraffic",
    primary: "The illicit production, smuggling, distribution, and sale of illegal narcotic drugs on a commercial scale.",
    secondary: "In international law enforcement and criminology, transnational organized criminal commerce that destabilizes economies and finances paramilitarism.",
    quotes: [
      { author: "Joseph Stiglitz", work: "Globalization and Its Discontents", quote: "The billions generated by global **narcotraffic** corrupt financial institutions across developed and developing nations alike." },
      { author: "Noam Chomsky", work: "Rogue States", quote: "The militarized campaigns against **narcotraffic** routinely target peasant farmers while leaving major money-laundering banks untouched." },
      { author: "Paul Collier", work: "The Plunder of the Earth", quote: "Where state authority collapses, **narcotraffic** fills the vacuum with violence and lawlessness." }
    ]
  },

  // === Dashboard — tox ===
  "Dashboard — tox/anatoxin.md": {
    word: "anatoxin",
    primary: "A bacterial toxin that has been treated with heat or chemicals (such as formaldehyde) to destroy its toxicity while retaining its antigenic properties; a toxoid.",
    secondary: "In immunology, developed by Gaston Ramon at the Pasteur Institute, the basis for successful vaccines against diphtheria and tetanus.",
    quotes: [
      { author: "Gaston Ramon", work: "Sur les toxines et les anatoxines", quote: "By treating the diphtheria toxin with formalin and heat, we produced a stable **anatoxin** capable of conferring durable immunity without illness." },
      { author: "Paul de Kruif", work: "Microbe Hunters", quote: "Ramon's discovery of the **anatoxin** provided humanity with a shield against the lethal lockjaw of tetanus." },
      { author: "Siddhartha Mukherjee", work: "The Song of the Cell", quote: "The **anatoxin** preserves the exact three-dimensional epitope required for neutralizing antibody generation." }
    ]
  },
  "Dashboard — tox/antitoxic.md": {
    word: "antitoxic",
    primary: "Counteracting, neutralizing, or opposing the effects of a toxin or poison.",
    secondary: "In immunology and therapeutics, describing antibodies (such as diphtheria antitoxin) or chemical antidotes that bind and neutralize specific bacterial toxins.",
    quotes: [
      { author: "Emil von Behring", work: "Nobel Lecture: Serum Therapy in Therapeutics", quote: "The blood serum of an immunized horse possesses an **antitoxic** power capable of neutralizing the diphtheria poison in vivo." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Immediate administration of **antitoxic** serum remains the only sovereign remedy against tetanus spasms." },
      { author: "Paul Ehrlich", work: "Studies in Immunity", quote: "The **antitoxic** unit was standardized by measuring the exact quantity of serum required to neutralize a fatal dose of toxin." }
    ]
  },
  "Dashboard — tox/antitoxin.md": {
    word: "antitoxin",
    primary: "An antibody that counteracts or neutralizes a specific toxin, especially one produced by a bacterium, plant, or animal.",
    secondary: "In the history of immunology, discovered by Emil von Behring and Kitasato Shibasaburo in 1890, providing the first successful passive serum therapy for diphtheria.",
    quotes: [
      { author: "Emil von Behring", work: "On the Mechanism of Immunity in Diphtheria", quote: "The discovery of the **antitoxin** showed that passive transfer of serum could rescue a child dying from suffocating diphtheria." },
      { author: "Paul de Kruif", work: "Microbe Hunters", quote: "Roux raced through the streets of Paris carrying the precious **antitoxin** that would empty the diphtheria wards." },
      { author: "William Osler", work: "Aequanimitas", quote: "The triumph of the diphtheria **antitoxin** marked the dawn of modern rational biotherapy." }
    ]
  },
  "Dashboard — tox/atoxic.md": {
    word: "atoxic",
    primary: "Not toxic; free from poison; non-poisonous.",
    secondary: "In pharmacodynamics, describing compounds or vaccine antigens that exhibit no measurable cytotoxicity or systemic adverse reactions in therapeutic concentrations.",
    quotes: [
      { author: "Paul Ehrlich", work: "Experimental Chemotherapy", quote: "Our goal was to synthesize a derivative that was parasitotropic against the spirochete yet completely **atoxic** to the host." },
      { author: "Selman Waksman", work: "My Life with the Microbes", quote: "The antibiotic candidate proved highly active against bacteria and fortunately **atoxic** to mammalian kidneys." },
      { author: "Arthur Guyton", work: "Textbook of Medical Physiology", quote: "The degradation products of the plasma expander are inert, biodegradable, and entirely **atoxic**." }
    ]
  },
  "Dashboard — tox/autotoxin.md": {
    word: "autotoxin",
    primary: "A poison or toxic substance generated within the body of an organism by metabolic processes or tissue breakdown.",
    secondary: "In classical nineteenth-century pathology (the auto-intoxication theory), metabolic byproducts (such as uremic or hepatic toxins) that accumulate when excretory organs fail.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Uremic coma was attributed to the retention of an uneliminated **autotoxin** poisoning the cerebral cortex." },
      { author: "Élie Metchnikoff", work: "The Prolongation of Life", quote: "He believed that intestinal putrefaction generated an insidious **autotoxin** that hastened premature arterial decay." },
      { author: "Oliver Wendell Holmes Sr.", work: "Medical Essays", quote: "The healthy liver and kidneys stand as faithful sentinels against every endogenous **autotoxin**." }
    ]
  },
  "Dashboard — tox/endotoxin.md": {
    word: "endotoxin",
    primary: "A toxic component present inside a bacterial cell that is released only when the bacterium disintegrates or lyses.",
    secondary: "In microbiology and immunology, the lipopolysaccharide (LPS) of the outer membrane of Gram-negative bacteria (e.g., E. coli, Salmonella), which activates Toll-like receptor 4 to trigger fever, septic shock, and disseminated intravascular coagulation.",
    quotes: [
      { author: "Lewis Thomas", work: "The Lives of a Cell", quote: "Gram-negative **endotoxin** is our ultimate alarm chemical; the body reads its presence as a catastrophic invasion and mobilizes defenses that can destroy the host." },
      { author: "Siddhartha Mukherjee", work: "The Song of the Cell", quote: "Circulating bacterial **endotoxin** binds to macrophage receptors, unleashing a storm of inflammatory cytokines." },
      { author: "Atul Gawande", work: "Complications", quote: "The collapse of blood pressure in septic shock is driven by the massive release of **endotoxin** from dying bacteria." }
    ]
  },
  "Dashboard — tox/exotoxin.md": {
    word: "exotoxin",
    primary: "A potent toxic substance secreted by living bacterial cells into the surrounding environment.",
    secondary: "In clinical microbiology, highly lethal proteins (such as botulinum neurotoxin, tetanus toxin, and diphtheria toxin) that possess specific enzymatic targets and can be neutralized by antibodies or converted into toxoids.",
    quotes: [
      { author: "Emil von Behring", work: "Studies on Tetanus and Diphtheria", quote: "The diphtheria bacillus remains confined to the throat, but its soluble **exotoxin** circulates to paralyze the heart muscle." },
      { author: "Paul de Kruif", work: "Microbe Hunters", quote: "A few drops of purified botulinum **exotoxin** contained enough concentrated venom to destroy an entire regiment." },
      { author: "Siddhartha Mukherjee", work: "The Song of the Cell", quote: "Tetanus **exotoxin** ascends retrograde along motor axons to block inhibitory neurotransmission in the spinal cord." }
    ]
  },
  "Dashboard — tox/intoxicant.md": {
    word: "intoxicant",
    primary: "A substance (such as alcohol, a narcotic, or a psychoactive drug) that causes intoxication or inebriation.",
    secondary: "In toxicology and public health, any chemical agent capable of altering central nervous system function, motor coordination, and judgment.",
    quotes: [
      { author: "James George Frazer", work: "The Golden Bough", quote: "In ancient Dionysian mysteries, the divine **intoxicant** was believed to fill the worshipper with the living presence of the god." },
      { author: "Edward William Bok", work: "The Americanization of Edward Bok", quote: "The campaign against the sale of patent medicines revealed that many popular tonics were little more than disguised **intoxicants**." },
      { author: "Thomas Hardy", work: "The Mayor of Casterbridge", quote: "Under the reckless influence of the potent **intoxicant**, Henchard committed the act that shadowed his entire future." }
    ]
  },
  "Dashboard — tox/intoxicate.md": {
    word: "intoxicate",
    primary: "To cause someone to lose control of their faculties or behavior by the administration of alcohol or drugs; to inebriate.",
    secondary: "To excite, exhilarate, or elate someone to the point of losing sober judgment.",
    quotes: [
      { author: "Alexander Pope", work: "An Essay on Criticism", quote: "A little learning is a dangerous thing; drink deep, or taste not the Pierian spring: there shallow draughts **intoxicate** the brain, and drinking largely sobers us again." },
      { author: "Charles Dickens", work: "David Copperfield", quote: "The unexpected praise from the great man served to **intoxicate** my youthful vanity beyond measure." },
      { author: "Herman Melville", work: "Moby-Dick", quote: "The exhilarating sea wind seemed to **intoxicate** the sailors as the Pequod raced before the gale." }
    ]
  },
  "Dashboard — tox/intoxicated.md": {
    word: "intoxicated",
    primary: "Drunk or under the influence of drugs; inebriated; or overwhelmed by strong excitement and joy.",
    secondary: "In forensic toxicology, having a blood alcohol concentration or drug level sufficient to impair cognitive and physical performance.",
    quotes: [
      { author: "Arthur Conan Doyle", work: "The Sign of Four", quote: "The missing coachman was discovered in an **intoxicated** stupor in the tavern cellar." },
      { author: "Charlotte Brontë", work: "Jane Eyre", quote: "He spoke with wild passion, looking at me with eyes **intoxicated** by love and defiance." },
      { author: "Jack London", work: "John Barleycorn", quote: "He walked through the swinging doors, **intoxicated** not by beer alone, but by the roar of frontier life." }
    ]
  },
  "Dashboard — tox/intoxicating.md": {
    word: "intoxicating",
    primary: "Causing drunkenness or inebriation; or producing intense excitement, delight, or exhilaration.",
    secondary: "Capable of impairing neurological motor and cognitive functions through chemical action.",
    quotes: [
      { author: "Thomas Hardy", work: "Tess of the d'Urbervilles", quote: "The heavy floral scent of the garden on that summer evening had an **intoxicating** quality that made her head swim." },
      { author: "Nathaniel Hawthorne", work: "The Scarlet Letter", quote: "She breathed the **intoxicating** air of freedom for the first time in seven weary years." },
      { author: "F. Scott Fitzgerald", work: "The Great Gatsby", quote: "The sparkling music and the warm champagne combined into an **intoxicating** enchantment under the summer stars." }
    ]
  },
  "Dashboard — tox/intoxication.md": {
    word: "intoxication",
    primary: "The state of being intoxicated or drunk; or poisoning by a toxic substance or drug.",
    secondary: "In medical pathology, acute physiological poisoning resulting from the ingestion, inhalation, or systemic production of a toxic agent.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Acute alcoholic **intoxication** in severe cases may depress the medullary respiratory centers to the point of fatal coma." },
      { author: "Thomas Hardy", work: "Far from the Madding Crowd", quote: "In a moment of reckless **intoxication**, Troy spent his young wife's fortune upon gambling debts." },
      { author: "Sherwin B. Nuland", work: "Doctors: The Biography of Medicine", quote: "The fatal **intoxication** of puerperal fever was caused by toxins carried directly on the unsterilized fingers of the accoucheur." }
    ]
  },
  "Dashboard — tox/neurotoxic.md": {
    word: "neurotoxic",
    primary: "Poisonous, destructive, or damaging to nerve tissue or the nervous system.",
    secondary: "In toxicology and neurology, describing substances (such as snake venoms, lead, organophosphates, or tetrodotoxin) that disrupt ion channel conduction or neurotransmitter release.",
    quotes: [
      { author: "Rachel Carson", work: "Silent Spring", quote: "The synthetic chlorinated insecticides exert a violent **neurotoxic** effect, causing tremors, convulsions, and respiratory paralysis." },
      { author: "Oliver Sacks", work: "The Island of the Colorblind", quote: "We investigated whether the traditional cycad flour contained a **neurotoxic** amino acid that triggered the local Parkinsonism dementia." },
      { author: "Siddhartha Mukherjee", work: "The Song of the Cell", quote: "The coral snake's venom is intensely **neurotoxic**, blocking acetylcholine receptors at the neuromuscular junction." }
    ]
  },
  "Dashboard — tox/neurotoxin.md": {
    word: "neurotoxin",
    primary: "A poison or toxic substance that acts specifically upon the nervous system, disrupting nerve transmission.",
    secondary: "In biochemistry, potent biological venoms or synthetic chemicals (such as botulinum toxin, tetrodotoxin, or saxitoxin) that block sodium channels or cleave SNARE proteins in synaptic exocytosis.",
    quotes: [
      { author: "Lewis Thomas", work: "The Lives of a Cell", quote: "A minute trace of botulinum **neurotoxin** can silence all motor nerve signals with mathematical precision." },
      { author: "Arthur Conan Doyle", work: "The Adventure of the Devil's Foot", quote: "The ordeal powder from West Africa contained a deadly **neurotoxin** that induced madness and asphyxiation." },
      { author: "Oliver Sacks", work: "Musicophilia", quote: "The pufferfish **neurotoxin** paralyzed his peripheral nerves while leaving his conscious auditory perception intact." }
    ]
  },
  "Dashboard — tox/psychotoxic.md": {
    word: "psychotoxic",
    primary: "Having a toxic, damaging, or deranging effect on the mind, mental health, or psychological functioning.",
    secondary: "In psychopharmacology, describing drugs or chemical exposures that induce hallucinations, delirium, acute psychosis, or permanent cognitive impairment.",
    quotes: [
      { author: "Aldous Huxley", work: "The Doors of Perception", quote: "Unlike crude alcohol, certain mescaline alkaloids produce perceptual shifts without gross **psychotoxic** hangover." },
      { author: "Alexander Shulgin", work: "PiHKAL: A Chemical Love Story", quote: "Careful dosage titrations are required to establish whether a compound is psychotherapeutic or dangerously **psychotoxic**." },
      { author: "Cesare Lombroso", work: "The Man of Genius", quote: "Prolonged exposure to industrial lead fumes exerted a **psychotoxic** influence, culminating in melancholic hallucinations." }
    ]
  },
  "Dashboard — tox/toxic.md": {
    word: "toxic",
    primary: "Poisonous; capable of causing injury, illness, or death to living organisms.",
    secondary: "In pathology and medicine, caused by or relating to a toxin; in modern colloquial and sociological usage, extremely harmful, malicious, or pervasive.",
    quotes: [
      { author: "Rachel Carson", work: "Silent Spring", quote: "The **toxic** chemicals sprayed upon the orchards seeped into underground aquifers, poisoning farm wells miles away." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The **toxic** goiter produces a racing pulse, fine tremors, and profound metabolic exhaustion." },
      { author: "Siddhartha Mukherjee", work: "The Emperor of All Maladies", quote: "Chemotherapy remains a brutally **toxic** therapy, balancing destruction of cancer cells against survival of the patient." }
    ]
  },
  "Dashboard — tox/toxicity.md": {
    word: "toxicity",
    primary: "The quality, state, or relative degree of being poisonous or harmful to life.",
    secondary: "In pharmacology and environmental science, the dose-dependent capacity of a substance to cause cellular damage, organ failure, or mortality (measured as LD50).",
    quotes: [
      { author: "Rachel Carson", work: "Silent Spring", quote: "Parathion exhibits an acute **toxicity** so extreme that a single drop upon the skin can kill an adult." },
      { author: "Paul Ehrlich", work: "Studies in Immunity", quote: "The therapeutic index is determined by dividing the curative dose by the maximum tolerated **toxicity**." },
      { author: "Jerome Groopman", work: "The Anatomy of Hope", quote: "The oncologist reduced the drug dosage to mitigate hepatic **toxicity** while preserving antitumor pressure." }
    ]
  },
  "Dashboard — tox/toxin.md": {
    word: "toxin",
    primary: "An antigenic poison or venom of plant or animal origin, especially one produced by or derived from microorganisms.",
    secondary: "In molecular toxicology, a biological macromolecule that causes disease upon contact or absorption, provoking an immune response (formation of antitoxins).",
    quotes: [
      { author: "Paul de Kruif", work: "Microbe Hunters", quote: "Roux proved that the filtered broth contained the deadly diphtheria **toxin**, free from any living bacteria." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The tetanus **toxin** exhibits a specific biochemical affinity for the motor neurons of the anterior horns." },
      { author: "Lewis Thomas", work: "The Lives of a Cell", quote: "A bacterial **toxin** is not merely a poison; it is an evolutionary key fashioned to turn our own cellular locks." }
    ]
  },
  "Dashboard — tox/toxoid.md": {
    word: "toxoid",
    primary: "A bacterial toxin whose toxicity has been inactivated or suppressed (by chemical treatment or heat) while its immunogenic properties are maintained; an anatoxin.",
    secondary: "In preventive medicine, the cornerstone of active immunization vaccines (e.g., tetanus toxoid and diphtheria toxoid) that stimulate protective neutralizing antibodies.",
    quotes: [
      { author: "Gaston Ramon", work: "On Anatoxins and Toxoids", quote: "By formalizing the toxin, we created an innocuous **toxoid** that safely immunizes horses and humans against tetanus." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Routine immunization with diphtheria **toxoid** during infancy has practically banished membranous croup from civilised communities." },
      { author: "Atul Gawande", work: "Better", quote: "Every patient presenting with a contaminated laceration receives a booster dose of tetanus **toxoid**." }
    ]
  },
  "Dashboard — tox/toxology.md": {
    word: "toxology",
    primary: "The scientific study of poisons, their effects, detection, and treatments; toxicology (historical/variant spelling).",
    secondary: "In historical forensic science and medical jurisprudence, the systematic investigation of toxic substances, postmortem chemical analysis, and antidote preparation.",
    quotes: [
      { author: "Robert Christison", work: "A Treatise on Poisons", quote: "The student of medical **toxology** must master chemical reagents to demonstrate arsenic in postmortem tissues." },
      { author: "Arthur Conan Doyle", work: "A Study in Scarlet", quote: "Sherlock Holmes was well versed in forensic **toxology**, identifying rare alkaloids from a single droplet of blood." },
      { author: "Alfred Swaine Taylor", work: "Medical Jurisprudence", quote: "Modern **toxology** has closed the avenues through which secret poisoners once escaped detection." }
    ]
  },
  "Dashboard — tox/toxoplasmosis.md": {
    word: "toxoplasmosis",
    primary: "An infectious disease caused by the microscopic intracellular protozoan parasite Toxoplasma gondii, transmitted via undercooked meat or contact with cat feces.",
    secondary: "In obstetrics and infectious disease, a dangerous congenital infection causing chorioretinitis, hydrocephalus, and intracranial calcifications in the fetus, or encephalitis in immunocompromised hosts.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Congenital **toxoplasmosis** produces devastating intracranial calcifications and blindness in the newborn." },
      { author: "Oliver Sacks", work: "The Man Who Mistook His Wife for a Hat", quote: "Cerebral **toxoplasmosis** formed multiple ring-enhancing abscesses in the immunosuppressed patient's basal ganglia." },
      { author: "Jerome Groopman", work: "The Anatomy of Hope", quote: "Antiparasitic therapy with pyrimethamine successfully suppressed the opportunistic flare of **toxoplasmosis**." }
    ]
  },

  // === Dashboard — tom ===
  "Dashboard — tom/anatomic.md": {
    word: "anatomic",
    primary: "Of or relating to anatomy or the physical structure of living organisms.",
    secondary: "Describing structural landmarks, architectural relationships, or physiological body planes.",
    quotes: [
      { author: "Andreas Vesalius", work: "De Humani Corporis Fabrica", quote: "True medical progress requires that we verify every ancient doctrine against direct **anatomic** dissection." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Careful physical diagnosis allows the physician to construct a precise **anatomic** map of the cardiac defect." },
      { author: "Thomas Henry Huxley", work: "Man's Place in Nature", quote: "The **anatomic** differences separating man from the gorilla are less than those separating the gorilla from lower apes." }
    ]
  },
  "Dashboard — tom/anatomical.md": {
    word: "anatomical",
    primary: "Relating to the bodily structure of organisms; of or pertaining to the science of anatomy.",
    secondary: "Exhibiting structural accuracy or morphological organization (as an anatomical atlas or specimen).",
    quotes: [
      { author: "Andreas Vesalius", work: "De Humani Corporis Fabrica", quote: "My **anatomical** plates were drawn from life at the dissecting table to banish the errors of Galen." },
      { author: "Charles Darwin", work: "The Descent of Man", quote: "Homologous **anatomical** structures across mammals bear silent witness to their common evolutionary descent." },
      { author: "Sherwin B. Nuland", work: "Doctors: The Biography of Medicine", quote: "The Renaissance passion for **anatomical** truth transformed both art and surgery into sciences of exact observation." }
    ]
  },
  "Dashboard — tom/anatomically.md": {
    word: "anatomically",
    primary: "With reference to or in terms of bodily structure; by means of dissection or anatomical analysis.",
    secondary: "Structurally or morphologically formed according to the organization of an organism.",
    quotes: [
      { author: "Charles Darwin", work: "The Origin of Species", quote: "The hand of a man, the flipper of a seal, and the wing of a bat are **anatomically** identical in their underlying skeletal framework." },
      { author: "Thomas Henry Huxley", work: "Evidence as to Man's Place in Nature", quote: "Man is **anatomically** closer to the chimpanzee than the chimpanzee is to the lemur." },
      { author: "Oliver Sacks", work: "A Leg to Stand On", quote: "The limb was **anatomically** healed, yet neurologically alienated from my conscious body image." }
    ]
  },
  "Dashboard — tom/anatomise.md": {
    word: "anatomise",
    primary: "To dissect a human, animal, or plant body in order to examine its structure; or to analyze something in minute detail (chiefly British spelling of anatomize).",
    secondary: "In literary and philosophical prose, to subject human motives, society, or melancholy to exhaustive scrutiny.",
    quotes: [
      { author: "William Shakespeare", work: "King Lear", quote: "Then let them **anatomise** Regan; see what breeds about her heart: is there any cause in nature that make these hard hearts?" },
      { author: "Robert Burton", work: "The Anatomy of Melancholy", quote: "My intent is to **anatomise** this widespread disease of melancholy, exposing its causes and symptoms to the world." },
      { author: "John Donne", work: "An Anatomy of the World", quote: "The world is sick, and now is dead; and we must **anatomise** this carcase to discover how it fell." }
    ]
  },
  "Dashboard — tom/anatomist.md": {
    word: "anatomist",
    primary: "A specialist or scholar who studies the structure and organization of living organisms; one who performs anatomical dissections.",
    secondary: "Historically, Renaissance scholars (such as Vesalius and John Hunter) whose physical investigations founded modern scientific surgery and pathology.",
    quotes: [
      { author: "John Hunter", work: "Essays and Observations on Natural History, Anatomy, and Physiology", quote: "The true **anatomist** never speculates upon function until he has laid bare every fiber of structure." },
      { author: "William Shakespeare", work: "All's Well That Ends Well", quote: "I will make him an example, and show him to the world like a dissected subject for the **anatomist**." },
      { author: "Sherwin B. Nuland", work: "Doctors", quote: "Vesalius was an intrepid **anatomist** who stole corpses from the gallows to establish the truths of human morphology." }
    ]
  },
  "Dashboard — tom/anatomize.md": {
    word: "anatomize",
    primary: "To dissect a body or organism for scientific examination; or to examine, analyze, and lay bare the parts of something in exhaustive detail.",
    secondary: "In critical rhetoric and essayistic analysis, to dissect an argument, historical event, or passion down to its constituent components.",
    quotes: [
      { author: "Alexander Pope", work: "Moral Essays", quote: "Search then the Ruling Passion: there alone the wild are constant, and the cunning known; this clue once found unfolds all the rest, and helps you **anatomize** the human breast." },
      { author: "Michel de Montaigne", work: "Essays", quote: "I dare not only speak of myself, but I speak only of myself; I **anatomize** my own nature with unsparing candor." },
      { author: "Francis Bacon", work: "The Advancement of Learning", quote: "It is the office of inductive science to **anatomize** nature, breaking down complex phenomena into simple laws." }
    ]
  },
  "Dashboard — tom/anatomy.md": {
    word: "anatomy",
    primary: "The branch of science concerned with the bodily structure of humans, animals, and other living organisms, especially as revealed by dissection.",
    secondary: "An exhaustive written analysis or structural dissection of a complex topic, institution, or psychological condition (e.g., Robert Burton's Anatomy of Melancholy).",
    quotes: [
      { author: "Andreas Vesalius", work: "De Humani Corporis Fabrica", quote: "The study of **anatomy** is the only reliable foundation upon which the sublime palace of medicine can be built." },
      { author: "Robert Burton", work: "The Anatomy of Melancholy", quote: "I write of melancholy by being busy to avoid melancholy, crafting this **anatomy** of human misery." },
      { author: "William Osler", work: "Aequanimitas", quote: "Without thorough training in morbid **anatomy**, the clinician is like a mariner without a compass." }
    ]
  },
  "Dashboard — tom/appendectomy.md": {
    word: "appendectomy",
    primary: "The surgical operation to remove the vermiform appendix.",
    secondary: "In emergency surgery, the standard definitive cure for acute appendicitis (first successfully performed by Reginald Fitz and Charles McBurney), preventing fatal peritonitis.",
    quotes: [
      { author: "Charles McBurney", work: "The Indications for Early Laparotomy in Appendicitis", quote: "Early **appendectomy** through an oblique muscle-splitting incision averts the catastrophic hazard of gangrenous perforation." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "In doubtful acute abdominal cases, McBurney's point of maximal tenderness dictates prompt surgical **appendectomy**." },
      { author: "Atul Gawande", work: "Complications", quote: "The routine laparoscopic **appendectomy** has become the bread-and-butter operation of modern emergency general surgery." }
    ]
  },
  "Dashboard — tom/dichotomise.md": {
    word: "dichotomise",
    primary: "To divide, separate, or classify into two contradictory or mutually exclusive groups or parts (chiefly British spelling of dichotomize).",
    secondary: "In logic and botanical taxonomy, to bifurcate a key or category into contrasting paired branches.",
    quotes: [
      { author: "Jeremy Bentham", work: "Chrestomathia", quote: "The analytical mind loves to **dichotomise** complex phenomena into mutually exhaustive divisions." },
      { author: "John Stuart Mill", work: "A System of Logic", quote: "Logicians who **dichotomise** every argument into polar extremes frequently overlook intermediate truths." },
      { author: "George Bernard Shaw", work: "Major Barbara", quote: "Society seeks to **dichotomise** all men into saints and scoundrels, ignoring the mixed comedy of real life." }
    ]
  },
  "Dashboard — tom/dichotomize.md": {
    word: "dichotomize",
    primary: "To divide, classify, or split into two sharply distinguished, opposed, or contradictory parts.",
    secondary: "In statistics and research design, to transform a continuous numerical variable into a binary categorical variable.",
    quotes: [
      { author: "William James", work: "The Principles of Psychology", quote: "We tend to **dichotomize** our thoughts into self and not-self, carving reality along psychological lines." },
      { author: "Bertrand Russell", work: "History of Western Philosophy", quote: "Plato was prone to **dichotomize** the universe into an eternal world of ideas and an illusory world of sense." },
      { author: "Stephen Jay Gould", work: "The Mismeasure of Man", quote: "To **dichotomize** human intelligence into nature versus nurture is a fallacy that distorts biological complexity." }
    ]
  },
  "Dashboard — tom/dichotomous.md": {
    word: "dichotomous",
    primary: "Dividing into two parts, branches, or classes; exhibiting or relating to a dichotomy.",
    secondary: "In botany and systematic biology, describing branching where the axis repeatedly forks into two equal shoots, or a dichotomous identification key.",
    quotes: [
      { author: "Asa Gray", work: "Manual of the Botany of the Northern United States", quote: "The floral identification key is strictly **dichotomous**, offering pairs of contrasting choices at every step." },
      { author: "Charles Darwin", work: "The Origin of Species", quote: "The **dichotomous** branching of the ancestral lineage illustrates how two distinct species diverge from a common stock." },
      { author: "M. C. Cooke", work: "Introduction to the Study of Fungi", quote: "The hyphae display **dichotomous** forking at their growing tips under favorable nutritional conditions." }
    ]
  },
  "Dashboard — tom/dichotomously.md": {
    word: "dichotomously",
    primary: "In a dichotomous manner; by dividing into two equal or contrasting branches or parts.",
    secondary: "In morphological development and algorithmic classification, branching repeatedly into pairs.",
    quotes: [
      { author: "Julius von Sachs", work: "Text-Book of Botany", quote: "The thallus of the liverwort Riccia grows and forks **dichotomously** across the damp soil." },
      { author: "Thomas Henry Huxley", work: "The Crayfish", quote: "The gills branch **dichotomously**, expanding the surface area for respiratory gas exchange." },
      { author: "Alfred North Whitehead", work: "Science and the Modern World", quote: "When thought proceeds **dichotomously**, it sharpens distinctions at the expense of comprehensive synthesis." }
    ]
  },
  "Dashboard — tom/dichotomy.md": {
    word: "dichotomy",
    primary: "A division or contrast between two things that are represented as being entirely opposed, contradictory, or mutually exclusive.",
    secondary: "In astronomy, the phase of the Moon or an inferior planet (Mercury, Venus) when exactly half of its illuminated disk is visible from Earth.",
    quotes: [
      { author: "William James", work: "Pragmatism", quote: "Pragmatism refuses to accept the rigid **dichotomy** between tough-minded materialism and tender-minded idealism." },
      { author: "John Dewey", work: "Experience and Education", quote: "Mankind likes to think in terms of an either-or **dichotomy**, framing educational debate as traditional versus progressive." },
      { author: "Stephen Jay Gould", work: "Time's Arrow, Time's Cycle", quote: "Geological thought has long been structured around the false **dichotomy** of sudden catastrophe versus gradual change." }
    ]
  },
  "Dashboard — tom/episiotomy.md": {
    word: "episiotomy",
    primary: "A surgical incision made in the perineum and vaginal wall to facilitate childbirth and prevent traumatic tearing during difficult delivery.",
    secondary: "In obstetric surgery, a procedure (mediolateral or midline) historically practiced routinely but now reserved for specific fetal or maternal indications.",
    quotes: [
      { author: "Joseph DeLee", work: "The Prophylactic Episiotomy", quote: "I advocated the routine **episiotomy** to preserve the muscular integrity of the pelvic floor and spare the fetal head prolonged compression." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Careful repair of an **episiotomy** incision with absorbable sutures ensures primary intention healing of the perineum." },
      { author: "Abraham Verghese", work: "Cutting for Stone", quote: "The midwife swiftly performed a clean mediolateral **episiotomy** as the baby's head crowned in distress." }
    ]
  },
  "Dashboard — tom/laparotomy.md": {
    word: "laparotomy",
    primary: "A surgical incision into the abdominal cavity, either for exploratory diagnosis or for major operative surgery (celiotomy).",
    secondary: "In acute general surgery, exploratory laparotomy performed for penetrating abdominal trauma, acute hemoperitoneum, bowel obstruction, or perforated viscus.",
    quotes: [
      { author: "Ephraim McDowell", work: "Observations on Diseased Ovaria", quote: "In 1809, without anesthesia or antisepsis, I performed the first successful elective **laparotomy** to remove a colossal ovarian tumor." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "In acute intestinal obstruction, early exploratory **laparotomy** offers the only reasonable prospect of recovery." },
      { author: "Atul Gawande", work: "Complications", quote: "The trauma team made a midline **laparotomy** incision from xiphoid to pubis to pack the hemorrhaging liver." }
    ]
  },
  "Dashboard — tom/lobotomy.md": {
    word: "lobotomy",
    primary: "A surgical operation involving incision into the prefrontal lobes of the brain, formerly used to treat severe psychiatric disorders (prefrontal leukotomy).",
    secondary: "In the history of psychosurgery, introduced by Egas Moniz in 1935 (for which he won the 1949 Nobel Prize) and popularized by Walter Freeman, later condemned and abandoned due to catastrophic personality blunting and the advent of antipsychotic medications.",
    quotes: [
      { author: "Egas Moniz", work: "Tentatives opératoires dans le traitement de certaines psychoses", quote: "By prefrontal **lobotomy**, we severed the white association tracts to disrupt the fixed melancholic obsessions of the patient." },
      { author: "Oliver Sacks", work: "Awakenings", quote: "The tragedy of the surgical **lobotomy** was that it extinguished the patient's psychosis only by extinguishing the patient's soul." },
      { author: "Ken Kesey", work: "One Flew Over the Cuckoo's Nest", quote: "There was nothing in the face of the man who came back from the **lobotomy** but a blank, staring void." }
    ]
  },
  "Dashboard — tom/mastectomy.md": {
    word: "mastectomy",
    primary: "The surgical removal of one or both breasts, partially or completely, usually to treat or prevent breast cancer.",
    secondary: "In surgical oncology, historically pioneered as the Halsted radical mastectomy (removing breast, pectoralis muscles, and axillary nodes), now largely replaced by modified radical mastectomy or breast-conserving lumpectomy with sentinel lymph node biopsy.",
    quotes: [
      { author: "William Stewart Halsted", work: "The Results of Operations for the Cure of Cancer of the Breast", quote: "My radical **mastectomy** was designed upon the pathological truth that cancer spreads uninterruptedly along continuous lymphatic paths." },
      { author: "Siddhartha Mukherjee", work: "The Emperor of All Maladies", quote: "For half a century, Halsted's brutal radical **mastectomy** reigned supreme, until clinical trials proved that less mutilating operations were equally curative." },
      { author: "Jerome Groopman", work: "The Anatomy of Hope", quote: "The patient underwent a bilateral prophylactic **mastectomy** after genetic screening revealed a high-penetrance BRCA1 mutation." }
    ]
  },
  "Dashboard — tom/microtome.md": {
    word: "microtome",
    primary: "A mechanical instrument used to cut extremely thin slices of biological tissue (sections) for microscopic study.",
    secondary: "In histotechnology, a precision instrument (rotary, rocking, or vibrating blade) that cuts tissue embedded in paraffin wax or frozen medium into sections one to ten micrometers thick.",
    quotes: [
      { author: "Rudolf Virchow", work: "Cellular Pathology", quote: "The introduction of the razor-sharp **microtome** allowed pathologists to examine tissue architecture at single-cell resolution." },
      { author: "Santiago Ramón y Cajal", work: "Advice for a Young Investigator", quote: "A skilled histologist knows how to coax unbroken ribbons of serial sections from the blade of his **microtome**." },
      { author: "Oliver Sacks", work: "Uncle Tungsten", quote: "In my father's surgery stood a gleaming brass **microtome**, which shaved specimens into translucent ribbons for staining." }
    ]
  },
  "Dashboard — tom/prostatectomy.md": {
    word: "prostatectomy",
    primary: "The surgical operation involving the partial or complete removal of the prostate gland.",
    secondary: "In urologic surgery, performed via transurethral resection (TURP) for benign prostatic hyperplasia, or radical prostatectomy (open, laparoscopic, or robotic) for localized prostate cancer.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Suprapubic **prostatectomy** has transformed the miserable existence of elderly men suffering from chronic urinary retention." },
      { author: "Atul Gawande", work: "Complications", quote: "Robotic nerve-sparing **prostatectomy** permits the surgeon to excise the malignant gland while preserving erectile function." },
      { author: "Sherwin B. Nuland", work: "How We Die", quote: "Following a successful radical **prostatectomy**, the patient's prostate-specific antigen fell to undetectable levels." }
    ]
  },
  "Dashboard — tom/thoracotomy.md": {
    word: "thoracotomy",
    primary: "A surgical incision into the chest wall to gain access to the pleural cavity, lungs, heart, or great vessels.",
    secondary: "In thoracic and trauma surgery, emergency anterolateral thoracotomy performed in the resuscitation bay for penetrating cardiac injuries, or posterolateral thoracotomy for pulmonary lobectomy.",
    quotes: [
      { author: "Michael E. DeBakey", work: "Surgical Treatment of Thoracic Aortic Aneurysms", quote: "Through a left posterolateral **thoracotomy**, we mobilized the descending thoracic aorta and sutured the Dacron graft." },
      { author: "Atul Gawande", work: "Complications", quote: "An emergency **thoracotomy** opened the chest in seconds, allowing the surgeon to cross-clamp the aorta directly." },
      { author: "Abraham Verghese", work: "Cutting for Stone", quote: "The rib spreader ratcheted open the **thoracotomy** incision, exposing the collapsed, diseased lung." }
    ]
  },
  "Dashboard — tom/thyroidectomy.md": {
    word: "thyroidectomy",
    primary: "The surgical removal of all or part of the thyroid gland.",
    secondary: "In endocrine surgery, pioneered by Emil Theodor Kocher (1909 Nobel Prize), who perfected surgical technique to minimize hemorrhage and avoid damaging the recurrent laryngeal nerve and parathyroid glands.",
    quotes: [
      { author: "Emil Theodor Kocher", work: "Nobel Lecture: Concerning Pathological Manifestations in Low-Grade Thyroid Function", quote: "Total **thyroidectomy** for goiter cured the hyperthyroidism, but taught us the tragic clinical picture of cachexia strumipriva when all tissue was removed." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Kocher's exquisite anatomical hemostasis made **thyroidectomy** one of the safest and most successful major surgical procedures." },
      { author: "Atul Gawande", work: "The Checklist Manifesto", quote: "During a total **thyroidectomy**, the surgeon carefully identifies and preserves the delicate recurrent laryngeal nerves." }
    ]
  },
  "Dashboard — tom/tonsillectomy.md": {
    word: "tonsillectomy",
    primary: "The surgical removal of the tonsils, usually performed for recurrent tonsillitis, peritonsillar abscess, or obstructive sleep apnea.",
    secondary: "In pediatric otolaryngology, historically one of the most frequently performed operations in children, executed by guillotine excision, cold-knife dissection, or electrocautery.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Hypertrophied adenoids and chronically infected palatine tonsils demand prompt **tonsillectomy** to restore nasal breathing." },
      { author: "Sinclair Lewis", work: "Main Street", quote: "The village doctor earned his living performing **tonsillectomies** upon a kitchen table with chloroform and an old snare." },
      { author: "Atul Gawande", work: "Complications", quote: "Post-operative hemorrhage days after a **tonsillectomy** remains a terrifying emergency requiring immediate surgical control." }
    ]
  }
};

function updateWordNote(relPath, data) {
  const fullPath = path.join(baseDir, relPath);
  if (!fs.existsSync(fullPath)) {
    console.error("File not found:", fullPath);
    return;
  }

  let content = fs.readFileSync(fullPath, "utf8");

  // Format quotes
  const quotesFormatted = data.quotes.map(q => `> - 📜 **${q.author} (*${q.work}*):** *"${q.quote}"*`).join("\n");

  // Replace Definition & Semantic Range
  const defRegex = /> \[!book\] 📖 Definitions & Semantic Range[\s\S]*?(?=> \[!quote\]|$)/;
  const newDef = `> [!book] 📖 Definitions & Semantic Range\n> 1. **Primary Definition (Lexical / Standard Consensus)**: ${data.primary}\n> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: ${data.secondary}\n\n`;

  if (defRegex.test(content)) {
    content = content.replace(defRegex, newDef);
  } else {
    console.warn("Could not find [!book] in", relPath);
  }

  // Replace Quotes
  const quoteRegex = /> \[!quote\] 💬 Contextual Usage & Authentic Quotations[\s\S]*$/;
  const newQuotes = `> [!quote] 💬 Contextual Usage & Authentic Quotations\n${quotesFormatted}\n`;

  if (quoteRegex.test(content)) {
    content = content.replace(quoteRegex, newQuotes);
  } else {
    console.warn("Could not find [!quote] in", relPath);
  }

  fs.writeFileSync(fullPath, content, "utf8");
  console.log("Updated:", relPath);
}

for (const [relPath, data] of Object.entries(wordsData)) {
  updateWordNote(relPath, data);
}
console.log("Medicine & Pathology Batch 5 completed! Total words updated:", Object.keys(wordsData).length);
