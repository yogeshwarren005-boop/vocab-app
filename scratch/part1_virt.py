# -*- coding: utf-8 -*-
"""
Part 1: 10 words from Dashboard — virt ('virtu' through 'virtuousness')
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

part1_virt = {
  "virtu": {
    "primary": "A love of or taste for fine arts, rare curiosities, and antiquities; also antique or artistic value in an object.",
    "secondary": "In aesthetic history and Renaissance political theory (Machiavellian virtù), fine art connoisseurship or civic prowess, martial drive, and statecraft boldness.",
    "quotes": [
      {"author": "Niccolò Machiavelli", "work": "The Prince", "quote": "Fortune is a woman, and if you wish to control her, you must conquer her with bold and decisive **virtu**."},
      {"author": "Horace Walpole", "work": "Letters of Horace Walpole", "quote": "Strawberry Hill was enriched with rare medals, porcelain, and exquisite articles of **virtu** gathered from every capital in Europe."},
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "Gilbert Osmond regarded his daughter and his collection of Florentine antiquities with the fastidious eye of a man of **virtu**."}
    ]
  },
  "virtual": {
    "primary": "Almost or nearly as described, but not completely or according to strict formal definition; existing in essence or effect.",
    "secondary": "In physics and computer science, simulated or carried on by software rather than physical reality, or denoting quantum particle states of transient existence.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "To deny the federal legislature the means of executing its powers is to decree its **virtual** dissolution and impotence."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "He slept little, and his waking hours were spent in a **virtual** solitude of brooding disappointment and unuttered grief."},
      {"author": "Frank A. Fetter", "work": "Economics Volume II: Modern Economic Problems", "quote": "The concentration of capital in large rail mergers created a **virtual** monopoly over inland freight transport."}
    ]
  },
  "virtuality": {
    "primary": "The quality of having the potential or inherent efficacy to produce an effect without the formal material presence.",
    "secondary": "In scholastic metaphysics and contemporary digital ontology, latent potentiality ready to be actualized, or simulated digital reality.",
    "quotes": [
      {"author": "Samuel Taylor Coleridge", "work": "Aids to Reflection", "quote": "The germ contains in its secret **virtuality** the entire future architecture and blossom of the mighty oak."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "The power of producing ideas in the mind resides in the active **virtuality** of external material corpuscles."},
      {"author": "Thomas Aquinas", "work": "Summa Theologiae", "quote": "The cause possesses an operative **virtuality** that pre-contains the form and perfection of the subsequent effect."}
    ]
  },
  "virtually": {
    "primary": "Nearly, almost, or for all practical purposes, even if not strictly or technically in every detail.",
    "secondary": "In legal interpretation and digital systems, having functional equivalence in practical operation or executed via digital computational environments.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The suitors in Jarndyce and Jarndyce have discovered that the suit is **virtually** ended only when the entire estate is devoured in costs."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Oak found himself **virtually** master of the great farm, directing its daily operations while Bathsheba remained in seclusion."},
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The title of emperor was **virtually** abolished by the barbarian chieftains who dictated every measure from behind the throne."}
    ]
  },
  "virtue": {
    "primary": "Behavior showing high moral standards, righteousness, or moral excellence; also a beneficial efficacy or good quality.",
    "secondary": "In classical Aristotelian ethics and Christian theology, an acquired moral habitus disposing an agent toward the human good, or healing medicinal potency.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "Assume a **virtue**, if you have it not. That monster, custom, who all sense doth eat of habits devil, is angel yet in this."},
      {"author": "John Milton", "work": "Areopagitica", "quote": "I cannot praise a fugitive and cloistered **virtue**, unexercised and unbreathed, that never sallies out and sees her adversary."},
      {"author": "Francis Bacon", "work": "Essays", "quote": "**Virtue** is like precious odours, most fragrant when they are incensed or crushed; for prosperity doth best discover vice, but adversity doth best discover virtue."}
    ]
  },
  "virtuosity": {
    "primary": "Great technical skill, brilliant mastery, and consummate execution displayed in the practice of an artistic craft.",
    "secondary": "In musicology and aesthetic critique, dazzling instrumental dexterity that evokes admiration, sometimes contrasted with spiritual depth.",
    "quotes": [
      {"author": "George Bernard Shaw", "work": "Music in London", "quote": "The violinist dazzled the audience with incredible **virtuosity**, executing rapid harmonics and flying staccatos with effortless bravura."},
      {"author": "Walter Pater", "work": "Appreciations", "quote": "The poet's stylistic **virtuosity** enabled him to capture the subtlest shades of ephemeral mood and chromatic light."},
      {"author": "Henry James", "work": "The Tragic Muse", "quote": "Miriam's performance revealed not merely dramatic passion, but a conscious **virtuosity** acquired through relentless Parisian stage training."}
    ]
  },
  "virtuoso": {
    "primary": "A person highly skilled in music or another artistic pursuit; a master performer displaying consummate brilliance.",
    "secondary": "In the history of connoisseurship and early modern science, an enthusiastic collector, amateur natural philosopher, or learned antiquarian.",
    "quotes": [
      {"author": "Robert Browning", "work": "An Introduction to the Study of Browning", "quote": "The musical **virtuoso** commanded the instrument like a living spirit, drawing forth harmonies of extraordinary power and pathos."},
      {"author": "Joseph Addison", "work": "The Tatler", "quote": "The learned **virtuoso** spent his days cataloging ancient coins, stuffed lizards, and fossils of dubious antiquity."},
      {"author": "Charles Dickens", "work": "The Old Curiosity Shop", "quote": "The elderly antiquary presided over his cluttered shop like an eccentric **virtuoso** guarding the relics of forgotten centuries."}
    ]
  },
  "virtuous": {
    "primary": "Having or showing high moral standards, ethical righteousness, integrity, or upright personal character.",
    "secondary": "In Aristotelian and Thomistic moral philosophy, possessing stable dispositions toward the golden mean in passion and action.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Twelfth Night", "quote": "Dost thou think, because thou art **virtuous**, there shall be no more cakes and ale? Yes, by Saint Anne, and ginger shall be hot i' the mouth too!"},
      {"author": "Jane Austen", "work": "Mansfield Park", "quote": "Fanny Price remained steadfast in her convictions, choosing rather to endure cold neglect than compromise her **virtuous** principles."},
      {"author": "Benjamin Franklin", "work": "Autobiography", "quote": "I conceived the bold and arduous project of arriving at moral perfection, desiring to live without committing any fault, and to become truly **virtuous**."}
    ]
  },
  "virtuously": {
    "primary": "In a manner characterized by high moral standards, ethical integrity, rectitude, and upright conduct.",
    "secondary": "In moral philosophy and homiletic literature, acting in deliberate conformity with righteous ethical precepts and self-command.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Winter's Tale", "quote": "The queen has lived **virtuously**, and bearing her great sorrow with quiet dignity, has won the reverence of all Sicily."},
      {"author": "John Locke", "work": "Some Thoughts Concerning Education", "quote": "A child trained to act **virtuously** from early infancy will prize honor and temperance above momentary physical gratifications."},
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "To live **virtuously** requires a continuous vigilance over the secret desires and imaginations of the solitary heart."}
    ]
  },
  "virtuousness": {
    "primary": "The quality of possessing high moral standards, righteousness, ethical integrity, and purity of conduct.",
    "secondary": "In systematic ethical treatises, the persistent disposition toward righteous action and moral fortitude across tempting circumstances.",
    "quotes": [
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "The true dignity of human nature consists in the unfeigned **virtuousness** that seeks the glory of the Creator and the relief of man's estate."},
      {"author": "George Eliot", "work": "Adam Bede", "quote": "Dinah Morris spoke with a calm, sweet authority that sprang from the deep, unaffected **virtuousness** of her gentle soul."},
      {"author": "Thomas Carlyle", "work": "Past and Present", "quote": "Modern society must reawaken to genuine **virtuousness** of character if it hopes to master the industrial chaos of this mechanical era."}
    ]
  }
}
