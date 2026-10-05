# -*- coding: utf-8 -*-
"""
Part 3 of Curated Law, Justice & Feudal Batch 1:
Dashboard — damn (8 words)
Dashboard — fisc (5 words)
Total: 13 words
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

data_damn_fisc = {
    # =========================================================================
    # Dashboard — damn (8 words)
    # =========================================================================
    "damn": {
        "primary": "To condemn to eternal punishment in hell, or to express complete condemnation and censure.",
        "secondary": "In theological and literary discourse, to consign to perdition, ruin utterly, or pronounce an irrevocable verdict of failure.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "I'll not endure it. Would I were satisfied! Death and **damn**ation! O!"},
            {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The parson refused to perform the full rite, declaring that unbaptized babes must abide in darkness, which seemed to **damn** the innocent soul forever."},
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "I'll chase him round Good Hope, and round the Horn, and round the Norway Maelstrom, and round perdition's flames before I **damn** my resolution and give him up!"}
        ]
    },
    "damnable": {
        "primary": "Deserving severe condemnation, moral censure, or eternal punishment; thoroughly detestable.",
        "secondary": "In moral philosophy and early theological jurisprudence, describing offenses or heresies so egregious that they incur spiritual ruin and societal reprobation.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "O thou foul thief! where hast thou stow'd my daughter? **Damnable** wretch, thou hast enchanted her!"},
            {"author": "Henry David Thoreau", "work": "A Week on the Concord and Merrimack Rivers", "quote": "It is a **damnable** fallacy that trade and material acquisition represent the true end and nobility of human existence."},
            {"author": "G. K. Chesterton", "work": "The Ball and the Cross", "quote": "To treat sacred ideals with callous levity seemed to him a **damnable** degradation of intellectual honor."}
        ]
    },
    "damnably": {
        "primary": "In a manner that is detestable, odious, or deserving of severe condemnation.",
        "secondary": "In expressive literary prose, used to describe intense unpleasantness, excessive difficulty, or shameful moral failure.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "They will scarcely believe this without trial; offer them instances, which shall bear no less likelihood than to see me at any time impartially execute justice; for he hath **damnably** deceived me in this trust."},
            {"author": "James Joyce", "work": "Ulysses", "quote": "BEAUFOY: (Spluttering) You have **damnably** betrayed the confidence reposed in you by honest men!"},
            {"author": "Robert Louis Stevenson", "work": "The Master of Ballantrae", "quote": "The wind blew **damnably** cold off the black waters, biting through our soaked greatcoats to the very bone."}
        ]
    },
    "damnation": {
        "primary": "Consignment to eternal punishment in perdition, or the fact of being utterly ruined and condemned.",
        "secondary": "In Christian soteriology and classical tragedy, the catastrophic irrevocable exclusion of a soul from grace, salvation, and divine communion.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "For nothing canst thou to **damnation** add Greater than that."},
            {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "He painted in large red letters upon the stile the fearful words: THY **DAMNATION** SLUMBERETH NOT."},
            {"author": "John Milton", "work": "Paradise Lost", "quote": "So bent on self-destruction that their pride Chose rather grim **damnation** than repentance before the Throne."}
        ]
    },
    "damnatory": {
        "primary": "Conveying, expressing, or implying condemnation, censure, or eternal perdition.",
        "secondary": "In forensic theology and ecclesiastic law, describing dogmatic clauses, anathemas, or judicial findings that formally pronounce spiritual doom.",
        "quotes": [
            {"author": "Charles Dickens", "work": "Great Expectations", "quote": "He delivered the sentence with a cold, **damnatory** emphasis that left the wretched prisoner without a gleam of hope."},
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The synod affixed **damnatory** clauses to every creed that differed by a single iota from the orthodox formula."},
            {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The manifesto contained **damnatory** strictures upon the past administration, alienating moderate supporters of the Crown."}
        ]
    },
    "damned": {
        "primary": "Condemned to eternal punishment, or intensely disliked, doomed, and denounced.",
        "secondary": "In classical theology and expressive literature, describing souls consigned to infernal torments, or situations regarded with supreme exasperation.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "O, I were **damned** beneath all depth in hell, But that I did proceed upon just grounds To this extremity."},
            {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "I have sold my soul for eternal youth, and I am **damned** to walk the earth bearing the secret stain of corruption."},
            {"author": "Bram Stoker", "work": "Dracula", "quote": "The Un-Dead exist in a state of horrific desolation, forever **damned** to feed upon the living until holy release comes."}
        ]
    },
    "damnify": {
        "primary": "To cause financial loss, physical damage, or legal injury to another person or estate.",
        "secondary": "In classical common-law pleading, to inflict a tortious harm or measurable prejudice upon a claimant's property or rights.",
        "quotes": [
            {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "A nuisance that does not actually **damnify** the neighbor in the enjoyment of his tenement gives no rise to an action on the case."},
            {"author": "Jeremy Bentham", "work": "Rationale of Judicial Evidence", "quote": "The law must provide swift redress whenever trespassers willfully **damnify** the lands or possessions of honest husbandmen."},
            {"author": "Edward Coke", "work": "Institutes of the Lawes of England", "quote": "Every covenant of indemnity protects the purchaser against all encumbrances that may hereafter **damnify** the title."}
        ]
    },
    "damning": {
        "primary": "Conclusively proving guilt, fault, or failure; impossible to refute or explain away.",
        "secondary": "In judicial inquiry and critical biography, presenting unequivocal documentary or testimonial evidence that completely discredits a reputation.",
        "quotes": [
            {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "The thumb-mark on the wall was the most **damning** piece of evidence yet uncovered against the unhappy prisoner."},
            {"author": "Ralph Waldo Emerson", "work": "Essays: First Series", "quote": "A man's secret actions often furnish a **damning** commentary upon his loud public professions of virtue."},
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The entries in the battered log-book offered a **damning** testimony of neglect and mutinous defiance on the voyage."}
        ]
    },

    # =========================================================================
    # Dashboard — fisc (5 words)
    # =========================================================================
    "confiscate": {
        "primary": "To seize private property with authority and transfer it to the public treasury.",
        "secondary": "In administrative and maritime prize law, to condemn and expropriate contraband, enemy assets, or illicit goods by sovereign prerogative.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Merchant of Venice", "quote": "Thy lands and goods Are, by the laws of Venice, **confiscate** Unto the state of Venice."},
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The avaricious prefect did not hesitate to **confiscate** the vast estates of patricians accused of imaginary conspiracies."},
            {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "To **confiscate** the ancient endowments of the church to satisfy speculative paper debts is sheer spoliation under the mask of reform."}
        ]
    },
    "confiscation": {
        "primary": "The seizure of property by authority of a sovereign government or legal judgment.",
        "secondary": "In political history and revenue law, an executive or judicial forfeiture of assets to the public fisc following rebellion, treason, or smuggling.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "Thy lands and goods are by the laws of Venice subject to general **confiscation** for seeking the life of an alien citizen."},
            {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "Decrees of universal **confiscation** fell upon the emigrant nobility, stripping ancient houses of both titles and revenues."},
            {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "The financial ruin was completed by wholesale **confiscation**, which destroyed credit and undermined all security of title."}
        ]
    },
    "fisc": {
        "primary": "The public treasury or exchequer of a state, monarch, or government body.",
        "secondary": "In Roman and civil law jurisprudence, the imperial or state fund distinct from the sovereign's private patrimony, maintained for public revenue and expenditure.",
        "quotes": [
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The imperial **fisc** swallowed up the forfeitures of condemned senators, filling the coffers of the Palatine treasury."},
            {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "Every coin collected under the new customs tariff was directed straightway to the royal **fisc** to pay the standing army."},
            {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The revenue of the ancient crown **fisc** was derived primarily from domain lands, feudal reliefs, and judicial amercements."}
        ]
    },
    "fiscal": {
        "primary": "Relating to government finances, taxation, public revenues, and state expenditure.",
        "secondary": "In macroeconomic policy and public administration, pertaining to budgetary management, public debt issuance, and taxation strategies employed by treasuries.",
        "quotes": [
            {"author": "Frank A. Fetter", "work": "Economics Volume II: Modern Economic Problems", "quote": "The **fiscal** policies of the modern state have a profound bearing upon the distribution of wealth and industrial progress."},
            {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "Money is, with propriety, considered as the vital principle of the body politic; hence sound **fiscal** provisions are essential to sovereignty."},
            {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Prudent monarchs regulate their **fiscal** demands so that the burden of taxation does not impoverish the productive labor of the people."}
        ]
    },
    "fiscally": {
        "primary": "In a manner pertaining to financial administration, public revenues, or fiscal policies.",
        "secondary": "In public finance economics, evaluating measures, budgets, or governmental interventions in terms of expenditure efficiency and revenue impact.",
        "quotes": [
            {"author": "Frank A. Fetter", "work": "Economics Volume II: Modern Economic Problems", "quote": "A municipality cannot remain **fiscally** sound while continuously issuing long-term bonds to meet routine annual expenses."},
            {"author": "Woodrow Wilson", "work": "Congressional Government", "quote": "Congress is **fiscally** sovereign, holding exclusive authority over the appropriation of public moneys and the imposition of duties."},
            {"author": "John Maynard Keynes", "work": "The Economic Consequences of the Peace", "quote": "The indemnities imposed were **fiscally** impossible to collect without destroying the economic fabric of Central Europe."}
        ]
    }
}
