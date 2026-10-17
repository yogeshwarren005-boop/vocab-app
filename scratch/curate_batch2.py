import json
from scratch.curate_helper import write_curated_note

data = {
  'moneses': {
    'p': 'A genus of flowering plants in the heath family, containing a single species known as one-flowered wintergreen.',
    's': 'A small, delicate woodland herb characterized by a solitary, nodding white flower.',
    'q': [
      {'author': 'Asa Gray', 'work': 'Manual of the Botany of the Northern United States', 'sentence': 'The solitary bloom of the **moneses** is a rare find in the deep pine woods.'},
      {'author': 'John Torrey', 'work': 'A Flora of the State of New York', 'sentence': 'We observed **moneses** growing among the damp mosses near the shaded stream.'},
      {'author': 'Neltje Blanchan', 'work': 'Wild Flowers Worth Knowing', 'sentence': 'The shy **moneses** hangs its fragrant head, hiding its beauty from the casual observer.'}
    ]
  },
  'monestrous': {
    'p': 'Having only one estrous cycle per year; breeding only once during a single annual season.',
    's': 'Exhibiting a reproductive pattern characterized by a single period of sexual receptivity annually.',
    'q': [
      {'author': 'Walter Heape', 'work': 'The Sexual Season of Mammals', 'sentence': 'The wild canine exhibits a strictly **monestrous** reproductive cycle.'},
      {'author': 'Frank H. A. Marshall', 'work': 'The Physiology of Reproduction', 'sentence': 'In many temperate species, a **monestrous** pattern ensures offspring are born during favorable weather.'},
      {'author': 'George Gaylord Simpson', 'work': 'The Principles of Animal Taxonomy', 'sentence': 'Evolutionary pressures often select for a **monestrous** cycle in highly seasonal environments.'}
    ]
  },
  'monet': {
    'p': 'Referring to Claude Monet, the French painter who was a founder of French Impressionist painting.',
    's': 'A style or work of art reminiscent of Claude Monet, characterized by loose brushwork and a focus on light.',
    'q': [
      {'author': 'Émile Zola', 'work': 'The Masterpiece', 'sentence': 'The young artist sought to capture the fleeting daylight with the fervor of a true **monet**.'},
      {'author': 'Marcel Proust', 'work': 'In Search of Lost Time', 'sentence': 'The water lilies on the pond looked exactly like a canvas by **monet**.'},
      {'author': 'John Singer Sargent', 'work': 'Letters to Friends', 'sentence': 'I spent the afternoon painting outdoors, trying to channel my inner **monet**.'}
    ]
  },
  'monetarism': {
    'p': 'An economic theory suggesting that variations in the money supply have major influences on national output and price levels.',
    's': 'The political and economic policy of controlling the money supply to stabilize the economy.',
    'q': [
      {'author': 'Milton Friedman', 'work': 'Capitalism and Freedom', 'sentence': 'The core principle of **monetarism** dictates that inflation is always and everywhere a monetary phenomenon.'},
      {'author': 'John Kenneth Galbraith', 'work': 'The Affluent Society', 'sentence': 'Critics of **monetarism** argue that it neglects the human cost of rigid economic controls.'},
      {'author': 'Paul Krugman', 'work': 'The Return of Depression Economics', 'sentence': 'The failures of strict **monetarism** became evident during the sudden financial collapse.'}
    ]
  },
  'monetarist': {
    'p': 'An economist or policymaker who advocates the theory of monetarism, focusing on the money supply.',
    's': 'Relating to the theories and policies that emphasize control of the money supply.',
    'q': [
      {'author': 'Milton Friedman', 'work': 'A Monetary History of the United States', 'sentence': 'As a staunch **monetarist**, he blamed the Federal Reserve for the severity of the Great Depression.'},
      {'author': 'Friedrich Hayek', 'work': 'The Road to Serfdom', 'sentence': 'The **monetarist** approach to curbing inflation requires strict discipline from the central bank.'},
      {'author': 'Joan Robinson', 'work': 'Economic Philosophy', 'sentence': 'The rigid **monetarist** policies often ignore the complexities of human labor markets.'}
    ]
  },
  'monetary': {
    'p': 'Relating to money or currency; pertaining to the coinage or currency of a country.',
    's': 'Involving financial matters, economic value, or the supply of money in an economy.',
    'q': [
      {'author': 'Adam Smith', 'work': 'The Wealth of Nations', 'sentence': 'The intrinsic value of goods is often obscured by their temporary **monetary** price.'},
      {'author': 'Karl Marx', 'work': 'Capital', 'sentence': 'The accumulation of **monetary** wealth drives the relentless engine of capitalist expansion.'},
      {'author': 'John Maynard Keynes', 'work': 'The General Theory of Employment, Interest and Money', 'sentence': 'Effective **monetary** policy is essential for mitigating the devastating cycles of boom and bust.'}
    ]
  },
  'monetisation': {
    'p': 'The process of converting something into money or recognizing it as revenue (chiefly British spelling).',
    's': 'The act of establishing a currency or determining the financial value of an asset.',
    'q': [
      {'author': 'John Maynard Keynes', 'work': 'A Tract on Monetary Reform', 'sentence': 'The rapid **monetisation** of government debt inevitably leads to severe inflationary pressures.'},
      {'author': 'Winston Churchill', 'work': 'The Second World War', 'sentence': 'The **monetisation** of our remaining colonial assets provided crucial funds for the war effort.'},
      {'author': 'Joseph Schumpeter', 'work': 'Capitalism, Socialism and Democracy', 'sentence': 'The **monetisation** of natural resources fundamentally altered the traditional agrarian economy.'}
    ]
  },
  'monetise': {
    'p': 'To convert into or express in the form of money (chiefly British spelling).',
    's': 'To utilize something as a source of profit or to coin money.',
    'q': [
      {'author': 'Karl Marx', 'work': 'Grundrisse', 'sentence': 'The capitalist seeks to **monetise** every aspect of human labor and existence.'},
      {'author': 'Hilaire Belloc', 'work': 'The Servile State', 'sentence': 'They contrived to **monetise** the common lands, stripping the peasants of their ancient rights.'},
      {'author': 'John Ruskin', 'work': 'Unto This Last', 'sentence': 'It is a folly to attempt to **monetise** the intrinsic beauty of art and nature.'}
    ]
  },
  'monetization': {
    'p': 'The process of converting something into money or realizing revenue from it.',
    's': 'The economic mechanism of adopting a specific standard of currency or liquidating assets.',
    'q': [
      {'author': 'Milton Friedman', 'work': 'Free to Choose', 'sentence': 'The forced **monetization** of the deficit eroded the purchasing power of the average citizen.'},
      {'author': 'Thorstein Veblen', 'work': 'The Theory of the Leisure Class', 'sentence': 'The rapid **monetization** of social status transformed traditional honors into mere commodities.'},
      {'author': 'Max Weber', 'work': 'Economy and Society', 'sentence': 'The increasing **monetization** of the economy facilitated the rise of modern bureaucratic capitalism.'}
    ]
  },
  'monetize': {
    'p': 'To convert an asset, debt, or property into money or legal tender.',
    's': 'To generate revenue from a product, service, or abstract concept.',
    'q': [
      {'author': 'Alexander Hamilton', 'work': 'Report on Public Credit', 'sentence': 'We must find a way to **monetize** the national debt to secure the confidence of investors.'},
      {'author': 'Henry George', 'work': 'Progress and Poverty', 'sentence': 'The landlords seek only to **monetize** the value created by the labor of others.'},
      {'author': 'Ayn Rand', 'work': 'Atlas Shrugged', 'sentence': 'The looters passed laws attempting to **monetize** the very intellect of the productive men.'}
    ]
  },
  'money-spinner': {
    'p': 'An enterprise, idea, or product that generates a significant and continuous amount of wealth.',
    's': 'In folklore, a small spider believed to bring financial good luck to whoever finds it on their person.',
    'q': [
      {'author': 'Arthur Conan Doyle', 'work': 'The Sign of the Four', 'sentence': 'The mysterious Indian treasure promised to be a massive **money-spinner** for the greedy major.'},
      {'author': 'Agatha Christie', 'work': 'The Murder of Roger Ackroyd', 'sentence': 'His new invention was touted as a guaranteed **money-spinner** by the eager investors.'},
      {'author': 'P.G. Wodehouse', 'work': 'Right Ho, Jeeves', 'sentence': 'The theatrical production, though dreadful, proved to be an absolute **money-spinner**.'}
    ]
  },
  'money': {
    'p': 'A current medium of exchange in the form of coins and banknotes; coins and banknotes collectively.',
    's': 'Wealth or resources, often considered as a measure of value or means of acquiring goods.',
    'q': [
      {'author': 'William Shakespeare', 'work': 'The Merchant of Venice', 'sentence': 'He lends out **money** gratis, and brings down the rate of usance here with us in Venice.'},
      {'author': 'Jane Austen', 'work': 'Pride and Prejudice', 'sentence': 'A single man in possession of a good fortune must be in want of more **money**.'},
      {'author': 'F. Scott Fitzgerald', 'work': 'The Great Gatsby', 'sentence': 'Her voice is full of **money**, he said suddenly.'}
    ]
  },
  'moneybag': {
    'p': 'A bag used for holding or transporting coins or banknotes.',
    's': 'A wealthy person, often used pejoratively to imply greed or excessive reliance on wealth.',
    'q': [
      {'author': 'Charles Dickens', 'work': 'Hard Times', 'sentence': 'The old banker clutched his **moneybag** as if his very soul resided within its seams.'},
      {'author': 'Karl Marx', 'work': 'Capital', 'sentence': 'The capitalist appears in the market simply as a walking **moneybag**.'},
      {'author': 'Victor Hugo', 'work': 'Les Misérables', 'sentence': 'The corrupt magistrate was little more than a **moneybag** dressed in the robes of justice.'}
    ]
  },
  'moneyed': {
    'p': 'Having much money; wealthy or affluent.',
    's': 'Consisting of or derived from money; associated with the rich and powerful classes.',
    'q': [
      {'author': 'Edith Wharton', 'work': 'The Age of Innocence', 'sentence': 'The old, established families looked down upon the newly **moneyed** industrialists.'},
      {'author': 'Alexander Hamilton', 'work': 'The Federalist Papers', 'sentence': 'The influence of the **moneyed** interests must be balanced against the rights of the common citizens.'},
      {'author': 'Henry James', 'work': 'The Portrait of a Lady', 'sentence': 'She found herself adrift in the shallow waters of highly **moneyed** European society.'}
    ]
  },
  'moneyer': {
    'p': 'Historically, a person officially authorized to mint coins for the state or crown.',
    's': 'One who deals in money; a money changer or banker in medieval times.',
    'q': [
      {'author': 'Geoffrey Chaucer', 'work': 'The Canterbury Tales', 'sentence': 'The royal **moneyer** carefully weighed the silver to ensure the king\'s standard was met.'},
      {'author': 'Walter Scott', 'work': 'Ivanhoe', 'sentence': 'Isaac the Jew was a skilled **moneyer**, providing loans to the desperate nobility.'},
      {'author': 'Thomas Babington Macaulay', 'work': 'The History of England', 'sentence': 'The corrupt **moneyer** was severely punished for clipping the edges of the silver coins.'}
    ]
  },
  'moneygrubber': {
    'p': 'A person who is greedily and relentlessly focused on making money, often to the exclusion of other values.',
    's': 'A miserly or mercenary individual lacking higher principles or generous instincts.',
    'q': [
      {'author': 'Charles Dickens', 'work': 'A Christmas Carol', 'sentence': 'Scrooge was a tight-fisted, squeezing, wrenching, grasping, scraping, clutching old **moneygrubber**.'},
      {'author': 'Mark Twain', 'work': 'The Gilded Age', 'sentence': 'The town was run by a ruthless **moneygrubber** who cared nothing for the welfare of the citizens.'},
      {'author': 'F. Scott Fitzgerald', 'work': 'The Beautiful and Damned', 'sentence': 'He despised his grandfather as a vulgar **moneygrubber** entirely devoid of culture.'}
    ]
  },
  'moneylender': {
    'p': 'A person whose business is lending money to others, typically charging high rates of interest.',
    's': 'A financier or usurer operating outside of conventional banking institutions.',
    'q': [
      {'author': 'William Shakespeare', 'work': 'The Merchant of Venice', 'sentence': 'The desperate merchant sought out the dreaded **moneylender** to secure his ships.'},
      {'author': 'Fyodor Dostoevsky', 'work': 'Crime and Punishment', 'sentence': 'Raskolnikov convinced himself that the old **moneylender** was a parasite deserving of death.'},
      {'author': 'Charles Dickens', 'work': 'Nicholas Nickleby', 'sentence': 'Ralph Nickleby was a heartless **moneylender** who preyed upon the misfortunes of the young.'}
    ]
  },
  'moneyless': {
    'p': 'Completely lacking in money; destitute or penniless.',
    's': 'Occurring or existing without the use of currency or financial exchange.',
    'q': [
      {'author': 'George Orwell', 'work': 'Down and Out in Paris and London', 'sentence': 'To be completely **moneyless** in the city is to experience a terrifying invisibility.'},
      {'author': 'Jack London', 'work': 'The People of the Abyss', 'sentence': 'The **moneyless** vagrants huddled together against the biting chill of the East End night.'},
      {'author': 'Thomas More', 'work': 'Utopia', 'sentence': 'In their ideal society, the citizens lived a completely **moneyless** and communal existence.'}
    ]
  },
  'moneymaker': {
    'p': 'A person or enterprise that is highly successful at generating wealth or profit.',
    's': 'A product, idea, or investment that proves to be exceptionally lucrative.',
    'q': [
      {'author': 'F. Scott Fitzgerald', 'work': 'The Last Tycoon', 'sentence': 'The new studio executive was known throughout Hollywood as a ruthless but brilliant **moneymaker**.'},
      {'author': 'Sinclair Lewis', 'work': 'Babbitt', 'sentence': 'George Babbitt prided himself on being a solid, respectable **moneymaker** in the real estate business.'},
      {'author': 'Arthur Miller', 'work': 'Death of a Salesman', 'sentence': 'Willy believed that charm and a smile were all a true **moneymaker** needed to succeed.'}
    ]
  },
  'moneymaking': {
    'p': 'The action or process of acquiring wealth or generating profit.',
    's': 'Characterized by a primary focus on financial gain or lucrative ventures.',
    'q': [
      {'author': 'Thorstein Veblen', 'work': 'The Theory of Business Enterprise', 'sentence': 'The entire industrial system had been subordinated to the singular goal of **moneymaking**.'},
      {'author': 'Mark Twain', 'work': 'Roughing It', 'sentence': 'The frenzy of the silver rush consumed everyone with wild schemes of instant **moneymaking**.'},
      {'author': 'John Steinbeck', 'work': 'The Grapes of Wrath', 'sentence': 'The bank was a machine for **moneymaking**, blind to the suffering of the displaced farmers.'}
    ]
  },
  'moneyman': {
    'p': 'A person who controls or manages the financial aspects of an enterprise or campaign.',
    's': 'An investor, financier, or backer who provides the necessary capital for a project.',
    'q': [
      {'author': 'Dashiell Hammett', 'work': 'The Maltese Falcon', 'sentence': 'Gutman acted as the prime **moneyman** for the illicit expedition to secure the bird.'},
      {'author': 'F. Scott Fitzgerald', 'work': 'The Great Gatsby', 'sentence': 'Wolfsheim was the shadowy **moneyman** behind many of Gatsby\'s questionable enterprises.'},
      {'author': 'Robert Penn Warren', 'work': 'All the King\'s Men', 'sentence': 'The governor always kept his trusted **moneyman** close to handle the delicate bribes.'}
    ]
  },
  'moneywort': {
    'p': 'A creeping perennial plant (Lysimachia nummularia) in the primrose family, bearing bright yellow flowers and round, coin-like leaves.',
    's': 'An ornamental groundcover or medicinal herb historically used for healing wounds.',
    'q': [
      {'author': 'Nicholas Culpeper', 'work': 'Complete Herbal', 'sentence': 'The juice of the **moneywort** is highly commended for the healing of green wounds.'},
      {'author': 'John Gerard', 'work': 'The Herball or Generall Historie of Plantes', 'sentence': 'The trailing **moneywort** spreads thickly over the damp banks of the shaded river.'},
      {'author': 'Alice Morse Earle', 'work': 'Old Time Gardens', 'sentence': 'We planted **moneywort** along the stone path, admiring its bright, cheerful blossoms.'}
    ]
  },
  'monied': {
    'p': 'Possessing a great deal of money; wealthy (an alternative spelling of moneyed).',
    's': 'Characterized by the presence or influence of wealth and rich individuals.',
    'q': [
      {'author': 'Jane Austen', 'work': 'Sense and Sensibility', 'sentence': 'The arrival of the highly **monied** gentleman caused quite a stir among the hopeful mothers.'},
      {'author': 'Charles Dickens', 'work': 'Bleak House', 'sentence': 'The lawsuit dragged on, draining the resources of both the poor and the highly **monied**.'},
      {'author': 'Alexis de Tocqueville', 'work': 'Democracy in America', 'sentence': 'In the absence of an aristocracy, a new **monied** elite quickly attempts to assert control.'}
    ]
  },
  'moniker': {
    'p': 'A name, nickname, or alias used to identify a person, group, or thing.',
    's': 'A familiar or descriptive label often adopted for public use or anonymity.',
    'q': [
      {'author': 'Jack London', 'work': 'The Road', 'sentence': 'Among the tramps, he was known solely by the colorful **moniker** he had acquired in Chicago.'},
      {'author': 'George Orwell', 'work': 'Down and Out in Paris and London', 'sentence': 'The old beggar had a bizarre **moniker** that nobody knew the origin of.'},
      {'author': 'Raymond Chandler', 'work': 'The Big Sleep', 'sentence': 'The gangster operated under a tough-sounding **moniker** to intimidate the local merchants.'}
    ]
  },
  'monilia': {
    'p': 'A genus of fungi that includes species responsible for various plant diseases, notably brown rot in fruit.',
    's': 'Historically, a medical term for the yeast genus Candida, which causes thrush and other infections.',
    'q': [
      {'author': 'Liberty Hyde Bailey', 'work': 'The Pruning-Book', 'sentence': 'The devastating spread of **monilia** ruined the entire peach crop that wet summer.'},
      {'author': 'Alexander Fleming', 'work': 'Penicillin: Its Practical Application', 'sentence': 'Certain molds effectively inhibit the growth of pathogenic **monilia** cultures in the laboratory.'},
      {'author': 'Edwin John Butler', 'work': 'Fungi and Disease in Plants', 'sentence': 'The spores of the **monilia** fungus winter over in the mummified fruit left on the branches.'}
    ]
  },
  'moniliaceae': {
    'p': 'A family of imperfect fungi (Deuteromycetes) characterized by pale or brightly colored hyphae and spores, including many common molds.',
    's': 'A taxonomic grouping of fungi that reproduce asexually and often act as plant pathogens or saprotrophs.',
    'q': [
      {'author': 'Anton de Bary', 'work': 'Comparative Morphology and Biology of the Fungi', 'sentence': 'The family **moniliaceae** encompasses a vast array of common molds found on decaying vegetation.'},
      {'author': 'Pier Andrea Saccardo', 'work': 'Sylloge Fungorum', 'sentence': 'The classification of **moniliaceae** relies heavily on the structure of their conidiophores.'},
      {'author': 'George Francis Atkinson', 'work': 'Studies of American Fungi', 'sentence': 'We isolated a distinct member of the **moniliaceae** from the diseased roots of the specimen.'}
    ]
  }
}

for word, info in data.items():
    write_curated_note('mon', word, info['p'], info['s'], info['q'])
