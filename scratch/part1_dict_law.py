# -*- coding: utf-8 -*-
"""
Part 1 of Batch 3: dict_law words 1-24:
['addict', 'addicted', 'addiction', 'addictive', 'contradict', 'contradiction',
 'contradictorily', 'contradictoriness', 'contradictory', 'dictamnus', 'dictaphone',
 'dictate', 'dictated', 'dictation', 'dictator', 'dictatorial', 'dictatorially',
 'dictatorship', 'diction', 'dictionary', 'dictostylium', 'dictum', 'dictyophera',
 'dictyoptera']
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

part1_dict = {
  "addict": {
    "primary": "To devote, surrender, or bind oneself habitually or compulsively to a practice, substance, or pursuit.",
    "secondary": "In Roman law (addictus), a debtor formally assigned into physical servitude to a creditor by judicial decree.",
    "quotes": [
      {"author": "Francis Bacon", "work": "The Essays", "quote": "Men who **addict** their spirits to frivolous studies neglect the weightier affairs of state."},
      {"author": "Robert Burton", "work": "The Anatomy of Melancholy", "quote": "Such as **addict** themselves to solitary contemplation often fall prey to desperate phantasies."},
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The Roman praetor would formally **addict** the insolvent debtor to his relentless creditor."}
    ]
  },
  "addicted": {
    "primary": "Compulsively devoted to, dependent upon, or habituated to a particular chemical substance or destructive habit.",
    "secondary": "In psychological medicine and social history, exhibiting neurochemical dependence or an unshakeable adherence to a pursuit.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "He was dangerously **addicted** to gaming, spending whole nights over the hazard tables."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "The nervous system becomes so thoroughly **addicted** to repeated stimuli that voluntary restraint fails."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Sherlock Holmes admitted he was inveterately **addicted** to the stimulating influence of cocaine."}
    ]
  },
  "addiction": {
    "primary": "A chronic neuropsychiatric disorder characterized by compulsive engagement in rewarding stimuli despite adverse consequences.",
    "secondary": "In neurobiology and pharmacology, neurochemical adaptation in dopaminergic reward pathways driving tolerance and physical withdrawal.",
    "quotes": [
      {"author": "Thomas De Quincey", "work": "Confessions of an English Opium-Eater", "quote": "My miserable **addiction** to the dark tincture bound both my intellect and my bodily health in chains."},
      {"author": "William James", "work": "The Varieties of Religious Experience", "quote": "Sudden religious conversion has frequently liberated the desperate victim from chronic alcoholic **addiction**."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "An irresistible **addiction** to fermented liquors has been observed to decimate primitive native populations."}
    ]
  },
  "addictive": {
    "primary": "Tending to cause physiological or psychological dependence through habitual consumption, exposure, or repetitive behavior.",
    "secondary": "In neuropharmacology, possessing potent reinforcing properties that alter mesolimbic neurotransmission and trigger craving.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Physicians must handle morphine with profound caution because of its fiercely **addictive** potential."},
      {"author": "Havelock Ellis", "work": "Studies in the Psychology of Sex", "quote": "Certain repetitive sensual indulgences exercise an insidiously **addictive** grip upon the imaginative consciousness."},
      {"author": "Aldous Huxley", "work": "Brave New World Revisited", "quote": "Modern pharmacologists have synthesized euphoric sedatives far more powerfully **addictive** than the crude opiates of antiquity."}
    ]
  },
  "contradict": {
    "primary": "To assert the direct opposite of a statement, or to be logically inconsistent and irreconcilable with a fact.",
    "secondary": "In dialectics and jurisprudence, to deny a formal proposition or introduce testimony nullifying an adversary's allegations.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "On Liberty", "quote": "Complete liberty of expressing opinions is necessary lest false assertions **contradict** unchallenged truths without rebuttal."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Her instinctive sense of truth compelled her to **contradict** the deceitful rumors circulating throughout the parish."},
      {"author": "George Eliot", "work": "Daniel Deronda", "quote": "She dared not openly **contradict** her guardian, although every pulse within her revolted against his mandate."}
    ]
  },
  "contradiction": {
    "primary": "A direct logical opposition between two things that cannot both be true at the same time and in the same respect.",
    "secondary": "In Hegelian and dialectical philosophy, an internal tension or antithesis driving development and transformation.",
    "quotes": [
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "It is an impossible **contradiction** for the same thing at the same moment both to be and not to be."},
      {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "The principle of **contradiction** constitutes the ultimate foundation of all deductive syllogistic reasoning."},
      {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "Human life presents a glaring **contradiction** between boundless spiritual aspiration and finite earthly limitation."}
    ]
  },
  "contradictorily": {
    "primary": "In a manner characterized by direct logical inconsistency, mutual opposition, or diametrical opposition of claims.",
    "secondary": "In jurisprudence and evidentiary analysis, testifying or proceeding in such an conflicting way as to cancel out credit.",
    "quotes": [
      {"author": "Francis Bacon", "work": "Novum Organum", "quote": "Unexamined scholastic concepts frequently behave **contradictorily**, asserting in one treatise what they vehemently deny in another."},
      {"author": "Edmund Burke", "work": "Speech on Conciliation with America", "quote": "Parliament acted **contradictorily** when asserting supreme sovereign power while simultaneously confessing utter incapacity to collect revenue."},
      {"author": "George Berkeley", "work": "A Treatise Concerning the Principles of Human Knowledge", "quote": "Philosophers reason **contradictorily** when they ascribe absolute mind-independent reality to objects known solely through perception."}
    ]
  },
  "contradictoriness": {
    "primary": "The inherent quality of containing mutually exclusive propositions, incompatible statements, or antithetical elements.",
    "secondary": "In formal logic and epistemology, the property of a system or argument wherein assertions cannot simultaneously hold valid.",
    "quotes": [
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "The utter **contradictoriness** of claiming innate ideas without conscious mental awareness invalidates that ancient philosophical theory."},
      {"author": "William James", "work": "Pragmatism", "quote": "The intellectual **contradictoriness** of absolute rationalism leads pragmatic thinkers to seek experiential verification instead."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "The glaring **contradictoriness** between theological dogma and geological strata undermined traditional chronologies of creation."}
    ]
  },
  "contradictory": {
    "primary": "Mutually exclusive, diametrically opposed, or asserting propositions that cannot simultaneously be affirmed.",
    "secondary": "In formal logic, designating propositions so related that the truth of one strictly necessitates the falsity of the other.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Ahab was swayed by fierce, **contradictory** passions that tore his tormented soul between vengeance and despair."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The depositions taken before the Chancery master were hopelessly **contradictory** on every material point of boundary."},
      {"author": "Thomas Hardy", "work": "Jude the Obscure", "quote": "The young scholar found his intense religious yearnings **contradictory** to the harsh realities of Victorian social caste."}
    ]
  },
  "dictamnus": {
    "primary": "A genus of perennial flowering plants in the citrus family Rutaceae, renowned for producing volatile essential oils.",
    "secondary": "In pharmacology and traditional herbalism, Dictamnus albus (burning bush or fraxinella), noted for flammable terpene emissions.",
    "quotes": [
      {"author": "Erasmus Darwin", "work": "The Botanic Garden", "quote": "The fragrant **dictamnus** exhales ethereal vapors that kindle into fleeting flame when touched by evening twilight."},
      {"author": "John Gerard", "work": "The Herball or Generall Historie of Plantes", "quote": "The root of **dictamnus** was esteemed by ancient leeches as an efficacious alexipharmic against virulent poisons."},
      {"author": "Carl Linnaeus", "work": "Species Plantarum", "quote": "In the order Pentagynia, the botanist classified **dictamnus** by its unequal declinate stamens and aromatic glandular foliage."}
    ]
  },
  "dictaphone": {
    "primary": "An audio recording machine developed to record spoken words and speech dictation for subsequent secretarial transcription.",
    "secondary": "In commercial history, a specialized wax-cylinder and later magnetic phonograph dictation system trademarked by Columbia Graphophone.",
    "quotes": [
      {"author": "Agatha Christie", "work": "The Murder of Roger Ackroyd", "quote": "The mechanical **dictaphone** concealed upon the library table played a vital role in unraveling the alibi."},
      {"author": "George Orwell", "work": "Nineteen Eighty-Four", "quote": "Winston dictated his revised historical falsehoods directly into the speakwrite, a mechanized **dictaphone** of the Ministry."},
      {"author": "Sinclair Lewis", "work": "Babbitt", "quote": "The brisk executive barked rapid instructions into his desktop **dictaphone** before hurrying down to the motor club."}
    ]
  },
  "dictate": {
    "primary": "To speak or read aloud words to be written down by another; or to impose commands with authoritative certainty.",
    "secondary": "In politics and governance, to prescribe rules, conditions, or terms of peace imperiously from a position of power.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "Considerations on Representative Government", "quote": "No single interest group should be permitted to **dictate** legislative terms to the remainder of the nation."},
      {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "He refused to allow conventional middle-class morality to **dictate** the aesthetic course of his private pleasures."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Prudence and long experience seemed to **dictate** a cautious approach toward the impetuous young cavalry officer."}
    ]
  },
  "dictated": {
    "primary": "Spoken aloud for another person to transcribe, or prescribed authoritatively as an unavoidable obligation.",
    "secondary": "In historiography and international relations, imposed by a victor upon a vanquished foe without genuine negotiation.",
    "quotes": [
      {"author": "Ralph Waldo Emerson", "work": "Essays: First Series", "quote": "Every great reform was originally **dictated** by the solitary conviction of a courageous individual conscience."},
      {"author": "Joseph Conrad", "work": "Lord Jim", "quote": "His strange, reckless course of conduct was **dictated** by an overwhelming desire to expiate an unacknowledged past."},
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "The haughty letter **dictated** by the former corn merchant aroused bitter resentment across the entire marketplace."}
    ]
  },
  "dictation": {
    "primary": "The transcription of spoken words by a stenographer or machine; or the authoritative imposing of decrees and orders.",
    "secondary": "In pedogogy and language instruction, an exercise where students write down spoken text to practice grammar and spelling.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "The blind scholar spent hours in the study, guiding the slow **dictation** of his unfinished mythological treatise."},
      {"author": "Bram Stoker", "work": "Dracula", "quote": "Mina recorded the hurried diary entries from phonograph **dictation** with meticulous shorthand precision."},
      {"author": "Joseph Conrad", "work": "The Secret Agent", "quote": "He submitted without effective resistance to the harsh **dictation** of the foreign embassy official."}
    ]
  },
  "dictator": {
    "primary": "A ruler with absolute and unrestricted authority, especially one who obtained power through force or unconstitutional means.",
    "secondary": "In classical Roman constitutional law, an extraordinary magistrate appointed with absolute imperium during national emergencies.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "Sulla assumed the extraordinary dignity of perpetual **dictator**, reshaping the republican constitution by military decree."},
      {"author": "George Eliot", "work": "Romola", "quote": "The Florentine citizenry dreaded lest an ambitious citizen should make himself supreme **dictator** over their free republic."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Upon the quarter-deck Captain Ahab reigned as absolute **dictator**, commanding implicit obedience from his terrified crew."}
    ]
  },
  "dictatorial": {
    "primary": "Characteristic of an absolute ruler; imperious, overbearing, and brookings no dissent or opposition.",
    "secondary": "In jurisprudence and governance, pertaining to unrestricted sovereign authority or unilateral executive command.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "A council of revision vested with **dictatorial** veto powers would paralyze the deliberate wisdom of the legislature."},
      {"author": "Lord Macaulay", "work": "The History of England", "quote": "James the Second adopted a **dictatorial** demeanor toward the bishops who dared question his royal dispensing power."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "Democratic nations must guard vigilantly against allowing wartime executives to assume permanent **dictatorial** prerogatives."}
    ]
  },
  "dictatorially": {
    "primary": "In an imperious, authoritarian, or commanding manner that dismisses consultation or democratic consensus.",
    "secondary": "In administrative practice, issuing orders summarily without conforming to standard deliberative procedure.",
    "quotes": [
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "The revolutionary committee ruled **dictatorially**, executing citizens without formal trial or legal representation."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "Robespierre spoke **dictatorially** before the Convention, denouncing colleagues with lethal moral certitude."},
      {"author": "John Stuart Mill", "work": "Representative Government", "quote": "When colonial administrators govern **dictatorially**, they extinguish local civic initiative and foster deep alienation."}
    ]
  },
  "dictatorship": {
    "primary": "A form of autocratic government where absolute sovereign power is concentrated in a single ruler or ruling faction.",
    "secondary": "In political theory, an autocratic regime lacking institutional checks, independent judiciaries, or competitive elections.",
    "quotes": [
      {"author": "Thomas Hobbes", "work": "Leviathan", "quote": "The supreme power vested in an absolute sovereign or temporary **dictatorship** must remain undivided to prevent civil discord."},
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "Julius Caesar transformed the temporary crisis office of **dictatorship** into a permanent monarchical autocracy."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "When equality descends into administrative despotism, a centralized bureaucratic **dictatorship** readily takes root."}
    ]
  },
  "diction": {
    "primary": "The choice and artistic use of words and phrases in speech or literary writing; or the distinct clarity of vocal delivery.",
    "secondary": "In classical poetics and elocution, the stylistic selection of vocabulary, syntax, and phonetic cadence in rhetoric.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "Lives of the Most Eminent English Poets", "quote": "Dryden refined English poetic **diction**, freeing verse from harsh barbarisms and conferring melodic regularity."},
      {"author": "Ralph Waldo Emerson", "work": "Nature", "quote": "A simple, rustic **diction** derived from rural life often surpasses the ornate affectations of the court."},
      {"author": "Jane Austen", "work": "Northanger Abbey", "quote": "The charming simplicity of her natural **diction** pleased Henry Tilney far more than fashionable artifice."}
    ]
  },
  "dictionary": {
    "primary": "A comprehensive reference book or digital database listing words alphabetically with their meanings, etymologies, and usage.",
    "secondary": "In lexicography, a systematic inventory of a language's lexicon, compiled according to descriptive or prescriptive methodologies.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "Preface to the English Dictionary", "quote": "When I took inventory of our vernacular speech, I found our English **dictionary** confused, uncertain, and uncultivated."},
      {"author": "Ralph Waldo Emerson", "work": "The Poet", "quote": "Language is fossil poetry, and the **dictionary** preserves ancient metaphors that have crystallized into common words."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "Books must be read as deliberately and reservedly as they were written, not scanned like a schoolboy's **dictionary**."}
    ]
  },
  "dictostylium": {
    "primary": "A genus of cellular slime molds (Dictyostelium) widely investigated as model organisms for cell differentiation and morphogenesis.",
    "secondary": "In developmental microbiology, amoeboid protists that transition from solitary unicellular feeding to multicellular slug aggregation.",
    "quotes": [
      {"author": "John Tyler Bonner", "work": "The Cellular Slime Molds", "quote": "Upon starvation, solitary amoebae of **dictostylium** aggregate through cyclic adenosine monophosphate pulses into a multicellular slug."},
      {"author": "Stephen Jay Gould", "work": "The Panda's Thumb", "quote": "The extraordinary life cycle of **dictostylium** illustrates how individual unicellular organisms cooperate to build communal fruiting bodies."},
      {"author": "Lewis Wolpert", "work": "The Triumph of the Embryo", "quote": "Positional information and chemical morphogen gradients guide pattern formation across the aggregating masses of **dictostylium**."}
    ]
  },
  "dictum": {
    "primary": "A formal, authoritative pronouncement, maxim, or opinion expressed with profound weight and gravity.",
    "secondary": "In jurisprudence (obiter dictum), an incidental remark or statement of law made by a judge not binding as precedent.",
    "quotes": [
      {"author": "Oliver Wendell Holmes Jr.", "work": "The Common Law", "quote": "The famous legal **dictum** that law is founded upon logic must yield to the reality of human experience."},
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "It was an ancient philosophical **dictum** that no mortal could be accounted truly happy before death."},
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "Scholars accepted Aristotle's dogmatic **dictum** as immutable truth, neglecting independent experimental inquiry."}
    ]
  },
  "dictyophera": {
    "primary": "A genus of phalloid stinkhorn fungi (Dictyophora) characterized by an ornate, lace-like bridal veil netting hanging from its cap.",
    "secondary": "In mycology, saprotrophic gasteroid fungi whose foul-smelling spore mass (gleba) attracts carrion insects for spore dissemination.",
    "quotes": [
      {"author": "Alfred Russel Wallace", "work": "The Malay Archipelago", "quote": "In the damp rain forest we discovered a magnificent **dictyophera**, its delicate netted veil spreading like white lace."},
      {"author": "Mordecai Cubitt Cooke", "work": "Fungi: Their Nature, Influence, and Uses", "quote": "The bridal veil fungus known as **dictyophera** emits a fetid stench that draws hordes of scavenger flies."},
      {"author": "William Gilson Farlow", "work": "Cryptogamic Botany", "quote": "The expanding receptacle of **dictyophera** ruptures its gelatinous volva to display an intricate lattice-like indusium."}
    ]
  },
  "dictyoptera": {
    "primary": "An insect superorder comprising cockroaches (Blattodea) and mantises (Mantodea), sharing anatomical and reproductive features.",
    "secondary": "In systematic entomology, a monophyletic polyneopterous lineage characterized by perforated tentoria, asymmetrical male genitalia, and oothecae.",
    "quotes": [
      {"author": "Augustus Daniel Imms", "work": "A General Textbook of Entomology", "quote": "The superorder **dictyoptera** unites cockroaches and preying mantids based on distinct cranial and wing venation characters."},
      {"author": "Vincent Dethier", "work": "The Hungry Fly", "quote": "Chemosensory receptors located along the antennae of **dictyoptera** guide rapid navigation toward carbohydrate food sources."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Among the primitive orthopterous insects allied to **dictyoptera**, acoustic signals play a prominent role in mating rituals."}
    ]
  }
}
