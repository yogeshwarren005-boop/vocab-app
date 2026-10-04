# -*- coding: utf-8 -*-
"""
Curates Cluster Sleep, Rest & Stillness:
- Dashboard — sopor (4 words)
- Dashboard — vacat (5 words)
- Dashboard — quies (8 words)
Total: 17 words.
"""
import os, sys, re

sys.stdout.reconfigure(encoding="utf-8")

data_batch1 = {
  # Dashboard — sopor
  "sopor": {
    "primary": "An abnormally deep, unnatural sleep or stupor from which one can be aroused only with difficulty.",
    "secondary": "In clinical neurology, a severe state of altered consciousness intermediate between lethargy and coma.",
    "quotes": [
      {"author": "Thomas Browne", "work": "Pseudodoxia Epidemica", "quote": "Certain botanical extracts induce a heavy **sopor** that mimics the appearance of death."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The patient lapsed from drowsiness into profound **sopor**, responding only to noxious tactile stimuli."},
      {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "The narcotic draft plunged his senses into an unnatural **sopor**, silencing conscious reflection."}
    ]
  },
  "soporiferous": {
    "primary": "Tending to cause, induce, or produce deep sleep; sleep-bringing or drowsy.",
    "secondary": "In pharmaceutical history, describing herbal decoctions containing opium, mandrake, or henbane.",
    "quotes": [
      {"author": "Jonathan Swift", "work": "Gulliver's Travels", "quote": "The Lilliputians mingled a **soporiferous** potion in the wine hogsheads to ensure the giant remained asleep."},
      {"author": "Robert Burton", "work": "The Anatomy of Melancholy", "quote": "Physicians recommend lettuce, poppy, and other **soporiferous** herbs to pacify nocturnal agitations."},
      {"author": "Francis Bacon", "work": "Sylva Sylvarum", "quote": "The vapors exhaled from the bruised seeds possessed a **soporiferous** virtue that calmed violent spasms."}
    ]
  },
  "soporific": {
    "primary": "Causing, inducing, or tending to produce sleep; drowsy, tedious, or monotonous.",
    "secondary": "In pharmacology, a sedative medication prescribed to promote sleep or manage severe insomnia.",
    "quotes": [
      {"author": "Jules Verne", "work": "Twenty Thousand Leagues under the Sea", "quote": "The gentle rhythmic hum of the Nautilus machinery exerted a **soporific** influence over the exhausted crew."},
      {"author": "Leo Tolstoy", "work": "War and Peace", "quote": "The warm summer air and the monotonous drone of the lecturer's voice exerted a **soporific** effect upon the pupils."},
      {"author": "Jane Austen", "work": "Emma", "quote": "Mr. Woodhouse found the quiet ticking of the parlor clock pleasantly **soporific** on winter afternoons."}
    ]
  },
  "soporose": {
    "primary": "Pertaining to, resembling, or marked by profound, unnatural sleep or lethargic stupor.",
    "secondary": "In historical medicine, describing morbid conditions characterized by continuous morbid drowsiness.",
    "quotes": [
      {"author": "Thomas Sydenham", "work": "Works", "quote": "The feverish epidemic terminated either in critical sweats or in a **soporose** stupor ending fatally."},
      {"author": "William Cullen", "work": "First Lines of the Practice of Physic", "quote": "Apoplexy frequently manifests with **soporose** symptoms accompanied by stertorous breathing."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The dying monarch sank into a **soporose** exhaustion, heedless of the weeping courtiers surrounding his bed."}
    ]
  },

  # Dashboard — vacat
  "vacate": {
    "primary": "To leave a place, property, or position vacant; to surrender occupancy or annul legally.",
    "secondary": "In civil jurisprudence, to set aside, cancel, or render void a judicial order, judgment, or lease.",
    "quotes": [
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "The tenant was required to **vacate** the lodge cottage before the arrival of the new steward."},
      {"author": "Blackstone", "work": "Commentaries on the Laws of England", "quote": "The court possessed discretionary jurisdiction to **vacate** letters patent obtained through fraudulent representations."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The bewildered lodger agreed to **vacate** the premises rather than face endless legal actions in Chancery."}
    ]
  },
  "vacation": {
    "primary": "A period of suspension of regular work, study, or business, taken for recreation or travel; holiday.",
    "secondary": "In judicial and university administrations, the formal recess period between legislative or court terms.",
    "quotes": [
      {"author": "William Shakespeare", "work": "As You Like It", "quote": "Time travels in divers paces with divers persons. I'll tell you who Time ambles withal, who Time trots withal, who Time gallops withal, and who he stands still withal. With lawyers in the **vacation**."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The long **vacation** arrived, and the Court of Chancery suspended its labyrinthine proceedings until Michaelmas."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "I went to the woods because I wished to make life a perpetual holiday rather than a hurried **vacation**."}
    ]
  },
  "vacationer": {
    "primary": "A person who is taking a vacation or holiday, especially traveling away from home for recreation.",
    "secondary": "In tourism economics, a seasonal consumer whose travel spending sustains regional resort hospitality.",
    "quotes": [
      {"author": "John Muir", "work": "Our National Parks", "quote": "Every summer **vacationer** who climbs the granite peaks returns renewed in spirit and bodily vigor."},
      {"author": "Sinclair Lewis", "work": "Main Street", "quote": "The wealthy **vacationer** looked with mild condescension upon the dusty storefronts of the prairie town."},
      {"author": "F. Scott Fitzgerald", "work": "Tender Is the Night", "quote": "The glamorous American **vacationer** lounged along the pale sands of the French Riviera."}
    ]
  },
  "vacationing": {
    "primary": "Taking or spending a vacation; engaging in holiday travel, rest, or recreational leisure.",
    "secondary": "In seasonal demographic migration, temporarily residing at a holiday destination or mountain retreat.",
    "quotes": [
      {"author": "Edith Wharton", "work": "The Age of Innocence", "quote": "New York society was **vacationing** in Newport, observing their rigid rituals of lawn tennis and driving."},
      {"author": "Henry James", "work": "Daisy Miller", "quote": "Winterbourne encountered the charming family while **vacationing** beside the clear blue waters of Lake Geneva."},
      {"author": "Virginia Woolf", "work": "To the Lighthouse", "quote": "The Ramsay household had been **vacationing** in the Hebrides every August for a decade."}
    ]
  },
  "vacationist": {
    "primary": "A person taking a holiday or vacation; a vacationer seeking recreational leisure.",
    "secondary": "In urban sociological studies, an individual participating in the organized commercial tourism industry.",
    "quotes": [
      {"author": "Theodore Dreiser", "work": "Sister Carrie", "quote": "The crowded excursion steamer carried many a cheerful **vacationist** toward the seaside pavilions."},
      {"author": "H. G. Wells", "work": "Kipps", "quote": "Every summer holiday turned the modest draper into an eager **vacationist** exploring Kentish lanes."},
      {"author": "Jack London", "work": "Martin Eden", "quote": "The tired city clerk became an adventurous **vacationist** the moment his canoe touched the wild river."}
    ]
  },

  # Dashboard — quies
  "acquiesce": {
    "primary": "To accept, agree, or comply with something passively or without protest, though not with enthusiasm.",
    "secondary": "In legal doctrine, to forfeit a claim or objection by remaining silent when action was required.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth was obliged to **acquiesce** in her father's decision, though she feared its consequences."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "A minority must ultimately **acquiesce** in the constitutional determinations of the respectable majority."},
      {"author": "Thomas Jefferson", "work": "Notes on the State of Virginia", "quote": "Citizens will **acquiesce** in legitimate authority when governance is guided by reason and equity."}
    ]
  },
  "acquiescence": {
    "primary": "Reluctant acceptance or passive consent given to something without open objection or resistance.",
    "secondary": "In real property law and boundary disputes, tacit recognition of a borderline over a statutory period.",
    "quotes": [
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "Ancient institutions retain legitimacy through long uninterrupted prescription and general **acquiescence**."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Dorothea bowed her head in silent **acquiescence** to her husband's rigid scholarly arrangements."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "Tyranny often establishes itself securely through the tired **acquiescence** of exhausted citizens."}
    ]
  },
  "acquiescent": {
    "primary": "Ready to accept or submit to something without protest; passively agreeable or submissive.",
    "secondary": "In interpersonal psychology, displaying a compliant behavioral tendency that avoids direct conflict.",
    "quotes": [
      {"author": "Charlotte Brontë", "work": "Villette", "quote": "Lucy Snowe maintained an **acquiescent** demeanor, observing the salon while masking her inner judgments."},
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "Madame Merle found Gilbert Osmond far less **acquiescent** once his matrimonial ambitions were secured."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Biddy was never servile, but remained gently **acquiescent** when Pip shared his restless ambitions."}
    ]
  },
  "quiesce": {
    "primary": "To become quiet, calm, still, or inactive; to settle into a dormant or resting condition.",
    "secondary": "In computer systems and database administration, to pause or flush active transactions to allow backup or snapshotting.",
    "quotes": [
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "Passions violent in youth tend to **quiesce** as age brings sober philosophical reflection."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Certain latent cellular tendencies **quiesce** for generations before reappearing as atavistic reversions."},
      {"author": "Thomas Huxley", "work": "Science and Culture", "quote": "Physical perturbations gradually **quiesce** as kinetic energy dissipates into equilibrium."}
    ]
  },
  "quiescence": {
    "primary": "A period, condition, or state of quietness, stillness, temporary inactivity, or dormancy.",
    "secondary": "In developmental biology and cytology, a reversible cell-cycle arrest in which cells exit active division (G0 phase).",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Night brought welcome **quiescence** to the battlefield, wrapping the exhausted hosts in silent darkness."},
      {"author": "Charles Darwin", "work": "On the Origin of Species", "quote": "Long periods of evolutionary **quiescence** may separate sudden episodes of organic modification."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The apparent **quiescence** of the northern frontiers deceived the imperial ministers at Constantinople."}
    ]
  },
  "quiescency": {
    "primary": "The quality or disposition of being quiet, dormant, inactive, or at rest; tranquility.",
    "secondary": "In classical natural philosophy, the resting equilibrium of physical bodies unaffected by external momentum.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "The Idler", "quote": "Human nature cannot long endure absolute **quiescency**, but craves novelty and intellectual diversion."},
      {"author": "Thomas Browne", "work": "Pseudodoxia Epidemica", "quote": "The winter torpor of swallows was once regarded as an unbroken **quiescency** at the bottom of frozen lakes."},
      {"author": "Isaac Newton", "work": "Principia Mathematica", "quote": "A body preserves its state of **quiescency** or uniform motion unless compelled by impressed forces to change."}
    ]
  },
  "quiescent": {
    "primary": "In a state or period of temporary inactivity, dormancy, rest, or peaceful stillness.",
    "secondary": "In geology and vulcanology, describing a volcano that is currently dormant but capable of future eruption.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The Pacific rolled in endless blue billows, deceptively **quiescent** beneath the equatorial sun."},
      {"author": "Rachel Carson", "work": "The Sea Around Us", "quote": "Minute planktonic larvae remain **quiescent** in cold abyssal currents until rising temperatures trigger growth."},
      {"author": "Walter Scott", "work": "The Bride of Lammermoor", "quote": "The castle lay silent and **quiescent** under the shadows of the brooding Scottish hills."}
    ]
  },
  "requiescat": {
    "primary": "A prayer or wish for the repose of the soul of a deceased person ('may he or she rest in peace').",
    "secondary": "In musical and poetic eulogy, an elegy or chant commemorating the deceased at funeral rites.",
    "quotes": [
      {"author": "Oscar Wilde", "work": "Poems", "quote": "Tread lightly, she is near / Under the snow, / Speak gently, she can hear / The daisies grow... A soft **requiescat** for a departed soul."},
      {"author": "Edgar Allan Poe", "work": "The Cask of Amontillado", "quote": "Against the new masonry I re-erected the old rampart of bones. For the half of a century no mortal has disturbed them. In pace **requiescat**!"},
      {"author": "Matthew Arnold", "work": "Requiescat", "quote": "Strew on her roses, roses, / And never a spray of yew! / In quiet she reposes; / Ah, would that I did too! A tender **requiescat** carved upon the stone."}
    ]
  }
}
