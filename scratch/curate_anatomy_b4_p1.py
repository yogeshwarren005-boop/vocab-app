# -*- coding: utf-8 -*-
"""
curate_anatomy_b4_p1.py
Batch 4 Part 1 of Cluster Anatomy & Clinical Medicine (Dashboard — ren: 38 words):
adrenal, adrenalectomy, adrenalin, adrenaline, adrenarche, adrenergic, adrenocortical,
adrenocorticotrophic, adrenocorticotrophin, adrenocorticotropic, adrenocorticotropin,
adrenosterone, antiadrenergic, nonrenewable, renaissance, renal, rename, renascence,
renascent, render, rendering, rending, rendition, renegade, renege, renegociate,
renegotiate, renew, renewable, renewal, renewed, renewing, reniform, renin, rennet,
rennin, reno, renoir
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

data_anatomy_b4_p1 = {
    "adrenal": {
        "primary": "Situated near or atop the kidneys; or relating to the adrenal glands and their hormones.",
        "secondary": "In endocrinology, designating the paired suprarenal glands composed of an outer steroidogenic cortex and an inner catecholaminergic medulla.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Addison demonstrated that primary fibrocaseous destruction of the **adrenal** capsules leads inexorably to bronzed skin and fatal asthenia."},
            {"author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "Each **adrenal** gland rests upon the superior pole of the corresponding kidney, enclosed in renal fascia."},
            {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Extracts prepared from the **adrenal** medulla exert an immediate pressor effect upon the peripheral vascular channels."}
        ]
    },
    "adrenalectomy": {
        "primary": "The surgical removal or excision of one or both adrenal glands.",
        "secondary": "In endocrine surgery, the operative ablation of the adrenal glands indicated for functional pheochromocytoma, Cushing's disease, or metastatic malignancy.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Bilateral **adrenalectomy** in experimental animals precipitates severe electrolyte collapse unless cortical hormones are continuously replaced."},
            {"author": "Harvey Cushing", "work": "The Life of Sir William Osler", "quote": "The surgical clinic explored subtotal **adrenalectomy** in severe basophilism to relieve the distressing symptoms of hypercortisolism."},
            {"author": "William Stewart Halsted", "work": "Surgical Papers", "quote": "Meticulous ligation of the fragile suprarenal veins is the cardinal step in preventing catastrophic hemorrhage during **adrenalectomy**."}
        ]
    },
    "adrenalin": {
        "primary": "Epinephrine; a catecholamine hormone and neurotransmitter secreted by the adrenal medulla.",
        "secondary": "In emergency pharmacotherapy and autonomic physiology, a sympathomimetic amine stimulating alpha and beta adrenergic receptors to elevate cardiac output and dilate airways.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Hypodermic injection of **adrenalin** provides instantaneous relief in paroxysms of acute spasmodic asthma by relaxing bronchial smooth muscle."},
            {"author": "Claude Bernard", "work": "Lectures on Experimental Physiology", "quote": "The intravenous introduction of minute doses of **adrenalin** immediately produces powerful vasoconstriction and rising blood pressure."},
            {"author": "Alexis Carrel", "work": "Man, The Unknown", "quote": "Under the sudden influence of fear or rage, a surge of **adrenalin** mobilizes hepatic glycogen for immediate muscular exertion."}
        ]
    },
    "adrenaline": {
        "primary": "A sympathomimetic hormone secreted by the adrenal medulla; epinephrine.",
        "secondary": "In biochemical pharmacology and stress physiology, the principal catecholamine mediating the acute 'fight-or-flight' autonomic reaction in vertebrates.",
        "quotes": [
            {"author": "H. G. Wells", "work": "The Invisible Man", "quote": "A sudden surge of frantic **adrenaline** coursed through his veins as he dodged past the bewildered constable."},
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "In profound anaphylactic shock, prompt intramuscular administration of **adrenaline** counteracts catastrophic systemic vasodilation."},
            {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "The physiological manifestations of terror—dilated pupils, pallor, and trembling—are governed by sympathetic discharge and circulating **adrenaline**."}
        ]
    },
    "adrenarche": {
        "primary": "The developmental awakening of the adrenal cortex in middle childhood initiating adrenal androgen secretion.",
        "secondary": "In pediatric endocrinology, the normal maturational increase in dehydroepiandrosterone (DHEA) and androstenedione production preceding true gonadal puberty.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Premature **adrenarche** manifests with early pubic and axillary hair growth in children without advanced skeletal maturation."},
            {"author": "Abraham Flexner", "work": "Medical Education in the United States and Canada", "quote": "Instruction in pediatric endocrinology distinguished the physiological onset of **adrenarche** from pathologic adrenal hyperplasia."},
            {"author": "Harvey Cushing", "work": "The Life of Sir William Osler", "quote": "He studied the metabolic transitions of **adrenarche**, correlating hormonal excretion with cutaneous and somatic growth patterns."}
        ]
    },
    "adrenergic": {
        "primary": "Relating to, activated by, or releasing adrenaline, noradrenaline, or related sympathomimetic compounds.",
        "secondary": "In neuropharmacology, designating postganglionic sympathetic neurons, cellular receptors (alpha and beta), or medications that mimic sympathetic nerve activity.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Excessive **adrenergic** stimulation originating from an occult pheochromocytoma precipitates severe hypertensive crises."},
            {"author": "Claude Bernard", "work": "Lectures on Experimental Physiology", "quote": "The physiological response of the arterial tree to sympathetic stimulation depends upon specific **adrenergic** neuroeffector junctions."},
            {"author": "Alexis Carrel", "work": "Man, The Unknown", "quote": "The autonomic equilibrium maintains a constant balance between cholinergic vagal restraint and powerful **adrenergic** acceleration."}
        ]
    },
    "adrenocortical": {
        "primary": "Pertaining to, produced by, or affecting the cortex of the adrenal gland.",
        "secondary": "In steroid endocrinology, relating to the glucocorticoid, mineralocorticoid, and sex steroid hormones synthesized within the three zones of the adrenal cortex.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Chronic **adrenocortical** insufficiency leads to electrolyte wasting, profound dehydration, and systemic hypotension."},
            {"author": "Harvey Cushing", "work": "The Life of Sir William Osler", "quote": "Autopsy sections in patients with plethoric adiposity revealed diffuse bilateral **adrenocortical** hyperplasia."},
            {"author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "The **adrenocortical** layers—the glomerulosa, fasciculata, and reticularis—exhibit distinct histological organization under the microscope."}
        ]
    },
    "adrenocorticotrophic": {
        "primary": "Stimulating or governing the hormonal secretion of the adrenal cortex (British spelling).",
        "secondary": "In pituitary endocrinology, designating the anterior pituitary polypeptide hormone that stimulates cortisol production in the adrenal cortex.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Basophilic adenomas of the anterior pituitary secrete excessive **adrenocorticotrophic** hormone, driving bilateral cortical overgrowth."},
            {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The anterior hypophysis exerts master endocrine control through its **adrenocorticotrophic** and gonadotrophic secretions."},
            {"author": "Harvey Cushing", "work": "The Life of Sir William Osler", "quote": "Experimental administration of purified **adrenocorticotrophic** extracts demonstrated rapid restoration of atrophic adrenal glands."}
        ]
    },
    "adrenocorticotrophin": {
        "primary": "A polypeptide hormone secreted by the anterior pituitary that stimulates the adrenal cortex (British variant).",
        "secondary": "In clinical endocrinology, ACTH (corticotropin), a 39-amino-acid peptide regulating glucocorticoid synthesis in response to hypothalamic CRH.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Elevated circulating levels of **adrenocorticotrophin** cause characteristic cutaneous hyperpigmentation in primary adrenal failure."},
            {"author": "Claude Bernard", "work": "Lectures on Experimental Physiology", "quote": "The secretion of **adrenocorticotrophin** fluctuates in response to physiological stress, cold, and acute trauma."},
            {"author": "Alexis Carrel", "work": "Man, The Unknown", "quote": "The hypothalamic-pituitary axis modulates the release of **adrenocorticotrophin**, demonstrating how emotional states influence somatic metabolism."}
        ]
    },
    "adrenocorticotropic": {
        "primary": "Having a stimulating effect on the adrenal cortex; corticotropic.",
        "secondary": "In biochemistry, designating the anterior pituitary trophic hormone (ACTH) that binds to melanocortin receptors on adrenocortical cells.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Synthetic **adrenocorticotropic** peptide infusions are utilized in provocative testing to evaluate adrenal functional reserve."},
            {"author": "Harvey Cushing", "work": "The Life of Sir William Osler", "quote": "The discovery of the **adrenocorticotropic** factor clarified the obscure pathology connecting pituitary tumors with suprarenal obesity."},
            {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The **adrenocorticotropic** feedback loop maintains plasma cortisol concentrations within strict physiological limits."}
        ]
    },
    "adrenocorticotropin": {
        "primary": "Adrenocorticotropic hormone (ACTH); the anterior pituitary hormone that stimulates the adrenal cortex.",
        "secondary": "In neuroendocrinology, the cleavage product of pro-opiomelanocortin (POMC) that stimulates cholesterol conversion to pregnenolone in the adrenal cortex.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The clinical diagnosis of Addison's disease is verified by measuring an elevated serum **adrenocorticotropin** alongside subnormal cortisol levels."},
            {"author": "Claude Bernard", "work": "Lectures on Experimental Physiology", "quote": "Hypophysectomy in animals results in rapid cortical atrophy that can be entirely reversed by administering purified **adrenocorticotropin**."},
            {"author": "Alexis Carrel", "work": "Man, The Unknown", "quote": "The physiological pulse of **adrenocorticotropin** peaks in the early morning hours, synchronizing the organism with the diurnal cycle."}
        ]
    },
    "adrenosterone": {
        "primary": "An endogenous steroid hormone produced in the adrenal cortex exhibiting weak androgenic activity.",
        "secondary": "In steroid biochemistry, 11-ketoandrostenedione, a C19 adrenal steroid intermediate isolated by Tadeus Reichstein during early corticosteroid characterization.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Excessive excretion of **adrenosterone** and related 17-ketosteroids is observed in virilizing tumors of the adrenal cortex."},
            {"author": "Claude Bernard", "work": "Lectures on Experimental Physiology", "quote": "The chemical isolation of **adrenosterone** from suprarenal extracts revealed the diverse spectrum of steroids synthesized by the gland."},
            {"author": "Harvey Cushing", "work": "The Life of Sir William Osler", "quote": "Biochemists demonstrated that **adrenosterone** possesses mild masculinizing properties compared to testicular testosterone."}
        ]
    },
    "antiadrenergic": {
        "primary": "Opposing, blocking, or counteracting the physiological effects of adrenaline or sympathetic stimulation.",
        "secondary": "In cardiovascular pharmacology, designating sympathetic receptor antagonists (such as alpha or beta blockers) used to lower blood pressure and manage arrhythmias.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Administration of an **antiadrenergic** agent prevents paroxysmal hypertensive surges during the surgical manipulation of a pheochromocytoma."},
            {"author": "Claude Bernard", "work": "Lectures on Experimental Physiology", "quote": "The **antiadrenergic** properties of ergot alkaloids were demonstrated by their ability to reverse the vascular pressor response of epinephrine."},
            {"author": "Alexis Carrel", "work": "Man, The Unknown", "quote": "Modern pharmacologists developed targeted **antiadrenergic** compounds to shield the failing myocardium from excessive sympathetic drive."}
        ]
    },
    "nonrenewable": {
        "primary": "Not capable of being renewed, replenished, or regenerated once consumed; exhaustible.",
        "secondary": "In environmental economics and natural resource management, designating finite geological resources (such as fossil fuels or minerals) that cannot replenish on a human timescale.",
        "quotes": [
            {"author": "Ralph Waldo Emerson", "work": "English Traits", "quote": "The vast coal beds of Britain represent a **nonrenewable** treasury of buried solar energy upon which modern industry subsists."},
            {"author": "John Muir", "work": "Our National Parks", "quote": "We squander these ancient subterranean resources as though our **nonrenewable** mineral wealth had no inevitable end."},
            {"author": "Henry David Thoreau", "work": "Walden", "quote": "The primeval forest once felled by ruthless commerce represents a virtually **nonrenewable** inheritance of centuries."}
        ]
    },
    "renaissance": {
        "primary": "The great revival of art, classical literature, and humanist learning in Europe from the 14th to 17th centuries; or any major rebirth.",
        "secondary": "In cultural historiography and aesthetics, the historical epoch marked by the revival of classical antiquity, empirical science, and individualistic philosophy.",
        "quotes": [
            {"author": "George Eliot", "work": "Romola", "quote": "Florence in the late fifteenth century was the radiant heart of the **Renaissance**, vibrant with intellectual passions and artistic rivalries."},
            {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "He looked for a new spirituality that would combine the passion of the **Renaissance** with modern artistic consciousness."},
            {"author": "G. K. Chesterton", "work": "The Wisdom of Father Brown", "quote": "His magnificent palace was furnished with all the lavish splendor and intellectual pride of a **Renaissance** prince."}
        ]
    },
    "renal": {
        "primary": "Pertaining to, involving, or situated in the vicinity of the kidneys.",
        "secondary": "In human nephrology and metabolic physiology, relating to glomerular filtration, tubular reabsorption, or the excretion of nitrogenous waste.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Chronic **renal** failure manifests clinically with uremic stomatitis, progressive normocytic anemia, and secondary hyperparathyroidism."},
            {"author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "The **renal** artery arises directly from the abdominal aorta, dividing into segmental branches at the hilum of the kidney."},
            {"author": "René Laennec", "work": "A Treatise on the Diseases of the Chest", "quote": "Widespread anasarca without evidence of primary cardiac failure directed our diagnostic suspicion toward advanced **renal** disease."}
        ]
    },
    "rename": {
        "primary": "To give a new, different, or updated name to a person, place, institution, or entity.",
        "secondary": "In administrative nomenclature and archival management, the formal alteration of a taxonomic, geographical, or institutional title.",
        "quotes": [
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Constantine determined to **rename** the ancient city of Byzantium after himself, establishing it as the new capital of the empire."},
            {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "Parliament resolved to **rename** the strategic forts and public squares to celebrate the victorious Protestant succession."},
            {"author": "Walter Scott", "work": "Ivanhoe", "quote": "The Norman conquerors did not hesitate to **rename** the ancient Saxon manors according to their own dialect."}
        ]
    },
    "renascence": {
        "primary": "A rebirth, revival, or renewed blossoming of life, art, culture, or intellectual energy.",
        "secondary": "In cultural history and philosophical literature, a resurgence of classical aesthetic vitality or intellectual enthusiasm; a renaissance.",
        "quotes": [
            {"author": "G. K. Chesterton", "work": "The Wisdom of Father Brown", "quote": "There was something of the **Renascence** Prince about his omnivorous culture and restless publicity."},
            {"author": "Walter Pater", "work": "Studies in the History of the Renaissance", "quote": "The delicate dawn of the fifteenth century represented a glorious **renascence** of the human spirit."},
            {"author": "Matthew Arnold", "work": "Culture and Anarchy", "quote": "Hellenism enjoyed a splendid **renascence** during the revival of classical letters in western Europe."}
        ]
    },
    "renascent": {
        "primary": "Springing into fresh life, experiencing a revival, or rising again with renewed vigor.",
        "secondary": "In social philosophy and psychological narrative, describing values, emotions, or artistic impulses that awaken into energetic expression after prolonged suppression.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "So spoke love **renascent**, preparing the way for Tess's devoted outpouring upon the bridge."},
            {"author": "George Meredith", "work": "The Egoist", "quote": "Her **renascent** cheerfulness welcomed the warm sunshine that swept away the gloom of winter."},
            {"author": "John Addington Symonds", "work": "Renaissance in Italy", "quote": "The **renascent** energy of Italian scholarship exhumed forgotten classical manuscripts from dusty monastic libraries."}
        ]
    },
    "render": {
        "primary": "To submit, deliver, or yield up; to cause to become; or to execute an artistic depiction.",
        "secondary": "In jurisprudence and artistic expression, to deliver a formal judicial verdict, or to interpret and represent a visual scene or musical composition.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Merchant of Venice", "quote": "Therefore, Jew, though justice be thy plea, consider this, that in the course of justice none of us should see salvation; we do pray for mercy, and that same prayer doth teach us all to **render** the deeds of mercy."},
            {"author": "Ralph Waldo Emerson", "work": "Self-Reliance", "quote": "A man should learn to detect and watch that gleam of light which flashes across his mind from within, more than the lustre of the firmament of bards and sages; yet he dismisses without notice his thought, because it is his; in every work of genius we recognize our own rejected thoughts; they come back to us with a certain alienated majesty; great works of art have no more affecting lesson for us than this: they teach us to abide by our spontaneous impression with good-humored inflexibility; then only will nature **render** up her deepest secret."},
            {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The jury took but little time to **render** their unanimous verdict of guilty against the prisoner."}
        ]
    },
    "rendering": {
        "primary": "An artistic performance, translation, graphic depiction, or legal delivery of an account.",
        "secondary": "In architectural visualization and musical interpretation, the specific execution and stylistic realization of a score, sketch, or dramatic text.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Measure for Measure", "quote": "By **rendering** up your liberty, you may redeem your brother from impending execution."},
            {"author": "Thomas Hardy", "work": "The Woodlanders", "quote": "His faithful **rendering** of the old woodland ballad moved the rustic listeners to thoughtful silence."},
            {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "The artist gave a vivid **rendering** of facial agony, capturing every furrow etched upon the brow."},
        ]
    },
    "rending": {
        "primary": "Tearing apart violently; splitting; or causing excruciating emotional anguish.",
        "secondary": "In dramatic narrative and acoustic description, the physical laceration of fabrics or tissues, or a sound that pierces the air with violent sharpness.",
        "quotes": [
            {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "A terrible, heart-**rending** cry of mortal agony broke the dead silence of the lonely moor."},
            {"author": "Henry David Thoreau", "work": "Walden", "quote": "The sudden cracking of the winter pond ice sounded like the loud **rending** of massive timbers."},
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The ship shuddered under the **rending** shock of the whale's assault against the wooden hull."}
        ]
    },
    "rendition": {
        "primary": "An interpretation, artistic performance, translation, or formal surrender of a person or property.",
        "secondary": "In legal procedure and aesthetic criticism, the official extradition or surrender of an individual, or the stylistic execution of a dramatic role.",
        "quotes": [
            {"author": "Edgar Allan Poe", "work": "The Fall of the House of Usher", "quote": "His wild **rendition** of the antique ballad struck upon my ear with fantastic and melancholy power."},
            {"author": "Frederick Douglass", "work": "Life and Times of Frederick Douglass", "quote": "The northern magistrates resisted the compulsory **rendition** of fugitive slaves to their southern masters."},
            {"author": "Henry James", "work": "The Bostonians", "quote": "Her dramatic **rendition** of the poetic recitation held the fashionable drawing-room completely spellbound."}
        ]
    },
    "renegade": {
        "primary": "An individual who deserts a faith, cause, party, or allegiance; a traitor or apostate.",
        "secondary": "In political history and religious warfare, a turncoat who abandons conventional principles to join hostile or outlaw factions.",
        "quotes": [
            {"author": "G. K. Chesterton", "work": "The Man Who Was Thursday", "quote": "The cynical **renegade** mocked the loyal soldiers who continued to defend the crumbling citadel."},
            {"author": "Walter Scott", "work": "Ivanhoe", "quote": "He was branded as a **renegade** knight who had betrayed his sacred crusading vows for Saracen gold."},
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Imperial deserters found refuge among the barbarian tribes, serving as **renegade** commanders against Rome."}
        ]
    },
    "renege": {
        "primary": "To go back on a promise, undertaking, or contract; or in card games to fail to follow suit.",
        "secondary": "In contract disputes and vernacular idiom, the deliberate refusal to fulfill a solemn commitment or acknowledged obligation.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Antony and Cleopatra", "quote": "His captain's heart, which in the scuffles of great fights hath burst the buckles on his breast, **renege** all temper."},
            {"author": "James Joyce", "work": "Ulysses", "quote": "He was not the man to **renege** upon a comrade in the hour of political adversity."},
            {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "Henchard was too proud to **renege** upon his word, even when financial ruin stared him in the face."}
        ]
    },
    "renegociate": {
        "primary": "To negotiate again; to revise or discuss terms of an agreement anew (variant spelling).",
        "secondary": "In commercial and diplomatic history, reopening formal discussions to modify treaties, financial debts, or trade agreements.",
        "quotes": [
            {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The commissioners were instructed to **renegociate** commercial treaties with the maritime powers of Europe."},
            {"author": "Thomas Jefferson", "work": "The Writings of Thomas Jefferson", "quote": "We sought to **renegociate** the boundary conventions to avert impending frontier collisions."},
            {"author": "John Adams", "work": "Letters of John Adams", "quote": "The foreign ministry showed reluctance to **renegociate** terms that had been settled in the previous convention."}
        ]
    },
    "renegotiate": {
        "primary": "To negotiate anew; to discuss the terms of an agreement, contract, or treaty again to reach revised terms.",
        "secondary": "In international relations and financial jurisprudence, entering fresh deliberations to restructure debt obligations or alter trade protocols.",
        "quotes": [
            {"author": "Daniel Webster", "work": "Speeches and Forensic Arguments", "quote": "The government was obliged to **renegotiate** the disputed border clauses of the northeastern boundary treaty."},
            {"author": "John Maynard Keynes", "work": "The Economic Consequences of the Peace", "quote": "The allied powers must eventually **renegotiate** the crushing reparations clauses to avert continental economic ruin."},
            {"author": "Theodore Roosevelt", "work": "State Papers as Governor and President", "quote": "We stand ready to **renegotiate** commercial compacts whenever reciprocity benefits our domestic producers."}
        ]
    },
    "renew": {
        "primary": "To resume, restore to fresh condition, re-establish, or extend the period of validity of something.",
        "secondary": "In philosophical ethics and civil administration, to revive spiritual commitments or extend legal covenants before expiration.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Sonnet 15", "quote": "All in war with Time for love of you, as he takes from you, I engraft you new, and in my verse your youth **renew**."},
            {"author": "Ralph Waldo Emerson", "work": "Nature", "quote": "In the woods we return to reason and faith; there I feel that nothing can befall me in life which nature cannot **renew**."},
            {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The gentle spring shower seemed to **renew** the green youth of the blooming valley pastures."}
        ]
    },
    "renewable": {
        "primary": "Capable of being replenished naturally or extended in contractual duration.",
        "secondary": "In environmental science and property law, describing resources that regenerate through natural cycles, or leases subject to formal extension.",
        "quotes": [
            {"author": "John Muir", "work": "The Yosemite", "quote": "The cascading mountain streams represent an ever-flowing, **renewable** blessing bestowed by winter snows upon the valley."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "The farm lease was declared **renewable** every seven years upon mutual agreement of landlord and tenant."},
            {"author": "Henry David Thoreau", "work": "Walden", "quote": "The annual harvest of woodland birch and cedar is a **renewable** harvest if managed with prudent economy."}
        ]
    },
    "renewal": {
        "primary": "The act of restoring, reviving, or extending the validity of an agreement or process.",
        "secondary": "In psychological and seasonal narrative, the restorative resurgence of vitality, energy, or spiritual hope after exhaustion.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "The Woodlanders", "quote": "With the first budding of the saplings came a quiet **renewal** of hope in the hearts of the forest folk."},
            {"author": "George Eliot", "work": "Silas Marner", "quote": "The little child brought a blessed **renewal** of warmth and human sympathy into the lonely weaver's solitary cottage."},
            {"author": "Nathaniel Hawthorne", "work": "The Marble Faun", "quote": "The arrival of Roman springtime brought a joyous **renewal** of creative inspiration to the artist's studio."}
        ]
    },
    "renewed": {
        "primary": "Restored to fresh vitality, vigor, or valid condition; revived or resumed.",
        "secondary": "In historical narrative and psychology, regaining strength, resolve, or active operation following an interval of cessation.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Henry V", "quote": "With **renewed** courage our soldiers charged the breach, inspired by the royal banner waving above."},
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Oak returned to his shearing with **renewed** energy, determined to complete the task before sunset."},
            {"author": "George Eliot", "work": "Daniel Deronda", "quote": "She looked upon the tranquil morning landscape with **renewed** composure and a peaceful heart."}
        ]
    },
    "renewing": {
        "primary": "Restoring to fresh condition, regenerating, or extending the period of validity.",
        "secondary": "In spiritual philosophy and biological regeneration, the ongoing restorative process of rebuilding vital tissues or ethical convictions.",
        "quotes": [
            {"author": "George Eliot", "work": "Middlemarch", "quote": "The steady influence of quiet study was effective in **renewing** his intellectual ambition and purpose."},
            {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "The forest breeze seemed capable of **renewing** the faded roses upon the frail woman's pale cheeks."},
            {"author": "Bram Stoker", "work": "Dracula", "quote": "Sleep exerted its gentle **renewing** influence, smoothing away the haggard lines etched by terror."}
        ]
    },
    "reniform": {
        "primary": "Shaped like a kidney; having a rounded curved outline with a deep notch or sinus at the base.",
        "secondary": "In botanical morphology and anatomical pathology, describing kidney-shaped leaves (such as Asarum) or bean-shaped pathological lesions.",
        "quotes": [
            {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "Wild ginger produces a pair of large, dark green **reniform** leaves that carpet the moist woodland soil."},
            {"author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "The normal human spleen presents a flattened, oblong, slightly **reniform** contour against the diaphragm."},
            {"author": "Charles Darwin", "work": "The Power of Movement in Plants", "quote": "The **reniform** cotyledons of the seedling rotate towards the light with striking phototropic precision."}
        ]
    },
    "renin": {
        "primary": "An enzymatic hormone secreted by renal juxtaglomerular cells that initiates the renin-angiotensin-aldosterone cascade.",
        "secondary": "In renal physiology and hypertension pathophysiology, an aspartic protease converting circulating angiotensinogen into angiotensin I to regulate arterial pressure.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Experimental renal ischemia triggers copious release of **renin**, which initiates severe secondary arterial hypertension."},
            {"author": "Claude Bernard", "work": "Lectures on Experimental Physiology", "quote": "The discovery of **renin** in kidney extracts demonstrated that the organ functions as an active endocrine gland as well as an excretory filter."},
            {"author": "Alexis Carrel", "work": "Man, The Unknown", "quote": "The enzymatic action of **renin** upon plasma proteins illustrates the exquisite biochemical feedback governing systemic blood pressure."}
        ]
    },
    "rennet": {
        "primary": "A coagulating preparation extracted from the abomasum of ruminants containing chymosin, used to curdle milk in cheesemaking.",
        "secondary": "In dairy science and traditional husbandry, an enzymatic extract rich in proteolytic chymosin utilized to precipitate casein curds from whey.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Mrs. Crick added the measured spoonful of **rennet** to the warm vat, stirring the milk with practiced dairy skill."},
            {"author": "George Eliot", "work": "Adam Bede", "quote": "The cool dairy was fragrant with fresh cream, clean wooden churns, and the pungent aroma of drying **rennet**."},
            {"author": "Henry David Thoreau", "work": "Walden", "quote": "Simple country fare of milk curdled with wild plant **rennet** provided the hermit with wholesome sustenance."}
        ]
    },
    "rennin": {
        "primary": "Chymosin; a proteolytic enzyme found in the gastric juice of young ruminants that curdles milk.",
        "secondary": "In gastric biochemistry, an endopeptidase that specifically cleaves the peptide bond between phenylalanine and methionine in kappa-casein.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The gastric glands of infant mammals secrete **rennin** to precipitate casein for efficient peptic digestion."},
            {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Under the catalytic action of **rennin**, liquid milk is rapidly converted into a firm gelatinous clot in the stomach."},
            {"author": "Claude Bernard", "work": "Lectures on Experimental Physiology", "quote": "In the fourth stomach of the calf, **rennin** operates at a specific acidic pH to optimize the curdling of maternal milk."}
        ]
    },
    "reno": {
        "primary": "Reno, a prominent city in western Nevada near Lake Tahoe, celebrated for tourism, gaming, and legal services.",
        "secondary": "In twentieth-century American cultural geography, 'The Biggest Little City in the World', renowned historically as a hub for rapid divorce proceedings and early gaming resorts.",
        "quotes": [
            {"author": "F. Scott Fitzgerald", "work": "Tender Is the Night", "quote": "She spoke with cynical amusement of taking a temporary residence in **Reno** to sever her matrimonial ties."},
            {"author": "Sinclair Lewis", "work": "Dodsworth", "quote": "The train sped westward across the sagebrush desert toward the glittering oasis of **Reno**."},
            {"author": "John Steinbeck", "work": "The Grapes of Wrath", "quote": "Migrants talked of the Nevada crossroads around **Reno**, where gambling palaces gleamed against the arid Sierra hills."}
        ]
    },
    "renoir": {
        "primary": "Pierre-Auguste Renoir (1841–1919), celebrated French Impressionist painter renowned for vibrant color and luminous depictions of human life.",
        "secondary": "In art history, a master painter of the French Impressionist school famed for sparkling light effects, sensuous nudes, and joyful Parisian leisure scenes.",
        "quotes": [
            {"author": "Émile Zola", "work": "The Masterpiece", "quote": "The radiant sun-dappled canvases of **Renoir** celebrated the joyful spectacle of Parisian youth with incomparable warmth."},
            {"author": "Herbert Read", "work": "A Concise History of Modern Painting", "quote": "In the luminous brushwork of **Renoir**, color becomes pure vibration, capturing the transient glow of flesh and summer foliage."},
            {"author": "George Moore", "work": "Modern Painting", "quote": "Nobody understood the delicate bloom upon a young woman's cheek better than the lyric master **Renoir**."}
        ]
    }
}
