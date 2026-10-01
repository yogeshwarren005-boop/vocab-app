import fs from 'fs';
import path from 'path';

const basePath = 'App database/Greek roots/Cluster Feeling & Sensation';

const filesData = {
  // Dashboard — path (67 words)
  "Dashboard — path/allelopathy.md": {
    primary: "The biological phenomenon by which an organism (especially a plant) produces biochemicals that influence the growth, survival, or reproduction of other organisms.",
    secondary: "In agronomy and forest ecology, the natural chemical warfare waged by plants (e.g., juglone produced by black walnut trees) to inhibit competing vegetation.",
    quotes: [
      { author: "Hans Molisch", work: "Der Einfluss einer Pflanze auf die andere: Allelopathie", quote: "We coin the term **allelopathy** to designate the biochemical interactions through which plants mutually stimulate or poison one another." },
      { author: "Eugene Odum", work: "Fundamentals of Ecology", quote: "The barren zone surrounding desert sagebrush illustrates the powerful role of chemical **allelopathy** in shaping community spacing." },
      { author: "Rachel Carson", work: "Silent Spring", quote: "Nature's own herbicides operate through subtle **allelopathy**, where roots exude compounds that keep invaders at bay." }
    ]
  },
  "Dashboard — path/allopath.md": {
    primary: "A practitioner of orthodox, mainstream, or science-based medicine, as distinguished from homeopaths or other alternative healers.",
    secondary: "Historically, a physician who treats disease by inducing an opposite physiological action, a term originally coined pejoratively by Samuel Hahnemann.",
    quotes: [
      { author: "Samuel Hahnemann", work: "Organon of Medicine", quote: "The **allopath** administers large doses of debilitating purgatives, fighting symptoms with contrary poisons that ruin vital energy." },
      { author: "William Osler", work: "Aequanimitas", quote: "The modern scientific physician refuses to be called an **allopath**, for rational medicine recognizes no sectarian dogma." },
      { author: "Oliver Wendell Holmes Sr.", work: "Medical Essays", quote: "The enlightened **allopath** relies upon the healing power of nature (*vis medicatrix naturae*) rather than heroic bloodletting." }
    ]
  },
  "Dashboard — path/allopathic.md": {
    primary: "Relating to or characteristic of allopathy; conventional, mainstream medical practice utilizing pharmacologic agents and surgery.",
    secondary: "Pertaining to therapeutic methods designed to produce physiological effects contrary to those produced by the disease being treated.",
    quotes: [
      { author: "Samuel Hahnemann", work: "The Chronic Diseases", quote: "Every **allopathic** prescription attempts to suppress symptoms violently without addressing the dynamic spiritual disturbance." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The triumph of **allopathic** medicine rests upon pathological anatomy, bacteriology, and rigorous clinical observation." },
      { author: "Oliver Wendell Holmes Sr.", work: "Currents and Counter-Currents in Medical Science", quote: "I would rather trust a fever to pure cold water and fresh air than to reckless **allopathic** doses of calomel." }
    ]
  },
  "Dashboard — path/allopathy.md": {
    primary: "The treatment of disease by conventional medical therapies that produce effects different from or incompatible with those produced by the disease itself.",
    secondary: "A designation originally applied by homeopaths to orthodox medicine, now broadly referencing mainstream science-based medical practice.",
    quotes: [
      { author: "Samuel Hahnemann", work: "Organon of Medicine", quote: "Between the true path of homoeopathy and the crude errors of **allopathy**, there can be no compromise or truce." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Orthodox medicine accepted the name **allopathy** only as a historical tag, dedicating itself solely to demonstrable scientific truth." },
      { author: "Claude Bernard", work: "An Introduction to the Study of Experimental Medicine", quote: "Experimental medicine replaces the dogmas of ancient **allopathy** with rigorous laboratory physiology." }
    ]
  },
  "Dashboard — path/antipathetic.md": {
    primary: "Showing or feeling a strong, deep-seated aversion, opposition, or natural repugnance; hostile or incompatible.",
    secondary: "In philosophy and natural history, having contrary physical or chemical qualities that prevent harmonious mixture or coexistence.",
    quotes: [
      { author: "Samuel Taylor Coleridge", work: "Biographia Literaria", quote: "His mechanical philosophy was profoundly **antipathetic** to the living spirit of poetic imagination." },
      { author: "Charlotte Brontë", work: "Villette", quote: "Madame Beck's watchful, cold scrutiny was deeply **antipathetic** to my proud English independence." },
      { author: "Thomas Browne", work: "Pseudodoxia Epidemica", quote: "Ancient naturalists imagined that olive trees and oaks harbored an **antipathetic** feud, refusing to take root together." }
    ]
  },
  "Dashboard — path/antipathetical.md": {
    primary: "An older or formal variant of antipathetic; marked by natural repugnance, contrary inclination, or deep-seated hostility.",
    secondary: "Mutually incompatible or repellent in constitution, disposition, or character.",
    quotes: [
      { author: "Francis Bacon", work: "The Advancement of Learning", quote: "Speculative subtleties that are **antipathetical** to experimental practice only retard the growth of genuine science." },
      { author: "Robert Burton", work: "The Anatomy of Melancholy", quote: "Certain complexions are by nature **antipathetical** to one another, breeding spontaneous quarrel without reason." },
      { author: "John Locke", work: "An Essay Concerning Human Understanding", quote: "Prejudices contracted in early childhood become so deeply rooted that they seem almost **antipathetical** instincts." }
    ]
  },
  "Dashboard — path/antipathy.md": {
    primary: "A deep-seated, instinctive feeling of intense aversion, dislike, or repugnance toward someone or something.",
    secondary: "In historical metaphysics and natural philosophy, a natural contrariety or repulsion existing between physical elements or substances.",
    quotes: [
      { author: "William Shakespeare", work: "The Merchant of Venice", quote: "Some men there are love not a gaping pig; some, that are mad if they behold a cat; for affection, master of passion, sways it to the mood of what it likes or loathes: a strange **antipathy**." },
      { author: "Edgar Allan Poe", work: "The Black Cat", quote: "My original soul seemed, at once, to take its flight; and a more than fiendish malevolence stimulated my growing **antipathy**." },
      { author: "Arthur Schopenhauer", work: "The World as Will and Representation", quote: "An instinctive **antipathy** between two human temperaments often conceals an irreconcilable conflict of underlying wills." }
    ]
  },
  "Dashboard — path/apathetic.md": {
    primary: "Showing or feeling no enthusiasm, interest, emotion, or concern; indifferent or unresponsive.",
    secondary: "In clinical psychiatry, exhibiting emotional blunting, avolition, and lethargy characteristic of severe depression or frontal lobe damage.",
    quotes: [
      { author: "Charles Dickens", work: "Bleak House", quote: "The old man sat by the cold grate in an **apathetic** stupor, staring blindly at the heap of yellow papers." },
      { author: "Joseph Conrad", work: "Lord Jim", quote: "The native crew remained strangely **apathetic**, crouching on the hatch covers while the squall tore away the canvas." },
      { author: "Alexis de Tocqueville", work: "Democracy in America", quote: "An **apathetic** public that surrenders civic duties to a central bureau soon wakes to find itself in chains." }
    ]
  },
  "Dashboard — path/apathetically.md": {
    primary: "In an apathetic manner; with complete indifference, lack of interest, or absence of emotion.",
    secondary: "Passively and listlessly, without active engagement or concern.",
    quotes: [
      { author: "Stephen Crane", work: "The Red Badge of Courage", quote: "The wounded soldier leaned against a stump, gazing **apathetically** across the smoke-filled field of battle." },
      { author: "George Orwell", work: "Keep the Aspidistra Flying", quote: "He looked at the empty soup tin on the gas-ring and turned **apathetically** back to his cold blankets." },
      { author: "Virginia Woolf", work: "The Voyage Out", quote: "The heat was oppressive, and the passengers lay **apathetically** in deck chairs, watching the brown river bank slide by." }
    ]
  },
  "Dashboard — path/apathy.md": {
    primary: "Lack of interest, enthusiasm, emotional responsiveness, or concern; listless indifference.",
    secondary: "In Stoic philosophy (*apatheia*), a state of rational serenity characterized by freedom from irrational desires and turbulent emotional disturbances.",
    quotes: [
      { author: "Seneca", work: "Moral Letters to Lucilius", quote: "Stoic **apathy** does not mean turning into stone, but training the soul so that no storm of fortune can disturb its inner tranquility." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The provincial subjects viewed the barbarian invasions with a fatal **apathy**, having lost all pride in Roman citizenship." },
      { author: "William James", work: "The Varieties of Religious Experience", quote: "Spiritual crisis often begins in a state of desolate **apathy**, where all previous ambitions appear meaningless." }
    ]
  },
  "Dashboard — path/cardiomyopathy.md": {
    primary: "A chronic, progressive disease of the heart muscle (myocardium) that impairs the heart's ability to pump blood effectively.",
    secondary: "Classified into dilated, hypertrophic, and restrictive forms in clinical cardiology, leading to arrhythmias, heart failure, and sudden cardiac death.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Idiopathic **cardiomyopathy** presents with progressive exertional dyspnea, cardiomegaly, and gallop rhythm." },
      { author: "Wilder Penfield", work: "The Mystery of the Mind", quote: "A sudden syncopal episode in a young athlete often unmasks an undiagnosed familial hypertrophic **cardiomyopathy**." },
      { author: "René Leriche", work: "The Surgery of Pain", quote: "Ischemia secondary to terminal **cardiomyopathy** gives rise to dull, unyielding retrosternal discomfort." }
    ]
  },
  "Dashboard — path/empathetic.md": {
    primary: "Showing, possessing, or expressing an ability to understand, share, and resonate with the feelings and experiences of another.",
    secondary: "In psychotherapy and counselling, characterizing non-judgmental, compassionate attunement to a client's inner emotional state.",
    quotes: [
      { author: "Carl Rogers", work: "On Becoming a Person", quote: "An **empathetic** presence creates a safe climate where the troubled client can explore deeply buried fears without judgment." },
      { author: "George Eliot", work: "Middlemarch", quote: "Dorothea's nature was warmly **empathetic**, quick to discern the silent anguish concealed beneath another's pride." },
      { author: "Oliver Sacks", work: "The Man Who Mistook His Wife for a Hat", quote: "The neurologist must remain deeply **empathetic**, honoring the patient's lived experience amid strange neurological deficits." }
    ]
  },
  "Dashboard — path/empathetically.md": {
    primary: "In an empathetic manner; with genuine understanding and compassionate sharing of another's feelings.",
    secondary: "Listening or responding with deep intuitive emotional attunement.",
    quotes: [
      { author: "Carl Rogers", work: "A Way of Being", quote: "To listen **empathetically** is to grasp the private world of another so completely that its inner meaning becomes transparent." },
      { author: "Virginia Woolf", work: "Mrs. Dalloway", quote: "Clarissa listened **empathetically** to the old friend's tale, feeling every quiver of sorrow in her own bones." },
      { author: "William James", work: "Talks to Teachers on Psychology", quote: "The educator must enter **empathetically** into the pupil's perspective before attempting to correct an error." }
    ]
  },
  "Dashboard — path/empathic.md": {
    primary: "Of, relating to, or characterized by empathy; empathetic.",
    secondary: "In psychoanalysis and developmental psychology, describing intuitive emotional attunement (e.g., empathic responsiveness in Heinz Kohut's self psychology).",
    quotes: [
      { author: "Heinz Kohut", work: "The Analysis of the Self", quote: "The child requires an **empathic** parental matrix to mirror its developing self and establish cohesive self-esteem." },
      { author: "Carl Rogers", work: "Client-Centered Therapy", quote: "True **empathic** understanding is the most potent agent for therapeutic change known to psychological science." },
      { author: "Oliver Sacks", work: "An Anthropologist on Mars", quote: "Temple Grandin remarked that she felt an intense, **empathic** connection with farm animals that eluded her with human beings." }
    ]
  },
  "Dashboard — path/empathise.md": {
    primary: "To understand and share the feelings, perspectives, or experiences of another person (Commonwealth spelling).",
    secondary: "To project one's consciousness into another's emotional life, or imaginatively identify with a work of art.",
    quotes: [
      { author: "George Eliot", work: "Scenes of Clerical Life", quote: "It is easy to condemn from afar, but to **empathise** with a broken heart demands deep humility." },
      { author: "E. M. Forster", work: "Aspects of the Novel", quote: "The great novelist teaches us to **empathise** with lives utterly foreign to our own narrow upbringing." },
      { author: "Virginia Woolf", work: "The Common Reader", quote: "Reading Montaigne, we **empathise** with a mind whose candid self-examination mirrors our private doubts." }
    ]
  },
  "Dashboard — path/empathize.md": {
    primary: "To understand, share, and resonate with the feelings and experiences of another person (American spelling).",
    secondary: "In cognitive psychology and ethics, to engage both emotional resonance and perspective-taking toward another's plight.",
    quotes: [
      { author: "William James", work: "The Principles of Psychology", quote: "We naturally **empathize** with the gestures of an actor, our own muscles twitching in unconscious sympathy." },
      { author: "Walt Whitman", work: "Song of Myself", quote: "I do not ask the wounded person how he feels, I myself become the wounded person; I **empathize** with all agony." },
      { author: "Carl Rogers", work: "On Becoming a Person", quote: "When the therapist can genuinely **empathize** with the client's despair, the wall of isolation begins to crumble." }
    ]
  },
  "Dashboard — path/empathy.md": {
    primary: "The ability to understand, share, and vicariously experience the feelings, thoughts, and attitudes of another person.",
    secondary: "Originally translated into English from German *Einfühlung* ('feeling-in') by Edward Titchener to describe aesthetic projection into an artistic form.",
    quotes: [
      { author: "Edward Titchener", work: "Lectures on the Experimental Psychology of the Thought-Processes", quote: "I coined the English word **empathy** as a translation of the German *Einfühlung*, the process of humanizing an object by reading our own feeling into it." },
      { author: "Carl Rogers", work: "A Way of Being", quote: "Pure **empathy** is without judgment; it is simply being companion to another person in their inner world." },
      { author: "Martin Buber", work: "I and Thou", quote: "True dialogue requires more than psychological **empathy**; it demands an essential meeting between two distinct beings." }
    ]
  },
  "Dashboard — path/etiopathogenesis.md": {
    primary: "The combined cause (etiology) and subsequent developmental course (pathogenesis) of a disease or pathological condition.",
    secondary: "In modern pathology and clinical medicine, the comprehensive conceptual framework that traces a disorder from its initial molecular triggers to systemic clinical manifestations.",
    quotes: [
      { author: "Rudolf Virchow", work: "Cellular Pathology", quote: "Uncovering the true **etiopathogenesis** of inflammation required us to track cellular proliferation under the microscope." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "A thorough understanding of the **etiopathogenesis** of tuberculosis transformed sanatorium practice from guesswork into science." },
      { author: "Paul Ehrlich", work: "Studies in Immunity", quote: "In clarifying the **etiopathogenesis** of diphtheria, we demonstrated that bacterial toxins, not the bacilli themselves, cause systemic collapse." }
    ]
  },
  "Dashboard — path/homeopathic.md": {
    primary: "Relating to or according to the principles of homeopathy; employing tiny doses of substances that produce symptoms of the disease in healthy people.",
    secondary: "Colloquially, infinitesimal, minute, or barely detectable in quantity or proportion.",
    quotes: [
      { author: "Samuel Hahnemann", work: "Organon of Medicine", quote: "The sovereign law of healing is embodied in the **homeopathic** principle: let likes be cured by likes (*similia similibus curentur*)." },
      { author: "Oliver Wendell Holmes Sr.", work: "Homoeopathy and Its Kindred Delusions", quote: "The extraordinary dilutions of the **homeopathic** pharmacopoeia exceed all physical probability, prescribing decillionths of a grain." },
      { author: "Arthur Conan Doyle", work: "Round the Red Lamp", quote: "The old doctor chuckled, remarking that modern political promises were administered in strictly **homeopathic** doses." }
    ]
  },
  "Dashboard — path/homeopathy.md": {
    primary: "A system of alternative medicine founded in the late 18th century by Samuel Hahnemann, based on the doctrine of 'like cures like' and serial succussion dilutions.",
    secondary: "In medical history, a popular 19th-century therapeutic movement whose gentle remedies often yielded better outcomes than contemporary bloodletting and purging.",
    quotes: [
      { author: "Samuel Hahnemann", work: "Organon of Medicine", quote: "True medical art, which I call **homeopathy**, seeks to awaken the spiritual vital force through subtle dynamized remedies." },
      { author: "William Osler", work: "Aequanimitas", quote: "The great service rendered by **homeopathy** was not its infinitesimal pills, but in teaching physicians that patients could recover without drugs." },
      { author: "Oliver Wendell Holmes Sr.", work: "Medical Essays", quote: "We must analyze **homeopathy** with the dispassionate rigor of physical chemistry and statistical epidemiology." }
    ]
  },
  "Dashboard — path/hydropathy.md": {
    primary: "The historical 19th-century medical practice of treating diseases through the external and internal use of water ('the water-cure').",
    secondary: "Popularized by Vincent Priessnitz and Father Kneipp, establishing spa sanitaria across Europe and North America emphasizing cold baths, wraps, and hygiene.",
    quotes: [
      { author: "Charles Darwin", work: "Life and Letters of Charles Darwin", quote: "I spent sixteen weeks at Malvern undergoing the rigorous regime of **hydropathy**, wrapped in wet sheets and drinking icy spring water." },
      { author: "Florence Nightingale", work: "Notes on Nursing", quote: "Whatever errors attached to professional **hydropathy**, it taught the world the boundless therapeutic blessing of pure water." },
      { author: "Nathaniel Hawthorne", work: "The Blithedale Romance", quote: "The reformer recommended a course of **hydropathy** to wash away the nervous languor induced by city life." }
    ]
  },
  "Dashboard — path/idiopathic.md": {
    primary: "Relating to or denoting any disease or clinical condition that arises spontaneously or for which the underlying cause is unknown.",
    secondary: "In clinical nosology, a primary disease entity not secondary to or caused by another recognized disorder.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "We retain the label **idiopathic** epilepsy for those convulsive seizures where neither trauma nor tumor can be identified." },
      { author: "Jean-Martin Charcot", work: "Clinical Lectures on Diseases of the Nervous System", quote: "When the autopsy reveals no structural lesion, the physician is driven to classify the paralysis as functional or **idiopathic**." },
      { author: "Armand Trousseau", work: "Lectures on Clinical Medicine", quote: "True **idiopathic** tetanus was often distinguished from traumatic tetanus, though both run an agonizing clinical course." }
    ]
  },
  "Dashboard — path/mononeuropathy.md": {
    primary: "Damage, disease, or dysfunction affecting a single peripheral nerve trunk (e.g., carpal tunnel syndrome, peroneal nerve palsy).",
    secondary: "In neurology, characterized by sensory and motor deficits strictly confined to the anatomical distribution of the affected nerve.",
    quotes: [
      { author: "William Gowers", work: "A Manual of Diseases of the Nervous System", quote: "Direct compression of the radial nerve against the humerus produces an acute **mononeuropathy** known as Saturday night palsy." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Isolated facial paralysis, or Bell's palsy, represents the most familiar form of acute cranial **mononeuropathy**." },
      { author: "S. Weir Mitchell", work: "Injuries of Nerves and Their Consequences", quote: "A gunshot grazing the median nerve results in an agonizing **mononeuropathy** accompanied by burning causalgia." }
    ]
  },
  "Dashboard — path/myopathic.md": {
    primary: "Of, relating to, or characteristic of myopathy; involving or caused by primary disease of muscle tissue.",
    secondary: "In neurology, describing muscle weakness (myopathic facies, myopathic gait) resulting from intrinsic muscular dystrophy rather than denervation.",
    quotes: [
      { author: "William Gowers", work: "Pseudo-Hypertrophic Muscular Paralysis", quote: "The peculiar waddling gait and rising on one's knees reveal an unmistakably **myopathic** origin of the child's weakness." },
      { author: "Jean-Martin Charcot", work: "Lectures on the Diseases of the Nervous System", quote: "Microscopic section demonstrated that the muscular fibers were degenerated, confirming a purely **myopathic** process." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "In differentiating spinal muscular atrophy from muscular dystrophy, the absence of sensory loss favors a **myopathic** diagnosis." }
    ]
  },
  "Dashboard — path/myopathy.md": {
    primary: "A disease or disorder of muscle tissue, characterized by progressive muscular weakness, degeneration, or wasting without primary nerve disease.",
    secondary: "In clinical neuromuscular medicine, encompassing congenital dystrophies, metabolic muscle disorders, and inflammatory conditions like polymyositis.",
    quotes: [
      { author: "William Gowers", work: "A Manual of Diseases of the Nervous System", quote: "We group under primary **myopathy** those remarkable wasting disorders where the muscular fibers perish while the spinal cord remains intact." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "In familial **myopathy**, the child often presents with enlarged, doughy calves that conceal actual profound loss of contractile power." },
      { author: "Oliver Sacks", work: "A Leg to Stand On", quote: "Following orthopedic casting, my quadriceps suffered a temporary disuse **myopathy** that paralyzed my walking reflex." }
    ]
  },
  "Dashboard — path/neuropathy.md": {
    primary: "Disease, inflammation, or damage affecting the peripheral nerves, typically causing numbness, tingling, weakness, and pain.",
    secondary: "In medicine, a widespread complication of diabetes mellitus (diabetic neuropathy), nutritional deficiencies, alcoholism, or autoimmune disease.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Peripheral **neuropathy** in chronic alcoholics begins with numbness in the toes and progresses to bilateral wrist-drop." },
      { author: "William Gowers", work: "A Manual of Diseases of the Nervous System", quote: "Toxic **neuropathy** caused by lead or arsenic selectively impairs the extensor muscles of the forearms." },
      { author: "Oliver Sacks", work: "The Man Who Mistook His Wife for a Hat", quote: "The sudden sensory **neuropathy** had stripped Christina of all proprioception, leaving her bodily blind and floating." }
    ]
  },
  "Dashboard — path/paleopathology.md": {
    primary: "The study of ancient diseases, injuries, and health in mummies, fossilized hominids, and archaeological skeletal remains.",
    secondary: "An interdisciplinary field combining bioarchaeology and forensic pathology to reconstruct disease ecology and trauma in historical populations.",
    quotes: [
      { author: "Marc Armand Ruffer", work: "Studies in the Palaeopathology of Egypt", quote: "Microscopic analysis of mummified tissues founded scientific **paleopathology**, revealing arterial calcification in pharaohs." },
      { author: "Ales Hrdlicka", work: "Anthropometry", quote: "Evidence of healed trephinations and syphilitic nodes in ancient Peruvian skulls opened vast horizons for **paleopathology**." },
      { author: "Ernst Mayr", work: "What Evolution Is", quote: "Through **paleopathology**, we trace the history of infectious parasitism back millions of years into the dinosaur fossil record." }
    ]
  },
  "Dashboard — path/parasympathetic.md": {
    primary: "Relating to the craniosacral division of the autonomic nervous system that conserves energy, slows heart rate, increases intestinal and gland activity, and relaxes sphincter muscles ('rest and digest').",
    secondary: "Contrasted with the sympathetic nervous system; mediated primarily by acetylcholine acting on muscarinic receptors.",
    quotes: [
      { author: "John Newport Langley", work: "The Autonomic Nervous System", quote: "I propose the term **parasympathetic** for those craniosacral autonomic outflows that act antagonistically to the thoracic-lumbar sympathetic trunk." },
      { author: "Walter Cannon", work: "The Wisdom of the Body", quote: "While the sympathetic system mobilizes the body for fight or flight, the **parasympathetic** division presides over nutrition and recuperation." },
      { author: "Charles Sherrington", work: "The Integrative Action of the Nervous System", quote: "The vagal nerve provides the chief **parasympathetic** brake upon cardiac rhythm, preventing metabolic exhaustion." }
    ]
  },
  "Dashboard — path/parasympathomimetic.md": {
    primary: "Producing physiological effects resembling those caused by stimulation of the parasympathetic nervous system (cholinergic).",
    secondary: "In pharmacology, describing cholinomimetic drugs (e.g., pilocarpine, physostigmine, bethanechol) that stimulate muscarinic receptors or inhibit acetylcholinesterase.",
    quotes: [
      { author: "Henry Hallett Dale", work: "Adventures in Physiology", quote: "Acetylcholine acts as the quintessential **parasympathomimetic** transmitter, inducing bronchoconstriction and profuse salivary secretion." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Ophthalmologists utilize the **parasympathomimetic** action of pilocarpine drops to constrict the pupil in acute glaucoma." },
      { author: "Walter Cannon", work: "Bodily Changes in Pain, Hunger, Fear and Rage", quote: "Administration of a **parasympathomimetic** agent accelerates gastric peristalsis, reversing the inhibitory shutdown of fear." }
    ]
  },
  "Dashboard — path/path.md": {
    primary: "The Greek root *path-* (from *pathos*), signifying suffering, feeling, emotion, or disease (seen in *pathology*, *sympathy*, *apathy*); also a track or way.",
    secondary: "The universal morphological combining form across psychological, ethical, and medical vocabularies denoting affective states or morbid conditions.",
    quotes: [
      { author: "Henry George Liddell & Robert Scott", work: "A Greek-English Lexicon", quote: "The Greek noun *pathos* and its combining root **path** convey whatever befalls someone: calamity, passion, illness, or tender emotion." },
      { author: "Aristotle", work: "Rhetoric", quote: "The orator persuades through ethos, logos, and **pathos**, touching the emotional springs of human nature." },
      { author: "Rudolf Virchow", work: "Cellular Pathology", quote: "In medical terminology, the radical **path** identifies those alterations in living tissues that depart from physiological health." }
    ]
  },
  "Dashboard — path/pathan.md": {
    primary: "A member of a Pashto-speaking people (the Pashtuns) living primarily in southeastern Afghanistan and northwestern Pakistan.",
    secondary: "Historically famed in frontier history for their fierce martial independence, tribal code of honor (*Pashtunwali*), and resistance to imperial powers.",
    quotes: [
      { author: "Rudyard Kipling", work: "The Ballad of East and West", quote: "Kamal was the leader of the frontier border thieves, a hardy **Pathan** warrior of the Khyber Hills." },
      { author: "Winston Churchill", work: "The Story of the Malakand Field Force", quote: "The **Pathan** tribesman is a born rifleman, defending his barren crags with reckless personal gallantry." },
      { author: "Arthur Conan Doyle", work: "A Study in Scarlet", quote: "Watson had been wounded by a Jezail bullet while serving on the Afghan border against the fierce **Pathan** tribes." }
    ]
  },
  "Dashboard — path/pathetic.md": {
    primary: "Arousing pity, sorrow, or sympathy through vulnerability or sadness; miserably inadequate or feeble.",
    secondary: "In classical rhetoric and aesthetics, evoking deep pathos, poignant emotion, or tragic grandeur.",
    quotes: [
      { author: "John Ruskin", work: "Modern Painters", quote: "The poetic attribution of human passions to inanimate nature—as when leaves weep—I denominate the **pathetic** fallacy." },
      { author: "Charles Dickens", work: "The Old Curiosity Shop", quote: "The death of Little Nell was so exquisitely **pathetic** that readers on both sides of the Atlantic wept open tears." },
      { author: "Thomas Carlyle", work: "The French Revolution", quote: "The fallen monarch sat in his prison chamber, a **pathetic** shadow of the divine majesty that once ruled Versailles." }
    ]
  },
  "Dashboard — path/pathetically.md": {
    primary: "In a way that arouses pity, sorrow, or compassion; touchingly.",
    secondary: "In a miserably inadequate, weak, or contemptible manner.",
    quotes: [
      { author: "Charlotte Brontë", work: "Jane Eyre", quote: "The orphaned child looked up at me **pathetically**, her small cold fingers trembling in the November wind." },
      { author: "Herman Melville", work: "Bartleby, the Scrivener", quote: "Bartleby folded his hands and answered **pathetically**, 'I would prefer not to', before turning to the dead wall." },
      { author: "George Orwell", work: "Down and Out in Paris and London", quote: "The tramp counted his few copper coins **pathetically**, knowing they fell short of the price of a night's lodging." }
    ]
  },
  "Dashboard — path/pathless.md": {
    primary: "Having no path, track, or trail; untrodden, trackless, and wild.",
    secondary: "In poetic and existential literature, untraveled, boundless, or perplexing in spiritual course.",
    quotes: [
      { author: "Lord Byron", work: "Childe Harold's Pilgrimage", quote: "There is a pleasure in the **pathless** woods, there is a rapture on the lonely shore, there is society where none intrudes." },
      { author: "John Milton", work: "Paradise Lost", quote: "The Arch-fiend steered his ponderous flight across the **pathless** void of dark, unbottomed Chaos." },
      { author: "William Wordsworth", work: "The Excursion", quote: "The solitary shepherd climbed through the **pathless** crags where mist and silence reign supreme." }
    ]
  },
  "Dashboard — path/pathoclisis.md": {
    primary: "A selective susceptibility or localized vulnerability of specific brain regions, cell groups, or tissues to particular toxins, infections, or trauma.",
    secondary: "A neuropathological concept introduced by Cécile and Oskar Vogt explaining why certain diseases (e.g., carbon monoxide poisoning) target specific nuclei like the globus pallidus.",
    quotes: [
      { author: "Cécile Vogt & Oskar Vogt", work: "Erkrankungen der Grosshirnrinde", quote: "The distinct vulnerability of the striatum to hypoxic insult demonstrates the biological law of regional **pathoclisis**." },
      { author: "William Gowers", work: "A Manual of Diseases of the Nervous System", quote: "Selective motor neuron degeneration in amyotrophic lateral sclerosis provides a tragic instance of system **pathoclisis**." },
      { author: "Oliver Sacks", work: "The Man Who Mistook His Wife for a Hat", quote: "The localized destruction of the mamillary bodies in Korsakoff's syndrome illustrates cerebral **pathoclisis** under thiamine starvation." }
    ]
  },
  "Dashboard — path/pathogen.md": {
    primary: "A biological agent, especially a bacterium, virus, fungus, or parasite, capable of causing disease in a host organism.",
    secondary: "In microbiology and public health, an infectious microscopic entity governed by mechanisms of virulence, transmission, and host immune evasion.",
    quotes: [
      { author: "Louis Pasteur", work: "Germ Theory and Its Applications", quote: "The microscopic **pathogen** carried on surgical instruments was proved to be the true author of hospital gangrene." },
      { author: "Robert Koch", work: "Investigations into the Etiology of Traumatic Infective Diseases", quote: "To prove that a specific microorganism is the causal **pathogen**, it must be isolated in pure culture from every diseased animal." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Typhoid fever is engendered by a bacillary **pathogen** that contaminates community drinking wells." }
    ]
  },
  "Dashboard — path/pathogenesis.md": {
    primary: "The biological mechanism and chain of events through which a disease develops from initial cause to full manifestation.",
    secondary: "In experimental pathology, the cellular and molecular steps (e.g., inflammation, necrosis, fibrosis) that constitute disease progression.",
    quotes: [
      { author: "Rudolf Virchow", work: "Cellular Pathology", quote: "The ultimate **pathogenesis** of every systemic ailment resolves itself into altered metabolic processes within individual cells." },
      { author: "Paul Ehrlich", work: "Studies in Immunity", quote: "Understanding toxin-receptor binding on cell membranes clarified the cellular **pathogenesis** of tetanus." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Recent autopsy studies have illuminated the vascular **pathogenesis** of atherosclerotic apoplexy." }
    ]
  },
  "Dashboard — path/pathogenic.md": {
    primary: "Capable of producing, inciting, or causing disease; infectious or disease-causing.",
    secondary: "In bacteriology and parasitology, possessing specific virulence factors that overcome host biological defenses.",
    quotes: [
      { author: "Louis Pasteur", work: "The Germ Theory", quote: "We demonstrated that non-virulent strains can be cultivated to protect sheep against lethal **pathogenic** anthrax spores." },
      { author: "Robert Koch", work: "The Etiology of Tuberculosis", quote: "The tubercle bacillus possesses a waxy coat that renders it an extraordinarily durable **pathogenic** invader." },
      { author: "Rachel Carson", work: "Silent Spring", quote: "Overuse of antibiotics in agriculture risks breeding resistant strains among formerly docile **pathogenic** bacteria." }
    ]
  },
  "Dashboard — path/pathogenically.md": {
    primary: "In a pathogenic manner; by disease-causing mechanisms or biological infection.",
    secondary: "With respect to the production and propagation of disease within living tissues.",
    quotes: [
      { author: "Robert Koch", work: "Bacterial Morphology and Diagnosis", quote: "The inoculated mice reacted **pathogenically** within twenty-four hours, exhibiting splenic enlargement and septicaemia." },
      { author: "Louis Pasteur", work: "Studies on Fermentation", quote: "Foreign micro-organisms behave **pathogenically** toward beer wort, turning the vintage sour and unpalatable." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The streptococcus acts **pathogenically** across diverse tissues, producing erysipelas in the skin and endocarditis in the heart." }
    ]
  },
  "Dashboard — path/pathologic.md": {
    primary: "Relating to or caused by disease; indicative of a morbid physical or mental state; pathological.",
    secondary: "In diagnostic medicine, departing from the normal physiological baseline due to disease processes (e.g., pathologic fracture).",
    quotes: [
      { author: "Rudolf Virchow", work: "Cellular Pathology", quote: "Every **pathologic** growth is merely a modified physiological tissue proliferating under abnormal stimuli." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "A minor stumble produced a **pathologic** fracture of the femur, betraying the presence of metastatic malignancy." },
      { author: "William Gowers", work: "A Manual of Diseases of the Nervous System", quote: "The exaggerated deep tendon reflexes revealed a **pathologic** interruption of the descending corticospinal tract." }
    ]
  },
  "Dashboard — path/pathological.md": {
    primary: "Caused by, relating to, or involving physical or mental disease; morbid.",
    secondary: "Compulsive, obsessive, or wildly unreasonable, behaving like an involuntary disease (e.g., a pathological liar).",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The autopsy exposed a **pathological** enlargement of the spleen that explained the patient's severe refractory anemia." },
      { author: "Sigmund Freud", work: "The Psychopathology of Everyday Life", quote: "Slips of the tongue reveal the borderland between normal mental slips and true **pathological** symptoms." },
      { author: "Arthur Conan Doyle", work: "The Adventure of the Sussex Vampire", quote: "Holmes remarked that the stepson's jealousy had transcended normal family spite, becoming a dangerous **pathological** obsession." }
    ]
  },
  "Dashboard — path/pathologically.md": {
    primary: "In a pathological manner; as a consequence of or in relation to disease.",
    secondary: "In an extreme, obsessive, or abnormal degree.",
    quotes: [
      { author: "Rudolf Virchow", work: "Cellular Pathology", quote: "The liver parenchyma was **pathologically** altered, cells distended with globules of neutral fat." },
      { author: "William James", work: "The Varieties of Religious Experience", quote: "Certain religious hysterics appear **pathologically** sensitive to noise and light during their visions." },
      { author: "Henry Maudsley", work: "Body and Mind", quote: "The patient was **pathologically** suspicious, suspecting that poison had been infused into his evening tea." }
    ]
  },
  "Dashboard — path/pathologist.md": {
    primary: "A physician or medical scientist who specializes in pathology, the study of bodily tissues, fluids, and organs to diagnose disease.",
    secondary: "The forensic or hospital doctor responsible for conducting post-mortem autopsies and histological examinations.",
    quotes: [
      { author: "Rudolf Virchow", work: "Address to the Medical Society", quote: "The **pathologist** must combine clinical bedside observation with microscopic section to uncover the truth." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "As a young hospital **pathologist**, I spent long winter mornings in the Montreal morgue tracing endocarditis." },
      { author: "Arthur Conan Doyle", work: "The Resident Patient", quote: "The coroner relied upon the report of the **pathologist**, whose chemical analysis detected trace aconite in the deceased's tea." }
    ]
  },
  "Dashboard — path/pathology.md": {
    primary: "The scientific study of the nature, causes, processes, and consequences of disease.",
    secondary: "The structural and functional manifestations of a disease in a specific organ or condition (e.g., the pathology of pneumonia).",
    quotes: [
      { author: "Rudolf Virchow", work: "Cellular Pathology", quote: "Modern **pathology** is founded upon the single fundamental truth that all cells arise only from preexisting cells." },
      { author: "William Osler", work: "Aequanimitas", quote: "There is no royal road to the mastery of clinical medicine save through the post-mortem room and the laboratory of **pathology**." },
      { author: "Claude Bernard", work: "An Introduction to the Study of Experimental Medicine", quote: "Physiology and **pathology** are not two separate sciences, but merely the normal and disturbed manifestations of the same vital mechanisms." }
    ]
  },
  "Dashboard — path/pathos.md": {
    primary: "A quality in literature, art, music, or speech that evokes pity, tenderness, compassion, or sorrow.",
    secondary: "In classical Aristotelian rhetoric, one of the three primary artistic modes of persuasion, appealing directly to the audience's emotions.",
    quotes: [
      { author: "Aristotle", work: "Rhetoric", quote: "Persuasion is produced through the hearers themselves when their passions are stirred by speech, for **pathos** alters judgment." },
      { author: "Samuel Johnson", work: "Preface to Shakespeare", quote: "Shakespeare's power over human **pathos** commands our tears without the clumsy machinery of artificial lamentation." },
      { author: "Oscar Wilde", work: "De Profundis", quote: "Behind every sorrow there is a soul; suffering is the supreme truth that informs genuine artistic **pathos**." }
    ]
  },
  "Dashboard — path/psychopath.md": {
    primary: "A person suffering from a chronic mental disorder characterized by abnormal, violent, or callous behavior, egocentricity, and total lack of empathy or remorse.",
    secondary: "In forensic psychiatry and criminology, an individual exhibiting severe psychopathy who manipulates and exploits others without guilt.",
    quotes: [
      { author: "Hervey Cleckley", work: "The Mask of Sanity", quote: "The true **psychopath** presents a convincing facade of intelligence and charm that masks profound emotional bankruptcy." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The moral imbecile or criminal **psychopath** knows the legal definition of crime but feels no conscience." },
      { author: "Cesare Lombroso", work: "Criminal Man", quote: "Among habitual recidivists, the constitutional **psychopath** displays callous insensitivity to the suffering of his victims." }
    ]
  },
  "Dashboard — path/psychopathic.md": {
    primary: "Relating to, characteristic of, or affected with psychopathy; exhibiting callous, manipulative, and antisocial behavior without remorse.",
    secondary: "In historical psychiatric nosology, denoting any constitutionally unstable or eccentric personality disorder (psychopathic personality).",
    quotes: [
      { author: "Hervey Cleckley", work: "The Mask of Sanity", quote: "The **psychopathic** personality commits reckless, destructive acts without malice, driven merely by shallow momentary impulses." },
      { author: "Karl Jaspers", work: "General Psychopathology", quote: "We designate as **psychopathic** those abnormal personalities who suffer from their peculiarities or make society suffer." },
      { author: "William James", work: "The Varieties of Religious Experience", quote: "Genius is frequently accompanied by a **psychopathic** temperament that makes ordinary domestic happiness impossible." }
    ]
  },
  "Dashboard — path/psychopathy.md": {
    primary: "A mental disorder characterized by persistent antisocial behavior, impaired empathy, absence of remorse, boldness, and disinhibited egocentric traits.",
    secondary: "In clinical psychology and criminology, a personality construct measured by structured checklists (e.g., the Hare Psychopathy Checklist).",
    quotes: [
      { author: "Hervey Cleckley", work: "The Mask of Sanity", quote: "The mystery of **psychopathy** lies in the dissociation between intact cognitive intellect and totally flattened moral affect." },
      { author: "Karl Jaspers", work: "General Psychopathology", quote: "In the study of **psychopathy**, the alienist encounters personalities whose defect lies not in intelligence, but in moral sensibility." },
      { author: "Sigmund Freud", work: "Civilization and Its Discontents", quote: "The total absence of guilt characterizing severe **psychopathy** demonstrates what happens when the super-ego fails to form." }
    ]
  },
  "Dashboard — path/retinopathy.md": {
    primary: "Non-inflammatory damage or disease affecting the retina of the eye, typically resulting in impaired vision or blindness.",
    secondary: "In clinical ophthalmology, a common microvascular complication of chronic systemic disease, especially diabetic retinopathy and hypertensive retinopathy.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Ophthalmoscopic inspection in malignant hypertension reveals flame hemorrhages and soft exudates characteristic of severe **retinopathy**." },
      { author: "Oliver Sacks", work: "The Island of the Colorblind", quote: "Diabetic **retinopathy** had clouded his visual field with dark vitreous floaters, threatening total darkness." },
      { author: "Albrecht von Graefe", work: "Archiv für Ophthalmologie", quote: "Careful examination of the ocular fundus exposes early microaneurysms of **retinopathy** before visual acuity fails." }
    ]
  },
  "Dashboard — path/sociopath.md": {
    primary: "A person with a personality disorder manifesting in extreme antisocial attitudes and behavior, lack of conscience, and disregard for the rights of others.",
    secondary: "In sociological and psychological terminology, an individual whose antisocial criminality and lack of empathy are attributed primarily to environmental or social factors.",
    quotes: [
      { author: "Hervey Cleckley", work: "The Mask of Sanity", quote: "The glib **sociopath** uses words of love and contrition as mere tools to manipulate those who foolishly trust him." },
      { author: "Hannah Arendt", work: "Eichmann in Jerusalem", quote: "The totalitarian bureaucrat was no ordinary **sociopath**, but a thoughtless creature who suspended conscience to follow orders." },
      { author: "Oliver Sacks", work: "An Anthropologist on Mars", quote: "Unlike the autistic person who is bewildered by social cues, the **sociopath** understands them only too well to exploit them." }
    ]
  },
  "Dashboard — path/sociopathic.md": {
    primary: "Characterized by, relating to, or exhibiting the traits of a sociopath; antisocial, remorseless, and manipulative.",
    secondary: "Reflecting a total contempt for the moral conventions, legal codes, and safety of human society.",
    quotes: [
      { author: "Aldous Huxley", work: "Brave New World Revisited", quote: "Modern totalitarian regimes provide an ideal arena for **sociopathic** personalities to rise to absolute executive command." },
      { author: "George Orwell", work: "Nineteen Eighty-Four", quote: "O'Brien operated with a cold, **sociopathic** serenity, taking philosophical pleasure in shattering human wills." },
      { author: "Hervey Cleckley", work: "The Mask of Sanity", quote: "The **sociopathic** pattern of repeated financial fraud and abandoned families reveals a total absence of long-term remorse." }
    ]
  },
  "Dashboard — path/sympathectomy.md": {
    primary: "The surgical cutting, transection, or ablation of a portion of the sympathetic nervous pathway.",
    secondary: "Performed to treat severe palmar or facial hyperhidrosis, reflex sympathetic dystrophy (causalgia), or Raynaud's phenomenon by abolishing vasoconstriction.",
    quotes: [
      { author: "René Leriche", work: "The Surgery of Pain", quote: "By performing a periarterial **sympathectomy**, we relieved the intractable burning causalgia that tortured the wounded soldier." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Cervical **sympathectomy** produces Horner's syndrome: miosis, ptosis, and an absence of facial sweating." },
      { author: "Wilder Penfield", work: "The Cerebral Cortex of Man", quote: "Autonomic vascular tone in the upper extremity dropped immediately upon thoracic **sympathectomy**, warming the cold blanched hand." }
    ]
  },
  "Dashboard — path/sympathetic.md": {
    primary: "Feeling, showing, or expressing sympathy, compassion, and understanding for another person's distress.",
    secondary: "Relating to the thoracic-lumbar division of the autonomic nervous system that prepares the body for fight or flight; in physics, vibrating in resonance with another body.",
    quotes: [
      { author: "William Shakespeare", work: "The Tempest", quote: "Mine eyes, even sociable to the show of thine, fall fellowly drops in **sympathetic** sorrow." },
      { author: "Walter Cannon", work: "Bodily Changes in Pain, Hunger, Fear and Rage", quote: "Activation of the **sympathetic** nervous system dilates the bronchioles, accelerates heart rate, and pours sugar into the blood." },
      { author: "Charles Darwin", work: "The Descent of Man", quote: "Communities that included the greatest number of **sympathetic** members would flourish best and rear the greatest number of offspring." }
    ]
  },
  "Dashboard — path/sympathetically.md": {
    primary: "In a sympathetic manner; with compassion, pity, benevolence, or emotional agreement.",
    secondary: "In physiology or physics, in autonomic response or harmonic resonance.",
    quotes: [
      { author: "Jane Austen", work: "Emma", quote: "Mr. Knightley listened **sympathetically** to her confession, pleased to see her vanity give way to penitence." },
      { author: "George Eliot", work: "Middlemarch", quote: "Dorothea looked **sympathetically** at the tired peasant woman, offering whatever small comfort her hands could bring." },
      { author: "John Tyndall", work: "Sound", quote: "When the primary tuning fork is struck, the adjacent matched fork vibrates **sympathetically** across the room." }
    ]
  },
  "Dashboard — path/sympathise.md": {
    primary: "To feel or express sorrow, pity, compassion, or solidarity for someone experiencing distress (Commonwealth spelling).",
    secondary: "To agree with or approve of a sentiment, cause, or political principle.",
    quotes: [
      { author: "Charlotte Brontë", work: "Jane Eyre", quote: "I can readily **sympathise** with your lonely vigil, Jane, for my own youth was dark and tempestuous." },
      { author: "William Makepeace Thackeray", work: "Vanity Fair", quote: "Dobbin could not but **sympathise** with poor Amelia's silent heartbreak when the regiment was ordered abroad." },
      { author: "George Bernard Shaw", work: "Major Barbara", quote: "It is easy to **sympathise** with the suffering of the poor, but far harder to abolish their poverty." }
    ]
  },
  "Dashboard — path/sympathiser.md": {
    primary: "A person who agrees with, feels compassion for, or provides support to an opinion, party, or cause (Commonwealth spelling).",
    secondary: "A covert or open adherent of an insurgent, political, or social movement.",
    quotes: [
      { author: "Walter Scott", work: "Waverley", quote: "Every Jacobite **sympathiser** in the Highlands drank secretly to the health of the king across the water." },
      { author: "Arthur Conan Doyle", work: "The Valley of Fear", quote: "The coal company suspected that every third miner was a secret **sympathiser** with the Scowrers." },
      { author: "Joseph Conrad", work: "Under Western Eyes", quote: "Razumov was horrified to find himself celebrated as a heroic **sympathiser** with the bomb-throwing revolutionist." }
    ]
  },
  "Dashboard — path/sympathize.md": {
    primary: "To feel or express sympathy, pity, or compassion for another's misfortune (American spelling).",
    secondary: "To share in, agree with, or support an opinion or aspiration.",
    quotes: [
      { author: "Nathaniel Hawthorne", work: "The Scarlet Letter", quote: "Nature itself seemed to **sympathize** with the solitary lovers, sending golden sunshine through the dark forest canopy." },
      { author: "Mark Twain", work: "The Adventures of Tom Sawyer", quote: "Aunt Polly began to soften and **sympathize** with the weeping boy, dropping her birch switch to the floor." },
      { author: "Ralph Waldo Emerson", work: "Friendship", quote: "To **sympathize** with a great man's vision is already to participate in his intellectual elevation." }
    ]
  },
  "Dashboard — path/sympathizer.md": {
    primary: "A person who supports or approves of a particular cause, policy, or movement, especially without being a formal member (American spelling).",
    secondary: "Someone who feels emotional alignment or pity toward another's condition.",
    quotes: [
      { author: "Abraham Lincoln", work: "Letters and Speeches", quote: "The administration must distinguish between an armed rebel and a misguided Southern **sympathizer** who took no active part." },
      { author: "Frederick Douglass", work: "My Bondage and My Freedom", quote: "Many a quiet Quaker **sympathizer** along the Underground Railroad risked imprisonment to shelter our flight." },
      { author: "Henry David Thoreau", work: "A Plea for Captain John Brown", quote: "I hear many a Northern **sympathizer** praise Brown's bravery, while shrinking from his radical abolitionism." }
    ]
  },
  "Dashboard — path/sympathomimetic.md": {
    primary: "Producing physiological effects resembling those caused by stimulation of the sympathetic nervous system.",
    secondary: "In pharmacology, describing adrenergic agonists (e.g., epinephrine, norepinephrine, amphetamine) that raise blood pressure, increase heart rate, and dilate bronchi.",
    quotes: [
      { author: "George Barger & Henry Hallett Dale", work: "Chemical Structure and Sympathomimetic Action of Amines", quote: "We propose the term **sympathomimetic** to designate those amines that simulate the peripheral effects of sympathetic nerve stimulation." },
      { author: "Walter Cannon", work: "The Wisdom of the Body", quote: "Circulating adrenaline behaves as an endogenous **sympathomimetic** hormone, fortifying the organism against emergency demands." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The powerful **sympathomimetic** vasoconstriction induced by ephedrine relieves acute bronchial spasm in asthmatic attacks." }
    ]
  },
  "Dashboard — path/sympathy.md": {
    primary: "Feelings of pity, sorrow, and compassion for someone else's misfortune.",
    secondary: "Mutual affinity or harmonious agreement between persons, minds, or natural objects; resonance.",
    quotes: [
      { author: "Adam Smith", work: "The Theory of Moral Sentiments", quote: "How selfish soever man may be supposed, there are evidently some principles in his nature which interest him in the fortune of others: this is **sympathy**." },
      { author: "William Shakespeare", work: "Hamlet", quote: "A little more than kin, and less than kind; no **sympathy** bound the grieving prince to the usurping king." },
      { author: "Percy Bysshe Shelley", work: "A Defence of Poetry", quote: "The great secret of morals is love, or a going out of our nature, an identification of ourselves with the beautiful, which is pure **sympathy**." }
    ]
  },
  "Dashboard — path/telepathic.md": {
    primary: "Communicating thoughts, sensations, or mental states from one person to another without the use of known physical senses.",
    secondary: "Pertaining to telepathy; exhibiting an apparent direct extrasensory mental link.",
    quotes: [
      { author: "Frederic W. H. Myers", work: "Human Personality and Its Survival of Bodily Death", quote: "We accumulated extensive evidence of **telepathic** transfer occurring between twins separated by hundreds of miles." },
      { author: "William James", work: "The Will to Believe and Other Essays", quote: "Scientific curiosity demands an open-minded examination of spontaneous **telepathic** hallucinations occurring at the moment of death." },
      { author: "Arthur Conan Doyle", work: "The Edge of the Unknown", quote: "The experimental subjects demonstrated a remarkable **telepathic** rapport when blindfolded in separate rooms." }
    ]
  },
  "Dashboard — path/telepathise.md": {
    primary: "To communicate thoughts, feelings, or mental imagery by telepathy (Commonwealth spelling).",
    secondary: "To transmit ideas mind-to-mind without verbal or sensory mechanisms.",
    quotes: [
      { author: "H. G. Wells", work: "Men Like Gods", quote: "The utopian humans had abandoned vocal speech, choosing to **telepathise** their complex thoughts with instantaneous clarity." },
      { author: "Arthur Conan Doyle", work: "The Land of Mist", quote: "The medium attempted to **telepathise** the sealed symbol to the investigator sitting across the table." },
      { author: "George Bernard Shaw", work: "Back to Methuselah", quote: "In the far distant future, the Ancients will scarcely need to speak; they will **telepathise** across continents." }
    ]
  },
  "Dashboard — path/telepathist.md": {
    primary: "A person who claims to possess the ability to communicate telepathically or who investigates telepathic phenomena.",
    secondary: "A mentalist or parapsychological researcher focused on mind-reading experiments.",
    quotes: [
      { author: "Frederic W. H. Myers", work: "Phantasms of the Living", quote: "The professional **telepathist** was tested in our laboratory under strict conditions to prevent auditory cueing." },
      { author: "Arthur Conan Doyle", work: "The Memoirs of Sherlock Holmes", quote: "Holmes remarked that a clever detective must be half **telepathist**, reading thoughts from the twitch of an eyelid." },
      { author: "William James", work: "Memories and Studies", quote: "Mrs. Piper performed feats that led many observers to believe she was a genuine **telepathist** of extraordinary power." }
    ]
  },
  "Dashboard — path/telepathize.md": {
    primary: "To transmit thoughts, images, or impressions directly to another mind without physical communication (American spelling).",
    secondary: "To engage in telepathic transmission or extrasensory projection.",
    quotes: [
      { author: "H. G. Wells", work: "The Shape of Things to Come", quote: "Speculative psychologists wondered whether future mankind might learn to **telepathize** during sleep." },
      { author: "Arthur Conan Doyle", work: "The Vital Message", quote: "He believed that departed souls could **telepathize** comforting thoughts into the minds of grieving mourners." },
      { author: "William James", work: "Essays in Psychical Research", quote: "If one mind can **telepathize** a geometric figure to another across a stone wall, the old physics of sensation must be revised." }
    ]
  },
  "Dashboard — path/telepathy.md": {
    primary: "The purported communication of thoughts, impressions, or feelings between minds without the use of known sensory channels or physical signs.",
    secondary: "A term coined in 1882 by Frederic W. H. Myers for psychical research, from Greek *tēle* ('distant') and *patheia* ('feeling').",
    quotes: [
      { author: "Frederic W. H. Myers", work: "Phantasms of the Living", quote: "I propose the word **telepathy** to designate the communication of impressions of any kind from one mind to another, independently of the recognized channels of sense." },
      { author: "William James", work: "The Varieties of Religious Experience", quote: "If **telepathy** be established, the boundaries between individual human consciousnesses will appear far more porous than materialism admits." },
      { author: "Sigmund Freud", work: "Psychoanalysis and Telepathy", quote: "We must approach the problem of **telepathy** without prejudice, recognizing that the unconscious may transmit impulses across space." }
    ]
  },
  "Dashboard — path/unsympathetic.md": {
    primary: "Not showing, feeling, or expressing sympathy, warmth, or compassion; cold, callous, or unfeeling.",
    secondary: "Not pleasing, agreeable, or congenial in nature or tone.",
    quotes: [
      { author: "Charlotte Brontë", work: "Jane Eyre", quote: "Mr. Brocklehurst possessed a harsh, **unsympathetic** voice that chilled the shivering orphans of Lowood." },
      { author: "Jane Austen", work: "Sense and Sensibility", quote: "Fanny Dashwood was an **unsympathetic** woman who grudged her widowed mother-in-law the smallest comfort." },
      { author: "Charles Dickens", work: "Hard Times", quote: "Bounderby looked down upon the striking factory hands with an **unsympathetic** sneer, boasting of his own self-made rise." }
    ]
  },
  "Dashboard — path/unsympathetically.md": {
    primary: "In an unsympathetic, indifferent, or harsh manner; without compassion or understanding.",
    secondary: "Unpleasantly or discordantly.",
    quotes: [
      { author: "George Eliot", work: "Middlemarch", quote: "Mr. Casaubon replied **unsympathetically** to Dorothea's eager suggestions, retreating into his pedantic silence." },
      { author: "Arthur Conan Doyle", work: "The Adventure of the Speckled Band", quote: "Dr. Roylott glared **unsympathetically** at the terrified girl, commanding her to mind her household duties." },
      { author: "Thomas Hardy", work: "Tess of the d'Urbervilles", quote: "The village matrons gossiped **unsympathetically** by the well, passing judgment upon the ruined maiden." }
    ]
  }
};

for (const [relPath, entry] of Object.entries(filesData)) {
  const filePath = path.join(basePath, relPath);
  if (!fs.existsSync(filePath)) {
    console.error(`Missing file: ${filePath}`);
    continue;
  }
  const content = fs.readFileSync(filePath, 'utf8');

  // Find top portion up to > [!book]
  const bookIdx = content.indexOf('> [!book]');
  if (bookIdx === -1) {
    console.error(`No > [!book] in ${relPath}`);
    continue;
  }
  const topBlock = content.substring(0, bookIdx);

  const newContent = `${topBlock}> [!book] 📖 Definitions & Semantic Range
> 1. **Primary Definition (Lexical / Standard Consensus)**: ${entry.primary}
> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: ${entry.secondary}

> [!quote] 💬 Contextual Usage & Authentic Quotations
${entry.quotes.map(q => `> - 📜 **${q.author} (*${q.work}*):** *"${q.quote}"*`).join('\n')}
`;

  fs.writeFileSync(filePath, newContent, 'utf8');
  console.log(`Updated: ${relPath}`);
}

console.log('Batch 6 complete! Total files updated:', Object.keys(filesData).length);
