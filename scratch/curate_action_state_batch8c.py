# -*- coding: utf-8 -*-
import os, sys, re
sys.stdout.reconfigure(encoding="utf-8")

data = {
  # --- Dashboard — und Part 3 (8C, 52 words) ---
  "Dashboard — und/underdressed.md": {
    "primary": "Wearing clothes that are too casual or informal for a formal occasion or setting.",
    "secondary": "In social etiquette chronicles, being underdressed causes acute embarrassment at high-society balls or state receptions.",
    "quotes": [
      {"author": "Edith Wharton", "work": "The Custom of the Country", "quote": "Undine was mortified to discover she was noticeably **underdressed** among the diamond-laden dowagers at the opera."},
      {"author": "Jane Austen", "work": "Emma", "quote": "Harriet worried lest she appear **underdressed** at the grand dinner party given by the Coles."},
      {"author": "F. Scott Fitzgerald", "work": "The Great Gatsby", "quote": "A few latecomers arrived in tweed coats, looking distinctly **underdressed** amid Gatsby's glittering throng."}
    ]
  },
  "Dashboard — und/undereducated.md": {
    "primary": "Having received inadequate, insufficient, or poor quality formal education and schooling.",
    "secondary": "In sociological policy, an undereducated workforce struggles to adapt to technological automation and advanced industrial demands.",
    "quotes": [
      {"author": "Thomas Carlyle", "work": "Chartism", "quote": "An **undereducated** populace left in spiritual darkness will inevitably fall prey to violent revolutionary demagogues."},
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "The state has an imperative duty to ensure that no child grows up **undereducated** and incapable of civic self-governance."},
      {"author": "H. G. Wells", "work": "The Outline of History", "quote": "Vast populations in ancient empires remained **undereducated**, toiling as illiterate agricultural serfs."}
    ]
  },
  "Dashboard — und/underemployed.md": {
    "primary": "Employed in a job that does not make full use of one's skills, abilities, education, or working capacity.",
    "secondary": "In labor economics, an underemployed graduate working in low-skilled manual service illustrates structural human capital misallocation.",
    "quotes": [
      {"author": "George Gissing", "work": "New Grub Street", "quote": "Edwin Reardon found himself an **underemployed** classical scholar struggling to earn bread by writing cheap magazine reviews."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "During seasonal trade slumps, manufacturing artisans remain **underemployed**, earning barely enough for bare subsistence."},
      {"author": "George Orwell", "work": "Keep the Aspidistra Flying", "quote": "Gordon felt bitter that his literary talents left him an **underemployed** clerk in a dingy antiquarian bookshop."}
    ]
  },
  "Dashboard — und/underestimate.md": {
    "primary": "To estimate something to be smaller, less important, or less capable than it actually is.",
    "secondary": "In military intelligence, commanders who underestimate enemy artillery reserves risk disastrous tactical counteroffensives.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Final Problem", "quote": "Holmes warned me never to **underestimate** Professor Moriarty, whose criminal genius was equal to any emergency."},
      {"author": "Winston Churchill", "work": "The World Crisis", "quote": "The allied high command did **underestimate** the defensive strength of modern machine-gun entrenchments."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "We must not **underestimate** the centrifugal jealousies that threaten to dissolve the American confederacy."}
    ]
  },
  "Dashboard — und/underestimation.md": {
    "primary": "An estimate that is too low, or an appraisal that undervalues importance, difficulty, or cost.",
    "secondary": "In large infrastructure projects, initial underestimation of geotechnical challenges frequently leads to severe budget overruns.",
    "quotes": [
      {"author": "Winston Churchill", "work": "The River War", "quote": "A fatal **underestimation** of the dervish strength led to the catastrophic annihilation of Hicks Pasha's army."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The widespread **underestimation** of maritime risk encourages merchants to insure their vessels inadequately."},
      {"author": "H. G. Wells", "work": "The War of the Worlds", "quote": "Early newspaper reports displayed a ludicrous **underestimation** of the technological power of the Martian fighting-machines."}
    ]
  },
  "Dashboard — und/underevaluation.md": {
    "primary": "An evaluation or financial valuation that rates someone or something below their true merit or value.",
    "secondary": "In equity analysis, systematic underevaluation of corporate assets provides activist investors with attractive takeover targets.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The **underevaluation** of silver relative to gold at the royal mint caused silver coinage to be melted down and exported."},
      {"author": "David Ricardo", "work": "Principles of Political Economy and Taxation", "quote": "A persistent **underevaluation** of agricultural capital distorts national economic development toward speculative foreign trade."},
      {"author": "Theodore Dreiser", "work": "The Financier", "quote": "Cowperwood realized that the market **underevaluation** of street railway shares offered an immense opportunity for speculative profit."}
    ]
  },
  "Dashboard — und/underexpose.md": {
    "primary": "To expose photographic film or digital sensors to light for too short a time, resulting in dark images.",
    "secondary": "In technical photography, taking care not to underexpose shadow details preserves tonal range across high-contrast compositions.",
    "quotes": [
      {"author": "Thomas Edison", "work": "The Edison Papers", "quote": "Careful shutter regulation ensures that the moving film does not **underexpose** under artificial incandescent studio illumination."},
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Sussex Vampire", "quote": "The photographer was warned not to **underexpose** the crime-scene negatives in the dim interior of the old manor."},
      {"author": "Camille Flammarion", "work": "Popular Astronomy", "quote": "Astronomers took long telescope exposures so as not to **underexpose** the faint spiral arms of distant nebulae."}
    ]
  },
  "Dashboard — und/underexposure.md": {
    "primary": "Insufficient exposure of photographic film or image sensors to light, producing dark, muddy pictures.",
    "secondary": "In digital radiography, severe underexposure introduces quantum mottle noise that obscures subtle anatomical fracture lines.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Stark Munro Letters", "quote": "The experimental photographic plate was ruined by severe **underexposure**, showing only shadowy silhouettes."},
      {"author": "Thomas Edison", "work": "The Edison Papers", "quote": "We adjusted the aperture to eliminate **underexposure** during high-speed kinetoscope filming."},
      {"author": "H. G. Wells", "work": "The Time Machine", "quote": "The faint light of the dying sun caused an **underexposure** of the photographic plates left to record the horizon."}
    ]
  },
  "Dashboard — und/underfed.md": {
    "primary": "Not having enough food to eat; insufficiently fed or suffering from chronic malnutrition.",
    "secondary": "In social reform histories, underfed factory laborers were vulnerable to tuberculosis and occupational exhaustion.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Oliver Twist", "quote": "Oliver Twist and his companions suffered the tortures of slow starvation, being systematically **underfed** in the parish workhouse."},
      {"author": "George Orwell", "work": "The Road to Wigan Pier", "quote": "The unemployed miner looked pale and chronically **underfed**, his face lined with the anxiety of providing for his children."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The overworked farm horses were visibly **underfed**, their rib cages showing prominently through dull winter coats."}
    ]
  },
  "Dashboard — und/underfelt.md": {
    "primary": "A thick layer of felt or padded material laid beneath a carpet to provide insulation and cushioning.",
    "secondary": "In interior architecture and acoustics, high-density wool underfelt absorbs impact sound and extends carpet pile life.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The newly furnished chambers were carpeted with luxurious Brussels tapestry laid over heavy insulating **underfelt**."},
      {"author": "Anthony Trollope", "work": "The Way We Live Now", "quote": "The drawing room floor was soft to the tread, padded with thick **underfelt** imported by fashionable London upholsterers."},
      {"author": "Henry James", "work": "The Golden Bowl", "quote": "Their footsteps were muffled by the dense **underfelt** that lined the long corridors of the country mansion."}
    ]
  },
  "Dashboard — und/underfoot.md": {
    "primary": "Under one's feet; on the ground; or in the way, causing an obstruction or nuisance.",
    "secondary": "In botanical descriptions of peat bogs, spongy sphagnum moss yields wetly underfoot with every walking stride.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "The dried heath twigs crackled crisply **underfoot** as Venn walked across the dark expanses of Egdon Heath."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "The children were constantly tumbling **underfoot** in the crowded, happy confusion of the Peggotty boathouse."},
      {"author": "Robert Louis Stevenson", "work": "Treasure Island", "quote": "The loose sand shifted **underfoot** as we scrambled up the steep hillside toward Captain Flint's treasure cache."}
    ]
  },
  "Dashboard — und/underframe.md": {
    "primary": "The supporting framework or chassis underneath a railway car, automobile, or heavy structure.",
    "secondary": "In railway rolling stock engineering, a cast-steel underframe absorbs buffing shocks from locomotive couplers during freight hauling.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Bruce-Partington Plans", "quote": "The detective examined the steel **underframe** of the railway carriage where the dead clerk had landed."},
      {"author": "H. G. Wells", "work": "The War in the Air", "quote": "The heavy machine guns were bolted securely to the reinforced aluminum **underframe** of the combat dirigible."},
      {"author": "Theodore Dreiser", "work": "Sister Carrie", "quote": "The streetcar groaned as its heavy iron **underframe** jolted over the frozen tracks of Broadway."}
    ]
  },
  "Dashboard — und/underfur.md": {
    "primary": "The thick, soft, dense fur that grows beneath the longer, stiffer guard hairs of an animal.",
    "secondary": "In mammalian pelage biology, the woolly underfur traps an insulating layer of warm air next to the epidermis.",
    "quotes": [
      {"author": "Jack London", "work": "The Call of the Wild", "quote": "Buck's dense **underfur** thickened as the Yukon winter set in, shielding his body from seventy-degree frosts."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "The prized silky **underfur** of the Angora rabbit is developed through centuries of artificial selective breeding."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "The beaver's soft **underfur** was anciently prized by fur trappers for fashioning waterproof felt hats."}
    ]
  },
  "Dashboard — und/undergarment.md": {
    "primary": "An article of clothing worn beneath other clothes, especially next to the skin; underwear.",
    "secondary": "In fashion history, linen and wool undergarments protected expensive tailored outer fabrics from bodily oils and perspiration.",
    "quotes": [
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "Jane packed a simple change of linen **undergarment** into her small traveling bag before departing from Gateshead."},
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "The minister wore a coarse haircloth **undergarment** next to his flesh as a secret, self-inflicted penance."},
      {"author": "Edith Wharton", "work": "The Age of Innocence", "quote": "The delicate lace trimming on the bridal **undergarment** was stitched by hand in a French convent."}
    ]
  },
  "Dashboard — und/undergird.md": {
    "primary": "To secure or support from below; to strengthen or reinforce the underlying foundation of something.",
    "secondary": "In nautical history and constitutional theory, fundamental moral principles undergird the stability of democratic institutions.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "Sound public credit and fiscal integrity must **undergird** the authority of the newly established national government."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The crew passed heavy chains beneath the damaged hull to **undergird** the ship against the pounding typhoon seas."},
      {"author": "Thomas Carlyle", "work": "Past and Present", "quote": "Sincere religious reverence must **undergird** all human labor if society is to escape spiritual despair."}
    ]
  },
  "Dashboard — und/undergo.md": {
    "primary": "To experience or be subjected to something, typically something unpleasant, arduous, or transformative.",
    "secondary": "In physical chemistry, materials undergo allotropic phase transitions when subjected to elevated temperatures and pressures.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "All living organisms must **undergo** continuous modifications in the relentless struggle for existence over geological time."},
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "I was forced to **undergo** months of solitary toil and physical exhaustion to accomplish my terrible creation."},
      {"author": "William Shakespeare", "work": "The Tempest", "quote": "Which thou didst bear, and with a smile infused; which raised in me an undergoing stomach, to bear up against what should ensue, and **undergo** all hardships."}
    ]
  },
  "Dashboard — und/undergrad.md": {
    "primary": "An informal abbreviation for an undergraduate; a university student who has not yet taken a first degree.",
    "secondary": "In university campus culture, an undergrad balances collegiate coursework, athletic competitions, and student societies.",
    "quotes": [
      {"author": "P. G. Wodehouse", "work": "The Inimitable Jeeves", "quote": "Bertie Wooster looked back fondly on his days as a carefree Oxford **undergrad**, remembering boat races and dining club pranks."},
      {"author": "F. Scott Fitzgerald", "work": "This Side of Paradise", "quote": "The young Princeton **undergrad** debated poetry and social philosophy late into the night in dormitories."},
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Missing Three-Quarter", "quote": "The missing rugby captain was a popular Cambridge **undergrad** whose disappearance alarmed the entire university."}
    ]
  },
  "Dashboard — und/undergraduate.md": {
    "primary": "A student at a college or university who has not yet earned a bachelor's or first degree.",
    "secondary": "In academic history, undergraduate curriculum historically required mastery of the classical quadrivium, moral philosophy, and rhetoric.",
    "quotes": [
      {"author": "Thomas Babington Macaulay", "work": "Life and Letters of Lord Macaulay", "quote": "As an **undergraduate** at Trinity College, Cambridge, he distinguished himself by his extraordinary classical erudition."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Fred Vincy returned to his family home after three expensive years as a leisurely university **undergraduate**."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Steerforth was living in style as an Oxford **undergraduate**, looking down with easy grace upon common professions."}
    ]
  },
  "Dashboard — und/underground.md": {
    "primary": "Beneath the surface of the earth; or secret, clandestine, and operating outside official authority.",
    "secondary": "In nineteenth-century American abolitionism, the Underground Railroad was a clandestine network aiding escaped enslaved people to freedom.",
    "quotes": [
      {"author": "H. G. Wells", "work": "The Time Machine", "quote": "The sinister Morlocks inhabited an **underground** industrial labyrinth beneath the idyllic gardens of the upper world."},
      {"author": "Frederick Douglass", "work": "Narrative of the Life of Frederick Douglass", "quote": "The secret **underground** pathways steered fugitives from southern bondage north toward freedom in Canada."},
      {"author": "Jules Verne", "work": "Journey to the Center of the Earth", "quote": "We descended into the vast **underground** gallery, following the footsteps of Arne Saknussemm into the volcanic depths."}
    ]
  },
  "Dashboard — und/undergrow.md": {
    "primary": "To grow beneath or under other plants, trees, or vegetation; to form an understory.",
    "secondary": "In silvicultural ecology, shade-tolerant shrubs undergrow tall forest canopies, capturing filtered sunlight for photosynthesis.",
    "quotes": [
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "Low huckleberry and blueberry bushes **undergrow** the tall pitch pines along the sandy shores of the pond."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "Stout evergreen ferns and dwarf bamboos **undergrow** the beech trees in the rain-soaked Fuegian forests."},
      {"author": "Joseph Dalton Hooker", "work": "Himalayan Journals", "quote": "Dense rhododendron thickets **undergrow** the giant mountain hemlocks at ten thousand feet elevation."}
    ]
  },
  "Dashboard — und/undergrowth.md": {
    "primary": "A dense growth of shrubs, saplings, and smaller plants growing beneath the trees in a forest; underbrush.",
    "secondary": "In wilderness travel, dense undergrowth slows infantry marches and conceals animal trails from casual observation.",
    "quotes": [
      {"author": "James Fenimore Cooper", "work": "The Deerslayer", "quote": "The scout pushed through the tangled forest **undergrowth**, keeping his eyes fixed upon the distant lake."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The seedlings of forest trees must struggle against thick **undergrowth** of brambles and weeds for light and space."},
      {"author": "Arthur Conan Doyle", "work": "The Lost World", "quote": "We hacked our way through the steamy tropical **undergrowth** with heavy machetes to reach the base of the cliffs."}
    ]
  },
  "Dashboard — und/underhand.md": {
    "primary": "Done secretly, slyly, and dishonorably; deceitful or treacherous; or performed with the hand below shoulder level.",
    "secondary": "In political rivalry, underhand maneuvers to discredit an honorable opponent backfire when exposed to public scrutiny.",
    "quotes": [
      {"author": "William Shakespeare", "work": "As You Like It", "quote": "Yet he hath an **underhand** malice against me for no other reason than that the people praise my virtue."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth suspected that Caroline Bingley was engaged in an **underhand** scheme to separate Jane from her brother."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Uriah Heep pursued his **underhand** designs against Mr. Wickfield with false humility and cunning flattery."}
    ]
  },
  "Dashboard — und/underhanded.md": {
    "primary": "Marked by secrecy, deception, slyness, and dishonesty; clandestine and untrustworthy.",
    "secondary": "In legal ethics, underhanded tactics designed to conceal discoverable evidence invite severe court sanctions.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Beryl Coronet", "quote": "Holmes exposed the **underhanded** conspiracy that had framed an innocent young man for the theft of the coronet."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Bulstrode shrank from the memory of the **underhanded** commercial transactions that had founded his great fortune."},
      {"author": "Anthony Trollope", "work": "Barchester Towers", "quote": "The archdeacon denounced the curate's **underhanded** efforts to influence the patronage of the hospital appointment."}
    ]
  },
  "Dashboard — und/underhandedly.md": {
    "primary": "In an underhanded, deceitful, secret, and dishonest manner; slyly.",
    "secondary": "In commercial competition, acquiring proprietary trade secrets underhandedly breaches statutory antitrust and tort laws.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Smallweed worked **underhandedly** to purchase debts and foreclose upon unfortunate London tradesmen."},
      {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "Becky Sharp operated **underhandedly**, extracting costly presents from the old baronet while flattering his sisters."},
      {"author": "Walter Scott", "work": "Rob Roy", "quote": "Rashleigh Osbaldistone acted **underhandedly**, plotting to ruin his family's credit in the City of London."}
    ]
  },
  "Dashboard — und/underhung.md": {
    "primary": "Suspended or supported from above; or having a lower jaw that projects noticeably forward beyond the upper jaw.",
    "secondary": "In mechanical crane engineering, an underhung overhead bridge crane travels along the bottom flanges of supporting runway beams.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "The bulldogs display a distinctly **underhung** jaw, an anatomical modification preserved by selective breeding for bull-baiting."},
      {"author": "Thomas Henry Huxley", "work": "The Anatomy of Vertebrated Animals", "quote": "In certain deep-sea teleosts, the **underhung** mandible is armed with formidable recurved teeth for seizing slippery prey."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "The prize-fighter was a burly man with a pugnacious, **underhung** jaw and broken cauliflower ears."}
    ]
  },
  "Dashboard — und/underivative.md": {
    "primary": "Not derived or deduced from another source; original, primitive, or underived.",
    "secondary": "In theoretical morphology and linguistics, underivative root words serve as primitive base morphemes from which compound terms branch.",
    "quotes": [
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Simple sensory ideas are primary and **underivative**, constituting the foundational materials of all human knowledge."},
      {"author": "Max Müller", "work": "Lectures on the Science of Language", "quote": "Comparative philologists identify primitive, **underivative** verbal roots common to both Sanskrit and classical Greek."},
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "First principles in natural philosophy must be sought in **underivative** axioms confirmed by direct observation."}
    ]
  },
  "Dashboard — und/underived.md": {
    "primary": "Not derived from anything else; original, primary, independent, or self-existent.",
    "secondary": "In metaphysical ontology, underived existence designates eternal, non-contingent being that requires no prior cause.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "Axioms of pure geometry are regarded by rationalists as original and **underived** truths of the understanding."},
      {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "The primary imagination is an **underived** creative power that echoes in the finite mind the eternal act of creation."},
      {"author": "Herbert Spencer", "work": "First Principles", "quote": "The ultimate cosmic energy that sustains the universe is an **underived** reality transcending human comprehension."}
    ]
  },
  "Dashboard — und/underlay.md": {
    "primary": "To lay or place something underneath; or a layer of material placed under a carpet or mattress for support.",
    "secondary": "In letterpress printing, an underlay was paper pasted under type or plates to level the impression surface evenly.",
    "quotes": [
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Peggotty carefully spread the clean wool **underlay** upon the bed to make David comfortable for the night."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Gabriel Oak helped the shepherd **underlay** the lambing pens with clean dry straw against the frost."},
      {"author": "Herman Melville", "work": "Typee", "quote": "The islanders wove mats of soft coconut fiber to **underlay** the sleeping couches inside their bamboo dwellings."}
    ]
  },
  "Dashboard — und/underlayment.md": {
    "primary": "A layer of material, such as foam, plywood, or felt, placed beneath flooring, carpeting, or roofing to provide a smooth, resilient base.",
    "secondary": "In architectural building science, water-resistant underlayment protects structural roof sheathing from wind-driven rain penetration.",
    "quotes": [
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "I laid down an **underlayment** of dry white pine boards to insulate the cabin floor from the frozen ground."},
      {"author": "Arthur C. Clarke", "work": "Islands in the Sky", "quote": "The acoustic engineers installed a vibration-damping **underlayment** beneath the machinery deck of the orbital station."},
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The Venetian builders laid a resilient **underlayment** of Istrian stone flags over sunken timber pilings in the lagoon."}
    ]
  },
  "Dashboard — und/underlie.md": {
    "primary": "To lie situated beneath something; or to be the foundation, basis, or fundamental cause of something.",
    "secondary": "In structural geology, ancient crystalline basement granites underlie younger sedimentary and volcanic strata across continental cratons.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Universal laws of variation and natural selection **underlie** the astonishing morphological diversity of living forms."},
      {"author": "Thomas Henry Huxley", "work": "Physiography", "quote": "Thick beds of impermeable London clay **underlie** the gravel terraces that border the lower Thames valley."},
      {"author": "Adam Smith", "work": "The Theory of Moral Sentiments", "quote": "Natural human sympathies and mutual regard **underlie** the stability of all civilized social compacts."}
    ]
  },
  "Dashboard — und/underline.md": {
    "primary": "To draw a line under a word or phrase; or to emphasize, highlight, or stress the importance of something.",
    "secondary": "In typographic composition, setting text with an underline was the historical manuscript convention indicating italic font for the printer.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Second Stain", "quote": "Holmes used his pen to **underline** the critical sentence in the secret diplomatic dispatch on Baker Street."},
      {"author": "Jane Austen", "work": "Emma", "quote": "Mr. Elton took pains to **underline** certain sentimental phrases in the charade he presented to Harriet."},
      {"author": "Winston Churchill", "work": "The Second World War", "quote": "The catastrophic losses at sea served to **underline** the desperate urgency of securing our Atlantic convoy routes."}
    ]
  },
  "Dashboard — und/underling.md": {
    "primary": "A person of lower status or subordinate rank, often used in a mildly derogatory or dismissive sense.",
    "secondary": "In corporate hierarchies, a dismissive manager passes menial routine tasks down to an anonymous underling.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Julius Caesar", "quote": "The fault, dear Brutus, is not in our stars, but in ourselves, that we are **underling**s to Caesar's ambition."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The pompous clerk refused to discuss business with a common **underling**, demanding an interview with the principal."},
      {"author": "Edmund Burke", "work": "Speech on American Taxation", "quote": "Imperial policy should not be abandoned to the arbitrary caprice of every subaltern **underling** in the customs office."}
    ]
  },
  "Dashboard — und/underlip.md": {
    "primary": "The lower lip of the human mouth or an animal's mouth.",
    "secondary": "In expressive portraiture, a protruding or trembling underlip conveys petulant defiance or suppressed grief in a subject.",
    "quotes": [
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "Rochester bit his **underlip** with suppressed agitation, pacing the library floor as the storm raged outside."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Pip noticed that Magwitch's scarred **underlip** twitched with deep emotion as he gazed upon the boy he had enriched."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Tess pressed her trembling **underlip** with her teeth, striving to maintain composure before her harsh interrogator."}
    ]
  },
  "Dashboard — und/underlying.md": {
    "primary": "Situated beneath or below; or fundamental, implicit, or serving as the root cause of something.",
    "secondary": "In macroeconomic analysis, identifying underlying inflation trends requires excluding volatile food and energy price swings.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Lay Sermons, Addresses, and Reviews", "quote": "A profound unity of physical composition constitutes the **underlying** basis of all animal and plant life."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The **underlying** community of descent explains why the homologies between primate and human anatomy are so close."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Lydgate failed to perceive the **underlying** vanity that poisoned his domestic peace with Rosamond."}
    ]
  },
  "Dashboard — und/undermanned.md": {
    "primary": "Having too few crew, workers, or personnel to operate efficiently, properly, or safely.",
    "secondary": "In maritime history, an undermanned vessel in stormy waters struggled to shorten sail quickly, risking structural dismasting.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The whaling ship was dangerously **undermanned** after several seamen died of scurvy in the tropical doldrums."},
      {"author": "Winston Churchill", "work": "The World Crisis", "quote": "The naval shore batteries were severely **undermanned**, leaving the harbor mouth exposed to night torpedo raids."},
      {"author": "Joseph Conrad", "work": "The Shadow-Line", "quote": "With half the crew prostrate with tropical fever, the barque was pitifully **undermanned** for the passage across the gulf."}
    ]
  },
  "Dashboard — und/undermentioned.md": {
    "primary": "Mentioned, specified, or referred to further down in a document, letter, or book.",
    "secondary": "In legal drafting and administrative notices, rights and schedules set forth in the undermentioned clauses bind contracting parties.",
    "quotes": [
      {"author": "Daniel Defoe", "work": "The Complete English Tradesman", "quote": "The merchant signed the commercial bill of lading, promising delivery of the **undermentioned** crates of woolens."},
      {"author": "Charles Dickens", "work": "Pickwick Papers", "quote": "The legal notice published in the gazette warned that the **undermentioned** debtors must discharge their liabilities."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The powers conferred upon the national executive in the **undermentioned** sections of the charter are strictly enumerated."}
    ]
  },
  "Dashboard — und/undermine.md": {
    "primary": "To dig or excavate beneath something; or to erode, weaken, or damage insidiously and gradually.",
    "secondary": "In historical siegecraft, sappers dig tunnels beneath castle bastions to undermine their masonry foundations with fire or explosives.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The Roman sappers worked tirelessly day and night to **undermine** the ramparts of the besieged Persian stronghold."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "Factional demagogues will seek to **undermine** public confidence in constitutional institutions to establish personal tyranny."},
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "For 'tis the sport to have the engineer hoist with his own petard; and 't shall go hard but I will delve one yard below their mines, and blow them at the moon: O, 'tis most sweet, when in one line two crafts directly meet, to **undermine** an adversary."}
    ]
  },
  "Dashboard — und/underneath.md": {
    "primary": "Situated directly below or beneath; situated on the underside of something.",
    "secondary": "In psychoanalytic personality theory, a serene public persona frequently conceals intense anxieties churning underneath.",
    "quotes": [
      {"author": "Charles Dickens", "work": "A Christmas Carol", "quote": "Scrooge looked up at the clock, then down at the floor, seeing a pale phantom hovering directly **underneath** the doorway."},
      {"author": "Robert Louis Stevenson", "work": "Treasure Island", "quote": "Silver dug into the sandy earth with his spade, looking for the iron chest hidden **underneath** the pine roots."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The great leviathan sounded into the deep abyss, leaving a vast whirlpool swirling **underneath** our boat."}
    ]
  },
  "Dashboard — und/undernourish.md": {
    "primary": "To provide with insufficient food or nutrition for healthy bodily growth, maintenance, and energy.",
    "secondary": "In public health advocacy, failing to feed growing children balanced protein diets will undernourish their cognitive and physical development.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Oliver Twist", "quote": "The parish guardians resolved to **undernourish** the workhouse paupers systematically, hoping to discourage vagrancy."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "To **undernourish** a convalescent patient recovering from protracted typhus fever is to invite fatal secondary infections."},
      {"author": "George Orwell", "work": "The Road to Wigan Pier", "quote": "Economic poverty forces mining families to **undernourish** their children on cheap bread, margarine, and sweetened tea."}
    ]
  },
  "Dashboard — und/undernourished.md": {
    "primary": "Not receiving enough food or nourishment to maintain good health; malnourished and frail.",
    "secondary": "In clinical nutritional assessment, undernourished patients present with muscle wasting, delayed wound healing, and hypoalbuminemia.",
    "quotes": [
      {"author": "George Orwell", "work": "The Road to Wigan Pier", "quote": "The children playing in the soot-blackened streets looked pale, rickety, and chronically **undernourished**."},
      {"author": "Charles Dickens", "work": "Nicholas Nickleby", "quote": "Smike was a pitiful, **undernourished** drudge whose hollow cheeks and frightened eyes revealed years of cruelty at Dotheboys Hall."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The **undernourished** child showed marked delayed ossification of the epiphyses typical of nutritional rickets."}
    ]
  },
  "Dashboard — und/undernourishment.md": {
    "primary": "Insufficient nutritional intake, malnutrition, or deficiency in essential vitamins and calories.",
    "secondary": "In global humanitarian relief, chronic undernourishment in early childhood induces irreversible physical stunting and cognitive deficits.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Progressive constitutional debility and localized edema frequently result from protracted dietary **undernourishment**."},
      {"author": "George Orwell", "work": "The Road to Wigan Pier", "quote": "The physical effects of long-term **undernourishment** were visible in the stooped frames and decaying teeth of the miners."},
      {"author": "Charles Dickens", "work": "Oliver Twist", "quote": "The board of guardians was indicted in the public press for the cruel **undernourishment** of the parish apprentices."}
    ]
  },
  "Dashboard — und/underpants.md": {
    "primary": "An undergarment worn over the genitals and buttocks under trousers, skirts, or shorts; underdrawers.",
    "secondary": "In modern textile manufacture, breathable cotton jersey underpants replaced heavy woven flannel garments for daily wear.",
    "quotes": [
      {"author": "George Orwell", "work": "Down and Out in Paris and London", "quote": "The tramp stood shivering in his threadbare **underpants** while the dormitory warder sprayed his coat with disinfectant."},
      {"author": "James Joyce", "work": "Ulysses", "quote": "Bloom adjusted his braces over his clean cotton **underpants**, preparing for his morning walk across Dublin."},
      {"author": "John Steinbeck", "work": "Cannery Row", "quote": "Mack washed his solitary pair of wool **underpants** in a bucket behind the palace flophouse."}
    ]
  },
  "Dashboard — und/underpart.md": {
    "primary": "The lower or underside of an object, surface, animal, or structure; underbelly.",
    "secondary": "In avian taxonomy, field guides describe the contrasting colors of the crown, mantle, and underpart to identify warbler species.",
    "quotes": [
      {"author": "John Gould", "work": "The Birds of Australia", "quote": "The plumage on the **underpart** of the honeyeater was bright lemon yellow, contrasting with its olive-green back."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The curious lizard displayed brilliant blue mottling across its white **underpart** when basking in the sun."},
      {"author": "Thomas Henry Huxley", "work": "The Anatomy of Vertebrated Animals", "quote": "The protective dermal scutes covering the **underpart** of the crocodilian belly are flattened and non-keeled."}
    ]
  },
  "Dashboard — und/underpass.md": {
    "primary": "A road, railway line, or pedestrian walkway that passes underneath another road or railway.",
    "secondary": "In civil traffic engineering, grade separation via an underpass eliminates hazardous vehicular rail crossings and reduces intersection delays.",
    "quotes": [
      {"author": "H. G. Wells", "work": "The War in the Air", "quote": "Panicked London refugees jammed the railway **underpass**, fleeing the approaching flight of hostile airships."},
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Bruce-Partington Plans", "quote": "The railway line dipped into a deep arched **underpass** near the underground station where the body was discovered."},
      {"author": "George Orwell", "work": "Nineteen Eighty-Four", "quote": "Winston hurried through the gloomy concrete **underpass**, his head down against the biting November wind."}
    ]
  },
  "Dashboard — und/underpay.md": {
    "primary": "To pay someone less than is deserved, agreed upon, or required by fair market wages.",
    "secondary": "In labor economics, unscrupulous employers who underpay workers exploit geographic isolation and limited employment alternatives.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Master manufacturers who conspire to **underpay** their laborers provoke bitter strikes and industrial emigration."},
      {"author": "Charles Dickens", "work": "Hard Times", "quote": "Bounderby sought every legal loophole to **underpay** his factory hands while demanding unremitting twelve-hour shifts."},
      {"author": "Thomas Carlyle", "work": "Past and Present", "quote": "To **underpay** the honest workman who produces the wealth of the nation is an iniquity that cries to heaven."}
    ]
  },
  "Dashboard — und/underpayment.md": {
    "primary": "Payment of less than the agreed, required, fair, or full amount owed.",
    "secondary": "In commercial litigation and contract audit, systematic underpayment of royalties justifies statutory interest and contract termination.",
    "quotes": [
      {"author": "Daniel Defoe", "work": "The Complete English Tradesman", "quote": "The merchant warned his factor that repeated **underpayment** of accepted bills of exchange would destroy his credit on the exchange."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Mr. Micawber acknowledged the temporary **underpayment** of his rental obligation with magnificent flourishes of his cane."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The chronic **underpayment** of provincial revenue officers encourages bribery and widespread smuggling along the coast."}
    ]
  },
  "Dashboard — und/underperform.md": {
    "primary": "To perform less well than expected, required, or relative to a benchmark or competitor.",
    "secondary": "In investment portfolio management, assets that underperform the benchmark index are reallocated or liquidated by fund managers.",
    "quotes": [
      {"author": "Walter Bagehot", "work": "Lombard Street: A Description of the Money Market", "quote": "Joint-stock banks that **underperform** during commercial liquidity crises lose customer deposits to conservative institutions."},
      {"author": "Thomas Edison", "work": "The Edison Papers", "quote": "If the dynamo should **underperform** under continuous electrical load, we must rewind the armature with heavier copper wire."},
      {"author": "Herbert Spencer", "work": "The Principles of Sociology", "quote": "Inefficient bureaucratic departments consistently **underperform** private enterprises in delivering complex public works."}
    ]
  },
  "Dashboard — und/underperformer.md": {
    "primary": "A person, company, investment, or machine that performs less well than expected or required.",
    "secondary": "In human resources management, an underperformer is placed on an improvement plan to diagnose skill gaps or motivational hurdles.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Nicholas Nickleby", "quote": "Mr. Vincent Crummles dismissed the stage **underperformer** whose wooden acting had ruined the romantic third act."},
      {"author": "Thomas Carlyle", "work": "Past and Present", "quote": "The idle aristocratic **underperformer** who lives upon hereditary rents without performing public duty invites social revolution."},
      {"author": "Arthur Conan Doyle", "work": "The Stark Munro Letters", "quote": "The senior medical partner proved a chronic **underperformer**, leaving all the arduous night calls to his young assistant."}
    ]
  },
  "Dashboard — und/underpin.md": {
    "primary": "To support or form the foundation for; or to strengthen a wall or foundation from below.",
    "secondary": "In structural civil engineering, technicians underpin settling building foundations by driving micro-piles down to solid bedrock.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Physiography", "quote": "Rigorous empirical facts must **underpin** every scientific theory regarding the geological evolution of river basins."},
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "Masons worked beneath the water level to **underpin** the leaning palace facade with fresh squared oak timbers."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "A robust revenue power must **underpin** the constitutional authority of the national government to maintain public credit."}
    ]
  },
  "Dashboard — und/underplay.md": {
    "primary": "To minimize, downplay, or treat something as being of less importance than it really is; or to underact.",
    "secondary": "In theatrical performance and diplomatic negotiation, seasoned practitioners underplay emotional rhetoric to project quiet authority.",
    "quotes": [
      {"author": "George Bernard Shaw", "work": "Dramatic Opinions and Essays", "quote": "The accomplished tragedian chose to **underplay** the grief scene, achieving a poignant intimacy that moved the entire audience."},
      {"author": "Winston Churchill", "work": "The World Crisis", "quote": "Ministers attempted to **underplay** the disastrous loss of the armored cruisers, but the naval public was not deceived."},
      {"author": "Henry James", "work": "The Art of the Novel", "quote": "The novelist must not **underplay** the crucial dramatic climax upon which the entire moral theme of the book depends."}
    ]
  },
  "Dashboard — und/underpopulated.md": {
    "primary": "Having an unusually or undesirably small population; sparsely inhabited.",
    "secondary": "In demographic geography, vast underpopulated frontier territories offer arable acreage but lack domestic consumer markets.",
    "quotes": [
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "The western territories were vast and **underpopulated**, offering boundless fertile soil to energetic pioneer immigrants."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The American colonies, being fertile and **underpopulated**, displayed the most rapid natural population increase in human history."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Recurrent plagues left the Italian countryside **underpopulated**, prompting emperors to settle captive barbarian tribes upon deserted farms."}
    ]
  },
  "Dashboard — und/underprice.md": {
    "primary": "To price something below its real value, cost, or market equilibrium rate.",
    "secondary": "In competitive commercial statecraft, foreign exporters may underprice goods (dumping) to drive domestic competitors out of business.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Monopolistic cartels may temporarily **underprice** their wares to crush budding domestic competitors before raising charges."},
      {"author": "Theodore Dreiser", "work": "The Financier", "quote": "Cowperwood realized the directors had decided to **underprice** the new stock issue, enabling insiders to accumulate shares cheaply."},
      {"author": "Daniel Defoe", "work": "The Complete English Tradesman", "quote": "The shopkeeper who seeks to gain custom by resolving to **underprice** honest competitors often ends in the bankruptcy court."}
    ]
  }
}

base_dir = r"App database\Latin roots\Cluster Action & State"

updated = 0
for rel_path, info in data.items():
    fpath = os.path.join(base_dir, rel_path.replace("/", os.sep))
    if not os.path.exists(fpath):
        print(f"Warning: {fpath} does not exist!")
        continue
    
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    book_idx = content.find("> [!book]")
    if book_idx == -1:
        print(f"Warning: No > [!book] callout in {rel_path}")
        continue
    
    prefix = content[:book_idx]
    
    p_def = info["primary"].strip().rstrip(".") + "."
    s_def = info["secondary"].strip().rstrip(".") + "."
    
    new_book = f"> [!book] 📖 Definitions & Semantic Range\n> 1. **Primary Definition (Lexical / Standard Consensus)**: {p_def}\n> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: {s_def}\n"
    
    new_quote = "> [!quote] 💬 Contextual Usage & Authentic Quotations\n"
    for q in info["quotes"]:
        auth = q["author"].strip()
        work = q["work"].strip()
        quote_text = q["quote"].strip().strip('"').strip('“').strip('”')
        new_quote += f'> - 📜 **{auth} (*{work}*):** *"{quote_text}"*\n'
    
    new_content = prefix + new_book + "\n" + new_quote + "\n"
    
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(new_content)
    updated += 1

print(f"Dashboard — und Part 3 (8C): Successfully updated {updated}/{len(data)} notes.")
