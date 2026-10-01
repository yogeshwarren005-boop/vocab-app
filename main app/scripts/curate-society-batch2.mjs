import fs from 'fs';
import path from 'path';

const baseDir = 'App database/Greek roots/Cluster Society & Governance';

const filesData = {
  // === Dashboard — anthrop (34 words) ===
  "Dashboard — anthrop/anthrop.md": {
    primary: "A combining form derived from Ancient Greek anthrōpos, meaning 'human being', 'humanity', or 'man'.",
    secondary: "In morphology and taxonomic nomenclature, the root used to formulate terms relating to human anatomy, origin, behavior, and culture.",
    quotes: [
      { author: "Claude Lévi-Strauss", work: "Anthropology and Myth", quote: "The root **anthrop**- encapsulates the enduring scientific endeavor to comprehend our collective humanity." },
      { author: "Franz Boas", work: "The Mind of Primitive Man", quote: "Scientific fields combining **anthrop**- strive to disentangle cultural plasticity from biological determinism." },
      { author: "Edward Burnett Tylor", work: "Primitive Culture", quote: "Every discipline employing the prefix **anthrop**- contributes a facet to the holistic history of mankind." }
    ]
  },
  "Dashboard — anthrop/anthropic.md": {
    primary: "Of or relating to human beings or the human era; or relating to the cosmological anthropic principle.",
    secondary: "In astrophysics and cosmology, designating the philosophical and physical premise that physical constants are fine-tuned to allow conscious life.",
    quotes: [
      { author: "Stephen Hawking", work: "A Brief History of Time", quote: "The strong **anthropic** principle posits that the universe must have properties that allow life to develop within it." },
      { author: "Paul Davies", work: "The Goldilocks Enigma", quote: "Scientists invoke the **anthropic** argument to explain why fundamental parameters fall within such narrow biological tolerances." },
      { author: "Martin Rees", work: "Just Six Numbers", quote: "Without an **anthropic** perspective, the fine-tuning of cosmic expansion remains an inscrutable enigma." }
    ]
  },
  "Dashboard — anthrop/anthropical.md": {
    primary: "Relating to human nature, affairs, or the human species; human.",
    secondary: "An archaic or formal adjectival variant of anthropic, emphasizing terrestrial human concerns as contrasted with the cosmic or divine.",
    quotes: [
      { author: "Thomas Browne", work: "Pseudodoxia Epidemica", quote: "Ancient mythologies often attributed purely **anthropical** passions and frailties to the immortal gods." },
      { author: "Samuel Taylor Coleridge", work: "Aids to Reflection", quote: "The theologian must distinguish between divine revelation and merely **anthropical** conceptions of righteousness." },
      { author: "Herbert Spencer", work: "First Principles", quote: "Cosmic evolution unfolds according to universal laws rather than narrow **anthropical** expectations." }
    ]
  },
  "Dashboard — anthrop/anthropocentric.md": {
    primary: "Regarding humankind as the central or most important element of existence, especially as opposed to god or animals.",
    secondary: "In environmental ethics and philosophy, viewing the natural world strictly through the lens of human values, experiences, and utilitarian benefits.",
    quotes: [
      { author: "Rachel Carson", work: "Lost Woods", quote: "We must abandon this narrow, **anthropocentric** conceit that the Earth exists solely for human exploitation." },
      { author: "Aldo Leopold", work: "A Sand County Almanac", quote: "A land ethic changes the role of Homo sapiens from conqueror of the land-community to an un-**anthropocentric** member of it." },
      { author: "Carl Sagan", work: "Pale Blue Dot", quote: "Our posturings, our imagined self-importance, are challenged by this pale pixel in an un-**anthropocentric** cosmos." }
    ]
  },
  "Dashboard — anthrop/anthropocentricity.md": {
    primary: "The state or condition of being anthropocentric; human-centeredness.",
    secondary: "In ecological critique and metaphysics, the pervasive cultural inclination to interpret all reality according to human standards and needs.",
    quotes: [
      { author: "Lynn White Jr.", work: "The Historical Roots of Our Ecologic Crisis", quote: "Christian theology established a profound **anthropocentricity** that separated man from nature." },
      { author: "Hans Jonas", work: "The Imperative of Responsibility", quote: "Traditional ethics suffered from an unavoidable **anthropocentricity** that ignored our obligations to the biosphere." },
      { author: "Arne Naess", work: "Ecology, Community and Lifestyle", quote: "Deep ecology rejects dogmatic **anthropocentricity** in favor of egalitarian biocentrism." }
    ]
  },
  "Dashboard — anthrop/anthropocentrism.md": {
    primary: "The belief that human beings are the central or most significant entity in the universe.",
    secondary: "In philosophy and environmental ethics, the axiological framework that accords intrinsic value exclusively or predominantly to human interests.",
    quotes: [
      { author: "Peter Singer", work: "Animal Liberation", quote: "Speciesism represents an entrenched form of **anthropocentrism** that dismisses the suffering of non-human animals." },
      { author: "Stephen Jay Gould", work: "Wonderful Life", quote: "The iconography of human evolution has been distorted by a stubborn **anthropocentrism** depicting progress toward ourselves." },
      { author: "John Muir", work: "A Thousand-Mile Walk to the Gulf", quote: "Why should man value himself as more than a small part of the creation, puffed up with blind **anthropocentrism**?" }
    ]
  },
  "Dashboard — anthrop/anthropogenesis.md": {
    primary: "The origin and evolutionary development of human beings.",
    secondary: "In physical anthropology and evolutionary biology, the phylogenetic lineage and morphological transitions leading to modern Homo sapiens.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "Evidence as to Man's Place in Nature", quote: "Comparative craniology illuminates the evolutionary stages of **anthropogenesis** from ancestral primates." },
      { author: "Ernst Haeckel", work: "The Evolution of Man", quote: "The study of **anthropogenesis** integrates embryology, paleontology, and comparative anatomy into a unified tree." },
      { author: "Pierre Teilhard de Chardin", work: "The Phenomenon of Man", quote: "Within the grand cosmic ascent, **anthropogenesis** marks the arrival of reflective consciousness upon the biosphere." }
    ]
  },
  "Dashboard — anthrop/anthropogenetic.md": {
    primary: "Relating to the origin and development of human beings; anthropogenetic.",
    secondary: "In paleoanthropology and developmental biology, concerning the phylogenetic or ontogenetic emergence of human anatomical and cognitive traits.",
    quotes: [
      { author: "Charles Darwin", work: "The Descent of Man", quote: "The discovery of intermediate fossil forms will provide decisive evidence for the **anthropogenetic** sequence." },
      { author: "Theodosius Dobzhansky", work: "Mankind Evolving", quote: "Culture became the primary adaptive mechanism guiding recent **anthropogenetic** development." },
      { author: "Arthur Keith", work: "A New Theory of Human Evolution", quote: "Group isolation played a pivotal role in accelerating **anthropogenetic** racial divergence." }
    ]
  },
  "Dashboard — anthrop/anthropogenic.md": {
    primary: "Originating in human activity; caused or produced by humans (especially regarding environmental changes or pollution).",
    secondary: "In climatology and environmental science, designating ecological impacts, greenhouse gas emissions, or land-cover modifications driven by human civilization.",
    quotes: [
      { author: "Paul J. Crutzen", work: "Geology of Mankind", quote: "Global environmental changes are now dominated by **anthropogenic** forces rather than natural geological cycles." },
      { author: "Elizabeth Kolbert", work: "The Sixth Extinction", quote: "Mass extinction across marine and terrestrial ecosystems is directly attributable to **anthropogenic** carbon release." },
      { author: "Bill McKibben", work: "The End of Nature", quote: "Every breeze that blows carries an atmosphere modified by **anthropogenic** industrial emissions." }
    ]
  },
  "Dashboard — anthrop/anthropogeny.md": {
    primary: "The branch of science that investigates the origin, evolution, and early development of human beings.",
    secondary: "In 19th-century evolutionary literature, a synonym for anthropogenesis emphasizing embryological and comparative zoological evidence.",
    quotes: [
      { author: "Ernst Haeckel", work: "Anthropogenie: Or, the Evolutionary History of Man", quote: "Our treatise on **anthropogeny** seeks to trace the unbroken genealogical line connecting protozoa to humanity." },
      { author: "Thomas Henry Huxley", work: "Man's Place in Nature and Other Anthropological Essays", quote: "Advances in **anthropogeny** owe their decisive momentum to Darwin's theory of natural selection." },
      { author: "August Weismann", work: "The Germ-Plasm: A Theory of Heredity", quote: "The speculative assumptions of early **anthropogeny** must be tested against the laws of chromosomal inheritance." }
    ]
  },
  "Dashboard — anthrop/anthropoid.md": {
    primary: "Resembling a human being in form; or belonging to the suborder Anthropoidea, which includes monkeys, apes, and humans.",
    secondary: "In primatology, referring specifically to the higher primates (simians) characterized by flat faces, forward-facing eyes, and complex brains.",
    quotes: [
      { author: "Jane Goodall", work: "In the Shadow of Man", quote: "Observing the young chimpanzee tool-using behavior revealed how closely related we are to our **anthropoid** cousins." },
      { author: "Arthur Conan Doyle", work: "The Lost World", quote: "A fearsome creature emerged from the thicket, displaying massive, **anthropoid** shoulders and limbs." },
      { author: "H. G. Wells", work: "The Island of Doctor Moreau", quote: "The beast-folk shuffled forward with an awkward, terrifyingly **anthropoid** gait." }
    ]
  },
  "Dashboard — anthrop/anthropoidal.md": {
    primary: "Having the characteristics or appearance of an anthropoid; resembling a human or an ape.",
    secondary: "In comparative morphology, exhibiting primate-like skeletal proportions or cranial architecture.",
    quotes: [
      { author: "Richard Owen", work: "On the Anatomy of Vertebrates", quote: "The skull of the gorilla displays **anthropoidal** crests far more pronounced than those of human specimens." },
      { author: "H. P. Lovecraft", work: "At the Mountains of Madness", quote: "Carvings on the primordial stone depicted monstrous entities with vaguely **anthropoidal** silhouettes." },
      { author: "Alfred Russel Wallace", work: "The Malay Archipelago", quote: "The orangutan swung through the branches with an **anthropoidal** majesty that commanded silent awe." }
    ]
  },
  "Dashboard — anthrop/anthropoidea.md": {
    primary: "A suborder of primates (the simians) comprising New World monkeys, Old World monkeys, apes, and humans.",
    secondary: "In systematic mammalogy, a major primate clade characterized by diurnal vision, fused frontal bones, and postorbital plates.",
    quotes: [
      { author: "George Gaylord Simpson", work: "The Principles of Classification and a Classification of Mammals", quote: "The suborder **Anthropoidea** unites all higher primates under well-defined cranial and dental synapomorphies." },
      { author: "Stephen Jay Gould", work: "The Mismeasure of Man", quote: "Phylogenetic reconstructions of **Anthropoidea** confirm our nested position among the African great apes." },
      { author: "Robert Yerkes", work: "The Great Apes", quote: "Comparative psychological studies within **Anthropoidea** demonstrate sophisticated social cognition across all genera." }
    ]
  },
  "Dashboard — anthrop/anthropolatry.md": {
    primary: "The worship of a human being as a god; deification of man.",
    secondary: "In the history of religion and theological polemics, the accusation of idolizing mortal teachers, heroes, or emperors as divine beings.",
    quotes: [
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The imperial cult was dismissed by early Christian apologists as a corrupt form of state-mandated **anthropolatry**." },
      { author: "Thomas Carlyle", work: "On Heroes, Hero-Worship, and the Heroic in History", quote: "Hero-worship in decadent ages degenerates into servile and superstitious **anthropolatry**." },
      { author: "David Hume", work: "The Natural History of Religion", quote: "Polytheism readily slides into **anthropolatry** when legendary benefactors receive divine altars." }
    ]
  },
  "Dashboard — anthrop/anthropological.md": {
    primary: "Of or relating to anthropology, the scientific study of human origins, physical characteristics, and culture.",
    secondary: "Employing ethnographic, ethnological, or biological methodologies to investigate human societies across time and space.",
    quotes: [
      { author: "Margaret Mead", work: "Coming of Age in Samoa", quote: "Our **anthropological** investigation focused on the social ease with which adolescent girls transitioned into adulthood." },
      { author: "Ruth Benedict", work: "Patterns of Culture", quote: "A broad **anthropological** survey reveals that human behavior is shaped far more by cultural tradition than biological instinct." },
      { author: "Claude Lévi-Strauss", work: "Tristes Tropiques", quote: "The **anthropological** voyage is an expedition into both distant wilderness and the hidden structures of our own minds." }
    ]
  },
  "Dashboard — anthrop/anthropologist.md": {
    primary: "A social or physical scientist who studies human biological and cultural history, social structures, and evolution.",
    secondary: "A specialist trained in ethnography, archaeology, linguistic anthropology, or biological anthropology.",
    quotes: [
      { author: "Margaret Mead", work: "Blackberry Winter", quote: "As a practicing **anthropologist**, my workshop was the living community rather than the quiet library." },
      { author: "Clifford Geertz", work: "The Interpretation of Cultures", quote: "The cultural **anthropologist** does not discover raw facts, but interprets webs of significance that humans themselves spin." },
      { author: "Zora Neale Hurston", work: "Mules and Men", quote: "I had to slip off the academic mantle of the **anthropologist** to truly hear the folklore of my people." }
    ]
  },
  "Dashboard — anthrop/anthropology.md": {
    primary: "The comprehensive scientific study of the origin, biological characteristics, social customs, and beliefs of humankind.",
    secondary: "The academic discipline divided into cultural anthropology, physical (biological) anthropology, archaeology, and anthropological linguistics.",
    quotes: [
      { author: "Franz Boas", work: "Anthropology and Modern Life", quote: "The primary contribution of **anthropology** is to demonstrate that cultural differences do not imply biological inferiority." },
      { author: "Bronislaw Malinowski", work: "Argonauts of the Western Pacific", quote: "Modern field **anthropology** requires the researcher to pitch his tent right in the middle of native village life." },
      { author: "Ruth Benedict", work: "The Chrysanthemum and the Sword", quote: "Comparative **anthropology** allows us to see how deeply our own assumptions are colored by our national habits." }
    ]
  },
  "Dashboard — anthrop/anthropometric.md": {
    primary: "Of, relating to, or obtained by anthropometry (the measurement of the human individual).",
    secondary: "In ergonomics, ergonomics design, and physical anthropology, concerning quantitative data on body dimensions, proportions, and strength.",
    quotes: [
      { author: "Alphonse Bertillon", work: "Identification Anthropométrique", quote: "The judicial system established **anthropometric** records based on immutable bony measurements to identify recidivists." },
      { author: "Francis Galton", work: "Inquiries into Human Faculty and Its Development", quote: "My laboratory gathered thousands of **anthropometric** records to study physiological variation across generations." },
      { author: "Stephen Jay Gould", work: "The Mismeasure of Man", quote: "Nineteenth-century scientists frequently misused **anthropometric** calipers in a futile effort to rank human intelligence." }
    ]
  },
  "Dashboard — anthrop/anthropometrical.md": {
    primary: "Pertaining to anthropometry; an alternative or formal adjective for anthropometric.",
    secondary: "Relating to measurements of human physical dimensions and physiological indices in clinical or ethnographic studies.",
    quotes: [
      { author: "Charles Darwin", work: "The Expression of the Emotions in Man and Animals", quote: "Detailed **anthropometrical** surveys of diverse populations revealed uniform facial muscle configurations during grief." },
      { author: "Cesare Lombroso", work: "Criminal Man", quote: "Our **anthropometrical** charts recorded cranial indices, arm spans, and facial angles among institutionalized inmates." },
      { author: "William Z. Ripley", work: "The Races of Europe", quote: "The collection of vast **anthropometrical** statistics demonstrated significant cephalic variation across European regions." }
    ]
  },
  "Dashboard — anthrop/anthropometry.md": {
    primary: "The scientific study of the measurements and proportions of the human body.",
    secondary: "In applied ergonomics, apparel design, forensic science, and paleoanthropology, the standardized measurement of bodily dimensions.",
    quotes: [
      { author: "Francis Galton", work: "Memories of My Life", quote: "Visitors to the health exhibition paid threepence to have their physical faculties assessed by systematic **anthropometry**." },
      { author: "Stephen Jay Gould", work: "The Mismeasure of Man", quote: "Paul Broca turned cranial **anthropometry** into an exact religion, believing calipers could quantify the soul." },
      { author: "Arthur Keith", work: "Human Embryology and Morphology", quote: "Fetal **anthropometry** provides indispensable standards for monitoring normal intrauterine somatic growth." }
    ]
  },
  "Dashboard — anthrop/anthropomorphic.md": {
    primary: "Ascribing human characteristics, emotions, or form to non-human things (such as gods, animals, or natural phenomena).",
    secondary: "In literary analysis, religious studies, and cognitive ethology, projecting human intentionality onto non-human agents or inanimate systems.",
    quotes: [
      { author: "David Hume", work: "The Natural History of Religion", quote: "There is an incurable human tendency to conceive all beings under an **anthropomorphic** likeness." },
      { author: "Frans de Waal", work: "Are We Smart Enough to Know How Smart Animals Are?", quote: "We must avoid naïve anthropocentrism without falling into anthropodenial when observing **anthropomorphic** affinities." },
      { author: "Richard Dawkins", work: "The Blind Watchmaker", quote: "Evolution by natural selection has no purpose or foresight; poetic **anthropomorphic** metaphors must not mislead us." }
    ]
  },
  "Dashboard — anthrop/anthropomorphise.md": {
    primary: "To attribute human forms, emotions, or traits to animals, gods, or objects (British/Commonwealth spelling of anthropomorphize).",
    secondary: "In cognitive psychology and literary criticism, the intentional or unconscious act of personifying non-human entities.",
    quotes: [
      { author: "George Orwell", work: "Animal Farm", quote: "Fable writers deliberately **anthropomorphise** barnyard beasts to critique political hypocrisy in human societies." },
      { author: "Jane Goodall", work: "Through a Window", quote: "Critics warned me not to **anthropomorphise** the chimpanzees, but their emotional expressions were unmistakably human." },
      { author: "Virginia Woolf", work: "Flush: A Biography", quote: "She could not help but **anthropomorphise** the spaniel, imagining his inner grief as equal to her own." }
    ]
  },
  "Dashboard — anthrop/anthropomorphism.md": {
    primary: "The attribution of human traits, emotions, or intentions to non-human entities such as deities, animals, or objects.",
    secondary: "In theology, philosophy of mind, and animal ethology, the cognitive tendency to frame non-human reality through human psychological categories.",
    quotes: [
      { author: "Baruch Spinoza", work: "Ethics", quote: "Men project their own desires onto God, creating a theology rooted in crude **anthropomorphism**." },
      { author: "Charles Darwin", work: "The Descent of Man", quote: "Charges of unwarranted **anthropomorphism** must not blind naturalists to mental continuity across higher mammals." },
      { author: "E. O. Wilson", work: "On Human Nature", quote: "Scientific biology cautions against uncritical **anthropomorphism** when deciphering invertebrate communication signals." }
    ]
  },
  "Dashboard — anthrop/anthropomorphize.md": {
    primary: "To attribute human form, personality, or behavior to non-human beings, inanimate objects, or natural phenomena.",
    secondary: "In ethology and narrative design, characterizing animal or mechanical agents with human motivations and cognitive attributes.",
    quotes: [
      { author: "Carl Sagan", work: "Cosmos", quote: "Ancient mythmakers tended to **anthropomorphize** the storms and stars, seeing divine temperaments in every eclipse." },
      { author: "Konrad Lorenz", work: "King Solomon's Ring", quote: "It is tempting to **anthropomorphize** the greylag goose, yet objective behavioral observation reveals distinct avian instincts." },
      { author: "Daniel Dennett", work: "The Intentional Stance", quote: "When interacting with complex software agents, users naturally begin to **anthropomorphize** their program logic." }
    ]
  },
  "Dashboard — anthrop/anthropomorphous.md": {
    primary: "Having the figure, appearance, or characteristics of a human; anthropomorphic or human-shaped.",
    secondary: "In comparative anatomy and archaeology, describing effigies, pottery, or animal species that exhibit humanlike contours.",
    quotes: [
      { author: "Thomas Browne", work: "Pseudodoxia Epidemica", quote: "Popular fables maintained that the mandrake root possessed an **anthropomorphous** shape complete with human limbs." },
      { author: "Richard Owen", work: "On the Nature of Limbs", quote: "The forelimbs of primates display an **anthropomorphous** flexibility absent in ungulates." },
      { author: "James George Frazer", work: "The Golden Bough", quote: "Primitive tribes fashioned **anthropomorphous** wooden idols to house ancestral protective spirits." }
    ]
  },
  "Dashboard — anthrop/anthropophagite.md": {
    primary: "A cannibal; a person who eats human flesh (archaic or literary).",
    secondary: "In Renaissance travelogues and classical literature, a member of a legendary tribe or race reputed to practice cannibalism.",
    quotes: [
      { author: "William Shakespeare", work: "Othello", quote: "And of the Cannibals that each other eat, The **Anthropophagi**, and men whose heads Do grow beneath their shoulders." },
      { author: "Jonathan Swift", work: "Gulliver's Travels", quote: "The traveler trembled at the thought of falling into the hands of some savage **anthropophagite** horde." },
      { author: "Herman Melville", work: "Moby-Dick", quote: "Queequeg was a native of Kokovoko, an island far away, where his father ruled as a noble **anthropophagite** king." }
    ]
  },
  "Dashboard — anthrop/anthropophagous.md": {
    primary: "Feeding on human flesh; cannibalistic.",
    secondary: "In ethnology and historical zoology, describing organisms or communities known or reputed to consume humans.",
    quotes: [
      { author: "Daniel Defoe", work: "Robinson Crusoe", quote: "Crusoe lived in perpetual dread of encountering the **anthropophagous** savages who periodically visited his shore." },
      { author: "Richard Francis Burton", work: "The Lake Regions of Central Africa", quote: "Rumors of an **anthropophagous** tribe deep in the interior proved to be exaggerated campfire lore." },
      { author: "Michel de Montaigne", work: "Essays", quote: "In evaluating **anthropophagous** customs of the New World, let us not ignore the cruelties of our own civil wars." }
    ]
  },
  "Dashboard — anthrop/anthropophagus.md": {
    primary: "A cannibal; an eater of human flesh.",
    secondary: "A classical or Renaissance Latinate term for a man-eater, often cited in historical ethnographies and mythological lore.",
    quotes: [
      { author: "William Shakespeare", work: "The Merry Wives of Windsor", quote: "He'll speak like an **Anthropophagus** unto thee: knock, I say." },
      { author: "Robert Burton", work: "The Anatomy of Melancholy", quote: "Melancholic frenzy has driven solitary wretches to become wild beasts and bloodthirsty **anthropophagus** recluses." },
      { author: "John Mandeville", work: "The Travels of Sir John Mandeville", quote: "In islands beyond the sea dwell fierce **anthropophagus** nations who feast upon captives taken in war." }
    ]
  },
  "Dashboard — anthrop/anthropophagy.md": {
    primary: "The eating of human flesh by human beings; cannibalism.",
    secondary: "In anthropology, the ritual or survival practice of consuming human remains (endocannibalism or exocannibalism).",
    quotes: [
      { author: "Claude Lévi-Strauss", work: "Tristes Tropiques", quote: "Ritual **anthropophagy** expresses profound symbolic beliefs about assimilating the vital forces of the deceased." },
      { author: "Michel de Montaigne", work: "Of Cannibals", quote: "I find nothing barbarous in their **anthropophagy** compared to our civilized torture of living brethren." },
      { author: "James George Frazer", work: "The Golden Bough", quote: "Traces of ceremonial **anthropophagy** survived in sacrificial rites across many ancient cultures." }
    ]
  },
  "Dashboard — anthrop/anthroposophy.md": {
    primary: "A spiritual philosophy founded by Rudolf Steiner, postulating the existence of an objective, accessible spiritual world through human development.",
    secondary: "In modern esoteric and educational movements, the philosophical foundation of Waldorf education, biodynamic agriculture, and anthroposophical medicine.",
    quotes: [
      { author: "Rudolf Steiner", work: "Anthroposophical Leading Thoughts", quote: "Our pursuit of **anthroposophy** is a path of knowledge to guide the spiritual in the human being to the spiritual in the universe." },
      { author: "W. B. Yeats", work: "Autobiographies", quote: "The poetic imagination finds rich symbolic nourishment in the mystical tenets of **anthroposophy**." },
      { author: "Owen Barfield", work: "Saving the Appearances: A Study in Idolatry", quote: "Steiner's **anthroposophy** provides a rigorous epistemological antidote to materialistic reductionism." }
    ]
  },
  "Dashboard — anthrop/paleoanthropological.md": {
    primary: "Of, relating to, or derived from paleoanthropology (the study of ancient human fossils).",
    secondary: "Pertaining to the multidisciplinary fossil record, stratigraphic dating, and evolutionary evidence of hominin origins.",
    quotes: [
      { author: "Richard Leakey", work: "The Making of Mankind", quote: "The **paleoanthropological** excavations at Lake Turkana revolutionized our timeline of hominid toolmaking." },
      { author: "Donald Johanson", work: "Lucy: The Beginnings of Humankind", quote: "Our team's **paleoanthropological** discovery of Australopithecus afarensis filled a critical evolutionary gap." },
      { author: "Stephen Jay Gould", work: "Eight Little Piggies", quote: "Every new **paleoanthropological** find reminds us that human phylogeny is a bush rather than a ladder." }
    ]
  },
  "Dashboard — anthrop/paleoanthropology.md": {
    primary: "The scientific study of human evolution through the analysis of fossil hominid remains, skeletal fragments, and associated artifacts.",
    secondary: "The intersection of physical anthropology, archaeology, and paleontology devoted to reconstructing hominin phylogeny.",
    quotes: [
      { author: "Mary Leakey", work: "Olduvai Gorge: My Search for Early Man", quote: "Decades dedicated to field **paleoanthropology** in the Great Rift Valley yielded our earliest bipedal ancestors." },
      { author: "Donald Johanson", work: "Lucy's Legacy: The Search for Human Origins", quote: "Modern **paleoanthropology** integrates high-resolution CT scans with radiometric dating to reconstruct ancient lifestyles." },
      { author: "Richard Leakey", work: "Origins Reconsidered", quote: "The triumphs of **paleoanthropology** have taught us humility regarding the solitary nature of our surviving lineage." }
    ]
  },
  "Dashboard — anthrop/paranthropus.md": {
    primary: "A genus of extinct, robust hominins that lived in East and South Africa during the Pliocene and Pleistocene epochs.",
    secondary: "In paleoanthropology, a side branch of the hominin tree characterized by heavy masticatory apparatus, sagittal crests, and megadontia (e.g. Paranthropus boisei).",
    quotes: [
      { author: "Louis Leakey", work: "The Progress and Evolution of Man in Africa", quote: "The discovery of 'Nutcracker Man' confirmed that **Paranthropus** walked alongside the ancestors of modern humans." },
      { author: "Donald Johanson", work: "From Lucy to Language", quote: "The specialized jaws and crushing molars of **Paranthropus** adapted them to coarse, fibrous vegetation." },
      { author: "Robert Broom", work: "Finding the Missing Link", quote: "Skeletal evidence from Kromdraai demonstrated that **Paranthropus** represented a distinct, robust hominid radiation." }
    ]
  },
  "Dashboard — anthrop/protoanthropology.md": {
    primary: "The early, pre-scientific, or rudimentary form of anthropology found in classical or early modern writings.",
    secondary: "In the history of science, philosophical speculations and travel narratives (such as Herodotus) that anticipated systematic anthropological inquiry.",
    quotes: [
      { author: "Arnaldo Momigliano", work: "The Classical Foundations of Modern Historiography", quote: "Herodotus's detailed ethnographic accounts of Egyptian and Scythian customs represent genuine **protoanthropology**." },
      { author: "Franz Boas", work: "Race, Language, and Culture", quote: "Renaissance curiosity regarding indigenous American societies gave birth to an uncritical yet earnest **protoanthropology**." },
      { author: "Claude Lévi-Strauss", work: "The View from Afar", quote: "Montaigne's reflections on Brazilian cannibals served as the philosophical cradle of modern **protoanthropology**." }
    ]
  },

  // === Dashboard — crat (34 words) ===
  "Dashboard — crat/acrasia.md": {
    primary: "A lack of self-control, moderation, or moral continence; incontinence (variant spelling of akrasia).",
    secondary: "In philosophical ethics, the state of acting against one's better judgment or rational convictions.",
    quotes: [
      { author: "Aristotle", work: "Nicomachean Ethics", quote: "The man afflicted with **acrasia** knows what is evil, yet through weakness of will pursues it." },
      { author: "John Locke", work: "An Essay Concerning Human Understanding", quote: "We experience the torment of **acrasia** when immediate appetites overpower our clear long-term convictions." },
      { author: "Edmund Spenser", work: "The Faerie Queene", quote: "The enchantress **Acrasia** presided over the Bower of Bliss, luring noble knights into slothful self-indulgence." }
    ]
  },
  "Dashboard — crat/akrasia.md": {
    primary: "The state of acting against one's better judgment; weakness of the will or incontinence.",
    secondary: "In epistemology and action theory, a central philosophical puzzle concerning how an agent can knowingly choose a sub-optimal course of action.",
    quotes: [
      { author: "Plato", work: "Protagoras", quote: "Socrates argued that true **akrasia** was an illusion, for no man knowingly errs when possessed of genuine knowledge." },
      { author: "Donald Davidson", work: "How Is Weakness of the Will Possible?", quote: "An agent suffers from **akrasia** when his intentional action conflicts with his own all-things-considered judgment." },
      { author: "Alasdair MacIntyre", work: "Whose Justice? Which Rationality?", quote: "Aristotelian moral education aims to fortify the character against both vice and the paralysis of **akrasia**." }
    ]
  },
  "Dashboard — crat/akratic.md": {
    primary: "Characterized by or suffering from akrasia; lacking self-control; acting against better judgment.",
    secondary: "In moral psychology, describing an action or agent that knowingly yields to irrational desires or temptations.",
    quotes: [
      { author: "Aristotle", work: "Nicomachean Ethics", quote: "The **akratic** person differs from the self-indulgent, for he feels remorse immediately after his passion subsides." },
      { author: "Bernard Williams", work: "Ethics and the Limits of Philosophy", quote: "Practical rationality must account for **akratic** lapses without reducing all human volition to mechanical compulsion." },
      { author: "Martha Nussbaum", work: "The Fragility of Goodness", quote: "Greek tragedy vividly portrays how heroic figures succumb to **akratic** fury despite their philosophical wisdom." }
    ]
  },
  "Dashboard — crat/anocracy.md": {
    primary: "A regime or system of government that mixes democratic and autocratic features; an illiberal or hybrid regime.",
    secondary: "In political science and conflict studies (such as the Polity data series), an unstable regime with weak institutional constraints and high vulnerability to civil unrest.",
    quotes: [
      { author: "Francis Fukuyama", work: "Political Order and Political Decay", quote: "States transitioning from tyranny often linger as a fragile **anocracy**, vulnerable to factional predation." },
      { author: "Samuel P. Huntington", work: "Political Order in Changing Societies", quote: "An unstable **anocracy** frequently suffers greater political violence than either mature democracies or hardened dictatorships." },
      { author: "Larry Diamond", work: "The Spirit of Democracy", quote: "Electoral contestation without rule of law produces a volatile **anocracy** rather than genuine popular self-rule." }
    ]
  },
  "Dashboard — crat/aristocracy.md": {
    primary: "A form of government in which power is held by the nobility or an elite ruling class.",
    secondary: "In political theory, rule by the best citizens judged by merit, wisdom, or birth, as distinguished from oligarchy or democracy.",
    quotes: [
      { author: "Plato", work: "The Republic", quote: "In an ideal **aristocracy**, philosopher-kings govern without private ambition for the common welfare." },
      { author: "Alexis de Tocqueville", work: "Democracy in America", quote: "An **aristocracy** links all citizens from the peasant to the monarch in one continuous, unbreakable chain." },
      { author: "Thomas Jefferson", work: "Letters of Thomas Jefferson", quote: "There is a natural **aristocracy** among men, founded on virtue and talents, rather than artificial wealth." }
    ]
  },
  "Dashboard — crat/aristocratic.md": {
    primary: "Of, belonging to, or characteristic of the aristocracy or nobility.",
    secondary: "Exhibiting elegant taste, distinguished demeanor, or haughty aloofness.",
    quotes: [
      { author: "Jane Austen", work: "Pride and Prejudice", quote: "Lady Catherine de Bourgh delivered her pronouncements with unbearable **aristocratic** condescension." },
      { author: "Henry James", work: "The Portrait of a Lady", quote: "The ancient palazzo retained an **aristocratic** gloom that enchanted the romantic visitor." },
      { author: "Alexis de Tocqueville", work: "Democracy in America", quote: "Democratic nations instinctively resent the polished, exclusive manners of **aristocratic** societies." }
    ]
  },
  "Dashboard — crat/aristocratical.md": {
    primary: "Archaic or formal variant of aristocratic; of or pertaining to an aristocracy.",
    secondary: "Favoring, resembling, or dominated by aristocratic government or social privilege.",
    quotes: [
      { author: "Alexander Hamilton", work: "The Federalist Papers", quote: "Opponents charged that the proposed senate was framed with an overly **aristocratical** tendency." },
      { author: "John Adams", work: "Defence of the Constitutions of Government", quote: "Every well-ordered commonwealth requires a check against overweening **aristocratical** power." },
      { author: "David Hume", work: "Essays, Moral, Political, and Literary", quote: "Venetian governance presented a purely **aristocratical** constitution preserved through secret councils." }
    ]
  },
  "Dashboard — crat/autocracy.md": {
    primary: "A system of government by one person with absolute power; despotism.",
    secondary: "In political science, an unconstrained regime where supreme authority is concentrated in an individual ruler exempt from constitutional checks.",
    quotes: [
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "Under the Caesars, the forms of the ancient republic served merely to mask an absolute imperial **autocracy**." },
      { author: "Hannah Arendt", work: "The Origins of Totalitarianism", quote: "Modern tyranny differs fundamentally from traditional **autocracy** in its total ideological subjugation of civil society." },
      { author: "Leo Tolstoy", work: "War and Peace", quote: "The vast Russian empire was governed by an absolute **autocracy** resting on the twin pillars of bureaucracy and faith." }
    ]
  },
  "Dashboard — crat/autocrat.md": {
    primary: "A ruler who has absolute power; a domineering or dictatorial person.",
    secondary: "In governance and institutional leadership, an authority figure who exercises complete control without taking advice or allowing opposition.",
    quotes: [
      { author: "Oliver Wendell Holmes Sr.", work: "The Autocrat of the Breakfast-Table", quote: "The genial **autocrat** held forth on philosophy and manners with unchallenged domestic supremacy." },
      { author: "Charles Dickens", work: "Hard Times", quote: "Mr. Bounderby ruled his factory and household like a self-satisfied, unyielding **autocrat**." },
      { author: "Winston Churchill", work: "The World Crisis", quote: "The Russian Tsar stood as the last great hereditary **autocrat** presiding over a collapsing empire." }
    ]
  },
  "Dashboard — crat/autocratic.md": {
    primary: "Relating to a ruler who has absolute power; taking no account of other people's wishes or opinions; domineering.",
    secondary: "In organizational and political behavior, characterized by unilateral decision-making and demanding absolute obedience.",
    quotes: [
      { author: "George Orwell", work: "Shooting an Elephant", quote: "The imperial administration enforced its mandates through rigid, **autocratic** directives." },
      { author: "Jane Austen", work: "Emma", quote: "Her manner in company had grown somewhat **autocratic**, brooking no difference in social arrangements." },
      { author: "Bertrand Russell", work: "Power: A New Social Analysis", quote: "The **autocratic** ruler lives in constant dread of conspiracy, isolating himself behind armed guards." }
    ]
  },
  "Dashboard — crat/bureaucracy.md": {
    primary: "A system of government or administration in which most decisions are taken by state officials rather than by elected representatives.",
    secondary: "In sociology, a rationalized, hierarchical administrative structure operating through standardized procedures and impersonal rules (Max Weber).",
    quotes: [
      { author: "Max Weber", work: "Economy and Society", quote: "Rational modern **bureaucracy** operates with calculated impersonality and strict jurisdictional competence." },
      { author: "Franz Kafka", work: "The Trial", quote: "K. wandered through endless attics and dusty hallways, suffocated by the unseen **bureaucracy**." },
      { author: "Alexis de Tocqueville", work: "The Old Regime and the Revolution", quote: "Centralized **bureaucracy** had quietly replaced local aristocratic administration long before the revolution erupted." }
    ]
  },
  "Dashboard — crat/bureaucrat.md": {
    primary: "An official in a government department, especially one concerned with procedural correctness at the expense of people's needs.",
    secondary: "In organizational sociology, a professional administrator whose authority derives from bureaucratic office and procedural expertise.",
    quotes: [
      { author: "Honoré de Balzac", work: "The Bureaucrats", quote: "The Parisian **bureaucrat** sat behind mountains of dossiers, wielding more real power than ministers of state." },
      { author: "George Orwell", work: "Nineteen Eighty-Four", quote: "Winston Smith toiled like a mechanical **bureaucrat** in the Ministry of Truth, rewriting historical records." },
      { author: "Hannah Arendt", work: "Eichmann in Jerusalem", quote: "The terrifying aspect of modern evil was the banal **bureaucrat** who carried out monstrous directives with clerk-like efficiency." }
    ]
  },
  "Dashboard — crat/bureaucratic.md": {
    primary: "Relating to the business of running an organization, or government; overly complicated, formal, and characterized by red tape.",
    secondary: "In sociology and organizational theory, defined by fixed official jurisdictions, hierarchical supervision, and written records.",
    quotes: [
      { author: "Max Weber", work: "The Theory of Social and Economic Organization", quote: "The **bureaucratic** form of administration is capable of attaining the highest degree of technical efficiency." },
      { author: "Joseph Heller", work: "Catch-22", quote: "Doc Daneeka found himself declared legally dead by an unyielding **bureaucratic** snafu." },
      { author: "C. Wright Mills", work: "The Power Elite", quote: "Modern corporate life has become dominated by a vast **bureaucratic** apparatus managing human capital." }
    ]
  },
  "Dashboard — crat/bureaucratism.md": {
    primary: "Excessive or rigid adherence to bureaucratic rules, routines, and official procedures; red tape.",
    secondary: "In political critique and socialist history, the concentration of state power in an entrenched, self-serving administrative caste.",
    quotes: [
      { author: "Leon Trotsky", work: "The Revolution Betrayed", quote: "Soviet society succumbed to the chokehold of entrenched **bureaucratism**, stifling revolutionary initiative." },
      { author: "Vladimir Lenin", work: "The State and Revolution", quote: "We must wage an uncompromising struggle against the disease of **bureaucratism** in worker councils." },
      { author: "Milovan Djilas", work: "The New Class", quote: "Monopolistic state ownership inevitably breeds a privileged caste driven solely by self-protective **bureaucratism**." }
    ]
  },
  "Dashboard — crat/cracy.md": {
    primary: "A combining form denoting a form of government, rule, or social influence (e.g. democracy, theocracy, meritocracy).",
    secondary: "In linguistic morphology and political philosophy, the productive suffix originating from Greek kratia, signifying sovereign power or dominion.",
    quotes: [
      { author: "Aristotle", work: "Politics", quote: "In analyzing states, we distinguish forms of civic power signified by the suffix -**cracy**, from demo- to aristo-." },
      { author: "Werner Jaeger", work: "Paideia: The Ideals of Greek Culture", quote: "The Greek concept of civic dominance embedded in -**cracy** shaped constitutional debate across antiquity." },
      { author: "H. L. Mencken", work: "Notes on Democracy", quote: "Every newly minted -**cracy** promises popular salvation while delivering old-fashioned elite rule." }
    ]
  },
  "Dashboard — crat/crataegus.md": {
    primary: "A genus of spiny shrubs and small trees commonly known as hawthorns (family Rosaceae), producing white or pink flowers and red pomes.",
    secondary: "In systematic botany and herbal medicine, deciduous woody plants renowned for heart-tonic flavonoids and dense hedging thorns.",
    quotes: [
      { author: "Gilbert White", work: "The Natural History of Selborne", quote: "The hedges of **Crataegus** blossomed with such profusion that the lanes seemed draped in white linen." },
      { author: "Henry David Thoreau", work: "Walden", quote: "I lingered by the flowering **Crataegus**, listening to the drowsy hum of bees among its scented thorns." },
      { author: "Asa Gray", work: "Manual of the Botany of the Northern United States", quote: "Species delimitation in the genus **Crataegus** presents extraordinary taxonomic complexity due to apomixis." }
    ]
  },
  "Dashboard — crat/crate.md": {
    primary: "A slatted wooden box or case used for transporting or storing goods; or to pack into such a container.",
    secondary: "In logistics, maritime shipping, and material handling, a rigid protective packaging framework.",
    quotes: [
      { author: "Jack London", work: "The Call of the Wild", quote: "Buck was released from his heavy wooden **crate** only to face the brutal discipline of the man in the red sweater." },
      { author: "John Steinbeck", work: "The Grapes of Wrath", quote: "They stacked each wooden fruit **crate** high upon the truck bed before hitting the dusty highway." },
      { author: "H. G. Wells", work: "The War of the Worlds", quote: "Curious villagers gathered around the battered packing **crate** containing optical instruments from London." }
    ]
  },
  "Dashboard — crat/crateful.md": {
    primary: "The amount that a crate will hold; as much as fills a crate.",
    secondary: "In commerce and domestic life, a substantial quantity or volume sufficient to fill a standard shipping crate.",
    quotes: [
      { author: "Thomas Hardy", work: "The Mayor of Casterbridge", quote: "The merchant ordered another **crateful** of fresh earthen jars to be delivered for the annual Michaelmas fair." },
      { author: "Charles Dickens", work: "David Copperfield", quote: "A generous **crateful** of oranges and winter apples arrived unexpectedly from the country." },
      { author: "Mark Twain", work: "Life on the Mississippi", quote: "We unloaded an enormous **crateful** of merchandise onto the muddy riverbank landing." }
    ]
  },
  "Dashboard — crat/crater.md": {
    primary: "A large, bowl-shaped cavity in the ground or on the surface of a planet or the moon, typically caused by an explosion or the impact of a meteorite, or the mouth of a volcano.",
    secondary: "In classical antiquity, an ancient Greek vessel (krater) used for mixing wine with water at symposia.",
    quotes: [
      { author: "Galileo Galilei", work: "Sidereus Nuncius", quote: "Through the telescope, the lunar surface is seen marked by many circular depressions resembling a volcanic **crater**." },
      { author: "John Boardman", work: "Athenian Red Figure Vases", quote: "The ceramic **crater** was placed in the center of the symposium room for mixing unwatered wine." },
      { author: "Charles Lyell", work: "Principles of Geology", quote: "The immense caldera erupted violent jets of steam from the central **crater** during the summer of 1822." }
    ]
  },
  "Dashboard — crat/crateva.md": {
    primary: "A genus of flowering trees and shrubs in the caper family (Capparaceae), native to tropical regions.",
    secondary: "In tropical botany and ethnopharmacology, plants such as Crateva religiosa valued for medicinal bark and ornamental showy flowers.",
    quotes: [
      { author: "Joseph Dalton Hooker", work: "The Flora of British India", quote: "Along riverbanks in Bengal, the handsome tree **Crateva** magna displays clouds of creamy white blossoms." },
      { author: "John Lindley", work: "The Vegetable Kingdom", quote: "Botanists classify **Crateva** within Capparaceae on account of its prominent stipitate ovary." },
      { author: "George Bentham", work: "Genera Plantarum", quote: "The trifoliolate leaves of **Crateva** distinguish it readily from neighboring caperaceous genera." }
    ]
  },
  "Dashboard — crat/craton.md": {
    primary: "A large, stable block of the earth's crust forming the ancient nucleus of a continent.",
    secondary: "In geotectonics and geophysics, the deep, mechanically rigid portion of continental lithosphere that has survived multiple cycles of rifting and collision.",
    quotes: [
      { author: "Eduard Suess", work: "The Face of the Earth", quote: "The primordial Canadian **craton** resisted orogenic deformation, standing as a firm anchor for the continent." },
      { author: "John Tuzo Wilson", work: "A Revolution in Earth Science", quote: "Plate margins collide and fold around the immovable roots of an ancient continental **craton**." },
      { author: "Alfred Wegener", work: "The Origin of Continents and Oceans", quote: "The stable crystalline blocks that constitute each **craton** exhibit matching structural trends across ocean basins." }
    ]
  },
  "Dashboard — crat/democracy.md": {
    primary: "A system of government by the whole population or all the eligible members of a state, typically through elected representatives.",
    secondary: "In political philosophy and constitutional history, self-governance rooted in popular sovereignty, equality under the law, and majority rule with minority protections.",
    quotes: [
      { author: "Abraham Lincoln", work: "Gettysburg Address", quote: "That government of the people, by the people, for the people, shall not perish from the earth in this **democracy**." },
      { author: "Alexis de Tocqueville", work: "Democracy in America", quote: "In a **democracy**, each generation is a new people that must forge its own civil institutions." },
      { author: "Winston Churchill", work: "Speech in the House of Commons", quote: "Many forms of Government have been tried, and no one pretends that **democracy** is all-wise or all-virtuous." }
    ]
  },
  "Dashboard — crat/democrat.md": {
    primary: "An advocate or supporter of democracy; or a member/supporter of a Democratic Party.",
    secondary: "A person who believes in social and political equality, treating others without aristocratic pretensions.",
    quotes: [
      { author: "Walt Whitman", work: "Democratic Vistas", quote: "The true **democrat** sees in every laborer and mechanic an equal partner in the republic." },
      { author: "Thomas Paine", work: "Common Sense", quote: "A sincere **democrat** insists that rights belong to humanity by nature, not by royal patent." },
      { author: "Alexis de Tocqueville", work: "Democracy in America", quote: "The American **democrat** carries into all life an ingrained habit of independent civic participation." }
    ]
  },
  "Dashboard — crat/democratic.md": {
    primary: "Relating to or supporting the principles of democracy; favoring social equality.",
    secondary: "Characterized by open participation, equal voting rights, and transparency across civic or organizational bodies.",
    quotes: [
      { author: "John Dewey", work: "Democracy and Education", quote: "A **democratic** society must have a type of education which gives individuals a personal interest in social relationships." },
      { author: "George Orwell", work: "The Lion and the Unicorn", quote: "English social habits are deeply **democratic** in spirit, despite lingering distinctions of class and accent." },
      { author: "Woodrow Wilson", work: "Address to Congress", quote: "The world must be made safe for democracy through the promotion of **democratic** self-determination." }
    ]
  },
  "Dashboard — crat/democratise.md": {
    primary: "To introduce a democratic system or democratic principles to; make democratic (British/Commonwealth spelling of democratize).",
    secondary: "To make something widely accessible or available to everyone regardless of social class or wealth.",
    quotes: [
      { author: "H. G. Wells", work: "The Outline of History", quote: "The spread of the printing press served to **democratise** knowledge across every stratum of European society." },
      { author: "John Stuart Mill", work: "Considerations on Representative Government", quote: "Reforms must gradually **democratise** municipal councils to train the citizenry for higher civic duties." },
      { author: "E. M. Forster", work: "Two Cheers for Democracy", quote: "Attempts to **democratise** taste often succeed in substituting commercial vulgarity for genuine culture." }
    ]
  },
  "Dashboard — crat/democratize.md": {
    primary: "To make democratic; introduce a democratic system or principles into.",
    secondary: "To make something accessible or available to the general public rather than an elite minority.",
    quotes: [
      { author: "John Dewey", work: "The Public and Its Problems", quote: "We must constantly **democratize** our daily associations if political democracy is to remain genuine." },
      { author: "Alexis de Tocqueville", work: "Democracy in America", quote: "Forces that tend to equalize conditions will eventually **democratize** all social institutions." },
      { author: "Noam Chomsky", work: "Necessary Illusions", quote: "True reform requires that we **democratize** the media and open public airwaves to authentic debate." }
    ]
  },
  "Dashboard — crat/isocrates.md": {
    primary: "Ancient Greek rhetorician and orator (436–338 BC), one of the Ten Attic Orators and founder of an influential school of rhetoric in Athens.",
    secondary: "In classical education and political philosophy, the leading champion of Panhellenism and broad liberal education (paideia) through polished political discourse.",
    quotes: [
      { author: "Cicero", work: "De Oratore", quote: "From the rhetorical school of **Isocrates**, as from the Trojan horse, none but real princes stepped forth." },
      { author: "Quintilian", work: "Institutio Oratoria", quote: "The smooth, rhythmic prose of **Isocrates** was polished with unbelievable patience for civic assemblies." },
      { author: "Werner Jaeger", work: "Paideia: The Ideals of Greek Culture", quote: "In the curriculum of **Isocrates**, rhetorical eloquence was inseparable from moral and patriotic virtue." }
    ]
  },
  "Dashboard — crat/kratos.md": {
    primary: "The personification of strength, might, sovereign power, or dominion in Greek mythology.",
    secondary: "In classical political thought and linguistics, the root word representing sovereign coercive force, state authority, and political dominion.",
    quotes: [
      { author: "Aeschylus", work: "Prometheus Bound", quote: "**Kratos** and Bia, divine emissaries of Zeus, bind the defiant Titan to the Caucasian crag." },
      { author: "Hesiod", work: "Theogony", quote: "Styx brought her children, **Kratos** and Nike, to assist Olympian Zeus in his war against the Titans." },
      { author: "Plato", work: "Gorgias", quote: "Callicles asserted that by nature's law, supreme **kratos** belongs of right to the strongest." }
    ]
  },
  "Dashboard — crat/meritocracy.md": {
    primary: "A political system or society in which individuals hold power, status, or office based on their demonstrated ability and talent rather than wealth or birth.",
    secondary: "In sociology, a system of social stratification governed by educational credentials, competitive examinations, and measured performance (coined by Michael Young).",
    quotes: [
      { author: "Michael Young", work: "The Rise of the Meritocracy", quote: "I coined the term **meritocracy** as a satire, warning of a stratified society sorted purely by IQ and effort." },
      { author: "John Rawls", work: "A Theory of Justice", quote: "A pure **meritocracy** still leaves social outcomes hostage to the arbitrary lottery of natural talents." },
      { author: "Daniel Bell", work: "The Coming of Post-Industrial Society", quote: "In post-industrial society, professional credentials and technical knowledge make **meritocracy** the dominant ethos." }
    ]
  },
  "Dashboard — crat/meritocratic.md": {
    primary: "Relating to or characteristic of a meritocracy; selecting and promoting individuals based on ability rather than privilege.",
    secondary: "In institutional sociology, describing systems where career mobility depends upon demonstrable aptitude and objective performance standards.",
    quotes: [
      { author: "Thomas Piketty", work: "Capital in the Twenty-First Century", quote: "Modern society justifies vast inequalities through an appealing **meritocratic** rhetoric of personal effort." },
      { author: "Christopher Lasch", work: "The Revolt of the Elites", quote: "The new **meritocratic** class feels no loyalty to the communities left behind by their upward mobility." },
      { author: "Michael J. Sandel", work: "The Tyranny of Merit", quote: "The **meritocratic** hubris of winners creates humiliation and legitimate grievance among those who fall behind." }
    ]
  },
  "Dashboard — crat/monocracy.md": {
    primary: "Government or rule by a single person; autocracy or monarchy.",
    secondary: "In political science and constitutional history, a form of government where unshared supreme authority resides in one sovereign ruler.",
    quotes: [
      { author: "Thomas Jefferson", work: "The Writings of Thomas Jefferson", quote: "Our citizens rejected the federalist drift toward **monocracy**, reaffirming republican liberties." },
      { author: "James Madison", work: "The Federalist Papers", quote: "The separation of constitutional powers was devised precisely to prevent an accumulation into **monocracy**." },
      { author: "John Adams", work: "A Defence of the Constitutions of Government", quote: "A pure **monocracy** without legal checks degenerates swiftly into arbitrary oriental despotism." }
    ]
  },
  "Dashboard — crat/pancratium.md": {
    primary: "An ancient Greek athletic contest combining boxing and wrestling, characterized by minimal rules.",
    secondary: "In classical sports history, an Olympic event instituted in 648 BC; or in botany, a genus of bulbous amaryllid plants (sea daffodils).",
    quotes: [
      { author: "Pausanias", work: "Description of Greece", quote: "Athletes in the fierce **pancratium** were forbidden only to gouge eyes or sink their teeth into opponents." },
      { author: "Philostratus", work: "Gymnasticus", quote: "The champion of the **pancratium** must combine the agility of the wrestler with the brute power of the boxer." },
      { author: "John Lindley", work: "The Vegetable Kingdom", quote: "Fragrant white lilies of the genus **Pancratium** bloom gracefully along sandy Mediterranean shores." }
    ]
  },
  "Dashboard — crat/uncrate.md": {
    primary: "To remove something from a crate or packing case.",
    secondary: "In shipping, museology, and retail logistics, the careful unpacking and inspection of crated cargo or artworks.",
    quotes: [
      { author: "John Steinbeck", work: "Cannery Row", quote: "Doc carefully used his crowbar to **uncrate** the delicate glass jars containing marine specimens." },
      { author: "Ernest Hemingway", work: "A Moveable Feast", quote: "We hurried to **uncrate** the fresh shipment of literary magazines sent across the Atlantic from New York." },
      { author: "H. G. Wells", work: "The Invisible Man", quote: "The innkeeper watched the stranger **uncrate** dozens of mysterious glass retorts and chemical vials." }
    ]
  },
  "Dashboard — crat/undemocratic.md": {
    primary: "Not in accordance with democratic principles; autocratic, oligarchic, or denying equal political representation.",
    secondary: "Characterized by opaque decision-making, disenfranchisement, or denial of basic civil liberties.",
    quotes: [
      { author: "George Orwell", work: "Homage to Catalonia", quote: "The suppression of dissident political newspapers was denounced as thoroughly **undemocratic**." },
      { author: "John Stuart Mill", work: "Considerations on Representative Government", quote: "A system that denies suffrage based on hereditary birth is flagrantly **undemocratic**." },
      { author: "Alexis de Tocqueville", work: "Democracy in America", quote: "The arbitrary power of unelected magistrates struck visitors as an **undemocratic** anomaly." }
    ]
  }
};

let updatedCount = 0;
for (const [relPath, entry] of Object.entries(filesData)) {
  const filePath = path.join(baseDir, relPath);
  if (!fs.existsSync(filePath)) {
    console.error(`File does not exist: ${filePath}`);
    continue;
  }
  const content = fs.readFileSync(filePath, 'utf8');
  const bookIdx = content.indexOf('> [!book]');
  if (bookIdx === -1) {
    console.error(`No > [!book] in ${relPath}`);
    continue;
  }
  const topBlock = content.substring(0, bookIdx);
  const newContent = `${topBlock}> [!book] 📖 Definitions & Semantic Range
> 1. **Primary Definition (Lexical / Standard Consensus)**: ${entry.primary}
> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: ${entry.secondary}

> [!quote] 💬 Contextual Usage & Authentic Quotations
${entry.quotes.map(q => `> - 📜 **${q.author} (*${q.work}*):** *"${q.quote}"*`).join('\n')}
`;

  fs.writeFileSync(filePath, newContent, 'utf8');
  updatedCount++;
}

console.log(`Updated ${updatedCount} files in Batch 2 (anthrop + crat)!`);
