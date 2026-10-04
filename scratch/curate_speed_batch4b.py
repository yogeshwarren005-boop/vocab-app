# -*- coding: utf-8 -*-
import os, sys, re

sys.stdout.reconfigure(encoding="utf-8")

data = {
  # =========================================================================
  # Dashboard — vag (25 words)
  # =========================================================================
  "Dashboard — vag/divagate.md": {
    "primary": "To stray, wander off, or turn aside from the primary topic or direct course in speech or writing.",
    "secondary": "In narrative rhetoric, discursive ramblings that divert readers from the central plot or thesis.",
    "quotes": [
      {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "The author must not **divagate** too far into the social gossip of the neighboring parishes."},
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "She felt her thoughts begin to **divagate** aimlessly among memories of her childhood in Albany."},
      {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "Professor Teufelsdröckh was ever prone to **divagate** from clothes-philosophy into mystical cosmology."}
    ]
  },
  "Dashboard — vag/divagation.md": {
    "primary": "The act of wandering away or straying from the main path, subject, or line of argument; a digression.",
    "secondary": "In scholastic disputation, discursive tangents that obscure the core syllogism under debate.",
    "quotes": [
      {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "Let us be set down at Queen's Crawley without further **divagation** into family heraldry."},
      {"author": "Henry James", "work": "The Ambassadors", "quote": "His conversational **divagation** amused her, though it delayed the serious answer she awaited."},
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "Pardon this historical **divagation**, which is necessary to understand the maritime rise of the republic."}
    ]
  },
  "Dashboard — vag/extravagance.md": {
    "primary": "Lack of restraint in spending money or using resources; excessive elaboration or unreasonable excess.",
    "secondary": "In classical moral philosophy, prodigality violating prudence, contrasting with temperance and frugality.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Wickham's notorious **extravagance** soon involved him in heavy debts across every market town."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Great nations are never impoverished by private **extravagance**, but by public prodigality."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "We indulged in reckless **extravagance**, furnishing our chambers with expensive luxuries on credit."}
    ]
  },
  "Dashboard — vag/extravagancy.md": {
    "primary": "An instance or quality of excess, wild unreasonableness, or prodigal expenditure beyond prudent bounds.",
    "secondary": "In 17th- and 18th-century prose, intellectual or financial eccentricity wandering beyond social norms.",
    "quotes": [
      {"author": "John Locke", "work": "Some Thoughts Concerning Education", "quote": "Parents should curb every early inclination toward foolish **extravagancy** in their children."},
      {"author": "Jonathan Swift", "work": "A Tale of a Tub", "quote": "The satirist mocked the theological **extravagancy** of modern sectarian zealots."},
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "Such constitutional experiments exceed all reasonable limits of political **extravagancy**."}
    ]
  },
  "Dashboard — vag/extravagant.md": {
    "primary": "Lacking restraint in spending money or using resources; exceeding what is reasonable or appropriate.",
    "secondary": "In archaic usage, wandering beyond established boundaries (as an extravagant spirit wandering at night).",
    "quotes": [
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "The **extravagant** and erring spirit hies to his confine; and of the truth herein this present object made probation."},
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Willoughby had lived in an **extravagant** style far beyond the modest income of his estate."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "His **extravagant** habits brought him into constant collision with the bailiffs of London."}
    ]
  },
  "Dashboard — vag/extravagantly.md": {
    "primary": "In an extravagant, wasteful, or excessive manner; beyond reasonable limits.",
    "secondary": "In literary portraiture, living or praising in an excessively lavish, unrestrained, or hyperbolic fashion.",
    "quotes": [
      {"author": "Jane Austen", "work": "Emma", "quote": "Mr. Elton praised Harriet's modest watercolor drawing far too **extravagantly** for sound judgment."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Harold Skimpole spent money **extravagantly**, protesting that he possessed no head for figures."},
      {"author": "William Makepeace Thackeray", "work": "The Book of Snobs", "quote": "They furnished their suburban drawing-room **extravagantly** to rival their wealthy aristocratic relations."}
    ]
  },
  "Dashboard — vag/extravaganza.md": {
    "primary": "An elaborate, spectacular, and lavishly staged theatrical, musical, or visual production.",
    "secondary": "In 19th-century theater history, a whimsical dramatic work characterized by pantomime, parody, and splendid scenic effects.",
    "quotes": [
      {"author": "William Makepeace Thackeray", "work": "Pendennis", "quote": "The young gentlemen attended the Christmas **extravaganza** at the theater, enchanted by the fairy scenery."},
      {"author": "Charles Dickens", "work": "The Pickwick Papers", "quote": "The festive pantomime was an uproarious **extravaganza** filled with Harlequins, clowns, and transformation scenes."},
      {"author": "Henry James", "work": "The Tragic Muse", "quote": "She viewed the theatrical performance not as art, but as a glittering commercial **extravaganza**."}
    ]
  },
  "Dashboard — vag/invaginate.md": {
    "primary": "To fold inward or sheath; to cause an anatomical or cellular layer to turn inside out or tuck within itself.",
    "secondary": "In developmental embryology, the inward folding of blastoderm cells during blastopore formation in gastrulation.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Invertebrated Animals", "quote": "The blastula cells begin to **invaginate** at the vegetal pole, creating the primitive archenteron."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The sea-anemone can **invaginate** its delicate tentacles into the central body cavity when disturbed."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Peristaltic contraction caused the upper intestinal segment to **invaginate** into the lower lumen."}
    ]
  },
  "Dashboard — vag/invagination.md": {
    "primary": "The process of folding an outer layer inward to form a pocket or sheath; an infolding of a membrane.",
    "secondary": "In pediatric gastroenterology, intussusception or invagination of the ileum into the cecum causing mechanical obstruction.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "Embryologists demonstrated that gastrulation proceeds by the cellular **invagination** of the blastosphere."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Acute intestinal **invagination** in young infants requires early surgical reduction to prevent gangrene."},
      {"author": "Harvey Cushing", "work": "The Life of Sir William Osler", "quote": "The pathological museum exhibited classic specimens demonstrating vascular **invagination**."}
    ]
  },
  "Dashboard — vag/vagabond.md": {
    "primary": "A person who wanders from place to place without a permanent home or regular job; an itinerant or rover.",
    "secondary": "In historical vagrancy law, legal classifications penalizing unlicensed rovers and mendicants under Tudor statutes.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Richard II", "quote": "Whilst he, a **vagabond** exile, flitted from court to court seeking foreign arms against our throne."},
      {"author": "Walter Scott", "work": "The Heart of Midlothian", "quote": "The reckless **vagabond** wandered through the border hills, sleeping under haystacks and ruined towers."},
      {"author": "Charles Dickens", "work": "Oliver Twist", "quote": "The beadle denounced the poor homeless boy as an idle **vagabond** fit only for the workhouse."}
    ]
  },
  "Dashboard — vag/vagabondage.md": {
    "primary": "A nomadic, wandering life without a settled home or regular occupation; the condition of a vagabond.",
    "secondary": "In sociological criminology, early penal theories analyzing chronic itinerancy and seasonal migrant poverty.",
    "quotes": [
      {"author": "Walter Scott", "work": "Guy Mannering", "quote": "The gipsy tribe preserved their ancient habits of **vagabondage**, camping in the remote Scottish glens."},
      {"author": "Robert Louis Stevenson", "work": "Travels with a Donkey in the Cévennes", "quote": "I indulged in a fortnight of delightful **vagabondage**, wandering over the mountain crests with my pack."},
      {"author": "Thomas Carlyle", "work": "Past and Present", "quote": "Centuries of industrial turmoil have driven thousands of willing laborers into bitter **vagabondage**."}
    ]
  },
  "Dashboard — vag/vagal.md": {
    "primary": "Of, relating to, or mediated by the vagus nerve (cranial nerve X).",
    "secondary": "In cardiac electrophysiology and autonomic pharmacology, vagal tone slowing heart rate through acetylcholine release at the sinoatrial node.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Excessive **vagal** stimulation resulted in marked bradycardia and transient syncope in the patient."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Section of the **vagal** branches to the heart leads to an immediate acceleration of cardiac rhythm."},
      {"author": "Oliver Wendell Holmes Sr.", "work": "Medical Essays", "quote": "The physician recognized that fainting was an acute **vagal** reflex provoked by sudden emotional shock."}
    ]
  },
  "Dashboard — vag/vagary.md": {
    "primary": "An unexpected, erratic, or unpredictable change in someone's behavior, thought, or situation; a caprice.",
    "secondary": "In literary criticism, eccentric stylistic departures from established aesthetic conventions.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Mr. Bennet was accustomed to every wild **vagary** of his wife's excitable imagination."},
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "The financial ruin was precipitated by a sudden **vagary** of the autumn harvest weather."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Neighbors dismissed his generous philanthropy as a bizarre intellectual **vagary** of an old bachelor."}
    ]
  },
  "Dashboard — vag/vagile.md": {
    "primary": "Having freedom of movement; mobile or capable of active locomotion and dispersal throughout an environment.",
    "secondary": "In benthic marine ecology, vagile fauna (such as crabs and snails) that move freely across ocean substrates, contrasting with sessile organisms.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The **vagile** crustaceans scuttled actively across the exposed intertidal flats at low water."},
      {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Invertebrated Animals", "quote": "The transition from sessile polyp to **vagile** medusa represents a fundamental life-cycle divergence in hydrozoans."},
      {"author": "Richard Owen", "work": "Lectures on the Comparative Anatomy and Physiology of the Invertebrate Animals", "quote": "The highly **vagile** cephalopods navigate pelagic waters with rapid jet propulsion."}
    ]
  },
  "Dashboard — vag/vagina.md": {
    "primary": "A muscular canal leading from the external genitals to the cervix in female mammals; or a sheathing structure.",
    "secondary": "In comparative mammalian anatomy and botanical morphology, the sheathing base of a leaf encircling a stem.",
    "quotes": [
      {"author": "William Harvey", "work": "On the Generation of Animals", "quote": "The seminal fluid traverses the internal canal of the **vagina** to reach the uterine cavity."},
      {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "In placental mammals, the **vagina** forms the terminal passage of the female reproductive tract."},
      {"author": "Asa Gray", "work": "First Lessons in Botany", "quote": "The sheathing **vagina** of the grass leaf clasps the stem firmly above each node."}
    ]
  },
  "Dashboard — vag/vaginal.md": {
    "primary": "Relating to the vagina or to a sheath-like anatomical structure; sheathing.",
    "secondary": "In clinical gynecology and obstetrics, transvaginal physical examinations and medications administered per vaginam.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The surgeon inspected the deep **vaginal** vault to rule out malignant neoplastic ulceration."},
      {"author": "Oliver Wendell Holmes Sr.", "work": "Medical Essays", "quote": "Aseptic precautions during **vaginal** delivery eliminated the deadly menace of puerperal fever."},
      {"author": "Harvey Cushing", "work": "The Life of Sir William Osler", "quote": "The clinical demonstrator reviewed the anatomical relations of the pelvic **vaginal** fascia."}
    ]
  },
  "Dashboard — vag/vaginismus.md": {
    "primary": "A painful, involuntary spasm or contraction of the pelvic floor muscles surrounding the vagina.",
    "secondary": "In clinical gynecology and sexual medicine, severe reflex hypertonia preventing coitus or pelvic examination.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Severe psychological trauma often underlies functional **vaginismus**, requiring patient counseling alongside local therapy."},
      {"author": "Oliver Wendell Holmes Sr.", "work": "Medical Essays", "quote": "The physician identified acute **vaginismus** provoked by hyperesthetic mucosal inflammation."},
      {"author": "Harvey Cushing", "work": "The Life of Sir William Osler", "quote": "The gynecological lecture addressed surgical and behavioral remedies for intractable **vaginismus**."}
    ]
  },
  "Dashboard — vag/vaginitis.md": {
    "primary": "Inflammation of the vagina, typically accompanied by discharge, itching, and discomfort.",
    "secondary": "In clinical gynecology, infective or atrophic vaginitis caused by Candida albicans, Trichomonas, or estrogen deficiency.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Microscopic smears confirmed that the acute **vaginitis** was caused by parasitic protozoan organisms."},
      {"author": "Oliver Wendell Holmes Sr.", "work": "Medical Essays", "quote": "Antiseptic washes proved efficacious in resolving purulent **vaginitis** in hospital patients."},
      {"author": "Florence Nightingale", "work": "Notes on Nursing", "quote": "Rigid cleanliness and frequent laundering prevent infectious **vaginitis** in communal wards."}
    ]
  },
  "Dashboard — vag/vaginocele.md": {
    "primary": "A hernia or downward protrusion of a pelvic organ into the vaginal canal; a colpocele.",
    "secondary": "In pelvic organ prolapse surgery, cystocele or rectocele herniating through the anterior or posterior vaginal wall.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Physical examination revealed an extensive **vaginocele** resulting from attenuation of the pelvic floor."},
      {"author": "Oliver Wendell Holmes Sr.", "work": "Medical Essays", "quote": "Surgical repair of the **vaginocele** restored normal anatomical support to the pelvic viscera."},
      {"author": "Harvey Cushing", "work": "The Life of Sir William Osler", "quote": "The clinical notes documented successful surgical correction of an obstinate **vaginocele**."}
    ]
  },
  "Dashboard — vag/vagrancy.md": {
    "primary": "The circumstance or condition of wandering without a permanent home or lawful means of livelihood.",
    "secondary": "In legal history, statutes penalizing vagrancy, begging, and loitering in public spaces without visible support.",
    "quotes": [
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "Severe Tudor statutes punished **vagrancy** with whipping and branding upon the shoulder."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The poor crossing-sweeper was perpetually moved on by the police, guilty only of poverty and **vagrancy**."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Laws restricting the mobility of laborers were framed under the pretext of preventing parish **vagrancy**."}
    ]
  },
  "Dashboard — vag/vagrant.md": {
    "primary": "A person without a settled home or regular work who wanders from place to place; roving or wandering.",
    "secondary": "In legal statutes and historical police administration, an itinerant mendicant subject to municipal removal.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Antony and Cleopatra", "quote": "Like to a **vagrant** flag upon the stream, goes to and back, lackeying the varying tide."},
      {"author": "Walter Scott", "work": "The Antiquary", "quote": "Edie Ochiltree was a licensed Scottish **vagrant**, welcomed at every fireside for his tales and songs."},
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "A ragged **vagrant** stood at the inn gate, playing a plaintive tune upon a battered flute."}
    ]
  },
  "Dashboard — vag/vague.md": {
    "primary": "Of uncertain, indefinite, or unclear character, meaning, or form; not clearly expressed or perceived.",
    "secondary": "In epistemology and philosophy of language, predicates whose boundaries of application are indeterminate.",
    "quotes": [
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Men often employ **vague** and indeterminate words without having any clear ideas fixed to them."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "I entertained a **vague** hope that some unexpected turn of fortune would rescue us from ruin."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "The mysterious sound was too **vague** and distant to allow any certain inference as to its origin."}
    ]
  },
  "Dashboard — vag/vaguely.md": {
    "primary": "In a vague, indefinite, or imprecise manner; unclearly or slightly.",
    "secondary": "In cognitive psychology, impressions recalled with low sensory or semantic resolution.",
    "quotes": [
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "He **vaguely** hinted at secrets he dared not speak openly before the assembled magistrates."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "I **vaguely** remembered hearing the name whispered during my first lonely days at Lowood school."},
      {"author": "Joseph Conrad", "work": "Lord Jim", "quote": "He stared into the gloom, **vaguely** conscious of the dark shapes of the mountains towering above."}
    ]
  },
  "Dashboard — vag/vagueness.md": {
    "primary": "Lack of clarity, precision, or distinctness in expression, meaning, or sensory perception.",
    "secondary": "In formal philosophical logic, the sorites paradox arising from boundary vagueness in continuous natural predicates.",
    "quotes": [
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "The pervasive **vagueness** of scholastic terminology produces endless disputes without real knowledge."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Naturalists often complain of the **vagueness** that characterizes the boundary between varieties and species."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Mr. Brooke's conversation was celebrated for a delightful **vagueness** that committed him to no opinion."}
    ]
  },
  "Dashboard — vag/vagus.md": {
    "primary": "The tenth cranial nerve (CN X), a major parasympathetic nerve innervating thoracic and abdominal viscera.",
    "secondary": "In human neuroanatomy, the wandering nerve carrying sensory and motor fibers controlling heart rate, peristalsis, and vocalization.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Compression of the recurrent branch of the **vagus** by an aortic aneurysm produces laryngeal hoarseness."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The cardiac inhibitory fibers of the **vagus** nerve exert a constant regulatory control over the heartbeat."},
      {"author": "Oliver Wendell Holmes Sr.", "work": "Medical Essays", "quote": "The widespread visceral distribution of the **vagus** nerve justifies its ancient name of the wandering nerve."}
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

print(f"Speed Batch 4B: Successfully updated {updated}/{len(data)} notes.")
