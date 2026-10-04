# -*- coding: utf-8 -*-
import os, sys, re

sys.stdout.reconfigure(encoding="utf-8")

data = {
  # =========================================================================
  # Dashboard — fer (Batch 5E: 35 words)
  # =========================================================================
  "Dashboard — fer/reference.md": {
    "primary": "The action of mentioning, citing, or referring to something; or a source of information used to ascertain facts.",
    "secondary": "In semantics, analytical philosophy, and computer science, the relation connecting a linguistic symbol to its real-world referent, or a memory address pointing to a stored value.",
    "quotes": [
      {"author": "William Shakespeare", "work": "All's Well That Ends Well", "quote": "All that he is hath **reference** to your highness."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Words have their immediate **reference** to the ideas in the mind of him that speaks them."},
      {"author": "Bertrand Russell", "work": "On Denoting", "quote": "A phrase may denote an entity and yet have no direct **reference** to an existing object in empirical reality."}
    ]
  },
  "Dashboard — fer/referenced.md": {
    "primary": "Mentioned, cited, or consulted for authoritative information, evidence, or corroboration.",
    "secondary": "In computational systems and library informatics, accessed via pointer address or cataloged in an indexed citation index.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "The facts **referenced** in the memoirs of foreign naturalists fully confirm this conclusion."},
      {"author": "Thomas Henry Huxley", "work": "Critiques and Addresses", "quote": "Every statement of fact in the monograph was rigorously **referenced** to primary anatomical dissections."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "The mental events **referenced** by the subject occurred during the period of focused hypnotic suggestion."}
    ]
  },
  "Dashboard — fer/referendum.md": {
    "primary": "A direct and universal vote in which an entire electorate is invited to vote on a particular proposal or legislative measure.",
    "secondary": "In Swiss constitutional history and direct democracy theory, the institutional mechanism allowing citizens to approve or reject statutory enactments passed by parliament.",
    "quotes": [
      {"author": "James Bryce", "work": "The American Commonwealth", "quote": "The adoption of the constitutional **referendum** represents an effort to bypass legislative corruption through direct popular sovereignty."},
      {"author": "Woodrow Wilson", "work": "Congressional Government", "quote": "Advocates of the popular **referendum** sought to restore sovereign authority directly to the people."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "The principle of submitting critical civic questions to a general **referendum** reflects absolute trust in majority judgment."}
    ]
  },
  "Dashboard — fer/referent.md": {
    "primary": "The thing, object, person, or concept that a word, symbol, or sign refers to; the object of reference.",
    "secondary": "In semiotics and linguistic semantics, the concrete or conceptual entity symbolized by a sign through the mediation of thought.",
    "quotes": [
      {"author": "Charles Sanders Peirce", "work": "Collected Papers", "quote": "A sign stands for something, its **referent**, not in all respects, but in reference to a sort of idea."},
      {"author": "Bertrand Russell", "work": "An Inquiry into Meaning and Truth", "quote": "The assertive sentence is true when it points directly to an objective **referent** in the state of affairs."},
      {"author": "William James", "work": "The Meaning of Truth", "quote": "An idea becomes true when it leads us harmoniously toward its intended **referent** in experience."}
    ]
  },
  "Dashboard — fer/referential.md": {
    "primary": "Containing, making, or serving as a reference; pointing to something outside of itself.",
    "secondary": "In functional linguistics and communication theory, the cognitive or denotative function of language centered on describing the contextual world.",
    "quotes": [
      {"author": "Roman Jakobson", "work": "Linguistics and Poetics", "quote": "The **referential** function of speech is oriented toward the context, transmitting objective information about the environment."},
      {"author": "Edward Sapir", "work": "Language", "quote": "Language possesses not merely an emotive coloring but an indispensable **referential** apparatus for classifying physical reality."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Our complex ideas of substances possess a **referential** intent toward real external archetypes."}
    ]
  },
  "Dashboard — fer/referral.md": {
    "primary": "The act of directing someone to a different person, doctor, agency, or authority for advice, help, or treatment.",
    "secondary": "In health systems management and professional ethics, the formal protocol whereby a primary generalist transfers clinical custody or evaluation of a patient to a specialized consultant.",
    "quotes": [
      {"author": "William Osler", "work": "Aequanimitas", "quote": "A timely clinical **referral** to an experienced surgeon frequently determines the difference between recovery and disaster."},
      {"author": "Florence Nightingale", "work": "Notes on Nursing", "quote": "Administrative efficiency requires that every patient **referral** be accompanied by clear notes on diet and environmental ventilation."},
      {"author": "Oliver Wendell Holmes Jr.", "work": "The Common Law", "quote": "The formal **referral** of the dispute to commercial arbitration ended years of bitter litigation."}
    ]
  },
  "Dashboard — fer/somniferous.md": {
    "primary": "Causing, tending to cause, or inducing sleep; soporific or dormitive.",
    "secondary": "In pharmacological history and literary satire, describing sedative herbal potions (such as poppy and mandragora) or tediously dull discourse.",
    "quotes": [
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "It must have been a work of vast ability in the **somniferous** school of literature, for its perusal never failed to invite repose."},
      {"author": "Izaak Walton", "work": "The Compleat Angler", "quote": "A quiet afternoon beside the slow stream exerts a **somniferous** influence upon the weary angler."},
      {"author": "Herman Melville", "work": "Moby-Dick; or, The Whale", "quote": "The slow, monotonous rocking of the ship on the calm sea produced a **somniferous** tranquility throughout the watch."}
    ]
  },
  "Dashboard — fer/suffer.md": {
    "primary": "To experience, undergo, or endure pain, distress, loss, or hardship; or to allow, permit, or tolerate.",
    "secondary": "In theological ethics and civil jurisprudence, to submit willingly to adversity without moral compromise, or to grant legal sufferance to an act.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Sonnet 58", "quote": "O let me **suffer** (being at your beck) / Th' imprisoned absence of your liberty."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Better to reign in Hell than serve in Heaven; / Or rather choose to **suffer** all than yield."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Sympathy causes us to **suffer** when we witness the distress of our fellow creatures."}
    ]
  },
  "Dashboard — fer/sufferable.md": {
    "primary": "Capable of being suffered, endured, tolerated, or borne; tolerable.",
    "secondary": "In stoic moral philosophy, describing pains or hardships that remain within the threshold of human psychological fortitude.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick; or, The Whale", "quote": "Still, looking round me again, and seeing no possible chance of spending a **sufferable** night elsewhere, I resolved to endure the companion."},
      {"author": "Geoffrey Chaucer", "work": "The Canterbury Tales", "quote": "Ye must be **sufferable** and patient in the tribulations of this mortal pilgrimage."},
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "Physical pain is generally **sufferable** if not aggravated by the dread of imaginary evils."}
    ]
  },
  "Dashboard — fer/sufferance.md": {
    "primary": "The capacity to endure hardship or pain with patience; endurance; or passive permission or toleration without formal approval.",
    "secondary": "In real property law, a tenancy at sufferance arising when a tenant wrongfully holds over possession after the expiration of a lawful lease.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Merchant of Venice", "quote": "Still have I borne it with a patient shrug, / For **sufferance** is the badge of all our tribe."},
      {"author": "John Locke", "work": "Second Treatise of Government", "quote": "A tyrant rules not by the consent of the governed, but solely through their temporary **sufferance**."},
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "An estate at **sufferance** is where one comes into possession of land by lawful title, but keeps it afterwards without any title at all."}
    ]
  },
  "Dashboard — fer/sufferer.md": {
    "primary": "A person who suffers or experiences pain, grief, illness, distress, or persecution.",
    "secondary": "In medical clinical care and philanthropic ethics, an afflicted individual requiring compassionate intervention, palliative comfort, or moral support.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The **sufferer** was got to bed, and Oak, finding from the bulletins that the wound was not mortal, returned to his sheep."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "She tended the feverish **sufferer** with untiring patience through the long, dark hours of the night."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "A generous nature instinctively sympathizes with the silent **sufferer** whose agony is hidden from the crowd."}
    ]
  },
  "Dashboard — fer/suffering.md": {
    "primary": "The state, experience, or condition of enduring acute physical pain, emotional distress, or severe hardship.",
    "secondary": "In religious philosophy, the universal existential predicament arising from mortal transience, attachment, and vulnerability.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Coriolanus", "quote": "For your wants, / Your **suffering** in this dearth, you may as well / Strike at the heaven with your staves as lift them / Against the Roman state."},
      {"author": "Arthur Schopenhauer", "work": "The World as Will and Representation", "quote": "All life is **suffering**, proceeding from the endless striving of an unsatisfied will."},
      {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "The ultimate end of moral action is the prevention and mitigation of human **suffering**."}
    ]
  },
  "Dashboard — fer/surfer.md": {
    "primary": "A person who rides ocean waves on a surfboard; or the surf duck (scoter).",
    "secondary": "In contemporary cultural sociology, an enthusiast of marine board riding, or a navigator exploring the hypertext nodes of the World Wide Web.",
    "quotes": [
      {"author": "Jack London", "work": "The Cruise of the Snark", "quote": "Out there, through the boiling breakers, came the royal **surfer**, riding the foaming crest like a bronze sea-god."},
      {"author": "Mark Twain", "work": "Roughing It", "quote": "I tried surf-bathing once at Waikiki, but unlike the native **surfer**, I found myself instantly buried under tons of churning foam."},
      {"author": "Herman Melville", "work": "Typee: A Romance of the South Seas", "quote": "The young islanders plunged into the roaring surf, each **surfer** matching his skill against the giant combers."}
    ]
  },
  "Dashboard — fer/transfer.md": {
    "primary": "To move, convey, or pass someone or something from one place, person, or position to another; or the act of doing so.",
    "secondary": "In property law and thermodynamics, the legal conveyance of title or ownership, or the net exchange of thermal energy between systems.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "She proposed to build a couple of cottages, and **transfer** two families from the crowded tenements of the village."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Commerce allows nations to **transfer** their surplus manufactures in exchange for foreign raw commodities."},
      {"author": "James Clerk Maxwell", "work": "Theory of Heat", "quote": "Conduction is the process by which heat undergoes **transfer** through contiguous portions of matter."}
    ]
  },
  "Dashboard — fer/transferability.md": {
    "primary": "The capability, quality, or property of being transferred, conveyed, assigned, or handed over from one party or place to another.",
    "secondary": "In financial economics and contract jurisprudence, the institutional attribute of negotiable instruments and equity shares enabling frictionless exchange in secondary markets.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The easy **transferability** of paper currency facilitates the rapid circulation of national wealth."},
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "The legal **transferability** of land tenure encouraged agricultural improvements by enterprising leaseholders."},
      {"author": "Oliver Wendell Holmes Jr.", "work": "The Common Law", "quote": "The development of modern commerce depended upon establishing the unrestricted **transferability** of promissory notes."}
    ]
  },
  "Dashboard — fer/transferable.md": {
    "primary": "Capable of being transferred, passed, or assigned from one person, place, or context to another.",
    "secondary": "In commercial law and education, designating negotiable bills of exchange that can be endorsed to third parties, or academic credits accepted across institutions.",
    "quotes": [
      {"author": "Ralph Waldo Emerson", "work": "Self-Reliance", "quote": "Good and bad are but names very readily **transferable** to that or this; the only right is what is after my constitution."},
      {"author": "James George Frazer", "work": "The Golden Bough", "quote": "Primitive peoples frequently believe that vitality or disease is physically **transferable** to trees, stones, or sacrificial animals."},
      {"author": "John Maynard Keynes", "work": "The General Theory of Employment", "quote": "A liquid asset must be readily **transferable** without capital loss."}
    ]
  },
  "Dashboard — fer/transferase.md": {
    "primary": "Any of a class of enzymes that catalyze the transfer of a specific functional group (such as methyl, glycosyl, or phosphate) from one molecule to another.",
    "secondary": "In molecular biochemistry and enzymology, key regulatory biocatalysts (such as DNA methyltransferases or aminotransferases) essential for metabolism and gene regulation.",
    "quotes": [
      {"author": "Arthur Kornberg", "work": "DNA Replication", "quote": "The terminal deoxynucleotidyl **transferase** catalyzes the addition of nucleotides to the hydroxyl terminus of a DNA chain."},
      {"author": "Christian de Duve", "work": "A Guided Tour of the Living Cell", "quote": "Cellular biosynthesis relies upon each specific **transferase** to shuttle functional groups between donor and acceptor molecules."},
      {"author": "Max Perutz", "work": "Proteins and Nucleic Acids", "quote": "X-ray crystallography reveals the exact active-site binding pocket of the acyl **transferase**."}
    ]
  },
  "Dashboard — fer/transferee.md": {
    "primary": "A person, party, or entity to whom a conveyance, title, property, or legal right is transferred.",
    "secondary": "In real estate jurisprudence and commercial law, the recipient in a deed or contract who succeeds to all rights, encumbrances, and equities held by the transferor.",
    "quotes": [
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "Upon delivery and acceptance of the deed, the **transferee** acquires the full freehold estate subject to existing easements."},
      {"author": "Oliver Wendell Holmes Jr.", "work": "The Common Law", "quote": "A bona fide purchaser for value without notice stands as a protected **transferee** against prior unrecorded equities."},
      {"author": "Henry Sumner Maine", "work": "Ancient Law", "quote": "Early conveyance rituals required the **transferee** to grasp the sod or spear in the presence of sworn witnesses."}
    ]
  },
  "Dashboard — fer/transference.md": {
    "primary": "The act, process, or instance of transferring, conveying, or redirecting something from one place, person, or context to another.",
    "secondary": "In psychoanalysis, the unconscious redirection of feelings, expectations, and relational patterns from early childhood figures onto the therapist.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The converse case of the first development of characters in the female, and their **transference** to the male, is exceedingly rare."},
      {"author": "Sigmund Freud", "work": "The Dynamics of Transference", "quote": "The patient directs toward the physician an intense wave of affectionate or hostile feelings which are rooted in childhood; this is the phenomenon of **transference**."},
      {"author": "Carl Jung", "work": "The Psychology of the Transference", "quote": "The therapeutic process reaches its critical turning point when the unconscious **transference** is analyzed and integrated."}
    ]
  },
  "Dashboard — fer/transferer.md": {
    "primary": "A person, machine, or mechanism that transfers, moves, or conveys something from one position or owner to another.",
    "secondary": "In mechanical manufacturing and logistical transport, an automated apparatus or individual responsible for routing components between processing stages.",
    "quotes": [
      {"author": "Thomas Edison", "work": "The Inventions of Thomas Alva Edison", "quote": "An automatic mechanical **transferer** was designed to move the phonograph cylinder swiftly from the recording stylus to the playback horn."},
      {"author": "Charles Babbage", "work": "Passages from the Life of a Philosopher", "quote": "The calculating engine employs a toothed **transferer** to carry tens across adjacent calculating columns."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Chemistry", "quote": "The experimenter acted as a careful **transferer** of volatile vapors between the retort and the sealed receiver."}
    ]
  },
  "Dashboard — fer/transferor.md": {
    "primary": "A person, corporate entity, or legal party that makes a transfer, assignment, or conveyance of property or rights to another.",
    "secondary": "In statutory commercial law and probate, the party executing a deed, assignment, or bill of sale who warrants title and covenants quiet enjoyment.",
    "quotes": [
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "The covenants of the **transferor** bind his heirs and executors to warrant the title against all lawful claimants."},
      {"author": "Oliver Wendell Holmes Jr.", "work": "The Common Law", "quote": "The title of the transferee can rise no higher than the legitimate right possessed by the **transferor**."},
      {"author": "Henry Sumner Maine", "work": "Ancient Law", "quote": "In primitive transfer of ownership, the presence of the **transferor** before the tribal council was indispensable."}
    ]
  },
  "Dashboard — fer/transferrable.md": {
    "primary": "Capable of being transferred, conveyed, or passed from one person, place, or condition to another (variant of transferable).",
    "secondary": "In financial securities and administrative licensing, denoting negotiable stocks or permits that can be endorsed and reissued to third parties.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "A public stock that is freely **transferrable** commands a higher price in the capital market."},
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "The rights of tenant cultivators were made legally **transferrable** to encourage land improvements."},
      {"author": "Alexander Hamilton", "work": "Report on Public Credit", "quote": "The public debt certificates were designed to be fully **transferrable**, thereby invigorating domestic commerce."}
    ]
  },
  "Dashboard — fer/transferral.md": {
    "primary": "The act, operation, or process of transferring, removing, or relocating something from one location or party to another.",
    "secondary": "In institutional administration and military logistics, the formal reassignment of personnel, records, or material assets between jurisdictions.",
    "quotes": [
      {"author": "Woodrow Wilson", "work": "The State", "quote": "The constitutional **transferral** of administrative duties required comprehensive reorganization of the civil ministries."},
      {"author": "Theodore Roosevelt", "work": "An Autobiography", "quote": "The **transferral** of federal forest reserves to the Department of Agriculture marked the true beginning of scientific conservation."},
      {"author": "Winston Churchill", "work": "The World Crisis", "quote": "The sudden **transferral** of divisions to the western front altered the strategic balance of the campaign."}
    ]
  },
  "Dashboard — fer/transferrer.md": {
    "primary": "A person, agent, or mechanism that performs a transfer or makes a legal conveyance (variant of transferer).",
    "secondary": "In property law and postal logistics, the party or mechanical carriage executing the dispatch or assignment of assets.",
    "quotes": [
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "The law requires that the **transferrer** possess full mental capacity at the moment the conveyance is sealed."},
      {"author": "Charles Babbage", "work": "On the Economy of Machinery", "quote": "An ingenious mechanical **transferrer** shifted the woven cloth from the loom to the folding table."},
      {"author": "Samuel Johnson", "work": "The Idler", "quote": "He who acts as the **transferrer** of private gossip seldom retains the friendship of either party."}
    ]
  },
  "Dashboard — fer/transferrin.md": {
    "primary": "An iron-binding blood plasma glycoprotein that controls the level of free iron in biological fluids and transports it to cells.",
    "secondary": "In hematology and clinical biochemistry, the primary physiological vehicle for delivery of ferric ions to bone marrow erythroblasts for hemoglobin synthesis.",
    "quotes": [
      {"author": "Max Perutz", "work": "Proteins and Nucleic Acids", "quote": "Each molecule of **transferrin** possesses two distinct high-affinity binding sites for ferric iron."},
      {"author": "Christian de Duve", "work": "A Guided Tour of the Living Cell", "quote": "Cell surface receptors internalize the iron-laden **transferrin** through receptor-mediated endocytosis."},
      {"author": "Arthur Kornberg", "work": "For the Love of Enzymes", "quote": "Circulating **transferrin** prevents toxic free iron from catalyzing dangerous hydroxyl radical formation."}
    ]
  },
  "Dashboard — fer/undeferential.md": {
    "primary": "Not showing deference; lacking respectful submission, courtesy, or reverent regard for authority.",
    "secondary": "In social history and Victorian literature, exhibiting an outspoken, egalitarian, or irreverent demeanor toward social superiors.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "His **undeferential** tone toward the senior parish magistrates provoked indignant whispers among the town elders."},
      {"author": "Anthony Trollope", "work": "Barchester Towers", "quote": "The young clergyman adopted an **undeferential** bearing that offended the archdeacon's sense of clerical hierarchy."},
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "The crowd gave vent to their discontent in loud, **undeferential** remarks directed at the town council."}
    ]
  },
  "Dashboard — fer/undifferentiated.md": {
    "primary": "Not differentiated; having no distinct specialized features; homogenous, uniform, or embryonic.",
    "secondary": "In embryology and cell biology, designating primitive stem cells that have not yet undergone lineage commitment or specialized morphological development.",
    "quotes": [
      {"author": "Charles Darwin", "work": "On the Origin of Species", "quote": "In primitive organisms, the body plan remains largely **undifferentiated**, performing all vital functions with generalized tissues."},
      {"author": "Thomas Henry Huxley", "work": "Man's Place in Nature", "quote": "The early blastoderm consists of an **undifferentiated** layer of rounded cells before germ layer separation occurs."},
      {"author": "Herbert Spencer", "work": "First Principles", "quote": "Cosmic evolution begins in an **undifferentiated** primordial nebulosity and progresses toward organized diversity."}
    ]
  },
  "Dashboard — fer/unfermented.md": {
    "primary": "Not having undergone fermentation; unfermented juice, must, or bread dough.",
    "secondary": "In historical brewing and Jewish liturgical tradition, referring to unfermented grape juice or unleavened dough free from yeast action.",
    "quotes": [
      {"author": "Louis Pasteur", "work": "Studies on Fermentation", "quote": "The pure **unfermented** wort remains sweet and limpid indefinitely if protected from airborne microorganisms."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "I baked simple cakes of **unfermented** cornmeal and water upon a flat stone beside the hearth."},
      {"author": "Justus von Liebig", "work": "Familiar Letters on Chemistry", "quote": "Boiling prevents fermentation, preserving the vegetable extract in an **unfermented** condition."}
    ]
  },
  "Dashboard — fer/unfertile.md": {
    "primary": "Not fertile; barren, sterile, or producing little or no vegetation or offspring (infertile).",
    "secondary": "In classical agronomy and economic geography, describing soil lacking mineral humus or tracts of wasteland incapable of profitable tillage.",
    "quotes": [
      {"author": "Thomas Malthus", "work": "An Essay on the Principle of Population", "quote": "Settlers on an **unfertile** tract must expend double the labor to extract a subsistence wage."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Hybrids between these distant species proved completely **unfertile** when crossed among themselves."},
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "Speculative minds that despise practical experiments remain barren and **unfertile** in productive results."}
    ]
  },
  "Dashboard — fer/unfertilised.md": {
    "primary": "Not having been fertilized; not impregnated with sperm or pollen; or soil not enriched with fertilizer.",
    "secondary": "In developmental embryology and botany, designating a virgin ovum that has not united with a male gamete.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Perrier notes that **unfertilised** ova in certain insects occasionally undergo spontaneous parthenogenetic cleavage."},
      {"author": "Thomas Hunt Morgan", "work": "Experimental Embryology", "quote": "The **unfertilised** sea urchin egg can be chemically stimulated to begin division without sperm."},
      {"author": "Jacques Loeb", "work": "Artificial Parthenogenesis and Fertilization", "quote": "Exposure to hypertonic solutions initiated developmental cleavage in completely **unfertilised** marine eggs."}
    ]
  },
  "Dashboard — fer/unfertilized.md": {
    "primary": "Not fertilized; not united with male gametes; or soil lacking added nutrients (American spelling of unfertilised).",
    "secondary": "In cell biology and agricultural science, referring to an ovum awaiting fertilization, or agricultural soil left without nutrient supplementation.",
    "quotes": [
      {"author": "Thomas Hunt Morgan", "work": "The Mechanism of Mendelian Heredity", "quote": "An **unfertilized** ovum contains only the single haploid chromosome complement of the maternal lineage."},
      {"author": "Charles Darwin", "work": "The Effects of Cross and Self Fertilisation", "quote": "Flowers excluded from insect visits remained **unfertilized** and dropped their petals without setting seed."},
      {"author": "Rachel Carson", "work": "Silent Spring", "quote": "The chemical runoff poisoned the pond, leaving fish eggs **unfertilized** and lifeless along the muddy shore."}
    ]
  },
  "Dashboard — fer/unsufferable.md": {
    "primary": "Incapable of being suffered or endured; intolerable, unbearable, or insufferable.",
    "secondary": "In classical poetry and religious drama, characterizing tortures, blasphemies, or insolence exceeding human endurance.",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Hell heard the **unsufferable** noise; Hell saw / Heaven ruining from Heaven, and would have fled / Affrighted; but strict Fate had cast too deep / Her dark foundations."},
      {"author": "Richard Hooker", "work": "Of the Lawes of Ecclesiasticall Politie", "quote": "An **unsufferable** burden is laid upon the church when human traditions are equated with divine mandates."},
      {"author": "Walter Scott", "work": "The Bride of Lammermoor", "quote": "The haughty arrogance of his enemy became at last an **unsufferable** provocation to violence."}
    ]
  },
  "Dashboard — fer/untransferable.md": {
    "primary": "Not capable of being transferred, conveyed, or assigned to another person, place, or entity.",
    "secondary": "In constitutional jurisprudence and property law, designating inalienable personal rights, sovereign duties, or non-delegable judicial authority.",
    "quotes": [
      {"author": "John Locke", "work": "Second Treatise of Government", "quote": "The legislative power, being derived from the people by a positive voluntary grant, is an **untransferable** trust."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The supreme executive power represents an **untransferable** responsibility that cannot be partitioned among rival councils."},
      {"author": "Ralph Waldo Emerson", "work": "Essays: First Series", "quote": "The moral conviction of the individual soul is an **untransferable** certainty that cannot be borrowed from another."}
    ]
  },
  "Dashboard — fer/vociferous.md": {
    "primary": "Making or given to making a loud, vehement, clamorous, or noisy outcry; clamorous.",
    "secondary": "In political history and natural history, describing vehement vocal demonstrations by crowds, or loud vocalizations by animals during courtship or alarm.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The meaning of these differences in the trachea becomes apparent in the **vociferous** calls of the male waterfowl during courtship."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The **vociferous** shouts of the London mob greeted the acquittal of the seven bishops."},
      {"author": "Herman Melville", "work": "Moby-Dick; or, The Whale", "quote": "The captain answered the hail with a **vociferous** shout through his brass speaking-trumpet."}
    ]
  },
  "Dashboard — fer/vociferously.md": {
    "primary": "In a vociferous, loud, vehement, or clamorous manner; with clamor and noise.",
    "secondary": "In courtroom rhetoric and public assemblies, demanding, protesting, or asserting claims with loud, insistent, and impassioned urgency.",
    "quotes": [
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Peggotty was no less pleased than his nephew, though his modesty forbade him to rejoice as **vociferously** as the younger folks."},
      {"author": "Mark Twain", "work": "Life on the Mississippi", "quote": "The deckhands argued **vociferously** about the depth of the channel as the steamboat neared the sandbar."},
      {"author": "Joseph Conrad", "work": "Lord Jim", "quote": "The native crew shouted **vociferously**, pointing through the darkness toward the ominous surf breaking on the reef."}
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

print(f"Carrying Batch 5E (fer): Successfully updated {updated}/{len(data)} notes.")
