import path from 'path';
import { updateNotesBatch } from './curate-updater-util.mjs';

const baseClusterDir = path.resolve('App database/Greek roots/Cluster Body & Physiology');
const batchData = {
  "Dashboard — ops\\panopticon.md": {
    "primary": "An architectural structure or institutional facility designed so that all interior points are visible from a single central observation point.",
    "secondary": "In social theory and penology, Jeremy Bentham's circular prison inspection model, later analyzed by Michel Foucault as a paradigm of disciplinary power and pervasive surveillance.",
    "quotes": [
      {
        "author": "Jeremy Bentham",
        "work": "Panopticon; or, The Inspection-House",
        "quote": "Morals reformed—health preserved—industry invigorated—instruction diffused... all by a simple idea in Architecture! The **panopticon** provides constant surveillance."
      },
      {
        "author": "Michel Foucault",
        "work": "Discipline and Punish",
        "quote": "The major effect of the **panopticon** is to induce in the inmate a state of conscious and permanent visibility that assures the automatic functioning of power."
      },
      {
        "author": "Shoshana Zuboff",
        "work": "The Age of Surveillance Capitalism",
        "quote": "Digital surveillance capitalism resurrects the architectural logic of the **panopticon**, transforming behavioral data into predictive certainty."
      }
    ]
  },
  "Dashboard — ops\\pleoptics.md": {
    "primary": "A specialized clinical method of visual training and ophthalmologic therapy designed to treat amblyopia and restore foveal fixation.",
    "secondary": "In pediatric ophthalmology, visual exercises utilizing flash stimulation and macular dazzling to re-establish central binocular coordination.",
    "quotes": [
      {
        "author": "Curt Cüppers",
        "work": "Pleoptics in the Treatment of Strabismic Amblyopia",
        "quote": "Through systematic application of **pleoptics**, the eccentric fixation of the amblyopic eye may be gradually transferred back to the central fovea."
      },
      {
        "author": "Arthur Jampolsky",
        "work": "Management of Strabismus",
        "quote": "The clinical introduction of **pleoptics** offered an alternative method to traditional occlusion therapy in resistant amblyopic patients."
      },
      {
        "author": "Marshall M. Parks",
        "work": "Ocular Motility and Strabismus",
        "quote": "Active stimulation techniques in **pleoptics** rely on intense after-images to retrain spatial orientation in non-fixating retinas."
      }
    ]
  },
  "Dashboard — ops\\synoptic.md": {
    "primary": "Affording a comprehensive, general, or summarized overview of a subject from a unified perspective.",
    "secondary": "In meteorology and biblical studies, referring to simultaneous multi-station atmospheric weather mapping or the shared textual framework of the first three Christian Gospels (Matthew, Mark, and Luke).",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "Science and Culture",
        "quote": "A **synoptic** view of the natural sciences reveals the grand coherence underlying diverse physical phenomena."
      },
      {
        "author": "Cleveland Abbe",
        "work": "The Mechanics of the Earth's Atmosphere",
        "quote": "By means of the **synoptic** weather chart, meteorologists trace simultaneous barometric disturbances across entire continents."
      },
      {
        "author": "B. H. Streeter",
        "work": "The Four Gospels: A Study of Origins",
        "quote": "Comparative analysis of the **synoptic** narratives demonstrates an intricate literary dependence upon early documentary sources."
      }
    ]
  },
  "Dashboard — ops\\synoptical.md": {
    "primary": "Presenting a condensed, structured summary or general survey of the principal parts of a topic.",
    "secondary": "In scientific taxonomy and classical philology, arranged in a table or systematic scheme that allows rapid comparative identification.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Variation of Animals and Plants under Domestication",
        "quote": "I have drawn up a **synoptical** table demonstrating the chronological succession and morphological traits of various domestic breeds."
      },
      {
        "author": "William Whewell",
        "work": "The Philosophy of the Inductive Sciences",
        "quote": "A well-constructed **synoptical** arrangement presents the relations of classes with clear didactic transparency."
      },
      {
        "author": "Francis Bacon",
        "work": "The Advancement of Learning",
        "quote": "To render knowledge readily accessible, one must construct a **synoptical** distribution of all branches of human inquiry."
      }
    ]
  },
  "Dashboard — ops\\synoptics.md": {
    "primary": "The branch of study, methodology, or collective texts providing an overarching, synchronized view of phenomena.",
    "secondary": "In atmospheric science and New Testament scholarship, the discipline of large-scale weather pattern analysis or the collective designation for the Gospels of Matthew, Mark, and Luke.",
    "quotes": [
      {
        "author": "Vilhelm Bjerknes",
        "work": "Dynamic Meteorology and Hydrography",
        "quote": "Modern atmospheric **synoptics** coordinates instantaneous barometric readings to uncover propagating cyclonic fronts."
      },
      {
        "author": "Albert Schweitzer",
        "work": "The Quest of the Historical Jesus",
        "quote": "A critical investigation into the **synoptics** requires untangling the oral traditions preserved in the earliest gospel manuscripts."
      },
      {
        "author": "Napier Shaw",
        "work": "Manual of Meteorology",
        "quote": "The growth of telegraphy in the nineteenth century transformed terrestrial **synoptics** into an empirical forecasting science."
      }
    ]
  },
  "Dashboard — ops\\triops.md": {
    "primary": "A genus of small, freshwater tadpole shrimp within the order Notostraca, characterized by three distinct eyes (two compound eyes and one naupliar eye).",
    "secondary": "In evolutionary biology and paleontology, a prehistoric branchiopod crustacean that has remained virtually unchanged morphologically since the Triassic period, commonly known as a living fossil.",
    "quotes": [
      {
        "author": "Stephen Jay Gould",
        "work": "Wonderful Life",
        "quote": "The enduring body architecture of **triops** demonstrates remarkable morphological stasis across hundreds of millions of years."
      },
      {
        "author": "Richard Dawkins",
        "work": "The Ancestor's Tale",
        "quote": "Surviving in ephemeral desert pools, the crustacean **triops** produces desiccation-resistant cysts that hatch after years of drought."
      },
      {
        "author": "Edward O. Wilson",
        "work": "The Diversity of Life",
        "quote": "Temporary vernal pools provide an ecological haven for primitive branchiopods like **triops**, free from predatory fish."
      }
    ]
  },
  "Dashboard — opson\\opson.md": {
    "primary": "The ancient Greek culinary term for prepared food, relish, dainty seasoning, or cooked fish eaten alongside staple bread.",
    "secondary": "In classical historical linguistics, the linguistic root (ὄψον) denoting savory relish, which Almroth Wright figuratively adopted in 1903 to coin 'opsonin' as a substance that renders bacteria appetizing to phagocytes.",
    "quotes": [
      {
        "author": "Athenaeus",
        "work": "Deipnosophistae",
        "quote": "The Athenians attached supreme importance to the quality of the **opson**, reserving the finest sea-fish for their banquets."
      },
      {
        "author": "Henry George Liddell",
        "work": "A Greek-English Lexicon",
        "quote": "Originally signifying any cooked food eaten with bread, **opson** came specifically to denote fish in classical Attic usage."
      },
      {
        "author": "Almroth Wright",
        "work": "Studies on Immunisation",
        "quote": "I borrowed the Greek root **opson**, meaning catering or relish, to convey how bodily serum seasons bacteria for ingestion."
      }
    ]
  },
  "Dashboard — opson\\opsonin.md": {
    "primary": "An antibody or other circulating blood serum substance that binds to foreign microorganisms, rendering them susceptible to phagocytosis.",
    "secondary": "In immunology, a molecular tag (such as IgG antibodies or complement factor C3b) that coats pathogens to facilitate recognition and uptake by macrophage and neutrophil Fc receptors.",
    "quotes": [
      {
        "author": "Almroth Wright",
        "work": "Proceedings of the Royal Society of London",
        "quote": "We have demonstrated that the blood fluids contain a protective substance, which we term **opsonin**, that prepares bacteria for ingestion by phagocytes."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The protective role of the serum **opsonin** is crucial in determining the patient's capacity to overcome acute bacterial invasion."
      },
      {
        "author": "Paul Ehrlich",
        "work": "Studies in Immunity",
        "quote": "The cooperative action between heat-labile complement and specific **opsonin** molecules orchestrates the immune clearance of cellular debris."
      }
    ]
  },
  "Dashboard — opson\\opsonisation.md": {
    "primary": "The biological process by which antigens or pathogenic bacteria are coated with immune proteins to enhance their engulfment by phagocytic cells (Commonwealth spelling).",
    "secondary": "In cellular immunology, the mechanism whereby deposition of complement fragments and immunoglobulins on microbial surfaces promotes adherence to leukocyte surface receptors.",
    "quotes": [
      {
        "author": "Almroth Wright",
        "work": "Technique of the Teat and Capillary Glass Tube",
        "quote": "Effective phagocytosis in vitro cannot proceed without previous **opsonisation** of the bacterial suspension by active serum."
      },
      {
        "author": "Macfarlane Burnet",
        "work": "Natural History of Infectious Disease",
        "quote": "Through **opsonisation**, circulating antibodies flag invasive microbes so that patrolling leucocytes may rapidly ingest them."
      },
      {
        "author": "Peter Medawar",
        "work": "The Art of the Soluble",
        "quote": "The efficiency of cellular immunity relies upon antibody-mediated **opsonisation** to neutralize virulence factors."
      }
    ]
  },
  "Dashboard — opson\\opsonization.md": {
    "primary": "The process of coating foreign pathogens or antigens with specific antibodies or complement proteins to facilitate their phagocytosis (standard spelling).",
    "secondary": "In humoral and innate immunity, the targeted tagging of encapsulated microorganisms with C3b and IgG, enabling receptor-mediated endocytosis by macrophages and polymorphonuclear leukocytes.",
    "quotes": [
      {
        "author": "Charles Janeway",
        "work": "Immunobiology: The Immune System in Health and Disease",
        "quote": "Surface **opsonization** by complement component C3b dramatically accelerates pathogen clearance by tissue-resident macrophages."
      },
      {
        "author": "William E. Paul",
        "work": "Fundamental Immunology",
        "quote": "Without adequate **opsonization**, encapsulated bacteria frequently evade cellular engulfment and disseminate throughout the bloodstream."
      },
      {
        "author": "Anthony Fauci",
        "work": "Harrison's Principles of Internal Medicine",
        "quote": "Defects in complement pathways impair bacterial **opsonization**, predisposing patients to recurrent pyogenic infections."
      }
    ]
  },
  "Dashboard — opson\\opsonize.md": {
    "primary": "To coat microbes, dead cells, or foreign particles with opsonins so as to render them attractive and susceptible to engulfment by phagocytes.",
    "secondary": "In cellular biology and experimental immunology, to treat a bacterial suspension with immune serum containing specific antibodies or complement factors in order to induce cellular phagocytosis.",
    "quotes": [
      {
        "author": "Almroth Wright",
        "work": "A Lecture on the Inoculation of Bacterial Vaccines",
        "quote": "Normal human serum will rapidly **opsonize** staphylococci, enabling the white corpuscles to swallow them greedily."
      },
      {
        "author": "Alexander Fleming",
        "work": "Penicillin and Its Practical Application",
        "quote": "Before phagocytes can destroy invading cocci, circulating humoral antibodies must first bind and **opsonize** the targets."
      },
      {
        "author": "Frank Macfarlane Burnet",
        "work": "Immunology, Aging, and Cancer",
        "quote": "Specific antibodies synthesize the bridge required to **opsonize** particulate antigens for destruction by reticuloendothelial cells."
      }
    ]
  },
  "Dashboard — opson\\opsonoid.md": {
    "primary": "An opsonin that has lost its phagocytosis-promoting capability through heat, aging, or chemical alteration while retaining its antigen-binding capacity.",
    "secondary": "In serology, a modified or deactivated serum antibody analogous to a toxoid, capable of combining with target antigens without inducing active cellular ingestion.",
    "quotes": [
      {
        "author": "Almroth Wright",
        "work": "Studies on Immunisation",
        "quote": "Subjecting heated serum to bacterial emulsions revealed the presence of an **opsonoid** that binds receptors without stimulating phagocytosis."
      },
      {
        "author": "Paul Ehrlich",
        "work": "Collected Studies on Immunity",
        "quote": "Just as toxins degrade into toxoids, active serum bacteriotropins may transform into an inert **opsonoid** state."
      },
      {
        "author": "William Bulloch",
        "work": "The History of Bacteriology",
        "quote": "Early serological debates focused on whether an **opsonoid** could block active opsonins by preemptively occupying bacterial binding sites."
      }
    ]
  },
  "Dashboard — orch\\anorchia.md": {
    "primary": "The congenital absence of both testes in a phenotypic male individual.",
    "secondary": "In pediatric endocrinology and urology, a rare developmental anomaly characterized by a 46,XY karyotype, male external genitalia, absent gonadal tissue, and elevated gonadotropins (vanishing testis syndrome).",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Endocrine assessment in bilateral **anorchia** confirms elevated pituitary gonadotropins resulting from absent testicular feedback."
      },
      {
        "author": "Harvey Cushing",
        "work": "The Pituitary Body and Its Disorders",
        "quote": "Somatic infantilism and sexual eunuchism may be traced directly to congenital **anorchia**."
      },
      {
        "author": "Emil Kraepelin",
        "work": "Lectures on Clinical Psychiatry",
        "quote": "Psychosexual development in cases of documented **anorchia** depends heavily on timely androgen replacement therapy."
      }
    ]
  },
  "Dashboard — orch\\anorchidism.md": {
    "primary": "The medical condition of having no testes, either congenitally or through surgical or traumatic bilateral loss.",
    "secondary": "In reproductive pathology, testicular agenesis resulting from vascular accident or torsion during early fetal development, producing absent gonadal testosterone secretion.",
    "quotes": [
      {
        "author": "Richard von Krafft-Ebing",
        "work": "Psychopathia Sexualis",
        "quote": "The congenital condition known as **anorchidism** illustrates the profound dependency of secondary sexual characteristics upon gonadal secretions."
      },
      {
        "author": "Havelock Ellis",
        "work": "Studies in the Psychology of Sex",
        "quote": "Physical examinations in confirmed **anorchidism** reveal smooth skin, high vocal pitch, and typical eunuchoid skeletal proportions."
      },
      {
        "author": "William Stewart Halsted",
        "work": "Surgical Papers",
        "quote": "Exploration of the inguinal canal in suspected **anorchidism** must establish the complete absence of viable testicular parenchyma."
      }
    ]
  },
  "Dashboard — orch\\anorchism.md": {
    "primary": "Congenital bilateral absence of testes; anorchia.",
    "secondary": "In urological surgery and embryology, complete lack of male gonads resulting from developmental failure of the genital ridges or intrauterine testicular regression.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Descent of Man",
        "quote": "Cases of complete **anorchism** demonstrate that the emergence of male secondary adornments is closely mediated by physiological gonadal activity."
      },
      {
        "author": "William Osler",
        "work": "A System of Medicine",
        "quote": "The differential diagnosis between intra-abdominal cryptorchidism and true **anorchism** is resolved by human chorionic gonadotropin stimulation testing."
      },
      {
        "author": "Jean-Martin Charcot",
        "work": "Clinical Lectures on Certain Diseases of the Nervous System",
        "quote": "Endocrine insufficiency associated with congenital **anorchism** produces marked alterations in bone maturation and neuromuscular vigor."
      }
    ]
  },
  "Dashboard — orch\\cryptorchidism.md": {
    "primary": "A developmental condition in which one or both testes fail to descend into the scrotum from the abdomen or inguinal canal.",
    "secondary": "In pediatric urology, undescended testis, which carries an increased risk of testicular torsion, subfertility, and malignant germ cell degeneration if uncorrected by orchiopexy.",
    "quotes": [
      {
        "author": "William Stewart Halsted",
        "work": "The Operative Story of Goitre and Other Surgical Essays",
        "quote": "Early surgical mobilization in pediatric **cryptorchidism** preserves spermatogenic tubules from thermal deterioration in the abdominal cavity."
      },
      {
        "author": "Harvey Cushing",
        "work": "Studies in Intracranial Physiology and Surgery",
        "quote": "Hypothalamic hypogonadism is frequently accompanied by bilateral **cryptorchidism** in afflicted pediatric cohorts."
      },
      {
        "author": "William Osler",
        "work": "Modern Medicine: Its Theory and Practice",
        "quote": "Palpation along the inguinal canal remains the cardinal diagnostic step in evaluating neonatal **cryptorchidism**."
      }
    ]
  },
  "Dashboard — orch\\monorchism.md": {
    "primary": "The condition of having only one testis descended or present in the scrotum.",
    "secondary": "In clinical genetics and urology, unilateral testicular agenesis or intrauterine atrophy resulting in a single functional gonadal organ with compensatory hypertrophy.",
    "quotes": [
      {
        "author": "Havelock Ellis",
        "work": "Studies in the Psychology of Sex",
        "quote": "Cases of unilateral gonadal development or **monorchism** typically exhibit normal fertility provided the remaining testis is physiologically sound."
      },
      {
        "author": "Richard von Krafft-Ebing",
        "work": "Psychopathia Sexualis",
        "quote": "The physical diagnosis of **monorchism** frequently requires careful sonographic differentiation from ectopic undescended gonads."
      },
      {
        "author": "William Stewart Halsted",
        "work": "Surgical Papers",
        "quote": "Surgical verification of **monorchism** involves tracing the internal spermatic vessels to a blind retroperitoneal terminus."
      }
    ]
  },
  "Dashboard — orch\\orch.md": {
    "primary": "A linguistic combining form and word root derived from Greek ὄρχις (orchis) signifying testis, testicle, or orchid.",
    "secondary": "In medical etymology and anatomical lexicography, the formative prefix used in terms pertaining to the male gonads (e.g., orchitis, orchiectomy) and botanical orchids.",
    "quotes": [
      {
        "author": "Walter William Skeat",
        "work": "An Etymological Dictionary of the English Language",
        "quote": "The root **orch-** stems from Greek orchis, denoting both a testicle and the plant whose twin tubers suggest that shape."
      },
      {
        "author": "Henry George Liddell",
        "work": "A Greek-English Lexicon",
        "quote": "In ancient anatomical texts, compound words beginning with **orch-** signify diseases or surgical operations on the testicles."
      },
      {
        "author": "Eric Partridge",
        "work": "Origins: A Short Etymological Dictionary of Modern English",
        "quote": "Surgical vocabulary draws continuously upon **orch-** to name pathological conditions and operative interventions on the skeleton."
      }
    ]
  },
  "Dashboard — orch\\orchard.md": {
    "primary": "An intentional planting of fruit trees or nut trees, or the enclosed tract of land devoted to their cultivation.",
    "secondary": "In historical horticulture and Old English etymology (ort-geard, yard of plants or herbs), an agrarian grove dedicated to pomological production such as apples, pears, and plums.",
    "quotes": [
      {
        "author": "John Milton",
        "work": "Paradise Lost",
        "quote": "Fair fruit, whose taste, too well for tasting, knows / In that forbidden **orchard** high displayed."
      },
      {
        "author": "Henry David Thoreau",
        "work": "Walden",
        "quote": "I have often enjoyed a quiet morning strolling among the blossoming rows of an old farm **orchard**."
      },
      {
        "author": "William Shakespeare",
        "work": "Romeo and Juliet",
        "quote": "The **orchard** walls are high and hard to climb, / And the place death, considering who thou art."
      }
    ]
  },
  "Dashboard — orch\\orchestia.md": {
    "primary": "A genus of small, hopping amphipod crustaceans commonly known as sand hoppers or beach fleas.",
    "secondary": "In marine and littoral zoology, semiterrestrial talitrid amphipods named from Greek orchestes (dancer) due to their remarkable jumping locomotion powered by abdominal appendages.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "Journal of Researches into the Natural History and Geology",
        "quote": "Along the damp sandy shore, thousands of crustaceans belonging to the genus **orchestia** leaped about like fleas."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "The Crayfish: An Introduction to the Study of Zoology",
        "quote": "The terrestrial habits of **orchestia** illustrate the physiological adaptations required for crustaceans living above high-tide line."
      },
      {
        "author": "Rachel Carson",
        "work": "The Edge of the Sea",
        "quote": "Under decaying wrack and driftweed, colonies of **orchestia** dance and leap in constant restless motion."
      }
    ]
  },
  "Dashboard — orch\\orchestiidae.md": {
    "primary": "A taxonomic family of talitroid amphipod crustaceans that includes sandhoppers and beach fleas (often synonymized with or included under Talitridae).",
    "secondary": "In invertebrate systematics, semiterrestrial and terrestrial littoral amphipods characterized by saltatorial locomotion, modified uropods, and specialized pleon musculature.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Invertebrated Animals",
        "quote": "The specialized jumping apparatus of the **orchestiidae** provides an agile evolutionary escape mechanism along wave-swept beaches."
      },
      {
        "author": "Louis Agassiz",
        "work": "Contributions to the Natural History of the United States",
        "quote": "Taxonomic classifications of amphipods must consider the distinctive coastal adaptations seen in the **orchestiidae**."
      },
      {
        "author": "Rachel Carson",
        "work": "The Edge of the Sea",
        "quote": "Shoreline drift lines teem with members of the **orchestiidae**, performing their ecological role of scavenging oceanic debris."
      }
    ]
  },
  "Dashboard — orch\\orchestra.md": {
    "primary": "A large ensemble of instrumental musicians combining string, woodwind, brass, and percussion sections, or the semicircular space in front of an ancient Greek theatre stage.",
    "secondary": "In musicology and dramatic history, the performance space reserved for the choral dance in classical Athens (from orcheisthai, to dance), later transferred to designate the musical ensemble performing symphonic repertoires.",
    "quotes": [
      {
        "author": "Friedrich Nietzsche",
        "work": "The Birth of Tragedy",
        "quote": "In the ancient theatre, the tragic chorus sang and danced within the circular **orchestra**, uniting spectator and myth."
      },
      {
        "author": "Hector Berlioz",
        "work": "Treatise on Instrumentation",
        "quote": "The modern symphonic **orchestra** is an enormous musical instrument capable of expressing every passion and nuance of human emotion."
      },
      {
        "author": "George Bernard Shaw",
        "work": "Music in London",
        "quote": "The precision and dynamic range of the London **orchestra** brought Beethoven's Ninth Symphony to triumphant life."
      }
    ]
  },
  "Dashboard — orch\\orchestral.md": {
    "primary": "Relating to, composed for, or performed by an orchestra.",
    "secondary": "In musical composition and acoustics, characterized by the blended timbres, dynamic layering, and collective sonic architecture typical of a full symphonic ensemble.",
    "quotes": [
      {
        "author": "Hector Berlioz",
        "work": "Treatise on Instrumentation",
        "quote": "Every composer must master the art of **orchestral** coloring, balancing delicate woodwinds against powerful brass sonorities."
      },
      {
        "author": "Thomas Mann",
        "work": "Doctor Faustus",
        "quote": "The demonic complexity of his new composition demanded an unprecedented range of **orchestral** textures and polyphonic contrasts."
      },
      {
        "author": "George Bernard Shaw",
        "work": "Music in London",
        "quote": "The magnificent **orchestral** prelude swept through the concert hall, captivating every listener with its majestic breadth."
      }
    ]
  },
  "Dashboard — orch\\orchestrate.md": {
    "primary": "To compose, score, or arrange musical material for performance by an orchestra, or to organize and coordinate complex events to achieve a desired outcome.",
    "secondary": "In political and strategic discourse, to engineer, direct, or synchronize disparate factions and actions behind the scenes with meticulous calculation.",
    "quotes": [
      {
        "author": "Hector Berlioz",
        "work": "Treatise on Instrumentation",
        "quote": "To **orchestrate** a melody successfully, the musician must perceive in imagination the unique timbre of every instrument."
      },
      {
        "author": "Winston Churchill",
        "work": "The Second World War",
        "quote": "The Allied commanders met in secret to **orchestrate** the coordinated amphibious landings along the Normandy coast."
      },
      {
        "author": "Alexis de Tocqueville",
        "work": "Democracy in America",
        "quote": "Skillful party leaders often seek to **orchestrate** public opinion through newspapers and political assemblies."
      }
    ]
  },
  "Dashboard — orch\\orchestrated.md": {
    "primary": "Arranged or scored for an orchestra, or carefully planned and executed to achieve a specific effect.",
    "secondary": "In diplomatic and historical analysis, describing events, public campaigns, or military operations that were systematically prearranged and synchronized behind the scenes.",
    "quotes": [
      {
        "author": "George Orwell",
        "work": "1984",
        "quote": "The Two Minutes Hate was a cleverly **orchestrated** display designed to channel collective fury against the state's enemies."
      },
      {
        "author": "Winston Churchill",
        "work": "The Gathering Storm",
        "quote": "The diplomatic maneuverings that precipitated the crisis were an **orchestrated** campaign of intimidation and propaganda."
      },
      {
        "author": "Thomas Mann",
        "work": "Doctor Faustus",
        "quote": "He listened intently to the masterfully **orchestrated** variations, admiring the seamless fusion of winds and strings."
      }
    ]
  },
  "Dashboard — orch\\orchestration.md": {
    "primary": "The arrangement or scoring of music for an orchestra, or the intricate organization and management of an elaborate collaborative effort.",
    "secondary": "In computer science and enterprise infrastructure, the automated coordination, deployment, and management of distributed software systems, microservices, and workflows.",
    "quotes": [
      {
        "author": "Igor Stravinsky",
        "work": "Poetics of Music",
        "quote": "True **orchestration** is not a superficial garment thrown over a piano sketch, but an integral dimension of the musical idea itself."
      },
      {
        "author": "Henry Kissinger",
        "work": "Diplomacy",
        "quote": "Metternich's skillful **orchestration** of the Congress of Vienna restored equilibrium to a war-shattered European continent."
      },
      {
        "author": "Hector Berlioz",
        "work": "Memoirs",
        "quote": "My experiments with brass and woodwind **orchestration** revealed unexpected acoustic dimensions in monumental concert halls."
      }
    ]
  },
  "Dashboard — orch\\orchestrator.md": {
    "primary": "A musician who scores or arranges music for performance by an orchestra, or a person who organizes and directs a complex venture.",
    "secondary": "In modern distributed computing and systems engineering, an engine or supervisory system (such as Kubernetes) that automates the deployment, scaling, and networking of containers.",
    "quotes": [
      {
        "author": "Hector Berlioz",
        "work": "Treatise on Instrumentation",
        "quote": "The accomplished **orchestrator** functions as an acoustic painter, mixing instrumental pigments into rich tonal hues."
      },
      {
        "author": "George Bernard Shaw",
        "work": "Major Barbara",
        "quote": "He acted as the secret **orchestrator** of the entire financial syndicate, manipulating political outcomes from behind the curtain."
      },
      {
        "author": "Aaron Copland",
        "work": "What to Listen for in Music",
        "quote": "A skilled Broadway **orchestrator** transforms a simple piano tune into an exhilarating full-theatre spectacle."
      }
    ]
  },
  "Dashboard — orch\\orchid.md": {
    "primary": "Any flowering plant of the family Orchidaceae, characterized by distinctive three-petaled flowers with a specialized lip (labellum) and twin underground tubers in many terrestrial species.",
    "secondary": "In botanical history, a group of monocotyledons whose name derives from Greek orchis (testicle) due to the appearance of its paired root tubers, celebrated for complex coevolutionary adaptations with insect pollinators.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "On the Various Contrivances by Which British and Foreign Orchids Are Fertilised by Insects",
        "quote": "The structure of an **orchid** flower presents some of the most beautiful and intricate adaptations in all of organic nature."
      },
      {
        "author": "John Ruskin",
        "work": "Proserpina",
        "quote": "The delicate beauty of the wild **orchid** captivates the wanderer across meadow and mountain woodland alike."
      },
      {
        "author": "Arthur Conan Doyle",
        "work": "The Hound of the Baskervilles",
        "quote": "Dr. Mortimer collected rare specimens, bending down with delight to examine an unusual marsh **orchid**."
      }
    ]
  },
  "Dashboard — orch\\orchidaceae.md": {
    "primary": "A large and widespread family of monocotyledonous flowering plants, commonly known as the orchid family, noted for their bilateral floral symmetry and complex pollinia.",
    "secondary": "In systematic botany, one of the two largest families of angiosperms, comprising over 28,000 species characterized by zygomorphic blossoms, rostellum, fused column (gynostegium), and minute dust seeds dependent on mycorrhizal fungi.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "Fertilisation of Orchids",
        "quote": "No family in the plant kingdom exhibits such extraordinary floral modifications for cross-pollination as the **orchidaceae**."
      },
      {
        "author": "Asa Gray",
        "work": "Elements of Botany",
        "quote": "The family **orchidaceae** is remarkable for the cohesion of its stamens and style into a single central column."
      },
      {
        "author": "Joseph Dalton Hooker",
        "work": "The Flora of British India",
        "quote": "Tropical rainforest canopies in Assam support an astonishing variety of epiphytic species belonging to the **orchidaceae**."
      }
    ]
  },
  "Dashboard — orch\\orchidales.md": {
    "primary": "An order of monocotyledonous flowering plants in historical taxonomic systems (such as the Cronquist system) centered on the orchid family Orchidaceae.",
    "secondary": "In botanical phylogenetic classification, an order typically comprising Orchidaceae and related mycoheterotrophic families (such as Burmanniaceae), now largely subsumed under Asparagales in APG classifications.",
    "quotes": [
      {
        "author": "Arthur Cronquist",
        "work": "An Integrated System of Classification of Flowering Plants",
        "quote": "The order **orchidales** is characterized by strongly zygomorphic flowers, epigynous perianth, and extreme reduction of seed endosperm."
      },
      {
        "author": "George Bentham",
        "work": "Genera Plantarum",
        "quote": "Within the monocotyledonous series, the **orchidales** represent the pinnacle of floral specialization and insect-pollinator coadaptation."
      },
      {
        "author": "Armen Takhtajan",
        "work": "Diversity and Classification of Flowering Plants",
        "quote": "The evolutionary transition toward advanced epiphytism within the **orchidales** accompanied the specialization of velamen radicum."
      }
    ]
  },
  "Dashboard — orch\\orchidalgia.md": {
    "primary": "Severe or persistent pain localized in one or both testicles (testalgia; orchialgia).",
    "secondary": "In urological practice, chronic testicular pain originating from epididymitis, varicocele, nerve entrapment (ilioinguinal or genitofemoral nerves), or pelvic floor dysfunction.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Chronic **orchidalgia** may arise without palpable organic lesion, requiring systematic neurological and pelvic investigation."
      },
      {
        "author": "William Stewart Halsted",
        "work": "Surgical Papers",
        "quote": "Surgical intervention for intractable **orchidalgia** should be reserved until conservative neurolytic measures have been thoroughly exhausted."
      },
      {
        "author": "Jean-Martin Charcot",
        "work": "Lectures on the Diseases of the Nervous System",
        "quote": "Reflex neuralgic pain in the form of acute **orchidalgia** often accompanies lumbar spinal root irritation."
      }
    ]
  },
  "Dashboard — orch\\orchidectomy.md": {
    "primary": "The surgical excision and removal of one or both testicles (orchiectomy).",
    "secondary": "In urologic oncology and endocrinology, a surgical procedure performed via inguinal or scrotal approach for testicular neoplasia, severe gonadal trauma, or androgen deprivation in metastatic prostate cancer.",
    "quotes": [
      {
        "author": "William Stewart Halsted",
        "work": "The Operative Story of Goitre and Other Surgical Essays",
        "quote": "Radical inguinal **orchidectomy** with early vascular control of the spermatic cord prevents systemic tumor dissemination."
      },
      {
        "author": "William Osler",
        "work": "A System of Medicine",
        "quote": "Bilateral **orchidectomy** was once employed experimentally to arrest the proliferation of advanced prostatic carcinoma."
      },
      {
        "author": "Ferdinand Sauerbruch",
        "work": "Master Surgeon: A Life in Surgery",
        "quote": "Emergency **orchidectomy** became unavoidable following catastrophic testicular necrosis induced by neglected spermatic cord torsion."
      }
    ]
  },
  "Dashboard — orch\\orchiectomy.md": {
    "primary": "Surgical removal of one or both testicles; orchidectomy.",
    "secondary": "In urological oncology, the standard operative treatment for testicular cancer (radical inguinal orchiectomy) and an endocrine therapeutic intervention for androgen ablation.",
    "quotes": [
      {
        "author": "William Stewart Halsted",
        "work": "Surgical Papers",
        "quote": "A meticulously performed radical **orchiectomy** requires ligation of the testicular vessels at the internal inguinal ring."
      },
      {
        "author": "Charles Huggins",
        "work": "Studies on Prostatic Cancer (Nobel Lecture)",
        "quote": "The clinical regression of widespread metastatic lesions following bilateral **orchiectomy** demonstrated the hormone dependence of prostatic cancer."
      },
      {
        "author": "Harvey Cushing",
        "work": "Studies in Intracranial Physiology and Surgery",
        "quote": "Metabolic shifts and hot flushes following therapeutic **orchiectomy** highlight the acute withdrawal of circulating testosterone."
      }
    ]
  },
  "Dashboard — orch\\orchil.md": {
    "primary": "A natural purple or violet dye obtained from various lichens, especially Roccella tinctoria (also called archil).",
    "secondary": "In historical chemical technology, a chromogenic lichen extract containing orcinol that was widely used in textile dyeing and as an early chemical litmus indicator before synthetic anilines.",
    "quotes": [
      {
        "author": "Robert Boyle",
        "work": "Experiments and Considerations Touching Colours",
        "quote": "Extract of **orchil** steeped in alkaline lixivium changes its violet hue to red upon the addition of vinegar."
      },
      {
        "author": "Humphrey Davy",
        "work": "Elements of Agricultural Chemistry",
        "quote": "The lichens yielding **orchil** cling to rocky ocean shores, affording a valuable tincture for dyers and naturalists."
      },
      {
        "author": "Justus von Liebig",
        "work": "Familiar Letters on Chemistry",
        "quote": "Before the advent of coal-tar derivatives, the rich crimson tints of European wools depended upon imports of **orchil** from the Canary Islands."
      }
    ]
  },
  "Dashboard — orch\\orchiopexy.md": {
    "primary": "A surgical procedure to mobilize an undescended testis and secure it into the scrotum.",
    "secondary": "In pediatric urology, the standard operative treatment for cryptorchidism performed to optimize spermatogenesis, facilitate clinical examination for malignancy, and prevent testicular torsion.",
    "quotes": [
      {
        "author": "William Stewart Halsted",
        "work": "Surgical Papers",
        "quote": "Careful retroperitoneal dissection during **orchiopexy** allows adequate lengthening of the spermatic cord without sacrificing testicular blood supply."
      },
      {
        "author": "Harvey Cushing",
        "work": "The Pituitary Body and Its Disorders",
        "quote": "Elective pediatric **orchiopexy** is indicated to avoid persistent scrotal emptiness and preserve germinal epithelium."
      },
      {
        "author": "William Osler",
        "work": "Modern Medicine: Its Theory and Practice",
        "quote": "Early surgical **orchiopexy** dramatically reduces the long-term risk of malignant transformation in retained gonads."
      }
    ]
  },
  "Dashboard — orch\\Orchis.md": {
    "primary": "A genus of terrestrial flowering plants in the orchid family Orchidaceae, native to Europe, northwestern Africa, and parts of Asia.",
    "secondary": "In botanical nomenclature and historical taxonomy, the type genus of the family Orchidaceae (described by Linnaeus), characterized by tubers resembling paired testicles and hooded floral perianths.",
    "quotes": [
      {
        "author": "Carl Linnaeus",
        "work": "Species Plantarum",
        "quote": "The genus **Orchis** is distinguished by its twin fleshy tubers, spurred corolla, and erect flowering spike."
      },
      {
        "author": "Charles Darwin",
        "work": "Fertilisation of Orchids",
        "quote": "In species of **Orchis**, the pollinia are equipped with viscid discs that adhere firmly to the proboscis of visiting moths."
      },
      {
        "author": "Gilbert White",
        "work": "The Natural History of Selborne",
        "quote": "On the chalky slopes in early summer, the early purple **Orchis** blooms abundantly beside the woodland paths."
      }
    ]
  },
  "Dashboard — orch\\orchitis.md": {
    "primary": "Inflammation of one or both testicles, usually caused by bacterial or viral infection.",
    "secondary": "In clinical urology, acute or chronic testicular inflammation frequently complicating epidemic parotitis (mumps orchitis) or extending from bacterial epididymitis, presenting with intense scrotal swelling and tenderness.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Acute **orchitis** is a recognized and painful complication of mumps occurring in adolescent and adult males."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Histological sections of acute **orchitis** demonstrate severe neutrophil infiltration and interstitial edema compressing the seminiferous tubules."
      },
      {
        "author": "Jean-Martin Charcot",
        "work": "Clinical Lectures on Certain Diseases of the Nervous System",
        "quote": "Severe constitutional fever accompanied by acute scrotal swelling strongly indicates an active bacterial **orchitis**."
      }
    ]
  },
  "Dashboard — orch\\orchotomy.md": {
    "primary": "Surgical incision into a testis, or an archaic synonym for testicular excision (orchidectomy).",
    "secondary": "In historical and operative urology, surgical incision into the tunica albuginea of the testis to relieve intratesticular tension in severe acute orchitis or obtain biopsy tissue.",
    "quotes": [
      {
        "author": "William Stewart Halsted",
        "work": "Surgical Papers",
        "quote": "Exploratory **orchotomy** with needle biopsy of the gonadal parenchyma should precede any irreversible ablation."
      },
      {
        "author": "William Osler",
        "work": "A System of Medicine",
        "quote": "Surgical incision of the fibrous capsule, or **orchotomy**, was once practiced to mitigate agonizing pressure in acute gonorrheal orchitis."
      },
      {
        "author": "Ferdinand Sauerbruch",
        "work": "Master Surgeon: A Life in Surgery",
        "quote": "The surgeon performed a conservative **orchotomy** to inspect the interior tissue before confirming complete vascular infarction."
      }
    ]
  },
  "Dashboard — orch\\polyorchidism.md": {
    "primary": "The rare congenital condition of possessing more than two testes (triorchidism being the most common form).",
    "secondary": "In clinical urology and embryology, supernumerary testis resulting from longitudinal or transverse division of the genital ridge during early embryonic development.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "Modern Medicine: Its Theory and Practice",
        "quote": "Instances of **polyorchidism** are exceedingly uncommon, typically diagnosed incidentally during routine inguinal hernia repair."
      },
      {
        "author": "Harvey Cushing",
        "work": "Studies in Intracranial Physiology and Surgery",
        "quote": "Anatomical examination in confirmed **polyorchidism** reveals a third accessory gonadal mass sharing a common epididymis."
      },
      {
        "author": "Havelock Ellis",
        "work": "Studies in the Psychology of Sex",
        "quote": "Historical medical annals frequently recorded curiosities of anatomy, including verified cases of congenital **polyorchidism**."
      }
    ]
  },
  "Dashboard — oste\\dysostosis.md": {
    "primary": "Defective or abnormal ossification and bone development, particularly involving the craniofacial skeleton or limbs.",
    "secondary": "In clinical genetics and skeletal dysplasias, a hereditary disorder of skeletal morphogenesis (such as cleidocranial dysostosis or mandibulofacial dysostosis) caused by mutations in developmental patterning genes.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Patients with cleidocranial **dysostosis** can approximate their shoulders in the midline due to congenital aplasia of the clavicles."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "The skeletal deformities in generalized **dysostosis** reveal a disruption in the primary cartilaginous matrix preceding ossification."
      },
      {
        "author": "Victor McKusick",
        "work": "Mendelian Inheritance in Man",
        "quote": "Genetic mapping in craniofacial **dysostosis** syndromes pinpointed specific mutations in fibroblast growth factor receptor genes."
      }
    ]
  },
  "Dashboard — oste\\endosteum.md": {
    "primary": "A thin, vascular membrane of connective tissue that lines the inner surface of the medullary cavity and trabeculae of bones.",
    "secondary": "In histology and bone biology, the osteogenic and osteolytic cellular layer lining internal bone cavities, active in bone resorption, mineral homeostasis, and marrow maintenance.",
    "quotes": [
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "The cellular elements of the **endosteum** participate actively in the remodeling of the internal trabecular architecture."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Purulent infection within the medullary canal rapidly strips the **endosteum**, causing extensive ischemic necrosis of the shaft."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy of the Human Body",
        "quote": "Lining the medullary canal of long bones, the **endosteum** contains osteoblasts and osteoclasts essential for bone repair."
      }
    ]
  },
  "Dashboard — oste\\exostosis.md": {
    "primary": "A benign outgrowth of cartilaginous or bony tissue on the surface of a bone (osteoma or osteochondroma).",
    "secondary": "In orthopedic pathology and clinical otology, an abnormal bone formation projecting into soft tissues or the external auditory canal (surfer's ear), often stimulated by chronic trauma or cold water exposure.",
    "quotes": [
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "A localized **exostosis** arises from the periosteal surface as a dense bony projection preserving lamellar structure."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Hereditary multiple **exostosis** leads to asymmetric limb shortening and secondary compressive neuropathies in growing children."
      },
      {
        "author": "William Stewart Halsted",
        "work": "Surgical Papers",
        "quote": "Surgical excision of the symptomatic **exostosis** must remove the entire cartilaginous cap to prevent local recurrence."
      }
    ]
  },
  "Dashboard — oste\\hyperostosis.md": {
    "primary": "An excessive or abnormal overgrowth and thickening of bone tissue.",
    "secondary": "In rheumatology and skeletal radiology, pathological diffuse cortical thickening, such as diffuse idiopathic skeletal hyperostosis (DISH) or hyperostosis frontalis interna.",
    "quotes": [
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Marked **hyperostosis** of the cranial vault reflects chronic periosteal bone deposition in response to long-standing irritation."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Radiographs in Paget's disease demonstrate generalized **hyperostosis** with irregular remodeling and cortical expansion."
      },
      {
        "author": "Harvey Cushing",
        "work": "Intracranial Tumours",
        "quote": "The overlying calvarium exhibited localized **hyperostosis** directly above the vascular meningioma."
      }
    ]
  },
  "Dashboard — oste\\monostotic.md": {
    "primary": "Affecting or confined to a single bone.",
    "secondary": "In skeletal pathology and orthopedic oncology, describing lesions (such as fibrous dysplasia, Paget's disease, or eosinophilic granuloma) that occur exclusively in one skeletal site, in contrast to polyostotic forms.",
    "quotes": [
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "The **monostotic** variant of fibrous dysplasia remains confined to a solitary femur, sparing the remaining skeleton."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "In young adults, **monostotic** skeletal lesions often present asymptomatically until discovered following minor pathological fracture."
      },
      {
        "author": "Harvey Cushing",
        "work": "Studies in Intracranial Physiology and Surgery",
        "quote": "A solitary **monostotic** thickening of the sphenoid ridge was carefully excised during the frontal craniotomy."
      }
    ]
  },
  "Dashboard — oste\\oste.md": {
    "primary": "A combining form and morpheme derived from Greek ὀστέον (osteon) signifying bone.",
    "secondary": "In medical and biological terminology, the prefix (frequently osteo-) denoting bone tissue, skeletal structures, or osseous diseases (as in osteocyte, osteotomy, osteoarthritis).",
    "quotes": [
      {
        "author": "Walter William Skeat",
        "work": "An Etymological Dictionary of the English Language",
        "quote": "The formative **oste-** is derived from Greek osteon, cognate with Latin os and Sanskrit asthi, meaning bone."
      },
      {
        "author": "Henry George Liddell",
        "work": "A Greek-English Lexicon",
        "quote": "In Hippocratic and Galenic medical treatises, compounds beginning with **oste-** refer to skeletal fracture and bone physiology."
      },
      {
        "author": "Eric Partridge",
        "work": "Origins: A Short Etymological Dictionary of Modern English",
        "quote": "Surgical vocabulary draws continuously upon **oste-** to name pathological conditions and operative interventions on the skeleton."
      }
    ]
  },
  "Dashboard — oste\\osteal.md": {
    "primary": "Relating to, consisting of, or resembling bone; osseous.",
    "secondary": "In histology and comparative osteology, describing anatomical structures, membranes, and cellular processes directly associated with bone matrix formation or mineral turnover.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Vertebrated Animals",
        "quote": "The evolution of the vertebrate endoskeleton accompanied the gradual replacement of cartilage by true **osteal** tissue."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Reparative callus formation demonstrates the latent capacity of connective tissue cells to differentiate into **osteal** matrix."
      },
      {
        "author": "Richard Owen",
        "work": "On the Archetype and Homologies of the Vertebrate Skeleton",
        "quote": "Every cranial segment displays homologies in its **osteal** components across the vertebrate series."
      }
    ]
  },
  "Dashboard — oste\\Osteichthyes.md": {
    "primary": "A major taxonomic class or superclass of aquatic vertebrates comprising the bony fishes, in contrast to the cartilaginous fishes (Chondrichthyes).",
    "secondary": "In ichthyology and vertebrate evolutionary biology, the clade of jawed fish possessing an internal skeleton composed predominantly of true bone tissue, an operculum covering the gills, and swim bladders or lungs.",
    "quotes": [
      {
        "author": "Louis Agassiz",
        "work": "Recherches sur les Poissons Fossiles",
        "quote": "The great division of the **Osteichthyes** encompasses the vast majority of living freshwater and marine species, distinguished by true osseous skeletons."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Vertebrated Animals",
        "quote": "Dermal armor and ossified endoskeletal elements distinguish the **Osteichthyes** from primitive cartilaginous elasmobranchs."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "The Structure of Evolutionary Theory",
        "quote": "The radiation of the **Osteichthyes** during the Devonian period laid the skeletal foundation for subsequent terrestrial tetrapod evolution."
      }
    ]
  },
  "Dashboard — oste\\osteitis.md": {
    "primary": "Inflammation of bone tissue.",
    "secondary": "In clinical pathology, acute or chronic inflammatory disease of bone, such as osteitis deformans (Paget's disease of bone) or osteitis fibrosa cystica (hyperparathyroid bone disease).",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "In advanced cases of **osteitis** deformans, the enlarged cranium and bowed tibiae present a characteristic diagnostic picture."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Suppurative **osteitis** leads directly to thrombosis of Haversian canals and subsequent sequestration of necrotic bone fragments."
      },
      {
        "author": "James Paget",
        "work": "On a Form of Chronic Inflammation of Bones",
        "quote": "I have proposed the designation **osteitis** deformans to signify the progressive enlargement and softening of the long bones."
      }
    ]
  },
  "Dashboard — oste\\ostensible.md": {
    "primary": "Stated, appearing, or declared to be true, but perhaps not so in reality; apparent; professed.",
    "secondary": "In rhetoric and diplomatic history, serving as an outward pretext or plausible justification designed to conceal underlying motives or covert intentions.",
    "quotes": [
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The **ostensible** reason for the expedition was the protection of the frontier, though the true motive was territorial conquest."
      },
      {
        "author": "John Locke",
        "work": "An Essay Concerning Human Understanding",
        "quote": "Men frequently adopt opinions for reasons other than their **ostensible** logical justifications."
      },
      {
        "author": "Edmund Burke",
        "work": "Reflections on the Revolution in France",
        "quote": "Beneath their **ostensible** declarations of liberty and equality lay a ruthless ambition to overthrow constitutional order."
      }
    ]
  },
  "Dashboard — oste\\ostensibly.md": {
    "primary": "Apparently or outwardly, but not necessarily genuinely; supposedly; professedly.",
    "secondary": "In legal and historical analysis, denoting actions undertaken under a public pretext while serving private or ulterior purposes.",
    "quotes": [
      {
        "author": "Adam Smith",
        "work": "The Wealth of Nations",
        "quote": "Trade restrictions were **ostensibly** enacted for the protection of domestic manufacture, but served the monopoly profits of merchants."
      },
      {
        "author": "George Orwell",
        "work": "Homage to Catalonia",
        "quote": "The militias were reorganized **ostensibly** to increase military efficiency, but in practice to suppress political dissidents."
      },
      {
        "author": "Alexis de Tocqueville",
        "work": "Democracy in America",
        "quote": "Laws that are **ostensibly** enacted for the general welfare often bear disproportionately upon vulnerable minorities."
      }
    ]
  },
  "Dashboard — oste\\ostensive.md": {
    "primary": "Manifesting, demonstrating, or pointing directly to an object or instance; directly demonstrative.",
    "secondary": "In philosophy of language and epistemology, referring to direct definition or teaching by pointing to an exemplar (ostensive definition), rather than through verbal description.",
    "quotes": [
      {
        "author": "Ludwig Wittgenstein",
        "work": "Philosophical Investigations",
        "quote": "An **ostensive** definition can be variously interpreted in every case unless the grammar of the language-game is already established."
      },
      {
        "author": "Bertrand Russell",
        "work": "Human Knowledge: Its Scope and Limits",
        "quote": "All empirical vocabulary must ultimately trace its meaning back to **ostensive** acquaintance with concrete sensory data."
      },
      {
        "author": "John Stuart Mill",
        "work": "A System of Logic",
        "quote": "The most primitive mode of explaining names is the **ostensive** method of pointing directly at the named object."
      }
    ]
  },
  "Dashboard — oste\\ostensorium.md": {
    "primary": "A vessel or sacred receptacle used in the Roman Catholic Church to display the consecrated Eucharistic host for veneration; a monstrance.",
    "secondary": "In ecclesiastical art history and liturgical studies, an ornate, radiant metalwork shrine (derived from Latin ostendere, to show) designed with a glass-enclosed lunette surrounded by solar rays.",
    "quotes": [
      {
        "author": "John Henry Newman",
        "work": "Apologia Pro Vita Sua",
        "quote": "The priest elevated the glittering **ostensorium** amid clouds of incense, blessing the kneeling congregation."
      },
      {
        "author": "Walter Pater",
        "work": "Marius the Epicurean",
        "quote": "In the solemn liturgical mystery, the golden **ostensorium** shone like a sun amidst the shadowed sanctuary."
      },
      {
        "author": "Desiderius Erasmus",
        "work": "Praise of Folly",
        "quote": "The multitude gazes in awe upon the gem-encrusted **ostensorium**, revering outward splendor above spiritual repentance."
      }
    ]
  },
  "Dashboard — oste\\ostentate.md": {
    "primary": "To display or exhibit something boastfully, conspicuously, or with pretension.",
    "secondary": "In archaic English literature and classical rhetoric, to make an elaborate, vainglorious public show of one's wealth, knowledge, or virtues.",
    "quotes": [
      {
        "author": "Francis Bacon",
        "work": "The Advancement of Learning",
        "quote": "Vain scholars love to **ostentate** their learning in strange phrases rather than advance solid knowledge."
      },
      {
        "author": "Robert Burton",
        "work": "The Anatomy of Melancholy",
        "quote": "Proud men seek every occasion to **ostentate** their costly apparel and ancestral pedigrees before the crowd."
      },
      {
        "author": "Thomas Browne",
        "work": "Pseudodoxia Epidemica",
        "quote": "It is an unseemly weakness to **ostentate** miracles where natural causes sufficiently explain the observed effect."
      }
    ]
  },
  "Dashboard — oste\\ostentation.md": {
    "primary": "Pretentious and vulgar display, especially of wealth and luxury, intended to impress or attract notice.",
    "secondary": "In moral philosophy and social satire, an excessive, self-aggrandizing demonstration of status, learning, or piety aimed at soliciting public admiration.",
    "quotes": [
      {
        "author": "Adam Smith",
        "work": "The Theory of Moral Sentiments",
        "quote": "It is the vanity of human nature that drives men to parade their fortunes with vulgar **ostentation**."
      },
      {
        "author": "Jane Austen",
        "work": "Pride and Prejudice",
        "quote": "Elizabeth saw that Mr. Collins was resolved to make an **ostentation** of his intimacy with Lady Catherine."
      },
      {
        "author": "Francis Bacon",
        "work": "Essays",
        "quote": "Excessive **ostentation** in apparel or retinue is rather a sign of inward emptiness than of true magnanimity."
      }
    ]
  },
  "Dashboard — oste\\ostentatious.md": {
    "primary": "Characterized by vulgar or pretentious display; designed to impress or attract notice.",
    "secondary": "In cultural and behavioral critique, conspicuously elaborate, flamboyant, or extravagant in manner, dress, or spending.",
    "quotes": [
      {
        "author": "Charles Dickens",
        "work": "Great Expectations",
        "quote": "His pocketbook, his heavy watch-chain, and his whole manner were an **ostentatious** proclamation of newfound wealth."
      },
      {
        "author": "Thorstein Veblen",
        "work": "The Theory of the Leisure Class",
        "quote": "The leisure class affirms its social superiority through an **ostentatious** expenditure of unearned wealth."
      },
      {
        "author": "George Eliot",
        "work": "Middlemarch",
        "quote": "She shrank from the **ostentatious** luxury of the drawing-room, longing for simplicity and purposeful work."
      }
    ]
  },
  "Dashboard — oste\\ostentatiously.md": {
    "primary": "In a pretentious, showy, or conspicuous manner calculated to attract notice.",
    "secondary": "In narrative literature, performing an action with deliberate visual emphasis or affectation to ensure observation by onlookers.",
    "quotes": [
      {
        "author": "Arthur Conan Doyle",
        "work": "The Adventures of Sherlock Holmes",
        "quote": "The visitor **ostentatiously** looked at his pocket watch, sighing heavily to indicate his urgent impatience."
      },
      {
        "author": "Mark Twain",
        "work": "The Adventures of Tom Sawyer",
        "quote": "Tom walked **ostentatiously** past the window, whistling loudly and pretending not to notice Becky Thatcher."
      },
      {
        "author": "Henry James",
        "work": "The Portrait of a Lady",
        "quote": "He **ostentatiously** arranged his papers upon the mahogany desk, basking in the deference of his subordinates."
      }
    ]
  },
  "Dashboard — oste\\ostentatiousness.md": {
    "primary": "The quality or state of being ostentatious; showiness; pretentious display.",
    "secondary": "In aesthetic critique and sociology, an excessive fondness for outward glitter, flamboyant luxury, or theatrical self-dramatization.",
    "quotes": [
      {
        "author": "Ralph Waldo Emerson",
        "work": "Essays: First Series",
        "quote": "True greatness is simple and unadorned, detesting the noisy **ostentatiousness** of the shallow multitude."
      },
      {
        "author": "Thorstein Veblen",
        "work": "The Theory of the Leisure Class",
        "quote": "The competitive urge to surpass rivals drives the **ostentatiousness** of fashionable suburban architecture."
      },
      {
        "author": "William Hazlitt",
        "work": "Table-Talk",
        "quote": "His conversation suffered from constant **ostentatiousness**, a ceaseless effort to dazzle the company with cheap wit."
      }
    ]
  },
  "Dashboard — oste\\osteoarthritis.md": {
    "primary": "A degenerative joint disease characterized by the breakdown and eventual loss of cartilage of one or more joints.",
    "secondary": "In rheumatology and orthopedic pathology, the most common form of arthritis, involving progressive degradation of articular cartilage, subchondral bone sclerosis, and osteophyte formation.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "In chronic **osteoarthritis**, the articular cartilage is gradually worn away, exposing the polished eburnated bone beneath."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Microscopic sections in severe **osteoarthritis** reveal chondrocyte clustering and deep fibrillations of the articular cartilage."
      },
      {
        "author": "Harvey Cushing",
        "work": "Studies in Intracranial Physiology and Surgery",
        "quote": "Cervical spine mobility was significantly restricted by advanced degenerative **osteoarthritis**."
      }
    ]
  },
  "Dashboard — oste\\osteoblast.md": {
    "primary": "A bone-forming cell that secretes the collagenous matrix (osteoid) and coordinates its mineralization.",
    "secondary": "In histology and bone physiology, a specialized mesenchymal cell that produces alkaline phosphatase, type I collagen, and osteocalcin, transforming into an osteocyte when trapped in mineralized matrix.",
    "quotes": [
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "The active **osteoblast** deposits layers of osseous matrix, gradually enclosing itself within a lacuna to become a mature bone corpuscle."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Bone repair after fracture relies upon vigorous proliferation of the **osteoblast** population derived from periosteum."
      },
      {
        "author": "Alexander Maximow",
        "work": "A Text-Book of Histology",
        "quote": "Under parathyroid hormone modulation, the **osteoblast** regulates both matrix deposition and osteoclastic bone resorption."
      }
    ]
  },
  "Dashboard — oste\\osteoblastoma.md": {
    "primary": "A rare, benign, osteoid-producing bone tumor histologically related to osteoid osteoma but larger in size (typically greater than 2 centimeters).",
    "secondary": "In orthopedic oncology and bone pathology, a vascular osteoblastic neoplasm commonly arising in the posterior elements of the spine and long bones, characterized by progressive local bone destruction.",
    "quotes": [
      {
        "author": "William Stewart Halsted",
        "work": "Surgical Papers",
        "quote": "Surgical curettage of a spinal **osteoblastoma** must be followed by bone grafting to restore structural stability."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Histological differentiation between a benign **osteoblastoma** and low-grade osteosarcoma requires careful assessment of mitotic atypia."
      },
      {
        "author": "William Osler",
        "work": "Modern Medicine: Its Theory and Practice",
        "quote": "Persistent nocturnal back pain in adolescents should prompt radiological evaluation for vertebral **osteoblastoma**."
      }
    ]
  },
  "Dashboard — oste\\osteochondritis.md": {
    "primary": "Inflammation of both bone and its overlying or adjacent cartilage.",
    "secondary": "In pediatric orthopedics, a group of self-limiting disorders affecting ossification centers in growing children, such as osteochondritis dissecans or juvenile osteochondritis of the femoral head (Legg-Calvé-Perthes disease).",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Juvenile **osteochondritis** leads to temporary avascular softening of the epiphysis, demanding prolonged relief from weight-bearing."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Inflammatory necrosis in **osteochondritis** dissecans frequently causes a fragment of cartilage and subchondral bone to separate into the joint cavity."
      },
      {
        "author": "William Stewart Halsted",
        "work": "Surgical Papers",
        "quote": "Arthroscopic debridement of the loose body in knee **osteochondritis** restores smooth gliding of the joint surfaces."
      }
    ]
  },
  "Dashboard — oste\\osteochondroma.md": {
    "primary": "The most common benign bone tumor, consisting of a cartilage-capped bony projection on the external surface of a bone.",
    "secondary": "In orthopedic oncology, an exostosis originating near the growth plate (physis) of long bones, which ceases growing with skeletal maturity but carries a small risk of malignant transformation into chondrosarcoma.",
    "quotes": [
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "The histological structure of an **osteochondroma** faithfully mirrors normal endochondral ossification beneath its hyaline cartilage cap."
      },
      {
        "author": "William Stewart Halsted",
        "work": "Surgical Papers",
        "quote": "Excision of a pedunculated **osteochondroma** must include its cartilaginous cap and contiguous periosteum."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Symptomatic compression of the peroneal nerve by a proximal fibular **osteochondroma** requires timely surgical relief."
      }
    ]
  },
  "Dashboard — oste\\osteochondrosis.md": {
    "primary": "A family of developmental orthopedic disorders in children and adolescents affecting the centers of bone ossification, characterized by localized tissue necrosis followed by calcification and repair.",
    "secondary": "In veterinary and human orthopedics, a failure of endochondral ossification leading to ischemic necrosis of the growing epiphysis or apophysis (such as Scheuermann's disease or Osgood-Schlatter lesion).",
    "quotes": [
      {
        "author": "William Osler",
        "work": "Modern Medicine: Its Theory and Practice",
        "quote": "Vertebral **osteochondrosis** in adolescents leads to progressive thoracic kyphosis and wedge-shaped deformities of vertebral bodies."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "The initial phase of **osteochondrosis** involves ischemic infarction of the growth cartilage followed by fragmented revascularization."
      },
      {
        "author": "William Stewart Halsted",
        "work": "Surgical Papers",
        "quote": "Conservative management of tibial tubercle **osteochondrosis** usually yields complete recovery upon skeletal maturity."
      }
    ]
  },
  "Dashboard — oste\\osteoclasis.md": {
    "primary": "The surgical intentional fracturing of a deformed bone to remedy a deformity, or the biological process of bone resorption by osteoclasts.",
    "secondary": "In orthopedic surgery and physiological histology, either manual or instrumental osteotomy performed to correct malunion, or cellular osteolysis mediated by multi-nucleated osteoclasts dissolving mineralized bone matrix.",
    "quotes": [
      {
        "author": "William Stewart Halsted",
        "work": "Surgical Papers",
        "quote": "Controlled manual **osteoclasis** of the malunited radius allowed anatomical realignment without open operative exposure."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Microscopic lacunae of Howship demonstrate active **osteoclasis**, where specialized multinucleated giant cells resorb the bony trabeculae."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "In severe rachitic bowing of the lower limbs, closed **osteoclasis** was successfully performed to straighten the legs."
      }
    ]
  }
};

console.log('Starting Body Rem B Batch 1 curation (' + Object.keys(batchData).length + ' words)...');
const updated = updateNotesBatch(baseClusterDir, batchData);
console.log('Batch 1 complete: successfully updated ' + updated + ' notes.');
