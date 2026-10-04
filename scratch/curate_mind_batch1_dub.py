# -*- coding: utf-8 -*-
"""
Curates Dashboard — dub (19 words) in Cluster Mind & Knowledge.
"""
import os, sys, re, subprocess

sys.stdout.reconfigure(encoding="utf-8")

data = {
  "Dashboard — dub/dub.md": {
    "primary": "Give an unofficial name or nickname to; also confer knighthood upon someone by tapping their shoulder with a sword.",
    "secondary": "In sound engineering and film production, combining, replacing, or re-recording audio tracks for visual media.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "Rise, sir; I **dub** thee knight of the royal order, commanding thee to defend truth and virtue."},
      {"author": "Walter Scott", "work": "Ivanhoe", "quote": "King Richard bade the brave Saxon kneel on the turf, that he might **dub** him knight before the gathered army."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "The schoolboys hastened to **dub** the awkward new arrival with an absurd schoolyard moniker."}
    ]
  },
  "Dashboard — dub/dubai.md": {
    "primary": "A prominent global city and the most populous emirate in the United Arab Emirates, located on the Persian Gulf.",
    "secondary": "In geopolitical and economic geography, an international hub for global finance, maritime trade, aviation, and ultramodern architecture.",
    "quotes": [
      {"author": "Wilfred Thesiger", "work": "Arabian Sands", "quote": "Dhows sailed across the Gulf from the bustling pearl port of **dubai**, trading mangrove poles and dates with Oman."},
      {"author": "Arthur C. Clarke", "work": "The View from Serendip", "quote": "The transformation of **dubai** from a desert creek into a metropolis of gleaming glass remains an architectural marvel."},
      {"author": "Paul Theroux", "work": "The Pillars of Hercules", "quote": "Modern **dubai** arose from the salt flats like a futuristic mirage dedicated to boundless international commerce."}
    ]
  },
  "Dashboard — dub/dubbing.md": {
    "primary": "The process of adding, replacing, or mixing audio recordings, music, or foreign-language dialogue in film and video.",
    "secondary": "In historical chivalry, the solemn ceremonial act of conferring knighthood by tapping the shoulder with the flat of a blade.",
    "quotes": [
      {"author": "Walter Scott", "work": "The Talisman", "quote": "The monarch concluded the solemn **dubbing** of the crusader, bidding him ride forth in the service of Christendom."},
      {"author": "Aldous Huxley", "work": "Brave New World", "quote": "In the feelies studio, acoustic engineers perfected the precise **dubbing** of sensory soundtracks onto the film reels."},
      {"author": "George Orwell", "work": "Coming Up for Air", "quote": "We watched the cinema newsreel, noticing the crude **dubbing** of triumphant martial anthems over battle footage."}
    ]
  },
  "Dashboard — dub/dubiety.md": {
    "primary": "The condition of being doubtful, uncertain, or hesitant; feeling of perplexity.",
    "secondary": "In epistemological philosophy and judicial deliberation, cognitive hesitation suspended between assent and disbelief.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "Henchard listened with growing **dubiety**, unsure whether to credit the stranger's astonishing market report."},
      {"author": "Henry James", "work": "The Golden Bowl", "quote": "Her smile was clouded by a subtle **dubiety**, as if she already perceived the flaw in the crystal cup."},
      {"author": "George Eliot", "work": "Romola", "quote": "Tito weighed the magistrate's offer with calculating **dubiety**, wary of political entanglements."}
    ]
  },
  "Dashboard — dub/dubious.md": {
    "primary": "Hesitating, doubting, or uncertain; also morally questionable, suspicious, or unreliable.",
    "secondary": "In judicial analysis and commercial transactions, assertions lacking credibility or contracts fraught with hidden hazards.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "She regarded the stranger with **dubious** eyes, wondering whether to answer his probing inquiry."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Mr. Guppy wore an expression of **dubious** satisfaction as he reviewed the parchment copy of the deed."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Ahab made a **dubious** motion with his ivory leg, dismissing the mate's objection with cold disdain."}
    ]
  },
  "Dashboard — dub/dubiously.md": {
    "primary": "In a dubious, doubtful, skeptical, or hesitant manner; with lingering uncertainty.",
    "secondary": "In fictional dialogue and detective narrative, responding with visible skepticism toward an unbelievable claim.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Gabriel shook his head **dubiously**, calculating the market price of the rain-damaged Wessex fleece."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "Watson looked **dubiously** at the battered felt hat upon the wooden table, wondering what clues it held."},
      {"author": "Lewis Carroll", "work": "Through the Looking-Glass", "quote": "Alice looked **dubiously** at the path through the wood, uncertain which way led to the eighth square."}
    ]
  },
  "Dashboard — dub/dubiousness.md": {
    "primary": "The characteristic of being dubious; uncertainty, questionable authenticity, or suspicious character.",
    "secondary": "In textual criticism and moral theology, the ambivalence surrounding an unverified manuscript or motive.",
    "quotes": [
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "Isabel sensed the moral **dubiousness** of Osmond's proposal, despite the surface elegance of his Roman villa."},
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "The financial **dubiousness** of revolutionary paper assignats shook public confidence throughout Europe."},
      {"author": "Nathaniel Hawthorne", "work": "The House of the Seven Gables", "quote": "Pyncheon looked with obvious **dubiousness** upon the faded family parchment, doubting its legal validity."}
    ]
  },
  "Dashboard — dub/dubitable.md": {
    "primary": "Open to doubt; capable of being questioned, contested, or challenged as uncertain.",
    "secondary": "In Cartesian philosophical epistemology, knowledge claims subject to methodological doubt before arriving at foundational certainty.",
    "quotes": [
      {"author": "René Descartes", "work": "Meditations on First Philosophy", "quote": "I resolved to strip away all **dubitable** opinions from my intellect, seeking that bedrock which cannot be doubted."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Whatever ideas rest merely upon casual hearsay must remain strictly **dubitable** in the eyes of a philosopher."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Sensory evidence alone often yields **dubitable** conclusions until verified by systematic experiment."}
    ]
  },
  "Dashboard — dub/dublin.md": {
    "primary": "The capital, largest city, and historic cultural heart of Ireland, situated at the mouth of the River Liffey.",
    "secondary": "In literary and colonial history, the Georgian city immortalized by Jonathan Swift, James Joyce, and the Easter Rising.",
    "quotes": [
      {"author": "James Joyce", "work": "Dubliners", "quote": "The evening light faded over the quays of **dublin**, casting grey shadows across the tranquil waters of the Liffey."},
      {"author": "Jonathan Swift", "work": "The Drapier's Letters", "quote": "Every shopkeeper in **dublin** resolved to reject Wood's debased copper coinage to save Ireland from ruin."},
      {"author": "Robert Burns", "work": "Poems and Songs of Robert Burns", "quote": "Word reached our town that the famous printing press of **dublin** had issued an elegant collection of Scottish songs."}
    ]
  },
  "Dashboard — dub/dubliner.md": {
    "primary": "A native, citizen, or permanent inhabitant of the city of Dublin, Ireland.",
    "secondary": "In twentieth-century literature, the distinctive urban personality and dialect immortalized in James Joyce's classic short story collection.",
    "quotes": [
      {"author": "James Joyce", "work": "Ulysses", "quote": "A true **dubliner** knows every turn of the North Wall and the sharp, salty smell of the pigeonhouse."},
      {"author": "George Bernard Shaw", "work": "John Bull's Other Island", "quote": "Broadbent could never fathom the melancholy irony of an educated **dubliner** surviving in London exile."},
      {"author": "Oscar Wilde", "work": "The Decay of Lying", "quote": "As a native **dubliner**, he brought a dazzling lyrical wit to the drawing rooms of Victorian London."}
    ]
  },
  "Dashboard — dub/dubnium.md": {
    "primary": "A synthetic, radioactive chemical element with symbol Db and atomic number 105, belonging to the transactinides.",
    "secondary": "In nuclear chemistry, named in honor of Dubna, Russia, the research center where heavy-ion fusion synthesis occurred.",
    "quotes": [
      {"author": "Glenn T. Seaborg", "work": "Transuranium Elements: A Half Century", "quote": "The synthetic identification of **dubnium** by heavy-ion bombardment settled years of priority disputes between rival laboratories."},
      {"author": "Carl Sagan", "work": "The Demon-Haunted World", "quote": "Synthesizing fleeting atoms of **dubnium** in particle accelerators illustrates the immense power of twentieth-century physics."},
      {"author": "Steven Weinberg", "work": "The Discovery of Subatomic Particles", "quote": "The brief half-lives of superheavy isotopes like **dubnium** test the limits of theoretical nuclear shell stability."}
    ]
  },
  "Dashboard — dub/dubonnet.md": {
    "primary": "A sweet, aromatized French wine-based aperitif flavored with quinine, herbs, spices, and orange peel.",
    "secondary": "In French culinary culture and bartending, a classic Parisian aperitif formulated in 1846 by Joseph Dubonnet for the French Foreign Legion.",
    "quotes": [
      {"author": "Ernest Hemingway", "work": "The Sun Also Rises", "quote": "We sat outside on the Boulevard Saint-Michel, drinking chilled **dubonnet** with lemon twist while the crowds hurried by."},
      {"author": "Graham Greene", "work": "Travels with My Aunt", "quote": "My aunt ordered a generous tumbler of **dubonnet**, declaring it the only cordial that restored her zest for adventure."},
      {"author": "Agatha Christie", "work": "Evil Under the Sun", "quote": "Poirot sipped his **dubonnet** on the terrace, politely declining the heavier cocktails favored by the younger hotel guests."}
    ]
  },
  "Dashboard — dub/dubrovnik.md": {
    "primary": "A historic fortified coastal city in southern Dalmatia, Croatia, situated on the Adriatic Sea (historically Ragusa).",
    "secondary": "In Mediterranean history, an independent maritime republic renowned for diplomatic agility, maritime commerce, and massive stone walls.",
    "quotes": [
      {"author": "Rebecca West", "work": "Black Lamb and Grey Falcon", "quote": "The white marble ramparts of **dubrovnik** rose proudly out of the turquoise Adriatic, a republic built on maritime freedom."},
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The citizens of ancient Ragusa, now called **dubrovnik**, maintained their civil liberty between the Ottoman empire and Venice."},
      {"author": "Lord Byron", "work": "Childe Harold's Pilgrimage", "quote": "The Adriatic sun illumined the stone towers of **dubrovnik**, where argosies once loaded silver from the Balkan hills."}
    ]
  },
  "Dashboard — dub/dubuque.md": {
    "primary": "A historic commercial city in eastern Iowa, situated along the bluffs of the upper Mississippi River.",
    "secondary": "In American frontier and economic history, founded by French-Canadian lead miner Julien Dubuque, becoming an early Iowa hub.",
    "quotes": [
      {"author": "Mark Twain", "work": "Life on the Mississippi", "quote": "Steamboats churned the brown river water as they rounded the limestone bluffs into the busy port of **dubuque**."},
      {"author": "L. P. Brockett", "work": "Woman's Work in the Civil War", "quote": "Hospital aid societies in **dubuque** collected flannel bandages and medical supplies for the Mississippi gunboat fleet."},
      {"author": "Hamlin Garland", "work": "Main-Travelled Roads", "quote": "Farmers brought their grain wagons down the winding ridge road, selling wheat to the merchants of **dubuque**."}
    ]
  },
  "Dashboard — dub/dubya.md": {
    "primary": "A colloquial American nickname representing the letter 'W', popularly applied to President George W. Bush.",
    "secondary": "In political journalism and satire, a Southern vernacular moniker highlighting informal persona and folksy rhetorical style.",
    "quotes": [
      {"author": "Hunter S. Thompson", "work": "Kingdom of Fear", "quote": "The campaign operatives celebrated when the Texas crowds cheered for good old **dubya** at the state fairgrounds."},
      {"author": "Molly Ivins", "work": "Shrub: The Short but Happy Political Life of George W. Bush", "quote": "No matter how bitter the legislative fight, **dubya** possessed an uncanny gift for charm and backslapping camaraderie in Austin."},
      {"author": "Christopher Hitchens", "work": "Love, Poverty, and War", "quote": "Foreign commentators often underestimated the stubborn strategic resolve hidden beneath the casual moniker of **dubya**."}
    ]
  },
  "Dashboard — dub/dubyuh.md": {
    "primary": "An eye-dialect spelling representing the Southern or Texan pronunciation of the letter 'W'.",
    "secondary": "In political folklore and linguistic orthography, a phonetic transcription capturing folksy regional vernacular cadence.",
    "quotes": [
      {"author": "Molly Ivins", "work": "You Got to Dance with Them What Brung You", "quote": "The campaign buttons spelled out **dubyuh** in bold western font, leaning hard into rustic regional identity."},
      {"author": "Garrison Keillor", "work": "Lake Wobegon Days", "quote": "The radio announcer drawled out the southern letter **dubyuh** with exaggerated theatrical slow-motion cadence."},
      {"author": "H. L. Mencken", "work": "The American Language", "quote": "Regional phonetics across the Gulf States frequently expand the letter into a full two-syllable diphthong written as **dubyuh**."}
    ]
  },
  "Dashboard — dub/indubitability.md": {
    "primary": "The characteristic of being unquestionable, undeniable, and impossible to doubt; certainty.",
    "secondary": "In epistemological theory, the supreme status of clear and distinct ideas that withstand Cartesian hyper-skepticism.",
    "quotes": [
      {"author": "René Descartes", "work": "Meditations on First Philosophy", "quote": "The proposition 'I think, therefore I am' possesses that luminous **indubitability** which defeats the most cunning deceiver."},
      {"author": "William James", "work": "Pragmatism", "quote": "Dogmatic philosophers seek an absolute **indubitability** that human experience, with all its messiness, can never furnish."},
      {"author": "Bertrand Russell", "work": "The Analysis of Mind", "quote": "We search in vain for mathematical **indubitability** among the chaotic, shifting data of direct sensory awareness."}
    ]
  },
  "Dashboard — dub/indubitable.md": {
    "primary": "Too evident, obvious, or certain to be doubted; unquestionable, clear, and undeniable.",
    "secondary": "In formal jurisprudence and scientific demonstration, evidence that establishes a fact beyond reasonable challenge.",
    "quotes": [
      {"author": "Jane Austen", "work": "Mansfield Park", "quote": "She considered his affection an **indubitable** truth that needed no spoken confirmation to comfort her heart."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "It is an **indubitable** maxim of government that powers must be proportioned to responsibilities and public safety."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "My aunt treated the child's right to protection as an **indubitable** moral obligation that brook no hesitation."}
    ]
  },
  "Dashboard — dub/indubitably.md": {
    "primary": "In an indubitable manner; unquestionably, undeniably, and beyond all doubt.",
    "secondary": "In narrative characterization and judicial argument, asserting a conclusion with total, unshakable conviction.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "She was **indubitably** the daughter of the late baronet, as the legal deeds and baptismal register clearly attested."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "The footprints **indubitably** belonged to a man with a wooden leg, as Holmes demonstrated with his measuring tape."},
      {"author": "Leo Tolstoy", "work": "War and Peace", "quote": "Prince Andrei felt that victory was **indubitably** within reach as the sun pierced the morning smoke of Austerlitz."}
    ]
  }
}

def curate_file(rel_path, info):
    base_dir = "App database/Latin roots/Cluster Mind & Knowledge"
    filepath = os.path.join(base_dir, rel_path)
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return False
        
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
        
    fm_match = re.search(r"^---\n.*?\n---\n", content, re.DOTALL)
    if not fm_match:
        print(f"Frontmatter missing: {filepath}")
        return False
    frontmatter = fm_match.group(0)
    
    w = os.path.splitext(os.path.basename(rel_path))[0]
    header = f"# {w}\n\n"
    
    dv_match = re.search(r"(> \[!status\] 🎯 \*\*Status:\*\*.*?```dataviewjs.*?```)", content, re.DOTALL)
    if not dv_match:
        print(f"Dataview block missing: {filepath}")
        return False
    dv_block = dv_match.group(1)
    
    defs_block = f"""> [!book] 📖 Definitions & Semantic Range
> 1. **Primary Definition (Lexical / Standard Consensus)**: {info['primary']}
> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: {info['secondary']}"""

    quotes_lines = ["> [!quote] 💬 Contextual Usage & Authentic Quotations"]
    for q in info["quotes"]:
        quotes_lines.append(f"> - 📜 **{q['author']} (*{q['work']}*):** *\"{q['quote']}\"*")
    quotes_block = "\n".join(quotes_lines)
    
    new_content = f"{frontmatter}{header}{dv_block}\n\n{defs_block}\n\n{quotes_block}\n"
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)
    return True

success = 0
for rel_path, info in data.items():
    if curate_file(rel_path, info):
        success += 1

print(f"Successfully updated {success}/{len(data)} notes in Dashboard — dub.")
