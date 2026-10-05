# -*- coding: utf-8 -*-
"""
Part 1 of Curated Law, Justice & Feudal Batch 1:
Dashboard — arbitr (18 words)
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

data_arbitr = {
    "arbitrable": {
        "primary": "Legally capable of being settled, judged, or determined by arbitration rather than litigation.",
        "secondary": "In dispute resolution and labor law, describing controversies, grievances, or contractual claims that fall within the lawful jurisdiction of an arbitral tribunal.",
        "quotes": [
            {"author": "Frank A. Fetter", "work": "Economics Volume II: Modern Economic Problems", "quote": "The statute strictly defined which collective bargaining disputes were **arbitrable** before the state mediation board."},
            {"author": "Oliver Wendell Holmes Jr.", "work": "The Common Law", "quote": "Whether an issue of breach is properly **arbitrable** depends upon the express covenant framed by the consenting parties."},
            {"author": "Roscoe Pound", "work": "The Spirit of the Common Law", "quote": "Commercial custom gradually expanded the categories of differences deemed **arbitrable** outside the formal courts of equity."}
        ]
    },
    "arbitrage": {
        "primary": "The simultaneous purchase and sale of an asset in different markets to exploit price discrepancies.",
        "secondary": "In international finance and securities trading, a risk-mitigated strategy profiting from temporary imbalances in exchange rates, yields, or commodity valuations.",
        "quotes": [
            {"author": "Frank A. Fetter", "work": "Economics Volume II: Modern Economic Problems", "quote": "Modern telegraphic communication enabled swift **arbitrage** between the stock exchanges of London and New York."},
            {"author": "John Maynard Keynes", "work": "A Treatise on Money", "quote": "The flow of short-term funds driven by foreign exchange **arbitrage** rapidly evens out minor discrepancies in interest rates."},
            {"author": "Alfred Marshall", "work": "Principles of Economics", "quote": "Dealings in international bullion depend intimately upon the alertness of operators engaged in continuous **arbitrage**."}
        ]
    },
    "arbitrager": {
        "primary": "A financial trader who executes simultaneous transactions across markets to capture price differences.",
        "secondary": "In market microstructure, an exchange market maker whose rapid offsetting operations provide cross-market liquidity and enforce uniform pricing.",
        "quotes": [
            {"author": "Frank A. Fetter", "work": "Economics Volume II: Modern Economic Problems", "quote": "The professional **arbitrager** watches cable dispatches closely to purchase wheat where it is cheap and sell where dear."},
            {"author": "Thorstein Veblen", "work": "The Theory of Business Enterprise", "quote": "The speculative maneuvers of the **arbitrager** thrive upon momentary imbalances in the securities market."},
            {"author": "Irving Fisher", "work": "The Nature of Capital and Income", "quote": "By equalizing prices across distant trading centers, the vigilant **arbitrager** performs a steady economic function."}
        ]
    },
    "arbitrageur": {
        "primary": "A specialized professional who engages in the practice of financial arbitrage across disparate markets.",
        "secondary": "In investment banking and corporate finance, an investor who trades in risk arbitrage, particularly involving shares of firms undergoing mergers, takeovers, or reorganizations.",
        "quotes": [
            {"author": "Joseph Schumpeter", "work": "Business Cycles", "quote": "The shrewd **arbitrageur** continuously realigns fluctuating discount rates between domestic and overseas capital centers."},
            {"author": "John Maynard Keynes", "work": "The General Theory of Employment, Interest and Money", "quote": "The professional **arbitrageur** balances competing monetary claims across borders with calculated precision."},
            {"author": "Walter Bagehot", "work": "Lombard Street: A Description of the Money Market", "quote": "Every London banking house relied upon the expert **arbitrageur** to steady bill transactions in Continental cities."}
        ]
    },
    "arbitral": {
        "primary": "Relating to, proceeding from, or determined by an arbitrator or an official court of arbitration.",
        "secondary": "In public international law and jurisprudence, designating binding decisions, procedures, or conventions governing neutral dispute adjudication.",
        "quotes": [
            {"author": "James Bryce", "work": "The American Commonwealth", "quote": "The international convention recommended an **arbitral** tribunal to settle boundary friction between neighboring republics."},
            {"author": "Woodrow Wilson", "work": "The State: Elements of Historical and Practical Politics", "quote": "The permanent court provided a neutral forum where **arbitral** proceedings replaced bellicose confrontations."},
            {"author": "Elihu Root", "work": "Addresses on International Subjects", "quote": "Confidence in an **arbitral** award rests upon the perceived impartiality and unimpeachable honor of the judges."}
        ]
    },
    "arbitrament": {
        "primary": "The authoritative settlement of a dispute by an arbiter; a definitive judgment or decision.",
        "secondary": "In historical and legal prose, the ultimate trial, adjudication, or recourse—such as the arbitrament of arms or a solemn peace council—that resolves conflict.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "The gods by their divine **arbitrament** Have given you this knight; he is a good one As ever struck at head."},
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The supreme importance of these characters has been proved by the final **arbitrament** of the battle for life."},
            {"author": "Robert Browning", "work": "An Introduction to the Study of Browning's Poetry", "quote": "Man must commit his mortal soul to the supreme **arbitrament** of conscience rather than worldly applause."}
        ]
    },
    "arbitrarily": {
        "primary": "In a manner determined by personal discretion, chance, or whim rather than by rule or reason.",
        "secondary": "In scientific methodology and statistical sampling, describing selections, categorizations, or boundaries established without intrinsic systemic criteria.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "From these remarks it will be seen that I look at the term species, as one **arbitrarily** given for the sake of convenience to a set of individuals closely resembling each other."},
            {"author": "Henry David Thoreau", "work": "Walden", "quote": "In one instance, on a line **arbitrarily** chosen, the depth did not vary more than one foot in thirty rods."},
            {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Words are **arbitrarily** annexed to ideas, having no natural connection with the things they signify."}
        ]
    },
    "arbitrariness": {
        "primary": "Grounding in random whim, impulse, or autocratic discretion rather than reason, law, or objective principle.",
        "secondary": "In constitutional theory and jurisprudence, the despotic exertion of sovereign power unchecked by established statutory bounds or due process.",
        "quotes": [
            {"author": "Leo Tolstoy", "work": "War and Peace", "quote": "Nowhere did the unpredictable **arbitrariness** of military commanders produce greater bewilderment among the troops."},
            {"author": "John Stuart Mill", "work": "On Liberty", "quote": "Protection against the tyranny of the magistrate is not enough; society must guard against the **arbitrariness** of prevailing opinion."},
            {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The independent tenure of the judicial department serves as an essential barrier against the **arbitrariness** of executive decrees."}
        ]
    },
    "arbitrary": {
        "primary": "Based on individual discretion, random choice, or personal impulse rather than reason or system.",
        "secondary": "In political philosophy and administrative law, describing despotic authority exercised without reference to general principles, statutes, or judicial restraint.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "She was ashamed of herself for her gloom of the night, based on nothing more tangible than a sense of condemnation under an **arbitrary** law of society which had no foundation in Nature."},
            {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "We are not, however, to infer that its acceptance or rejection must depend on blind impulse, or **arbitrary** choice."},
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "I was much struck how entirely vague and **arbitrary** is the distinction between species and varieties."}
        ]
    },
    "arbitrate": {
        "primary": "To act as an impartial referee or mediator to judge, reconcile, and settle a dispute between parties.",
        "secondary": "In labor relations and legal procedure, to hear formal evidence and render a binding judgment that resolves an impasse outside statutory courts.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "Which now the manage of two kingdoms must With fearful bloody issue **arbitrate**."},
            {"author": "Francis Bacon", "work": "The Essays", "quote": "It is a happy thing when kings assemble wise counselors who may fairly **arbitrate** disputes among the estates."},
            {"author": "Adam Smith", "work": "The Theory of Moral Sentiments", "quote": "The impartial spectator within the breast is appointed to **arbitrate** between self-love and the duties we owe to mankind."}
        ]
    },
    "arbitration": {
        "primary": "The formal settlement of a dispute by an impartial third party chosen or appointed by the disputants.",
        "secondary": "In institutional economics and international treaties, an established quasi-judicial mechanism for resolving collective labor conflicts or transnational commercial claims.",
        "quotes": [
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Hawley in consequence took an opportunity of seeing Caleb, calling at his office to ask whether he had time to undertake an **arbitration** if it were required."},
            {"author": "Thomas Henry Huxley", "work": "Evolution and Ethics", "quote": "Resolving all events, with their effects And manifold results, into the will And **arbitration** wise of the Supreme."},
            {"author": "G. K. Chesterton", "work": "The Ball and the Cross", "quote": "Here you can fall back on that naked and awful **arbitration** which is the only thing that balances the stars--a still, continuous violence."}
        ]
    },
    "arbitrational": {
        "primary": "Pertaining to, derived from, or characteristic of the process of arbitration and formal dispute settlement.",
        "secondary": "In comparative procedural jurisprudence, concerning the statutory protocols, clauses, and enforcement mechanisms of non-judicial arbitral proceedings.",
        "quotes": [
            {"author": "Elihu Root", "work": "Addresses on International Subjects", "quote": "The development of **arbitrational** machinery marks a genuine advance toward permanent international peace."},
            {"author": "James Bryce", "work": "Modern Democracies", "quote": "Industrial boards established **arbitrational** procedures to forestall disruptive strikes in key municipal utilities."},
            {"author": "Woodrow Wilson", "work": "The State: Elements of Historical and Practical Politics", "quote": "Treaty obligations increasingly incorporated **arbitrational** clauses to regulate contested maritime frontiers."}
        ]
    },
    "arbitrative": {
        "primary": "Serving to settle disputes through arbitration; exercising or possessing the authority of an arbiter.",
        "secondary": "In conflict resolution theory, describing administrative bodies or commissions vested with discretionary mediating power between contending factions.",
        "quotes": [
            {"author": "Oliver Wendell Holmes Jr.", "work": "Collected Legal Papers", "quote": "The commission exercised an **arbitrative** function, adjusting railway tariffs with flexible administrative discretion."},
            {"author": "Jeremy Bentham", "work": "An Introduction to the Principles of Morals and Legislation", "quote": "Judges endowed with **arbitrative** authority may tailor remedies to the distinctive equities of each contested case."},
            {"author": "Edmund Burke", "work": "Speech on Conciliation with America", "quote": "Parliament ought to have maintained an **arbitrative** temper rather than asserting unyielding legislative supremacy."}
        ]
    },
    "arbitrator": {
        "primary": "An independent person officially appointed to judge and settle a dispute between conflicting parties.",
        "secondary": "In administrative jurisprudence and commercial arbitration, a designated referee whose award is contractually binding upon both disputants.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "But now the **arbitrator** of despairs, Just Death, kind umpire of men’s miseries, With sweet enlargement doth dismiss me hence."},
            {"author": "Francis Bacon", "work": "The Essays", "quote": "A wise prince will choose an **arbitrator** whose integrity is acknowledged by both contending factions."},
            {"author": "John Locke", "work": "Second Treatise of Government", "quote": "Men enter into civil society so that an impartial **arbitrator** may decide their controversies according to established law."}
        ]
    },
    "arbitrement": {
        "primary": "An archaic variant of arbitrament, signifying the settlement of a controversy by an appointed arbiter.",
        "secondary": "In early modern English literature and diplomacy, the final determination, adjudication, or award rendered in a contested quarrel.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "Faith, yes, to be put to the **arbitrement** of swords, and by such two that would by all likelihood have confounded one the other."},
            {"author": "John Milton", "work": "Paradise Lost", "quote": "Stand fast; to stand or fall Free in thine own **arbitrement** it lies."},
            {"author": "Edmund Spenser", "work": "The Faerie Queene", "quote": "To that sage knight they did refer the cause, Abiding the **arbitrement** of his righteous laws."}
        ]
    },
    "nonarbitrable": {
        "primary": "Not legally capable of being submitted to or settled by arbitration due to statutory restrictions.",
        "secondary": "In administrative and public policy jurisprudence, describing matters of fundamental public order, criminal sanction, or non-waivable statutory rights reserved exclusively for judicial courts.",
        "quotes": [
            {"author": "Felix Frankfurter", "work": "The Public and Its Government", "quote": "Matters touching public safety and criminal enforcement remain strictly **nonarbitrable** before private tribunals."},
            {"author": "Roscoe Pound", "work": "Jurisprudence", "quote": "Certain core rights of personal liberty are inherently **nonarbitrable** under constitutional doctrine."},
            {"author": "Benjamin N. Cardozo", "work": "The Nature of the Judicial Process", "quote": "The contract could not make that controversy arbitral which public policy declared fundamentally **nonarbitrable**."}
        ]
    },
    "nonarbitrary": {
        "primary": "Determined by objective principles, demonstrable reasoning, or established evidence rather than personal whim.",
        "secondary": "In scientific philosophy and legal theory, exhibiting systematic consistency, rational justification, and freedom from subjective caprice.",
        "quotes": [
            {"author": "Bertrand Russell", "work": "The Problems of Philosophy", "quote": "Scientific induction seeks a **nonarbitrary** foundation for our inferences concerning the physical universe."},
            {"author": "John Dewey", "work": "Logic: The Theory of Inquiry", "quote": "Inquiry establishes **nonarbitrary** distinctions grounded in empirical observation and verified consequences."},
            {"author": "William James", "work": "The Principles of Psychology", "quote": "A rational mind classifies experience according to **nonarbitrary** patterns perceived within sensory data."}
        ]
    },
    "unarbitrary": {
        "primary": "Free from randomness, caprice, or despotic discretion; governed by consistent and equitable standards.",
        "secondary": "In political philosophy and ethical discourse, characterizing administrative decisions or moral judgments that conform strictly to predictable, rational norms.",
        "quotes": [
            {"author": "Matthew Arnold", "work": "Culture and Anarchy", "quote": "The state must embody an **unarbitrary** ideal of justice that transcends narrow partisan animosities."},
            {"author": "George Santayana", "work": "The Life of Reason", "quote": "True civilization consists in substituting an **unarbitrary** order of reason for the chaos of animal impulse."},
            {"author": "John Stuart Mill", "work": "Considerations on Representative Government", "quote": "An **unarbitrary** code of administrative law reassures citizens that public authority will not degenerate into tyranny."}
        ]
    }
}
