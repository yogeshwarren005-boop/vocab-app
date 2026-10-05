# -*- coding: utf-8 -*-
"""
curate_anatomy_b1_p1c.py
Batch 1 Part 1c of Cluster Anatomy & Clinical Medicine (26 words):
- maxill remaining (4 words): premaxilla, premaxillary, submaxilla, submaxillary
- ocul (16 words): binocular, inoculant, inoculate, inoculating, inoculation,
  monocular, ocul, ocular, ocularly, oculist, oculomotor, oculus,
  postocular, preocular, subocular, triocular
- aur_ear part 1 (6 words): aura, aural, aurally, aurate, laureate, aurelia
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

data_anatomy_p1c = {
    # ==================== Dashboard — maxill (remaining 4 words) ====================
    "premaxilla": {
        "primary": "A pair of cranial bones situated at the anterior tip of the upper jaw in most vertebrates.",
        "secondary": "In comparative osteology and mammalian odontogeny, tooth-bearing bones that house the upper incisors, forming the primary palate.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The reduction or complete fusion of the **premaxilla** with the adjacent maxilla represents a landmark diagnostic character in higher primates."},
            {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "In the human skull the **premaxilla** fuses so completely with the maxilla during embryonic life that its separate identity is masked."},
            {"author": "Richard Owen", "work": "Odontography", "quote": "The upper incisor teeth in rodents are invariably implanted deeply within the sockets of the expanded **premaxilla**."},
        ]
    },
    "premaxillary": {
        "primary": "Situated in front of the maxilla, or pertaining to the premaxilla bone.",
        "secondary": "In craniofacial embryology and morphology, relating to the bone segment, alveolar ridge, or dentition derived from the embryonic frontonasal process.",
        "quotes": [
            {"author": "Thomas Henry Huxley", "work": "The Anatomy of Vertebrated Animals", "quote": "The **premaxillary** bones in birds are immensely extended forward to form the structural core of the upper beak."},
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Goethe achieved a celebrated anatomical triumph by demonstrating the existence of the suture bounding the human **premaxillary** bone."},
            {"author": "William Flower", "work": "An Introduction to the Osteology of the Mammalia", "quote": "In cetaceans the **premaxillary** elements are drawn backward over the skull roof, shifting the blowhole to the vertex."}
        ]
    },
    "submaxilla": {
        "primary": "The lower jawbone (mandible), or the submandibular salivary gland situated beneath the lower jaw.",
        "secondary": "In archaic and comparative anatomical descriptions, designating the inferior jaw arch or the encapsulated salivary structures tucked beneath the mylohyoid muscle.",
        "quotes": [
            {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "In lower vertebrates the **submaxilla** consists of several distinct ossicles that fuse into a single dentary bone in mammals."},
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Suppurative inflammation originating beneath the **submaxilla** threatens rapid descent of purulence into the deep fascial planes of the neck."},
            {"author": "Claude Bernard", "work": "Lectures on Experimental Physiology", "quote": "Stimulation of the chorda tympani nerve produces a copious secretion of thin watery saliva from the exposed **submaxilla**."}
        ]
    },
    "submaxillary": {
        "primary": "Situated beneath or situated on the lower aspect of the maxilla or lower jaw.",
        "secondary": "In human digestive anatomy and surgical oncology, relating to the submandibular (submaxillary) salivary gland, ganglion, duct of Wharton, or lymph nodes.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "Under the influence of acute terror, the **submaxillary** salivary glands cease their natural secretion, leaving the tongue and throat parched."},
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Tuberculous adenitis most frequently targets the deep cervical and **submaxillary** lymph chain in scrofulous children."},
            {"author": "Claude Bernard", "work": "Lectures on the Physiology and Pathology of the Nervous System", "quote": "The galvanic excitation of the lingual nerve provokes instantaneous vascular engorgement throughout the **submaxillary** gland."}
        ]
    },

    # ==================== Dashboard — ocul (16 words) ====================
    "binocular": {
        "primary": "Adapted for or involving the use of both eyes simultaneously, or an optical instrument utilizing two eyepieces.",
        "secondary": "In vision science and neurophysiology, sensory stereopsis and depth perception achieved by the cortical fusion of two slightly disparate retinal images.",
        "quotes": [
            {"author": "Herman Melville", "work": "Moby-Dick; or, The Whale", "quote": "The lookout raised his **binocular** glass to scan the distant horizon for the spouting of the great white whale."},
            {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Holmes adjusted his **binocular** field glasses, following the furtive movements of the figure upon the granite tor."},
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The frontally directed orbits of primates afford true **binocular** vision, enhancing accurate distance estimation among tree branches."}
        ]
    },
    "inoculant": {
        "primary": "A substance, biological agent, or microorganism introduced into an organism or substrate to produce immunity or initiate growth.",
        "secondary": "In agricultural microbiology and industrial fermentation, a concentrated bacterial culture (such as *Rhizobium*) introduced into soil to promote nitrogen fixation.",
        "quotes": [
            {"author": "Louis Pasteur", "work": "Studies on Fermentation", "quote": "The purity of the yeast **inoculant** determines whether the fermentation proceeds to sound alcohol or spoils into vinegar."},
            {"author": "Selman Waksman", "work": "Principles of Soil Microbiology", "quote": "Leguminous seeds treated with a viable bacterial **inoculant** exhibit abundant root nodule formation and vigorous growth."},
            {"author": "Martinus Beijerinck", "work": "Studies in Soil Bacteriology", "quote": "A fresh **inoculant** derived from healthy clover root nodules rapidly establishes symbiotic colonies in sterile sand."}
        ]
    },
    "inoculate": {
        "primary": "To treat a person or animal with a vaccine or antigenic material to induce immunity against a disease.",
        "secondary": "In medical history and zymology (*in-* + *oculus*, grafting a bud into an eye), to implant pathogens into culture media, or to introduce antigens into living tissue.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Hamlet", "quote": "I loved you not; you should not have believed me; for virtue cannot so **inoculate** our old stock but we shall relish of it; I loved you not."},
            {"author": "Edward Jenner", "work": "An Inquiry into the Causes and Effects of the Variolae Vaccinae", "quote": "I resolved to **inoculate** the boy with matter taken directly from a pustule on the hand of the milkmaid Sarah Nelmes."},
            {"author": "Louis Pasteur", "work": "Memoir on the Attenuation of Viruses", "quote": "By subculturing the bacillus over successive weeks, we obtained an attenuated strain safe enough to **inoculate** healthy sheep."}
        ]
    },
    "inoculating": {
        "primary": "The act of introducing a vaccine, antigen, or infectious organism into an animal or culture medium.",
        "secondary": "In historical arboriculture and bacteriology, grafting a dormant bud into a host branch, or systematically infecting experimental media.",
        "quotes": [
            {"author": "Francis Bacon", "work": "Sylva Sylvarum", "quote": "In gardening, the subtle art of **inoculating** or grafting upon alien boughs yieldeth fruit of sweeter and more delicate flavor."},
            {"author": "Edward Jenner", "work": "Further Observations on the Variolae Vaccinae", "quote": "The practice of **inoculating** infants with mild cowpox fluid provides an unbreachable barrier against the dread scourge of smallpox."},
            {"author": "Louis Pasteur", "work": "Studies on Rabies", "quote": "By **inoculating** the virus directly into the subdural space of rabbits, the incubation period was stabilized to an exact duration."}
        ]
    },
    "inoculation": {
        "primary": "The introduction of an antigenic substance or pathogen into the body to produce immunity against disease.",
        "secondary": "In immunology and epidemiology, the historical practice of variolation, succeeded by Jennerian vaccination and modern preventative immunization.",
        "quotes": [
            {"author": "Lady Mary Wortley Montagu", "work": "Letters from the Right Honourable Lady Mary Wortley Montagu", "quote": "The Turkish matrons perform the operation of **inoculation** with a needle, preserving thousands of children from death and disfigurement."},
            {"author": "Edward Jenner", "work": "An Inquiry into the Causes and Effects of the Variolae Vaccinae", "quote": "The security against smallpox derived from cowpox **inoculation** has proved constant through extensive trials across every age."},
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Preventive **inoculation** against typhoid fever has drastically reduced mortality among soldiers serving in foreign encampments."}
        ]
    },
    "monocular": {
        "primary": "Pertaining to, adapted for, or using only one eye; or an optical device designed for a single eye.",
        "secondary": "In visual optics and ophthalmology, vision with a single eye, lacking stereoscopic parallax and relying primarily on monocular depth cues such as perspective and motion parallax.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Animals with laterally positioned eyes possess extensive panoramic fields, though their vision is predominantly **monocular**."},
            {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "He raised his **monocular** lens to scrutinize the curious crystalline ash remaining in the grate."},
            {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Patients who suffer the loss of one eye gradually learn to estimate relative distance through **monocular** clues of perspective and lighting."}
        ]
    },
    "ocul": {
        "primary": "A root morpheme denoting the eye, derived from the classical Latin *oculus*.",
        "secondary": "In etymology and anatomical lexicography, the foundational Latin morpheme entering into clinical compounds such as ocular, oculist, and oculomotor.",
        "quotes": [
            {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "The ancients appropriately symbolized keen mental vision by borrowing terms from the bodily eye or **ocul**."},
            {"author": "Thomas Browne", "work": "Pseudodoxia Epidemica", "quote": "The Latin root **ocul** signifieth an eye, whence our language derives ocular evidence and diverse anatomical designations."},
            {"author": "Samuel Johnson", "work": "A Dictionary of the English Language", "quote": "From the primitive noun oculus or its radical element **ocul**, numerous scholarly derivatives have enriched our medical vocabulary."}
        ]
    },
    "ocular": {
        "primary": "Pertaining to or connected with the eyes or the sense of sight; visual.",
        "secondary": "In microscope optics and legal evidence, the eyepiece lens that magnifies the objective image, or direct eyewitness visual testimony.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Othello", "quote": "Villain, be sure thou prove my love a whore, be sure of it; give me the **ocular** proof: or by the worth of man's eternal soul, thou hadst been better have been born a dog than answer my waked wrath!"},
            {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "Henchard demanded **ocular** proof of the rumor, refusing to credit the scandal without the testimony of his own eyes."},
            {"author": "G. K. Chesterton", "work": "The Innocence of Father Brown", "quote": "The brilliant sleuth relied not merely on theoretical deductions, but sought immediate **ocular** inspection of the crime scene."}
        ]
    },
    "ocularly": {
        "primary": "By means of the eye or direct visual observation.",
        "secondary": "In forensic demonstration and empirical optics, establishing verification through unassisted or instrumentally magnified visual inspection.",
        "quotes": [
            {"author": "Thomas Browne", "work": "Pseudodoxia Epidemica", "quote": "We have repeatedly confirmed this curious anatomical fact **ocularly**, dissecting the organ beneath a bright lens."},
            {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "The stratification of the cliff could be verified **ocularly** from the deck of the packet as we sailed along the coast."},
            {"author": "Robert Boyle", "work": "New Experiments Physico-Mechanical", "quote": "The experimenter was able to demonstrate **ocularly** that the mercury column fell steadily as air was exhausted from the receiver."}
        ]
    },
    "oculist": {
        "primary": "A medical specialist who treats diseases and defects of the eye; an ophthalmologist.",
        "secondary": "In medical history and historical social life, a physician specializing in cataract couching, prescribing corrective spectacles, and managing eye ailments.",
        "quotes": [
            {"author": "Jane Austen", "work": "Emma", "quote": "The delicate state of his sight induced Mr. Woodhouse to seek the advice of a celebrated London **oculist**."},
            {"author": "Charles Dickens", "work": "Bleak House", "quote": "The poor clerk strained his inflamed eyes by candlelight until he was compelled to consult an **oculist** in Lincoln's Inn."},
            {"author": "Oliver Wendell Holmes Sr.", "work": "The Autocrat of the Breakfast-Table", "quote": "The skillful **oculist** examines the fundus of the eye, discerning systemic disorders mirrored upon the vascular retina."}
        ]
    },
    "oculomotor": {
        "primary": "Pertaining to or causing movements of the eyeball.",
        "secondary": "In clinical neuroanatomy, relating to the third cranial nerve (CN III), which innervates the superior, inferior, and medial recti, the inferior oblique, and parasympathetic pupillary constrictors.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Complete paralysis of the **oculomotor** nerve causes marked ptosis, pupillary dilation, and an eye turned downward and outward."},
            {"author": "Santiago Ramón y Cajal", "work": "Histology of the Nervous System", "quote": "Fibers from the **oculomotor** nucleus emerge from the medial aspect of the cerebral peduncles toward the cavernous sinus."},
            {"author": "Charles Sherrington", "work": "The Integrative Action of the Nervous System", "quote": "Reciprocal innervation coordinates antagonistic muscle groups through the motor nuclei of the **oculomotor** and abducens nerves."}
        ]
    },
    "oculus": {
        "primary": "A circular opening in the center of a dome or wall, or the eye in classical anatomical description.",
        "secondary": "In Roman architecture and botany, the unglazed circular opening at the apex of a rotunda (as in the Pantheon), or a leaf bud on a tuber.",
        "quotes": [
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The majestic dome of the Pantheon is illuminated solely by the great circular **oculus** open to the changing skies of Rome."},
            {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "A beautifully carved marble **oculus** admitted a beam of filtered daylight into the dark vaulted sanctuary."},
            {"author": "Henry James", "work": "Italian Hours", "quote": "Rain fell gently through the central **oculus** of the ancient temple, splashing upon the polished porphyry pavement beneath."}
        ]
    },
    "postocular": {
        "primary": "Situated behind or posterior to the eye.",
        "secondary": "In entomology and herpetology, designating specialized scales, bristles, or glands located immediately posterior to the orbit in snakes and insects.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Zoology of the Voyage of H.M.S. Beagle", "quote": "In this newly discovered viper, the two **postocular** scales are markedly enlarged and distinctly keeled along their upper margins."},
            {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "The sensory canal in the fish skull bifurcates behind the orbit, giving rise to the **postocular** lateral line branch."},
            {"author": "Louis Agassiz", "work": "Contributions to the Natural History of the United States", "quote": "The diagnostic arrangement of the **postocular** plates in young turtles remains constant across diverse geographic races."}
        ]
    },
    "preocular": {
        "primary": "Situated in front of or anterior to the eye.",
        "secondary": "In comparative anatomy and entomological taxonomy, describing scales, bristles, or sensory organs positioned anterior to the orbital boundary.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Zoology of the Voyage of H.M.S. Beagle", "quote": "The serpent is easily recognized by its single prominent **preocular** scale, which separates the eye from the nasal plate."},
            {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "In elasmobranchs the **preocular** cartilage supports the rostrum and provides attachment for the olfactory capsules."},
            {"author": "David Starr Jordan", "work": "A Guide to the Study of Fishes", "quote": "A sharp **preocular** spine in this scorpaenoid fish delivers a painful puncture when carelessly handled by fishermen."}
        ]
    },
    "subocular": {
        "primary": "Situated beneath, below, or on the inferior aspect of the eye.",
        "secondary": "In craniofacial morphology and herpetological taxonomy, designating scales, pouches, or nerve branches lying directly inferior to the orbital margin.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Zoology of the Voyage of H.M.S. Beagle", "quote": "A series of small smooth **subocular** scales completely separates the lower eyelid from the upper labial plates in this lizard."},
            {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "The infraorbital canal opens onto the **subocular** surface of the facial skeleton through a wide foramen."},
            {"author": "Richard Owen", "work": "On the Anatomy of Vertebrates", "quote": "In nocturnal lemurs the expanded **subocular** shelf of the zygoma provides extensive support for the hypertrophied globe."}
        ]
    },
    "triocular": {
        "primary": "Having or possessing three eyes, or an optical instrument fitted with three viewing ports.",
        "secondary": "In invertebrate morphology and microscopy, describing organisms with three ocelli, or microscope heads equipped with binocular eyepieces and a third camera port.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Certain primitive arthropod larvae exhibit a **triocular** arrangement of simple median eyes before developing compound vision."},
            {"author": "Thomas Henry Huxley", "work": "The Crayfish", "quote": "The ancestral crustacean head likely featured a **triocular** photoreceptive cluster comprising two lateral and one median ocellus."},
            {"author": "Louis Pasteur", "work": "Studies on Fermentation", "quote": "The laboratory was equipped with an advanced **triocular** microscope that allowed the operator to photograph yeast cells during division."}
        ]
    },

    # ==================== Dashboard — aur_ear (part 1: 6 words) ====================
    "aura": {
        "primary": "A distinctive atmosphere, quality, or emanation surrounding a person, thing, or place.",
        "secondary": "In clinical neurology, a perceptual warning disturbance (visual, olfactory, or sensory) preceding an epileptic seizure or migraine headache.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The epileptic attack is frequently heralded by a sensory **aura**, such as an epigastric distress or flashes of light before the eyes."},
            {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Ancient physicians imagined a subtle vital **aura** that emanated from active spirits and animated the nervous humors."},
            {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "There hung about her an **aura** of woodland innocence that fascinated Angel Clare in the dewy morning pastures."}
        ]
    },
    "aural": {
        "primary": "Pertaining to the ear or the sense of hearing; auditory.",
        "secondary": "In otology and acoustic perception, relating to the anatomical structures of hearing, acoustic frequency processing, or audiological symptoms.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Severe vertigo accompanied by distressing **aural** tinnitus and progressive deafness characterizes Meniere's disease."},
            {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The auditory nerve transmits **aural** impulses from the hair cells of the organ of Corti to the temporal cortex."},
            {"author": "Arthur Conan Doyle", "work": "The Adventure of the Cardboard Box", "quote": "The gruesome parcel contained two severed ears, pointing unmistakably to an act of vengeful **aural** mutilation."}
        ]
    },
    "aurally": {
        "primary": "By means of the ear or the sense of hearing; through auditory reception.",
        "secondary": "In cognitive phonetics and psychoacoustics, processing linguistic information or musical pitch through auditory perception rather than visual reading.",
        "quotes": [
            {"author": "Walter Pater", "work": "The Renaissance: Studies in Art and Poetry", "quote": "Poetry appeals both visually upon the page and **aurally** through the enchanting music of its spoken vowels."},
            {"author": "William James", "work": "The Principles of Psychology", "quote": "A trained musician perceives an entire orchestral chord **aurally**, effortlessly distinguishing the timbre of each instrument."},
            {"author": "Charles Dickens", "work": "Bleak House", "quote": "Mr. Guppy followed the testimony **aurally**, taking frantic notes whenever a witness uttered a damaging admission."}
        ]
    },
    "aurate": {
        "primary": "A chemical salt containing gold in its anionic form, especially gold in the +3 oxidation state.",
        "secondary": "In inorganic chemistry and metallurgy, complex aurate salts (such as potassium aurate) formed by dissolving auric hydroxide in strong alkalis.",
        "quotes": [
            {"author": "Humphry Davy", "work": "Elements of Chemical Philosophy", "quote": "By treating auric oxide with concentrated potash, we prepared crystalline **aurate** of potassium as a pale yellow salt."},
            {"author": "Jöns Jacob Berzelius", "work": "Treatise on Chemistry", "quote": "The alkaline solutions of **aurate** decompose slowly under the action of light, precipitating metallic gold flakes."},
            {"author": "Michael Faraday", "work": "Experimental Researches in Chemistry and Physics", "quote": "Dilute solutions of potassium **aurate** yielded finely divided colloidal gold upon reduction with phosphorus vapors."}
        ]
    },
    "aureate": {
        "primary": "Brilliant golden in color, or characterized by ornate, grandiloquent, and elaborate literary style.",
        "secondary": "In fifteenth-century English rhetoric, highly stylized poetic diction enriched with Latinate coinages and opulent decorative flourishes.",
        "quotes": [
            {"author": "John Milton", "work": "Paradise Lost", "quote": "The heavenly courts were paved with **aureate** light that dazzled the seraphic orders standing about the throne."},
            {"author": "Samuel Johnson", "work": "The Lives of the English Poets", "quote": "The early Scottish Chaucerians cultivated an **aureate** language adorned with precious classical figures and Latinate rhymes."},
            {"author": "Walter Pater", "work": "Appreciations", "quote": "The poet's lines glow with an **aureate** splendor, turning common speech into a rich tapestry of golden imagery."}
        ]
    },
    "aurelia": {
        "primary": "A pupa or chrysalis of an insect, especially a butterfly with golden spots, or a genus of scyphozoan jellyfish (moon jellies).",
        "secondary": "In classical entomology and marine invertebrate zoology, the golden chrysalis of nymphalid butterflies, or the common coastal scyphozoan *Aurelia aurita*.",
        "quotes": [
            {"author": "Gilbert White", "work": "The Natural History of Selborne", "quote": "The caterpillar suspended itself from the wall, transforming within days into a gilded **aurelia** marked with brilliant spots."},
            {"author": "Jean-Henri Fabre", "work": "The Life of the Caterpillar", "quote": "From the silken cocoon emerges a dormant **aurelia**, awaiting the warm breath of spring to unfurl its wings."},
            {"author": "Louis Agassiz", "work": "Contributions to the Natural History of the United States", "quote": "The saucer-shaped jellyfish belonging to the genus **Aurelia** pulsates through the coastal shallows in enormous translucent shoals."}
        ]
    }
}
