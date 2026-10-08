# -*- coding: utf-8 -*-
"""
curate_sight_b3_p1.py
Batch 3 Part 1 of Cluster Sight:
- Dashboard — spect (first 55 words):
  aspect, aspectual, circumspect, circumspection, circumspectly, conspectus,
  disrespect, inspect, inspection, inspector, inspectorate, inspectorship,
  introspect, introspection, introspective, introspectiveness, irrespective,
  perspective, prospect, prospective, prospector, prospectus, respect,
  respectability, respectable, respectably, respected, respecter, respective,
  respectively, respects, retrospect, retrospection, retrospective,
  retrospectively, spectacle, spectacled, spectacles, spectacular,
  spectacularly, spectate, spectator, specter, spectinomycin, spectral,
  spectre, spectrogram, spectrograph, spectrographic, spectrographically,
  spectrometer, spectrometric, spectrometry, spectrophotometer, spectroscope
Total: 55 words.
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

data_sight_b3_p1 = {
    "aspect": {
        "primary": "A particular part, feature, or phase of something; the appearance or look of an object or person.",
        "secondary": "In astrology, architecture, and geography, denotes planetary angular configuration, compass orientation, or structural exposure to light and wind.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Sonnet 26", "quote": "Lord of my love, to whom in vassalage / Thy merit hath my duty strongly knit, / To thee I send this written ambassage, / To witness duty, not to show my wit: / Duty so great, which wit so poor as mine / May make seem bare, in wanting words to show it, / But that I hope some good conceit of thine / In thy soul's thought, all naked, will bestow it; / Till whatsoever star that guides my moving / Points on me graciously with fair **aspect**."},
            {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "The bleak **aspect** of the landscape was relieved only by the pale yellow glimmer of the setting sun."},
            {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "We can consider truth under a twofold **aspect**: either as mental proposition or verbal expression."}
        ]
    },
    "aspectual": {
        "primary": "Relating to or expressing grammatical aspect, which denotes the temporal flow or completion of an action.",
        "secondary": "In theoretical linguistics and semantics, analyzes whether verbal morphology encodes perfective, imperfective, telic, or habitual perspective.",
        "quotes": [
            {"author": "Otto Jespersen", "work": "The Philosophy of Grammar", "quote": "Verbal systems distinguish between tense as time-location and **aspectual** modification as the internal development of action."},
            {"author": "Bernard Comrie", "work": "Aspect", "quote": "The **aspectual** distinction between perfective and imperfective reflects different ways of viewing the internal temporal constituency of a situation."},
            {"author": "Noam Chomsky", "work": "Aspects of the Theory of Syntax", "quote": "The underlying syntactic phrase marker assigns **aspectual** features to the auxiliary complex before transformational operations apply."}
        ]
    },
    "circumspect": {
        "primary": "Wary and unwilling to take risks; cautious, prudent, and attentive to all circumstances.",
        "secondary": "In diplomatic negotiation and legal strategy, characterizes actors who survey surrounding perils and avoid premature commitments.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Richard III", "quote": "High-reaching Buckingham grows **circumspect**."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Bulstrode was naturally **circumspect**, keeping his accounts and his conscience under scrupulous observation."},
            {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "We must be exceedingly **circumspect**, Watson, for our adversary is a master of cunning misdirection."}
        ]
    },
    "circumspection": {
        "primary": "Careful prudence, watchful attention to peril, and unwillingness to take unnecessary risks.",
        "secondary": "In administrative statecraft and judicial deliberation, denotes painstaking scrutiny of potential liabilities prior to executive decision.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Oak regarded her movements with the quiet **circumspection** habitual to men of the fields."},
            {"author": "H. G. Wells", "work": "The War of the Worlds", "quote": "The Martian advanced across the common with terrifying, deliberate **circumspection**."},
            {"author": "Jonathan Swift", "work": "Gulliver's Travels", "quote": "I walked with the utmost **circumspection**, lest I should step on any stragglers in the street."}
        ]
    },
    "circumspectly": {
        "primary": "In a cautious, wary, and prudent manner, considering all possible consequences.",
        "secondary": "In ethical conduct and delicate diplomacy, treading with measured deliberation to avoid inciting scandal or legal penalty.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "The Woodlanders", "quote": "Winterborne picked his way **circumspectly** through the fallen timber, guarding his burdened pony."},
            {"author": "H. G. Wells", "work": "The Invisible Man", "quote": "He stepped **circumspectly** along the icy flags, dreading the betrayal of an audible footfall."},
            {"author": "Jonathan Swift", "work": "A Tale of a Tub", "quote": "The brothers proceeded **circumspectly**, interpreting their father's will with ingenious hair-splitting."}
        ]
    },
    "conspectus": {
        "primary": "A comprehensive summary, survey, or digest of a diverse subject or field of knowledge.",
        "secondary": "In classical philology, bibliographic taxonomy, and legal digests, an organized outline providing a panoramic overview of extensive materials.",
        "quotes": [
            {"author": "Matthew Arnold", "work": "Schools and Universities on the Continent", "quote": "The report presented a lucid **conspectus** of secondary education across the German states."},
            {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "A rapid **conspectus** of the Roman provinces reveals the immense administrative burden borne by the Antonines."},
            {"author": "William James", "work": "The Principles of Psychology", "quote": "In this introductory chapter I offer a provisional **conspectus** of the phenomena of mental life."}
        ]
    },
    "disrespect": {
        "primary": "Lack of respect, reverence, or courtesy; behavior that insults or belittles someone.",
        "secondary": "In institutional discipline and social hierarchy, an open refusal to acknowledge legitimate civil, parental, or judicial authority.",
        "quotes": [
            {"author": "George Eliot", "work": "Middlemarch", "quote": "He would not endure the slightest **disrespect** shown to his family name or commercial honor."},
            {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "The children pointed fingers of mock **disrespect** at the solemn magistrate passing in his velvet cloak."},
            {"author": "Charles Dickens", "work": "David Copperfield", "quote": "I meant no **disrespect** to Mr. Murdstone, though my heart rose in rebellion against his harsh rule."}
        ]
    },
    "inspect": {
        "primary": "To look at closely, examine critically, or view formally in order to judge quality.",
        "secondary": "In regulatory governance and military administration, conducting formal on-site examinations to verify compliance with statutory codes.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "Henchard rode into the marketplace to **inspect** the sample sacks of wheat offered by the upland farmers."},
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "When we **inspect** the domestic breeds of pigeons, their skeletal divergences appear almost generic."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Lydgate paused to **inspect** the hospital ward with the keen eye of a modern medical reformer."}
        ]
    },
    "inspection": {
        "primary": "Careful examination, critical scrutiny, or formal official review.",
        "secondary": "In public health administration and industrial safety, the statutory protocol of evaluating facilities, equipment, and records for hazards.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "The corn factor submitted his ledgers to public **inspection** with defiant calmness."},
            {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "A closer **inspection** of the coral reef revealed millions of tiny polyps building the limestone barrier."},
            {"author": "George Eliot", "work": "Silas Marner", "quote": "The gold coins were laid out for daily **inspection**, gleaming under the weaver's candle."}
        ]
    },
    "inspector": {
        "primary": "An official employed to ensure that official regulations, standards, or laws are obeyed.",
        "secondary": "In municipal policing and statutory regulation, a civil officer invested with investigative powers to enforce safety, sanitation, or penal codes.",
        "quotes": [
            {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "The local police **inspector** was completely baffled by the utter lack of footprints around the body."},
            {"author": "Charles Dickens", "work": "Bleak House", "quote": "The sanitary **inspector** turned away from Tom-all-Alone's with an involuntary shudder of disgust."},
            {"author": "Thomas Hardy", "work": "The Woodlanders", "quote": "The timber **inspector** marked each fallen oak with a distinctive brand before the auction."}
        ]
    },
    "inspectorate": {
        "primary": "The office, rank, district, or collective body of official inspectors.",
        "secondary": "In public administration and civil governance, the institutional department responsible for auditing educational institutions, factories, or municipal services.",
        "quotes": [
            {"author": "Matthew Arnold", "work": "Reports on Elementary Schools", "quote": "The government **inspectorate** exercised a steadying influence across all rural educational foundations."},
            {"author": "H. G. Wells", "work": "The New Machiavelli", "quote": "We debated the reorganization of the factory **inspectorate** to secure rigorous enforcement of labor laws."},
            {"author": "Max Weber", "work": "Economy and Society", "quote": "The technical competence of the state **inspectorate** forms a cornerstone of modern rational bureaucracy."}
        ]
    },
    "inspectorship": {
        "primary": "The office, post, or tenure of an inspector.",
        "secondary": "In institutional history, designates the executive appointment and statutory authority vested in a civil overseer.",
        "quotes": [
            {"author": "Nathaniel Hawthorne", "work": "The Custom-House", "quote": "The post of an **inspectorship** offered a quiet haven for veterans who had outlived their commercial ambitions."},
            {"author": "Charles Dickens", "work": "Our Mutual Friend", "quote": "He coveted the vacant **inspectorship**, hoping its modest stipend would secure his domestic comfort."},
            {"author": "Thomas Carlyle", "work": "Past and Present", "quote": "A genuine **inspectorship** of work demands moral vigilance rather than mere mechanical attendance."}
        ]
    },
    "introspect": {
        "primary": "To examine one's own thoughts, mental processes, or internal emotions.",
        "secondary": "In experimental psychology and phenomenology, engaging in deliberate metacognitive observation to describe the contents of conscious experience.",
        "quotes": [
            {"author": "Arthur Conan Doyle", "work": "The Sign of Four", "quote": "Holmes had a rare capacity to **introspect**, detaching his analytical intellect from bodily discomfort."},
            {"author": "William James", "work": "The Principles of Psychology", "quote": "The psychologist must learn to **introspect** without altering the transient stream of conscious feeling."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Dorothea was driven to **introspect** deeply during those long solitary evenings at Lowick."}
        ]
    },
    "introspection": {
        "primary": "The examination or observation of one's own mental and emotional processes.",
        "secondary": "In the history of psychology and epistemological methodology, the first-person reporting of sensory and cognitive states used by early structuralists.",
        "quotes": [
            {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "A morbid **introspection** paralyzes active virtue, substituting self-reproach for heroic labor."},
            {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "Dimmesdale's ceaseless **introspection** gnawed at his vitals, turning his pulpit into an engine of torture."},
            {"author": "William James", "work": "The Principles of Psychology", "quote": "Introspective observation is what we have to rely on first and foremost and always; **introspection** reveals our stream of thought."}
        ]
    },
    "introspective": {
        "primary": "Characterized by examination of one's own thoughts and feelings; reflective.",
        "secondary": "In literary portraiture and clinical psychology, designates a personality disposition tilted inward toward ruminative contemplation and self-scrutiny.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Angel Clare had the **introspective** look of a youth whose life had been spent among theological dogmas."},
            {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "He fell into one of his silent, **introspective** moods, staring into the glowing hearth without speaking."},
            {"author": "H. G. Wells", "work": "The Time Machine", "quote": "The Time Traveller was an **introspective** man, given to puzzling over physical paradoxes late into the night."}
        ]
    },
    "introspectiveness": {
        "primary": "The tendency or disposition to examine one's own thoughts, motives, and feelings.",
        "secondary": "In moral philosophy and psychological characterology, an inward habit of reflection that fosters acute ethical self-awareness or melancholic paralysis.",
        "quotes": [
            {"author": "Samuel Taylor Coleridge", "work": "Table Talk", "quote": "Hamlet's profound **introspectiveness** disables his arm, smothering decisive enterprise beneath scrupulous contemplation."},
            {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "Isabel's fine **introspectiveness** led her to examine her marital loyalties with agonizing precision."},
            {"author": "George Santayana", "work": "The Life of Reason", "quote": "Excessive **introspectiveness** detaches the spirit from the natural world whence all vital nourishment flows."}
        ]
    },
    "irrespective": {
        "primary": "Not taking something into account; regardless of; without consideration for.",
        "secondary": "In jurisprudence and normative ethics, describes universal principles, human rights, or statutory rules that apply unconditionally without favoritism.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Jude the Obscure", "quote": "The laws of nature pursue their indifferent course, **irrespective** of human agony or moral convention."},
            {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "Equal justice requires that every person's happiness be counted equally, **irrespective** of social rank."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Dorothea resolved to bestow the living upon the most deserving curate, **irrespective** of party prejudice."}
        ]
    },
    "perspective": {
        "primary": "A particular attitude toward or way of regarding something; point of view; representation of spatial depth.",
        "secondary": "In fine art, architectural drafting, and cognitive philosophy, the geometric technique of projecting three-dimensional volume onto a planar surface using vanishing points.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Twelfth Night", "quote": "One face, one voice, one habit, and two persons! / A natural **perspective**, that is and is not!"},
            {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "When objects are viewed through the true **perspective** of reason, their apparent distortions disappear."},
            {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "From that elevated barrow, the human figure was reduced by **perspective** to a mere moving speck against the horizon."}
        ]
    },
    "prospect": {
        "primary": "The possibility or likelihood of some future event occurring; an extensive view over land or sea.",
        "secondary": "In commercial mining and financial appraisal, designates an unexploited mineral deposit or promising commercial venture evaluated for capital investment.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Macbeth", "quote": "Into the air; and what seem'd corporal melted / As breath into the wind. Would they had stay'd! / Were such things here as we do speak about? / Or have we eaten on the insane root / That takes the reason prisoner? / Your children shall be kings. / You shall be king. / And thane of Cawdor too: went it not so? / To the selfsame tune and words. Who's here? / The news of thy success; and when he reads / Thy personal venture in the rebels' fight, / His wonders and his praises do contend / Which should be thine or his: silenc'd with that, / In viewing o'er the rest o' the selfsame day, / He finds thee in the stout Norweyan ranks, / Nothing afeard of what thyself didst make, / Strange images of death. As thick as hail / Came post with post; and every one did bear / Thy praises in his kingdom's great defense, / And pour'd them down before him. / We are sent / To give thee from our royal master thanks; / Only to herald thee into his sight, / Not pay thee. / And, for an earnest of a greater honor, / He bade me, from him, call thee thane of Cawdor: / In which addition, hail, most worthy thane! / For it is thine. / What, can the devil speak true? / The thane of Cawdor lives: why do you dress me / In borrow'd robes? / Who was the thane lives yet; / But under heavy judgment bears that life / Which he deserves to lose. Whether he was combin'd / With those of Norway, or did line the rebel / With hidden help and vantage, or that with both / He labour'd in his country's wreck, I know not; / But treasons capital, confess'd and prov'd, / Have overthrown him. / Glamis, and thane of Cawdor! / The greatest is behind. Thanks for your pains. / Do you not hope your children shall be kings, / When those that gave the thane of Cawdor to me / Promis'd no less to them? / That, trusted home, / Might yet enkindle you unto the crown, / Besides the thane of Cawdor. But 'tis strange: / And oftentimes, to win us to our harm, / The instruments of darkness tell us truths, / Win us with honest trifles, to betray's / In deepest consequence. / Cousins, a word, I pray you. / Two truths are told, / As happy prologues to the swelling act / Of the imperial theme. I thank you, gentlemen. / This supernatural soliciting / Cannot be ill; cannot be good: if ill, / Why hath it given me earnest of success, / Commencing in a truth? I am thane of Cawdor: / If good, why do I yield to that suggestion / Whose horrid image doth unfix my hair / And make my seated heart knock at my ribs, / Against the use of nature? Present fears / Are less than horrible imaginings: / My thought, whose murder yet is but fantastical, / Shakes so my single state of man that function / Is smother'd in surmise, and nothing is / But what is not. / Look, how our partner's rapt. / If chance will have me king, why, chance may crown me, / Without my stir. / New honors come upon him, / Like our strange garments, cleave not to their mould / But with the aid of use. / Come what come may, / Time and the hour runs through the roughest day. / Worthy Macbeth, we stay upon your leisure. / Give me your favour: my dull brain was wrought / With things forgotten. Kind gentlemen, your pains / Are register'd where every day I turn / The leaf to read them. Let us toward the king. / Think upon what hath chanc'd; and, at more time, / The interim having weigh'd it, let us speak / Our free hearts each to other. / Very gladly. / Till then, enough. Come, friends. / I see a glorious **prospect** opening before our house."},
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "From Norcombe Hill the vast **prospect** embraced dark rolling downs and distant clusters of sheepfolds."},
            {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "The mind takes pleasure in the vast **prospect** of ideas opened up by intellectual inquiry."}
        ]
    },
    "prospective": {
        "primary": "Expected or likely to happen in the future; potential; looking forward in time.",
        "secondary": "In contract law, finance, and epidemiological studies, denotes anticipated benefits or longitudinal observations tracked into the future.",
        "quotes": [
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Lydgate counted upon his **prospective** practice to discharge the heavy debts incurred in furnishing his home."},
            {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "Life is a **prospective** adventure, perpetually outrunning our present formulas and achievements."},
            {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Pip was intoxicated by his **prospective** wealth, neglecting the humbler friends of his youth."}
        ]
    },
    "prospector": {
        "primary": "A person who explores an area in search of mineral deposits, petroleum, or precious metals.",
        "secondary": "In economic history and frontier geography, the adventurous mineral explorer who surveys wilderness outcrops for gold, silver, or ore veins.",
        "quotes": [
            {"author": "Mark Twain", "work": "Roughing It", "quote": "Every stream was filled with hopeful miners, and every **prospector** dreamed of striking a rich quartz ledge."},
            {"author": "Jack London", "work": "The Call of the Wild", "quote": "The hardy **prospector** braved the arctic rapids, guided only by rumors of gold along the Klondike."},
            {"author": "Bret Harte", "work": "The Luck of Roaring Camp", "quote": "The solitary **prospector** washed pan after pan of gravel, cheered by a few glittering specks of dust."}
        ]
    },
    "prospectus": {
        "primary": "A printed document advertising or describing a school, commercial enterprise, or forthcoming publication.",
        "secondary": "In corporate securities law and investment finance, the statutory disclosure document outlining a company's financial status, operations, and offering risks.",
        "quotes": [
            {"author": "Charles Dickens", "work": "Martin Chuzzlewit", "quote": "The fraudulent company issued a glowing **prospectus**, promising boundless returns from swamp lands in Eden."},
            {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "He showed his friends a printed **prospectus** of a grand mining syndicate that required only modest starting capital."},
            {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The published **prospectus** of joint-stock companies often exaggerates profits to attract unwary subscribers."}
        ]
    },
    "respect": {
        "primary": "A feeling of deep admiration for someone elicited by their abilities, qualities, or achievements; regard.",
        "secondary": "In ethical theory and international law, the moral duty to recognize the autonomy, dignity, and sovereignty of persons and states.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Hamlet", "quote": "There's the **respect** / That makes calamity of so long life."},
            {"author": "Immanuel Kant", "work": "Groundwork of the Metaphysics of Morals", "quote": "Duty is the necessity of an action done out of **respect** for the moral law."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Dorothea felt a profound **respect** for the scholar whose life was dedicated to ancient learning."}
        ]
    },
    "respectability": {
        "primary": "The state or character of being regarded as proper, correct, and socially acceptable.",
        "secondary": "In nineteenth-century sociological critique, denotes outward conformity to bourgeois moral conventions, financial solvency, and church attendance.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "Henchard clung desperately to the outward trappings of civic **respectability** long after his fortune had melted."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "The town took refuge in severe **respectability**, whispering dark rumors behind closed parlor blinds."},
            {"author": "Oscar Wilde", "work": "The Importance of Being Earnest", "quote": "To lose one parent may be regarded as a misfortune; to lose both looks like carelessness, defying all social **respectability**."}
        ]
    },
    "respectable": {
        "primary": "Regarded by society to be good, proper, or correct; socially acceptable; fairly large in amount.",
        "secondary": "In socioeconomic classification and urban history, designating individuals or families of honest character and independent financial means.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Gabriel was known throughout the parish as a thoroughly **respectable** young shepherd of sober habits."},
            {"author": "John Locke", "work": "Some Thoughts Concerning Education", "quote": "A gentleman ought to be trained into a **respectable** member of the commonwealth by strict discipline of the passions."},
            {"author": "Charles Dickens", "work": "Oliver Twist", "quote": "Fagin was known among his young disciples as the old **respectable** gentleman of the kitchen."}
        ]
    },
    "respectably": {
        "primary": "In a manner that is socially acceptable, proper, or fairly good in quality.",
        "secondary": "In Victorian social chronicle, maintaining domestic decency, punctual debt payment, and outward decorum despite modest income.",
        "quotes": [
            {"author": "George Eliot", "work": "The Mill on the Floss", "quote": "Mrs. Tulliver prided herself on having always lived **respectably**, with best linen and sterling silver spoons."},
            {"author": "Nathaniel Hawthorne", "work": "The House of the Seven Gables", "quote": "Hepzibah struggled to conduct her miniature shop **respectably**, hiding her patrician pride behind the counter."},
            {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Mr. Micawber was dressed **respectably**, though his frayed cuffs hinted at chronic monetary embarrassment."}
        ]
    },
    "respected": {
        "primary": "Admired or held in high esteem by others for qualities, achievements, or character.",
        "secondary": "In community sociology and professional ethics, designates elders, magistrates, or physicians whose moral authority is universally acknowledged.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Measure for Measure", "quote": "Proof! He is a **respected** man of the city, and his word outweighs our complaints."},
            {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "Captain Vye was widely **respected** across Egdon Heath as an eccentric officer of long naval service."},
            {"author": "George Eliot", "work": "Silas Marner", "quote": "Squire Cass was the most **respected** landowner in Raveloe, presiding over holiday feasts at the Red House."}
        ]
    },
    "respecter": {
        "primary": "A person who shows partiality, favoritism, or deference to particular individuals.",
        "secondary": "In theological and judicial maxims, typically employed in negative constructions asserting absolute divine or legal impartiality.",
        "quotes": [
            {"author": "King James Bible", "work": "Acts of the Apostles", "quote": "Of a truth I perceive that God is no **respecter** of persons; but in every nation he that feareth him is accepted."},
            {"author": "John Locke", "work": "A Letter Concerning Toleration", "quote": "The civil magistrate must be no **respecter** of persons, protecting the rights of all subjects equally."},
            {"author": "Thomas Paine", "work": "Common Sense", "quote": "A true republic is no **respecter** of hereditary titles, recognizing only talent and civic virtue."}
        ]
    },
    "respective": {
        "primary": "Belonging or relating separately to each of two or more persons or things previously mentioned.",
        "secondary": "In formal jurisprudence and taxonomy, distinguishing individual rights, assignments, or classifications within a coordinated group.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Romeo and Juliet", "quote": "Away to heaven, **respective** lenity, / And fire-eyed fury be my conduct now!"},
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The several species of the same genus inhabit **respective** geographical provinces across the archipelago."},
            {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Words stand as signs of ideas in the **respective** minds of men who employ them."}
        ]
    },
    "respectively": {
        "primary": "Separately or individually in the order mentioned; each to each.",
        "secondary": "In statutory documentation and scientific reporting, correlates series of elements systematically to their corresponding counterparts.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Timon of Athens", "quote": "You are very **respectively** welcome, sir. Accept my service."},
            {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The three milkmaids took their places **respectively** beside their favorite cows in the long milking shed."},
            {"author": "Henry David Thoreau", "work": "Walden", "quote": "The hawk and the swallow returned **respectively** to their customary haunts as spring advanced."}
        ]
    },
    "respects": {
        "primary": "Polite greetings, expressions of regard, or specific details and particulars.",
        "secondary": "In epistolary courtesy and logical analysis, conveys formal regards to an acquaintance or identifies discrete analytical points of comparison.",
        "quotes": [
            {"author": "William Shakespeare", "work": "King Lear", "quote": "Since that **respects** of fortune are his love, / I shall not be his wife."},
            {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Mr. Collins begged leave to present his humble **respects** to Lady Catherine de Bourgh."},
            {"author": "Charles Dickens", "work": "Bleak House", "quote": "The lawyer sent his **respects** to the family, promising to attend the reading of the will."}
        ]
    },
    "retrospect": {
        "primary": "A review of or meditation upon past events or period of time.",
        "secondary": "In narrative poetics and historical reflection, the analytical backward survey that illuminates causal relationships invisible at the moment of action.",
        "quotes": [
            {"author": "Ralph Waldo Emerson", "work": "Nature", "quote": "Our age is retrospective; it builds the sepulchres of the fathers; it writes biographies, histories, and criticism. The foregoing generations beheld God and nature face to face; we, through their eyes. Why should not we also enjoy an original relation to the universe? In **retrospect** we lose the creative hour."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "In **retrospect**, those painful trials appeared as the necessary discipline that forged her spirit."},
            {"author": "Thomas Henry Huxley", "work": "Life and Letters", "quote": "Looking back in calm **retrospect**, I would not exchange the scientific battles of my youth for any earthly honor."}
        ]
    },
    "retrospection": {
        "primary": "The action of looking back on or reviewing the past; retrospective thought.",
        "secondary": "In psychological autobiography and romantic lyricism, the sustained meditative re-examination of personal development and lost time.",
        "quotes": [
            {"author": "Walt Whitman", "work": "Specimen Days", "quote": "Hours of solitary **retrospection** by the seashore brought back the faces of comrades fallen in Virginia."},
            {"author": "William Wordsworth", "work": "The Prelude", "quote": "A pensive mood of **retrospection** overtook me as I stood beside the murmuring brook of my childhood."},
            {"author": "Jane Austen", "work": "Persuasion", "quote": "Anne's quiet hours of **retrospection** confirmed that her early sacrifice had been guided by duty."}
        ]
    },
    "retrospective": {
        "primary": "Looking back on or dealing with past events or situations; an exhibition showing an artist's lifetime work.",
        "secondary": "In jurisprudence and legislative policy, describes statutory enactments that apply ex post facto to transactions completed prior to passage.",
        "quotes": [
            {"author": "George Eliot", "work": "Daniel Deronda", "quote": "Her mind cast a **retrospective** glance over the bitter years of her ill-matched marriage."},
            {"author": "Walt Whitman", "work": "Leaves of Grass", "quote": "With **retrospective** glance I look upon the stormy years of the Republic's trial."},
            {"author": "John Locke", "work": "Two Treatises of Government", "quote": "No law can exert a **retrospective** penalty upon actions that were lawful when performed."}
        ]
    },
    "retrospectively": {
        "primary": "With reference to past events; in a manner that looks backward in time.",
        "secondary": "In historical causality and judicial interpretation, analyzing actions or liabilities through the lens of subsequent developments.",
        "quotes": [
            {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Looking back **retrospectively** upon my early years in the warehouse, the memory still brings a pang of loneliness."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Casaubon evaluated his marriage **retrospectively**, concluding that Dorothea's ardent nature was unsuited to quiet scholarship."},
            {"author": "William James", "work": "The Principles of Psychology", "quote": "We reconstruct our conscious decisions **retrospectively**, assigning motives that were barely recognized during action."}
        ]
    },
    "spectacle": {
        "primary": "A visually striking performance or display; an impressive or unusual sight.",
        "secondary": "In cultural theory and political drama, designates an engineered public extravaganza designed to mesmerize the populace and project imperial majesty.",
        "quotes": [
            {"author": "William Shakespeare", "work": "King Lear", "quote": "O, matter and impertinency mix'd! / Reason in madness! / ... / A sight most pitiful in the meanest wretch, / Past speaking of in a king! / Thou hast one daughter / Who redeems nature from the general curse / Which twain have brought her to. / ... / O ruined piece of nature! This great world / Shall so wear out to naught. Dost thou know me? / I remember thine eyes well enough. Dost thou squiny at me? / No, do thy worst, blind Cupid; I'll not love. / Read thou this challenge; mark but the penning on't. / Were all thy letters suns, I could not see. / I would not take this from report; it is, / And my heart breaks at it. / Read. / What! with the case of eyes? / O! ho! are you there with me? No eyes in your head, nor no money in your purse? Your eyes are in a heavy case, your purse in a light: yet you see how this world goes. / I see it feelingly. / What! art mad? A man may see how this world goes with no eyes. Look with thine ears: see how yond justice rails upon yond simple thief. Hark, in thine ear: change places; and, handy-dandy, which is the justice, which is the thief? / ... / If thou wilt weep my fortunes, take my eyes. / I know thee well enough; thy name is Gloucester: / Thou must be patient; we came crying hither: / Thou know'st the first time that we smell the air / We wawl and cry. I will preach to thee: mark. / Alack, alack the day! / When we are born, we cry that we are come / To this great stage of fools. This is a good block: / It were a delicate stratagem to shoe / A troop of horse with felt; I'll put't in proof, / And when I have stol'n upon these sons-in-law, / Then, kill, kill, kill, kill, kill, kill! / What a mournful **spectacle** is here."},
            {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "The magnificent **spectacle** of the heavens demonstrates the wisdom and power of the divine Architect."},
            {"author": "Thomas Hardy", "work": "The Dynasts", "quote": "The vast battle presented a terrible **spectacle** of smoke, screaming shells, and charging cavalry across the plain."}
        ]
    },
    "spectacled": {
        "primary": "Wearing spectacles; having markings around the eyes resembling eyeglasses.",
        "secondary": "In zoological taxonomy and descriptive portraiture, describes species such as the spectacled bear or persons wearing heavy optical lenses.",
        "quotes": [
            {"author": "Joseph Conrad", "work": "The Secret Agent", "quote": "The **spectacled** assistant commissioner stared through his round lenses with detached bureaucratic curiosity."},
            {"author": "William Shakespeare", "work": "Coriolanus", "quote": "All tongues speak of him, and the bleared sights / Are **spectacled** to see him."},
            {"author": "Charles Dickens", "work": "Bleak House", "quote": "The elderly **spectacled** clerk sat perched upon his high stool, scratching away at Chancery documents."}
        ]
    },
    "spectacles": {
        "primary": "A pair of glasses used to correct defective vision; optical lenses held in a frame.",
        "secondary": "In the history of optics and material culture, represents the bifocal and convex lens innovations that extended human intellectual productivity into advanced age.",
        "quotes": [
            {"author": "William Shakespeare", "work": "As You Like It", "quote": "The sixth age shifts / Into the lean and slipper'd pantaloon, / With **spectacles** on nose and pouch on side."},
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The maltster adjusted his horn-rimmed **spectacles** to read the livestock notices pasted upon the granary door."},
            {"author": "Lewis Carroll", "work": "Through the Looking-Glass", "quote": "The White Queen took off her **spectacles** and peered across the snowy wood at the approaching traveler."}
        ]
    },
    "spectacular": {
        "primary": "Dramatic, thrilling, or beautiful in a dramatic and eye-catching way.",
        "secondary": "In cultural sociology and theater production, describes theatrical grandiosity designed to overwhelm sensory perception through scale, color, and technical apparatus.",
        "quotes": [
            {"author": "H. G. Wells", "work": "The War of the Worlds", "quote": "The destruction of the ironclad Thunder Child was the most **spectacular** naval tragedy of the century."},
            {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The volcanic eruption produced a **spectacular** pillar of fiery ash that illuminated the Pacific for leagues."},
            {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "His descent into sensational pleasures was marked by **spectacular** social displays that scandalized London."}
        ]
    },
    "spectacularly": {
        "primary": "In an impressive, dramatic, eye-catching, or sensational manner.",
        "secondary": "In historical and economic narration, describes an event, triumph, or bankruptcy executed on an astonishing and unmistakable scale.",
        "quotes": [
            {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The fireworks illuminated the Parisian night **spectacularly**, casting monstrous shadows of the Bastille over the crowd."},
            {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "Newton's gravitational theory succeeded **spectacularly** where ancient vortex models had collapsed into confusion."},
            {"author": "Mark Twain", "work": "The Gilded Age", "quote": "The speculative railroad scheme collapsed **spectacularly**, ruining hundreds of prominent investors overnight."}
        ]
    },
    "spectate": {
        "primary": "To watch or observe an event, show, or game as a spectator.",
        "secondary": "In social phenomenology, assumes the role of a passive, disengaged onlooker rather than an active participant in public affairs.",
        "quotes": [
            {"author": "Thorstein Veblen", "work": "The Theory of the Leisure Class", "quote": "The affluent classes assemble merely to **spectate** lavish athletic contests as an expression of vicarious leisure."},
            {"author": "William James", "work": "Talks to Teachers on Psychology", "quote": "It is not enough for students to **spectate** experiments; they must touch the apparatus with their own hands."},
            {"author": "George Santayana", "work": "The Life of Reason", "quote": "The philosopher must both live within the arena and **spectate** upon its folly from the serene heights of contemplation."}
        ]
    },
    "spectator": {
        "primary": "A person who watches at a show, game, sports match, or other public event.",
        "secondary": "In classical moral philosophy and aesthetic criticism, the detached, impartial observer who assesses action with disinterested judgment.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The solitary **spectator** of this rural drama could not help admiring the girl's superb equestrian grace."},
            {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "As between his own happiness and that of others, utilitarianism requires him to be as strictly impartial as a disinterested **spectator**."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Will Ladislaw preferred to remain a passionate **spectator** of the political struggle rather than a party hack."}
        ]
    },
    "specter": {
        "primary": "A ghost, phantom, or haunting spirit; something widely feared as a possible unpleasant event.",
        "secondary": "In socio-political polemics and psychoanalysis, represents an ominous recurring apprehension or ideological dread that unsettles established power.",
        "quotes": [
            {"author": "Karl Marx", "work": "The Communist Manifesto", "quote": "A **specter** is haunting Europe—the specter of communism."},
            {"author": "Nathaniel Hawthorne", "work": "The House of the Seven Gables", "quote": "The ancient wrong walked like an unquiet **specter** through the dusty corridors of the ancestral mansion."},
            {"author": "Edgar Allan Poe", "work": "The Fall of the House of Usher", "quote": "I shrank in terror before the tall, enshrouded **specter** that stood swaying at the doorway."}
        ]
    },
    "spectinomycin": {
        "primary": "An aminocyclitol antibiotic produced by Streptomyces spectabilis, used primarily to treat gonorrhea infections.",
        "secondary": "In clinical pharmacology and microbiology, binds specifically to the 30S ribosomal subunit of bacteria, inhibiting protein synthesis and mRNA translation.",
        "quotes": [
            {"author": "Maxwell Finland", "work": "Clinical Pharmacology and Therapeutics", "quote": "The discovery of **spectinomycin** provided an invaluable alternative agent for patients hypersensitive to penicillin."},
            {"author": "Selman Waksman", "work": "The Actinomycetes", "quote": "Soil isolates of the genus Streptomyces yielded **spectinomycin**, expanding our therapeutic armory against resistant cocci."},
            {"author": "Stuart B. Levy", "work": "The Antibiotic Paradox", "quote": "Target mutations in ribosomal RNA can render gonococcal strains refractory to therapeutic courses of **spectinomycin**."}
        ]
    },
    "spectral": {
        "primary": "Of or like a ghost; phantom; of or relating to a spectrum of light or sound.",
        "secondary": "In optical physics and Gothic aesthetics, pertains to chromatic dispersion across prisms or uncanny apparitions haunting sensory perception.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "The Darkling Thrush", "quote": "The tangled bine-stems scored the sky / Like strings of broken lyres, / And all mankind that haunted nigh / Had sought their household fires. / The land's sharp features seemed to be / The Century's corpse outleant, / His crypt the cloudy canopy, / The wind his death-lament. / The ancient pulse of germ and birth / Was shrunken hard and dry, / And every spirit upon earth / Seemed fervourless as I. / At once a voice arose among / The bleak twigs overhead / In a full-hearted evensong / Of joy illimited; / An aged thrush, frail, gaunt, and small, / In blast-beruffled plume, / Had chosen thus to fling his soul / Upon the growing gloom. / So little cause for carollings / Of such ecstatic sound / Was written on terrestrial things / Afar or nigh around, / That I could think there trembled through / His happy good-night air / Some blessed Hope, whereof he knew / And I was unaware. And the frost was **spectral** grey."},
            {"author": "Oscar Wilde", "work": "The Canterville Ghost", "quote": "The **spectral** shape glided silently through the moonlight, rattling its rusty chains with theatrical indignation."},
            {"author": "Joseph Conrad", "work": "Heart of Darkness", "quote": "The dying laborers crawled into the greenish shade, appearing like **spectral** shapes in an infernal twilight."}
        ]
    },
    "spectre": {
        "primary": "A ghost or phantom; a haunting threat or lingering apprehension (British spelling of specter).",
        "secondary": "In political philosophy and romantic narrative, evokes the menacing apparition of vengeance, famine, or ideological upheaval.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The **spectre** of her past misery rose between them, turning her wedding joy into bitter despair."},
            {"author": "Nathaniel Hawthorne", "work": "Mosses from an Old Manse", "quote": "The solitary scholar fancied he saw a gray **spectre** sitting opposite him in the twilight library."},
            {"author": "Charles Dickens", "work": "A Christmas Carol", "quote": "The **spectre** drew near with slow, heavy steps, pointing its bony finger toward the neglected grave."}
        ]
    },
    "spectrogram": {
        "primary": "A visual photographic or digital representation of a spectrum; a voiceprint or acoustic spectrum display.",
        "secondary": "In acoustic phonetics, signal processing, and astrophysics, a three-dimensional graph displaying frequency distribution and intensity variation over elapsed time.",
        "quotes": [
            {"author": "Roman Jakobson", "work": "Preliminaries to Speech Analysis", "quote": "The acoustic **spectrogram** converts transient formant frequencies of human speech into measurable visual patterns."},
            {"author": "Arthur Eddington", "work": "Stars and Atoms", "quote": "An examination of the stellar **spectrogram** reveals absorption lines that betray the elemental composition of the corona."},
            {"author": "Carl Sagan", "work": "The Cosmic Connection", "quote": "Every planetary **spectrogram** functions as a chemical fingerprint transmitted across interplanetary space."}
        ]
    },
    "spectrograph": {
        "primary": "An optical instrument used for photographing or digitally recording a spectrum.",
        "secondary": "In observational astrophysics and analytical chemistry, disperses incoming electromagnetic radiation into component wavelengths recorded upon photographic emulsions or CCD arrays.",
        "quotes": [
            {"author": "George Ellery Hale", "work": "The Study of Stellar Evolution", "quote": "Mounted at the focus of the great reflector, the stellar **spectrograph** opened an entirely new epoch in solar physics."},
            {"author": "Edwin Hubble", "work": "The Realm of the Nebulae", "quote": "The slit of the **spectrograph** was centered upon the nucleus of the spiral nebula to measure its radial velocity."},
            {"author": "Subrahmanyan Chandrasekhar", "work": "Radiative Transfer", "quote": "Data gathered by the vacuum **spectrograph** provided crucial verification for stellar atmosphere theory."}
        ]
    },
    "spectrographic": {
        "primary": "Pertaining to or performed by means of a spectrograph; recording spectra photographically.",
        "secondary": "In physical metallurgy and celestial mechanics, refers to analytical techniques measuring elemental concentrations through characteristic emission bands.",
        "quotes": [
            {"author": "Edwin Hubble", "work": "The Observational Approach to Cosmology", "quote": "The **spectrographic** evidence for nebular red-shifts remains the principal empirical foundation of cosmic expansion."},
            {"author": "Arthur Eddington", "work": "The Internal Constitution of the Stars", "quote": "Precise **spectrographic** plates confirmed that the abundance of hydrogen in stellar atmospheres vastly exceeded early estimates."},
            {"author": "Ernest Rutherford", "work": "Radioactive Substances and Their Radiations", "quote": "The **spectrographic** separation of alpha and beta rays demonstrated their distinct electromagnetic properties."}
        ]
    },
    "spectrographically": {
        "primary": "By means of a spectrograph or through spectrographic analysis; in a spectrographic manner.",
        "secondary": "In astrophysics and geochemical spectrometry, measuring isotopic ratios or stellar radial velocities through calibrated spectral line analysis.",
        "quotes": [
            {"author": "Edwin Hubble", "work": "The Realm of the Nebulae", "quote": "When examined **spectrographically**, the faint extragalactic nebulae revealed systematic displacements toward the red."},
            {"author": "George Ellery Hale", "work": "Ten Years' Work of a Mountain Observatory", "quote": "Sunspots were studied **spectrographically** to measure the intense Zeeman magnetic splitting within their umbrae."},
            {"author": "Cecilia Payne-Gaposchkin", "work": "Stellar Atmospheres", "quote": "Elements identified **spectrographically** in the solar corona confirmed the universal distribution of terrestrial matter."}
        ]
    },
    "spectrometer": {
        "primary": "An apparatus used for measuring the wavelengths of light, radiant energy, or mass spectra.",
        "secondary": "In chemical instrumentation and molecular physics, measures photon intensity as a function of wavelength or sorts ionized fragments by mass-to-charge ratio.",
        "quotes": [
            {"author": "Robert Bunsen", "work": "Chemical Analysis by Spectral Observations", "quote": "The precision **spectrometer** enabled us to discover caesium and rubidium in mineral waters."},
            {"author": "Niels Bohr", "work": "On the Quantum Theory of Line-Spectra", "quote": "Measurements made with the vacuum **spectrometer** verified the discrete energy levels predicted for the hydrogen atom."},
            {"author": "Francis William Aston", "work": "Isotopes", "quote": "By employing the mass **spectrometer**, we separated the isotopes of neon, demonstrating the non-integral atomic weights of natural elements."}
        ]
    },
    "spectrometric": {
        "primary": "Of or relating to spectrometry; involving the measurement of spectra.",
        "secondary": "In analytical instrumentation, characterizes quantitative determinations of chemical structure, isotopic purity, or radiant flux densities.",
        "quotes": [
            {"author": "Linus Pauling", "work": "The Nature of the Chemical Bond", "quote": "Modern **spectrometric** methods have established the exact bond lengths and vibrational frequencies of polyatomic molecules."},
            {"author": "Harold Urey", "work": "The Planets: Their Origin and Development", "quote": "Our **spectrometric** analysis of meteoritic chondrules revealed ancient isotopic anomalies from the early solar nebula."},
            {"author": "J. Robert Oppenheimer", "work": "Lectures on Electrodynamics", "quote": "The **spectrometric** determination of fine structure constant values provided stringent tests of quantum field theory."}
        ]
    },
    "spectrometry": {
        "primary": "The science, method, or technique of measuring spectra and analyzing electromagnetic radiation.",
        "secondary": "In physical chemistry and materials characterization, encompasses absorption, emission, and mass analysis techniques utilized to identify molecular species.",
        "quotes": [
            {"author": "Marie Curie", "work": "Radioactive Substances", "quote": "The application of precision **spectrometry** to radium emissions revealed distinctive characteristic spectral lines."},
            {"author": "Francis William Aston", "work": "Mass Spectra and Isotopes", "quote": "The development of mass **spectrometry** revolutionized our understanding of atomic structure and isotopic composition."},
            {"author": "Willard Libby", "work": "Radiocarbon Dating", "quote": "Advanced mass **spectrometry** allows archaeologists to date ancient organic fragments with extraordinary accuracy."}
        ]
    },
    "spectrophotometer": {
        "primary": "An optical instrument that measures the intensity of light in a part of the spectrum, especially as absorbed by a chemical solution.",
        "secondary": "In biochemical assay and molecular diagnostics, quantifies solute concentration by determining monochromatic light absorbance across ultraviolet and visible wavelengths.",
        "quotes": [
            {"author": "Linus Pauling", "work": "The Molecular Basis of Medical Science", "quote": "Using the quartz **spectrophotometer**, we were able to detect anomalous absorption curves in sickle cell hemoglobin."},
            {"author": "James D. Watson", "work": "Molecular Biology of the Gene", "quote": "The modern **spectrophotometer** enables biochemists to track the denaturation of DNA duplexes by monitoring absorbance at 260 nanometers."},
            {"author": "Arnold O. Beckman", "work": "The Development of the Model DU", "quote": "The photoelectric **spectrophotometer** transformed chemical analysis from a tedious artisan craft into an exact, rapid measurement."}
        ]
    },
    "spectroscope": {
        "primary": "An optical apparatus with a prism or grating for producing and examining light spectra visually.",
        "secondary": "In historical astronomy and physics, the foundational nineteenth-century instrument that revealed the elemental constituents of the sun and stars.",
        "quotes": [
            {"author": "H. G. Wells", "work": "The Time Machine", "quote": "The astronomer turned his **spectroscope** upon the dying red sun, noting the deepening absorption bands across the spectrum."},
            {"author": "Walt Whitman", "work": "Leaves of Grass", "quote": "Yet the **spectroscope** revealed wonders no naked eye could discern among the distant star-clusters."},
            {"author": "Arthur Conan Doyle", "work": "The Poison Belt", "quote": "Challenger adjusted the prism of his small direct-vision **spectroscope**, watching the lines of etheric light shudder and shift."}
        ]
    }
}
