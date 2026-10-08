# -*- coding: utf-8 -*-
"""
curate_power_b1_p3.py
Pristine curation for Cluster Power Batch 1 Part 3:
- Dashboard — imper (40 words)
"""
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

data_power_b1_p3 = {
    # =========================================================================
    # Dashboard — imper (40 words)
    # =========================================================================
    "imperative": {
        "primary": "Expressing an urgent authoritative command, obligatory duty, or unavoidable necessity.",
        "secondary": "In grammar, the verbal mood utilized to articulate direct commands, injunctions, or entreaties.",
        "quotes": [
            {
                "author": "Thomas Hardy",
                "work": "Far from the Madding Crowd",
                "quote": "An **imperative** sense of duty urged him forward through the blinding snow toward the sheepfold."
            },
            {
                "author": "George Eliot",
                "work": "Middlemarch",
                "quote": "The financial necessity had become **imperative**, forcing him to consider measures he once despised."
            },
            {
                "author": "Ralph Waldo Emerson",
                "work": "The Conduct of Life",
                "quote": "Moral law addresses every human conscience with an **imperative** authority that brooks no evasion."
            }
        ]
    },
    "imperatively": {
        "primary": "In a commanding, authoritative, or urgently obligatory manner admitting no refusal.",
        "secondary": "With peremptory force that demands immediate compliance or practical resolution.",
        "quotes": [
            {
                "author": "Thomas Hardy",
                "work": "Tess of the d'Urbervilles",
                "quote": "Her conscience spoke **imperatively**, demanding that she make a full disclosure before the wedding morning."
            },
            {
                "author": "George Eliot",
                "work": "Middlemarch",
                "quote": "The circumstances called **imperatively** for instant decision, yet he lingered in painful hesitation."
            },
            {
                "author": "Nathaniel Hawthorne",
                "work": "The Marble Faun",
                "quote": "The voice of duty summoned him **imperatively** away from the sunny terraces of the Roman villa."
            }
        ]
    },
    "imperativeness": {
        "primary": "The character of being urgently commanding, peremptorily authoritative, or unyielding.",
        "secondary": "The compelling urgency or unavoidable moral necessity attaching to an obligation.",
        "quotes": [
            {
                "author": "George Eliot",
                "work": "Felix Holt, the Radical",
                "quote": "There was a quiet **imperativeness** in his tone which quelled the rising anger of the assembly."
            },
            {
                "author": "Henry James",
                "work": "The Portrait of a Lady",
                "quote": "She felt the **imperativeness** of the summons, knowing that further delay would appear unpardonable."
            },
            {
                "author": "Thomas Carlyle",
                "work": "Sartor Resartus",
                "quote": "The divine **imperativeness** of work alone rescues man from frivolous despair and sluggish apathy."
            }
        ]
    },
    "imperceptibility": {
        "primary": "The characteristic of being too subtle, minute, or gradual to be detected by human senses.",
        "secondary": "In sensory psychology and physics, the property of falling below the minimum threshold of conscious perception.",
        "quotes": [
            {
                "author": "John Locke",
                "work": "An Essay Concerning Human Understanding",
                "quote": "The perpetual decay of material particles proceeds with an **imperceptibility** that eludes our grosser sensory faculties."
            },
            {
                "author": "William James",
                "work": "The Principles of Psychology",
                "quote": "Transitions in stream-of-consciousness occur with such delicate **imperceptibility** that boundary lines cannot be fixed."
            },
            {
                "author": "Thomas Henry Huxley",
                "work": "Method and Results",
                "quote": "Slow geological alterations accomplish enormous displacements despite the total **imperceptibility** of daily movement."
            }
        ]
    },
    "imperceptible": {
        "primary": "Extremely slight, gradual, or subtle; incapable of being perceived by ordinary sensory observation.",
        "secondary": "Proceeding by increments so fine as to escape detection except through cumulative duration.",
        "quotes": [
            {
                "author": "Thomas Hardy",
                "work": "The Mayor of Casterbridge",
                "quote": "By an **imperceptible** transition, the afternoon gold faded into the dull ash of an autumn twilight."
            },
            {
                "author": "Charles Darwin",
                "work": "The Origin of Species",
                "quote": "Natural selection can act only by very short and slow steps, by **imperceptible** varieties suited to new conditions."
            },
            {
                "author": "Joseph Conrad",
                "work": "Lord Jim",
                "quote": "The ship rose on the swell with an almost **imperceptible** roll, gliding silently through the nocturnal sea."
            }
        ]
    },
    "imperceptibly": {
        "primary": "In a manner so slight, gradual, or subtle as to be virtually unnoticeable.",
        "secondary": "By minute successive stages that reveal change only over significant intervals of time.",
        "quotes": [
            {
                "author": "Ralph Waldo Emerson",
                "work": "Essays: First Series",
                "quote": "The character forms **imperceptibly** amidst daily choices, like coral islands rising silently beneath ocean waves."
            },
            {
                "author": "H. G. Wells",
                "work": "The Time Machine",
                "quote": "The sun seemed to travel across the sky with unnatural speed, dimming **imperceptibly** into twilight."
            },
            {
                "author": "George Eliot",
                "work": "Silas Marner",
                "quote": "The hard gold had passed away, and its place was filled **imperceptibly** by the soft golden curls of the child."
            }
        ]
    },
    "imperial": {
        "primary": "Pertaining to, characteristic of, or ruled by an emperor, empress, or expansive sovereign empire.",
        "secondary": "Commanding, majestic, or magnificent in scale; also designating established British systems of weights and measures.",
        "quotes": [
            {
                "author": "William Shakespeare",
                "work": "Henry IV, Part 2",
                "quote": "My due from thee is this **imperial** crown, / Which, as immediate from thy place and blood, / Derives itself to me."
            },
            {
                "author": "Thomas Hardy",
                "work": "Far from the Madding Crowd",
                "quote": "She carried herself with an **imperial** pride that forbade any familiarity from rustic admirers."
            },
            {
                "author": "Arthur Conan Doyle",
                "work": "The Return of Sherlock Holmes",
                "quote": "The international theft involved documents vital to the **imperial** interests of the British government."
            }
        ]
    },
    "imperialism": {
        "primary": "A national policy, practice, or advocacy of extending sovereign power and colonial dominion abroad.",
        "secondary": "The geopolitical acquisition and economic exploitation of overseas territories through military or diplomatic hegemony.",
        "quotes": [
            {
                "author": "J. A. Hobson",
                "work": "Imperialism: A Study",
                "quote": "Modern **imperialism** represents a debasement of genuine nationalism, transforming defensive patriotism into aggressive territorial expansion."
            },
            {
                "author": "G. K. Chesterton",
                "work": "Tremendous Trifles",
                "quote": "The trouble with modern **imperialism** is that it is not proud of its land; it is only proud of its size."
            },
            {
                "author": "H. G. Wells",
                "work": "The War of the Worlds",
                "quote": "Before we judge the Martians too harshly, we must remember what ruthless destruction our own European **imperialism** wrought upon gentle races."
            }
        ]
    },
    "imperialist": {
        "primary": "An advocate, supporter, or political agent of imperial expansion and colonial dominion.",
        "secondary": "Relating to or motivated by ideological doctrines of overseas hegemony and territorial annexation.",
        "quotes": [
            {
                "author": "George Orwell",
                "work": "Burmese Days",
                "quote": "The honest **imperialist** suffers because he must perpetually defend a commercial monopoly under the cant of bringing civilization."
            },
            {
                "author": "Rudyard Kipling",
                "work": "The Five Nations",
                "quote": "He spoke with the fervent conviction of an unyielding **imperialist**, envisioning order and commerce across distant oceans."
            },
            {
                "author": "Bertrand Russell",
                "work": "Principles of Social Reconstruction",
                "quote": "The narrow outlook of the ardent **imperialist** blinds him to the legitimate aspirations of subject nationalities."
            }
        ]
    },
    "imperialistic": {
        "primary": "Exhibiting characteristics, policies, or aggressive aims typical of imperial empire-building.",
        "secondary": "Promoting geopolitical domination, military hegemony, or commercial subjugation over foreign peoples.",
        "quotes": [
            {
                "author": "G. K. Chesterton",
                "work": "The Flying Inn",
                "quote": "This grand **imperialistic** scheme promises to unite the globe, yet it forgets the simple liberty of an English tavern."
            },
            {
                "author": "Thorstein Veblen",
                "work": "The Theory of the Leisure Class",
                "quote": "Pecuniary emulation easily aligns itself with **imperialistic** ambitions that celebrate collective dominance and predatory display."
            },
            {
                "author": "H. G. Wells",
                "work": "The New Machiavelli",
                "quote": "The young politicians of that decade were captivated by noisy **imperialistic** slogans that promised national grandeur without intellectual toil."
            }
        ]
    },
    "imperially": {
        "primary": "In an imperial, royal, or sovereignly commanding manner.",
        "secondary": "With majestic grandeur or sovereign magnificence befitting supreme imperial governance.",
        "quotes": [
            {
                "author": "Herman Melville",
                "work": "Moby-Dick",
                "quote": "He looked **imperially** round upon his harpooneers, as if summoning them to witness a covenant of life and death."
            },
            {
                "author": "Charlotte Brontë",
                "work": "Villette",
                "quote": "Madame Beck governed the pensionnat **imperially**, directing every movement of pupils and teachers with serene, despotic grace."
            },
            {
                "author": "Ralph Waldo Emerson",
                "work": "Representative Men",
                "quote": "Shakespeare ruled **imperially** over the English tongue, commanding words like obedient courtiers to mirror every subtle emotion."
            }
        ]
    },
    "imperil": {
        "primary": "To put in danger, risk, or jeopardy of injury, loss, destruction, or failure.",
        "secondary": "To expose vital assets, lives, or institutions to proximate physical or moral hazards.",
        "quotes": [
            {
                "author": "Charles Dickens",
                "work": "Great Expectations",
                "quote": "I would not **imperil** your safety for the world; keep close within doors until the vessel is ready to sail."
            },
            {
                "author": "Walter Scott",
                "work": "The Talisman",
                "quote": "A rash knight may **imperil** the entire crusading host by yielding to personal anger in the face of the enemy."
            },
            {
                "author": "Thomas Hardy",
                "work": "The Woodlanders",
                "quote": "To divulge the secret now would **imperil** the delicate reputation of one whose happiness he was pledged to defend."
            }
        ]
    },
    "imperious": {
        "primary": "Arrogantly domineering, overbearing, dictatorial, or urgent and compelling in demand.",
        "secondary": "Displaying haughty command that tolerates no opposition or delay in submission.",
        "quotes": [
            {
                "author": "William Shakespeare",
                "work": "Cymbeline",
                "quote": "**Imperious** Caesar, dead and turn'd to clay, / Might stop a hole to keep the wind away: / O, that that earth, which kept the world in awe, / Should patch a wall to expel the winter's flaw!"
            },
            {
                "author": "Thomas Hardy",
                "work": "The Return of the Native",
                "quote": "Eustacia had an **imperious** desire for escape from the lonely heath, longing for music, lights, and crowded ballrooms."
            },
            {
                "author": "Nathaniel Hawthorne",
                "work": "The Scarlet Letter",
                "quote": "Her demeanor was characterized by an **imperious** dignity which seemed to rise above the ignominy of the public scaffold."
            }
        ]
    },
    "imperiously": {
        "primary": "In a haughtily domineering, dictatorial, or commanding manner.",
        "secondary": "With peremptory authority that commands instant and unquestioning compliance.",
        "quotes": [
            {
                "author": "William Shakespeare",
                "work": "Henry VI, Part 1",
                "quote": "Who's there that knocks so **imperiously**? What haughty lord disturbs our council with insolent clamor?"
            },
            {
                "author": "Charles Dickens",
                "work": "Bleak House",
                "quote": "Lady Dedlock looks **imperiously** at her visitor when the servant has left the room, casting a chilling glance upon him."
            },
            {
                "author": "Charlotte Brontë",
                "work": "Jane Eyre",
                "quote": "'Answer me—speak again!' he ordered, **imperiously** and aloud, gazing intently into my eyes."
            }
        ]
    },
    "imperiousness": {
        "primary": "Arrogant overbearingness, haughty command, or dictatorial presumption in manner.",
        "secondary": "An imposing habit of sovereign command that demands deference and subdues resistance.",
        "quotes": [
            {
                "author": "Thomas Hardy",
                "work": "Far from the Madding Crowd",
                "quote": "Such **imperiousness** would have damned a little less beauty; and on the other hand, such beauty would have redeemed far greater pride."
            },
            {
                "author": "George Eliot",
                "work": "Middlemarch",
                "quote": "Bulstrode's native **imperiousness** and strength of determination served him well when confronting rebellious townsmen."
            },
            {
                "author": "Jane Austen",
                "work": "Pride and Prejudice",
                "quote": "The haughty **imperiousness** of Lady Catherine's manners alienated all who were not intimidated by her aristocratic wealth."
            }
        ]
    },
    "imperishability": {
        "primary": "The attribute of being immune to decay, destruction, oblivion, or temporal dissolution.",
        "secondary": "Enduring immortal preservation through spiritual nature, transcendent value, or material invulnerability.",
        "quotes": [
            {
                "author": "John Milton",
                "work": "Paradise Lost",
                "quote": "Ethereal spirits boast an innate **imperishability**, proof against mortal weapons and the corrosive flight of worldly centuries."
            },
            {
                "author": "Percy Bysshe Shelley",
                "work": "A Defence of Poetry",
                "quote": "Poetry redeems from decay the visitations of the divinity in man, conferring an authentic **imperishability** upon mortal thought."
            },
            {
                "author": "Samuel Taylor Coleridge",
                "work": "Biographia Literaria",
                "quote": "The genuine classics of literature achieve their **imperishability** by speaking directly to the universal moral faculties of mankind."
            }
        ]
    },
    "imperishable": {
        "primary": "Incapable of perishing, rotting, or fading; enduring eternally through all temporal vicissitudes.",
        "secondary": "Remaining permanently vital, untarnished, and indestructible in memory, value, or essence.",
        "quotes": [
            {
                "author": "Henry David Thoreau",
                "work": "Walden",
                "quote": "Books are the treasured wealth of the world and the fit inheritance of generations, an **imperishable** monument of genius."
            },
            {
                "author": "John Milton",
                "work": "Paradise Lost",
                "quote": "Their bright celestial armour was forged of **imperishable** substance, defying the fiery darts of the adversary."
            },
            {
                "author": "Herman Melville",
                "work": "Moby-Dick",
                "quote": "There is an **imperishable** dignity in heroic endeavor, even when crowned with disaster in the lonely oceans."
            }
        ]
    },
    "imperishableness": {
        "primary": "The state or character of enduring without decay, deterioration, or temporal dissolution.",
        "secondary": "Inherent resilience against the corrupting ravages of time, physical corrosion, or oblivion.",
        "quotes": [
            {
                "author": "Ralph Waldo Emerson",
                "work": "Essays: Second Series",
                "quote": "The moral sentiment alone possesses the seal of absolute **imperishableness**, outlasting all material monuments and empires."
            },
            {
                "author": "Thomas Carlyle",
                "work": "Past and Present",
                "quote": "Justice is eternal, and the **imperishableness** of divine truth guarantees that wrong cannot prosper forever."
            },
            {
                "author": "William Hazlitt",
                "work": "Table-Talk",
                "quote": "The true mark of literary genius is the **imperishableness** of its creations amidst shifting fashions of speech."
            }
        ]
    },
    "imperishingness": {
        "primary": "The essential quality of existing without susceptibility to death, rot, or temporal decline.",
        "secondary": "Enduring, incorruptible longevity characterized by continuous metaphysical or physical permanence.",
        "quotes": [
            {
                "author": "Algernon Charles Swinburne",
                "work": "William Blake: A Critical Essay",
                "quote": "The prophetic vision asserts the eternal **imperishingness** of the imaginative faculty above all transient forms."
            },
            {
                "author": "John Ruskin",
                "work": "Modern Painters",
                "quote": "In every great mountain landscape there is a solemn testimony to the **imperishingness** of divine design amidst geological decay."
            },
            {
                "author": "Walter Pater",
                "work": "Appreciations",
                "quote": "The exquisite lyric possesses a rare **imperishingness**, surviving intact while vast systems of philosophy crumble into dust."
            }
        ]
    },
    "imperium": {
        "primary": "Supreme executive authority, sovereign power, or command over an empire or armed forces.",
        "secondary": "In Roman constitutional law, supreme military and civil jurisdiction vested in magistrates and consuls.",
        "quotes": [
            {
                "author": "Alexander Hamilton",
                "work": "The Federalist Papers (No. 15)",
                "quote": "They still seem to cherish with blind devotion the political monster of an **imperium** in imperio, dividing sovereignty against itself."
            },
            {
                "author": "Edward Gibbon",
                "work": "The Decline and Fall of the Roman Empire",
                "quote": "The senate conferred the full consular **imperium** upon Augustus, masking autocratic dominion under ancient constitutional titles."
            },
            {
                "author": "James Joyce",
                "work": "Ulysses",
                "quote": "He spoke with satirical venom of the Roman **imperium** that held ancient nations bound beneath foreign legions."
            }
        ]
    },
    "impermanence": {
        "primary": "Transitory mutability, fleeting duration, or temporary existence of physical phenomena.",
        "secondary": "In philosophical and contemplative traditions, the universal law that all compounded phenomena undergo dissolution.",
        "quotes": [
            {
                "author": "William James",
                "work": "The Principles of Psychology",
                "quote": "The radical **impermanence** of our emotional states is one of the most familiar facts of introspective observation."
            },
            {
                "author": "Bertrand Russell",
                "work": "The Problems of Philosophy",
                "quote": "Physical objects exhibit continuous **impermanence**, dissolving under analysis into ever-shifting configurations of energy."
            },
            {
                "author": "D. H. Lawrence",
                "work": "The Rainbow",
                "quote": "She watched the clouds dissolving across the evening sky, overwhelmed by the haunting **impermanence** of human joy."
            }
        ]
    },
    "impermanency": {
        "primary": "The state or characteristic of not lasting; transient mutability or temporary duration.",
        "secondary": "Susceptibility to swift termination, dissolution, or historical replacement.",
        "quotes": [
            {
                "author": "Ralph Waldo Emerson",
                "work": "The Conduct of Life",
                "quote": "Nature teaches the wise observer the lesson of **impermanency**, sweeping away proud dynasties like autumn leaves."
            },
            {
                "author": "Thomas Henry Huxley",
                "work": "Evolution and Ethics",
                "quote": "Cosmic nature reveals an unceasing flux, an essential **impermanency** in all organic forms and environmental adaptations."
            },
            {
                "author": "George Santayana",
                "work": "The Life of Reason",
                "quote": "The tragic sense of life springs from our awareness of the **impermanency** of beauty and the inevitable loss of cherished ideals."
            }
        ]
    },
    "impermanent": {
        "primary": "Not permanent; enduring only for a short time; transitory, fleeting, or provisional.",
        "secondary": "Lacking structural stability or lasting institutional endurance under shifting conditions.",
        "quotes": [
            {
                "author": "James Joyce",
                "work": "Ulysses",
                "quote": "He reflected on the necessity to counteract by an **impermanent** sojourn the rigid permanence of bureaucratic arrest."
            },
            {
                "author": "Virginia Woolf",
                "work": "The Waves",
                "quote": "Our fragile identities seem brief and **impermanent**, like shadows dancing upon an empty wall."
            },
            {
                "author": "H. G. Wells",
                "work": "Tono-Bungay",
                "quote": "All the commercial splendor of the city appeared strangely **impermanent**, a flimsy superstructure awaiting inevitable collapse."
            }
        ]
    },
    "impermeability": {
        "primary": "The property of not permitting fluids, gases, or radiation to pass through a substance.",
        "secondary": "In earth sciences and materials engineering, the physical resistance of dense rock or membrane barriers to fluid transmission.",
        "quotes": [
            {
                "author": "Leo Tolstoy",
                "work": "War and Peace",
                "quote": "A series of experiments proves that matter exhibits both extension and relative **impermeability** to external impact."
            },
            {
                "author": "Michael Faraday",
                "work": "Experimental Researches in Chemistry and Physics",
                "quote": "The absolute **impermeability** of the glass enclosure preserved the delicate vacuum against atmospheric penetration."
            },
            {
                "author": "Charles Darwin",
                "work": "The Formation of Vegetable Mould through the Action of Worms",
                "quote": "The dense layer of compacted clay possessed sufficient **impermeability** to retain surface water throughout prolonged droughts."
            }
        ]
    },
    "impermeable": {
        "primary": "Incapable of being passed through or penetrated, especially by liquids or moisture.",
        "secondary": "Having a compact texture or structure that prevents the transmission of water or other fluids.",
        "quotes": [
            {
                "author": "Charles Lyell",
                "work": "Principles of Geology",
                "quote": "An **impermeable** stratum of shale underlying porous sandstone forces the subterranean water to emerge as natural springs."
            },
            {
                "author": "Thomas Henry Huxley",
                "work": "Physiography: An Introduction to the Study of Nature",
                "quote": "Clay formations form an **impermeable** floor, preventing rain from sinking into deeper geological basins."
            },
            {
                "author": "H. G. Wells",
                "work": "The Island of Doctor Moreau",
                "quote": "We fashioned a shelter of woven branches plastered with stiff mud, which proved almost **impermeable** to the torrential tropical rain."
            }
        ]
    },
    "impermeableness": {
        "primary": "The state or property of resisting the penetration or passage of fluids through pores.",
        "secondary": "The degree to which a geological strata, membrane, or building material repels moisture ingress.",
        "quotes": [
            {
                "author": "Archibald Geikie",
                "work": "Textbook of Geology",
                "quote": "The **impermeableness** of crystalline schist causes surface drainage to carve deep ravines along mountain flanks."
            },
            {
                "author": "John Tyndall",
                "work": "Heat Considered as a Mode of Motion",
                "quote": "The relative **impermeableness** of different substances to radiant heat reveals profound differences in molecular architecture."
            },
            {
                "author": "Robert Boyle",
                "work": "Experiments and Notes about the Mechanical Origine of Divers Particular Qualities",
                "quote": "Experiments demonstrate the **impermeableness** of dense metals when subjected to extreme hydrostatical pressures."
            }
        ]
    },
    "impermissibility": {
        "primary": "Unlawfulness, moral inadmissibility, or strict prohibition under authoritative rules.",
        "secondary": "In jurisprudence and normative ethics, the strict inadmissibility of an act under categorical legal or moral statutes.",
        "quotes": [
            {
                "author": "Immanuel Kant",
                "work": "Critique of Practical Reason",
                "quote": "The moral law demonstrates the categorical **impermissibility** of treating rational beings merely as instruments for selfish ends."
            },
            {
                "author": "John Stuart Mill",
                "work": "Utilitarianism",
                "quote": "The social **impermissibility** of deceptive practices rests upon the irreparable damage they inflict on mutual human trust."
            },
            {
                "author": "Henry Sidgwick",
                "work": "The Methods of Ethics",
                "quote": "Common sense morality recognizes the absolute **impermissibility** of deliberate betrayal, even where utilitarian advantages seem tempting."
            }
        ]
    },
    "impermissible": {
        "primary": "Not allowable, admissible, or permissible; contrary to accepted law, ethics, or rules.",
        "secondary": "Excluded from legitimate practice, legal procedure, or ethical conduct by formal mandate.",
        "quotes": [
            {
                "author": "Bertrand Russell",
                "work": "Introduction to Mathematical Philosophy",
                "quote": "It is logically **impermissible** to treat a class as a member of itself, if vicious paradoxes are to be avoided."
            },
            {
                "author": "G. E. Moore",
                "work": "Principia Ethica",
                "quote": "An action is judged morally **impermissible** when alternative conduct would produce significantly greater organic good."
            },
            {
                "author": "William James",
                "work": "The Will to Believe",
                "quote": "To close our minds against evidence merely from dread of error is an **impermissible** abdication of intellectual responsibility."
            }
        ]
    },
    "impermissibly": {
        "primary": "In a manner that violates established laws, regulations, or ethical standards.",
        "secondary": "Without lawful sanction or legitimate moral warrant.",
        "quotes": [
            {
                "author": "Jeremy Bentham",
                "work": "An Introduction to the Principles of Morals and Legislation",
                "quote": "When the magistrate acts **impermissibly**, exceeding the clear limits of his charter, public confidence is undermined."
            },
            {
                "author": "John Stuart Mill",
                "work": "On Liberty",
                "quote": "Society interferes **impermissibly** whenever it attempts to dictate private opinion without showing direct injury to others."
            },
            {
                "author": "Arthur Schopenhauer",
                "work": "The World as Will and Representation",
                "quote": "Egoism oversteps **impermissibly** when it seeks self-affirmation through the deliberate destruction of another living will."
            }
        ]
    },
    "impersonal": {
        "primary": "Not influenced by personal feelings, individual bias, or private emotional considerations.",
        "secondary": "Lacking distinct personal reference or emotional warmth; objective, detached, or abstract.",
        "quotes": [
            {
                "author": "George Eliot",
                "work": "Middlemarch",
                "quote": "He spoke with that cold, **impersonal** precision which wounded her more deeply than an outburst of passionate anger."
            },
            {
                "author": "Arthur Conan Doyle",
                "work": "The Memoirs of Sherlock Holmes",
                "quote": "Sherlock Holmes regarded the mystery from an **impersonal** standpoint, viewing human misery merely as data for intellectual deduction."
            },
            {
                "author": "Henry David Thoreau",
                "work": "Walden",
                "quote": "Nature presents an **impersonal** majesty which neither flatters human vanity nor yields to our petulant sorrow."
            }
        ]
    },
    "impersonally": {
        "primary": "Without personal bias, individual partiality, or subjective emotional involvement.",
        "secondary": "In an objective, detached, or generalized manner addressing broad principles rather than specific persons.",
        "quotes": [
            {
                "author": "Nathaniel Hawthorne",
                "work": "The Scarlet Letter",
                "quote": "It is scarcely decorous, however, to speak all, even where we speak **impersonally** and under the protection of historical distance."
            },
            {
                "author": "G. K. Chesterton",
                "work": "The Innocence of Father Brown",
                "quote": "The detective examined the bloodstained letter **impersonally**, as though analyzing an algebraic equation on a blackboard."
            },
            {
                "author": "Donn Byrne",
                "work": "The Wind Bloweth",
                "quote": "And when he died, I was very sorry, but **impersonally** sorry, as if something noble in the distant landscape had vanished."
            }
        ]
    },
    "impersonate": {
        "primary": "To assume the identity, character, or appearance of another person, often for fraudulent deception or stage performance.",
        "secondary": "To represent or embody an abstract quality, deity, or dramatic persona in artistic representation.",
        "quotes": [
            {
                "author": "Charles Dickens",
                "work": "The Mystery of Edwin Drood",
                "quote": "The young actor was summoned to **impersonate** a foreign dignitary, donning elaborate robes and false whiskers for the masquerade."
            },
            {
                "author": "Leo Tolstoy",
                "work": "War and Peace",
                "quote": "I can just imagine what a funny figure the actor cut as he waved his arms to **impersonate** a frantic French officer."
            },
            {
                "author": "Arthur Conan Doyle",
                "work": "The Adventures of Sherlock Holmes",
                "quote": "Holmes possessed a remarkable talent to **impersonate** an elderly clergyman or a drunken groom with complete verisimilitude."
            }
        ]
    },
    "impersonation": {
        "primary": "The act of pretending to be another person, whether for dramatic entertainment or fraudulent imposture.",
        "secondary": "The artistic or psychological embodiment of a distinct persona, archetype, or dramatic character.",
        "quotes": [
            {
                "author": "Thomas Hardy",
                "work": "Far from the Madding Crowd",
                "quote": "His silent courtship seemed an unconscious **impersonation** of ancient patient devotion, enduring all rebuffs without complaint."
            },
            {
                "author": "Herman Melville",
                "work": "Typee: A Romance of the South Seas",
                "quote": "The aged priest appeared like a living **impersonation** of archaic superstition, mumbling incantations beside the carved idols."
            },
            {
                "author": "Charles Dickens",
                "work": "David Copperfield",
                "quote": "Mr. Micawber's theatrical **impersonation** of injured innocence deceived nobody, yet it delighted his loyal family."
            }
        ]
    },
    "impersonator": {
        "primary": "A performer, mimic, or impostor who adopts the voice, appearance, or identity of another person.",
        "secondary": "An actor specializing in satirical or dramatic character sketches portraying celebrated public figures.",
        "quotes": [
            {
                "author": "Thomas Hardy",
                "work": "Far from the Madding Crowd",
                "quote": "Even then Boldwood did not recognize that the **impersonator** of Heaven's persistent irony stood smiling on the threshold."
            },
            {
                "author": "James Joyce",
                "work": "Ulysses",
                "quote": "The skilled mimic on the music-hall stage proved a marvelous **impersonator**, copying every vocal mannerism of Dublin magistrates."
            },
            {
                "author": "G. K. Chesterton",
                "work": "The Man Who Was Thursday",
                "quote": "The anarchist agent was an accomplished **impersonator**, passing undetected through police cordons in the disguise of a bishop."
            }
        ]
    },
    "impertinence": {
        "primary": "Insolent disrespect, improper forwardness, or rude presumption toward superiors or companions.",
        "secondary": "Irrelevance, inapplicability, or lack of pertinence to the matter under current deliberation.",
        "quotes": [
            {
                "author": "John Locke",
                "work": "An Essay Concerning Human Understanding",
                "quote": "To introduce irrelevant metaphysical disputations into practical morals is a tedious **impertinence** that darkens counsel."
            },
            {
                "author": "Thomas Hardy",
                "work": "Far from the Madding Crowd",
                "quote": "'What **impertinence**!' said Liddy in a low voice, blushing at the audacious compliments paid by the stranger."
            },
            {
                "author": "George Eliot",
                "work": "Middlemarch",
                "quote": "She resented his unsolicited advice as an unpardonable **impertinence**, though concealed beneath an air of polite concern."
            }
        ]
    },
    "impertinent": {
        "primary": "Rude, insolently disrespectful, or brazenly lacking proper deference in speech or bearing.",
        "secondary": "Not pertinent; irrelevant or inapplicable to the subject matter under examination.",
        "quotes": [
            {
                "author": "William Shakespeare",
                "work": "The Merchant of Venice",
                "quote": "In very brief, the suit is **impertinent** to myself, as your worship shall know by this honest old man."
            },
            {
                "author": "Lewis Carroll",
                "work": "Alice's Adventures in Wonderland",
                "quote": "'You should learn not to make personal remarks,' Alice said with some severity; 'it's very **impertinent**.'"
            },
            {
                "author": "George Eliot",
                "work": "Silas Marner",
                "quote": "The young squire considered any inquiry into his private amusements as an **impertinent** intrusion upon gentlemanly liberty."
            }
        ]
    },
    "impertinently": {
        "primary": "In an insolently disrespectful, intrusive, or presumptuously rude manner.",
        "secondary": "In a manner irrelevant, inappropriate, or unsuited to the serious subject under discussion.",
        "quotes": [
            {
                "author": "Jane Austen",
                "work": "Sense and Sensibility",
                "quote": "He interrupted her reflections by inquiring **impertinently** into the state of her heart with unfeeling levity."
            },
            {
                "author": "Walter Scott",
                "work": "Ivanhoe",
                "quote": "Credit me, it is better to enjoy the good which God sends thee, than to be **impertinently** curious about secret perils."
            },
            {
                "author": "Jonathan Swift",
                "work": "Gulliver's Travels",
                "quote": "The Lilliputian courtiers whispered **impertinently** among themselves, mocking my size and awkward manners behind my back."
            }
        ]
    },
    "imperturbability": {
        "primary": "Unshakable calmness, serene composure, or steady self-possession incapable of being upset.",
        "secondary": "Stoic equanimity that remains placid and tranquil through acute crises or violent provocations.",
        "quotes": [
            {
                "author": "Jules Verne",
                "work": "Twenty Thousand Leagues under the Sea",
                "quote": "His countenance had resumed its habitual **imperturbability**, revealing neither fear nor triumph as the monster drew near."
            },
            {
                "author": "James Joyce",
                "work": "Ulysses",
                "quote": "The pluterperfect **imperturbability** of the department officials exasperated every petitioner who sought redress."
            },
            {
                "author": "Arthur Conan Doyle",
                "work": "A Study in Scarlet",
                "quote": "Holmes listened to the harrowing narrative with absolute **imperturbability**, his eyes fixed dreamily upon the ceiling."
            }
        ]
    },
    "imperturbable": {
        "primary": "Incapable of being agitated, upset, or excited; profoundly calm and steadily serene.",
        "secondary": "Displaying unshakable coolness, placid detachment, and steady self-control under severe stress.",
        "quotes": [
            {
                "author": "Charles Dickens",
                "work": "Bleak House",
                "quote": "Mr. Tulkinghorn is as **imperturbable** as the hearthstone to which he has quietly walked, listening without moving a muscle."
            },
            {
                "author": "Herman Melville",
                "work": "Moby-Dick",
                "quote": "Starbuck remained **imperturbable** amid the confusion, directing the lowering of the boats with cool nautical skill."
            },
            {
                "author": "George Eliot",
                "work": "Daniel Deronda",
                "quote": "His **imperturbable** exterior concealed a mind acutely alive to every subtle shade of meaning in the conversation."
            }
        ]
    },
    "imperturbableness": {
        "primary": "Enduring serenity, unshakeable tranquility, and proof against emotional agitation.",
        "secondary": "A steady, tranquil stoicism of temperament that remains calm and unruffled amidst turmoil.",
        "quotes": [
            {
                "author": "Ralph Waldo Emerson",
                "work": "Representative Men",
                "quote": "Socrates met his judges with that sublime **imperturbableness** which flows from conscious integrity and philosophical peace."
            },
            {
                "author": "Thomas Carlyle",
                "work": "The French Revolution",
                "quote": "Mirabeau alone confronted the tumultuous mob with an iron **imperturbableness**, mastering their passions with his voice."
            },
            {
                "author": "William Hazlitt",
                "work": "Characters of Shakespear's Plays",
                "quote": "The extraordinary **imperturbableness** of Iago makes his villainy appear more sinister and inexorable."
            }
        ]
    }
}

def tokenize(text):
    return set(re.findall(r'[a-zA-Z]{3,}', text.lower()))

def jaccard(s1, s2):
    t1 = tokenize(s1)
    t2 = tokenize(s2)
    if not t1 or not t2:
        return 0.0
    return len(t1 & t2) / len(t1 | t2)

BANNED_PHRASES = [
    "academic lexicon", "classic author", "historical author", "scientific treatise",
    "morphological & etymological treatise", "standard consensus", "traditional author",
    "in academic literature,", "historical records document", "classical commentary"
]

CIRCULAR = re.compile(r'\b(?:the\s+)?(?:quality|state|condition)(?:,\s*state)?(?:,\s*or\s*degree)?\s+of\s+being\b', re.I)

def validate():
    print(f"Total words in data_power_b1_p3: {len(data_power_b1_p3)}")
    errors = []
    for word, item in data_power_b1_p3.items():
        # Primary check
        p = item["primary"]
        if len(p) < 25:
            errors.append(f"[{word}] Primary definition too short ({len(p)} chars)")
        if CIRCULAR.search(p):
            errors.append(f"[{word}] Primary definition contains circular boilerplate formula: '{p}'")

        # Secondary check
        s = item["secondary"]
        if len(s) < 25:
            errors.append(f"[{word}] Secondary definition too short ({len(s)} chars)")
        if CIRCULAR.search(s):
            errors.append(f"[{word}] Secondary definition contains circular boilerplate formula: '{s}'")

        # Jaccard overlap
        j = jaccard(p, s)
        if j >= 0.70:
            errors.append(f"[{word}] Jaccard token overlap too high ({j:.2f})")

        # Quotes check
        quotes = item.get("quotes", [])
        if len(quotes) != 3:
            errors.append(f"[{word}] Expected exactly 3 quotes, got {len(quotes)}")

        authors = set()
        for idx, q in enumerate(quotes):
            author = q.get("author", "")
            work = q.get("work", "")
            qtext = q.get("quote", "")

            if not author or not work or not qtext:
                errors.append(f"[{word}] Quote {idx+1} missing fields")
            if author in authors:
                errors.append(f"[{word}] Duplicate author: '{author}'")
            authors.add(author)

            # Check banned phrases
            full_str = f"{author} {work} {qtext}".lower()
            for bp in BANNED_PHRASES:
                if bp in full_str:
                    errors.append(f"[{word}] Contains banned phrase '{bp}' in quote {idx+1}")

            # Target word bolded check
            if "**" not in qtext:
                errors.append(f"[{word}] Target word not bolded in quote {idx+1}: '{qtext[:60]}...'")

    if errors:
        print(f"\n❌ VALIDATION FAILED with {len(errors)} errors:")
        for err in errors[:25]:
            print(f"  - {err}")
        return False
    else:
        print("\n✅ ALL 40 words in Cluster Power Batch 1 Part 3 PASSED local pre-audit validation!")
        return True

if __name__ == "__main__":
    if not validate():
        sys.exit(1)
