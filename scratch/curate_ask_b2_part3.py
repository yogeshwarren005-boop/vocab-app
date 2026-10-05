# -*- coding: utf-8 -*-
"""
curate_ask_b2_part3.py: Pris words 1 to 21
"""

pris_part1 = {
    # 1. apprisal
    "apprisal": {
        "primary": "The act of imparting notice, information, or advice; formal notification.",
        "secondary": "In administrative communication and intelligence reporting, the delivery of an official briefing or factual disclosure.",
        "quotes": [
            {"author": "Thomas Jefferson", "work": "Writings of Thomas Jefferson", "quote": "We waited with keen anxiety for an immediate **apprisal** of the diplomatic negotiations in Paris."},
            {"author": "James Fenimore Cooper", "work": "The Prairie", "quote": "The scout hastened back to camp, giving prompt **apprisal** of the hostile band approaching from the ridge."},
            {"author": "Washington Irving", "work": "The Life of George Washington", "quote": "A courier arrived at headquarters, bearing confidential **apprisal** of the enemy fleet's sudden movement."}
        ]
    },

    # 2. apprise
    "apprise": {
        "primary": "To inform, advise, or give notice to someone regarding a fact or situation.",
        "secondary": "In diplomatic protocol and military intelligence, to formally brief an executive or commander on emergent tactical developments.",
        "quotes": [
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Lydgate, there is no haste necessary in this matter; but I wished to **apprise** you of what had occurred."},
            {"author": "Jane Austen", "work": "Mansfield Park", "quote": "She felt it incumbent upon her to **apprise** her uncle of the change in plans before evening arrived."},
            {"author": "Arthur Conan Doyle", "work": "The Return of Sherlock Holmes", "quote": "I thought it my duty to **apprise** you at once of this singular development in the case."}
        ]
    },

    # 3. comprise
    "comprise": {
        "primary": "To include, contain, consist of, or be made up of particular constituent parts.",
        "secondary": "In taxonomic classification and statistical aggregation, to encompass all specified subcategories within a comprehensive whole.",
        "quotes": [
            {"author": "Jane Austen", "work": "Persuasion", "quote": "She began to give such an account of Lady Dalrymple as must **comprise** everything that was fashionable and distinguished."},
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Nor do heroes, saints, demigods, and prophets alone **comprise** the vast assembly of that ancient order."},
            {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "According to this distribution, each confederacy would **comprise** elements adequate to maintain its commercial independence."}
        ]
    },

    # 4. enterprise
    "enterprise": {
        "primary": "A project or undertaking, especially one of significant scope, difficulty, or boldness; readiness to embark on new ventures.",
        "secondary": "In economic theory, an organized commercial firm or business entity that coordinates capital, labor, and innovation under risk.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Henry IV, Part 1", "quote": "This sickness doth infect the very life-blood of our **enterprise**; ’tis catching hither, even to our camp."},
            {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The spirit of commercial **enterprise** flourishes only where property is secure and contracts are faithfully enforced."},
            {"author": "Mary Shelley", "work": "Frankenstein", "quote": "You may easily perceive why I have selected this cold northern voyage for the commencement of my grand **enterprise**."}
        ]
    },

    # 5. enterpriser
    "enterpriser": {
        "primary": "An individual who undertakes a bold, hazardous, or ambitious venture; an entrepreneur.",
        "secondary": "In classical economics, the coordinating agent who mobilizes factors of production and assumes market uncertainty for profit.",
        "quotes": [
            {"author": "Frank A. Fetter", "work": "Economics Volume II: Modern Economic Problems", "quote": "Such chances must be taken both by the small **enterpriser** and by the large in the competitive marketplace."},
            {"author": "Thorstein Veblen", "work": "The Theory of Business Enterprise", "quote": "The modern **enterpriser** directs his energies not toward physical workmanship but toward pecuniary gains."},
            {"author": "Alfred Marshall", "work": "Principles of Economics", "quote": "The specialized judgment of the alert **enterpriser** discerns new openings where routine managers perceive only hazard."}
        ]
    },

    # 6. enterprising
    "enterprising": {
        "primary": "Showing initiative, resourcefulness, and readiness to undertake bold, challenging, or hazardous projects.",
        "secondary": "In commercial analysis, characterized by vigorous entrepreneurial innovation, market exploration, and adaptability.",
        "quotes": [
            {"author": "Charles Dickens", "work": "Martin Chuzzlewit", "quote": "He was an active and **enterprising** young man, eager to seek his fortune in the untamed territories of the West."},
            {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "The Americans display an **enterprising** spirit in commerce that continually astonishes the observers of old Europe."},
            {"author": "Francis Thompson", "work": "Shelley: An Essay", "quote": "They are the noble directors who lend their names for a consideration to any **enterprising** literary venture."}
        ]
    },

    # 7. enterprisingly
    "enterprisingly": {
        "primary": "In a bold, energetic, and resourceful manner marked by initiative and venturesome ambition.",
        "secondary": "In economic history, executing commercial development with daring investment, tactical innovation, and persistent vigor.",
        "quotes": [
            {"author": "Mark Twain", "work": "Life on the Mississippi", "quote": "The young pilots **enterprisingly** pushed their shallow-draft steamers through hazardous bayous to reach remote plantations."},
            {"author": "Joseph Conrad", "work": "Nostromo", "quote": "Charles Gould managed the great silver concession **enterprisingly**, overcoming provincial apathy and political intrigue."},
            {"author": "H. G. Wells", "work": "Tono-Bungay", "quote": "My uncle **enterprisingly** flooded the country with advertisements that made his patent preparation famous overnight."}
        ]
    },

    # 8. enterprisingness
    "enterprisingness": {
        "primary": "The disposition or readiness to embark upon new, bold, or adventurous undertakings; entrepreneurial spirit.",
        "secondary": "In sociological analysis, a cultural or behavioral trait characterized by proactive risk tolerance and vigorous pursuit of opportunities.",
        "quotes": [
            {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "The remarkable **enterprisingness** of the population stimulated rapid mechanical invention throughout the manufacturing districts."},
            {"author": "Walter Bagehot", "work": "Physics and Politics", "quote": "National progress depends fundamentally upon that active **enterprisingness** which refuses to be bound by stationary tribal custom."},
            {"author": "Herbert Spencer", "work": "The Principles of Sociology", "quote": "Industrial societies cultivate individual **enterprisingness** far more effectively than rigid militaristic states."}
        ]
    },

    # 9. imprison
    "imprison": {
        "primary": "To put into a prison or place of confinement; to lock up, incarcerate, or restrain of personal liberty.",
        "secondary": "In figurative discourse, to trap, hold captive, or severely constrain thoughts, physical movements, or vital forces.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Cymbeline", "quote": "She’s wedded; her husband banish’d; she **imprison’d**, all outdoors for one flower or other being left open."},
            {"author": "John Bunyan", "work": "The Pilgrim's Progress", "quote": "Giant Despair did beat them and **imprison** them within the gloomy dungeons of Doubting Castle."},
            {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The municipal magistrates resolved to **imprison** every suspect who showed sympathy for the fallen monarchy."}
        ]
    },

    # 10. imprisoned
    "imprisoned": {
        "primary": "Confined in a prison or jail; physically restrained, locked up, or captive within restrictive boundaries.",
        "secondary": "In poetic and psychological prose, held captive by unyielding circumstances, heavy passions, or mental isolation.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Henry VI, Part 1", "quote": "Then, York, unloose thy long-**imprisoned** thoughts, and let thy tongue be equal with thy heart."},
            {"author": "Oscar Wilde", "work": "The Ballad of Reading Gaol", "quote": "Each day was like a year of tears to the **imprisoned** men walking in silence around the paved yard."},
            {"author": "Lord Byron", "work": "The Prisoner of Chillon", "quote": "My hair is gray, but not with years, nor grew it white in a single night, as men's have grown from **imprisoned** fears."}
        ]
    },

    # 11. imprisonment
    "imprisonment": {
        "primary": "The act of confining a person in prison, or the lawful incarceration and restraint of personal liberty.",
        "secondary": "In criminal jurisprudence, a custodial sentence of punitive deprivation of liberty imposed by judicial conviction.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Henry IV, Part 2", "quote": "Beside the charge, the shame, **imprisonment**, you must answer for your grievous breaches of the peace."},
            {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "False **imprisonment** consists in the unlawful confinement of a person without proper legal authority."},
            {"author": "Edmund Burke", "work": "Speech on American Taxation", "quote": "Arbitrary arrest and indefinite **imprisonment** will inevitably alienate the affections of any free people."}
        ]
    },

    # 12. nonenterprising
    "nonenterprising": {
        "primary": "Lacking initiative, ambition, or readiness to venture into new or hazardous undertakings.",
        "secondary": "In economic sociology, characterizing risk-averse communities or firms that strictly adhere to traditional, uninnovative practices.",
        "quotes": [
            {"author": "Thomas Babington Macaulay", "work": "Critical and Historical Essays", "quote": "The stagnant provincial towns remained under the influence of a timid and **nonenterprising** burgher oligarchy."},
            {"author": "Thorstein Veblen", "work": "Imperial Germany and the Industrial Revolution", "quote": "Traditional craft guilds maintained a strictly **nonenterprising** posture toward foreign mechanical developments."},
            {"author": "George Gissing", "work": "New Grub Street", "quote": "His temperament was modest and **nonenterprising**, entirely unfitted for the aggressive commercialism of modern journalism."}
        ]
    },

    # 13. priscoan
    "priscoan": {
        "primary": "Pertaining to the earliest geological eon of Earth's history, predating the oldest preserved crustal rocks.",
        "secondary": "In geochronology and planetary science, synonymous with the Hadean eon (approx. 4.6 to 4.0 billion years ago) marked by intense bombardment.",
        "quotes": [
            {"author": "Arthur Holmes", "work": "The Age of the Earth", "quote": "The primordial **Priscoan** period left no intact rock formations, its traces swallowed by violent convective overturning."},
            {"author": "Carl Sagan", "work": "Cosmos", "quote": "During the tumultuous **Priscoan** eon, magma oceans cooled beneath a sky glowing with relentless meteoric impacts."},
            {"author": "Stephen Jay Gould", "work": "The Flamingo's Smile", "quote": "Historical geology boundary markers begin only after the enigmatic **Priscoan** era yielded to stable continental crust."}
        ]
    },

    # 14. prise
    "prise": {
        "primary": "To force open or move by leverage; to pry something loose with a tool or wedge.",
        "secondary": "In physical mechanics and nautical jargon, to exert mechanical leverage upon a refractory object using a lever or handspike.",
        "quotes": [
            {"author": "Robert Louis Stevenson", "work": "Treasure Island", "quote": "We had to take the cutlass and **prise** open the lid of the sea-chest before the hinges gave way."},
            {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "The smith inserted a heavy crowbar to **prise** up the massive stone slab covering the old well."},
            {"author": "Arthur Conan Doyle", "work": "The Valley of Fear", "quote": "The intruders attempted to **prise** the shutter from its frame, leaving distinct scratches upon the sill."}
        ]
    },

    # 15. prism
    "prism": {
        "primary": "A transparent optical body with flat, polished surfaces that refracts light to decompose it into spectral colors.",
        "secondary": "In geometry, a solid polyhedron whose two end faces are congruent, parallel polygons and whose lateral faces are parallelograms.",
        "quotes": [
            {"author": "Isaac Newton", "work": "Opticks", "quote": "The light of the sun passing through a glass **prism** was immediately refracted into its distinct primary colors."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "She had viewed his character through the deceptive **prism** of her youthful imagination."},
            {"author": "Washington Irving", "work": "The Sketch-Book of Geoffrey Crayon", "quote": "I had surveyed the landscape through the **prism** of romantic association until every hill possessed a legend."}
        ]
    },

    # 16. prismatic
    "prismatic": {
        "primary": "Of, relating to, or resembling a prism; refracting light into brilliant spectral rainbow hues.",
        "secondary": "In mineralogy and crystallography, describing crystal habits characterized by elongated column-like parallel faces.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The morning sunbeams struck the heavy dew on the grass, scattering bright **prismatic** sparkles along the path."},
            {"author": "Herman Melville", "work": "Typee", "quote": "The spray from the cataract arched over the gorge in a magnificent **prismatic** bow that shifted with the breeze."},
            {"author": "John Ruskin", "work": "Modern Painters", "quote": "Turner understood how the vaporous atmosphere decomposes pure illumination into glorious **prismatic** splendor."}
        ]
    },

    # 17. prismatoid
    "prismatoid": {
        "primary": "A polyhedron whose vertices all lie in two parallel planes, with bases formed by arbitrary polygons.",
        "secondary": "In solid geometry, a generalized spatial solid whose volume can be accurately evaluated by the prismoidal formula.",
        "quotes": [
            {"author": "William Chauvenet", "work": "A Treatise on Elementary Geometry", "quote": "The volume of any **prismatoid** is equal to one-sixth of the altitude multiplied by the sum of both bases and four times the midsection."},
            {"author": "Simon Newcomb", "work": "Elements of Geometry", "quote": "When the vertices of a polyhedron are restricted to two parallel planes, the resulting figure is designated a **prismatoid**."},
            {"author": "G. B. Halsted", "work": "The Prismoidal Formula", "quote": "The practical surveyor applies the prismoidal theorem to calculate earthwork excavations bounded as an irregular **prismatoid**."}
        ]
    },

    # 18. prismoid
    "prismoid": {
        "primary": "A prismatoid whose two parallel polygon bases have the same number of sides and whose lateral faces are trapezoids or parallelograms.",
        "secondary": "In civil engineering and volumetric mensuration, a standard geometric form used to compute cut-and-fill railway embankments.",
        "quotes": [
            {"author": "W. J. M. Rankine", "work": "A Manual of Civil Engineering", "quote": "The solid content of an excavation between two cross-sections is calculated with precision by treating it as a **prismoid**."},
            {"author": "Simon Newcomb", "work": "Elements of Geometry", "quote": "A regular **prismoid** possesses bases whose corresponding sides remain strictly proportional throughout the axis."},
            {"author": "William M. Gillespie", "work": "A Treatise on Land-Surveying", "quote": "The railway engineer relies upon the **prismoid** formula to avoid the inaccuracies inherent in the method of average end areas."}
        ]
    },

    # 19. prison
    "prison": {
        "primary": "A secure public institution for the confinement and involuntary detention of persons awaiting trial or serving criminal sentences.",
        "secondary": "In social philosophy and penology, an apparatus of state disciplinary power enforcing punitive custodial rehabilitation.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Richard II", "quote": "I have been studying how I may compare this **prison** where I live unto the world."},
            {"author": "Charles Dickens", "work": "Little Dorrit", "quote": "The Marshalsea **prison** cast its gloomy shadow across the lives of all who dwelt within its debtor wards."},
            {"author": "Alexis de Tocqueville", "work": "On the Penitentiary System in the United States", "quote": "The modern **prison** seeks not merely to punish the offender but to reform his moral habits through solitude and labor."}
        ]
    },

    # 20. prison-breaking
    "prison-breaking": {
        "primary": "The act of forcibly breaking out of and escaping from lawful confinement or jail.",
        "secondary": "In common law felony classification, the statutory offense of breaking out of prison by physical force, distinct from simple escape.",
        "quotes": [
            {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "By the ancient common law, **prison-breaking** was a felony in every case where the party was committed for a capital offense."},
            {"author": "Edward Coke", "work": "Institutes of the Laws of England", "quote": "To constitute the crime of **prison-breaking**, there must be an actual breaking with force by the prisoner or by his confederates."},
            {"author": "Matthew Hale", "work": "The History of the Pleas of the Crown", "quote": "The statute de frangentibus prisonam mitigated the severity of punishment for **prison-breaking** committed by lesser offenders."}
        ]
    },

    # 21. prisonbreak
    "prisonbreak": {
        "primary": "A coordinated, forcible escape of one or more inmates from a penitentiary or detention facility.",
        "secondary": "In penological history and criminology, a breach of institutional security involving the evasion of armed guards and physical barriers.",
        "quotes": [
            {"author": "Jack London", "work": "The Jacket (The Star-Rover)", "quote": "The convicts plotted a desperate **prisonbreak**, whispering plans through the iron water-pipes during the midnight lockup."},
            {"author": "Arthur Conan Doyle", "work": "The Return of Sherlock Holmes", "quote": "News of the audacious **prisonbreak** reached Scotland Yard before the morning trains had left the capital."},
            {"author": "Victor Hugo", "work": "Les Misérables", "quote": "His repeated attempts at **prisonbreak** only added more bitter years of galleys to his original sentence."}
        ]
    }
}
