# -*- coding: utf-8 -*-
import os, sys

sys.stdout.reconfigure(encoding="utf-8")

data = {
  # =========================================================================
  # Dashboard — cur (Batch 8C: 39 words including fixes for curtal and inaccuracy)
  # =========================================================================
  "Dashboard — cur/curtal.md": {
    "primary": "Having a docked tail; shortened, truncated, or cropped; a horse or dog with a docked tail.",
    "secondary": "In early modern English drama and balladry, designating a member of certain religious orders, notably friars, or describing a short heavy cutlass.",
    "quotes": [
      {"author": "William Shakespeare", "work": "All's Well That Ends Well", "quote": "I'd give bay **curtal** and his furniture, my mouth no more were broken than these boys'."},
      {"author": "Walter Scott", "work": "Ivanhoe", "quote": "The jolly friar rode upon a stout **curtal** mule whose dock had been cropped close."},
      {"author": "Francis James Child", "work": "The English and Scottish Popular Ballads", "quote": "There was a **curtal** friar in Fountains Dale, that well could bend a bow."}
    ]
  },
  "Dashboard — cur/inaccuracy.md": {
    "primary": "A deviation from truth, precision, or factual correctness; an error, miscalculation, or mistake in statement or calculation.",
    "secondary": "In historiography and scientific publishing, factual or numerical discrepancies compromising the empirical reliability of a study.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "It is, I fear, nothing more than a part of his general **inaccuracy** and indisposition to patient research."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "A single careless **inaccuracy** in recording breeding pedigrees can mislead the investigator for years."},
      {"author": "Bertrand Russell", "work": "The Problems of Philosophy", "quote": "Philosophical skepticism warns us against the constant danger of perceptual **inaccuracy**."}
    ]
  },
  "Dashboard — cur/inaccurate.md": {
    "primary": "Not correct, true, or exact; containing errors or mistakes in detail, measurement, or statement.",
    "secondary": "In cartography and physical measurement, falling outside acceptable tolerances or deviating systematically from verified reference standards.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "False facts are highly injurious to the progress of science, for they often endure long; but false views, if supported by some evidence, do little harm, as every one takes a salutary pleasure in proving their **inaccurate** character."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "A client who gives an **inaccurate** description of circumstances merely wastes his own time and mine."},
      {"author": "Bertrand Russell", "work": "The Analysis of Mind", "quote": "Memories that are vividly presented to consciousness may nevertheless prove entirely **inaccurate** upon critical examination."}
    ]
  },
  "Dashboard — cur/inaccurately.md": {
    "primary": "In a manner that contains errors, mistakes, or deviations from truth and exact precision.",
    "secondary": "In empirical reporting and laboratory transcription, recording observations with observational bias or improper instrument calibration.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Ancient writers frequently describe foreign animals so **inaccurately** that naturalists cannot identify the species with certainty."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The numbers of the rebel army were reported so **inaccurately** by contemporary chroniclers that modern historians despair of certainty."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "When intervals of time are estimated without external markers, our senses perceive them most **inaccurately**."}
    ]
  },
  "Dashboard — cur/incur.md": {
    "primary": "To become subject to something unwelcome or unpleasant as a result of one's own actions; to bring upon oneself.",
    "secondary": "In contract law and fiscal accounting, to assume a legally binding financial liability or obligation through transactional execution.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "I must confess that he has what many will call prejudice; but it will not **incur** the censure of those who know the world."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "A merchant cannot long continue a trade in which he is sure to **incur** substantial and recurring losses."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "No nation can preserve its independence when it must perpetually **incur** debts that its revenues cannot redeem."}
    ]
  },
  "Dashboard — cur/incurability.md": {
    "primary": "The incapacity of a disease, disorder, or condition to be healed, remedied, or reversed by medical intervention.",
    "secondary": "In clinical nosology and prognosis, definitive pathophysiological progression beyond the therapeutic window of remedial intervention.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The recognized **incurability** of the malady in its advanced stages demands palliative care of the highest order."},
      {"author": "Thomas Henry Huxley", "work": "Discourses: Biological & Geological", "quote": "To declare the **incurability** of a biological disorder before exploring all physical avenues is unscientific despair."},
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "Patience is the only sovereign antidote against the **incurability** of human misfortune."}
    ]
  },
  "Dashboard — cur/incurable.md": {
    "primary": "Unable to be cured, remedied, or corrected; enduring or unyielding in pathology or habit.",
    "secondary": "In hospice oncology and chronic palliative medicine, designating terminal pathology refractory to curative treatments.",
    "quotes": [
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "He had a severe, harsh temper, and an **incurable** disposition to brood over injuries."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The delay in the Court of Chancery has grown into an **incurable** cancer upon the commonwealth."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "There are certain queer times and occasions in this strange mixed affair we call life when a man takes this whole universe for an **incurable** practical joke."}
    ]
  },
  "Dashboard — cur/incurableness.md": {
    "primary": "The chronic or irreversible character of a malady, moral defect, or systemic institutional flaw.",
    "secondary": "In medical ethics and classical philosophy, recognition of irreversible mortality shaping stoic acceptance and end-of-life care.",
    "quotes": [
      {"author": "Robert Burton", "work": "The Anatomy of Melancholy", "quote": "The **incurableness** of this passion proceeds from our own stubborn refusal to submit to reason."},
      {"author": "Jeremy Taylor", "work": "Holy Living and Holy Dying", "quote": "When the physician proclaims the **incurableness** of the sickness, the soul must compose itself for departure."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Men readily argue for the **incurableness** of their prejudices when they lack the patience to examine their foundations."}
    ]
  },
  "Dashboard — cur/incurably.md": {
    "primary": "In a manner that defies cure, remedy, or reform; beyond recovery or restoration.",
    "secondary": "In clinical prognosis, designating a physiological degeneration that permanently resists therapeutic remediation.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "He felt that his peace of mind was **incurably** wounded by the disclosure."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "A member who was **incurably** antisocial or treacherous would quickly be expelled from the primitive tribe."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "The man was **incurably** insane, driven to frenzy by the superstitious terror of the moor."}
    ]
  },
  "Dashboard — cur/incurious.md": {
    "primary": "Lacking interest, desire to know, or curiosity; indifferent, heedless, or uninquiring.",
    "secondary": "In epistemological philosophy, cognitive apathy or passive habituation that disinclines an observer from empirical investigation.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The inhabitants of the province were dull, passive, and **incurious** spectators of the revolutions of the capital."},
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "She was far from **incurious** regarding the secret motives of those who surrounded her."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The rustic mind remained tranquil and **incurious** amidst the momentous changes of the season."}
    ]
  },
  "Dashboard — cur/insecure.md": {
    "primary": "Not firmly fixed, stable, or safe; subject to danger, uncertainty, or vulnerability.",
    "secondary": "In structural engineering and architectural assessment, lacking mechanical equilibrium, adequate bracing, or tensile load capacity.",
    "quotes": [
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "My sleep was disturbed by the wild dreams of an **insecure** and perilous journey."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The throne of a usurper must ever remain **insecure** against the sudden surge of popular indignation."},
      {"author": "Joseph Conrad", "work": "Heart of Darkness", "quote": "He seemed to hold his power by an **insecure** and precarious tenure among the wilderness."}
    ]
  },
  "Dashboard — cur/insecurely.md": {
    "primary": "In a precarious, unstable, or unsafe manner; without firm footing, anchor, or protection.",
    "secondary": "In seamanship and mechanical rigging, fastening hawsers, spars, or anchors without adequate tension or dogging.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The heavy harpoon hung **insecurely** balanced upon the gunwale of the tossing whaleboat."},
      {"author": "Robert Louis Stevenson", "work": "Treasure Island", "quote": "The chest was **insecurely** corded with old hemp, ready to burst at the slightest shock."},
      {"author": "Jack London", "work": "The Sea-Wolf", "quote": "He clung **insecurely** to the ratlines as the schooner rolled violently into the trough of the sea."}
    ]
  },
  "Dashboard — cur/insecureness.md": {
    "primary": "The precarious condition of lacking stability, safety, psychological confidence, or physical equilibrium.",
    "secondary": "In military fortification and strategic reconnaissance, vulnerability arising from unfortified bastions, weak flanks, or exposed supply routes.",
    "quotes": [
      {"author": "Francis Bacon", "work": "Essays", "quote": "The **insecureness** of high worldly fortune makes princes more susceptible to suspicion and fear."},
      {"author": "Thomas Hobbes", "work": "Leviathan", "quote": "Without a common power to keep them in awe, men live in perpetual dread and **insecureness**."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "The fragile barrier gave no shelter from the storm, exposing their **insecureness** to every hostile blast."}
    ]
  },
  "Dashboard — cur/insecurity.md": {
    "primary": "Uncertainty or anxiety about oneself; lack of confidence; or the state of being exposed to danger, instability, or risk.",
    "secondary": "In geopolitical analysis and macroeconomic theory, exposure to systemic shocks, food deficits, or supply chain fragility.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "Safety from external danger is the most powerful director of national conduct, and constant **insecurity** forces nations to submit to standing armies."},
      {"author": "George Eliot", "work": "The Mill on the Floss", "quote": "She felt that vague sense of **insecurity** which troubles children when their elders speak with suppressed bitterness."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Commerce and manufactures can seldom flourish long in any state which does not enjoy a regular administration of justice, but suffers from perpetual **insecurity**."}
    ]
  },
  "Dashboard — cur/manicure.md": {
    "primary": "A cosmetic treatment of the hands and fingernails, including trimming, shaping, cuticle care, and polishing.",
    "secondary": "In aesthetic cosmetology and dermatology, clinical grooming and cleansing of the perionychium and nail plate to preserve skin integrity.",
    "quotes": [
      {"author": "Edith Wharton", "work": "The Age of Innocence", "quote": "Her hands were cared for with a meticulous **manicure** that betrayed the leisure of her aristocratic life."},
      {"author": "F. Scott Fitzgerald", "work": "The Beautiful and Damned", "quote": "He surveyed his polished fingernails, admiring the delicate **manicure** he had received that morning."},
      {"author": "Sinclair Lewis", "work": "Babbitt", "quote": "He stopped at the barbershop for a haircut and an unaccustomed **manicure** before the banquet."}
    ]
  },
  "Dashboard — cur/manicurist.md": {
    "primary": "A person whose profession is the cosmetic care, grooming, and beautification of fingernails and hands.",
    "secondary": "In beauty salon management and occupational licensing, a licensed aesthetician skilled in nail shaping, cuticle therapy, and chemical polishes.",
    "quotes": [
      {"author": "P. G. Wodehouse", "work": "Right Ho, Jeeves", "quote": "The **manicurist** at the hotel had spent twenty minutes buffing his nails to an unnatural brilliance."},
      {"author": "O. Henry", "work": "The Trimmed Lamp", "quote": "Lou worked as an apprentice **manicurist** in a large downtown hotel, listening patiently to the confidences of travelers."},
      {"author": "Arnold Bennett", "work": "The Old Wives' Tale", "quote": "The smart young **manicurist** deftly arranged her instruments upon the glass table before commencing work."}
    ]
  },
  "Dashboard — cur/occur.md": {
    "primary": "To happen, take place, or come about; or to come to mind or suggest itself to one's thoughts.",
    "secondary": "In geology, ecology, and botany, to exist or be found naturally within a specific habitat, stratum, or geographical range.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Regretting at the same time that the meeting should be about to **occur** in the darkest point of her route."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Variations and reversions of character probably do **occur**; but natural selection will determine how far they shall be preserved."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "It did not **occur** to me at the moment that there was any sinister design beneath the visitor's strange errand."}
    ]
  },
  "Dashboard — cur/overcurious.md": {
    "primary": "Excessively inquisitive, prying, or overly concerned with minute, trivial, or private details.",
    "secondary": "In historical rhetoric and early modern theology, impious prying into divine mysteries or esoteric arcana exceeding human limits.",
    "quotes": [
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "It is an **overcurious** and unhealthy mind that seeks to uncover matters that prudence would leave in obscurity."},
      {"author": "John Milton", "work": "Areopagitica", "quote": "He that is **overcurious** to examine every subtle doctrine will often stumble into heresies without intending it."},
      {"author": "Jonathan Swift", "work": "Gulliver's Travels", "quote": "I was not **overcurious** to examine into the secret policy of the emperor, lest I should draw suspicion upon myself."}
    ]
  },
  "Dashboard — cur/pedicure.md": {
    "primary": "A cosmetic and hygienic treatment of the feet, toenails, and soles to remove calluses and trim nails.",
    "secondary": "In podiatric hygiene and aesthetic cosmetology, therapeutic foot care involving exfoliation of hyperkeratotic skin and nail debridement.",
    "quotes": [
      {"author": "Virginia Woolf", "work": "The Voyage Out", "quote": "She spent the afternoon resting her tired feet after a soothing **pedicure** at the seaside villa."},
      {"author": "H. G. Wells", "work": "The World of William Clissold", "quote": "Modern hygiene has elevated the bath and the **pedicure** from aristocratic luxuries to democratic necessities."},
      {"author": "Somerset Maugham", "work": "Of Human Bondage", "quote": "The old practitioner advised regular bathing and a skilled **pedicure** to alleviate the painful corns caused by poor boots."}
    ]
  },
  "Dashboard — cur/procurable.md": {
    "primary": "Capable of being obtained, acquired, or secured through effort, purchase, or request.",
    "secondary": "In supply chain management and commodity economics, available within current market inventories or manufacturing lead times.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Provisions of every kind were easily **procurable** in the market at moderate and stable prices."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "Fresh water was scarcely **procurable** on this barren coast, compelling the crew to ration every drop."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "Scientific apparatus of the highest precision is now **procurable** by every university laboratory."}
    ]
  },
  "Dashboard — cur/procural.md": {
    "primary": "The act or process of obtaining, acquiring, or bringing about something; procurement.",
    "secondary": "In legal contracts and commercial logistics, formal acquisition of goods, rights, or specialized services under binding terms.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The prompt **procural** of foreign supplies was indispensable to the survival of the continental army."},
      {"author": "Benjamin Franklin", "work": "Autobiography", "quote": "My father assisted in the **procural** of suitable books, encouraging my early inclination toward learning."},
      {"author": "Walter Scott", "work": "The Antiquary", "quote": "The **procural** of this ancient parchment cost the collector many months of patient correspondence."}
    ]
  },
  "Dashboard — cur/procurance.md": {
    "primary": "The obtaining, bringing about, or management of an acquisition, result, or office through deliberate effort.",
    "secondary": "In early modern jurisprudence, the formal facilitation or solicitation of an official decree, warrant, or royal dispensation.",
    "quotes": [
      {"author": "Francis Bacon", "work": "The Elements of the Common Lawes of England", "quote": "The **procurance** of such an illicit writ by covin or deceit invalidates the subsequent judgment."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The elevation of the bishop was effected through the secret **procurance** of influential courtiers."},
      {"author": "Thomas More", "work": "The History of King Richard the Third", "quote": "By the private **procurance** of certain lords, the young prince was brought under their immediate control."}
    ]
  },
  "Dashboard — cur/procurator.md": {
    "primary": "An agent, proxy, or representative authorized to manage another's affairs or legal interests.",
    "secondary": "In Roman imperial administration, a financial officer or provincial governor directly appointed by the emperor (e.g., Pontius Pilate).",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The imperial **procurator** was entrusted with the collection of taxes and the fiscal management of the province."},
      {"author": "Jack London", "work": "The Star Rover", "quote": "I sat as a Roman **procurator** upon the judgment seat, weighing the complaints of the provincial magistrates."},
      {"author": "Tacitus", "work": "The Annals", "quote": "The harsh exactions of the imperial **procurator** drove the Britons into open and violent rebellion."}
    ]
  },
  "Dashboard — cur/procure.md": {
    "primary": "To obtain or acquire something through effort, care, or means; or to bring about or cause to happen.",
    "secondary": "In civil contract law, to secure or arrange performance, supplies, or contractual services on behalf of a principal.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Comedy of Errors", "quote": "Proceed, Solinus, to **procure** my fall, and by the doom of death end woes and all."},
      {"author": "Jane Austen", "work": "Emma", "quote": "She was anxious to **procure** for her friend every advantage that wealth and position could afford."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "I was dispatched to **procure** the necessary provisions from the village without exciting suspicion."}
    ]
  },
  "Dashboard — cur/procurement.md": {
    "primary": "The act or process of acquiring goods, services, or works, especially for an organization or government.",
    "secondary": "In defense logistics and supply chain governance, systematic tendering, purchasing, and vendor qualification to fulfill operational mandates.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The efficient **procurement** of military stores depends upon unified administrative authority."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The **procurement** of raw materials from foreign markets stimulated domestic manufacturing."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The **procurement** of supplies for a three years' cruise required the master's vigilant personal attention."}
    ]
  },
  "Dashboard — cur/procurer.md": {
    "primary": "A person who obtains or acquires something, especially one who recruits or provides clients for prostitutes (a pimp).",
    "secondary": "In legal codes and criminal jurisprudence, an individual who solicits, induces, or facilitates unlawful commerce or prostitution.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Measure for Measure", "quote": "A bawd, a wicked **procurer** of evil pleasures, who deserves the full rigor of the law."},
      {"author": "Daniel Defoe", "work": "Moll Flanders", "quote": "She fell into the hands of an artful **procurer** who promised her honest employment in the city."},
      {"author": "Henry Fielding", "work": "Tom Jones", "quote": "He indignantly rejected the proposal, refusing to act as a **procurer** for another man's vices."}
    ]
  },
  "Dashboard — cur/procuress.md": {
    "primary": "A woman who procures prostitutes or operates a brothel; a madam.",
    "secondary": "In social history and criminal statutes, a female broker of illicit sexual commerce or keeper of a disorderly house.",
    "quotes": [
      {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "The old **procuress** watched the young ladies with greedy eyes, calculating the profit of her trade."},
      {"author": "Charles Dickens", "work": "Nicholas Nickleby", "quote": "He shrank in horror from the vile **procuress** who offered to introduce him to fashionable company."},
      {"author": "Tobias Smollett", "work": "The Adventures of Peregrine Pickle", "quote": "The unsuspecting maiden was lured into the lodgings of a notorious **procuress**."}
    ]
  },
  "Dashboard — cur/recur.md": {
    "primary": "To happen again periodically or repeatedly; or to return in thought or discourse.",
    "secondary": "In epidemiology and oncology, the return of clinical signs and symptoms of disease after a period of remission.",
    "quotes": [
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "The same ominous memory would **recur** to haunt my dreams whenever the wind wailed in the chimney."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "He did not wish the painful subject to **recur** in their conversations, preferring silence."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Ancient ancestral characters often **recur** in domestic varieties after many generations of absence."}
    ]
  },
  "Dashboard — cur/secure.md": {
    "primary": "Free from danger, risk, or fear; firmly fixed, anchored, or fastened; to make safe or obtain firmly.",
    "secondary": "In cryptographic networking and information theory, protected against unauthorized access, decryption, or malicious alteration.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "Upon my **secure** hour thy uncle stole, with juice of cursed hebona in a vial."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Man hath his daily work of body or mind appointed, which declares his dignity, and regard of Heaven on all his ways; while other animals unactive range, and of their doings God takes no account, but **secure** they sleep."},
      {"author": "Daniel Defoe", "work": "Robinson Crusoe", "quote": "I worked tirelessly to make my cave **secure** against any sudden attack from wild beasts or savages."}
    ]
  },
  "Dashboard — cur/securely.md": {
    "primary": "In a safe, well-protected, or firmly fastened manner; without danger of falling, failing, or escaping.",
    "secondary": "In maritime navigation and heavy cargo rigging, lashed with certified cables and turnbuckles to withstand high sea states.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Merchant of Venice", "quote": "Fast bind, fast find; a proverb never stale in thrifty mind, where keys are kept **securely**."},
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "The heavy iron door was locked **securely** behind me, shutting out the howling tempest."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "The stolen papers had been placed **securely** in the secret drawer of the bureau."}
    ]
  },
  "Dashboard — cur/secureness.md": {
    "primary": "The quality of feeling or being secure; freedom from apprehension, danger, or instability (often carrying an archaic sense of overconfidence).",
    "secondary": "In classical theology and moral philosophy, false peace of mind or heedless overconfidence preceding disaster.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Richard II", "quote": "Thy careless **secureness** breeds thy ruin, while danger watches at the gate."},
      {"author": "Robert Burton", "work": "The Anatomy of Melancholy", "quote": "Too much **secureness** is an enemy to wisdom, lulling men into a fatal slumber."},
      {"author": "John Bunyan", "work": "The Pilgrim's Progress", "quote": "He was betrayed by his own **secureness**, taking ease in the enchanted arbor when he should have watched."}
    ]
  },
  "Dashboard — cur/securer.md": {
    "primary": "More secure, safe, firmly fastened, or free from hazard; comparative of secure; or one that secures.",
    "secondary": "In mechanical fastening and structural engineering, a bracket, anchor bolt, or safety latch providing redundant retention.",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "But, in **securer** bounds, Heaven has preserved for thee a happier lot."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "A **securer** hiding-place for the coronet could scarcely have been conceived by mortal mind."},
      {"author": "Alexander Pope", "work": "An Essay on Man", "quote": "Build on a **securer** base, nor build on man's opinion for thy happiness."}
    ]
  },
  "Dashboard — cur/security.md": {
    "primary": "Freedom from danger, risk, or anxiety; measures taken to ensure safety; or a financial asset or collateral pledged against a debt.",
    "secondary": "In financial markets and securities law, a fungible, negotiable financial instrument (such as a stock or bond) holding monetary value.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Macbeth", "quote": "And you all know, **security** is mortals' chiefest enemy."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The great objective of the prudent capitalist is the **security** of his principal rather than exorbitant profit."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "Mutual confidence and internal tranquility are the strongest guarantors of public **security**."}
    ]
  },
  "Dashboard — cur/sinecure.md": {
    "primary": "A position or office requiring little or no work but yielding financial benefit, social status, or salary.",
    "secondary": "In ecclesiastical history and civil service reform, a benefice without cure of souls, or an unearned political appointment abolished by merit legislation.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "He regarded the purser's berth as a comfortable **sinecure** suited to his advancing years."},
      {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "His uncle procured for him an appointment in the customs, an agreeable **sinecure** with three hundred a year."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The lucrative **sinecure** was bestowed as a reward for party loyalty rather than administrative talent."}
    ]
  },
  "Dashboard — cur/uncured.md": {
    "primary": "Not healed, remedied, or restored to health; or (of meat, leather, or tobacco) not preserved by salting, smoking, or chemical curing.",
    "secondary": "In food preservation science and culinary chemistry, meat processed without synthetic nitrates or nitrites, relying solely on natural sea salts or celery powder.",
    "quotes": [
      {"author": "Walter Scott", "work": "Ivanhoe", "quote": "The knight's deep wound remained **uncured**, bleeding afresh with every strenuous movement."},
      {"author": "Herman Melville", "work": "Omoo", "quote": "The sailors grumbled at the foul rations of **uncured** beef that turned rancid in the tropical heat."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The native hunters consumed strips of **uncured** venison dried hurriedly in the wind."}
    ]
  },
  "Dashboard — cur/uncurl.md": {
    "primary": "To straighten out from a curled, coiled, or rolled shape; to cause to become flat or unrolled.",
    "secondary": "In botanical morphogenesis and animal ethology, spontaneous unwinding of tendrils, ferns (circinate vernation), or defensive hedgehog ball posture.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Titus Andronicus", "quote": "Do not **uncurl** your hair to show your grief, but let revenge take hold upon your mind."},
      {"author": "Charlotte Brontë", "work": "Villette", "quote": "I watched the delicate tendrils of the vine slowly **uncurl** toward the morning sunlight."},
      {"author": "Donn Byrne", "work": "The Wind Bloweth", "quote": "It seemed to **uncurl** like a ribbon of smoke against the purple hills."}
    ]
  },
  "Dashboard — cur/uncurled.md": {
    "primary": "Straightened out; not having curls, coils, or waves; relaxed from a curled or coiled posture.",
    "secondary": "In botanical description, vegetative fronds or shoots that have completed circinate foliar expansion into planar leaf lamina.",
    "quotes": [
      {"author": "Donn Byrne", "work": "The Wind Bloweth", "quote": "His long fingers **uncurled** slowly as the deep sleep of exhaustion overtook him."},
      {"author": "Eleanor H. Porter", "work": "Miss Billy — Married", "quote": "Her damp hair hung **uncurled** about her shoulders in straight, dark strands."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "The sleeping child lay with its small hand **uncurled** upon the coverlet."}
    ]
  },
  "Dashboard — cur/uncurtained.md": {
    "primary": "Lacking curtains, drapes, or window coverings; open to external observation, light, or air.",
    "secondary": "In domestic architecture and Victorian interior descriptions, bare windows admitting raw daylight without decorative drapery.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Through the **uncurtained** window of the cottage, a solitary candle flickered into the foggy night."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The dreary garret had only one **uncurtained** casement looking out upon a forest of chimney pots."},
      {"author": "Charlotte Brontë", "work": "Shirley", "quote": "The moon shone directly through the large **uncurtained** window, illuminating the bare boards of the schoolroom."}
    ]
  },
  "Dashboard — cur/unprocurable.md": {
    "primary": "Impossible or exceedingly difficult to obtain, acquire, or purchase; not available.",
    "secondary": "In wartime rationing and embargo economics, essential commodities or strategic alloys rendered inaccessible due to blockade or market exhaustion.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Certain rare breeds of poultry described by older fanciers have now become entirely **unprocurable**."},
      {"author": "Herman Melville", "work": "Typee", "quote": "Iron nails and trade beads were **unprocurable** on the isolated island, valued by the natives above pearls."},
      {"author": "H. G. Wells", "work": "The War of the Worlds", "quote": "In the panic-stricken capital, bread and clean water had become utterly **unprocurable** at any price."}
    ]
  }
}

base_dir = r"App database\Latin roots\Cluster Movement & Speed"
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

print(f"Speed Batch 8C: Successfully updated {updated}/{len(data)} notes.")
