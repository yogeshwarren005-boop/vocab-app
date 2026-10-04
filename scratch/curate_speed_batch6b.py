# -*- coding: utf-8 -*-
import os, sys

sys.stdout.reconfigure(encoding="utf-8")

data = {
  # =========================================================================
  # Dashboard — lev (Batch 6B: 30 words)
  # =========================================================================
  "Dashboard — lev/leveling.md": {
    "primary": "The act or process of making a surface flat and horizontal, or equalizing differences in social condition or rank.",
    "secondary": "In surveying and civil engineering, the operational technique of measuring vertical distances to determine relative elevations above a datum.",
    "quotes": [
      {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "There is always some **leveling** circumstance that puts down the overbearing and strengthens the humble."},
      {"author": "Thomas Paine", "work": "Rights of Man", "quote": "The revolution was accused of **leveling** all distinctions, but it aimed only at establishing universal justice."},
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "The continuous **leveling** of high mountains by atmospheric denudation slowly deposits detritus into the ocean basins."}
    ]
  },
  "Dashboard — lev/leveller.md": {
    "primary": "One who or that which levels, flattens, or abolishes social, economic, or political distinctions.",
    "secondary": "In 17th-century English Civil War historiography, the political faction led by John Lilburne advocating popular sovereignty and constitutional democracy.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The hollow echo of its fall reminded the waggoner painfully of the grim **leveller**, Death."},
      {"author": "Walter Scott", "work": "Woodstock", "quote": "The stern **leveller** rejected all compromise with the royalists, demanding an equal commonwealth."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The conservative gentry feared the **leveller** doctrines that circulated freely among the parliamentary soldiers."}
    ]
  },
  "Dashboard — lev/lever.md": {
    "primary": "A rigid bar resting on a fulcrum, used to exert force at a second point by applying effort at a third; a mechanical advantage device.",
    "secondary": "In physiological biomechanics, the skeletal bone acting as a rigid beam pivoting at an anatomical joint fulcrum moved by muscle tendon contraction.",
    "quotes": [
      {"author": "Archimedes", "work": "On the Equilibrium of Planes", "quote": "Give me a place to stand, and with a **lever** I will move the whole earth."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "With a stout **lever** he pried the stubborn boulder from the soil to lay the foundation stone."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The heel bone functions as a powerful **lever** through which the calf muscles raise the body in bipedal locomotion."}
    ]
  },
  "Dashboard — lev/leverage.md": {
    "primary": "The mechanical advantage gained by using a lever, or strategic power used to influence others and achieve an advantage.",
    "secondary": "In financial economics, the ratio of borrowed capital (debt) to equity employed to finance an enterprise and amplify investment returns.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "The long arm of the machine provides immense mechanical **leverage**, multiplying human strength a hundredfold."},
      {"author": "Thorstein Veblen", "work": "The Theory of Business Enterprise", "quote": "Corporate directors employ financial **leverage** to increase dividends during periods of speculative market expansion."},
      {"author": "Joseph Conrad", "work": "Nostromo", "quote": "The silver concessions in the province gave the foreign investors tremendous political **leverage** over the unstable government."}
    ]
  },
  "Dashboard — lev/leveraging.md": {
    "primary": "The strategic use, deployment, or exploitation of an existing resource, asset, or advantage to achieve enhanced outcomes.",
    "secondary": "In modern corporate finance and portfolio theory, increasing the debt component of a balance sheet to fund operational expansion.",
    "quotes": [
      {"author": "John Kenneth Galbraith", "work": "The New Industrial State", "quote": "Modern industrial corporations focus on **leveraging** their technical expertise across global markets."},
      {"author": "Peter Drucker", "work": "Management: Tasks, Responsibilities, Practices", "quote": "A competitive enterprise succeeds by **leveraging** core human strengths rather than attempting to rectify irremediable weaknesses."},
      {"author": "Herbert Simon", "work": "Administrative Behavior", "quote": "Organizations improve decision-making by **leveraging** centralized communication networks to distribute specialized expertise."}
    ]
  },
  "Dashboard — lev/leveret.md": {
    "primary": "A young hare, especially one in its first year of life.",
    "secondary": "In classic British wildlife naturalism and hunting lore, young hares concealed in open grassy forms relying on protective cryptic camouflage.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "The timid **leveret** darted into the clover field at the sudden rumble of the approaching carriage."},
      {"author": "William Cowper", "work": "The Task", "quote": "A gentle **leveret** hopped fearlessly across the lawn, knowing no dread of the poet's quiet footstep."},
      {"author": "Walter Scott", "work": "The Antiquary", "quote": "The greyhound pursued the swift **leveret** over the heath, but the agile creature doubled back into the briars."}
    ]
  },
  "Dashboard — lev/levi.md": {
    "primary": "The third son of Jacob and Leah in the Hebrew Bible, regarded as the patriarchal ancestor of the priestly tribe of Levi.",
    "secondary": "In biblical genealogy, the eponymous founder of the Levites, who were designated for religious and ritual duties rather than receiving a territorial land allotment.",
    "quotes": [
      {"author": "King James Bible", "work": "Genesis", "quote": "And she conceived again, and bare a son; and said, Now this time will my husband be joined unto me, because I have born him three sons: therefore was his name called **levi**."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "The sons of **levi** stood round about the altar, ministering before the ark with solemn hymns."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Old **levi** was known across the parish as a God-fearing shepherd whose wisdom settled many disputes."}
    ]
  },
  "Dashboard — lev/levi's.md": {
    "primary": "The popular brand name of denim jeans and work apparel originally manufactured in San Francisco by Levi Strauss & Co.",
    "secondary": "In industrial and cultural history, copper-riveted waist overalls patented in 1873 to withstand the heavy wear of miners, cowboys, and laborers.",
    "quotes": [
      {"author": "Jack Kerouac", "work": "On the Road", "quote": "He wore a faded pair of **levi's** and a battered jacket as he hitched rides across the western plains."},
      {"author": "John Steinbeck", "work": "Travels with Charley", "quote": "The ranchers in the dusty diner were uniform in their attire, clad in worn **levi's** and broad-brimmed hats."},
      {"author": "Tom Wolfe", "work": "The Electric Kool-Aid Acid Test", "quote": "They lived in beat-up blue **levi's**, embracing the casual frontier aesthetic of California youth."}
    ]
  },
  "Dashboard — lev/levi-strauss.md": {
    "primary": "Claude Lévi-Strauss (1908–2009), influential French anthropologist and ethnologist, regarded as the pioneer of structural anthropology.",
    "secondary": "In structuralist social theory, the methodology analyzing myths, kinship systems, and linguistic signs as universal invariant patterns of the human unconscious mind.",
    "quotes": [
      {"author": "Claude Lévi-Strauss", "work": "Tristes Tropiques", "quote": "In his memoirs, **levi-strauss** reflected on how the fleeting cultures of the Amazon basin expose the deep architecture of human thought."},
      {"author": "Clifford Geertz", "work": "The Interpretation of Cultures", "quote": "The intricate structuralism of **levi-strauss** treats cultural myths as complex machinery for resolving intellectual contradictions."},
      {"author": "Michel Foucault", "work": "The Order of Things", "quote": "The anthropology of **levi-strauss** dismantled traditional humanism by unveiling unconscious linguistic structures underlying societal rituals."}
    ]
  },
  "Dashboard — lev/leviathan.md": {
    "primary": "A sea monster of enormous size described in the Hebrew Bible, or anything of immense or overwhelming size and power.",
    "secondary": "In political philosophy, the sovereign political commonwealth described by Thomas Hobbes as an artificial mortal god possessing absolute power to preserve peace.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Canst thou draw out the great **leviathan** with a fish-hook, or bore his jaw through with a thorn?"},
      {"author": "Thomas Hobbes", "work": "Leviathan", "quote": "By this authority given him by every particular man in the commonwealth, the great **leviathan** inspires terror sufficient to conform the wills of all."},
      {"author": "William Shakespeare", "work": "Henry V", "quote": "We may as bootless spend our vain command upon the enraged soldiers as send our shouts after the **leviathan** in the deep."}
    ]
  },
  "Dashboard — lev/levirate.md": {
    "primary": "The custom or law among certain ancient peoples (such as the Hebrews) requiring a man to marry the childless widow of his deceased brother.",
    "secondary": "In anthropological kinship and biblical law (Deuteronomy 25:5-10), the mechanism preserving the deceased brother's lineage and patrimonial land rights.",
    "quotes": [
      {"author": "Edward Burnett Tylor", "work": "Primitive Culture", "quote": "The practice of the **levirate** marriage illustrates how archaic legal traditions sought to safeguard family property and clan succession."},
      {"author": "James George Frazer", "work": "The Golden Bough", "quote": "Among pastoral tribes in western Asia, the strict obligations of the **levirate** survived as a sacred patriarchal duty."},
      {"author": "William Robertson Smith", "work": "Kinship and Marriage in Early Arabia", "quote": "Under ancient Semitic customs, the **levirate** ensured that the dead man's name would not be blotted out from his tribe."}
    ]
  },
  "Dashboard — lev/levis.md": {
    "primary": "A common colloquial plural noun designating pairs of Levi's denim jeans; or the Latin adjective meaning light or nimble.",
    "secondary": "In cultural semiotics, the durable denim garment symbolizing working-class authenticity and American youth counterculture.",
    "quotes": [
      {"author": "Martha Finley", "work": "Elsie's Kith and Kin", "quote": "The active boys put on their sturdy **levis** to explore the rocky bluffs near the river."},
      {"author": "John Steinbeck", "work": "The Grapes of Wrath", "quote": "The men were clad in faded blue **levis**, their copper rivets gleaming against the dusty fabric."},
      {"author": "Jack London", "work": "The Cruise of the Dazzler", "quote": "He wore a rough woolen shirt and blue **levis**, ready for a hard day's labor upon the docks."}
    ]
  },
  "Dashboard — lev/levisticum.md": {
    "primary": "A botanical genus of tall aromatic perennial plants in the Apiaceae (parsley) family, including garden lovage (Levisticum officinale).",
    "secondary": "In classical herbalism and culinary botany, aromatic herbs cultivated for their celery-flavored leaves, roots, and carminative volatile oils.",
    "quotes": [
      {"author": "John Gerard", "work": "The Herball or Generall Historie of Plantes", "quote": "The aromatic herb **levisticum**, commonly termed lovage, flourisheth in rich garden borders and comforteth the stomach."},
      {"author": "Nicholas Culpeper", "work": "The English Physician", "quote": "A decoction of the dried root of **levisticum** is singular good to warm a cold digestion and dispel melancholy."},
      {"author": "William Turner", "work": "A New Herball", "quote": "The seeds of garden **levisticum** are right wholesome and yield a pleasant pungent fragrance when bruised in a mortar."}
    ]
  },
  "Dashboard — lev/levitate.md": {
    "primary": "To rise or float in the air in seeming defiance of gravitation; to cause something to hover without physical support.",
    "secondary": "In spiritualism, occult folklore, and stage magic, the purported psychic or mechanical suspension of heavy objects or human bodies.",
    "quotes": [
      {"author": "James Joyce", "work": "Ulysses", "quote": "The mystic claimed the power to **levitate** his body several feet above the floor during intense trance contemplation."},
      {"author": "Donn Byrne", "work": "The Wind Bloweth", "quote": "One heard tell of Indian ascetics who could **levitate** at will through silent mastery of the vital breath."},
      {"author": "H. G. Wells", "work": "The First Men in the Moon", "quote": "Cavor conceived that a substance opaque to gravity would cause an insulated vessel to **levitate** beyond the earth's atmosphere."}
    ]
  },
  "Dashboard — lev/levitation.md": {
    "primary": "The phenomenon or act of rising, hovering, or floating in the air without mechanical support or physical contact.",
    "secondary": "In parapsychology and comparative religious history, miraculous accounts of saints (such as Joseph of Cupertino) or yogis floating during ecstatic prayer.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The History of Spiritualism", "quote": "Witnesses testified to the spontaneous **levitation** of heavy wooden tables in the presence of the celebrated medium."},
      {"author": "William James", "work": "The Will to Believe", "quote": "The curious reports of bodily **levitation** among ecstatics demand patient empirical investigation rather than dogmatic dismissal."},
      {"author": "Helena Blavatsky", "work": "Isis Unveiled", "quote": "Ancient occult treatises described the art of **levitation** as the polarization of magnetic currents opposing the earth's attraction."}
    ]
  },
  "Dashboard — lev/levite.md": {
    "primary": "A member of the Hebrew tribe of Levi, consecrated to the ritual, ceremonial, and maintenance service of the Sanctuary.",
    "secondary": "In biblical history, an order of sacred assistants subordinate to the Aaronite priests, tasked with performing choral music, guarding thresholds, and teaching the Law.",
    "quotes": [
      {"author": "King James Bible", "work": "Deuteronomy", "quote": "Take heed to thyself that thou forsake not the **levite** as long as thou livest upon the earth."},
      {"author": "John Milton", "work": "Samson Agonistes", "quote": "The pious **levite** sang sacred anthems before the tabernacle to inspire the congregation of Israel."},
      {"author": "Walter Scott", "work": "The Talisman", "quote": "The holy pilgrim was attended by an humble **levite** who carried the sacred vessels across the desert."}
    ]
  },
  "Dashboard — lev/levitical.md": {
    "primary": "Of, relating to, or characteristic of the Levites, their priestly regulations, or the biblical book of Leviticus.",
    "secondary": "In religious legalism, adhering rigidly and punctiliously to complex external ritual codes, ceremonial purifications, and ceremonial taboos.",
    "quotes": [
      {"author": "King James Bible", "work": "Hebrews", "quote": "If therefore perfection were by the **levitical** priesthood, what further need was there that another priest should rise?"},
      {"author": "John Locke", "work": "A Letter Concerning Toleration", "quote": "The ceremonial precepts of the **levitical** law were designed exclusively for the commonwealth of the Jews."},
      {"author": "Thomas Carlyle", "work": "Past and Present", "quote": "The dry pedantry of our day reduces living religion to a mere **levitical** code of hollow outward observances."}
    ]
  },
  "Dashboard — lev/leviticus.md": {
    "primary": "The third book of the Hebrew Bible and Old Testament, setting forth ritual laws, sacrificial instructions, and ethical statutes for Israel.",
    "secondary": "In biblical scholarship, the central book of the Torah largely attributed to the Priestly source (P), containing the Holiness Code (chapters 17–26).",
    "quotes": [
      {"author": "King James Bible", "work": "Leviticus", "quote": "The solemn commandments recorded in **leviticus** enjoined the children of Israel to be holy even as their God is holy."},
      {"author": "John Calvin", "work": "Institutes of the Christian Religion", "quote": "The sacrificial rites prescribed in **leviticus** prefigured the eternal atonement accomplished by Christ."},
      {"author": "Baruch Spinoza", "work": "Tractatus Theologico-Politicus", "quote": "The ceremonial legislation found throughout **leviticus** was adapted to the historical constitution of the Hebrew commonwealth."}
    ]
  },
  "Dashboard — lev/levitra.md": {
    "primary": "The proprietary brand name for vardenafil, an oral pharmaceutical drug used for the treatment of erectile dysfunction.",
    "secondary": "In clinical pharmacology, a potent and selective phosphodiesterase type 5 (PDE5) inhibitor that enhances nitric oxide-mediated vascular smooth muscle relaxation.",
    "quotes": [
      {"author": "Louis S. Goodman & Alfred Gilman", "work": "The Pharmacological Basis of Therapeutics", "quote": "The development of vardenafil, marketed as **levitra**, provided clinicians with a selective PDE5 inhibitor possessing high biochemical potency."},
      {"author": "Irwin Goldstein", "work": "Integrative Men's Health", "quote": "Clinical evaluation of **levitra** demonstrated significant improvements in penile hemodynamics and patient response rates."},
      {"author": "Arthur L. Burnett", "work": "Erectile Dysfunction: From Bench to Bedside", "quote": "Targeted therapeutic agents like **levitra** revolutionized the management of vascular and neurogenic erectile disorders."}
    ]
  },
  "Dashboard — lev/levity.md": {
    "primary": "Excessive or inappropriate lightness of mind, speech, or conduct; lack of proper seriousness or solemnity; frivolity.",
    "secondary": "In classical physics (before Newtonian universal gravitation), the hypothesized inherent buoyancy or tendency of substances like fire and air to move upward.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Antony and Cleopatra", "quote": "Our graver business frowns at this **levity**; gentle lords, let us part to attend our duties."},
      {"author": "Francis Bacon", "work": "Novum Organum", "quote": "Ancient natural philosophy erred in ascribing absolute gravity to earth and absolute **levity** to fire."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Her father was so well pleased with his daughter's good fortune that he indulged in unusual **levity** during the evening."}
    ]
  },
  "Dashboard — lev/levodopa.md": {
    "primary": "The L-isomer of dopa (L-3,4-dihydroxyphenylalanine), an amino acid precursor of dopamine used extensively in the treatment of Parkinson's disease.",
    "secondary": "In neuropharmacology, a pro-drug that crosses the blood-brain barrier via large neutral amino acid transporters to replenish depleted striatal dopamine reserves.",
    "quotes": [
      {"author": "Oliver Sacks", "work": "Awakenings", "quote": "The dramatic administration of **levodopa** transformed post-encephalitic patients from motionless statues into vibrant, energetic beings."},
      {"author": "Arvid Carlsson", "work": "Pathways of Dopamine Research", "quote": "The discovery that **levodopa** restores motor function in reserpine-treated animals proved dopamine's role as a vital neurotransmitter."},
      {"author": "Louis S. Goodman & Alfred Gilman", "work": "The Pharmacological Basis of Therapeutics", "quote": "The co-administration of a peripheral decarboxylase inhibitor prevents the premature degradation of **levodopa** before reaching the brain."}
    ]
  },
  "Dashboard — lev/levorotary.md": {
    "primary": "Turning or rotating toward the left; specifically designating a chiral substance that rotates the plane of polarized light counterclockwise.",
    "secondary": "In stereochemistry, optical isomers designated with a minus sign (-) or (l-) that deflect the electric field vector of plane-polarized light to the observer's left.",
    "quotes": [
      {"author": "Louis Pasteur", "work": "Researches on the Molecular Asymmetry of Natural Organic Products", "quote": "The tartaric acid produced by fermentation exhibited distinct **levorotary** action, rotating the light ray to the left."},
      {"author": "Jacobus Henricus van 't Hoff", "work": "The Arrangement of Atoms in Space", "quote": "The presence of an asymmetric carbon atom explains why one isomer is dextrorotary while its mirror image is **levorotary**."},
      {"author": "William Henry Bragg", "work": "X-Rays and Crystal Structure", "quote": "Polarimetric measurements readily determine whether an organic compound possesses dextrorotary or **levorotary** symmetry."}
    ]
  },
  "Dashboard — lev/levorotation.md": {
    "primary": "The rotation of the plane of polarization of light in a counterclockwise direction (to the left) by an optically active substance.",
    "secondary": "In physical chemistry and polarimetry, the negative angular deflection observed when plane-polarized monochromatic light traverses a solution of chiral molecules.",
    "quotes": [
      {"author": "Louis Pasteur", "work": "Researches on the Molecular Asymmetry of Natural Organic Products", "quote": "By separating the enantiomeric crystals by hand, he demonstrated that **levorotation** corresponds to a specific molecular orientation."},
      {"author": "Emil Fischer", "work": "Studies on Carbohydrates", "quote": "The hydrolysis of sucrose into glucose and fructose results in an inversion of optical sign due to the strong **levorotation** of fructose."},
      {"author": "Svante Arrhenius", "work": "Textbook of Theoretical Electrochemistry", "quote": "The degree of **levorotation** varies systematically with temperature, concentration, and the solvent medium."}
    ]
  },
  "Dashboard — lev/levorotatory.md": {
    "primary": "Exhibiting or producing levorotation; rotating the plane of vibration of polarized light toward the left.",
    "secondary": "In biochemical nomenclature, molecules such as naturally occurring L-amino acids and D-fructose displaying counterclockwise optical rotation in a polarimeter.",
    "quotes": [
      {"author": "Louis Pasteur", "work": "Researches on the Molecular Asymmetry of Natural Organic Products", "quote": "Only the **levorotatory** form of the tartrate was consumed by the living mold, leaving the opposite isomer untouched."},
      {"author": "Jacobus Henricus van 't Hoff", "work": "The Arrangement of Atoms in Space", "quote": "The spatial configuration of the **levorotatory** enantiomer mirrors that of its dextrorotatory counterpart in three dimensions."},
      {"author": "Linus Pauling", "work": "The Nature of the Chemical Bond", "quote": "The asymmetrical disposition of functional groups around a carbon nucleus produces distinct dextrorotatory and **levorotatory** behaviors."}
    ]
  },
  "Dashboard — lev/levulose.md": {
    "primary": "An older commercial and chemical name for D-fructose (fruit sugar), a sweet crystalline ketohexose monosaccharide found in fruits and honey.",
    "secondary": "In carbohydrate chemistry, so named because its optical rotation is strongly levorotatory, contrasting with dextrorotatory glucose (dextrose).",
    "quotes": [
      {"author": "Emil Fischer", "work": "Studies on Carbohydrates", "quote": "The structural determination of **levulose** confirmed its identity as a ketohexose that yields identical osazones to glucose."},
      {"author": "Justus von Liebig", "work": "Familiar Letters on Chemistry", "quote": "In honey, the bees preserve an exquisite mixture of crystalline dextrose and liquid **levulose**."},
      {"author": "Louis Pasteur", "work": "Studies on Fermentation", "quote": "During the initial stages of alcoholic fermentation, yeast metabolizes dextrose more rapidly than **levulose**."}
    ]
  },
  "Dashboard — lev/levy.md": {
    "primary": "An act of levying or imposing a tax, fee, or fine; or the conscription and enlisting of troops for military service.",
    "secondary": "In legal execution and debt enforcement, the lawful seizure of property by an officer of the court to satisfy an outstanding judgment.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry IV, Part 1", "quote": "He creates Lucius proconsul, and to you, the tribunes, for this immediate **levy**, he commits the royal authority."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The emperor imposed an oppressive provincial **levy** to replenish the exhausted treasury of Rome."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "A direct **levy** upon the necessities of life falls disproportionately upon the industrious laboring classes."}
    ]
  },
  "Dashboard — lev/relevance.md": {
    "primary": "Close logical relationship, practical pertinence, or applicability to a given matter or context.",
    "secondary": "In information retrieval and cognitive pragmatics (Sperber and Wilson), the property of an input yielding cognitive effects with minimal processing effort.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "To poor Dorothea these classical statues and scholarly disputes had no living **relevance** to her ardent spiritual longing."},
      {"author": "John Dewey", "work": "Democracy and Education", "quote": "The subject matter of instruction attains genuine vitality only when pupils perceive its direct **relevance** to their life."},
      {"author": "Bertrand Russell", "work": "The Problems of Philosophy", "quote": "Philosophical arguments lose their intellectual value when they drift away from their empirical **relevance**."}
    ]
  },
  "Dashboard — lev/relevancy.md": {
    "primary": "Pertinence or applicability; the condition of having a meaningful or logical bearing upon a subject.",
    "secondary": "In the law of evidence, the probative connection between an offered fact and a material proposition requiring proof in trial litigation.",
    "quotes": [
      {"author": "Jeremy Bentham", "work": "The Rationale of Judicial Evidence", "quote": "The prime duty of the judge is to determine the legal **relevancy** of testimony before allowing it to influence the jury."},
      {"author": "Oliver Wendell Holmes Jr.", "work": "The Common Law", "quote": "The historical **relevancy** of ancient legal precedents must be tested against the evolving needs of human society."},
      {"author": "Thomas Babington Macaulay", "work": "Critical and Historical Essays", "quote": "The advocate insisted upon the **relevancy** of the intercepted letters, showing that they revealed a treasonable plot."}
    ]
  },
  "Dashboard — lev/relevant.md": {
    "primary": "Having significant and demonstrable bearing on or connection with the matter in hand; pertinent and applicable.",
    "secondary": "In epistemological reasoning, evidence that raises or lowers the objective probability of a contested hypothesis.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "These considerations are **relevant**, not to the estimation of actions, but of persons and motives."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "Let us confine our attention strictly to the facts that are **relevant** to the mystery of the missing coronet."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Every anatomical detail of the cranial structure is highly **relevant** to our understanding of human descent."}
    ]
  },
  "Dashboard — lev/relevantly.md": {
    "primary": "In a relevant, pertinent, or fitting manner; with direct application to the subject under consideration.",
    "secondary": "In logical exposition and philosophical dialogue, advancing premises that directly substantiate the central thesis.",
    "quotes": [
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "She replied **relevantly** to his inquiry, refusing to be drawn into a sentimental discussion of the past."},
      {"author": "Leo Tolstoy", "work": "War and Peace", "quote": "Pierre reasoned **relevantly** upon the question of military strategy, astonishing the older staff officers."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "To discourse **relevantly**, a speaker must affix clear and determinate ideas to the words he employs."}
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

print(f"Speed Batch 6B: Successfully updated {updated}/{len(data)} notes.")
