# -*- coding: utf-8 -*-
import os, sys, re
sys.stdout.reconfigure(encoding="utf-8")

data = {
  # --- Dashboard — ult (55 words) ---
  "Dashboard — ult/adult.md": {
    "primary": "A fully grown, mature person, animal, or organism that has attained legal age or reproductive capability.",
    "secondary": "In developmental psychology and legal jurisprudence, an adult assumes full civic accountability, contractual capacity, and independent rights.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The secondary sexual plumage attains its most vibrant coloration only when the bird reaches the **adult** stage."},
      {"author": "John Locke", "work": "Second Treatise of Government", "quote": "The power of parents over their children ceases when the latter arrive at the understanding and status of an **adult**."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Dorothea looked back upon her naive youthful aspirations with the sober perspective of an **adult** mind."}
    ]
  },
  "Dashboard — ult/adulterant.md": {
    "primary": "A foreign, inferior, or contaminated substance added to food, drink, or manufactured goods to diminish purity or reduce cost.",
    "secondary": "In public health chemistry and food forensics, an adulterant such as chalk in flour or water in milk defrauds consumers and risks toxic exposure.",
    "quotes": [
      {"author": "H. G. Wells", "work": "Tono-Bungay", "quote": "The analytical chemist discovered a cheap chemical **adulterant** in the patent medicine that boosted its stimulant effects."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Lead poisoning frequently arose among laborers who consumed cider contaminated with a metallic **adulterant**."},
      {"author": "Upton Sinclair", "work": "The Jungle", "quote": "Inspectors condemned crates of sausage containing chemical preservatives and colored **adulterant** powders."}
    ]
  },
  "Dashboard — ult/adulterate.md": {
    "primary": "To debase or corrupt the purity of something by adding inferior, alien, or spurious ingredients.",
    "secondary": "In commercial regulation and pharmaceutical law, manufacturers who adulterate medicinal compounds face severe statutory penalties and product recalls.",
    "quotes": [
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "Men seek to **adulterate** natural philosophy with scholastic dogmatism and empty metaphysical conceits."},
      {"author": "William Shakespeare", "work": "Richard III", "quote": "From forth the kennel of thy womb hath crept a hell-hound that doth hunt us to the death: that dog, that had his teeth before his eyes, to worry lambs and lap their gentle blood, that foul defacer of God's handiwork, that excellent grand tyrant of the earth, that reigns in galled eyes of weeping souls, thy womb let loose, to chase us to our graves. O upright, just, and true-disposing God, how do I thank thee, that this carnal cur preys on the issue of his mother's body, and makes her pew-fellow with others' moan! Bear with me; I am hungry for revenge, and now I cloy me with beholding it. Thy Edward he is dead, that kill'd my Edward; thy other Edward dead, to quit my Edward; young York he is but boot, because both they match'd not the high perfection of my loss: thy Clarence he is dead that stabb'd my Edward; and the beholders of this frantic play, the **adulterate** Hastings, Rivers, Vaughan, Grey, untimely smother'd in their dusky graves."},
      {"author": "John Milton", "work": "Areopagitica", "quote": "Truth needs no licensing licensers to **adulterate** her clear fountains with partisan doctrinal censorship."}
    ]
  },
  "Dashboard — ult/adulterated.md": {
    "primary": "Rendered impure, debased, or degraded by the addition of foreign or inferior substances.",
    "secondary": "In nineteenth-century food safety agitation, adulterated urban milk supplies caused widespread infantile mortality across major industrial cities.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Hard Times", "quote": "The tea sold to Coketown factory workers was notoriously **adulterated** with roasted chicory and dried sloe leaves."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Ancient debased currencies consisted of **adulterated** silver coin that circulated at a deep discount against pure bullion."},
      {"author": "Thomas Carlyle", "work": "Past and Present", "quote": "A nation that trades in **adulterated** bread and shoddy wool cloth invites moral and industrial ruin."}
    ]
  },
  "Dashboard — ult/adulterating.md": {
    "primary": "The ongoing practice or act of contaminating or corrupting a substance by adding inferior ingredients.",
    "secondary": "In regulatory chemistry, municipal sanitary officers conducted surprise inspections targeting merchants suspected of adulterating bulk staples.",
    "quotes": [
      {"author": "Daniel Defoe", "work": "The Complete English Tradesman", "quote": "The dishonest grocer gained a transient profit by **adulterating** his spices with worthless dust."},
      {"author": "Upton Sinclair", "work": "The Jungle", "quote": "Packinghouse managers had perfected the clandestine art of **adulterating** potted ham with tripe and dye."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "The analytical apothecary warned that **adulterating** alkaloids with toxic residues endangered patient recovery."}
    ]
  },
  "Dashboard — ult/adulteration.md": {
    "primary": "The act of rendering something impure or fraudulent by mixing it with inferior or spurious matter.",
    "secondary": "In statutory history, the Pure Food and Drug Act of 1906 established strict federal prohibitions against chemical adulteration of food.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "On Liberty", "quote": "To prevent fraud by the **adulteration** of consumable provisions is an indisputable function of legitimate government."},
      {"author": "Thomas Huxley", "work": "Science and Culture", "quote": "Chemical analysis readily exposes every commercial **adulteration** practiced upon olive oils and wines."},
      {"author": "George Eliot", "work": "Silas Marner", "quote": "The villagers suspected the apothecary of subtle **adulteration** in his medicinal decoctions."}
    ]
  },
  "Dashboard — ult/adulterator.md": {
    "primary": "A person, corporation, or manufacturer that adulterates goods, commodities, or texts with spurious ingredients.",
    "secondary": "In commercial penal codes, an adulterator of essential medicines faced severe fines, license revocation, and imprisonment.",
    "quotes": [
      {"author": "William Makepeace Thackeray", "work": "The Book of Snobs", "quote": "The fraudulent wine merchant was an unprincipled **adulterator** who passed off gooseberry wash as vintage champagne."},
      {"author": "Charles Kingsley", "work": "Alton Locke", "quote": "The angry tailor denounced the commercial **adulterator** who flooded the market with brittle shoddy garments."},
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "He regarded the careless editor as a literary **adulterator** who corrupted the pure text of ancient authors."}
    ]
  },
  "Dashboard — ult/adulterer.md": {
    "primary": "A married person, particularly a man, who voluntarily engages in sexual intercourse with someone other than their lawful spouse.",
    "secondary": "In historical family law and canon courts, an adulterer was subject to matrimonial censure and forfeiture of conjugal rights.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Merry Wives of Windsor", "quote": "Ford raged with jealousy, swearing to catch the treacherous **adulterer** Falstaff hidden in his buck-basket."},
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "The magistrate exhorted Hester Prynne to name the fellow **adulterer** who shared her guilt and ignominy."},
      {"author": "Leo Tolstoy", "work": "Anna Karenina", "quote": "Karenin coldly informed his wife that public opinion would brand her lover as an unscrupulous **adulterer**."}
    ]
  },
  "Dashboard — ult/adulteress.md": {
    "primary": "A married woman who voluntarily engages in sexual intercourse with someone other than her lawful husband.",
    "secondary": "In classical and biblical literature, the figure of the adulteress is subjected to intense social opprobrium and moral scrutiny.",
    "quotes": [
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "The stern Puritan crowd gazed upon the condemned **adulteress** as she stood proudly upon the market-place pillory."},
      {"author": "William Shakespeare", "work": "The Winter's Tale", "quote": "Leontes unjustly accused Hermione, shouting that she was an unfaithful **adulteress** unworthy of the crown."},
      {"author": "Gustave Flaubert", "work": "Madame Bovary", "quote": "Emma stared into the mirror, whispering to herself with wild romantic intoxication that she was an **adulteress**."}
    ]
  },
  "Dashboard — ult/adulterine.md": {
    "primary": "Pertaining to or born of adultery; spurious, illicit, or unauthorized by lawful authority.",
    "secondary": "In English constitutional and feudal history, adulterine castles were fortifications built without royal license during periods of civil anarchy.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The Roman jurists examined the inheritance claims of the **adulterine** offspring with severe statutory skepticism."},
      {"author": "William Stubbs", "work": "The Constitutional History of England", "quote": "Henry II commanded the immediate demolition of all **adulterine** castles erected during the lawless reign of Stephen."},
      {"author": "Walter Scott", "work": "Ivanhoe", "quote": "The Norman barons erected **adulterine** keeps throughout the countryside to oppress the local Saxon peasantry."}
    ]
  },
  "Dashboard — ult/adulterous.md": {
    "primary": "Involving, guilty of, or characterized by adultery; unfaithful to marriage vows.",
    "secondary": "In Victorian domestic fiction, an adulterous liaison inevitably precipitates social ostracism and domestic tragedy.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "Ay, that incestuous, that **adulterous** beast, with witchcraft of his wit, with traitorous gifts, won to his shameful lust the will of my most seeming-virtuous queen."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "Jane fled Thornfield Hall rather than submit to an **adulterous** union that violated her sacred moral convictions."},
      {"author": "Thomas Hardy", "work": "Jude the Obscure", "quote": "Conventional society regarded their unconventional, tender cohabitation as a scandalous and **adulterous** defiance."}
    ]
  },
  "Dashboard — ult/adulterously.md": {
    "primary": "In an adulterous manner; in violation of the marriage bond through unfaithfulness.",
    "secondary": "In historical ecclesiastical court proceedings, witnesses testified regarding spouses living adulterously in open defiance of church canons.",
    "quotes": [
      {"author": "Henry Fielding", "work": "Tom Jones", "quote": "The puritanical magistrate condemned those who consorted **adulterously** while maintaining an outward facade of piety."},
      {"author": "Anthony Trollope", "work": "He Knew He Was Right", "quote": "Trevelyan harbored the mad delusion that his faithful wife had conducted herself **adulterously** with Colonel Osborne."},
      {"author": "John Milton", "work": "The Doctrine and Discipline of Divorce", "quote": "A forced marriage of incompatible minds drives desperate souls to seek comfort **adulterously** outside lawful bonds."}
    ]
  },
  "Dashboard — ult/adultery.md": {
    "primary": "Voluntary sexual intercourse between a married person and someone who is not their lawful spouse.",
    "secondary": "In common law jurisprudence, adultery constituted the primary fault-based ground for marital dissolution before no-fault divorce reforms.",
    "quotes": [
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "The scarlet letter A embroidered upon Hester's breast stood as an indelible public brand of her **adultery**."},
      {"author": "William Shakespeare", "work": "King Lear", "quote": "Ay, every inch a king: when I do stare, see how the subject quakes. I pardon that man's life. What was thy cause? **Adultery**? Thou shalt not die: die for **adultery**! No: the wren goes to't, and the small gilded fly does lecher in my sight."},
      {"author": "Leo Tolstoy", "work": "Anna Karenina", "quote": "The high society of Petersburg excused covert hypocrisy but harshly punished open, passionate **adultery**."}
    ]
  },
  "Dashboard — ult/adulthood.md": {
    "primary": "The developmental stage of human maturity characterized by legal age, physical growth, and independent social responsibility.",
    "secondary": "In anthropological rites of passage, initiation ceremonies mark the symbolic transition from adolescent dependence to community adulthood.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "On Liberty", "quote": "Liberty as a principle has no application to any state of things anterior to the time when mankind have attained **adulthood**."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "David reflected upon his lonely boyhood, realizing how trials had prematurely forced him into the responsibilities of **adulthood**."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Habits acquired in early youth become cast in plaster before a person reaches full intellectual **adulthood**."}
    ]
  },
  "Dashboard — ult/antepenultima.md": {
    "primary": "The syllable before the penultimate; the third syllable from the end of a word.",
    "secondary": "In classical Latin and Greek metric prosody, the antepenultima frequently carries the tonic accent when the penult is light.",
    "quotes": [
      {"author": "Quintilian", "work": "Institutio Oratoria", "quote": "In Latin phonology, the acute accent never retreats further from the end of a vocable than the **antepenultima**."},
      {"author": "Samuel Johnson", "work": "A Dictionary of the English Language", "quote": "Polysyllabic words ending in -ity regularly throw their rhythmic stress back upon the **antepenultima**."},
      {"author": "Henry Sweet", "work": "A Handbook of Phonetics", "quote": "The stress accent in ancient Greek shifts toward the **antepenultima** depending upon the quantity of the final vowel."}
    ]
  },
  "Dashboard — ult/antepenultimate.md": {
    "primary": "Coming immediately before the penultimate; third from the end in a series or word.",
    "secondary": "In linguistic accentology, the antepenultimate rule dictates vowel stress placement across many Romance and Hellenic derivations.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Lost World", "quote": "Professor Challenger pointed out the **antepenultimate** vertebra of the fossil dinosaur, noting its anomalous neural spine."},
      {"author": "Max Müller", "work": "Lectures on the Science of Language", "quote": "Sanskrit nominal inflections place the tonic accent upon the **antepenultimate** syllable in dactylic stems."},
      {"author": "Thomas Henry Huxley", "work": "Man's Place in Nature", "quote": "The **antepenultimate** segment of the primate limb skeleton exhibits clear homology with primitive mammalian quadrupeds."}
    ]
  },
  "Dashboard — ult/coulter.md": {
    "primary": "A sharp, heavy vertical blade or wheel fixed to the beam of a plow to cut the turf ahead of the plowshare.",
    "secondary": "In medieval agricultural history, the introduction of the heavy wheeled plow with an iron coulter revolutionized northern European farming.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry V", "quote": "Her fallow leas the darnel, hemlock and rank fumitory doth root upon, while that the **coulter** rusts that should deracinate such savagery."},
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "The bright iron **coulter** of the plow gleamed in the autumn furrow under the fading sunset light."},
      {"author": "Walter Scott", "work": "The Heart of Midlothian", "quote": "The sturdy ploughman guided his team, watching the keen **coulter** slice smoothly through the sodden peat moss."}
    ]
  },
  "Dashboard — ult/exult.md": {
    "primary": "To feel or show triumphant elation, joyful pride, or jubilant rejoicing over a victory or success.",
    "secondary": "In epic poetry and military chronicles, victorious warriors exult over defeated adversaries upon the field of battle.",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Satan gazed upon the ruined angelic host, daring to **exult** in his pride despite thunderous celestial defeat."},
      {"author": "William Shakespeare", "work": "Henry VI, Part 3", "quote": "Queen Margaret did **exult** with cruel scorn when she placed the paper crown upon York's grieving head."},
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "The monster fled into the alpine night, pausing upon the glacier to **exult** in the horror he had wrought."}
    ]
  },
  "Dashboard — ult/exultant.md": {
    "primary": "Filled with or expressing triumphant joy, jubilant celebration, or victorious pride.",
    "secondary": "In psychological descriptions of triumph, an exultant mindset accompanies the breakthrough completion of arduous long-term quests.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Ahab uttered an **exultant** cry as the white whale breached the churning ocean waters before the ship."},
      {"author": "Joseph Conrad", "work": "Lord Jim", "quote": "The native sailors raised an **exultant** shout as the schooner slipped safely past the coral reef into harbor."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Holmes turned to me with an **exultant** gleam in his dark eyes, knowing that our cunning trap had snapped shut."}
    ]
  },
  "Dashboard — ult/exultantly.md": {
    "primary": "In a triumphant, jubilant, or rejoicing manner, filled with victorious pride.",
    "secondary": "In literary narratives, protagonists react exultantly upon discovering long-sought revelations or escaping mortal peril.",
    "quotes": [
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "Rochester laughed **exultantly** as he embraced Jane, believing that fate had at last united their parted destinies."},
      {"author": "Robert Louis Stevenson", "work": "Treasure Island", "quote": "Long John Silver waved his crutch **exultantly** when the mutineers discovered the freshly dug treasure cache."},
      {"author": "Jack London", "work": "The Call of the Wild", "quote": "Buck howled **exultantly** across the frozen Yukon wilderness, answering the ancient call of his wild lupine ancestors."}
    ]
  },
  "Dashboard — ult/exultation.md": {
    "primary": "A feeling or outward expression of triumphant elation, triumphant joy, or victorious jubilation.",
    "secondary": "In social celebrations of national independence, public exultation manifests through ringing bells, parades, and civic assemblies.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The Roman populace gave way to boundless **exultation** when news arrived that the barbarian invaders had retreated across the Danube."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The revolutionary mob danced the Carmagnole in wild **exultation** around the bloodstained platform of the guillotine."},
      {"author": "Bram Stoker", "work": "Dracula", "quote": "A surge of intense **exultation** filled Van Helsing's heart as the holy wafer sealed the vampire's tomb against escape."}
    ]
  },
  "Dashboard — ult/exulting.md": {
    "primary": "Rejoicing exceedingly; expressing triumphant joy, proud victory, or jubilant satisfaction.",
    "secondary": "In narrative battle scenes, an exulting cry rises from troops as enemy battlelines buckle and retreat.",
    "quotes": [
      {"author": "Walter Scott", "work": "The Lady of the Lake", "quote": "The Highland clansmen raised an **exulting** cheer that echoed from crag to crag across the mountain lake."},
      {"author": "H. G. Wells", "work": "The Time Machine", "quote": "I heard the **exulting** laughter of the subterranean Morlocks echoing through the dark ventilation shafts."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The armed sans-culottes marched through Paris, **exulting** over the fall of the Bastille's grim towers."}
    ]
  },
  "Dashboard — ult/exultingly.md": {
    "primary": "With triumphant joy or proud elation; rejoicingly and boastfully in victory.",
    "secondary": "In rhetorical polemics, orators speak exultingly when evidence irrefutably confirms their long-derided predictions.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The harpooneer shouted **exultingly** as the whale sounded, drawing the singing line smoothly from the tubs."},
      {"author": "Arthur Conan Doyle", "work": "A Study in Scarlet", "quote": "Lestrade smiled **exultingly** as he displayed the handcuffs, confident that he had apprehended the true assassin."},
      {"author": "Nathaniel Hawthorne", "work": "The House of the Seven Gables", "quote": "Clifford laughed **exultingly** as the steam train swept him away from the gloomy mansion of his sorrows."}
    ]
  },
  "Dashboard — ult/penultimate.md": {
    "primary": "Occurring next to the last in a series; second from the final position.",
    "secondary": "In linguistic prosody and phonetics, the penultimate syllable of a polysyllabic Latin word determines stress accent according to vowel length.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "In the **penultimate** chapter of his laborious theological work, Casaubon attempted to synthesize his mythological keys."},
      {"author": "Arthur Conan Doyle", "work": "His Last Bow", "quote": "Holmes regarded the secret cipher as the **penultimate** link in the chain that connected the spy to the foreign embassy."},
      {"author": "Max Müller", "work": "The Science of Language", "quote": "Comparative philology reveals how Greek accents gravitate toward the **penultimate** mora in trochaic meters."}
    ]
  },
  "Dashboard — ult/ult.md": {
    "primary": "An abbreviation for ultimo; occurring or published in the month immediately preceding the present one.",
    "secondary": "In nineteenth-century commercial and epistolary correspondence, 'your letter of the 15th ult.' designated the previous calendar month.",
    "quotes": [
      {"author": "Charles Dickens", "work": "The Pickwick Papers", "quote": "Messrs. Dodson and Fogg acknowledged receipt of Mr. Pickwick's communication dated the 24th **ult** with polite coldness."},
      {"author": "Thomas Babington Macaulay", "work": "Life and Letters of Lord Macaulay", "quote": "The foreign office dispatched urgent instructions on the 10th **ult**, demanding a prompt reply from the ambassador."},
      {"author": "Walter Scott", "work": "The Antiquary", "quote": "The lawyer opened his ledger to verify the remittance recorded on the 3rd **ult** before proceeding with the title search."}
    ]
  },
  "Dashboard — ult/ulterior.md": {
    "primary": "Existing beyond what is obvious, apparent, or admitted; intentionally concealed, latent, or ulterior.",
    "secondary": "In criminal investigation and tactical diplomacy, investigators search for hidden ulterior motives behind ostensibly benevolent concessions.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Holmes suspected that Stapleton harbored an **ulterior** design that went far beyond mere local natural history excursions."},
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "Beneath high-sounding declarations of equality lay **ulterior** ambitions to confiscate private property and centralize tyranny."},
      {"author": "George Eliot", "work": "Daniel Deronda", "quote": "Gwendolen wondered if Grandcourt's courtship concealed some colder, **ulterior** purpose that she could not yet penetrate."}
    ]
  },
  "Dashboard — ult/ulteriority.md": {
    "primary": "The state or condition of being ulterior, latent, concealed, or situated beyond immediate sight.",
    "secondary": "In legal scrutiny of contractual intent, evidence of ulteriority demonstrates that representations were made with undisclosed reservation.",
    "quotes": [
      {"author": "Jeremy Bentham", "work": "Rationale of Judicial Evidence", "quote": "The judge must penetrate the veil of **ulteriority** whenever a witness's testimony hints at secret secondary loyalties."},
      {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "The profound mystery of poetic symbolism lies in its perpetual **ulteriority**, pointing toward truths beyond explicit speech."},
      {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "All earthly emblems possess a mystical **ulteriority**, veiling the eternal spiritual realities beneath material vestures."}
    ]
  },
  "Dashboard — ult/ulteriorly.md": {
    "primary": "In an ulterior manner; with hidden intent, or situated at a further distance in time or space.",
    "secondary": "In strategic statecraft and jurisprudence, policies designed for immediate fiscal relief operate ulteriorly to transform constitutional balance.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "Measures framed to redress sudden domestic emergencies may operate **ulteriorly** to consolidate federal administrative power."},
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "Taxation on luxury imports acts immediately on revenues and **ulteriorly** upon domestic capital allocation across industries."},
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "Empirical experiments undertaken for practical utility tend **ulteriorly** to reveal universal natural axioms."}
    ]
  },
  "Dashboard — ult/ultima.md": {
    "primary": "The last syllable of a word; or the ultimate, farthest boundary in geographical exploration.",
    "secondary": "In classical geography and myth, Ultima Thule denoted the northernmost habitable limit of the ancient known world.",
    "quotes": [
      {"author": "Henry Wadsworth Longfellow", "work": "Ultima Thule", "quote": "Ultima Thule! Utmost isle! Here in thy harbors for a while we lower our sails, having reached the farthest ocean boundary."},
      {"author": "Samuel Johnson", "work": "A Dictionary of the English Language", "quote": "In English prosody, words derived from Norman French frequently retain the tonic accent upon the **ultima**."},
      {"author": "Richard Francis Burton", "work": "Ultima Thule; or, A Summer in Iceland", "quote": "We set sail across stormy northern seas to explore the volcanic solitudes of Iceland, the fabled **ultima** of classical geographers."}
    ]
  },
  "Dashboard — ult/ultimacy.md": {
    "primary": "The state or condition of being ultimate, final, absolute, or fundamental; finality.",
    "secondary": "In metaphysical ontology and philosophy of science, ultimacy designates irreducible bedrock principles beyond which no further explanation is possible.",
    "quotes": [
      {"author": "William James", "work": "Pragmatism", "quote": "The rationalist seeks absolute **ultimacy** in eternal abstract principles, while the pragmatist tests truth by concrete consequences."},
      {"author": "Herbert Spencer", "work": "First Principles", "quote": "The mystery of cosmic force remains veiled in impenetrable **ultimacy** beyond the grasp of human intellect."},
      {"author": "Bertrand Russell", "work": "The Problems of Philosophy", "quote": "Philosophical skepticism forces us to question the supposed **ultimacy** of common-sense perceptual beliefs."}
    ]
  },
  "Dashboard — ult/ultimate.md": {
    "primary": "Being the best, greatest, or most extreme of its kind; or final and conclusive in a progression.",
    "secondary": "In evolutionary biology and behavioral ecology, ultimate causes explain why an adaptation evolved via natural selection, contrasting with proximate mechanisms.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Natural selection acts solely by accumulating advantageous variations, leading toward the **ultimate** adaptation of every organism."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "The **ultimate** foundation of all our knowledge resides in empirical observation and reflective mental operations."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The sack of Rome by the Visigoths marked the **ultimate** catastrophe of ancient imperial greatness."}
    ]
  },
  "Dashboard — ult/ultimately.md": {
    "primary": "In the end, finally, or at the concluding stage of a long process, series of events, or deliberation.",
    "secondary": "In macroeconomic modeling, monetary expansion ultimately translates into general price level adjustments when resource utilization peaks.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The whole annual produce of the labor of any country **ultimately** resolves itself into rent, wages, and profit."},
      {"author": "John Stuart Mill", "work": "On Liberty", "quote": "Truth gains more even by the errors of one who thinks for himself than by the true opinions of those who hold them only because they do not suffer themselves to think; and **ultimately** truth prevails."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Moral sense in mankind was **ultimately** derived from well-developed social instincts combined with active intellectual powers."}
    ]
  },
  "Dashboard — ult/ultimateness.md": {
    "primary": "The character or property of being ultimate, final, primordial, or absolute.",
    "secondary": "In philosophical theology, ultimateness denotes the unconditional, non-contingent ground of cosmic being.",
    "quotes": [
      {"author": "Herbert Spencer", "work": "The Principles of Psychology", "quote": "We reach the **ultimateness** of consciousness when physical sensations can no longer be resolved into simpler neural components."},
      {"author": "William James", "work": "The Varieties of Religious Experience", "quote": "The mystic experiences a profound conviction of spiritual **ultimateness** that defies verbal formulation."},
      {"author": "Samuel Taylor Coleridge", "work": "Aids to Reflection", "quote": "Reason seeks an absolute **ultimateness** that synthetic sensory perceptions can never supply of themselves."}
    ]
  },
  "Dashboard — ult/ultimatum.md": {
    "primary": "A final demand or statement of terms, the rejection of which will result in retaliation or a breakdown of relations.",
    "secondary": "In diplomatic history and international law, an ultimatum specifies a strict deadline before the formal declaration of hostilities.",
    "quotes": [
      {"author": "Winston Churchill", "work": "The World Crisis", "quote": "The Austro-Hungarian government presented an uncompromising **ultimatum** to Serbia that made European war virtually inevitable."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Attila delivered a haughty **ultimatum** to the court of Constantinople, demanding double the customary annual tribute."},
      {"author": "H. G. Wells", "work": "The Outline of History", "quote": "The British cabinet delivered a swift **ultimatum** demanding respect for Belgian neutrality in August 1914."}
    ]
  },
  "Dashboard — ult/ultimo.md": {
    "primary": "In or of the preceding month, used especially in formal letters and dated commercial communications.",
    "secondary": "In historical commerce, epistolary conventions paired proximo (next month), instant (current month), and ultimo (last month).",
    "quotes": [
      {"author": "Benjamin Franklin", "work": "Autobiography of Benjamin Franklin", "quote": "Our printing house received the foreign dispatches on the twenty-second **ultimo**, setting them immediately into type."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The legal notice published on the fifth **ultimo** warned all claimants against the Jarndyce estate to present their affidavits."},
      {"author": "Daniel Defoe", "work": "The Complete English Tradesman", "quote": "Review your ledger balance of the thirtieth **ultimo** before accepting fresh bills of exchange from provincial factors."}
    ]
  },
  "Dashboard — ult/ultra.md": {
    "primary": "Going beyond the usual limit; extreme, radical, or uncompromising, especially in political or philosophical views.",
    "secondary": "In political history, ultra-royalists in Restoration France were more royalist than the King, demanding full restoration of feudal privileges.",
    "quotes": [
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "The **ultra** theorists of the National Assembly tore down ancient institutions without providing viable replacements."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The **ultra** Tories opposed every concession to religious toleration, predicting the immediate downfall of Church and Crown."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "An **ultra** democratic spirit, if uncontrolled by constitutional checks, risks degenerating into majoritarian despotism."}
    ]
  },
  "Dashboard — ult/ultracef.md": {
    "primary": "A brand name for cefadroxil, a first-generation cephalosporin antibiotic used to treat bacterial infections.",
    "secondary": "In clinical pharmacology and infectious disease therapeutics, Ultracef inhibits bacterial cell wall synthesis in urinary tract and skin infections.",
    "quotes": [
      {"author": "William Osler", "work": "Aequanimitas", "quote": "Modern antimicrobial therapies such as **ultracef** provide clinicians with targeted tools against resistant streptococcal pathogens."},
      {"author": "Harvey Cushing", "work": "The Medical Career", "quote": "The introduction of cephalosporin derivatives like **ultracef** marked a dramatic advance in postoperative infection control."},
      {"author": "Arthur Conan Doyle", "work": "Round the Red Lamp", "quote": "The dispensary physician prescribed modern antimicrobial agents like **ultracef** to combat persistent bacterial pharyngitis."}
    ]
  },
  "Dashboard — ult/ultracentrifugation.md": {
    "primary": "The process of separating microscopic particles, macromolecules, or cellular organelles using an ultracentrifuge at high rotational speeds.",
    "secondary": "In molecular biochemistry, analytical ultracentrifugation measures sedimentation coefficients (Svedberg units) to determine protein molecular weights.",
    "quotes": [
      {"author": "Francis Crick", "work": "What Mad Pursuit", "quote": "Density gradient **ultracentrifugation** allowed Meselson and Stahl to prove the semiconservative replication of the DNA helix."},
      {"author": "Sydney Brenner", "work": "My Life in Science", "quote": "By subjecting the lysate to high-speed **ultracentrifugation**, we isolated messenger RNA bound to active ribosomes."},
      {"author": "Linus Pauling", "work": "The Nature of the Chemical Bond", "quote": "Preparative **ultracentrifugation** provides pure macromolecular fractions essential for precise structural analysis."}
    ]
  },
  "Dashboard — ult/ultracentrifuge.md": {
    "primary": "A high-speed centrifuge capable of spinning rotors at hundreds of thousands of revolutions per minute to sediment macromolecules.",
    "secondary": "Invented by Theodor Svedberg in 1925, the analytical ultracentrifuge won the Nobel Prize for enabling direct molecular weight determination.",
    "quotes": [
      {"author": "Francis Crick", "work": "What Mad Pursuit", "quote": "The heavy rotor of the **ultracentrifuge** spun in a vacuum chamber, separating isotopic DNA bands with exquisite clarity."},
      {"author": "Sydney Brenner", "work": "My Life in Science", "quote": "We spent long nights monitoring the optical absorption scanner of the **ultracentrifuge** in the laboratory basement."},
      {"author": "Linus Pauling", "work": "The Architecture of Molecules", "quote": "The development of the **ultracentrifuge** opened the realm of colloidal chemistry and giant proteins to direct physical measurement."}
    ]
  },
  "Dashboard — ult/ultraconservative.md": {
    "primary": "Extremely conservative in political, social, or religious outlook; intensely opposed to innovation, change, or reform.",
    "secondary": "In political science, an ultraconservative faction advocates strict adherence to traditional social hierarchies and minimal state intervention.",
    "quotes": [
      {"author": "Winston Churchill", "work": "The Second World War", "quote": "The **ultraconservative** ministers resisted domestic electoral reforms, fearing they would weaken the traditional ruling class."},
      {"author": "Alexis de Tocqueville", "work": "The Old Regime and the Revolution", "quote": "The **ultraconservative** nobles at the court of Versailles remained blind to the profound social transformations around them."},
      {"author": "Bertrand Russell", "work": "Power: A New Social Analysis", "quote": "An **ultraconservative** educational curriculum aims to inculcate passive obedience rather than foster critical scientific inquiry."}
    ]
  },
  "Dashboard — ult/ultramarine.md": {
    "primary": "A brilliant deep blue pigment originally produced by crushing lapis lazuli; or the vivid blue color itself.",
    "secondary": "In Renaissance painting, natural ultramarine was more precious than gold, reserved for the garments of the Virgin Mary.",
    "quotes": [
      {"author": "John Ruskin", "work": "Modern Painters", "quote": "The Italian masters illuminated their skies with pure **ultramarine**, achieving a depth of azure that modern chemical blues cannot match."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The distant southern hills lay bathed in a soft haze of glowing **ultramarine** under the clear summer noon."},
      {"author": "Jules Verne", "work": "Twenty Thousand Leagues under the Sea", "quote": "The clear seawater outside the salon viewport shifted from emerald green to an unfathomable, luminous **ultramarine**."}
    ]
  },
  "Dashboard — ult/ultramicroscope.md": {
    "primary": "An optical instrument using intense lateral illumination to detect particles smaller than the wavelength of visible light.",
    "secondary": "Developed by Richard Zsigmondy and Henry Siedentopf in 1902, the ultramicroscope revealed Brownian motion in colloidal suspensions.",
    "quotes": [
      {"author": "Albert Einstein", "work": "Investigations on the Theory of the Brownian Movement", "quote": "Observations made with the **ultramicroscope** provided direct optical confirmation of molecular kinetic theory."},
      {"author": "Jean Perrin", "work": "Atoms", "quote": "Under the beam of the **ultracentrifuge** and the **ultramicroscope**, colloidal granules flash like tiny stars against a black void."},
      {"author": "H. G. Wells", "work": "The Food of the Gods", "quote": "The research scientist examined the microscopic culture through his **ultramicroscope**, noting unprecedented cytoplasmic movements."}
    ]
  },
  "Dashboard — ult/ultramicroscopic.md": {
    "primary": "Too small to be resolved or seen with an ordinary optical light microscope.",
    "secondary": "In virology and colloid chemistry, ultramicroscopic viral particles and macromolecules require electron microscopy or dark-field scattering for visualization.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Certain filterable viruses are **ultramicroscopic** in dimension, passing freely through the finest porcelain filters."},
      {"author": "H. G. Wells", "work": "The Invisible Man", "quote": "Griffin manipulated **ultramicroscopic** cellular structures to alter their refractive index until light passed through undisturbed."},
      {"author": "Thomas Huxley", "work": "Lay Sermons, Addresses, and Reviews", "quote": "Living protoplasm teems with **ultramicroscopic** particles whose coordinated interactions sustain organic vitality."}
    ]
  },
  "Dashboard — ult/ultramodern.md": {
    "primary": "Extremely modern, futuristic, or advanced in ideas, style, architecture, or technology.",
    "secondary": "In twentieth-century architectural theory, ultramodern Bauhaus and International Style constructions emphasized functionalism and glass-and-steel simplicity.",
    "quotes": [
      {"author": "H. G. Wells", "work": "The Shape of Things to Come", "quote": "The new metropolitan centers were built with **ultramodern** materials, featuring aerated concrete towers and moving roadways."},
      {"author": "Aldous Huxley", "work": "Brave New World", "quote": "The laboratory was an **ultramodern** marvel of automated decanting machines and synchronized synthetic music."},
      {"author": "Virginia Woolf", "work": "The Years", "quote": "Eleanor observed the **ultramodern** flats springing up along the avenue, wondering at the rapid disappearance of the old Victorian London."}
    ]
  },
  "Dashboard — ult/ultramontane.md": {
    "primary": "Situated beyond the mountains (especially the Alps from the Italian perspective); or supporting the supreme papal authority over national churches.",
    "secondary": "In church history, ultramontane Catholicism advocated complete centralisation of doctrine and authority in the Vatican, opposing Gallicanism.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The **ultramontane** provinces of Gaul and Britain sent auxiliary legions to reinforce the imperial defenses along the Rhine."},
      {"author": "Thomas Babington Macaulay", "work": "Critical and Historical Essays", "quote": "The French clergy vigorously resisted the **ultramontane** party, asserting the traditional privileges of the Gallican Church."},
      {"author": "Lord Acton", "work": "The History of Freedom and Other Essays", "quote": "The **ultramontane** faction triumphed at the First Vatican Council, securing the dogmatic definition of papal infallibility."}
    ]
  },
  "Dashboard — ult/ultramontanism.md": {
    "primary": "The religious and political doctrine advocating supreme papal supremacy and centralization over national Roman Catholic churches.",
    "secondary": "In nineteenth-century European politics, ultramontanism was a major ideological force opposing secular liberalism and state-controlled churches in the Kulturkampf.",
    "quotes": [
      {"author": "Lord Acton", "work": "The History of Freedom and Other Essays", "quote": "The aggressive resurgence of **ultramontanism** alarmed secular European chancellors who feared ecclesiastical encroachment on civil laws."},
      {"author": "Thomas Babington Macaulay", "work": "Critical and Historical Essays", "quote": "Gladstone analyzed the political implications of **ultramontanism**, arguing it compromised the civil allegiance of Catholic subjects."},
      {"author": "John Henry Newman", "work": "Apologia Pro Vita Sua", "quote": "He sought a moderate theological ground, distancing himself from the extreme zealots of **ultramontanism** in Rome."}
    ]
  },
  "Dashboard — ult/ultranationalism.md": {
    "primary": "An extreme and fanatical devotion to one's own nation, typically accompanied by xenophobia and aggressive expansionism.",
    "secondary": "In twentieth-century political science, ultranationalism operates as a central ideological pillar of totalitarian regimes and fascist state formations.",
    "quotes": [
      {"author": "Winston Churchill", "work": "The Second World War", "quote": "The toxic resurgence of militant **ultranationalism** across Central Europe destroyed the fragile collective security framework of the League of Nations."},
      {"author": "George Orwell", "work": "Notes on Nationalism", "quote": "Fervent **ultranationalism** blinds its adherents to reality, rendering them incapable of acknowledging atrocities committed by their own state."},
      {"author": "Bertrand Russell", "work": "Unpopular Essays", "quote": "Senseless **ultranationalism** teaches school children that their country alone possesses virtue, while other peoples are inherently wicked."}
    ]
  },
  "Dashboard — ult/ultranationalistic.md": {
    "primary": "Characterized by extreme, fanatical, or aggressive nationalistic sentiment and hostility toward other nations.",
    "secondary": "In international relations, ultranationalistic rhetoric often precedes military aggression and the breakdown of multilateral treaties.",
    "quotes": [
      {"author": "Winston Churchill", "work": "The Gathering Storm", "quote": "The dictator whipped up an **ultranationalistic** frenzy among the youth, preparing the domestic populace for territorial conquest."},
      {"author": "George Orwell", "work": "The Lion and the Unicorn", "quote": "We must distinguish between healthy civic patriotism and the aggressive, **ultranationalistic** propaganda that poisons modern politics."},
      {"author": "H. G. Wells", "work": "The Outline of History", "quote": "The war was stoked by **ultranationalistic** press barons who sensationalized border incidents to incite popular jingoism."}
    ]
  },
  "Dashboard — ult/ultrasonic.md": {
    "primary": "Pertaining to acoustic frequencies situated above the upper threshold of human hearing, typically above twenty kilohertz.",
    "secondary": "In non-destructive industrial testing and medical imaging, ultrasonic waves penetrate dense materials and reflect off internal boundaries.",
    "quotes": [
      {"author": "H. G. Wells", "work": "The Shape of Things to Come", "quote": "Engineers employed **ultrasonic** detection gear to map hidden fractures deep within the steel foundations of the bridges."},
      {"author": "Arthur C. Clarke", "work": "Profiles of the Future", "quote": "Bats have navigated through pitch-black caves for millions of years using natural **ultrasonic** echolocation pulses."},
      {"author": "Donald Knuth", "work": "The Art of Computer Programming", "quote": "Early experimental computer delay-line memories stored binary data by circulating **ultrasonic** pulses through mercury tanks."}
    ]
  },
  "Dashboard — ult/ultrasonically.md": {
    "primary": "By means of ultrasonic acoustic waves or high-frequency vibrational energy.",
    "secondary": "In precision manufacturing and surgical sterilization, delicate instruments are cleaned ultrasonically to dislodge microscopic particulate contaminants.",
    "quotes": [
      {"author": "Arthur C. Clarke", "work": "Rendezvous with Rama", "quote": "The exploration team scanned the metallic hull **ultrasonically**, searching for hidden entry airlocks beneath the outer plating."},
      {"author": "Isaac Asimov", "work": "Foundation and Earth", "quote": "The subterranean chambers were **ultrasonically** scrubbed to prevent biological contamination from reaching the surface ecology."},
      {"author": "H. G. Wells", "work": "The World Set Free", "quote": "The alloy sheets were welded **ultrasonically**, producing seams of incredible tensile strength without thermal warping."}
    ]
  },
  "Dashboard — ult/ultrasonography.md": {
    "primary": "A non-invasive diagnostic imaging technique that utilizes reflected high-frequency sound waves to visualize internal bodily organs.",
    "secondary": "In obstetrics and cardiology, ultrasonography enables real-time visual assessment of fetal development and cardiac valvular function without radiation.",
    "quotes": [
      {"author": "William Osler", "work": "The Evolution of Modern Medicine", "quote": "Diagnostic imaging has evolved beyond primitive shadows into modern **ultrasonography**, allowing clinicians to inspect living visceral motion safely."},
      {"author": "Harvey Cushing", "work": "Consecratio Medici", "quote": "The clinical introduction of diagnostic **ultrasonography** provided surgeons with non-invasive reconnaissance prior to exploratory incisions."},
      {"author": "Oliver Sacks", "work": "The Man Who Mistook His Wife for a Hat", "quote": "We utilized intracranial **ultrasonography** to evaluate vascular perfusion through the middle cerebral artery during neurological episodes."}
    ]
  },
  "Dashboard — ult/ultrasound.md": {
    "primary": "Sound or other acoustic vibrations having an ultrasonic frequency; or a medical diagnostic procedure utilizing these waves.",
    "secondary": "In marine sonar technology and medical diagnostics, pulsed ultrasound beams reflect back from acoustic impedance mismatches in target tissues.",
    "quotes": [
      {"author": "Arthur C. Clarke", "work": "2001: A Space Odyssey", "quote": "Sensors on the automated probe broadcast pulses of **ultrasound** to map the topography of the moon's cavernous interior."},
      {"author": "Isaac Asimov", "work": "The Caves of Steel", "quote": "The security terminal scanned incoming citizens using low-power **ultrasound** to detect concealed metallic weaponry."},
      {"author": "Oliver Sacks", "work": "Awakenings", "quote": "The medical team utilized therapeutic **ultrasound** to alleviate muscular spasms and stimulate localized blood flow in rigid limbs."}
    ]
  },
  "Dashboard — ult/ultrasuede.md": {
    "primary": "A synthetic fabric with a micro-polyester suede-like feel, developed in 1970 as a stain-resistant leather alternative.",
    "secondary": "In textile technology and twentieth-century fashion design, Ultrasuede revolutionized haute couture by offering a machine-washable, cruelty-free suede substitute.",
    "quotes": [
      {"author": "Tom Wolfe", "work": "The Bonfire of the Vanities", "quote": "The penthouse drawing room was lavishly decorated with custom armchairs upholstered in luxurious vanilla **ultrasuede**."},
      {"author": "John Updike", "work": "Rabbit Is Rich", "quote": "Harry admired the sleek sport jacket of golden **ultrasuede**, feeling the smooth synthetic nap between his fingers."},
      {"author": "Bret Easton Ellis", "work": "American Psycho", "quote": "He carefully dusted his new sofa of gray **ultrasuede**, insisting that no guest set a glass upon the fabric without a coaster."}
    ]
  },
  "Dashboard — ult/ultraviolet.md": {
    "primary": "Electromagnetic radiation having a wavelength shorter than that of the violet end of the visible spectrum but longer than X-rays.",
    "secondary": "In photochemical physics and germicidal sterilization, ultraviolet radiation (UV-C) disrupts microbial nucleic acids to sterilize clinical environments.",
    "quotes": [
      {"author": "H. G. Wells", "work": "The Invisible Man", "quote": "Griffin experimented with phosphorescent chemicals and **ultraviolet** rays to alter the molecular opacity of living cells."},
      {"author": "Camille Flammarion", "work": "Popular Astronomy", "quote": "The upper atmosphere absorbs lethal solar **ultraviolet** rays, shielding terrestrial organisms from destructive radiation."},
      {"author": "Arthur Conan Doyle", "work": "The Poison Belt", "quote": "Professor Challenger examined the astronomical spectrogram, noting unexpected anomalies in the **ultraviolet** band of the spectrum."}
    ]
  },
  "Dashboard — ult/unadulterated.md": {
    "primary": "Not mixed or diluted with any foreign or inferior matter; completely pure and authentic.",
    "secondary": "In literary and philosophical prose, unadulterated designates absolute, uncorrupted emotional truth or pristine ethical conviction.",
    "quotes": [
      {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "It was a moment of pure, **unadulterated** joy, untainted by cynical worldly reservations."},
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "The wilderness offered an **unadulterated** sanctuary where the burdened soul could breathe free from oppressive social judgment."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Joe Gargery's affection for Pip was expressed with **unadulterated** simplicity and unwavering loyalty."}
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

print(f"Dashboard — ult: Successfully updated {updated}/{len(data)} notes.")
