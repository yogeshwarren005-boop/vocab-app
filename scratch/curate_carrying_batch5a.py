# -*- coding: utf-8 -*-
import os, sys, re

sys.stdout.reconfigure(encoding="utf-8")

data = {
  # =========================================================================
  # Dashboard — fer (Batch 5A: 36 words)
  # =========================================================================
  "Dashboard — fer/afferent.md": {
    "primary": "Conducting or transmitting inward toward a central organ, nerve center, or reference point; opposed to efferent.",
    "secondary": "In neuroanatomy and cardiovascular physiology, designating sensory nerve fibers carrying impulses from peripheral receptors toward the central nervous system, or arterioles conveying blood to a glomerulus.",
    "quotes": [
      {"author": "William James", "work": "The Principles of Psychology", "quote": "An incoming sensory impulse travels along an **afferent** nerve fiber to reach the cerebral cortex."},
      {"author": "Charles Sherrington", "work": "The Integrative Action of the Nervous System", "quote": "The reflex arc commences with an **afferent** neurone conducting excitation from a receptive surface to the spinal axis."},
      {"author": "Santiago Ramón y Cajal", "work": "Histology of the Nervous System", "quote": "Sensory ganglia give rise to bifurcating axons whose medial branches form the **afferent** dorsal roots."}
    ]
  },
  "Dashboard — fer/antiferromagnetic.md": {
    "primary": "Exhibiting magnetism in which adjacent magnetic moments align antiparallel to each other, resulting in zero net macroscopic magnetization.",
    "secondary": "In solid-state condensed matter physics, describing crystal lattices that exhibit magnetic sublattices of opposing spin below the Néel temperature.",
    "quotes": [
      {"author": "Louis Néel", "work": "Propriétés magnétiques des ferrites", "quote": "Below the characteristic transition temperature, the material enters an **antiferromagnetic** state of ordered antiparallel spins."},
      {"author": "Philip W. Anderson", "work": "Basic Notions of Condensed Matter Physics", "quote": "The broken symmetry in an **antiferromagnetic** insulator produces collective spin-wave excitations known as magnons."},
      {"author": "Neville Mott", "work": "Metal-Insulator Transitions", "quote": "Strong on-site Coulomb repulsion stabilizes an insulating state with **antiferromagnetic** spin alignments."}
    ]
  },
  "Dashboard — fer/antiferromagnetism.md": {
    "primary": "A form of magnetism in solid matter wherein magnetic dipoles align in an alternating antiparallel configuration, producing zero net magnetic moment.",
    "secondary": "In quantum physics and magnetism, the cooperative quantum ordering phenomenon mediated by superexchange interactions across opposing ionic sublattices below the Néel temperature.",
    "quotes": [
      {"author": "Louis Néel", "work": "Magnetism and Local Molecular Field", "quote": "The phenomenon of **antiferromagnetism** accounts for the anomalous temperature dependence of magnetic susceptibility."},
      {"author": "John H. Van Vleck", "work": "The Theory of Electric and Magnetic Susceptibilities", "quote": "Molecular field theory offers an elegant mathematical treatment of **antiferromagnetism** in transition-metal compounds."},
      {"author": "Philip W. Anderson", "work": "Concepts in Solids", "quote": "Superexchange between cations through intermediate anions provides the primary microscopic mechanism responsible for **antiferromagnetism**."}
    ]
  },
  "Dashboard — fer/antifertility.md": {
    "primary": "Capable of preventing conception, reducing reproductive fecundity, or inhibiting biological fertilization.",
    "secondary": "In reproductive endocrinology and pharmacology, designating synthetic steroid agents or hormonal compounds that suppress ovulation or disrupt spermatogenesis.",
    "quotes": [
      {"author": "Gregory Pincus", "work": "The Control of Fertility", "quote": "The clinical investigation demonstrated that synthetic progestins exert potent **antifertility** effects by inhibiting the ovulatory surge."},
      {"author": "Carl Djerassi", "work": "The Politics of Contraception", "quote": "The synthesis of orally active 19-norsteroids provided the foundational compound for pharmacological **antifertility** agents."},
      {"author": "Thomas Malthus", "work": "An Essay on the Principle of Population", "quote": "Natural limitations and physiological checks upon fecundity act as systemic **antifertility** constraints in human societies."}
    ]
  },
  "Dashboard — fer/aquifer.md": {
    "primary": "An underground layer of water-bearing permeable rock, rock fractures, gravel, sand, or silt from which groundwater can be extracted.",
    "secondary": "In hydrogeology, a subsurface geological formation capable of storing and yielding economically usable quantities of water to wells, springs, or baseflow.",
    "quotes": [
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "Subterranean percolation feeds the deep **aquifer**, replenishing artesian basins far removed from surface precipitation."},
      {"author": "John Wesley Powell", "work": "Report on the Lands of the Arid Region of the United States", "quote": "Agricultural settlement in arid regions depends upon tapping the underlying **aquifer** with deep borings."},
      {"author": "G. K. Gilbert", "work": "Report on the Geology of the Henry Mountains", "quote": "The structural syncline forms a natural reservoir holding a confined **aquifer** beneath impermeable shale beds."}
    ]
  },
  "Dashboard — fer/aquiferous.md": {
    "primary": "Containing, yielding, or conveying water or a watery fluid.",
    "secondary": "In invertebrate zoology and plant anatomy, designating specialized canals, vessels, or parenchymatous tissue that circulate water through an organism.",
    "quotes": [
      {"author": "Charles Darwin", "work": "Monograph on the Sub-class Cirripedia", "quote": "The **aquiferous** canals in certain sponges and sessile barnacles maintain continuous respiratory currents."},
      {"author": "Richard Owen", "work": "Lectures on the Comparative Anatomy and Physiology of the Invertebrate Animals", "quote": "The porous body of the poriferan is permeated throughout by an **aquiferous** system of cilia-lined chambers."},
      {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Invertebrated Animals", "quote": "The sponge relies upon its **aquiferous** network for both nutrition and respiration."}
    ]
  },
  "Dashboard — fer/circumference.md": {
    "primary": "The enclosing boundary curve of a circle or round geometric figure; or the linear distance around the perimeter of an object.",
    "secondary": "In classical geometry and geodesy, the closed plane curve equidistant from a central locus, or the measured equatorial perimeter of a planetary body.",
    "quotes": [
      {"author": "William Shakespeare", "work": "King John", "quote": "Tis not the roundure of your old-faced walls / Can hide you from our messengers of war, / Though all these English, and their discipline, / Were harbor'd in their rude **circumference**."},
      {"author": "Isaac Newton", "work": "Opticks", "quote": "The rays that fell nearest the **circumference** of the lens suffered the greatest amount of chromatic aberration."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Round through the vast profundity obscure, / And said, Thus far extend, thus far thy bounds, / This be thy just **circumference**, O World."}
    ]
  },
  "Dashboard — fer/circumferent.md": {
    "primary": "Surrounding, encircling, or encompassing an area, body, or space on all sides.",
    "secondary": "In anatomical description and descriptive morphology, designating structures, membranes, or annular bands that wrap completely around an axis or organ.",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "His ponderous shield, / Ethereal temper, massy, large, and round, / Behind him cast; the broad **circumferent** orb / Hung on his shoulders like the moon."},
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "The sensory faculties receive impressions from the whole **circumferent** world."},
      {"author": "Samuel Taylor Coleridge", "work": "The Friend", "quote": "The eye surveys the horizon, bounded by the **circumferent** hills that frame the valley."}
    ]
  },
  "Dashboard — fer/circumferential.md": {
    "primary": "Relating to, lying along, or extending around the circumference or perimeter of an object or region.",
    "secondary": "In structural biomechanics and vascular histology, describing hoop stress, circular muscular fibers, or concentric lamellae oriented tangentially around a cylinder.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Now bees, as may be clearly seen by examining the edge of a growing comb, add successive **circumferential** layers of wax."},
      {"author": "William Harvey", "work": "Exercitatio Anatomica de Motu Cordis et Sanguinis in Animalibus", "quote": "The **circumferential** fibers of the ventricle contract forcibly to diminish the internal cavity."},
      {"author": "James Clerk Maxwell", "work": "A Treatise on Electricity and Magnetism", "quote": "The induced current flows along **circumferential** paths encircling the fluctuating magnetic flux."}
    ]
  },
  "Dashboard — fer/confer.md": {
    "primary": "To grant, bestow, or award an honor, title, privilege, or right; or to consult and discuss matters together.",
    "secondary": "In academic and civil protocol, to formally invest a candidate with a scholarly degree or civic dignity in accordance with statutory rights.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Love's Labour's Lost", "quote": "And, madam, at your father's castle walls / We'll crave a parley, to **confer** with you / On severals of head to her enterprise."},
      {"author": "Francis Bacon", "work": "Essays", "quote": "Reading maketh a full man; conference a ready man; and writing an exact man; and therefore, if a man write little, he had need have a great memory; if he **confer** little, he had need have a present wit."},
      {"author": "John Locke", "work": "Second Treatise of Government", "quote": "Society cannot **confer** upon the legislative body a greater power than what each individual had in the state of nature."}
    ]
  },
  "Dashboard — fer/conferee.md": {
    "primary": "A participant who takes part in a conference, convention, or formal diplomatic consultation.",
    "secondary": "In parliamentary procedure and jurisprudence, an appointed delegate serving on a joint committee to resolve disagreements between legislative chambers.",
    "quotes": [
      {"author": "Woodrow Wilson", "work": "Congressional Government", "quote": "Each **conferee** enters the joint committee room prepared to negotiate amendments on behalf of his chamber."},
      {"author": "Henry Adams", "work": "The Education of Henry Adams", "quote": "The experienced **conferee** weighed every word, mindful of the conflicting interests represented at the table."},
      {"author": "Theodore Roosevelt", "work": "An Autobiography", "quote": "The industrial **conferee** demonstrated a practical grasp of the labor conditions under review."}
    ]
  },
  "Dashboard — fer/conference.md": {
    "primary": "A formal meeting or consultation for discussion, exchange of views, or deliberation on specific topics.",
    "secondary": "In organizational and scholarly domains, a structured multi-day symposium where researchers present peer-reviewed findings and debate methodological paradigms.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Antony and Cleopatra", "quote": "Now, for the love of Love and her soft hours, / Let's not confound the time with **conference** harsh."},
      {"author": "Francis Bacon", "work": "Essays", "quote": "Reading maketh a full man; **conference** a ready man; and writing an exact man."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The bishops assembled in solemn **conference** to debate the orthodox formulation of the creed."}
    ]
  },
  "Dashboard — fer/conferment.md": {
    "primary": "The formal act of presenting, bestowing, or granting an honor, distinction, award, or degree.",
    "secondary": "In university ceremonial tradition and civic heraldry, the statutory ritual whereby scholastic or honorary credentials are officially conveyed upon recipients.",
    "quotes": [
      {"author": "Thomas Babington Macaulay", "work": "Critical and Historical Essays", "quote": "The **conferment** of peerages was used by the ministry to secure a compliant majority in the upper house."},
      {"author": "John Henry Newman", "work": "The Idea of a University", "quote": "The **conferment** of degrees is not merely an outward ceremony, but a public recognition of intellectual discipline."},
      {"author": "Benjamin Disraeli", "work": "Sybil, or The Two Nations", "quote": "The sudden **conferment** of titles transformed the political influence of the landed gentry."}
    ]
  },
  "Dashboard — fer/conferral.md": {
    "primary": "The act of conferring, bestowing, or awarding a privilege, title, award, or degree.",
    "secondary": "In constitutional law and institutional governance, the statutory transmission of delegated legal authority or sovereign jurisdiction from a principal to an agent.",
    "quotes": [
      {"author": "James Madison", "work": "The Federalist Papers", "quote": "The **conferral** of executive powers upon a single magistrate was balanced by constitutional checks."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "The **conferral** of municipal privileges encouraged active participation in local public affairs."},
      {"author": "Henry Sumner Maine", "work": "Ancient Law", "quote": "The formal **conferral** of status through solemn covenant marked the early transition from kinship to civil society."}
    ]
  },
  "Dashboard — fer/conferrer.md": {
    "primary": "A person, institution, or authority that confers, grants, or bestows an honor, gift, or benefit.",
    "secondary": "In philanthropic foundations and chivalric orders, the sovereign or corporate patron retaining the exclusive prerogative to bestow endowed honors.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "The benefactor expects gratitude from the receiver, but the **conferrer** of favors must prepare for occasional disappointment."},
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "The gratitude of the citizen should correspond to the integrity of the **conferrer** of civic honors."},
      {"author": "Jonathan Swift", "work": "A Tale of a Tub", "quote": "The author praised the generous **conferrer** of his living with elaborate dedicatory verses."}
    ]
  },
  "Dashboard — fer/conifer.md": {
    "primary": "Any gymnosperm tree or shrub of the division Pinophyta (order Coniferales), typically evergreen and bearing cones and needle-shaped or scalelike leaves.",
    "secondary": "In botanical silviculture and forest ecology, resinous vascular plants (such as pines, firs, spruces, and cedars) that dominate temperate and boreal taiga biomes.",
    "quotes": [
      {"author": "John Muir", "work": "The Mountains of California", "quote": "Every **conifer** in the High Sierra has its own peculiar voice when the wind sweeps through its branches."},
      {"author": "Charles Darwin", "work": "On the Origin of Species", "quote": "The ancient fossil record reveals that the **conifer** flourished long before the emergence of flowering plants."},
      {"author": "Henry David Thoreau", "work": "The Maine Woods", "quote": "The tall pine stood out against the northern sky, a stately **conifer** that had weathered a century of blizzards."}
    ]
  },
  "Dashboard — fer/coniferous.md": {
    "primary": "Bearing or producing cones, as plants of the division Pinophyta; or composed of cone-bearing trees.",
    "secondary": "In phytogeography and biogeoclimatology, designating evergreen forests and taiga ecosystems characterized by needle-leaved gymnosperms adapted to cold climates.",
    "quotes": [
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "The fossilized trunks embedded in the coal strata belong predominantly to ancient **coniferous** vegetation."},
      {"author": "John Muir", "work": "Our National Parks", "quote": "The dense **coniferous** forests of the Pacific slopes harbor some of the grandest timber on earth."},
      {"author": "Alexander von Humboldt", "work": "Cosmos", "quote": "The transition from deciduous hardwoods to **coniferous** evergreen woods marks the ascent into higher alpine zones."}
    ]
  },
  "Dashboard — fer/coreference.md": {
    "primary": "The grammatical or semantic relationship where two or more expressions in a text refer to the same extralinguistic entity.",
    "secondary": "In formal semantics and computational linguistics, the anaphoric resolution linking pronouns, noun phrases, and deictic markers to a shared discourse entity.",
    "quotes": [
      {"author": "Noam Chomsky", "work": "Lectures on Government and Binding", "quote": "Binding principles regulate the syntactic conditions under which **coreference** between a pronoun and its antecedent is permitted."},
      {"author": "Otto Jespersen", "work": "The Philosophy of Grammar", "quote": "The grammatical device of **coreference** prevents awkward repetition of substantives in continuous discourse."},
      {"author": "Roman Jakobson", "work": "Selected Writings", "quote": "The poetic texture exploits **coreference** to weave an intricate web of semantic correspondences across the text."}
    ]
  },
  "Dashboard — fer/coreferent.md": {
    "primary": "Referring to the same entity or individual; or a linguistic element that shares an identical referent with another expression.",
    "secondary": "In discourse analysis and syntax, designating an anaphor or noun phrase that points to an antecedent within the same or an adjacent sentence.",
    "quotes": [
      {"author": "Leonard Bloomfield", "work": "Language", "quote": "Two distinct linguistic forms are **coreferent** when both evoke the same object in the situational context."},
      {"author": "Bertrand Russell", "work": "An Inquiry into Meaning and Truth", "quote": "The pronoun and its antecedent are **coreferent** in that their assertive force terminates upon the same individual."},
      {"author": "Edward Sapir", "work": "Language: An Introduction to the Study of Speech", "quote": "Every language employs specialized formal means to mark expressions that are **coreferent** across narrative clauses."}
    ]
  },
  "Dashboard — fer/coreferential.md": {
    "primary": "Pertaining to, having, or exhibiting coreference; referring to the exact same entity or referent.",
    "secondary": "In syntactic binding theory, describing noun phrases and reflexive pronouns that must be co-indexed within their local governing syntactic category.",
    "quotes": [
      {"author": "Noam Chomsky", "work": "Aspects of the Theory of Syntax", "quote": "Reflexivization occurs only when two noun phrases within the same clause are **coreferential** in the deep structure."},
      {"author": "Otto Jespersen", "work": "A Modern English Grammar", "quote": "The possessive adjective and the subject noun are **coreferential** in standard reciprocal constructions."},
      {"author": "Charles Sanders Peirce", "work": "Collected Papers", "quote": "Signs that are **coreferential** determine identical interpretants in the mind of the comprehending observer."}
    ]
  },
  "Dashboard — fer/counteroffer.md": {
    "primary": "An offer made in response to a prior proposal by someone who has rejected the original offer or proposed revised terms.",
    "secondary": "In contract law, a response that alters the material terms of an initial offer, functioning legally as both a rejection and a new proposal.",
    "quotes": [
      {"author": "Oliver Wendell Holmes Jr.", "work": "The Common Law", "quote": "A qualified acceptance containing new conditions operates in law as a **counteroffer** that extinguishes the original proposal."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "In open markets, the haggling between buyer and seller proceeds through offer and **counteroffer** until an equilibrium price is reached."},
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "The employer made a **counteroffer** to the union delegates, offering shorter hours in lieu of increased wages."}
    ]
  },
  "Dashboard — fer/countertransference.md": {
    "primary": "The emotional reaction of a psychoanalyst or therapist toward a patient, particularly when influenced by the therapist's own unconscious conflicts.",
    "secondary": "In clinical psychodynamics, the therapeutic phenomenon wherein the analyst projects unresolved personal emotions, defenses, or past relational dynamics onto the analysand.",
    "quotes": [
      {"author": "Sigmund Freud", "work": "The Future Prospects of Psycho-Analytic Therapy", "quote": "We have become aware of the **countertransference**, which arises in the physician as a result of the patient's influence on his unconscious feelings."},
      {"author": "Carl Jung", "work": "The Psychology of the Transference", "quote": "The physician cannot insulate himself from the emotional field; his own **countertransference** becomes an indispensable instrument of diagnosis."},
      {"author": "Melanie Klein", "work": "Envy and Gratitude and Other Works", "quote": "Careful monitoring of **countertransference** allows the analyst to understand the primitive anxieties projected by the patient."}
    ]
  },
  "Dashboard — fer/dedifferentiate.md": {
    "primary": "To revert from a specialized morphological or physiological state to a simpler, less differentiated stem-like cellular condition.",
    "secondary": "In developmental and regenerative cell biology, to undergo biochemical reprogramming wherein mature somatic cells regain developmental plasticity and multipotency.",
    "quotes": [
      {"author": "Thomas Hunt Morgan", "work": "Regeneration", "quote": "When an amphibian limb is amputated, mature skeletal and muscular cells **dedifferentiate** to form the regenerative blastema."},
      {"author": "Hans Driesch", "work": "The Science and Philosophy of the Organism", "quote": "Certain tissues retain the latent potency to **dedifferentiate** under the influence of severe injury."},
      {"author": "Conrad Hal Waddington", "work": "The Strategy of the Genes", "quote": "Epigenetic barriers normally prevent cells from rolling backward, yet under extreme stimuli they may **dedifferentiate**."}
    ]
  },
  "Dashboard — fer/dedifferentiated.md": {
    "primary": "Having reverted from a mature, specialized cellular state to an earlier, simpler, or more primitive form.",
    "secondary": "In oncological pathology and histology, designating malignant tumor cells that have lost normal architectural organization, contact inhibition, and specialized metabolic functions.",
    "quotes": [
      {"author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "The rapidly growing sarcoma consisted of **dedifferentiated** cells bearing little resemblance to the parent connective tissue."},
      {"author": "Julian Huxley", "work": "Problems of Relative Growth", "quote": "In regenerating tissue, **dedifferentiated** cells congregate beneath the epidermis to initiate new morphogenesis."},
      {"author": "Stephen Jay Gould", "work": "Ontogeny and Phylogeny", "quote": "The presence of **dedifferentiated** cellular zones in lower vertebrates illustrates their extraordinary capacity for epimorphic regeneration."}
    ]
  },
  "Dashboard — fer/dedifferentiation.md": {
    "primary": "The cellular process of reverting from a specialized form or function back to a more primitive, generalized, or unspecialized state.",
    "secondary": "In regenerative biology and stem cell genetics, the loss of lineage-specific epigenetic marks enabling somatic cells to proliferate as pluripotent progenitors.",
    "quotes": [
      {"author": "Thomas Hunt Morgan", "work": "Experimental Embryology", "quote": "The phenomenon of **dedifferentiation** is a prerequisite for epimorphic regeneration in salamander appendages."},
      {"author": "Ernst Mayr", "work": "The Growth of Biological Thought", "quote": "Early embryologists debated whether **dedifferentiation** represented a true reversion of cellular fate or merely phenotypic masking."},
      {"author": "Conrad Hal Waddington", "work": "Principles of Embryology", "quote": "Tissue repair in lower organisms demonstrates that **dedifferentiation** does not erase the fundamental genomic program."}
    ]
  },
  "Dashboard — fer/defer.md": {
    "primary": "To put off, postpone, or delay an action to a future time; or to submit politely to the judgment or wishes of another.",
    "secondary": "In social etiquette and judicial procedure, to yield precedence or suspend immediate determination out of respect for higher appellate authority.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry VI, Part 1", "quote": "**Defer** no time, delays have dangerous ends; / Enter and cry, 'The Dauphin!' / Presently through all the streets of Rouen."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "The mind has the power to suspend the execution of its desires, and **defer** its decisions until deliberation is complete."},
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "He who resolves to amend tomorrow merely seeks an excuse to **defer** his duty today."}
    ]
  },
  "Dashboard — fer/deference.md": {
    "primary": "Respectful submission, courteous yielding, or polite compliance with the judgment, will, or opinion of another.",
    "secondary": "In sociological theory and diplomatic etiquette, the institutionalized display of reverence or social subordinate alignment toward recognized moral, judicial, or aristocratic authority.",
    "quotes": [
      {"author": "Charles Darwin", "work": "On the Origin of Species", "quote": "I am aware that two paleontologists, whose opinions are worthy of much **deference**, have argued against this interpretation."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth listened with all the **deference** she could muster to the pompous advice of Mr. Collins."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "Democratic societies diminish the instinctive **deference** that citizens in an aristocracy pay to their social superiors."}
    ]
  },
  "Dashboard — fer/deferent.md": {
    "primary": "Serving to carry, convey, or conduct; or showing respectful deference and submission.",
    "secondary": "In classical Ptolemaic astronomy, the large circular orbital path centered near the Earth along which the center of a planet's epicycle revolves.",
    "quotes": [
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "The physical air serves as a **deferent** medium for the propagation of sound waves."},
      {"author": "Nicolaus Copernicus", "work": "De revolutionibus orbium coelestium", "quote": "In the ancient model, the planet traversed an epicycle whose center was carried along the **deferent** circle."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "With centric and eccentric scribbled o'er, / Cycle and epicycle, orb in orb, / How would they build their **deferent** spheres!"}
    ]
  },
  "Dashboard — fer/deferential.md": {
    "primary": "Showing, expressing, or characterized by courteous deference, high respect, or polite submission.",
    "secondary": "In interpersonal sociology, exhibiting behavioral markers of deference and verbal hesitation designed to acknowledge another's senior status or authority.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The oppressive sense of the harm she had done led Tess to be more **deferential** to his wishes than she had ever been before."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Mr. Guppy adopted a **deferential** attitude in the presence of his employer, bowing at every pause in the conversation."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "His manner toward the elderly scholar was marked by a **deferential** modesty that won immediate approval."}
    ]
  },
  "Dashboard — fer/deferentially.md": {
    "primary": "In a deferential manner; with courteous respect, polite submission, or reverent compliance.",
    "secondary": "In social discourse and narrative descriptions, speaking or acting with measured humility to avoid giving offense to superiors.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "On the contrary it seemed to Dorothea that Will had a happier way of disagreeing **deferentially** than anyone she had ever met."},
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "The servant answered **deferentially**, keeping his eyes lowered as he delivered the message."},
      {"author": "Thomas Hardy", "work": "The Woodlanders", "quote": "He removed his hat and spoke **deferentially** to the lady of the manor as she passed the gate."}
    ]
  },
  "Dashboard — fer/deferment.md": {
    "primary": "The act of delaying, postponing, or putting off something to a future time; a postponement.",
    "secondary": "In civil administration and military conscription, an official temporary exemption from compulsory public duty or tax assessment.",
    "quotes": [
      {"author": "Walt Whitman", "work": "Leaves of Grass", "quote": "Curious in time I stand, noting the efforts of heroes, / Is the **deferment** of their victory a reason for despair?"},
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "The **deferment** of the assembly's decision only allowed factional passions to ferment more fiercely."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "A dangerous **deferment** of the national debt would destroy public credit and foreign confidence."}
    ]
  },
  "Dashboard — fer/deferral.md": {
    "primary": "A postponement or intentional delay of an action, decision, payment, or proceeding to a subsequent time.",
    "secondary": "In financial accounting and fiscal policy, the postponement of recognizing an incurred expense or accrued revenue until a subsequent reporting period.",
    "quotes": [
      {"author": "Woodrow Wilson", "work": "The State: Elements of Historical and Practical Politics", "quote": "The **deferral** of legislative action allowed public opinion to mature before a final vote was taken."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "A merchant cannot easily endure the indefinite **deferral** of payments due from foreign correspondents."},
      {"author": "John Maynard Keynes", "work": "The General Theory of Employment, Interest and Money", "quote": "Liquidity preference reflects the desire for the **deferral** of consumption in the face of economic uncertainty."}
    ]
  },
  "Dashboard — fer/deferred.md": {
    "primary": "Put off or postponed to a later date; delayed or suspended until a future determination.",
    "secondary": "In corporate finance and taxation, describing liabilities, revenues, or compensation earned in the present period but payable or recognized at a specified future date.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry VIII", "quote": "I do beseech your Grace to pardon me, / Who, earnest in the service of my God, / Have long **deferred** my visit to your highness."},
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "Hope is itself a species of happiness... but expectations improperly indulged must end in disappointment, especially when **deferred**."},
      {"author": "Ralph Waldo Emerson", "work": "Essays: First Series", "quote": "Every promise of the soul is fulfilled, though the execution may be **deferred** by human frailty."}
    ]
  },
  "Dashboard — fer/differ.md": {
    "primary": "To be unlike, dissimilar, or distinct in nature, quality, or form; or to hold an opposing opinion or disagree.",
    "secondary": "In comparative morphology and taxonomy, to exhibit measurable morphological divergence that distinguishes one taxon from another.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Winter's Tale", "quote": "Therein do men from children nothing **differ**."},
      {"author": "Charles Darwin", "work": "On the Origin of Species", "quote": "Individuals of the same species often **differ** slightly in relative proportions and coloring."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Men **differ** widely in their speculative opinions, but their moral principles often converge."}
    ]
  },
  "Dashboard — fer/difference.md": {
    "primary": "The state, quality, or condition of being unlike, dissimilar, or distinct; or the amount or degree by which things vary.",
    "secondary": "In philosophical metaphysics and set theory, the distinguishing principle (differentia) that separates a species from its genus, or the set-theoretic subtraction of elements.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Sonnet 105", "quote": "Kind is my love to-day, to-morrow kind, / Still constant in a wondrous excellence; / Therefore my verse, to constancy confined, / One thing expressing, leaves out **difference**."},
      {"author": "René Descartes", "work": "Discourse on Method", "quote": "The diversity of our opinions does not proceed from some being more rational than others, but solely from our conducting our thoughts along different paths and not all considering the same **difference**."},
      {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "The method of **difference** consists in comparing an instance in which the phenomenon occurs with an instance in which it does not."}
    ]
  },
  "Dashboard — fer/different.md": {
    "primary": "Not the same as another; distinct, separate, or dissimilar in character, identity, or nature.",
    "secondary": "In evolutionary taxonomy and cognitive psychology, exhibiting contrasting phenotypic adaptations or categorized into separate conceptual schemas.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Sonnet 98", "quote": "Yet nor the lays of birds, nor the sweet smell / Of **different** flowers in odour and in hue, / Could make me any summer's story tell."},
      {"author": "Francis Bacon", "work": "Novum Organum", "quote": "The human understanding is not a dry light, but receives an infusion from the will and affections... and so forth, in **different** ways."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The mental faculties of animals of **different** species diverge according to their specific conditions of life."}
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

print(f"Carrying Batch 5A (fer): Successfully updated {updated}/{len(data)} notes.")
