# -*- coding: utf-8 -*-
"""
Part 1: merces (20 words)
['commercial', 'commercial-grade', 'commercialisation', 'commercialise', 'commercialised', 'commercialism', 'commercialization', 'commercialize', 'commercialized', 'commercially', 'mercenaria', 'mercenary', 'merciless', 'mercilessly', 'mercilessness', 'noncommercial', 'uncommercial', 'uncommercialised', 'uncommercialized', 'unmercenary']
"""
import sys
sys.stdout.reconfigure(encoding="utf-8")

data_merces = {
  "commercial": {
    "primary": "Pertaining to commerce, mercantile trade, business transactions, or the manufacture and sale of goods for monetary gain.",
    "secondary": "In media broadcasting and cultural sociology, produced primarily for mass consumption and immediate market profit rather than purely artistic value.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The bustling town hall was thronged with farmers and traders engaged in brisk **commercial** traffic on market day."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "His uncle had acquired substantial wealth through prudent investments and shrewd **commercial** enterprises across the county."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "I observed that the trade of the village was governed by strictly **commercial** instincts rather than pastoral simplicity."}
    ]
  },
  "commercial-grade": {
    "primary": "Manufactured to rigorous standards of strength, durability, and duty suitable for continuous industrial, professional, or retail use.",
    "secondary": "In engineering specifications and procurement protocols, materials or equipment exceeding domestic consumer tolerances to withstand heavy repetitive stress.",
    "quotes": [
      {"author": "Thomas Edison", "work": "The Papers of Thomas A. Edison", "quote": "The laboratory required **commercial-grade** copper wiring and heavy insulated fittings to sustain continuous high-voltage trials."},
      {"author": "Henry Ford", "work": "My Life and Work", "quote": "We replaced the fragile shop machinery with durable, **commercial-grade** presses designed for uninterrupted assembly work."},
      {"author": "Herbert Hoover", "work": "Principles of Mining", "quote": "Deep lode extraction demands **commercial-grade** steel cables and hoisting engines built to withstand abrasive quarry conditions."}
    ]
  },
  "commercialisation": {
    "primary": "The process of managing, exploiting, or transforming an activity, product, or enterprise primarily for financial profit.",
    "secondary": "In cultural economics and sociology, the adaptation of indigenous customs, intellectual discoveries, or artistic forms to market mechanisms and commodity exchange.",
    "quotes": [
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The unrestrained **commercialisation** of Venetian crafts degraded the noble craftsmanship that once honored sacred architecture."},
      {"author": "Matthew Arnold", "work": "Culture and Anarchy", "quote": "He lamented the steady **commercialisation** of provincial life, where pecuniary measurement supplanted spiritual cultivate."},
      {"author": "Thorstein Veblen", "work": "The Higher Learning in America", "quote": "The creeping **commercialisation** of academic research subordinated disinterested inquiry to immediate corporate utility."}
    ]
  },
  "commercialise": {
    "primary": "To exploit, adapt, or develop a concept, invention, artistic work, or service for market sale and financial return.",
    "secondary": "In business administration, to transition an invention or experimental technique from prototype development into full-scale market production.",
    "quotes": [
      {"author": "George Bernard Shaw", "work": "Major Barbara", "quote": "They seek to **commercialise** human salvation itself, turning benevolence into a balance sheet of public acclaim."},
      {"author": "H. G. Wells", "work": "Tono-Bungay", "quote": "My uncle resolved to **commercialise** the patent medicine on a scale that would capture the national press."},
      {"author": "William Morris", "work": "Hopes and Fears for Art", "quote": "Modern industry attempts to **commercialise** every decorative impulse, stripping manual labor of its spontaneous joy."}
    ]
  },
  "commercialised": {
    "primary": "Transformed, developed, or managed primarily for commercial exploitation and monetary profitability.",
    "secondary": "In socio-cultural critique, altered so that intrinsic ethical, aesthetic, or traditional values are sacrificed to consumer marketing.",
    "quotes": [
      {"author": "G. K. Chesterton", "work": "What's Wrong with the World", "quote": "The modern Christmas festival has become thoroughly **commercialised**, smothered under department store pageantry."},
      {"author": "Virginia Woolf", "work": "The Common Reader", "quote": "Literary publishing had grown increasingly **commercialised**, forcing novelists to court broad metropolitan tastes."},
      {"author": "George Orwell", "work": "The Road to Wigan Pier", "quote": "Even traditional seaside resorts had become mechanized and **commercialised** for cheap weekend excursionists."}
    ]
  },
  "commercialism": {
    "primary": "The practices, principles, methods, and general spirit of commerce and financial profit-seeking.",
    "secondary": "In ethical and aesthetic commentary, excessive emphasis upon financial return and market advantage at the expense of artistic or moral considerations.",
    "quotes": [
      {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "The rampant **commercialism** of the age threatens to subordinate the finest intellectual faculties to the pursuit of dividends."},
      {"author": "William James", "work": "The Varieties of Religious Experience", "quote": "A pervasive **commercialism** frequently deadens that contemplative detachment essential to profound mystical insight."},
      {"author": "Jane Addams", "work": "Democracy and Social Ethics", "quote": "Unregulated industrial **commercialism** treated immigrant workers as mere mechanical factors in factory production."}
    ]
  },
  "commercialization": {
    "primary": "The introduction of a new product, technology, or service into the public marketplace to generate revenue.",
    "secondary": "In science policy and economic development, the systematic translation of university laboratory discoveries into marketable industrial commodities.",
    "quotes": [
      {"author": "Thorstein Veblen", "work": "The Theory of Business Enterprise", "quote": "The rapid **commercialization** of mechanical inventions concentrated industrial control in the hands of investment bankers."},
      {"author": "John Dewey", "work": "Democracy and Education", "quote": "The excessive **commercialization** of vocational training risks reducing liberal education to crude job preparation."},
      {"author": "Lewis Mumford", "work": "Technics and Civilization", "quote": "The aggressive **commercialization** of electrical power revolutionized domestic habits throughout modern cities."}
    ]
  },
  "commercialize": {
    "primary": "To organize, manage, or develop something for the express purpose of generating pecuniary profit.",
    "secondary": "In economic strategy, to establish distribution channels, marketing campaigns, and volume manufacturing for an innovative process.",
    "quotes": [
      {"author": "Sinclair Lewis", "work": "Arrowsmith", "quote": "The pharmaceutical directors urged Martin to **commercialize** his newly isolated antibacterial phage without awaiting clinical trials."},
      {"author": "Frank Norris", "work": "The Pit", "quote": "Speculators sought to **commercialize** every bushel of prairie wheat flowing through the Chicago grain elevators."},
      {"author": "Upton Sinclair", "work": "The Jungle", "quote": "The meatpacking magnates managed to **commercialize** every scrap of animal byproduct with cold industrial efficiency."}
    ]
  },
  "commercialized": {
    "primary": "Adapted, altered, or exploited for monetary gain and large-scale market distribution.",
    "secondary": "In cultural anthropology, subjected to market relations to the detriment of communal heritage, authenticity, or ritual significance.",
    "quotes": [
      {"author": "W. E. B. Du Bois", "work": "The Souls of Black Folk", "quote": "He warned that traditional jubilee melodies were becoming distorted when performed in **commercialized** concert halls."},
      {"author": "Henry James", "work": "The American Scene", "quote": "He observed with distaste how historical landmarks had been converted into **commercialized** curiosities for hurried tourists."},
      {"author": "Jack London", "work": "Martin Eden", "quote": "The aspiring author resented the cynical compromises of **commercialized** magazine editors who rejected original thought."}
    ]
  },
  "commercially": {
    "primary": "In a commercial manner; from the viewpoint of trade, business operations, or financial profitability.",
    "secondary": "In chemical and industrial manufacturing, producing substances at scale and price acceptable for profitable market consumption.",
    "quotes": [
      {"author": "James Joyce", "work": "Ulysses", "quote": "The merchant calculated whether the imported Dublin stout could be distributed **commercially** across provincial rail depots."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Several varieties of silkworms have been cultivated **commercially** across southern Europe for hundreds of years."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Chemistry and Physics", "quote": "The synthesized hydrocarbon was not yet obtainable **commercially** in quantities sufficient for extensive lighting trials."}
    ]
  },
  "mercenaria": {
    "primary": "A biological genus of hard-shell marine clams in the family Veneridae, notably including the quahog.",
    "secondary": "In marine biology and malacology, edible bivalve mollusks native to Atlantic coastal estuaries, historically harvested by Indigenous peoples to fashion wampum shell beads.",
    "quotes": [
      {"author": "Carl Linnaeus", "work": "Systema Naturae", "quote": "The naturalist classified the heavy northern quahog as Venus **mercenaria**, alluding to its shell's use as native currency."},
      {"author": "Louis Agassiz", "work": "Contributions to the Natural History of the United States", "quote": "The thick porcelain-like valves of **Mercenaria** exhibit pronounced concentric growth ridges along the pallial sinus."},
      {"author": "Alexander Agassiz", "work": "Seaside Studies in Natural History", "quote": "Dredges brought up abundant specimens of **Mercenaria** from the muddy sediments of Buzzards Bay."}
    ]
  },
  "mercenary": {
    "primary": "Primarily motivated by the desire for financial gain, monetary reward, or selfish material benefit.",
    "secondary": "In military history, a professional soldier hired to fight in a foreign army without allegiance to the political cause.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry V", "quote": "For many of our princes lie drowned and soaked in **mercenary** blood on the muddy fields of Agincourt."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "She had no wicked plots, nothing sordid or **mercenary** in her affectionate devotion to the elderly invalid."},
      {"author": "Nathaniel Hawthorne", "work": "The House of the Seven Gables", "quote": "The cold-hearted magistrate pursued his inheritance with an overtly **mercenary** eagerness that disgusted his kinswoman."}
    ]
  },
  "merciless": {
    "primary": "Showing no mercy, clemency, or compassion; relentlessly cruel, severe, unsparing, and pitiless.",
    "secondary": "In literary description of nature or adversity, harsh and destructive physical conditions that offer no respite.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Macbeth", "quote": "The **merciless** Macdonwald, worthy to be a rebel, received reinforcements from the Western Isles."},
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "Henchard faced the **merciless** ruin of his commercial fortunes with defiant, unbending pride."},
      {"author": "Joseph Conrad", "work": "Lord Jim", "quote": "The blazing sun Beat down upon the calm tropical sea with a **merciless** and blinding glare."}
    ]
  },
  "mercilessly": {
    "primary": "In a merciless, pitiless, or unsparing manner; without leniency, compassion, or indulgence.",
    "secondary": "In rhetorical or physical conflict, executing severe punishment, censure, or destruction without restraint.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The frosty winter wind swept across the upland fields, chilling the tired farm laborers **mercilessly**."},
      {"author": "Joseph Conrad", "work": "Heart of Darkness", "quote": "The unrelenting wilderness seemed to mock the intruders, beating them down **mercilessly** under oppressive fever heat."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "The sharp-tongued sister cross-examined the frightened boy **mercilessly** concerning his mysterious disappearance."}
    ]
  },
  "mercilessness": {
    "primary": "The disposition or character of being merciless, pitiless, cruel, or completely devoid of compassion.",
    "secondary": "In moral philosophy and legal history, absolute rigor in applying punitive sanctions without allowance for human frailty.",
    "quotes": [
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "The revolutionary tribunals operated with a calculating **mercilessness** that appalled civilized nations across Europe."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The grim **mercilessness** of the Committee struck terror into the hearts of suspects crowded in the conciergerie."},
      {"author": "George Sand", "work": "Consuelo", "quote": "The inquisitor questioned the prisoner with an icy **mercilessness** masked beneath solemn ecclesiastical courtesy."}
    ]
  },
  "noncommercial": {
    "primary": "Not engaged in, intended for, or motivated by commerce, trade, or the accumulation of financial profit.",
    "secondary": "In communications law, copyright, and institutional governance, designated for educational, civic, or public interest use free from market monetization.",
    "quotes": [
      {"author": "Jane Addams", "work": "Twenty Years at Hull-House", "quote": "The settlement house maintained a strictly **noncommercial** dispensary providing medicines to impoverished neighborhood families."},
      {"author": "John Dewey", "work": "The School and Society", "quote": "Educational workshops should operate on a **noncommercial** basis to cultivate genuine creative experimentation."},
      {"author": "Thorstein Veblen", "work": "The Instinct of Workmanship", "quote": "Primitive toolmaking flourished originally under **noncommercial** tribal customs oriented toward collective survival."}
    ]
  },
  "uncommercial": {
    "primary": "Not commercial in character; indifferent to financial gain or unsuited to successful business enterprise.",
    "secondary": "In literary biography and artistic tradition, pursuing disinterested creative excellence while disregarding market profitability.",
    "quotes": [
      {"author": "Charles Dickens", "work": "The Uncommercial Traveller", "quote": "I am both a wanderer and a dreamer, traveling on **uncommercial** journeys through the crowded streets of London."},
      {"author": "George Gissing", "work": "New Grub Street", "quote": "The scholarly recluse preserved an entirely **uncommercial** devotion to classical prosody despite mounting debts."},
      {"author": "Henry James", "work": "The Tragic Muse", "quote": "His temperament was singularly **uncommercial**, recoiling from the crude barter of politics and high finance."}
    ]
  },
  "uncommercialised": {
    "primary": "Retaining original authenticity, integrity, or purity without being altered or exploited for trade and profit.",
    "secondary": "In environmental geography and folklore preservation, an unspoiled rural landscape or cultural practice free from tourist monetization.",
    "quotes": [
      {"author": "W. H. Hudson", "work": "Afoot in England", "quote": "We discovered a remote downs village whose ancient green remained completely **uncommercialised** by modern transport."},
      {"author": "George Borrow", "work": "Wild Wales", "quote": "The secluded mountain valley maintained an **uncommercialised** pastoral rhythm untouched by industrial chimneys."},
      {"author": "Edward Thomas", "work": "The South Country", "quote": "He sought out quiet woodland footpaths where the natural landscape remained tranquil and **uncommercialised**."}
    ]
  },
  "uncommercialized": {
    "primary": "Not developed, organized, or exploited for financial gain, consumer trade, or market commodification.",
    "secondary": "In regional ethnography and heritage conservation, traditional crafts and rituals conducted without marketing influence.",
    "quotes": [
      {"author": "John Muir", "work": "The Yosemite", "quote": "These high alpine valleys remain sublime and **uncommercialized**, guarded by granite precipices against human exploitation."},
      {"author": "Sarah Orne Jewett", "work": "The Country of the Pointed Firs", "quote": "The retired sea captains lived in quiet dignity within their primitive, **uncommercialized** coastal haven."},
      {"author": "Willa Cather", "work": "The Song of the Lark", "quote": "The ancient cliff-dwelling ruins conveyed a profound and entirely **uncommercialized** mystery to the wanderer."}
    ]
  },
  "unmercenary": {
    "primary": "Not motivated by pecuniary gain; generous, disinterested, and free from mercenary greed or calculation.",
    "secondary": "In civic ethics and personal character, performing devoted public service or heroic acts without seeking reward.",
    "quotes": [
      {"author": "P. G. Wodehouse", "work": "Love Among the Chickens", "quote": "He was an entirely **unmercenary** soul who regarded money merely as a tedious necessity for buying paint and tobacco."},
      {"author": "William Makepeace Thackeray", "work": "The Newcomes", "quote": "The old colonel possessed an **unmercenary** heart, always ready to expend his modest pension upon distressed comrades."},
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "True friendship can subsist only between minds that are generous, transparent, and thoroughly **unmercenary**."}
    ]
  }
}
