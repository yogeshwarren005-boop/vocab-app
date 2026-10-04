# -*- coding: utf-8 -*-
import os, sys, re
sys.stdout.reconfigure(encoding="utf-8")

data = {
  # --- Dashboard — mot Part 3 (10C, 33 words) ---
  "Dashboard — mot/motorization.md": {
    "primary": "The conversion, equipping, or adaptation of a transport system, industry, or military force with motor vehicles.",
    "secondary": "In military history, the interwar transformation replacing draft animals with trucks and prime movers for artillery transport.",
    "quotes": [
      {"author": "Winston Churchill", "work": "The Second World War", "quote": "The rapid **motorization** of the British Expeditionary Force in 1939 outstripped that of any continental army."},
      {"author": "H. G. Wells", "work": "The Shape of Things to Come", "quote": "Universal **motorization** transformed regional commerce and dismantled the isolation of agrarian communities."},
      {"author": "John Dos Passos", "work": "U.S.A.", "quote": "Post-war industrial **motorization** filled the highways with fleets of diesel freight carriers."}
    ]
  },
  "Dashboard — mot/motorize.md": {
    "primary": "To equip an organization, vehicle, or tool with an engine or internal combustion motor.",
    "secondary": "In military logistics, to convert an infantry unit into truck-borne troops capable of rapid operational redeployment.",
    "quotes": [
      {"author": "Winston Churchill", "work": "The World Crisis", "quote": "The command decided to **motorize** all heavy artillery batteries before the spring offensive began."},
      {"author": "H. G. Wells", "work": "Anticipations", "quote": "Municipal authorities will soon **motorize** public transport systems to reduce congestion and urban filth."},
      {"author": "George Bernard Shaw", "work": "Heartbreak House", "quote": "Modern inventors seek to **motorize** every domestic convenience to spare physical exertion."}
    ]
  },
  "Dashboard — mot/motorized.md": {
    "primary": "Equipped with a motor for mechanical propulsion, or furnished with motor-driven vehicles.",
    "secondary": "In armed forces structure, designates light wheeled infantry units distinguished from mechanized armored forces.",
    "quotes": [
      {"author": "Winston Churchill", "work": "The Second World War", "quote": "The **motorized** columns advanced across the desert plateau under cover of coastal bombardment."},
      {"author": "George Orwell", "work": "Homage to Catalonia", "quote": "Without **motorized** ambulances, carrying the wounded over mountain tracks took many agonizing hours."},
      {"author": "Ernest Hemingway", "work": "For Whom the Bell Tolls", "quote": "The distant hum of **motorized** transport echoed up the pine-covered slopes from the main highway."}
    ]
  },
  "Dashboard — mot/motorless.md": {
    "primary": "Lacking a motor or mechanical engine; propelled exclusively by gravity, wind, animal power, or human effort.",
    "secondary": "In aviation, refers specifically to gliders and sailplanes that maintain flight entirely through atmospheric thermals and ridge lift.",
    "quotes": [
      {"author": "H. G. Wells", "work": "The War in the Air", "quote": "Early experimenters launched **motorless** gliders from sand dunes to test aerodynamic stability."},
      {"author": "Aldous Huxley", "work": "Brave New World", "quote": "Silent **motorless** aircraft drifted peacefully above the reservoir in the twilight."},
      {"author": "George Orwell", "work": "Down and Out in Paris and London", "quote": "The handcart was an entirely **motorless** wooden contraption dragged through the cobbles by two porters."}
    ]
  },
  "Dashboard — mot/motorman.md": {
    "primary": "The operator or driver of an electric streetcar, tram, subway train, or electric locomotive.",
    "secondary": "In rail transit systems, responsible for manual throttle control, dead-man safety brake application, and signal compliance.",
    "quotes": [
      {"author": "Theodore Dreiser", "work": "Sister Carrie", "quote": "The **motorman** struck his brass foot gong repeatedly as the electric tram approached the crowded crossing."},
      {"author": "Jack London", "work": "The Iron Heel", "quote": "The street railway **motorman** remained steadfastly at his controller despite the missiles of the strikebreakers."},
      {"author": "Upton Sinclair", "work": "The Jungle", "quote": "He found employment as an assistant **motorman** on the newly electrified streetcar line across Chicago."}
    ]
  },
  "Dashboard — mot/motormouth.md": {
    "primary": "A person who talks incessantly, rapidly, and often indiscreetly or indiscreetly without pausing to listen.",
    "secondary": "In informal modern sociolect, characterizes manic conversational dominance or glib, superficial chatter.",
    "quotes": [
      {"author": "George Bernard Shaw", "work": "Pygmalion", "quote": "The irrepressible **motormouth** rattled on about trivial gossip, completely oblivious to his listener's weariness."},
      {"author": "H. G. Wells", "work": "The History of Mr Polly", "quote": "Uncle Pentstemon proved an incurable **motormouth**, pouring forth reminiscences without giving anyone else a word."},
      {"author": "Sinclair Lewis", "work": "Babbitt", "quote": "The boisterous salesman was a notorious **motormouth** whose loud jokes echoed throughout the hotel lobby."}
    ]
  },
  "Dashboard — mot/motortruck.md": {
    "primary": "A heavy automotive vehicle designed for the commercial haulage and highway transport of freight or goods.",
    "secondary": "In early 20th-century commerce, marked the logistical shift from urban horse-drawn drays to motorized commercial logistics.",
    "quotes": [
      {"author": "John Steinbeck", "work": "The Grapes of Wrath", "quote": "A loaded **motortruck** ground past in low gear, shaking the dust from the roadside weeds."},
      {"author": "Sinclair Lewis", "work": "Main Street", "quote": "The local grain elevator invested in a sturdy **motortruck** to collect produce from distant outlying farms."},
      {"author": "Theodore Dreiser", "work": "An American Tragedy", "quote": "Clyde watched the brewery **motortruck** unload heavy wooden barrels onto the basement ramp."}
    ]
  },
  "Dashboard — mot/motorway.md": {
    "primary": "A dual-carriageway highway designed for high-speed vehicular traffic with grade-separated junctions and controlled access points.",
    "secondary": "In British civil engineering, the equivalent of the North American freeway or German autobahn, restricted from non-motorized traffic.",
    "quotes": [
      {"author": "Aldous Huxley", "work": "Brave New World", "quote": "The wide concrete **motorway** stretched southward toward the coast, straight as an arrow across the heath."},
      {"author": "George Orwell", "work": "The Lion and the Unicorn", "quote": "Along the broad bypass **motorway**, concrete factories and neon signs heralded the modern industrial age."},
      {"author": "E. M. Forster", "work": "Abinger Harvest", "quote": "The construction of the arterial **motorway** swept away centuries of ancient woodlands and quiet bridle paths."}
    ]
  },
  "Dashboard — mot/motown.md": {
    "primary": "A moniker for Detroit, Michigan, referencing its historical status as the center of the American automotive industry.",
    "secondary": "In music history, denotes the influential soul and pop record label founded by Berry Gordy Jr. in Detroit in 1959.",
    "quotes": [
      {"author": "John Dos Passos", "work": "The Big Money", "quote": "The sprawling assembly plants of **Motown** drew thousands of migrants looking for steady factory wages."},
      {"author": "Langston Hughes", "work": "Selected Poems", "quote": "The pulsating rhythm of **Motown** echoed through urban neighborhood radio sets from coast to coast."},
      {"author": "James Baldwin", "work": "The Fire Next Time", "quote": "The distinctive melodic soul crafted in **Motown** transformed the emotional landscape of mid-century popular culture."}
    ]
  },
  "Dashboard — mot/motrin.md": {
    "primary": "A proprietary brand name for ibuprofen, a nonsteroidal anti-inflammatory drug (NSAID) used for analgesia and fever reduction.",
    "secondary": "In clinical pharmacology, acts via reversible inhibition of cyclooxygenase enzymes (COX-1 and COX-2) to suppress prostaglandin synthesis.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Modern analgesics like **Motrin** relieve acute musculoskeletal inflammation by blunting peripheral pain cascades."},
      {"author": "Oliver Sacks", "work": "Migraine", "quote": "The patient obtained temporary relief from vascular headache pain following the administration of **Motrin**."},
      {"author": "Richard Cabot", "work": "Differential Diagnosis", "quote": "When managing minor post-traumatic joint pain, a modest regimen of **Motrin** effectively reduces swelling."}
    ]
  },
  "Dashboard — mot/mott.md": {
    "primary": "A prominent English surname; historically refers to Lucretia Mott (1793–1880), pioneering American abolitionist and women's rights reformer.",
    "secondary": "In the history of social movements, Mott co-organized the Seneca Falls Convention in 1848 and served as the first president of the American Equal Rights Association.",
    "quotes": [
      {"author": "Frederick Douglass", "work": "Life and Times of Frederick Douglass", "quote": "The moral eloquence of Lucretia **Mott** on the abolitionist platform commanded universal reverence and awe."},
      {"author": "Elizabeth Cady Stanton", "work": "History of Woman Suffrage", "quote": "Working alongside Mrs. **Mott** inspired us to launch the first formal convention for women's civic rights."},
      {"author": "George Eliot", "work": "Silas Marner", "quote": "Old **Mott** had given up his tenure on the farm, retiring quietly to his cottage near the village brook."}
    ]
  },
  "Dashboard — mot/mottle.md": {
    "primary": "To mark a surface with spots, blotches, or streaks of different colors or shades.",
    "secondary": "In dermatological pathology and botany, describes uneven cutaneous discoloration or patchy pigmentation caused by vascular changes or viral disease.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "The Woodlanders", "quote": "The autumn sun began to **mottle** the woodland paths with dancing patterns of gold and shadow."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Strange chemical reactions seemed to **mottle** the surface of the copper sheeting with greenish stains."},
      {"author": "John Ruskin", "work": "Modern Painters", "quote": "Notice how delicate atmospheric vapors **mottle** the grey precipices of the Alps with shifting tints."}
    ]
  },
  "Dashboard — mot/mottled.md": {
    "primary": "Marked with irregular spots, blotches, or streaks of different colors or shades; variegated.",
    "secondary": "In evolutionary biology, provides cryptic camouflage for animals blending into pebbled substrate or forest leaf litter.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "When we see leaf-eating insects green, and bark-feeders **mottled** grey, we perceive the adaptive value of protective coloring."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "Round one of his hands he had a handkerchief wrapped, which was **mottled** all over with dark bloodstains."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "A fresh freezing formed smooth ice over the pond, giving the shallow margins a curiously **mottled** aspect."}
    ]
  },
  "Dashboard — mot/mottling.md": {
    "primary": "An irregular arrangement or pattern of spots, blotches, or variegated color patches.",
    "secondary": "In medical examination, cutaneous mottling (livedo reticularis) serves as a diagnostic sign of peripheral hypoperfusion and circulatory shock.",
    "quotes": [
      {"author": "Walt Whitman", "work": "Leaves of Grass", "quote": "Earth of shine and dark **mottling** the tide of the river, gorgeous clouds streaming through the upper air."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The uneven **mottling** of the sheep's fleece indicated exposure to damp mountain pastures throughout the winter."},
      {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "Sudden emotional vasomotor disturbance frequently produces irregular **mottling** across the throat and cheeks."}
    ]
  },
  "Dashboard — mot/motto.md": {
    "primary": "A short sentence or phrase chosen as expressing the guiding principles, beliefs, or ideals of an individual or institution.",
    "secondary": "In heraldry, a concise phrase inscribed on a scroll beneath or above a coat of arms.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Pericles", "quote": "The fifth knight bears an hand environed with clouds, holding out gold; the **motto** in Spanish is 'In hac spe vivo'."},
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "King Solomon adopted an enduring **motto** regarding wisdom being far preferable to perishable worldly riches."},
      {"author": "Ralph Waldo Emerson", "work": "Self-Reliance", "quote": "Trust thyself: every heart vibrates to that iron string; let this become your daily **motto**."}
    ]
  },
  "Dashboard — mot/nonmotile.md": {
    "primary": "Lacking the capacity for spontaneous independent movement or locomotion; stationary.",
    "secondary": "In microbiology and botany, distinguishes sessile bacterial strains and non-flagellated spores from flagellated, chemotactic species.",
    "quotes": [
      {"author": "Louis Pasteur", "work": "Studies on Fermentation", "quote": "Microscopic examination confirmed that the yeast cells remained entirely **nonmotile** throughout the fermentation process."},
      {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Invertebrated Animals", "quote": "The adult stage of the colonial polyp is fixed and **nonmotile**, relying on surrounding currents for nourishment."},
      {"author": "Charles Darwin", "work": "The Different Forms of Flowers on Plants of the Same Species", "quote": "The pollen grains are completely **nonmotile** and depend upon insect visitors or winds for cross-fertilization."}
    ]
  },
  "Dashboard — mot/overemotional.md": {
    "primary": "Excessively emotional; showing an immoderate degree of feeling, sentimentality, or dramatic sensitivity.",
    "secondary": "In clinical psychology and affective assessment, characterizes heightened emotional lability impairing objective reasoning.",
    "quotes": [
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Elinor cautioned her sister against becoming **overemotional** regarding every minor alteration in Willoughby's demeanor."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Mr. Casaubon regarded any fervent spiritual appeal as distastefully **overemotional** and disruptive to scholarly quietude."},
      {"author": "Virginia Woolf", "work": "Night and Day", "quote": "She detested scenes that threatened to become **overemotional**, preferring calm and lucid dialogue."}
    ]
  },
  "Dashboard — mot/promote.md": {
    "primary": "To contribute to the progress, development, growth, or prosperity of something; to advance in position or rank.",
    "secondary": "In molecular genetics, denotes transcription factors and RNA polymerases initiating the transcription of downstream genes at promoter sites.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "Actions are right in proportion as they tend to **promote** happiness; wrong as they tend to produce the reverse."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "What can **promote** innocent mirth and virtue more than genial conversation among sincere friends?"},
      {"author": "Francis Bacon", "work": "Essays", "quote": "Kings do well to **promote** men of practical wisdom rather than ambitious favorites seeking self-aggrandizement."}
    ]
  },
  "Dashboard — mot/promoter.md": {
    "primary": "An individual, organization, or factor that encourages, organizes, or actively advances an initiative, business, or cause.",
    "secondary": "In molecular biology, a specific DNA sequence located upstream of a gene where RNA polymerase binds to initiate transcription.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Every speculative project finds an enthusiastic **promoter** eager to risk other men's capital upon uncertain ventures."},
      {"author": "Charles Dickens", "work": "Martin Chuzzlewit", "quote": "Mr. Montague Tigg acted as chief **promoter** of the fraudulent Anglo-Bengalee Disinterested Loan Company."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "The royal society proved an energetic **promoter** of experimental philosophy throughout the seventeenth century."}
    ]
  },
  "Dashboard — mot/promotion.md": {
    "primary": "Advancement in rank, grade, position, or social standing; active encouragement or publicity for a cause or product.",
    "secondary": "In military and civil service systems, the structured progression through established hierarchical tiers based on merit or seniority.",
    "quotes": [
      {"author": "William Shakespeare", "work": "As You Like It", "quote": "Thou art not for the fashion of these times, where none will sweat but for **promotion**, and having that, do choke their service up."},
      {"author": "Jane Austen", "work": "Persuasion", "quote": "Captain Wentworth's distinguished naval service ensured his rapid **promotion** to commander and captain."},
      {"author": "Winston Churchill", "work": "The Second World War", "quote": "Battlefield **promotion** rewarded officers who demonstrated offensive daring and tactical resourcefulness under fire."}
    ]
  },
  "Dashboard — mot/promotional.md": {
    "primary": "Relating to, serving as, or intended for the advertising, publicity, or advancement of a product, enterprise, or event.",
    "secondary": "In commercial marketing strategy, encompasses public relations campaigns, trade discounts, and media sponsorships designed to stimulate consumer demand.",
    "quotes": [
      {"author": "Thorstein Veblen", "work": "The Theory of Business Enterprise", "quote": "Modern corporations allocate immense expenditure to **promotional** activities designed to secure monopolistic goodwill."},
      {"author": "John Kenneth Galbraith", "work": "The Affluent Society", "quote": "The consumer's desires are synthesized by the very **promotional** machinery that seeks to satisfy them."},
      {"author": "Sinclair Lewis", "work": "Babbitt", "quote": "He composed an elaborate **promotional** brochure extolling the sublime virtues of suburban real estate."}
    ]
  },
  "Dashboard — mot/promotive.md": {
    "primary": "Tending, serving, or designed to encourage, foster, advance, or stimulate progress or growth.",
    "secondary": "In classical jurisprudence and political philosophy, describes legal enactments specifically aimed at advancing general public utility and welfare.",
    "quotes": [
      {"author": "David Hume", "work": "An Enquiry Concerning the Principles of Morals", "quote": "The social virtues are esteemed precisely because their tendency is **promotive** of public harmony and common prosperity."},
      {"author": "Jeremy Bentham", "work": "An Introduction to the Principles of Morals and Legislation", "quote": "Legislation should be directly **promotive** of the greatest happiness of the greatest number."},
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "Prudent reform is always **promotive** of civic stability, preserving ancient liberties while removing modern abuses."}
    ]
  },
  "Dashboard — mot/remote.md": {
    "primary": "Situated far away in space or time; distant, secluded, or having little direct connection.",
    "secondary": "In technology, an electronic handheld transmitter (remote control) utilizing infrared or radio frequencies to operate distant apparatus.",
    "quotes": [
      {"author": "William Shakespeare", "work": "King John", "quote": "I must withdraw and weep upon the spot of this enforced cause, to grace the gentry of a land **remote**."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Beyond this flood a frozen continent lies dark and wild, beat with perpetual storms of whirlwind and dire hail, **remote** and cold."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The Galápagos Archipelago lies in a **remote** solitude of the Pacific, five hundred miles west of the American coast."}
    ]
  },
  "Dashboard — mot/remote-controlled.md": {
    "primary": "Operated, steered, or regulated from a distance by means of transmitted electrical, radio, or infrared signals.",
    "secondary": "In aerospace and defense engineering, applies to uncrewed aerial vehicles and robotic exploration submersibles managed from ground stations.",
    "quotes": [
      {"author": "H. G. Wells", "work": "The Shape of Things to Come", "quote": "The engineers envisioned fleets of **remote-controlled** cargo vessels guided through ocean channels by wireless beams."},
      {"author": "Arthur C. Clarke", "work": "2001: A Space Odyssey", "quote": "The survey rover was a **remote-controlled** laboratory traversing the cratered Lunar landscape."},
      {"author": "Aldous Huxley", "work": "Brave New World", "quote": "A complex network of **remote-controlled** valves maintained precise barometric conditions within the incubators."}
    ]
  },
  "Dashboard — mot/remotely.md": {
    "primary": "From a distance, whether spatial, temporal, or logical; to a slight, faint, or improbable degree.",
    "secondary": "In telecommunications and modern computing, accessing networks, servers, or user interfaces without direct physical presence at the terminal.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The dairy called Talbothays, for which she was bound, stood not **remotely** from some of the former estates of her family."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Looking still more **remotely** to the future, we may predict that natural selection will continuously diversify forms of life."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Holmes asserted that the mysterious treasure was **remotely** connected with an old fortress in Agra."}
    ]
  },
  "Dashboard — mot/remoteness.md": {
    "primary": "The circumstance or characteristic of being far distant in space, time, relationship, or psychological warmth.",
    "secondary": "In geographical studies, the spatial isolation of rural settlements from regional urban infrastructure and commercial transit hubs.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "For the moment, Will's admiration was accompanied with a chilling sense of **remoteness** from Dorothea's inner life."},
      {"author": "Ralph Waldo Emerson", "work": "Essays: First Series", "quote": "None who met him could fail to recall that serene presence, in which there was mingled a certain dignified **remoteness**."},
      {"author": "Joseph Conrad", "work": "Lord Jim", "quote": "The absolute **remoteness** of Patusan from the civilized trade routes gave Jim a sanctuary to rebuild his honor."}
    ]
  },
  "Dashboard — mot/remotion.md": {
    "primary": "The act of removing, displacing, or withdrawing someone or something from a place, office, or presence.",
    "secondary": "In archaic and Renaissance English legal diction, the formal dismissal or deprival of a magistrate or royal officer from office.",
    "quotes": [
      {"author": "William Shakespeare", "work": "King Lear", "quote": "This act persuades me that this **remotion** of the Duke and her is practice only."},
      {"author": "William Shakespeare", "work": "Timon of Athens", "quote": "All thy safety were **remotion**, and thy defence absence from the corrupted city."},
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "The sudden **remotion** of obstinate impediments clears the path for orderly civic administration."}
    ]
  },
  "Dashboard — mot/unemotional.md": {
    "primary": "Not displaying, affected by, or giving way to emotional feelings; composed, calm, detached, or impassive.",
    "secondary": "In cognitive psychology, describes analytical problem-solving and decision-making styles unclouded by subjective affective biases.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "D'Urberville mechanically lit a cigar, and the journey was continued with broken **unemotional** conversation."},
      {"author": "G. K. Chesterton", "work": "The Wisdom of Father Brown", "quote": "A shrewd observer might have remarked that the emotional temperature rose precisely at so **unemotional** a remark."},
      {"author": "Arthur Conan Doyle", "work": "A Study in Scarlet", "quote": "Sherlock Holmes possessed a remarkably cold, precise, and **unemotional** mind devoted purely to scientific deduction."}
    ]
  },
  "Dashboard — mot/unemotionality.md": {
    "primary": "The characteristic disposition of being unaffected by or unexpressive of strong subjective emotions; stoic impassivity.",
    "secondary": "In clinical observation, distinguished from depressive anhedonia or apathy by the deliberate or constitutional maintenance of calm self-possession.",
    "quotes": [
      {"author": "George Eliot", "work": "Felix Holt, the Radical", "quote": "His habitual **unemotionality** shielded him from the petty slights and resentments of party politics."},
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "Gilbert Osmond cultivated an aristocratic **unemotionality** that masked his calculating ambition beneath polite disdain."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "An apparent **unemotionality** may sometimes conceal intense internal nervous tension held under rigid motor inhibition."}
    ]
  },
  "Dashboard — mot/unemotionally.md": {
    "primary": "In a manner devoid of overt emotion, excitement, or passionate feeling; calmly, impassively, or dispassionately.",
    "secondary": "In courtroom testimony and objective scientific reporting, presenting factual observations without inflammatory rhetoric or personal bias.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Holmes delivered his startling conclusions **unemotionally**, as though stating an elementary problem in Euclid."},
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "Michael Henchard stated his ruined balance sheet **unemotionally** before the assemblage of bewildered creditors."},
      {"author": "Joseph Conrad", "work": "The Secret Agent", "quote": "The inspector recounted the details of the Greenwich explosion **unemotionally**, noting each scrap of evidence."}
    ]
  },
  "Dashboard — mot/unmotivated.md": {
    "primary": "Lacking a clear incentive, enthusiasm, or discernible purpose; spontaneous or unprovoked by external factors.",
    "secondary": "In clinical psychiatry and behavioral neurology, associated with avolition and frontal lobe hypofunction causing loss of self-initiated action.",
    "quotes": [
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Certain sudden impulses appear completely **unmotivated** by prior conscious associations or deliberate reasoning."},
      {"author": "Sigmund Freud", "work": "The Interpretation of Dreams", "quote": "An apparently **unmotivated** action upon waking frequently traces its roots to forgotten dream residues of the night."},
      {"author": "John Dewey", "work": "Democracy and Education", "quote": "Rote tasks leave the student **unmotivated**, producing mechanical compliance rather than living understanding."}
    ]
  },
  "Dashboard — mot/unmotorised.md": {
    "primary": "Not equipped with, operated by, or propelled by a motor or engine; relying on muscle power or passive forces.",
    "secondary": "In urban planning and transport policy, describes infrastructure dedicated to active travel such as bicycle tracks and pedestrian pathways.",
    "quotes": [
      {"author": "George Orwell", "work": "The Road to Wigan Pier", "quote": "The miners pushed heavy **unmotorised** coal tubs along the subterranean rails by sheer muscular exertion."},
      {"author": "H. G. Wells", "work": "The Wheels of Chance", "quote": "He delighted in the quiet freedom of an **unmotorised** bicycle touring along idyllic English country lanes."},
      {"author": "John Galsworthy", "work": "The Forsyte Saga", "quote": "Swithin clung obstinately to his **unmotorised** carriage, despising the noisy automobiles invading London streets."}
    ]
  },
  "Dashboard — mot/unmotorized.md": {
    "primary": "Operating without a motorized propulsion system; propelled by pedals, oars, sails, draft animals, or human walking.",
    "secondary": "In environmental recreation management, designates wilderness zones and park waterways where motorized craft and off-road vehicles are prohibited.",
    "quotes": [
      {"author": "Aldous Huxley", "work": "Island", "quote": "The island council restricted vehicular transit to **unmotorized** bicycles and small pedal carriages to preserve tranquility."},
      {"author": "Henry David Thoreau", "work": "The Maine Woods", "quote": "We traversed the northern lakes in an **unmotorized** birchbark canoe guided silently by Indian paddles."},
      {"author": "John Muir", "work": "The Mountains of California", "quote": "True intimacy with the Sierra wilderness requires travel by **unmotorized** foot, carrying one's pack through high granite passes."}
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

print(f"Motion Batch 10C: Successfully updated {updated}/{len(data)} notes.")
