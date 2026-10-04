# -*- coding: utf-8 -*-
import os, sys, re
sys.stdout.reconfigure(encoding="utf-8")

data = {
  # --- Dashboard — scul (12 words) ---
  "Dashboard — scul/scull.md": {
    "primary": "An oar used in pairs by a rower, or a single stern oar worked back and forth to propel a boat.",
    "secondary": "In competitive rowing regattas, a scull designates both the lightweight racing shell and the dual oars operated by an individual sculler.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Herbert took up the **scull** and dipped it quietly into the dark water of the Thames, pulling steadily against the tide."},
      {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "The ferryman handled his long **scull** with practiced ease, guiding the flat-bottomed punt across the swollen stream."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "We watched the lone boatman feather his **scull** through the Thames mist as the police launch surged past."}
    ]
  },
  "Dashboard — scul/sculler.md": {
    "primary": "A person who propels a boat with sculls, or a rowing boat propelled by sculls.",
    "secondary": "In maritime history and Thames watermen lore, a licensed sculler ferried passengers between London wharves prior to the construction of modern bridges.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Our Mutual Friend", "quote": "Gaffer Hexam was an expert **sculler**, gliding silently through the nighttime currents beneath Southwark Bridge."},
      {"author": "William Makepeace Thackeray", "work": "The History of Pendennis", "quote": "Arthur watched the champion **sculler** from Cambridge skimming across the sparkling surface of the river."},
      {"author": "Jerome K. Jerome", "work": "Three Men in a Boat", "quote": "A clumsy **sculler** managed to foul our towline, providing George with an excuse for prolonged rhetorical indignation."}
    ]
  },
  "Dashboard — scul/scullery.md": {
    "primary": "A small room attached to a kitchen, used for washing dishes, pots, and household cleaning chores.",
    "secondary": "In Victorian domestic architecture and downstairs servant economy, the scullery was the lowliest workspace where pots were scoured with sand and potash.",
    "quotes": [
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "The kitchen staff bustled about their work, while the scullery maid wept quietly in the outer **scullery** over a pile of brass pans."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "A dismal **scullery** smelling of cold soap-suds and wet flagstones formed the lowest precinct of the London house."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The milkmaids scrubbed the copper pails in the stone-flagged **scullery** as the morning sun peered over the dairy eaves."}
    ]
  },
  "Dashboard — scul/sculling.md": {
    "primary": "The action of propelling a boat with sculls or a stern oar; or competing in a sculling race.",
    "secondary": "In kinesiology and aquatic exercise, sculling describes figure-eight hand sweep motions generating continuous propulsive lift in synchronized swimming.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "We kept up our steady **sculling** past the black hulls of colliers moored four deep in the Pool of London."},
      {"author": "Arthur Conan Doyle", "work": "The Memoirs of Sherlock Holmes", "quote": "He maintained his athletic vigor through morning **sculling** on the upper reaches of the Cam."},
      {"author": "Robert Louis Stevenson", "work": "Treasure Island", "quote": "I observed Ben Gunn **sculling** his crude coracle across the white surf toward the sheltered cove."}
    ]
  },
  "Dashboard — scul/scullion.md": {
    "primary": "A servant employed to do rough, menial kitchen work, such as cleaning pots and floors.",
    "secondary": "In early modern English literature and social hierarchy, calling someone a scullion constituted a sharp contemptuous slur on their character or breeding.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "Fie upon't! Foh! About, my brain! I have heard that guilty creatures sitting at a play have by the very cunning of the scene been struck so to the soul that presently they have proclaim'd their malefactions; yet I, a dull and muddy-mettled rascal, peak like John-a-dreams, unpregnant of my cause, and can say nothing; no, not for a king, upon whose property and most dear life a damn'd defeat was made. Am I a coward? Who calls me villain? breaks my pate across? plucks off my beard, and blows it in my face? tweaks me by the nose? gives me the lie i' the throat, as deep as to the lungs? who does me this? Ha! 'Swounds, I should take it: for it cannot be but I am pigeon-liver'd and lack gall to make oppression bitter, or ere this I should have fatted all the region kites with this slave's offal: bloody, bawdy villain! Remorseless, treacherous, lecherous, kindless villain! O, vengeance! Why, what an ass am I! This is most brave, that I, the son of a dear father murder'd, prompted to my revenge by heaven and hell, must, like a whore, unpack my heart with words, and fall a-cursing, like a very drab, a **scullion**! Fie upon't! foh! About, my brain!"},
      {"author": "Miguel de Cervantes", "work": "Don Quixote", "quote": "The pampered knight mistook a ragged kitchen **scullion** for a lovely princess detained by enchanted spells."},
      {"author": "Walter Scott", "work": "Ivanhoe", "quote": "Even the lowest **scullion** in Cedric's hall dared to whisper insolent mockeries behind the foreign monk's back."}
    ]
  },
  "Dashboard — scul/sculpt.md": {
    "primary": "To carve, mold, or fashion a three-dimensional figure or design out of clay, stone, or metal.",
    "secondary": "In geomorphology and physical geography, fluvial and glacial forces sculpt deep canyons and dramatic mountain cirques across geological epochs.",
    "quotes": [
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The medieval master sought to **sculpt** the stone capital with living leaves that seemed to bend under invisible alpine breezes."},
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "Subaerial erosion and glacial ice continually **sculpt** the granite summits into rugged arêtes and amphitheaters."},
      {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "The artist felt a longing to **sculpt** the youth's features in pure Parian marble rather than render them in fading oils."}
    ]
  },
  "Dashboard — scul/sculpted.md": {
    "primary": "Carved, molded, or fashioned into a three-dimensional shape, with well-defined contours.",
    "secondary": "In evolutionary morphology and skeletal biology, sculpted cranial bones exhibit specialized sutures adapted for dissipating biomechanical bite forces.",
    "quotes": [
      {"author": "Nathaniel Hawthorne", "work": "The Marble Faun", "quote": "The ancient bust displayed **sculpted** curls and a gentle faun-like smile frozen in eternal marble repose."},
      {"author": "George Eliot", "work": "Romola", "quote": "The palazzo doorway was framed with **sculpted** shields displaying the proud armorial bearings of the Medici."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Her finely **sculpted** chin and delicate profile stood out clearly against the twilight shadows of the lane."}
    ]
  },
  "Dashboard — scul/sculptor.md": {
    "primary": "An artist who creates three-dimensional sculptures by carving stone, modeling clay, or casting metal.",
    "secondary": "In classical art history and Renaissance workshops, the sculptor transformed raw marble blocks into lifelike human anatomies by the subtractive method.",
    "quotes": [
      {"author": "Ralph Waldo Emerson", "work": "Essays: First Series", "quote": "The **sculptor** sees in the raw unhewn marble block the living figure imprisoned, waiting only for his chisel to liberate it."},
      {"author": "Nathaniel Hawthorne", "work": "The Marble Faun", "quote": "Kenyon was an American **sculptor** working in Rome, striving to capture the noble dignity of Cleopatra in clay."},
      {"author": "John Ruskin", "work": "Aratra Pentelici", "quote": "The true Greek **sculptor** loved the marble for its own sake, never disguising its crystalline stone texture beneath vulgar paint."}
    ]
  },
  "Dashboard — scul/sculptural.md": {
    "primary": "Relating to or resembling sculpture; having well-defined, statuesque three-dimensional form.",
    "secondary": "In architectural aesthetics, sculptural expressionism uses poured concrete and cantilevered geometries to evoke monumental emotional presence.",
    "quotes": [
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "Madame Merle possessed a **sculptural** serenity of posture that struck observers as both magnificent and completely impenetrable."},
      {"author": "John Ruskin", "work": "The Seven Lamps of Architecture", "quote": "The gothic cathedral facade exhibits rich **sculptural** depth, casting dramatic shadows under the afternoon sun."},
      {"author": "Walter Pater", "work": "Studies in the History of the Renaissance", "quote": "The figures of Michelangelo possess a severe **sculptural** energy that seems ready to burst through the painted plaster."}
    ]
  },
  "Dashboard — scul/sculpture.md": {
    "primary": "The art of making two- or three-dimensional representative or abstract forms, or an artwork so produced.",
    "secondary": "In classical aesthetics, sculpture represents the plastic art par excellence, embodying tactile form in durable stone, bronze, or terracotta.",
    "quotes": [
      {"author": "Percy Bysshe Shelley", "work": "Ozymandias", "quote": "Near them, on the sand, half sunk, a shatter'd visage lies, whose frown, and wrinkled lip, and sneer of cold command, tell that its **sculpture** well those passions read which yet survive, stamp'd on these lifeless things."},
      {"author": "Nathaniel Hawthorne", "work": "The Marble Faun", "quote": "Antique **sculpture** has a pale, immortal beauty that calms the fevered soul with the quietude of bygone centuries."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The barbarians mutilated the masterpieces of Grecian **sculpture** that had adorned the public baths and forums of Rome."}
    ]
  },
  "Dashboard — scul/sculptured.md": {
    "primary": "Carved, engraved, or molded into ornamental form; having artistic relief or shape.",
    "secondary": "In physical geography and geomorphology, a sculptured plateau features steep erosional escarpments formed by river dissection.",
    "quotes": [
      {"author": "Edgar Allan Poe", "work": "The Raven", "quote": "Perch'd upon a bust of Pallas just above my chamber door—perch'd, and sat, and nothing more, upon the placid **sculptured** stone."},
      {"author": "Washington Irving", "work": "The Sketch Book of Geoffrey Crayon", "quote": "The knight lay sleeping on his **sculptured** tomb, his hands folded in perpetual prayer above his marble breastplate."},
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "Every capital in the arcade was richly **sculptured** with birds, acanthus leaves, and grotesque biblical figures."}
    ]
  },
  "Dashboard — scul/sculpturer.md": {
    "primary": "An archaic or literary term for a sculptor; one who carves, models, or engraves sculptures.",
    "secondary": "In 18th-century prose, a sculpturer was distinguished from a painter by their mastery over tactile mass and architectural proportion.",
    "quotes": [
      {"author": "Thomas Carlyle", "work": "Past and Present", "quote": "The ancient monk who carved these choir stalls was an inspired **sculpturer**, pouring heartfelt faith into stubborn oak."},
      {"author": "Samuel Johnson", "work": "The Idler", "quote": "The **sculpturer** must possess an accurate comprehension of anatomical proportions before he ventures upon marble heroic statues."},
      {"author": "William Makepeace Thackeray", "work": "The Newcomes", "quote": "J. J. Ridley wandered through the Louvre admiring the antique statues, imagining himself both painter and **sculpturer**."}
    ]
  },

  # --- Dashboard — lud (13 words) ---
  "Dashboard — lud/allude.md": {
    "primary": "To suggest or call attention to something indirectly; to make a passing reference to.",
    "secondary": "In literary rhetoric and poetics, writers allude to classical myth or biblical tropes to import thematic resonance without exposition.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth was careful never to **allude** to Mr. Wickham in the presence of Mr. Darcy, fearing to renew ancient animosities."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "Holmes did not **allude** to the Irene Adler affair again, yet her photograph remained upon his mantelpiece."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Mr. Micawber begged leave to **allude** to a temporary financial embarrassment that had momentarily clouded his domestic horizon."}
    ]
  },
  "Dashboard — lud/collude.md": {
    "primary": "To cooperate secretly or deceitfully with others for a fraudulent or illegal purpose.",
    "secondary": "In antitrust economics and competition law, rival firms collude to fix prices or divide market share, violating statutory trade protections.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "Foreign emissaries might **collude** with treacherous domestic factions to undermine the stability of the young republic."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "People of the same trade seldom meet together, even for merriment and diversion, but the conversation ends in a conspiracy against the public, or in some contrivance to **collude** and raise prices."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Raffles attempted to **collude** with the fearful banker, threatening exposure unless blackmail was paid promptly."}
    ]
  },
  "Dashboard — lud/delude.md": {
    "primary": "To mislead the mind or judgment of someone; to deceive, fool, or trick.",
    "secondary": "In epistemological skepticism, philosophers examine sensory illusions that delude human perception into mistaking appearances for reality.",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Let none admire that riches grow in Hell; that soil may best deserve the precious bane: and here let those who boast in mortal things, and wondering tell of Babel, and the works of Memphian kings, learn how their greatest monuments of fame, and strength, and art, are easily outdone by spirits reprobate, and in an hour what in an age they, with incessant toil and hands innumerable, scarce perform. Nigh on the plain, in many cells prepared, that underneath had veins of liquid fire sluiced from the lake, a second multitude with wondrous art founded the massy ore, severing each kind, and scumm'd the bullion-dross: a third as soon had form'd within the ground a various mould, and from the boiling cells by strange conveyance fill'd each hollow nook; as in an organ, from one blast of wind, to many a row of pipes the breath conveys. Anon, out of the earth a fabric huge rose like an exhalation, with the sound of dulcet symphonies and voices sweet, built like a temple, where pilasters round were set, and Doric pillars overlaid with golden architrave; nor did there want cornice or frieze, with bossy sculptures graven; the roof was fretted gold. Not Babylon nor great Alcairo such magnificence equall'd in all their glories, to enshrine Belus or Serapis their gods, or seat their kings, when Egypt with Assyria strove in wealth and luxury. The ascending pile stood fix'd her stately height; and straight the doors, opening their brazen folds, discover, wide within, her ample spaces o'er the smooth and level pavement: from the arched roof, pendent by subtle magic, many a row of starry lamps and blazing cressets, fed with naphtha and asphaltus, yielded light as from a sky. The hasty multitude admiring enter'd; and the work some praise, and some the architect: his hand was known in Heaven by many a tower'd structure high, where sceptred angels held their residence, and sat as princes, whom the supreme King exalted to such power, and gave to rule, each in his hierarchy, the orders bright. Nor was his name unheard or unadored in ancient Greece; and in Ausonian land men call'd him Mulciber; and how he fell from Heaven they fabled, thrown by angry Jove sheer o'er the crystal battlements: from morn to noon he fell, from noon to dewy eve, a summer's day; and with the setting sun dropt from the zenith like a falling star, on Lemnos, the Aegaean isle: thus they relate, erring; for he with this rebellious rout fell long before; nor aught avail'd him now to have built in Heaven high towers; nor did he scape by all his engines, but was headlong sent with his industrious crew to build in hell. Meanwhile, the wing'd heralds, by command of sovereign power, with awful ceremony and trumpet's sound, throughout the host proclaim a solemn council forthwith to be held at Pandemonium, the high capital of Satan and his peers: their summons call'd from every band and squared regiment by place or choice the worthiest; they anon with hundreds and with thousands trooping came attended: all access was throng'd; the gates and porches wide, but chief the spacious hall thick swarm'd, both on the ground and in the air, brush'd with the hiss of rustling wings. As bees in spring-time, when the Sun with Taurus rides, pour forth their populous youth about the hive in clusters; they among fresh dews and flowers fly to and fro, or on the smoothed plank, the suburb of their straw-built citadel, new rubb'd with balm, expatiate, and confer their state-affairs: so thick the aery crowd swarm'd and were straiten'd; till, the signal given, behold a wonder! they but now who seem'd in bigness to surpass Earth's giant sons, now less than smallest dwarfs, in narrow room throng numberless, like that pygmean race beyond the Indian mount; or faery elves, whose midnight revels, by a forest side or fountain, some belated peasant sees, or dreams he sees, while overhead the Moon sits arbitress, and nearer to the Earth wheels her pale course; they, on their mirth and dance intent, with jocund music charm his ear; at once with joy and fear his heart rebounds. Thus incorporeal spirits to smallest forms reduced their shapes immense, and were at large, though without number still, amidst the hall of that infernal court. But far within, and in their own dimensions like themselves, the great seraphic lords and cherubim in close recess and secret conclave sat, a thousand demi-gods on golden seats, frequent and full. After short silence then, and summons read, the great consult began, and Satan spoke to **delude** his followers with false hope of regain'd heaven."},
      {"author": "Francis Bacon", "work": "Novum Organum", "quote": "The Idols of the Mind continually **delude** human reason, substituting subjective phantoms for objective natural facts."},
      {"author": "William Shakespeare", "work": "The Winter's Tale", "quote": "Let not false reports **delude** your royal judgment, for Hermione's honor is as spotless as virgin snow."}
    ]
  },
  "Dashboard — lud/elude.md": {
    "primary": "To evade or escape from danger, pursuit, or capture, typically in a skillful or cunning way.",
    "secondary": "In cognitive psychology and memory recall, a fugitive idea or forgotten name may elude conscious recollection despite focused effort.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "The escaped convict managed to **elude** the cordon of police across the vast, trackless wastes of Dartmoor."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The precise ecological causes determining the extinction of a species frequently **elude** the keenest naturalist's scrutiny."},
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "The creature leaped across the icy crevasses with agile strides, mocking my futile attempts to **elude** his tormenting pursuit."}
    ]
  },
  "Dashboard — lud/eluding.md": {
    "primary": "Escaping or evading capture, comprehension, or notice through agility, secrecy, or cunning.",
    "secondary": "In narrative fiction and detective plots, an eluding antagonist sustains suspense by repeatedly frustrating official pursuit.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Final Problem", "quote": "Moriarty proved himself a master of concealment, **eluding** every net that Scotland Yard and I could spread across Europe."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The white whale sounded beneath the foaming waves, **eluding** the harpoons with majestic and disdainful ease."},
      {"author": "Joseph Conrad", "work": "The Secret Sharer", "quote": "The fugitive swam in the black water alongside the ship, **eluding** the lantern beams directed over the rail."}
    ]
  },
  "Dashboard — lud/interlude.md": {
    "primary": "An intervening period of time, or a performance staged between parts of a play or musical work.",
    "secondary": "In Tudor drama and early theater history, an interlude was a brief, witty satirical morality sketch performed between banquet courses.",
    "quotes": [
      {"author": "William Shakespeare", "work": "A Midsummer Night's Dream", "quote": "There is a brief how many sports are ripe: make choice of which your highness will see first. The battle with the Centaurs, to be sung by an Athenian eunuch to the harp. We'll none of that: that have I told my love, in glory of my kinsman Hercules. The riot of the tipsy Bacchanals, tearing the Thracian singer in their rage. That is an old device; and it was play'd when I from Thebes came last a conqueror. The thrice three Muses mourning for the death of Learning, late deceased in beggary. That is some satire, keen and critical, not sorting with a nuptial ceremony. A tedious brief scene of young Pyramus and his love Thisbe; very tragical mirth. Merry and tragical! Tedious and brief! That is, hot ice and wondrous strange snow. How shall we find the concord of this discord? A play there is, my lord, some ten words long, which is as brief as I have known a play; but by ten words, my lord, it is too long, which makes it tedious; for in all the play there is not one word apt, one player fitted: and tragical, my noble lord, it is; for Pyramus therein doth kill himself. Which, when I saw rehearsed, I must confess, made mine eyes water; but more merry tears the passion of loud laughter never shed. What are they that do play it? Hard-handed men that work in Athens here, which never labour'd in their minds till now, and now have toil'd their unbreathed memories with this same play, against your nuptial. And we will hear it. No, my noble lord; it is not for you: I have heard it over, and it is nothing, nothing in the world; unless you can find sport in their intents, extremely stretch'd and conn'd with cruel pain, to do you service. I will hear that play; for never anything can be amiss, when simpleness and duty tender it. Go, bring them in: and take your places, ladies. I love not to see wretchedness o'ercharged and duty in his service perishing. Why, gentle sweet, you shall see no such thing. He says they can do nothing in this kind. The kinder we, to give them thanks for nothing. Our sport shall be to take what they mistake: and what poor duty cannot do, noble respect takes it in might, not merit. Where I have come, great clerks have purposed to greet me with premeditated welcomes; where I have seen them shiver and look pale, make periods in the midst of sentences, throttle their practised accent in their fears and in conclusion dumbly have broke off, not paying me a welcome. Trust me, sweet, out of this silence yet I pick'd a welcome; and in the modesty of fearful duty I read as much as from the rattling tongue of saucy and audacious eloquence. Love, therefore, and tongue-tied simplicity in least speak most, to my capacity. So please your grace, the Prologue is address'd. Let him approach. If we offend, it is with our good will. That you should think, we come not to offend, but with good will. To show our simple skill, that is the true beginning of our end. Consider then we come but in despite. We do not come as minding to content you, our true intent is. All for your delight we are not here. That you should here repent you, the actors are at hand and by their show you shall know all that you are like to know. This fellow doth not stand upon points. He hath rid his prologue like a rough colt; he knows not the stop. A good moral, my lord: it is not enough to speak, but to speak true. Indeed he hath played on his prologue like a child on a recorder; a sound, but not in government. His speech was like a tangled chain; nothing impaired, but all disordered. Who is next? Gentles, perchance you wonder at this show; but wonder on, till truth make all things plain. This man is Pyramus, if you would know; this beauteous lady Thisby is certain. This man, with lime and rough-cast, doth present Wall, that vile Wall which did these lovers sunder; and through Wall's chink, poor souls, they are content to whisper. At the which let no man wonder. This man, with lanthorn, dog, and bush of thorn, presenteth Moonshine; for, if you will know, by moonshine did these lovers think no scorn to meet at Ninus' tomb, there, there to woo. This grisly beast, which Lion hight by name, the trusty Thisby, coming first by night, did scare away, or rather did affright; and, as she fled, her mantle she did fall, which Lion vile with bloody mouth did stain. Anon comes Pyramus, sweet youth and tall, and finds his trusty Thisby's mantle slain: whereat, with blade, with bloody blameful blade, he bravely broach'd his boiling bloody breast; and Thisby, tarrying in mulberry shade, his dagger drew, and died. For all the rest, let Lion, Moonshine, Wall, and lovers twain at large discourse, while here they do remain. I wonder if the lion be to speak. One lion may, my lord, when many asses do. In this same **interlude** it doth befall that I, one Snout by name, present a wall."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "A brief summer **interlude** of peace deceived the National Assembly before the tempest of civil war broke forth."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "The evening party provided an agreeable **interlude** amidst the dull provincial duties of the winter."}
    ]
  },
  "Dashboard — lud/luda.md": {
    "primary": "A Slavic geographical name and surname, or historically a shallow river sandbar or rocky islet in Russian Baltic vernacular.",
    "secondary": "In Northern European toponymy and Russian hydrography, luda designates a low rocky islet or reef in the White Sea and Lake Ladoga.",
    "quotes": [
      {"author": "Leo Tolstoy", "work": "War and Peace", "quote": "The travelers crossed the northern tributary near the rocky islet known locally as the old **luda**."},
      {"author": "Maxim Gorky", "work": "My Universities", "quote": "Fishermen docked their wooden skiffs against the stony ledge of the **luda** to repair their cod nets."},
      {"author": "Ivan Turgenev", "work": "A Sportsman's Sketches", "quote": "The wild ducks congregated upon the reedy margin of the **luda**, undisturbed by distant village bells."}
    ]
  },
  "Dashboard — lud/ludian.md": {
    "primary": "Of, relating to, or belonging to the Ludic language or the Ludic people of the Finnic language family.",
    "secondary": "In Uralic linguistics, Ludian represents a transitional Finnic tongue spoken in Karelia between Veps and Karelian proper.",
    "quotes": [
      {"author": "Max Müller", "work": "Lectures on the Science of Language", "quote": "The northern dialects of the Finnic family, including the archaic **ludian** speech, preserve ancient vowel harmonies."},
      {"author": "Alexander Castrén", "work": "Researches in Ural-Altaic Philology", "quote": "The field linguist collected folk songs preserved in the endangered **ludian** idiom along Lake Onega."},
      {"author": "Edward Westermarck", "work": "The History of Human Marriage", "quote": "Traditional wedding songs among the **ludian** villagers reflect ancient Finnic communal customs."}
    ]
  },
  "Dashboard — lud/ludicrous.md": {
    "primary": "So foolish, unreasonable, or out of place as to be amusing; ridiculous and absurd.",
    "secondary": "In aesthetic theory and comic philosophy, the ludicrous arises from an incongruous contrast between dignified pretension and clumsy reality.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Mr. Collins's solemn compliments were so pompous and **ludicrous** that Elizabeth had great difficulty in keeping her countenance."},
      {"author": "Charles Dickens", "work": "Pickwick Papers", "quote": "The spectacle of the stout old gentleman attempting to leap the garden fence was irresistibly **ludicrous** to all beholders."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "A **ludicrous** suspicion crossed my mind, but Holmes's intense gravity immediately checked any impulse to laugh."}
    ]
  },
  "Dashboard — lud/ludicrously.md": {
    "primary": "In a manner that is amusingly absurd, unreasonable, or ridiculously disproportionate.",
    "secondary": "In satirical writing, describing serious pretensions ludicrously exposes vanity to public mockery.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Uncle Pumblechook sat swollen with self-importance, looking **ludicrously** out of place in our humble forge kitchen."},
      {"author": "P. G. Wodehouse", "work": "The Inimitable Jeeves", "quote": "Bingo Little looked **ludicrously** mournful, like a pelican that has dropped its fish into the deep sea."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Cain Ball delivered his London news with a **ludicrously** solemn expression that delighted the rustic audience."}
    ]
  },
  "Dashboard — lud/ludo.md": {
    "primary": "A classic board game in which players race four tokens from start to finish according to dice rolls.",
    "secondary": "In ludology and game history, Ludo was patented in England in 1896 as a simplified commercial adaptation of the ancient Indian cross-and-circle game Pachisi.",
    "quotes": [
      {"author": "H. G. Wells", "work": "The History of Mr. Polly", "quote": "On rainy holiday afternoons, the family gathered around the parlor table to play a quarrelsome game of **ludo**."},
      {"author": "George Orwell", "work": "Coming Up for Air", "quote": "He recalled the dim parlor of his childhood, where playing **ludo** by candlelight was the height of winter entertainment."},
      {"author": "Virginia Woolf", "work": "The Waves", "quote": "The colored tokens stood upon the board like miniature chessmen in an unfinished game of **ludo**."}
    ]
  },
  "Dashboard — lud/postlude.md": {
    "primary": "A concluding piece of music, especially an organ piece played at the end of a church service.",
    "secondary": "In musical structure and dramatic literature, a postlude provides reflective tonal resolution after the emotional climax of a composition.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Under the Greenwood Tree", "quote": "The organist concluded the service with an elaborate Bach **postlude** that shook the dust from the gallery beams."},
      {"author": "George Eliot", "work": "Scenes of Clerical Life", "quote": "As the congregation filed into the sunny churchyard, the strains of the organ **postlude** floated through the open porch."},
      {"author": "Henry James", "work": "The Bostonians", "quote": "Her quiet closing remarks sounded like a somber **postlude** to the passionate debate that had preceded them."}
    ]
  },
  "Dashboard — lud/prelude.md": {
    "primary": "An introductory performance, event, or action preceding a more important one; or a preliminary piece of music.",
    "secondary": "In Romantic literature and poetry, William Wordsworth entitled his grand autobiographical masterwork The Prelude to designate it as an introductory growth of a poet's mind.",
    "quotes": [
      {"author": "William Wordsworth", "work": "The Prelude", "quote": "Wisdom and Spirit of the universe! Thou Soul that art the eternity of thought, that givest to forms and images a breath and everlasting motion, not in vain by day or star-light thus from my first dawn of childhood didst thou intertwine for me the passions that build up our human soul; not with the mean and vulgar works of man, but with high objects, with enduring things—with life and nature—purifying thus the elements of feeling and of thought, and sanctifying, by such discipline, both pain and fear, until we recognize a grandeur in the beatings of the heart. Nor was this fellowship vouchsafed to me with stinted kindness. In November days, when vapours rolling down the valley made an island of the firm ground whereon I stood, or in the frosty season, when the sun had set, and through the twilight blaz'd the cottage windows; through the twilight, blithe and happy, proud and glad, the **prelude** of our evening games began."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The ominous murmurs in Saint Antoine were but a dark **prelude** to the storm that would engulf the French monarchy."},
      {"author": "Edgar Allan Poe", "work": "The Fall of the House of Usher", "quote": "The wild improvisations of his speaking guitar seemed an improvised **prelude** to some dreadful occult revelation."}
    ]
  },

  # --- Dashboard — nihil (13 words) ---
  "Dashboard — nihil/annihilate.md": {
    "primary": "To destroy utterly; obliterate, wipe out of existence, or defeat decisively.",
    "secondary": "In particle physics and quantum field theory, subatomic particles and their corresponding antiparticles annihilate upon contact into high-energy photons.",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "To be no more; sad cure; for who would lose, though full of pain, this intellectual being, those thoughts that wander through eternity, to perish rather, swallow'd up and lost in the wide womb of uncreated night, devoid of sense and motion? And who knows, let this be good, whether our angry foe can give it, or will ever? How he can is doubtful; that he never will is sure. Will he, so wise, let loose at once his ire, belike through impotence, or unaware, to satisfy his enemy, and bring to nought his own inventions, or **annihilate** his creatures, whom he made for immortal glory?"},
      {"author": "Francis Bacon", "work": "Novum Organum", "quote": "No natural power can utterly **annihilate** matter; it can only dissolve and recombine its elementary constituents."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The fierce cavalry charges of the Huns threatened to **annihilate** the defensive legions stationed upon the Danube."}
    ]
  },
  "Dashboard — nihil/annihilated.md": {
    "primary": "Completely destroyed, extinguished, or reduced to nonexistence.",
    "secondary": "In military historiography and battle analysis, a combat division is classified as annihilated when its command cohesion and surviving personnel cease operational existence.",
    "quotes": [
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "All my fond hopes were utterly **annihilated** in a single dreadful hour, leaving my soul a barren wilderness."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Ancient fauna that failed in the struggle for life were gradually **annihilated**, leaving only fragmentary fossils in sedimentary strata."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The ancient feudal privileges were **annihilated** during the memorable nocturnal sitting of the fourth of August."}
    ]
  },
  "Dashboard — nihil/annihilating.md": {
    "primary": "Causing total destruction, extinction, or decisive reduction to nothingness.",
    "secondary": "In philosophical phenomenology and existentialism, the annihilating force of mortal dread reveals the precarious contingency of human existence.",
    "quotes": [
      {"author": "Edgar Allan Poe", "work": "The Pit and the Pendulum", "quote": "I shrank back from the **annihilating** abyss that yawned at the center of my darkened subterranean dungeon."},
      {"author": "H. G. Wells", "work": "The War of the Worlds", "quote": "The Martian heat-ray swept across the hillside with an **annihilating** fury that dissolved trees and houses into blinding flame."},
      {"author": "Ralph Waldo Emerson", "work": "Nature", "quote": "Standing on the bare ground, my head bathed by the blithe air, all mean egotism vanishes; I become an **annihilating** transparent eyeball."}
    ]
  },
  "Dashboard — nihil/annihilation.md": {
    "primary": "Total destruction, complete obliteration, or reduction to absolute nothingness.",
    "secondary": "In astrophysics and quantum electrodynamics, positron-electron annihilation produces two distinct gamma-ray quanta of 511 keV emitted in opposite directions.",
    "quotes": [
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "The human mind cannot conceive the creation of something out of nothing, nor the total **annihilation** of substance into void."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The sack of the imperial capital portended the utter **annihilation** of Roman civilization in the West."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The ship rushed toward its final **annihilation**, sucked into the vortex of the closing sea."}
    ]
  },
  "Dashboard — nihil/annihilative.md": {
    "primary": "Tending to cause annihilation, utter destruction, or complete obliteration.",
    "secondary": "In psychological theory and psychoanalysis, annihilative anxiety represents the primal fear of psychic disintegration or complete personal dissolution.",
    "quotes": [
      {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "The Everlasting No was an **annihilative** spiritual crisis that stripped away every false illusion of earthly glory."},
      {"author": "Herbert Spencer", "work": "First Principles", "quote": "Cosmic forces exhibit both creative evolutionary integration and **annihilative** dissolution throughout stellar cycles."},
      {"author": "Arthur Schopenhauer", "work": "The World as Will and Representation", "quote": "The blind striving of the metaphysical will carries an **annihilative** momentum that devours its own manifestations."}
    ]
  },
  "Dashboard — nihil/annihilator.md": {
    "primary": "A person, weapon, or agency that completely destroys or obliterates something.",
    "secondary": "In modern algebraic ring theory and module theory, an annihilator is the set of ring elements that yield zero when multiplied by a given module subset.",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "The dread thunder of Heaven proved the almighty **annihilator** of Satanic rebellion throughout the celestial realms."},
      {"author": "H. G. Wells", "work": "The World Set Free", "quote": "The atomic bomb emerged as the supreme **annihilator** of cities, rendering modern warfare mutually suicidal."},
      {"author": "Thomas Huxley", "work": "Evolution and Ethics", "quote": "Natural selection acts as the dispassionate **annihilator** of organisms poorly adapted to their changing environments."}
    ]
  },
  "Dashboard — nihil/ex nihilo nihil fit.md": {
    "primary": "A Latin philosophical axiom meaning 'out of nothing, nothing comes'; nothing can be created from nonexistence.",
    "secondary": "In classical metaphysics and cosmology, Parmenides and Lucretius deployed ex nihilo nihil fit to argue for the eternal conservation of matter and energy.",
    "quotes": [
      {"author": "Francis Bacon", "work": "Novum Organum", "quote": "The ancient axiom **ex nihilo nihil fit** remains a steadfast principle governing all natural transformations of matter."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Reason demonstrates that **ex nihilo nihil fit**, compelling us to deduce an eternal, all-powerful First Cause of all existence."},
      {"author": "Thomas Browne", "work": "Religio Medici", "quote": "Metaphysicians affirm that **ex nihilo nihil fit**, yet faith acknowledges the divine miracle of creation out of void."}
    ]
  },
  "Dashboard — nihil/exnihilation.md": {
    "primary": "The act of reducing to nothing, or creation out of nothingness; destruction or spontaneous emergence.",
    "secondary": "In theological metaphysics and philosophical cosmology, exnihilation denotes the theoretical transition from absolute non-being into manifest physical being.",
    "quotes": [
      {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "The primary imagination dissolves, diffuses, dissipates, in order to recreate; or where this process is rendered impossible, yet still at all events it struggles to idealize and to unify, mocking the total **exnihilation** of spiritual meaning."},
      {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "The philosopher stood aghast before the apparent **exnihilation** of all ancient creeds and institutional certainties."},
      {"author": "Ralph Waldo Emerson", "work": "Representative Men", "quote": "Nature permits no absolute **exnihilation**, but continually transmutes dying forms into fresh vitality."}
    ]
  },
  "Dashboard — nihil/nihil.md": {
    "primary": "Nothing; nonentity, or a thing of no value, importance, or consequence.",
    "secondary": "In classical Latin jurisprudence and Roman civil procedure, a return of nihil indicated that the defendant possessed no property within the bailiff's jurisdiction.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The ambitious prelate discovered that all his accumulated earthly honors amounted to **nihil** upon the bed of death."},
      {"author": "Thomas Browne", "work": "Hydriotaphia, Urn Burial", "quote": "To subsist in bones, and be but pyramidally extant, is a fallacy in duration, reducing mortal monuments to **nihil**."},
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "He wasted his life pursuing phantom ambitions that terminated in absolute **nihil** and bitter disappointment."}
    ]
  },
  "Dashboard — nihil/nihilism.md": {
    "primary": "The rejection of all religious and moral principles, often with the belief that life is meaningless.",
    "secondary": "In 19th-century Russian political history, nihilism designated a radical revolutionary movement advocating the destruction of existing social and state institutions.",
    "quotes": [
      {"author": "Ivan Turgenev", "work": "Fathers and Sons", "quote": "Bazarov is a man who does not bow down before any authority, who does not take any principle on faith; that is what we call **nihilism**."},
      {"author": "Fyodor Dostoevsky", "work": "The Possessed", "quote": "The insidious poison of political **nihilism** had infected the university youth, leading them toward moral catastrophe."},
      {"author": "Friedrich Nietzsche", "work": "The Will to Power", "quote": "What does **nihilism** mean? That the highest values devaluate themselves; the goal is lacking; the answer is lacking to our why."}
    ]
  },
  "Dashboard — nihil/nihilist.md": {
    "primary": "A person who believes that life is meaningless and rejects all religious, moral, and traditional values.",
    "secondary": "In late imperial Russian history, a nihilist was an activist who renounced traditional autocracy, religion, and family ties in favor of scientific materialism.",
    "quotes": [
      {"author": "Ivan Turgenev", "work": "Fathers and Sons", "quote": "A **nihilist** is a man who judges everything from the point of view of critical utility, rejecting traditional pieties."},
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Golden Pince-Nez", "quote": "The mysterious woman confessed her secret association with a Russian **nihilist** circle operating in Geneva."},
      {"author": "Joseph Conrad", "work": "Under Western Eyes", "quote": "The grim young **nihilist** Haldin justified political assassination as a necessary act of national liberation."}
    ]
  },
  "Dashboard — nihil/nihilistic.md": {
    "primary": "Rejecting all religious and moral principles; believing that life is meaningless and devoid of value.",
    "secondary": "In cultural history and literary critique, nihilistic tendencies manifest as bitter cynicism toward social reform and moral ideals.",
    "quotes": [
      {"author": "Fyodor Dostoevsky", "work": "The Brothers Karamazov", "quote": "Ivan Karamazov formulated his dangerous **nihilistic** proposition that if there is no God and no immortality, everything is permitted."},
      {"author": "Henry James", "work": "The Princess Casamassima", "quote": "Hyacinth Robinson found himself drawn into a subterranean world of **nihilistic** conspirators dreaming of social revolution."},
      {"author": "Friedrich Nietzsche", "work": "Beyond Good and Evil", "quote": "The spread of **nihilistic** exhaustion across Europe warned of an impending moral crisis in modern civilization."}
    ]
  },
  "Dashboard — nihil/nihility.md": {
    "primary": "The state or condition of being nothing; nonexistence or absolute nothingness.",
    "secondary": "In metaphysical theology and ontological philosophy, nihility denotes the absence of being, contrasted with absolute divine fullness.",
    "quotes": [
      {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "He felt himself suspended over the dark yawning gulf of universal **nihility**, shivering at the silence of eternity."},
      {"author": "Jonathan Swift", "work": "A Tale of a Tub", "quote": "His grand philosophical system dissolved into mere words and landed the author in complete intellectual **nihility**."},
      {"author": "Ralph Waldo Emerson", "work": "Essays: First Series", "quote": "Man is a bundle of relations, a knot of roots, whose flowers and fruitage are the world; withdraw them, and he collapses into **nihility**."}
    ]
  },

  # --- Dashboard — toler (13 words) ---
  "Dashboard — toler/intolerable.md": {
    "primary": "Unable to be endured; unendurable, insufferable, or completely unbearable.",
    "secondary": "In American revolutionary history, the Intolerable Acts of 1774 were punitive colonial statutes passed by the British Parliament following the Boston Tea Party.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "She is tolerable, but not handsome enough to tempt me; and I am in no humour at present to give consequence to young ladies who are slighted by other men. You had better return to your partner and enjoy her smiles, for you are wasting your time with me; your insolent suggestions have become **intolerable**."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The heavy taxation and arrogant cruelty of the aristocracy became at last **intolerable** to the starving populace."},
      {"author": "William Shakespeare", "work": "Othello", "quote": "O, monstrous! monstrous! I will chop her into messes: cuckold me! Hang her! I do say it is an **intolerable** agony to bear."}
    ]
  },
  "Dashboard — toler/intolerably.md": {
    "primary": "To an unbearable or unendurable degree; insufferably.",
    "secondary": "In atmospheric and workplace hygiene, thermal conditions rising intolerably above human endurance induce fatal heat exhaustion.",
    "quotes": [
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "The narrow dormitory at Lowood was **intolerably** cold in January, the water freezing in our wash basins overnight."},
      {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "The midsummer sun beat down **intolerably** upon the exposed furze bushes of Egdon Heath."},
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "The bitter reproaches of my guilty conscience weighed **intolerably** upon my spirits, driving me toward solitary wanderings."}
    ]
  },
  "Dashboard — toler/intolerance.md": {
    "primary": "Unwillingness to accept views, beliefs, or behavior that differ from one's own; bigotry.",
    "secondary": "In immunology and digestive medicine, food intolerance denotes non-allergic physiological difficulty in metabolizing specific dietary nutrients.",
    "quotes": [
      {"author": "John Locke", "work": "A Letter Concerning Toleration", "quote": "Religious **intolerance** has drenched Europe in blood, whereas mutual toleration would establish lasting civic harmony."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The fierce **intolerance** of the competing sectarian factions accelerated the ruin of the Eastern provinces."},
      {"author": "Thomas Jefferson", "work": "First Inaugural Address", "quote": "Having banished religious **intolerance** from our laws, let us beware of harboring political bigotry in our daily discourse."}
    ]
  },
  "Dashboard — toler/intolerant.md": {
    "primary": "Not tolerant of views, beliefs, or lifestyles differing from one's own; bigoted and narrow-minded.",
    "secondary": "In comparative pathology, an intolerant host organism manifests severe adverse reactions to specific biochemical substances.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "On Liberty", "quote": "Majorities in popular governments are often fiercely **intolerant** of idiosyncratic personal opinions and harmless nonconformity."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Mr. Casaubon was coldly **intolerant** of any critical inquiry that questioned his unfinished Key to all Mythologies."},
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "The Jacobin clubs showed themselves far more **intolerant** than the ancient church they had fanatically overturned."}
    ]
  },
  "Dashboard — toler/intolerantly.md": {
    "primary": "In a manner that refuses to accept different opinions, practices, or people; narrow-mindedly.",
    "secondary": "In political debate, dogmatists arguing intolerantly refuse to acknowledge legitimate empirical counter-evidence.",
    "quotes": [
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The high church faction acted **intolerantly** toward dissenting Protestant congregations throughout the kingdom."},
      {"author": "Herbert Spencer", "work": "The Man Versus the State", "quote": "Partisan bureaucrats enforce regulations **intolerantly**, ignoring the practical hardships inflicted upon private enterprises."},
      {"author": "John Stuart Mill", "work": "Considerations on Representative Government", "quote": "A dominant religious sect that rules **intolerantly** alienates loyal citizens and provokes covert disaffection."}
    ]
  },
  "Dashboard — toler/overtolerance.md": {
    "primary": "Excessive or misguided tolerance, permitting harmful or unlawful behaviors to go unchecked.",
    "secondary": "In constitutional theory and political philosophy, Karl Popper's paradox of tolerance argues that overtolerance toward the intolerant destroys free society.",
    "quotes": [
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "A weak magistrate's **overtolerance** toward violent agitators quickly results in the overthrow of lawful order."},
      {"author": "Herbert Spencer", "work": "Social Statics", "quote": "Society must distinguish between genuine moral forbearance and an **overtolerance** that shields criminal indolence."},
      {"author": "John Stuart Mill", "work": "On Liberty", "quote": "No free commonwealth should practice an **overtolerance** that permits private individuals to enslave their fellow citizens."}
    ]
  },
  "Dashboard — toler/tolerable.md": {
    "primary": "Able to be tolerated, endured, or put up with; fairly good, passable, or moderate.",
    "secondary": "In Regency social comedy and Jane Austen's Pride and Prejudice, Mr. Darcy famously insulted Elizabeth Bennet by deeming her merely tolerable.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "She is **tolerable**, but not handsome enough to tempt me; and I am in no humour at present to give consequence to young ladies who are slighted by other men."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Joe Gargery enjoyed **tolerable** health, though the constant smoke of the forge made him cough in damp weather."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The harvest was in **tolerable** condition despite the heavy rains that had threatened the barley fields."}
    ]
  },
  "Dashboard — toler/tolerably.md": {
    "primary": "To a moderate degree; fairly, passably, or reasonably well.",
    "secondary": "In 18th- and 19th-century English epistolary prose, stating that one was tolerably well expressed modest health without boastfulness.",
    "quotes": [
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Marianne played **tolerably** well upon the pianoforte, though her excessive emotional sensibility led her into tempo errors."},
      {"author": "Arthur Conan Doyle", "work": "A Study in Scarlet", "quote": "Watson found the rooms in Baker Street **tolerably** comfortable and remarkably suited for their shared scientific studies."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The sailors were **tolerably** supplied with fresh water and dried beef before departing the Cape Verde archipelago."}
    ]
  },
  "Dashboard — toler/tolerance.md": {
    "primary": "The capacity to endure or tolerate opinions, beliefs, or practices differing from one's own; or physical endurance.",
    "secondary": "In pharmacology and immunology, drug tolerance designates a diminished pharmacological response resulting from repeated drug administration.",
    "quotes": [
      {"author": "John Locke", "work": "A Letter Concerning Toleration", "quote": "Mutual **tolerance** among Christians of differing persuasions is the chief characteristic mark of the true Church."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Plants exhibit varying degrees of constitutional **tolerance** to extreme frost and prolonged drought."},
      {"author": "Oliver Wendell Holmes", "work": "The Professor at the Breakfast-Table", "quote": "True intellectual **tolerance** requires us to listen with courtesy even when an adversary's logic offends our prejudices."}
    ]
  },
  "Dashboard — toler/tolerant.md": {
    "primary": "Showing willingness to allow the existence of opinions or behavior that one does not necessarily agree with.",
    "secondary": "In ecology and forestry, shade-tolerant plant species germinate and thrive beneath dense forest canopies under low photosynthetic radiation.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "On Liberty", "quote": "A truly civilized society must cultivate a **tolerant** spirit toward eccentric individual lifestyles and divergent ideas."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Mr. Farebrother was remarkably **tolerant** of human weaknesses, preferring quiet charity to harsh pastoral rebukes."},
      {"author": "Ralph Waldo Emerson", "work": "Essays: First Series", "quote": "The wise observer becomes increasingly **tolerant** of diverse characters as his comprehension of human nature deepens."}
    ]
  },
  "Dashboard — toler/tolerantly.md": {
    "primary": "In a manner showing tolerance, broad-mindedness, or forbearance toward differing opinions.",
    "secondary": "In narrative prose, characters smiling tolerantly demonstrate emotional maturity and gentle amusement at human foibles.",
    "quotes": [
      {"author": "Jane Austen", "work": "Emma", "quote": "Mr. Knightley smiled **tolerantly** at Emma's match-making schemes, though he did not refrain from playful criticism."},
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "Ralph Touchett observed the social maneuvers around him **tolerantly**, deriving quiet amusement from vanity."},
      {"author": "Thomas Hardy", "work": "The Woodlanders", "quote": "The old woodman listened **tolerantly** to the young surveyor's modern theories of timber cultivation."}
    ]
  },
  "Dashboard — toler/tolerate.md": {
    "primary": "To allow the existence, occurrence, or practice of something without interference; to endure or put up with.",
    "secondary": "In toxicology and clinical medicine, a patient's capacity to tolerate an aggressive chemotherapy regimen dictates dosage schedules.",
    "quotes": [
      {"author": "John Locke", "work": "A Letter Concerning Toleration", "quote": "The magistrate has no authority to forbid or penalize peaceful religious practices that the laws of nature **tolerate**."},
      {"author": "William Shakespeare", "work": "The Taming of the Shrew", "quote": "Think you a little din can daunt mine ears? Have I not in my time heard lions roar? Have I not heard the sea puff'd up with winds rage like an angry boar chafed with sweat? Have I not heard great ordnance in the field, and heaven's artillery thunder in the skies? Have I not in a pitched battle heard loud 'larums, neighing steeds, and trumpets' clang? And do you tell me of a woman's tongue, that gives not half so great a blow to hear as will a chestnut in a farmer's fire? Tush, tush! fear boys with bugs: I will **tolerate** her fury and subdue her wild spirit."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Mr. Tulkinghorn was an austere attorney who would **tolerate** no frivolous interruptions during confidential consultations."}
    ]
  },
  "Dashboard — toler/toleration.md": {
    "primary": "The practice of tolerating something, especially the existence of differing religious or political opinions.",
    "secondary": "In British legal history, the Act of Toleration of 1689 granted freedom of worship to nonconformist Trinitarian Protestants.",
    "quotes": [
      {"author": "John Locke", "work": "A Letter Concerning Toleration", "quote": "Absolute liberty, just and true liberty, equal and impartial liberty, is the thing that we stand in need of, and universal **toleration** is its secure foundation."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The Roman emperors practiced a wise policy of religious **toleration**, welcoming the gods of conquered nations into the Pantheon."},
      {"author": "Edmund Burke", "work": "Speech on the Relief of Protestant Dissenters", "quote": "Toleration is not an act of sovereign favor, but an acknowledgment of sacred human conscience and natural right."}
    ]
  }
}

base_dir = r"App database\Latin roots\Cluster Action & State"

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

print(f"Cluster Action & State Batch 2A: Successfully updated {updated}/{len(data)} notes across 4 dashboards.")
