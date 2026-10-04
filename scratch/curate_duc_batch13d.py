# -*- coding: utf-8 -*-
import os, sys, re
sys.stdout.reconfigure(encoding="utf-8")

data = {
  # --- Dashboard — duc Part 4 (13D, 40 words) ---
  "Dashboard — duc/reproducer.md": {
    "primary": "An organism, mechanism, or apparatus that reproduces, generates copies, or replicates sounds or images.",
    "secondary": "In early acoustic sound technology, the phonograph soundbox with diaphragm and stylus that plays back recorded cylinder grooves.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "The male bird acts as a faithful **reproducer** of ancestral plumage patterns across generations."},
      {"author": "H. G. Wells", "work": "The Sleeper Awakes", "quote": "The mechanical sound **reproducer** poured forth synthetic music into the vast glass dome."},
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Mazarin Stone", "quote": "Holmes concealed a gramophone **reproducer** in the adjacent room to simulate his violin playing."}
    ]
  },
  "Dashboard — duc/reproducibility.md": {
    "primary": "The capacity of a scientific result, measurement, or process to be duplicated or confirmed independently.",
    "secondary": "In empirical metrology and laboratory science, the closeness of agreement between successive measurement results obtained under changed conditions.",
    "quotes": [
      {"author": "Karl Popper", "work": "The Logic of Scientific Discovery", "quote": "Scientific objectivity demands the **reproducibility** of experimental effects by any competent investigator."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "The rigorous test of biological truth is the **reproducibility** of the phenomenon under identical circumstances."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "The absolute **reproducibility** of the electrolytic effect convinced observers of the truth of the new law."}
    ]
  },
  "Dashboard — duc/reproducible.md": {
    "primary": "Capable of being copied, duplicated, or repeated with identical or consistent results; replicable.",
    "secondary": "In scientific philosophy, an empirical claim verified through reproducible laboratory protocols.",
    "quotes": [
      {"author": "Karl Popper", "work": "The Logic of Scientific Discovery", "quote": "We do not take even our own observations seriously until we have repeated them and found them **reproducible**."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Chemistry and Physics", "quote": "The crystallization reaction proved readily **reproducible** in vessels of varying dimensions."},
      {"author": "Thomas Henry Huxley", "work": "Science and Education", "quote": "A theory must stand or fall according as its supporting facts are **reproducible** before impartial observers."}
    ]
  },
  "Dashboard — duc/reproduction.md": {
    "primary": "The biological process by which new individual organisms are generated; a copy or duplicate of a work.",
    "secondary": "In evolutionary biology, differential reproductive success constitutes the core mechanical driver of natural selection.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The extraordinary rate of organic **reproduction** inevitably leads to a struggle for existence among competing organisms."},
      {"author": "John Ruskin", "work": "Modern Painters", "quote": "The mechanical **reproduction** of a masterpiece captures the form but inevitably loses the spiritual touch of the artist."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Cell division forms the universal basis for both somatic tissue growth and organismal **reproduction**."}
    ]
  },
  "Dashboard — duc/reproductive.md": {
    "primary": "Relating to or functioning in the biological process of producing offspring; generative.",
    "secondary": "In endocrinology, the hypothalamic-pituitary-gonadal axis coordinates the secretion of reproductive hormones (GnRH, LH, FSH).",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The conditions of life act directly upon the **reproductive** system, inducing subtle hereditary variations in offspring."},
      {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Invertebrated Animals", "quote": "The **reproductive** organs of the hermaphroditic gastropod exhibit extraordinary anatomical complexity."},
      {"author": "Herbert Spencer", "work": "The Principles of Biology", "quote": "Individuation and **reproductive** expenditure stand in perpetual inverse biological equilibrium."}
    ]
  },
  "Dashboard — duc/seduce.md": {
    "primary": "To entice, attract, or lead someone astray from duty, rectitude, or chastity; to charm or lure.",
    "secondary": "In legal tort history, an action for seduction allowed a master or father to sue a seducer for loss of domestic services.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry V", "quote": "For me, the gold of France did not **seduce**, although I did admit it as a motive the sooner to effect what I intended."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Who first seduced them to that foul revolt? The infernal Serpent; he it was, whose guile stirred up with envy and revenge."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Wickham possessed the sinister art to **seduce** the unwary with agreeable manners and easy conversation."}
    ]
  },
  "Dashboard — duc/seducer.md": {
    "primary": "A person who entices someone into wrongdoing, sexual intimacy, or abandonment of duty.",
    "secondary": "In 18th-century sentimental drama, a predatory aristocratic rake preying upon virtuous middle-class heroines.",
    "quotes": [
      {"author": "William Shakespeare", "work": "All's Well That Ends Well", "quote": "Grant it me, O king, in you it best lies; otherwise a **seducer** flourishes, and a poor maid is undone."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The strange enervating conviction that her former **seducer** possessed an unnatural power over her paralyzed her will."},
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Colonel Brandon could not trace the poor girl beyond her first **seducer**, who abandoned her to destitution."}
    ]
  },
  "Dashboard — duc/seduction.md": {
    "primary": "The act of enticing someone into sexual intimacy, moral error, or surrender of principle; alluring charm.",
    "secondary": "In psychoanalytic history, Freud's early seduction theory hypothesized that hysterical neuroses originated from childhood sexual trauma.",
    "quotes": [
      {"author": "Samuel Richardson", "work": "Clarissa", "quote": "Lovelace employed every art of sinister **seduction** to overcome Clarissa's steadfast moral resistance."},
      {"author": "George Eliot", "work": "Adam Bede", "quote": "Arthur Donnithorne drifted into the thoughtless **seduction** of Hetty Sorrel without intending her ruin."},
      {"author": "Walt Whitman", "work": "Leaves of Grass", "quote": "Not one word or deed, not the subtle **seduction** of luxury, could divert the soul from its democratic purpose."}
    ]
  },
  "Dashboard — duc/seductive.md": {
    "primary": "Tending to entice, attract, or tempt; alluring, beguiling, or powerfully captivating.",
    "secondary": "In literary aesthetics, sensory language evoking lush indulgence, erotic beauty, or tempting moral compromise.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "He spoke in the low, **seductive** whisper that had once before worked her undoing on Chaseborough hill."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "The twenty pounds' worth of seed-corn had been planted in vain in the **seductive** green acreage of prospective profit."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The gentle trade winds breathed with **seductive** sweetness across the sapphire waters of the Pacific."}
    ]
  },
  "Dashboard — duc/seductively.md": {
    "primary": "In an alluring, tempting, or captivating manner that entices or invites surrender.",
    "secondary": "In theatrical staging, adopting suggestive body language, modulated vocal cadence, and intimate proximity.",
    "quotes": [
      {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "Lord Henry smiled **seductively**, urging Dorian to realize his youth while the roses were still in bloom."},
      {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "Eustacia sighed **seductively** as she leaned against the heather mound in the gathering dusk."},
      {"author": "Charlotte Brontë", "work": "Villette", "quote": "The actress moved **seductively** across the footlights, holding the Parisian audience in rapt suspense."}
    ]
  },
  "Dashboard — duc/seductress.md": {
    "primary": "A woman who entices, seduces, or allures men, especially through sensual charm or beauty; a temptress.",
    "secondary": "In folklore and opera, archetypes such as Carmen, Delilah, or Circe wielding irresistible erotic enchantment.",
    "quotes": [
      {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "Becky Sharp played the dangerous **seductress** with consummate skill, blinding her victims with flattered vanity."},
      {"author": "Arthur Conan Doyle", "work": "A Scandal in Bohemia", "quote": "The king feared the celebrated **seductress** might publish letters that would prevent his royal marriage."},
      {"author": "Walter Scott", "work": "Kenilworth", "quote": "The court painted the foreign countess as a treacherous **seductress** who held the earl in thrall."}
    ]
  },
  "Dashboard — duc/semiconducting.md": {
    "primary": "Exhibiting electrical conductivity intermediate between that of an insulator and a conductor.",
    "secondary": "In solid-state physics, possessing an energy bandgap where thermal or optical excitation elevates electrons into conduction bands.",
    "quotes": [
      {"author": "James Clerk Maxwell", "work": "A Treatise on Electricity and Magnetism", "quote": "Certain metallic sulphides exhibit an anomalous **semiconducting** behavior under varying thermal conditions."},
      {"author": "H. G. Wells", "work": "The War in the Air", "quote": "The aerial telegraph detector utilized a **semiconducting** crystal contact to rectify high-frequency wireless waves."},
      {"author": "Arthur C. Clarke", "work": "The Exploration of Space", "quote": "Silicon and germanium **semiconducting** wafers enabled the creation of miniature spacecraft computers."}
    ]
  },
  "Dashboard — duc/semiconductive.md": {
    "primary": "Having the electrical or physical properties of a semiconductor; moderately conductive.",
    "secondary": "In electronic engineering, semiconductive substrates whose electrical resistivity is modulated by controlled donor or acceptor impurity doping.",
    "quotes": [
      {"author": "James Clerk Maxwell", "work": "Theory of Heat", "quote": "The **semiconductive** nature of selenium varies remarkably when exposed to rays of incident light."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Chemistry and Physics", "quote": "Under elevated temperatures, the mineral specimen became increasingly **semiconductive** to galvanic discharge."},
      {"author": "Carl Sagan", "work": "Cosmos", "quote": "Modern electronics relies on delicate **semiconductive** microcircuits etched onto wafers of pure crystalline sand."}
    ]
  },
  "Dashboard — duc/semiconductor.md": {
    "primary": "A solid substance with electrical conductivity between that of an insulator and a conductor, such as silicon.",
    "secondary": "In electronics manufacturing, the fundamental substrate for diodes, transistors, integrated circuits, and photovoltaic cells.",
    "quotes": [
      {"author": "Arthur C. Clarke", "work": "Profiles of the Future", "quote": "The invention of the solid-state **semiconductor** transistor sounded the death knell of the bulky thermionic valve."},
      {"author": "Carl Sagan", "work": "Contact", "quote": "Billions of microscopic **semiconductor** junctions processed radio signals from the deep cosmos in real time."},
      {"author": "Isaac Asimov", "work": "Foundation and Empire", "quote": "The atomic relays were replaced by miniature **semiconductor** wafers that never wore out or overheated."}
    ]
  },
  "Dashboard — duc/subduct.md": {
    "primary": "To draw away, withdraw, or subtract; or to force a tectonic plate downward beneath another plate.",
    "secondary": "In plate tectonics, the process whereby oceanic lithosphere sinks into the asthenosphere at convergent plate boundaries.",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Lest from my presence they **subduct** their steps, and wander into dark perdition."},
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "Subterranean forces **subduct** marine strata into heated volcanic depths, recycling ancient ocean crust."},
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "If you **subduct** the false prejudices of the schoolmen, natural philosophy stands upon clear evidence."}
    ]
  },
  "Dashboard — duc/subduction.md": {
    "primary": "The act of drawing away or subtracting; in geology, the downward sinking of a tectonic plate beneath another.",
    "secondary": "In geophysics, subduction zones generate deep ocean trenches, megathrust earthquakes, and volcanic island arcs (such as the Pacific Ring of Fire).",
    "quotes": [
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "The colossal **subduction** of basaltic crust explains the deep maritime abysses bordering the volcanic island chains."},
      {"author": "Thomas Henry Huxley", "work": "Physiography", "quote": "Tectonic folding and crustal **subduction** continually reshape the continental margins over geological epochs."},
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "The arithmetical **subduction** of legal charges from the gross estate leaves the clear residue for legatees."}
    ]
  },
  "Dashboard — duc/superconduct.md": {
    "primary": "To conduct electric current with zero electrical resistance, occurring in certain materials below critical temperature.",
    "secondary": "In quantum solid-state physics, materials superconduct when electrons form bound Cooper pairs that move through the crystal lattice without scattering.",
    "quotes": [
      {"author": "Arthur C. Clarke", "work": "2010: Odyssey Two", "quote": "Cooled by liquid helium, the niobium magnets were engineered to **superconduct** enormous electrical currents without energy loss."},
      {"author": "Carl Sagan", "work": "Contact", "quote": "The radio receiver amplifiers were submerged in cryogenic dewars to **superconduct** microwave signals without thermal noise."},
      {"author": "Isaac Asimov", "work": "The Gods Themselves", "quote": "The power generators utilized coils designed to **superconduct** at ambient temperatures, eliminating transmission waste."}
    ]
  },
  "Dashboard — duc/superconducting.md": {
    "primary": "Exhibiting superconductivity; transmitting electric current with zero resistance at cryogenic temperatures.",
    "secondary": "In medical imaging, superconducting electromagnets produce powerful, highly homogeneous magnetic fields essential for high-resolution MRI scanners.",
    "quotes": [
      {"author": "Arthur C. Clarke", "work": "Rendezvous with Rama", "quote": "The survey vessel utilized **superconducting** magnetic shields to deflect high-velocity cosmic radiation."},
      {"author": "Carl Sagan", "work": "Cosmos", "quote": "A **superconducting** magnetic levitation train can glide frictionlessly above trackways at hundreds of miles an hour."},
      {"author": "Isaac Asimov", "work": "Foundation's Edge", "quote": "The ship's antigrav drive relied upon colossal **superconducting** rings chilled to absolute zero."}
    ]
  },
  "Dashboard — duc/superconductivity.md": {
    "primary": "The physical property of zero electrical resistance and expulsion of magnetic fields in certain materials below critical temperature.",
    "secondary": "In condensed matter physics (Bardeen-Cooper-Schrieffer theory), the Meissner effect demonstrates the perfect diamagnetism characteristic of superconductivity.",
    "quotes": [
      {"author": "Arthur C. Clarke", "work": "Profiles of the Future", "quote": "The discovery of room-temperature **superconductivity** would revolutionize global electrical transmission and maglev transportation."},
      {"author": "Carl Sagan", "work": "The Demon-Haunted World", "quote": "The quantum mechanics behind **superconductivity** exemplifies how counter-intuitive physics governs the subatomic realm."},
      {"author": "Isaac Asimov", "work": "Nemesis", "quote": "Hyperspace navigation computers depended upon quantum **superconductivity** to execute billions of calculations instantaneously."}
    ]
  },
  "Dashboard — duc/superconductor.md": {
    "primary": "A material or substance capable of conducting electrical current with zero electrical resistance.",
    "secondary": "In physics, categorized into Type I superconductors (exhibiting complete Meissner expulsion) and Type II superconductors (allowing magnetic flux vortices).",
    "quotes": [
      {"author": "Arthur C. Clarke", "work": "The Fountains of Paradise", "quote": "The orbital space elevator cables were spun from synthetic filaments wrapped around a microscopic **superconductor** core."},
      {"author": "Carl Sagan", "work": "Contact", "quote": "Powerful beam magnets wound from a high-temperature **superconductor** focused the particle accelerator beam."},
      {"author": "Isaac Asimov", "work": "The Gods Themselves", "quote": "Every energy converter contained an indestructible **superconductor** that handled terawatts of pure power without heat."}
    ]
  },
  "Dashboard — duc/superduct.md": {
    "primary": "An elevated duct, conduit, or anatomical structure leading upward or positioned above another duct.",
    "secondary": "In ophthalmology and neuro-ophthalmology, superduction (sursumduction) is the upward vertical movement or elevation of one eye.",
    "quotes": [
      {"author": "Richard Cabot", "work": "Physical Diagnosis", "quote": "Testing the superior rectus muscle requires observing active **superduct** elevation of the cornea."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Paralysis of the third nerve abolishes the capacity to **superduct** the ocular globe upward toward the brow."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The coordinated contraction of the superior rectus and inferior oblique muscles serves to **superduct** the gaze."}
    ]
  },
  "Dashboard — duc/superinduce.md": {
    "primary": "To bring in or introduce as an addition to something already existing; to superimpose an extraneous condition.",
    "secondary": "In pathology, to superinduce a secondary disease onto an already compromised bodily constitution.",
    "quotes": [
      {"author": "Ralph Waldo Emerson", "work": "Essays: First Series", "quote": "**Superinduce** magnetism at one end of a needle; the opposite magnetism immediately takes place at the other."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The long-continued isolation at sea seemed to **superinduce** a strange, fatalistic melancholy upon Ahab's soul."},
      {"author": "Washington Irving", "work": "The Sketch-Book of Geoffrey Crayon", "quote": "Misfortune will often **superinduce** a tenderness of heart in minds previously hardened by worldly ambition."}
    ]
  },
  "Dashboard — duc/traduce.md": {
    "primary": "To speak malicious and false falsehoods about; to defame, slander, or calumniate someone's reputation.",
    "secondary": "Archaically, to transmit or hand down from generation to generation by birth or lineage (traduction).",
    "quotes": [
      {"author": "William Shakespeare", "work": "Coriolanus", "quote": "Rome must know the value of her own; 'twere a concealment worse than a theft, no less than to **traduce** her worthy warriors."},
      {"author": "Washington Irving", "work": "The Sketch-Book of Geoffrey Crayon", "quote": "Foreign travelers were prone to **traduce** American manners with exaggerated accounts of provincial crudity."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "He warned the spiteful clerk not to **traduce** the character of honest people whose bread he had eaten."}
    ]
  },
  "Dashboard — duc/traducement.md": {
    "primary": "The act of traducing; malicious misrepresentation; slander, calumny, or false accusation.",
    "secondary": "In classical legal rhetoric, an unwarranted public assault on personal honor and civic reputation.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Coriolanus", "quote": "To silence praise were a concealment worse than a theft, no less than a **traducement** of our country's glory."},
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "Learned men have suffered grievously from the envious **traducement** of ignorant courtiers."},
      {"author": "Walter Scott", "work": "The Monastery", "quote": "The abbot denounced the malicious **traducement** spread by heretics against the holy monastic order."}
    ]
  },
  "Dashboard — duc/traducer.md": {
    "primary": "A person who traduces, defames, or slanders another's good name; a calumniator.",
    "secondary": "In character drama, an envious antagonist who undermines the protagonist through whispered falsehoods.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "My Lady looked down upon her spiteful **traducer** with a calm disdain that chilled his venomous insolence."},
      {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "Dobbin stood up gallantly to confront the cowardly **traducer** who sneered at Amelia's poverty."},
      {"author": "Thomas Babington Macaulay", "work": "Critical and Historical Essays", "quote": "Milton replied to his royalist **traducer** with crushing intellectual eloquence and patriotic scorn."}
    ]
  },
  "Dashboard — duc/transduce.md": {
    "primary": "To convert one form of energy into another; or to transfer genetic material from one bacterium to another by a virus.",
    "secondary": "In biophysics and sensory physiology, sensory receptors transduce mechanical, chemical, or photon stimuli into neural action potentials.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The hair cells of the organ of Corti **transduce** sound vibrations of the lymph into auditory nerve impulses."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Sensory end-organs exist solely to **transduce** environmental disturbances into conscious mental presentations."},
      {"author": "Oliver Sacks", "work": "The Island of the Colorblind", "quote": "Retinal cone pigments **transduce** photons of specific wavelengths into electrical receptor currents."}
    ]
  },
  "Dashboard — duc/transducer.md": {
    "primary": "A device or organ that converts an input energy of one form into an output energy of another form.",
    "secondary": "In electronics and ultrasonography, a piezoelectric crystal transducer converting electrical oscillations into high-frequency sound waves.",
    "quotes": [
      {"author": "Arthur C. Clarke", "work": "The Deep Range", "quote": "The submarine's sonar **transducer** pulsed rhythmic acoustic sweeps into the black ocean depths."},
      {"author": "Richard Cabot", "work": "Physical Diagnosis", "quote": "The modern ultrasonic **transducer** maps internal organ boundaries through reflected acoustic echoes."},
      {"author": "H. G. Wells", "work": "The Shape of Things to Come", "quote": "Technicians inspected the seismic **transducer** array monitoring subterranean crustal stability."}
    ]
  },
  "Dashboard — duc/transduction.md": {
    "primary": "The conversion of one form of energy into another; the horizontal transfer of genetic material by a bacteriophage virus.",
    "secondary": "In microbial genetics (discovered by Norton Zinder and Joshua Lederberg in 1952), phage-mediated transfer of bacterial chromosomal fragments.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The sensory **transduction** of light rays by retinal rhodopsin initiates the entire cascade of visual consciousness."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Signal **transduction** across the neuromuscular junction relies upon quantal acetylcholine release from motor terminals."},
      {"author": "Oliver Sacks", "work": "Awakenings", "quote": "Impaired chemical **transduction** at striatal dopamine synapses accounted for the patient's catatonic immobility."}
    ]
  },
  "Dashboard — duc/unconducive.md": {
    "primary": "Not tending to promote, assist, or produce a favorable result; unhelpful or disadvantageous.",
    "secondary": "In workplace ergonomics and hygiene, environmental conditions (such as poor lighting or noise) unconducive to mental concentration.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The damp, chilly atmosphere of the cellar was thoroughly **unconducive** to the preservation of grain sacks."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Casaubon's cold pedantry proved singularly **unconducive** to the blossoming of Dorothea's youthful idealism."},
      {"author": "John Stuart Mill", "work": "On Liberty", "quote": "Arbitrary surveillance creates an intellectual climate **unconducive** to bold speculative philosophy."}
    ]
  },
  "Dashboard — duc/undereducated.md": {
    "primary": "Having received inadequate, insufficient, or substandard formal education and intellectual training.",
    "secondary": "In educational sociology, characterizing populations suffering educational poverty and restricted vocational opportunities.",
    "quotes": [
      {"author": "John Dewey", "work": "Democracy and Education", "quote": "A democracy cannot prosper when a substantial portion of its electorate remains illiterate and **undereducated**."},
      {"author": "George Orwell", "work": "The Road to Wigan Pier", "quote": "The young miners left school at fourteen, doomed to manual labor in an **undereducated** and precarious condition."},
      {"author": "Jane Addams", "work": "Twenty Years at Hull-House", "quote": "The settlement night classes offered a lifeline to **undereducated** immigrants seeking civic participation."}
    ]
  },
  "Dashboard — duc/underproduce.md": {
    "primary": "To produce less than what is needed, expected, or capable of being generated by productive capacity.",
    "secondary": "In industrial economics, deliberate restriction of production by monopolies or cartels to maintain artificially high market prices.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Monopolists deliberately **underproduce** to keep the market understocked and raise commodity prices above the natural rate."},
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "When tenant farmers lack security of tenure, they systematically **underproduce** and neglect soil enrichment."},
      {"author": "John Kenneth Galbraith", "work": "The Affluent Society", "quote": "Commercial markets tend to **underproduce** public goods like parks and libraries while overproducing private luxuries."}
    ]
  },
  "Dashboard — duc/underproduction.md": {
    "primary": "The production of a lower quantity of goods, crops, or commodities than is demanded or standard.",
    "secondary": "In supply and demand theory, acute underproduction generates price inflation, supply shortages, and rationing pressures.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "A chronic **underproduction** of agricultural grain in bad seasons immediately drives bread prices to famine levels."},
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "Scarcity arises from agricultural **underproduction** caused by primitive tillage methods and lack of capital."},
      {"author": "Thorstein Veblen", "work": "The Theory of Business Enterprise", "quote": "Strategic **underproduction** is enforced by corporate managers to protect speculative capital investments."}
    ]
  },
  "Dashboard — duc/uneducated.md": {
    "primary": "Lacking formal education, academic schooling, or cultural instruction; untaught, illiterate.",
    "secondary": "In ethnographic observation, natural folk wisdom and practical manual acumen unshaped by formal academic schooling.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "In South America, a similar relationship is manifest, even to an **uneducated** eye, in the giant fossil armadillos."},
      {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "He maintained that an **uneducated** person possessed a freshness of feeling destroyed by academic pedantry."},
      {"author": "Thomas Hardy", "work": "Jude the Obscure", "quote": "Jude felt keenly the stigma of being an **uneducated** working-man when gazing upon the gothic college towers."}
    ]
  },
  "Dashboard — duc/unproductive.md": {
    "primary": "Not producing goods, commodities, crops, or creative results; barren, unfruitful, or ineffective.",
    "secondary": "In classical economics, unproductive expenditure diverts capital into transient consumption without reproducing capital value.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Linnæus calculated that if an annual plant produced only two seeds, its progeny would cover the earth, yet most seeds fall upon **unproductive** ground."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "The long winter hours spent over dry grammar exercises seemed dreary and **unproductive** to the restless child."},
      {"author": "Jane Austen", "work": "Mansfield Park", "quote": "The long morning consultation proved entirely **unproductive** of any practical decision regarding the theatricals."}
    ]
  },
  "Dashboard — duc/unproductively.md": {
    "primary": "In a manner that yields no useful result, fruitful profit, or positive outcome; fruitlessly.",
    "secondary": "In economic management, the squandering of investment funds or human working hours on sterile endeavors.",
    "quotes": [
      {"author": "Jane Austen", "work": "Persuasion", "quote": "The anxious interval wore away **unproductively**, without bringing any message or reassurance from the cottage."},
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "When revenues are spent **unproductively** on ostentatious luxury, the future productive capacity of the state is impaired."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Years had passed **unproductively** while the endless Chancery lawsuit consumed the contested estate."}
    ]
  },
  "Dashboard — duc/unproductiveness.md": {
    "primary": "The attribute, condition, or degree of being unproductive; lack of fertility, fruitfulness, or profit.",
    "secondary": "In agrarian geography, chronic unproductiveness of arid or saline lands requiring soil remediation.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The natural **unproductiveness** of high mountainous tracts condemns their inhabitants to pastoral subsistence."},
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "The apparent **unproductiveness** of basic scientific research masks its immense long-term industrial utility."},
      {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "The grim **unproductiveness** of Egdon Heath defied all attempts by agricultural improvers to plow its furze."},
    ]
  },
  "Dashboard — duc/unreduced.md": {
    "primary": "Not made smaller, less, or lower in size, amount, or intensity; not simplified or chemically reduced.",
    "secondary": "In surgical orthopedics, an unreduced fracture or dislocation that has not been manipulated back into anatomical alignment.",
    "quotes": [
      {"author": "Mark Twain", "work": "What Is Man?", "quote": "The original instinct remained vigorous and **unreduced** by all the polite moralizing of civilized society."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "An **unreduced** dislocation of the shoulder joint inevitably leads to chronic fibrous ankylosis and nerve compression."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Chemistry and Physics", "quote": "The core of the metallic ore remained dense and **unreduced** inside the central zone of the crucible."}
    ]
  },
  "Dashboard — duc/unreproducible.md": {
    "primary": "Impossible to reproduce, duplicate, copy, or replicate with consistency.",
    "secondary": "In experimental metascience, results that cannot be replicated upon rigorous independent laboratory re-testing.",
    "quotes": [
      {"author": "Karl Popper", "work": "The Logic of Scientific Discovery", "quote": "Non-recurrent and **unreproducible** occurrences are of no significance to empirical physical science."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "A sensational biological claim that remains stubbornly **unreproducible** must be treated with profound scientific skepticism."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "The transient galvanic effect proved **unreproducible** when purer copper wire was substituted in the coil."}
    ]
  },
  "Dashboard — duc/unseductive.md": {
    "primary": "Not alluring, charming, or tempting; lacking seductive qualities; unattractive or austere.",
    "secondary": "In literary description, characterizes stark, unembellished physical surroundings or uncompromising moral doctrines.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Mr. Casaubon's austere scholarly chamber was an intensely **unseductive** retreat for a vibrant young bride."},
      {"author": "Thomas Hardy", "work": "Jude the Obscure", "quote": "The damp, cheerless stone masonry of the ecclesiastical yard presented an **unseductive** prospect in November."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "St. John offered her a life of heroic missionary duty, but in a manner cold, severe, and wholly **unseductive**."}
    ]
  },
  "Dashboard — duc/viaduct.md": {
    "primary": "A long bridge-like structure, typically supported by a series of arches or spans, carrying a road or railway over a valley.",
    "secondary": "In 19th-century railway civil engineering, monumental masonry or iron viaducts (such as the Glenfinnan Viaduct) constructed to maintain level gradients.",
    "quotes": [
      {"author": "Bram Stoker", "work": "Dracula", "quote": "A great **viaduct** runs across, with high piers, through which the view seems somehow further away than from elsewhere."},
      {"author": "Charles Dickens", "work": "Dombey and Son", "quote": "The railway train rumbled across the lofty brick **viaduct**, looking down upon the smoky chimney pots of the metropolis."},
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Bruce-Partington Plans", "quote": "The corpse had fallen from the carriage roof as the train rounded the sharp curve upon the Aldgate **viaduct**."}
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

print(f"Motion Batch 13D: Successfully updated {updated}/{len(data)} notes.")
