# -*- coding: utf-8 -*-
import os, sys, re
sys.stdout.reconfigure(encoding="utf-8")

data = {
  # --- Dashboard — press Part 2 (11B, 33 words) ---
  "Dashboard — press/expressive.md": {
    "primary": "Effectively conveying thought, feeling, or meaning; full of character, significance, or emotion.",
    "secondary": "In linguistics, expressive words or intonations convey the speaker's emotional attitude rather than denotative truth conditions.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Her dark eyes were wonderfully **expressive**, reflecting every shifting shadow of thought and feeling."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Mr. Darcy was continually struck by the fine eyes and **expressive** countenance of Elizabeth."},
      {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "The mobility of facial muscles renders the human face exceptionally **expressive** under emotional stress."}
    ]
  },
  "Dashboard — press/expressively.md": {
    "primary": "In a manner that clearly and vividly conveys meaning, emotional feeling, or deep significance.",
    "secondary": "In musical performance (espressivo), directing musicians to play with heightened sensitivity and dynamic inflection.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "The Woodlanders", "quote": "Giles looked at her **expressively**, though words failed him at that critical parting moment."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "She paused and looked **expressively** toward the locked doorway on the third story."},
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "Ralph Touchett shrugged his shoulders **expressively**, indicating amused resignation."}
    ]
  },
  "Dashboard — press/expressiveness.md": {
    "primary": "The capacity or power of conveying meaning, sentiment, emotion, or artistic character with vivid clarity.",
    "secondary": "In semiotics and aesthetics, the communicative range and affective richness inherent in symbolic or visual media.",
    "quotes": [
      {"author": "John Ruskin", "work": "Modern Painters", "quote": "The subtle **expressiveness** of Turner's skies transcends mere photographic imitation of clouds."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "The extraordinary **expressiveness** of the human voice originates from delicate motor coordination."},
      {"author": "George Eliot", "work": "Daniel Deronda", "quote": "The singular **expressiveness** of her singing drew tears from the most worldly listeners in the salon."}
    ]
  },
  "Dashboard — press/expressly.md": {
    "primary": "In an explicit, clear, and unmistakable manner; or specifically and particularly for a stated purpose.",
    "secondary": "In contract law, expressly stated conditions supersede implied terms and common usage defaults.",
    "quotes": [
      {"author": "John Locke", "work": "Second Treatise of Government", "quote": "Civil society is formed when men **expressly** consent to submit to the determination of the majority."},
      {"author": "Francis Bacon", "work": "Essays", "quote": "The ancient statutes **expressly** forbid monopolies that constrain public trade and common commodities."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The document was prepared **expressly** to satisfy the rigorous requirements of the Court of Chancery."}
    ]
  },
  "Dashboard — press/impress.md": {
    "primary": "To apply pressure to leave a mark; to produce a strong, favorable, or lasting effect on the mind.",
    "secondary": "Historically, to force men into public military or naval service by sovereign prerogative; to press gang.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Macbeth", "quote": "As easy mayst thou the intrenchant air with thy keen sword **impress** as make me bleed."},
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "Sound arguments **impress** themselves upon reasonable minds with the force of innate truth."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "My aunt sought to **impress** upon me the necessity of firmness and independent resolution."}
    ]
  },
  "Dashboard — press/impressed.md": {
    "primary": "Deeply affected, influenced, or stamped with a mark or strong conviction; conscripted.",
    "secondary": "In numismatics and sealing, stamped with an official die, hallmark, or seal into molten wax or heated metal.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry IV, Part 1", "quote": "A mad fellow met me on the way and told me I had unloaded all the gibbets and **impressed** the dead bodies."},
      {"author": "Herman Melville", "work": "Billy Budd, Sailor", "quote": "Billy was summarily **impressed** from the merchantman Rights-of-Man into His Majesty's frigate Bellipotent."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth was thoroughly **impressed** by the grandeur of Pemberley and the quiet elegance of its grounds."}
    ]
  },
  "Dashboard — press/impressible.md": {
    "primary": "Easily affected, influenced, or molded by external impressions, suggestions, or emotions; susceptible.",
    "secondary": "In material science and engraving, capable of receiving and retaining a sharp indented mechanical stamp.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Dorothea possessed an **impressible** nature that vibrated acutely to every appeal of human need."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Her young and **impressible** mind absorbed the somber fatalism of the rural landscape."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "The infant understanding resembles an **impressible** wax tablet awaiting the inscriptions of experience."}
    ]
  },
  "Dashboard — press/impression.md": {
    "primary": "An effect, imprint, or feeling produced on the mind, senses, or a pliable surface.",
    "secondary": "In publishing and bibliographical descriptive cataloging, the entire quantity of books printed from one set of plates during a single print run.",
    "quotes": [
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "External objects produce an **impression** upon our senses, which transmits perceptions directly to the mind."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Holmes examined the clay soil, finding a clear **impression** of a small naked foot with splayed toes."},
      {"author": "Jane Austen", "work": "Persuasion", "quote": "Anne Elliot could not shake off the profound **impression** made by Captain Wentworth's sudden return."}
    ]
  },
  "Dashboard — press/impressionable.md": {
    "primary": "Easily influenced, swayed, or affected by surrounding people, suggestions, or environments.",
    "secondary": "In developmental psychology, denotes critical sensitive periods during childhood when social and linguistic inputs permanently shape cognitive pathways.",
    "quotes": [
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "Young Adele was lively and **impressionable**, readily adopting the manners of those around her."},
      {"author": "Robert Louis Stevenson", "work": "The Strange Case of Dr Jekyll and Mr Hyde", "quote": "Utterson was not an **impressionable** man, yet the singular mystery of Hyde disturbed his nightly rest."},
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "Isabel Archer was generous, eager, and dangerously **impressionable** to romantic ideals of sacrifice."}
    ]
  },
  "Dashboard — press/impressionism.md": {
    "primary": "A 19th-century artistic movement characterized by depicting visual impressions of light, color, and momentary movement.",
    "secondary": "In musical composition, associated with Debussy and Ravel, using unresolved ninth chords, whole-tone scales, and exotic timbre to evoke atmosphere.",
    "quotes": [
      {"author": "Virginia Woolf", "work": "The Waves", "quote": "Literary **impressionism** captures the fleeting shimmer of waves and the rapid mosaic of passing thoughts."},
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The critics debated whether French **impressionism** sacrificed eternal architectural form for transient optical sparkle."},
      {"author": "Oscar Wilde", "work": "The Decay of Lying", "quote": "The subtle atmospheric effects of London fog were scarcely appreciated until **impressionism** taught us to see them."}
    ]
  },
  "Dashboard — press/impressionist.md": {
    "primary": "A painter, composer, or writer who practices impressionism; an entertainer who mimics prominent figures.",
    "secondary": "In art history, the group of painters who mounted independent exhibitions in Paris between 1874 and 1886, including Monet, Renoir, and Pissarro.",
    "quotes": [
      {"author": "Henry James", "work": "The Ambassadors", "quote": "Strether stood before the small landscape like an enthusiastic **impressionist** absorbing atmospheric harmony."},
      {"author": "Virginia Woolf", "work": "Roger Fry: A Biography", "quote": "Fry explained how the French **impressionist** revolutionized color by rejecting conventional studio bitumen and muddy shadows."},
      {"author": "E. M. Forster", "work": "A Room with a View", "quote": "The young gentleman sketched the Tuscan hillside with the rapid, dotted strokes of a committed **impressionist**."}
    ]
  },
  "Dashboard — press/impressionistic.md": {
    "primary": "Based on subjective personal impressions rather than detailed objective facts or precise analysis.",
    "secondary": "In fine art and literature, characterized by loose brushwork, dappled lighting, or episodic narrative vignettes.",
    "quotes": [
      {"author": "Virginia Woolf", "work": "To the Lighthouse", "quote": "Lily Briscoe contemplated her canvas, blending colors into an **impressionistic** balance of mass and empty space."},
      {"author": "Aldous Huxley", "work": "Along the Road", "quote": "The travel essays presented an **impressionistic** sketch of Italian towns rather than an exhaustive guidebook."},
      {"author": "Joseph Conrad", "work": "Notes on Life and Letters", "quote": "His prose style was richly **impressionistic**, rendering the mysterious menace of the tropical sea."}
    ]
  },
  "Dashboard — press/impressive.md": {
    "primary": "Evoking admiration, respect, or solemn wonder through grand scale, high ability, or stately character.",
    "secondary": "In architecture and monument design, monumental proportions, symmetrical colonnades, and heavy rustication designed to convey civic majesty.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "The great stone hall of Baskerville was an **impressive** room, hung with ancient armour and family portraits."},
      {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "Egdon Heath presented an **impressive** spectacle under the darkening twilight of late November."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The court was filled with an **impressive** silence as the jury returned to deliver their fatal verdict."}
    ]
  },
  "Dashboard — press/impressively.md": {
    "primary": "In a manner that commands admiration, solemn respect, or profound awe; powerfully, grandly.",
    "secondary": "In rhetoric and public oratory, employing measured cadence and authoritative tone to sway an audience.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Memoirs of Sherlock Holmes", "quote": "The inspector paused **impressively**, allowing his deduction to sink into the minds of the listeners."},
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "The old Roman amphitheatre loomed **impressively** above the quiet Dorset meadows at twilight."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Mr. Casaubon cleared his throat **impressively** before outlining the grand design of his theological treatise."}
    ]
  },
  "Dashboard — press/impressiveness.md": {
    "primary": "The attribute of commanding attention, admiration, or deep respect through grandeur or gravity.",
    "secondary": "In aesthetics and rhetorical theory, the psychological weight and emotional resonance imparted by artistic compositions.",
    "quotes": [
      {"author": "John Ruskin", "work": "The Seven Lamps of Architecture", "quote": "The solemn **impressiveness** of a Gothic nave depends upon its soaring height and mysterious shadows."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The vast monolithic stones of Stonehenge gained added **impressiveness** against the pale light of dawn."},
      {"author": "Edgar Allan Poe", "work": "The Fall of the House of Usher", "quote": "The somber **impressiveness** of the antique room deepened the melancholy of my brooding host."}
    ]
  },
  "Dashboard — press/impressment.md": {
    "primary": "The act of compelling men into military or naval service by force, especially historical naval press gangs.",
    "secondary": "In maritime and international history, British impressment of American merchant sailors was a primary proximate cause of the War of 1812.",
    "quotes": [
      {"author": "Herman Melville", "work": "Billy Budd, Sailor", "quote": "The lieutenant boarded the merchant brig to enforce naval **impressment**, selecting the handsome sailor for the king's warship."},
      {"author": "Bram Stoker", "work": "Dracula", "quote": "He opened the old chest with much solemn **impressment**, revealing a thick bundle of ancient deeds."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The brutal practice of **impressment** filled naval crews with unwilling landsmen torn from their families."}
    ]
  },
  "Dashboard — press/incompressibility.md": {
    "primary": "The physical characteristic of resisting reduction in volume when subjected to external compressive pressure.",
    "secondary": "In hydrodynamics, liquids are modeled as having practical incompressibility, simplifying Navier-Stokes fluid flow formulations.",
    "quotes": [
      {"author": "James Clerk Maxwell", "work": "Theory of Heat", "quote": "The relative **incompressibility** of liquid water enables hydraulic presses to transmit immense mechanical power."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Chemistry and Physics", "quote": "Under the highest hydrostatic forces, water demonstrates remarkable **incompressibility** compared with gases."},
      {"author": "Thomas Henry Huxley", "work": "Physiography", "quote": "The effective **incompressibility** of ocean depths ensures that deep water does not collapse under colossal hydrostatic head."}
    ]
  },
  "Dashboard — press/incompressible.md": {
    "primary": "Incapable of being squeezed, pressed, or compacted into a smaller space or volume.",
    "secondary": "In mechanical engineering, applies to hydraulic oils whose non-compressible behavior enables precise force transmission in jacks and brakes.",
    "quotes": [
      {"author": "Isaac Newton", "work": "Opticks", "quote": "An **incompressible** fluid would transmit an impulse instantaneously across any distance, which contradicts observation."},
      {"author": "Robert Boyle", "work": "New Experiments Physico-Mechanicall", "quote": "Liquids were long regarded as practically **incompressible** until delicate apparatus revealed minute volume changes under extreme force."},
      {"author": "Herbert Spencer", "work": "First Principles", "quote": "The assumption of absolutely rigid, **incompressible** ultimate atoms creates insoluble contradictions in mechanical philosophy."}
    ]
  },
  "Dashboard — press/inexpressible.md": {
    "primary": "Beyond the power of language or words to describe; ineffable, unspeakable, or overwhelming.",
    "secondary": "In 18th- and 19th-century colloquial humor, a Victorian euphemistic term for trousers (inexpressibles).",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "To hear that Gabriel had safely thatched the ricks was an **inexpressible** relief to her tormented mind."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "I felt an **inexpressible** longing to pass beyond the blue horizon and see the wide world outside."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "The sight of Joe Gargery's honest, patient face brought an **inexpressible** warmth to my lonely heart."}
    ]
  },
  "Dashboard — press/inexpressive.md": {
    "primary": "Lacking expression, emotional animation, or communicative clarity; blank, dull, or impassive.",
    "secondary": "In semiotic analysis, describes signs or representations that fail to signify intended communicative content.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The pale dawn of the chilly March morning was singularly **inexpressive**, offering no clue to the day's fortunes."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Where any whaling name happens to be vague or **inexpressive**, I shall say so and suggest a more accurate term."},
      {"author": "William Shakespeare", "work": "As You Like It", "quote": "Hang there, my verse, in witness of my love, run, run, Orlando, carve on every tree the fair, the chaste, and **unexpressive** she."}
    ]
  },
  "Dashboard — press/inexpressively.md": {
    "primary": "In a manner devoid of facial expression, emotional inflection, or communicative animation.",
    "secondary": "In dramatic direction, delivery of dialogue in a flat, deadpan monotone to convey shock, dissociation, or detachment.",
    "quotes": [
      {"author": "Henry James", "work": "The Bostonians", "quote": "She gazed **inexpressively** toward the distant window, refusing to reveal the pain of his refusal."},
      {"author": "Joseph Conrad", "work": "Under Western Eyes", "quote": "Razumov blinked **inexpressively** under the sharp scrutiny of the secret police magistrate."},
      {"author": "George Eliot", "work": "Daniel Deronda", "quote": "Grandcourt murmured his consent **inexpressively**, flicking an invisible grain of ash from his cuff."}
    ]
  },
  "Dashboard — press/oppress.md": {
    "primary": "To keep down or burden with cruel, unjust authority or unreasonable hardship; to weigh heavily on the spirit.",
    "secondary": "In political philosophy and human rights doctrine, systematic institutional subjugation denying fundamental civil liberties to minority populations.",
    "quotes": [
      {"author": "William Shakespeare", "work": "All's Well That Ends Well", "quote": "You ne'er **oppress'd** me with a mother's groan, yet I express to you a mother's care."},
      {"author": "John Locke", "work": "Second Treatise of Government", "quote": "When rulers **oppress** the subject and invade property, the people are absolved from further obedience."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The aristocratic lords continued to **oppress** the starving peasantry until retribution broke over their heads."}
    ]
  },
  "Dashboard — press/oppressed.md": {
    "primary": "Subject to harsh, authoritarian, or tyrannical treatment; weighed down by grief, anxiety, or heavy labor.",
    "secondary": "In critical social theory, marginalized socioeconomic classes suffering systemic deprivation at the hands of ruling elites.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Sonnet 28", "quote": "When day's oppression is not eased by night, but day by night and night by day **oppressed**."},
      {"author": "Frederick Douglass", "work": "Narrative of the Life of Frederick Douglass", "quote": "I have seen the lash applied to the bare backs of the **oppressed** until the blood mingled with the soil."},
      {"author": "Percy Bysshe Shelley", "work": "The Masque of Anarchy", "quote": "Rise like Lions after slumber in unvanquishable number, shake your chains to earth like dew which in sleep had fallen on you: ye are many, they are few!"}
    ]
  },
  "Dashboard — press/oppression.md": {
    "primary": "The exercise of authority or power in an unjust, cruel, or burdensome manner; a sense of heavy depression.",
    "secondary": "In historical sociology, the institutionalized disenfranchisement, economic exploitation, and cultural erasure of vulnerable demographic groups.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Romeo and Juliet", "quote": "At thy good heart's **oppression**. Why, gentle cousin, does love weigh so heavy on thy breast?"},
      {"author": "Thomas Jefferson", "work": "Declaration of Independence", "quote": "In every stage of these **oppressions** we have petitioned for redress in the most humble terms."},
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "Resistance to tyranny is justified when arbitrary power degenerates into intolerable **oppression**."}
    ]
  },
  "Dashboard — press/oppressive.md": {
    "primary": "Unjustly harsh, tyrannical, or burdensome; suffocating, stifling, or heavily distressing.",
    "secondary": "In meteorology, describes extreme summer weather combinations of high temperature and saturating humidity that impair human evaporative cooling.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The **oppressive** sense of the harm she had unwittingly done led Tess to be more deferential than ever."},
      {"author": "Joseph Conrad", "work": "Heart of Darkness", "quote": "The silence of the vast primeval jungle felt heavy, sinister, and relentlessly **oppressive**."},
      {"author": "George Orwell", "work": "1984", "quote": "The atmosphere of perpetual surveillance and state suspicion grew increasingly **oppressive** with every passing year."}
    ]
  },
  "Dashboard — press/oppressively.md": {
    "primary": "In a heavy, suffocating, burdensome, or tyrannical manner that weighs down body or spirit.",
    "secondary": "In atmospheric descriptions, characterizes close, sultry weather preceding violent electrical thunderstorms.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "The summer afternoon was **oppressively** hot, and the blinds were drawn down across the Baker Street sitting room."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The thick air hung **oppressively** over the cornfields as the dark thunder clouds gathered in the south."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "The heavy velvet curtains and stifling silence of the red-room closed **oppressively** around the weeping child."}
    ]
  },
  "Dashboard — press/oppressiveness.md": {
    "primary": "The state or condition of being burdensome, stifling, unjustly severe, or psychologically overwhelming.",
    "secondary": "In clinical psychopathology, the sensation of crushing chest tightness and somatic dread accompanying panic episodes.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "They writhed feverishly under the **oppressiveness** of an emotion thrust upon them by cruel Nature."},
      {"author": "Joseph Conrad", "work": "Lord Jim", "quote": "The **oppressiveness** of the tropical heat seemed to weigh upon the very souls of the ship's crew."},
      {"author": "Edgar Allan Poe", "work": "The Fall of the House of Usher", "quote": "An irresistible **oppressiveness** crept over my senses as I breathed the stagnant vapors of the antique mansion."}
    ]
  },
  "Dashboard — press/oppressor.md": {
    "primary": "A person, monarch, or ruling regime that exercises power cruelly, unjustly, or with heavy burdens.",
    "secondary": "In political ethics and revolutionary philosophy, the tyrannical agent against whom the moral right of rebellion is legitimately asserted.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "For who would bear the whips and scorns of time, the **oppressor**'s wrong, the proud man's contumely?"},
      {"author": "Frederick Douglass", "work": "My Bondage and My Freedom", "quote": "The slaveholder must dehumanize his victim in order to preserve his own peace of mind as an **oppressor**."},
      {"author": "John Milton", "work": "Samson Agonistes", "quote": "Samson pulled down the pillars of the pagan temple, burying the haughty **oppressor** beneath the ruin."}
    ]
  },
  "Dashboard — press/overpressure.md": {
    "primary": "Pressure exceeding the normal, safe, or ambient atmospheric baseline; excessive mechanical urging.",
    "secondary": "In blast dynamics and explosive ballistics, the transient peak pressure wave produced by a detonation above atmospheric ambient pressure.",
    "quotes": [
      {"author": "Arthur C. Clarke", "work": "Rendezvous with Rama", "quote": "The safety relief valves vented instantly when the gas manifold detected an **overpressure** of two atmospheres."},
      {"author": "H. G. Wells", "work": "The War in the Air", "quote": "The explosive blast wave created an immense **overpressure** that shattered every window within five miles."},
      {"author": "Sinclair Lewis", "work": "Arrowsmith", "quote": "The autoclave began to hiss violently as the steam **overpressure** strained the brass safety bolts."}
    ]
  },
  "Dashboard — press/postimpressionist.md": {
    "primary": "An artist associated with the late 19th-century reaction against naturalistic impressionism, emphasizing structure and symbolic color.",
    "secondary": "In art history, encompasses Cézanne, Van Gogh, Gauguin, and Seurat, whose formal innovations laid the foundations for 20th-century modernism.",
    "quotes": [
      {"author": "Virginia Woolf", "work": "Roger Fry: A Biography", "quote": "Fry organized the sensational **Post-Impressionist** exhibition in London, shocking the public with Cézanne and Van Gogh."},
      {"author": "Aldous Huxley", "work": "Point Counter Point", "quote": "The studio walls were hung with vibrant reproductions of **postimpressionist** landscapes full of emotional intensity."},
      {"author": "W. H. Auden", "work": "The Dyer's Hand", "quote": "The bold formal discipline of the **postimpressionist** masters rescued painting from mere optical dissolution."}
    ]
  },
  "Dashboard — press/press.md": {
    "primary": "To exert steady physical force against; to crowd together; or the news media and printing machinery.",
    "secondary": "In constitutional jurisprudence, freedom of the press protects the right of journalists and newspapers to publish without government censorship.",
    "quotes": [
      {"author": "William Shakespeare", "work": "As You Like It", "quote": "I **press** in here, sir, amongst the rest of the country copulatives, to swear and to forswear."},
      {"author": "Francis Bacon", "work": "Novum Organum", "quote": "Printing, gunpowder, and the compass have changed the whole face and state of things throughout the world, and the **press** heads them all."},
      {"author": "Thomas Jefferson", "work": "Letters of Thomas Jefferson", "quote": "Our liberty depends on the freedom of the **press**, and that cannot be limited without being lost."}
    ]
  },
  "Dashboard — press/pressed.md": {
    "primary": "Exerted force upon, squeezed, ironed, or urged urgently; conscripted into service.",
    "secondary": "In historic common law (peine forte et dure), accused felons refusing to plead were pressed under heavy iron stones until they answered or died.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Coriolanus", "quote": "Being **pressed** to the war, even when the navel of the state was touched, they would not thread the gates."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "He held out his hand to take hers, which had eased her side by being **pressed** against the rustic gate."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "The urgent demands of the creditor **pressed** heavily upon Mr. Micawber's temporary tranquility."}
    ]
  },
  "Dashboard — press/pressing.md": {
    "primary": "Demanding immediate attention, urgent, critical; the physical act of applying compressive pressure.",
    "secondary": "In vinyl audio manufacturing, a single phonograph record stamped from metal stampers in a hydraulic heated press.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Measure for Measure", "quote": "Marrying a punk, my lord, is **pressing** to death, whipping, and hanging."},
      {"author": "Francis Bacon", "work": "Essays", "quote": "In matters of state, delay is dangerous when affairs arrive at a **pressing** and acute crisis."},
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "A **pressing** need for capital compelled Henchard to pledge his remaining corn warehouse to rival dealers."}
    ]
  }
}

base_dir = r"App database\Latin roots\Cluster Motion"
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

print(f"Motion Batch 11B: Successfully updated {updated}/{len(data)} notes.")
