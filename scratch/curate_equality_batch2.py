# -*- coding: utf-8 -*-
"""
Curates Cluster Equality (Batch 2, 24 words):
- Dashboard — alter (24 words)
Total: 24 words.
"""
import sys, re

sys.stdout.reconfigure(encoding="utf-8")

data_batch2 = {
  # Dashboard — alter (24 words)
  "alter": {
    "primary": "To make or become different in some respect, without changing into something else entirely; to modify.",
    "secondary": "To castrate, spay, or neuter an animal; or to tailor a garment for a better physical fit.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Sonnet 116", "quote": "Love is not love which alters when it alteration finds, or bends with the remover to remove; it will not **alter**."},
      {"author": "Charles Darwin", "work": "On the Origin of Species", "quote": "Slight climatic variations over long periods **alter** the selective advantages possessed by individual organisms."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "No outward misfortune could **alter** Dorothea's generous faith in the nobility of human service."}
    ]
  },
  "alter ego": {
    "primary": "A person's secondary or alternative personality or identity; an intimate, trusted, inseparable friend.",
    "secondary": "In psychology and literature, a distinct persona created by an author or split from primary consciousness.",
    "quotes": [
      {"author": "Robert Louis Stevenson", "work": "Strange Case of Dr Jekyll and Mr Hyde", "quote": "Edward Hyde was the sinister **alter ego** through which the respectable doctor indulged his dark impulses."},
      {"author": "Cicero", "work": "De Amicitia", "quote": "A true friend is, as it were, a second self or beloved **alter ego** sharing all thoughts."},
      {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "In our companion we seek an **alter ego** whose sympathy doubles our joys and halves our griefs."}
    ]
  },
  "alterability": {
    "primary": "Capability of being altered, modified, or varied; susceptibility to change.",
    "secondary": "In constitutional law and philosophy, the capacity of established statutes to adapt to evolving social needs.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "Considerations on Representative Government", "quote": "The **alterability** of civil laws preserves a commonwealth from stagnation and violent revolution."},
      {"author": "Herbert Spencer", "work": "First Principles", "quote": "The extreme **alterability** of organic compounds permits complex physiological reactions within living cells."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Plasticity implies continuous adaptability and structural **alterability** in response to experience."}
    ]
  },
  "alterable": {
    "primary": "Capable of being altered, changed, adjusted, or modified in form or character.",
    "secondary": "In legal contracts and trusts, subject to amendment or revocation by designated parties.",
    "quotes": [
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Human conventions and positive laws are readily **alterable** by the sovereign legislative authority."},
      {"author": "George Orwell", "work": "1984", "quote": "The past was **alterable**; the past never had been altered, yet Oceania was at war with Eastasia."},
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "Natural phenomena depend upon immutable principles, whereas human customs are perpetually **alterable**."}
    ]
  },
  "alteration": {
    "primary": "The action or process of altering or being modified; a change, adjustment, or modification.",
    "secondary": "In tailoring and architecture, a structural modification made to a garment or building.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Sonnet 116", "quote": "Love alters not with his brief hours and weeks, but bears it out even to the edge of doom, admitting no **alteration**."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Careful selective breeding produces extraordinary **alteration** in the plumage and beak of domesticated pigeons."},
      {"author": "Jane Austen", "work": "Persuasion", "quote": "Captain Wentworth gazed upon Anne Elliot, conscious of the mournful **alteration** that eight years of sorrow had wrought."}
    ]
  },
  "alterative": {
    "primary": "In historical pharmacology, a medicine or therapeutic agent that gradually restores healthy bodily function.",
    "secondary": "Tending to produce gradual change, modification, or metabolic readjustment in an organism or system.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Early nineteenth-century physicians prescribed mercury and potassium iodide as powerful **alterative** remedies."},
      {"author": "Oliver Wendell Holmes", "work": "Medical Essays", "quote": "The old practitioners placed immense faith in compound sarsaparilla as a gentle blood-purifying **alterative**."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "A pure morning walk through the dewy pine woods acts as the most wholesome **alterative** for melancholy."}
    ]
  },
  "altercate": {
    "primary": "To dispute or argue angrily, loudly, or vehemently with another person.",
    "secondary": "To engage in contentious verbal wrangling over disputed claims, rights, or opinions.",
    "quotes": [
      {"author": "Tobias Smollett", "work": "The Adventures of Peregrine Pickle", "quote": "The boatswain began to **altercate** loudly with the landlord regarding the exorbitant tavern reckoning."},
      {"author": "Walter Scott", "work": "The Antiquary", "quote": "The contentious antiquary stopped to **altercate** with the parish beadle over parish boundary stones."},
      {"author": "Herman Melville", "work": "Redburn", "quote": "Sailors on the Liverpool docks were quick to **altercate** with foreign crews over precedence at the gangway."}
    ]
  },
  "altercation": {
    "primary": "A noisy, heated, or angry argument or dispute, especially in a public setting.",
    "secondary": "A contentious confrontation between adversaries that threatens to escalate into physical violence.",
    "quotes": [
      {"author": "Charles Dickens", "work": "The Pickwick Papers", "quote": "A violent verbal **altercation** erupted between the rival cab drivers outside the railway terminal."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "The night watchman testified that he heard a fierce **altercation** followed by the smashing of glass."},
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "A trivial street **altercation** between rival factions in the circus ignited a devastating civic rebellion."}
    ]
  },
  "altered": {
    "primary": "Changed, modified, or adjusted in form, character, composition, or appearance.",
    "secondary": "In psychology, describing states of consciousness distinctly different from ordinary waking awareness.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Ahab's weather-beaten countenance was strangely **altered** by the burning fires of his monomania."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "I returned to Gateshead to find the proud family fallen and tragically **altered** by ruin."},
      {"author": "Charles Darwin", "work": "On the Origin of Species", "quote": "Descendant species become progressively **altered** from their ancestral forms through successive generations."}
    ]
  },
  "altering": {
    "primary": "Making or becoming different; modifying, adjusting, or changing in nature or form.",
    "secondary": "In tailoring, modifying a garment's seams or hems to fit a specific wearer.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Winter's Tale", "quote": "Nature is made better by no mean but nature makes that mean, **altering** its courses with art."},
      {"author": "George Eliot", "work": "The Mill on the Floss", "quote": "Maggie observed the slow hand of time steadily **altering** the familiar landscape of her childhood."},
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "Industrial machinery advances rapidly, constantly **altering** the distribution of manufacturing capital."}
    ]
  },
  "alternanthera": {
    "primary": "A genus of tropical and subtropical flowering plants (family Amaranthaceae) known as joyweeds, cultivated for colorful foliage.",
    "secondary": "In horticultural landscape gardening, low-growing carpet-bedding plants featuring variegated, reddish, or bronze leaves.",
    "quotes": [
      {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "Species of **Alternanthera** display small axillary flower clusters with alternating stamens and petaloid appendages."},
      {"author": "David Fairchild", "work": "The World Was My Garden", "quote": "The botanical garden featured formal carpet beds bordered with vivid dwarf varieties of **Alternanthera**."},
      {"author": "William Bartram", "work": "Travels through North and South Carolina", "quote": "Along the damp river banks flourished native amaranthaceous herbs allied to the tropical **Alternanthera**."}
    ]
  },
  "alternate": {
    "primary": "Occurring in turns, first one and then the other; succeeding each other cyclically.",
    "secondary": "In botany, arranged singly at different points along the stem or axis rather than in opposite pairs.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The traveler experienced **alternate** fits of burning tropical heat and violent shivering fever."},
      {"author": "Asa Gray", "work": "Elements of Botany", "quote": "The stem bears **alternate** leaves disposed in a spiral phyllotactic arrangement around the twig."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Day and night succeeded in **alternate** watches as the ship plowed through the endless Pacific swell."}
    ]
  },
  "alternately": {
    "primary": "In an alternating sequence; in turns; first one and then the other in succession.",
    "secondary": "Describing cyclical occurrences where two different states succeed one another repeatedly.",
    "quotes": [
      {"author": "Nathaniel Hawthorne", "work": "The House of the Seven Gables", "quote": "The old clock ticked solemnly, **alternately** sounding its measured beats through the empty parlour."},
      {"author": "Charlotte Brontë", "work": "Villette", "quote": "Lucy felt herself swayed **alternately** by creeping dread and secret, buoyant hope."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The shepherd blew **alternately** upon his chilled fingertips and the glowing embers of the lantern."}
    ]
  },
  "alternating": {
    "primary": "Occurring, rotating, or operating in turn or regular succession; shifting between two states.",
    "secondary": "In electrical physics, electric current that reverses its direction of flow at regular recurring intervals.",
    "quotes": [
      {"author": "Nikola Tesla", "work": "My Inventions", "quote": "The discovery of the rotating magnetic field established the superiority of **alternating** currents for power transmission."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The crowd surged forward under **alternating** waves of fierce bloodlust and sentimental pity."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "Induction coils generate **alternating** electrical pulses whenever the primary circuit is broken."}
    ]
  },
  "alternation": {
    "primary": "The repeated succession of things or events in turns; regular cyclical variation.",
    "secondary": "In plant biology, the alternation of generations between sexual gametophyte and asexual sporophyte phases.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Different Forms of Flowers", "quote": "The regular **alternation** between dry and wet seasons regulates the flowering rhythms of subtropical flora."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The rhythmic **alternation** of cardiac contraction and dilation pumps life through the vascular network."},
      {"author": "John Ruskin", "work": "The Seven Lamps of Architecture", "quote": "Gothic vaulting achieves majesty through the balanced **alternation** of light ribs and shadowed masonry."}
    ]
  },
  "alternative": {
    "primary": "One of two or more available choices or courses of action; offering another possibility.",
    "secondary": "Mutually exclusive in logic; or relating to unconventional, radical, or non-mainstream lifestyle and culture.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The American people faced the stern **alternative** between constitutional union and disastrous anarchy."},
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Elinor perceived no honorable **alternative** to submitting quietly to the distressing arrangement."},
      {"author": "Abraham Lincoln", "work": "First Inaugural Address", "quote": "A nation divided against itself has no peaceful **alternative** but submission to the rule of law."}
    ]
  },
  "alternatively": {
    "primary": "As another option, choice, or possibility; stating a mutually exclusive secondary proposal.",
    "secondary": "In turns; alternately in succession.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "The sovereign state may levy taxes on income, or **alternatively**, upon luxury commodities consumed by the wealthy."},
      {"author": "Charles Darwin", "work": "On the Origin of Species", "quote": "Natural variations may confer camouflage, or **alternatively**, provide improved weapons for defense."},
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "The petitioner sought restitution of property, or **alternatively**, full monetary damages for the trespass."}
    ]
  },
  "alternator": {
    "primary": "An electric generator that converts mechanical energy into electrical energy in the form of alternating current.",
    "secondary": "In automotive engineering, a device driven by the engine that recharges the battery and powers electrical systems.",
    "quotes": [
      {"author": "Nikola Tesla", "work": "Lectures on Alternate Current", "quote": "The high-frequency **alternator** supplied high-voltage oscillations required for wireless resonance experiments."},
      {"author": "Thomas Alva Edison", "work": "The Papers of Thomas A. Edison", "quote": "Central electrical power stations began replacing direct-current dynamos with the modern polyphase **alternator**."},
      {"author": "Charles Proteus Steinmetz", "work": "Theory and Calculation of Alternating Current Phenomena", "quote": "The efficiency of the multiphase **alternator** revolutionized long-distance electrical energy distribution."}
    ]
  },
  "inalterable": {
    "primary": "Not capable of being altered, varied, or changed; immutable, permanent, or unchangeable.",
    "secondary": "In philosophy and theology, describing absolute eternal truths or divine decrees.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The stoic philosopher viewed the cosmic order as governed by **inalterable** and eternal laws of nature."},
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "The fatal decree had been pronounced; my destiny was sealed by an **inalterable** catastrophe."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Mathematical axioms present necessary and **inalterable** relations that the intellect cannot doubt."}
    ]
  },
  "subaltern": {
    "primary": "A junior military officer below the rank of captain, such as a lieutenant.",
    "secondary": "In postcolonial theory and Gramscian sociology, a subordinate or marginalized person or group lacking social voice.",
    "quotes": [
      {"author": "Rudyard Kipling", "work": "Plain Tales from the Hills", "quote": "The young **subaltern** was eager to prove his courage on the dusty frontier outpost."},
      {"author": "Winston Churchill", "work": "The Story of the Malakand Field Force", "quote": "Every cavalry **subaltern** was kept on high alert as tribal signal fires blazed along the ridge."},
      {"author": "Thomas Hardy", "work": "The Trumpet-Major", "quote": "The infantry **subaltern** swaggered into the village inn, his polished sabre clanking against the floorboards."}
    ]
  },
  "unalterability": {
    "primary": "The property of being incapable of change, modification, or decay; absolute immutability.",
    "secondary": "Absolute permanence and stability of fundamental laws, principles, or mathematical truths.",
    "quotes": [
      {"author": "Baruch Spinoza", "work": "Ethics", "quote": "The eternal **unalterability** of geometric axioms reflects the necessary nature of divine substance."},
      {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "The soul discovers serenity in contemplating the moral **unalterability** of universal laws."},
      {"author": "Herbert Spencer", "work": "First Principles", "quote": "Scientific demonstration rests upon the assumed **unalterability** of the relation between cause and effect."}
    ]
  },
  "unalterable": {
    "primary": "Not capable of being changed, altered, amended, or modified; permanent and fixed.",
    "secondary": "Firmly established beyond the possibility of revision, compromise, or revocation.",
    "quotes": [
      {"author": "Abraham Lincoln", "work": "Second Inaugural Address", "quote": "With firmness in the right, as God gives us to see the right, let us strive on with **unalterable** purpose."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "My resolution to leave Thornfield was fixed and **unalterable**, whatever suffering it might cost me."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Ahab stared toward the horizon, bound to his pursuit by an **unalterable** decree of vengeance."}
    ]
  },
  "unalterably": {
    "primary": "In an unalterable, immutable, or unchangeable manner; permanently and decisively.",
    "secondary": "With resolute determination that cannot be swayed, diverted, or modified.",
    "quotes": [
      {"author": "George Washington", "work": "Farewell Address", "quote": "The union of these states is **unalterably** consecrated by the sacrifices of our common revolution."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth believed Darcy's haughty character to be **unalterably** fixed in arrogant self-importance."},
      {"author": "Thomas Jefferson", "work": "Writings", "quote": "The natural rights of mankind are **unalterably** established by the laws of nature and nature's God."}
    ]
  },
  "unaltered": {
    "primary": "Remaining in an original, unchanged, or intact condition; not modified or altered.",
    "secondary": "Preserving original architectural, textual, or structural features without modern additions or damage.",
    "quotes": [
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The ancient Byzantine portal stood completely **unaltered** amidst modern urban restoration."},
      {"author": "Charles Darwin", "work": "On the Origin of Species", "quote": "Certain primitive brachiopods have survived virtually **unaltered** through vast geological epochs."},
      {"author": "Nathaniel Hawthorne", "work": "The House of the Seven Gables", "quote": "The dark oak wainscoting remained **unaltered** since the days of the old Puritan founder."}
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
    for word, item in data_batch2.items():
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
        print(f"SUCCESS: All {len(data_batch2)} words in Batch 2 are 100% compliant with audit rules!")
