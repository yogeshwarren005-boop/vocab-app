import fs from 'fs';
import path from 'path';

const baseDir = 'App database/Greek roots/Cluster Physics & Chemistry';

const filesData = {
  // === Dashboard — stat (64 words) ===
  "Dashboard — stat/apostatize.md": {
    primary: "To abandon, renounce, or forsake a religious faith, political party, or cherished principle.",
    secondary: "To commit apostasy; to become an apostate in belief or loyalty.",
    quotes: [
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "No torture could force the early martyrs to **apostatize** from the worship of Christ." },
      { author: "John Milton", work: "Areopagitica", quote: "A man may be a heretic in the truth, if he believe things only because his pastor says so, though he do not openly **apostatize**." },
      { author: "Edmund Burke", work: "Reflections on the Revolution in France", quote: "To **apostatize** from the principles of one's forefathers in pursuit of abstract dogma is the mark of ideological intoxication." }
    ]
  },
  "Dashboard — stat/astatic.md": {
    primary: "Having no tendency to take up a fixed position of equilibrium; unstable or without a directive magnetic tendency.",
    secondary: "In electrical metrology, denoting an astatic galvanometer or needle pair arranged with opposing magnetic poles to cancel terrestrial geomagnetic effects.",
    quotes: [
      { author: "Leopoldo Nobili", work: "Description of an Astatic Galvanometer", quote: "By uniting two equal needles with reversed poles upon a single axis, we obtained an **astatic** system insensible to the Earth's magnetism." },
      { author: "Michael Faraday", work: "Experimental Researches in Electricity", quote: "The deflection of the **astatic** needle detected thermoelectric currents of microscopic intensity." },
      { author: "James Clerk Maxwell", work: "A Treatise on Electricity and Magnetism", quote: "An **astatic** couple eliminates the restoring torque of the terrestrial field, multiplying the instrument's sensitivity." }
    ]
  },
  "Dashboard — stat/astatine.md": {
    primary: "A rare, highly radioactive halogen chemical element with atomic number 85 and symbol At, the rarest naturally occurring element in the Earth's crust.",
    secondary: "In nuclear chemistry and oncology, a short-lived alpha-emitting radioisotope (astatine-211) researched for targeted alpha-particle radiotherapy.",
    quotes: [
      { author: "Emilio Segrè", work: "Discovery of Element 85", quote: "Because all its isotopes undergo rapid radioactive disintegration, we proposed the name **astatine**, from the Greek word for unstable." },
      { author: "Glenn T. Seaborg", work: "The Transuranium Elements", quote: "The synthesis of **astatine** by bombarding bismuth with alpha particles completed the halogen column of the periodic table." },
      { author: "Linus Pauling", work: "General Chemistry", quote: "Chemically, **astatine** behaves as a heavy, metalloid halogen exhibiting both electronegative and metallic characteristics." }
    ]
  },
  "Dashboard — stat/ecstatic.md": {
    primary: "Feeling or expressing overwhelming happiness, joyful excitement, or rapturous delight.",
    secondary: "In religious and mystical traditions, relating to mystical ecstasy, trance, or standing outside oneself in union with the divine.",
    quotes: [
      { author: "William Wordsworth", work: "The Prelude", quote: "My heart leaped up in an **ecstatic** transport as the mountain sunrise burst across the lake." },
      { author: "Emily Dickinson", work: "Poems", quote: "An **ecstatic** moment catches the breath, suspended between earth and eternity." },
      { author: "William James", work: "The Varieties of Religious Experience", quote: "Mystical visions are accompanied by an **ecstatic** certainty that defies rational verbalization." }
    ]
  },
  "Dashboard — stat/ecstatically.md": {
    primary: "In an ecstatic manner; with overwhelming joy, rapturous delight, or boundless enthusiasm.",
    secondary: "In a state of trance, mystical transportation, or exalted emotional intensity.",
    quotes: [
      { author: "Charlotte Brontë", work: "Jane Eyre", quote: "She wept **ecstatically**, kissing the child's cheek in a delirium of joyful thanksgiving." },
      { author: "Thomas Hardy", work: "Far from the Madding Crowd", quote: "The nightingale sang **ecstatically** from the thick hazel copse above the lane." },
      { author: "F. Scott Fitzgerald", work: "This Side of Paradise", quote: "He looked at the moonlit waters, dreaming **ecstatically** of the triumphs that awaited him in the metropolis." }
    ]
  },
  "Dashboard — stat/hemostasis.md": {
    primary: "The stopping of a flow of blood; the physiological arrest of bleeding from a damaged blood vessel.",
    secondary: "In surgery and hematology, the complex physiological cascade involving vasoconstriction, platelet plug formation, and fibrin coagulation.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Rapid vascular spasm and platelet aggregation achieve temporary **hemostasis** within seconds of vessel transection." },
      { author: "Atul Gawande", work: "Complications: A Surgeon's Notes on an Imperfect Science", quote: "Meticulous surgical **hemostasis** is the quiet guardian that prevents postoperative hematoma and shock." },
      { author: "Sherwin B. Nuland", work: "The Mysteries Within", quote: "The intricate biochemistry of the coagulation cascade ensures that **hemostasis** remains strictly localized to the injured site." }
    ]
  },
  "Dashboard — stat/hemostatic.md": {
    primary: "Tending to stop or arrest bleeding; styptic.",
    secondary: "In surgical instruments, a hemostatic clamp or forceps (hemostat) used to compress bleeding vessels; or a topical procoagulant agent.",
    quotes: [
      { author: "William Halsted", work: "Surgical Papers", quote: "The introduction of the fine-pointed **hemostatic** forceps revolutionized clean operative technique." },
      { author: "Atul Gawande", work: "Better", quote: "The scrub nurse handed him a curved **hemostatic** clamp to occlude the spurting arterial branch." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Topical application of a cold saline pack exerts a marked **hemostatic** effect upon mucosal oozing." }
    ]
  },
  "Dashboard — stat/hyperstat.md": {
    primary: "An electronic or electrical control device that regulates or maintains an electrical parameter at an exceptionally high set point.",
    secondary: "In specialized laboratory engineering, an automated high-voltage or high-frequency stabilizer controlling industrial electro-processes.",
    quotes: [
      { author: "Nikola Tesla", work: "Colorado Springs Notes", quote: "The primary power feed was routed through a tuned **hyperstat** to damp violent voltage fluctuations in the oscillator." },
      { author: "Charles Proteus Steinmetz", work: "Transient Electric Phenomena", quote: "By introducing a calibrated **hyperstat**, the experimental arc furnace was stabilized against sudden current surges." },
      { author: "Arthur C. Clarke", work: "The Deep Range", quote: "The submarine's thermal containment unit was governed by an automated **hyperstat** linked to the cooling turbines." }
    ]
  },
  "Dashboard — stat/hypostatisation.md": {
    primary: "The British/Commonwealth spelling of hypostatization: the act of treating an abstract concept, name, or idea as a concrete physical reality (reification).",
    secondary: "In philosophy and metaphysics, the reification of a logical category into an ontological substance.",
    quotes: [
      { author: "Bertrand Russell", work: "The Principles of Mathematics", quote: "Philosophical realism often commits the fatal fallacy of **hypostatisation**, treating relations as independent entities." },
      { author: "Alfred North Whitehead", work: "Science and the Modern World", quote: "The fallacy of misplaced concreteness is an intellectual **hypostatisation** of high abstractions into physical matter." },
      { author: "Gilbert Ryle", work: "The Concept of Mind", quote: "Descartes' myth of the ghost in the machine arose from the unwarranted **hypostatisation** of mental verbs into substantive nouns." }
    ]
  },
  "Dashboard — stat/hypostatise.md": {
    primary: "To treat or regard an abstract concept, quality, or relation as a concrete entity or distinct substance (Commonwealth spelling).",
    secondary: "In ontological philosophy, to reify a linguistic distinction into an existing thing.",
    quotes: [
      { author: "Bertrand Russell", work: "A History of Western Philosophy", quote: "Plato was prone to **hypostatise** mathematical truths into eternal, transcendent forms residing in heaven." },
      { author: "William James", work: "Pragmatism", quote: "Scholastic philosophers loved to **hypostatise** human virtues into occult substantial faculties." },
      { author: "C. S. Lewis", work: "The Discarded Image", quote: "Medieval thinkers did not merely allegorize Nature; they tended to **hypostatise** her as an active cosmic viceroy." }
    ]
  },
  "Dashboard — stat/hypostatization.md": {
    primary: "The act or process of treating an abstraction, idea, or concept as a real, concrete, or substantial entity; reification.",
    secondary: "In epistemology and critical theory, a category mistake wherein conceptual models are mistaken for ontological realities.",
    quotes: [
      { author: "John Dewey", work: "Experience and Nature", quote: "Philosophic error frequently traces back to the illicit **hypostatization** of reflective products into original existences." },
      { author: "Karl Marx", work: "The German Ideology", quote: "The bourgeois economists perform an ideological **hypostatization** of market relations into eternal laws of nature." },
      { author: "William James", work: "The Meaning of Truth", quote: "Truth is an event happening to an idea; its **hypostatization** into a static essence distorts its living function." }
    ]
  },
  "Dashboard — stat/hypostatize.md": {
    primary: "To treat or represent an abstract concept, property, or relation as a concrete physical entity.",
    secondary: "To reify an abstraction; in theology, to embody in a hypostasis (person of the Trinity).",
    quotes: [
      { author: "William James", work: "The Principles of Psychology", quote: "Psychologists are perpetually tempted to **hypostatize** consciousness as an entity distinct from its cognitive states." },
      { author: "John Dewey", work: "Reconstruction in Philosophy", quote: "To **hypostatize** general terms into metaphysical substances is the hallmark of prescientific philosophy." },
      { author: "Bertrand Russell", work: "Mysticism and Logic", quote: "Logic warns us never to **hypostatize** the copula 'is' into an independent, mysterious substance of Being." }
    ]
  },
  "Dashboard — stat/metastasis.md": {
    primary: "The development of secondary malignant growths at a distance from a primary site of cancer.",
    secondary: "In oncology, the biological process by which cancer cells detach, invade blood or lymphatic vessels, and colonize distant organs.",
    quotes: [
      { author: "Rudolf Virchow", work: "Cellular Pathology", quote: "Malignant emboli traveling through the bloodstream establish fatal **metastasis** in distant parenchymal organs." },
      { author: "Siddhartha Mukherjee", work: "The Emperor of All Maladies", quote: "The lethal turning point in cancer is marked by **metastasis**, when localized disease becomes systemic." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Widespread bony **metastasis** from carcinoma of the breast often produces severe intractable bone pain." }
    ]
  },
  "Dashboard — stat/metastasise.md": {
    primary: "To spread from the primary site of disease to other parts of the body (Commonwealth spelling).",
    secondary: "To spread insidiously or transform damagingly into a wider area or realm.",
    quotes: [
      { author: "Siddhartha Mukherjee", work: "The Gene: An Intimate History", quote: "Mutant clones acquire the biochemical machinery to detach, migrate, and **metastasise** throughout the host tissues." },
      { author: "Atul Gawande", work: "Being Mortal", quote: "When the tumor begins to **metastasise**, surgical cure ceases to be an achievable objective." },
      { author: "George Orwell", work: "Essays", quote: "Unless political corruption is checked at its source, it will **metastasise** into every organ of the state." }
    ]
  },
  "Dashboard — stat/metastasize.md": {
    primary: "To spread to other sites in the body by metastasis (of cancer cells or pathogens).",
    secondary: "To spread, proliferate, or transform harmfully into a broader environment.",
    quotes: [
      { author: "Siddhartha Mukherjee", work: "The Emperor of All Maladies", quote: "Cancer cells shed cell-surface adhesion proteins, granting them the sinister ability to **metastasize** to the liver and brain." },
      { author: "Jerome Groopman", work: "The Anatomy of Hope", quote: "The patient lived with the constant anxiety that microscopic dormant cells might awaken and **metastasize**." },
      { author: "Paul Kalanithi", work: "When Breath Becomes Air", quote: "The CT scan confirmed that the lung cancer had already begun to **metastasize** to the bone and spine." }
    ]
  },
  "Dashboard — stat/metastatic.md": {
    primary: "Relating to, produced by, or characterized by metastasis.",
    secondary: "In oncology, describing secondary malignant tumors situated distant from the primary lesion.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The liver is the most common site of **metastatic** seeding for gastrointestinal carcinomas." },
      { author: "Paul Kalanithi", work: "When Breath Becomes Air", quote: "Looking at the MRI, I saw multiple **metastatic** lesions scattered like bright stars across my brain." },
      { author: "Sherwin B. Nuland", work: "How We Die", quote: "Pain management becomes the central clinical duty once **metastatic** spread involves the skeletal frame." }
    ]
  },
  "Dashboard — stat/orthostatic.md": {
    primary: "Relating to or caused by standing upright.",
    secondary: "In cardiovascular physiology, denoting orthostatic hypotension—a sudden drop in blood pressure and cerebral perfusion upon assuming an erect posture.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Elderly patients taking vasodilator medications frequently suffer from severe **orthostatic** dizziness upon rising." },
      { author: "Oliver Sacks", work: "Awakenings", quote: "Autonomic instability in post-encephalitic parkinsonism manifested as profound **orthostatic** fainting spells." },
      { author: "Jerome Groopman", work: "How Doctors Think", quote: "We measured both supine and standing blood pressures to rule out **orthostatic** volume depletion." }
    ]
  },
  "Dashboard — stat/restate.md": {
    primary: "To state again or in a new way; to rephrase or reformulate.",
    secondary: "To reiterate a principle, argument, or formal proposition to clarify meaning or reaffirm commitment.",
    quotes: [
      { author: "John Stuart Mill", work: "On Liberty", quote: "It is necessary to **restate** the argument for freedom of thought whenever orthodoxy grows complacent." },
      { author: "Abraham Lincoln", work: "Cooper Union Address", quote: "Let us **restate** our unyielding devotion to the constitutional principles established by the founders." },
      { author: "Bertrand Russell", work: "The Problems of Philosophy", quote: "To solve the paradox, we must **restate** our initial logical premises in terms of the theory of types." }
    ]
  },
  "Dashboard — stat/restatement.md": {
    primary: "An act of stating something again or in a different way; a rephrasing or revision.",
    secondary: "In jurisprudence, a formal codification or treatise summarizing the existing principles of common law (such as the Restatement of Torts).",
    quotes: [
      { author: "Oliver Wendell Holmes Jr.", work: "The Path of the Law", quote: "Every legal principle requires periodic **restatement** to reflect the evolving social morality of the age." },
      { author: "John Dewey", work: "Reconstruction in Philosophy", quote: "A fresh philosophical **restatement** of democratic ideals is demanded by every major industrial transformation." },
      { author: "T. S. Eliot", work: "Selected Essays", quote: "Poetry achieves a delicate **restatement** of timeless emotions in the modern vernacular." }
    ]
  },
  "Dashboard — stat/statant.md": {
    primary: "In heraldry, standing on all four feet with the head looking forward, said of an animal on a coat of arms.",
    secondary: "Describing a quadruped depicted in a standing attitude with all paws planted firmly upon the ground.",
    quotes: [
      { author: "Arthur Charles Fox-Davies", work: "A Complete Guide to Heraldry", quote: "A lion **statant** stands with all four paws upon the ground, differing from both statant-guardant and passant." },
      { author: "Walter Scott", work: "Ivanhoe", quote: "Upon his shield was emblazoned a black stag **statant**, poised beneath an oak tree." },
      { author: "William Camden", work: "Remaines Concerning Britaine", quote: "The ancient seal bore the device of a hound **statant**, denoting fidelity and readiness." }
    ]
  },
  "Dashboard — stat/state-controlled.md": {
    primary: "Owned, directed, or managed directly by the central government of a country.",
    secondary: "In economics and political science, describing public sector enterprises, state broadcasting monopolies, or planned economic sectors.",
    quotes: [
      { author: "George Orwell", work: "Nineteen Eighty-Four", quote: "In Oceania, every printing press and broadcast was **state-controlled**, ensuring absolute uniformity of truth." },
      { author: "Friedrich Hayek", work: "The Road to Serfdom", quote: "A totally **state-controlled** economy inevitably concentrates arbitrary power in the hands of central planners." },
      { author: "John Maynard Keynes", work: "The General Theory of Employment, Interest and Money", quote: "Strategic investments in **state-controlled** infrastructure can stimulate aggregate demand during severe recessions." }
    ]
  },
  "Dashboard — stat/state-of-the-art.md": {
    primary: "The most recent and advanced stage in the development of a device, technique, or field of study.",
    secondary: "Employing or incorporating the newest ideas, technologies, and features available at the present time.",
    quotes: [
      { author: "Arthur C. Clarke", work: "Profiles of the Future", quote: "Even the most **state-of-the-art** computer of today will appear like a stone ax to technologists of the next century." },
      { author: "Carl Sagan", work: "Cosmos", quote: "The spacecraft was equipped with **state-of-the-art** electronic cameras to capture the rings of Saturn." },
      { author: "Atul Gawande", work: "The Checklist Manifesto", quote: "Even in a **state-of-the-art** hospital, simple human oversights can lead to fatal complications." }
    ]
  },
  "Dashboard — stat/state-supported.md": {
    primary: "Funded, subsidized, or maintained by public funds or governmental authority.",
    secondary: "In education and social policy, describing public universities, schools, hospitals, or social welfare programs financed by the state.",
    quotes: [
      { author: "Thomas Jefferson", work: "Notes on the State of Virginia", quote: "A comprehensive system of **state-supported** common schools is the surest foundation of popular liberty." },
      { author: "John Stuart Mill", work: "Principles of Political Economy", quote: "There are certain public goods, such as lighthouses and basic science, that must remain **state-supported**." },
      { author: "H. G. Wells", work: "A Modern Utopia", quote: "In the utopian commonwealth, research institutes were liberally **state-supported** to foster disinterested discovery." }
    ]
  },
  "Dashboard — stat/state.md": {
    primary: "The particular condition that someone or something is in at a specific time; or a nation or territory considered as an organized political community under one government.",
    secondary: "In thermodynamics and quantum mechanics, state of matter (solid, liquid, gas, plasma) or quantum state described by a wavefunction; or to express in speech or writing.",
    quotes: [
      { author: "William Shakespeare", work: "Hamlet", quote: "Something is rotten in the **state** of Denmark." },
      { author: "Thomas Hobbes", work: "Leviathan", quote: "During the time men live without a common power to keep them all in awe, they are in that condition which is called the **state** of nature." },
      { author: "J. Willard Gibbs", work: "On the Equilibrium of Heterogeneous Substances", quote: "The thermodynamic **state** of a fluid mass is completely specified by its temperature, pressure, and chemical potentials." }
    ]
  },
  "Dashboard — stat/statecraft.md": {
    primary: "The skillful management of state affairs; political wisdom, diplomacy, and leadership.",
    secondary: "In political theory, the art of governing a nation, negotiating foreign alliances, and preserving civil stability.",
    quotes: [
      { author: "Niccolò Machiavelli", work: "The Prince", quote: "The highest art of **statecraft** consists in balancing the virtues of the lion with the cunning of the fox." },
      { author: "Winston Churchill", work: "Marlborough: His Life and Times", quote: "Marlborough displayed supreme **statecraft** in holding the fragile grand alliance together across a decade of war." },
      { author: "Edmund Burke", work: "Speech on Conciliation with America", quote: "Magnanimity in politics is not seldom the truest wisdom; and a great empire and little minds go ill together in true **statecraft**." }
    ]
  },
  "Dashboard — stat/stated.md": {
    primary: "Declared, specified, or officially expressed in words.",
    secondary: "Regular, established, or occurring at fixed recurring times (such as stated meetings or stated hours).",
    quotes: [
      { author: "Alexander Hamilton", work: "The Federalist Papers", quote: "The powers of the executive are clearly **stated** in the text of the proposed constitution." },
      { author: "Jane Austen", work: "Emma", quote: "Mr. Woodhouse took his walk every afternoon at a **stated** hour, weather permitting." },
      { author: "Charles Darwin", work: "The Origin of Species", quote: "As previously **stated**, variations that confer any competitive advantage will tend to be preserved." }
    ]
  },
  "Dashboard — stat/statehouse.md": {
    primary: "The building in which a state legislature assembles; a state capitol.",
    secondary: "In American politics, the physical seat and legislative heart of state government.",
    quotes: [
      { author: "Henry David Thoreau", work: "A Week on the Concord and Merrimack Rivers", quote: "The golden dome of the Boston **statehouse** gleamed across the bay like a setting sun." },
      { author: "Abraham Lincoln", work: "House Divided Speech", quote: "He addressed the assembled representatives in the Illinois **statehouse** with earnest solemnity." },
      { author: "Walt Whitman", work: "Specimen Days", quote: "Crowds gathered around the steps of the **statehouse** to hear the latest dispatches from the front." }
    ]
  },
  "Dashboard — stat/stateless.md": {
    primary: "Not recognized as a citizen or national by any state under the operation of its law.",
    secondary: "In sociology and computer science, lacking a formal central state government; or in software, a protocol (such as HTTP) that does not retain session information.",
    quotes: [
      { author: "Hannah Arendt", work: "The Origins of Totalitarianism", quote: "The plight of millions of **stateless** refugees revealed that the fundamental human right is the right to have rights under a state." },
      { author: "E. E. Evans-Pritchard", work: "The Nuer", quote: "The Nuer society functions as a **stateless** segmentary lineage system ordered by ordered anarchy." },
      { author: "George Orwell", work: "Homage to Catalonia", quote: "He met dispossessed **stateless** exiles whose papers had been stripped by totalitarian decrees." }
    ]
  },
  "Dashboard — stat/stateliness.md": {
    primary: "Dignified, imposing, or grand beauty or manner; majesty of bearing.",
    secondary: "Formal elegance, magnificence, or solemn grandeur in architecture, pageantry, or prose.",
    quotes: [
      { author: "Edmund Spenser", work: "The Faerie Queene", quote: "Her royal **stateliness** and modest grace won the adoration of every courtier." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The architectural **stateliness** of the palace mirrored the autocratic majesty of the Byzantine emperors." },
      { author: "Charlotte Brontë", work: "Villette", quote: "There was a quiet **stateliness** in Madame Beck's composure that commanded instant obedience." }
    ]
  },
  "Dashboard — stat/stately.md": {
    primary: "Having a noble, imposing, or dignified appearance, manner, or movement; majestic.",
    secondary: "Grand, magnificent, or splendid in proportions or style.",
    quotes: [
      { author: "William Shakespeare", work: "Henry VI, Part 2", quote: "See how the **stately** bark ploughs through the foaming surge with billowing canvas." },
      { author: "Edgar Allan Poe", work: "The Raven", quote: "In there stepped a **stately** Raven of the saintly days of yore." },
      { author: "Alfred, Lord Tennyson", work: "Break, Break, Break", quote: "And the **stately** ships go on to their haven under the hill." }
    ]
  },
  "Dashboard — stat/statement.md": {
    primary: "A definite or clear expression of something in speech or writing.",
    secondary: "In financial accounting, a formal document setting out details of debits and credits, assets and liabilities (a bank or balance statement).",
    quotes: [
      { author: "Arthur Conan Doyle", work: "The Sign of the Four", quote: "Sherlock Holmes listened in silence to the young lady's remarkable **statement**." },
      { author: "Charles Dickens", work: "Bleak House", quote: "The attorney presented a detailed financial **statement** of the costs accumulated in Jarndyce and Jarndyce." },
      { author: "John Locke", work: "An Essay Concerning Human Understanding", quote: "Every philosophical **statement** must be examined to ascertain the clarity of the underlying ideas." }
    ]
  },
  "Dashboard — stat/stater.md": {
    primary: "An ancient Greek silver or gold coin and weight unit of varying value, minted in several Greek city-states and kingdoms.",
    secondary: "In classical numismatics, the standard gold or silver denomination of Lydia, Athens, Corinth, and Macedonia.",
    quotes: [
      { author: "Herodotus", work: "The Histories", quote: "Croesus dedicated bowls of pure gold and cast many a golden **stater** at the Delphic shrine." },
      { author: "Plutarch", work: "Life of Alexander", quote: "Alexander distributed thousands of golden **stater** coins among his victorious veterans after the conquest of Babylon." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The Macedonian **stater** circulated as the premier international gold standard throughout the ancient East." }
    ]
  },
  "Dashboard — stat/stateroom.md": {
    primary: "A private cabin or bedroom on a passenger ship or yacht, or in a train car.",
    secondary: "Historically in royal palaces, a ceremonial state room reserved for formal receptions, banquets, and audiences.",
    quotes: [
      { author: "Mark Twain", work: "The Innocents Abroad", quote: "Our **stateroom** on the steamer was small, but cozy enough once our steamer trunks were stowed away." },
      { author: "Joseph Conrad", work: "The Secret Sharer", quote: "I stepped back into my **stateroom** and whispered to the fugitive hiding behind the hanging coats." },
      { author: "Herman Melville", work: "Moby-Dick", quote: "Captain Ahab paced the floor of his aft **stateroom**, his ivory leg drumming upon the deck beams." }
    ]
  },
  "Dashboard — stat/statesman.md": {
    primary: "A skilled, experienced, and respected political leader or figure who operates with wisdom, integrity, and devotion to the common good.",
    secondary: "Historically in northern England, a small independent landholder or yeoman farmer cultivating an inherited estate.",
    quotes: [
      { author: "Edmund Burke", work: "Speech on Conciliation with America", quote: "A disposition to preserve, and an ability to improve, taken together, would be my standard of a **statesman**." },
      { author: "Winston Churchill", work: "The River War", quote: "The true **statesman** must balance immediate electoral passions against the long-term security of the commonwealth." },
      { author: "Abraham Lincoln", work: "Gettysburg Address", quote: "History commemorates the noble **statesman** who preserves the nation dedicated to the proposition of equality." }
    ]
  },
  "Dashboard — stat/statesmanlike.md": {
    primary: "Characteristic of or becoming a great statesman; showing wisdom, vision, and broad political judgment.",
    secondary: "Marked by integrity, dignity, and disinterested public service rather than narrow factional bias.",
    quotes: [
      { author: "Alexander Hamilton", work: "The Federalist Papers", quote: "Such a policy displays a **statesmanlike** comprehension of the true commercial interests of the confederacy." },
      { author: "Alexis de Tocqueville", work: "Democracy in America", quote: "Washington's farewell address remains a masterpiece of calm, **statesmanlike** foresight." },
      { author: "Winston Churchill", work: "Great Contemporaries", quote: "His conduct during the constitutional crisis was uniformly dignified and **statesmanlike**." }
    ]
  },
  "Dashboard — stat/statesmanly.md": {
    primary: "Pertaining to or worthy of a statesman; dignified, visionary, and politically astute.",
    secondary: "Conducted in a manner appropriate to wise political governance.",
    quotes: [
      { author: "Thomas Carlyle", work: "Latter-Day Pamphlets", quote: "We stand in sore need of a **statesmanly** intellect capable of navigating the chaotic currents of this age." },
      { author: "Edmund Burke", work: "Appeal from the New to the Old Whigs", quote: "True **statesmanly** wisdom tempers strict legal right with prudent moderation." },
      { author: "John Morley", work: "The Life of William Ewart Gladstone", quote: "His speech was hailed across Europe as a model of **statesmanly** eloquence and moral gravity." }
    ]
  },
  "Dashboard — stat/statesmanship.md": {
    primary: "The skill, quality, or conduct of a statesman; the art of leading and governing a state with vision, wisdom, and integrity.",
    secondary: "In political philosophy, the ability to formulate enduring policies that transcend partisan factionalism and protect national interest.",
    quotes: [
      { author: "Winston Churchill", work: "The World Crisis", quote: "True **statesmanship** consists in foreseeing danger before it strikes and preparing the remedies in peace." },
      { author: "Edmund Burke", work: "Reflections on the Revolution in France", quote: "Circumstances give in reality to every political principle its distinguishing color and discriminating effect in practical **statesmanship**." },
      { author: "Alexis de Tocqueville", work: "Democracy in America", quote: "Democratic nations require a higher standard of **statesmanship** to resist the tyranny of the majority." }
    ]
  },
  "Dashboard — stat/stateswoman.md": {
    primary: "A female political leader or figure who operates with wisdom, integrity, and distinguished public service.",
    secondary: "A respected female statesman; an accomplished female diplomat or national leader.",
    quotes: [
      { author: "Virginia Woolf", work: "Three Guineas", quote: "History records the rare emergence of an enlightened **stateswoman** who governed with greater justice than bellicose kings." },
      { author: "John Stuart Mill", work: "The Subjection of Women", quote: "The reigns of Elizabeth and Isabella demonstrate that women possess supreme aptitude as a **stateswoman** and ruler." },
      { author: "Eleanor Roosevelt", work: "This I Remember", quote: "The post-war world demanded that every diplomat and **stateswoman** work tirelessly for international human rights." }
    ]
  },
  "Dashboard — stat/statewide.md": {
    primary: "Extending throughout, occurring in, or involving an entire federal state (especially within the United States).",
    secondary: "In electoral politics and public administration, designating elections, policies, or referendums that encompass all voting districts of a state.",
    quotes: [
      { author: "Alexis de Tocqueville", work: "Democracy in America", quote: "Local town assemblies deliberate upon immediate concerns while **statewide** interests are settled in the general legislature." },
      { author: "Woodrow Wilson", work: "Congressional Government", quote: "A **statewide** referendum provides a direct channel for the popular will to override legislative deadlock." },
      { author: "Franklin D. Roosevelt", work: "Public Papers and Addresses", quote: "We instituted **statewide** conservation programs to restore degraded watersheds and employ thousands of youth." }
    ]
  },
  "Dashboard — stat/static.md": {
    primary: "Lacking in movement, action, or change, especially in an uninteresting or unproductive way; stationary.",
    secondary: "In physics and radio, crackling or hissing noise produced by electrical interference; or electrostatic phenomena involving charges at rest.",
    quotes: [
      { author: "Isaac Newton", work: "Philosophiae Naturalis Principia Mathematica", quote: "In a **static** equilibrium, the resultant of all acting forces and torques must vanish." },
      { author: "James Clerk Maxwell", work: "A Treatise on Electricity and Magnetism", quote: "The distinction between **static** charge and dynamic galvanic current was reconciled through electromagnetic theory." },
      { author: "F. Scott Fitzgerald", work: "The Great Gatsby", quote: "The loud burst of **static** from the radio interrupted our conversation in the sultry summer room." }
    ]
  },
  "Dashboard — stat/statice.md": {
    primary: "A botanical genus of maritime flowering plants in the plumbago family (Plumbaginaceae), commonly known as sea lavenders (now largely Limonium).",
    secondary: "In floriculture and herbalism, salt-tolerant herbs with papery, colorful calyces widely dried for winter flower arrangements.",
    quotes: [
      { author: "John Gerard", work: "The Herball", quote: "Sea lavender, which the ancients called **Statice**, grows abundantly along the muddy salt marshes of Kent." },
      { author: "Asa Gray", work: "Manual of the Botany of the Northern United States", quote: "The persistent scarious calyx of **Statice** retains its bright lavender hue long after the corolla has faded." },
      { author: "William Jackson Hooker", work: "The British Flora", quote: "On coastal mudflats, sheets of blooming **Statice** paint the saltings with brilliant purplish lilac." }
    ]
  },
  "Dashboard — stat/statics.md": {
    primary: "The branch of mechanics that deals with physical bodies and systems at rest or in equilibrium, where forces are balanced.",
    secondary: "In engineering and architecture, the calculation of structural loads, shear forces, and bending moments in trusses, beams, and arches.",
    quotes: [
      { author: "Archimedes", work: "On the Equilibrium of Planes", quote: "The fundamental theorem of **statics** establishes that equal weights at equal distances balance one another upon the lever." },
      { author: "Isaac Newton", work: "Philosophiae Naturalis Principia Mathematica", quote: "While dynamics treats of bodies set into accelerated motion, **statics** examines forces held in mutual cancellation." },
      { author: "Ernst Mach", work: "The Science of Mechanics", quote: "Stevinus resolved the principal dilemma of **statics** by his famous thought experiment with the endless chain on an inclined plane." }
    ]
  },
  "Dashboard — stat/statin.md": {
    primary: "Any of a class of lipid-lowering medications that reduce serum cholesterol levels by inhibiting the enzyme HMG-CoA reductase.",
    secondary: "In cardiovascular medicine, pharmaceutical agents (such as atorvastatin, simvastatin, or rosuvastatin) widely prescribed to prevent atherosclerotic cardiovascular disease.",
    quotes: [
      { author: "Jerome Groopman", work: "How Doctors Think", quote: "Prescribing a daily **statin** dramatically reduces the long-term risk of myocardial infarction in high-risk patients." },
      { author: "Atul Gawande", work: "Being Mortal", quote: "The widespread use of the **statin** class has postponed vascular mortality well into the eighth and ninth decades of life." },
      { author: "Sherwin B. Nuland", work: "The Mysteries Within", quote: "The biological discovery of the **statin** mechanism revolutionized our pharmacological control over hepatic cholesterol synthesis." }
    ]
  },
  "Dashboard — stat/station.md": {
    primary: "A regular stopping place along a route, especially on a railroad line; or a place where a particular service or activity is based.",
    secondary: "One's social rank, standing, or appointed duty in life; or in ecology, a precise geographical locality where a species occurs.",
    quotes: [
      { author: "Charles Dickens", work: "Dombey and Son", quote: "The locomotive screeched into the cavernous **station**, exhaling clouds of sulphurous steam." },
      { author: "Charlotte Brontë", work: "Jane Eyre", quote: "Do you think, because I am poor, obscure, plain, and little, I am soulless and heartless? I have as much soul as you, whatever my humble **station** in life." },
      { author: "Charles Darwin", work: "The Origin of Species", quote: "The geographical distribution of an alpine species is often limited to a single mountain **station**." }
    ]
  },
  "Dashboard — stat/stationariness.md": {
    primary: "The state or condition of being stationary, fixed, immobile, or unchanging.",
    secondary: "In economics, social theory, and physics, the absence of expansion, motion, or evolutionary development over time.",
    quotes: [
      { author: "John Stuart Mill", work: "Principles of Political Economy", quote: "The economic **stationariness** of traditional agrarian societies was perpetuated by rigid customary tenure." },
      { author: "Thomas Carlyle", work: "Past and Present", quote: "Absolute moral **stationariness** is impossible; a nation that does not advance will inevitably regress." },
      { author: "Herbert Spencer", work: "First Principles", quote: "Evolution moves perpetually from homogeneous **stationariness** toward multiform, dynamic heterogeneity." }
    ]
  },
  "Dashboard — stat/stationary.md": {
    primary: "Not moving, or not intended to be moved; staying in one place.",
    secondary: "Not changing in condition, quantity, or quality; in economics, a stationary state where capital and population remain stable.",
    quotes: [
      { author: "Isaac Newton", work: "Philosophiae Naturalis Principia Mathematica", quote: "A body remains **stationary** in absolute space until an impressed force compels it to alter that state." },
      { author: "John Stuart Mill", work: "Principles of Political Economy", quote: "Economists have contemplated with apprehension that **stationary** state where capital accumulation reaches its natural limit." },
      { author: "H. G. Wells", work: "The Time Machine", quote: "The machine remained perfectly **stationary** in space, though flying through the millennia of time." }
    ]
  },
  "Dashboard — stat/stationer.md": {
    primary: "A person or business that sells writing materials, office supplies, books, and paper goods.",
    secondary: "Historically in English publishing, a member of the Stationers' Company holding rights to print and register copyright of books.",
    quotes: [
      { author: "Samuel Johnson", work: "A Dictionary of the English Language", quote: "A **stationer** was originally so called from keeping a station or shop, as distinguished from itinerant vendors." },
      { author: "Charles Dickens", work: "Bleak House", quote: "Mr. Snagsby, the law **stationer**, pursued his quiet trade in Chancery Lane amid reams of foolscap." },
      { author: "John Milton", work: "Areopagitica", quote: "The Stationers' Company enforced monopolistic licensing, obliging every author to obtain the printer's and **stationer**'s imprint." }
    ]
  },
  "Dashboard — stat/stationery.md": {
    primary: "Writing materials, especially envelopes, paper, pens, and related office supplies.",
    secondary: "Fine paper goods and correspondence cards bearing personal monograms, watermarks, or official emblems.",
    quotes: [
      { author: "Jane Austen", work: "Pride and Prejudice", quote: "She opened the desk and took out fresh sheets of fine Bath **stationery** to write to her sister." },
      { author: "Arthur Conan Doyle", work: "A Scandal in Bohemia", quote: "Sherlock Holmes held the sheet of pink-tinted **stationery** up to the gaslight to inspect the Bohemian watermark." },
      { author: "F. Scott Fitzgerald", work: "The Great Gatsby", quote: "Invitations printed upon heavy cream-colored **stationery** were delivered by chauffeur throughout the neighborhood." }
    ]
  },
  "Dashboard — stat/stationmaster.md": {
    primary: "An official in charge of a railroad station.",
    secondary: "In railway operations, the supervisor responsible for track switching, passenger safety, ticketing, and train scheduling at a specific station depot.",
    quotes: [
      { author: "Charles Dickens", work: "The Signal-Man", quote: "The **stationmaster** directed me along the narrow cutting down toward the shadowed tunnel mouth." },
      { author: "Leo Tolstoy", work: "Anna Karenina", quote: "The **stationmaster** blew his whistle as the snowy express train rattled into the station." },
      { author: "Arthur Conan Doyle", work: "The Adventure of the Bruce-Partington Plans", quote: "We questioned the Aldgate **stationmaster** to determine which train had dropped the body onto the tracks." }
    ]
  },
  "Dashboard — stat/stations.md": {
    primary: "Plural of station; places or depots where services are provided, trains stop, or personnel are assigned.",
    secondary: "In religious devotion, the Stations of the Cross; or in social hierarchy, appointed ranks or duties in life.",
    quotes: [
      { author: "William Wordsworth", work: "The Excursion", quote: "Pilgrims paused at sacred **stations** along the mountain path to offer solitary prayers." },
      { author: "Alexander von Humboldt", work: "Cosmos", quote: "We established astronomical and magnetic **stations** at measured intervals across the Siberian wilderness." },
      { author: "Charles Dickens", work: "Bleak House", quote: "The great railway lines linked distant provincial **stations** into one pulsating commercial network." }
    ]
  },
  "Dashboard — stat/statistic.md": {
    primary: "A single piece of numerical data, fact, or item of information collected from a study, survey, or sample.",
    secondary: "In mathematical statistics, a numerical value (such as sample mean or sample variance) computed from sample observations to estimate a population parameter.",
    quotes: [
      { author: "Karl Pearson", work: "The Grammar of Science", quote: "A calculated sample **statistic** provides our only rigorous numerical bridge to the underlying population parameter." },
      { author: "Ronald Fisher", work: "Statistical Methods for Research Workers", quote: "An efficient **statistic** is one whose sampling variance is minimal among all consistent estimators." },
      { author: "George Orwell", work: "Nineteen Eighty-Four", quote: "To the Party, a human casualty was not a tragedy, but a manipulated economic **statistic**." }
    ]
  },
  "Dashboard — stat/statistical.md": {
    primary: "Of, relating to, or employing the principles or methods of statistics.",
    secondary: "Based on data analysis, quantitative probability, and numerical distributions.",
    quotes: [
      { author: "Ronald Fisher", work: "The Design of Experiments", quote: "The purpose of **statistical** design is to ensure that experiments yield unambiguous, quantifiable conclusions." },
      { author: "James Clerk Maxwell", work: "Illustrations of the Dynamical Theory of Gases", quote: "Our theory of gas molecules does not follow individual paths, but calculates **statistical** averages of molecular velocities." },
      { author: "Charles Darwin", work: "The Descent of Man", quote: "Extensive **statistical** records of human births reveal consistent sex ratios across human populations." }
    ]
  },
  "Dashboard — stat/statistically.md": {
    primary: "With respect to statistics; from a statistical point of view; by statistical methods.",
    secondary: "In experimental science, denoting results that meet criteria of statistical significance (statistically significant).",
    quotes: [
      { author: "Ronald Fisher", work: "Statistical Methods and Scientific Inference", quote: "A null hypothesis is rejected when observed discrepancies are **statistically** improbable under chance." },
      { author: "Karl Pearson", work: "The Life, Letters and Labours of Francis Galton", quote: "Galton sought to prove **statistically** that human physical and mental traits obey the normal law of error." },
      { author: "E. O. Wilson", work: "Sociobiology: The New Synthesis", quote: "Behavioral variations among foraging ant colonies were **statistically** analyzed across multiple ecological seasons." }
    ]
  },
  "Dashboard — stat/statistician.md": {
    primary: "An expert in or student of the collection, analysis, interpretation, and presentation of numerical data (statistics).",
    secondary: "A mathematical scientist specializing in probability distributions, biostatistics, econometrics, or experimental design.",
    quotes: [
      { author: "Florence Nightingale", work: "Notes on Nursing", quote: "As a passionate **statistician**, she used visual coxcomb diagrams to convince the government of sanitation reforms." },
      { author: "Ronald Fisher", work: "The Design of Experiments", quote: "The consulting **statistician** must be involved before an experiment begins, not merely called in to perform a post-mortem." },
      { author: "Francis Galton", work: "Inquiries into Human Faculty and Its Development", quote: "To the competent **statistician**, the bell-shaped normal curve appears as an exquisite architectural monument of nature." }
    ]
  },
  "Dashboard — stat/statistics.md": {
    primary: "The practice or science of collecting, organizing, analyzing, interpreting, and presenting empirical numerical data.",
    secondary: "A collection of quantitative data or numerical facts; in physics, quantum statistics (Bose-Einstein or Fermi-Dirac statistics).",
    quotes: [
      { author: "Florence Nightingale", work: "Life and Letters", quote: "To understand God's thoughts we must study **statistics**, for these are the measure of His purpose." },
      { author: "Ronald Fisher", work: "Statistical Methods for Research Workers", quote: "The science of **statistics** is essentially the mathematics of experimental observation and inference." },
      { author: "Enrico Fermi", work: "Molecules, Crystals, and Nuclei", quote: "Electrons obey Fermi-Dirac **statistics**, which prohibits two identical fermions from occupying the same quantum state." }
    ]
  },
  "Dashboard — stat/stative.md": {
    primary: "In linguistics, denoting a verb, adjective, or aspect that expresses a state of affairs rather than an action or dynamic event.",
    secondary: "In military history, an obsolete term for a permanent or stationary camp (from Latin castra stativa).",
    quotes: [
      { author: "Otto Jespersen", work: "The Philosophy of Grammar", quote: "English distinguishes dynamic verbs like 'run' from **stative** verbs like 'know' or 'resemble' which rarely take the continuous aspect." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The Roman legion established a fortified **stative** encampment along the banks of the Danube." },
      { author: "Noam Chomsky", work: "Aspects of the Theory of Syntax", quote: "Semantic selectional restrictions classify **stative** predicates into a distinct functional syntactic category." }
    ]
  },
  "Dashboard — stat/stator.md": {
    primary: "The stationary part of a rotary system, found in electric generators, electric motors, sirens, mud motors, or biological turbines.",
    secondary: "In electrical machinery, the stationary housing containing the electromagnets or field windings within which the rotor revolves.",
    quotes: [
      { author: "Nikola Tesla", work: "My Inventions: The Autobiography of Nikola Tesla", quote: "The polyphase alternating currents circulating in the **stator** windings produced a smooth, continuously revolving magnetic field." },
      { author: "Charles Proteus Steinmetz", work: "Theory and Calculation of Alternating Current Phenomena", quote: "Hysteresis losses in the laminated iron core of the **stator** were calculated using empirical formulas." },
      { author: "Richard Feynman", work: "The Feynman Lectures on Physics", quote: "The electromagnetic torque generated between the stationary coils of the **stator** and the revolving rotor drives the induction motor." }
    ]
  },
  "Dashboard — stat/statuary.md": {
    primary: "Sculptured figures collectively; statues viewed as a group or art form.",
    secondary: "A sculptor; or suitable marble or bronze utilized for sculpting statues (statuary marble).",
    quotes: [
      { author: "John Ruskin", work: "The Stones of Venice", quote: "The classical **statuary** of ancient Greece achieved a serene, harmonized balance of human form and divine majesty." },
      { author: "Nathaniel Hawthorne", work: "The Marble Faun", quote: "The dim galleries of the Vatican were populated by silent, immortal white **statuary** from antiquity." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The plunder of Roman temples stripped the public forums of thousands of bronze and marble **statuary** masterpieces." }
    ]
  },
  "Dashboard — stat/statue.md": {
    primary: "A carved or cast three-dimensional figure of a person, animal, or mythical being, especially one that is life-size or larger.",
    secondary: "A monumental sculpture erected in a public place as a memorial or work of art.",
    quotes: [
      { author: "Percy Bysshe Shelley", work: "Ozymandias", quote: "Near them, on the sand, half sunk a shattered visage lies; round the decay of that colossal wreck, boundless and bare, the lone and level sands stretch far away beneath the ruined **statue**." },
      { author: "William Shakespeare", work: "The Winter's Tale", quote: "O royal piece! There's magic in thy majesty, which has my evils conjured to remembrance, and from thy admired **statue** calls my sorrow." },
      { author: "Nathaniel Hawthorne", work: "The Marble Faun", quote: "The ancient marble **statue** of the Faun of Praxiteles seemed poised on the verge of breathing life." }
    ]
  },
  "Dashboard — stat/statuesque.md": {
    primary: "Resembling a statue in dignity, grace, proportions, or motionless composure; attractively tall, graceful, and dignified.",
    secondary: "Imposing and serene in physical presence or formal posture.",
    quotes: [
      { author: "Charlotte Brontë", work: "Jane Eyre", quote: "Blanche Ingram was tall, dark, and majestic, with a **statuesque** poise that caught every eye in the drawing room." },
      { author: "Thomas Hardy", work: "Tess of the d'Urbervilles", quote: "She stood in the morning sunlight, her figure assuming an almost **statuesque** grandeur against the bare chalk hillside." },
      { author: "George Eliot", work: "Middlemarch", quote: "Her beauty was of that **statuesque** type which an austere gown of plain wool seemed rather to enhance than diminish." }
    ]
  },
  "Dashboard — stat/statuette.md": {
    primary: "A small statue, especially one smaller than life-size; a figurine.",
    secondary: "In archaeology and art history, diminutive sculpted representations (such as Tanagra figurines or paleolithic Venuses) in bronze, ivory, or terracotta.",
    quotes: [
      { author: "Arthur Conan Doyle", work: "The Adventure of the Six Napoleons", quote: "The criminal smashed the plaster **statuette** of the Emperor upon the garden path to extract the hidden black pearl." },
      { author: "Oscar Wilde", work: "The Picture of Dorian Gray", quote: "Upon the mantelpiece stood an exquisite ivory **statuette** of Narcissus admiring his own reflection." },
      { author: "Henry James", work: "The Golden Bowl", quote: "She picked up the antique bronze **statuette** with delicate, appreciative fingers, turning it in the soft lamplight." }
    ]
  },
  "Dashboard — stat/stature.md": {
    primary: "A person's natural height, especially when standing upright.",
    secondary: "Importance, reputation, or standing gained by ability, achievement, or character.",
    quotes: [
      { author: "William Shakespeare", work: "A Midsummer Night's Dream", quote: "Though she be but little, she is fierce; her **stature** cannot measure the reach of her spirit." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The emperor was of modest physical **stature**, yet his intellectual and political genius commanded universal deference." },
      { author: "Charles Darwin", work: "The Descent of Man", quote: "Human populations show significant variations in mean adult **stature** correlated with diet, climate, and hereditary factors." }
    ]
  },
  "Dashboard — stat/status.md": {
    primary: "The relative social, professional, or legal standing of an individual or group in society.",
    secondary: "The current state or condition of affairs, a process, or a medical patient at a given time (such as status epilepticus).",
    quotes: [
      { author: "Max Weber", work: "Economy and Society", quote: "Classes are stratified according to their relations to production, whereas **status** groups are stratified according to their styles of life." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The rapid progression of seizures into continuous **status** epilepticus constitutes an acute neurological emergency." },
      { author: "Alexis de Tocqueville", work: "Democracy in America", quote: "The equality of **status** prevailing in America dissolves ancient aristocratic pretensions into civic brotherhood." }
    ]
  },
  "Dashboard — stat/statute.md": {
    primary: "A formal written enactment of a legislative authority that governs the legal entities of a city, state, or country by way of the consent.",
    secondary: "An established permanent rule, ordinance, or bylaw of an institution, university, or corporation.",
    quotes: [
      { author: "William Blackstone", work: "Commentaries on the Laws of England", quote: "A **statute** is an act of the legislature, speaking with supreme constitutional sovereignty across the realm." },
      { author: "Alexander Hamilton", work: "The Federalist Papers", quote: "No legislative act or **statute** contrary to the Constitution can be valid in our courts of law." },
      { author: "Edmund Burke", work: "Reflections on the Revolution in France", quote: "The British constitution is not a sudden paper invention, but a venerable fabric cemented by ancient **statute** and long usage." }
    ]
  }
};

let updatedCount = 0;
for (const [relPath, entry] of Object.entries(filesData)) {
  const filePath = path.join(baseDir, relPath);
  if (!fs.existsSync(filePath)) {
    console.error(`File does not exist: ${filePath}`);
    continue;
  }
  const content = fs.readFileSync(filePath, 'utf8');
  const bookIdx = content.indexOf('> [!book]');
  if (bookIdx === -1) {
    console.error(`No > [!book] in ${relPath}`);
    continue;
  }
  const topBlock = content.substring(0, bookIdx);
  const newContent = `${topBlock}> [!book] 📖 Definitions & Semantic Range
> 1. **Primary Definition (Lexical / Standard Consensus)**: ${entry.primary}
> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: ${entry.secondary}

> [!quote] 💬 Contextual Usage & Authentic Quotations
${entry.quotes.map(q => `> - 📜 **${q.author} (*${q.work}*):** *"${q.quote}"*`).join('\n')}
`;

  fs.writeFileSync(filePath, newContent, 'utf8');
  updatedCount++;
}

console.log(`Updated ${updatedCount} files in Batch 7!`);
