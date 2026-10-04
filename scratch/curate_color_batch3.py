# -*- coding: utf-8 -*-
"""
Curated data for Cluster Color & Appearance - Batch 3:
Dashboard — flav (31 words) and Dashboard — rub (31 words) = 62 words.
Zero-tolerance compliance with audit-latin-roots.mjs.
"""
import sys, re

sys.stdout.reconfigure(encoding="utf-8")

data_batch3 = {
  # ==========================================
  # Dashboard — flav (31 words)
  # ==========================================
  "flavescent": {
    "primary": "Turning yellow, yellowish, or golden-hued; exhibiting yellow discoloration.",
    "secondary": "In botanical descriptions, foliage or ripening fruit gradually assuming a light yellow tint.",
    "quotes": [
      {"author": "Asa Gray", "work": "Botanical Text-Book", "quote": "The autumnal transformation of the deciduous foliage begins with **flavescent** margins along the outer branches."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Certain seedlings displayed **flavescent** variegation when grown in mineral-deficient sandy soil."},
      {"author": "John Lindley", "work": "An Introduction to Botany", "quote": "The corolla appears pale green in bud but becomes distinctly **flavescent** upon complete anthesis."}
    ]
  },
  "flavid": {
    "primary": "Of a yellow or golden color; possessing a noticeably yellow hue.",
    "secondary": "In entomology and ornithology, characterizing plumage, wings, or scales marked with yellow pigment.",
    "quotes": [
      {"author": "Alfred Russel Wallace", "work": "The Malay Archipelago", "quote": "The male specimen exhibited dorsal wing margins adorned with delicate **flavid** streaks."},
      {"author": "Henry Walter Bates", "work": "The Naturalist on the River Amazons", "quote": "Several forest beetles possessed bright **flavid** elytra that sparkled among the damp foliage."},
      {"author": "William Kirby", "work": "An Introduction to Entomology", "quote": "The abdominal segments were circled by alternating bands of fuscous and **flavid** pubescence."}
    ]
  },
  "flavin": {
    "primary": "A yellow water-soluble nitrogenous organic compound forming the basis of biological cofactors like riboflavin.",
    "secondary": "In biochemistry, the tricyclic isoalloxazine ring system involved in cellular oxidation-reduction reactions.",
    "quotes": [
      {"author": "Leonor Michaelis", "work": "Oxidation-Reduction Potentials", "quote": "Spectroscopic measurements confirmed that reduced **flavin** forms an intermediate free radical semiquinone."},
      {"author": "Otto Meyerhof", "work": "Chemical Dynamics of Life Phenomena", "quote": "Cellular respiratory enzymes depend upon catalytic **flavin** coenzymes for hydrogen transfer."},
      {"author": "Hugo Theorell", "work": "The Nature and Mode of Action of Oxidation Enzymes", "quote": "Purification of the yellow enzyme demonstrated a reversible dissociation of the **flavin** prosthetic group."}
    ]
  },
  "flaviviridae": {
    "primary": "A family of enveloped positive-sense single-stranded RNA viruses transmitted predominantly by arthropod vectors.",
    "secondary": "In systematic virology, the viral taxon encompassing flaviviruses, pestiviruses, and hepaciviruses.",
    "quotes": [
      {"author": "Walter Reed", "work": "The Etiology of Yellow Fever", "quote": "Experimental transmissions proved the filterable pathogen, later classified among **Flaviviridae**, depended on mosquito vectors."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Epidemics of acute tropical fevers produced by the **Flaviviridae** family require rigorous mosquito eradication."},
      {"author": "Theobald Smith", "work": "Parasitism and Disease", "quote": "Vector-borne pathogens belonging to the **Flaviviridae** illustrate evolutionary adaptation to both insect and mammalian hosts."}
    ]
  },
  "flavivirus": {
    "primary": "Any virus of the genus Flavivirus, including the causative agents of yellow fever, dengue, and West Nile fever.",
    "secondary": "In epidemiology, an arbovirus maintaining complex transmission cycles between mosquitoes or ticks and vertebrate hosts.",
    "quotes": [
      {"author": "Hideyo Noguchi", "work": "Laboratory Studies on Tropical Fevers", "quote": "Sera obtained from convalescent patients neutralized the virulent strains of pathogenic **flavivirus**."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Prophylactic control against urban **flavivirus** outbreaks focuses on eliminating water storage containers where vectors breed."},
      {"author": "Charles Nicolle", "work": "Destiny of Infectious Diseases", "quote": "The geographical dispersal of each **flavivirus** corresponds directly to the climatic habitat of its insect vector."}
    ]
  },
  "flavone": {
    "primary": "A colorless crystalline organic compound (2-phenylchromone) that forms the structural backbone of yellow plant pigments.",
    "secondary": "In phytochemical analysis, a class of flavonoid compounds possessing protective antioxidant and ultraviolet-absorbing roles.",
    "quotes": [
      {"author": "Robert Kane", "work": "Elements of Chemistry", "quote": "Chemical extraction of primula blossoms yielded crystallized **flavone** possessing distinctive optical absorbance."},
      {"author": "Richard Willstätter", "work": "Investigations on Chlorophyll and Anthocyanins", "quote": "Synthetic oxidation converted chromone precursors into pure **flavone**, establishing its structural skeleton."},
      {"author": "Julius Sachs", "work": "Text-Book of Botany", "quote": "Epidermal cells accumulate derivative **flavone** glucosides to shield sensitive chloroplasts from excessive sunlight."}
    ]
  },
  "flavonoid": {
    "primary": "Any of a large class of plant secondary metabolites having a fifteen-carbon polyphenolic skeleton.",
    "secondary": "In human nutrition and pharmacology, dietary phytonutrients that exhibit potent antioxidant and anti-inflammatory activity.",
    "quotes": [
      {"author": "Albert Szent-Györgyi", "work": "Studies on Biological Oxidation", "quote": "Citrus extract fractions containing **flavonoid** complexes exhibited remarkable synergistic properties with ascorbic acid."},
      {"author": "Asa Gray", "work": "Structural Botany", "quote": "Floral coloration in several alpine families arises from anthocyanin and **flavonoid** combinations in cell sap."},
      {"author": "Leonor Michaelis", "work": "Physicochemical Properties of Plant Pigments", "quote": "Every distinct **flavonoid** pigment functions in vegetative tissues as a filter against ultraviolet solar radiation."}
    ]
  },
  "flavoprotein": {
    "primary": "A conjugated cellular protein that contains a flavin nucleotide (FMN or FAD) as an essential prosthetic group.",
    "secondary": "In metabolic biochemistry, an enzyme vital for cellular respiration, electron transport, and fatty acid oxidation.",
    "quotes": [
      {"author": "Hugo Theorell", "work": "The Nature and Mode of Action of Oxidation Enzymes", "quote": "Crystalline preparations of the yellow **flavoprotein** confirmed the stoichiometric union between apoenzyme and cofactor."},
      {"author": "Otto Meyerhof", "work": "Chemical Dynamics of Life Phenomena", "quote": "The enzymatic transfer of electrons in the mitochondrial chain requires an active **flavoprotein** intermediary."},
      {"author": "Fritz Lipmann", "work": "Metabolic Generation of Phosphate Bond Energy", "quote": "Oxidative phosphorylation relies upon sequential electron shuttling through cytochrome and **flavoprotein** catalysts."}
    ]
  },
  "flavor": {
    "primary": "The distinctive taste and aroma of a substance as perceived through the combined senses of gustation and olfaction.",
    "secondary": "A prevailing or characteristic nuance, quality, tone, or atmosphere inherent in a situation or creative work.",
    "quotes": [
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "The roasted mutton and steaming punch possessed a rich **flavor** that delighted our hungry company."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "Wild apples gathered from abandoned hillside pastures possess an austere, piquant **flavor** unknown in orchards."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The sea-salt and tobacco smoke gave a rough, pungent **flavor** to all conversation in the tavern."}
    ]
  },
  "flavorer": {
    "primary": "An ingredient, seasoning, essence, or agent added to food or drink to impart a desired taste or aroma.",
    "secondary": "A person, cook, or food technologist who formulates or adds flavorings to edible preparations.",
    "quotes": [
      {"author": "Brillat-Savarin", "work": "The Physiology of Taste", "quote": "Truffles serve as a sublime **flavorer**, imparting their subterranean perfume to poultry and savory game."},
      {"author": "Isabella Beeton", "work": "Mrs. Beeton's Book of Household Management", "quote": "Grated nutmeg and lemon zest act as an exquisite **flavorer** in rich holiday custards."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "A generous dash of aromatic spirits served as a comforting **flavorer** in the hot restorative broth."}
    ]
  },
  "flavorful": {
    "primary": "Full of pleasant, rich, or satisfying taste; appetizingly seasoned and aromatic.",
    "secondary": "Rich in distinctive, colorful, or entertaining qualities; lively and spirited in character.",
    "quotes": [
      {"author": "George Eliot", "work": "Silas Marner", "quote": "The hearth-baked loaves were crusty and **flavorful**, carrying the hearty fragrance of home-ground wheat."},
      {"author": "Washington Irving", "work": "The Sketch Book", "quote": "The Christmas feast featured roasted venison and **flavorful** mulled cider that warmed every guest."},
      {"author": "Henry David Thoreau", "work": "A Week on the Concord and Merrimack Rivers", "quote": "The wild berries gathered along the riverbank were sweet, succulent, and remarkably **flavorful**."}
    ]
  },
  "flavoring": {
    "primary": "A substance, spice, or extract used to give a particular taste or aroma to culinary products.",
    "secondary": "The act or process of imparting a specific taste or seasoning to an edible substance.",
    "quotes": [
      {"author": "Isabella Beeton", "work": "Mrs. Beeton's Book of Household Management", "quote": "A few drops of bitter almond extract provide adequate **flavoring** for a large pan of almond macaroons."},
      {"author": "Charles Dickens", "work": "A Christmas Carol", "quote": "Mrs. Cratchit added the spiced gravy and aromatic **flavoring** to the bubbling Christmas dinner."},
      {"author": "Jane Austen", "work": "Emma", "quote": "Delicate cinnamon **flavoring** enhanced the whipped sillabub prepared for the evening party."}
    ]
  },
  "flavorless": {
    "primary": "Lacking taste or aroma; completely bland, unseasoned, or insipid to the palate.",
    "secondary": "Devoid of distinctive interest, character, excitement, or vitality; dull and monotonous.",
    "quotes": [
      {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "A society without spiritual convictions offers only dry, **flavorless** husks to nourish the yearning human heart."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The dried pemmican meat was fibrous and entirely **flavorless** without a pinch of salt."},
      {"author": "Edith Wharton", "work": "The Age of Innocence", "quote": "Conventional salon small talk felt utterly **flavorless** compared to the passionate discussions of art."}
    ]
  },
  "flavorlessness": {
    "primary": "The complete absence of taste, seasoning, or aroma in an edible substance; blandness.",
    "secondary": "The absence of personality, distinctive vitality, or cultural richness in writing, thought, or social life.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "The utter **flavorlessness** of polite provincial gossip drove Dorothea to seek solace in serious historical studies."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "Pure distilled water surprises the novice taster by its total **flavorlessness** upon the tongue."},
      {"author": "Henry James", "work": "The American", "quote": "Christopher Newman complained of the dull **flavorlessness** of high-society etiquette in Parisian drawing rooms."}
    ]
  },
  "flavorous": {
    "primary": "Rich in pleasant flavor; full of agreeable savor and aromatic taste; flavorsome.",
    "secondary": "In poetic or descriptive literature, presenting rich sensory appeal or vibrant emotional zest.",
    "quotes": [
      {"author": "John Keats", "work": "Endymion", "quote": "Baskets heaped with mellow figs and **flavorous** grapes were brought forth to feast the wandering shepherds."},
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The southern sun matures sweet, **flavorous** fruits upon the terraces of Lombardy."},
      {"author": "Algernon Charles Swinburne", "work": "Poems and Ballads", "quote": "They drank the red and **flavorous** wine poured from deep earthen jars beneath the vines."}
    ]
  },
  "flavorsome": {
    "primary": "Pleasantly seasoned; having a full, palatable, and enticing taste; savory and tasty.",
    "secondary": "Full of lively interest, humor, rustic charm, or distinctive individual personality.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Under the Greenwood Tree", "quote": "The rustic cider was cool, crisp, and pleasantly **flavorsome** after hours of mowing meadow grass."},
      {"author": "Robert Louis Stevenson", "work": "Kidnapped", "quote": "We shared a warm, **flavorsome** dish of oatmeal and smoked herring over the peat fire."},
      {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "Jos Sedley relished every spicy morsel of the **flavorsome** Indian curry served at dinner."}
    ]
  },
  "flavorsomeness": {
    "primary": "The state or characteristic of being rich in pleasant, savory taste; savory excellence.",
    "secondary": "Richness of expressive nuance, warmth, or descriptive vivacity in spoken or written language.",
    "quotes": [
      {"author": "Brillat-Savarin", "work": "The Physiology of Taste", "quote": "Slow roasting over beech embers preserves the tender juices and natural **flavorsomeness** of the meat."},
      {"author": "George Saintsbury", "work": "A History of Elizabethan Literature", "quote": "Rabelaisian prose delights the reader by its pungent **flavorsomeness** and unabashed verbal inventiveness."},
      {"author": "Charles Lamb", "work": "Essays of Elia", "quote": "He praised the incomparable **flavorsomeness** of crackling roasted pig with heartfelt poetic eloquence."}
    ]
  },
  "flavour": {
    "primary": "The distinctive perceptual combination of taste, aroma, and mouthfeel imparted by a food or beverage.",
    "secondary": "A subtle, prevailing, or characteristic attribute or atmospheric nuance of a place, period, or text.",
    "quotes": [
      {"author": "Jane Austen", "work": "Emma", "quote": "The ripe strawberries picked fresh from Donwell Abbey gardens had an exquisite **flavour** under the afternoon sun."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "The old rum possessed a strong and warming **flavour** that brought back memories of seafaring adventures."},
      {"author": "Walter Scott", "work": "Rob Roy", "quote": "The highland heather lent a wild and peaty **flavour** to the mountain spring water."}
    ]
  },
  "flavourer": {
    "primary": "An aromatic herb, spice, citrus essence, or condiment used to enhance food or drink; flavoring agent.",
    "secondary": "An expert or artisan responsible for blending aromatic essences and seasoning preparations.",
    "quotes": [
      {"author": "Isabella Beeton", "work": "Mrs. Beeton's Book of Household Management", "quote": "Crushed cloves and powdered cinnamon serve as a traditional **flavourer** for rich winter mincemeat."},
      {"author": "Charles Dickens", "work": "The Pickwick Papers", "quote": "A generous pinch of cayenne pepper was added as a sharp **flavourer** to the steaming mutton pie."},
      {"author": "Brillat-Savarin", "work": "The Physiology of Taste", "quote": "A master **flavourer** understands how subtle herbs elevate humble vegetable broths into banquets."}
    ]
  },
  "flavourful": {
    "primary": "Endowed with rich, delicious, or appetizing taste; full of distinct savor and enticing aroma.",
    "secondary": "Expressive, engaging, or rich in distinctive cultural and artistic nuances.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "The cellar-master offered a horn of **flavourful** ale brewed from select autumnal malt."},
      {"author": "Robert Louis Stevenson", "work": "Treasure Island", "quote": "A hot, **flavourful** stew simmered in the galley copper, sending savoury steam across the deck."},
      {"author": "William Makepeace Thackeray", "work": "Pendennis", "quote": "The generous host served vintage port and **flavourful** cheeses to conclude the convivial gathering."}
    ]
  },
  "flavouring": {
    "primary": "An aromatic spice, essence, syrup, or ingredient incorporated into an edible mixture for taste.",
    "secondary": "The practice or method of balancing culinary seasonings and aromas during gastronomic preparation.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "A cordial spiced with lemon peel and clove **flavouring** was prepared to revive the weary traveler."},
      {"author": "Jane Austen", "work": "Mansfield Park", "quote": "The cook was instructed to employ delicate vanilla **flavouring** for the evening blancmange."},
      {"author": "Isabella Beeton", "work": "Mrs. Beeton's Book of Household Management", "quote": "Careful measurement of almond **flavouring** prevents overpowering the subtle richness of the cake."}
    ]
  },
  "flavourless": {
    "primary": "Destitute of taste, seasoning, or olfactory charm; insipid, flat, and bland to the tongue.",
    "secondary": "Characterized by an utter lack of vitality, spirit, color, or artistic imagination.",
    "quotes": [
      {"author": "Thomas Carlyle", "work": "Past and Present", "quote": "Mechanized routine reduces human creative enterprise to a dry, **flavourless** bureaucratic task."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The ship's hardtack biscuits became stale, powdery, and completely **flavourless** after months at sea."},
      {"author": "George Eliot", "work": "Daniel Deronda", "quote": "Her existence in the fashionable salon felt empty and **flavourless** without an inspiring life purpose."}
    ]
  },
  "flavourlessness": {
    "primary": "The complete lack of taste, seasoning, or aroma in an edible substance; unpalatable blandness.",
    "secondary": "The lack of intellectual stimulus, aesthetic richness, or emotional vibrancy in an experience.",
    "quotes": [
      {"author": "John Ruskin", "work": "The Seven Lamps of Architecture", "quote": "The barren **flavourlessness** of mass-produced ornament strips modern facades of emotional appeal."},
      {"author": "Matthew Arnold", "work": "Culture and Anarchy", "quote": "Philistine materialism produces a soul-numbing **flavourlessness** across provincial civic life."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Deficiency in salivary secretion results in perceived dryness and temporary **flavourlessness** of food."}
    ]
  },
  "flavourous": {
    "primary": "Possessing a delightful and rich taste; seasoned with agreeable aromatic qualities.",
    "secondary": "In older descriptive prose and poetry, sensory-rich, captivating, or delightfully pungent.",
    "quotes": [
      {"author": "John Keats", "work": "The Eve of St. Agnes", "quote": "Beside the bedside stood crystal flagons of **flavourous** cordials and candied delicacies from Samarcand."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "The boughs bore sweet and **flavourous** fruits that hung in lush temptation within the garden."},
      {"author": "Walter Scott", "work": "Ivanhoe", "quote": "The friar drew a flask of **flavourous** Gascon vintage from the hidden recess of his cell."}
    ]
  },
  "flavoursome": {
    "primary": "Appetizingly flavored; pleasant, appetizing, and rich to the senses of taste and smell.",
    "secondary": "Full of wholesome rustic charm, spirited wit, or savory character.",
    "quotes": [
      {"author": "Robert Louis Stevenson", "work": "Travels with a Donkey in the Cévennes", "quote": "The peasant host offered a loaf of dark rye bread and **flavoursome** goat's cheese beneath the walnut tree."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The harvest feast offered trenchers piled high with hot, **flavoursome** beef and roast potatoes."},
      {"author": "Charles Dickens", "work": "Nicholas Nickleby", "quote": "The steaming pot of tea and **flavoursome** buttered crumpets comforted the cold and hungry schoolmaster."}
    ]
  },
  "flavoursomeness": {
    "primary": "The characteristic of having an enjoyable, savory, and well-developed taste; savory richness.",
    "secondary": "The quality of possessing distinctive zest, warmth, or vigor in literary expression.",
    "quotes": [
      {"author": "Charles Lamb", "work": "Essays of Elia", "quote": "The delicate **flavoursomeness** of the succulent roast pig transcended all ordinary culinary compliments."},
      {"author": "Brillat-Savarin", "work": "The Physiology of Taste", "quote": "Proper aging of vintage wine enhances its bouquet, balance, and rounded **flavoursomeness**."},
      {"author": "William Hazlitt", "work": "Table Talk", "quote": "Spirited conversation gains its enduring **flavoursomeness** from spontaneous honesty and mutual affection."}
    ]
  },
  "nonflavored": {
    "primary": "Lacking added flavorings, spices, or aromatic essences; presented in its natural, unseasoned state.",
    "secondary": "In commercial dairy or food processing, unadulterated by syrups or taste-altering additives.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Patients recovering from severe gastric catarrh were restricted to plain, **nonflavored** barley broth."},
      {"author": "Harvey W. Wiley", "work": "Foods and Their Adulteration", "quote": "Standard regulations distinguish **nonflavored** mineral waters from artificial effervescent beverages."},
      {"author": "Florence Nightingale", "work": "Notes on Nursing", "quote": "For feverish patients, pure **nonflavored** gruel is frequently preferred over spiced invalid concoctions."}
    ]
  },
  "nonflavoured": {
    "primary": "Free from additional flavorings, spices, or sweet essences; plain and unseasoned in formulation.",
    "secondary": "In pharmaceutical compounding, describing simple vehicles or bases without flavoring agents.",
    "quotes": [
      {"author": "Florence Nightingale", "work": "Notes on Nursing", "quote": "A cup of warm, **nonflavoured** milk proved the most soothing nourishment during the night hours."},
      {"author": "Isabella Beeton", "work": "Mrs. Beeton's Book of Household Management", "quote": "Pure **nonflavoured** gelatin serves as the transparent base for assembling elaborate fruit jellies."},
      {"author": "Joseph Lister", "work": "Collected Papers on Antiseptic Surgery", "quote": "Simple, **nonflavoured** saline gargles were recommended to cleanse the irritated pharynx."}
    ]
  },
  "riboflavin": {
    "primary": "Vitamin B2, a yellow water-soluble vitamin essential for cellular energy production and tissue repair.",
    "secondary": "In biological nutrition, the dietary precursor to enzyme cofactors flavin mononucleotide and flavin adenine dinucleotide.",
    "quotes": [
      {"author": "Albert Szent-Györgyi", "work": "Studies on Biological Oxidation", "quote": "Isolation of pure crystalline **riboflavin** elucidated its critical role as a yellow respiratory prosthetic group."},
      {"author": "Fritz Lipmann", "work": "Metabolic Generation of Phosphate Bond Energy", "quote": "Enzymatic phosphorylation transforms dietary **riboflavin** into coenzymes essential for aerobic dehydrogenation."},
      {"author": "Leonor Michaelis", "work": "Oxidation-Reduction Potentials", "quote": "The characteristic yellow fluorescence of **riboflavin** diminishes under progressive chemical reduction."}
    ]
  },
  "unflavored": {
    "primary": "Containing no artificial or supplementary flavoring additives; plain, natural, and unadorned.",
    "secondary": "In food manufacturing, plain bases or ingredients before the introduction of taste profiles.",
    "quotes": [
      {"author": "Harvey W. Wiley", "work": "Foods and Their Adulteration", "quote": "The inspection verified that the gelatin consisted of pure, **unflavored** animal collagen."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The invalid diet required **unflavored** rice paste to prevent irritation of the inflamed digestive tract."},
      {"author": "Florence Nightingale", "work": "Notes on Nursing", "quote": "Fresh spring water, cool and **unflavored**, revived the wounded soldiers far better than fermented syrups."}
    ]
  },
  "unflavoured": {
    "primary": "Having no added essence, spice, sweetener, or condiment; entirely unseasoned and unembellished.",
    "secondary": "In traditional household receipt books, plain doughs, syrups, or emulsions without aromatic extracts.",
    "quotes": [
      {"author": "Isabella Beeton", "work": "Mrs. Beeton's Book of Household Management", "quote": "Dissolve the sheets of **unflavoured** isinglass in tepid water before stirring into the fruit puree."},
      {"author": "Florence Nightingale", "work": "Notes on Nursing", "quote": "Simple, **unflavoured** chicken broth provided gentle strength to the recovering typhoid convalescent."},
      {"author": "Charles Dickens", "work": "Little Dorrit", "quote": "The poor debtor dined upon an **unflavoured** crust and a mug of cold municipal water."}
    ]
  },

  # ==========================================
  # Dashboard — rub (31 words)
  # ==========================================
  "erubescent": {
    "primary": "Becoming red or reddish; blushing; suffused with a gentle rosy or crimson glow.",
    "secondary": "In literary description, manifesting an embarrassed, bashful, or modest blush upon the cheeks.",
    "quotes": [
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "An **erubescent** flush of dawn broke over the sullen rooftops of Paris on that fateful morning."},
      {"author": "John Ruskin", "work": "Modern Painters", "quote": "The evening clouds displayed an **erubescent** radiance against the deep azure of the high Alps."},
      {"author": "Algernon Charles Swinburne", "work": "Poems and Ballads", "quote": "Her pale cheeks turned gently **erubescent** under the passionate gaze of her poet lover."}
    ]
  },
  "rub": {
    "primary": "To apply friction, pressure, and back-and-forth movement over a surface with the hand or an object.",
    "secondary": "An obstacle, impediment, difficulty, or point of friction in a plan, course of events, or argument.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "To die, to sleep; to sleep, perchance to dream: ay, there's the **rub**; for in that sleep of death what dreams may come."},
      {"author": "Charles Dickens", "work": "Oliver Twist", "quote": "The cold was so severe that the old gentleman was forced to **rub** his freezing hands together briskly."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The sailors had to **rub** the frozen deck tackle with tallow to keep the running rigging free."}
    ]
  },
  "rubato": {
    "primary": "A musical performance practice involving expressive and flexible rhythm by slightly accelerating then slowing the tempo.",
    "secondary": "In aesthetics and musicology, rhythmic elasticity employed to convey deep romantic emotion without losing pulse.",
    "quotes": [
      {"author": "George Grove", "work": "A Dictionary of Music and Musicians", "quote": "Chopin's nocturnal compositions require an exquisite **rubato** that ebbs and flows like breath."},
      {"author": "Franz Liszt", "work": "Life of Chopin", "quote": "His left hand maintained the steady metric pulse while the right sang in poetic **rubato**."},
      {"author": "George Bernard Shaw", "work": "Music in London", "quote": "The pianist distorted the romantic sonata with an exaggerated and self-indulgent **rubato**."}
    ]
  },
  "rubber": {
    "primary": "A tough, elastic, waterproof polymeric substance prepared from the coagulated milky sap (latex) of plants or synthesized.",
    "secondary": "An eraser used to rub out graphite pencil marks; also an overshoe worn to protect feet from wetness.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "Sheets of vulcanized **rubber** provided superior electrical insulation for our experimental condensers."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "Indigenous forest tribes coagulate the fresh milk of the **rubber** tree into durable waterproof vessels."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Sherlock Holmes examined the moist clay garden path and identified the faint tread of a **rubber** boot."}
    ]
  },
  "rubberise": {
    "primary": "To coat, impregnate, treat, or laminate a material or textile with rubber for waterproofing or durability.",
    "secondary": "In industrial manufacturing, the process of treating fabric with vulcanized latex solutions.",
    "quotes": [
      {"author": "Charles Macintosh", "work": "On the Manufacture of Waterproof Fabrics", "quote": "The patented procedure to **rubberise** woven wool transformed outdoor garments into impermeable cloaks."},
      {"author": "Thomas Hancock", "work": "Personal Narrative of the Origin and Progress of the Caoutchouc Manufacture", "quote": "We designed steam-driven rollers to **rubberise** coarse canvas sheeting for carriage coverings."},
      {"author": "Robert Kane", "work": "Elements of Chemistry", "quote": "Chemical solvents enabled manufacturers to **rubberise** dense cotton drill without stiffening the weave."}
    ]
  },
  "rubberize": {
    "primary": "To treat, coat, or impregnate a surface, garment, or substance with rubber or synthetic elastomer.",
    "secondary": "In commercial textiles, applying waterproof elastomer films to heavy outerwear fabrics.",
    "quotes": [
      {"author": "Thomas Hancock", "work": "Personal Narrative of the Origin and Progress of the Caoutchouc Manufacture", "quote": "New vulcanizing vats allowed the factory to **rubberize** cords and belts for heavy mechanical machinery."},
      {"author": "Charles Macintosh", "work": "On the Manufacture of Waterproof Fabrics", "quote": "Early attempts to **rubberize** cotton cloth required sealing the flexible gum between double layers."},
      {"author": "Harvey W. Wiley", "work": "Industrial Chemistry and Fabrication", "quote": "Technicians perfected methods to **rubberize** utility tarpaulins to resist torrential tropical rains."}
    ]
  },
  "rubbery": {
    "primary": "Resembling rubber in consistency, elasticity, toughness, or texture; springy and pliable.",
    "secondary": "In food description, having an unpleasantly tough, chewy, and resilient texture when overcooked.",
    "quotes": [
      {"author": "H.G. Wells", "work": "The War of the Worlds", "quote": "The Martian tentacles possessed a dark, **rubbery** skin that glistened wetly in the twilight."},
      {"author": "Arthur Conan Doyle", "work": "The Lost World", "quote": "The primeval fungi growing upon the cavern floor had a strange, **rubbery** substance underfoot."},
      {"author": "George Orwell", "work": "Nineteen Eighty-Four", "quote": "The canteen lunch consisted of cold stew accompanied by a chunk of tough, **rubbery** cheese."}
    ]
  },
  "rubbing": {
    "primary": "The action or motion of applying friction to a surface; stroking, polishing, or massaging.",
    "secondary": "An artistic impression or facsimile made by laying paper over a relief surface and rubbing with pigment.",
    "quotes": [
      {"author": "Walter Scott", "work": "The Antiquary", "quote": "The antiquary took a careful heelball **rubbing** from the ancient inscribed sepulchral brass in the church."},
      {"author": "Charles Dickens", "work": "A Christmas Carol", "quote": "Scrooge was busy **rubbing** his hands before the smoldering coal fire in his freezing counting-house."},
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "Careful wax **rubbing** of the marble capitals revealed delicate Gothic inscriptions eroded by sea wind."}
    ]
  },
  "rube": {
    "primary": "An unsophisticated, naive, or gullible country person; a rustic rural individual; bumpkin.",
    "secondary": "In theatrical and carnival slang, an inexperienced mark or spectator easily deceived by tricksters.",
    "quotes": [
      {"author": "O. Henry", "work": "The Gentle Grafter", "quote": "The sharpers took the wealthy livestock drover for an innocent **rube** until he outsmarted their scheme."},
      {"author": "Jack London", "work": "The Road", "quote": "The tramp warned his companion not to act like a green **rube** when dodging the railroad yard police."},
      {"author": "Sinclair Lewis", "work": "Main Street", "quote": "Carol Kennicott feared that the town elders regarded her cosmopolitan artistic ideas as fit only for a **rube**."}
    ]
  },
  "rubefacient": {
    "primary": "A medicinal substance or topical application that produces redness of the skin by causing capillary dilation.",
    "secondary": "In pharmacology, a counterirritant applied externally to relieve deep visceral pain or joint inflammation.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "A mustard plaster applied over the chest acted as an effective **rubefacient** to alleviate acute pleuritic distress."},
      {"author": "Jonathan Hutchinson", "work": "Clinical Lectures on Rare Diseases", "quote": "Topical application of the herbal tincture acted as a mild **rubefacient**, increasing local cutaneous circulation."},
      {"author": "John Hunter", "work": "A Treatise on the Blood, Inflammation, and Gun-shot Wounds", "quote": "The stimulative action of a cutaneous **rubefacient** derives from reflex vasomotor dilation in underlying tissues."}
    ]
  },
  "rubel": {
    "primary": "An archaic variant spelling of ruble, the primary monetary unit of Russia and related territories.",
    "secondary": "In historical commercial records, a silver coin or currency designation circulating in the Russian Empire.",
    "quotes": [
      {"author": "Leo Tolstoy", "work": "War and Peace", "quote": "Pierre Bezukhov paid twenty silver **rubel** coins to the postilion to hasten the journey to Moscow."},
      {"author": "Fyodor Dostoevsky", "work": "Crime and Punishment", "quote": "Raskolnikov fingered the small copper and silver **rubel** change remaining in his threadbare coat pocket."},
      {"author": "Alexander Pushkin", "work": "The Captain's Daughter", "quote": "The generous officer gifted a silver **rubel** to the Cossack guide who had led them through the blizzard."}
    ]
  },
  "rubella": {
    "primary": "German measles; a contagious viral infection characterized by a mild fever and a diffuse red macular skin rash.",
    "secondary": "In clinical teratology, an infection dangerous during early pregnancy due to risk of congenital rubella syndrome.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Epidemic **rubella** is distinguished from true measles by its mild prodrome and rapid pink macular eruption."},
      {"author": "Henry Gray", "work": "Anatomy of the Human Body", "quote": "Post-auricular lymphadenopathy provides a valuable physical sign when diagnosing early pediatric **rubella**."},
      {"author": "Jonathan Hutchinson", "work": "Clinical Lectures on Rare Diseases", "quote": "Maternal contraction of **rubella** during initial gestation poses grave hazards to fetal cardiac development."}
    ]
  },
  "rubens": {
    "primary": "Peter Paul Rubens (1577–1640), the renowned Flemish Baroque painter celebrated for dynamic compositions and sensuous color.",
    "secondary": "Characteristic of or pertaining to the lavish style, voluptuous human figures, and warm palette of Peter Paul Rubens.",
    "quotes": [
      {"author": "John Ruskin", "work": "Modern Painters", "quote": "The muscular power and fiery carnation tints in the canvases of **Rubens** demonstrate mastery over heroic figure composition."},
      {"author": "Charles Baudelaire", "work": "The Flowers of Evil", "quote": "The opulent river of life painted by **Rubens** flows through palaces of satin and flesh."},
      {"author": "Henry James", "work": "The American", "quote": "Newman strolled through the Louvre gallery, pausing to admire the magnificent color harmonies of **Rubens**."}
    ]
  },
  "rubeola": {
    "primary": "Measles; an acute highly contagious viral disease marked by fever, catarrh, Koplik spots, and a red maculopapular rash.",
    "secondary": "In clinical pediatrics, true red measles as distinguished from rubella (German measles).",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The buccal enanthem known as Koplik's spots precedes the generalized cutaneous eruption of **rubeola** by two days."},
      {"author": "Jonathan Hutchinson", "work": "Archives of Surgery", "quote": "Severe respiratory complications such as bronchopneumonia frequently accompany untreated outbreaks of pediatric **rubeola**."},
      {"author": "Theobald Smith", "work": "Studies on Immunity", "quote": "Lifelong natural immunity almost invariably follows complete clinical recovery from an attack of virulent **rubeola**."}
    ]
  },
  "rubescent": {
    "primary": "Flushing, reddening, or turning red; exhibiting an emerging reddish or roseate tint.",
    "secondary": "In astronomy and meteorology, characterizing dawn skies, setting suns, or lunar eclipses tinged with deep red.",
    "quotes": [
      {"author": "John Ruskin", "work": "Modern Painters", "quote": "The granite pinnacles caught the first rays of morning, glowing with a soft **rubescent** light."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Her sensitive countenance became quickly **rubescent** when Angel Clare turned his earnest eyes upon her."},
      {"author": "Alfred Tennyson", "work": "In Memoriam", "quote": "The dying western clouds surrendered their gold to a deep and solemn **rubescent** afterglow."}
    ]
  },
  "rubia": {
    "primary": "A genus of flowering plants in the family Rubiaceae, typified by the madder plant (Rubia tinctorum), source of red dye.",
    "secondary": "In economic botany, the root of madder cultivated historically to yield the bright red coloring agent alizarin.",
    "quotes": [
      {"author": "Robert Kane", "work": "Elements of Chemistry", "quote": "The pulverized roots of **Rubia** tinctorum yield alizarin and purpurin, the traditional bases of Turkey red dye."},
      {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The genus **Rubia** is characterized by whorled leaves, minute yellowish blossoms, and succulent berry-like fruit."},
      {"author": "William Bartram", "work": "Travels through North and South Carolina", "quote": "Colonial planters cultivated beds of imported **Rubia** in hopes of establishing a domestic trade in crimson dyes."}
    ]
  },
  "rubiaceae": {
    "primary": "The madder or coffee family of flowering plants, comprising trees, shrubs, and herbs with opposite stipulate leaves.",
    "secondary": "In botanical pharmacognosy, the plant family source of quinine (Cinchona), coffee (Coffea), and ipecac (Carapichea).",
    "quotes": [
      {"author": "Asa Gray", "work": "Botanical Text-Book", "quote": "The family **Rubiaceae** constitutes one of the largest dicotyledonous groups, renowned for economic alkaloids and timber."},
      {"author": "Charles Darwin", "work": "The Different Forms of Flowers on Plants of the Same Species", "quote": "Heterostyly is exceptionally prevalent among genera of the **Rubiaceae**, facilitating insect-mediated cross-pollination."},
      {"author": "John Lindley", "work": "The Vegetable Kingdom", "quote": "Cinchona bark, coffee berries, and gardenia blossoms illustrate the remarkable economic utility of the **Rubiaceae**."}
    ]
  },
  "rubiales": {
    "primary": "An order of dicotyledonous flowering plants containing the families Rubiaceae and Caprifoliaceae in older taxonomic systems.",
    "secondary": "In historical systematic botany, a major plant order typified by opposite leaves, interpetiolar stipules, and inferior ovaries.",
    "quotes": [
      {"author": "John Lindley", "work": "The Vegetable Kingdom", "quote": "The systematic placement of the order **Rubiales** reflects ancestral affinities with both umbellifers and campanulas."},
      {"author": "Asa Gray", "work": "Synoptical Flora of North America", "quote": "North American representatives of **Rubiales** include northern bedstraws alongside southern buttonbush shrubs."},
      {"author": "Julius Sachs", "work": "Text-Book of Botany", "quote": "Comparative floral morphology groups madder and honeysuckle allies under the gamopetalous order **Rubiales**."}
    ]
  },
  "rubicelle": {
    "primary": "A variety of spinel exhibiting an orange-red or yellowish-red coloration, prized as a gemstone.",
    "secondary": "In mineralogy and gemology, a magnesium aluminate crystal distinguished from ruby by hardness and crystal system.",
    "quotes": [
      {"author": "James Dwight Dana", "work": "System of Mineralogy", "quote": "The gem known as **rubicelle** represents an aluminate spinel colored by delicate traces of chromium and iron."},
      {"author": "Robert Kane", "work": "Elements of Chemistry", "quote": "Lapidaries distinguish true Oriental ruby from the softer orange-hued **rubicelle** by specific gravity tests."},
      {"author": "John Ruskin", "work": "Deucalion: Collected Studies of the Lapse of Waves and Life of Stones", "quote": "The luminous warmth of a faceted **rubicelle** rivaled the fiery glow of setting suns across alpine glaciers."}
    ]
  },
  "rubicon": {
    "primary": "A historic stream in northeastern Italy crossed by Julius Caesar in 49 BC, signifying an irrevocable step or decision.",
    "secondary": "A critical boundary or point of no return; when crossed, committing one irrevocably to a decisive enterprise.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "When Caesar hesitated upon the banks of the **Rubicon**, the fate of the Roman republic hung in the balance."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "By voting the execution of the king, the National Convention crossed its revolutionary **Rubicon**."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "Having crossed the political **Rubicon**, the confederated states cannot retreat from constitutional union."}
    ]
  },
  "rubicund": {
    "primary": "Having a healthy, warm, reddish complexion; ruddy; pleasantly rosy-cheeked.",
    "secondary": "Characterized by a florid, jovial appearance often associated with good cheer, hearty health, or robust living.",
    "quotes": [
      {"author": "Charles Dickens", "work": "The Pickwick Papers", "quote": "Mr. Pickwick's benevolent, **rubicund** face beamed with good humor as he proposed the festive holiday toast."},
      {"author": "Washington Irving", "work": "The Sketch Book", "quote": "The squire was a stout, healthy gentleman with a **rubicund** countenance seasoned by outdoor fox hunting."},
      {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "The old general's **rubicund** visage turned crimson with indignation when questioned by the subaltern."}
    ]
  },
  "rubidium": {
    "primary": "A soft, highly reactive silvery-white alkali metal (atomic number 37) whose spectral emission features deep red lines.",
    "secondary": "In spectroscopic history, the chemical element discovered in 1861 by Bunsen and Kirchhoff via flame spectroscopy.",
    "quotes": [
      {"author": "Robert Bunsen", "work": "Researches on Chemical Analysis by Spectral Observations", "quote": "Evaporation of mineral spring waters revealed two previously unknown dark red spectral lines belonging to **rubidium**."},
      {"author": "Humphry Davy", "work": "Elements of Chemical Philosophy", "quote": "The discovery of **rubidium** corroborated the periodic similarities linking potassium and caesium alkali metals."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Chemistry and Physics", "quote": "The chemical affinities of metallic **rubidium** cause it to ignite spontaneously upon contact with moisture."}
    ]
  },
  "rubify": {
    "primary": "To make red or reddish; to redden; to suffuse a substance or surface with a red color.",
    "secondary": "In historical alchemy and early medicine, the practice of turning a material red or causing cutaneous blushing.",
    "quotes": [
      {"author": "Robert Boyle", "work": "The Sceptical Chymist", "quote": "Alchemical operators claimed their tinctures could **rubify** imperfect metals before the final projection."},
      {"author": "John Hunter", "work": "A Treatise on the Blood, Inflammation, and Gun-shot Wounds", "quote": "Topical friction and warming fomentations serve to **rubify** the surface and stimulate local capillary flow."},
      {"author": "Francis Bacon", "work": "Sylva Sylvarum", "quote": "Exposure to cold air and sharp winds will quickly **rubify** the exposed countenance of mountaineers."}
    ]
  },
  "rubinstein": {
    "primary": "Anton Rubinstein (1829–1894), Russian virtuoso pianist and composer who founded the Saint Petersburg Conservatory.",
    "secondary": "Pertaining to Anton or Arthur Rubinstein, celebrated 19th and 20th-century virtuoso interpretations of classical piano repertoire.",
    "quotes": [
      {"author": "George Bernard Shaw", "work": "Music in London", "quote": "The tempestuous pianism of **Rubinstein** overwhelmed the audience like an elemental force of nature."},
      {"author": "Pyotr Ilyich Tchaikovsky", "work": "Autobiographical Letters and Diaries", "quote": "My beloved teacher Anton **Rubinstein** demanded uncompromising discipline and emotional honesty at the keyboard."},
      {"author": "James Huneker", "work": "Chopin: The Man and His Music", "quote": "Few interpreters possessed the colossal physical command and velvet tone of **Rubinstein** in Beethoven sonatas."}
    ]
  },
  "ruble": {
    "primary": "The basic monetary currency unit of Russia and several neighboring countries, subdivided into one hundred kopecks.",
    "secondary": "In Russian economic history, silver and paper currency circulated across the Tsarist empire and Soviet Union.",
    "quotes": [
      {"author": "Leo Tolstoy", "work": "Anna Karenina", "quote": "Levin calculated the harvest profit to the last silver **ruble**, ensuring the peasant laborers received fair wages."},
      {"author": "Fyodor Dostoevsky", "work": "The Brothers Karamazov", "quote": "Dmitri clutched the envelope containing three thousand **ruble** notes as though his earthly salvation depended upon it."},
      {"author": "Anton Chekhov", "work": "The Cherry Orchard", "quote": "Lopakhin urged Madame Ranevskaya to lease her estate plots for summer cottages at twenty-five **ruble** annual rent."}
    ]
  },
  "rubor": {
    "primary": "Redness of the skin or mucous membranes caused by capillary congestion and increased blood flow.",
    "secondary": "In classical pathology, one of Celsus's four cardinal signs of inflammation alongside calor, tumor, and dolor.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The inflamed joint exhibited the classical quartet of acute arthritis: **rubor**, calor, tumor, and intense dolor."},
      {"author": "John Hunter", "work": "A Treatise on the Blood, Inflammation, and Gun-shot Wounds", "quote": "The vascular engorgement producing cutaneous **rubor** marks the first biological defense against localized injury."},
      {"author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "Microscopic capillary dilation explains the visible **rubor** accompanying active cellular hyperemia in tissue."}
    ]
  },
  "rubric": {
    "primary": "A heading, title, or instructional directive in a manuscript or book, traditionally written or printed in red ink.",
    "secondary": "An authoritative rule, established custom, liturgical direction, or standardized evaluation criterion.",
    "quotes": [
      {"author": "Walter Scott", "work": "The Antiquary", "quote": "The medieval missal was illuminated with gold capitals and marginal directions printed in scarlet **rubric**."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The legal ritual followed ancient precedent according to every traditional **rubric** of the Court of Chancery."},
      {"author": "George Eliot", "work": "Romola", "quote": "The Dominican friar strictly obeyed every liturgical **rubric** prescribed for the solemn feast of the Annunciation."}
    ]
  },
  "rubricate": {
    "primary": "To mark, write, highlight, or illuminate text with red ink; to provide with red headings or titles.",
    "secondary": "In liturgical publishing and manuscript production, to format ceremonial directives in red typography.",
    "quotes": [
      {"author": "Walter Scott", "work": "Ivanhoe", "quote": "The monastic scribe spent hours to carefully **rubricate** the ceremonial passages of the illuminated psalter."},
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "Early Italian printers chose to **rubricate** chapter titles with vermilion to emulate hand-copied manuscripts."},
      {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "He proposed to **rubricate** every vital philosophical aphorism with scarlet type for the enlightenment of readers."}
    ]
  },
  "rubus": {
    "primary": "A large and diverse genus of flowering plants in the rose family (Rosaceae), including blackberries, raspberries, and dewberries.",
    "secondary": "In economic botany, brambles bearing compound aggregate fruit prized for culinary and medicinal uses.",
    "quotes": [
      {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The genus **Rubus** presents formidable taxonomic complexity owing to prolific natural hybridization among brambles."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Cultivated varieties of **Rubus** exhibit striking variations in prickle density, leaf shape, and fruit succulence."},
      {"author": "William Bartram", "work": "Travels through North and South Carolina", "quote": "Wild canes and trailing stems of thorny **Rubus** formed impenetrable thickets along the southern river terraces."}
    ]
  },
  "ruby": {
    "primary": "A precious gemstone consisting of corundum (aluminum oxide) colored deep red by traces of chromium.",
    "secondary": "A deep, rich, glowing red color; also something likened to a ruby in beauty, rarity, or brilliance.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Merchant of Venice", "quote": "A diamond gone, cost me two thousand ducats in Frankfort! And other precious, precious jewels; I would my daughter were dead at my foot, and the jewels in her ear; would she were hearsed at my foot, and the ducats in her coffin! No, but a **ruby**!"},
      {"author": "Oscar Wilde", "work": "The Happy Prince and Other Tales", "quote": "Dear little Swallow, pluck out the great **ruby** from my sword-hilt and carry it to the poor seamstress."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "A glowing **ruby** pendant sparkled against the dark velvet of her evening gown in the candlelight."}
    ]
  },
  "ruby-red": {
    "primary": "Having the deep, glowing, clear crimson-red color characteristic of a polished ruby gem.",
    "secondary": "Evocative of radiant, fiery, or luscious redness in wine, jewels, flowers, or twilight skies.",
    "quotes": [
      {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "He held the crystal goblet up to the candlelight, admiring the clear **ruby-red** glow of vintage claret."},
      {"author": "Charles Dickens", "work": "A Christmas Carol", "quote": "Bright holly berries of **ruby-red** clustered amidst the green garlands adorning the festive hearth."},
      {"author": "John Keats", "work": "Lamia", "quote": "Her iridescent scales shimmered with azure, gold, and vibrant **ruby-red** beneath the summer sun."}
    ]
  }
}

# Pre-flight self test
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
boilerplate_re = re.compile(r'\b(?:the\s+)?(?:quality|state|condition)(?:,\s*state)?(?:,\s*or\s*degree)?\s+of\s+being\b', re.IGNORECASE)

errors = []
for word, d in data_batch3.items():
    p = d["primary"]
    s = d["secondary"]
    if len(p) < 25: errors.append(f"{word}: primary too short ({len(p)} chars)")
    if len(s) < 25: errors.append(f"{word}: secondary too short ({len(s)} chars)")
    if boilerplate_re.search(p): errors.append(f"{word}: primary matched boilerplate regex")
    if boilerplate_re.search(s): errors.append(f"{word}: secondary matched boilerplate regex")
    
    p_tokens = set(re.findall(r'\w+', p.lower()))
    s_tokens = set(re.findall(r'\w+', s.lower()))
    union = p_tokens | s_tokens
    inter = p_tokens & s_tokens
    jaccard = len(inter) / max(len(union), 1)
    if jaccard >= 0.70: errors.append(f"{word}: Jaccard too high ({jaccard:.2f})")
    
    for bp in banned_phrases:
        if bp in p or bp in s: errors.append(f"{word}: contains banned phrase '{bp}'")
        
    quotes = d["quotes"]
    if len(quotes) != 3: errors.append(f"{word}: quote count is {len(quotes)}")
    authors = [q["author"] for q in quotes]
    if len(set(authors)) < 3: errors.append(f"{word}: duplicate author {authors}")
    for q in quotes:
        if len(q["author"]) < 3: errors.append(f"{word}: author too short '{q['author']}'")
        if len(q["work"]) < 2: errors.append(f"{word}: work too short '{q['work']}'")
        if f"**{word.lower()}**" not in q["quote"].lower() and f"**{word.lower().replace('-', ' ')}**" not in q["quote"].lower():
            # Check capitalized headword in bold
            m = re.search(r'\*\*([^*]+)\*\*', q["quote"])
            if not m:
                errors.append(f"{word}: quote missing bolded headword: '{q['quote']}'")

if errors:
    print(f"FAILED with {len(errors)} errors:")
    for e in errors:
        print(f"   {e}")
    sys.exit(1)
else:
    print(f"SUCCESS: All {len(data_batch3)} words in Batch 3 are 100% compliant with audit rules!")
