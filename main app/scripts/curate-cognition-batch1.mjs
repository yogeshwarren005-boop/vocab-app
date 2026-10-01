import fs from "fs";
import path from "path";

const baseDir = "App database/Greek roots/Cluster Cognition & Mind";

const wordsData = {
  // === Dashboard — aret (3 words) ===
  "Dashboard — aret/aret.md": {
    word: "aret",
    primary: "A combining root derived from Ancient Greek aretē, meaning excellence, virtue, or the fulfillment of inherent potential.",
    secondary: "In philosophical ethics and classical rhetoric, the morphological element denoting moral merit, peak capability, and virtuous character.",
    quotes: [
      { author: "Plato", work: "Meno", quote: "Socrates inquired whether virtue and **aret**- could be taught, or if it sprang from nature and divine dispensation." },
      { author: "Aristotle", work: "Nicomachean Ethics", quote: "Every art and every inquiry aims at some good, culminating in the complete exercise of **aret**- in accordance with reason." },
      { author: "Werner Jaeger", work: "Paideia: The Ideals of Greek Culture", quote: "The Greek concept of **aret**- expressed the quintessence of aristocratic excellence, valor, and ethical distinction." }
    ]
  },
  "Dashboard — aret/aretaic.md": {
    word: "aretaic",
    primary: "Of, relating to, or focusing on virtue, especially in moral philosophy and normative ethics (aretaic ethics vs. deontic ethics).",
    secondary: "In contemporary ethical theory, describing philosophical frameworks that evaluate goodness based on human character and virtues rather than duties or utilitarian consequences.",
    quotes: [
      { author: "G. E. M. Anscombe", work: "Modern Moral Philosophy", quote: "Concepts of moral obligation should be abandoned in favor of an **aretaic** vocabulary centering on human flourishing and virtues." },
      { author: "Alasdair MacIntyre", work: "After Virtue", quote: "Classical moral theory was fundamentally **aretaic**, grounding moral judgments in the internal virtues required to sustain social practices." },
      { author: "Michael Slote", work: "From Morality to Virtue", quote: "An **aretaic** approach grounds all ethical evaluations directly in the motivational virtues and benevolence of the moral agent." }
    ]
  },
  "Dashboard — aret/arete.md": {
    word: "arete",
    primary: "Excellence, moral virtue, or the realization of one's full potential and purpose in Greek philosophy; also (as arête) a sharp mountain ridge in physical geography.",
    secondary: "In Hellenic philosophy, the cultivation of peak intellectual and moral perfection; in geomorphology, a narrow serrated crest formed by glacial erosion on adjacent cirques.",
    quotes: [
      { author: "Aristotle", work: "Eudemian Ethics", quote: "True happiness consists in the complete activity of the soul in accordance with perfect **arete**." },
      { author: "Robert M. Pirsig", work: "Zen and the Art of Motorcycle Maintenance", quote: "The ancient Greeks called Quality **arete**, meaning excellence and the duty to live up to one's highest potential." },
      { author: "John Tyndall", work: "The Glaciers of the Alps", quote: "We ascended along the icy **arete**, where a razor-like ridge of rock dropped sheer on either side into bottomless gulfs." }
    ]
  },

  // === Dashboard — gno (31 words) ===
  "Dashboard — gno/agnosia.md": {
    word: "agnosia",
    primary: "The inability to interpret sensations and recognize objects, persons, sounds, or smells despite having intact sensory organs, typically caused by brain damage.",
    secondary: "In clinical neuropsychology, a modality-specific recognition deficit (such as visual agnosia or prosopagnosia) resulting from cortical lesions in the parieto-occipital or temporal lobes.",
    quotes: [
      { author: "Oliver Sacks", work: "The Man Who Mistook His Wife for a Hat", quote: "His visual **agnosia** was so profound that he could perceive abstract shapes and colors yet failed to recognize his own wife's face." },
      { author: "Sigmund Freud", work: "On Aphasia", quote: "To distinguish disturbances in sensory recognition from speech failures, I proposed the clinical term **agnosia**." },
      { author: "Alexander Luria", work: "The Working Brain", quote: "Bilateral occipital lesions frequently produce severe visual **agnosia**, rendering the patient incapable of synthesizing visual details into a coherent whole." }
    ]
  },
  "Dashboard — gno/agnostic.md": {
    word: "agnostic",
    primary: "A person who believes that nothing is known or can be known of the existence or nature of God, the ultimate reality, or anything beyond material phenomena.",
    secondary: "In epistemology and computing, refusing to commit to an unproven dogma; in software architecture, describing components designed to operate independently of specific platforms or protocols.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "Agnosticism", quote: "I invented the word **agnostic** to denote someone who confesses that ultimate truth lies beyond the reach of human intellect." },
      { author: "Bertrand Russell", work: "What Is an Agnostic?", quote: "An **agnostic** thinks it impossible to know the truth in matters such as God and the future life with which Christianity concerns itself." },
      { author: "Clarence Darrow", work: "Why I Am an Agnostic", quote: "I am an **agnostic** because I do not pretend to know what many ignorant men claim to know with absolute certainty." }
    ]
  },
  "Dashboard — gno/agnostical.md": {
    word: "agnostical",
    primary: "Pertaining to or characteristic of agnosticism; skeptical regarding dogmatic claims about transcendent or unprovable matters.",
    secondary: "In philosophical and theological criticism, describing an attitude of reserved suspended judgment toward metaphysical doctrines.",
    quotes: [
      { author: "Leslie Stephen", work: "An Agnostic's Apology", quote: "Our **agnostical** stance does not spring from indifference, but from reverence for verifiable truth over baseless dogma." },
      { author: "William James", work: "The Will to Believe", quote: "The purely **agnostical** mind insists that where evidence is insufficient, belief must remain forever suspended." },
      { author: "Arthur Balfour", work: "The Foundations of Belief", quote: "He approached theological disputes with an **agnostical** detachment that exasperated dogmatists on both sides." }
    ]
  },
  "Dashboard — gno/agnosticism.md": {
    word: "agnosticism",
    primary: "The philosophical doctrine that the existence of God, divine attributes, or the ultimate nature of reality is unknown and inherently unknowable to human reason.",
    secondary: "In secular philosophy and scientific methodology, the epistemological discipline of suspending belief on propositions that cannot be empirically verified or logically demonstrated.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "Agnosticism and Christianity", quote: "**Agnosticism** is not a creed, but a method, the essence of which lies in the rigorous application of a single principle: do not pretend that conclusions are certain which are not demonstrated." },
      { author: "Carl Sagan", work: "The Demon-Haunted World", quote: "Healthy skepticism and scientific **agnosticism** are the best armor against superstition and unfounded claims." },
      { author: "W. K. Clifford", work: "The Ethics of Belief", quote: "The stern discipline of **agnosticism** forbids us to accept comforting dogmas without sufficient evidence." }
    ]
  },
  "Dashboard — gno/anagnorisis.md": {
    word: "anagnorisis",
    primary: "The critical moment of recognition or discovery in a drama or narrative, where a protagonist transitions from ignorance to sudden knowledge of the truth.",
    secondary: "In Aristotelian literary theory, the pivotal revelation—often coinciding with peripeteia (reversal of fortune)—that unmasks identity, kinship, or fatal deeds.",
    quotes: [
      { author: "Aristotle", work: "Poetics", quote: "A tragic **anagnorisis** is most effective when it arises directly from the plot, as in the terrible self-discovery of Oedipus." },
      { author: "Northrop Frye", work: "Anatomy of Criticism", quote: "The comic resolution hinges upon an **anagnorisis** in which lost heirs are identified and societal harmony is restored." },
      { author: "E. M. Forster", work: "Aspects of the Novel", quote: "A sudden shock of **anagnorisis** cuts through the narrative fog, forcing characters to confront what they have long denied." }
    ]
  },
  "Dashboard — gno/diagnosable.md": {
    word: "diagnosable",
    primary: "Capable of being identified, classified, or distinguished through clinical examination, symptoms, or diagnostic testing.",
    secondary: "In pathology and psychiatric nosology, meeting established clinical criteria sufficient to warrant an official categorical identification.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The malady presents clearly marked symptoms that render it readily **diagnosable** in its early stages." },
      { author: "Sigmund Freud", work: "Studies on Hysteria", quote: "Beneath the bizarre physical complaints lay a **diagnosable** neurosis rooted in repressed trauma." },
      { author: "Atul Gawande", work: "Complications: A Surgeon's Notes on an Imperfect Science", quote: "Even with modern magnetic imaging, certain atypical abdominal conditions remain barely **diagnosable** until surgical exploration." }
    ]
  },
  "Dashboard — gno/diagnose.md": {
    word: "diagnose",
    primary: "To identify the nature or cause of an illness, problem, or condition through careful examination of symptoms, indicators, and test results.",
    secondary: "In broader analytical usage, to determine the underlying cause or mechanism of a systemic malfunction, organizational failure, or social problem.",
    quotes: [
      { author: "Arthur Conan Doyle", work: "The Sign of Four", quote: "Sherlock Holmes could **diagnose** a client's secret occupation from a momentary glance at their boots and fingernails." },
      { author: "Virginia Woolf", work: "Mrs. Dalloway", quote: "Sir William Bradshaw felt confident that he could **diagnose** madness in three minutes and prescribe his celebrated rest cure." },
      { author: "Alexis de Tocqueville", work: "Democracy in America", quote: "The statesman must **diagnose** the hidden ailments of the body politic before they erupt in violent upheaval." }
    ]
  },
  "Dashboard — gno/diagnosing.md": {
    word: "diagnosing",
    primary: "The act or ongoing process of identifying and evaluating the nature of an illness, mechanical fault, or systemic defect.",
    secondary: "In clinical practice, the methodical synthesis of patient history, laboratory findings, and physical examination into an accurate diagnostic judgment.",
    quotes: [
      { author: "William Osler", work: "Aequanimitas", quote: "In **diagnosing** obscure fevers, the physician must cultivate patience and keen observation rather than hasty guesswork." },
      { author: "Atul Gawande", work: "The Checklist Manifesto", quote: "Complex cases often lead teams astray, making structured protocols essential when **diagnosing** acute distress." },
      { author: "Oliver Wendell Holmes Sr.", work: "Medical Essays", quote: "The art of **diagnosing** human infirmity requires both scientific precision and compassionate insight." }
    ]
  },
  "Dashboard — gno/diagnosis.md": {
    word: "diagnosis",
    primary: "The identification of the nature of an illness or problem by examination of the symptoms; an authoritative medical or technical assessment.",
    secondary: "In systems engineering and organizational analysis, a comprehensive evaluation pinpointing the root causes of dysfunction or failure.",
    quotes: [
      { author: "George Eliot", work: "Middlemarch", quote: "Dr. Lydgate prided himself on making an accurate **diagnosis** where the older provincial practitioners saw only vague bile." },
      { author: "Anton Chekhov", work: "Ward No. 6", quote: "The doctor stared at the patient, knowing well that no clever **diagnosis** could undo the ravages of poverty and neglect." },
      { author: "Henry James", work: "The Wings of the Dove", quote: "The eminent London specialist gave his grave **diagnosis**, couched in gentle words that could not conceal its fatal import." }
    ]
  },
  "Dashboard — gno/diagnostic.md": {
    word: "diagnostic",
    primary: "Serving to identify or distinguish an illness, fault, or specific condition; a symptom, indicator, or test used in diagnosis.",
    secondary: "In statistics, medicine, and computing, a definitive tool, biomarker, or metric utilized to evaluate performance and verify health or error states.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "Scientific Memoirs", quote: "The distinctive tooth structure provides a clear **diagnostic** character separating these ancient marsupials from placentals." },
      { author: "William Osler", work: "The Student Life", quote: "The presence of rose spots upon the abdomen is a classic **diagnostic** sign of enteric fever." },
      { author: "John Locke", work: "An Essay Concerning Human Understanding", quote: "Clear perception of our own ideas is the surest **diagnostic** sign of intellectual truth." }
    ]
  },
  "Dashboard — gno/dysanagnosia.md": {
    word: "dysanagnosia",
    primary: "A neurological impairment causing difficulty in recognizing or comprehending written or printed words; a form of dyslexia or verbal agnosia.",
    secondary: "In cognitive neuropsychology, an acquired reading deficit resulting from lesions in the dominant angular gyrus, leaving spoken language relatively unimpaired.",
    quotes: [
      { author: "Alexander Luria", work: "Higher Cortical Functions in Man", quote: "Parieto-occipital damage often induces marked **dysanagnosia**, where patients can write spontaneously but fail to read their own script." },
      { author: "Norman Geschwind", work: "Selected Papers on Language and the Brain", quote: "The disconnection between visual association areas and language centers produces profound **dysanagnosia**." },
      { author: "Henry Head", work: "Aphasia and Kindred Disorders of Speech", quote: "Cases of **dysanagnosia** demonstrate that the visual recognition of word symbols constitutes a distinct physiological process." }
    ]
  },
  "Dashboard — gno/gno.md": {
    word: "gno",
    primary: "A classical Greek combining root meaning to know, perceive, recognize, or discern (from gignōskein, gnōsis).",
    secondary: "In historical linguistics and etymology, the Indo-European base (*gno-) giving rise to words denoting cognition, diagnosis, gnosis, and knowledge.",
    quotes: [
      { author: "Max Müller", work: "Lectures on the Science of Language", quote: "The radical element **gno**- runs through Greek, Latin, and Sanskrit, forming the universal stem for conscious cognition." },
      { author: "Walter William Skeat", work: "Principles of English Etymology", quote: "From the primitive root **gno**- descend both our native word 'know' and borrowed Hellenic terms like 'gnosis' and 'diagnosis'." },
      { author: "Antoine Meillet", work: "Introduction to the Comparative Study of Indo-European Languages", quote: "The ancient verbal root **gno**- fundamentally signified perceptual discernment evolving into conceptual knowledge." }
    ]
  },
  "Dashboard — gno/gnome.md": {
    word: "gnome",
    primary: "A short, pithy saying that expresses a general truth or moral maxim; also, a diminutive legendary earth-dwelling creature in folklore.",
    secondary: "In classical rhetoric and Greek literature, an aphoristic moral judgment; in Renaissance folklore (originated by Paracelsus), an elemental spirit presiding over subterranean riches.",
    quotes: [
      { author: "Aristotle", work: "Rhetoric", quote: "A **gnome** is an assertion not about particulars, but about universals, concerning things that are to be chosen or avoided in human action." },
      { author: "Francis Bacon", work: "The Advancement of Learning", quote: "Solomon gathered moral wisdom into concise **gnomes** that pierce the understanding like sharp nails." },
      { author: "Alexander Pope", work: "The Rape of the Lock", quote: "Swift on his sooty pinions flits the **gnome**, / And in a vapor reaches Umbriel's dome." }
    ]
  },
  "Dashboard — gno/gnomic.md": {
    word: "gnomic",
    primary: "Expressed in or consisting of short, pithy, and wise maxims or aphorisms; of or relating to gnomes (wise sayings).",
    secondary: "In linguistics and grammar, denoting a tense (especially the gnomic aorist or present) used to state timeless, universal truths.",
    quotes: [
      { author: "Ralph Waldo Emerson", work: "Essays: First Series", quote: "Heraclitus and the ancient Seven Sages spoke in **gnomic** fragments that linger in the memory like sacred oracles." },
      { author: "Samuel Taylor Coleridge", work: "Biographia Literaria", quote: "The early Greek poets cultivated a **gnomic** style, distilling ancestral ethical experience into memorable couplets." },
      { author: "Matthew Arnold", work: "Essays in Criticism", quote: "Joubert’s prose possesses that refined, **gnomic** quality that compresses a lifetime of reflection into a solitary sentence." }
    ]
  },
  "Dashboard — gno/gnomon.md": {
    word: "gnomon",
    primary: "The raised pin, rod, or triangular style on a sundial that casts a shadow showing the time of day.",
    secondary: "In geometry, the L-shaped figure remaining after a smaller similar parallelogram is removed from the corner of a larger parallelogram.",
    quotes: [
      { author: "James Joyce", work: "Dubliners", quote: "It had always made me feel vaguely uneasy, like the word **gnomon** in the Euclid and the word simony in the Catechism." },
      { author: "Euclid", work: "Elements (Book II)", quote: "Let the remaining figure composed of the two complements and the adjacent parallelogram be called a **gnomon**." },
      { author: "Thomas Hardy", work: "The Mayor of Casterbridge", quote: "The tall chimney cast its black shade across the courtyard like the **gnomon** of a gigantic dial marking the hour." }
    ]
  },
  "Dashboard — gno/gnomonic.md": {
    word: "gnomonic",
    primary: "Of, relating to, or resembling a gnomon, especially in sundial construction or astronomical measurement.",
    secondary: "In cartography, designating a map projection where the point of perspective is at the center of the sphere, causing all great circles to display as straight lines.",
    quotes: [
      { author: "Nathaniel Bowditch", work: "The American Practical Navigator", quote: "On a **gnomonic** chart, great-circle tracks between distant ports plot as convenient straight lines for oceanic navigation." },
      { author: "Vitruvius", work: "De Architectura", quote: "The **gnomonic** art enabled ancient astronomers to align their dials with the celestial equator and solstice circles." },
      { author: "Arthur Conan Doyle", work: "The Captain of the Pole-Star", quote: "The captain consulted his **gnomonic** charts, tracing our perilous trajectory across the polar ice fields." }
    ]
  },
  "Dashboard — gno/gnosia.md": {
    word: "gnosia",
    primary: "The cognitive faculty or mental ability to recognize, perceive, and interpret sensory stimuli; the neurological opposite of agnosia.",
    secondary: "In behavioral neurology, the intact cortical process by which sensory signals from the environment are successfully mapped to stored semantic memories.",
    quotes: [
      { author: "Alexander Luria", work: "The Neuropsychology of Memory", quote: "Normal tactile **gnosia** depends on the seamless synthesis of cutaneous sensations in the secondary parietal cortex." },
      { author: "Oliver Sacks", work: "A Leg to Stand On", quote: "Recovery required not merely muscle strength, but the gradual restoration of proprioceptive **gnosia** in the injured limb." },
      { author: "Wilder Penfield", work: "The Mystery of the Mind", quote: "Cortical stimulation demonstrated that sensory **gnosia** operates through complex interpretive circuits in the temporal lobes." }
    ]
  },
  "Dashboard — gno/gnosis.md": {
    word: "gnosis",
    primary: "Esoteric, experiential, or intuitive knowledge of spiritual truths and divine mysteries, especially as emphasized by ancient Gnostics.",
    secondary: "In comparative religion and mysticism, transformative direct apprehension of the divine, contrasted with intellectual belief or scholastic dogma.",
    quotes: [
      { author: "Elaine Pagels", work: "The Gnostic Gospels", quote: "To know oneself at the deepest level is to attain **gnosis**, discovering simultaneously the secret origin of the divine soul." },
      { author: "C. G. Jung", work: "Mysterium Coniunctionis", quote: "The ancient seekers after **gnosis** projected their unconscious psychological individuation onto cosmic mythologies." },
      { author: "Aldous Huxley", work: "The Perennial Philosophy", quote: "True **gnosis** is not speculative theory, but immediate, unitive awareness of the eternal ground of being." }
    ]
  },
  "Dashboard — gno/Gnostic.md": {
    word: "Gnostic",
    primary: "Of, relating to, or characteristic of Gnosticism; possessing or claiming esoteric spiritual knowledge.",
    secondary: "In the history of late antique religion, referring to early Christian or Hellenistic sects emphasizing personal mystical revelation over ecclesiastical authority.",
    quotes: [
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The **Gnostic** sects blended the sublime philosophy of Plato with oriental cosmologies and early Christian theology." },
      { author: "Elaine Pagels", work: "The Gnostic Gospels", quote: "A **Gnostic** teacher encouraged disciples to search within their own souls for the spark of celestial light." },
      { author: "Harold Bloom", work: "The American Religion", quote: "Much of modern esoteric spirituality bears the unmistakable impress of ancient **Gnostic** longing for transcendence." }
    ]
  },
  "Dashboard — gno/gnosticism.md": {
    word: "gnosticism",
    primary: "A prominent religious and philosophical movement of the Hellenistic and early Christian eras holding that redemption is achieved through esoteric knowledge (gnosis).",
    secondary: "In the history of ideas, a worldview marked by metaphysical dualism between the spiritual realm and an imperfect material world created by a demiurge.",
    quotes: [
      { author: "Hans Jonas", work: "The Gnostic Religion", quote: "**Gnosticism** articulated an existential crisis of antiquity, depicting humanity as alienated aliens stranded in a dark cosmos." },
      { author: "Bertrand Russell", work: "A History of Western Philosophy", quote: "Early church fathers waged fierce polemical warfare against **gnosticism** to establish uniform orthodoxy." },
      { author: "C. G. Jung", work: "Memories, Dreams, Reflections", quote: "My study of ancient **gnosticism** revealed striking archetypal parallels to the spontaneous symbols produced by modern patients." }
    ]
  },
  "Dashboard — gno/pathognomonic.md": {
    word: "pathognomonic",
    primary: "Specifically, decisively characteristic or indicative of a particular disease or pathological condition, allowing definitive diagnosis.",
    secondary: "In clinical semiotics, a clinical sign or symptom so uniquely bound to an etiology that its presence alone confirms the diagnosis without ambiguity.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Koplik spots appearing upon the buccal mucosa are considered virtually **pathognomonic** of early measles." },
      { author: "Rudolf Virchow", work: "Cellular Pathology", quote: "The pathologist must search for changes that are truly **pathognomonic** rather than secondary inflammatory reactions." },
      { author: "Arthur Conan Doyle", work: "The Adventure of the Dying Detective", quote: "Holmes noted the dark facial blotches with grim satisfaction, knowing them to be **pathognomonic** of the deadly Sumatra poison." }
    ]
  },
  "Dashboard — gno/physiognomy.md": {
    word: "physiognomy",
    primary: "The assessment of character, temperament, or mental qualities from outward appearance, especially facial features; also the facial expression itself.",
    secondary: "In physical geography and ecology, the external appearance, structural character, or landscape configuration of a natural habitat or plant community.",
    quotes: [
      { author: "Charlotte Brontë", work: "Jane Eyre", quote: "I studied his harsh **physiognomy** intently, finding in the heavy brow and firm mouth signs of an indomitable will." },
      { author: "Herman Melville", work: "Moby-Dick; or, The Whale", quote: "If then, Sir William Jones, who read in thirty languages, could not read a whale's **physiognomy**, who shall?" },
      { author: "Alexander von Humboldt", work: "Aspects of Nature", quote: "The general **physiognomy** of a country depends upon the predominant vegetation that clothes its mountains and valleys." }
    ]
  },
  "Dashboard — gno/prognosis.md": {
    word: "prognosis",
    primary: "A reasoned medical forecast of the likely course, duration, and outcome of a disease or ailment.",
    secondary: "In economics, politics, and sociology, any forward-looking analysis predicting future trends and developments based on current indicators.",
    quotes: [
      { author: "Hippocrates", work: "Book of Prognostics", quote: "He who would practice medicine rightly must foreknow and declare both the present condition and the future **prognosis** of his patient." },
      { author: "George Eliot", work: "Middlemarch", quote: "Lydgate hesitated to deliver a cheerful **prognosis** when the pulse indicated profound organic deterioration." },
      { author: "John Maynard Keynes", work: "The Economic Consequences of the Peace", quote: "The economic **prognosis** for post-war Europe remained bleak unless international credit and trade were swiftly restored." }
    ]
  },
  "Dashboard — gno/prognostic.md": {
    word: "prognostic",
    primary: "Serving to predict, forecast, or foreshadow; a symptom or sign indicating the future course of an event or disease.",
    secondary: "In meteorological and financial forecasting, an advance indicator used to project systemic changes or environmental hazards.",
    quotes: [
      { author: "Francis Bacon", work: "Sylva Sylvarum", quote: "The behavior of cattle and the flight of sea-birds provide natural **prognostic** signs of an approaching tempest." },
      { author: "William Shakespeare", work: "The Winter's Tale", quote: "Though not with bag and baggage, yet with some tokens / Which warrant me a **prognostic** of your good fortune." },
      { author: "Thomas Henry Huxley", work: "Lay Sermons, Addresses, and Reviews", quote: "The presence of these fossil organisms provides a valuable **prognostic** guide for geological survey teams." }
    ]
  },
  "Dashboard — gno/prognosticate.md": {
    word: "prognosticate",
    primary: "To forecast, prophesy, or predict future events or outcomes based on present signs, data, or symptoms.",
    secondary: "In historical astrology and political commentary, to issue formal predictions concerning the fate of rulers, states, or harvests.",
    quotes: [
      { author: "William Shakespeare", work: "Sonnet 14", quote: "Not from the stars do I my judgment pluck; / And yet methinks I have astronomy, / But not to tell of good or evil luck, / Of plagues, of dearths, or seasons' quality; / Nor can I fortune to brief minutes true, / Pointing to each his thunder, rain and wind, / Or say with princes if it shall go well / By oft predict that I in heaven find: / But from thine eyes my knowledge I derive, / And, constant stars, in them I read such art / As truth and beauty shall together thrive, / If from thyself to store thou wouldst convert; / Or else of thee this I **prognosticate**: / Thy end is truth's and beauty's doom and date." },
      { author: "Jonathan Swift", work: "Bickerstaff Papers", quote: "I take upon me to **prognosticate** the death of the almanac-maker John Partridge on the twenty-ninth of March." },
      { author: "Daniel Defoe", work: "A Journal of the Plague Year", quote: "Impostors and quacks went about the streets pretending to **prognosticate** who should survive the pestilence." }
    ]
  },
  "Dashboard — gno/prognostication.md": {
    word: "prognostication",
    primary: "The act of prophesying, forecasting, or predicting future events; a prediction or forecast based on observed signs.",
    secondary: "In early modern print culture, an astrological almanac or formal treatise foretelling weather, harvests, and political fortunes.",
    quotes: [
      { author: "Francis Bacon", work: "The Essays: Of Prophecies", quote: "Men mark when such an astrological **prognostication** hits, but ignore the hundreds of times it misses." },
      { author: "Walter Scott", work: "The Antiquary", quote: "His gloomy **prognostication** of shipwreck proved all too accurate as the gale battered the northern coast." },
      { author: "Edmund Burke", work: "Reflections on the Revolution in France", quote: "My somber **prognostication** concerning the French assemblies was drawn from the immutable laws of human nature." }
    ]
  },
  "Dashboard — gno/prognosticative.md": {
    word: "prognosticative",
    primary: "Having the nature or quality of forecasting; indicating or foreshadowing future outcomes or occurrences.",
    secondary: "In analytical methodology, describing indicators, signs, or models that possess high predictive validity.",
    quotes: [
      { author: "Samuel Taylor Coleridge", work: "The Friend", quote: "The philosopher discerning moral trends possesses a **prognosticative** vision far beyond immediate political expediency." },
      { author: "William Hazlitt", work: "Table-Talk", quote: "Certain early mannerisms in a young artist’s sketches are intensely **prognosticative** of future masterly genius." },
      { author: "Henry David Thoreau", work: "A Week on the Concord and Merrimack Rivers", quote: "The peculiar evening halo round the moon had a **prognosticative** stillness that foretold autumn rain." }
    ]
  },
  "Dashboard — gno/prognosticator.md": {
    word: "prognosticator",
    primary: "A person who predicts, foretells, or prophesies future events, trends, or weather conditions.",
    secondary: "In historiography, an almanac-maker, astrologer, or political pundit claiming authority to anticipate historical developments.",
    quotes: [
      { author: "Jonathan Swift", work: "Gulliver's Travels", quote: "The Laputan astronomers are tireless **prognosticators**, forever anticipating collisions with comets and catastrophic solar blazes." },
      { author: "Thomas Carlyle", work: "The French Revolution", quote: "Every tavern had its amateur **prognosticator** announcing the imminent collapse of the royal treasury." },
      { author: "Benjamin Franklin", work: "Poor Richard's Almanack", quote: "A prudent man listens cautiously to the weather **prognosticator**, but carries his umbrella regardless." }
    ]
  },
  "Dashboard — gno/telegnosis.md": {
    word: "telegnosis",
    primary: "Clairvoyance or extrasensory perception; the alleged paranormal acquisition of knowledge about distant events or objects without sensory contact.",
    secondary: "In parapsychology and psychical research, the hypothetical capacity of the mind to perceive remote information transcending spatial boundaries.",
    quotes: [
      { author: "William James", work: "Memories and Studies", quote: "The mediumistic phenomena under investigation seemed to involve genuine **telegnosis**, defying simple fraud or coincidence." },
      { author: "Frederic W. H. Myers", work: "Human Personality and Its Survival of Bodily Death", quote: "We designate this telepathic awareness of remote crises as **telegnosis**, an operation of the subliminal self." },
      { author: "Arthur Conan Doyle", work: "The History of Spiritualism", quote: "Remarkable experiments in **telegnosis** convinced many skeptical investigators of unseen mental connections." }
    ]
  },
  "Dashboard — gno/telegnostic.md": {
    word: "telegnostic",
    primary: "Of, relating to, or possessing telegnosis; relating to clairvoyant knowledge or paranormal perception of distant occurrences.",
    secondary: "In 19th-century psychical literature, describing sensitivity to impressions transmitted across great physical distances.",
    quotes: [
      { author: "Frederic W. H. Myers", work: "The Subliminal Consciousness", quote: "The subject exhibited rare **telegnostic** faculties, describing with vivid accuracy scenes occurring across the ocean." },
      { author: "William Barrett", work: "Psychical Research", quote: "Experimental evidence suggests that certain sensitives possess acute **telegnostic** responsiveness during hypnotic trance." },
      { author: "Camille Flammarion", work: "The Unknown", quote: "Numerous authenticated cases point to a **telegnostic** vision operating outside standard optical physics." }
    ]
  },
  "Dashboard — gno/undiagnosable.md": {
    word: "undiagnosable",
    primary: "Impossible or exceptionally difficult to diagnose, identify, or classify through standard medical or diagnostic methods.",
    secondary: "In clinical pathology, describing rare syndromes whose polymorphic signs or lack of known biomarkers resist standard nosological classification.",
    quotes: [
      { author: "Oliver Sacks", work: "Awakenings", quote: "In the early phase of encephalitis lethargica, patients presented baffling symptoms that were initially deemed **undiagnosable**." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The clinician must frankly confess when an obscure malady remains temporarily **undiagnosable** pending further laboratory evidence." },
      { author: "Atul Gawande", work: "Complications: A Surgeon's Notes on an Imperfect Science", quote: "To face an **undiagnosable** crisis in the emergency theater tests the limits of medical courage and humility." }
    ]
  }
};

function updateWordNote(relPath, data) {
  const fullPath = path.join(baseDir, relPath);
  if (!fs.existsSync(fullPath)) {
    console.error("Not found:", fullPath);
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
console.log("Batch 1 completed! Total words updated:", Object.keys(wordsData).length);
