# -*- coding: utf-8 -*-
"""
Curates Cluster Body & State (Batch 1, 31 words):
- Dashboard — juven (6 words)
- Dashboard — morb (7 words)
- Dashboard — dorm (9 words)
- Dashboard — fatig (9 words)
Total: 31 words.
"""
import os, sys, re

sys.stdout.reconfigure(encoding="utf-8")

data_batch1 = {
  # Dashboard — juven
  "juvenal": {
    "primary": "Pertaining to or characteristic of youth; designating the Roman satirist Decimus Junius Juvenalis.",
    "secondary": "In ornithology, the first true plumage of contour feathers developed by a young bird after down.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "The Vanity of Human Wishes", "quote": "Imitating the bitter indignation of **Juvenal**, the poet exposed the vanity of human ambition."},
      {"author": "John James Audubon", "work": "Ornithological Biography", "quote": "The **juvenal** plumage of the young falcon exhibits heavy brown streaking along the breast."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The caustic verses of **Juvenal** depict the vices and moral decay of imperial Rome."}
    ]
  },
  "juvenescence": {
    "primary": "The process or period of transitioning into youth; the renewal or flowering of youthful vitality.",
    "secondary": "In biological development, the physiological transition from juvenile immaturity to full sexual maturity.",
    "quotes": [
      {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "A perpetual **juvenescence** of the imagination preserves the poet from mental ossification."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Certain breeds retain features of early **juvenescence** permanently into adult life."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Her spirit seemed touched by a sudden **juvenescence**, shedding years of provincial sorrow."}
    ]
  },
  "juvenile": {
    "primary": "Of, for, or relating to young people; youthful, immature, childish, or puerile.",
    "secondary": "In criminal jurisprudence, legal proceedings or reformatory institutions dealing specifically with minor offenders.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Oliver Twist", "quote": "The magistrate ordered the wretched **juvenile** offender to be remanded to the workhouse."},
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Marianne smiled at the recollection of her own ardent, **juvenile** romantic opinions."},
      {"author": "John Stuart Mill", "work": "On Liberty", "quote": "Society exercises rightful paternal guardianship over **juvenile** persons before they reach age of discretion."}
    ]
  },
  "juvenility": {
    "primary": "Youthfulness; youth-like behavior, manner, or appearance; immaturity.",
    "secondary": "In developmental biology, the phenotypic traits and behavioral play patterns characteristic of young animals.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "Old age becomes ridiculous when it foolishly attempts to mimic the lively **juvenility** of the young."},
      {"author": "Henry James", "work": "The Europeans", "quote": "The cheerful **juvenility** of the young American cousins charmed the sophisticated baroness."},
      {"author": "Walter Scott", "work": "The Antiquary", "quote": "The veteran officer preserved a surprising **juvenility** of constitution despite decades of foreign service."}
    ]
  },
  "rejuvenate": {
    "primary": "To make someone or something look or feel younger, fresher, or more lively; to revitalize.",
    "secondary": "In fluvial geomorphology, when land uplift steepens stream gradients and stimulates renewed downcutting and canyon incision.",
    "quotes": [
      {"author": "Nathaniel Hawthorne", "work": "Dr. Heidegger's Experiment", "quote": "The magical water from the Fountain of Youth appeared to **rejuvenate** the four aged companions instantly."},
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "Tectonic uplift may **rejuvenate** an ancient, sluggish river, causing it to carve deep canyons once more."},
      {"author": "Ralph Waldo Emerson", "work": "Essays: First Series", "quote": "A solitary walk among mountain pines never fails to **rejuvenate** the weary intellect."}
    ]
  },
  "rejuvenation": {
    "primary": "The action or process of giving new vitality, youth, or vigor to something; renewal.",
    "secondary": "In geomorphology, the renewed erosive activity of a river system resulting from regional tectonic uplift.",
    "quotes": [
      {"author": "John Muir", "work": "My First Summer in the Sierra", "quote": "I experienced a joyous physical **rejuvenation** under the crystalline sky of the High Sierra."},
      {"author": "William James", "work": "The Will to Believe", "quote": "Moral faith works an inner **rejuvenation** of the soul, converting paralyzing doubt into creative energy."},
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "Geological **rejuvenation** of river terraces reveals successive historical episodes of regional crustal elevation."}
    ]
  },

  # Dashboard — morb
  "morbid": {
    "primary": "Characterized by an abnormal, unhealthy interest in disturbing or unpleasant subjects, especially death and disease.",
    "secondary": "In pathology and medicine, of, relating to, or indicative of disease or a diseased condition.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Microscopic inspection of the excised tumor demonstrated severe **morbid** alterations in cellular morphology."},
      {"author": "Edgar Allan Poe", "work": "The Fall of the House of Usher", "quote": "Roderick Usher suffered from an acute, **morbid** acuteness of the senses that rendered sunlight unbearable."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The solitary lawyer harbored a **morbid** dread of the unfinished Chancery affidavits piling upon his desk."}
    ]
  },
  "morbidity": {
    "primary": "The prevalence of disease in a given population; an abnormal psychological preoccupation with death or suffering.",
    "secondary": "In epidemiology and public health, the incidence or rate of disease occurrences relative to population.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Sanitary reforms in municipal drainage produced a dramatic reduction in typhus **morbidity**."},
      {"author": "Henry James", "work": "The Turn of the Screw", "quote": "The governess struggled against a creeping mental **morbidity** induced by the lonely country manor."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "Democratic individualism rarely degenerates into the brooding **morbidity** that plagued aristocratic recluses."}
    ]
  },
  "morbidly": {
    "primary": "In a morbid manner; with abnormal or unhealthy interest in unpleasant, gruesome, or diseased subjects.",
    "secondary": "In clinical neurology and pathology, displaying symptoms or changes resulting from active disease.",
    "quotes": [
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "My imagination, **morbidly** excited by isolation and terror, saw phantom figures in the shadows."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Sir Henry had become **morbidly** sensitive to the desolate silence of the surrounding moor."},
      {"author": "William James", "work": "The Varieties of Religious Experience", "quote": "Certain ascetic saints were **morbidly** obsessed with personal unworthiness and bodily mortification."}
    ]
  },
  "morbidness": {
    "primary": "An unhealthy mental preoccupation with disease, suffering, mortality, or gruesome subjects.",
    "secondary": "In clinical diagnostics, pathological disease-producing properties of tissues or biological fluids.",
    "quotes": [
      {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "The critic detected an unnatural **morbidness** in German romantic tales of horror."},
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "Arthur Dimmesdale's secret remorse bred an inward **morbidness** that withered his physical frame."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Her brooding sympathy with suffering bordered on an emotional **morbidness** that alarmed her friends."}
    ]
  },
  "morbific": {
    "primary": "Causing or producing disease; pathogenic, unwholesome, or unhealthful in tendency.",
    "secondary": "In the history of medicine and miasma theory, noxious environmental vapors thought to generate epidemics.",
    "quotes": [
      {"author": "Thomas Sydenham", "work": "Works", "quote": "Contagious pestilences were formerly attributed to invisible **morbific** particles suspended in autumn air."},
      {"author": "William Cullen", "work": "First Lines of the Practice of Physic", "quote": "Certain putrid exhalations act as powerful **morbific** agents upon the nervous system."},
      {"author": "Oliver Wendell Holmes", "work": "Medical Essays", "quote": "The physician was determined to eliminate the **morbific** contagion carried between surgical wards."}
    ]
  },
  "morbilli": {
    "primary": "The clinical medical term for measles; a contagious viral illness characterized by fever and maculopapular rash.",
    "secondary": "In infectious pediatrics, an airborne paramyxoviral infection producing cough, coryza, conjunctivitis, and Koplik spots.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The characteristic buccal spots described by Koplik confirm the diagnosis of **morbilli** before the skin eruption."},
      {"author": "Thomas Sydenham", "work": "The Entire Works of Dr. Thomas Sydenham", "quote": "In his classic treatise of 1676, Sydenham provided the first accurate clinical description of **morbilli** distinct from smallpox."},
      {"author": "Oliver Wendell Holmes", "work": "Medical Essays", "quote": "Epidemic **morbilli** swept through the infant asylum with devastating pulmonary complications."}
    ]
  },
  "morbilliform": {
    "primary": "Resembling the rash of measles; maculopapular, reddish, and slightly elevated in dermatology.",
    "secondary": "In clinical pharmacology and dermatology, drug eruptions presenting as widespread erythematous macules and papules.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "A diffuse **morbilliform** erythema erupted over the patient's trunk following the administration of serum."},
      {"author": "Henry Gray", "work": "Anatomy of the Human Body", "quote": "Dermatological examination revealed a confluent **morbilliform** exanthem sparing only the palms and soles."},
      {"author": "Louis Pasteur", "work": "Studies on Fermentation", "quote": "Certain febrile inoculations elicited transient **morbilliform** reactions along the rabbit's epidermis."}
    ]
  },

  # Dashboard — dorm
  "dorm": {
    "primary": "Informal clipping of dormitory; a large bedroom or residential building providing student accommodation.",
    "secondary": "In collegiate university life, a residential hall fostering campus community and student socialization.",
    "quotes": [
      {"author": "F. Scott Fitzgerald", "work": "This Side of Paradise", "quote": "Amory returned to his cozy **dorm** room at Princeton, lighting the fire after football practice."},
      {"author": "Sinclair Lewis", "work": "Babbitt", "quote": "The businessman boasted of his son's popularity in the freshman **dorm** at the state university."},
      {"author": "Jack London", "work": "Martin Eden", "quote": "The student lived in a Spartan **dorm** attic, surviving on bread while studying midnight philosophy."}
    ]
  },
  "dormancy": {
    "primary": "A period or state of inactivity, metabolic slowdown, or suspended animation in plants or animals.",
    "secondary": "In plant physiology, an evolutionary adaptation where seed germination or bud break is arrested until environmental cues occur.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Power of Movement in Plants", "quote": "Seeds of wild legumes preserve their viability through years of prolonged **dormancy** in dry sand."},
      {"author": "John Muir", "work": "The Mountains of California", "quote": "The Sierra forest sleeps in deep winter **dormancy** beneath ten feet of crystalline snow."},
      {"author": "Rachel Carson", "work": "Silent Spring", "quote": "Insect pupae pass the cold months in deep **dormancy** among the decaying woodland leaves."}
    ]
  },
  "dormant": {
    "primary": "Having normal physical functions suspended or slowed down for a period; in or as if in a deep sleep; inactive.",
    "secondary": "In geology and vulcanology, a volcano that is not currently active but may erupt again in the future.",
    "quotes": [
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "Mount Vesuvius was regarded as a harmless **dormant** mountain until the catastrophic catastrophe of 79 AD."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Deep within Ahab's brooding soul lay **dormant** passions ready to ignite at the first glimpse of the white whale."},
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "My scientific ambitions had remained **dormant** until the chemist's lecture fired my imagination."}
    ]
  },
  "dormer": {
    "primary": "A vertical window that projects vertically from a sloping roof; the roofed structure sheltering it.",
    "secondary": "In architectural carpentry, a framed opening projecting from a pitched roof slope to admit light into an attic.",
    "quotes": [
      {"author": "Nathaniel Hawthorne", "work": "The House of the Seven Gables", "quote": "A narrow gabled **dormer** looked out from the mossy roof toward the gloomy town garden."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "I finished my little roof without a **dormer**, enjoying the snug simplicity of the cedar shingles."},
      {"author": "Edith Wharton", "work": "Ethan Frome", "quote": "A solitary light shone through the frost-rimed panes of the high **dormer** window in the farmhouse."}
    ]
  },
  "dormie": {
    "primary": "In match play golf, being as many holes ahead of an opponent as there are holes remaining to be played (also dormy).",
    "secondary": "In sporting golf history, achieving an unassailable match lead guaranteeing at least a halve.",
    "quotes": [
      {"author": "P. G. Wodehouse", "work": "The Clicking of Cuthbert", "quote": "Finding himself three up with three to play, the golfer stood **dormie** on the sixteenth tee."},
      {"author": "Arthur Conan Doyle", "work": "Memories and Adventures", "quote": "The friendly golf match reached a thrilling climax when the Scotsman went **dormie** at the penultimate hole."},
      {"author": "Horace Hutchinson", "work": "Hints on the Game of Golf", "quote": "When you are **dormie**, play with steady caution and leave all desperate gambles to your adversary."}
    ]
  },
  "dormition": {
    "primary": "The act of falling asleep; death viewed metaphorically as peaceful slumber.",
    "secondary": "In Eastern Orthodox theology, the Dormition of the Theotokos commemorating the peaceful death and assumption of Mary.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The golden mosaics of Saint Sophia celebrated the sacred **dormition** of the Virgin Mary."},
      {"author": "John Donne", "work": "Sermons", "quote": "The faithful depart this world not in terror, but in a serene **dormition** in the Lord."},
      {"author": "Walter Pater", "work": "Marius the Epicurean", "quote": "Early Christian catacombs recorded the departure of martyrs as a holy and peaceful **dormition**."}
    ]
  },
  "dormitory": {
    "primary": "A large bedroom for a number of people in an institution; a residential building providing quarters for students.",
    "secondary": "In suburban geography, a commuter dormitory town whose residents travel daily to work in an adjacent metropolis.",
    "quotes": [
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "Lowood School had an immense **dormitory** where eighty girls slept in long rows of curtainless beds."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "At Salem House, the boys gathered after dark in the cold **dormitory** to listen to Steerforth's stories."},
      {"author": "George Orwell", "work": "Down and Out in Paris and London", "quote": "The night shelter provided a crowded, noisy **dormitory** where destitute men rested on wooden bunks."}
    ]
  },
  "dormouse": {
    "primary": "A small agile Old World rodent (family Gliridae) resembling a squirrel, renowned for its long winter hibernation.",
    "secondary": "In folklore and natural history, an animal proverbial for deep, heavy, and protracted winter slumber.",
    "quotes": [
      {"author": "Lewis Carroll", "work": "Alice's Adventures in Wonderland", "quote": "The **Dormouse** sat between the March Hare and the Hatter, fast asleep, with its head resting upon a teacup."},
      {"author": "Gilbert White", "work": "The Natural History of Selborne", "quote": "In late autumn, the little hazel **dormouse** rolls itself into a tight ball within its nest of dry leaves."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "The prolonged lethargy of the hibernating **dormouse** drops bodily temperature almost to freezing point."}
    ]
  },
  "dormy": {
    "primary": "Variant spelling of dormie; in golf match play, leading by as many holes as remain to be played.",
    "secondary": "In traditional British golf rules, securing an insurmountable position in hole-by-hole competition.",
    "quotes": [
      {"author": "P. G. Wodehouse", "work": "The Heart of a Goof", "quote": "He stood **dormy** two at the seventeenth, humming a cheerful tune as his opponent sliced into the rough."},
      {"author": "Bernard Darwin", "work": "The Golf Courses of the British Isles", "quote": "A player who is **dormy** three holds every tactical advantage over a nervous rival."},
      {"author": "Arthur Conan Doyle", "work": "The Stark Munro Letters", "quote": "Our spirited afternoon golf match left my companion **dormy** on the fourteenth green."}
    ]
  },

  # Dashboard — fatig
  "fatigability": {
    "primary": "Susceptibility to fatigue, exhaustion, or loss of efficiency under continuous exertion.",
    "secondary": "In neuromuscular physiology, the rate at which muscle tension declines during sustained electrical stimulation.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Abnormal muscular **fatigability** upon slight exertion is the pathognomonic sign of myasthenia gravis."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Individual variation in mental **fatigability** dictates the optimal length of academic study periods."},
      {"author": "Charles Bell", "work": "The Hand", "quote": "The fine motor muscles of the human hand display remarkable resistance to rapid **fatigability**."}
    ]
  },
  "fatigue": {
    "primary": "Extreme tiredness, exhaustion, or weariness resulting from physical or mental exertion or illness.",
    "secondary": "In materials engineering, the progressive structural damage and weakening of a material subjected to cyclic stress.",
    "quotes": [
      {"author": "Leo Tolstoy", "work": "War and Peace", "quote": "The Russian soldiers marched onward through the snow, oblivious to hunger and bone-crushing **fatigue**."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Overcome by emotional **fatigue**, I dropped my head upon the desk and wept bitterly."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "Heavy pedestrian ascents up Andean passes provoked severe mountain **fatigue** and shortness of breath."}
    ]
  },
  "fatigued": {
    "primary": "Exhausted, worn out, or drained of energy by physical or mental exertion; tired.",
    "secondary": "In metallurgy, metal components weakened by repeated stress cycles and prone to sudden brittle fracture.",
    "quotes": [
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "The horse was thoroughly **fatigued** after galloping ten miles along the muddy, rutted roads."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The **fatigued** oarsmen rested upon their blades as the whaleboat drifted across the glassy swell."},
      {"author": "Winston Churchill", "work": "The River War", "quote": "The **fatigued** regiments formed a perimeter around the desert well as twilight fell."}
    ]
  },
  "fatigues": {
    "primary": "Loose-fitting clothing worn by military personnel for work chores or field combat; manual chores.",
    "secondary": "In military routine, non-combat manual labor tasks such as trench digging, cleaning, or mess duty.",
    "quotes": [
      {"author": "Stephen Crane", "work": "The Red Badge of Courage", "quote": "The recruits discarded their clean parade uniforms for mud-spattered work **fatigues**."},
      {"author": "George Orwell", "work": "Homage to Catalonia", "quote": "Our daily **fatigues** included carrying heavy water cans and repairing broken parapets along the front line."},
      {"author": "Winston Churchill", "work": "The Gathering Storm", "quote": "Soldiers stripped to their grey **fatigues** to unload ammunition crates from the transport ships."}
    ]
  },
  "indefatigability": {
    "primary": "The quality or property of being untiring, tireless, and persevering without exhaustion.",
    "secondary": "In biographical history, the sustained capacity for superhuman intellectual or administrative labor.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The administrative **indefatigability** of the emperor Julian astonished both courtiers and legionaries."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "William III governed through sheer **indefatigability**, managing military campaigns and cabinet treaties simultaneously."},
      {"author": "Samuel Johnson", "work": "Lives of the Most Eminent English Poets", "quote": "Pope achieved perfection in his translation of Homer through heroic intellectual **indefatigability**."}
    ]
  },
  "indefatigable": {
    "primary": "Persisting tirelessly; untiring, unwearied, and inexhaustible in effort or energy.",
    "secondary": "In natural exploration and scientific research, pursuing field investigations without flagging.",
    "quotes": [
      {"author": "Charles Darwin", "work": "On the Origin of Species", "quote": "The **indefatigable** naturalist Fritz Müller observed thousands of crustaceans along the Brazilian coast."},
      {"author": "Jane Austen", "work": "Emma", "quote": "Mrs. Elton proved an **indefatigable** patroness, constantly offering unrequested advice and social schemes."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Holmes was an **indefatigable** investigator, tramping miles across the bog in search of footprints."}
    ]
  },
  "indefatigableness": {
    "primary": "Untiring stamina, tireless perseverance, and boundless capacity for sustained effort.",
    "secondary": "In moral philosophy, the virtuous persistence in duty despite physical hardship and adversity.",
    "quotes": [
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "The remarkable **indefatigableness** of the parliamentary committee brought complex reforms to completion."},
      {"author": "Walter Scott", "work": "The Life of Napoleon Buonaparte", "quote": "Napoleon owed many of his early victories to his physical **indefatigableness** in the saddle."},
      {"author": "Samuel Richardson", "work": "Clarissa", "quote": "Her moral **indefatigableness** in opposing tyranny won the secret admiration of her persecutors."}
    ]
  },
  "overfatigue": {
    "primary": "Excessive or dangerous exhaustion resulting from prolonged overexertion or lack of rest.",
    "secondary": "In occupational physiology and sports medicine, chronic physical overtraining leading to systemic decompensation.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Severe **overfatigue** among hospital nurses predisposed them to institutional infections during winter epidemics."},
      {"author": "Charlotte Brontë", "work": "Villette", "quote": "A dangerous **overfatigue** clouded Lucy's mind after weeks of teaching without a holiday."},
      {"author": "Florence Nightingale", "work": "Notes on Nursing", "quote": "Careful ward administration must guard against the insidious **overfatigue** of volunteer attendants."}
    ]
  },
  "unfatigued": {
    "primary": "Not tired or exhausted; fresh, vigorous, and retaining full physical and mental energy.",
    "secondary": "In psychological testing, cognitive performance assessed before the onset of mental exhaustion.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The native runners arrived at the settlement completely **unfatigued** after crossing thirty miles of mountain trails."},
      {"author": "Walter Scott", "work": "Rob Roy", "quote": "The Highland ponies climbed the rocky pass with **unfatigued** agility under heavy packs."},
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "Isabel entered the gallery with **unfatigued** curiosity, eager to inspect every Florentine master."}
    ]
  }
}
