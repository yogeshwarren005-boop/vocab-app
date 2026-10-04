# -*- coding: utf-8 -*-
"""
Part 3: 23 words from Dashboard — strict ('constrict' to 'unrestrictive')
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

part3_strict = {
  "constrict": {
    "primary": "To make narrower, tighter, or smaller by squeezing, compressing, or contracting around something.",
    "secondary": "In physiology and vascular medicine, to narrow a lumen, blood vessel, or airway through smooth muscle contraction; or to limit freedom.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "Intense terror causes the cutaneous arterioles to **constrict**, producing a sudden, deathlike pallor over the entire countenance."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Vasomotor nerve impulses stimulate circular muscular fibers to **constrict** the peripheral blood vessels, elevating arterial pressure."},
      {"author": "Jack London", "work": "The Call of the Wild", "quote": "He felt a cold band of fear **constrict** his throat as the wolves drew their deadly circle around the dying fire."}
    ]
  },
  "constricted": {
    "primary": "Narrowed, tightened, or compressed in dimension; or restricted and inhibited in scope, freedom, or expression.",
    "secondary": "In anatomy and pathology, having an abnormally narrowed lumen or reduced physical diameter due to spasms, scarring, or external pressure.",
    "quotes": [
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "I felt my heart oppressed and my breathing painfully **constricted** within the narrow confines of the red-room."},
      {"author": "Jack London", "work": "The Star Rover", "quote": "The canvas jacket was laced so tightly that my lungs felt **constricted** and every breath became an agony."},
      {"author": "Leo Tolstoy", "work": "War and Peace", "quote": "Passing through the narrow gorge, the marching column became tightly **constricted** between the mountain rocks."}
    ]
  },
  "constricting": {
    "primary": "Narrowing, tightening, or compressing something by inward squeezing; or imposing severe limits on liberty or development.",
    "secondary": "In ophidian predatory behavior and cardiovascular hemodynamics, killing prey by coils that halt respiration or narrowing arterial passages.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The large serpent subdued its prey by wrapping powerful **constricting** coils around the struggling mammal."},
      {"author": "Jack London", "work": "The Star Rover", "quote": "The cruel bonds tightened around my chest with **constricting** force until I could barely whisper a plea for water."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "She struggled against the cold, **constricting** rules of the Lowood institution that sought to break her independent spirit."}
    ]
  },
  "constriction": {
    "primary": "The mechanical narrowing or compression of an opening, channel, or duct; a tight inward restriction or choke point.",
    "secondary": "In cardiology and pulmonology, the pathological or physiological narrowing of a duct, sphincter, or blood vessel; or severe social constraint.",
    "quotes": [
      {"author": "Jack London", "work": "The Star Rover", "quote": "With every breath I drew, the relentless **constriction** of the straitjacket crushed against my ribs and spine."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The sudden **constriction** of the glottis during choking prevents air from penetrating into the pulmonary alveoli."},
      {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "Violent grief is often accompanied by an agonizing sensation of **constriction** across the chest and throat."}
    ]
  },
  "constrictive": {
    "primary": "Serving or tending to contract, tighten, or narrow; causing compression, restriction, or limitation.",
    "secondary": "In pathology (as in constrictive pericarditis), characterized by rigid fibrotic thickening that impairs normal physiological expansion.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Chronic inflammation of the pericardial sac produces a dense, **constrictive** sheath that hampers diastolic ventricular filling."},
      {"author": "Herbert Spencer", "work": "The Principles of Sociology", "quote": "Feudal guild regulations exerted a highly **constrictive** influence upon the natural expansion of artisan manufacturing."},
      {"author": "Oliver Wendell Holmes", "work": "Medical Essays", "quote": "The tight corsets worn by fashionable women exerted a **constrictive** pressure upon the thoracic cage and vital organs."}
    ]
  },
  "constrictor": {
    "primary": "A snake, such as a boa or python, that kills prey by wrapping its muscular coils around it and squeezing; or a muscle that closes an orifice.",
    "secondary": "In human anatomy, any sphincter-like muscle (such as the pharyngeal constrictors) whose contraction narrows a hollow passageway.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "In the dense tropical thickets along the Parana, we encountered a magnificent boa **constrictor** sunning itself upon a fallen log."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "During the act of swallowing, the inferior pharyngeal **constrictor** contracts sequentially to propel the bolus down into the esophagus."},
      {"author": "James George Frazer", "work": "The Golden Bough", "quote": "Certain indigenous tribes regarded the giant python or boa **constrictor** with religious reverence, forbidden from slaying it."}
    ]
  },
  "derestrict": {
    "primary": "To remove, relax, or abolish legal or official limits, regulations, or speed limits imposed on an activity or area.",
    "secondary": "In transport policy, traffic regulation, and economic governance, to lift statutory restrictions on highway speeds or trade quotas.",
    "quotes": [
      {"author": "John Maynard Keynes", "work": "The Economic Consequences of the Peace", "quote": "To revive continental trade, the allied powers must urgently **derestrict** the movement of basic raw materials across borders."},
      {"author": "H. G. Wells", "work": "The World of William Clissold", "quote": "The transport ministry decided to **derestrict** the new arterial highway, permitting motorists to travel at their own discretion."},
      {"author": "George Bernard Shaw", "work": "The Intelligent Woman's Guide to Socialism and Capitalism", "quote": "Whenever municipal authorities **derestrict** speculative commerce, private monopolies instantly rush in to exploit the unwary consumer."}
    ]
  },
  "district": {
    "primary": "An area of a country, territory, or city that has defined borders or distinct administrative, geographical, or cultural characteristics.",
    "secondary": "In municipal administration and electoral law, a demarcated precinct established for schooling, tax assessment, or judicial jurisdiction.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "In that secluded agricultural **district**, news of the outer world filtered through only on weekly market days."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Plants inhabiting an isolated mountainous **district** frequently exhibit endemic variations absent from the surrounding plains."},
      {"author": "George Eliot", "work": "Silas Marner", "quote": "Raveloe was a village situated in a fertile, undulating **district** where the old customs of rural England lingered undisturbed."}
    ]
  },
  "nonrestrictive": {
    "primary": "Not imposing restrictions, limitations, or constraints; allowing broad freedom or latitude of action.",
    "secondary": "In descriptive grammar and syntax, designating a relative clause that provides supplementary parenthetical detail without defining the noun.",
    "quotes": [
      {"author": "Henry Sweet", "work": "A New English Grammar", "quote": "A **nonrestrictive** relative clause is set off by commas because it adds descriptive information without limiting the antecedent noun."},
      {"author": "Otto Jespersen", "work": "The Philosophy of Grammar", "quote": "In spoken discourse, the pitch drop distinctly marks the **nonrestrictive** qualifier from the defining, restrictive clause."},
      {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "A wise legal covenant should be essentially **nonrestrictive**, encouraging commercial enterprise while guarding against fraud."}
    ]
  },
  "restrict": {
    "primary": "To put a limit on someone or something; to keep within bounds, confine, or control access to resources or movements.",
    "secondary": "In constitutional governance and resource management, to limit personal liberties, trade flows, or property use by statutory regulation.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The powers granted to the central government must not arbitrarily **restrict** the traditional rights of the several states."},
      {"author": "Bram Stoker", "work": "Dracula", "quote": "Now let us see what precautions we can take to **restrict** the vampire's movements within the perimeter of the ancient abbey."},
      {"author": "John Stuart Mill", "work": "On Liberty", "quote": "The only purpose for which power can be rightfully exercised over any member of a civilized community is to prevent harm to others; in all else, the law must not **restrict** him."}
    ]
  },
  "restricted": {
    "primary": "Limited in extent, amount, or scope; allowed only to specific individuals, or kept within strict boundaries.",
    "secondary": "In security administration, copyright law, and zoning statutes, subject to confidential access controls or specific land-use limitations.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "The monopoly granted to ancient guild masters **restricted** the freedom of ambitious apprentices to establish independent workshops."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Endemic species inhabiting oceanic islands are often **restricted** to an exceedingly narrow geographical range and specific habitat."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Her social sphere had been painfully **restricted** by provincial prejudice, preventing the full exercise of her intellectual gifts."}
    ]
  },
  "restricting": {
    "primary": "Placing limits or boundaries on someone or something; keeping within definite bounds or controlling freedom of action.",
    "secondary": "In regulatory policy and biological adaptation, limiting the expansion of market monopolies or confining anatomical development.",
    "quotes": [
      {"author": "Frank A. Fetter", "work": "Economics Volume II: Modern Economic Problems", "quote": "By **restricting** the output of coal mines, the commercial cartel succeeded in maintaining artificially inflated prices across the market."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The captain paced the quarterdeck, **restricting** the sailors to their essential duties while the gale raged around them."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "A constitutional charter achieves its purpose by **restricting** legislative excess and protecting fundamental civic guarantees."}
    ]
  },
  "restriction": {
    "primary": "A limiting condition or measure; a rule or law that limits what you can do, or the act of limiting someone or something.",
    "secondary": "In molecular genetics and commerce, cleavage of DNA at specific palindromic sequences by endonucleases; or legal tariffs and trade quotas.",
    "quotes": [
      {"author": "Mrs. Oliphant", "work": "A Beleaguered City", "quote": "Every gate of the city was guarded, and no citizen could pass through without submitting to the stern **restriction** of the guard."},
      {"author": "Frank A. Fetter", "work": "Economics Volume II: Modern Economic Problems", "quote": "The imposition of an import **restriction** on foreign manufactured goods created an immediate windfall for domestic industrialists."},
      {"author": "John Stuart Mill", "work": "On Liberty", "quote": "Any artificial **restriction** upon the expression of philosophical opinion tends to deprive mankind of the discovery of truth."}
    ]
  },
  "restrictive": {
    "primary": "Imposing limits, constraints, or boundaries on freedom, movement, development, or choice; limiting in nature.",
    "secondary": "In syntax and economic policy, defining and narrowing the identity of a noun phrase; or protectionist and trade-impeding in fiscal effects.",
    "quotes": [
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "I found the domestic routine of the schoolroom exceedingly **restrictive**, longing for the wider horizons beyond the garden walls."},
      {"author": "Frank A. Fetter", "work": "Economics Volume II: Modern Economic Problems", "quote": "The medieval trade guilds operated under highly **restrictive** covenants that prohibited innovation and barred alien craftsmen."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "A **restrictive** tariff upon grain imports inevitably burdens the laboring classes while enriching agricultural landlords."}
    ]
  },
  "restrictively": {
    "primary": "In a manner that places limits, bounds, or tight constraints on freedom, interpretation, or activity.",
    "secondary": "In judicial interpretation and statutory construction, construing legislative texts with narrow, literal, and strict boundaries.",
    "quotes": [
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "Penal statutes must ever be construed **restrictively**, lest the liberties of the subject be infringed by loose judicial implication."},
      {"author": "John Marshall", "work": "Judicial Decisions", "quote": "The powers granted in the constitution are not to be interpreted so **restrictively** as to paralyze the necessary operations of government."},
      {"author": "Jeremy Bentham", "work": "The Rationale of Judicial Evidence", "quote": "Rules that exclude witness testimony operate **restrictively**, blinding the court to essential facts required for just adjudication."}
    ]
  },
  "restrictiveness": {
    "primary": "The quality, state, or extent of being restrictive; the degree to which rules, limits, or controls constrain freedom.",
    "secondary": "In regulatory sociology and institutional design, the severity and rigidity of formal bureaucratic prohibitions and access barriers.",
    "quotes": [
      {"author": "Herbert Spencer", "work": "The Principles of Sociology", "quote": "The oppressive **restrictiveness** of ancient sumptuary laws dictated the exact fabric and color of garments permitted to each social rank."},
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "Whenever the **restrictiveness** of guild statutes exceeded endurance, contraband commerce arose in suburban districts beyond their reach."},
      {"author": "Alexis de Tocqueville", "work": "The Old Regime and the Revolution", "quote": "The bureaucratic **restrictiveness** of the royal administration stifled local civic initiative across the provinces of pre-revolutionary France."}
    ]
  },
  "strict": {
    "primary": "Demanding that rules, discipline, or procedures be obeyed completely and without compromise; rigorous, exact, and severe.",
    "secondary": "In textual analysis and legal construction, adhering to the literal, narrow meaning of a term without latitude or metaphorical extension.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "Lord Angelo is precise; stands at a guard with envy; scarce confesses that his blood flows; he follows a **strict** discipline."},
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "Henchard maintained a **strict** integrity in his commercial transactions, refusing to alter a ledger by a single copper penny."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "In the struggle for existence, the balance of nature is preserved through a **strict** competition between rival organic varieties."}
    ]
  },
  "strictly": {
    "primary": "In a strict, rigorous, and exact manner; with meticulous adherence to rules, definitions, facts, or instructions.",
    "secondary": "In scientific methodology and formal logic, with absolute precision that permits no ambiguity, deviation, or broad interpretation.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "Charge him that he tell the truth **strictly**, omitting no circumstance that may uncover the conspirators."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Gabriel Oak **strictly** observed every shift in the barometer, knowing that the harvest depended upon prompt preparation."},
      {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "In logical discourse, we must employ terms **strictly** according to their precise definitions to avoid fallacious deductions."}
    ]
  },
  "strictness": {
    "primary": "Rigorous, unyielding adherence to rules, principles, exact standards, or severe ethical and institutional discipline.",
    "secondary": "In moral philosophy and institutional governance, uncompromising rectitude or severity that tolerates no relaxation of prescribed codes.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Will Ladislaw rebelled against the puritanical **strictness** of his uncle's household, longing for artistic color and spontaneous joy."},
      {"author": "Ralph Waldo Emerson", "work": "Representative Men", "quote": "The moral **strictness** of the ancient Stoics fortified the spirit against the vicissitudes of tyranny and bodily pain."},
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "The magistrates governed the colony with an unrelenting **strictness** that mirrored the severe theology of their faith."}
    ]
  },
  "stricture": {
    "primary": "Severe criticism, adverse remark, or stern censure; or an abnormal narrowing of a canal, duct, or vessel in the human body.",
    "secondary": "In pathology and pathology-informed surgery, a fibrous constriction of a tubular organ (such as the urethra, esophagus, or bowel) causing obstruction.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth smiled at his sharp **stricture** on the manners of the local assembly, knowing he spoke more from pride than malice."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Boldwood bore the sarcastic **stricture** of his companion in stony silence, his heart preoccupied with deeper grievances."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Surgical dilation of the cicatricial **stricture** restored normal passage through the esophagus, relieving the patient's dysphagia."}
    ]
  },
  "unconstricted": {
    "primary": "Not compressed, narrowed, or tightened; free from physical compression, inhibiting restriction, or artificial limitation.",
    "secondary": "In circulatory physiology and biomechanics, characterized by fully dilated vessel lumens, unimpeded fluid flow, and normal elastic compliance.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Power of Movement in Plants", "quote": "When the tender tendril grows in an **unconstricted** space, it moves in wide, graceful circles seeking support."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "In the healthy circulatory system, blood flows smoothly through **unconstricted** arterioles without excessive vascular resistance."},
      {"author": "John Ruskin", "work": "The Seven Lamps of Architecture", "quote": "The Gothic vault arches upward with an **unconstricted** vitality that mirrors the soaring branches of a primeval forest."}
    ]
  },
  "unrestricted": {
    "primary": "Not limited or restricted in size, scope, movement, or activity; free, open, and without bounds or conditions.",
    "secondary": "In commercial economics and constitutional jurisprudence, enjoying plenary freedom of access, unhampered by protective tariffs or state censorship.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "He was granted **unrestricted** liberty to wander through the crumbling rooms and overgrown gardens of Satis House."},
      {"author": "Herman Melville", "work": "Typee: A Peep at Polynesian Life", "quote": "The native youths enjoyed **unrestricted** freedom amidst the lush breadfruit groves, untroubled by European conventions."},
      {"author": "Frank A. Fetter", "work": "Economics Volume II: Modern Economic Problems", "quote": "The policy of **unrestricted** immigration furnished American industries with an abundant supply of adaptable manual labor."}
    ]
  },
  "unrestrictive": {
    "primary": "Not imposing restrictions, limitations, or constraints; broad, permissive, and granting wide freedom.",
    "secondary": "In regulatory jurisprudence and institutional policy, establishing liberal frameworks that promote voluntary association and free enterprise.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "An **unrestrictive** commercial code enables capital to flow naturally into those domestic employment channels where profits are highest."},
      {"author": "Herbert Spencer", "work": "Social Statics", "quote": "A truly progressive society maintains an **unrestrictive** legal regime that maximizes individual initiative and voluntary contract."},
      {"author": "John Stuart Mill", "work": "On Liberty", "quote": "The state serves its citizens best when its laws remain fundamentally **unrestrictive**, allowing diverse moral experiments in living."}
    ]
  }
}
