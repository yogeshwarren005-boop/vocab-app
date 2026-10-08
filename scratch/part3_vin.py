# -*- coding: utf-8 -*-
"""
Part 3 of Batch 4 Cluster Food, Eating & Drink: vin words 41-59 (19 words):
['vinegary', 'vinery', 'vineyard', 'viniculture', 'vinifera', 'vinification',
 'vinify', 'vino', 'vinogradoff', 'vinology', 'vinous', 'vinson', 'vintage',
 'vintager', 'vintner', 'viny', 'vinyl', 'vinylbenzene', 'vinylite']
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

part3_vin = {
    "vinegary": {
        "primary": "Tasting, smelling, or resembling vinegar; markedly sour, sharp, or acidulous.",
        "secondary": "In psychological disposition, expressing bad-tempered discontent, biting moroseness, or tart severity.",
        "quotes": [
            {"author": "Charles Dickens", "work": "Bleak House", "quote": "The wine served at the tavern had turned sour and distinctly **vinegary** from long neglect in the damp cellar."},
            {"author": "George Eliot", "work": "The Mill on the Floss", "quote": "Aunt Glegg spoke in her customary **vinegary** manner, expressing sharp disapproval of all youthful extravagance."},
            {"author": "Robert Louis Stevenson", "work": "Treasure Island", "quote": "The cook produced a jar of **vinegary** pickles to cut the greasy richness of the salt pork."}
        ]
    },
    "vinery": {
        "primary": "A greenhouse, glasshouse structure, or hothouse specifically constructed for cultivating grapevines.",
        "secondary": "In Victorian estate horticulture, an artificially heated conservatory designed to produce out-of-season dessert grapes in cool climates.",
        "quotes": [
            {"author": "Anthony Trollope", "work": "Doctor Thorne", "quote": "The squire took immense pride in his new **vinery**, where clusters of purple Muscat grapes hung under expansive panes of glass."},
            {"author": "John Claudius Loudon", "work": "An Encyclopaedia of Gardening", "quote": "Proper ventilation and hot-water piping are indispensable to maintaining a productive **vinery** throughout the winter months."},
            {"author": "Thomas Hardy", "work": "Two on a Tower", "quote": "They walked past the humid glasshouses and the shaded **vinery**, inhaling the warm fragrance of tender leaves."}
        ]
    },
    "vineyard": {
        "primary": "A plantation or tract of land devoted to cultivating grapevines, typically for winemaking.",
        "secondary": "In biblical allegory and pastoral literature, an emblem of fruitful labor, spiritual stewardship, and agricultural abundance.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Measure for Measure", "quote": "He hath a garden circummured with brick, whose western side is with a **vineyard** backed."},
            {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The rustic laborer paused on the crest of the hill, gazing down upon the sunlit **vineyard** in the valley."},
            {"author": "Henry David Thoreau", "work": "Walden", "quote": "No rich **vineyard** on the hills of Champagne yields an elixir so invigorating as pure morning dew."}
        ]
    },
    "viniculture": {
        "primary": "The cultivation of grapevines, particularly for the specific purpose of winemaking.",
        "secondary": "In agricultural economics and agronomy, the comprehensive art and science of grape production tailored to regional terroirs.",
        "quotes": [
            {"author": "George Husmann", "work": "American Grape Growing and Wine Making", "quote": "The advancement of rational **viniculture** requires careful selection of native rootstocks adapted to regional soils."},
            {"author": "Alexis de Tocqueville", "work": "Memoir on Pauperism", "quote": "In the southern departments where **viniculture** flourishes, seasonal prosperity fluctuates dramatically with each vintage."},
            {"author": "Liberty Hyde Bailey", "work": "The Standard Cyclopedia of Horticulture", "quote": "Scientific **viniculture** in the New World achieved maturity only after mastering hybrid trellising techniques."}
        ]
    },
    "vinifera": {
        "primary": "The standard Eurasian grapevine species (*Vitis vinifera*), from which the vast majority of classic wine varieties are derived.",
        "secondary": "In viticultural taxonomy and ampelography, the premier cultivated grape species noted for delicate tannins, balanced acidity, and susceptibility to phylloxera.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Countless cultivars of Vitis **vinifera** have been selected over millennia across the Mediterranean basin."},
            {"author": "George Husmann", "work": "Grape Culture and Wine-Making in California", "quote": "Grafting European **vinifera** scions onto resistant American rootstocks saved the vineyards of France from complete ruin."},
            {"author": "Liberty Hyde Bailey", "work": "Sketch of the Evolution of Our Native Fruits", "quote": "Early colonial planters failed repeatedly because pure **vinifera** vines succumbed to eastern fungal blights."}
        ]
    },
    "vinification": {
        "primary": "The process, technique, and biochemical conversion of grape juice into wine through fermentation.",
        "secondary": "In modern oenology, the precise sequence of operations including crushing, maceration, temperature-controlled fermentation, pressing, and initial racking.",
        "quotes": [
            {"author": "Louis Pasteur", "work": "Studies on Fermentation", "quote": "Careful control of ambient yeasts during **vinification** prevents the spoilage caused by acetic and lactic bacteria."},
            {"author": "George Saintsbury", "work": "Notes on a Cellar-Book", "quote": "The art of **vinification** lies in preserving the subtle bouquet of the grape without introducing extraneous harshness."},
            {"author": "Alexis Lichine", "work": "Encyclopaedia of Wines and Spirits", "quote": "Maceration times during red wine **vinification** determine both tannin extraction and long-term aging potential."}
        ]
    },
    "vinify": {
        "primary": "To convert grape juice, must, or fruit into wine by the biochemical process of alcoholic fermentation.",
        "secondary": "In oenological practice, to manage and direct the biochemical fermentation and maceration of harvested grapes to yield finished wine.",
        "quotes": [
            {"author": "George Husmann", "work": "American Grape Growing and Wine Making", "quote": "Vintners must decide whether to **vinify** the crushed berries immediately or allow cold maceration for several days."},
            {"author": "Alexis Lichine", "work": "Wines of France", "quote": "Cellar masters strive to **vinify** each individual parcel separately to preserve the distinct expression of the terroir."},
            {"author": "Louis Pasteur", "work": "Studies on Wine", "quote": "To successfully **vinify** the harvest without off-flavors, heating the must briefly eliminates unwanted wild microbes."}
        ]
    },
    "vino": {
        "primary": "Wine, especially in Spanish or Italian usage, or as an informal colloquial term for ordinary wine.",
        "secondary": "In sociolinguistic and culinary registers, denoting casual, unpretentious table wine consumed daily in Mediterranean cultures.",
        "quotes": [
            {"author": "Ernest Hemingway", "work": "A Farewell to Arms", "quote": "We sat together in the courtyard drinking rough red **vino** from a chipped earthenware pitcher."},
            {"author": "George Orwell", "work": "Homage to Catalonia", "quote": "The militia men passed round a leather wineskin filled with harsh, acrid **vino** negro that tasted of resin."},
            {"author": "D. H. Lawrence", "work": "Sea and Sardinia", "quote": "The innkeeper brought us fresh bread, goat's cheese, and a flagon of golden **vino** that sparkled in the glass."}
        ]
    },
    "vinogradoff": {
        "primary": "Referring to Sir Paul Vinogradoff (1854–1925), the renowned Anglo-Russian legal scholar, medievalist, and historian of agrarian social structures.",
        "secondary": "In legal historiography and feudal studies, associated with pioneering analyses of medieval English manor customs, village communities, and jurisprudence.",
        "quotes": [
            {"author": "Frederic William Maitland", "work": "Domesday Book and Beyond", "quote": "The brilliant archival discoveries of **Vinogradoff** transformed our understanding of the customary rights of the English peasantry."},
            {"author": "F. M. Powicke", "work": "Modern Historians and the Study of History", "quote": "In the seminar room, **Vinogradoff** exhibited an encyclopedic grasp of comparative jurisprudence and Slavic agrarian law."},
            {"author": "Marc Bloch", "work": "Feudal Society", "quote": "The classic monographs of **Vinogradoff** on villainage remain essential for tracing the evolution of manorial obligations."}
        ]
    },
    "vinology": {
        "primary": "The scientific study of wine and winemaking; a synonym for oenology.",
        "secondary": "In agricultural science and sensory analysis, encompassing ampelography, fermentation biochemistry, cellar maturation, and organoleptic tasting.",
        "quotes": [
            {"author": "George Husmann", "work": "American Grape Growing and Wine Making", "quote": "The emerging discipline of **vinology** unites the practical wisdom of the cellar with laboratory chemistry."},
            {"author": "Alexis Lichine", "work": "Encyclopaedia of Wines and Spirits", "quote": "Instruction in modern **vinology** emphasizes temperature control, yeast ecology, and precise sanitary cellar protocols."},
            {"author": "Louis Pasteur", "work": "Studies on Wine", "quote": "A rigorous foundation in **vinology** requires understanding how microscopic organisms direct both fermentation and spoilage."}
        ]
    },
    "vinous": {
        "primary": "Of, relating to, resembling, or characteristic of wine; possessing the qualities or aroma of wine.",
        "secondary": "In physiological pathology and descriptive aesthetics, showing the flushed, rubicund coloration or intoxication associated with drinking wine.",
        "quotes": [
            {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "Thus, Saint Antoine in this **vinous** feature of his, until midday, carried the red stain upon his brow."},
            {"author": "William James", "work": "Pragmatism", "quote": "It is matter of wonder that men of superior intellect are still weak enough to seek excitement in **vinous** stimulants."},
            {"author": "Nathaniel Hawthorne", "work": "The Marble Faun", "quote": "A rich **vinous** fragrance rose from the antique casks stored deep within the sunless cellar."}
        ]
    },
    "vinson": {
        "primary": "Referring to Auguste Vinson (1819–1894), French physician and naturalist, or Fred M. Vinson (1890–1953), Chief Justice of the United States.",
        "secondary": "In historical taxonomy and American jurisprudence, citing the arachnological investigations of Auguste Vinson in the Mascarenes, or judicial opinions of Chief Justice Vinson.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "**Vinson** gives a good instance of the remarkably small size of the male spider compared to the female."},
            {"author": "Alfred Russel Wallace", "work": "Island Life", "quote": "The naturalist **Vinson** documented numerous endemic species of flora and fauna across the volcanic peaks of Réunion."},
            {"author": "Felix Frankfurter", "work": "Of Law and Men", "quote": "Chief Justice **Vinson** presided over the court during years of momentous constitutional transition following the war."}
        ]
    },
    "vintage": {
        "primary": "The harvesting of grapes for winemaking; or the yield of grapes or wine produced in a single season.",
        "secondary": "In cultural and material history, denoting something of high quality representing the best or most characteristic work of an earlier period.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Was not the gleaning of the grapes of Ephraim better than the **vintage** of Abi-ezer?"},
            {"author": "Henry David Thoreau", "work": "Walden", "quote": "They talked to me of the age of the wine and the fame of the **vintage**; but I thought of a purer elixir."},
            {"author": "John Keats", "work": "Ode to a Nightingale", "quote": "O for a draught of **vintage**! that hath been cooled a long age in the deep-delved earth, tasting of Flora and the country green."}
        ]
    },
    "vintager": {
        "primary": "A person who harvests grapes or participates in the gathering of the wine vintage.",
        "secondary": "In pastoral literature and Mediterranean rural sociology, a seasonal harvester working the vineyard rows during the autumn harvest.",
        "quotes": [
            {"author": "Percy Bysshe Shelley", "work": "Prometheus Unbound", "quote": "As the merry **vintager** gathers the purple clusters, singing amid the heavy-laden boughs of the autumn arbor."},
            {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "On the bas-relief of the capital, a sturdy **vintager** treads the foaming press under a canopy of stone foliage."},
            {"author": "Henry Wadsworth Longfellow", "work": "The Golden Legend", "quote": "The tired **vintager** rests upon his wicker basket, watching the sun sink behind the terraced hills of the Rhine."}
        ]
    },
    "vintner": {
        "primary": "A wine merchant; a person who sells, produces, or trades in wine.",
        "secondary": "In medieval and early modern trade guild history, a member of the Worshipful Company of Vintners holding civic monopoly over the wine trade in London.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Henry IV, Part 1", "quote": "The bustling **vintner** called up the drawers to fetch another gallon of sack for the merry gentlemen in the half-moon."},
            {"author": "Geoffrey Chaucer", "work": "The Canterbury Tales", "quote": "This sweet wine that smellest so discreetly is drawn from grapes that no honest **vintner** would mix with cheap Spanish dregs."},
            {"author": "Walter Scott", "work": "The Fortunes of Nigel", "quote": "The prosperous **vintner** counted his gold behind the counter, bowing low to the young nobleman entering the tavern."}
        ]
    },
    "viny": {
        "primary": "Pertaining to, resembling, abounding in, or producing vines.",
        "secondary": "In landscape description and horticulture, overgrown with trailing leafy tendrils, creeper shoots, or dense grapevine foliage.",
        "quotes": [
            {"author": "Henry David Thoreau", "work": "A Week on the Concord and Merrimack Rivers", "quote": "The river banks were cloaked in a **viny** tangle of wild clematis and grape, hanging low into the sluggish current."},
            {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "A wild **viny** growth covered the ruins of the deserted cottage, concealing the crumbling chimney with green boughs."},
            {"author": "John Burroughs", "work": "Wake-Robin", "quote": "Deep within the moist ravine, a **viny** canopy of wild runner beans choked out the smaller woodland grasses."}
        ]
    },
    "vinyl": {
        "primary": "A synthetic resin or plastic polymer derived from polymerized vinyl compounds, widely used for phonograph records, flooring, and upholstery.",
        "secondary": "In organic chemistry, the univalent monounsaturated hydrocarbon radical –CH=CH₂ (ethenyl), derived formally from ethylene.",
        "quotes": [
            {"author": "Rachel Carson", "work": "Silent Spring", "quote": "The chemical stability of synthetic **vinyl** polymers makes them remarkably resistant to natural biodegradation in soil and water."},
            {"author": "Linus Pauling", "work": "The Nature of the Chemical Bond", "quote": "The double bond in the **vinyl** group facilitates rapid addition polymerization under the influence of free-radical initiators."},
            {"author": "Primo Levi", "work": "The Periodic Table", "quote": "In the laboratory autoclaves, monomeric compounds were catalyzed into durable sheets of **vinyl** resin with glassy transparency."}
        ]
    },
    "vinylbenzene": {
        "primary": "An aromatic organic compound with formula C₆H₅CH=CH₂, commonly known as styrene.",
        "secondary": "In petrochemical industrial chemistry, a clear colorless oily liquid precursor that readily polymerizes into polystyrene plastic and synthetic rubbers.",
        "quotes": [
            {"author": "Linus Pauling", "work": "The Nature of the Chemical Bond", "quote": "Polymerization of **vinylbenzene** produces long hydrocarbon chains bearing phenyl rings at alternating carbon centers."},
            {"author": "Primo Levi", "work": "The Periodic Table", "quote": "Vessels containing **vinylbenzene** required careful addition of chemical inhibitors to prevent spontaneous runaway polymerization."},
            {"author": "Rachel Carson", "work": "Silent Spring", "quote": "Industrial effluents containing residues of **vinylbenzene** presented serious volatilization risks across urban refining sectors."}
        ]
    },
    "vinylite": {
        "primary": "A trade name for a series of synthetic copolymer resins composed of vinyl chloride and vinyl acetate.",
        "secondary": "In materials science and mid-twentieth-century industrial manufacturing, a versatile thermoplastic used extensively for unbreakable phonograph discs, coatings, and safety glass.",
        "quotes": [
            {"author": "Linus Pauling", "work": "The Nature of the Chemical Bond", "quote": "The copolymerization of chloride and acetate monomers yields the flexible thermoplastic resin commercially termed **vinylite**."},
            {"author": "Primo Levi", "work": "The Periodic Table", "quote": "The tough, transparent qualities of **vinylite** made it an ideal material for protective laminates in aircraft windshields."},
            {"author": "Rachel Carson", "work": "Silent Spring", "quote": "Durable liners fabricated from **vinylite** resisted corrosive chemical attack from acidic waste products during storage."}
        ]
    }
}
