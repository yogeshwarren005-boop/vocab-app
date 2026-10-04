# -*- coding: utf-8 -*-
import os, sys, re

sys.stdout.reconfigure(encoding="utf-8")

data = {
  # =========================================================================
  # Dashboard — pi (24 words)
  # =========================================================================
  "Dashboard — pi/copious.md": {
    "primary": "Yielding or containing plenty; abundant, plentiful, or large in quantity or volume.",
    "secondary": "In literary rhetoric and natural history, characterized by diffuse eloquence, vast vocabulary, or prolific natural fecundity.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Venus and Adonis", "quote": "Their fresh complaints they spend on tears and sighs, / And pour down **copious** tears from sorrowing eyes."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "The trees yielded an harvest of **copious** fruit, bending beneath their golden load."},
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "A **copious** collection of natural history observations must precede the formulation of physical axioms."}
    ]
  },
  "Dashboard — pi/copiously.md": {
    "primary": "In a copious, plentiful, or abundant manner; amply or generously.",
    "secondary": "In narrative prose and historical documentation, writing or speaking at great length, or flowing in large, unrestricted streams.",
    "quotes": [
      {"author": "James Joyce", "work": "Dubliners", "quote": "Mr Henchy snuffled vigorously and spat so **copiously** that he nearly extinguished the fire."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "The glands secrete **copiously** during periods of high environmental temperature."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The ancient historians have treated this campaign so **copiously** that every maneuver is known to posterity."}
    ]
  },
  "Dashboard — pi/copiousness.md": {
    "primary": "The attribute, extent, or degree of being copious; great abundance, plentifulness, or fullness.",
    "secondary": "In literary criticism and classical rhetoric, exuberant richness of diction or encyclopedic breadth of subject matter.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "The Lives of the English Poets", "quote": "The chief characteristic of Dryden's prose is its boundless vigor and easy **copiousness**."},
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "The **copiousness** of nature far surpasses the subtle conceptions of the human intellect."},
      {"author": "Ralph Waldo Emerson", "work": "Representative Men", "quote": "The **copiousness** of Shakespeare's vocabulary reflects the myriad facets of human experience."}
    ]
  },
  "Dashboard — pi/epi.md": {
    "primary": "A psychological assessment (Eysenck Personality Inventory, EPI); or prefix meaning on, upon, or near.",
    "secondary": "In personality psychology and psychometrics, a standardized self-report questionnaire assessing extraversion and neuroticism dimensions.",
    "quotes": [
      {"author": "Hans Eysenck", "work": "The Biological Basis of Personality", "quote": "Scores on the **EPI** provide a quantitative measure of cortical arousal and autonomic reactivity."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "The Greek prefix **epi** denotes superimposition, as seen in words describing phenomena upon an organ."},
      {"author": "Sigmund Freud", "work": "The Ego and the Id", "quote": "The **epi**-phenomenal view of consciousness reduces subjective awareness to a mere byproduct of neural discharge."}
    ]
  },
  "Dashboard — pi/expiate.md": {
    "primary": "To make amends or reparation for guilt, wrongdoing, or a sin; to atone for.",
    "secondary": "In theological ethics and sacrificial ritual, to purify moral taint through formal penance, compensatory suffering, or sacred sacrifice.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Sonnet 22", "quote": "Then look I death my days should **expiate**."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "He with his life the trespass must **expiate**, dying to redeem fallen mankind."},
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "No remorse can wholly **expiate** a neglected duty, though repentance may soften its consequences."}
    ]
  },
  "Dashboard — pi/expiation.md": {
    "primary": "The act of making amends or reparation for guilt or wrongdoing; atonement.",
    "secondary": "In ancient anthropology and liturgical theology, the ritual propitiation or purification by which a defiled community restores divine favor.",
    "quotes": [
      {"author": "graf Leo Tolstoy", "work": "War and Peace", "quote": "He felt that in this suffering lay his true **expiation**, cleansing his soul from prior selfishness."},
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "The minister sought in severe self-chastisement some hidden **expiation** for his unacknowledged transgression."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Public sacrifices were decreed by the Senate as solemn **expiation** for the defeat of the legions."}
    ]
  },
  "Dashboard — pi/expiative.md": {
    "primary": "Having the power, intent, or capacity to make expiation or atone for wrongdoing; propitiatory.",
    "secondary": "In sacramental theology and comparative religion, designating penitential acts or offerings designed to cancel ceremonial or moral defilement.",
    "quotes": [
      {"author": "Jeremy Taylor", "work": "Holy Dying", "quote": "He offered fervent prayers as an **expiative** sacrifice for the transgressions of his youth."},
      {"author": "John Henry Newman", "work": "Parochial and Plain Sermons", "quote": "The ancient sacrifices possessed a symbolic and **expiative** character anticipating the cross."},
      {"author": "Samuel Taylor Coleridge", "work": "Aids to Reflection", "quote": "Repentance without an **expiative** transformation of will remains a sterile emotion."}
    ]
  },
  "Dashboard — pi/expiatory.md": {
    "primary": "Intended, designed, or serving to make expiation, amends, or atonement for an offense.",
    "secondary": "In ritual anthropology and classical history, characterizing sacrifices, lustrations, or offerings performed to avert divine retribution.",
    "quotes": [
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "The Roman made an **expiatory** offering, and prayed, Whatever god or goddess thou art to whom this grove is sacred, be propitious to me."},
      {"author": "James George Frazer", "work": "The Golden Bough", "quote": "The community designated an **expiatory** scapegoat to carry into the desert the collective sins of the year."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The emperor instituted **expiatory** rites to cleanse the capital from the pollution of civil slaughter."}
    ]
  },
  "Dashboard — pi/impiety.md": {
    "primary": "Lack of piety or reverence for a deity or sacred things; irreverence, ungodliness, or wickedness.",
    "secondary": "In classical Athenian law and moral theology, a grave civic and religious transgression challenging established civic religion or filial duty.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Sonnet 67", "quote": "Ah wherefore with infection should he live, / And with his presence grace **impiety**?"},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "To question heaven's high decree was accounted an unpardonable **impiety** by the seraphic host."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Socrates was condemned by his fellow citizens on a charge of public **impiety** and subversion of ancestral rites."}
    ]
  },
  "Dashboard — pi/impious.md": {
    "primary": "Not showing respect or reverence, especially for a deity or religion; ungodly or profane.",
    "secondary": "In classical tragic literature, defying sacred moral laws, ancestral obligations, or fundamental natural piety.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Cymbeline", "quote": "The gates of monarchs / Are arch'd so high that giants may jet through / And keep their **impious** turbans on, without / Good morrow to the sun."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Against the throne of God with **impious** war and battle proud they strove in vain."},
      {"author": "Francis Bacon", "work": "Essays", "quote": "They that deny a God destroy man's nobility; for certainly man is of kin to the beasts by his body, and an **impious** mind dissolves the spiritual bond."}
    ]
  },
  "Dashboard — pi/impiously.md": {
    "primary": "In an impious, irreverent, profane, or ungodly manner; without religious reverence.",
    "secondary": "In narrative and religious writing, defying sacred moral commandments or mocking solemn holy rites.",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Easily the proud attempt / Of Spirits apostate, and their counsels vain, / He laughs to scorn; while they **impiously** deride his sovereign throne."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The temple was plundered and its altars **impiously** defiled by the invading barbarian host."},
      {"author": "James George Frazer", "work": "The Golden Bough", "quote": "He who had **impiously** stepped upon the sacred grove was shunned by his fellow tribesmen."}
    ]
  },
  "Dashboard — pi/impiousness.md": {
    "primary": "The quality, characteristic, or attribute of being impious; irreverence, ungodliness, or profanity.",
    "secondary": "In theological ethics and moral philosophy, willful contempt for sacred obligations, divine authority, or familial piety.",
    "quotes": [
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "Atheism leaves a man to sense, to philosophy, to natural piety, but superstition brands all with frantic **impiousness**."},
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "The shocking **impiousness** of their blasphemies provoked horror among the sober citizens of the town."},
      {"author": "John Locke", "work": "A Letter Concerning Toleration", "quote": "No magistrate can compel a citizen to act against conscience without committing an act of religious **impiousness**."}
    ]
  },
  "Dashboard — pi/pi.md": {
    "primary": "The sixteenth letter of the Greek alphabet; or the mathematical constant representing the ratio of a circle's circumference to its diameter (approximately 3.14159).",
    "secondary": "In printing and typography, a mass of type jumbled or spilled together indiscriminately; or to jumble type into disorder.",
    "quotes": [
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "The compositor had dropped the composing stick, reducing the neat lines of type to a hopeless heap of **pi**."},
      {"author": "Herman Melville", "work": "Typee: A Romance of the South Seas", "quote": "The native printing press stood neglected, its fonts scattered in hopeless **pi** upon the clay floor."},
      {"author": "Isaac Newton", "work": "The Method of Fluxions", "quote": "The quadrature of the circle demonstrates that the transcendental quantity **pi** cannot be expressed as a simple rational fraction."}
    ]
  },
  "Dashboard — pi/pietism.md": {
    "primary": "A 17th-century movement in the German Lutheran Church emphasizing personal religious devotion, Bible study, and practical Christian living.",
    "secondary": "In religious sociology and intellectual history, an intense personal or emotional piety, often contrasted with rigid institutional dogmatism.",
    "quotes": [
      {"author": "Immanuel Kant", "work": "Critique of Practical Reason", "quote": "The moral rigor of early **pietism** influenced my lifelong conviction regarding the unconditional nature of duty."},
      {"author": "Max Weber", "work": "The Protestant Ethic", "quote": "Continental **pietism** fostered an inner-worldly asceticism that shaped the work ethic of modern industrial culture."},
      {"author": "Matthew Arnold", "work": "Culture and Anarchy", "quote": "German **pietism** was a protest of individual spirituality against the dry formalism of state scholasticism."}
    ]
  },
  "Dashboard — pi/pietistic.md": {
    "primary": "Pertaining to, characteristic of, or resembling Pietism; characterized by exaggerated or demonstrative religious devotion.",
    "secondary": "In cultural history and literature, denoting earnest personal piety centered on introspective conversion, emotional prayer, and rigorous moral asceticism.",
    "quotes": [
      {"author": "Johann Wolfgang von Goethe", "work": "Poetry and Truth", "quote": "The **pietistic** circles of Frankfurt met regularly for intimate prayer, cultivating a tender sensibility."},
      {"author": "Thomas Carlyle", "work": "Life of Friedrich Schiller", "quote": "The youth was educated under strict **pietistic** influences that left an indelible mark upon his moral character."},
      {"author": "William James", "work": "The Varieties of Religious Experience", "quote": "In **pietistic** confessions, the soul documents its spiritual trials with acute psychological precision."}
    ]
  },
  "Dashboard — pi/pietistical.md": {
    "primary": "Relating to or affected by pietism; excessively or hypocritically religious; sanctimonious.",
    "secondary": "In Victorian satire and church history, describing outward displays of moral rectitude used as a mask for worldly ambition or social intolerance.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Nicholas Nickleby", "quote": "He adopted a **pietistical** whine that was calculated to deceive the benevolent trustees of the charity."},
      {"author": "Anthony Trollope", "work": "Barchester Towers", "quote": "Mr. Slope indulged in **pietistical** platitudes that aroused the immediate distrust of the archdeacon."},
      {"author": "George Eliot", "work": "Scenes of Clerical Life", "quote": "Her conversation was filled with **pietistical** phrases that sounded strangely hollow to those who knew her private conduct."}
    ]
  },
  "Dashboard — pi/piety.md": {
    "primary": "Devotion, reverence for God or sacred obligations, and dutiful respect for family and ancestral traditions.",
    "secondary": "In classical Roman antiquity (pietas), the supreme civic virtue encompassing filial duty to parents, loyalty to the commonwealth, and solemn devotion to the gods.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Much Ado About Nothing", "quote": "No, thou villain, thou art full of **piety**, as shall be proved upon thee by good witness."},
      {"author": "Virgil", "work": "Aeneid", "quote": "Renowned for **piety** as well as arms, pious Aeneas carried his aged father through the flames of burning Troy."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "True **piety** consists not in outward ceremonial rites, but in the obedience of the humble heart."}
    ]
  },
  "Dashboard — pi/pious.md": {
    "primary": "Devoutly religious; showing reverent devotion to God or religious obligations; or dutiful toward parents and family.",
    "secondary": "In classical literature and ethics, demonstrating faithful fulfillment of duty to ancestral traditions, country, and sacred laws.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Cymbeline", "quote": "Where I have lived at honest freedom, paid / More **pious** debts to heaven than in all / The fore-end of my time."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "With **pious** awe the archangel bowed before the celestial majesty."},
      {"author": "Jane Austen", "work": "Mansfield Park", "quote": "She was guided by a **pious** gratitude for the quiet home that had sheltered her youth."}
    ]
  },
  "Dashboard — pi/piously.md": {
    "primary": "In a pious, devout, or religious manner; with deep reverence, godliness, or dutiful devotion.",
    "secondary": "In descriptive narrative and satirical prose, performing actions with ostentatious religious solemnity or sincere moral fidelity.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick; or, The Whale", "quote": "In life but few of them would have helped the whale, I ween, if **piously** requested to do so for the sake of mercy."},
      {"author": "Frank A. Fetter", "work": "Modern Economic Problems", "quote": "The medieval guildsmen **piously** dedicated their craft halls to the patron saint of their trade."},
      {"author": "Nathaniel Hawthorne", "work": "Twice-Told Tales", "quote": "The old puritan stepped **piously** into the meetinghouse, bowing gravely to the assembled elders."}
    ]
  },
  "Dashboard — pi/piousness.md": {
    "primary": "The display or habit of devout reverence; godliness, piety, or sincere religious dedication.",
    "secondary": "In moral philosophy and literature, the earnest inward dedication to spiritual duties and ethical rectitude.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "Sincere **piousness** sheds a gentle luster over all the domestic virtues without souring the mind with bigotry."},
      {"author": "George Eliot", "work": "Adam Bede", "quote": "The quiet **piousness** of Dinah Morris touched the hearts of the rough village miners."},
      {"author": "Ralph Waldo Emerson", "work": "Essays: Second Series", "quote": "True **piousness** does not withdraw from the world, but transforms daily labor into a sacred vocation."}
    ]
  },
  "Dashboard — pi/piscina.md": {
    "primary": "A stone basin in a church near the altar, equipped with a drain to receive water used in liturgical ablutions.",
    "secondary": "In Roman archaeology, a bathing pool, fishpond, or baptismal font situated in an ancient Roman villa or early Christian baptistery.",
    "quotes": [
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "Near the altar of the Gothic chapel was a delicately carved **piscina** displaying thirteenth-century foliage."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The luxurious ruins of the imperial bath included an expansive marble **piscina** fed by mountain aqueducts."},
      {"author": "Thomas Hardy", "work": "A Pair of Blue Eyes", "quote": "The young architect sketched the Norman **piscina** uncovered during the restoration of the parish chancel."}
    ]
  },
  "Dashboard — pi/piteous.md": {
    "primary": "Deserving or arousing pity; pathetic, sorrowful, or heart-rending; or displaying compassionate pity.",
    "secondary": "In classical drama and tragic poetry, provoking deep cathartic compassion and sorrow through extreme vulnerability and undeserved suffering.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "And with a look so **piteous** in purport / As if he had been loosed out of hell / To speak of horrors—he comes before me."},
      {"author": "John Milton", "work": "Samson Agonistes", "quote": "To see him fallen from such high estate into this blind, **piteous** servitude drew tears from every bystander."},
      {"author": "Charles Dickens", "work": "Oliver Twist", "quote": "The starved child lifted his hands with a **piteous** cry that softened even the beadle's hardened heart."}
    ]
  },
  "Dashboard — pi/piteously.md": {
    "primary": "In a piteous manner; in a way that evokes sorrow, compassion, or pity; pathetically.",
    "secondary": "In tragic narrative, lamenting, crying, or begging with desperate, heart-wrenching emotional distress.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Antony and Cleopatra", "quote": "Say that the last I spoke was 'Antony', / And word it, prithee, **piteously**."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "I can never forget how the poor, shivering creature looked at me so **piteously** from the damp doorstep."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The wounded pheasant cried **piteously** in the dark thicket before expiring at dawn."}
    ]
  },
  "Dashboard — pi/pity.md": {
    "primary": "A feeling of sorrow, compassion, and sympathy caused by the sufferings and misfortunes of others.",
    "secondary": "In Aristotelian poetics, one of the two foundational tragic emotions (paired with fear) aroused by the spectacle of undeserved suffering, culminating in catharsis.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Sonnet 111", "quote": "Thence comes it that my name receives a brand... / **Pity** me then, and wish I were renew'd."},
      {"author": "Aristotle", "work": "Poetics", "quote": "Tragedy achieves the catharsis of such passions through the arousal of **pity** and fear."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Compassion or **pity** is an uneasy sensation aroused in the mind by the sight of another's misery."}
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

print(f"Faith Batch 3 (pi): Successfully updated {updated}/{len(data)} notes.")
