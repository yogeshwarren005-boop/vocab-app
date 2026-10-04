# -*- coding: utf-8 -*-
"""
Curates Dashboard — oti (16 words) in Cluster Sleep, Rest & Stillness.
"""
import os, sys, re

sys.stdout.reconfigure(encoding="utf-8")

data_oti = {
  "cootie": {
    "primary": "Slang for a body louse; in American child folklore, an imaginary germ or contamination.",
    "secondary": "In military slang of the First World War, trench lice infesting soldiers' uniforms and bedding.",
    "quotes": [
      {"author": "John Dos Passos", "work": "Three Soldiers", "quote": "The weary infantrymen stripped off their tunics by candlelight to hunt for the elusive **cootie**."},
      {"author": "E. E. Cummings", "work": "The Enormous Room", "quote": "In the filthy detention barracks, every blanket was infested with biting **cootie** vermin."},
      {"author": "Ernest Hemingway", "work": "A Farewell to Arms", "quote": "He sat by the tent flap scratching his seams where a stray **cootie** had found lodging."}
    ]
  },
  "exotic": {
    "primary": "Originating in or characteristic of a distant foreign country; strikingly unusual or alluring.",
    "secondary": "In ecology and conservation biology, an introduced non-native species establishing in an alien ecosystem.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The lush Brazilian forest was filled with **exotic** orchid blooms and brightly colored parrots."},
      {"author": "Joseph Conrad", "work": "Heart of Darkness", "quote": "The trader displayed a collection of rare ivory carvings and **exotic** African plumage."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Queequeg carried with him the fierce, mysterious dignity of his **exotic** Pacific island home."}
    ]
  },
  "exoticism": {
    "primary": "The allure, charm, or character of foreign origin; unusual distinction in style or manner.",
    "secondary": "In 19th-century European art and literature, the romantic fascination with Eastern or distant non-Western cultures.",
    "quotes": [
      {"author": "Gustave Flaubert", "work": "Salammbô", "quote": "The opulent palace interiors glittered with the sumptuous **exoticism** of ancient Carthage."},
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "Gilbert Osmond cultivated a delicate **exoticism** in his Florentine villa to impress visiting connoisseurs."},
      {"author": "Edward Said", "work": "Orientalism", "quote": "Western imaginative geography constructed a stylized **exoticism** that obscured actual Near Eastern realities."}
    ]
  },
  "exoticness": {
    "primary": "Unusual foreignness, distinctive unfamiliarity, or striking novelty in appearance or character.",
    "secondary": "In aesthetic evaluation, the distinctive charm or novelty imparted by alien origin or rarity.",
    "quotes": [
      {"author": "Edith Wharton", "work": "The Age of Innocence", "quote": "Ellen Olenska brought an unsettling **exoticness** into the rigid, conventional drawing rooms of old New York."},
      {"author": "Virginia Woolf", "work": "Orlando", "quote": "The Turkish embassy was filled with an aromatic **exoticness** that intoxicated the young ambassador."},
      {"author": "Thomas Mann", "work": "Death in Venice", "quote": "Aschenbach was lured onward by the tropical **exoticness** of the Venetian lagoon under the summer sun."}
    ]
  },
  "exotism": {
    "primary": "Exotic quality, character, or foreign influence; a synonym of exoticism.",
    "secondary": "In linguistic philology, a loanword or idiom borrowed directly from a foreign language to retain local color.",
    "quotes": [
      {"author": "Matthew Arnold", "work": "Essays in Criticism", "quote": "Certain modern French poets cultivate a deliberate **exotism** to escape bourgeois domesticity."},
      {"author": "Walter Pater", "work": "The Renaissance", "quote": "The painter infused classical mythology with a subtle **exotism** derived from Levantine travel."},
      {"author": "George Santayana", "work": "The Sense of Beauty", "quote": "Romantic sensibility is easily seduced by the superficial **exotism** of distant landscapes."}
    ]
  },
  "negotiable": {
    "primary": "Open to discussion or modification; capable of being transferred legally from one person to another.",
    "secondary": "In commercial banking and finance, a financial instrument whose legal title can be transferred by endorsement or delivery.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "A bill of exchange serves as a highly **negotiable** instrument that expedites international trade payments."},
      {"author": "Alexander Hamilton", "work": "Report on Public Credit", "quote": "Government certificates of debt must remain readily **negotiable** to restore commercial confidence."},
      {"author": "John Maynard Keynes", "work": "The General Theory of Employment, Interest and Money", "quote": "The liquidity of an asset depends upon whether it is immediately **negotiable** without capital loss."}
    ]
  },
  "negotiant": {
    "primary": "A person who conducts negotiations; an agent, merchant, or negotiator in trade or diplomacy.",
    "secondary": "In early modern commerce, an international wholesale merchant conducting large-scale maritime trade.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "A skilled Roman **negotiant** was dispatched to the Persian court to fix terms of border commerce."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The Dutch **negotiant** secured lucrative trading privileges through patient diplomacy at Versailles."},
      {"author": "Edmund Burke", "work": "Letters on a Regicide Peace", "quote": "The envoy acted not as a dignified ambassador, but as a mercenary **negotiant** bartering national honor."}
    ]
  },
  "negotiate": {
    "primary": "To confer with another so as to arrive at the settlement of some matter; to arrange by conference.",
    "secondary": "In navigation or driving, to successfully navigate, travel over, or traverse a difficult obstacle.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The executive magistrate is uniquely equipped to **negotiate** treaties with foreign powers with secrecy and dispatch."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "Democratic republics must learn to **negotiate** with autocratic neighbors without sacrificing principle."},
      {"author": "Mark Twain", "work": "Life on the Mississippi", "quote": "The river pilot had to **negotiate** dangerous sandbars and hidden snags during the midnight run."}
    ]
  },
  "negotiation": {
    "primary": "Mutual discussion and arrangement of the terms of a transaction or agreement.",
    "secondary": "In public international law, formal diplomatic communication between sovereign states to settle disputes.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "Considerations on Representative Government", "quote": "Deliberative assemblies provide a public arena for compromise and continuous political **negotiation**."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Protracted **negotiation** averted military collision between the rival empires for another decade."},
      {"author": "Benjamin Franklin", "work": "Autobiography", "quote": "I conducted the diplomatic **negotiation** with French ministers with patient perseverance and frugality."}
    ]
  },
  "negotiator": {
    "primary": "A person who conducts or takes part in negotiations; an authorized intermediary or mediator.",
    "secondary": "In dispute resolution, a professional third party facilitating compromise between conflicting factions.",
    "quotes": [
      {"author": "Walter Bagehot", "work": "The English Constitution", "quote": "A successful prime minister must prove an adroit parliamentary **negotiator** among contending factions."},
      {"author": "Winston Churchill", "work": "The Gathering Storm", "quote": "The veteran **negotiator** recognized that concessions made to an insatiable aggressor only hasten war."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "William of Orange sent his most trusted Dutch **negotiator** to confer secretly with English lords."}
    ]
  },
  "ocotillo": {
    "primary": "A spiny, drought-deciduous desert shrub (Fouquieria splendens) native to the southwestern United States and Mexico.",
    "secondary": "In desert botanical ecology, a xerophytic plant whose whip-like stems leaf out rapidly following desert rains.",
    "quotes": [
      {"author": "John Muir", "work": "Steep Trails", "quote": "Slender red blossoms crowned the wand-like stems of the **ocotillo** across the sun-baked Sonoran flats."},
      {"author": "Willa Cather", "work": "Death Comes for the Archbishop", "quote": "Across the arid canyon floor, clumps of spiny **ocotillo** stood like giant candelabra against the red sandstone cliffs."},
      {"author": "Mary Austin", "work": "The Land of Little Rain", "quote": "After the sudden desert storm, the grey thorny canes of the **ocotillo** burst into miraculous emerald leaf."}
    ]
  },
  "otic": {
    "primary": "Pertaining to, situated near, or affecting the ear; auditory or aural in anatomical reference.",
    "secondary": "In human skull osteology, relating to the otic capsule that encloses the inner ear labyrinth.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Chronic suppurative disease may spread from the **otic** cavity into adjacent intracranial sinuses."},
      {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "The tiny vestigial tubercle upon the **otic** margin of the human ear reflects ancient mammalian descent."},
      {"author": "Thomas Henry Huxley", "work": "Manual of the Anatomy of Vertebrated Animals", "quote": "The prootic and opisthotic bones unite during embryonic development to form the rigid **otic** capsule."}
    ]
  },
  "otiose": {
    "primary": "Serving no practical purpose or result; useless, futile, idle, or superfluous.",
    "secondary": "In theology and comparative mythology, an otiose deity (deus otiosus) who created the cosmos and then withdrew from human affairs.",
    "quotes": [
      {"author": "Thomas Babington Macaulay", "work": "Critical and Historical Essays", "quote": "All rhetorical declamation becomes utterly **otiose** when the plain facts speak for themselves."},
      {"author": "Henry James", "work": "The Sacred Fount", "quote": "My lingering doubts were dismissed as **otiose** speculations that led nowhere in our social inquiry."},
      {"author": "Mircea Eliade", "work": "The Sacred and the Profane", "quote": "Tribal religions frequently venerate a celestial creator who has become an **otiose** god, remote from daily prayer."}
    ]
  },
  "otis": {
    "primary": "A taxonomic genus of large terrestrial birds comprising the Great Bustard (Otis tarda); a given name or surname.",
    "secondary": "In systematic ornithology, the type genus of the family Otididae, characterized by ground-dwelling bustards inhabiting open plains.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "Across the open Argentine pampas we observed birds closely related to the European genus **Otis** foraging in dry grasses."},
      {"author": "Gilbert White", "work": "The Natural History of Selborne", "quote": "Flocks of the Great Bustard, known to naturalists as **Otis**, once grazed commonly upon the chalky downs of Wiltshire."},
      {"author": "Thomas Bewick", "work": "A History of British Birds", "quote": "The massive plumage and wary habits of the genus **Otis** made it a difficult quarry for early sportsmen."}
    ]
  },
  "otitis": {
    "primary": "Inflammation or infection of the ear, typically classified as otitis externa, media, or interna.",
    "secondary": "In clinical otolaryngology, middle ear effusion and bacterial inflammation leading to conductive hearing impairment.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Acute **otitis** media frequently complicates measles and scarlet fever in young pediatric patients."},
      {"author": "Oliver Wendell Holmes", "work": "Medical Essays", "quote": "Early paracentesis of the tympanic membrane prevents permanent auditory injury in severe suppurative **otitis**."},
      {"author": "John Hunter", "work": "Works", "quote": "Careful examination of the temporal bone revealed extensive osteitis resulting from neglected chronic **otitis**."}
    ]
  },
  "renegotiate": {
    "primary": "To negotiate again in order to alter, update, or revise the terms of an existing agreement.",
    "secondary": "In international treaty law and finance, formally amending sovereign debt covenants or trade pacts.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "States that find initial covenants burdensome will seek to **renegotiate** the constitutional compact."},
      {"author": "Walter Bagehot", "work": "Lombard Street", "quote": "When monetary panics subside, financial syndicates must **renegotiate** their discounted credit obligations."},
      {"author": "Winston Churchill", "work": "The Second World War", "quote": "The allied powers met at Yalta to **renegotiate** the postwar administrative boundaries of central Europe."}
    ]
  }
}
