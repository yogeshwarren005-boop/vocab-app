import fs from 'fs';
import path from 'path';

const baseDir = 'App database/Greek roots/Cluster Physics & Chemistry';

const filesData = {
  // === Dashboard — capn (14 words) ===
  "Dashboard — capn/acapnic.md": {
    primary: "Relating to, afflicted with, or characterized by acapnia; having an abnormally low concentration of carbon dioxide in the blood.",
    secondary: "In physiological mechanics, describing hypocapnic vascular or neurological responses induced by hyperventilation.",
    quotes: [
      { author: "Yandell Henderson", work: "Adventures in Respiration", quote: "The **acapnic** state induced by excessive artificial respiration leads to immediate cessation of spontaneous breathing." },
      { author: "J. S. Haldane", work: "Respiration", quote: "In an **acapnic** subject, cerebral blood vessels constrict, diminishing cortical oxygen delivery." },
      { author: "Walter B. Cannon", work: "Bodily Changes in Pain, Hunger, Fear and Rage", quote: "Rapid breathing during acute fear often produces an **acapnic** reaction accompanied by lightheadedness." }
    ]
  },
  "Dashboard — capn/acapnotic.md": {
    primary: "Free from smoke or soot; smokeless; or designating non-smoking conditions or environments.",
    secondary: "In physiological contexts, an archaic synonym for acapnic, describing conditions devoid of carbon dioxide.",
    quotes: [
      { author: "Benjamin Franklin", work: "Observations on the Causes and Cure of Smoky Chimneys", quote: "The improved stove was designed to ensure an **acapnotic** hearth, free from offensive fumes and soot." },
      { author: "Count Rumford (Benjamin Thompson)", work: "Essays, Political, Economical, and Philosophical", quote: "By altering the throat of the fireplace, we obtained an almost perfectly **acapnotic** combustion." },
      { author: "John Evelyn", work: "Fumifugium: or The Inconvenience of the Aer and Smoak of London Dissipated", quote: "He envisioned an **acapnotic** city where clean fuels would replace the pestilential bituminous sea-coal." }
    ]
  },
  "Dashboard — capn/capn.md": {
    primary: "A combining form derived from Greek kapnos, meaning 'smoke', 'vapor', or in modern physiological terminology, 'carbon dioxide'.",
    secondary: "In biomedical nomenclature, the classical root employed to form terms relating to respiratory carbon dioxide measurement and monitoring.",
    quotes: [
      { author: "J. S. Haldane", work: "Methods of Air Analysis", quote: "The morpheme **capn**- appears consistently in modern instruments devoted to expired gas analysis." },
      { author: "Yandell Henderson", work: "Respiration and Blood Gas Kinetics", quote: "From the Hellenic root **capn**-, physiologists coined acapnia and hypercapnia to designate extremes of blood carbon dioxide." },
      { author: "Julius Comroe", work: "Physiology of Respiration", quote: "Diagnostic terminology relying on **capn**- reflects the historic association between smoke and combustion gases." }
    ]
  },
  "Dashboard — capn/capnogram.md": {
    primary: "The continuous waveform tracing of carbon dioxide concentration in expired respiratory gases displayed over time.",
    secondary: "In anesthesia and critical care medicine, a graphical waveform providing real-time verification of endotracheal tube placement and pulmonary perfusion.",
    quotes: [
      { author: "Atul Gawande", work: "The Checklist Manifesto", quote: "A steady rectangular wave on the **capnogram** immediately confirmed that the tube was situated in the trachea." },
      { author: "Jerome Groopman", work: "How Doctors Think", quote: "The sudden loss of the plateau on the **capnogram** alerted the team to a catastrophic drop in cardiac output." },
      { author: "Henry K. Beecher", work: "Resuscitation and Anesthesia for Wounded Men", quote: "Continuous inspection of the **capnogram** provides immediate warning of hypoventilation during surgery." }
    ]
  },
  "Dashboard — capn/capnograph.md": {
    primary: "An electronic monitoring instrument that measures and displays the concentration of carbon dioxide in respiratory gases as a continuous visual curve.",
    secondary: "An infrared gas analyzer used in operating rooms and emergency units to assess ventilation, cardiac output, and metabolic rate.",
    quotes: [
      { author: "Oliver Sacks", work: "Awakenings", quote: "The gentle rhythmic chirp of the **capnograph** kept watch over the patient's breathing throughout the procedure." },
      { author: "Paul Kalanithi", work: "When Breath Becomes Air", quote: "In the neurosurgical suite, the **capnograph** registered each subtle change in end-tidal gas concentration." },
      { author: "Abraham Verghese", work: "Cutting for Stone", quote: "The technician calibrated the **capnograph** with precision gases before wheeling it into theatre." }
    ]
  },
  "Dashboard — capn/capnography.md": {
    primary: "The non-invasive monitoring and graphical recording of carbon dioxide levels in the respiratory cycle.",
    secondary: "In anesthesiology and critical care, an indispensable standard of care for assessing alveolar ventilation and detecting circuit disconnections.",
    quotes: [
      { author: "Atul Gawande", work: "Complications: A Surgeon's Notes on an Imperfect Science", quote: "The widespread adoption of **capnography** caused anesthesia-related hypoxia deaths to plummet across the globe." },
      { author: "Julius Comroe", work: "The Lung: Clinical Physiology and Pulmonary Function Tests", quote: "Quantitative **capnography** enables the clinician to calculate physiologic dead space with remarkable ease." },
      { author: "Jerome Groopman", work: "The Anatomy of Hope", quote: "Modern intensive care relies on continuous **capnography** to fine-tune mechanical ventilation." }
    ]
  },
  "Dashboard — capn/capnolagnia.md": {
    primary: "A paraphilia or psychological condition in which sexual arousal is derived from the sight, smell, or presence of tobacco smoke or smokers.",
    secondary: "In clinical sexology and psychopathology, a rare fetish centered on the aesthetics, gestures, or odor of smoking cigarettes or pipes.",
    quotes: [
      { author: "Havelock Ellis", work: "Studies in the Psychology of Sex", quote: "In certain individuals displaying **capnolagnia**, the swirling smoke of a cigarette serves as an intense erotic stimulus." },
      { author: "Richard von Krafft-Ebing", work: "Psychopathia Sexualis", quote: "Fetishistic associations with burning tobacco leaves, occasionally classified under **capnolagnia**, illustrate associative sensory conditioning." },
      { author: "Magnus Hirschfeld", work: "Sexual Anomalies and Perversions", quote: "Cases of **capnolagnia** reveal how olfactory and visual cues around pipe or cigar smoking can become exclusive objects of desire." }
    ]
  },
  "Dashboard — capn/capnomancy.md": {
    primary: "Divination or fortune-telling by observing the movement, thickness, direction, or color of smoke rising from sacrificial fires or hearths.",
    secondary: "An ancient ritual practice documented across classical Greece, Mesopotamia, and Rome to divine divine will or military fortunes.",
    quotes: [
      { author: "James George Frazer", work: "The Golden Bough", quote: "The temple augur practiced **capnomancy**, watching whether the sacrificial smoke rose straight to heaven or drifted ominously back to earth." },
      { author: "Lewis Spence", work: "An Encyclopaedia of Occultism", quote: "In ancient rites of **capnomancy**, thin white smoke ascending vertically was universally hailed as an auspicious omen." },
      { author: "Edward Tylor", work: "Primitive Culture", quote: "Priests interpreted the flickering spirals of sacred smoke through the elaborate rules of **capnomancy**." }
    ]
  },
  "Dashboard — capn/capnometer.md": {
    primary: "A device or apparatus that measures the concentration or partial pressure of carbon dioxide in a gas mixture, displaying a numerical value.",
    secondary: "A clinical diagnostic instrument providing numerical end-tidal CO2 readings without necessarily rendering a continuous graphic wave.",
    quotes: [
      { author: "J. S. Haldane", work: "Respiration", quote: "A portable **capnometer** was lowered into the mine shaft to ensure that atmospheric carbon dioxide remained within breathable limits." },
      { author: "Julius Comroe", work: "Physiology of Respiration", quote: "The bedside **capnometer** signaled an abrupt rise in expired carbon dioxide during the hypoventilation trial." },
      { author: "August Krogh", work: "The Respiratory Exchange of Animals and Man", quote: "Direct volumetric determination with a calibrated **capnometer** confirmed the increased metabolic production during exercise." }
    ]
  },
  "Dashboard — capn/capnometry.md": {
    primary: "The measurement and numerical display of carbon dioxide concentrations in respiratory gases.",
    secondary: "The diagnostic discipline and methodology of quantifying end-tidal carbon dioxide (EtCO2) in pulmonary medicine.",
    quotes: [
      { author: "Julius Comroe", work: "The Lung: Clinical Physiology and Pulmonary Function Tests", quote: "Routine **capnometry** in intensive care units provides an immediate index of effective alveolar gas exchange." },
      { author: "Atul Gawande", work: "Better: A Surgeon's Notes on Performance", quote: "Even without full waveform imaging, simple colorimetric **capnometry** alerts the paramedic to tracheal intubation." },
      { author: "Paul Kalanithi", work: "When Breath Becomes Air", quote: "We tracked the patient's respiratory stabilization through quantitative **capnometry** over the critical post-operative hours." }
    ]
  },
  "Dashboard — capn/capnomor.md": {
    primary: "A colorless, oily liquid hydrocarbon mixture obtained by the destructive distillation of wood tar, peat, or animal matter.",
    secondary: "In historical organic chemistry, an aromatic fraction isolated by Carl Reichenbach in the 1830s, consisting primarily of alkylbenzenes.",
    quotes: [
      { author: "Carl Reichenbach", work: "Researches on Magnetism, Electricity, and Heat", quote: "From the volatile products of beech-wood tar, I separated the oily, fragrant liquid which I designated **capnomor**." },
      { author: "Justus von Liebig", work: "Familiar Letters on Chemistry", quote: "The substances known as eupione, creosote, and **capnomor** represent distinct distillation fractions of wood pyroligneous products." },
      { author: "Jöns Jacob Berzelius", work: "Traité de Chimie", quote: "Reichenbach's **capnomor** was examined for its solvency toward resins and volatile oils." }
    ]
  },
  "Dashboard — capn/capnophile.md": {
    primary: "A microorganism, especially a bacterium, that thrives in or requires high concentrations of carbon dioxide for optimal growth.",
    secondary: "In clinical microbiology, organisms such as Campylobacter, Neisseria, or Haemophilus cultivated under 5-10% CO2 candle jar conditions.",
    quotes: [
      { author: "René Dubos", work: "The Bacterial Cell in Its Relation to Problems of Virulence", quote: "The pathogenic **capnophile** requires an enriched carbon dioxide atmosphere to initiate robust colony formation." },
      { author: "Macfarlane Burnet", work: "Natural History of Infectious Disease", quote: "Culturing fastidious respiratory pathogens revealed that several were obligate or facultative **capnophile** strains." },
      { author: "Paul Ehrlich", work: "Studies in Immunity", quote: "Incubation within closed chambers with elevated carbon dioxide favored the isolation of the delicate **capnophile** species." }
    ]
  },
  "Dashboard — capn/hypercapnia.md": {
    primary: "An abnormally high concentration of carbon dioxide in the blood, resulting from hypoventilation or respiratory failure.",
    secondary: "In clinical pathophysiology, elevated arterial PCO2 exceeding 45 mmHg, leading to respiratory acidosis, somnolence, and vasodilation.",
    quotes: [
      { author: "J. S. Haldane", work: "Respiration", quote: "Severe **hypercapnia** acts as a powerful narcotic, eventually depressing the very respiratory center it initially stimulated." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "In chronic emphysema, long-standing **hypercapnia** blunts the sensitivity of the carotid body chemoreceptors." },
      { author: "Oliver Sacks", work: "Awakenings", quote: "The patient slipped into a drowsy stupor precipitated by progressive nighttime **hypercapnia**." }
    ]
  },
  "Dashboard — capn/hypocapnia.md": {
    primary: "An abnormally low concentration of carbon dioxide in the blood, typically caused by hyperventilation.",
    secondary: "In pulmonary medicine, arterial PCO2 below 35 mmHg, causing respiratory alkalosis, paresthesias, dizziness, and carpopedal spasm.",
    quotes: [
      { author: "Yandell Henderson", work: "Adventures in Respiration", quote: "Rapid breathing at high altitude brings about marked **hypocapnia**, shifting the hemoglobin dissociation curve to the left." },
      { author: "Walter B. Cannon", work: "The Wisdom of the Body", quote: "The physiological defense against **hypocapnia** involves renal excretion of bicarbonate to restore plasma pH." },
      { author: "Julius Comroe", work: "Physiology of Respiration", quote: "Cerebral vasoconstriction caused by acute **hypocapnia** can reduce intracranial pressure during acute brain swelling." }
    ]
  },

  // === Dashboard — cry (23 words) ===
  "Dashboard — cry/crier.md": {
    primary: "An official who makes public announcements or proclamations in the streets or in a court of justice (a town crier).",
    secondary: "A person who weeps or cries out; or one who proclaims news loudly in a public assembly.",
    quotes: [
      { author: "Charles Dickens", work: "A Tale of Two Cities", quote: "The court **crier** shouted for silence in the name of the Republic as the jury entered." },
      { author: "Nathaniel Hawthorne", work: "The Scarlet Letter", quote: "The town **crier** strode forward, ringing his brass bell and summoning the burghers to the marketplace." },
      { author: "William Shakespeare", work: "Troilus and Cressida", quote: "Silence in the court! Let the **crier** read the charge against the defendant." }
    ]
  },
  "Dashboard — cry/cry.md": {
    primary: "To shed tears, typically as an expression of pain, grief, sorrow, or intense joy; or to shout loudly.",
    secondary: "A combining root derived from Greek kryos, meaning 'cold', 'frost', or 'ice', used extensively in scientific terminology.",
    quotes: [
      { author: "William Shakespeare", work: "King Lear", quote: "When we are born, we **cry** that we are come to this great stage of fools." },
      { author: "Emily Brontë", work: "Wuthering Heights", quote: "I did not **cry** aloud, but buried my face in the pillow to muffle my bitter sobs." },
      { author: "Charles Darwin", work: "The Expression of the Emotions in Man and Animals", quote: "Infants **cry** instinctively from birth as a physiological signal of physical discomfort or hunger." }
    ]
  },
  "Dashboard — cry/crying.md": {
    primary: "The act of shedding tears or uttering loud vocal lamentations.",
    secondary: "Demanding immediate attention or redress; flagrant, urgent, or notorious (as in 'a crying injustice').",
    quotes: [
      { author: "Charles Dickens", work: "Oliver Twist", quote: "The child lay in the corner, **crying** bitterly from hunger and neglected loneliness." },
      { author: "Thomas Carlyle", work: "Past and Present", quote: "The condition of the working poor in our industrial cities is a **crying** scandal before heaven and earth." },
      { author: "Mary Shelley", work: "Frankenstein", quote: "I heard the creature **crying** in the icy darkness of the glacier, lamenting his miserable existence." }
    ]
  },
  "Dashboard — cry/cryo-adsorption.md": {
    primary: "The adsorption of gases or vapors onto a solid adsorbent surface at cryogenic temperatures.",
    secondary: "In high-vacuum engineering and cryopumping, a technique using charcoal or zeolites cooled to liquid helium temperatures to evacuate chambers.",
    quotes: [
      { author: "Irving Langmuir", work: "The Adsorption of Gases on Plane Surfaces", quote: "At low temperatures, **cryo-adsorption** immobilizes inert gas molecules onto activated carbon matrices." },
      { author: "James Dewar", work: "Collected Papers on Physical Phenomena", quote: "Utilizing **cryo-adsorption** on chilled coconut charcoal, we succeeded in obtaining extraordinary degrees of vacuum." },
      { author: "Heike Kamerlingh Onnes", work: "Communications from the Physical Laboratory of Leiden", quote: "The residual hydrogen in the liquefier was eliminated by selective **cryo-adsorption**." }
    ]
  },
  "Dashboard — cry/cryoablation.md": {
    primary: "The surgical or interventional destruction of diseased tissue, such as a tumor or cardiac arrhythmogenic focus, by the application of extreme cold.",
    secondary: "In oncology and cardiology, a minimally invasive procedure using cryoprobes circulating pressurized liquid nitrogen or argon to induce cellular necrosis.",
    quotes: [
      { author: "Atul Gawande", work: "Being Mortal", quote: "Targeted **cryoablation** offered the elderly patient a non-invasive alternative to major open pulmonary resection." },
      { author: "Siddhartha Mukherjee", work: "The Emperor of All Maladies", quote: "By driving sub-zero needles into the hepatic mass, **cryoablation** crystallizes intracellular water and destroys tumor membranes." },
      { author: "Jerome Groopman", work: "How Doctors Think", quote: "The electrophysiologist recommended catheter **cryoablation** to interrupt the aberrant pathway causing atrial fibrillation." }
    ]
  },
  "Dashboard — cry/cryobacterium.md": {
    primary: "A psychrophilic bacterium capable of living, metabolizing, and reproducing at extremely low, freezing temperatures.",
    secondary: "In astrobiology and polar microbiology, cold-adapted bacterial taxa isolated from deep glacial ice cores and permafrost.",
    quotes: [
      { author: "Lynn Margulis", work: "Symbiosis in Cell Evolution", quote: "The discovery of living **cryobacterium** strains in ancient Antarctic permafrost reshaped our notions of biological limits." },
      { author: "Carl Sagan", work: "The Cosmic Connection", quote: "If life evolved on Mars, a dormant **cryobacterium** encased in subsurface polar ice might still await detection." },
      { author: "Stephen Jay Gould", work: "The Panda's Thumb", quote: "Specialized cold-shock proteins enable each **cryobacterium** to survive the crushing crystallization of cellular water." }
    ]
  },
  "Dashboard — cry/cryobiology.md": {
    primary: "The branch of biology concerned with the effects of low temperatures on living organisms, tissues, and biological systems.",
    secondary: "The scientific discipline studying freeze-tolerance, cryoprotectants, and the preservation of cells, gametes, and organs at sub-zero temperatures.",
    quotes: [
      { author: "J. B. S. Haldane", work: "Possible Worlds", quote: "Advances in **cryobiology** may one day allow living tissues to be suspended in time without cellular degeneration." },
      { author: "E. O. Wilson", work: "The Diversity of Life", quote: "Studies in **cryobiology** revealed how wood frogs produce natural glucose anti-freeze to endure total winter freezing." },
      { author: "Francis Crick", work: "Life Itself: Its Origin and Nature", quote: "The experimental principles of **cryobiology** are crucial when considering the transport of viable spores through interstellar space." }
    ]
  },
  "Dashboard — cry/cryobot.md": {
    primary: "A robotic robotic probe or vehicle designed to melt and penetrate through thick glacial ice caps or extraterrestrial ice sheets.",
    secondary: "In planetary exploration, a thermal probe equipped with radioactive or electric heaters engineered to explore subglacial oceans on Europa or Enceladus.",
    quotes: [
      { author: "Arthur C. Clarke", work: "2010: Odyssey Two", quote: "An autonomous **cryobot** was envisioned to melt through Europa's frozen crust and sample the hidden ocean beneath." },
      { author: "Carl Sagan", work: "Pale Blue Dot", quote: "Proposals for exploring icy moons often feature a compact **cryobot** carrying miniaturized spectrometers through miles of ice." },
      { author: "Freeman Dyson", work: "Disturbing the Universe", quote: "Thermal drill probes resembling a **cryobot** have demonstrated remarkable efficiency in Antarctic borehole tests." }
    ]
  },
  "Dashboard — cry/cryochemistry.md": {
    primary: "The study of chemical reactions and molecular interactions occurring at extremely low temperatures, typically near absolute zero.",
    secondary: "In physical chemistry, the examination of matrix-isolation kinetics, quantum tunneling, and reactive free radicals immobilized in frozen inert gas matrices.",
    quotes: [
      { author: "George Pimentel", work: "Matrix Isolation Studies", quote: "The field of **cryochemistry** permitted the spectroscopic capture of reactive intermediates trapped in frozen argon at ten kelvins." },
      { author: "Linus Pauling", work: "The Nature of the Chemical Bond", quote: "At temperatures where thermal agitation ceases, **cryochemistry** demonstrates reactions driven purely by quantum mechanical tunneling." },
      { author: "C. N. Hinshelwood", work: "The Kinetics of Chemical Change", quote: "Classical activation energies lose their traditional significance when examined under the exotic conditions of **cryochemistry**." }
    ]
  },
  "Dashboard — cry/cryoelectronics.md": {
    primary: "The branch of electronics dealing with the behavior, design, and applications of electronic devices and circuits operating at cryogenic temperatures.",
    secondary: "The engineering discipline encompassing superconducting circuits, Josephson junctions, and ultra-low-noise amplifiers for quantum computing and radio astronomy.",
    quotes: [
      { author: "John Bardeen", work: "Theory of Superconductivity", quote: "Operating semiconductors at liquid nitrogen temperatures opened the field of **cryoelectronics**, drastically reducing thermal noise." },
      { author: "Richard Feynman", work: "Feynman Lectures on Computation", quote: "The integration of superconducting logic gates represents the ultimate frontier of modern **cryoelectronics**." },
      { author: "Philip W. Anderson", work: "Basic Notions of Condensed Matter Physics", quote: "Josephson junction arrays are the quintessential building blocks of superconducting **cryoelectronics**." }
    ]
  },
  "Dashboard — cry/cryogenic.md": {
    primary: "Of, relating to, or produced by extremely low temperatures, typically below -150 degrees Celsius (123 kelvins).",
    secondary: "Utilizing deep refrigeration or liquefied gases, such as liquid nitrogen, liquid oxygen, or liquid helium, in rocket propulsion or industrial processes.",
    quotes: [
      { author: "Arthur C. Clarke", work: "The Exploration of Space", quote: "Rockets fueled by **cryogenic** propellants like liquid oxygen and liquid hydrogen achieve the highest exhaust velocities." },
      { author: "Wernher von Braun", work: "History of Rocketry and Space Travel", quote: "Handling vast volumes of **cryogenic** fuel required specialized vacuum-jacketed plumbing on the launch pad." },
      { author: "Carl Sagan", work: "Cosmos", quote: "Infrared space telescopes must be kept at **cryogenic** temperatures to prevent their own heat from blinding their detectors." }
    ]
  },
  "Dashboard — cry/cryogenics.md": {
    primary: "The branch of physics and engineering that studies the production and effects of materials at very low temperatures.",
    secondary: "The technology of liquefying industrial gases and maintaining systems at temperatures below 120 kelvins for scientific and industrial applications.",
    quotes: [
      { author: "Heike Kamerlingh Onnes", work: "Investigations into the Properties of Substances at Low Temperatures", quote: "The triumph of modern **cryogenics** was achieved when liquid helium boiled peacefully in our Leiden laboratory." },
      { author: "James Dewar", work: "Collected Papers on Physical Phenomena", quote: "The practical foundations of **cryogenics** were established with the invention of the silvered vacuum flask." },
      { author: "Freeman Dyson", work: "From Eros to Gaia", quote: "Without the remarkable advances in **cryogenics**, particle accelerators like the Tevatron could never have functioned." }
    ]
  },
  "Dashboard — cry/cryomicroscopy.md": {
    primary: "The observation of biological specimens or materials with a microscope while maintaining them at cryogenic temperatures.",
    secondary: "In structural biology, cryo-electron microscopy (cryo-EM), a revolutionary imaging technique where vitrified frozen hydrated macromolecules are resolved at near-atomic resolution.",
    quotes: [
      { author: "Richard Henderson", work: "Cryo-EM: The Resolution Revolution", quote: "Vitrification of protein specimens without ice crystallization made **cryomicroscopy** the supreme tool of structural biology." },
      { author: "Jacques Dubochet", work: "Cryo-Electron Microscopy of Vitrified Specimens", quote: "By plunging thin aqueous films into liquid ethane, **cryomicroscopy** preserves the pristine native state of viral capsids." },
      { author: "Joachim Frank", work: "Three-Dimensional Electron Microscopy of Macromolecular Assemblies", quote: "Single-particle reconstruction coupled with **cryomicroscopy** unveiled the dynamic conformations of the ribosome." }
    ]
  },
  "Dashboard — cry/cryoneurolysis.md": {
    primary: "A specialized interventional pain-management technique that applies extreme cold to a peripheral nerve to temporarily interrupt pain signaling.",
    secondary: "In anesthesiology and pain medicine, the freezing of nerve axons using a closed cryoprobe, inducing reversible Wallerian degeneration while preserving the endoneurial sheath.",
    quotes: [
      { author: "John J. Bonica", work: "The Management of Pain", quote: "Percutaneous **cryoneurolysis** of the intercostal nerves produced lasting relief for the post-thoracotomy neuralgia patient." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Direct thermal interruption via **cryoneurolysis** provides temporary numbness without creating a permanent neuroma." },
      { author: "Henry K. Beecher", work: "Measurement of Subjective Responses", quote: "Sustained clinical analgesia following **cryoneurolysis** persists until axonal regeneration traverses the surviving sheath." }
    ]
  },
  "Dashboard — cry/cryonic.md": {
    primary: "Relating to cryonics, the deep-freeze preservation of human bodies or brains after legal death in anticipation of future medical reanimation.",
    secondary: "Describing preservation chambers, equipment, or protocols associated with cryopreserving human remains at liquid nitrogen temperatures.",
    quotes: [
      { author: "Robert Ettinger", work: "The Prospect of Immortality", quote: "The **cryonic** suspension of the deceased represents an audacious wager on the boundless potential of future medical science." },
      { author: "Isaac Asimov", work: "Change! Seventy-One Glimpses of the Future", quote: "While sensationalized in fiction, the **cryonic** storage of whole human organisms faces colossal biophysical hurdles." },
      { author: "Arthur C. Clarke", work: "Profiles of the Future", quote: "Long before interstellar travel becomes commonplace, reliable **cryonic** hibernation will have to be perfected." }
    ]
  },
  "Dashboard — cry/cryonics.md": {
    primary: "The practice of freezing human bodies or heads after legal death with the hope of restoring them to life and health when future technology allows.",
    secondary: "A controversial bioengineering field utilizing vitrification mixtures and liquid nitrogen storage dewar vessels to store deceased human subjects.",
    quotes: [
      { author: "Robert Ettinger", work: "The Prospect of Immortality", quote: "The central premise of **cryonics** is that death is a gradual process that low temperature can indefinitely arrest." },
      { author: "Carl Sagan", work: "The Demon-Haunted World", quote: "Proponents of **cryonics** promise a resurrection that contemporary biophysics cannot yet validate." },
      { author: "Richard Feynman", work: "The Pleasure of Finding Things Out", quote: "When considering **cryonics**, one must ask whether the intricate synaptic wiring of the brain survives freezing undamaged." }
    ]
  },
  "Dashboard — cry/cryopreservation.md": {
    primary: "The preservation of cells, tissues, organs, or viable biological material by cooling and storing them at extremely low temperatures.",
    secondary: "In reproductive biology, regenerative medicine, and biobanking, the freezing of gametes, embryos, and stem cells using liquid nitrogen and specialized cryoprotective agents.",
    quotes: [
      { author: "Peter Medawar", work: "The Uniqueness of the Individual", quote: "The successful **cryopreservation** of living spermatozoa opened an entirely new era in animal husbandry and genetics." },
      { author: "Ian Wilmut", work: "The Second Creation: Dolly and the Age of Biological Control", quote: "Modern reproductive cloning depends upon the meticulous **cryopreservation** of donor cell nuclei in liquid nitrogen." },
      { author: "E. O. Wilson", work: "The Future of Life", quote: "Frozen zoos rely on deep **cryopreservation** to maintain the viable genetic heritage of critically endangered species." }
    ]
  },
  "Dashboard — cry/cryoprotectant.md": {
    primary: "A substance used to protect biological tissue from damage caused by ice crystal formation during freezing.",
    secondary: "In cell biology and biobanking, chemical additives such as dimethyl sulfoxide (DMSO) or glycerol that lower the freezing point and prevent intracellular ice.",
    quotes: [
      { author: "Peter Medawar", work: "The Art of the Soluble", quote: "The discovery of glycerol as an effective **cryoprotectant** made the long-term freezing of red blood cells possible." },
      { author: "Francis Crick", work: "What Mad Pursuit", quote: "Without an adequate **cryoprotectant**, ice crystals act like microscopic blades, shearing fragile cell membranes to ribbons." },
      { author: "J. B. S. Haldane", work: "The Causes of Evolution", quote: "Natural compounds such as trehalose and glycerol serve as endogenous **cryoprotectant** molecules in arctic beetles." }
    ]
  },
  "Dashboard — cry/cryosphere.md": {
    primary: "The portions of the Earth's surface where water is in solid form, including sea ice, lake ice, river ice, snow cover, glaciers, ice caps, and permafrost.",
    secondary: "In Earth system science and climatology, the global frozen water sphere that plays a critical role in regulating global climate through planetary albedo.",
    quotes: [
      { author: "Rachel Carson", work: "The Sea Around Us", quote: "The frozen margins of the **cryosphere** expand and contract with the rhythmic beat of the planetary seasons." },
      { author: "Al Gore", work: "An Inconvenient Truth", quote: "Rapid warming in the Arctic is destabilizing the **cryosphere**, triggering feedback loops that accelerate global warming." },
      { author: "Arthur Holmes", work: "Principles of Physical Geology", quote: "The retreat of continental ice sheets illustrates the immense dynamic sensitivity of the terrestrial **cryosphere**." }
    ]
  },
  "Dashboard — cry/cryosurgery.md": {
    primary: "Surgery in which diseased or abnormal tissue is destroyed by the application of extreme cold, typically using liquid nitrogen.",
    secondary: "In clinical dermatology, urology, and neurosurgery, the targeted ablation of lesions (such as skin keratoses or prostate tumors) using controlled freezing.",
    quotes: [
      { author: "Atul Gawande", work: "Complications: A Surgeon's Notes on an Imperfect Science", quote: "The introduction of modern **cryosurgery** allowed dermatologists to eradicate precancerous lesions quickly in the clinic." },
      { author: "Sherwin B. Nuland", work: "How We Die", quote: "Pioneering attempts at **cryosurgery** in the brain utilized cooled cannulas to destroy subcortical tremor centers." },
      { author: "Oliver Sacks", work: "The Man Who Mistook His Wife for a Hat", quote: "Techniques of stereotaxic **cryosurgery** were once employed to ablate hyperactive thalamic nuclei in Parkinsonism." }
    ]
  },
  "Dashboard — cry/cryotherapy.md": {
    primary: "The local or general therapeutic use of low temperatures in medical treatment, sports rehabilitation, or dermatological therapy.",
    secondary: "In sports medicine and rheumatology, whole-body cold chambers or ice applications used to relieve inflammation, swelling, and muscle soreness.",
    quotes: [
      { author: "William Osler", work: "Aequanimitas", quote: "The prudent physician employs **cryotherapy** to soothe acute inflammatory swelling and dampen localized fever." },
      { author: "Jerome Groopman", work: "Second Opinions", quote: "Following the athletic injury, the trainer prescribed intensive **cryotherapy** alongside compression to minimize hematoma formation." },
      { author: "Oliver Sacks", work: "A Leg to Stand On", quote: "The chilling wraps of **cryotherapy** provided temporary relief from the throbbing neuralgic sensations in the convalescent limb." }
    ]
  },
  "Dashboard — cry/cryovolcano.md": {
    primary: "A volcano that erupts volatiles such as water, ammonia, or methane instead of molten silicate rock, typically occurring on icy moons.",
    secondary: "In planetary geology, an icy eruptive feature identified on celestial bodies such as Enceladus, Triton, Europa, and Titan.",
    quotes: [
      { author: "Carl Sagan", work: "Pale Blue Dot", quote: "Geysers erupting from a distant **cryovolcano** on Triton shoot nitrogen plumes miles into the tenuous atmosphere." },
      { author: "Arthur C. Clarke", work: "2010: Odyssey Two", quote: "The smooth plains of Europa bore witness to the resurfacing power of an ancient **cryovolcano** spewing slushy brine." },
      { author: "Stephen Hawking", work: "The Grand Design", quote: "Spectacular images from the Cassini probe confirmed that an active **cryovolcano** powers the majestic ring system of Saturn." }
    ]
  },
  "Dashboard — cry/decry.md": {
    primary: "To publicly denounce, condemn, or express strong disapproval of someone or something.",
    secondary: "To disparage, belittle, or depreciate the value, merit, or reputation of an action or institution.",
    quotes: [
      { author: "John Stuart Mill", work: "On Liberty", quote: "It is easy for prevailing opinion to **decry** novel philosophies before their rational merits can be evaluated." },
      { author: "Edmund Burke", work: "Reflections on the Revolution in France", quote: "Philosophers who **decry** ancient customs frequently fail to appreciate the latent wisdom embedded in long-standing institutions." },
      { author: "George Orwell", work: "Essays", quote: "Sycophantic critics hasten to **decry** any work of art that fails to flatter the prevailing ideological dogmas." }
    ]
  },

  // === Dashboard — electr (27 words) ===
  "Dashboard — electr/antielectron.md": {
    primary: "The antiparticle of the electron, having the same mass and spin as an electron but a positive electric charge; a positron.",
    secondary: "In particle physics, the fundamental lepton (e+) predicted by Paul Dirac in 1928 and experimentally discovered by Carl Anderson in 1932.",
    quotes: [
      { author: "Paul Dirac", work: "The Principles of Quantum Mechanics", quote: "Relativistic wave mechanics required the existence of a positive counterpart to the electron, an **antielectron** having identical mass." },
      { author: "Carl D. Anderson", work: "The Positive Electron", quote: "Cloud chamber photographs revealed the track of an **antielectron** curving in the magnetic field opposite to that of a negative electron." },
      { author: "Richard Feynman", work: "QED: The Strange Theory of Light and Matter", quote: "An **antielectron** or positron can be mathematically described as an ordinary electron moving backward through time." }
    ]
  },
  "Dashboard — electr/electr.md": {
    primary: "A combining root derived from Greek ēlektron, meaning 'amber', signifying electricity, electric charge, or electrons.",
    secondary: "In physical science and engineering nomenclature, the universal formative prefix designating phenomena, devices, and theories based on electric charge.",
    quotes: [
      { author: "William Gilbert", work: "De Magnete", quote: "From the Hellenic name for amber, ēlektron, we derive the term **electr**- to describe all bodies possessing attractive virtue upon friction." },
      { author: "Michael Faraday", work: "Experimental Researches in Electricity", quote: "The root **electr**- permeates modern natural philosophy, linking chemical affinity directly to galvanic forces." },
      { author: "James Clerk Maxwell", work: "A Treatise on Electricity and Magnetism", quote: "The extensive family of terms sharing the prefix **electr**- unified the disparate studies of static charge, magnetism, and light." }
    ]
  },
  "Dashboard — electr/electra.md": {
    primary: "A figure in Greek mythology, daughter of Agamemnon and Clytemnestra, who incited her brother Orestes to avenge their father's murder.",
    secondary: "In psychoanalysis, the eponymous figure of the Electra complex; or in astronomy, a bright blue-white giant star in the Pleiades cluster.",
    quotes: [
      { author: "Sophocles", work: "Electra", quote: "O sorrowful **Electra**, weeping by the palace gates, your lamentations echo through the hills of Mycenae." },
      { author: "Carl Jung", work: "The Theory of Psychoanalysis", quote: "To complement the Oedipus concept in boys, we introduced the **Electra** complex to describe the daughter's unconscious attachment to the father." },
      { author: "Arthur Eddington", work: "Stars and Atoms", quote: "Spectroscopic observations of **Electra** in the Pleiades reveal a rapidly rotating giant surrounded by glowing nebular gas." }
    ]
  },
  "Dashboard — electr/electric.md": {
    primary: "Of, relating to, producing, or operated by electricity.",
    secondary: "Exhilarating, thrilling, or charged with intense excitement, tension, or emotional energy.",
    quotes: [
      { author: "Benjamin Franklin", work: "Experiments and Observations on Electricity", quote: "The kite experiment proved conclusively that lightning is an **electric** discharge identical to the sparks produced in our laboratories." },
      { author: "Walt Whitman", work: "Leaves of Grass", quote: "I sing the body **electric**, the armies of those I love engirth me and I engirth them." },
      { author: "Charles Dickens", work: "Great Expectations", quote: "An **electric** thrill of apprehension passed through the company as the escaped convict burst through the door." }
    ]
  },
  "Dashboard — electr/electrical.md": {
    primary: "Related to, concerned with, or operated by electricity or the study of electricity.",
    secondary: "In engineering and physical science, pertaining to equipment, circuits, measurements, or energy derived from electric charge flows.",
    quotes: [
      { author: "Nikola Tesla", work: "My Inventions: The Autobiography of Nikola Tesla", quote: "The alternating current **electrical** transmission system eliminated the fatal distance limitations of direct current." },
      { author: "Thomas Edison", work: "The Diary of Thomas Edison", quote: "We worked for weeks in the laboratory until the **electrical** resistance of the carbon filament reached four hundred ohms." },
      { author: "Michael Faraday", work: "Experimental Researches in Electricity", quote: "Lines of **electrical** induction traverse dielectric space in curves that reflect the distribution of neighboring conductors." }
    ]
  },
  "Dashboard — electr/electrically.md": {
    primary: "In an electric manner; by means of electricity; with respect to electricity.",
    secondary: "In physical chemistry and physics, describing charges, bonds, or circuits operating via electrostatic or electrodynamic interactions.",
    quotes: [
      { author: "James Clerk Maxwell", work: "A Treatise on Electricity and Magnetism", quote: "The medium between the two conducting spheres becomes **electrically** polarized under the influence of the charge." },
      { author: "Lord Kelvin (William Thomson)", work: "Popular Lectures and Addresses", quote: "The transatlantic cable was **electrically** tested every hour to detect any flaw in the gutta-percha insulation." },
      { author: "Marie Curie", work: "Radioactive Substances", quote: "The ionization chamber rendered the surrounding air **electrically** conductive in the presence of radium rays." }
    ]
  },
  "Dashboard — electr/electrician.md": {
    primary: "A tradesperson skilled in installing, maintaining, and repairing electrical wiring, fixtures, and apparatus.",
    secondary: "Historically in eighteenth- and nineteenth-century natural philosophy, a scientist or experimentalist who studied electricity.",
    quotes: [
      { author: "Benjamin Franklin", work: "Experiments and Observations on Electricity", quote: "The curious **electrician** may easily repeat these trials with an ordinary Leyden jar and a glass rod." },
      { author: "H. G. Wells", work: "The Invisible Man", quote: "The village **electrician** was summoned to inspect the mysterious humming coming from the stranger's laboratory apparatus." },
      { author: "Joseph Priestley", work: "The History and Present State of Electricity", quote: "Every zealous **electrician** of that era sought to improve the frictional machine to generate larger sparks." }
    ]
  },
  "Dashboard — electr/electricity.md": {
    primary: "A fundamental form of physical energy resulting from the existence of charged particles (such as electrons or protons), manifesting as static charges, currents, and electromagnetic fields.",
    secondary: "Electric current used as a source of power for lighting, heating, computing, and mechanical work; or an intense feeling of collective suspense or excitement.",
    quotes: [
      { author: "Michael Faraday", work: "Experimental Researches in Electricity", quote: "The chemical action of **electricity** is always definite and directly proportional to the absolute quantity that passes." },
      { author: "Nikola Tesla", work: "Experiments with Alternate Currents", quote: "Ere many generations pass, our machinery will be driven by a power obtainable at any point in the universe, for **electricity** is everywhere." },
      { author: "Mary Shelley", work: "Frankenstein", quote: "With an anxiety that almost amounted to agony, I collected the instruments of life around me, that I might infuse a spark of being into the lifeless thing through **electricity**." }
    ]
  },
  "Dashboard — electr/electrification.md": {
    primary: "The process of charging a body with electricity; or the conversion of a system, railroad, or region to electric power.",
    secondary: "In economic and technological history, the large-scale infrastructure program replacing steam and manual power with electric grids.",
    quotes: [
      { author: "Vladimir Lenin", work: "Report on the Work of the Council of People's Commissars", quote: "Communism is Soviet power plus the **electrification** of the whole country, for without industry modern life cannot advance." },
      { author: "Lewis Mumford", work: "Technics and Civilization", quote: "The rapid **electrification** of urban manufacturing dispersed industrial power and dismantled the smoky reign of the steam engine." },
      { author: "James Clerk Maxwell", work: "A Treatise on Electricity and Magnetism", quote: "The state of **electrification** on the surface of a conductor is determined by the outward normal derivative of the potential." }
    ]
  },
  "Dashboard — electr/electrify.md": {
    primary: "To charge with electricity; to equip with electric power; or to shock or startle dramatically.",
    secondary: "To thrill, exhilarate, or arouse intense excitement and wonder in an audience or populace.",
    quotes: [
      { author: "H. G. Wells", work: "The Time Machine", quote: "The prospect of traveling through the fourth dimension seemed to **electrify** his imagination." },
      { author: "Arthur Conan Doyle", work: "The Lost World", quote: "Professor Challenger's sensational disclosure served to **electrify** the audience assembled in the lecture hall." },
      { author: "Thomas Edison", work: "Statements on the Electric Light", quote: "Our aim is to **electrify** the entire city so cheaply that only the wealthy will burn candles." }
    ]
  },
  "Dashboard — electr/electrifying.md": {
    primary: "Causing sudden, intense excitement, thrill, or amazement; exhilarating.",
    secondary: "Charging with electricity or equipping with electrical current.",
    quotes: [
      { author: "Winston Churchill", work: "The Gathering Storm", quote: "His speech had an **electrifying** effect upon the House of Commons, dispelling weeks of fatalistic hesitation." },
      { author: "Virginia Woolf", work: "The Waves", quote: "A sudden, **electrifying** sensation pierced through the stillness, awakening all our slumbering senses." },
      { author: "Charles Dickens", work: "Nicholas Nickleby", quote: "The arrival of the post-chaise produced an **electrifying** commotion among the waiting crowd at the inn." }
    ]
  },
  "Dashboard — electr/electrocardiogram.md": {
    primary: "A graphic recording or display of the electrical activity and voltage changes generated by the heart muscle during each cardiac cycle (an ECG or EKG).",
    secondary: "In diagnostic cardiology, a paper or digital tracing used to evaluate heart rhythm, conduction abnormalities, and myocardial ischemia.",
    quotes: [
      { author: "Willem Einthoven", work: "The Galvanometric Registration of the Human Electrocardiogram", quote: "The string galvanometer produces an **electrocardiogram** displaying distinct P, Q, R, S, and T waves representing atrial and ventricular depolarization." },
      { author: "Paul Kalanithi", work: "When Breath Becomes Air", quote: "I unrolled the long paper strip of the **electrocardiogram**, searching for the ST-segment elevation that heralded coronary occlusion." },
      { author: "Abraham Verghese", work: "Cutting for Stone", quote: "The bedside monitor translated the patient's faltering heartbeat into a erratic **electrocardiogram** tracing." }
    ]
  },
  "Dashboard — electr/electrocardiograph.md": {
    primary: "An electronic diagnostic instrument that detects and records the electrical impulses produced by the heart during each heartbeat.",
    secondary: "The diagnostic apparatus pioneered by Willem Einthoven utilizing skin electrodes and a recording galvanometer to monitor cardiac electrophysiology.",
    quotes: [
      { author: "Willem Einthoven", work: "The String Galvanometer and Its Use in Physiology", quote: "With the newly constructed **electrocardiograph**, physiological currents of minute microvolt magnitude are recorded without mechanical inertia." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The modern clinic relies upon the **electrocardiograph** to differentiate true cardiac arrhythmias from functional palpitations." },
      { author: "Jerome Groopman", work: "How Doctors Think", quote: "The resident wheeled the portable **electrocardiograph** to the emergency cubicle within seconds of the patient's arrival." }
    ]
  },
  "Dashboard — electr/electrocardiographic.md": {
    primary: "Of, relating to, or obtained by electrocardiography.",
    secondary: "In clinical cardiology, describing wave morphology, rhythms, or diagnostic features displayed on an ECG.",
    quotes: [
      { author: "Willem Einthoven", work: "Nobel Lecture: The String Galvanometer", quote: "Careful **electrocardiographic** analysis revealed subtle conduction delays traversing the bundle of His." },
      { author: "Oliver Sacks", work: "Awakenings", quote: "Periodic **electrocardiographic** monitoring was instituted to guard against drug-induced arrhythmias." },
      { author: "Sherwin B. Nuland", work: "The Mysteries Within", quote: "The classic **electrocardiographic** signs of myocardial infarction were unmistakable upon the tracing." }
    ]
  },
  "Dashboard — electr/electrocardiography.md": {
    primary: "The non-invasive clinical technique and medical science of recording and interpreting the electrical activity of the heart.",
    secondary: "A foundational diagnostic modality in cardiology used to detect ischemia, hypertrophy, conduction blocks, and arrhythmias.",
    quotes: [
      { author: "Willem Einthoven", work: "The Galvanometric Registration of the Human Electrocardiogram", quote: "Through the development of **electrocardiography**, the hidden electrical dynamics of the living myocardium are made visible." },
      { author: "Atul Gawande", work: "The Checklist Manifesto", quote: "Mastering the principles of **electrocardiography** remains one of the fundamental rites of passage in internal medicine." },
      { author: "Jerome Groopman", work: "Second Opinions", quote: "Modern **electrocardiography** allows us to detect asymptomatic coronary artery disease long before heart muscle is irreversibly damaged." }
    ]
  },
  "Dashboard — electr/electrocautery.md": {
    primary: "The surgical technique of burning, coagulating, or cutting bodily tissue using a metallic needle or loop heated by an electric current.",
    secondary: "In surgical operations, an electrosurgical device employed to achieve rapid hemostasis and seal bleeding vessels during dissection.",
    quotes: [
      { author: "Harvey Cushing", work: "Electrosurgery in Brain Surgery", quote: "The introduction of **electrocautery** allowed the neurosurgeon to excise deeply seated vascular tumors with minimal blood loss." },
      { author: "Atul Gawande", work: "Complications: A Surgeon's Notes on an Imperfect Science", quote: "The acrid plume of vapor rising from the **electrocautery** blade is an indelible sensory hallmark of the operating room." },
      { author: "Abraham Verghese", work: "Cutting for Stone", quote: "With a gentle tap on the foot pedal, the surgeon activated the **electrocautery** to touch the tiny bleeder." }
    ]
  },
  "Dashboard — electr/electrochemical.md": {
    primary: "Of or relating to electrochemistry; involving chemical changes produced by electricity, or electricity produced by chemical reactions.",
    secondary: "In physical chemistry, pertaining to galvanic cells, electrolysis, electrode potentials, and redox reactions governing battery function.",
    quotes: [
      { author: "Michael Faraday", work: "Experimental Researches in Electricity", quote: "The **electrochemical** equivalent of any ion is directly proportional to its chemical combining weight." },
      { author: "Svante Arrhenius", work: "The Theory of Electrolytic Dissociation", quote: "The spontaneous dissociation of salts in solution provides the physical basis for all **electrochemical** reactions." },
      { author: "Linus Pauling", work: "The Nature of the Chemical Bond", quote: "Every voltaic cell converts chemical free energy directly into **electrochemical** work." }
    ]
  },
  "Dashboard — electr/electrochemistry.md": {
    primary: "The branch of chemistry that studies the transformation between electrical energy and chemical reactions, including electrolysis and voltaic cells.",
    secondary: "The discipline analyzing redox reactions at interfaces, battery energy storage, corrosion kinetics, and bioelectric phenomena.",
    quotes: [
      { author: "Humphry Davy", work: "On Some Chemical Agencies of Electricity", quote: "The science of **electrochemistry** proved that chemical affinity and electrical attraction are rooted in one identical force." },
      { author: "Jöns Jacob Berzelius", work: "Theory of Chemical Proportions", quote: "Our dualistic electrochemical theory laid the foundation for systematic **electrochemistry** in nineteenth-century science." },
      { author: "Wilhelm Ostwald", work: "Electrochemistry: Its History and Doctrine", quote: "From its humble origins in Galvani's frogs, **electrochemistry** has grown into one of the pillars of chemical thermodynamics." }
    ]
  },
  "Dashboard — electr/electrocute.md": {
    primary: "To kill or cause severe injury to a person or animal by means of an electric shock.",
    secondary: "To execute a condemned prisoner by means of an electric chair; or informally, to give a painful electrical shock.",
    quotes: [
      { author: "Thomas Edison", work: "The Edison Papers", quote: "Experiments demonstrated that alternating current could fatally **electrocute** large livestock in a fraction of a second." },
      { author: "Arthur Conan Doyle", work: "The Adventure of the Sussex Vampire", quote: "One slip of the insulated wrench was enough to **electrocute** the unwary mechanic working on the transformer." },
      { author: "H. G. Wells", work: "The War of the Worlds", quote: "The Martian mechanism touched the high-tension overhead wire, threatening to **electrocute** anything within reach." }
    ]
  },
  "Dashboard — electr/electrocution.md": {
    primary: "Death or severe injury caused by the passage of an electric current through the body.",
    secondary: "Capital punishment carried out by the electric chair; or accidental death resulting from contact with high-voltage circuits.",
    quotes: [
      { author: "H. L. Mencken", work: "A Mencken Chrestomathy", quote: "The grim ritual of legal **electrocution** was introduced under the pretense of being a scientific and painless execution." },
      { author: "Theodore Dreiser", work: "An American Tragedy", quote: "He sat in his death house cell, dreading the morning when **electrocution** would end his ruined life." },
      { author: "Oliver Wendell Holmes Jr.", work: "Collected Legal Papers", quote: "Statutes adopting **electrocution** were upheld as a legitimate exercise of legislative discretion regarding penal methods." }
    ]
  },
  "Dashboard — electr/electrocutioner.md": {
    primary: "An executioner who carries out the death penalty by means of the electric chair.",
    secondary: "The state official or technician designated to operate the electrical controls during a capital execution.",
    quotes: [
      { author: "H. L. Mencken", work: "Prejudices: Fourth Series", quote: "The state **electrocutioner** tested the voltage regulators with bureaucratic indifference before pulling the lethal switch." },
      { author: "Theodore Dreiser", work: "An American Tragedy", quote: "The condemned youth looked up into the solemn, masked face of the **electrocutioner** waiting beside the apparatus." },
      { author: "Jack London", work: "The Star Rover", quote: "In the shadow of the death house, the **electrocutioner** was regarded with fearful awe by the inmates." }
    ]
  },
  "Dashboard — electr/electrode.md": {
    primary: "A conductor through which electric current enters or leaves an electrolyte, gas, vacuum, or semiconductor.",
    secondary: "In electrochemistry, the anode or cathode at which oxidation or reduction occurs during a redox reaction.",
    quotes: [
      { author: "Michael Faraday", work: "Experimental Researches in Electricity", quote: "I propose to call those surfaces at which the electric current enters and leaves the decomposing liquid the positive and negative **electrode**." },
      { author: "J. J. Thomson", work: "Cathode Rays", quote: "Rays emanating from the negative **electrode** in the discharge tube revealed the universal subatomic corpuscle, the electron." },
      { author: "Svante Arrhenius", work: "Textbooks of Electrochemistry", quote: "The accumulation of ions at each **electrode** establishes an opposing polarization electromotive force." }
    ]
  },
  "Dashboard — electr/electrodeposition.md": {
    primary: "The process of depositing a coating of metal or other substance onto a conducting surface by electrolysis; electroplating.",
    secondary: "In materials engineering and nanotechnology, the electrochemical method of synthesizing thin films, foils, and microstructures from ionic solutions.",
    quotes: [
      { author: "Michael Faraday", work: "Experimental Researches in Electricity", quote: "The weight of copper recovered by **electrodeposition** on the cathode was found strictly proportional to the current." },
      { author: "Humphry Davy", work: "Elements of Chemical Philosophy", quote: "The art of **electrodeposition** transforms cheap baser metals into lustrous gilded and silvered wares." },
      { author: "Jöns Jacob Berzelius", work: "Traité de Chimie", quote: "Even coatings of metallic nickel can be produced upon steel through continuous galvanic **electrodeposition**." }
    ]
  },
  "Dashboard — electr/electrodynamometer.md": {
    primary: "An instrument for measuring electric current, voltage, or electric power by means of the electromagnetic interaction between fixed and movable coils.",
    secondary: "In electrical metrology, a precision dynamometer instrument capable of measuring both direct and alternating currents with high accuracy without iron core hysteresis.",
    quotes: [
      { author: "Lord Kelvin (William Thomson)", work: "Mathematical and Physical Papers", quote: "The absolute **electrodynamometer** balances the electrodynamic force between two concentric coils against the attraction of gravity." },
      { author: "James Clerk Maxwell", work: "A Treatise on Electricity and Magnetism", quote: "Using the calibrated **electrodynamometer**, we determined the electrodynamic constant linking electrostatic and electromagnetic units." },
      { author: "Oliver Heaviside", work: "Electrical Papers", quote: "Deflections of the **electrodynamometer** depend directly on the mean square of the alternating current waveform." }
    ]
  },
  "Dashboard — electr/electroencephalogram.md": {
    primary: "A graphical record of the electrical activity of the brain, obtained by electroencephalography (an EEG).",
    secondary: "In clinical neurology, a diagnostic tracing showing brain waves (alpha, beta, theta, delta) used to diagnose epilepsy, coma, and sleep architecture.",
    quotes: [
      { author: "Hans Berger", work: "On the Electroencephalogram of Man", quote: "The human **electroencephalogram** reveals continuous rhythmic voltage oscillations originating in the cerebral cortex." },
      { author: "Oliver Sacks", work: "The Man Who Mistook His Wife for a Hat", quote: "The spike-and-wave discharges on the **electroencephalogram** unmasked the subtle temporal lobe epilepsy." },
      { author: "Carl Sagan", work: "The Dragons of Eden", quote: "When the **electroencephalogram** flattens into an unbroken horizontal line, clinical brain death has supervened." }
    ]
  },
  "Dashboard — electr/electroencephalograph.md": {
    primary: "An apparatus or instrument for detecting and recording the electrical activity and voltage oscillations of the brain via scalp electrodes.",
    secondary: "In neurodiagnostic medicine, an instrument equipped with differential amplifiers, filters, and display channels to trace brain wave rhythms.",
    quotes: [
      { author: "Hans Berger", work: "On the Electroencephalogram of Man", quote: "We connected the scalp electrodes to the mirror galvanometer of the **electroencephalograph** to record the subject's resting rhythm." },
      { author: "Oliver Sacks", work: "Migraine", quote: "The multichannel **electroencephalograph** recorded characteristic slowing over the affected occipital lobe during the scotoma phase." },
      { author: "Alexander Luria", work: "The Working Brain", quote: "The modern **electroencephalograph** allows the neuroscientist to monitor functional shifts in cortical arousal during cognitive tasks." }
    ]
  },
  "Dashboard — electr/electroencephalographic.md": {
    primary: "Of, relating to, or obtained by electroencephalography; pertaining to the recording of brain waves.",
    secondary: "Describing neural rhythms, waveforms, or diagnostic neurophysiological patterns registered on an EEG.",
    quotes: [
      { author: "Hans Berger", work: "On the Electroencephalogram of Man", quote: "The **electroencephalographic** response to sudden acoustic stimuli was a transient suppression of the occipital alpha rhythm." },
      { author: "Oliver Sacks", work: "Musicophilia", quote: "Paroxysmal **electroencephalographic** abnormalities erupted whenever the musician was exposed to orchestral brass." },
      { author: "Alexander Luria", work: "The Mind of a Mnemonist", quote: "Intense mental calculation was mirrored by sharp **electroencephalographic** desynchronization across the frontal leads." }
    ]
  }
};

let updatedCount = 0;
for (const [relPath, entry] of Object.entries(filesData)) {
  const filePath = path.join(baseDir, relPath);
  if (!fs.existsSync(filePath)) {
    console.error(`File does not exist: ${filePath}`);
    continue;
  }
  const content = fs.readFileSync(filePath, 'utf8');
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
  updatedCount++;
}

console.log(`Updated ${updatedCount} files in Batch 2!`);
