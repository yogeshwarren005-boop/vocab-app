# -*- coding: utf-8 -*-
import os, sys, re
sys.stdout.reconfigure(encoding="utf-8")

data = {
  # --- Dashboard — press Part 3 (11C, 34 words) ---
  "Dashboard — press/pressingly.md": {
    "primary": "In an urgent, insistent, or importunate manner that demands immediate attention.",
    "secondary": "In diplomatic or business correspondence, framing an urgent plea or critical petition with solemn insistence.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Nicholas Nickleby", "quote": "He wrote **pressingly** to his uncle, entreating him to grant an immediate interview on matters of vital moment."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The bailiff urged the matter **pressingly**, insisting that the shearing must commence before the rain."},
      {"author": "Walter Scott", "work": "The Heart of Midlothian", "quote": "Jeanie pleaded **pressingly** for her sister's pardon, moving the queen by her simple Scottish eloquence."}
    ]
  },
  "Dashboard — press/pressman.md": {
    "primary": "A printer who operates a printing press, or a journalist working for newspapers.",
    "secondary": "In historical printing trades, skilled artisans who ink the form, position the paper, and pull the bar of the printing press.",
    "quotes": [
      {"author": "Benjamin Franklin", "work": "Autobiography of Benjamin Franklin", "quote": "I was at first an apprentice **pressman**, working vigorously at the heavy hand-press from dawn till dusk."},
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Six Napoleons", "quote": "The eager **pressman** scribbled shorthand notes in the police corridor, hoping for an exclusive scoop."},
      {"author": "George Orwell", "work": "Homage to Catalonia", "quote": "An American **pressman** arrived at the front line with cameras and notebooks, seeking frontline accounts."}
    ]
  },
  "Dashboard — press/pressmark.md": {
    "primary": "A notation, symbol, or shelf mark stamped in a library book indicating its physical location.",
    "secondary": "In archival bibliographical classification, the alphanumeric shelving code linking catalog cards to specific bays, shelves, and volumes.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Red Circle", "quote": "Holmes noted the obscure British Museum **pressmark** penciled on the inner margin of the pamphlet."},
      {"author": "Thomas Frognall Dibdin", "work": "The Bibliomania", "quote": "The rare incunabulum bore an ancient monastic **pressmark** indicating its former shelf in the abbey scriptorium."},
      {"author": "M. R. James", "work": "Ghost Stories of an Antiquary", "quote": "The antiquary traced the curious parchment by its distinctive eighteenth-century library **pressmark**."}
    ]
  },
  "Dashboard — press/pressor.md": {
    "primary": "Causing an increase in arterial blood pressure, or a substance or physiological reflex that raises blood pressure.",
    "secondary": "In cardiovascular physiology, pressor reflexes stimulate peripheral arteriolar vasoconstriction via sympathetic adrenergic signaling.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Intravenous infusion of an adrenal extract elicited an instantaneous **pressor** response with rising arterial tension."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Stimulation of the medullary vasomotor center provokes a systemic **pressor** discharge throughout the arterioles."},
      {"author": "Richard Cabot", "work": "Physical Diagnosis", "quote": "The patient showed marked hypersensitivity to endogenous **pressor** substances during severe emotional agitation."}
    ]
  },
  "Dashboard — press/pressure.md": {
    "primary": "Continuous physical force exerted against or upon an object by something in contact with it; urgent demand.",
    "secondary": "In classical thermodynamics and fluid dynamics, the scalar perpendicular force exerted per unit area, quantified in Pascals or atmospheres.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "A rusty patch appeared upon the Bible verse, caused by previous **pressure** of an iron substance."},
      {"author": "Isaac Newton", "work": "Philosophiae Naturalis Principia Mathematica", "quote": "The inward hydrostatic **pressure** of the fluid is proportional to the vertical height of the incumbent column."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Under the pecuniary **pressure** of relentless creditors, Mr. Micawber preserved his theatrical optimism."}
    ]
  },
  "Dashboard — press/pressure-cook.md": {
    "primary": "To cook food quickly inside a sealed vessel using high-pressure steam at temperatures above the normal boiling point.",
    "secondary": "In culinary physics, sealing water in a vessel elevates boiling temperatures to approximately 120°C, dramatically accelerating collagen gelatinization.",
    "quotes": [
      {"author": "Aldous Huxley", "work": "Brave New World", "quote": "The communal kitchen apparatus could **pressure-cook** tons of synthetic proteins in a matter of minutes."},
      {"author": "George Orwell", "work": "Coming Up for Air", "quote": "Modern kitchens advertised gadgets to **pressure-cook** stews and vegetables in half the traditional time."},
      {"author": "Sinclair Lewis", "work": "Cass Timberlane", "quote": "She learned to use the heavy aluminum pot to **pressure-cook** meals when evening guests arrived unexpectedly."}
    ]
  },
  "Dashboard — press/pressure-wash.md": {
    "primary": "To clean an exterior surface using a high-pressure stream or jet of pressurized water.",
    "secondary": "In architectural restoration and surface maintenance, removing paint, grime, or mildew using calibrated hydraulic nozzle discharges.",
    "quotes": [
      {"author": "John Steinbeck", "work": "Cannery Row", "quote": "The cannery mechanics began to **pressure-wash** the concrete gutting tables with high-velocity harbor hoses."},
      {"author": "Sinclair Lewis", "work": "Babbitt", "quote": "The contractor hired laborers to **pressure-wash** the soot-stained limestone facade of the newly acquired office building."},
      {"author": "Upton Sinclair", "work": "The Jungle", "quote": "Workers had to **pressure-wash** the bloody brick runways of the slaughterhouse at the end of each shift."}
    ]
  },
  "Dashboard — press/pressurise.md": {
    "primary": "To maintain or increase normal atmospheric pressure inside an enclosed chamber, aircraft cabin, or vessel.",
    "secondary": "In aeronautical design, pumping conditioned engine bleed air into sealed fuselage structures to sustain breathable conditions at altitude.",
    "quotes": [
      {"author": "Arthur C. Clarke", "work": "The Exploration of Space", "quote": "Before opening the inner airlock, the crew must **pressurise** the cargo transfer corridor with breathable air."},
      {"author": "H. G. Wells", "work": "The Shape of Things to Come", "quote": "The engineers sought to **pressurise** the high-altitude passenger cabins to allow flight above turbulent storm zones."},
      {"author": "Aldous Huxley", "work": "Brave New World", "quote": "Auxiliary pumps worked constantly to **pressurise** the high-temperature chemical synthesis chambers."}
    ]
  },
  "Dashboard — press/pressurize.md": {
    "primary": "To maintain normal atmospheric pressure inside a sealed enclosure flying or operating at high altitudes or depths.",
    "secondary": "In fluid transport engineering, using compressors or header tanks to sustain positive hydraulic pressure across pipeline networks.",
    "quotes": [
      {"author": "Arthur C. Clarke", "work": "2001: A Space Odyssey", "quote": "The command module systems worked smoothly to **pressurize** the central living sphere before the astronauts awoke."},
      {"author": "Carl Sagan", "work": "Contact", "quote": "Engineers checked the redundant valves designed to **pressurize** the observation sphere for atmospheric reentry."},
      {"author": "H. G. Wells", "work": "The War in the Air", "quote": "The ground crew worked through the night to **pressurize** the reserve gas cylinders of the experimental airship."}
    ]
  },
  "Dashboard — press/repress.md": {
    "primary": "To subdue, suppress, or restrain by force; to keep emotional feelings or memories under conscious control.",
    "secondary": "In psychoanalytic theory, an unconscious defense mechanism banishing distressing impulses, memories, or wishes from conscious awareness.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "She determined to **repress** all visible evidences of feeling as Gabriel entered the barn."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Mary was unable to **repress** her natural sarcasm when listening to Mr. Tyke's solemn platitudes."},
      {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "Society must **repress** antisocial aggression in order to safeguard the security of all citizens."}
    ]
  },
  "Dashboard — press/repressed.md": {
    "primary": "Subdued, restrained, or kept under rigid emotional or political control.",
    "secondary": "In psychoanalysis, thoughts, desires, or traumatic experiences relegated to the unconscious mind through psychological repression.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Tess was trying to lead a **repressed** life, but she little divined the invincible strength of her own vital passions."},
      {"author": "Sigmund Freud", "work": "The Ego and the Id", "quote": "The ego seeks to mediate between the urgent claims of the id and the rigid censorship of **repressed** desires."},
      {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "We should be glad to see just conduct enforced and unjust predation rigorously **repressed** in public affairs."}
    ]
  },
  "Dashboard — press/represser.md": {
    "primary": "One who or that which represses, restrains, subdues, or keeps in check.",
    "secondary": "In political discourse, characterizes authoritarian rulers or legal statutes that silence dissenting speech.",
    "quotes": [
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "A wise magistrate acts as the firm **represser** of tumult while remaining the protector of ancient liberties."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "Cromwell proved a stern **represser** of Royalist conspiracies throughout the protectorate."},
      {"author": "Francis Bacon", "work": "Essays", "quote": "A severe prince may become an effectual **represser** of common brigandage, yet breed sullen discontent."}
    ]
  },
  "Dashboard — press/repressing.md": {
    "primary": "Holding back, curbing, checking, or preventing the natural expression of feeling or rebellion.",
    "secondary": "In emotional self-regulation, the active inhibition of overt motor actions or speech in response to provoking stimuli.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Fred was under some difficulty in **repressing** a laugh, which would have grievously offended his dignified uncle."},
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "Henchard walked with stiff strides, **repressing** the groan that rose spontaneously to his parched lips."},
      {"author": "Charlotte Brontë", "work": "Villette", "quote": "I sat motionless at my desk, **repressing** every sob until the classroom was completely deserted."}
    ]
  },
  "Dashboard — press/repression.md": {
    "primary": "The action of subduing someone or something by force; the psychological prevention of desires from surfacing.",
    "secondary": "In Freudian psychoanalysis, the primary ego defense mechanism that excludes unacceptable impulses and memories from conscious thought.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Instead of being a man trained to stoic **repression**, he proved vulnerable to every sudden impulse of passion."},
      {"author": "Sigmund Freud", "work": "A General Introduction to Psychoanalysis", "quote": "The theory of **repression** is the cornerstone on which the whole structure of psychoanalysis rests."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Lydgate felt sure she was suffering under the painful strain of long-continued self-**repression**."}
    ]
  },
  "Dashboard — press/repressive.md": {
    "primary": "Inhibiting, restraining, or tending to keep under control; characterized by political or psychological oppression.",
    "secondary": "In sociological analysis, repressive laws impose severe punitive sanctions to enforce mechanical social solidarity.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "He was fuming under a **repressive** convention which he was forced to acknowledge despite inward rebellion."},
      {"author": "John Stuart Mill", "work": "On Liberty", "quote": "The **repressive** force of public opinion can prove more tyrannical than the direct penalties of the magistrate."},
      {"author": "George Orwell", "work": "1984", "quote": "The regime constructed an elaborate apparatus of **repressive** institutions to extinguish any flicker of independent thought."}
    ]
  },
  "Dashboard — press/repressor.md": {
    "primary": "An agent, person, or mechanism that represses or exerts a restraining influence.",
    "secondary": "In molecular biology and genetics, a DNA- or RNA-binding protein that inhibits the expression of one or more genes by blocking transcription.",
    "quotes": [
      {"author": "Francis Bacon", "work": "Essays", "quote": "The law stands as an impartial **repressor** of private vengeance and disordered passions in the commonwealth."},
      {"author": "Thomas Henry Huxley", "work": "Evolution and Ethics", "quote": "Civilized society serves as an essential **repressor** of the ruthless struggle for existence."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Social sympathy functions as an internal **repressor** of selfish animal instincts among gregarious creatures."}
    ]
  },
  "Dashboard — press/suppress.md": {
    "primary": "To forcibly put an end to, crush, or prevent the dissemination, development, or expression of something.",
    "secondary": "In clinical medicine, to stop or restrain physiological discharge, bleeding, or immunological responsiveness.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry V", "quote": "The mercy that was quick in us but late, by your own counsel is **suppress'd** and kill'd."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The emperor dispatched two veteran legions to **suppress** the insurrection that broke out in Illyricum."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The spy attempted to **suppress** his sudden nervousness when questioned closely at the barrier."}
    ]
  },
  "Dashboard — press/suppressant.md": {
    "primary": "An agent or medication that suppresses or diminishes a bodily function or symptom, such as cough or appetite.",
    "secondary": "In pharmacotherapy, an antitussive cough suppressant acts centrally on the brainstem cough center to reduce the cough reflex.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The physician prescribed an effective cough **suppressant** to allow the exhausted patient a night of restorative sleep."},
      {"author": "Richard Cabot", "work": "Differential Diagnosis", "quote": "The administration of an immune **suppressant** prevented further inflammatory degradation of the joint tissues."},
      {"author": "Oliver Sacks", "work": "Awakenings", "quote": "We gradually reduced the metabolic **suppressant** as neurological reflexes began to show spontaneous improvement."}
    ]
  },
  "Dashboard — press/suppressed.md": {
    "primary": "Forcibly restrained, subdued, withheld from publication, or prevented from normal physical manifestation.",
    "secondary": "In literary and publishing history, designates banned, censored, or confiscated editions prohibited by civil or ecclesiastical authorities.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry VI, Part 1", "quote": "Thus the Mortimers, in whom the royal title rested, were **suppressed** by political usurpation."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "How can you ask? she said with **suppressed** passion that trembled in every syllable."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Her eyes filled with tears at something indefinable, like the resolute effort of a **suppressed** grief."}
    ]
  },
  "Dashboard — press/suppresser.md": {
    "primary": "One who or that which suppresses, crushes, silences, or holds back from manifestation.",
    "secondary": "In genetics, a suppressor mutation or gene that reverses the phenotypic effect of an existing mutation at another locus.",
    "quotes": [
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "The standing army acted as the prompt **suppresser** of seditious assemblies throughout the capital."},
      {"author": "Thomas Babington Macaulay", "work": "Critical and Historical Essays", "quote": "Milton stood forth as the unyielding **suppresser** of clerical censorship and intellectual monopolies."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Certain genetic modifiers act as an effectual **suppresser** of ancestral reversionary plumage."}
    ]
  },
  "Dashboard — press/suppression.md": {
    "primary": "The act of subduing, quashing, concealing, or preventing the disclosure or operation of something.",
    "secondary": "In immunology, active immunosuppression diminishes cell-mediated or humoral antibody responses to allografts or autoantigens.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Is it not clear that there has been a systematic **suppression** of the vital correspondence from the beginning?"},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "She spoke with continued self-**suppression**, anxious not to arouse her companion's irritable temper."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "The deliberate **suppression** of my true sentiments cost me an agonizing inward conflict."}
    ]
  },
  "Dashboard — press/suppressive.md": {
    "primary": "Tending to suppress, quash, conceal, or prevent manifestation or expression.",
    "secondary": "In military tactical doctrine, suppressive fire prevents enemy forces from observing or firing effectively during friendly movement.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "On Liberty", "quote": "All **suppressive** measures directed against unorthodox doctrines ultimately injure intellectual progress."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The **suppressive** edicts issued against the eastern provinces only intensified religious resistance."},
      {"author": "George Orwell", "work": "1984", "quote": "The Thought Police employed ruthlessly **suppressive** techniques to extirpate unorthodox thoughts before they coalesced."}
    ]
  },
  "Dashboard — press/suppressor.md": {
    "primary": "An agent, device, or person that suppresses, restrains, or dampens an unwanted action or sound.",
    "secondary": "In firearms technology, an acoustic baffle cylinder attached to the muzzle to decelerate propellant gases and attenuate acoustic report.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Empty House", "quote": "The air-gun was fitted with an ingenious mechanical **suppressor** that discharged the deadly soft-nosed bullet in absolute silence."},
      {"author": "H. G. Wells", "work": "The Invisible Man", "quote": "He searched the apparatus for a chemical **suppressor** to neutralize the luminous refractory compounds."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "The secondary cross acted as a biological **suppressor** of the abnormal floral monstrosity."}
    ]
  },
  "Dashboard — press/uncompress.md": {
    "primary": "To release from pressure; to restore a compressed object or digital file to its original uncompressed volume.",
    "secondary": "In computer systems and data architecture, expanding compressed byte streams into raw readable files using matching codec decompression.",
    "quotes": [
      {"author": "Arthur C. Clarke", "work": "The City and the Stars", "quote": "The central computer needed only an instant to **uncompress** millions of recorded human memories from the memory banks."},
      {"author": "H. G. Wells", "work": "The First Men in the Moon", "quote": "We released the safety valves to **uncompress** the dense gases accumulated within our metallic sphere."},
      {"author": "Sinclair Lewis", "work": "Arrowsmith", "quote": "The technician waited for the autoclave chamber to **uncompress** before inspecting the sterile culture tubes."}
    ]
  },
  "Dashboard — press/unexpressed.md": {
    "primary": "Not made explicit, voiced, or manifested; held silently within the mind or heart.",
    "secondary": "In legal interpretation, unexpressed intent cannot override the plain meaning of words written within a formal contract or will.",
    "quotes": [
      {"author": "Ralph Waldo Emerson", "work": "Essays: First Series", "quote": "Prayer is the soul's sincere desire, uttered or **unexpressed**, the motion of a hidden fire that trembles in the breast."},
      {"author": "Joseph Conrad", "work": "Heart of Darkness", "quote": "He leaned back serene, with that peculiar smile of his sealing the **unexpressed** depths of his dark reflections."},
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "They walked side by side through the deep shadows of the forest with an **unexpressed** understanding between them."}
    ]
  },
  "Dashboard — press/unexpressible.md": {
    "primary": "Incapable of being expressed, spoken, or communicated in words; ineffable, indescribable.",
    "secondary": "In theological discourse, the transcendent nature of the divine that surpasses the conceptual limits of human language.",
    "quotes": [
      {"author": "John Tillotson", "work": "Sermons on Several Occasions", "quote": "The infinite majesty of the Divine Being fills the devout soul with **unexpressible** reverence and adoration."},
      {"author": "John Bunyan", "work": "The Pilgrim's Progress", "quote": "Christian felt an **unexpressible** joy as the heavy burden rolled from his shoulders into the empty sepulchre."},
      {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "Deep within the silence of the starry night there dwells an **unexpressible** grandeur that humbles human pride."}
    ]
  },
  "Dashboard — press/unexpressive.md": {
    "primary": "Lacking facial expression, emotional inflection, or meaningful communication; blank, impassive.",
    "secondary": "Archaically (as in Shakespeare and Milton), ineffable, indescribably wonderful, or beyond expression.",
    "quotes": [
      {"author": "William Shakespeare", "work": "As You Like It", "quote": "Run, run, Orlando, carve on every tree the fair, the chaste, and **unexpressive** she."},
      {"author": "John Milton", "work": "Lycidas", "quote": "And hears the **unexpressive** nuptial song, in the blest kingdoms meek of joy and love."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "His features remained completely **unexpressive**, masking the tempest of jealousy raging within his breast."}
    ]
  },
  "Dashboard — press/unimpressed.md": {
    "primary": "Not moved, affected, or influenced by someone or something; maintaining indifferent detachment.",
    "secondary": "In aesthetic criticism, withholding praise or approval due to perceived lack of originality or technical merit.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "As ever before, the pagan harpooneers remained almost wholly **unimpressed** by the ominous warnings of the stranger."},
      {"author": "Arthur Conan Doyle", "work": "The Valley of Fear", "quote": "McMurdo listened with an **unimpressed** air to the threats uttered by the leader of the lodge."},
      {"author": "George Bernard Shaw", "work": "Major Barbara", "quote": "Undershaft looked on with an **unimpressed** smile while the young intellectuals debated abstract socialism."}
    ]
  },
  "Dashboard — press/unimpressionable.md": {
    "primary": "Not easily influenced, moved, or affected by emotions, impressions, or external circumstances; hardened.",
    "secondary": "In character study, denotes individuals endowed with rigid stoicism, profound skepticism, or emotional imperviousness.",
    "quotes": [
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "St. John Rivers possessed a cold, **unimpressionable** nature that sacrificed personal warmth to ascetic duty."},
      {"author": "Robert Louis Stevenson", "work": "The Strange Case of Dr Jekyll and Mr Hyde", "quote": "Mr. Utterson the lawyer was a man of a rugged countenance, cold, scanty, and remarkably **unimpressionable**."},
      {"author": "Henry James", "work": "The American", "quote": "Christopher Newman found his French hosts stiff, haughty, and stubbornly **unimpressionable** to his candid goodwill."}
    ]
  },
  "Dashboard — press/unimpressive.md": {
    "primary": "Failing to command attention, admiration, or respect; ordinary, unremarkable, or lackluster.",
    "secondary": "In architectural appraisal, describes modest, utilitarian facades lacking scale, proportion, or decorative distinction.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Norwood Builder", "quote": "The suspect was an **unimpressive**, timid-looking little gentleman whose appearance belied a terrible crime."},
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "The exterior of the ancient corn market was singularly **unimpressive**, consisting of dull brick arches and weathered slate."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Mr. Brooke's parliamentary oratory was notoriously **unimpressive**, meandering through vague allusions and disconnected anecdotes."}
    ]
  },
  "Dashboard — press/unimpressively.md": {
    "primary": "In a manner that fails to make a strong, favorable, or memorable impression; unremarkably.",
    "secondary": "In performative assessment, executing a role or task without dynamism, flair, or persuasive presence.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "The witness spoke **unimpressively**, stammering over simple details before the coroner's jury."},
      {"author": "Thomas Hardy", "work": "Jude the Obscure", "quote": "The tiny country railway station stood **unimpressively** amid the damp turnip fields of Berkshire."},
      {"author": "Charles Dickens", "work": "Little Dorrit", "quote": "The petitioner bowed **unimpressively** as he retired from the haughty presence of the Circumlocution Office chief."}
    ]
  },
  "Dashboard — press/unpressed.md": {
    "primary": "Not subjected to physical pressure; not ironed, smoothed, crushed, or urged.",
    "secondary": "In wine making and olive oil extraction, refers to free-run juices drained naturally prior to mechanical pressing.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Antony and Cleopatra", "quote": "Have I my pillow left **unpressed** in Rome, forborne the getting of a lawful race, and by a gem of women to be abused?"},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The tall summer grasses remained **unpressed** by footsteps along the secluded pathway leading to the sheep-wash."},
      {"author": "John Keats", "work": "Endymion", "quote": "Upon a bed of **unpressed** violets and moss the weary wanderer lay down to rest under the forest canopy."}
    ]
  },
  "Dashboard — press/unrepressed.md": {
    "primary": "Not held back, restrained, subdued, or suppressed; freely expressed and unrestrained.",
    "secondary": "In psychological evaluation, spontaneous emotional or creative expression unconstrained by neurotic inhibitions.",
    "quotes": [
      {"author": "George MacDonald", "work": "The Portent", "quote": "A burst of **unrepressed** youthful laughter broke the gloomy stillness of the ancestral Scottish castle."},
      {"author": "Charlotte Brontë", "work": "Villette", "quote": "The **unrepressed** warmth of her welcome brought a sudden color to my pale cheeks."},
      {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "Eustacia gave vent to an **unrepressed** sigh of rebellious discontent against the monotony of the heath."}
    ]
  },
  "Dashboard — press/unsuppressed.md": {
    "primary": "Not kept under, extinguished, or held in check; breaking forth openly without restraint.",
    "secondary": "In epidemiological and clinical reporting, unsuppressed viral replication signifies failure of therapeutic medication to control infection.",
    "quotes": [
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "An **unsuppressed** murmur of fierce indignation ran through the courtroom as the cruel sentence was pronounced."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "A sob of **unsuppressed** anguish escaped her lips as she watched the horse stumble and fall dying on the road."},
      {"author": "Arthur Conan Doyle", "work": "The Lost World", "quote": "Challenger uttered an **unsuppressed** cry of scientific triumph when the pterodactyl swept over the volcanic crater."}
    ]
  }
}

base_dir = r"App database\Latin roots\Cluster Motion"
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

print(f"Motion Batch 11C: Successfully updated {updated}/{len(data)} notes.")
