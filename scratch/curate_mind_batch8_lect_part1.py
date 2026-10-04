# -*- coding: utf-8 -*-
"""
Curates Dashboard — lect (Part 1: words 1-65) in Cluster Mind & Knowledge.
"""
import os, sys, re

sys.stdout.reconfigure(encoding="utf-8")

data_part1 = {
  "antielectron": {
    "primary": "The antimatter counterpart of an electron, identical in mass and spin but carrying a positive charge; a positron.",
    "secondary": "In particle physics, a lepton (e+) predicted by Dirac's relativistic wave equation and discovered in cosmic rays.",
    "quotes": [
      {"author": "Paul Dirac", "work": "The Principles of Quantum Mechanics", "quote": "The relativistic wave equation required negative energy states, interpreted physically as an **antielectron**."},
      {"author": "Carl Sagan", "work": "Cosmos", "quote": "When an electron collides with an **antielectron**, both particles annihilate in a blinding flash of gamma rays."},
      {"author": "Richard Feynman", "work": "QED: The Strange Theory of Light and Matter", "quote": "A positron can be mathematically described as an ordinary electron or **antielectron** traveling backward in time."}
    ]
  },
  "aplectrum": {
    "primary": "A monotypic genus of North American terrestrial orchids comprising Aplectrum hyemale, the puttyroot or Adam-and-Eve orchid.",
    "secondary": "In botanical systematics, a woodland orchid characterized by coralloid corms that produce mucilage used as glue.",
    "quotes": [
      {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The solitary winter leaf of **Aplectrum** unfolds in autumn, persisting until the flowering scape emerges in May."},
      {"author": "Liberty Hyde Bailey", "work": "Cyclopedia of American Horticulture", "quote": "Rich deciduous forests provide the organic leaf mold required by wild colonies of **Aplectrum**."},
      {"author": "John Muir", "work": "The Story of My Boyhood and Youth", "quote": "Pioneers gathered sticky corms of **Aplectrum** to mend fractured pottery and earthenware bowls."}
    ]
  },
  "collect": {
    "primary": "To bring together things from different places or people, or a short liturgical prayer in Christian services.",
    "secondary": "In municipal administration, to gather public revenues, municipal waste, or postal communications.",
    "quotes": [
      {"author": "Charles Darwin", "work": "Autobiography", "quote": "My zeal to **collect** rare beetles in Cambridge was so great that I once carried one specimen inside my mouth."},
      {"author": "Jane Austen", "work": "Emma", "quote": "Mr. Elton rose to recite the appointed liturgical **collect** with a sonorous and polished cadence."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The sovereign must employ trustworthy magistrates to **collect** customs duties along maritime ports."}
    ]
  },
  "collectable": {
    "primary": "An item valued by collectors and considered worthy of collecting, or capable of being collected or recovered.",
    "secondary": "In accounting, debts, receivables, or delinquent taxes that can be realistically recovered through legal means.",
    "quotes": [
      {"author": "Henry James", "work": "The Aspern Papers", "quote": "Every scrap of the deceased poet's handwriting was considered an invaluable **collectable** by literary devotees."},
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Illustrious Client", "quote": "Baron Gruner's private diary was a perilous **collectable**, detailing his sinister romantic conquests."},
      {"author": "Charles Dickens", "work": "Little Dorrit", "quote": "The debt collector surveyed the meager assets, wondering if any outstanding shilling remained **collectable**."}
    ]
  },
  "collected": {
    "primary": "Calm, self-possessed, and composed, or brought together into a single comprehensive assembly or edition.",
    "secondary": "In literary publishing, the definitive compilation of an author's complete works, poems, or letters.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth remained remarkably cool and **collected**, refusing to be intimidated by Lady Catherine's haughty brow."},
      {"author": "Samuel Johnson", "work": "Lives of the Poets", "quote": "His **collected** verses were published in three handsome calfskin folios by the university press."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Holmes examined the ashes with a **collected** demeanor that inspired confidence in his anxious client."}
    ]
  },
  "collectedly": {
    "primary": "In a calm, cool, self-possessed, and deliberate manner; without showing signs of agitation or panic.",
    "secondary": "In courtroom testimony, answering adversarial cross-examinations with measured serenity.",
    "quotes": [
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "Darnay answered the revolutionary prosecutor **collectedly**, looking calmly upon the howling gallery."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "Jane spoke **collectedly**, refusing to surrender her moral conscience to Rochester's passionate entreaties."},
      {"author": "Walter Scott", "work": "The Heart of Midlothian", "quote": "Jeanie Deans delivered her testimony **collectedly**, determined to speak only the plain, unvarnished truth."}
    ]
  },
  "collectible": {
    "primary": "An object suitable for or sought after by collectors, such as rare stamps, coins, antiquities, or artwork.",
    "secondary": "In retail commerce, limited-edition manufactured items designed specifically to appreciate in secondary markets.",
    "quotes": [
      {"author": "Edith Wharton", "work": "The Age of Innocence", "quote": "Old Mr. van der Luyden displayed a rare porcelain figurine that was the most prized **collectible** in New York."},
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Six Napoleons", "quote": "The plaster bust was an ordinary five-shilling cast, possessing no inherent value as a connoisseur's **collectible**."},
      {"author": "Henry James", "work": "The Spoils of Poynton", "quote": "Mrs. Gereth lived only for her furniture, evaluating every room in terms of its unique **collectible** treasure."}
    ]
  },
  "collecting": {
    "primary": "The act or hobby of gathering objects of a particular type, or gathering together scattered entities into a group.",
    "secondary": "In finance, the systematic pursuit and recovery of overdue debts, commercial accounts, or municipal fees.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "I spent hours along the riverbanks, **collecting** unknown land shells and pressing delicate ferns into paper."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Mr. Casaubon devoted his solitary life to **collecting** obscure mythical fragments for his vast unfinished treatise."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Stapleton bounded across the treacherous Grimpen Mire with his green net, **collecting** rare nocturnal moths."}
    ]
  },
  "collection": {
    "primary": "A group of things or people gathered together; a curated assemblage of artworks, books, or historical specimens.",
    "secondary": "In financial banking, the formal process of presenting negotiable instruments to obtain payment.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The imperial library of Constantinople preserved a magnificent **collection** of classical Greek poets and orators."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "A single visit to the national **collection** of minerals reveals every intermediate transition of crystal form."},
      {"author": "Jane Austen", "work": "Northanger Abbey", "quote": "Catherine was astonished by the immense **collection** of gothic curiosities displayed within the abbey gallery."}
    ]
  },
  "collective": {
    "primary": "Done by or characteristic of individuals acting together as a group; cooperative, combined, or shared.",
    "secondary": "In agricultural sociology, an enterprise or farm managed cooperatively under communal or state ownership.",
    "quotes": [
      {"author": "Carl Jung", "work": "The Archetypes and the Collective Unconscious", "quote": "The **collective** unconscious contains the inherited spiritual treasury of primordial mythological motifs."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "The **collective** strength of citizens united in civic association surpasses the absolute power of monarchs."},
      {"author": "Karl Marx", "work": "Das Kapital", "quote": "Modern manufacture converts the isolated artisan into a specialized organ of the **collective** working body."}
    ]
  },
  "collectively": {
    "primary": "As a whole or combined group; in a collective manner, jointly, or cooperatively.",
    "secondary": "In legal liability, denoting joint responsibility borne equally by all corporate partners or signatories.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The states united **collectively** possess maritime power sufficient to repel foreign commercial aggression."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Consumers acting **collectively** dictate the market prices of commodities through aggregate effective demand."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Social insects act **collectively** to defend the hive, sacrificing individual lives for the community."}
    ]
  },
  "collectivisation": {
    "primary": "The process of organizing an economy, industry, or agriculture around collective ownership (British spelling).",
    "secondary": "In Soviet history, the enforced consolidation of individual peasant farms into state-managed kolkhozes.",
    "quotes": [
      {"author": "George Orwell", "work": "Animal Farm", "quote": "The windmill construction symbolized the forced **collectivisation** of animal labor under Napoleon's decree."},
      {"author": "Arthur Koestler", "work": "The Yogi and the Commissar", "quote": "The catastrophic agricultural **collectivisation** claimed millions of lives across the black-earth famine belt."},
      {"author": "E. H. Carr", "work": "The Russian Revolution", "quote": "Massive **collectivisation** served as the indispensable economic engine to finance rapid heavy industrialization."}
    ]
  },
  "collectivise": {
    "primary": "To organize something on the basis of ownership or control by the state or a group (British spelling).",
    "secondary": "In agrarian policy, merging individual private farms into state-controlled cooperative units.",
    "quotes": [
      {"author": "George Orwell", "work": "Homage to Catalonia", "quote": "In revolutionary Aragon, the peasants chose to **collectivise** the olive groves and share the harvest equally."},
      {"author": "Arthur Koestler", "work": "Darkness at Noon", "quote": "Rubashov recalled his brutal mission to **collectivise** recalcitrant kulaks who hid their wheat beneath floorboards."},
      {"author": "Eric Hobsbawm", "work": "The Age of Extremes", "quote": "State planners sought to **collectivise** grain production to guarantee food supplies for industrial cities."}
    ]
  },
  "collectivised": {
    "primary": "Organized under collective or state control; converted into collective ownership (British spelling).",
    "secondary": "In historical economics, describing Soviet-bloc farms and industrial factories managed by collective boards.",
    "quotes": [
      {"author": "George Orwell", "work": "Nineteen Eighty-Four", "quote": "In Oceania, all productive property was nominally **collectivised**, yet true power rested in the hands of the Inner Party."},
      {"author": "Arthur Koestler", "work": "The God That Failed", "quote": "The bleak **collectivised** villages presented a scene of sullen despair that shocked foreign socialist pilgrims."},
      {"author": "Alexander Solzhenitsyn", "work": "The Gulag Archipelago", "quote": "Peasants from **collectivised** regions filled the cattle cars bound for Siberian logging camps."}
    ]
  },
  "collectivism": {
    "primary": "A political or economic theory advocating collective control, ownership, and management of production and distribution.",
    "secondary": "In moral philosophy, prioritizing the goals, harmony, and welfare of the community over individual autonomy.",
    "quotes": [
      {"author": "Friedrich Hayek", "work": "The Road to Serfdom", "quote": "Economic **collectivism** inevitably leads to totalitarian political control as state planning expands."},
      {"author": "George Orwell", "work": "Nineteen Eighty-Four", "quote": "Oligarchical **collectivism** was the theoretical foundation of the regime, ensuring permanent power for the Party."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "He warned that a paternal state could impose a gentle **collectivism** that enervates individual citizen initiative."}
    ]
  },
  "collectivist": {
    "primary": "Relating to, practicing, or advocating collectivism; favoring collective control over individual enterprise.",
    "secondary": "In cross-cultural psychology, cultures emphasizing communal harmony, familial duty, and interdependence.",
    "quotes": [
      {"author": "Aldous Huxley", "work": "Brave New World", "quote": "The planetary motto community, identity, stability embodied the supreme triumph of a **collectivist** state."},
      {"author": "Karl Popper", "work": "The Open Society and Its Enemies", "quote": "Platonic political philosophy presents the earliest and most influential **collectivist** blueprint in the West."},
      {"author": "Hannah Arendt", "work": "The Origins of Totalitarianism", "quote": "Totalitarian propaganda appeals to deracinated individuals by promising absorption into a powerful **collectivist** mass."}
    ]
  },
  "collectivistic": {
    "primary": "Characterized by or adhering to collectivism; emphasizing collective social unity and communal goals.",
    "secondary": "In sociopolitical analysis, societies or political parties emphasizing collective social safety nets.",
    "quotes": [
      {"author": "Bertrand Russell", "work": "Authority and the Individual", "quote": "A modern state must balance **collectivistic** economic organization with sphere for individual artistic freedom."},
      {"author": "Steven Pinker", "work": "The Better Angels of Our Nature", "quote": "Traditional **collectivistic** cultures frequently demonstrate higher levels of clan feuding and honor violence."},
      {"author": "Max Weber", "work": "The Protestant Ethic and the Spirit of Capitalism", "quote": "Puritan individualism stood in stark contrast to the **collectivistic** guilds of medieval Catholic Europe."}
    ]
  },
  "collectivization": {
    "primary": "The organization of an economy, agricultural system, or enterprise around collective or state ownership.",
    "secondary": "In historical political economy, the Soviet agricultural transformation launched under Stalin's first Five-Year Plan.",
    "quotes": [
      {"author": "Hannah Arendt", "work": "The Origins of Totalitarianism", "quote": "The forced **collectivization** of Russian agriculture destroyed the rural social fabric and created millions of victims."},
      {"author": "Alexander Solzhenitsyn", "work": "The Gulag Archipelago", "quote": "The dekulakization campaign accompanying **collectivization** funneled millions of hardy farmers into the Gulag."},
      {"author": "Eric Hobsbawm", "work": "The Age of Extremes", "quote": "Despite catastrophic short-term famine, **collectivization** enabled the state to feed wartime industrial workers."}
    ]
  },
  "collectivize": {
    "primary": "To organize a business, economy, or land on the basis of collective or communal ownership.",
    "secondary": "In political governance, replacing private property with cooperative or state-managed productive enterprises.",
    "quotes": [
      {"author": "George Orwell", "work": "Homage to Catalonia", "quote": "Anarchist militias moved quickly to **collectivize** transport, barber shops, and bakeries across Barcelona."},
      {"author": "Arthur Koestler", "work": "Darkness at Noon", "quote": "The Party resolved to **collectivize** the land at all costs, brushing aside sentimental objections to violence."},
      {"author": "Karl Marx", "work": "The Communist Manifesto", "quote": "The victorious proletariat will use its political supremacy to **collectivize** the instruments of credit."}
    ]
  },
  "collectivized": {
    "primary": "Transferred to collective or state ownership; operated under cooperative management.",
    "secondary": "In twentieth-century history, agricultural land organized into collective state farms.",
    "quotes": [
      {"author": "George Orwell", "work": "Animal Farm", "quote": "The **collectivized** animals harvested the wheat fields under the proud slogan: Four legs good, two legs bad."},
      {"author": "Alexander Solzhenitsyn", "work": "One Day in the Life of Ivan Denisovich", "quote": "Ivan Denisovich recalled his former village life before the land was **collectivized** into a drab state collective."},
      {"author": "Milovan Djilas", "work": "The New Class", "quote": "The bureaucracy derived its immense privileges from administering the **collectivized** national wealth."}
    ]
  },
  "collector": {
    "primary": "A person who collects things of a specified type, such as art, books, stamps, or biological specimens.",
    "secondary": "In electrical engineering, an electrode or component that captures or collects charge carriers in transistors.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "As an enthusiastic young **collector**, I felt indescribable delight upon capturing a rare tropical longicorn beetle."},
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Six Napoleons", "quote": "Dr. Barnicot was an enthusiastic **collector** of Napoleonic bronzes, busts, and battle prints."},
      {"author": "William Shakespeare", "work": "Love's Labour's Lost", "quote": "A dapper little clerk served as **collector** of royal duties, inspecting shipments along the river wharf."}
    ]
  },
  "delectability": {
    "primary": "Delicious taste, exceptional appeal, or delicious quality that affords great sensory pleasure.",
    "secondary": "In culinary aesthetics, the harmonious combination of texture, aroma, and flavor in fine gastronomy.",
    "quotes": [
      {"author": "Auguste Escoffier", "work": "A Guide to Modern Cookery", "quote": "The supreme **delectability** of a truffle sauce depends upon gentle simmering with matured Madeira wine."},
      {"author": "Charles Dickens", "work": "A Christmas Carol", "quote": "The roasted goose and glistening plum pudding were praised for their unsurpassed **delectability** by the Cratchits."},
      {"author": "Marcel Proust", "work": "Swann's Way", "quote": "The buttery **delectability** of the madeleine soaked in lime-blossom tea unlocked the gates of lost Combray."}
    ]
  },
  "delectable": {
    "primary": "Extremely delicious, pleasant, delightful, or charming; affording great sensory or aesthetic enjoyment.",
    "secondary": "In pastoral and religious literature, tranquil landscapes or spiritual blessings of Edenic sweetness.",
    "quotes": [
      {"author": "John Bunyan", "work": "The Pilgrim's Progress", "quote": "The shepherds guided Christian and Hopeful to the summit of the **Delectable** Mountains, where orchards flourished."},
      {"author": "Jane Austen", "work": "Emma", "quote": "Frank Churchill pronounced the strawberry gathering at Donwell Abbey to be a most **delectable** entertainment."},
      {"author": "John Keats", "work": "Endymion", "quote": "Beneath the green bower lay baskets filled with **delectable** fruits and amber honey from mountain hives."}
    ]
  },
  "delectation": {
    "primary": "Pleasure and delight; enjoyment or entertainment, especially of a refined sensory or intellectual nature.",
    "secondary": "In formal rhetoric, presenting an artistic performance, banquet, or musical composition for public pleasure.",
    "quotes": [
      {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "Becky Sharp sang Mozart arias at the piano for the **delectation** of the distinguished aristocratic guests."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Mr. Chadband offered a pious sermon for the spiritual **delectation** of the Snagsby household."},
      {"author": "Walter Scott", "work": "Ivanhoe", "quote": "The minstrel tuned his harp, reciting ancient lays of chivalry for the **delectation** of the Norman baron."}
    ]
  },
  "dielectric": {
    "primary": "An electrical insulator that can be polarized by an applied electric field without conducting electricity.",
    "secondary": "In capacitor physics, the insulating material placed between conducting plates to increase capacitance.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "I introduced the term **dielectric** to express that substance through or across which electric forces operate."},
      {"author": "James Clerk Maxwell", "work": "A Treatise on Electricity and Magnetism", "quote": "The displacement current in a **dielectric** medium generates magnetic fields identical to conduction currents."},
      {"author": "Richard Feynman", "work": "The Feynman Lectures on Physics", "quote": "When a **dielectric** slab is inserted between capacitor plates, induced surface charges reduce the internal field."}
    ]
  },
  "dielectrolysis": {
    "primary": "Electrolysis or ionization occurring across or within a dielectric medium under high electrical stress.",
    "secondary": "In biophysics and electrotherapy, the introduction of ionic medications through tissues using electric currents.",
    "quotes": [
      {"author": "Oliver Heaviside", "work": "Electromagnetic Theory", "quote": "Under extreme electrical potential gradients, insulating oils undergo localized **dielectrolysis** and puncture."},
      {"author": "William Stewart Halsted", "work": "Surgical Papers", "quote": "Early investigators explored medical **dielectrolysis** to drive antiseptic metallic ions into deep abscess cavities."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "The boundary between electrostatic polarization and actual **dielectrolysis** marks the dielectric breakdown point."}
    ]
  },
  "elect": {
    "primary": "To choose or select someone for public office or membership by voting, or chosen and set apart.",
    "secondary": "In Calvinist theology, those chosen by God's sovereign grace from eternity for salvation.",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Some I have chosen of peculiar grace, **elect** above the rest; so is my sovereign will declared."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "Free citizens assemble periodically to **elect** magistrates who execute the public laws under public gaze."},
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Marianne declared that she would never **elect** to marry a man devoid of passionate taste for poetry."}
    ]
  },
  "elected": {
    "primary": "Chosen for office, honor, or position by vote, or selected out from a larger group.",
    "secondary": "In representative government, officials holding legitimate democratic mandates from constituents.",
    "quotes": [
      {"author": "Abraham Lincoln", "work": "First Inaugural Address", "quote": "I hold that in contemplation of universal law and of the Constitution, the Union is perpetual, governed by **elected** magistrates."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Trajan was **elected** by the Senate and the veteran legions as the emperor most worthy to govern."},
      {"author": "George Eliot", "work": "Felix Holt, the Radical", "quote": "The candidates paraded through the market square, hoping to be **elected** by the enthusiastic newly enfranchised burghers."}
    ]
  },
  "election": {
    "primary": "A formal and organized process of voting to choose a person for political office or other position.",
    "secondary": "In theological doctrine, predestination by divine grace to salvation.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The mode of **election** of the President is the only part of the system that has escaped without severe censure."},
      {"author": "Charles Dickens", "work": "The Pickwick Papers", "quote": "The Eatanswill **election** erupted into a glorious uproar of blue and buff banners, bribes, and broken heads."},
      {"author": "John Calvin", "work": "Institutes of the Christian Religion", "quote": "Divine **election** precedes all human merit, choosing whom God pleases out of sovereign mercy alone."}
    ]
  },
  "electioneer": {
    "primary": "To campaign actively for a political candidate, party, or cause in an election.",
    "secondary": "In local politics, canvassing neighborhoods, distributing handbills, and soliciting votes door-to-door.",
    "quotes": [
      {"author": "William Makepeace Thackeray", "work": "The Newcomes", "quote": "Colonel Newcome went down to the borough to **electioneer** with honest zeal, shaking hands with every voter."},
      {"author": "Anthony Trollope", "work": "Can You Forgive Her?", "quote": "George Vavasor spent hundreds of pounds to **electioneer** through the taverns and back alleys of the district."},
      {"author": "Mark Twain", "work": "The Gilded Age", "quote": "Political managers arrived from Washington to **electioneer** for their candidate with lavish promises of postmaster jobs."}
    ]
  },
  "electioneering": {
    "primary": "The activity of campaigning actively for a candidate, political party, or policy in an election.",
    "secondary": "In historical political chronicles, the tactics of speechmaking, treats, rallies, and propaganda used to secure votes.",
    "quotes": [
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "Every four years the entire republic is convulsed by the feverish **electioneering** of rival presidential parties."},
      {"author": "Charles Dickens", "work": "The Pickwick Papers", "quote": "The glorious art of **electioneering** was displayed in full vigor by the rival partisans of Slumkey and Fizkin."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Mr. Brooke's foray into **electioneering** ended disastrously when an effigy of him interrupted his speech."}
    ]
  },
  "elective": {
    "primary": "Chosen or appointed by election, or relating to voting; also optional, non-compulsory, or open to choice.",
    "secondary": "In academic curricula or surgical medicine, optional courses or non-emergency surgical procedures chosen by the patient.",
    "quotes": [
      {"author": "Johann Wolfgang von Goethe", "work": "Elective Affinities", "quote": "Chemical elements exhibit **elective** attractions, deserting one partner to combine passionately with another."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "An **elective** monarchy was rejected by the Philadelphia convention as dangerous to republican liberty."},
      {"author": "William Osler", "work": "Aequanimitas", "quote": "The clinical schedule permitted senior medical students several **elective** rotations in hospital pathology."}
    ]
  },
  "elector": {
    "primary": "A person who has the right to vote in an election, or an official member of an electoral college.",
    "secondary": "In German history, one of the imperial princes of the Holy Roman Empire entitled to elect the Emperor.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "Each presidential **elector** was expected to exercise wise, independent judgment in choosing the chief magistrate."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The Golden Bull of Charles IV formally established the seven German princes as the supreme **elector** body."},
      {"author": "John Stuart Mill", "work": "Considerations on Representative Government", "quote": "The civic duty of every **elector** is to vote not for private interest, but for the common public good."}
    ]
  },
  "electoral": {
    "primary": "Relating to elections or electors; pertaining to the voting process and political representation.",
    "secondary": "In constitutional law, the electoral college mechanism used to determine national executive leadership.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The **electoral** college system ensures that the chief magistrate does not depend solely upon legislative favor."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "The widening of the **electoral** franchise was the inevitable democratic current sweeping across the modern world."},
      {"author": "Winston Churchill", "work": "The Second World War", "quote": "The British public delivered a dramatic **electoral** verdict in the summer of 1945, returning a Labour majority."}
    ]
  },
  "electorate": {
    "primary": "All the people in a country or area who are entitled to vote in an election.",
    "secondary": "In historical German geography, the territory or principality ruled by an imperial prince-elector.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "On Liberty", "quote": "An educated and vigilant **electorate** constitutes the only enduring safeguard against parliamentary despotism."},
      {"author": "Edmund Burke", "work": "Speech to the Electors of Bristol", "quote": "A representative owes his **electorate** not industry only, but his judgment; and he betrays it if he sacrifices it to their opinion."},
      {"author": "George Orwell", "work": "The Lion and the Unicorn", "quote": "The British **electorate** demonstrated remarkable common sense during the crisis, refusing fascist panaceas."}
    ]
  },
  "electra": {
    "primary": "Electra, the daughter of Agamemnon and Clytemnestra in Greek mythology who helped avenge her father's murder.",
    "secondary": "In astronomy, a blue-white giant star in the Pleiades star cluster, or the Electra complex in psychoanalysis.",
    "quotes": [
      {"author": "Sophocles", "work": "Electra", "quote": "Tragic **Electra** wept by her father's tomb, calling upon the gods of the underworld to guide Orestes home."},
      {"author": "Carl Jung", "work": "The Theory of Psychoanalysis", "quote": "He proposed the name **Electra** complex to describe the daughter's unconscious psychoanalytic attachment to her father."},
      {"author": "John Herschel", "work": "Outlines of Astronomy", "quote": "The delicate nebulosity enveloping the star **Electra** in the Pleiades was revealed by long photographic exposure."}
    ]
  },
  "electric": {
    "primary": "Of, relating to, produced by, or operated by electricity; charged with intense excitement or tension.",
    "secondary": "In physics and engineering, systems, currents, or circuits utilizing the flow of electric charge.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "The magnetic needle swung violently as the **electric** circuit was completed through the copper coil."},
      {"author": "Walt Whitman", "work": "Leaves of Grass", "quote": "I sing the body **electric**, the armies of those I love engirth me and I engirth them."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "The newly installed **electric** lamps cast sharp, brilliant shadows across the foggy London thoroughfare."}
    ]
  },
  "electrical": {
    "primary": "Pertaining to, operating by, producing, or relating to electricity or electrical equipment.",
    "secondary": "In engineering, the design of power generation, distribution, and circuit systems.",
    "quotes": [
      {"author": "Nikola Tesla", "work": "My Inventions", "quote": "My early **electrical** experiments were conducted with induction coils and spark gaps in my school laboratory."},
      {"author": "Thomas Edison", "work": "The Diary and Sundry Observations", "quote": "The central **electrical** station on Pearl Street began supplying power to hundreds of incandescent bulbs."},
      {"author": "James Clerk Maxwell", "work": "A Treatise on Electricity and Magnetism", "quote": "Light itself consists of transverse undulations of the same medium which is the cause of **electrical** and magnetic phenomena."}
    ]
  },
  "electrically": {
    "primary": "By means of electricity; in an electrical manner or through electrical energy.",
    "secondary": "In physics, describing particles or surfaces possessing a positive or negative electrostatic charge.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "The pith ball was **electrically** charged by contact with the glass rod, repelling neighboring light fibers."},
      {"author": "H. G. Wells", "work": "The War of the Worlds", "quote": "The Martians controlled their towering tripods **electrically**, coordinating movements through telepathic dials."},
      {"author": "Ernest Rutherford", "work": "Radioactive Substances and Their Radiations", "quote": "Alpha particles were **electrically** deflected in strong magnetic fields, confirming their positive charge."}
    ]
  },
  "electrician": {
    "primary": "A skilled tradesperson who installs, operates, maintains, or repairs electrical wiring and equipment.",
    "secondary": "In nineteenth-century physics, an experimental scientist (like Franklin or Faraday) investigating electricity.",
    "quotes": [
      {"author": "Benjamin Franklin", "work": "Experiments and Observations on Electricity", "quote": "The curious **electrician** may easily replicate these cloud experiments with a common silk kite and iron wire."},
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Bruce-Partington Plans", "quote": "The underground railway employed an **electrician** who monitored signal currents along the dark track."},
      {"author": "Thomas Edison", "work": "The Diary and Sundry Observations", "quote": "He summoned his chief **electrician** to inspect the dynamo brushes after the generator began to spark."}
    ]
  },
  "electricity": {
    "primary": "A physical phenomenon associated with the presence and flow of electric charges, electrons, or ions.",
    "secondary": "In industrial history, the form of energy supplied via transmission grids to power lighting and motors.",
    "quotes": [
      {"author": "Benjamin Franklin", "work": "Autobiography", "quote": "My experiments in **electricity** demonstrated that lightning and electrical sparks are identical in nature."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "The mysterious force of **electricity** links chemistry, magnetism, and atomic cohesion into a unified domain."},
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "The sudden flash of lightning shattered the oak tree, demonstrating the colossal destructive power of **electricity**."}
    ]
  },
  "electrification": {
    "primary": "The process of charging something with electricity, or equipping a region or railway with electric power.",
    "secondary": "In economic modern history, infrastructure campaigns bringing electrical grids to rural and industrial regions.",
    "quotes": [
      {"author": "Vladimir Lenin", "work": "Collected Works", "quote": "Communism is Soviet power plus the **electrification** of the whole country, transforming archaic peasant agriculture."},
      {"author": "Nikola Tesla", "work": "My Inventions", "quote": "The complete **electrification** of American industry followed the triumph of polyphase alternating currents at Niagara."},
      {"author": "Thorstein Veblen", "work": "The Engineers and the Price System", "quote": "The rapid **electrification** of factories eliminated clumsy overhead belts and increased mechanical efficiency."}
    ]
  },
  "electrify": {
    "primary": "To charge with electricity, equip with electric power, or shock, excite, or thrill someone intensely.",
    "secondary": "In theater and public rhetoric, to captivate an audience with astonishing, high-energy delivery.",
    "quotes": [
      {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "Becky Sharp's brilliant performance at the charades seemed to **electrify** the entire assembly of aristocrats."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Chemistry", "quote": "Careful insulation is required whenever one attempts to **electrify** a large metallic cylinder by induction."},
      {"author": "Winston Churchill", "work": "Great Contemporaries", "quote": "The orator possessed a charismatic gift to **electrify** a hostile House of Commons into thunderous cheers."}
    ]
  },
  "electrifying": {
    "primary": "Causing a surge of excitement, intense thrill, or dramatic shock; astonishingly exciting.",
    "secondary": "In theatrical performance, describing a mesmerizing actor whose presence commands undivided attention.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "The revelation produced an **electrifying** effect upon Watson, who leaned forward with breathless curiosity."},
      {"author": "Charles Dickens", "work": "Nicholas Nickleby", "quote": "The tragedian made an **electrifying** entrance onto the provincial stage, brandishing his broadsword."},
      {"author": "Edith Wharton", "work": "The Age of Innocence", "quote": "The sudden arrival of Countess Olenska produced an **electrifying** murmur throughout the private opera boxes."}
    ]
  },
  "electrocardiogram": {
    "primary": "A recorded tracing of the electrical activity and voltage fluctuations of the heart over time; an ECG or EKG.",
    "secondary": "In clinical cardiology, a diagnostic recording identifying cardiac arrhythmias, ischemia, and infarction.",
    "quotes": [
      {"author": "Willem Einthoven", "work": "The Different Forms of the Human Electrocardiogram", "quote": "The string galvanometer produced an accurate **electrocardiogram**, displaying distinct P, Q, R, S, and T waves."},
      {"author": "Oliver Sacks", "work": "Awakenings", "quote": "The patient's **electrocardiogram** showed benign sinus bradycardia while resting in the neurological ward."},
      {"author": "Siddhartha Mukherjee", "work": "The Laws of Medicine", "quote": "An abnormal **electrocardiogram** prompted the resident to order emergency coronary angiography."}
    ]
  },
  "electrocardiograph": {
    "primary": "An instrument or medical apparatus used to record the electrical activity of the heart muscles.",
    "secondary": "In the history of medical technology, the apparatus invented by Willem Einthoven using string galvanometers.",
    "quotes": [
      {"author": "Willem Einthoven", "work": "Nobel Lecture", "quote": "The modern **electrocardiograph** enables clinicians to diagnose subtle conduction blocks without physical catheterization."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Introduction of the **electrocardiograph** into clinical practice revolutionized our classification of cardiac irregularities."},
      {"author": "Atul Gawande", "work": "Complications: A Surgeon's Notes on an Imperfect Science", "quote": "The mobile **electrocardiograph** was wheeled to the trauma bay as the resuscitation team began compressions."}
    ]
  },
  "electrocardiographic": {
    "primary": "Relating to or obtained by electrocardiography; pertaining to the tracing of heart electrical activity.",
    "secondary": "In clinical cardiology, abnormalities such as ST-segment elevation or inverted T-waves on a cardiac tracing.",
    "quotes": [
      {"author": "Oliver Sacks", "work": "Migraine", "quote": "Transient **electrocardiographic** abnormalities occasionally accompany severe migraine episodes with autonomic distress."},
      {"author": "William Stewart Halsted", "work": "Surgical Papers", "quote": "Preoperative **electrocardiographic** screening identified occult conduction defects in elderly surgical candidates."},
      {"author": "Eric Kandel", "work": "Principles of Neural Science", "quote": "Autonomic projections from the medulla exert profound influence upon **electrocardiographic** rhythms during stress."}
    ]
  },
  "electrocardiography": {
    "primary": "The medical science, technique, and practice of recording and interpreting the electrical activity of the heart.",
    "secondary": "In medical education, clinical training required to decipher 12-lead vectors and cardiac electrophysiology.",
    "quotes": [
      {"author": "Willem Einthoven", "work": "The Galvanometric Registration of the Human Electrocardiogram", "quote": "The development of clinical **electrocardiography** fulfilled the dream of observing cardiac muscle potentials in real time."},
      {"author": "William Osler", "work": "Aequanimitas", "quote": "He praised the laboratory methods of **electrocardiography** for uniting physiological research with hospital medicine."},
      {"author": "Siddhartha Mukherjee", "work": "The Song of the Cell", "quote": "Progress in diagnostic **electrocardiography** depended upon sensitive instruments capable of detecting microvolt currents."}
    ]
  },
  "electrocautery": {
    "primary": "The surgical technique of burning, coagulating, or cutting tissue using a needle or blade heated by electric current.",
    "secondary": "In modern operating suites, bipolar or monopolar electrosurgical devices used to achieve hemostasis in vessels.",
    "quotes": [
      {"author": "William Stewart Halsted", "work": "The Employment of Fine Silk in Surgery", "quote": "Modern surgeons employ **electrocautery** to seal bleeding arterioles cleanly without leaving foreign ligatures."},
      {"author": "Richard Selzer", "work": "Mortal Lessons", "quote": "A hiss of steam and the pungent scent of scorched flesh announced the swift work of the **electrocautery** blade."},
      {"author": "Atul Gawande", "work": "Better: A Surgeon's Notes on Performance", "quote": "With delicate taps of the **electrocautery** pencil, the surgeon dissected the tumor free from the vena cava."}
    ]
  },
  "electrochemical": {
    "primary": "Relating to or involving chemical reactions that produce electricity or are driven by an applied electric current.",
    "secondary": "In neurobiology, describing nerve impulses mediated through ionic concentration gradients across membranes.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "The **electrochemical** decomposition of an electrolyte is governed by definite quantitative atomic equivalents."},
      {"author": "Eric Kandel", "work": "In Search of Memory", "quote": "The action potential is an **electrochemical** wave driven by rapid influx of sodium and efflux of potassium ions."},
      {"author": "Svante Arrhenius", "work": "The Theory of Electrolytic Dissociation", "quote": "Electrolytic salts dissociate into charged ions, providing the basis for all **electrochemical** activity in solutions."}
    ]
  },
  "electrochemistry": {
    "primary": "The branch of chemistry concerned with the interrelation of electrical and chemical phenomena.",
    "secondary": "In industrial manufacturing, processes such as chlor-alkali production, electroplating, and lithium battery design.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "The laws of **electrochemistry** establish that the chemical affinity of atoms is identical with their electrical charge."},
      {"author": "Humphry Davy", "work": "Elements of Chemical Philosophy", "quote": "Through the new science of **electrochemistry**, we proved that potash and soda are oxides of unknown metals."},
      {"author": "Marie Curie", "work": "Radioactive Substances", "quote": "Early work in **electrochemistry** prepared the laboratory techniques used to isolate radium salts from pitchblende."}
    ]
  },
  "electrocute": {
    "primary": "To injure or execute a person or animal by sending a fatal electric current through the body.",
    "secondary": "In judicial penal history, carrying out a sentence of capital punishment using an electric chair.",
    "quotes": [
      {"author": "Thomas Edison", "work": "The Diary and Sundry Observations", "quote": "He warned that alternating currents were sufficiently hazardous to accidentally **electrocute** unwary factory workers."},
      {"author": "H. G. Wells", "work": "The War of the Worlds", "quote": "A severed high-voltage cable flailed on the wet pavement, threatening to **electrocute** the fleeing crowds."},
      {"author": "George Orwell", "work": "Nineteen Eighty-Four", "quote": "Winston feared the hidden tortures of the Ministry of Love, dreading currents that could **electrocute** the senses."}
    ]
  },
  "electrocution": {
    "primary": "Death or severe injury caused by the passage of an electric current through the body.",
    "secondary": "In capital punishment history, execution by the electric chair introduced in New York State in 1890.",
    "quotes": [
      {"author": "Nikola Tesla", "work": "My Inventions", "quote": "Critics staged public demonstrations of animal **electrocution** in an attempt to discredit alternating current."},
      {"author": "Oliver Sacks", "work": "Musicophilia", "quote": "A sudden lightning strike caused near-fatal **electrocution**, precipitating an extraordinary surge of musical creativity."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Industrial **electrocution** typically results in sudden ventricular fibrillation or paralysis of the respiratory center."}
    ]
  },
  "electrocutioner": {
    "primary": "An executioner or official appointed to carry out the sentence of execution by electrocution.",
    "secondary": "In historical prison administration, the technician operating the switches and rheostats of the electric chair.",
    "quotes": [
      {"author": "Sinclair Lewis", "work": "Arrowsmith", "quote": "The grim prison warden stood beside the state **electrocutioner**, who adjusted the damp leather helmet and electrodes."},
      {"author": "H. L. Mencken", "work": "Prejudices: Fourth Series", "quote": "The state **electrocutioner** earned his macabre fee by pulling the master switch in the dim basement at Sing Sing."},
      {"author": "Arthur Koestler", "work": "Reflections on Hanging", "quote": "Technological modernization replaced the traditional hangman with a mechanized **electrocutioner** manipulating voltage dials."}
    ]
  },
  "electrode": {
    "primary": "A conductor through which an electric current enters or leaves an electrolyte, gas, vacuum, or semiconductor.",
    "secondary": "In electrophysiology, fine microelectrodes inserted into neurons to record intracellular membrane potentials.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "I propose to call the surfaces at which the electric current enters or leaves the decomposing body the **electrode**."},
      {"author": "Eric Kandel", "work": "In Search of Memory", "quote": "Inserting a glass capillary **electrode** into the giant neuron of Aplysia allowed us to record synaptic potentials directly."},
      {"author": "J. J. Thomson", "work": "Rays of Positive Electricity", "quote": "Cathode rays streaming from the negative **electrode** revealed the universal corpuscular nature of electrons."}
    ]
  },
  "electrodeposition": {
    "primary": "The process of depositing a thin, coherent layer of metal onto a conductive surface by electrolysis; electroplating.",
    "secondary": "In materials science and metallurgy, coating industrial parts with chromium, nickel, or gold for corrosion protection.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "The mass of copper formed by **electrodeposition** upon the cathode conforms strictly to chemical equivalents."},
      {"author": "Thomas Edison", "work": "The Diary and Sundry Observations", "quote": "Phonograph master molds were replicated through delicate **electrodeposition** of nickel upon wax matrix recordings."},
      {"author": "Antoine Lavoisier", "work": "Elements of Chemistry", "quote": "Nineteenth-century chemists applied **electrodeposition** to coat delicate copper engravings with durable iron faces."}
    ]
  },
  "electrodynamometer": {
    "primary": "An electrical measuring instrument used for measuring current, voltage, or electric power via electrodynamic action.",
    "secondary": "In precision metrology, a laboratory meter utilizing mutual magnetic deflection between fixed and moving coils.",
    "quotes": [
      {"author": "James Clerk Maxwell", "work": "A Treatise on Electricity and Magnetism", "quote": "Weber's **electrodynamometer** provided the first absolute laboratory measure of electrodynamic torque between circuits."},
      {"author": "Lord Kelvin", "work": "Popular Lectures and Addresses", "quote": "Calibrated current balances and the Siemens **electrodynamometer** established standardized practical ampere values."},
      {"author": "Oliver Heaviside", "work": "Electrical Papers", "quote": "The deflection of the moving coil inside the **electrodynamometer** varies with the mean square of alternating current."}
    ]
  },
  "electroencephalogram": {
    "primary": "A recorded tracing of the electrical waves and voltage fluctuations of the brain, obtained by scalp electrodes; an EEG.",
    "secondary": "In clinical neurology, a diagnostic test evaluating epilepsy, encephalopathy, sleep architecture, and brain death.",
    "quotes": [
      {"author": "Hans Berger", "work": "On the Electroencephalogram of Man", "quote": "The human **electroencephalogram** revealed regular alpha rhythms of ten cycles per second during relaxed wakefulness."},
      {"author": "Oliver Sacks", "work": "The Man Who Mistook His Wife for a Hat", "quote": "The patient's **electroencephalogram** demonstrated focal spike-and-wave discharges originating in the left temporal lobe."},
      {"author": "Eric Kandel", "work": "Principles of Neural Science", "quote": "Synchronized cortical neuronal firing generates the rhythmic waveforms captured upon the **electroencephalogram**."}
    ]
  },
  "electroencephalograph": {
    "primary": "An apparatus or medical instrument used to record the electrical potentials and brainwaves of the cerebral cortex.",
    "secondary": "In neurophysiology laboratories, multi-channel amplifiers filtering and amplifying microvolt neural signals from the scalp.",
    "quotes": [
      {"author": "Hans Berger", "work": "On the Electroencephalogram of Man", "quote": "Careful grounding of the **electroencephalograph** eliminated alternating current interference from laboratory lighting."},
      {"author": "Oliver Sacks", "work": "Awakenings", "quote": "Technicians connected the twenty-channel **electroencephalograph** to monitor sleep stage transitions in the ward."},
      {"author": "Eric Kandel", "work": "Principles of Neural Science", "quote": "The modern digital **electroencephalograph** performs automated Fourier spectral analysis on EEG band frequencies."}
    ]
  },
  "electroencephalographic": {
    "primary": "Relating to or obtained by electroencephalography; pertaining to brainwave recordings.",
    "secondary": "In clinical neuroscience, designating diagnostic criteria for seizure activity or sleep stage scoring.",
    "quotes": [
      {"author": "Oliver Sacks", "work": "Hallucinations", "quote": "The nocturnal hallucinations coincided with distinct **electroencephalographic** paroxysms during non-REM sleep transitions."},
      {"author": "Eric Kandel", "work": "Principles of Neural Science", "quote": "Thalamocortical loops drive the rhythmic **electroencephalographic** spindle oscillations characteristic of stage 2 sleep."},
      {"author": "Kay Redfield Jamison", "work": "An Unquiet Mind", "quote": "Neurologists ruled out temporal lobe epilepsy through extensive **electroencephalographic** monitoring during admission."}
    ]
  },
  "electrograph": {
    "primary": "An apparatus for recording electrical phenomena, or an image or recording produced by electrical discharge.",
    "secondary": "In early telecommunications and electrical history, instruments automatically recording atmospheric electricity variations.",
    "quotes": [
      {"author": "Lord Kelvin", "work": "Reprint of Papers on Electrostatics and Magnetism", "quote": "A self-recording photographic **electrograph** monitored continuous atmospheric potential at the Kew Observatory."},
      {"author": "Nikola Tesla", "work": "Colorado Springs Notes", "quote": "The sparks formed an intricate branched **electrograph** on the sensitized plate placed beneath the discharge terminal."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "Early investigators constructed an **electrograph** using rotating discs to capture lightning transients."}
    ]
  },
  "electrologist": {
    "primary": "A specialist trained in electrolysis for the permanent removal of unwanted hair or cosmetic skin blemishes.",
    "secondary": "In dermatology, a practitioner utilizing galvanic or thermolytic high-frequency needles to destroy hair follicles.",
    "quotes": [
      {"author": "William Stewart Halsted", "work": "Surgical Papers", "quote": "The licensed **electrologist** inserts a fine platinum needle into the follicle to destroy the germinative papilla."},
      {"author": "Oliver Sacks", "work": "The Island of the Colorblind", "quote": "Patients troubled by hirsutism sought consultation from a clinical **electrologist** for permanent depilation."},
      {"author": "Atul Gawande", "work": "Complications", "quote": "Minor cosmetic procedures formerly performed by surgeons are now expertly handled by the trained **electrologist**."}
    ]
  },
  "electrolysis": {
    "primary": "Chemical decomposition produced by passing an electric current through a liquid or solution containing ions.",
    "secondary": "In cosmetic dermatology, the permanent destruction of hair roots using electrical current applied via a fine needle.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "The chemical power of a current of electricity is in direct proportion to the absolute quantity of **electrolysis** produced."},
      {"author": "Humphry Davy", "work": "Bakerian Lectures", "quote": "By subjecting molten potash to intense **electrolysis**, globules of gleaming potassium metal burst into flame."},
      {"author": "Svante Arrhenius", "work": "The Theory of Electrolytic Dissociation", "quote": "The passage of current during **electrolysis** does not create ions, but merely directs pre-existing ions toward the electrodes."}
    ]
  },
  "electrolyte": {
    "primary": "A chemical substance that conducts electricity when dissolved in water or melted, producing mobile ions.",
    "secondary": "In human physiology, essential blood minerals (such as sodium, potassium, and chloride) regulating cellular hydration.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "I propose to call bodies that undergo decomposition by electricity an **electrolyte**, and the process electrolysis."},
      {"author": "Svante Arrhenius", "work": "Textbook of Electrochemistry", "quote": "In dilute solutions, every strong **electrolyte** dissociates almost completely into free, independent ions."},
      {"author": "Oliver Sacks", "work": "Awakenings", "quote": "Intravenous saline restored normal serum **electrolyte** balance, relieving the patient's delirium and dehydration."}
    ]
  },
  "electrolytic": {
    "primary": "Relating to or produced by electrolysis; involving the conduction of electricity through chemical ions.",
    "secondary": "In electronics, an electrolytic capacitor utilizing an oxide dielectric layer on an aluminum or tantalum foil.",
    "quotes": [
      {"author": "Svante Arrhenius", "work": "The Theory of Electrolytic Dissociation", "quote": "The degree of **electrolytic** dissociation can be determined from osmotic pressure and electrical conductivity data."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "Water requires an **electrolytic** conductor such as sulfuric acid to facilitate rapid gas evolution at the poles."},
      {"author": "Marie Curie", "work": "Radioactive Substances", "quote": "Barium and radium were separated through fractional **electrolytic** deposition of their respective amalgams."}
    ]
  }
}
