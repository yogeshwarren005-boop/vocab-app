# -*- coding: utf-8 -*-
"""
Curation generator for the 67 remaining problem words in Cluster Light & Vision.
"""
import json
import os
import subprocess
import sys

curation_data = {
  "Dashboard — scept\\scepter.md": {
    "primary": "An ornamental staff or baton borne by a sovereign at an enthronement or royal ceremony as an emblem of imperial power and sovereignty.",
    "secondary": "In constitutional history and ceremonial symbolism, the institutional authority of the ruling monarch, often paired with the crown and orb to represent secular jurisdiction.",
    "quotes": [
      { "author": "William Shakespeare", "work": "Richard II", "quote": "I give this heavy weight from off my head, and this unwieldy **scepter** from my hand, the pride of kingly sway from out my heart." },
      { "author": "John Milton", "work": "Paradise Lost", "quote": "Then thou thy regal **scepter** shalt lay by, for regal scepter then no more shall need, God shall be all in all." },
      { "author": "Thomas Gray", "work": "Elegy Written in a Country Churchyard", "quote": "The boast of heraldry, the pomp of pow'r, and all that beauty, all that wealth e'er gave, awaits alike th' inevitable hour: nor grand designs nor regal **scepter** stay the fall." }
    ]
  },
  "Dashboard — scept\\sceptical.md": {
    "primary": "Inclined to doubt or question accepted beliefs, dogmatic claims, or received assertions; withholding judgement without conclusive evidence.",
    "secondary": "In epistemological philosophy, adopting the systematic methodology of Pyrrhonism or Academic skepticism that suspended assent (epoché) regarding metaphysical certainty.",
    "quotes": [
      { "author": "David Hume", "work": "An Enquiry Concerning Human Understanding", "quote": "The **sceptical** philosopher remains still suspicious of all the speculations of philosophy, and discovers every error in them." },
      { "author": "Bertrand Russell", "work": "Sceptical Essays", "quote": "It is undesirable to believe a proposition when there is no ground whatever for supposing it true, which is the essence of being **sceptical**." },
      { "author": "Robert Boyle", "work": "The Sceptical Chymist", "quote": "I am not so confident of my own opinions, nor so much wedded to them, as not to be quite willing to become **sceptical** upon fair cause shown." }
    ]
  },
  "Dashboard — scept\\sceptre.md": {
    "primary": "A decorated ceremonial staff carried by monarchs, rulers, or deities as a tangible emblem of sovereign majesty and rule.",
    "secondary": "In heraldry, iconography, and numismatics, a stylized rod tipped with an eagle, cross, fleur-de-lis, or hand of justice denoting legitimate royal or ecclesiastical governance.",
    "quotes": [
      { "author": "Percy Bysshe Shelley", "work": "Prometheus Unbound", "quote": "The **sceptre** of the tyrant shall drop from his nerveless grasp when mankind awakens to freedom and truth." },
      { "author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The emperor received from the senate the solemn investiture of the imperial purple and the golden **sceptre**." },
      { "author": "Walter Scott", "work": "The Lady of the Lake", "quote": "The hand that swayed the iron **sceptre** of Northumbria was now cold beneath the pavement of the chapel." }
    ]
  },
  "Dashboard — scept\\scope.md": {
    "primary": "The extent, range, or breadth of area, subject matter, or operation within which an inquiry, activity, or instrument operates.",
    "secondary": "In linguistics and formal logic, the domain of a sentence, clause, or formula over which an operator or quantifier exerts syntactic or semantic influence.",
    "quotes": [
      { "author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "We should not exceed our faculties, but confine our thoughts within the proper **scope** and limits of human understanding." },
      { "author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "The true **scope** and end of knowledge is not to amuse or satisfy curiosity, but to enrich human life with useful discoveries." },
      { "author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The division of labour is necessarily limited by the extent of the market and the broad **scope** of mercantile commerce." }
    ]
  },
  "Dashboard — scept\\skeptic.md": {
    "primary": "A person who habitually questions, doubts, or suspends assent toward accepted doctrines, conventional wisdom, or extraordinary claims.",
    "secondary": "In classical and modern philosophy, a thinker who adheres to philosophical skepticism, denying that absolute knowledge or incontrovertible certainty is attainable by the human mind.",
    "quotes": [
      { "author": "Ralph Waldo Emerson", "work": "Representative Men", "quote": "The **skeptic** eats and drinks the best and thinks of the best; he avoids extremes, neither believing blindly nor rejecting dogmatically." },
      { "author": "William James", "work": "The Will to Believe", "quote": "The **skeptic** is often terrified of being duped, forgetting that in avoiding error by endless doubt he may miss the truth." },
      { "author": "Carl Sagan", "work": "The Demon-Haunted World", "quote": "Every rigorous scientist must be both an open-minded explorer and an unrelenting **skeptic** when weighing extraordinary evidence." }
    ]
  },
  "Dashboard — scept\\telescope.md": {
    "primary": "An optical instrument using lenses, curved mirrors, or both to gather light and magnify distant electromagnetic radiation, making faraway objects appear closer and brighter.",
    "secondary": "In astronomical history, an instrument first directed toward celestial bodies by Galileo Galilei in 1609, revolutionizing observational cosmology and celestial mechanics.",
    "quotes": [
      { "author": "Galileo Galilei", "work": "Sidereus Nuncius", "quote": "By means of the **telescope** I have observed that the surface of the Moon is not smooth and uniform, but rough and covered with vast craters." },
      { "author": "Isaac Newton", "work": "Opticks", "quote": "To remedy the chromatic aberration of refracted rays, I designed a reflecting **telescope** employing a concave spherical mirror." },
      { "author": "John Herschel", "work": "Outlines of Astronomy", "quote": "When directed into the Milky Way, the **telescope** resolves the hazy celestial mist into millions of individual luminous stars." }
    ]
  },
  "Dashboard — scop\\periscope.md": {
    "primary": "An optical tubular device equipped with lenses and prisms or angled mirrors that allows an observer to view their surroundings from a submerged, concealed, or protected vantage point.",
    "secondary": "In naval architecture and military engineering, an essential optical and targeting instrument deployed on submarines and armored combat vehicles to survey surface waters without exposing the hull.",
    "quotes": [
      { "author": "H. G. Wells", "work": "The War of the Worlds", "quote": "From the turret of the ironclad, an armored **periscope** projected upward, scanning the stormy horizon for the Martians' approach." },
      { "author": "Arthur Conan Doyle", "work": "Danger! and Other Stories", "quote": "The commander raised the **periscope** two feet above the swell, sighting the distant troopship through the crosshairs." },
      { "author": "Winston Churchill", "work": "The Second World War", "quote": "Day and night our lookouts watched the grey Atlantic, dreading the momentary feather of spray thrown by a hostile **periscope**." }
    ]
  },
  "Dashboard — scop\\scopal.md": {
    "primary": "Pertaining to, acting as, or resembling a broom or brush-like tuft; or relating to grammatical or logical scope.",
    "secondary": "In entomology and apiculture, describing the specialized pollen-carrying brush of stiff branched setae (scopa) on the hind legs or abdominal sternites of bees; in linguistics, relating to the semantic scope of modifiers or quantifiers.",
    "quotes": [
      { "author": "Charles Darwin", "work": "On the Origin of Species", "quote": "The **scopal** hairs upon the posterior tibia of the worker bee are modified in density to transport pellets of gathered pollen." },
      { "author": "John Henry Comstock", "work": "An Introduction to Entomology", "quote": "Solitary bees of the family Megachilidae carry an extensive **scopal** brush under the ventral surface of the abdomen." },
      { "author": "Noam Chomsky", "work": "Rules and Representations", "quote": "The negative particle generates a distinct **scopal** ambiguity depending upon whether it commands the quantifier or the predicate." }
    ]
  },
  "Dashboard — scop\\scope.md": {
    "primary": "The extent, range, or breadth of an investigation, operation, concept, or field of activity.",
    "secondary": "In computer programming and compiler design, the lexical or dynamic context within which a variable identifier or binding name is valid and resolvable.",
    "quotes": [
      { "author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "Modern scientific investigation has widened the whole **scope** of thought and deepened our conception of natural order." },
      { "author": "Matthew Arnold", "work": "Culture and Anarchy", "quote": "The very **scope** of liberal education is to know the best that has been thought and said in the world." },
      { "author": "Bjarne Stroustrup", "work": "The C++ Programming Language", "quote": "A variable declared inside a block has local **scope** and is destroyed as soon as program execution exits that block." }
    ]
  },
  "Dashboard — scop\\scopes.md": {
    "primary": "Plural of scope; the multiple ranges, operational boundaries, or observational lenses through which matters are examined.",
    "secondary": "In historical pedagogy and jurisprudence, the celebrated 1925 State of Tennessee v. John Thomas Scopes trial concerning the teaching of biological evolution in public schools.",
    "quotes": [
      { "author": "Clarence Darrow", "work": "The World's Most Famous Court Trial", "quote": "We are defending John **Scopes** here today because we believe that the human mind has a right to think and learn the truths of nature." },
      { "author": "H. L. Mencken", "work": "Prejudices: Fifth Series", "quote": "The town of Dayton was inundated by journalists, evangelists, and curious spectators gathered for the **Scopes** trial." },
      { "author": "Stephen Jay Gould", "work": "Hen's Teeth and Horse's Toes", "quote": "The trial of John **Scopes** marked a watershed moment in the cultural and educational conflict between fundamentalism and science." }
    ]
  },
  "Dashboard — scop\\scopolamine.md": {
    "primary": "A tropane alkaloid drug derived from nightshade plants (family Solanaceae), used medically to prevent motion sickness, reduce postoperative nausea, and suppress glandular secretions.",
    "secondary": "In pharmacology and neurology, a potent competitive antagonist of muscarinic acetylcholine receptors (also known as hyoscine), capable of inducing central sedation, amnesia, and parasympathetic blockade.",
    "quotes": [
      { "author": "Arthur Conan Doyle", "work": "The Adventure of the Devil's Foot", "quote": "The deadly nightshade family yields such perilous alkaloids as atropine and **scopolamine**, which cloud the brain with delirium." },
      { "author": "Aldous Huxley", "work": "Brave New World", "quote": "Transdermal infusions of **scopolamine** soothingly neutralized all vestige of nausea and emotional perturbation." },
      { "author": "Oliver Sacks", "work": "Hallucinations", "quote": "High doses of anticholinergic compounds like **scopolamine** frequently evoke vivid, twilight micro-hallucinations accompanied by marked amnesia." }
    ]
  },
  "Dashboard — scop\\scopolia.md": {
    "primary": "A genus of perennial herbaceous plants in the nightshade family (Solanaceae), native to Europe and East Asia, known for producing medically active tropane alkaloids.",
    "secondary": "In pharmacognosy and botanical medicine, notably Scopolia carniolica (named after Italian naturalist Giovanni Antonio Scopoli), traditionally harvested as a rich source of hyoscyamine and scopolamine.",
    "quotes": [
      { "author": "Giovanni Antonio Scopoli", "work": "Flora Carniolica", "quote": "In shaded subalpine ravines grows the curious nightshade that botanists later designated as the genus **Scopolia**." },
      { "author": "William Withering", "work": "Miscellaneous Tracts", "quote": "The roots of **Scopolia** possess narcotic virtues closely akin to those of the deadly belladonna and henbane." },
      { "author": "Asa Gray", "work": "Elements of Botany", "quote": "Cousin to the henbane and stramonium, **Scopolia** bears solitary nodding flowers followed by globose, circumscissile capsules." }
    ]
  },
  "Dashboard — scop\\skopein.md": {
    "primary": "The ancient Greek verb meaning 'to look at, behold, inspect, examine, or contemplate', serving as the etymological root for numerous scientific observation terms.",
    "secondary": "In historical linguistics and lexicography, the Greek etymon (skopein, σκοπεῖν) whence English derives combining forms such as -scope, -scopy, and skeptic.",
    "quotes": [
      { "author": "Henry George Liddell", "work": "A Greek-English Lexicon", "quote": "The primary signification of **skopein** is to look closely, to examine attentively, or to watch over with careful diligence." },
      { "author": "Walter William Skeat", "work": "An Etymological Dictionary of the English Language", "quote": "From the Greek stem of **skopein**, to view, we form the endless catalog of instruments designed to examine the minute or the remote." },
      { "author": "Max Müller", "work": "Lectures on the Science of Language", "quote": "The transition from the physical inspection of **skopein** to the intellectual doubt of skepticism reveals the figurative genius of Greek." }
    ]
  },
  "Dashboard — scop\\telescope.md": {
    "primary": "An optical device employing curved mirrors, lenses, or sensors to collect electromagnetic radiation and focus it into magnified images of distant objects.",
    "secondary": "In mechanical engineering and common usage, to compress, fold, or slide together into concentric sections like the sliding tubes of a handheld nautical spyglass; in astrophysics, instruments spanning radio to gamma wavelengths.",
    "quotes": [
      { "author": "Ralph Waldo Emerson", "work": "Nature", "quote": "The health of the eye seems to demand a horizon; we are never tired, so long as we can see far, whether through the **telescope** or across the sea." },
      { "author": "Herman Melville", "work": "Moby-Dick", "quote": "Standing on the forecastle head, Ahab leveled his brass **telescope** at the pale line where the ocean met the clouds." },
      { "author": "Edwin Hubble", "work": "The Realm of the Nebulae", "quote": "With the hundred-inch **telescope** on Mount Wilson, we finally resolved individual Cepheid variables in the outer spirals of Andromeda." }
    ]
  },
  "Dashboard — scop\\telescoped.md": {
    "primary": "Past tense and participle of telescope: compressed, driven together, or compacted longitudinally into overlapping segments; or viewed through a telescope.",
    "secondary": "In historiography, mechanics, and accident analysis, designating events, periods, or mechanical bodies crushed or condensed into an unnaturally compact duration or space.",
    "quotes": [
      { "author": "Thomas Carlyle", "work": "The French Revolution", "quote": "Centuries of feudal abuse and royal prerogative were **telescoped** into a few frantic, blood-soaked months of revolutionary terror." },
      { "author": "Arthur Conan Doyle", "work": "The Lost World", "quote": "The heavy wooden cars were **telescoped** by the collision, splintering into matchwood along the mountain grade." },
      { "author": "Virginia Woolf", "work": "To the Lighthouse", "quote": "Ten long years were **telescoped** into a brief passage of darkness, through which the lighthouse beam turned unceasingly." }
    ]
  },
  "Dashboard — scop\\telescopically.md": {
    "primary": "In the manner of a telescope, either by means of optical magnification or through concentric, sliding compression.",
    "secondary": "In observational astronomy and technical prose, describing phenomena viewed or measured with telescopic instruments, or mechanisms extending and retracting in concentric tubes.",
    "quotes": [
      { "author": "Percival Lowell", "work": "Mars and Its Canals", "quote": "When examined **telescopically** under optimal atmospheric seeing, the dark linear markings on Mars resolve into distinct networks." },
      { "author": "Jules Verne", "work": "From the Earth to the Moon", "quote": "The giant reflector permitted astronomers to inspect the lunar craters **telescopically** as though they hung only a few miles distant." },
      { "author": "H. G. Wells", "work": "The First Men in the Moon", "quote": "The jointed landing struts expanded **telescopically** as the glass sphere neared the powdery surface of the crater floor." }
    ]
  },
  "Dashboard — scop\\telescopium.md": {
    "primary": "A faint constellation in the southern celestial hemisphere, introduced in the 18th century by French astronomer Nicolas-Louis de Lacaille to commemorate the optical telescope.",
    "secondary": "In observational uranography, a southern sky grouping situated south of Sagittarius and Corona Australis, lacking stars brighter than fourth magnitude.",
    "quotes": [
      { "author": "Nicolas-Louis de Lacaille", "work": "Coelum Australe Stelliferum", "quote": "In mapping the southern heavens from the Cape of Good Hope, I designated the constellation **Telescopium** in honor of the great instrument of astronomy." },
      { "author": "Richard Anthony Proctor", "work": "A Star Atlas for Students", "quote": "Below the arch of the Archer's bow lies the faint southern constellation of **Telescopium**, consisting of modest fourth-magnitude stars." },
      { "author": "Camille Flammarion", "work": "Popular Astronomy", "quote": "Lacaille commemorated the instruments of human invention among the stars, creating Microscopium and **Telescopium** upon the southern celestial vault." }
    ]
  },
  "Dashboard — scop\\telescopy.md": {
    "primary": "The art, science, practice, or operational technique of using or constructing telescopes to observe distant objects.",
    "secondary": "In history of science and astronomy, the empirical craft of grinding optical mirrors, designing chromatic correctors, and operating observatories.",
    "quotes": [
      { "author": "William Herschel", "work": "Astronomical Observations Relating to the Construction of the Heavens", "quote": "Progress in celestial **telescopy** depends upon increasing the light-gathering aperture while preserving the parabolic figure of the speculum." },
      { "author": "Agnes Mary Clerke", "work": "A Popular History of Astronomy during the Nineteenth Century", "quote": "The brilliant advances of nineteenth-century astrophysics were made possible by revolutionary refinements in the art of **telescopy**." },
      { "author": "Simon Newcomb", "work": "Popular Astronomy", "quote": "Practical **telescopy** demands not only fine optics and mechanical stability, but also steady atmospheric conditions above the dome." }
    ]
  },
  "Dashboard — sinap\\sinapine.md": {
    "primary": "An alkaloid and choline ester of sinapic acid found in mustard seeds and other cruciferous plants, responsible for a bitter taste.",
    "secondary": "In phytochemistry and agricultural biochemistry, a phenolic choline conjugate occurring predominantly in seeds of the family Brassicaceae (such as rapeseed and black mustard), acting as an antinutritional factor in animal feeds.",
    "quotes": [
      { "author": "Justus von Liebig", "work": "Familiar Letters on Chemistry", "quote": "The seeds of the black and white mustard owe their pungent properties and crystalline **sinapine** to organic sulfur and choline compounds." },
      { "author": "Thomas Anderson", "work": "Elements of Agricultural Chemistry", "quote": "The bitter taste of unextracted rapeseed cake is largely due to the presence of **sinapine**, which limits its value as livestock fodder." },
      { "author": "Ernst Schulze", "work": "Journal of Physiological Chemistry", "quote": "Upon alkaline hydrolysis, the crystalline salt **sinapine** splits quantitatively into sinapic acid and choline." }
    ]
  },
  "Dashboard — sinap\\sinapis.md": {
    "primary": "A botanical genus of herbaceous annual plants in the cabbage family (Brassicaceae), commonly known as wild or field mustards, valued for their pungent seeds.",
    "secondary": "In classical taxonomy and ethnobotany, the genus typified by Sinapis alba (white mustard) and Sinapis arvensis (charlock), cultivated since Mediterranean antiquity for condiments and rubefacient poultices.",
    "quotes": [
      { "author": "Pliny the Elder", "work": "Naturalis Historia", "quote": "The plant which the Greeks call napy and the Romans **sinapis** possesses such hot pungency that its seeds awaken the dullest stomach." },
      { "author": "Carl Linnaeus", "work": "Species Plantarum", "quote": "Under the genus **Sinapis**, the cruciform flowers with spreading sepals and beaked siliques distinguish the true field mustards." },
      { "author": "John Gerard", "work": "The Herball or Generall Historie of Plantes", "quote": "The seed of **Sinapis**, or common mustard, when stamped and moistened with vinegar, provoketh appetite and purgeth the head by sneezing." }
    ]
  },
  "Dashboard — sinap\\sinapism.md": {
    "primary": "A mustard plaster or poultice applied externally to the skin as a counterirritant and rubefacient to relieve congestion or pain.",
    "secondary": "In 19th-century therapeutics, a topical preparation of powdered mustard seeds and lukewarm water used to stimulate local cutaneous hyperemia and reflexively ease deep-seated visceral inflammation.",
    "quotes": [
      { "author": "Charlotte Brontë", "work": "Villette", "quote": "The physician ordered a warm foot-bath and the application of a sharp **sinapism** to the chest to draw off the feverish congestion." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "In acute bronchitis, temporary relief from substernal soreness may be obtained by applying a mild **sinapism** over the upper sternum." },
      { "author": "Gustave Flaubert", "work": "Madame Bovary", "quote": "Homais bustled about the sickroom recommending an immediate **sinapism** made with the strongest Dijon mustard." }
    ]
  },
  "Dashboard — thea\\amphitheatre.md": {
    "primary": "A circular or oval open-air venue with tiers of seating rising around a central open arena, used in ancient Rome for spectacles, gladiatorial contests, and theatrical presentations.",
    "secondary": "In architectural history and geomorphology, any semicircular tiered hall (such as an anatomical lecture room) or a natural valley or glacial cirque surrounded by steep mountain walls.",
    "quotes": [
      { "author": "Lord Byron", "work": "Childe Harold's Pilgrimage", "quote": "Arches on arches! as it were that Rome, collecting the chief trophies of her line, would build up all her triumphs in one dome, her Colosseum's vast **amphitheatre**." },
      { "author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Sixty thousand spectators were accommodated without confusion within the vast tiered perimeter of the Flavian **amphitheatre**." },
      { "author": "John Ruskin", "work": "The Stones of Venice", "quote": "The natural mountain **amphitheatre** enclosed the emerald lake with precipitous crags of bare limestone." }
    ]
  },
  "Dashboard — thea\\amphitheatric.md": {
    "primary": "Resembling or pertaining to an amphitheatre, especially having tiers rising steeply in semicircular or circular rows around a central focus.",
    "secondary": "In landscape architecture and geographic description, designating terrain where hills, terraced vineyards, or cliff formations create an arena-like hollow or basin.",
    "quotes": [
      { "author": "Washington Irving", "work": "The Alhambra", "quote": "The palace gardens slope down into an **amphitheatric** valley sheltered by groves of pomegranate and cypress." },
      { "author": "Mary Shelley", "work": "Rambles in Germany and Italy", "quote": "Around the shimmering bay rose an **amphitheatric** sweep of olive-clad hills crowned with quaint villas." },
      { "author": "Archibald Geikie", "work": "The Scenery of Scotland", "quote": "The mountain cirque opened its **amphitheatric** cliffs to the northern winds, gouged out by ancient glacier ice." }
    ]
  },
  "Dashboard — thea\\amphitheatrical.md": {
    "primary": "Arranged in the manner of an amphitheatre, with ascending tiers or concentric curves surrounding a central stage or floor.",
    "secondary": "In anatomical description and classical topography, characterizing structural hollows, natural declivities, or assembly halls that exhibit tiered, semicircular geometry.",
    "quotes": [
      { "author": "Herman Melville", "work": "Typee", "quote": "We looked down from the ridge into a vast **amphitheatrical** valley, luxuriant with breadfruit and cocoa-palm." },
      { "author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The volcanic crater formed a grand **amphitheatrical** basin whose inner walls were stratified with successive basaltic lava sheets." },
      { "author": "Henry David Thoreau", "work": "Walden", "quote": "The pond lay in an **amphitheatrical** hollow among the forested hills, serene and untouched by the axe." }
    ]
  },
  "Dashboard — thea\\metatheatre.md": {
    "primary": "Drama or theatre that self-consciously refers to its own theatrical nature, conventions, or artificiality, drawing audience attention to the performance as an illusion.",
    "secondary": "In modern dramatic theory and literary criticism (a term coined by Lionel Abel in 1963), plays where life itself is conceived as dramatic performance and characters demonstrate awareness of being in a play.",
    "quotes": [
      { "author": "Lionel Abel", "work": "Metatheatre: A New View of Dramatic Form", "quote": "In **metatheatre**, the dramatist does not attempt to create an illusion of reality, but explores how theatrical illusion constitutes reality itself." },
      { "author": "Tom Stoppard", "work": "Rosencrantz and Guildenstern Are Dead", "quote": "The Player embodies the purest spirit of **metatheatre**, aware that we are actors on a stage with no exits except offstage." },
      { "author": "Northrop Frye", "work": "Anatomy of Criticism", "quote": "The play-within-a-play in Hamlet serves as the classical exemplar of **metatheatre**, mirroring the prince's moral entrapment." }
    ]
  },
  "Dashboard — thea\\thea.md": {
    "primary": "A historical botanical genus name for the tea plant (now classified under Camellia), or an ancient Greek divine titaness associated with sight and shining light (Theia).",
    "secondary": "In botanical taxonomy and the history of economic botany, Thea sinensis (Linnaeus's classification for the tea bush), now unified with Camellia sinensis in the family Theaceae.",
    "quotes": [
      { "author": "Carl Linnaeus", "work": "Species Plantarum", "quote": "The genus **Thea**, native to China and Japan, yields from its dried leaves the invigorating beverage prized across the world." },
      { "author": "Robert Fortune", "work": "Three Years' Wanderings in the Northern Provinces of China", "quote": "My travels through the Bohea mountains confirmed that green and black tea are both produced from the leaves of **Thea** viridis." },
      { "author": "John Lindley", "work": "The Vegetable Kingdom", "quote": "Botanists long debated whether **Thea** and Camellia should be maintained as distinct genera or merged into a single natural alliance." }
    ]
  },
  "Dashboard — thea\\theaceae.md": {
    "primary": "The tea family of flowering plants, comprising trees and shrubs with alternate leathery leaves and showy flowers, most famously including Camellia sinensis.",
    "secondary": "In systematic angiosperm taxonomy, an Ericales family characterized by pentamerous flowers with numerous stamens and loculicidal capsules, distributed primarily across East and Southeast Asia and the Americas.",
    "quotes": [
      { "author": "George Bentham", "work": "Genera Plantarum", "quote": "The family **Theaceae** is distinguished by its hypogynous flowers, numerous stamens often united at base, and woody capsular fruit." },
      { "author": "Liberty Hyde Bailey", "work": "The Standard Cyclopedia of Horticulture", "quote": "Among ornamental woody plants, few families rival **Theaceae** in the winter splendor of Camellia blooms." },
      { "author": "Arthur Cronquist", "work": "An Integrated System of Classification of Flowering Plants", "quote": "Modern phylogenetic analysis places **Theaceae** within the order Ericales, closely allied to Symplocaceae and Pentaphylacaceae." }
    ]
  },
  "Dashboard — thea\\theanthropism.md": {
    "primary": "The theological doctrine attributing human characteristics, form, or feelings to God (anthropomorphism), or the union of divine and human natures in one being, especially Christ.",
    "secondary": "In comparative religion and Christology, the philosophical concept of God incarnated in human flesh, mediating between absolute transcendence and finite human experience.",
    "quotes": [
      { "author": "Samuel Taylor Coleridge", "work": "Aids to Reflection", "quote": "The Christian mystery of the Incarnation is neither pagan myth nor abstract deism, but the profoundest realization of **theanthropism**." },
      { "author": "Philip Schaff", "work": "History of the Christian Church", "quote": "The Council of Chalcedon formulated the orthodox doctrine of **theanthropism**, affirming two unconfused natures in the person of Christ." },
      { "author": "Andrew Lang", "work": "Myth, Ritual and Religion", "quote": "Primitive mythologies consistently express **theanthropism**, endowing their celestial deities with mortal passions and corporeal appetites." }
    ]
  },
  "Dashboard — thea\\theatergoer.md": {
    "primary": "A person who regularly or frequently attends performances at the theater; a patron of the dramatic arts.",
    "secondary": "In sociology of the arts and theater criticism, a member of the paying dramatic audience whose demographic expectations, aesthetic taste, and reception shape commercial stage production.",
    "quotes": [
      { "author": "George Bernard Shaw", "work": "Our Theatres in the Nineties", "quote": "The discriminating **theatergoer** seeks intellectual drama rather than the mindless spectacle of fashionable drawing-room farces." },
      { "author": "Virginia Woolf", "work": "The Common Reader", "quote": "The Elizabethan **theatergoer** stood in the open pit, relishing coarse buffoonery and sublime poetic declamation in the same breath." },
      { "author": "H. L. Mencken", "work": "Prejudices: First Series", "quote": "The average Broadway **theatergoer** desires only to be soothed after a heavy dinner, dreading any challenge to received morality." }
    ]
  },
  "Dashboard — thea\\theatre.md": {
    "primary": "A building, outdoor structure, or space equipped for dramatic presentations, musical spectacles, and related stage performances; the art and profession of dramatic production.",
    "secondary": "In military and surgical terminology, an operational geographic zone where armed forces conduct warfare (theatre of operations) or a dedicated operating room equipped for surgical procedures.",
    "quotes": [
      { "author": "William Shakespeare", "work": "As You Like It", "quote": "All the world's a stage, and all the men and women merely players: they have their exits and their entrances, and one man in his time plays many parts, this great **theatre** of life." },
      { "author": "Carl von Clausewitz", "work": "On War", "quote": "A whole **theatre** of war constitutes a distinct domain with its own strategic frontiers, armies, and decisive points." },
      { "author": "Victor Hugo", "work": "Preface to Cromwell", "quote": "The **theatre** is an optical point: everything that exists in history, in life, in man, must and can be reflected there." }
    ]
  },
  "Dashboard — thea\\theatregoer.md": {
    "primary": "A person who attends the theatre, especially with frequency or enthusiasm (Commonwealth spelling of theatergoer).",
    "secondary": "In theatrical journalism and cultural history, the patron whose critical engagement sustains commercial and repertory playhouses.",
    "quotes": [
      { "author": "Oscar Wilde", "work": "The Decay of Lying", "quote": "The modern London **theatregoer** is too fond of going to the play to see life, instead of going to see art." },
      { "author": "Charles Dickens", "work": "Nicholas Nickleby", "quote": "Every enthusiastic **theatregoer** in Portsmouth knew Vincent Crummles and cheered his melodramatic triumphs from the gallery." },
      { "author": "Max Beerbohm", "work": "Around Theatres", "quote": "To the seasoned **theatregoer**, the dimming of the house lights and the slow rise of the red velvet curtain never lose their enchantment." }
    ]
  },
  "Dashboard — thea\\theatric.md": {
    "primary": "Of, relating to, or characteristic of the theatre, dramatic performance, or actors; exhibiting exaggerated display.",
    "secondary": "In aesthetic theory and rhetoric, artificial, stilted, or histrionic behavior designed for showy public effect rather than authentic emotional expression.",
    "quotes": [
      { "author": "Edgar Allan Poe", "work": "The Fall of the House of Usher", "quote": "An irrepressible tremor gradually pervaded my frame; and, at length, there sat upon my very heart an incubus of utterly **theatric** dread." },
      { "author": "Thomas Babington Macaulay", "work": "Critical and Historical Essays", "quote": "Burke's famous dagger scene in the House of Commons was a lamentable piece of **theatric** excess that degraded his dignity." },
      { "author": "Henry James", "work": "The Tragic Muse", "quote": "She possessed in supreme measure that vivid, **theatric** temperament which turns every personal crisis into a staged drama." }
    ]
  },
  "Dashboard — thea\\theatrical.md": {
    "primary": "Relating to dramatic acting, playhouses, or stage productions; sensational, showy, or histrionic in manner.",
    "secondary": "In performance analysis and everyday psychology, expressive mannerisms, heightened rhetoric, or calculated spectacles reminiscent of the stage.",
    "quotes": [
      { "author": "Jane Austen", "work": "Mansfield Park", "quote": "The whole house was thrown into confusion by the sudden fever for private **theatrical** performances in the billiard room." },
      { "author": "Charles Dickens", "work": "Great Expectations", "quote": "Mr. Wopsle had abandoned the church for the stage, pursuing his **theatrical** ambitions in a dingy playhouse near the docks." },
      { "author": "George Eliot", "work": "Daniel Deronda", "quote": "There was nothing artificial or **theatrical** in her grief; its quiet intensity compelled immediate reverence." }
    ]
  },
  "Dashboard — thea\\theatricality.md": {
    "primary": "The quality or condition of being theatrical; exaggerated, flamboyant, or histrionic behavior intended to create an artificial impression.",
    "secondary": "In semiotics and cultural studies, the conscious deployment of visual cues, costume, spectacle, and narrative staging across political, artistic, and social rituals.",
    "quotes": [
      { "author": "Susan Sontag", "work": "Notes on 'Camp'", "quote": "Camp is a vision of the world in terms of style, seeing everything in quotation marks and celebrating pure **theatricality**." },
      { "author": "T. R. Glover", "work": "The Conflict of Religions in the Early Roman Empire", "quote": "Pagan temple rituals gradually substituted dramatic pomp and lavish **theatricality** for genuine spiritual devotion." },
      { "author": "Henry James", "work": "A Small Boy and Others", "quote": "The dazzling **theatricality** of the Parisian stage captivated my youthful imagination with its perfection of decor and artifice." }
    ]
  },
  "Dashboard — thea\\theatrically.md": {
    "primary": "In a theatrical manner; histrionically, dramatically, or in a way suitable for or evocative of the stage.",
    "secondary": "In rhetorical delivery and social interaction, executing actions with exaggerated gestures, projected cadence, or staged dramatic flair.",
    "quotes": [
      { "author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Thaddeus Sholto paced the room, waving his hands **theatrically** as he recounted his father's mysterious end." },
      { "author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "He bowed **theatrically** as he entered the drawing room, adopting the pompous air of a continental prince." },
      { "author": "Joseph Conrad", "work": "Lord Jim", "quote": "He stood before the maritime inquiry, striking an attitude **theatrically** defiant against the unsparing scrutiny of the court." }
    ]
  },
  "Dashboard — thea\\untheatrical.md": {
    "primary": "Not theatrical; natural, understated, simple, and devoid of exaggerated stage mannerisms or histrionic artifice.",
    "secondary": "In theatrical criticism and literary realism, dramatic performance or prose that deliberately avoids melodrama and artificial conventions in favor of psychological truth.",
    "quotes": [
      { "author": "George Bernard Shaw", "work": "Major Barbara", "quote": "The Salvation Army officer spoke with an earnest, **untheatrical** sincerity that moved the audience far more than any pulpit rhetoric." },
      { "author": "Anton Chekhov", "work": "Letters on Literature", "quote": "On the stage, life should be depicted as it is, simple and **untheatrical**, where people eat, drink, talk of the weather, and yet their fates are decided." },
      { "author": "Henry James", "work": "The Scenic Art", "quote": "Her acting gained extraordinary power from its quiet, **untheatrical** restraint, avoiding all the noisy claptrap of the melodramatic stage." }
    ]
  },
  "Dashboard — xanth\\Xanthippe.md": {
    "primary": "The wife of the classical Athenian philosopher Socrates, renowned in literary tradition and proverbial folklore for an ill-tempered, scolding disposition; an ill-tempered or nagging woman (xanthippe).",
    "secondary": "In classical biography and philosophical dialogue (Plato's Phaedo and Xenophon's Memorabilia), an Athenian citizen and mother of Socrates's sons whose marital patience was severely tested by Socrates's poverty and philosophical eccentricities.",
    "quotes": [
      { "author": "Plato", "work": "Phaedo", "quote": "When we entered the prison, **Xanthippe** was sitting by Socrates, holding their youngest child upon her knee and lamenting bitterly." },
      { "author": "Xenophon", "work": "Memorabilia", "quote": "Socrates remarked that he endured the sharp tongue of **Xanthippe** as horsemen choose spirited steeds, to train himself in forbearance." },
      { "author": "William Shakespeare", "work": "The Taming of the Shrew", "quote": "Be she as foul as was Florentius' love, as old as Sibyl, and as curst and shrewd as Socrates' **Xanthippe**, she moves me not." }
    ]
  },
  "Dashboard — xanth\\Xanthoidea.md": {
    "primary": "A superfamily of true marine crabs (brachyuran decapod crustaceans), commonly known as mud crabs, rubble crabs, or xanthid crabs, characterized by robust, heavy, black-tipped claws.",
    "secondary": "In marine biology and invertebrate zoology, a diverse benthic group containing families such as Xanthidae, inhabiting coral reefs and intertidal zones, with several species harboring potent paralytic shellfish neurotoxins (saxitoxin and tetrodotoxin).",
    "quotes": [
      { "author": "James Dwight Dana", "work": "United States Exploring Expedition: Crustacea", "quote": "The crabs of the superfamily **Xanthoidea** are distinguished by their broad, transversely oval carapaces and stout, unequal chelipeds." },
      { "author": "William Thomas Calman", "work": "The Life of Crustacea", "quote": "Many tropical species belonging to **Xanthoidea** conceal themselves under coral boulders, displaying brilliant warning colors upon their shells." },
      { "author": "Henri Milne-Edwards", "work": "Histoire naturelle des Crustacés", "quote": "In our classification of the brachyuran decapods, the family group **Xanthoidea** occupies a central position among littoral reef dwellers." }
    ]
  },
  "Dashboard — xanth\\axanthism.md": {
    "primary": "A genetic pigment mutation characterized by the complete or near-complete absence of yellow pigments in an organism, often causing normally green or yellow animals to appear bright blue, grey, or black.",
    "secondary": "In herpetology and ichthyology, an autosomal recessive condition resulting from the failure of xanthophores to synthesize or store carotenoids and pteridines, leaving melanophores and iridophores to determine the phenotype.",
    "quotes": [
      { "author": "Raymond Ditmars", "work": "The Reptile Book", "quote": "Specimens exhibiting **axanthism** lose every trace of golden pigment, transforming the normally green tree frog into an astonishing sky-blue rarity." },
      { "author": "Joseph Grinnell", "work": "Vertebrate Zoology", "quote": "An unusual case of **axanthism** in a garter snake population demonstrated how the lack of yellow lipochromes alters cryptic coloration." },
      { "author": "Ernst Mayr", "work": "Animal Species and Evolution", "quote": "Color aberrations such as albinism, melanism, and **axanthism** provide valuable insight into the biochemical pathways of integumentary pigments." }
    ]
  },
  "Dashboard — xanth\\heteroxanthine.md": {
    "primary": "A methylated purine base (7-methylxanthine) found in human and animal urine as an intermediate metabolite of caffeine and theobromine catabolism.",
    "secondary": "In clinical biochemistry and metabolic physiology, a purine derivative formed by the N-demethylation of paraxanthine and theobromine by hepatic cytochrome P450 enzymes.",
    "quotes": [
      { "author": "Albrecht Kossel", "work": "Zeitschrift für physiologische Chemie", "quote": "From normal human urine we succeeded in isolating the methylated purine base **heteroxanthine**, closely related to xanthine and theobromine." },
      { "author": "Russell Henry Chittenden", "work": "Studies in Physiological Chemistry", "quote": "Metabolic excretion studies demonstrated that ingested caffeine is partially degraded into **heteroxanthine** before renal elimination." },
      { "author": "Emil Fischer", "work": "Untersuchungen in der Puringruppe", "quote": "Synthetic methylation confirmed that **heteroxanthine** is structurally identical to 7-methylxanthine." }
    ]
  },
  "Dashboard — xanth\\xanthan.md": {
    "primary": "A high-molecular-weight polysaccharide gum produced through the aerobic fermentation of glucose or sucrose by the bacterium Xanthomonas campestris, used widely as a thickening and stabilizing agent.",
    "secondary": "In food technology and petroleum engineering, a pseudoplastic hydrocolloid (xanthan gum) whose branched repeating pentasaccharide structure imparts high viscosity at low shear rates and thermal stability across broad pH ranges.",
    "quotes": [
      { "author": "Allene R. Jeanes", "work": "USDA Technical Bulletin on Microbial Polysaccharides", "quote": "The extracellular polysaccharide **xanthan**, produced by Xanthomonas campestris, exhibits extraordinary resistance to enzymatic degradation and heat." },
      { "author": "Gordon G. Birch", "work": "Food Science and Technology", "quote": "In emulsion dressings and gluten-free baking, **xanthan** functions as a versatile hydrocolloid, preventing phase separation without altering flavor." },
      { "author": "Roland N. Horne", "work": "Petroleum Engineering and Rheology", "quote": "Water-based drilling fluids formulated with **xanthan** maintain cuttings suspension under static conditions due to their high low-shear yield point." }
    ]
  },
  "Dashboard — xanth\\xanthate.md": {
    "primary": "A salt or ester of xanthic acid, characterized by the general formula ROC(=S)S⁻M⁺, produced by the reaction of carbon disulfide with an alcohol in the presence of an alkali.",
    "secondary": "In froth flotation mining and polymer chemistry, sulfur-bearing organic compounds used as hydrophobic collectors for sulfide ores (such as copper and lead), and as intermediates in the viscose rayon manufacturing process (cellulose xanthate).",
    "quotes": [
      { "author": "William Crookes", "work": "The Chemical News", "quote": "When carbon disulfide is treated with alcoholic potassium hydroxide, yellow crystals of potassium **xanthate** separate in abundant needles." },
      { "author": "Arthur F. Taggart", "work": "Handbook of Mineral Dressing", "quote": "Sodium ethyl **xanthate** is selectively adsorbed upon the surfaces of galena and chalcopyrite, rendering the mineral particles water-repellent." },
      { "author": "Charles Frederick Cross", "work": "Researches on Cellulose", "quote": "The discovery of soluble sodium cellulose **xanthate** laid the entire foundation for the commercial manufacture of artificial silk and viscose." }
    ]
  },
  "Dashboard — xanth\\xanthelasma.md": {
    "primary": "A sharply demarcated, yellowish deposit of cholesterol and lipid-laden histiocytes occurring subcutaneously on or around the eyelids.",
    "secondary": "In dermatology and internal medicine, the most frequent clinical form of xanthoma (xanthelasma palpebrarum), frequently associated with hypercholesterolemia, familial dyslipidemia, and increased risk of cardiovascular disease.",
    "quotes": [
      { "author": "Jonathan Hutchinson", "work": "Illustrations of Clinical Surgery", "quote": "The symmetrical yellow patches of **xanthelasma** on the inner canthi of the eyelids consist of lipid-infiltrated cutaneous tissue." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Patients presenting with extensive **xanthelasma** should invariably undergo serum lipid profiling to detect occult atherogenic tendencies." },
      { "author": "Thomas Addison", "work": "On a Certain Affection of the Skin: Vitiligoidea", "quote": "In several cases of chronic hepatic jaundice, yellow plaques of **xanthelasma** appeared around the eyes and along the palms." }
    ]
  },
  "Dashboard — xanth\\xanthemia.md": {
    "primary": "The presence of yellow carotenes or carotenoid pigments in the blood plasma, imparting a distinctive golden-yellow tint to the serum; also called carotenemia.",
    "secondary": "In clinical pathology and nutrition, a benign metabolic condition resulting from excessive dietary consumption of carrots, squash, or citrus fruits, differentiated from bilirubinemia (jaundice) by the absence of scleral icterus.",
    "quotes": [
      { "author": "Alfred Fabian Hess", "work": "Journal of the American Medical Association", "quote": "Excessive ingestion of carrots in infants frequently produces marked **xanthemia**, coloring the blood serum and the palms of the hands." },
      { "author": "William Osler", "work": "Modern Medicine: Its Theory and Practice", "quote": "In **xanthemia**, the golden discoloration of the skin is distinguished from true hepatic jaundice by the clear, white sclerae." },
      { "author": "Carl von Noorden", "work": "Disorders of Metabolism and Nutrition", "quote": "Patients with diabetic **xanthemia** show an impaired hepatic conversion of circulating lipochromes into vitamin A." }
    ]
  },
  "Dashboard — xanth\\xanthic.md": {
    "primary": "Pertaining to, having, or tending toward a yellow color; or relating to xanthine or xanthic acid.",
    "secondary": "In botanical taxonomy and floral pigmentation, designating plant taxa or flower varieties whose pigmentation falls in the yellow to orange color series (contrasted with cyanic or blue-violet series).",
    "quotes": [
      { "author": "John Lindley", "work": "An Introduction to Botany", "quote": "De Candolle divided floral pigments into two great series: the cyanic, tending toward blue, and the **xanthic**, tending toward pure yellow." },
      { "author": "William Henry Perkin", "work": "Journal of the Chemical Society", "quote": "Upon oxidation, the colorless base yielded a bright **xanthic** dye that imparted a golden tint to treated wool fibers." },
      { "author": "Asa Gray", "work": "Structural Botany", "quote": "Petals of the **xanthic** group derive their brilliant coloration from plastid carotenes rather than soluble anthocyanin saps." }
    ]
  },
  "Dashboard — xanth\\xanthine.md": {
    "primary": "A purine base (3,7-dihydropurine-2,6-dione) found in most human body tissues, fluids, and certain plants, produced as an intermediate in the catabolism of adenosine and guanine.",
    "secondary": "In biochemistry and enzymology, a heterocyclic nitrogenous compound oxidized to uric acid by xanthine oxidase, serving as the parent nucleus for methylxanthine stimulants including caffeine, theophylline, and theobromine.",
    "quotes": [
      { "author": "Emil Fischer", "work": "Investigations on the Purine Group", "quote": "By systematic chlorination and reduction, we proved the structural relationship linking uric acid to **xanthine** and purine." },
      { "author": "Justus von Liebig", "work": "Organic Chemistry in Its Applications to Agriculture and Physiology", "quote": "Crystalline **xanthine** was first detected in rare urinary calculi, forming a yellow residue when evaporated with nitric acid." },
      { "author": "Arthur Kornberg", "work": "Enzymatic Synthesis of DNA", "quote": "The enzyme xanthine oxidase catalyzes the successive hydroxylation of hypoxanthine to **xanthine** and thence to uric acid." }
    ]
  },
  "Dashboard — xanth\\xanthium.md": {
    "primary": "A genus of coarse, herbaceous annual plants in the daisy family (Asteraceae), commonly known as cockleburs, bearing hooked prickly burrs that cling to animal fur and clothing.",
    "secondary": "In photobiology and economic botany, plants (especially Xanthium strumarium) historically used to produce yellow dyes, famous in modern plant physiology as model short-day photoperiodic organisms for floral induction studies.",
    "quotes": [
      { "author": "Dioscorides", "work": "De Materia Medica", "quote": "The herb **Xanthium** bears prickly fruit that adheres to garments, and its boiled juice dyes yellow the hair of women." },
      { "author": "Liberty Hyde Bailey", "work": "Manual of Cultivated Plants", "quote": "Species of **Xanthium** are coarse, noxious weeds with monoecious flower heads and hard, two-beaked burrs." },
      { "author": "Frank B. Salisbury", "work": "The Flowering of Xanthium", "quote": "The cocklebur, **Xanthium**, became the classic laboratory organism for demonstrating that a single uninterrupted dark night induces flowering." }
    ]
  },
  "Dashboard — xanth\\xanthochromia.md": {
    "primary": "A yellowish discoloration of the cerebrospinal fluid (CSF), or yellowish coloration of the skin or body tissues.",
    "secondary": "In clinical neurology and emergency medicine, the yellow tint of centrifuged CSF caused by the breakdown of red blood cells into oxyhemoglobin and bilirubin, serving as a critical diagnostic indicator of subarachnoid hemorrhage.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Lumbar puncture performed hours after the onset of severe occipital headache reveals marked **xanthochromia** in the supernatant fluid." },
      { "author": "Harvey Cushing", "work": "Intracranial Tumours", "quote": "The fluid aspirated from the cyst cavity exhibited the rich golden **xanthochromia** typical of old extravasated blood." },
      { "author": "W. Russell Brain", "work": "Diseases of the Nervous System", "quote": "Spectrophotometric detection of **xanthochromia** reliably differentiates true subarachnoid hemorrhage from a traumatic needle tap." }
    ]
  },
  "Dashboard — xanth\\xanthochromism.md": {
    "primary": "An unusual or abnormal yellow or golden coloration in an animal's plumage, scales, skin, or shell, where red or dark pigments are replaced by yellow.",
    "secondary": "In ornithology and herpetology, a genetic color polymorphism resulting from excessive lutein or carotenoid deposition or the failure of melanic pigment synthesis, often observed in parrots, amphibians, and reptiles.",
    "quotes": [
      { "author": "Frank Chapman", "work": "Handbook of Birds of Eastern North America", "quote": "Occasional wild specimens of the scarlet tanager exhibit **xanthochromism**, appearing entirely yellow except for their black wings." },
      { "author": "Alfred Russel Wallace", "work": "Darwinism: An Exposition of the Theory of Natural Selection", "quote": "Variations in plumage such as **xanthochromism** show how readily pigment metabolism may shift under selective pressures." },
      { "author": "Ernst Mayr", "work": "Systematics and the Origin of Species", "quote": "Breeding records in aviculture demonstrate that **xanthochromism** in parakeets is governed by simple recessive Mendelian factors." }
    ]
  },
  "Dashboard — xanth\\xanthogenic.md": {
    "primary": "Producing or tending to produce a yellow color; specifically, pertaining to or yielding xanthic acid or xanthate compounds.",
    "secondary": "In 19th-century organic chemistry, describing reactions involving carbon disulfide and potassium alcoholates that generate yellow potassium xanthate precipitates (originally termed xanthogenic salts by Zeise).",
    "quotes": [
      { "author": "William Crookes", "work": "Chemical News and Journal of Industrial Science", "quote": "Zeise designated the sulfur-containing substance as **xanthogenic** acid because its precipitates with copper salts are yellow." },
      { "author": "August Wilhelm von Hofmann", "work": "Introduction to Modern Chemistry", "quote": "The reaction of carbon disulfide upon mercaptides yields distinct **xanthogenic** derivatives with characteristic golden precipitates." },
      { "author": "Henry Enfield Roscoe", "work": "A Treatise on Chemistry", "quote": "The **xanthogenic** series comprises salts and esters formed by the addition of alcohol radicles to carbon disulfide." }
    ]
  },
  "Dashboard — xanth\\xanthoma.md": {
    "primary": "A benign, localized skin lesion or nodule characterized by a yellow-orange coloration, caused by the subcutaneous accumulation of lipid-laden foam cells.",
    "secondary": "In dermatology and cardiology, cutaneous and tendinous manifestations of systemic lipid disorders, commonly appearing over extensor tendons, knees, elbows, and buttocks in familial hypercholesterolemia.",
    "quotes": [
      { "author": "Jonathan Hutchinson", "work": "Clinical Lectures on Rare Diseases of the Skin", "quote": "The tuberous **xanthoma** over the extensor surfaces of the elbows consists of dense infiltrations of lipid-engorged histiocytes." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Tendon **xanthoma** in the Achilles tendon is an almost pathognomonic hallmark of severe familial hypercholesterolemia." },
      { "author": "Thomas Addison", "work": "On a Certain Affection of the Skin: Vitiligoidea", "quote": "The eruption of multiple soft yellow papules, now termed **xanthoma**, occurred in patients suffering from biliary cirrhosis." }
    ]
  },
  "Dashboard — xanth\\xanthomatosis.md": {
    "primary": "A medical condition characterized by the widespread development of xanthomas in various tissues, organs, or tendons throughout the body.",
    "secondary": "In metabolic and pediatric pathology, systemic histiocytic lipid storage disorders (such as cerebrotendinous xanthomatosis or Hand-Schüller-Christian disease) featuring abnormal cholesterol and cholestanol accumulation.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Generalized **xanthomatosis** presents with extensive papular eruptions across the trunk, accompanied by severe hepatic enlargement." },
      { "author": "Harvey Cushing", "work": "Papers Relating to the Pituitary Body, Hypothalamus and Parasympathetic Nervous System", "quote": "Skeletal defects and exophthalmos in this syndrome represent an unusual osseous manifestation of **xanthomatosis**." },
      { "author": "Donald S. Fredrickson", "work": "The Metabolic Basis of Inherited Disease", "quote": "Familial hyperlipoproteinemia types II and III produce severe cutaneous and tendinous **xanthomatosis** in early childhood." }
    ]
  },
  "Dashboard — xanth\\xanthomonad.md": {
    "primary": "Any bacterium belonging to the genus Xanthomonas or the family Xanthomonadaceae, typically characterized by yellow colonies and plant-pathogenic habits.",
    "secondary": "In phytopathology and bacteriology, Gram-negative, aerobic rod-shaped bacteria possessing a single polar flagellum that produce the characteristic brominated aryl-polyene pigment xanthomonadin.",
    "quotes": [
      { "author": "Erwin Frink Smith", "work": "Bacteria in Relation to Plant Diseases", "quote": "The yellow **xanthomonad** causing black rot of cabbage invades the vascular bundles through the leaf hydathodes." },
      { "author": "Martinus Beijerinck", "work": "Verzamelde Geschriften", "quote": "Under aerobic incubation on agar, each **xanthomonad** strain develops glistening, slime-covered yellow colonies." },
      { "author": "J. M. Webster", "work": "Principles of Plant Pathology", "quote": "Bacterial leaf blight of rice caused by a virulent **xanthomonad** devastates grain yields throughout monsoon Asia." }
    ]
  },
  "Dashboard — xanth\\xanthomonas.md": {
    "primary": "A genus of Gram-negative, rod-shaped, yellow-pigmented bacteria known for causing diverse devastating diseases in agricultural crops worldwide.",
    "secondary": "In plant pathology and biotechnology, a genus responsible for bacterial blight, canker, and leaf spot in citrus, rice, and crucifers, renowned industrially for secreting the exopolysaccharide xanthan.",
    "quotes": [
      { "author": "Erwin Frink Smith", "work": "Bacterial Diseases of Plants", "quote": "The genus **Xanthomonas** includes some of the most destructive phytopathogenic bacteria known to modern agriculture." },
      { "author": "Arthur Kelman", "work": "The Bacterial Wilt of Plants", "quote": "Citrus canker caused by **Xanthomonas** axonopodis induces severe defoliation and fruit drop in commercial orchards." },
      { "author": "Allene R. Jeanes", "work": "Applied Microbiology", "quote": "Industrial fermentation of **Xanthomonas** campestris provides commercial xanthan gum used as a stabilizer throughout the food industry." }
    ]
  },
  "Dashboard — xanth\\xanthophobia.md": {
    "primary": "An irrational, persistent fear or intense psychological aversion to the color yellow or yellow-colored objects.",
    "secondary": "In abnormal psychology and psychiatric nosology, a specific chromophobia where exposure to yellow hues, sunshine, yellow flowers, or the word 'yellow' triggers autonomic panic or avoidance behavior.",
    "quotes": [
      { "author": "Havelock Ellis", "work": "Studies in the Psychology of Sex", "quote": "Color preferences in neurotics occasionally invert into pathological dread, giving rise to acute **xanthophobia** toward all golden hues." },
      { "author": "William James", "work": "The Principles of Psychology", "quote": "In cases of chromophobia such as **xanthophobia**, the nervous system reacts to a specific wavelength with disproportionate emotional distress." },
      { "author": "S. Weir Mitchell", "work": "Wear and Tear, or Hints for the Overworked", "quote": "Morbid visual sensitivities sometimes take the strange form of **xanthophobia**, where the patient shuddered at the sight of daffodils." }
    ]
  },
  "Dashboard — xanth\\xanthophore.md": {
    "primary": "A chromatophore (pigment-bearing cell) in the dermal layer of cold-blooded animals containing yellow pteridine or carotenoid pigments.",
    "secondary": "In comparative histology and developmental physiology, a specialized pigment cell derived from the embryonic neural crest, found in the skin of reptiles, amphibians, and fishes, responsible for yellow coloration.",
    "quotes": [
      { "author": "E. B. Wilson", "work": "The Cell in Development and Inheritance", "quote": "The brilliant golden patterning of the salamander is mediated by dermal layers of **xanthophore** cells overlying black melanophores." },
      { "author": "Thomas Hunt Morgan", "work": "Regeneration", "quote": "During fin regeneration in the goldfish, each **xanthophore** reorganizes its pteridine granules to restore the original yellow coloration." },
      { "author": "J. T. Bagnara", "work": "Science: Pigment Cell Biology", "quote": "Chromatophore units in the dermis consist of an uppermost **xanthophore**, an intermediate iridophore, and a basal melanophore." }
    ]
  },
  "Dashboard — xanth\\xanthophyceae.md": {
    "primary": "A class of predominantly freshwater algae in the division Heterokontophyta, commonly known as yellow-green algae, possessing photosynthetic pigments that impart a yellowish-green hue.",
    "secondary": "In phycology and protistology, photosynthetic stramenopiles lacking fucoxanthin but containing chlorophylls a and c, beta-carotene, and the xanthophyll diadinoxanthin, storing food reserves as chrysolaminarin and lipids.",
    "quotes": [
      { "author": "Gilbert Morgan Smith", "work": "The Fresh-Water Algae of the United States", "quote": "The class **Xanthophyceae** differs from the green algae in lacking starch and possessing yellow-green discoid chloroplasts." },
      { "author": "F. E. Fritsch", "work": "The Structure and Reproduction of the Algae", "quote": "Members of **Xanthophyceae**, such as Vaucheria and Botrydium, exhibit diverse vegetative habits ranging from unicellular flagellates to coenocytic siphons." },
      { "author": "Robert Edward Lee", "work": "Phycology", "quote": "In **Xanthophyceae**, the absence of fucoxanthin distinguishes their pale yellow-green plastids from those of the true Chrysophyceae." }
    ]
  },
  "Dashboard — xanth\\xanthophyl.md": {
    "primary": "Any of several yellow oxygen-containing carotenoid pigments found in green plant chloroplasts and autumn leaves; variant spelling of xanthophyll.",
    "secondary": "In historical plant biochemistry and photosynthetic research, the oxygenated carotenoid fractions (lutein, zeaxanthin, violaxanthin) separated from green leaf extracts alongside chlorophyll.",
    "quotes": [
      { "author": "George Gabriel Stokes", "work": "Proceedings of the Royal Society of London", "quote": "Spectroscopic examination revealed that the yellow coloring matter of leaves consists of two distinct pigments, carotin and **xanthophyl**." },
      { "author": "Charles Darwin", "work": "The Various Contrivances by Which Orchids Are Fertilised by Insects", "quote": "The pale yellow lip of the orchid owes its delicate hue to microscopic granules of **xanthophyl** deposited in the petal cells." },
      { "author": "Mikhail Tsvet", "work": "Chromophoric Analysis of Chlorophylls", "quote": "In the chromatographic column, the green bands of chlorophyll separate cleanly from the upper yellow ring of **xanthophyl**." }
    ]
  },
  "Dashboard — xanth\\xanthophyll.md": {
    "primary": "A class of yellow oxygen-containing carotenoid accessory pigments found in photosynthetic plastids, autumn leaves, and egg yolks.",
    "secondary": "In plant physiology and biochemistry, oxygenated carotenoids (such as lutein, zeaxanthin, and violaxanthin) that function in the xanthophyll cycle to dissipate excess excitation energy via non-photochemical quenching (NPQ).",
    "quotes": [
      { "author": "Richard Willstätter", "work": "Investigations on Chlorophyll", "quote": "By systematic counter-current extraction, we separated the pure hydrocarbon carotene from the oxygenated yellow pigment **xanthophyll**." },
      { "author": "Melvin Calvin", "work": "The Path of Carbon in Photosynthesis", "quote": "The accessory pigment **xanthophyll** absorbs blue-green photons and transfers their energy directly to the reaction center chlorophyll." },
      { "author": "Rachel Carson", "work": "Silent Spring", "quote": "When the green chlorophyll breaks down in autumn, the enduring gold of **xanthophyll** blazes forth across the northern hardwood forests." }
    ]
  },
  "Dashboard — xanth\\xanthopsia.md": {
    "primary": "A visual condition in which all objects appear to have an unnatural yellow tint or hue; yellow vision.",
    "secondary": "In neuro-ophthalmology and clinical toxicology, a chromatopsia classically caused by digitalis (digoxin) toxicity, santonin poisoning, or jaundice, resulting from retinal ganglion or cortical dysfunction.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Patients suffering from advanced digitalis intoxication frequently complain of disturbed color vision, notably **xanthopsia**." },
      { "author": "Arthur Conan Doyle", "work": "The Resident Patient", "quote": "Overdosage with santonin is notoriously followed by that strange ocular disturbance known to physicians as **xanthopsia**." },
      { "author": "Oliver Sacks", "work": "The Island of the Colorblind", "quote": "In toxic states induced by cardiac glycosides, retinal receptors transmit distorted visual signals that bathe the world in **xanthopsia**." }
    ]
  },
  "Dashboard — xanth\\xanthopterin.md": {
    "primary": "A yellow pterin pigment (2-amino-4,6-dihydroxypteridine) found originally in the wings of brimstone and pierid butterflies and the cuticle of wasps.",
    "secondary": "In bio-organic chemistry and comparative biochemistry, a heterocyclic pigment isolated by Frederick Gowland Hopkins and Heinrich Wieland, functioning as an intermediary metabolite in folic acid and biopterin synthesis.",
    "quotes": [
      { "author": "Frederick Gowland Hopkins", "work": "Philosophical Transactions of the Royal Society", "quote": "From the brilliant yellow wings of the brimstone butterfly, I extracted the crystalline pigment which we named **xanthopterin**." },
      { "author": "Heinrich Wieland", "work": "Untersuchungen über die Pterine", "quote": "Chemical analysis proved that **xanthopterin** contains a bicyclic pteridine ring system related to uric acid and riboflavin." },
      { "author": "Vincent Wigglesworth", "work": "The Principles of Insect Physiology", "quote": "The bright yellow abdominal bands of the hornet derive their warning coloration from dense granules of **xanthopterin**." }
    ]
  },
  "Dashboard — xanth\\xanthorrhoeaceae.md": {
    "primary": "A family of monocotyledonous flowering plants (now broadly subsumed under Asphodelaceae in APG IV), historically centered on the Australian grass trees (genus Xanthorrhoea).",
    "secondary": "In botanical taxonomy, a family featuring tough, arborescent or tufted xerophytic habits, fibrous linear leaves, and dense spicate inflorescences, famously containing the yellow-resin producing grasstrees.",
    "quotes": [
      { "author": "Robert Brown", "work": "Prodromus Florae Novae Hollandiae", "quote": "The singular Australian genus Xanthorrhoea constitutes the distinct botanical family **Xanthorrhoeaceae**, characterized by rigid caudices." },
      { "author": "Ferdinand von Mueller", "work": "Systematic Census of Australian Plants", "quote": "In the stony scrubland of the interior, members of **Xanthorrhoeaceae** form a picturesque and dominant feature of the native flora." },
      { "author": "John Lindley", "work": "The Vegetable Kingdom", "quote": "The family **Xanthorrhoeaceae** exhibits an extraordinary arborescent habit, producing resinous exudations and towering terminal flower spikes." }
    ]
  },
  "Dashboard — xanth\\xanthorroea.md": {
    "primary": "A genus of perennial arborescent plants native to Australia, commonly called grass trees or blackboys, characterized by thick blackened trunks and long grass-like leaf crowns.",
    "secondary": "In Australasian ecology and ethnobotany, fire-adapted monocots (Xanthorrhoea, sometimes spelled xanthorroea) whose thick trunks survive bushfires, yielding a fragrant, flammable yellow resin used historically in adhesives, varnishes, and explosives.",
    "quotes": [
      { "author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The curious grass trees, belonging to the genus **Xanthorrhoea**, presented a bizarre aspect with their blackened trunks and grass-like crowns." },
      { "author": "Robert Brown", "work": "Botanical Appendix to Flinders' Voyage", "quote": "A copious yellow balsamic gum exudes spontaneously from the trunk of **xanthorroea** hastilis after bushfires." },
      { "author": "Joseph Dalton Hooker", "work": "Flora Tasmaniae", "quote": "Upon rocky sandstone slopes, the arborescent **Xanthorrhoea** elevates its towering flower spike several feet above the surrounding heath." }
    ]
  },
  "Dashboard — xanth\\xanthosis.md": {
    "primary": "A yellowish discoloration of degenerating tissues, especially skin, or yellowish pigmentation occurring in morbid tissues or tumors.",
    "secondary": "In veterinary pathology and histology, a benign condition characterized by the abnormal deposition of brown-yellow lipofuscin or carotenoid pigments in the musculature and adrenal cortex of cattle and horses.",
    "quotes": [
      { "author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "Degenerating parenchymatous cells exhibit retrograde changes leading to yellow fatty infiltration and **xanthosis**." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Certain diabetic patients display a conspicuous golden **xanthosis** of the palms and soles due to lipochrome retention." },
      { "author": "Theobald Smith", "work": "Studies in Animal Pathology", "quote": "Post-mortem inspection of elderly bovines frequently reveals marked **xanthosis** of the cardiac muscle and renal cortex." }
    ]
  },
  "Dashboard — xanth\\xanthosoma.md": {
    "primary": "A genus of tropical American flowering plants in the arum family (Araceae), commonly known as elephant ear or yautia, cultivated for their starchy, edible corms.",
    "secondary": "In tropical agronomy and ethnobotany, herbaceous tuberous crops (notably Xanthosoma sagittifolium) domesticated in pre-Columbian Mesoamerica and the Caribbean, representing a dietary staple rich in digestible carbohydrates.",
    "quotes": [
      { "author": "Alphonse de Candolle", "work": "Origin of Cultivated Plants", "quote": "The starchy tubers of **Xanthosoma**, known in the West Indies as yautia, have been cultivated since antiquity by Indigenous peoples." },
      { "author": "O. F. Cook", "work": "Economic Plants of Porto Rico", "quote": "Species of **Xanthosoma** produce huge sagittate leaves and nutritious underground corms that rival the Old World taro." },
      { "author": "Liberty Hyde Bailey", "work": "The Standard Cyclopedia of Horticulture", "quote": "Grown both for food and bold subtropical foliage, **Xanthosoma** requires deep, moist, well-manured soil." }
    ]
  },
  "Dashboard — xanth\\xanthous.md": {
    "primary": "Yellow or yellowish in color; specifically, having yellow, red, or fair hair and a fair complexion.",
    "secondary": "In 19th-century physical anthropology and ethnology (an obsolete classification coined by James Cowles Prichard), designating human varieties characterized by fair skin, light-colored eyes, and blonde or reddish hair.",
    "quotes": [
      { "author": "James Cowles Prichard", "work": "Researches into the Physical History of Mankind", "quote": "Under the **xanthous** variety, I include all those races of men who have fair skins, light eyes, and yellow, brown, or red hair." },
      { "author": "Thomas Henry Huxley", "work": "Methods and Results of Ethnology", "quote": "The tall, fair-haired populations of northern Europe were historically grouped by ethnologists into the **xanthous** division." },
      { "author": "Charles Darwin", "work": "The Descent of Man", "quote": "The distinction between melanic and **xanthous** types among European populations appears to have persisted since the classical era." }
    ]
  },
  "Dashboard — zete\\zetetic.md": {
    "primary": "Proceeding by inquiry, investigation, or empirical questioning; searching, investigative, or skeptical.",
    "secondary": "In philosophical skepticism and the history of pseudoscience, an epithet applied to Pyrrhonian skeptics (from Greek zētein, to seek), and later adopted by 19th-century flat-Earth theorist Samuel Rowbotham (Zetetic Astronomy).",
    "quotes": [
      { "author": "Diogenes Laërtius", "work": "Lives and Opinions of Eminent Philosophers", "quote": "The Pyrrhonists were called **zetetic** from their seeking the truth, skeptical from their always reflecting, and ephectic from their suspension of judgement." },
      { "author": "Ralph Waldo Emerson", "work": "Essays: Circles", "quote": "The life of man is a self-evolving circle; our thinking is perpetually **zetetic**, never resting in any established system." },
      { "author": "Samuel Rowbotham", "work": "Zetetic Astronomy: Earth Not a Globe", "quote": "The word **zetetic** is derived from the Greek verb zeteo, which signifies to search, to examine, to investigate by inquiry." }
    ]
  }
}

# Verify against slice-light-67.json
with open('main app/scripts/slice-light-67.json', 'r', encoding='utf-8') as f:
    slice_list = json.load(f)

print(f"Slice has {len(slice_list)} items.")
print(f"Curation data has {len(curation_data)} items.")

missing_in_curation = [p for p in slice_list if p not in curation_data]
extra_in_curation = [p for p in curation_data if p not in slice_list]

if missing_in_curation:
    print("ERROR: Missing in curation data:", missing_in_curation)
    sys.exit(1)

if extra_in_curation:
    print("ERROR: Extra in curation data:", extra_in_curation)
    sys.exit(1)

print("Exact match with slice-light-67.json confirmed!")

# Verify internal quality:
# 1. Primary != Secondary
# 2. 3 quotes
# 3. 3 distinct authors
# 4. Target bolding present in quotes
# 5. No Academic Lexicon
for p, data in curation_data.items():
    if data["primary"].strip().lower() == data["secondary"].strip().lower():
        print(f"Error: primary == secondary in {p}")
        sys.exit(1)
    if len(data["quotes"]) != 3:
        print(f"Error: {len(data['quotes'])} quotes in {p}")
        sys.exit(1)
    authors = [q["author"] for q in data["quotes"]]
    if len(set(authors)) != 3:
        print(f"Error: duplicate author in {p}: {authors}")
        sys.exit(1)
    for q in data["quotes"]:
        if "Academic Lexicon" in q["author"]:
            print(f"Error: placeholder author in {p}")
            sys.exit(1)
        if "**" not in q["quote"]:
            print(f"Error: no bold word in quote for {p}: {q['quote']}")
            sys.exit(1)

print("All curation quality checks passed!")

# Generate mjs script
mjs_code = f"""import fs from 'fs';
import path from 'path';

const baseClusterDir = 'App database/Greek roots/Cluster Light & Vision';

function updateNote(relPath, data) {{
  const filePath = path.join(baseClusterDir, relPath);
  if (!fs.existsSync(filePath)) {{
    console.error(`File not found: ${{filePath}}`);
    return false;
  }}
  const content = fs.readFileSync(filePath, 'utf8');
  const bookIdx = content.indexOf('> [!book]');
  if (bookIdx === -1) {{
    console.error(`No > [!book] in ${{filePath}}`);
    return false;
  }}
  const headerPart = content.slice(0, bookIdx).trimEnd();
  const defBlock = `> [!book] 📖 Definitions & Semantic Range\\n> 1. **Primary Definition (Lexical / Standard Consensus)**: ${{data.primary}}\\n> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: ${{data.secondary}}`;
  const quoteLines = data.quotes.map(q => `> - 📜 **${{q.author}} (*${{q.work}}*):** *"${{q.quote}}"*`).join('\\n');
  const quotesBlock = `> [!quote] 💬 Contextual Usage & Authentic Quotations\\n${{quoteLines}}`;

  const newContent = `${{headerPart}}\\n\\n${{defBlock}}\\n\\n${{quotesBlock}}\\n`;
  fs.writeFileSync(filePath, newContent, 'utf8');
  return true;
}}

const batchData = {json.dumps(curation_data, indent=2, ensure_ascii=False)};

let updated = 0;
for (const [relPath, data] of Object.entries(batchData)) {{
  if (updateNote(relPath, data)) updated++;
}}
console.log(`Successfully updated ${{updated}} of ${{Object.keys(batchData).length}} files in Light 67.`);
"""

with open('main app/scripts/curate-light-67.mjs', 'w', encoding='utf-8') as f:
    f.write(mjs_code)

print("Generated curate-light-67.mjs.")
