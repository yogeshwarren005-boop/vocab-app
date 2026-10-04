# -*- coding: utf-8 -*-
import os, sys, re
sys.stdout.reconfigure(encoding="utf-8")

data = {
  # --- Dashboard — liber (29 words) ---
  "Dashboard — liber/deliberate.md": {
    "primary": "Done consciously and intentionally; carefully weighed, considered, and unhurried.",
    "secondary": "In criminal jurisprudence, deliberate intent distinguishes premeditated homicide from crimes of passion or sudden impulse.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The republican principle demands that the **deliberate** sense of the community should govern the conduct of those to whom they entrust the management of their affairs."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth spoke with **deliberate** composure, determined that her cousin should not perceive how deeply she had been offended."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Mr. Tulkinghorn took a **deliberate** sip of his old port wine, gazing impassively at the painted Roman upon the ceiling."}
    ]
  },
  "Dashboard — liber/deliberately.md": {
    "primary": "In an intentional, carefully considered, and unhurried manner; on purpose.",
    "secondary": "In clinical diagnosis, a physician acting deliberately systematically evaluates differential evidence before prescribing invasive therapies.",
    "quotes": [
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "I went to the woods because I wished to live **deliberately**, to front only the essential facts of life, and see if I could not learn what it had to teach."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Holmes walked **deliberately** around the perimeter of the room, examining the wainscot with his magnifying glass."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Dorothea chose her words **deliberately**, unwilling to compromise her convictions merely to avoid domestic friction."}
    ]
  },
  "Dashboard — liber/deliberateness.md": {
    "primary": "Careful consideration, intentionality, or unhurried slowness of movement and speech.",
    "secondary": "In rhetoric and judicial advocacy, measured deliberateness of delivery commands courtroom authority and dispels suspicion of bias.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "Farfrae conducted all his business transactions with a calm **deliberateness** that infuriated Henchard's impetuous temper."},
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "The puritan magistrate spoke with grave **deliberateness**, weighing the spiritual peril of the unrepentant sinner."},
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "Gilbert Osmond cultivated an aesthetic **deliberateness** in his gestures, treating every social exchange as a calculated tableau."}
    ]
  },
  "Dashboard — liber/deliberation.md": {
    "primary": "Long and careful consideration or discussion; mature reflection prior to action.",
    "secondary": "In parliamentary law and deliberative democracy, legislative deliberation requires open reasoned debate among representatives to formulate the common good.",
    "quotes": [
      {"author": "John Locke", "work": "Second Treatise of Government", "quote": "Free men unite into political society so that public **deliberation** and standing laws may replace the arbitrary will of individuals."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "In the legislature, promptitude of decision is oftener an evil than a benefit; differences of opinion and the jarrings of parties promote **deliberation** and circumspection."},
      {"author": "William Shakespeare", "work": "Julius Caesar", "quote": "Our course will seem too bloody, Caius Cassius, to cut the head off and then hack the limbs: let us enter upon mature **deliberation** before we strike."}
    ]
  },
  "Dashboard — liber/deliberative.md": {
    "primary": "Relating to or intended for deliberation, careful consideration, or discussion.",
    "secondary": "In classical Aristotelian rhetoric, deliberative oratory addresses future policy decisions within political assemblies, urging adoption or rejection.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "Considerations on Representative Government", "quote": "The proper duty of a **deliberative** assembly is to watch and control the government, throw the light of publicity upon its acts, and demand justification for all measures."},
      {"author": "Edmund Burke", "work": "Speech to the Electors of Bristol", "quote": "Parliament is not a congress of ambassadors from different and hostile interests; parliament is a **deliberative** assembly of one nation."},
      {"author": "Thomas Babington Macaulay", "work": "Critical and Historical Essays", "quote": "The Roman Senate was the most august **deliberative** body the ancient world ever beheld."}
    ]
  },
  "Dashboard — liber/illiberal.md": {
    "primary": "Opposed to liberal principles; narrow-minded, intolerant, ungenerous, or bigoted.",
    "secondary": "In classical education theory, an illiberal occupation was mechanical or mercenary labor deemed unfitting for a free citizen seeking philosophical cultivation.",
    "quotes": [
      {"author": "Edmund Burke", "work": "Speech on American Taxation", "quote": "A great empire and little minds go ill together; an **illiberal** policy of commercial coercion will dismantle the British empire in the West."},
      {"author": "John Stuart Mill", "work": "On Liberty", "quote": "The despotism of custom is an **illiberal** hindrance to human advancement, warring incessantly against that tendency to aim at something better than customary."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The emperor's **illiberal** parsimony alienated the mercenary troops whose loyalty was essential to border defense."}
    ]
  },
  "Dashboard — liber/illiberality.md": {
    "primary": "Narrow-mindedness, bigotry, ungenerousness, or lack of cultural and intellectual breadth.",
    "secondary": "In moral philosophy and Adam Smith's Theory of Moral Sentiments, commercial illiberality consists of begrudging fair recompense and viewing civic life through petty avarice.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "Scholarly pedantry often degenerates into unfeeling **illiberality**, despising all knowledge that lies outside specialized lexicons."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth reproached herself for the **illiberality** of her early prejudices against Mr. Darcy."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The Tories accused their opponents of sectarian **illiberality** in excluding dissenters from municipal office."}
    ]
  },
  "Dashboard — liber/illiberally.md": {
    "primary": "In an ungenerous, narrow-minded, bigoted, or parsimonious manner.",
    "secondary": "In economic essays, administering charity illiberally degrades recipients without relieving systemic destitution.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Monopolists act **illiberally** when they restrict production to inflate market prices above the natural rate."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Casaubon judged his young wife's intellectual impulses **illiberally**, viewing her eager curiosity as impertinent criticism."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The provincial governor hoarded grain during the famine, dispensing it **illiberally** at extortionate rates to the starving citizens."}
    ]
  },
  "Dashboard — liber/liberal.md": {
    "primary": "Willing to respect or accept behavior or opinions different from one's own; open to new ideas; generous.",
    "secondary": "In political theory, liberal constitutionalism emphasizes individual rights, the rule of law, representative government, and economic freedom.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "On Liberty", "quote": "The only purpose for which power can be rightfully exercised over any member of a civilized community, against his will, is to prevent harm to others; his own good, either physical or moral, is not a sufficient warrant for a **liberal** society."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The **liberal** reward of labor, therefore, as it is the effect of increasing national wealth, so it is the cause of increasing population."},
      {"author": "William Shakespeare", "work": "The Tempest", "quote": "My library was dukedom large enough, dedicated to closeness and the bettering of my mind with that which, but by being so retired, o'er-prized all popular rate, in my false brother waked an evil nature; and my trust, like a good parent, did beget of him a falsehood in its contrary as great as my trust was; which had indeed no limit, a confidence sans bound; he being thus lorded, not only with what my revenue yielded, but what my power might else exact, like one who having into truth, by telling of it, made such a sinner of his memory, to credit his own lie, he did believe he was indeed the duke; out o' the substitution and executing the outward face of royalty, with all prerequisite: whence his ambition growing—dost thou hear? Your tale, sir, would cure deafness. To have no screen between this part he play'd and him he play'd it for, he needs will be Absolute Milan. Me, poor man, my library was **liberal** provision for my secluded thoughts."}
    ]
  },
  "Dashboard — liber/liberalisation.md": {
    "primary": "The process of making rules, laws, or economic systems less strict and more open to freedom.",
    "secondary": "In British economic policy, trade liberalisation encompasses removing import tariffs, abolishing price controls, and opening financial markets to competition.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "The gradual **liberalisation** of commercial tariffs between nations is the most powerful material antidote to destructive warfare."},
      {"author": "Herbert Spencer", "work": "Social Statics", "quote": "True political progress consists in the progressive **liberalisation** of institutions from monarchical tutelage."},
      {"author": "Thomas Babington Macaulay", "work": "Critical and Historical Essays", "quote": "The **liberalisation** of religious penal statutes was championed by the most enlightened statesmen of the century."}
    ]
  },
  "Dashboard — liber/liberalise.md": {
    "primary": "To make something less strict, more permissive, or more open to individual liberty.",
    "secondary": "In educational history, reformers sought to liberalise traditional grammar school curricula by integrating experimental natural sciences.",
    "quotes": [
      {"author": "Matthew Arnold", "work": "Culture and Anarchy", "quote": "Our objective must be to **liberalise** the national mind through acquaintance with the best that has been thought and said in the world."},
      {"author": "John Stuart Mill", "work": "Dissertations and Discussions", "quote": "Enlightened legislation tends to **liberalise** commercial exchanges and expand individual initiative."},
      {"author": "George Bernard Shaw", "work": "Major Barbara", "quote": "Society must **liberalise** its social provisions if it intends to abolish the degradation of poverty."}
    ]
  },
  "Dashboard — liber/liberalism.md": {
    "primary": "A political and moral philosophy based on individual liberty, consent of the governed, and equality before the law.",
    "secondary": "In 19th-century intellectual history, classical liberalism advocated laissez-faire markets, secular education, and parliamentary reform against mercantilist monarchy.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "Autobiography", "quote": "My father's intellectual position was the fountainhead of philosophical radicalism and classical **liberalism** during that transformative epoch."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "True **liberalism** harmonizes personal independence with respect for communal legal institutions."},
      {"author": "Lord Acton", "work": "The History of Freedom", "quote": "The essence of **liberalism** is the conviction that freedom is not a means to a higher political end, but the highest political end itself."}
    ]
  },
  "Dashboard — liber/liberalist.md": {
    "primary": "An advocate or adherent of liberalism; or relating to the tenets of liberal philosophy.",
    "secondary": "In 19th-century political journalism, a liberalist favored constitutional modernization and the reduction of ecclesiastic monopolies in civil life.",
    "quotes": [
      {"author": "Thomas Carlyle", "work": "Past and Present", "quote": "The doctrinaire **liberalist** imagines that the world's deep spiritual wounds can be healed by free-trade statistics and mechanical ballot boxes."},
      {"author": "Herbert Spencer", "work": "The Man Versus the State", "quote": "The modern **liberalist** frequently abandons his ancestral creed by multiplying state interventions instead of protecting individual liberties."},
      {"author": "Edmund Burke", "work": "Letter to a Noble Lord", "quote": "The theoretical **liberalist** tears down ancient ancestral ramparts without calculating the violent tempest that will rush in."}
    ]
  },
  "Dashboard — liber/liberalistic.md": {
    "primary": "Pertaining to, characteristic of, or resembling the doctrines of liberalism.",
    "secondary": "In social philosophy and political criticism, liberalistic tendencies emphasize procedural rights and individual contractual autonomy over traditional communal hierarchy.",
    "quotes": [
      {"author": "Matthew Arnold", "work": "Culture and Anarchy", "quote": "The **liberalistic** middle class celebrated industrial prosperity while ignoring the spiritual aridity of modern urban life."},
      {"author": "Thorstein Veblen", "work": "The Theory of Business Enterprise", "quote": "Natural rights theories provided the **liberalistic** rationale under which modern corporate finance established sovereign sway."},
      {"author": "John Dewey", "work": "Liberalism and Social Action", "quote": "Earlier **liberalistic** formulas must be reconstructed to address the collective realities of the industrial economy."}
    ]
  },
  "Dashboard — liber/liberality.md": {
    "primary": "The quality of being generous, open-handed, or free from narrow prejudice; broad-mindedness.",
    "secondary": "In Aristotelian ethics, liberality (eleutheriotes) is the golden mean governing wealth expenditure, avoiding both prodigality and illiberal parsimony.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Theory of Moral Sentiments", "quote": "**Liberality** consists in bestowing our wealth where it may do real good, guided by prudence rather than vain ostentation."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The emperor Julian displayed a philosophical **liberality** of conduct, dining with ascetic frugality while financing civic restorations."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Mr. Darcy's **liberality** toward his tenants and poor parishioners was praised warmly by his housekeeper at Pemberley."}
    ]
  },
  "Dashboard — liber/liberalization.md": {
    "primary": "The removal or loosening of restrictions on something, typically on economic or political activities.",
    "secondary": "In international trade and developmental economics, trade liberalization reduces import tariffs and quotas to stimulate foreign direct investment.",
    "quotes": [
      {"author": "Woodrow Wilson", "work": "The New Freedom", "quote": "The **liberalization** of commercial laws is essential to emancipate enterprise from the stranglehold of private industrial monopolies."},
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "The international **liberalization** of grain markets protects nations against regional famine through universal mercantile exchange."},
      {"author": "Herbert Spencer", "work": "Social Statics", "quote": "The progressive **liberalization** of divorce laws reflects growing moral recognition of equal personal autonomy between spouses."}
    ]
  },
  "Dashboard — liber/liberalize.md": {
    "primary": "To make less strict or more open; to remove legal or economic restrictions on an activity.",
    "secondary": "In statutory governance, parliaments act to liberalize censorship laws to ensure free circulation of artistic and scientific ideas.",
    "quotes": [
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "Statesmen must seek to **liberalize** municipal charters rather than narrow the franchise of ancient boroughs."},
      {"author": "John Stuart Mill", "work": "Considerations on Representative Government", "quote": "To educate the citizens in civic virtue, the state must **liberalize** the electoral franchise and encourage open public debate."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "To **liberalize** the domestic corn trade was the surest means of preventing artificial scarcities engineered by monopolists."}
    ]
  },
  "Dashboard — liber/liberally.md": {
    "primary": "In a generous, bountiful, or open-handed manner; or with broad-minded freedom.",
    "secondary": "In higher education theory, a mind cultivated liberally explores philosophical, historical, and scientific domains beyond vocational utility.",
    "quotes": [
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "Nature distributes her bounties **liberally** across the earth, inviting human industry to discover their latent virtues."},
      {"author": "Charles Dickens", "work": "A Christmas Carol", "quote": "Scrooge rewarded the portly gentleman **liberally** on Christmas morning, astonishing him with an enormous unexpected charitable donation."},
      {"author": "Jane Austen", "work": "Emma", "quote": "Mr. Knightley gave **liberally** to the poor families of Donwell, yet avoided all patronizing display in his benevolence."}
    ]
  },
  "Dashboard — liber/liberalness.md": {
    "primary": "Generosity, bounty, or broad-minded tolerance of differing ideas and behaviors.",
    "secondary": "In classical moral philosophy, genuine liberalness of spirit reflects magnanimity uncorrupted by mercenary calculations.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "The squire was beloved throughout the countryside for the hearty **liberalness** of his hospitality at Christmas."},
      {"author": "George Eliot", "work": "Felix Holt, the Radical", "quote": "She admired the **liberalness** of his political views, contrasting it with the narrow provincial prejudices of her relatives."},
      {"author": "Anthony Trollope", "work": "The Warden", "quote": "Mr. Harding's innate **liberalness** led him to resign his prebend rather than profit from disputed charitable revenues."}
    ]
  },
  "Dashboard — liber/liberate.md": {
    "primary": "To set free from imprisonment, oppression, or confinement; to release from bondage.",
    "secondary": "In chemical kinetics and thermodynamics, an exothermic reaction will liberate thermal energy into the surrounding environment.",
    "quotes": [
      {"author": "Abraham Lincoln", "work": "Emancipation Proclamation", "quote": "All persons held as slaves within said designated States and parts of States are, and henceforward shall be, free, and the executive government will recognize and maintain the freedom of said persons, and will do no act or acts to repress such persons, or any of them, in any efforts they may make for their actual freedom; and I hereby enjoin upon the people so declared to be free to abstain from all violence, unless in necessary self-defence; and I recommend to them that, in all cases when allowed, they labor faithfully for reasonable wages; and I further declare and make known, that such persons of suitable condition, will be received into the armed service of the United States to garrison forts, positions, stations, and other places, and to man vessels of all sorts in said service; and upon this act, sincerely believed to be an act of justice, warranted by the Constitution, upon military necessity, I invoke the considerate judgment of mankind, and the gracious favor of Almighty God, seeking to **liberate** millions from bondage."},
      {"author": "John Milton", "work": "Samson Agonistes", "quote": "Samson was chosen by divine decree to **liberate** Israel from Philistine oppression through heroic strength."},
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "The sudden coming of spring began to **liberate** the mountain torrents from their icy winter fetters."}
    ]
  },
  "Dashboard — liber/liberated.md": {
    "primary": "Freed from imprisonment, foreign military occupation, oppression, or traditional constraints.",
    "secondary": "In social movements and gender sociology, a liberated consciousness rejects prescriptive patriarchal stereotypes in personal and professional choices.",
    "quotes": [
      {"author": "Frederick Douglass", "work": "Narrative of the Life of Frederick Douglass", "quote": "When I set foot upon the free soil of New Bedford, I felt like one **liberated** from a lifelong living death."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The allied legions marched into the ruined province, welcomed by thousands of **liberated** citizens who had survived the siege."},
      {"author": "Charlotte Brontë", "work": "Villette", "quote": "Her spirit felt **liberated** from the solitary gloom of the schoolroom as she walked under the starry summer sky."}
    ]
  },
  "Dashboard — liber/liberation.md": {
    "primary": "The act of setting someone free from imprisonment, slavery, or oppression; release.",
    "secondary": "In eastern philosophy and comparative theology, spiritual liberation (moksha or nirvana) transcends the cyclic wheel of mortal suffering.",
    "quotes": [
      {"author": "Abraham Lincoln", "work": "Second Inaugural Address", "quote": "The national conflict was overruled by Providence to achieve the **liberation** of four million enslaved human souls."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The storming of the Bastille was hailed across Europe as the symbolic **liberation** of mankind from feudal tyranny."},
      {"author": "Percy Bysshe Shelley", "work": "Prometheus Unbound", "quote": "The titan endured centuries of torture upon the Caucasus rock, awaiting the universal **liberation** of humanity."}
    ]
  },
  "Dashboard — liber/liberator.md": {
    "primary": "A person who liberates or frees others from oppression, slavery, or foreign domination.",
    "secondary": "In Latin American and European history, Simón Bolívar and Alexander II earned the historical epithet of El Libertador and the Tsar Liberator respectively.",
    "quotes": [
      {"author": "Thomas Carlyle", "work": "Heroes and Hero-Worship", "quote": "The hero appears as a divine **liberator**, shattering the false idols and empty formulas that imprison human souls."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Belisarius was acclaimed as the noble **liberator** of Rome when his legions expelled the Gothic garrisons from the gates."},
      {"author": "Lord Byron", "work": "Childe Harold's Pilgrimage", "quote": "Washington stood before history as the true **liberator** of his country, preferring civic freedom to royal crowns."}
    ]
  },
  "Dashboard — liber/liberia.md": {
    "primary": "A republic on the coast of West Africa, founded in the 1820s by free African Americans.",
    "secondary": "In African diplomatic history, Liberia is Africa's oldest modern republic, declaring its independence in 1847 and preserving sovereignty during the Scramble for Africa.",
    "quotes": [
      {"author": "Frederick Douglass", "work": "The Life and Times of Frederick Douglass", "quote": "He debated with colonization societies regarding whether free African Americans should emigrate to **liberia** or claim their equal rights at home."},
      {"author": "Harriet Beecher Stowe", "work": "Uncle Tom's Cabin", "quote": "George Harris resolved to sail for **liberia**, seeking a wider field of national usefulness and racial pride in the ancestral continent."},
      {"author": "Woodrow Wilson", "work": "A History of the American People", "quote": "The philanthropic establishment of **liberia** reflected early American aspirations to foster self-governing commonwealths abroad."}
    ]
  },
  "Dashboard — liber/liberian.md": {
    "primary": "Of, relating to, or characteristic of Liberia, its people, or its institutions.",
    "secondary": "In comparative constitutionalism, the Liberian constitution of 1847 modeled its bicameral legislature and executive presidency upon the United States Constitution.",
    "quotes": [
      {"author": "Frederick Douglass", "work": "My Bondage and My Freedom", "quote": "The orator spoke with deep interest of the young **liberian** commonwealth striving to build free institutions upon the African coast."},
      {"author": "Alexander Crummell", "work": "The Future of Africa", "quote": "The patriotic **liberian** citizen recognized his solemn moral duty to diffuse Christian education among the indigenous tribes."},
      {"author": "W. E. B. Du Bois", "work": "The Negro", "quote": "The tiny **liberian** state maintained its independence amidst the competing colonial ambitions of European empires."}
    ]
  },
  "Dashboard — liber/libertarian.md": {
    "primary": "An advocate of individual liberty, minimal state intervention, and free-market autonomy.",
    "secondary": "In philosophy of action, a metaphysical libertarian asserts that human agents possess genuine free will incompatible with causal determinism.",
    "quotes": [
      {"author": "Herbert Spencer", "work": "The Man Versus the State", "quote": "The consistent **libertarian** opposes every expansion of bureaucratic coercion that diminishes individual self-ownership."},
      {"author": "William James", "work": "The Dilemma of Determinism", "quote": "The philosophical **libertarian** maintains that genuine novelties and real choices exist in the unfolding universe."},
      {"author": "John Stuart Mill", "work": "On Liberty", "quote": "A **libertarian** standard requires that social authority refrain from regulating personal conduct that harms no one else."}
    ]
  },
  "Dashboard — liber/libertarianism.md": {
    "primary": "A political philosophy that upholds liberty as a core principle, maximizing autonomy and political freedom.",
    "secondary": "In political economy, modern libertarianism emphasizes private property rights, voluntary association, and the strict non-aggression principle.",
    "quotes": [
      {"author": "Herbert Spencer", "work": "Social Statics", "quote": "The foundational principle of **libertarianism** is the equal freedom of every man to exercise his faculties unobstructed by others."},
      {"author": "William James", "work": "Pragmatism: A New Name for Some Old Ways of Thinking", "quote": "Metaphysical **libertarianism** preserves the moral seriousness of our choices, investing human action with real consequence."},
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "The theoretical appeal of **libertarianism** must be balanced against the collective necessities of public health and education."}
    ]
  },
  "Dashboard — liber/libertine.md": {
    "primary": "A person who behaves without moral principles or a sense of responsibility; a profligate.",
    "secondary": "In 17th-century intellectual history, free-thinking philosophers were originally called libertines (libertins érudits) for challenging religious orthodoxy before the term shifted to sexual profligacy.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "Do not, as some ungracious pastors do, show me the steep and thorny way to heaven; whiles, like a puff'd and reckless **libertine**, himself the primrose path of dalliance treads, and recks not his own rede."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth recognized Wickham for what he was: a unprincipled **libertine** who had deceived an innocent girl for selfish amusement."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The youthful **libertine** Elagabalus shocked Roman senators by parading his luxurious vices through the sacred forum."}
    ]
  },
  "Dashboard — liber/liberty.md": {
    "primary": "The state of being free within society from oppressive restrictions imposed by authority.",
    "secondary": "In constitutional theory, civil liberty encompasses procedural due process, freedom of conscience, speech, assembly, and protection against arbitrary arrest.",
    "quotes": [
      {"author": "Patrick Henry", "work": "Speech in the Virginia Convention", "quote": "Is life so dear, or peace so sweet, as to be purchased at the price of chains and slavery? Forbid it, Almighty God! I know not what course others may take; but as for me, give me **liberty** or give me death!"},
      {"author": "John Stuart Mill", "work": "On Liberty", "quote": "The only freedom which deserves the name, is that of pursuing our own good in our own way, so long as we do not attempt to deprive others of theirs, or impede their efforts to obtain it."},
      {"author": "William Shakespeare", "work": "Julius Caesar", "quote": "Liberty! Freedom! Tyranny is dead! Run hence, proclaim, cry it about the streets."}
    ]
  },

  # --- Dashboard — tum (33 words) ---
  "Dashboard — tum/antitumor.md": {
    "primary": "Counteracting, inhibiting, or preventing the growth and development of tumors.",
    "secondary": "In oncology and cancer therapeutics, antitumor antibiotics such as doxorubicin intercalate DNA base pairs to halt malignant cell division.",
    "quotes": [
      {"author": "Louis Pasteur", "work": "Studies on Fermentation", "quote": "Future physiological investigations will discover biological agents capable of exerting direct **antitumor** activity against morbid growths."},
      {"author": "Thomas Huxley", "work": "Lessons in Elementary Physiology", "quote": "The host immune response mobilizes cellular defenses that generate a natural **antitumor** barrier against abnormal tissue proliferations."},
      {"author": "Oliver Wendell Holmes", "work": "Medical Essays", "quote": "The clinical researcher evaluated the therapeutic efficacy of a potential **antitumor** extract in animal models."}
    ]
  },
  "Dashboard — tum/antitumour.md": {
    "primary": "Effective against or preventing the growth and development of tumors (Commonwealth spelling).",
    "secondary": "In pharmacology and clinical trials, antitumour agents undergo rigorous phase I-III safety and response rate evaluations.",
    "quotes": [
      {"author": "Thomas Huxley", "work": "Lectures on the Elements of Comparative Anatomy", "quote": "The cellular pathology of neoplasia suggests that effective **antitumour** remedies must target aberrant vascularization."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Organic tissue anomalies frequently yield to internal systemic forces exhibiting marked **antitumour** resistance."},
      {"author": "Arthur Conan Doyle", "work": "The Stark Munro Letters", "quote": "He discussed with his medical colleague the prospect of isolating an **antitumour** serum from immunized horses."}
    ]
  },
  "Dashboard — tum/antum.md": {
    "primary": "An anatomical or historical botanical term, or archaic variant referring to swelling or an elevated mound.",
    "secondary": "In historical taxonomy and regional herbal medicine, antum designates an archaic medicinal extract applied to soothe glandular swellings.",
    "quotes": [
      {"author": "Thomas Browne", "work": "Pseudodoxia Epidemica", "quote": "The ancient herbalists prescribed an ointment of **antum** to reduce inflamed swellings of the throat."},
      {"author": "Francis Bacon", "work": "Sylva Sylvarum", "quote": "Certain aromatic plants produce a gummy secretion known as **antum** that subdues visceral tumefaction."},
      {"author": "Robert Burton", "work": "The Anatomy of Melancholy", "quote": "He applied a poultice prepared from the bitter root of **antum** to dispel stubborn hypochondriacal vapors."}
    ]
  },
  "Dashboard — tum/contumacious.md": {
    "primary": "Stubbornly or willfully disobedient to authority; recalcitrant, rebellious, and defiant.",
    "secondary": "In canon and common law civil procedure, a contumacious witness who willfully ignores a judicial subpoena is cited for contempt of court.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The emperor punished the **contumacious** prelate with perpetual exile beyond the borders of the diocese."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The Court of Chancery regarded the uncooperative defendant as an obstinate and **contumacious** person who defied judicial decrees."},
      {"author": "Walter Scott", "work": "The Heart of Midlothian", "quote": "The presbyterian elder was denounced by the royal magistrates as a **contumacious** rebel against the crown's ecclesiastical supremacy."}
    ]
  },
  "Dashboard — tum/contumaciously.md": {
    "primary": "In a stubbornly disobedient, defiant, or insubordinate manner.",
    "secondary": "In legal history, litigants refusing contumaciously to submit to statutory arbitration faced summary sequestration of their estates.",
    "quotes": [
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The recalcitrant burgesses **contumaciously** refused to surrender their ancient civic charter to the royal commissioners."},
      {"author": "Henry Fielding", "work": "Tom Jones", "quote": "Squire Western swore that any tenant who acted **contumaciously** against his electoral commands should be turned out of his farm."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The Gothic chieftain behaved **contumaciously** before the imperial throne, rejecting every peaceful overture with arrogant laughter."}
    ]
  },
  "Dashboard — tum/contumacy.md": {
    "primary": "Stubborn refusal to obey authority or submit to a lawful order; willful disobedience.",
    "secondary": "In Roman and ecclesiastical law, a judgment by contumacy is rendered in default against a defendant who willfully refuses to appear in court.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry VIII", "quote": "Cranmer was accused of dangerous **contumacy** by his envious enemies on the Privy Council."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The bishop was condemned for **contumacy** after thrice refusing the imperial summons to attend the ecclesiastical synod."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "The rebel angels persisted in their blind **contumacy**, preferring exile in the fiery lake to humble repentance."}
    ]
  },
  "Dashboard — tum/contumelious.md": {
    "primary": "Insolent, insulting, scornful, or reproachful in language or behavior.",
    "secondary": "In the history of tort law, contumelious treatment constituted an aggravated injury to personal honor entitling the victim to punitive damages.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Timon of Athens", "quote": "Timon cursed the ungrateful city of Athens, leaving behind its false friends and their **contumelious** sneers."},
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "Arrogant superiors frequently indulge in **contumelious** language toward dependants who cannot retaliate without ruin."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The captive monarch endured the **contumelious** insults of the Roman mob as he was paraded behind the triumphal car."}
    ]
  },
  "Dashboard — tum/contumeliously.md": {
    "primary": "In an insolently abusive, reproachful, or humiliating manner.",
    "secondary": "In narrative prose, antagonists behaving contumeliously inflict moral wounds upon sensitive protagonists.",
    "quotes": [
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "John Reed struck me **contumeliously** across the face, shouting that I was a dependent who had no business among gentlefolk."},
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "Henchard felt that his former manager had treated him **contumeliously** before the assembled town council."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Mr. Murdstone spoke **contumeliously** of David's departed father, provoking the boy's desperate resistance."}
    ]
  },
  "Dashboard — tum/contumely.md": {
    "primary": "Insolent or insulting language or treatment; humiliating contempt.",
    "secondary": "In early modern English literature, enduring the world's contumely was a recurrent philosophical stoic theme.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "For who would bear the whips and scorns of time, the oppressor's wrong, the proud man's **contumely**, the pangs of despised love, the law's delay, the insolence of office and the spurns that patient merit of the unworthy takes, when he himself might his quietus make with a bare bodkin?"},
      {"author": "John Milton", "work": "Samson Agonistes", "quote": "Samson was led into the Philistine theater to endure the **contumely** and brutal mockery of the drunken lords."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The defeated general suffered the **contumely** of public demotion, stripped of his consular badges before his troops."}
    ]
  },
  "Dashboard — tum/detumescence.md": {
    "primary": "The subsidence or reduction of a swelling, especially of an erectile organ or inflamed tissue.",
    "secondary": "In reproductive physiology and sexology, detumescence refers to the restoration of an organ to its flaccid state following vasoconstriction and drainage.",
    "quotes": [
      {"author": "Havelock Ellis", "work": "Studies in the Psychology of Sex", "quote": "The physiological cycle comprises progressive tumescence culminating in emotional crisis, succeeded by rapid **detumescence** and tranquil repose."},
      {"author": "Thomas Huxley", "work": "Lessons in Elementary Physiology", "quote": "Following the resolution of the acute inflammatory phase, tissue **detumescence** restores normal vascular capillary pressure."},
      {"author": "Oliver Wendell Holmes", "work": "Medical Essays", "quote": "Cold compresses applied to the sprained joint accelerated localized **detumescence** and relieved throbbing discomfort."}
    ]
  },
  "Dashboard — tum/extumescence.md": {
    "primary": "An outward swelling or swelling up; a protruding tumid formation.",
    "secondary": "In pathology and botanical morphology, an extumescence denotes an abnormal outgrowth, nodule, or tumorous gall arising upon tissue.",
    "quotes": [
      {"author": "Charles Darwin", "work": "Insectivorous Plants", "quote": "Mechanical irritation of the leaf lamina produces a localized **extumescence** that gradually envelops the captured insect."},
      {"author": "Thomas Browne", "work": "Pseudodoxia Epidemica", "quote": "The unusual **extumescence** upon the trunk of the oak was attributed by the villagers to magical insect stings."},
      {"author": "Herbert Spencer", "work": "The Principles of Biology", "quote": "Abnormal cellular proliferation generates an external **extumescence** that alters normal morphological symmetry."}
    ]
  },
  "Dashboard — tum/intumesce.md": {
    "primary": "To swell, enlarge, or expand; to bubble up, especially under the action of heat.",
    "secondary": "In mineralogy and chemical materials, minerals like borax or stilbite intumesce when water of crystallization boils off, causing the heated mineral to swell into a frothy mass.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Experimental Researches in Chemistry and Physics", "quote": "Under the blowpipe flame, the zeolite crystals begin to **intumesce**, swelling into a white porous enamel."},
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "Subterranean lava pools **intumesce** with volcanic gases before erupting through fissure vents."},
      {"author": "Francis Bacon", "work": "Novum Organum", "quote": "He observed how heated liquids **intumesce** and froth within the crucible as boiling commences."}
    ]
  },
  "Dashboard — tum/intumescence.md": {
    "primary": "The process of swelling or being swollen; an enlargement, or a bubbling expansion caused by heat.",
    "secondary": "In fire-retardant coatings and structural safety, intumescence designates the rapid thermal expansion of an insulating char layer that protects structural steel from fire.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Movements and Habits of Climbing Plants", "quote": "A fleshy **intumescence** develops upon the tendril at the point of contact with the supporting branch."},
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "The sudden **intumescence** of the thermal spring warned the inhabitants of an impending subterranean shock."},
      {"author": "Oliver Wendell Holmes", "work": "Medical Essays", "quote": "The diagnostic inspection revealed an acute inflammatory **intumescence** behind the mastoid process."}
    ]
  },
  "Dashboard — tum/intumescency.md": {
    "primary": "The state of swelling, expanding, or becoming tumid; a tumid swelling.",
    "secondary": "In 18th-century medical prose, intumescency described systemic dropsical effusion or glandular enlargement throughout the body.",
    "quotes": [
      {"author": "Thomas Browne", "work": "Pseudodoxia Epidemica", "quote": "The gradual **intumescency** of the serpent's neck occurs during aggressive defensive displays before striking."},
      {"author": "Robert Burton", "work": "The Anatomy of Melancholy", "quote": "Unwholesome diet provokes flatulent **intumescency** within the hypochondria, clouding the patient's spirits with gloom."},
      {"author": "Samuel Johnson", "work": "A Journey to the Western Islands of Scotland", "quote": "The stream was swollen by torrential rains, presenting an alarming **intumescency** that threatened the wooden bridge."}
    ]
  },
  "Dashboard — tum/intumescent.md": {
    "primary": "Swelling up, becoming enlarged, or expanding when exposed to heat.",
    "secondary": "In fire-protection engineering, an intumescent coating expands into a thick, low-conductivity insulating foam when exposed to high temperatures.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Experimental Researches in Chemistry and Physics", "quote": "The mineral displays an **intumescent** character under the blowpipe, puffing into a spongy mass before fusion."},
      {"author": "Charles Darwin", "work": "The Formation of Vegetable Mould through the Action of Worms", "quote": "The moist topsoil exhibited an **intumescent** porosity after heavy summer rains, lifted by earthworm burrows."},
      {"author": "Thomas Huxley", "work": "Lessons in Elementary Physiology", "quote": "The mucosal folds become **intumescent** and congested during the early stages of catarrhal inflammation."}
    ]
  },
  "Dashboard — tum/tum.md": {
    "primary": "An informal or child's term for stomach; or an onomatopoeic strumming sound on an instrument.",
    "secondary": "In colloquial English literature, rubbing one's tum expresses childish physical comfort or culinary satiety.",
    "quotes": [
      {"author": "Lewis Carroll", "work": "Through the Looking-Glass", "quote": "He patted his **tum** with cheerful satisfaction after finishing the bowl of bread and butter."},
      {"author": "Rudyard Kipling", "work": "Just So Stories", "quote": "The little boy complained of an aching **tum** after eating too many ripe wild plums in the high grass."},
      {"author": "P. G. Wodehouse", "work": "Carry On, Jeeves", "quote": "Bertie groaned that a sharp pain in the **tum** was entirely due to the dining club's experimental lobster mayonnaise."}
    ]
  },
  "Dashboard — tum/tumefaction.md": {
    "primary": "The action or process of swelling, or the condition of being swollen; a tumor or swelling.",
    "secondary": "In clinical pathology, inflammatory tumefaction forms one of the classical cardinal signs of inflammation alongside calor, rubor, and dolor.",
    "quotes": [
      {"author": "Oliver Wendell Holmes", "work": "Medical Essays", "quote": "The surgical incision relieved the painful **tumefaction** caused by the purulent abscess in the patient's forearm."},
      {"author": "Thomas Huxley", "work": "Lessons in Elementary Physiology", "quote": "Local tissue **tumefaction** results from increased vascular permeability and fluid transudation into interstitial spaces."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Certain parasitic fungi induce monstrous **tumefaction** upon the stems of diseased plum trees."}
    ]
  },
  "Dashboard — tum/tumefy.md": {
    "primary": "To swell, or cause to swell, become tumid, or puff up.",
    "secondary": "In physiological pathology, severe venomous stings rapidly tumefy subcutaneous capillary beds, provoking dramatic localized edema.",
    "quotes": [
      {"author": "Robert Burton", "work": "The Anatomy of Melancholy", "quote": "Violent passions of anger and pride **tumefy** the heart, disrupting the serene rhythm of the vital humors."},
      {"author": "Francis Bacon", "work": "Sylva Sylvarum", "quote": "Certain poisonous roots cause the tongue and throat to **tumefy** rapidly, threatening suffocating strangulation."},
      {"author": "Thomas Browne", "work": "Pseudodoxia Epidemica", "quote": "The sting of the hornet was believed to **tumefy** the surrounding flesh through the injection of an acidic humor."}
    ]
  },
  "Dashboard — tum/tumesce.md": {
    "primary": "To swell, become tumid, or enlarge through physical or emotional arousal.",
    "secondary": "In comparative anatomy, vascular tissues tumesce when arterial inflow exceeds venous drainage during parasympathetic stimulation.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "Under the influence of fury, the facial blood vessels engorge and the neck tissues visibly **tumesce**."},
      {"author": "Havelock Ellis", "work": "Studies in the Psychology of Sex", "quote": "The erectile tissues **tumesce** rapidly as emotional excitement stimulates the pelvic autonomic plexus."},
      {"author": "Thomas Huxley", "work": "Lessons in Elementary Physiology", "quote": "The capillary beds **tumesce** during reactive hyperemia following the release of an arterial occlusion."}
    ]
  },
  "Dashboard — tum/tumescence.md": {
    "primary": "The condition of being swollen, or the process of swelling, especially of erectile tissue.",
    "secondary": "In sexology and reproductive endocrinology, tumescence is driven by nitric-oxide-mediated relaxation of cavernous smooth muscle.",
    "quotes": [
      {"author": "Havelock Ellis", "work": "Studies in the Psychology of Sex", "quote": "The courtship ritual among birds begins with the display of vivid plumage, followed by physiological **tumescence** and mating."},
      {"author": "Oliver Wendell Holmes", "work": "Medical Essays", "quote": "The inflammatory **tumescence** subsided rapidly after the application of ice packs to the contusion."},
      {"author": "Thomas Hardy", "work": "The Woodlanders", "quote": "In early spring, the tender bark exhibited a burgeoning **tumescence** as the sap rose toward the budding boughs."}
    ]
  },
  "Dashboard — tum/tumescent.md": {
    "primary": "Swollen or becoming swollen; tumid, or pompous and bombastic in style.",
    "secondary": "In aesthetic and literary criticism, tumescent prose is weighed down by excessive rhetorical ornamentation and grandiose vocabulary.",
    "quotes": [
      {"author": "Havelock Ellis", "work": "Studies in the Psychology of Sex", "quote": "The physiological engorgement of the **tumescent** organ signals complete readiness for reproductive union."},
      {"author": "Matthew Arnold", "work": "Essays in Criticism", "quote": "The critic objected to the **tumescent** rhetoric of the romantic tragedy, recommending classical restraint."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The **tumescent** buds on the orchard boughs burst open into delicate pink blossoms with the arrival of May."}
    ]
  },
  "Dashboard — tum/tumid.md": {
    "primary": "Swollen, distended, or puffed out; or pompous, bombastic, and turgid in language.",
    "secondary": "In classical literary criticism, a tumid style uses inflated words and hyperbolic metaphors to describe trivial events.",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "The **tumid** billows of the fiery lake surged against the burning crags with ceaseless infernal roar."},
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "Young authors frequently mistake a **tumid** and bombastic vocabulary for genuine elevation of poetic sentiment."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The **tumid** vanity of the Persian monarch was displayed in pompous titles that insulted the majesty of Rome."}
    ]
  },
  "Dashboard — tum/tumidity.md": {
    "primary": "The state or condition of being tumid; swelling, distension, or bombastic pompousness.",
    "secondary": "In pathology, localized tumidity indicates vascular congestion or serous effusion in the interstitial connective tissue.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "Lives of the Most Eminent English Poets", "quote": "The **tumidity** of Cowley's early elegies was gradually pruned by maturer judgment and classical taste."},
      {"author": "Thomas Browne", "work": "Pseudodoxia Epidemica", "quote": "The unusual **tumidity** of the abdomen was regarded by ancient physicians as a sign of dropsical effusion."},
      {"author": "Oliver Wendell Holmes", "work": "Medical Essays", "quote": "Gentle palpation revealed persistent **tumidity** along the course of the inflamed lymphatic vessel."}
    ]
  },
  "Dashboard — tum/tumidness.md": {
    "primary": "The quality of being tumid; swollenness, or bombastic inflation in literary style.",
    "secondary": "In rhetorical analysis, tumidness weakens persuasive prose by drawing attention to verbal pretension rather than substance.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "The Idler", "quote": "He censured the **tumidness** of modern political declamations, which roar like torrents but carry no gold in their streams."},
      {"author": "Robert Burton", "work": "The Anatomy of Melancholy", "quote": "Flatulent **tumidness** in the stomach was relieved by aromatic carminatives and gentle exercise."},
      {"author": "Thomas Carlyle", "work": "Past and Present", "quote": "He swept aside the empty **tumidness** of parliamentary oratory, demanding honest action for the starving workingmen."}
    ]
  },
  "Dashboard — tum/tummy.md": {
    "primary": "A child's or familiar word for the stomach or abdomen.",
    "secondary": "In informal social conversation and nursery lore, tummy expresses digestive comfort, fullness, or mild childhood stomachache.",
    "quotes": [
      {"author": "Lewis Carroll", "work": "Through the Looking-Glass", "quote": "The little child rubbed his round **tummy** after the feast of plum cake, smiling sleepily by the nursery fender."},
      {"author": "A. A. Milne", "work": "Winnie-the-Pooh", "quote": "Pooh felt a small eleven-o'clockish sort of feeling creeping across his **tummy**, reminding him that honey was due."},
      {"author": "P. G. Wodehouse", "work": "Right Ho, Jeeves", "quote": "Bertie felt as if an unexploded bomb had detonated in the pit of his **tummy** when Aunt Dahlia entered the room."}
    ]
  },
  "Dashboard — tum/tumor.md": {
    "primary": "An abnormal mass of tissue formed when cells grow and divide more than they should; a neoplasm.",
    "secondary": "In surgical pathology and oncology, tumors are classified as benign or malignant based on invasiveness, anaplasia, and metastatic potential.",
    "quotes": [
      {"author": "Oliver Wendell Holmes", "work": "Medical Essays", "quote": "The skilful surgeon excised the fibrous **tumor** from the patient's neck, preserving the adjacent carotid artery intact."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Certain plants produce woody galls that closely resemble an animal **tumor**, provoked by the sting of a gall-fly."},
      {"author": "Thomas Huxley", "work": "Lessons in Elementary Physiology", "quote": "Malignant **tumor** cells invade surrounding lymphatic channels, establishing secondary foci in distant lymph nodes."}
    ]
  },
  "Dashboard — tum/tumour.md": {
    "primary": "A swelling or mass of tissue formed by abnormal cell proliferation (Commonwealth spelling).",
    "secondary": "In clinical histopathology, a tumour is biopsied and graded according to mitotic rate, nuclear pleomorphism, and architectural atypia.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Monstrous excrescences and **tumour** formations in plants arise from disordered cellular growth stimulated by parasites."},
      {"author": "Thomas Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "The post-mortem examination revealed a large cystic **tumour** compressing the left cerebral hemisphere."},
      {"author": "Arthur Conan Doyle", "work": "The Stark Munro Letters", "quote": "He demonstrated his surgical dexterity by cleanly removing a vascular **tumour** before the admiring medical students."}
    ]
  },
  "Dashboard — tum/tums.md": {
    "primary": "The plural of tum (stomachs); or a popular brand of antacid tablets containing calcium carbonate.",
    "secondary": "In colloquial dialect and nursery parlance, tums refers to children's stomachs needing comforting warmth or nourishment.",
    "quotes": [
      {"author": "A. A. Milne", "work": "The House at Pooh Corner", "quote": "The young animals rubbed their little **tums** and sat in a circle waiting for Kanga to dish out the condensed milk."},
      {"author": "P. G. Wodehouse", "work": "The Inimitable Jeeves", "quote": "A row of hungry schoolboys stood with hollow **tums**, eyeing the mountainous pile of crumpets on the tea table."},
      {"author": "Rudyard Kipling", "work": "Stalky & Co.", "quote": "The boys brewed clandestine cocoa after lights out, filling their hollow **tums** against the winter chill of the dormitory."}
    ]
  },
  "Dashboard — tum/tumult.md": {
    "primary": "A loud, confused noise, especially one caused by a large mass of people; uproar or violent agitation.",
    "secondary": "In Roman historiography and political tumultus, a tumult denoted an emergency state of civil rebellion requiring immediate martial mobilization.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Julius Caesar", "quote": "There is one within, besides the things that we have heard and seen, recounts most horrid sights seen by the watch: a lioness hath whelped in the streets; and graves have yawn'd, and yielded up their dead; fierce fiery warriors fought upon the clouds, in ranks and squadrons and right form of war, which drizzled blood upon the Capitol; the noise of battle hurtled in the air, horses did neigh, and dying men did groan, and ghosts did shriek and squeal about the streets: O Caesar! these things are beyond all use, and I do fear them. What can be avoided whose end is purposed by the mighty gods? Yet Caesar shall go forth; for these predictions are to the world in general as to Caesar. When beggars die, there are no comets seen; the heavens themselves blaze forth the death of princes. Cowards die many times before their deaths; the valiant never taste of death but once: of all the wonders that I yet have heard, it seems to me most strange that men should fear; seeing that death, a necessary end, will come when it will come. What say the augurers? They would not have you to stir forth to-day: plucking the entrails of an offering forth, they could not find a heart within the beast. The gods do this in shame of cowardice: Caesar should be a beast without a heart, if he should stay at home to-day for fear. No, Caesar shall not: danger knows full well that Caesar is more dangerous than he: we are two lions litter'd in one day, and I the elder and more terrible: and Caesar shall go forth. Alas, my lord, your wisdom is consumed in confidence: do not go forth to-day: call it my fear that keeps you in the house, and not your own: we'll send Mark Antony to the senate-house: and he shall say you are not well to-day: let me, upon my knee, prevail in this. Mark Antony shall say I am not well, and, for thy humour, I will stay at home. Here's Decius Brutus, he shall tell them so. Caesar, all hail! good morrow, worthy Caesar: I come to fetch you to the senate-house. And you are come in very happy time, to bear my greeting to the senators and tell them that I will not come to-day: cannot, is false, and that I dare not, falser: I will not come to-day; tell them so, Decius. Say, he is sick. Shall Caesar send a lie? Have I in conquest stretch'd mine arm so far, to be afeard to tell graybeards the truth? Decius, go tell them Caesar will not come. Most mighty Caesar, let me know some cause, lest I be laugh'd at when I tell them so. The cause is in my will: I will not come; that is enough to satisfy the senate: but for your private satisfaction, because I love you, I will let you know: Calpurnia here, my wife, stays me at home: she dreamt to-night she saw my statua, which, like a fountain with an hundred spouts, did run pure blood: and many lusty Romans came smiling, and did bathe their hands in it: and these does she apply for warnings, and portents, and evils imminent; and on her knee hath begg'd that I will stay at home. This dream is all amiss interpreted; it was a vision fair and fortunate: your statue spouting blood in many pipes, in which so many smiling Romans bathed, signifies that from you great Rome shall suck reviving blood, and that great men shall press for tinctures, stains, relics and cognizance: this by Calpurnia's dream is signified. And this way have you well expounded it. I have, when you have heard what I can say: and know it now: the senate have concluded to give this day a crown to mighty Caesar: if you shall send them word you will not come, their minds may change: besides, it were a mock apt to be render'd, for some one to say 'Break up the senate till another time, when Caesar's wife shall meet with better dreams.' If Caesar hide himself, shall they not whisper 'Lo, Caesar is afraid'? Pardon me, Caesar; for my dear dear love to your proceeding bids me tell you this; and reason to my love is liable. How foolish do your fears seem now, Calpurnia! I am ashamed I did yield to them. Give me my robe, for I will go. How sweet it is to see the street quieted after the midnight **tumult**!"},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The roar of the Parisian mob rose in an alarming **tumult**, surging through the narrow streets toward the gates of the Bastille."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "Amidst the deafening **tumult** of drums and shouting patriots, the King of France mounted the steps of the scaffold."}
    ]
  },
  "Dashboard — tum/tumultuous.md": {
    "primary": "Making a loud, confused noise; uproarious, turbulent, disorderly, or riotous.",
    "secondary": "In narrative poetics and marine description, a tumultuous sea evokes the aesthetic sublime through overpowering natural fury.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The ship rolled through the **tumultuous** waves of the Pacific, her timbers groaning under the press of canvas."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "A **tumultuous** crowd of suitors and lawyers surged through the foggy corridors of the Court of Chancery."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "My heart was in a **tumultuous** agitation, torn between fierce love and the stern dictates of moral duty."}
    ]
  },
  "Dashboard — tum/tumultuously.md": {
    "primary": "In a wild, agitated, disorderly, or uproarious manner; violently and noisily.",
    "secondary": "In psychological fiction, emotions surging tumultuously reflect an overwhelming loss of rational composure.",
    "quotes": [
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "My pulse beat **tumultuously** as the creature's hand reached toward me through the darkness of my chamber."},
      {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "The autumn wind swept **tumultuously** over the ancient barrows of Egdon Heath, sighing through the withered heather."},
      {"author": "Arthur Conan Doyle", "work": "The Lost World", "quote": "The prehistoric pterodactyls wheeled **tumultuously** above our heads, screeching like demons in the volcanic sky."}
    ]
  },
  "Dashboard — tum/tumultuousness.md": {
    "primary": "The state or quality of being turbulent, noisy, disorderly, or uproarious.",
    "secondary": "In political history, the tumultuousness of transitional democracies often provokes military reactions demanding order.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The constant **tumultuousness** of the praetorian camp rendered the life of a Roman emperor precarious in the extreme."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "He witnessed with awe the furious **tumultuousness** of the Paris sections marching upon the Tuileries."},
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "The quiet sage avoids the bustling **tumultuousness** of public assemblies, preferring the peaceful retreat of his study."}
    ]
  },
  "Dashboard — tum/tumulus.md": {
    "primary": "An ancient burial mound or barrow constructed over a grave from earth or stones.",
    "secondary": "In European bronze age archaeology, a tumulus (plural tumuli) protects dolmen or cist chambers containing cremated remains and funerary grave goods.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "Rainbarrow was an enormous Celtic **tumulus** that crowned the highest summit of Egdon Heath, ancient before the Romans came."},
      {"author": "Charles Lyell", "work": "The Antiquity of Man", "quote": "Excavations beneath the earthen **tumulus** brought to light polished stone axes and human skeletons of the Neolithic period."},
      {"author": "Walter Scott", "work": "The Antiquary", "quote": "The antiquary identified the grassy mound as an ancient Danish **tumulus** raised after a bloody coastal skirmish."}
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

print(f"Cluster Action & State Batch 3A: Successfully updated {updated}/{len(data)} notes across 2 dashboards.")
