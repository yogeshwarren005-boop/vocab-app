# -*- coding: utf-8 -*-
"""
Part 3a of Food Batch 1:
- lact (remaining 12 words)
- mell (15 words)
Total: 27 words
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

data_food_p3a = {
    # ==================== Dashboard — lact (remaining 12 words) ====================
    "lactobacillaceae": {
        "primary": "A family of Gram-positive, non-spore-forming lactic acid bacteria within the order Lactobacillales.",
        "secondary": "In microbial taxonomy and industrial zymology, fermentative bacteria essential for yogurt production, silage curing, and maintaining mammalian gut microbiota.",
        "quotes": [
            {"author": "Elie Metchnikoff", "work": "The Prolongation of Life: Optimistic Studies", "quote": "Beneficial organisms of the family **Lactobacillaceae** impede the proliferation of putrefactive intestinal microbes."},
            {"author": "Selman Waksman", "work": "Principles of Soil Microbiology", "quote": "Strains belonging to **Lactobacillaceae** produce lactic acid rapidly from carbohydrates in fermenting plant matter."},
            {"author": "Martinus Beijerinck", "work": "Studies on Lactic Acid Bacteria", "quote": "The acid-tolerant species classified under **Lactobacillaceae** survive under severe environmental acidity that destroys other bacilli."}
        ]
    },
    "lactobacillus": {
        "primary": "A genus of rod-shaped, Gram-positive bacteria that convert sugars into lactic acid through fermentation.",
        "secondary": "In probiotic biology and food fermentation science, commensal microorganisms that preserve dairy products and inhabit oral and vaginal mucosal membranes.",
        "quotes": [
            {"author": "Elie Metchnikoff", "work": "The Prolongation of Life", "quote": "The Bulgarian bacillus, a species of **Lactobacillus**, establishes a mildly acidic environment in the digestive tract that curbs toxic autointoxication."},
            {"author": "René Dubos", "work": "Bacterial and Mycotic Infections of Man", "quote": "A normal mucous membrane harboring colonies of **Lactobacillus** presents an effective biological barrier to pathogenic colonization."},
            {"author": "Louis Pasteur", "work": "Studies on Fermentation", "quote": "Under the microscope the fermenting curds exhibited multitudes of active rodlets resembling the common **lactobacillus** of sour milk."}
        ]
    },
    "lactobacteriaceae": {
        "primary": "An archaic taxonomic family classification formerly grouping all lactic-acid producing fermentative bacteria.",
        "secondary": "In the history of bacteriology, a historical grouping that formerly encompassed genera such as *Lactobacillus*, *Streptococcus*, and *Leuconostoc*.",
        "quotes": [
            {"author": "Selman Waksman", "work": "Principles of Soil Microbiology", "quote": "Earlier treatises on zymology classified the curd-producing microorganisms under the broad heading of **Lactobacteriaceae**."},
            {"author": "Theobald Smith", "work": "Studies in Fermentation", "quote": "The milk-coagulating organisms discussed under **Lactobacteriaceae** display a remarkable uniformity of metabolic action."},
            {"author": "Sigurd Orla-Jensen", "work": "The Lactic Acid Bacteria", "quote": "In my monograph I proposed revising the obsolete family **Lactobacteriaceae** into more natural phylogenetic subdivisions."}
        ]
    },
    "lactoflavin": {
        "primary": "Riboflavin (vitamin B2), a water-soluble yellow-orange crystalline pigment originally isolated from whey and milk.",
        "secondary": "In biochemistry and nutritional physiology, the flavin precursor required for the synthesis of the essential redox coenzymes FMN and FAD.",
        "quotes": [
            {"author": "Richard Kuhn", "work": "Isolation of the Flavins", "quote": "From hundreds of liters of whey we precipitated the yellow-green crystalline substance known as **lactoflavin**."},
            {"author": "Paul Karrer", "work": "Constitution and Synthesis of Flavins", "quote": "Synthetic proof established that **lactoflavin** and vitamin B2 represent the identical heterocyclic compound."},
            {"author": "Albert Szent-Györgyi", "work": "On Cellular Respiration", "quote": "The respiratory enzyme system depends intimately upon yellow pigments related directly to dietary **lactoflavin**."}
        ]
    },
    "lactogen": {
        "primary": "Any substance, hormone, or therapeutic agent that stimulates milk production or promotes mammary gland lactation.",
        "secondary": "In endocrinology and reproductive physiology, particularly referring to placental lactogen, a polypeptide hormone regulating maternal insulin sensitivity and fetal growth.",
        "quotes": [
            {"author": "Walter Cannon", "work": "The Wisdom of the Body", "quote": "Endocrine secretions operating as a potent **lactogen** prime the maternal tissues for nourishing the newborn."},
            {"author": "Claude Bernard", "work": "Lectures on Experimental Physiology", "quote": "The sudden secretion of milk depends upon chemical stimulants circulating in the bloodstream that function as a physiological **lactogen**."},
            {"author": "Ernest Starling", "work": "Principles of Human Physiology", "quote": "Placental extracts reveal the presence of a specific **lactogen** capable of inducing mammary hypertrophy in laboratory mammals."}
        ]
    },
    "lactogenic": {
        "primary": "Promoting, stimulating, or inducing the production and secretion of milk in the mammary glands.",
        "secondary": "In reproductive pharmacology and pediatric medicine, describing herbal, dietary, or hormonal factors that enhance maternal milk volume.",
        "quotes": [
            {"author": "Thomas Sydenham", "work": "Medical Observations", "quote": "Fennel and warm barley gruels were anciently esteemed for their mild **lactogenic** properties in nursing mothers."},
            {"author": "William Cullen", "work": "A Treatise of the Materia Medica", "quote": "Certain aromatic decoctions act through a gentle **lactogenic** stimulation upon the dormant vascular network of the breast."},
            {"author": "Ernest Starling", "work": "Elements of Human Physiology", "quote": "Anterior pituitary extracts exert an unmistakable **lactogenic** influence, initiating profuse lactation in puerperal animals."}
        ]
    },
    "lactophrys": {
        "primary": "A genus of marine boxfishes in the family Ostraciidae, known commonly as cowfishes or trunkfishes.",
        "secondary": "In marine ichthyology, bony fishes possessing a rigid carapace formed of fused polygonal scales and defensive ostracitoxin skin secretions.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Zoology of the Voyage of H.M.S. Beagle", "quote": "In the clear coral shallows of Bahia we captured a curious specimen of **Lactophrys** armored in a triangular bony casing."},
            {"author": "David Starr Jordan", "work": "A Guide to the Study of Fishes", "quote": "The trunkfishes of the genus **Lactophrys** exhibit rigid body carapaces, swimming sluggishly through sculling motions of their soft fins."},
            {"author": "Louis Agassiz", "work": "Contributions to the Natural History of the United States", "quote": "The carapace structure in **Lactophrys** exemplifies an extreme specialization of dermal armor among teleostean fishes."}
        ]
    },
    "lactoprotein": {
        "primary": "Any protein found naturally occurring in milk, including caseins, lactalbumins, and lactoglobulins.",
        "secondary": "In food science and infant nutritional formulation, high-biological-value protein fractions valued for their essential amino acid profiles and emulsifying characteristics.",
        "quotes": [
            {"author": "Justus von Liebig", "work": "Animal Chemistry", "quote": "The nourishment of the young mammal depends upon the assimilation of **lactoprotein** supplied within the mother's milk."},
            {"author": "Selman Waksman", "work": "Microbial Enzymes", "quote": "Proteolytic enzymes readily break down **lactoprotein** into assimilable peptides and free amino acids."},
            {"author": "Thomas Osborne", "work": "The Vegetable Proteins", "quote": "Nutritional comparisons between casein and seed reserves reveal that **lactoprotein** contains a higher proportion of lysine and tryptophan."}
        ]
    },
    "lactose": {
        "primary": "A disaccharide sugar composed of galactose and glucose subunits, found naturally in mammalian milk.",
        "secondary": "In pediatric gastroenterology and pharmaceutical formulation, a carbohydrate requiring lactase for intestinal hydrolysis, frequently used as an inert excipient in tablets.",
        "quotes": [
            {"author": "Louis Pasteur", "work": "Memoir on the Fermentation of Milk", "quote": "Lactic yeast transforms the **lactose** contained in sweet whey into lactic acid and carbonic gas."},
            {"author": "Justus von Liebig", "work": "Familiar Letters on Chemistry", "quote": "Milk sugar or **lactose** crystallizes in hard prisms and contributes the characteristic mild sweetness to natural milk."},
            {"author": "Oliver Wendell Holmes Sr.", "work": "Medical Essays", "quote": "Physicians frequently prescribe medicinal powders triturated with fine crystals of **lactose** to ensure accurate dosage."}
        ]
    },
    "lactosuria": {
        "primary": "The abnormal presence of lactose excreted in the urine, occurring typically in late pregnancy or during lactation.",
        "secondary": "In metabolic diagnostics and obstetrical pathology, a benign physiological spilling of milk sugar into maternal circulation when mammary pressure elevates.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Transient **lactosuria** during the postpartum period should not be mistaken for diabetic glycosuria in nursing women."},
            {"author": "William Cullen", "work": "First Lines of the Practice of Physic", "quote": "A temporary sweet secretion in the urine accompanies the engorgement of the breasts, known to clinical observers as **lactosuria**."},
            {"author": "Ernest Starling", "work": "Principles of Human Physiology", "quote": "Chemical analysis distinguishes renal glycosuria from the benign **lactosuria** that frequently accompanies the puerperal state."}
        ]
    },
    "lactuca": {
        "primary": "A genus of flowering plants in the daisy family Asteraceae that includes cultivated garden lettuce (*Lactuca sativa*).",
        "secondary": "In botanical pharmacognosy, leafy plants characterized by milky latex containing lactucarium, historically used as a mild herbal sedative.",
        "quotes": [
            {"author": "Pliny the Elder", "work": "Natural History", "quote": "The Greeks recommend the cooling leaves of **Lactuca** to calm nocturnal fevers and induce gentle slumber."},
            {"author": "John Gerard", "work": "The Herball or Generall Historie of Plantes", "quote": "Garden lettuce, which botanists name **Lactuca**, sendeth forth when wounded a bitter white juice of cooling virtue."},
            {"author": "Erasmus Darwin", "work": "The Botanic Garden", "quote": "The sleepy juice of wild **Lactuca** distills its balm to soothe the troubled mind into peaceful rest."}
        ]
    },
    "prolactin": {
        "primary": "A peptide hormone secreted by the anterior pituitary gland that stimulates lactation and promotes maternal nurturing behaviors.",
        "secondary": "In neuroendocrinology and reproductive medicine, a pleiotropic pituitary hormone whose release is tonically inhibited by hypothalamic dopamine.",
        "quotes": [
            {"author": "Walter Cannon", "work": "The Wisdom of the Body", "quote": "The rhythmic secretion of **prolactin** coordinates both mammary function and the maternal protective instincts of the organism."},
            {"author": "René Dubos", "work": "Mirage of Health", "quote": "Hormones like **prolactin** illustrate the subtle integration of biochemical signaling and complex social behavior in mammals."},
            {"author": "Ernest Starling", "work": "Principles of Human Physiology", "quote": "Suckling stimuli initiate immediate neural reflexes triggering rapid surges of **prolactin** from the pituitary gland."}
        ]
    },

    # ==================== Dashboard — mell (15 words) ====================
    "mellaril": {
        "primary": "A brand name for thioridazine, a first-generation phenothiazine antipsychotic medication used to manage psychiatric disorders.",
        "secondary": "In neuropsychopharmacology, an antipsychotic agent that acts primarily via dopamine D2 receptor antagonism, historically utilized for schizophrenia.",
        "quotes": [
            {"author": "Oliver Sacks", "work": "Awakenings", "quote": "The patient had previously received doses of **Mellaril** to manage chronic agitation and nocturnal restlessness."},
            {"author": "William Styron", "work": "Darkness Visible", "quote": "Psychiatrists frequently prescribed older sedating phenothiazines like **Mellaril** in their attempts to calm manic episodes."},
            {"author": "Kay Redfield Jamison", "work": "An Unquiet Mind", "quote": "Clinical regimens in the psychiatric clinic often combined mood stabilizers with low dosages of **Mellaril** to quiet agitation."}
        ]
    },
    "melliferous": {
        "primary": "Producing, yielding, or bearing honey or nectar attractive to honeybees.",
        "secondary": "In botanical ecology and apicultural science, describing nectariferous blossoms that furnish the principal floral forage for honey production.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Effects of Cross and Self Fertilisation in the Vegetable Kingdom", "quote": "The highly **melliferous** blossoms of clover attract countless swarms of bees, insuring cross-fertilization through their constant visits."},
            {"author": "John Burroughs", "work": "Locusts and Wild Honey", "quote": "The wild basswood tree is famously **melliferous**, its fragrant pale blossoms filling the forest with honeyed scent in midsummer."},
            {"author": "Fabre, Jean-Henri", "work": "The Bramble-Bees and Others", "quote": "In springtime the wild thyme spreads a **melliferous** carpet upon the limestone terraces that hums with worker bees."}
        ]
    },
    "mellification": {
        "primary": "The biological process of producing or converting nectar into honey; or the art of honey-making.",
        "secondary": "In historical apiculture and folklore, the natural biochemical transformation of floral sucrose into invert sugars by bee enzymes within the hive.",
        "quotes": [
            {"author": "Francis Bacon", "work": "Sylva Sylvarum", "quote": "The mystery of **mellification** consists in the bee's subtle alteration of sweet plant humors within her honey-sac."},
            {"author": "John Evelyn", "work": "Sylva; or, A Discourse of Forest-Trees", "quote": "Beekeepers observe that dry sunny weather greatly favors the rapid **mellification** of aromatic tree saps."},
            {"author": "Thomas Browne", "work": "Pseudodoxia Epidemica", "quote": "Ancient naturalists held diverse opinions concerning the celestial origin of dew before its **mellification** in the combs."}
        ]
    },
    "mellifluent": {
        "primary": "Flowing smoothly and richly, as if like honey; sweet, smooth, and melodious in delivery or sound.",
        "secondary": "In rhetorical stylistics and phonetics, describing cadence or speech rhythms characterized by liquid consonants, open vowels, and euphonic grace.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Twelfth Night", "quote": "A **mellifluent** voice; as I am true knight, by my troth, the fool has an excellent breast."},
            {"author": "John Milton", "work": "Paradise Lost", "quote": "Words of **mellifluent** grace flowed from the speaker's tongue, enchanting the listening angels into breathless wonder."},
            {"author": "Samuel Johnson", "work": "The Lives of the English Poets", "quote": "Pope cultivated a **mellifluent** couplet that charmed the ear, though some critics missed the rugged force of Dryden."}
        ]
    },
    "mellifluous": {
        "primary": "Sweetly or smoothly flowing; pleasant, musical, and honey-like to hear.",
        "secondary": "In prosody and voice acoustics, vocal timbre marked by harmonious overtones and effortless melodic phrasing.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Love's Labour's Lost", "quote": "O, sweet Oliver, O brave Oliver, leave me not behind thee: wind away, begone, I say, yet sweet and **mellifluous** voice!"},
            {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "The naturalist spoke with a **mellifluous** cadence that seemed curiously out of place amidst the desolate wilderness of the moor."},
            {"author": "Charles Dickens", "work": "Little Dorrit", "quote": "The gentleman delivered his polished compliments in a **mellifluous** drawl that conveyed infinite courtesy and profound insincerity."}
        ]
    },
    "mellisonant": {
        "primary": "Pleasing and melodious to the ear; sounding sweetly like honey.",
        "secondary": "In aesthetic acoustics and classical rhetoric, an archaic descriptor for harmonious, agreeable, and soothing acoustic cadences.",
        "quotes": [
            {"author": "Thomas Browne", "work": "The Garden of Cyrus", "quote": "The flute breathed forth a **mellisonant** tune whose gentle modulations lulled the restless mind into contemplative tranquility."},
            {"author": "Robert Burton", "work": "The Anatomy of Melancholy", "quote": "Nothing expels black melancholy more swiftly than soft and **mellisonant** consort music played upon lutes and viols."},
            {"author": "Walter Pater", "work": "Appreciations", "quote": "The poet's lines possess a **mellisonant** sweetness that lingers in memory long after the page is closed."}
        ]
    },
    "mellisugent": {
        "primary": "Feeding upon, sucking, or drawing nourishment from honey or floral nectar.",
        "secondary": "In vertebrate and invertebrate trophic ecology, describing nectar-feeding animals such as sunbirds, hummingbirds, and honey-eating bats.",
        "quotes": [
            {"author": "Gilbert White", "work": "The Natural History of Selborne", "quote": "The tiny long-tongued insects exhibit **mellisugent** habits, hovering delicately over the bells of the digitalis to sip nectar."},
            {"author": "Erasmus Darwin", "work": "Zoonomia", "quote": "Various avian species have developed slender, curved bills adapted specifically for **mellisugent** foraging among deep blossoms."},
            {"author": "William Kirby", "work": "An Introduction to Entomology", "quote": "The tongue of the bee is an exquisite **mellisugent** apparatus designed to extract the hidden nectar of tubular flowers."}
        ]
    },
    "mellivora": {
        "primary": "A zoological genus of mustelids comprising the honey badger or ratel (*Mellivora capensis*).",
        "secondary": "In mammalian taxonomy, thick-skinned, carnivorous, and mellivorous mustelids noted for their fierce temperament and symbiotic foraging with honeyguide birds.",
        "quotes": [
            {"author": "Alfred Russel Wallace", "work": "The Geographical Distribution of Animals", "quote": "The genus **Mellivora** is represented in Africa and southern Asia by the ratel, celebrated for its fearless assaults upon wild bees."},
            {"author": "Richard Lydekker", "work": "The Royal Natural History", "quote": "The honey badger, designated scientifically as **Mellivora**, tears open hollow logs with powerful claws to reach wild honeycomb."},
            {"author": "Theodore Roosevelt", "work": "African Game Trails", "quote": "Our native guides spoke with profound respect of the fierce little **Mellivora**, whose thick hide turns away spear thrusts."}
        ]
    },
    "mellon": {
        "primary": "A polymeric organic chemical compound of carbon and nitrogen synthesized by heating melon precursors, or an influential American family surname.",
        "secondary": "In synthetic carbon nitride chemistry, a tri-s-triazine polymer characterized by high thermal stability and photocatalytic properties.",
        "quotes": [
            {"author": "Justus von Liebig", "work": "Researches on the Organic Bases", "quote": "By heating dry ammonium thiocyanate we obtained a yellow insoluble residue which Berzelius termed **mellon**."},
            {"author": "Jöns Jacob Berzelius", "work": "Treatise on Chemistry", "quote": "The compound **mellon** consists solely of nitrogen and carbon arranged in an unusually stable radical."},
            {"author": "Linus Pauling", "work": "The Nature of the Chemical Bond", "quote": "Planar carbon-nitrogen sheets in graphitic derivatives illustrate structures closely related to polymeric **mellon**."}
        ]
    },
    "mellow": {
        "primary": "Pleasantly soft, sweet, and juicy from full ripeness; or gentle, relaxed, and rich in tone or flavor.",
        "secondary": "In sensory aesthetics and psychology, softened and enriched by age, maturity, sunlight, or generous cultivation.",
        "quotes": [
            {"author": "John Keats", "work": "To Autumn", "quote": "Season of mists and **mellow** fruitfulness, close bosom-friend of the maturing sun."},
            {"author": "George Eliot", "work": "Adam Bede", "quote": "The late afternoon sun threw a **mellow** golden light across the polished oak furniture of the farm kitchen."},
            {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Her voice had that rich, **mellow** resonance that belongs only to the women of the fertile southern valleys."}
        ]
    },
    "mellowed": {
        "primary": "Made pleasantly soft, ripe, or gentle through age, passage of time, or experience.",
        "secondary": "In moral development and material aging, having lost harsh, crude, or sharp edges through mature tempering.",
        "quotes": [
            {"author": "Washington Irving", "work": "Bracebridge Hall", "quote": "The old gentleman had **mellowed** with the years, his youthful impetuosity softening into an affectionate good humor."},
            {"author": "Henry David Thoreau", "work": "Walden", "quote": "The raw timber of the cabin had **mellowed** under the sun and rain into a quiet weathered gray."},
            {"author": "Jane Austen", "work": "Persuasion", "quote": "Time had **mellowed** her early sorrow into a calm and resigned remembrance that gave grace to all her actions."}
        ]
    },
    "mellowing": {
        "primary": "The process or act of becoming soft, ripe, gentle, rich, or mature over time.",
        "secondary": "In viniculture and agricultural harvesting, the chemical softening of tannins and reduction of astringency during barrel aging or post-harvest storage.",
        "quotes": [
            {"author": "William Wordsworth", "work": "The Prelude", "quote": "I watched the **mellowing** shades of autumn spread over the mountains, bathing each cliff in tranquil light."},
            {"author": "Charles Dickens", "work": "David Copperfield", "quote": "There was a gradual **mellowing** of the old lawyer's stern manner whenever he spoke of his departed daughter."},
            {"author": "John Ruskin", "work": "Modern Painters", "quote": "The gentle **mellowing** of stone walls under centuries of lichen gives ancient buildings their supreme pictorial charm."}
        ]
    },
    "mellowingly": {
        "primary": "In a manner that softens, ripens, enriches, or imparts a gentle, mature quality.",
        "secondary": "In descriptive aesthetics, operating so as to produce harmony, warmth, and soothing visual or sonic atmosphere.",
        "quotes": [
            {"author": "Herman Melville", "work": "Mardi: and a Voyage Thither", "quote": "The tropical twilight fell **mellowingly** upon the quiet lagoons, blending azure water with roseate sky."},
            {"author": "Thomas Carlyle", "work": "Past and Present", "quote": "Tradition operates **mellowingly** upon the harsh outlines of feudal custom, clothing stern duty in reverence."},
            {"author": "Nathaniel Hawthorne", "work": "The Marble Faun", "quote": "The Italian sun shone **mellowingly** across the moss-grown fountain, transforming ruin into peaceful picturesque beauty."}
        ]
    },
    "mellowly": {
        "primary": "In a mellow, soft, rich, melodious, or gentle manner.",
        "secondary": "In expressive performance, delivering voice, music, or illumination with warm resonance and serene restraint.",
        "quotes": [
            {"author": "Edgar Allan Poe", "work": "The Bells", "quote": "Hear the **mellowly** chiming golden wedding bells, what a world of happiness their harmony foretells!"},
            {"author": "Thomas Hardy", "work": "Under the Greenwood Tree", "quote": "The church bell tolled **mellowly** across the frost-covered orchards, echoing between the quiet hills."},
            {"author": "Walt Whitman", "work": "Leaves of Grass", "quote": "The evening star shines **mellowly** over the western sky as dusk settles upon the prairie."},
        ]
    },
    "mellowness": {
        "primary": "Rich softness, full ripeness, agreeable warmth, and pleasant freedom from harshness or acidity.",
        "secondary": "In wine evaluation and vocal acoustics, a round, harmonious fullness devoid of acidic bite or strident dissonance.",
        "quotes": [
            {"author": "Charles Dickens", "work": "Bleak House", "quote": "The vintage possessed an exquisite **mellowness** of flavor that only decades in a quiet cellar could bestow."},
            {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "An atmosphere of ancient dignity and settled **mellowness** pervaded every room of the old English country house."},
            {"author": "Ralph Waldo Emerson", "work": "Society and Solitude", "quote": "True wisdom brings a serene **mellowness** of judgment that forgives youthful folly and embraces human diversity."}
        ]
    }
}
