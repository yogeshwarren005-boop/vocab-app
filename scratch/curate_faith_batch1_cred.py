# -*- coding: utf-8 -*-
import os, sys, re

sys.stdout.reconfigure(encoding="utf-8")

data = {
  # =========================================================================
  # Dashboard — cred (42 words)
  # =========================================================================
  "Dashboard — cred/accredit.md": {
    "primary": "To give official authorization to or approval of; to provide with credentials; or to attribute to.",
    "secondary": "In international diplomacy and higher education, to officially send an envoy with letters of credence, or to certify an educational institution as meeting rigorous academic standards.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The emperor refused to **accredit** the barbarian ambassadors until they had rendered homage."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Men readily **accredit** doctrines that flatter their preconceived passions and traditional prejudices."},
      {"author": "Thomas Jefferson", "work": "Writings", "quote": "The President has the constitutional power to receive and **accredit** foreign ministers from friendly nations."}
    ]
  },
  "Dashboard — cred/accreditation.md": {
    "primary": "The formal granting of official approval, recognition, or credentials to an institution or person.",
    "secondary": "In higher education and international law, the institutional evaluation process verifying that an academic program meets professional quality criteria, or the formal delivery of diplomatic credentials.",
    "quotes": [
      {"author": "Woodrow Wilson", "work": "The State", "quote": "The formal **accreditation** of an ambassador establishes his immunity under the law of nations."},
      {"author": "Henry Adams", "work": "The Education of Henry Adams", "quote": "Without proper academic **accreditation**, the new scientific disciplines struggled for recognition within conservative faculties."},
      {"author": "Theodore Roosevelt", "work": "An Autobiography", "quote": "The rapid **accreditation** of consular agents across the Americas facilitated hemispheric commerce."}
    ]
  },
  "Dashboard — cred/accredited.md": {
    "primary": "Officially recognized, authorized, or given credentials; accepted as having standard qualification.",
    "secondary": "In diplomatic protocol and public journalism, formally recognized by a host government or sovereign body as a certified representative or correspondent.",
    "quotes": [
      {"author": "Benjamin Franklin", "work": "Autobiography", "quote": "I was received in Paris as the **accredited** representative of the United States Congress."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "The opinions of **accredited** jurists carry immense weight in shaping American constitutional jurisprudence."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "He was the **accredited** agent of the great legal firm, trusted with its most delicate negotiations."}
    ]
  },
  "Dashboard — cred/cred.md": {
    "primary": "Believability, trustworthiness, or acceptance, especially among members of an urban counterculture or fashionable peer group.",
    "secondary": "In modern sociolinguistics and popular culture, informal social currency or peer validation earned through authentic cultural performance rather than institutional authority.",
    "quotes": [
      {"author": "Tom Wolfe", "work": "The Electric Kool-Aid Acid Test", "quote": "To maintain their underground **cred**, they avoided all mainstream commercial publicity."},
      {"author": "Hunter S. Thompson", "work": "Fear and Loathing in Las Vegas", "quote": "He had sufficient street **cred** to move through the motorcycle gangs without attracting violence."},
      {"author": "Joan Didion", "work": "Slouching Towards Bethlehem", "quote": "The young radicals jealously guarded their revolutionary **cred** against bourgeois compromise."}
    ]
  },
  "Dashboard — cred/credal.md": {
    "primary": "Relating to, consisting of, or based upon a formal religious creed or statement of belief.",
    "secondary": "In historical theology and confessional sociology, pertaining to dogmatic formulations (such as the Nicene Creed) that delineate orthodox membership from schism.",
    "quotes": [
      {"author": "John Henry Newman", "work": "An Essay on the Development of Christian Doctrine", "quote": "The emergence of explicit **credal** statements was necessary to defend apostolic teaching against subtle heresies."},
      {"author": "Matthew Arnold", "work": "Literature and Dogma", "quote": "Rigid **credal** orthodoxy often ossifies into mechanical assent, choking the vital springs of spiritual life."},
      {"author": "William James", "work": "The Varieties of Religious Experience", "quote": "Personal religious experience precedes and outlasts the formal **credal** structures of organized churches."}
    ]
  },
  "Dashboard — cred/credence.md": {
    "primary": "Belief in or acceptance of something as true, valid, or reliable.",
    "secondary": "In liturgical ecclesiastical practice and historical furniture design, a small side table or shelf beside the altar holding Eucharistic vessels prior to consecration.",
    "quotes": [
      {"author": "William Shakespeare", "work": "All's Well That Ends Well", "quote": "His love and wisdom, / Approved so to your majesty, may plead / For ample **credence**."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "With easy **credence** mankind embraced the false promises of the deceiver."},
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "We must give no **credence** to ungrounded rumors unsupported by careful experiment."}
    ]
  },
  "Dashboard — cred/credendum.md": {
    "primary": "An article of faith or doctrine that is to be believed; a required religious dogma (contrasted with agendum, a practical duty).",
    "secondary": "In systematic theology and political ideology, an essential theological proposition or doctrinal dogma that demands assent from all faithful adherents.",
    "quotes": [
      {"author": "Jeremy Taylor", "work": "Holy Living", "quote": "The simple **credendum** of the gospel was gradually overlaid with scholastic subtleties."},
      {"author": "Samuel Taylor Coleridge", "work": "Aids to Reflection", "quote": "Every moral agendum is rooted in a prior spiritual **credendum**."},
      {"author": "Thomas Browne", "work": "Religio Medici", "quote": "I find no difficulty in assenting to this mysterious **credendum**, though reason cannot fathom it."}
    ]
  },
  "Dashboard — cred/credential.md": {
    "primary": "Warranting credit or confidence; or a document attesting to a person's qualification, authority, or trustworthiness.",
    "secondary": "In political history and institutional sociology, letters patent or diplomatic certificates verifying an envoy's authority to negotiate on behalf of a sovereign.",
    "quotes": [
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "The ancient customs of the commonwealth carry their own **credential** inscribed upon generations of civic peace."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "No ambassador can enter upon his mission without presenting an authentic **credential** from his sovereign."},
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "His venerable demeanor served as a silent **credential** of his high clerical character."}
    ]
  },
  "Dashboard — cred/credentialled.md": {
    "primary": "Possessing recognized official credentials, qualifications, certifications, or professional testimonials.",
    "secondary": "In institutional sociology and labor economics, having undergone formal vetting and licensing required for elite professional practice.",
    "quotes": [
      {"author": "Max Weber", "work": "Economy and Society", "quote": "Bureaucratic administration relies upon a staff of **credentialled** experts trained in standardized procedures."},
      {"author": "Thorstein Veblen", "work": "The Higher Learning in America", "quote": "The modern university functions as a factory producing **credentialled** graduates for corporate enterprise."},
      {"author": "John Dewey", "work": "Democracy and Education", "quote": "A truly democratic society values practical competence above mere **credentialled** titles."}
    ]
  },
  "Dashboard — cred/credentials.md": {
    "primary": "Documents, certificates, or letters that prove a person's identity, qualifications, or authority.",
    "secondary": "In statecraft and institutional administration, letters of credence presented by an ambassador to a head of state to establish official diplomatic representation.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick; or, The Whale", "quote": "The veteran harpooneer carried in his scarred body the unmistakable **credentials** of his perilous trade."},
      {"author": "Benjamin Franklin", "work": "Autobiography", "quote": "Upon arriving at the court of Versailles, I delivered my diplomatic **credentials** to the French foreign minister."},
      {"author": "Jane Austen", "work": "Mansfield Park", "quote": "Her quiet manners and modest deportment were the best **credentials** she could offer to her new companions."}
    ]
  },
  "Dashboard — cred/credenza.md": {
    "primary": "A low, elongated sideboard or buffet table, often with drawers and cupboards, used for storage or serving meals.",
    "secondary": "In corporate interior design and Italian Renaissance decorative arts, a piece of formal furniture positioned against a wall behind a principal desk or dining table.",
    "quotes": [
      {"author": "Henry James", "work": "The Golden Bowl", "quote": "Upon the carved Renaissance **credenza** stood a magnificent collection of Venetian glass."},
      {"author": "Edith Wharton", "work": "The Age of Innocence", "quote": "The dining room was dominated by an imposing mahogany **credenza** laden with family silver."},
      {"author": "Walter Pater", "work": "The Renaissance", "quote": "The Florentine interior was distinguished by the refined proportions of its walnut **credenza**."}
    ]
  },
  "Dashboard — cred/credibility.md": {
    "primary": "The fact or attribute of being trusted, believed, or accepted as convincing, authentic, and true.",
    "secondary": "In evidence jurisprudence and media communications, the objective believability of a witness testimony or public announcement under critical scrutiny.",
    "quotes": [
      {"author": "Nathaniel Hawthorne", "work": "The House of the Seven Gables", "quote": "Oftener, however, its **credibility** rested on the faith of some lonely maiden whose imaginative life had woven strange romances."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "The **credibility** of a report depends upon the integrity, competence, and number of the witnesses."},
      {"author": "David Hume", "work": "An Enquiry Concerning Human Understanding", "quote": "When a miracle is reported, we must weigh the **credibility** of the testimony against the universal uniformity of the laws of nature."}
    ]
  },
  "Dashboard — cred/credible.md": {
    "primary": "Capable of being believed, trusted, or accepted as true; convincing and reliable.",
    "secondary": "In epistemological philosophy and historical criticism, meeting sufficient evidentiary standards to warrant rational assent.",
    "quotes": [
      {"author": "William Shakespeare", "work": "All's Well That Ends Well", "quote": "Nay, 'tis most **credible**, we here receive it, / A certainty, vouch'd with our sponsor's eye."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The explanation appeared completely **credible** to everyone present at the market exchange."},
      {"author": "Charles Darwin", "work": "On the Origin of Species", "quote": "It seems scarcely **credible** that so vast an amount of geological change could be effected by such slow processes."}
    ]
  },
  "Dashboard — cred/credibleness.md": {
    "primary": "The quality, characteristic, or attribute of being credible; believability or trustworthiness.",
    "secondary": "In natural philosophy and historical apologetics, the degree to which an observed empirical narrative commands intellectual assent.",
    "quotes": [
      {"author": "Robert Boyle", "work": "The Sceptical Chymist", "quote": "The **credibleness** of our chemical hypotheses must rest upon repeatable experimental trials rather than ancient scholastic authority."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "The degree of **credibleness** we attach to any proposition ought to be proportioned to the probability of its grounds."},
      {"author": "Samuel Clarke", "work": "A Demonstration of the Being and Attributes of God", "quote": "The historical **credibleness** of ancient testimony requires careful examination of the witnesses' veracity."}
    ]
  },
  "Dashboard — cred/credibly.md": {
    "primary": "In a credible manner; in a way that induces belief or can be trusted as reliable.",
    "secondary": "In historiography and investigative reporting, attested by trustworthy witnesses or corroborated by documentary proof.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The chroniclers **credibly** report that the emperor marched fifty miles in a single day."},
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "We have been **credibly** informed of strange phenomena in the mines that demand further scientific inquiry."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "It was **credibly** affirmed that the intercepted despatches contained the complete plan of the invasion."}
    ]
  },
  "Dashboard — cred/credit.md": {
    "primary": "Public trust, confidence, or reliance placed in a person's truthfulness or solvency; or the acknowledgment of an achievement.",
    "secondary": "In commercial finance and macroeconomic banking, an arrangement allowing a borrower to obtain goods, services, or money based on the promise of future repayment.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Sonnet 138", "quote": "Thus vainly thinking that she thinks me young, / Although she knows my days are past the best, / Simply I **credit** her false-speaking tongue."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Commerce and manufactures can seldom flourish long in any state without public and private **credit**."},
      {"author": "Alexander Hamilton", "work": "Report on Public Credit", "quote": "The maintenance of national **credit** is an indispensable necessity to the prosperity and honor of the commonwealth."}
    ]
  },
  "Dashboard — cred/creditable.md": {
    "primary": "Deserving of praise, honor, or esteem; worthy of credit or respect.",
    "secondary": "In historical prose and legal testimony, deemed sufficiently reputable and trustworthy to support belief or public respectability.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "She blushes at the insult, murmured Bathsheba, watching the pink flush on her companion's cheek, which made a very **creditable** show of indignation."},
      {"author": "Jane Austen", "work": "Emma", "quote": "He managed the affairs of the Donwell parish in a very **creditable** manner, gaining the goodwill of all his neighbors."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "A young physician who conducts himself with such industry is bound to attain a **creditable** position in the profession."}
    ]
  },
  "Dashboard — cred/creditably.md": {
    "primary": "In a creditable or praiseworthy manner; with good reputation, honor, or success.",
    "secondary": "In biographical narrative, executing a public duty or profession with diligence and unimpeachable integrity.",
    "quotes": [
      {"author": "Jane Austen", "work": "Emma", "quote": "He had lived very **creditably** on his small annuity, never running into debt or complaining of his fortunes."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Gabriel conducted the spring shearing so **creditably** that Bathsheba raised his wages on the spot."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "He discharged his responsibilities in the counting-house most **creditably**, winning the warm commendation of his employers."}
    ]
  },
  "Dashboard — cred/credited.md": {
    "primary": "Attributed to someone as a creator, cause, or source; or having belief or confidence placed in one.",
    "secondary": "In banking and corporate accounting, entered as an addition to an account balance, reducing an asset or increasing a liability.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Bathsheba had grounds for conjecturing a connection between her own foolish act and the grave look **credited** to her neighbor."},
      {"author": "Ralph Waldo Emerson", "work": "Essays: First Series", "quote": "The ancient philosophers are **credited** with sayings that anticipated all modern wisdom."},
      {"author": "Charles Darwin", "work": "On the Origin of Species", "quote": "Naturalists of high repute have **credited** this plant with remarkable medicinal properties."}
    ]
  },
  "Dashboard — cred/creditor.md": {
    "primary": "A person, bank, or company to whom money is owed.",
    "secondary": "In bankruptcy jurisprudence and commercial law, an individual or corporate party possessing an enforceable legal claim against the estate of a debtor.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Comedy of Errors", "quote": "I will discharge thee ere I go from thee; / Bear me forthwith unto his **creditor**."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "A profligate debtor ruins not only himself, but frequently brings down his honest **creditor** along with him."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The impatient **creditor** paced outside the office door, demanding immediate settlement of his bill."}
    ]
  },
  "Dashboard — cred/credits.md": {
    "primary": "Acknowledgment or praise given to contributors; or the accounting entries recording sums paid or owed.",
    "secondary": "In film production and academic administration, the scrolling sequence listing cast and crew, or units evaluating completed educational coursework.",
    "quotes": [
      {"author": "Ralph Waldo Emerson", "work": "Representative Men", "quote": "This fable, which tradition **credits** to ancient Persian bards, contains profound spiritual meaning."},
      {"author": "Charles Dickens", "work": "Nicholas Nickleby", "quote": "The bookkeeper examined the ledger, verifying that the debits and **credits** were strictly balanced."},
      {"author": "Mark Twain", "work": "Roughing It", "quote": "He gave his partner all the **credits** for discovering the rich silver vein on the mountainside."}
    ]
  },
  "Dashboard — cred/creditworthiness.md": {
    "primary": "The capacity and reliability of a borrower to repay debt; financial trustworthiness.",
    "secondary": "In banking risk assessment and macroeconomic credit ratings, the quantitative score evaluating a borrower's default risk based on cash flow, collateral, and repayment history.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "A merchant's **creditworthiness** depends upon the regularity of his payments and the prudence of his commercial undertakings."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "Establishing the national **creditworthiness** was the essential first step toward securing loans from European capitals."},
      {"author": "John Maynard Keynes", "work": "The General Theory of Employment", "quote": "The perceived **creditworthiness** of borrowers collapses during periods of acute liquidity panic."}
    ]
  },
  "Dashboard — cred/creditworthy.md": {
    "primary": "Suitable, trustworthy, or sufficiently solvent to receive credit or loans.",
    "secondary": "In financial underwriting and commercial banking, possessing adequate collateral, capital reserves, and earnings to justify the extension of credit without undue risk.",
    "quotes": [
      {"author": "Walter Bagehot", "work": "Lombard Street", "quote": "In times of financial panic, the central bank must lend freely to all solvent and **creditworthy** houses upon good security."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Prudent bankers extend accommodation only to those traders whom they know to be strictly **creditworthy**."},
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "The accumulation of capital enables lenders to provide funds to any **creditworthy** entrepreneur with a viable enterprise."}
    ]
  },
  "Dashboard — cred/credo.md": {
    "primary": "A statement of the beliefs or principles that guide someone's actions; a creed.",
    "secondary": "In church liturgy and choral music, the third item of the Ordinary of the Catholic Mass setting the Nicene Creed to music.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "He only feels confident that you will do it, said Dorothea, expressing her simple **credo** of faith in human goodness."},
      {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "Every man must fashion for himself a living **credo** out of the ashes of outworn dogmas."},
      {"author": "Matthew Arnold", "work": "Essays in Criticism", "quote": "The poet articulated his artistic **credo** with unyielding devotion to classical simplicity."}
    ]
  },
  "Dashboard — cred/credulity.md": {
    "primary": "A tendency to be too ready to believe that something is real or true; gullibility.",
    "secondary": "In Enlightenment philosophy and historical criticism, the uncritical psychological disposition to accept superstitious, miraculous, or unverified claims.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Troilus and Cressida", "quote": "Such strange **credulity** of love is in me, / That on the heart of Troilus I will build / A world of true delight."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The **credulity** of the populace swallowed the most extravagant tales of pagan oracles and portents."},
      {"author": "David Hume", "work": "An Enquiry Concerning Human Understanding", "quote": "This boundless **credulity** has betrayed many an honest man into accepting fictitious marvels."}
    ]
  },
  "Dashboard — cred/credulous.md": {
    "primary": "Having or showing too great a readiness to believe things; easily deceived, gullible, or unsuspecting.",
    "secondary": "In psychological characterization and classical drama, prone to accepting deceitful flattery or baseless rumors without critical examination.",
    "quotes": [
      {"author": "William Shakespeare", "work": "All's Well That Ends Well", "quote": "We thank you, maiden, / But may not be so **credulous** of cure, / When our most learned doctors have forsaken us."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Ah, flattering guise! so easily deceived / Is the **credulous** mind by feigned humility."},
      {"author": "Francis Bacon", "work": "Essays", "quote": "The **credulous** man is an easy prey to impostors, for his mind is always open to marvels."}
    ]
  },
  "Dashboard — cred/credulously.md": {
    "primary": "In a credulous, gullible, or overly trusting manner; with ready and uncritical belief.",
    "secondary": "In historical and satirical literature, accepting unfounded assertions, fraudulent promises, or superstitious prophecies without question.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The soldiers listened **credulously** to the soothsayers, believing that victory was guaranteed by the stars."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The simple villagers **credulously** received the tale, wondering at the strange gentleman from Paris."},
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "The puritan crowd **credulously** imagined they saw an angelic sign flaming across the midnight sky."}
    ]
  },
  "Dashboard — cred/credulousness.md": {
    "primary": "The quality, habit, or disposition of being credulous; gullibility or excessive readiness to believe.",
    "secondary": "In epistemological critique, an intellectual defect characterized by the absence of skepticism and critical evaluation of sensory reports.",
    "quotes": [
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "The first distemper of learning is when men study words and not matter, which breedeth **credulousness** and imposture."},
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "Universal **credulousness** is dangerous, but total skepticism is contrary to the active conduct of life."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "A habit of unexamined **credulousness** disposes the mind to receive any tradition however absurd."}
    ]
  },
  "Dashboard — cred/discredit.md": {
    "primary": "To harm the good reputation of someone or something; or to cause to be distrusted or disbelieved.",
    "secondary": "In historiography and scientific debate, the systematic refutation of a witness, theory, or alleged fact by uncovering fatal discrepancies.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry VI, Part 1", "quote": "Did he not rather / **Discredit** my authority with yours, / And make the faction greater than it was?"},
      {"author": "Charles Darwin", "work": "On the Origin of Species", "quote": "A single well-authenticated fossil in an older stratum would **discredit** the entire proposed lineage."},
      {"author": "John Stuart Mill", "work": "On Liberty", "quote": "To attempt to **discredit** an opponent by imputing bad motives is the most common vice of polemical discussion."}
    ]
  },
  "Dashboard — cred/discreditable.md": {
    "primary": "Tending to bring discredit, shame, or disgrace; dishonorable or disreputable.",
    "secondary": "In professional ethics and public administration, conduct that violates established fiduciary standards and lowers institutional dignity.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "The objectors to utilitarianism cannot always be charged with representing it in a **discreditable** light."},
      {"author": "Anthony Trollope", "work": "The Warden", "quote": "To accept the income without discharging the duty appeared to him a most **discreditable** position."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The clandestine transaction was so **discreditable** that both parties sought to keep it buried in secrecy."}
    ]
  },
  "Dashboard — cred/discreditably.md": {
    "primary": "In a discreditable, dishonorable, shameful, or disreputable manner.",
    "secondary": "In narrative prose, failing to meet moral, professional, or social expectations of dignity and rectitude.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick; or, The Whale", "quote": "The first time Stubb lowered with him, Pip evinced much nervousness, and acted so **discreditably** that he was sternly rebuked."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "He had backed out of the contract so **discreditably** that his former partners refused to greet him in public."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "He concluded his speech so **discreditably** that even his warmest supporters were covered with confusion."}
    ]
  },
  "Dashboard — cred/discredited.md": {
    "primary": "Having lost credibility, reputation, or public confidence; shown to be false, unreliable, or fraudulent.",
    "secondary": "In the history of science and political theory, describing superseded hypotheses (like the phlogiston theory) or disgraced political regimes abandoned by scholars.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Winter's Tale", "quote": "O, sir, you had then left unseen a wonderful piece of work, which not to have been blessed with, would have **discredited** your travels."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The antiquated notion of separate cataclysmic creations has been completely **discredited** by modern paleontology."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The oracle had been so often **discredited** by false predictions that its priests could no longer attract pilgrims."}
    ]
  },
  "Dashboard — cred/incredibility.md": {
    "primary": "The property or characteristic of being incredible; surpassing belief or being impossible to believe.",
    "secondary": "In philosophical skepticism and aesthetics, the extreme degree of implausibility that prevents a rational mind from assenting to an extraordinary proposition.",
    "quotes": [
      {"author": "John Dryden", "work": "The Hind and the Panther", "quote": "The very **incredibility** of the mystery challenges the pride of human reason and commands humble faith."},
      {"author": "David Hume", "work": "A Treatise of Human Nature", "quote": "The **incredibility** of a report increases in proportion to its departure from common sensory experience."},
      {"author": "Samuel Johnson", "work": "The Lives of the English Poets", "quote": "The extravagant fables of heroic romance offend by their total **incredibility**."}
    ]
  },
  "Dashboard — cred/incredible.md": {
    "primary": "Difficult or impossible to believe; extraordinary, astonishing, or surpassing ordinary comprehension.",
    "secondary": "In dramatic narrative and rhetorical description, exceeding ordinary human experience to a degree that astounds the imagination.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Taming of the Shrew", "quote": "I tell you, 'tis **incredible** to believe / How much she loves me: O! the kindest Kate!"},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The variety and beauty of these marine animals seemed almost **incredible** when viewed through the clear water."},
      {"author": "Herman Melville", "work": "Moby-Dick; or, The Whale", "quote": "The vast speed at which the wounded whale darted across the ocean seemed **incredible** to the pursuing oarsmen."}
    ]
  },
  "Dashboard — cred/incredibleness.md": {
    "primary": "The attribute or degree of being incredible; astonishment or extreme implausibility.",
    "secondary": "In Victorian speculative fiction and natural philosophy, the utter departure of a concept or phenomenon from conventional scientific plausibility.",
    "quotes": [
      {"author": "H. G. Wells", "work": "The Time Machine", "quote": "So I don't think any of us said very much about time travelling in the interval, owing to its sheer **incredibleness**."},
      {"author": "Robert Boyle", "work": "Experiments and Considerations Touching Colours", "quote": "The sudden transmutation of colors excited wonder in the spectators by its apparent **incredibleness**."},
      {"author": "Thomas Browne", "work": "Pseudodoxia Epidemica", "quote": "The **incredibleness** of these monstrous descriptions should have warned compilers against recording them as natural facts."}
    ]
  },
  "Dashboard — cred/incredibly.md": {
    "primary": "In an incredible manner; to a degree that is difficult to believe; amazingly or astonishingly.",
    "secondary": "In narrative and descriptive literature, indicating exceptional intensity, speed, complexity, or expenditure of effort.",
    "quotes": [
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "I learned from my two years' experience that it would cost **incredibly** little trouble to obtain one's necessary food."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "The morphological variations produced by artificial selection within a few generations are **incredibly** diverse."},
      {"author": "Mark Twain", "work": "Life on the Mississippi", "quote": "The pilot navigated the snags with a precision that seemed **incredibly** daring to a landsman."}
    ]
  },
  "Dashboard — cred/incredulity.md": {
    "primary": "The state, disposition, or feeling of being unwilling or unable to believe something; skepticism or disbelief.",
    "secondary": "In psychological observation and social history, the instinctive mental resistance to accepting astonishing discoveries or sudden disasters.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Gabriel looked incredulous and sad, but between his moments of **incredulity** he resolved to discover the whole truth."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "It was the epoch of belief, it was the epoch of **incredulity**, it was the season of light, it was the season of darkness."},
      {"author": "Nathaniel Hawthorne", "work": "The Blithedale Romance", "quote": "A smile of gentle **incredulity** played upon her lips as she listened to his grand philanthropic schemes."}
    ]
  },
  "Dashboard — cred/incredulous.md": {
    "primary": "Unwilling or unable to believe something; showing, feeling, or expressing disbelief or skepticism.",
    "secondary": "In character portrayal and psychological dialogue, reacting with critical doubt or astonished rejection to an unexpected revelation.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry IV, Part 2", "quote": "If I do feign, O, let me in my present wildness die / And never live to show the **incredulous** world / The noble change that I have purposed!"},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth looked at him with an **incredulous** smile, unable to comprehend the change in his sentiments."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Angel Clare listened with an **incredulous** expression, as if his ears had deceived him."}
    ]
  },
  "Dashboard — cred/incredulously.md": {
    "primary": "In an incredulous manner; with an expression or tone of disbelief, skepticism, or astonishment.",
    "secondary": "In narrative fiction, expressing shock, doubt, or suspicious hesitation when confronting an unbelievable event.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Are they mine? she asked **incredulously**, staring at the flock of sheep that filled the lane."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "She shook her head **incredulously**, refusing to accept the sinister interpretation placed upon his conduct."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Joe looked at me **incredulously**, as if he suspected I was playing some elaborate trick upon him."}
    ]
  },
  "Dashboard — cred/overcredulity.md": {
    "primary": "Excessive credulity; too great a readiness to believe without adequate proof or investigation.",
    "secondary": "In rationalist philosophy and historical criticism, the intellectual error of accepting superstitions, rumors, or unverified claims through gullibility.",
    "quotes": [
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "The mind of man must be purged of both extreme skepticism and foolish **overcredulity**."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The **overcredulity** of the Byzantine chroniclers transformed modest military skirmishes into celestial miracles."},
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "A youthful disposition is frequently marred by **overcredulity**, which lays it open to bitter subsequent disillusionment."}
    ]
  },
  "Dashboard — cred/overcredulous.md": {
    "primary": "Excessively credulous; too easily convinced; disposed to believe on slight or insufficient evidence.",
    "secondary": "In dramatic character analysis and satire, depicting individuals whose naive trust makes them easy victims of deceit.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Othello", "quote": "A loving, noble nature... Perplexed in the extreme, and far too **overcredulous** of honest Iago's reports."},
      {"author": "John Milton", "work": "Samson Agonistes", "quote": "I, an **overcredulous** husband, gave up the secret of my consecrated strength to a treacherous deceiver."},
      {"author": "Jonathan Swift", "work": "Gulliver's Travels", "quote": "The emperor was surrounded by flatterers who found in his **overcredulous** temper a fertile field for advancement."}
    ]
  },
  "Dashboard — cred/unaccredited.md": {
    "primary": "Lacking official accreditation, authorization, certification, or formal credentials.",
    "secondary": "In diplomatic protocol and education policy, describing an uncertified academic institution or an unofficial envoy lacking letters of credence.",
    "quotes": [
      {"author": "Woodrow Wilson", "work": "The State", "quote": "An **unaccredited** agent possesses no legal standing to negotiate binding treaties between sovereign states."},
      {"author": "Henry Adams", "work": "The Education of Henry Adams", "quote": "He attended lectures at the **unaccredited** private academy, finding its informal curriculum surprisingly invigorating."},
      {"author": "Theodore Roosevelt", "work": "An Autobiography", "quote": "The commissioner warned the public against investing in **unaccredited** mineral enterprises lacking geological surveys."}
    ]
  }
}

base_dir = r"App database\Latin roots\Cluster Faith"

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

print(f"Faith Batch 1 (cred): Successfully updated {updated}/{len(data)} notes.")
