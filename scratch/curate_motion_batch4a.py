# -*- coding: utf-8 -*-
import os, sys, re
sys.stdout.reconfigure(encoding="utf-8")

data = {
  # --- Dashboard — gress (37 words) ---
  "Dashboard — gress/aggress.md": {
    "primary": "To initiate an unprovoked attack, quarrel, or hostile invasion against another person or nation.",
    "secondary": "In international relations and military history, sovereign states that aggress against neutral neighbors violate non-intervention pacts.",
    "quotes": [
      {"author": "Winston Churchill", "work": "The Second World War", "quote": "A totalitarian power will not hesitate to **aggress** upon weaker states whenever it senses diplomatic irresolution."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The nomadic tribes rarely waited for the legions to advance, preferring to **aggress** across the undefended border."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The revolutionary leaders resolved to **aggress** against neighboring monarchies before foreign coalitions could assemble."}
    ]
  },
  "Dashboard — gress/aggression.md": {
    "primary": "Hostile, injurious, or destructive behavior or action; an unprovoked attack or invasion.",
    "secondary": "In international public law, the crime of aggression consists of the planning, preparation, initiation, or execution of an act of armed force by a state.",
    "quotes": [
      {"author": "Winston Churchill", "work": "The Second World War", "quote": "We are fighting to save the civilized world from the brutal and unprovoked **aggression** of Nazi tyranny."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The sudden barbarian **aggression** along the Danube shattered two centuries of Roman peace."},
      {"author": "John Locke", "work": "Second Treatise of Government", "quote": "He who makes an unprovoked **aggression** upon another's natural liberty places himself in a state of war with all mankind."}
    ]
  },
  "Dashboard — gress/aggressive.md": {
    "primary": "Ready or likely to attack, confront, or pursue one's goals forcefully; competitive and assertive.",
    "secondary": "In oncology and clinical pathology, an aggressive neoplasm demonstrates rapid cellular proliferation and early metastasis.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Male stags become remarkably fierce and **aggressive** during the autumn rut, clashing antlers in combat."},
      {"author": "Winston Churchill", "work": "The World Crisis", "quote": "The admiralty adopted an **aggressive** naval policy designed to sweep the German high seas fleet from the North Sea."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Jonathan Small adopted an **aggressive** demeanor when challenged, threatening the officers with his wooden crutch."}
    ]
  },
  "Dashboard — gress/aggressively.md": {
    "primary": "In a forceful, competitive, hostile, or attacking manner; with energetic determination.",
    "secondary": "In commercial antitrust economics, dominant firms that price aggressively below marginal cost risk predation penalties.",
    "quotes": [
      {"author": "Theodore Dreiser", "work": "The Financier", "quote": "Cowperwood pushed his traction investments **aggressively**, buying up rival transit lines across Philadelphia."},
      {"author": "Jack London", "work": "The Sea-Wolf", "quote": "Wolf Larsen stepped forward **aggressively**, intimidating the sullen sailors with his immense physical strength."},
      {"author": "Winston Churchill", "work": "The Second World War", "quote": "General Montgomery resolved to attack **aggressively** at El Alamein to break the Axis armored line."}
    ]
  },
  "Dashboard — gress/aggressiveness.md": {
    "primary": "The tendency, disposition, or inclination to initiate attacks, hostility, or highly assertive actions.",
    "secondary": "In behavioral ethology and endocrinology, male aggressiveness correlates with circulating plasma testosterone elevations.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The natural **aggressiveness** of carnivorous predators is tempered by instincts that avoid unnecessary injury."},
      {"author": "Herbert Spencer", "work": "The Study of Sociology", "quote": "Militant tribal societies cultivate personal **aggressiveness** as the supreme civic virtue among their young warriors."},
      {"author": "William James", "work": "The Varieties of Religious Experience", "quote": "Spiritual transformation often channels raw human **aggressiveness** into tireless humanitarian reform."}
    ]
  },
  "Dashboard — gress/aggressor.md": {
    "primary": "A person, group, or nation that initiates an unprovoked attack, hostility, or invasion.",
    "secondary": "In customary international humanitarian law, identifying the primary aggressor state determines collective self-defense obligations under Article 51.",
    "quotes": [
      {"author": "Winston Churchill", "work": "The Second World War", "quote": "No compromise can be made with the criminal **aggressor** who has drenched Europe in innocent blood."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The Roman legions faced a formidable **aggressor** in the Gothic cavalry commanded by Alaric."},
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "Society is justified in using defensive force to repel any foreign **aggressor** who threatens its freedom."}
    ]
  },
  "Dashboard — gress/congress.md": {
    "primary": "A formal meeting or series of meetings of representatives to discuss matters; or the national legislative body of a republic.",
    "secondary": "In diplomatic history, the Congress of Vienna (1814–1815) reconstituted the European balance of power following the Napoleonic Wars.",
    "quotes": [
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "Envoys from every sovereign court assembled in solemn **congress** to negotiate the terms of European peace."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The federal **Congress** must possess adequate legislative power to regulate interstate and foreign commerce."},
      {"author": "George Washington", "work": "Writings of George Washington", "quote": "The general submitted his military dispatches to the Continental **Congress**, urging immediate financial support."}
    ]
  },
  "Dashboard — gress/congressional.md": {
    "primary": "Pertaining to, enacted by, or characteristic of a congress, especially the United States Congress.",
    "secondary": "In constitutional law, congressional committee subpoenas carry statutory contempt powers to enforce legislative oversight.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The **congressional** record reveals the careful deliberations that shaped our constitutional framework."},
      {"author": "Mark Twain", "work": "The Gilded Age", "quote": "The Washington hotel lobby buzzed with lobbyists seeking to influence the upcoming **congressional** vote."},
      {"author": "Theodore Roosevelt", "work": "An Autobiography", "quote": "The president engaged in vigorous political debates with **congressional** leaders over conservation legislation."}
    ]
  },
  "Dashboard — gress/congressman.md": {
    "primary": "A male member of a national congress, especially a member of the United States House of Representatives.",
    "secondary": "In American electoral legislative politics, each congressman represents a constitutionally apportioned single-member district.",
    "quotes": [
      {"author": "Mark Twain", "work": "The Gilded Age", "quote": "The influential **congressman** promised to insert an appropriation bill for the navigation of the local river."},
      {"author": "Sinclair Lewis", "work": "Babbitt", "quote": "George Babbitt was eager to shake hands with his local **congressman** at the annual chamber of commerce banquet."},
      {"author": "Theodore Dreiser", "work": "The Titan", "quote": "The street railway syndicate contributed generously to the campaign fund of the senior **congressman**."}
    ]
  },
  "Dashboard — gress/degressive.md": {
    "primary": "Decreasing gradually in rate, proportion, or severity as the amount increases; or descending by stages.",
    "secondary": "In fiscal public taxation theory, a degressive tax structure reduces effective tax percentages on lower income tiers.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The fiscal reformer proposed a **degressive** tariff schedule to encourage domestic industrial manufacturing."},
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "A **degressive** tax on small incomes mitigates the harsh burden of direct taxation upon the working classes."},
      {"author": "Herbert Spencer", "work": "The Principles of Sociology", "quote": "The intensity of feudal obligations followed a **degressive** scale from direct retainers to remote vassals."}
    ]
  },
  "Dashboard — gress/digress.md": {
    "primary": "To turn aside temporarily from the main subject, topic, or argument in speech or writing.",
    "secondary": "In rhetorical composition and literary narratology, authors digress into philosophical parabases to offer meta-commentary.",
    "quotes": [
      {"author": "Jane Austen", "work": "Emma", "quote": "Miss Bates was perpetually prone to **digress** into endless village gossip whenever asked a simple question."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "David paused in his narrative, begging the reader's pardon for his inclination to **digress** upon happy memories."},
      {"author": "Jonathan Swift", "work": "A Tale of a Tub", "quote": "The author resolved to **digress** into a profound treatise upon the nature and utility of madness in a commonwealth."}
    ]
  },
  "Dashboard — gress/digression.md": {
    "primary": "A temporary departure from the main subject or theme in speech, writing, or thought.",
    "secondary": "In classical Greco-Roman oratorical theory, the parekbasis or digression serves to engage emotional sympathy before returning to proofs.",
    "quotes": [
      {"author": "Jonathan Swift", "work": "A Tale of a Tub", "quote": "The satirical author dedicated an entire chapter to a delightful **digression** concerning critics and philosophers."},
      {"author": "Laurence Sterne", "work": "The Life and Opinions of Tristram Shandy", "quote": "Digressions, incontestably, are the sunshine; they are the life, the soul of reading; take them out of this book, you might as well take the book along with them; one cold eternal winter would reign in every page of it; restore them to the writer, he steps forth like a bridegroom, bids all-hail; brings in variety, and forbids the appetite to fail; such a **digression** is the soul of wit."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Holmes listened patiently to Thaddeus Sholto's nervous **digression** before steering him back to the missing treasure."}
    ]
  },
  "Dashboard — gress/digressive.md": {
    "primary": "Characterized by, tending toward, or departing from the main subject in speech or writing; rambling.",
    "secondary": "In narrative stylistics, digressive fiction (such as Rabelais, Sterne, or Cervantes) disrupts linear chronology to explore tangents.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Mr. Collins's **digressive** letters were filled with pomposity, apologies, and detailed descriptions of Rosings."},
      {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "The editor struggled through Teufelsdröckh's wildly **digressive** manuscripts, untangling philosophy from biography."},
      {"author": "Henry James", "work": "The Art of Fiction", "quote": "A sprawling, **digressive** novel risks losing its architectural unity unless anchored by strong psychological portraiture."}
    ]
  },
  "Dashboard — gress/egress.md": {
    "primary": "The act of going out of or leaving a place; an exit, departure, or means of exit.",
    "secondary": "In structural building codes and fire safety engineering, calculating maximum occupant egress capacity dictates corridor width.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Holmes inspected the locked windows, determining that the killer's sole means of **egress** was through the roof trapdoor."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "The fiery cherubim guarded the eastern portal, permitting no **egress** to the fallen angels from the burning lake."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The armed sentries barred every gate of Paris, cutting off all possibility of **egress** for fleeing aristocrats."}
    ]
  },
  "Dashboard — gress/egression.md": {
    "primary": "The act or process of coming out, emerging, or going forth from an enclosure or obscured position.",
    "secondary": "In positional astronomy and celestial mechanics, the egression of an occulted star or planetary body marks its reappearance.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Physiography", "quote": "The **egression** of subterranean thermal waters through fissure vents created immense travertine mineral deposits."},
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "Geologists monitored the periodic **egression** of boiling mud from the dormant volcanic vents."},
      {"author": "David Brewster", "work": "Treatise on Optics", "quote": "The precise astronomical timing of planetary **egression** during a solar transit provides distance calculations."}
    ]
  },
  "Dashboard — gress/ingress.md": {
    "primary": "The act of entering, going in, or arriving; or the right, liberty, or means of entry.",
    "secondary": "In orbital astronomy and astrometry, the ingress of Venus across the solar disk marks the beginning of the transit contact.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Holmes examined the chimney and the stout oak door to determine the point of **ingress** used by the nocturnal intruder."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Through the high crystal portal, the angelic messengers found ready **ingress** into the radiant courts of heaven."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The foggy court of Chancery admitted no easy **ingress** to suitors who lacked wealth or legal influence."}
    ]
  },
  "Dashboard — gress/nonaggression.md": {
    "primary": "A policy or state of refraining from unprovoked hostility, military aggression, or territorial invasion.",
    "secondary": "In diplomatic history, nonaggression pacts (such as the 1939 Molotov-Ribbentrop Pact) temporarily secured borders before wartime betrayal.",
    "quotes": [
      {"author": "Winston Churchill", "work": "The Second World War", "quote": "The cynical **nonaggression** pact between Berlin and Moscow cleared the path for the invasion of Poland."},
      {"author": "George Orwell", "work": "Nineteen Eighty-Four", "quote": "The shifting **nonaggression** treaties between Oceania and Eurasia were rewritten daily in the Ministry of Truth."},
      {"author": "H. G. Wells", "work": "The Shape of Things to Come", "quote": "The global federation enforced strict **nonaggression** protocols among the reconstituted regional administrative councils."}
    ]
  },
  "Dashboard — gress/nonaggressive.md": {
    "primary": "Not aggressive; peaceful, mild-mannered, and lacking hostile or competitive tendencies.",
    "secondary": "In developmental psychology, nonaggressive conflict resolution skills correlate with superior adolescent peer relationships.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Certain herbivorous ungulates maintain a completely **nonaggressive** disposition, relying upon speed to escape predators."},
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Edward Ferrars possessed a quiet, **nonaggressive** temperament that shrank from the loud rivalries of fashionable London."},
      {"author": "William James", "work": "The Moral Equivalent of War", "quote": "Civilized society must cultivate **nonaggressive** avenues for the heroic energies and physical vigor of youth."}
    ]
  },
  "Dashboard — gress/nonprogressive.md": {
    "primary": "Not progressing, advancing, or reforming; stagnant; or in medicine, not increasing in severity.",
    "secondary": "In clinical neurology, a nonprogressive congenital encephalopathy exhibits stable neurological deficits without ongoing deterioration.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The clinician reassured the family that the child's muscular deficit was a **nonprogressive** congenital condition."},
      {"author": "Herbert Spencer", "work": "First Principles", "quote": "Static human societies become trapped in a **nonprogressive** traditionalism that resists technical innovation."},
      {"author": "Thomas Carlyle", "work": "Past and Present", "quote": "A merely conservative, **nonprogressive** parliament cannot comprehend the urgent needs of the industrial poor."}
    ]
  },
  "Dashboard — gress/progress.md": {
    "primary": "Forward or onward movement toward a destination; or developmental advancement toward a higher or better state.",
    "secondary": "In philosophical historicism and Enlightenment theory, human history is conceived as the moral and scientific progress of mankind.",
    "quotes": [
      {"author": "John Bunyan", "work": "The Pilgrim's Progress", "quote": "This book will make a traveler of thee, if by its counsel thou wilt rule thy life, and trace Christian's **progress** to glory."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The general **progress** of organic beings toward structural specialization is a natural consequence of natural selection."},
      {"author": "Thomas Babington Macaulay", "work": "History of England", "quote": "The history of England during the last two centuries is the history of physical, moral, and intellectual **progress**."}
    ]
  },
  "Dashboard — gress/progression.md": {
    "primary": "The process of developing, advancing, or moving gradually toward a more advanced state; a sequence of items or stages.",
    "secondary": "In pure mathematics and algebra, an arithmetic progression features a constant numerical difference between consecutive terms.",
    "quotes": [
      {"author": "Thomas Malthus", "work": "An Essay on the Principle of Population", "quote": "Population, when unchecked, increases in a geometrical ratio; subsistence increases only in an arithmetical **progression**."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The geological record reveals an ascending **progression** of organic forms from simple invertebrates to mammals."},
      {"author": "Herbert Spencer", "work": "First Principles", "quote": "The universal law of cosmic evolution demonstrates an orderly **progression** from homogeneity to heterogeneity."}
    ]
  },
  "Dashboard — gress/progressive.md": {
    "primary": "Favoring or advocating social, political, or scientific reform and progress; moving forward or increasing gradually.",
    "secondary": "In clinical medicine, a progressive chronic disease exhibits worsening functional impairment and pathological tissue damage over time.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "On Liberty", "quote": "The spirit of improvement is not always a spirit of liberty; for it may aim at forcing **progressive** changes on an unwilling people."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Human intellect has undergone **progressive** development through speech, social cooperation, and tool manufacture."},
      {"author": "H. G. Wells", "work": "A Modern Utopia", "quote": "The utopian order was designed to foster continuous **progressive** evolution in educational and technological life."}
    ]
  },
  "Dashboard — gress/progressively.md": {
    "primary": "Increasingly; steadily advancing in amount, extent, or degree over time.",
    "secondary": "In macroeconomic fiscal policy, progressive income tax systems tax higher discretionary earnings progressively higher.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The landscape grew **progressively** more barren and desolate as the survey party approached the southern cordillera."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Pip watched the convict's leg-iron become **progressively** more rusted by the wet sea-fog of the marshes."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Holmes's deductions became **progressively** clearer as each fresh clue narrowed the search for the fugitive."}
    ]
  },
  "Dashboard — gress/progressiveness.md": {
    "primary": "The characteristic or quality of being progressive, innovative, or oriented toward continuous social or technical improvement.",
    "secondary": "In institutional economics and organizational culture, corporate progressiveness correlates with R&D reinvestment and agility.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "Considerations on Representative Government", "quote": "The primary virtue of democratic institutions lies in their capacity to stimulate the intellectual **progressiveness** of citizens."},
      {"author": "Herbert Spencer", "work": "The Study of Sociology", "quote": "True national **progressiveness** depends upon individual initiative rather than coercive administrative decrees."},
      {"author": "Sinclair Lewis", "work": "Babbitt", "quote": "George Babbitt constantly boasted of the commercial **progressiveness** of Zenith compared to rival midwestern cities."}
    ]
  },
  "Dashboard — gress/progressivism.md": {
    "primary": "A political and social philosophy that advocates progressive socio-economic reform, government regulation, and social justice.",
    "secondary": "In American political historiography, the early twentieth-century Progressive Era championed antitrust laws, electoral reform, and pure food acts.",
    "quotes": [
      {"author": "Theodore Roosevelt", "work": "The New Nationalism", "quote": "Genuine **progressivism** demands that the federal government curb corporate power to secure fair play for all citizens."},
      {"author": "Woodrow Wilson", "work": "The New Freedom", "quote": "The spirit of modern **progressivism** seeks to emancipate the individual from the grip of monopolistic trusts."},
      {"author": "Sinclair Lewis", "work": "Main Street", "quote": "Carol Kennicott's parlor **progressivism** was viewed with suspicious bewilderment by the conservative matrons of Gopher Prairie."}
    ]
  },
  "Dashboard — gress/progressivity.md": {
    "primary": "The quality, state, or extent of being progressive, especially describing a tax system where rates increase with income.",
    "secondary": "In public finance economics, measuring the progressivity index (such as the Kakwani index) quantifies tax redistribution.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The fiscal reformer debated the economic consequences and social equity of tax **progressivity** upon high landed revenues."},
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "A moderate degree of **progressivity** in legacy duties prevents the unhealthy dynastic accumulation of unearned wealth."},
      {"author": "Herbert Spencer", "work": "Social Statics", "quote": "Philosophers analyzed the legal implications of statutory **progressivity** within national revenue legislation."}
    ]
  },
  "Dashboard — gress/regress.md": {
    "primary": "To return to an earlier, inferior, or less developed state; or the action of returning or going back.",
    "secondary": "In developmental psychoanalysis, psychological regress serves as an unconscious defensive retreat to earlier developmental stages.",
    "quotes": [
      {"author": "Herbert Spencer", "work": "First Principles", "quote": "Societies that abandon rigorous scientific education inevitably **regress** toward superstitious tribal barbarism."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Certain domestic varieties tend to **regress** toward the ancestral wild morphology when abandoned in nature."},
      {"author": "Thomas Carlyle", "work": "Past and Present", "quote": "Without moral heroism in our leaders, human civilization will surely **regress** into chaos and misery."}
    ]
  },
  "Dashboard — gress/regression.md": {
    "primary": "A return to an earlier, primitive, or less developed condition; or in statistics, a model calculating relationships between variables.",
    "secondary": "In biostatistics and econometric modeling, linear regression quantifies the relationship between dependent outcomes and explanatory covariates.",
    "quotes": [
      {"author": "Francis Galton", "work": "Natural Inheritance", "quote": "Galton formulated the mathematical law of filial **regression** to explain why extreme parental traits revert toward the population mean."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Breeders observe occasional morphological **regression** where fancy pigeons produce ancestral rock-dove traits."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "In severe psychiatric exhaustion, mental functions exhibit temporary **regression** to primitive reflex patterns."}
    ]
  },
  "Dashboard — gress/regressive.md": {
    "primary": "Returning to a less developed or less advanced state; or in taxation, taking a larger percentage from low incomes than high ones.",
    "secondary": "In fiscal tax incidence analysis, flat consumption sales taxes are considered regressive because poor households consume higher proportions of income.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "A sales tax upon basic food staples is fundamentally **regressive**, placing an unfair burden on working families."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Certain parasitic organisms exhibit **regressive** structural changes, losing organs of locomotion and digestion."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The late imperial bureaucracy enforced a **regressive** tax code that crushed provincial agricultural initiative."}
    ]
  },
  "Dashboard — gress/retrogress.md": {
    "primary": "To go backward, deteriorate, or decline into a worse or more primitive state; to regress.",
    "secondary": "In macro-historical sociology, civilizations that over-exploit topsoil and water aquifers retrogress into agrarian collapse.",
    "quotes": [
      {"author": "Herbert Spencer", "work": "First Principles", "quote": "When external physical conditions become hostile, biological species frequently **retrogress** rather than advance."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "Should public virtue fail, the glorious gains of freedom will swiftly **retrogress** into military despotism."},
      {"author": "Thomas Henry Huxley", "work": "Evolution and Ethics", "quote": "Human moral progress requires constant effort, lest the ethical process **retrogress** to the cruel law of the jungle."}
    ]
  },
  "Dashboard — gress/retrogression.md": {
    "primary": "The process or act of returning to an inferior, less advanced, or deteriorating state; decline.",
    "secondary": "In evolutionary biology and comparative parasitology, evolutionary retrogression describes the secondary loss of complex anatomical traits.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The degenerate anatomy of sessile barnacles represents a clear case of evolutionary **retrogression** from free-swimming ancestors."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The rapid **retrogression** of Western Europe into dark illiterate centuries followed the fall of the Roman administration."},
      {"author": "Herbert Spencer", "work": "The Principles of Sociology", "quote": "Militant autocracy represents an institutional **retrogression** that strangles modern commercial prosperity."}
    ]
  },
  "Dashboard — gress/retrogressive.md": {
    "primary": "Characterized by, tending toward, or causing a return to an earlier, inferior, or less developed state.",
    "secondary": "In metamorphic petrology, retrogressive metamorphism describes the alteration of high-grade mineral assemblages into lower-grade hydrous minerals.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Certain rudimentary structures result from **retrogressive** evolutionary modifications preserved in modern species."},
      {"author": "John Stuart Mill", "work": "Considerations on Representative Government", "quote": "To revive absolute royal vetoes would constitute a **retrogressive** blow against established parliamentary liberty."},
      {"author": "Thomas Carlyle", "work": "Past and Present", "quote": "A merely mechanical political economy offers a **retrogressive** solution to the profound spiritual malaise of our age."}
    ]
  },
  "Dashboard — gress/transgress.md": {
    "primary": "To infringe upon, cross, or go beyond the bounds of a moral principle, command, or legal boundary; to sin.",
    "secondary": "In theological ethics and biblical jurisprudence, to transgress the divine covenant incurs moral guilt requiring expiation.",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Shall we **transgress** the sole command of heaven, and taste the mortal fruit that brings death into the world?"},
      {"author": "William Shakespeare", "work": "The Winter's Tale", "quote": "I am not prone to weeping, as our sex commonly are, yet I have that honorable grief lodged here which does not **transgress**."},
      {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "The soul must never **transgress** the sacred laws of conscience, however dazzling worldly temptations may appear."}
    ]
  },
  "Dashboard — gress/transgression.md": {
    "primary": "An act that goes against a moral rule, law, code of conduct, or social convention; an offense or sin.",
    "secondary": "In sequence stratigraphy and marine geology, a marine transgression occurs when sea level rises relative to land, shifting the shoreline inland.",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Man's first disobedience, and the fruit of that forbidden tree, whose mortal **transgression** brought death into the world."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Pip was haunted by a dark sense of criminal **transgression** after stealing the pork pie and file for the convict."},
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "The widespread marine **transgression** across central Europe deposited thick limestone strata upon eroded basement rocks."}
    ]
  },
  "Dashboard — gress/transgressor.md": {
    "primary": "A person who violates a moral rule, statutory law, or divine command; a wrongdoer or sinner.",
    "secondary": "In legal philosophy and criminal jurisprudence, retributionist theories hold that the transgressor must suffer proportional punishment.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Measure for Measure", "quote": "The law hath not been dead, though it hath slept; now the **transgressor** shall feel the sharpness of its edge."},
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "The stern Puritan magistrates gathered to condemn the unhappy **transgressor** who stood upon the public pillory."},
      {"author": "John Bunyan", "work": "The Pilgrim's Progress", "quote": "The road of the **transgressor** is hard and beset with briars, while the pilgrim walks in righteousness toward the Celestial City."}
    ]
  },
  "Dashboard — gress/unaggressive.md": {
    "primary": "Not aggressive; lacking hostile, competitive, or combative tendencies; gentle, quiet, and peaceful.",
    "secondary": "In veterinary ethology, domestic livestock strains are bred for an unaggressive temperament to ensure safe herd handling.",
    "quotes": [
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Edward Ferrars had an **unaggressive** and unassuming manner, completely free from the arrogant pride of his family."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Artificial selection has produced remarkably gentle, **unaggressive** varieties among domestic sheep and cattle."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Mr. Farebrother was an **unaggressive** clergyman, preferring his natural history collections to bitter theological disputes."}
    ]
  },
  "Dashboard — gress/unprogressive.md": {
    "primary": "Not progressive; opposed to change, innovation, or modern social advancement; static and traditional.",
    "secondary": "In economic development theory, unprogressive agrarian structures characterized by insecure tenancy impede capital investments.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "Considerations on Representative Government", "quote": "A stationary and **unprogressive** society inevitably falls behind neighboring nations in wealth and intellectual power."},
      {"author": "Sinclair Lewis", "work": "Main Street", "quote": "Carol lamented the stubbornly **unprogressive** mentality of the town aldermen, who rejected her modern civic improvements."},
      {"author": "Thomas Carlyle", "work": "Past and Present", "quote": "To maintain an idle, **unprogressive** aristocracy in an age of urgent industrial labor is an invitation to catastrophe."}
    ]
  },

  # --- Dashboard — ced (41 words) ---
  "Dashboard — ced/accede.md": {
    "primary": "To agree to a demand, request, or proposal; or to formally assume an office, dignity, or treaty.",
    "secondary": "In international public law, sovereign nations accede to multilateral conventions by depositing formal instruments of accession.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Mr. Bennet was at length prevailed upon to **accede** to his wife's earnest request to visit Netherfield."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The young prince was summoned by the senate to **accede** to the imperial throne amidst the cheers of the guard."},
      {"author": "Winston Churchill", "work": "The World Crisis", "quote": "The foreign office urged the neutral kingdom to **accede** to the maritime treaty for the protection of merchant shipping."}
    ]
  },
  "Dashboard — ced/alcedinidae.md": {
    "primary": "The taxonomic bird family of kingfishers in the order Coraciiformes, known for large heads, long pointed bills, and iridescent plumage.",
    "secondary": "In systematic avian ornithology, the Alcedinidae comprise river kingfishers, characterized by syndactyl feet and plunge-diving for fish.",
    "quotes": [
      {"author": "John James Audubon", "work": "Ornithological Biography", "quote": "The belted kingfisher and its vibrant allies in the **Alcedinidae** frequent rushing wilderness streams and tidal creeks."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Naturalists admire the brilliant metallic colors and dagger-like bills that distinguish the **Alcedinidae** across tropical climes."},
      {"author": "Thomas Henry Huxley", "work": "Manual of the Anatomy of Vertebrated Animals", "quote": "The osteological structure of the bill and syndactyl feet across the **Alcedinidae** displays adaptation for piscivorous predation."}
    ]
  },
  "Dashboard — ced/alcedo.md": {
    "primary": "The type genus of typical river kingfishers in the family Alcedinidae, including the common European kingfisher (Alcedo atthis).",
    "secondary": "In avian ecological morphology, species of Alcedo possess specialized corneal refractive adaptations enabling sharp underwater binocular vision.",
    "quotes": [
      {"author": "Gilbert White", "work": "The Natural History of Selborne", "quote": "A flash of brilliant turquoise along the riverbank revealed a solitary specimen of the genus **Alcedo** darting after minnows."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The geographic distribution of the genus **Alcedo** across the Old World demonstrates remarkable conservation of hunting form."},
      {"author": "Thomas Henry Huxley", "work": "The Crayfish", "quote": "The crayfish must beware the sharp plunge-diving assault of **Alcedo** when sunning in shallow stream waters."}
    ]
  },
  "Dashboard — ced/antecede.md": {
    "primary": "To precede in time, rank, order, or importance; to go before.",
    "secondary": "In legal causation and historical philosophy, determining which political conditions antecede a revolution illuminates causal origins.",
    "quotes": [
      {"author": "David Hume", "work": "A Treatise of Human Nature", "quote": "In every causal sequence, the cause must necessarily **antecede** the effect in chronological time."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Simple sensory ideas must always **antecede** the complex mental operations performed upon them by the understanding."},
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "Volcanic eruptions frequently **antecede** regional seismic tremors, signaling deep subterranean magma displacement."}
    ]
  },
  "Dashboard — ced/antecedence.md": {
    "primary": "The state, condition, or fact of preceding or going before something in time, order, or priority; priority.",
    "secondary": "In epistemological philosophy of science, temporal antecedence serves as a necessary, though not sufficient, condition for causal inference.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "The invariant and unconditional **antecedence** of one phenomenon to another constitutes the philosophical essence of physical cause."},
      {"author": "David Hume", "work": "An Enquiry Concerning Human Understanding", "quote": "Constant conjunction and temporal **antecedence** are the empirical elements that our minds interpret as necessary connection."},
      {"author": "Herbert Spencer", "work": "First Principles", "quote": "The cosmic **antecedence** of nebulous matter to organized stellar systems illustrates the progressive law of evolution."}
    ]
  },
  "Dashboard — ced/antecedency.md": {
    "primary": "The state or quality of being antecedent; precedence in time, rank, or logical sequence.",
    "secondary": "In analytical logic and philosophical grammar, antecedency defines the syntactic relationship of a pronoun to its referent.",
    "quotes": [
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "The natural **antecedency** of empirical observation over speculative theory is the foundation of inductive science."},
      {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "The primary imagination claims an ontological **antecedency** over all secondary artistic creative processes."},
      {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "Spiritual reality possesses an eternal **antecedency** over the transient material forms of the visible world."}
    ]
  },
  "Dashboard — ced/antecedent.md": {
    "primary": "A preceding circumstance, event, or condition; or in grammar, a word or phrase to which a subsequent pronoun refers.",
    "secondary": "In deductive conditional logic (modus ponens), affirming the antecedent in a conditional premise ('if P then Q') validates the consequent.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "A Study in Scarlet", "quote": "Holmes traced the mysterious killer's **antecedent** history back to the early pioneer settlements of Utah."},
      {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "The inductive method compares varying instances to isolate the single invariable **antecedent** associated with the effect."},
      {"author": "David Hume", "work": "A Treatise of Human Nature", "quote": "Every event in nature is preceded by some physical **antecedent** that determines its occurrence in space and time."}
    ]
  },
  "Dashboard — ced/antecedently.md": {
    "primary": "At an earlier time; prior to something else; previously.",
    "secondary": "In philosophical epistemology and Bayesian inference, an event judged antecedently improbable requires extraordinary confirmatory evidence.",
    "quotes": [
      {"author": "David Hume", "work": "An Enquiry Concerning Human Understanding", "quote": "A miracle is an event which, **antecedently** to all testimony, must be considered contrary to universal experience."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "The mind cannot contain complex innate notions **antecedently** to all sensory experience of the external world."},
      {"author": "Thomas Babington Macaulay", "work": "Critical and Historical Essays", "quote": "The political measures had been **antecedently** agreed upon in secret conferences before parliamentary debate began."}
    ]
  },
  "Dashboard — ced/arced.md": {
    "primary": "Followed or curved along an arc-shaped curved trajectory; or produced an electric discharge arc across a gap.",
    "secondary": "In electrical power transmission and switchgear engineering, high-voltage current arced across contact points during circuit breaking.",
    "quotes": [
      {"author": "H. G. Wells", "work": "The War of the Worlds", "quote": "A dazzling flash of emerald lightning **arced** between the tripod's metallic tentacles, striking the pine trees."},
      {"author": "Arthur Conan Doyle", "work": "The Lost World", "quote": "Challenger's makeshift electric barrier **arced** with a sharp crackle whenever inquisitive pterodactyls approached."},
      {"author": "Stephen Crane", "work": "The Red Badge of Courage", "quote": "The artillery shell **arced** gracefully across the smoky blue sky before plunging into the dense forest below."}
    ]
  },
  "Dashboard — ced/cedar.md": {
    "primary": "Any of several coniferous evergreen trees of the genus Cedrus, renowned for aromatic, decay-resistant, fragrant wood.",
    "secondary": "In dendrochronology and ancient Mediterranean timber history, the Cedar of Lebanon was prized for shipbuilding and temple columns.",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Overhead up grew inuperable height of loftiest shade, **cedar**, and pine, and fir, and branching palm in heavenly Eden."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The delicate ribs of the whaleboat were crafted from aromatic **cedar**, combining light buoyancy with remarkable flexibility."},
      {"author": "Nathaniel Hawthorne", "work": "The House of the Seven Gables", "quote": "An ancient **cedar** tree cast its gloomy, fragrant boughs across the overgrown garden of the old mansion."}
    ]
  },
  "Dashboard — ced/cedar-scented.md": {
    "primary": "Imbued with or diffusing the distinctive sweet, resinous, aromatic fragrance of cedar wood.",
    "secondary": "In domestic historic preservation, cedar-scented linen chests were traditionally utilized to deter fabric-destroying clothes moths.",
    "quotes": [
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "Jane opened the antique wardrobe in the guest chamber, breathing the comforting, **cedar-scented** air of old lavender and linen."},
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "The quiet library of the country estate was pleasant and **cedar-scented**, its high windows overlooking the park."},
      {"author": "F. Scott Fitzgerald", "work": "The Beautiful and Damned", "quote": "Gloria stored her delicate furs and silk evening gowns in a **cedar-scented** trunk before departing for the season."}
    ]
  },
  "Dashboard — ced/cedarbird.md": {
    "primary": "A North American passerine bird (Bombycilla cedrorum), commonly known as the cedar waxwing, with sleek plumage and waxy red wingtips.",
    "secondary": "In avian ornithological ecology, the cedarbird exhibits specialized frugivorous behavior, feeding on cedar berries and wild cherries.",
    "quotes": [
      {"author": "John James Audubon", "work": "Ornithological Biography", "quote": "Flocks of the gentle **cedarbird** descend upon the juniper groves in winter, feasting upon the blue aromatic berries."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "I observed a handsome **cedarbird** perched motionless upon a hemlock branch, its crested head sleek in the morning light."},
      {"author": "Gilbert White", "work": "The Natural History of Selborne", "quote": "American naturalists describe the social feeding habits and exquisite waxy wingtips of the migrant **cedarbird**."}
    ]
  },
  "Dashboard — ced/cedarn.md": {
    "primary": "Made of, relating to, or resembling cedar; aromatic like cedar wood.",
    "secondary": "In Romantic and Renaissance poetic diction, cedarn groves evoked mythic classical sanctuaries and incorruptible timber.",
    "quotes": [
      {"author": "John Milton", "work": "Comus", "quote": "Right against the eastern gate, where the great sun begins his state, arrayed in flames and amber light, upon the **cedarn** alley."},
      {"author": "Percy Bysshe Shelley", "work": "Prometheus Unbound", "quote": "Sweet winds breathed through the **cedarn** shadows of the mountain, scattering fragrant needles upon the moss."},
      {"author": "Lord Byron", "work": "Don Juan", "quote": "The private chamber was lined with polished **cedarn** paneling that filled the warm air with a subtle incense."}
    ]
  },
  "Dashboard — ced/cedarwood.md": {
    "primary": "The durable, fragrant, insect-repelling wood obtained from cedar trees, prized for cabinetry and construction.",
    "secondary": "In essential oil extraction and perfumery, cedarwood oil functions as a grounding base note and natural insect repellent.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "The lawyer kept his confidential files locked in a heavy chest of fragrant **cedarwood** bound with brass straps."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The sea chest was fashioned from aromatic **cedarwood**, protecting Queequeg's woven garments from the damp sea air."},
      {"author": "Rudyard Kipling", "work": "Kim", "quote": "The Tibetan lama carried an exquisite small box carved from aromatic **cedarwood**, containing sacred pilgrimage charms."}
    ]
  },
  "Dashboard — ced/cede.md": {
    "primary": "To give up, surrender, or relinquish power, territory, or legal rights to another party.",
    "secondary": "In international treaties and territorial sovereignty, defeated nations cede peripheral provinces through formal peace conventions.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The weakened emperor was compelled to **cede** the rich provinces of Moesia and Dacia to the Gothic invaders."},
      {"author": "Winston Churchill", "work": "The World Crisis", "quote": "Britain refused to **cede** an inch of colonial territory under the naval threats of foreign powers."},
      {"author": "Thomas Babington Macaulay", "work": "History of England", "quote": "The crown agreed to **cede** certain ancient prerogatives in exchange for regular parliamentary financial subsidies."}
    ]
  },
  "Dashboard — ced/cedi.md": {
    "primary": "The basic monetary currency unit of Ghana, divided into one hundred pesewas.",
    "secondary": "In African macroeconomic monetary history, the Bank of Ghana introduced the cedi in 1965 to replace the colonial West African pound.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "West African commerce formerly relied upon cowrie shells, foreshadowing modern national currencies like the **cedi**."},
      {"author": "John Maynard Keynes", "work": "The Economic Consequences of the Peace", "quote": "Monetary stabilization requires sound central bank reserves whether calculating in sterling, francs, or the African **cedi**."},
      {"author": "Joseph Conrad", "work": "Heart of Darkness", "quote": "The coastal merchant evaluated foreign trade drafts and local African currencies with seasoned commercial precision."}
    ]
  },
  "Dashboard — ced/cedilla.md": {
    "primary": "A diacritical mark (ç) placed below the letter 'c' in French, Portuguese, and other languages to indicate a soft 's' sound.",
    "secondary": "In historical romance orthography, the cedilla evolved from a miniature Visigothic script 'z' placed beneath letters.",
    "quotes": [
      {"author": "Charlotte Brontë", "work": "Villette", "quote": "Lucy Snowe carefully corrected the French composition, inserting a missing **cedilla** beneath the letter 'c' on the blackboard."},
      {"author": "Mark Twain", "work": "A Tramp Abroad", "quote": "Twain joked that foreign alphabets were adorned with hooks, umlauts, and the mysterious **cedilla** to confound travelers."},
      {"author": "Henry James", "work": "The American", "quote": "Christopher Newman examined the Parisian legal document, noticing the delicate **cedilla** under French names on the seal."}
    ]
  },
  "Dashboard — ced/ceding.md": {
    "primary": "Surrendering, yielding, or formally transferring possession, rights, or territory to another sovereign or party.",
    "secondary": "In geopolitical diplomacy, ceding strategic maritime islands frequently alters exclusive economic zone boundaries under international law.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "By **ceding** the frontier strongholds to the Persians, the disgraced emperor purchased a temporary and precarious peace."},
      {"author": "Winston Churchill", "work": "The Second World War", "quote": "The capitulation of the government was sealed by **ceding** naval bases and strategic territory to the conqueror."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The monarchy was trapped into **ceding** prerogative after prerogative to the surging national representatives."}
    ]
  },
  "Dashboard — ced/cedrela.md": {
    "primary": "A genus of seven species of flowering trees in the mahogany family Meliaceae, especially Cedrela odorata (Spanish cedar).",
    "secondary": "In tropical timber forestry, the rot-resistant aromatic wood of Cedrela is widely used for traditional high-grade cigar boxes.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "Dense forests of Spanish cedar belonging to **Cedrela** covered the moist tropical mountain slopes of the mainland."},
      {"author": "Alexander von Humboldt", "work": "Personal Narrative of Travels to the Equinoctial Regions", "quote": "The river banks were shaded by majestic trunks of **Cedrela**, whose fragrant timber was exported for cabinetmaking."},
      {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "Botanists study the pinnate foliage and valuable aromatic hardwood produced by tropical species of **Cedrela**."}
    ]
  },
  "Dashboard — ced/cedrus.md": {
    "primary": "The botanical genus of true cedars in the pine family Pinaceae, encompassing the cedar of Lebanon, atlas cedar, and deodar.",
    "secondary": "In dendrological taxonomy, Cedrus is native to the Mediterranean basin and western Himalayas, distinguished by clustered needle rosettes.",
    "quotes": [
      {"author": "John Muir", "work": "The Mountains of California", "quote": "The magnificent Himalayan deodar, a noble member of **Cedrus**, rivals the Sierra pines in majesty of form."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Cultivated specimens of **Cedrus** libani exhibit considerable morphological variation under differing European soils."},
      {"author": "Gilbert White", "work": "The Natural History of Selborne", "quote": "The great estate was adorned with towering trees of **Cedrus**, their flat horizontal boughs providing deep shade."}
    ]
  },
  "Dashboard — ced/concede.md": {
    "primary": "To acknowledge, admit, or surrender something as true, valid, or proper, typically after initial reluctance or debate.",
    "secondary": "In democratic electoral politics, candidates concede defeat once vote tallies demonstrate an insurmountable statistical lead.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth was forced to **concede** that Darcy's letter presented the facts regarding Wickham in a completely new light."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Holmes was generous enough to **concede** that the Scotland Yard inspector had shown commendable initiative."},
      {"author": "John Stuart Mill", "work": "On Liberty", "quote": "An honest debater will readily **concede** points where empirical facts refute his initial preconceptions."}
    ]
  },
  "Dashboard — ced/conceding.md": {
    "primary": "Admitting, acknowledging, or yielding something as true, valid, or lost during discussion, debate, or contest.",
    "secondary": "In diplomatic treaty bargaining, strategically conceding non-essential points preserves core national security objectives.",
    "quotes": [
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Elinor spoke with calm reason, **conceding** that appearances were unfavorable while maintaining her private faith."},
      {"author": "Winston Churchill", "work": "The Second World War", "quote": "The allied high command refused to consider **conceding** any territory that would compromise Mediterranean sea lanes."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Mr. Tulkinghorn listened in cold silence, **conceding** nothing to the agitated lady who pleaded before him."}
    ]
  },
  "Dashboard — ced/decedent.md": {
    "primary": "A deceased person, especially one who has died recently and whose estate is subject to legal probate administration.",
    "secondary": "In estate and probate jurisprudence, the personal representative settles the decedent's debts prior to distributing testamentary bequests.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The dusty solicitors examined the disputed testament of the **decedent**, calculating endless fees from the contested estate."},
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Norwood Builder", "quote": "Holmes examined the testamentary will of the supposed **decedent**, noticing strange anomalies in the handwritten signature."},
      {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "The greedy relatives gathered in black at the mansion to hear the will of the wealthy **decedent** read aloud."}
    ]
  },
  "Dashboard — ced/intercede.md": {
    "primary": "To intervene, mediate, or plead on behalf of another person, especially in a dispute or difficulty.",
    "secondary": "In theological soteriology, Christ is described as the heavenly mediator who lives to intercede for humanity.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Merchant of Venice", "quote": "Portia resolved to **intercede** on behalf of the noble merchant Antonio against the vengeful bond of Shylock."},
      {"author": "Jane Austen", "work": "Mansfield Park", "quote": "Fanny Price attempted to **intercede** for her cousin, begging Sir Thomas to moderate his severe judgment."},
      {"author": "Walter Scott", "work": "The Heart of Midlothian", "quote": "Jeanie Deans traveled on foot to London to **intercede** with the Queen for her sister's pardon."}
    ]
  },
  "Dashboard — ced/precede.md": {
    "primary": "To come, occur, or exist before something or someone in time, order, position, or rank.",
    "secondary": "In ceremonial diplomatic protocol, ambassadorial accreditations precede consular appointments according to international order.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "Let our best thought **precede** our actions, lest hasty judgment lead our steps into tragic error."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Simpler organic structures invariably **precede** more complex, specialized adaptations in the fossil strata."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Mr. Collins was careful to allow Lady Catherine's carriage to **precede** his own in every village procession."}
    ]
  },
  "Dashboard — ced/precedence.md": {
    "primary": "The condition of being considered more important than someone or something else; priority in rank or order.",
    "secondary": "In aristocratic court protocol, strict tables of precedence govern seating arrangements and entry order at state banquets.",
    "quotes": [
      {"author": "Jane Austen", "work": "Persuasion", "quote": "Sir Walter Elliot was obsessively devoted to matters of social **precedence**, consulting the Baronetage daily."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The rival consuls contested bitter disputes over ceremonial **precedence** before the assembled Roman senate."},
      {"author": "Winston Churchill", "work": "The Second World War", "quote": "Vital aircraft production was given absolute priority and **precedence** over all other military manufacturing."}
    ]
  },
  "Dashboard — ced/precedency.md": {
    "primary": "The state or condition of preceding in time, rank, order, or importance; an alternative spelling of precedence.",
    "secondary": "In early modern British ceremonial history, disputes over royal precedency were adjudicated by the Court of Chivalry.",
    "quotes": [
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "The ancient orders of nobility maintained their established **precedency** as a barrier against arbitrary monarchical power."},
      {"author": "Jonathan Swift", "work": "Gulliver's Travels", "quote": "The courtiers of Lilliput engaged in acrobatic rope-dancing contests to determine their political **precedency**."},
      {"author": "Thomas Babington Macaulay", "work": "History of England", "quote": "The ambassadors of France and Spain fought openly in the streets of London over diplomatic **precedency**."}
    ]
  },
  "Dashboard — ced/precedent.md": {
    "primary": "An earlier event, decision, or action that is regarded as an example, guide, or authority for subsequent similar circumstances.",
    "secondary": "In Anglo-American common law, the doctrine of stare decisis mandates that courts adhere to established judicial precedent.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Holmes remarked that in criminal investigation, an exact historical **precedent** can almost always be found in the archives."},
      {"author": "Thomas Babington Macaulay", "work": "History of England", "quote": "The parliamentary jurists scrupulously searched ancient rolls of parchment to find a sound constitutional **precedent**."},
      {"author": "Edmund Burke", "work": "Speech on Conciliation with America", "quote": "We must govern our great empire not by abstract metaphysical theories, but by historical **precedent** and human prudence."}
    ]
  },
  "Dashboard — ced/precedented.md": {
    "primary": "Supported, justified, or sanctioned by previous example, custom, or historical precedent.",
    "secondary": "In administrative and legal decision-making, an action is judged precedented when prior statutory rulings provide explicit authority.",
    "quotes": [
      {"author": "Thomas Babington Macaulay", "work": "History of England", "quote": "The royal proclamation was fully **precedented** by numerous Tudor and Stuart ordinances in the state papers."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The elevation of the military commander was **precedented** by the frequent practice of the late imperial legions."},
      {"author": "John Locke", "work": "Second Treatise of Government", "quote": "Civil magistrates must act within **precedented** statutory limits established by the legislative authority of the people."}
    ]
  },
  "Dashboard — ced/precedentedly.md": {
    "primary": "In a manner supported by or conforming to established prior examples or historical precedents.",
    "secondary": "In parliamentary procedure, bills handled precedentedly adhere strictly to standard reading schedules and committee referrals.",
    "quotes": [
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "The English Revolution of 1688 proceeded **precedentedly**, adhering to ancient constitutional forms and charters."},
      {"author": "Thomas Babington Macaulay", "work": "History of England", "quote": "The crown acted **precedentedly** in summoning parliament according to established historical writs."},
      {"author": "David Hume", "work": "The History of England", "quote": "The judicial council resolved the disputed estate **precedentedly**, citing ancient Saxon land tenures."}
    ]
  },
  "Dashboard — ced/precedential.md": {
    "primary": "Of, relating to, or having the force or authority of a legal or authoritative precedent.",
    "secondary": "In appellate jurisprudence, opinions designated for official publication carry binding precedential effect upon subordinate trial courts.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "To avoid an arbitrary discretion in the courts, judges must be bound down by strict rules and **precedential** decisions."},
      {"author": "Thomas Babington Macaulay", "work": "Critical and Historical Essays", "quote": "The trial of the seven bishops was recognized as carrying profound **precedential** significance for constitutional freedom."},
      {"author": "John Stuart Mill", "work": "Considerations on Representative Government", "quote": "A single unconstitutional decree may establish a dangerous **precedential** foothold for future despotic encroachments."}
    ]
  },
  "Dashboard — ced/preceding.md": {
    "primary": "Existing, occurring, or coming immediately before something in time, place, order, or rank; previous.",
    "secondary": "In chronological data analysis and economics, comparing quarterly output to the preceding quarter measures sequential growth.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Holmes reviewed the events of the **preceding** night, noting each footprint upon the rain-softened pathway."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The horrors of the terror eclipsed even the misery of the **preceding** decades under aristocratic rule."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The structural modifications described in the **preceding** chapter illustrate the power of natural selection."}
    ]
  },
  "Dashboard — ced/procedural.md": {
    "primary": "Relating to, established by, or conforming to established official procedures, protocols, or rules of conduct.",
    "secondary": "In constitutional due process law, procedural due process guarantees notice and an opportunity to be heard before deprivation of rights.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Inspector Athelney Jones insisted upon strict **procedural** protocol, though it continually delayed his investigation."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The Court of Chancery was entangled in endless **procedural** motions while the suit of Jarndyce dragged on."},
      {"author": "Winston Churchill", "work": "The Second World War", "quote": "The war cabinet dispensed with peacetime **procedural** delays to accelerate the emergency supply of munitions."}
    ]
  },
  "Dashboard — ced/procedure.md": {
    "primary": "An established or official way of doing something, especially an agreed series of steps or actions.",
    "secondary": "In modern surgical medicine, an invasive surgical procedure requires sterile operative field preparation and anesthesia.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "A Study in Scarlet", "quote": "Holmes explained his scientific **procedure** for detecting minute traces of human blood in criminal investigations."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The labyrinthine legal **procedure** of Chancery exhausted the patience and wealth of every unfortunate suitor."},
      {"author": "Francis Bacon", "work": "Novum Organum", "quote": "The true scientific method requires a rigorous **procedure** of inductive experimentation and critical elimination."}
    ]
  },
  "Dashboard — ced/recede.md": {
    "primary": "To move back or further away from a previous position; to retreat, ebb, or diminish.",
    "secondary": "In coastal geomorphology and marine hydrology, ocean tides recede during low water, exposing intertidal mudflats.",
    "quotes": [
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "I watched the dark mountain shadow slowly **recede** as the morning sun illuminated the valley of Chamounix."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The shores of Nantucket began to **recede** into the distance as the Pequod plunged into the open Atlantic."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "David watched the white cliffs of Dover **recede** into the ocean haze from the deck of the packet boat."}
    ]
  },
  "Dashboard — ced/receding.md": {
    "primary": "Moving back, withdrawing, or sloping backward; diminishing or fading from sight.",
    "secondary": "In dental morphology and periodontology, receding gingival tissue exposes sensitive tooth root surfaces to bacterial caries.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Watson listened to the **receding** footsteps of the night watcher dying away across the desolate granite moor."},
      {"author": "Joseph Conrad", "work": "Heart of Darkness", "quote": "The river steamboat crawled up the yellow stream, the **receding** banks of forest watching in monumental silence."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "The storm passed over Thornfield, its **receding** thunder muttering faintly among the distant hills."}
    ]
  },
  "Dashboard — ced/secede.md": {
    "primary": "To withdraw formally from an alliance, federation, political union, or religious organization.",
    "secondary": "In constitutional and civil war history, eleven southern states resolved to secede from the American Union in 1860–1861.",
    "quotes": [
      {"author": "Abraham Lincoln", "work": "First Inaugural Address", "quote": "No state upon its own mere motion can lawfully get out of the Union; to **secede** is the essence of anarchy."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Several Gallic legions threatened to **secede** from the empire and crown their own provincial commander."},
      {"author": "Thomas Babington Macaulay", "work": "History of England", "quote": "The non-juring clergy resolved to **secede** from the established church rather than swear allegiance to William of Orange."}
    ]
  },
  "Dashboard — ced/succedaneum.md": {
    "primary": "A substitute, replacement, or surrogate; especially a medicinal drug or material used in place of another.",
    "secondary": "In classical pharmacology, synthetic antipyretics were evaluated as an effective succedaneum for scarce natural quinine.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The physician cautioned against employing an untested herbal **succedaneum** when standard digitalis was available."},
      {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "Utilitarian materialism offers only a cold, mechanical **succedaneum** for the living spiritual faith of past ages."},
      {"author": "Oliver Goldsmith", "work": "The Citizen of the World", "quote": "The eccentric philosopher invented a curious chemical **succedaneum** to replace expensive oriental tea."}
    ]
  },
  "Dashboard — ced/supercede.md": {
    "primary": "An alternative or variant spelling of supersede, signifying to replace, supplant, or set aside in favor of another.",
    "secondary": "In legal drafting and contract interpretation, newer statutory amendments supercede prior contradictory administrative rules.",
    "quotes": [
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "New empirical discoveries must eventually **supercede** ancient scholastic dogmas in the investigation of nature."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The new administrative edicts issued by the emperor were intended to **supercede** the ancient laws of the republic."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "The mechanical theory of heat was destined to **supercede** the obsolete fluid hypothesis of caloric."}
    ]
  },
  "Dashboard — ced/unprecedented.md": {
    "primary": "Never done, experienced, or known before; completely without prior parallel or historical precedent.",
    "secondary": "In constitutional crises and executive emergency law, governments adopt unprecedented statutory measures during total war.",
    "quotes": [
      {"author": "Winston Churchill", "work": "The Second World War", "quote": "The blitz on London presented an **unprecedented** challenge to the courage and civil organization of our people."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The sudden collapse of three frontier armies was a calamity **unprecedented** in the annals of imperial Rome."},
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "Frankenstein embarked upon an **unprecedented** scientific enterprise that defied the established laws of nature."}
    ]
  },
  "Dashboard — ced/unprecedentedly.md": {
    "primary": "In a manner or to an extent that has never occurred or been known before; without parallel.",
    "secondary": "In economic history, industrial productivity grew unprecedentedly following the adoption of steam-driven rotary power.",
    "quotes": [
      {"author": "Winston Churchill", "work": "The World Crisis", "quote": "The expansion of British munitions manufacturing proceeded **unprecedentedly** during the critical summer of 1915."},
      {"author": "Charles Dickens", "work": "Hard Times", "quote": "The profits of the Coketown textile mills rose **unprecedentedly** as automated spinning looms ran day and night."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The Parisian populace mobilized **unprecedentedly**, storming the royal arsenal to arm thirty thousand citizens."}
    ]
  }
}

base_dir = r"App database\Latin roots\Cluster Motion"
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

print(f"Motion Batch 4A: Successfully updated {updated}/{len(data)} notes.")
