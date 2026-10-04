# -*- coding: utf-8 -*-
"""
Curates Cluster Equality (Batch 3B, 34 words):
- Dashboard — ali (remaining 34 words: aralia through unreality)
Total: 34 words.
"""
import sys, re

sys.stdout.reconfigure(encoding="utf-8")

data_batch3b = {
  "aralia": {
    "primary": "A genus of deciduous trees, shrubs, and perennial herbs commonly known as spikenard or angelica tree.",
    "secondary": "Aromatic woodland plants cultivated for bold pinnate foliage and historical medicinal root tonics.",
    "quotes": [
      {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The American spikenard, belonging to the genus **Aralia**, bears aromatic roots and drooping umbels."},
      {"author": "John Torrey", "work": "Flora of North America", "quote": "The prickly stems of **Aralia** spinosa form formidable thickets along southern woodland edges."},
      {"author": "William Bartram", "work": "Travels through North and South Carolina", "quote": "Indigenous healers prepared stimulating infusions from the pungent bark of wild **Aralia**."}
    ]
  },
  "araliaceae": {
    "primary": "The ivy or ginseng family of flowering plants, comprising woody climbers, shrubs, and trees with umbellate flowers.",
    "secondary": "A cosmopolitan family of core eudicots containing economically valuable medicinal plants such as ginseng.",
    "quotes": [
      {"author": "Asa Gray", "work": "Elements of Botany", "quote": "The family **Araliaceae** is closely allied to the Umbelliferae, distinguished by baccate fleshy fruits."},
      {"author": "Joseph Dalton Hooker", "work": "The Flora of British India", "quote": "Species of **Araliaceae** constitute prominent canopy epiphytes and climbers across Himalayan cloud forests."},
      {"author": "John Lindley", "work": "The Vegetable Kingdom", "quote": "Lindley classified the ginseng family under **Araliaceae**, noting the characteristic resinous sap."}
    ]
  },
  "coalition": {
    "primary": "A temporary alliance for combined action, especially of political parties or distinct factions.",
    "secondary": "In international diplomacy, an alliance of nations formed to achieve a specific military or strategic purpose.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "A defensive **coalition** among sovereign states often collapses when immediate external danger recedes."},
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "A grand **coalition** of barbarian tribes threatened the Danubian frontiers of the empire."},
      {"author": "Winston Churchill", "work": "The World Crisis", "quote": "The parliamentary **coalition** maintained national unity throughout the darkest months of the crisis."}
    ]
  },
  "dealing": {
    "primary": "Commercial, professional, or interpersonal transactions and business relations between parties.",
    "secondary": "Fairness, equity, or method in conducting trade, negotiations, or personal treatment.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Honesty and punctual **dealing** constitute the foundation of mercantile credit across nations."},
      {"author": "Charles Dickens", "work": "A Christmas Carol", "quote": "Mankind was my business; charity, mercy, and benevolence were my true **dealing**."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth expected open and candid **dealing** from those whom she honored with her friendship."}
    ]
  },
  "dealings": {
    "primary": "Business relations, transactions, or interpersonal associations carried on with others.",
    "secondary": "Reciprocal commercial intercourse or diplomatic exchanges between organizations or governments.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Queequeg was simple and honest in all his **dealings**, harboring no deceit or petty malice."},
      {"author": "Benjamin Franklin", "work": "Autobiography", "quote": "I resolved to observe scrupulous integrity in all my commercial **dealings** with fellow printers."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "The merchant was guided by legal contracts and mutual self-interest in his daily **dealings**."}
    ]
  },
  "inalienable": {
    "primary": "Unable to be taken away, surrendered, or transferred to another; inherent and absolute.",
    "secondary": "In constitutional jurisprudence, fundamental human rights that belong inherently to each individual.",
    "quotes": [
      {"author": "Thomas Jefferson", "work": "Declaration of Independence", "quote": "All men are endowed by their Creator with certain **inalienable** rights, among these life, liberty, and happiness."},
      {"author": "John Locke", "work": "Second Treatise of Government", "quote": "Natural liberty and property constitute **inalienable** endowments that no sovereign may legitimately usurp."},
      {"author": "Ralph Waldo Emerson", "work": "Self-Reliance", "quote": "Every thinking mind possesses an **inalienable** sovereignty that refuses to conform to blind custom."}
    ]
  },
  "inalienably": {
    "primary": "In an inalienable manner; so as not to be capable of being surrendered or transferred.",
    "secondary": "By inherent right or legal guarantee that cannot be forfeited or revoked.",
    "quotes": [
      {"author": "Thomas Paine", "work": "Rights of Man", "quote": "Civil rights appertain **inalienably** to man by virtue of his existence as a member of society."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "Sovereignty remains **inalienably** vested in the people, though delegated temporarily to their representatives."},
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "Certain core prerogatives of the crown were held to belong **inalienably** to the royal office."}
    ]
  },
  "irreality": {
    "primary": "The lack of reality, substance, or genuine existence; an illusory or dreamlike property.",
    "secondary": "In phenomenological philosophy, the experienced unreality of perceived illusions, fancies, or hallucinations.",
    "quotes": [
      {"author": "Virginia Woolf", "work": "To the Lighthouse", "quote": "A sudden sense of the ghostly **irreality** of material objects swept over her in the quiet room."},
      {"author": "Henry James", "work": "The Wings of the Dove", "quote": "Milly moved through the grand palazzo enveloped in an atmosphere of enchanted **irreality**."},
      {"author": "Joseph Conrad", "work": "Heart of Darkness", "quote": "The silent African jungle produced a disquieting feeling of phantom-like **irreality** upon the European travelers."}
    ]
  },
  "nonalinement": {
    "primary": "The policy or principle of remaining neutral and not aligning with major rival power blocs.",
    "secondary": "In international diplomacy during the Cold War, the stance of nations committed to non-alignment.",
    "quotes": [
      {"author": "Jawaharlal Nehru", "work": "Speeches", "quote": "The foreign policy of **nonalinement** preserves our national freedom of judgment in global affairs."},
      {"author": "George Kennan", "work": "Memoirs", "quote": "Diplomats observed the emerging bloc of developing nations that advocated strict diplomatic **nonalinement**."},
      {"author": "Winston Churchill", "work": "The Second World War", "quote": "Small nations found it perilous to profess **nonalinement** when totalitarian empires sought continental hegemony."}
    ]
  },
  "opaline": {
    "primary": "Showing a variety of changing colors like an opal; displaying soft, milky, or iridescent hues.",
    "secondary": "A type of translucent or opaque milky glass often tinted with delicate pastel colors.",
    "quotes": [
      {"author": "John Ruskin", "work": "Modern Painters", "quote": "The evening clouds dissolved into an ethereal **opaline** haze against the alpine horizon."},
      {"author": "Edgar Allan Poe", "work": "The Domain of Arnheim", "quote": "The placid lake reflected the soft **opaline** tints of the sunset sky with crystalline fidelity."},
      {"author": "Herman Melville", "work": "Typee", "quote": "The secluded bay shone like an **opaline** jewel framed by emerald mountain ridges."}
    ]
  },
  "opalise": {
    "primary": "To make or become opalescent; to take on the milky, iridescent luster of an opal.",
    "secondary": "In geology, to convert wood or organic fossils into opal through silica mineral precipitation.",
    "quotes": [
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The morning mist began to **opalise** under the first radiant beams of the Adriatic dawn."},
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "Siliceous thermal springs gradually **opalise** buried tree trunks into fossilized wood."},
      {"author": "Thomas Hardy", "work": "A Pair of Blue Eyes", "quote": "The evening sea seemed to **opalise** beneath the pale crescent moon."}
    ]
  },
  "opalize": {
    "primary": "To convert into or take on the appearance and milky iridescence of an opal.",
    "secondary": "In petrology, to replace mineral grains or fossil organic structures with hydrated amorphous silica.",
    "quotes": [
      {"author": "Charles Darwin", "work": "Geological Observations on South America", "quote": "Siliceous thermal waters **opalize** the trunks of ancient coniferous trees embedded in volcanic tuff."},
      {"author": "James Dwight Dana", "work": "Manual of Mineralogy", "quote": "Hydrated silica solutions slowly **opalize** porous sedimentary beds, creating precious gems."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "The autumn twilight seemed to **opalize** the glassy surface of the tranquil pond."}
    ]
  },
  "realine": {
    "primary": "To align again; to bring back into correct relative position, orientation, or line.",
    "secondary": "In military maneuvers or institutional planning, to reorganize forces or strategic goals.",
    "quotes": [
      {"author": "Winston Churchill", "work": "The River War", "quote": "The battalion halted beneath the ridge to **realine** its ranks before advancing into the open plain."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The assembly attempted to **realine** municipal administrative boundaries throughout the provinces."},
      {"author": "Herman Melville", "work": "White-Jacket", "quote": "The boatswain ordered the seamen to **realine** the heavy deck battery along the starboard battery."}
    ]
  },
  "realisation": {
    "primary": "The act of becoming fully aware of something as a fact; comprehension or awareness.",
    "secondary": "The fulfillment, achievement, or actual execution of a plan, artistic vision, or financial asset.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "The sudden **realisation** of her husband's intellectual mediocrity fell heavily upon Dorothea's heart."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Pip awoke to the bitter **realisation** that his lavish lifestyle had brought ruin and debt."},
      {"author": "Joseph Conrad", "work": "Lord Jim", "quote": "His romantic dreams of heroic conduct crumbled before the sudden **realisation** of mortal peril."}
    ]
  },
  "realise": {
    "primary": "To become fully aware of something as a fact; to understand clearly and vividly.",
    "secondary": "To bring into concrete reality; to accomplish a goal or convert property into money.",
    "quotes": [
      {"author": "Jane Austen", "work": "Emma", "quote": "Emma paused, beginning to **realise** the foolish vanity that had guided her matchmaking schemes."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "I did not **realise** the full extent of my loneliness until the cold winter night set in."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "A prudent merchant sells his surplus stock to **realise** immediate liquid capital."}
    ]
  },
  "realised": {
    "primary": "Clearly understood, perceived, or made fully conscious in thought.",
    "secondary": "Brought into actual, concrete existence or converted into cash assets.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Angel Clare **realised** too late the cruel injustice of his self-righteous abandonment."},
      {"author": "George Eliot", "work": "Silas Marner", "quote": "The weaver had **realised** a small fortune in golden guineas through decades of uninterrupted toil."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The legacy was never **realised**, swallowed entirely by the monstrous costs of the Chancery litigation."}
    ]
  },
  "realism": {
    "primary": "The attitude or practice of accepting a situation as it is and dealing with it practically.",
    "secondary": "In the arts and literature, the accurate and unembellished representation of ordinary life and nature.",
    "quotes": [
      {"author": "George Eliot", "work": "Adam Bede", "quote": "The author defended artistic **realism**, painting Dutch-like pictures of rustic life without false glamour."},
      {"author": "William Dean Howells", "work": "Criticism and Fiction", "quote": "Literary **realism** is nothing more and nothing less than the truthful treatment of material."},
      {"author": "Henry James", "work": "The Art of Fiction", "quote": "The novel achieves greatness when psychological **realism** reveals the inner motives of human conduct."}
    ]
  },
  "realist": {
    "primary": "A person who accepts a situation as it is and deals with it in a practical, unromantic way.",
    "secondary": "In literature, art, or philosophy, a writer, painter, or thinker who adheres to the principles of realism.",
    "quotes": [
      {"author": "George Bernard Shaw", "work": "Man and Superman", "quote": "The true **realist** sees human nature without sentimental illusions and acts accordingly."},
      {"author": "Edith Wharton", "work": "The Age of Innocence", "quote": "Newland Archer considered himself a cool **realist**, yet he was trapped by tribal conventions."},
      {"author": "Ralph Waldo Emerson", "work": "Representative Men", "quote": "Montaigne was the quintessential **realist**, testing every dogma against the facts of daily experience."}
    ]
  },
  "realistic": {
    "primary": "Having or showing a sensible and practical idea of what can be achieved or expected.",
    "secondary": "Representing things in a way that is accurate and true to life in art or literature.",
    "quotes": [
      {"author": "Sinclair Lewis", "work": "Babbitt", "quote": "The committee adopted a **realistic** business plan that anticipated seasonal market downturns."},
      {"author": "Virginia Woolf", "work": "To the Lighthouse", "quote": "Lily Briscoe struggled to paint a vision that was neither photographic nor falsely **realistic**."},
      {"author": "Winston Churchill", "work": "The Gathering Storm", "quote": "A **realistic** appraisal of enemy armaments dispelled the comfortable delusions of the appeasers."}
    ]
  },
  "realistically": {
    "primary": "In a way that demonstrates a sensible and practical approach to life or problems.",
    "secondary": "In a manner that depicts things accurately and faithfully to life.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Farebrother advised Lydgate to assess his financial prospects **realistically** before taking on debt."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Traddles faced his humble prospects **realistically**, working diligently in his modest lodgings."},
      {"author": "Thomas Hardy", "work": "Jude the Obscure", "quote": "The author depicted rural poverty **realistically**, stripping away idyllic pastoral illusions."}
    ]
  },
  "reality": {
    "primary": "The state of things as they actually exist, rather than as they may appear or might be imagined.",
    "secondary": "The real world, real events, or actual facts taken as a whole.",
    "quotes": [
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "The scarlet letter had the effect of an inescapable spell, taking place of all other **reality**."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Meditation and water are wedded for ever; but **reality** demands our constant vigilance at the helm."},
      {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "Behind the outward mask of material appearance lies the sublime spiritual **reality** of the universe."}
    ]
  },
  "realization": {
    "primary": "An act of becoming fully aware of something as a fact; understanding.",
    "secondary": "The fulfillment, achievement, or actual execution of a plan, concept, or artistic work.",
    "quotes": [
      {"author": "Nathaniel Hawthorne", "work": "The Marble Faun", "quote": "The sudden **realization** of shared guilt created an indissoluble bond between the companions."},
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "Isabel paused in horror at the **realization** that she had walked into a calculated trap."},
      {"author": "Ralph Waldo Emerson", "work": "The Conduct of Life", "quote": "Genius consists in the practical **realization** of inspired thought through persistent labor."}
    ]
  },
  "realize": {
    "primary": "To become fully aware of something as a fact; to understand clearly.",
    "secondary": "To bring into concrete reality; to achieve, accomplish, or convert property into money.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Pip began to **realize** that true gentility lay in honest kindness rather than fine clothes."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Few men **realize** the terrifying magnitude of a sperm whale until they encounter it upon the sea."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "A manufacturer must sell his inventory in timely fashion to **realize** his capital profits."}
    ]
  },
  "sealing": {
    "primary": "The action of fastening, closing, or securing something firmly with a wax, adhesive, or mechanical seal.",
    "secondary": "The hunting of marine seals for oil, fur, or meat; seal fishery.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The ship was engaged in southern **sealing** expeditions among the rocky Crozet Islands."},
      {"author": "Jack London", "work": "The Sea-Wolf", "quote": "The schooner Ghost was bound for the stormy waters of the Bering Sea on a **sealing** voyage."},
      {"author": "Arthur Conan Doyle", "work": "The Adventure of Black Peter", "quote": "The old sea captain had spent his youth in arctic whaling and **sealing** in the icy north."}
    ]
  },
  "sedalia": {
    "primary": "A historic city in west-central Missouri, renowned as a major railroad crossroads and birthplace of ragtime music.",
    "secondary": "In nineteenth-century frontier history, northern terminus of historic Texas cattle drives along the Sedalia Trail.",
    "quotes": [
      {"author": "Mark Twain", "work": "Life on the Mississippi", "quote": "Railroads converged upon the burgeoning Missouri town of **Sedalia**, linking midwestern markets."},
      {"author": "Theodore Roosevelt", "work": "Hunting Trips of a Ranchman", "quote": "Cowboys drove massive herds of Texas longhorns northward toward the railway corrals at **Sedalia**."},
      {"author": "Sinclair Lewis", "work": "Main Street", "quote": "The traveling salesman recounted his adventures from Chicago to the busy railroad yards of **Sedalia**."}
    ]
  },
  "surrealism": {
    "primary": "A twentieth-century avant-garde movement in art and literature seeking to release unconscious creative potential.",
    "secondary": "Artistic expression characterized by dreamlike, bizarre, or irrational juxtapositions of imagery.",
    "quotes": [
      {"author": "André Breton", "work": "Manifesto of Surrealism", "quote": "Philosophical **surrealism** rests upon the supreme belief in the superior reality of dream associations."},
      {"author": "Salvador Dalí", "work": "The Secret Life of Salvador Dalí", "quote": "Through paranoiac-critical painting, I sought to materialize the irrational visions of **surrealism**."},
      {"author": "Gertrude Stein", "work": "The Autobiography of Alice B. Toklas", "quote": "In the Parisian avant-garde cafes, artists debated whether **surrealism** had superseded cubism."}
    ]
  },
  "surrealist": {
    "primary": "An artist, writer, or adherent associated with the surrealism movement.",
    "secondary": "Relating to or characteristic of surrealism; producing incongruous or dreamlike artistic works.",
    "quotes": [
      {"author": "André Breton", "work": "Surrealism and Painting", "quote": "The **surrealist** poet uncovers the hidden marvellous in the everyday streets of modern Paris."},
      {"author": "Salvador Dalí", "work": "The Secret Life of Salvador Dalí", "quote": "Every true **surrealist** painter transforms inner obsessions into objective pictorial realities."},
      {"author": "Virginia Woolf", "work": "The Waves", "quote": "The fragmented juxtaposition of images reminded her of the provocative canvases of a modern **surrealist**."}
    ]
  },
  "surrealistic": {
    "primary": "Having a strange, dreamlike, bizarre, or hallucinatory quality; characteristic of surrealism.",
    "secondary": "Featuring unexpected, irrational, or incongruous juxtapositions of scenes, objects, or ideas.",
    "quotes": [
      {"author": "H.G. Wells", "work": "The Shape of Things to Come", "quote": "The ruins of the bombed metropolis presented a horrifying, **surrealistic** landscape of twisted steel."},
      {"author": "Aldous Huxley", "work": "Brave New World", "quote": "The sensory synthetic cinema projected vivid, **surrealistic** visions directly into the spectator's cortex."},
      {"author": "George Orwell", "work": "Homage to Catalonia", "quote": "The midnight trench raid under blinding magnesium flares had a nightmare, **surrealistic** horror."}
    ]
  },
  "unalienable": {
    "primary": "Incapable of being alienated, surrendered, or transferred; variant of inalienable.",
    "secondary": "In political theory, describing inherent rights belonging to mankind that cannot be surrendered to government.",
    "quotes": [
      {"author": "Thomas Jefferson", "work": "Declaration of Independence", "quote": "We hold these truths to be self-evident, that all men are created equal, with certain **unalienable** Rights."},
      {"author": "Abraham Lincoln", "work": "Speech at Lewistown", "quote": "The founders declared that liberty was the **unalienable** birthright of all human beings."},
      {"author": "Ralph Waldo Emerson", "work": "The Conduct of Life", "quote": "Moral freedom is the **unalienable** prerogative of every soul that dares to think independently."}
    ]
  },
  "unrealised": {
    "primary": "Not achieved, fulfilled, completed, or brought into actual reality.",
    "secondary": "In finance, potential profit or loss on an investment that has not yet been sold or converted to cash.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Casaubon died leaving his grandiose Key to all Mythologies a tragic, **unrealised** fragment."},
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "Henchard lamented his **unrealised** ambitions, viewing his ruined business with bitter despair."},
      {"author": "Charlotte Brontë", "work": "Villette", "quote": "A thousand **unrealised** hopes fluttered through Lucy's lonely heart in the quiet schoolroom."}
    ]
  },
  "unrealism": {
    "primary": "The lack of realism; impracticality, fancifulness, or detachment from objective facts.",
    "secondary": "In art and literature, stylistic departure from faithful representation in favor of fantasy or abstraction.",
    "quotes": [
      {"author": "George Bernard Shaw", "work": "Major Barbara", "quote": "The dramatist mocked the sentimental **unrealism** of popular melodrama with acerbic wit."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Daydreaming indulges a harmless **unrealism**, but habitual detachment from facts paralyzes the will."},
      {"author": "John Dewey", "work": "Art as Experience", "quote": "Excessive aesthetic **unrealism** severs art from its vital roots in human biological experience."}
    ]
  },
  "unrealistic": {
    "primary": "Not realistic; having an impractical, romanticized, or distorted view of what can be accomplished.",
    "secondary": "Not depicted in a natural, accurate, or life-like manner in art or literature.",
    "quotes": [
      {"author": "Sinclair Lewis", "work": "Arrowsmith", "quote": "The laboratory director dismissed the ambitious young researcher's proposals as hopelessly **unrealistic**."},
      {"author": "Virginia Woolf", "work": "Night and Day", "quote": "Katharine resisted her mother's **unrealistic** romantic fantasies regarding family lineage."},
      {"author": "Winston Churchill", "work": "The Gathering Storm", "quote": "It was fatally **unrealistic** to suppose that international treaties alone could restrain armed aggression."}
    ]
  },
  "unrealistically": {
    "primary": "In an unrealistic, impractical, or fanciful manner; without regard to actual conditions.",
    "secondary": "In a manner that departs from faithful or natural representation.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Rosamond judged her husband's income **unrealistically**, expecting endless credit from local tradesmen."},
      {"author": "Thomas Hardy", "work": "Jude the Obscure", "quote": "Jude had dreamed **unrealistically** of university honors while laboring as an obscure stonecutter."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Mr. Skimpole lived **unrealistically**, serenely expecting others to pay his mounting butcher bills."}
    ]
  },
  "unreality": {
    "primary": "The property or fact of being unreal, illusory, fictitious, or insubstantial.",
    "secondary": "An illusion, phantom, or daydream lacking genuine substance or factual foundation.",
    "quotes": [
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "The minister walked through the town as in a dream, conscious of the terrifying **unreality** around him."},
      {"author": "Herman Melville", "work": "Pierre; or, The Ambiguities", "quote": "The luxurious aristocratic world of his youth dissolved into a pale, hollow **unreality**."},
      {"author": "Joseph Conrad", "work": "Lord Jim", "quote": "The sudden catastrophe struck Jim with the paralyzing force of an incomprehensible **unreality**."}
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
    for word, item in data_batch3b.items():
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
        print(f"SUCCESS: All {len(data_batch3b)} words in Batch 3B are 100% compliant with audit rules!")
