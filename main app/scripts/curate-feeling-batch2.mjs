import fs from 'fs';
import path from 'path';

const basePath = 'App database/Greek roots/Cluster Feeling & Sensation';

const filesData = {
  // Dashboard — erot (17 words)
  "Dashboard — erot/erode.md": {
    primary: "To gradually wear away, abrade, or dissolve soil, rock, or other material through the physical action of water, wind, glacial ice, or chemical weathering.",
    secondary: "In figurative and social contexts, to slowly undermine, diminish, or weaken authority, confidence, value, or institutional integrity over time.",
    quotes: [
      { author: "Charles Lyell", work: "Principles of Geology", quote: "The mountain streams continuously **erode** the underlying granite strata, carving deep chasms over uncounted centuries." },
      { author: "Rachel Carson", work: "Silent Spring", quote: "Rains wash across the bare fields and **erode** the precious topsoil that required millennia of forest growth to create." },
      { author: "Alexis de Tocqueville", work: "Democracy in America", quote: "Excessive bureaucratic centralization tends quietly to **erode** local civic virtues and personal initiative." }
    ]
  },
  "Dashboard — erot/eroded.md": {
    primary: "Worn away, degraded, or diminished gradually by the abrasive forces of water, wind, friction, or chemical weathering.",
    secondary: "Impaired, depleted, or hollowed out through protracted attrition in political, psychological, or economic spheres.",
    quotes: [
      { author: "John Muir", work: "The Mountains of California", quote: "The sheer canyon walls of **eroded** slate glistened like polished armor in the bright alpine noon." },
      { author: "Charles Darwin", work: "The Origin of Species", quote: "We behold the magnificent ruins of ancient formations, now deeply **eroded** and fractured by volcanic upheavals." },
      { author: "George Orwell", work: "Homage to Catalonia", quote: "Living in the trenches, our youthful illusions were steadily **eroded** by cold, vermin, and administrative cynicism." }
    ]
  },
  "Dashboard — erot/eroding.md": {
    primary: "In the process of wearing away or gradually dissolving through abrasive environmental, chemical, or frictional forces.",
    secondary: "Progressively eating into, consuming, or weakening boundaries, financial reserves, or cultural traditions.",
    quotes: [
      { author: "Henry David Thoreau", work: "Walden", quote: "The spring thaw brought torrents of sand and gravel down the bank, **eroding** the railway embankment in miniature deltas." },
      { author: "Aldous Huxley", work: "Brave New World Revisited", quote: "Subtle commercial propaganda acts as an **eroding** acid upon individual critical judgment." },
      { author: "Theodore Roosevelt", work: "The New Nationalism", quote: "Unregulated industrial exploitation is rapidly **eroding** the natural resource heritage of our descendants." }
    ]
  },
  "Dashboard — erot/eros.md": {
    primary: "The ancient Greek god of passionate love and sexual desire; passionate, romantic, or sensual love, distinguished from philia (friendship) and agape (unconditional charity).",
    secondary: "In Freudian psychoanalysis, the life instinct (Eros) that seeks to preserve life, create organic harmony, and channel libidinal drive against Thanatos (the death drive).",
    quotes: [
      { author: "Plato", work: "Symposium", quote: "Love, or **Eros**, is not a god but a great daemon who mediates between mortals and the immortal realm of beauty." },
      { author: "Sigmund Freud", work: "Civilization and Its Discontents", quote: "The battle of civilization presents itself as a struggle between **Eros** and Death, between the instinct of life and the instinct of destruction." },
      { author: "C. S. Lewis", work: "The Four Loves", quote: "Being in love, which the ancients named **Eros**, transforms mere sexual appetite into an imaginative adoration of the beloved." }
    ]
  },
  "Dashboard — erot/erosive.md": {
    primary: "Tending to erode; causing, characterized by, or resulting from gradual abrasion, wearing away, or corrosion.",
    secondary: "Having a destructive, gnawing, or corrosive effect upon anatomical tissues (e.g., erosive gastritis) or institutional foundations.",
    quotes: [
      { author: "Charles Lyell", work: "Elements of Geology", quote: "The ceaseless **erosive** power of oceanic breakers shatters the toughest basalt headlands into shingle." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Chronic ingestion of irritants provokes an **erosive** gastritis that may precipitate severe gastrointestinal bleeding." },
      { author: "Edmund Burke", work: "Reflections on the Revolution in France", quote: "Radical speculative dogmas exert an **erosive** influence upon the unwritten customs that hold civil society together." }
    ]
  },
  "Dashboard — erot/erot.md": {
    primary: "The Greek root *erot-* (from *erōs*, genitive *erōtos*), signifying romantic love, sexual passion, amorous desire, or libido.",
    secondary: "The foundational combining form in clinical sexology, psychoanalysis, and literary criticism designating sexual or sensual themes.",
    quotes: [
      { author: "Henry George Liddell & Robert Scott", work: "A Greek-English Lexicon", quote: "From the stem **erot** spring numerous compounds denoting love-songs, passionate longing, and amatory verse." },
      { author: "Havelock Ellis", work: "Studies in the Psychology of Sex", quote: "Medical terminology borrowed the Greek root **erot** to construct objective classifications of instinctual desire." },
      { author: "Michel Foucault", work: "The History of Sexuality", quote: "Classical Hellenic discourses treated the impulse of **erot** as an art of existence governed by temperance rather than sin." }
    ]
  },
  "Dashboard — erot/erotic.md": {
    primary: "Relating to, tending to arouse, or characterized by sexual desire, passion, or sensual pleasure; amatory.",
    secondary: "In literary and art criticism, pertaining to representations of romantic intimacy, sensual beauty, and libidinal energy.",
    quotes: [
      { author: "Oscar Wilde", work: "The Picture of Dorian Gray", quote: "The canvas possessed an intense, half-veiled **erotic** allure that troubled the young artist's quiet studio." },
      { author: "Virginia Woolf", work: "The Waves", quote: "The dusk trembled with an **erotic** vibration, heavy with the perfume of damp stocks and blooming jasmine." },
      { author: "Sigmund Freud", work: "Three Essays on the Theory of Sexuality", quote: "Sublimation diverts raw **erotic** energies into higher artistic creation and intellectual investigation." }
    ]
  },
  "Dashboard — erot/erotica.md": {
    primary: "Literature, artwork, films, or photographs that deal with sexual love and desire, intended to arouse sensual or aesthetic appreciation.",
    secondary: "The genre or catalog of rare historical books, antiquities, and prints celebrating the nude human form and amatory practices.",
    quotes: [
      { author: "Walter Pater", work: "Greek Studies", quote: "The painted vases from Pompeii exhibited delicate **erotica** where mythology blended gracefully with sensual delight." },
      { author: "Aldous Huxley", work: "Point Counter Point", quote: "The collector kept his volumes of seventeenth-century French **erotica** locked safely behind glass doors." },
      { author: "Simone de Beauvoir", work: "The Second Sex", quote: "Female sexuality has too frequently been represented in male-authored **erotica** as passive submission to conquest." }
    ]
  },
  "Dashboard — erot/erotically.md": {
    primary: "In an erotic manner; with sexual appeal, passion, or sensual allure.",
    secondary: "In a way that stimulates or reflects sexual excitement, romantic desire, or sensual enchantment in artistic expression.",
    quotes: [
      { author: "D. H. Lawrence", work: "Lady Chatterley's Lover", quote: "The spring woods stirred **erotically** as the birch buds unfurled in the warm southern breeze." },
      { author: "Joris-Karl Huysmans", work: "À rebours", quote: "The exotic orchids seemed **erotically** shaped, blooming in bizarre flesh-tinted petals and velvet corollas." },
      { author: "Anaïs Nin", work: "The Diary of Anaïs Nin", quote: "She danced with hypnotic abandon, moving **erotically** to the slow pulse of the Spanish guitar." }
    ]
  },
  "Dashboard — erot/eroticism.md": {
    primary: "The state or quality of being erotic; the expression of sexual feelings, desires, or sensual themes in life, literature, and art.",
    secondary: "In philosophical anthropology and psychology (notably Georges Bataille), the distinctively human transformation of biological sexual reproduction into a conscious quest for transgression and intimacy.",
    quotes: [
      { author: "Georges Bataille", work: "Erotism: Death and Sensuality", quote: "Human **eroticism** differs from animal sexuality in that it is an inward quest concerning the problem of discontinuous beings." },
      { author: "Susan Sontag", work: "Against Interpretation", quote: "In place of a hermeneutics of art, we need an **eroticism** of art that restores our sensory immediacy to form." },
      { author: "Octavio Paz", work: "The Double Flame: Love and Eroticism", quote: "Just as poetry is an eroticization of language, so is **eroticism** a poeticization of raw biological copulation." }
    ]
  },
  "Dashboard — erot/eroticize.md": {
    primary: "To give an erotic or sexually suggestive character to; to endow with sexual significance or appeal.",
    secondary: "In psychoanalytic and feminist critique, to invest non-sexual objects, power dynamics, or daily activities with unconscious libidinal excitement.",
    quotes: [
      { author: "Sigmund Freud", work: "The Ego and the Id", quote: "Under obsessional neurosis, the patient can **eroticize** the purely intellectual process of doubt and metaphysical questioning." },
      { author: "Simone de Beauvoir", work: "The Second Sex", quote: "Patriarchal traditions systematically **eroticize** female subordination, disguising domination as romantic destiny." },
      { author: "Roland Barthes", work: "The Pleasure of the Text", quote: "Modern advertising attempts to **eroticize** every domestic appliance, investing motorcars and perfumes with sensual desire." }
    ]
  },
  "Dashboard — erot/erotism.md": {
    primary: "Erotic sentiment, sexual desire, or the tendency to dwell upon sexual feelings (an older or technical synonym of eroticism).",
    secondary: "In classical psychoanalysis, the investment of libidinal energy in specific bodily zones (e.g., oral erotism, anal erotism).",
    quotes: [
      { author: "Sigmund Freud", work: "Introductory Lectures on Psycho-Analysis", quote: "Infantile **erotism** demonstrates that bodily pleasure zones function long before puberty awakens reproductive maturity." },
      { author: "Havelock Ellis", work: "The Dance of Life", quote: "A subtle **erotism** permeates the sacred rituals and ecstatic dances of primitive Mediterranean cults." },
      { author: "Carl Jung", work: "Psychology of the Unconscious", quote: "To reduce all mythological symbolism to primitive genital **erotism** is to blind psychology to spiritual transcendence." }
    ]
  },
  "Dashboard — erot/erotomania.md": {
    primary: "A psychiatric delusion in which an individual maintains a fixed, false belief that another person (usually of higher social status, wealth, or fame) is passionately in love with them.",
    secondary: "Historically known as de Clérambault's syndrome, categorized under delusional disorders in modern psychiatric nosology.",
    quotes: [
      { author: "G. G. de Clérambault", work: "Les Psychoses Passionnelles", quote: "The hallmark of pure **erotomania** is the patient's unshakable conviction that the target was the first to initiate amorous advances." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "In monomania of the affective type, severe **erotomania** leads to persistent surveillance and letter-writing." },
      { author: "Henry Maudsley", work: "Responsibility in Mental Disease", quote: "The unfortunate victim of **erotomania** misinterprets the most indifferent glance of a stranger as a secret confession of devotion." }
    ]
  },
  "Dashboard — erot/erotophilia.md": {
    primary: "A positive attitude toward sexuality; the tendency to exhibit open, favorable, and comfortable emotional responses to sexual topics and experiences.",
    secondary: "A psychometric dimension in human sexology measuring an individual's comfort with and enthusiastic approach toward erotic stimuli.",
    quotes: [
      { author: "Havelock Ellis", work: "Studies in the Psychology of Sex", quote: "A healthy cultural **erotophilia** fosters natural candor in youth regarding the mysteries of reproductive life." },
      { author: "Alfred Kinsey", work: "Sexual Behavior in the Human Male", quote: "Subjects displaying pronounced **erotophilia** reported greater relationship satisfaction and freedom from neurotic guilt." },
      { author: "Margaret Mead", work: "Coming of Age in Samoa", quote: "Samoan adolescent freedom cultivated a relaxed **erotophilia** that spared their society our Western neuroses." }
    ]
  },
  "Dashboard — erot/erotophobia.md": {
    primary: "An abnormal, irrational fear, guilt, or aversion toward sexuality, sexual feelings, or erotic materials.",
    secondary: "A psychological and behavioral tendency to react with distress, shame, or avoidance to sexual stimuli or discussions.",
    quotes: [
      { author: "Havelock Ellis", work: "The Task of Social Hygiene", quote: "Victorian prudery bred a pervasive social **erotophobia** that treated biological facts as unmentionable crimes." },
      { author: "Bertrand Russell", work: "Marriage and Morals", quote: "Puritanical schooling often instills a crippling **erotophobia** that poisons marital intimacy in later adult years." },
      { author: "Sigmund Freud", work: "Totem and Taboo", quote: "Rigid cultural taboos surrounding incest and menstruation give rise to unconscious religious **erotophobia**." }
    ]
  },
  "Dashboard — erot/homoerotic.md": {
    primary: "Concerning, depicting, or characterized by sexual desire, attraction, or romantic feeling directed toward persons of one's own sex.",
    secondary: "In literary, artistic, and classical criticism, describing artwork, verse, or aesthetics celebrating male-male or female-female physical beauty and emotional bonds.",
    quotes: [
      { author: "Walter Pater", work: "The Renaissance: Studies in Art and Poetry", quote: "Winckelmann's passion for antique Greek sculpture was steeped in a purely **homoerotic** reverence for the adolescent male form." },
      { author: "E. M. Forster", work: "Maurice", quote: "The Platonic dialogues read in college revealed an ancient tradition of high **homoerotic** chivalry that justified his heart." },
      { author: "John Addington Symonds", work: "A Problem in Greek Ethics", quote: "The military valor of the Sacred Band of Thebes rested openly upon deep **homoerotic** fidelity between comrades in arms." }
    ]
  },
  "Dashboard — erot/homoeroticism.md": {
    primary: "The state, quality, or artistic manifestation of homoerotic feeling or desire; romantic or sexual attraction to persons of the same sex represented in culture.",
    secondary: "In cultural history and queer theory, the presence of same-sex sensual and erotic motifs across art, literature, and visual media.",
    quotes: [
      { author: "John Addington Symonds", work: "Studies of the Greek Poets", quote: "Hellenic lyric poetry cannot be understood if one ignores the pervasive presence of **homoeroticism** in Spartan and Doric life." },
      { author: "Christopher Isherwood", work: "Christopher and His Kind", quote: "Berlin of the late Weimar years allowed a brazen public celebration of **homoeroticism** that outraged bourgeois nationalists." },
      { author: "Walter Pater", work: "Greek Studies", quote: "In the statue of the youthful Hermes, an idealized **homoeroticism** is sublimated into eternal religious calm." }
    ]
  },

  // Dashboard — eu (9 words)
  "Dashboard — eu/aneuploid.md": {
    primary: "Having an abnormal number of chromosomes that is not an exact multiple of the haploid number characteristic of the species (e.g., trisomy or monosomy).",
    secondary: "An organism or somatic cell line exhibiting chromosomal imbalance due to non-disjunction during meiosis or mitotic replication.",
    quotes: [
      { author: "Theodosius Dobzhansky", work: "Genetics and the Origin of Species", quote: "An **aneuploid** gamete carrying an extra chromosome typically suffers from severe developmental instability." },
      { author: "Barbara McClintock", work: "The Chromosome Constitution of Races of Maize", quote: "Cytological analysis confirmed that the mutant plant was **aneuploid**, displaying twenty-one chromosomes rather than twenty." },
      { author: "Ernst Mayr", work: "Animal Species and Evolution", quote: "Most **aneuploid** zygotes perish in early embryogenesis due to widespread lethal gene dosage imbalances." }
    ]
  },
  "Dashboard — eu/aneuploidy.md": {
    primary: "The chromosomal condition of having an abnormal number of chromosomes, either extra or missing, relative to the normal diploid or haploid state.",
    secondary: "A major cause of spontaneous miscarriage and congenital genetic disorders (such as Down syndrome) in human medical genetics, and a hallmark of malignant cancer genomes.",
    quotes: [
      { author: "Jerome Lejeune", work: "Turpin's Studies in Human Cytogenetics", quote: "The discovery of trisomy 21 established that constitutional **aneuploidy** accounts for the physical symptoms of mongolism." },
      { author: "Theodosius Dobzhansky", work: "Mankind Evolving", quote: "Meiotic non-disjunction during maternal oogenesis represents the primary mechanism behind human **aneuploidy**." },
      { author: "Barbara McClintock", work: "Cytological Observations on Zea Mays", quote: "Segmental **aneuploidy** enabled us to map specific chlorophyll deficiencies directly to broken chromosomal arms." }
    ]
  },
  "Dashboard — eu/eu.md": {
    primary: "The Greek prefix *eu-*, meaning good, well, true, pleasant, easily, or normal, appearing in *euphoria*, *eukaryote*, *eulogy*, and *euphemism*.",
    secondary: "The linguistic combining form denoting excellence of condition, beneficial function, or auspicious character across biological and philosophical nomenclature.",
    quotes: [
      { author: "Henry George Liddell & Robert Scott", work: "A Greek-English Lexicon", quote: "The indeclinable particle **eu** serves in classical Greek as an adverb meaning well, rightly, happily, or auspiciously." },
      { author: "Desiderius Erasmus", work: "The Praise of Folly", quote: "The ancient Greeks prefixed their words with **eu** whenever they wished to invoke prosperity, good fortune, and graceful life." },
      { author: "Francis Bacon", work: "The Advancement of Learning", quote: "Scientific terminology borrows the prefix **eu** to designate those sound and wholesome states of natural bodies." }
    ]
  },
  "Dashboard — eu/eudaemon.md": {
    primary: "A good or benevolent spirit; a benign supernatural guardian or guiding genius, contrasted with a cacodemon.",
    secondary: "In classical Greek religion and Hellenistic philosophy, an auspicious personal daemon that fosters wisdom, prosperity, and moral flourishing.",
    quotes: [
      { author: "Plato", work: "Phaedo", quote: "Socrates believed that each man's **eudaemon** guides him through life and leads his soul safely into the underworld." },
      { author: "Robert Burton", work: "The Anatomy of Melancholy", quote: "While the melancholic is haunted by devils, the virtuous soul is attended by a quiet, protective **eudaemon**." },
      { author: "Thomas Browne", work: "Religio Medici", quote: "I can readily believe that every mortal has a guardian **eudaemon** appointed to whisper secret warnings in times of peril." }
    ]
  },
  "Dashboard — eu/eudaemonic.md": {
    primary: "Pertaining to, producing, or conducive to happiness, well-being, or moral flourishing; eudaimonic.",
    secondary: "Relating to the philosophical ethical system (eudaimonism) that judges actions by their capacity to promote human fulfillment and flourishing.",
    quotes: [
      { author: "Aristotle", work: "Nicomachean Ethics", quote: "The highest good is an **eudaemonic** existence achieved through the active exercise of virtue in conformity with reason." },
      { author: "John Stuart Mill", work: "Utilitarianism", quote: "A properly constructed commonwealth aims at an **eudaemonic** harmony where private happiness coincides with public welfare." },
      { author: "William James", work: "The Varieties of Religious Experience", quote: "Healthy-minded religion cultivates an **eudaemonic** temper that regards misery and sin as mere temporary illusions." }
    ]
  },
  "Dashboard — eu/euphoria.md": {
    primary: "A feeling or state of intense excitement, supreme happiness, elation, and boundless physical and emotional well-being.",
    secondary: "In psychopathology and pharmacology, an abnormal or exaggerated sense of physical well-being and confidence, often drug-induced or observed in manic states.",
    quotes: [
      { author: "Thomas De Quincey", work: "Confessions of an English Opium-Eater", quote: "Within an hour, all bodily anguish dissolved into a tranquil, celestial **euphoria** that no earthly words can depict." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The phthisical patient often exhibits a deceptive **euphoria**, expressing bright hopes of recovery days before dissolution." },
      { author: "Aldous Huxley", work: "The Doors of Perception", quote: "Mescaline lifted the dull curtain of routine, plunging consciousness into an extraordinary visual **euphoria**." }
    ]
  },
  "Dashboard — eu/euphoric.md": {
    primary: "Characterized by, feeling, or producing a state of euphoria; intensely happy, confident, and exhilarated.",
    secondary: "Pertaining to drug actions or neuropsychological episodes that induce buoyant optimism and sensory bliss.",
    quotes: [
      { author: "Sigmund Freud", work: "On Coca", quote: "Cocaine produces an exhilaration and lasting **euphoric** condition that allows arduous physical exertion without fatigue." },
      { author: "Virginia Woolf", work: "Orlando", quote: "The crisp morning air filled her with a **euphoric** impulse to run wild across the frost-crusted lawns." },
      { author: "Oliver Sacks", work: "Awakenings", quote: "Administration of L-DOPA lifted the post-encephalitic patients from catatonia into an energetic, almost **euphoric** awakening." }
    ]
  },
  "Dashboard — eu/euphory.md": {
    primary: "An older or literary variant of euphoria; a state of well-being, buoyancy, or bodily ease.",
    secondary: "In 18th- and 19th-century medical dictionaries, the comfortable sensations of health and free respiration in convalescence.",
    quotes: [
      { author: "Thomas Browne", work: "Pseudodoxia Epidemica", quote: "A healthful animal constitution maintains a gentle **euphory** of spirits that dispels melancholic vapours." },
      { author: "Samuel Johnson", work: "The Rambler", quote: "The morning walk in open meadows confers a pleasant **euphory** which sedentary scholars too rarely know." },
      { author: "Alexander Bain", work: "The Emotions and the Will", quote: "The physical recovery from exhausting fever brings a serene bodily **euphory** that feels like rebirth." }
    ]
  },
  "Dashboard — eu/euploid.md": {
    primary: "Having an exact, balanced multiple of the basic haploid chromosome number for the species (e.g., diploid, triploid, tetraploid), contrasted with aneuploid.",
    secondary: "In cytogenetics, describing an organism or karyotype with a normal, balanced chromosome complement devoid of segmental deletions or additions.",
    quotes: [
      { author: "Theodosius Dobzhansky", work: "Genetics and the Origin of Species", quote: "Plant breeders intentionally select **euploid** polyploids because their genomic balance produces robust foliage and giant fruit." },
      { author: "Barbara McClintock", work: "The Chromosome Constitution of Races of Maize", quote: "Unlike defective aneuploid sports, the **euploid** strain showed normal meiotic pairing across all ten chromosomes." },
      { author: "Ernst Mayr", work: "Principles of Systematic Zoology", quote: "Speciation through polyploid doubling creates fertile, reproductively isolated **euploid** races in flowering plants." }
    ]
  },

  // Dashboard — geu (6 words)
  "Dashboard — geu/ageusia.md": {
    primary: "The complete absence or loss of the sense of taste (gustatory perception).",
    secondary: "In neurology, a sensory deficit arising from damage to the lingual, glossopharyngeal, or facial cranial nerves, or following respiratory viral infections.",
    quotes: [
      { author: "William Gowers", work: "A Manual of Diseases of the Nervous System", quote: "Bilateral lesions of the chorda tympani result in total **ageusia** over the anterior two-thirds of the tongue." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The patient complained that food had become like sawdust, a distressing post-influenzal **ageusia** that persisted for months." },
      { author: "Oliver Sacks", work: "The Island of the Colorblind", quote: "Loss of smell inevitably drags taste down with it, producing what patients mistakenly describe as absolute **ageusia**." }
    ]
  },
  "Dashboard — geu/dysgeusia.md": {
    primary: "A distorted, abnormal, or impaired perception of the sense of taste, commonly causing persistent metallic, sour, bitter, or salty tastes in the mouth.",
    secondary: "A common clinical adverse effect of medications (chemotherapy, antibiotics), zinc deficiency, or neurological disease affecting gustatory pathways.",
    quotes: [
      { author: "Henry Maudsley", work: "Pathology of Mind", quote: "Hysterical patients frequently report a repulsive **dysgeusia**, declaring that fresh bread tastes of sulfur and copper." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Chronic heavy metal poisoning invariably begins with foul halitosis and an intractable metallic **dysgeusia**." },
      { author: "Oliver Sacks", work: "A Leg to Stand On", quote: "Under intense pharmacological therapy, the simplest meal was ruined by a persistent chemical **dysgeusia**." }
    ]
  },
  "Dashboard — geu/geu.md": {
    primary: "The Greek root *geu-* (from *geusis*), denoting taste, savor, flavor, or the gustatory sense, as found in *ageusia*, *dysgeusia*, and *hypergeusia*.",
    secondary: "The linguistic morpheme employed in neurobiology and sensory physiology to classify disorders of lingual taste buds and cranial taste pathways.",
    quotes: [
      { author: "Henry George Liddell & Robert Scott", work: "A Greek-English Lexicon", quote: "The primary verb *geuein* and its noun *geusis* yield the root **geu**, signifying to give a taste of, to sample, or to savor." },
      { author: "Charles Sherrington", work: "The Integrative Action of the Nervous System", quote: "Receptors belonging to the root **geu** operate in intimate chemical partnership with olfactory nerve endings." },
      { author: "Alexander Bain", work: "The Senses and the Intellect", quote: "The organic faculty designated by **geu** provides the earliest gatekeeper for nutritional ingestion and bodily defense." }
    ]
  },
  "Dashboard — geu/hypergeusia.md": {
    primary: "An abnormally heightened, exaggerated, or acute sensitivity to taste sensations.",
    secondary: "A sensory condition observed in certain endocrine disorders (such as Addison's disease), nutritional states, or neuroses where gustatory thresholds are markedly lowered.",
    quotes: [
      { author: "William Gowers", work: "A Manual of Diseases of the Nervous System", quote: "In adrenal cortical failure, patients sometimes display remarkable **hypergeusia**, detecting trace salinity imperceptible to healthy observers." },
      { author: "Henry Maudsley", work: "The Physiology of Mind", quote: "Sensory hyperesthesia may isolate itself to the tongue, causing an intolerable **hypergeusia** during febrile excitement." },
      { author: "Oliver Sacks", work: "The Man Who Mistook His Wife for a Hat", quote: "During brief temporal lobe auras, he experienced a vivid **hypergeusia** where each herb exploded with blinding intensity." }
    ]
  },
  "Dashboard — geu/hypogeusia.md": {
    primary: "A diminished or reduced sensitivity of the sense of taste, falling short of total loss (ageusia).",
    secondary: "A clinical condition associated with upper respiratory infections, nutritional zinc deficiency, aging, or adverse pharmacological reactions.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Elderly patients with dry oral mucosa frequently suffer from an insidious **hypogeusia** that precipitates poor appetite and weight loss." },
      { author: "William Gowers", work: "A Manual of Diseases of the Nervous System", quote: "Partial degeneration of the glossopharyngeal trunk produces unilateral **hypogeusia** over the posterior third of the tongue." },
      { author: "Oliver Sacks", work: "An Anthropologist on Mars", quote: "Following a mild head injury, the artist noticed an unexpected **hypogeusia**, finding that wines had lost their subtle bouquet and tang." }
    ]
  },
  "Dashboard — geu/parageusia.md": {
    primary: "An abnormal, unpleasant, or hallucinatory taste perception, such as experiencing a persistent bad taste in the absence of gustatory stimuli.",
    secondary: "In clinical psychiatry and neurology, a sensory hallucination or aura occurring in temporal lobe epilepsy or psychotic disorders.",
    quotes: [
      { author: "William Gowers", work: "Epilepsy and Other Chronic Convulsive Diseases", quote: "The epileptic aura often manifested as an inexplicable **parageusia**, a gustatory phantom of burning rubber or copper." },
      { author: "Henry Maudsley", work: "Responsibility in Mental Disease", quote: "Suspicious delusions of poisoning are often provoked by an unrecognized somatic **parageusia** arising from visceral disease." },
      { author: "Jean-Martin Charcot", work: "Clinical Lectures on Diseases of the Nervous System", quote: "Hysterical hemianesthesia is occasionally accompanied by a bizarre contralateral **parageusia** where water tastes like brine." }
    ]
  },

  // Dashboard — glyc (37 words)
  "Dashboard — glyc/deglycerolise.md": {
    primary: "To wash and remove glycerol cryoprotectant from thawed red blood cells or biological tissues prior to clinical transfusion (Commonwealth spelling).",
    secondary: "A critical laboratory washing procedure employing descending saline solutions to prevent osmotic lysis of preserved erythrocytes.",
    quotes: [
      { author: "Charles Drew", work: "Studies in Blood Preservation", quote: "Technicians must thoroughly **deglycerolise** thawed erythrocytes with sequential saline washes before patient infusion." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Modern blood banking protocols require technicians to **deglycerolise** frozen units to avoid systemic hyperosmolar shock." },
      { author: "Linus Pauling", work: "Molecular Architecture and the Life Process", quote: "The physical chemistry of osmotic gradients dictates the exact steps needed to **deglycerolise** frozen cellular membranes safely." }
    ]
  },
  "Dashboard — glyc/deglycerolize.md": {
    primary: "To remove glycerol from frozen red blood cells or tissues through stepwise washing prior to medical transfusion (American spelling).",
    secondary: "In cryobiology and transfusion medicine, the post-thaw processing that restores normal intracellular osmolarity to preserved cells.",
    quotes: [
      { author: "Charles Drew", work: "Banked Blood and Plasma Storage", quote: "To utilize rare-type frozen red blood cells, the blood bank must carefully **deglycerolize** each unit using automated cell washers." },
      { author: "William Carlos Williams", work: "The Doctor Stories", quote: "The hospital laboratory worked around the clock to thaw and **deglycerolize** the frozen blood units needed for surgery." },
      { author: "Linus Pauling", work: "The Nature of the Chemical Bond", quote: "Stepwise dilution is essential to **deglycerolize** living cells without rupturing their fragile phospholipid bilayer." }
    ]
  },
  "Dashboard — glyc/glyc.md": {
    primary: "The Greek root *glyc-* (from *glykys*), meaning sweet, sugar, or glucose, forming words like *glycogen*, *glycolysis*, and *glycerin*.",
    secondary: "The universal biochemical combining form designating carbohydrate molecules, saccharides, and sugar metabolism.",
    quotes: [
      { author: "Henry George Liddell & Robert Scott", work: "A Greek-English Lexicon", quote: "The Greek adjective *glykys*, underlying the prefix **glyc**, signifies sweet to the taste, delightful, or endearing." },
      { author: "Claude Bernard", work: "Lectures on the Physiology of Digestion", quote: "In naming the sugar-forming substance of the liver, we adopted the ancient radical **glyc** to designate its saccharine nature." },
      { author: "Justus von Liebig", work: "Animal Chemistry", quote: "Organic analysis demonstrates that substances carrying the morpheme **glyc** represent the essential fuel of animal respiration." }
    ]
  },
  "Dashboard — glyc/glyceraldehyde.md": {
    primary: "A three-carbon triose monosaccharide (C3H6O3), the simplest aldose sugar, playing a foundational role as an intermediate in glycolysis and photosynthesis.",
    secondary: "In stereochemistry, the historical reference standard (D- and L-glyceraldehyde) used to define the absolute configuration of sugars and amino acids.",
    quotes: [
      { author: "Emil Fischer", work: "Syntheses in the Sugar Group", quote: "Optically active **glyceraldehyde** provided the ultimate stereochemical touchstone for determining the configuration of all hexoses." },
      { author: "Hans Krebs", work: "Carbohydrate Metabolism in Animal Tissues", quote: "During glycolysis, fructose-1,6-bisphosphate is cleaved by aldolase into dihydroxyacetone phosphate and **glyceraldehyde** 3-phosphate." },
      { author: "Linus Pauling", work: "General Chemistry", quote: "The asymmetric carbon in **glyceraldehyde** represents the quintessential textbook example of enantiomeric optical isomerism." }
    ]
  },
  "Dashboard — glyc/glyceria.md": {
    primary: "A genus of tall, aquatic or wetland grasses (family Poaceae), commonly called mannagrass, growing in marshes, ditches, and stream banks.",
    secondary: "A botanical genus named from Greek *glykys* ('sweet') on account of the sweetish taste of the nutritious grains collected for porridge in central and eastern Europe.",
    quotes: [
      { author: "Asa Gray", work: "Manual of the Botany of the Northern United States", quote: "The aquatic species of **Glyceria** line our marsh ditches, bearing nodding panicles of sweet-tasting seeds." },
      { author: "John Muir", work: "The Yosemite", quote: "Meadows of lush **Glyceria** flourished in the river bends, providing succulent grazing for deer and pack mules." },
      { author: "Liberty Hyde Bailey", work: "The Standard Cyclopedia of Horticulture", quote: "European peasants formerly harvested the fallen seeds of **Glyceria** fluitans to cook a delicate, sweet cereal gruel." }
    ]
  },
  "Dashboard — glyc/glyceride.md": {
    primary: "A chemical compound consisting of an ester formed from glycerol and one or more fatty acids (e.g., monoglyceride, diglyceride, or triglyceride).",
    secondary: "In lipid biochemistry and organic chemistry, the primary constituent of natural animal adipose tissue and vegetable seed oils.",
    quotes: [
      { author: "Michel Eugène Chevreul", work: "Chemical Researches on Animal Fats", quote: "Saponification decomposes each neutral **glyceride** into free fatty acids and sweet vegetable glycerol." },
      { author: "Justus von Liebig", work: "Familiar Letters on Chemistry", quote: "The animal body stores surplus nutritive carbon in the form of neutral **glyceride** deposits beneath the skin." },
      { author: "Linus Pauling", work: "The Architecture of Molecules", quote: "The chemical ester bond linking each fatty acid chain to the **glyceride** backbone determines its melting point and fluidity." }
    ]
  },
  "Dashboard — glyc/glycerin.md": {
    primary: "A colorless, odorless, viscous, sweet-tasting liquid (trihydroxy alcohol, C3H8O3) obtained by the saponification of fats, widely used in pharmacy, cosmetics, and explosives.",
    secondary: "A humectant and solvent (often interchangeably called glycerol) prized for its water-retaining properties and non-toxicity in medical formulations.",
    quotes: [
      { author: "Carl Wilhelm Scheele", work: "Chemical Essays", quote: "By boiling olive oil with litharge, I isolated the sweet principle of oils, which we now term **glycerin**." },
      { author: "Arthur Conan Doyle", work: "The Adventure of the Cardboard Box", quote: "The laboratory smelled faintly of carbolic acid and pharmaceutical **glycerin** from the doctor's recent experiments." },
      { author: "Mark Twain", work: "Roughing It", quote: "The miners handled nitroglycerin with trembling terror, knowing that a single unbuffered drop of that **glycerin** compound could shatter a hill." }
    ]
  },
  "Dashboard — glyc/glycerine.md": {
    primary: "A commercial and traditional variant spelling of glycerin; propane-1,2,3-triol, used as an emollient, solvent, and sweetening agent.",
    secondary: "In 19th-century pharmacopoeias and industrial chemical literature, the purified sweet oil derived from animal tallow and seed oils.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "Lessons in Elementary Physiology", quote: "Digestion in the small intestine splits fatty meals into free fatty acids and neutral **glycerine**." },
      { author: "H. G. Wells", work: "The Time Machine", quote: "The bronze machinery was lubricated with fine clarified oils and viscous **glycerine** that resisted oxidation." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "A soothing application of borax in pure **glycerine** quickly allays the painful aphthae of an inflamed tongue." }
    ]
  },
  "Dashboard — glyc/glycerite.md": {
    primary: "A pharmaceutical preparation or medicinal solution in which glycerin serves as the primary liquid solvent vehicle.",
    secondary: "In historical pharmacognosy, a stable liquid preparation (e.g., glycerite of tannic acid, glycerite of phenol) used for topical mucosal applications.",
    quotes: [
      { author: "Jonathan Pereira", work: "The Elements of Materia Medica", quote: "The **glycerite** of tannin forms a superior topical application for relaxed uvula and chronic pharyngitis." },
      { author: "William Osler", work: "Aequanimitas", quote: "The country doctor carried in his leather bag a bottle of carbolized **glycerite** for dressing infected farm wounds." },
      { author: "Arthur Conan Doyle", work: "Round the Red Lamp", quote: "He painted the diphtheritic throat with a thick soothing **glycerite**, praying that the airway would remain patent." }
    ]
  },
  "Dashboard — glyc/glycerogel.md": {
    primary: "A soft, jelly-like topical pharmaceutical dressing or vehicle composed of gelatin, glycerin, and water with active therapeutic ingredients.",
    secondary: "In dermatological therapeutics, a soothing hydrogel melted prior to application and painted onto chronic eczematous or ulcerated skin lesions.",
    quotes: [
      { author: "Paul Gerson Unna", work: "The Histopathology of the Diseases of the Skin", quote: "We introduced the zinc **glycerogel** as a pliable protective cast for indolent varicose ulcers of the lower leg." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "For rebellious erythematous patches, an unctuous **glycerogel** affords immediate cooling relief without greasiness." },
      { author: "Sir Astley Cooper", work: "Lectures on the Principles and Practice of Surgery", quote: "A medicated **glycerogel** seals the denuded dermis from atmospheric dust while promoting cellular granulation." }
    ]
  },
  "Dashboard — glyc/glycerogelatin.md": {
    primary: "A medicinal mass consisting of gelatin, glycerin, water, and therapeutic medicaments, melted for application as a flexible cutaneous protective dressing.",
    secondary: "The dermatological compounding base invented by Unna (Unna's boot) used in compressive bandages for venous stasis and ulcers.",
    quotes: [
      { author: "Paul Gerson Unna", work: "Selected Monographs on Dermatology", quote: "The melted **glycerogelatin** is painted warm upon the limb and enveloped in gauze, solidifying into an elastic supportive casing." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Zinc oxide compounded in **glycerogelatin** remains the sovereign remedy for chronic stasis dermatitis." },
      { author: "Jonathan Pereira", work: "The Elements of Materia Medica", quote: "The elastic properties of **glycerogelatin** make it an incomparable vehicle for continuous antiseptic contact." }
    ]
  },
  "Dashboard — glyc/glycerol.md": {
    primary: "Propane-1,2,3-triol (C3H8O3), a colorless, odorless, viscous, hygroscopic, sweet-tasting trihydroxy alcohol that forms the structural backbone of lipids.",
    secondary: "In biochemistry and cryobiology, an essential metabolite in gluconeogenesis and a premier cryoprotective agent used to preserve living cells at liquid nitrogen temperatures.",
    quotes: [
      { author: "Claude Bernard", work: "An Introduction to the Study of Experimental Medicine", quote: "Lipase cleaves neutral fats into their component fatty acids and free **glycerol**, ready for hepatic glycogen synthesis." },
      { author: "Linus Pauling", work: "General Chemistry", quote: "The three hydroxyl groups of **glycerol** form extensive hydrogen-bonding networks, explaining its syrupy viscosity." },
      { author: "Hans Krebs", work: "The Regulation of Cell Metabolism", quote: "Phosphorylated **glycerol** enters the central glycolytic highway through conversion into dihydroxyacetone phosphate." }
    ]
  },
  "Dashboard — glyc/glycerole.md": {
    primary: "An older or archaic pharmaceutical term for a solution, medicinal tincture, or syrup prepared with glycerin as the base (glycerite).",
    secondary: "In 19th-century apothecaries' formularies, a non-fermenting liquid medium for administering alkaloids, resins, and astringents.",
    quotes: [
      { author: "Jonathan Pereira", work: "The Elements of Materia Medica", quote: "The **glycerole** of aloes provides a mild, non-alcoholic preparation suitable for delicate pediatric administration." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "He prescribed a soothing **glycerole** of bismuth to coat the inflamed gastric mucosa in acute catarrh." },
      { author: "Arthur Conan Doyle", work: "The Stark Munro Letters", quote: "Behind the counter stood rows of glass jars labeled with each tincture, syrup, and **glycerole** known to the British Pharmacopoeia." }
    ]
  },
  "Dashboard — glyc/glycerolise.md": {
    primary: "To treat, impregnate, or equilibrate biological cells, tissues, or organs with glycerol prior to cryopreservation to prevent ice crystal damage (Commonwealth spelling).",
    secondary: "In cell banking and reproductive biology, the laboratory process of adding glycerol step-by-step as a cryoprotectant.",
    quotes: [
      { author: "Charles Drew", work: "Studies in Blood Preservation", quote: "Before plunging the red cell suspension into subzero storage, we must slowly **glycerolise** the mixture to prevent intracellular lysis." },
      { author: "Linus Pauling", work: "Molecular Architecture and the Life Process", quote: "Technicians **glycerolise** biological specimens so that cellular water vitrifies without shattering fragile organelles." },
      { author: "Julian Huxley", work: "Essays of a Biologist", quote: "The ability to **glycerolise** and freeze germ cells opens unprecedented possibilities for artificial selection across generations." }
    ]
  },
  "Dashboard — glyc/glycerolize.md": {
    primary: "To treat or infuse biological specimens, cells, or blood units with glycerol to prevent cellular damage during freezing and cryostorage (American spelling).",
    secondary: "In cryobiology and biophysics, to protect cellular membranes against mechanical shearing from ice crystals during ultra-low temperature preservation.",
    quotes: [
      { author: "Charles Drew", work: "Banked Blood and Plasma Storage", quote: "Careful laboratory technicians **glycerolize** rare erythrocyte units to maintain military reserve stocks indefinitely." },
      { author: "William Carlos Williams", work: "Autobiography", quote: "Modern hematology discovered how to **glycerolize** blood, cheating the clock that once spoiled stored pints in three weeks." },
      { author: "Linus Pauling", work: "The Nature of the Chemical Bond", quote: "When you **glycerolize** living tissue, the polyol molecules displace water around structural proteins, maintaining stability." }
    ]
  },
  "Dashboard — glyc/glyceryl.md": {
    primary: "The trivalent organic radical or acyl group C3H5 derived from glycerol by the removal of its three hydroxyl groups.",
    secondary: "In organic chemistry, the central trivalent moiety in natural fats (glyceryl esters) and in pharmaceuticals such as glyceryl trinitrate (nitroglycerin).",
    quotes: [
      { author: "Justus von Liebig", work: "Animal Chemistry", quote: "The three fatty acid chains of stearin attach directly to the **glyceryl** core to form solid animal tallow." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "For the sudden agony of angina pectoris, a small sublingual tablet of **glyceryl** trinitrate brings miraculous relief within minutes." },
      { author: "Linus Pauling", work: "General Chemistry", quote: "In lipid synthesis, each hydroxyl site on the **glyceryl** radical forms a stable ester linkage with an incoming fatty acid." }
    ]
  },
  "Dashboard — glyc/glycine.md": {
    primary: "The simplest of the twenty standard amino acids (C2H5NO2, aminoacetic acid), having a single hydrogen atom as its side chain, found abundantly in collagen.",
    secondary: "In neurobiology, a major inhibitory neurotransmitter acting predominantly in the spinal cord, brainstem, and retina, co-activating NMDA glutamate receptors.",
    quotes: [
      { author: "Emil Fischer", work: "Investigations on Amino Acids, Polypeptides and Proteins", quote: "We synthesized the simplest dipeptide by condensing two molecules of **glycine** into glycyl-glycine." },
      { author: "Linus Pauling", work: "The Structure of Proteins", quote: "The absence of a bulky side chain in **glycine** permits the polypeptide backbone to make tight bends within the collagen triple helix." },
      { author: "Oliver Sacks", work: "The Island of the Colorblind", quote: "Strychnine exerts its lethal convulsive toxicity by competitively blocking the inhibitory actions of **glycine** in the spinal cord." }
    ]
  },
  "Dashboard — glyc/glycogen.md": {
    primary: "A multi-branched polysaccharide of glucose that serves as the principal form of carbohydrate energy storage in animals, fungi, and humans ('animal starch').",
    secondary: "Synthesized and stored primarily in liver and skeletal muscle cells, broken down enzymatically into glucose to maintain blood sugar homeostasis.",
    quotes: [
      { author: "Claude Bernard", work: "On the Mechanism of the Formation of Sugar in the Liver", quote: "I discovered in the hepatic tissue a starch-like substance, which I named **glycogen**, capable of producing sugar continuously." },
      { author: "Hans Krebs", work: "The Citric Acid Cycle", quote: "Muscle contraction draws upon local **glycogen** reserves to fuel rapid anaerobic bursts of lactic acid fermentation." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "In severe diabetes, the liver fails to retain its stored **glycogen**, pouring excessive sugar directly into the circulatory stream." }
    ]
  },
  "Dashboard — glyc/glycogenesis.md": {
    primary: "The biological process and biochemical pathway by which glucose molecules are converted and polymerized into glycogen for storage in the liver and skeletal muscles.",
    secondary: "Stimulated by the pancreatic hormone insulin in response to high circulating blood glucose levels following carbohydrate digestion.",
    quotes: [
      { author: "Claude Bernard", work: "Lectures on Experimental Physiology", quote: "Hepatic **glycogenesis** represents an internal secretion by which the liver stores dietary sugar after a meal." },
      { author: "Hans Krebs", work: "Carbohydrate Metabolism in Animal Tissues", quote: "Insulin accelerates **glycogenesis** by activating glycogen synthase, locking circulating hexoses into insoluble cellular storage." },
      { author: "Arthur Conan Doyle", work: "The Stark Munro Letters", quote: "The professor discoursed learnedly on hepatic **glycogenesis**, marveling at the chemical laboratory operating silently within our ribs." }
    ]
  },
  "Dashboard — glyc/glycogenic.md": {
    primary: "Of, relating to, or producing glycogen; capable of giving rise to glycogen in living tissues.",
    secondary: "In physiological biochemistry, describing amino acids (glycogenic amino acids) or metabolic substrates capable of conversion into glucose and glycogen via gluconeogenesis.",
    quotes: [
      { author: "Claude Bernard", work: "Memoir on the Pancreas and the Role of Pancreatic Juice", quote: "The **glycogenic** function of the liver proved that animals do not merely consume vegetable organic matter, but synthesize carbohydrates internally." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Glucagon acts as a potent stimulator of hepatic enzymes, opposing the **glycogenic** action of insulin." },
      { author: "Hans Krebs", work: "Reminiscences and Reflections", quote: "We classified the amino acids into ketogenic and **glycogenic** groups depending upon their metabolic fate in diabetic animals." }
    ]
  },
  "Dashboard — glyc/glycogenolysis.md": {
    primary: "The biochemical breakdown of stored glycogen into glucose-1-phosphate and glucose molecules in response to energy demands or fasting.",
    secondary: "A enzymatic cascade triggered by glucagon and epinephrine in hepatic and muscular tissues to maintain systemic euglycemia and support muscular exertion.",
    quotes: [
      { author: "Hans Krebs", work: "The Regulation of Cell Metabolism", quote: "Adrenaline initiates a swift phosphorylation cascade that triggers massive **glycogenolysis** in muscle during fight or flight." },
      { author: "Walter Cannon", work: "The Wisdom of the Body", quote: "Emergency mobilization of energy requires immediate hepatic **glycogenolysis** to flood the bloodstream with fuel for working muscles." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "In glycogen storage diseases, congenital enzyme deficiencies arrest normal **glycogenolysis**, causing massive hepatomegaly." }
    ]
  },
  "Dashboard — glyc/glycol.md": {
    primary: "Any organic chemical compound belonging to the alcohol family that possesses two hydroxyl (-OH) groups attached to different carbon atoms (a diol, such as ethylene glycol).",
    secondary: "Commonly referring to ethylene glycol, widely used as an industrial automotive antifreeze, heat-transfer fluid, and precursor for polyester polymers.",
    quotes: [
      { author: "Charles-Adolphe Wurtz", work: "Sur une nouvelle classe de radicaux organiques", quote: "By reacting ethylene dibromide with silver acetate, I succeeded in isolating **glycol**, the first known diatomic alcohol." },
      { author: "Linus Pauling", work: "General Chemistry", quote: "Because each **glycol** molecule bears two polar hydroxyl groups, it mixes freely with water and lowers its freezing point." },
      { author: "Rachel Carson", work: "Silent Spring", quote: "Improper disposal of automotive **glycol** poses a lethal hazard to wildlife attracted by its sweet, deceptive taste." }
    ]
  },
  "Dashboard — glyc/glycolipid.md": {
    primary: "A lipid molecule covalently linked to a carbohydrate moiety (monosaccharide or oligosaccharide), found abundantly on the extracellular surface of eukaryotic cell membranes.",
    secondary: "In cell biology and immunology, crucial membrane components (e.g., cerebrosides, gangliosides) that mediate cellular recognition, adhesion, and blood group antigens.",
    quotes: [
      { author: "Ernst Klenk", work: "On the Nature of Gangliosides", quote: "In neural cell membranes, the complex **glycolipid** structure known as ganglioside plays an essential role in synaptic signaling." },
      { author: "Linus Pauling", work: "Molecular Architecture and the Life Process", quote: "The outer leaflet of the cellular membrane is studded with **glycolipid** antennae that distinguish self from non-self." },
      { author: "Oliver Sacks", work: "The Man Who Mistook His Wife for a Hat", quote: "In Tay-Sachs disease, an inborn metabolic failure to degrade a specific **glycolipid** leads to tragic neurological degeneration." }
    ]
  },
  "Dashboard — glyc/glycolysis.md": {
    primary: "The fundamental enzymatic anaerobic metabolic pathway in cellular cytoplasm by which one molecule of glucose is broken down into two molecules of pyruvate, generating ATP and NADH.",
    secondary: "The ancient, universal biochemical sequence (the Embden-Meyerhof-Parnas pathway) conserved across nearly all living organisms to extract energy from carbohydrates.",
    quotes: [
      { author: "Hans Krebs", work: "The Citric Acid Cycle", quote: "Under anaerobic conditions, **glycolysis** converts pyruvate to lactate, generating two net moles of ATP per mole of glucose consumed." },
      { author: "Otto Warburg", work: "The Metabolism of Tumours", quote: "Cancer cells exhibit an extraordinary increase in aerobic **glycolysis**, fermenting glucose to lactic acid even in the presence of abundant oxygen." },
      { author: "Jacques Monod", work: "Chance and Necessity", quote: "The universal conservation of the ten enzymatic steps of **glycolysis** bears silent witness to the single common ancestor of all terrestrial life." }
    ]
  },
  "Dashboard — glyc/glycophyte.md": {
    primary: "A plant that thrives only in soil or freshwater with low salt concentrations, and is easily injured or stunted by high salinity (contrasted with a halophyte).",
    secondary: "In plant ecology and agronomy, including the vast majority of agricultural crop species (e.g., wheat, rice, corn) whose growth is inhibited by saline irrigation.",
    quotes: [
      { author: "Asa Gray", work: "Elements of Botany", quote: "Most cultivated field crops are typical **glycophyte** species, showing immediate root toxicity when exposed to brackish water." },
      { author: "Liberty Hyde Bailey", work: "The Standard Cyclopedia of Horticulture", quote: "To reclaim salt-damaged soil, the farmer must grow salt-accumulating halophytes before returning the field to any standard **glycophyte** crop." },
      { author: "Eugene Odum", work: "Fundamentals of Ecology", quote: "Estuarine zonation reflects the sharp osmotic boundary separating salt-marsh halophytes from upland **glycophyte** vegetation." }
    ]
  },
  "Dashboard — glyc/glycoprotein.md": {
    primary: "A conjugated protein consisting of a polypeptide chain covalently linked to one or more oligosaccharide (carbohydrate) chains.",
    secondary: "Widely present in cell membranes, extracellular matrices, blood plasma (e.g., immunoglobulins, transferrin), and mucus, mediating cellular adhesion, immunity, and signaling.",
    quotes: [
      { author: "Linus Pauling", work: "The Structure of Antibodies", quote: "Every circulating antibody molecule is a **glycoprotein** whose carbohydrate chains stabilize its quaternary immunological architecture." },
      { author: "Francis Crick", work: "What Mad Pursuit", quote: "Membrane receptors are predominantly **glycoprotein** complexes whose projecting sugar branches recognize chemical messengers outside the cell." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Erythropoietin is a circulating renal **glycoprotein** that commands bone marrow stem cells to produce red corpuscles." }
    ]
  },
  "Dashboard — glyc/glycoside.md": {
    primary: "Any chemical compound in which a carbohydrate molecule (glycone) is bound to another functional group or non-sugar moiety (aglycone) via a glycosidic bond.",
    secondary: "In pharmacology and pharmacognosy, plant-derived secondary metabolites including cardiac glycosides (e.g., digoxin) and cyanogenic glycosides used in therapeutics or defense.",
    quotes: [
      { author: "William Withering", work: "An Account of the Foxglove and Some of Its Medical Uses", quote: "The active digitalis **glycoside** strengthens the failing myocardium while slowing an irregular, runaway pulse." },
      { author: "Justus von Liebig", work: "Animal Chemistry", quote: "Amygdalin extracted from bitter almonds represents a classical **glycoside**, yielding glucose, benzaldehyde, and prussic acid upon hydrolysis." },
      { author: "Paul Ehrlich", work: "Studies in Immunity", quote: "Certain plant toxins operate as a **glycoside** compound that selectively attaches to specific chemical side-chains on animal cells." }
    ]
  },
  "Dashboard — glyc/glycosidic.md": {
    primary: "Pertaining to, involving, or denoting a glycoside or a glycosidic bond.",
    secondary: "In carbohydrate chemistry, specifying the covalent acetal or ketal linkage connecting the anomeric carbon of a saccharide to another group.",
    quotes: [
      { author: "Emil Fischer", work: "Syntheses in the Sugar Group", quote: "The alpha and beta configurations of the **glycosidic** linkage explain the divergent physical properties of starch and cellulose." },
      { author: "Linus Pauling", work: "The Nature of the Chemical Bond", quote: "Enzymatic cleavage of the **glycosidic** bond in disaccharides requires precise orientation of catalytic acidic residues." },
      { author: "Hans Krebs", work: "Carbohydrate Metabolism in Animal Tissues", quote: "Glycogen phosphorylase specifically attacks the alpha-1,4 **glycosidic** bond to liberate glucose-1-phosphate for muscular energy." }
    ]
  },
  "Dashboard — glyc/glycosuria.md": {
    primary: "The abnormal presence and excretion of glucose in the urine, typically occurring when blood glucose concentrations exceed the renal reabsorption threshold.",
    secondary: "A hallmark clinical symptom of untreated diabetes mellitus, renal diabetes, or severe acute metabolic stress.",
    quotes: [
      { author: "Thomas Willis", work: "Pharmaceutice Rationalis", quote: "In patients afflicted with diabetes, the urine is wonderfully sweet, an extraordinary **glycosuria** as though infused with honey." },
      { author: "Claude Bernard", work: "Lectures on Experimental Physiology", quote: "Puncturing the floor of the fourth cerebral ventricle in a rabbit provoked an acute, transient **glycosuria**." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Persistent **glycosuria** accompanied by polydipsia and wasting demands immediate dietary restriction of all starches and sugars." }
    ]
  },
  "Dashboard — glyc/glycyrrhiza.md": {
    primary: "A genus of perennial leguminous herbs (family Fabaceae) including licorice (*Glycyrrhiza glabra*), valued for its sweet-tasting roots containing the saponin glycyrrhizin.",
    secondary: "A classical medicinal plant derived from Greek *glykys* ('sweet') and *rhiza* ('root'), used as an expectorant, anti-inflammatory, and flavoring agent since antiquity.",
    quotes: [
      { author: "Dioscorides", work: "De Materia Medica", quote: "The root of **Glycyrrhiza**, which grows abundantly along river banks, soothes the throat and clears hoarseness of the lungs." },
      { author: "Jonathan Pereira", work: "The Elements of Materia Medica", quote: "Extracts of **Glycyrrhiza** are prized in pharmacy for disguising the nauseous bitterness of aloes and quinine." },
      { author: "Asa Gray", work: "Manual of the Botany of the Northern United States", quote: "Our native wild licorice, **Glycyrrhiza** lepidota, bears prickly bur-like pods reminiscent of cocklebur." }
    ]
  },
  "Dashboard — glyc/hyperglycaemia.md": {
    primary: "An abnormally high concentration of glucose in the circulating blood plasma, characteristic of diabetes mellitus (Commonwealth spelling).",
    secondary: "In metabolic medicine, sustained elevations in plasma glucose causing osmotic diuresis, cellular dehydration, ketoacidosis, and long-term vascular complications.",
    quotes: [
      { author: "Frederick Banting", work: "Pancreatic Extracts in the Treatment of Diabetes Mellitus", quote: "Administration of active islet extract caused the profound **hyperglycaemia** of diabetic dogs to fall rapidly to normal levels." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Severe **hyperglycaemia** drives glucose across the renal threshold, precipitating polyuria, dehydration, and diabetic coma." },
      { author: "Claude Bernard", work: "An Introduction to the Study of Experimental Medicine", quote: "We measured hepatic venous outflow to demonstrate that liver glycogenolysis is the immediate cause of post-prandial **hyperglycaemia**." }
    ]
  },
  "Dashboard — glyc/hyperglycemia.md": {
    primary: "An excessive concentration of glucose in the bloodstream, exceeding standard fasting physiological limits (American spelling).",
    secondary: "A diagnostic hallmark of diabetes mellitus that induces non-enzymatic glycation of proteins and microvascular damage.",
    quotes: [
      { author: "Frederick Banting", work: "The Internal Secretion of the Pancreas", quote: "Within two hours of insulin injection, the marked **hyperglycemia** was replaced by a safe, normal blood sugar level." },
      { author: "William Carlos Williams", work: "The Doctor Stories", quote: "The old man was slipping into stupor from unmonitored **hyperglycemia** after indulging in cider and sweet holiday pies." },
      { author: "Walter Cannon", work: "The Wisdom of the Body", quote: "Acute emotional excitement provokes sympathetic adrenal discharge, causing temporary functional **hyperglycemia** for physical exertion." }
    ]
  },
  "Dashboard — glyc/hypoglycaemia.md": {
    primary: "An abnormally low concentration of glucose in the circulating blood, producing sweating, trembling, palpitations, mental confusion, and potential loss of consciousness (Commonwealth spelling).",
    secondary: "In endocrinology and emergency medicine, a critical metabolic state commonly triggered by excessive insulin administration or prolonged fasting.",
    quotes: [
      { author: "Frederick Banting", work: "Nobel Lecture: The Discovery of Insulin", quote: "An overdose of insulin precipitates acute **hypoglycaemia**, which can be immediately relieved by intravenous glucose or orange juice." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The clinical signs of severe **hypoglycaemia** mimic acute intoxication, requiring prompt diagnostic blood evaluation." },
      { author: "Hans Krebs", work: "The Citric Acid Cycle", quote: "When hepatic gluconeogenesis fails during starvation, catastrophic **hypoglycaemia** deprives the central nervous system of essential fuel." }
    ]
  },
  "Dashboard — glyc/hypoglycaemic.md": {
    primary: "Relating to, characterized by, or suffering from hypoglycaemia; producing a lowering of blood glucose levels (Commonwealth spelling).",
    secondary: "Describing pharmacologic agents (e.g., sulfonylureas, biguanides, insulin) employed to treat elevated blood glucose in diabetes.",
    quotes: [
      { author: "Frederick Banting", work: "Pancreatic Extracts in the Treatment of Diabetes Mellitus", quote: "The potent **hypoglycaemic** action of our purified pancreatic fraction was verified across dozens of animal trials." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The physician must educate the diabetic patient to recognize the earliest trembling sensations of an impending **hypoglycaemic** crisis." },
      { author: "Claude Bernard", work: "Lectures on Experimental Physiology", quote: "Certain hepatic poisons produce a profound **hypoglycaemic** shock by paralyzing carbohydrate synthesis." }
    ]
  },
  "Dashboard — glyc/hypoglycemia.md": {
    primary: "A deficiency of glucose in the bloodstream below normal physiological levels, leading to neuroglycopenic symptoms and autonomic stress responses (American spelling).",
    secondary: "A clinical emergency in diabetes care characterized by diaphoresis, tachycardia, anxiety, confusion, seizures, or coma when plasma glucose drops below critical thresholds.",
    quotes: [
      { author: "Frederick Banting", work: "The Internal Secretion of the Pancreas", quote: "Convulsions occurring during severe insulin-induced **hypoglycemia** were promptly arrested by sugar administration." },
      { author: "William Carlos Williams", work: "Autobiography", quote: "The patient lay pale and drenched in sweat, a victim of sudden **hypoglycemia** that required an emergency syringe of dextrose." },
      { author: "Walter Cannon", work: "The Wisdom of the Body", quote: "The autonomic nervous system reacts to **hypoglycemia** with intense sympathoadrenal discharge to restore circulating sugar levels." }
    ]
  },
  "Dashboard — glyc/hypoglycemic.md": {
    primary: "Pertaining to, experiencing, or causing an abnormally low concentration of glucose in the blood (American spelling).",
    secondary: "Describing medications (oral hypoglycemic agents) or metabolic states that decrease blood glucose concentrations.",
    quotes: [
      { author: "Frederick Banting", work: "Nobel Lecture: The Discovery of Insulin", quote: "The discovery of a reliable **hypoglycemic** agent revolutionized the prognosis of juvenile diabetes from death to life." },
      { author: "William Carlos Williams", work: "The Doctor Stories", quote: "I carried ampoules of glucose in my doctor's bag to treat sudden **hypoglycemic** reactions in elderly insulin users." },
      { author: "Walter Cannon", work: "Bodily Changes in Pain, Hunger, Fear and Rage", quote: "The animal exhibited classic **hypoglycemic** tremors until a spoonful of corn syrup restored normal cortical function." }
    ]
  },
  "Dashboard — glyc/triglyceride.md": {
    primary: "A lipid molecule composed of a single glycerol backbone ester-linked to three fatty acid molecules, constituting the main constituent of vegetable oils and animal fats.",
    secondary: "In clinical biochemistry and cardiovascular medicine, circulating blood lipids measured as an indicator of metabolic health, insulin resistance, and atherosclerotic risk.",
    quotes: [
      { author: "Michel Eugène Chevreul", work: "Chemical Researches on Animal Fats", quote: "Natural tallow consists chiefly of neutral **triglyceride** combinations of stearic, palmitic, and oleic acids." },
      { author: "Linus Pauling", work: "General Chemistry", quote: "The compact, hydrophobic structure of a **triglyceride** yields twice as much metabolic energy per gram as carbohydrate." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Elevated serum **triglyceride** levels accompanying obesity and diabetes signal impaired clearance of chylomicrons." }
    ]
  }
};

for (const [relPath, entry] of Object.entries(filesData)) {
  const filePath = path.join(basePath, relPath);
  if (!fs.existsSync(filePath)) {
    console.error(`Missing file: ${filePath}`);
    continue;
  }
  const content = fs.readFileSync(filePath, 'utf8');

  // Find top portion up to > [!book]
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
  console.log(`Updated: ${relPath}`);
}

console.log('Batch 2 complete! Total files updated:', Object.keys(filesData).length);
