# -*- coding: utf-8 -*-
"""
Part 1 of Dashboard — temp (29 words: attemper to extempore)
"""
import sys
sys.stdout.reconfigure(encoding="utf-8")

part1_temp = {
  "attemper": {
    "primary": "To reduce, modify, or moderate the strength or temperature of something by blending or dilution.",
    "secondary": "In historical metallurgy and brewing, to regulate heat or alcoholic potency by mixing countervailing elements.",
    "quotes": [
      {"author": "Alexander Pope", "work": "The Odyssey of Homer", "quote": "With skillful hand the gentle bards **attemper** their strains to soothe the grief of mourning heroes."},
      {"author": "Richard Chenevix Trench", "work": "On the Study of Words", "quote": "If sweet with bitter were not wisely **attempered** still in human life, our character would remain untested."},
      {"author": "Edmund Spenser", "work": "The Faerie Queene", "quote": "She learned to **attemper** her flaming passions with wise discretion and mild counsel."}
    ]
  },
  "attempt": {
    "primary": "To make an effort to achieve, perform, or accomplish something difficult or perilous.",
    "secondary": "In criminal jurisprudence, an overt act performed with specific intent to commit a crime beyond mere preparation.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "I'll stay at home, and pray God's blessing into thy **attempt**."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Oak cast his eyes down the field in a way implying that it was useless to **attempt** argument."},
      {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "Yet they seldom **attempt** to make out a list of the a priori principles which are to serve as the premises."}
    ]
  },
  "attempted": {
    "primary": "Having been tried or undertaken, often unsuccessfully or without full fruition.",
    "secondary": "In legal indictments, qualifying a substantive criminal charge where execution fell short of completion.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "You are to know that prosperously I have **attempted**, and with bloody passage led your wars even to the gates of Rome."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "As the crook had absorbed most of Gabriel's money, he **attempted**, and carried out, an exchange of his overcoat for a shepherd's regulation smock-frock."},
      {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "It constituted the entire idea among the Hebrews, up to the birth of Christianity, as might be expected in the case of a people whose laws **attempted** to embrace all subjects on which precepts were required."}
    ]
  },
  "attempter": {
    "primary": "A person who undertakes an effort, essay, enterprise, or hostile assault.",
    "secondary": "In archaic and early modern English, an assailant who assays a fortress or makes an aggressive trial against authority.",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "The bold **attempter** of the celestial throne surveyed the gulf of darkness stretching beneath him."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Every daring **attempter** of the imperial purple found eager partisans among the mutinous frontier legions."},
      {"author": "Francis Bacon", "work": "Essays", "quote": "The rash **attempter** who seeks innovation without maturity of counsel meets inevitable disaster."}
    ]
  },
  "contemplate": {
    "primary": "To look at or view with continued attention; to observe thoughtfully or meditate deeply upon.",
    "secondary": "In philosophical theology, to engage in intuitive intellectual beholding of transcendent or ultimate truths.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "So many hours must I tend my flock; so many hours must I take my rest; so many hours must I **contemplate**; so many hours must I sport myself."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "It was with gloom he considered on landing at Liverpool that if he were to go home his reception would be of a kind very unpleasant to **contemplate**."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Farebrother, my dear sir, is a man deeply painful to **contemplate**."}
    ]
  },
  "contemplation": {
    "primary": "The action of looking thoughtfully at something for a long time; deep reflective thought.",
    "secondary": "In monastic mysticism, a quiet affective communion with the divine beyond reasoned discursive meditation.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "And did you leave him in this **contemplation**?"},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "When the waggon had passed on, Gabriel withdrew from his point of espial, and descending into the road, followed the vehicle to the turnpike-gate, where the object of his **contemplation** now halted for the payment of toll."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Meditation and water are wedded for ever in solemn **contemplation**."}
    ]
  },
  "contemplative": {
    "primary": "Expressing, involving, or given to prolonged and serious meditation or reflective thought.",
    "secondary": "In ecclesiastical classification, designating religious orders whose primary vocation is prayer, silence, and enclosure.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "That fools should be so deep-**contemplative**, and I did laugh sans intermission an hour by his dial."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Nevertheless, though the novel was intended to be neither didactic nor aggressive, in the **contemplative** parts it was oftener charged with impressions than with convictions."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Cadwallader's errand could not be despatched in the presence of grooms, so she asked to be taken into the conservatory close by, and on coming to a **contemplative** stand, she spoke."}
    ]
  },
  "contemplativeness": {
    "primary": "A persistent habit or disposition of engaging in deep, serious, and tranquil reflection.",
    "secondary": "In aesthetic psychology, the meditative repose that permits disinterested observation of beauty or artistic forms.",
    "quotes": [
      {"author": "Henry David Thoreau", "work": "A Week on the Concord and Merrimack Rivers", "quote": "There is a quiet **contemplativeness** in the fisherman's posture that harmonizes with the gentle motion of the stream."},
      {"author": "Nathaniel Hawthorne", "work": "Twice-Told Tales", "quote": "The solitary recluse preserved a serene **contemplativeness** amidst the noisy bustle of the growing township."},
      {"author": "George Eliot", "work": "Scenes of Clerical Life", "quote": "Her face wore that settled **contemplativeness** which comes from long hours spent beside the quiet hearth."}
    ]
  },
  "contemporaneity": {
    "primary": "The state or fact of existing, occurring, or flourishing during the same period of time.",
    "secondary": "In historical geology and paleontology, the synchronicity of stratigraphic strata across geographically distant formations.",
    "quotes": [
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "The apparent **contemporaneity** of widely separated fossil deposits must be evaluated with extreme caution by the field geologist."},
      {"author": "John Phillips", "work": "Memoirs of William Smith", "quote": "Smith traced the lines of **contemporaneity** across the stratified formations of the British Isles with singular accuracy."},
      {"author": "Thomas Henry Huxley", "work": "Lay Sermons, Addresses, and Reviews", "quote": "Similarity of organic forms in distant strata does not necessarily prove absolute geological **contemporaneity**."}
    ]
  },
  "contemporaneous": {
    "primary": "Existing, occurring, originating, or living in the same historical era or chronological period.",
    "secondary": "In evidentiary jurisprudence, statements made simultaneously with an event that fall under the res gestae doctrine.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Until the existence of this **contemporaneous** Wessex was acknowledged, the rustic customs were regarded as entirely obsolete."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The cold may have come on, or have ceased, earlier at one point of the globe than at another, but several large areas were **contemporaneous** in their glacial phenomena."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The testimonies of **contemporaneous** Greek historians corroborate the swift decline of the Roman military frontier."}
    ]
  },
  "contemporaneously": {
    "primary": "In a manner occurring, developing, or coexisting at the very same time or period.",
    "secondary": "In historiographical analysis, recording observations parallel to events without retrospective distortion.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "I am not, I trust, mistaken in the recognition of some deeper correspondence than that of date in the events unfolding **contemporaneously** around us."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The negotiations were conducted **contemporaneously** in London and Paris with the utmost secrecy."},
      {"author": "Herbert Spencer", "work": "First Principles", "quote": "Various physical forces act **contemporaneously** upon the evolving organism to shape its structural adaptation."}
    ]
  },
  "contemporaneousness": {
    "primary": "The characteristic of existing, developing, or taking place at the identical point in time.",
    "secondary": "In modern literary theory, the perceived immediacy and shared temporal horizon uniting author and audience.",
    "quotes": [
      {"author": "William Hazlitt", "work": "Table-Talk", "quote": "The sheer **contemporaneousness** of popular gossip lends it an ephemeral brilliance that quickly fades with the season."},
      {"author": "Henry James", "work": "The Art of Fiction", "quote": "A novel achieves vivid realism when it conveys the felt **contemporaneousness** of every human heartbeat in the narrative."},
      {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "The **contemporaneousness** of two related phenomena does not of itself establish direct reciprocal causation."}
    ]
  },
  "contemporaries": {
    "primary": "Persons living, creating, or flourishing at the same historical period as one another.",
    "secondary": "In sociology and generational cohorts, peer groups subject to the same transformative socio-political events.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Her straw bonnet, which our **contemporaries** might look at with conjectural curiosity as at an obsolete form of basket, fell a little backward."},
      {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "Next to his reserve and the faultless propriety of his conduct, his **contemporaries** at college seemed most impressed by the great maturity of his mind."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "He is not fed, sheltered, clothed, warmed, like his **contemporaries**."}
    ]
  },
  "contemporary": {
    "primary": "Belonging to, occurring in, or characteristic of the present time or a shared historical era.",
    "secondary": "In art criticism and architecture, creative practice produced after the mid-twentieth century breaking with historicist forms.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Old Mr Clare was a clergyman of a type which, within the last twenty years, has well nigh dropped out of **contemporary** life."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "The hall furniture comprised a piece of carving by a **contemporary** of Gibbons."},
      {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "This pile of chivalry, which seems so fair to those who look at the **contemporary** facts for science or entertainment, is not equally pleasant to all spectators."}
    ]
  },
  "contemporise": {
    "primary": "To cause things to synchronize in time, or to adapt something historical to current sensibilities.",
    "secondary": "In dramaturgy and stage production, setting an ancient or classical drama within a present-day cultural milieu.",
    "quotes": [
      {"author": "George Bernard Shaw", "work": "Our Theatres in the Nineties", "quote": "The director resolved to **contemporise** the Elizabethan dialogue so that modern audiences might grasp its satirical sting."},
      {"author": "Walter Pater", "work": "Appreciations", "quote": "The humanist essayists sought to **contemporise** classical virtues for the emerging civic society of their day."},
      {"author": "Oscar Wilde", "work": "The Decay of Lying", "quote": "To **contemporise** every ancient myth with crude realism is to strip romantic art of its imaginative veil."}
    ]
  },
  "contemporize": {
    "primary": "To place, coordinate, or represent occurrences within the same contemporary timeframe.",
    "secondary": "In chronometry and computational historiography, aligning divergent epochal calendars onto a single synchronized timeline.",
    "quotes": [
      {"author": "Henry Adams", "work": "The Education of Henry Adams", "quote": "The historian must strive to **contemporize** contradictory archival narratives before attempting a coherent synthesis."},
      {"author": "Matthew Arnold", "work": "Culture and Anarchy", "quote": "We must **contemporize** our intellectual ideals with the practical demands of modern industrial democracy."},
      {"author": "Thomas Carlyle", "work": "Critical and Miscellaneous Essays", "quote": "The antiquarian endeavors to **contemporize** the remote feudal struggles with our own political factions."}
    ]
  },
  "contempt": {
    "primary": "The feeling that a person or a thing is beneath consideration, worthless, or deserving scorn.",
    "secondary": "In procedural jurisprudence, willful disobedience to or open disrespect for the lawful authority of a court or legislature.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "Why, what place make you special, when you put off that with such **contempt**?"},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "In those earlier days she had always nourished a secret **contempt** for girls who were the slaves of the first good-looking young fellow."},
      {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "No one of those who profess the most sublime **contempt** for the consequences of actions as an element in their morality attaches more importance to the distinction than I do."}
    ]
  },
  "contemptibility": {
    "primary": "Utter unworthiness, baseness, or despicable character deserving universal scorn.",
    "secondary": "In ethical philosophy, the status of an agent who has thoroughly repudiated honor, duty, and civic obligation.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "Nothing sinks a claimant so swiftly into utter **contemptibility** as the boast of virtues which his conduct belies."},
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "The frivolous antics of the Parisian demagogues exposed their political program to universal **contemptibility**."},
      {"author": "Jonathan Swift", "work": "A Tale of a Tub", "quote": "The meager pretensions of the Grub Street scribblers revealed the naked **contemptibility** of their learning."}
    ]
  },
  "contemptible": {
    "primary": "Deserving of contempt, scorn, or extreme disdain; despicable and low in estimation.",
    "secondary": "In moral satire, characterizing individuals whose cowardly venality invites public ridicule and reprobation.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "Heaven and our Lady gracious hath it pleased to shine on my **contemptible** estate."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Bathsheba demurely regarded a **contemptible** straw lying upon the ground, in a way which suggested less ovine criticism than womanly embarrassment."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Might, could, would—they are **contemptible** auxiliaries."}
    ]
  },
  "contemptibly": {
    "primary": "In a manner that excites or thoroughly deserves scorn, disdain, or mean reprobation.",
    "secondary": "In behavioral critique, acting with such petty malice or cowardice as to degrade personal dignity.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "He isolated himself till the space he filled in the public eye was **contemptibly** small."},
      {"author": "Joseph Conrad", "work": "Heart of Darkness", "quote": "Sometimes he was **contemptibly** childish."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "In common life we esteem but meanly and **contemptibly** a fellow who anoints his hair, and palpably smells of that anointing."}
    ]
  },
  "contemptuous": {
    "primary": "Showing, feeling, or expressing deep hatred, scorn, or arrogant disrespect toward others.",
    "secondary": "In interpersonal communication, facial micro-expressions such as unilateral lip curl that signal perceived superiority.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "**Contemptuous** base-born callet as she is, she vaunted 'mongst her minions t'other day the very train of her worst wearing gown was better worth than all my father's lands."},
      {"author": "Lewis Carroll", "work": "Alice's Adventures in Wonderland", "quote": "When the sands are all dry, he is gay as a lark, and will talk in **contemptuous** tones of the Shark."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Featherstone handed back the letter to him with a **contemptuous** gesture, saying you don't suppose I believe a thing because Bulstrode writes it out fine."}
    ]
  },
  "contemptuously": {
    "primary": "In a scornful, haughty, or derisive manner that clearly exhibits complete disdain.",
    "secondary": "In judicial proceedings, dismissing an opponent's specious arguments with manifest judicial disregard.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "As in revenge of thy ingratitude, I throw thy name against the bruising stones, trampling **contemptuously** on thy disdain."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "What, did you think I should break in? said Boldwood, **contemptuously**."},
      {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "They **contemptuously** ask, what right hast thou to be happy? A question which Carlyle pressed with unsparing force."}
    ]
  },
  "contemptuousness": {
    "primary": "A persistent disposition or habit of looking down upon others with haughty arrogance.",
    "secondary": "In character study and dramatic dialogue, the cold superciliousness of an aristocrat scorning popular sentiment.",
    "quotes": [
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "There was a frosty **contemptuousness** in Blanche Ingram's gaze that withered every humble domestic dependent."},
      {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "The Marquis treated the entreaties of his creditors with habitual aristocratic **contemptuousness**."},
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "Osmond's quiet **contemptuousness** toward American provincialism was masked beneath impeccably polished manners."}
    ]
  },
  "distemper": {
    "primary": "A disordered physical or mental state; a contagious viral disease affecting domestic animals.",
    "secondary": "In historical painting and interior decor, a water-based paint using animal glue or casein as an adhesive binder.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "If you are sick at sea or stomach-qualmed at land, a dram of this will drive away **distemper**."},
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "She attended her sickbed; her watchful attentions triumphed over the malignity of the **distemper**."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Thus Eve with countenance blithe her story told; but in her cheek **distemper** flushing glowed."}
    ]
  },
  "extemporaneous": {
    "primary": "Spoken, performed, composed, or executed on the spur of the moment without prior preparation.",
    "secondary": "In competitive forensics and public debate, delivery where arguments are outlined in advance but delivered without a script.",
    "quotes": [
      {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "Your own gift you can present every moment with the cumulative force of a whole life's cultivation; but of the adopted talent of another, you have only an **extemporaneous**, half possession."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "His **extemporaneous** eloquence in the House of Commons swayed votes that weeks of private lobbying could not shake."},
      {"author": "Mark Twain", "work": "Autobiography", "quote": "It usually takes me more than three weeks to prepare a good **extemporaneous** speech that sounds genuinely spontaneous."}
    ]
  },
  "extemporaneously": {
    "primary": "Without premeditation, rehearsals, or prepared notes; in a spontaneous improvised manner.",
    "secondary": "In homiletics and parliamentary rhetoric, preaching or arguing fluently from general knowledge without written text.",
    "quotes": [
      {"author": "Charles Dickens", "work": "The Pickwick Papers", "quote": "Mr. Snodgrass recited several romantic stanzas **extemporaneously** to the astonishment of the assembled rural club."},
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "The venerable minister addressed the flock **extemporaneously**, his solemn words flowing directly from inward inspiration."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Holmes deduced the traveler's past career **extemporaneously**, glancing merely at the mud stains upon his boots."}
    ]
  },
  "extemporarily": {
    "primary": "In an impromptu or extemporary manner; without previous study, premeditation, or design.",
    "secondary": "In theatrical improvisation, improvising comic stage business and dialogue to accommodate unexpected audience reactions.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Antony and Cleopatra", "quote": "The quick comedians **extemporarily** will stage us, and present our Alexandrian revels."},
      {"author": "Ben Jonson", "work": "Every Man in His Humour", "quote": "He will compose a sonnet **extemporarily** upon any subject you please, before the candle burns down an inch."},
      {"author": "Samuel Johnson", "work": "The Idler", "quote": "Many young speakers vanity prompts to deliver their judgments **extemporarily**, risking foolish blunders for brief applause."}
    ]
  },
  "extemporary": {
    "primary": "Made, done, or uttered on the spur of the occasion; impromptu and lacking formal premeditation.",
    "secondary": "In ecclesiastical history, spontaneous spoken prayers contrasted with prescribed liturgical texts from a prayer book.",
    "quotes": [
      {"author": "Thomas Fuller", "work": "The Worthies of England", "quote": "His devotion shone brightest in **extemporary** prayer, when fervent piety supplied the absence of written liturgy."},
      {"author": "Joseph Addison", "work": "The Spectator", "quote": "An **extemporary** assembly gathered quickly in the coffeehouse upon hearing the startling continental rumors."},
      {"author": "John Locke", "work": "Some Thoughts Concerning Education", "quote": "He condemned the practice of burdening youth with **extemporary** tasks before fundamental principles were thoroughly grounded."}
    ]
  },
  "extempore": {
    "primary": "Carried out, spoken, or composed without preparation; impromptu or on the spur of the moment.",
    "secondary": "In classical musical performance, improvising a cadenza or accompaniment over a figured bass line.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "O villain, thou stolest a cup of sack eighteen years ago, and wert taken with the manner, and ever since thou hast blushed **extempore**."},
      {"author": "Samuel Pepys", "work": "The Diary of Samuel Pepys", "quote": "The parson preached an **extempore** sermon of an hour long, which pleased the congregation exceedingly well."},
      {"author": "Jonathan Swift", "work": "A Tale of a Tub", "quote": "The enthusiastic preacher poured forth his **extempore** meditations with uncommon zeal and vehement gestures."}
    ]
  }
}
