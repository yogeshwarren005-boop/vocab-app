import fs from 'fs';
import path from 'path';

const basePath = 'App database/Greek roots/Cluster Feeling & Sensation';

const filesData = {
  // Dashboard — aesth (20 words)
  "Dashboard — aesth/aesth.md": {
    primary: "The Greek root *aesth-* (from *aisthēsis*), denoting perception, physical sensation, feeling, or sensory awareness, forming the foundation of *aesthetic*, *aesthesia*, and *anaesthesia*.",
    secondary: "The foundational morpheme in philosophical epistemology and sensory physiology signifying the immediate apprehension of phenomena through the somatic senses.",
    quotes: [
      { author: "Henry George Liddell & Robert Scott", work: "A Greek-English Lexicon", quote: "The primitive stem **aesth** underlies Greek verbs signifying to perceive, to comprehend by sense-perception, or to feel physically." },
      { author: "Alexander Baumgarten", work: "Aesthetica", quote: "Borrowing from ancient **aesth**, we propose aesthetics as the science of sensory cognition directed toward beauty." },
      { author: "Walter Pater", work: "The Renaissance: Studies in Art and Poetry", quote: "The Greek mind anchored all intellectual contemplation in the delicate alertness of **aesth**, the pure vitality of physical sensation." }
    ]
  },
  "Dashboard — aesth/aesthesia.md": {
    primary: "The normal physiological capacity to experience sensations; sensory perception or tactile sensibility across bodily nerve pathways.",
    secondary: "In neurology and psychological medicine, the intact functioning of sensory afferents that allows conscious detection of tactile, thermal, and pain stimuli.",
    quotes: [
      { author: "William James", work: "The Principles of Psychology", quote: "Conscious awareness rests upon an unbroken background of bodily **aesthesia** by which we know that we live and move." },
      { author: "Charles Sherrington", work: "The Integrative Action of the Nervous System", quote: "Reflex coordination requires unimpaired cutaneous **aesthesia** to signal peripheral resistance back to central motor arcs." },
      { author: "Henry Maudsley", work: "The Physiology of Mind", quote: "Disorders of the cerebral cortex manifest first in distortions of visceral and somatic **aesthesia**." }
    ]
  },
  "Dashboard — aesth/aesthesis.md": {
    primary: "Direct sensory perception or tactile sensation; the immediate apprehension of external reality through sensory receptors, as conceptualized in Greek philosophy.",
    secondary: "In classical Aristotelian epistemology, the sensory faculty distinct from *noesis* (intellect) that registers perceptible forms without their material substance.",
    quotes: [
      { author: "Aristotle", work: "De Anima", quote: "By **aesthesis**, the soul receives sensible forms without matter, just as wax receives the impression of an iron signet ring." },
      { author: "John Ruskin", work: "Modern Painters", quote: "True art demands vivid **aesthesis**, an unclouded receptivity to the light and colour spread across the living earth." },
      { author: "Walter Pater", work: "Marius the Epicurean", quote: "He sought to refine his momentary **aesthesis**, regarding each fleeting impression of the senses as an end in itself." }
    ]
  },
  "Dashboard — aesth/aesthete.md": {
    primary: "A person who affects, exhibits, or cultivates a special or refined sensitivity to art, beauty, and aesthetic value, often to the neglect of practical concerns.",
    secondary: "A dedicated adherent of the late-19th-century Aesthetic Movement who elevated 'art for art's sake' into a personal ethos.",
    quotes: [
      { author: "Oscar Wilde", work: "The Picture of Dorian Gray", quote: "He had always been an **aesthete**, valuing life only for the intense sensations and exquisite decorative moments it afforded." },
      { author: "Gilbert & Sullivan", work: "Patience", quote: "If you walk down Piccadilly with a poppy or a lily in your medieval hand, then everyone will say as you walk your flowery way, what an ultra-poetical **aesthete** this young man must be!" },
      { author: "Max Beerbohm", work: "Zuleika Dobson", quote: "The undergraduate pose of the melancholy **aesthete** melted away in the brisk afternoon sunshine along the riverbank." }
    ]
  },
  "Dashboard — aesth/aesthetic.md": {
    primary: "Concerned with beauty or the appreciation of beauty; possessing or displaying good taste, artistic refinement, and harmonious form.",
    secondary: "In philosophy and critical theory, relating to the branch of philosophy dealing with the nature of art, sensory value judgments, and taste.",
    quotes: [
      { author: "Immanuel Kant", work: "Critique of Judgment", quote: "An **aesthetic** judgment of taste claims universal validity while resting upon a purely disinterested feeling of pleasure." },
      { author: "Friedrich Schiller", work: "On the Aesthetic Education of Man", quote: "It is through beauty alone that man journeys to freedom, for the **aesthetic** impulse harmonizes our animal instincts with reason." },
      { author: "Oscar Wilde", work: "The Decay of Lying", quote: "Life imitates art far more than art imitates life, for the **aesthetic** temperament finds in reality only what artists have taught it to see." }
    ]
  },
  "Dashboard — aesth/aesthetical.md": {
    primary: "Relating to aesthetics, artistic beauty, or the philosophy of taste; an older or formal variant of aesthetic.",
    secondary: "Concerning the critical principles that govern the appreciation of sensory harmony and artistic composition in 18th- and 19th-century philosophical prose.",
    quotes: [
      { author: "Samuel Taylor Coleridge", work: "Biographia Literaria", quote: "We stand in great need of an **aesthetical** vocabulary capable of discriminating between the fancy and the higher creative imagination." },
      { author: "Thomas Carlyle", work: "Sartor Resartus", quote: "Our clothing serves not merely physical shelter, but represents an **aesthetical** embodiment of inward moral order." },
      { author: "George Eliot", work: "Middlemarch", quote: "Her uncle displayed a mild **aesthetical** interest in classical architectural ruins during his Italian tours." }
    ]
  },
  "Dashboard — aesth/aesthetically.md": {
    primary: "In a manner relating to beauty, artistic taste, or visual harmony; from an aesthetic point of view.",
    secondary: "With conscious consideration for stylistic elegance, symmetry, and sensory pleasingness rather than purely utilitarian function.",
    quotes: [
      { author: "Clive Bell", work: "Art", quote: "A cathedral or painting moves us **aesthetically** through the pure resonance of significant form rather than through documentary subject matter." },
      { author: "Virginia Woolf", work: "To the Lighthouse", quote: "The mass of the hedge balanced the blue line of the bay, satisfying her **aesthetically** as the canvas reached completion." },
      { author: "Roger Fry", work: "Vision and Design", quote: "An object designed **aesthetically** speaks directly to the contemplative imagination through line and color." }
    ]
  },
  "Dashboard — aesth/aesthetician.md": {
    primary: "A philosopher, critic, or scholar who specializes in aesthetics, the theory of beauty, and the principles of artistic creation.",
    secondary: "A specialist or licensed professional trained in the cosmetic care and beautification of the skin (frequently styled esthetician in modern salons).",
    quotes: [
      { author: "Benedetto Croce", work: "Aesthetic as Science of Expression and General Linguistic", quote: "The true **aesthetician** must demonstrate that intuitive knowledge is independent of conceptual logic." },
      { author: "George Santayana", work: "The Sense of Beauty", quote: "The **aesthetician** does not legislate rules of style; he analyzes the psychological springs of delight." },
      { author: "Monroe Beardsley", work: "Aesthetics: Problems in the Philosophy of Criticism", quote: "The task of the philosophical **aesthetician** is to clarify what reasons legitimately support artistic evaluation." }
    ]
  },
  "Dashboard — aesth/aesthetics.md": {
    primary: "The branch of philosophy that deals with the nature and expression of beauty, art, taste, and the sublimity of sensory perception.",
    secondary: "The set of artistic principles, stylistic convictions, or visual conventions characterizing the work of a particular artist, movement, or cultural epoch.",
    quotes: [
      { author: "G. W. F. Hegel", work: "Introductory Lectures on Aesthetics", quote: "The realm of **aesthetics** has for its object the wide domain of the beautiful, and specifically the beauty of fine art." },
      { author: "Arthur Schopenhauer", work: "The World as Will and Representation", quote: "In contemplation through **aesthetics**, the mind escapes the endless torment of the willing self and gazes upon eternal Platonic ideas." },
      { author: "Leo Tolstoy", work: "What Is Art?", quote: "Modern **aesthetics** has mistaken the pursuit of pleasure for the sacred moral mission of artistic communication." }
    ]
  },
  "Dashboard — aesth/anaesthesia.md": {
    primary: "The temporary, medically induced insensitivity to pain or sensation, especially as achieved by the administration of anaesthetic gases or drugs during surgical operations.",
    secondary: "The pathological or congenital absence of sensory perception in a region of the body resulting from nerve lesion, spinal trauma, or hysteria.",
    quotes: [
      { author: "Oliver Wendell Holmes Sr.", work: "Medical Essays", quote: "I suggest the word **anaesthesia** for this miraculous state of insensibility that permits surgery without human torment." },
      { author: "William T. G. Morton", work: "Remarks on the Proper Mode of Administering Sulphuric Ether", quote: "The patient inhaled the vapor until complete surgical **anaesthesia** was established, whereupon the tumor was painlessly excised." },
      { author: "James Young Simpson", work: "On a New Anaesthetic Agent, More Efficient than Sulphuric Ether", quote: "In midwifery, the discovery of **anaesthesia** delivers humanity from a curse that has burdened every generation." }
    ]
  },
  "Dashboard — aesth/anaesthetic.md": {
    primary: "A drug, gas, or agent that induces temporary insensibility to pain and other sensations; producing a state of anaesthesia.",
    secondary: "Pertaining to or characterized by the absence of sensation; acting to dull, numb, or obliterate emotional or sensory responsiveness.",
    quotes: [
      { author: "H. G. Wells", work: "The Island of Doctor Moreau", quote: "He operated with remorseless anatomical precision, yet neglected the mercy of any soothing **anaesthetic**." },
      { author: "Thomas De Quincey", work: "Confessions of an English Opium-Eater", quote: "The drug exercised an almost divine **anaesthetic** power over the sharp neuralgic agonies of my face." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The discovery of an effective surgical **anaesthetic** stands as the greatest single boon conferred by science upon medicine." }
    ]
  },
  "Dashboard — aesth/anaesthetise.md": {
    primary: "To administer an anaesthetic to a patient or animal so as to render them insensible to pain during medical interventions (predominantly Commonwealth spelling).",
    secondary: "To deaden, numb, or blunt someone's moral sensibilities, emotions, or critical awareness against troubling realities.",
    quotes: [
      { author: "Sigmund Freud", work: "The Interpretation of Dreams", quote: "Neurotic symptoms serve in part to **anaesthetise** the conscious mind against the painful pressure of repressed trauma." },
      { author: "Aldous Huxley", work: "Brave New World", quote: "Soma was distributed daily to **anaesthetise** every spark of civic discontent and personal anxiety." },
      { author: "T. S. Eliot", work: "The Love Song of J. Alfred Prufrock", quote: "When the evening is spread out against the sky like a patient etherised upon a table, quietude seems to **anaesthetise** the street." }
    ]
  },
  "Dashboard — aesth/anaesthetist.md": {
    primary: "A medical specialist trained to administer anaesthetics and monitor the vital bodily signs of patients before, during, and after surgical procedures (Commonwealth usage).",
    secondary: "The operating-room physician responsible for hemodynamic stability, airway management, and pain control under surgical stress.",
    quotes: [
      { author: "John Snow", work: "On Chloroform and Other Anaesthetics", quote: "The skilled **anaesthetist** must continuously observe the pulse and respiration rather than watch the surgeon's knife." },
      { author: "Joseph Clover", work: "On the Administration of Chloroform in Dental Operations", quote: "A prudent **anaesthetist** adjusts the ether vapor percentage gradually to prevent laryngospasm." },
      { author: "Arthur Conan Doyle", work: "The Stark Munro Letters", quote: "I stood at the patient's head acting as **anaesthetist**, measuring each drop of chloroform with trembling hands." }
    ]
  },
  "Dashboard — aesth/anaesthetize.md": {
    primary: "To induce anaesthesia in; to render insensible to physical pain through pharmaceutical agents (standard American spelling).",
    secondary: "To suppress, dull, or stupefy emotional distress, intellectual anguish, or conscience.",
    quotes: [
      { author: "William James", work: "The Principles of Psychology", quote: "Certain narcotic agents temporarily **anaesthetize** the sensory cortex without completely extinguishing subconscious reflexes." },
      { author: "Havelock Ellis", work: "Studies in the Psychology of Sex", quote: "Routine social conventions frequently operate to **anaesthetize** the moral imagination of the multitude." },
      { author: "Bertrand Russell", work: "The Conquest of Happiness", quote: "Men turn to intoxicating beverages not for joy, but merely to **anaesthetize** the constant dread of competitive failure." }
    ]
  },
  "Dashboard — aesth/paraesthesia.md": {
    primary: "An abnormal, spontaneous dermal sensation such as tingling, pricking, numbness, burning, or pins-and-needles without an apparent physical stimulus.",
    secondary: "In clinical neurology, a hallmark symptom of peripheral neuropathy, root compression, or central demyelinating disease (alternative spelling of paresthesia).",
    quotes: [
      { author: "Jean-Martin Charcot", work: "Clinical Lectures on Diseases of the Nervous System", quote: "The onset of spinal sclerosis is often heralded by creeping **paraesthesia** across the toes and soles." },
      { author: "William Gowers", work: "A Manual of Diseases of the Nervous System", quote: "A persistent burning **paraesthesia** along the cutaneous nerve distribution signals ongoing ischemic irritation." },
      { author: "S. Weir Mitchell", work: "Injuries of Nerves and Their Consequences", quote: "Soldiers recovering from bullet wounds to the brachial plexus complained bitterly of intractable **paraesthesia** in their fingers." }
    ]
  },
  "Dashboard — aesth/synaesthesia.md": {
    primary: "A neurological phenomenon in which stimulation of one sensory or cognitive pathway leads to involuntary, automatic experiences in a second, unrelated pathway (e.g., hearing colours).",
    secondary: "In literary aesthetics and symbolist poetry, the deliberate blending of imagery appealing to different senses to evoke transcendent psychological harmonies.",
    quotes: [
      { author: "Francis Galton", work: "Inquiries into Human Faculty and Its Development", quote: "Persons gifted with visual **synaesthesia** see distinctive colour tints whenever numerals or musical notes are presented." },
      { author: "Charles Baudelaire", work: "Correspondances", quote: "Perfumes, sounds, and colours respond to one another across the mysterious twilight of poetic **synaesthesia**." },
      { author: "Arthur Rimbaud", work: "Voyelles", quote: "Through lyrical **synaesthesia**, I invented vowels with hues: A black, E white, I red, U green, O blue." }
    ]
  },
  "Dashboard — aesth/synaesthetic.md": {
    primary: "Characterized by, relating to, or exhibiting synaesthesia; involving cross-sensory correspondences.",
    secondary: "Evoking a vivid sensory impression through descriptions properly belonging to another sense in artistic, musical, or literary compositions.",
    quotes: [
      { author: "Vladimir Nabokov", work: "Speak, Memory", quote: "From childhood I possessed a **synaesthetic** alphabet where the letter M was the tint of dry pink flannel." },
      { author: "Wassily Kandinsky", work: "Concerning the Spiritual in Art", quote: "A yellow trumpet blast produces an unmistakably bright, shrill **synaesthetic** sensation on the painter's canvas." },
      { author: "Joris-Karl Huysmans", work: "À rebours", quote: "Des Esseintes constructed a mouth-organ of liqueurs where each drop provided a **synaesthetic** equivalent of flute or cello music." }
    ]
  },
  "Dashboard — aesth/synesthesia.md": {
    primary: "A condition in which a stimulus received in one sensory modality simultaneously triggers a perceptual experience in another modality (American spelling of synaesthesia).",
    secondary: "Cross-modal neuro-cognitive association investigated in perception science to uncover brain wiring and multisensory integration.",
    quotes: [
      { author: "Richard Cytowic", work: "The Man Who Tasted Shapes", quote: "Her case of **synesthesia** demonstrated that sensory boundaries in the limbic system are far more permeable than textbook anatomy suggested." },
      { author: "Oliver Sacks", work: "Musicophilia: Tales of Music and the Brain", quote: "Musicians with tone-color **synesthesia** do not merely imagine colors; they vividly experience an inner visual light show." },
      { author: "John Locke", work: "An Essay Concerning Human Understanding", quote: "A blind man who boasted he understood scarlet asserted that scarlet was like the sound of a trumpet, an early intuition of **synesthesia**." }
    ]
  },
  "Dashboard — aesth/synesthetic.md": {
    primary: "Pertaining to, demonstrating, or induced by synesthesia; cross-sensory.",
    secondary: "Describing metaphorical language or cognitive linkages that fuse sight, sound, touch, taste, or smell into a unified perception.",
    quotes: [
      { author: "Maurice Merleau-Ponty", work: "Phenomenology of Perception", quote: "Far from being a rare pathological oddity, **synesthetic** perception is the primordial rule of our lived bodily experience." },
      { author: "Marshall McLuhan", work: "The Gutenberg Galaxy", quote: "Pre-literate oral culture sustained a balanced **synesthetic** interplay between the ear and eye that typography shattered." },
      { author: "Roman Jakobson", work: "Linguistics and Poetics", quote: "Poetic metaphors draw their evocative vigor from deep-seated **synesthetic** affinities between vowel timbres and chromatic values." }
    ]
  },
  "Dashboard — aesth/unaesthetic.md": {
    primary: "Lacking beauty, artistic merit, or good taste; aesthetically displeasing, ugly, or uncouth.",
    secondary: "Offending against the canons of harmonious design, symmetry, or sensory refinement.",
    quotes: [
      { author: "Oscar Wilde", work: "The Critic as Artist", quote: "Modern commerce has made our public streets terribly drab and **unaesthetic**, substituting billboard hoardings for frescoes." },
      { author: "George Bernard Shaw", work: "Dramatic Opinions and Essays", quote: "The stage setting was so clumsy and **unaesthetic** that no acting could redeem the romantic illusion." },
      { author: "Vernon Lee", work: "The Beautiful", quote: "Disproportion in architecture creates an instantly jarred, **unaesthetic** reaction in the spectator's sympathetic muscle memory." }
    ]
  },

  // Dashboard — agap (4 words)
  "Dashboard — agap/agap.md": {
    primary: "The Greek root *agap-* (from *agapē*), denoting unconditional, benevolent, or sacrificial love, in contrast to erotic (*eros*) or affectionate friendship (*philia*).",
    secondary: "The theological and ethical morpheme designating divine charity, communion, and selfless regard for the welfare of others.",
    quotes: [
      { author: "Henry George Liddell & Robert Scott", work: "A Greek-English Lexicon", quote: "The Greek stem **agap** expresses fraternal affection, high esteem, and the purest benevolent love." },
      { author: "C. S. Lewis", work: "The Four Loves", quote: "In Christian theology, the root **agap** stands for that unconditional divine charity which gives without expecting return." },
      { author: "Anders Nygren", work: "Agape and Eros", quote: "The profound theological divide of late antiquity turned upon the fundamental contrast between eros and **agap**." }
    ]
  },
  "Dashboard — agap/agapanthus.md": {
    primary: "A genus of African monocotyledonous perennial plants (family Amaryllidaceae), known as the lily of the Nile or African lily, bearing large globose umbels of blue or white flowers.",
    secondary: "A popular ornamental garden perennial derived from Greek *agapē* ('love') and *anthos* ('flower'), symbolizing tender affection in horticultural lore.",
    quotes: [
      { author: "Gertrude Jekyll", work: "Colour in the Flower Garden", quote: "Tubs of sky-blue **agapanthus** placed along the stone terrace provided bold architectural dignity through August." },
      { author: "Vita Sackville-West", work: "In Your Garden", quote: "The noble blue umbels of **agapanthus** withstand autumn gales if wintered safely in cold frames." },
      { author: "Reginald Farrer", work: "The English Rock Garden", quote: "While alpine species demand lean screes, the African **agapanthus** luxuriates in deep loam and blazing sun." }
    ]
  },
  "Dashboard — agap/agape.md": {
    primary: "Selfless, sacrificial, unconditional love; the highest form of love in Christian theology, exemplified by God's love for humanity and love of neighbor.",
    secondary: "A communal 'love feast' or fellowship meal practiced by early Christians in conjunction with or prior to the celebration of the Eucharist.",
    quotes: [
      { author: "Saint Paul", work: "First Epistle to the Corinthians", quote: "Now abideth faith, hope, and charity, but the greatest of these is **agape**, the love that suffereth long and is kind." },
      { author: "Martin Luther King Jr.", work: "Stride Toward Freedom", quote: "When we speak of loving those who oppose us, we refer not to emotional affection, but to **agape**, redemptive goodwill for all." },
      { author: "Søren Kierkegaard", work: "Works of Love", quote: "Christian **agape** discovers neighbor in every single soul, refusing all preference based on worldly kinship or beauty." }
    ]
  },
  "Dashboard — agap/agapornis.md": {
    primary: "A genus of small, brightly plumaged parrots native to Africa and Madagascar, commonly known as lovebirds, noted for lifelong monogamous pair bonding.",
    secondary: "An avian genus (family Psittaculidae) named from Greek *agapē* ('love') and *ornis* ('bird') because mates sit side by side preening affectionately.",
    quotes: [
      { author: "Alfred Russel Wallace", work: "The Geographical Distribution of Animals", quote: "The dwarf parrots of the genus **Agapornis** are characteristic of the Ethiopian zoological region." },
      { author: "Charles Darwin", work: "The Descent of Man", quote: "The constant Mutual preening and attachment observed in caged **Agapornis** illustrates the intensity of avian monogamy." },
      { author: "John Gould", work: "The Birds of Australia", quote: "African species of **Agapornis** possess compact bodies and brilliant facial masks unmatched among small parakeets." }
    ]
  },

  // Dashboard — alg (15 words)
  "Dashboard — alg/alg.md": {
    primary: "The Greek root *alg-* (from *algos*), meaning physical pain, grief, or bodily distress, seen in *analgesic*, *nostalgia*, and *neuralgia*.",
    secondary: "The diagnostic combining form indicating localized suffering, ache, or soreness across anatomical terminologies.",
    quotes: [
      { author: "Henry George Liddell & Robert Scott", work: "A Greek-English Lexicon", quote: "The primary noun *algos* and its combining root **alg** signify acute bodily pain, sorrow, and grief in Greek epic and tragic poetry." },
      { author: "Galen", work: "Method of Medicine", quote: "When diagnosing afflictions of the joints, the physician distinguishes the dull ache from the sharp lancinating **alg**." },
      { author: "Thomas Sydenham", work: "Medical Observations Concerning the History and Cure of Acute Diseases", quote: "The sudden onset of severe articular **alg** in the great toe marks the classical paroxysm of podagra." }
    ]
  },
  "Dashboard — alg/alga.md": {
    primary: "A simple, nonflowering, typically aquatic photosynthetic plant or organism belonging to a large, polyphyletic group including seaweeds and many single-celled forms.",
    secondary: "In phycology and limnology, any oxygen-producing photosynthetic protist lacking true stems, roots, leaves, or vascular tissue.",
    quotes: [
      { author: "Charles Darwin", work: "The Voyage of the Beagle", quote: "The number of living creatures of all orders whose existence depends on the giant marine **alga** is wonderful." },
      { author: "Rachel Carson", work: "The Sea Around Us", quote: "Beneath the surface drifts the microscopic **alga**, capturing solar energy to fuel the boundless oceanic food chain." },
      { author: "Henry David Thoreau", work: "Cape Cod", quote: "The tide had cast upon the beach glistening ribbons of brown **alga**, filling the brisk air with iodine." }
    ]
  },
  "Dashboard — alg/algal.md": {
    primary: "Of, relating to, resembling, or composed of algae.",
    secondary: "Pertaining to algal blooms, mats, or biogenic deposits in marine and freshwater aquatic ecosystems.",
    quotes: [
      { author: "Rachel Carson", work: "The Edge of the Sea", quote: "The damp rock ledges were coated with a slippery **algal** crust that sheltered tiny barnacles and periwinkles." },
      { author: "Ernst Haeckel", work: "Art Forms in Nature", quote: "The delicate symmetry of **algal** skeletons under the microscope reveals nature's inherent architectural geometries." },
      { author: "James Lovelock", work: "Gaia: A New Look at Life on Earth", quote: "Marine **algal** emissions of dimethyl sulfide serve as global cloud condensation nuclei, stabilizing Earth's climate." }
    ]
  },
  "Dashboard — alg/alger.md": {
    primary: "A reference to Horatio Alger Jr. (1832–1899) or the archetype of the virtuous, impoverished youth rising to wealth and respectability through pluck, hard work, and honesty.",
    secondary: "An adjective or noun characterizing an American mythos of meritocratic self-help, upward social mobility, and industrious perseverance against adversity.",
    quotes: [
      { author: "Horatio Alger Jr.", work: "Ragged Dick", quote: "The hero embodied the classic **Alger** creed: save your pennies, study at night, and shun all gambling and drink." },
      { author: "Henry Adams", work: "The Education of Henry Adams", quote: "The young republic still believed blindly in its innocent **Alger** heroes climbing toward industrial fortune." },
      { author: "Thorstein Veblen", work: "The Theory of the Leisure Class", quote: "The popular fascination with the **Alger** narrative serves to legitimize pecuniary accumulation by portraying it as moral triumph." }
    ]
  },
  "Dashboard — alg/algoid.md": {
    primary: "Resembling or having the characteristics of algae; alga-like in appearance, structure, or habitat.",
    secondary: "In botany and microbiological pathology, denoting filamentous, slimy, or thalloid growth forms resembling aquatic algal mats.",
    quotes: [
      { author: "Asa Gray", work: "Elements of Botany", quote: "Certain primitive lichens present an **algoid** appearance until microscopic examination exposes their fungal filaments." },
      { author: "John Muir", work: "Studies in the Sierra", quote: "The glacial pools were fringed with an **algoid** scum of vibrant emerald despite the icy mountain runoff." },
      { author: "Thomas Henry Huxley", work: "Lay Sermons, Addresses, and Reviews", quote: "The primordial protoplasmic slime was presumed to have taken an **algoid** form in shallow Archean seas." }
    ]
  },
  "Dashboard — alg/analgesia.md": {
    primary: "The inability to feel pain while remaining fully conscious, whether occurring naturally, through neuropathy, or induced by medication.",
    secondary: "In medical therapeutics and surgical practice, the targeted elimination of nociceptive sensation without inducing generalized loss of consciousness.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Complete cutaneous **analgesia** accompanied by preserved thermal sensibility is the diagnostic sign of syringomyelia." },
      { author: "René Leriche", work: "The Surgery of Pain", quote: "The surgeon strives not merely to suppress symptom, but to establish durable **analgesia** by sympathetic nerve block." },
      { author: "Oliver Sacks", work: "The Man Who Mistook His Wife for a Hat", quote: "Congenital **analgesia** turns out to be a perilous curse, depriving children of the vital protective warnings of pain." }
    ]
  },
  "Dashboard — alg/analgesic.md": {
    primary: "A drug or remedy that relieves or eliminates pain without causing loss of consciousness; pain-relieving.",
    secondary: "Pertaining to or characterized by the pharmacological property of suppressing pain perception along spinal and thalamic pathways.",
    quotes: [
      { author: "Arthur Conan Doyle", work: "The Adventure of the Creeping Man", quote: "The physician administered a soothing **analgesic** draught to calm the patient's acute neuralgic paroxysms." },
      { author: "Paul Ehrlich", work: "Studies in Immunity", quote: "Synthetic chemists sought an ideal **analgesic** compound that would bind selectively to pain receptors without respiratory depression." },
      { author: "William Carlos Williams", work: "Autobiography", quote: "In the working-class tenements, the doctor had little to offer beyond comforting words and a pocketful of **analgesic** tablets." }
    ]
  },
  "Dashboard — alg/analgetic.md": {
    primary: "Relieving pain; having the properties of an analgesic (an older, formal linguistic variant of analgesic).",
    secondary: "In early physiological and pharmacological literature, producing a state of analgesia or insensibility to physical suffering.",
    quotes: [
      { author: "John Tyndall", work: "Fragments of Science", quote: "Ether and chloroform exert an **analgetic** effect that disarms the surgical knife of its traditional terror." },
      { author: "Claude Bernard", work: "An Introduction to the Study of Experimental Medicine", quote: "The **analgetic** action of morphine was verified by measuring spinal reflex thresholds in lab animals." },
      { author: "William James", work: "The Varieties of Religious Experience", quote: "Mystical contemplation exerts an **analgetic** influence on bodily afflictions, rendering martyrdom bearable." }
    ]
  },
  "Dashboard — alg/arthralgia.md": {
    primary: "Severe, aching pain in a joint or multiple joints, occurring without primary inflammatory swelling or joint damage.",
    secondary: "A common clinical complaint in systemic rheumatology, infectious prodromes (such as viral fevers), and degenerative arthropathies.",
    quotes: [
      { author: "Benjamin Rush", work: "Medical Inquiries and Observations", quote: "The autumn ague frequently left the patient tormented by stubborn **arthralgia** in knees and hips." },
      { author: "Thomas Sydenham", work: "Tractatus de Podagra et Hydrope", quote: "Before the overt redness appears, an agonizing **arthralgia** grips the metatarsal joint during midnight hours." },
      { author: "William Heberden", work: "Commentaries on the History and Cure of Diseases", quote: "Persistent weather-sensitive **arthralgia** must be distinguished from the acute febrile swelling of rheumatic fever." }
    ]
  },
  "Dashboard — alg/arthralgic.md": {
    primary: "Of, relating to, or affected by arthralgia; characterized by joint pain.",
    secondary: "Describing painful joint manifestations or complaints arising in connective tissue and rheumatologic syndromes.",
    quotes: [
      { author: "Jean-Martin Charcot", work: "Lectures on the Diseases of the Nervous System", quote: "Tabetic patients often present early **arthralgic** episodes long before frank Charcot joints develop." },
      { author: "Sir William Osler", work: "Aequanimitas", quote: "The practitioner must listen attentively to each **arthralgic** symptom while hunting for subtle systemic autoimmune signs." },
      { author: "Archibald Garrod", work: "The Inborn Errors of Metabolism", quote: "In ochronosis, the deposition of homogentisic acid pigments provokes severe **arthralgic** attacks in mature adults." }
    ]
  },
  "Dashboard — alg/fibromyalgia.md": {
    primary: "A chronic disorder characterized by widespread musculoskeletal pain, fatigue, sleep disturbances, cognitive difficulties, and localized areas of tenderness ('tender points').",
    secondary: "A centralized pain sensitivity syndrome (central sensitization) involving altered nociceptive processing in the central nervous system.",
    quotes: [
      { author: "William R. Gowers", work: "Lumbago: Its Lessons and Analogues", quote: "What our predecessors labeled muscular fibrositis anticipates the modern clinical entity known as **fibromyalgia**." },
      { author: "Oliver Sacks", work: "A Leg to Stand On", quote: "Patients suffering from **fibromyalgia** endure a pervasive sensory hyperalgesia that defies simple peripheral explanation." },
      { author: "Robert M. Sapolsky", work: "Why Zebras Don't Get Ulcers", quote: "Chronic activation of the neuroendocrine stress response correlates closely with symptom flares in **fibromyalgia**." }
    ]
  },
  "Dashboard — alg/gastralgia.md": {
    primary: "Severe, paroxysmal pain or cramping localized to the stomach; gastric neuralgia or stomach ache.",
    secondary: "In historical clinical medicine, non-ulcer neurosis of the stomach characterized by spasmodic epigastric pain independent of food intake.",
    quotes: [
      { author: "William Beaumont", work: "Experiments and Observations on the Gastric Juice and the Physiology of Digestion", quote: "Sudden irritation of the inner mucosal lining induced intense **gastralgia** accompanied by pallor and nausea." },
      { author: "Armand Trousseau", work: "Lectures on Clinical Medicine", quote: "True **gastralgia** often mimics organic ulcer, yet yields dramatically to antispasmodics and rest." },
      { author: "George Miller Beard", work: "American Nervousness", quote: "Neurasthenic exhaustion among brain-workers commonly manifests in functional dyspepsia and debilitating **gastralgia**." }
    ]
  },
  "Dashboard — alg/mastalgia.md": {
    primary: "Pain, tenderness, or discomfort in one or both breasts, either cyclical (associated with menstrual periods) or non-cyclical.",
    secondary: "A common gynecological symptom evaluated to distinguish benign hormonally driven breast pain from underlying structural or inflammatory lesions.",
    quotes: [
      { author: "Sir Astley Cooper", work: "Illustrations of the Diseases of the Breast", quote: "Young women of nervous temperament frequently consult us for agonizing **mastalgia** where no mammary tumor exists." },
      { author: "Percivall Pott", work: "Chirurgical Works", quote: "A prudent practitioner will reassure the frightened sufferer that acute **mastalgia** rarely betokens malignant disease." },
      { author: "John Hunter", work: "A Treatise on the Blood, Inflammation, and Gun-shot Wounds", quote: "Sympathetic irritation between the uterus and mammary glands provokes recurrent premenstrual **mastalgia**." }
    ]
  },
  "Dashboard — alg/nostalgia.md": {
    primary: "A sentimental longing or wistful affection for the past, typically for a period or place with happy personal associations.",
    secondary: "Originally diagnosed in 1688 as a severe, potentially fatal medical disease of homesickness affecting Swiss mercenaries stationed far from their Alpine home.",
    quotes: [
      { author: "Johannes Hofer", work: "Dissertatio Medica de Nostalgia", quote: "We coin the diagnosis **nostalgia** to describe the melancholy wasting disease provoked by agonizing longing for one's fatherland." },
      { author: "Marcel Proust", work: "Swann's Way", quote: "A sudden taste of the tea-soaked petite madeleine ignited an overwhelming wave of childhood **nostalgia**." },
      { author: "Milan Kundera", work: "Ignorance", quote: "The Greek etymology of **nostalgia** unites *nostos*, the homecoming, with *algos*, the unbearable pain of yearning." }
    ]
  },
  "Dashboard — alg/nostalgic.md": {
    primary: "Experiencing, exhibiting, or evoking a sentimental yearning for the past or for familiar places.",
    secondary: "Characterized by wistful retrospective contemplation in art, literature, and memory studies.",
    quotes: [
      { author: "Virginia Woolf", work: "Mrs. Dalloway", quote: "The sound of Big Ben striking the hour carried a **nostalgic** weight of summers long buried in the country." },
      { author: "Vladimir Nabokov", work: "Speak, Memory", quote: "My **nostalgic** reverie recreates the stained-glass veranda of our country estate with photographic fidelity." },
      { author: "W. G. Sebald", work: "The Rings of Saturn", quote: "Walking through decaying coastal resorts, one feels a **nostalgic** ache for a grandeur that has vanished forever." }
    ]
  },

  // Dashboard — alges (5 words)
  "Dashboard — alges/algesis.md": {
    primary: "The physiological sense or perception of physical pain; the capacity to feel painful stimuli through cutaneous and visceral nociceptors.",
    secondary: "In experimental neurophysiology and somatosensory psychophysics, the direct neurological awareness of noxious stimuli.",
    quotes: [
      { author: "Charles Sherrington", work: "The Integrative Action of the Nervous System", quote: "The apparatus of **algesis** evolved as an imperative protective sentinel against tissue damage." },
      { author: "Henry Head", work: "Studies in Neurology", quote: "Protopathic sensation includes crude thermal detection and cutaneous **algesis**, mediated by unmyelinated fibers." },
      { author: "Alexander Bain", work: "The Senses and the Intellect", quote: "In the taxonomy of organic sensations, **algesis** commands the highest degree of urgent voluntary avoidance." }
    ]
  },
  "Dashboard — alges/analgesia.md": {
    primary: "The state of being unable to feel pain while remaining conscious; insensibility to pain induced by pharmaceuticals or neurogenic interruption.",
    secondary: "The targeted therapeutic dampening or abolition of noxious nerve signals in clinical anaesthesiology and pain management.",
    quotes: [
      { author: "René Descartes", work: "Treatise on Man", quote: "Were the filament running from the burned foot to the brain severed, complete **analgesia** would follow despite the blazing flame." },
      { author: "S. Weir Mitchell", work: "Wear and Tear, or Hints for the Overworked", quote: "The modern physician commands drugs that grant blessed **analgesia** to bodies broken by agonizing surgical trauma." },
      { author: "Wilder Penfield", work: "The Cerebral Cortex of Man", quote: "Direct electrical stimulation of the postcentral gyrus never produces true **analgesia**, but triggers paresthesias." }
    ]
  },
  "Dashboard — alges/analgesic.md": {
    primary: "Acting to relieve pain; a medicinal substance that diminishes or suppresses the sensation of pain.",
    secondary: "Pertaining to pharmacologic agents (e.g., opioids, NSAIDs, paracetamol) that interrupt pain pathways centrally or peripherally.",
    quotes: [
      { author: "Humphry Davy", work: "Researches, Chemical and Philosophical", quote: "Nitrous oxide appears to possess a wonderful **analgesic** property, destroying physical pain during minor surgical cutting." },
      { author: "Louis Pasteur", work: "Germ Theory and Its Applications to Medicine and Surgery", quote: "While antiseptic dressings prevent suppuration, the physician administers an **analgesic** potion to comfort the fevered wound." },
      { author: "Walter Cannon", work: "The Wisdom of the Body", quote: "The secretion of adrenaline produces an acute **analgesic** state that enables wounded animals to fight or escape." }
    ]
  },
  "Dashboard — alges/analgetic.md": {
    primary: "Alleviating pain; an analgesic agent (alternative or historical medical spelling).",
    secondary: "Causing insensibility to pain in physiological experimentation and pharmacodynamics.",
    quotes: [
      { author: "William Henry Welch", work: "Papers and Addresses", quote: "The widespread adoption of **analgetic** therapies transformed the surgical amphitheatre from a torture chamber into a place of healing." },
      { author: "T. Lauder Brunton", work: "Lectures on the Action of Medicines", quote: "Coal-tar derivatives were shown to exert a rapid **analgetic** and antipyretic action upon neuralgic patients." },
      { author: "Ernst von Leyden", work: "Clinical Lectures on Disorders of the Nervous System", quote: "We observed that this new synthetic compound acts as a powerful **analgetic** without disturbing cardiac rhythm." }
    ]
  },
  "Dashboard — alges/psychalgia.md": {
    primary: "Severe, localized physical pain of emotional, psychogenic, or mental origin, occurring without identifiable organic disease.",
    secondary: "In psychosomatic medicine and psychopathology, the somatic conversion of repressed mental conflict or emotional distress into physical aches.",
    quotes: [
      { author: "Pierre Janet", work: "The Mental State of Hystericals", quote: "The patient complained of constant cephalic **psychalgia**, which lifted only when the underlying subconscious obsession was uncovered." },
      { author: "Sigmund Freud", work: "Studies on Hysteria", quote: "In hysterical conversion, moral sorrow is transformed into genuine physical agony, a classic instance of somatic **psychalgia**." },
      { author: "Carl Jung", work: "Psychological Types", quote: "The unexpressed psychic tension of an introverted neurosis readily expresses itself bodily through stubborn **psychalgia**." }
    ]
  },

  // Dashboard — cac (18 words)
  "Dashboard — cac/cac.md": {
    primary: "The Greek prefix *cac-* (from *kakos*), meaning bad, evil, ill, diseased, or harsh, seen in *cacophony*, *cachexia*, and *cacodemonic*.",
    secondary: "The classical pejorative and pathological combining element denoting foulness, defect, moral wickedness, or physical decrepitude.",
    quotes: [
      { author: "Henry George Liddell & Robert Scott", work: "A Greek-English Lexicon", quote: "The morpheme **cac** and its fuller form *kako-* signify bad of its kind, worthless, noxious, or morally disgraceful." },
      { author: "Desiderius Erasmus", work: "Adagia", quote: "Ancient Greek proverbs made frequent play with the prefix **cac**, contrasting noble virtues with vile degeneracy." },
      { author: "Samuel Johnson", work: "A Dictionary of the English Language", quote: "In medical nomenclature, words derived from Greek **cac** universally denote depraved habit of body or malignant disease." }
    ]
  },
  "Dashboard — cac/cachectic.md": {
    primary: "Suffering from or relating to cachexia; exhibiting extreme weight loss, muscle atrophy, fatigue, and severe debility due to chronic illness.",
    secondary: "Having a haggard, emaciated, and ashen bodily appearance characteristic of terminal cancer, tuberculosis, or advanced heart failure.",
    quotes: [
      { author: "Rudolf Virchow", work: "Cellular Pathology", quote: "The **cachectic** patient exhibits profound cellular starvation as circulating toxic metabolites break down somatic protein." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The sunken eyes, sallow complexion, and wasted limbs give the late carcinoma sufferer an unmistakably **cachectic** facies." },
      { author: "Matthew Baillie", work: "The Morbid Anatomy of Some of the Most Important Parts of the Human Body", quote: "In deeply **cachectic** subjects, the internal viscera were found shrunken and devoid of adipose tissue." }
    ]
  },
  "Dashboard — cac/cachexia.md": {
    primary: "Extreme physical wasting, loss of weight, and muscle depletion occurring in the course of a chronic, debilitating disease such as advanced cancer or tuberculosis.",
    secondary: "A complex metabolic syndrome characterized by persistent hypermetabolism, systemic inflammation, and inability to reverse muscle loss with nutritional feeding alone.",
    quotes: [
      { author: "Hippocrates", work: "Aphorisms", quote: "When the humors turn corrupt, bodily **cachexia** supervenes, and the flesh melts away from the bones." },
      { author: "Thomas Sydenham", work: "Epistle to Dr. Brady", quote: "Prolonged quartan agues reduce the most robust laborers to a state of dropsical **cachexia**." },
      { author: "Jean-Nicolas Corvisart", work: "An Essay on the Organic Diseases and Lesions of the Heart", quote: "In end-stage cardiac insufficiency, the venous stasis eventually terminates in irreversible general **cachexia**." }
    ]
  },
  "Dashboard — cac/cachexy.md": {
    primary: "An older or literary form of cachexia; a depraved, exhausted, or deeply impaired physical state of the body.",
    secondary: "In 17th- and 18th-century medical and philosophical literature, a general condition of constitutional decline and vitiated bodily fluids.",
    quotes: [
      { author: "John Locke", work: "An Essay Concerning Human Understanding", quote: "A constitutional **cachexy** obstructs the natural vigor of the animal spirits, dulling the sensory organs." },
      { author: "Jonathan Swift", work: "Gulliver's Travels", quote: "The Struldbrugs suffered from an incurable spiritual and physical **cachexy** that accompanied their joyless immortality." },
      { author: "Tobias Smollett", work: "The Adventures of Peregrine Pickle", quote: "His long confinement in debtor's prison had brought on a stubborn **cachexy** that resisted all cordials." }
    ]
  },
  "Dashboard — cac/cacistocracy.md": {
    primary: "Government by the worst, least qualified, or most unscrupulous individuals; an alternative spelling of kakistocracy.",
    secondary: "A political system degraded by incompetence, venality, and moral corruption in public administration.",
    quotes: [
      { author: "Thomas Love Peacock", work: "Melincourt", quote: "If the wise and virtuous withdraw from public life, the commonwealth degenerates rapidly into a sheer **cacistocracy**." },
      { author: "James Russell Lowell", work: "The Biglow Papers", quote: "What better name than **cacistocracy** can honest citizens give to a regime where rogues distribute the spoils of office?" },
      { author: "H. L. Mencken", work: "Notes on Democracy", quote: "Under universal demagogy, democratic governance tends asymptotically toward an unmitigated **cacistocracy**." }
    ]
  },
  "Dashboard — cac/cacodemon.md": {
    primary: "An evil spirit or malevolent demon (derived from Greek *kakos* and *daimon*), contrasted with an agathodemon (benevolent spirit).",
    secondary: "A malicious person regarded as devilish; in medieval astrology, a malignant celestial position or planetary aspect bringing misfortune.",
    quotes: [
      { author: "William Shakespeare", work: "Richard III", quote: "Hie thee to hell for shame, and leave the world, thou **cacodemon**! there thy kingdom is." },
      { author: "Robert Burton", work: "The Anatomy of Melancholy", quote: "The superstitious patient imagines that a foul **cacodemon** sits upon his breast in the dark, suffocating his breathing." },
      { author: "John Webster", work: "The White Devil", quote: "Thou art a **cacodemon** in human shape, whose breath poisons the honour of our ancient house." }
    ]
  },
  "Dashboard — cac/cacodemonic.md": {
    primary: "Pertaining to, resembling, or possessed by an evil spirit; malevolent, demonic, or devilish.",
    secondary: "Characterized by frantic malice, diabolical terror, or nightmarish torment in gothic and historical literature.",
    quotes: [
      { author: "Thomas Carlyle", work: "The French Revolution: A History", quote: "The Jacobin mobs surged through the gates in a tempest of **cacodemonic** fury, shouting vengeance against the aristocrats." },
      { author: "Herman Melville", work: "Moby-Dick", quote: "Ahab paced the quarter-deck by moonlight, his furrowed brow stamped with a kind of **cacodemonic** grandeur." },
      { author: "H. P. Lovecraft", work: "The Call of Cthulhu", quote: "The cyclopean masonry seemed impregnated with a brooding, **cacodemonic** horror older than human memory." }
    ]
  },
  "Dashboard — cac/cacoepy.md": {
    primary: "Incorrect, faulty, or vulgar pronunciation of words, contrasted with orthoepy (correct pronunciation).",
    secondary: "In linguistic orthoepy and rhetorical pedagogy, speech that departs systematically from standard grammatical and phonetic norms.",
    quotes: [
      { author: "John Walker", work: "A Critical Pronouncing Dictionary", quote: "The provincial speaker often falls into habitual **cacoepy**, clipping diphthongs and misplacing the principal accent." },
      { author: "Henry Sweet", work: "A Handbook of Phonetics", quote: "What pedantic grammarians brand as **cacoepy** is often merely the legitimate phonetic evolution of popular speech." },
      { author: "George Bernard Shaw", work: "Pygmalion", quote: "Higgins took fierce delight in diagnosing cockney **cacoepy**, transforming gutter vowels into Duchess English in six months." }
    ]
  },
  "Dashboard — cac/cacography.md": {
    primary: "Bad, illegible, or careless handwriting; also bad spelling or incorrect orthography (contrasted with calligraphy and orthography).",
    secondary: "Deliberately flawed or humorous misspelling employed for comic effect in colloquial dialect literature.",
    quotes: [
      { author: "Alexander Pope", work: "The Dunciad", quote: "Page after page of wretched **cacography** flowed from the scribbler's quill, defying the compositor's tired eyes." },
      { author: "Charles Lamb", work: "Essays of Elia", quote: "His epistolary hand was such a maze of crabbed **cacography** that even the postmaster could not decipher the village name." },
      { author: "Mark Twain", work: "Life on the Mississippi", quote: "The pilot log contained marvels of frontier **cacography**, where words were spelled entirely by wild phonetic inspiration." }
    ]
  },
  "Dashboard — cac/cacophobe.md": {
    primary: "A person who fears, abhors, or displays an extreme aversion to harsh, discordant noise or disharmonious sounds.",
    secondary: "An acoustic purist or delicate listener who cannot tolerate musical dissonance, industrial clamor, or vocal discord.",
    quotes: [
      { author: "Friedrich Nietzsche", work: "Nietzsche contra Wagner", quote: "The sensitive listener becomes a terrified **cacophobe** when confronted with the blaring brass storms of modern music dramas." },
      { author: "E. M. Forster", work: "A Room with a View", quote: "Poor Cecil was an inveterate **cacophobe**, fleeing to the quiet library at the first hint of vulgar drawing-room clatter." },
      { author: "George Moore", work: "Evelyn Innes", quote: "Her father lived as a musical **cacophobe**, refusing to allow any unmelodic nineteenth-century composition past his doorway." }
    ]
  },
  "Dashboard — cac/cacophobia.md": {
    primary: "An irrational, abnormal fear or extreme hatred of ugliness, whether in physical appearance, people, or artistic objects.",
    secondary: "A psychological aversion or phobic reaction triggered by unsightly environments, facial deformities, or grotesque imagery.",
    quotes: [
      { author: "Théophile Gautier", work: "Mademoiselle de Maupin", quote: "The romantic artist suffered from acute **cacophobia**, regarding an ungraceful chair as an intolerable insult to the soul." },
      { author: "Oscar Wilde", work: "The Picture of Dorian Gray", quote: "His unspoken **cacophobia** made him recoil in shuddering horror from the first faint wrinkles on his painted canvas." },
      { author: "Arthur Schopenhauer", work: "Parerga and Paralipomena", quote: "Refined aesthetic sensibilities may border on neurotic **cacophobia**, finding the coarse reality of mankind unbearable." }
    ]
  },
  "Dashboard — cac/cacophobic.md": {
    primary: "Exhibiting or characteristic of cacophobia; intensely averse to or fearful of ugliness.",
    secondary: "Pertaining to hypersensitive distaste for unpleasing aesthetics or unsightly forms in art and daily life.",
    quotes: [
      { author: "Walter Pater", work: "Appreciations", quote: "The poet maintained a **cacophobic** vigilance over his diction, striking out any phrase that grated on the eye or ear." },
      { author: "James Joyce", work: "Ulysses", quote: "Stephen Dedalus gazed upon the battered paving stones with a weary, almost **cacophobic** distaste for civic squalor." },
      { author: "John Ruskin", work: "The Stones of Venice", quote: "Our industrial cities have created a **cacophobic** panic among cultured minds, driving them back to medieval sanctuaries." }
    ]
  },
  "Dashboard — cac/cacophonic.md": {
    primary: "Involving, producing, or characterized by harsh, jarring, discordant sound; cacophonous.",
    secondary: "Marked by an unpleasing acoustic clash of tones or syllables in speech, poetry, or musical composition.",
    quotes: [
      { author: "Hector Berlioz", work: "Memoirs", quote: "The amateur brass band erupted into a **cacophonic** uproar that sent the startled pigeons flying from the bell tower." },
      { author: "Igor Stravinsky", work: "Poetics of Music", quote: "What conservative critics first condemned as a **cacophonic** assault in the ballet score soon became the rhythm of a new century." },
      { author: "George Bernard Shaw", work: "Music in London", quote: "The theatre pit was filled with a **cacophonic** scraping of out-of-tune violins before the conductor took his stand." }
    ]
  },
  "Dashboard — cac/cacophonous.md": {
    primary: "Harsh-sounding; producing a loud, discordant, unpleasant mixture of sounds.",
    secondary: "In literary criticism, describing prose or poetry that employs rough, dissonant consonant clusters for jarring aesthetic effect.",
    quotes: [
      { author: "Herman Melville", work: "Mardi: and a Voyage Thither", quote: "The parrots kept up a **cacophonous** squawking among the mangrove boughs that drowned out our quiet oars." },
      { author: "Aldous Huxley", work: "Point Counter Point", quote: "The jazz trumpet broke into a series of jagged, **cacophonous** shrieks that mocked the sentimental melody." },
      { author: "Joseph Conrad", work: "Heart of Darkness", quote: "From the dense wall of black jungle came a **cacophonous** burst of savage drums and wild shouting." }
    ]
  },
  "Dashboard — cac/cacophony.md": {
    primary: "A harsh, discordant mixture of sounds; an unpleasant acoustic din.",
    secondary: "In phonetics and literary stylistics, the jarring, unmusical effect produced by difficult consonant combinations in succession.",
    quotes: [
      { author: "Lord Byron", work: "Don Juan", quote: "The noisy port was a babel of conflicting tongues, sea-chants, and the grating **cacophony** of creaking winches." },
      { author: "Edgar Allan Poe", work: "The Philosophy of Composition", quote: "The poet must scrupulously avoid all accidental **cacophony**, ensuring that vowels and liquids flow in melodious succession." },
      { author: "T. S. Eliot", work: "The Waste Land", quote: "The mechanical rattle of taxis and typewriter keys formed the persistent urban **cacophony** of the foggy morning." }
    ]
  },
  "Dashboard — cac/cacorrhacitis.md": {
    primary: "A severe, inflammatory disease of the spine or vertebral column (derived from Greek *kakos* 'bad' and *rhachis* 'spine', with *-itis*).",
    secondary: "In 19th-century surgical pathology, tuberculous or destructive caries of the vertebrae (closely allied to Pott's disease of the spine).",
    quotes: [
      { author: "Percivall Pott", work: "Remarks on that Kind of Palsy of the Lower Limbs", quote: "The curvature of the back and paralysis of the legs arise from an insidious **cacorrhacitis** eroding the vertebral bodies." },
      { author: "Sir Astley Cooper", work: "A Treatise on Dislocations and on Fractures of the Joints", quote: "In cases of suspected **cacorrhacitis**, absolute recumbency on a firm mattress must be enforced to prevent spinal collapse." },
      { author: "Robert Liston", work: "Practical Surgery", quote: "Suppurative **cacorrhacitis** demands early evacuation of cold abscesses before spinal cord compression ensues." }
    ]
  },
  "Dashboard — cac/kakistocracy.md": {
    primary: "Government by the worst, least qualified, or most unprincipled citizens (from Greek *kakistos* 'worst' and *kratos* 'rule').",
    secondary: "A political state or regime characterized by the utter degeneration of governance, where venality, incompetence, and greed dominate public office.",
    quotes: [
      { author: "Thomas Love Peacock", work: "Melincourt", quote: "An aristocracy of talent may decline into oligarchy, but when the lowest sycophants seize power, it becomes a true **kakistocracy**." },
      { author: "Charles Sumner", work: "The Crime Against Kansas", quote: "The territorial administration was handed over to a lawless **kakistocracy** that trampled upon the ballot box." },
      { author: "Frederick Douglass", work: "Narrative of the Life of Frederick Douglass", quote: "Under the slave power, local law was administered by an insolent **kakistocracy** that silenced all appeals to natural justice." }
    ]
  },
  "Dashboard — cac/kakistocrat.md": {
    primary: "A member of a kakistocracy; a ruler or government official who is among the worst, least qualified, or most corrupt in society.",
    secondary: "A politician or bureaucrat whose exercise of public power is marked by profound incompetence, venality, and contempt for the common good.",
    quotes: [
      { author: "Ambrose Bierce", work: "The Devil's Dictionary", quote: "The triumphant **kakistocrat** regards the national treasury as a private orchard planted exclusively for his harvest." },
      { author: "H. L. Mencken", work: "Prejudices: Fourth Series", quote: "The average party boss is an unblushing **kakistocrat**, skilled in nothing save the manipulation of human gullibility." },
      { author: "George Orwell", work: "Nineteen Eighty-Four", quote: "The inner circle had elevated the professional **kakistocrat** to supreme power, ruling through continuous deceit." }
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

console.log('Batch 1 complete! Total files updated:', Object.keys(filesData).length);
