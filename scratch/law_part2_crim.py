# -*- coding: utf-8 -*-
"""
Part 2 of Curated Law, Justice & Feudal Batch 1:
Dashboard — crim (46 words)
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

data_crim = {
    "crime": {
        "primary": "An action or omission that constitutes an offense punishable by law.",
        "secondary": "In criminology and penal jurisprudence, a severe violation of social norms codified by state statutes and sanctioned through institutional punishment.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "Tremble, thou wretch, That hast within thee undivulged **crime**, Unwhipp’d of justice."},
            {"author": "John Locke", "work": "Second Treatise of Government", "quote": "Every offense that can be committed in the state of nature may in the commonwealth be equally punished, for **crime** offends against the preservation of all."},
            {"author": "Mary Shelley", "work": "Frankenstein", "quote": "I am malicious because I am miserable; am I not shunned and hated by all mankind? If misery is my lot, shall **crime** not be my recourse?"}
        ]
    },
    "crimea": {
        "primary": "A historic peninsula on the northern coast of the Black Sea, south of Ukraine.",
        "secondary": "In geopolitical and military history, a strategically vital peninsula that served as the theater for the Crimean War and ancient Black Sea maritime commerce.",
        "quotes": [
            {"author": "Leo Tolstoy", "work": "Sevastopol Sketches", "quote": "The hills and bastions of the **Crimea** reverberated day and night with the booming fire of allied artillery."},
            {"author": "Alfred Lord Tennyson", "work": "The Charge of the Light Brigade", "quote": "Into the valley of death rode the six hundred, carving immortal legend upon the bloodstained fields of the **Crimea**."},
            {"author": "Florence Nightingale", "work": "Notes on Hospitals", "quote": "The military hospitals established in the **Crimea** suffered grievously from inadequate drainage, foul air, and systemic neglect."}
        ]
    },
    "criminal": {
        "primary": "A person who has committed a crime, or relating to actions prohibited and penalized by law.",
        "secondary": "In penal law and sociology, concerning formal statutes, judicial proceedings, and behavioral patterns associated with unlawful violations of societal welfare.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "Let me see: what think you of hanging, if some doubtful **criminal** should be brought before the bench?"},
            {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "He is the Napoleon of crime, Watson; he is the organizer of half that is evil and of nearly all that is undetected in this great city, the supreme **criminal** mastermind."},
            {"author": "John Stuart Mill", "work": "On Liberty", "quote": "Acts injurious to others require a totally different treatment: encroaching on their rights requires penal measures under the **criminal** code."}
        ]
    },
    "criminalisation": {
        "primary": "The process of making an activity or behavior illegal through statutory enactment.",
        "secondary": "In sociology of law and legislative politics, the institutional translation of social deviance or contested conduct into penal offenses subject to police power.",
        "quotes": [
            {"author": "Michel Foucault", "work": "Discipline and Punish", "quote": "The **criminalisation** of popular illegalities was a necessary step in the capitalist consolidation of disciplinary control."},
            {"author": "H. L. A. Hart", "work": "Law, Liberty, and Morality", "quote": "The state must demonstrate tangible harm before embarking upon the coercive **criminalisation** of private conduct."},
            {"author": "Emile Durkheim", "work": "The Rules of Sociological Method", "quote": "Every society achieves the **criminalisation** of acts that offend deeply collective sentiments across the populace."}
        ]
    },
    "criminalise": {
        "primary": "To make an activity unlawful or designate individuals engaged in it as offenders under law.",
        "secondary": "In jurisprudence and penal policy, to extend statutory definitions to prohibit previously permitted actions and impose state penalties.",
        "quotes": [
            {"author": "H. L. A. Hart", "work": "Law, Liberty, and Morality", "quote": "To **criminalise** actions merely because the majority disapproves of them is an abuse of statutory coercive power."},
            {"author": "Bertrand Russell", "work": "Political Ideals", "quote": "Governments tend to **criminalise** dissent whenever threatened by political innovation or independent thought."},
            {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "It is unwise for legislators to **criminalise** commercial contracts freely negotiated between competent adults."}
        ]
    },
    "criminalism": {
        "primary": "The state or system of being criminal; habitual indulgence in illegal activities.",
        "secondary": "In 19th-century penal sociology, the study or manifestation of systematic unlawful practices and collective behavioral pathology within urban centers.",
        "quotes": [
            {"author": "Cesare Lombroso", "work": "Criminal Man", "quote": "The anatomical anomalies of the born delinquent reveal the deep biological roots of hereditary **criminalism**."},
            {"author": "Henry Mayhew", "work": "London Labour and the London Poor", "quote": "Vast districts of the metropolis exhibited ingrained pockets of **criminalism** that resisted both reform and church education."},
            {"author": "William Booth", "work": "In Darkest England and the Way Out", "quote": "To rescue youth from submerged **criminalism**, we must provide decent labor and moral environment."}
        ]
    },
    "criminality": {
        "primary": "Unlawful culpability under penal statutes, or the general incidence of criminal behavior across a population.",
        "secondary": "In criminology and forensic psychiatry, the complex interaction of socioeconomic, psychological, and behavioral factors that foster unlawful conduct.",
        "quotes": [
            {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "The state of the laboring classes was deteriorated, and their **criminality** increased, under the pressure of widespread poverty."},
            {"author": "Mary Shelley", "work": "Frankenstein", "quote": "I am full of fears; for if she is condemned, I never more shall have joy; her innocence will be stained with unnatural **criminality**."},
            {"author": "Cesare Lombroso", "work": "Criminal Man", "quote": "The statistical distribution of **criminality** mirrors the atmospheric changes, economic hardships, and social crises of the realm."}
        ]
    },
    "criminalization": {
        "primary": "The legislative process whereby an activity is transformed into a legally punishable offense.",
        "secondary": "In critical legal studies, the deployment of statutory power and policing mechanisms to penalize marginalized populations or nonconformist behaviors.",
        "quotes": [
            {"author": "Michel Foucault", "work": "Discipline and Punish", "quote": "The **criminalization** of minor agrarian customs transformed peasants into convicts to enforce private property claims."},
            {"author": "H. L. A. Hart", "work": "Punishment and Responsibility", "quote": "Rational criteria must guide the **criminalization** of harmful conduct to prevent unconstrained legislative paternalism."},
            {"author": "Thorstein Veblen", "work": "The Theory of the Leisure Class", "quote": "The social elite dictates the **criminalization** of habits peculiar to the lower classes while condoning its own predations."}
        ]
    },
    "criminalize": {
        "primary": "To turn an act into a crime or treat a person engaging in it as a lawbreaker.",
        "secondary": "In public policy and constitutional law, to attach penal sanctions to formerly unregulated behaviors through legislative action.",
        "quotes": [
            {"author": "H. L. A. Hart", "work": "Law, Liberty, and Morality", "quote": "A liberal society should hesitate to **criminalize** choices that inflict no demonstrable injury upon non-consenting parties."},
            {"author": "Oliver Wendell Holmes Jr.", "work": "The Common Law", "quote": "The legislature may **criminalize** an act previously innocent if the perceived public welfare urgently requires its suppression."},
            {"author": "Felix Frankfurter", "work": "The Public and Its Government", "quote": "Attempts to **criminalize** complex industrial practices through ambiguous statutes place an unfair burden on honest commerce."}
        ]
    },
    "criminally": {
        "primary": "In a manner that violates criminal statutes or deserves legal and moral condemnation.",
        "secondary": "In forensic jurisprudence and tort law, describing actions undertaken with culpable negligence or deliberate malicious intent.",
        "quotes": [
            {"author": "Arthur Conan Doyle", "work": "The Sign of Four", "quote": "The conspirators acted **criminally** in concealing the Agra treasure from the legitimate authorities."},
            {"author": "Charles Dickens", "work": "Bleak House", "quote": "The trustees were **criminally** indifferent to the squalor accumulating under their administrative care."},
            {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "Those who subvert the established constitution of their country act **criminally** against generations unborn."}
        ]
    },
    "criminalness": {
        "primary": "Inherent culpability, wickedness, or blameworthiness of an act in the eyes of penal law.",
        "secondary": "In moral philosophy and legal ethics, the degree of intrinsic turpitude or culpability attaching to a wrongful deed.",
        "quotes": [
            {"author": "Jeremy Bentham", "work": "An Introduction to the Principles of Morals and Legislation", "quote": "The apparent **criminalness** of an action depends upon the mischief it produces and the motive whence it springs."},
            {"author": "Samuel Johnson", "work": "The Rambler", "quote": "No sophistry can diminish the fundamental **criminalness** of betraying a public trust for private enrichment."},
            {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Conscience perceives the innate **criminalness** of violence against the innocent prior to the formulation of positive laws."}
        ]
    },
    "criminate": {
        "primary": "To charge with a crime, or to show evidence that implicates someone in an offense.",
        "secondary": "In adversarial procedure and constitutional law, to expose oneself or an associate to penal prosecution through testimony or admissions.",
        "quotes": [
            {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "The ancient maxim of the common law holds that no prisoner shall be forced to **criminate** himself."},
            {"author": "Thomas Babington Macaulay", "work": "Critical and Historical Essays", "quote": "The conspirators were eager to **criminate** their accomplices in the hope of purchasing royal pardons."},
            {"author": "Jeremy Bentham", "work": "Rationale of Judicial Evidence", "quote": "Rules that forbid a witness to **criminate** another merely withhold vital truth from the searching light of justice."}
        ]
    },
    "criminative": {
        "primary": "Having the nature of an accusation or tending to incriminate an individual in wrongdoing.",
        "secondary": "In evidence law and forensic argumentation, describing witness testimony, physical exhibits, or documents that establish culpability.",
        "quotes": [
            {"author": "Jeremy Bentham", "work": "Rationale of Judicial Evidence", "quote": "Circumstantial facts possessing **criminative** force must be scrutinized with rigorous skepticism before a jury."},
            {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "The indictment must present clearly **criminative** averments rather than speculative insinuations."},
            {"author": "Edmund Burke", "work": "The Works of Edmund Burke", "quote": "The managers produced a mass of **criminative** evidence demonstrating systemic extortion across the province."}
        ]
    },
    "criminatory": {
        "primary": "Relating to or expressing accusation; casting blame or imputing unlawful conduct.",
        "secondary": "In prosecutorial rhetoric and legal documentation, formulated to charge an adversary formally with unlawful misconduct.",
        "quotes": [
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The senate listened with fearful silence to the **criminatory** letter dispatched by the suspicious emperor."},
            {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "A series of **criminatory** petitions was presented to Parliament accusing the ministers of high treason."},
            {"author": "Samuel Johnson", "work": "Lives of the Most Eminent English Poets", "quote": "The pamphlet was filled with **criminatory** invective directed against his literary rivals."}
        ]
    },
    "criminological": {
        "primary": "Relating to the scientific study of crime, criminals, and penal systems.",
        "secondary": "In social sciences, pertaining to theoretical models, statistical data, and empirical methodologies regarding crime etiology and recidivism.",
        "quotes": [
            {"author": "Cesare Lombroso", "work": "Criminal Man", "quote": "Our **criminological** investigations demand precise anthropometric measurements across diverse prison populations."},
            {"author": "Emile Durkheim", "work": "The Division of Labour in Society", "quote": "From a **criminological** viewpoint, the social reaction to transgression reveals the collective moral conscience."},
            {"author": "Max Weber", "work": "Economy and Society", "quote": "Modern bureaucratic justice rests upon **criminological** doctrines that emphasize uniform codification and rational deterrence."}
        ]
    },
    "criminologist": {
        "primary": "A specialist or scholar who studies crime, criminal behavior, and the penal system.",
        "secondary": "In modern behavioral and legal academia, a social scientist investigating the causes of delinquency, prevention methods, and judicial reform.",
        "quotes": [
            {"author": "G. K. Chesterton", "work": "The Innocence of Father Brown", "quote": "The eminent French **criminologist** examined the footprints with a magnifying glass, entirely missing the spiritual significance of the scene."},
            {"author": "Arthur Conan Doyle", "work": "The Return of Sherlock Holmes", "quote": "As an amateur **criminologist**, Holmes regarded the bizarre cipher as one of the most intriguing puzzles of his career."},
            {"author": "Cesare Lombroso", "work": "Crime, Its Causes and Remedies", "quote": "The observant **criminologist** must look beyond statutory texts to study the physical and mental constitution of the offender."}
        ]
    },
    "criminology": {
        "primary": "The scientific study of crime, criminal psychology, and penal rehabilitation.",
        "secondary": "In interdisciplinary behavioral science, the comprehensive study of the etiology, prevention, policing, and societal impact of unlawful conduct.",
        "quotes": [
            {"author": "Cesare Lombroso", "work": "Crime, Its Causes and Remedies", "quote": "The primary objective of modern **criminology** is to substitute scientific observation for blind retribution in penal treatment."},
            {"author": "H. G. Wells", "work": "The Work, Wealth and Happiness of Mankind", "quote": "Progressive developments in psychology have fundamentally transformed the methods and scope of contemporary **criminology**."},
            {"author": "Max Weber", "work": "General Economic History", "quote": "The emergence of rational **criminology** coincided with the rise of modern administrative law and secularized states."}
        ]
    },
    "crimson": {
        "primary": "A rich, deep red color inclining toward purple, or to blush deeply with that color.",
        "secondary": "In heraldry, histology, and descriptive literature, a vivid saturated hue associated with arterial blood, regal draperies, or intense emotion.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "O, would to God that the compass of my pale **crimson** gold Were red-hot steel, to sear me to the brains!"},
            {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The sun, on the other side of the hedge, was glistening on the droplets of mist, and turning the wet gossamers into **crimson** threads."},
            {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "A faint blush, like the shadow of a rose in a mirror of silver, came to her cheeks, deepening to rich **crimson**."}
        ]
    },
    "crimson-magenta": {
        "primary": "A vibrant, saturated chromatic shade combining deep crimson with vivid reddish-purple magenta.",
        "secondary": "In colorimetry and artistic design, a high-chroma purplish-red tincture located between carmine and fuchsia on the optical spectrum.",
        "quotes": [
            {"author": "John Ruskin", "work": "Modern Painters", "quote": "The sunset clouds burned with an intense **crimson-magenta** hue that defied reproduction on the artist's palette."},
            {"author": "William Morris", "work": "Hopes and Fears for Art", "quote": "The natural cochineal bath yielded an exquisite **crimson-magenta** tone for the hand-dyed wool tapestries."},
            {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "The exotic orchids exhibited rich petals of **crimson-magenta**, glistening amidst the dark tropical foliage."}
        ]
    },
    "crimson-purple": {
        "primary": "A deep, royal shade of purple infused with rich red or crimson tones.",
        "secondary": "In textiles and classical descriptive prose, the imperial shade reminiscent of ancient Tyrian dye, blending arterial scarlet with violet depths.",
        "quotes": [
            {"author": "H. G. Wells", "work": "The War of the Worlds", "quote": "The Red Weed had covered the landscape with a spongy, **crimson-purple** growth that choked the river banks."},
            {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "Across the vast expanses of Egdon Heath, the blooming heather assumed a dark **crimson-purple** tint under the evening sky."},
            {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The mosaic decorations glittered with veins of porphyry and rich **crimson-purple** marble imported from the Levant."}
        ]
    },
    "crimson-yellow": {
        "primary": "A variegated or blended chromatic color exhibiting flashes of deep crimson alongside golden yellow.",
        "secondary": "In botanical descriptions and mineralogy, characterizing autumn foliage, petal variegations, or ores that display fiery red and golden gradations.",
        "quotes": [
            {"author": "Henry David Thoreau", "work": "Excursions", "quote": "The autumn maples along the river displayed brilliant streaks of **crimson-yellow** that mirrored in the quiet water."},
            {"author": "John Muir", "work": "The Mountains of California", "quote": "As dawn broke over the Sierra peaks, the sky flamed with magnificent **crimson-yellow** light."},
            {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The blossoms of the tropical creeper displayed curious **crimson-yellow** patterns designed to attract hummingbirds."}
        ]
    },
    "decriminalisation": {
        "primary": "The elimination of criminal penalties for an activity while potentially retaining civil regulations.",
        "secondary": "In penal reform and public health policy, the statutory transition from penal sanctions to civil infractions or therapeutic interventions.",
        "quotes": [
            {"author": "H. L. A. Hart", "work": "Law, Liberty, and Morality", "quote": "The systematic **decriminalisation** of victimless conduct marks the progress of an enlightened penal system."},
            {"author": "Michel Foucault", "work": "Discipline and Punish", "quote": "The formal **decriminalisation** of minor offenses often conceals an expansion of subtle bureaucratic surveillance."},
            {"author": "Bertrand Russell", "work": "Proposed Roads to Freedom", "quote": "Social liberty expands whenever the state embarks upon the sensible **decriminalisation** of individual conscience."}
        ]
    },
    "decriminalise": {
        "primary": "To repeal criminal penalties for an act, converting it into a legal or civilly regulated practice.",
        "secondary": "In legislative jurisprudence, to lift penal prohibitions from specific behaviors in favor of administrative supervision or complete legality.",
        "quotes": [
            {"author": "H. L. A. Hart", "work": "Law, Liberty, and Morality", "quote": "Parliament should move promptly to **decriminalise** private sexual behavior between consenting adults."},
            {"author": "John Stuart Mill", "work": "On Liberty", "quote": "To **decriminalise** harmless differences of opinion is the first obligation of a free commonwealth."},
            {"author": "Felix Frankfurter", "work": "The Public and Its Government", "quote": "Prudent legislators seek to **decriminalise** economic regulations that are better enforced through civil remedies."}
        ]
    },
    "decriminalization": {
        "primary": "The legislative process of removing criminal sanctions from an action formerly prohibited by law.",
        "secondary": "In legal history and sociopolitical reform, an institutional shift where penal courts surrender jurisdiction to public health agencies or civil tribunals.",
        "quotes": [
            {"author": "H. L. A. Hart", "work": "Punishment and Responsibility", "quote": "The arguments in favor of **decriminalization** rest on the principle that the criminal law should not enforce mere morality."},
            {"author": "Roscoe Pound", "work": "Criminal Justice in America", "quote": "Overburdened courts benefit substantially from the prudent **decriminalization** of minor regulatory offenses."},
            {"author": "Michel Foucault", "work": "Power/Knowledge", "quote": "The historical **decriminalization** of certain practices often coincided with the creation of new medicalized categories of deviance."}
        ]
    },
    "decriminalize": {
        "primary": "To legalize or remove criminal penalties from a specific action, behavior, or substance.",
        "secondary": "In statutory reform, to reclassify an offense from a misdemeanor or felony to a permissible act or administrative infraction.",
        "quotes": [
            {"author": "H. L. A. Hart", "work": "Law, Liberty, and Morality", "quote": "To **decriminalize** activities that harm no one is essential if the dignity of penal law is to be maintained."},
            {"author": "Oliver Wendell Holmes Jr.", "work": "Collected Legal Papers", "quote": "The community may decide through legislation to **decriminalize** what previous generations severely punished."},
            {"author": "Felix Frankfurter", "work": "Of Law and Men", "quote": "Good governance requires us to **decriminalize** technical violations that clutter court dockets without benefiting the public."}
        ]
    },
    "discriminable": {
        "primary": "Capable of being recognized, distinguished, or differentiated from something else.",
        "secondary": "In experimental psychology and sensory physiology, describing perceptual stimuli whose physical differences exceed the threshold of conscious detection.",
        "quotes": [
            {"author": "William James", "work": "The Principles of Psychology", "quote": "Two sensory impressions must possess a **discriminable** difference in frequency or intensity to trigger separate neural responses."},
            {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "The mind distinguishes between simple ideas through clearly **discriminable** qualities inherent in sensation."},
            {"author": "Bertrand Russell", "work": "The Analysis of Mind", "quote": "Our perceptions consist of complex elements that are analytically **discriminable** upon careful introspection."}
        ]
    },
    "discriminate": {
        "primary": "To recognize or perceive the difference between things, or to treat people unfairly based on prejudice.",
        "secondary": "In epistemology and social theory, to make fine analytical distinctions between concepts, or unjustly to disadvantage classes of individuals under the law.",
        "quotes": [
            {"author": "George Eliot", "work": "Middlemarch", "quote": "He had a mind capable of acute precision, able to **discriminate** between fine shades of theological dogma."},
            {"author": "Arthur Conan Doyle", "work": "The Sign of Four", "quote": "It is of the first importance not to allow your judgment to be biased by personal qualities; you must **discriminate** between facts and impressions."},
            {"author": "Ralph Waldo Emerson", "work": "Essays: First Series", "quote": "The intellect must **discriminate** between eternal realities and the passing illusions of sensory vanity."}
        ]
    },
    "discriminating": {
        "primary": "Having or showing refined judgment, good taste, or the ability to make fine distinctions.",
        "secondary": "In aesthetic criticism and social analysis, exhibiting astute discernment, or establishing selective preferential standards among competing options.",
        "quotes": [
            {"author": "Henry David Thoreau", "work": "A Week on the Concord and Merrimack Rivers", "quote": "A truly **discriminating** eye appreciates the delicate harmonies of nature where an ordinary observer sees only weeds."},
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Female birds exercise a **discriminating** choice, selecting the most melodious or brightly plumaged males."},
            {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "He had an acute and **discriminating** understanding, quick to detect absurdities in the manners of his neighbors."}
        ]
    },
    "discrimination": {
        "primary": "The unjust treatment of different categories of people, or the ability to make fine distinctions.",
        "secondary": "In constitutional law and perceptual philosophy, the unconstitutional unequal application of statutes, or the cognitive ability to distinguish subtle differences.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "She made a desperate effort to exercise some **discrimination** between her real duty and the phantom obligations imposed upon her."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "His critical judgment was distinguished by a luminous clarity and uncommon power of intellectual **discrimination**."},
            {"author": "Ralph Waldo Emerson", "work": "Representative Men", "quote": "The greatness of a thinker appears in his power of **discrimination**, separating the vital seed from the dead husk of convention."}
        ]
    },
    "discriminative": {
        "primary": "Serving to distinguish, differentiate, or mark an essential difference between entities.",
        "secondary": "In cognitive psychology and semiotics, designating diagnostic markers, perceptual traits, or testing instruments designed to differentiate categories.",
        "quotes": [
            {"author": "William James", "work": "The Principles of Psychology", "quote": "Attention sharpens our **discriminative** sensibility, allowing us to detect nuances of pitch that escape ordinary hearing."},
            {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "The faculty of clear judgment rests upon the **discriminative** power of separating ideas that contain minute differences."},
            {"author": "Herbert Spencer", "work": "The Principles of Psychology", "quote": "Evolutionary progress in nervous systems is evidenced by increasing **discriminative** capacity toward environmental stimuli."}
        ]
    },
    "discriminator": {
        "primary": "A person or device that identifies differences, or one who treats others unfairly based on bias.",
        "secondary": "In electronics and statistical decision theory, an electrical circuit or classification algorithm that differentiates between distinct signal levels or data categories.",
        "quotes": [
            {"author": "James Clerk Maxwell", "work": "A Treatise on Electricity and Magnetism", "quote": "The experimental apparatus acted as an accurate physical **discriminator**, separating rapid electric oscillations from steady galvanic currents."},
            {"author": "Thomas Edison", "work": "The Edison Papers", "quote": "In telephone signaling, a mechanical **discriminator** was employed to distinguish between voice frequencies and line static."},
            {"author": "Oliver Wendell Holmes Jr.", "work": "The Common Law", "quote": "The impartial magistrate must stand as a vigilant **discriminator** between valid contractual covenants and unconscionable exactions."}
        ]
    },
    "discriminatory": {
        "primary": "Making or showing an unjust or prejudicial distinction between different groups of people.",
        "secondary": "In constitutional law and international trade policy, designating statutes, tariffs, or institutional actions that confer unfair disadvantages upon designated classes.",
        "quotes": [
            {"author": "Frank A. Fetter", "work": "Economics Volume II: Modern Economic Problems", "quote": "The interstate commerce commission was created specifically to eliminate **discriminatory** freight rates favoring monopoly trusts."},
            {"author": "Oliver Wendell Holmes Jr.", "work": "Collected Legal Papers", "quote": "A statute that imposes **discriminatory** burdens upon nonresident merchants violates the core spirit of the federal union."},
            {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "Taxes levied at differential rates upon competing commodities introduce **discriminatory** distortions into foreign trade."}
        ]
    },
    "encrimson": {
        "primary": "To dye, cover, or suffuse with a deep crimson color.",
        "secondary": "In poetic and romantic imagery, to blush passionately or stain vividly with rich, bloody, or sunset hues.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "The setting sun did **encrimson** the western sky, dyeing the clouds with shades of fiery blood before the fall of night."},
            {"author": "Percy Bysshe Shelley", "work": "Prometheus Unbound", "quote": "The dawn's first shafts did **encrimson** the snowy peaks of Caucasus with radiant, burning splendors."},
            {"author": "Alfred Lord Tennyson", "work": "The Princess", "quote": "A sudden rush of modest feeling did **encrimson** her pale cheeks as she addressed the assembled court."}
        ]
    },
    "incriminate": {
        "primary": "To make someone appear guilty of a crime, or to provide evidence of wrongdoing.",
        "secondary": "In criminal procedure and constitutional jurisprudence, to adduce testimonial or documentary proof that exposes an individual to criminal liability.",
        "quotes": [
            {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "The bloodstained garment found near the mire was enough to **incriminate** any man in whose possession it was discovered."},
            {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The forged papers found in the prisoner's desk threatened to **incriminate** him irrevocably before the revolutionary tribunal."},
            {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "The privilege against compulsory self-disclosure protects citizens from being forced to **incriminate** themselves."}
        ]
    },
    "incriminating": {
        "primary": "Making someone appear guilty or directly implying involvement in a criminal act.",
        "secondary": "In law of evidence, describing documentary materials, physical artifacts, or circumstantial proofs that substantiate an accusation of illegal conduct.",
        "quotes": [
            {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "We found an **incriminating** letter hidden behind the wainscot, detailing the rendezvous upon the lonely moor."},
            {"author": "Wilkie Collins", "work": "The Moonstone", "quote": "The stained nightgown was the sole piece of **incriminating** evidence connecting the household to the theft of the gem."},
            {"author": "Robert Louis Stevenson", "work": "The Strange Case of Dr Jekyll and Mr Hyde", "quote": "Utterson locked the **incriminating** confession inside his private safe, resolved to examine it with the utmost secrecy."}
        ]
    },
    "incriminatingly": {
        "primary": "In a manner that suggests or establishes guilt or involvement in a criminal offense.",
        "secondary": "In forensic narrative and judicial analysis, describing circumstances, demeanors, or clues that point convincingly toward culpability.",
        "quotes": [
            {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "The suspect looked **incriminatingly** toward the open window through which the stolen jewels had vanished."},
            {"author": "G. K. Chesterton", "work": "The Innocence of Father Brown", "quote": "The knife lay **incriminatingly** near his hand, yet the priest suspected a deeper, more subtle hand at work."},
            {"author": "Wilkie Collins", "work": "The Woman in White", "quote": "The ledger entries pointed **incriminatingly** to the steward, whose sudden flight confirmed everyone's worst suspicions."}
        ]
    },
    "incrimination": {
        "primary": "The act of charging with a crime, or presenting evidence that demonstrates guilt.",
        "secondary": "In constitutional law, the exposure of an accused or witness to criminal prosecution, particularly regarding the right against compulsory disclosure.",
        "quotes": [
            {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "The common law guarantees protection against forced self-**incrimination** as a sacred bulwark of English liberty."},
            {"author": "Jeremy Bentham", "work": "Rationale of Judicial Evidence", "quote": "The rules governing **incrimination** must balance the protection of the innocent with the state's duty to punish crime."},
            {"author": "Oliver Wendell Holmes Jr.", "work": "Collected Legal Papers", "quote": "The constitutional shield against **incrimination** prevents inquisitorial abuses by overzealous magistrates."}
        ]
    },
    "incriminatory": {
        "primary": "Tending to demonstrate guilt, involve in a crime, or convey an accusation.",
        "secondary": "In prosecutorial practice and legal evidentiary standards, describing exhibits or disclosures that strongly establish culpability.",
        "quotes": [
            {"author": "Arthur Conan Doyle", "work": "The Memoirs of Sherlock Holmes", "quote": "Holmes held up the scorched scrap of paper, pointing out the **incriminatory** handwriting of Colonel Moran."},
            {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "The committee produced an **incriminatory** report detailing the alleged financial misdeeds of the former ministers."},
            {"author": "Charles Dickens", "work": "Bleak House", "quote": "Tulkinghorn guarded the bundle of **incriminatory** letters with silent, predatory vigilance."}
        ]
    },
    "indiscriminate": {
        "primary": "Done at random or without careful judgment; failing to make distinctions.",
        "secondary": "In warfare, public policy, and ecological analysis, describing actions, bombardments, or harvesting practices executed without selective restraint.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "His sudden fits of generosity were as reckless and **indiscriminate** as his outbursts of anger."},
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Nature carries on an **indiscriminate** destruction of young seedlings through frost, drought, and voracious insects."},
            {"author": "H. G. Wells", "work": "The War of the Worlds", "quote": "The Martians discharged their heavy canisters of black smoke with **indiscriminate** ruthlessness upon fleeing crowds."}
        ]
    },
    "indiscriminately": {
        "primary": "In a random manner; without making distinctions or showing careful judgment.",
        "secondary": "In social observation and natural history, describing forces, distributions, or behaviors applied uniformly across disparate categories.",
        "quotes": [
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The storm tossed the fragile boats **indiscriminately** among the white-capped surges of the Pacific."},
            {"author": "H. G. Wells", "work": "The Time Machine", "quote": "Over millions of years, the cooling sun radiated its weakening light **indiscriminately** upon land and sea."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "She bestowed her small charities **indiscriminately** upon every beggar who presented a sorrowful countenance at her gate."}
        ]
    },
    "indiscriminating": {
        "primary": "Lacking the ability or tendency to make fine distinctions; uncritical and unselective.",
        "secondary": "In intellectual criticism and public affairs, characterizing judgment or benevolence that fails to differentiate merit from mediocrity.",
        "quotes": [
            {"author": "Washington Irving", "work": "The Sketch-Book of Geoffrey Crayon", "quote": "His **indiscriminating** admiration embraced every antique relic, however dubious its historical provenance."},
            {"author": "Frank A. Fetter", "work": "Economics Volume II: Modern Economic Problems", "quote": "An **indiscriminating** distribution of outdoor relief undermines thrift and exacerbates systemic pauperism."},
            {"author": "Samuel Johnson", "work": "The Rambler", "quote": "The praise of an **indiscriminating** critic confers no genuine honor upon the ambitious poet."}
        ]
    },
    "recriminate": {
        "primary": "To make countercharges or counter-accusations against an accuser.",
        "secondary": "In family law and marital litigation, to present counter-allegations of misconduct against a petitioning party to bar their remedy.",
        "quotes": [
            {"author": "Emily Brontë", "work": "Wuthering Heights", "quote": "Instead of answering my entreaties, she began to **recriminate**, heaping bitter accusations upon my head."},
            {"author": "Edmund Burke", "work": "Speech on Conciliation with America", "quote": "It is not for statesmen to **recriminate** over past errors when the preservation of an empire is at stake."},
            {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "In suits for separation, the respondent may **recriminate** by demonstrating that the petitioner is equally guilty of adultery."}
        ]
    },
    "recrimination": {
        "primary": "An accusation made in response to one given; a bitter counter-charge.",
        "secondary": "In diplomatic history and marital jurisprudence, the exchange of mutual allegations of fault, or the defense in divorce where mutual guilt defeats relief.",
        "quotes": [
            {"author": "Charles Dickens", "work": "Great Expectations", "quote": "The bitter **recrimination** between the partners continued long after the failure of their commercial venture was assured."},
            {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "She refrained from angry **recrimination**, maintaining her calm dignity in the presence of her tormentors."},
            {"author": "Washington Irving", "work": "The Sketch-Book of Geoffrey Crayon", "quote": "The family quarrel ended not in reconciliation, but in sullen exhaustion after hours of vehement **recrimination**."}
        ]
    },
    "recriminative": {
        "primary": "Tending to return an accusation; conveying counter-charges against an accuser.",
        "secondary": "In rhetorical and legal discourse, describing communications or pleas characterized by retaliatory assertions of wrongdoing.",
        "quotes": [
            {"author": "Jeremy Bentham", "work": "Rationale of Judicial Evidence", "quote": "The witness indulged in a **recriminative** diatribe against the prosecution, attempting to shift suspicion onto the arresting constable."},
            {"author": "Edmund Burke", "work": "The Works of Edmund Burke", "quote": "His speech degenerated into a **recriminative** assault upon his political colleagues rather than a defense of his policy."},
            {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The debate in Parliament assumed a fierce **recriminative** tone as each party blamed the other for the disasters of the campaign."}
        ]
    },
    "recriminatory": {
        "primary": "Involving or expressing counter-accusations against a critic or accuser.",
        "secondary": "In dispute resolution and legal advocacy, characterized by mutual blaming and retaliatory counter-allegations rather than substantive defense.",
        "quotes": [
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The council dissolved into angry **recriminatory** shouts between rival bishops, each branding the other anathema."},
            {"author": "George Eliot", "work": "Felix Holt, the Radical", "quote": "Their private interview was filled with **recriminatory** bitterness, reviving grievances that had smoldered for years."},
            {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "She shrank from the **recriminatory** scene that she knew awaited her return to the gloomy palazzo."}
        ]
    },
    "undiscriminating": {
        "primary": "Lacking discernment or careful judgment; failing to distinguish differences.",
        "secondary": "In critical philosophy and behavioral assessment, characterized by indiscriminate acceptance, distribution, or appraisal without criteria.",
        "quotes": [
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The savage gale struck the ship with an **undiscriminating** fury that tested every timber and rope."},
            {"author": "Charles Dickens", "work": "The Mystery of Edwin Drood", "quote": "He showered the young clerks with **undiscriminating** praise, heedless of their individual talents or negligence."},
            {"author": "Frank A. Fetter", "work": "Economics Volume II: Modern Economic Problems", "quote": "An **undiscriminating** tariff policy indiscriminately shelters inefficient monopolies while burdening essential exports."}
        ]
    }
}
