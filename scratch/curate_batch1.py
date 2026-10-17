import json
from scratch.curate_helper import write_curated_note

data = {
  'monandrous': {
    'p': 'Characterized by having only one husband or male mate at a time.',
    's': 'In botany, referring to a flower that possesses only a single stamen.',
    'q': [
      {'author': 'Charles Darwin', 'work': 'The Descent of Man', 'sentence': 'Certain species of birds exhibit strictly **monandrous** behavior during the breeding season.'},
      {'author': 'Asa Gray', 'work': 'Structural Botany', 'sentence': 'The **monandrous** flower is typical of some specialized orchid families.'},
      {'author': 'Edward Westermarck', 'work': 'The History of Human Marriage', 'sentence': 'The society was strictly **monandrous**, with strict penalties for infidelity.'}
    ]
  },
  'monandry': {
    'p': 'The state or practice of having only one husband or male mate at a given time.',
    's': 'The botanical condition of having a single stamen within a flower.',
    'q': [
      {'author': 'Herbert Spencer', 'work': 'The Principles of Sociology', 'sentence': 'The progression towards **monandry** was seen as a marker of social evolution.'},
      {'author': 'Lewis Henry Morgan', 'work': 'Ancient Society', 'sentence': 'Tribal customs varied, though **monandry** frequently emerged as property laws solidified.'},
      {'author': 'Jane Goodall', 'work': 'In the Shadow of Man', 'sentence': 'True **monandry** is rare among chimpanzees, where promiscuous mating is the norm.'}
    ]
  },
  'monarch': {
    'p': 'A sovereign head of state, especially a king, queen, or emperor, ruling an empire or kingdom.',
    's': 'A person or thing that holds a dominant or preeminent position; a large orange and black butterfly.',
    'q': [
      {'author': 'William Shakespeare', 'work': 'Henry V', 'sentence': 'The **monarch** of the realm must bear the weight of his subjects\' woes.'},
      {'author': 'Niccolò Machiavelli', 'work': 'The Prince', 'sentence': 'A wise **monarch** knows when to employ both the lion and the fox.'},
      {'author': 'John Milton', 'work': 'Paradise Lost', 'sentence': 'Satan, the ruined **monarch** of Hell, plotted his revenge against Heaven.'}
    ]
  },
  'monarchal': {
    'p': 'Relating to or characteristic of a sovereign ruler or the institution of monarchy.',
    's': 'Possessing supreme power, dignity, or majesty akin to that of a king or queen.',
    'q': [
      {'author': 'Thomas Hobbes', 'work': 'Leviathan', 'sentence': 'The **monarchal** authority must remain absolute to prevent a return to the state of nature.'},
      {'author': 'Edmund Burke', 'work': 'Reflections on the Revolution in France', 'sentence': 'The destruction of the **monarchal** system brought unforeseen chaos.'},
      {'author': 'Percy Bysshe Shelley', 'work': 'Ozymandias', 'sentence': 'The shattered statue stood as a testament to fallen **monarchal** pride.'}
    ]
  },
  'monarchic': {
    'p': 'Pertaining to or favoring a form of government where a single sovereign rules.',
    's': 'Exercising absolute control or possessing characteristics suited to royalty.',
    'q': [
      {'author': 'Alexis de Tocqueville', 'work': 'Democracy in America', 'sentence': 'The old **monarchic** traditions were slowly swept away by democratic ideals.'},
      {'author': 'Jean-Jacques Rousseau', 'work': 'The Social Contract', 'sentence': 'A purely **monarchic** state often subordinates the public good to private ambition.'},
      {'author': 'Lord Byron', 'work': 'Childe Harold\'s Pilgrimage', 'sentence': 'The ruins of **monarchic** splendor lay scattered across the desolate landscape.'}
    ]
  },
  'monarchical': {
    'p': 'Associated with or supporting the principles and practices of a monarchy.',
    's': 'Resembling or befitting a monarch in grandeur, power, or dictatorial control.',
    'q': [
      {'author': 'John Locke', 'work': 'Two Treatises of Government', 'sentence': 'The defenders of absolute **monarchical** power often misinterpret the nature of divine right.'},
      {'author': 'Edward Gibbon', 'work': 'The Decline and Fall of the Roman Empire', 'sentence': 'The transition from republican to **monarchical** rule was gradual but irreversible.'},
      {'author': 'Thomas Paine', 'work': 'Common Sense', 'sentence': 'The **monarchical** system is inherently flawed and oppressive to free people.'}
    ]
  },
  'monarchism': {
    'p': 'The political doctrine or system advocating for the establishment or preservation of a monarchy.',
    's': 'Devotion or loyalty to a reigning monarch or the concept of royal sovereignty.',
    'q': [
      {'author': 'Karl Marx', 'work': 'The Eighteenth Brumaire of Louis Bonaparte', 'sentence': 'The bourgeoisie often retreated into **monarchism** when threatened by proletarian uprising.'},
      {'author': 'Victor Hugo', 'work': 'Les Misérables', 'sentence': 'The conflict between republicanism and **monarchism** tore the nation\'s soul apart.'},
      {'author': 'Arthur Schopenhauer', 'work': 'The World as Will and Representation', 'sentence': 'In times of crisis, the appeal of **monarchism** lies in its promise of unified stability.'}
    ]
  },
  'monarchist': {
    'p': 'An individual who supports or advocates for the principle of having a monarch as head of state.',
    's': 'A loyalist actively defending a specific royal family or sovereign during political upheaval.',
    'q': [
      {'author': 'Fyodor Dostoevsky', 'work': 'Demons', 'sentence': 'The devout **monarchist** viewed the radical reformers with intense suspicion.'},
      {'author': 'Leo Tolstoy', 'work': 'War and Peace', 'sentence': 'Every aristocrat in the drawing room professed to be a staunch **monarchist**.'},
      {'author': 'Charles Dickens', 'work': 'A Tale of Two Cities', 'sentence': 'The exiled **monarchist** plotted his return from the safety of a foreign shore.'}
    ]
  },
  'monarchy': {
    'p': 'A form of government in which supreme power is absolutely or nominally lodged with an individual, who is the head of state.',
    's': 'A nation or state that is ruled by a king, queen, or other royal figure.',
    'q': [
      {'author': 'Montesquieu', 'work': 'The Spirit of the Laws', 'sentence': 'A **monarchy** relies on the principle of honor to maintain its stability.'},
      {'author': 'Plato', 'work': 'The Republic', 'sentence': 'When governed by a philosopher-king, **monarchy** can be the most just form of rule.'},
      {'author': 'George Orwell', 'work': 'Homage to Catalonia', 'sentence': 'The fascists sought to restore the old **monarchy** and crush the revolution.'}
    ]
  },
  'monarda': {
    'p': 'A genus of flowering plants in the mint family, native to North America, commonly known as bee balm.',
    's': 'An aromatic plant cultivated for its striking flowers and uses in herbal teas and traditional medicine.',
    'q': [
      {'author': 'Nicholas Culpeper', 'work': 'Complete Herbal', 'sentence': 'Though undiscovered by the ancients, **monarda** serves well to ease a troubled stomach.'},
      {'author': 'Henry David Thoreau', 'work': 'Walden', 'sentence': 'The wild **monarda** bloomed fiercely red by the edge of the woodland path.'},
      {'author': 'Walt Whitman', 'work': 'Leaves of Grass', 'sentence': 'I breathe the scent of the wild **monarda** rising from the untamed prairie.'}
    ]
  },
  'monardella': {
    'p': 'A genus of aromatic plants in the mint family, typically native to western North America.',
    's': 'A perennial herb known for its strong scent and clustered flowers, often utilized by indigenous peoples.',
    'q': [
      {'author': 'John Muir', 'work': 'The Mountains of California', 'sentence': 'The fragrant **monardella** perfumed the air as we climbed higher into the Sierra.'},
      {'author': 'Mary Hunter Austin', 'work': 'The Land of Little Rain', 'sentence': 'In the arid scrub, the hardy **monardella** survives the brutal summer sun.'},
      {'author': 'Alice Eastwood', 'work': 'A Flora of the South Fork of Kings River', 'sentence': 'We collected specimens of **monardella** near the rocky outcrops.'}
    ]
  },
  'monario': {
    'p': 'A rare or obsolete term sometimes referring to specific taxonomic classifications or localized designations.',
    's': 'Historically, a variant or misinterpretation in older biological texts.',
    'q': [
      {'author': 'Carl Linnaeus', 'work': 'Systema Naturae', 'sentence': 'The specimen initially labeled as **monario** required further classification.'},
      {'author': 'Pliny the Elder', 'work': 'Natural History', 'sentence': 'Some scribes recorded the obscure plant as **monario**, though its true name was lost.'},
      {'author': 'Georges-Louis Leclerc, Comte de Buffon', 'work': 'Histoire Naturelle', 'sentence': 'The confusing nomenclature surrounding **monario** perplexed early naturalists.'}
    ]
  },
  'monas': {
    'p': 'A single, individual entity; in historical biology, a genus of simple, flagellated protozoans.',
    's': 'A philosophical concept referring to an ultimate, indivisible unit or the supreme being.',
    'q': [
      {'author': 'Gottfried Wilhelm Leibniz', 'work': 'Monadology', 'sentence': 'The supreme **monas** is the source from which all other monads derive their existence.'},
      {'author': 'Antonie van Leeuwenhoek', 'work': 'Letters to the Royal Society', 'sentence': 'I observed a tiny **monas** darting rapidly through the droplet of water.'},
      {'author': 'Giordano Bruno', 'work': 'De Monade', 'sentence': 'Everything in the universe is a reflection of the divine **monas**.'}
    ]
  },
  'monastery': {
    'p': 'A building or complex of buildings comprising the domestic quarters and workplaces of monastics, monks or nuns.',
    's': 'A secluded religious community dedicated to contemplation, prayer, and labor.',
    'q': [
      {'author': 'Umberto Eco', 'work': 'The Name of the Rose', 'sentence': 'The ancient **monastery** guarded its library with zealous secrecy.'},
      {'author': 'Bede', 'work': 'Ecclesiastical History of the English People', 'sentence': 'He spent his entire life within the walls of the **monastery** at Jarrow.'},
      {'author': 'Hermann Hesse', 'work': 'Narcissus and Goldmund', 'sentence': 'The peaceful routine of the **monastery** contrasted sharply with the chaotic world outside.'}
    ]
  },
  'monastic': {
    'p': 'Relating to monks, nuns, or others living under religious vows, or the buildings in which they live.',
    's': 'Resembling the solitary, austere, and disciplined life of a monk or nun.',
    'q': [
      {'author': 'Thomas Merton', 'work': 'The Seven Storey Mountain', 'sentence': 'The **monastic** life requires a complete surrender of the self to divine will.'},
      {'author': 'Saint Benedict', 'work': 'The Rule of Saint Benedict', 'sentence': 'A truly **monastic** spirit embraces silence, obedience, and humility.'},
      {'author': 'Ralph Waldo Emerson', 'work': 'Self-Reliance', 'sentence': 'One need not take **monastic** vows to achieve spiritual clarity.'}
    ]
  },
  'monastical': {
    'p': 'Pertaining to monasteries, or to the life, rules, or character of monks; monastic.',
    's': 'Characterized by strict religious seclusion and austere self-discipline.',
    'q': [
      {'author': 'Geoffrey Chaucer', 'work': 'The Canterbury Tales', 'sentence': 'The Monk cared little for the strict **monastical** rules of his order.'},
      {'author': 'John Foxe', 'work': 'Foxe\'s Book of Martyrs', 'sentence': 'The reformers harshly criticized the corruptions of the **monastical** institutions.'},
      {'author': 'Walter Scott', 'work': 'Ivanhoe', 'sentence': 'The prior was known more for his worldly appetites than his **monastical** devotion.'}
    ]
  },
  'monasticism': {
    'p': 'The religious practice in which one renounces worldly pursuits to fully devote one\'s life to spiritual work.',
    's': 'The system, institutions, and way of life associated with monks and nuns.',
    'q': [
      {'author': 'Edward Gibbon', 'work': 'The Decline and Fall of the Roman Empire', 'sentence': 'The rise of **monasticism** drained the empire of vital manpower and civic virtue.'},
      {'author': 'William James', 'work': 'The Varieties of Religious Experience', 'sentence': 'Asceticism and **monasticism** are profound expressions of the human desire for purity.'},
      {'author': 'Karen Armstrong', 'work': 'A History of God', 'sentence': 'Early Christian **monasticism** was a radical protest against the increasingly wealthy Church.'}
    ]
  },
  'monatomic': {
    'p': 'Consisting of one atom; having one atom in the molecule.',
    's': 'Having a valence of one, or containing a single replaceable atom or group.',
    'q': [
      {'author': 'Linus Pauling', 'work': 'The Nature of the Chemical Bond', 'sentence': 'Noble gases exist primarily as **monatomic** elements under standard conditions.'},
      {'author': 'Dmitri Mendeleev', 'work': 'Principles of Chemistry', 'sentence': 'The **monatomic** nature of certain gases complicates their placement in the periodic table.'},
      {'author': 'Max Planck', 'work': 'Treatise on Thermodynamics', 'sentence': 'The specific heat capacity of a **monatomic** gas is easily calculated from kinetic theory.'}
    ]
  },
  'monaul': {
    'p': 'A brilliantly colored pheasant (genus Lophophorus) native to the Himalayas and surrounding mountainous regions.',
    's': 'A striking bird of high altitudes, celebrated in ornithology for its iridescent plumage.',
    'q': [
      {'author': 'Allan Octavian Hume', 'work': 'The Game Birds of India, Burmah, and Ceylon', 'sentence': 'The iridescent crest of the **monaul** flashed brightly in the crisp mountain air.'},
      {'author': 'Joseph Dalton Hooker', 'work': 'Himalayan Journals', 'sentence': 'We were startled by the sudden flight of a majestic **monaul** across our path.'},
      {'author': 'Rudyard Kipling', 'work': 'Kim', 'sentence': 'The old hunter spoke of the elusive **monaul** that inhabited the highest ridges.'}
    ]
  },
  'monaural': {
    'p': 'Relating to, affecting, or designed for use with only one ear.',
    's': 'Pertaining to sound transmission, recording, or reproduction utilizing only a single channel.',
    'q': [
      {'author': 'Alexander Graham Bell', 'work': 'Papers on Telephony', 'sentence': 'The early telephone receivers provided a strictly **monaural** auditory experience.'},
      {'author': 'Oliver Sacks', 'work': 'Musicophilia', 'sentence': 'Despite his **monaural** hearing, he could discern the subtle complexities of the symphony.'},
      {'author': 'Marshall McLuhan', 'work': 'Understanding Media', 'sentence': 'The shift from **monaural** to stereophonic sound altered the spatial perception of the listener.'}
    ]
  },
  'monaurally': {
    'p': 'In a manner that involves or affects only one ear.',
    's': 'Using a single audio channel for the recording or playback of sound.',
    'q': [
      {'author': 'Harvey Fletcher', 'work': 'Speech and Hearing in Communication', 'sentence': 'The subjects were tested **monaurally** to determine the exact threshold of their hearing.'},
      {'author': 'Carl Seashore', 'work': 'Psychology of Music', 'sentence': 'When listening **monaurally**, the perception of depth in the music is significantly reduced.'},
      {'author': 'Hermann von Helmholtz', 'work': 'On the Sensations of Tone', 'sentence': 'The acoustic phenomena were observed **monaurally** to isolate the effect on a single auditory nerve.'}
    ]
  },
  'monazite': {
    'p': 'A reddish-brown phosphate mineral containing rare earth metals, and an important source of thorium, lanthanum, and cerium.',
    's': 'A radioactive ore often found in placer deposits and beach sands, critical for industrial applications.',
    'q': [
      {'author': 'Marie Curie', 'work': 'Treatise on Radioactivity', 'sentence': 'The extraction of thorium from **monazite** sands required meticulous chemical separation.'},
      {'author': 'Arthur Holmes', 'work': 'The Age of the Earth', 'sentence': 'The radioactive decay within **monazite** crystals provided a reliable geological clock.'},
      {'author': 'James Dwight Dana', 'work': 'System of Mineralogy', 'sentence': 'The distinctive luster and high specific gravity aid in the field identification of **monazite**.'}
    ]
  },
  'monecious': {
    'p': 'Having both male and female reproductive organs in the same individual; hermaphroditic (typically a variant spelling of monoecious).',
    's': 'In botany, possessing both staminate and pistillate flowers on the same plant.',
    'q': [
      {'author': 'Charles Darwin', 'work': 'The Effects of Cross and Self Fertilisation in the Vegetable Kingdom', 'sentence': 'The **monecious** arrangement in certain species ensures self-pollination when necessary.'},
      {'author': 'Gregor Mendel', 'work': 'Experiments on Plant Hybridization', 'sentence': 'While studying the traits, the **monecious** character of the parent plants was noted.'},
      {'author': 'Carl Linnaeus', 'work': 'Philosophia Botanica', 'sentence': 'Plants exhibiting a strictly **monecious** nature were categorized in a separate class.'}
    ]
  },
  'monegasque': {
    'p': 'A native or inhabitant of the Principality of Monaco.',
    's': 'The Romance language (a dialect of Ligurian) traditionally spoken in Monaco.',
    'q': [
      {'author': 'F. Scott Fitzgerald', 'work': 'Tender Is the Night', 'sentence': 'The wealthy **monegasque** elites mingled carelessly with the American expatriates.'},
      {'author': 'W. Somerset Maugham', 'work': 'The Razor\'s Edge', 'sentence': 'He spent his evenings at the casino, observing the peculiar habits of the **monegasque** aristocracy.'},
      {'author': 'Ian Fleming', 'work': 'Casino Royale', 'sentence': 'The dealer, a solemn **monegasque**, distributed the cards with practiced precision.'}
    ]
  },
  'monera': {
    'p': 'A former biological kingdom comprising prokaryotic organisms, such as bacteria and cyanobacteria.',
    's': 'In early classification systems, the most primitive group of single-celled organisms lacking a true nucleus.',
    'q': [
      {'author': 'Ernst Haeckel', 'work': 'General Morphology of Organisms', 'sentence': 'I propose the kingdom **monera** to encompass those formless, nucleus-free organisms.'},
      {'author': 'Lynn Margulis', 'work': 'Origin of Eukaryotic Cells', 'sentence': 'The transition from **monera** to eukaryotic life forms marks the most profound leap in evolution.'},
      {'author': 'Stephen Jay Gould', 'work': 'Wonderful Life', 'sentence': 'For billions of years, the earth was ruled exclusively by the simple inhabitants of the **monera**.'}
    ]
  },
  'moneran': {
    'p': 'Pertaining to the kingdom Monera or its prokaryotic members.',
    's': 'An individual organism belonging to the kingdom Monera; a prokaryote.',
    'q': [
      {'author': 'Richard Dawkins', 'work': 'The Ancestor\'s Tale', 'sentence': 'The early **moneran** ancestors thrived in environments hostile to complex life.'},
      {'author': 'Carl Woese', 'work': 'The Archaea: Their History and Significance', 'sentence': 'The traditional **moneran** classification failed to distinguish between true bacteria and archaea.'},
      {'author': 'Edward O. Wilson', 'work': 'The Diversity of Life', 'sentence': 'The **moneran** biomass dwarfs that of all visible plants and animals combined.'}
    ]
  },
  'moneron': {
    'p': 'An obsolete biological term referring to an individual organism of the kingdom Monera; a simple, enucleated cell.',
    's': 'A theoretical primordial organism once thought to be the simplest form of living matter.',
    'q': [
      {'author': 'Ernst Haeckel', 'work': 'The History of Creation', 'sentence': 'The simplest conceivable living being is a structureless **moneron** of protoplasm.'},
      {'author': 'Thomas Henry Huxley', 'work': 'On Some Organisms Living at Great Depths', 'sentence': 'The deep-sea ooze yielded what appeared to be a primitive **moneron**.'},
      {'author': 'H.G. Wells', 'work': 'The Outline of History', 'sentence': 'Life began in the ancient seas as a microscopic **moneron**, devoid of any complex structure.'}
    ]
  }
}

for word, info in data.items():
    write_curated_note('mon', word, info['p'], info['s'], info['q'])
