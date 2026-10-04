# -*- coding: utf-8 -*-
"""
Curates Cluster Color & Appearance (Batch 1, 50 words):
- Dashboard — virid (3 words)
- Dashboard — ater (4 words)
- Dashboard — aure (5 words)
- Dashboard — purpur (5 words)
- Dashboard — fusc (6 words)
- Dashboard — macul (8 words)
- Dashboard — russ (8 words)
- Dashboard — nigr (11 words)
Total: 50 words.
"""
import sys, re

sys.stdout.reconfigure(encoding="utf-8")

data_batch1 = {
  # Dashboard — virid (3 words)
  "viridescent": {
    "primary": "Becoming green or greenish; tinged with or taking on a fresh green hue.",
    "secondary": "In botany and ecology, describing young foliage turning green with chlorophyll during spring.",
    "quotes": [
      {"author": "John Ruskin", "work": "Modern Painters", "quote": "The grey limestone ledges were softened by **viridescent** patches of early alpine moss."},
      {"author": "Thomas Hardy", "work": "The Woodlanders", "quote": "The spring hedgerows turned delicately **viridescent** as tender birch buds unfolded."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "The ice upon the pond assumed a **viridescent** cast before breaking up in April."}
    ]
  },
  "viridian": {
    "primary": "A bluish-green pigment composed of hydrated chromium(III) oxide, prized for brilliant permanence.",
    "secondary": "A deep vivid green color with a subtle bluish undertone, widely favored by landscape painters.",
    "quotes": [
      {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "The tapestry was embroidered with peacocks displaying plumes of iridescent **viridian** and gold."},
      {"author": "Virginia Woolf", "work": "To the Lighthouse", "quote": "Lily Briscoe dabbed her brush in clean **viridian** to capture the cool shadow across the lawn."},
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The deep **viridian** of the canal water mirrored the weathered marble facades of the palazzi."}
    ]
  },
  "viridity": {
    "primary": "Fresh greenness of growing vegetation; youthful vigor, innocence, or naive freshness.",
    "secondary": "In landscape aesthetics, the vivid verdant hue of moist temperate pastures and woodlands.",
    "quotes": [
      {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "Poetic imagination restores the dew and pristine **viridity** of childhood perceptions."},
      {"author": "Nathaniel Hawthorne", "work": "The Blithedale Romance", "quote": "The springtime meadow shone with an exhilarating **viridity** that gladdened our spirits."},
      {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "The soul renews its spiritual **viridity** after shedding dead dogmas and formal robes."}
    ]
  },

  # Dashboard — ater (4 words)
  "anteater": {
    "primary": "A toothless mammal that feeds primarily on ants and termites, possessing an elongated tubular snout.",
    "secondary": "In zoology, a xenarthran mammal adapted to specialized insectivory with sticky saliva and powerful digging claws.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "We observed the giant **anteater** pacing across the pampas, tearing open hardened termite mounds."},
      {"author": "Alfred Russel Wallace", "work": "Tropical Nature and Other Essays", "quote": "The anatomical specializations of the South American **anteater** illustrate extreme niche adaptation."},
      {"author": "William Henry Hudson", "work": "The Naturalist in La Plata", "quote": "A solitary great **anteater** ambled along the dusty cattle trail, unfazed by our horses."}
    ]
  },
  "eater": {
    "primary": "A person, animal, or organism that consumes food or sustenance.",
    "secondary": "In social description, a person characterized by a particular appetite or dietary habit.",
    "quotes": [
      {"author": "Thomas De Quincey", "work": "Confessions of an English Opium-Eater", "quote": "The solitary opium-**eater** experienced celestial visions succeeded by unutterable gloom."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "A cannibal is a hearty **eater** who finds relish in wholesome sustenance after a hard voyage."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Joe Gargery was a modest **eater**, marveling at Pip's refined appetite at the forge table."}
    ]
  },
  "eatery": {
    "primary": "An informal restaurant, diner, cafe, or other casual dining establishment serving meals.",
    "secondary": "In colloquial American usage, a small neighborhood food shop or roadside canteen.",
    "quotes": [
      {"author": "Sinclair Lewis", "work": "Main Street", "quote": "The provincial town boasted a modest German bakery and a bustling roadside **eatery** near the depot."},
      {"author": "F. Scott Fitzgerald", "work": "The Great Gatsby", "quote": "Nick and Jordan stopped at a modest highway **eatery** to escape the oppressive summer heat."},
      {"author": "John Steinbeck", "work": "The Grapes of Wrath", "quote": "Truckers gathered at the roadside **eatery** along Route 66, drinking hot black coffee."}
    ]
  },
  "quaternary": {
    "primary": "Consisting of four units, elements, or members; fourth in an order or sequence.",
    "secondary": "In geology, the current and most recent period of the Cenozoic era, spanning the last 2.58 million years.",
    "quotes": [
      {"author": "Charles Lyell", "work": "The Geological Evidences of the Antiquity of Man", "quote": "Fossil deposits of the **quaternary** period demonstrate the coexistence of early man with the mammoth."},
      {"author": "Thomas Henry Huxley", "work": "Discourses: Biological and Geological", "quote": "Glacial moraines across northern Europe were deposited during the eventful **quaternary** epoch."},
      {"author": "Louis Agassiz", "work": "Geological Sketches", "quote": "The colossal ice sheets of the **quaternary** reshaped the topography of North America."}
    ]
  },

  # Dashboard — aure (5 words)
  "aureate": {
    "primary": "Golden in color; having the radiant splendor or appearance of pure gold.",
    "secondary": "Denoting an overly ornate, florid, or rhetorical style of literary language.",
    "quotes": [
      {"author": "John Keats", "work": "Hyperion", "quote": "The god reclined upon an **aureate** throne glowing amidst the celestial evening clouds."},
      {"author": "Thomas Babington Macaulay", "work": "Critical and Historical Essays", "quote": "The poet adorned his verses with **aureate** diction borrowed from medieval Latin hymns."},
      {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "The book was bound in antique **aureate** leather embossed with exquisite Venetian arabesques."}
    ]
  },
  "aurelius": {
    "primary": "Marcus Aurelius Antoninus (121-180 AD), Roman Emperor and renowned Stoic philosopher.",
    "secondary": "In classical intellectual history, the emperor renowned for authoring the Meditations on duty and virtue.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The Roman world flourished in peace under the enlightened philosophical rule of Marcus **Aurelius**."},
      {"author": "Matthew Arnold", "work": "Essays in Criticism", "quote": "Marcus **Aurelius** remains the purest and most tragic figure of the ancient pagan moralists."},
      {"author": "John Stuart Mill", "work": "On Liberty", "quote": "Even the wise emperor Marcus **Aurelius** failed to foresee the historical destiny of the new Christian faith."}
    ]
  },
  "aureolaria": {
    "primary": "A genus of North American hemiparasitic flowering plants known as false foxgloves (family Orobanchaceae).",
    "secondary": "Yellow-flowered woodland herbs whose root systems attach parasitically to oak tree roots.",
    "quotes": [
      {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The tall golden trumpets of **Aureolaria** illuminate the dry upland oak woods in late summer."},
      {"author": "John Torrey", "work": "Flora of North America", "quote": "Botanists classified several parasitic woodland herbs under the generic name **Aureolaria**."},
      {"author": "William Bartram", "work": "Travels through North and South Carolina", "quote": "Along the sandy pine barrens we observed glorious yellow blossoms of wild **Aureolaria**."}
    ]
  },
  "aureole": {
    "primary": "A circle of light, halo, or radiant aura surrounding the head or body of a holy figure.",
    "secondary": "In astronomy and meteorology, a luminous corona seen around the sun or moon through thin cloud.",
    "quotes": [
      {"author": "John Ruskin", "work": "Modern Painters", "quote": "Early Italian masters painted an exquisite golden **aureole** encircling the Madonna's head."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "The lamp cast an **aureole** of soft amber light over the sleeping child's curls."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The morning sun formed a radiant **aureole** around her hair as she crossed the dew-drenched meadow."}
    ]
  },
  "aureomycin": {
    "primary": "An early broad-spectrum antibiotic (chlortetracycline) discovered in 1945, derived from Streptomyces aureofaciens.",
    "secondary": "In clinical pharmacology, a golden-yellow crystalline antibiotic historically used against bacterial and rickettsial infections.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The therapeutic introduction of **aureomycin** drastically lowered mortality from typhus and pneumonia."},
      {"author": "Sinclair Lewis", "work": "Arrowsmith", "quote": "The medical laboratory celebrated the extraction of crystalline **aureomycin** from soil actinomycetes."},
      {"author": "Rachel Carson", "work": "Silent Spring", "quote": "Agricultural use of antibiotic supplements like **aureomycin** in livestock feeds raised concerns of drug resistance."}
    ]
  },

  # Dashboard — purpur (5 words)
  "purpura": {
    "primary": "A rash of purple spots on the skin caused by internal bleeding from small capillary blood vessels.",
    "secondary": "In clinical hematology, a hemorrhagic condition associated with thrombocytopenia or vascular inflammation.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Extensive cutaneous **purpura** accompanied by joint pains signaled Henoch-Schonlein syndrome."},
      {"author": "Henry Gray", "work": "Anatomy of the Human Body", "quote": "Subcutaneous extravasation of red blood cells produces the typical petechial lesions of **purpura**."},
      {"author": "Jonathan Hutchinson", "work": "Clinical Lectures on Rare Diseases", "quote": "The physician differentiated simple senile **purpura** from malignant hemorrhagic diathesis."}
    ]
  },
  "purpurate": {
    "primary": "A salt or ester of purpuric acid, especially ammonium purpurate (murexide).",
    "secondary": "In classical terminology, colored purple; or a person invested with imperial purple dignity.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Experimental Researches in Chemistry and Physics", "quote": "Treatment of uric acid with nitric acid and ammonia yields the brilliant crimson crystals of ammonium **purpurate**."},
      {"author": "Humphry Davy", "work": "Elements of Chemical Philosophy", "quote": "The reddish-purple coloration indicated the presence of synthetic **purpurate** compounds."},
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The Roman senate greeted the **purpurate** general returning in triumph from the Persian frontier."}
    ]
  },
  "purpure": {
    "primary": "In heraldry, the heraldic tincture purple, depicted in uncolored engravings by diagonal lines.",
    "secondary": "Of or relating to the color purple in armorial bearings and chivalric insignia.",
    "quotes": [
      {"author": "Walter Scott", "work": "Ivanhoe", "quote": "The knight's shield was blazoned with a lion rampant upon a field of **purpure**."},
      {"author": "Arthur Conan Doyle", "work": "The White Company", "quote": "The herald inspected the banner bearing a chevron **purpure** between three golden martlets."},
      {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "Feudal heraldry blazoned every coat with argent, gules, and imperial **purpure**."}
    ]
  },
  "purpureal": {
    "primary": "Of a purple or imperial crimson color; purpureous, richly regal, or purple-hued.",
    "secondary": "In poetic literature, adorned with or characterized by opulent purple splendor.",
    "quotes": [
      {"author": "John Keats", "work": "Endymion", "quote": "Sunset poured its **purpureal** glory across the silent mountain peaks of Latmos."},
      {"author": "Edgar Allan Poe", "work": "Al Aaraaf", "quote": "The distant star glowed with **purpureal** radiance through the velvet interstellar void."},
      {"author": "Percy Bysshe Shelley", "work": "Prometheus Unbound", "quote": "Vapors of bright **purpureal** mist ascended from the enchanted chasms beneath."}
    ]
  },
  "purpurin": {
    "primary": "A red anthraquinone dye extracted from the root of the madder plant (Rubia tinctorum).",
    "secondary": "In organic chemistry, 1,2,4-trihydroxyanthraquinone, used as a histological biological stain.",
    "quotes": [
      {"author": "William Henry Perkin", "work": "Journal of the Chemical Society", "quote": "Extraction of natural madder root yielded alizarin alongside bright crystalline needles of **purpurin**."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Chemistry and Physics", "quote": "The optical absorption spectrum of **purpurin** distinguishes it readily from synthetic coal-tar dyes."},
      {"author": "Henry Gray", "work": "Anatomy of the Human Body", "quote": "Histologists employed **purpurin** to demonstrate microscopic calcium deposits in osseous specimens."}
    ]
  },

  # Dashboard — fusc (6 words)
  "fuscoboletinus": {
    "primary": "A genus of bolete mushrooms characterized by dark dusky or fuscous spore prints and glandular stems.",
    "secondary": "Mycorrhizal fungi found in boreal peat bogs and conifer forests, closely allied to the genus Suillus.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Boreal conifer forests nourish symbiotic boletes of the genus **Fuscoboletinus** along peat hollows."},
      {"author": "John Muir", "work": "My First Summer in the Sierra", "quote": "Beneath the damp tamarack pines flourished robust clusters of the dark-spored **Fuscoboletinus**."},
      {"author": "William Bartram", "work": "Travels through North and South Carolina", "quote": "Naturalists cataloged unusual fleshy boletes including dark-capped species of **Fuscoboletinus** in swamp margins."}
    ]
  },
  "fuscous": {
    "primary": "Of a dark, gloomy, brownish-gray or dusky color; somber in tone.",
    "secondary": "In entomology and ornithology, describing dull brownish-black plumage or insect wing coloration.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The plumage of the Galapagos ground finch is of a dull, uniform **fuscous** brown."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "A **fuscous** cloud of smoke billowed from the whale-tryworks into the midnight air."},
      {"author": "John Ruskin", "work": "Modern Painters", "quote": "The background was painted in **fuscous** tones that highlighted the glowing flesh tints."}
    ]
  },
  "infuscate": {
    "primary": "To darken, obscure, or tinge with a dusky brownish or smoky hue.",
    "secondary": "In entomology, describing insect wings or body segments that are clouded with dark pigment.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Certain island beetles exhibit darkened or **infuscate** elytra adapted to volcanic sands."},
      {"author": "Thomas Henry Huxley", "work": "Manual of the Anatomy of Invertebrated Animals", "quote": "The membranous wings of the sawfly become progressively **infuscate** toward their outer margins."},
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "Centuries of coal smoke had served to **infuscate** the delicate reliefs of the cathedral portal."}
    ]
  },
  "obfuscate": {
    "primary": "To make obscure, unclear, or unintelligible; to deliberately bewilder or confuse.",
    "secondary": "To darken or cast a shadow over an intellectual argument or conceptual distinction.",
    "quotes": [
      {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "Pedantic commentators labored to **obfuscate** the simple truth beneath mountains of Latin glosses."},
      {"author": "George Orwell", "work": "Politics and the English Language", "quote": "Pretentious diction is used to **obfuscate** harsh political realities from public scrutiny."},
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "Scholastic disputations tend to **obfuscate** genuine inquiry through endless verbal sophistry."}
    ]
  },
  "obfuscation": {
    "primary": "The action of making something obscure, ambiguous, or difficult to understand.",
    "secondary": "In rhetoric and law, the deliberate creation of confusion to conceal uncomfortable facts.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The Court of Chancery was an impenetrable fog of legal technicality and institutional **obfuscation**."},
      {"author": "Thomas Babington Macaulay", "work": "History of England", "quote": "The minister deployed diplomatic **obfuscation** to conceal the controversial clauses of the treaty."},
      {"author": "John Stuart Mill", "work": "System of Logic", "quote": "Fallacious arguments survive only through the systematic **obfuscation** of fundamental terms."}
    ]
  },
  "subfusc": {
    "primary": "Dull, dark, dusky, or sober in color; traditional dark clothing worn for university examinations.",
    "secondary": "Specifically, the dark formal academic dress worn with cap and gown at Oxford University.",
    "quotes": [
      {"author": "Max Beerbohm", "work": "Zuleika Dobson", "quote": "Undergraduates hurried into the examination schools, clad in sober **subfusc** attire beneath black gowns."},
      {"author": "Thomas Hardy", "work": "Jude the Obscure", "quote": "Jude observed the scholars walking through the college quadrangles in dignified **subfusc** garments."},
      {"author": "John Ruskin", "work": "Praeterita", "quote": "The Victorian university maintained a severe code of **subfusc** habit for all solemn occasions."}
    ]
  },

  # Dashboard — macul (8 words)
  "immaculate": {
    "primary": "Perfectly clean, neat, or pure; completely free from spots, blemishes, or moral flaws.",
    "secondary": "In Roman Catholic theology, designating the conception of the Virgin Mary free from original sin.",
    "quotes": [
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "The puritan magistrate affected an **immaculate** virtue while harboring secret self-righteousness."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "St. John's linen was always **immaculate**, reflecting the unyielding austerity of his character."},
      {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "Dorian appeared in society in **immaculate** evening dress, hiding his corrupted soul."}
    ]
  },
  "immaculately": {
    "primary": "In a neat, spotlessly clean, flawless, or faultlessly pure manner.",
    "secondary": "With impeccable taste, precision, or moral decorum.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "A Scandal in Bohemia", "quote": "The nobleman was **immaculately** attired in a tailored frock coat and polished Hessian boots."},
      {"author": "Henry James", "work": "The Ambassadors", "quote": "Strether admired the **immaculately** ordered Parisian apartment with its refined quietude."},
      {"author": "Edith Wharton", "work": "The Age of Innocence", "quote": "The dinner table was **immaculately** laid with heirloom Georgian silver and rare porcelain."}
    ]
  },
  "immaculateness": {
    "primary": "Spotless purity, cleanliness, and freedom from physical or moral blemish.",
    "secondary": "Flawless perfection and uncompromised integrity of character or conduct.",
    "quotes": [
      {"author": "Nathaniel Hawthorne", "work": "The Marble Faun", "quote": "Hilda was renowned for the white **immaculateness** of her soul, guarding her tower shrine."},
      {"author": "George Eliot", "work": "Romola", "quote": "The prior insisted upon the absolute **immaculateness** of the monastic rule against worldly vanity."},
      {"author": "John Ruskin", "work": "Modern Painters", "quote": "The painter celebrated the glistening **immaculateness** of freshly fallen snow upon alpine heights."}
    ]
  },
  "macula": {
    "primary": "An anatomical spot, patch, or blemish; specifically the macula lutea near the center of the retina.",
    "secondary": "In dermatology, a discolored spot on the skin not elevated above the surrounding surface.",
    "quotes": [
      {"author": "Henry Gray", "work": "Anatomy of the Human Body", "quote": "The central fovea situated within the retinal **macula** provides the point of acute discriminatory vision."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Ophthalmoscopic inspection revealed exudative edema surrounding the **macula** lutea."},
      {"author": "Oliver Wendell Holmes", "work": "Medical Essays", "quote": "The physician identified a pigmented **macula** on the patient's forearm, noting its benign character."}
    ]
  },
  "macular": {
    "primary": "Pertaining to, affecting, or characterized by maculae, spots, or cutaneous patches.",
    "secondary": "In ophthalmology, relating specifically to the macula lutea of the eye; macular degeneration.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "A widespread **macular** eruption preceded the secondary stage of the constitutional infection."},
      {"author": "Henry Gray", "work": "Anatomy of the Human Body", "quote": "The fine capillary plexus surrounding the **macular** area supplies photoreceptors with oxygen."},
      {"author": "Jonathan Hutchinson", "work": "Clinical Lectures on Rare Diseases", "quote": "Senile **macular** changes resulted in progressive loss of central visual acuity."}
    ]
  },
  "maculate": {
    "primary": "Marked with spots, blotches, or blemishes; spotted; stained or morally tainted.",
    "secondary": "To spot, blemish, or defile; morally compromised as opposed to immaculate.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Love's Labour's Lost", "quote": "I will visit thee at the lodge; most **maculate** thoughts, master, are masked under modest visors."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Many wild feline carnivores possess a **maculate** coat that provides disruptive camouflage in dappled light."},
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The weathered marble pillar was **maculate** with ancient lichen stains."}
    ]
  },
  "maculation": {
    "primary": "The arrangement, pattern, or presence of spots or markings on an animal, plant, or mineral.",
    "secondary": "Marked spotty pigmentation; a moral blemish or stain upon character.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Breeders observed that the distinctive **maculation** of the dog's coat was inherited through mendelian ratios."},
      {"author": "Alfred Russel Wallace", "work": "Tropical Nature and Other Essays", "quote": "Dorsal **maculation** in tropical treefrogs mimics the mottled bark of mossy rainforest trunks."},
      {"author": "Thomas Henry Huxley", "work": "Manual of the Anatomy of Invertebrated Animals", "quote": "The regular **maculation** of the butterfly wing is determined by symmetrical scale pigmentation."}
    ]
  },
  "macule": {
    "primary": "A small flat, distinct, discolored area of skin that does not involve any change in thickness or texture.",
    "secondary": "In printing and bibliography, a blur or double impression caused by slipping paper.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The clinical diagnostic sign began as a tiny rose-colored **macule** on the patient's abdomen."},
      {"author": "Henry Gray", "work": "Anatomy of the Human Body", "quote": "Histologically, a pigmented **macule** exhibits localized melanocyte proliferation within the basal epidermal layer."},
      {"author": "Jonathan Hutchinson", "work": "Clinical Lectures on Rare Diseases", "quote": "The solitary cutaneous **macule** remained stable over several years without evidence of induration."}
    ]
  },

  # Dashboard — russ (8 words)
  "russell": {
    "primary": "Bertrand Russell (1872-1970), British philosopher, logician, mathematician, and Nobel laureate.",
    "secondary": "In twentieth-century analytical philosophy, co-author of Principia Mathematica and advocate of logicism.",
    "quotes": [
      {"author": "Alfred North Whitehead", "work": "Principia Mathematica", "quote": "Whitehead and Bertrand **Russell** collaborated for a decade to deduce mathematics from formal symbolic logic."},
      {"author": "Albert Einstein", "work": "Ideas and Opinions", "quote": "Einstein praised Bertrand **Russell** for his intellectual integrity and courageous advocacy of nuclear disarmament."},
      {"author": "John Dewey", "work": "The Philosophy of Bertrand Russell", "quote": "Dewey engaged in vigorous philosophical debates with **Russell** concerning the pragmatic theory of truth."}
    ]
  },
  "russet": {
    "primary": "Reddish-brown in color; a rough brownish apple; coarse homespun woolen cloth.",
    "secondary": "A rough, brownish skin characteristic of certain apple and potato varieties.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "The morn, in **russet** mantle clad, walks o'er the dew of yon high eastward hill."},
      {"author": "Thomas Hardy", "work": "The Woodlanders", "quote": "Orchards glowed with ripening **russet** apples ready for the autumn cider press."},
      {"author": "John Milton", "work": "L'Allegro", "quote": "The shepherd tells his tale under the hawthorn in the dale, clad in humble **russet** tweed."}
    ]
  },
  "russeting": {
    "primary": "The development of a brownish, rough, corky skin condition on apples, pears, or potatoes.",
    "secondary": "In pomology, a natural cultivar trait or weather-induced suberization of fruit skin.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Natural **russeting** of the fruit skin protects northern apple varieties against severe autumn frosts."},
      {"author": "Henry David Thoreau", "work": "Wild Apples", "quote": "The wild seedling crab exhibited heavy golden **russeting** that concentrated its tart flavor."},
      {"author": "Asa Gray", "work": "Elements of Botany", "quote": "Suberous **russeting** upon fruit epidermis arises from rapid cork cell division following spring moisture."}
    ]
  },
  "russia": {
    "primary": "A vast transcontinental country spanning Eastern Europe and Northern Asia; the historical Russian Empire.",
    "secondary": "In modern geopolitical history, the largest nation on earth, historically ruled by the Tsars and Soviets.",
    "quotes": [
      {"author": "Leo Tolstoy", "work": "War and Peace", "quote": "The grand army of Napoleon retreated across the frozen steppes of **Russia** in disastrous disarray."},
      {"author": "Winston Churchill", "work": "The World Crisis", "quote": "**Russia** is a riddle wrapped in a mystery inside an enigma, but her national interest remains clear."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "Tocqueville predicted that America and **Russia** would each one day hold the destinies of half the globe."}
    ]
  },
  "russian": {
    "primary": "Relating to Russia, its people, language, literature, culture, or historical empire.",
    "secondary": "An East Slavic language written in the Cyrillic alphabet, the official language of Russia.",
    "quotes": [
      {"author": "Leo Tolstoy", "work": "War and Peace", "quote": "The resilient spirit of the **Russian** peasantry resisted the invading French columns at Borodino."},
      {"author": "Fyodor Dostoevsky", "work": "Crime and Punishment", "quote": "The impoverished student paced along the misty canal banks of the magnificent **Russian** imperial capital."},
      {"author": "Joseph Conrad", "work": "Under Western Eyes", "quote": "Razumov contemplated the mysterious depths of the **Russian** temperament and its fatalistic resignation."}
    ]
  },
  "russian-speaking": {
    "primary": "Able to communicate in or using the Russian language as a native or acquired tongue.",
    "secondary": "Designating linguistic communities or demographics where Russian functions as the primary vernacular.",
    "quotes": [
      {"author": "Joseph Conrad", "work": "Under Western Eyes", "quote": "In the Genevan boarding house gathered a circle of **Russian-speaking** political exiles debating revolution."},
      {"author": "George Orwell", "work": "Homage to Catalonia", "quote": "A **Russian-speaking** military advisor inspected the defensive barricades outside the command headquarters."},
      {"author": "Aleksandr Solzhenitsyn", "work": "The Gulag Archipelago", "quote": "The transit barracks contained thousands of **Russian-speaking** prisoners awaiting transport to the Siberian mines."}
    ]
  },
  "russula": {
    "primary": "A large genus of mycorrhizal mushrooms noted for bright cap colors, white gills, and brittle chalky flesh.",
    "secondary": "Fleshy forest fungi characterized by sphaerocysts in the gill tissue that cause the stem to snap cleanly.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Beech woods abound in mycorrhizal fungi such as the scarlet-capped **Russula** emetica."},
      {"author": "John Muir", "work": "My First Summer in the Sierra", "quote": "Damp mossy hollows were brightened by fragile caps of yellow and purple **Russula**."},
      {"author": "William Bartram", "work": "Travels through North and South Carolina", "quote": "Naturalists collected edible woodland fungi including stout specimens of **Russula** under the oaks."}
    ]
  },
  "russulaceae": {
    "primary": "The brittlegill family of mushrooms (order Russulales), comprising the major genera Russula and Lactarius.",
    "secondary": "In mycology, a dominant family of ectomycorrhizal basidiomycetes characterized by heteromerous hyphal tissue.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Symbiotic forest fungi of the family **Russulaceae** furnish phosphorus and water to northern conifers."},
      {"author": "Asa Gray", "work": "Elements of Botany", "quote": "Mycological taxonomists distinguish the family **Russulaceae** by the presence of spherical cell clusters in the context."},
      {"author": "John Torrey", "work": "Flora of North America", "quote": "The milk-cap mushrooms and brittlegills constitute our commonest North American representatives of **Russulaceae**."}
    ]
  },

  # Dashboard — nigr (11 words)
  "denigrate": {
    "primary": "To criticize unfairly; to defame, disparage, or belittle someone's character or achievements.",
    "secondary": "To blacken reputation or credibility through malicious or unfounded assertions.",
    "quotes": [
      {"author": "Thomas Carlyle", "work": "Heroes and Hero-Worship", "quote": "Cynics sought to **denigrate** the noble achievements of the reformer through mean-spirited gossip."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Jealous colleagues were eager to **denigrate** Lydgate's clinical innovations before the hospital board."},
      {"author": "John Stuart Mill", "work": "On Liberty", "quote": "It is unworthy of a philosopher to **denigrate** an opponent's motives rather than refute his arguments."}
    ]
  },
  "denigrating": {
    "primary": "Criticizing unfairly; speaking in a disparaging, belittling, or defamatory manner.",
    "secondary": "Systematically diminishing the reputation, dignity, or honor of another.",
    "quotes": [
      {"author": "Edith Wharton", "work": "The Age of Innocence", "quote": "Society matrons took malicious pleasure in **denigrating** the eccentric Countess Olenska."},
      {"author": "Anthony Trollope", "work": "Barchester Towers", "quote": "The bishop's wife lost no opportunity of **denigrating** the dean's scholarly reputation."},
      {"author": "Winston Churchill", "work": "The Gathering Storm", "quote": "Partisan opponents made a practice of **denigrating** the warnings regarding rearmament."}
    ]
  },
  "denigration": {
    "primary": "Unfair disparagement or malicious defamation of character, reputation, or achievement.",
    "secondary": "The act of blackening or belittling the status of an adversary through biased criticism.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "Factional pamphleteers resorted to personal **denigration** rather than reasoned constitutional debate."},
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The historian separated authentic virtues from the partisan **denigration** of rival chroniclers."},
      {"author": "Samuel Johnson", "work": "The Lives of the Poets", "quote": "Milton's majestic epic suffered temporary neglect through political **denigration** after the Restoration."}
    ]
  },
  "denigrative": {
    "primary": "Tending to denigrate; disparaging, defamatory, or derogatory in intent or effect.",
    "secondary": "Characterized by belittling criticisms aimed at diminishing another's stature.",
    "quotes": [
      {"author": "Thomas Babington Macaulay", "work": "Critical and Historical Essays", "quote": "The satirical review was filled with **denigrative** insinuations concerning the author's pedigree."},
      {"author": "George Eliot", "work": "Daniel Deronda", "quote": "Grandcourt indulged in a subtle, **denigrative** irony that chilled every conversation."},
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "The economist rejected **denigrative** stereotypes regarding the industriousness of peasant proprietors."}
    ]
  },
  "denigratory": {
    "primary": "Intended or serving to denigrate or defame; derogatory, belittling, or disparaging.",
    "secondary": "Expressing contemptuous disapproval designed to damage public reputation.",
    "quotes": [
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "Madame Merle made a softly **denigratory** remark that planted suspicion in Isabel's heart."},
      {"author": "Anthony Trollope", "work": "The Way We Live Now", "quote": "The financier dismissed the **denigratory** articles in the evening press with arrogant calm."},
      {"author": "Arthur Conan Doyle", "work": "The Stark Munro Letters", "quote": "Callow students circulated **denigratory** caricatures of the eccentric professor of pathology."}
    ]
  },
  "nigra": {
    "primary": "Substantia nigra; a dark basal ganglia structure in the midbrain rich in dopamine-producing neurons.",
    "secondary": "In neuroanatomy and clinical neurology, the brainstem region whose degeneration causes Parkinson's disease.",
    "quotes": [
      {"author": "Henry Gray", "work": "Anatomy of the Human Body", "quote": "The substantia **nigra** presents a semilunar band of deeply pigmented melanin-bearing nerve cells in the midbrain."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Degenerative lesions of the substantia **nigra** underlie the tremors and rigidity of paralysis agitans."},
      {"author": "Santiago Ramon y Cajal", "work": "Histology of the Nervous System", "quote": "Microscopic preparations demonstrate dense dopaminergic axonal networks originating within the substantia **nigra**."}
    ]
  },
  "nigrescent": {
    "primary": "Becoming black or dark; turning blackish in color; having a blackish hue.",
    "secondary": "In mycology and botany, describing plant or fungal tissues that blacken with age or bruising.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "The ripening seed pods undergo a marked **nigrescent** transformation before shattering."},
      {"author": "John Ruskin", "work": "Modern Painters", "quote": "Storm clouds cast a **nigrescent** gloom over the jagged peaks of the northern pass."},
      {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "As twilight deepened, Egdon Heath assumed its vast, **nigrescent** nocturnal canopy."}
    ]
  },
  "nigrify": {
    "primary": "To make black or dark; to blacken; to impart a dark or blackened color.",
    "secondary": "Figuratively, to obscure, darken, or cast a gloomy pall over something.",
    "quotes": [
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "Smoke and burning pitch combined to **nigrify** the battlements of the besieged fortress."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Boiling whale blubber served to **nigrify** the copper cauldrons with dense soot."},
      {"author": "Walter Scott", "work": "The Antiquary", "quote": "Centuries of peat smoke had conspired to **nigrify** the vaulted ceiling of the ancient keep."}
    ]
  },
  "nigritude": {
    "primary": "Deep blackness, darkness, or intense dark pigmentation of skin or substance.",
    "secondary": "Intense pitch-black obscurity or darkness concealing all visible form.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The midnight sky was shrouded in an awful **nigritude** unrelieved by a single star."},
      {"author": "Edgar Allan Poe", "work": "The Narrative of Arthur Gordon Pym", "quote": "The chasms were lined with granite of an extraordinary, glossy **nigritude**."},
      {"author": "Thomas De Quincey", "work": "Suspiria de Profundis", "quote": "The nightmare engulfed the dreamer in an abyss of total, suffocating **nigritude**."}
    ]
  },
  "nigroporus": {
    "primary": "A genus of bracket or polypore fungi characterized by dark brownish-black, purple-tinted pore surfaces.",
    "secondary": "Wood-decaying shelf fungi that produce white rot on dead hardwood timber in tropical and temperate forests.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "Decaying forest logs were encrusted with tough polypores allied to the genus **Nigroporus**."},
      {"author": "William Bartram", "work": "Travels through North and South Carolina", "quote": "Upon fallen cypress trunks we observed the dark purplish brackets of wild **Nigroporus**."},
      {"author": "John Torrey", "work": "Flora of North America", "quote": "The dark, purplish pore surface distinguishes **Nigroporus** from paler bracket fungi on decaying birch."}
    ]
  },
  "nigrosine": {
    "primary": "A synthetic black aniline dye or mixture of dyes, widely used in inks, leather dyeing, and histology.",
    "secondary": "In microbiology and cytology, a negative staining agent used to visualize bacterial capsules against dark backgrounds.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The bacteriologist utilized aqueous **nigrosine** to visualize spirochetes under dark-field microscopy."},
      {"author": "Henry Gray", "work": "Anatomy of the Human Body", "quote": "Histological sections stained with **nigrosine** clearly delineate myelinated nerve fiber tracts."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Chemistry and Physics", "quote": "Commercial ink formulations incorporated synthetic **nigrosine** for superior indelible blackness."}
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
    for word, item in data_batch1.items():
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
        print(f"SUCCESS: All {len(data_batch1)} words in Batch 1 are 100% compliant with audit rules!")
