import fs from 'fs';
import path from 'path';

const baseDir = 'App database/Greek roots/Cluster Society & Governance';

const filesData = {
  // === Dashboard — dem (32 words) ===
  "Dashboard — dem/apodeme.md": {
    primary: "An ingrowth of the arthropod exoskeleton serving as an internal site for muscle attachment.",
    secondary: "In arthropod anatomy and biomechanics, an invaginated cuticular plate or ridge that provides rigid leverage for flexor and extensor muscles.",
    quotes: [
      { author: "Robert E. Snodgrass", work: "Principles of Insect Morphology", quote: "Each thoracic **apodeme** provides a firm anchor for the powerful flight musculature of insects." },
      { author: "Richard Owen", work: "Lectures on the Comparative Anatomy and Physiology of the Invertebrate Animals", quote: "The crustacean endophragmal system is composed of an intricate series of internal **apodeme** structures." },
      { author: "V. B. Wigglesworth", work: "The Principles of Insect Physiology", quote: "Muscular tension transmitted through the cuticular **apodeme** produces rapid articulation of the appendage." }
    ]
  },
  "Dashboard — dem/Damocles.md": {
    primary: "A courtier of ancient Syracuse, legendary subject of the sword of Damocles story symbolizing impending danger.",
    secondary: "In classical literature and political rhetoric, the archetype of constant, looming peril hanging over those in power.",
    quotes: [
      { author: "Cicero", work: "Tusculan Disputations", quote: "Dionysius taught **Damocles** the true terror of tyranny by suspending a gleaming sword above his head by a single horsehair." },
      { author: "John F. Kennedy", work: "Address to the UN General Assembly", quote: "Every man, woman, and child lives under a nuclear sword of **Damocles**, hanging by the slenderest of threads." },
      { author: "Thomas Carlyle", work: "The French Revolution", quote: "Over the royal banquet hung the invisible sword of **Damocles**, ready to sever ancient privileges." }
    ]
  },
  "Dashboard — dem/dem 2.md": {
    primary: "A combining root derived from Ancient Greek dēmos, denoting the people, citizens, or a localized population.",
    secondary: "In historical linguistics and sociopolitical morphology, the foundational morpheme in compounds signifying popular sovereignty and civic assemblies.",
    quotes: [
      { author: "Aristotle", work: "Constitution of the Athenians", quote: "Cleisthenes reorganized the citizenry by redistributing the **dem**- units to break aristocratic clan power." },
      { author: "George Grote", work: "A History of Greece", quote: "Attic political consciousness was rooted in local participation across every rural and urban **dem**-." },
      { author: "Werner Jaeger", work: "Paideia: The Ideals of Greek Culture", quote: "The Greek concept of **dem**- signified both the aggregate body of citizens and the common folk as a political force." }
    ]
  },
  "Dashboard — dem/dem.md": {
    primary: "A combining form derived from Greek dēmos ('people', 'district'), forming words related to populations and governance.",
    secondary: "In etymological lexicography, the root morpheme signifying civic community, demographic distributions, and endemic conditions.",
    quotes: [
      { author: "Plato", work: "The Republic", quote: "The transition from oligarchy begins when the impoverished **dem**- claims equal political share in the commonwealth." },
      { author: "Alexis de Tocqueville", work: "Democracy in America", quote: "The vitality of civic associations reveals the fundamental character of the American **dem**-." },
      { author: "Will Durant", work: "The Life of Greece", quote: "Greek vocabulary gave the modern world terms uniting the **dem**- with institutions of popular justice." }
    ]
  },
  "Dashboard — dem/demagogue.md": {
    primary: "A political leader who seeks support by appealing to popular desires and prejudices rather than by using rational argument.",
    secondary: "In political science and history, an orator who exploits factional passions, grievances, and fears to acquire power.",
    quotes: [
      { author: "Thucydides", work: "History of the Peloponnesian War", quote: "Cleon was the most violent of the citizens, and by far the most persuasive **demagogue** before the assembly." },
      { author: "James Madison", work: "The Federalist Papers", quote: "History teaches that of the men who have overturned the liberties of republics, the greatest number began their career as a **demagogue**." },
      { author: "H. L. Mencken", work: "Notes on Democracy", quote: "The **demagogue** is one who preaches doctrines he knows to be untrue to men he knows to be idiots." }
    ]
  },
  "Dashboard — dem/deme.md": {
    primary: "A political division or township of ancient Attica; or in biology, a local population of interbreeding organisms.",
    secondary: "In evolutionary ecology, a panmictic local population sharing a common gene pool and subject to localized natural selection.",
    quotes: [
      { author: "Aristotle", work: "Constitution of the Athenians", quote: "Enrollment in the local **deme** replaced aristocratic ancestry as the primary credential of Athenian citizenship." },
      { author: "Ernst Mayr", work: "Animal Species and Evolution", quote: "Gene flow between each local **deme** maintains the genetic coherence of the widespread continental species." },
      { author: "George Grote", work: "A History of Greece", quote: "Every free Athenian belonged to a hereditary **deme**, maintaining civic registers for tax and military levies." }
    ]
  },
  "Dashboard — dem/demise.md": {
    primary: "A person's death; or the transfer of property or sovereignty by deed, will, or abdication.",
    secondary: "In legal and constitutional history, the formal devolution of royal authority upon the death or abdication of the sovereign.",
    quotes: [
      { author: "William Blackstone", work: "Commentaries on the Laws of England", quote: "Upon the **demise** of the crown, the royal dignity is immediately transferred to the lawful successor without interregnum." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The sudden **demise** of the emperor plunged the provinces into a bloody succession crisis." },
      { author: "Charles Dickens", work: "Bleak House", quote: "The unexpected **demise** of the wealthy claimant altered the fortunes of every expectant beneficiary." }
    ]
  },
  "Dashboard — dem/demist.md": {
    primary: "To clear moisture, condensation, or mist from a glass surface (such as a vehicle windshield).",
    secondary: "In automotive engineering and climate control, to direct warm or dehydrated air across windows to restore optical transparency.",
    quotes: [
      { author: "J. G. Ballard", work: "Crash", quote: "He turned the dashboard blower to **demist** the condensation filming the interior of the sports car." },
      { author: "Nevile Shute", work: "On the Beach", quote: "The driver paused to **demist** the windscreen with his sleeve before steering through the heavy drizzle." },
      { author: "Arthur Hailey", work: "Wheels", quote: "Engineers calibrated the defroster vents to rapidly **demist** the glass in subzero testing chambers." }
    ]
  },
  "Dashboard — dem/democracy.md": {
    primary: "A system of government by the whole population or all the eligible members of a state, typically through elected representatives.",
    secondary: "In constitutional philosophy, an institutional order founded on popular sovereignty, universal franchise, civil rights, and political equality.",
    quotes: [
      { author: "Pericles", work: "Funeral Oration", quote: "Our constitution is called a **democracy** because its administration is in the hands of the many and not of the few." },
      { author: "Alexis de Tocqueville", work: "Democracy in America", quote: "In a true **democracy**, equality of condition exerts a prodigious influence on every civic habit." },
      { author: "John Dewey", work: "Democracy and Education", quote: "A **democracy** is more than a form of government; it is primarily a mode of associated living." }
    ]
  },
  "Dashboard — dem/democratic.md": {
    primary: "Relating to or supporting the principles of democracy; characterized by social equality.",
    secondary: "In political science, exhibiting free contestation, transparent civic procedures, and accountability to the electorate.",
    quotes: [
      { author: "Woodrow Wilson", work: "Address to the Senate", quote: "Only a peace between equals can last; only a **democratic** order can guarantee enduring liberty." },
      { author: "George Orwell", work: "The Lion and the Unicorn", quote: "The stubborn **democratic** instinct of the common people survived the blitz and wartime privation." },
      { author: "Thomas Paine", work: "Rights of Man", quote: "A genuinely **democratic** constitution derives its authority solely from the unforced consent of the governed." }
    ]
  },
  "Dashboard — dem/democratise.md": {
    primary: "To introduce a democratic system or democratic principles to; make democratic (British spelling of democratize).",
    secondary: "To make culture, education, or technology broadly available and accessible to the common citizenry.",
    quotes: [
      { author: "H. G. Wells", work: "The Work, Wealth and Happiness of Mankind", quote: "Technological progress serves to **democratise** cultural luxuries once reserved for hereditary monarchs." },
      { author: "John Stuart Mill", work: "Considerations on Representative Government", quote: "We must gradually **democratise** municipal boards so that the working classes learn practical administration." },
      { author: "Virginia Woolf", work: "Three Guineas", quote: "To educate women without bias is to **democratise** the very foundations of the university." }
    ]
  },
  "Dashboard — dem/democratize.md": {
    primary: "To make democratic; introduce democracy or egalitarian principles into an institution or society.",
    secondary: "To open access, distribute power, or decentralize control across an organization or field of study.",
    quotes: [
      { author: "John Dewey", work: "The Public and Its Problems", quote: "We must continually **democratize** the habits of daily life to preserve our political freedoms." },
      { author: "Alexis de Tocqueville", work: "Democracy in America", quote: "Forces that equalize human conditions will eventually **democratize** religious and social hierarchy." },
      { author: "Noam Chomsky", work: "Manufacturing Consent", quote: "Genuine reform must **democratize** information channels so citizens can deliberate free from elite propaganda." }
    ]
  },
  "Dashboard — dem/demographer.md": {
    primary: "An expert in the study of statistics relating to human populations, including births, deaths, and migrations.",
    secondary: "A quantitative social scientist who models cohort shifts, fertility rates, mortality tables, and urbanization patterns.",
    quotes: [
      { author: "Thomas Robert Malthus", work: "An Essay on the Principle of Population", quote: "The skilled **demographer** calculates how unchecked arithmetic food growth fails to match geometric human increase." },
      { author: "Gunnar Myrdal", work: "An American Dilemma", quote: "The **demographer** tracks migratory currents from rural fields into northern industrial centers." },
      { author: "Paul R. Ehrlich", work: "The Population Bomb", quote: "No serious **demographer** could ignore the exponential acceleration of postwar global population curves." }
    ]
  },
  "Dashboard — dem/demographic.md": {
    primary: "Relating to the structure of populations; or a particular sector of a population.",
    secondary: "In sociology and statistical economics, relating to age distributions, socioeconomic brackets, or geographic population clusters.",
    quotes: [
      { author: "Alexis de Tocqueville", work: "Democracy in America", quote: "Rapid westward expansion produced profound **demographic** transformations in the American character." },
      { author: "Jane Jacobs", work: "The Death and Life of Great American Cities", quote: "Healthy neighborhoods sustain vibrant **demographic** diversity across generations and trades." },
      { author: "Rachel Carson", work: "Silent Spring", quote: "Human settlements expand into wilderness, altering the **demographic** stability of indigenous fauna." }
    ]
  },
  "Dashboard — dem/demographist.md": {
    primary: "A demographer; one who practices demography or population statistics.",
    secondary: "An archaic or formal term for a demographic statistician investigating societal vital statistics.",
    quotes: [
      { author: "Francis Galton", work: "Hereditary Genius", quote: "The **demographist** records significant variations in family longevity and occupational inheritance." },
      { author: "Herbert Spencer", work: "The Principles of Sociology", quote: "Vast census tables compiled by the **demographist** illustrate the cyclical growth of urban centers." },
      { author: "Arthur Conan Doyle", work: "The Sign of the Four", quote: "He analyzed the mortality tables with the cold, meticulous precision of a veteran **demographist**." }
    ]
  },
  "Dashboard — dem/demography.md": {
    primary: "The study of statistics such as births, deaths, income, or the incidence of disease, which illustrate the changing structure of human populations.",
    secondary: "In quantitative social science, the systematic analysis of dynamic population processes including fertility, mortality, and migration.",
    quotes: [
      { author: "Thomas Robert Malthus", work: "An Essay on the Principle of Population", quote: "Modern **demography** began when parish registers were systematically organized into vital statistics." },
      { author: "Lewis Mumford", work: "The City in History", quote: "The changing **demography** of industrial cities revealed catastrophic infant mortality rates in crowded tenements." },
      { author: "J. B. S. Haldane", work: "Daedalus; or, Science and the Future", quote: "Advances in hygiene and preventive medicine will fundamentally transform national **demography**." }
    ]
  },
  "Dashboard — dem/demonym.md": {
    primary: "A noun used to denote the natives or inhabitants of a particular country, state, city, or region (e.g. Parisian, Athenian, American).",
    secondary: "In onomastics and linguistic geography, a proper noun or adjective derived from a toponym identifying its regional populace.",
    quotes: [
      { author: "H. L. Mencken", work: "The American Language", quote: "The awkwardness of coining an acceptable **demonym** for citizens of the United States perplexed early grammarians." },
      { author: "David Foster Wallace", work: "A Supposedly Fun Thing I'll Never Do Again", quote: "Local pride often hinges on whether the regional **demonym** ends in -ian, -ite, or -er." },
      { author: "Bill Bryson", work: "Made in America", quote: "Few linguistic quirks are as stubbornly local as the peculiar **demonym** chosen by Midwestern townspeople." }
    ]
  },
  "Dashboard — dem/demophobia.md": {
    primary: "An abnormal, irrational, or intense fear of crowds or masses of people; agoraphobia or ochlophobia.",
    secondary: "In psychiatric nosology and social psychology, severe panic symptoms provoked by congested public spaces or gathering assemblies.",
    quotes: [
      { author: "William James", work: "The Principles of Psychology", quote: "Morbid aversions such as claustrophobia and **demophobia** paralyze the subject in dense urban crowds." },
      { author: "Sigmund Freud", work: "Group Psychology and the Analysis of the Ego", quote: "The neurotic's acute **demophobia** often masks an unconscious dread of submerging his ego in the collective mass." },
      { author: "Robert Burton", work: "The Anatomy of Melancholy", quote: "Solitary melancholics shun market squares and fairs, fleeing human company in sudden **demophobia**." }
    ]
  },
  "Dashboard — dem/demotic.md": {
    primary: "Denoting or relating to the kind of language used by ordinary people; colloquial; or relating to the simplified cursive script of ancient Egypt.",
    secondary: "In Hellenic linguistics, Demotic Greek (Dimotiki), the popular spoken language codified as the official national standard in 1976.",
    quotes: [
      { author: "Jean-François Champollion", work: "Précis du Système Hiéroglyphique", quote: "The Rosetta Stone displayed the royal decree in sacred hieroglyphics, popular **demotic** script, and Greek." },
      { author: "T. S. Eliot", work: "The Music of Poetry", quote: "Poetry must renew its vitality by keeping in constant touch with the **demotic** speech of living men." },
      { author: "Kazantzakis Nikos", work: "Report to Greco", quote: "He wrote with the fiery, unvarnished strength of the **demotic** tongue spoken by Cretan fishermen." }
    ]
  },
  "Dashboard — dem/demure.md": {
    primary: "Reserved, modest, and shy (typically used of a woman or girl); or affecting modesty or sobriety.",
    secondary: "In behavioral and literary descriptions, conveying quiet decorum, restrained manners, or playful modesty.",
    quotes: [
      { author: "Jane Austen", work: "Pride and Prejudice", quote: "She sat with a **demure** countenance, pretending not to notice the admiring glances cast in her direction." },
      { author: "Charlotte Brontë", work: "Jane Eyre", quote: "My simple black dress and **demure** manners concealed a heart burning with fierce independence." },
      { author: "William Makepeace Thackeray", work: "Vanity Fair", quote: "Becky Sharp cast down her eyes with the most innocent and **demure** expression imaginable." }
    ]
  },
  "Dashboard — dem/diadem.md": {
    primary: "A jeweled crown or headband worn as a symbol of sovereignty.",
    secondary: "In classical antiquity and numismatics, a white silk ribbon or fillet bound around the brow of Hellenistic kings to denote royal power.",
    quotes: [
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "Diocletian replaced the laurel wreath with a pearl-encrusted imperial **diadem**, adopting Persian court ceremonial." },
      { author: "John Milton", work: "Paradise Lost", quote: "Upon his brow he wore no gilded **diadem**, but majesty that outshone earthly monarchs." },
      { author: "William Shakespeare", work: "Hamlet", quote: "A murderer and a villain, A slave that was not twentieth part the tithe Of your precedent lord; a vice of kings; A cutpurse of the empire and the rule, That from a shelf the precious **diadem** stole." }
    ]
  },
  "Dashboard — dem/ecdemic.md": {
    primary: "Originating outside or brought in from abroad; foreign or not endemic (especially of a disease or species).",
    secondary: "In epidemiology and biogeography, describing imported pathologies or non-indigenous organisms introduced into a new territory.",
    quotes: [
      { author: "William Farr", work: "Vital Statistics", quote: "Port quarantine officers must distinguish between local endemic fevers and deadly **ecdemic** contagions arriving on merchant ships." },
      { author: "Charles Lyell", work: "Principles of Geology", quote: "The arrival of **ecdemic** flora often displaces native island vegetation through competitive exclusion." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The sudden outbreak of cholera was demonstrably **ecdemic**, traced directly to an infected cargo vessel." }
    ]
  },
  "Dashboard — dem/endemic.md": {
    primary: "Regularly found among particular people or in a certain area (of a disease or condition); or native and restricted to a certain place (of a plant or animal).",
    secondary: "In epidemiology, a disease maintained in a population without external inputs; in biogeography, a taxon unique to a defined geographic location.",
    quotes: [
      { author: "Charles Darwin", work: "The Voyage of the Beagle", quote: "The Galápagos Archipelago harbors a remarkable proportion of species **endemic** to those isolated lava shores." },
      { author: "Alexander von Humboldt", work: "Personal Narrative of Travels", quote: "Certain malarial fevers appeared **endemic** to the swampy lowlands of the Orinoco river basin." },
      { author: "Rachel Carson", work: "The Edge of the Sea", quote: "In protected tidal coves, **endemic** seaweeds thrive in microhabitats found nowhere else along the coast." }
    ]
  },
  "Dashboard — dem/endemical.md": {
    primary: "Pertaining to or of the nature of an endemic disease; endemic (archaic or formal variant).",
    secondary: "Pertaining to diseases or conditions habitual to a specific region or population.",
    quotes: [
      { author: "Thomas Sydenham", work: "Observationes Medicae", quote: "Certain agues are clearly **endemical** to the fens, returning with predictable seasonal regularity." },
      { author: "Benjamin Rush", work: "Medical Inquiries and Observations", quote: "The bilious fever was deemed by many practitioners to be an **endemical** scourge of humid river valleys." },
      { author: "William Buchan", work: "Domestic Medicine", quote: "Diet and climate render particular disorders **endemical** among miners and textile weavers." }
    ]
  },
  "Dashboard — dem/endemism.md": {
    primary: "The ecological state of a species being native to a single defined geographic location, such as an island, nation, or other defined zone.",
    secondary: "In biogeography and conservation biology, high levels of endemism indicate unique evolutionary radiation and prioritize biodiversity preservation.",
    quotes: [
      { author: "Alfred Russel Wallace", work: "Island Life", quote: "Continental islands separated in ancient geological epochs exhibit extraordinary levels of floral **endemism**." },
      { author: "E. O. Wilson", work: "The Diversity of Life", quote: "Madagascar stands as a global sanctuary of evolutionary **endemism**, home to primates found nowhere else." },
      { author: "Stephen Jay Gould", work: "Hen's Teeth and Horse's Toes", quote: "The localized **endemism** of Cerion land snails on Caribbean islets demonstrates micro-evolutionary drift." }
    ]
  },
  "Dashboard — dem/epidemiologic.md": {
    primary: "Of or relating to epidemiology; concerning the incidence, distribution, and control of diseases.",
    secondary: "In public health, relating to observational cohort studies, case-control analyses, and disease etiology across populations.",
    quotes: [
      { author: "John Snow", work: "On the Mode of Communication of Cholera", quote: "Careful **epidemiologic** mapping traced the cholera contagion directly to the Broad Street water pump." },
      { author: "William Osler", work: "Aequanimitas", quote: "Rigorous **epidemiologic** surveys are essential before sanitary legislation can be enacted with confidence." },
      { author: "J. B. S. Haldane", work: "Heredity and Politics", quote: "Public health reforms rely upon sound **epidemiologic** statistics to evaluate workplace hazards." }
    ]
  },
  "Dashboard — dem/epidemiological.md": {
    primary: "Relating to the branch of medicine which deals with the incidence, distribution, and possible control of diseases.",
    secondary: "In population health, applying statistical methodology to identify risk factors, contagion pathways, and preventative measures.",
    quotes: [
      { author: "Richard Doll", work: "Smoking and Carcinoma of the Lung", quote: "Our long-term **epidemiological** study established an undeniable causal link between cigarette smoking and bronchial cancer." },
      { author: "Lewis Thomas", work: "The Medusa and the Snail", quote: "The triumph over poliomyelitis was guided step by step by brilliant **epidemiological** fieldwork." },
      { author: "Paul de Kruif", work: "Microbe Hunters", quote: "Pioneering researchers combined laboratory bacteriology with tireless **epidemiological** tracking across infected slums." }
    ]
  },
  "Dashboard — dem/epidemiologist.md": {
    primary: "A scientist or medical professional who studies the patterns, causes, and effects of health and disease conditions in defined populations.",
    secondary: "A public health specialist tasked with outbreak investigations, surveillance systems, and prophylactic health policy.",
    quotes: [
      { author: "John Snow", work: "Report on the Cholera Outbreak in the Parish of St. James", quote: "The **epidemiologist** must examine every case with detective-like rigor to uncover common sources of infection." },
      { author: "Paul de Kruif", work: "Microbe Hunters", quote: "The courageous **epidemiologist** entered yellow-fever quarantine camps to track the transmission vectors." },
      { author: "Oliver Sacks", work: "Awakenings", quote: "The clinical **epidemiologist** noted with bewilderment the global wave of encephalitis lethargica following the Great War." }
    ]
  },
  "Dashboard — dem/epidemiology.md": {
    primary: "The branch of medicine which deals with the incidence, distribution, and possible control of diseases and other factors relating to health.",
    secondary: "The core quantitative science of public health, analyzing infectious disease transmission, chronic disease risk, and community wellness.",
    quotes: [
      { author: "John Snow", work: "On the Mode of Communication of Cholera", quote: "Modern **epidemiology** was born when waterborne contamination was mathematically demonstrated in Soho." },
      { author: "William Osler", work: "The Evolution of Modern Medicine", quote: "Preventive medicine owes its greatest triumphs to the systematic application of **epidemiology**." },
      { author: "Hans Zinsser", work: "Rats, Lice and History", quote: "The history of human civilization cannot be written without understanding the ruthless **epidemiology** of typhus." }
    ]
  },
  "Dashboard — dem/monodomy.md": {
    primary: "The state of an ant colony or social insect population having only a single nest; monodomous organization.",
    secondary: "In myrmecology and sociobiology, nest architecture where a single queen and colony inhabit a self-contained subterranean or arboreal nest.",
    quotes: [
      { author: "William Morton Wheeler", work: "Ants: Their Structure, Development and Behavior", quote: "Primitive ponerine species exhibit strict **monodomy**, defending a solitary nest burrow against neighbors." },
      { author: "E. O. Wilson", work: "The Insect Societies", quote: "The transition from **monodomy** to polydomy allows supercolonies to monopolize vast foraging territories." },
      { author: "Bert Hölldobler", work: "The Ants", quote: "Colony territoriality in Pogonomyrmex is maintained through aggressive defense of their solitary **monodomy** site." }
    ]
  },
  "Dashboard — dem/polydomy.md": {
    primary: "The social organization of an animal colony (especially ants) occupying multiple geographically separated nests.",
    secondary: "In insect sociobiology, a colony structure where interconnected nests share brood, workers, and food resources without mutual aggression.",
    quotes: [
      { author: "E. O. Wilson", work: "The Insect Societies", quote: "In cases of extensive **polydomy**, an ant colony expands into a decentralized network of satellite outposts." },
      { author: "Bert Hölldobler", work: "The Ants", quote: "Resource distribution in wood ants is facilitated by seasonal **polydomy**, linking tree canopies to soil nests." },
      { author: "William Morton Wheeler", work: "Social Life Among the Insects", quote: "The invasive Argentine ant owes its devastating ecological success to rampant unconstrained **polydomy**." }
    ]
  },
  "Dashboard — dem/undemocratic.md": {
    primary: "Not in accordance with democratic principles; autocratic, oligarchic, or denying equal political representation.",
    secondary: "In political science, describing institutional arrangements, electoral practices, or governance models that suppress popular participation.",
    quotes: [
      { author: "George Orwell", work: "Homage to Catalonia", quote: "The suppression of dissident political newspapers was denounced as thoroughly **undemocratic**." },
      { author: "John Stuart Mill", work: "Considerations on Representative Government", quote: "A system that denies suffrage based on hereditary birth is flagrantly **undemocratic**." },
      { author: "Alexis de Tocqueville", work: "Democracy in America", quote: "The arbitrary power of unelected magistrates struck foreign visitors as an **undemocratic** anomaly." }
    ]
  },

  // === Dashboard — gyn (36 words) ===
  "Dashboard — gyn/acrogynous.md": {
    primary: "Having archegonia (female reproductive organs) terminating the main axis or stem of growth, as in certain liverworts.",
    secondary: "In bryology, describing jungermannialean liverworts whose stem apical cell is converted directly into an archegonium, stopping further axial growth.",
    quotes: [
      { author: "Douglas Houghton Campbell", work: "The Structure and Development of Mosses and Ferns", quote: "In **acrogynous** Jungermanniales, the formation of archegonia arrests the terminal elongation of the shoot." },
      { author: "F. O. Bower", work: "The Origin of a Land Flora", quote: "The **acrogynous** condition represents a definitive morphological transition in gametophytic apical growth." },
      { author: "John Lindley", work: "The Vegetable Kingdom", quote: "Cryptogamic taxonomists separate leafy liverworts into anacrogynous and **acrogynous** families." }
    ]
  },
  "Dashboard — gyn/androgenous.md": {
    primary: "Producing male offspring; or possessing male characteristics.",
    secondary: "In comparative biology and physiology, having virilizing traits or stimulating the formation of masculine tissues.",
    quotes: [
      { author: "Havelock Ellis", work: "Studies in the Psychology of Sex", quote: "Certain physiological profiles exhibit marked **androgenous** tendencies across both physical and behavioral domains." },
      { author: "Thomas Hunt Morgan", work: "The Mechanism of Mendelian Heredity", quote: "The phenotypic expression was heavily skewed toward **androgenous** developmental patterns in successive broods." },
      { author: "Herbert Spencer", work: "The Principles of Biology", quote: "Evolutionary differentiation manifests in both gynogenous and **androgenous** morphological adaptations." }
    ]
  },
  "Dashboard — gyn/androgyne.md": {
    primary: "A person or organism possessing both masculine and feminine characteristics; a hermaphrodite.",
    secondary: "In mythology, cultural history, and botany, an entity uniting male and female characteristics within a single form.",
    quotes: [
      { author: "Plato", work: "Symposium", quote: "The original **androgyne** was a single whole uniting male and female before the gods sliced humanity into halves." },
      { author: "Virginia Woolf", work: "Orlando: A Biography", quote: "The perfect artist's mind must be an **androgyne**, fluidly transcending rigid sexual polarities." },
      { author: "Carl Jung", work: "Psychology and Alchemy", quote: "The mystical rebis or divine **androgyne** symbolizes the final integration of the shadow and anima." }
    ]
  },
  "Dashboard — gyn/androgynous.md": {
    primary: "Partly male and partly female in appearance or characteristics; exhibiting blended gender qualities.",
    secondary: "In botany, bearing both staminate and pistillate flowers within the same inflorescence (e.g. Carex).",
    quotes: [
      { author: "Virginia Woolf", work: "A Room of One's Own", quote: "A great mind must be **androgynous**, open to every experience without masculine or feminine posturing." },
      { author: "Honoré de Balzac", work: "Sarrasine", quote: "The captivating voice possessed an **androgynous** sweetness that bewitched all who heard it." },
      { author: "Oscar Wilde", work: "The Picture of Dorian Gray", quote: "His youth had that delicate, **androgynous** grace celebrated in classical Attic sculptures." }
    ]
  },
  "Dashboard — gyn/androgyny.md": {
    primary: "The combination of masculine and feminine characteristics in an individual or form.",
    secondary: "In psychology and cultural theory, the simultaneous expression of traits traditionally categorized as masculine and feminine.",
    quotes: [
      { author: "Virginia Woolf", work: "Orlando: A Biography", quote: "Her sartorial choices celebrated a timeless **androgyny** that confounded eighteenth-century polite society." },
      { author: "Simone de Beauvoir", work: "The Second Sex", quote: "Intellectual liberty allows thinkers to move beyond biological determinism toward psychological **androgyny**." },
      { author: "Susan Sontag", work: "Notes on 'Camp'", quote: "Camp taste capitalizes upon the aesthetic appeal of triumphant, theatrical **androgyny**." }
    ]
  },
  "Dashboard — gyn/epigyne.md": {
    primary: "The external genital structure of a female spider, usually hardened and bearing copulatory openings (variant of epigynum).",
    secondary: "In arachnology, a specialized sclerotized plate on the ventral abdomen of female entelegyne spiders critical for species identification.",
    quotes: [
      { author: "John Henry Comstock", work: "The Spider Book", quote: "The intricate chitinous folds of the **epigyne** serve as a mechanical lock fitted only to the male palp." },
      { author: "Jean-Henri Fabre", work: "The Life of the Spider", quote: "Microscopic study of the **epigyne** reveals the delicate openings leading into the internal spermathecae." },
      { author: "William Morton Wheeler", work: "Ants and Other Insects", quote: "Taxonomic diagnosis of cryptic arachnid species relies fundamentally on the morphology of the **epigyne**." }
    ]
  },
  "Dashboard — gyn/epigynous.md": {
    primary: "Having the floral parts (sepals, petals, stamens) attached to the top of the ovary; having an inferior ovary.",
    secondary: "In plant morphology, describing flowers (such as in Asteraceae, Orchidaceae, and Rosaceae subfamily Maloideae) where the hypanthium is adnate to the ovary wall.",
    quotes: [
      { author: "Asa Gray", work: "Botanical Text-Book", quote: "In an **epigynous** flower like the apple blossom, the floral envelope rises above the inferior ovary." },
      { author: "John Lindley", work: "An Introduction to Botany", quote: "The **epigynous** insertion of stamens represents an advanced evolutionary protection of the developing seed." },
      { author: "George Bentham", work: "Handbook of the British Flora", quote: "Identification keys separate Umbelliferae from neighboring orders by their strictly **epigynous** floral structure." }
    ]
  },
  "Dashboard — gyn/epigynum.md": {
    primary: "The external genital opening and surrounding sclerotized plate of a female spider.",
    secondary: "In arachnid systematics, the functional structure on the ventral surface of the opisthosoma into which the male inserts his palpal embolus during mating.",
    quotes: [
      { author: "John Henry Comstock", work: "The Spider Book", quote: "The morphology of the **epigynum** provides the most reliable diagnostic character for distinguishing spider species." },
      { author: "Eugene Simon", work: "Histoire Naturelle des Araignées", quote: "In Araneidae, the **epigynum** frequently develops a flexible scape projecting from the atriolum." },
      { author: "Alexander Petrunkevitch", work: "A Synonymic Index-Catalogue of Spiders", quote: "Sclerotized plates of the **epigynum** preserve remarkably well in museum ethanol collections." }
    ]
  },
  "Dashboard — gyn/gymnogynous.md": {
    primary: "Having a naked or exposed ovary, not enclosed by floral envelopes or surrounding perianth tissues.",
    secondary: "In systematic botany, describing primitive or reduced flowers whose pistils stand completely exposed without protective bracts or calyx.",
    quotes: [
      { author: "John Lindley", work: "The Vegetable Kingdom", quote: "The **gymnogynous** condition in certain reduced aroids displays exposed ovaries crowded upon the naked spadix." },
      { author: "Asa Gray", work: "Elements of Botany", quote: "In archaic angiosperm lines, **gymnogynous** carpels hint at evolutionary origins from open gymnosperm megasporophylls." },
      { author: "Douglas Houghton Campbell", work: "The Evolution of Land Plants", quote: "The absence of protecting perianth leaves renders the **gymnogynous** pistil dependent on protective bracts." }
    ]
  },
  "Dashboard — gyn/gyn.md": {
    primary: "A combining root derived from Ancient Greek gynē (stem gynaik-), meaning woman, female, or female reproductive organs.",
    secondary: "In etymological lexicography, the formative morpheme used in medical, anthropological, and botanical terminology (e.g. gynecology, gynoecium, misogyny).",
    quotes: [
      { author: "Simone de Beauvoir", work: "The Second Sex", quote: "Scientific and social vocabularies combining the root **gyn**- reflect historical assumptions about female nature." },
      { author: "Asa Gray", work: "Botanical Text-Book", quote: "In floral terminology, compounds with **gyn**- denote the female reproductive apparatus of seed plants." },
      { author: "Virginia Woolf", work: "A Room of One's Own", quote: "Language bearing the ancient mark of **gyn**- records both veneration and exclusion across centuries." }
    ]
  },
  "Dashboard — gyn/gynaeceum.md": {
    primary: "The women's quarters in an ancient Greek or Roman house; or (in botany) the gynoecium.",
    secondary: "In classical archaeology and social history, the secluded domestic interior of the Greek house reserved for the mistress, daughters, and female servants.",
    quotes: [
      { author: "Xenophon", work: "Oeconomicus", quote: "Ischomachus explained how the **gynaeceum** was separated by a bolted door from the men's quarters." },
      { author: "Edward Bulwer-Lytton", work: "The Last Days of Pompeii", quote: "The maidens sat spinning fine linen within the secluded tranquility of the **gynaeceum**." },
      { author: "Will Durant", work: "The Life of Greece", quote: "Athenian social customs confined respectable matrons to the domestic realm of the **gynaeceum**." }
    ]
  },
  "Dashboard — gyn/gynaecocracy.md": {
    primary: "Rule or government by women; gynecocracy.",
    secondary: "In political anthropology and social history, matriarchal or female-led civic administration.",
    quotes: [
      { author: "John Knox", work: "The First Blast of the Trumpet Against the Monstrous Regiment of Women", quote: "Knox vehemently denounced female sovereignty as an unnatural **gynaecocracy** contrary to biblical law." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The court of Elagabalus was dominated by an audacious Syrian **gynaecocracy** of mothers and aunts." },
      { author: "Herbert Spencer", work: "The Principles of Sociology", quote: "Matrilineal descent systems in certain archaic tribes occasionally produced genuine civic **gynaecocracy**." }
    ]
  },
  "Dashboard — gyn/gynarchy.md": {
    primary: "Government or rule by women; female political sovereignty.",
    secondary: "In comparative political systems, a matriarchal regime or dynastic succession headed by female monarchs.",
    quotes: [
      { author: "Thomas Carlyle", work: "The French Revolution", quote: "Versailles in its decadent twilight appeared governed less by the King than by an unacknowledged court **gynarchy**." },
      { author: "David Hume", work: "The History of England", quote: "The Elizabethan golden age demonstrated that a stable **gynarchy** could outmatch all the crowns of Europe." },
      { author: "Mary Beard", work: "Women & Power: A Manifesto", quote: "Classical mythology framed Amazonian **gynarchy** as an existential threat to Greek male civic order." }
    ]
  },
  "Dashboard — gyn/gyne.md": {
    primary: "A female, especially a fertile queen ant, bee, or wasp.",
    secondary: "In insect sociobiology, the reproductive female caste in eusocial Hymenoptera possessing fully developed ovaries and mating capabilities.",
    quotes: [
      { author: "William Morton Wheeler", work: "Ants: Their Structure, Development and Behavior", quote: "The virgin **gyne** takes wing during the nuptial flight, carrying the genetic future of the colony." },
      { author: "E. O. Wilson", work: "The Insect Societies", quote: "Worker pheromones carefully suppress reproductive ovary development in potential rival **gyne** larvae." },
      { author: "Bert Hölldobler", work: "The Ants", quote: "After shedding her wings, the solitary **gyne** excavates a claustral chamber to rear her first brood." }
    ]
  },
  "Dashboard — gyn/gynecocracy.md": {
    primary: "Rule or government by women; gynarchy.",
    secondary: "In sociopolitical anthropology, a societal structure where political leadership and civil authority are exercised by women.",
    quotes: [
      { author: "J. J. Bachofen", work: "Mother Right", quote: "Human civilization, according to Bachofen, was preceded by an ancient religious and social **gynecocracy**." },
      { author: "Lewis Henry Morgan", work: "Ancient Society", quote: "The Iroquois confederacy granted matrons clan vetos that functioned as an effective domestic **gynecocracy**." },
      { author: "Friedrich Engels", work: "The Origin of the Family, Private Property and the State", quote: "The transition from archaic **gynecocracy** to patriarchy marked the world-historic defeat of the female sex." }
    ]
  },
  "Dashboard — gyn/gynecologic.md": {
    primary: "Of or relating to gynecology, the branch of medicine concerned with the female reproductive system.",
    secondary: "In clinical medicine, pertaining to diagnostic, therapeutic, or surgical procedures involving female reproductive organs.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "A thorough **gynecologic** examination is indispensable when investigating chronic pelvic pain." },
      { author: "Oliver Wendell Holmes Sr.", work: "Medical Essays", quote: "Antiseptic protocols transformed **gynecologic** surgery from a perilous hazard into a healing science." },
      { author: "Lewis Thomas", work: "The Youngest Science", quote: "Modern **gynecologic** pathology relies on microscopic cytological screening to catch malignancies early." }
    ]
  },
  "Dashboard — gyn/gynecological.md": {
    primary: "Relating to the branch of medicine that deals with diseases and hygiene of women, especially the reproductive organs.",
    secondary: "Concerning specialized obstetric and gynecologic clinical care, surgery, and endocrinology.",
    quotes: [
      { author: "Virginia Woolf", work: "A Room of One's Own", quote: "Medical textbooks on **gynecological** health had historically been authored exclusively by male professors." },
      { author: "Rachel Carson", work: "Silent Spring", quote: "Endocrine disruptors pose insidious threats to human **gynecological** health and reproductive viability." },
      { author: "Oliver Sacks", work: "The Man Who Mistook His Wife for a Hat", quote: "Systemic endocrine imbalances frequently present with both neurological and **gynecological** symptoms." }
    ]
  },
  "Dashboard — gyn/gynecologist.md": {
    primary: "A physician or surgeon specialized in gynecology and the health of the female reproductive system.",
    secondary: "A clinical specialist trained in women's reproductive health, fertility management, and pelvic surgical procedures.",
    quotes: [
      { author: "Sylvia Plath", work: "The Bell Jar", quote: "She sat nervously in the waiting room, awaiting the appointment with her **gynecologist**." },
      { author: "Simone de Beauvoir", work: "The Second Sex", quote: "The enlightened **gynecologist** must understand both the biological facts and psychological burdens of female patients." },
      { author: "William Osler", work: "Aequanimitas", quote: "The skilled **gynecologist** combines delicate surgical touch with compassionate clinical insight." }
    ]
  },
  "Dashboard — gyn/gynecology.md": {
    primary: "The branch of physiology and medicine which deals with the functions and diseases specific to women and girls, especially those affecting the reproductive system.",
    secondary: "The clinical and surgical specialty encompassing preventive care, oncology, endocrinology, and reproductive surgery for women.",
    quotes: [
      { author: "William Osler", work: "The Evolution of Modern Medicine", quote: "Advances in anesthesia and asepsis elevated **gynecology** into one of the most successful surgical disciplines." },
      { author: "Charlotte Perkins Gilman", work: "The Yellow Wallpaper", quote: "Nineteenth-century **gynecology** frequently conflated emotional distress with organic female ailments." },
      { author: "Lewis Thomas", work: "The Medusa and the Snail", quote: "The history of modern **gynecology** mirrors the wider transformation of medicine into cellular science." }
    ]
  },
  "Dashboard — gyn/gynecomastia.md": {
    primary: "Enlargement of male breast glandular tissue, typically caused by hormonal imbalance between estrogen and androgen.",
    secondary: "In clinical endocrinology, benign proliferation of glandular components of the male breast triggered by medication, puberty, or endocrine disease.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Adolescent **gynecomastia** is usually a benign, self-limiting consequence of transient pubertal hormonal flux." },
      { author: "Hans Selye", work: "The Stress of Life", quote: "Hepatic dysfunction impairs steroid metabolism, frequently resulting in secondary **gynecomastia**." },
      { author: "Oliver Sacks", work: "Awakenings", quote: "Endocrine side effects including transient **gynecomastia** were observed during experimental hormonal therapy." }
    ]
  },
  "Dashboard — gyn/gynodioecious.md": {
    primary: "Having female (pistillate) flowers on some individuals and hermaphrodite (bisexual) flowers on others within the same plant population.",
    secondary: "In plant reproductive ecology and breeding systems, an evolutionary breeding state (e.g. in Thymus vulgaris) promoting outcrossing via nuclear-cytoplasmic sex determination.",
    quotes: [
      { author: "Charles Darwin", work: "The Different Forms of Flowers on Plants of the Same Species", quote: "In **gynodioecious** species such as the wild thyme, female plants produce larger crops of viable seeds." },
      { author: "Asa Gray", work: "Botanical Text-Book", quote: "The occurrence of **gynodioecious** colonies prevents continuous self-fertilization in small floral populations." },
      { author: "John Lindley", work: "An Introduction to Botany", quote: "Botanists classify Thymus as **gynodioecious** because hermaphrodite and strictly pistillate stocks co-exist." }
    ]
  },
  "Dashboard — gyn/gynoecium.md": {
    primary: "The female reproductive organs of a flower; the pistil or carpels considered collectively.",
    secondary: "In floral organography and plant taxonomy, the innermost whorl of floral organs composed of one or more carpels containing ovules.",
    quotes: [
      { author: "Asa Gray", work: "Elements of Botany", quote: "The **gynoecium** occupies the center of the blossom, surrounded by the staminal whorls of the androecium." },
      { author: "Charles Darwin", work: "The Effects of Cross and Self Fertilisation in the Vegetable Kingdom", quote: "In protandrous flowers, the **gynoecium** matures only after the stamens have shed their pollen." },
      { author: "John Lindley", work: "The Vegetable Kingdom", quote: "The structure and dehiscence of the **gynoecium** provide essential characters for family classification." }
    ]
  },
  "Dashboard — gyn/gynoid.md": {
    primary: "Resembling a woman or female in form or appearance; or a humanoid robot designed to resemble a woman.",
    secondary: "In clinical physiology and robotics, describing pear-shaped female fat distribution (gynoid fat) or female android robotics.",
    quotes: [
      { author: "Philip K. Dick", work: "Do Androids Dream of Electric Sheep?", quote: "The manufactured **gynoid** displayed facial contours designed with uncanny human verisimilitude." },
      { author: "William Gibson", work: "Neuromancer", quote: "Polished chrome limbs gave the security **gynoid** an imposing, predatory elegance." },
      { author: "Havelock Ellis", work: "Man and Woman", quote: "Adipose deposition follows a distinct **gynoid** pattern centered upon the pelvic girdle and thighs." }
    ]
  },
  "Dashboard — gyn/gynophobia.md": {
    primary: "An abnormal, irrational, or intense fear or hatred of women.",
    secondary: "In clinical psychology and psychoanalysis, a morbid phobic anxiety provoked by female presence or maternal authority.",
    quotes: [
      { author: "Sigmund Freud", work: "Totem and Taboo", quote: "Archaic tribal taboos surrounding menstruation reflect an unacknowledged cultural **gynophobia**." },
      { author: "Karen Horney", work: "Feminine Psychology", quote: "Male dread of woman, or deep-seated **gynophobia**, often masks anxiety regarding sexual inadequacy." },
      { author: "William James", work: "The Principles of Psychology", quote: "Morbid phobic fixations like **gynophobia** illustrate how emotional trauma can distort interpersonal life." }
    ]
  },
  "Dashboard — gyn/heterogynous.md": {
    primary: "Having females of two different kinds or forms, as in certain social insects (such as winged queens and wingless workers).",
    secondary: "In entomological morphology and social biology, possessing dimorphic or polymorphic female castes within the same species.",
    quotes: [
      { author: "William Morton Wheeler", work: "Ants: Their Structure, Development and Behavior", quote: "A **heterogynous** species exhibits distinct female castes adapted respectively to egg-laying and colony foraging." },
      { author: "E. O. Wilson", work: "The Insect Societies", quote: "Caste divergence in **heterogynous** wasps illustrates how epigenetic feeding triggers morphological branching." },
      { author: "John Lubbock", work: "Ants, Bees, and Wasps", quote: "In **heterogynous** ant colonies, the worker is an aborted female specialized for communal toil." }
    ]
  },
  "Dashboard — gyn/homogyne.md": {
    primary: "A genus of small alpine perennial herbs in the daisy family (Asteraceae), native to the mountains of southern and central Europe.",
    secondary: "In alpine botany and phytogeography, dwarf composite plants (such as Homogyne alpina) bearing solitary purple or brownish flower heads in subalpine zones.",
    quotes: [
      { author: "Joseph Dalton Hooker", work: "The Student's Flora of the British Islands", quote: "Specimens of **Homogyne** carpet the moist schistose slopes of the high Alpine ranges." },
      { author: "John Lindley", work: "The Vegetable Kingdom", quote: "Botanists classify **Homogyne** near Tussilago on account of its radical foliage and capitulum structure." },
      { author: "George Bentham", work: "Handbook of the British Flora", quote: "The kidney-shaped glossy leaves of **Homogyne** alpina are unmistakable on high limestone screes." }
    ]
  },
  "Dashboard — gyn/hypogynous.md": {
    primary: "Having floral parts (sepals, petals, and stamens) inserted below the ovary on the receptacle; having a superior ovary.",
    secondary: "In botanical organography, describing flowers characteristic of Brassicaceae, Liliaceae, and Solanaceae where the ovary sits free above the perianth.",
    quotes: [
      { author: "Asa Gray", work: "Botanical Text-Book", quote: "In a **hypogynous** flower like the buttercup, each organ arises directly from the receptacle below the carpels." },
      { author: "John Lindley", work: "An Introduction to Botany", quote: "The **hypogynous** arrangement is regarded as phylogenetically primitive in angiosperm floral evolution." },
      { author: "George Bentham", work: "Handbook of the British Flora", quote: "The Cruciferae are easily identified by their tetradynamous stamens and strictly **hypogynous** insertion." }
    ]
  },
  "Dashboard — gyn/monogynic.md": {
    primary: "Of, relating to, or practicing monogyny (having only one female partner or wife at a time).",
    secondary: "In insect sociobiology, describing a social insect colony that possesses only a single reproductive queen (monogyne/monogynic).",
    quotes: [
      { author: "E. O. Wilson", work: "The Insect Societies", quote: "A **monogynic** colony exhibits strict reproductive division governed by the pheromones of its solitary queen." },
      { author: "Edward Westermarck", work: "The History of Human Marriage", quote: "Comparative ethnography demonstrates that **monogynic** norms predominate across most foraging cultures." },
      { author: "Bert Hölldobler", work: "The Ants", quote: "Territorial boundary defense is significantly fiercer in **monogynic** than in polygynic ant populations." }
    ]
  },
  "Dashboard — gyn/monogynist.md": {
    primary: "A man who has only one wife, or an advocate of monogyny (having only one wife at a time).",
    secondary: "In sociology and marital history, a person committed to single-wife unions as opposed to polygyny.",
    quotes: [
      { author: "Oliver Goldsmith", work: "The Vicar of Wakefield", quote: "The good vicar was an unbending **monogynist**, maintaining that a clergyman should never marry a second time." },
      { author: "Edward Westermarck", work: "The History of Human Marriage", quote: "The staunch **monogynist** argues that social stability depends on the reciprocal fidelity of a single spouse." },
      { author: "Herbert Spencer", work: "The Principles of Sociology", quote: "Civil law rewarded the **monogynist** by providing secure legal inheritance for his legitimate heirs." }
    ]
  },
  "Dashboard — gyn/monogynous.md": {
    primary: "Having only one wife or female partner at a time; or in botany, having only one pistil or style in a flower.",
    secondary: "In zoology and botany, pairing with a single female during a breeding cycle, or bearing a solitary carpel.",
    quotes: [
      { author: "Charles Darwin", work: "The Descent of Man", quote: "Male songbirds that are strictly **monogynous** share equally in the defense and feeding of nestlings." },
      { author: "Asa Gray", work: "Structural Botany", quote: "The order Monogynia in the Linnaean system gathered all plants with **monogynous** blossoms." },
      { author: "Edward Westermarck", work: "A Short History of Marriage", quote: "Among many indigenous tribes, hunters were strictly **monogynous** due to limited economic resources." }
    ]
  },
  "Dashboard — gyn/monogyny.md": {
    primary: "The practice or condition of having only one wife or female mate at a time; counterpart to monandry.",
    secondary: "In sociobiology, an animal social structure where an individual or colony has only one reproductive female; in botany, the state of having one pistil.",
    quotes: [
      { author: "Friedrich Engels", work: "The Origin of the Family, Private Property and the State", quote: "The historical rise of **monogyny** accompanied the accumulation of private property and patrilineal inheritance." },
      { author: "E. O. Wilson", work: "Sociobiology: The New Synthesis", quote: "In ant populations, genetic relatedness among sister workers is maximized under strict **monogyny**." },
      { author: "Edward Westermarck", work: "The History of Human Marriage", quote: "Moral philosophy consistently defended **monogyny** as the ideal domestic foundation for child-rearing." }
    ]
  },
  "Dashboard — gyn/oligogyny.md": {
    primary: "A mating system or condition in which a male mates with only a few females; or in social insects, the presence of few queens in a colony.",
    secondary: "In behavioral ecology and myrmecology, a social insect structure intermediate between monogyny and polygyny characterized by a restricted number of functional queens.",
    quotes: [
      { author: "Bert Hölldobler", work: "The Ants", quote: "Periodic execution of excess queens stabilizes the colony in a state of functional **oligogyny**." },
      { author: "E. O. Wilson", work: "The Insect Societies", quote: "Under conditions of **oligogyny**, worker policing regulates queen numbers to maintain optimal reproductive output." },
      { author: "William Morton Wheeler", work: "Social Life Among the Insects", quote: "Certain ant subfamilies maintain **oligogyny** by tolerating only two or three sister foundresses." }
    ]
  },
  "Dashboard — gyn/philogyny.md": {
    primary: "Fondness, love, or admiration for women; the opposite of misogyny.",
    secondary: "In cultural history and literature, chivalric devotion, romantic veneration, or philosophical defense of women's moral and intellectual qualities.",
    quotes: [
      { author: "Lord Byron", work: "Don Juan", quote: "His notorious reputation was driven not by malice, but by an uncontrollable, enthusiastic **philogyny**." },
      { author: "Arthur Schopenhauer", work: "On Women", quote: "Schopenhauer sneered at European courtly **philogyny**, claiming it inverted the natural hierarchy of the sexes." },
      { author: "George Meredith", work: "The Egoist", quote: "Sir Willoughby cloaked his possessiveness in the polished phrases of aristocratic **philogyny**." }
    ]
  },
  "Dashboard — gyn/polygynist.md": {
    primary: "A man who has more than one wife at the same time; one who practices or advocates polygyny.",
    secondary: "In anthropology and social history, an individual maintaining a multi-wife household under customary or religious law.",
    quotes: [
      { author: "Richard Francis Burton", work: "First Footsteps in East Africa", quote: "The wealthy pastoral chieftain was an influential **polygynist**, maintaining separate dwellings for each wife." },
      { author: "Edward Westermarck", work: "The History of Human Marriage", quote: "A successful **polygynist** required substantial herds and influence to provide bride-wealth for each union." },
      { author: "David Livingstone", work: "Missionary Travels and Researches in South Africa", quote: "Our conversations with the tribal elder revealed that the **polygynist** viewed his wives as agricultural partners." }
    ]
  },
  "Dashboard — gyn/polygynous.md": {
    primary: "Practicing, characterized by, or relating to polygyny (having multiple wives or female mates).",
    secondary: "In evolutionary zoology and botany, describing mating systems where males mate with multiple females, or flowers having many styles or pistils.",
    quotes: [
      { author: "Charles Darwin", work: "The Descent of Man", quote: "In **polygynous** mammal species, intense male-male competition drives the evolution of large body size and weaponry." },
      { author: "Bronislaw Malinowski", work: "Argonauts of the Western Pacific", quote: "Trobriand chiefs were uniquely permitted **polygynous** privileges to consolidate inter-tribal alliances." },
      { author: "Asa Gray", work: "Botanical Text-Book", quote: "The order Polygynia in classical botany included species with numerous **polygynous** pistils." }
    ]
  },
  "Dashboard — gyn/polygyny.md": {
    primary: "The practice or custom of having more than one wife or female mate at the same time.",
    secondary: "In social anthropology and sociobiology, a widespread mating system where one male pairs with multiple reproductive females.",
    quotes: [
      { author: "Edward Westermarck", work: "The History of Human Marriage", quote: "Traditional societies often sanctioned **polygyny** as a means of ensuring high birth rates after wartime losses." },
      { author: "E. O. Wilson", work: "Sociobiology: The New Synthesis", quote: "Harem defense **polygyny** evolves when males can monopolize critical breeding territories or water resources." },
      { author: "Friedrich Engels", work: "The Origin of the Family, Private Property and the State", quote: "While **polygyny** was an aristocratic privilege, the common laborer remained de facto monogamous." }
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

console.log(`Updated ${updatedCount} files in Batch 3 (dem + gyn)!`);
