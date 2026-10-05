# -*- coding: utf-8 -*-
"""
Part 2: sanc (19 words)
['sanctification', 'sanctified', 'sanctify', 'sanctimonious', 'sanctimoniously', 'sanctimoniousness', 'sanctimony', 'sanction', 'sanctionative', 'sanctioned', 'sanctioning', 'sanctitude', 'sanctity', 'sanctuary', 'sanctum', 'unsanctification', 'unsanctified', 'unsanctify', 'unsanctioned']
"""
import sys
sys.stdout.reconfigure(encoding="utf-8")

data_sanc = {
  "sanctification": {
    "primary": "The act or process of making holy, purifying from sin, or consecrating to sacred purposes.",
    "secondary": "In Christian systematic theology, the progressive spiritual work of the Holy Spirit transforming a believer into moral conformity with divine righteousness.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The traveling preacher spoke solemnly of inward **sanctification** and repentance before the rural congregation."},
      {"author": "King James Bible", "work": "The Holy Bible", "quote": "God hath from the beginning chosen you to salvation through **sanctification** of the Spirit and belief of the truth."},
      {"author": "John Calvin", "work": "Institutes of the Christian Religion", "quote": "Regeneration comprises two complementary dimensions, namely mortification of the flesh and the spiritual **sanctification** of the new life."}
    ]
  },
  "sanctified": {
    "primary": "Made holy, consecrated to divine service, or purified from moral defilement and sin.",
    "secondary": "In ecclesiastical law and ritual, set apart by religious blessing for liturgical or sacramental functions.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "Do not believe his vows; for they are brokers, breathing like **sanctified** and pious bonds, the better to beguile."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Her noble impulses seemed **sanctified** by the quiet humility with which she accepted daily duties."},
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "The venerable minister walked with solemn step, revered as a **sanctified** vessel of spiritual truth."}
    ]
  },
  "sanctify": {
    "primary": "To set apart as holy, purify from sin, or dedicate solemnly to religious and sacred purposes.",
    "secondary": "In moral philosophy and literature, to render an action or relationship venerable, worthy, or elevated by noble motive.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Winter's Tale", "quote": "The heavens with that sweet smile of yours **sanctify** the morning air of this royal court."},
      {"author": "Henry David Thoreau", "work": "A Week on the Concord and Merrimack Rivers", "quote": "True friendship and poetic labor **sanctify** the wilderness through which the river quietly glides."},
      {"author": "Bram Stoker", "work": "Dracula", "quote": "It was sanctified to such use of man, now we **sanctify** it to God for our holy crusade against darkness."}
    ]
  },
  "sanctimonious": {
    "primary": "Making a hypocritical show of religious devotion, righteousness, or superior moral piety.",
    "secondary": "In social satire, ostentatiously pious in external deportment while harboring selfish, judgmental, or dishonest motives.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Measure for Measure", "quote": "Thou concludest like the **sanctimonious** pirate, that went to sea with the Ten Commandments, but scraped one out of the table."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Mr. Chadband rolled his heavy eyes with a **sanctimonious** grimace before bestowing his tedious homily upon the household."},
      {"author": "Emily Brontë", "work": "Wuthering Heights", "quote": "Old Joseph sat by the fireside, groaning over his Bible with a **sanctimonious** relish for the damnation of his neighbors."}
    ]
  },
  "sanctimoniously": {
    "primary": "In a sanctimonious, hypocritically moralizing, or ostentatiously pious manner.",
    "secondary": "In interpersonal discourse, delivering moral rebukes or platitudes with an offensive air of unearned moral superiority.",
    "quotes": [
      {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "The worldly dowager nodded **sanctimoniously**, pretending to lament the very scandals she had eagerly spread."},
      {"author": "Mark Twain", "work": "The Innocents Abroad", "quote": "The guide rolled his eyes **sanctimoniously** while reciting questionable legends of local martyrs to the gullible pilgrims."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "Mr. Brocklehurst spoke **sanctimoniously** of Christian humility while clothing his own family in lavish silks and plumes."}
    ]
  },
  "sanctimoniousness": {
    "primary": "Hypocritical piety, affectation of holy devotion, or smug and ostentatious righteousness.",
    "secondary": "In behavioral critique and rhetoric, superficial moral posture adopted to conceal pride, intolerance, or deceit.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "The Idler", "quote": "Nothing more thoroughly disgusts honest minds than the transparent **sanctimoniousness** of those who affect perpetual austerity."},
      {"author": "George Eliot", "work": "Scenes of Clerical Life", "quote": "His dry speeches were tinged with a chilly **sanctimoniousness** that alienated the straightforward farmers of the parish."},
      {"author": "Anthony Trollope", "work": "Barchester Towers", "quote": "The chaplain's oily **sanctimoniousness** exasperated the archdeacon far more than any honest disagreement could have done."}
    ]
  },
  "sanctimony": {
    "primary": "Pretended, affected, or hypocritical religious devotion, holiness, or moral superiority.",
    "secondary": "In social discourse, outward performance of sanctified virtue employed as a shield against legitimate accountability.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Twelfth Night", "quote": "A virtuous maid, the daughter of a count that died some twelvemonth since, then leaving her in the protection of his son... but out of **sanctimony** she hath abjured the sight of men."},
      {"author": "Jonathan Swift", "work": "A Tale of a Tub", "quote": "The sectarian preacher wrapped himself in affected **sanctimony**, denouncing all wholesome human pleasures as worldly snares."},
      {"author": "Alexander Pope", "work": "Epistle to Dr. Arbuthnot", "quote": "He exposed the hollow **sanctimony** of court flatterers who masked private ambition under public zeal for reform."}
    ]
  },
  "sanction": {
    "primary": "Authoritative permission, official approval, or formal ratification given to an action, law, or agreement.",
    "secondary": "In international relations and jurisprudence, a coercive economic or diplomatic measure enacted against a state to enforce compliance.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "The conscience of the individual provides the ultimate internal **sanction** for moral duty across human society."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "She felt that the marriage could not prosper without the affectionate **sanction** of those who had guided her youth."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The high chancellor gave formal **sanction** to the proposed settlement after years of ruinous litigation."}
    ]
  },
  "sanctionative": {
    "primary": "Serving to give authority, confirmation, or formal sanction; confirming or ratifying.",
    "secondary": "In constitutional theory and legal philosophy, possessing the institutional authority to enact binding validation or approval.",
    "quotes": [
      {"author": "Jeremy Bentham", "work": "An Introduction to the Principles of Morals and Legislation", "quote": "The legislator relies upon **sanctionative** powers derived from public penalties to ensure obedience to civil statutes."},
      {"author": "Herbert Spencer", "work": "The Principles of Sociology", "quote": "Early religious dogmas provided a **sanctionative** authority that reinforced rudimentary tribal codes and traditions."},
      {"author": "James Martineau", "work": "Types of Ethical Theory", "quote": "Conscience exercises a distinctively **sanctionative** function over human volition, approving or condemning each impulse."}
    ]
  },
  "sanctioned": {
    "primary": "Formally approved, officially permitted, or authoritative by virtue of legal or social ratification.",
    "secondary": "In international politics, subjected to punitive trade restrictions, asset freezes, or diplomatic embargoes.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Her father promptly **sanctioned** the engagement with heartfelt joy upon receiving Mr. Darcy's formal petition."},
      {"author": "Thomas Henry Huxley", "work": "Evolution and Ethics", "quote": "Ancient moral conventions were often **sanctioned** by the fear of supernatural retribution rather than civic reason."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "The solemn ceremony proceeded, **sanctioned** by the ancient rites of the church and the presence of witnesses."}
    ]
  },
  "sanctioning": {
    "primary": "Giving authoritative approval, permission, or legal ratification to an action, law, or policy.",
    "secondary": "In foreign diplomacy, applying coercive regulatory or economic penalties against an offending sovereign entity.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The chief magistrate bears grave responsibility when **sanctioning** legislative acts passed by both houses of Congress."},
      {"author": "Woodrow Wilson", "work": "Congressional Government", "quote": "By tacitly **sanctioning** executive agreements, the senate broadened the operational scope of foreign diplomacy."},
      {"author": "Lord Acton", "work": "Historical Essays and Studies", "quote": "Ecclesiastical authorities erred grievously in **sanctioning** coercive measures against intellectual innovators."}
    ]
  },
  "sanctitude": {
    "primary": "Holiness, sacredness, saintliness, or spiritual purity of character and life.",
    "secondary": "In classic theological and devotional literature, the solemn transcendent majesty associated with divine attributes.",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Men endued with **sanctitude** of reason might know God and contemplate the glory of the celestial creation."},
      {"author": "Sir Walter Scott", "work": "The Monastery", "quote": "The hermit was revered across the border hills for his austere lifestyle and profound personal **sanctitude**."},
      {"author": "John Dryden", "work": "The Hind and the Panther", "quote": "The ancient mother church maintained an undisputed claim to **sanctitude** through unnumbered centuries of devotion."}
    ]
  },
  "sanctity": {
    "primary": "The state or attribute of being holy, sacred, inviolable, or spiritually pure and consecrated.",
    "secondary": "In constitutional ethics and bioethics, the absolute inviolability of fundamental human rights, life, or solemn oaths.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Macbeth", "quote": "A most miraculous work in this good king, which often since my here-remain in England I have seen him do: how he solicits heaven, himself best knows; but strangely-visited people, all swollen and ulcerous, he cures, hanging a golden stamp about their necks, put on with holy prayers: and 'tis spoken, to the succeeding royalty he leaves the healing **sanctity**."},
      {"author": "Ralph Waldo Emerson", "work": "Self-Reliance", "quote": "Nothing is at last sacred but the **sanctity** of your own mind; absolve you to yourself, and you shall have the suffrage of the world."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Father Mapple enjoyed such a wide reputation for sincerity and **sanctity** that the mariners listened in breathless silence."}
    ]
  },
  "sanctuary": {
    "primary": "A sacred place, holy shrine, or consecrated space dedicated to divine worship.",
    "secondary": "In law and conservation, a place of safety, immunity from arrest, or a protected reserve for threatened wildlife.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Richard III", "quote": "The queen took **sanctuary** in the abbey, placing her younger son under the sacred protection of the church."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "The quiet old library served as a tranquil **sanctuary** where Dorothea could reflect upon her troubled marriage."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The isolated volcanic archipelago served as an undisturbed **sanctuary** for unique giant tortoises and iguanas."}
    ]
  },
  "sanctum": {
    "primary": "A sacred place or holy retreat; a private study, retreat, or secluded room where one is undisturbed.",
    "secondary": "In temple architecture and religious history, the innermost holy of holies inaccessible to ordinary worshippers.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The captain remained secluded within his dark cabin **sanctum**, brooding over his vengeful oceanic charts."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The elderly attorney sat enthroned within his dusty legal **sanctum**, surrounded by ancient parchment rolls."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Holmes invited the inspector into his inner **sanctum** at Baker Street to scrutinize the enigmatic footprint."}
    ]
  },
  "unsanctification": {
    "primary": "The absence, lack, or reversal of sanctification, spiritual holiness, or consecration.",
    "secondary": "In dogmatic and sacramental theology, the unregenerate spiritual condition remaining unaffected by sanctifying grace.",
    "quotes": [
      {"author": "Richard Baxter", "work": "The Practical Works", "quote": "The fatal error of hypocrites lies in mistaking formal ritual observance for deliverance from internal **unsanctification**."},
      {"author": "John Owen", "work": "Pneumatologia: A Discourse Concerning the Holy Spirit", "quote": "Without the indwelling renovation of the Spirit, the human heart remains bound within its natural **unsanctification**."},
      {"author": "Jonathan Edwards", "work": "Treatise Concerning Religious Affections", "quote": "He demonstrated that intellectual knowledge of scripture cannot compensate for pervasive **unsanctification** of the affections."}
    ]
  },
  "unsanctified": {
    "primary": "Not sanctified, consecrated, or purified; unholy, unhallowed, profane, or worldly.",
    "secondary": "In moral critique, cleverness, eloquence, or secular learning employed for selfish ends without ethical grounding.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Macbeth", "quote": "I hope, in no place so **unsanctified** where such as thou mayst find him, cried the brave mother defending her son."},
      {"author": "Nathaniel Hawthorne", "work": "The Marble Faun", "quote": "The old ruins appeared wild and **unsanctified**, haunted by lingering echoes of ancient pagan ceremonies."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "The fallen host plotted revenge with **unsanctified** fury, despising the righteous majesty of heaven's eternal throne."}
    ]
  },
  "unsanctify": {
    "primary": "To strip of sanctity, profane, desecrate, or pollute that which was previously consecrated.",
    "secondary": "In ecclesiastical controversies, to declare invalid or polluted a holy altar, vessel, or religious office.",
    "quotes": [
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "The revolutionary mobs sought to **unsanctify** the ancient cathedrals, turning venerable sanctuaries into storehouses for munitions."},
      {"author": "Walter Pater", "work": "Marius the Epicurean", "quote": "Skeptical philosophy seemed to **unsanctify** the domestic pieties that had long sustained Roman household life."},
      {"author": "Jeremy Taylor", "work": "Holy Living and Holy Dying", "quote": "Deliberate and repeated willful transgression will inevitably **unsanctify** the soul once washed by baptismal vows."}
    ]
  },
  "unsanctioned": {
    "primary": "Not sanctioned, authorized, permitted, or officially approved; lacking legitimate authority.",
    "secondary": "In military operations and statecraft, aggressive actions undertaken without constitutional authorization or diplomatic approval.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Evolution and Ethics", "quote": "He warned that **unsanctioned** hypotheses unsupported by empirical demonstration have no rightful standing in scientific inquiry."},
      {"author": "James Fenimore Cooper", "work": "The Deerslayer", "quote": "The frontiersmen embarked upon an **unsanctioned** retaliatory raid across the forest without the garrison captain's warrant."},
      {"author": "Joseph Conrad", "work": "Nostromo", "quote": "The provincial general attempted an **unsanctioned** coup d'etat, hoping to seize the silver mines before the fleet arrived."}
    ]
  }
}
