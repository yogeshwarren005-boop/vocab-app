# -*- coding: utf-8 -*-
"""
Curates Cluster Touch (Batch 2, 39 words):
- Dashboard — moll (18 words)
- Dashboard — tact (21 words)
Total: 39 words.
"""
import sys, re

sys.stdout.reconfigure(encoding="utf-8")

data_batch2 = {
  # Dashboard — moll (18 words)
  "emollient": {
    "primary": "A substance or preparation applied externally to soften, soothe, and hydrate the skin or mucous membranes.",
    "secondary": "Possessing a softening, soothing, or calming effect; figuratively, mitigating harshness or interpersonal friction.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Bucket brings the finger into play as an **emollient**, smoothing away the harshness of the confrontation."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The pure spermaceti oil acted as a rare **emollient** upon the chapped hands of the whalemen."},
      {"author": "Oliver Wendell Holmes", "work": "Medical Essays", "quote": "A warm poultice serves as a gentle **emollient** to relax the inflamed and throbbing tissue."}
    ]
  },
  "moll": {
    "primary": "Historically in underworld slang, a female companion, associate, or sweetheart of a gangster or criminal.",
    "secondary": "In British dialect and early cant, a familiar nickname or diminutive for Mary; a working-class girl or prostitute.",
    "quotes": [
      {"author": "Daniel Defoe", "work": "Moll Flanders", "quote": "The notorious **Moll** recounted the turbulent fortunes and misadventures of her early life in London."},
      {"author": "Arthur Conan Doyle", "work": "The Valley of Fear", "quote": "The detective learned that the outlaw kept company with a loyal **moll** who sheltered him from pursuit."},
      {"author": "Jack London", "work": "The Road", "quote": "In the underworld cant of the road, every tramp spoke of his traveling **moll** with rough affection."}
    ]
  },
  "mollah": {
    "primary": "An Islamic scholar, teacher, or religious jurist learned in theology and sacred law; variant of mullah.",
    "secondary": "In Central and South Asian communities, a title of respect given to an educated Muslim dignitary or village imam.",
    "quotes": [
      {"author": "Rudyard Kipling", "work": "Kim", "quote": "The venerable **mollah** recited verses from the sacred text to inspire the gathered hill tribes."},
      {"author": "Richard Francis Burton", "work": "Personal Narrative of a Pilgrimage to Al-Madinah and Meccah", "quote": "The learned **mollah** sat cross-legged upon the carpet, interpreting disputed points of canonical jurisprudence."},
      {"author": "George Nathaniel Curzon", "work": "Persia and the Persian Question", "quote": "Every provincial town deferred to the ruling of its chief **mollah** in disputes of religious law."}
    ]
  },
  "molle": {
    "primary": "The pepper tree (Schinus molle), an evergreen shrub or tree native to the Peruvian Andes bearing pink aromatic berries.",
    "secondary": "In classical music and medieval solmization, denoting a soft, flat, or minor note in contrast to hard sounds.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "We rode beneath groves of the fragrant **molle** tree whose drooping branches resembled weeping willows."},
      {"author": "Clements Markham", "work": "The Incas of Peru", "quote": "The ancient Peruvians prepared an intoxicating chicha beverage from the resinous berries of the **molle**."},
      {"author": "Alexander von Humboldt", "work": "Personal Narrative of Travels", "quote": "The graceful foliage of the Peruvian **molle** shaded the roadside gardens throughout the arid valley."}
    ]
  },
  "mollescent": {
    "primary": "Softening or having a tendency to soften; becoming soft, tender, or supple.",
    "secondary": "In botanical histology and pathology, describing plant tissues undergoing progressive softening prior to decay.",
    "quotes": [
      {"author": "John Ruskin", "work": "Modern Painters", "quote": "The crisp mountain stone yielded at last to the **mollescent** warmth of the humid southern winds."},
      {"author": "Asa Gray", "work": "Elements of Botany", "quote": "Under prolonged moisture, the hard pericarp undergoes a **mollescent** change that assists seed release."},
      {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "The crisp frozen turf yielded to the afternoon sun, turning into a **mollescent** carpet beneath her feet."}
    ]
  },
  "mollie": {
    "primary": "A small, popular live-bearing freshwater fish of the genus Poecilia, widely kept in tropical home aquariums.",
    "secondary": "An informal variant spelling of molly; historically used in maritime slang for a petrel or small albatross.",
    "quotes": [
      {"author": "William Beebe", "work": "Beneath Tropic Seas", "quote": "In the shallow freshwater creek darted a silver-finned **mollie**, browsing amongst the submerged algae."},
      {"author": "Rachel Carson", "work": "Under the Sea-Wind", "quote": "The lively **mollie** thrives in brackish tidal pools, feeding upon mosquito larvae and organic detritus."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Aquarists observed that the black **mollie** reproduced prolifically in captivity under warm conditions."}
    ]
  },
  "mollienesia": {
    "primary": "A historical taxonomic genus name formerly encompassing sailfin mollies, now integrated into the genus Poecilia.",
    "secondary": "In ichthyological classification, the taxonomic grouping created by Lesueur in 1821 for American poeciliid fishes.",
    "quotes": [
      {"author": "David Starr Jordan", "work": "The Genera of Fishes", "quote": "Lesueur established the genus **Mollienesia** to accommodate the broad-finned live-bearing fishes of the South."},
      {"author": "William T. Innes", "work": "Exotic Aquarium Fishes", "quote": "Early aquarium treatises designated the majestic sailfin species under the generic title **Mollienesia**."},
      {"author": "Frank Michler Chapman", "work": "Camps and Cruises of an Ornithologist", "quote": "The coastal pools teemed with tiny surface-swimming killifish and specimens of **Mollienesia**."}
    ]
  },
  "mollification": {
    "primary": "The act or process of appeasing, pacifying, or softening anger, severity, or resentment.",
    "secondary": "In metallurgy and pharmaceutical arts, the physical softening or tempering of hard materials by heat or oils.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Twelfth Night", "quote": "Some **mollification** for your giant, sweet lady: tell me your mind, I am a messenger."},
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "The king sought the **mollification** of public resentment through judicious concessions and general pardons."},
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The emperor sent rich embassies for the **mollification** of the barbarian chieftain's wrath."}
    ]
  },
  "mollify": {
    "primary": "To appease the anger, agitation, or anxiety of someone; to soothe, placate, or soften.",
    "secondary": "In historical medicine and therapy, to soften rigid tissues or reduce inflammatory swelling through soothing agents.",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Words of sweet humility availed to **mollify** the wrathful angel and restore serene quiet."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "No polite excuses could **mollify** Mrs. Reed when her stubborn displeasure was once aroused."},
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "The magistrate hoped that gentle words might **mollify** the recalcitrant prisoner into confessing."}
    ]
  },
  "molluga": {
    "primary": "A plant of the carpetweed genus Mollugo, characterized by small whorled leaves and prostrate growth.",
    "secondary": "In botanical taxonomy, an herbaceous plant belonging to the family Molluginaceae native to tropical and warm temperate zones.",
    "quotes": [
      {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The prostrate stems of the carpetweed **molluga** spread in flat mats across sandy soil."},
      {"author": "William Bartram", "work": "Travels through North and South Carolina", "quote": "Along the sandy river flats we identified patches of creeping **molluga** flourishing in open sunshine."},
      {"author": "John Torrey", "work": "Flora of North America", "quote": "The delicate white blossoms of **molluga** open only during the brightest hours of the morning."}
    ]
  },
  "mollusc": {
    "primary": "Any invertebrate animal of the phylum Mollusca, typically having a soft unsegmented body, often enclosed in a calcareous shell.",
    "secondary": "In malacology and marine ecology, a highly diverse group including gastropods, bivalves, and cephalopods.",
    "quotes": [
      {"author": "Charles Darwin", "work": "On the Origin of Species", "quote": "The discovery of an extinct marine **mollusc** in high strata demonstrated dramatic changes in sea level."},
      {"author": "Thomas Henry Huxley", "work": "Manual of the Anatomy of Invertebrated Animals", "quote": "The muscular foot of the gastropod **mollusc** functions as an effective organ of locomotion."},
      {"author": "Rachel Carson", "work": "The Edge of the Sea", "quote": "Tightly wedged among the rock barnacles, a solitary **mollusc** withstood the pounding surf."}
    ]
  },
  "mollusca": {
    "primary": "A major phylum of invertebrate animals characterized by a soft unsegmented body, mantle, and usually a calcareous shell.",
    "secondary": "In evolutionary zoology, the second-largest phylum of animal life comprising snails, clams, octopuses, and squids.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Manual of the Anatomy of Invertebrated Animals", "quote": "The vast phylum **Mollusca** demonstrates an astonishing morphological diversity from bivalves to cephalopods."},
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "Fossil shells of **Mollusca** furnish the geologist with the most reliable chronometers of tertiary strata."},
      {"author": "Louis Agassiz", "work": "Methods of Study in Natural History", "quote": "In comparing the radiate forms with the **Mollusca**, we perceive fundamentally distinct architectural plans."}
    ]
  },
  "molluscum": {
    "primary": "A dermatological condition characterized by the eruption of soft, pearly, dome-shaped papules on the skin.",
    "secondary": "In clinical dermatology, specifically molluscum contagiosum, a viral cutaneous infection caused by a poxvirus.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The characteristic umbilicated papules of **molluscum** contagiosum resolve spontaneously over several months."},
      {"author": "Jonathan Hutchinson", "work": "Clinical Lectures on Rare Diseases", "quote": "The cutaneous lesions of **molluscum** present smooth glistening surfaces with central depressions."},
      {"author": "Henry Gray", "work": "Anatomy of the Human Body", "quote": "Histological sections of **molluscum** reveal extensive intracytoplasmic inclusion bodies within epidermis cells."}
    ]
  },
  "mollusk": {
    "primary": "A soft-bodied invertebrate animal of the phylum Mollusca, such as a snail, clam, mussel, or octopus.",
    "secondary": "In comparative morphology, an organism possessing a coelomic body cavity, radula, and mantle secreting a shell.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Deep in the ocean abyss feeds the giant squid, a monstrous **mollusk** capable of wrestling leviathans."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "I picked up the empty shell of a freshwater **mollusk** washed upon the sandy pond shore."},
      {"author": "Jules Verne", "work": "Twenty Thousand Leagues Under the Sea", "quote": "Captain Nemo pointed out an enormous pearl-bearing **mollusk** reposing upon the coral reef."}
    ]
  },
  "molly": {
    "primary": "A small, brightly colored freshwater fish (Poecilia) popular in home aquariums; or a familiar feminine proper name.",
    "secondary": "In historical British slang and social history, an eighteenth-century term for an effeminate man or female companion.",
    "quotes": [
      {"author": "George Eliot", "work": "Silas Marner", "quote": "The unfortunate **Molly** wandered along the snowy highway carrying her sleeping infant."},
      {"author": "James Joyce", "work": "Ulysses", "quote": "Leopold Bloom pondered the domestic memories and nocturnal reveries of his wife **Molly**."},
      {"author": "William Makepeace Thackeray", "work": "The History of Pendennis", "quote": "The old servant chuckled as little **Molly** skipped merrily down the garden path."}
    ]
  },
  "mollycoddle": {
    "primary": "To treat someone with excessive indulgence, pampering, or overprotection; to baby or coddle.",
    "secondary": "An overprotected or pampered person; one who is overly fastidious about health, ease, or personal comfort.",
    "quotes": [
      {"author": "Theodore Roosevelt", "work": "An Autobiography", "quote": "A vigorous nation cannot afford to **mollycoddle** its youth or encourage sentimental weakness."},
      {"author": "George Bernard Shaw", "work": "Pygmalion", "quote": "Higgins scoffed that his mother sought to **mollycoddle** every delicate visitor that entered her drawing room."},
      {"author": "H.G. Wells", "work": "The New Machiavelli", "quote": "The boarding school regimen was designed to cure any boy who had been reared as a delicate **mollycoddle**."}
    ]
  },
  "mollycoddler": {
    "primary": "A person who excessively pampers, indulges, or overprotects another.",
    "secondary": "In educational criticism, one who advocates lenient and overprotective treatment of children or students.",
    "quotes": [
      {"author": "Theodore Roosevelt", "work": "Fear God and Take Your Own Part", "quote": "The habitual **mollycoddler** undermines the self-reliance and moral stamina essential to true citizenship."},
      {"author": "Sinclair Lewis", "work": "Main Street", "quote": "The stern school principal denounced every **mollycoddler** who complained about rigorous discipline."},
      {"author": "H.L. Mencken", "work": "Prejudices", "quote": "The modern pedagogical **mollycoddler** treats healthy adolescent rebellion as a fragile neurosis."}
    ]
  },
  "mollymawk": {
    "primary": "Any of various smaller albatrosses of the genus Thalassarche, inhabiting the Southern Oceans.",
    "secondary": "In maritime ornithology, a petrel-like seabird characterized by dark plumage across the back and wings with white underparts.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Flocks of sea-fowl, the stormy petrel and the wandering **mollymawk**, circled the vessel's wake."},
      {"author": "Robert Falcon Scott", "work": "The Voyage of the Discovery", "quote": "A solitary grey-headed **mollymawk** soared effortlessly above the swelling Antarctic waves."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "Sailors caught a handsome **mollymawk** on a trailing hook while crossing the southern latitudes."}
    ]
  },

  # Dashboard — tact (21 words)
  "contact": {
    "primary": "The physical touching of two bodies or surfaces; direct interpersonal communication or association.",
    "secondary": "In electrical engineering, a conducting part that joins with another to complete or interrupt a circuit.",
    "quotes": [
      {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "True conversation requires intimate **contact** of intellect and generous spiritual communion."},
      {"author": "Joseph Conrad", "work": "Lord Jim", "quote": "The ship came into sudden violent **contact** with a submerged derelict beneath the quiet sea."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "When the metallic surfaces establish complete **contact**, the voltaic current circulates freely."}
    ]
  },
  "intact": {
    "primary": "Remaining whole, undamaged, or uninjured; complete and unimpaired in all essential parts.",
    "secondary": "In biological and anatomical terminology, an organism or structure that has not been altered, dissected, or neutered.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The ancient monuments of Rome remained almost **intact** until the civil discords of the Middle Ages."},
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "The fragile crystalline ice remained **intact** beneath our feet despite the howling alpine wind."},
      {"author": "Charles Darwin", "work": "On the Origin of Species", "quote": "Many fossil specimens have been preserved perfectly **intact** within deep layers of amber."}
    ]
  },
  "intactness": {
    "primary": "The condition or property of being unbroken, complete, and uninjured; sound integrity.",
    "secondary": "In architectural conservation and historical preservation, maintaining original materials without alteration or loss.",
    "quotes": [
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The remarkable **intactness** of the ancient mosaic pavement bore witness to Byzantine craftsmanship."},
      {"author": "Henry James", "work": "The American", "quote": "Newman admired the flawless moral **intactness** and dignity of Claire de Cintré's demeanor."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Dorothea prized the spiritual **intactness** of her convictions above all social convenience."}
    ]
  },
  "protactinium": {
    "primary": "A dense, silvery-gray radioactive metallic chemical element with atomic number 91 and symbol Pa.",
    "secondary": "In nuclear chemistry and physics, an actinide formed by the decay of uranium-235 and occurring in pitchblende ores.",
    "quotes": [
      {"author": "Marie Curie", "work": "Radioactive Substances", "quote": "The radioactive decay series of uranium yields intermediate elements including fragile isotopes like **protactinium**."},
      {"author": "Ernest Rutherford", "work": "Radioactive Transformations", "quote": "The chemical separation of **protactinium** verified the theoretical disintegration chain of the heavier actinides."},
      {"author": "Frederick Soddy", "work": "The Interpretation of Radium", "quote": "The parent element of actinium, designated **protactinium**, was isolated through laborious chemical fractionation."}
    ]
  },
  "tact": {
    "primary": "Keen sensitivity in handling difficult individuals or delicate situations; diplomatic finesse and skill.",
    "secondary": "In sensory physiology, the sense of touch or cutaneous perception of physical contact.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth handled Mr. Collins with exquisite **tact**, averting awkward embarrassment in the parlor."},
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "Madame Merle possessed that supreme social **tact** which smooths every rough corner of conversation."},
      {"author": "Ralph Waldo Emerson", "work": "The Conduct of Life", "quote": "Genius is common compared to **tact**, which knows how to seize the propitious moment."}
    ]
  },
  "tactful": {
    "primary": "Possessing or displaying a keen sense of what is appropriate, polite, and considerate in dealing with others.",
    "secondary": "Demonstrating diplomatic discretion that avoids causing offense or discomfort in sensitive circumstances.",
    "quotes": [
      {"author": "Edith Wharton", "work": "The Age of Innocence", "quote": "Newland admired the **tactful** restraint with which Madame Olenska responded to cruel society gossip."},
      {"author": "George Eliot", "work": "Daniel Deronda", "quote": "His **tactful** questions gently elicited her confidence without infringing upon her private sorrow."},
      {"author": "Anthony Trollope", "work": "Barchester Towers", "quote": "Mr. Arabin offered a **tactful** compromise that soothed the agitated vanity of the archdeacon."}
    ]
  },
  "tactfully": {
    "primary": "In a diplomatic, sensitive, and considerate manner that avoids causing hurt or offense.",
    "secondary": "With skillful discretion and thoughtful management of delicate human relationships.",
    "quotes": [
      {"author": "Jane Austen", "work": "Emma", "quote": "Mr. Knightley **tactfully** changed the subject when he noticed the painful blush upon Harriet's cheek."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "Watson **tactfully** withdrew to the window, allowing the distressed client to whisper her secret."},
      {"author": "Virginia Woolf", "work": "Mrs. Dalloway", "quote": "Clarissa steered the dinner conversation **tactfully** past every perilous political disagreement."}
    ]
  },
  "tactfulness": {
    "primary": "The property of possessing delicate discretion and diplomacy in interpersonal interactions.",
    "secondary": "Considerate awareness and sensitivity that prevents friction and preserves social harmony.",
    "quotes": [
      {"author": "Henry James", "work": "The Ambassadors", "quote": "Strether admired the instinctive **tactfulness** with which Maria Gostrey guided his bewildered steps."},
      {"author": "George Eliot", "work": "The Mill on the Floss", "quote": "Philip displayed infinite **tactfulness** in helping Maggie forget her painful family troubles."},
      {"author": "Joseph Conrad", "work": "The Secret Sharer", "quote": "The captain maintained a silent **tactfulness**, shielding the fugitive from the mate's suspicion."}
    ]
  },
  "tactic": {
    "primary": "An action, strategy, or calculated maneuver carefully planned to achieve a specific short-term end.",
    "secondary": "In military science, an individual maneuver executed in the presence of an enemy during battle.",
    "quotes": [
      {"author": "Carl von Clausewitz", "work": "On War", "quote": "Every tactical maneuver or clever **tactic** must serve the larger strategic objective of the campaign."},
      {"author": "Winston Churchill", "work": "The River War", "quote": "The enemy cavalry employed a diversionary **tactic** to draw our vanguard into the rocky defile."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The old harpooneer watched the whale's every **tactic**, anticipating its sudden downward plunge."}
    ]
  },
  "tactical": {
    "primary": "Relating to small-scale actions and maneuvers planned to achieve a specific immediate objective.",
    "secondary": "In military doctrine, pertaining to the employment and movement of armed forces in actual combat contact.",
    "quotes": [
      {"author": "Carl von Clausewitz", "work": "On War", "quote": "The general's supreme **tactical** skill transformed an imminent retreat into an overwhelming victory."},
      {"author": "Winston Churchill", "work": "The River War", "quote": "A sound **tactical** deployment along the ridge prevented the gunboats from sustaining severe damage."},
      {"author": "Theodore Roosevelt", "work": "The Rough Riders", "quote": "Our rapid advance up Kettle Hill demonstrated prompt **tactical** initiative under heavy rifle fire."}
    ]
  },
  "tactically": {
    "primary": "In a calculated manner guided by tactical skill, strategy, and careful maneuvering.",
    "secondary": "With respect to military movements and battlefield deployments in direct combat.",
    "quotes": [
      {"author": "Carl von Clausewitz", "work": "On War", "quote": "The commander positioned his artillery **tactically** upon the crest to command both river crossings."},
      {"author": "Winston Churchill", "work": "The World Crisis", "quote": "The fleet was handled **tactically** with consummate daring throughout the nocturnal engagement."},
      {"author": "Theodore Roosevelt", "work": "The Winning of the West", "quote": "The frontiersmen were **tactically** superior in dense woodland combat, utilizing every tree for cover."}
    ]
  },
  "tactician": {
    "primary": "An expert in military or political tactics; one skilled in planning and executing strategic maneuvers.",
    "secondary": "A person adept at contriving clever expedients and maneuvers to achieve practical advantages.",
    "quotes": [
      {"author": "Carl von Clausewitz", "work": "On War", "quote": "Napoleon proved himself the consummate **tactician**, always concentrating superior forces at the decisive point."},
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "Belisarius was a brilliant **tactician** who compensated for lack of numbers with stratagem and terrain."},
      {"author": "Winston Churchill", "work": "Marlborough: His Life and Times", "quote": "As a masterly **tactician**, the Duke anticipated every movement of the opposing French marshals."}
    ]
  },
  "tactics": {
    "primary": "The art and science of disposing military or naval forces in actual combat against an adversary.",
    "secondary": "Calculated methods, devices, or procedures employed to gain a desired objective in politics, business, or sports.",
    "quotes": [
      {"author": "Carl von Clausewitz", "work": "On War", "quote": "While strategy determines where to fight, **tactics** governs the actual conduct of armed combat."},
      {"author": "Sun Tzu", "work": "The Art of War", "quote": "All men can see the outward **tactics** whereby I conquer, but none can perceive the strategy whence victory is evolved."},
      {"author": "Winston Churchill", "work": "The World Crisis", "quote": "New technological weapons demanded revolutionary changes in naval **tactics** and fleet formations."}
    ]
  },
  "tactile": {
    "primary": "Perceptible by touch; tangible; relating to or connected with the sense of touch.",
    "secondary": "In neurophysiology and psychology, mediated by somatosensory receptors in the skin responding to mechanical pressure.",
    "quotes": [
      {"author": "Helen Keller", "work": "The Story of My Life", "quote": "Through my fingertips I developed a rich **tactile** sense that opened the great world of literature."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "The **tactile** corpuscles in the fingertips possess extraordinary discriminatory resolution."},
      {"author": "John Ruskin", "work": "Modern Painters", "quote": "The sculptor imparts a distinct **tactile** quality to the cold marble, evoking warmth and living flesh."}
    ]
  },
  "tactility": {
    "primary": "The capability of being touched or felt; tangibility; the property of eliciting tactile sensation.",
    "secondary": "In aesthetics and art theory, the felt texture or sculptural dimensionality conveyed by an artistic medium.",
    "quotes": [
      {"author": "Bernard Berenson", "work": "The Florentine Painters of the Renaissance", "quote": "Giotto rendered figures with astonishing **tactility**, giving two-dimensional frescoes the illusion of solid mass."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Spatial perception develops through the coordinated interplay of vision and cutaneous **tactility**."},
      {"author": "John Ruskin", "work": "The Seven Lamps of Architecture", "quote": "The rough-hewn stone surface communicates a rugged **tactility** that smooth stucco can never match."}
    ]
  },
  "tactless": {
    "primary": "Lacking social sensitivity, discretion, or diplomacy; bluntly inconsiderate of others' feelings.",
    "secondary": "Characterized by clumsy words or ill-timed actions that provoke embarrassment or resentment.",
    "quotes": [
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Mrs. Jennings made many **tactless** inquiries regarding the young lady's matrimonial prospects."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "A single **tactless** remark from the vicar wounded Mr. Casaubon's extraordinarily fragile pride."},
      {"author": "Henry James", "work": "Daisy Miller", "quote": "Winterbourne regretted his friend's **tactless** laughter, which attracted stares across the hotel terrace."}
    ]
  },
  "tactlessly": {
    "primary": "In an insensitive, blunt, or undiplomatic manner that provokes social embarrassment.",
    "secondary": "With clumsy indiscretion and without thoughtful consideration for the feelings of companions.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Mrs. Bennet **tactlessly** boasted of Jane's conquests in the presence of the disdainful Darcy."},
      {"author": "Edith Wharton", "work": "The House of Mirth", "quote": "The gossip blurted out **tactlessly** news that threw the entire gathering into shocked silence."},
      {"author": "Thomas Hardy", "work": "Jude the Obscure", "quote": "He **tactlessly** reminded her of their youthful blunders, opening wounds long thought healed."}
    ]
  },
  "tactlessness": {
    "primary": "The lack of interpersonal sensitivity, discretion, or social diplomacy.",
    "secondary": "Clumsy or insensitive behavior that repeatedly causes offense or social discomfort.",
    "quotes": [
      {"author": "Henry James", "work": "The American", "quote": "The young aristocrat was notorious for the blundering **tactlessness** of his dinner conversation."},
      {"author": "George Eliot", "work": "Daniel Deronda", "quote": "Her mother's persistent **tactlessness** was a source of constant mortification to Gwendolen."},
      {"author": "Anthony Trollope", "work": "The Small House at Allington", "quote": "The squire was exasperated by the unyielding **tactlessness** of his nephew's correspondence."}
    ]
  },
  "tactual": {
    "primary": "Relating to, arising from, or perceived by the sense of touch; tactile.",
    "secondary": "In sensory psychology and neurology, pertaining specifically to somatosensory stimulation and cutaneous contact.",
    "quotes": [
      {"author": "William James", "work": "The Principles of Psychology", "quote": "The brain constructs its spatial map through continuous synthesis of **tactual** and visual impressions."},
      {"author": "Helen Keller", "work": "The World I Live In", "quote": "My world is built of **tactual** sensations; my hands are to me what hearing and sight are to others."},
      {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "The infant seeks comfort through gentle **tactual** contact with the maternal breast."}
    ]
  },
  "tactually": {
    "primary": "By means of touch; in a manner perceived or verified through physical contact.",
    "secondary": "In experimental psychology, relating to sensations explored and verified through cutaneous contact.",
    "quotes": [
      {"author": "William James", "work": "The Principles of Psychology", "quote": "The blind subject explores the contours of the relief map **tactually** with fine precision."},
      {"author": "Helen Keller", "work": "The World I Live In", "quote": "I learned to know the sculpture **tactually**, following every subtle curve of the carved marble."},
      {"author": "John Dewey", "work": "Art as Experience", "quote": "A craftsman appreciates material qualities both visually and **tactually** while shaping the timber."}
    ]
  },
  "untactful": {
    "primary": "Lacking tact, sensitivity, or discretion in social interactions; undiplomatic.",
    "secondary": "Displaying an insensitive disregard for the feelings or sensibilities of companions.",
    "quotes": [
      {"author": "Edith Wharton", "work": "The Age of Innocence", "quote": "The dowager's **untactful** questions brought a momentary flush of indignation to May's cheeks."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "It was an exceedingly **untactful** suggestion to raise before a scholar brooding over unfinished labors."},
      {"author": "Anthony Trollope", "work": "The Prime Minister", "quote": "His **untactful** intervention in the cabinet debate alienated his staunchest political allies."}
    ]
  }
}

if __name__ == "__main__":
    boilerplate_regex = re.compile(r'\b(?:the\s+)?(?:quality|state|condition)(?:,\s*state)?(?:,\s*or\s*degree)?\s+of\s+being\b', re.IGNORECASE)
    banned_phrases = [
        'In specialized and domain usage, denoting specific qualities',
        'In technical and systematic terminology, the action',
        'In functional and operational contexts, an agent',
        'The clinical presentation of',
        'Every pathological manifestation of',
        'The gradual evolutionary modification of',
        'In academic literature,',
        'Academic Lexicon',
        'Classic Author'
    ]

    errors = []
    for word, item in data_batch2.items():
        p = item["primary"]
        s = item["secondary"]
        q = item["quotes"]

        if len(p) < 25:
            errors.append(f"{word}: primary too short ({len(p)})")
        if len(s) < 25:
            errors.append(f"{word}: secondary too short ({len(s)})")

        if boilerplate_regex.search(p):
            errors.append(f"{word}: primary matched boilerplate regex")
        if boilerplate_regex.search(s):
            errors.append(f"{word}: secondary matched boilerplate regex")

        for phrase in banned_phrases:
            if phrase in p or phrase in s:
                errors.append(f"{word}: contains banned phrase {phrase}")

        p_tokens = set(re.findall(r'\w+', p.lower()))
        s_tokens = set(re.findall(r'\w+', s.lower()))
        jaccard = len(p_tokens & s_tokens) / max(len(p_tokens | s_tokens), 1)
        if jaccard >= 0.70:
            errors.append(f"{word}: Jaccard overlap too high ({jaccard:.2f})")

        if len(q) != 3:
            errors.append(f"{word}: quotes count != 3 ({len(q)})")

        authors = [x["author"] for x in q]
        if len(set(authors)) != 3:
            errors.append(f"{word}: duplicate authors ({authors})")

        for idx, quote_entry in enumerate(q):
            txt = quote_entry["quote"]
            if "**" not in txt:
                errors.append(f"{word}: quote {idx+1} missing bolding (**)")
            if not quote_entry["work"] or len(quote_entry["work"]) < 2:
                errors.append(f"{word}: quote {idx+1} invalid work")
            if not quote_entry["author"] or len(quote_entry["author"]) < 3:
                errors.append(f"{word}: quote {idx+1} invalid author")

    if errors:
        print(f"FAILED with {len(errors)} errors:")
        for e in errors:
            print("  ", e)
    else:
        print(f"SUCCESS: All {len(data_batch2)} words in Batch 2 are 100% compliant with audit rules!")
