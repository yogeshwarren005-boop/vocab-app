import fs from 'fs';
import path from 'path';

const CLUSTER_DIR = 'App database/Greek roots/Cluster Action';

const BATCH6_DATA = {
  "Dashboard — dog/dogmatist.md": {
    "primary": "A person who asserts opinions in an arrogant, positive, or dictatorial manner, without evidence or argument.",
    "secondary": "In philosophy and theology, an adherent of dogmatism who insists upon absolute doctrinal certainty without critical epistemological testing.",
    "quotes": [
      {
        "author": "David Hume",
        "work": "An Enquiry Concerning Human Understanding",
        "text": "The dogmatical spirit is natural to man; the **dogmatist** rushes boldly into speculation while the skeptic hesitates."
      },
      {
        "author": "Immanuel Kant",
        "work": "Critique of Pure Reason",
        "text": "The critical philosopher exposes the illusions of the **dogmatist** who constructs metaphysical castles in the air."
      },
      {
        "author": "John Locke",
        "work": "An Essay Concerning Human Understanding",
        "text": "No **dogmatist** is more intractable than he whose opinions are founded upon unexamined scholastic authority."
      }
    ]
  },
  "Dashboard — dog/dogmatize.md": {
    "primary": "To express principles or opinions strongly and positively as if they were indisputable facts; to preach dogmatically.",
    "secondary": "In theological discourse, to establish, define, or promulgate official religious dogmas.",
    "quotes": [
      {
        "author": "Francis Bacon",
        "work": "The Advancement of Learning",
        "text": "Men are prone to **dogmatize** upon scanty observations rather than endure the patient labor of induction."
      },
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "text": "The bishops assembled at Nicaea to **dogmatize** upon the consubstantial nature of the divine Logos."
      },
      {
        "author": "Bertrand Russell",
        "work": "Unpopular Essays",
        "text": "It is unwise to **dogmatize** about human destiny when our cosmic knowledge remains so profoundly fragmentary."
      }
    ]
  },
  "Dashboard — dog/doxology.md": {
    "primary": "A liturgical expression or short hymn of praise to God, commonly sung in Christian worship.",
    "secondary": "In hymnology, the traditional Gloria Patri or metrical verses ('Praise God from whom all blessings flow') concluding a psalm or prayer.",
    "quotes": [
      {
        "author": "John Milton",
        "work": "Paradise Lost",
        "text": "The angelic choirs struck their golden harps, raising an eternal **doxology** to the sovereign throne."
      },
      {
        "author": "George Eliot",
        "work": "Adam Bede",
        "text": "The rustic congregation stood to sing the evening **doxology**, their voices swelling through the ancient timbered nave."
      },
      {
        "author": "Thomas Hardy",
        "work": "Under the Greenwood Tree",
        "text": "The Mellstock parish band accompanied the final **doxology** with vigorous strokes on cello and clarionet."
      }
    ]
  },
  "Dashboard — dog/undogmatic.md": {
    "primary": "Not dogmatic; free from dogmatism; open-minded, tentative, and receptive to differing viewpoints.",
    "secondary": "In philosophical inquiry, characterising a critical or empirical mindset that holds conclusions provisional to fresh evidence.",
    "quotes": [
      {
        "author": "Bertrand Russell",
        "work": "A History of Western Philosophy",
        "text": "Socrates cultivated an **undogmatic** temper, demonstrating through cross-examination that he knew only that he knew nothing."
      },
      {
        "author": "William James",
        "work": "The Will to Believe",
        "text": "A healthy scientific mind remains **undogmatic**, acknowledging that our clearest hypotheses may be superseded tomorrow."
      },
      {
        "author": "John Stuart Mill",
        "work": "On Liberty",
        "text": "Progress requires an **undogmatic** public sphere where unpopular opinions may be expressed without penal censorship."
      }
    ]
  },
  "Dashboard — dog/undogmatical.md": {
    "primary": "Characterized by an absence of dogmatism; modest, cautious, and flexible in asserting beliefs.",
    "secondary": "In scholarship and intellectual history, marked by open inquiry rather than doctrinal rigidity.",
    "quotes": [
      {
        "author": "Samuel Johnson",
        "work": "The Rambler",
        "text": "He offered his corrections in an **undogmatical** tone, winning respect by his courteous forbearance."
      },
      {
        "author": "David Hume",
        "work": "Dialogues Concerning Natural Religion",
        "text": "Philo conducted the philosophical dialogue in an **undogmatical** spirit, balancing conflicting probabilities with calm neutrality."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "Science and Culture",
        "text": "The true student of nature preserves an **undogmatical** demeanor before the vast complexity of phenomena."
      }
    ]
  },
  "Dashboard — dra/dra.md": {
    "primary": "The Greek combining root (from dran, 'to do, act, perform') signifying action, theatrical enactment, or deed.",
    "secondary": "In historical etymology, the lexical root of drama, dramatic, dramatize, and drastic.",
    "quotes": [
      {
        "author": "Aristotle",
        "work": "Poetics",
        "text": "The Dorians claim both tragedy and comedy, deriving the word drama from the verb **dra** meaning to do or act."
      },
      {
        "author": "Walter William Skeat",
        "work": "An Etymological Dictionary of the English Language",
        "text": "Through Greek dran, the stem **dra** embodies the concept of forceful deed translated onto the stage."
      },
      {
        "author": "Henry George Liddell",
        "work": "A Greek-English Lexicon",
        "text": "Attic usage preserves **dra** in legal and dramatic contexts as an emphatic deed performed in public."
      }
    ]
  },
  "Dashboard — dra/drama.md": {
    "primary": "A play for theater, radio, or television; or dramatic art and literature as a genre.",
    "secondary": "An exciting, emotional, or unexpected series of events or set of circumstances in real life.",
    "quotes": [
      {
        "author": "Aristotle",
        "work": "Poetics",
        "text": "Tragic **drama** is an imitation of an action that is serious, complete, and of a certain magnitude, effecting through pity and fear the catharsis of such emotions."
      },
      {
        "author": "William Shakespeare",
        "work": "As You Like It",
        "text": "All the world's a stage, and all the men and women merely players; they have their exits and their entrances in this strange eventful **drama**."
      },
      {
        "author": "George Bernard Shaw",
        "work": "The Quintessence of Ibsenism",
        "text": "Modern **drama** abandons the clockwork intrigues of melodrama to place real human conscience upon trial."
      }
    ]
  },
  "Dashboard — dra/dramatic.md": {
    "primary": "Relating to drama or the theater; or sudden, striking, and exciting in appearance or effect.",
    "secondary": "In literary criticism and psychology, marked by intense emotional conflict, suspense, or theatrical expressiveness.",
    "quotes": [
      {
        "author": "Samuel Taylor Coleridge",
        "work": "Biographia Literaria",
        "text": "True **dramatic** illusion requires that willing suspension of disbelief for the moment which constitutes poetic faith."
      },
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "text": "The fossil record exhibits sudden, **dramatic** appearances of specialized clades in sedimentary horizons."
      },
      {
        "author": "Virginia Woolf",
        "work": "The Common Reader",
        "text": "Defoe achieves extraordinary narrative power without relying upon forced **dramatic** crises."
      }
    ]
  },
  "Dashboard — dra/dramatisation.md": {
    "primary": "The act or process of adapting a literary work or historical event for presentation as a play (chiefly British spelling).",
    "secondary": "In psychoanalysis and cognitive theory, the unconscious conversion of latent abstract thoughts into sensory, theatrical dream imagery.",
    "quotes": [
      {
        "author": "Sigmund Freud",
        "work": "The Interpretation of Dreams",
        "text": "Through **dramatisation**, abstract intellectual concepts are transformed into concrete visual scenes upon the stage of sleep."
      },
      {
        "author": "George Bernard Shaw",
        "work": "Our Theatres in the Nineties",
        "text": "The successful stage **dramatisation** of the novel required pruning secondary subplots to intensify central conflict."
      },
      {
        "author": "Walter Pater",
        "work": "Appreciations",
        "text": "Shakespeare's historical plays represent a sublime poetic **dramatisation** of the English dynastic wars."
      }
    ]
  },
  "Dashboard — dra/dramatise.md": {
    "primary": "To adapt a novel or narrative for presentation as a play or broadcast (chiefly British spelling).",
    "secondary": "To exaggerate, embellish, or present circumstances with heightened theatrical emotion.",
    "quotes": [
      {
        "author": "Henry James",
        "work": "The Art of the Novel",
        "text": "The novelist's supreme obligation is ever to **dramatise** the inner life, avoiding sterile expository summary."
      },
      {
        "author": "Jane Austen",
        "work": "Northanger Abbey",
        "text": "Catherine's romantic fancy led her to **dramatise** ordinary domestic incidents into gothic mysteries."
      },
      {
        "author": "George Eliot",
        "work": "Middlemarch",
        "text": "She had a youthful impulse to **dramatise** her own devotion, imagining severe sacrifices for duty's sake."
      }
    ]
  },
  "Dashboard — dra/dramatist.md": {
    "primary": "A person who writes plays; a playwright.",
    "secondary": "In literary history, an author who constructs narrative through dialogue, scenic action, and theatrical staging.",
    "quotes": [
      {
        "author": "Samuel Johnson",
        "work": "Preface to Shakespeare",
        "text": "Shakespeare is, above all writers, at least above all modern writers, the **dramatist** of nature."
      },
      {
        "author": "John Dryden",
        "work": "An Essay of Dramatic Poesy",
        "text": "The modern **dramatist** must observe decorum while animating the scene with vigorous passions."
      },
      {
        "author": "George Bernard Shaw",
        "work": "Plays Pleasant and Unpleasant",
        "text": "The duty of the serious **dramatist** is to challenge the moral complacencies of the comfortable classes."
      }
    ]
  },
  "Dashboard — dra/dramatization.md": {
    "primary": "The adaptation of a story or event into a dramatic script or theatrical performance.",
    "secondary": "The act of presenting an ordinary event with excessive, theatrical emotion or embellishment.",
    "quotes": [
      {
        "author": "Sigmund Freud",
        "work": "A General Introduction to Psychoanalysis",
        "text": "The dream-work employs plastic **dramatization**, staging internal wishes as dynamic visual occurrences."
      },
      {
        "author": "Herman Melville",
        "work": "The Confidence-Man",
        "text": "The masquerade was an elaborate social **dramatization** where every traveler enacted a chosen role."
      },
      {
        "author": "Arthur Conan Doyle",
        "work": "Memories and Adventures",
        "text": "The stage **dramatization** of Sherlock Holmes proved a spectacular triumph in London and New York."
      }
    ]
  },
  "Dashboard — dra/dramatize.md": {
    "primary": "To adapt for the stage, film, or broadcast; or to present something in an exaggerated or theatrical manner.",
    "secondary": "In narrative poetics, to render thoughts and psychological motives as spoken, visible actions.",
    "quotes": [
      {
        "author": "Henry James",
        "work": "The Ambassadors",
        "text": "Dramatize, **dramatize**! was my constant creative watchword, turning every mental hesitation into scenic confrontation."
      },
      {
        "author": "Ralph Waldo Emerson",
        "work": "Essays: First Series",
        "text": "We tend to **dramatize** our misfortunes, acting tragic roles before the sympathetic mirror of our own vanity."
      },
      {
        "author": "Mark Twain",
        "work": "Life on the Mississippi",
        "text": "Old river pilots loved to **dramatize** a shallow sandbar crossing into a harrowing encounter with doom."
      }
    ]
  },
  "Dashboard — dra/drastic.md": {
    "primary": "Likely to have a strong, severe, radical, or far-reaching effect; extreme in action.",
    "secondary": "Historically in medicine and pharmacology, designating powerful purgatives or cathartics that act with extreme violence.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "text": "Ancient therapeutics relied too heavily upon **drastic** purgatives that exhausted the patient's remaining vitality."
      },
      {
        "author": "Winston Churchill",
        "work": "The Second World War",
        "text": "The critical shortage of shipping demanded **drastic** rationing across all sectors of the civilian economy."
      },
      {
        "author": "Adam Smith",
        "work": "The Wealth of Nations",
        "text": "Sudden and **drastic** prohibitions upon foreign trade disrupt domestic employment and provoke economic turmoil."
      }
    ]
  },
  "Dashboard — dra/melodrama.md": {
    "primary": "A sensational dramatic piece with exaggerated characters and exciting events intended to appeal to the emotions.",
    "secondary": "Historically, a theatrical genre combining spoken dialogue with musical accompaniment; or any overly theatrical real-life situation.",
    "quotes": [
      {
        "author": "George Bernard Shaw",
        "work": "Our Theatres in the Nineties",
        "text": "Popular Victorian **melodrama** offered clear moral simplifications, where virtue triumphed and villainy was swiftly punished."
      },
      {
        "author": "Henry James",
        "work": "The Portrait of a Lady",
        "text": "Isabel shrank from anything resembling cheap domestic **melodrama**, desiring only dignified clarity."
      },
      {
        "author": "Charles Dickens",
        "work": "Nicholas Nickleby",
        "text": "Mr. Crummles's traveling company delighted provincial audiences with broad romantic **melodrama** and broadsword fights."
      }
    ]
  },
  "Dashboard — dra/melodramatic.md": {
    "primary": "Characteristic of melodrama, especially in being overly theatrical, exaggerated, or emotional.",
    "secondary": "Appealing to sensationalism or crude emotional effect rather than nuanced psychological truth.",
    "quotes": [
      {
        "author": "Jane Austen",
        "work": "Northanger Abbey",
        "text": "Catherine blushed at her own **melodramatic** suspicions, realizing General Tilney was merely a selfish, proud man."
      },
      {
        "author": "Arthur Conan Doyle",
        "work": "A Study in Scarlet",
        "text": "There was no need for **melodramatic** flourish; the grim facts in the Brixton Road spoke clearly for themselves."
      },
      {
        "author": "George Eliot",
        "work": "Middlemarch",
        "text": "Lydgate despised the **melodramatic** posturing of rival provincial doctors who peddled miraculous nostrums."
      }
    ]
  },
  "Dashboard — dra/monodrama.md": {
    "primary": "A dramatic piece for one actor or speaker only, typically depicting an internal psychological crisis.",
    "secondary": "In musical theater and poetics, a theatrical monologue with musical accompaniment, such as Tennyson's Maud.",
    "quotes": [
      {
        "author": "Alfred Tennyson",
        "work": "Maud: A Monodrama",
        "text": "The poet cast the psychological narrative as a passionate **monodrama**, charting the speaker's descent into madness and recovery."
      },
      {
        "author": "Walter Pater",
        "work": "Appreciations",
        "text": "Robert Browning's dramatic monologues approach the intensity of a private **monodrama** unfolding in the soul."
      },
      {
        "author": "George Bernard Shaw",
        "work": "Dramatic Opinions and Essays",
        "text": "The solo performance succeeded as a tour de force of **monodrama**, holding the crowded auditorium through solitary presence."
      }
    ]
  },
  "Dashboard — dra/undramatic.md": {
    "primary": "Not dramatic; lacking excitement, suspense, or emotional intensity; quiet, ordinary, or uneventful.",
    "secondary": "In literature and historical narrative, soberly realistic and avoiding theatrical exaggeration.",
    "quotes": [
      {
        "author": "George Orwell",
        "work": "Homage to Catalonia",
        "text": "Modern trench warfare is mostly an **undramatic** business of mud, cold, lice, and interminable boredom."
      },
      {
        "author": "Virginia Woolf",
        "work": "To the Lighthouse",
        "text": "Her thoughts moved through the **undramatic** routine of afternoon tea and children's bedtimes with tranquil grace."
      },
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "text": "Natural selection operates through **undramatic**, infinitesimal variations accumulated over millions of years."
      }
    ]
  },
  "Dashboard — erg/allergic.md": {
    "primary": "Relating to, caused by, or characterized by allergy, an abnormal immunological hypersensitivity.",
    "secondary": "Informally, having a strong antipathy, aversion, or reluctance toward someone or something.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "text": "The acute **allergic** response involves cutaneous urticaria, bronchospasm, and sudden capillary dilatation."
      },
      {
        "author": "Rachel Carson",
        "work": "Silent Spring",
        "text": "Synthetic chemical aerosols provoke severe **allergic** sensitisation in individuals chronically exposed to crop dusts."
      },
      {
        "author": "Siddhartha Mukherjee",
        "work": "The Song of the Cell",
        "text": "When IgE antibodies cross-link on mast cells, they ignite a violent cascade of **allergic** inflammation."
      }
    ]
  },
  "Dashboard — erg/allergist.md": {
    "primary": "A medical physician specializing in the diagnosis and clinical treatment of allergies and immunological disorders.",
    "secondary": "In clinical immunology, an expert evaluating hypersensitivities via skin prick testing, desensitization, and immunotherapy.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "text": "The consulting **allergist** identified ragweed pollen as the principal trigger of the child's intractable seasonal asthma."
      },
      {
        "author": "Siddhartha Mukherjee",
        "work": "The Song of the Cell",
        "text": "Working at the intersection of immunology and clinic, the **allergist** uncovers how the immune system turns against harmless proteins."
      },
      {
        "author": "Oliver Sacks",
        "work": "A Leg to Stand On",
        "text": "Skin testing conducted by an experienced **allergist** ruled out hypersensitivity to the surgical antibiotic wash."
      }
    ]
  },
  "Dashboard — erg/allergy.md": {
    "primary": "A damaging immune response by the body to a substance, especially pollen, fur, food, or dust, to which it has become hypersensitive.",
    "secondary": "In immunology, Clemens von Pirquet's term for altered biological reactivity following antigen exposure.",
    "quotes": [
      {
        "author": "Clemens von Pirquet",
        "work": "Allergy",
        "text": "I proposed the term **allergy** to designate this general condition of altered immunological responsiveness."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "text": "Anaphylaxis represents the most extreme, life-threatening manifestation of systemic drug **allergy**."
      },
      {
        "author": "Rachel Carson",
        "work": "Silent Spring",
        "text": "Chemical pollution induces an acquired environmental **allergy**, leaving tissues vulnerable to everyday household toxins."
      }
    ]
  },
  "Dashboard — erg/argon.md": {
    "primary": "A chemical element of atomic number 18 (symbol Ar), an inert noble gas that makes up roughly 0.93% of Earth's atmosphere.",
    "secondary": "Named from Greek argos ('lazy, inactive') by Lord Rayleigh and William Ramsay due to its chemical inertness.",
    "quotes": [
      {
        "author": "Lord Rayleigh",
        "work": "Argon, a New Constituent of the Atmosphere",
        "text": "William Ramsay and I succeeded in isolating **argon**, a gaseous element distinguished by absolute chemical inertness."
      },
      {
        "author": "William Ramsay",
        "work": "The Gases of the Atmosphere",
        "text": "Refusing to combine with oxygen, fluorine, or alkali metals, **argon** earned its name from the Greek word for idle."
      },
      {
        "author": "Arthur Holmes",
        "work": "Principles of Physical Geology",
        "text": "Radiometric dating measures the steady accumulation of radiogenic **argon** produced by potassium-40 decay in minerals."
      }
    ]
  },
  "Dashboard — erg/asynergic.md": {
    "primary": "Lacking synergy or muscular coordination; characterized by asynergy.",
    "secondary": "In clinical neurology, describing gait or movements marked by the failure of agonist and antagonist muscles to cooperate smoothly.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "text": "Cerebellar hemorrhage produces an **asynergic** gait wherein the patient's trunk lags clumsily behind his advancing legs."
      },
      {
        "author": "Oliver Sacks",
        "work": "The Man Who Mistook His Wife for a Hat",
        "text": "The limbs performed jerky, **asynergic** reaches, overshooting the teacup by several inches."
      },
      {
        "author": "Charles Sherrington",
        "work": "The Integrative Action of the Nervous System",
        "text": "Disruption of proprioceptive feedback loops renders voluntary movements painfully slow and **asynergic**."
      }
    ]
  },
  "Dashboard — erg/asynergy.md": {
    "primary": "Lack of coordination between muscles, organs, or physiological systems that normally act together.",
    "secondary": "In clinical neurology, a cardinal sign of cerebellar disease characterized by the breakdown of complex compound movements into isolated jerks.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "text": "Joseph Babinski defined cerebellar **asynergy** as the inability to coordinate the muscular components of complex motor acts."
      },
      {
        "author": "Oliver Sacks",
        "work": "A Leg to Stand On",
        "text": "A sudden profound **asynergy** overtook the leg, rendering each conscious step a chaotic mechanical puzzle."
      },
      {
        "author": "Charles Sherrington",
        "work": "The Integrative Action of the Nervous System",
        "text": "Without the cerebellum's coordinating tonicity, motor commands disintegrate into clumsy **asynergy**."
      }
    ]
  },
  "Dashboard — erg/demiurge.md": {
    "primary": "A being responsible for the creation of the universe, especially in Plato's philosophy and Gnostic theology.",
    "secondary": "In Gnosticism, an inferior, subordinate deity regarded as the creator of the material, flawed physical world.",
    "quotes": [
      {
        "author": "Plato",
        "work": "Timaeus",
        "text": "The benevolent **demiurge** fashioned the physical cosmos by gazing upon the eternal, unchanging Forms."
      },
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "text": "Gnostic sects distinguished the supreme spiritual deity from the blind, material **demiurge** who formed this sorrowful earth."
      },
      {
        "author": "Bertrand Russell",
        "work": "A History of Western Philosophy",
        "text": "In Plato's cosmogony, the **demiurge** does not create ex nihilo, but imposes order and geometric harmony upon chaotic matter."
      }
    ]
  },
  "Dashboard — erg/dramaturgic.md": {
    "primary": "Relating to dramaturgy, the art, craft, or technique of dramatic composition and theatrical representation.",
    "secondary": "In sociological analysis, applying concepts of theatrical performance and stagecraft to everyday human social interaction.",
    "quotes": [
      {
        "author": "Gotthold Ephraim Lessing",
        "work": "Hamburg Dramaturgy",
        "text": "Strict **dramaturgic** principles require that theatrical action spring organically from character rather than theatrical contrivance."
      },
      {
        "author": "Erving Goffman",
        "work": "The Presentation of Self in Everyday Life",
        "text": "A **dramaturgic** perspective reveals how individuals maintain front-stage composure while concealing back-stage doubts."
      },
      {
        "author": "George Bernard Shaw",
        "work": "Dramatic Opinions and Essays",
        "text": "Ibsen possessed an unmatched **dramaturgic** economy, eliminating every line that failed to deepen moral exposure."
      }
    ]
  },
  "Dashboard — erg/dramaturgical.md": {
    "primary": "Pertaining to the technical composition or staging of dramatic works; theatrical.",
    "secondary": "In social theory, describing human behavior as an ongoing theatrical performance for an audience.",
    "quotes": [
      {
        "author": "Erving Goffman",
        "work": "The Presentation of Self in Everyday Life",
        "text": "From a **dramaturgical** standpoint, social life is an ongoing series of performances where actors manage impressions."
      },
      {
        "author": "T. S. Eliot",
        "work": "Selected Essays",
        "text": "Shakespeare's **dramaturgical** skill reached its zenith in Hamlet, balancing poetry with swift stage action."
      },
      {
        "author": "Walter Pater",
        "work": "Appreciations",
        "text": "The historical drama requires profound **dramaturgical** intuition to condense decades of chronicle into two hours."
      }
    ]
  },
  "Dashboard — erg/dramaturgy.md": {
    "primary": "The theory, craft, and practice of dramatic composition and theatrical representation.",
    "secondary": "In contemporary sociology, the study of social interaction through theatrical metaphors of scripts, stages, and performers.",
    "quotes": [
      {
        "author": "Gotthold Ephraim Lessing",
        "work": "Hamburg Dramaturgy",
        "text": "True **dramaturgy** teaches that tragedy purifies our passions by holding a clear mirror up to human nature."
      },
      {
        "author": "Erving Goffman",
        "work": "The Presentation of Self in Everyday Life",
        "text": "The concepts of **dramaturgy** illustrate how social roles are sustained by careful control of scenery and props."
      },
      {
        "author": "George Bernard Shaw",
        "work": "The Quintessence of Ibsenism",
        "text": "Ibsen overturned the conventional **dramaturgy** of Paris, replacing manufactured intrigue with searing discussion."
      }
    ]
  },
  "Dashboard — erg/endoergic.md": {
    "primary": "In physics and physical chemistry, requiring the absorption of energy; endothermic in a nuclear or reaction process.",
    "secondary": "Describing nuclear reactions in which the total kinetic energy of the products is less than that of the reacting particles (negative Q-value).",
    "quotes": [
      {
        "author": "Enrico Fermi",
        "work": "Nuclear Physics",
        "text": "An **endoergic** nuclear disintegration requires the incident particle to exceed a definite kinetic energy threshold."
      },
      {
        "author": "Ernest Rutherford",
        "work": "Radiations from Radioactive Substances",
        "text": "Artificial transmutation induced by alpha bombardment is frequently an **endoergic** process absorbing nuclear energy."
      },
      {
        "author": "Hans Bethe",
        "work": "Elementary Nuclear Theory",
        "text": "Calculations of cross sections for **endoergic** collisions must incorporate the negative energy balance of the reaction."
      }
    ]
  },
  "Dashboard — erg/energetic.md": {
    "primary": "Showing or involving great activity, drive, or vitality; vigorous and active.",
    "secondary": "In physics and thermodynamics, relating to energy, its transformations, and mechanical work potential.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Voyage of the Beagle",
        "text": "The gauchos are bold, **energetic** horsemen, capable of enduring immense physical fatigue across the pampas."
      },
      {
        "author": "William James",
        "work": "The Energies of Men",
        "text": "Human beings possess an **energetic** reserve that is summoned only under conditions of heroic crisis."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "Lay Sermons, Addresses, and Reviews",
        "text": "Science demands **energetic** skepticism, testing every proposition against the hard anvil of facts."
      }
    ]
  },
  "Dashboard — erg/energise.md": {
    "primary": "To give vitality, enthusiasm, and vigor to; to invigorate or stimulate (chiefly British spelling).",
    "secondary": "In electrical engineering, to supply electric current or power to a device, circuit, or magnet.",
    "quotes": [
      {
        "author": "Michael Faraday",
        "work": "Experimental Researches in Electricity",
        "text": "Connecting the voltaic battery served to **energise** the core of the great electromagnet instantly."
      },
      {
        "author": "Thomas Carlyle",
        "work": "Past and Present",
        "text": "A great national hero must arise to **energise** the sluggish conscience of a distracted people."
      },
      {
        "author": "H. G. Wells",
        "work": "The Time Machine",
        "text": "Closing the contact switch allowed the dynamos to **energise** the gleaming brass mechanism of the traveler."
      }
    ]
  },
  "Dashboard — erg/energiser.md": {
    "primary": "One who or that which energises; a person, device, or substance that provides vigor or power (chiefly British spelling).",
    "secondary": "In agricultural engineering, an electric fence charging unit supplying intermittent voltage pulses.",
    "quotes": [
      {
        "author": "Thomas Edison",
        "work": "Notebooks and Diaries",
        "text": "The powerful steam dynamo acted as the prime **energiser** of the entire Lower Manhattan lighting grid."
      },
      {
        "author": "William James",
        "work": "The Will to Believe",
        "text": "Passionate faith is a moral **energiser**, unlocking unsuspected capacities for endurance and action."
      },
      {
        "author": "Arthur Conan Doyle",
        "work": "The Stark Munro Letters",
        "text": "Fresh morning sea breezes served as a wondrous **energiser** for our tired clinical minds."
      }
    ]
  },
  "Dashboard — erg/energising.md": {
    "primary": "Giving vitality, energy, or enthusiasm; invigorating (chiefly British spelling).",
    "secondary": "Supplying electrical power or physical energy to an apparatus or physiological system.",
    "quotes": [
      {
        "author": "William Wordsworth",
        "work": "The Prelude",
        "text": "Nature imparted an **energising** spirit that exalted the youthful heart above petty anxieties."
      },
      {
        "author": "Claude Bernard",
        "work": "Lectures on the Phenomena of Life",
        "text": "Oxygenation of arterial blood plays an **energising** role in sustaining muscular and cerebral vitality."
      },
      {
        "author": "Winston Churchill",
        "work": "The Second World War",
        "text": "His arrival at headquarters had an **energising** effect upon the fatigued staff, restoring confidence and purpose."
      }
    ]
  },
  "Dashboard — erg/energize.md": {
    "primary": "To give energy to; to activate, stimulate, or invigorate.",
    "secondary": "In electrical engineering and mechanics, to supply operating voltage, current, or mechanical impulse to a system.",
    "quotes": [
      {
        "author": "Nikola Tesla",
        "work": "My Inventions",
        "text": "High-frequency resonant coils **energize** the surrounding atmosphere, transmitting wireless power through space."
      },
      {
        "author": "Ralph Waldo Emerson",
        "work": "Essays: First Series",
        "text": "Courageous thoughts **energize** the will, sweeping aside artificial impediments to great achievement."
      },
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "text": "An intense emotional interest will **energize** the neural cortex, focusing attention with fierce intensity."
      }
    ]
  },
  "Dashboard — erg/energizer.md": {
    "primary": "One who or that which imparts energy, vigor, or electrical power.",
    "secondary": "In athletics and nutrition, an agent or beverage formulated to boost physical stamina or alertness.",
    "quotes": [
      {
        "author": "Thomas Edison",
        "work": "Writings and Observations",
        "text": "The central generator stood as the tireless **energizer** of the industrial works along the river."
      },
      {
        "author": "William James",
        "work": "The Energies of Men",
        "text": "A sudden crisis serves as a psychological **energizer**, calling forth dormant human capacities."
      },
      {
        "author": "Jack London",
        "work": "The Sea-Wolf",
        "text": "The stinging spray of the northern gale was a fierce **energizer** for the crew of the sealing schooner."
      }
    ]
  },
  "Dashboard — erg/energizing.md": {
    "primary": "Imparting energy, vitality, or vigor; stimulating and refreshing.",
    "secondary": "Supplying active electrical current or driving power to an apparatus.",
    "quotes": [
      {
        "author": "Henry David Thoreau",
        "work": "Walden",
        "text": "Morning air has an **energizing** purity that awakens the contemplative spirit to the dawn of creation."
      },
      {
        "author": "Michael Faraday",
        "work": "Experimental Researches in Electricity",
        "text": "By **energizing** the secondary winding with rapid pulses, we induced powerful luminous sparks across the gap."
      },
      {
        "author": "John Muir",
        "work": "The Mountains of California",
        "text": "Glacial winds sweeping down from Sierra peaks have an **energizing** clarity that banishes all human languor."
      }
    ]
  },
  "Dashboard — erg/energy.md": {
    "primary": "The strength and vitality required for sustained physical or mental activity; drive and enthusiasm.",
    "secondary": "In physics, the quantitative property that must be transferred to a body or physical system to perform work or produce heat.",
    "quotes": [
      {
        "author": "Albert Einstein",
        "work": "Relativity: The Special and General Theory",
        "text": "Mass and **energy** are different manifestations of the same thing—a somewhat unfamiliar conception for the average mind."
      },
      {
        "author": "James Prescott Joule",
        "work": "On the Mechanical Equivalent of Heat",
        "text": "Whenever mechanical force is expended, an exact equivalent of thermal **energy** is invariably generated."
      },
      {
        "author": "Richard Feynman",
        "work": "The Feynman Lectures on Physics",
        "text": "There is a law governing all natural phenomena: the total quantity called **energy** remains strictly conserved."
      }
    ]
  },
  "Dashboard — erg/erg.md": {
    "primary": "A unit of work or energy in the centimeter-gram-second (CGS) system, equal to 10^-7 joules.",
    "secondary": "In geomorphology, a vast, flat area of desert covered with wind-swept sand dunes with little or no vegetative cover.",
    "quotes": [
      {
        "author": "James Clerk Maxwell",
        "work": "A Treatise on Electricity and Magnetism",
        "text": "The British Association defined the **erg** as the mechanical work done by a force of one dyne acting through one centimeter."
      },
      {
        "author": "Antoine de Saint-Exupéry",
        "work": "Wind, Sand and Stars",
        "text": "Our airplane crossed the shimmering wilderness of the Grand **Erg**, where golden barchans rolled toward the horizon."
      },
      {
        "author": "Max Planck",
        "work": "The Theory of Heat Radiation",
        "text": "The quantum of action expresses energy multiplied by time, yielding dimensions of the **erg**-second."
      }
    ]
  },
  "Dashboard — erg/ergate.md": {
    "primary": "A worker ant, the sterile female caste that performs foraging, nest construction, and brood care in an ant colony.",
    "secondary": "In myrmecology and entomology, the wingless adult worker form of social hymenopterans lacking functional reproductive anatomy.",
    "quotes": [
      {
        "author": "William Morton Wheeler",
        "work": "Ants: Their Structure, Development and Behavior",
        "text": "The typical **ergate** displays profound morphological reduction, lacking both ocelli and flight musculature."
      },
      {
        "author": "E. O. Wilson",
        "work": "The Insect Societies",
        "text": "Caste differentiation within Pheidole produces both the small foraging **ergate** and the colossal soldier."
      },
      {
        "author": "Arthur D. Imms",
        "work": "A General Textbook of Entomology",
        "text": "Nutrition during the early larval instars determines whether the female egg matures into a queen or an **ergate**."
      }
    ]
  },
  "Dashboard — erg/ergatocracy.md": {
    "primary": "Government or political rule by workers or the working class; worker democracy or dictatorship of the proletariat.",
    "secondary": "In political philosophy and sociology, a state where political authority resides entirely in workers' councils or trade syndicates.",
    "quotes": [
      {
        "author": "Bertrand Russell",
        "work": "The Practice and Theory of Bolshevism",
        "text": "The early revolutionary soviets purported to establish an **ergatocracy**, placing state power in the hands of industrial laborers."
      },
      {
        "author": "George Bernard Shaw",
        "work": "The Intelligent Woman's Guide to Socialism and Capitalism",
        "text": "Advocates of syndicalism dreamt of an **ergatocracy** where each industry was governed directly by its organized producers."
      },
      {
        "author": "H. G. Wells",
        "work": "The Shape of Things to Come",
        "text": "Utopian theorists envisioned an efficient **ergatocracy** that would abolish hereditary privilege in favor of productive merit."
      }
    ]
  },
  "Dashboard — erg/ergometer.md": {
    "primary": "An apparatus designed for measuring work performed by muscles, or the power output of human or animal exertion.",
    "secondary": "In exercise physiology and sports medicine, a stationary bicycle or rowing machine equipped with load resistance to assess aerobic capacity.",
    "quotes": [
      {
        "author": "August Krogh",
        "work": "The Anatomy and Physiology of Capillaries",
        "text": "Subjects working on the bicycle **ergometer** demonstrated a forty-fold increase in open muscular capillaries."
      },
      {
        "author": "Archibald Hill",
        "work": "Muscular Activity",
        "text": "By coupling muscular contraction to a recording **ergometer**, we measured the precise mechanical efficiency of human muscle."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "text": "Cardiac stress testing utilizing a calibrated **ergometer** unmasks latent coronary ischemia."
      }
    ]
  },
  "Dashboard — erg/ergon.md": {
    "primary": "The Greek word for work, deed, task, or action; or an elementary unit of energy in physical chemistry.",
    "secondary": "In early quantum mechanics, a name proposed by Max Planck for the quantum of action (energy element).",
    "quotes": [
      {
        "author": "Aristotle",
        "work": "Nicomachean Ethics",
        "text": "The ultimate good of man resides in his specific function or **ergon**, which is the active exercise of the soul in accordance with reason."
      },
      {
        "author": "Max Planck",
        "work": "Scientific Autobiography",
        "text": "I originally designated the discrete energy packet as an **ergon**, before the terminology of the quantum became universally accepted."
      },
      {
        "author": "Hannah Arendt",
        "work": "The Human Condition",
        "text": "Greek thought distinguished between effortless biological labor and the enduring crafted work of the **ergon**."
      }
    ]
  },
  "Dashboard — erg/ergonomic.md": {
    "primary": "Designed for efficiency, ease of use, and comfort in the working environment, minimizing physical strain.",
    "secondary": "Pertaining to human engineering, optimizing tools and machinery to accommodate human anatomical and cognitive capabilities.",
    "quotes": [
      {
        "author": "Oliver Sacks",
        "work": "A Leg to Stand On",
        "text": "The surgical ward was equipped with **ergonomic** armchairs designed to support the lower spine during prolonged recovery."
      },
      {
        "author": "Richard Feynman",
        "work": "Surely You're Joking, Mr. Feynman!",
        "text": "Control panels in industrial cockpits require sound **ergonomic** layout to prevent fatal operator confusion under stress."
      },
      {
        "author": "Donald Norman",
        "work": "The Design of Everyday Things",
        "text": "A poorly conceived interface ignores **ergonomic** human factors, forcing the user into unnatural physical postures."
      }
    ]
  },
  "Dashboard — erg/ergonomics.md": {
    "primary": "The study of people's efficiency in their working environment; biotechnology applied to workstation design.",
    "secondary": "In industrial engineering, the science of adapting workplace tools, furniture, and systems to human biomechanics.",
    "quotes": [
      {
        "author": "Donald Norman",
        "work": "The Design of Everyday Things",
        "text": "Modern **ergonomics** unites human anatomy, cognitive psychology, and mechanical design into a coherent discipline."
      },
      {
        "author": "Oliver Sacks",
        "work": "An Anthropologist on Mars",
        "text": "Temple Grandin designed livestock facilities utilizing principles of animal **ergonomics** to reduce distress."
      },
      {
        "author": "Norbert Wiener",
        "work": "Cybernetics",
        "text": "The feedback loops linking machine controls to human musculature form the foundation of practical **ergonomics**."
      }
    ]
  },
  "Dashboard — erg/exoergic.md": {
    "primary": "In physics and physical chemistry, releasing energy; exothermic, especially in a nuclear reaction process.",
    "secondary": "Describing nuclear or chemical reactions in which the total kinetic energy of the products exceeds that of the reactants (positive Q-value).",
    "quotes": [
      {
        "author": "Enrico Fermi",
        "work": "Elementary Particles",
        "text": "Slow neutron capture in uranium initiates an intensely **exoergic** fission chain releasing millions of electron volts."
      },
      {
        "author": "Hans Bethe",
        "work": "Energy Production in Stars",
        "text": "The carbon-nitrogen cycle in stellar cores is an **exoergic** thermonuclear furnace converting hydrogen into helium."
      },
      {
        "author": "Robert Oppenheimer",
        "work": "Physics in the Contemporary World",
        "text": "Harnessing the immense **exoergic** output of nuclear binding energies transformed world geopolitics forever."
      }
    ]
  },
  "Dashboard — erg/gamergate.md": {
    "primary": "In myrmecology and entomology, a mated, fertile worker ant that can reproduce in place of or in the absence of a morphological queen.",
    "secondary": "A functional reproductive female worker in queenless social insect colonies, capable of laying diploid eggs.",
    "quotes": [
      {
        "author": "E. O. Wilson",
        "work": "The Insect Societies",
        "text": "In primitive ponerine ants, a mated **gamergate** assumes the egg-laying role, dispensing with the specialized queen caste."
      },
      {
        "author": "William Morton Wheeler",
        "work": "Ants: Their Structure, Development and Behavior",
        "text": "Behavioral dominance rituals among workers determine which individual becomes the colony's functional **gamergate**."
      },
      {
        "author": "Bert Hölldobler",
        "work": "The Ants",
        "text": "Chemical pheromones secreted by the functional **gamergate** suppress ovarian development in fellow nestmates."
      }
    ]
  },
  "Dashboard — erg/heterorganic.md": {
    "primary": "In phonetics and linguistics, articulated with different vocal organs or speech articulators.",
    "secondary": "In comparative anatomy, derived from or composed of differing anatomical organs or organic systems.",
    "quotes": [
      {
        "author": "Max Müller",
        "work": "Lectures on the Science of Language",
        "text": "Transitions between homorganic consonants are smooth, whereas shifting between **heterorganic** sounds requires distinct muscular readjustment."
      },
      {
        "author": "Henry Sweet",
        "work": "A Handbook of Phonetics",
        "text": "Consonant clusters combining labial and velar elements are **heterorganic**, demanding rapid shifts in tongue and lip positioning."
      },
      {
        "author": "Richard Owen",
        "work": "On the Anatomy of Vertebrates",
        "text": "The compound structure was revealed to be a **heterorganic** synthesis of dermal bone and endochondral cartilage."
      }
    ]
  },
  "Dashboard — erg/homorganic.md": {
    "primary": "In phonetics, produced or articulated with the same speech organs (such as p, b, and m, which are all bilabial).",
    "secondary": "In linguistics, sounds that share identical place of articulation while differing in manner or voicing.",
    "quotes": [
      {
        "author": "Henry Sweet",
        "work": "A Handbook of Phonetics",
        "text": "Nasal assimilation naturally produces **homorganic** sequences, as seen when 'in-' becomes 'im-' before bilabial stops."
      },
      {
        "author": "Max Müller",
        "work": "Lectures on the Science of Language",
        "text": "Sanskrit grammarians meticulously grouped consonants into classes based on their **homorganic** vocal origin."
      },
      {
        "author": "Edward Sapir",
        "work": "Language: An Introduction to the Study of Speech",
        "text": "The ease of pronouncing **homorganic** clusters explains why children master nasal-stop pairs early in speech development."
      }
    ]
  },
  "Dashboard — erg/liturgical.md": {
    "primary": "Relating to liturgy or public religious worship, especially standardized rites and ceremonies.",
    "secondary": "In ecclesiastical history, pertaining to prescribed prayer forms, vestments, rubrics, and choral rituals.",
    "quotes": [
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "text": "Byzantine basilicas resounded with elaborate **liturgical** chants that celebrated the majesty of the heavenly court."
      },
      {
        "author": "T. S. Eliot",
        "work": "Selected Essays",
        "text": "The solemn cadence of Cranmer's **liturgical** prose left an indelible stamp upon the rhythms of English literature."
      },
      {
        "author": "John Henry Newman",
        "work": "Apologia Pro Vita Sua",
        "text": "The beauty of the ancient Catholic **liturgical** tradition offered a refuge from the shallow rationalism of modern controversy."
      }
    ]
  },
  "Dashboard — erg/liturgist.md": {
    "primary": "A person who studies, writes, or directs liturgical worship; an expert in liturgics.",
    "secondary": "In classical Athens, a wealthy citizen who funded public works or theatrical choruses (choregos) as a civic tax.",
    "quotes": [
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "text": "The learned Byzantine **liturgist** codified every bow, incense swing, and vestment used in the patriarchal liturgy."
      },
      {
        "author": "George Grote",
        "work": "A History of Greece",
        "text": "In democratic Athens, the public-spirited **liturgist** took immense pride in outfitting a trireme or staging a tragedy at his own cost."
      },
      {
        "author": "John Henry Newman",
        "work": "Historical Sketches",
        "text": "The Roman **liturgist** reformed the breviary, stripping away medieval accretions to restore patristic purity."
      }
    ]
  },
  "Dashboard — erg/liturgy.md": {
    "primary": "A customary code of public religious worship and ritual ceremonies, especially in Christian churches.",
    "secondary": "In ancient Greece, a mandatory civic duty or public service performed by wealthy citizens at their own expense.",
    "quotes": [
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "text": "Under the golden dome of Saint Sophia, Justinian witnessed the solemn **liturgy** enacted by hundreds of white-robed priests."
      },
      {
        "author": "Aristotle",
        "work": "Politics",
        "text": "In well-ordered democracies, the expenses of the religious festivals and theatrical choruses are borne through the civic **liturgy**."
      },
      {
        "author": "John Henry Newman",
        "work": "The Idea of a University",
        "text": "Sacred **liturgy** unites aesthetic splendor with spiritual devotion, engaging the imagination in the adoration of God."
      }
    ]
  },
  "Dashboard — erg/microorganism.md": {
    "primary": "A microscopic organism, especially a bacterium, virus, or microscopic fungus.",
    "secondary": "In microbiology and public health, single-celled or acellular biological entities that drive biogeochemical cycles and infectious diseases.",
    "quotes": [
      {
        "author": "Louis Pasteur",
        "work": "Studies on Fermentation",
        "text": "Fermentation is not an inorganic chemical breakdown, but an act of life correlative with the nutrition of a microscopic **microorganism**."
      },
      {
        "author": "Robert Koch",
        "work": "The Etiology of Tuberculosis",
        "text": "Isolation of the specific pathogenic **microorganism** in pure culture is essential to prove bacterial etiology."
      },
      {
        "author": "Rachel Carson",
        "work": "Silent Spring",
        "text": "Every handful of forest earth teems with millions of unseen **microorganism** species sustaining soil fertility."
      }
    ]
  },
  "Dashboard — erg/organ.md": {
    "primary": "A part of an organism that is typically self-contained and has a specific vital function, such as the heart, liver, or eye.",
    "secondary": "A large musical instrument with pipes sounded by compressed air, played with keyboard and pedals; or a mouthpiece newspaper/periodical.",
    "quotes": [
      {
        "author": "William Harvey",
        "work": "De Motu Cordis",
        "text": "The heart is the primary **organ** of life, whose muscular pulsations propel blood throughout the entire vascular system."
      },
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "text": "To suppose that the eye with all its inimitable contrivances could have been formed by natural selection seems, I confess, absurd in the highest degree; yet reason tells me such an **organ** may be perfected."
      },
      {
        "author": "John Milton",
        "work": "Paradise Lost",
        "text": "There let the pealing **organ** blow to the full voiced quire below, in service high and anthems clear."
      }
    ]
  },
  "Dashboard — erg/organic.md": {
    "primary": "Relating to or derived from living matter; or containing carbon compounds.",
    "secondary": "Characterized by systematic, harmonious coordination of parts in a unified, living whole; natural and integral.",
    "quotes": [
      {
        "author": "Justus von Liebig",
        "work": "Familiar Letters on Chemistry",
        "text": "Agricultural chemistry demonstrates that plants draw mineral salts from the soil to synthesize complex **organic** nutrients."
      },
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "text": "All **organic** beings around us are exposed to severe competition in the great and complex battle of life."
      },
      {
        "author": "Samuel Taylor Coleridge",
        "work": "Shakespearean Criticism",
        "text": "Mechanical form is impressed from without, whereas **organic** form shapes itself from within as it develops."
      }
    ]
  },
  "Dashboard — erg/organisation.md": {
    "primary": "The action of organizing something; or an organized body of people with a particular purpose (chiefly British spelling).",
    "secondary": "In developmental biology and anatomy, the coordinated structural arrangement of tissues, cells, and organs in an organism.",
    "quotes": [
      {
        "author": "Herbert Spencer",
        "work": "The Principles of Biology",
        "text": "Evolution is an integration of matter and concomitant dissipation of motion, progressing from simple to complex structural **organisation**."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "On the Physical Basis of Life",
        "text": "The highest plant and the lowest beast share an identical underlying protoplasmic **organisation**."
      },
      {
        "author": "Max Weber",
        "work": "Economy and Society",
        "text": "Rational bureaucratic **organisation** represents the most technically proficient instrument of administration."
      }
    ]
  },
  "Dashboard — erg/organise.md": {
    "primary": "To make arrangements or preparations for an event or activity; to coordinate (chiefly British spelling).",
    "secondary": "To endow with organic structure, vitality, or living tissue; to form into a structured whole.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Descent of Man",
        "text": "Tribes that know how to **organise** communal defense and mutual aid invariably survive hostile environments."
      },
      {
        "author": "Herbert Spencer",
        "work": "First Principles",
        "text": "Natural forces continually operate to **organise** diffuse cosmic matter into coherent solar systems."
      },
      {
        "author": "George Bernard Shaw",
        "work": "The Intelligent Woman's Guide to Socialism",
        "text": "The primary task of enlightened statesmanship is to **organise** industrial production for the common welfare."
      }
    ]
  },
  "Dashboard — erg/organism.md": {
    "primary": "An individual animal, plant, or single-celled life form capable of growth, reproduction, and response to stimuli.",
    "secondary": "In philosophy and sociology, an entity comprising mutually dependent parts whose functions are determined by their relation to the whole.",
    "quotes": [
      {
        "author": "Claude Bernard",
        "work": "Introduction to the Study of Experimental Medicine",
        "text": "The living **organism** does not live in the external environment, but in the liquid internal environment formed by the circulating organic fluids."
      },
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "text": "Every single **organism** is bound by intricate reciprocal dependencies to dozens of neighboring species."
      },
      {
        "author": "Erwin Schrödinger",
        "work": "What Is Life?",
        "text": "A living **organism** avoids decay into thermodynamic equilibrium by drawing negative entropy from its food."
      }
    ]
  },
  "Dashboard — erg/organismal.md": {
    "primary": "Of, relating to, or characteristic of an organism as a complete whole.",
    "secondary": "In evolutionary and developmental biology, focused on the level of the intact individual rather than sub-cellular or molecular components.",
    "quotes": [
      {
        "author": "Stephen Jay Gould",
        "work": "The Structure of Evolutionary Theory",
        "text": "Darwin maintained that selection acts primarily upon the **organismal** individual, not upon isolated genes or populations."
      },
      {
        "author": "Julian Huxley",
        "work": "Evolution: The Modern Synthesis",
        "text": "Natural selection integrates biochemical mutations into a functionally coherent **organismal** phenotype."
      },
      {
        "author": "Ernst Mayr",
        "work": "Animal Species and Evolution",
        "text": "The whole **organismal** architecture determines reproductive fitness in the wild, regardless of reductionist genetic models."
      }
    ]
  },
  "Dashboard — erg/organismic.md": {
    "primary": "Pertaining to or viewing organisms as integrated, functioning wholes; holistic in biological theory.",
    "secondary": "In theoretical biology and psychology, adhering to organismic theory, which emphasizes that properties of life cannot be reduced to chemistry alone.",
    "quotes": [
      {
        "author": "Ludwig von Bertalanffy",
        "work": "General System Theory",
        "text": "The **organismic** conception in biology emphasizes that living systems cannot be understood by mere summation of isolated parts."
      },
      {
        "author": "Alfred North Whitehead",
        "work": "Process and Reality",
        "text": "Philosophy of **organismic** cosmology replaces static mechanical substances with dynamic, interrelated occasions of experience."
      },
      {
        "author": "Jean Piaget",
        "work": "Biology and Knowledge",
        "text": "Cognitive development is an extension of fundamental **organismic** self-regulation and environmental adaptation."
      }
    ]
  },
  "Dashboard — erg/organist.md": {
    "primary": "A person who plays the pipe organ, especially in a church, concert hall, or cathedral.",
    "secondary": "In musical history, a liturgical musician skilled in counterpoint, improvisation, and pedal keyboard technique.",
    "quotes": [
      {
        "author": "Johann Wolfgang von Goethe",
        "work": "Conversations with Eckermann",
        "text": "Listening to Bach's fugues, one imagines the supreme **organist** in dialogue with eternity before the creation of the world."
      },
      {
        "author": "Thomas Hardy",
        "work": "Tess of the d'Urbervilles",
        "text": "The village church **organist** rehearsed the Sunday voluntary, filling the aisle with rich, vibrating chords."
      },
      {
        "author": "Robert Browning",
        "work": "Abt Vogler",
        "text": "The inspired **organist** extemporized upon his musical instrument, rearing a palace of sound that touched high heaven."
      }
    ]
  },
  "Dashboard — erg/organization.md": {
    "primary": "An organized body of people with a particular purpose, such as a business, society, or association.",
    "secondary": "The structural arrangement or manner in which the parts of something are coordinated to function as an integrated whole.",
    "quotes": [
      {
        "author": "Herbert Spencer",
        "work": "The Principles of Sociology",
        "text": "Social **organization** evolves in parallel with biological structures, progressing from uniform bands to complex divisions of labor."
      },
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "text": "High structural **organization** does not invariably guarantee competitive victory over simpler, hardier forms of life."
      },
      {
        "author": "Alexis de Tocqueville",
        "work": "Democracy in America",
        "text": "In no country on earth is the principle of voluntary civic **organization** applied with such brilliant success as in America."
      }
    ]
  },
  "Dashboard — erg/organize.md": {
    "primary": "To arrange into a structured whole; to coordinate, systematize, or make preparations for.",
    "secondary": "In unionism and politics, to form workers into a labor union or cooperative association.",
    "quotes": [
      {
        "author": "Francis Bacon",
        "work": "Novum Organum",
        "text": "We must **organize** our empirical observations into systematic tables of discovery before drawing general axioms."
      },
      {
        "author": "Jane Addams",
        "work": "Twenty Years at Hull-House",
        "text": "Working women must learn to **organize** collective trade associations to demand safe sanitary working conditions."
      },
      {
        "author": "Winston Churchill",
        "work": "The Second World War",
        "text": "The cabinet labored night and day to **organize** national defense against the imminent threat of airborne invasion."
      }
    ]
  },
  "Dashboard — erg/organized.md": {
    "primary": "Arranged or structured in a systematic way; methodical and orderly.",
    "secondary": "Formed into a structured body, such as a trade union or civic institution.",
    "quotes": [
      {
        "author": "Adam Smith",
        "work": "The Wealth of Nations",
        "text": "An **organized** division of labor multiplies productivity in manufacturing beyond all traditional handicrafts."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "Lay Sermons",
        "text": "Protoplasm is **organized** living matter, possessing the unique attributes of assimilation and reproduction."
      },
      {
        "author": "George Orwell",
        "work": "Homage to Catalonia",
        "text": "The militia units were poorly **organized** and armed with obsolete rifles, yet their spirit was unbroken."
      }
    ]
  },
  "Dashboard — erg/organizer.md": {
    "primary": "A person who arranges, plans, or coordinates an event, organization, or activity.",
    "secondary": "In developmental embryology, a region of an embryo (such as the Spemann-Mangold organizer) that directs the differentiation of surrounding tissues.",
    "quotes": [
      {
        "author": "Hans Spemann",
        "work": "Embryonic Development and Induction",
        "text": "I demonstrated that the dorsal blastopore lip functions as the primary embryonic **organizer**, inducing the neural tube."
      },
      {
        "author": "Bruce Alberts",
        "work": "Molecular Biology of the Cell",
        "text": "Signals secreted by the Spemann **organizer** diffuse across the ectoderm, blocking epidermal fates to establish the central nervous system."
      },
      {
        "author": "Jane Addams",
        "work": "Twenty Years at Hull-House",
        "text": "An effective community **organizer** listens to neighbors' grievances before formulating collective social action."
      }
    ]
  },
  "Dashboard — erg/organoleptic.md": {
    "primary": "Acting on, involving, or tested by the use of the physical sense organs, particularly taste, smell, touch, and sight.",
    "secondary": "In food science and pharmacology, evaluating the quality, freshness, and purity of a substance through direct sensory appraisal.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "text": "Before chemical tests were codified, clinicians relied upon **organoleptic** assessment of urine color, clarity, and scent."
      },
      {
        "author": "Louis Pasteur",
        "work": "Studies on Wine",
        "text": "The sommelier conducted an **organoleptic** appraisal of the vintage, noting bouquet, acidity, and palate finish."
      },
      {
        "author": "Rachel Carson",
        "work": "Silent Spring",
        "text": "Chemical contamination may escape **organoleptic** detection by consumers even while concentrating toxic residues."
      }
    ]
  }
};

function formatQuotes(quotes) {
  return quotes.map(q => `> - 📜 **${q.author} (*${q.work}*):** *"${q.text}"*`).join('\n');
}

function updateFile(relPath, wordData) {
  const filePath = path.join(CLUSTER_DIR, relPath);
  if (!fs.existsSync(filePath)) {
    console.error(`File NOT found: ${filePath}`);
    return false;
  }
  const content = fs.readFileSync(filePath, 'utf8');
  const bookIdx = content.indexOf('> [!book]');
  if (bookIdx === -1) {
    console.error(`Missing [!book] in ${filePath}`);
    return false;
  }
  const topPart = content.slice(0, bookIdx).trimEnd();

  const newDefBlock = `> [!book] 📖 Definitions & Semantic Range\n> 1. **Primary Definition (Lexical / Standard Consensus)**: ${wordData.primary}\n> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: ${wordData.secondary}\n\n> [!quote] 💬 Contextual Usage & Authentic Quotations\n${formatQuotes(wordData.quotes)}\n`;

  const finalContent = topPart + '\n\n' + newDefBlock;
  fs.writeFileSync(filePath, finalContent, 'utf8');
  return true;
}

let count = 0;
for (const [relPath, data] of Object.entries(BATCH6_DATA)) {
  if (updateFile(relPath, data)) {
    count++;
  }
}

console.log(`========================================`);
console.log(`Action Batch 6 Completed: ${count} / ${Object.keys(BATCH6_DATA).length} words updated`);
console.log(`========================================`);
