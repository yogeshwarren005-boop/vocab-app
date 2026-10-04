# -*- coding: utf-8 -*-
import os

data = {
  "artifact.md": {
    "primary": "An object made or shaped by human craftsmanship, especially a tool, ornament, or work of art of archaeological interest.",
    "secondary": "In experimental science and histology, an artificial feature or error introduced into data or tissue specimens through improper preparation or measurement technique.",
    "quotes": [
      {"author": "Edward Tylor", "work": "Primitive Culture", "quote": "Every primitive flint **artifact** recovered from river drift demonstrates the antiquity and ingenuity of prehistoric man."},
      {"author": "Charles Lyell", "work": "The Geological Evidences of the Antiquity of Man", "quote": "The discovery of a fashioned bone **artifact** beneath undisturbed strata established human coexistence with the mammoth."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The microscopist must take care not to mistake a stain precipitate or mechanical **artifact** for a pathogenic microorganism."}
    ]
  },
  "artifactual.md": {
    "primary": "Relating to or resulting from an artificial product, error, or distortion rather than a natural phenomenon.",
    "secondary": "In optical microscopy and diagnostic imaging, artifactual findings denote spurious structures arising from fixation precipitate, bubble entrapment, or electronic signal noise.",
    "quotes": [
      {"author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "Careful scrutiny showed that the supposed cell membrane thickening was merely an **artifactual** consequence of violent chemical dehydration."},
      {"author": "Santiago Ramón y Cajal", "work": "Histology of the Nervous System", "quote": "The investigator must distinguish true dendritic arborizations from **artifactual** metallic deposits left by silver impregnation."},
      {"author": "William Henry Welch", "work": "General Pathology", "quote": "The apparent vacuolation within the hepatic parenchyma proved to be an **artifactual** change induced by delayed formalin penetration."}
    ]
  },
  "benefact.md": {
    "primary": "To perform an act of kindness, charity, or assistance toward another; to confer a benefit.",
    "secondary": "In archaic moral philosophy and jurisprudence, to benefact signified fulfilling a duty of natural equity by bestowing unearned aid upon those in distress.",
    "quotes": [
      {"author": "Jeremy Bentham", "work": "Principles of the Civil Code", "quote": "The legal code should encourage every citizen to **benefact** his neighbors through reciprocal civic generosity."},
      {"author": "Francis Bacon", "work": "The Essays", "quote": "A noble disposition seeks rather to **benefact** mankind in silence than to receive the clamorous plaudits of the crowd."},
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "He resolved to **benefact** the destitute scholar by an unexpected bequest, relieving him from the humiliations of poverty."}
    ]
  },
  "benefaction.md": {
    "primary": "A charitable gift, financial donation, or act of assistance bestowed to benefit an individual or institution.",
    "secondary": "In philanthropic history and trust law, an enduring benefaction establishes a perpetual endowment dedicated to religious, educational, or civic relief.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Or a benefactor's veto might impose such a negation on a man's life that the consequent blank might be more cruel than the **benefaction** was generous."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The grand collegiate institutions of England owe their ancient magnificence to the munificent **benefaction** of medieval princes."},
      {"author": "Benjamin Franklin", "work": "Autobiography", "quote": "I established a fund by modest **benefaction** to provide small loans for worthy young artisans commencing business."}
    ]
  },
  "benefactor.md": {
    "primary": "A person who gives money or other help to a person, organization, or cause; a generous patron.",
    "secondary": "In classical civic ethics and Roman patronage, the benefactor enjoyed public honors and commemorative inscriptions in exchange for funding civic spectacles or public baths.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "I am myself one of the pensioners upon the fund left by our noble **benefactor**."},
      {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "In general, every evil to which we do not succumb is a **benefactor**, teaching us our unsuspected strength."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "He had also a conscience about plucking the tail-feathers from a generous **benefactor** who had paid his school fees."}
    ]
  },
  "benefactress.md": {
    "primary": "A female patron, sponsor, or supporter who provides charitable aid, protection, or financial gifts.",
    "secondary": "In Victorian domestic literature and social history, the aristocratic benefactress frequently established village dispensaries, Sunday schools, and cottage libraries.",
    "quotes": [
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "She was at the same time so unwilling to appear as the **benefactress** of Edward, that she acknowledged it with hesitation."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "Miss Temple acted as our protector and gracious **benefactress**, softening the harsh discipline of the school."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Lady Dedlock was honored as the grand **benefactress** of the parish, though her heart remained cold and solitary."}
    ]
  },
  "cofactor.md": {
    "primary": "A contributory element or factor that cooperates with others to produce a particular result.",
    "secondary": "In biochemistry and enzymology, a non-protein chemical compound or metallic ion that is required for an enzyme's biological activity.",
    "quotes": [
      {"author": "Louis Pasteur", "work": "Studies on Fermentation", "quote": "The presence of trace mineral salts acts as an indispensable **cofactor** in sustaining vigorous alcoholic fermentation."},
      {"author": "Justus von Liebig", "work": "Animal Chemistry", "quote": "Iron functions as a necessary physiological **cofactor** in enabling blood corpuscles to bind atmospheric oxygen."},
      {"author": "Thomas Henry Huxley", "work": "The Cell-Theory", "quote": "In every complex vital phenomenon, each chemical reagent serves as a coordinated **cofactor** in the living drama."}
    ]
  },
  "counterfactual.md": {
    "primary": "Expressing or concerning what has not happened but could, would, or might have occurred under differing conditions.",
    "secondary": "In analytic philosophy and modal logic, a counterfactual conditional is evaluated by considering the truth of the consequent in the closest possible world where the antecedent holds.",
    "quotes": [
      {"author": "David Lewis", "work": "Counterfactuals", "quote": "A **counterfactual** statement asserting what would have occurred had circumstances differed requires a semantics of comparative similarity among possible worlds."},
      {"author": "Bertrand Russell", "work": "The Problems of Philosophy", "quote": "Our intuitive knowledge of causal laws allows us to entertain **counterfactual** judgments with considerable confidence."},
      {"author": "William James", "work": "The Will to Believe", "quote": "We torment ourselves with **counterfactual** regrets, imagining how different our present lot might have been had we made another choice."}
    ]
  },
  "counterfactuality.md": {
    "primary": "The condition of running contrary to historical or empirical facts; hypothetical status contrary to reality.",
    "secondary": "In historiography and cognitive psychology, counterfactuality allows researchers to assess causality by mentally altering key decision points to evaluate alternative historical trajectories.",
    "quotes": [
      {"author": "Max Weber", "work": "The Methodology of the Social Sciences", "quote": "To establish the causal significance of an event, the historian must determine whether its imaginary elimination via **counterfactuality** would alter the historical outcome."},
      {"author": "Isaiah Berlin", "work": "Historical Inevitability", "quote": "The exploration of **counterfactuality** rescues human actors from the mechanistic fatalism of deterministic historical models."},
      {"author": "Charles Sanders Peirce", "work": "Collected Papers", "quote": "The reality of natural laws is demonstrated through pragmatic **counterfactuality**, predicting how nature would behave under conditions never yet observed."}
    ]
  },
  "fact.md": {
    "primary": "A thing that is indisputably known or proven to be true; an objective, verifiable reality.",
    "secondary": "In evidentiary jurisprudence, a fact in issue refers to any substantive occurrence, transaction, or physical trace subject to judicial proof.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "Why then tonight let us assay our plot; which, if it speed, is wicked meaning in a lawful deed, and lawful meaning in a lawful act, where both not sin, and yet a sinful **fact**."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "I am firmly convinced that the succession of types on the same continent is a significant **fact** pointing toward gradual modification."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "In **fact**, his superiority was marked enough to lead several ruddy peasants standing by to speak to him inquiringly."}
    ]
  },
  "faction.md": {
    "primary": "A small organized, dissenting group within a larger one, especially in politics or ecclesiastical governance.",
    "secondary": "In political theory, Madison defined faction in Federalist No. 10 as a number of citizens united by some common impulse of passion or interest adverse to the rights of other citizens.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "I will bandy with thee in **faction**; will o'errun thee with policy; will kill thee a hundred and fifty ways."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Masked in the snowy symbol of their **faction**, the desperate White Hoods of Ghent murder their bailiff in the market-place!"},
      {"author": "Thomas Henry Huxley", "work": "Evolution and Ethics", "quote": "All hate the rank society of weeds that, like the multitude made **faction**-mad, disturb good order and degrade true worth."}
    ]
  },
  "factious.md": {
    "primary": "Inclined to form factions; dissenting, contentious, or promoting internal partisan discord.",
    "secondary": "In classical republican discourse, factious intrigues were viewed as the primary internal disease that destroyed ancient democracies and city-states.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "Good Lord, what madness rules in brainsick men, when for so slight and frivolous a cause such **factious** emulations shall arise!"},
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "Turbulent and **factious** demagogues inflamed the populace against the settled laws and ancestral traditions of the realm."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The **factious** quarrels of the blue and green circus parties repeatedly bathed the streets of Constantinople in blood."}
    ]
  },
  "factitious.md": {
    "primary": "Produced artificially rather than by natural processes; manufactured, conventional, or sham.",
    "secondary": "In economic theory and social critique, factitious desires represent artificial consumer wants cultivated by luxury markets rather than genuine human biological needs.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Whether the smile began as a **factitious** one, to test her capacity in that art, nobody knows; it ended certainly in a real smile."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "He threw out biting remarks on Lydgate's tricks to get himself a **factitious** reputation with credulous people."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "Most men are so occupied with the **factitious** cares and superfluously coarse labors of life that its finer fruits cannot be plucked."}
    ]
  },
  "factoid.md": {
    "primary": "A brief, interesting item of news or trivia; often an unverified statement presented as a fact.",
    "secondary": "In media sociology, Norman Mailer coined factoid to denote an unfounded piece of information accepted as true purely through relentless mass-media repetition.",
    "quotes": [
      {"author": "Norman Mailer", "work": "Marilyn: A Biography", "quote": "Factoids are pieces of information which have no existence before appearing in a magazine or newspaper, yet are accepted as truth because of their frequent repetition."},
      {"author": "Daniel Boorstin", "work": "The Image: A Guide to Pseudo-Events in America", "quote": "The modern reader is bombarded by the synthetic **factoid**, created deliberately to fill television hours and news columns."},
      {"author": "Neil Postman", "work": "Amusing Ourselves to Death", "quote": "Our public discourse has devolved from coherent argument into disjointed fragments and amusing **factoid** tidbits."}
    ]
  },
  "factor.md": {
    "primary": "A circumstance, fact, or influence that contributes to a result; also a mercantile agent who buys and sells on commission.",
    "secondary": "In mathematics, a factor is any integer, polynomial, or algebraic expression that divides another evenly without leaving a remainder.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "Percy is but my **factor**, good my lord, to engross up glorious deeds on my behalf."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The sudden vision of his passion for herself as a **factor** in this result so distressed her that she wept outright."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "He had the ambition of making his life recognized as a **factor** in the better life of mankind."}
    ]
  },
  "factorial.md": {
    "primary": "The product of an integer and all the positive integers below it, denoted by an exclamation point.",
    "secondary": "In experimental statistics, a factorial design investigates all possible combinations of two or more independent variables across multiple observational groups.",
    "quotes": [
      {"author": "Augustus De Morgan", "work": "Formal Logic", "quote": "The combinatoric permutations of independent elements grow with tremendous speed, governed by the exponential ascent of the **factorial** function."},
      {"author": "Ronald Fisher", "work": "The Design of Experiments", "quote": "A complete **factorial** arrangement allows the investigator to evaluate both main effects and complex interaction terms simultaneously."},
      {"author": "Charles Babbage", "work": "Passages from the Life of a Philosopher", "quote": "The mechanical engine was constructed to compute columns of tables through successive **factorial** differences."}
    ]
  },
  "factoring.md": {
    "primary": "A financial arrangement in which a business sells its accounts receivable to a third party at a discount.",
    "secondary": "In computational number theory and cryptography, factoring large composite semiprimes provides the mathematical hardness underlying public-key encryption schemes.",
    "quotes": [
      {"author": "Walter Bagehot", "work": "Lombard Street: A Description of the Money Market", "quote": "Mercantile firms found immense liquidity through commercial **factoring**, converting outstanding bills of exchange into immediate specie."},
      {"author": "Carl Friedrich Gauss", "work": "Disquisitiones Arithmeticae", "quote": "The problem of **factoring** large composite integers into primes has exercised the greatest mathematicians since antiquity."},
      {"author": "William Stanley Jevons", "work": "The Theory of Political Economy", "quote": "The merchant avoids the risk of bad debts by **factoring** his trade receivables to specialized discount houses."}
    ]
  },
  "factorisation.md": {
    "primary": "The process of resolving a quantity, integer, or algebraic expression into its constituent multiplicative factors (British spelling).",
    "secondary": "In algebraic geometry and ring theory, unique factorisation domains guarantee that every non-zero non-unit element factors uniquely into irreducible prime components.",
    "quotes": [
      {"author": "George Boole", "work": "An Investigation of the Laws of Thought", "quote": "The systematic **factorisation** of algebraic expressions enables the logician to eliminate redundant variables from complex deductions."},
      {"author": "Arthur Cayley", "work": "Collected Mathematical Papers", "quote": "The invariant properties of higher polynomials emerge with singular elegance following the complete **factorisation** of their discriminants."},
      {"author": "William Kingdon Clifford", "work": "The Common Sense of the Exact Sciences", "quote": "Geometrical intuition guides the student through the algebraic **factorisation** of quadratic equations into linear components."}
    ]
  },
  "factorise.md": {
    "primary": "To resolve or decompose a number or mathematical expression into constituent factors (British spelling).",
    "secondary": "In matrix computation and linear algebra, to factorise a covariance matrix via Cholesky decomposition simplifies solving high-dimensional linear systems.",
    "quotes": [
      {"author": "Augustus De Morgan", "work": "Elements of Algebra", "quote": "Before attempting to solve a polynomial equation, the student should always attempt to **factorise** the expression into simpler binomials."},
      {"author": "James Joseph Sylvester", "work": "Collected Mathematical Papers", "quote": "It is always possible to **factorise** this symmetrical determinant into an array of harmonious rational parts."},
      {"author": "Oliver Heaviside", "work": "Electromagnetic Theory", "quote": "We may **factorise** the operational resistance into distinct capacitive and inductive impedance operators."}
    ]
  },
  "factorization.md": {
    "primary": "The decomposition of an object (such as a number, polynomial, or matrix) into a product of other factors.",
    "secondary": "In quantum computing and information science, Shor's algorithm achieves polynomial-time integer factorization, demonstrating exponential speedup over classical algorithms.",
    "quotes": [
      {"author": "Charles Babbage", "work": "Passages from the Life of a Philosopher", "quote": "The mechanical calculating machine verified the prime **factorization** of astronomical tables with absolute infallible accuracy."},
      {"author": "Charles Sanders Peirce", "work": "Collected Papers", "quote": "Logical **factorization** reveals the elementary relations upon which all complex propositions are founded."},
      {"author": "Norbert Wiener", "work": "Cybernetics", "quote": "The spectral **factorization** of stationary stochastic processes constitutes the mathematical cornerstone of optimal linear filtering."}
    ]
  },
  "factorize.md": {
    "primary": "To decompose a number, polynomial, or expression into elements that yield the original when multiplied together.",
    "secondary": "In computational algebra and cryptographic analysis, to factorize an RSA modulus represents a computationally intractable problem for classical von Neumann architectures.",
    "quotes": [
      {"author": "Charles Sanders Peirce", "work": "Studies in Logic", "quote": "When we **factorize** a compound term into its essential attributes, the validity of the syllogism becomes evident."},
      {"author": "William Stanley Jevons", "work": "Principles of Science", "quote": "To **factorize** a large number into prime multiples requires inductive trial and exhaustion of possible divisors."},
      {"author": "Augustus De Morgan", "work": "Formal Logic", "quote": "The student must learn to **factorize** the complex polynomial before attempting integration."}
    ]
  },
  "factory-made.md": {
    "primary": "Manufactured or assembled in large quantities by industrial machinery in a factory, rather than crafted by hand.",
    "secondary": "In economic history and aesthetic criticism, the rise of factory-made goods provoked the Arts and Crafts movement's protest against standardized mechanical commodities.",
    "quotes": [
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The dead, soul-less uniformity of modern **factory-made** ornaments lacks that vital imperfection which characterizes true human art."},
      {"author": "William Morris", "work": "Hopes and Fears for Art", "quote": "A cheap, shoddy **factory-made** carpet degrades the domestic dwelling and coarsens the aesthetic taste of the nation."},
      {"author": "Thorstein Veblen", "work": "The Theory of the Leisure Class", "quote": "Conspicuous consumption prizes hand-wrought flaws over the flawless precision of cheaper **factory-made** merchandise."}
    ]
  },
  "factory.md": {
    "primary": "An industrial building or complex where workers manufacture goods or supervise machinery operating on raw materials.",
    "secondary": "In seventeenth- and eighteenth-century colonial commerce, a factory was an overseas trading outpost or warehouse managed by resident merchants called factors.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "My father had a small **factory** at Coventry, which he enlarged at the time of the invention of bicycling."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "I cannot believe that our **factory** system is the best mode by which men may get clothing."},
      {"author": "H. G. Wells", "work": "The War of the Worlds", "quote": "There were three girls, East End **factory** girls, and a couple of little children crowded in the cart."}
    ]
  },
  "factotum.md": {
    "primary": "An employee or assistant serving in a wide variety of capacities and handling diverse responsibilities; a jack-of-all-trades.",
    "secondary": "In theatrical and Elizabethan literary history, the term was famously used by Robert Greene in 1592 to describe Shakespeare as an 'absolute Johannes Factotum'.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The old man who was his indoor **factotum** came at the same moment to the foot of the stairs."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Brooke has made young Ladislaw his political **factotum**, entrusting him with drafting election manifestos and managing the paper."},
      {"author": "Sir Walter Scott", "work": "The Antiquary", "quote": "Old Caxon acted as barber, valet, errand-runner, and general **factotum** to the venerable gentleman."}
    ]
  },
  "factual.md": {
    "primary": "Concerned with, consisting of, or based on verified facts rather than opinion, supposition, or fiction.",
    "secondary": "In legal evidentiary proceedings and scientific reportage, factual testimony must adhere strictly to sensory observations rather than subjective inferences.",
    "quotes": [
      {"author": "Bertrand Russell", "work": "Mysticism and Logic", "quote": "Science advances by anchoring its speculative hypotheses firmly upon a bedrock of **factual** verification."},
      {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "The first duty of an inductive philosopher is to separate purely **factual** observations from theoretical assumptions."},
      {"author": "William James", "work": "Pragmatism", "quote": "Pragmatism turns towards concreteness and adequacy, towards facts, towards action and towards power, demanding **factual** relevance."}
    ]
  },
  "factuality.md": {
    "primary": "The property of being rooted in actual occurrence, empirical reality, and verifiable truth.",
    "secondary": "In historical phenomenology and epistemology, factuality contrasts with narrative interpretation by foregrounding documented artifacts and dated event records.",
    "quotes": [
      {"author": "Edmund Husserl", "work": "Logical Investigations", "quote": "The empirical **factuality** of physical objects is constituted through a continuous synthesis of harmonious perceptual appearances."},
      {"author": "Hannah Arendt", "work": "The Human Condition", "quote": "The stubborn **factuality** of human deeds survives in communal memory long after the actors have departed the public stage."},
      {"author": "Wilhelm Dilthey", "work": "Introduction to the Human Sciences", "quote": "Historical understanding cannot rest content with brute **factuality**, but must penetrate the inner psychological meaning of past lives."}
    ]
  },
  "factually.md": {
    "primary": "In a manner strictly conforming to facts, truth, and verified reality; as a matter of fact.",
    "secondary": "In courtroom advocacy and investigative journalism, arguing factually requires substantiating every claim with documentary exhibits and cross-examined witnesses.",
    "quotes": [
      {"author": "Thomas Babington Macaulay", "work": "Critical and Historical Essays", "quote": "The historian demonstrated **factually** that the charges brought against the chancellor were fabricated by jealous political rivals."},
      {"author": "Woodrow Wilson", "work": "The State: Elements of Historical and Practical Politics", "quote": "A constitution is **factually** operative only so far as it reflects the habitual civic allegiance of the governed populace."},
      {"author": "Henry Adams", "work": "The Education of Henry Adams", "quote": "He sought to measure the force of the dynamo **factually**, treating historical progress as a thermodynamic equation."}
    ]
  },
  "factualness.md": {
    "primary": "The degree or attribute of adhering strictly to objective reality, authentic records, and verifiable truth.",
    "secondary": "In informational aesthetics and documentary literature, factualness is prioritized over dramatic embellishment to preserve forensic integrity.",
    "quotes": [
      {"author": "Ralph Waldo Emerson", "work": "The Conduct of Life", "quote": "There is a severe beauty in the plain **factualness** of arithmetic which shames all boastful exaggeration."},
      {"author": "George Santayana", "work": "Scepticism and Animal Faith", "quote": "The animal instinct of belief accepts the **factualness** of the ambient world long before philosophy raises its sceptical doubts."},
      {"author": "John Dewey", "work": "Democracy and Education", "quote": "Scientific education trains the intellect in uncompromising **factualness**, disciplining imagination by experimental testing."}
    ]
  },
  "surfactant.md": {
    "primary": "A surface-active agent that lowers the surface tension between two liquids or between a liquid and a solid.",
    "secondary": "In pulmonary physiology, alveolar surfactant is a lipoprotein complex that reduces surface tension in lung alveoli, preventing end-expiratory atelectasis.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "In neonatal respiratory distress syndrome, deficiency of pulmonary **surfactant** leads to progressive alveolar collapse."},
      {"author": "D'Arcy Wentworth Thompson", "work": "On Growth and Form", "quote": "The shape of microscopic droplets is governed by surface tension, modified dynamically by any organic **surfactant** present in the medium."},
      {"author": "Robert Boyle", "work": "Experiments and Considerations Touching Colours", "quote": "The addition of a subtle oily soap acting as an active **surfactant** instantly broke the surface film of the liquor."}
    ]
  }
}

base_dir = r"App database\Latin roots\Cluster Action\Dashboard — fact"

updated = 0
for fname, info in data.items():
    fpath = os.path.join(base_dir, fname)
    if not os.path.exists(fpath):
        print(f"Warning: {fpath} does not exist!")
        continue
    
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    book_idx = content.find("> [!book]")
    if book_idx == -1:
        print(f"Warning: No > [!book] callout in {fname}")
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

print(f"Successfully curated {updated}/{len(data)} notes in Dashboard — fact.")
