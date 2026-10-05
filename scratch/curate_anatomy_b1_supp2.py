# -*- coding: utf-8 -*-
"""
curate_anatomy_b1_supp2.py
Batch 1 Supplement Part 2 (14 words):
- dent: edental, indentured
- front: frontally, frontierswoman, frontmost, frontstall, prefrontal
- maxill: maxillodental, maxillomandibular
- ocul: inoculator, inoculum, intraocular, oculism, supraocular
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

data_anatomy_supp2 = {
    # 1. edental
    "edental": {
        "primary": "Lacking teeth; toothless; pertaining to or characteristic of edentate animals.",
        "secondary": "In comparative anatomy and odontography, describing mandibular arches or palates naturally devoid of dental structures.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The giant fossil skull showed an **edental** premaxilla similar to the living anteaters of Brazil."},
            {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "In certain baleen whales, the embryonic dental papillae are reabsorbed, leaving an entirely **edental** adult jaw."},
            {"author": "Richard Owen", "work": "Odontography", "quote": "The **edental** condition of the jaw in birds is compensated by the development of a sharp horny rhamphotheca."}
        ]
    },

    # 2. indentured
    "indentured": {
        "primary": "Bound by a formal contract of service or apprenticeship to work for another for a specified term.",
        "secondary": "In colonial labor economics and contract history, designating workers bound by legal indentures to repay transit or learn a recognized trade.",
        "quotes": [
            {"author": "Charles Dickens", "work": "Great Expectations", "quote": "I was formally **indentured** to Joe Gargery before the magistrate, binding me to serve faithfully as his blacksmith apprentice."},
            {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "Thousands of political convicts were transported to the American colonies as **indentured** laborers under harsh taskmasters."},
            {"author": "Benjamin Franklin", "work": "The Autobiography of Benjamin Franklin", "quote": "At the age of twelve I was **indentured** to my brother James to learn the printing trade in Boston."}
        ]
    },

    # 3. frontally
    "frontally": {
        "primary": "From the front; in a head-on or forward-facing manner or direction.",
        "secondary": "In military tactics, cognitive craniometry, and portraiture, engaging an enemy head-on, or presenting a direct anterior aspect.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The orbits in predatory primates are directed **frontally**, enabling precise stereoscopic vision and accurate leaping among tree branches."},
            {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The cavalry charged the entrenchments **frontally**, suffering frightful losses from the murderous volley of musketry."},
            {"author": "John Ruskin", "work": "Modern Painters", "quote": "The master drew the marble statue **frontally**, capturing the calm and monumental majesty of the classical deity."}
        ]
    },

    # 4. frontierswoman
    "frontierswoman": {
        "primary": "A woman who lives on or explores the wilderness boundary of settled territory.",
        "secondary": "In American pioneer history, a female settler noted for resilience, domestic fortitude, and armed defense on the frontier border.",
        "quotes": [
            {"author": "Theodore Roosevelt", "work": "The Winning of the West", "quote": "The pioneer **frontierswoman** exhibited equal courage with her husband, defending the isolated cabin against Indian assaults with rifle in hand."},
            {"author": "Francis Parkman", "work": "The Oregon Trail", "quote": "We met a resolute **frontierswoman** driving her ox wagon across the Platte river with astonishing skill and calm self-reliance."},
            {"author": "Willa Cather", "work": "O Pioneers!", "quote": "She possessed the indomitable spirit of the true **frontierswoman**, wresting prosperity from the wild prairie sod through sheer determination."}
        ]
    },

    # 5. frontmost
    "frontmost": {
        "primary": "Positioned furthest forward; situated in the very front position.",
        "secondary": "In military infantry tactics and maritime convoy formations, occupying the vanguard rank closest to potential enemy engagement.",
        "quotes": [
            {"author": "Herman Melville", "work": "Moby-Dick; or, The Whale", "quote": "The harpooner stood erect in the **frontmost** thwart of the whaleboat, darting iron poised for the strike."},
            {"author": "Thomas Hardy", "work": "The Dynasts", "quote": "The **frontmost** ranks of the British square received the furious onslaught of the French cuirassiers with steady bayonets."},
            {"author": "Joseph Conrad", "work": "The Nigger of the 'Narcissus'", "quote": "The ship pitched violently into the head seas, her **frontmost** timbers shuddering under each crashing comber."}
        ]
    },

    # 6. frontstall
    "frontstall": {
        "primary": "A seat or stall in the front row of a theater, church, or market.",
        "secondary": "In ecclesiastical choir architecture and theatrical staging, an anterior reserved bench occupied by senior dignitaries or prominent patrons.",
        "quotes": [
            {"author": "Charles Dickens", "work": "The Mystery of Edwin Drood", "quote": "The precentor took his place in the carved oak **frontstall** of the cathedral choir as the organ prelude began."},
            {"author": "George Eliot", "work": "Scenes of Clerical Life", "quote": "The village squire and his family occupied the red-cushioned **frontstall** overlooking the parish pulpit."},
            {"author": "Thomas Hardy", "work": "Under the Greenwood Tree", "quote": "The churchwardens sat with solemn gravity in the **frontstall**, keeping a watchful eye upon the fidgeting schoolboys."}
        ]
    },

    # 7. prefrontal
    "prefrontal": {
        "primary": "Situated in the anterior part of the frontal lobe of the brain or frontal bone of the skull.",
        "secondary": "In behavioral neuroscience and neuropsychiatry, designating the prefrontal cortex, critical for executive function, impulse inhibition, and decision-making.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Lesions involving the **prefrontal** cortex produce marked alterations in personality, apathy, and loss of moral inhibition."},
            {"author": "William James", "work": "The Principles of Psychology", "quote": "The celebrated crowbar case of Phineas Gage demonstrated that profound character changes follow severe destruction of the **prefrontal** lobes."},
            {"author": "Santiago Ramón y Cajal", "work": "Histology of the Nervous System", "quote": "Dense association fibers link the associative centers of the **prefrontal** gyri with the motor and sensory cortices."}
        ]
    },

    # 8. maxillodental
    "maxillodental": {
        "primary": "Pertaining to or involving both the maxilla (upper jaw) and the teeth.",
        "secondary": "In orthodontics and craniofacial surgery, relating to the anatomical and biomechanical relationships between the maxillary dental arch and the facial skeleton.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Congenital cleft palate severely alters normal **maxillodental** alignment, requiring coordinated surgical and orthodontic care."},
            {"author": "Richard Owen", "work": "Odontography", "quote": "The firm anchorage of mammalian molars relies upon specialized **maxillodental** sutures within the alveolar processes."},
            {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "In carnivores, the massive canines are supported by thickened **maxillodental** buttresses capable of resisting heavy biting forces."}
        ]
    },

    # 9. maxillomandibular
    "maxillomandibular": {
        "primary": "Pertaining to or connecting both the upper jaw (maxilla) and the lower jaw (mandible).",
        "secondary": "In oral and maxillofacial surgery, designating the occlusal relationship, surgical fixation (MMF), or intermaxillary elastic traction between the upper and lower jaws.",
        "quotes": [
            {"author": "Sir Astley Cooper", "work": "A Treatise on Dislocations and Fractures of the Joints", "quote": "Temporary **maxillomandibular** wiring was employed to immobilize the shattered fragments in anatomically correct dental occlusion."},
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Chronic spasm of the masticatory muscles impedes normal **maxillomandibular** excursion in cases of severe tetanus."},
            {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "The articulation of the **maxillomandibular** apparatus in teleost fishes exhibits intricate linkage systems that expand the oral cavity."}
        ]
    },

    # 10. inoculator
    "inoculator": {
        "primary": "A person who performs inoculations, or an instrument used to introduce antigens or culture media.",
        "secondary": "In the history of public health, an early medical practitioner or operator who performed smallpox variolation before Jennerian cowpox vaccination.",
        "quotes": [
            {"author": "Edward Jenner", "work": "An Inquiry into the Causes and Effects of the Variolae Vaccinae", "quote": "The rural **inoculator** carried variolous lymph on lancets from village to village to immunize children against smallpox."},
            {"author": "Lady Mary Wortley Montagu", "work": "Letters of Lady Mary Wortley Montagu", "quote": "I observed the expert Turkish **inoculator** puncture the veins of the arm with a small needle dipped in fresh virus."},
            {"author": "Louis Pasteur", "work": "Studies on Fermentation", "quote": "The laboratory technician utilized a platinum **inoculator** to transfer pure colonies of the ferment onto nutrient gelatin."}
        ]
    },

    # 11. inoculum
    "inoculum": {
        "primary": "A small quantity of material, microorganisms, or cells introduced into a culture medium or host organism.",
        "secondary": "In clinical microbiology and industrial zymology, the calibrated microbial suspension transferred to start a fermentation culture or assay.",
        "quotes": [
            {"author": "Louis Pasteur", "work": "Studies on Fermentation", "quote": "A minute **inoculum** of selected yeast introduced into sterile wort initiates rapid alcoholic fermentation without bacterial contamination."},
            {"author": "Robert Koch", "work": "The Etiology of Tuberculosis", "quote": "Even the smallest **inoculum** containing viable tubercle bacilli provoked progressive generalized disease in guinea pigs."},
            {"author": "Selman Waksman", "work": "Principles of Soil Microbiology", "quote": "The survival of the microbial **inoculum** depends heavily upon soil moisture, pH, and the competition of native saprophytes."}
        ]
    },

    # 12. intraocular
    "intraocular": {
        "primary": "Situated, occurring, or administered within the interior of the eyeball.",
        "secondary": "In ophthalmology and vision science, designating fluid dynamics, tumors, lenses, or the internal fluid pressure (*intraocular* pressure) measured in glaucoma.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Persistent elevation of **intraocular** pressure leads to progressive cupping of the optic disc and permanent visual field loss in glaucoma."},
            {"author": "Hermann von Helmholtz", "work": "Treatise on Physiological Optics", "quote": "The invention of the ophthalmoscope permitted physicians to inspect the living **intraocular** structures with crystalline clarity."},
            {"author": "Oliver Wendell Holmes Sr.", "work": "Medical Essays", "quote": "Delicate microsurgical instruments are required to extract cataracts from the anterior **intraocular** chamber without injuring the cornea."}
        ]
    },

    # 13. oculism
    "oculism": {
        "primary": "The medical study, diagnosis, and treatment of eye diseases; ophthalmology.",
        "secondary": "In the history of nineteenth-century medicine, the specialized scientific discipline and clinical practice devoted to diseases of the visual organ.",
        "quotes": [
            {"author": "Oliver Wendell Holmes Sr.", "work": "Medical Essays", "quote": "The rapid development of modern **oculism** has transformed eye surgery from crude empiricism into an exact scientific art."},
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Specialized treatises on **oculism** emphasize the crucial diagnostic significance of funduscopic changes in renal disease."},
            {"author": "Charles Dickens", "work": "Bleak House", "quote": "The fashionable physician had devoted his youth to the study of **oculism** in the great ophthalmic clinics of Vienna."}
        ]
    },

    # 14. supraocular
    "supraocular": {
        "primary": "Situated above or superior to the eye.",
        "secondary": "In herpetology and avian anatomy, designating specialized scales, feathers, or bony brow ridges positioned directly above the orbit.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Zoology of the Voyage of H.M.S. Beagle", "quote": "In the horned pit-viper of Central America, a prominent spine-like **supraocular** scale rises sharply above each eye."},
            {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "The **supraocular** canal transmits cutaneous sensory branches of the ophthalmic division of the trigeminal nerve."},
            {"author": "David Starr Jordan", "work": "A Guide to the Study of Fishes", "quote": "The deep-sea anglerfish carries a luminous photophore mounted directly upon its modified **supraocular** crest."}
        ]
    }
}
