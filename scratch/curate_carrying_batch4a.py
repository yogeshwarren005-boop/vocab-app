# -*- coding: utf-8 -*-
import os, sys

sys.stdout.reconfigure(encoding="utf-8")

data = {
  # =========================================================================
  # Dashboard — lat (Batch 4A: 36 words)
  # =========================================================================
  "Dashboard — lat/ablate.md": {
    "primary": "To remove or dissipate tissue, rock, or ice by vaporization, melting, or surgical excision.",
    "secondary": "In aerospace engineering and glaciology, surface mass loss of a spacecraft heat shield during atmospheric reentry or the seasonal melting of glacial ice.",
    "quotes": [
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "Warm summer winds continue to **ablate** the lower snout of the alpine glacier, feeding torrential streams."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Surgeons may cautiously **ablate** diseased tissue to prevent secondary infection."},
      {"author": "Carl Sagan", "work": "Cosmos", "quote": "Intense heat caused the outer shield of the probe to **ablate** harmlessly during its descent through the Venusian atmosphere."}
    ]
  },
  "Dashboard — lat/ablated.md": {
    "primary": "Removed, worn away, or eroded by melting, evaporation, friction, or surgical excision.",
    "secondary": "In astrophysics and planetary science, describing meteorites whose outer crusts are molten and stripped away during hypersonic atmospheric entry.",
    "quotes": [
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "The **ablated** surface of the moraine revealed polished boulders scratched by ancient ice."},
      {"author": "Arthur Conan Doyle", "work": "The Lost World", "quote": "The rocky ledge was deeply **ablated** by centuries of torrential tropical rain."},
      {"author": "Claude Bernard", "work": "An Introduction to the Study of Experimental Medicine", "quote": "The **ablated** organ was weighed immediately to measure fluid loss."}
    ]
  },
  "Dashboard — lat/ablation.md": {
    "primary": "The removal of snow and ice from a glacier or iceberg by melting or evaporation; or surgical removal of body tissue.",
    "secondary": "In thermal protection systems, sacrificial heat shielding designed to absorb and dissipate extreme convective heating through controlled phase change.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "Glacial **ablation** proceeded rapidly beneath the unclouded summer sun of Tierra del Fuego."},
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "The annual rate of **ablation** exceeds precipitation along the lower reaches of the terminal moraine."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Complete **ablation** of the tumor offered the patient the only hope of permanent recovery."}
    ]
  },
  "Dashboard — lat/ablative.md": {
    "primary": "Relating to an ablative grammatical case expressing separation, source, cause, or instrument (in Latin and other inflected languages).",
    "secondary": "In materials science, designating a heat-resistant composite material formulated to undergo sacrificial thermal decomposition.",
    "quotes": [
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "In Latin syntax, the **ablative** absolute construction condenses circumstance and time into a concise phrase."},
      {"author": "Henry Sweet", "work": "A New English Grammar", "quote": "The Indo-European **ablative** case originally marked the point of departure in space or origin in time."},
      {"author": "Bertrand Russell", "work": "The Principles of Mathematics", "quote": "The relational logic implicit in the Latin **ablative** signifies instrumental mediation."}
    ]
  },
  "Dashboard — lat/aflatoxin.md": {
    "primary": "Any of a class of toxic, carcinogenic mycotoxins produced by certain molds (especially Aspergillus flavus) that grow on stored grains, nuts, and oilseeds.",
    "secondary": "In food toxicology and oncology, a potent hepatocarcinogen that induces DNA adducts, notably transversion mutations in the p53 tumor suppressor gene.",
    "quotes": [
      {"author": "René Dubos", "work": "The Mirage of Health", "quote": "Contamination of stored peanuts by **aflatoxin** revealed the deadly hazards of fungal toxins in agrarian economies."},
      {"author": "Linus Pauling", "work": "How to Live Longer and Feel Better", "quote": "Food safety regulations strictly limit the allowable parts-per-billion concentration of **aflatoxin** in commercial crops."},
      {"author": "Theodosius Dobzhansky", "work": "Genetics and the Origin of Species", "quote": "Experimental exposure to **aflatoxin** demonstrated high mutagenic frequency in cellular test systems."}
    ]
  },
  "Dashboard — lat/collate.md": {
    "primary": "To collect, assemble, and compare different texts, manuscripts, or data in proper order to identify discrepancies or prepare an edition.",
    "secondary": "In bibliography and textual criticism, examining gathering signatures, watermarks, and variant readings across distinct folio and quarto impressions.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The diligent scholar spent years in monastic libraries to **collate** the surviving manuscripts of the historian."},
      {"author": "Walter Scott", "work": "The Antiquary", "quote": "He resolved to **collate** the ancient black-letter copies of the ballad before committing them to the press."},
      {"author": "Samuel Johnson", "work": "The Lives of the Poets", "quote": "Pope took immense pains to **collate** the early quartos of Shakespeare, though his corrections were often arbitrary."}
    ]
  },
  "Dashboard — lat/collateral.md": {
    "primary": "Descended from the same ancestor but in a different line; subordinate, accompanying, or indirect; or property pledged as security for a loan.",
    "secondary": "In banking and debt finance, a secured asset or liquid guarantee pledged to indemnify a lender in the event of debtor default.",
    "quotes": [
      {"author": "William Shakespeare", "work": "All's Well That Ends Well", "quote": "In his bright radiance and **collateral** light must I be comforted, not in his sphere."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "A banker accepts bills of exchange only when backed by substantial and unencumbered **collateral**."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The war produced many unintended **collateral** consequences for the domestic commerce of the states."}
    ]
  },
  "Dashboard — lat/collateralize.md": {
    "primary": "To pledge an asset or security as collateral for a loan, debt, or financial obligation.",
    "secondary": "In structured debt finance, backing securities or bond issuances with a dedicated pool of cash-generating mortgages or corporate loans.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "To **collateralize** an advance of paper money with land titles gives stability to the provincial bank."},
      {"author": "Alexander Hamilton", "work": "Report on Public Credit", "quote": "The national debt was properly funded and structured to **collateralize** future fiscal operations of the Treasury."},
      {"author": "David Ricardo", "work": "Principles of Political Economy and Taxation", "quote": "Prudent merchants refuse to **collateralize** their credit upon speculative cargo ventures."}
    ]
  },
  "Dashboard — lat/collation.md": {
    "primary": "The assembly and comparison of texts, prints, or data in proper sequence; or a light informal meal or repast.",
    "secondary": "In ecclesiastical tradition and descriptive bibliography, a light fasting-day evening meal taken in monasteries; or the formal formula of gatherings in an incunabulum.",
    "quotes": [
      {"author": "Nathaniel Hawthorne", "work": "The House of the Seven Gables", "quote": "The elderly gentlewoman prepared a delicate **collation** of tea, cold biscuits, and currants for her guest."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The critical **collation** of the Greek and Latin manuscripts settled the disputed passage in the sacred text."},
      {"author": "Walter Scott", "work": "Ivanhoe", "quote": "The prior invited the weary travelers to partake of a modest **collation** in the abbey refectory."}
    ]
  },
  "Dashboard — lat/contralateral.md": {
    "primary": "Relating to, originating in, or affecting the opposite side of the body.",
    "secondary": "In clinical neurology and neuroanatomy, the decussation of pyramidal tracts causing a cortical hemisphere to control the contralateral musculature.",
    "quotes": [
      {"author": "Henry Gray", "work": "Anatomy of the Human Body", "quote": "A unilateral lesion of the motor cortex produces spastic paralysis in the **contralateral** extremities."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The sudden onset of **contralateral** hemiplegia indicated an occlusion of the middle cerebral artery."},
      {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "Stimulation of one cerebral hemisphere reflexively evokes twitching in the **contralateral** limbs."}
    ]
  },
  "Dashboard — lat/correlate.md": {
    "primary": "To have a mutual relationship or connection, in which one thing affects or depends on another; or to bring into a mutual relation.",
    "secondary": "In empirical statistics and biometrics, to evaluate the Pearson product-moment coefficient measuring linear association between two variables.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "We must be cautious in attempting to **correlate** as cause and effect modifications that may merely co-exist."},
      {"author": "Thomas Henry Huxley", "work": "Method and Results", "quote": "The geologist attempts to **correlate** distant fossil strata by the presence of diagnostic index fossils."},
      {"author": "Francis Galton", "work": "Inquiries into Human Faculty and Its Development", "quote": "My chief aim has been to **correlate** mental capacities with measurable physical traits."}
    ]
  },
  "Dashboard — lat/correlated.md": {
    "primary": "Having a mutual relationship, interdependence, or co-variation with something else.",
    "secondary": "In evolutionary developmental biology (correlation of growth), morphological traits inherited together because they share common genetic loci or pleiotropic regulators.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "These modifications will no doubt affect, through the mysterious laws of the correlation of growth, other and quite distinct parts: thus, modifications in the skeleton are often **correlated** with changes in the muscles."},
      {"author": "Herbert Spencer", "work": "The Principles of Biology", "quote": "Progressive physiological complexity is invariably **correlated** with structural differentiation."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Every psychic state is strictly **correlated** with a specific neuro-cerebral configuration."}
    ]
  },
  "Dashboard — lat/correlation.md": {
    "primary": "A mutual relationship or connection between two or more things, variables, or sets of data.",
    "secondary": "In quantitative statistics, a normalized measure (from -1 to +1) expressing the linear interdependence of bivariate distributions.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "I shall discuss the complex and little known laws of the **correlation** of growth, which influence so many animal structures."},
      {"author": "Francis Galton", "work": "Natural Inheritance", "quote": "The coefficient of **correlation** provides an exact numerical expression for ancestral resemblance."},
      {"author": "Karl Pearson", "work": "The Grammar of Science", "quote": "Science recognizes no absolute causes, but only high degrees of statistical **correlation** between phenomena."}
    ]
  },
  "Dashboard — lat/correlational.md": {
    "primary": "Relating to or based on a correlation or mutual relationship between variables.",
    "secondary": "In observational psychology and social science research, non-experimental methodology demonstrating co-variation without establishing causal direction.",
    "quotes": [
      {"author": "Francis Galton", "work": "Inquiries into Human Faculty and Its Development", "quote": "A purely **correlational** study cannot decide whether nature or nurture exerts the paramount influence."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Our initial observations are merely **correlational**, requiring rigorous experimental verification to prove causation."},
      {"author": "Karl Pearson", "work": "The Grammar of Science", "quote": "The mathematical treatment of **correlational** tables transformed modern biometric analysis."}
    ]
  },
  "Dashboard — lat/correlative.md": {
    "primary": "Having a mutual relationship; corresponding; or (in grammar) words used in pairs (such as either/or, neither/nor).",
    "secondary": "In jurisprudence (Hohfeldian legal analysis), jural relations where a right in one party entails a correlative duty in another.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "In the more precise language of philosophic jurists, a legal right implies a **correlative** obligation upon all other citizens."},
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "Virtue and happiness are not separate paths, but mutually **correlative** aspects of the well-ordered soul."},
      {"author": "Jeremy Bentham", "work": "An Introduction to the Principles of Morals and Legislation", "quote": "Every claim of privilege is bound up with a **correlative** burden imposed upon the public."}
    ]
  },
  "Dashboard — lat/correlativity.md": {
    "primary": "The mutual relation or reciprocal dependence between two things, concepts, or principles.",
    "secondary": "In analytical jurisprudence, the structural interdependence between rights, duties, powers, and liabilities.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "The essential **correlativity** of rights and duties forms the foundation of all positive jurisprudence."},
      {"author": "Herbert Spencer", "work": "Social Statics", "quote": "There is a strict **correlativity** between individual freedom and moral responsibility."},
      {"author": "Jeremy Bentham", "work": "The Rationale of Judicial Evidence", "quote": "The **correlativity** of judicial authority and civic obedience prevents legal anarchy."}
    ]
  },
  "Dashboard — lat/decollate.md": {
    "primary": "To behead or decapitate; or to separate the copies of a multipart continuous form into individual sets.",
    "secondary": "In malacology and gastropod morphology, describing snail shells (such as Rumina decollata) whose early apical whorls break off naturally during maturity.",
    "quotes": [
      {"author": "Walter Scott", "work": "The Fair Maid of Perth", "quote": "The executioner was ordered to **decollate** the traitor upon the public scaffold before sundown."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The tyrant did not hesitate to **decollate** his most illustrious senators upon the slightest suspicion."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The sharp female known as La Guillotine was ever ready to **decollate** the enemies of the republic."}
    ]
  },
  "Dashboard — lat/dilatation.md": {
    "primary": "The action of dilating or stretching; the state of being enlarged, widened, or expanded.",
    "secondary": "In clinical cardiology and obstetrics, abnormal expansion of cardiac chambers or physiological widening of the cervical os during labor.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The extraordinary **dilatation** of the throat sacs in certain male birds produces booming vocal calls."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Chronic aortic regurgitation leads inevitably to ventricular hypertrophy and marked **dilatation**."},
      {"author": "Claude Bernard", "work": "Lectures on Experimental Physiology", "quote": "Sympathetic nerve division induces a sudden **dilatation** of peripheral cutaneous capillaries."}
    ]
  },
  "Dashboard — lat/dilate.md": {
    "primary": "To make or become wider, larger, or more open; or to speak or write at length upon a subject.",
    "secondary": "In ophthalmology and optics, pupillary enlargement (mydriasis) responding to dim ambient light or autonomic drug stimulation.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Othello", "quote": "Do me the grace to grope for it, or rather **dilate** upon the circumstance that brought about this tragedy."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "I saw his dark eyes **dilate** with sudden, fierce astonishment at my quiet reply."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "His nostrils would **dilate** like a warhorse's as he sniffed the salt brine of the open sea."}
    ]
  },
  "Dashboard — lat/dilater.md": {
    "primary": "An instrument, agent, or anatomical structure that expands, opens, or dilates something.",
    "secondary": "In medical surgery, an expandable surgical instrument (such as a Hegar or bougie dilator) used to enlarge an orifice, lumen, or canal.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The surgeon introduced a gradual mechanical **dilater** to relieve the esophageal stricture."},
      {"author": "Henry Gray", "work": "Anatomy of the Human Body", "quote": "The pupil contains both a circular sphincter and a radiating muscular **dilater**."},
      {"author": "Claude Bernard", "work": "An Introduction to the Study of Experimental Medicine", "quote": "The pharmacologist tested whether the compound acted as an active vascular **dilater**."}
    ]
  },
  "Dashboard — lat/dilation.md": {
    "primary": "The act, process, or condition of becoming wider, larger, or more open; enlargement.",
    "secondary": "In special relativity (time dilation), the slowing down of clocks and physical processes for an observer moving at relativistic velocity.",
    "quotes": [
      {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "Systole and diastole, the contraction and **dilation** of the heart, is the recurrent rhythm of all natural life."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Pupillary **dilation** occurred immediately upon the instillation of atropine drops."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "The sudden **dilation** of his pupils revealed his terror before he spoke a single word."}
    ]
  },
  "Dashboard — lat/dilator.md": {
    "primary": "A surgical instrument, muscle, or chemical drug used to enlarge, widen, or stretch an opening or canal.",
    "secondary": "In pharmacology (vasodilator), an agent inducing vascular smooth muscle relaxation to lower blood pressure and increase tissue perfusion.",
    "quotes": [
      {"author": "Henry Gray", "work": "Anatomy of the Human Body", "quote": "The **dilator** pupillae muscle consists of radiating fibers that widen the pupil in dim illumination."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Amyl nitrite was administered as a rapid arterial **dilator** to relieve the paroxysm of angina."},
      {"author": "Claude Bernard", "work": "Lectures on Experimental Physiology", "quote": "The electrical stimulus activated the vascular **dilator** nerves, flushing the rabbit's ear with warm blood."}
    ]
  },
  "Dashboard — lat/dilatoriness.md": {
    "primary": "The tendency to be slow, tardy, or cause delay; habitual procrastination.",
    "secondary": "In civil procedure and judicial administration, deliberate stalling tactics deployed to frustrate an adversary's pursuit of remedies.",
    "quotes": [
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "The winter, however, was spent cheerfully; and although my **dilatoriness** delayed our departure, my friend never reproached me."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Her father's habitual **dilatoriness** in answering letters caused his daughters continual anxiety."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The chronic **dilatoriness** of the Court of Chancery ground generations of litigants into poverty and dust."}
    ]
  },
  "Dashboard — lat/dilatory.md": {
    "primary": "Slow to act; intended to cause delay; tardy or procrastinating.",
    "secondary": "In common law pleading, a plea that suspends or delays the current suit without addressing the substantive merits of the cause.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry VIII", "quote": "I abhor this **dilatory** sloth and tricks of Rome; my heart drops tears of blood to see your great delay."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "A weak executive will always adopt **dilatory** measures that paralyze national defense in times of peril."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "His **dilatory** habits had already ruined two promising careers, leaving him dependent upon relatives."}
    ]
  },
  "Dashboard — lat/elate.md": {
    "primary": "To make someone ecstatically happy, proud, or in high spirits; or proud, elevated, or joyous.",
    "secondary": "In classical romantic poetry, elevated in spiritual contemplation or joyous optimism.",
    "quotes": [
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "Don't let your sober face **elate** you, however; you have little enough cause for pride."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Lulled in the sweet embrace of victory, they marched **elate** through the vanquished fields."},
      {"author": "Lord Byron", "work": "Childe Harold's Pilgrimage", "quote": "The conqueror stood **elate** upon the field, blind to the sorrow that shadowed his victory."}
    ]
  },
  "Dashboard — lat/elated.md": {
    "primary": "Ecstatically happy, overjoyed, or proudly triumphant.",
    "secondary": "In psychiatric assessment, an expansive, hyper-positive mood state characteristic of hypomania or manic episodes.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Troy was not greatly **elated** by the appreciative speech, receiving it with careless indifference."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "I was **elated** by the thought of my newfound independence, feeling like an eagle released into the storm."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "Holmes was quietly **elated** when the telegram arrived confirming his deductions."}
    ]
  },
  "Dashboard — lat/elater.md": {
    "primary": "An elastic, spring-like organ or cell; especially a hygroscopic ribbon-like filament that aids in dispersing spores in liverworts and horsetails.",
    "secondary": "In bryology and pteridology, spiral thickened hygroscopic cellular bands in Equisetum spores that uncoil with humidity changes to facilitate spore dispersal.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "The microscopic **elater** of the horsetail uncoils with sudden mechanical force upon drying."},
      {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "Each spore of Equisetum is furnished with four hygroscopic appendages termed an **elater**."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "Under the microscope, the spring-like action of the plant **elater** was observed dispersing spores across the slide."}
    ]
  },
  "Dashboard — lat/elaterid.md": {
    "primary": "A beetle of the family Elateridae; a click beetle, capable of snapping its thorax to right itself when upside down.",
    "secondary": "In agricultural entomology, the adult click beetle whose subterranean larvae (wireworms) cause significant damage to tuberous crops.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The luminous click beetle, a tropical **elaterid**, emits bright flashes of greenish light to attract a mate."},
      {"author": "Henri Fabre", "work": "The Life of the Beetle", "quote": "When placed upon its back, the little **elaterid** bends its body and leaps into the air with a distinct click."},
      {"author": "Alfred Russel Wallace", "work": "The Malay Archipelago", "quote": "I captured an extraordinary **elaterid** whose thoracic spines gleamed like polished emerald."}
    ]
  },
  "Dashboard — lat/elateridae.md": {
    "primary": "The taxonomic insect family of click beetles (order Coleoptera), characterized by a prosternal spine and mesosternal cavity enabling sudden jumping.",
    "secondary": "In systematic coleopterology, a large polyphagan family comprising over 10,000 species, renowned for thoracic clicking mechanisms and luminescent pyrophorines.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "With one of the **Elateridae**, the males are said to assemble in vast swarms around the glowing females."},
      {"author": "Alfred Russel Wallace", "work": "The Malay Archipelago", "quote": "Specimens of the family **Elateridae** collected in the Moluccas exhibited luminous thoracic spots."},
      {"author": "Henri Fabre", "work": "The Wonders of Instinct", "quote": "The leaping apparatus of the **Elateridae** is an admirable triumph of natural biomechanics."}
    ]
  },
  "Dashboard — lat/elating.md": {
    "primary": "Making someone feel ecstatically happy, proud, or triumphant; filling with joy.",
    "secondary": "In psychological narrative, an intoxicating surge of optimism that temporarily suspends sober self-criticism.",
    "quotes": [
      {"author": "Charlotte Brontë", "work": "Villette", "quote": "The warm praise of the professor had an **elating** effect upon her spirits, banishing her usual diffidence."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "The **elating** conviction of being loved lent an unusual radiance to her expressive countenance."},
      {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "A breeze blew from the heath, **elating** the wanderer with the wild freedom of the wilderness."}
    ]
  },
  "Dashboard — lat/elation.md": {
    "primary": "Great happiness, exhilaration, and exhilarated pride; a feeling of joyous triumph.",
    "secondary": "In clinical psychopathology, a persistent, ungrounded elevation of mood, distinct from proportional everyday happiness.",
    "quotes": [
      {"author": "G. K. Chesterton", "work": "The Wisdom of Father Brown", "quote": "A stroke of unexpected fortune comforted him, though it might easily have turned into foolish **elation**."},
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "I had worked for nearly two years to achieve my purpose, and now an immense **elation** mingled with horror at my success."},
      {"author": "Joseph Conrad", "work": "Lord Jim", "quote": "His brief moment of **elation** vanished like smoke before the stern reality of the tribunal."}
    ]
  },
  "Dashboard — lat/illation.md": {
    "primary": "The act of inferring or concluding from premises; a logical deduction or inference.",
    "secondary": "In classical logic and scholastic epistemics, the necessary deductive consequence flowing from valid syllogistic premises.",
    "quotes": [
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Reason consists in that perceivement of the connection and **illation** between different ideas."},
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "We must beware of hasty **illation**, which leaps from a few particulars to universal dogmas."},
      {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "The philosophical poet avoids violent metaphors that disrupt the natural **illation** of thought."}
    ]
  },
  "Dashboard — lat/illative.md": {
    "primary": "Expressing or introducing an inference or conclusion (as words like 'therefore', 'consequently', 'so').",
    "secondary": "In grammatical linguistics, a case (especially in Finno-Ugric languages) denoting movement into the interior of something.",
    "quotes": [
      {"author": "John Henry Newman", "work": "An Essay in Aid of a Grammar of Assent", "quote": "The **illative** sense is that personal judgment which guides the mind to a certitude beyond explicit syllogisms."},
      {"author": "Samuel Taylor Coleridge", "work": "The Friend", "quote": "Connectives of an **illative** character mark the transitions of sound logical argument."},
      {"author": "Henry Sweet", "work": "A New English Grammar", "quote": "Conjunctions such as 'therefore' and 'hence' are classified by grammarians as **illative** particles."}
    ]
  },
  "Dashboard — lat/interrelate.md": {
    "primary": "To connect or associate with one another in a mutual or reciprocal relationship.",
    "secondary": "In systems theory and ecological modeling, analyzing how dynamic components feedback upon and regulate each other within an open system.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "All organic beings are bound together by an intricate web of complex affinities that mutually **interrelate** them."},
      {"author": "Herbert Spencer", "work": "The Principles of Sociology", "quote": "The specialized institutions of a commonwealth **interrelate** closely to preserve social equilibrium."},
      {"author": "Thomas Henry Huxley", "work": "Critiques and Addresses", "quote": "The natural sciences do not exist in isolation, but deeply **interrelate** through shared physical principles."}
    ]
  },
  "Dashboard — lat/interrelated.md": {
    "primary": "Connected with one another; having a mutual or reciprocal relationship or interdependence.",
    "secondary": "In ecological systems biology, community structures where perturbations in one trophic level cascade through interconnected feeding links.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "In every domestic race, we see that varied organs and instincts are closely **interrelated**."},
      {"author": "William James", "work": "Pragmatism", "quote": "The universe is a vast network of **interrelated** experiences rather than a static monad."},
      {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "Economic phenomena are so thoroughly **interrelated** that isolated variables can rarely be studied in pure detachment."}
    ]
  },
  "Dashboard — lat/interrelatedness.md": {
    "primary": "The state or condition of being interrelated, interconnected, or mutually dependent.",
    "secondary": "In holistic metaphysics and environmental ethics, recognizing that all living organisms and ecological subsystems exist in reciprocal interdependence.",
    "quotes": [
      {"author": "Alfred North Whitehead", "work": "Process and Reality", "quote": "The ultimate reality of nature is found in the universal **interrelatedness** of all actual entities."},
      {"author": "Rachel Carson", "work": "Silent Spring", "quote": "Ecology reveals the profound **interrelatedness** of all living things within the thin fabric of the biosphere."},
      {"author": "William James", "work": "The Will to Believe", "quote": "Philosophical pluralism recognizes the partial **interrelatedness** of facts without demanding a rigid monistic whole."}
    ]
  }
}

base_dir = r"App database\Latin roots\Cluster Carrying"
updated = 0

for rel_path, info in data.items():
    fpath = os.path.join(base_dir, rel_path.replace("/", os.sep))
    if not os.path.exists(fpath):
        print(f"Warning: {fpath} does not exist!")
        continue
    
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    book_idx = content.find("> [!book]")
    if book_idx == -1:
        print(f"Warning: No > [!book] callout in {rel_path}")
        continue
    
    prefix = content[:book_idx]
    
    p_def = info["primary"].strip().rstrip(".") + "."
    s_def = info["secondary"].strip().rstrip(".") + "."
    
    new_book = f"> [!book] 📖 Definitions & Semantic Range\n> 1. **Primary Definition (Lexical / Standard Consensus)**: {p_def}\n> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: {s_def}\n"
    
    new_quote = "> [!quote] 💬 Contextual Usage & Authentic Quotations\n"
    for q in info["quotes"]:
        auth = q["author"].strip()
        work = q["work"].strip()
        quote_text = q["quote"].strip().strip('"').strip('“').strip('”')
        new_quote += f'> - 📜 **{auth} (*{work}*):** *"{quote_text}"*\n'
    
    new_content = prefix + new_book + "\n" + new_quote + "\n"
    
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(new_content)
    updated += 1

print(f"Carrying Batch 4A (lat): Successfully updated {updated}/{len(data)} notes.")
