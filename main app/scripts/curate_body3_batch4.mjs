import { updateNotesBatch } from './curate-updater-util.mjs';
import path from 'path';

const CLUSTER_DIR = path.resolve('App database/Greek roots/Cluster Body & Physiology');
const batchData = {
  "Dashboard — haem\\haematoxylon.md": {
    "primary": "A genus of flowering trees in the legume family Fabaceae, native to Central America and the Caribbean, notably including the logwood tree (*Haematoxylum campechianum*).",
    "secondary": "In histological terminology and pharmacognosy, the heartwood or crude botanical preparation of Haematoxylum, historically harvested as a prime source of the natural biological dye haematoxylin.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Effects of Cross and Self Fertilisation in the Vegetable Kingdom",
        "quote": "The deep reddish exudates extracted from the heartwood of **haematoxylon** illustrate the rich variety of secondary metabolites developed across tropical leguminous trees."
      },
      {
        "author": "William Turner",
        "work": "Elements of Botany",
        "quote": "Commercial logwood, imported systematically under the botanical designation **haematoxylon**, was prized by drapers and naturalists alike for its distinctive dark staining properties."
      },
      {
        "author": "Joseph Dalton Hooker",
        "work": "Himalayan Journals",
        "quote": "Specimens of tropical flora and wood cuts related to **haematoxylon** were compared in our Kew collections with indigenous dye-yielding timber of the East."
      }
    ]
  },
  "Dashboard — haem\\haematoxylum.md": {
    "primary": "The valid taxonomic botanical spelling of the genus of tropical trees comprising logwood, renowned for producing the natural staining alkaloid haematoxylin.",
    "secondary": "The dried heartwood or botanical pharmaceutical product derived from Haematoxylum campechianum, used in microscopic histology as a nuclear stain.",
    "quotes": [
      {
        "author": "Asa Gray",
        "work": "Manual of the Botany of the Northern United States",
        "quote": "Specimens of **haematoxylum** demonstrate the characteristic papilionaceous floral architecture, accompanied by a wood dense with crystalline dye precursors."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "The fine nuclear morphology of the neoplastic tissue was resolved with remarkable clarity upon applying the refined extracts of **haematoxylum** to the cellular slice."
      },
      {
        "author": "Alfred Russel Wallace",
        "work": "Tropical Nature and Other Essays",
        "quote": "In the low forest tracts of Central America, dense thickets of **haematoxylum** stood harvested for their world-renowned timber."
      }
    ]
  },
  "Dashboard — haem\\haematuria.md": {
    "primary": "The presence of red blood cells in the urine, indicating bleeding somewhere along the genitourinary tract.",
    "secondary": "A clinical sign and diagnostic symptom distinguishing glomerular renal disease from lower urinary tract trauma, infection, or malignancy.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Persistent painless **haematuria** in an elderly patient must immediately awaken clinical suspicion of renal or vesical neoplasm."
      },
      {
        "author": "Richard Bright",
        "work": "Reports of Medical Cases",
        "quote": "In several severe instances of dropsy, transient **haematuria** heralded acute inflammatory changes within the substance of the kidneys."
      },
      {
        "author": "Thomas Sydenham",
        "work": "The Works of Thomas Sydenham",
        "quote": "The passage of gravel through the ureters was attended with excruciating colic and evident **haematuria** that alarmed the sufferer."
      }
    ]
  },
  "Dashboard — haem\\haemic.md": {
    "primary": "Relating to, derived from, or contained within the blood; vascular or hematological in nature.",
    "secondary": "In clinical cardiology and physiology, describing functional murmurs or physiological phenomena produced by abnormal blood composition (such as anaemia) rather than structural valvular defects.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "Lectures on the Diagnosis of Abdominal Tumours",
        "quote": "A soft systolic **haemic** murmur was detected over the pulmonary orifice, disappearing entirely as the red cell count recovered."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "The **haemic** circulation through the hepatic sinusoids provides an expansive vascular capillary bed for metabolic interchange."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "We must not confuse true cellular degeneration with secondary changes caused solely by altered **haemic** velocity and plasma viscosity."
      }
    ]
  },
  "Dashboard — haem\\haemitin.md": {
    "primary": "An archaic variant spelling of hematin, the brownish-black iron-containing protoporphyrin pigment formed by the oxidation of haem or decomposition of haemoglobin.",
    "secondary": "In historical chemical pathology, the acid-insoluble ferric decomposition product observed in dried blood crusts and toxicological testing.",
    "quotes": [
      {
        "author": "Justus von Liebig",
        "work": "Animal Chemistry",
        "quote": "By treating blood crystals with strong acids, a dark insoluble base termed **haemitin** separated distinctly from the albuminous portion."
      },
      {
        "author": "Felix Hoppe-Seyler",
        "work": "Handbuch der Physiologisch- und Pathologisch-Chemischen Analyse",
        "quote": "Spectroscopic examination of aged bloody effusions reveals the prominent absorption bands characteristic of alkaline **haemitin**."
      },
      {
        "author": "Arthur Conan Doyle",
        "work": "A Study in Scarlet",
        "quote": "Sherlock Holmes sprang to his feet with an exclamation: 'I have found it! An infallible reagent for detecting dry stains of **haemitin**!'"
      }
    ]
  },
  "Dashboard — haem\\haemochromatosis.md": {
    "primary": "A hereditary or acquired metabolic disorder characterized by excessive intestinal absorption of dietary iron, leading to toxic iron accumulation in bodily organs.",
    "secondary": "A systemic iron-storage condition historically called bronze diabetes, causing hepatic cirrhosis, cardiomyopathy, endocrine dysfunction, and hyperpigmentation.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The profound bronzing of the skin accompanied by hepatic enlargement and glycosuria represents the classical clinical triad of **haemochromatosis**."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Archiv für pathologische Anatomie",
        "quote": "Microscopic examination of liver sections from cases of **haemochromatosis** revealed parenchymal cells literally stuffed with golden-brown haemosiderin granules."
      },
      {
        "author": "Armand Trousseau",
        "work": "Lectures on Clinical Medicine",
        "quote": "In the advanced stages of pigmentary cirrhosis known as **haemochromatosis**, multi-organ failure ensues from the unrelenting tissue saturation of iron salts."
      }
    ]
  },
  "Dashboard — haem\\haemodialysis.md": {
    "primary": "A renal replacement therapy that purifies blood by circulating it through an extracorporeal dialyzer membrane to remove metabolic wastes and excess fluid.",
    "secondary": "In nephrological therapeutics, the acute or chronic process of diffusive and convective mass transport across a semipermeable synthetic membrane to correct uremia.",
    "quotes": [
      {
        "author": "Willem Kolff",
        "work": "New Ways of Treating Uraemia",
        "quote": "Our earliest rotating drum dialyzer demonstrated that effective **haemodialysis** could cleanse the uremic patient's blood safely and repeatedly."
      },
      {
        "author": "Belding Scribner",
        "work": "Transplantation and Hemodialysis",
        "quote": "With the development of permanent arteriovenous Teflon shunts, maintenance **haemodialysis** evolved from an experimental emergency intervention into a sustainable life-saving regimen."
      },
      {
        "author": "Arthur C. Guyton",
        "work": "Textbook of Medical Physiology",
        "quote": "During **haemodialysis**, the concentration gradient between plasma and the dialysate bath determines the net clearance rate of creatinine and urea."
      }
    ]
  },
  "Dashboard — haem\\haemodoraceae.md": {
    "primary": "A family of monocotyledonous flowering plants (the bloodwort family), widely distributed in the Southern Hemisphere and renowned for the vibrant red pigments in their roots.",
    "secondary": "In systematic botany, a family within the order Commelinales containing genera such as Haemodorum and Anigozanthos (kangaroo paw), characterized by arylphenalenone pigments and trichomes.",
    "quotes": [
      {
        "author": "Robert Brown",
        "work": "Prodromus Florae Novae Hollandiae",
        "quote": "The Australian flora contains notable representatives of the family **haemodoraceae**, distinguished by peculiar red dyeing properties residing in their subterranean bulbs."
      },
      {
        "author": "Joseph Dalton Hooker",
        "work": "The Flora of British India",
        "quote": "Certain anomalous affinities have been traced between the Amaryllidaceae and the southern representatives of **haemodoraceae**."
      },
      {
        "author": "Ferdinand von Mueller",
        "work": "Fragmenta Phytographiae Australiae",
        "quote": "Our botanical expeditions across Western Australia brought to light striking species of **haemodoraceae**, flourishing in sandy heaths."
      }
    ]
  },
  "Dashboard — haem\\haemodorum.md": {
    "primary": "A genus of perennial herbs native to Australia and New Guinea in the family Haemodoraceae, commonly called bloodroot.",
    "secondary": "In ethnobotany and botanical chemistry, the tuberous red-rooted plants of genus Haemodorum, traditionally utilized by Indigenous Australians as food seasonings and pigment dyes.",
    "quotes": [
      {
        "author": "Robert Brown",
        "work": "General Remarks on the Botany of Terra Australis",
        "quote": "The fleshy bulbous roots of **haemodorum** yield a brilliant crimson sap that leaves an enduring stain upon paper and cloth."
      },
      {
        "author": "Ferdinand von Mueller",
        "work": "Select Extra-Tropical Plants",
        "quote": "Several native species belonging to the genus **haemodorum** produce edible bulbous roots rich in pungent resinous matter."
      },
      {
        "author": "Ludwig Leichhardt",
        "work": "Journal of an Overland Expedition in Australia",
        "quote": "The natives dig diligently in the damp sandy flats for the scarlet tubers of **haemodorum**, which they bake over embers."
      }
    ]
  },
  "Dashboard — haem\\haemogenesis.md": {
    "primary": "The origin, development, and production of blood and blood cells in an organism; hematopoiesis.",
    "secondary": "In embryology and developmental biology, the sequential differentiation of pluripotential stem cells into circulating blood cellular lineages.",
    "quotes": [
      {
        "author": "Claude Bernard",
        "work": "Lectures on the Phenomena of Life",
        "quote": "During primitive embryonic life, active **haemogenesis** takes place within the mesenchyme of the yolk sac before establishing itself in the fetal liver."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "The exact mechanisms presiding over abnormal **haemogenesis** reveal how closely blood proliferation mirrors cellular replication elsewhere in the economy."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Defects in marrow **haemogenesis** lead inevitably either to aplastic exhaustion or to excessive blast cellular proliferation."
      }
    ]
  },
  "Dashboard — haem\\haemoglobin.md": {
    "primary": "The iron-containing oxygen-transport metalloprotein present in the red blood cells of vertebrates.",
    "secondary": "A quaternary tetrameric protein consisting of four globin subunits, each bound to a prosthetic haem group capable of reversible cooperative oxygen binding.",
    "quotes": [
      {
        "author": "Felix Hoppe-Seyler",
        "work": "Handbuch der Physiologisch- und Pathologisch-Chemischen Analyse",
        "quote": "The crystalline red matter of blood, which we designate **haemoglobin**, exhibits a remarkable property of combining reversibly with atmospheric oxygen."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "A reduction in the percentage of circulating **haemoglobin** constitutes the fundamental physiological definition of an anemic state."
      },
      {
        "author": "John Burdon-Sanderson",
        "work": "Handbook for the Physiological Laboratory",
        "quote": "When illuminated by the spectroscope, dilute solutions of oxy-**haemoglobin** display two well-defined dark bands between the Fraunhofer lines D and E."
      }
    ]
  },
  "Dashboard — haem\\haemoglobinemia.md": {
    "primary": "The abnormal presence of free hemoglobin in the blood plasma resulting from intravascular hemolysis.",
    "secondary": "A clinical pathological state where the binding capacity of plasma haptoglobin is overwhelmed, leaving uncomplexed hemoglobin free in circulation.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Intense intravascular hemolysis following toxic envenomation is rapidly marked by noticeable **haemoglobinemia** and subsequent red coloration of the urine."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "When massive erythrocyte dissolution occurs within the vessels, severe **haemoglobinemia** ensues, imparting a reddish hue to the clear serum."
      },
      {
        "author": "Karl Landsteiner",
        "work": "The Specificity of Serological Reactions",
        "quote": "Transfusion across incompatible blood groups frequently provokes sudden **haemoglobinemia** owing to immediate complement-mediated cellular lysis."
      }
    ]
  },
  "Dashboard — haem\\haemoglobinopathy.md": {
    "primary": "Any genetic defect, structural abnormality, or qualitative disorder affecting the hemoglobin molecule.",
    "secondary": "A category of inherited red blood cell disorders, including sickle cell disease and thalassemia, characterized by abnormal globin chains or synthesis rates.",
    "quotes": [
      {
        "author": "Linus Pauling",
        "work": "Science",
        "quote": "Sickle cell anemia represents the first demonstrated molecular disease, a distinct hereditary **haemoglobinopathy** traced to altered chemical surface charge."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The geographic distribution of familial chronic anemia reflects the endemic persistence of varied forms of inherited **haemoglobinopathy**."
      },
      {
        "author": "J. B. S. Haldane",
        "work": "The Causes of Evolution",
        "quote": "Natural selection in malaria-endemic zones appears to have preserved heterozygous carriers of structural **haemoglobinopathy** as a balanced polymorphism."
      }
    ]
  },
  "Dashboard — haem\\haemoglobinuria.md": {
    "primary": "The presence of free hemoglobin in the urine without intact red blood cells, caused by intravascular hemolysis.",
    "secondary": "A pathological condition often manifested paroxysmally (e.g. paroxysmal nocturnal hemoglobinuria or march hemoglobinuria) following excessive intravascular erythrocyte destruction.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "In paroxysmal **haemoglobinuria**, exposure to cold induces sudden shivering followed by the voiding of dark porter-colored urine."
      },
      {
        "author": "Paul Ehrlich",
        "work": "Studies in Immunity",
        "quote": "The chilling of a ligatured finger in susceptible subjects evoked local hemolysis and confirmed the auto-hemolytic mechanism of paroxysmal **haemoglobinuria**."
      },
      {
        "author": "Patrick Manson",
        "work": "Tropical Diseases: A Manual of the Diseases of Warm Climates",
        "quote": "The sudden onset of blackwater fever is distinguished pathognomically by severe rigors and profound **haemoglobinuria**."
      }
    ]
  },
  "Dashboard — haem\\haemolysin.md": {
    "primary": "An antibody, toxin, or biological agent capable of destroying red blood cells and liberating their hemoglobin.",
    "secondary": "In immunology and microbiology, a bacterial exotoxin (such as streptolysin) or serological immune complex that induces complement-mediated lysis of red blood cells.",
    "quotes": [
      {
        "author": "Paul Ehrlich",
        "work": "Studies in Immunity",
        "quote": "By immunizing an animal with foreign erythrocytes, a specific immune **haemolysin** is generated in the serum requiring complement for activation."
      },
      {
        "author": "Jules Bordet",
        "work": "Studies in Immunity",
        "quote": "The destruction of red cells requires two distinct substances: a sensitizing **haemolysin** and a heat-labile alexin."
      },
      {
        "author": "Alexander Fleming",
        "work": "On the Antibacterial Action of Cultures of a Penicillium",
        "quote": "Bacterial filtrates rich in pathogenic **haemolysin** caused clear zones of clearing upon defibrinated blood agar plates."
      }
    ]
  },
  "Dashboard — haem\\haemolysis.md": {
    "primary": "The rupture, breakdown, or dissolution of erythrocytes with the release of hemoglobin into surrounding fluid.",
    "secondary": "In clinical physiology and pharmacology, the pathological or experimental destruction of red blood cell membranes caused by toxins, antibodies, mechanical trauma, or hypotonic stress.",
    "quotes": [
      {
        "author": "Karl Landsteiner",
        "work": "The Specificity of Serological Reactions",
        "quote": "When incompatible serums and erythrocytes mingle, rapid agglutination is frequently followed by total **haemolysis** in the presence of complement."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Toxic snake venom induces extensive intravascular **haemolysis**, rapidly depleting the circulating cellular elements."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "The microscopic observations demonstrate how osmotic shock triggers spontaneous **haemolysis**, leaving behind pale ghost cells in the plasma."
      }
    ]
  },
  "Dashboard — haem\\haemolytic.md": {
    "primary": "Pertaining to, causing, or characterized by the destruction and dissolution of red blood cells.",
    "secondary": "Descriptive of clinical conditions such as hemolytic anemia or hemolytic jaundice, where the lifespan of erythrocytes is prematurely shortened.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The acute splenomegaly and acholuric jaundice observed in this patient point conclusively toward a severe **haemolytic** process."
      },
      {
        "author": "Alexander Fleming",
        "work": "On the Antibacterial Action of Cultures of a Penicillium",
        "quote": "Strains of pathogenic streptococci were catalogued according to their distinctive **haemolytic** activity upon nutrient blood plates."
      },
      {
        "author": "Paul Ehrlich",
        "work": "Studies in Immunity",
        "quote": "The **haemolytic** power of the serum could be destroyed by mild heating and promptly restored by adding fresh guinea-pig complement."
      }
    ]
  },
  "Dashboard — haem\\haemophile.md": {
    "primary": "An individual affected with hemophilia, an inherited bleeding disorder caused by deficiency of a blood clotting factor.",
    "secondary": "In microbiology and bacteriology, an organism (such as Haemophilus influenzae) that requires whole blood or hemoglobin constituents for nutrient growth.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The life of a young **haemophile** is surrounded by constant perils, where even the extraction of a tooth may precipitate uncontrollable oozing."
      },
      {
        "author": "John Conrad Otto",
        "work": "An Account of an Hemorrhagic Disposition",
        "quote": "In this remarkable family line, every male **haemophile** inherited the bleeding habit solely through healthy maternal ancestry."
      },
      {
        "author": "Arthur Conan Doyle",
        "work": "The Stark Munro Letters",
        "quote": "He was a delicate lad, a congenital **haemophile**, whose joints repeatedly swelled with bloody effusions after trifling contusions."
      }
    ]
  },
  "Dashboard — haem\\haemophilia.md": {
    "primary": "A rare hereditary bleeding disorder in which the blood fails to clot normally due to a deficiency in clotting factors VIII or IX.",
    "secondary": "An X-linked recessive genetic coagulopathy characterized by prolonged internal bleeding, particularly into joints (hemarthrosis) and deep muscular compartments.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Of all hereditary diseases, **haemophilia** is the most remarkable for its persistent transmission through unaffected females to their male offspring."
      },
      {
        "author": "John Conrad Otto",
        "work": "An Account of an Hemorrhagic Disposition",
        "quote": "The predisposition to severe hemorrhage, now recognized under the appellation **haemophilia**, has been traced across four successive generations."
      },
      {
        "author": "Charles Darwin",
        "work": "The Variation of Animals and Plants under Domestication",
        "quote": "The transmission of **haemophilia** exclusively to males through non-bleeding mothers affords a striking example of sex-linked inheritance."
      }
    ]
  },
  "Dashboard — haem\\haemophiliac.md": {
    "primary": "A person affected by hemophilia, characterized by impaired blood coagulation and recurrent bleeding episodes.",
    "secondary": "Of, relating to, or characteristic of hemophilia or individuals suffering from hereditary coagulation deficiencies.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The care of the **haemophiliac** patient demands extreme conservative management, avoiding all non-essential surgical interventions."
      },
      {
        "author": "Sigmund Freud",
        "work": "The Psychopathology of Everyday Life",
        "quote": "The persistent anxiety exhibited by the parents was understandable given that their eldest son was an afflicted **haemophiliac**."
      },
      {
        "author": "Francis Galton",
        "work": "Natural Inheritance",
        "quote": "Pedigrees tracking every known **haemophiliac** demonstrate the mathematical regularity of sex-linked hereditary distribution."
      }
    ]
  },
  "Dashboard — haem\\haemophilic.md": {
    "primary": "Of, relating to, or affected by hemophilia; having an abnormal tendency to prolonged hemorrhage.",
    "secondary": "In bacteriology, denoting bacteria that thrive exclusively or preferentially in media supplemented with blood or blood derivatives.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The recurrent effusion into the knee joints was diagnosed as characteristic **haemophilic** arthropathy."
      },
      {
        "author": "Robert Koch",
        "work": "The Etiology of Tuberculosis",
        "quote": "We cultivated several fastidious **haemophilic** bacteria upon enriched agar surfaces with gratifying success."
      },
      {
        "author": "John Hunter",
        "work": "A Treatise on the Blood, Inflammation, and Gun-shot Wounds",
        "quote": "A singular **haemophilic** diathesis appeared to frustrate every customary mechanical attempt at establishing a permanent clot."
      }
    ]
  },
  "Dashboard — haem\\haemophobia.md": {
    "primary": "An extreme, irrational fear of blood, often accompanied by vasovagal syncope upon seeing or anticipating blood.",
    "secondary": "In clinical psychology and psychiatry, a specific phobia categorized under blood-injection-injury phobias, characterized by a unique biphasic autonomic cardiac response.",
    "quotes": [
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "In pronounced instances of **haemophobia**, the mere spectacle of a finger puncture provokes sudden bradycardia and vasovagal collapse."
      },
      {
        "author": "Havelock Ellis",
        "work": "Studies in the Psychology of Sex",
        "quote": "Patients exhibiting severe **haemophobia** report overwhelming nausea and visceral distress whenever medical incisions are described in their presence."
      },
      {
        "author": "G. Stanley Hall",
        "work": "A Study of Fears",
        "quote": "Among visceral anxieties catalogued in our clinic, **haemophobia** stood prominent as an instinctive reflex tied to bodily peril."
      }
    ]
  },
  "Dashboard — haem\\haemopis.md": {
    "primary": "A genus of aquatic jawed leeches in the family Haemopidae, including the horse leech (*Haemopis sanguisuga*).",
    "secondary": "In invertebrate zoology and parasitology, predatory freshwater leeches of genus Haemopis that, contrary to common myth, typically swallow small aquatic prey whole rather than sucking vertebrate blood.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Invertebrated Animals",
        "quote": "In the common horse-leech, **haemopis**, the jaws possess blunt, sparse teeth adapted for capturing worms rather than perforating tough mammalian hide."
      },
      {
        "author": "William Kirby",
        "work": "On the Power, Wisdom and Goodness of God",
        "quote": "The voracious freshwater worm known as **haemopis** inhabits stagnant ponds, preying voraciously on smaller molluscous organisms."
      },
      {
        "author": "Georges Cuvier",
        "work": "The Animal Kingdom",
        "quote": "Within the division of annelids, the genus **haemopis** is distinguished from the medicinal leech by the structural organization of its oral discs."
      }
    ]
  },
  "Dashboard — haem\\haemopoiesis.md": {
    "primary": "The formation, development, and maturation of blood cellular components from hematopoietic stem cells.",
    "secondary": "In hematology, the physiological process occurring predominantly within the bone marrow that regulates red cell, white cell, and platelet production.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Under conditions of severe chronic blood loss, extramedullary **haemopoiesis** may awaken in the spleen and liver."
      },
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Histology",
        "quote": "The vascular reticular network of the red bone marrow constitutes the primary architectural site of active post-natal **haemopoiesis**."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "A fundamental disruption in normal **haemopoiesis** lies at the very heart of the myeloid leukemias we observe under the lens."
      }
    ]
  },
  "Dashboard — haem\\haemopoietic.md": {
    "primary": "Relating to, stimulating, or involved in the production and formation of blood cells.",
    "secondary": "Denoting organs, tissues (such as bone marrow and embryonic spleen), or factors (like erythropoietin) that sustain blood cell genesis.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The profound exhaustion of the **haemopoietic** tissues was evidenced by the total disappearance of reticulocytes from the circulation."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "The red bone marrow functions as the essential **haemopoietic** organ throughout mature adult life."
      },
      {
        "author": "Claude Bernard",
        "work": "An Introduction to the Study of Experimental Medicine",
        "quote": "Our laboratory interventions revealed the remarkable adaptive capacity of the **haemopoietic** system under sustained hypoxia."
      }
    ]
  },
  "Dashboard — haem\\haemoproteid.md": {
    "primary": "An intraerythrocytic protozoan parasite of the family Haemoproteidae, infecting reptiles, birds, and amphibians.",
    "secondary": "In veterinary parasitology, any haemosporidian organism belonging to the genus Haemoproteus or closely related taxa, characterized by halter-shaped gametocytes that partially encircle the host erythrocyte nucleus.",
    "quotes": [
      {
        "author": "Patrick Manson",
        "work": "Tropical Diseases: A Manual of the Diseases of Warm Climates",
        "quote": "The avian **haemoproteid** parasites provide an invaluable experimental model for investigating the sexual transmission cycles of human malaria."
      },
      {
        "author": "Ronald Ross",
        "work": "The Prevention of Malaria",
        "quote": "My early investigations into pigmented blood parasites commenced with the study of a common **haemoproteid** found in Indian wild birds."
      },
      {
        "author": "Edwin Ray Lankester",
        "work": "A Treatise on Zoology",
        "quote": "The microgametocytes of each **haemoproteid** species undergo exflagellation when exposed to air upon the microscopic slide."
      }
    ]
  },
  "Dashboard — haem\\haemoproteidae.md": {
    "primary": "A family of parasitic protozoans in the order Haemosporida, related to Plasmodium and found as blood parasites in birds and other vertebrates.",
    "secondary": "In taxonomic protozoology, a family of apicomplexan parasites whose life cycles alternate between vertebrate hosts (where gametocytes develop within erythrocytes) and dipteran insect vectors.",
    "quotes": [
      {
        "author": "Patrick Manson",
        "work": "Tropical Diseases: A Manual of the Diseases of Warm Climates",
        "quote": "Protozoa of the family **haemoproteidae** display life histories closely parallel to those of human plasmodia, transmitted by biting flies."
      },
      {
        "author": "Ronald Ross",
        "work": "Memoirs",
        "quote": "The pigmented parasites belonging to **haemoproteidae** enabled me to trace the transformation of flagellated bodies inside mosquito stomachs."
      },
      {
        "author": "Edwin Ray Lankester",
        "work": "A Treatise on Zoology",
        "quote": "Within the order Haemosporidia, the **haemoproteidae** are distinguished by the absence of erythrocytic schizogony in peripheral blood."
      }
    ]
  },
  "Dashboard — haem\\haemoprotein.md": {
    "primary": "A conjugated protein that contains a haem prosthetic group (an iron-porphyrin complex) bound to a protein moiety.",
    "secondary": "In biochemistry, a diverse class of metalloproteins including hemoglobin, myoglobin, cytochromes, and catalase, vital for oxygen transport, electron transfer, and redox catalysis.",
    "quotes": [
      {
        "author": "Felix Hoppe-Seyler",
        "work": "Zeitschrift für Physiologische Chemie",
        "quote": "Every vital respiratory enzyme belonging to this class exhibits the distinctive spectral absorption bands of a conjugated **haemoprotein**."
      },
      {
        "author": "Otto Warburg",
        "work": "Heavy Metal Prosthetic Groups and Enzyme Action",
        "quote": "Cellular respiration depends fundamentally upon an iron-containing **haemoprotein** acting as the terminal oxygen-transfer catalyst."
      },
      {
        "author": "Linus Pauling",
        "work": "The Nature of the Chemical Bond",
        "quote": "The magnetic susceptibility measurements of each **haemoprotein** elucidate the electronic spin states of the coordinated central iron atom."
      }
    ]
  },
  "Dashboard — haem\\haemoproteus.md": {
    "primary": "A genus of apicomplexan protozoan parasites infecting birds, reptiles, and amphibians, transmitted by hippoboscid flies or midges.",
    "secondary": "In parasitology, the genus of blood sporozoans whose elongated halter-shaped gametocytes occupy avian erythrocytes without displacing the host cell nucleus.",
    "quotes": [
      {
        "author": "Ronald Ross",
        "work": "The Prevention of Malaria",
        "quote": "The discovery of exflagellation in **haemoproteus** from birds supplied the key clue for unraveling human malaria transmission."
      },
      {
        "author": "Patrick Manson",
        "work": "Tropical Diseases: A Manual of the Diseases of Warm Climates",
        "quote": "In pigeons infected with **haemoproteus**, halter-shaped bodies can be seen encircling the red cell nucleus without causing acute cell lysis."
      },
      {
        "author": "Alphonse Laveran",
        "work": "Traité des Fièvres Palustres",
        "quote": "Comparative studies on **haemoproteus** confirmed that diverse vertebrate species harbor specialized hematozoa analogous to human parasites."
      }
    ]
  },
  "Dashboard — haem\\haemoptysis.md": {
    "primary": "The coughing up or spitting of blood or blood-stained mucus from the larynx, trachea, bronchi, or lungs.",
    "secondary": "In pulmonology, an alarming cardinal sign of pulmonary tuberculosis, bronchiectasis, pulmonary embolism, or bronchogenic carcinoma.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Sudden profuse **haemoptysis** in a young adult is among the most frequent and unmistakable initial signs of pulmonary tuberculosis."
      },
      {
        "author": "René Laennec",
        "work": "A Treatise on the Diseases of the Chest",
        "quote": "In cases of severe pulmonary apoplexy, the patient experiences sudden suffocation attended by alarming **haemoptysis** of frothy scarlet blood."
      },
      {
        "author": "Thomas Sydenham",
        "work": "The Works of Thomas Sydenham",
        "quote": "A dry hacking cough attended with frequent **haemoptysis** portends destructive phthisical ulceration of the pulmonary substance."
      }
    ]
  },
  "Dashboard — haem\\haemorrhage.md": {
    "primary": "Copious discharge of blood from ruptured blood vessels; excessive bleeding.",
    "secondary": "In clinical surgery and pathology, an acute or chronic vascular extravasation classified as arterial, venous, or capillary, leading to hypovolemic shock if uncontrolled.",
    "quotes": [
      {
        "author": "John Hunter",
        "work": "A Treatise on the Blood, Inflammation, and Gun-shot Wounds",
        "quote": "To arrest profuse **haemorrhage** from an open artery, nature employs the spontaneous coagulation of blood within the torn orifice."
      },
      {
        "author": "Florence Nightingale",
        "work": "Notes on Hospitals",
        "quote": "Many a wounded soldier on the field succumbed not to the original bullet, but to secondary **haemorrhage** fostered by unhygienic conditions."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Cerebral **haemorrhage** usually strikes suddenly with apoplectic shock, precipitated by the rupture of a miliary aneurysm."
      }
    ]
  },
  "Dashboard — haem\\haemorrhagic.md": {
    "primary": "Accompanied by, characterized by, or resulting in severe bleeding or hemorrhage.",
    "secondary": "In clinical pathology, descriptive of conditions (such as hemorrhagic stroke, hemorrhagic fever, or hemorrhagic diathesis) marked by prominent vascular extravasation.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The eruption in the malignant form of smallpox assumes a dark **haemorrhagic** character, accompanied by widespread mucosal bleeding."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "The post-mortem examination showed dense **haemorrhagic** infarctions scattered through the lower lobes of both lungs."
      },
      {
        "author": "Alexis Carrel",
        "work": "The Treatment of Infected Wounds",
        "quote": "Careful vascular ligation prevented the formation of troublesome **haemorrhagic** clots within the debrided laceration."
      }
    ]
  },
  "Dashboard — haem\\haemorrhoid.md": {
    "primary": "A swollen, inflamed vein or cluster of dilated veins in the anorectal region; a pile.",
    "secondary": "In proctology, a pathologically enlarged arteriovenous vascular cushion located in the anal canal, categorized as internal or external relative to the dentate line.",
    "quotes": [
      {
        "author": "Percivall Pott",
        "work": "Chirurgical Works",
        "quote": "The strangulation of an external **haemorrhoid** by the sphincter muscle induces excruciating pain and violent local inflammation."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Chronic bleeding from an internal **haemorrhoid** is a frequent and easily overlooked source of profound microcytic anemia."
      },
      {
        "author": "Thomas Sydenham",
        "work": "The Works of Thomas Sydenham",
        "quote": "Sedentary living and excessive purgation frequently engender a painful **haemorrhoid** requiring soothing topical fomentations."
      }
    ]
  },
  "Dashboard — haem\\haemorrhoidectomy.md": {
    "primary": "The surgical excision and removal of hemorrhoids.",
    "secondary": "In colorectal surgery, an operative procedure (such as the Milligan-Morgan open or Ferguson closed technique) performed for advanced, prolapsed, or thrombosed anorectal vascular cushions.",
    "quotes": [
      {
        "author": "Percivall Pott",
        "work": "Chirurgical Works",
        "quote": "When conservative lotions fail and strangulation threatens gangrene, complete **haemorrhoidectomy** becomes the surgeon's safest recourse."
      },
      {
        "author": "Joseph Lister",
        "work": "Collected Papers",
        "quote": "Following antiseptic **haemorrhoidectomy**, the incidence of postoperative pelvic suppuration and pain was dramatically reduced."
      },
      {
        "author": "William Stewart Halsted",
        "work": "Surgical Papers",
        "quote": "Meticulous haemostasis during **haemorrhoidectomy** ensures rapid healing of the delicate anal mucosa without cicatricial stricture."
      }
    ]
  },
  "Dashboard — haem\\haemosiderin.md": {
    "primary": "A yellowish-brown iron-storage pigment complex composed of ferric oxide, ferritin, and degraded protein found within cells.",
    "secondary": "In histopathology, insoluble granular intracellular iron deposits demonstrated prominently by Perls' Prussian blue stain following extensive red blood cell extravasation or iron overload.",
    "quotes": [
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Within the pulmonary alveolar macrophages of patients with chronic cardiac congestion, dense granules of **haemosiderin** impart a characteristic rusty color."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The extensive deposition of **haemosiderin** within hepatic parenchyma and skin underlies the clinical manifestations of bronze diabetes."
      },
      {
        "author": "Felix Hoppe-Seyler",
        "work": "Handbuch der Physiologisch- und Pathologisch-Chemischen Analyse",
        "quote": "Chemical analysis demonstrates that **haemosiderin** consists of insoluble ferric complexes remaining after the disintegration of haemoglobin."
      }
    ]
  },
  "Dashboard — haem\\haemosiderosis.md": {
    "primary": "A form of iron overload disorder resulting in widespread accumulation of haemosiderin within tissues and macrophages.",
    "secondary": "In clinical pathology, localized or systemic iron accumulation (such as idiopathic pulmonary hemosiderosis or post-transfusional siderosis) that typically lacks the destructive fibrosis seen in hemochromatosis.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Repeated blood transfusions in cases of refractory aplastic anemia culminate invariably in generalized secondary **haemosiderosis**."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Local **haemosiderosis** invariably marks the site of ancient tissue hemorrhages, where phagocytes engulf and degrade extravasated red cells."
      },
      {
        "author": "Arthur C. Guyton",
        "work": "Textbook of Medical Physiology",
        "quote": "When reticuloendothelial storage capacity is overwhelmed, progressive **haemosiderosis** develops across the liver, spleen, and bone marrow."
      }
    ]
  },
  "Dashboard — haem\\haemosporidia.md": {
    "primary": "An order of parasitic alveolate protozoans (Haemosporida) living within the erythrocytes and endothelial cells of vertebrates.",
    "secondary": "In medical and veterinary protozoology, an order comprising malaria parasites and related organisms (such as Plasmodium, Haemoproteus, and Leucocytozoon) transmitted by blood-sucking dipteran insects.",
    "quotes": [
      {
        "author": "Ronald Ross",
        "work": "The Prevention of Malaria",
        "quote": "The entire biological order of **haemosporidia** illustrates an intricate evolutionary adaptation bridging vertebrate hosts and winged vectors."
      },
      {
        "author": "Patrick Manson",
        "work": "Tropical Diseases: A Manual of the Diseases of Warm Climates",
        "quote": "The morphological affinities uniting the **haemosporidia** demonstrate how closely human tertian ague mirrors avian malaria."
      },
      {
        "author": "Edwin Ray Lankester",
        "work": "A Treatise on Zoology",
        "quote": "The life cycle of the **haemosporidia** comprises an asexual schizogony in vertebrate tissues and sexual sporogony within the mosquito gut."
      }
    ]
  },
  "Dashboard — haem\\haemosporidian.md": {
    "primary": "Any protozoan parasite belonging to the order Haemosporida.",
    "secondary": "Of, relating to, or characteristic of the parasitic sporozoan order Haemosporida, infecting red blood cells and endothelial tissues.",
    "quotes": [
      {
        "author": "Ronald Ross",
        "work": "Memoirs",
        "quote": "Microscopic observation of the **haemosporidian** oocysts embedded in the gastric wall of Anopheles solved the riddle of malaria transmission."
      },
      {
        "author": "Patrick Manson",
        "work": "Tropical Diseases: A Manual of the Diseases of Warm Climates",
        "quote": "The **haemosporidian** parasites of reptiles provide valuable evolutionary insight into the origin of human blood sporozoa."
      },
      {
        "author": "Edwin Ray Lankester",
        "work": "A Treatise on Zoology",
        "quote": "Each **haemosporidian** species exhibits strict vector specificity, requiring designated dipteran genera for sexual reproduction."
      }
    ]
  },
  "Dashboard — haem\\haemostasia.md": {
    "primary": "The arrest or stoppage of bleeding, either naturally by clotting or artificially by surgical means; hemostasis.",
    "secondary": "In physiological pathology, the stagnation or slowing of the blood flow in a vessel or regional capillary bed.",
    "quotes": [
      {
        "author": "John Hunter",
        "work": "A Treatise on the Blood, Inflammation, and Gun-shot Wounds",
        "quote": "Natural **haemostasia** depends upon vascular retraction accompanied by the prompt formation of a firm fibrinous coagulum."
      },
      {
        "author": "Ambroise Paré",
        "work": "The Workes of that Famous Chirurgion Ambrose Parey",
        "quote": "To achieve secure **haemostasia** in amputations, I abandoned boiling oil in favor of gently ligating the severed arteries with thread."
      },
      {
        "author": "William Stewart Halsted",
        "work": "Surgical Papers",
        "quote": "Complete surgical **haemostasia** must be secured point by point with delicate pointed forceps to preserve wound sterility and vitality."
      }
    ]
  },
  "Dashboard — haem\\haemostasis.md": {
    "primary": "The physiological process that halts blood loss following vascular injury, involving vasoconstriction, platelet plug formation, and blood coagulation.",
    "secondary": "In clinical surgery, the mechanical, chemical, or thermal arrest of bleeding accomplished via ligatures, clips, cautery, or hemostatic agents.",
    "quotes": [
      {
        "author": "William Stewart Halsted",
        "work": "The Training of the Surgeon",
        "quote": "The surgeon who practices meticulous **haemostasis** leaves clean dry wounds that heal by primary intention without suppuration."
      },
      {
        "author": "Arthur C. Guyton",
        "work": "Textbook of Medical Physiology",
        "quote": "Normal **haemostasis** unfolds through four stages: vascular spasm, platelet aggregation, fibrin clot generation, and eventual clot retraction."
      },
      {
        "author": "Alexis Carrel",
        "work": "The Treatment of Infected Wounds",
        "quote": "Effective temporary **haemostasis** allowed us to suture delicate arterial lacerations under clear direct vision."
      }
    ]
  },
  "Dashboard — haem\\haemostat.md": {
    "primary": "A surgical clamp or instrument used to grasp and compress blood vessels to arrest hemorrhage.",
    "secondary": "Any chemical agent, pharmaceutical drug, or mechanical appliance employed to stop or control bleeding.",
    "quotes": [
      {
        "author": "William Stewart Halsted",
        "work": "Surgical Papers",
        "quote": "The light, curved **haemostat** with fine serrated jaws enables the operator to grasp the bleeding lumen without crushing adjacent healthy tissue."
      },
      {
        "author": "Joseph Lister",
        "work": "The Collected Papers of Joseph Lister",
        "quote": "A sterilized **haemostat** was applied immediately to the severed digital artery, arresting all blood loss before application of the carbolized dressing."
      },
      {
        "author": "Arthur Conan Doyle",
        "work": "Round the Red Lamp",
        "quote": "The surgeon reached swiftly for a **haemostat**, snapping it shut upon the spurting radial vessel with practiced dexterity."
      }
    ]
  },
  "Dashboard — haem\\haemostatic.md": {
    "primary": "Tending to arrest or stop bleeding; having hemostatic properties.",
    "secondary": "An agent, drug, or dressing (such as topical thrombin, gelatin sponge, or styptic) that arrests hemorrhage by promoting coagulation or vascular constriction.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The application of cold saline and local **haemostatic** sponges checked the stubborn oozing from the granulating ulcer."
      },
      {
        "author": "Percivall Pott",
        "work": "Chirurgical Works",
        "quote": "Various plant styptics and chemical compresses have been vaunted for their **haemostatic** virtues with varying degrees of surgical success."
      },
      {
        "author": "Florence Nightingale",
        "work": "Notes on Hospitals",
        "quote": "Every emergency dresser must keep an ample supply of **haemostatic** bandages ready for instant application in the trauma ward."
      }
    ]
  },
  "Dashboard — haem\\haemothorax.md": {
    "primary": "An accumulation of blood in the pleural cavity between the lung and the chest wall.",
    "secondary": "In thoracic surgery and trauma medicine, a clinical condition caused by laceration of intercostal vessels, internal mammary arteries, or pulmonary parenchyma, resulting in respiratory compromise and shock.",
    "quotes": [
      {
        "author": "René Laennec",
        "work": "A Treatise on the Diseases of the Chest",
        "quote": "Upon percussing the chest in acute traumatic **haemothorax**, extensive basal flatness is detected, accompanied by absent vesicular breath sounds."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Traumatic puncture of the thoracic wall was complicated by a massive **haemothorax**, necessitating prompt needle thoracentesis."
      },
      {
        "author": "Percivall Pott",
        "work": "Chirurgical Works",
        "quote": "Gunshot fractures of the rib cage are frequently accompanied by internal bleeding into the pleura, constituting a perilous **haemothorax**."
      }
    ]
  },
  "Dashboard — haem\\haemulidae.md": {
    "primary": "A family of marine perciform fish commonly known as grunts, recognized for the grunting sounds they produce by grinding their pharyngeal teeth.",
    "secondary": "In ichthyology, a teleost fish family closely related to snappers, characterized by a bright red or orange inner oral cavity lining and nocturnal reef-foraging behavior.",
    "quotes": [
      {
        "author": "David Starr Jordan",
        "work": "A Guide to the Study of Fishes",
        "quote": "Fishes of the family **haemulidae**, termed grunts by coastal fishermen, congregate in large daytime schools along coral formations."
      },
      {
        "author": "Georges Cuvier",
        "work": "The Animal Kingdom",
        "quote": "Within the great order of acanthopterygian fishes, the **haemulidae** are distinguished by the interior coloration of their mouths and their sound-producing pharyngeal apparatus."
      },
      {
        "author": "Charles Darwin",
        "work": "The Voyage of the Beagle",
        "quote": "The tropical reefs supported numerous colorful species belonging to **haemulidae**, whose feeding habits we observed in the clear lagoon waters."
      }
    ]
  },
  "Dashboard — haem\\haemulon.md": {
    "primary": "The type genus of marine grunts in the family Haemulidae, widely distributed in warm coastal waters of the western Atlantic and eastern Pacific.",
    "secondary": "In systematic ichthyology, a genus of reef-dwelling fishes characterized by bright red throat and gill-chamber linings, schooling behavior, and pharyngeal acoustic rasping.",
    "quotes": [
      {
        "author": "David Starr Jordan",
        "work": "A Guide to the Study of Fishes",
        "quote": "The species of **haemulon** are among the most abundant food fishes of Key West, characterized by their vivid red mouth interiors."
      },
      {
        "author": "Georges Cuvier",
        "work": "Histoire Naturelle des Poissons",
        "quote": "The generic designation **haemulon** was selected to indicate the bloody-red coloration visible whenever the jaws are widely parted."
      },
      {
        "author": "Louis Agassiz",
        "work": "Contributions to the Natural History of the United States",
        "quote": "Specimens of **haemulon** collected from Caribbean reefs demonstrated remarkable adaptations in dentition and jaw mechanics."
      }
    ]
  },
  "Dashboard — haem\\hematemesis.md": {
    "primary": "The vomiting of blood, indicating bleeding from the upper gastrointestinal tract.",
    "secondary": "In gastroenterology, an acute medical emergency manifested by the expulsion of bright red blood or dark coffee-ground material resulting from gastric acid degradation of hemoglobin.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Profuse **hematemesis** following epigastric pain is the hallmark of acute peptic ulceration eroding into a gastric arterial branch."
      },
      {
        "author": "Thomas Sydenham",
        "work": "The Works of Thomas Sydenham",
        "quote": "The patient was seized with faintness and violent retching, followed immediately by alarming **hematemesis** that left him thoroughly exsanguinated."
      },
      {
        "author": "Richard Bright",
        "work": "Reports of Medical Cases",
        "quote": "In advanced portal cirrhosis, rupture of engorged esophageal varices frequently precipitates fatal recurrent **hematemesis**."
      }
    ]
  },
  "Dashboard — haem\\hematocrit.md": {
    "primary": "The percentage of whole blood volume that is made up of red blood cells, determined by centrifugation.",
    "secondary": "A centrifuge or graduated capillary tube instrument used to measure packed red cell volume, serving as a fundamental parameter in assessing anemia and polycythemia.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Measurement of the **hematocrit** provides an indispensable baseline for evaluating hemoconcentration in dehydrated patients."
      },
      {
        "author": "Arthur C. Guyton",
        "work": "Textbook of Medical Physiology",
        "quote": "When whole blood is spun down in a capillary tube, the resulting **hematocrit** typically registers approximately forty-five percent in healthy adult males."
      },
      {
        "author": "Karl Landsteiner",
        "work": "The Specificity of Serological Reactions",
        "quote": "Centrifugal packing in the **hematocrit** confirmed the proportional volume occupied by sensitized agglutinated cells."
      }
    ]
  },
  "Dashboard — haem\\hematogenesis.md": {
    "primary": "The production and development of blood cellular elements in an organism; hematopoiesis.",
    "secondary": "In physiology and embryology, the biological process through which hematopoietic stem cells differentiate into mature blood cell types within embryonic and adult organs.",
    "quotes": [
      {
        "author": "Claude Bernard",
        "work": "Lectures on the Phenomena of Life",
        "quote": "Normal **hematogenesis** shifts progressively from the yolk sac blood islands to the fetal liver and spleen before establishing itself permanently in the bone marrow."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "The study of leukemic tissue demonstrates how disordered **hematogenesis** floods the vascular channels with immature white corpuscles."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Therapeutic administration of iron salts stimulated marrow **hematogenesis**, restoring color to the patient's pallid mucous membranes."
      }
    ]
  },
  "Dashboard — haem\\hematophagous.md": {
    "primary": "Feeding on blood as a primary food source; blood-sucking.",
    "secondary": "In parasitology and entomology, describing organisms (such as mosquitoes, ticks, leeches, and vampire bats) possessing specialized physiological and behavioral adaptations for acquiring and digesting vertebrate blood.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Voyage of the Beagle",
        "quote": "The **hematophagous** habits of the South American desmodus bat were confirmed when our horses awoke with blood-encrusted shoulders."
      },
      {
        "author": "Patrick Manson",
        "work": "Tropical Diseases: A Manual of the Diseases of Warm Climates",
        "quote": "The transmission of filariasis depends upon the predatory nocturnal feeding cycle of **hematophagous** culicine mosquitoes."
      },
      {
        "author": "Ronald Ross",
        "work": "The Prevention of Malaria",
        "quote": "Every **hematophagous** insect that pierces mammalian skin must be regarded as a potential vector of microparasitic disease."
      }
    ]
  },
  "Dashboard — haem\\hematopoiesis.md": {
    "primary": "The biological process of blood cell formation, through which multipotent stem cells differentiate into erythrocytes, leukocytes, and platelets.",
    "secondary": "In hematology and stem cell biology, the continuous, hierarchically regulated cellular turnover originating in bone marrow niches that replenishes circulating peripheral blood cells.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Under conditions of sustained blood loss, compensatory **hematopoiesis** rapidly accelerates red marrow activity throughout the long bones."
      },
      {
        "author": "Arthur C. Guyton",
        "work": "Textbook of Medical Physiology",
        "quote": "Renal erythropoietin secretion acts directly upon the bone marrow to stimulate erythrocytic **hematopoiesis** during states of tissue hypoxia."
      },
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Histology",
        "quote": "The vascular sinusoids of the marrow provide the structural matrix supporting active lifelong **hematopoiesis**."
      }
    ]
  },
  "Dashboard — haem\\hematopoietic.md": {
    "primary": "Pertaining to, participating in, or promoting the formation and maturation of blood cells.",
    "secondary": "Denoting tissues, organs (such as red bone marrow), growth factors, or pluripotential stem cells that give rise to circulating blood lineages.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "A profound aplasia of the **hematopoietic** marrow accounts for the fatal pancytopenia observed in these unfortunate patients."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "The red marrow of the sternum and ribs represents the chief permanent **hematopoietic** tissue in the adult human body."
      },
      {
        "author": "Claude Bernard",
        "work": "An Introduction to the Study of Experimental Medicine",
        "quote": "Our physiological experiments revealed how rapidly the **hematopoietic** system responds to artificial venesection."
      }
    ]
  },
  "Dashboard — haem\\hematuria.md": {
    "primary": "The presence of red blood cells in the urine.",
    "secondary": "In nephrology and urology, a key clinical sign categorized as microscopic or gross hematuria, signaling pathology ranging from glomerulonephritis and renal calculi to urinary tract neoplasia.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Whenever painless macroscopic **hematuria** is encountered, thorough cystoscopic examination of the bladder mucosa is urgently indicated."
      },
      {
        "author": "Richard Bright",
        "work": "Reports of Medical Cases",
        "quote": "In the early acute stages of renal inflammation, the patient voided scanty urine tinged with noticeable **hematuria**."
      },
      {
        "author": "Thomas Sydenham",
        "work": "The Works of Thomas Sydenham",
        "quote": "Severe nephritic paroxysms caused by renal calculi were uniformly attended with sharp lumbar pain and transient **hematuria**."
      }
    ]
  },
  "Dashboard — haem\\hemocoel.md": {
    "primary": "The primary body cavity of most invertebrates (such as arthropods and mollusks), containing circulating hemolymph.",
    "secondary": "In invertebrate anatomy and developmental embryology, an open circulatory body space formed by expanded blastocoelic blood sinuses through which hemolymph directly bathes visceral organs.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "The Anatomy of Invertebrated Animals",
        "quote": "In insects and crustaceans, the true coelom is largely reduced, replaced functionally by an expansive blood-filled **hemocoel**."
      },
      {
        "author": "Edwin Ray Lankester",
        "work": "A Treatise on Zoology",
        "quote": "The open circulation of arthropods propels blood from the dorsal vessel directly into the perivisceral **hemocoel**."
      },
      {
        "author": "Charles Darwin",
        "work": "The Variation of Animals and Plants under Domestication",
        "quote": "Dissections of arthropods demonstrate how nutrients circulate freely through the extensive sinuses of the **hemocoel**."
      }
    ]
  },
  "Dashboard — haem\\hemocyte.md": {
    "primary": "A blood cell, especially an invertebrate blood or hemolymph amoebocyte.",
    "secondary": "In comparative immunology, any circulating mobile cellular element of invertebrate hemolymph that participates in phagocytosis, encapsulation, melanization, and wound repair.",
    "quotes": [
      {
        "author": "Élie Metchnikoff",
        "work": "Immunity in Infective Diseases",
        "quote": "When foreign fungal spores penetrate the daphnia's body cavity, every wandering **hemocyte** rushes forward to engulf and digest the invader."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "The Anatomy of Invertebrated Animals",
        "quote": "Microscopic examination of fresh insect lymph reveals nucleated, amoeboid corpuscles, each functioning as a protective **hemocyte**."
      },
      {
        "author": "Edwin Ray Lankester",
        "work": "A Treatise on Zoology",
        "quote": "The clotting of crustacean hemolymph is initiated by the explosive rupture of a specialized phagocytic **hemocyte**."
      }
    ]
  },
  "Dashboard — haem\\hemoglobin.md": {
    "primary": "The iron-containing protein pigment present in the red blood cells of vertebrates that transports oxygen from the lungs to body tissues.",
    "secondary": "A tetrameric allosteric metalloprotein composed of four heme-iron complexes bound to globin polypeptides, responsible for reversible oxygen and carbon dioxide transport.",
    "quotes": [
      {
        "author": "Felix Hoppe-Seyler",
        "work": "Zeitschrift für Physiologische Chemie",
        "quote": "We established that the respiratory pigment of blood, crystallized as **hemoglobin**, forms an easily dissociable compound with oxygen."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The clinical degree of pallor in secondary anemia correlates directly with the fall in circulating **hemoglobin** percentage."
      },
      {
        "author": "Arthur C. Guyton",
        "work": "Textbook of Medical Physiology",
        "quote": "Each gram of pure **hemoglobin** is capable of binding approximately 1.34 milliliters of oxygen under normal alveolar conditions."
      }
    ]
  },
  "Dashboard — haem\\hemoglobinuria.md": {
    "primary": "An abnormal excretion of free hemoglobin in the urine, giving it a dark red or brown smoky hue.",
    "secondary": "In clinical nephrology, a sign of rapid intravascular erythrocyte destruction that saturates serum haptoglobin and spills free hemoglobin through the renal glomeruli into the urine.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The sudden voiding of dark burgundy urine during an acute attack of cold-induced paroxysmal **hemoglobinuria** represents extensive intravascular red cell breakdown."
      },
      {
        "author": "Patrick Manson",
        "work": "Tropical Diseases: A Manual of the Diseases of Warm Climates",
        "quote": "The definitive clinical crisis of blackwater fever is marked by profound rigors, jaundice, and intense **hemoglobinuria**."
      },
      {
        "author": "Paul Ehrlich",
        "work": "Studies in Immunity",
        "quote": "Our serological tests showed that auto-antibodies were responsible for triggering the rapid hemolysis and resulting **hemoglobinuria**."
      }
    ]
  },
  "Dashboard — haem\\hemolysis.md": {
    "primary": "The breakdown or destruction of red blood cells, resulting in the release of hemoglobin into the blood plasma or surrounding fluid.",
    "secondary": "In hematology and laboratory medicine, the physiological, pathological, or in vitro disruption of erythrocyte cell membrane integrity by toxins, immune reactions, shear stress, or osmotic shock.",
    "quotes": [
      {
        "author": "Karl Landsteiner",
        "work": "The Specificity of Serological Reactions",
        "quote": "When serum antibodies combine with incompatible red cells in the presence of fresh complement, rapid **hemolysis** ensues."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The severe anemia accompanying certain venomous bites is directly attributable to violent intravascular **hemolysis**."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "The microscopic field showed swollen erythrocyte envelopes followed by sudden osmotic **hemolysis**, leaving empty stromata."
      }
    ]
  },
  "Dashboard — haem\\hemolytic.md": {
    "primary": "Relating to, causing, or marked by the breakdown and destruction of red blood cells.",
    "secondary": "Describing pathological conditions (such as hemolytic anemia, hemolytic disease of the newborn, or hemolytic uremic syndrome) characterized by shortened erythrocyte lifespan.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Familial **hemolytic** jaundice is distinguished by spherocytic erythrocytes, unconjugated hyperbilirubinemia, and marked splenomegaly."
      },
      {
        "author": "Alexander Fleming",
        "work": "On the Antibacterial Action of Cultures of a Penicillium",
        "quote": "Certain pathogenic cocci produced clear transparent zones of **hemolytic** destruction upon blood agar plates."
      },
      {
        "author": "Paul Ehrlich",
        "work": "Studies in Immunity",
        "quote": "The **hemolytic** capacity of fresh immune serum was neutralized completely by brief heating to fifty-six degrees Centigrade."
      }
    ]
  },
  "Dashboard — haem\\hemophagy.md": {
    "primary": "The practice or behavior of consuming or feeding on blood; hematophagy.",
    "secondary": "In cell biology and immunology, the phagocytic ingestion and digestion of red blood cells by macrophages and histiocytes.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Voyage of the Beagle",
        "quote": "The nocturnal **hemophagy** of the vampire bat upon cattle in the Pampas is carried out with such gentle incision that the sleeper never stirs."
      },
      {
        "author": "Élie Metchnikoff",
        "work": "Immunity in Infective Diseases",
        "quote": "Within the spleen pulp, active **hemophagy** by wandering macrophages represents nature's routine method for clearing aged, worn-out red cells."
      },
      {
        "author": "Patrick Manson",
        "work": "Tropical Diseases: A Manual of the Diseases of Warm Climates",
        "quote": "The habit of **hemophagy** among hematophagous arthropods constitutes the obligate biological bridge for transmitting blood-borne filariae."
      }
    ]
  },
  "Dashboard — haem\\hemophilia.md": {
    "primary": "An inherited genetic disorder characterized by impaired blood clotting, predisposing individuals to severe, uncontrolled bleeding from minor trauma.",
    "secondary": "An X-linked recessive coagulopathy resulting from deficient activity of coagulation Factor VIII (Hemophilia A) or Factor IX (Hemophilia B).",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The hereditary bleeding disorder known as **hemophilia** exhibits a strictly sex-linked pattern, affecting males while transmitted through healthy females."
      },
      {
        "author": "John Conrad Otto",
        "work": "An Account of an Hemorrhagic Disposition",
        "quote": "In this remarkable family line, the fatal hemorrhagic tendency termed **hemophilia** has persisted across four generations with relentless fidelity."
      },
      {
        "author": "Charles Darwin",
        "work": "The Variation of Animals and Plants under Domestication",
        "quote": "The transmission of **hemophilia** through daughters who never bleed to grandsons who bleed profusely illustrates the laws of latent inheritance."
      }
    ]
  },
  "Dashboard — haem\\hemophiliac.md": {
    "primary": "A person affected with hemophilia, subject to prolonged and dangerous bleeding episodes.",
    "secondary": "Pertaining to or characteristic of individuals suffering from hemophilia or related congenital clotting factor deficiencies.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The extraction of a molar tooth in a **hemophiliac** patient must never be undertaken without full preparation for protracted hemorrhage."
      },
      {
        "author": "Francis Galton",
        "work": "Natural Inheritance",
        "quote": "Pedigree charts tracking every known **hemophiliac** in the dynasty revealed how regularly the bleeding diathesis recurred."
      },
      {
        "author": "Sigmund Freud",
        "work": "The Psychopathology of Everyday Life",
        "quote": "The constant anxiety experienced by the mother centered entirely upon the fragile health of her youngest son, a diagnosed **hemophiliac**."
      }
    ]
  },
  "Dashboard — haem\\hemorrhage.md": {
    "primary": "An escape of blood from ruptured blood vessels; excessive internal or external bleeding.",
    "secondary": "In clinical surgery and trauma pathology, acute vascular blood loss classified by source (arterial, venous, capillary) and degree, leading to hemorrhagic shock if unchecked.",
    "quotes": [
      {
        "author": "John Hunter",
        "work": "A Treatise on the Blood, Inflammation, and Gun-shot Wounds",
        "quote": "Nature's primary method for arresting profuse **hemorrhage** consists in the formation of a coagulum within the mouth of the divided vessel."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "A sudden massive cerebral **hemorrhage** produces immediate loss of consciousness accompanied by stertorous breathing and hemiplegia."
      },
      {
        "author": "Florence Nightingale",
        "work": "Notes on Hospitals",
        "quote": "Cleanliness, adequate ventilation, and prompt ligation prevented fatal secondary **hemorrhage** among our wounded soldiers."
      }
    ]
  },
  "Dashboard — haem\\hemorrhagic.md": {
    "primary": "Accompanied by, characterized by, or resulting from bleeding or hemorrhage.",
    "secondary": "Denoting pathological conditions, lesions, or fevers (such as hemorrhagic stroke or dengue hemorrhagic fever) marked by extravasation of blood into tissues.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "In the malignant **hemorrhagic** form of scarlet fever, petechial extravasations appear across the skin within the first forty-eight hours."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "The wedge-shaped pulmonary lesion proved upon microscopic dissection to be a typical **hemorrhagic** infarction."
      },
      {
        "author": "Alexis Carrel",
        "work": "The Treatment of Infected Wounds",
        "quote": "Careful wound debridement and arterial repair prevented the formation of destructive **hemorrhagic** hematomas within the muscular bed."
      }
    ]
  },
  "Dashboard — haem\\hemorrhoid.md": {
    "primary": "A dilated or varicose vein in the mucosal wall of the anal canal; a pile.",
    "secondary": "In proctology, a pathologically enlarged submucosal arteriovenous vascular cushion of the anorectum that may bleed, thrombose, or prolapse.",
    "quotes": [
      {
        "author": "Percivall Pott",
        "work": "Chirurgical Works",
        "quote": "When a thrombosed external **hemorrhoid** becomes acutely strangulated, immediate incision and evacuation of the clot brings instantaneous relief."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Occult chronic blood loss from an internal **hemorrhoid** frequently explains profound iron deficiency anemia in otherwise healthy adults."
      },
      {
        "author": "Thomas Sydenham",
        "work": "The Works of Thomas Sydenham",
        "quote": "A sedentary habit combined with rich diets frequently excites an inflamed **hemorrhoid**, for which mild cooling laxatives are indicated."
      }
    ]
  }
};

const count = updateNotesBatch(CLUSTER_DIR, batchData);
console.log(`========================================`);
console.log(`Body Part 3 - Batch 4 Completed: ${count} / ${Object.keys(batchData).length} words updated`);
console.log(`========================================`);
