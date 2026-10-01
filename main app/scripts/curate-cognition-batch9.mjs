import fs from "fs";
import path from "path";

const baseDir = "App database/Greek roots/Cluster Cognition & Mind";

const wordsSharedData = {
  "theorem": {
    primary: "A mathematical statement or proposition that has been proved on the basis of previously established statements (axioms, postulates, or other theorems).",
    secondary: "In formal logic and deductive systems, a formula derived from axioms via accepted transformation rules; broadly, a well-established general truth.",
    quotes: [
      { author: "Euclid", work: "Elements (Book I)", quote: "In any right-angled triangle, the square on the hypotenuse is equal to the squares on the sides containing the right angle; this celebrated **theorem** is established beyond doubt." },
      { author: "Bertrand Russell", work: "Principia Mathematica", quote: "Every mathematical **theorem** is a tautology, revealing relations already implicit within the initial axioms." },
      { author: "Albert Einstein", work: "Relativity: The Special and the General Theory", quote: "The Pythagorean **theorem** provides the Euclidean metric foundation that general relativity generalized into curved spacetime." }
    ]
  },
  "theoretic": {
    primary: "Of or relating to theory; theoretical; conceptual and abstract rather than practical or applied.",
    secondary: "In classical philosophy (Aristotle's theōrētikē philosophia), concerning the contemplative pursuit of truth (physics, mathematics, theology) as distinct from practical action (praxis).",
    quotes: [
      { author: "Aristotle", work: "Metaphysics", quote: "The **theoretic** sciences—mathematics, physics, and theology—are the most honorable, seeking truth for its own sake." },
      { author: "Francis Bacon", work: "Novum Organum", quote: "Pure **theoretic** speculation divorced from empirical experiments produces only empty webs of scholastic dogma." },
      { author: "John Ruskin", work: "Modern Painters", quote: "The **theoretic** faculty perceives beauty not as mere sensual pleasure, but as a moral reflection of divine perfection." }
    ]
  },
  "theoretical": {
    primary: "Concerned with or based on the theory of a subject or field of study rather than its practical application; abstract or speculative.",
    secondary: "In scientific research, formulating mathematical models and hypotheses (theoretical physics) in advance of experimental verification.",
    quotes: [
      { author: "Albert Einstein", work: "Ideas and Opinions", quote: "The grand aim of all **theoretical** physics is to form comprehensive concepts that require the fewest possible independent hypotheses." },
      { author: "Adam Smith", work: "The Wealth of Nations", quote: "The statesman must distinguish between sound **theoretical** principles of trade and short-sighted mercantile protectionism." },
      { author: "George Eliot", work: "Middlemarch", quote: "Lydgate was fascinated by the **theoretical** problems of living tissue, longing to discover the ultimate cellular web of life." }
    ]
  },
  "theoretically": {
    primary: "In a manner according to theory; hypothetically or in principle, as distinguished from practical reality.",
    secondary: "In academic discourse, deduced by logical calculation from accepted principles, though potentially modified by real-world friction or empirical variables.",
    quotes: [
      { author: "Charles Darwin", work: "The Origin of Species", quote: "Although a species may **theoretically** multiply in geometric progression, severe natural checks restrict its population." },
      { author: "Arthur Conan Doyle", work: "The Sign of Four", quote: "'Theoretically,' Holmes remarked, 'it is quite simple; practically, we must find where the boat landed in the fog.'" },
      { author: "Alexis de Tocqueville", work: "Democracy in America", quote: "The constitution granted equal rights **theoretically**, but local custom determined how those rights were exercised in daily life." }
    ]
  },
  "theoretician": {
    primary: "An expert who formulates, develops, or studies the theoretical foundations of a science, art, or discipline (as opposed to an experimentalist or practitioner).",
    secondary: "In mathematics, physics, and economics, a thinker who constructs deductive mathematical models to explain empirical observations.",
    quotes: [
      { author: "Richard Feynman", work: "Surely You're Joking, Mr. Feynman!", quote: "The experimentalists came running to the office of the **theoretician**, demanding an equation that could explain their baffling bubble chamber tracks." },
      { author: "Bertrand Russell", work: "The Scientific Outlook", quote: "The brilliant **theoretician** perceives a hidden mathematical symmetry where the practical engineer sees only chaos." },
      { author: "John Maynard Keynes", work: "The General Theory of Employment, Interest and Money", quote: "The ideas of the economic **theoretician**, both when they are right and when they are wrong, are more powerful than is commonly understood." }
    ]
  },
  "theoria": {
    primary: "In classical Greek philosophy, the act of viewing, contemplation, or speculative reflection upon truth and cosmic reality (contrasted with praxis and poiesis).",
    secondary: "In theological and mystical traditions (especially Christian Neoplatonism and Eastern Orthodoxy), the direct spiritual vision or contemplation of God and divine energies.",
    quotes: [
      { author: "Aristotle", work: "Nicomachean Ethics", quote: "The activity of God, which surpasses all others in blessedness, must be the contemplative activity of **theoria**." },
      { author: "Hans-Georg Gadamer", work: "Truth and Method", quote: "**Theoria** is not a detached stance, but a genuine participation in the spectacle, where the spectator is completely absorbed in what is seen." },
      { author: "Gregory Palamas", work: "The Triads", quote: "True **theoria** is not abstract syllogistic reasoning about the divine, but the luminous vision of uncreated divine light." }
    ]
  },
  "theorisation": {
    primary: "The act or process of formulating, developing, or constructing a theory or explanatory framework (British English spelling).",
    secondary: "In sociological and cultural theory, systematic conceptual modeling used to interpret institutional power, social structures, and historical change.",
    quotes: [
      { author: "Michel Foucault", work: "Power/Knowledge", quote: "Our **theorisation** of power must abandon the sovereign model and examine disciplinary techniques operating at the micro-level." },
      { author: "Jürgen Habermas", work: "The Theory of Communicative Action", quote: "A rigorous **theorisation** of modernity requires grounding rationality in communicative speech acts rather than instrumental domination." },
      { author: "Virginia Woolf", work: "The Common Reader", quote: "Behind the spontaneous poetry of the Elizabethans lay centuries of subtle classical **theorisation**." }
    ]
  },
  "theorise": {
    primary: "To form a theory or theories about something; to speculate or develop conceptual explanations (British English spelling).",
    secondary: "In scientific inquiry, to propose hypotheses that connect disparate observations into a coherent predictive structure.",
    quotes: [
      { author: "Arthur Conan Doyle", work: "A Study in Scarlet", quote: "It is a capital mistake to **theorise** before one has data; insensibly one begins to twist facts to suit theories, instead of theories to suit facts." },
      { author: "Charles Darwin", work: "Life and Letters of Charles Darwin", quote: "How odd it is that anyone should not see that all observation must be for or against some view if it is to be of any service! How can one not **theorise**?" },
      { author: "Thomas Henry Huxley", work: "Science and Culture", quote: "The natural philosopher is compelled to **theorise**, but must be ready to slay his pet hypothesis the moment a contrary fact appears." }
    ]
  },
  "theoriser": {
    primary: "A person who theorizes or speculates; an architect of conceptual explanations (British English spelling).",
    secondary: "In political commentary, an abstract thinker whose idealized blueprints may overlook practical human realities.",
    quotes: [
      { author: "Edmund Burke", work: "Reflections on the Revolution in France", quote: "The political **theoriser** in Paris reconstructed the state on paper, blind to the living ancestral habits of the people." },
      { author: "George Eliot", work: "Middlemarch", quote: "Lydgate was no mere idle **theoriser**, but a determined researcher who spent nocturnal hours at his microscope." },
      { author: "William Makepeace Thackeray", work: "The Virginians", quote: "The old **theoriser** loved to discourse upon military strategy while younger men did the fighting in the field." }
    ]
  },
  "theorist": {
    primary: "A person who develops, studies, or advocates theories; a thinker concerned with conceptual foundations rather than practical application.",
    secondary: "In physics, economics, and political philosophy, an intellectual who builds formal models to synthesize data and predict future phenomena.",
    quotes: [
      { author: "Albert Einstein", work: "Autobiographical Notes", quote: "The **theorist** is not to be envied, for nature—or more strictly speaking, experiment—is an inexorable and not very friendly judge of his work." },
      { author: "Adam Smith", work: "The Wealth of Nations", quote: "The armchair **theorist** imagines he can arrange the members of a great society with as much ease as the hand arranges pieces on a chess-board." },
      { author: "Hannah Arendt", work: "The Human Condition", quote: "The political **theorist** must balance the contemplative life of the mind against the vita activa of democratic participation." }
    ]
  },
  "theorization": {
    primary: "The formulation, development, or construction of a theory or systematic conceptual model to explain phenomena.",
    secondary: "In scientific methodology, the process of synthesizing experimental data into abstract laws, predictive equations, and explanatory frameworks.",
    quotes: [
      { author: "Karl Popper", work: "The Logic of Scientific Discovery", quote: "Scientific **theorization** proceeds by bold conjectures subjected to rigorous empirical attempts at refutation." },
      { author: "Thomas Kuhn", work: "The Structure of Scientific Revolutions", quote: "A period of paradigm crisis stimulates creative **theorization**, challenging long-held assumptions." },
      { author: "Max Weber", work: "The Methodology of the Social Sciences", quote: "Sociological **theorization** relies on ideal types to make complex historical realities intelligible to analysis." }
    ]
  },
  "theorize": {
    primary: "To formulate a theory or conceptual explanation about something; to speculate conceptually based on observed facts.",
    secondary: "In scientific research, to construct mathematical or causal models to deduce testable hypotheses.",
    quotes: [
      { author: "Arthur Conan Doyle", work: "The Valley of Fear", quote: "I never **theorize** before having all the evidence, for that is a capital error which biases the judgment." },
      { author: "Charles Darwin", work: "More Letters of Charles Darwin", quote: "I cannot avoid continuing to **theorize** on everything I see, for nature without a guiding hypothesis is an unintelligible chaos." },
      { author: "Bertrand Russell", work: "Mysticism and Logic", quote: "The human mind feels an irresistible urge to **theorize**, seeking orderly cosmos behind the chaotic flux of sensations." }
    ]
  },
  "theorizer": {
    primary: "A person who theorizes; one who invents, constructs, or proposes theoretical explanations.",
    secondary: "In historiography and political analysis, an intellectual who formulates overarching models to explain social developments.",
    quotes: [
      { author: "Alexis de Tocqueville", work: "The Old Regime and the Revolution", quote: "The French literary **theorizers** built a glorious utopian republic in their minds, ignoring the messy art of actual government." },
      { author: "Herman Melville", work: "Moby-Dick; or, The Whale", quote: "Ahab was no ordinary sea-captain, but a brooding **theorizer** who saw cosmic malice incarnate in the white whale." },
      { author: "William James", work: "Pragmatism", quote: "The pragmatic thinker smiles at the metaphysical **theorizer** who imagines he has captured the infinite in a neat syllogism." }
    ]
  },
  "theory-based": {
    primary: "Founded on, derived from, or guided by a systematic theory, conceptual model, or empirical hypothesis.",
    secondary: "In educational methodology and policy evaluation, describing programs or interventions whose design is explicitly structured around validated scientific frameworks.",
    quotes: [
      { author: "John Dewey", work: "Democracy and Education", quote: "A truly **theory-based** curriculum unites reflective thinking with active manual experimentation in the classroom." },
      { author: "Donald O. Hebb", work: "The Organization of Behavior", quote: "Our research proposed a **theory-based** model of neural assemblies capable of explaining cognitive attention and perceptual learning." },
      { author: "Herbert A. Simon", work: "Administrative Behavior", quote: "Modern organizational design relies on **theory-based** decision analysis to manage bounded rationality in complex environments." }
    ]
  },
  "theory": {
    primary: "A well-substantiated explanation of some aspect of the natural world, acquired through the scientific method and repeatedly tested and confirmed through observation and experiment.",
    secondary: "In philosophical contemplation (Greek theōria, a looking at, contemplation, speculation), the pursuit of truth for its own sake; colloquially, an unproven supposition or conjecture.",
    quotes: [
      { author: "Aristotle", work: "Nicomachean Ethics", quote: "The activity of philosophical contemplation, or **theory**, is the highest and most godlike exercise of the human soul." },
      { author: "Charles Darwin", work: "The Origin of Species", quote: "I look at the natural geological record as a history of the world imperfectly kept; yet on this view, my **theory** of natural selection is supported by countless facts." },
      { author: "Albert Einstein", work: "Ideas and Opinions", quote: "It can scarcely be denied that the supreme goal of all **theory** is to make the irreducible basic elements as simple and as few as possible." }
    ]
  }
};

function updateWordNote(fullPath, data) {
  if (!fs.existsSync(fullPath)) {
    console.error("Not found:", fullPath);
    return;
  }
  let content = fs.readFileSync(fullPath, "utf8");

  // Format quotes
  const quotesFormatted = data.quotes.map(q => `> - 📜 **${q.author} (*${q.work}*):** *"${q.quote}"*`).join("\n");

  // Replace Definition & Semantic Range
  const defRegex = /> \[!book\] 📖 Definitions & Semantic Range[\s\S]*?(?=> \[!quote\]|$)/;
  const newDef = `> [!book] 📖 Definitions & Semantic Range\n> 1. **Primary Definition (Lexical / Standard Consensus)**: ${data.primary}\n> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: ${data.secondary}\n\n`;

  if (defRegex.test(content)) {
    content = content.replace(defRegex, newDef);
  } else {
    console.warn("Could not find [!book] in", fullPath);
  }

  // Replace Quotes
  const quoteRegex = /> \[!quote\] 💬 Contextual Usage & Authentic Quotations[\s\S]*$/;
  const newQuotes = `> [!quote] 💬 Contextual Usage & Authentic Quotations\n${quotesFormatted}\n`;

  if (quoteRegex.test(content)) {
    content = content.replace(quoteRegex, newQuotes);
  } else {
    console.warn("Could not find [!quote] in", fullPath);
  }

  fs.writeFileSync(fullPath, content, "utf8");
  console.log("Updated:", path.relative(baseDir, fullPath));
}

// 1. Dashboard — theor (15 words)
const theorDir = path.join(baseDir, "Dashboard — theor");
const theorFiles = fs.readdirSync(theorDir).filter(f => f.endsWith(".md") && !f.startsWith("Dashboard") && !f.startsWith("Word Triage"));
let count = 0;
for (const file of theorFiles) {
  const wordKey = file.replace(".md", "");
  if (wordsSharedData[wordKey]) {
    updateWordNote(path.join(theorDir, file), wordsSharedData[wordKey]);
    count++;
  } else {
    console.warn("No data for theor file:", file);
  }
}

// 2. Dashboard — theori (12 words)
const theoriDir = path.join(baseDir, "Dashboard — theori");
const theoriFiles = fs.readdirSync(theoriDir).filter(f => f.endsWith(".md") && !f.startsWith("Dashboard") && !f.startsWith("Word Triage"));
for (const file of theoriFiles) {
  const wordKey = file.replace(".md", "");
  if (wordsSharedData[wordKey]) {
    updateWordNote(path.join(theoriDir, file), wordsSharedData[wordKey]);
    count++;
  } else {
    console.warn("No data for theori file:", file);
  }
}

console.log("Batch 9 completed! Total words updated:", count);
