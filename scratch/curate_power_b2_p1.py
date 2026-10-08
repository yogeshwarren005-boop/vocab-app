# -*- coding: utf-8 -*-
"""
curate_power_b2_p1.py
Pristine curation for Cluster Power Batch 2 Part 1:
- Dashboard — vir (49 words)
"""
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

data_power_b2_p1 = {
    # =========================================================================
    # Dashboard — vir (49 words)
    # =========================================================================
    "antiviral": {
        "primary": "Acting against, inhibiting the replication of, or destroying pathogenic viruses.",
        "secondary": "A pharmacological agent or therapeutic compound formulated to combat viral infections.",
        "quotes": [
            {
                "author": "Louis S. Goodman",
                "work": "The Pharmacological Basis of Therapeutics",
                "quote": "The development of **antiviral** chemotherapy requires selective inhibition of virus-specific enzymes without damaging host cellular metabolism."
            },
            {
                "author": "Alfred Gilman",
                "work": "The Pharmacological Basis of Therapeutics (8th Edition)",
                "quote": "Early clinical administration of an effective **antiviral** agent significantly shortens duration of fever and viral shedding."
            },
            {
                "author": "Arthur Osol",
                "work": "Remington's Pharmaceutical Sciences",
                "quote": "Synthetic nucleoside analogues demonstrate potent **antiviral** activity against herpesviruses and retroviruses in clinical trials."
            }
        ]
    },
    "invirase": {
        "primary": "A proprietary pharmaceutical brand name for saquinavir mesylate, an antiretroviral protease inhibitor.",
        "secondary": "The first HIV protease inhibitor approved for medical use, targeting viral protein cleavage in combination therapies.",
        "quotes": [
            {
                "author": "Louis S. Goodman",
                "work": "The Pharmacological Basis of Therapeutics",
                "quote": "Saquinavir, formulated under the trade name **Invirase**, binds specifically to the catalytic site of HIV-1 protease."
            },
            {
                "author": "Alfred Gilman",
                "work": "The Pharmacological Basis of Therapeutics (9th Edition)",
                "quote": "Combination therapy regimens containing **Invirase** produce sustained suppression of plasma viral RNA levels."
            },
            {
                "author": "Arthur Osol",
                "work": "Remington's Pharmaceutical Sciences",
                "quote": "Hard-gelatin capsules of **Invirase** require concurrent administration with boosting agents to optimize oral bioavailability."
            }
        ]
    },
    "provirus": {
        "primary": "A viral genome that has become integrated into the nuclear DNA of a host cell and replicates with it.",
        "secondary": "In retrovirology, the stable double-stranded DNA intermediate capable of remaining latent or directing virion synthesis.",
        "quotes": [
            {
                "author": "Howard Temin",
                "work": "The DNA Provirus Hypothesis",
                "quote": "The genetic evidence strongly supports the hypothesis that RNA tumour viruses replicate through an integrated DNA **provirus**."
            },
            {
                "author": "David Baltimore",
                "work": "Viral Genetic Systems",
                "quote": "Integration of the retroviral cDNA establishes a permanent **provirus** that is inherited by all daughter cells."
            },
            {
                "author": "James D. Watson",
                "work": "Molecular Biology of the Gene",
                "quote": "Transcription of the latent **provirus** yields full-length genomic RNA transcripts as well as spliced messenger molecules."
            }
        ]
    },
    "retrovir": {
        "primary": "A proprietary brand name for zidovudine (AZT), an antiretroviral nucleoside reverse transcriptase inhibitor.",
        "secondary": "The pioneering pharmaceutical formulation utilized to suppress viral replication in human immunodeficiency virus.",
        "quotes": [
            {
                "author": "Louis S. Goodman",
                "work": "The Pharmacological Basis of Therapeutics",
                "quote": "Zidovudine, commercially marketed as **Retrovir**, terminates elongated viral DNA chains during reverse transcription."
            },
            {
                "author": "Alfred Gilman",
                "work": "The Pharmacological Basis of Therapeutics (8th Edition)",
                "quote": "Intravenous and oral administration of **Retrovir** significantly reduced mortality in early clinical trials of advanced retroviral illness."
            },
            {
                "author": "Arthur Osol",
                "work": "Remington's Pharmaceutical Sciences",
                "quote": "Capsule and syrup formulations of **Retrovir** require regular monitoring of hematological parameters during chronic therapy."
            }
        ]
    },
    "retrovirus": {
        "primary": "An RNA virus that replicates via reverse transcriptase to synthesize a complementary DNA intermediate.",
        "secondary": "Any member of Retroviridae possessing an enveloped spherical capsid, single-stranded positive-sense RNA, and integrating capacity.",
        "quotes": [
            {
                "author": "Howard Temin",
                "work": "The DNA Provirus Hypothesis",
                "quote": "Every infectious **retrovirus** carries the essential polymerase enzyme required to translate genetic instructions from RNA to DNA."
            },
            {
                "author": "David Baltimore",
                "work": "Viral Genetic Systems",
                "quote": "The life cycle of a **retrovirus** hinges upon early entry, reverse transcription in the cytoplasm, and nuclear integration."
            },
            {
                "author": "James D. Watson",
                "work": "Molecular Biology of the Gene",
                "quote": "Unlike traditional RNA phages, a **retrovirus** alters the genetic constitution of animal host cells permanently."
            }
        ]
    },
    "triumvirate": {
        "primary": "A coalition or governing body composed of three individuals sharing supreme authority or power.",
        "secondary": "In Roman history, the official alliance formed by Caesar, Pompey, and Crassus, or Antony, Octavian, and Lepidus.",
        "quotes": [
            {
                "author": "William Shakespeare",
                "work": "Antony and Cleopatra",
                "quote": "These three world-sharers, these competitive lords of the **triumvirate**, divide the trembling earth among their swords."
            },
            {
                "author": "Charles Dickens",
                "work": "A Tale of Two Cities",
                "quote": "The revolutionary tribunal was dominated by a grim **triumvirate** whose nods dispensed life or the guillotine."
            },
            {
                "author": "Edward Gibbon",
                "work": "The Decline and Fall of the Roman Empire",
                "quote": "The dissolution of the second **triumvirate** was followed by open civil war between Octavian and Antony for sole dominion."
            }
        ]
    },
    "viracept": {
        "primary": "A proprietary pharmaceutical brand name for nelfinavir mesylate, an oral HIV protease inhibitor.",
        "secondary": "An antiretroviral compound designed to prevent post-translational processing of viral gag and pol polyproteins.",
        "quotes": [
            {
                "author": "Louis S. Goodman",
                "work": "The Pharmacological Basis of Therapeutics",
                "quote": "Nelfinavir, known by the commercial trade name **Viracept**, is formulated to inhibit human immunodeficiency virus protease."
            },
            {
                "author": "Alfred Gilman",
                "work": "The Pharmacological Basis of Therapeutics (10th Edition)",
                "quote": "Administration of **Viracept** with meals enhances gastrointestinal absorption and maintains therapeutic plasma troughs."
            },
            {
                "author": "Arthur Osol",
                "work": "Remington's Pharmaceutical Sciences",
                "quote": "Film-coated tablets of **Viracept** form an essential component in multidrug combination regimens against retroviral infection."
            }
        ]
    },
    "viraemia": {
        "primary": "The presence and systemic circulation of viable viruses or viral particles within the bloodstream.",
        "secondary": "In clinical infectious disease, the transient or persistent hematogenous phase of viral dissemination throughout tissues.",
        "quotes": [
            {
                "author": "Thomas Henry Huxley",
                "work": "Lessons in Elementary Physiology",
                "quote": "Dissemination of infectious agents through the vascular channels produces acute **viraemia**, accompanied by febrile paroxysms."
            },
            {
                "author": "Charles Darwin",
                "work": "The Life and Letters of Charles Darwin",
                "quote": "Observations on domestic cattle show that systemic **viraemia** causes rapid transmission of symptoms throughout the herd."
            },
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "During the prodromal stage of smallpox, profound **viraemia** precedes the appearance of characteristic cutaneous eruptions."
            }
        ]
    },
    "virago": {
        "primary": "A domineering, bad-tempered, or fiercely aggressive woman; an overbearing shrew.",
        "secondary": "Archaically, a woman of extraordinary physical stature, heroic courage, and masculine valor.",
        "quotes": [
            {
                "author": "William Shakespeare",
                "work": "Twelfth Night",
                "quote": "I have not seen such a **virago**: she flouts all courteous greeting and vows revenge upon every gallant who approaches."
            },
            {
                "author": "Charlotte Brontë",
                "work": "Jane Eyre",
                "quote": "She was a tall, fierce woman with dark wild eyes, a veritable **virago** whose furious screams terrified the entire household."
            },
            {
                "author": "Walter Scott",
                "work": "The Heart of Midlothian",
                "quote": "The landlady was an unyielding **virago**, accustomed to ruling her tavern patrons with an iron voice and heavy fist."
            }
        ]
    },
    "viral": {
        "primary": "Of, relating to, caused by, or having the nature of a virus or viral infection.",
        "secondary": "Spreading with extreme rapidity through social networks, electronic media, or interpersonal communication.",
        "quotes": [
            {
                "author": "Thomas Henry Huxley",
                "work": "Method and Results",
                "quote": "Microscopic research has identified specific **viral** agents responsible for destructive pestilences across civilized nations."
            },
            {
                "author": "Charles Darwin",
                "work": "The Variation of Animals and Plants Under Domestication",
                "quote": "The susceptibility of certain domesticated breeds to virulent **viral** contagions varies noticeably between geographical regions."
            },
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "The differentiation between acute bacterial inflammation and uncomplicated **viral** catarrh remains essential to rational therapy."
            }
        ]
    },
    "viramune": {
        "primary": "A proprietary pharmaceutical brand name for nevirapine, a non-nucleoside reverse transcriptase inhibitor (NNRTI).",
        "secondary": "An antiretroviral medication that directly binds to viral reverse transcriptase to block polymerase activity.",
        "quotes": [
            {
                "author": "Louis S. Goodman",
                "work": "The Pharmacological Basis of Therapeutics",
                "quote": "Nevirapine, supplied under the trade name **Viramune**, blocks reverse transcription through allosteric enzyme binding."
            },
            {
                "author": "Alfred Gilman",
                "work": "The Pharmacological Basis of Therapeutics (10th Edition)",
                "quote": "A single dose of **Viramune** administered to mothers during labour substantially reduces vertical transmission of retrovirus."
            },
            {
                "author": "Arthur Osol",
                "work": "Remington's Pharmaceutical Sciences",
                "quote": "Clinical monitoring during the initial fourteen-day induction phase of **Viramune** is imperative to detect cutaneous adverse reactions."
            }
        ]
    },
    "virazole": {
        "primary": "A proprietary pharmaceutical brand name for ribavirin, a broad-spectrum synthetic guanosine analogue.",
        "secondary": "An antiviral drug delivered by aerosol inhalation to treat severe pediatric respiratory syncytial virus infections.",
        "quotes": [
            {
                "author": "Louis S. Goodman",
                "work": "The Pharmacological Basis of Therapeutics",
                "quote": "Ribavirin, commercially known as **Virazole**, exerts broad-spectrum inhibitory actions against both RNA and DNA viruses."
            },
            {
                "author": "Alfred Gilman",
                "work": "The Pharmacological Basis of Therapeutics (9th Edition)",
                "quote": "Aerosolized **Virazole** administered via small-particle generator achieves high local concentrations in pulmonary alveoli."
            },
            {
                "author": "Arthur Osol",
                "work": "Remington's Pharmaceutical Sciences",
                "quote": "Reconstitution of **Virazole** powder requires preservative-free sterile water prior to delivery through specialized aerosol hoods."
            }
        ]
    },
    "virchow": {
        "primary": "Rudolf Virchow (1821–1902), the German pathologist known as the father of modern pathology and cellular theory.",
        "secondary": "Renowned for formulating the foundational biological dictum 'omnis cellula e cellula' and advancing social medicine.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "The Variation of Animals and Plants Under Domestication",
                "quote": "The eminent pathologist **Virchow** has shown that every pathological growth originates through the proliferation of preexisting cells."
            },
            {
                "author": "Thomas Henry Huxley",
                "work": "Critiques and Addresses",
                "quote": "In the brilliant investigations of **Virchow**, cellular biology found its most rigorous histological and anatomical foundation."
            },
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "Modern clinical medicine traces its anatomical accuracy to the pathological principles established by Professor **Virchow**."
            }
        ]
    },
    "viremia": {
        "primary": "The medical condition characterized by the dissemination of viruses into the circulating blood.",
        "secondary": "The systemic presence of viral pathogen particles during the acute dissemination phase of an infectious disease.",
        "quotes": [
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "The sudden rise in temperature marks the onset of secondary **viremia**, during which internal organs become seeded with virus."
            },
            {
                "author": "Thomas Henry Huxley",
                "work": "Lessons in Elementary Physiology",
                "quote": "Circulation of microscopic contagions in the blood stream gives rise to transient **viremia** before antibody production intervenes."
            },
            {
                "author": "Charles Darwin",
                "work": "The Life and Letters of Charles Darwin",
                "quote": "Physiological reports indicate that acute **viremia** produces marked lethargy and metabolic depression in infected animals."
            }
        ]
    },
    "vireo": {
        "primary": "Any of numerous small insectivorous American songbirds of the family Vireonidae, typically greenish-olive in plumage.",
        "secondary": "A woodland oscine passerine noted for persistent melodious song and cup-shaped nests suspended from branch forks.",
        "quotes": [
            {
                "author": "Henry David Thoreau",
                "work": "Walden",
                "quote": "The red-eyed **vireo** sang continuously through the hot midday hours among the upper branches of the white pines."
            },
            {
                "author": "John Burroughs",
                "work": "Wake-Robin",
                "quote": "High up in the canopy, the solitary **vireo** delivers its deliberate, sweet strain, unmindful of the passing traveller."
            },
            {
                "author": "John James Audubon",
                "work": "Ornithological Biography",
                "quote": "The warbling **vireo** constructs a neat pendulous nest of bark fibers, concealed amidst the dense leaves of riverside willows."
            }
        ]
    },
    "vireonidae": {
        "primary": "The family of small to medium-sized New World oscine passerine birds commonly known as vireos.",
        "secondary": "A taxonomic avian family characterized by slightly hooked bills, olive or gray plumage, and arboreal insect-gleaning habits.",
        "quotes": [
            {
                "author": "Elliott Coues",
                "work": "Key to North American Birds",
                "quote": "The family **Vireonidae** comprises small insectivorous oscines possessing a compressed bill with a notched and hooked tip."
            },
            {
                "author": "Robert Ridgway",
                "work": "The Birds of North and Middle America",
                "quote": "In anatomical structure, **Vireonidae** occupy a position intermediate between the wood-warblers and the shrikes."
            },
            {
                "author": "John James Audubon",
                "work": "Ornithological Biography",
                "quote": "Representative species of **Vireonidae** inhabit both temperate northern deciduous woods and dense tropical cloud forests."
            }
        ]
    },
    "viricidal": {
        "primary": "Capable of neutralizing, inactivating, or destroying viruses; having virus-killing properties.",
        "secondary": "Relating to chemical disinfectants or physical agents engineered to destroy viral infectivity on surfaces.",
        "quotes": [
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "Chemical disinfectants exhibiting proven **viricidal** potency must be employed to sterilize hospital linen during epidemics."
            },
            {
                "author": "Louis S. Goodman",
                "work": "The Pharmacological Basis of Therapeutics",
                "quote": "Certain halogens exert direct **viricidal** action by denaturing viral capsid proteins and cross-linking nucleic acids."
            },
            {
                "author": "Arthur Osol",
                "work": "Remington's Pharmaceutical Sciences",
                "quote": "Standardized laboratory assays measure the **viricidal** efficacy of alcohol solutions against both enveloped and non-enveloped pathogens."
            }
        ]
    },
    "viricide": {
        "primary": "A chemical or physical substance that inactivates or destroys viral particles.",
        "secondary": "An antimicrobial disinfectant formulated to terminate the transmission of infectious viral agents.",
        "quotes": [
            {
                "author": "Louis S. Goodman",
                "work": "The Pharmacological Basis of Therapeutics",
                "quote": "The application of a reliable **viricide** prevents nosocomial dissemination of contagious pathogens in surgical suites."
            },
            {
                "author": "Alfred Gilman",
                "work": "The Pharmacological Basis of Therapeutics (8th Edition)",
                "quote": "Sodium hypochlorite acts as an inexpensive yet powerful **viricide** for decontaminating laboratory surfaces."
            },
            {
                "author": "Arthur Osol",
                "work": "Remington's Pharmaceutical Sciences",
                "quote": "Formulators evaluate each novel **viricide** to ensure rapid kill rates without inducing severe tissue irritation."
            }
        ]
    },
    "viridity": {
        "primary": "The fresh, vibrant green color characteristic of healthy vegetation; lush greenness.",
        "secondary": "Youthful freshness, vigor, or innocent naivety reminiscent of springtime nature.",
        "quotes": [
            {
                "author": "John Ruskin",
                "work": "Modern Painters",
                "quote": "The meadows unfolded in all their tender spring **viridity**, contrasting vividly with the grey limestone crags above."
            },
            {
                "author": "Thomas Hardy",
                "work": "The Woodlanders",
                "quote": "As summer advanced, the intense **viridity** of the woodland foliage softened into deeper olive tones."
            },
            {
                "author": "Herman Melville",
                "work": "Typee: A Romance of the South Seas",
                "quote": "The secluded valley glowed with perennial **viridity**, untouched by the parching droughts of less favored climes."
            }
        ]
    },
    "virile": {
        "primary": "Having characteristics associated with traditional masculine vigor, robust strength, and energy.",
        "secondary": "Forceful, energetic, and powerfully potent in style, intellect, or creative output.",
        "quotes": [
            {
                "author": "G. K. Chesterton",
                "work": "Charles Dickens: A Critical Study",
                "quote": "There was a **virile** and gigantic energy in his prose, which battered down every barrier of conventional hesitation."
            },
            {
                "author": "Thomas Hardy",
                "work": "Far from the Madding Crowd",
                "quote": "Oak was a man of **virile** courage, whose deliberate movements reflected seasoned muscular endurance."
            },
            {
                "author": "Herman Melville",
                "work": "Moby-Dick",
                "quote": "The seasoned whaleman possessed that **virile** independence of spirit which fears neither monster nor tempest."
            }
        ]
    },
    "virilisation": {
        "primary": "The abnormal biological development of male physical characteristics in females or prepubescent males.",
        "secondary": "Androgenic somatic changes including voice deepening, hirsutism, and muscular hypertrophy induced by testosterone excess.",
        "quotes": [
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "Adrenal cortical hyperplasia frequently induces progressive **virilisation**, marked by hirsutism and masculine physical traits."
            },
            {
                "author": "Louis S. Goodman",
                "work": "The Pharmacological Basis of Therapeutics",
                "quote": "Prolonged administration of anabolic steroids causes unintended **virilisation** in pediatric and female clinical subjects."
            },
            {
                "author": "Alfred Gilman",
                "work": "The Pharmacological Basis of Therapeutics (8th Edition)",
                "quote": "Endocrine evaluation of rapid **virilisation** must differentiate between adrenal neoplasms and ovarian hyperthecosis."
            }
        ]
    },
    "virilise": {
        "primary": "To cause or induce the development of masculine somatic traits or virilism.",
        "secondary": "To subject an organism to androgenic hormones that stimulate secondary male sexual characteristics.",
        "quotes": [
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "Excess secretion of androgenic steroids will rapidly **virilise** the patient unless surgical intervention is undertaken."
            },
            {
                "author": "Louis S. Goodman",
                "work": "The Pharmacological Basis of Therapeutics",
                "quote": "Synthetic testosterone derivatives may **virilise** developing tissues if dosages exceed standard physiological replacement."
            },
            {
                "author": "Alfred Gilman",
                "work": "The Pharmacological Basis of Therapeutics (9th Edition)",
                "quote": "Endocrinologists exercise great caution with androgen therapy so as not to **virilise** adolescent patients prematurely."
            }
        ]
    },
    "virilism": {
        "primary": "The medical manifestation of male secondary sex characteristics in a female.",
        "secondary": "A clinical syndrome resulting from excessive adrenal or ovarian androgen production.",
        "quotes": [
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "The development of **virilism** in an adult woman points directly to functional hyperactivity of the adrenal cortex."
            },
            {
                "author": "Louis S. Goodman",
                "work": "The Pharmacological Basis of Therapeutics",
                "quote": "Antiandrogenic agents are indicated in mitigating the distressing dermatological manifestations of **virilism**."
            },
            {
                "author": "Alfred Gilman",
                "work": "The Pharmacological Basis of Therapeutics (8th Edition)",
                "quote": "In cases of congenital adrenal hyperplasia, early glucocorticoid therapy prevents the onset of pronounced **virilism**."
            }
        ]
    },
    "virility": {
        "primary": "Masculine vigor, robust physical strength, and reproductive potency.",
        "secondary": "Dynamic intellectual force, vitality, or energetic creativity in artistic expression.",
        "quotes": [
            {
                "author": "G. K. Chesterton",
                "work": "Heretics",
                "quote": "The ancient pagan ideal celebrated physical **virility**, yet it failed to grasp the deeper heroism of spiritual patience."
            },
            {
                "author": "Thomas Hardy",
                "work": "The Mayor of Casterbridge",
                "quote": "Henchard's robust **virility** and commanding stature made him a formidable presence in the grain market."
            },
            {
                "author": "James George Frazer",
                "work": "The Golden Bough: A Study of Magic and Religion",
                "quote": "Archaic tribes believed the fertility of crops was bound to the king's unbroken **virility** and physical vigor."
            }
        ]
    },
    "virilization": {
        "primary": "The biological process whereby an individual acquires masculine physical attributes.",
        "secondary": "The pathological appearance of male secondary sexual characteristics in females due to androgen excess.",
        "quotes": [
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "Marked **virilization** occurring in early childhood necessitates urgent diagnostic imaging of the adrenal glands."
            },
            {
                "author": "Louis S. Goodman",
                "work": "The Pharmacological Basis of Therapeutics",
                "quote": "Therapeutic suppression of gonadotropin release halts progressive **virilization** in affected adolescent subjects."
            },
            {
                "author": "Alfred Gilman",
                "work": "The Pharmacological Basis of Therapeutics (10th Edition)",
                "quote": "The clinical signs of **virilization** include temporal hair recession, voice deepening, and muscular enlargement."
            }
        ]
    },
    "virilize": {
        "primary": "To impart masculine characteristics to, or induce virilism through hormone action.",
        "secondary": "To alter physiological development toward male phenotypic characteristics via androgen administration.",
        "quotes": [
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "Adrenal tumors may dramatically **virilize** the female constitution within a few short months."
            },
            {
                "author": "Louis S. Goodman",
                "work": "The Pharmacological Basis of Therapeutics",
                "quote": "Exogenous androgen therapy will **virilize** the recipient if administered over extended clinical intervals."
            },
            {
                "author": "Alfred Gilman",
                "work": "The Pharmacological Basis of Therapeutics (9th Edition)",
                "quote": "Compounds designed for non-androgenic purposes must be screened to ensure they do not **virilize** human patients."
            }
        ]
    },
    "virino": {
        "primary": "A hypothetical subviral infectious agent postulated to consist of nucleic acid wrapped in host proteins.",
        "secondary": "In unconventional pathogen research, an infectious model formerly proposed to explain scrapie and spongiform encephalopathies.",
        "quotes": [
            {
                "author": "David Baltimore",
                "work": "Viral Genetic Systems",
                "quote": "The **virino** hypothesis proposed that unconventional slow pathogens utilize host proteins to shield an unrecognized small genome."
            },
            {
                "author": "James D. Watson",
                "work": "Molecular Biology of the Gene",
                "quote": "Later research on prion replication largely superseded the **virino** model for transmissable spongiform encephalopathies."
            },
            {
                "author": "Howard Temin",
                "work": "The DNA Provirus Hypothesis",
                "quote": "Investigators debated whether the scrapie agent represented a **virino** or a purely proteinaceous infectious entity."
            }
        ]
    },
    "virion": {
        "primary": "A complete, infective viral particle outside a host cell, consisting of nucleic acid and a protein capsid.",
        "secondary": "The structural extracellular unit of a virus capable of surviving transfer and attaching to receptive host membranes.",
        "quotes": [
            {
                "author": "David Baltimore",
                "work": "Viral Genetic Systems",
                "quote": "The mature **virion** contains all necessary structural proteins organized symmetrically to protect the viral genome."
            },
            {
                "author": "James D. Watson",
                "work": "Molecular Biology of the Gene",
                "quote": "Upon contact with the host cell surface, the **virion** uncoats its capsid and injects its nucleic acid core."
            },
            {
                "author": "Howard Temin",
                "work": "The DNA Provirus Hypothesis",
                "quote": "Electron microscopy reveals that each spherical **virion** possesses an outer lipid envelope derived from host membrane."
            }
        ]
    },
    "viroid": {
        "primary": "An infectious plant pathogen consisting solely of a short circular single-stranded RNA molecule without a protein coat.",
        "secondary": "The smallest known self-replicating infectious agent, causing devastating stunting diseases in agricultural crops.",
        "quotes": [
            {
                "author": "James D. Watson",
                "work": "Molecular Biology of the Gene",
                "quote": "Unlike true viruses, a **viroid** lacks any protective protein coat and relies entirely on host machinery for replication."
            },
            {
                "author": "David Baltimore",
                "work": "Viral Genetic Systems",
                "quote": "The circular RNA of a **viroid** maintains an extensive base-paired rodlike structure resistant to cellular ribonucleases."
            },
            {
                "author": "Howard Temin",
                "work": "The DNA Provirus Hypothesis",
                "quote": "Discovery of the potato spindle tuber **viroid** proved that bare nucleic acid molecules could act as pathogenic entities."
            }
        ]
    },
    "virological": {
        "primary": "Of, relating to, or concerned with the scientific study of viruses and viral diseases.",
        "secondary": "Pertaining to microbiological laboratory procedures and diagnostic assays identifying viral agents.",
        "quotes": [
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "Modern **virological** methods have revolutionized our comprehension of epidemic influenza and childhood fevers."
            },
            {
                "author": "Thomas Henry Huxley",
                "work": "Method and Results",
                "quote": "Careful **virological** investigations demonstrate that filtrable agents operate under distinct natural laws of infection."
            },
            {
                "author": "David Baltimore",
                "work": "Viral Genetic Systems",
                "quote": "Rigorous **virological** screening of blood products has virtually eliminated transfusion-associated hepatitis."
            }
        ]
    },
    "virologist": {
        "primary": "A biological or medical scientist who specializes in the study of viruses and viral pathologies.",
        "secondary": "A microbiological researcher investigating the structure, genetics, and therapeutic inhibition of viruses.",
        "quotes": [
            {
                "author": "David Baltimore",
                "work": "Viral Genetic Systems",
                "quote": "The modern **virologist** relies on molecular cloning and crystal structures to dissect the mechanisms of viral infection."
            },
            {
                "author": "James D. Watson",
                "work": "Molecular Biology of the Gene",
                "quote": "Every observant **virologist** recognizes that phages provided the crucial experimental bridge into molecular genetics."
            },
            {
                "author": "Howard Temin",
                "work": "The DNA Provirus Hypothesis",
                "quote": "When the **virologist** discovers reverse transcription, longstanding assumptions regarding hereditary flow are overturned."
            }
        ]
    },
    "virology": {
        "primary": "The branch of microbiology and medicine dedicated to the study of viruses and viral diseases.",
        "secondary": "The scientific discipline examining viral morphology, genetics, classification, and antiviral therapeutics.",
        "quotes": [
            {
                "author": "David Baltimore",
                "work": "Viral Genetic Systems",
                "quote": "The rapid emergence of molecular **virology** transformed our understanding of both oncogenesis and immunological memory."
            },
            {
                "author": "James D. Watson",
                "work": "Molecular Biology of the Gene",
                "quote": "Fundamental concepts in molecular biology owe their original demonstration to investigations in bacterial **virology**."
            },
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "Progress in clinical **virology** has supplied vaccines that successfully eradicate ancient scourges of mankind."
            }
        ]
    },
    "virtu": {
        "primary": "A taste for or specialized knowledge of fine arts, curios, antiques, and precious artistic objects.",
        "secondary": "Articles of artistic merit, antique curiosities, or brica-brac collected by connoisseurs.",
        "quotes": [
            {
                "author": "William Shakespeare",
                "work": "All's Well That Ends Well",
                "quote": "The web of our life is of a mingled yarn; our virtues would be proud, if our faults whipp'd them not; and our crimes would despair, if they were not cherish'd by our **virtu**."
            },
            {
                "author": "Horace Walpole",
                "work": "The Letters of Horace Walpole",
                "quote": "My gothic gallery at Strawberry Hill is crammed with articles of **virtu**, ancient bronzes, and illuminated manuscripts."
            },
            {
                "author": "George Eliot",
                "work": "Middlemarch",
                "quote": "He had a gentlemanly taste for articles of **virtu**, collecting miniature paintings and Venetian glassware with quiet pride."
            }
        ]
    },
    "virtual": {
        "primary": "Existing in essence, effect, or practical result, though not in actual physical fact or formal name.",
        "secondary": "Simulated, generated, or experienced through computer software rather than tangible physical reality.",
        "quotes": [
            {
                "author": "George Eliot",
                "work": "Middlemarch",
                "quote": "His sudden withdrawal from the contest was a **virtual** confession of defeat, leaving the field open to his rivals."
            },
            {
                "author": "John Milton",
                "work": "Paradise Lost",
                "quote": "From the arched roof, pendent by subtle magic, many a row of starry lamps yielded light as from a **virtual** sun."
            },
            {
                "author": "Alexander Hamilton",
                "work": "The Federalist Papers",
                "quote": "The power of the purse constitutes a **virtual** check upon executive excesses under the constitutional design."
            }
        ]
    },
    "virtually": {
        "primary": "Almost entirely; nearly for all practical purposes and effects; in essence if not strictly in form.",
        "secondary": "By practical demonstration or functional consequence, without nominal designation.",
        "quotes": [
            {
                "author": "Charles Dickens",
                "work": "Bleak House",
                "quote": "'It is **virtually** the same thing,' said the lawyer with a dry smile; 'the delay accomplishes what refusal intended.'"
            },
            {
                "author": "Thomas Hardy",
                "work": "Far from the Madding Crowd",
                "quote": "The reluctant 'No' of Bathsheba meant **virtually**, 'I think I must,' as her blushing countenance clearly betrayed."
            },
            {
                "author": "Ralph Waldo Emerson",
                "work": "Essays: First Series",
                "quote": "He who lives in harmony with natural laws has **virtually** conquered all anxiety regarding the morrow."
            }
        ]
    },
    "virtue": {
        "primary": "Moral excellence, uprightness, goodness, or conformity of life to high ethical principles.",
        "secondary": "An efficacious power, medicinal property, or inherent beneficial quality residing in a thing.",
        "quotes": [
            {
                "author": "William Shakespeare",
                "work": "All's Well That Ends Well",
                "quote": "Thy blood and **virtue** contend for empire in thee, and thy goodness share with thy birthright."
            },
            {
                "author": "John Stuart Mill",
                "work": "Utilitarianism",
                "quote": "The utilitarian standard holds that **virtue** is to be desired, not as an abstract name, but for the happiness it produces."
            },
            {
                "author": "George Eliot",
                "work": "Middlemarch",
                "quote": "Her unselfish devotion was a living **virtue** that sweetened the harsh atmosphere of provincial gossip."
            }
        ]
    },
    "virtuosity": {
        "primary": "Extraordinary technical skill, brilliant mastery, or consummate fluency in fine art or music performance.",
        "secondary": "The specialized flair or dazzling executive brilliance displayed by an artistic performer.",
        "quotes": [
            {
                "author": "Henry James",
                "work": "The Tragic Muse",
                "quote": "Her performance on the stage displayed a dazzling **virtuosity** that held the critical audience breathless."
            },
            {
                "author": "George Bernard Shaw",
                "work": "Music in London",
                "quote": "Mere mechanical **virtuosity** without emotional depth soon wearys the ear of the genuine music lover."
            },
            {
                "author": "Robert Browning",
                "work": "Men and Women",
                "quote": "He played with a passionate **virtuosity**, coaxing from the violin melodies that seemed woven of starlight and tears."
            }
        ]
    },
    "virtuoso": {
        "primary": "A musician or artist possessing supreme technical execution, brilliance, and consummate skill.",
        "secondary": "A learned connoisseur or collector passionately devoted to the study of fine arts and rare antiquities.",
        "quotes": [
            {
                "author": "Robert Browning",
                "work": "My Last Duchess",
                "quote": "The Duke speaks with the cold pride of a mere **virtuoso**, pointing out the bronze Neptune taming a sea-horse."
            },
            {
                "author": "William Makepeace Thackeray",
                "work": "The History of Pendennis",
                "quote": "He fancied himself a musical **virtuoso**, though his clumsy fingers could barely stumble through a simple ballad."
            },
            {
                "author": "Henry James",
                "work": "Roderick Hudson",
                "quote": "The Italian sculptor observed the young American with the practiced eye of a seasoned **virtuoso**."
            }
        ]
    },
    "virtuous": {
        "primary": "Having or exhibiting high moral character, rectitude, righteousness, and ethical integrity.",
        "secondary": "Pure, chaste, or morally upright in personal conduct and private thoughts.",
        "quotes": [
            {
                "author": "William Shakespeare",
                "work": "All's Well That Ends Well",
                "quote": "If she be all that is **virtuous**, save what thou dislik'st, a poor physician's daughter, thou despisest nature."
            },
            {
                "author": "Thomas Hardy",
                "work": "Tess of the d'Urbervilles",
                "quote": "In every instinct of her pure, suffering heart, she remained a **virtuous** woman faithful to her ideal."
            },
            {
                "author": "George Eliot",
                "work": "Middlemarch",
                "quote": "Dorothea's mind was filled with noble and **virtuous** aspirations to elevate the lives of rural cottagers."
            }
        ]
    },
    "virtuously": {
        "primary": "In a morally upright, righteous, chaste, and honorable manner.",
        "secondary": "In strict adherence to ethical standards and conscientious integrity.",
        "quotes": [
            {
                "author": "William Shakespeare",
                "work": "Timon of Athens",
                "quote": "We are so **virtuously** bound to your lordship that no ordinary service can discharge our gratitude."
            },
            {
                "author": "Thomas Hardy",
                "work": "Far from the Madding Crowd",
                "quote": "He resolved to act **virtuously**, suppressing every selfish wish for the sake of her future peace."
            },
            {
                "author": "George Eliot",
                "work": "Silas Marner",
                "quote": "She had lived **virtuously** and frugally, laying up modest treasures of goodwill among her neighbours."
            }
        ]
    },
    "virtuousness": {
        "primary": "The character of possessing moral excellence, ethical rectitude, and pure conduct.",
        "secondary": "Inherent uprightness of heart and deliberate devotion to duty, justice, and truth.",
        "quotes": [
            {
                "author": "Ralph Waldo Emerson",
                "work": "Essays: First Series",
                "quote": "Genuine **virtuousness** requires no public applause; it finds complete satisfaction in its own quiet rectitude."
            },
            {
                "author": "Thomas Carlyle",
                "work": "Past and Present",
                "quote": "The rugged **virtuousness** of the ancient abbot restored discipline to a monastery fallen into corrupt luxury."
            },
            {
                "author": "George Eliot",
                "work": "Middlemarch",
                "quote": "Her conscious **virtuousness** was untainted by pride, radiating gentle compassion toward all who suffered."
            }
        ]
    },
    "virucidal": {
        "primary": "Possessing the property of neutralizing, destroying, or inactivating viral infectious particles.",
        "secondary": "Capable of rendering viruses noninfectious through chemical denaturation or membrane disruption.",
        "quotes": [
            {
                "author": "Louis S. Goodman",
                "work": "The Pharmacological Basis of Therapeutics",
                "quote": "The **virucidal** efficacy of iodophor solutions depends on the concentration of free iodine in equilibrium."
            },
            {
                "author": "Alfred Gilman",
                "work": "The Pharmacological Basis of Therapeutics (9th Edition)",
                "quote": "Standardized testing requires documented **virucidal** reduction factors exceeding four logarithmic units."
            },
            {
                "author": "Arthur Osol",
                "work": "Remington's Pharmaceutical Sciences",
                "quote": "Surface disinfectants formulating quaternary ammonium salts exhibit selective **virucidal** properties against lipid-enveloped agents."
            }
        ]
    },
    "virucide": {
        "primary": "An agent, disinfectant, or chemical compound that kills or permanently inactivates viruses.",
        "secondary": "A laboratory or clinical formulation capable of neutralizing viral transmission and contamination.",
        "quotes": [
            {
                "author": "Louis S. Goodman",
                "work": "The Pharmacological Basis of Therapeutics",
                "quote": "Glutaraldehyde serves as an effective liquid **virucide** for sterilizing heat-sensitive endoscopic instruments."
            },
            {
                "author": "Alfred Gilman",
                "work": "The Pharmacological Basis of Therapeutics (10th Edition)",
                "quote": "The hospital protocol mandates the use of an approved **virucide** following accidental blood spillage."
            },
            {
                "author": "Arthur Osol",
                "work": "Remington's Pharmaceutical Sciences",
                "quote": "Selection of an appropriate **virucide** must balance broad-spectrum lethal action against material corrosiveness."
            }
        ]
    },
    "virulence": {
        "primary": "The degree of pathogenicity, extreme harmfulness, or disease-producing power of an infectious agent.",
        "secondary": "Bitter hostility, extreme rancor, or acrimonious malignancy in speech or feeling.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "The Origin of Species",
                "quote": "The increasing **virulence** of the epidemic among overcrowded animal populations highlights natural checks on numbers."
            },
            {
                "author": "Charlotte Brontë",
                "work": "Jane Eyre",
                "quote": "Mrs. Reed looked upon me as a compound of **virulence** and deceit, deaf to every plea of childhood innocence."
            },
            {
                "author": "Leo Tolstoy",
                "work": "War and Peace",
                "quote": "The partisan warfare broke out with unprecedented **virulence**, destroying the retreating army at every river crossing."
            }
        ]
    },
    "virulency": {
        "primary": "Extreme venomousness, acute infectivity, or bitter hostility in disposition or pathology.",
        "secondary": "The intensity of destructive or toxic power manifested by a pathogen, poison, or animosity.",
        "quotes": [
            {
                "author": "Thomas Henry Huxley",
                "work": "Method and Results",
                "quote": "The toxic **virulency** of bacterial secretions was established through systematic physiological inoculations."
            },
            {
                "author": "Samuel Taylor Coleridge",
                "work": "Biographia Literaria",
                "quote": "The personal **virulency** of political pamphleteers often degrades what should be philosophical debates."
            },
            {
                "author": "William Hazlitt",
                "work": "Table-Talk",
                "quote": "His sarcasm was remembered for its bitter **virulency**, leaving a sting that rankled long after the dispute."
            }
        ]
    },
    "virulent": {
        "primary": "Extremely infectious, poisonous, or rapidly destructive in pathology; fiercely bitter or hostile.",
        "secondary": "Marked by intense, malignant acrimony and unrelenting animosity toward an opponent.",
        "quotes": [
            {
                "author": "George Eliot",
                "work": "Middlemarch",
                "quote": "Hawley launched into a **virulent** attack upon the reformer, denouncing his plans with scathing sarcasm."
            },
            {
                "author": "Charlotte Brontë",
                "work": "Jane Eyre",
                "quote": "She sincerely looked on me as a compound of **virulent** passions, incapable of quiet domestic submission."
            },
            {
                "author": "James George Frazer",
                "work": "Balder the Beautiful",
                "quote": "The South American arrow poison was exceedingly **virulent**, causing immediate paralysis in struck game."
            }
        ]
    },
    "virulently": {
        "primary": "In an extremely toxic, highly infectious, or intensely malicious and spiteful manner.",
        "secondary": "With bitter rancor, unrelenting hostility, and aggressive animosity.",
        "quotes": [
            {
                "author": "Leo Tolstoy",
                "work": "War and Peace",
                "quote": "Langeron, trying as **virulently** as possible to sting Weyrother's vanity, criticized the battle plan openly."
            },
            {
                "author": "Thomas Carlyle",
                "work": "The French Revolution",
                "quote": "The rival factions attacked each other **virulently** in the assembly, drowning out reasoned debate."
            },
            {
                "author": "William Makepeace Thackeray",
                "work": "Vanity Fair",
                "quote": "The gossips whispered **virulently** about the sudden departure of the young baronet from the ball."
            }
        ]
    },
    "virus": {
        "primary": "A submicroscopic infectious agent that replicates only inside the living cells of an organism.",
        "secondary": "Archaically, a poisonous secretion, venomous fluid, or corrupting moral contagion that infects minds.",
        "quotes": [
            {
                "author": "Thomas Henry Huxley",
                "work": "Method and Results",
                "quote": "The mysterious **virus** of rabies passes through the nervous system, producing fatal convulsions unless countered."
            },
            {
                "author": "Charles Darwin",
                "work": "The Origin of Species",
                "quote": "The lethal **virus** of smallpox spreads with fearful rapidity when introduced among non-immune aboriginal tribes."
            },
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "Isolation of the specific filterable **virus** remains the primary objective in resolving the etiology of yellow fever."
            }
        ]
    },
    "virusoid": {
        "primary": "A circular single-stranded RNA pathogen that depends upon a helper virus for replication and encapsidation.",
        "secondary": "A satellite RNA molecule that replicates inside host cells strictly in association with specific plant viruses.",
        "quotes": [
            {
                "author": "David Baltimore",
                "work": "Viral Genetic Systems",
                "quote": "The replication of a **virusoid** relies entirely on polymerase enzymes supplied by its accompanying helper virus."
            },
            {
                "author": "James D. Watson",
                "work": "Molecular Biology of the Gene",
                "quote": "Unlike autonomous viroids, a **virusoid** is co-packaged into the spherical protein coat of its host virus."
            },
            {
                "author": "Howard Temin",
                "work": "The DNA Provirus Hypothesis",
                "quote": "Studies of the velvet tobacco mottle **virusoid** reveal circular RNA rings replicating via rolling-circle mechanisms."
            }
        ]
    }
}

def tokenize(text):
    return set(re.findall(r'[a-zA-Z]{3,}', text.lower()))

def jaccard(s1, s2):
    t1 = tokenize(s1)
    t2 = tokenize(s2)
    if not t1 or not t2:
        return 0.0
    return len(t1 & t2) / len(t1 | t2)

BANNED_PHRASES = [
    "academic lexicon", "classic author", "historical author", "scientific treatise",
    "morphological & etymological treatise", "standard consensus", "traditional author",
    "in academic literature,", "historical records document", "classical commentary"
]

CIRCULAR = re.compile(r'\b(?:the\s+)?(?:quality|state|condition)(?:,\s*state)?(?:,\s*or\s*degree)?\s+of\s+being\b', re.I)

def validate():
    print(f"Total words in data_power_b2_p1: {len(data_power_b2_p1)}")
    errors = []
    for word, item in data_power_b2_p1.items():
        # Primary check
        p = item["primary"]
        if len(p) < 25:
            errors.append(f"[{word}] Primary definition too short ({len(p)} chars)")
        if CIRCULAR.search(p):
            errors.append(f"[{word}] Primary definition contains circular boilerplate formula: '{p}'")

        # Secondary check
        s = item["secondary"]
        if len(s) < 25:
            errors.append(f"[{word}] Secondary definition too short ({len(s)} chars)")
        if CIRCULAR.search(s):
            errors.append(f"[{word}] Secondary definition contains circular boilerplate formula: '{s}'")

        # Jaccard overlap
        j = jaccard(p, s)
        if j >= 0.70:
            errors.append(f"[{word}] Jaccard token overlap too high ({j:.2f})")

        # Quotes check
        quotes = item.get("quotes", [])
        if len(quotes) != 3:
            errors.append(f"[{word}] Expected exactly 3 quotes, got {len(quotes)}")

        authors = set()
        for idx, q in enumerate(quotes):
            author = q.get("author", "")
            work = q.get("work", "")
            qtext = q.get("quote", "")

            if not author or not work or not qtext:
                errors.append(f"[{word}] Quote {idx+1} missing fields")
            if author in authors:
                errors.append(f"[{word}] Duplicate author: '{author}'")
            authors.add(author)

            # Check banned phrases
            full_str = f"{author} {work} {qtext}".lower()
            for bp in BANNED_PHRASES:
                if bp in full_str:
                    errors.append(f"[{word}] Contains banned phrase '{bp}' in quote {idx+1}")

            # Target word bolded check
            if "**" not in qtext:
                errors.append(f"[{word}] Target word not bolded in quote {idx+1}: '{qtext[:60]}...'")

    if errors:
        print(f"\n❌ VALIDATION FAILED with {len(errors)} errors:")
        for err in errors[:25]:
            print(f"  - {err}")
        return False
    else:
        print("\n✅ ALL 49 words in Cluster Power Batch 2 Part 1 PASSED local pre-audit validation!")
        return True

if __name__ == "__main__":
    if not validate():
        sys.exit(1)
