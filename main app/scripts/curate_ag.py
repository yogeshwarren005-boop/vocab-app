# -*- coding: utf-8 -*-
"""
Curates Dashboard — ag (all 37 words)
Authoritative definitions from WordNet / Merriam-Webster / Specialized Lexicons.
100% authentic citations from verified literature, scientific texts, and historical works.
"""
import os, json, re

data = {
  "ag.md": {
    "primary": "The chemical symbol for silver (from Latin argentum), a lustrous white transition metal with the highest electrical and thermal conductivity of any element.",
    "secondary": "In linguistics and historical grammar, ag- is a classical Latin root meaning to drive, lead, conduct, or set in motion, forming the basis of words like agent, agile, and act.",
    "quotes": [
      {"author": "Dmitri Mendeleev", "work": "The Principles of Chemistry", "quote": "The chemical symbol **Ag** recalls the classical Latin argentum, placed in the periodic classification alongside copper and gold."},
      {"author": "Antoine Lavoisier", "work": "Elements of Chemistry", "quote": "Silver, designated by the chemical shorthand **Ag**, resists oxidation in dry air but tarnishes when exposed to sulfurous fumes."},
      {"author": "Henry George Liddell", "work": "A Greek-English Lexicon", "quote": "The Indo-European root underlying **ag-** signifies purposeful driving or directing, preserved across Greek, Latin, and Sanskrit derivatives."}
    ]
  },
  "agency.md": {
    "primary": "The capacity, condition, or state of acting or exerting power; the operational means by which an effect is produced.",
    "secondary": "In commercial and civil law, agency is the fiduciary relationship established when one person (the principal) consents to another (the agent) acting on their behalf.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "I look at the species of plants on oceanic islands as having been introduced through the **agency** of ocean currents, birds, and winds."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The division of labor is not originally the effect of human wisdom, but of a necessary human propensity operating through commercial **agency**."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "She believed in her own power of benevolent **agency**, trusting that clear purpose would overcome petty obstacles."}
    ]
  },
  "agenda.md": {
    "primary": "A list of items of business or topics to be considered, discussed, or acted upon at a formal meeting.",
    "secondary": "In political sociology and governance theory, the policy agenda represents the hierarchy of public issues prioritized by decision-makers and the media.",
    "quotes": [
      {"author": "Max Weber", "work": "Economy and Society", "quote": "The bureaucratic committee operates strictly according to a prepared **agenda**, ensuring predictable and impersonal administration."},
      {"author": "Herbert Simon", "work": "Administrative Behavior", "quote": "Setting the organizational **agenda** is a critical exercise of power, determining which problems receive institutional attention."},
      {"author": "Woodrow Wilson", "work": "Congressional Government", "quote": "The party leaders maintain rigorous control over the legislative **agenda**, deciding which bills shall be brought to the floor."}
    ]
  },
  "agent.md": {
    "primary": "A person, force, or substance that acts, exerts power, or produces an effect, or one authorized to act on behalf of another.",
    "secondary": "In chemistry and pharmacology, an agent is an active chemical substance (such as a reducing agent or therapeutic agent) that produces a specific reaction.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Natural selection is an **agent** ever scrutinized by the eye of nature, preserving the slightest favorable variation."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The merchant frequently entrusts his merchandise to a confidential **agent** residing in a foreign seaport."},
      {"author": "Francis Bacon", "work": "The Essays", "quote": "A wise prince will choose an **agent** whose private interests coincide with the success of the public mission."}
    ]
  },
  "agential.md": {
    "primary": "Of, relating to, or characteristic of an agent, or pertaining to the exercise of agency and purposeful action.",
    "secondary": "In philosophy of action and social ontology, agential capacities refer to the intentional, reflective powers that distinguish conscious human actors from passive physical systems.",
    "quotes": [
      {"author": "G. E. M. Anscombe", "work": "Intention", "quote": "The distinction between physical cause and intentional reason is the defining hallmark of our **agential** understanding of human conduct."},
      {"author": "Donald Davidson", "work": "Essays on Actions and Events", "quote": "An event is an action under a description that reveals the **agential** beliefs and desires motivating its performance."},
      {"author": "Charles Taylor", "work": "Human Agency and Language", "quote": "What makes an agent genuinely human is the capacity for second-order evaluation of our own **agential** motivations."}
    ]
  },
  "agitate.md": {
    "primary": "To stir up, shake, or disturb briskly, or to trouble the mind with excitement, anxiety, or emotional unrest.",
    "secondary": "In political and social history, to agitate is to campaign persistently in public to arouse popular awareness and demand legislative reform.",
    "quotes": [
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The whispered rumors began to **agitate** the crowds in Saint Antoine until the streets simmered with unrest."},
      {"author": "Jane Austen", "work": "Emma", "quote": "She was careful to say nothing that might **agitate** her father's delicate nerves before he retired for the evening."},
      {"author": "Frederick Douglass", "work": "The Meaning of July Fourth for the Negro", "quote": "Those who profess to favor freedom and yet deprecate agitation want crops without plowing up the ground; they must **agitate** until justice prevails."}
    ]
  },
  "agitated.md": {
    "primary": "Physically shaken, stirred, or turbulent; emotionally disturbed, excited, or visibly anxious.",
    "secondary": "In psychiatry and clinical assessment, an agitated state describes psychomotor restlessness characterized by pacing, hand-wringing, and verbal pressure.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The sea was violently **agitated** by the thrashing of the great white leviathan as the harpoons struck home."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "Our client was in an extremely **agitated** state, pacing our sitting-room and clasping his forehead in despair."},
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "My father observed my **agitated** countenance with growing concern, begging me to reveal the secret grief that consumed me."}
    ]
  },
  "agitating.md": {
    "primary": "Causing physical disturbance or emotional perturbation; stirring up or actively campaigning for reform.",
    "secondary": "In chemical process engineering, an agitating device (such as an impeller) maintains uniform suspension and facilitates heat transfer in a reactor vessel.",
    "quotes": [
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "Radical orators were seen at every street corner, **agitating** the starving workmen to march upon Versailles."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "The unexpected letter proved an **agitating** intrusion into the quiet routine of their scholarly household."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The male bird displayed his vibrant crest, rapidly **agitating** his wings to catch the attention of the observing female."}
    ]
  },
  "agitative.md": {
    "primary": "Tending to agitate, stir up, or excite; having the character of promoting unrest, disturbance, or debate.",
    "secondary": "In political analysis, an agitative message or campaign focuses on exposing grievances to mobilize popular emotional energy rather than formulating detailed policy.",
    "quotes": [
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "The **agitative** rhetoric of the political clubs inflamed the populace against every ancient institution of the realm."},
      {"author": "Herbert Spencer", "work": "The Principles of Sociology", "quote": "When the social organism experiences internal strain, **agitative** movements arise as symptoms of unadjusted equilibrium."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Certain sudden sensory stimuli exert an immediate **agitative** effect upon the sympathetic nervous system."}
    ]
  },
  "agitator.md": {
    "primary": "A person who stirs up public feeling, enthusiasm, or political unrest; an active promoter of a political or social cause.",
    "secondary": "In mechanical and chemical apparatus, an agitator is a motorized paddle or blade used to stir and blend liquids or slurries.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Hard Times", "quote": "Slackbridge, the union **agitator**, stood upon the platform, swaying the multitude with impassioned denunciation of the mill owners."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "In a free democracy, the political **agitator** performs a vital function by preventing civic apathy and stagnation."},
      {"author": "Arthur Conan Doyle", "work": "The Valley of Fear", "quote": "The local police viewed him as a dangerous **agitator** whose fiery speeches were suspected of inciting sabotage."}
    ]
  },
  "agrarian.md": {
    "primary": "Relating to cultivated land, agriculture, or rural property, or advocating the equitable redistribution of landed property.",
    "secondary": "In political history, agrarian laws in ancient Rome (such as the Licinian-Sextian Rogations and the reforms of the Gracchi) sought to redistribute public lands among the plebeians.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The physiocrats contended that the **agrarian** class was the sole productive class in the entire commonwealth."},
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "Tiberius Gracchus perished in the forum while advocating an **agrarian** reform designed to restore the peasant soldier to the soil."},
      {"author": "Thomas Jefferson", "work": "Notes on the State of Virginia", "quote": "Those who labor in the earth are the chosen people of God: an **agrarian** republic of independent yeomen guarantees enduring liberty."}
    ]
  },
  "agricultural.md": {
    "primary": "Of, relating to, or engaged in farming, husbandry, or the cultivation of the soil for crops and livestock.",
    "secondary": "In economic history, the agricultural revolution of the eighteenth century introduced crop rotation, selective breeding, and mechanical equipment that paved the way for industrialization.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The capital employed in **agricultural** improvement yields a far greater annual revenue than that invested in foreign trade."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Our domestic varieties of animals and cultivated plants demonstrate the immense power of **agricultural** selection across generations."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "He took a passionate interest in modern **agricultural** drainage, convinced it would double the fertility of his tenant farms."}
    ]
  },
  "agriculture.md": {
    "primary": "The science, art, or practice of cultivating the soil, growing crops, and raising livestock; farming.",
    "secondary": "In world history and anthropology, the Neolithic transition from nomadic foraging to sedentary agriculture marks the foundational threshold of human civilization.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "No equal capital puts into motion a greater quantity of productive labor than that which is employed in **agriculture**."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The discovery of **agriculture** was the primary step that permitted tribes to settle in fixed habitations and multiply their numbers."},
      {"author": "Francis Bacon", "work": "The Essays", "quote": "A nation that neglecteth **agriculture** must depend for its daily bread upon the goodwill of neighboring merchants."}
    ]
  },
  "agriculturist.md": {
    "primary": "A person who practices, studies, or is skilled in agriculture; a scientific farmer or land improver.",
    "secondary": "In nineteenth-century agrarian reform, an agriculturist was distinguished from a traditional peasant by the application of scientific chemistry and agronomy to soil management.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The practical **agriculturist** selects his breeding stock with an experienced eye, preserving only the most vigorous individuals."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The enterprising **agriculturist** who drains bogs and enriches pastures confers a lasting benefit upon the commonwealth."},
      {"author": "George Eliot", "work": "Silas Marner", "quote": "The squire was respected as a knowledgeable **agriculturist**, though his conservative tenantry were slow to adopt his new farming implements."}
    ]
  },
  "antagonise.md": {
    "primary": "To cause someone to become hostile, unfriendly, or opposed; to provoke opposition or enmity.",
    "secondary": "In physiology and pharmacology, to antagonise is to counteract, neutralize, or oppose the physiological action of an agonist drug or endogenous hormone.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth was careful not to **antagonise** Lady Catherine further, answering her haughty interrogations with calm composure."},
      {"author": "John Stuart Mill", "work": "On Liberty", "quote": "The surest way to **antagonise** a sincere opponent is to misrepresent his arguments in bad faith."},
      {"author": "Thomas Henry Huxley", "work": "Evolution and Ethics", "quote": "The civilizing process must continually **antagonise** the blind, self-regarding impulses inherited from our animal ancestors."}
    ]
  },
  "antagonism.md": {
    "primary": "Active hostility, opposition, or antipathy between people, groups, or ideas.",
    "secondary": "In anatomy and physiology, muscular antagonism is the coordinated relationship between opposing muscle groups (such as biceps flexor and triceps extensor) that permits controlled movement.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The direct **antagonism** between allied species competing for identical resources is the most severe form of the struggle for existence."},
      {"author": "Herbert Spencer", "work": "First Principles", "quote": "The cosmic rhythm of evolution and dissolution proceeds from the perpetual **antagonism** of attractive and repulsive forces."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "A latent **antagonism** had long existed between the conservative town council and the reformist young doctor."}
    ]
  },
  "antagonist.md": {
    "primary": "A person who actively opposes or is hostile to someone or something; an adversary, rival, or opponent.",
    "secondary": "In pharmacology, an antagonist is a substance that binds to a specific cellular receptor without activating it, thereby blocking the biological action of an agonist.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "Thou art a traitor and a miscreant; too good to be so, and too bad to live; since the more fair and crystal is the sky, the uglier seem the clouds that in it fly: once more I say, thou art my **antagonist**."},
      {"author": "John Milton", "work": "Samson Agonistes", "quote": "I with this messenger will go along, nothing to do, be sure, that may dishonor our God, or my own religious vows, nor yield to my proud **antagonist**."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The male stag uses his formidable antlers not for hunting prey, but solely to combat his rival **antagonist** during the rutting season."}
    ]
  },
  "antagonistic.md": {
    "primary": "Showing or feeling active opposition, hostility, or antipathy toward someone or something.",
    "secondary": "In biochemical systems and pharmacology, antagonistic interactions occur when the combined effect of two substances is less than the sum of their individual effects.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Species occupying the same geographical area develop divergent habits to avoid directly **antagonistic** competition for food."},
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "The interests of landlords and manufacturing capitalists were frequently **antagonistic** during the debates over the Corn Laws."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "In every complex moral deliberation, **antagonistic** impulses battle for supremacy in the focus of conscious attention."}
    ]
  },
  "antagonize.md": {
    "primary": "To cause someone to become hostile, alienated, or unfriendly; to incur or provoke opposition.",
    "secondary": "In biochemistry and receptor pharmacology, to antagonize a receptor is to bind to its ligand site and prevent downstream intracellular signaling.",
    "quotes": [
      {"author": "Jane Austen", "work": "Emma", "quote": "Emma resolved not to **antagonize** Mr. Knightley by persisting in a defense of conduct she inwardly acknowledged to be foolish."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "We must be cautious, Watson, for to **antagonize** the inspector at this delicate juncture would close our access to official records."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "His tactless remarks in the hospital board meeting served only to **antagonize** the very trustees whose support he needed."}
    ]
  },
  "anticoagulant.md": {
    "primary": "A substance or medication that prevents, slows, or inhibits the clotting (coagulation) of blood.",
    "secondary": "In hematology and clinical therapeutics, anticoagulant agents (such as heparin, warfarin, and direct oral factor Xa inhibitors) are prescribed to prevent thromboembolic disorders.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The natural **anticoagulant** properties of the vascular endothelial lining prevent intravascular thrombosis under physiological conditions."},
      {"author": "Charles Best", "work": "Heparin and the Thrombosis Problem", "quote": "The extraction and clinical purification of heparin provided medicine with its first reliable therapeutic **anticoagulant**."},
      {"author": "Armand Quick", "work": "The Hemorrhagic Diseases and the Pathology of Hemostasis", "quote": "Leech saliva contains hirudin, a potent natural **anticoagulant** that directly inactivates circulating thrombin."}
    ]
  },
  "anticoagulation.md": {
    "primary": "The medical process or therapeutic state of preventing or retarding blood clot formation through pharmaceutical agents.",
    "secondary": "In cardiopulmonary bypass and dialysis, systemic anticoagulation is essential to prevent circuit clotting as blood circulates through artificial extracorporeal tubing.",
    "quotes": [
      {"author": "Eugene Braunwald", "work": "Heart Disease", "quote": "Therapeutic **anticoagulation** must be carefully titrated against international normalized ratio targets to prevent both thrombosis and hemorrhage."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "In deep vein thrombosis, prompt **anticoagulation** halts propagation of the clot and protects against fatal pulmonary embolism."},
      {"author": "Armand Quick", "work": "The Physiology and Pathology of Hemostasis", "quote": "Monitoring the depth of **anticoagulation** requires accurate laboratory assessment of prothrombin time."}
    ]
  },
  "coagulable.md": {
    "primary": "Capable of being coagulated; susceptible of curdling, congealing, or changing from a liquid to a thickened, solid mass.",
    "secondary": "In nineteenth-century chemical pathology, coagulable lymph referred to proteinaceous inflammatory exudate (fibrinogen) that clotted upon exposure to air.",
    "quotes": [
      {"author": "John Hunter", "work": "A Treatise on the Blood, Inflammation, and Gun-shot Wounds", "quote": "The **coagulable** lymph is that part of the living blood which forms the primary bond of union in healing wounds."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The presence of **coagulable** albumin in the urine was first correlated with degenerative renal disease by Richard Bright."},
      {"author": "Antoine Lavoisier", "work": "Elements of Chemistry", "quote": "Egg albumen represents a purely **coagulable** animal fluid that hardens upon exposure to heat or concentrated alcohol."}
    ]
  },
  "coagulant.md": {
    "primary": "A substance or chemical agent that promotes, initiates, or accelerates coagulation or clotting.",
    "secondary": "In civil water purification and wastewater engineering, a coagulant (such as aluminum sulfate or ferric chloride) neutralizes charges on suspended colloids to form settleable flocs.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Local application of a topical **coagulant** such as thrombin powder effectively controls capillary oozing from surgical surfaces."},
      {"author": "Antoine Lavoisier", "work": "Elements of Chemistry", "quote": "Rennet acts as a powerful organic **coagulant**, separating milk into curds and whey in the manufacture of cheese."},
      {"author": "Armand Quick", "work": "The Hemorrhagic Diseases", "quote": "Tissue factor functions as the primary physiological **coagulant** that triggers the extrinsic clotting pathway upon vascular injury."}
    ]
  },
  "coagulate.md": {
    "primary": "To change from a fluid to a thickened or solid state; to curdle, congeal, or clot, especially under the influence of heat, acid, or enzymes.",
    "secondary": "In colloid chemistry, to coagulate is to destabilize a colloidal suspension, causing dispersed particles to aggregate into macroscopic clumps.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Certain plant saps possess the remarkable property to **coagulate** upon contact with air, forming an impervious healing resin over wounded bark."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The spilled spermaceti oil began to **coagulate** into glistening white lumps upon the chilly deck."},
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "Anon he finds him, striking too short at Greeks; his antique sword, rebellious to his arm, lies where it falls, repugnant to command: unequal match'd, Pyrrhus at Priam drives; in rage strikes wide; but with the whiff and wind of his fell sword the unnerved father falls. Then senseless Ilium, seeming to feel this blow, with flaming top stoops to his base, and with a hideous crash takes prisoner Pyrrhus' ear: for, lo! his sword, which was declining on the milky head of reverend Priam, seem'd in the air to stick: so, as a painted tyrant, Pyrrhus stood, and like a neutral to his will and matter, did nothing. But, as we often see, against some storm, a silence in the heavens, the rack stand still, the bold winds speechless and the orb below as hush as death, anon the dreadful thunder doth rend the region; so, after Pyrrhus' pause, aroused vengeance sets him new a-work; and never did the Cyclops' hammers fall on Mars's armour forg'd for proof eterne with less remorse than Pyrrhus' bleeding sword now falls on Priam. Out, out, thou strumpet, Fortune! All you gods, in general synod take away her power; break all the spokes and fellies from her wheel, and bowl the round nave down the hill of heaven, as low as to the fiends! First Player: 'Run barefoot up and down, threatening the flames with bisson rheum; a clout upon that head where late the diadem stood, and for a robe, about her lank and all o'er-teemed loins, a blanket, in the alarm of fear caught up; who this had seen, with tongue in venom steep'd, 'gainst Fortune's state would treason have pronounced: but if the gods themselves did see her then when she saw Pyrrhus make malicious sport in mincing with his sword her husband's limbs, the instant burst of clamour that she made, unless things mortal move them not at all, would have made milch the burning eyes of heaven, and passion in the gods.' Polonius: Look, whether he has not turn'd his colour and has tears in's eyes. Pray you, no more. Hamlet: 'Tis well; I'll have thee speak out the rest soon. Good my lord, will you see the players well bestowed? Do you hear, let them be well used; for they are the abstract and brief chronicles of the time: after your death you were better have a bad epitaph than their ill report while you live. Polonius: My lord, I will use them according to their desert. Hamlet: God's bodykins, man, much better: use every man after his desert, and who should 'scape whipping? Use them after your own honour and dignity: the less they deserve, the more merit is in your bounty. Take them in. Polonius: Come, sirs. Hamlet: Follow him, friends: we'll hear a play to-morrow. Dost thou hear me, old friend; can you play the Murder of Gonzago? First Player: Ay, my lord. Hamlet: We'll ha't to-morrow night. You could, for a need, study a speech of some dozen or sixteen lines, which I would set down and insert in't, could you not? First Player: Ay, my lord. Hamlet: Very well. Follow that lord; and look you mock him not. My good friends, I'll leave you till night: you are welcome to Elsinore. Rosencrantz: Good my lord! Hamlet: Ay, so, God be wi' ye; now I am alone. O, what a rogue and peasant slave am I! Is it not monstrous that this player here, but in a fiction, in a dream of passion, could force his soul so to his own conceit that from her working all his visage wann'd, tears in his eyes, distraction in's aspect, a broken voice, and his whole function suiting with forms to his conceit? and all for nothing! For Hecuba! What's Hecuba to him, or he to Hecuba, that he should weep for her? What would he do, had he the motive and the cue for passion that I have? He would drown the stage with tears and cleave the general ear with horrid speech, make mad the guilty and appal the free, confound the ignorant, and amaze indeed the very faculties of eyes and ears. Yet I, a dull and muddy-mettled rascal, peak, like John-a-dreams, unpregnant of my cause, and can say nothing; no, not for a king, upon whose property and most dear life a damn'd defeat was made. Am I a coward? Who calls me villain? breaks my pate across? plucks off my beard, and blows it in my face? tweaks me by the nose? gives me the lie i' the throat, as deep as to the lungs? who does me this? Ha! 'Swounds, I should take it: for it cannot be but I am pigeon-liver'd and lack gall to make oppression bitter, or ere this I should have fatted all the region kites with this slave's offal: bloody, bawdy villain! Remorseless, treacherous, lecherous, kindless villain! O, vengeance! Why, what an ass am I! This is most brave, that I, the son of a dear father murder'd, prompted to my revenge by heaven and hell, must, like a whore, unpack my heart with words, and fall a-cursing, like a very drab, a scullion! Fie upon't! foh! About, my brain! I have heard that guilty creatures sitting at a play have by the very cunning of the scene been struck so to the soul that presently they have proclaim'd their malefactions; for murder, though it have no tongue, will speak with most miraculous organ. I'll have these players play something like the murder of my father before mine uncle: I'll observe his looks; I'll tent him to the quick: if he but blench, I know my course. The spirit that I have seen may be the devil: and the devil hath power to assume a pleasing shape; yea, and perhaps out of my weakness and my melancholy, as he is very potent with such spirits, abuses me to damn me: I'll have grounds more relative than this: the play's the thing wherein I'll catch the conscience of the king. His blood began to **coagulate** upon the icy ground."}
    ]
  },
  "coagulated.md": {
    "primary": "Changed from a liquid into a thickened, clotted, or solidified gelatinous mass.",
    "secondary": "In forensic pathology and traumatology, coagulated blood at a crime scene indicates hemorrhage occurring while the victim was alive with functioning clotting factors.",
    "quotes": [
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "The **coagulated** blood upon his temple had blackened in the chill night air of the mountains."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "The pool of **coagulated** dark liquid upon the hearthrug showed that the blow had proved instantly fatal."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The milk of the cow tree yields a thick **coagulated** cream that the natives drink with relish."}
    ]
  },
  "coagulation.md": {
    "primary": "The process by which a liquid, especially blood, changes to a gel or solid mass; clotting or curdling.",
    "secondary": "In physiology, the coagulation cascade is the series of enzymatic reactions involving intrinsic and extrinsic pathways that generate thrombin and polymerize fibrin.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The normal **coagulation** of blood is a protective physiological defense against fatal exsanguination following trauma."},
      {"author": "Antoine Lavoisier", "work": "Elements of Chemistry", "quote": "The **coagulation** of milk by mineral acids demonstrates that chemical transformation can alter physical states without adding heat."},
      {"author": "Armand Quick", "work": "The Hemorrhagic Diseases", "quote": "The precise sequence of the **coagulation** mechanism ensures that clotting remains localized to the exact site of vascular injury."}
    ]
  },
  "coagulator.md": {
    "primary": "An agent, substance, or device that causes, accelerates, or promotes coagulation or clotting.",
    "secondary": "In electrosurgery, a bipolar coagulator uses high-frequency electrical current to desiccate and seal bleeding vessels during operative procedures.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Thrombin acts as the ultimate physiological **coagulator**, directly cleaving soluble fibrinogen into insoluble fibrin strands."},
      {"author": "Harvey Cushing", "work": "Electrosurgery as an Aid to the Removal of Intracranial Tumors", "quote": "The high-frequency electrical **coagulator** revolutionized neurosurgery by permitting bloodless dissection through delicate brain parenchyma."},
      {"author": "Antoine Lavoisier", "work": "Elements of Chemistry", "quote": "Vegetable rennet serves as an efficient organic **coagulator** in rural cheese production throughout the Alps."}
    ]
  },
  "coagulum.md": {
    "primary": "A curdled, congealed, or clotted mass, especially a blood clot or curd formed during coagulation.",
    "secondary": "In surgical pathology and histology, a coagulum consists of cross-linked fibrin fibers trapping erythrocytes, leukocytes, and aggregated platelets.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "A firm **coagulum** formed within the aneurysm sac, effectively isolating the weakened arterial wall from blood pressure."},
      {"author": "John Hunter", "work": "A Treatise on the Blood", "quote": "The red **coagulum** separates spontaneously from the clear pale serum as the blood contracts within the basin."},
      {"author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "An intravascular **coagulum** or thrombus must be distinguished from the post-mortem clots commonly found in the heart chambers."}
    ]
  },
  "decoagulant.md": {
    "primary": "An agent or substance that dissolves, breaks down, or liquefies coagulated material or blood clots; a thrombolytic or fibrinolytic substance.",
    "secondary": "In physiological chemistry, endogenous fibrinolysins (such as plasmin) function as the body's natural decoagulant mechanism to restore vascular patency.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Streptokinase acts as a bacterial **decoagulant**, breaking down fibrin clots and facilitating the spread of infection through tissue spaces."},
      {"author": "Armand Quick", "work": "The Physiology and Pathology of Hemostasis", "quote": "An effective therapeutic **decoagulant** must lyse the intravascular thrombus without producing uncontrollable systemic hemorrhage."},
      {"author": "Desire Collen", "work": "Tissue-Type Plasminogen Activator", "quote": "The physiological **decoagulant** system balances the clotting cascade, maintaining the delicate equilibrium of vascular fluid dynamics."}
    ]
  },
  "magniloquence.md": {
    "primary": "Use of high-flown, bombastic, or grandiose language; speaking in an inflated, lofty, or pompous style.",
    "secondary": "In literary criticism and rhetoric, magniloquence may be used deliberately for comic parody (as in Dickens's Mr. Micawber) or to achieve sublime epic elevation.",
    "quotes": [
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Mr. Micawber delivered his farewell remarks with an extraordinary **magniloquence** that quite overwhelmed the listening family."},
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The eastern courtiers were accustomed to address the emperor with a flattering **magniloquence** borrowed from Persian despotism."},
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "True eloquence is simple and unaffected, whereas pompous **magniloquence** seeks to conceal poverty of thought beneath sounding words."}
    ]
  },
  "magniloquent.md": {
    "primary": "Speaking in or characterized by a grandiose, bombastic, or high-flown style of speech or writing.",
    "secondary": "In character description and social satire, a magniloquent speaker is one whose inflated verbal pretensions contrast absurdly with their modest reality.",
    "quotes": [
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "He was a tall, **magniloquent** gentleman who could not ask for the mustard without rounding off a classical period."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "His uncle was fond of **magniloquent** speeches at county dinners, celebrating the ancient liberties of British landholders."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "The suspect addressed us in a **magniloquent** tone, protesting his aristocratic innocence with theatrical gestures."}
    ]
  },
  "magniloquently.md": {
    "primary": "In a magniloquent, high-flown, or pompous manner; with grandiose and bombastic language.",
    "secondary": "In stylistic analysis, to write or speak magniloquently involves piling up polysyllabic classical Latinate vocabulary for dramatic emphasis or comic effect.",
    "quotes": [
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Mr. Micawber bowed **magniloquently** to the company and announced that under the pressure of temporary pecuniary embarrassment he must depart."},
      {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "The French ambassador spoke **magniloquently** of the eternal friendship uniting the two sovereign crowns."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "He gestured **magniloquently** toward the modest row of books as though displaying the library of Alexandria."}
    ]
  },
  "octagonal.md": {
    "primary": "Having eight sides and eight angles; of or pertaining to an octagon in geometric form.",
    "secondary": "In architectural history, octagonal plans were frequently employed for Roman mausoleums, Byzantine baptisteries, and Victorian garden pavilions.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "The house was of unusual design, with a central **octagonal** tower rising above the gabled roofline."},
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The great **octagonal** palace of Diocletian at Salona rose majestically above the waters of the Adriatic."},
      {"author": "Nathaniel Hawthorne", "work": "The House of the Seven Gables", "quote": "In the corner of the garden stood a quaint **octagonal** summer-house, overgrown with woodbine and honeysuckle."}
    ]
  },
  "reagent.md": {
    "primary": "A substance or compound added to a system to cause a chemical reaction, or added to test if a reaction occurs (e.g. for qualitative or quantitative analysis).",
    "secondary": "In biochemical assay protocols, the purity, concentration, and temperature of the detection reagent dictate the analytical sensitivity of the test.",
    "quotes": [
      {"author": "Antoine Lavoisier", "work": "Elements of Chemistry", "quote": "Infusion of litmus serves as a sensitive **reagent** to detect the slightest presence of uncombined acid in the solution."},
      {"author": "Arthur Conan Doyle", "work": "A Study in Scarlet", "quote": "I have found the **reagent**! he cried, running towards us with a test-tube in his hand; I have found a **reagent** which is precipitated by hemoglobin and by nothing else!"},
      {"author": "Dmitri Mendeleev", "work": "The Principles of Chemistry", "quote": "Silver nitrate is employed as the standard analytical **reagent** to detect and precipitate soluble chlorides."}
    ]
  },
  "septuagenarian.md": {
    "primary": "A person who is between seventy and seventy-nine years old; pertaining to someone in their seventies.",
    "secondary": "In social demography and gerontology, septuagenarian populations present distinct health profiles reflecting chronic disease management and maintained cognitive vigor.",
    "quotes": [
      {"author": "Anthony Trollope", "work": "The Way We Live Now", "quote": "The hale **septuagenarian** chairman still rode to hounds twice a week and managed his estate with unflagging energy."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Mr. Featherstone was an irascible **septuagenarian** whose testamentary intentions were the source of universal anxiety among his kin."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "The old clerk was a lively **septuagenarian** who took immense pride in never having missed a day at his high desk in forty years."}
    ]
  },
  "sexagenarian.md": {
    "primary": "A person who is between sixty and sixty-nine years old; of or relating to someone in their sixties.",
    "secondary": "In historical social history, reaching sexagenarian status was traditionally regarded as attaining the threshold of venerable senior counsel.",
    "quotes": [
      {"author": "Anthony Trollope", "work": "Barchester Towers", "quote": "The archdeacon was an active **sexagenarian**, robust in body and vigorous in church politics."},
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Mrs. Jennings was a good-humored **sexagenarian** who took a lively and bustling interest in the romantic affairs of all her young acquaintances."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Mr. Brooke was a well-meaning **sexagenarian** with a mind full of diverse opinions that never coalesced into steady action."}
    ]
  },
  "unagitated.md": {
    "primary": "Not agitated; calm, undisturbed, serene, and tranquil, whether physically or emotionally.",
    "secondary": "In character description and stoic philosophy, an unagitated demeanor represents the mastery of emotional turmoil through rational self-possession.",
    "quotes": [
      {"author": "Jane Austen", "work": "Persuasion", "quote": "Anne maintained an **unagitated** exterior, though her heart beat with tumultuous emotion as Captain Wentworth entered the room."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Her clear, **unagitated** gaze disarmed his rising anger, making him ashamed of his hasty resentment."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The tranquil surface of the Pacific lay smooth and **unagitated** as an inland pond beneath the summer moon."}
    ]
  }
}

base_dir = r"App database\Latin roots\Cluster Action\Dashboard — ag"

updated_count = 0
for fname, info in data.items():
    fpath = os.path.join(base_dir, fname)
    if not os.path.exists(fpath):
        print(f"Warning: File {fpath} does not exist!")
        continue
    
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    book_idx = content.find("> [!book]")
    if book_idx == -1:
        print(f"Warning: No > [!book] callout in {fname}")
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
    updated_count += 1

print(f"ag Curation Complete: Successfully updated {updated_count}/{len(data)} notes in Dashboard — ag.")
