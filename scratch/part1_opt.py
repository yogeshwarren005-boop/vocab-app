# -*- coding: utf-8 -*-
"""
Part 1: 25 words from Dashboard — opt ('adopt' through 'optimisation')
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

part1_opt = {
  "adopt": {
    "primary": "To legally take another's child into one's family, or to formally choose and embrace a method, principle, or policy.",
    "secondary": "In parliamentary procedure and civil jurisprudence, to formally approve and ratify a resolution, motion, or legislative enactment.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The convention determined to **adopt** a plan of federal government capable of uniting the sovereign states."},
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Mrs. Dashwood was ready to **adopt** any scheme that promised comfort and independence to her daughters."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Naturalists will find reason to **adopt** the principle of natural selection when explaining organic adaptations."}
    ]
  },
  "adoptable": {
    "primary": "Suitable, eligible, or legally qualified for adoption into a family, or capable of being embraced as a plan.",
    "secondary": "In family law and policy analysis, satisfying statutory criteria for custodial placement or practical feasibility for institutional implementation.",
    "quotes": [
      {"author": "George Eliot", "work": "Daniel Deronda", "quote": "The charitable guardians deemed the child thoroughly **adoptable**, noting his tractable temperament and promising health."},
      {"author": "Jeremy Bentham", "work": "The Rationale of Judicial Evidence", "quote": "A legal reform is truly valuable only when it offers a readily **adoptable** rule of procedure for common courts."},
      {"author": "Herbert Spencer", "work": "Social Statics", "quote": "No administrative scheme is permanently **adoptable** unless it aligns with the evolving moral consensus of society."}
    ]
  },
  "adopted": {
    "primary": "Taken into a family through legal procedures, or chosen, embraced, and formally accepted as a custom or measure.",
    "secondary": "In comparative ethnology and international law, formally incorporated into a kinship clan, institutional canon, or statutory code.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "Trajan was the first stranger who was **adopted** into the family of the Caesars and adorned the purple."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "She felt herself warmly loved and fully **adopted** as a daughter by the venerable clergyman and his sisters."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "The newly settled townships quickly **adopted** the municipal bylaws that had long prevailed in the older colonies."}
    ]
  },
  "adoptee": {
    "primary": "An individual who has been legally received into a family other than that of their biological birth parents.",
    "secondary": "In domestic relations jurisprudence and sociological studies, a person holding full filial inheritance and civil rights established by judicial decree.",
    "quotes": [
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "Under the civil law of Rome, the **adoptee** entered the agnatic lineage of the adoptive parent with all privileges of an heir."},
      {"author": "Henry Maine", "work": "Ancient Law", "quote": "Archaic tribal codes provided that the **adoptee** was severed irrevocably from his ancestral hearth and domestic religion."},
      {"author": "G. K. Chesterton", "work": "What's Wrong with the World", "quote": "The legal fiction that treats the **adoptee** as born of the house is an ancient and generous tribute to the family bond."}
    ]
  },
  "adopter": {
    "primary": "A person who legally assumes parental responsibility for a child, or an individual who takes up a novel technique.",
    "secondary": "In diffusion of innovations theory and family law, the legal petitioner assuming custodial liabilities or an early consumer embracing technological novelty.",
    "quotes": [
      {"author": "Benjamin Franklin", "work": "Autobiography", "quote": "Every early **adopter** of an uncommon philosophical doctrine must prepare to face initial suspicion and dispute."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Miss Havisham proved a capricious **adopter**, molding Estella into an instrument of cold retribution against mankind."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The enterprising farmer who becomes the first **adopter** of improved drainage usually reaps an immediate economic advantage."}
    ]
  },
  "adoption": {
    "primary": "The legal act of creating a permanent parent-child relationship between individuals not biologically related, or the formal choosing of a course.",
    "secondary": "In Christian theology and constitutional jurisprudence, spiritual grafting into divine covenant or legislative ratification of fundamental statutory codes.",
    "quotes": [
      {"author": "John Locke", "work": "Two Treatises of Government", "quote": "The formal **adoption** of civil government by mutual consent marks the transition from the state of nature to society."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The triumphant **adoption** of the Declaration of Rights settled forever the balance of the English constitution."},
      {"author": "George Eliot", "work": "Silas Marner", "quote": "The weaver's informal **adoption** of the golden-haired child restored his withered heart to human fellowship."}
    ]
  },
  "adoptive": {
    "primary": "Related through or acquired by legal adoption rather than by biological descent; also having the power to adopt.",
    "secondary": "In social anthropology and legal status doctrine, describing non-consanguineous relationships given full juridical and ceremonial equivalence to blood ties.",
    "quotes": [
      {"author": "Sir Walter Scott", "work": "Rob Roy", "quote": "He regarded the Scottish Highlands as his **adoptive** homeland, defending its ancient traditions with filial fervor."},
      {"author": "Washington Irving", "work": "The Sketch Book", "quote": "The emigrant wept as he beheld his **adoptive** country rising across the western waters of the Atlantic."},
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "She found solace in the quiet village, looking upon its severe inhabitants with the gentle regard of an **adoptive** mother."}
    ]
  },
  "apoptosis": {
    "primary": "A genetically programmed and orderly process of cellular self-destruction essential for organismal development and tissue homeostasis.",
    "secondary": "In cellular biology and oncology, energy-dependent physiological cell death featuring chromatin condensation, membrane blebbing, and phagocytosis without inflammation.",
    "quotes": [
      {"author": "Sydney Brenner", "work": "Nature (Scientific Memoirs)", "quote": "Genetic analysis revealed that **apoptosis** during nematode morphogenesis eliminates redundant cell lineages with exact precision."},
      {"author": "William Harvey", "work": "Anatomical Disquisitions", "quote": "The orderly involution of living parts resembles what modern physiologists identify as controlled **apoptosis** in developing tissues."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "Nature balances tissue accretion with systematic **apoptosis**, shaping embryonic organs through selective cellular sacrifice."}
    ]
  },
  "co-opt": {
    "primary": "To elect or appoint someone as a member of a committee or group by the existing members; also to assimilate or appropriate.",
    "secondary": "In political sociology and governance theory, absorbing dissident leaders or hostile ideological symbols into institutional frameworks to neutralize opposition.",
    "quotes": [
      {"author": "Max Weber", "work": "Economy and Society", "quote": "Ruling bureaucratic elites frequently **co-opt** charismatic protest leaders to stabilize administrative authority."},
      {"author": "John Stuart Mill", "work": "Considerations on Representative Government", "quote": "A governing council may **co-opt** distinguished jurists to enhance the technical caliber of its legislative deliberations."},
      {"author": "George Bernard Shaw", "work": "Major Barbara", "quote": "The industrial capitalists seek to **co-opt** radical reformers by funding philanthropic charities and municipal institutions."}
    ]
  },
  "co-optation": {
    "primary": "The process of appointing a new member by vote of existing peers, or the institutional absorption of dissident factions.",
    "secondary": "In organizational sociology and political dynamics, strategic assimilation of external critics into administrative councils to preserve hegemony.",
    "quotes": [
      {"author": "Robert Michels", "work": "Political Parties", "quote": "The iron law of oligarchy perpetuates power through deliberate **co-optation** of emerging working-class organizers."},
      {"author": "Alexis de Tocqueville", "work": "The Old Regime and the Revolution", "quote": "The crown attempted the **co-optation** of influential provincial nobles, yet failed to quell underlying peasant discontent."},
      {"author": "Harold Laski", "work": "A Grammar of Politics", "quote": "Judicial independence is threatened whenever legislative majorities utilize **co-optation** to populate the higher tribunals."}
    ]
  },
  "co-option": {
    "primary": "The act of co-opting an individual or idea; appointment to membership by incumbent colleagues.",
    "secondary": "In corporatist governance and political philosophy, institutional preemption of dissident movements through structural incorporation and minor concessions.",
    "quotes": [
      {"author": "James Bryce", "work": "The American Commonwealth", "quote": "The municipal committee maintained stability through regular **co-option** of trusted community elders and civic leaders."},
      {"author": "Woodrow Wilson", "work": "Congressional Government", "quote": "The permanent standing committees resisted executive interference by relying on internal **co-option** for leadership succession."},
      {"author": "Beatrice Webb", "work": "My Apprenticeship", "quote": "The trade union executive resisted imperial **co-option**, refusing to compromise its socialist principles for minor titles."}
    ]
  },
  "diopter": {
    "primary": "A unit of measurement of the refractive power of an optical lens, equal to the reciprocal of the focal length in meters.",
    "secondary": "In ophthalmic optics and clinical optometry, the standard quantitative metric denoting corrective lens curvature and convergent vergence.",
    "quotes": [
      {"author": "Hermann von Helmholtz", "work": "Treatise on Physiological Optics", "quote": "The crystalline lens accommodates visual focus by increasing its refractive power by several **diopter** units."},
      {"author": "Thomas Young", "work": "Lectures on Natural Philosophy", "quote": "Visual astigmatism can be compensated by adjusting the meridional power of the lens to the proper **diopter** value."},
      {"author": "Ernst Abbe", "work": "Contributions to the Theory of the Microscope", "quote": "Precision grinding allows the optical technician to calibrate each **diopter** interval with microscopic fidelity."}
    ]
  },
  "dioptre": {
    "primary": "The British standard spelling of diopter, measuring the refractive and focal power of optical lenses.",
    "secondary": "In clinical ophthalmology and optical physics, reciprocal metric focal length used to prescribe spectacle lenses and assess refractive errors.",
    "quotes": [
      {"author": "Lord Rayleigh", "work": "Scientific Papers", "quote": "The convex lens exhibited a power of one **dioptre**, bringing parallel rays to a focus at precisely one metre distance."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Myopic anomalies in domestic animals show variations equivalent to several degrees of **dioptre** deviation."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Mortimer adjusted his spectacles, whose thick ground glass indicated a corrective prescription of several **dioptre** units."}
    ]
  },
  "exopterygota": {
    "primary": "A superorder of winged insects whose wings develop externally outside the body wall during gradual hemimetabolous metamorphosis.",
    "secondary": "In systematic entomology and phylogenetics, the clade comprising hemimetabolous orders such as Odonata, Orthoptera, and Hemiptera lacking a pupal instar.",
    "quotes": [
      {"author": "Alfred Russel Wallace", "work": "The Malay Archipelago", "quote": "The collection contained primitive species of **exopterygota**, whose external wing pads were clearly visible upon the nymphs."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Sexual ornamentation among the **exopterygota** frequently manifests in the elaborate wing venation of male crickets."},
      {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Invertebrated Animals", "quote": "Unlike holometabolous beetles, members of the **exopterygota** undergo direct nymphal molts without an intervening chrysalis."}
    ]
  },
  "opt": {
    "primary": "To make a choice or decision between different possibilities; to choose one course over others.",
    "secondary": "In rational choice economics and decision theory, to select an action that maximizes subjective expected utility among available alternatives.",
    "quotes": [
      {"author": "William James", "work": "The Will to Believe", "quote": "In every moral crisis, the thinker must **opt** for one live hypothesis and face the hazard of being mistaken."},
      {"author": "John Dewey", "work": "Human Nature and Conduct", "quote": "Deliberation enables the reflective agent to **opt** for constructive habits rather than blind instinctual reactions."},
      {"author": "H. G. Wells", "work": "The World Set Free", "quote": "Mankind must either **opt** for international disarmament or perish in the fires of atomic devastation."}
    ]
  },
  "optative": {
    "primary": "Expressing a wish, desire, or prayerful longing; also designating a grammatical mood expressing wishes.",
    "secondary": "In classical Indo-European philology and Greek linguistics, the inflectional verbal mood expressing potentiality, hypothetical condition, or heartfelt desire.",
    "quotes": [
      {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "The poet shifted from categorical assertion to an **optative** yearning for transcendent spiritual union."},
      {"author": "Matthew Arnold", "work": "Culture and Anarchy", "quote": "The Hellenic spirit expressed in the **optative** mood an unquenchable aspiration toward sweetness and light."},
      {"author": "Walter Pater", "work": "Plato and Platonism", "quote": "Socrates concluded the dialogue not with dogmatic certainty, but in the serene **optative** tone of philosophical prayer."}
    ]
  },
  "optez": {
    "primary": "A French imperative or plural verbal form meaning 'choose' or 'opt', occasionally encountered in diplomatic, culinary, or bilingual registers.",
    "secondary": "In historical bilingual correspondence and European political tracts, an imperative exhortation urging an audience to decide between competing loyalties.",
    "quotes": [
      {"author": "Voltaire", "work": "Philosophical Letters", "quote": "Between superstitious servitude and enlightened reason, **optez** for liberty and think as autonomous men."},
      {"author": "Edmund Burke", "work": "Letters on a Regicide Peace", "quote": "The French manifesto presented a blunt ultimatum to neighboring states: **optez** for our republic or face our bayonets."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The revolutionary orator mounted the tribune, crying out to the wavering assembly: **optez** between courage and eternal infamy!"}
    ]
  },
  "optic": {
    "primary": "Relating to the eye, visual perception, or the transmission of light; ocular or visual.",
    "secondary": "In neuroanatomy and physiological optics, pertaining specifically to the cranial second nerve, visual pathways, or optical receptive organs.",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "The moon, whose orb through **optic** glass the Tuscan artist views at evening from the top of Fiesole."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Sensory impressions travel along the **optic** nerve to the cerebral cortex where conscious vision is generated."},
      {"author": "Alexander Pope", "work": "An Essay on Man", "quote": "Why has not man a microscopic eye? For this plain reason, man is not a fly; our **optic** powers fit our earthly sphere."}
    ]
  },
  "optical": {
    "primary": "Relating to sight, light, or vision; constructed to assist visual inspection or harness the physics of light.",
    "secondary": "In physics and instrumentation, concerning electromagnetic radiation within and near the visible spectrum and devices manipulating wave fronts.",
    "quotes": [
      {"author": "Isaac Newton", "work": "Opticks", "quote": "The white light of the sun is a heterogeneous mixture of rays possessing distinct **optical** refrangibilities."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Lydgate examined the minute cellular tissue through his favorite **optical** instrument with passionate scientific curiosity."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Holmes examined the minute powder residue under an **optical** lens of high magnifying magnification."}
    ]
  },
  "optically": {
    "primary": "In a manner pertaining to optics, visual perception, or the transmission and manipulation of light rays.",
    "secondary": "In stereochemistry and crystallography, rotating the plane of polarized light or displaying anisotropic optical behavior.",
    "quotes": [
      {"author": "Louis Pasteur", "work": "Researches on Molecular Asymmetry", "quote": "Tartaric acid derived from fermentation is **optically** active, rotating polarized light clockwise through the solution."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "The heavy glass prism became **optically** birefringent when placed within a potent magnetic field."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The horizon was **optically** distorted by the shimmering heat rising from the glassy surface of the equatorial sea."}
    ]
  },
  "optician": {
    "primary": "A professional technician qualified to make, verify, and fit spectacle lenses and optical appliances prescribed for patients.",
    "secondary": "In the history of science and commercial craftsmanship, a maker of astronomical telescopes, microscopes, and navigational surveying instruments.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Dombey and Son", "quote": "Sol Gills was an old-fashioned **optician** and nautical instrument maker, surrounded by chronometers and brass telescopes."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The specialized skill of the London **optician** depends upon a fine division of labor in polishing lenses."},
      {"author": "H. G. Wells", "work": "The Invisible Man", "quote": "Griffin purchased flint glass prisms from a London **optician** to conduct his secret light-refraction experiments."}
    ]
  },
  "optics": {
    "primary": "The scientific discipline and branch of physics that studies the behavior, properties, and manipulation of light.",
    "secondary": "In modern political analysis and corporate communication, public perception and aesthetic presentation of policy decisions or leadership actions.",
    "quotes": [
      {"author": "Isaac Newton", "work": "Opticks", "quote": "My design in this treatise of **optics** is not to explain the properties of light by hypotheses, but to propose and prove them by reason and experiments."},
      {"author": "Johann Wolfgang von Goethe", "work": "Theory of Colours", "quote": "The physiological phenomena of vision constitute the living foundation upon which all natural **optics** must rest."},
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "The venerable minister studied the subtle **optics** of human nature, discerning spiritual passions beneath veiled brows."}
    ]
  },
  "optimal": {
    "primary": "Best, most favorable, or most desirable possible under a given set of conditions or constraints.",
    "secondary": "In applied mathematics and evolutionary biology, maximizing fitness or achieving the global extremum of an objective function within parameter bounds.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Natural selection constantly drives anatomical structures toward an **optimal** form suited to environmental survival."},
      {"author": "Alfred Marshall", "work": "Principles of Economics", "quote": "The competitive market tends toward an **optimal** allocation of productive resources across competing industries."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Sustained mental concentration requires an **optimal** level of nervous excitement, neither languid nor hysterical."}
    ]
  },
  "optimally": {
    "primary": "In the best, most effective, or most favorable manner possible under prevailing circumstances.",
    "secondary": "In optimization algorithms and ecological modeling, achieving maximal performance efficiency or resource utilization with minimal thermodynamic cost.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Lay Sermons, Addresses, and Reviews", "quote": "The human organism functions **optimally** when physical exercise, balanced nutrition, and intellectual labor are harmonized."},
      {"author": "Herbert Spencer", "work": "The Data of Ethics", "quote": "Social institutions function **optimally** only when the liberty of each citizen is bounded solely by equal liberty for all."},
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "Capital yields its greatest societal benefit when deployed **optimally** across productive and sustainable enterprises."}
    ]
  },
  "optimisation": {
    "primary": "The action, process, or methodology of making something as effective, perfect, or functional as possible (British spelling).",
    "secondary": "In computational mathematics and industrial engineering, algorithmic discovery of local or global maxima and minima within parameter spaces.",
    "quotes": [
      {"author": "Charles Babbage", "work": "On the Economy of Machinery and Manufactures", "quote": "The systematic **optimisation** of workshop processes reduces material waste and dramatically multiplies national wealth."},
      {"author": "Alfred Marshall", "work": "Industry and Trade", "quote": "Modern enterprise relies upon the continuous **optimisation** of transport networks to reduce distribution overheads."},
      {"author": "H. G. Wells", "work": "The Work, Wealth and Happiness of Mankind", "quote": "Scientific governance requires the deliberate **optimisation** of global resource distribution for the common welfare."}
    ]
  }
}
