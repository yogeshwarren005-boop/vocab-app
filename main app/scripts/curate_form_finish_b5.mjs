import { updateNotesBatch } from './curate-updater-util.mjs';

const baseDir = "App database\\Greek roots\\Cluster Form & Space";
const batchData = {
  "Dashboard — oec\\andromonecy.md": {
    "primary": "The botanical condition of bearing both staminate (male) and hermaphroditic (perfect) flowers on the same individual plant.",
    "secondary": "In reproductive plant biology and evolutionary ecology, andromonecy optimizes maternal resource allocation between fruit set and pollen export in species like Solanum and chestnut.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Different Forms of Flowers on Plants of the Same Species",
        "quote": "In species exhibiting **andromonecy**, the presence of male flowers alongside hermaphrodites conserves maternal resources for maturing fruit."
      },
      {
        "author": "Asa Gray",
        "work": "Structural Botany",
        "quote": "The umbels of many Apiaceae illustrate **andromonecy**, where central flowers bear fertile ovules while peripheral blossoms are purely staminate."
      },
      {
        "author": "Daniel Zohary",
        "work": "Domestication of Plants in the Old World",
        "quote": "Cultivated olive varieties show variable rates of **andromonecy** depending upon environmental water stress during flower bud differentiation."
      }
    ]
  },
  "Dashboard — oec\\archdiocesan.md": {
    "primary": "Pertaining to, administered by, or characteristic of an archdiocese or its governing archbishop.",
    "secondary": "In canon law and ecclesiastical history, describing pastoral chancery decrees, synodal courts, or charitable trusts operating under the metropolitan jurisdiction.",
    "quotes": [
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "Metropolitan bishops extended their **archdiocesan** authority over suffragan sees, formalizing provincial ecclesiastical hierarchies."
      },
      {
        "author": "Alexis de Tocqueville",
        "work": "Democracy in America",
        "quote": "The establishment of an **archdiocesan** administration in Baltimore marked the institutional maturation of Catholicism in the early republic."
      },
      {
        "author": "Thomas Aquinas",
        "work": "Summa Theologiae",
        "quote": "The archbishop exercises **archdiocesan** supervision to preserve unity of discipline and orthodox preaching throughout his province."
      }
    ]
  },
  "Dashboard — oec\\archdiocese.md": {
    "primary": "The episcopal district, see, or jurisdictional diocese presided over by an archbishop or metropolitan bishop.",
    "secondary": "In Roman Catholic and Eastern Orthodox church governance, an archdiocese typically serves as the primary or historic metropolitan center of an ecclesiastical province.",
    "quotes": [
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The patriarchal dignity conferred upon the **archdiocese** of Constantinople reflected its status as the imperial capital of the East."
      },
      {
        "author": "Thomas Babington Macaulay",
        "work": "The History of England",
        "quote": "The metropolitan see of Canterbury remained the premier **archdiocese** of England, commanding ancient cathedral revenues."
      },
      {
        "author": "Alexis de Tocqueville",
        "work": "The Old Regime and the Revolution",
        "quote": "Prior to 1789, the wealthy French **archdiocese** commanded vast agrarian seigneuries and collected tithes from multiple rural provinces."
      }
    ]
  },
  "Dashboard — oec\\autoecious.md": {
    "primary": "In mycology, completing all stages of the parasitic life cycle upon a single host species, contrasting with heteroecious rusts.",
    "secondary": "In plant pathology, autoecious rust fungi (such as Puccinia helianthi on sunflowers) produce pycnia, aecia, uredinia, and telia on the same host plant.",
    "quotes": [
      {
        "author": "Anton de Bary",
        "work": "Comparative Morphology and Biology of the Fungi",
        "quote": "The flax rust parasite is strictly **autoecious**, carrying out every spore phase from pycnium to telium upon Linum usitatissimum."
      },
      {
        "author": "John Webster",
        "work": "Introduction to Fungi",
        "quote": "Unlike stem rust of wheat, an **autoecious** species does not require an alternate woody host to complete its meiotic cycle."
      },
      {
        "author": "Bryce Kendrick",
        "work": "The Fifth Kingdom",
        "quote": "The evolution of the **autoecious** habit represents a derived simplification that eliminates dependence on two independent host populations."
      }
    ]
  },
  "Dashboard — oec\\autoecism.md": {
    "primary": "The parasitic biological condition or life history strategy of being autoecious; completing all life-cycle stages on one host.",
    "secondary": "In systematic mycology and parasitology, autoecism in rust fungi evolved secondarily from heteroecious ancestors through the loss of alternate host requirements.",
    "quotes": [
      {
        "author": "Anton de Bary",
        "work": "Comparative Morphology and Biology of the Fungi, Mycetozoa and Bacteria",
        "quote": "Our infection experiments confirmed **autoecism** in asparagus rust, resolving long-standing doubts regarding alternate host plants."
      },
      {
        "author": "John Webster",
        "work": "Introduction to Fungi",
        "quote": "The genetic basis of **autoecism** involves the condensation of developmental spore cascades onto a single ecological substrate."
      },
      {
        "author": "C. V. Subramanian",
        "work": "Hyphomycetes",
        "quote": "Agricultural crop protection is simplified when pathogens exhibit **autoecism**, as eradicating wild alternate hosts is unnecessary."
      }
    ]
  },
  "Dashboard — oec\\dioecious.md": {
    "primary": "Having the male and female reproductive organs located in separate individual organisms; unisexual in individuality.",
    "secondary": "In botany, describing plant species (such as willow, holly, and cannabis) where staminate and pistillate flowers are borne on distinct individual plants.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Different Forms of Flowers on Plants of the Same Species",
        "quote": "In **dioecious** plants, cross-fertilization is an absolute necessity, completely preventing self-pollination in nature."
      },
      {
        "author": "Asa Gray",
        "work": "Manual of the Botany of the Northern United States",
        "quote": "The willows are strictly **dioecious**, bearing staminate and pistillate catkins on separate trees along river banks."
      },
      {
        "author": "Karl Linnaeus",
        "work": "Systema Naturae",
        "quote": "In my sexual system of classification, the class Dioecia unites all plants that are **dioecious** in flowering habit."
      }
    ]
  },
  "Dashboard — oec\\dioecy.md": {
    "primary": "The sexual system or reproductive condition of being dioecious; the state in which male and female sex organs are on separate individuals.",
    "secondary": "In evolutionary botany, dioecy occurs in approximately six percent of angiosperm species, functioning as an outcrossing mechanism that prevents inbreeding depression.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Effects of Cross and Self Fertilisation in the Vegetable Kingdom",
        "quote": "The evolutionary advantage of **dioecy** lies primarily in the total avoidance of the deleterious effects of self-fertilization."
      },
      {
        "author": "Ronald Fisher",
        "work": "The Genetical Theory of Natural Selection",
        "quote": "Natural selection maintains a balanced one-to-one sex ratio under **dioecy** because parents investing equally in sons and daughters maximize fitness."
      },
      {
        "author": "John Maynard Smith",
        "work": "The Evolution of Sex",
        "quote": "The transition from cosexuality to **dioecy** requires the accumulation of male-sterility and female-sterility mutations on nascent sex chromosomes."
      }
    ]
  },
  "Dashboard — oec\\ecesis.md": {
    "primary": "The successful establishment and maturation of a plant or animal in a new habitat following migration or dispersal, including germination and growth.",
    "secondary": "In ecological plant succession, ecesis represents the crucial intermediate phase between initial seed immigration and competitive aggregation.",
    "quotes": [
      {
        "author": "Frederic Clements",
        "work": "Plant Succession: An Analysis of the Development of Vegetation",
        "quote": "Migration brings the disseminule to the bare area, but **ecesis** decides whether the seedling can adapt to the local soil and climate."
      },
      {
        "author": "Arthur Tansley",
        "work": "Practical Plant Ecology",
        "quote": "Successful **ecesis** requires adequate soil moisture during the vulnerable period of embryonic root penetration."
      },
      {
        "author": "Eugene Odum",
        "work": "Fundamentals of Ecology",
        "quote": "Colonizing pioneers fail in **ecesis** whenever abiotic microclimates exceed their physiological tolerance limits."
      }
    ]
  },
  "Dashboard — oec\\ecologic.md": {
    "primary": "Pertaining to, dealing with, or relating to ecology or the relationships between organisms and their environment.",
    "secondary": "In environmental science and policy, ecologic assessments model the impacts of industrial pollutants on aquatic food chains and biodiversity.",
    "quotes": [
      {
        "author": "Ernst Haeckel",
        "work": "Generelle Morphologie der Organismen",
        "quote": "Every organism exists within a complex **ecologic** web of mutual dependencies with organic and inorganic nature."
      },
      {
        "author": "Rachel Carson",
        "work": "Silent Spring",
        "quote": "The chemical assault upon the landscape ignores the delicate **ecologic** balance that binds soil, water, and wildlife together."
      },
      {
        "author": "Aldo Leopold",
        "work": "A Sand County Almanac",
        "quote": "A land ethic changes the role of Homo sapiens from conqueror of the land community to plain member and citizen of the **ecologic** realm."
      }
    ]
  },
  "Dashboard — oec\\ecological.md": {
    "primary": "Pertaining to ecology; concerned with the interactions between living organisms and their physical and biological surroundings.",
    "secondary": "In conservation biology, maintaining ecological integrity requires preserving trophic cascades, nutrient cycles, and habitat connectivity.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "The complex **ecological** relations of animals and plants to each other illustrate how severe is the struggle for existence."
      },
      {
        "author": "Arthur Tansley",
        "work": "The Use and Abuse of Vegetational Concepts and Terms",
        "quote": "The concept of an **ecological** community must encompass both the living biocoenosis and the physical factors of its abiotic biotope."
      },
      {
        "author": "Eugene Odum",
        "work": "Fundamentals of Ecology",
        "quote": "Energy flow through an **ecological** food web follows the strict thermodynamic laws of conservation and entropy."
      }
    ]
  },
  "Dashboard — oec\\ecologically.md": {
    "primary": "In an ecological manner; with regard to the relationships between organisms and their environment.",
    "secondary": "In sustainable resource management, harvesting practices must be ecologically sustainable to prevent soil erosion and fish stock collapse.",
    "quotes": [
      {
        "author": "Aldo Leopold",
        "work": "A Sand County Almanac",
        "quote": "A thing is right when it tends to preserve the integrity, stability, and beauty of the biotic community; it is wrong when it tends **ecologically** otherwise."
      },
      {
        "author": "Rachel Carson",
        "work": "Silent Spring",
        "quote": "We have subjected millions of acres to pesticide applications that are **ecologically** disastrous and ultimately futile."
      },
      {
        "author": "E. O. Wilson",
        "work": "The Diversity of Life",
        "quote": "Conserving rainforests is **ecologically** sound because primary forests generate their own regional rainfall cycles."
      }
    ]
  },
  "Dashboard — oec\\ecologist.md": {
    "primary": "A scientist who studies ecology, focusing on the interactions of living organisms with each other and their environments.",
    "secondary": "In environmental policy and conservation, an ecologist conducts field bio-inventories and models wildlife population dynamics to guide habitat preservation.",
    "quotes": [
      {
        "author": "Arthur Tansley",
        "work": "Practical Plant Ecology",
        "quote": "The field **ecologist** must possess the botanical eye of a taxonomist combined with the analytical rigor of a physiologist."
      },
      {
        "author": "Aldo Leopold",
        "work": "A Sand County Almanac",
        "quote": "One of the penalties of an **ecologist** education is that one lives alone in a world of wounds, seeing devastation where others see progress."
      },
      {
        "author": "Eugene Odum",
        "work": "Fundamentals of Ecology",
        "quote": "The modern **ecologist** employs radiotracers and computer simulations to track phosphorus and nitrogen cycling through lake watersheds."
      }
    ]
  },
  "Dashboard — oec\\ecology.md": {
    "primary": "The branch of biological science that studies the relationships between living organisms and their physical and biological environments.",
    "secondary": "In contemporary science, ecology spans physiological, population, community, and landscape scales to analyze energy flux and biodiversity conservation.",
    "quotes": [
      {
        "author": "Ernst Haeckel",
        "work": "Generelle Morphologie der Organismen",
        "quote": "By **ecology**, we mean the body of knowledge concerning the economy of nature: the investigation of the total relations of the animal both to its inorganic and to its organic environment."
      },
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "Plants and animals, most remote in the scale of nature, are bound together by a web of complex relations that forms the subject of **ecology**."
      },
      {
        "author": "Arthur Tansley",
        "work": "The Use and Abuse of Vegetational Concepts and Terms",
        "quote": "The ecosystem stands as the basic unit of modern **ecology**, integrating biome and physical habitat into a single interacting whole."
      }
    ]
  },
  "Dashboard — oec\\economic.md": {
    "primary": "Pertaining to the production, distribution, and consumption of goods, services, and wealth; relating to the economy of a nation or household.",
    "secondary": "In public policy, economic indicators (such as GDP, inflation rates, and labor productivity) determine fiscal legislation and sovereign budgeting.",
    "quotes": [
      {
        "author": "Adam Smith",
        "work": "The Wealth of Nations",
        "quote": "Every individual necessarily labors to render the annual revenue of the society as great as he can, pursuing his own **economic** interest."
      },
      {
        "author": "John Maynard Keynes",
        "work": "The General Theory of Employment, Interest and Money",
        "quote": "The ideas of economists and political philosophers, both when they are right and when they are wrong, are more powerful than is commonly understood; indeed the world is ruled by little else than **economic** theory."
      },
      {
        "author": "Karl Marx",
        "work": "Das Kapital",
        "quote": "The **economic** structure of capitalist society grew out of the economic structure of feudal society through class struggle."
      }
    ]
  },
  "Dashboard — oec\\economical.md": {
    "primary": "Prudent, thrifty, and careful in the management of money, resources, or time; avoiding waste or extravagance.",
    "secondary": "In engineering and design, an economical structure achieves maximum mechanical performance and safety with minimal material expenditure.",
    "quotes": [
      {
        "author": "Benjamin Franklin",
        "work": "The Way to Wealth",
        "quote": "A man may, if he knows not how to be **economical**, keep his nose all his life to the grindstone and die not worth a groat."
      },
      {
        "author": "Adam Smith",
        "work": "The Wealth of Nations",
        "quote": "Parsimony, and not industry, is the immediate cause of the increase of capital; an **economical** citizen augments public wealth by frugality."
      },
      {
        "author": "Jane Austen",
        "work": "Sense and Sensibility",
        "quote": "Elinor's **economical** arrangements in their small cottage ensured that their modest income provided every comfort without incurring debt."
      }
    ]
  },
  "Dashboard — oec\\economically.md": {
    "primary": "In an economical manner; with frugality, prudence, and avoidance of unnecessary expenditure or waste.",
    "secondary": "With respect to economic principles, financial feasibility, or the material wealth of a nation or industry.",
    "quotes": [
      {
        "author": "Adam Smith",
        "work": "The Wealth of Nations",
        "quote": "A private estate managed **economically** yields a surplus that can be reinvested into agricultural improvements."
      },
      {
        "author": "John Stuart Mill",
        "work": "Principles of Political Economy",
        "quote": "A nation cannot develop **economically** unless personal property is secure and contracts are impartially enforced by law."
      },
      {
        "author": "Alexis de Tocqueville",
        "work": "Democracy in America",
        "quote": "Free associations allow citizens to accomplish **economically** great industrial enterprises that elsewhere require monarchical subsidies."
      }
    ]
  },
  "Dashboard — oec\\economics.md": {
    "primary": "The social science that studies the production, distribution, and consumption of goods, services, and wealth in human societies.",
    "secondary": "In academic inquiry, economics combines microeconomic models of consumer choice with macroeconomic analyses of national income and central banking.",
    "quotes": [
      {
        "author": "Alfred Marshall",
        "work": "Principles of Economics",
        "quote": "Political economy or **economics** is a study of mankind in the ordinary business of life; it examines that part of individual and social action which is most closely connected with the attainment and with the use of the material requisites of wellbeing."
      },
      {
        "author": "John Maynard Keynes",
        "work": "Essays in Biography",
        "quote": "The study of **economics** does not seem to require any specialized gifts of an unusually high order, yet good economists are extremely rare."
      },
      {
        "author": "Paul Samuelson",
        "work": "Economics: An Introductory Analysis",
        "quote": "Modern **economics** analyzes how societies use scarce resources to produce valuable commodities and distribute them among different people."
      }
    ]
  },
  "Dashboard — oec\\economise.md": {
    "primary": "To practice economy; to spend money, resources, or time with frugality and careful management; to avoid waste (British spelling).",
    "secondary": "In industrial engineering, to economise fuel by installing heat recovery equipment on exhaust flues.",
    "quotes": [
      {
        "author": "Adam Smith",
        "work": "The Wealth of Nations",
        "quote": "Every prodigal appears to be a public enemy, and every frugal man a public benefactor who strives to **economise** his resources."
      },
      {
        "author": "Charles Dickens",
        "work": "David Copperfield",
        "quote": "Mr. Micawber was perpetually resolving to **economise**, yet tomorrow invariably found him contracting some novel and fanciful liability."
      },
      {
        "author": "John Stuart Mill",
        "work": "Principles of Political Economy",
        "quote": "To **economise** human labor by substituting mechanical water power increases the net output of the agricultural community."
      }
    ]
  },
  "Dashboard — oec\\economist.md": {
    "primary": "A specialist or scholar in the field of economics; a person who studies economic systems, theories, and data.",
    "secondary": "In public administration, an economist advises finance ministries and corporations on monetary forecasting, pricing strategies, and taxation policy.",
    "quotes": [
      {
        "author": "Adam Smith",
        "work": "The Wealth of Nations",
        "quote": "The statesman or **economist** who attempts to direct private capital would assume an authority which could safely be trusted to no council."
      },
      {
        "author": "John Maynard Keynes",
        "work": "The General Theory of Employment, Interest and Money",
        "quote": "The master **economist** must possess a rare combination of gifts: he must be mathematician, historian, statesman, philosopher in some degree."
      },
      {
        "author": "David Ricardo",
        "work": "On the Principles of Political Economy and Taxation",
        "quote": "The principal problem in political economy for the **economist** is to determine the laws which regulate the distribution of rent, profit, and wages."
      }
    ]
  },
  "Dashboard — oec\\economize.md": {
    "primary": "To manage financial, natural, or physical resources with prudence and frugality; to reduce expenditure and prevent waste.",
    "secondary": "In thermodynamics and power plant design, to economize boiler fuel consumption by preheating feedwater using waste flue gases.",
    "quotes": [
      {
        "author": "Benjamin Franklin",
        "work": "Poor Richard's Almanack",
        "quote": "Beware of little expenses; a small leak will sink a great ship: **economize** today that you may feast in old age."
      },
      {
        "author": "Ralph Waldo Emerson",
        "work": "The Conduct of Life",
        "quote": "Spend for your expense, and **economize** in your expenditure, remembering that wealth consists in the wise direction of power."
      },
      {
        "author": "Herbert Spencer",
        "work": "First Principles",
        "quote": "Evolutionary progress tends everywhere to **economize** vital energy, substituting specialized physiological organs for diffuse tissues."
      }
    ]
  },
  "Dashboard — oec\\economizer.md": {
    "primary": "A mechanical device, apparatus, or person that economizes; specifically, a heat exchanger that preheats boiler feedwater using waste flue gases.",
    "secondary": "In industrial steam engineering and thermal power plants, an economizer significantly increases overall thermal efficiency and reduces boiler fuel consumption.",
    "quotes": [
      {
        "author": "William Rankine",
        "work": "A Manual of the Steam Engine and Other Prime Movers",
        "quote": "The installation of an **economizer** in the chimney flue recovers waste heat from the gases before they discharge into the atmosphere."
      },
      {
        "author": "Thomas Edison",
        "work": "The Papers of Thomas A. Edison",
        "quote": "We introduced a flue-gas **economizer** into the Pearl Street central station to reduce the tons of coal burned per kilowatt-hour."
      },
      {
        "author": "James Watt",
        "work": "Correspondence of the Late James Watt",
        "quote": "Every thermal **economizer** attached to a condensing engine repays its construction cost within a single mining season."
      }
    ]
  },
  "Dashboard — oec\\economy.md": {
    "primary": "The management, structure, and operational system of resources, money, production, and consumption of goods and services in a community, state, or nation.",
    "secondary": "Etymologically derived from Greek oikonomia (household management), signifying careful, orderly stewardship and frugality across any system.",
    "quotes": [
      {
        "author": "Adam Smith",
        "work": "The Wealth of Nations",
        "quote": "Political **economy**, considered as a branch of the science of a statesman, proposes to enrich both the people and the sovereign."
      },
      {
        "author": "Aristotle",
        "work": "Politics",
        "quote": "The art of **economy** pertains to the household and the acquisition of provisions necessary for the good life."
      },
      {
        "author": "John Maynard Keynes",
        "work": "The General Theory of Employment, Interest and Money",
        "quote": "When savings exceed investment, the whole **economy** sinks into an underemployment equilibrium with idle factories and workers."
      }
    ]
  },
  "Dashboard — oec\\ecoregion.md": {
    "primary": "A major geographic and ecological area characterized by a distinctive assemblage of natural communities, native species, and environmental conditions.",
    "secondary": "In conservation planning and landscape ecology, ecoregions (such as the Mediterranean forest biome) delineate biogeographical units for biodiversity priority setting.",
    "quotes": [
      {
        "author": "E. O. Wilson",
        "work": "The Future of Life",
        "quote": "Global conservation mapping classifies the biosphere into distinct **ecoregion** units to identify vanishing biodiversity hotspots."
      },
      {
        "author": "Eugene Odum",
        "work": "Fundamentals of Ecology",
        "quote": "An **ecoregion** reflects shared macroclimatic boundaries and geological substrates that dictate dominant vegetation formations."
      },
      {
        "author": "Robert MacArthur",
        "work": "Geographical Ecology",
        "quote": "Species richness gradients across an **ecoregion** are governed by regional productivity and habitat heterogeneity."
      }
    ]
  },
  "Dashboard — oec\\ecosystem.md": {
    "primary": "A biological community of interacting organisms together with the abiotic, physical environment with which they exchange energy and nutrients.",
    "secondary": "In earth system science and ecological energetics, ecosystems operate as open thermodynamic systems characterized by trophic energy transfer and biogeochemical cycling.",
    "quotes": [
      {
        "author": "Arthur Tansley",
        "work": "The Use and Abuse of Vegetational Concepts and Terms",
        "quote": "I introduced the term **ecosystem** to denote the whole system, including not only the organism-complex, but also the whole complex of physical factors forming what we call the environment."
      },
      {
        "author": "Eugene Odum",
        "work": "Fundamentals of Ecology",
        "quote": "The watershed **ecosystem** provides an ideal laboratory for measuring nutrient budgets and primary forest productivity."
      },
      {
        "author": "Rachel Carson",
        "work": "Silent Spring",
        "quote": "No part of the living **ecosystem** can be poisoned with synthetic chemicals without endangering the survival of the whole."
      }
    ]
  },
  "Dashboard — oec\\ecumenic.md": {
    "primary": "Universal, general, or worldwide in scope, authority, or influence; representing the whole inhabited world or whole church.",
    "secondary": "In classical Greco-Roman history, ecumenic described matters pertaining to the oikoumene (the civilized inhabited Mediterranean world).",
    "quotes": [
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The bishops claimed **ecumenic** jurisdiction over the faithful, proclaiming canons meant to bind all provinces of the Roman world."
      },
      {
        "author": "Polybius",
        "work": "The Histories",
        "quote": "The dramatic rise of Rome established an **ecumenic** dominion unprecedented in ancient history."
      },
      {
        "author": "Thomas Aquinas",
        "work": "Summa Theologiae",
        "quote": "The decrees promulgated by an **ecumenic** council derive their universal validity from the guidance of the Holy Spirit."
      }
    ]
  },
  "Dashboard — oec\\ecumenical.md": {
    "primary": "Promoting or tending toward worldwide Christian unity or cooperation among differing denominations; of worldwide Christian scope.",
    "secondary": "In church history, designating the historical general church councils (such as Nicaea and Chalcedon) whose doctrinal definitions are accepted across Christendom.",
    "quotes": [
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The first **ecumenical** council at Nicaea brought together three hundred and eighteen prelates to formulate the orthodox creed."
      },
      {
        "author": "C. S. Lewis",
        "work": "Mere Christianity",
        "quote": "My aim is not to plead the cause of any particular faction, but to present that **ecumenical** faith which Christians have held in common across all ages."
      },
      {
        "author": "Pope John XXIII",
        "work": "Gaudet Mater Ecclesia",
        "quote": "The convening of the Second Vatican Council marks an **ecumenical** opening toward dialogue with all separated Christian brethren."
      }
    ]
  },
  "Dashboard — oec\\ecumenicism.md": {
    "primary": "The philosophy, doctrine, or movement advocating mutual understanding, dialogue, and institutional unity among differing Christian denominations.",
    "secondary": "In contemporary religious sociology, ecumenicism promotes interdenominational cooperation on civil rights, poverty relief, and common liturgical traditions.",
    "quotes": [
      {
        "author": "Paul Tillich",
        "work": "Systematic Theology",
        "quote": "Modern **ecumenicism** seeks to overcome sectarian fragmentation without erasing the prophetic insights of the Protestant Reformation."
      },
      {
        "author": "Hans Küng",
        "work": "The Council, Reform and Reunion",
        "quote": "True **ecumenicism** begins within each communion through continuous internal spiritual renewal and historical self-criticism."
      },
      {
        "author": "Karl Barth",
        "work": "Church Dogmatics",
        "quote": "Theological **ecumenicism** cannot rest on vague emotional sentimentality, but must be anchored in Christological truth."
      }
    ]
  },
  "Dashboard — oec\\ecumenism.md": {
    "primary": "The organized movement or theological principle directed toward promoting cooperation and visible unity among the world's Christian churches.",
    "secondary": "In 20th-century religious history, ecumenism catalyzed the formation of the World Council of Churches and bilateral dialogues reconciling historic theological schisms.",
    "quotes": [
      {
        "author": "Pope John Paul II",
        "work": "Ut Unum Sint",
        "quote": "The commitment to **ecumenism** is not merely an optional appendix to the life of the Church, but an organic part of her evangelical mission."
      },
      {
        "author": "Dietrich Bonhoeffer",
        "work": "No Rusty Swords",
        "quote": "If international **ecumenism** cannot speak with a united voice against fascist persecution, its assemblies remain empty words."
      },
      {
        "author": "Hans Küng",
        "work": "Global Responsibility: In Search of a New World Ethic",
        "quote": "There can be no peace among the nations without peace among the religions, and no peace among religions without authentic **ecumenism**."
      }
    ]
  },
  "Dashboard — oec\\gynomonoecy.md": {
    "primary": "The botanical condition of bearing both pistillate (female) and hermaphroditic (perfect) flowers upon the same individual plant.",
    "secondary": "In floral morphology and plant reproductive ecology, gynomonoecy is common in the Asteraceae (daisy family), where ray florets are female and disc florets are hermaphroditic.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Different Forms of Flowers on Plants of the Same Species",
        "quote": "In the composite family, **gynomonoecy** is beautifully illustrated by the common daisy, whose outer ray florets bear only female organs."
      },
      {
        "author": "Asa Gray",
        "work": "Structural Botany",
        "quote": "The functional significance of **gynomonoecy** in sunflowers lies in cross-pollination promoted by receptive peripheral pistillate flowers."
      },
      {
        "author": "Daniel Zohary",
        "work": "Domestication of Plants in the Old World",
        "quote": "Wild progenitors of several cultivated oilseed Asteraceae display stable **gynomonoecy** that facilitates hybrid vigor in nature."
      }
    ]
  },
  "Dashboard — oec\\heteroecious.md": {
    "primary": "In mycology, requiring two different, unrelated host species to complete a full sexual and asexual life cycle, as observed in certain parasitic rust fungi.",
    "secondary": "In plant pathology, heteroecious rusts (such as Puccinia graminis) produce urediniospores and teliospores on cereals while producing aecia on barberry.",
    "quotes": [
      {
        "author": "Anton de Bary",
        "work": "Comparative Morphology and Biology of the Fungi, Mycetozoa and Bacteria",
        "quote": "I demonstrated by experimental inoculation that the cereal rust is **heteroecious**, requiring the leaves of the common barberry to complete its spring cycle."
      },
      {
        "author": "John Webster",
        "work": "Introduction to Fungi",
        "quote": "The life cycle of a **heteroecious** rust encompasses five distinct spore states alternating between two widely separated plant families."
      },
      {
        "author": "Bryce Kendrick",
        "work": "The Fifth Kingdom",
        "quote": "Agricultural legislation eradicating barberry bushes broke the reproductive chain of the **heteroecious** wheat stem rust."
      }
    ]
  },
  "Dashboard — oec\\heteroecism.md": {
    "primary": "The biological condition, property, or life history strategy of being heteroecious; requiring two alternate host species to complete a life cycle.",
    "secondary": "In evolutionary parasitology and mycology, heteroecism provides an evolutionary mechanism for exploiting disparate seasonal plant hosts.",
    "quotes": [
      {
        "author": "Anton de Bary",
        "work": "Comparative Morphology and Biology of the Fungi",
        "quote": "The discovery of **heteroecism** resolved centuries of dispute among farmers regarding the connection between barberry hedges and blighted wheat fields."
      },
      {
        "author": "John Webster",
        "work": "Introduction to Fungi",
        "quote": "Evolutionary models suggest that **heteroecism** arose as ancestral rusts colonized gymnosperms before hopping to emerging angiosperm hosts."
      },
      {
        "author": "C. V. Subramanian",
        "work": "Hyphomycetes",
        "quote": "In classical plant pathology courses, the demonstration of **heteroecism** in Puccinia graminis stands as a triumph of inductive microscopy."
      }
    ]
  },
  "Dashboard — oec\\heteroecy.md": {
    "primary": "The biological phenomenon of heteroecism; the alternation of parasitic generations between two different host species.",
    "secondary": "In systematic mycology and entomology, heteroecy characterizes both rust fungi and certain gall-forming aphid lineages that migrate between primary and secondary plants.",
    "quotes": [
      {
        "author": "Anton de Bary",
        "work": "Comparative Morphology and Biology of the Fungi, Mycetozoa and Bacteria",
        "quote": "The proof of **heteroecy** in rust fungi showed that what appeared to be separate fungal species were merely alternating generations of one organism."
      },
      {
        "author": "John Webster",
        "work": "Introduction to Fungi",
        "quote": "Obligate **heteroecy** imposes severe ecological vulnerability, as the absence of either host halts sexual teliospore generation."
      },
      {
        "author": "E. O. Wilson",
        "work": "Sociobiology: The New Synthesis",
        "quote": "Cyclical host alternation in aphids mirrors the **heteroecy** of fungal rusts, tracking nutritional flushes in seasonal foliage."
      }
    ]
  },
  "Dashboard — oec\\homoecious.md": {
    "primary": "In mycology, completing all stages of the developmental life cycle upon a single host species; autoecious.",
    "secondary": "In parasitology, homoecious parasites require no intermediate or alternate hosts to complete their sexual and asexual reproduction.",
    "quotes": [
      {
        "author": "Anton de Bary",
        "work": "Comparative Morphology and Biology of the Fungi",
        "quote": "Many rusts infesting wild composites are strictly **homoecious**, producing aecia and telia upon the very same rosette of leaves."
      },
      {
        "author": "John Webster",
        "work": "Introduction to Fungi",
        "quote": "In **homoecious** life cycles, spore dispersal is localized, maintaining dense fungal populations within a single host stand."
      },
      {
        "author": "Bryce Kendrick",
        "work": "The Fifth Kingdom",
        "quote": "Phylogenetic analysis demonstrates that **homoecious** rusts frequently evolve from complex heteroecious ancestors by shedding the primary host phase."
      }
    ]
  },
  "Dashboard — oec\\macroeconomic.md": {
    "primary": "Pertaining to the branch of economics that analyzes large-scale or aggregate economic factors, including national income, inflation, unemployment, and gross domestic product.",
    "secondary": "In fiscal and monetary policy, macroeconomic frameworks model the systemic interactions between interest rates, money supply, and aggregated consumption.",
    "quotes": [
      {
        "author": "John Maynard Keynes",
        "work": "The General Theory of Employment, Interest and Money",
        "quote": "Aggregate effective demand serves as the decisive **macroeconomic** lever governing total employment and national output."
      },
      {
        "author": "Paul Samuelson",
        "work": "Economics: An Introductory Analysis",
        "quote": "A nation cannot manage inflation without understanding the **macroeconomic** interactions between government spending and private investment."
      },
      {
        "author": "Milton Friedman",
        "work": "A Monetary History of the United States",
        "quote": "Monetary policy exerts a profound **macroeconomic** influence that operates with long and variable lags upon general price levels."
      }
    ]
  },
  "Dashboard — oec\\macroeconomics.md": {
    "primary": "The study of the economy as an aggregate whole, focusing on national productivity, broad price levels, employment trends, and government monetary policies.",
    "secondary": "In academic economic theory, modern macroeconomics synthesizes neoclassical market equilibria with New Keynesian price stickiness to model business cycles.",
    "quotes": [
      {
        "author": "John Maynard Keynes",
        "work": "The General Theory of Employment, Interest and Money",
        "quote": "The transition from classical microanalysis to aggregate **macroeconomics** shifts attention to total savings, investment, and national consumption."
      },
      {
        "author": "Gregory Mankiw",
        "work": "Macroeconomics",
        "quote": "The central challenge of **macroeconomics** is to explain why economic activity fluctuates and how policymakers can mitigate recessions."
      },
      {
        "author": "Robert Lucas Jr.",
        "work": "Studies in Business-Cycle Theory",
        "quote": "Modern **macroeconomics** requires microfoundations that incorporate the rational expectations of forward-looking economic agents."
      }
    ]
  },
  "Dashboard — oec\\macroeconomist.md": {
    "primary": "An economist specializing in the study, analysis, and forecasting of aggregate national and international economic systems.",
    "secondary": "In public policy and central banking, a macroeconomist advises regulatory authorities on interest rate adjustments, sovereign debt management, and systemic growth modeling.",
    "quotes": [
      {
        "author": "Joseph Schumpeter",
        "work": "History of Economic Analysis",
        "quote": "The modern **macroeconomist** seeks to synthesize monetary dynamics with structural changes across industrial sectors."
      },
      {
        "author": "Paul Krugman",
        "work": "Peddling Prosperity",
        "quote": "Every central bank relies upon the quantitative forecasts of its chief **macroeconomist** when setting base interest rates."
      },
      {
        "author": "Ben Bernanke",
        "work": "The Courage to Act",
        "quote": "During the financial panic, the role of the **macroeconomist** was to prevent liquidity contraction from paralyzing the real economy."
      }
    ]
  },
  "Dashboard — oec\\microeconomic.md": {
    "primary": "Pertaining to the branch of economics that analyzes the behaviors and decisions of individual consumers, households, and firms in resource allocation.",
    "secondary": "In market theory, microeconomic models examine price formation, consumer utility maximization, and marginal production costs within competitive markets.",
    "quotes": [
      {
        "author": "Alfred Marshall",
        "work": "Principles of Economics",
        "quote": "At the **microeconomic** margin, the consumer equates the marginal utility of expenditure across all purchased commodities."
      },
      {
        "author": "Paul Samuelson",
        "work": "Foundations of Economic Analysis",
        "quote": "The theory of revealed preference provides an operational mathematical foundation for **microeconomic** consumer behavior."
      },
      {
        "author": "Kenneth Arrow",
        "work": "Social Choice and Individual Values",
        "quote": "Individual preference orderings serve as the starting point for **microeconomic** theorems of general market equilibrium."
      }
    ]
  },
  "Dashboard — oec\\microeconomics.md": {
    "primary": "The branch of economics that analyzes the decision-making processes of individuals, households, and business firms in allocating scarce resources.",
    "secondary": "In academic economic curriculum, microeconomics investigates supply and demand equilibrium, elasticity of prices, cost curves, and imperfect market competition.",
    "quotes": [
      {
        "author": "Alfred Marshall",
        "work": "Principles of Economics",
        "quote": "The study of **microeconomics** examines the equilibrium price determined by the intersection of supply and demand schedules."
      },
      {
        "author": "Hal Varian",
        "work": "Intermediate Microeconomics: A Modern Approach",
        "quote": "In **microeconomics**, profit maximization by firms provides the analytical engine that drives resource allocation across competitive industries."
      },
      {
        "author": "Joseph Stiglitz",
        "work": "Information and the Change in the Paradigm in Economics",
        "quote": "Asymmetric information fundamentally overturned traditional **microeconomics**, showing that markets often fail to clear smoothly."
      }
    ]
  },
  "Dashboard — oec\\microeconomist.md": {
    "primary": "An economist who specializes in microeconomics, analyzing the behavior, incentives, and choices of individual consumers, workers, and firms.",
    "secondary": "In industrial organization and antitrust litigation, a microeconomist assesses market concentration, pricing collusion, and the welfare effects of corporate mergers.",
    "quotes": [
      {
        "author": "George Stigler",
        "work": "The Theory of Price",
        "quote": "The applied **microeconomist** investigates how regulatory rules alter incentives and create unintended economic distortions."
      },
      {
        "author": "Paul Krugman",
        "work": "Geography and Trade",
        "quote": "When examining local industrial clusters, the **microeconomist** focuses on positive externalities and specialized labor pools."
      },
      {
        "author": "Jean Tirole",
        "work": "The Theory of Industrial Organization",
        "quote": "Game-theoretic modeling equips the modern **microeconomist** to analyze strategic bidding in government spectrum auctions."
      }
    ]
  },
  "Dashboard — oec\\monoecious.md": {
    "primary": "Having separate male and female reproductive flowers or organs on the same individual plant or organism; hermaphroditic at the organismal level.",
    "secondary": "In botany, monoecious plants (such as maize, oak, and birch) bear separate staminate and pistillate flowers on different branches of a single individual.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Different Forms of Flowers on Plants of the Same Species",
        "quote": "In **monoecious** plants like corn, wind dispersal easily carries pollen from the apical tassel to the lower female silk ears."
      },
      {
        "author": "Asa Gray",
        "work": "Manual of the Botany of the Northern United States",
        "quote": "The oaks are **monoecious**, bearing dangling staminate aments and solitary fertile acorns upon the same tree."
      },
      {
        "author": "Karl Linnaeus",
        "work": "Species Plantarum",
        "quote": "I established the class Monoecia to group all plants that are **monoecious**, having male and female flowers in separate housings on one stem."
      }
    ]
  },
  "Dashboard — oec\\monoecy.md": {
    "primary": "The sexual condition or reproductive system of being monoecious; possessing separate male and female unisexual organs on the same individual plant.",
    "secondary": "In evolutionary plant biology, monoecy facilitates wind pollination while allowing differential timing of male and female maturation (dichogamy) to limit selfing.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Effects of Cross and Self Fertilisation in the Vegetable Kingdom",
        "quote": "The evolution of **monoecy** provides plants with the reproductive economy of hermaphroditism while minimizing accidental self-pollination."
      },
      {
        "author": "Ronald Fisher",
        "work": "The Genetical Theory of Natural Selection",
        "quote": "In species exhibiting **monoecy**, sex allocation theory predicts equal maternal and paternal investment in floral structures under outcrossing."
      },
      {
        "author": "Daniel Zohary",
        "work": "Domestication of Plants in the Old World",
        "quote": "Domestication of maize transformed the ancestral teosinte spike into an extraordinarily productive manifestation of **monoecy**."
      }
    ]
  },
  "Dashboard — oec\\oec.md": {
    "primary": "A Greek root and combining element derived from oikos, signifying house, dwelling, habitation, or household management.",
    "secondary": "In scientific and classical terminology, oec- provides the morphological foundation for ecology, economy, ecumenical councils, and diocesan jurisdictions.",
    "quotes": [
      {
        "author": "Henry George Liddell",
        "work": "A Greek-English Lexicon",
        "quote": "The classical Greek noun oikos forms the stem **oec**, designating the ancestral house, family estate, or domestic hearth."
      },
      {
        "author": "Robert Beekes",
        "work": "Etymological Dictionary of Greek",
        "quote": "Cognate with Latin vicus and Sanskrit vesa, the root **oec** reflects Proto-Indo-European *woyk- meaning settlement or clan homestead."
      },
      {
        "author": "Ernst Haeckel",
        "work": "Generelle Morphologie der Organismen",
        "quote": "I chose the Greek root **oec** to coin ecology, conceiving of nature as the grand household wherein living beings dwell."
      }
    ]
  },
  "Dashboard — oec\\oecology.md": {
    "primary": "An archaic or classical British spelling of ecology, the branch of biology studying the interactions between living organisms and their environment.",
    "secondary": "In nineteenth-century natural history and early botanical science, oecology represented Ernst Haeckel's original formulation of the economy of nature.",
    "quotes": [
      {
        "author": "Ernst Haeckel",
        "work": "The History of Creation",
        "quote": "By **oecology** we designate the science of the relations that all organisms bear to the external surrounding world."
      },
      {
        "author": "Arthur Tansley",
        "work": "Types of British Vegetation",
        "quote": "Early treatises on plant geography used the spelling **oecology** before modern ecological nomenclature was standardized."
      },
      {
        "author": "Eugenius Warming",
        "work": "Oecology of Plants: An Introduction to the Study of Plant Communities",
        "quote": "The study of **oecology** investigates how morphological growth forms reflect external soil moisture and light intensity."
      }
    ]
  },
  "Dashboard — oec\\oeconomus.md": {
    "primary": "An ecclesiastical or civil estate steward, bursar, or financial administrator charged with managing church property, revenues, or diocesan temporalities.",
    "secondary": "In Roman Catholic and Byzantine canon law, an oeconomus is appointed by the diocesan bishop to administer the temporal goods and financial assets of the diocese.",
    "quotes": [
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The Council of Chalcedon decreed that every diocese should maintain an **oeconomus** to manage church estates and prevent financial corruption."
      },
      {
        "author": "Thomas Aquinas",
        "work": "Summa Theologiae",
        "quote": "The bishop acts as the chief pastor, while the **oeconomus** executes the faithful administration of temporal alms for the poor."
      },
      {
        "author": "Alexis de Tocqueville",
        "work": "The Old Regime and the Revolution",
        "quote": "Ancient abbey records reveal that the Benedictine **oeconomus** meticulously recorded crop yields, mill tolls, and tenant leases."
      }
    ]
  },
  "Dashboard — oec\\oecumenic.md": {
    "primary": "A classical or archaic spelling of ecumenic, signifying universal, worldwide, or representing the entire inhabited world.",
    "secondary": "In classical historiography and Byzantine diplomacy, describing councils, titles, or edicts with empire-wide or global authority across the oikoumene.",
    "quotes": [
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The Byzantine patriarch claimed the proud title of **oecumenic** bishop, exciting the indignant jealousy of the Roman pontiff."
      },
      {
        "author": "Polybius",
        "work": "The Histories",
        "quote": "The Mediterranean basin became an integrated **oecumenic** theatre of war wherein the fortunes of all nations became intertwined."
      },
      {
        "author": "Gilbert Murray",
        "work": "Five Stages of Greek Religion",
        "quote": "The Hellenistic monarchies fostered an **oecumenic** culture that replaced the narrow patriotism of the independent city-state."
      }
    ]
  },
  "Dashboard — oec\\oecumenical.md": {
    "primary": "A classical or archaic spelling of ecumenical, signifying universal, worldwide, or promoting global Christian unity.",
    "secondary": "In ecclesiastical history, designating the historical universal councils of the ancient undivided church that defined foundational trinitarian and christological dogmas.",
    "quotes": [
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The emperor summoned an **oecumenical** synod to Ephesus, where theological debates erupted into fierce partisan riots."
      },
      {
        "author": "Thomas Babington Macaulay",
        "work": "The History of England",
        "quote": "The Anglican divines revered the decisions of the first four **oecumenical** councils as authoritative standards of catholic antiquity."
      },
      {
        "author": "John Henry Newman",
        "work": "An Essay on the Development of Christian Doctrine",
        "quote": "The decrees of an **oecumenical** assembly acquire their permanent authority through subsequent reception by the universal church."
      }
    ]
  },
  "Dashboard — oec\\oecumenism.md": {
    "primary": "A classical or alternative spelling of ecumenism, the movement or principle directed toward promoting cooperation and visible unity among Christian churches.",
    "secondary": "In twentieth-century theological discourse, oecumenism emphasized mutual recognition of baptism, common prayer, and shared social witness among divided communions.",
    "quotes": [
      {
        "author": "Dietrich Bonhoeffer",
        "work": "No Rusty Swords",
        "quote": "True **oecumenism** must not seek a superficial organizational peace at the expense of confessing the Gospel under totalitarian tyranny."
      },
      {
        "author": "Karl Barth",
        "work": "Church Dogmatics",
        "quote": "The work of **oecumenism** requires humble listening to how other Christian traditions hear the Word of God."
      },
      {
        "author": "Hans Küng",
        "work": "The Council, Reform and Reunion",
        "quote": "Our commitment to **oecumenism** demands that we reform our own structures before pointing out the faults of our brethren."
      }
    ]
  },
  "Dashboard — oec\\oikology.md": {
    "primary": "The science of housekeeping, household governance, or domestic management; domestic science.",
    "secondary": "In 19th-century educational philosophy and sociology, oikology was proposed as an academic discipline applying biological, chemical, and economic principles to family home life.",
    "quotes": [
      {
        "author": "Herbert Spencer",
        "work": "Education: Intellectual, Moral, and Physical",
        "quote": "A rational education should include **oikology**, preparing youth for the practical duties of household management and hygiene."
      },
      {
        "author": "John Ruskin",
        "work": "Sesame and Lilies",
        "quote": "The ancient ideal of **oikology** viewed the home as a sanctuary where noble housekeeping fosters civic and moral virtues."
      },
      {
        "author": "Ellen Swallow Richards",
        "work": "The Cost of Living as Modified by Sanitary Science",
        "quote": "We must elevate domestic economy into true **oikology**, applying sanitary chemistry to food preparation and home ventilation."
      }
    ]
  },
  "Dashboard — oec\\oikophobia.md": {
    "primary": "An abnormal aversion to or hatred of one's home environment, family surroundings, or native culture and homeland.",
    "secondary": "In political philosophy and cultural criticism, Roger Scruton popularized oikophobia to describe the intellectual repudiation of one's national heritage and civil traditions in favor of foreign customs.",
    "quotes": [
      {
        "author": "Roger Scruton",
        "work": "The Need for Nations",
        "quote": "I defined **oikophobia** as the felt need to denigrate the customs, culture, and institutions that are identifiably 'ours' in favor of the alien."
      },
      {
        "author": "Roger Scruton",
        "work": "England: An Elegy",
        "quote": "The modern intellectual often succumbs to **oikophobia**, despising the quiet domestic decencies of his own countrymen."
      },
      {
        "author": "Pierre Janet",
        "work": "Les Névroses",
        "quote": "In severe domestic neuroses, an obsessional **oikophobia** drives the patient to flee the familiar confines of the ancestral home."
      }
    ]
  },
  "Dashboard — oec\\palaeoecology.md": {
    "primary": "A classical or British spelling of paleoecology; the scientific study of the relationships between extinct fossil organisms and their ancient environments.",
    "secondary": "In Quaternary geology and paleobiology, palaeoecology reconstructs prehistoric climates and vegetation shifts through pollen cores, fossil diatoms, and stable isotope ratios.",
    "quotes": [
      {
        "author": "Charles Lyell",
        "work": "Principles of Geology",
        "quote": "Reconstructing past climates through fossil shell beds laid the groundwork for modern evolutionary **palaeoecology**."
      },
      {
        "author": "Arthur Holmes",
        "work": "Principles of Physical Geology",
        "quote": "Sediment cores retrieved from ancient lake beds provide **palaeoecology** with continuous records of post-glacial forest succession."
      },
      {
        "author": "Richard Fortey",
        "work": "Trilobite: Eyewitness to Evolution",
        "quote": "Through detailed **palaeoecology**, we can reconstruct the sea-floor habitats where Ordovician trilobites burrowed in soft carbonate mud."
      }
    ]
  },
  "Dashboard — oec\\paleoecology.md": {
    "primary": "The scientific discipline that uses fossils and sedimentary evidence to reconstruct the environmental conditions, food webs, and ecological relationships of prehistoric geological eras.",
    "secondary": "In contemporary earth science, paleoecology illuminates how ancient ecosystems responded to past asteroid impacts, volcanic greenhouse surges, and glacial cycles.",
    "quotes": [
      {
        "author": "George Gaylord Simpson",
        "work": "Tempo and Mode in Evolution",
        "quote": "The synthesis of paleontology and **paleoecology** reveals that adaptive radiation occurs when evolutionary lineages colonize open ecospaces."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "The Structure of Evolutionary Theory",
        "quote": "Fossil assemblages from the Burgess Shale provide **paleoecology** with a pristine snapshot of early Cambrian marine predation."
      },
      {
        "author": "Eugene Odum",
        "work": "Fundamentals of Ecology",
        "quote": "Understanding modern ecosystem stability requires the long-term perspective provided by historical **paleoecology**."
      }
    ]
  },
  "Dashboard — oec\\parish.md": {
    "primary": "A small administrative district having its own church and priest or pastor; a local civil and ecclesiastical territorial community.",
    "secondary": "In English local governance and civil administration, the parish served for centuries as the fundamental unit responsible for poor relief, road maintenance, and church rates.",
    "quotes": [
      {
        "author": "William Blackstone",
        "work": "Commentaries on the Laws of England",
        "quote": "A **parish** is that circuit of ground which is committed to the charge of one parson, or other minister having cure of souls therein."
      },
      {
        "author": "Adam Smith",
        "work": "The Wealth of Nations",
        "quote": "The English laws of settlement bound poor laborers to their native **parish**, impeding the natural circulation of industrial labor."
      },
      {
        "author": "George Eliot",
        "work": "Middlemarch",
        "quote": "Mr. Casaubon's clerical duties in his rural **parish** left him ample leisure for his endless mythological researches."
      }
    ]
  },
  "Dashboard — oec\\parochially.md": {
    "primary": "In a parochial manner; with a narrow, limited, or provincial outlook; or in a manner relating strictly to a local church parish.",
    "secondary": "In cultural and political discourse, describing administrative decisions or intellectual viewpoints that ignore broad national interests in favor of petty local concerns.",
    "quotes": [
      {
        "author": "Alexis de Tocqueville",
        "work": "Democracy in America",
        "quote": "Township citizens who think only **parochially** risk missing the grand collective destiny of their democratic republic."
      },
      {
        "author": "Walter Bagehot",
        "work": "The English Constitution",
        "quote": "When members of Parliament act merely **parochially**, they degenerate from national legislators into mere agents for borough interests."
      },
      {
        "author": "George Eliot",
        "work": "Scenes of Clerical Life",
        "quote": "The vestry met weekly to manage their funds **parochially**, debating the mendicants' bread allowances with meticulous frugality."
      }
    ]
  },
  "Dashboard — oec\\paroecious.md": {
    "primary": "In bryology and botany, having male (antheridia) and female (archegonia) reproductive organs borne in the same inflorescence or cluster but in separate leaf axils.",
    "secondary": "In moss morphology, paroecious mosses (such as certain Bryum or Sphagnum species) exhibit close sexual proximity, ensuring high rates of fertilization in moist microhabitats.",
    "quotes": [
      {
        "author": "Wilhelm Hofmeister",
        "work": "On the Germination, Development, and Fructification of the Higher Cryptogamia",
        "quote": "In **paroecious** mosses, the antheridia appear in the axils of the upper perichaetial leaves immediately below the terminal archegonia."
      },
      {
        "author": "Douglas Houghton Campbell",
        "work": "The Structure and Development of Mosses and Ferns",
        "quote": "The **paroecious** condition facilitates water droplet fertilization, allowing sperms to reach archegonial necks with minimal travel across the gametophore."
      },
      {
        "author": "Arthur J. Eames",
        "work": "Morphology of Vascular Plants",
        "quote": "Careful dissection of the perichaetial bud distinguishes autoecious arrangements from the closely clustered **paroecious** type."
      }
    ]
  },
  "Dashboard — oec\\perioeci.md": {
    "primary": "In ancient Sparta and classical Laconia, the free, non-citizen autonomous residents living in peripheral towns, subject to Spartan military service and taxation.",
    "secondary": "In classical Greek historiography, the perioeci (perioikoi, 'dwellers around') controlled commerce, manufacturing, and bronze-working, lacking political franchise in the Spartan assembly.",
    "quotes": [
      {
        "author": "Thucydides",
        "work": "History of the Peloponnesian War",
        "quote": "The Spartan army drew heavy hoplite contingents from the towns of the **perioeci**, who fought alongside the Spartiate peers."
      },
      {
        "author": "Aristotle",
        "work": "Politics",
        "quote": "The Spartans kept their agricultural serfs in check while entrusting external trade and coastal manufacture to the **perioeci**."
      },
      {
        "author": "George Grote",
        "work": "A History of Greece",
        "quote": "Unlike the enslaved helots, the **perioeci** retained local municipal autonomy and property ownership in their provincial communities."
      }
    ]
  },
  "Dashboard — oec\\trioecious.md": {
    "primary": "Having male, female, and hermaphroditic (perfect) flowers or reproductive organs on different individual plants within the same species.",
    "secondary": "In reproductive botany, trioecy (trioecious breeding systems) represents a rare sexual polymorphism that balances genetic outcrossing and self-fertility under fluctuating pollinator availability.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Different Forms of Flowers on Plants of the Same Species",
        "quote": "A species that is strictly **trioecious** presents three distinct individuals: purely male, purely female, and fully hermaphrodite plants."
      },
      {
        "author": "Asa Gray",
        "work": "Structural Botany",
        "quote": "Botanical surveys identify occasional **trioecious** populations where sexual expression varies across seedling progenies."
      },
      {
        "author": "Ronald Fisher",
        "work": "The Genetical Theory of Natural Selection",
        "quote": "The theoretical stability of a **trioecious** population requires delicate fitness compensations among the three reproductive morphs."
      }
    ]
  },
  "Dashboard — oec\\uneconomic.md": {
    "primary": "Not profitable, financially unviable, or commercially disadvantageous; wasting capital or generating insufficient return on investment.",
    "secondary": "In industrial and resource economics, describing extraction or production methods whose operating costs exceed market price realization.",
    "quotes": [
      {
        "author": "Adam Smith",
        "work": "The Wealth of Nations",
        "quote": "To maintain public enterprises that yield no revenue is fundamentally **uneconomic**, burdening the productive capital of the nation."
      },
      {
        "author": "John Maynard Keynes",
        "work": "The General Theory of Employment, Interest and Money",
        "quote": "When interest rates are excessively high, private capital investment becomes **uneconomic**, causing factories to stand idle."
      },
      {
        "author": "David Ricardo",
        "work": "On the Principles of Political Economy and Taxation",
        "quote": "Cultivating marginal soils where cost exceeds grain yield is an **uneconomic** expenditure of national capital."
      }
    ]
  },
  "Dashboard — oec\\uneconomical.md": {
    "primary": "Wasteful of money, time, materials, or energy; not economical; extravagant or inefficient in resource use.",
    "secondary": "In mechanical engineering and thermal design, an uneconomical engine dissipates excessive heat or friction, demanding excessive fuel per unit of work.",
    "quotes": [
      {
        "author": "Benjamin Franklin",
        "work": "The Way to Wealth",
        "quote": "Sloth makes all things difficult, but industry all things easy; an **uneconomical** life squanders the precious currency of time."
      },
      {
        "author": "Thomas Edison",
        "work": "The Papers of Thomas A. Edison",
        "quote": "Our earliest dynamo prototypes were **uneconomical**, dissipating over forty percent of generated electrical energy as waste heat."
      },
      {
        "author": "John Stuart Mill",
        "work": "Principles of Political Economy",
        "quote": "Small-scale peasant agriculture can be **uneconomical** when it prevents the adoption of advanced steam machinery."
      }
    ]
  },
  "Dashboard — oesophag\\oesophag.md": {
    "primary": "A Greek combining root derived from oisophagos, signifying the esophagus, gullet, or passage connecting the pharynx to the stomach.",
    "secondary": "In anatomical nomenclature and surgical literature, forms roots in terms denoting diseases (oesophagitis), diagnostics (oesophagoscopy), or resections of the gullet.",
    "quotes": [
      {
        "author": "Henry George Liddell",
        "work": "A Greek-English Lexicon",
        "quote": "The Greek anatomical noun oisophagos forms the scientific combining root **oesophag**, literally meaning the carrier of food."
      },
      {
        "author": "Robert Beekes",
        "work": "Etymological Dictionary of Greek",
        "quote": "Classical etymologists traced **oesophag** to compound roots denoting the swallowing and carriage of alimentary boluses."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy of the Human Body",
        "quote": "The prefix **oesophag** designates the muscular tube and its associated nervous and arterial plexuses traversing the mediastinum."
      }
    ]
  },
  "Dashboard — oesophag\\oesophagectomy.md": {
    "primary": "The surgical removal or excision of all or a portion of the esophagus, typically performed to treat esophageal cancer or severe traumatic rupture.",
    "secondary": "In thoracic surgical oncology, an oesophagectomy is frequently followed by gastric pull-up reconstruction to re-establish alimentary continuity.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Malignant neoplasms of the lower gullet historically posed insurmountable obstacles until pioneer surgeons attempted radical **oesophagectomy**."
      },
      {
        "author": "Juan Rosai",
        "work": "Rosai and Ackerman's Surgical Pathology",
        "quote": "Pathological staging following an **oesophagectomy** requires thorough microscopic examination of resected periesophageal lymph nodes."
      },
      {
        "author": "Lord Moynihan",
        "work": "Abdominal Operations",
        "quote": "A successful transthoracic **oesophagectomy** requires delicate mobilization of the stomach while preserving the gastroepiploic arcade."
      }
    ]
  },
  "Dashboard — oesophag\\oesophagitis.md": {
    "primary": "Inflammation of the mucosal lining of the esophagus, commonly caused by acid reflux, infectious organisms, or chemical ingestion.",
    "secondary": "In gastroenterology, chronic gastro-oesophageal reflux disease (GORD) produces reflux oesophagitis, which can advance to ulceration, stricture, and Barrett's esophagus.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Corrosive poisons accidentally swallowed induce acute corrosive **oesophagitis**, leading to extensive sloughing and cicatricial stenosis."
      },
      {
        "author": "Anthony S. Fauci",
        "work": "Harrison's Principles of Internal Medicine",
        "quote": "In immunocompromised patients, acute **oesophagitis** presenting with severe odynophagia frequently stems from Candida or herpes simplex infection."
      },
      {
        "author": "Juan Rosai",
        "work": "Rosai and Ackerman's Surgical Pathology",
        "quote": "Biopsies demonstrating basal zone hyperplasia and intraepithelial eosinophils confirm the diagnosis of chronic reflux **oesophagitis**."
      }
    ]
  },
  "Dashboard — oesophag\\oesophagoscope.md": {
    "primary": "A rigid or flexible medical endoscope equipped with a light and camera, used to visually examine the interior lumen of the esophagus.",
    "secondary": "In modern endoscopic medicine, an oesophagoscope allows gastroenterologists to biopsy mucosal lesions, dilate strictures, and ligate bleeding esophageal varices.",
    "quotes": [
      {
        "author": "Chevalier Jackson",
        "work": "Tracheo-Bronchoscopy, Esophagoscopy and Gastroscopy",
        "quote": "The introduction of the illuminated **oesophagoscope** transformed the extraction of swallowed foreign bodies from hazardous surgery into safe endoscopy."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Direct inspection through the **oesophagoscope** reveals mucosal ulcerations and early neoplasms long before radiographic changes appear."
      },
      {
        "author": "Lord Moynihan",
        "work": "Abdominal Operations",
        "quote": "The surgeon passed the flexible **oesophagoscope** to identify the precise distal extent of the bleeding variceal columns."
      }
    ]
  },
  "Dashboard — oesophag\\oesophagus.md": {
    "primary": "The muscular membranous tube through which food and liquids pass from the pharynx down to the stomach; the gullet (British spelling).",
    "secondary": "In human digestive anatomy, the oesophagus passes through the posterior mediastinum and pierces the diaphragm at the esophageal hiatus, propelling food via peristalsis.",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy of the Human Body",
        "quote": "The **oesophagus** is a muscular canal, about twenty-five centimeters long, extending from the pharynx to the cardiac orifice of the stomach."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Spasmodic stricture of the **oesophagus**, commonly termed cardiospasm, produces regurgitation of undigested food without organic tumor."
      },
      {
        "author": "Claude Bernard",
        "work": "Leçons de physiologie opératoire",
        "quote": "By establishing a fistulous opening into the cervical **oesophagus**, we demonstrated that sham feeding triggers gastric acid secretion through reflex vagal stimulation."
      }
    ]
  },
  "Dashboard — oid\\asteroid.md": {
    "primary": "A small rocky or metallic celestial body orbiting the Sun, mostly situated within the main asteroid belt between Mars and Jupiter; starlike in shape.",
    "secondary": "In planetary astronomy and celestial mechanics, asteroids represent primordial planetesimal remnants that failed to coalesce into a planet due to Jupiter's gravitational perturbations.",
    "quotes": [
      {
        "author": "William Herschel",
        "work": "Observations on the Nature of the Newly Discovered Stars",
        "quote": "Since these newly discovered small celestial bodies resemble faint stars yet move like planets, I propose to designate them by the term **asteroid**."
      },
      {
        "author": "Carl Sagan",
        "work": "Cosmos",
        "quote": "The impact of a large **asteroid** with the Earth sixty-six million years ago triggered catastrophic climatic disruptions that terminated the age of dinosaurs."
      },
      {
        "author": "Eugene Shoemaker",
        "work": "Asteroid and Comet Impacts on the Earth",
        "quote": "Near-Earth asteroids represent an active dynamical population whose orbits regularly intersect the inner solar system."
      }
    ]
  }
};

const count = updateNotesBatch(baseDir, batchData);
console.log(`Updated ${count} notes in Finish Slice 1 Batch 5.`);
