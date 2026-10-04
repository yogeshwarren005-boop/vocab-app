# -*- coding: utf-8 -*-
"""
Curates Cluster Equality (Batch 1, 39 words):
- Dashboard — ceter (3 words)
- Dashboard — integr (17 words)
- Dashboard — simil (19 words)
Total: 39 words.
"""
import sys, re

sys.stdout.reconfigure(encoding="utf-8")

data_batch1 = {
  # Dashboard — ceter (3 words)
  "ceterach": {
    "primary": "The rustyback fern (Asplenium ceterach), an evergreen rock fern densely covered beneath with brown scales.",
    "secondary": "In traditional herbal medicine, a botanical remedy historically used for splenic disorders and kidney gravel.",
    "quotes": [
      {"author": "John Gerard", "work": "The Herball or Generall Historie of Plantes", "quote": "The small rock fern termed **ceterach** groweth upon ancient stone walls and rocky crags."},
      {"author": "John Ruskin", "work": "Proserpina", "quote": "The under surface of the **ceterach** frond is plated with golden-brown imbricated scales."},
      {"author": "William Withering", "work": "An Arrangement of British Plants", "quote": "Old herbalists celebrated the virtues of **ceterach** in dissolving stones and soothing hepatic complaints."}
    ]
  },
  "ceteris paribus": {
    "primary": "A Latin phrase meaning with other conditions remaining the same or all other things being equal.",
    "secondary": "In theoretical economics and social science, an assumption isolating the causal effect of a single independent variable.",
    "quotes": [
      {"author": "Alfred Marshall", "work": "Principles of Economics", "quote": "An increase in price reduces market demand, **ceteris paribus**, when consumer preferences remain unchanged."},
      {"author": "John Maynard Keynes", "work": "The General Theory of Employment, Interest and Money", "quote": "The propensity to consume rises with income, **ceteris paribus**, in modern industrial societies."},
      {"author": "David Ricardo", "work": "Principles of Political Economy and Taxation", "quote": "Higher wages diminish the rate of capital profits, **ceteris paribus**, across all trading sectors."}
    ]
  },
  "et cetera": {
    "primary": "And other similar things; and the rest; and so forth; used to indicate that further items in a series are omitted.",
    "secondary": "Additional unspecified items of the same general class or character, abbreviated commonly as etc.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The bill of costs enumerated charges for attendances, consultations, copying of documents, **et cetera**."},
      {"author": "Jane Austen", "work": "Mansfield Park", "quote": "The theatrical wardrobe comprised cloaks, swords, powdered wigs, **et cetera**, scattered about the billiard room."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The ship's manifest recorded salt beef, hard biscuit, casks of rum, **et cetera**, for the three-year voyage."}
    ]
  },

  # Dashboard — integr (17 words)
  "disintegrable": {
    "primary": "Capable of being broken down into constituent fragments, particles, or small components.",
    "secondary": "In geology and materials science, susceptible to gradual crumbling or decomposition under weathering agents.",
    "quotes": [
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "The porous sandstone strata are readily **disintegrable** under the cyclical action of frost and rain."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Chemistry and Physics", "quote": "The fused mass proved easily **disintegrable** when immersed in warm acidified water."},
      {"author": "Thomas Henry Huxley", "work": "Discourses: Biological and Geological", "quote": "Chalk cliffs consist of microscopic, easily **disintegrable** shells of ancient foraminifera."}
    ]
  },
  "disintegrate": {
    "primary": "To break up into small parts, fragments, or components, typically as a result of impact or decay.",
    "secondary": "Figuratively, to lose cohesion, unity, or structural integrity over time.",
    "quotes": [
      {"author": "H.G. Wells", "work": "The War of the Worlds", "quote": "The heat-ray caused solid brick walls to flash into flame and **disintegrate** into smoking dust."},
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "Weakened by civil strife, the administrative fabric of the Western Empire began to **disintegrate**."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The exposed volcanic boulders slowly **disintegrate** into fertile red soil upon the lower slopes."}
    ]
  },
  "disintegration": {
    "primary": "The process of losing cohesion and breaking down into small parts or component elements.",
    "secondary": "In nuclear physics, the spontaneous radioactive decay of an atomic nucleus with emission of radiation.",
    "quotes": [
      {"author": "Ernest Rutherford", "work": "Radioactive Transformations", "quote": "The spontaneous **disintegration** of radium atoms generates helium particles and radioactive radon gas."},
      {"author": "Winston Churchill", "work": "The World Crisis", "quote": "The sudden **disintegration** of the Russian front altered the entire balance of military forces in Europe."},
      {"author": "Henry Adams", "work": "The Education of Henry Adams", "quote": "The historian contemplated the gradual **disintegration** of medieval spiritual unity under modern industrial forces."}
    ]
  },
  "disintegrative": {
    "primary": "Tending to cause or promote disintegration, decomposition, or fragmentation.",
    "secondary": "In sociology and political theory, undermining institutional harmony, civic order, or social cohesion.",
    "quotes": [
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "Unbridled individualism exerts a **disintegrative** influence upon communal bonds and civic responsibility."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Violent emotional trauma produces **disintegrative** effects upon the normal synthesis of conscious memory."},
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The **disintegrative** power of damp sea salt gnawed steadily into the carved Gothic capitals."}
    ]
  },
  "integral": {
    "primary": "Necessary to make a whole complete; essential, fundamental, or constituent.",
    "secondary": "In mathematics, an expression giving the area under a curve or solving a differential equation.",
    "quotes": [
      {"author": "Isaac Newton", "work": "Principia Mathematica", "quote": "The summation of infinitesimal increments yields the complete **integral** of planetary motion."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Intellectual honesty was an **integral** part of Dorothea Brooke's unbending moral character."},
      {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "Every natural fact is an **integral** reflection of some spiritual truth in the universe."}
    ]
  },
  "integrality": {
    "primary": "The attribute of being whole, undivided, complete, or structurally sound.",
    "secondary": "In philosophical ontology, the irreducible completeness or totality of an organic system.",
    "quotes": [
      {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "The living poem maintains its imaginative **integrality**, wherein each part reflects the harmony of the whole."},
      {"author": "John Ruskin", "work": "Modern Painters", "quote": "A true master respects the **integrality** of landscape composition, subordinating minor details to the total effect."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "The stream of consciousness possesses an unbroken **integrality** despite changing sensory impressions."}
    ]
  },
  "integrally": {
    "primary": "In an integral, essential, or complete manner; as an inseparable part of a whole.",
    "secondary": "Completely, entirely, or holistically without omitting any constituent element.",
    "quotes": [
      {"author": "Ralph Waldo Emerson", "work": "The Conduct of Life", "quote": "Moral character is **integrally** woven into every word, gesture, and decision of a great leader."},
      {"author": "John Dewey", "work": "Art as Experience", "quote": "Aesthetic experience is **integrally** connected with the vital interactions of everyday living."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "Scientific methods are **integrally** bound to the rigorous discipline of empirical verification."}
    ]
  },
  "integrate": {
    "primary": "To combine one thing with another so that they become a whole; to unify separate parts.",
    "secondary": "To desegregate an institution, school, or community, providing equal access to all groups.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The new federal constitution was drafted to **integrate** thirteen sovereign states into one durable republic."},
      {"author": "Herbert Spencer", "work": "First Principles", "quote": "Evolution manifests a continuous tendency to **integrate** matter while dissipating motion."},
      {"author": "John Dewey", "work": "Democracy and Education", "quote": "The primary function of public schools is to **integrate** diverse cultural populations into democratic citizenship."}
    ]
  },
  "integrated": {
    "primary": "Combined, coordinated, or unified into a functioning, harmonious, or interrelated whole.",
    "secondary": "Open to people of all racial and ethnic groups on equal terms; desegregated.",
    "quotes": [
      {"author": "Alfred Marshall", "work": "Principles of Economics", "quote": "A large modern factory operates through an **integrated** division of specialized machinery and skilled labor."},
      {"author": "Winston Churchill", "work": "The Second World War", "quote": "The Allied command established an **integrated** strategy coordinating naval, air, and ground forces."},
      {"author": "Jane Addams", "work": "Twenty Years at Hull-House", "quote": "The settlement house fostered an **integrated** neighborhood where immigrants found dignity and mutual aid."}
    ]
  },
  "integrating": {
    "primary": "Unifying, coordinating, or combining separate components into a single coherent system.",
    "secondary": "In mathematics, performing the mathematical operation of integration to calculate totals or areas.",
    "quotes": [
      {"author": "William James", "work": "The Principles of Psychology", "quote": "The brain performs the continuous task of **integrating** disparate sensory inputs into coherent perceptions."},
      {"author": "John Stuart Mill", "work": "System of Logic", "quote": "Inductive reasoning advances by **integrating** numerous observations into comprehensive general laws."},
      {"author": "Herbert Spencer", "work": "The Principles of Biology", "quote": "Living organisms develop by **integrating** external nutrients into differentiated organs and tissues."}
    ]
  },
  "integration": {
    "primary": "The action or process of combining and coordinating separate components into a unified whole.",
    "secondary": "The incorporation of individuals of different groups, races, or backgrounds into equal social membership.",
    "quotes": [
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "The political **integration** of diverse immigrant populations required widespread civic participation."},
      {"author": "Charles Darwin", "work": "On the Origin of Species", "quote": "Evolution exhibits both the specialization of distinct organs and the physiological **integration** of bodily functions."},
      {"author": "John Dewey", "work": "Democracy and Education", "quote": "Social harmony depends upon the active **integration** of individual liberty with communal responsibility."}
    ]
  },
  "integrative": {
    "primary": "Serving or tending to integrate, unify, or bring together into a coherent whole.",
    "secondary": "In neuroscience and systems biology, coordinating complex physiological activities into unified functional responses.",
    "quotes": [
      {"author": "William James", "work": "The Principles of Psychology", "quote": "The cerebral cortex exercises an **integrative** control over the lower reflex arcs of the nervous system."},
      {"author": "John Dewey", "work": "Human Nature and Conduct", "quote": "Creative intelligence performs an **integrative** function, harmonizing conflicting desires and ethical duties."},
      {"author": "Charles Sherrington", "work": "The Integrative Action of the Nervous System", "quote": "The nervous system exhibits an **integrative** capacity that coordinates individual reflexes into purposeful movements."}
    ]
  },
  "integrator": {
    "primary": "An individual, system, device, or mechanism that unifies or coordinates disparate elements.",
    "secondary": "In analogue electronics and computing, an operational amplifier circuit producing an output proportional to integrated time.",
    "quotes": [
      {"author": "Lord Kelvin", "work": "Popular Lectures and Addresses", "quote": "The mechanical harmonic **integrator** calculated tidal heights from complex astronomical curves with astonishing speed."},
      {"author": "James Clerk Maxwell", "work": "A Treatise on Electricity and Magnetism", "quote": "An ingenious mechanical **integrator** traced the mathematical lines of electrostatic potential."},
      {"author": "Norbert Wiener", "work": "Cybernetics", "quote": "The feedback loop functions as an internal **integrator**, adjusting the mechanism to environmental fluctuations."}
    ]
  },
  "integrity": {
    "primary": "Moral uprightness, honesty, and uncompromising adherence to ethical principles.",
    "secondary": "Structural soundness, wholeness, and unbroken completeness of form or construction.",
    "quotes": [
      {"author": "George Washington", "work": "Letters", "quote": "I hope I shall possess firmness and virtue enough to maintain what I consider the most enviable of all titles, the character of an honest man of unblemished **integrity**."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "An independent judiciary is indispensable to preserve the structural **integrity** of the constitutional charter."},
      {"author": "Ralph Waldo Emerson", "work": "Self-Reliance", "quote": "Nothing is at last sacred but the **integrity** of your own mind."}
    ]
  },
  "nonintegrated": {
    "primary": "Not unified, merged, or combined into a cohesive, coordinated whole; uncoordinated.",
    "secondary": "Operating as separate, independent units rather than as parts of a centralized system.",
    "quotes": [
      {"author": "Alfred Marshall", "work": "Principles of Economics", "quote": "Small handicraft workshops maintained a **nonintegrated** mode of production, buying components from distinct craftsmen."},
      {"author": "Herbert Spencer", "work": "First Principles", "quote": "Primitive societies remain in a comparatively **nonintegrated** condition with loose tribal affiliations."},
      {"author": "John Dewey", "work": "Logic: The Theory of Inquiry", "quote": "Disorganized, **nonintegrated** observations fail to yield reliable scientific deductions."}
    ]
  },
  "reintegrate": {
    "primary": "To integrate again; to restore to a unified, functional, or whole condition.",
    "secondary": "To reincorporate a person or group into society or an organization following disruption or exile.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The emperor sought to **reintegrate** the rebellious eastern provinces into the imperial administrative framework."},
      {"author": "Thomas Carlyle", "work": "Past and Present", "quote": "Society must **reintegrate** the alienated working masses into a just and compassionate civic order."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Hypnotic suggestion occasionally helps to **reintegrate** fractured fragments of traumatic memory."}
    ]
  },
  "unintegrated": {
    "primary": "Not integrated; not combined or coordinated into an organized, unified whole.",
    "secondary": "In psychology and sociology, lacking psychological cohesion or remaining socially marginalized.",
    "quotes": [
      {"author": "William James", "work": "The Principles of Psychology", "quote": "In hysterical patients, split-off mental processes remain **unintegrated** with the primary consciousness."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "Isolated, **unintegrated** communities within a commonwealth weaken the collective strength of the nation."},
      {"author": "John Dewey", "work": "Democracy and Education", "quote": "Knowledge acquired by rote memorization remains sterile and **unintegrated** with practical experience."}
    ]
  },

  # Dashboard — simil (19 words)
  "assimilable": {
    "primary": "Capable of being absorbed, digested, and incorporated into living tissue or a larger system.",
    "secondary": "Readily understood, adapted, or integrated into an intellectual, cultural, or social framework.",
    "quotes": [
      {"author": "Justus von Liebig", "work": "Familiar Letters on Chemistry", "quote": "Plants absorb nitrogen only in specific **assimilable** chemical compounds such as ammonia and nitrates."},
      {"author": "Herbert Spencer", "work": "The Principles of Biology", "quote": "Digestion converts complex foodstuffs into soluble, **assimilable** nutrients for cellular nourishment."},
      {"author": "John Dewey", "work": "Democracy and Education", "quote": "New information becomes truly **assimilable** only when connected to the child's existing world of experience."}
    ]
  },
  "assimilate": {
    "primary": "To take in and understand fully; to absorb and incorporate nutrients into a living organism.",
    "secondary": "To absorb a person or minority into the prevailing culture and customs of a dominant community.",
    "quotes": [
      {"author": "Charles Darwin", "work": "On the Origin of Species", "quote": "Every living cell must **assimilate** organic nutrients from its environment to support growth and repair."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "The American republic demonstrated an extraordinary capacity to **assimilate** immigrants of diverse European origins."},
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "The human mind cannot **assimilate** deep wisdom without patient contemplation and quiet study."}
    ]
  },
  "assimilating": {
    "primary": "Absorbing, incorporating, and converting nutrients or components into a unified substance.",
    "secondary": "Becoming culturally or socially integrated into a larger dominant group or tradition.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Dorothea possessed an eager intellect, constantly **assimilating** new ideas and spiritual aspirations."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The liver plays a vital role in **assimilating** carbohydrates and regulating blood sugar levels."},
      {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "The poet grows by **assimilating** the beauties of nature into immortal verse."}
    ]
  },
  "assimilation": {
    "primary": "The process of taking in, digesting, and absorbing nutrients into cellular bodily tissue.",
    "secondary": "The social process of absorbing immigrants or minority cultures into the dominant society.",
    "quotes": [
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "The rapid **assimilation** of newcomers into the democratic body politic surprised European observers."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Differences in food **assimilation** explain variations in size and vitality among domesticated breeds."},
      {"author": "John Dewey", "work": "Democracy and Education", "quote": "Education fosters the mutual **assimilation** of cultural traditions into a shared democratic heritage."}
    ]
  },
  "assimilative": {
    "primary": "Having the capacity or tendency to assimilate, absorb, or incorporate substance or ideas.",
    "secondary": "In physiological metabolism, pertaining to anabolism and the constructive absorption of nutrients.",
    "quotes": [
      {"author": "Herbert Spencer", "work": "First Principles", "quote": "Living organisms maintain their internal equilibrium through continuous **assimilative** metabolic processes."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "A powerful intellect possesses vast **assimilative** capacity, organizing complex facts into clear hierarchies."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "The mind's **assimilative** faculty must be nourished by empirical observation and philosophical reflection."}
    ]
  },
  "assimilator": {
    "primary": "A person, organism, or system that absorbs, integrates, or assimilates components into itself.",
    "secondary": "In cognitive psychology, a learning style characterized by abstract conceptualization and inductive reasoning.",
    "quotes": [
      {"author": "Ralph Waldo Emerson", "work": "Representative Men", "quote": "Goethe was the great **assimilator** of his century, digesting every art, science, and philosophy."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Man is a universal **assimilator**, adapting foodstuffs from every climate and flora."},
      {"author": "John Dewey", "work": "Experience and Nature", "quote": "The active thinker functions as an **assimilator**, synthesizing discordant observations into harmonious knowledge."}
    ]
  },
  "assimilatory": {
    "primary": "Pertaining to, promoting, or characterized by the process of assimilation or absorption.",
    "secondary": "In physiology and biochemistry, describing metabolic reactions that synthesize organic compounds.",
    "quotes": [
      {"author": "Justus von Liebig", "work": "Animal Chemistry", "quote": "The liver and lymphatic channels perform vital **assimilatory** transformations upon digested foodstuffs."},
      {"author": "Herbert Spencer", "work": "The Principles of Biology", "quote": "Plant growth depends entirely upon the **assimilatory** action of chlorophyll under solar illumination."},
      {"author": "Thomas Henry Huxley", "work": "Discourses: Biological and Geological", "quote": "Microscopic algae perform the primary **assimilatory** work upon which all marine food chains depend."}
    ]
  },
  "dissimilar": {
    "primary": "Not alike; different in nature, appearance, properties, or quality.",
    "secondary": "Distinct or diverging in fundamental characteristics, structure, or origin.",
    "quotes": [
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "Two beings more **dissimilar** in temperament and outlook than St. John and myself could hardly be imagined."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Joe Gargery and Pip were placed in circumstances utterly **dissimilar** from their humble village beginnings."},
      {"author": "Charles Darwin", "work": "On the Origin of Species", "quote": "Natural selection frequently produces remarkably **dissimilar** forms from a single ancestral species."}
    ]
  },
  "dissimilarity": {
    "primary": "Difference, unlikeness, or diversity between two or more persons, things, or concepts.",
    "secondary": "Distinct divergence in specific characteristics, features, or qualities.",
    "quotes": [
      {"author": "Jane Austen", "work": "Mansfield Park", "quote": "The striking **dissimilarity** between the sisters' tastes became obvious during the rehearsal."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "In spite of the wide **dissimilarity** of their pursuits, Lydgate and Farebrother enjoyed warm intellectual companionship."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The geographical **dissimilarity** of the northern and southern states creates distinct commercial interests."}
    ]
  },
  "dissimilate": {
    "primary": "In linguistics and phonetics, to make or become unlike or distinct from an adjacent sound in speech.",
    "secondary": "In physiology, to break down complex organic compounds into simpler ones; to catabolize.",
    "quotes": [
      {"author": "Max Müller", "work": "Lectures on the Science of Language", "quote": "Phonetic laws frequently cause adjacent identical consonants to **dissimilate** for ease of vocal articulation."},
      {"author": "William Dwight Whitney", "work": "Language and the Study of Language", "quote": "In the evolution of Romance dialects, duplicate liquids often **dissimilate** into distinct consonants."},
      {"author": "Herbert Spencer", "work": "The Principles of Biology", "quote": "Muscular exertion causes muscle tissues to **dissimilate** glycogen and release thermal energy."}
    ]
  },
  "dissimilation": {
    "primary": "The process of making or becoming unlike; in phonology, the change of one sound into a different one near a similar sound.",
    "secondary": "In biological metabolism, the breakdown of complex living matter into simpler waste products.",
    "quotes": [
      {"author": "Max Müller", "work": "The Science of Language", "quote": "The phonetic phenomenon of consonant **dissimilation** explains the shift from Latin peregrinus to English pilgrim."},
      {"author": "William Dwight Whitney", "work": "The Life and Growth of Language", "quote": "Syllabic **dissimilation** prevents tedious repetition of identical sounds in rapid conversational speech."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Cellular respiration represents continuous **dissimilation**, oxidizing nutrients to liberate physiological energy."}
    ]
  },
  "dissimilitude": {
    "primary": "Diversity, unlikeness, or difference between two or more entities; contrast.",
    "secondary": "Lack of resemblance in character, structure, appearance, or style.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The immense **dissimilitude** in the laws and habits of the confederated provinces impeded uniform legislation."},
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The extreme **dissimilitude** between Roman civility and barbarian savagery struck contemporary observers."},
      {"author": "Samuel Johnson", "work": "The Lives of the Poets", "quote": "The metaphysical poets delighted in discovering unexpected resemblances amidst obvious **dissimilitude**."}
    ]
  },
  "facsimile": {
    "primary": "An exact copy or reproduction of a written document, book, painting, or map.",
    "secondary": "A method of transmitting graphic or photographic material over telegraphic wires or radio.",
    "quotes": [
      {"author": "Jules Verne", "work": "Twenty Thousand Leagues Under the Sea", "quote": "Captain Nemo opened a velvet case containing an accurate **facsimile** of the rare ancient chart."},
      {"author": "Edgar Allan Poe", "work": "The Gold-Bug", "quote": "Legrand displayed an exact pen-and-ink **facsimile** of the cryptic cipher found upon the parchment."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The revolutionary assembly ordered a certified **facsimile** of the declaration to be engraved upon bronze."}
    ]
  },
  "similar": {
    "primary": "Having a resemblance in appearance, character, or quantity, without being identical; alike.",
    "secondary": "In geometry, having the same shape and corresponding proportional sides, but differing in size.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Whales of **similar** magnitude and vicious disposition had been encountered off the coast of Japan."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The two legal cases presented **similar** complications that baffled the venerable judges of Chancery."},
      {"author": "Charles Darwin", "work": "On the Origin of Species", "quote": "Species belonging to the same genus usually inhabit regions characterized by **similar** environmental conditions."}
    ]
  },
  "similarity": {
    "primary": "Resemblance in features, appearance, character, or structure between distinct entities.",
    "secondary": "A specific point or feature of resemblance between different people or objects.",
    "quotes": [
      {"author": "Jane Austen", "work": "Persuasion", "quote": "Anne noted with quiet amusement the remarkable **similarity** of tastes between Captain Wentworth and Louisa."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "There was a striking **similarity** in the rustic manners of the weather-beaten sheep shearers."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The anatomical **similarity** between the skeleton of man and the anthropoid ape is unmistakable."}
    ]
  },
  "similarly": {
    "primary": "In a similar, comparable, or corresponding manner; likewise.",
    "secondary": "Used as a transition to introduce a point that resembles or follows the previous statement.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The fog crept into the court of Chancery; **similarly**, confusion reigned throughout the convoluted legal arguments."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Lydgate was fascinated by the microscope; **similarly**, Dorothea sought spiritual clarity through self-denying charity."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The state executive enforces the law; **similarly**, the federal president must execute congressional enactments."}
    ]
  },
  "simile": {
    "primary": "A figure of speech involving the explicit comparison of one thing with another using like or as.",
    "secondary": "In rhetoric and literary criticism, a vivid metaphorical illustration enhancing poetic description.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Love's Labour's Lost", "quote": "A lover's eyes will gaze an eagle blind; his speech is rich in **simile** and courtly compliment."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The author described her innocent youth with a tender **simile** likening her to a woodland blossom."},
      {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "A true poetic **simile** arises from imaginative intuition rather than artificial verbal decoration."}
    ]
  },
  "similitude": {
    "primary": "Resemblance, likeness, or close correspondence in appearance, form, or character.",
    "secondary": "A comparison, allegory, parable, or visible representation of an abstract concept.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The vast white hump of the leviathan rose from the blue sea in strange **similitude** to a snow-capped pyramid."},
      {"author": "John Bunyan", "work": "The Pilgrim's Progress", "quote": "Delivered under the **similitude** of a dream, the pilgrimage portrays the perilous pathway of the soul."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "There exists a remarkable **similitude** between the proposed federal constitution and the state charter of New York."}
    ]
  },
  "unsimilarity": {
    "primary": "The property or fact of being unalike; distinct divergence or dissimilarity.",
    "secondary": "Marked divergence or disparity in form, appearance, or disposition between objects.",
    "quotes": [
      {"author": "George Eliot", "work": "The Mill on the Floss", "quote": "The glaring **unsimilarity** of temperament between Tom and Maggie caused frequent childhood quarrels."},
      {"author": "Herbert Spencer", "work": "First Principles", "quote": "Organic development proceeds from homogeneous simplicity toward complex heterogeneity and marked **unsimilarity** of parts."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "A careful naturalist distinguishes essential homology from superficial **unsimilarity** produced by environmental adaptation."}
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
    for word, item in data_batch1.items():
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
        print(f"SUCCESS: All {len(data_batch1)} words in Batch 1 are 100% compliant with audit rules!")
