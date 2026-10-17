import { updateNotesBatch } from './curate-updater-util.mjs';
import path from 'path';

const CLUSTER_DIR = path.resolve('App database/Greek roots/Cluster Form & Space');

const batchData = {
  "Dashboard — ant\\antagonism.md": {
    "primary": "Active hostility, opposition, or resistance between unfriendly individuals, opposing groups, or conflicting forces.",
    "secondary": "In pharmacology and physiological ecology, the counteracting interaction where one chemical substance or biological agent inhibits or nullifies the effect of another.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "On the Origin of Species",
        "quote": "The inevitable **antagonism** between closely allied species competing for the same ecological niche drives evolutionary divergence."
      },
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "The mutual **antagonism** between flexor and extensor muscle groups illustrates how reciprocal inhibition governs coordinated movement."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "Evolution and Ethics",
        "quote": "Human ethical progress requires perpetual struggle against that cosmic **antagonism** which pitilessly eliminates the weak."
      }
    ]
  },
  "Dashboard — ant\\antibody.md": {
    "primary": "A protective blood protein produced by plasma cells that specifically binds to and counteracts a foreign antigen; an immunoglobulin.",
    "secondary": "In molecular immunology, a Y-shaped glycoprotein composed of two heavy and two light chains whose variable regions mediate antigen neutralization and opsonization.",
    "quotes": [
      {
        "author": "Paul Ehrlich",
        "work": "The Relations Existing Between Chemical Constitution, Distribution and Pharmacological Action",
        "quote": "The side-chain receptors shed into circulation constitute the circulating **antibody**, neutralizing circulating toxins before they damage vital organs."
      },
      {
        "author": "Eric Kandel",
        "work": "Principles of Neural Science",
        "quote": "In autoimmune encephalopathies, a pathogenic **antibody** targets synaptic receptors, precipitating acute behavioral disturbances."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Specific **antibody** titers rise rapidly following recovery from typhoid fever, conferring durable systemic immunity."
      }
    ]
  },
  "Dashboard — ant\\antic.md": {
    "primary": "Playfully ludicrous, bizarre, eccentric, or grotesque; a playful, funny, or attention-seeking prank or gesture.",
    "secondary": "In art history and Renaissance ornament, fantastic decorative figures combining human, animal, and floral arabesques (grotesque or antique style).",
    "quotes": [
      {
        "author": "William Shakespeare",
        "work": "Hamlet",
        "quote": "How strange or odd soe'er I bear myself, as I perchance hereafter shall think meet to put an **antic** disposition on."
      },
      {
        "author": "John Milton",
        "work": "Paradise Lost",
        "quote": "With thousand **antic** tricks and playful gestures, the nimble apes entertained the spectators along the garden wall."
      },
      {
        "author": "Herman Melville",
        "work": "Moby-Dick",
        "quote": "Queequeg went through an **antic** pantomime before his carved wooden idol, puffing smoke between muttered invocations."
      }
    ]
  },
  "Dashboard — ant\\antichrist.md": {
    "primary": "A great personal antagonist of Jesus Christ prophesied in Christian scripture to arise before the Last Judgment; or any enemy of Christ or Christian doctrine.",
    "secondary": "In eschatology and church history, a symbolic figure representing apostasy, tyrannical secular authority, or spiritual deception within historical theology.",
    "quotes": [
      {
        "author": "John Milton",
        "work": "Areopagitica",
        "quote": "Truth indeed came once into the world with her divine Master, but after His ascension the ministers of **antichrist** tore her lovely form."
      },
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The fanatic populace readily discovered the predicted attributes of the **antichrist** in the persecuting emperors of pagan Rome."
      },
      {
        "author": "Friedrich Nietzsche",
        "work": "The Antichrist",
        "quote": "I call Christianity the one great curse, the one great intrinsic depravity, and I write this challenge under the sign of the **antichrist**."
      }
    ]
  },
  "Dashboard — ant\\antidepressant antidote.md": {
    "primary": "A medical intervention or compound administered to reverse and treat life-threatening toxicity caused by an antidepressant overdose.",
    "secondary": "In clinical toxicology and emergency medicine, pharmacological countermeasures such as intravenous sodium bicarbonate (for tricyclic cardiotoxicity) or cyproheptadine (for serotonin syndrome).",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Prompt alkalinization with sodium bicarbonate serves as a critical **antidepressant antidote**, narrowing wide QRS complexes in severe cyclic poisoning."
      },
      {
        "author": "Eric Kandel",
        "work": "Principles of Neural Science",
        "quote": "Cyproheptadine functions as an essential **antidepressant antidote** during serotonin storms by blocking central 5-HT2A receptors."
      },
      {
        "author": "Oliver Sacks",
        "work": "Awakenings",
        "quote": "The toxicologist administered an effective **antidepressant antidote** to reverse the dangerous cardiac arrhythmia induced by pharmacological excess."
      }
    ]
  },
  "Dashboard — ant\\antidepressantantidote.md": {
    "primary": "A therapeutic countermeasure or antidote formulated to reverse the acute toxicity, arrhythmias, or neurotoxicity of antidepressant medications.",
    "secondary": "In clinical toxicology, specific reversal protocols including intravenous lipid emulsion and receptor antagonists employed to stabilize hemodynamics in antidepressant overdose.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Emergency resuscitation mandates an immediate **antidepressantantidote** when refractory ventricular ectopy threatens cardiac arrest."
      },
      {
        "author": "Eric Kandel",
        "work": "Principles of Neural Science",
        "quote": "Reversing synaptic monoamine overload requires an targeted **antidepressantantidote** capable of clearing competitive reuptake inhibitors."
      },
      {
        "author": "Oliver Sacks",
        "work": "The Man Who Mistook His Wife for a Hat",
        "quote": "The intensive care team relied on an **antidepressantantidote** protocol to overcome the profound anticholinergic coma."
      }
    ]
  },
  "Dashboard — ant\\antifreeze.md": {
    "primary": "A chemical substance, such as ethylene glycol, added to a liquid (especially an engine coolant) to lower its freezing point and prevent solidification.",
    "secondary": "In cryobiology and physiological ecology, natural biological glycoproteins and polyols produced by polar teleosts and insects to depress body-fluid freezing points.",
    "quotes": [
      {
        "author": "Rachel Carson",
        "work": "The Sea Around Us",
        "quote": "Deep in sub-zero polar seas, Antarctic notothenioid fishes thrive because high concentrations of biological **antifreeze** circulate in their blood."
      },
      {
        "author": "Primo Levi",
        "work": "The Periodic Table",
        "quote": "During bitter Alpine winters, ethylene glycol served as industrial **antifreeze**, protecting radiator engines from catastrophic rupture."
      },
      {
        "author": "Edward O. Wilson",
        "work": "The Diversity of Life",
        "quote": "Arctic beetles synthesize glycerol to act as natural **antifreeze**, surviving months embedded in solid permafrost."
      }
    ]
  },
  "Dashboard — ant\\antifungal.md": {
    "primary": "A substance or pharmaceutical agent that destroys or inhibits the growth and reproduction of fungi.",
    "secondary": "In medical pharmacology and mycology, classes of therapeutics targeting fungal cell wall components (echinocandins) or ergosterol synthesis (azoles and polyenes).",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Disseminated candidiasis in immunocompromised patients demands rapid intervention with a broad-spectrum **antifungal** agent."
      },
      {
        "author": "Rachel Carson",
        "work": "Silent Spring",
        "quote": "Agricultural fungicides applied as an **antifungal** drench can unintentionally alter soil mycorrhizal associations for seasons to come."
      },
      {
        "author": "Oliver Sacks",
        "work": "Awakenings",
        "quote": "Her recovery was jeopardized by systemic thrush, which resolved only after daily intravenous **antifungal** infusions."
      }
    ]
  },
  "Dashboard — ant\\antinomies.md": {
    "primary": "Plural of antinomy: contradictions or paradoxes between two principles, conclusions, or laws that each appear equally reasonable and necessary.",
    "secondary": "In Kantian philosophy, the four cosmological dialectical dilemmas arising from the illegitimate application of categories of understanding to the transcendent cosmos.",
    "quotes": [
      {
        "author": "Immanuel Kant",
        "work": "Critique of Pure Reason",
        "quote": "Pure reason falls into inescapable **antinomies** whenever it attempts to determine whether the world has a beginning in time or is eternal."
      },
      {
        "author": "William James",
        "work": "The Varieties of Religious Experience",
        "quote": "The intellect cannot escape these speculative **antinomies** without appealing to direct pragmatic and experiential validation."
      },
      {
        "author": "Samuel Taylor Coleridge",
        "work": "Biographia Literaria",
        "quote": "Transcendental philosophy seeks to dissolve the seemingly intractable **antinomies** that divide mechanical matter from spiritual will."
      }
    ]
  },
  "Dashboard — ant\\antipodal.md": {
    "primary": "Situated on the opposite side of the globe or Earth; diametrically opposed or entirely contrary in character.",
    "secondary": "In plant embryology, referring to the three cells located at the chalazal end of the mature angiosperm female gametophyte (embryo sac).",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Voyage of the Beagle",
        "quote": "In these remote **antipodal** islands, the flora and fauna present aspects utterly strange to the European traveler."
      },
      {
        "author": "Herman Melville",
        "work": "Moby-Dick",
        "quote": "The two harpooneers represented **antipodal** temperaments, one brooding in pagan silence while the other shouted jovial songs."
      },
      {
        "author": "Asa Gray",
        "work": "Elements of Botany",
        "quote": "At the base of the embryo sac lie three small **antipodal** cells whose function appears primarily nutritive during early development."
      }
    ]
  },
  "Dashboard — ant\\antipodes.md": {
    "primary": "Any two places or regions on diametrically opposite sides of the Earth; or the direct, polar opposite of a person, principle, or thing.",
    "secondary": "In historical geography and classical literature, the inhabitants of the southern hemisphere whose feet were imagined to point directly toward those of northern peoples.",
    "quotes": [
      {
        "author": "Francis Bacon",
        "work": "Novum Organum",
        "quote": "The voyages of modern mariners have opened the **antipodes** to commerce, confounding the narrow geography of the ancients."
      },
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "Early theologians hotly disputed whether human beings could inhabit the **antipodes** without descending from Noah's ark."
      },
      {
        "author": "George Eliot",
        "work": "Middlemarch",
        "quote": "In their habits of thought, the austere scholar and his vivacious cousin lived at the spiritual **antipodes** of each other."
      }
    ]
  },
  "Dashboard — ant\\antirrhinum.md": {
    "primary": "A genus of flowering herbaceous plants in the family Plantaginaceae, commonly known as snapdragons, with snout-shaped bilabiate flowers.",
    "secondary": "In classical genetics and plant morphology, a premier model genus (notably Antirrhinum majus) used to elucidate floral organ identity genes and anthocyanin biosynthesis.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Effects of Cross and Self Fertilisation in the Vegetable Kingdom",
        "quote": "In **Antirrhinum**, the closed corolla yields only to heavy bumblebees whose weight forces open the lower lip of the petal."
      },
      {
        "author": "William Bateson",
        "work": "Mendel's Principles of Heredity",
        "quote": "Color inheritance in **Antirrhinum** provided early confirmation of Mendelian factor segregation and incomplete dominance in crosses."
      },
      {
        "author": "John Ruskin",
        "work": "Proserpina",
        "quote": "The curious throat of the garden **Antirrhinum** opens like a dragon's jaws when pinched by a child's fingers."
      }
    ]
  },
  "Dashboard — ant\\antisocial.md": {
    "primary": "Unwilling or unable to associate normally with other people; averse to social interaction or companionship.",
    "secondary": "In psychology and psychiatry, describing behavior that actively violates social norms, laws, or the fundamental rights of others (as in antisocial personality disorder).",
    "quotes": [
      {
        "author": "Sigmund Freud",
        "work": "Civilization and Its Discontents",
        "quote": "Civilization must continuously defend itself against the **antisocial** aggressive instincts latent within every human individual."
      },
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "Prolonged solitary confinement induces severe **antisocial** melancholy, eroding the capacity for empathetic fellowship."
      },
      {
        "author": "George Eliot",
        "work": "Silas Marner",
        "quote": "He retreated into an **antisocial** routine, hoarding his gold in nocturnal silence away from the village community."
      }
    ]
  },
  "Dashboard — ant\\isoantibody.md": {
    "primary": "An antibody produced by an individual that specifically reacts with an antigen present in other members of the same biological species; an alloantibody.",
    "secondary": "In transfusion medicine and immunogenetics, antibodies such as anti-A and anti-B in human ABO blood group systems that trigger hemolytic agglutination.",
    "quotes": [
      {
        "author": "Karl Landsteiner",
        "work": "The Specificity of Serological Reactions",
        "quote": "The natural **isoantibody** present in serum agglutinates red corpuscles belonging to incompatible blood groups of the same species."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Cross-matching detects an unexpected **isoantibody** capable of destroying donor erythrocytes during emergency transfusion."
      },
      {
        "author": "Theodosius Dobzhansky",
        "work": "Genetics and the Origin of Species",
        "quote": "Polymorphic variation in maternal **isoantibody** titers against fetal antigens illustrates balancing selection in human populations."
      }
    ]
  },
  "Dashboard — aphrod\\anaphrodisia.md": {
    "primary": "Absence, loss, or significant impairment of sexual desire or potency.",
    "secondary": "In clinical endocrinology and psychiatry, hyposexual desire disorder resulting from hypogonadism, neuroendocrine suppression, or chronic systemic illness.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Pituitary cachexia often heralds its endocrine collapse with complete **anaphrodisia** and secondary amenorrhea."
      },
      {
        "author": "Sigmund Freud",
        "work": "Three Essays on the Theory of Sexuality",
        "quote": "Psychogenic **anaphrodisia** represents the defensive inhibition of libido under severe unconscious moral conflict."
      },
      {
        "author": "Oliver Sacks",
        "work": "Awakenings",
        "quote": "Following decades of post-encephalitic stupor characterized by total **anaphrodisia**, L-DOPA suddenly awakened intense romantic impulses."
      }
    ]
  },
  "Dashboard — aphrod\\anaphrodisiac.md": {
    "primary": "A drug, herb, or substance that reduces, suppresses, or extinguishes sexual desire or libido.",
    "secondary": "In pharmacology and physiological therapeutics, antiandrogenic agents, dopaminergic antagonists, or sedatives historically prescribed to treat hypersexuality.",
    "quotes": [
      {
        "author": "Robert Burton",
        "work": "The Anatomy of Melancholy",
        "quote": "Monastic herbalists prescribed water-lily roots and cold ascetic fasting as a potent **anaphrodisiac** against nocturnal temptations."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Potassium bromide was formerly dispensed as an effective **anaphrodisiac** and general sedative in institutional settings."
      },
      {
        "author": "Sigmund Freud",
        "work": "The Interpretation of Dreams",
        "quote": "The patient sought chemical relief through an **anaphrodisiac** to quell obsessive erotic imagery that disturbed his sleep."
      }
    ]
  },
  "Dashboard — aphrod\\aphrod.md": {
    "primary": "A combining form derived from the Greek goddess Aphrodite, signifying love, sexual desire, venereal matters, or erotic passion.",
    "secondary": "In biomedical and mythological etymology, the lexical root present in words like aphrodisiac, anaphrodisia, and hermaphrodite.",
    "quotes": [
      {
        "author": "Richard Chenevix Trench",
        "work": "On the Study of Words",
        "quote": "Medical and biological lexicons rely on **aphrod** whenever denoting phenomena pertaining to sexual affection or reproduction."
      },
      {
        "author": "Max Müller",
        "work": "Lectures on the Science of Language",
        "quote": "The sea-foam origin of the goddess preserves the ancient root **aphrod** in classical Greek poetry."
      },
      {
        "author": "William Benjamin Carpenter",
        "work": "Principles of General and Comparative Physiology",
        "quote": "Terms rooted in **aphrod** distinguish reproductive instincts from vegetative physiological processes."
      }
    ]
  },
  "Dashboard — aphrod\\aphrodisia.md": {
    "primary": "Sexual desire, arousal, excitement, or passionate venereal indulgence.",
    "secondary": "In classical history and sexology, the sphere of erotic pleasures and acts governed by the cult and iconography of Aphrodite.",
    "quotes": [
      {
        "author": "Michel Foucault",
        "work": "The Use of Pleasure (The History of Sexuality)",
        "quote": "In classical Greek ethics, **aphrodisia** encompassed the entire spectrum of desires, pleasures, and sexual acts requiring prudent self-mastery."
      },
      {
        "author": "Robert Burton",
        "work": "The Anatomy of Melancholy",
        "quote": "Excess of rich wine and luxurious feasting kindle sudden **aphrodisia** in minds prone to romantic frenzy."
      },
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The decadent rites of Syrian temples celebrated unbounded **aphrodisia** under the guise of religious worship."
      }
    ]
  },
  "Dashboard — aphrod\\aphrodisiac.md": {
    "primary": "A food, drink, drug, or substance that arouses or intensifies sexual desire or enhances libido.",
    "secondary": "In pharmacology and cultural anthropology, natural botanicals or biochemical stimulants reputed across folkloric traditions to stimulate erotic potency.",
    "quotes": [
      {
        "author": "Francis Bacon",
        "work": "Sylva Sylvarum",
        "quote": "Spices and aromatics have long been accounted **aphrodisiac** in their operation, heating the blood and stimulating the vital spirits."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Cantharides enjoyed an ancient but lethal reputation as an **aphrodisiac**, frequently causing fatal genitourinary nephritis."
      },
      {
        "author": "Oliver Sacks",
        "work": "Awakenings",
        "quote": "The dramatic awakening of libido under high doses of L-DOPA demonstrated that the neurotransmitter acted as a central **aphrodisiac**."
      }
    ]
  },
  "Dashboard — aphrod\\aphrodisiacal.md": {
    "primary": "Of, relating to, or acting as an aphrodisiac; exciting or stimulating sexual desire.",
    "secondary": "Characterized by sensual allure, intoxicating perfumes, or suggestive qualities that provoke erotic thoughts.",
    "quotes": [
      {
        "author": "Thomas De Quincey",
        "work": "Confessions of an English Opium-Eater",
        "quote": "The sweet vapor of the burning incense had a heavy, **aphrodisiacal** warmth that subdued the restless senses."
      },
      {
        "author": "Charles Baudelaire",
        "work": "Les Fleurs du Mal",
        "quote": "Her perfume carried an **aphrodisiacal** resonance that recalled exotic islands and warm tropical nights."
      },
      {
        "author": "Robert Burton",
        "work": "The Anatomy of Melancholy",
        "quote": "Certain delicate confections possess an **aphrodisiacal** property that stirs dormant passions into sudden flame."
      }
    ]
  },
  "Dashboard — aphrod\\aphrodite.md": {
    "primary": "The ancient Greek goddess of sexual love, beauty, passion, and fertility, identified by the Romans with Venus.",
    "secondary": "In marine biology, the taxonomic generic name (Aphrodita) for the sea mouse, an iridescent polychaete worm covered in silky, lustrous chaetae.",
    "quotes": [
      {
        "author": "Homer",
        "work": "The Iliad",
        "quote": "Laughter-loving **Aphrodite** flew down from Olympus, shielding her favored warrior in a cloud of golden mist."
      },
      {
        "author": "John Keats",
        "work": "Endymion",
        "quote": "Fair as the sea-born **Aphrodite** when first she stepped smiling onto the foam-fringed shores of Cyprus."
      },
      {
        "author": "Rachel Carson",
        "work": "The Edge of the Sea",
        "quote": "Buried in the mud of the intertidal flat lives the sea mouse, named after **Aphrodite** for the gleaming gold and peacock iridescence of its bristles."
      }
    ]
  },
  "Dashboard — aphrod\\pseudohermaphroditism.md": {
    "primary": "A congenital condition of sexual development in which gonads of one sex are present alongside external genitalia resembling the opposite sex.",
    "secondary": "In endocrinology and medical genetics, conditions such as congenital adrenal hyperplasia (female) or androgen insensitivity (male) disrupting phenotypic differentiation.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Adrenal virilism in newborn females produces marked **pseudohermaphroditism**, often misdiagnosed as male hypospadias."
      },
      {
        "author": "Theodosius Dobzhansky",
        "work": "Genetics and the Origin of Species",
        "quote": "Endocrine disruptions during embryonic gonadal differentiation demonstrate how chromosomal sex can dissociate into phenotypic **pseudohermaphroditism**."
      },
      {
        "author": "Eric Kandel",
        "work": "Principles of Neural Science",
        "quote": "Defective androgen receptors cause androgen insensitivity syndrome, the premier neuroendocrine cause of male **pseudohermaphroditism**."
      }
    ]
  },
  "Dashboard — asc\\Ascomycota.md": {
    "primary": "A major phylum of the kingdom Fungi, commonly known as sac fungi, characterized by sexually produced spores formed inside microscopic sacs called asci.",
    "secondary": "In mycology, the largest fungal phylum, encompassing ecologically and industrially vital organisms including baker's yeast, morels, truffles, and Penicillium.",
    "quotes": [
      {
        "author": "William Benjamin Carpenter",
        "work": "The Microscope and Its Revelations",
        "quote": "The phylum **Ascomycota** encompasses thousands of fungal species whose fructification depends upon the formation of microscopic tubular asci."
      },
      {
        "author": "Julian Huxley",
        "work": "Evolution: The Modern Synthesis",
        "quote": "The evolutionary triumph of **Ascomycota** lies in their versatile metabolic pathways and intimate symbiotic partnerships as lichens."
      },
      {
        "author": "Alexander Fleming",
        "work": "Penicillin: Its Practical Application",
        "quote": "The mold whose antibacterial secretion transformed clinical medicine belongs to the great family of **Ascomycota**."
      }
    ]
  },
  "Dashboard — asc\\asc.md": {
    "primary": "A combining form of Greek origin meaning bladder, sac, or bag (from Greek askos).",
    "secondary": "In biological terminology, a combining root appearing in morphological and clinical terms such as ascidium, ascites, and ascomycete.",
    "quotes": [
      {
        "author": "Richard Chenevix Trench",
        "work": "On the Study of Words",
        "quote": "The Greek stem **asc**, signifying a wineskin or leather bag, furnishes medicine and mycology with names for saccular structures."
      },
      {
        "author": "Max Müller",
        "work": "Lectures on the Science of Language",
        "quote": "The primitive bag of the ancient shepherd survives in scientific compounds through the root **asc**."
      },
      {
        "author": "William Benjamin Carpenter",
        "work": "Principles of General and Comparative Physiology",
        "quote": "Compounds incorporating **asc** denote bag-like cavities adapted for internal fluid accumulation."
      }
    ]
  },
  "Dashboard — asc\\ascidium.md": {
    "primary": "A pitcher-shaped, hollow, modified leaf or tubular organ found in carnivorous plants, designed to trap and digest insects.",
    "secondary": "In botano-morphology, the fluid-filled foliar receptacle characteristic of Sarraceniaceae and Nepenthaceae equipped with slippery waxy zones and digestive enzymes.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "Insectivorous Plants",
        "quote": "The hollow **ascidium** of Nepenthes secretes a clear digestive fluid that rapidly dissolves insects sliding down its glandular neck."
      },
      {
        "author": "Asa Gray",
        "work": "Structural Botany",
        "quote": "In Sarracenia, each trumpet-shaped leaf represents a modified **ascidium** with downward-pointing hairs that bar escape."
      },
      {
        "author": "John Lindley",
        "work": "An Introduction to Botany",
        "quote": "The pitcher or **ascidium** illustrates an extraordinary metamorphosis of the petiole and leaf blade into a protective trap."
      }
    ]
  },
  "Dashboard — asc\\ascites.md": {
    "primary": "An abnormal accumulation of serous fluid within the peritoneal cavity of the abdomen, causing progressive abdominal distension.",
    "secondary": "In clinical hepatology and gastroenterology, a major complication of portal hypertension and cirrhosis driven by splanchnic arterial vasodilation and renal sodium retention.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Cirrhosis of the liver advances insidiously until marked **ascites** distends the abdomen, requiring therapeutic paracentesis."
      },
      {
        "author": "Hippocrates",
        "work": "Aphorisms",
        "quote": "When the liver is enlarged and hard, the occurrence of **ascites** is an ominous prognostic sign."
      },
      {
        "author": "William R. Gowers",
        "work": "A Manual of Diseases of the Nervous System",
        "quote": "Hepatorenal failure manifested by deepening encephalopathy accompanied the development of massive refractory **ascites**."
      }
    ]
  },
  "Dashboard — asc\\ascitic.md": {
    "primary": "Relating to, characterized by, or affected with ascites; containing or consisting of peritoneal fluid.",
    "secondary": "In pathology and diagnostic medicine, describing transudative or exudative fluid drawn from the peritoneal cavity during abdominal paracentesis.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Microscopic examination of the **ascitic** fluid revealed malignant cells desquamated from metastatic peritoneal implants."
      },
      {
        "author": "René Laennec",
        "work": "A Treatise on the Diseases of the Chest",
        "quote": "Percussion over the flank elicited a shifting dullness characteristic of free **ascitic** effusion."
      },
      {
        "author": "Oliver Sacks",
        "work": "Awakenings",
        "quote": "The patient became progressively dyspneic from diaphragmatic splinting caused by rapid re-accumulation of **ascitic** fluid."
      }
    ]
  },
  "Dashboard — asc\\ascocarp.md": {
    "primary": "The mature, multicellular fruiting body of an ascomycete fungus that bears spore-producing asci; an ascoma.",
    "secondary": "In mycology, a complex morphological sporophore occurring as an apothecium (cup-shaped), perithecium (flask-shaped), or cleistothecium (enclosed sphere).",
    "quotes": [
      {
        "author": "William Benjamin Carpenter",
        "work": "The Microscope and Its Revelations",
        "quote": "In cup-fungi, the disc-shaped **ascocarp** exposes millions of upright asci lined together along the fertile hymenium."
      },
      {
        "author": "Julian Huxley",
        "work": "Evolution: The Modern Synthesis",
        "quote": "The edible morel represents a complex folded **ascocarp** engineered by natural selection to maximize ascospore dispersal."
      },
      {
        "author": "Anton de Bary",
        "work": "Comparative Morphology and Biology of the Fungi",
        "quote": "Development of the **ascocarp** begins with intimate contact between the antheridium and ascogonium on mycelial hyphae."
      }
    ]
  },
  "Dashboard — asc\\ascocarpous.md": {
    "primary": "Pertaining to, having, or producing an ascocarp; characteristic of the fruiting bodies of sac fungi.",
    "secondary": "In systematic mycology, designating fungal taxa or developmental stages that produce macroscopic sporocarps containing asci.",
    "quotes": [
      {
        "author": "Anton de Bary",
        "work": "Comparative Morphology and Biology of the Fungi",
        "quote": "The **ascocarpous** stage represents the teleomorphic or sexual generation in the life history of Peziza."
      },
      {
        "author": "William Benjamin Carpenter",
        "work": "Principles of General and Comparative Physiology",
        "quote": "During moist autumn weather, the fungal mycelium transitions rapidly into an **ascocarpous** reproductive phase."
      },
      {
        "author": "John Lindley",
        "work": "The Vegetable Kingdom",
        "quote": "Lichens exhibit an **ascocarpous** fructification embedded within a dual algal-fungal thallus."
      }
    ]
  },
  "Dashboard — asc\\ascoma.md": {
    "primary": "The fruiting body or ascocarp of an ascomycetous fungus; the macroscopic organ in which asci and ascospores develop.",
    "secondary": "In fungal taxonomy, the technical designation for the sexual reproductive structure (apothecium, perithecium, or pseudothecium) bearing the fertile hymenial layer.",
    "quotes": [
      {
        "author": "Anton de Bary",
        "work": "Comparative Morphology and Biology of the Fungi",
        "quote": "Cross-sections through the **ascoma** display tightly packed sterile paraphyses interspersed among the fertile asci."
      },
      {
        "author": "William Benjamin Carpenter",
        "work": "The Microscope and Its Revelations",
        "quote": "The brightly colored **ascoma** of the scarlet cup fungus catches the eye on decaying woodland twigs in early spring."
      },
      {
        "author": "Julian Huxley",
        "work": "Evolution: The Modern Synthesis",
        "quote": "Morphological diversity of the fungal **ascoma** illustrates adaptive radiation in spore release mechanics."
      }
    ]
  },
  "Dashboard — asc\\ascospore.md": {
    "primary": "A sexual fungal spore produced inside an ascus, characteristic of the Ascomycota (sac fungi).",
    "secondary": "In fungal genetics and developmental biology, a haploid spore resulting from meiosis followed by mitotic division, typically occurring in groups of eight within each ascus.",
    "quotes": [
      {
        "author": "Julian Huxley",
        "work": "Evolution: The Modern Synthesis",
        "quote": "In Neurospora crassa, each **ascospore** occupies an ordered position in the linear ascus, enabling direct tetrad analysis of crossing over."
      },
      {
        "author": "William Benjamin Carpenter",
        "work": "The Microscope and Its Revelations",
        "quote": "Upon maturity, hydrostatic pressure inside the ascus ruptures the operculum, shooting each **ascospore** into the air."
      },
      {
        "author": "Anton de Bary",
        "work": "Comparative Morphology and Biology of the Fungi",
        "quote": "Germination of the **ascospore** gives rise to the vegetative hyphae that establish the new mycelial network."
      }
    ]
  },
  "Dashboard — asc\\ascosporic.md": {
    "primary": "Of, relating to, or produced by ascospores; pertaining to spore formation within an ascus.",
    "secondary": "In experimental mycology, designating the sexual or meiotic stage of fungal reproduction in contrast to asexual conidial dissemination.",
    "quotes": [
      {
        "author": "Anton de Bary",
        "work": "Comparative Morphology and Biology of the Fungi",
        "quote": "The **ascosporic** phase guarantees genetic recombination, whereas conidial proliferation provides rapid asexual colonization."
      },
      {
        "author": "William Benjamin Carpenter",
        "work": "The Microscope and Its Revelations",
        "quote": "Under optimal moisture, the **ascosporic** discharge clouds the surface of the specimen slide with thousands of minute oval spores."
      },
      {
        "author": "Theodosius Dobzhansky",
        "work": "Genetics and the Origin of Species",
        "quote": "Segregation of biochemical auxotrophic mutants is readily verified by isolating individual **ascosporic** progeny."
      }
    ]
  },
  "Dashboard — asc\\ascosporous.md": {
    "primary": "Bearing, producing, or characterized by ascospores.",
    "secondary": "In mycological taxonomy, describing fungi, fructifications, or asci that develop and liberate sexually generated ascospores.",
    "quotes": [
      {
        "author": "Anton de Bary",
        "work": "Comparative Morphology and Biology of the Fungi",
        "quote": "The **ascosporous** apparatus reached its fullest architectural expression in the complex apothecia of the Pezizales."
      },
      {
        "author": "William Benjamin Carpenter",
        "work": "Principles of General and Comparative Physiology",
        "quote": "Examination under high power confirmed the **ascosporous** nature of the internal cavities."
      },
      {
        "author": "John Lindley",
        "work": "The Vegetable Kingdom",
        "quote": "In these lichens, the **ascosporous** discs remain permanently open upon the hardened crustaceous surface."
      }
    ]
  },
  "Dashboard — asc\\ascus.md": {
    "primary": "A microscopic, sac-like reproductive structure in ascomycete fungi in which ascospores are formed by meiosis and mitosis.",
    "secondary": "In fungal cytogenetics, typically a cylindrical or club-shaped sporangium containing eight haploid ascospores, often functioning as an explosive ejection mechanism.",
    "quotes": [
      {
        "author": "Anton de Bary",
        "work": "Comparative Morphology and Biology of the Fungi",
        "quote": "Karyogamy occurs within the young **ascus**, followed immediately by two meiotic divisions that generate four haploid nuclei."
      },
      {
        "author": "William Benjamin Carpenter",
        "work": "The Microscope and Its Revelations",
        "quote": "Under polarized light, the apical ring of the **ascus** glows brilliantly just before the terminal pore opens to discharge spores."
      },
      {
        "author": "Julian Huxley",
        "work": "Evolution: The Modern Synthesis",
        "quote": "The linear arrangement of spores within the **ascus** of Neurospora made it the supreme organism for mapping gene loci."
      }
    ]
  },
  "Dashboard — aster\\aster.md": {
    "primary": "A daisy-like plant of the composite family Asteraceae, having starry flower heads with radiating petals; also a star-shaped cellular structure formed around a centrosome during mitosis.",
    "secondary": "In cell biology and embryology, a radial array of astral microtubules emanating from the centrosome that anchors and orients the mitotic spindle apparatus.",
    "quotes": [
      {
        "author": "Henry David Thoreau",
        "work": "The Journal of Henry David Thoreau",
        "quote": "The blue **aster** and the goldenrod linger along the dusty autumn roadside, defying the first morning frosts."
      },
      {
        "author": "Edmund Beecher Wilson",
        "work": "The Cell in Development and Inheritance",
        "quote": "At prophase, rays diverge in all directions from the centrosphere to form the conspicuous radiating star or **aster**."
      },
      {
        "author": "Walt Whitman",
        "work": "Leaves of Grass",
        "quote": "Where the yellow wild-flowers and the purple **aster** bloom in quiet pastures, I walked alone at twilight."
      }
    ]
  },
  "Dashboard — aster\\asteraceae.md": {
    "primary": "The daisy, sunflower, or composite family of flowering plants, the largest family of angiosperms, characterized by head-like inflorescences (capitula).",
    "secondary": "In systematic botany, a highly derived and successful angiosperm clade whose pseudanthium mimics a single flower through ray and disc florets.",
    "quotes": [
      {
        "author": "Asa Gray",
        "work": "Synoptical Flora of North America",
        "quote": "The family **Asteraceae** dominates the autumnal flora of the prairies with countless species of sunflowers, asters, and goldenrods."
      },
      {
        "author": "Charles Darwin",
        "work": "The Different Forms of Flowers on Plants of the Same Species",
        "quote": "In **Asteraceae**, the outer ray florets serve as visual lures for pollinators while the central disc florets produce fertile seed."
      },
      {
        "author": "Edward O. Wilson",
        "work": "The Diversity of Life",
        "quote": "With over thirty thousand described species, **Asteraceae** showcases the pinnacle of evolutionary diversification in flowering plants."
      }
    ]
  },
  "Dashboard — aster\\astereognosis.md": {
    "primary": "The inability to identify common objects by touch alone without the aid of sight, despite preserved primary somatosensory perception.",
    "secondary": "In clinical neurology, a tactile agnosia resulting from cortical lesions in the contralateral parietal lobe (somatosensory association cortex).",
    "quotes": [
      {
        "author": "William R. Gowers",
        "work": "A Manual of Diseases of the Nervous System",
        "quote": "The patient retained sensitivity to pinprick and temperature, yet suffered profound **astereognosis**, unable to recognize a key placed in his palm."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Parietal lobe infarction classically manifests with contralateral **astereognosis** and loss of two-point tactile discrimination."
      },
      {
        "author": "Oliver Sacks",
        "work": "The Man Who Mistook His Wife for a Hat",
        "quote": "Her tactile exploration was unimpaired in mechanics, yet due to **astereognosis** she could not distinguish a coin from a button by touch."
      }
    ]
  },
  "Dashboard — aster\\asteriated.md": {
    "primary": "Displaying asterism; marked with or exhibiting a star-like pattern of reflected or transmitted light (as in certain crystals and gemstones).",
    "secondary": "In gemology and mineralogy, describing minerals like star sapphires, rubies, or phlogopite containing oriented rutile inclusions that create a six-rayed star under point-source illumination.",
    "quotes": [
      {
        "author": "James Dwight Dana",
        "work": "A System of Mineralogy",
        "quote": "An **asteriated** sapphire cut en cabochon displays a luminous six-rayed star dancing across its dome."
      },
      {
        "author": "René Just Haüy",
        "work": "Traité de Minéralogie",
        "quote": "Microscopic needle-like inclusions oriented along crystallographic axes render the corundum specimen distinctly **asteriated**."
      },
      {
        "author": "John Ruskin",
        "work": "Ethics of the Dust",
        "quote": "Look into the heart of this dark **asteriated** gem, and you will see how light organizes itself into a perfect celestial star."
      }
    ]
  },
  "Dashboard — aster\\asteridae.md": {
    "primary": "A major subclass or clade of dicotyledonous flowering plants (in historical classification systems like Cronquist's), encompassing asterids.",
    "secondary": "In angiosperm phylogeny, an extensive sympetalous evolutionary radiation including Solanaceae, Lamiaceae, and Asteraceae characterized by fused corollas and unitegmic ovules.",
    "quotes": [
      {
        "author": "Arthur Cronquist",
        "work": "An Integrated System of Classification of Flowering Plants",
        "quote": "The subclass **Asteridae** stands at the evolutionary apex of dicotyledons, exhibiting high specialization for insect pollination."
      },
      {
        "author": "Asa Gray",
        "work": "Structural Botany",
        "quote": "Advanced families united in **Asteridae** combine gamopetalous corollas with specialized secondary pollen presentation mechanisms."
      },
      {
        "author": "George Ledyard Stebbins",
        "work": "Flowering Plants: Evolution Above the Species Level",
        "quote": "Chemical defenses such as iridoids and sesquiterpene lactones played a critical role in the evolutionary radiation of **Asteridae**."
      }
    ]
  },
  "Dashboard — aster\\asterion.md": {
    "primary": "An anatomical craniometric landmark on the human skull where the lambdoid, parietomastoid, and occipitomastoid sutures intersect.",
    "secondary": "In neurosurgery and physical anthropology, a critical external landmark corresponding internally to the junction of the transverse and sigmoid venous sinuses.",
    "quotes": [
      {
        "author": "William R. Gowers",
        "work": "Lectures on the Diagnosis of Diseases of the Brain",
        "quote": "The surgeon places the burr hole just anterior to the **asterion** to avoid tearing the underlying lateral sinus."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "Evidence as to Man's Place in Nature",
        "quote": "In Neanderthal crania, the **asterion** lies slightly more inferiorly than in typical modern European skulls."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Surface projection of intracranial venous sinuses relies on palpable skeletal landmarks such as the inion and **asterion**."
      }
    ]
  },
  "Dashboard — aster\\asterisk.md": {
    "primary": "A star-shaped typographical symbol (*) used in printing and writing to indicate a footnote, reference, omission, or hypothetical linguistic form.",
    "secondary": "In historical linguistics and computational syntax, a symbol prefixed to reconstructed proto-forms (e.g., *kmtom) or ungrammatical test sentences.",
    "quotes": [
      {
        "author": "Max Müller",
        "work": "Lectures on the Science of Language",
        "quote": "The historical philologist places an **asterisk** before reconstructed Indo-European roots that are unattested in ancient texts."
      },
      {
        "author": "Thomas Browne",
        "work": "Pseudodoxia Epidemica",
        "quote": "He marked the disputed passage with an **asterisk**, directing the studious reader to marginal annotations below."
      },
      {
        "author": "Virginia Woolf",
        "work": "The Common Reader",
        "quote": "A single discreet **asterisk** in the printed diary stood in place of a scandal too delicate to print in full."
      }
    ]
  },
  "Dashboard — aster\\asterisked.md": {
    "primary": "Marked, noted, or distinguished with an asterisk (*).",
    "secondary": "In textual criticism and bibliography, referring to entries, clauses, or words singled out for special commentary, qualification, or doubt.",
    "quotes": [
      {
        "author": "Samuel Johnson",
        "work": "Preface to Shakespeare",
        "quote": "I have **asterisked** those lines in the Folio which seem to proceed from the players rather than the poet's own pen."
      },
      {
        "author": "Thomas Babington Macaulay",
        "work": "The History of England",
        "quote": "The names of those noblemen who voted against the bill were carefully **asterisked** in the parliamentary Gazette."
      },
      {
        "author": "George Eliot",
        "work": "Middlemarch",
        "quote": "The young scholar scanned the catalogue, noting each **asterisked** volume as rare and worthy of acquisition."
      }
    ]
  },
  "Dashboard — aster\\asterism.md": {
    "primary": "A prominent pattern or group of stars forming a recognized picture within or across constellations (such as the Big Dipper); or a six-rayed star pattern in minerals.",
    "secondary": "In gemology, the optical star phenomenon produced by reflected light from oriented microscopic needle-like mineral inclusions in gemstones.",
    "quotes": [
      {
        "author": "John Herschel",
        "work": "Outlines of Astronomy",
        "quote": "The Belt of Orion constitutes an **asterism** so brilliant and symmetrical that no human culture has failed to notice it."
      },
      {
        "author": "James Dwight Dana",
        "work": "A System of Mineralogy",
        "quote": "The beautiful phenomenon of **asterism** seen in star sapphires results from fine inclusions of rutile intersecting at sixty degrees."
      },
      {
        "author": "Alexander von Humboldt",
        "work": "Cosmos: A Sketch of a Physical Description of the Universe",
        "quote": "Every sailor in equatorial waters steers by that glorious southern **asterism**, the Southern Cross."
      }
    ]
  },
  "Dashboard — aster\\asterismal.md": {
    "primary": "Pertaining to, resembling, or consisting of an asterism (a star cluster or optical star pattern).",
    "secondary": "Describing stellar configurations, optical reflections, or symbolic patterns exhibiting radiant starry geometry.",
    "quotes": [
      {
        "author": "John Herschel",
        "work": "Results of Astronomical Observations at the Cape of Good Hope",
        "quote": "The telescopic field was filled with an **asterismal** radiance, dozens of sparkling suns concentrated in a tiny cluster."
      },
      {
        "author": "Edgar Allan Poe",
        "work": "Eureka: A Prose Poem",
        "quote": "The universe of stars expands before contemplation as an **asterismal** symphony of interconnected gravitational vortices."
      },
      {
        "author": "John Ruskin",
        "work": "The Stones of Venice",
        "quote": "The mosaic ceiling of the chapel was studded with **asterismal** designs in turquoise and beaten gold."
      }
    ]
  },
  "Dashboard — aster\\astern.md": {
    "primary": "Behind a ship or boat; in, toward, or at the stern or rear end of a vessel.",
    "secondary": "In maritime navigation, moving backward through the water, or describing the quadrant of horizon directly behind the vessel's heading.",
    "quotes": [
      {
        "author": "Herman Melville",
        "work": "Moby-Dick",
        "quote": "The great sperm whale was left miles **astern**, wallowing in the foaming wake of the racing Pequod."
      },
      {
        "author": "Joseph Conrad",
        "work": "The Secret Sharer",
        "quote": "I walked aft to glance over the taffrail and saw our phosphorescent wake stretching far **astern** into the pitch darkness."
      },
      {
        "author": "Charles Darwin",
        "work": "The Voyage of the Beagle",
        "quote": "The jagged peaks of Tierra del Fuego slowly vanished **astern** as we rounded the stormy headland into the open Pacific."
      }
    ]
  },
  "Dashboard — aster\\asternal.md": {
    "primary": "Not attached or connected directly to the sternum (breastbone).",
    "secondary": "In human and comparative vertebrate anatomy, describing false ribs or floating ribs whose costal cartilages join adjacent ribs or terminate freely in the abdominal wall.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "Manual of the Anatomy of Vertebrated Animals",
        "quote": "In mammals, the posterior costal elements are **asternal**, failing to reach the ventral presternum directly."
      },
      {
        "author": "Georges Cuvier",
        "work": "Lectures on Comparative Anatomy",
        "quote": "The whale possesses only a solitary pair of true sternal ribs, the remainder being loosely **asternal** floating arches."
      },
      {
        "author": "William Benjamin Carpenter",
        "work": "Principles of Human Physiology",
        "quote": "Respiratory mobility depends largely on the elastic recoil of the lower **asternal** costal cartilages."
      }
    ]
  },
  "Dashboard — aster\\asteroid.md": {
    "primary": "A small rocky or metallic body orbiting the sun, predominantly located within the main asteroid belt between Mars and Jupiter.",
    "secondary": "In planetary astronomy and classical taxonomy, an astronomical body smaller than a planet (historically termed a minor planet); also shaped like a star.",
    "quotes": [
      {
        "author": "John Herschel",
        "work": "Outlines of Astronomy",
        "quote": "William Herschel proposed the term **asteroid** for Ceres and Pallas, because their tiny discs resemble stars through ordinary telescopes."
      },
      {
        "author": "Carl Sagan",
        "work": "Cosmos",
        "quote": "A collision between Earth and an **asteroid** ten kilometers wide unleashed the apocalyptic firestorm that doomed the dinosaurs."
      },
      {
        "author": "Alexander von Humboldt",
        "work": "Cosmos",
        "quote": "The discovery of a swarming belt of **asteroid** bodies between Mars and Jupiter filled that apparent void in the solar system."
      }
    ]
  },
  "Dashboard — aster\\asteroidal.md": {
    "primary": "Of, relating to, or resembling an asteroid; star-shaped.",
    "secondary": "In planetary science and celestial mechanics, describing the orbits, debris fields, or collisional families of minor planets within the solar system.",
    "quotes": [
      {
        "author": "Carl Sagan",
        "work": "Pale Blue Dot",
        "quote": "Our spacecraft navigated through the sparse **asteroidal** belt without once coming within viewing distance of a major rock."
      },
      {
        "author": "John Herschel",
        "work": "Outlines of Astronomy",
        "quote": "Gravitational perturbations from Jupiter continually shape the distribution and Kirkwood gaps of **asteroidal** orbits."
      },
      {
        "author": "Alexander von Humboldt",
        "work": "Cosmos",
        "quote": "Zodiacal light originates from sunlight scattered by microscopic particles of cometary and **asteroidal** dust."
      }
    ]
  },
  "Dashboard — aster\\asteroidea.md": {
    "primary": "The class of marine invertebrates in the phylum Echinodermata comprising the true starfishes or sea stars.",
    "secondary": "In marine zoology, echinoderms characterized by pentamerous radial symmetry, central disc with five or more radiating arms, and an open ambulacral water-vascular system.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "The Invertebrata",
        "quote": "The class **Asteroidea** is distinguished from Ophiuroidea by deep open ambulacral grooves along the oral surface of the rays."
      },
      {
        "author": "Rachel Carson",
        "work": "The Edge of the Sea",
        "quote": "On the granite rocks of Maine, colorful purple and ochre species of **Asteroidea** cling tightly against the pounding surf."
      },
      {
        "author": "Charles Darwin",
        "work": "The Voyage of the Beagle",
        "quote": "In low-tide pools at low water, we found numerous predatory species of **Asteroidea** prying open bivalve mussels."
      }
    ]
  },
  "Dashboard — aster\\asterope.md": {
    "primary": "In Greek mythology, one of the seven Pleiades, daughters of Atlas and Pleione; also the double star Sterope (Asterope) in the Pleiades cluster.",
    "secondary": "In observational astronomy, a visual double star (Asterope I and II / 21 and 22 Tauri) embedded within the reflection nebulae of the Pleiades.",
    "quotes": [
      {
        "author": "John Herschel",
        "work": "Outlines of Astronomy",
        "quote": "Through a modest telescope, faint **Asterope** resolves into twin starry sparks amidst the luminous gauze of the Pleiades."
      },
      {
        "author": "John Keats",
        "work": "Ode to Maia",
        "quote": "With sweet Maia and her starry sisters, gentle **Asterope** leads the celestial dance across the nocturnal skies of Greece."
      },
      {
        "author": "Alexander von Humboldt",
        "work": "Cosmos",
        "quote": "Ancient navigators looked to the rising of **Asterope** and her sisters to mark the safe opening of Mediterranean sailing."
      }
    ]
  },
  "Dashboard — aster\\astor.md": {
    "primary": "A prominent family surname associated with American commerce and fur trading (John Jacob Astor); or a taxonomic star-related name.",
    "secondary": "In American economic history, the dynasty founded by John Jacob Astor, whose monopoly over the Pacific fur trade shaped 19th-century frontier expansion.",
    "quotes": [
      {
        "author": "Washington Irving",
        "work": "Astoria",
        "quote": "John Jacob **Astor** conceived a commercial enterprise of continental scope, planting a fur-trading outpost at the mouth of the Columbia."
      },
      {
        "author": "Alexis de Tocqueville",
        "work": "Democracy in America",
        "quote": "The immense fortune amassed by **Astor** in New York illustrates how unrestrained enterprise thrives in the American republic."
      },
      {
        "author": "Henry David Thoreau",
        "work": "A Week on the Concord and Merrimack Rivers",
        "quote": "The voyageur stories of **Astor** and the fur companies sounded like chivalric romances enacted in the wild western forests."
      }
    ]
  },
  "Dashboard — aster\\astrologer.md": {
    "primary": "A person who practices astrology, claiming to predict events or discern human character by interpreting the motions and positions of celestial bodies.",
    "secondary": "In the history of science, an astronomical practitioner of antiquity and the Middle Ages who combined empirical planetary observation with astrological divination.",
    "quotes": [
      {
        "author": "Francis Bacon",
        "work": "The Advancement of Learning",
        "quote": "The ancient **astrologer** corrupted natural philosophy by mingling the pure motions of heaven with frivolous superstitious predictions."
      },
      {
        "author": "William Shakespeare",
        "work": "King Lear",
        "quote": "This is the excellent foppery of the world, that, when we are sick in fortune—often the surfeit of our own behaviour—we make guilty of our disasters the sun, the moon, and the stars, as if we were villains by necessity and knaves by an **astrologer**'s craft."
      },
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The emperor Septimius Severus rarely undertook an expedition without consulting his favorite Egyptian **astrologer**."
      }
    ]
  },
  "Dashboard — aster\\astrological.md": {
    "primary": "Pertaining to, based on, or characteristic of astrology or the belief in stellar influence over human affairs.",
    "secondary": "Relating to zodiacal charts, planetary aspects, or historical horoscopic systems.",
    "quotes": [
      {
        "author": "Thomas Browne",
        "work": "Pseudodoxia Epidemica",
        "quote": "To attribute mortal crimes and virtues to mere **astrological** aspects of Mars or Venus is to defraud the human will of moral agency."
      },
      {
        "author": "Johannes Kepler",
        "work": "Harmonices Mundi",
        "quote": "Though I cast **astrological** nativities to earn my bread, my true devotion belongs to the mathematical laws of the planetary orbits."
      },
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "An **astrological** prophecy predicting the death of the tyrant threw the entire imperial palace into suspicious panic."
      }
    ]
  },
  "Dashboard — aster\\astrologist.md": {
    "primary": "A practitioner of astrology; an astrologer.",
    "secondary": "In historical and philosophical literature, an archaic or formal synonym for an astrologer, especially one who claims scientific systematicity in casting horoscopes.",
    "quotes": [
      {
        "author": "Jonathan Swift",
        "work": "The Bickerstaff-Partridge Papers",
        "quote": "I undertook to expose that notorious impostor and almanac **astrologist**, John Partridge, by predicting his own untimely demise."
      },
      {
        "author": "Francis Bacon",
        "work": "Novum Organum",
        "quote": "The credulous public listens to the **astrologist** when one lucky prediction succeeds, while ignoring twenty that miserably fail."
      },
      {
        "author": "Walter Scott",
        "work": "Guy Mannering",
        "quote": "The old Laird retained an eccentric **astrologist** whose charts hung framed beside the ancestral armorial bearings."
      }
    ]
  },
  "Dashboard — aster\\astrology.md": {
    "primary": "The ancient divination practice that interprets the apparent positions and aspects of celestial bodies in the belief that they influence human destinies and earthly events.",
    "secondary": "In the history of science, a proto-scientific cosmic worldview that historically stimulated rigorous astronomical calculation and cartography before the Copernican revolution.",
    "quotes": [
      {
        "author": "Carl Sagan",
        "work": "Cosmos",
        "quote": "For millennia, astronomy was inextricably bound up with **astrology**, the desire to read human destiny written across the stars."
      },
      {
        "author": "Francis Bacon",
        "work": "The Advancement of Learning",
        "quote": "We do not entirely reject **astrology**, but we would have it cleansed of superstitious vanities and based on physical affinities."
      },
      {
        "author": "John Milton",
        "work": "Paradise Lost",
        "quote": "Whether the sun or earth move, let not human vanity seek in **astrology** what heaven has hidden in secret wisdom."
      }
    ]
  },
  "Dashboard — aster\\diasterism geaster.md": {
    "primary": "A botanical and mycological designation referring to the star-like dehiscence and spore configuration of earthstar fungi (genus Geastrum).",
    "secondary": "In morphological mycology, the dual radial symmetry exhibited by the splitting exoperidium and rayed central peristome of earthstar sporocarps.",
    "quotes": [
      {
        "author": "Anton de Bary",
        "work": "Comparative Morphology and Biology of the Fungi",
        "quote": "In **diasterism geaster**, the star-shaped rays of the exoperidium peel backward upon the soil like a hygroscopic floral blossom."
      },
      {
        "author": "William Benjamin Carpenter",
        "work": "The Microscope and Its Revelations",
        "quote": "The elegant symmetry of **diasterism geaster** reveals how fungal peridia split along radial cleavage planes to liberate dry spores."
      },
      {
        "author": "John Lindley",
        "work": "The Vegetable Kingdom",
        "quote": "The curious earthstar displays a remarkable **diasterism geaster** pattern, mimicking a celestial constellation cast upon the forest floor."
      }
    ]
  },
  "Dashboard — aster\\diasterismgeaster.md": {
    "primary": "A compound morphological term in cryptogamic botany denoting the double star-shaped fruiting structure of earthstar fungi (Geastrum).",
    "secondary": "In systematic mycology, referring to the characteristic hygroscopic outer and inner star formations of the basidiocarp that open and close with moisture.",
    "quotes": [
      {
        "author": "Anton de Bary",
        "work": "Comparative Morphology and Biology of the Fungi",
        "quote": "The double star architecture of **diasterismgeaster** functions mechanically to elevate the puffball sac above damp forest litter."
      },
      {
        "author": "William Benjamin Carpenter",
        "work": "The Microscope and Its Revelations",
        "quote": "Under humid conditions, the arms of **diasterismgeaster** unfurl smoothly, exposing the apical ostiole to rain droplets."
      },
      {
        "author": "Julian Huxley",
        "work": "Evolution: The Modern Synthesis",
        "quote": "The functional morphology of **diasterismgeaster** demonstrates how passive mechanical tissue hygroscopy aids fungal dissemination."
      }
    ]
  },
  "Dashboard — aster\\disaster.md": {
    "primary": "A sudden, calamitous event that causes great damage, destruction, distress, or loss of life.",
    "secondary": "Etymologically from the Italian disastro (an unfavorable aspect of the stars), an overwhelming catastrophe or complete failure.",
    "quotes": [
      {
        "author": "William Shakespeare",
        "work": "Hamlet",
        "quote": "Stars with trains of fire and dews of blood, **disaster** in the sun; and the moist star upon whose influence Neptune's empire stands was sick almost to doomsday with eclipse."
      },
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The defeat at Adrianople was the greatest military **disaster** the Roman empire had suffered since the fatal field of Cannae."
      },
      {
        "author": "Herman Melville",
        "work": "Moby-Dick",
        "quote": "A dark presentiment of impending **disaster** hung over the ship, whispered among the sailors as the wind began to howl."
      }
    ]
  },
  "Dashboard — aster\\disastrous.md": {
    "primary": "Causing immense distress, injury, ruin, or catastrophe; calamitous.",
    "secondary": "Marked by ill fortune or leading to completely ruinous and adverse consequences.",
    "quotes": [
      {
        "author": "John Milton",
        "work": "Paradise Lost",
        "quote": "As when the Sun new risen looks through the horizontal misty air shorn of his beams, or from behind the moon in dim eclipse **disastrous** twilight sheds on half the nations."
      },
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The retreat from Moscow proved far more **disastrous** to the invading army than the fiercest pitched battles of the campaign."
      },
      {
        "author": "Charles Darwin",
        "work": "The Voyage of the Beagle",
        "quote": "The earthquake along the Chilean coast produced **disastrous** destruction, reducing flourishing towns to heaps of smoking rubble in seconds."
      }
    ]
  },
  "Dashboard — aster\\disastrously.md": {
    "primary": "In a disastrous manner; with ruinous, catastrophic, or terribly adverse consequences.",
    "secondary": "Leading directly or inevitably to total failure, destruction, or collapse.",
    "quotes": [
      {
        "author": "Thomas Babington Macaulay",
        "work": "The History of England",
        "quote": "The ill-conceived Scottish expedition ended **disastrously**, its leaders captured and executed on the scaffold."
      },
      {
        "author": "George Eliot",
        "work": "Middlemarch",
        "quote": "His financial speculations collapsed **disastrously**, dragging down innocent depositors in the provincial bank."
      },
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The campaign in Mesopotamia terminated **disastrously** when starvation forced the legionaries to sue for humiliating terms."
      }
    ]
  },
  "Dashboard — aster\\monaster.md": {
    "primary": "A single star-like radiating structure of chromatin or microtubules formed during early mitotic cell division before bipolar separation.",
    "secondary": "In cytology and karyokinesis, the unipolar aster configuration observed during aberrant mitosis or experimental block of centrosome separation.",
    "quotes": [
      {
        "author": "Edmund Beecher Wilson",
        "work": "The Cell in Development and Inheritance",
        "quote": "During unipolar division, chromosomes arrange themselves radially around a solitary centrosome, forming a characteristic **monaster**."
      },
      {
        "author": "Walther Flemming",
        "work": "Cell Substance, Nucleus, and Cell Division",
        "quote": "The chromatin loops assemble into an equatorial rosette or **monaster** prior to the cleavage of the nuclear membrane."
      },
      {
        "author": "William Benjamin Carpenter",
        "work": "The Microscope and Its Revelations",
        "quote": "Under high magnification, the radiating fibrils of the **monaster** reveal the active reorganization of protoplasmic substance."
      }
    ]
  },
  "Dashboard — aster\\monastic.md": {
    "primary": "Relating to, characteristic of, or resembling monks, nuns, or monasteries; secluded, austere, contemplative, or communal.",
    "secondary": "In social and ecclesiastical history, a lifestyle characterized by religious vows of poverty, chastity, and obedience within an organized cloistered community.",
    "quotes": [
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The rapid growth of the **monastic** order in Egypt withdrew thousands of industrious citizens from the military defense of the empire."
      },
      {
        "author": "Henry David Thoreau",
        "work": "Walden",
        "quote": "My life in the woods had something of **monastic** solitude, though free from gloomy dogmas and cloistered penance."
      },
      {
        "author": "John Ruskin",
        "work": "The Stones of Venice",
        "quote": "The quiet beauty of the cloister reflected the **monastic** ideal of peace in an age of feudal turbulence."
      }
    ]
  },
  "Dashboard — aster\\monastical.md": {
    "primary": "Pertaining to monasteries, monks, or a monastic mode of living; monastic (archaic or formal variant).",
    "secondary": "Describing institutions, customs, or disciplines rooted in cloistered religious vows and ascetic practices.",
    "quotes": [
      {
        "author": "Francis Bacon",
        "work": "The Advancement of Learning",
        "quote": "A purely contemplative life, such as the **monastical** retreat, was never intended to absolve men from public civic duties."
      },
      {
        "author": "Samuel Johnson",
        "work": "The History of Rasselas, Prince of Abissinia",
        "quote": "The hermit confessed that his **monastical** seclusion had not extinguished those passions which disturb the worldly breast."
      },
      {
        "author": "Thomas Carlyle",
        "work": "Past and Present",
        "quote": "Under Abbot Samson, the ancient **monastical** discipline of Saint Edmundsbury was restored to vigor and probity."
      }
    ]
  },
  "Dashboard — aster\\monasticism.md": {
    "primary": "The religious practice, system, or lifestyle of living in secluded communities as monks or nuns under vows of poverty, chastity, and obedience.",
    "secondary": "In the history of world religions, an ascetic and contemplative institutional movement prominent in Christianity, Buddhism, and Jainism.",
    "quotes": [
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The enthusiastic spread of **monasticism** transformed the Mediterranean landscape with solitary hermitages and fortified abbeys."
      },
      {
        "author": "William James",
        "work": "The Varieties of Religious Experience",
        "quote": "The ascetic rigors of **monasticism** represent heroic attempts to emancipate the spiritual life from worldly contamination."
      },
      {
        "author": "Thomas Babington Macaulay",
        "work": "Critical and Historical Essays",
        "quote": "During the Dark Ages, European **monasticism** preserved the fragile spark of classical learning amidst barbarian chaos."
      }
    ]
  },
  "Dashboard — aster\\unasterisked.md": {
    "primary": "Not marked, designated, or noted with an asterisk (*).",
    "secondary": "In bibliographies, academic indices, and critical editions, describing standard entries or attested linguistic forms that require no qualification.",
    "quotes": [
      {
        "author": "Max Müller",
        "work": "Lectures on the Science of Language",
        "quote": "Attested forms recorded in ancient Sanskrit inscriptions remain **unasterisked** in comparative tables."
      },
      {
        "author": "Samuel Johnson",
        "work": "Preface to Shakespeare",
        "quote": "Those readings which possess unanimous support in early quartos are left **unasterisked** for the general reader."
      },
      {
        "author": "George Eliot",
        "work": "Middlemarch",
        "quote": "The ordinary, **unasterisked** titles in the library inventory attracted little notice from the antiquarian collector."
      }
    ]
  }
};

const count = updateNotesBatch(CLUSTER_DIR, batchData);
console.log(`========================================`);
console.log(`Form & Space Part 1 - Batch 2 Completed: ${count} / ${Object.keys(batchData).length} words updated`);
console.log(`========================================`);
