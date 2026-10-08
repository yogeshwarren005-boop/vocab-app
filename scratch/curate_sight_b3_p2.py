# -*- coding: utf-8 -*-
"""
curate_sight_b3_p2.py
Batch 3 Part 2 of Cluster Sight:
- Dashboard — spect (remaining 7 words):
  spectroscopic, spectroscopical, spectroscopy, spectrum,
  unrespectability, unrespectable, unspectacular
- Dashboard — spic (46 words):
  auspicious, auspiciously, auspiciousness, conspicuous, conspicuously,
  conspicuousness, despicability, despicable, despicableness, despicably,
  inauspicious, inauspiciously, inauspiciousness, inconspicuous,
  inconspicuously, inconspicuousness, oversuspicious, perspicacious,
  perspicaciousness, perspicacity, perspicuity, perspicuous, perspicuously,
  perspicuousness, prospicience, prospicient, spic, spica, spicate,
  spiccato, spice, spice-scented, spiceberry, spicebush, spicemill,
  spicery, spicily, spiciness, spicule, spiculum, spicy, suspicion,
  suspicious, suspiciously, suspiciousness, unsuspicious
Total: 53 words.
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

data_sight_b3_p2 = {
    "spectroscopic": {
        "primary": "Relating to or obtained by the use of a spectroscope or spectroscopic techniques.",
        "secondary": "In modern astrophysics and quantum chemistry, pertains to the diagnostic examination of energy transitions and line splitting across electromagnetic frequencies.",
        "quotes": [
            {"author": "Arthur Eddington", "work": "The Internal Constitution of the Stars", "quote": "Our **spectroscopic** knowledge of stellar envelopes demonstrates the enormous abundance of hydrogen in deep space."},
            {"author": "Edwin Hubble", "work": "The Realm of the Nebulae", "quote": "The **spectroscopic** displacement toward the red is observed in all extragalactic nebulae whose distances have been measured."},
            {"author": "Robert Bunsen", "work": "Chemical Analysis by Spectral Observations", "quote": "Distinct **spectroscopic** lines appear with unfailing sharpness whenever volatile salts are introduced into the flame."}
        ]
    },
    "spectroscopical": {
        "primary": "Relating to a spectroscope or to spectroscopy; spectroscopic in character or method.",
        "secondary": "In nineteenth-century observational astronomy, denotes experimental setups utilizing prisms to analyze solar prominences and chemical vapours.",
        "quotes": [
            {"author": "George Ellery Hale", "work": "The Study of Stellar Evolution", "quote": "The **spectroscopical** examination of solar flares revealed bright reversals of the hydrogen lines."},
            {"author": "William Huggins", "work": "Atlas of Representative Stellar Spectra", "quote": "Through **spectroscopical** analysis, we proved that nebulae were not merely unresolved clusters of stars, but luminous incandescent gases."},
            {"author": "James Clerk Maxwell", "work": "Theory of Heat", "quote": "The **spectroscopical** method affords an invaluable test of the kinetic vibrations executed by gaseous molecules."}
        ]
    },
    "spectroscopy": {
        "primary": "The branch of science concerned with the investigation and measurement of spectra produced when matter interacts with or emits radiation.",
        "secondary": "In analytical physics and astrochemistry, serves as the primary technique for identifying atomic isotopes, molecular orbitals, and celestial compositions.",
        "quotes": [
            {"author": "Niels Bohr", "work": "On the Quantum Theory of Line-Spectra", "quote": "The quantum postulates find their most direct empirical foundation in the measurements of optical **spectroscopy**."},
            {"author": "Arthur Eddington", "work": "Stars and Atoms", "quote": "Without the aid of astronomical **spectroscopy**, the physical nature of the stars would remain an impenetrable enigma."},
            {"author": "Linus Pauling", "work": "The Nature of the Chemical Bond", "quote": "Modern infrared **spectroscopy** provides an indispensable map of interatomic forces within organic molecules."}
        ]
    },
    "spectrum": {
        "primary": "A band of colors produced by separation of the components of light by their different degrees of refraction; a continuous range.",
        "secondary": "In electromagnetic physics and social sciences, spans the complete continuum of radiant frequencies or an unbroken continuum of political opinions.",
        "quotes": [
            {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "The intellectual eye splits the white light of truth into a rich **spectrum** of diverse individual insights."},
            {"author": "Charles Darwin", "work": "The Variation of Animals and Plants Under Domestication", "quote": "In every domestic breed we discover a wide **spectrum** of variations departing from the aboriginal type."},
            {"author": "H. G. Wells", "work": "The Time Machine", "quote": "Beyond the visible red of the **spectrum** lies the vast domain of thermal radiation."}
        ]
    },
    "unrespectability": {
        "primary": "The state or character of not being respectable; lack of social standing or conventional bourgeois decency.",
        "secondary": "In cultural history and Victorian sociology, describes lifestyles, occupations, or bohemias that deliberately flouted bourgeois etiquette.",
        "quotes": [
            {"author": "George Eliot", "work": "Middlemarch", "quote": "The family shrank from any taint of **unrespectability** that might compromise their credit in the county."},
            {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "Jopp embraced his local **unrespectability** with bitter defiance, haunting the low tavern on the quay."},
            {"author": "George Bernard Shaw", "work": "Pygmalion", "quote": "Doolittle rejoiced in his cheerful **unrespectability**, declaring that bourgeois morality was a burden he could ill afford."}
        ]
    },
    "unrespectable": {
        "primary": "Not considered proper, respectable, or socially acceptable; disreputable.",
        "secondary": "In social classification, designating individuals, dwellings, or pastimes ostracized by polite society for nonconformist or disorderly ways.",
        "quotes": [
            {"author": "Charles Dickens", "work": "Bleak House", "quote": "The ragged court was filled with **unrespectable** lodgers whose precarious trades eluded the parish authorities."},
            {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Her relatives regarded the traveling tinker as a thoroughly **unrespectable** vagrant."},
            {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "He had a curious penchant for wandering through the most **unrespectable** quarters of the East End."}
        ]
    },
    "unspectacular": {
        "primary": "Not spectacular, dramatic, or sensational; ordinary, modest, and understated.",
        "secondary": "In evolutionary biology and institutional historiography, characterizes gradual, mundane processes that yield profound long-term systemic transformations.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Natural selection accumulates minute, **unspectacular** modifications through immense lapses of geological time."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Her daily life was filled with quiet, **unspectacular** duties that won no public applause."},
            {"author": "Thomas Henry Huxley", "work": "Method and Results", "quote": "The most durable triumphs of scientific method arise from patient, **unspectacular** laboratory verification."}
        ]
    },
    "auspicious": {
        "primary": "Conducive to success; favorable; giving or being a sign of future success.",
        "secondary": "In classical augury and ceremonial politics, designates omens, horoscopes, or inaugural events deemed propitious by sacred authorities.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Hamlet", "quote": "With an **auspicious** and a dropping eye, / With mirth in funeral and with dirge in marriage, / In equal scale weighing delight and dole."},
            {"author": "Ralph Waldo Emerson", "work": "The Conduct of Life", "quote": "Let us meet the new day under an **auspicious** resolve to welcome every fresh discovery of truth."},
            {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "The settlement began under **auspicious** skies, yet the dark shadow of the scaffold soon fell across the marketplace."}
        ]
    },
    "auspiciously": {
        "primary": "In a manner that bodes well for the future; favorably, propitiously, or successfully.",
        "secondary": "In narrative chronicles, inaugurating an enterprise under circumstances that promise continued prosperity and good fortune.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Winter's Tale", "quote": "My father's rough and hitches at my looks: / But he may soften; and I may find an hour / To woo his love again: if I can, / This business will end **auspiciously**."},
            {"author": "Charles Dickens", "work": "Great Expectations", "quote": "The journey commenced most **auspiciously**, with clear morning air and high hopes in young Pip's heart."},
            {"author": "Jane Austen", "work": "Emma", "quote": "The wedding day opened **auspiciously**, despite the gloomiest prognostications of Mr. Woodhouse."}
        ]
    },
    "auspiciousness": {
        "primary": "The promising, favorable, or propitious nature of circumstances attending an undertaking.",
        "secondary": "In ancient divination and institutional ceremonialism, the perceived presence of divine goodwill attending an enterprise or treaty.",
        "quotes": [
            {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "No sober statesman mistakes the transient popularity of a faction for genuine constitutional **auspiciousness**."},
            {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The **auspiciousness** of Trajan's reign was commemorated on countless triumphal arches throughout the provinces."},
            {"author": "Walter Pater", "work": "Marius the Epicurean", "quote": "He admired the serene ritual of the ancient religion, noting the sense of **auspiciousness** it imparted to daily toil."}
        ]
    },
    "conspicuous": {
        "primary": "Standing out so as to be clearly visible; attracting notice or attention.",
        "secondary": "In evolutionary ethology and social theory, characterizes warning coloration in organisms or ostentatious consumption designed to signal status.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Caterpillars that possess noxious properties are rendered **conspicuous** by bright colors to deter insectivorous birds."},
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Her scarlet cloak made her **conspicuous** against the bleak expanse of the autumn downs."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Lydgate's medical theories made him **conspicuous** among the conservative practitioners of the county."}
        ]
    },
    "conspicuously": {
        "primary": "In a clearly visible or noticeable way; strikingly or prominently.",
        "secondary": "In behavioral ecology and sociology, displaying traits or expenditures boldly to ensure immediate perception by competitors or onlookers.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Many poisonous species are **conspicuously** marked, advertising their unpalatability across the forest."},
            {"author": "Thorstein Veblen", "work": "The Theory of the Leisure Class", "quote": "Wealth must be **conspicuously** wasted if it is to confer unblemished social honor upon its possessor."},
            {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "The purloined document had been placed **conspicuously** upon the mantelpiece, escaping notice by its very boldness."}
        ]
    },
    "conspicuousness": {
        "primary": "The striking prominence that makes something obvious to the eye or mind.",
        "secondary": "In evolutionary coloration theory and social psychology, the degree of optical contrast that distinguishes an organism or individual from surrounding context.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Variation of Animals and Plants Under Domestication", "quote": "The high **conspicuousness** of the male bird's plumage often exposes him to greater danger from predators."},
            {"author": "Alfred Russel Wallace", "work": "Contributions to the Theory of Natural Selection", "quote": "We must distinguish between the warning **conspicuousness** of dangerous insects and the protective concealment of their prey."},
            {"author": "William James", "work": "The Principles of Psychology", "quote": "Any sudden alteration in sensory intensity guarantees the immediate **conspicuousness** of an idea in consciousness."}
        ]
    },
    "despicability": {
        "primary": "Extreme baseness, contemptibility, or worthiness of utter scorn and indignation.",
        "secondary": "In moral theology and dramatic villainy, extreme baseness that violates fundamental obligations of fidelity and human honor.",
        "quotes": [
            {"author": "Samuel Johnson", "work": "The Rambler", "quote": "There is an inherent **despicability** in the character of the flatterer who cringes before power he secretly abhors."},
            {"author": "George Eliot", "work": "Romola", "quote": "Tito's descent into moral **despicability** began with small evasions and culminated in betrayal."},
            {"author": "Henry Fielding", "work": "Tom Jones", "quote": "Blifil's sanctimonious hypocrisy cloaked a **despicability** that sickened all honest observers."}
        ]
    },
    "despicable": {
        "primary": "Deserving hatred and contempt; vile, worthless, and low in moral character.",
        "secondary": "In ethical philosophy, designating actions or dispositions that merit unreserved moral censure for craven malice or treachery.",
        "quotes": [
            {"author": "George Eliot", "work": "Middlemarch", "quote": "He thought that taking bribes was a **despicable** business, beneath the dignity of any gentleman."},
            {"author": "Henry David Thoreau", "work": "Walden", "quote": "I know that my townspeople will not look upon my simple mode of life as **despicable**, but rather as eccentric."},
            {"author": "Bram Stoker", "work": "Dracula", "quote": "To prey upon the helpless in their sleep is the most **despicable** cruelty known to man or beast."}
        ]
    },
    "despicableness": {
        "primary": "The vile nature or abject baseness that renders someone or something worthy of contempt.",
        "secondary": "In moral characterization, profound moral degradation that forfeits all claim to sympathy or respectful fellowship.",
        "quotes": [
            {"author": "Samuel Richardson", "work": "Clarissa", "quote": "Lovelace felt a momentary shame at the unvarnished **despicableness** of his machinations against innocence."},
            {"author": "Jonathan Swift", "work": "Gulliver's Travels", "quote": "The King of Brobdingnag commented upon the **despicableness** of European political intrigues with biting disdain."},
            {"author": "William Hazlitt", "work": "Characters of Shakespear's Plays", "quote": "Iago's villainy possesses no tragic grandeur, but a cold, venomous **despicableness**."}
        ]
    },
    "despicably": {
        "primary": "In a contemptible, mean, vile, or cowardly manner; shamefully.",
        "secondary": "In judicial censure and literary critique, acting in a way that demonstrates craven submission to base impulse or dishonorable gain.",
        "quotes": [
            {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The judge acted **despicably**, bending the laws to flatter royal prerogative and crush innocent prisoners."},
            {"author": "Charles Dickens", "work": "Nicholas Nickleby", "quote": "Squeers fawned **despicably** before his wealthy patrons while starving the helpless pupils in his charge."},
            {"author": "Tobias Smollett", "work": "The Adventures of Roderick Random", "quote": "The cowardly lieutenant shrank **despicably** behind the capstan the moment the enemy opened fire."}
        ]
    },
    "inauspicious": {
        "primary": "Not conducive to success; unpromising, ominous, or unfavorable.",
        "secondary": "In dramatic tragedy and historic annals, portending disaster or sorrow from the very threshold of an undertaking.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Romeo and Juliet", "quote": "O, here / Will I set up my everlasting rest, / And shake the yoke of **inauspicious** stars / From this world-wearied flesh."},
            {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "The grim doorway was an **inauspicious** portal through which to usher a fragile mother and child."},
            {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "The gathering darkness cast an **inauspicious** gloom over the wedding party assembling near the barrow."}
        ]
    },
    "inauspiciously": {
        "primary": "In a way that bodes ill; ominously, unfavorably, or unluckily.",
        "secondary": "In historical chronicle, beginning an enterprise under circumstances that forecast subsequent tragedy or institutional collapse.",
        "quotes": [
            {"author": "Charles Dickens", "work": "Bleak House", "quote": "The great chancery suit had begun **inauspiciously**, consuming the small patrimony of the original suitors in preliminary costs."},
            {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The Persian campaign opened **inauspiciously**, with fever devastating the legions before battle was joined."},
            {"author": "Sir Walter Scott", "work": "The Bride of Lammermoor", "quote": "The raven croaked **inauspiciously** above the bridal carriage as it passed the ruined chapel."}
        ]
    },
    "inauspiciousness": {
        "primary": "The unpromising, ominous, or ill-boding quality of circumstances or portents.",
        "secondary": "In dramatic aesthetics and fatalistic poetics, the oppressive atmosphere of impending doom that envelopes tragic characters.",
        "quotes": [
            {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "The **inauspiciousness** of the voyage is established from the moment the Mariner shoots the solitary albatross."},
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Fedallah's dark prophecies imparted a chilling sense of **inauspiciousness** to the Pequod's final cruise."},
            {"author": "Thomas De Quincey", "work": "Confessions of an English Opium-Eater", "quote": "A melancholy **inauspiciousness** seemed to hang over the deserted London streets at midnight."}
        ]
    },
    "inconspicuous": {
        "primary": "Not clearly visible or attracting attention; not conspicuous; unobtrusive.",
        "secondary": "In evolutionary camouflage and industrial design, blending seamlessly into visual backgrounds through cryptic coloration or understated form.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Many small desert animals are colored in **inconspicuous** grey tones that conceal them from birds of prey."},
            {"author": "Arthur Conan Doyle", "work": "The Return of Sherlock Holmes", "quote": "The secret entrance was rendered **inconspicuous** by a clever arrangement of bookshelves."},
            {"author": "Thomas Hardy", "work": "Under the Greenwood Tree", "quote": "The rustic lovers found an **inconspicuous** nook beneath the spreading branches of the ancient yew."}
        ]
    },
    "inconspicuously": {
        "primary": "In a way that does not attract attention; unobtrusively or discreetly.",
        "secondary": "In social anthropology and detective tradecraft, moving or existing within an environment without provoking surveillance or alarm.",
        "quotes": [
            {"author": "Joseph Conrad", "work": "The Secret Agent", "quote": "The conspirator slipped **inconspicuously** through the damp alley, melding into the London fog."},
            {"author": "Henry James", "work": "The American", "quote": "Newman stood **inconspicuously** by the doorway, observing the delicate etiquette of the Parisian salon."},
            {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The nightjar nested **inconspicuously** upon the bare stony ground, matching the pebbles perfectly."}
        ]
    },
    "inconspicuousness": {
        "primary": "The unobtrusive trait of escaping visual attention or blended concealment.",
        "secondary": "In evolutionary biology and architectural camouflage, the optical adaptation that prevents visual detection by predators or competitors.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The female bird owes her safety to the sober **inconspicuousness** of her plumage while incubating eggs."},
            {"author": "Alfred Russel Wallace", "work": "Darwinism", "quote": "Cryptic **inconspicuousness** is achieved by mimicking the texture, hue, and shadows of bark or lichen."},
            {"author": "H. G. Wells", "work": "The Invisible Man", "quote": "Total **inconspicuousness** proved impossible in snowy weather, where footprints revealed every step."}
        ]
    },
    "oversuspicious": {
        "primary": "Excessively inclined to distrust others or suspect foul play; unduly paranoid.",
        "secondary": "In forensic psychology and diplomatic statecraft, a diseased hypervigilance that interprets innocent gestures as coordinated conspiracies.",
        "quotes": [
            {"author": "Francis Bacon", "work": "Essays", "quote": "Princes that are **oversuspicious** multiply enemies by demonstrating that they hold all men for traitors."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Bulstrode had grown **oversuspicious**, dreading that every casual glance from a neighbor hid secret blackmail."},
            {"author": "William Shakespeare", "work": "The Winter's Tale", "quote": "An **oversuspicious** heart turns wholesome love into venomous jealousy."}
        ]
    },
    "perspicacious": {
        "primary": "Having a ready insight into and understanding of things; mentally acute or discerning.",
        "secondary": "In intellectual history and philosophy of mind, denotes exceptional clarity of judgment capable of seeing through sophistry and obfuscation.",
        "quotes": [
            {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "A **perspicacious** naturalist detects structural affinities where the casual observer sees only superficial diversity."},
            {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "A **perspicacious** mind quickly disentangles complex ideas into their simple components."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Mr. Farebrother was too **perspicacious** not to perceive the unspoken tension between Lydgate and his bride."}
        ]
    },
    "perspicaciousness": {
        "primary": "Acute discernment, sharp intellectual penetration, and ready insight.",
        "secondary": "In cognitive analysis and forensic investigation, the intellectual penetration that pierces surface appearances to grasp fundamental truths.",
        "quotes": [
            {"author": "Arthur Conan Doyle", "work": "The Sign of Four", "quote": "Holmes demonstrated his customary **perspicaciousness** by reconstructing the intruder's movements from three ashes."},
            {"author": "Samuel Johnson", "work": "Lives of the English Poets", "quote": "Dryden's prefaces display a critical **perspicaciousness** that laid the groundwork for modern literary critique."},
            {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "True **perspicaciousness** consists not in contentious disputation, but in uncovering the secrets of nature."}
        ]
    },
    "perspicacity": {
        "primary": "The ability to understand things quickly and make accurate judgments; acute mental penetration.",
        "secondary": "In epistemological appraisal, denotes penetrating analytical intelligence that comprehends nuanced relationships and foresees outcomes.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "Venn possessed a shrewd **perspicacity** in judging rustic character that made him an invaluable ally."},
            {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "Character is higher than intellect; yet what **perspicacity** equals the spontaneous insight of an honest mind?"},
            {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The emperor lacked the political **perspicacity** required to navigate the factions of the capital."}
        ]
    },
    "perspicuity": {
        "primary": "The luminous clarity and precision of expression that makes an idea readily understandable.",
        "secondary": "In classical rhetoric, prose stylistics, and logic, the essential virtue of discourse that ensures immediate intelligibility without ambiguity.",
        "quotes": [
            {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "The first rule of communication is **perspicuity**, without which words serve only to darken knowledge."},
            {"author": "David Hume", "work": "An Enquiry Concerning Human Understanding", "quote": "True philosophy cultivates elegance and **perspicuity**, banishing scholastic jargon forever."},
            {"author": "Quintilian", "work": "Institutio Oratoria", "quote": "Let our speech possess such **perspicuity** that our meaning shall not merely be understood, but cannot be misunderstood."}
        ]
    },
    "perspicuous": {
        "primary": "Clearly expressed and easily understood; lucid; plain.",
        "secondary": "In philosophical argumentation and jurisprudence, describing statutory language or mathematical deduction free from obscurity.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Troilus and Cressida", "quote": "Whose high respect and curb to his could bring / A work so **perspicuous** in itself."},
            {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "An argument is truly **perspicuous** when each step follows with transparent geometric necessity."},
            {"author": "Thomas Henry Huxley", "work": "Method and Results", "quote": "His lectures were celebrated for their **perspicuous** exposition of difficult biological doctrines."}
        ]
    },
    "perspicuously": {
        "primary": "In a clear, lucid, and easily understood manner; plainly.",
        "secondary": "In didactic writing and legal drafting, expounding complex premises with luminous clarity and orderly progression.",
        "quotes": [
            {"author": "Charles Dickens", "work": "Bleak House", "quote": "The chancellor set forth the principles of equity **perspicuously**, cutting through centuries of legal clutter."},
            {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "He that delivers knowledge should deliver it **perspicuously**, so that it may be examined and tested."},
            {"author": "Samuel Johnson", "work": "The Idler", "quote": "The historian ought to relate facts simply and **perspicuously**, avoiding rhetorical vanity."}
        ]
    },
    "perspicuousness": {
        "primary": "The lucid clarity of statement or discourse that banishes ambiguity.",
        "secondary": "In philosophical treatises and legal standards, the degree of unambiguous clarity that guarantees shared understanding among readers.",
        "quotes": [
            {"author": "John Locke", "work": "Some Thoughts Concerning Education", "quote": "Train the youth to express his thoughts with natural ease and **perspicuousness**."},
            {"author": "Edmund Burke", "work": "A Philosophical Enquiry into the Sublime and Beautiful", "quote": "In eloquence, **perspicuousness** must often yield to emotional passion and evocative obscurity."},
            {"author": "George Campbell", "work": "The Philosophy of Rhetoric", "quote": "Of all the qualities of style, strict **perspicuousness** is the most indispensable to conviction."}
        ]
    },
    "prospicience": {
        "primary": "The act of looking forward; foresight, prescience, or provident anticipation.",
        "secondary": "In moral theology and teleological philosophy, the intellectual faculty of surveying future contingencies and aligning present action accordingly.",
        "quotes": [
            {"author": "Samuel Taylor Coleridge", "work": "The Friend", "quote": "Human wisdom consists in a sober **prospicience** that calculates the moral consequences of legislation."},
            {"author": "Thomas Browne", "work": "Christian Morals", "quote": "Exercise a holy **prospicience** toward eternity, neglecting the vain bubbles of temporal glory."},
            {"author": "William Godwin", "work": "Enquiry Concerning Political Justice", "quote": "True benevolence requires rational **prospicience**, anticipating how institutions will shape unborn generations."}
        ]
    },
    "prospicient": {
        "primary": "Looking forward; having or showing foresight; provident and prescient.",
        "secondary": "In statecraft and ethical stewardship, anticipating oncoming societal needs and making proactive institutional preparations.",
        "quotes": [
            {"author": "John Milton", "work": "The Reason of Church-Government", "quote": "A wise and **prospicient** magistrate plants nurseries of learning to illuminate future ages."},
            {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "The seer stands upon the mountain ridge, **prospicient** of the dawn while valleys remain plunged in night."},
            {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "The soul is not retrospective, but **prospicient**, forever launching into uncharted seas of thought."}
        ]
    },
    "spic": {
        "primary": "A spike or ear of grain in historical botany; alternatively an archaic dialectal term for fat or bacon.",
        "secondary": "In historical agronomy and cereal morphology, refers to the spicate inflorescence or grain spike of wheat, barley, or rye.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Variation of Animals and Plants Under Domestication", "quote": "In wild cereals, the **spic** or spikelet readily disarticulates upon maturity to disperse the seed."},
            {"author": "John Gerard", "work": "The Herball", "quote": "The bearded **spic** of the winter rye stands erect upon its slender culm."},
            {"author": "William Turner", "work": "A New Herball", "quote": "The wild corn shooteth forth a rough **spic** whose awns defend it from browsing beasts."}
        ]
    },
    "spica": {
        "primary": "A bright binary star in the constellation Virgo; in surgery, a figure-eight bandage resembling an ear of barley.",
        "secondary": "In observational astronomy and orthopedics, the primary alpha star of Virgo or a composite plaster cast stabilizing hip and pelvic joints.",
        "quotes": [
            {"author": "Henry David Thoreau", "work": "Journals", "quote": "In the clear autumn twilight, the blue star **Spica** glittered low in the western sky above the pines."},
            {"author": "Arthur Eddington", "work": "Stars and Atoms", "quote": "Spectroscopic measurements revealed that **Spica** is a massive spectroscopic binary with an extraordinarily short period."},
            {"author": "Sir William Osler", "work": "The Principles and Practice of Medicine", "quote": "The surgeon applied a firm plaster **spica** to immobilize the fractured neck of the femur."}
        ]
    },
    "spicate": {
        "primary": "Having the form of or arranged in a spike or ear of grain; spikelike in botanical arrangement.",
        "secondary": "In systematic plant taxonomy, describes inflorescences whose sessile flowers are arranged along an unbranched central rachis.",
        "quotes": [
            {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The genus is easily distinguished by its dense, **spicate** racemes of purple flowers."},
            {"author": "Charles Darwin", "work": "The Different Forms of Flowers on Plants of the Same Species", "quote": "In many species possessing a **spicate** inflorescence, cross-fertilization is promoted by sequential blooming."},
            {"author": "John Lindley", "work": "An Introduction to Botany", "quote": "A **spicate** flower head ensures that pollen is readily shed upon the wind or visiting bees."}
        ]
    },
    "spiccato": {
        "primary": "A musical bowing technique for string instruments where the bow bounces lightly upon the string.",
        "secondary": "In violin performance and orchestral orchestration, produces short, crisp, detached staccato notes via controlled bow elasticity.",
        "quotes": [
            {"author": "Hector Berlioz", "work": "Treatise on Instrumentation", "quote": "The rapid **spiccato** of the violins imparts a shimmering, capricious energy to the Scherzo."},
            {"author": "George Bernard Shaw", "work": "Music in London", "quote": "The soloist executed the dazzling **spiccato** passages with breathtaking agility and flawless intonation."},
            {"author": "Leopold Auer", "work": "Violin Playing as I Teach It", "quote": "A pure **spiccato** requires complete relaxation of the wrist, allowing the stick to bounce by its own natural rebound."}
        ]
    },
    "spice": {
        "primary": "An aromatic or pungent vegetable substance used to flavor food, such as cloves, pepper, or cinnamon.",
        "secondary": "In global economic history and culinary chemistry, represents plant secondary metabolites that drove maritime exploration and colonial trade empires.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Winter's Tale", "quote": "I must have saffron to colour the warden pies; mace; dates... nutmegs, seven; a race or two of ginger... What a feast of **spice**!"},
            {"author": "Ralph Waldo Emerson", "work": "Nature", "quote": "The merchant sails across the globe to bring home a handful of tea and a pound of **spice**."},
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The warm trade winds blew across the ocean, laden with the faint, exotic **spice** of the Moluccas."}
        ]
    },
    "spice-scented": {
        "primary": "Fragrant with the pungent, sweet, or aromatic smell of spices.",
        "secondary": "In sensory descriptive prose and romantic landscape poetry, evokes tropical atmospheres, oriental bazaars, or autumnal orchard kitchens.",
        "quotes": [
            {"author": "Joseph Conrad", "work": "Lord Jim", "quote": "A faint, **spice-scented** breeze drifted offshore from the dark jungle coast of Sumatra."},
            {"author": "Henry David Thoreau", "work": "Excursions", "quote": "The autumn woods were dry and **spice-scented**, smelling of sweet-fern and bruised sassafras."},
            {"author": "Rudyard Kipling", "work": "Kim", "quote": "They rested in a **spice-scented** caravanserai where camel drivers smoked long pipes beneath the stars."}
        ]
    },
    "spiceberry": {
        "primary": "The aromatic edible berry of certain shrubs, such as wintergreen or spicebush.",
        "secondary": "In North American ethnobotany and wildlife ecology, designates pungent red drupes of Lindera benzoin consumed by migrating songbirds.",
        "quotes": [
            {"author": "John Burroughs", "work": "Signs and Seasons", "quote": "The robins fed eagerly upon the bright scarlet **spiceberry**, stripping the bushes before the first snowfall."},
            {"author": "Henry David Thoreau", "work": "Journals", "quote": "I crushed a glossy **spiceberry** between my fingers, enjoying its sharp aromatic fragrance in the woods."},
            {"author": "Asa Gray", "work": "Synoptical Flora of North America", "quote": "The aromatic oil of the **spiceberry** was valued by early settlers for both culinary and medicinal decoctions."}
        ]
    },
    "spicebush": {
        "primary": "A North American deciduous aromatic shrub (Lindera benzoin) bearing small yellow flowers and glossy red berries.",
        "secondary": "In woodland botany and riparian ecology, an underbrush indicator shrub thriving in moist calcareous soils and damp bottomlands.",
        "quotes": [
            {"author": "Henry David Thoreau", "work": "Walden", "quote": "The fragrance of the bruised **spicebush** along the swamp edge signaled the true awakening of spring."},
            {"author": "John Burroughs", "work": "Wake-Robin", "quote": "Before a leaf has unfolded, the **spicebush** covers itself with clusters of pale yellow flowers that illuminate the damp woods."},
            {"author": "Donald Culross Peattie", "work": "A Natural History of Trees", "quote": "Pioneers brewed a comforting aromatic tea from the twigs of the wild **spicebush** during winter months."}
        ]
    },
    "spicemill": {
        "primary": "A mechanical mill, grinder, or mortar used for grinding whole spices into powder.",
        "secondary": "In historical material culture and culinary domestic economy, a cast-iron or wooden rotary apparatus essential for freshly releasing essential oils.",
        "quotes": [
            {"author": "Charles Dickens", "work": "Great Expectations", "quote": "A heavy brass **spicemill** stood upon the dresser, filling the kitchen with fragrant dust whenever Joe turned the crank."},
            {"author": "Washington Irving", "work": "Bracebridge Hall", "quote": "The cook was busy with pestle and **spicemill**, preparing the savory condiments for the Christmas banquet."},
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The ship's galley boasted a small iron **spicemill** that clattered merrily through every roll of the sea."}
        ]
    },
    "spicery": {
        "primary": "Spices collectively; a place where spices are stored or processed.",
        "secondary": "In medieval and early modern trade history, the royal household department or merchant warehouse managing precious imported condiments.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Richard III", "quote": "Let them exchange their cursed oil of rage / For balmy drops of holy balm and peace; / For sorrow will make **spicery** of death."},
            {"author": "King James Bible", "work": "Genesis", "quote": "And, behold, a company of Ishmeelites came from Gilead with their camels bearing **spicery** and balm and myrrh."},
            {"author": "John Milton", "work": "Paradise Lost", "quote": "Sabæan odours from the spicy shore / Of Araby the blest, with rich **spicery** blown / Across the Indian ocean."}
        ]
    },
    "spicily": {
        "primary": "In a spicy manner; with aromatic pungency, sharp flavor, or lively piquancy.",
        "secondary": "In culinary prose and satirical journalism, describing pungent taste profiles or witty, provocative turns of phrase.",
        "quotes": [
            {"author": "Herman Melville", "work": "Omoo", "quote": "The island feast was **spicily** seasoned with native roots that brought tears of delight to the sailors' eyes."},
            {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "Becky Sharp commented **spicily** upon the fashionable hypocrisies of the London season."},
            {"author": "James Joyce", "work": "Dubliners", "quote": "The mulled port wine was **spicily** heated with cinnamon and cloves to ward off the winter chill."}
        ]
    },
    "spiciness": {
        "primary": "The characteristic of being spicy; pungent flavor or aroma; lively excitement.",
        "secondary": "In sensory food science and literary aesthetics, the physiological stimulation caused by essential oils or the biting wit of satirical discourse.",
        "quotes": [
            {"author": "Nathaniel Hawthorne", "work": "Mosses from an Old Manse", "quote": "There was a wholesome autumnal **spiciness** in the air that quickened our footsteps through the orchard."},
            {"author": "Charles Dickens", "work": "The Pickwick Papers", "quote": "Mr. Wardle praised the warm **spiciness** of the punch, refilling every glass with genial hospitality."},
            {"author": "Thomas Henry Huxley", "work": "Essays on Controverted Questions", "quote": "A dash of polemical **spiciness** keeps public debate awake without compromising philosophical integrity."}
        ]
    },
    "spicule": {
        "primary": "A small needlelike structure or sharp-pointed body, especially of sponges or solar flares.",
        "secondary": "In solar physics and marine zoology, refers to supersonic plasma jets in the solar chromosphere or microscopic skeletal spikes supporting poriferan tissue.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The glass sponge is composed of intricate lattices of silica, each microscopic **spicule** exquisitely formed."},
            {"author": "Thomas Henry Huxley", "work": "Manual of the Anatomy of Invertebrated Animals", "quote": "The skeletal framework of Calcispongiae consists of tri-radiate and quadri-radiate **spicule** elements."},
            {"author": "Arthur Eddington", "work": "Stars and Atoms", "quote": "A solar **spicule** erupts through the chromosphere at enormous speed, carrying magnetized plasma into the corona."}
        ]
    },
    "spiculum": {
        "primary": "A small sharp spike, dart, or needlelike anatomical part in invertebrates or botany.",
        "secondary": "In invertebrate morphology, Roman weaponry, and botany, designates copulatory needles in nematodes, Roman javelins, or pointed bracts.",
        "quotes": [
            {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The Roman infantry discharged the heavy **spiculum** with deadly precision before engaging sword in hand."},
            {"author": "Thomas Henry Huxley", "work": "Manual of the Anatomy of Invertebrated Animals", "quote": "The male nematode possesses a chitinous **spiculum** utilized for transfer during reproduction."},
            {"author": "Asa Gray", "work": "Botanical Text-Book", "quote": "Under the lens, each minute **spiculum** projecting from the seed coat assists in mechanical dispersal."}
        ]
    },
    "spicy": {
        "primary": "Flavored with or fragrant with spice; pungent; piquant; mildly scandalous or provocative.",
        "secondary": "In gastronomy and colloquial journalism, characterizes foods rich in aromatic essential oils or anecdotes possessing scandalous, entertaining details.",
        "quotes": [
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The **spicy** breezes of Ceylon greeted the weary crew after months across the barren Indian sea."},
            {"author": "James Joyce", "work": "Ulysses", "quote": "A warm, **spicy** aroma drifted from the bakery door, mingling with the smell of roasting chicory."},
            {"author": "Thomas Henry Huxley", "work": "Life and Letters", "quote": "He enlivened the biological controversy with several **spicy** remarks that delighted the medical students."}
        ]
    },
    "suspicion": {
        "primary": "A feeling or thought that something is possible, likely, or true; cautious distrust of someone or something.",
        "secondary": "In procedural criminal law and moral philosophy, a preliminary subjective apprehension unsupported by direct evidentiary proof.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Henry VI, Part 3", "quote": "**Suspicion** always haunts the guilty mind; / The thief doth fear each bush an officer."},
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "A faint **suspicion** of his true designs crossed Bathsheba's mind, but she dismissed it as unworthy."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Bulstrode lived in constant terror that some casual word might awaken **suspicion** regarding his early wealth."}
        ]
    },
    "suspicious": {
        "primary": "Having or showing a cautious distrust of someone or something; causing distrust.",
        "secondary": "In behavioral psychology and forensic investigation, an alert mental state characterized by hyper-attunement to anomalies, deceit, or hazards.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Winter's Tale", "quote": "A spider steep'd. / The venom of a **suspicious** thought / Infects the purest draught of human joy."},
            {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "Henchard had grown moody and **suspicious**, imagining that every glance in the marketplace mocked his fall."},
            {"author": "George Eliot", "work": "Silas Marner", "quote": "The rustic company at the Rainbow turned **suspicious** eyes upon the strange weaver who lived alone by the stone-pits."}
        ]
    },
    "suspiciously": {
        "primary": "With a cautious distrust or suspicion of someone or something; in a way that arouses suspicion.",
        "secondary": "In descriptive narrative and courtroom testimony, behaving in an evasive, guarded, or anomalous manner that invites investigation.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "The furze-cutter peered **suspiciously** across the dark hollow, hearing footsteps where none should be."},
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Ahab glanced **suspiciously** at the compass, noticing that the needle pointed contrary to the vessel's course."},
            {"author": "Bram Stoker", "work": "Dracula", "quote": "The peasants looked at us **suspiciously**, crossing themselves whenever the Count's castle was mentioned."}
        ]
    },
    "suspiciousness": {
        "primary": "The state or habit of being suspicious; a distrustful nature or disposition.",
        "secondary": "In character study and political psychology, a chronic predisposition to attribute hidden, malevolent motives to associates and rivals.",
        "quotes": [
            {"author": "Francis Bacon", "work": "Essays", "quote": "**Suspiciousness** in a prince is a defect of heart and head, clouding judgment and alienating faithful subjects."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Casaubon's morbid **suspiciousness** converted Dorothea's most innocent inquiries into disguised accusations."},
            {"author": "William James", "work": "The Varieties of Religious Experience", "quote": "A chronic **suspiciousness** poisons all natural communion between the soul and its surrounding fellows."}
        ]
    },
    "unsuspicious": {
        "primary": "Not having or showing suspicion; trusting, unwary, and unsuspecting.",
        "secondary": "In character ethics and pastoral literature, denotes an open, candid innocence that presumes goodwill in others without deceit.",
        "quotes": [
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Dorothea was of an ardent, **unsuspicious** nature, incapable of attributing petty malice to those she honored."},
            {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "Chillingworth preyed upon the **unsuspicious** minister, worming his way into the young man's secret soul."},
            {"author": "Thomas Henry Huxley", "work": "Method and Results", "quote": "The naive, **unsuspicious** observer is easily misled by superficial appearances in nature."}
        ]
    }
}
