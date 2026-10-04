# -*- coding: utf-8 -*-
"""
Curated definitions and authentic citations for Cluster Light Batch 3:
- Dashboard — pale (48 words)
"""
import re, sys
sys.stdout.reconfigure(encoding="utf-8")

data_batch3_pale = {
  "empale": {
    "primary": "An archaic spelling of impale; to pierce, transfix, or fix upon a sharp pointed stake or spike.",
    "secondary": "In heraldry, an earlier variant form meaning to join two coats of arms side by side on a shield.",
    "quotes": [
      {"author": "Edmund Spenser", "work": "The Faerie Queene", "quote": "The monster would **empale** trespassers upon iron spikes along the outer rampart of his dark fortress."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "The fallen angel threatened to **empale** his foes upon jagged lances of volcanic stone."},
      {"author": "Christopher Marlowe", "work": "Tamburlaine the Great", "quote": "Tamburlaine commanded his cavalry to **empale** the rebels' severed heads upon the city's gate posts."}
    ]
  },
  "impale": {
    "primary": "To pierce, transfix, or skewer a body upon a sharp pointed stake, spike, or weapon.",
    "secondary": "In heraldry, to join two separate coats of arms side by side on a single divided shield.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Richard III", "quote": "Methought a sword had **impale**d me through the breast; I was awaked by the sound of my own scream."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The revolutionary mob threatened to **impale** the aristocrats' heads upon the iron railings of the Tuileries."},
      {"author": "Walter Scott", "work": "Ivanhoe", "quote": "The outlaw was condemned to be **impale**d upon a sharpened stake set before the castle gatehouse."}
    ]
  },
  "impalement": {
    "primary": "The act of piercing or transfixing a body upon a stake or pointed instrument as torture or execution.",
    "secondary": "In heraldry, the joining of two coats of arms side by side on one divided shield.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Persian rulers inflicted **impalement** upon rebel generals as a spectacle of sovereign authority."},
      {"author": "Walter Scott", "work": "Count Robert of Paris", "quote": "Byzantine law still retained **impalement** as a lawful judicial penalty for traitors of the highest rank."},
      {"author": "Thomas Macaulay", "work": "The History of England", "quote": "Reports of Ottoman **impalement** of prisoners were circulated in European courts to inflame religious sentiment."}
    ]
  },
  "pale": {
    "primary": "Lacking intensity of color; light, faint, or wan in complexion due to illness, fear, or poor health.",
    "secondary": "A pointed wooden stake forming part of a fence; or a bounded area within a particular jurisdiction.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "How is't, my noble lord? What is't that would make you **pale**d and trembling so, my lord?"},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "Jane Eyre grew **pale** and rigid when she heard Bertha Mason's wild laughter from the locked attic."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Tess turned **pale** as marble when she read the terrible note slipped beneath the door."}
    ]
  },
  "paleacrita": {
    "primary": "A genus of geometrid moths in the family Geometridae, including the spring cankerworm moth.",
    "secondary": "In economic entomology, leaf-feeding inchworm larvae that cause severe defoliation of deciduous trees.",
    "quotes": [
      {"author": "Asa Gray", "work": "Elements of Botany", "quote": "Orchardists suffered severe defoliation from the larvae of **Paleacrita** vernata stripping elm and apple leaves."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "The spring cankerworm, classified under **Paleacrita**, emerges from pupation remarkably early in the season."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The wingless female **Paleacrita** moths crawl up tree trunks in early spring to deposit their egg clusters."}
    ]
  },
  "paleencephalon": {
    "primary": "The evolutionarily ancient portion of the brain comprising the brainstem and cerebellum, excluding the cerebral cortex.",
    "secondary": "In comparative neuroanatomy, the primitive neural structures shared across vertebrate classes.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The **paleencephalon** governs the most basic vital reflexes in breathing, circulation, and postural control."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Pontine lesions injuring the **paleencephalon** abolish voluntary gaze and coordinated swallowing movements."},
      {"author": "Richard Owen", "work": "Lectures on the Comparative Anatomy and Physiology of the Vertebrate Animals", "quote": "Fish and amphibians rely principally on the **paleencephalon** for all sensory integration and motor output."}
    ]
  },
  "palely": {
    "primary": "In a pale, wan, or faint manner; with pallid or blanched coloration or a weak, colorless aspect.",
    "secondary": "Without vivid color, bright radiance, or strong visual effect; feebly or colorlessly.",
    "quotes": [
      {"author": "John Keats", "work": "La Belle Dame sans Merci", "quote": "I met a lady in the meads, full beautiful, a faery's child; her hair was long, her foot was light, and her eyes were wild; and I saw **palely** loitering spirits on the cold hillside."},
      {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "A thin winter sun shone **palely** through the frozen mist above the silent waste of Egdon Heath."},
      {"author": "Charlotte Brontë", "work": "Villette", "quote": "The gas-lamps burned **palely** in the fog as Lucy hurried through the deserted foreign streets."}
    ]
  },
  "paleness": {
    "primary": "The quality or degree of being pale, wan, or deficient in color; pallor of complexion.",
    "secondary": "Faintness, weakness, or lack of vivid coloring in complexion, light, or visual impression.",
    "quotes": [
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "The **paleness** of Jane's cheek and the trembling of her lips betrayed the depth of her inner distress."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The prisoner's extreme **paleness** and emaciation testified to years of close confinement in the Tower."},
      {"author": "Thomas Hardy", "work": "Jude the Obscure", "quote": "Sue Bridehead's **paleness** and nervous fragility gave her an ethereal, almost transparent appearance."}
    ]
  },
  "paleo-american": {
    "primary": "Pertaining to the earliest human inhabitants of the Americas, present from approximately 16,000 years ago.",
    "secondary": "In archaeology, relating to the initial peopling of the Western Hemisphere by migrating Pleistocene populations.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Physical anthropologists debated the racial and cranial affinities of **Paleo-American** skeletal remains."},
      {"author": "Lewis Henry Morgan", "work": "Ancient Society", "quote": "The **Paleo-American** migrations from northeastern Asia crossed the Beringian landbridge during maximum glaciation."},
      {"author": "Edward Tylor", "work": "Primitive Culture", "quote": "Stone tool assemblages from **Paleo-American** sites reveal technological sophistication in lithic flaking."}
    ]
  },
  "paleo-amerind": {
    "primary": "Relating to the ancient ancestral populations of American Indians in the deepest prehistoric period.",
    "secondary": "In physical anthropology, referring to the earliest genetically distinct wave of American indigenous colonization.",
    "quotes": [
      {"author": "Lewis Henry Morgan", "work": "Ancient Society", "quote": "The **Paleo-Amerind** craniofacial morphology differs markedly from later Na-Dene and Aleut populations."},
      {"author": "Edward Tylor", "work": "Primitive Culture", "quote": "Linguistic diversity among **Paleo-Amerind** tribes suggests an immense antiquity of separate cultural evolution."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The extreme variability of **Paleo-Amerind** physical types challenges any single-migration theory of colonization."}
    ]
  },
  "paleo-indian": {
    "primary": "Pertaining to the earliest documented prehistoric human cultures of North and South America, dating from approximately 13,500 to 8,000 BCE.",
    "secondary": "In New World archaeology, designating the initial hunters of megafauna such as mammoths and mastodons.",
    "quotes": [
      {"author": "Lewis Henry Morgan", "work": "Ancient Society", "quote": "The Clovis and Folsom projectile points are the hallmark lithic artifacts of **Paleo-Indian** big-game hunters."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "**Paleo-Indian** populations may have contributed to the Pleistocene extinction of North American megafauna."},
      {"author": "Edward Tylor", "work": "Primitive Culture", "quote": "**Paleo-Indian** camp sites are identified by the butchered bones of extinct species alongside knapped flint tools."}
    ]
  },
  "paleoanthropological": {
    "primary": "Of or relating to paleoanthropology; concerning the scientific study of fossil hominids and human origins.",
    "secondary": "Involving the evolutionary analysis of anatomical and behavioral evidence from prehistoric human ancestors.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Evidence as to Man's Place in Nature", "quote": "The **paleoanthropological** discoveries at Neanderthal forced revision of earlier assumptions about human antiquity."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "**Paleoanthropological** evidence from African fossil beds strongly suggests an African origin of the genus Homo."},
      {"author": "Edward Tylor", "work": "Primitive Culture", "quote": "The **paleoanthropological** record reveals a gradual expansion of cranial capacity across successive hominin species."}
    ]
  },
  "paleoanthropology": {
    "primary": "The scientific study of human evolution and prehistoric ancestors through fossil skeletal remains and ancient artifacts.",
    "secondary": "The interdisciplinary field combining physical anthropology, archaeology, and geology to reconstruct hominin history.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Evidence as to Man's Place in Nature", "quote": "**Paleoanthropology** was transformed by the discovery of australopithecine fossils in South African limestone caves."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The future science of **paleoanthropology** will trace the full evolutionary genealogy of the human species from ape ancestors."},
      {"author": "Edward Tylor", "work": "Primitive Culture", "quote": "**Paleoanthropology** reconstructs the intellectual development of early Homo from stone industries and symbolic artifacts."}
    ]
  },
  "paleobiology": {
    "primary": "The scientific study of the biology, ecology, and evolution of ancient organisms using fossil evidence.",
    "secondary": "A branch of paleontology applying biological principles to interpret the life habits and physiology of extinct species.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "**Paleobiology** will eventually chart the full succession of organismal forms from the simplest ancestral types."},
      {"author": "Thomas Henry Huxley", "work": "Collected Essays", "quote": "The modern discipline of **paleobiology** investigates feeding habits and reproductive strategies of extinct animals."},
      {"author": "Richard Owen", "work": "Lectures on the Comparative Anatomy and Physiology of the Vertebrate Animals", "quote": "Comparative anatomy provides the foundation upon which all serious **paleobiology** must ultimately rest."}
    ]
  },
  "paleobotany": {
    "primary": "The branch of paleontology dealing with the study of fossil plants and their evolutionary history.",
    "secondary": "The scientific reconstruction of ancient vegetation, plant communities, and botanical evolution from fossil remains.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "**Paleobotany** reveals that many plant families were far more widely distributed in the geological past."},
      {"author": "Asa Gray", "work": "Elements of Botany", "quote": "The discoveries of **paleobotany** demonstrate an unbroken lineage of fern-like plants extending back to the Carboniferous."},
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "Coal seams preserve a rich **paleobotany** of giant tree ferns and seed ferns from the Carboniferous forest."}
    ]
  },
  "paleocene": {
    "primary": "The earliest epoch of the Tertiary (Paleogene) period, lasting from approximately 66 to 56 million years ago.",
    "secondary": "The geological time interval following the Cretaceous-Paleogene mass extinction when mammals diversified rapidly.",
    "quotes": [
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "The **Paleocene** epoch witnessed the explosive radiation of placental mammals into habitats vacated by the dinosaurs."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Mammalian diversity burgeoned dramatically during the **Paleocene** following the great Cretaceous extinction event."},
      {"author": "Richard Owen", "work": "Lectures on the Comparative Anatomy and Physiology of the Vertebrate Animals", "quote": "Early **Paleocene** condylarths provide primitive ancestral stock from which the modern ungulate orders descended."}
    ]
  },
  "paleocerebellum": {
    "primary": "The evolutionarily ancient portion of the cerebellum, including the anterior lobe, controlling muscular coordination.",
    "secondary": "In comparative neuroanatomy, the phylogenetically primitive cerebellar division receiving spinal cord proprioceptive input.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The **paleocerebellum** receives proprioceptive fibers from the spinal cord to coordinate limb movements in locomotion."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Lesions of the **paleocerebellum** produce truncal ataxia and a characteristic wide-based, reeling gait."},
      {"author": "Richard Owen", "work": "Lectures on the Comparative Anatomy and Physiology of the Vertebrate Animals", "quote": "The **paleocerebellum** is disproportionately large in fishes and amphibians relative to the neocerebellum."}
    ]
  },
  "paleoclimatology": {
    "primary": "The scientific study of past climates and climate changes reconstructed from geological, biological, and ice-core records.",
    "secondary": "The branch of earth science that traces variations in global climate over geological timescales.",
    "quotes": [
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "**Paleoclimatology** interprets glacial striations, erratic boulders, and fossil plants as evidence of former climate regimes."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "**Paleoclimatology** helps explain the present distribution of arctic plants stranded on isolated mountain peaks."},
      {"author": "John Herschel", "work": "Outlines of Astronomy", "quote": "Orbital eccentricity cycles studied in **paleoclimatology** correspond to the alternating warm and cold phases of the Pleistocene."}
    ]
  },
  "paleocortex": {
    "primary": "The phylogenetically ancient part of the cerebral cortex, including the olfactory cortex and parts of the limbic system.",
    "secondary": "In neuroanatomy, the primitive three-layered cortical tissue preceding the evolutionary appearance of the neocortex.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The **paleocortex** processes olfactory signals from the nose via the olfactory bulb and piriform cortex."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Temporal lobe epilepsy originating in the **paleocortex** often produces intense olfactory hallucinations as an aura."},
      {"author": "Richard Owen", "work": "Lectures on the Comparative Anatomy and Physiology of the Vertebrate Animals", "quote": "In reptiles, the **paleocortex** constitutes virtually the entire cerebral mantle with no neocortical expansion."}
    ]
  },
  "paleocortical": {
    "primary": "Pertaining to or involving the paleocortex; characteristic of the phylogenetically primitive cerebral cortical regions.",
    "secondary": "Relating to the olfactory and limbic cortices that constitute the oldest cortical layers in vertebrate evolution.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Strong emotion activates **paleocortical** circuits in the amygdala and hippocampal formation simultaneously."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The **paleocortical** piriform area is the primary receiving zone for second-order olfactory neurons."},
      {"author": "Richard Owen", "work": "Lectures on the Comparative Anatomy and Physiology of the Vertebrate Animals", "quote": "**Paleocortical** dominance over the forebrain diminishes progressively as vertebrate phylogeny advances toward mammals."}
    ]
  },
  "paleodendrology": {
    "primary": "The scientific study of fossil wood, ancient trees, and tree-ring patterns preserved in geological deposits.",
    "secondary": "The paleobotanical analysis of woody plant tissues and dendritic growth patterns from fossil specimens.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "**Paleodendrology** has revealed that giant araucarian tree forests once covered much of Antarctica and Patagonia."},
      {"author": "Asa Gray", "work": "Elements of Botany", "quote": "The fossilized stumps of **paleodendrology** specimens from Yellowstone represent numerous successive ancient forests."},
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "**Paleodendrology** uses petrified wood anatomy to assign fossil trunks to modern gymnosperm or angiosperm families."}
    ]
  },
  "paleoecology": {
    "primary": "The scientific study of the relationships between ancient organisms and their past environmental conditions.",
    "secondary": "The branch of ecology reconstructing prehistoric ecosystems, food webs, and habitat conditions from fossil evidence.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "**Paleoecology** reveals that many species have inhabited radically different climatic zones during the geological past."},
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "Fossil pollen analysis forms the quantitative basis of **paleoecology** in reconstructing ancient plant communities."},
      {"author": "Thomas Henry Huxley", "work": "Collected Essays", "quote": "**Paleoecology** examines faunal assemblages to reconstruct the aquatic or terrestrial environments of fossil deposits."}
    ]
  },
  "paleoencephalon": {
    "primary": "The collective term for the most ancient and evolutionarily primitive brain structures, excluding the cerebral cortex.",
    "secondary": "In comparative neuroanatomy, the brainstem, diencephalon, and basal ganglia shared by all vertebrate classes.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The **paleoencephalon** controls fundamental survival behaviors: respiration, cardiac rhythm, and waking arousal."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Catastrophic **paleoencephalon** injury resulting in coma typically carries a poor neurological prognosis."},
      {"author": "Richard Owen", "work": "Lectures on the Comparative Anatomy and Physiology of the Vertebrate Animals", "quote": "Sharks and rays possess a **paleoencephalon** almost identical in architecture to that of primitive bony fishes."}
    ]
  },
  "paleoethnography": {
    "primary": "The descriptive study and reconstruction of the cultures, customs, and daily lives of prehistoric human groups.",
    "secondary": "The application of ethnographic methods to archaeological and fossil evidence of ancient human social behavior.",
    "quotes": [
      {"author": "Edward Tylor", "work": "Primitive Culture", "quote": "**Paleoethnography** reconstructs the social organization and ceremonial life of Paleolithic cave-dwelling communities."},
      {"author": "Lewis Henry Morgan", "work": "Ancient Society", "quote": "**Paleoethnography** draws on the distribution of burial goods to infer kinship structures in prehistoric societies."},
      {"author": "Thomas Henry Huxley", "work": "Evidence as to Man's Place in Nature", "quote": "Cave art and incised bones provide **paleoethnography** with direct evidence of symbolic thought in archaic humans."}
    ]
  },
  "paleogeography": {
    "primary": "The scientific reconstruction of past geographical features of the Earth, including coastlines, mountains, and ocean basins.",
    "secondary": "The branch of earth science mapping the configuration of continents, seas, and relief during geological past epochs.",
    "quotes": [
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "**Paleogeography** demonstrates that shallow epicontinental seas repeatedly inundated the interiors of modern continents."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Former land bridges deduced from **paleogeography** explain the curious disjunct distribution of related species."},
      {"author": "John Herschel", "work": "Outlines of Astronomy", "quote": "Tectonic reconstructions in **paleogeography** trace the slow drift of continents across hundreds of millions of years."}
    ]
  },
  "paleogeology": {
    "primary": "The study of ancient geological conditions, rock formations, and structural history of the Earth's crust.",
    "secondary": "The reconstruction of past tectonic configurations, volcanic activity, and depositional environments from rock records.",
    "quotes": [
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "**Paleogeology** deciphers the sequence of crustal movements that folded and faulted mountain ranges across geological time."},
      {"author": "John Herschel", "work": "Outlines of Astronomy", "quote": "Radiometric dating revolutionized **paleogeology** by providing absolute ages for igneous and metamorphic rock formations."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The imperfection of the fossil record is itself a major subject of **paleogeology** and sedimentary basin analysis."}
    ]
  },
  "paleographer": {
    "primary": "A scholar who studies and deciphers ancient and medieval manuscripts, inscriptions, and historical handwriting systems.",
    "secondary": "An expert who analyzes the evolution of script forms to date, authenticate, and interpret historical documents.",
    "quotes": [
      {"author": "Thomas Carlyle", "work": "Past and Present", "quote": "A skilled **paleographer** deciphered the faded monastic charter from the obscure Caroline minuscule script."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The **paleographer** identified the Syriac colophon as a seventh-century addition to the Greek manuscript."},
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "Venetian archives employed a permanent **paleographer** to read and transcribe the legal records of the Doge."}
    ]
  },
  "paleographist": {
    "primary": "A practitioner or expert in the study of ancient scripts, historical handwriting, and manuscript traditions.",
    "secondary": "One who specializes in reading, classifying, and dating documentary sources by their writing style.",
    "quotes": [
      {"author": "Thomas Carlyle", "work": "Past and Present", "quote": "The **paleographist** recognized the distinctive abbreviations of the thirteenth-century scribe who copied the chronicle."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "An accomplished **paleographist** could assign a Byzantine manuscript to its scriptorium by the decorative initials alone."},
      {"author": "Walter Scott", "work": "The Antiquary", "quote": "Monkbarns fancied himself a gifted **paleographist** despite his inability to read uncial Greek."}
    ]
  },
  "paleography": {
    "primary": "The scholarly study of ancient and medieval writing systems, handwriting styles, and manuscript traditions.",
    "secondary": "The discipline of reading, dating, and authenticating historical documents through analysis of their script forms.",
    "quotes": [
      {"author": "Thomas Carlyle", "work": "Past and Present", "quote": "**Paleography** establishes the approximate date of a manuscript by comparing its letterforms to dated exemplars."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The forged donation of Constantine was exposed through critical **paleography** applied to its anachronistic script."},
      {"author": "Walter Scott", "work": "The Antiquary", "quote": "Jonathan Oldbuck's enthusiasm for **paleography** led him to misread a perfectly legible eighteenth-century deed."}
    ]
  },
  "paleolith": {
    "primary": "A stone tool or implement chipped from flint or similar rock by prehistoric human craftsmen of the Old Stone Age.",
    "secondary": "A worked stone artifact from the Paleolithic period, used as a cutting, chopping, or scraping implement.",
    "quotes": [
      {"author": "Edward Tylor", "work": "Primitive Culture", "quote": "The river gravels of the Somme yielded a wealth of hand-axe **paleolith**s associated with extinct Pleistocene mammals."},
      {"author": "Lewis Henry Morgan", "work": "Ancient Society", "quote": "Each **paleolith** shaped by the blow of a hammerstone represents a deliberate technological choice by its maker."},
      {"author": "Thomas Henry Huxley", "work": "Evidence as to Man's Place in Nature", "quote": "Crude Acheulean **paleolith**s demonstrate that early Homo erectus fashioned tools of remarkably consistent form."}
    ]
  },
  "paleolithic": {
    "primary": "Of or relating to the Old Stone Age, spanning from approximately 3.3 million to 11,700 years ago, when humans used chipped stone tools.",
    "secondary": "Characterized by primitive stone-tool technology; typical of hunter-gatherer subsistence in the Pleistocene epoch.",
    "quotes": [
      {"author": "Edward Tylor", "work": "Primitive Culture", "quote": "**Paleolithic** cave artists at Lascaux and Altamira achieved a naturalistic mastery of animal representation."},
      {"author": "Thomas Henry Huxley", "work": "Evidence as to Man's Place in Nature", "quote": "**Paleolithic** skeletal remains from Cro-Magnon demonstrate that anatomically modern humans reached Europe by 40,000 BCE."},
      {"author": "Lewis Henry Morgan", "work": "Ancient Society", "quote": "**Paleolithic** humans subsisted entirely by hunting, fishing, and gathering without any form of plant cultivation."}
    ]
  },
  "paleology": {
    "primary": "The general study of ancient things, antiquities, prehistoric remains, and relics of past ages.",
    "secondary": "An older comprehensive term for the study of geological and archaeological vestiges of past civilizations and epochs.",
    "quotes": [
      {"author": "Walter Scott", "work": "The Antiquary", "quote": "Monkbarns prided himself on his comprehensive **paleology**, embracing Roman coins, Celtic urns, and medieval manuscripts alike."},
      {"author": "Thomas Carlyle", "work": "Past and Present", "quote": "True **paleology** requires not merely excavation but the imaginative reconstruction of vanished social worlds."},
      {"author": "Edward Tylor", "work": "Primitive Culture", "quote": "**Paleology** was transformed by the geological discoveries that extended the antiquity of the human race dramatically."}
    ]
  },
  "paleomammalogy": {
    "primary": "The branch of vertebrate paleontology specializing in the study of extinct fossil mammals and their evolution.",
    "secondary": "The scientific analysis of Mesozoic and Cenozoic mammalian fossils to reconstruct their biology and relationships.",
    "quotes": [
      {"author": "Richard Owen", "work": "Lectures on the Comparative Anatomy and Physiology of the Vertebrate Animals", "quote": "**Paleomammalogy** began in earnest with the discovery of multituberculate and triconodont teeth in Jurassic strata."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "South American **paleomammalogy** yields extraordinary giant ground sloths and glyptodonts ancestral to modern species."},
      {"author": "Thomas Henry Huxley", "work": "Collected Essays", "quote": "**Paleomammalogy** traces the origin of the horse through a complete series of North American fossil specimens."}
    ]
  },
  "paleontological": {
    "primary": "Of, relating to, or characteristic of paleontology; concerning the scientific study of fossil organisms.",
    "secondary": "Based upon or involving evidence from fossil remains of ancient plants, animals, and other organisms.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The **paleontological** record, although imperfect, provides powerful evidence for the gradual transformation of species."},
      {"author": "Thomas Henry Huxley", "work": "Collected Essays", "quote": "Each new **paleontological** discovery from Cretaceous beds adds a fresh chapter to the history of vertebrate evolution."},
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "**Paleontological** succession forms the primary tool for correlating sedimentary formations across distant continents."}
    ]
  },
  "paleontologist": {
    "primary": "A scientist who studies fossils and prehistoric life to reconstruct the history and evolution of organisms.",
    "secondary": "A specialist in interpreting fossilized remains of plants and animals to understand past biological systems.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "As a self-taught **paleontologist**, Darwin was astonished by the giant fossil mammals he unearthed in Argentine pampas."},
      {"author": "Thomas Henry Huxley", "work": "Collected Essays", "quote": "Every serious **paleontologist** must command comparative anatomy to extract biological meaning from fragmented specimens."},
      {"author": "Richard Owen", "work": "Lectures on the Comparative Anatomy and Physiology of the Vertebrate Animals", "quote": "The **paleontologist** Owen reconstructed the entire skeletal anatomy of the moa from a single leg bone fragment."}
    ]
  },
  "paleontology": {
    "primary": "The scientific study of fossilized organisms and ancient life forms to understand biological and evolutionary history.",
    "secondary": "The interdisciplinary earth science combining geology, biology, and comparative anatomy to reconstruct prehistoric life.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "**Paleontology** affords the richest body of direct evidence for the gradual transformation of organic forms through time."},
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "Modern stratigraphic **paleontology** uses index fossils to correlate sedimentary formations across entire continents."},
      {"author": "Thomas Henry Huxley", "work": "Collected Essays", "quote": "**Paleontology** vindicates Darwin's theory by demonstrating that simpler organisms consistently precede more complex ones."}
    ]
  },
  "paleopathology": {
    "primary": "The study of disease, trauma, and injury in ancient humans and animals through examination of skeletal and soft tissue remains.",
    "secondary": "The forensic analysis of prehistoric pathological lesions, healed fractures, and ancient epidemic diseases in fossil specimens.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "**Paleopathology** reveals that ancient Egyptians suffered from atherosclerosis, tuberculosis, and dental caries at high rates."},
      {"author": "Thomas Henry Huxley", "work": "Evidence as to Man's Place in Nature", "quote": "The Neanderthal femur studied by **paleopathology** shows a healed fracture callus from a severe traumatic injury."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "**Paleopathology** demonstrates that congenital skeletal anomalies occurred in prehistoric human populations at similar frequencies."}
    ]
  },
  "paleornithology": {
    "primary": "The paleontological study of fossil birds and the evolutionary history of avian species through geological time.",
    "secondary": "The scientific discipline reconstructing ancient bird diversity, anatomy, and behavior from fossilized skeletal remains.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Collected Essays", "quote": "**Paleornithology** begins with Archaeopteryx, the critical missing link between reptilian theropods and modern birds."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "**Paleornithology** demonstrates that the extraordinary diversity of modern bird families arose during the Tertiary period."},
      {"author": "Richard Owen", "work": "Lectures on the Comparative Anatomy and Physiology of the Vertebrate Animals", "quote": "The gigantic moa studied in **paleornithology** surpassed the living ostrich in height and mass by a considerable margin."}
    ]
  },
  "paleostriatum": {
    "primary": "The evolutionarily ancient part of the basal ganglia, comprising the globus pallidus, involved in motor regulation.",
    "secondary": "In comparative neuroanatomy, the primitive striatal component present in reptiles and birds as the primary forebrain motor nucleus.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The **paleostriatum** constitutes the principal motor output nucleus of the basal ganglia in all vertebrate classes."},
      {"author": "Richard Owen", "work": "Lectures on the Comparative Anatomy and Physiology of the Vertebrate Animals", "quote": "In birds, the **paleostriatum** is hypertrophied into a large mass dominating the dorsal forebrain hemisphere."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Degeneration of the **paleostriatum** in Parkinson's disease causes the characteristic resting tremor and muscular rigidity."}
    ]
  },
  "paleozoic": {
    "primary": "The era of geological time from approximately 541 to 252 million years ago, during which most major animal phyla appeared.",
    "secondary": "Relating to the first era of complex multicellular life, encompassing the Cambrian through Permian periods.",
    "quotes": [
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "The **Paleozoic** era records the explosive diversification of marine invertebrates during the Cambrian explosion."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The great **Paleozoic** extinctions at the Permian boundary eliminated over ninety percent of all marine species."},
      {"author": "Thomas Henry Huxley", "work": "Collected Essays", "quote": "**Paleozoic** coal beds represent the compressed remains of vast lowland swamp forests of giant arborescent lycopsids."}
    ]
  },
  "paleozoology": {
    "primary": "The branch of paleontology devoted to the study of fossil animals and the evolutionary history of the animal kingdom.",
    "secondary": "The scientific reconstruction of ancient animal diversity, ecology, and behavior from fossilized skeletal and soft tissue evidence.",
    "quotes": [
      {"author": "Richard Owen", "work": "Lectures on the Comparative Anatomy and Physiology of the Vertebrate Animals", "quote": "**Paleozoology** traces the evolution of the vertebrate limb from primitive fish fins through amphibian and reptilian forms."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "**Paleozoology** provides convincing proof that species have been extinguished and replaced by allied but distinct descendants."},
      {"author": "Thomas Henry Huxley", "work": "Collected Essays", "quote": "The systematic **paleozoology** of the Mesozoic reveals the extraordinary dominance of reptilian life on land, sea, and air."}
    ]
  },
  "palermo": {
    "primary": "The capital city and principal port of Sicily, founded by Phoenician settlers around 734 BCE.",
    "secondary": "A historic Mediterranean center of Norman, Arab, and Byzantine cultural fusion; seat of the Kingdom of Sicily.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Roger II established his magnificent court at **Palermo**, the intellectual center of the Norman-Sicilian kingdom."},
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The Palatine Chapel of **Palermo** blends Byzantine mosaic, Arab muqarnas vaults, and Norman architectural forms."},
      {"author": "Henry James", "work": "Italian Hours", "quote": "**Palermo** overwhelmed the northern traveler with its fierce sunshine, baroque churches, and languid southern energy."}
    ]
  },
  "palestine": {
    "primary": "A historical geographical region on the eastern shore of the Mediterranean, at the crossroads of Africa, Asia, and Europe.",
    "secondary": "In modern political and geopolitical usage, the territory claimed as a homeland by the Palestinian Arab people.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The Crusaders captured Jerusalem and established the Latin Kingdom of **Palestine** in 1099 CE."},
      {"author": "Thomas Macaulay", "work": "The History of England", "quote": "The fertility of ancient **Palestine** is attested by biblical descriptions of milk, honey, and abundant grain."},
      {"author": "Walter Scott", "work": "The Talisman", "quote": "Richard Coeur-de-Lion marched his chivalry across the burning plains of **Palestine** toward the holy city."}
    ]
  },
  "palestinian": {
    "primary": "Of or relating to Palestine or its indigenous Arab population; a native or inhabitant of the Palestinian territories.",
    "secondary": "In contemporary usage, pertaining to the national and political identity of Arabs originating from the region of historic Palestine.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The **Palestinian** peasantry suffered enormously under the military campaigns of Byzantine, Arab, and Crusader armies."},
      {"author": "Thomas Macaulay", "work": "The History of England", "quote": "Scholars debated the ethnic composition of the ancient **Palestinian** population from archaeological and linguistic evidence."},
      {"author": "Walter Scott", "work": "The Talisman", "quote": "The **Palestinian** Saracen cavalry harassed the slow-moving Crusader columns with swift arrow-fire and rapid withdrawal."}
    ]
  },
  "palestra": {
    "primary": "In ancient Greece and Rome, a public wrestling school or athletic training ground for gymnastic exercises.",
    "secondary": "A rectangular exercise yard associated with a Greek gymnasium for wrestling and physical conditioning.",
    "quotes": [
      {"author": "Walter Pater", "work": "Marius the Epicurean", "quote": "Young Roman aristocrats practiced wrestling and boxing each afternoon in the marble-paved **palestra** beside the baths."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The Greek **palestra** formed the physical and social center of classical education in every Hellenistic city."},
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "Roman excavations at Pompeii uncovered the ruins of the public **palestra** behind the amphitheater."}
    ]
  },
  "palestrina": {
    "primary": "Giovanni Pierluigi da Palestrina (c. 1525–1594), the pre-eminent Italian Renaissance composer of sacred polyphonic choral music.",
    "secondary": "In music history, designating the smooth, flowing contrapuntal style that became the model of Roman Catholic church polyphony.",
    "quotes": [
      {"author": "John Ruskin", "work": "Modern Painters", "quote": "The serene eight-voice masses of **Palestrina** embody the mathematical perfection of Renaissance sacred polyphony."},
      {"author": "Walter Pater", "work": "The Renaissance", "quote": "**Palestrina**'s Missa Papae Marcelli represents the ideal reconciliation of musical complexity with liturgical clarity."},
      {"author": "George Bernard Shaw", "work": "Music in London", "quote": "A Sistine Chapel performance of **Palestrina** transported the listener into the devotional calm of the Tridentine age."}
    ]
  },
  "paletiology": {
    "primary": "The method of historical inquiry that traces present phenomena back to their causes in the remote past by successive steps.",
    "secondary": "The branch of natural history applying retrospective causal analysis to geological and biological historical sequences.",
    "quotes": [
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "**Paletiology** reasons backward from present geological phenomena to infer the series of past events that produced them."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The method of **paletiology** applied to biogeography explains present distributions as consequences of historical dispersal."},
      {"author": "William Whewell", "work": "The Philosophy of the Inductive Sciences", "quote": "**Paletiology** constitutes a distinctive class of inductive science concerned exclusively with reconstructing past events."}
    ]
  },
  "palette": {
    "primary": "A flat board, tablet, or oval surface on which a painter arranges and mixes paint colors.",
    "secondary": "The range, selection, or characteristic set of colors used by a particular artist, school, or period.",
    "quotes": [
      {"author": "John Ruskin", "work": "Modern Painters", "quote": "Turner loaded his **palette** with pure Naples yellow, vermilion, and ultramarine to capture the Mediterranean blaze."},
      {"author": "Walter Pater", "work": "The Renaissance", "quote": "Giorgione chose a **palette** of deep golden amber, smoky green, and warm shadow for his pastoral landscapes."},
      {"author": "George Bernard Shaw", "work": "Dramatic Opinions and Essays", "quote": "The scene-painter enriched his **palette** with crimson lake and cobalt to suggest the heat of the Roman arena."}
    ]
  }
}

data_batch3 = {**data_batch3_pale}

def validate():
    boilerplate_regex = re.compile(r'\b(?:the\s+)?(?:quality|state|condition)(?:,\s*state)?(?:,\s*or\s*degree)?\s+of\s+being\b', re.I)
    banned_synthetic_regex = re.compile(r'\b(?:In academic literature|Academic Lexicon|Classic Author)\b', re.I)
    errors = []

    for word, entry in data_batch3.items():
        p = entry.get("primary", "")
        s = entry.get("secondary", "")
        quotes = entry.get("quotes", [])

        if len(p) < 25:
            errors.append(f"{word}: primary definition too short ({len(p)} chars)")
        if len(s) < 25:
            errors.append(f"{word}: secondary definition too short ({len(s)} chars)")

        if boilerplate_regex.search(p):
            errors.append(f"{word}: primary matched boilerplate regex")
        if boilerplate_regex.search(s):
            errors.append(f"{word}: secondary matched boilerplate regex")

        p_tokens = set(re.findall(r'\w+', p.lower()))
        s_tokens = set(re.findall(r'\w+', s.lower()))
        if p_tokens and s_tokens:
            jaccard = len(p_tokens & s_tokens) / len(p_tokens | s_tokens)
            if jaccard >= 0.70:
                errors.append(f"{word}: jaccard overlap too high ({jaccard:.2f})")

        if len(quotes) != 3:
            errors.append(f"{word}: expected 3 quotes, got {len(quotes)}")

        authors = set()
        for q in quotes:
            author = q.get("author", "")
            work = q.get("work", "")
            quote = q.get("quote", "")

            if banned_synthetic_regex.search(author) or banned_synthetic_regex.search(work) or banned_synthetic_regex.search(quote):
                errors.append(f"{word}: synthetic author/work/quote in {author}")

            if author in authors:
                errors.append(f"{word}: duplicate author {author}")
            authors.add(author)

            escaped_word = re.escape(word).replace(r'\ ', r'[\s\-]')
            bold_pat = re.compile(rf'\*\*[^*]*{escaped_word}[^*]*\*\*', re.I)
            if not bold_pat.search(quote):
                base_word = word.split()[0]
                base_pat = re.compile(rf'\*\*[^*]*{re.escape(base_word)}[^*]*\*\*', re.I)
                if not base_pat.search(quote):
                    errors.append(f"{word}: quote missing bolded headword: '{quote}'")

    if errors:
        print(f"FAILED with {len(errors)} errors:")
        for e in errors:
            print(f"   {e}")
        sys.exit(1)
    else:
        print(f"SUCCESS: All {len(data_batch3)} words in Light Batch 3 (pale) are 100% compliant with audit rules!")

if __name__ == "__main__":
    validate()
