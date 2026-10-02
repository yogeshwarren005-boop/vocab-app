import os, re

BASE_DIR = r"App database\Latin roots\Cluster Action\Dashboard — act"

refined_defs = {
    "interactivity.md": {
        "primary": "A two-way exchange between a user and a digital system, interface, or medium, where human input directly and dynamically alters the output in real time.",
        "secondary": "In media studies, game design, and cybernetics, interactivity distinguishes participatory environments—where audiences co-create the narrative or experience—from passive broadcast consumption like television or print."
    },
    "activeness.md": {
        "primary": "Lively physical motion, mental alertness, or continuous engagement in practical pursuits rather than passive repose.",
        "secondary": "In comparative linguistics and grammar, activeness denotes the syntactic property of an active voice construction where the grammatical subject performs the action of the verb."
    },
    "activity.md": {
        "primary": "Energetic physical or mental movement, or an organized pursuit undertaken by individuals or institutions to achieve an aim.",
        "secondary": "In thermodynamics and physical chemistry, activity is the effective concentration of a chemical species in a non-ideal solution, accounting for molecular interactions that alter its real chemical potential."
    },
    "actualisation.md": {
        "primary": "The full realization or manifestation of latent capabilities, potential, or ideals into concrete, observable reality.",
        "secondary": "In humanistic psychology (Abraham Maslow, Carl Rogers), self-actualisation represents the highest drive of human development, striving toward the complete fulfillment of personal talent, creative expression, and authentic purpose."
    },
    "actualization.md": {
        "primary": "The full realization or manifestation of latent capabilities, potential, or ideals into concrete, observable reality.",
        "secondary": "In humanistic psychology (Abraham Maslow, Carl Rogers), self-actualization represents the highest drive of human development, striving toward the complete fulfillment of personal talent, creative expression, and authentic purpose."
    },
    "actuality.md": {
        "primary": "Concrete, observable factual existence as distinguished from theory, conjecture, possibility, or wishful imagination.",
        "secondary": "In Aristotelian metaphysics, actuality (entelecheia) designates the realized state of an entity that has achieved its inherent form, contrasted with mere potentiality (dynamis)."
    },
    "actuation.md": {
        "primary": "The mechanical, electrical, or hydraulic triggering of a mechanism, valve, or device into physical motion or operational performance.",
        "secondary": "In robotics and control systems engineering, actuation transforms control signals into physical force through servomotors, solenoids, or pneumatic cylinders."
    },
    "deactivation.md": {
        "primary": "The deliberate disabling, dismantling, or neutralization of an explosive, weapon system, electronic account, or military unit to render it safely inoperative.",
        "secondary": "In biochemistry and enzymatic kinetics, deactivation occurs when conformational changes, temperature denaturation, or chemical inhibitors abolish the catalytic competency of an enzyme."
    },
    "exaction.md": {
        "primary": "The compulsory extraction or extortion of money, labor, fees, or compliance through the harsh abuse of authoritative power.",
        "secondary": "In fiscal history and political economy, an exaction is an arbitrary levy or tribute imposed by a ruler outside established constitutional and statutory law."
    },
    "exactitude.md": {
        "primary": "Strict adherence to precision, mathematical accuracy, and rigorous standards of correctness that leaves no margin for error or approximation.",
        "secondary": "In scientific methodology and measurement theory, exactitude distinguishes quantitative empirical results from mere qualitative estimation."
    },
    "inactivation.md": {
        "primary": "The permanent or temporary neutralization of a virus, toxin, chemical reagent, or metabolic pathway, eliminating its biological or chemical efficacy.",
        "secondary": "In molecular genetics and epigenetics, X-chromosome inactivation (lyonization) silences one of the two X chromosomes in female mammalian somatic cells to equalize gene dosage with males."
    },
    "inactiveness.md": {
        "primary": "A period or disposition of quiet dormancy, disuse, or suspended exertion, characterized by the absence of energetic motion or productivity.",
        "secondary": "In behavioral ecology and physiology, inactiveness represents an adaptive energy-conservation strategy (such as torpor or midday resting) deployed in response to thermal stress or food scarcity."
    },
    "inexactitude.md": {
        "primary": "An error, deviation, or approximation that fails to match the true fact, calculated measurement, or precise specification.",
        "secondary": "In historical rhetoric, Winston Churchill famously coined the euphemism 'terminological inexactitude' in the House of Commons as a parliamentary periphrasis for a falsehood or untruth."
    },
    "inexactness.md": {
        "primary": "A lack of strict precision, sharpness, or fidelity in speech, measurement, or calculation, leaving margins of uncertainty or vagueness.",
        "secondary": "In the philosophy of science, inexactness characterizes phenomenological laws and heuristic models that capture broad qualitative regularities without achieving mathematical rigor."
    },
    "reenactment.md": {
        "primary": "The theatrical, ceremonial, or educational restaging of a historical battle, trial, or cultural event by participants wearing authentic period attire.",
        "secondary": "In legal jurisprudence and statutory interpretation, the reenactment canon dictates that when a legislature re-adopts existing statutory language without alteration, it implicitly adopts settled judicial interpretations of that text."
    }
}

updated = 0
for fname, defs in refined_defs.items():
    fpath = os.path.join(BASE_DIR, fname)
    if not os.path.exists(fpath):
        print(f"Warning: {fpath} not found")
        continue
    
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
        
    p_def = defs["primary"].strip().rstrip(".") + "."
    s_def = defs["secondary"].strip().rstrip(".") + "."
    
    # Replace primary definition line
    content = re.sub(
        r'1\.\s*\*\*Primary Definition[^*]*\*\*:\s*[^\r\n]+',
        f'1. **Primary Definition (Lexical / Standard Consensus)**: {p_def}',
        content
    )
    # Replace secondary definition line
    content = re.sub(
        r'2\.\s*\*\*Secondary[^*]*\*\*:\s*[^\r\n]+',
        f'2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: {s_def}',
        content
    )
    
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)
    updated += 1
    print(f"Refined: {fname}")

print(f"\nSuccessfully refined {updated} word notes with non-formulaic substantive definitions.")
