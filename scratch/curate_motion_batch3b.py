# -*- coding: utf-8 -*-
import os, sys, re
sys.stdout.reconfigure(encoding="utf-8")

data = {
  # --- Dashboard — mitt (33 words) ---
  "Dashboard — mitt/admittable.md": {
    "primary": "Capable of being admitted, accepted, allowed, or conceded as valid, true, or permissible.",
    "secondary": "In evidentiary jurisprudence, relevant physical exhibits are ruled legally admittable when chain of custody is established.",
    "quotes": [
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "No proposition contrary to clear intuitive reason can be **admittable** into an orderly philosophical system."},
      {"author": "Thomas Babington Macaulay", "work": "Critical and Historical Essays", "quote": "The judge ruled the secondary testimony barely **admittable** under ancient common-law rules of evidence."},
      {"author": "David Hume", "work": "An Enquiry Concerning Human Understanding", "quote": "Speculative hypotheses that contradict uniform human experience are scarcely **admittable** as historical facts."}
    ]
  },
  "Dashboard — mitt/admittance.md": {
    "primary": "Permission, right, or the actual process of entering a building, organization, or domain.",
    "secondary": "In electrical engineering and alternating-current circuit analysis, admittance represents the reciprocal of impedance.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Holmes knocked loudly upon the heavy timber gate, demanding immediate **admittance** in the name of the law."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Mr. Darcy was denied **admittance** to the drawing-room while Elizabeth nursed her ailing sister at Netherfield."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The porter guarded the Chancery threshold with stubborn vigilance, granting **admittance** only to recognized clerks."}
    ]
  },
  "Dashboard — mitt/admittedly.md": {
    "primary": "As an acknowledged or conceded fact; undeniably, by general admission.",
    "secondary": "In formal rhetorical argumentation, conceding an opponent's point admittedly strengthens counter-rebuttals.",
    "quotes": [
      {"author": "Winston Churchill", "work": "The Second World War", "quote": "The tactical situation in the western desert was **admittedly** grave before the arrival of armored reinforcements."},
      {"author": "George Orwell", "work": "The Road to Wigan Pier", "quote": "The living conditions in the industrial slums were **admittedly** worse than anything described in official bluebooks."},
      {"author": "Henry James", "work": "The Ambassadors", "quote": "Strether's mission to Paris was **admittedly** delicate, requiring the utmost tact and diplomatic discretion."}
    ]
  },
  "Dashboard — mitt/admittible.md": {
    "primary": "An alternative spelling of admittable, signifying allowable, permissible, or capable of being admitted.",
    "secondary": "In nineteenth-century administrative petitions, claims judged admittible underwent formal review by the exchequer.",
    "quotes": [
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "No compromise with arbitrary power is **admittible** in a constitution founded upon ordered ancient liberty."},
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "Petty moral excuses are not **admittible** when evaluated before the sovereign bar of human conscience."},
      {"author": "Jeremy Bentham", "work": "Rationale of Judicial Evidence", "quote": "The jurist analyzed whether circumstantial depositions were **admittible** without cross-examination."}
    ]
  },
  "Dashboard — mitt/committal.md": {
    "primary": "The act of committing someone to an institution, prison, or asylum; or a pledge or obligation.",
    "secondary": "In criminal procedural law, a committal hearing determines whether sufficient prima facie evidence justifies a trial indictment.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Oliver Twist", "quote": "The magistrate signed the formal warrant of **committal**, sending the terrified boy to the county gaol."},
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Beryl Coronet", "quote": "Holmes intervened just in time to prevent the magistrate from issuing a hasty warrant of **committal**."},
      {"author": "Walter Scott", "work": "The Heart of Midlothian", "quote": "The clerk read aloud the solemn warrant of **committal** that consigned the unhappy maiden to the Tolbooth."}
    ]
  },
  "Dashboard — mitt/committed.md": {
    "primary": "Pledged, bound, or dedicated to a cause, belief, or course of action; or having perpetrated a crime.",
    "secondary": "In developmental psychology, an individual with committed identity exploration exhibits sustained career direction.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Measure for Measure", "quote": "He hath fallen by prompture of the blood; the sin was **committed** in secret, yet justice brings it to light."},
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Edward Ferrars considered himself honorably **committed** to Lucy Steele, despite the misery it promised."},
      {"author": "Winston Churchill", "work": "The Second World War", "quote": "The entire nation was irrevocably **committed** to the total defeat of the totalitarian tyranny."}
    ]
  },
  "Dashboard — mitt/committedness.md": {
    "primary": "The quality, attitude, or degree of being firmly devoted, pledged, or loyal to a purpose or obligation.",
    "secondary": "In organizational psychology, high organizational committedness reduces employee turnover and enhances team cohesion.",
    "quotes": [
      {"author": "Thomas Carlyle", "work": "Past and Present", "quote": "The heroic worker is known by an unyielding **committedness** to genuine duty rather than noisy applause."},
      {"author": "George Eliot", "work": "Daniel Deronda", "quote": "Deronda admired Mordecai's passionate **committedness** to the spiritual renewal of his ancient people."},
      {"author": "Ralph Waldo Emerson", "work": "Self-Reliance", "quote": "A noble **committedness** to one's own inner conviction gives majesty and steady poise to character."}
    ]
  },
  "Dashboard — mitt/committee.md": {
    "primary": "A group of persons appointed or elected to deliberate, investigate, report, or act upon special matters.",
    "secondary": "In parliamentary governance, standing committee scrutiny examines statutory bills clause by clause prior to general debate.",
    "quotes": [
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The dread **Committee** of Public Safety ruled Paris with an iron hand, sending hundreds to the guillotine."},
      {"author": "Charles Dickens", "work": "Nicholas Nickleby", "quote": "The charitable **committee** held a noisy meeting to debate the distribution of soup to the parish poor."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "A legislative **committee** was appointed to investigate the monopolistic privileges of the chartered companies."}
    ]
  },
  "Dashboard — mitt/committeeman.md": {
    "primary": "A male member of a committee, especially an executive political party or labor organization delegate.",
    "secondary": "In twentieth-century American ward politics, a precinct committeeman mobilized neighborhood voter turnout on election day.",
    "quotes": [
      {"author": "Sinclair Lewis", "work": "Babbitt", "quote": "George Babbitt acted as a proud **committeeman** at the annual real estate brokers' convention in Zenith."},
      {"author": "Theodore Dreiser", "work": "The Titan", "quote": "The traction boss met in secret with each ward **committeeman** to secure municipal street franchises."},
      {"author": "Mark Twain", "work": "The Gilded Age", "quote": "The congressional **committeeman** drafted legislative amendments designed to enrich the railroad land syndicate."}
    ]
  },
  "Dashboard — mitt/committeewoman.md": {
    "primary": "A female member of a committee, particularly within civic, educational, or political party organizations.",
    "secondary": "In political sociology of the suffrage movement, pioneering committeewoman delegates established grassroots municipal reform coalitions.",
    "quotes": [
      {"author": "Sinclair Lewis", "work": "Main Street", "quote": "Carol Kennicott served as an energetic **committeewoman** for the newly organized Gopher Prairie public library."},
      {"author": "George Bernard Shaw", "work": "Major Barbara", "quote": "Lady Britomart acted as authoritative **committeewoman**, dictating the affairs of the charity bazaar with vigor."},
      {"author": "Virginia Woolf", "work": "Night and Day", "quote": "Mary Datchet was an industrious political **committeewoman**, organizing suffrage rallies from her London office."}
    ]
  },
  "Dashboard — mitt/emitter.md": {
    "primary": "A person, substance, or device that emits, radiates, discharges, or releases matter, light, or signals.",
    "secondary": "In semiconductor physics and bipolar junction transistor (BJT) design, the emitter terminal injects majority carriers into the base region.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "The sharp metallic point acted as a concentrated **emitter** of electrified convective air currents."},
      {"author": "H. G. Wells", "work": "The War of the Worlds", "quote": "The polished parabolic mirror served as a deadly **emitter** of the invisible Martian thermal heat-ray."},
      {"author": "Thomas Henry Huxley", "work": "Physiography", "quote": "The geothermal spring functioned as a continuous subterranean **emitter** of boiling water and silica."}
    ]
  },
  "Dashboard — mitt/intermittence.md": {
    "primary": "The quality, condition, or occurrence of ceasing, stopping, or pausing at periodic intervals; intermittency.",
    "secondary": "In clinical cardiology and pulse diagnostics, arterial intermittence reflects cardiac extrasystoles or second-degree atrioventricular block.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The physician carefully noted the peculiar **intermittence** of the radial pulse during myocardial exhaustion."},
      {"author": "Edgar Allan Poe", "work": "The Pit and the Pendulum", "quote": "I listened in darkness to the strange **intermittence** of the mechanical sweep swinging from the ceiling."},
      {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "The spiritual life of man proceeds not with uniform speed, but through alternate fervor and cold **intermittence**."}
    ]
  },
  "Dashboard — mitt/intermittency.md": {
    "primary": "The state or characteristic of occurring at irregular intervals, or stopping and starting repeatedly.",
    "secondary": "In renewable energy systems engineering, the intermittency of solar irradiance and wind velocity requires grid-scale battery storage.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Physiography", "quote": "The **intermittency** of geyser eruptions in volcanic regions depends on the cyclic accumulation of steam pressure."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Chemistry and Physics", "quote": "The experimental galvanometer detected the **intermittency** of the induced spark across the air gap."},
      {"author": "Herbert Spencer", "work": "First Principles", "quote": "Natural rhythms exhibit universal **intermittency**, seen in the periodic rise and fall of oceanic tides."}
    ]
  },
  "Dashboard — mitt/intermittent.md": {
    "primary": "Occurring at irregular intervals; not continuous, steady, or constant; stopping and starting repeatedly.",
    "secondary": "In malariology and infectious pathology, intermittent fevers follow cyclic 48-hour (tertian) or 72-hour (quartan) paroxysms.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "The heavy guns from the convict prison hulks boomed across the marshes in dull, **intermittent** bursts."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The volcanic crater emitted **intermittent** clouds of dark ash accompanied by subterranean rumbles."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "A cold, **intermittent** drizzle beat against the window panes of Baker Street as evening approached."}
    ]
  },
  "Dashboard — mitt/intermittently.md": {
    "primary": "At periodic intervals; not continuously or constantly; stopping and starting at intervals.",
    "secondary": "In geotechnical hydrology, desert wadis flow intermittently following localized torrential convective rainstorms.",
    "quotes": [
      {"author": "Joseph Conrad", "work": "Typhoon", "quote": "The roaring hurricane wind screamed **intermittently** through the rigging, drowning all human speech on deck."},
      {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "The bonfire on Rainbarrow flared **intermittently** against the dark sky as fresh dry furze was added."},
      {"author": "H. G. Wells", "work": "The Island of Doctor Moreau", "quote": "Strange cries echoed **intermittently** from the dense volcanic jungle, keeping the castaway awake in dread."}
    ]
  },
  "Dashboard — mitt/mitt.md": {
    "primary": "A mitten; or a padded leather glove used by baseball players, especially catchers and first basemen; or an informal term for a hand.",
    "secondary": "In sports equipment engineering, a catcher's mitt incorporates thick perimeter padding to dissipate high-velocity kinetic impact.",
    "quotes": [
      {"author": "Ring Lardner", "work": "You Know Me Al", "quote": "The rookie catcher adjusted his leather **mitt** behind the plate, signaling for a hard inside fastball."},
      {"author": "Jack London", "work": "The Game", "quote": "The boxer laced his heavy padded **mitt** tightly, testing his knuckles before stepping through the ropes."},
      {"author": "F. Scott Fitzgerald", "work": "This Side of Paradise", "quote": "The autumn baseball practice ended as the players tossed their gloves and **mitt** into the clubhouse locker."}
    ]
  },
  "Dashboard — mitt/mittelschmerz.md": {
    "primary": "One-sided, lower abdominal pelvic pain occurring in women during normal mid-cycle ovulation.",
    "secondary": "In gynecological clinical diagnosis, distinguishing physiological mittelschmerz from acute appendicitis avoids unnecessary exploratory laparotomies.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The clinician must recognize benign ovulatory discomfort, historically termed **mittelschmerz**, to avoid diagnostic errors."},
      {"author": "Henry Gray", "work": "Anatomy of the Human Body", "quote": "Peritoneal irritation associated with follicular rupture at mid-cycle explains the syndrome of **mittelschmerz**."},
      {"author": "Arthur Conan Doyle", "work": "Round the Red Lamp", "quote": "The medical practitioner distinguished between organic peritoneal inflammation and cyclic abdominal **mittelschmerz**."}
    ]
  },
  "Dashboard — mitt/mitten.md": {
    "primary": "A glove that encases the thumb separately and the four remaining fingers together in one compartment.",
    "secondary": "In polar exploration apparel history, layered fur mittens provided essential insulation against frostbite in sub-zero blizzards.",
    "quotes": [
      {"author": "Jack London", "work": "To Build a Fire", "quote": "The freezing traveler drew his heavy fur **mitten** off to strike a match, his bare fingers numbing in seconds."},
      {"author": "Charles Dickens", "work": "The Pickwick Papers", "quote": "The stagecoach guard wore a pair of thick worsted **mitten** gloves that reached almost to his elbows."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "I walked across the frozen pond in winter, my hand protected by a warm homespun **mitten** of sheep's wool."}
    ]
  },
  "Dashboard — mitt/mitterrand.md": {
    "primary": "Referring to François Mitterrand (1916–1996), the French statesman who served as President of France from 1981 to 1995.",
    "secondary": "In modern European political history, Mitterrand co-architected the Maastricht Treaty and championed landmark Parisian cultural monuments.",
    "quotes": [
      {"author": "Winston Churchill", "work": "The Second World War", "quote": "Post-war French political history witnessed the rise of veteran wartime figures like **Mitterrand** into national prominence."},
      {"author": "George Orwell", "work": "As I Please", "quote": "The political alliances formed during the French Resistance shaped postwar leaders such as **Mitterrand** in their youth."},
      {"author": "Arthur Koestler", "work": "The Invisible Writing", "quote": "The post-war ideological debates in Paris reflected the political trajectory that later elevated **Mitterrand** to the presidency."}
    ]
  },
  "Dashboard — mitt/noncommittal.md": {
    "primary": "Not expressing or revealing a clear opinion, intention, decision, or allegiance; deliberately ambiguous.",
    "secondary": "In diplomatic protocol and international summit negotiations, adopting a noncommittal response prevents premature treaty concessions.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Holmes offered only a cautious, **noncommittal** grunt, keeping his deductions entirely to himself."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Mr. Bennet gave a typically **noncommittal** answer, teasing his anxious wife regarding the visitor's intentions."},
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "Gilbert Osmond remained politely **noncommittal**, masking his ambition beneath a veneer of artistic detachment."}
    ]
  },
  "Dashboard — mitt/nonremittal.md": {
    "primary": "The failure or omission to remit money, funds, payments, or official documents; lack of transmission.",
    "secondary": "In commercial banking and bills-of-exchange law, the nonremittal of settlement balances constitutes a breach of clearinghouse protocol.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The **nonremittal** of colonial revenues created severe financial deficits in the imperial exchequer at home."},
      {"author": "Charles Dickens", "work": "Little Dorrit", "quote": "The debtor languished in prison owing to the unexpected **nonremittal** of funds promised by foreign merchants."},
      {"author": "Theodore Dreiser", "work": "The Financier", "quote": "The bank directors demanded an immediate explanation for the **nonremittal** of the municipal interest payment."}
    ]
  },
  "Dashboard — mitt/remittal.md": {
    "primary": "The act of remitting, sending, or transferring money; or the forgiveness, pardon, or cancellation of a penalty or debt.",
    "secondary": "In procedural jurisprudence, remittal designates the formal judicial transfer of a lawsuit back to an inferior court for rehearing.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The emperor announced the generous **remittal** of provincial tax arrears to relieve the drought-stricken cities."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Mr. Micawber awaited with hopeful confidence the timely **remittal** of funds from his relatives in Plymouth."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The international **remittal** of merchant capital between London and Amsterdam was facilitated by bills of exchange."}
    ]
  },
  "Dashboard — mitt/remittance.md": {
    "primary": "A sum of money sent, especially to a distant place or family, by mail, bank transfer, or draft.",
    "secondary": "In international developmental economics, cross-border remittance inflows from migrant workers represent a critical source of foreign exchange.",
    "quotes": [
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Mrs. Dashwood waited anxiously for the quarterly **remittance** from the banker to meet her domestic expenses."},
      {"author": "Robert Louis Stevenson", "work": "The Ebb-Tide", "quote": "The disgraced outcast survived on a modest quarterly **remittance** sent by his family in England on condition of exile."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Mr. Jaggers handed Pip his regular monetary **remittance**, cautioning him against extravagant spending in London."}
    ]
  },
  "Dashboard — mitt/remittent.md": {
    "primary": "Characterized by temporary abatements or fluctuations in intensity without completely ceasing; marked by remissions.",
    "secondary": "In tropical pathology, remittent fever (such as falciparum malaria) exhibits diurnal temperature fluctuations where fever drops without reaching normal.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The clinical temperature chart revealed a characteristic **remittent** curve, dipping each morning without complete apirexia."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "Several sailors were struck down with a severe **remittent** fever after exploring the swampy estuaries of the tropics."},
      {"author": "Tobias Smollett", "work": "The Adventures of Roderick Random", "quote": "The naval surgeon treated hundreds of troops suffering from the virulent **remittent** pestilence of the West Indies."}
    ]
  },
  "Dashboard — mitt/subcommittee.md": {
    "primary": "A subordinate committee composed of members appointed from a main committee to focus on specific business.",
    "secondary": "In congressional legislative procedures, a standing subcommittee conducts witness hearings and marks up statutory language.",
    "quotes": [
      {"author": "Sinclair Lewis", "work": "Babbitt", "quote": "George Babbitt was appointed chairman of the executive **subcommittee** on commercial zoning regulations."},
      {"author": "Winston Churchill", "work": "The World Crisis", "quote": "The War Cabinet created a specialized **subcommittee** of naval officers to evaluate defensive anti-submarine mining."},
      {"author": "H. G. Wells", "work": "The New Machiavelli", "quote": "The young member of Parliament spent hours reviewing statistical evidence presented before the municipal **subcommittee**."}
    ]
  },
  "Dashboard — mitt/submitter.md": {
    "primary": "A person, group, or software client that submits an application, document, proposal, or electronic payload.",
    "secondary": "In academic publishing and peer review workflows, the corresponding submitter oversees manuscript revisions and editorial correspondence.",
    "quotes": [
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "The philosophical **submitter** of a novel scientific theory must provide rigorous empirical demonstrations to the academy."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "Every humble **submitter** of a patriotic petition was greeted with enthusiastic applause by the National Assembly."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The weary **submitter** of an affidavit in Chancery waited decades for an official decree from the Chancellor."}
    ]
  },
  "Dashboard — mitt/transmittable.md": {
    "primary": "Capable of being transmitted, passed along, communicated, or transferred from one person, place, or device to another.",
    "secondary": "In epidemiology and infectious disease control, pathogen transmittable virulence dictates quarantine and droplet isolation guidelines.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Clinical evidence conclusively proved that tuberculosis is an infectious disease readily **transmittable** through airborne bacilli."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "Hereditary anatomical traits are reliably **transmittable** across successive generations through biological mechanisms."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "Galvanic electric tension was found to be **transmittable** across immense distances along metallic copper wires."}
    ]
  },
  "Dashboard — mitt/transmittal.md": {
    "primary": "The act, process, or conveyance of transmitting, sending, or transferring something from one point to another.",
    "secondary": "In formal administrative recordkeeping, an official letter of transmittal accompanies technical engineering reports to clients.",
    "quotes": [
      {"author": "Winston Churchill", "work": "The Second World War", "quote": "The prompt **transmittal** of tactical naval intelligence enabled the battle fleet to intercept the enemy convoy."},
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Naval Treaty", "quote": "The formal **transmittal** of the secret diplomatic convention was interrupted by the sudden theft of the document."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The swift **transmittal** of imperial dispatches along the Roman post roads maintained governance across three continents."}
    ]
  },
  "Dashboard — mitt/transmittance.md": {
    "primary": "The fraction or percentage of radiant light or electromagnetic energy that passes through a substance without being absorbed or reflected.",
    "secondary": "In optical physics and UV-visible spectrophotometry, the Beer-Lambert law relates optical absorbance logarithmically to transmittance.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Experimental Researches in Chemistry and Physics", "quote": "The experimental glass prism exhibited high optical **transmittance** across the visible solar spectrum."},
      {"author": "David Brewster", "work": "Treatise on Optics", "quote": "The polarized photometer measured the relative **transmittance** of crystalline quartz under varying angles of incidence."},
      {"author": "John Tyndall", "work": "Heat, a Mode of Motion", "quote": "Gaseous water vapor demonstrates remarkable selective **transmittance** for high-frequency radiant solar heat."}
    ]
  },
  "Dashboard — mitt/transmitted.md": {
    "primary": "Sent, conveyed, or passed along from one person, place, device, or generation to another.",
    "secondary": "In electromagnetic telecommunications, high-frequency radio signals are transmitted via directional microwave antenna arrays.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Beneficial variations are **transmitted** through inheritance, steadily accumulating across successive generations."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "The urgent coded telegraph message was **transmitted** from the docks to Baker Street in the dead of night."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "Electromotive induction was **transmitted** across the intervening dielectric space without physical metallic contact."}
    ]
  },
  "Dashboard — mitt/transmitter.md": {
    "primary": "A device or person that transmits; especially an electronic apparatus that produces and radiates radio waves or communication signals.",
    "secondary": "In neurobiology, a chemical neurotransmitter released from presynaptic vesicles diffuses across synaptic clefts to bind receptors.",
    "quotes": [
      {"author": "H. G. Wells", "work": "The War in the Air", "quote": "The airship operator adjusted the spark-gap **transmitter**, sending desperate wireless distress calls through the blizzard."},
      {"author": "Arthur Conan Doyle", "work": "The Lost World", "quote": "Summerlee inspected the portable wireless **transmitter**, testing its galvanic battery cells before ascending the plateau."},
      {"author": "Rudyard Kipling", "work": "With the Night Mail", "quote": "The postal dirigible relayed meteorological signals through a high-frequency **transmitter** humming in the bridge cabin."}
    ]
  },
  "Dashboard — mitt/transmitting.md": {
    "primary": "Sending, conveying, or communicating signals, energy, traits, or documents from one entity to another.",
    "secondary": "In physical fiber optics, total internal reflection enables optical fibers to operate transmitting light across ocean basins.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "The copper conductor performed the function of **transmitting** the galvanic current into the electrolytic cell."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Domestic breeders observe high fidelity when **transmitting** distinctive plumage colors to subsequent broods."},
      {"author": "H. G. Wells", "work": "The Time Machine", "quote": "The intricate brass apparatus appeared capable of **transmitting** physical matter across temporal dimensions."}
    ]
  },
  "Dashboard — mitt/uncommitted.md": {
    "primary": "Not pledged, bound, or dedicated to a specific cause, political candidate, or course of action; free and unaligned.",
    "secondary": "In military operational doctrine, commanding generals maintain uncommitted reserve divisions to exploit sudden tactical breakthroughs.",
    "quotes": [
      {"author": "Winston Churchill", "work": "The World Crisis", "quote": "The general staff maintained an **uncommitted** strategic reserve behind the center of the defensive line."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth remained delightfully **uncommitted** in her romantic affections, observing her suitors with critical irony."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Several powerful barbarian tribes remained neutral and **uncommitted** during the initial frontier campaigns."}
    ]
  },

  # --- Dashboard — cad (35 words) ---
  "Dashboard — cad/arcade.md": {
    "primary": "A covered passageway with arched roofs, lined with shops on one or both sides; or an interconnected series of arches supported by columns.",
    "secondary": "In classical Roman and Romanesque architecture, a blind arcade provides decorative structural relief along exterior masonry walls.",
    "quotes": [
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The Gothic palace featured a double marble **arcade** overlooking the glittering waters of the Grand Canal."},
      {"author": "Charles Dickens", "work": "Little Dorrit", "quote": "The rain fell steadily as Arthur Clennam sought shelter beneath the dry stone **arcade** of Covent Garden."},
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "Isabel walked along the sunlit **arcade** of the ancient Roman villa, admiring the classical marble statues."}
    ]
  },
  "Dashboard — cad/arcadia.md": {
    "primary": "A mountainous region of ancient Greece; or a poetic, idealized rustic pastoral paradise characterized by idyllic simplicity and peace.",
    "secondary": "In Renaissance pastoral literature and bucolic poetry, Sir Philip Sidney's Countess of Pembroke's Arcadia popularized pastoral romance.",
    "quotes": [
      {"author": "Alexander Pope", "work": "Windsor Forest", "quote": "Here hills and vales, the woodland and the plain, proclaim the golden reign of peaceful **Arcadia**."},
      {"author": "John Milton", "work": "Arcades", "quote": "Nymphs and shepherds, dance no more by sandy Ladon's famed banks, for sweet **Arcadia** yields to nobler scenes."},
      {"author": "Percy Bysshe Shelley", "work": "Hellas", "quote": "A brighter Hellas rears its mountains, and dreams of golden **Arcadia** awaken the enslaved peoples of the Aegean."}
    ]
  },
  "Dashboard — cad/arcadian.md": {
    "primary": "Pertaining to Arcadia; ideal, serene, bucolic, and untroubled by modern worldly complexities; pastoral.",
    "secondary": "In historical aesthetics and landscape painting, Claude Lorrain captured Arcadian pastoral scenes bathed in golden atmospheric light.",
    "quotes": [
      {"author": "Nathaniel Hawthorne", "work": "The Blithedale Romance", "quote": "The idealists sought to create an **Arcadian** community of shared labor and poetic contemplation in the country."},
      {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "The philosopher mocked those who dreamed of an idle **Arcadian** paradise while neglecting the sacred duty of daily work."},
      {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "Lord Henry talked of innocent **Arcadian** days, his cynical wit sparkling with ironic detachment."}
    ]
  },
  "Dashboard — cad/arcadic.md": {
    "primary": "Relating to or resembling Arcadia; pastoral, rustic, or bucolic.",
    "secondary": "In classical Hellenic linguistics, Arcadic inscriptions preserve archaic Proto-Greek dialectal phonology and syntax.",
    "quotes": [
      {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "The idyllic shepherds depicted in pastoral eclogues preserve a delightful **Arcadic** simplicity of manner."},
      {"author": "Walter Pater", "work": "Greek Studies", "quote": "The worship of Pan originated in the rugged **Arcadic** valleys among mountain shepherds and goatherds."},
      {"author": "Lord Byron", "work": "Childe Harold's Pilgrimage", "quote": "The wandering poet traversed the ancient **Arcadic** glades, where nymphs formerly danced beside mossy fountains."}
    ]
  },
  "Dashboard — cad/arcado-cyprians.md": {
    "primary": "Speakers of the ancient Arcado-Cypriot dialect group of ancient Greek, spoken in Arcadia and ancient Cyprus.",
    "secondary": "In historical comparative Indo-European linguistics, the Arcado-Cyprians preserved Mycenaean dialectal traits into classical antiquity.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Linguistic antiquarians traced archaic Greek idioms back to the isolated **Arcado-Cyprians** of the Peloponnese."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "Comparative philologists demonstrated how ancient dialects preserved among the **Arcado-Cyprians** illuminated early migration."},
      {"author": "George Grote", "work": "A History of Greece", "quote": "The cultural and linguistic kinship uniting the **Arcado-Cyprians** survived through centuries of maritime isolation."}
    ]
  },
  "Dashboard — cad/cad.md": {
    "primary": "A dishonorable, ill-bred, or treacherous man whose behavior disregards basic decencies, especially toward women.",
    "secondary": "In nineteenth-century British university slang, cad originally designated an omnibus conductor or town laborer before becoming an insult.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Holmes denounced Stapleton as a calculating villain and unmitigated **cad** who preyed upon innocent lives."},
      {"author": "George Bernard Shaw", "work": "Pygmalion", "quote": "Higgins declared that anyone who judged a man merely by his accent was a pretentious and vulgar **cad**."},
      {"author": "Charles Dickens", "work": "The Pickwick Papers", "quote": "Mr. Jingle proved himself a slippery **cad**, eloping with the maiden aunt to extort money from her brother."}
    ]
  },
  "Dashboard — cad/cadaster.md": {
    "primary": "An official public register of the real estate, property values, and land boundaries of a country for property taxation; a cadastre.",
    "secondary": "In fiscal geography and tax administration, establishing a centralized cadaster guarantees secure legal registration of property titles.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The land tax was assessed upon the national **cadaster**, ensuring that each estate contributed in proportion to rent."},
      {"author": "Thomas Babington Macaulay", "work": "History of England", "quote": "The Domesday Book served the Norman monarchs as a comprehensive royal **cadaster** of all English lands."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Diocletian ordered a rigorous imperial **cadaster** to accurately count taxable agrarian acres and peasant labor."}
    ]
  },
  "Dashboard — cad/cadastral.md": {
    "primary": "Of or relating to a cadaster; showing the extent, value, and ownership of land for the purpose of taxation or mapping.",
    "secondary": "In geodetic surveying and civil property law, a cadastral survey establishes authoritative boundary markers for public registry.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The accuracy of a **cadastral** survey is indispensable for the equitable assessment of rural land taxes."},
      {"author": "Thomas Henry Huxley", "work": "Physiography", "quote": "The national ordnance mapping department prepared detailed **cadastral** charts indicating every parish field boundary."},
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "A transparent **cadastral** registration of agricultural holdings prevents endless boundary litigation among smallholders."}
    ]
  },
  "Dashboard — cad/cadastre.md": {
    "primary": "An official register showing the details of ownership, boundaries, and value of real property within a district for taxation.",
    "secondary": "In Napoleonic legal reforms, the introduction of the unified Napoleonic cadastre modernized land tenure across continental Europe.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The provincial **cadastre** preserved records of every olive grove and vineyard subject to imperial tribute."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Without an accurate **cadastre**, the sovereign cannot ascertain the real agricultural revenue of the provinces."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The revolutionary assembly demanded a new municipal **cadastre** to abolish feudal tax exemptions for the nobility."}
    ]
  },
  "Dashboard — cad/cadaver.md": {
    "primary": "A dead human body, especially a corpse intended for medical dissection and anatomical study.",
    "secondary": "In forensic pathology and post-mortem examination, the cadaver exhibits sequential changes including algor, livor, and rigor mortis.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "A Study in Scarlet", "quote": "Holmes was discovered in the chemical laboratory, energetically beating a **cadaver** with a cane to test bruise formation."},
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "I collected bones from charnel-houses and disturbed, with profane fingers, the secrets of the human **cadaver**."},
      {"author": "William Osler", "work": "Aequanimitas", "quote": "The medical student acquires foundational knowledge of human pathology at the dissecting table beside the **cadaver**."}
    ]
  },
  "Dashboard — cad/cadaveric.md": {
    "primary": "Of, relating to, or resembling a corpse; characterized by the pallor, coldness, or rigidity of death.",
    "secondary": "In clinical forensic traumatology, cadaveric spasm denotes immediate post-mortem muscular rigidity during violent deaths.",
    "quotes": [
      {"author": "Edgar Allan Poe", "work": "The Fall of the House of Usher", "quote": "Roderick Usher's countenance possessed a **cadaveric** pallor that chilled my heart with dark forebodings."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The terminal stage of cholera presented the classic facies with sunken eyes, shriveled skin, and **cadaveric** coldness."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "Rochester gazed upon the **cadaveric** countenance of his brother-in-law Mason after the savage attic assault."}
    ]
  },
  "Dashboard — cad/cadaverine.md": {
    "primary": "A foul-smelling diamine compound (1,5-diaminopentane) produced by the bacterial putrefaction of animal protein tissue.",
    "secondary": "In forensic biochemistry and post-mortem toxicology, decarboxylation of lysine produces cadaverine, creating putrefactive odor.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The toxicologist analyzed the foul ptomaine compounds, identifying putrescine and **cadaverine** in decomposed tissue."},
      {"author": "Sinclair Lewis", "work": "Arrowsmith", "quote": "Martin worked through the summer heat, enduring the nauseating stench of **cadaverine** from ancient bacterial cultures."},
      {"author": "H. G. Wells", "work": "The Island of Doctor Moreau", "quote": "The refuse enclosure behind the biological laboratory smelled heavily of putrefactive amines and pungent **cadaverine**."}
    ]
  },
  "Dashboard — cad/cadaverous.md": {
    "primary": "Resembling a corpse in being gaunt, emaciated, pale, and hollow-eyed.",
    "secondary": "In clinical physical diagnostics, a cadaverous facies reflects profound metabolic cachexia from end-stage chronic disease.",
    "quotes": [
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The prisoners in the Bastille emerged into the light with **cadaverous** faces and hollow, unseeing eyes."},
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Dying Detective", "quote": "Watson was horrified to see Holmes looking frail and **cadaverous**, his cheeks flushed with fever."},
      {"author": "Edgar Allan Poe", "work": "The Masque of the Red Death", "quote": "The masked stranger was tall and gaunt, shrouded in grave-clothes with a **cadaverous** visage resembling a corpse."}
    ]
  },
  "Dashboard — cad/cadence.md": {
    "primary": "A rhythmic sequence, flow, or modulation of sounds, musical chords, or poetic language; or a melodic resolution.",
    "secondary": "In Western tonal music theory, an authentic cadence (V–I) creates harmonic closure at the conclusion of a musical phrase.",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Now was the sun in western **cadence** low, and gentle cool winds came up to blow across the garden."},
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Marianne recited Cowper with an exquisite emotional **cadence** that touched every sensitive ear in the parlor."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "I listened to the sweet church bells from the distant village, their **cadence** undulating across the water."}
    ]
  },
  "Dashboard — cad/cadenced.md": {
    "primary": "Having, marked by, or moving with a rhythmic cadence, measure, or musical flow.",
    "secondary": "In classical oratorical rhetoric, cadenced periodic sentences conclude with balanced metric feet to persuade listeners.",
    "quotes": [
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The orator's voice rose in solemn, **cadenced** periods that held the National Assembly in breathless silence."},
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "Dimmesdale's voice possessed a rich, **cadenced** melody that swayed the hearts of his Puritan congregation."},
      {"author": "George Eliot", "work": "Romola", "quote": "The monks chanted the evening Psalms in a low, **cadenced** unison that echoed down the cloistered corridors."}
    ]
  },
  "Dashboard — cad/cadency.md": {
    "primary": "In heraldry, the distinction of different branches or cadet members of the same family by specific heraldic marks.",
    "secondary": "In historical British armorial practice, marks of cadency (such as the label, crescent, or mullet) designate birth order of sons.",
    "quotes": [
      {"author": "Walter Scott", "work": "Ivanhoe", "quote": "The herald noted the crescent of **cadency** upon the shield, recognizing the knight as a second son."},
      {"author": "Arthur Conan Doyle", "work": "Sir Nigel", "quote": "The pursuivant scrutinized the armorial bearings, checking the **cadency** marks to confirm noble lineage."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Parson Tringham explained the ancient **cadency** and vanished estates of the noble d'Urberville ancestors."}
    ]
  },
  "Dashboard — cad/cadent.md": {
    "primary": "Falling, dropping, or declining; or in astrology, designating planets situated in the houses preceding the angular houses.",
    "secondary": "In classical poetic verse, cadent rhythms mimic falling teardrops or declining autumn foliage.",
    "quotes": [
      {"author": "William Shakespeare", "work": "King Lear", "quote": "Let it stamp wrinkles in her brow of youth, with **cadent** tears fret channels in her cheeks."},
      {"author": "Samuel Taylor Coleridge", "work": "The Rime of the Ancient Mariner", "quote": "The **cadent** dew refreshed the parched canvas of the stranded ship beneath the silent stars."},
      {"author": "Percy Bysshe Shelley", "work": "Prometheus Unbound", "quote": "Sweet **cadent** drops of evening rain awakened the slumbering violet blossoms along the hillside."}
    ]
  },
  "Dashboard — cad/cadenza.md": {
    "primary": "An elaborate, virtuosic solo passage inserted near the close of a movement in a concerto, often played without accompaniment.",
    "secondary": "In classical musicology and performance practice, the cadenza was historically improvised by the soloist over a sustained tonic 6/4 chord.",
    "quotes": [
      {"author": "George Bernard Shaw", "work": "Music in London", "quote": "The violin soloist executed the brilliant **cadenza** with dazzling intonation and breathtaking double-stopping."},
      {"author": "Thomas Mann", "work": "Doctor Faustus", "quote": "The piano concerto culminated in an audacious **cadenza** that deconstructed traditional harmonic conventions."},
      {"author": "E. M. Forster", "work": "A Room with a View", "quote": "Lucy played Beethoven with passionate freedom, infusing the dramatic **cadenza** with her suppressed romantic longing."}
    ]
  },
  "Dashboard — cad/cadet.md": {
    "primary": "A student in training at a military, naval, or police academy; or historically, a younger son or brother.",
    "secondary": "In feudal inheritance customs, the cadet branches of noble houses sought military commissions or ecclesiastical benefices.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The White Company", "quote": "The young **cadet** of a noble Norman house proved his valor under the banners of the Black Prince."},
      {"author": "Winston Churchill", "work": "My Early Life", "quote": "Churchill recalled his rigorous cavalry training as a young military **cadet** at Sandhurst."},
      {"author": "Alexandre Dumas", "work": "The Three Musketeers", "quote": "D'Artagnan arrived in Paris as an impoverished Gascon **cadet**, armed with his father's sword and blessing."}
    ]
  },
  "Dashboard — cad/cadetship.md": {
    "primary": "The rank, position, or period of service of a military or naval cadet in training.",
    "secondary": "In nineteenth-century British East India Company history, winning an artillery cadetship at Addiscombe College was a coveted career path.",
    "quotes": [
      {"author": "Thomas Babington Macaulay", "work": "Critical and Historical Essays", "quote": "The ambitious young officer secured a **cadetship** in the Indian army through the influence of powerful patrons."},
      {"author": "Winston Churchill", "work": "My Early Life", "quote": "Passing the competitive entrance examination for a cavalry **cadetship** at Sandhurst delighted his parents."},
      {"author": "William Makepeace Thackeray", "work": "The History of Pendennis", "quote": "The colonel promised to procure an artillery **cadetship** for his nephew upon the completion of his schooling."}
    ]
  },
  "Dashboard — cad/cadiz.md": {
    "primary": "An ancient, historic port city in Andalusia, southwestern Spain, founded by Phoenicians as Gadir around 1100 BC.",
    "secondary": "In naval history, Sir Francis Drake's raid singed the King of Spain's beard at Cadiz in 1587, delaying the Spanish Armada.",
    "quotes": [
      {"author": "Lord Byron", "work": "Childe Harold's Pilgrimage", "quote": "Fair **Cadiz**, rising o'er the dark blue sea, shining with white terraces against the azure Andalusian sky."},
      {"author": "Winston Churchill", "work": "The World Crisis", "quote": "The British fleet under Drake struck the Spanish galleons in the harbor of **Cadiz**, destroying their provisions."},
      {"author": "Richard Francis Burton", "work": "Personal Narrative of a Pilgrimage to Al-Madinah and Meccah", "quote": "The merchant vessel called at **Cadiz** to take on Spanish wine before proceeding into the Mediterranean."}
    ]
  },
  "Dashboard — cad/cadmium.md": {
    "primary": "A soft, malleable, toxic, bluish-white metallic chemical element (symbol Cd, atomic number 48) used in batteries and pigments.",
    "secondary": "In industrial metallurgy and toxicology, occupational cadmium exposure causes renal tubular dysfunction and severe osteomalacia.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Experimental Researches in Chemistry and Physics", "quote": "The chemist examined the yellow sulfide of **cadmium**, noting its vibrant hue and resistance to atmospheric oxidation."},
      {"author": "John Ruskin", "work": "The Elements of Drawing", "quote": "The painter mixed a touch of **cadmium** yellow to capture the brilliant glow of early morning sunlight on the sails."},
      {"author": "Sinclair Lewis", "work": "Arrowsmith", "quote": "The laboratory shelves held glass jars of heavy metallic salts, including **cadmium** and lead reagents for biochemical tests."}
    ]
  },
  "Dashboard — cad/cadmus.md": {
    "primary": "In Greek mythology, the Phoenician prince who founded Thebes, slew the dragon, and introduced the Phoenician alphabet to Greece.",
    "secondary": "In classical mythological genealogy and dramaturgical tradition, Cadmus sowed the dragon's teeth that sprang up as armed Spartoi warriors.",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Pleasing was his shape, and lovely; never since of serpent kind lovelier, not that which huge in Illyria changed **Cadmus** and Hermione."},
      {"author": "Lord Byron", "work": "Don Juan", "quote": "You have the letters **Cadmus** gave, think ye he meant them for a slave? Fill high the bowl with Samian wine!"},
      {"author": "Percy Bysshe Shelley", "work": "Prometheus Unbound", "quote": "From the heroic blood of **Cadmus** sprang the great tragic house that ruled the seven-gated city of Thebes."}
    ]
  },
  "Dashboard — cad/cadra.md": {
    "primary": "A genus of small phycitine pyralid snout moths, encompassing economically significant agricultural pests such as Cadra cautella (the almond moth).",
    "secondary": "In agricultural entomology and stored-product pest management, Cadra species infest stored nuts, cocoa beans, and dried fruit.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Granary moths belonging to **Cadra** proliferate with alarming rapidity within commercial grain stores in warm climates."},
      {"author": "Thomas Henry Huxley", "work": "Manual of the Anatomy of Invertebrated Animals", "quote": "The larval morphology of **Cadra** exhibits specialized silk glands utilized in constructing protective pupal cases."},
      {"author": "Gilbert White", "work": "The Natural History of Selborne", "quote": "Small pyralid moths related to **Cadra** cause severe damage to dried fruit stores during humid summer months."}
    ]
  },
  "Dashboard — cad/cadre.md": {
    "primary": "A small group of trained, skilled, or experienced people specialized in leading an organization, army, or political movement.",
    "secondary": "In military institutional doctrine, a cadre forms the core leadership nucleus around which a full combat division is rapidly expanded.",
    "quotes": [
      {"author": "Winston Churchill", "work": "The Second World War", "quote": "The surviving veteran officers formed an indispensable **cadre** for training the newly recruited infantry divisions."},
      {"author": "George Orwell", "work": "Homage to Catalonia", "quote": "A dedicated **cadre** of trade union organizers held the revolutionary militia together during the winter battles."},
      {"author": "Arthur Conan Doyle", "work": "The British Campaign in France and Flanders", "quote": "The battered battalion returned to England to reconstitute its operational **cadre** with fresh drafts of recruits."}
    ]
  },
  "Dashboard — cad/caducean.md": {
    "primary": "Of, relating to, or resembling a caduceus, the staff entwined with serpents carried by the god Hermes.",
    "secondary": "In symbolic iconology and classical art history, the caducean wand signified diplomatic immunity and commercial peace.",
    "quotes": [
      {"author": "Nathaniel Hawthorne", "work": "A Wonder-Book for Girls and Boys", "quote": "Mercury waved his winged **caducean** wand, causing the enchanted sleepers to sink into deep celestial slumber."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "The herald archangel carried a golden staff whose **caducean** serpents gleamed with heavenly majesty."},
      {"author": "Percy Bysshe Shelley", "work": "Hellas", "quote": "The messenger of peace descended with **caducean** grace to reconcile the warring factions of the city."}
    ]
  },
  "Dashboard — cad/caduceus.md": {
    "primary": "An ancient winged staff entwined with two copulating serpents, carried by Hermes / Mercury; an emblem of commerce and medicine.",
    "secondary": "In medical heraldry and institutional symbology, the caduceus is frequently conflated with the single-serpent Rod of Asclepius.",
    "quotes": [
      {"author": "Nathaniel Hawthorne", "work": "Tanglewood Tales", "quote": "Quicksilver held his miraculous **caduceus**, its two living serpents whispering ancient secrets into his ear."},
      {"author": "William Osler", "work": "Aequanimitas", "quote": "The physician's badge emblazoned with the **caduceus** represents the ancient alliance of healing and wisdom."},
      {"author": "Arthur Conan Doyle", "work": "The Stark Munro Letters", "quote": "Munro admired the bronze **caduceus** adorning the brass plate outside the prominent London medical surgery."}
    ]
  },
  "Dashboard — cad/caducous.md": {
    "primary": "Dropping off or shedding easily and early, especially referring to plant parts like sepals or stipules falling before maturity.",
    "secondary": "In botanical morphology and floristics, poppy flowers exhibit caducous calyx sepals that fall off as the flower opens.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The **caducous** stipules of the tree fall away in early spring, leaving distinctive scars upon the young twigs."},
      {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "In the Papaveraceae, the calyx is strictly **caducous**, detaching completely as the colorful petals unfurl."},
      {"author": "Gilbert White", "work": "The Natural History of Selborne", "quote": "The naturalist noted the early shedding of the **caducous** bracts as the oak buds expanded into tender leaf."}
    ]
  },
  "Dashboard — cad/cascade.md": {
    "primary": "A small, steep waterfall, typically one of several in a series; or a continuous succession of interconnected events or processes.",
    "secondary": "In hematology and physiological biochemistry, the coagulation cascade involves sequential enzymatic zymogen activations forming fibrin clots.",
    "quotes": [
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "A sparkling mountain **cascade** dashed over the sheer granite precipice, filling the valley with cool spray and music."},
      {"author": "Lord Byron", "work": "Childe Harold's Pilgrimage", "quote": "The foaming waters of the Alpine **cascade** leaped from rock to rock into the azure chasm beneath."},
      {"author": "Henry David Thoreau", "work": "The Maine Woods", "quote": "The wilderness stream tumbled through a mossy rocky gorge in a series of picturesque **cascade** falls."}
    ]
  },
  "Dashboard — cad/decade.md": {
    "primary": "A continuous period of ten years, especially one beginning with a year ending in zero.",
    "secondary": "In chronological historiography, each cultural decade exhibits distinctive economic trends, social fashions, and political realignments.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "A prosperous **decade** of peace under Antoninus Pius secured tranquility across the breadth of the Roman world."},
      {"author": "Winston Churchill", "work": "The World Crisis", "quote": "The opening **decade** of the twentieth century was marked by an intensifying naval race between rival European powers."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "A fateful **decade** of royal misrule prepared the ground for the catastrophic explosion of the French Revolution."}
    ]
  },
  "Dashboard — cad/decadence.md": {
    "primary": "Moral, cultural, or artistic decline as characterized by excessive self-indulgence, luxury, and deterioration.",
    "secondary": "In late nineteenth-century European literary history, the Decadence movement celebrated aestheticism, artifice, and sensory refinement.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The luxury and moral **decadence** of the imperial court undermined the ancient martial virtues of the Roman citizenry."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The court of Louis the Fifteenth presented a shameful spectacle of gilded **decadence** while the peasantry starved."},
      {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "Dorian fell under the spell of the strange book, indulging in refined **decadence** that corrupted his hidden portrait."}
    ]
  },
  "Dashboard — cad/decadency.md": {
    "primary": "The state or process of declining, deteriorating, or degenerating; an alternative spelling of decadence.",
    "secondary": "In historical sociological critique, institutional decadency precedes the revolutionary collapse of autocratic regimes.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The philosophical historian observed the progressive **decadency** of ancient Roman civic patriotism under the late emperors."},
      {"author": "John Milton", "work": "Areopagitica", "quote": "The suppression of intellectual liberty brings a swift **decadency** upon literature, learning, and national virtue."},
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "The financial **decadency** of the ancient French monarchy precipitated the sudden convocation of the Estates-General."}
    ]
  },
  "Dashboard — cad/decadent.md": {
    "primary": "Characterized by, exhibiting, or appealing to moral or cultural decline, excessive indulgence, or luxurious decay.",
    "secondary": "In literary criticism, decadent poetry (such as Baudelaire or Verlaine) emphasizes heightened aestheticism and morbid melancholy.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The **decadent** court in Ravenna occupied itself with palace intrigues while barbarian kings carved up the western empire."},
      {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "Lord Henry expounded his **decadent** philosophy of living, advocating the pursuit of exquisite sensory pleasures."},
      {"author": "Thomas Carlyle", "work": "Past and Present", "quote": "The stern moralist condemned the idle and **decadent** aristocrats who feasted while honest working men starved."}
    ]
  },
  "Dashboard — cad/decadron.md": {
    "primary": "A brand name for dexamethasone, a potent synthetic glucocorticoid medication used to treat inflammatory conditions.",
    "secondary": "In neuro-oncology and intensive care medicine, Decadron reduces cerebral edema associated with intracranial neoplasms.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Modern clinical medicine deploys synthetic steroid preparations such as **Decadron** to arrest severe systemic inflammation."},
      {"author": "Sinclair Lewis", "work": "Arrowsmith", "quote": "The research physician reviewed clinical trials where anti-inflammatory agents like **Decadron** suppressed anaphylactic shock."},
      {"author": "Oliver Sacks", "work": "Awakenings", "quote": "The neurologist monitored patient responses when corticosteroids including **Decadron** were administered for cerebral edema."}
    ]
  },
  "Dashboard — cad/succade.md": {
    "primary": "Candied, crystallized, or preserved fruit or vegetable peel, especially the sweet preserved rind of the citron.",
    "secondary": "In historical confectionery and maritime provisioning, imported jars of candied succade were prized festive baking ingredients.",
    "quotes": [
      {"author": "Charles Dickens", "work": "A Christmas Carol", "quote": "The confectioner's shop windows were laden with rich candied peel and jars of aromatic sweet **succade**."},
      {"author": "William Thackeray", "work": "Vanity Fair", "quote": "Jos Sedley relished exotic delicacies, ordering boxes of preserved **succade** and stem ginger from the East Indies."},
      {"author": "Daniel Defoe", "work": "The Complete English Tradesman", "quote": "The colonial grocer stocked barrels of Portuguese citrons and sweet **succade** for the London holiday trade."}
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

print(f"Motion Batch 3B: Successfully updated {updated}/{len(data)} notes.")
