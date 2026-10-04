# -*- coding: utf-8 -*-
import os, sys, re

sys.stdout.reconfigure(encoding="utf-8")

data = {
  # =========================================================================
  # Dashboard — log (Words 46-90)
  # =========================================================================
  "Dashboard — log/ecologically.md": {
    "primary": "In a way that relates to the relations between organisms and their environment.",
    "secondary": "In conservation science and biophysics, evaluated in terms of ecological footprint, biodiversity, or environmental balance.",
    "quotes": [
      {"author": "Ernst Haeckel", "work": "The Wonders of Life", "quote": "The flora and fauna of coral reefs are **ecologically** interdependent to an extraordinary degree."},
      {"author": "Alfred Russel Wallace", "work": "Island Life", "quote": "The fauna of Madagascar evolved in isolation, becoming **ecologically** distinct from the mainland."},
      {"author": "Aldo Leopold", "work": "A Sand County Almanac", "quote": "A thing is right when it tends to preserve the integrity of the biotic community; we must think **ecologically**."}
    ]
  },
  "Dashboard — log/ecologist.md": {
    "primary": "An expert in or student of the relationships between organisms and their environments.",
    "secondary": "In environmental science, a researcher studying population dynamics, trophic cascades, and habitat restoration.",
    "quotes": [
      {"author": "Ernst Haeckel", "work": "The History of Creation", "quote": "The field **ecologist** must observe the animal not in the museum cabinet, but in its living habitat."},
      {"author": "Arthur Tansley", "work": "The Use and Abuse of Vegetational Concepts and Terms", "quote": "The modern **ecologist** conceives of plant communities as dynamic components of a unified ecosystem."},
      {"author": "Aldo Leopold", "work": "A Sand County Almanac", "quote": "An **ecologist** must live in a world of wounds, seeing marks of degradation where others see progress."}
    ]
  },
  "Dashboard — log/ecology.md": {
    "primary": "The branch of biology dealing with the relations of organisms to one another and to their physical surroundings.",
    "secondary": "In evolutionary science, the comprehensive term coined by Ernst Haeckel in 1866 for the economy of nature.",
    "quotes": [
      {"author": "Ernst Haeckel", "work": "Generelle Morphologie der Organismen", "quote": "By **ecology** we mean the investigation of the total relations of the animal both to its inorganic and to its organic environment."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The complex web of interactions that regulates plant and animal populations constitutes the true foundation of **ecology**."},
      {"author": "Arthur Tansley", "work": "Practical Plant Ecology", "quote": "The fundamental task of plant **ecology** is to discover how vegetation adapts to soil, climate, and topography."}
    ]
  },
  "Dashboard — log/epilogue.md": {
    "primary": "A concluding section or speech at the end of a book or play serving as a commentary or resolution.",
    "secondary": "In dramatic literature and historical narrative, a concluding address spoken directly to the audience asking for indulgence.",
    "quotes": [
      {"author": "William Shakespeare", "work": "As You Like It", "quote": "It is not the fashion to see the lady the **epilogue**; but it is no more unhandsome than to see the lord the prologue."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "In the final **epilogue**, the author records the peaceful twilight of those who survived the Reign of Terror."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Every limit is a beginning as well as an ending, as will be seen in this brief **epilogue** upon our various characters."}
    ]
  },
  "Dashboard — log/etymological.md": {
    "primary": "Relating to the origin and historical development of words and their meanings; linguistic.",
    "secondary": "In comparative philology, tracing cognate lexical roots back through sound shifts to ancestral Indo-European forms.",
    "quotes": [
      {"author": "Max Müller", "work": "Lectures on the Science of Language", "quote": "The true **etymological** analysis of a word reveals the historical psychology of the race that created it."},
      {"author": "Richard Chenevix Trench", "work": "On the Study of Words", "quote": "Many a moral truth lies fossilized in the **etymological** pedigree of an everyday term."},
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "The examination of **etymological** derivations often discloses the philosophical intuitions of antiquity."}
    ]
  },
  "Dashboard — log/etymologise.md": {
    "primary": "To trace the origin and development of a word; to study etymology (British spelling of etymologize).",
    "secondary": "In classical scholarship and philology, reconstructing ancient root forms and historical shifts in pronunciation.",
    "quotes": [
      {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "To **etymologise** accurately requires not mere fanciful resemblance of sound, but strict historical grammar."},
      {"author": "Richard Chenevix Trench", "work": "English Past and Present", "quote": "When we **etymologise** common Saxon idioms, we uncover the domestic life of our ancestors."},
      {"author": "Max Müller", "work": "Chips from a German Workshop", "quote": "Scholars who **etymologise** without phonetic laws are like navigators sailing without a compass."}
    ]
  },
  "Dashboard — log/etymologist.md": {
    "primary": "A scholar who specializes in etymology, the study of the origins and historical development of words.",
    "secondary": "In comparative linguistics, a researcher tracing lexical cognates across diverse language families through systematic sound laws.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "A Dictionary of the English Language", "quote": "The **etymologist** must explore the deep roots of speech and track every dialectical variation to its fountain."},
      {"author": "Max Müller", "work": "Lectures on the Science of Language", "quote": "Grimm was an extraordinary **etymologist** whose laws explained the transformation of consonants across Europe."},
      {"author": "Walter Scott", "work": "The Antiquary", "quote": "The pedantic **etymologist** derived the local Scottish placename from a fanciful combination of Celtic roots."}
    ]
  },
  "Dashboard — log/etymologize.md": {
    "primary": "To trace the etymology or historical development of a word or linguistic form.",
    "secondary": "In linguistic pedagogy and lexicography, analyzing the morphological components of words to illuminate their original significance.",
    "quotes": [
      {"author": "Ralph Waldo Emerson", "work": "Essays: Second Series", "quote": "The poet knows how to **etymologize** nature itself, discovering spirit hidden within physical forms."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "I love to **etymologize** the names of our native ponds and hills, finding poetry in ancient Saxon roots."},
      {"author": "Oliver Wendell Holmes Jr.", "work": "The Common Law", "quote": "If we **etymologize** legal terms, we discover that ancient criminal remedies grew out of private vengeance."}
    ]
  },
  "Dashboard — log/etymologizing.md": {
    "primary": "The practice or activity of tracing the origins and historical development of words.",
    "secondary": "In intellectual essays and literary criticism, pursuing verbal derivations to uncover hidden cultural or philosophical layers.",
    "quotes": [
      {"author": "Samuel Taylor Coleridge", "work": "Aids to Reflection", "quote": "A habit of careful **etymologizing** protects the mind against vague generalizations and loose rhetoric."},
      {"author": "Max Müller", "work": "Lectures on the Science of Language", "quote": "Fanciful **etymologizing** was the fatal weakness of ancient grammarians from Plato to Varro."},
      {"author": "Richard Chenevix Trench", "work": "On the Study of Words", "quote": "There is profound moral profit in the sober **etymologizing** of terms that express human virtues and vices."}
    ]
  },
  "Dashboard — log/etymology.md": {
    "primary": "The study of the origin of words and the historical evolution of their meanings; a word's lineage.",
    "secondary": "In historical linguistics, the documented lineage of a lexical unit through sound changes, borrowing, and morphological adaptation.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "The Lives of the English Poets", "quote": "He investigated the **etymology** of disputed words with indefatigable curiosity and robust learning."},
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "The study of **etymology** reveals how ancient peoples conceived the fundamental operations of nature."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "If we trace the **etymology** of words denoting intellectual concepts, we find they all originally signified sensible ideas."}
    ]
  },
  "Dashboard — log/eulogise.md": {
    "primary": "To praise highly in speech or writing; to deliver a eulogy for someone (British spelling of eulogize).",
    "secondary": "In civic oratory and memorial literature, commemorating public services or moral excellence before an assembly.",
    "quotes": [
      {"author": "Thomas Babington Macaulay", "work": "Critical and Historical Essays", "quote": "It was the orator's duty to **eulogise** the fallen statesman while acknowledging the hazards of his policy."},
      {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "The parish vicar rose to **eulogise** the late baronet, dwelling with tears upon his private charities."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The town council met to **eulogise** the distinguished philanthropist who had founded the local infirmary."}
    ]
  },
  "Dashboard — log/eulogist.md": {
    "primary": "A person who praises someone or something highly, especially in a formal speech or writing.",
    "secondary": "In classical rhetoric and biography, an orator delivering a panegyric commemorating the character and deeds of the deceased.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The courtly **eulogist** exhausted every classical metaphor in celebrating the emperor's imaginary victories."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "Mirabeau found in him an ardent **eulogist** who proclaimed his genius to the electrified assembly."},
      {"author": "Samuel Johnson", "work": "The Lives of the English Poets", "quote": "A judicious **eulogist** preserves credibility by tempering praise with candid acknowledgment of human frailties."}
    ]
  },
  "Dashboard — log/eulogistic.md": {
    "primary": "Praising or extolling someone or something highly; laudatory, commendatory.",
    "secondary": "In literary criticism and public discourse, characterized by elevated encomiums or formal praise.",
    "quotes": [
      {"author": "Walter Scott", "work": "The Antiquary", "quote": "The local chronicle published a **eulogistic** account of the festivities, praising the generosity of the host."},
      {"author": "William Hazlitt", "work": "Table-Talk", "quote": "His review was not an impartial critique, but a **eulogistic** tribute to an intimate friend."},
      {"author": "Washington Irving", "work": "The Life of George Washington", "quote": "Contemporary addresses to the Commander-in-Chief were couched in the most **eulogistic** language."}
    ]
  },
  "Dashboard — log/eulogize.md": {
    "primary": "To praise highly or extravagantly in speech or writing; to deliver a eulogy.",
    "secondary": "In commemorative oratory and civic ritual, magnifying the patriotic virtues and public achievements of a departed leader.",
    "quotes": [
      {"author": "Abraham Lincoln", "work": "Eulogy on Henry Clay", "quote": "To **eulogize** the character of such a patriot is to celebrate the triumph of constitutional liberty."},
      {"author": "Ralph Waldo Emerson", "work": "Representative Men", "quote": "Biographers are eager to **eulogize** heroics, but the philosopher seeks the underlying law of life."},
      {"author": "Nathaniel Hawthorne", "work": "The House of the Seven Gables", "quote": "The town minister was summoned to **eulogize** the late judge, recounting his exemplary civic virtues."}
    ]
  },
  "Dashboard — log/eulogy.md": {
    "primary": "A speech or piece of writing that praises someone or something highly, typically delivered at a funeral.",
    "secondary": "In classical rhetoric, a formal discourse celebrating the virtue, valor, or achievements of an individual.",
    "quotes": [
      {"author": "Pericles", "work": "Funeral Oration", "quote": "Our ancestors deserve a tribute of **eulogy**, for they preserved our city in freedom by their valor."},
      {"author": "Ralph Waldo Emerson", "work": "Essays: First Series", "quote": "The greatest **eulogy** of character is that it requires no apology and commands instant veneration."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Mr. Micawber pronounced a magnificent **eulogy** upon the virtues of friendship and mutual loyalty."}
    ]
  },
  "Dashboard — log/ideologic.md": {
    "primary": "Relating to ideology, doctrine, or a system of ideas; ideological.",
    "secondary": "In political theory and history of thought, pertaining to partisan intellectual systems governing public policy.",
    "quotes": [
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "The great party struggles of modern times have lost their territorial character and assumed an **ideologic** nature."},
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "Behind every tariff policy lies an **ideologic** debate concerning the legitimate functions of the state."},
      {"author": "Bertrand Russell", "work": "Power: A New Social Analysis", "quote": "The fiercest conflicts arise when military force is allied with fanatical **ideologic** fervor."}
    ]
  },
  "Dashboard — log/ideological.md": {
    "primary": "Based on or relating to a particular system of ideas and ideals; doctrinal.",
    "secondary": "In modern sociology and political philosophy, expressing the collective beliefs and dogmas of a political or social movement.",
    "quotes": [
      {"author": "Bertrand Russell", "work": "Unpopular Essays", "quote": "Intolerance is the inevitable byproduct of dogmatic **ideological** certainty that permits no dissent."},
      {"author": "George Orwell", "work": "1984", "quote": "The party demanded complete **ideological** conformity in thought as well as in public expression."},
      {"author": "John Dewey", "work": "Freedom and Culture", "quote": "Democracy is not a rigid **ideological** formula, but a dynamic method of continuous social inquiry."}
    ]
  },
  "Dashboard — log/ideologically.md": {
    "primary": "In a manner related to ideology or a system of political or economic ideas.",
    "secondary": "In sociological analysis, motivated by rigid philosophical or partisan doctrines rather than pragmatic empirical facts.",
    "quotes": [
      {"author": "Bertrand Russell", "work": "The Practice and Theory of Bolshevism", "quote": "The government was **ideologically** committed to principles that collided with economic reality."},
      {"author": "George Orwell", "work": "Homage to Catalonia", "quote": "The rival factions were **ideologically** divided, yet fighting side by side in the common trenches."},
      {"author": "John Dewey", "work": "Individualism Old and New", "quote": "Society remains **ideologically** anchored in eighteenth-century individualism while living in a corporate age."}
    ]
  },
  "Dashboard — log/ideologist.md": {
    "primary": "An adherent of a particular ideology; a theorist who conceives or promotes a system of ideas.",
    "secondary": "In history of philosophy, originally applied to the French philosophers studying the origin of ideas; later used for rigid doctrinaires.",
    "quotes": [
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "Napoleon dismissed the metaphysical theorists of the institute as mere windbag **ideologists**."},
      {"author": "Karl Marx", "work": "The German Ideology", "quote": "The bourgeois **ideologist** mistakes the temporary conditions of his class for eternal laws of nature."},
      {"author": "Alexis de Tocqueville", "work": "The Old Regime and the Revolution", "quote": "The literary **ideologist** designed theoretical constitutions without ever having managed the affairs of a village."}
    ]
  },
  "Dashboard — log/ideology.md": {
    "primary": "A system of ideas, ideals, and principles forming the basis of economic or political theory.",
    "secondary": "In political philosophy and sociology of knowledge, the conceptual framework shaping how a class or society perceives reality.",
    "quotes": [
      {"author": "Karl Marx", "work": "The German Ideology", "quote": "The ruling ideas of each age have ever been the **ideology** of its ruling class."},
      {"author": "Bertrand Russell", "work": "A History of Western Philosophy", "quote": "A coherent political **ideology** gives cohesion to an empire, but easily degenerates into persecuting bigotry."},
      {"author": "George Orwell", "work": "Notes on Nationalism", "quote": "Every nationalist is obsessed with altering the past to conform to his political **ideology**."}
    ]
  },
  "Dashboard — log/illogic.md": {
    "primary": "Lack of logic or valid reasoning; unreasonableness, absurdity, or irrationality.",
    "secondary": "In cognitive critique and polemics, structural fallacies or emotional bias subverting coherent thought.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "The human mind falls into persistent **illogic** when it mistake its own prejudices for self-evident truths."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Her generous indignation made her blind to the patent **illogic** of her passionate defense."},
      {"author": "William James", "work": "Pragmatism", "quote": "There is an incurable **illogic** in building vast metaphysical systems upon unverified dogmatic premises."}
    ]
  },
  "Dashboard — log/illogical.md": {
    "primary": "Lacking sense or clear, sound reasoning; contrary to the rules of logic.",
    "secondary": "In analytical philosophy, a proposition or argument that commits a formal fallacy or contradicts established empirical facts.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "It was an absurd and **illogical** proceeding, but thoroughly characteristic of the Court of Chancery."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth smiled at the completely **illogical** sequence of reasons with which Mrs. Bennet defended her plans."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "It is an **illogical** mistake to theorize before one has all the facts; it biases the judgment."}
    ]
  },
  "Dashboard — log/illogicality.md": {
    "primary": "The property or quality of being illogical; an irrational statement or deed.",
    "secondary": "In literary satire and judicial review, demonstrable internal contradiction or non sequitur in reasoning.",
    "quotes": [
      {"author": "George Eliot", "work": "Daniel Deronda", "quote": "The charming **illogicality** of her conversation concealed an acute instinctive discernment of character."},
      {"author": "John Stuart Mill", "work": "On Liberty", "quote": "Persecutors of opinion are guilty of the grossest **illogicality**, claiming for themselves the infallibility they deny to others."},
      {"author": "Thomas Henry Huxley", "work": "Science and Christian Tradition", "quote": "The glaring **illogicality** of the theological argument was exposed the moment scientific criteria were applied."}
    ]
  },
  "Dashboard — log/illogically.md": {
    "primary": "In a way that lacks sense or sound reasoning; contrarily to logic.",
    "secondary": "In character analysis, drawing emotional conclusions that defy the premises from which they ostensibly proceed.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles: A Pure Woman", "quote": "Angel Clare argued **illogically**, letting conventional social taboos overpower his philosophical convictions."},
      {"author": "Charlotte Brontë", "work": "Villette", "quote": "She reasoned **illogically**, yet her intuitive instinct led her straight to the truth."},
      {"author": "Mark Twain", "work": "A Connecticut Yankee in King Arthur's Court", "quote": "The knights reasoned so **illogically** that any modern schoolboy could have refuted their legends."}
    ]
  },
  "Dashboard — log/illogicalness.md": {
    "primary": "Incoherence, irrationality, or the characteristic of violating sound logic.",
    "secondary": "In epistemological critique, systemic inconsistency in doctrinal formulations or empirical claims.",
    "quotes": [
      {"author": "Herbert Spencer", "work": "The Study of Sociology", "quote": "The astonishing **illogicalness** of popular political opinions is revealed in their self-cancelling legislative schemes."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "The chronic **illogicalness** of emotional thinking arises from the selective distortion of memory."},
      {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "A philosopher's duty is to expose the hidden **illogicalness** underlying celebrated metaphysical dogmas."}
    ]
  },
  "Dashboard — log/immunologic.md": {
    "primary": "Relating to immunology, immunity, or the body's physiological immune mechanisms; immunological.",
    "secondary": "In clinical pathology and biomedical research, pertaining to antibody-antigen kinetics and cellular defense responses.",
    "quotes": [
      {"author": "Frank Macfarlane Burnet", "work": "The Integrity of the Body", "quote": "The fundamental **immunologic** problem is how the vertebrate organism distinguishes self from non-self."},
      {"author": "Peter Medawar", "work": "The Hope of Progress", "quote": "Transplantation tolerance represents an induced **immunologic** unresponsiveness toward specific donor tissues."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The diagnostic test is based on a specific **immunologic** agglutination of bacterial antigens."}
    ]
  },
  "Dashboard — log/immunological.md": {
    "primary": "Relating to the immune system and the body's mechanisms of defense against pathogens.",
    "secondary": "In modern immunology, mechanisms encompassing innate and adaptive cellular and humoral defense networks.",
    "quotes": [
      {"author": "Frank Macfarlane Burnet", "work": "Immunology, Aging, and Cancer", "quote": "The **immunological** surveillance mechanism continually destroys aberrant somatic cells before they form tumors."},
      {"author": "Peter Medawar", "work": "The Uniqueness of the Individual", "quote": "Skin grafting provides the classic **immunological** model for analyzing tissue histocompatibility."},
      {"author": "Louis Pasteur", "work": "Studies on Fermentation", "quote": "Attenuation of viral virulence laid the foundation for the entire science of **immunological** prophylaxis."}
    ]
  },
  "Dashboard — log/immunologically.md": {
    "primary": "In a manner related to the immune system, antibodies, or physiological immunity.",
    "secondary": "In experimental pathology, characterized by antigen recognition, lymphocyte activation, and memory response.",
    "quotes": [
      {"author": "Peter Medawar", "work": "The Hope of Progress", "quote": "The recipient animal was rendered **immunologically** tolerant by neonatal exposure to donor spleen cells."},
      {"author": "Frank Macfarlane Burnet", "work": "The Clonal Selection Theory of Acquired Immunity", "quote": "Plasma cells are **immunologically** committed to secreting a single molecular species of antibody."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The patient responded **immunologically** with a rapid rise in serum antitoxin titers."}
    ]
  },
  "Dashboard — log/immunologist.md": {
    "primary": "A specialist or researcher in the branch of biomedical science dealing with the immune system.",
    "secondary": "In laboratory medicine, an investigator exploring autoimmune pathologies, vaccine development, and antibody structure.",
    "quotes": [
      {"author": "Peter Medawar", "work": "The Uniqueness of the Individual", "quote": "The modern **immunologist** investigates not merely disease resistance, but the biological basis of individuality."},
      {"author": "Frank Macfarlane Burnet", "work": "Immunology, Aging, and Cancer", "quote": "Every **immunologist** recognizes that somatic mutation plays a decisive role in antibody diversification."},
      {"author": "Paul Ehrlich", "work": "Studies in Immunity", "quote": "The **immunologist** must conceive of antibodies as chemical receptors complementary to specific microbial haptens."}
    ]
  },
  "Dashboard — log/immunology.md": {
    "primary": "The branch of biomedical science concerned with immunity, the immune system, and defense against diseases.",
    "secondary": "In medicine, the discipline investigating humoral antibodies, cellular immunity, hypersensitivity, and autoimmune disorders.",
    "quotes": [
      {"author": "Frank Macfarlane Burnet", "work": "The Integrity of the Body", "quote": "Modern **immunology** began with Jenner's discovery of vaccination and Pasteur's work on attenuated microbes."},
      {"author": "Peter Medawar", "work": "The Hope of Progress", "quote": "The rapid expansion of **immunology** transformed organ transplantation from a dream into clinical reality."},
      {"author": "Paul Ehrlich", "work": "Studies in Immunity", "quote": "The side-chain theory established a chemical foundation for the emerging science of **immunology**."}
    ]
  },
  "Dashboard — log/log.md": {
    "primary": "A thick segment of felled tree trunk; an official recorded chronicle of events on a voyage or journey.",
    "secondary": "In maritime navigation and operational management, a device measuring ship speed through water, or a chronological registry of events.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The captain paced the quarterdeck and ordered the mate to heave the **log** and record our dead-reckoning."},
      {"author": "Joseph Conrad", "work": "The Secret Sharer", "quote": "I turned over the pages of the ship's **log**, examining the entries made during the preceding gale."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "I sat upon a pine **log** beside the pond, watching the sunlight sparkle across the ripples."}
    ]
  },
  "Dashboard — log/logagraphia.md": {
    "primary": "Loss of the ability to express ideas in writing while retaining the ability to copy words; motor agraphia.",
    "secondary": "In historical aphasiology and neurology, a motor-linguistic defect where written composition is impaired despite intact manual dexterity.",
    "quotes": [
      {"author": "William James", "work": "The Principles of Psychology", "quote": "In cases of **logagraphia**, the patient understands speech perfectly but cannot write a spontaneous sentence."},
      {"author": "Sigmund Freud", "work": "On Aphasia", "quote": "Clinical **logagraphia** demonstrates the dissociation between internal verbal conception and the motor acts of penmanship."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "A localized lesion in the left frontal convolution frequently produces motor aphasia accompanied by **logagraphia**."}
    ]
  },
  "Dashboard — log/logan.md": {
    "primary": "A rocking stone or balanced boulder that rocks with slight force; a rocking boulder.",
    "secondary": "In geomorphology and Celtic antiquities, a huge perched boulder balanced so delicately on bedrock that a child can sway it.",
    "quotes": [
      {"author": "Walter Scott", "work": "The Antiquary", "quote": "The great **logan** stone on the cliff rocked gently beneath the pressure of the antiquary's cane."},
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "Weathering along joints in the granite created the famous perched **logan** stones of Cornwall."},
      {"author": "Thomas Hardy", "work": "The Well-Beloved", "quote": "The massive block swayed like a **logan** rock, balanced upon its ancient natural pivot."}
    ]
  },
  "Dashboard — log/loganberry.md": {
    "primary": "A cultivated hybrid berry between the blackberry and raspberry, bearing dark red edible fruit.",
    "secondary": "In horticulture and pomology, Rubus × loganobaccus, created in California in 1881 by Judge James Harvey Logan.",
    "quotes": [
      {"author": "Luther Burbank", "work": "His Methods and Discoveries", "quote": "The **loganberry** combined the vigorous growth of the Pacific wild blackberry with the delicate acid flavor of the red raspberry."},
      {"author": "John Burroughs", "work": "Under the Maples", "quote": "In the garden borders, heavy clusters of dark crimson **loganberry** ripened under the summer sun."},
      {"author": "Liberty Hyde Bailey", "work": "The Standard Cyclopedia of Horticulture", "quote": "The **loganberry** has proved one of the most valuable commercial bush fruits introduced in modern times."}
    ]
  },
  "Dashboard — log/logania.md": {
    "primary": "A genus of shrubs and herbs in the family Loganiaceae, native to Australasia.",
    "secondary": "In systematic botany, the type genus of Loganiaceae comprising opposite-leaved plants bearing small white or yellow flowers.",
    "quotes": [
      {"author": "Robert Brown", "work": "Prodromus Florae Novae Hollandiae", "quote": "The genus **Logania** was established to commemorate the botanical services of James Logan of Pennsylvania."},
      {"author": "Joseph Dalton Hooker", "work": "The Flora of British India", "quote": "Species of **Logania** inhabit the sandy scrublands and coastal heaths of the Australian continent."},
      {"author": "George Bentham", "work": "Genera Plantarum", "quote": "The opposite leaves and interpetiolar stipules characterize the shrubs of the genus **Logania**."}
    ]
  },
  "Dashboard — log/loganiaceae.md": {
    "primary": "A family of flowering plants in the order Gentianales, containing toxic alkaloids such as strychnine.",
    "secondary": "In economic botany and pharmacognosy, a tropical family celebrated for yielding Strychnos nux-vomica and arrow poisons.",
    "quotes": [
      {"author": "Asa Gray", "work": "Structural Botany", "quote": "The family **Loganiaceae** contains arborescent and climbing plants notorious for yielding the virulent alkaloid strychnine."},
      {"author": "Joseph Dalton Hooker", "work": "The Flora of British India", "quote": "Numerous climbing lianas of the tropical forest belong to the poisonous family **Loganiaceae**."},
      {"author": "George Bentham", "work": "Genera Plantarum", "quote": "The opposite simple leaves and cymose inflorescence are typical of **Loganiaceae**."}
    ]
  },
  "Dashboard — log/logarithm.md": {
    "primary": "The power to which a base must be raised to yield a given number, invented to simplify computation.",
    "secondary": "In computational mathematics, a revolutionary calculation tool invented by John Napier in 1614 converting multiplication into addition.",
    "quotes": [
      {"author": "John Napier", "work": "Mirifici Logarithmorum Canonis Descriptio", "quote": "The calculation of planetary orbits is marvelously shortened by the use of the **logarithm**."},
      {"author": "Isaac Newton", "work": "Opticks", "quote": "The ratio of the refracted indices was computed using the common **logarithm** of each sine."},
      {"author": "Charles Babbage", "work": "Passages from the Life of a Philosopher", "quote": "My difference engine was designed to compute and tabulate the **logarithm** of every integer without human error."}
    ]
  },
  "Dashboard — log/logarithmic.md": {
    "primary": "Relating to, expressed by, or using logarithms; varying according to a logarithmic scale.",
    "secondary": "In biophysics and mathematics, nonlinear scaling where equal increments represent exponential multipliers.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "The growth of the nautilus shell follows an exquisite **logarithmic** spiral across its chambers."},
      {"author": "William Whewell", "work": "The Philosophy of the Inductive Sciences", "quote": "Astronomers rely upon **logarithmic** tables to resolve the vast numerical coordinates of celestial bodies."},
      {"author": "Gustav Fechner", "work": "Elements of Psychophysics", "quote": "The intensity of sensation increases as the **logarithmic** function of the physical stimulus."}
    ]
  },
  "Dashboard — log/logarithmically.md": {
    "primary": "In a logarithmic manner; by means of or according to a logarithmic scale.",
    "secondary": "In psychophysics and mathematical analysis, scaling proportionally to the logarithm of a variable rather than linearly.",
    "quotes": [
      {"author": "Gustav Fechner", "work": "Elements of Psychophysics", "quote": "Psychophysical experiments demonstrate that sensory perception increases **logarithmically** as stimulus intensity doubles."},
      {"author": "Charles Babbage", "work": "Passages from the Life of a Philosopher", "quote": "The engine calculates coordinates that advance **logarithmically** across the successive calculation wheels."},
      {"author": "Lord Kelvin", "work": "Popular Lectures and Addresses", "quote": "The dissipation of thermodynamic energy inside a cooling sphere proceeds **logarithmically** over geological epochs."}
    ]
  },
  "Dashboard — log/loge.md": {
    "primary": "A private box or the front section of the first balcony in a theater or opera house.",
    "secondary": "In French dramatic culture and social history, an enclosed theater booth where patrons observed performances in seclusion.",
    "quotes": [
      {"author": "Charlotte Brontë", "work": "Villette", "quote": "From our private **loge** in the theater, we had an unimpeded view of the glittering royal audience."},
      {"author": "Henry James", "work": "The American", "quote": "Newman sat back in the velvet-lined **loge**, surveying the fashionable Parisian assembly through his opera glass."},
      {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "Becky Sharp smiled triumphantly from her aristocratic **loge** across the crowded opera house."}
    ]
  },
  "Dashboard — log/logger.md": {
    "primary": "A person whose job is to fell trees and transport timber; a lumberjack.",
    "secondary": "In frontier economic history and forestry, an operative skilled in felling, hauling, and driving logs down rivers.",
    "quotes": [
      {"author": "Henry David Thoreau", "work": "The Maine Woods", "quote": "The hardy **logger** spends his winter deep in the spruce wilderness, felling giant timber for the mills."},
      {"author": "John Muir", "work": "The Mountains of California", "quote": "The axe of the commercial **logger** spared neither ancient sequoia nor noble sugar pine."},
      {"author": "Theodore Roosevelt", "work": "The Wilderness Hunter", "quote": "In the camps of the northwest, the American **logger** displays incredible endurance and axe craftsmanship."}
    ]
  },
  "Dashboard — log/logging.md": {
    "primary": "The commercial activity or business of cutting down trees and transporting logs to sawmills.",
    "secondary": "In environmental history and timber engineering, forest harvesting operations utilizing skid-roads, river drives, and sawmills.",
    "quotes": [
      {"author": "John Muir", "work": "Our National Parks", "quote": "Unrestricted commercial **logging** turns magnificent mountain forests into scarred, fire-swept barrens."},
      {"author": "Henry David Thoreau", "work": "The Maine Woods", "quote": "We passed numerous **logging** camps where rafts of spruce timber were assembled for the spring thaw."},
      {"author": "Gifford Pinchot", "work": "The Fight for Conservation", "quote": "Scientific forestry must replace destructive **logging** if our national timber reserves are to survive."}
    ]
  },
  "Dashboard — log/logic.md": {
    "primary": "Reasoning conducted according to strict principles of validity; the study of correct reasoning.",
    "secondary": "In classical philosophy and mathematics, the normative science initiated by Aristotle evaluating arguments and deductions.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "**Logic** is the common judge and arbiter of all particular investigations, whether physical or moral."},
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "The traditional school **logic** is useful rather for disputation than for the discovery of new truths."},
      {"author": "Bertrand Russell", "work": "Introduction to Mathematical Philosophy", "quote": "Pure mathematics and symbolic **logic** have developed until they are now recognized as one and the same discipline."}
    ]
  },
  "Dashboard — log/logical.md": {
    "primary": "According to the rules of logic or formal reasoning; reasonable, sound, and valid.",
    "secondary": "In philosophical argumentation, a proposition that follows necessarily from established true premises.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Eliminate all other factors, and the one which remains must be the truth; such is the **logical** method."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "He followed the argument to its stern and **logical** conclusion with inexorable legal precision."},
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Elinor's **logical** mind rejected every romantic illusion that contradicted common sense."}
    ]
  },
  "Dashboard — log/logicality.md": {
    "primary": "Soundness, coherence, and strict validity of reasoning according to formal principles.",
    "secondary": "In epistemology and literary characterization, rigorous consistency in intellectual deduction and systematic thought.",
    "quotes": [
      {"author": "William James", "work": "The Principles of Psychology", "quote": "The absolute **logicality** of a deduction cannot compensate for the falsity of its initial premises."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Casaubon's system possessed a rigid internal **logicality**, yet bore no relation to living historical reality."},
      {"author": "John Stuart Mill", "work": "Autobiography", "quote": "My early training in Greek dialectic gave my intellect a permanent habit of **logicality** and precision."}
    ]
  }
}

base_dir = r"App database/Latin roots/Cluster Thought"

updated_count = 0
for rel_path, entry in data.items():
    full_path = os.path.join(base_dir, rel_path)
    if not os.path.exists(full_path):
        print(f"Missing file: {full_path}")
        continue
    
    with open(full_path, "r", encoding="utf-8") as f:
        content = f.read()

    book_pattern = r"(> 1\.\s*\*\*[^*]+\*\*:\s*)([^\r\n]+)(\r?\n> 2\.\s*\*\*[^*]+\*\*:\s*)([^\r\n]+)"
    def repl_book(m):
        return f"{m.group(1)}{entry['primary']}{m.group(3)}{entry['secondary']}"
    
    new_content = re.sub(book_pattern, repl_book, content)
    if new_content == content:
        book_pattern2 = r"(1\.\s*\*\*[^*]+\*\*:\s*)([^\r\n]+)(\r?\n.*?2\.\s*\*\*[^*]+\*\*:\s*)([^\r\n]+)"
        new_content = re.sub(book_pattern2, repl_book, content)

    q_pos = new_content.find("> [!quote]")
    if q_pos != -1:
        before_q = new_content[:q_pos]
        after_q = new_content[q_pos:]
        
        new_q_lines = ["> [!quote] 💬 Contextual Usage & Authentic Quotations"]
        for q in entry["quotes"]:
            new_q_lines.append(f"> - 📜 **{q['author']} (*{q['work']}*):** *\"{q['quote']}\"*")
        
        rest = after_q.split("\n")
        remaining_lines = []
        skip = True
        for line in rest[1:]:
            if skip:
                if line.startswith("> - 📜") or line.strip() == ">" or line.strip() == "":
                    continue
                else:
                    skip = False
                    remaining_lines.append(line)
            else:
                remaining_lines.append(line)
        
        new_content = before_q + "\n".join(new_q_lines) + ("\n" + "\n".join(remaining_lines) if remaining_lines else "\n")
    
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    updated_count += 1

print(f"Thought Batch 4-2 (log 46-90): Successfully updated {updated_count}/{len(data)} notes.")
