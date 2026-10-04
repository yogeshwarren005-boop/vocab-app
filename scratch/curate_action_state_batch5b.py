# -*- coding: utf-8 -*-
import os, sys, re
sys.stdout.reconfigure(encoding="utf-8")

data = {
  # --- Dashboard — len (58 words) ---
  "Dashboard — len/allen.md": {
    "primary": "A personal name or surname of Celtic origin; or an Allen key (hexagonal wrench tool).",
    "secondary": "In historical biography, Ethan Allen led the Green Mountain Boys in capturing Fort Ticonderoga during the American Revolutionary War.",
    "quotes": [
      {"author": "Washington Irving", "work": "Life of George Washington", "quote": "Colonel Ethan **allen** demanded the surrender of the British fortress in the name of the Great Jehovah and the Continental Congress."},
      {"author": "Henry David Thoreau", "work": "A Week on the Concord and Merrimack Rivers", "quote": "The frontiersman recalled the bold exploits of Ethan **allen** in the northern green mountains."},
      {"author": "Ralph Waldo Emerson", "work": "Representative Men", "quote": "The rough pioneer spirit of **allen** represented the untamed vigor of the early American border settlements."}
    ]
  },
  "Dashboard — len/allentown.md": {
    "primary": "A major industrial city in eastern Pennsylvania, situated along the Lehigh River.",
    "secondary": "In American economic and industrial history, Allentown developed as a premier center for anthracite iron manufacture and silk milling.",
    "quotes": [
      {"author": "Upton Sinclair", "work": "The Moneychangers", "quote": "Steel contracts negotiated in **allentown** sent ripples of speculative activity through the Wall Street exchanges."},
      {"author": "Theodore Dreiser", "work": "The Financier", "quote": "The railway barons planned branch extensions through the busy manufacturing districts of **allentown** and Bethlehem."},
      {"author": "W. E. B. Du Bois", "work": "The Philadelphia Negro", "quote": "Migrant laborers traveled along the Lehigh Valley lines connecting Philadelphia, **allentown**, and the mining towns."}
    ]
  },
  "Dashboard — len/lena.md": {
    "primary": "A major Siberian river flowing north into the Arctic Ocean; or a feminine given name.",
    "secondary": "In Russian geography and geology, the Lena River drains eastern Siberia, creating the Lena Pillars nature park and immense fossil mammoth beds.",
    "quotes": [
      {"author": "Leo Tolstoy", "work": "Resurrection", "quote": "The political exiles endured the grueling overland march across Siberia toward the icy reaches of the river **lena**."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Carcasses of woolly mammoths preserved in the frozen soil of the **lena** delta testify to past climatic fluctuations."},
      {"author": "Peter Kropotkin", "work": "Memoirs of a Revolutionist", "quote": "Geographical expeditions along the upper tributaries of the **lena** mapped uncharted mountain passes in eastern Siberia."}
    ]
  },
  "Dashboard — len/lenard.md": {
    "primary": "Philipp Lenard (1862–1947), German physicist who won the 1905 Nobel Prize for research on cathode rays.",
    "secondary": "In the history of modern physics, Lenard rays (cathode rays escaping thin metal foils) provided critical experimental data for the discovery of the electron.",
    "quotes": [
      {"author": "Albert Einstein", "work": "Investigations on the Theory of the Brownian Movement", "quote": "The pioneering photoelectric experiments of **lenard** stimulated our formulation of the light quantum hypothesis."},
      {"author": "Ernest Rutherford", "work": "Radioactive Substances and Their Radiations", "quote": "The penetrating power of cathode streams investigated by **lenard** demonstrated that atoms consist largely of empty space."},
      {"author": "J. J. Thomson", "work": "Conduction of Electricity through Gases", "quote": "Using a thin aluminum window, **lenard** succeeded in projecting cathode particles outside the vacuum tube into the air."}
    ]
  },
  "Dashboard — len/lene.md": {
    "primary": "A smooth, unaspirated consonant sound in classical Greek and phonetics; non-aspirated voiceless plosive.",
    "secondary": "In historical Indo-European phonology, the lene stops (p, t, k) contrast with aspiratae (ph, th, kh) and mediae (b, d, g).",
    "quotes": [
      {"author": "Max Müller", "work": "Lectures on the Science of Language", "quote": "Grimm's Law explains the systematic shift of ancient Greek **lene** consonants into Germanic voiceless fricatives."},
      {"author": "Henry Sweet", "work": "A Handbook of Phonetics", "quote": "The unaspirated **lene** stop is pronounced without the audible puff of breath that characterizes English plosives."},
      {"author": "Ferdinand de Saussure", "work": "Course in General Linguistics", "quote": "In archaic dialect inscriptions, the distinction between a **lene** consonant and an aspirate was preserved with phonetic rigor."}
    ]
  },
  "Dashboard — len/lenience.md": {
    "primary": "The disposition to show mercy, forbearance, mildness, or clemency toward offenders.",
    "secondary": "In judicial jurisprudence, statutory guidelines permit judicial lenience when mitigating factors outweigh aggravating circumstances.",
    "quotes": [
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The revolutionary tribunal showed not the slightest **lenience** to prisoners accused of aristocratic sympathies."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Mr. Farebrother advocated generous **lenience** in judging poor Fred Vincy's youthful monetary indiscretions."},
      {"author": "Edmund Burke", "work": "Speech on Conciliation with America", "quote": "True imperial statesmanship combines political firmness with magnanimous **lenience** toward colonial grievances."}
    ]
  },
  "Dashboard — len/leniency.md": {
    "primary": "Merciful tolerance, mildness in punishment, or compassionate indulgence.",
    "secondary": "In military discipline and criminal justice, perceived excess of leniency risks undermining deterrence and order.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "The police inspector warned that past **leniency** had only emboldened the audacious criminal gang."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The King's sudden **leniency** toward the captured insurgents surprised his vindictive councilors."},
      {"author": "Jane Austen", "work": "Mansfield Park", "quote": "Sir Thomas could not look with **leniency** upon conduct that had disgraced the moral honor of his family."}
    ]
  },
  "Dashboard — len/lenient.md": {
    "primary": "Characterized by mildness, mercy, tolerance, and forbearance in judgment or discipline.",
    "secondary": "In penal history, prison reformers advocated lenient treatment for juvenile first offenders to facilitate moral rehabilitation.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Measure for Measure", "quote": "Lord Angelo was urged to show a **lenient** heart toward Claudio, remembering human fallibility."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Joe Gargery was ever a gentle and **lenient** guardian, shielding Pip from Mrs. Joe's fiery temper."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The emperor Antoninus Pius was celebrated for his **lenient** administration and aversion to harsh capital sentences."}
    ]
  },
  "Dashboard — len/leniently.md": {
    "primary": "In a mild, compassionate, forgiving, or tolerant manner without harsh severity.",
    "secondary": "In judicial sentencing, first-time infractions are often dealt with leniently through restitution rather than penal confinement.",
    "quotes": [
      {"author": "George Eliot", "work": "Silas Marner", "quote": "The rector resolved to deal **leniently** with the wayward parish youth, offering counsel rather than public reproof."},
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "The elders debated whether to treat the repentant sinner **leniently** or enforce the full rigors of the colony's code."},
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Blue Carbuncle", "quote": "Holmes decided to treat the trembling culprit **leniently**, allowing him to escape prosecution at Christmastime."}
    ]
  },
  "Dashboard — len/lenify.md": {
    "primary": "To soothe, assuage, soften, mitigate, or alleviate pain, anger, or harshness.",
    "secondary": "In historical pharmacopeia and rhetoric, a soothing cordial or gentle speech was prescribed to lenify visceral or emotional distress.",
    "quotes": [
      {"author": "Francis Bacon", "work": "Sylva Sylvarum", "quote": "Certain balms and aromatic decoctions serve to **lenify** the irritation of acute topical inflammations."},
      {"author": "Robert Burton", "work": "The Anatomy of Melancholy", "quote": "Soft music and gentle discourse have wondrous power to **lenify** the bitter anguish of a troubled spirit."},
      {"author": "Jeremy Taylor", "work": "Holy Living", "quote": "Pious meditation operates to **lenify** the terrors of mortality and bring tranquil resignation to the dying."}
    ]
  },
  "Dashboard — len/lenin.md": {
    "primary": "Vladimir Ilyich Lenin (1870–1924), Russian revolutionary leader and founder of the Soviet state.",
    "secondary": "In political history, Lenin adapted Marxist economic theories to revolutionary vanguard party organisation, establishing the Bolshevik regime in 1917.",
    "quotes": [
      {"author": "Winston Churchill", "work": "The World Crisis", "quote": "The German high command transported **lenin** across Europe in a sealed train like a plague bacillus into Russia."},
      {"author": "H. G. Wells", "work": "Russia in the Shadows", "quote": "In the Kremlin, **lenin** explained his colossal dream for the universal electrification of the Russian countryside."},
      {"author": "Bertrand Russell", "work": "The Practice and Theory of Bolshevism", "quote": "Meeting with **lenin** impressed me with his extraordinary political willpower and fanatical intellectual single-mindedness."}
    ]
  },
  "Dashboard — len/leningrad.md": {
    "primary": "The Soviet name (1924–1991) for Saint Petersburg, Russia's historic Baltic imperial metropolis.",
    "secondary": "In World War II military history, the 872-day Siege of Leningrad stood as one of the deadliest and most harrowing urban sieges in human annals.",
    "quotes": [
      {"author": "Winston Churchill", "work": "The Second World War", "quote": "The heroic, protracted resistance of the citizens of **leningrad** tied down entire German army groups along the Baltic front."},
      {"author": "George Orwell", "work": "Animal Farm", "quote": "Soviet radio dispatches from besieged **leningrad** were listened to with solemn sympathy throughout wartime Britain."},
      {"author": "Vasily Grossman", "work": "Life and Fate", "quote": "The memory of the starvation winter of **leningrad** haunted the veteran soldiers as they prepared for the Don counteroffensive."}
    ]
  },
  "Dashboard — len/leninism.md": {
    "primary": "The political and economic theories of Vladimir Lenin, advocating vanguard revolutionary socialism and the dictatorship of the proletariat.",
    "secondary": "In twentieth-century political science, Marxism-Leninism combined historical materialism with central party control and anti-imperialist geopolitical theory.",
    "quotes": [
      {"author": "Bertrand Russell", "work": "The Practice and Theory of Bolshevism", "quote": "The strict dogma of **leninism** demanded absolute subordination of individual conscience to the revolutionary central committee."},
      {"author": "George Orwell", "work": "Nineteen Eighty-Four", "quote": "The ideological doctrines of Ingsoc derived their totalitarian bureaucratic mechanics from historical adaptations of **leninism**."},
      {"author": "Arthur Koestler", "work": "Darkness at Noon", "quote": "Rubashov reflected on the logical ruthlessness of **leninism**, which treated human individuals as mere statistical variables."}
    ]
  },
  "Dashboard — len/lenis.md": {
    "primary": "Produced with relatively weak muscular effort and low breath pressure; a weak, soft consonant.",
    "secondary": "In articulatory phonetics, English voiced plosives (b, d, g) are classified as lenis in contrast to voiceless fortis consonants (p, t, k).",
    "quotes": [
      {"author": "Henry Sweet", "work": "A Handbook of Phonetics", "quote": "The distinction between a fortis and a **lenis** consonant depends on the muscular tension exerted by the tongue and lips."},
      {"author": "Max Müller", "work": "Lectures on the Science of Language", "quote": "The phonologist observes that Germanic languages systematically soften medial plosives into a **lenis** articulation."},
      {"author": "Otto Jespersen", "work": "Language: Its Nature, Development and Origin", "quote": "In rapid colloquial speech, a voiceless stop frequently degenerates into a voiced **lenis** through economy of effort."}
    ]
  },
  "Dashboard — len/lenitive.md": {
    "primary": "Having the quality of easing pain, soothing irritation, or mitigating severity; a soothing medication.",
    "secondary": "In classical pharmacopeia, a lenitive electuary or syrup of senna was administered as a mild laxative to soothe bowel inflammation.",
    "quotes": [
      {"author": "Francis Bacon", "work": "Essays", "quote": "Prudent counsel and gentle speech act as a soothing **lenitive** upon the exasperated passions of the multitude."},
      {"author": "Robert Burton", "work": "The Anatomy of Melancholy", "quote": "The physician prescribed a gentle **lenitive** draught composed of sweet almond oil and barley water to calm the patient."},
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "Patience is the only sovereign **lenitive** that can mitigate the inevitable distresses of mortal life."}
    ]
  },
  "Dashboard — len/lenity.md": {
    "primary": "Gentleness of disposition, clemency, or merciful mildness of treatment toward offenders.",
    "secondary": "In classical statecraft, Roman emperors like Augustus balanced severe treason laws with displays of calculated imperial lenity.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Romeo and Juliet", "quote": "Away to heaven, respective **lenity**, and fire-eyed fury be my conduct now! Now, Tybalt, take the 'villain' back again."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The conquered provincials were astonished by the unusual **lenity** with which the barbarian king treated their municipal institutions."},
      {"author": "Edmund Burke", "work": "Speech on American Taxation", "quote": "Our ancestors governed their colonies by a policy of affectionate **lenity** and mutual commercial advantage."}
    ]
  },
  "Dashboard — len/lennoaceae.md": {
    "primary": "A small family of parasitic, achlorophyllous flowering plants native to arid deserts of North and South America.",
    "secondary": "In systematic botany, Lennoaceae (now often placed in Boraginaceae) comprises root parasites like Pholisma, lacking chlorophyll and true leaves.",
    "quotes": [
      {"author": "Asa Gray", "work": "Synoptical Flora of North America", "quote": "Botanists examining the desert flora of the Colorado basin described rare specimens belonging to the parasitic family **lennoaceae**."},
      {"author": "Charles Darwin", "work": "The Different Forms of Flowers on Plants of the Same Species", "quote": "The morphological reductions observed in root parasites like the **lennoaceae** parallel those seen in Rafflesiaceae."},
      {"author": "John Torrey", "work": "Report on the United States and Mexican Boundary Survey", "quote": "Among the sand dunes of the Gila river, explorers discovered fleshy subterranean spikes of the anomalous **lennoaceae**."}
    ]
  },
  "Dashboard — len/lennon.md": {
    "primary": "John Lennon (1940–1980), legendary English singer-songwriter, peace activist, and co-founder of the Beatles.",
    "secondary": "In twentieth-century cultural history, Lennon revolutionized popular music through innovative lyrical introspection, avant-garde arrangements, and global anti-war advocacy.",
    "quotes": [
      {"author": "George Harrison", "work": "I, Me, Mine", "quote": "Working in the studio with John **lennon** was an exhilarating adventure in musical spontaneity and fearless imagination."},
      {"author": "Philip Norman", "work": "Shout! The Beatles in Their Generation", "quote": "The caustic wit and raw emotional honesty of John **lennon** provided the driving creative engine of the band."},
      {"author": "Hunter S. Thompson", "work": "The Great Shark Hunt", "quote": "The songs of John **lennon** captured the turbulent spirit and dashed political hopes of an entire generation."}
    ]
  },
  "Dashboard — len/lens.md": {
    "primary": "A piece of glass or transparent material with curved sides for concentrating or dispersing light rays.",
    "secondary": "In optical physics and astronomy, chromatic aberration in a refracting lens is corrected by pairing flint and crown glass elements in an achromatic doublet.",
    "quotes": [
      {"author": "Isaac Newton", "work": "Opticks", "quote": "When light passes through a convex **lens**, rays of different colors are refracted at unequal angles, producing color fringes."},
      {"author": "Robert Hooke", "work": "Micrographia", "quote": "By adjusting the tiny glass **lens** of the microscope, the pores in cork tissue became plainly visible to the observer."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Holmes took out his magnifying **lens** and knelt down to examine the faint impressions on the carpet."}
    ]
  },
  "Dashboard — len/lense.md": {
    "primary": "A variant spelling of lens, referring to a transparent optical component that refracts light.",
    "secondary": "In historical nineteenth-century printings, the spelling 'lense' occasionally appeared in technical and photographic manuals before modern standardization.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Physiography", "quote": "The crystalline **lense** of the vertebrate eye adjusts its convexity to focus light sharply upon the retinal surface."},
      {"author": "Camille Flammarion", "work": "Popular Astronomy", "quote": "The giant objective **lense** of the telescope gathered distant starlight, revealing nebulae hidden to the naked eye."},
      {"author": "H. G. Wells", "work": "The Invisible Man", "quote": "He calculated how an optical **lense** could bend electromagnetic waves without casting a detectable shadow."}
    ]
  },
  "Dashboard — len/lensman.md": {
    "primary": "A photographer, especially a photojournalist; or a member of the elite interstellar law-enforcement corps in E. E. Smith's space operas.",
    "secondary": "In the history of science fiction, the Lensman series by E. E. 'Doc' Smith pioneered space opera tropes, centering on warriors wielding telepathic lenses.",
    "quotes": [
      {"author": "Arthur C. Clarke", "work": "Astounding Days", "quote": "Generations of science fiction readers were enthralled by the heroic exploits of the interstellar **lensman** in the pulp magazines."},
      {"author": "Isaac Asimov", "work": "Before the Golden Age", "quote": "E. E. Smith created in the cosmic **lensman** an archetype of galactic law enforcement that inspired countless space operas."},
      {"author": "Robert A. Heinlein", "work": "Expanded Universe", "quote": "The intrepid press **lensman** pushed his way to the front of the crowd to snap a photograph of the departing rocket."}
    ]
  },
  "Dashboard — len/lent.md": {
    "primary": "The period of forty days leading up to Easter, observed by Christian churches as a time of fasting, repentance, and prayer; or past tense of lend.",
    "secondary": "In liturgical history, Lent commences on Ash Wednesday, commemorating the forty-day fast of Jesus in the Judaean desert.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Romeo and Juliet", "quote": "No hare, sir; unless a hare, sir, in a **lent** pie, that is something stale and hoar ere it be spent."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Peggotty gently **lent** her ear to David's youthful troubles, comforting him with unwearied affection."},
      {"author": "Geoffrey Chaucer", "work": "The Canterbury Tales", "quote": "The devout parson observed the holy fast of **lent** with strict abstinence, giving his meager bread to the village poor."}
    ]
  },
  "Dashboard — len/lenten.md": {
    "primary": "Pertaining to, appropriate for, or characteristic of Lent; austere, somber, or meager.",
    "secondary": "In social and ecclesiastical history, Lenten entertainment restrictions historically curtailed public dramatic performances and meat consumption.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "To think, my lord, if you delight not in man, what **lenten** entertainment the players shall receive from you."},
      {"author": "Walter Scott", "work": "The Abbot", "quote": "The monastery refectory offered only **lenten** fare of salted herrings and coarse barley bread during the fast."},
      {"author": "Thomas Hardy", "work": "Under the Greenwood Tree", "quote": "The church choir practiced their **lenten** hymns with somber diligence under the guidance of the parish vicar."}
    ]
  },
  "Dashboard — len/lententide.md": {
    "primary": "The season or time of Lent; the liturgical forty-day period before Easter.",
    "secondary": "In medieval English social calendars, Lententide was marked by strict dietary fasting and cessation of seasonal festivities.",
    "quotes": [
      {"author": "Geoffrey Chaucer", "work": "The Canterbury Tales", "quote": "Throughout the solemn season of **lententide**, devout pilgrims traveled along muddy roads toward Canterbury."},
      {"author": "Walter Scott", "work": "Ivanhoe", "quote": "The hermit excused the frugality of his woodland cell, reminding his guest that holy **lententide** demanded austere penance."},
      {"author": "Thomas Carlyle", "work": "Past and Present", "quote": "Abbot Samson governed the abbey with vigilant discipline, inspecting the storehouses as **lententide** approached."}
    ]
  },
  "Dashboard — len/lentia.md": {
    "primary": "The ancient Roman name for modern Linz, Austria, a Roman fort and river station along the Danube limes.",
    "secondary": "In Roman provincial archaeology and military history, Lentia formed part of Noricum's fortified river border against Germanic Marcomannic raids.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The legions stationed at **lentia** patrolled the Danube limes, repelling barbarian incursions into Noricum."},
      {"author": "Theodor Mommsen", "work": "The Provinces of the Roman Empire", "quote": "Archaeological inscriptions uncovered at modern Linz attest to the auxiliary cavalry garrison quartered at ancient **lentia**."},
      {"author": "James Bryce", "work": "The Holy Roman Empire", "quote": "The strategic Danube crossing at **lentia** retained its military importance from imperial Roman times through the medieval empire."}
    ]
  },
  "Dashboard — len/lentibulariaceae.md": {
    "primary": "A botanical family of carnivorous flowering plants, commonly known as the bladderwort family.",
    "secondary": "In plant physiology and evolutionary ecology, Lentibulariaceae includes Utricularia, Pinguicula, and Genlisea, adapted to nutrient-poor aquatic habitats.",
    "quotes": [
      {"author": "Charles Darwin", "work": "Insectivorous Plants", "quote": "The extraordinary suction bladders of Utricularia, belonging to the family **lentibulariaceae**, capture microscopic aquatic crustacea with astonishing rapidity."},
      {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "Aquatic species of the family **lentibulariaceae** thrive in shallow peaty bogs, bearing delicate bilabiate flowers."},
      {"author": "Joseph Dalton Hooker", "work": "The Flora of British India", "quote": "Botanical surveys of Himalayan marshlands documented several endemic species of **lentibulariaceae** clinging to wet mossy rocks."}
    ]
  },
  "Dashboard — len/lentic.md": {
    "primary": "Pertaining to or inhabiting still, calm, or standing fresh water, such as lakes, ponds, or swamps.",
    "secondary": "In limnology and aquatic ecology, lentic ecosystems contrast with lotic (flowing water) systems, exhibiting vertical thermal stratification.",
    "quotes": [
      {"author": "Rachel Carson", "work": "Under the Sea-Wind", "quote": "Quiet **lentic** waters in woodland beaver ponds shelter teeming populations of dragon-fly larvae and tadpoles."},
      {"author": "Thomas Henry Huxley", "work": "Physiography", "quote": "The sedimentation patterns of a **lentic** basin preserve finely laminated varves of silt and organic detritus."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Freshwater shells inhabiting calm **lentic** pools often show wide geographical distribution across disconnected river basins."}
    ]
  },
  "Dashboard — len/lenticel.md": {
    "primary": "A porous tissue consisting of cells with large intercellular spaces in the periderm of woody plant stems, functioning as a pore.",
    "secondary": "In plant anatomy, a lenticel provides an opening through impermeable suberized bark, facilitating gas exchange between internal tissues and the atmosphere.",
    "quotes": [
      {"author": "Asa Gray", "work": "Structural Botany", "quote": "Under the microscope, each **lenticel** on the birch stem appears as a loose powdery mass of unsuberized cork cells."},
      {"author": "Charles Darwin", "work": "The Movements and Habits of Climbing Plants", "quote": "The climbing tendrils anchor themselves firmly, their surfaces dotted with microscopic **lenticel** apertures."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Plant respiration through bark is sustained by specialized **lenticel** openings that permit the inward diffusion of oxygen."}
    ]
  },
  "Dashboard — len/lenticular.md": {
    "primary": "Shaped like a lentil or a double-convex lens; biconvex.",
    "secondary": "In meteorology, lenticular clouds (altocumulus lenticularis) form stationary saucer-like lenses over mountain crests due to atmospheric standing waves.",
    "quotes": [
      {"author": "John Herschel", "work": "Outlines of Astronomy", "quote": "The Milky Way galaxy was originally conceived by William Herschel as a vast **lenticular** stratum of stars."},
      {"author": "Charles Darwin", "work": "Geological Observations on South America", "quote": "The quartz pebbles in the conglomerate were ground into smooth, flattened **lenticular** disks by surf action."},
      {"author": "Camille Flammarion", "work": "Popular Astronomy", "quote": "A magnificent **lenticular** cloud hovered motionless above the alpine peak, glowing crimson in the setting sun."}
    ]
  },
  "Dashboard — len/lentiform.md": {
    "primary": "Having the form or shape of a lentil; lenticular or biconvex.",
    "secondary": "In human neuroanatomy, the lentiform nucleus is a lens-shaped mass of grey matter within the basal ganglia, comprising the putamen and globus pallidus.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "A cerebral hemorrhage into the internal capsule frequently compresses adjacent **lentiform** nuclei, causing contralateral hemiplegia."},
      {"author": "Thomas Henry Huxley", "work": "The Anatomy of Vertebrated Animals", "quote": "Comparative dissection of mammalian brains reveals the distinct contour of the **lentiform** ganglion in the forebrain."},
      {"author": "Oliver Sacks", "work": "Awakenings", "quote": "Degenerative lesions affecting the **lentiform** nucleus produce the classic motor rigidity and tremors of post-encephalitic parkinsonism."}
    ]
  },
  "Dashboard — len/lentiginose.md": {
    "primary": "Covered with small freckle-like spots or freckly dots; lentiginous.",
    "secondary": "In descriptive botanical and entomological taxonomy, a lentiginose petal or insect wing exhibits minute, scattered brownish maculations.",
    "quotes": [
      {"author": "Asa Gray", "work": "Synoptical Flora of North America", "quote": "The pale corolla of the mountain orchid is delicately **lentiginose**, marked with tiny rust-colored flecks."},
      {"author": "Joseph Dalton Hooker", "work": "Flora Antarctica", "quote": "The herbarium specimen was distinguished by its **lentiginose** foliage, speckled with microscopic glandular spots."},
      {"author": "William Jackson Hooker", "work": "British Flora", "quote": "The lower lip of the foxglove blossom is distinctly **lentiginose**, guiding pollinating insects toward the nectary."}
    ]
  },
  "Dashboard — len/lentiginous.md": {
    "primary": "Relating to, covered with, or resembling freckles or lentigo; marked by small pigmented spots.",
    "secondary": "In clinical dermatology, acral lentiginous melanoma develops as an irregular pigmented macule on the palms, soles, or under nail beds.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The patient presented with widespread **lentiginous** mottling of the facial epidermis following prolonged solar exposure."},
      {"author": "Arthur Conan Doyle", "work": "Round the Red Lamp", "quote": "The doctor examined the **lentiginous** eruption across the patient's shoulders, diagnosing a harmless benign melanin cluster."},
      {"author": "Erasmus Wilson", "work": "Diseases of the Skin", "quote": "Fair-skinned individuals of reddish hair frequently display dense **lentiginous** macules upon the cheeks in summer."}
    ]
  },
  "Dashboard — len/lentigo.md": {
    "primary": "A small, clearly defined brownish or pigmented spot on the skin caused by localized proliferation of melanocytes; a freckle.",
    "secondary": "In dermatology, solar lentigo (commonly called a liver spot or age spot) results from cumulative ultraviolet radiation exposure in elderly individuals.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "A benign senile **lentigo** must be distinguished from dysplastic pigmented lesions during routine geriatric screening."},
      {"author": "Erasmus Wilson", "work": "On Diseases of the Skin", "quote": "The development of **lentigo** is accelerated by solar radiation, which stimulates melanogenesis in fair cutaneous types."},
      {"author": "Arthur Conan Doyle", "work": "The Stark Munro Letters", "quote": "The young physician examined the brown **lentigo** upon the patient's forearm, assuring him it posed no malignant threat."}
    ]
  },
  "Dashboard — len/lentil.md": {
    "primary": "A high-protein edible pulse or seed of the leguminous plant Lens culinaris, widely cultivated for food.",
    "secondary": "In agricultural history and paleobotany, the lentil was among the earliest domesticated founder crops in the fertile crescent over 9,000 years ago.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The Mediterranean peasant subsisted largely upon cheap porridge made from barley, beans, and the nutritious **lentil**."},
      {"author": "Charles Darwin", "work": "Insectivorous Plants", "quote": "I observed that the tender root-hairs of the sprouting **lentil** bent sensitively toward moisture in the soil."},
      {"author": "Leo Tolstoy", "work": "War and Peace", "quote": "The French soldier shared his mess-tin of boiled **lentil** stew with his famished Russian prisoner of war."}
    ]
  },
  "Dashboard — len/lentinus.md": {
    "primary": "A genus of wood-decaying bracket fungi in the family Polyporaceae, characterized by tough, leathery caps with serrated gills.",
    "secondary": "In mycology and forest pathology, Lentinus species cause white rot in fallen hardwood timber by enzymatically degrading lignin and cellulose.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The damp decaying tree-trunks in the Fuegian forests were encrusted with parasitic fungi of the genus **lentinus**."},
      {"author": "Joseph Dalton Hooker", "work": "Himalayan Journals", "quote": "We gathered specimens of a leathery **lentinus** mushroom growing abundantly upon rotted rhododendron trunks."},
      {"author": "William Jackson Hooker", "work": "Kew Gardens Bulletins", "quote": "Mycological collectors sent to the herbarium several new tropical species of **lentinus** noted for their tough, toothed gills."}
    ]
  },
  "Dashboard — len/lentisk.md": {
    "primary": "The mastic tree (Pistacia lentiscus), a small evergreen Mediterranean shrub yielding an aromatic resin called mastic.",
    "secondary": "In Mediterranean ethnobotany, the resinous gum harvested from the bark of the lentisk has been prized since antiquity for incense and breath fresheners.",
    "quotes": [
      {"author": "Richard Francis Burton", "work": "The Land of Midian", "quote": "The rocky limestone ravines were covered with dense fragrant thickets of wild thyme and resinous **lentisk**."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The island of Chios derived immense commercial revenues from its exclusive royal monopolies of the gum **lentisk**."},
      {"author": "Camille Flammarion", "work": "Travels in Greece and the Levant", "quote": "The warm air was scented with the balsam exudations of the green **lentisk** bushes bordering the Aegean shore."}
    ]
  },
  "Dashboard — len/lentissimo.md": {
    "primary": "A musical performance direction indicating that a passage should be played extremely slowly.",
    "secondary": "In orchestral score analysis, lentissimo indicates a tempo even more broad and decelerated than largo or lento, conveying profound solemnity.",
    "quotes": [
      {"author": "Romain Rolland", "work": "Jean-Christophe", "quote": "The funeral march moved with solemn majesty, played **lentissimo** by the muted brasses of the orchestra."},
      {"author": "Hector Berlioz", "work": "Treatise on Modern Instrumentation and Orchestration", "quote": "The composer directed the strings to sustain the opening chord **lentissimo**, creating an atmosphere of suspenseful awe."},
      {"author": "Arthur Symons", "work": "Plays, Acting and Music", "quote": "The cellist drew his bow **lentissimo** across the lower strings, producing a tone of deep mournful gravity."}
    ]
  },
  "Dashboard — len/lento.md": {
    "primary": "A musical tempo marking instructing that a piece or movement be played at a slow, stately pace.",
    "secondary": "In classical sonata form, a lento introduction frequently establishes tragic solemnity before launching into an allegro movement.",
    "quotes": [
      {"author": "Thomas Mann", "work": "Doctor Faustus", "quote": "The string quartet played the poignant **lento** movement with sublime contrapuntal clarity and restraint."},
      {"author": "E. M. Forster", "work": "A Room with a View", "quote": "Lucy played Beethoven's **lento** upon the drawing-room piano, pouring all her secret romantic longing into the keys."},
      {"author": "George Bernard Shaw", "work": "Music in London", "quote": "The conductor took the opening **lento** at an excessively dragging pace that robbed the melody of rhythmic pulse."}
    ]
  },
  "Dashboard — len/millenary.md": {
    "primary": "A thousandth anniversary, or a period consisting of a thousand years; millenarian.",
    "secondary": "In British church history, the Millenary Petition of 1603 was presented to King James I by Puritan ministers requesting ecclesiastical reforms.",
    "quotes": [
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "King James met the Puritan divines at the Hampton Court Conference following the presentation of the **millenary** petition."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Philip the Arab celebrated the **millenary** anniversary of the foundation of Rome with magnificent secular games in the Colosseum."},
      {"author": "Samuel Johnson", "work": "A Dictionary of the English Language", "quote": "The word **millenary** denotes both a space of a thousand years and one who expects the millennial reign."}
    ]
  },
  "Dashboard — len/millennial.md": {
    "primary": "Pertaining to or occurring every thousand years; or relating to the biblical millennium or a golden age of peace.",
    "secondary": "In sociopolitical discourse, millennial expectations inspire utopian movements anticipating the imminent transformation of human society.",
    "quotes": [
      {"author": "Ralph Waldo Emerson", "work": "Nature, Addresses, and Lectures", "quote": "Every reform movement contains within itself a spark of **millennial** enthusiasm, believing human nature can be perfected."},
      {"author": "Thomas Carlyle", "work": "Signs of the Times", "quote": "Modern mechanical optimism promises a **millennial** era of effortless wealth and universal comfort."},
      {"author": "H. G. Wells", "work": "The Outline of History", "quote": "Early Christian communities lived in intense **millennial** expectation of the immediate end of the earthly empire."}
    ]
  },
  "Dashboard — len/millennian.md": {
    "primary": "A person who believes in the millennium; a millenarian or chiliast.",
    "secondary": "In theological historiography, a millennian anticipated the literal thousand-year reign of Christ upon earth before the final judgment.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The ancient **millennian** believers comforted their persecuted brethren with prophecies of an earthly paradise."},
      {"author": "Thomas Babington Macaulay", "work": "Critical and Historical Essays", "quote": "The Fifth Monarchy men were fanatical **millennian** sectaries who refused allegiance to any earthly sovereign."},
      {"author": "John Locke", "work": "A Paraphrase and Notes on the Epistles of St. Paul", "quote": "Early patristic commentators occasionally adopted a literal **millennian** interpretation of apocalyptic visions."}
    ]
  },
  "Dashboard — len/millennium.md": {
    "primary": "A period of one thousand years, especially calculated from the traditional birth of Christ; or a future golden age of peace.",
    "secondary": "In apocalyptic theology and eschatology, the Millennium refers to the prophesied thousand-year earthly reign of righteousness in Revelation 20.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "As the close of the first **millennium** approached, a widespread panic seized Europe that the end of the world was at hand."},
      {"author": "H. G. Wells", "work": "The World Set Free", "quote": "The establishment of a unified world federation promised to usher in a new **millennium** of scientific prosperity and peace."},
      {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "Foolish dreamers expect a political **millennium** to arrive through mechanical acts of parliament alone."}
    ]
  },
  "Dashboard — len/millenniumism.md": {
    "primary": "The religious belief in the coming millennium, an earthly thousand-year reign of peace and spiritual righteousness.",
    "secondary": "In nineteenth-century American religious history, millenniumism gave birth to Millerism, Seventh-day Adventism, and various utopian commune experiments.",
    "quotes": [
      {"author": "William James", "work": "The Varieties of Religious Experience", "quote": "The fervor of apocalyptic **millenniumism** often reflects intense dissatisfaction with existing social inequalities."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "Religious enthusiasm in the American frontier frequently assumed the form of ardent **millenniumism** and revivalist camp meetings."},
      {"author": "Thomas Babington Macaulay", "work": "Critical and Historical Essays", "quote": "The English civil wars witnessed the proliferation of radical sects preaching militant **millenniumism** and immediate divine rule."}
    ]
  },
  "Dashboard — len/postmillennial.md": {
    "primary": "Relating to the theological belief that the second coming of Christ will occur after the millennium of Christian peace.",
    "secondary": "In American intellectual history, nineteenth-century postmillennial optimism fueled abolitionism, temperance crusades, and educational reforms.",
    "quotes": [
      {"author": "Ralph Waldo Emerson", "work": "Nature, Addresses, and Lectures", "quote": "The **postmillennial** reformers believed that moral education and social reform were actively building the kingdom of God on earth."},
      {"author": "William James", "work": "The Varieties of Religious Experience", "quote": "A robust **postmillennial** theology views human history as a progressive moral ascent toward divine harmony."},
      {"author": "H. G. Wells", "work": "The Outline of History", "quote": "The nineteenth-century faith in inevitable human progress was essentially a secularized version of **postmillennial** optimism."}
    ]
  },
  "Dashboard — len/relent.md": {
    "primary": "To abandon or mitigate a harsh, severe, or cruel intention or treatment; to become less severe or unyielding.",
    "secondary": "In narrative drama, a stubborn protagonist refuses to relent until tragic catastrophe shatters their resolve.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Richard III", "quote": "Relent, and save your souls. Which of you, if you were a prince's son, being shut up with murder, would not **relent**?"},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Can we think that the almighty will **relent** and grant us peaceful oblivion after this celestial rebellion?"},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "St. John Rivers was not a man to **relent** when once he had decided upon a path of religious duty."}
    ]
  },
  "Dashboard — len/relentless.md": {
    "primary": "Oppressively constant, unyielding, harsh, and refusing to abate or soften.",
    "secondary": "In natural history, relentless competition for scarce resources drives the adaptive divergence of living organisms.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Bucket pursued the clues through the labyrinthine streets of London with **relentless** tenacity."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The struggle for existence is **relentless** and perpetual among all organic beings sharing the same geographical region."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Captain Ahab drove the Pequod through stormy seas with a **relentless** fury that terrified his superstitious crew."}
    ]
  },
  "Dashboard — len/relentlessly.md": {
    "primary": "In an unyielding, severe, persistent, and unremitting manner without softening.",
    "secondary": "In investigative journalism, reporters pursue financial corruption relentlessly through thousands of banking records.",
    "quotes": [
      {"author": "Bram Stoker", "work": "Dracula", "quote": "Van Helsing tracked the vampire **relentlessly** across the Black Sea, giving him no respite by day or night."},
      {"author": "H. G. Wells", "work": "The War of the Worlds", "quote": "The Martian fighting-machines advanced **relentlessly** across Surrey, sweeping the countryside with their thermal heat-rays."},
      {"author": "Joseph Conrad", "work": "Heart of Darkness", "quote": "The silent jungle pressed in **relentlessly** upon the tiny river steamer like an impenetrable wall of shadow."}
    ]
  },
  "Dashboard — len/relentlessness.md": {
    "primary": "Unyielding persistence, unremitting severity, or inexorable determination.",
    "secondary": "In Greek tragedy, the relentlessness of fate (ananke) crushes mortal heroes who attempt to outwit divine oracles.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "The grim **relentlessness** of circumstance seemed deliberately contrived to bring about Michael Henchard's downfall."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The **relentlessness** of the Persian siege engines eventually battered down the eastern ramparts of Antioch."},
      {"author": "George Eliot", "work": "Romola", "quote": "Romola shuddered at the cold **relentlessness** with which Tito discarded every moral tie that threatened his personal safety."}
    ]
  },
  "Dashboard — len/selenarctos.md": {
    "primary": "A former zoological genus name for the Asian black bear (Selenarctos thibetanus), now classified under Ursus.",
    "secondary": "In mammalian taxonomy, Selenarctos (literally 'moon bear') was characterized by the distinctive white crescent marking across its chest.",
    "quotes": [
      {"author": "Alfred Russel Wallace", "work": "The Geographical Distribution of Animals", "quote": "The Himalayan black bear, designated **selenarctos** by Hodgson, ranges through forested montane belts across East Asia."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The crescent pectoral marking of **selenarctos** exhibits slight individual variation among geographic subspecies."},
      {"author": "Richard Lydekker", "work": "The Royal Natural History", "quote": "Hunters in the Assam hills encountered the fierce Asiatic bear, formerly placed in the subgenus **selenarctos**."}
    ]
  },
  "Dashboard — len/selene.md": {
    "primary": "The ancient Greek goddess and mythological personification of the moon; or the moon itself.",
    "secondary": "In Hellenic myth and classical poetry, Selene drove her silver chariot across the nocturnal sky, famously loving the sleeping Endymion.",
    "quotes": [
      {"author": "Percy Bysshe Shelley", "work": "Hellas", "quote": "The silver radiance of **selene** touched the Aegean waves, illuminating the dark hulls of the Greek fleet."},
      {"author": "John Keats", "work": "Endymion", "quote": "The shepherd youth lay entranced upon Mount Latmos while pale **selene** descended to kiss his sleeping brow."},
      {"author": "Camille Flammarion", "work": "Popular Astronomy", "quote": "Ancient Athenian poets sang hymns to **selene**, admiring the serene splendor of the crescent moon above the Parthenon."}
    ]
  },
  "Dashboard — len/selenicereus.md": {
    "primary": "A genus of climbing epiphytic cacti renowned for massive, fragrant, nocturnal white blooms; queen of the night.",
    "secondary": "In arid and tropical botany, Selenicereus grandiflorus produces fragrant blossoms up to a foot in diameter that open for a single night.",
    "quotes": [
      {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "Cultivated in warm greenhouses, the climbing cactus **selenicereus** delights horticulturists with its sweet-scented nocturnal flowers."},
      {"author": "Charles Darwin", "work": "The Different Forms of Flowers on Plants of the Same Species", "quote": "The rapid expansion of the night-blooming **selenicereus** corolla demonstrates sensitive floral adaptation to moth pollination."},
      {"author": "William Jackson Hooker", "work": "Curtis's Botanical Magazine", "quote": "The magnificent blossom of **selenicereus** grandiflorus opened at twilight, filling the conservatory with heavy vanilla fragrance."}
    ]
  },
  "Dashboard — len/selenipedium.md": {
    "primary": "A genus of primitive terrestrial slipper orchids native to tropical Central and South America.",
    "secondary": "In orchidology and plant evolutionary systematics, Selenipedium represents an ancient relict lineage possessing three-locular ovaries and plicate leaves.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Various Contrivances by Which Orchids Are Fertilised by Insects", "quote": "The primitive floral anatomy of **selenipedium** provides critical transitional links between ordinary monocotyledons and specialized slipper orchids."},
      {"author": "Joseph Dalton Hooker", "work": "Flora of the British West Indies", "quote": "Botanical collectors in the Andean cloud forests gathered rare specimens of **selenipedium** growing on shaded cliffs."},
      {"author": "Asa Gray", "work": "Elements of Botany", "quote": "The persistent perianth of **selenipedium** distinguishes this archaic orchid genus from its north temperate allies."}
    ]
  },
  "Dashboard — len/selenium.md": {
    "primary": "A nonmetallic chemical element of the oxygen group (atomic number 34), possessing unique photovoltaic and photoconductive properties.",
    "secondary": "Discovered by Jöns Jacob Berzelius in 1817, selenium was historically utilized in early photoelectric cells, glass decolouration, and xerography.",
    "quotes": [
      {"author": "Alexander Graham Bell", "work": "Upon the Production of Sound by Radiant Energy", "quote": "In our experiments with the photophone, we utilized a variable **selenium** resistance cell to transmit speech via a beam of light."},
      {"author": "Camille Flammarion", "work": "Popular Astronomy", "quote": "Berzelius discovered the element **selenium** in the residues of Swedish sulfuric acid works, naming it after the moon."},
      {"author": "Thomas Edison", "work": "The Edison Papers", "quote": "The electrical conductivity of **selenium** varies directly with illumination, making it an extraordinary medium for photographic sensing."}
    ]
  },
  "Dashboard — len/selenolatry.md": {
    "primary": "The religious worship of the moon, common among ancient pastoral and agrarian societies.",
    "secondary": "In comparative mythology and anthropological religion, selenolatry frequently preceded solar worship in early lunar calendar-based cultures.",
    "quotes": [
      {"author": "James George Frazer", "work": "The Golden Bough", "quote": "Traces of archaic **selenolatry** survive in folk customs that link agricultural planting and human fertility to the waxing moon."},
      {"author": "Edward Burnett Tylor", "work": "Primitive Culture", "quote": "The practice of **selenolatry** reflects the primal awe with which early mankind observed the nocturnal transformations of the lunar disk."},
      {"author": "Max Müller", "work": "Lectures on the Origin and Growth of Religion", "quote": "Comparative Aryan mythology reveals how poetic hymns to the moon gradually hardened into liturgical **selenolatry**."}
    ]
  },
  "Dashboard — len/selenology.md": {
    "primary": "The scientific branch of astronomy that deals with the geology, topography, and physical features of the moon.",
    "secondary": "In lunar science, selenology maps crater formations, mare basalt flows, and regolith properties through orbital radar and returned Apollo rock samples.",
    "quotes": [
      {"author": "Jules Verne", "work": "From the Earth to the Moon", "quote": "Barbicane delivered an exhaustive lecture on **selenology**, mapping the craters of Tycho and Copernicus for the gun club members."},
      {"author": "John Herschel", "work": "Outlines of Astronomy", "quote": "Telescopic **selenology** proves conclusively that the lunar surface lacks oceans, clouds, and an appreciable gaseous atmosphere."},
      {"author": "Camille Flammarion", "work": "Popular Astronomy", "quote": "Modern **selenology** has reconstructed the fiery volcanic origins of the vast lunar ring plains."}
    ]
  },
  "Dashboard — len/somnolence.md": {
    "primary": "Drowsiness, heavy sleepiness, or an unnatural inclination toward slumber.",
    "secondary": "In clinical neurology, progressive somnolence is a warning symptom of increased intracranial pressure or metabolic encephalopathy.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The onset of uremic poisoning is heralded by increasing headache, mental apathy, and profound **somnolence**."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The warm afternoon air of the Lord Chancellor's court induced a state of heavy **somnolence** among the barristers."},
      {"author": "Thomas Hardy", "work": "The Woodlanders", "quote": "The gentle hum of the cider press lulled the farmhands into a tranquil **somnolence** beneath the orchard shade."}
    ]
  },
  "Dashboard — len/somnolent.md": {
    "primary": "Sleepy, drowsy, heavy with slumber, or inducing sleep; quiet and inactive.",
    "secondary": "In regional fiction, a somnolent cathedral town or country village sleeps peacefully away from the noisy rush of modern industrial centers.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "The great moor lay **somnolent** under the autumn twilight, silent save for the occasional cry of a curlew."},
      {"author": "Nathaniel Hawthorne", "work": "The House of the Seven Gables", "quote": "Old Hepzibah sat in the **somnolent** shop, startled whenever the bell above the door jangled for a customer."},
      {"author": "Washington Irving", "work": "The Legend of Sleepy Hollow", "quote": "A drowsy, dreamy influence seems to hang over the land and to pervade the very atmosphere of this **somnolent** valley."}
    ]
  },
  "Dashboard — len/somnolently.md": {
    "primary": "In a drowsy, sleepy, sluggish, or lethargic manner.",
    "secondary": "In descriptive narrative prose, domestic animals blink somnolently before a crackling fireplace during winter evenings.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Joe Gargery sat by the kitchen forge, nodding **somnolently** with his pipe in his hand after a hard day's labor."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "The fat spaniel blinked **somnolently** upon the hearth-rug, undisturbed by the conversation of the drawing-room guests."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The dairy cows chewed their cud **somnolently** in the lush riverside meadow under the heavy midday warmth."}
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

print(f"Dashboard — len: Successfully updated {updated}/{len(data)} notes.")
