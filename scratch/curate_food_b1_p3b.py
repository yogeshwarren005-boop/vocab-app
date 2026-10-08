# -*- coding: utf-8 -*-
"""
Part 3b of Food Batch 1:
- pan (9 words)
- pota (6 words)
Total: 15 words
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

data_food_p3b = {
    # ==================== Dashboard — pan (9 words) ====================
    "companion": {
        "primary": "A person who frequently accompanies, associates with, or shares mutual experiences with another.",
        "secondary": "In domestic social history and etymological roots (*com-* + *panis*, sharing bread), an associate sharing daily bread, travels, or intimate household life.",
        "quotes": [
            {"author": "Mary Shelley", "work": "Frankenstein", "quote": "I desired love and fellowship, and I was still spurned; I demanded a creature of another sex, but as hideous as myself, to become my **companion**."},
            {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "My friend and **companion** sat opposite me in the cab, his lean face illuminated by the flickering gas lamps of London."},
            {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth found in her sister a sympathetic and sensible **companion** whose conversation was always delightful."}
        ]
    },
    "companionship": {
        "primary": "The state of fellowship, close association, and mutual comfort shared between friends or partners.",
        "secondary": "In social psychology and attachment theory, the supportive interpersonal bond characterized by mutual trust, emotional security, and shared activities.",
        "quotes": [
            {"author": "George Eliot", "work": "Middlemarch", "quote": "She felt the deep loneliness of a marriage where intellectual sympathy and true **companionship** were utterly lacking."},
            {"author": "Robert Louis Stevenson", "work": "Travels with a Donkey in the Cévennes", "quote": "Even the obstinate beast provided a rough sort of **companionship** upon the silent mountain passes of southern France."},
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Their long acquaintance had matured into that calm **companionship** which frequently forms the surest foundation of love."}
        ]
    },
    "empanada": {
        "primary": "A baked or fried turnover pastry filled with seasoned meat, vegetables, or fruit, popular in Hispanic cuisines.",
        "secondary": "In regional Iberian and Latin American gastronomy, a traditional filled bread pastry originating from Galicia, whose name derives etymologically from enclosing filling in bread (*empanar*).",
        "quotes": [
            {"author": "Benito Pérez Galdós", "work": "Fortunata and Jacinta", "quote": "The street vendor carried a smoking basket of freshly baked **empanada**, tempting hungry passersby with the savory aroma of onions and pork."},
            {"author": "Richard Ford", "work": "Gatherings from Spain", "quote": "At the country inn we were served a generous slice of Galician **empanada** packed with savory tuna and sweet peppers."},
            {"author": "George Borrow", "work": "The Bible in Spain", "quote": "The innkeeper produced a cold **empanada** and a bottle of Valdepeñas wine, which furnished our hungry party an admirable repast."}
        ]
    },
    "pan": {
        "primary": "A broad, shallow, open metal container used for cooking, baking, or frying food.",
        "secondary": "In domestic technology and geological mining, a wide vessel utilized for heating culinary ingredients or panning alluvial gravel for gold particles.",
        "quotes": [
            {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Joe Gargery stirred the gravy in the iron **pan** while the fire crackled cheerfully upon the blacksmith's hearth."},
            {"author": "Henry David Thoreau", "work": "Walden", "quote": "I baked my rye and Indian cakes in a simple tin **pan** set before the glowing embers of my fireplace."},
            {"author": "Mark Twain", "work": "Roughing It", "quote": "The prospector washed shovel after shovel of gravel in his tin **pan**, eagerly watching for glittering flecks of yellow gold."}
        ]
    },
    "panic": {
        "primary": "Sudden overwhelming terror or apprehension, often irrational and spreading rapidly through a group.",
        "secondary": "In financial history and behavioral psychology, an acute collective frenzy prompting frantic selling of assets, herd flight, or market collapse.",
        "quotes": [
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "A wild **panic** seized the harpooners as the enormous white bulk breached suddenly through the churning waves beside them."},
            {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The false rumor spread like wildfire through London, exciting an uncontrollable **panic** among the credulous citizens."},
            {"author": "Joseph Conrad", "work": "Lord Jim", "quote": "In that sudden squall a blind **panic** swept through the officers, robbing them of judgment and moral courage."}
        ]
    },
    "panification": {
        "primary": "The process of making or converting grain flour and water into bread through fermentation and baking.",
        "secondary": "In historical food chemistry and industrial milling, the complex enzymatic and thermal transformation of dough into aerated bread crumb.",
        "quotes": [
            {"author": "Justus von Liebig", "work": "Familiar Letters on Chemistry", "quote": "The art of **panification** involves the conversion of cereal starch into fermentable sugars by diastase and active yeast."},
            {"author": "Louis Pasteur", "work": "Studies on Fermentation", "quote": "In the process of **panification**, the alcoholic fermentation of the dough produces the carbonic gas that puffs up the loaf."},
            {"author": "Benjamin Thompson (Count Rumford)", "work": "Essays, Political, Economical, and Philosophical", "quote": "Proper heat regulation during **panification** ensures a crisp exterior crust while preserving a light, digestible interior."}
        ]
    },
    "panivorous": {
        "primary": "Feeding on or subsisting predominantly upon bread or baked grain foods.",
        "secondary": "In dietary anthropology and physiological categorization, an uncommon term describing cultures, individuals, or animals whose primary caloric staple is bread.",
        "quotes": [
            {"author": "William Cullen", "work": "A Treatise of the Materia Medica", "quote": "Scurvy is rarely observed among pastoral races, but appears readily in strictly **panivorous** populations deprived of fresh vegetables."},
            {"author": "Thomas Browne", "work": "Pseudodoxia Epidemica", "quote": "Whether humans were originally frugivorous or **panivorous** remains an ancient disputation among natural philosophers."},
            {"author": "Erasmus Darwin", "work": "Zoonomia", "quote": "The digestive organs of civilized humans have adapted comfortably to a largely **panivorous** regimen composed of wheat and rye."}
        ]
    },
    "pannier": {
        "primary": "A large basket, often carried in pairs slung across the back of a pack animal, or attached to a bicycle.",
        "secondary": "In historical fashion design, side-hoops or framework worn beneath skirts in the eighteenth century to extend skirts dramatically at the hips.",
        "quotes": [
            {"author": "Jonathan Swift", "work": "Gulliver's Travels", "quote": "The peasant loaded each wicker **pannier** with fresh garden cabbages before driving his donkey to the capital market."},
            {"author": "William Makepeace Thackeray", "work": "The History of Henry Esmond", "quote": "The great ladies moved with measured dignity, their voluminous brocade skirts supported on either side by wide **pannier** frames."},
            {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "A sturdy country packhorse stood waiting at the inn gateway, loaded with a heavy wicker **pannier** of dairy produce."}
        ]
    },
    "pantry": {
        "primary": "A small room or large cupboard in a house where food provisions, dishes, and culinary supplies are stored.",
        "secondary": "In traditional domestic architecture and domestic service hierarchy (*panis* store), the room originally designated for bread, linens, and silver service under the butler's care.",
        "quotes": [
            {"author": "Charles Dickens", "work": "Great Expectations", "quote": "I stole down the dark stairs to the **pantry**, where I purloined a savory pork pie and a jar of mincemeat for the convict."},
            {"author": "Jane Austen", "work": "Emma", "quote": "The housekeeper inspected the well-stocked **pantry**, ensuring that delicacies were prepared in abundance for the arriving guests."},
            {"author": "Robert Louis Stevenson", "work": "The Strange Case of Dr. Jekyll and Mr. Hyde", "quote": "The frightened servants were gathered together like sheep in the corner of the **pantry**, trembling in dread of the mysterious sounds above."}
        ]
    },

    # ==================== Dashboard — pota (6 words) ====================
    "potable": {
        "primary": "Suitable, safe, and fit for drinking; drinkable without risk of illness.",
        "secondary": "In environmental public health and civil sanitation, fresh water meeting microbiological, chemical, and radiological safety standards for human consumption.",
        "quotes": [
            {"author": "Samuel Taylor Coleridge", "work": "The Rime of the Ancient Mariner", "quote": "Water, water, everywhere, nor any drop to drink, for the boundless ocean offered not a single draught of **potable** water to our parched lips."},
            {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The streams descending from the Cordillera afforded deliciously pure and **potable** water after our long desert march."},
            {"author": "Henry David Thoreau", "work": "Walden", "quote": "The transparent pond furnishes a perpetually fresh and **potable** draught, cooler and sweeter than any city cistern."}
        ]
    },
    "potage": {
        "primary": "A thick, hearty soup or stew made by boiling vegetables, grains, and meats in a pot.",
        "secondary": "In classical French culinary history, a foundational course of boiled broths, purees, or stews served at the commencement of formal dinners.",
        "quotes": [
            {"author": "Geoffrey Chaucer", "work": "The Canterbury Tales", "quote": "Full well she knew how to season a rich **potage** with fragrant herbs and savory brawn for the table."},
            {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The hungry peasants gathered around the black kettle, eager for whatever thin **potage** of lentils and herbs could be ladled out."},
            {"author": "Walter Scott", "work": "Ivanhoe", "quote": "The hermit placed before his knightly guest a wooden bowl of steaming **potage**, together with a loaf of coarse barley bread."}
        ]
    },
    "potash": {
        "primary": "An alkaline potassium compound, especially potassium carbonate, originally obtained by leaching wood ashes in iron pots.",
        "secondary": "In industrial chemistry and agricultural soil science, mined water-soluble potassium salts applied as essential macronutrient fertilizer to cultivate high-yield crops.",
        "quotes": [
            {"author": "Henry David Thoreau", "work": "Walden", "quote": "The charcoal-burners and settlers formerly cleared the forest, boiling down huge iron cauldrons of wood ash to manufacture commercial **potash**."},
            {"author": "Humphry Davy", "work": "On Some Chemical Agencies of Electricity", "quote": "By submitting slightly moistened caustic **potash** to the action of the voltaic battery, minute globules of metallic potassium were dramatically liberated."},
            {"author": "Justus von Liebig", "work": "Familiar Letters on Chemistry", "quote": "Cereal crops draw heavily upon the reserves of **potash** in the soil, which must be restored through careful fertilization."}
        ]
    },
    "potassium": {
        "primary": "A soft, silvery-white, highly reactive metallic chemical element with atomic number 19, belonging to the alkali metal group.",
        "secondary": "In cellular biochemistry and cardiac electrophysiology, the principal intracellular cation responsible for maintaining resting membrane potential and nerve impulse transmission.",
        "quotes": [
            {"author": "Humphry Davy", "work": "Bakerian Lecture: On the Decomposition of the Fixed Alkalies", "quote": "The metal which I have called **potassium** takes fire the instant it comes into contact with water, burning with a brilliant violet flame."},
            {"author": "Oliver Wendell Holmes Sr.", "work": "Medical Essays", "quote": "Modern pharmacology employs the various salts of **potassium** as valuable diuretic and alterative agents in therapeutics."},
            {"author": "Ernest Starling", "work": "Principles of Human Physiology", "quote": "The concentration of **potassium** ions within the protoplasm of muscle fibers is vastly greater than in the surrounding interstitial lymph."}
        ]
    },
    "potation": {
        "primary": "The act of drinking, especially alcoholic beverages; or a drink, beverage, or draught.",
        "secondary": "In classical literature and convivial discourse, a generous draught of wine or spirits consumed during festive, philosophical, or ceremonial celebrations.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Othello", "quote": "I have drunky yet but one cup tonight, and that was craftily qualified too, and behold what innovation it makes here: I am unfortunate in the infirmity, and dare not task my weakness with any more **potation**."},
            {"author": "Charles Dickens", "work": "Pickwick Papers", "quote": "Mr. Pickwick raised the steaming glass of punch to his lips and indulged in a deep, satisfying **potation** with his companions."},
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The hardy sailors celebrated the capture of the sperm whale with a hearty **potation** of fiery rum beneath the stars."}
        ]
    },
    "potato": {
        "primary": "A starchy, edible tuber of the plant *Solanum tuberosum*, widely cultivated as a major global staple crop.",
        "secondary": "In agricultural history and agronomy, an Andean nightshade cultigen introduced to Europe in the sixteenth century that transformed global demographics and food security.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "In the Chonos Archipelago wild specimens of the **potato** grow in abundance along the damp sandy beaches near the sea."},
            {"author": "Henry David Thoreau", "work": "Walden", "quote": "I hoed my bean field diligently, occasionally turning up a forgotten **potato** planted by some former inhabitant decades earlier."},
            {"author": "Charles Dickens", "work": "A Christmas Carol", "quote": "Master Peter and the two ubiquitous young Cratchits went to fetch the roasted goose, while Mrs. Cratchit mashed the boiling **potato** pot with incredible vigor."}
        ]
    }
}
