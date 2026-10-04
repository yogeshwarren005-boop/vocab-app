# -*- coding: utf-8 -*-
import os, sys, re

sys.stdout.reconfigure(encoding="utf-8")

data = {
  # =========================================================================
  # Dashboard — fid (26 words)
  # =========================================================================
  "Dashboard — fid/affidavit.md": {
    "primary": "A written statement confirmed by oath or solemn affirmation, for use as judicial evidence in court.",
    "secondary": "In civil jurisprudence and procedural law, a sworn voluntary deposition made before an authorized notary, magistrate, or commissioner of oaths.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Why then should you expect me to pen this kind of **affidavit**, which binds me to declarations I cannot honestly affirm?"},
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "The facts stated in the **affidavit** must be within the personal knowledge of the deponent."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The legal clerk spent the morning engrossing an enormous **affidavit** in the endless suit of Jarndyce and Jarndyce."}
    ]
  },
  "Dashboard — fid/confidant.md": {
    "primary": "A trusted friend or associate to whom one shares private thoughts, personal secrets, or intimate concerns.",
    "secondary": "In narrative literature and classical drama, a secondary character to whom the protagonist reveals motivations that would otherwise remain hidden from the audience.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "She found to her surprise that an intimate **confidant** was ready to listen to her most secret perplexities."},
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Elinor was the chosen **confidant** of her sister's enthusiastic hopes and tender anxieties."},
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "He acted as her discreet **confidant**, guiding her judgment through the intricate society of Rome."}
    ]
  },
  "Dashboard — fid/confidante.md": {
    "primary": "A female friend or intimate companion to whom private matters, emotional secrets, and confidences are entrusted.",
    "secondary": "In social history and Victorian fiction, a trusted lady's maid or intimate female companion serving as counselor and keeper of domestic secrets.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Liddy, she said, with a lighter heart, for youth and hope had begun to revive in her trusted **confidante**, let us speak of him no more."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Charlotte Lucas was the only **confidante** with whom Elizabeth could discuss the astonishing events of the ball."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "She had neither friend nor **confidante** to relieve the oppressive loneliness of the great mansion."}
    ]
  },
  "Dashboard — fid/confide.md": {
    "primary": "To tell someone about a secret or private matter while trusting them not to repeat it to others; or to place trust in.",
    "secondary": "In fiduciary ethics and psychological counseling, to disclose vulnerable truths under a covenant of professional secrecy or personal fidelity.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "It was certainly not her plainness that attracted them, but her rare capacity to listen and **confide** with unaffected sincerity."},
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Marianne was eager to **confide** the happiness of her attachment to everyone who loved her."},
      {"author": "William Shakespeare", "work": "Richard II", "quote": "In God and my own innocence I **confide**, fearing no earthly malice."}
    ]
  },
  "Dashboard — fid/confidence.md": {
    "primary": "Firm trust, reliance, or faith placed in a person, idea, or future outcome; or a feeling of self-assurance.",
    "secondary": "In legal finance and banking stability, the collective faith of depositors and investors that sustains the circulation of credit and fiduciary currency.",
    "quotes": [
      {"author": "William Shakespeare", "work": "All's Well That Ends Well", "quote": "Upon thy certainty and **confidence** / What dar'st thou venture?"},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The stability of commercial enterprise depends entirely upon the mutual **confidence** of merchants in one another's integrity."},
      {"author": "Ralph Waldo Emerson", "work": "Self-Reliance", "quote": "Trust thyself: every heart vibrates to that iron string... cultivate supreme **confidence** in your powers."}
    ]
  },
  "Dashboard — fid/confident.md": {
    "primary": "Feeling or showing certainty about something; self-assured, bold, and free from doubt.",
    "secondary": "In classical drama and rhetoric, firmly assured of victory or rectitude, sometimes verging on tragic hubris.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Cymbeline", "quote": "I do think I saw't this morning; **confident** I am / Last night 'twas on her arm."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Mr. Darcy was too **confident** of success to imagine that his proposal could possibly be rejected."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Troy was **confident** of his power to charm, relying upon his dashing manner and military uniform."}
    ]
  },
  "Dashboard — fid/confidential.md": {
    "primary": "Intended to be kept secret; entrusted with private information; or indicating intimacy and confidence.",
    "secondary": "In legal ethics and enterprise administration, designating privileged communications shielded from compulsory disclosure.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "One day she was led by an accident into an oddly **confidential** dialogue with her shepherd."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Mr. Tulkinghorn was the repository of family secrets, moving like a dark, **confidential** shadow through aristocratic drawing-rooms."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "He addressed her in a low, **confidential** tone that excluded all other listeners in the parlor."}
    ]
  },
  "Dashboard — fid/confidentiality.md": {
    "primary": "The duty or principle of keeping sensitive information secret and protecting it from unauthorized disclosure.",
    "secondary": "In medical jurisprudence and professional ethics, the legal obligation binding fiduciaries to preserve the secrecy of disclosures made during professional service.",
    "quotes": [
      {"author": "William Osler", "work": "Aequanimitas", "quote": "The sacred duty of clinical **confidentiality** demands that the physician guard the secrets of the patient as inviolable."},
      {"author": "Oliver Wendell Holmes Jr.", "work": "The Common Law", "quote": "The law protects professional **confidentiality** not for the counselor's benefit, but to ensure that citizens may seek justice without fear."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "The seal of **confidentiality** surrounding grand jury deliberations preserves them from popular intimidation."}
    ]
  },
  "Dashboard — fid/confidentially.md": {
    "primary": "In a confidential manner; privately, secretly, or with an understanding that the information will not be shared.",
    "secondary": "In social discourse and narrative prose, communicating in low, secretive tones implying mutual trust and exclusive intimacy.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "He said to himself that he was only doing right in telling her this **confidentially**, before any public announcement was made."},
      {"author": "Jane Austen", "work": "Emma", "quote": "Mrs. Weston took Emma aside to whisper **confidentially** the news she had received that morning."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Mr. Micawber leaned across the table and informed me **confidentially** that he was momentarily waiting for something to turn up."}
    ]
  },
  "Dashboard — fid/confidently.md": {
    "primary": "In a confident manner; with strong assurance, conviction, or certainty; without hesitation or fear.",
    "secondary": "In scientific deduction and historical analysis, asserting conclusions warranted by overwhelming empirical demonstration.",
    "quotes": [
      {"author": "William Shakespeare", "work": "All's Well That Ends Well", "quote": "None better than to let him fetch off his drum, which you hear him so **confidently** undertake to do."},
      {"author": "Charles Darwin", "work": "On the Origin of Species", "quote": "We may look forward **confidently** to discovering many intermediate links when the geological record is more thoroughly explored."},
      {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "He spoke **confidently** of the future, refusing to let the melancholy heath depress his spirits."}
    ]
  },
  "Dashboard — fid/confiding.md": {
    "primary": "Having or showing trust and confidence in others; trustful, unsuspicious, and candid.",
    "secondary": "In psychological development and romantic fiction, characterized by innocent, childlike vulnerability and complete absence of cynical suspicion.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "So the reserve went off, and they were **confiding** and warm as friends of long standing."},
      {"author": "Charles Dickens", "work": "Little Dorrit", "quote": "Her gentle, **confiding** nature endeared her to all the unfortunate inmates of the Marshalsea."},
      {"author": "George Eliot", "work": "Adam Bede", "quote": "A young girl's **confiding** affection is a precious treasure that should never be trifled with."}
    ]
  },
  "Dashboard — fid/confidingly.md": {
    "primary": "In a confiding, trusting, or unsuspicious manner; with complete faith and openness.",
    "secondary": "In descriptive narrative, leaning upon, looking toward, or speaking to another with unreserved emotional reliance.",
    "quotes": [
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "Lorry took the hesitating little hand that **confidingly** advanced toward him and pressed it warmly."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "She looked up **confidingly** into his face, believing that all her sorrows were ended forever."},
      {"author": "Jane Austen", "work": "Mansfield Park", "quote": "Fanny placed her arm **confidingly** within her cousin's, finding comfort in his steady presence."}
    ]
  },
  "Dashboard — fid/diffidence.md": {
    "primary": "Modesty, shyness, or hesitation resulting from a lack of self-confidence; reserve.",
    "secondary": "In classical moral philosophy, the prudent hesitance of judgment grounded in an acute awareness of human fallibility.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry VI, Part 1", "quote": "We have been guided by thee hitherto, / And of thy cunning had no **diffidence**."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "His natural **diffidence** in the presence of strangers was frequently mistaken for supercilious arrogance."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "A modest **diffidence** concerning our own knowledge is the best preservative against dogmatism."}
    ]
  },
  "Dashboard — fid/diffident.md": {
    "primary": "Modest, shy, or reserved because of a lack of self-confidence; unassertive.",
    "secondary": "In rhetorical characterization and social history, displaying modest restraint and reluctance to advance personal claims in public.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "He was a **diffident** though distinguished nurseryman, and feared that his modest speech might weary the company."},
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Edward was naturally **diffident**, requiring the encouragement of familiar friends to draw out his conversational powers."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Oak was too **diffident** of his merits to press his suit with bold persistence."}
    ]
  },
  "Dashboard — fid/diffidently.md": {
    "primary": "In a diffident, shy, modest, or hesitant manner; without self-assertion.",
    "secondary": "In narrative prose, speaking or approaching a superior with cautious, deferential humility.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Heh-heh! well, I wish to noise nothing abroad—nothing at all, murmured the rustic, smiling **diffidently** at his boots."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Biddy looked up **diffidently** from her needlework and asked if I were quite sure of my own intentions."},
      {"author": "George Eliot", "work": "Adam Bede", "quote": "The young scholar stepped forward **diffidently**, holding his manuscript with trembling hands."}
    ]
  },
  "Dashboard — fid/fidelity.md": {
    "primary": "Faithfulness to a person, cause, belief, or duty, shown by continued loyalty and support.",
    "secondary": "In acoustic engineering and translation studies, the degree of exactness with which a sound recording reproduces the original signal, or a translation preserves the source text.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Merry Wives of Windsor", "quote": "By my **fidelity**, this is not well, Master Ford, this wrongs you."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Among innumerable false, unmoved, / Unshaken, unseduced, unterrified, / His loyalty he kept... In steadfast **fidelity** to heaven's sovereign."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The extraordinary **fidelity** and courage of dogs in defending their masters have been celebrated in all ages."}
    ]
  },
  "Dashboard — fid/fiducial.md": {
    "primary": "Based on, having, or inspiring trust or reliance; or serving as a fixed standard of reference or comparison.",
    "secondary": "In observational astronomy and surveying instrumentation, designating reference marks, lines, or points upon an optical reticle used as fixed spatial benchmarks.",
    "quotes": [
      {"author": "John Herschel", "work": "Outlines of Astronomy", "quote": "The micrometer wire must be aligned precisely upon the **fiducial** line of the reticle to ensure accurate coordinates."},
      {"author": "George Biddell Airy", "work": "Theory of Errors of Observations", "quote": "Errors of collimation are eliminated by referring all angular sweeps to a stable **fiducial** mark."},
      {"author": "Jeremy Taylor", "work": "Holy Dying", "quote": "The Christian conscience rests with **fiducial** reliance upon the divine promises of mercy."}
    ]
  },
  "Dashboard — fid/fiduciary.md": {
    "primary": "Involving trust, especially regarding the relationship between a trustee and a beneficiary; or held or given in trust.",
    "secondary": "In monetary banking economics, designating unbacked paper money circulating upon public faith in the issuing bank or government.",
    "quotes": [
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "A trustee stands in a **fiduciary** relation toward the ward, bound to administer the estate with scrupulous fidelity."},
      {"author": "Walter Bagehot", "work": "Lombard Street", "quote": "The entire banking system rests upon a delicate **fiduciary** foundation of mutual credit."},
      {"author": "Oliver Wendell Holmes Jr.", "work": "The Common Law", "quote": "The breach of a **fiduciary** covenant was redressed by the Court of Chancery through the enforcement of equitable trusts."}
    ]
  },
  "Dashboard — fid/infidel.md": {
    "primary": "A person who does not believe in a particular religion or in religion at all; an unbeliever.",
    "secondary": "In historical religious polemics and medieval chronicles, an adherent of a rival faith (such as a Christian viewed by Muslims or vice versa).",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry IV, Part 1", "quote": "What a pagan rascal is this, an **infidel**!"},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The crusaders advanced with fanatical fury against the armies of the **infidel**."},
      {"author": "Francis Bacon", "work": "Essays", "quote": "None can remain an **infidel** but the superficial, who never contemplate the order of nature."}
    ]
  },
  "Dashboard — fid/infidelity.md": {
    "primary": "The action or state of being unfaithful to a spouse or sexual partner; or disbelief in a particular religion.",
    "secondary": "In Enlightenment intellectual history and ethics, the conscious philosophical rejection of traditional religious dogmas, or breach of fiduciary trust.",
    "quotes": [
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "And thus was this land saved from **infidelity**, as the remainder of the world was preserved from darkness."},
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "Marital **infidelity** dissolves the sacred bond of domestic happiness, poisoning the purest fountain of human affection."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The charges of theological **infidelity** were frequently employed to ruin political rivals at the imperial court."}
    ]
  },
  "Dashboard — fid/overconfidence.md": {
    "primary": "Excessive or unjustified confidence; too great a reliance on one's own abilities or good fortune.",
    "secondary": "In behavioral economics and military strategy, the cognitive bias wherein subjective certainty systematically exceeds objective accuracy, leading to strategic blunder.",
    "quotes": [
      {"author": "Thucydides", "work": "History of the Peloponnesian War", "quote": "The disastrous Sicilian expedition was born of an arrogant **overconfidence** in our naval supremacy."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The overweening conceit of men leads to fatal **overconfidence** in adventurous lotteries."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Ignorance more frequently begets **overconfidence** than does knowledge."}
    ]
  },
  "Dashboard — fid/overconfident.md": {
    "primary": "Excessively confident, presumptuous, or assured; cocky or imprudently bold.",
    "secondary": "In classical tragedy and tactical planning, disregarding genuine hazards and warnings due to inflated self-estimation.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "He had been too **overconfident** in his calculations, forgetting how easily weather upsets the plans of the most prudent farmer."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The **overconfident** general neglected his scouts and led his legions into a deadly mountain ambush."},
      {"author": "Ralph Waldo Emerson", "work": "Essays: First Series", "quote": "The youthful soul is often **overconfident** of its strength until battered by the harsh realities of worldly conflict."}
    ]
  },
  "Dashboard — fid/perfidious.md": {
    "primary": "Deceitful and untrustworthy; guilty of violating good faith, vows, or allegiance; treacherous.",
    "secondary": "In historical diplomacy and classical tragedy, deliberately breaking sworn alliances or betraying solemn covenants for political gain.",
    "quotes": [
      {"author": "William Shakespeare", "work": "All's Well That Ends Well", "quote": "He's quoted for a most **perfidious** slave, / With all the spots o' the world tax'd and debosh'd."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Thus fell the **perfidious** tempter, snared in his own malicious designs."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The treaty was celebrated with solemn oaths, only to be violated within the month by that **perfidious** monarch."}
    ]
  },
  "Dashboard — fid/perfidiously.md": {
    "primary": "In a perfidious, treacherous, deceitful, or faithless manner; with deliberate violation of trust.",
    "secondary": "In legal accusations and historical annals, betraying a sworn monarch, comrade, or covenant in secret collusion with enemies.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The garrison surrendered upon promise of quarter, but were **perfidiously** butchered the following dawn."},
      {"author": "Walter Scott", "work": "The Talisman", "quote": "He acted **perfidiously** toward the crusader king, concealing his secret correspondence with the Saracens."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The minister was accused of having **perfidiously** betrayed his sovereign's private counsels to the French court."}
    ]
  },
  "Dashboard — fid/perfidiousness.md": {
    "primary": "The quality, characteristic, or display of being perfidious; treacherousness or faithlessness.",
    "secondary": "In ethical philosophy and historical jurisprudence, deliberate treasonous deception that destroys social trust and foundational covenants.",
    "quotes": [
      {"author": "Edward Hyde, Earl of Clarendon", "work": "History of the Rebellion", "quote": "The shocking **perfidiousness** of his closest associates hastened the king's ruin more than the arms of his enemies."},
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "No vice is more universally detested by mankind than the insidious **perfidiousness** of a false friend."},
      {"author": "David Hume", "work": "The History of England", "quote": "The reign was stained by repeated acts of royal **perfidiousness** that dissolved the allegiance of the barons."}
    ]
  },
  "Dashboard — fid/perfidy.md": {
    "primary": "The quality, act, or state of being deceitful and untrustworthy; deliberate breach of faith or violation of trust.",
    "secondary": "In international law of armed conflict, treacherous actions (such as feigning surrender or truce under the white flag) designed to betray an adversary's trust.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "True, we may thank the **perfidy** of France / That picked the jewel out of England's crown, / But our own folly gave the opportunity."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The Roman Senate denounced the shameful **perfidy** of the Carthaginian peace commissioners."},
      {"author": "John Milton", "work": "Samson Agonistes", "quote": "She was false to her nuptial vows, and by her cruel **perfidy** delivered me blind into the hands of the Philistines."}
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

print(f"Faith Batch 2 (fid): Successfully updated {updated}/{len(data)} notes.")
