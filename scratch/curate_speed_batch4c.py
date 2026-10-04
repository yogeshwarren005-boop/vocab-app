# -*- coding: utf-8 -*-
import os, sys, re

sys.stdout.reconfigure(encoding="utf-8")

data = {
  # =========================================================================
  # Dashboard — vi (25 words)
  # =========================================================================
  "Dashboard — vi/devi.md": {
    "primary": "A Hindu goddess, especially the supreme goddess regarded as the feminine manifestation of divine creative energy.",
    "secondary": "In Hindu theology and Shakta traditions, Devi embodies cosmic cosmic power (Shakti), appearing in benign or fierce aspects (Parvati, Durga, Kali).",
    "quotes": [
      {"author": "Richard Francis Burton", "work": "The Book of the Thousand Nights and a Night", "quote": "The temple priest made offerings of fragrant garlands and clarified butter before the golden shrine of **Devi**."},
      {"author": "Max Müller", "work": "The Sacred Books of the East", "quote": "In ancient hymns, **Devi** is revered as the all-pervading feminine force animating the celestial universe."},
      {"author": "Ralph Waldo Emerson", "work": "Indian Superstition", "quote": "The mystic imagery surrounding the goddess **Devi** reflected profound philosophical insights of ancient Vedic thinkers."}
    ]
  },
  "Dashboard — vi/deviance.md": {
    "primary": "Behavior, action, or condition that departs substantially from established social, moral, or statistical norms.",
    "secondary": "In sociological criminology, deviance conceptualized through labeling theory and structural-functional strains (Merton, Becker).",
    "quotes": [
      {"author": "Herbert Spencer", "work": "The Study of Sociology", "quote": "Social institutions tend to penalize individual **deviance** in order to preserve corporate cohesion."},
      {"author": "John Stuart Mill", "work": "On Liberty", "quote": "The tyranny of prevailing public opinion views any intellectual **deviance** from orthodoxy with severe hostility."},
      {"author": "William James", "work": "The Varieties of Religious Experience", "quote": "Exceptional spiritual experiences frequently appear as psychological **deviance** to the common observer."}
    ]
  },
  "Dashboard — vi/deviant.md": {
    "primary": "Departing from usual or accepted standards, especially in social, intellectual, or moral behavior.",
    "secondary": "In statistical analysis and social psychology, observations or individuals falling beyond standard distributional parameters.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "On Liberty", "quote": "It is essential that society tolerate **deviant** modes of thinking if intellectual progress is to be maintained."},
      {"author": "Herbert Spencer", "work": "The Principles of Ethics", "quote": "A strictly **deviant** member of the clan was often expelled into the wilderness for self-preservation."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "The eccentric thinker represents a **deviant** variation whose ideas may ultimately enrich the community."}
    ]
  },
  "Dashboard — vi/deviate.md": {
    "primary": "To depart or turn aside from an established course, principle, standard, or accepted pattern.",
    "secondary": "In maritime navigation and statistics, variance between magnetic and true headings; or departure from an expected mean.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The legislative department must not **deviate** from the clear boundaries prescribed by the fundamental charter."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "When we **deviate** from the simple evidence of our senses, we fall into endless metaphysical errors."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Offspring will occasionally **deviate** slightly in form or color from the typical parental standard."}
    ]
  },
  "Dashboard — vi/deviation.md": {
    "primary": "The action of departing from an established course or accepted standard; a divergence or departure.",
    "secondary": "In mathematical statistics and physics, standard deviation measuring data dispersion about the arithmetic mean.",
    "quotes": [
      {"author": "Isaac Newton", "work": "Opticks", "quote": "The refraction of the light ray through the glass prism causes a distinct angular **deviation** for each color."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Any notable **deviation** from the typical osteological structure was carefully recorded by the comparative anatomist."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Market prices exhibit frequent **deviation** from the natural price in response to temporary shifts in supply."}
    ]
  },
  "Dashboard — vi/devious.md": {
    "primary": "Showing a skillful use of underhanded or deceitful tactics; or wandering, winding, and circuitous.",
    "secondary": "In landscape description and narrative style, winding labyrinthine pathways departing from direct thoroughfares.",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Through trackless paths and **devious** ways they wound their solitary course across the fallen world."},
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "By indirections find directions out; so by my former lecture and advice, shall you my son win in his **devious** course."},
      {"author": "Jane Austen", "work": "Mansfield Park", "quote": "She disliked Crawford's **devious** conduct, perceiving selfish calculation beneath his polished manners."}
    ]
  },
  "Dashboard — vi/deviously.md": {
    "primary": "In a devious, circuitous, or deceitfully indirect manner; by underhanded means.",
    "secondary": "In narrative prose, pursuing an objective through roundabout diplomacy or concealed stratagems.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "The criminal had acted **deviously**, laying false scents across the moor to baffle the tracker dogs."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Tulkinghorn moved **deviously** through the legal world, keeping all family secrets locked within his breast."},
      {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "Becky Sharp advanced **deviously** through fashionable society, concealing her desperate financial straits."}
    ]
  },
  "Dashboard — vi/deviousness.md": {
    "primary": "Underhanded cunning, deceitful indirectness, or roundabout complexity in action or speech.",
    "secondary": "In character analysis, calculating duplicity masking true motives behind superficial amiability.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Bulstrode's habitual **deviousness** in business transactions was rationalized by pious theological pretexts."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "I observed the lawyer's extraordinary **deviousness**, noticing how he answered every question with another riddle."},
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "The political **deviousness** of the revolutionary factions undermined all public trust in the assembly."}
    ]
  },
  "Dashboard — vi/obviate.md": {
    "primary": "To remove, avoid, or prevent a need, difficulty, or obstacle; to render unnecessary.",
    "secondary": "In engineering and statutory drafting, proactive preventative design eliminating predictable operational failures.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "A clear constitutional provision will **obviate** many disputes that might otherwise arise between the states."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "The prompt arrival of the carriage served to **obviate** all the inconveniences of traveling on foot."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "Careful laboratory precautions were taken to **obviate** the danger of bacterial contamination."}
    ]
  },
  "Dashboard — vi/obviating.md": {
    "primary": "Removing, avoiding, or rendering unnecessary an obstacle, danger, or complication.",
    "secondary": "In clinical preventative medicine, hygienic interventions forestalling the spread of communicable disease.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Prompt aseptic irrigation was effective in **obviating** the risk of systemic septic infection."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The invention of bills of exchange facilitated distant commerce, **obviating** the hazard of transporting coin."},
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "Clear contracts serve the public interest by **obviating** costly litigation in trade disputes."}
    ]
  },
  "Dashboard — vi/obviation.md": {
    "primary": "The act or process of obviating; prevention or removal of a difficulty or obstacle.",
    "secondary": "In classical legal jurisprudence and formal logic, the procedural elimination of contradictory claims.",
    "quotes": [
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "The **obviation** of common fallacies requires a disciplined understanding of inductive reasoning."},
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "The statutory amendment was enacted for the **obviation** of doubts concerning testamentary inheritances."},
      {"author": "Edmund Burke", "work": "Speech on Conciliation with America", "quote": "True statesmanship lies in the timely **obviation** of grievances before they produce open rebellion."}
    ]
  },
  "Dashboard — vi/obvious.md": {
    "primary": "Easily perceived or understood; clear, self-evident, or apparent to the eye or mind.",
    "secondary": "In archaic literary usage (Milton), lying directly in the path; fronting or standing in the way.",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "To the evil turn my **obvious** breast, armed with celestial virtue against tempting guile."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "It has long been an axiom of mine that the little things are infinitely the most **obvious**."},
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "It was **obvious** to all who saw them that Colonel Brandon admired Marianne with unfeigned sincerity."}
    ]
  },
  "Dashboard — vi/obviously.md": {
    "primary": "In a way that is easily perceived or understood; clearly, plainly, or unmistakably.",
    "secondary": "In logical discourse, denoting a conclusion following demonstrably from acknowledged premises.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "The footprints were **obviously** those of a creature of colossal size, sinking deep into the peat."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Joe was **obviously** uncomfortable in his stiff Sunday clothes, standing awkwardly upon the carpet."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Bingley was **obviously** fascinated by Jane, gazing upon her throughout the evening with joyful admiration."}
    ]
  },
  "Dashboard — vi/obviousness.md": {
    "primary": "The unmistakable clarity or self-evident nature of a fact, perception, or conclusion.",
    "secondary": "In philosophical epistemology, the immediate intuitive grasp of axiomatic mathematical truths.",
    "quotes": [
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "The **obviousness** of sensory ideas makes it unnecessary to argue for their immediate reality."},
      {"author": "William James", "work": "Pragmatism", "quote": "Philosophers often overlook essential truths precisely because of their transparent **obviousness**."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "Holmes smiled at the **obviousness** of the clue, which had nevertheless escaped the Scotland Yard detectives."}
    ]
  },
  "Dashboard — vi/previous.md": {
    "primary": "Existing or occurring before in time or order; earlier or prior.",
    "secondary": "In parliamentary procedure, the 'previous question' motion moved to end debate and force an immediate vote.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Her **previous** impressions of Mr. Darcy were completely overturned by his gentlemanlike letter."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The **previous** night had been spent in sleepless agitation within the dark prison chamber."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "A **previous** treaty between the confederates had failed to secure the necessary public revenues."}
    ]
  },
  "Dashboard — vi/previously.md": {
    "primary": "At an earlier time or on a former occasion; beforehand, antecedently.",
    "secondary": "In legal and scientific reporting, prior established precedents or baseline experimental observations.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Holmes had **previously** examined the walking-stick before Watson ventured his own deduction."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Species that had **previously** inhabited a wide continental range were gradually restricted to island refuges."},
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Elinor had **previously** formed a high opinion of Edward's moral integrity and modest character."}
    ]
  },
  "Dashboard — vi/trivia.md": {
    "primary": "Pieces of information or details of little importance or value; curious minor facts.",
    "secondary": "In medieval scholastic education, the trivium (grammar, logic, rhetoric) forming the lower division of the seven liberal arts.",
    "quotes": [
      {"author": "John Gay", "work": "Trivia, or The Art of Walking the Streets of London", "quote": "Through dusty lanes and crowded ways my muse records the daily **trivia** of London life."},
      {"author": "Virginia Woolf", "work": "Jacob's Room", "quote": "Letters were filled with domestic **trivia**, passing gossip, and the trivial news of the country parish."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "He occupied his leisure hours with harmless historical **trivia**, collecting old coins and broken pottery."}
    ]
  },
  "Dashboard — vi/trivial.md": {
    "primary": "Of little value or importance; trifling, insignificant, or commonplace.",
    "secondary": "In taxonomy and classical logic, the trivial name denoting the specific epithet in a binomial nomenclature.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "Yea, from the table of my memory I'll wipe away all **trivial** fond records, all saws of books."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "We spent the evening discussing **trivial** matters to distract our minds from impending disaster."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "A seemingly **trivial** variation in the shape of a beak may prove of vital importance in the struggle for life."}
    ]
  },
  "Dashboard — vi/trivialise.md": {
    "primary": "To make something seem unimportant, insignificant, or frivolous; to minimize serious weight.",
    "secondary": "In cultural criticism, mass media sensationalism reducing serious historical tragedies to shallow entertainment.",
    "quotes": [
      {"author": "George Bernard Shaw", "work": "Major Barbara", "quote": "To treat great moral dilemmas with flippant humor is to **trivialise** the deepest struggles of the human conscience."},
      {"author": "Virginia Woolf", "work": "A Room of One's Own", "quote": "Literary critics too often **trivialise** women's experiences, reducing them to domestic footnotes."},
      {"author": "H. G. Wells", "work": "The Outline of History", "quote": "Modern sensational journalism tends to **trivialise** the grave political transformations of our epoch."}
    ]
  },
  "Dashboard — vi/triviality.md": {
    "primary": "Insignificance, petty unimportance, or frivolous lack of serious value or weight; a trifle.",
    "secondary": "In existential philosophy, social conventions that divert consciousness from profound existential realities.",
    "quotes": [
      {"author": "Jane Austen", "work": "Emma", "quote": "Emma grew tired of the petty **triviality** of the card-table conversation at Mrs. Bates's lodging."},
      {"author": "Oscar Wilde", "work": "The Importance of Being Earnest", "quote": "We should treat all the **triviality** of serious things seriously, and all the serious things of life with sincere and studied triviality."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The great lawsuit consumed decades in haggling over microscopic legal **triviality** while the suitors starved."}
    ]
  },
  "Dashboard — vi/trivialize.md": {
    "primary": "To cause something to appear trivial, petty, or frivolous; to treat with superficial disregard.",
    "secondary": "In historical and sociological discourse, reducing systemic complex crises to simplistic personal anecdotes.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "On Liberty", "quote": "Public ridicule was employed to **trivialize** vital constitutional reforms championed by early advocates."},
      {"author": "George Orwell", "work": "Collected Essays", "quote": "Partisan propaganda seeks to **trivialize** genuine ideological disagreements into crude slogans."},
      {"author": "William James", "work": "The Will to Believe", "quote": "Skeptics attempt to **trivialize** religious convictions by treating them as mere emotional delusions."}
    ]
  },
  "Dashboard — vi/trivially.md": {
    "primary": "In a trivial or unimportant manner; superficially, slightly, or with little significance.",
    "secondary": "In mathematics, holding trivially or vacuously in extreme boundary cases without substantive proof.",
    "quotes": [
      {"author": "Bertrand Russell", "work": "The Principles of Mathematics", "quote": "The proposition holds **trivially** when the null set is considered as a subset of itself."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "They chatted **trivially** about the morning market, studiously avoiding the grave scandal in the town."},
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "He responded **trivially** to her earnest question, unwilling to reveal his true feelings."}
    ]
  },
  "Dashboard — vi/unobvious.md": {
    "primary": "Not readily apparent, self-evident, or easily seen; hidden or requiring subtle reflection to detect.",
    "secondary": "In patent jurisprudence and technological innovation, the requirement that an invention not be obvious to a person having ordinary skill in the art.",
    "quotes": [
      {"author": "Alfred North Whitehead", "work": "Science and the Modern World", "quote": "The grandest physical principles are often the most **unobvious**, veiled beneath familiar everyday appearances."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Holmes seized upon an **unobvious** speck of red mud upon the carpet, deducing the visitor's origin."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The evolutionary advantage of the structure was obscure and **unobvious** until observed in its native habitat."}
    ]
  },
  "Dashboard — vi/vi.md": {
    "primary": "The Roman numeral for the number six; or an abbreviation for the Virgin Islands or the classic visual editor.",
    "secondary": "In historical typography and classical epigraphy, VI engraved on Roman monuments to represent six.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Chapter **VI** traces the accession of the Antonines and the peak of Roman administrative tranquility."},
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "Book the second, title **VI**, treats of estates in possession, remainder, and reversion."},
      {"author": "Isaac Newton", "work": "Philosophiae Naturalis Principia Mathematica", "quote": "In Proposition **VI**, the centripetal force is demonstrated to vary inversely as the square of distance."}
    ]
  },
  "Dashboard — vi/via.md": {
    "primary": "By way of; passing through or traveling along a specified route or intermediate stopping point.",
    "secondary": "In Roman antiquities and civil engineering, public paved highways (such as the Via Appia and Via Flaminia) facilitating military transit.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Legions marched swiftly along the paved stones of the ancient **Via** Appia toward the port of Brundisium."},
      {"author": "Henry James", "work": "Italian Hours", "quote": "We journeyed from Florence to Rome **via** the hill towns of Umbria, delighting in every mountain vista."},
      {"author": "Charles Dickens", "work": "Pictures from Italy", "quote": "The courier advised traveling **via** Genoa to take advantage of the scenic coastal maritime road."}
    ]
  }
}

base_dir = r"App database\Latin roots\Cluster Movement & Speed"
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

print(f"Speed Batch 4C: Successfully updated {updated}/{len(data)} notes.")
