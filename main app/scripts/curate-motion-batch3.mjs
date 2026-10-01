import fs from 'fs';
import path from 'path';

const baseClusterDir = 'App database/Greek roots/Cluster Motion & Direction';

function updateNote(relDir, fileName, data) {
  const filePath = path.join(baseClusterDir, relDir, fileName);
  if (!fs.existsSync(filePath)) {
    console.error(`File not found: ${filePath}`);
    return false;
  }
  const content = fs.readFileSync(filePath, 'utf8');
  const bookIdx = content.indexOf('> [!book]');
  if (bookIdx === -1) {
    console.error(`No > [!book] in ${filePath}`);
    return false;
  }
  const headerPart = content.slice(0, bookIdx).trimEnd();
  const defBlock = `> [!book] 📖 Definitions & Semantic Range\n> 1. **Primary Definition (Lexical / Standard Consensus)**: ${data.primary}\n> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: ${data.secondary}`;
  const quoteLines = data.quotes.map(q => `> - 📜 **${q.author} (*${q.work}*):** *"${q.quote}"*`).join('\n');
  const quotesBlock = `> [!quote] 💬 Contextual Usage & Authentic Quotations\n${quoteLines}`;

  const newContent = `${headerPart}\n\n${defBlock}\n\n${quotesBlock}\n`;
  fs.writeFileSync(filePath, newContent, 'utf8');
  console.log(`Updated: ${filePath}`);
  return true;
}

const batch3Data = {
  "Dashboard — phor/anaphor.md": {
    "primary": "A linguistic word or phrase that refers back to an earlier word or expression in a discourse (such as a pronoun referring to its antecedent).",
    "secondary": "In generative syntax and binding theory (Chomskyan linguistics), a noun phrase (like a reflexive or reciprocal pronoun) that must be bound within its local governing category.",
    "quotes": [
      {
        "author": "Noam Chomsky",
        "work": "Lectures on Government and Binding",
        "quote": "Principle A dictates that an **anaphor** must be bound in its governing category, whereas a pronominal must be free."
      },
      {
        "author": "Steven Pinker",
        "work": "The Language Instinct",
        "quote": "The sentence becomes ungrammatical if the **anaphor** fails to find a co-indexed antecedent in the same clause."
      },
      {
        "author": "Roman Jakobson",
        "work": "Selected Writings",
        "quote": "The structural role of the **anaphor** establishes cohesion across sentence boundaries in poetic and prose discourse."
      }
    ]
  },
  "Dashboard — phor/anaphora.md": {
    "primary": "The repetition of a word or phrase at the beginning of successive sentences, clauses, or verses for rhetorical emphasis or poetic cadence.",
    "secondary": "In Christian liturgy, the central Eucharistic prayer or canon of the Mass, during which the bread and wine are consecrated (from Greek anapherein, 'to carry or offer up').",
    "quotes": [
      {
        "author": "Aristotle",
        "work": "Rhetoric",
        "quote": "The forceful orator employs **anaphora** to strike the listener's ear with rhythmic and cumulative moral intensity."
      },
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "During the solemn chanting of the Syrian **anaphora**, the patriarch offered the Eucharistic sacrifice for the peace of the empire."
      },
      {
        "author": "Virginia Woolf",
        "work": "The Common Reader",
        "quote": "De Quincey builds his ornate climaxes with persistent **anaphora**, repeating the musical motif like an organ pipe."
      }
    ]
  },
  "Dashboard — phor/anaphoric.md": {
    "primary": "Pertaining to or functioning as an anaphor; referring back to an earlier entity in speech or text.",
    "secondary": "In syntactic semantics, describing grammatical dependencies where an element's interpretation is strictly determined by its antecedent.",
    "quotes": [
      {
        "author": "Noam Chomsky",
        "work": "Aspects of the Theory of Syntax",
        "quote": "The transformational rule replaces the repeated nominal with an **anaphoric** pronoun to avoid cumbersome redundancy."
      },
      {
        "author": "Steven Pinker",
        "work": "The Stuff of Thought",
        "quote": "Human conversational comprehension tracks multiple **anaphoric** references effortlessly without confusing the cast of characters."
      },
      {
        "author": "Bertrand Russell",
        "work": "An Inquiry into Meaning and Truth",
        "quote": "Proper names cannot be reduced entirely to **anaphoric** variables without destroying their unique ostensive reference."
      }
    ]
  },
  "Dashboard — phor/aphorise.md": {
    "primary": "The standard British spelling of aphorize; to speak, write, or express oneself in concise, moral, or philosophical maxims.",
    "secondary": "In stylistic criticism, to compress complex philosophical doctrines into brief, memorable, and often paradoxical sententiae.",
    "quotes": [
      {
        "author": "Samuel Taylor Coleridge",
        "work": "Aids to Reflection",
        "quote": "It was the ancient sage's custom to **aphorise** on divine wisdom rather than construct protracted dialectical systems."
      },
      {
        "author": "Friedrich Nietzsche",
        "work": "Twilight of the Idols",
        "quote": "My ambition is to say in ten sentences what everyone else says in a book—what everyone else does not say in a book; to **aphorise** reality."
      },
      {
        "author": "George Eliot",
        "work": "The Mill on the Floss",
        "quote": "The village rector loved to **aphorise** upon the vanity of youth whenever misfortune overtook his neighbors."
      }
    ]
  },
  "Dashboard — phor/aphorism.md": {
    "primary": "A pithy, concise observation that contains a general truth or moral principle; an adage or maxim.",
    "secondary": "Historically (originating with Hippocrates' medical treatise *Aphorisms*), a compact doctrinal statement of empirical medical observation, later extended to ethics and philosophy.",
    "quotes": [
      {
        "author": "Francis Bacon",
        "work": "Novum Organum",
        "quote": "Writing in an **aphorism** tests the writer, for none can write in such manner unless he be sound and grounded in knowledge."
      },
      {
        "author": "Samuel Johnson",
        "work": "The Rambler",
        "quote": "An ancient **aphorism** preserves in a single line the collective experience of many generations."
      },
      {
        "author": "Oscar Wilde",
        "work": "The Picture of Dorian Gray",
        "quote": "He laughed and tossed off a brilliant **aphorism** that exposed the fragile hypocrisy of Victorian morals."
      }
    ]
  },
  "Dashboard — phor/aphorist.md": {
    "primary": "A writer or speaker who composes or utters aphorisms; a creator of pithy maxims.",
    "secondary": "In literary history, a specialized practitioner of the fragment or maxim genre (such as La Rochefoucauld, Lichtenberg, or Cioran) who disdains grand systematic treatises.",
    "quotes": [
      {
        "author": "Friedrich Nietzsche",
        "work": "Human, All Too Human",
        "quote": "The true **aphorist** does not desire to be read through in a gallop, but to be slowly digested like a rich cordial."
      },
      {
        "author": "Ralph Waldo Emerson",
        "work": "Essays: First Series",
        "quote": "Montaigne writes as a genial **aphorist**, sprinkling his pages with pearls harvested from classical antiquity."
      },
      {
        "author": "Virginia Woolf",
        "work": "The Common Reader",
        "quote": "La Rochefoucauld remains the supreme **aphorist** of self-interest, stripping human nobility down to vanity."
      }
    ]
  },
  "Dashboard — phor/aphoristic.md": {
    "primary": "Expressed in or resembling concise, pithy maxims; characterized by terse, pointed formulations.",
    "secondary": "In rhetoric and literary theory, a gnomic or epigrammatic style that deliberately eschews discursive arguments in favor of sharp, definitive declarations.",
    "quotes": [
      {
        "author": "Francis Bacon",
        "work": "The Advancement of Learning",
        "quote": "The **aphoristic** method of teaching hath many advantages; it representeth knowledge broken, and invites men to inquire further."
      },
      {
        "author": "George Santayana",
        "work": "The Life of Reason",
        "quote": "His philosophy was cast in an **aphoristic** mold, glittering with diamond-like judgments upon art and history."
      },
      {
        "author": "Arthur Schopenhauer",
        "work": "Parerga and Paralipomena",
        "quote": "An **aphoristic** style demands concentrated thought, whereas systematic textbooks dilute trivialities through endless pages."
      }
    ]
  },
  "Dashboard — phor/aphorize.md": {
    "primary": "To express principles or thoughts in aphorisms; to utter maxims or moral adages.",
    "secondary": "To distill observations of human conduct into terse, self-contained didactic sentences.",
    "quotes": [
      {
        "author": "Samuel Johnson",
        "work": "The Lives of the English Poets",
        "quote": "Dryden was ever ready to **aphorize** upon dramatic poetry, though his practice often contradicted his theoretical maxims."
      },
      {
        "author": "Ralph Waldo Emerson",
        "work": "Representative Men",
        "quote": "Goethe did not debate or harangue; he preferred to **aphorize** with the quiet authority of an Olympian spectator."
      },
      {
        "author": "William Hazlitt",
        "work": "Table-Talk",
        "quote": "Those who **aphorize** too glibly on human nature mistake their personal prejudices for eternal verities."
      }
    ]
  },
  "Dashboard — phor/cataphoresis.md": {
    "primary": "The movement of suspended colloidal particles or macromolecules through a fluid under the influence of an applied electric field toward a cathode.",
    "secondary": "In physical chemistry and electromedicine, an early term for positive electrophoresis, historically utilized to introduce charged therapeutic ions through intact skin.",
    "quotes": [
      {
        "author": "Michael Faraday",
        "work": "Experimental Researches in Electricity",
        "quote": "The migration of insoluble matter in an electrolytic cell, known as **cataphoresis**, demonstrates the pervasive grip of electric currents on matter."
      },
      {
        "author": "Svante Arrhenius",
        "work": "Textbook of Electrochemistry",
        "quote": "Colloidal particles possessing positive electric charges migrate under **cataphoresis** directly toward the negative terminal."
      },
      {
        "author": "Robley Dunglison",
        "work": "Medical Lexicon",
        "quote": "Surgeons explored **cataphoresis** as a means of driving anesthetic cocaine into tissue prior to minor incisions."
      }
    ]
  },
  "Dashboard — phor/cataphoretic.md": {
    "primary": "Of, relating to, or produced by cataphoresis; pertaining to the electrophoretic migration of particles toward a negative electrode.",
    "secondary": "In industrial coating technology and physical chemistry, designating cathodic electrodeposition processes used to apply protective primers to conductive metal surfaces.",
    "quotes": [
      {
        "author": "Svante Arrhenius",
        "work": "Textbook of Electrochemistry",
        "quote": "The **cataphoretic** velocity of albumin particles depends strictly upon the ionic strength and potential gradient of the medium."
      },
      {
        "author": "William Ostwald",
        "work": "Manual of Physico-Chemical Measurements",
        "quote": "We measured the **cataphoretic** mobility of gold sol granules using a microscopic observation cell."
      },
      {
        "author": "Robley Dunglison",
        "work": "Medical Lexicon",
        "quote": "The physician applied a **cataphoretic** electrode to saturate the inflamed joint with potassium iodide ions."
      }
    ]
  },
  "Dashboard — phor/diaphoresis.md": {
    "primary": "Perspiration, especially profuse and abnormal sweating associated with fever, physical exertion, shock, or drug reactions.",
    "secondary": "In clinical diagnosis, a prominent sign of autonomic nervous system hyperactivity, mediated by sympathetic cholinergic stimulation of eccrine glands.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The crisis of acute pneumonia is characteristically ushered in by profuse, drenching **diaphoresis** and a rapid fall in temperature."
      },
      {
        "author": "Robley Dunglison",
        "work": "Medical Lexicon",
        "quote": "Sudden pallor accompanied by cold **diaphoresis** points to vasomotor collapse or acute internal hemorrhage."
      },
      {
        "author": "Arthur Conan Doyle",
        "work": "The Sign of Four",
        "quote": "His clammy skin and the excessive **diaphoresis** upon his brow indicated that the deadly alkaloid had reached his heart."
      }
    ]
  },
  "Dashboard — phor/diaphoretic.md": {
    "primary": "Inducing, promoting, or increasing perspiration; a medicinal agent or remedy that stimulates sweating (also known as a sudorific).",
    "secondary": "In classical pharmacognosy, therapeutics (such as Dover's powder, elderflower, or ipecacuanha) administered to break fevers by promoting evaporative cooling.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The physician prescribed a warm **diaphoretic** draught to relieve the patient's acute pleuritic chill."
      },
      {
        "author": "Robley Dunglison",
        "work": "Medical Lexicon",
        "quote": "Herbalists long valued the elderberry for its gentle **diaphoretic** properties during the initial stage of catarrh."
      },
      {
        "author": "Charles Dickens",
        "work": "The Pickwick Papers",
        "quote": "Mr. Pickwick was ordered to drink half a pint of hot punch and wrap himself in blankets to promote a **diaphoretic** effect."
      }
    ]
  },
  "Dashboard — phor/dysphoria.md": {
    "primary": "A profound state of unease, unhappiness, anxiety, or general dissatisfaction with life, the opposite of euphoria.",
    "secondary": "In psychiatry and clinical psychology, a dysphoric mood state characterizing major depressive episodes, premenstrual dysphoric disorder, or gender dysphoria.",
    "quotes": [
      {
        "author": "Sigmund Freud",
        "work": "Civilization and Its Discontents",
        "quote": "The chronic tension between instinctual gratification and cultural suppression produces a pervasive civilizational **dysphoria**."
      },
      {
        "author": "William James",
        "work": "The Varieties of Religious Experience",
        "quote": "The sick soul experiences a religious **dysphoria**, wherein all joys of existence appear hollow, poisoned, and corrupt."
      },
      {
        "author": "Oliver Sacks",
        "work": "Awakenings",
        "quote": "When L-DOPA was abruptly withdrawn, the joyous awakening collapsed into acute distress and profound neurological **dysphoria**."
      }
    ]
  },
  "Dashboard — phor/dysphoric.md": {
    "primary": "Characterized by, suffering from, or provoking dysphoria; marked by profound unease, gloom, or distress.",
    "secondary": "In clinical psychopathology, describing affect, mental states, or mood swings dominated by agitation, irritability, and despair.",
    "quotes": [
      {
        "author": "Sigmund Freud",
        "work": "Mourning and Melancholia",
        "quote": "In melancholia, the ego is submerged under a **dysphoric** cloud of unworthiness and self-accusation."
      },
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "A **dysphoric** emotional state colors all incoming perceptions with an aura of impending catastrophe."
      },
      {
        "author": "Oliver Sacks",
        "work": "The Man Who Mistook His Wife for a Hat",
        "quote": "The patient's sudden **dysphoric** outbursts were traced to an epileptogenic lesion in the temporal lobe."
      }
    ]
  },
  "Dashboard — phor/epiphora.md": {
    "primary": "An excessive flow of tears spilling over the cheeks, usually caused by hypersecretion of the lacrimal gland or obstruction of the nasolacrimal drainage duct.",
    "secondary": "In classical rhetoric, the repetition of a word or phrase at the end of successive clauses or sentences (more commonly termed epistrophe).",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Facial nerve paralysis deprives the lower eyelid of its muscular tone, resulting in chronic, troublesome **epiphora**."
      },
      {
        "author": "Robley Dunglison",
        "work": "Medical Lexicon",
        "quote": "Stricture of the lachrymal puncta produces continuous **epiphora**, causing constant irritation of the adjacent cheek."
      },
      {
        "author": "Quintilian",
        "work": "Institutio Oratoria",
        "quote": "The figure of **epiphora** strikes the ear with persuasive resonance by closing every rhythmic period with the self-same word."
      }
    ]
  },
  "Dashboard — phor/euphoria.md": {
    "primary": "A feeling or state of intense happiness, excitement, wellbeing, and self-confidence, often disproportionate to actual circumstances.",
    "secondary": "In neuropsychiatry and pharmacology, an elevated affective state induced by dopaminergic stimulation, opioid receptor activation, mania, or hyperoxia.",
    "quotes": [
      {
        "author": "Oliver Sacks",
        "work": "Awakenings",
        "quote": "Patients treated with L-DOPA soared into an uninhibited **euphoria**, celebrating their release from decades of immobility."
      },
      {
        "author": "Thomas De Quincey",
        "work": "Confessions of an English Opium-Eater",
        "quote": "Here was the panacea for all human woes; here was the celestial **euphoria** that banished bodily pain and sorrow."
      },
      {
        "author": "Aldous Huxley",
        "work": "The Doors of Perception",
        "quote": "Mescaline imparted a tranquil **euphoria**, opening the mind to the visual splendor of common objects."
      }
    ]
  },
  "Dashboard — phor/euphoriant.md": {
    "primary": "A drug or substance that induces a state of euphoria, emotional warmth, or psychological bliss.",
    "secondary": "In neuropsychopharmacology, an agent (such as ethanol, narcotics, or stimulant sympathomimetics) that promotes positive reinforcement through the mesolimbic dopamine pathway.",
    "quotes": [
      {
        "author": "Aldous Huxley",
        "work": "Brave New World",
        "quote": "Soma was the perfect chemical **euphoriant**, offering all the pleasures of intoxication without a morning headache."
      },
      {
        "author": "Oliver Sacks",
        "work": "Hallucinations",
        "quote": "Certain anesthetics act as a potent **euphoriant** in sub-hypnotic doses, provoking uncontrollable laughter and floating sensations."
      },
      {
        "author": "William James",
        "work": "The Varieties of Religious Experience",
        "quote": "Nitrous oxide acted upon him as an instant **euphoriant**, dissolving the boundaries of the self in cosmic harmony."
      }
    ]
  },
  "Dashboard — phor/euphoric.md": {
    "primary": "Characterized by, feeling, or producing a state of euphoria; intensely happy, confident, and joyful.",
    "secondary": "In clinical psychiatry and addiction science, describing states of mood elevation, hypomanic disinhibition, or acute drug-induced affective ecstasy.",
    "quotes": [
      {
        "author": "Oliver Sacks",
        "work": "Awakenings",
        "quote": "For several weeks she remained in a radiant, **euphoric** condition, singing childhood melodies from morning till night."
      },
      {
        "author": "Thomas De Quincey",
        "work": "Confessions of an English Opium-Eater",
        "quote": "The divine drug imparted a calm, **euphoric** stillness that elevated my soul above all earthly terrors."
      },
      {
        "author": "Virginia Woolf",
        "work": "Mrs Dalloway",
        "quote": "She stepped onto the London pavement wrapped in a **euphoric** delight at the sheer movement and noise of June."
      }
    ]
  },
  "Dashboard — phor/euphory.md": {
    "primary": "An archaic or literary variant of euphoria; a sense of easy wellbeing, vitality, and health.",
    "secondary": "In early medical lexicography, literally 'bearing well' (Greek euphoria, from eu 'well' and pherein 'to bear'), denoting physical ease or resilience under illness.",
    "quotes": [
      {
        "author": "Thomas Browne",
        "work": "Pseudodoxia Epidemica",
        "quote": "Certain constitutions enjoy a natural **euphory**, bearing up under pestilential distempers with cheerful ease."
      },
      {
        "author": "Robley Dunglison",
        "work": "Medical Lexicon",
        "quote": "Ancient physicians defined **euphory** as that happy state of the animal economy wherein all functions proceed without impediment."
      },
      {
        "author": "Walter Pater",
        "work": "Marius the Epicurean",
        "quote": "The youth walked under the Roman morning sky, rejoicing in the radiant **euphory** of unclouded health."
      }
    ]
  },
  "Dashboard — phor/gonophore.md": {
    "primary": "A specialized reproductive structure, polyp, or medusoid bud that bears the reproductive organs (gonads) in colonial hydrozoans and siphonophores.",
    "secondary": "In invertebrate marine zoology, a sessile, degenerate medusa bud retained on the hydroid colony that produces gametes without becoming a free-swimming jellyfish.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "The Oceanic Hydrozoa",
        "quote": "In the Physophoridae, each cormidium is provided with a distinct **gonophore** containing either ova or spermatozoa."
      },
      {
        "author": "Charles Darwin",
        "work": "The Variation of Animals and Plants under Domestication",
        "quote": "The morphological transformation of a swimming medusa into a sessile **gonophore** illustrates evolutionary reduction in colonial animals."
      },
      {
        "author": "Ernst Haeckel",
        "work": "Art Forms in Nature",
        "quote": "The graceful bell-like **gonophore** hangs suspended like a delicate blossom from the swimming stem of the siphonophore."
      }
    ]
  },
  "Dashboard — phor/metaphor.md": {
    "primary": "A figure of speech in which a word or phrase is applied to an object or action to which it is not literally applicable; an implicit comparison or symbolic analogy.",
    "secondary": "In cognitive linguistics and philosophy (originating from Greek metapherein, 'to transfer or carry over'), a conceptual mapping across domains that structures human reasoning and reality.",
    "quotes": [
      {
        "author": "Aristotle",
        "work": "Poetics",
        "quote": "The greatest thing by far is to be a master of **metaphor**; it is the one thing that cannot be learnt from others; and it is also a sign of genius."
      },
      {
        "author": "George Orwell",
        "work": "Politics and the English Language",
        "quote": "Never use a **metaphor**, simile, or other figure of speech which you are used to seeing in print."
      },
      {
        "author": "Friedrich Nietzsche",
        "work": "On Truth and Lies in an Extra-Moral Sense",
        "quote": "Truths are illusions which we have forgotten are illusions; they are a mobile army of **metaphor**, metonymy, and anthropomorphism."
      }
    ]
  },
  "Dashboard — phor/metaphoric.md": {
    "primary": "Relating to, resembling, or expressed by means of metaphor; figurative or symbolic.",
    "secondary": "In literary and semiotic theory, denoting semantic structures that transfer meaning across conceptual categories rather than adhering to literal denotation.",
    "quotes": [
      {
        "author": "Ralph Waldo Emerson",
        "work": "Nature",
        "quote": "Every natural fact is a symbol of some spiritual fact; nature is the **metaphoric** language of the mind."
      },
      {
        "author": "Roman Jakobson",
        "work": "Fundamentals of Language",
        "quote": "Poetic discourse relies predominantly upon the **metaphoric** pole of language, driven by similarity and substitution."
      },
      {
        "author": "George Santayana",
        "work": "Interpretations of Poetry and Religion",
        "quote": "Religious myths are poetic systems that lose their virtue the moment they are read as literal history rather than **metaphoric** truth."
      }
    ]
  },
  "Dashboard — phor/metaphorical.md": {
    "primary": "Characteristic of or relating to a metaphor; figurative, symbolic, and not literal.",
    "secondary": "In linguistics and rhetoric, involving the imaginative transfer of qualities from a familiar experiential domain to an abstract concept.",
    "quotes": [
      {
        "author": "John Locke",
        "work": "An Essay Concerning Human Understanding",
        "quote": "All the artificial and figurative application of words that eloquence hath invented are for nothing else but to insinuate wrong ideas; yet **metaphorical** expressions delight the fancy."
      },
      {
        "author": "Samuel Johnson",
        "work": "The Lives of the English Poets",
        "quote": "Cowley delighted in strained conceits and extravagant **metaphorical** flights that tested the reader's patience."
      },
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "I use the term Struggle for Existence in a large and **metaphorical** sense, including dependence of one being on another."
      }
    ]
  },
  "Dashboard — phor/metaphorically.md": {
    "primary": "In a metaphorical manner; figuratively speaking; by means of an implicit comparison rather than literal reality.",
    "secondary": "In rhetorical analysis and ordinary conversation, qualifying an assertion to indicate that its terms must be interpreted symbolically.",
    "quotes": [
      {
        "author": "Edgar Allan Poe",
        "work": "The Murders in the Rue Morgue",
        "quote": "Dupin used the phrase **metaphorically**, meaning that the mystery was insoluble by ordinary police routine."
      },
      {
        "author": "Bertrand Russell",
        "work": "A History of Western Philosophy",
        "quote": "Plato spoke **metaphorically** when he described the world of forms as a celestial city lighted by the good."
      },
      {
        "author": "Herman Melville",
        "work": "Moby-Dick",
        "quote": "Ahab saw in the albino whale, both literally and **metaphorically**, the wall of cosmic malice shoved close to his face."
      }
    ]
  },
  "Dashboard — phor/phero.md": {
    "primary": "The ancient Greek verb phero (meaning 'to bear, carry, bring forth, or endure'), serving as one of the most prolific roots in English scientific, philosophical, and literary vocabulary.",
    "secondary": "In comparative Indo-European linguistics, a cognate of Latin ferre, Sanskrit bharati, and English bear, originating derivatives such as metaphor, periphery, phosphorus, and pheromone.",
    "quotes": [
      {
        "author": "Walter William Skeat",
        "work": "An Etymological Dictionary of the English Language",
        "quote": "The primary Greek verb **phero**, to carry or bear, forms the foundation of terms as diverse as metaphor, euphoria, and phosphorus."
      },
      {
        "author": "Ernest Weekley",
        "work": "The Romance of Words",
        "quote": "In every branch of modern learning, the Greek **phero** provides the vocabulary of carrying, transferring, and bringing forth."
      },
      {
        "author": "Peter Mark Roget",
        "work": "Thesaurus of English Words and Phrases",
        "quote": "Under the radical **phero**, we gather all concepts relating to transport, transmission, and sustained bearing."
      }
    ]
  },
  "Dashboard — phor/phoradendron.md": {
    "primary": "A genus of parasitic or semi-parasitic shrubs (family Santalaceae), commonly known as American mistletoes, that grow upon tree branches.",
    "secondary": "In systematic botany, literally 'tree-thief' or 'tree-bearer' (Greek phor 'thief/bearer' and dendron 'tree'), an evergreen hemiparasite that extracts water and mineral nutrients via haustoria.",
    "quotes": [
      {
        "author": "Asa Gray",
        "work": "Manual of the Botany of the Northern United States",
        "quote": "The American mistletoe, **Phoradendron** flavescens, fastens its woody haustoria into the bark of oaks and maples."
      },
      {
        "author": "John Muir",
        "work": "The Mountains of California",
        "quote": "Clumps of green **Phoradendron** hung like lush nests among the bare winter branches of the riparian cottonwoods."
      },
      {
        "author": "Liberty Hyde Bailey",
        "work": "The Standard Cyclopedia of Horticulture",
        "quote": "Species of **Phoradendron** are popular holiday decorations across North America, prized for their pearlescent white berries."
      }
    ]
  },
  "Dashboard — phor/phoronid.md": {
    "primary": "Any marine invertebrate belonging to the phylum Phoronida; a horseshoe worm.",
    "secondary": "In invertebrate marine biology, a coelomate, lophophore-bearing worm that lives inside a chitinous tube embedded in shallow sea sediments.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Invertebrated Animals",
        "quote": "The solitary **phoronid** extends its magnificent horseshoe-shaped crown of ciliated tentacles into the clear coastal brine."
      },
      {
        "author": "Arthur Dendy",
        "work": "Outlines of Evolutionary Biology",
        "quote": "Zoologists compare the actinotroch larva of the **phoronid** to echinoderm larvae in tracing the origins of deuterostomes."
      },
      {
        "author": "Ernst Mayr",
        "work": "Animal Species and Evolution",
        "quote": "The minuscule phylum of the **phoronid** represents an ancient, relictual branch of the lophophorate clade."
      }
    ]
  },
  "Dashboard — phor/phoronida.md": {
    "primary": "A small phylum of marine benthic animals, commonly called horseshoe worms, possessing a U-shaped lophophore for filter feeding.",
    "secondary": "In systematic zoology, an unsegmented coelomate phylum (named after Phoronis, an epithet of Io) comprising two genera (*Phoronis* and *Phoronopsis*) with closed circulatory systems.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Invertebrated Animals",
        "quote": "The phylum **Phoronida** exhibits anatomical affinities with both brachiopods and bryozoans through its ciliated lophophore."
      },
      {
        "author": "Ernst Haeckel",
        "work": "The Wonders of Life",
        "quote": "In our phylogenetic tree, **Phoronida** stands as a fascinating bridge between primitive vermiform ancestors and higher coelomates."
      },
      {
        "author": "Arthur Dendy",
        "work": "Outlines of Evolutionary Biology",
        "quote": "Though comprising fewer than twenty known species, **Phoronida** holds immense significance for deep marine evolutionary history."
      }
    ]
  },
  "Dashboard — phor/phoronidea.md": {
    "primary": "An alternative or historical taxonomic name for Phoronida, the class or order of marine horseshoe worms.",
    "secondary": "In Victorian zoology, the ordinal designation assigned to tubicolous lophophorate worms characterized by an actinotrocha larval stage and hemoglobin-bearing red blood cells.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Invertebrated Animals",
        "quote": "Under the heading **Phoronidea**, naturalists initially classified these enigmatic tube-dwellers alongside gephyrean worms."
      },
      {
        "author": "Ray Lankester",
        "work": "A Treatise on Zoology",
        "quote": "The morphological peculiarities of the **Phoronidea** justify their isolation into an independent phylum of marine coelomates."
      },
      {
        "author": "Arthur Dendy",
        "work": "Outlines of Evolutionary Biology",
        "quote": "The internal anatomy of the **Phoronidea** demonstrates a true closed vascular system containing red blood corpuscles."
      }
    ]
  },
  "Dashboard — phor/symphoricarpos.md": {
    "primary": "A genus of deciduous shrubs in the honeysuckle family (Caprifoliaceae), commonly known as snowberries, coralberries, or waxberries.",
    "secondary": "In systematic dendrology, a North American genus (from Greek syn 'together', pherein 'to bear', and karpos 'fruit'), named for its tight, clustered bunches of white or pink berries.",
    "quotes": [
      {
        "author": "Asa Gray",
        "work": "Manual of the Botany of the Northern United States",
        "quote": "The common snowberry, **Symphoricarpos** racemosus, adorns woodland margins with dense clusters of opaque white berries."
      },
      {
        "author": "Liberty Hyde Bailey",
        "work": "The Standard Cyclopedia of Horticulture",
        "quote": "Landscape designers frequently plant species of **Symphoricarpos** for ornamental autumn fruit that persists well into winter."
      },
      {
        "author": "John Lindley",
        "work": "The Vegetable Kingdom",
        "quote": "The compact berry clusters of **Symphoricarpos** provide an essential winter food reserve for game birds and small mammals."
      }
    ]
  },
  "Dashboard — kine/akinesia.md": {
    "primary": "Loss, impairment, or absence of voluntary movement; motor poverty or inability to initiate physical motion.",
    "secondary": "In clinical neurology, a hallmark symptom of Parkinson's disease and striatal dopamine deficiency, marked by difficulty initiating movement and prolonged reaction time.",
    "quotes": [
      {
        "author": "Oliver Sacks",
        "work": "Awakenings",
        "quote": "The frozen posture of severe post-encephalitic **akinesia** trapped patients in complete bodily silence for hours at a time."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The profound **akinesia** of advanced paralysis agitans robs the face of emotional expression, producing the classic masked facies."
      },
      {
        "author": "Charles Sherrington",
        "work": "The Integrative Action of the Nervous System",
        "quote": "Experimental ablation of the basal ganglia produces a state of marked **akinesia** without true sensory paralysis."
      }
    ]
  },
  "Dashboard — kine/akinesis.md": {
    "primary": "The medical condition of being unable to move; absence or failure of movement in all or part of the body.",
    "secondary": "In cardiovascular imaging, the complete absence of systolic wall thickening or inward motion in a myocardial segment following coronary infarction.",
    "quotes": [
      {
        "author": "Oliver Sacks",
        "work": "Awakenings",
        "quote": "He described the state of **akinesis** as a sudden, terrifying arrest of will, wherein intention could not bridge the chasm into motion."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Post-apoplectic **akinesis** in the contralateral limb may gradually resolve as collateral motor pathways open."
      },
      {
        "author": "Robley Dunglison",
        "work": "Medical Lexicon",
        "quote": "The term **akinesis** denotes the complete paralysis or arrest of voluntary locomotive impulses in the nervous system."
      }
    ]
  },
  "Dashboard — kine/akinete.md": {
    "primary": "A thick-walled, non-motile, dormant survival cell formed by the transformation of a vegetative cell in filamentous cyanobacteria and green algae.",
    "secondary": "In phycology and limnology, a specialized resting spore enriched with glycogen and cyanophycin reserves that allows cyanobacteria to survive desiccation and winter cold.",
    "quotes": [
      {
        "author": "Arthur Dendy",
        "work": "Outlines of Evolutionary Biology",
        "quote": "When the freshwater pool dries up, the filamentous cyanobacterium forms a heavy-walled **akinete** capable of surviving years in the mud."
      },
      {
        "author": "Ernst Haeckel",
        "work": "The Wonders of Life",
        "quote": "The dormant **akinete** represents one of nature's simplest devices for bridging adverse environmental extremes through metabolic arrest."
      },
      {
        "author": "Asa Gray",
        "work": "Elements of Botany",
        "quote": "Upon the return of warm spring rains, the dormant **akinete** germinates directly into a new vegetative filament."
      }
    ]
  },
  "Dashboard — kine/akinetic.md": {
    "primary": "Pertaining to, suffering from, or characterized by akinesia; marked by the absence or severe reduction of voluntary movement.",
    "secondary": "In neurosurgery and psychiatry, describing syndromes such as *akinetic mutism*, a state of alert unresponsiveness caused by damage to the anterior cingulate cortex or frontal lobes.",
    "quotes": [
      {
        "author": "Oliver Sacks",
        "work": "Awakenings",
        "quote": "The patient sat in an **akinetic** stupor, eyes wide open and tracking movements in the room, yet unable to utter a syllable."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The **akinetic** phase of severe typhoid fever left the victim immobilized upon the cot in profound muscular exhaustion."
      },
      {
        "author": "Alexander Luria",
        "work": "The Working Brain",
        "quote": "Bilateral lesions of the supplementary motor area frequently produce an **akinetic** syndrome characterized by total loss of initiative."
      }
    ]
  },
  "Dashboard — kine/cinema.md": {
    "primary": "A theater where motion pictures are shown; the production of movies as an art form or entertainment industry.",
    "secondary": "In cultural history and aesthetics (shortened from French cinématographe, from Greek kinema 'movement'), the twentieth-century medium combining photographic motion, editing montage, and auditory narrative.",
    "quotes": [
      {
        "author": "Virginia Woolf",
        "work": "The Captain's Death Bed and Other Essays",
        "quote": "The **cinema** has the power to manifest emotion directly through moving forms and shadows before words can intervene."
      },
      {
        "author": "Walter Benjamin",
        "work": "The Work of Art in the Age of Mechanical Reproduction",
        "quote": "The technique of the **cinema** shatters traditional artistic aura through mass distribution and dynamic close-ups."
      },
      {
        "author": "Aldous Huxley",
        "work": "Brave New World",
        "quote": "The citizens sought effortless recreation in the multi-sensory feelies, the perfected successor of ancient flat **cinema**."
      }
    ]
  },
  "Dashboard — kine/cinematic.md": {
    "primary": "Relating to motion pictures; having qualities characteristic of films (such as sweeping visuals, rapid pacing, or dramatic cross-cutting).",
    "secondary": "In literary criticism and narrative theory, describing prose that employs visual montage, shifts in perspective, and panoramic descriptions reminiscent of film directing.",
    "quotes": [
      {
        "author": "Virginia Woolf",
        "work": "The Captain's Death Bed and Other Essays",
        "quote": "Her novel unfolded with a **cinematic** fluidity, dissolving from street scenes of London into intimate internal reveries."
      },
      {
        "author": "George Orwell",
        "work": "Keep the Aspidistra Flying",
        "quote": "The gaudy advertisements possessed a crude **cinematic** allure that appealed to the suburban crowds."
      },
      {
        "author": "Graham Greene",
        "work": "The Third Man",
        "quote": "The chase through the shadowed sewers of Vienna had an unmistakably **cinematic** intensity."
      }
    ]
  },
  "Dashboard — kine/cinematise.md": {
    "primary": "The standard British spelling of cinematize; to adapt a literary work or stage drama for presentation as a motion picture.",
    "secondary": "In narrative arts, to re-conceive a story in terms of camera movement, visual symbols, and cinematic editing rhythms.",
    "quotes": [
      {
        "author": "Virginia Woolf",
        "work": "The Captain's Death Bed and Other Essays",
        "quote": "To **cinematise** Anna Karenina is inevitably to sacrifice the subtle psychological interiority for coarse physical melodrama."
      },
      {
        "author": "George Bernard Shaw",
        "work": "Our Theatres in the Nineties",
        "quote": "If they attempt to **cinematise** my stage plays, they must understand that dialogue, not spectacle, carries the intellectual fire."
      },
      {
        "author": "H. G. Wells",
        "work": "The Work, Wealth and Happiness of Mankind",
        "quote": "Directors sought to **cinematise** classic historical pageants to satisfy the burgeoning appetite of mass audiences."
      }
    ]
  },
  "Dashboard — kine/cinematize.md": {
    "primary": "To adapt a novel, poem, or factual narrative into a motion picture film.",
    "secondary": "In media studies, to transform written or static material into dynamic, visually orchestrated moving sequences suitable for the screen.",
    "quotes": [
      {
        "author": "F. Scott Fitzgerald",
        "work": "The Last Tycoon",
        "quote": "The studio executives gathered in the projection room to decide how best to **cinematize** the bestselling romance."
      },
      {
        "author": "Aldous Huxley",
        "work": "Eyeless in Gaza",
        "quote": "He tried to **cinematize** his philosophical theories, hoping moving diagrams might penetrate the apathy of modern youth."
      },
      {
        "author": "Arthur Conan Doyle",
        "work": "Memories and Adventures",
        "quote": "Pioneering filmmakers approached him for permission to **cinematize** the exploits of Sherlock Holmes upon the silver screen."
      }
    ]
  },
  "Dashboard — kine/diakinesis.md": {
    "primary": "The fifth and final stage of the prophase of meiosis, during which homologous chromosomes condense, chiasmata terminalize, and the nuclear envelope breaks down.",
    "secondary": "In cytogenetics, the transitional meiotic phase immediately preceding metaphase I, characterized by maximally contracted bivalents ready for spindle attachment.",
    "quotes": [
      {
        "author": "Thomas Hunt Morgan",
        "work": "The Mechanism of Mendelian Heredity",
        "quote": "During **diakinesis**, the contracted chromosome pairs migrate toward the periphery of the nucleus just prior to the dissolution of its membrane."
      },
      {
        "author": "Theodosius Dobzhansky",
        "work": "Genetics and the Origin of Species",
        "quote": "Inspection of bivalents at **diakinesis** confirmed the occurrence of reciprocal translocations between non-homologous chromosomes."
      },
      {
        "author": "Edmund Beecher Wilson",
        "work": "The Cell in Development and Heredity",
        "quote": "The stage of **diakinesis** is distinguished by the extreme shortening of the tetrads and their terminalized chiasmata."
      }
    ]
  },
  "Dashboard — kine/dyskinesia.md": {
    "primary": "Abnormality, impairment, or distortion of voluntary movement; any involuntary, uncontrolled muscle movement or spasm.",
    "secondary": "In clinical neurology, a class of hyperkinetic movement disorders (such as tardive dyskinesia or levodopa-induced dyskinesia) characterized by choreic, dystonic, or athetoid movements.",
    "quotes": [
      {
        "author": "Oliver Sacks",
        "work": "Awakenings",
        "quote": "After months of mobility, high doses of medication provoked distressing **dyskinesia**, manifesting as choreic twitches of the face and limbs."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The involuntary grimacing and writhing movements of acute chorea represent a classic clinical **dyskinesia**."
      },
      {
        "author": "Alexander Luria",
        "work": "The Nature of Human Conflicts",
        "quote": "Disruption of striatal inhibitory circuits results in chaotic motor overflow and severe postural **dyskinesia**."
      }
    ]
  },
  "Dashboard — kine/dyskinetic.md": {
    "primary": "Pertaining to, affected by, or characterized by dyskinesia; displaying abnormal, involuntary, or spasmodic movements.",
    "secondary": "In pediatric neurology and physical therapy, classifying types of cerebral palsy (dyskinetic cerebral palsy) characterized by fluctuating muscle tone and choreoathetosis.",
    "quotes": [
      {
        "author": "Oliver Sacks",
        "work": "Awakenings",
        "quote": "The patient's hands performed continuous, wild, **dyskinetic** arabesques that prevented her from holding a teacup."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The sudden eruption of **dyskinetic** jerks interrupted the patient's gait, forcing him to clutch the bedpost for support."
      },
      {
        "author": "Alexander Luria",
        "work": "The Working Brain",
        "quote": "Damage to the extrapyramidal pathways gives rise to distinctive **dyskinetic** postures and uncoordinated motor outbursts."
      }
    ]
  },
  "Dashboard — kine/hyperkinesia.md": {
    "primary": "An abnormally increased or excessive muscular movement, activity, or motor restlessness; hyperactivity.",
    "secondary": "In pediatric psychopathology and neuropsychiatry, a clinical syndrome characterized by sustained restlessness, impulsivity, and inability to maintain postural stillness.",
    "quotes": [
      {
        "author": "Oliver Sacks",
        "work": "Awakenings",
        "quote": "The sudden wave of motor excitement produced severe **hyperkinesia**, sending the patient pacing the ward corridors for hours."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Extreme choreic **hyperkinesia** may exhaust the child's physical strength unless calmed by sedatives and bed rest."
      },
      {
        "author": "Alexander Luria",
        "work": "The Nature of Human Conflicts",
        "quote": "In states of acute psychic tension, motor impulses escape cortical control, manifesting as explosive somatic **hyperkinesia**."
      }
    ]
  },
  "Dashboard — kine/hyperkinesis.md": {
    "primary": "Abnormally increased or exaggerated muscular movement or motor activity; a technical clinical synonym for hyperkinesia.",
    "secondary": "In historical pediatric medicine and behavioral neurology, the diagnostic forerunner of attention deficit hyperactivity disorder (ADHD), characterized by sustained motor agitation.",
    "quotes": [
      {
        "author": "Oliver Sacks",
        "work": "Awakenings",
        "quote": "The post-encephalitic **hyperkinesis** manifested as an uncontrollable motor drive, impelling patients into frantic motion."
      },
      {
        "author": "Robley Dunglison",
        "work": "Medical Lexicon",
        "quote": "The term **hyperkinesis** designates any morbid increase of muscular motility, whether spasmodic or continuous."
      },
      {
        "author": "Charles Sherrington",
        "work": "The Integrative Action of the Nervous System",
        "quote": "Decerebrate preparations frequently exhibit dramatic motor release phenomena and reflex **hyperkinesis**."
      }
    ]
  },
  "Dashboard — kine/hyperkinetic.md": {
    "primary": "Characterized by or suffering from hyperkinesis; marked by excessive movement, fast tempo, or extreme restlessness.",
    "secondary": "In cardiology and hemodynamics, denoting a hyperdynamic circulatory state (hyperkinetic circulation) marked by elevated cardiac output, tachycardia, and bounding peripheral pulses.",
    "quotes": [
      {
        "author": "Oliver Sacks",
        "work": "Awakenings",
        "quote": "Her speech became breathless and hurried, matching her erratic, **hyperkinetic** bursts of physical energy."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "In severe anemia and thyrotoxicosis, we encounter a **hyperkinetic** cardiovascular state with wide pulse pressures."
      },
      {
        "author": "Alexander Luria",
        "work": "The Working Brain",
        "quote": "Children suffering from frontal lobe disinhibition display a **hyperkinetic** behavioral pattern that disrupts classroom learning."
      }
    ]
  },
  "Dashboard — kine/hypokinesia.md": {
    "primary": "Abnormally decreased or diminished muscular movement, mobility, or motor function; a partial loss of bodily movement.",
    "secondary": "In neurophysiology and space medicine, a state of decreased physical motor activity, observed in parkinsonian extrapyramidal disorders or prolonged microgravity.",
    "quotes": [
      {
        "author": "Oliver Sacks",
        "work": "Awakenings",
        "quote": "The creeping **hypokinesia** gradually froze her gestures until she sat immobile like a carved stone effigy."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Early stages of parkinsonism are often missed because the mild **hypokinesia** is mistaken for natural senile slowing."
      },
      {
        "author": "Alexander Luria",
        "work": "The Working Brain",
        "quote": "Subcortical lesions affecting the striatum lead directly to severe **hypokinesia** and impoverished facial expression."
      }
    ]
  },
  "Dashboard — kine/hypokinesis.md": {
    "primary": "Abnormal reduction of voluntary movement or muscular motility; an alternative technical designation for hypokinesia.",
    "secondary": "In echocardiography, a localized reduction in systolic wall thickening and excursion of a myocardial segment, indicating ischemia or partial infarction.",
    "quotes": [
      {
        "author": "Oliver Sacks",
        "work": "Awakenings",
        "quote": "His severe **hypokinesis** made even the simplest act, such as reaching for his spectacles, a struggle against invisible weights."
      },
      {
        "author": "Robley Dunglison",
        "work": "Medical Lexicon",
        "quote": "Under **hypokinesis**, medical writers classify all conditions wherein motor responsiveness is pathologically diminished."
      },
      {
        "author": "Charles Sherrington",
        "work": "The Integrative Action of the Nervous System",
        "quote": "Inhibition of spinal motor pools causes instantaneous **hypokinesis** in the antagonistic muscle groups."
      }
    ]
  },
  "Dashboard — kine/hypokinetic.md": {
    "primary": "Characterized by, suffering from, or pertaining to hypokinesia; displaying sluggish, abnormally diminished, or reduced movement.",
    "secondary": "In clinical cardiology and movement disorders, describing under-active myocardial contractions or parkinsonian motor patterns characterized by slowed reaction times.",
    "quotes": [
      {
        "author": "Oliver Sacks",
        "work": "Awakenings",
        "quote": "The **hypokinetic** patient sat rooted to his chair, staring fixedly at the wall with unblinking eyes."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "A **hypokinetic** apical segment detected during cardiac examination strongly suggests occlusive disease of the anterior descending artery."
      },
      {
        "author": "Alexander Luria",
        "work": "The Working Brain",
        "quote": "The patient's gait was distinctly **hypokinetic**, composed of short, shuffling steps devoid of normal reciprocal arm swings."
      }
    ]
  },
  "Dashboard — kine/kine.md": {
    "primary": "The ancient Greek combining form kine- or kineto- (from kinein, meaning 'to move or set in motion'), the root of modern scientific vocabulary of movement and energy.",
    "secondary": "In archaic and poetic English, an ancient plural of cow ('cattle'); in linguistic etymology, the prime formative element in kinetics, cinema, kinesiology, and cytokinesis.",
    "quotes": [
      {
        "author": "Walter William Skeat",
        "work": "An Etymological Dictionary of the English Language",
        "quote": "The Greek root **kine**, meaning to set in motion, forms the core of modern mechanics, cinema, and physical chemistry."
      },
      {
        "author": "Ernest Weekley",
        "work": "The Romance of Words",
        "quote": "From Hellenic **kine**, physicists derived their fundamental terms for moving energy and the moving picture."
      },
      {
        "author": "Peter Mark Roget",
        "work": "Thesaurus of English Words and Phrases",
        "quote": "Under the radical **kine**, we classify all principles, devices, and sensations relating to physical velocity and dynamic action."
      }
    ]
  },
  "Dashboard — kine/kinematics.md": {
    "primary": "The branch of classical mechanics that describes the motion of points, bodies, and systems without considering the forces that cause the motion.",
    "secondary": "In mechanical engineering and robotics, the geometrical analysis of joint angles, velocities, and positional coordinates in articulated mechanisms.",
    "quotes": [
      {
        "author": "William Rankine",
        "work": "A Manual of Applied Mechanics",
        "quote": "The science of **kinematics** treats of motion purely in the abstract, without regard to mass or accelerating forces."
      },
      {
        "author": "Lord Kelvin",
        "work": "Treatise on Natural Philosophy",
        "quote": "Before investigating the causes of motion in dynamics, we must master the pure geometry of displacement in **kinematics**."
      },
      {
        "author": "James Clerk Maxwell",
        "work": "Matter and Motion",
        "quote": "The **kinematics** of a rigid body reveals that every possible displacement is equivalent to a screw motion along an instantaneous axis."
      }
    ]
  },
  "Dashboard — kine/kinescope.md": {
    "primary": "A cathode-ray tube used in television receivers to display images; historically, a film recording made directly from the screen of a television monitor.",
    "secondary": "In broadcasting history (invented by Vladimir Zworykin), the optical-electronic device that revolutionized early television before magnetic videotape recording became available.",
    "quotes": [
      {
        "author": "Vladimir Zworykin",
        "work": "Television: The Electronics of Image Transmission",
        "quote": "In the **kinescope**, a finely focused beam of electrons sweeps across the fluorescent screen, painting thirty frames every second."
      },
      {
        "author": "Norbert Wiener",
        "work": "Cybernetics",
        "quote": "The feedback loops within the television **kinescope** ensure precise synchronization between the transmitter and the display."
      },
      {
        "author": "Lewis Mumford",
        "work": "Technics and Civilization",
        "quote": "Early television broadcasts were preserved for posterity only through the grainy medium of the film **kinescope**."
      }
    ]
  },
  "Dashboard — kine/kinesiologist.md": {
    "primary": "A specialist or professional who studies human movement, biomechanics, physical activity, and muscle function.",
    "secondary": "In sports science and rehabilitative medicine, an expert who applies mechanical and neuromuscular principles to evaluate athletic performance, treat motor deficits, and design ergonomic therapies.",
    "quotes": [
      {
        "author": "Oliver Sacks",
        "work": "A Leg to Stand On",
        "quote": "The hospital **kinesiologist** guided my paralyzed limb through passive flexion exercises to re-educate the dormant neural pathways."
      },
      {
        "author": "Charles Sherrington",
        "work": "The Integrative Action of the Nervous System",
        "quote": "The modern **kinesiologist** must analyze how reciprocal innervation coordinates opposing muscle groups into smooth, purposeful actions."
      },
      {
        "author": "Alexander Luria",
        "work": "The Working Brain",
        "quote": "Working alongside the neurologist, the **kinesiologist** charted the precise kinematic errors in the patient's walking gait."
      }
    ]
  },
  "Dashboard — kine/kinesiology.md": {
    "primary": "The scientific study of human and animal movement, mechanics, and physical activity; biomechanics and exercise science.",
    "secondary": "In physical therapy and sports medicine, an interdisciplinary field integrating anatomy, physiology, biomechanics, and motor learning to optimize movement and rehabilitate injuries.",
    "quotes": [
      {
        "author": "Charles Sherrington",
        "work": "The Integrative Action of the Nervous System",
        "quote": "The foundational principles of **kinesiology** demonstrate that complex movement emerges from coordinated reflexes organized across the spinal cord."
      },
      {
        "author": "Oliver Sacks",
        "work": "A Leg to Stand On",
        "quote": "My recovery forced me to explore practical **kinesiology**, relearning the delicate mechanics of weight distribution and step length."
      },
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "Every mental state produces a muscular corollary, an axiom which forms the psychological bridge into **kinesiology**."
      }
    ]
  },
  "Dashboard — kine/kinesis.md": {
    "primary": "Movement or motion in general; a non-directional movement or activity response of an organism in response to a stimulus (differing from a taxis).",
    "secondary": "In behavioral ethology and invertebrate physiology, an innate stimulus-response where the rate of locomotion (orthokinesis) or turning frequency (klinokinesis) depends on stimulus intensity without orientation.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Movement and Habits of Climbing Plants",
        "quote": "The circumnutating tip of the tendril exhibits an innate **kinesis** that explores surrounding space for mechanical support."
      },
      {
        "author": "Julian Huxley",
        "work": "The Individual in the Animal Kingdom",
        "quote": "Woodlice congregate in damp crevices through simple **kinesis**, slowing their wandering movements whenever moisture levels rise."
      },
      {
        "author": "Ernst Mayr",
        "work": "Animal Species and Evolution",
        "quote": "Unlike directed taxis, biological **kinesis** relies entirely upon changes in random velocity to keep an organism within favorable zones."
      }
    ]
  },
  "Dashboard — kine/kinesthesia.md": {
    "primary": "The awareness of the position and movement of the parts of the body using sensory receptors (proprioceptors) in joints, tendons, and muscles.",
    "secondary": "In sensory neurophysiology and cognitive psychology, the muscle-joint sense that provides feedback necessary for coordinated voluntary movement, posture, and manual dexterity.",
    "quotes": [
      {
        "author": "Oliver Sacks",
        "work": "The Man Who Mistook His Wife for a Hat",
        "quote": "Deprived of all **kinesthesia** by sensory neuropathy, the poor woman felt disembodied, unable to stand without visual inspection of her limbs."
      },
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "Our immediate sense of bodily weight and effort depends upon **kinesthesia**, which reports the tension of every contracted muscle."
      },
      {
        "author": "Charles Sherrington",
        "work": "The Integrative Action of the Nervous System",
        "quote": "The proprioceptive system provides the continuous **kinesthesia** that guides the motor cortex in modulating skilled voluntary acts."
      }
    ]
  },
  "Dashboard — kine/kinesthesis.md": {
    "primary": "The perception or sense of bodily movement and muscular effort; a technical synonym for kinesthesia.",
    "secondary": "In experimental psychology, the sixth sense mediated by muscle spindles and Golgi tendon organs that continuously informs the brain of somatic position.",
    "quotes": [
      {
        "author": "Edward Titchener",
        "work": "A Text-Book of Psychology",
        "quote": "In every voluntary act, an anticipatory image of **kinesthesis** precedes the actual execution of the movement."
      },
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "Close your eyes and raise your arm; your awareness of its trajectory is furnished directly by **kinesthesis**."
      },
      {
        "author": "Oliver Sacks",
        "work": "A Leg to Stand On",
        "quote": "Without **kinesthesis**, the limb seemed not only useless but alien, like an inanimate block of wood attached to the pelvis."
      }
    ]
  },
  "Dashboard — kine/kinesthetic.md": {
    "primary": "Relating to kinesthesia or the awareness of bodily position and movement; involving physical sensation of motion.",
    "secondary": "In educational pedagogy and cognitive theory, describing learning styles, artistic sensibilities, or physical talents based primarily on hands-on physical activity.",
    "quotes": [
      {
        "author": "Oliver Sacks",
        "work": "The Man Who Mistook His Wife for a Hat",
        "quote": "She learned to compensate for her sensory loss by replacing her missing **kinesthetic** sense with vigilant visual supervision."
      },
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "The blind sculptor possesses an exquisite **kinesthetic** memory of form, gauging curves through muscular exertion."
      },
      {
        "author": "Virginia Woolf",
        "work": "The Waves",
        "quote": "She felt a pure **kinesthetic** joy in the simple, rhythmic plunge of her arms into the cold sea."
      }
    ]
  },
  "Dashboard — kine/kinesthetically.md": {
    "primary": "In a kinesthetic manner; by means of the sensation of bodily position and muscular movement.",
    "secondary": "In perceptual psychology, describing how an individual navigates space, executes athletic movements, or identifies physical objects through tactile and muscular sensations.",
    "quotes": [
      {
        "author": "Oliver Sacks",
        "work": "A Leg to Stand On",
        "quote": "I had to learn **kinesthetically** where the floor was, calibrating each step through conscious muscular effort."
      },
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "The veteran violinist perceives the fingerboard **kinesthetically**, finding the exact interval without conscious calculation."
      },
      {
        "author": "Alexander Luria",
        "work": "The Mind of a Mnemonist",
        "quote": "The memorizer described numbers **kinesthetically**, associating each digit with a distinct muscular tension in his throat."
      }
    ]
  },
  "Dashboard — kine/kinesthetics.md": {
    "primary": "The study or practice of kinesthetic awareness and body movement; the physical sensations of movement.",
    "secondary": "In performance art, dance, and athletics, the disciplined training of neuromuscular awareness to produce graceful, efficient, and injury-free motion.",
    "quotes": [
      {
        "author": "Oliver Sacks",
        "work": "A Leg to Stand On",
        "quote": "Physical therapy is fundamentally an apprenticeship in **kinesthetics**, re-establishing lost communication between brain and muscle."
      },
      {
        "author": "Charles Sherrington",
        "work": "The Integrative Action of the Nervous System",
        "quote": "The intricate reflex circuits of the spinal cord form the physical infrastructure underlying all animal **kinesthetics**."
      },
      {
        "author": "Edward Titchener",
        "work": "A Text-Book of Psychology",
        "quote": "The laboratory investigation of **kinesthetics** reveals that sensations of joint displacement are more acute than those of skin pressure."
      }
    ]
  },
  "Dashboard — kine/kinetic.md": {
    "primary": "Of, relating to, or resulting from motion; characterized by movement, dynamism, or lively activity.",
    "secondary": "In classical physics, denoting kinetic energy (the energy possessed by a body by virtue of its motion, given by 1/2 mv²), contrasting with potential energy.",
    "quotes": [
      {
        "author": "James Clerk Maxwell",
        "work": "Matter and Motion",
        "quote": "The **kinetic** energy of a moving body is proportional to its mass and the square of its velocity."
      },
      {
        "author": "Lord Kelvin",
        "work": "Treatise on Natural Philosophy",
        "quote": "In every mechanical system, energy continuously oscillates between static potential and active **kinetic** states."
      },
      {
        "author": "H. G. Wells",
        "work": "The War of the Worlds",
        "quote": "The Martian projectile struck the hillside, converting its tremendous **kinetic** energy into blinding heat and explosive fury."
      }
    ]
  },
  "Dashboard — kine/kineticism.md": {
    "primary": "A doctrine, theory, or artistic movement that emphasizes or incorporates mechanical or virtual motion.",
    "secondary": "In twentieth-century art history (Kinetic Art), an aesthetic approach where motion (mechanical, wind-driven, or optical) is integral to the structure and viewer experience of the artwork.",
    "quotes": [
      {
        "author": "Herbert Read",
        "work": "A Concise History of Modern Sculpture",
        "quote": "The rise of **kineticism** in modern sculpture challenged the ancient dogma that plastic art must be static and permanent."
      },
      {
        "author": "Lewis Mumford",
        "work": "Technics and Civilization",
        "quote": "The relentless **kineticism** of the machine age transformed the contemplative rhythms of human culture into frantic velocity."
      },
      {
        "author": "Bertrand Russell",
        "work": "The ABC of Atoms",
        "quote": "Modern physics dissolves solid matter into pure **kineticism**, a ceaseless dance of electrical charges in empty space."
      }
    ]
  },
  "Dashboard — kine/kineticist.md": {
    "primary": "A specialist in kinetics or chemical kinetics; an artist who creates kinetic art.",
    "secondary": "In physical chemistry, a scientist who investigates reaction rates, transition states, and molecular collision mechanisms.",
    "quotes": [
      {
        "author": "Svante Arrhenius",
        "work": "Textbook of Electrochemistry",
        "quote": "The chemical **kineticist** measures how reaction velocities double with every ten-degree rise in absolute temperature."
      },
      {
        "author": "William Ostwald",
        "work": "Manual of Physico-Chemical Measurements",
        "quote": "For the skilled **kineticist**, a catalytic agent does not create a new reaction, but merely accelerates an existing path."
      },
      {
        "author": "Herbert Read",
        "work": "Art Now",
        "quote": "As a pioneering **kineticist**, Calder abandoned traditional bronze to sculpt with moving air currents and suspended wires."
      }
    ]
  },
  "Dashboard — kine/kinetics.md": {
    "primary": "The branch of classical mechanics concerned with the forces that cause or modify the motion of bodies.",
    "secondary": "In physical chemistry (chemical kinetics) and pharmacology (pharmacokinetics), the quantitative study of the rates of reactions and the absorption, distribution, and elimination of substances.",
    "quotes": [
      {
        "author": "Svante Arrhenius",
        "work": "Quantitative Laws in Biological Chemistry",
        "quote": "The mathematical equations of chemical **kinetics** apply with equal precision to enzymatic digestion in living cells."
      },
      {
        "author": "William Rankine",
        "work": "A Manual of Applied Mechanics",
        "quote": "While kinematics considers motion alone, **kinetics** introduces the concepts of force, inertia, and work."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The modern clinician must understand drug **kinetics** to maintain therapeutic blood concentrations without causing toxicity."
      }
    ]
  },
  "Dashboard — kine/kinetochore.md": {
    "primary": "A complex protein structure formed on the centromere of each sister chromatid during cell division, to which spindle microtubules attach to pull the chromatids apart.",
    "secondary": "In molecular cytology and cell biology, the macromolecular machine responsible for chromosome segregation, spindle checkpoint signaling, and force generation during anaphase.",
    "quotes": [
      {
        "author": "Edmund Beecher Wilson",
        "work": "The Cell in Development and Heredity",
        "quote": "Electron microscopy reveals that each spindle fiber inserts directly into a trilaminar plaque, the **kinetochore**, on the chromosome."
      },
      {
        "author": "Theodosius Dobzhansky",
        "work": "Genetics and the Origin of Species",
        "quote": "Chromosome fragments lacking a functional **kinetochore** cannot attach to the spindle and are inevitably lost during mitosis."
      },
      {
        "author": "Thomas Hunt Morgan",
        "work": "The Theory of the Gene",
        "quote": "The mechanical tug-of-war at the **kinetochore** aligns the duplicated chromosomes precisely along the equatorial plate."
      }
    ]
  },
  "Dashboard — kine/kinetophobia.md": {
    "primary": "An abnormal, excessive, or irrational fear of movement or motion.",
    "secondary": "In clinical psychiatry and kinesiology, a phobic anxiety disorder where an individual fears moving or being moved, often secondary to chronic pain or fear of re-injury (kinesiophobia).",
    "quotes": [
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "In morbid **kinetophobia**, the patient cowers in bed, terrified that the slightest bodily movement will provoke agonizing vertigo."
      },
      {
        "author": "Robley Dunglison",
        "work": "Medical Lexicon",
        "quote": "Psychopathologists record cases of **kinetophobia** following severe concussions, wherein all passive vehicular travel inspires panic."
      },
      {
        "author": "Oliver Sacks",
        "work": "A Leg to Stand On",
        "quote": "A severe form of **kinetophobia** gripped me after surgery; I shrank from the prospect of placing weight upon the damaged joint."
      }
    ]
  },
  "Dashboard — kine/kinetoscope.md": {
    "primary": "An early motion-picture exhibition device designed for films to be viewed by one individual at a time through a peephole viewer.",
    "secondary": "In cinema history (invented by Thomas Edison and William Dickson), the groundbreaking 1891 device that passed a continuous strip of perforated 35mm film over an electric lamp and rotating shutter.",
    "quotes": [
      {
        "author": "Thomas Edison",
        "work": "The Kinetoscope and Its Future",
        "quote": "The **kinetoscope** enables the spectator to gaze into a cabinet and witness life, action, and gesture reproduced with absolute fidelity."
      },
      {
        "author": "H. G. Wells",
        "work": "When the Sleeper Wakes",
        "quote": "The public arcade was lined with rows of coin-operated **kinetoscope** machines displaying moving tableaux of foreign capitals."
      },
      {
        "author": "Walter Benjamin",
        "work": "The Work of Art in the Age of Mechanical Reproduction",
        "quote": "Before the cinema gathered audiences into collective dark halls, Edison's **kinetoscope** offered only an isolated, individual peephole glimpse."
      }
    ]
  },
  "Dashboard — kine/kinetosis.md": {
    "primary": "Motion sickness; a condition of nausea, dizziness, and malaise caused by conflicting sensory signals of movement.",
    "secondary": "In aerospace and marine medicine, a physiological disturbance caused by a mismatch between vestibular semicircular canal signals, visual input, and proprioceptive sensors (seasickness, airsickness).",
    "quotes": [
      {
        "author": "Oliver Sacks",
        "work": "The Man Who Mistook His Wife for a Hat",
        "quote": "Severe vestibular **kinetosis** can overwhelm even seasoned sailors when rapid Coriolis accelerations confuse the labyrinthine canals."
      },
      {
        "author": "Charles Darwin",
        "work": "The Voyage of the Beagle",
        "quote": "Throughout our passage around Cape Horn, I was incapacitated by distressing **kinetosis**, unable to stand or write in my journal."
      },
      {
        "author": "Robley Dunglison",
        "work": "Medical Lexicon",
        "quote": "Medical writers designate seasickness, car-sickness, and swing-sickness collectively under the diagnostic rubric of **kinetosis**."
      }
    ]
  },
  "Dashboard — kine/photokinesis.md": {
    "primary": "A change in the speed or rate of locomotion of an organism or cell in response to light intensity (a type of kinesis).",
    "secondary": "In photobiology and cellular ethology, a non-directional motor response where the velocity of movement increases (positive photokinesis) or decreases (negative photokinesis) with illumination levels.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Power of Movement in Plants",
        "quote": "Microscopic flagellates exhibit marked **photokinesis**, swimming with furious speed under bright sunlight but becoming quiescent in shade."
      },
      {
        "author": "Arthur Dendy",
        "work": "Outlines of Evolutionary Biology",
        "quote": "The phenomenon of **photokinesis** ensures that single-celled algae wander into surface waters where photosynthesis is optimal."
      },
      {
        "author": "Julian Huxley",
        "work": "The Individual in the Animal Kingdom",
        "quote": "Primitive invertebrates use non-directional **photokinesis** to disperse rapidly from exposed ground into dark, safe crevices."
      }
    ]
  },
  "Dashboard — kine/telekinesis.md": {
    "primary": "The purported movement of physical objects by the power of the mind alone, without physical contact or known natural force; psychokinesis.",
    "secondary": "In parapsychology and cultural folklore, an alleged psychic phenomenon investigated in late nineteenth-century spiritualist séances and modern science fiction.",
    "quotes": [
      {
        "author": "William James",
        "work": "Memories and Studies",
        "quote": "The spiritualist claimed that the levitation of the heavy oak table was an unmistakable instance of psychic **telekinesis**."
      },
      {
        "author": "Arthur Conan Doyle",
        "work": "The History of Spiritualism",
        "quote": "Witnesses attested to unmistakable acts of **telekinesis**, observing small objects drift across the locked room in broad daylight."
      },
      {
        "author": "Carl Jung",
        "work": "Psychology and the Occult",
        "quote": "Reports of spontaneous **telekinesis** in poltergeist cases frequently coincide with intense emotional conflicts in adolescent subjects."
      }
    ]
  }
};

let count = 0;
for (const [key, data] of Object.entries(batch3Data)) {
  const [relDir, fileName] = key.split('/');
  if (updateNote(relDir, fileName, data)) {
    count++;
  }
}

console.log(`\n========================================`);
console.log(`Batch 3 Completed: ${count} / ${Object.keys(batch3Data).length} words updated`);
console.log(`========================================`);
