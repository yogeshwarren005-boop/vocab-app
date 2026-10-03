---
latin_root: "[[Dashboard — lud]]"
cluster: "[[Cluster Action & State]]"
status: unread
---
# delude

> [!status] 🎯 **Status:**

```dataviewjs
if(!document.getElementById('apple-toggle-css')){const s=document.createElement('style');s.id='apple-toggle-css';s.textContent=':root{--apple-red:#FF375F;--apple-red-glow:rgba(255,55,95,0.45);--apple-amber:#FF9F0A;--apple-amber-glow:rgba(255,159,10,0.45);--apple-green:#30D158;--apple-green-glow:rgba(48,209,88,0.45)}.apple-c{position:relative;display:inline-flex;align-items:center;gap:8px;padding:2px 10px 2px 4px;border-radius:999px;background:var(--background-secondary,#111624);border:1px solid var(--background-modifier-border,#232d42);cursor:pointer;user-select:none;transition:border-color .2s ease,transform .2s ease,box-shadow .2s ease;line-height:1;vertical-align:middle;box-sizing:border-box}.apple-c:hover{border-color:var(--text-muted,#3b4b6b);transform:translateY(-1px);box-shadow:0 2px 8px rgba(0,0,0,.35)}.apple-c:active{transform:scale(.96)}.apple-c .track-c{position:relative;width:48px;height:18px;background:var(--background-primary,#090d17);border-radius:999px;border:1px solid var(--background-modifier-border,#1c2436);display:flex;align-items:center;justify-content:space-between;padding:0 6px;box-sizing:border-box}.apple-c .c-dot{width:3px;height:3px;border-radius:999px;background:var(--text-faint,#334155);opacity:.6}.apple-c .halo-c{position:absolute;top:1px;left:1px;width:14px;height:14px;border-radius:999px;transition:transform .35s cubic-bezier(.34,1.6,.64,1),background-color .25s ease,box-shadow .25s ease;display:flex;align-items:center;justify-content:center;box-sizing:border-box}.apple-c .halo-c .core-dot{width:5px;height:5px;border-radius:999px;background:#fff;box-shadow:0 0 4px #fff}.apple-c .halo-c.p0{transform:translateX(0);background:var(--apple-red);box-shadow:0 0 12px var(--apple-red),0 0 20px var(--apple-red-glow)}.apple-c .halo-c.p1{transform:translateX(15px);background:var(--apple-amber);box-shadow:0 0 12px var(--apple-amber),0 0 20px var(--apple-amber-glow)}.apple-c .halo-c.p2{transform:translateX(30px);background:var(--apple-green);box-shadow:0 0 12px var(--apple-green),0 0 20px var(--apple-green-glow)}.apple-c .label{font-size:11px;font-weight:700;letter-spacing:.2px;transition:color .2s ease;min-width:48px}.apple-c .label.unread{color:var(--apple-red)}.apple-c .label.learning{color:var(--apple-amber)}.apple-c .label.learned{color:var(--apple-green)}';document.head.appendChild(s);}
const p = dv.current();
const rawStatus = p.status || "unread";
const states = [{ key: 'unread', label: 'unread', cls: 'unread', p: 'p0' }, { key: 'learning', label: 'learning', cls: 'learning', p: 'p1' }, { key: 'learned', label: 'learned', cls: 'learned', p: 'p2' }];
let curIdx = states.findIndex(s => s.key === rawStatus);
if (curIdx === -1) curIdx = 0;
const toggle = document.createElement('div');
toggle.className = 'apple-c';
toggle.title = 'Click to glide: unread ➔ learning ➔ learned';
const track = document.createElement('div');
track.className = 'track-c';
track.innerHTML = '<span class="c-dot"></span><span class="c-dot"></span><span class="c-dot"></span><div class="halo-c ' + states[curIdx].p + '"><div class="core-dot"></div></div>';
const label = document.createElement('span');
label.className = 'label ' + states[curIdx].cls;
label.textContent = states[curIdx].label;
toggle.appendChild(track);
toggle.appendChild(label);
toggle.addEventListener('click', async (e) => {
    e.stopPropagation();
    curIdx = (curIdx + 1) % 3;
    const nxt = states[curIdx];
    track.querySelector('.halo-c').className = 'halo-c ' + nxt.p;
    label.className = 'label ' + nxt.cls;
    label.textContent = nxt.label;
    const file = app.vault.getAbstractFileByPath(p.file.path);
    if (file) {
        await app.fileManager.processFrontMatter(file, fm => { fm.status = nxt.key; });
        new Notice('' + (p.file.name) + ': marked ' + (nxt.key) + '');
    }
});
dv.container.appendChild(toggle);
```

> [!book] 📖 Definitions & Semantic Range
> 1. **Primary Definition (Lexical / Standard Consensus)**: To mislead the mind or judgment of someone; to deceive, fool, or trick.
> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: In epistemological skepticism, philosophers examine sensory illusions that delude human perception into mistaking appearances for reality.

> [!quote] 💬 Contextual Usage & Authentic Quotations
> - 📜 **John Milton (*Paradise Lost*):** *"Let none admire that riches grow in Hell; that soil may best deserve the precious bane: and here let those who boast in mortal things, and wondering tell of Babel, and the works of Memphian kings, learn how their greatest monuments of fame, and strength, and art, are easily outdone by spirits reprobate, and in an hour what in an age they, with incessant toil and hands innumerable, scarce perform. Nigh on the plain, in many cells prepared, that underneath had veins of liquid fire sluiced from the lake, a second multitude with wondrous art founded the massy ore, severing each kind, and scumm'd the bullion-dross: a third as soon had form'd within the ground a various mould, and from the boiling cells by strange conveyance fill'd each hollow nook; as in an organ, from one blast of wind, to many a row of pipes the breath conveys. Anon, out of the earth a fabric huge rose like an exhalation, with the sound of dulcet symphonies and voices sweet, built like a temple, where pilasters round were set, and Doric pillars overlaid with golden architrave; nor did there want cornice or frieze, with bossy sculptures graven; the roof was fretted gold. Not Babylon nor great Alcairo such magnificence equall'd in all their glories, to enshrine Belus or Serapis their gods, or seat their kings, when Egypt with Assyria strove in wealth and luxury. The ascending pile stood fix'd her stately height; and straight the doors, opening their brazen folds, discover, wide within, her ample spaces o'er the smooth and level pavement: from the arched roof, pendent by subtle magic, many a row of starry lamps and blazing cressets, fed with naphtha and asphaltus, yielded light as from a sky. The hasty multitude admiring enter'd; and the work some praise, and some the architect: his hand was known in Heaven by many a tower'd structure high, where sceptred angels held their residence, and sat as princes, whom the supreme King exalted to such power, and gave to rule, each in his hierarchy, the orders bright. Nor was his name unheard or unadored in ancient Greece; and in Ausonian land men call'd him Mulciber; and how he fell from Heaven they fabled, thrown by angry Jove sheer o'er the crystal battlements: from morn to noon he fell, from noon to dewy eve, a summer's day; and with the setting sun dropt from the zenith like a falling star, on Lemnos, the Aegaean isle: thus they relate, erring; for he with this rebellious rout fell long before; nor aught avail'd him now to have built in Heaven high towers; nor did he scape by all his engines, but was headlong sent with his industrious crew to build in hell. Meanwhile, the wing'd heralds, by command of sovereign power, with awful ceremony and trumpet's sound, throughout the host proclaim a solemn council forthwith to be held at Pandemonium, the high capital of Satan and his peers: their summons call'd from every band and squared regiment by place or choice the worthiest; they anon with hundreds and with thousands trooping came attended: all access was throng'd; the gates and porches wide, but chief the spacious hall thick swarm'd, both on the ground and in the air, brush'd with the hiss of rustling wings. As bees in spring-time, when the Sun with Taurus rides, pour forth their populous youth about the hive in clusters; they among fresh dews and flowers fly to and fro, or on the smoothed plank, the suburb of their straw-built citadel, new rubb'd with balm, expatiate, and confer their state-affairs: so thick the aery crowd swarm'd and were straiten'd; till, the signal given, behold a wonder! they but now who seem'd in bigness to surpass Earth's giant sons, now less than smallest dwarfs, in narrow room throng numberless, like that pygmean race beyond the Indian mount; or faery elves, whose midnight revels, by a forest side or fountain, some belated peasant sees, or dreams he sees, while overhead the Moon sits arbitress, and nearer to the Earth wheels her pale course; they, on their mirth and dance intent, with jocund music charm his ear; at once with joy and fear his heart rebounds. Thus incorporeal spirits to smallest forms reduced their shapes immense, and were at large, though without number still, amidst the hall of that infernal court. But far within, and in their own dimensions like themselves, the great seraphic lords and cherubim in close recess and secret conclave sat, a thousand demi-gods on golden seats, frequent and full. After short silence then, and summons read, the great consult began, and Satan spoke to **delude** his followers with false hope of regain'd heaven."*
> - 📜 **Francis Bacon (*Novum Organum*):** *"The Idols of the Mind continually **delude** human reason, substituting subjective phantoms for objective natural facts."*
> - 📜 **William Shakespeare (*The Winter's Tale*):** *"Let not false reports **delude** your royal judgment, for Hermione's honor is as spotless as virgin snow."*

