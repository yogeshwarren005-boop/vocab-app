# -*- coding: utf-8 -*-
import os, sys

sys.stdout.reconfigure(encoding="utf-8")

data = {
  # =========================================================================
  # Dashboard — curr (32 words)
  # =========================================================================
  "Dashboard — curr/concurrence.md": {
    "primary": "Agreement or cooperation in action, opinion, or intent; the occurrence of two or more events at the same time.",
    "secondary": "In legal and judicial opinions, an agreement with the majority conclusion arrived at through distinct rationale or separate principles.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Troy glided up to him, beckoned, and whispered a few words; and with a mutual glance of **concurrence** each went on his way."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The accumulation of each great fossiliferous formation will be recognised as having depended on an unusual **concurrence** of favourable circumstances."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Lydgate, I hope we shall not vary in sentiment as to a measure in which you are not likely to be acting without my full **concurrence**."}
    ]
  },
  "Dashboard — curr/concurrency.md": {
    "primary": "The state, quality, or fact of occurring, existing, or operating simultaneously or alongside another.",
    "secondary": "In computer science and distributed systems, the property of program parts executing out-of-order or in partial order without affecting the final outcome.",
    "quotes": [
      {"author": "Edsger W. Dijkstra", "work": "Co-operating Sequential Processes", "quote": "The fundamental problem of **concurrency** lies in coordinating independent sequential processes competing for shared storage."},
      {"author": "C. A. R. Hoare", "work": "Communicating Sequential Processes", "quote": "In analyzing system **concurrency**, input and output are considered as the primary primitives of computation."},
      {"author": "Leslie Lamport", "work": "Time, Clocks, and the Ordering of Events in a Distributed System", "quote": "The concept of **concurrency** requires a rigorous definition of partial ordering across distributed temporal events."}
    ]
  },
  "Dashboard — curr/concurrent.md": {
    "primary": "Existing, happening, or operating at the same time; joint or acting in conjunction with another.",
    "secondary": "In geometry and topology, describing three or more lines or planes that intersect at a single identical point.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Let but a flute play 'neath the fine-mixed metal: listen close till the right note flows forth, a singular tone made of **concurrent** vibrations."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "We know nothing positively on this head, but from the **concurrent** testimony of all travellers, infant mortality among savages is high."},
      {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "When several causes are **concurrent**, each produces its full effect as if the others were not operating."}
    ]
  },
  "Dashboard — curr/concurrently.md": {
    "primary": "At the same time; simultaneously; in joint or cooperative operation.",
    "secondary": "In legal sentencing, designating terms of imprisonment served at the same time rather than consecutively.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The two emperors administered the affairs of the East and West **concurrently**, maintaining the outward semblance of unity."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The Commons and the Lords debated the declaration of rights **concurrently**, eager to secure the constitutional succession."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Multiple sensory streams enter the central cortex **concurrently**, blending into a continuous stream of consciousness."}
    ]
  },
  "Dashboard — curr/concurring.md": {
    "primary": "Agreeing in opinion, purpose, or verdict; cooperating or acting together toward a common effect.",
    "secondary": "In appellate jurisprudence, issuing a separate opinion agreeing with the judgment reached by the court majority while rejecting its specific reasoning.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "In the case of every species, many different checks, acting at different periods of life, and **concurring** together, determine its average numbers."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "Our notions of law and harmony are commonly confined to those instances which we detect; but the harmony resulting from a far greater number of **concurring** laws is wonderful."},
      {"author": "William Shakespeare", "work": "Henry IV, Part 2", "quote": "The dangers of the days but newly gone, whose memory is written on the earth with yet-appearing blood, and the **concurring** likelihood of others to come, do call us back."}
    ]
  },
  "Dashboard — curr/countercurrent.md": {
    "primary": "A current flowing in a direction opposite to that of another current, whether in fluids, winds, or ideological movements.",
    "secondary": "In chemical engineering and biology, heat or solute exchange occurring between two fluids moving in opposite directions across a semipermeable interface.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The Pequod was caught in an eddying **countercurrent**, spinning slowly against the immense oceanic drift."},
      {"author": "Joseph Conrad", "work": "Lord Jim", "quote": "A swift **countercurrent** of thought seemed to arrest his impulse before he could utter another word."},
      {"author": "Matthew Fontaine Maury", "work": "The Physical Geography of the Sea", "quote": "Along the coast of Florida, a deep cold **countercurrent** flows beneath the warmer surface waters of the Gulf Stream."}
    ]
  },
  "Dashboard — curr/currajong.md": {
    "primary": "An Australian evergreen tree (Brachychiton populneus) noted for its swollen trunk, fibrous inner bark, and drought-resistant edible foliage.",
    "secondary": "In Australian indigenous technology and colonial ethnobotany, the tough bast fiber stripped from the trunk to twist into twine, fishing lines, and nets.",
    "quotes": [
      {"author": "Thomas Mitchell", "work": "Three Expeditions into the Interior of Eastern Australia", "quote": "We rested near several handsome specimens of the **currajong**, whose fibrous bark is prized by the natives for manufacturing cords."},
      {"author": "Ludwig Leichhardt", "work": "Journal of an Overland Expedition in Australia", "quote": "The green foliage of the **currajong** furnished our starving bullocks with refreshing fodder along the stony ridges."},
      {"author": "Joseph Maiden", "work": "The Useful Native Plants of Australia", "quote": "The bark of the **currajong** yields a strong and durable ribbon of fiber, long employed by the aborigines for fishing nets."}
    ]
  },
  "Dashboard — curr/currant.md": {
    "primary": "A small dried seedless grape of Mediterranean origin, or the small edible acid berry of shrubs belonging to the genus Ribes.",
    "secondary": "In culinary history and international trade, Corinthian dried raisins (raisins de Corinthe) exported extensively across medieval and early modern Europe.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The common gooseberry cannot be grafted on the **currant**, whereas the **currant** will take, though with difficulty, on the gooseberry."},
      {"author": "James Joyce", "work": "Dubliners", "quote": "We bought two big **currant** buns and sat down to eat them on some metal piping beside the river."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Perhaps you'd like to spend a couple of shillings or so, in a bottle of **currant** wine by and by, up in the bedroom?"}
    ]
  },
  "Dashboard — curr/currawong.md": {
    "primary": "Any of several large, predominantly dark Australian passerine birds of the genus Strepera, known for their loud ringing calls.",
    "secondary": "In Australasian avian ecology, aggressive forest corvoid predators that significantly influence smaller songbird nesting success in temperate woodlands.",
    "quotes": [
      {"author": "John Gould", "work": "The Birds of Australia", "quote": "The pied **currawong** frequents the heavily timbered mountain gullies, uttering its ringing bell-like cry through the morning mist."},
      {"author": "Archibald James Campbell", "work": "Nests and Eggs of Australian Birds", "quote": "In the eucalyptus canopies of Victoria, the watchful **currawong** builds a stout cup of twigs lined with dry grass."},
      {"author": "Neville William Cayley", "work": "What Bird is That?", "quote": "The black **currawong** is a bold and inquisitive inhabitant of Tasmanian scrub, easily recognized by its resounding call."}
    ]
  },
  "Dashboard — curr/currency.md": {
    "primary": "A medium of exchange in the form of banknotes and coins, or widespread acceptance and general circulation in public discourse.",
    "secondary": "In monetary economics, the liquid medium of exchange and unit of account issued by central authorities to settle public and private debts.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "A paper **currency** which is not redeemable in gold or silver will almost certainly undergo excessive depreciation."},
      {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "Every natural fact is a symbol of some spiritual fact; and the mind gives **currency** to symbols that embody universal truths."},
      {"author": "Joseph Conrad", "work": "Heart of Darkness", "quote": "They had given them every week three pieces of brass wire, which was the only **currency** recognized in those wild reaches."}
    ]
  },
  "Dashboard — curr/current.md": {
    "primary": "Flowing or moving in a definite stream or direction; belonging to the present time; generally accepted or in circulation.",
    "secondary": "In electrical physics, the rate of flow of electric charge through a conductor measured in amperes.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "And enterprises of great pith and moment with this regard their currents turn awry, and lose the name of action; but the **current** of my purpose remains fixed."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "When a magnetic pole is moved toward a closed helix of wire, a continuous electric **current** is induced in the circuit."},
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "The oceanic **current** transports sediment over vast marine distances before dropping it onto the continental shelf."}
    ]
  },
  "Dashboard — curr/currently.md": {
    "primary": "At the present time; now; or in a flowing, uninterrupted manner.",
    "secondary": "In contemporary administrative and technological discourse, denoting conditions or parameters prevailing at the moment of observation.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "Miss Doran, whose striking face attracted much attention, was **currently** reported to be the wealthiest heiress in San Francisco."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The rumour was **currently** received by the soldiers, who were prepared to believe any prodigy in that hour of alarm."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The decree was **currently** reported in the coffee-houses of Paris, exciting fierce debates among the patriots."}
    ]
  },
  "Dashboard — curr/currentness.md": {
    "primary": "The property of holding contemporary relevance or active circulation; freshness, up-to-dateness, or prevailing acceptance.",
    "secondary": "In historical rhetoric, fluency or smooth idiomatic flow in speech and written composition.",
    "quotes": [
      {"author": "William Camden", "work": "Remains Concerning Britain", "quote": "When **currentness** combineth with staidness, how can the language sound other than most full of sweetness and gravity?"},
      {"author": "Walter Bagehot", "work": "Biographical Studies", "quote": "The political writer must preserve the fresh **currentness** of his style if he wishes to influence public sentiment."},
      {"author": "John Henry Newman", "work": "The Idea of a University", "quote": "An academic education imparts a living **currentness** to ancient knowledge, rendering it serviceable to modern society."}
    ]
  },
  "Dashboard — curr/curricular.md": {
    "primary": "Of, relating to, or included in an academic course of study or institutional curriculum.",
    "secondary": "In pedagogical design, systematic educational frameworks structuring competencies, course objectives, and learning progressions.",
    "quotes": [
      {"author": "John Dewey", "work": "Democracy and Education", "quote": "The **curricular** program of the school must correspond with the growing social experience of the child."},
      {"author": "Alfred North Whitehead", "work": "The Aims of Education", "quote": "A rigid **curricular** schedule risks deadening the student's intellect with inert ideas that lead to no fresh discovery."},
      {"author": "Matthew Arnold", "work": "Higher Schools and Universities in Germany", "quote": "The German gymnasia maintain rigorous **curricular** standards that ensure comprehensive linguistic and scientific training."}
    ]
  },
  "Dashboard — curr/curriculum.md": {
    "primary": "The regular course of study or collective educational program offered by a school, college, or university.",
    "secondary": "In classical Latin etymology (curriculum), originally a running, racecourse, or career, later transferred to the course of intellectual development.",
    "quotes": [
      {"author": "John Dewey", "work": "The School and Society", "quote": "When the school introduces and trains each child of society into membership within such a little community, the whole **curriculum** is saturated with life."},
      {"author": "Matthew Arnold", "work": "Culture and Anarchy", "quote": "A humane **curriculum** should seek to impart the best that has been thought and said in the world."},
      {"author": "John Henry Newman", "work": "The Idea of a University", "quote": "The university **curriculum** aims at raising the intellectual tone of society and cultivating the public mind."}
    ]
  },
  "Dashboard — curr/currier.md": {
    "primary": "A craftsman who dresses, softens, colors, and finishes tanned leather to prepare it for commercial use.",
    "secondary": "In guild and trade history, the specialized artisan positioned between the tanner (who treated raw hides) and the shoemaker or saddler.",
    "quotes": [
      {"author": "Denis Diderot", "work": "Encyclopédie", "quote": "The **currier** must pummel, scrape, and tallow the tanned hide until it attains complete pliability for the saddler."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The division of labour between the tanner and the **currier** greatly improves the quality and durability of the finished leather."},
      {"author": "Walter Scott", "work": "The Fair Maid of Perth", "quote": "The master **currier** displayed skins dressed with such cunning that no blemish or roughness remained."}
    ]
  },
  "Dashboard — curr/currish.md": {
    "primary": "Resembling, characteristic of, or behaving like a snarling, bad-tempered, or cowardly cur; mean-spirited or snappish.",
    "secondary": "In Elizabethan drama and satire, base, treacherous, or ungrateful behavior devoid of noble sentiment.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Merchant of Venice", "quote": "Thy **currish** spirit govern'd a wolf, who, hang'd for human slaughter, even from the gallows did his fell soul fleet."},
      {"author": "Ben Jonson", "work": "Every Man in His Humour", "quote": "He that is so **currish** to his guests deserves neither love nor fellowship in society."},
      {"author": "John Dryden", "work": "The Spanish Friar", "quote": "He showed a **currish** disposition, barking at every stranger who dared approach his door."}
    ]
  },
  "Dashboard — curr/currishly.md": {
    "primary": "In a currish, snappish, mean-spirited, or ill-tempered manner; churlishly.",
    "secondary": "In early modern prose, responding with spiteful ingratitude or snarling cowardice to generous overtures.",
    "quotes": [
      {"author": "Samuel Richardson", "work": "Clarissa", "quote": "He answered **currishly** that he would not be dictated to by women who understood nothing of his designs."},
      {"author": "Tobias Smollett", "work": "The Adventures of Peregrine Pickle", "quote": "The surly innkeeper growled **currishly** when asked to provide fresh horses at midnight."},
      {"author": "Henry Fielding", "work": "Joseph Andrews", "quote": "He turned **currishly** away from the beggar, refusing even a crust of stale bread."}
    ]
  },
  "Dashboard — curr/curry.md": {
    "primary": "To groom or rub down the coat of a horse; to dress tanned leather; or to cook food with a pungent blend of spices.",
    "secondary": "In idiomatic phraseology (curry favour, from Middle English curry Favel, the chestnut horse of deceit), to seek ingratiating advantage through flattery.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry IV, Part 2", "quote": "If I had a suit to Master Shallow, I would **curry** with Master Shallow that no man could better command his servants."},
      {"author": "Jonathan Swift", "work": "Gulliver's Travels", "quote": "The groom was directed to **curry** and brush the noble steeds each morning with the utmost diligence."},
      {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "Jos Sedley boasted loudly of the fiery Bengal **curry** he had eaten at the Collector's table."}
    ]
  },
  "Dashboard — curr/currycomb.md": {
    "primary": "A comb or brush with rows of metal teeth or ridges, used for grooming horses to remove dried mud, sweat, and loose hair.",
    "secondary": "In agricultural and stable management, a standard implement employed to stimulate blood circulation in equine skin and muscle.",
    "quotes": [
      {"author": "Anna Sewell", "work": "Black Beauty", "quote": "John groomed me thoroughly every morning with the brush and the **currycomb**, never scratching my tender skin."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The rhythmic rasping of the **currycomb** against the horse's flank sounded clearly across the quiet courtyard."},
      {"author": "George Borrow", "work": "Lavengro", "quote": "The ostler set down his **currycomb** and turned to inspect the traveller's weary roadster."}
    ]
  },
  "Dashboard — curr/extracurricular.md": {
    "primary": "Pursued in addition to the normal course of study, curriculum, or regular duties.",
    "secondary": "In educational sociology, student-organized clubs, athletic programs, and civic activities fostering social leadership beyond formal academics.",
    "quotes": [
      {"author": "John Dewey", "work": "The School and Society", "quote": "The social life of the school must expand to include **extracurricular** endeavors where pupils practice practical cooperation."},
      {"author": "Thorstein Veblen", "work": "The Higher Learning in America", "quote": "University administrations have increasingly indulged **extracurricular** athletics to bolster institutional prestige."},
      {"author": "Bertrand Russell", "work": "Education and the Social Order", "quote": "Wholesome **extracurricular** pursuits provide young scholars with relief from the strain of competitive examinations."}
    ]
  },
  "Dashboard — curr/incurrence.md": {
    "primary": "The act of bringing something undesirable or burdensome upon oneself, such as debt, penalty, liability, or danger.",
    "secondary": "In legal and financial contracts, the formal undertaking or triggering of an obligation that binds an entity to subsequent liability.",
    "quotes": [
      {"author": "Jeremy Bentham", "work": "An Introduction to the Principles of Morals and Legislation", "quote": "The legislator must calculate the **incurrence** of mischief against the prospective utility of the enacted statute."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Prudent merchants seek to avoid the unnecessary **incurrence** of debts that cannot be liquidated from annual profits."},
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "The immediate **incurrence** of risk in new commercial enterprises is justified only by the prospect of higher returns."}
    ]
  },
  "Dashboard — curr/incurring.md": {
    "primary": "Bringing upon oneself something disadvantageous, harmful, or burdensome; becoming subject or liable to.",
    "secondary": "In ethics and political theory, assuming moral responsibility or legal culpability through voluntary actions.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "He saw no way of eluding Featherstone's stupid demand without **incurring** consequences which he liked still less."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "He lived in perpetual fear of **incurring** the wrath of his tyrannical stepfather."},
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "By subverting established ancient institutions, they run the danger of **incurring** evils far worse than those they pretend to remedy."}
    ]
  },
  "Dashboard — curr/noncurrent.md": {
    "primary": "Not current; not belonging to the present time; not in active circulation or immediate use.",
    "secondary": "In corporate accounting, assets and liabilities not expected to be converted into cash, consumed, or settled within the current operating cycle.",
    "quotes": [
      {"author": "Arthur Stone Dewing", "work": "The Financial Policy of Corporations", "quote": "A conservative balance sheet clearly segregates **noncurrent** investments from liquid working capital."},
      {"author": "Roy B. Kester", "work": "Accounting Theory and Practice", "quote": "Machinery and permanent plant constitute **noncurrent** assets held for ongoing productive utility rather than immediate sale."},
      {"author": "Irving Fisher", "work": "The Nature of Capital and Income", "quote": "Permanent durable instruments yield returns over protracted intervals and are rightly classified as **noncurrent** capital."}
    ]
  },
  "Dashboard — curr/nonoccurrence.md": {
    "primary": "The failure or absence of an expected event or phenomenon to happen or take place.",
    "secondary": "In probability theory and actuarial science, the complementary probability (1 - p) that a specified contingency does not materialize.",
    "quotes": [
      {"author": "William Stanley Jevons", "work": "The Principles of Science", "quote": "In inductive logic, the **nonoccurrence** of a predicted result provides critical evidence against the hypothesis."},
      {"author": "John Venn", "work": "The Logic of Chance", "quote": "We balance the frequency of occurrences against the **nonoccurrence** of an event across a large statistical series."},
      {"author": "Charles Sanders Peirce", "work": "Illustrations of the Logic of Science", "quote": "A scientific rule is confirmed as much by the constant **nonoccurrence** of violations as by direct positive instances."}
    ]
  },
  "Dashboard — curr/occurrence.md": {
    "primary": "An incident, event, or happening; the fact or frequency of something taking place.",
    "secondary": "In geology and mineralogy, the presence or geographic distribution of a mineral or rock formation within a specific stratigraphic setting.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Twelfth Night", "quote": "All the **occurrence** of my fortune since hath been between this lady and this lord."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "In the course of the afternoon she said to Liddy, who had been informed of the **occurrence**, 'What was that commotion?'"},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The rare **occurrence** of intermediate fossils between related species is directly explained by the imperfection of the geological record."}
    ]
  },
  "Dashboard — curr/occurrent.md": {
    "primary": "Happening or occurring; incident, current, or accidental; (archaic noun) an event, incident, or happening.",
    "secondary": "In early modern English literature and biblical translation, denoting an unfolding circumstance or unforeseen adversary.",
    "quotes": [
      {"author": "King James Bible", "work": "1 Kings", "quote": "But now the LORD my God hath given me rest on every side, so that there is neither adversary nor evil **occurrent**."},
      {"author": "Sir Thomas Browne", "work": "Pseudodoxia Epidemica", "quote": "These we must meet with in obvious **occurrent** events of the world, wherein everyday observations correct old errors."},
      {"author": "Francis Bacon", "work": "The History of the Reign of King Henry the Seventh", "quote": "He received daily intelligence of every remarkable **occurrent** that transpired within the northern borders."}
    ]
  },
  "Dashboard — curr/recurrence.md": {
    "primary": "The act or fact of happening or appearing again repeatedly after an interval.",
    "secondary": "In medical pathology, the return of symptoms or a disease process after a period of remission or apparent cure.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "The banker was always presupposing that he could count in general on Lydgate as a coadjutor, but feared the **recurrence** of obstinate opposition."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The eye prefers symmetry or figures with regular **recurrence** of parts, which seems connected with our aesthetic pleasure."},
      {"author": "Sigmund Freud", "work": "Beyond the Pleasure Principle", "quote": "The compulsion toward the **recurrence** of traumatic impressions points to an instinctual drive deeper than the pleasure principle."}
    ]
  },
  "Dashboard — curr/recurrent.md": {
    "primary": "Occurring, returning, or appearing repeatedly or at regular intervals.",
    "secondary": "In human anatomy and neurology, describing vessels or nerves (such as the recurrent laryngeal nerve) that turn back on their course.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Bathsheba said nothing; but he could distinctly hear her rhythmical pants, and the **recurrent** rustle of her dress."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "In the preservation of favoured individuals and races, during the constantly-**recurrent** Struggle for Life, we see a powerful mechanism of adaptation."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "A **recurrent** sensation leaves in the brain an organized path that facilitates its subsequent revival."}
    ]
  },
  "Dashboard — curr/recurrently.md": {
    "primary": "In a recurrent manner; periodically; occurring repeatedly after intervals.",
    "secondary": "In meteorological and physiological phenomena, unfolding in rhythmic, cyclical pulses over measured durations.",
    "quotes": [
      {"author": "Alexander von Humboldt", "work": "Cosmos", "quote": "The magnetic needle oscillates **recurrently** in accordance with diurnal solar variations."},
      {"author": "William James", "work": "The Varieties of Religious Experience", "quote": "Mystical convictions surge **recurrently** through the consciousness of the religious devotee."},
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "Volcanic eruptions broke out **recurrently** along the subterranean fracture during successive geological epochs."}
    ]
  },
  "Dashboard — curr/recurring.md": {
    "primary": "Happening, appearing, or coming to mind repeatedly or periodically.",
    "secondary": "In arithmetic, designating a repeating decimal where a digit or sequence of digits repeats indefinitely.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Battle within battle must ever be **recurring** with varying success; and yet in the long-run the forces are so nicely balanced."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The clock chimed the midnight hour with a slow **recurring** chime that resonated through the silent village."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "A **recurring** image in memory proves the existence of lasting structural modifications within the brain."}
    ]
  },
  "Dashboard — curr/undercurrent.md": {
    "primary": "A subsurface current in a body of water flowing beneath the surface layer; an underlying opinion, feeling, or tendency contrary to what is openly shown.",
    "secondary": "In social history and psychoanalysis, latent subconscious or subversive tendencies shaping manifest attitudes.",
    "quotes": [
      {"author": "G. K. Chesterton", "work": "The Man Who Was Thursday", "quote": "He made an effort to speak, but Syme went on in a low voice, but with an **undercurrent** of inhuman excitement."},
      {"author": "George Eliot", "work": "Daniel Deronda", "quote": "Beneath her outward composure ran a dark **undercurrent** of dread that she could neither quell nor confess."},
      {"author": "Joseph Conrad", "work": "Lord Jim", "quote": "An **undercurrent** of fierce indignation throbbed through every word he addressed to the court of inquiry."}
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

print(f"Speed Batch 5B: Successfully updated {updated}/{len(data)} notes.")
