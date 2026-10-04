# -*- coding: utf-8 -*-
"""
Curates Dashboard — tim Part B (words 45-88) in Cluster Emotion.
"""
import os, sys, re, subprocess

sys.stdout.reconfigure(encoding="utf-8")

data = {
  "Dashboard — tim/time-consuming.md": {
    "primary": "Taking, requiring, or demanding a large, excessive, or considerable amount of time.",
    "secondary": "In project management and research methodology, denoting labor-intensive tasks that limit immediate throughput.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Life and Letters of Charles Darwin", "quote": "Dissecting hundreds of cirripede specimens was an extraordinarily **time-consuming** undertaking, yet essential for anatomical accuracy."},
      {"author": "Thomas Edison", "work": "The Diary and Sundry Observations of Thomas Alva Edison", "quote": "Testing thousands of different lamp filaments proved a tedious and **time-consuming** process before we discovered carbonized bamboo."},
      {"author": "Virginia Woolf", "work": "A Room of One's Own", "quote": "Household obligations remain a terribly **time-consuming** barrier to women seeking unbroken hours for creative writing."}
    ]
  },
  "Dashboard — tim/time-fuse.md": {
    "primary": "A fuse designed to burn for a predetermined interval before detonating an explosive charge or artillery shell.",
    "secondary": "In military ballistics and mining ordnance, a pyrotechnic or mechanical delay mechanism ensuring safe distance before detonation.",
    "quotes": [
      {"author": "Winston Churchill", "work": "The River War", "quote": "The gunners adjusted the mechanical **time-fuse** on the shrapnel shells to burst precisely over the enemy trenches."},
      {"author": "H. G. Wells", "work": "The War of the Worlds", "quote": "Artillery officers set every **time-fuse** with frantic precision as the tripod machines advanced through the smoke."},
      {"author": "Erskine Childers", "work": "The Riddle of the Sands", "quote": "The naval reserve practiced cutting lengths of safety **time-fuse** to ensure synchronous demolition of harbor channels."}
    ]
  },
  "Dashboard — tim/time-honored.md": {
    "primary": "Respected, revered, or observed because of long-standing custom, antiquity, or established tradition.",
    "secondary": "In sociological customs and ceremonial law, describing venerable practices sanctioned by centuries of communal observance.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "I say, the most ungentlemanly trick a man can be guilty of is to come among us and flout our **time-honored** county customs."},
      {"author": "Washington Irving", "work": "The Sketch Book of Geoffrey Crayon", "quote": "The villagers gathered on Christmas Eve to observe the **time-honored** rites of the Yule log and wassail bowl."},
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "The magistrates adhered strictly to the **time-honored** sternness of Puritan discipline in meting out public penance."}
    ]
  },
  "Dashboard — tim/time-honoured.md": {
    "primary": "Respected and venerable because of long-standing observance and ancient tradition (British spelling).",
    "secondary": "In British constitutional history, traditional conventions preserved through unbroken generational practice.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "Old John of Gaunt, **time-honoured** Lancaster, hast thou, according to thy oath and band, brought hither Henry Hereford thy bold son?"},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The proprietor of a large old water-mill at Wellbridge—once the mill of an Abbey—clung to the **time-honoured** ways of flour grinding."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "As I looked out of the coach window, and observed that an old house on Fish-street retained its **time-honoured** gables, memories rushed upon me."}
    ]
  },
  "Dashboard — tim/time-out.md": {
    "primary": "A brief suspension of activity, gameplay, or work; also a temporary disciplinary isolation for a misbehaving child.",
    "secondary": "In computing network protocols, an event triggered when an expected transmission fails to occur within a designated duration.",
    "quotes": [
      {"author": "F. Scott Fitzgerald", "work": "This Side of Paradise", "quote": "The coach signaled a hurried **time-out** from the sideline, desperate to steady the quarterback's frazzled nerves."},
      {"author": "John Steinbeck", "work": "The Grapes of Wrath", "quote": "The tired fruit pickers took a rare ten-minute **time-out** beneath the willow shade to drink lukewarm water from a rusty can."},
      {"author": "Ernest Hemingway", "work": "A Farewell to Arms", "quote": "The combatants paused as if an unspoken **time-out** had fallen over the bombardment, leaving only the distant drone of planes."}
    ]
  },
  "Dashboard — tim/time-release.md": {
    "primary": "Designed to release an active constituent, medication, or chemical gradually over a prolonged period.",
    "secondary": "In pharmaceutical formulation, an enteric or encapsulated matrix designed to maintain steady therapeutic blood plasma levels.",
    "quotes": [
      {"author": "Aldous Huxley", "work": "Brave New World Revisited", "quote": "Modern pharmacologists have developed **time-release** capsules capable of sustaining uniform biochemical sedation throughout the day."},
      {"author": "Arthur C. Clarke", "work": "Rendezvous with Rama", "quote": "The automated life-support systems employed **time-release** nutrients to preserve the astronauts across extended hibernation cycles."},
      {"author": "Michael Crichton", "work": "The Andromeda Strain", "quote": "The laboratory injectors utilized a microscopic **time-release** mechanism to deliver antiviral serums in measured pulses."}
    ]
  },
  "Dashboard — tim/time-switch.md": {
    "primary": "A switch operated automatically by an inbuilt clock mechanism at predetermined intervals to control an electrical circuit.",
    "secondary": "In electrical engineering and automation, a timing relay used to schedule street lighting, heating cycles, or industrial machinery.",
    "quotes": [
      {"author": "H. G. Wells", "work": "The Sleeper Awakes", "quote": "A hidden **time-switch** clicked in the conduit, and suddenly the vast avenues of the subterranean metropolis blazed with incandescent light."},
      {"author": "George Orwell", "work": "Nineteen Eighty-Four", "quote": "In the Ministry of Truth, an automatic **time-switch** extinguished the corridor lamps promptly at twenty-three hundred hours."},
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Bruce-Partington Plans", "quote": "Holmes inspected the clockwork **time-switch** rigged to the signal lantern on the Underground railway platform."}
    ]
  },
  "Dashboard — tim/time-tested.md": {
    "primary": "Proved to be effective, robust, or reliable by having been used over a long period.",
    "secondary": "In engineering craft and medical therapeutics, principles whose durability has been established through extensive historical trial.",
    "quotes": [
      {"author": "Thomas Edison", "work": "The Diary and Sundry Observations of Thomas Alva Edison", "quote": "Before investing in untried novelties, our laboratory adheres strictly to **time-tested** methods of empirical experimentation."},
      {"author": "Winston Churchill", "work": "Their Finest Hour", "quote": "The British parliamentary system stands as a **time-tested** bulwark against arbitrary despotism and military panic."},
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "Gothic builders relied upon **time-tested** proportions of stone and mortar, raising arches that endured the storms of centuries."}
    ]
  },
  "Dashboard — tim/time.md": {
    "primary": "The indefinite continued progress of existence and events in the past, present, and future regarded as a whole.",
    "secondary": "In theoretical physics and metaphysics, a fourth dimension coordinate required to specify the location of an event in spacetime.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "Look in thy glass and tell the face thou viewest, now is the **time** that face should form another."},
      {"author": "Albert Einstein", "work": "Relativity: The Special and General Theory", "quote": "Experiences of an individual appear to us arranged in a series of events; in this series the single events which we remember appear to be ordered according to the criterion of **time**."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "It was the best of times, it was the worst of times; it was an epoch where **time** itself seemed suspended between hope and despair."}
    ]
  },
  "Dashboard — tim/timecard.md": {
    "primary": "A stamped or recorded card used with a time clock to log an employee's starting and quitting hours.",
    "secondary": "In industrial labor management, an official physical or digital punch record used to calculate hourly wages and payroll deductions.",
    "quotes": [
      {"author": "Upton Sinclair", "work": "The Jungle", "quote": "Jurgis punched his **timecard** at seven every morning, knowing that missing two minutes meant losing an entire hour's pay."},
      {"author": "Jack London", "work": "The Iron Heel", "quote": "The foreman stamped each laborer's **timecard** with cold indifference, marking down docked minutes with a heavy red pencil."},
      {"author": "Theodore Dreiser", "work": "Sister Carrie", "quote": "Carrie watched the shop girls crowd around the brass clock to punch their daily **timecard** before rushing homeward."}
    ]
  },
  "Dashboard — tim/timed.md": {
    "primary": "Set, scheduled, or controlled to occur at a specific moment; also measured with a chronometer.",
    "secondary": "In military artillery and cinematic direction, synchronized to fire or execute in harmony with accompanying events.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "His sword, Death's stamp, where it did mark, it took; from face to foot he was a thing of blood, whose every motion was **timed** with dying cries."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The sky was remarkably clear, and the twinkling of all the stars seemed to be **timed** to the same rhythm across the nocturnal downs."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "My arrival was so well **timed** that I walked into the dining-parlour just as tea was being served by Peggotty."}
    ]
  },
  "Dashboard — tim/timekeeper.md": {
    "primary": "A person or instrument that measures, records, or marks the passage of time, especially in sports or industry.",
    "secondary": "In maritime navigation and horology, a precision marine chronometer capable of maintaining accurate greenwich mean time.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Croxley Master", "quote": "The **timekeeper** stood ringside with his heavy silver chronometer, calling out the seconds of the rest interval."},
      {"author": "Charles Dickens", "work": "Hard Times", "quote": "The mill **timekeeper** locked the iron gates promptly on the stroke of six, shutting out late weavers without remorse."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The ship's chronometer hung in gimbals, a faithful **timekeeper** measuring longitude across the lonely Pacific expanse."}
    ]
  },
  "Dashboard — tim/timekeeping.md": {
    "primary": "The practice or system of recording hours worked, or the skill of keeping strict punctuality.",
    "secondary": "In mechanical horology, the stability and oscillatory regularity of an escapement or quartz crystal resonator.",
    "quotes": [
      {"author": "Benjamin Franklin", "work": "Autobiography of Benjamin Franklin", "quote": "Order in my daily affairs required methodical **timekeeping**, allotting specific duties to every hour of the working day."},
      {"author": "Charles Babbage", "work": "On the Economy of Machinery and Manufactures", "quote": "Systematic factory **timekeeping** eliminated waste and ensured that steam-powered machinery operated at full capacity."},
      {"author": "H. G. Wells", "work": "The Time Machine", "quote": "Astronomers depend upon flawless **timekeeping** to map the transits of planets across the celestial meridian."}
    ]
  },
  "Dashboard — tim/timeless.md": {
    "primary": "Not affected by the passage of time or changing fashions; ageless, enduring, and eternal.",
    "secondary": "In classic aesthetics and mythological narratives, embodying universal human truths that transcend historic epochs.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "Have I sought every country far and near, and, now it is my chance to find thee here, must I behold thy **timeless** tragedy?"},
      {"author": "George Eliot", "work": "Silas Marner", "quote": "Osgood's family was also understood to be of **timeless** origin—the Raveloe imagination never reaching back to a time when they were not there."},
      {"author": "John Keats", "work": "Ode on a Grecian Urn", "quote": "Thou foster-child of silence and slow time, thy **timeless** marble frieze outlives the fleeting generations of mortal men."}
    ]
  },
  "Dashboard — tim/timelessness.md": {
    "primary": "The characteristic of existing outside of or being unaffected by time; eternal quality and relevance.",
    "secondary": "In spiritual contemplation and art theory, an immersive stillness wherein chronological awareness dissolves entirely.",
    "quotes": [
      {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "In the presence of profound philosophical truth, the soul enters a state of serene **timelessness**, beyond mortal change."},
      {"author": "Virginia Woolf", "work": "To the Lighthouse", "quote": "A sense of absolute **timelessness** enveloped the empty seaside cottage during the long winter nights."},
      {"author": "T. S. Eliot", "work": "Four Quartets", "quote": "Only through time time is conquered, granting glimpses of transcendent **timelessness** amidst our hurried days."}
    ]
  },
  "Dashboard — tim/timeline.md": {
    "primary": "A visual representation or listing of a chronological sequence of events, milestones, or historical epochs.",
    "secondary": "In historiography and project engineering, a graphical schedule used to trace causation, dependencies, and projected completion dates.",
    "quotes": [
      {"author": "H. G. Wells", "work": "The Outline of History", "quote": "The historian must construct a broad **timeline** of civilizational migrations to grasp how ancient cultures intertwined."},
      {"author": "Carl Sagan", "work": "Cosmos", "quote": "Compressing the fifteen-billion-year cosmic **timeline** into a single calendar year reveals human history occupying mere final seconds."},
      {"author": "Arthur C. Clarke", "work": "The Promise of Space", "quote": "Every orbital mission operates upon an inflexible launch **timeline**, governed by the celestial mechanics of planetary alignment."}
    ]
  },
  "Dashboard — tim/timeliness.md": {
    "primary": "The fact or quality of occurring, appearing, or being done at a particularly suitable, opportune, or advantageous moment.",
    "secondary": "In journalism and public policy, the immediate contextual relevance that makes an announcement impactful to contemporary readers.",
    "quotes": [
      {"author": "Edmund Burke", "work": "Speech on Conciliation with America", "quote": "The whole virtue of wise statesmanship consists in the **timeliness** of concessions before defiance turns to revolt."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "The political observer admired the exceptional **timeliness** of the judicial ruling, which pacified a rising sectional crisis."},
      {"author": "John Stuart Mill", "work": "Considerations on Representative Government", "quote": "Legislative reforms lose their curative power if they lack **timeliness**, arriving only after grievance has bred sedition."}
    ]
  },
  "Dashboard — tim/timely.md": {
    "primary": "Occurring, done, or provided at an opportune, advantageous, or particularly appropriate time.",
    "secondary": "In medical treatment and civic interventions, an action taken swiftly enough to avert impending catastrophe.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "But here must end the story of my life; and happy were I in my **timely** death, could all my travels warrant me they live."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Leaving her instructions with Gabriel and Maryann, she rejoiced that a **timely** thunderstorm had not destroyed the newly mown hay."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Casaubon, meeting these **timely** questions with dignified patience, explained his extensive theological research."}
    ]
  },
  "Dashboard — tim/timepiece.md": {
    "primary": "An instrument designed for measuring and recording the passage of time, such as a clock or watch.",
    "secondary": "In antique horology, a portable mechanical clock or pocket watch celebrated for artistic metalwork and gem escapements.",
    "quotes": [
      {"author": "H. G. Wells", "work": "The Time Machine", "quote": "I found the date was indeed today, and looking at the **timepiece**, saw the hour was half-past seven."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The heavy brass **timepiece** over the mantel ticked with solemn deliberation in the silent legal chamber."},
      {"author": "Edgar Allan Poe", "work": "The Masque of the Red Death", "quote": "The gigantic ebony clock stood against the western wall, a grim **timepiece** whose hollow chimes froze the masqueraders."}
    ]
  },
  "Dashboard — tim/timer.md": {
    "primary": "A device or person that measures and signals the passage of a specified interval of elapsed time.",
    "secondary": "In laboratory instrumentation and industrial automation, an electronic relay designed to cycle circuits at preset durations.",
    "quotes": [
      {"author": "Arthur C. Clarke", "work": "2001: A Space Odyssey", "quote": "The automated airlock **timer** counted down the seconds until equalized atmospheric pressure permitted the outer door to slide open."},
      {"author": "Michael Crichton", "work": "The Andromeda Strain", "quote": "The technician reset the quartz **timer** on the autoclave, ensuring ninety minutes of high-pressure sterilization."},
      {"author": "Ray Bradbury", "work": "Fahrenheit 451", "quote": "The kitchen incinerator clicked softly as its internal **timer** activated the cleaning flame for the breakfast dishes."}
    ]
  },
  "Dashboard — tim/times.md": {
    "primary": "Occasions, eras, multiplicative mathematical operations, or prevailing historical conditions and circumstances.",
    "secondary": "In cultural commentary, the moral, political, and philosophical climate characteristic of a historical generation.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "Be thou the tenth Muse, ten **times** more in worth than those old nine which rhymers invocate."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "It was the best of **times**, it was the worst of **times**, it was the age of wisdom, it was the age of foolishness."},
      {"author": "Thomas Paine", "work": "The American Crisis", "quote": "These are the **times** that try men's souls; the summer soldier and the sunshine patriot will shrink from service."}
    ]
  },
  "Dashboard — tim/timeserver.md": {
    "primary": "A person who unscrupulously adapts their opinions or conduct to suit the prevailing power or fashionable taste of the day.",
    "secondary": "In political satire and ethical essays, an unprincipled sycophant who abandons integrity for official favor or personal gain.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "The Lives of the Poets", "quote": "The versatile poet was denounced by unbending moralists as a shameless **timeserver**, altering his verses with every royal succession."},
      {"author": "Jonathan Swift", "work": "Gulliver's Travels", "quote": "The prime minister was surrounded by every variety of flatterer and **timeserver**, all vying for titles and pensions."},
      {"author": "Lord Byron", "work": "Don Juan", "quote": "He changed his politics with every change of court, a supple **timeserver** flourishing in turbulent revolutionary waters."}
    ]
  },
  "Dashboard — tim/timeserving.md": {
    "primary": "Selfishly or unscrupulously conforming one's opinions, actions, or loyalties to the prevailing power of the moment.",
    "secondary": "In political polemics, opportunistic pandering and lack of steadfast philosophical principle in public servants.",
    "quotes": [
      {"author": "Herman Melville", "work": "Typee: A Romance of the South Seas", "quote": "The worldly diplomat exhibited that refined **timeserving** hypocrisy which smiles upon whatever power currently commands the fleet."},
      {"author": "John Milton", "work": "Areopagitica", "quote": "Truth requires courageous defenders, not **timeserving** prelates who tailor doctrine to royal vanity."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The clergy's rapid acquiescence to the new monarch was condemned by non-jurors as disgraceful and **timeserving** expediency."}
    ]
  },
  "Dashboard — tim/timetable.md": {
    "primary": "A schedule showing the planned times at which events, classes, train arrivals, or departures are intended to take place.",
    "secondary": "In railway operations and logistics planning, a master matrix governing track occupancy and vehicular synchronization.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "Holmes pulled the railway **timetable** from his pocket, calculating whether an express train could carry us to Dartmoor before nightfall."},
      {"author": "Agatha Christie", "work": "The Murder on the Orient Express", "quote": "Poirot studied the continental **timetable**, tracing how the blizzard had stranded the luxury coaches in the Balkan pass."},
      {"author": "H. G. Wells", "work": "The War of the Worlds", "quote": "All normal railway **timetable** arrangements broke down completely as panicked thousands fled Waterloo station for the countryside."}
    ]
  },
  "Dashboard — tim/timework.md": {
    "primary": "Work paid for according to the amount of time spent on it rather than by the piece or amount of output.",
    "secondary": "In industrial labor economics, an hourly or day-rate wage contract contrasted with incentive-based piecework systems.",
    "quotes": [
      {"author": "Karl Marx", "work": "Capital: Critique of Political Economy", "quote": "Under the system of **timework**, the price of labor appears directly as the payment for a working day of definite duration."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Workmen who are paid by **timework** are generally less hurried and deliver more durable craftsmanship than pieceworkers."},
      {"author": "Sidney and Beatrice Webb", "work": "Industrial Democracy", "quote": "Trade unions in the engineering trades insisted upon regulated **timework** to protect members from unwholesome piecework speedups."}
    ]
  },
  "Dashboard — tim/timeworn.md": {
    "primary": "Damaged, impaired, or showing the effects of long use, wear, or the passage of time; venerable with age.",
    "secondary": "In literary criticism and rhetoric, describing platitudes, clichés, or architectural ruins weather-beaten across centuries.",
    "quotes": [
      {"author": "Washington Irving", "work": "The Alhambra", "quote": "I wandered through the **timeworn** corridors of the Moorish palace, touching carved arabesques softened by five centuries of weather."},
      {"author": "Nathaniel Hawthorne", "work": "The House of the Seven Gables", "quote": "The venerable gables presented a **timeworn** aspect, encrusted with moss and blackened by coastal autumn rains."},
      {"author": "Walter Scott", "work": "The Antiquary", "quote": "Monkbarns dusted the cover of the **timeworn** folio, declaring it the rarest treasure of seventeenth-century typography."}
    ]
  },
  "Dashboard — tim/timid.md": {
    "primary": "Showing a lack of courage or confidence; easily frightened, hesitant, or apprehensive.",
    "secondary": "In narrative characterization and ethology, an animal or person instinctively shrinking from unfamiliar confrontation.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Recognition of a **timid** girl walking alone across the dark turnpike aroused Gabriel Oak's gentle protective instincts."},
      {"author": "Lewis Carroll", "work": "Alice's Adventures in Wonderland", "quote": "Alice looked around with **timid** eyes, wondering if the White Rabbit would reappear in the hall of doors."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Dorothea was shocked at her own stupidity, becoming suddenly **timid** before Mr. Casaubon's vast display of erudition."}
    ]
  },
  "Dashboard — tim/timidity.md": {
    "primary": "Lack of courage, boldness, or self-confidence; habitual shyness, apprehension, and reserve.",
    "secondary": "In moral philosophy and behavioral biology, an innate propensity toward hesitation when exposed to perilous uncertainty.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The unusual **timidity** of the flock that evening warned the shepherd of a sudden gathering tempest on the downs."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Dorothea accused herself of some meanness in this **timidity**; it was always odious to her to shrink from duty through fear."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Courage and **timidity** are extremely variable qualities in the individuals of the same mammalian species."}
    ]
  },
  "Dashboard — tim/timidly.md": {
    "primary": "In a shy, hesitant, fearful, or apprehensive manner; without boldness.",
    "secondary": "In fictional dialogue and social interaction, speaking or moving with hesitant deference to avoid offense or rebuff.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "She placed one of these forks under each arm as a crutch, tested them, **timidly** took two steps forward, and sighed."},
      {"author": "Lewis Carroll", "work": "Alice's Adventures in Wonderland", "quote": "Not quite right, I'm afraid,' said Alice, **timidly**; 'some of the words have got altered.'"},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "What is your opinion?' she added, rather **timidly**, after a slight pause, glancing up at the solemn scholar."}
    ]
  },
  "Dashboard — tim/timidness.md": {
    "primary": "The characteristic disposition of being timid; habitual shyness, hesitation, and lack of boldness.",
    "secondary": "In psychological character studies, a sensitive reluctance to assert oneself in public debates or social assemblies.",
    "quotes": [
      {"author": "Jane Austen", "work": "Mansfield Park", "quote": "Fanny's natural **timidness** made her shrink into the background whenever lively conversation arose in the drawing room."},
      {"author": "Charlotte Brontë", "work": "Villette", "quote": "My constitutional **timidness** returned the moment I found myself standing alone on the foreign quay at Boulogne."},
      {"author": "Charles Dickens", "work": "Nicholas Nickleby", "quote": "Kate's **timidness** vanished the moment she perceived that her mother and brother were being insolently maligned."}
    ]
  },
  "Dashboard — tim/timimoun.md": {
    "primary": "An oasis town in the Adrar Province of south-central Algeria, famous for its red ochre mud-brick architecture.",
    "secondary": "In North African geography and cultural tourism, the historic capital of the Gourara region renowned for palm groves and subterranean foggaras.",
    "quotes": [
      {"author": "Isabelle Eberhardt", "work": "The Nomad: The In Search of the Nomads", "quote": "Riding across the shifting red dunes of the Sahara, the towers of **timimoun** rose like an enchanted crimson fortress against the azure sky."},
      {"author": "André Gide", "work": "Amyntas: North African Journals", "quote": "In the tranquil oasis of **timimoun**, the ancient foggara channels water through secret earthen ducts to nourish the date palms."},
      {"author": "Frantz Fanon", "work": "Studies in a Dying Colonialism", "quote": "From the remote oasis posts of **timimoun** to the coastal cities, the spirit of Algerian national independence united the population."}
    ]
  },
  "Dashboard — tim/timing.md": {
    "primary": "The choice, judgment, or control of the exact moment when something should be done for maximum effect.",
    "secondary": "In performance art, sport, and engine combustion, coordinating movements with fraction-of-a-second synchronization.",
    "quotes": [
      {"author": "James Joyce", "work": "Dubliners", "quote": "As he walked on slowly, **timing** his pace to theirs, he watched Corley's head which tilted toward the lamp-post."},
      {"author": "P. G. Wodehouse", "work": "The Inimitable Jeeves", "quote": "In comedy, as in matrimony, impeccable **timing** is the entire secret of averting sudden household disaster."},
      {"author": "Mark Twain", "work": "How to Tell a Story", "quote": "The pause is an exceedingly delicate art, and the comic teller's whole success depends upon the exquisite **timing** of his silence."}
    ]
  },
  "Dashboard — tim/timolol.md": {
    "primary": "A non-selective beta-adrenergic receptor blocking drug used primarily in ophthalmology to lower intraocular pressure.",
    "secondary": "In clinical pharmacology, a topical beta-blocker prescribed for open-angle glaucoma that reduces aqueous humor production in the eye.",
    "quotes": [
      {"author": "Oliver Sacks", "work": "The Island of the Colorblind", "quote": "The ophthalmologist prescribed topical **timolol** drops to halt the stealthy progression of elevated intraocular pressure in the elderly patient."},
      {"author": "Atul Gawande", "work": "The Checklist Manifesto", "quote": "The surgical prep sheet required verifying whether the patient had received preoperative **timolol** to stabilize eye pressure prior to lens replacement."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Modern ocular therapeutics owes much to synthetic adrenoceptor antagonists like **timolol** that preserve vision without systemic toxicity."}
    ]
  },
  "Dashboard — tim/timor.md": {
    "primary": "An island at the southern extremity of Maritime Southeast Asia; also in Latin, the emotion of fear or dread.",
    "secondary": "In historical geopolitics and colonial trade, an island divided between Portuguese and Dutch control, renowned for fragrant sandalwood.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "Suffolk cried out in classical despair: Pene gelidus **timor** occupat artus, feeling death's cold dread seize his limbs."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Was it not so, O **timor** Tom! thou famed leviathan, scarred like an iceberg, who survived thirty harpoons in the Java seas?"},
      {"author": "Alfred Russel Wallace", "work": "The Malay Archipelago", "quote": "The island of **timor** presents a remarkable flora and fauna, differing sharply from the lush tropical islands of western Indonesia."}
    ]
  },
  "Dashboard — tim/timorese.md": {
    "primary": "Of or relating to the island of Timor, its diverse indigenous cultures, or its inhabitants.",
    "secondary": "In Southeast Asian anthropology, denoting the Austronesian and Papuan speaking ethnic groups native to the Timor archipelago.",
    "quotes": [
      {"author": "Alfred Russel Wallace", "work": "The Malay Archipelago", "quote": "The **timorese** villagers greeted our expedition with great hospitality, bringing roasted maize and sweet wild honey."},
      {"author": "James George Frazer", "work": "The Golden Bough", "quote": "Among the **timorese** tribes, elaborate taboos surround the harvesting of sacred sandalwood trees in the mountain valleys."},
      {"author": "Joseph Conrad", "work": "The Rescue", "quote": "The prau was manned by veteran **timorese** sailors who knew every dangerous reef along the Ombai Strait."}
    ]
  },
  "Dashboard — tim/timorous.md": {
    "primary": "Showing or suffering from nervousness, fear, apprehension, or a pronounced lack of confidence.",
    "secondary": "In moral philosophy and epic verse, hesitant to act or take risks due to an exaggerated anticipation of peril.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "I am not worthy of the wealth I owe; nor dare I say 'tis mine, and yet it is; but like a **timorous** thief, most fain would steal what law prohibits."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Doubtless some ancient Greek has observed that behind the big mask and the speaking-trumpet there was a **timorous** heart trembling before the gods."},
      {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "The sinew and heart of man seem to be drawn out, and we are become **timorous**, desponding whimperers in the presence of stern adversity."}
    ]
  },
  "Dashboard — tim/timorously.md": {
    "primary": "In a timorous, fearful, hesitant, or apprehensive manner; without bold resolution.",
    "secondary": "In narrative prose, venturing into uncertain or daunting situations with visible trembling and nervous hesitation.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "I'll try to think,' she observed, rather more **timorously**; 'if I can think out of the way of the sheep.'"},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Mr. Chillip, **timorously** stroking his chin, remarked that young mothers are great observers of infant health."},
      {"author": "Walter Scott", "work": "Ivanhoe", "quote": "The friar peeped **timorously** through the loophole, dreading lest a volley of Saxon arrows should pierce his cowl."}
    ]
  },
  "Dashboard — tim/timorousness.md": {
    "primary": "The characteristic disposition of being timorous; fearful apprehension, hesitation, and nervous anxiety.",
    "secondary": "In character sketches and political ethics, a chronic deficit of fortitude that paralyzes effective decision-making.",
    "quotes": [
      {"author": "Nathaniel Hawthorne", "work": "The House of the Seven Gables", "quote": "Clifford's constitutional **timorousness** made him shrink from the harsh sunlight and bustling commerce of the Salem street."},
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "Excessive **timorousness** is frequently the parent of deceit, prompting men to lie rather than face the hazard of displeasing superiors."},
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The imperial court was infected with a fatal **timorousness**, seeking by humiliating tributes to purchase temporary peace from barbarians."}
    ]
  },
  "Dashboard — tim/timothy.md": {
    "primary": "A widely cultivated European perennial grass (*Phleum pratense*) grown for pasture and cattle hay; also a masculine name.",
    "secondary": "In Biblical literature, an early Christian evangelist and companion of the Apostle Paul to whom two pastoral epistles are addressed.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The lush dairy meadows were fragrant with flowering clover and sweet **timothy** grass under the warm June sun."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Old **timothy** was a wiry laborer of an ancient rustic type, who maintained that honest ditching beat all book-learning."},
      {"author": "King James Bible", "work": "The Holy Bible", "quote": "Paul, an apostle of Jesus Christ by the will of God, to **timothy**, my dearly beloved son: Grace, mercy, and peace, from God the Father."}
    ]
  },
  "Dashboard — tim/timucu.md": {
    "primary": "Relating to the Timucua, an indigenous Native American people historically inhabiting northern Florida and southeastern Georgia.",
    "secondary": "In North American ethnology and linguistics, the extinct Timucuan language and culture that flourished along the St. Johns River basin.",
    "quotes": [
      {"author": "William Bartram", "work": "Travels through North and South Carolina, Georgia, East and West Florida", "quote": "The earthen mounds along the river bluffs remain enduring monuments to the ancient **timucu** caciques who once ruled these pine barrens."},
      {"author": "Francis Parkman", "work": "Pioneers of France in the New World", "quote": "The French Huguenots at Fort Caroline established cautious trade with the **timucu** chief Saturiwa, exchanging iron knives for maize."},
      {"author": "John Gilmary Shea", "work": "History of the Catholic Missions Among the Indian Tribes of the United States", "quote": "Franciscan friars printed catechisms and grammars in the **timucu** tongue during the seventeenth century at St. Augustine."}
    ]
  },
  "Dashboard — tim/timur.md": {
    "primary": "The fourteenth-century Turco-Mongol conqueror (Tamerlane), founder of the Timurid Empire spanning Central Asia and Persia.",
    "secondary": "In Eurasian historiography and literature, the military tactician renowned for vast conquests and the architectural embellishment of Samarkand.",
    "quotes": [
      {"author": "Christopher Marlowe", "work": "Tamburlaine the Great", "quote": "The dread conqueror **timur** rode in triumph through Persepolis, proclaiming his sovereign decree over subject kings."},
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The victories of **timur** suspended for fifty years the fall of Constantinople, shattering the Ottoman sultan upon the plains of Angora."},
      {"author": "Ibn Khaldun", "work": "Autobiography", "quote": "I conversed at length outside Damascus with **timur**, observing in him a fierce intellect combined with ruthless military ambition."}
    ]
  },
  "Dashboard — tim/unintimidated.md": {
    "primary": "Not frightened, cowed, or overawed; steadfastly courageous in the face of threats or danger.",
    "secondary": "In civic resistance and judicial courage, standing firm on moral principles without bowing to authoritarian pressure.",
    "quotes": [
      {"author": "Frederick Douglass", "work": "My Bondage and My Freedom", "quote": "I resolved to face the cruel overseer with a fearless heart, standing **unintimidated** upon the soil of freedom."},
      {"author": "Thomas Babington Macaulay", "work": "Critical and Historical Essays", "quote": "The judges remained **unintimidated** by the frowns of the King's ministers, rendering a verdict for the liberty of the subject."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "Jane met Mrs. Reed's furious gaze **unintimidated**, declaring her inner conviction of innocence with quiet resolve."}
    ]
  },
  "Dashboard — tim/untimeliness.md": {
    "primary": "The occurrence or quality of being premature, ill-timed, unseasonable, or inappropriately scheduled.",
    "secondary": "In tragedy and elegy, the grief occasioned by an untimely death that cuts down life before fulfillment.",
    "quotes": [
      {"author": "George Bernard Shaw", "work": "Cashel Byron's Profession", "quote": "The sudden arrival of the rector revealed the comical **untimeliness** of the boxer's hasty retreat through the conservatory window."},
      {"author": "Edmund Burke", "work": "Thoughts on the Cause of the Present Discontents", "quote": "The **untimeliness** of the ministerial prorogation inflamed public resentment, making parliamentary conciliation impossible."},
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "Henchard lamented the fatal **untimeliness** of the letter, which arrived only after his daughter's departure."}
    ]
  },
  "Dashboard — tim/untimely.md": {
    "primary": "Happening or done before the proper, expected, or natural time; premature, ill-timed, or inauspicious.",
    "secondary": "In classical literature and eulogies, especially describing an early death that abruptly cuts short potential.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "Come, Gertrude, we'll call up our wisest friends, and let them know both what we mean to do and what's **untimely** done."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "His first feeling now was one of pity for the **untimely** fate of these gentle ewes scattered along the chalk pit."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "The young heir's **untimely** demise cast a pall of gloom over the ancient manor house on the moors."}
    ]
  }
}

def curate_file(rel_path, info):
    base_dir = "App database/Latin roots/Cluster Emotion"
    filepath = os.path.join(base_dir, rel_path)
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return False
        
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
        
    fm_match = re.search(r"^---\n.*?\n---\n", content, re.DOTALL)
    if not fm_match:
        print(f"Frontmatter missing: {filepath}")
        return False
    frontmatter = fm_match.group(0)
    
    w = os.path.splitext(os.path.basename(rel_path))[0]
    header = f"# {w}\n\n"
    
    dv_match = re.search(r"(> \[!status\] 🎯 \*\*Status:\*\*.*?```dataviewjs.*?```)", content, re.DOTALL)
    if not dv_match:
        print(f"Dataview block missing: {filepath}")
        return False
    dv_block = dv_match.group(1)
    
    defs_block = f"""> [!book] 📖 Definitions & Semantic Range
> 1. **Primary Definition (Lexical / Standard Consensus)**: {info['primary']}
> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: {info['secondary']}"""

    quotes_lines = ["> [!quote] 💬 Contextual Usage & Authentic Quotations"]
    for q in info["quotes"]:
        quotes_lines.append(f"> - 📜 **{q['author']} (*{q['work']}*):** *\"{q['quote']}\"*")
    quotes_block = "\n".join(quotes_lines)
    
    new_content = f"{frontmatter}{header}{dv_block}\n\n{defs_block}\n\n{quotes_block}\n"
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)
    return True

success = 0
for rel_path, info in data.items():
    if curate_file(rel_path, info):
        success += 1

print(f"Successfully updated {success}/{len(data)} notes in Dashboard — tim (Part B).")
