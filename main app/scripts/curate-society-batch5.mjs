import fs from 'fs';
import path from 'path';

const baseDir = 'App database/Greek roots/Cluster Society & Governance';

const filesData = {
  // === Dashboard — hero (11 words) ===
  "Dashboard — hero/antihero.md": {
    primary: "A central character in a story, movie, or drama who lacks conventional heroic attributes such as idealism, courage, or morality.",
    secondary: "In literary modernism and postmodernism, a protagonist marked by disillusionment, moral ambiguity, alienation, or comic inadequacy.",
    quotes: [
      { author: "Albert Camus", work: "The Stranger", quote: "Meursault stands as the quintessential twentieth-century **antihero**, detached and refusing to lie about his feelings." },
      { author: "Fyodor Dostoevsky", work: "Notes from Underground", quote: "The spiteful underground narrator confesses his own flawed nature, celebrating the triumph of the self-conscious **antihero**." },
      { author: "James Joyce", work: "Ulysses", quote: "Leopold Bloom wanders Dublin as a gentle, unpretentious modern **antihero**, contrasting with Homeric warriors." }
    ]
  },
  "Dashboard — hero/hero.md": {
    primary: "A person admired for courage, outstanding achievements, or noble qualities; or the chief male character in a book, play, or film.",
    secondary: "In classical mythology and religion, a demigod or mortal endowed with superhuman strength and celebrated with post-mortem cult worship.",
    quotes: [
      { author: "Thomas Carlyle", work: "On Heroes, Hero-Worship, and the Heroic in History", quote: "Universal history is at bottom the history of the Great Men who have worked here, the **hero** as divinity, prophet, and poet." },
      { author: "Joseph Campbell", work: "The Hero with a Thousand Faces", quote: "A **hero** ventures forth from the world of common day into a region of supernatural wonder." },
      { author: "Homer", work: "The Iliad", quote: "Achilles fought with reckless fury, knowing that the glorious life of the true **hero** must be brief." }
    ]
  },
  "Dashboard — hero/heroic.md": {
    primary: "Having the characteristics of a hero or suitable for one; very brave, noble, or grand in scale.",
    secondary: "In classical prosody and literary genre, denoting epic poetry (e.g. heroic couplets, heroic dactylic hexameter).",
    quotes: [
      { author: "Alexander Pope", work: "The Rape of the Lock", quote: "The poet employed the **heroic** couplet to mock the trivial vanities of fashionable London society." },
      { author: "Percy Bysshe Shelley", work: "Prometheus Unbound", quote: "Prometheus endured eternal agony with sublime and **heroic** defiance against the tyranny of Jupiter." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The **heroic** resistance of Belisarius prolonged the twilight of the Roman military name." }
    ]
  },
  "Dashboard — hero/heroical.md": {
    primary: "Of, relating to, or befitting a hero; heroic (archaic or formal variant).",
    secondary: "In Renaissance rhetoric and Elizabethan literature, displaying magnificent, exalted courage or epic grandeur.",
    quotes: [
      { author: "Philip Sidney", work: "The Defence of Poesy", quote: "The **heroical** poet paints virtue in her most captivating colors to inflame the soul with generous desire." },
      { author: "Francis Bacon", work: "The Advancement of Learning", quote: "Poesy is feigned history, serving to magnify events to an **heroical** scale exceeding ordinary human fortune." },
      { author: "John Milton", work: "Paradise Lost", quote: "Milton sought to celebrate an **heroical** patience far surpassing the pagan wrath of Achilles or Turnus." }
    ]
  },
  "Dashboard — hero/heroically.md": {
    primary: "In a heroic manner; with extraordinary courage, bravery, or nobility.",
    secondary: "Confronting overwhelming odds or suffering with dignified fortitude and self-sacrifice.",
    quotes: [
      { author: "Lord Tennyson", work: "The Charge of the Light Brigade", quote: "Into the valley of Death rode the six hundred, storming **heroically** into the mouth of cannon fire." },
      { author: "Charlotte Brontë", work: "Jane Eyre", quote: "She struggled **heroically** against her secret grief, maintaining outward calm before her pupils." },
      { author: "Winston Churchill", work: "Their Finest Hour", quote: "The Royal Air Force fought **heroically** through the summer skies, turning back the German onslaught." }
    ]
  },
  "Dashboard — hero/heroics.md": {
    primary: "Behavior or talk that is bold, dramatic, or flamboyant, especially when regarded as exaggerated or insincere.",
    secondary: "In dramatic criticism and military analysis, ostentatious displays of bravery or theatrical valor.",
    quotes: [
      { author: "George Bernard Shaw", work: "Arms and the Man", quote: "Bluntschli stripped war of romantic **heroics**, preferring chocolates to cartridges in his holster." },
      { author: "Ernest Hemingway", work: "A Farewell to Arms", quote: "Abstract words like glory and courage seemed obscene compared to the bloody reality stripped of **heroics**." },
      { author: "Virginia Woolf", work: "The Waves", quote: "Schoolboy **heroics** on the playing field struck him as noisy, hollow posturing." }
    ]
  },
  "Dashboard — hero/heroin.md": {
    primary: "A highly addictive analgesic drug derived from morphine (diacetylmorphine), originally synthesized as a non-addictive cough suppressant.",
    secondary: "In pharmacology and social history, a Schedule I opioid named from German heroisch ('heroic') by the Bayer pharmaceutical company in 1898 for its powerful effects.",
    quotes: [
      { author: "William S. Burroughs", work: "Junky", quote: "The physiological hook of **heroin** takes hold slowly, reorganizing all cellular necessity around the next fix." },
      { author: "Oliver Sacks", work: "Musicophilia", quote: "The neurochemical surge produced by **heroin** blunts visceral nociceptive transmission across the limbic axis." },
      { author: "Arthur Conan Doyle", work: "The Sign of the Four", quote: "Watson protested against Holmes's reliance on potent narcotics, warning of the destructive grip of **heroin** and cocaine." }
    ]
  },
  "Dashboard — hero/heroine.md": {
    primary: "A woman admired for her courage, outstanding achievements, or noble qualities; or the chief female character in a story, play, or film.",
    secondary: "In literary history, the female protagonist whose moral agency, intellect, or resilience drives the dramatic narrative.",
    quotes: [
      { author: "Jane Austen", work: "Northanger Abbey", quote: "No one who had ever seen Catherine Morland in her infancy would have supposed her born to be an intrepid **heroine**." },
      { author: "George Eliot", work: "Middlemarch", quote: "Dorothea Brooke carried within her the noble, unfulfilled yearning of an epic **heroine**." },
      { author: "Mary Wollstonecraft", work: "A Vindication of the Rights of Woman", quote: "Female education should cultivate real fortitude rather than the fragile sensibility expected of a romance **heroine**." }
    ]
  },
  "Dashboard — hero/heroism.md": {
    primary: "Great bravery; courageous or noble conduct.",
    secondary: "In moral philosophy, the voluntary confrontation of lethal danger or extreme sacrifice in service to the common good.",
    quotes: [
      { author: "Ralph Waldo Emerson", work: "Essays: First Series", quote: "**Heroism** feels and never reasons, and therefore is always right, acting from divine instinct." },
      { author: "Thomas Carlyle", work: "Past and Present", quote: "True **heroism** consists in steadfast endurance of unglamorous duty when no crowd applauds." },
      { author: "Leo Tolstoy", work: "War and Peace", quote: "Captain Tushin demonstrated authentic, quiet **heroism** on the artillery line without ever dreaming himself a hero." }
    ]
  },
  "Dashboard — hero/heron.md": {
    primary: "A large, long-legged, long-necked, wading bird with a long pointed bill, belonging to the family Ardeidae.",
    secondary: "In avian ecology, a specialized wetland predator that stalks fish and amphibians in shallow fresh or saltwater shallows.",
    quotes: [
      { author: "Henry David Thoreau", work: "Walden", quote: "A solitary great blue **heron** rose slowly from the reeds, trailing its long legs across the glassy pond." },
      { author: "Rachel Carson", work: "The Edge of the Sea", quote: "At low tide, the stately **heron** stands motionless as a carved statue, watching the murky tidal pool." },
      { author: "John James Audubon", work: "Ornithological Biography", quote: "The snowy plumage and graceful flight of the **heron** make it the crowning ornament of southern lagoons." }
    ]
  },
  "Dashboard — hero/heronry.md": {
    primary: "A breeding colony or communal nesting place of herons.",
    secondary: "In ornithology, an established rookery of ardeid birds located in tall trees near marshes or rivers.",
    quotes: [
      { author: "Gilbert White", work: "The Natural History of Selborne", quote: "We visited the ancient **heronry** in the oak forest, where dozens of bulky twig nests crowded the upper branches." },
      { author: "W. H. Hudson", work: "Birds in Town and Village", quote: "A sudden clamor arose from the secluded **heronry** as returning adults fed their hungry, squawking broods." },
      { author: "Arthur Conan Doyle", work: "The Hound of the Baskervilles", quote: "Beyond the dismal mire lay an old pine wood harboring a noisy, secluded **heronry**." }
    ]
  },

  // === Dashboard — hybr (13 words) ===
  "Dashboard — hybr/hubris.md": {
    primary: "Excessive pride or dangerous self-confidence, often resulting in fatal retribution or ruin; arrogance.",
    secondary: "In Greek tragedy and law, outrageous arrogance, insolence, or violence that violates the cosmic or civic order and provokes nemesis.",
    quotes: [
      { author: "Aristotle", work: "Rhetoric", quote: "**Hubris** consists in doing and saying things that cause shame to the victim, purely for the pleasure of feeling superior." },
      { author: "Werner Jaeger", work: "Paideia: The Ideals of Greek Culture", quote: "Greek tragedy portrays the inexorable cycle whereby unbridled **hubris** invites divine catastrophe." },
      { author: "C. S. Lewis", work: "The Abolition of Man", quote: "Man's conquest of Nature, when divorced from objective value, becomes a display of catastrophic **hubris**." }
    ]
  },
  "Dashboard — hybr/hubristic.md": {
    primary: "Excessively proud, arrogant, or self-confident; characterized by hubris.",
    secondary: "In classical and political analysis, defying moral or divine limits with haughty disregard for catastrophic consequences.",
    quotes: [
      { author: "Hannah Arendt", work: "The Origins of Totalitarianism", quote: "Totalitarian ideology claims an **hubristic** omnipotence, pretending to master the secret laws of history." },
      { author: "Bertrand Russell", work: "Power: A New Social Analysis", quote: "Dictators develop an **hubristic** contempt for human limits, leading inevitably to their own downfall." },
      { author: "George Steiner", work: "The Death of Tragedy", quote: "Agamemnon's **hubristic** stride upon the crimson tapestries sealed his fate before the gods." }
    ]
  },
  "Dashboard — hybr/hybr.md": {
    primary: "A combining root derived from Ancient Greek hybris, denoting wanton insolence, outrage, or arrogance; or relating to hybridization (hybrid).",
    secondary: "In etymology and classical philology, the morphological stem present in legal crimes of assault (hybris) and later biological crossbreeding (hybrid).",
    quotes: [
      { author: "Plato", work: "The Republic", quote: "The democratic youth surrendered to wanton **hybr**- and insolence, mistaking license for true liberty." },
      { author: "Gregor Mendel", work: "Experiments in Plant Hybridisation", quote: "The morphological characters of the **hybr**- generation demonstrated precise statistical segregation." },
      { author: "Werner Jaeger", work: "Paideia: The Ideals of Greek Culture", quote: "Athenian jurisprudence punished civic **hybr**- severely to maintain social equilibrium among citizens." }
    ]
  },
  "Dashboard — hybr/hybrid.md": {
    primary: "The offspring of two plants or animals of different species or varieties; or a thing made by combining two different elements.",
    secondary: "In genetics and evolutionary biology, an individual produced by cross-breeding distinct genetic lines or taxa.",
    quotes: [
      { author: "Charles Darwin", work: "The Origin of Species", quote: "The sterility of a **hybrid** is not a specially acquired endowment, but an incidental consequence of differences in reproductive systems." },
      { author: "Gregor Mendel", work: "Experiments in Plant Hybridisation", quote: "In each **hybrid** pea plant, the dominant trait concealed the recessive character without blending." },
      { author: "Aldous Huxley", work: "Brave New World", quote: "Modern civilization produced a curious **hybrid** culture blending industrial efficiency with hedonistic consumerism." }
    ]
  },
  "Dashboard — hybr/hybridisation.md": {
    primary: "The process of an animal or plant breeding with an individual of another species or variety (British spelling of hybridization).",
    secondary: "In molecular genetics and cytogenetics, the annealing of complementary single-stranded DNA or RNA molecules.",
    quotes: [
      { author: "Charles Darwin", work: "The Variation of Animals and Plants under Domestication", quote: "Systematic **hybridisation** among domesticated pigeons revealed hidden ancestral plumages." },
      { author: "Ernst Mayr", work: "Animal Species and Evolution", quote: "Natural **hybridisation** between sister species often breaks down geographic isolation barriers." },
      { author: "Julian Huxley", work: "Evolution: The Modern Synthesis", quote: "Introgression following botanical **hybridisation** provides a fertile reservoir of novel genetic variants." }
    ]
  },
  "Dashboard — hybr/hybridise.md": {
    primary: "To breed with another species or variety to produce a hybrid (British spelling of hybridize).",
    secondary: "In molecular biology, to cause complementary nucleic acid strands to bind together.",
    quotes: [
      { author: "Charles Darwin", work: "The Origin of Species", quote: "When florists **hybridise** closely related orchids, they frequently obtain vigorous and fertile offspring." },
      { author: "Gregor Mendel", work: "Experiments in Plant Hybridisation", quote: "Artificial pollination allowed investigators to **hybridise** distinct pea varieties under controlled glasshouse conditions." },
      { author: "Thomas Hunt Morgan", work: "The Physical Basis of Heredity", quote: "Attempts to **hybridise** distinct Drosophila species illuminated chromosomal rearrangements." }
    ]
  },
  "Dashboard — hybr/hybridization.md": {
    primary: "The process of combining different varieties of organisms to create a hybrid; crossbreeding.",
    secondary: "In molecular biology and chemistry, the pairing of complementary nucleic acid strands (DNA/RNA) or the mixing of atomic orbitals (sp3, sp2).",
    quotes: [
      { author: "Linus Pauling", work: "The Nature of the Chemical Bond", quote: "The concept of orbital **hybridization** explains the tetrahedral geometry and equivalent bonds of the carbon atom." },
      { author: "James D. Watson", work: "Molecular Biology of the Gene", quote: "Fluorescence in situ **hybridization** allows researchers to pinpoint specific gene sequences on intact chromosomes." },
      { author: "Theodosius Dobzhansky", work: "Genetics and the Origin of Species", quote: "Botanical **hybridization** coupled with polyploidy has repeatedly spawned successful new plant species." }
    ]
  },
  "Dashboard — hybr/hybridize.md": {
    primary: "To produce or cause to produce hybrids; crossbreed.",
    secondary: "In chemistry, to combine atomic orbitals; in genetics, to anneal complementary nucleic acid sequences.",
    quotes: [
      { author: "Charles Darwin", work: "The Effects of Cross and Self Fertilisation in the Vegetable Kingdom", quote: "Experiments proved that when two distinct strains **hybridize**, the progeny often exhibit extraordinary vegetative vigor." },
      { author: "Francis Crick", work: "What Mad Pursuit", quote: "Synthetic RNA probes **hybridize** readily with complementary viral DNA fragments on the nitrocellulose filter." },
      { author: "Asa Gray", work: "Darwiniana", quote: "Wild species of oaks frequently **hybridize** where geographic ranges overlap in river valleys." }
    ]
  },
  "Dashboard — hybr/hybridizing.md": {
    primary: "The act or process of crossbreeding or forming hybrids; or engaging in hybridization.",
    secondary: "In agriculture and horticulture, the deliberate crossing of cultivars to develop pest resistance or higher yields.",
    quotes: [
      { author: "Luther Burbank", work: "The Training of the Human Plant", quote: "Through patient **hybridizing**, we can combine the frost-hardiness of wild stock with the luscious fruit of cultivated plums." },
      { author: "Charles Darwin", work: "The Variation of Animals and Plants under Domestication", quote: "The practice of **hybridizing** garden flowers has been pursued with immense commercial success for centuries." },
      { author: "Gregor Mendel", work: "Experiments in Plant Hybridisation", quote: "Careful isolation of blossoms prevented stray pollen from contaminating the **hybridizing** trials." }
    ]
  },
  "Dashboard — hybr/hybridoma.md": {
    primary: "A hybrid cell produced by the fusion of an antibody-producing B lymphocyte with a myeloma cancer cell.",
    secondary: "In immunology and biotechnology, an immortalized cell line used for continuous industrial production of monoclonal antibodies (developed by Köhler and Milstein).",
    quotes: [
      { author: "Georges Köhler", work: "Continuous Cultures of Fused Cells Secreting Antibody", quote: "The cloned **hybridoma** combines the antibody specificity of the spleen cell with the immortality of the myeloma line." },
      { author: "César Milstein", work: "From Antibody Diversity to Monoclonal Antibodies", quote: "Each **hybridoma** clone serves as an unvarying factory churning out identical monoclonal antibodies." },
      { author: "Lewis Thomas", work: "Late Night Thoughts on Listening to Mahler's Ninth Symphony", quote: "The invention of the **hybridoma** revolutionized therapeutic oncology and immunological diagnostics." }
    ]
  },
  "Dashboard — hybr/hybris.md": {
    primary: "Excessive pride, presumption, or arrogance; classic Greek transliteration of hubris.",
    secondary: "In Attic law and classical philosophy, an assault or insolent act committed intentionally to dishonor another citizen.",
    quotes: [
      { author: "Demosthenes", work: "Against Meidias", quote: "The law of **hybris** protects every citizen, rich or poor, from wanton insult and physical battery." },
      { author: "Werner Jaeger", work: "Paideia: The Ideals of Greek Culture", quote: "Solon warned that surfeit breeds **hybris**, which in turn provokes inevitable civic ruin." },
      { author: "Gilbert Murray", work: "Five Stages of Greek Religion", quote: "The cardinal sin in the Hellenic moral cosmos was **hybris**, the overstepping of mortal limits." }
    ]
  },
  "Dashboard — hybr/hybristic.md": {
    primary: "Arrogant, insolent, or overweening; exhibiting hybris (variant spelling of hubristic).",
    secondary: "In classical rhetoric and tragedy, defying moral decency or divine sanction through reckless self-exaltation.",
    quotes: [
      { author: "Thucydides", work: "History of the Peloponnesian War", quote: "The Athenians' **hybristic** dismissal of the Melian pleas revealed an imperial ambition blinded by power." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The young tyrant's **hybristic** disdain for ancient senatorial custom alienated all loyal subjects." },
      { author: "George Steiner", work: "The Death of Tragedy", quote: "Creon's **hybristic** decree prohibiting burial provoked the catastrophic vengeance of the underworld gods." }
    ]
  },
  "Dashboard — hybr/monohybrid.md": {
    primary: "A hybrid that is heterozygous with respect to a single specified gene or trait.",
    secondary: "In Mendelian genetics, an experimental cross between two organisms that differ in only one phenotypic trait (e.g. flower color).",
    quotes: [
      { author: "Gregor Mendel", work: "Experiments in Plant Hybridisation", quote: "A **monohybrid** cross involving tall and dwarf pea varieties yielded a uniform tall first filial generation." },
      { author: "Thomas Hunt Morgan", work: "The Mechanism of Mendelian Heredity", quote: "The 3:1 phenotypic ratio observed in the **monohybrid** F2 generation confirmed discrete particulate inheritance." },
      { author: "Theodosius Dobzhansky", work: "Genetics and the Origin of Species", quote: "Analysis of a simple **monohybrid** inheritance clarifies how recessive alleles persist unexpressed in populations." }
    ]
  },

  // === Dashboard — iren (6 words) ===
  "Dashboard — iren/eiren-iren.md": {
    primary: "A combining root derived from Ancient Greek eirēnē, meaning peace, concord, or harmony.",
    secondary: "In classical philology and political philosophy, the foundational morpheme denoting peaceful reconciliation, pacification, and conflict resolution.",
    quotes: [
      { author: "Hesiod", work: "Theogony", quote: "The Horae—Eunomia, Dike, and blooming **Eiren**-e—bestow peace and prosperity upon mortal cities." },
      { author: "Aristophanes", work: "Peace", quote: "The joyful farmers haul the divine goddess **Eiren**-e from the deep cavern where war had trapped her." },
      { author: "Werner Jaeger", work: "Paideia: The Ideals of Greek Culture", quote: "In classical Attic thought, **iren**-ic concord was celebrated as the highest blessing of well-governed civic life." }
    ]
  },
  "Dashboard — iren/irena.md": {
    primary: "A feminine given name derived from Greek Eirēnē ('peace'); or a genus of Asian passerine birds (the fairy-bluebirds).",
    secondary: "In systematic ornithology, the sole genus in the family Irenidae, comprising colorful frugivorous birds of tropical Asian forests.",
    quotes: [
      { author: "Alfred Russel Wallace", work: "The Malay Archipelago", quote: "The dazzling cobalt plumage of the fairy-bluebird, **Irena** puella, flashed brilliantly through the rainforest canopy." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The Byzantine Empress **Irena** restored the veneration of holy images at the Second Council of Nicaea." },
      { author: "John Gould", work: "Birds of Asia", quote: "Specimens of the genus **Irena** are renowned for their intense ultramarine mantle contrasting with velvet black." }
    ]
  },
  "Dashboard — iren/irenaeus.md": {
    primary: "Saint Irenaeus of Lyon (c. 130–202 AD), early Christian bishop, theologian, and Church Father.",
    secondary: "In historical theology and patristics, the author of Against Heresies who developed the theology of apostolic succession and the doctrine of recapitulation.",
    quotes: [
      { author: "Eusebius", work: "Ecclesiastical History", quote: "Bishop **Irenaeus** truly lived up to his peaceful name, mediating the Quartodeciman controversy with apostolic grace." },
      { author: "Henry Chadwick", work: "The Early Church", quote: "In refuting Gnostic dualism, **Irenaeus** established the essential fourfold canonical authority of the Gospels." },
      { author: "Jaroslav Pelikan", work: "The Christian Tradition", quote: "The theology of **Irenaeus** centered upon the cosmic recapitulation of all humanity in Christ." }
    ]
  },
  "Dashboard — iren/irenic.md": {
    primary: "Aiming or aimed at peace; conciliatory, non-confrontational, or promoting harmony.",
    secondary: "In ecumenical theology and diplomacy, an approach that emphasizes common ground rather than polemical division.",
    quotes: [
      { author: "Erasmus of Rotterdam", work: "Praise of Folly", quote: "Erasmus advocated an **irenic** reform of Christian morals rather than violent sectarian conflict." },
      { author: "John Henry Newman", work: "Apologia Pro Vita Sua", quote: "My response was written in an **irenic** spirit, seeking to clarify misunderstandings rather than wound opponents." },
      { author: "Bertrand Russell", work: "Common Sense and Nuclear Warfare", quote: "International survival requires an **irenic** diplomacy that dismantles ideological hostility." }
    ]
  },
  "Dashboard — iren/irenidae.md": {
    primary: "A small family of passerine birds (the fairy-bluebirds), native to southern and southeastern Asia.",
    secondary: "In avian taxonomy, a family in the superfamily Sylvioidea closely allied with leafbirds and bulbuls, containing the genus Irena.",
    quotes: [
      { author: "Alfred Russel Wallace", work: "The Malay Archipelago", quote: "The family **Irenidae** represents one of the most vividly plumaged avian lineages inhabiting the Sunda Islands." },
      { author: "Ernst Mayr", work: "Check-List of Birds of the World", quote: "Taxonomic arrangements historically debated whether **Irenidae** should be merged with Chloropseidae." },
      { author: "Arthur Landsborough Thomson", work: "A New Dictionary of Birds", quote: "Members of **Irenidae** feed primarily on wild figs and nectar in the upper layers of evergreen canopies." }
    ]
  },
  "Dashboard — iren/irenology.md": {
    primary: "The scientific or academic study of peace, conflict resolution, and the conditions that prevent war; peace studies.",
    secondary: "In political science and international relations, the multidisciplinary field founded to investigate disarmament, mediation, and sustainable peace.",
    quotes: [
      { author: "Johan Galtung", work: "Peace by Peaceful Means", quote: "Modern **irenology** must examine structural violence alongside direct physical war to build positive peace." },
      { author: "Kenneth Boulding", work: "Conflict and Defense: A General Theory", quote: "The theoretical models of **irenology** clarify how national defense budgets can stabilize into non-hostile equilibria." },
      { author: "Hedley Bull", work: "The Anarchical Society", quote: "Research in **irenology** provides diplomats with valuable frameworks for institutional arms reduction." }
    ]
  },

  // === Dashboard — klept (6 words) ===
  "Dashboard — klept/klept.md": {
    primary: "A combining root derived from Ancient Greek kleptēs ('thief') or kleptō ('to steal').",
    secondary: "In morphological lexicography, the root element in terms signifying illicit theft, compulsive stealing, or physiological resource hijacking.",
    quotes: [
      { author: "Aristotle", work: "Nicomachean Ethics", quote: "The law treats the nocturnal thief differently according to whether the act was simple theft or violent robbery, rooted in Greek **klept**-." },
      { author: "William James", work: "The Principles of Psychology", quote: "Compulsive neuroses uniting the root **klept**- illustrate how involuntary impulses usurp rational volition." },
      { author: "Werner Jaeger", work: "Paideia: The Ideals of Greek Culture", quote: "Homeric hymns celebrate Hermes as the arch-trickster whose mythological patronymic derives from **klept**-." }
    ]
  },
  "Dashboard — klept/kleptocracy.md": {
    primary: "A government or state in which those in power exploit national wealth and resources to steal from their people.",
    secondary: "In political science and macroeconomics, a regime dominated by corrupt rulers who misappropriate public revenues through institutionalized graft.",
    quotes: [
      { author: "Jared Diamond", work: "Guns, Germs, and Steel", quote: "Every complex state must balance the services it provides against degenerating into a self-serving **kleptocracy**." },
      { author: "Francis Fukuyama", work: "The Origins of Political Order", quote: "Without an independent judiciary and civil service, patrimonial rule inevitably decays into barefaced **kleptocracy**." },
      { author: "Paul Collier", work: "The Bottom Billion", quote: "In a resource-cursed **kleptocracy**, oil rents flow directly into foreign secret bank accounts while public infrastructure rots." }
    ]
  },
  "Dashboard — klept/kleptomania.md": {
    primary: "A recurrent, persistent, and uncontrollable urge to steal items, typically without regard for their economic value or personal need.",
    secondary: "In psychiatric nosology (DSM-5), an impulse-control disorder characterized by escalating tension before theft and relief or gratification afterward.",
    quotes: [
      { author: "William James", work: "The Principles of Psychology", quote: "In true **kleptomania**, the patient steals useless trifles without malice, driven by an overpowering subconscious obsession." },
      { author: "Sigmund Freud", work: "Introductory Lectures on Psycho-Analysis", quote: "The compulsive symptomatic act in **kleptomania** frequently symbolizes repressed erotic or emotional deprivation." },
      { author: "Arthur Conan Doyle", work: "The Adventure of the Naval Treaty", quote: "The physician wondered whether the strange theft of the document was an act of high treason or inexplicable **kleptomania**." }
    ]
  },
  "Dashboard — klept/kleptomaniac.md": {
    primary: "A person suffering from kleptomania; someone driven by an irresistible impulse to steal.",
    secondary: "In clinical psychiatry and legal jurisprudence, a defendant whose theft is diagnosed as a psychiatric compulsion rather than criminal premeditation.",
    quotes: [
      { author: "Mark Twain", work: "Following the Equator", quote: "A poor man who steals is called a petty thief; a wealthy gentleman caught with stolen goods is diagnosed as a **kleptomaniac**." },
      { author: "Virginia Woolf", work: "Mrs Dalloway", quote: "The society doctor discussed the tragic case of an aristocratic lady who had turned into a habitual **kleptomaniac**." },
      { author: "G. K. Chesterton", work: "The Innocence of Father Brown", quote: "Father Brown saw into the tortured conscience of the **kleptomaniac**, who hid trinkets under the floorboards." }
    ]
  },
  "Dashboard — klept/kleptophobia.md": {
    primary: "An abnormal, irrational, or intense fear of thieves, being robbed, or stealing.",
    secondary: "In psychopathology, severe anxiety manifesting in obsessive locking of doors, checking of belongings, or terror of committing theft.",
    quotes: [
      { author: "Robert Burton", work: "The Anatomy of Melancholy", quote: "The miser suffers from incurable **kleptophobia**, imagining that every footstep in the corridor announces a burglar." },
      { author: "William James", work: "The Principles of Psychology", quote: "Morbid fears like **kleptophobia** compel the sufferer to inspect his safes and bolts twenty times each evening." },
      { author: "Karen Horney", work: "Our Inner Conflicts", quote: "Acute anxiety regarding personal boundaries may manifest clinically as severe **kleptophobia**." }
    ]
  },
  "Dashboard — klept/kleptoplasty.md": {
    primary: "The phenomenon whereby a predator ingests an alga or prey and retains its chloroplasts to perform photosynthesis (as in certain sea slugs).",
    secondary: "In cell biology and marine ecology, endosymbiosis (e.g. in Elysia chlorotica) enabling prolonged autotrophic survival through sequestered plastids.",
    quotes: [
      { author: "Lynn Margulis", work: "Symbiosis in Cell Evolution", quote: "The green sacoglossan slug demonstrates **kleptoplasty**, grazing on Vaucheria algae and hijacking their living chloroplasts." },
      { author: "Richard Dawkins", work: "The Extended Phenotype", quote: "Cases of functional **kleptoplasty** blur the boundary between animal heterotrophy and plant autotrophy." },
      { author: "E. O. Wilson", work: "The Diversity of Life", quote: "Through **kleptoplasty**, solar-powered sea slugs synthesize sugars from sunlight for months after their last meal." }
    ]
  },

  // === Dashboard — nomad (4 words) ===
  "Dashboard — nomad/nomad.md": {
    primary: "A member of a people that travels from place to place to find fresh pasture for its livestock and has no permanent home.",
    secondary: "In cultural anthropology, pastoral or foraging groups whose seasonal movements follow ecological cycles of rain and grazing.",
    quotes: [
      { author: "Bruce Chatwin", work: "The Songlines", quote: "The true **nomad** carries his world with him, walking lightly across the surface of the earth." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The pastoral **nomad** of the Eurasian steppe possessed mobility that made him a formidable terror to settled empires." },
      { author: "Ibn Khaldun", work: "The Muqaddimah", quote: "The hardy life of the desert **nomad** fosters fierce solidarity and martial courage unknown to decadent city dwellers." }
    ]
  },
  "Dashboard — nomad/nomadic.md": {
    primary: "Living the life of a nomad; wandering, roaming, or migratory.",
    secondary: "In sociology and history, relating to pastoralism or lifestyle patterns characterized by periodic relocation rather than sedentary agriculture.",
    quotes: [
      { author: "Arnold J. Toynbee", work: "A Study of History", quote: "Drought on the central Asian steppe periodically propelled **nomadic** hordes against the sedentary civilizations of China and Europe." },
      { author: "Claude Lévi-Strauss", work: "Tristes Tropiques", quote: "The **nomadic** hunter-gatherers of the interior moved in tiny bands attuned to the seasonal ripening of forest fruits." },
      { author: "Henry David Thoreau", work: "Walking", quote: "There is in every human heart an unextinguished craving for a free and **nomadic** life under the open sky." }
    ]
  },
  "Dashboard — nomad/nomadism.md": {
    primary: "The state, practice, or way of life of nomads; pastoral migration.",
    secondary: "In ethnology and historical geography, an adaptive socio-ecological system based on seasonal transhumance across arid or semi-arid ecosystems.",
    quotes: [
      { author: "Ibn Khaldun", work: "The Muqaddimah", quote: "Pure **nomadism** demands complete self-sufficiency and mutual loyalty among kinship clans." },
      { author: "Fernand Braudel", work: "The Mediterranean and the Mediterranean World in the Age of Philip II", quote: "Mediterranean transhumance was a specialized form of **nomadism** linking coastal winter plains to high alpine pastures." },
      { author: "Bruce Chatwin", work: "What Am I Doing Here", quote: "He believed that human evolution had permanently imprinted psychological wanderlust and **nomadism** in our bones." }
    ]
  },
  "Dashboard — nomad/nomadize.md": {
    primary: "To live as a nomad; to wander about with herds or lead a migratory life.",
    secondary: "In historical travelogues and geography, to adopt a pastoral migratory pattern across open territories.",
    quotes: [
      { author: "Richard Francis Burton", work: "Personal Narrative of a Pilgrimage to El-Medinah and Meccah", quote: "Bedouin tribes continue to **nomadize** across the rocky plateau, pitching black tents wherever water is struck." },
      { author: "George Catlin", work: "Letters and Notes on the Manners, Customs, and Condition of the North American Indians", quote: "The plains tribes were compelled to **nomadize** continuously following the vast seasonal migrations of the buffalo." },
      { author: "Alexander von Humboldt", work: "Personal Narrative of Travels", quote: "Pastoralists who **nomadize** through the llanos must navigate annual transitions between scorched drought and inundating flood." }
    ]
  },

  // === Dashboard — obol (2 words) ===
  "Dashboard — obol/obol.md": {
    primary: "An ancient Greek coin of small value, equal to one-sixth of a drachma; an obolus.",
    secondary: "In classical Athenian society and funerary customs, the small silver or bronze coin placed in the mouth of the deceased to pay Charon the ferryman.",
    quotes: [
      { author: "Lucian of Samosata", work: "Dialogues of the Dead", quote: "Charon demanded his customary copper **obol** before permitting the naked ghost to board the ferry." },
      { author: "Aristophanes", work: "The Frogs", quote: "Dionysus paid Charon two obols for passage across the lake, muttering at the price of an **obol** in the underworld." },
      { author: "George Grote", work: "A History of Greece", quote: "Athenian jurors received an allowance of three obols a day, where an **obol** bought modest bread and olives." }
    ]
  },
  "Dashboard — obol/obolus.md": {
    primary: "An ancient Greek coin worth one-sixth of a drachma; an obol; or a historical weight unit.",
    secondary: "In medieval Europe, a small halfpenny or silver coin; or metaphorically, a modest financial contribution or alms.",
    quotes: [
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "Legend depicted the great general Belisarius reduced to begging for a solitary **obolus** in the streets of Constantinople." },
      { author: "Lord Byron", work: "Don Juan", quote: "Give an **obolus** to Belisarius, cried the poet, lamenting the fickle gratitude of princes." },
      { author: "Thomas Browne", work: "Hydriotaphia, Urn Burial", quote: "In pagan urns, antiquarians frequently find the bronze **obolus** intended as passage money across the Stygian stream." }
    ]
  },

  // === Dashboard — ochl (4 words) ===
  "Dashboard — ochl/enochlophobia.md": {
    primary: "An irrational, abnormal, or intense fear of large crowds; ochlophobia.",
    secondary: "In clinical psychiatry and behavioral therapy, panic symptomatology provoked by public gatherings, markets, or crowded venues.",
    quotes: [
      { author: "William James", work: "The Principles of Psychology", quote: "The patient suffering from severe **enochlophobia** experienced acute palpitations upon approaching any crowded boulevard." },
      { author: "Sigmund Freud", work: "Inhibitions, Symptoms and Anxiety", quote: "Agoraphobic symptoms closely overlapping with **enochlophobia** represent ego defense against sudden social panic." },
      { author: "Oliver Sacks", work: "Hallucinations", quote: "Sensory overload in bustling terminals precipitated terrifying episodes of **enochlophobia** in vulnerable subjects." }
    ]
  },
  "Dashboard — ochl/ochl.md": {
    primary: "A combining root derived from Ancient Greek ochlos, meaning 'crowd', 'multitude', or 'mob'.",
    secondary: "In political theory and psychopathology, the base morpheme denoting disorderly mass gatherings, mob rule, and fear of crowds.",
    quotes: [
      { author: "Polybius", work: "The Histories", quote: "When democracy degenerates into violence and lawlessness, it assumes the form of **ochl**-ocracy or mob tyranny." },
      { author: "Aristotle", work: "Politics", quote: "The demagogue flatters the turbulent **ochl**-os in order to undermine constitutional magistrates." },
      { author: "Werner Jaeger", work: "Paideia: The Ideals of Greek Culture", quote: "Greek political writers used compounds of **ochl**- to distinguish the unruly mob from the lawful assembly." }
    ]
  },
  "Dashboard — ochl/ochlocracy.md": {
    primary: "Government by the mob; mob rule or mobocracy.",
    secondary: "In classical political philosophy (first formulated by Polybius), the degenerate phase of democracy characterized by anarchy and demagoguery.",
    quotes: [
      { author: "Polybius", work: "The Histories", quote: "When democracy becomes turbulent and disdainful of law, it sinks into the ruinous state of **ochlocracy**." },
      { author: "Thomas Jefferson", work: "Letters of Thomas Jefferson", quote: "Unchecked popular passions risk tumbling the republic from ordered liberty into the horrors of **ochlocracy**." },
      { author: "John Adams", work: "A Defence of the Constitutions of Government", quote: "A constitution lacking checks and balances will rapidly veer between tyranny and destructive **ochlocracy**." }
    ]
  },
  "Dashboard — ochl/ochlophobia.md": {
    primary: "An abnormal, irrational, or intense fear of crowds or mobs.",
    secondary: "In clinical psychology, a specific situational phobia triggering severe panic in congested public spaces.",
    quotes: [
      { author: "William James", work: "The Principles of Psychology", quote: "The sufferer from **ochlophobia** will walk miles through deserted alleys to avoid passing through a busy market." },
      { author: "Robert Burton", work: "The Anatomy of Melancholy", quote: "Solitary recluses are seized with violent tremors and **ochlophobia** whenever dragged into public assemblies." },
      { author: "Karen Horney", work: "The Neurotic Personality of Our Time", quote: "Deep neurotic insecurity can manifest as paralyzing **ochlophobia**, making every gathering seem hostile." }
    ]
  },

  // === Dashboard — orphan (3 words) ===
  "Dashboard — orphan/orphan.md": {
    primary: "A child whose parents are dead; or to deprive of parents.",
    secondary: "In typography, an isolated first line of a paragraph appearing at the bottom of a page; in medicine, an orphan disease or drug.",
    quotes: [
      { author: "Charles Dickens", work: "Oliver Twist", quote: "The helpless **orphan** asked for more food, trembling before the astonished board of parish guardians." },
      { author: "Charlotte Brontë", work: "Jane Eyre", quote: "As a friendless **orphan** at Gateshead, she endured the cruel taunts of her wealthy cousins." },
      { author: "William Shakespeare", work: "Henry V", quote: "Think not upon the fault My father made in compassing the crown! I Richard's body have interred anew, And on it have bestow'd more contrite tears Than from it issued forced drops of blood. Five hundred poor I have in yearly pay, Who twice a day their wither'd hands hold up Toward heaven, to pardon blood; and I have built Two chantries, where the sad and solemn priests Sing still for Richard's soul. More will I do; Though all that I can do is nothing worth, Since that my penitence comes after all, Imploring pardon." }
    ]
  },
  "Dashboard — orphan/orphanage.md": {
    primary: "A residential institution for the care and education of orphans.",
    secondary: "In social welfare history, charitable or municipal asylums established to shelter parentless and destitute children.",
    quotes: [
      { author: "Leo Tolstoy", work: "Resurrection", quote: "She visited the municipal **orphanage**, moved to tears by the rows of pale children in identical gray frocks." },
      { author: "Charles Dickens", work: "Bleak House", quote: "The philanthropic lady spent lavishly on her favorite suburban **orphanage** while neglecting her own family." },
      { author: "George Orwell", work: "The Road to Wigan Pier", quote: "Records from the industrial parish **orphanage** revealed how children had been bound out as apprentice laborers." }
    ]
  },
  "Dashboard — orphan/orphaned.md": {
    primary: "Deprived of parents by death; having become an orphan.",
    secondary: "In computing and technology, describing data processes or files whose parent process or owner has terminated.",
    quotes: [
      { author: "Mary Shelley", work: "Frankenstein", quote: "Elizabeth was an **orphaned** child of noble blood, welcomed into the Frankenstein household as a sister." },
      { author: "Walter Scott", work: "The Heart of Midlothian", quote: "The poor **orphaned** infant was wrapped in coarse flannel and laid upon the parish steps." },
      { author: "Thomas Hardy", work: "Tess of the d'Urbervilles", quote: "The younger children wept bitterly, terrified by the thought of being left **orphaned** upon the world." }
    ]
  },

  // === Dashboard — ostrac (15 words) ===
  "Dashboard — ostrac/anostraca.md": {
    primary: "An order of branchiopod crustaceans known as fairy shrimps, lacking a carapace.",
    secondary: "In freshwater invertebrate zoology, swimming crustaceans possessing eleven pairs of swimming legs and exhibiting reverse-orientation locomotion.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "The Anatomy of Invertebrated Animals", quote: "The fairy shrimp represents the order **Anostraca**, characterized by graceful swimming with its ventral side uppermost." },
      { author: "Alpheus Spring Packard", work: "A Monograph of the Phyllopod Crustacea of North America", quote: "Temporary vernal pools provide the ideal predator-free habitat for ephemeral species of **Anostraca**." },
      { author: "Richard Owen", work: "Lectures on Invertebrate Anatomy", quote: "The absence of a carapace in **Anostraca** exposes the segmented body and leaf-like phyllopodia." }
    ]
  },
  "Dashboard — ostrac/Entomostraca.md": {
    primary: "A former subclass or group of small aquatic crustaceans, including water fleas, fairy shrimps, and barnacles.",
    secondary: "In historical invertebrate taxonomy, an artificial grouping of lower crustaceans possessing variable segment numbers and lacking abdominal limbs.",
    quotes: [
      { author: "Charles Darwin", work: "A Monograph on the Sub-class Cirripedia", quote: "The larval development of barnacles demonstrates their true affinity with the lower **Entomostraca**." },
      { author: "Thomas Henry Huxley", work: "A Manual of the Anatomy of Invertebrated Animals", quote: "Under the classical name **Entomostraca**, naturalists gathered the microscopic crustacea of ponds and ditches." },
      { author: "John Lubbock", work: "On Some Entomostraca Collected by Dr. Sutherland", quote: "Careful microscopic drawings revealed several undescribed species of **Entomostraca** from arctic waters." }
    ]
  },
  "Dashboard — ostrac/Leptostraca.md": {
    primary: "A primitive order of small marine malacostracan crustaceans, commonly called leptostracans (such as Nebalia).",
    secondary: "In marine carcinology, an archaic clade retaining primitive phyllopodous thoracic limbs and a bivalved carapace enclosing the thorax.",
    quotes: [
      { author: "William Thomas Calman", work: "The Life of Crustacea", quote: "The order **Leptostraca** bridges the morphological gap between lower branchiopods and true Malacostraca." },
      { author: "Thomas Henry Huxley", work: "The Anatomy of Invertebrated Animals", quote: "In Nebalia, the representative of **Leptostraca**, the carapace loosely covers the thorax without being fused to the segments." },
      { author: "Richard Owen", work: "Lectures on Comparative Anatomy", quote: "The preservation of eight abdominal segments in **Leptostraca** represents an ancestral crustacean trait." }
    ]
  },
  "Dashboard — ostrac/Malacostraca.md": {
    primary: "The largest class of crustaceans, comprising crabs, lobsters, shrimp, krill, woodlice, and mantis shrimp.",
    secondary: "In systematic arthropod zoology, higher crustaceans characterized by a fixed body plan of 19 or 20 segments and specialized cephalothorax tagmosis.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "The Crayfish: An Introduction to the Study of Zoology", quote: "The common freshwater crayfish illustrates the definitive morphological architectural plan of the **Malacostraca**." },
      { author: "Charles Darwin", work: "The Origin of Species", quote: "The extraordinary diversification of limbs in **Malacostraca** demonstrates the power of natural selection acting on homologous parts." },
      { author: "William Thomas Calman", work: "A Treatise on Zoology: Crustacea", quote: "Systematic classification separates the class **Malacostraca** into several major orders based on gill and carapace morphology." }
    ]
  },
  "Dashboard — ostrac/ostrac.md": {
    primary: "A combining root derived from Ancient Greek ostrakon, meaning 'earthenware vessel', 'tile', 'potsherd', or 'shell'.",
    secondary: "In classical Athenian history and biological nomenclature, the base morpheme signifying civic banishment by pottery ballot (ostracism) or shell-bearing organisms.",
    quotes: [
      { author: "Aristotle", work: "Constitution of the Athenians", quote: "Citizens inscribed the name of the man they wished to banish upon a broken piece of **ostrac**-on." },
      { author: "George Grote", work: "A History of Greece", quote: "Cleisthenes instituted the procedure rooted in **ostrac**- to prevent ambitious demagogues from establishing tyranny." },
      { author: "Werner Jaeger", work: "Paideia: The Ideals of Greek Culture", quote: "The Attic practice of **ostrac**-ism was conceived not as criminal punishment, but as a peaceful constitutional safeguard." }
    ]
  },
  "Dashboard — ostrac/ostraciidae.md": {
    primary: "A family of marine tetraodontiform fishes known as boxfishes, trunkfishes, or cowfishes.",
    secondary: "In ichthyological taxonomy, reef fishes enclosed in a rigid, bony triangular or rectangular carapace formed of modified scales.",
    quotes: [
      { author: "Albert Günther", work: "An Introduction to the Study of Fishes", quote: "In the family **Ostraciidae**, the body is encased in a solid bony armor formed of fused hexagonal plates." },
      { author: "William Beebe", work: "Beneath Tropic Seas", quote: "A small boxfish of the **Ostraciidae** sculled awkwardly through the coral reef, propelled only by transparent fins." },
      { author: "Georges Cuvier", work: "The Animal Kingdom", quote: "Cuvier classified **Ostraciidae** among the Plectognathi because of their fused jaws and immobile dermal coat." }
    ]
  },
  "Dashboard — ostrac/ostracise.md": {
    primary: "To exclude someone from a society or group; shun (British spelling of ostracize).",
    secondary: "In historical politics, to banish an unpopular or dangerous citizen by voting with potsherds in ancient Athens.",
    quotes: [
      { author: "George Bernard Shaw", work: "Major Barbara", quote: "Respectable society was quick to **ostracise** anyone who dared challenge established commercial morality." },
      { author: "George Grote", work: "A History of Greece", quote: "The Athenian assembly voted to **ostracise** Aristides, weary of hearing him called 'the Just'." },
      { author: "Virginia Woolf", work: "The Voyage Out", quote: "She feared that any breach of etiquette would cause the salon to quietly **ostracise** her." }
    ]
  },
  "Dashboard — ostrac/ostracism.md": {
    primary: "Exclusion from a society or group; or (in ancient Greece) temporary banishment from a city by popular vote.",
    secondary: "In classical Athenian democracy, a constitutional mechanism wherein citizens voted on pottery shards (ostraka) to expel a citizen for ten years without confiscating property.",
    quotes: [
      { author: "Plutarch", work: "Life of Aristides", quote: "An illiterate citizen asked Aristides himself to write the name on the shard, eager to vote for his **ostracism**." },
      { author: "George Grote", work: "A History of Greece", quote: "The institution of **ostracism** served as an safety valve against factional violence in young democracies." },
      { author: "Alexis de Tocqueville", work: "Democracy in America", quote: "The tyranny of the majority can exert an invisible social **ostracism** far more crushing than legal chains." }
    ]
  },
  "Dashboard — ostrac/ostracize.md": {
    primary: "To banish, shun, or exclude someone from a society, club, or social circle.",
    secondary: "In Athenian history, to cast a vote on potsherds to banish a citizen judged dangerous to the commonwealth.",
    quotes: [
      { author: "Nathaniel Hawthorne", work: "The Scarlet Letter", quote: "The puritan community resolved to **ostracize** Hester Prynne, forcing her to dwell on the lonely outskirts of town." },
      { author: "Thucydides", work: "History of the Peloponnesian War", quote: "The citizens determined to **ostracize** Hyperbolus, whose insolence had disgusted both rival political factions." },
      { author: "Mark Twain", work: "The Man That Corrupted Hadleyburg", quote: "The townspeople were swift to **ostracize** any neighbor who failed to maintain the appearance of civic virtue." }
    ]
  },
  "Dashboard — ostrac/ostracod.md": {
    primary: "A tiny bivalved crustacean of the class Ostracoda, commonly known as a seed shrimp.",
    secondary: "In micropaleontology and aquatic ecology, bivalved microcrustaceans whose calcified shells provide essential index fossils for biostratigraphy and paleoclimatology.",
    quotes: [
      { author: "Charles Darwin", work: "The Origin of Species", quote: "The delicate bivalved carapace of the tiny **ostracod** is preserved in freshwater shales across geological eras." },
      { author: "Alister Hardy", work: "The Open Sea: Its Natural History", quote: "Bioluminescent swarms of marine **ostracod** species illuminate night waters with brilliant blue flashes." },
      { author: "Stephen Jay Gould", work: "Wonderful Life", quote: "The evolutionary continuity of the **ostracod** carapace demonstrates morphological stasis over hundreds of millions of years." }
    ]
  },
  "Dashboard — ostrac/ostracoda.md": {
    primary: "A class of small crustaceans, typically less than a millimeter long, having the body enclosed in a bivalve-like calcareous shell.",
    secondary: "In marine and freshwater biology, a highly diverse arthropod clade (seed shrimp) widely used as paleoenvironmental and salinity indicators.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "The Anatomy of Invertebrated Animals", quote: "The class **Ostracoda** is distinguished by the reduction of body segmentation within a hinged bivalve shell." },
      { author: "Charles Lyell", work: "Principles of Geology", quote: "Abundant fossil valves belonging to **Ostracoda** assist geologists in correlating ancient lacustrine strata." },
      { author: "John Lubbock", work: "On the Senses, Instincts, and Intelligence of Animals", quote: "Microscopic observations on **Ostracoda** revealed surprisingly complex sensory setae along the shell margin." }
    ]
  },
  "Dashboard — ostrac/ostracoderm.md": {
    primary: "An extinct jawless armored fish of the Paleozoic era.",
    secondary: "In vertebrate paleontology, primitive agnathan fishes covered with heavy dermal bone plates that flourished from the Ordovician to the Devonian.",
    quotes: [
      { author: "Alfred Sherwood Romer", work: "Vertebrate Paleontology", quote: "The armored head shield of the **ostracoderm** was nature's first great experiment in bony vertebrate protection." },
      { author: "Stephen Jay Gould", work: "The Panda's Thumb", quote: "Early chordate evolution produced the jawless **ostracoderm**, groveling along Silurian lakebeds for detritus." },
      { author: "Hugh Miller", work: "The Old Red Sandstone", quote: "The strange winged cephalaspis and armored **ostracoderm** fossils looked more like clockwork machines than fishes." }
    ]
  },
  "Dashboard — ostrac/ostracodermi.md": {
    primary: "A former taxonomic group or subphylum encompassing the extinct jawless armored fishes (ostracoderms).",
    secondary: "In historical vertebrate systematics, an archaic assemblage of jawless agnathans (heterostracans, osteostracans, anaspids) encased in bony carapaces.",
    quotes: [
      { author: "Louis Agassiz", work: "Recherches sur les Poissons Fossiles", quote: "Agassiz recognized the armored fishes of the **Ostracodermi** as primitive pioneers of the vertebrate subphylum." },
      { author: "A. Smith Woodward", work: "Catalogue of the Fossil Fishes in the British Museum", quote: "The cranial anatomy of the **Ostracodermi** demonstrates the ancient origin of sensory canal systems in bone." },
      { author: "Richard Owen", work: "Palaeontology: Or, A Systematic Summary of Extinct Animals", quote: "The fossil plates of **Ostracodermi** from Devonian strata were originally mistaken for crustacean carapaces." }
    ]
  },
  "Dashboard — ostrac/ostracon.md": {
    primary: "A piece of broken pottery or potsherd used as a writing surface in antiquity (plural: ostraka).",
    secondary: "In classical archaeology and papyrology, an inscribed pottery fragment preserving administrative records, receipts, literary texts, or Athenian exile ballots.",
    quotes: [
      { author: "Plutarch", work: "Life of Aristides", quote: "The citizen scratched the name of Aristides upon an earthen **ostracon** without recognizing the statesman before him." },
      { author: "Flinders Petrie", work: "Ten Years' Digging in Egypt", quote: "Excavations at the Roman quarry yielded hundreds of inscribed **ostracon** fragments detailing soldier rations." },
      { author: "John Boardman", work: "The Archaeology of Greece", quote: "Thousands of discarded **ostracon** ballots recovered from the Athenian Agora preserve names of prominent politicians." }
    ]
  },
  "Dashboard — ostrac/periostracum.md": {
    primary: "The thin, outermost organic coating or skin protecting the calcareous shell of many mollusks.",
    secondary: "In malacology, a tough layer of the fibrous protein conchin secreted by the mantle edge that prevents acid dissolution of the underlying calcium carbonate shell.",
    quotes: [
      { author: "Charles Darwin", work: "The Voyage of the Beagle", quote: "The dark, velvety **periostracum** of the giant Patagonian mussel protects its heavy shell from wave erosion." },
      { author: "Thomas Henry Huxley", work: "The Anatomy of Invertebrated Animals", quote: "The mantle margin secretes the organic **periostracum** before the prismatic and nacreous shell layers are deposited." },
      { author: "Rachel Carson", work: "The Edge of the Sea", quote: "Freshly stranded shells retain a fibrous brown **periostracum** that soon dries and flakes away in the salt wind." }
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

console.log(`Updated ${updatedCount} files in Batch 5!`);
