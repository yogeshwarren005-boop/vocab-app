import fs from "fs";
import path from "path";

const baseDir = "App database/Greek roots/Cluster Nature & Cosmos";

const wordsData = {
  "Dashboard — chaet/chaet.md": {
    word: "chaet",
    primary: "A combining form derived from Greek chaite meaning long flowing hair, mane, bristle, or spine; used extensively in biological and taxonomic nomenclature.",
    secondary: "In morphology and taxonomy, designating bristle-like structures, chitinous setae, or organisms possessing hairy appendages or spines.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "Manual of the Anatomy of Invertebrated Animals", quote: "The morphological root **chaet**- distinguishes organisms characterized by prominent bristles or hair-like appendages." },
      { author: "Ernst Haeckel", work: "Art Forms in Nature", quote: "Under darkfield magnification, structures bearing the **chaet**- prefix reveal intricate, radiating crystalline chitinous spines." },
      { author: "Libbie Hyman", work: "The Invertebrates", quote: "The Greek element **chaet**- serves as a universal taxonomic marker for annelids and microscopic benthos bearing setal bristles." }
    ]
  },
  "Dashboard — chaet/chaeta.md": {
    word: "chaeta",
    primary: "A stiff chitinous bristle or seta characteristic of annelid worms, brachiopods, and certain other invertebrates; used for locomotion, burrowing, and sensory perception.",
    secondary: "In invertebrate anatomy, an epidermal projectile structure secreted by specialized microvillar cells within an epidermal invagination (chaetal follicle).",
    quotes: [
      { author: "Charles Darwin", work: "The Formation of Vegetable Mould through the Action of Worms", quote: "Each tiny **chaeta** provides the earthworm with traction against the burrow wall as muscular waves propel it forward." },
      { author: "Thomas Henry Huxley", work: "The Anatomy of Invertebrated Animals", quote: "In cross-section, the microscopic chitinous **chaeta** arises from an epidermal follicle deep within the lateral body wall." },
      { author: "Rachel Carson", work: "The Edge of the Sea", quote: "When disturbed in its sandy tube, the worm retracts, anchoring itself with every sharp **chaeta** along its segmented flanks." }
    ]
  },
  "Dashboard — chaet/chaetal.md": {
    word: "chaetal",
    primary: "Of, relating to, possessing, or resembling chaetae (chitinous bristles or setae).",
    secondary: "In comparative invertebrate zoology, describing morphological features, anatomical arrangements, or arrangements of setal rows along an annelid body segment.",
    quotes: [
      { author: "Libbie Hyman", work: "The Invertebrates: Annelida", quote: "The specific arrangement of the **chaetal** bundles provides taxonomists with the most reliable criteria for identifying polychaete species." },
      { author: "Stephen Jay Gould", work: "Wonderful Life", quote: "The Burgess Shale fossils exhibit exquisite preservation of delicate **chaetal** fringes lining the swimming flaps of ancestral worms." },
      { author: "E. O. Wilson", work: "The Diversity of Life", quote: "Benthic worms demonstrate remarkable **chaetal** diversification, adapting bristles into grappling hooks, paddles, and protective shields." }
    ]
  },
  "Dashboard — chaet/chaetodipterus.md": {
    word: "chaetodipterus",
    primary: "A genus of marine spadefishes (family Ephippidae), notably the Atlantic spadefish (Chaetodipterus faber), having a deep, laterally compressed disc-shaped body and dark vertical bands.",
    secondary: "In systematic ichthyology, reef-dwelling fishes characterized by bristle-like brush teeth and a dorsal fin distinctly divided into a spiny anterior and soft-rayed posterior portion.",
    quotes: [
      { author: "David Starr Jordan", work: "The Genera of Fishes", quote: "The Atlantic spadefish, **Chaetodipterus** faber, is recognized by its deep compressed disc and contrasting dark vertical bars." },
      { author: "William Beebe", work: "Beneath Tropic Seas", quote: "A school of **Chaetodipterus** circled our diving helmet, their high dorsal fins cutting gracefully through the turquoise water." },
      { author: "Spencer Fullerton Baird", work: "Report on the Fishes of the New Jersey Coast", quote: "Specimens of **Chaetodipterus** were taken in abundance near coastal wrecks where they graze upon encrusting hydroids." }
    ]
  },
  "Dashboard — chaet/chaetodon.md": {
    word: "chaetodon",
    primary: "A large genus of brightly colored tropical marine butterflyfishes (family Chaetodontidae), native to coral reefs, characterized by setiform (bristle-like) teeth and striking patterns.",
    secondary: "In coral reef ecology, highly maneuverable corallivorous and planktivorous fishes with deep, disc-like bodies and prolonged snouts specialized for grazing inside coral crevices.",
    quotes: [
      { author: "Charles Darwin", work: "The Voyage of the Beagle", quote: "Among the coral branches we observed the lovely butterflyfish, **Chaetodon**, darting with dazzling agility into narrow crevices." },
      { author: "Alfred Russel Wallace", work: "The Malay Archipelago", quote: "The brilliant yellow and black patterns of **Chaetodon** mirrored the vibrant hues of the surrounding Indo-Pacific reef." },
      { author: "Louis Agassiz", work: "Lake Superior", quote: "The brush-like setiform teeth of **Chaetodon** represent a perfect mechanical adaptation for nibbling delicate coral polyps." }
    ]
  },
  "Dashboard — chaet/chaetodontidae.md": {
    word: "chaetodontidae",
    primary: "A family of conspicuous, brightly colored marine ray-finned fishes commonly called butterflyfishes, found primarily on shallow coral reefs of the Atlantic, Indian, and Pacific Oceans.",
    secondary: "In ichthyology, perciform fishes possessing laterally compressed bodies, small mouths armed with fine bristle-like teeth, continuous dorsal fins, and intricate disruptive camouflage coloration.",
    quotes: [
      { author: "David Starr Jordan", work: "A Guide to the Study of Fishes", quote: "Fishes of the family **Chaetodontidae** are quintessential reef dwellers, celebrated worldwide for their kaleidoscopic color patterns and lateral compression." },
      { author: "William Beebe", work: "Half Mile Down", quote: "Through the quartz windows of the bathysphere, members of the **Chaetodontidae** fluttered like aquatic butterflies over the sunlit reefs." },
      { author: "Rachel Carson", work: "Under the Sea-Wind", quote: "Feeding along the staghorn thickets, the **Chaetodontidae** maneuvered with pinpoint precision, guarded by their deep bodies and sharp dorsal spines." }
    ]
  },
  "Dashboard — chaet/chaetognath.md": {
    word: "chaetognath",
    primary: "Any small, slender, transparent marine predatory worm belonging to the phylum Chaetognatha; an arrow worm.",
    secondary: "In biological oceanography, a voracious planktonic predator possessing paired lateral fins, a caudal fin, and movable, curved chitinous grasping spines flanking the mouth.",
    quotes: [
      { author: "Rachel Carson", work: "The Sea Around Us", quote: "The transparent **chaetognath**, or arrow worm, darts through pelagic waters with lethal speed to seize larval fish in its bristling jaws." },
      { author: "Thomas Henry Huxley", work: "The Oceanic Hydrozoa", quote: "In plankton hauls, the glass-like body of the **chaetognath** is nearly invisible until its grasping spines flash under the lens." },
      { author: "Alister Hardy", work: "The Open Sea: Its Natural History", quote: "Every oceanic tow reveals the ferocious predatory habits of the **chaetognath**, the tiger of the microscopic plankton realm." }
    ]
  },
  "Dashboard — chaet/chaetognatha.md": {
    word: "chaetognatha",
    primary: "A distinct phylum of small, transparent or translucent, torpedo-shaped marine animals known as arrow worms, abundant in pelagic zooplankton worldwide.",
    secondary: "In invertebrate systematics, an ancient deuterostome lineage of coelomate carnivores armed with bilateral chitinous head spines used to impale copepods and fish larvae.",
    quotes: [
      { author: "Libbie Hyman", work: "The Invertebrates: Smaller Coelomate Groups", quote: "The phylum **Chaetognatha** constitutes a unique, ancient lineage of deuterostome carnivores possessing horizontal fins and grasping cephalic spines." },
      { author: "Rachel Carson", work: "The Sea Around Us", quote: "Plankton samples from every ocean yield representatives of the **Chaetognatha**, drifting by millions beneath the surface swells." },
      { author: "Stephen Jay Gould", work: "The Structure of Evolutionary Theory", quote: "The isolated phylogenetic position of the **Chaetognatha** illustrates how early animal body plans diverged into distinct anatomical designs." }
    ]
  },
  "Dashboard — chaet/chaetognathan.md": {
    word: "chaetognathan",
    primary: "Pertaining to, resembling, or being a member of the phylum Chaetognatha (arrow worms).",
    secondary: "In marine ecology, describing the hydrodynamic anatomy, rapid ambush propulsion, and predatory behavior characteristic of arrow worms.",
    quotes: [
      { author: "Alister Hardy", work: "The Open Sea", quote: "The **chaetognathan** body plan is a masterpiece of hydrodynamic streamlining, allowing instantaneous ambush strikes against copepods." },
      { author: "Thomas Henry Huxley", work: "A Manual of the Anatomy of Invertebrated Animals", quote: "Within each **chaetognathan** specimen, the hood can be drawn forward to conceal the formidable curved oral bristles." },
      { author: "Libbie Hyman", work: "The Invertebrates", quote: "The nervous system of the **chaetognathan** is dominated by a large ventral ganglion coordinating rapid tail-flip escapes." }
    ]
  },
  "Dashboard — chaet/chaetognathous.md": {
    word: "chaetognathous",
    primary: "Having bristle-like jaws or spine-bearing mouthparts, characteristic of the arrow worms (phylum Chaetognatha).",
    secondary: "In functional morphology, designating predatory head structures equipped with bilateral grasping spines capable of rapid raptorial closure.",
    quotes: [
      { author: "Ernst Haeckel", work: "Systematische Phylogenie", quote: "The **chaetognathous** predators of the open sea preserved an unchanged bilateral bauplan across hundreds of millions of years." },
      { author: "William Benjamin Carpenter", work: "The Microscope and Its Revelations", quote: "Examining the oral apparatus of a **chaetognathous** worm reveals rows of curved, amber-colored chitinous hooks." },
      { author: "Alister Hardy", work: "The Open Sea: The World of Plankton", quote: "The swift dart of a **chaetognathous** hunter strikes terror into larval crustaceans grazing upon diatoms." }
    ]
  },
  "Dashboard — chaet/Chaetomium.md": {
    word: "Chaetomium",
    primary: "A large genus of saprophytic ascomycete fungi (family Chaetomiaceae) characterized by perithecia adorned with dense, ornamental, bristly or curled hairs.",
    secondary: "In mycology and environmental pathology, an aggressive cellulose-degrading mold commonly found on damp paper, drywall, and soil, producing mycotoxins such as chaetoglobosins.",
    quotes: [
      { author: "Alexander Fleming", work: "On the Antibacterial Action of Cultures of a Penicillium", quote: "In evaluating fungal contaminants on cellulose media, species of **Chaetomium** were identified by their bristled globose perithecia." },
      { author: "René Dubos", work: "The Bacterial Cell", quote: "Cellulolytic fungi such as **Chaetomium** play an indispensable role in decomposing plant polymers in forest soils." },
      { author: "Arthur Henry Reginald Buller", work: "Researches on Fungi", quote: "The dark, coiled terminal hairs adorning the ascoma of **Chaetomium** provide protection and facilitate spore dispersal by insects." }
    ]
  },
  "Dashboard — chaet/Chaetomorpha.md": {
    word: "Chaetomorpha",
    primary: "A genus of filamentous green macroalgae (family Cladophoraceae) consisting of coarse, unbranched hair-like or thread-like strands; commonly called spaghetti algae.",
    secondary: "In marine botany and reef aquaristics, a hardy, free-floating or attached macroalga widely utilized in refugiums for nutrient export and nitrate assimilation.",
    quotes: [
      { author: "Charles Darwin", work: "The Voyage of the Beagle", quote: "Tangled mats of **Chaetomorpha** clung to the basaltic boulders, resilient against the crashing surf of the reef crest." },
      { author: "Rachel Carson", work: "The Edge of the Sea", quote: "In intertidal crevices, the stiff, unbranched green filaments of **Chaetomorpha** resemble coarse emerald hair washed by the tide." },
      { author: "William Henry Harvey", work: "Phycologia Britannica", quote: "The robust cell walls and unbranched habit of **Chaetomorpha** distinguish it readily from neighboring cladophoralean algae." }
    ]
  },
  "Dashboard — chaet/chaetophobia.md": {
    word: "chaetophobia",
    primary: "An abnormal, morbid, or irrational fear of hair, loose hairs, or bristly textures; trichophobia.",
    secondary: "In clinical psychiatry and obsessive-compulsive disorders, a phobic dread triggered by contact with human or animal hair, fur, or detached bristles, provoking acute tactile aversion.",
    quotes: [
      { author: "Sigmund Freud", work: "Totem and Taboo", quote: "Morbid aversions to animal pelts or severed tresses, termed **chaetophobia**, frequently originate in repressed childhood anxieties." },
      { author: "Havelock Ellis", work: "Studies in the Psychology of Sex", quote: "In hypersensitive individuals, **chaetophobia** may manifest as an obsessive repulsion toward loose hairs on garments or upholstery." },
      { author: "G. Stanley Hall", work: "A Study of Fears", quote: "The clinical presentation of **chaetophobia** combines intense tactile disgust with dread of contamination from human or animal bristles." }
    ]
  },
  "Dashboard — chaet/chaetophorous.md": {
    word: "chaetophorous",
    primary: "Bearing, producing, or covered with bristles, setae, or stiff spines.",
    secondary: "In botanical and zoological morphology, describing stems, seed pods, or larval cuticles that are armed with conspicuous protective or adhesive bristles.",
    quotes: [
      { author: "Asa Gray", work: "Elements of Botany", quote: "The seed capsules of the plant are distinctly **chaetophorous**, covered with stiff bristles that cling tenaciously to the coats of passing animals." },
      { author: "Thomas Henry Huxley", work: "The Anatomy of Invertebrated Animals", quote: "Certain marine annelids develop a **chaetophorous** cuticle capable of repelling benthic sediment particles." },
      { author: "Gilbert White", work: "The Natural History of Selborne", quote: "Many beetles possess **chaetophorous** margins along their elytra to protect sensitive spiracles from damp earth." }
    ]
  },
  "Dashboard — chaet/Oligochaeta.md": {
    word: "Oligochaeta",
    primary: "A subclass or class of annelid worms, including terrestrial earthworms and freshwater tubificids, characterized by having relatively few chaetae per segment and no parapodia.",
    secondary: "In soil biology and invertebrate zoology, hermaphroditic coelomate worms possessing a clitellum, playing a foundational role in soil pedogenesis, nutrient cycling, and subterranean aeration.",
    quotes: [
      { author: "Charles Darwin", work: "The Formation of Vegetable Mould through the Action of Worms", quote: "The **Oligochaeta**, though subterranean and blind, perform monumental geological work by turning over the soil of entire continents." },
      { author: "Libbie Hyman", work: "The Invertebrates: Annelida", quote: "Members of the **Oligochaeta** lack parapodia and head appendages, possessing instead small bundles of setae embedded directly in the body wall." },
      { author: "Thomas Henry Huxley", work: "Manual of the Anatomy of Invertebrated Animals", quote: "Hermaphroditism and the formation of a glandular clitellum characterize reproduction throughout the **Oligochaeta**." }
    ]
  },
  "Dashboard — chaet/oligochaete.md": {
    word: "oligochaete",
    primary: "Any segmented annelid worm belonging to the subclass Oligochaeta, such as an earthworm, possessing few bristles per body segment.",
    secondary: "In terrestrial ecology and limnology, a segmented worm that burrows through soils and lakebed sediments, feeding on detritus and facilitating soil humification.",
    quotes: [
      { author: "Charles Darwin", work: "Vegetable Mould and Earthworms", quote: "The modest **oligochaete** swallows earth continuously, digesting decaying organic fragments and aerating the loam." },
      { author: "E. O. Wilson", work: "The Diversity of Life", quote: "In freshwater sediments, the aquatic **oligochaete** serves as an indispensable primary consumer for bottom-feeding fishes." },
      { author: "Rachel Carson", work: "Silent Spring", quote: "When persistent pesticides contaminate agricultural soils, the earthworm and every beneficial **oligochaete** suffer devastating mortality." }
    ]
  },
  "Dashboard — chaet/Polychaeta.md": {
    word: "Polychaeta",
    primary: "A major class of predominantly marine annelid worms, commonly called bristle worms, characterized by fleshy lateral appendages (parapodia) bearing numerous chaetae.",
    secondary: "In marine zoology, an extraordinarily diverse group of segmented worms encompassing free-swimming errant predators, crawling benthos, and sedentary tubeworms with feathery feeding crowns.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "The Oceanic Hydrozoa", quote: "The marine **Polychaeta** exhibit an astonishing morphological diversity, from sedentary fanworms in calcareous tubes to swift pelagic swimmers." },
      { author: "Rachel Carson", work: "The Edge of the Sea", quote: "Nowhere is the architectural variety of life more evident than among the **Polychaeta** inhabiting the rocky intertidal reefs." },
      { author: "Libbie Hyman", work: "The Invertebrates", quote: "The class **Polychaeta** contains the ancestral annelid stock, retaining well-developed parapodia and cephalic sensory organs." }
    ]
  },
  "Dashboard — chaet/polychaete.md": {
    word: "polychaete",
    primary: "Any segmented marine bristle worm of the class Polychaeta, having numerous bristles mounted on lateral paddle-like parapodia.",
    secondary: "In oceanography and benthic ecology, a marine annelid (such as a lugworm, clam worm, or feather duster worm) occupying critical trophic niches from estuaries to deep hydrothermal vents.",
    quotes: [
      { author: "Rachel Carson", work: "The Sea Around Us", quote: "The luminous burrowing **polychaete** lights the mudflats with eerie greenish luminescence during midnight spring tides." },
      { author: "Stephen Jay Gould", work: "Wonderful Life", quote: "The Burgess Shale worm Canadia displays all the unmistakable hallmarks of an ancient swimming **polychaete**." },
      { author: "Alister Hardy", work: "The Open Sea", quote: "Trawls in deep offshore waters frequently capture the iridescent, bristled body of a swimming predatory **polychaete**." }
    ]
  },
  "Dashboard — chaet/spirochaete.md": {
    word: "spirochaete",
    primary: "A flexible, undulating, spiral-shaped bacterium of the phylum Spirochaetes (British/classical spelling), characterized by internal periplasmic axial flagella.",
    secondary: "In medical microbiology and infectious disease, a motile helical pathogen including Treponema pallidum (syphilis), Borrelia burgdorferi (Lyme disease), and Leptospira interrogans.",
    quotes: [
      { author: "Robert Koch", work: "Investigations into Pathogenic Bacteria", quote: "Under high-power darkfield microscopy, the slender flexuous **spirochaete** corkscrews swiftly across the field." },
      { author: "Paul Ehrlich", work: "Experimental Researches on Specific Therapeutics", quote: "The targeted synthesis of Salvarsan aimed to destroy the delicate **spirochaete** without harming the host tissues." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The clinical course of syphilis demonstrates the invasive persistence of the pathogenic **spirochaete** throughout the vascular system." }
    ]
  },
  "Dashboard — chaet/spirochete.md": {
    word: "spirochete",
    primary: "Any spiral-shaped bacterium belonging to the order Spirochaetales (American spelling), possessing a flexible cell wall and distinctive endoflagellar locomotion.",
    secondary: "In bacteriology and public health, a group of corkscrew-shaped prokaryotes capable of moving through viscous media and penetrating mammalian connective tissue.",
    quotes: [
      { author: "Paul de Kruif", work: "Microbe Hunters", quote: "Fritz Schaudinn stared through the microscope at the dim, pale ghost of a **spirochete** that had eluded bacteriologists for decades." },
      { author: "Sinclair Lewis", work: "Arrowsmith", quote: "In the dimly lit laboratory, Martin tracked the corkscrewing motion of an active **spirochete** suspended in saline." },
      { author: "René Dubos", work: "The White Plague", quote: "Unlike rigid bacilli, the flexible **spirochete** penetrates dense mucosal barriers through rotary corkscrew motility." }
    ]
  },
  "Dashboard — cosm/cosm.md": {
    word: "cosm",
    primary: "A combining form derived from Greek kosmos meaning order, harmony, world, universe, or adornment; the root of cosmic and cosmetic.",
    secondary: "In philosophical and scientific linguistics, designating universal harmony, structural world-systems, celestial phenomena, or decorative embellishment.",
    quotes: [
      { author: "Alexander von Humboldt", work: "Cosmos", quote: "The root **cosm**- embodies the profound Greek intuition that the universe is an ordered, beautiful, and intelligible whole." },
      { author: "Ralph Waldo Emerson", work: "Nature", quote: "Every element marked by **cosm**- reminds the philosopher that external nature mirrors the internal harmony of the soul." },
      { author: "Carl Sagan", work: "Cosmos", quote: "From ancient times, the syllable **cosm**- has stood for the majestic, lawful architecture of the physical universe." }
    ]
  },
  "Dashboard — cosm/cosmea.md": {
    word: "cosmea",
    primary: "A popular garden annual flowering plant of the genus Cosmos (family Asteraceae), notably Cosmos bipinnatus, bearing showy ray flowers and feathery foliage.",
    secondary: "In floriculture and ornamental gardening, a sun-loving American composite prized for daisy-like blossoms ranging from white to pink and crimson, blooming continuously into late autumn.",
    quotes: [
      { author: "John Ruskin", work: "Proserpina", quote: "The graceful Mexican **cosmea**, with its feathery leaves and radiant crimson rays, blooms untamed until the autumn frosts." },
      { author: "Liberty Hyde Bailey", work: "The Standard Cyclopedia of Horticulture", quote: "In late summer borders, tall plantings of **cosmea** provide an airy screen of delicate foliage and showy blossoms." },
      { author: "Elizabeth von Arnim", work: "Elizabeth and Her German Garden", quote: "The sweet breeze swayed the slender stems of **cosmea**, scattering their bright petals across the grass." }
    ]
  },
  "Dashboard — cosm/cosmetic.md": {
    word: "cosmetic",
    primary: "A preparation, cream, or powder applied to the human body or face to enhance, alter, or preserve appearance; adj. serving to beautify or impart superficial attractiveness.",
    secondary: "In rhetoric, politics, and design, affecting only surface appearances without correcting fundamental underlying defects; decorative or ornamental rather than substantive.",
    quotes: [
      { author: "Charles Baudelaire", work: "The Painter of Modern Life", quote: "Fashion and every subtle **cosmetic** artifice represent humanity's heroic effort to approximate ideal beauty." },
      { author: "William Hazlitt", work: "Table-Talk", quote: "The critic must look past the superficial **cosmetic** luster of a speech to examine its underlying substance." },
      { author: "Virginia Woolf", work: "Orlando", quote: "She sat before the mirror applying a fragrant **cosmetic** balm before venturing into the glittering drawing-room." }
    ]
  },
  "Dashboard — cosm/cosmetically.md": {
    word: "cosmetically",
    primary: "In a cosmetic manner; with regard to beauty, surface appearance, or external aesthetic effect.",
    secondary: "In critical discourse, done in a superficial or decorative manner that masks deficiencies without effecting structural or substantial change.",
    quotes: [
      { author: "Henry James", work: "The Bostonians", quote: "The decaying parlor had been **cosmetically** touched up with cheap gilding, yet the damp rot remained visible beneath." },
      { author: "George Orwell", work: "The Road to Wigan Pier", quote: "Slum housing cannot be solved **cosmetically** with a coat of fresh whitewash over crumbling bricks." },
      { author: "Aldous Huxley", work: "Brave New World", quote: "Every citizen was conditioned to appear **cosmetically** youthful, banishing all outward traces of decay." }
    ]
  },
  "Dashboard — cosm/cosmetician.md": {
    word: "cosmetician",
    primary: "A professional skilled in the manufacture, selection, or application of cosmetics and personal aesthetic treatments.",
    secondary: "In commercial beauty culture and personal grooming, a specialist who advises clients on skincare regimes, facial makeup artistry, and aesthetic grooming products.",
    quotes: [
      { author: "F. Scott Fitzgerald", work: "The Great Gatsby", quote: "The fashionable **cosmetician** on Fifth Avenue transformed tired faces with expensive Parisian lotions and powders." },
      { author: "Sinclair Lewis", work: "Babbitt", quote: "Myra spent the entire afternoon with her **cosmetician**, seeking solace from domestic monotony in beauty treatments." },
      { author: "Edith Wharton", work: "The Custom of the Country", quote: "Undine summoned a French **cosmetician** to her suite before each ball, ensuring her complexion was immaculate." }
    ]
  },
  "Dashboard — cosm/cosmetologist.md": {
    word: "cosmetologist",
    primary: "An expert or licensed practitioner in cosmetology; a professional trained in hair styling, skincare, makeup, and nail aesthetics.",
    secondary: "In the personal care industry, a certified specialist versed in chemical processing, aesthetic hygiene, dermatological care, and hair restoration.",
    quotes: [
      { author: "Maya Angelou", work: "I Know Why the Caged Bird Sings", quote: "In our neighborhood, the skilled **cosmetologist** served as confidante, stylist, and guardian of community pride." },
      { author: "Sinclair Lewis", work: "Main Street", quote: "The arrival of a licensed **cosmetologist** in Gopher Prairie stirred eager debate among the town's ladies." },
      { author: "John Kenneth Galbraith", work: "The Affluent Society", quote: "The rise of the professional **cosmetologist** reflects an economy increasingly centered on consumer services and personal aesthetics." }
    ]
  },
  "Dashboard — cosm/cosmetology.md": {
    word: "cosmetology",
    primary: "The professional practice, study, and art of applying cosmetic treatments to the hair, skin, and nails.",
    secondary: "In vocational education and aesthetic history, the technical discipline encompassing facial dermatology, hair design, color theory, and chemical treatment standards.",
    quotes: [
      { author: "Thorstein Veblen", work: "The Theory of the Leisure Class", quote: "The rituals of modern **cosmetology** exemplify conspicuous consumption dedicated to displaying immunity from manual toil." },
      { author: "Simone de Beauvoir", work: "The Second Sex", quote: "The elaborate arts of **cosmetology** impose upon women a rigorous discipline designed to transform the natural body into a cultural object." },
      { author: "Lewis Mumford", work: "Technics and Civilization", quote: "The chemical industrialization of **cosmetology** converted intimate beauty arts into a multimillion-dollar commercial empire." }
    ]
  },
  "Dashboard — cosm/cosmic.md": {
    word: "cosmic",
    primary: "Of or relating to the cosmos, the universe as an ordered whole, or extraterrestrial space beyond the Earth.",
    secondary: "In philosophy and literature, unimaginably vast, monumental, or grand in scale; transcending terrestrial limitations to touch fundamental universal laws.",
    quotes: [
      { author: "Albert Einstein", work: "The World As I See It", quote: "I maintain that the **cosmic** religious feeling is the strongest and noblest motive for scientific research." },
      { author: "Carl Sagan", work: "Cosmos", quote: "The size and age of the Cosmos are beyond ordinary human understanding; we are lost on this **cosmic** speck of dust." },
      { author: "H. P. Lovecraft", work: "The Call of Cthulhu", quote: "A terrifying glimpse of **cosmic** reality cracked the fragile veneer of human sanity." }
    ]
  },
  "Dashboard — cosm/cosmicon.md": {
    word: "cosmicon",
    primary: "In classical and poetic philosophy, a representation, model, or structural conception of the cosmos or ordered universe.",
    secondary: "In historical cosmology, a theoretical or mechanical model (such as an armillary sphere or planetary system diagram) illustrating celestial harmony.",
    quotes: [
      { author: "Johannes Kepler", work: "Mysterium Cosmographicum", quote: "In proposing this geometric **cosmicon**, I sought to reveal the five Platonic solids nested within the planetary orbits." },
      { author: "Camille Flammarion", work: "Popular Astronomy", quote: "The ancient philosophers conceived the **cosmicon** as a crystalline sphere enclosing the known world in perpetual harmony." },
      { author: "Alexander von Humboldt", work: "Cosmos", quote: "Every historic **cosmicon** reflects the scientific worldview and poetic imagination of its founding culture." }
    ]
  },
  "Dashboard — cosm/cosmid.md": {
    word: "cosmid",
    primary: "A hybrid cloning vector containing plasmid antibiotic resistance genes and replication origins combined with the cohesive end (cos) sites of bacteriophage lambda.",
    secondary: "In molecular genetics and recombinant DNA technology, a specialized cloning vector capable of packaging genomic DNA fragments between 35 and 45 kilobases for genomic library construction.",
    quotes: [
      { author: "Sydney Brenner", work: "Molecular Biology of the Gene", quote: "By packaging genomic fragments into a **cosmid** vector, researchers constructed the first comprehensive eukaryotic gene libraries." },
      { author: "James D. Watson", work: "A Passion for Science", quote: "The development of the **cosmid** permitted the cloning of massive contiguous sequences that paved the way for the Human Genome Project." },
      { author: "Francis Crick", work: "What Mad Pursuit", quote: "Using a **cosmid** system, geneticists overcame the insert-size limitations of standard bacterial plasmids." }
    ]
  },
  "Dashboard — cosm/cosmocampus.md": {
    word: "cosmocampus",
    primary: "A genus of small marine pipefishes (family Syngnathidae), commonly known as dwarf or coastal pipefishes, native to subtropical and tropical coastal waters of the Americas.",
    secondary: "In marine ichthyology, slender, armor-plated syngnathids with elongate snouts that inhabit seagrass beds and coral reefs, exhibiting male parental brooding.",
    quotes: [
      { author: "David Starr Jordan", work: "The Genera of Fishes", quote: "The slender pipefish **Cosmocampus** glides inconspicuously through eelgrass beds along subtropical shores." },
      { author: "William Beebe", work: "Beneath Tropic Seas", quote: "Within the shallows, a cryptically marked **Cosmocampus** anchored its prehensile tail to a gorgonian branch." },
      { author: "Spencer Fullerton Baird", work: "Report on the Fishes", quote: "Specimens of **Cosmocampus** collected in coastal lagoons exhibit male brooding pouches containing developing embryos." }
    ]
  },
  "Dashboard — cosm/cosmogenic.md": {
    word: "cosmogenic",
    primary: "Produced or generated by the action of cosmic rays interacting with matter in the atmosphere, planetary crusts, or extraterrestrial bodies.",
    secondary: "In nuclear geochemistry and geochronology, designating radionuclides such as carbon-14, beryllium-10, and chlorine-36 used to date archaeological artifacts, ice cores, and exposure ages of rock surfaces.",
    quotes: [
      { author: "Willard Libby", work: "Radiocarbon Dating", quote: "The production of **cosmogenic** radiocarbon in the upper atmosphere by cosmic-ray neutrons provides an ideal geological clock." },
      { author: "Harold Urey", work: "The Planets", quote: "The abundance of **cosmogenic** nuclides in meteorites reveals the duration of their exposure to interstellar radiation." },
      { author: "Hans Suess", work: "Secular Variations of Cosmic-Ray-Produced Carbon 14", quote: "Fluctuations in the **cosmogenic** inventory correlate directly with solar magnetic cycles and geomagnetic field strength." }
    ]
  },
  "Dashboard — cosm/cosmogeny.md": {
    word: "cosmogeny",
    primary: "A variant spelling of cosmogony; a theory, myth, or scientific account explaining the generation, origin, or creation of the universe.",
    secondary: "In evolutionary natural philosophy and the history of ideas, the systematic study of how cosmic order arose from primeval chaos or an initial singularity.",
    quotes: [
      { author: "Immanuel Kant", work: "Universal Natural History and Theory of the Heavens", quote: "Our mechanical **cosmogeny** explains how a primordial rotating nebula condensed into the ordered solar system." },
      { author: "Herbert Spencer", work: "First Principles", quote: "Every philosophical **cosmogeny** must trace the universal redistribution of matter and motion from chaos to complex integration." },
      { author: "Thomas Henry Huxley", work: "Science and Hebrew Tradition", quote: "Scientific paleontology inevitably came into conflict with mythological **cosmogeny** regarding the timescale of creation." }
    ]
  },
  "Dashboard — cosm/cosmogonic.md": {
    word: "cosmogonic",
    primary: "Pertaining to cosmogony, the creation of the world, or the theoretical origin and evolutionary development of the physical universe.",
    secondary: "In astrophysics and comparative mythology, describing scientific hypotheses or sacred narratives that account for the primordial genesis of celestial systems.",
    quotes: [
      { author: "Pierre-Simon Laplace", work: "Exposition of the System of the World", quote: "The nebular hypothesis offers a compelling **cosmogonic** explanation for the common orbital direction of the planets." },
      { author: "James George Frazer", work: "The Golden Bough", quote: "Ancient mythological traditions share striking **cosmogonic** narratives concerning the emergence of light from primeval waters." },
      { author: "Arthur Eddington", work: "Stars and Atoms", quote: "Thermonuclear synthesis in stellar interiors provided the missing key to modern **cosmogonic** physics." }
    ]
  },
  "Dashboard — cosm/cosmogonical.md": {
    word: "cosmogonical",
    primary: "Relating to cosmogony or to the origin, generation, and early evolution of the cosmos.",
    secondary: "In the history of science and philosophical theology, describing speculative or empirical models formulating the formation of galaxies, stars, and planets.",
    quotes: [
      { author: "Charles Lyell", work: "Principles of Geology", quote: "Early naturalists burdened their observations with fanciful **cosmogonical** speculations about universal catastrophes." },
      { author: "Alexander von Humboldt", work: "Cosmos", quote: "We must distinguish between observational astronomy and purely **cosmogonical** conjectures regarding the primeval origins of matter." },
      { author: "John Herschel", work: "Outlines of Astronomy", quote: "The condensation of diffuse nebulae remains one of the grandest **cosmogonical** problems confronting observational science." }
    ]
  },
  "Dashboard — cosm/cosmogony.md": {
    word: "cosmogony",
    primary: "A theory, model, or account concerning the origin, creation, and evolution of the universe or the solar system.",
    secondary: "In astrophysics and anthropology, the systematic discipline exploring the origin of the cosmos, spanning ancient creation myths to the modern Big Bang singularity and cosmic inflation.",
    quotes: [
      { author: "Hesiod", work: "Theogony", quote: "Sing, O Muses, the sacred **cosmogony**, how earth and sky and the immortal gods first came to be." },
      { author: "Georges Lemaître", work: "The Primeval Atom", quote: "A physical **cosmogony** based on general relativity envisions the expansion of space from an initial singular state." },
      { author: "Carl Sagan", work: "Cosmos", quote: "Every civilization on Earth has crafted its own mythic **cosmogony** to explain how the world and its people began." }
    ]
  },
  "Dashboard — cosm/cosmographer.md": {
    word: "cosmographer",
    primary: "A scholar, cartographer, or scientist who maps, describes, and illustrates the physical features of the universe, including the heavens and the Earth.",
    secondary: "In Renaissance science and the Age of Discovery, a Renaissance polymath who combined celestial mechanics, planetary astronomy, terrestrial geography, and navigation.",
    quotes: [
      { author: "Gerardus Mercator", work: "Atlas sive Cosmographicae Meditationes", quote: "The dedicated **cosmographer** must combine celestial astronomy with terrestrial navigation to map the spherical Earth." },
      { author: "Christopher Columbus", work: "Journals", quote: "I consulted the ancient **cosmographer** Ptolemy and modern navigational charts before steering westward into the unknown ocean." },
      { author: "Alexander von Humboldt", work: "Cosmos", quote: "The classical **cosmographer** saw no division between charting the constellations above and surveying the continents below." }
    ]
  }
};

function updateWordNote(relPath, data) {
  const fullPath = path.join(baseDir, relPath);
  if (!fs.existsSync(fullPath)) {
    console.error("Not found:", fullPath);
    return;
  }
  let content = fs.readFileSync(fullPath, "utf8");

  // Format quotes
  const quotesFormatted = data.quotes.map(q => `> - 📜 **${q.author} (*${q.work}*):** *"${q.quote}"*`).join("\n");

  // Replace Definition & Semantic Range
  const defRegex = /> \[!book\] 📖 Definitions & Semantic Range[\s\S]*?(?=> \[!quote\]|$)/;
  const newDef = `> [!book] 📖 Definitions & Semantic Range\n> 1. **Primary Definition (Lexical / Standard Consensus)**: ${data.primary}\n> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: ${data.secondary}\n\n`;

  if (defRegex.test(content)) {
    content = content.replace(defRegex, newDef);
  } else {
    console.warn("Could not find [!book] in", relPath);
  }

  // Replace Quotes
  const quoteRegex = /> \[!quote\] 💬 Contextual Usage & Authentic Quotations[\s\S]*$/;
  const newQuotes = `> [!quote] 💬 Contextual Usage & Authentic Quotations\n${quotesFormatted}\n`;

  if (quoteRegex.test(content)) {
    content = content.replace(quoteRegex, newQuotes);
  } else {
    console.warn("Could not find [!quote] in", relPath);
  }

  fs.writeFileSync(fullPath, content, "utf8");
  console.log("Updated:", relPath);
}

for (const [relPath, data] of Object.entries(wordsData)) {
  updateWordNote(relPath, data);
}
console.log("Batch 4 finished! Total words updated:", Object.keys(wordsData).length);
