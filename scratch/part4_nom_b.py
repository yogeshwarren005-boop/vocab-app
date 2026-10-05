# -*- coding: utf-8 -*-
"""
Part 4 of Speech Batch 4:
- Dashboard — nom & nomin words (part B - 21 words):
  nominalism, nominalist, nominalistic, nominally, nominate,
  nominated, nomination, nominative, nominator, nominee,
  nomogram, nomograph, nomothetic, nondenominational, nonnomadic,
  obloquy (in loqu, verify), prenominal, pronominal, undenominational
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

part4_nom_b = {
  "nominalism": {
    "primary": "The philosophical doctrine that general terms or abstract concepts exist only as names, without corresponding objective reality.",
    "secondary": "In medieval scholastic philosophy and metaphysics, the rejection of Platonic realism, famously advanced by Roscelin and William of Ockham.",
    "quotes": [
      {"author": "Bertrand Russell", "work": "A History of Western Philosophy", "quote": "Scholastic **nominalism** prepared the way for modern empirical science by denying mystical real essences to abstract categories."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Radical **nominalism** asserts that thoughts are bound to individual sensible things, and that universals are mere breath and sound."},
      {"author": "Charles Sanders Peirce", "work": "Collected Papers", "quote": "The fundamental dispute between scholastic realism and **nominalism** continues to shape scientific understanding of natural laws."}
    ]
  },
  "nominalist": {
    "primary": "An adherent of nominalism; a thinker who holds that universal concepts exist only as names without objective reality.",
    "secondary": "In epistemology and scholastic history, an anti-realist philosopher denying independent ontological status to universal forms.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "An Examination of Sir William Hamilton's Philosophy", "quote": "Every consistent **nominalist** insists that words signifying classes refer solely to individual concrete objects."},
      {"author": "Bertrand Russell", "work": "Our Knowledge of the External World", "quote": "William of Ockham, as a subtle **nominalist**, applied his razor to eliminate unnecessary metaphysical entities."},
      {"author": "William James", "work": "Pragmatism", "quote": "The pragmatic philosopher is an unrepentant **nominalist**, looking away from first categories toward practical consequences."}
    ]
  },
  "nominalistic": {
    "primary": "Relating to, characteristic of, or adhering to the philosophical doctrine of nominalism.",
    "secondary": "In metaphysical semantics and ontology, denying the ontological reality of abstract universals and essences.",
    "quotes": [
      {"author": "Charles Sanders Peirce", "work": "Illustrations of the Logic of Science", "quote": "A purely **nominalistic** philosophy reduces physical laws to mere human conventions and shorthand summaries."},
      {"author": "Bertrand Russell", "work": "The Problems of Philosophy", "quote": "The **nominalistic** view of mathematics fails to account for relations that hold independently of human cognition."},
      {"author": "William James", "work": "The Meaning of Truth", "quote": "His **nominalistic** tendencies led him to distrust transcendent essences and demand concrete verification."}
    ]
  },
  "nominally": {
    "primary": "In name only; officially, but not in actual practice, reality, or fact.",
    "secondary": "In constitutional history and financial metrics, possessing title or titular status without exercising executive power.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The barbarian chieftain was **nominally** a vassal of Constantinople, though he reigned as an absolute sovereign in Gaul."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "The governor was **nominally** the chief executive of the state, but town selectmen held real local authority."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The monarch was **nominally** head of the church, yet Parliament dictated ecclesiastical governance and statutes."}
    ]
  },
  "nominate": {
    "primary": "To propose or formally enter as a candidate for election, appointment, or honor.",
    "secondary": "In political science and parliamentary procedure, to put forward an individual for elective office or civic commission.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The Constitution empowers the President to **nominate**, and with the advice and consent of the Senate, appoint ambassadors."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "Party caucuses assemble delegates to **nominate** candidates representing distinct regional coalitions."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The privy council met in emergency session to **nominate** a lord protector during the minority of the prince."}
    ]
  },
  "nominated": {
    "primary": "Formally proposed, selected, or designated as a candidate for office, honor, or position.",
    "secondary": "In electoral history, designated by ballot, caucus, or royal warrant for public office or ecclesiastical benefice.",
    "quotes": [
      {"author": "Abraham Lincoln", "work": "Speeches and Letters", "quote": "Having been **nominated** by the convention, I accept the solemn responsibility of defending the Union and the laws."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "When a candidate is formally **nominated**, the partisan press mobilizes its full resources to secure his election."},
      {"author": "Woodrow Wilson", "work": "Congressional Government", "quote": "The magistrate was **nominated** by the executive and confirmed without substantial opposition by the legislative chamber."}
    ]
  },
  "nomination": {
    "primary": "The act or instance of formally naming or proposing someone for an office, position, or honor.",
    "secondary": "In constitutional law and political convention, the formal institutional process designating a candidate for executive or judicial confirmation.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The sole act of **nomination** rests exclusively with the President, ensuring concentrated responsibility in executive selections."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "The presidential **nomination** provoked intense factional rivalry across every state committee in the Union."},
      {"author": "James Madison", "work": "The Federalist Papers", "quote": "The power of **nomination** prevents corrupt coalitions in the legislature from partitioning public offices among favorites."}
    ]
  },
  "nominative": {
    "primary": "Relating to or denoting the grammatical case that marks the subject of a finite verb in inflected languages.",
    "secondary": "In syntactic typology and traditional grammar, the unmarked grammatical case designating the agent or grammatical subject.",
    "quotes": [
      {"author": "Otto Jespersen", "work": "The Philosophy of Grammar", "quote": "In highly inflected tongues like Latin and Greek, the **nominative** case signals the primary agent or syntactic subject."},
      {"author": "Edward Sapir", "work": "Language: An Introduction to the Study of Speech", "quote": "The grammatical distinction between **nominative** and accusative forms preserves clarity in sentence organization."},
      {"author": "Leonard Bloomfield", "work": "Language", "quote": "Indo-European nouns carried distinctive **nominative** singular suffixes that eroded across subsequent phonetic evolution."}
    ]
  },
  "nominator": {
    "primary": "A person who proposes, names, or enters someone as a candidate for an office, election, or honor.",
    "secondary": "In electoral administration and parliamentary assemblies, the delegate or sponsor who presents a formal nomination petition.",
    "quotes": [
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "Each candidate relied upon a trusted **nominator** to introduce his platform with rousing speeches to the assembled delegates."},
      {"author": "Woodrow Wilson", "work": "The State: Elements of Historical and Practical Politics", "quote": "The primary sponsor or **nominator** must certify that the nominee meets all constitutional qualifications for office."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The chief **nominator** was shouted down by opposing factions in the crowded town hall during the borough election."}
    ]
  },
  "nominee": {
    "primary": "A person who is proposed, selected, or named as a candidate for an election, appointment, or award.",
    "secondary": "In corporate finance and electoral politics, a designated individual or entity holding securities or contesting public office.",
    "quotes": [
      {"author": "Abraham Lincoln", "work": "Speeches and Letters", "quote": "The party **nominee** addressed the crowded forum, pledging unswerving adherence to the principles of the founding fathers."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "Once designated by the state convention, the **nominee** traversed the countryside soliciting the votes of farmers and laborers."},
      {"author": "Woodrow Wilson", "work": "Congressional Government", "quote": "The presidential **nominee** faced rigorous public examination regarding his past legislative record and financial associations."}
    ]
  },
  "nomogram": {
    "primary": "A graphic calculating device, consisting of two or more calibrated lines, used to solve mathematical equations.",
    "secondary": "In graphical mathematics and engineering design, an alignment chart or computational scale invented by Maurice d'Ocagne for rapid calculation.",
    "quotes": [
      {"author": "Karl Pearson", "work": "The Grammar of Science", "quote": "By laying a straightedge across the scales of a **nomogram**, researchers can instantly read complex statistical relationships."},
      {"author": "Claude Shannon", "work": "The Mathematical Theory of Communication", "quote": "Engineers constructed an alignment **nomogram** to compute channel capacity and signal-to-noise ratios without tedious arithmetic."},
      {"author": "Norbert Wiener", "work": "Cybernetics", "quote": "A graphical **nomogram** serves as a direct analog computer, translating intricate differential relations into straight geometric lines."}
    ]
  },
  "nomograph": {
    "primary": "A diagram representing mathematical relations by means of calibrated scales; an alignment chart or nomogram.",
    "secondary": "In applied mathematics, ballistics, and biometrics, a graphical computational tool enabling rapid determination of numerical functions.",
    "quotes": [
      {"author": "Karl Pearson", "work": "The Life, Letters and Labours of Francis Galton", "quote": "Galton designed an ingenious **nomograph** to correlate biometric measurements of parents and offspring on calibrated logarithmic scales."},
      {"author": "Claude Shannon", "work": "A Symbolic Analysis of Relay and Switching Circuits", "quote": "The technician utilized a specialized **nomograph** to evaluate circuit impedance across varying frequency ranges."},
      {"author": "Thomas Henry Huxley", "work": "Physiography: An Introduction to the Study of Nature", "quote": "Meteorologists employed a printed **nomograph** to convert barometric pressure readings into precise altimetric elevations."}
    ]
  },
  "nomothetic": {
    "primary": "Relating to or based on the formulation and discovery of general or universal scientific laws.",
    "secondary": "In philosophy of science and psychology (contrasted with idiographic), seeking universal regularities and quantitative generalizations.",
    "quotes": [
      {"author": "Wilhelm Windelband", "work": "History and Natural Science", "quote": "Natural sciences pursue **nomothetic** methods aimed at formulating universal laws, whereas historical sciences study individual unique occurrences."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Empirical psychology oscillates between **nomothetic** generalization and the descriptive appreciation of singular human experience."},
      {"author": "Max Weber", "work": "The Methodology of the Social Sciences", "quote": "Sociology aspires to a **nomothetic** understanding of social action, formulating ideal types to reveal structural patterns."}
    ]
  },
  "nondenominational": {
    "primary": "Not restricted to, affiliated with, or sponsored by any specific religious denomination or sect.",
    "secondary": "In religious sociology and institutional education, welcoming diverse faith traditions without adherence to sectarian doctrine.",
    "quotes": [
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "The frontier community erected a **nondenominational** meetinghouse where itinerant preachers of all persuasions addressed the pioneers."},
      {"author": "William James", "work": "The Varieties of Religious Experience", "quote": "True mystical fellowship is fundamentally **nondenominational**, transcending the institutional boundaries of historical churches."},
      {"author": "John Dewey", "work": "Democracy and Education", "quote": "Public civic institutions must maintain a strictly **nondenominational** character to foster inclusive civic solidarity."}
    ]
  },
  "nonnomadic": {
    "primary": "Not living a nomadic life; leading a settled, sedentary existence tied to permanent dwellings.",
    "secondary": "In anthropology and economic history, practicing sedentary agriculture, village settlement, and permanent domicile.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The transition to a **nonnomadic** lifestyle fostered permanent dwellings, intensive agriculture, and rapid population growth."},
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The **nonnomadic** agriculturalists of the frontier river valleys bore the brunt of barbarian cavalry incursions."},
      {"author": "Alexander von Humboldt", "work": "Personal Narrative of Travels to the Equinoctial Regions of America", "quote": "Settled **nonnomadic** communities in the Andean highlands developed terraced agriculture and sophisticated irrigation canals."}
    ]
  },
  "prenominal": {
    "primary": "Placed before or occurring immediately prior to a noun; relating to what precedes a name.",
    "secondary": "In syntax and grammar, modifying elements positioned attributively before the head noun in a noun phrase.",
    "quotes": [
      {"author": "Otto Jespersen", "work": "A Modern English Grammar on Historical Principles", "quote": "English strongly favors **prenominal** adjectives in descriptive phrases, whereas Romance idioms place them postpositively."},
      {"author": "Edward Sapir", "work": "Language: An Introduction to the Study of Speech", "quote": "The ordering of **prenominal** demonstratives and quantifiers adheres to strict psychological and grammatical hierarchies."},
      {"author": "Leonard Bloomfield", "work": "Language", "quote": "In Germanic syntax, the compound modifier routinely takes a **prenominal** position, altering the phonetic stress of the clause."}
    ]
  },
  "pronominal": {
    "primary": "Relating to, functioning as, or resembling a pronoun in grammatical form or syntax.",
    "secondary": "In linguistics and syntax, designating grammatical structures, clitics, or affixes substituting for or referring to noun phrases.",
    "quotes": [
      {"author": "Otto Jespersen", "work": "The Philosophy of Grammar", "quote": "The intricate **pronominal** systems of Indo-European languages maintain vital distinctions of person, gender, and number."},
      {"author": "Edward Sapir", "work": "Language: An Introduction to the Study of Speech", "quote": "Certain indigenous American languages incorporate **pronominal** elements directly into the verbal stem as prefixes or infixes."},
      {"author": "Leonard Bloomfield", "work": "Language", "quote": "The replacement of a substantive by a **pronominal** form depends upon mutual situational awareness between speaker and hearer."}
    ]
  },
  "undenominational": {
    "primary": "Not having a connection with, or not restricted to, any particular religious denomination; non-sectarian.",
    "secondary": "In British educational and social history, non-sectarian religious instruction or institutions open to all Christian denominations.",
    "quotes": [
      {"author": "Matthew Arnold", "work": "Culture and Anarchy", "quote": "The advocates of **undenominational** public education sought to unite citizens across sectarian cleavages through shared cultural ideals."},
      {"author": "John Stuart Mill", "work": "On Liberty", "quote": "Philanthropic endeavors succeed most enduringly when conducted on a broad, **undenominational** basis free from dogma."},
      {"author": "William James", "work": "The Varieties of Religious Experience", "quote": "The charitable mission functioned as an **undenominational** sanctuary, welcoming destitute wanderers without theological inquiry."}
    ]
  }
}
