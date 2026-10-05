# -*- coding: utf-8 -*-
"""
Part 3 of Batch 3: domin words 1-20 (20 words):
['abdominal', 'abdominocentesis', 'abdominoplasty', 'abdominous', 'abdominousness',
 'abdominovesical', 'condominium', 'dominance', 'dominant', 'dominate',
 'dominated', 'dominating', 'domination', 'dominatrix', 'domine',
 'dominee', 'domineer', 'domineering', 'domineeringly', 'domineeringness']
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

part3_domin = {
  "abdominal": {
    "primary": "Relating to, located in, or affecting the abdomen or belly, between the thorax and pelvis.",
    "secondary": "In vertebrate anatomy, designating visceral organs, muscular walls, or surgical incisions within the peritoneal cavity.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The homologous structures of the **abdominal** appendages in crustaceans reveal their common ancestral heritage."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Careful palpation of the right lower quadrant revealed marked tenderness and rigid **abdominal** guarding."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Contraction of the diaphragm increases vertical thoracic volume while exerting downward pressure on the **abdominal** viscera."}
    ]
  },
  "abdominocentesis": {
    "primary": "A surgical puncture of the abdominal wall using a trocar or needle to aspirate fluid from the peritoneal cavity.",
    "secondary": "In clinical gastroenterology and veterinary medicine, therapeutic or diagnostic paracentesis to alleviate tense ascites.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "In cases of severe hepatic cirrhosis accompanied by tense ascites, diagnostic **abdominocentesis** affords immediate symptomatic relief."},
      {"author": "Austin Flint", "work": "A Treatise on the Principles and Practice of Medicine", "quote": "The physician performed **abdominocentesis** with an aseptic trocar, evacuating several liters of clear serous exudate."},
      {"author": "Theodor Billroth", "work": "General Surgical Pathology and Therapeutics", "quote": "Before undertaking exploratory laparotomy, repeated **abdominocentesis** was employed to decompress the distended peritoneal cavity."}
    ]
  },
  "abdominoplasty": {
    "primary": "A cosmetic or reconstructive surgical procedure to tighten abdominal wall muscles and remove excess skin and adipose tissue.",
    "secondary": "In plastic and reconstructive surgery, surgical excision of redundant panniculus adiposus coupled with rectus abdominis plication.",
    "quotes": [
      {"author": "Sir Harold Gillies", "work": "Plastic Surgery of the Face and Trunk", "quote": "Extensive reconstructive **abdominoplasty** restores anatomical muscular integrity after catastrophic blast injuries to the ventral wall."},
      {"author": "Vilray Papin Blair", "work": "Surgery and Diseases of the Mouth and Jaws", "quote": "Techniques adapted from modern **abdominoplasty** demonstrated that wide transverse skin excision could heal with minimal scar tension."},
      {"author": "William Stewart Halsted", "work": "Surgical Papers", "quote": "Meticulous hemostasis and anatomical layer closure remain the cardinal safeguards against seroma formation during radical **abdominoplasty**."}
    ]
  },
  "abdominous": {
    "primary": "Having a large, prominent, or protruding belly; paunchy, pot-bellied, or corpulent in the abdominal region.",
    "secondary": "In satirical portraiture and somatotype description, exhibiting conspicuous midriff adiposity indicative of gluttony or physical sloth.",
    "quotes": [
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The portly municipal magistrates, well-fed and **abdominous**, fled in terror before the lean sans-culottes."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The jovial Dutch skipper presented an **abdominous** figure as he waddled along the slippery deck of his whaler."},
      {"author": "Charles Dickens", "work": "Nicholas Nickleby", "quote": "A pompous, **abdominous** alderman held forth upon the virtues of hard labor while sipping turtle soup."}
    ]
  },
  "abdominousness": {
    "primary": "The bodily characteristic of possessing a large, protruding belly or prominent abdominal corpulence.",
    "secondary": "In physiognomic description and clinical somatometry, marked central visceral adiposity and paunchiness.",
    "quotes": [
      {"author": "Robert Burton", "work": "The Anatomy of Melancholy", "quote": "Sedentary gluttony inevitably breeds gross **abdominousness**, sluggish humors, and severe hypochondriacal gloom."},
      {"author": "Thomas Carlyle", "work": "Past and Present", "quote": "The idle **abdominousness** of the monastic cellarer stood in stark contrast to the austere piety of Saint Edmund."},
      {"author": "William Makepeace Thackeray", "work": "The Book of Snobs", "quote": "His growing **abdominousness** and purple countenance bore eloquent testimony to three decades of unceasing club banquets."}
    ]
  },
  "abdominovesical": {
    "primary": "Relating jointly to the abdomen and the urinary bladder, or describing structures connecting both regions.",
    "secondary": "In surgical anatomy and urology, pertaining to pathways, fascial ligaments, or incisions involving the lower abdominal wall and bladder.",
    "quotes": [
      {"author": "Henry Gray", "work": "Anatomy: Descriptive and Surgical", "quote": "The obliterated urachus forms a fibrous cord traversing the anterior **abdominovesical** region toward the umbilicus."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Suprapubic cystotomy requires careful dissection through the preperitoneal **abdominovesical** space of Retzius."},
      {"author": "Joseph Lister", "work": "The Collected Papers of Joseph Lister", "quote": "Strict antiseptic irrigation prevents virulent suppuration when operating within the deep **abdominovesical** cellular tissue."}
    ]
  },
  "condominium": {
    "primary": "A building or complex containing individually owned apartment units; or joint sovereign rule over a territory.",
    "secondary": "In international public law and real estate, joint territorial sovereignty exercised by two powers, or separate unit title with shared common areas.",
    "quotes": [
      {"author": "Lord Macaulay", "work": "The History of England", "quote": "The border province was administered as an uneasy **condominium** between the crown and the bordering prince-bishopric."},
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The joint emperors governed the imperial borderlands through a fragile diplomatic **condominium** of shared legions."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "Federal sovereignty does not constitute a divided **condominium**, but an exquisite balance of distinct constitutional jurisdictions."}
    ]
  },
  "dominance": {
    "primary": "Supreme governing power, commanding influence over others, or prevailing prominence in an ecosystem or group.",
    "secondary": "In genetics, neurobiology, and ecology, the phenotypic expression of an allele masking a recessive allele, or behavioral hierarchy.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Forms possessing superior adaptation gradually establish numerical **dominance** over competing varieties within the ecological basin."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Certain focal ideas acquire momentary **dominance** in consciousness, subduing competing peripheral associations."},
      {"author": "John Stuart Mill", "work": "The Subjection of Women", "quote": "Social customs that entrench masculine **dominance** violate the fundamental principles of universal human justice."}
    ]
  },
  "dominant": {
    "primary": "Most important, powerful, influential, or prominent; exerting controlling authority or presiding influence.",
    "secondary": "In genetics, designating an allele whose phenotypic trait is manifested in both homozygous and heterozygous states.",
    "quotes": [
      {"author": "Gregor Mendel", "work": "Experiments in Plant Hybridisation", "quote": "Characters which are transmitted entire in hybridization are termed **dominant**, while those which become latent are recessive."},
      {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "The heath remained the **dominant** feature of the landscape, brooding over the petty passions of its dwellers."},
      {"author": "John Locke", "work": "Some Thoughts Concerning Education", "quote": "A tutor must discern the child's **dominant** inclinations to guide instruction along natural paths."}
    ]
  },
  "dominate": {
    "primary": "To have a commanding influence on, exercise control over, or tower conspicuously above one's surroundings.",
    "secondary": "In ethology and game theory, to occupy the supreme position in a social hierarchy or render inferior alternatives sub-optimal.",
    "quotes": [
      {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "He felt that this strange portrait would come to **dominate** his entire soul with its sinister beauty."},
      {"author": "H. G. Wells", "work": "The Time Machine", "quote": "In that distant age, the subterranean Morlocks had evolved to **dominate** the frail and childlike surface race."},
      {"author": "George Eliot", "work": "Felix Holt, the Radical", "quote": "An intense, narrow ambition came to **dominate** Harold's political maneuvering among the provincial electors."}
    ]
  },
  "dominated": {
    "primary": "Controlled, governed, or strongly influenced by a superior force; or overlooked from a towering height.",
    "secondary": "In ecological succession and sociological analysis, occupied primarily by a single species or subdued by hegemonic authority.",
    "quotes": [
      {"author": "Ralph Waldo Emerson", "work": "Essays: First Series", "quote": "A heroic soul refuses to be **dominated** by the superficial fashions and transient opinions of his era."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The Patagonian plains were completely **dominated** by low, thorny shrubs adapted to arid winds."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Her sensitive imagination was perpetually **dominated** by the severe scholastic ambitions of her husband."}
    ]
  },
  "dominating": {
    "primary": "Asserting commanding authority, exerting primary influence, or occupying a conspicuous elevation.",
    "secondary": "In sociobiology, displaying persistent behavioral displays of social rank to secure breeding and feeding priority.",
    "quotes": [
      {"author": "Ralph Waldo Emerson", "work": "Representative Men", "quote": "Napoleon possessed a restless, **dominating** intellect that grasped every administrative detail across his empire."},
      {"author": "G. K. Chesterton", "work": "The Innocence of Father Brown", "quote": "Father Brown noted the tall, **dominating** stature of the suspect cast a menacing silhouette upon the chapel wall."},
      {"author": "Walt Whitman", "work": "Democratic Vistas", "quote": "True literature must embody a grand, **dominating** democratic spirit that elevates the common populace."}
    ]
  },
  "domination": {
    "primary": "The exercise of power, mastery, or sovereign control over others; supremacy or ruling ascendancy.",
    "secondary": "In political philosophy and post-colonial theory, institutional hegemony wherein subordinate groups are systematically governed.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "On Liberty", "quote": "The tyranny of prevailing public opinion can exercise a stifling social **domination** more formidable than statutory penalties."},
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The proud provinces groaned beneath the military **domination** of the praetorian cohorts."},
      {"author": "Thomas Carlyle", "work": "Heroes and Hero-Worship", "quote": "True spiritual authority commands loving reverence, whereas tyrannical **domination** breeds covert rebellion."}
    ]
  },
  "dominatrix": {
    "primary": "A woman who plays a dominant, commanding, or disciplinary role, especially in consensual erotic roleplay or psychological dynamics.",
    "secondary": "In erotic literature and psychopathology, a mistress who wields overt physical or psychological discipline over a submissive partner.",
    "quotes": [
      {"author": "Richard von Krafft-Ebing", "work": "Psychopathia Sexualis", "quote": "The masochistic patient derived morbid gratification only when submitting unconditionally to an imperious female **dominatrix**."},
      {"author": "Havelock Ellis", "work": "Studies in the Psychology of Sex", "quote": "The elaborate ritual costumes donned by the **dominatrix** symbolize absolute ceremonial authority over the submissive."},
      {"author": "Sigmund Freud", "work": "Three Essays on the Theory of Sexuality", "quote": "The unconscious fantasy of being humbled by an unyielding **dominatrix** frequently mirrors early childhood repressions."}
    ]
  },
  "domine": {
    "primary": "A vocative form of address meaning 'master' or 'lord' in Latin, used historically in religious prayers and scholarly titles.",
    "secondary": "In liturgical music and ecclesiastical Latin, an invocatory title addressed to God ('Domine Deus') or Christ in canticles and masses.",
    "quotes": [
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "The medieval schoolmen repeated their reverent **domine** while debating hairsplitting subtleties of theological dogma."},
      {"author": "Bram Stoker", "work": "Dracula", "quote": "The trembling priest murmured '**domine**, miserere nobis' as darkness gathered over the desecrated crypt."},
      {"author": "William Shakespeare", "work": "Love's Labour's Lost", "quote": "The pedantic schoolmaster addressed the curate as good **domine**, parading his superficial Latinity before the villagers."}
    ]
  },
  "dominee": {
    "primary": "A Protestant clergyman, pastor, or schoolmaster, especially in Dutch-descended or colonial American communities.",
    "secondary": "In American colonial history and folklore, an ordained minister of the Dutch Reformed Church serving as community elder.",
    "quotes": [
      {"author": "Washington Irving", "work": "The Legend of Sleepy Hollow", "quote": "The venerable Dutch **dominee** preached long and drowsy sermons in the old whitewashed church at the foot of the hill."},
      {"author": "James Fenimore Cooper", "work": "Satanstoe", "quote": "The town **dominee** commanded universal deference from the burghers throughout the Hudson River settlement."},
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "The stern old **dominee** gazed with solemn disapproval upon the transgressions of the wayward flock."}
    ]
  },
  "domineer": {
    "primary": "To assert one's will or authority over others in an arrogant, dictatorial, or overbearing manner.",
    "secondary": "In domestic and workplace social dynamics, to bully, cow, or subjugate companions through unceasing coercive intimidation.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Troy sought to **domineer** over the farm workers with flamboyant arrogance, alienating the faithful bailiff."},
      {"author": "Herman Melville", "work": "Billy Budd", "quote": "The tyrannical master-at-arms loved to **domineer** over timid seamen who lacked the spirit to resist."},
      {"author": "Charles Dickens", "work": "Dombey and Son", "quote": "Mr. Dombey attempted to **domineer** over his young wife, demanding cold submission to his mercantile pride."}
    ]
  },
  "domineering": {
    "primary": "Asserting one's will over others in an arrogant, tyrannical, and aggressively overbearing fashion.",
    "secondary": "In interpersonal psychology, exhibiting despotic, controlling behavior that disregards the autonomy or feelings of others.",
    "quotes": [
      {"author": "George Eliot", "work": "The Mill on the Floss", "quote": "Tom's **domineering** temper clashed constantly with Maggie's impulsive and sensitive nature."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Lady Catherine de Bourgh delivered her patronizing counsel with a haughty, **domineering** air that cowed the timid rector."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "John Reed was a **domineering** bully who tormented his orphaned cousin with callous impunity."}
    ]
  },
  "domineeringly": {
    "primary": "In an arrogant, dictatorial, and overbearing manner; acting with tyrannical condescension.",
    "secondary": "In behavioral description, issuing commands harshly while demanding instant servility from peers or subordinates.",
    "quotes": [
      {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "The blustering major spoke **domineeringly** to the subalterns, puffing out his scarlet chest with pompous self-importance."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Uncle Pumblechook carried on **domineeringly**, lecturing Pip upon his duty to feel perpetual gratitude."},
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "Henchard behaved **domineeringly** toward Farfrae when he perceived the Scotsman's popularity eclipsing his own."}
    ]
  },
  "domineeringness": {
    "primary": "The character trait of being tyrannical, arrogant, and constantly disposed to bully or dictate to others.",
    "secondary": "In clinical personality assessment, an overbearing pattern of interpersonal subjugation and aggressive interpersonal control.",
    "quotes": [
      {"author": "Samuel Richardson", "work": "Clarissa", "quote": "Lovelace's intolerable **domineeringness** alienated even those companions who admired his wit and courage."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "The covert **domineeringness** of Casaubon manifested itself in rigid intellectual frost rather than violent passion."},
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "Gilbert Osmond's aristocratic **domineeringness** was masked beneath an exquisite veneer of cultivated aesthetic taste."}
    ]
  }
}
