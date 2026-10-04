# -*- coding: utf-8 -*-
"""
Curates Dashboard — em (35 words) in Cluster Giving & Receiving.
"""
import os, sys, re

sys.stdout.reconfigure(encoding="utf-8")

data_em = {
  "deem": {
    "primary": "To consider, judge, believe, or hold as an opinion; to pronounce judgment upon.",
    "secondary": "In statutory interpretation, a legal fiction treating an entity or state of affairs as having a particular status.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Winter's Tale", "quote": "I **deem** it far more safe to listen to the honest counsel of an old counselor than the flattery of young courtiers."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The judiciary must **deem** the fundamental law of the constitution superior to any legislative enactment."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth did not **deem** it necessary to disclose the full particulars of Darcy's letter to her sister."}
    ]
  },
  "em": {
    "primary": "A unit of typographic measurement equal to the width of the letter M or the current point size of a font.",
    "secondary": "In digital web formatting and CSS, a scalable relative unit based on the font size of the parent element.",
    "quotes": [
      {"author": "Benjamin Franklin", "work": "Autobiography", "quote": "As an apprentice printer in London, I learned to space each composing stick by the standard pica and **em** rule."},
      {"author": "Theodore Low De Vinne", "work": "The Practice of Typography", "quote": "The typesetter aligns indentations and paragraph breaks by inserting a quad of one **em**."},
      {"author": "Mark Twain", "work": "Roughing It", "quote": "In the frontier printing shop, we calculated newspaper columns by counting brevier lines and **em** dashes."}
    ]
  },
  "exemplar": {
    "primary": "A person or thing serving as a typical example or excellent model to be imitated.",
    "secondary": "In manuscript codicology and textual criticism, the authoritative master manuscript from which copies are transcribed.",
    "quotes": [
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "Socrates stands as the supreme moral **exemplar** of antiquity, demonstrating virtue through life and death."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The emperor Marcus Aurelius chose the philosopher Antoninus Pius as his constant **exemplar** in statecraft."},
      {"author": "Matthew Arnold", "work": "Essays in Criticism", "quote": "Great classic poets provide an **exemplar** of high seriousness and consummate architectural style."}
    ]
  },
  "exemplary": {
    "primary": "Serving as a desirable model; representing the best of its kind; commendable and praiseworthy.",
    "secondary": "In civil tort law, exemplary damages (punitive damages) awarded to punish egregious malice and deter others.",
    "quotes": [
      {"author": "Jane Austen", "work": "Mansfield Park", "quote": "Fanny Price displayed an **exemplary** patience that won the reluctant affection of Sir Thomas."},
      {"author": "Blackstone", "work": "Commentaries on the Laws of England", "quote": "Juries may award **exemplary** damages against perpetrators of wanton and malicious injury."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "The rector's quiet devotion to his parishioners was regarded as truly **exemplary** throughout the county."}
    ]
  },
  "exemplification": {
    "primary": "The act of illustrating, clarifying, or demonstrating by means of an example; an instance or embodiment.",
    "secondary": "In administrative and legal archival practice, an attested official copy of a document under the seal of a court or public office.",
    "quotes": [
      {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "The ancient ballad serves as a vivid **exemplification** of passionate, spontaneous feeling."},
      {"author": "Blackstone", "work": "Commentaries on the Laws of England", "quote": "The attorney produced an attested **exemplification** of the royal charter bearing the Great Seal."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Sensory illusions provide striking **exemplification** of how unconscious inferences shape visual perception."}
    ]
  },
  "exemplify": {
    "primary": "To show or illustrate by example; to be a typical instance, embodiment, or model of.",
    "secondary": "In legal practice, to execute an official attested copy of a judicial record or document under seal.",
    "quotes": [
      {"author": "Ralph Waldo Emerson", "work": "Representative Men", "quote": "Great individuals **exemplify** the latent possibilities of human intellectual and spiritual power."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Oceanic island faunas **exemplify** the principles of geographic colonization and adaptive radiation."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "New England townships **exemplify** the direct application of democratic sovereignty in civic affairs."}
    ]
  },
  "exemplifying": {
    "primary": "Showing, illustrating, or demonstrating by typical example; embodying a principle or type.",
    "secondary": "In philosophical argument and literary criticism, serving as concrete evidence verifying a theoretical proposition.",
    "quotes": [
      {"author": "Matthew Arnold", "work": "Culture and Anarchy", "quote": "Sophocles achieved greatness by **exemplifying** sweetness and light in classical dramatic verse."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "Modern laboratory demonstrations succeed by **exemplifying** abstract physical formulas through visible phenomena."},
      {"author": "Henry James", "work": "The Art of Fiction", "quote": "The novelist creates memorable art by **exemplifying** human psychology through concrete moral dilemmas."}
    ]
  },
  "exempt": {
    "primary": "Free from an obligation, liability, duty, or tax imposed on others; released from a requirement.",
    "secondary": "In statutory tax and labor law, workers or organizations not subject to specific wage regulations or income levies.",
    "quotes": [
      {"author": "John Locke", "work": "Second Treatise of Government", "quote": "No man in civil society can be **exempt** from the laws thereof by royal prerogative."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Medieval church lands were frequently **exempt** from feudal land taxes and military service."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "No citizen can claim to be **exempt** from the legal jurisdiction of the federal courts."}
    ]
  },
  "exemption": {
    "primary": "Freedom, release, or immunity from an obligation, duty, penalty, or tax imposed on others.",
    "secondary": "In personal income tax schedules, a statutory allowance deducted from taxable income for dependents.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The wealthy senators purchased **exemption** from hazardous frontier service by paying heavy monetary fines."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "Aristocratic **exemption** from public taxation was the primary catalyst of revolutionary resentment in France."},
      {"author": "Blackstone", "work": "Commentaries on the Laws of England", "quote": "The ancient charter granted the university full **exemption** from the municipal jurisdiction of the mayor."}
    ]
  },
  "irredeemable": {
    "primary": "Not able to be saved, improved, corrected, or reformed; beyond hope of recovery or redemption.",
    "secondary": "In monetary finance, paper currency that cannot be converted on demand into metallic gold or silver specie.",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "The fallen angels realized their loss of heaven was absolute and **irredeemable** through any repentance."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "An excessive issue of **irredeemable** paper money inevitably depreciates exchange rates across foreign markets."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Bulstrode regarded his early financial crimes as an **irredeemable** stain upon his moral soul."}
    ]
  },
  "nonexempt": {
    "primary": "Not exempt from a rule, obligation, tax, or duty; subject to standard legal requirements.",
    "secondary": "In labor law, employees covered by statutory minimum wage and mandatory overtime pay protections.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "Report on Public Credit", "quote": "Every **nonexempt** merchant was required to pay the uniform import duty upon entering harbor."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "A fair revenue system ensures that **nonexempt** citizens contribute in proportion to their annual revenue."},
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "The statute imposed a modest excise upon **nonexempt** domestic manufactured goods."}
    ]
  },
  "peremptory": {
    "primary": "Insisting on immediate attention or obedience; leaving no opportunity for denial or refusal; imperious.",
    "secondary": "In civil and criminal trial procedure, a peremptory challenge allowing an attorney to reject a juror without stating a reason.",
    "quotes": [
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Mrs. Ferrars delivered her **peremptory** command that Edward should marry Miss Morton or face disinheritance."},
      {"author": "Blackstone", "work": "Commentaries on the Laws of England", "quote": "In capital felonies, the prisoner was allowed a **peremptory** challenge of thirty-five jurors without cause."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "Mr. Rochester's voice took on a **peremptory** tone that demanded instant obedience from his listeners."}
    ]
  },
  "pre-emptive": {
    "primary": "Serving or intended to pre-empt or forestall something, especially an anticipated attack or event.",
    "secondary": "In military doctrine and strategic security, a military strike launched to forestall an imminent adversary offensive.",
    "quotes": [
      {"author": "Winston Churchill", "work": "The Second World War", "quote": "The naval cabinet debated whether a **pre-emptive** landing along the Norwegian coast was strategically imperative."},
      {"author": "Thucydides", "work": "History of the Peloponnesian War", "quote": "The Corinthians urged their allies to take **pre-emptive** measures against Athenian maritime aggression."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "A nation must maintain readiness to execute a **pre-emptive** defense before hostile fleets approach its shores."}
    ]
  },
  "pre-emptor": {
    "primary": "One who exercises the right of pre-emption; a person who acquires property before others.",
    "secondary": "In public land history, a frontier settler claiming public lands under federal pre-emption statutes.",
    "quotes": [
      {"author": "Theodore Roosevelt", "work": "The Winning of the West", "quote": "The bold **pre-emptor** cleared the virgin forest, building a log cabin to establish his statutory homestead."},
      {"author": "Horace Greeley", "work": "Hints Toward Reforms", "quote": "The pioneer **pre-emptor** deserves protection from the speculative land syndicates that devour the public domain."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "The western **pre-emptor** staked out his claim with axe marks on the boundary trees."}
    ]
  },
  "preempt": {
    "primary": "To take action in order to prevent an anticipated event from happening; to forestall or take precedence over.",
    "secondary": "In broadcasting, to replace a scheduled television or radio program with breaking news or live coverage.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "Vigorous federal action will **preempt** dangerous discord between rival commercial states."},
      {"author": "Ralph Waldo Emerson", "work": "Essays: First Series", "quote": "A resolute original intellect will **preempt** the conclusions of slower analytical thinkers."},
      {"author": "Winston Churchill", "work": "The Gathering Storm", "quote": "Britain moved troops into Iceland to **preempt** potential enemy occupation of North Atlantic sea lanes."}
    ]
  },
  "preemption": {
    "primary": "The purchase of goods or shares by one person or party before the opportunity is offered to others.",
    "secondary": "In American property law, the statutory right of an actual settler on public lands to purchase them before public auction.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Royal monopolies once exercised the oppressive right of **preemption** over all grain brought to market."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "Federal statutes granted the right of **preemption** to encourage rapid agrarian settlement in western territories."},
      {"author": "Thomas Jefferson", "work": "Writings", "quote": "The policy of **preemption** secured productive homesteads for poor emigrants seeking economic independence."}
    ]
  },
  "preemptive": {
    "primary": "Relating to or characterized by the right to purchase property before others; designed to forestall action.",
    "secondary": "In computing and operating systems, preemptive multitasking where the scheduler interrupts active tasks to allocate CPU time.",
    "quotes": [
      {"author": "Winston Churchill", "work": "The Second World War", "quote": "The prime minister authorized a **preemptive** naval deployment to protect Gibraltar against surprise assault."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "A firm federal union provides **preemptive** security against the intrigues of foreign monarchs."},
      {"author": "Carl von Clausewitz", "work": "On War", "quote": "A decisive commander sometimes calculates that a **preemptive** maneuver offers the only path to survival."}
    ]
  },
  "preemptor": {
    "primary": "A person who buys or acquires something before others, especially an agricultural settler claiming land.",
    "secondary": "In nineteenth-century land legislation, an occupant possessing priority rights to buy surveyed government acreage.",
    "quotes": [
      {"author": "Theodore Roosevelt", "work": "Ranch Life and the Hunting-Trail", "quote": "The industrious **preemptor** defended his sod house against both prairie blizzards and range cattle."},
      {"author": "Horace Greeley", "work": "An Overland Journey", "quote": "Congress recognized the equity of the frontier **preemptor** over the claims of absentee speculators."},
      {"author": "Mark Twain", "work": "Roughing It", "quote": "Every ambitious miner and **preemptor** hurried to record his boundary stakes at the county registrar's cabin."}
    ]
  },
  "redeem": {
    "primary": "To compensate for faults; to gain or regain possession of something in exchange for payment.",
    "secondary": "In theology and soteriology, to deliver or liberate humanity from sin and spiritual death through divine grace.",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Which of ye will be mortal to **redeem** man's mortal crime, and just th' unjust to save?"},
      {"author": "Charles Dickens", "work": "A Christmas Carol", "quote": "Scrooge resolved to **redeem** his past misdeeds by living with benevolence toward all mankind."},
      {"author": "William Shakespeare", "work": "Henry IV, Part 1", "quote": "I will **redeem** all this on Percy's head and in the closing of some glorious day be bold to tell you that I am your son."}
    ]
  },
  "redeemable": {
    "primary": "Capable of being recovered, bought back, or converted into cash or goods; capable of moral reform.",
    "secondary": "In financial bonds and corporate debt, securities that the issuer has the right to repurchase at a specified call price.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Banknotes must remain instantly **redeemable** in gold coin upon demand to preserve commercial stability."},
      {"author": "Alexander Hamilton", "work": "Report on Public Credit", "quote": "The national debt was funded into annuities **redeemable** at the option of the federal government."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Even in his fallen state, Fred Vincy's character seemed **redeemable** through genuine affection and labor."}
    ]
  },
  "redeemed": {
    "primary": "Compensated for, bought back, or recovered through payment; spiritually saved or morally transformed.",
    "secondary": "In commercial pawn operations, pledged collateral reclaimed upon full repayment of the principal loan.",
    "quotes": [
      {"author": "Charles Dickens", "work": "A Christmas Carol", "quote": "The repentant merchant **redeemed** his wasted years by bringing joy and comfort to the Cratchit hearth."},
      {"author": "John Bunyan", "work": "The Pilgrim's Progress", "quote": "Christian rejoiced among the **redeemed** souls as his burden of guilt fell away before the Cross."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The weary mariners felt as though they had been miraculously **redeemed** from the watery abyss."}
    ]
  },
  "redeemer": {
    "primary": "A person who redeems, buys back, or liberates someone from captivity, bondage, or debt.",
    "secondary": "In Christian theology, Jesus Christ regarded as the divine savior delivering humanity from sin.",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Hail Son of God, Saviour of Men... The great **redeemer** of mankind shall reign in glory."},
      {"author": "Frederick Douglass", "work": "Narrative of the Life of Frederick Douglass", "quote": "The enslaved regarded the northern abolitionists as their promised earthly **redeemer**."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "St. John Rivers spoke with fervent conviction of the divine **Redeemer** calling laborers to the missionary field."}
    ]
  },
  "redeeming": {
    "primary": "Compensating for faults or defects; serving to offset a negative impression or character flaw.",
    "secondary": "In religious theology, bringing about spiritual deliverance or salvation from sin.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth acknowledged that Darcy's filial devotion and generosity to his sister were **redeeming** virtues."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Even the coarse convict Magwitch revealed a deeply **redeeming** tenderness in his gratitude toward Pip."},
      {"author": "Herman Melville", "work": "Billy Budd", "quote": "The handsome sailor possessed an innocent, **redeeming** simplicity that disarmed cynical shipmates."}
    ]
  },
  "redemption": {
    "primary": "The action of saving or delivering someone from sin, error, or evil; regaining possession through payment.",
    "secondary": "In finance and bond markets, the return of a mutual fund share or bond principal to the issuer for cash.",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Love without end, and without measure Grace... Bringing eternal **redemption** to man."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "A sinking fund was instituted for the gradual **redemption** of the principal of the national debt."},
      {"author": "Fyodor Dostoevsky", "work": "Crime and Punishment", "quote": "Raskolnikov began his long and painful journey toward moral **redemption** in the Siberian prison."}
    ]
  },
  "redemptional": {
    "primary": "Pertaining to, effecting, or involving redemption or salvation; redemptive in character.",
    "secondary": "In systematic theology, doctrines concerning the historical stages of divine salvation.",
    "quotes": [
      {"author": "Samuel Taylor Coleridge", "work": "Aids to Reflection", "quote": "The incarnation represents the central **redemptional** event in the spiritual history of humanity."},
      {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "Teufelsdröckh passed through the Everlasting No into a glorious **redemptional** awakening of the soul."},
      {"author": "John Bunyan", "work": "The Pilgrim's Progress", "quote": "The shining messenger unfolded the **redemptional** covenant inscribed upon the sacred parchment."}
    ]
  },
  "redemptive": {
    "primary": "Acting to save or free someone from error, sin, or evil; serving to redeem or compensate.",
    "secondary": "In literary tragedy, the spiritual purification or moral renewal achieved through suffering.",
    "quotes": [
      {"author": "George Eliot", "work": "Silas Marner", "quote": "The golden-haired child Eppie entered the solitary weaver's cottage with a quiet, **redemptive** grace."},
      {"author": "Martin Luther King Jr.", "work": "Letter from Birmingham Jail", "quote": "Unearned suffering is **redemptive**, possessing the moral power to transform the hearts of oppressors."},
      {"author": "Fyodor Dostoevsky", "work": "The Brothers Karamazov", "quote": "Father Zosima taught that active love possesses an infinite, **redemptive** strength in this earthly life."}
    ]
  },
  "redemptory": {
    "primary": "Serving to redeem; paid or given as a ransom or price of redemption; redemptive.",
    "secondary": "In ecclesiastical canon law, payments or sacrifices offered for the remission of canonical penalties.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The barbarian king demanded a vast **redemptory** payment before releasing his imperial captives."},
      {"author": "John Milton", "work": "The Reason of Church Government", "quote": "Spiritual liberty was purchased by the supreme **redemptory** sacrifice of the Son of God."},
      {"author": "Walter Scott", "work": "The Talisman", "quote": "The grand master offered gold and precious jewels as a **redemptory** ransom for the captured knights."}
    ]
  },
  "seem": {
    "primary": "To give the impression of being something or having a particular quality; to appear to the mind or senses.",
    "secondary": "In philosophical skepticism and epistemology, sensory appearances contrasted with true metaphysical reality.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "These indeed **seem**, for they are actions that a man might play; but I have that within which passeth show."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Things often **seem** identical to our careless senses while differing profoundly in real essence."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Darcy did not **seem** inclined to join in the conversation, remaining aloof beside the mantelpiece."}
    ]
  },
  "seeming": {
    "primary": "Apparent rather than real; outward appearance or aspect, especially when deceptive.",
    "secondary": "In ethical discourse, superficial piety or virtue masking selfish inward motives.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Measure for Measure", "quote": "Hence with thy false **seeming**! I will proclaim thee, Angelo; look for't!"},
      {"author": "Francis Bacon", "work": "Essays", "quote": "Dissimulation is but a faint kind of policy, for it relies on mere **seeming** rather than substance."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Satan concealed his burning malice beneath a fair **seeming** of angelic innocence and reverence."}
    ]
  },
  "seemliness": {
    "primary": "The quality of conforming to standards of decorum, good taste, and propriety; suitability.",
    "secondary": "In social etiquette, refined behavior that avoids vulgarity, ostentation, or offense.",
    "quotes": [
      {"author": "Samuel Richardson", "work": "Sir Charles Grandison", "quote": "Sir Charles observed every rule of polished **seemliness** with unaffected dignity and grace."},
      {"author": "Jane Austen", "work": "Emma", "quote": "Emma recognized the quiet **seemliness** of Mr. Knightley's conduct compared with the vanity of Frank Churchill."},
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "Ancient manners conferred a dignified **seemliness** upon public institutions that commanded respect."}
    ]
  },
  "seemly": {
    "primary": "Conforming to accepted standards of good taste, decorum, or propriety; fitting and suitable.",
    "secondary": "In historical aesthetics, attractive, pleasing to look at, or well-proportioned in physical appearance.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry VIII", "quote": "I am not an impostor, but a **seemly** and honest lady who claims her lawful royal rights."},
      {"author": "George Eliot", "work": "The Mill on the Floss", "quote": "Mrs. Tulliver insisted that all household linens should be displayed in a **seemly** and respectable order."},
      {"author": "Walter Scott", "work": "The Antiquary", "quote": "The old servitor wore a **seemly** coat of blue cloth, trimmed according to the ancient family livery."}
    ]
  },
  "unredeemable": {
    "primary": "Not capable of being redeemed, saved, reformed, or converted into cash; hopeless.",
    "secondary": "In finance, perpetual bonds or paper currency devoid of gold convertibility.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "The revolutionary government flooded the market with **unredeemable** assignats that caused ruinous inflation."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "Rochester lamented that his reckless early choices had tied him to an **unredeemable** domestic misery."},
      {"author": "Herman Melville", "work": "The Confidence-Man", "quote": "The cynical passenger proclaimed that human selfishness was an **unredeemable** trait of the race."}
    ]
  },
  "unredeemed": {
    "primary": "Not bought back, cleared of debt, or recovered; not having achieved moral reform or spiritual salvation.",
    "secondary": "In territorial diplomacy, border regions populated by an ethnic group under foreign rule awaiting reclamation (irredenta).",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "A mountainous public debt remained **unredeemed** long after the conclusion of the continental war."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The poor pawnbroker's shelves were crowded with **unredeemed** pledges belonging to destitute families."},
      {"author": "William Faulkner", "work": "The Sound and the Fury", "quote": "The haunted youth wandered through the dusk, feeling his lost honor was forever **unredeemed**."}
    ]
  },
  "unseemliness": {
    "primary": "Inappropriate, unbecoming, or indecorous conduct; an egregious breach of propriety.",
    "secondary": "In moral philosophy, conduct that degrades human dignity by violating civil decorum.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "The philosopher reproved the **unseemliness** of aged courtiers who affected the frivolous vices of youth."},
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Elinor was mortified by the vulgar **unseemliness** of Mrs. Jennings' loud matrimonial banter."},
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "The assembly degraded legislative dignity through the riotous **unseemliness** of its public galleries."}
    ]
  },
  "unseemly": {
    "primary": "Not suitable, proper, or decorous; inappropriate, unbecoming, or contrary to good manners.",
    "secondary": "In legal and judicial ethics, behavior by counsel or magistrate that breaches court decorum.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Romeo and Juliet", "quote": "Thy tears are womanish; thy wild acts denote the unreasonable fury of a beast: **unseemly** woman in a seeming man!"},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth considered Mrs. Bennet's boisterous boasting about Bingley to be highly **unseemly** before strangers."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "The young physician avoided all **unseemly** quarrels with his provincial rivals, relying upon professional diligence."}
    ]
  }
}
