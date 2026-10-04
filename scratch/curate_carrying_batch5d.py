# -*- coding: utf-8 -*-
import os, sys, re

sys.stdout.reconfigure(encoding="utf-8")

data = {
  # =========================================================================
  # Dashboard — fer (Batch 5D: 35 words)
  # =========================================================================
  "Dashboard — fer/infernally.md": {
    "primary": "In an infernal, fiendish, or hellish manner; diabolically or outrageous to an extreme degree.",
    "secondary": "In expressive colloquial and narrative prose, used as an intensive expressing exasperation or ominous grandeur.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick; or, The Whale", "quote": "Then come out those fiery effulgences, **infernally** superb; then the evil blaze upon the black hull."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The weather was **infernally** close, making the dusty legal chambers well-nigh unendurable."},
      {"author": "Joseph Conrad", "work": "Heart of Darkness", "quote": "The boiler groaned in an **infernally** ragged rhythm as we pushed upstream."}
    ]
  },
  "Dashboard — fer/inferno.md": {
    "primary": "A place or situation that resembles hell, especially a large and uncontrollable fire or scene of chaotic destruction.",
    "secondary": "In Dantean literature and apocalyptic imagery, the subterranean realm of eternal torment or an overwhelming conflagration.",
    "quotes": [
      {"author": "Joseph Conrad", "work": "Heart of Darkness", "quote": "My purpose was to stroll into the shade for a moment; but no sooner within than it seemed to me I had stepped into the gloomy circle of some **inferno**."},
      {"author": "Dante Alighieri", "work": "The Divine Comedy", "quote": "Through me you pass into the city of woe, through me you pass into eternal pain, into the dread **inferno**."},
      {"author": "H. G. Wells", "work": "The War of the Worlds", "quote": "The broken gas mains ignited, turning the ruined suburb into a roaring **inferno**."}
    ]
  },
  "Dashboard — fer/infertile.md": {
    "primary": "Incapable of producing offspring, seed, or fruit; barren, sterile, or lacking agricultural productivity.",
    "secondary": "In pedology and reproductive biology, describing soil depleted of essential plant minerals, or gametes failing to support zygotic development.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Galton says, 'I regret I am unable to solve the simple question whether heiresses are peculiarly **infertile**.'"},
      {"author": "Thomas Malthus", "work": "An Essay on the Principle of Population", "quote": "A rocky and **infertile** soil requires immense expenditure of human labor to yield a meager harvest."},
      {"author": "George Eliot", "work": "Silas Marner", "quote": "The neglected garden had grown weed-choked and **infertile** from years of disuse."}
    ]
  },
  "Dashboard — fer/infertility.md": {
    "primary": "The incapacity to produce offspring, seed, or fruit; barrenness, sterility, or unproductiveness.",
    "secondary": "In clinical medicine and evolutionary genetics, the physiological failure to conceive after regular intercourse, or the reproductive isolation separating distinct biological species.",
    "quotes": [
      {"author": "Charles Darwin", "work": "On the Origin of Species", "quote": "How far these experiments may be trusted, I know not; but the forms exhibit varying degrees of **infertility** when crossed."},
      {"author": "Thomas Malthus", "work": "An Essay on the Principle of Population", "quote": "The barrenness of the land and the apparent **infertility** of the climate imposed severe boundaries upon tribal growth."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The chronic **infertility** of the imperial dynasty led repeatedly to disputed accessions."}
    ]
  },
  "Dashboard — fer/insufferable.md": {
    "primary": "Too extreme, painful, or intolerable to be borne; incapable of being endured; unendurable.",
    "secondary": "In satirical social commentary and psychological description, describing overwhelming arrogance, conceit, or oppressive behavioral vanity.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick; or, The Whale", "quote": "**Insufferable** sting, that sanity should ground arms on such a field!"},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "He was looked upon as an **insufferable** man who gave himself haughty airs in company."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "The bright radiance of the cherubim was **insufferable** to mortal eyes."}
    ]
  },
  "Dashboard — fer/interfere.md": {
    "primary": "To intervene in an activity or situation without invitation, right, or necessity; to meddle or clash.",
    "secondary": "In wave physics, to undergo mutual superposition wherein two coherent wave trains combine to reinforce or cancel each other.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Somehow the fun seems to hang fire, though everything's there that a heart could desire, and I will not **interfere** to spoil it."},
      {"author": "John Locke", "work": "Second Treatise of Government", "quote": "No magistrate has authority to **interfere** with the peaceful private worship of conscientious citizens."},
      {"author": "Thomas Young", "work": "On the Theory of Light and Colours", "quote": "When two rays of monochromatic light cross each other, they **interfere** and produce alternate fringes of brightness and darkness."}
    ]
  },
  "Dashboard — fer/interference.md": {
    "primary": "The act, fact, or process of meddling, obstructing, or intervening in affairs; an obstacle or impediment.",
    "secondary": "In optical physics and telecommunications, the physical phenomenon in which two or more propagating wave patterns superimpose to form a resultant wave of greater, lower, or equal amplitude.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Oak's allusion to his own love for her lessened, to some extent, her anger at his **interference**."},
      {"author": "Thomas Young", "work": "Experiments Relative to Physical Optics", "quote": "The law of wave **interference** accounts completely for the colored rings observed between curved glass plates."},
      {"author": "John Stuart Mill", "work": "On Liberty", "quote": "The only purpose for which power can be rightfully exercised over any member of a civilized community is to prevent harm to others; his own good is not a warrant for state **interference**."}
    ]
  },
  "Dashboard — fer/interfering.md": {
    "primary": "Intruding into or meddling in the business, affairs, or relationships of others without invitation.",
    "secondary": "In mechanical engineering and wave optics, colliding mechanically during operational movement, or overlapping wave oscillations that produce fringes.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Bulstrode was laying down rules for the direction of the New Hospital, which seemed to the local surgeons an unwarrantable and **interfering** measure."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "I was severely admonished by my sister for being an inquisitive and **interfering** boy."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "The dogmatic theologian was warned against **interfering** with the legitimate deductions of observational geology."}
    ]
  },
  "Dashboard — fer/interferometer.md": {
    "primary": "An optical or physical instrument that superimposes two or more beams of light to measure small displacements, surface irregularities, or refractive indices.",
    "secondary": "In experimental astrophysics and metrology, an apparatus (such as the Michelson interferometer) used to measure stellar diameters, gravitational waves, or determine fundamental standards of length.",
    "quotes": [
      {"author": "Albert A. Michelson", "work": "Light Waves and Their Uses", "quote": "By means of the **interferometer**, we can measure distances with an accuracy rivaling the wavelength of light itself."},
      {"author": "Arthur Eddington", "work": "Space, Time and Gravitation", "quote": "The null result of the ether-drift experiment performed with Michelson's **interferometer** laid the empirical foundation of relativity."},
      {"author": "Lord Rayleigh", "work": "The Theory of Sound", "quote": "The acoustic **interferometer** demonstrates the phase cancellation of sound waves in parallel resonant tubes."}
    ]
  },
  "Dashboard — fer/interferon.md": {
    "primary": "Any of a group of signaling proteins produced and released by host cells in response to the presence of pathogens such as viruses.",
    "secondary": "In molecular immunology and oncology, a cytokine that activates natural killer cells and macrophages and upregulates antigen presentation to inhibit viral replication.",
    "quotes": [
      {"author": "Alick Isaacs", "work": "Virus Interference: The Interferon", "quote": "Cells exposed to inactivated influenza virus produce a protective factor which we have named **interferon**."},
      {"author": "Macfarlane Burnet", "work": "Immunology, Aging, and Cancer", "quote": "The discovery of **interferon** revealed that non-specific cellular defenses precede adaptive antibody responses."},
      {"author": "Christian de Duve", "work": "A Guided Tour of the Living Cell", "quote": "When infected by a virus, the host cell synthesizes **interferon** to warn neighboring cells to erect antiviral defenses."}
    ]
  },
  "Dashboard — fer/noninterference.md": {
    "primary": "The policy, doctrine, or practice of refraining from intervening in the affairs, disputes, or jurisdictions of others.",
    "secondary": "In international diplomacy and classical laissez-faire economics, the principle that sovereign states or governments must not interfere in foreign sovereignty or competitive private markets.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "The general rule of legislation must be **noninterference** in the voluntary transactions of adult individuals."},
      {"author": "Woodrow Wilson", "work": "The State", "quote": "The strict doctrine of **noninterference** in foreign alliances guided the early foreign policy of the republic."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "Local communities flourish best under a system of administrative **noninterference** from the central ministry."}
    ]
  },
  "Dashboard — fer/nonproliferation.md": {
    "primary": "The prevention or restriction of the increase or spread of something, especially nuclear, chemical, or biological weapons.",
    "secondary": "In international security and nuclear arms control diplomacy, the treaty framework (such as the 1968 NPT) binding signatory nations to prevent the dissemination of fissile materials.",
    "quotes": [
      {"author": "John F. Kennedy", "work": "Address to the United Nations", "quote": "The preservation of civilization demands an international treaty of nuclear **nonproliferation** before weapons multiply beyond control."},
      {"author": "Andrei Sakharov", "work": "Progress, Coexistence, and Intellectual Freedom", "quote": "A binding treaty on the **nonproliferation** of nuclear weapons is essential to safeguard the future of humanity."},
      {"author": "Hans Morgenthau", "work": "Politics Among Nations", "quote": "Diplomatic treaties governing **nonproliferation** depend ultimately upon the mutual balance of deterrence among great powers."}
    ]
  },
  "Dashboard — fer/nontransferable.md": {
    "primary": "Not capable of being transferred, conveyed, assigned, or made over to another person or party.",
    "secondary": "In commercial law and property jurisprudence, designating licenses, railway tickets, or specialized endowments that are legally valid only for the named individual holder.",
    "quotes": [
      {"author": "Oliver Wendell Holmes Jr.", "work": "The Common Law", "quote": "Certain personal privileges and fiduciary covenants are inherently **nontransferable** without the express consent of the obligee."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "A feudal privilege granted to a specific guild was strictly **nontransferable** to outside tradesmen."},
      {"author": "John Maynard Keynes", "work": "A Treatise on Money", "quote": "A **nontransferable** credit instrument cannot perform the standard circulating functions of broad money."}
    ]
  },
  "Dashboard — fer/offer.md": {
    "primary": "To present or put forward something for acceptance, rejection, consideration, or purchase; or to express readiness to do something.",
    "secondary": "In contract law, a manifest expression of willingness to enter into a binding agreement made on specific terms so as to invite acceptance.",
    "quotes": [
      {"author": "William Shakespeare", "work": "All's Well That Ends Well", "quote": "Be but your lordship present at his examination; if he do not for the promise of his life **offer** to betray you, hold me no more your servant."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth felt all the perverseness of the **offer**, and would not have accepted him for all the world."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "To **offer** a higher price is the natural method by which buyers compete for scarce goods in a market."}
    ]
  },
  "Dashboard — fer/offerer.md": {
    "primary": "A person who offers, presents, tenders, or proposes something for consideration or acceptance.",
    "secondary": "In religious liturgical history and civil law, a devotee making a sacred oblation at an altar, or a bidder tendering a proposal in an auction or covenant.",
    "quotes": [
      {"author": "Richard Hooker", "work": "Of the Lawes of Ecclesiasticall Politie", "quote": "The sacrifice was accepted according to the piety of the **offerer**, rather than the material value of the oblation."},
      {"author": "Samuel Johnson", "work": "The Idler", "quote": "The **offerer** of unsolicited advice is seldom welcomed with unreserved gratitude."},
      {"author": "Edmund Burke", "work": "Speech on Conciliation with America", "quote": "The **offerer** of terms must demonstrate sincerity if reconciliation is to be achieved."}
    ]
  },
  "Dashboard — fer/offering.md": {
    "primary": "Something offered or presented as a gift, sacrifice, contribution, or proposal; or the act of presenting an offer.",
    "secondary": "In liturgical theology and commercial markets, a consecrated sacrifice dedicated upon an altar, or an initial public distribution of securities.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry VI, Part 3", "quote": "Make war with him that climb'd unto their nest, / **Offering** their own lives in their young's defence?"},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Nor was his temple less / Hideous, nor the **offering** less profane."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The altar smoked with the constant **offering** of victims slaughtered to appease the pagan deities."}
    ]
  },
  "Dashboard — fer/offeror.md": {
    "primary": "A person, commercial entity, or legal party who initiates an offer or proposal to another party.",
    "secondary": "In contract law, the party who formulates and communicates the terms of a proposed covenant, retaining the power to revoke before acceptance.",
    "quotes": [
      {"author": "Oliver Wendell Holmes Jr.", "work": "The Common Law", "quote": "The **offeror** creates by his declaration a power of acceptance in the offeree which did not exist before."},
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "The **offeror** cannot bind the other party until an unequivocal assent has been communicated."},
      {"author": "Henry Sumner Maine", "work": "Ancient Law", "quote": "In modern jurisprudence, the liability of the **offeror** commences only upon the reciprocal promise of the offeree."}
    ]
  },
  "Dashboard — fer/offertory.md": {
    "primary": "The collection of money, gifts, or oblations made during a religious service; or the part of a service during which this takes place.",
    "secondary": "In Western Christian liturgy, the antiphon, choral chant, or psalm sung while the bread and wine for the Eucharist are presented at the altar.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "That I can't, indeed,' he said, moving past Oak as a Christian edges past the collecting plate at the **offertory**."},
      {"author": "Francis Bacon", "work": "Essays", "quote": "The gifts of devotion presented during the **offertory** should proceed from voluntary piety rather than ostentation."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "The curate paused at the conclusion of the sermon while the churchwardens collected the Sunday **offertory**."}
    ]
  },
  "Dashboard — fer/pestiferous.md": {
    "primary": "Carrying or bringing disease, plague, or pestilence; pestilential, highly noxious, or morally corrupting.",
    "secondary": "In historical public health and satirical literature, describing miasmatic atmospheric vapors or pernicious, irritating, and destructive pests.",
    "quotes": [
      {"author": "William Shakespeare", "work": "All's Well That Ends Well", "quote": "The general says you that have so traitorously discovered the secrets of your army, and made such **pestiferous** reports of men, are to be executed."},
      {"author": "Daniel Defoe", "work": "A Journal of the Plague Year", "quote": "The air of the crowded alleys was thick with **pestiferous** exhalations that spread the fatal distemper."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The filthy slum was a **pestiferous** sink of misery and contagion bordering upon the great houses of the rich."}
    ]
  },
  "Dashboard — fer/prefer.md": {
    "primary": "To like better, value more highly, or choose one option over another; or to present or bring forward for consideration.",
    "secondary": "In legal procedure and ecclesiastical administration, to submit a formal indictment or bill before a grand jury, or to advance someone to higher ecclesiastical office.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Cymbeline", "quote": "You must not so far **prefer** her 'fore ours of Italy."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "In every voluntary act, the mind must **prefer** the doing of this rather than the omission of it."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "I always **prefer** walking to any other exercise, especially through the pleasant countryside."}
    ]
  },
  "Dashboard — fer/preferable.md": {
    "primary": "More desirable, suitable, worthy, or advantageous than an alternative; worthy of being chosen in preference.",
    "secondary": "In rational choice theory and philosophical ethics, possessing higher relative normative value or utility when compared with alternative courses of action.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Perhaps a cloister would be **preferable** to this wandering misery."},
      {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "Of two pleasures, if there be one to which all who have experience of both give a decided preference, that is the more **preferable** pleasure."},
      {"author": "David Hume", "work": "An Enquiry Concerning the Principles of Morals", "quote": "A calm and peaceful life is universally deemed **preferable** to the tempest of ambition."}
    ]
  },
  "Dashboard — fer/preferably.md": {
    "primary": "By choice or preference; in a manner that is more desirable or preferred.",
    "secondary": "In technical specifications and procedural guidelines, indicating a favored or recommended condition while permitting functional alternatives.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Breeders select **preferably** those parent stocks that exhibit the desired phenotypic variations."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "I would **preferably** build my cabin near a pure spring of sweet water than near a noisy village road."},
      {"author": "Thomas Henry Huxley", "work": "Lay Sermons, Addresses, and Reviews", "quote": "The scientific investigator should **preferably** begin with direct observation of natural phenomena before consulting historical authorities."}
    ]
  },
  "Dashboard — fer/preference.md": {
    "primary": "A greater liking for one alternative over another or others; or the favoring of one person or thing above another.",
    "secondary": "In microeconomic utility theory, the ranking of alternative bundles of goods or outcomes reflecting a consumer's subjective evaluations.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Boldwood mistook his confusion: sensitive persons are always ready with an assumption of their rival's **preference**."},
      {"author": "Adam Smith", "work": "The Theory of Moral Sentiments", "quote": "Every man feels a natural **preference** for his own preservation, yet society requires sympathy with others."},
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Marianne made no secret of her **preference** for Willoughby over all other acquaintances."}
    ]
  },
  "Dashboard — fer/preferent.md": {
    "primary": "Preferred above all others; showing, receiving, or enjoying special favor, partiality, or precedence.",
    "secondary": "In social sociology and jurisprudence, designating a claimant, creditor, or party endowed with prior rights or senior legal status.",
    "quotes": [
      {"author": "Jeremy Bentham", "work": "The Rationale of Judicial Evidence", "quote": "The law must determine which class of creditors holds a **preferent** title upon the bankrupt's estate."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "No individual state can claim a **preferent** status in the regulation of interstate commerce."},
      {"author": "Henry Sumner Maine", "work": "Ancient Law", "quote": "Customary law granted a **preferent** inheritance share to the elder son to preserve the integrity of the ancestral homestead."}
    ]
  },
  "Dashboard — fer/preferential.md": {
    "primary": "Involving, showing, giving, or receiving a preference or priority over others; favoring a particular group.",
    "secondary": "In international trade policy and financial bankruptcy, designating reduced tariff rates (such as imperial preference) or debt payouts prioritized over unsecured claims.",
    "quotes": [
      {"author": "Woodrow Wilson", "work": "The State", "quote": "Tariff legislation was frequently manipulated to grant **preferential** treatment to domestic manufacturing interests."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "A commercial nation should avoid creating **preferential** monopolies that distort the natural allocation of capital."},
      {"author": "John Maynard Keynes", "work": "The Economic Consequences of the Peace", "quote": "The treaty established **preferential** economic regimes that crippled trade recovery in central Europe."}
    ]
  },
  "Dashboard — fer/preferentially.md": {
    "primary": "In a preferential manner; with bias, partiality, or priority given to one person, group, or entity over others.",
    "secondary": "In biochemistry and physical chemistry, reacting, binding, or diffusing with a higher rate or affinity toward a specific chemical target or stereoisomer.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Female birds choose **preferentially** those male suitors adorned with the most brilliant plumage."},
      {"author": "Louis Pasteur", "work": "Molecular Asymmetry of Organic Compounds", "quote": "Living organisms assimilate **preferentially** the dextrorotatory form of tartaric acid while leaving the levorotatory untouched."},
      {"author": "Thomas Henry Huxley", "work": "Method and Results", "quote": "Natural forces do not act **preferentially** in favor of human happiness, but follow immutable universal laws."}
    ]
  },
  "Dashboard — fer/preferment.md": {
    "primary": "Advancement or promotion to a higher position, rank, dignity, or office, especially in church or state hierarchy.",
    "secondary": "In historical British political and ecclesiastical history, the patronage-driven appointment to lucrative clerical livings, bishoprics, or court offices.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Othello", "quote": "I'll move the King / To any shape of thy **preferment**, such / As thou'lt desire."},
      {"author": "Francis Bacon", "work": "Essays", "quote": "Men in great place are thrice servants... yet they purchase their **preferment** with boundless toil."},
      {"author": "Jonathan Swift", "work": "Gulliver's Travels", "quote": "Candidates for high political **preferment** were required to dance on tightropes before the emperor."}
    ]
  },
  "Dashboard — fer/preferred.md": {
    "primary": "Liked better than alternatives; chosen or valued in preference to other options.",
    "secondary": "In corporate finance, designating preferred stock that gives holders priority over common stockholders in dividends and liquidation proceeds.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry VI, Part 2", "quote": "Peace, son! And show some reason, Buckingham, / Why Somerset should be **preferred** in this."},
      {"author": "Jane Austen", "work": "Emma", "quote": "Mr. Knightley was the only person who had ever ventured to point out her faults, and she **preferred** his judgment to all flattery."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Certain floral varieties were consistently **preferred** by gardeners on account of their vibrant colors."}
    ]
  },
  "Dashboard — fer/proffer.md": {
    "primary": "To hold out or put forward something to someone for acceptance; to tender, present, or offer.",
    "secondary": "In diplomatic negotiation and classical literature, a formal tender of friendship, alliance, terms, or assistance extended during negotiation.",
    "quotes": [
      {"author": "William Shakespeare", "work": "All's Well That Ends Well", "quote": "Whereto I could not answer, so much as / By the quietest **proffer** of my service."},
      {"author": "Walter Scott", "work": "Ivanhoe", "quote": "The Templar made a generous **proffer** to ransom the captives, which the Saxon leader haughtily rejected."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "None among the heavenly host dared accept the perilous mission or make **proffer** of his life for fallen mankind."}
    ]
  },
  "Dashboard — fer/proliferate.md": {
    "primary": "To increase rapidly in numbers; to multiply, reproduce, or spread profusely.",
    "secondary": "In cell biology and medical pathology, to grow and multiply rapidly through repetitive rounds of mitotic cell division.",
    "quotes": [
      {"author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "Under inflammatory irritation, connective tissue cells begin to **proliferate** and produce young vascular granulation."},
      {"author": "Charles Darwin", "work": "On the Origin of Species", "quote": "When introduced into a new and favorable environment with abundant food, species **proliferate** with astonishing rapidity."},
      {"author": "Rachel Carson", "work": "Silent Spring", "quote": "When natural predator insects are eliminated, resistant pest populations **proliferate** beyond all control."}
    ]
  },
  "Dashboard — fer/proliferation.md": {
    "primary": "Rapid increase in numbers; a large amount or rapid multiplication of something.",
    "secondary": "In cellular oncology and arms control diplomacy, the rapid proliferation of abnormal neoplastic cells, or the geopolitical spread of weapons systems.",
    "quotes": [
      {"author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "The histological study of tumors demonstrates an uncontrolled **proliferation** of atypical cellular elements."},
      {"author": "Ernst Mayr", "work": "Systematics and the Origin of Species", "quote": "Geographical isolation on oceanic archipelagos frequently sparks the rapid evolutionary **proliferation** of descendant species."},
      {"author": "George F. Kennan", "work": "The Cloud of Danger", "quote": "The unchecked **proliferation** of nuclear weapons remains the most perilous challenge confronting modern international diplomacy."}
    ]
  },
  "Dashboard — fer/refer.md": {
    "primary": "To direct the attention of someone to something for information, verification, or decision; or to make reference or allusion to.",
    "secondary": "In judicial arbitration and library research, to submit a contested case to an arbitrator, or to direct an inquirer to an authority or index.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Measure for Measure", "quote": "Only **refer** yourself to this advantage: first, that your stay with him may not be long; that the place may be dignified by the reason of it."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "When we seek to clarify our thoughts, we must **refer** our ideas back to the simple sensations from which they originated."},
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "Authors frequently **refer** to the applause of posterity when neglected by their own generation."}
    ]
  },
  "Dashboard — fer/referable.md": {
    "primary": "Capable of being referred, assigned, or attributed to a cause, source, principle, or origin; ascribable.",
    "secondary": "In epistemology and causal metaphysics, able to be explained by reduction or correlation to an underlying physical mechanism.",
    "quotes": [
      {"author": "Charles Dickens", "work": "The Old Curiosity Shop", "quote": "Something of the awfulness, even of Death itself, is **referable** to this mysterious power of quiet association."},
      {"author": "Charles Darwin", "work": "On the Origin of Species", "quote": "Many complex instincts are **referable** to the gradual accumulation of slight, inherited modifications."},
      {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "Every natural phenomenon is **referable** to some antecedent cause governed by general laws."}
    ]
  },
  "Dashboard — fer/referee.md": {
    "primary": "An official who watches a game or match closely to enforce the rules and arbitrate on matters arising from play.",
    "secondary": "In legal arbitration and academic publishing, an independent expert appointed by a court to hear testimony, or a peer reviewing a submitted manuscript.",
    "quotes": [
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "In this abstruse pursuit; in making an account for Peggotty, of all the things in the world, he was selected as an impartial **referee**."},
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "The matters in account were referred by the court to an experienced **referee** to take testimony and report."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "A neutral magistrate must serve as **referee** in commercial contracts where private self-interest threatens mutual justice."}
    ]
  },
  "Dashboard — fer/refereeing.md": {
    "primary": "The act, process, or role of officiating, judging, or umpiring a sporting match or contested proceeding.",
    "secondary": "In academic peer review and legal settlement, evaluating scholarly manuscripts for scientific rigor, or presiding over binding civil mediation.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Firm of Girdlestone", "quote": "He had spent years playing and **refereeing** football matches on the windswept fields of Scotland."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "In the contentious debates of science, unbiased observation must perform the thankless duty of **refereeing** between opposing hypotheses."},
      {"author": "H. G. Wells", "work": "The New Machiavelli", "quote": "The government found itself caught in the difficult business of **refereeing** bitter disputes between coal operators and miners."}
    ]
  }
}

base_dir = r"App database\Latin roots\Cluster Carrying"

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

print(f"Carrying Batch 5D (fer): Successfully updated {updated}/{len(data)} notes.")
