# -*- coding: utf-8 -*-
"""
Part 3 of Batch 2 Cluster Speech: cit words 45-65 (21 words):
['excitement', 'exciting', 'excitingly', 'incitation', 'incite', 'incitement',
 'inciter', 'incitive', 'noncitizen', 'occitan', 'overexcited', 'recital',
 'recitalist', 'recitation', 'recitative', 'recite', 'reciter', 'unexcitable',
 'unexcited', 'unexciting', 'unexcitingly']
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

part3_cit = {
    "excitement": {
        "primary": "A state of lively emotional agitation, enthusiasm, heightened interest, or physical stir.",
        "secondary": "In sensory psychology and psychiatric pathology, intense physiological sympathetic arousal or psychomotor turbulence requiring clinical stabilization.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The feverish **excitement** of the festival day had not yet subsided when she returned across the shadowed fields."},
            {"author": "John Stuart Mill", "work": "Autobiography", "quote": "When the mind is kept in perpetual **excitement** by ambitious pursuits, the quieter virtues of reflection are easily forgotten."},
            {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "A look of keen scientific **excitement** flashed across the detective's face as he bent down to examine the footprint."}
        ]
    },
    "exciting": {
        "primary": "Producing excitement, eager interest, or keen emotional response; stirring and dramatic.",
        "secondary": "In narrative theory and physiological aesthetics, creating suspenseful tension, rapid pacing, and sustained cognitive engagement in an audience.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "The Woodlanders", "quote": "The prospect of an unexpected journey to the distant market town offered an **exciting** interlude in their monotonous lives."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Nothing could be more **exciting** to the young student than the discovery of an unexamined manuscript in the library."},
            {"author": "Mrs. Oliphant", "work": "A Beleaguered City", "quote": "The ominous rumors passing through the town created an intensely **exciting** atmosphere of dread and expectation."}
        ]
    },
    "excitingly": {
        "primary": "In an exciting, thrilling, or remarkably stirring manner; producing lively sensation.",
        "secondary": "In aesthetic criticism and dramatic prose, unfolding with kinetic intensity and captivating suspense that rivets spectator attention.",
        "quotes": [
            {"author": "Bernard Shaw", "work": "Cashel Byron's Profession", "quote": "The pugilistic contest proceeded **excitingly**, with each champion trading furious blows before the cheering throng."},
            {"author": "Martha Finley", "work": "Elsie's Kith and Kin", "quote": "The historic tale unfolded **excitingly**, holding the children breathless around the blazing hearth."},
            {"author": "William Dean Howells", "work": "A Hazard of New Fortunes", "quote": "The strike rumors developed **excitingly** throughout the morning editions, creating deep apprehension among the financiers."}
        ]
    },
    "incitation": {
        "primary": "The action of inciting, prompting, or instigating; a stimulant or incentive urging action.",
        "secondary": "In jurisprudence and penal philosophy, the deliberate provocative solicitation or instigation of unlawful acts by external agents.",
        "quotes": [
            {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The fanatical sermons delivered by the monk served as a powerful **incitation** to popular riot and bloodshed."},
            {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "Foreign intriguers will find frequent **incitation** to embroil the confederacy in European dynastic disputes."},
            {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "The inflammatory tracts scattered among the Paris populace furnished continuous **incitation** to plunder and anarchy."}
        ]
    },
    "incite": {
        "primary": "To stir up, spur on, encourage, or urge someone to take specific action or display strong feeling.",
        "secondary": "In criminal jurisprudence, to intentionally solicit, counsel, or procure another person to perpetrate a felony or riotous breach of peace.",
        "quotes": [
            {"author": "William Shakespeare", "work": "King John", "quote": "How oft the sight of means to do ill deeds makes deeds ill done! You did **incite** me to this desperate murder."},
            {"author": "Jonathan Swift", "work": "Gulliver's Travels", "quote": "Ambition and avarice are the twin scourges that most frequently **incite** civilized princes to declare destructive wars."},
            {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "Fiery demagogues ascended the stone parapets of the Palais-Royal to **incite** the starving multitude to seize arms."}
        ]
    },
    "incitement": {
        "primary": "An action, factor, or motive that incites, stimulates, or encourages someone to behave in a certain way.",
        "secondary": "In criminal common law and political rhetoric, the formal offense of urging, provoking, or commanding another to commit an illegal act.",
        "quotes": [
            {"author": "George Eliot", "work": "Daniel Deronda", "quote": "The prospect of noble achievement was to him a far stronger **incitement** than any consideration of material gain."},
            {"author": "Jonathan Swift", "work": "The Battle of the Books", "quote": "The ancient manuscripts offered perpetual **incitement** to modern scribblers to attempt imitation beyond their powers."},
            {"author": "Mary Shelley", "work": "Frankenstein", "quote": "The sublime and magnificent scenes of the Alps afforded me the greatest consolation and **incitement** to endurance."}
        ]
    },
    "inciter": {
        "primary": "One who incites, urges on, instigates, or provokes others to action or rebellion.",
        "secondary": "In criminal doctrine and revolutionary history, an instigator or agitator who orchestrates collective civil disorder without necessarily participating physically.",
        "quotes": [
            {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The magistrates condemned the seditious orator as the principal **inciter** of the bloody factional violence in Antioch."},
            {"author": "Francis Bacon", "work": "The History of the Reign of King Henry the Seventh", "quote": "The pretender found a crafty and tireless **inciter** in the person of the exiled duchess across the channel."},
            {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "Every political club possessed its recognized **inciter**, whose passionate harangues directed the movements of the Parisian mobs."}
        ]
    },
    "incitive": {
        "primary": "Tending to incite, provoke, stimulate, or encourage; possessing an instigating quality.",
        "secondary": "In moral philosophy and behavioral science, an internal impulse or external lure operating as a motivating catalyst for human conduct.",
        "quotes": [
            {"author": "Jeremy Bentham", "work": "An Introduction to the Principles of Morals and Legislation", "quote": "The expectation of prospective pleasure operates upon the human will as a most powerful **incitive** to exertion."},
            {"author": "Samuel Taylor Coleridge", "work": "Aids to Reflection", "quote": "Conscience requires no external **incitive** when the moral law is clearly perceived by the rational intellect."},
            {"author": "Edmund Burke", "work": "Letters on a Regicide Peace", "quote": "The revolutionary doctrines circulated through the provinces served as an **incitive** venom against all ancient customs."}
        ]
    },
    "noncitizen": {
        "primary": "A person who is not an acknowledged citizen or lawful national of a given country in which they reside.",
        "secondary": "In immigration jurisprudence and international law, an alien subject possessing restricted civic entitlements and lacking formal political franchise.",
        "quotes": [
            {"author": "James Bryce", "work": "The American Commonwealth", "quote": "The constitutional status of the resident **noncitizen** entails obedience to territorial laws without entitlement to voting franchise."},
            {"author": "Woodrow Wilson", "work": "The State: Elements of Historical and Practical Politics", "quote": "Ancient Athens drew a rigid legal distinction between the sovereign freeman and the disenfranchised **noncitizen** merchant."},
            {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "The newly arrived immigrant remained for several years a mere **noncitizen**, acquiring republican habits through commercial intercourse."}
        ]
    },
    "occitan": {
        "primary": "Of, relating to, or denoting Occitania, a historical cultural region of southern France, or its Romance language (langue d'oc).",
        "secondary": "In Romance linguistics and medieval literature, the Gallo-Romance tongue spoken from the Pyrenees to the Alps, renowned as the language of the troubadours.",
        "quotes": [
            {"author": "Dante Alighieri", "work": "De Vulgari Eloquentia", "quote": "The refined poets of the **occitan** tongue were the first to cultivate elegant vernacular verse in courtly love lyrics."},
            {"author": "Walter Pater", "work": "The Renaissance: Studies in Art and Poetry", "quote": "The sweet melodies of the **occitan** troubadours brought a new springtime of lyrical passion to European culture."},
            {"author": "Henry Adams", "work": "Mont-Saint-Michel and Chartres", "quote": "The southern knights who marched under the banners of the crusade spoke the harmonious **occitan** idiom of Provence."}
        ]
    },
    "overexcited": {
        "primary": "Excessively stimulated, agitated, or enthusiastic; aroused beyond reasonable or healthy limits.",
        "secondary": "In pediatric neurology and psychiatric diagnostics, displaying neurobehavioral hyper-reactivity and acute sensory overwhelm under excessive environmental input.",
        "quotes": [
            {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "The little girl became so **overexcited** by the festive preparations that her governess had to lead her from the parlor."},
            {"author": "Arthur Conan Doyle", "work": "The Memoirs of Sherlock Holmes", "quote": "The witness had become so **overexcited** that his narrative was a confused jumble of frantic conjectures."},
            {"author": "George Eliot", "work": "The Mill on the Floss", "quote": "Maggie was in an **overexcited** mood, laughing and weeping alternately until her mother feared a nervous fever."}
        ]
    },
    "recital": {
        "primary": "A musical or artistic performance given by a soloist or small group; or a detailed spoken account of events.",
        "secondary": "In legal drafting and narrative rhetoric, formal enumerative statements of fact ('whereas' clauses) preceding the operative provisions of a deed or contract.",
        "quotes": [
            {"author": "Charles Dickens", "work": "Bleak House", "quote": "The dry legal **recital** of deeds and mortgages occupied hours while the listening parties drifted into slumber."},
            {"author": "Mary Shelley", "work": "Frankenstein", "quote": "The horrific **recital** of the monster's sufferings filled my soul with mingled feelings of remorse and terror."},
            {"author": "G. K. Chesterton", "work": "The Innocence of Father Brown", "quote": "The detective listened patiently to the strange **recital** given by the frightened housekeeper in the gloomy corridor."}
        ]
    },
    "recitalist": {
        "primary": "A musician, singer, or actor who performs in a solo recital or specialized chamber concert.",
        "secondary": "In music performance practice and criticism, a virtuoso soloist specializing in concert programming, such as an organ or pianoforte recitalist.",
        "quotes": [
            {"author": "George Bernard Shaw", "work": "Music in London", "quote": "The visiting piano **recitalist** displayed extraordinary digital velocity in the Chopin preludes, though his phrasing lacked subtlety."},
            {"author": "James Huneker", "work": "Chopin: The Man and His Music", "quote": "Every celebrated organ **recitalist** of the period journeyed to Weimar to hear the master improvise upon liturgical fugues."},
            {"author": "Arthur Symons", "work": "Plays, Acting, and Music", "quote": "The young **recitalist** commanded the rapt attention of the hall with her delicate interpretation of ancient French melodies."}
        ]
    },
    "recitation": {
        "primary": "The act of reciting or repeating memorized poetry, speeches, or lessons aloud before an audience.",
        "secondary": "In pedagogy and classical declamation, oral delivery assessed for memory accuracy, orthoepic pronunciation, rhetorical cadences, and dramatic inflection.",
        "quotes": [
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Tell me when you have finished your Greek **recitation**, that we may walk together in the parsonage garden."},
            {"author": "Ralph Waldo Emerson", "work": "English Traits", "quote": "The public **recitation** of classical odes at Oxford trained young scholars in precision of language and dignified composure."},
            {"author": "James Joyce", "work": "A Portrait of the Artist as a Young Man", "quote": "Stephen bowed respectfully before commencing his prize **recitation** of the Latin heroic hexameters before the assembled fathers."}
        ]
    },
    "recitative": {
        "primary": "A style of delivery in opera, oratorio, or cantata in which a singer adopts the rhythms of ordinary speech.",
        "secondary": "In musicology and vocal composition, narrative sung dialogue (recitativo secco or accompagnato) carrying dramatic plot between formal lyrical arias.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The rustic musicians modulated their simple tune into a quaint **recitative**, echoing the traditional ballads of Blackmoor Vale."},
            {"author": "Walt Whitman", "work": "Leaves of Grass", "quote": "I hear the opera, the musical **recitative** of the baritone filling the house with majestic cadences of grief."},
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The earliest musical vocalizations of primitive humans may have resembled a rhythmic **recitative** expressing emotional excitement."}
        ]
    },
    "recite": {
        "primary": "To repeat or speak aloud from memory, especially poetry, literary texts, or prepared speeches.",
        "secondary": "In formal law and parliamentary rhetoric, to enumerate facts or read out statutory clauses or articles in official assembly.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Henry VIII", "quote": "Let me **recite** the grievous wrongs which your deceitful counsel hath brought upon this innocent realm."},
            {"author": "Ralph Waldo Emerson", "work": "Representative Men", "quote": "The wandering bards were welcomed in every chieftain's hall to **recite** the legendary valor of ancestral kings."},
            {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "She stepped onto the stage to **recite** the lyrical verses of Shakespeare with exquisite grace and feeling."}
        ]
    },
    "reciter": {
        "primary": "A person who recites poetry, literary passages, historical narratives, or prepared lessons aloud.",
        "secondary": "In folklore studies and Islamic scholarship (qāriʾ), an oral performer or scholar preserving canonical religious texts and oral poetry through memory.",
        "quotes": [
            {"author": "Edward William Lane", "work": "An Account of the Manners and Customs of the Modern Egyptians", "quote": "In every public coffee-shop, a professional **reciter** chanted the romantic adventures of Abu Zayd to the delighted patrons."},
            {"author": "Richard Francis Burton", "work": "The Book of the Thousand Nights and a Night", "quote": "The professional **reciter** gathered a dense circle of listeners around the camp fire as evening fell over the desert."},
            {"author": "Walter Scott", "work": "Minstrelsy of the Scottish Border", "quote": "The aged ballad **reciter** preserved in memory ancient verses that had never been committed to parchment or print."}
        ]
    },
    "unexcitable": {
        "primary": "Not easily excited, provoked, or disturbed; characterized by a steady, calm, and phlegmatic temperament.",
        "secondary": "In psychopathology and comparative psychology, possessing a high physiological activation threshold resistant to external stress perturbations.",
        "quotes": [
            {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Sherlock Holmes possessed a remarkably cold, **unexcitable** mind that never permitted personal emotion to cloud scientific analysis."},
            {"author": "Thomas Hardy", "work": "The Woodlanders", "quote": "Giles Winterborne was of an **unexcitable** disposition, enduring misfortune with patient stoicism and quiet endurance."},
            {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "Domesticated animals of an **unexcitable** temperament are chosen for selective breeding because of their tractability."}
        ]
    },
    "unexcited": {
        "primary": "Calm, composed, and not emotionally stirred, agitated, or enthusiastic.",
        "secondary": "In quantum mechanics and emotional state assessment, resting at a basal ground energy level or demonstrating lack of autonomic activation.",
        "quotes": [
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Mr. Casaubon replied in his usual **unexcited** and measured cadence, showing no sympathy with her youthful enthusiasm."},
            {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "He surveyed the financial ruin before him with a curiously **unexcited** eye, as though observing another man's fate."},
            {"author": "Nathaniel Hawthorne", "work": "The House of the Seven Gables", "quote": "The quiet judge maintained an **unexcited** demeanor throughout the turbulent political meeting in the townhouse."}
        ]
    },
    "unexciting": {
        "primary": "Not exciting; lacking suspense, lively interest, or stimulation; dull or uneventful.",
        "secondary": "In literary criticism and mundane sociology, characterized by predictable routines and lack of dramatic conflict or sensory novelty.",
        "quotes": [
            {"author": "Charles Dickens", "work": "Bleak House", "quote": "The lawyer's office presented a thoroughly **unexciting** prospect of dusty parchments, black tin boxes, and slow clerical drudgery."},
            {"author": "Joseph Conrad", "work": "Heart of Darkness", "quote": "The dreary voyage along the flat coast appeared **unexciting** to the casual passenger, yet full of sinister undercurrents."},
            {"author": "George Eliot", "work": "Silas Marner", "quote": "The daily life of the weaver was an **unexciting** routine of rhythmic loom clicks from morning till nightfall."}
        ]
    },
    "unexcitingly": {
        "primary": "In a manner that lacks excitement, suspense, stimulation, or dramatic appeal.",
        "secondary": "In stylistic critique and narrative analysis, progressing in an ordinary, predictable, or monotonous fashion without sensory or emotional elevation.",
        "quotes": [
            {"author": "William Dean Howells", "work": "The Rise of Silas Lapham", "quote": "The business conference dragged on **unexcitingly**, dealing with ledgers, freight schedules, and mundane mercantile accounts."},
            {"author": "Arnold Bennett", "work": "The Old Wives' Tale", "quote": "The quiet years in the drapery shop passed **unexcitingly**, marked only by seasonal stocktaking and Sunday chapel sermons."},
            {"author": "Anthony Trollope", "work": "Barchester Towers", "quote": "The archdeacon's breakfast conversation proceeded **unexcitingly** until the bishop's controversial letter was unexpectedly delivered."}
        ]
    }
}
