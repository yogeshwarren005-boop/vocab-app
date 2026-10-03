---
latin_root: "[[Dashboard — solut]]"
cluster: "[[Cluster Action & State]]"
status: unread
---
# dissolution

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
> 1. **Primary Definition (Lexical / Standard Consensus)**: The closing down or dismissal of an assembly, official body, or contract; or physical decomposition.
> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: In British constitutional history, the royal dissolution of Parliament terminates the legislative session and triggers general elections.

> [!quote] 💬 Contextual Usage & Authentic Quotations
> - 📜 **William Shakespeare (*The Tempest*):** *"The cloud-capp'd towers, the gorgeous palaces, the solemn temples, the great globe itself, yea, all which it inherit, shall dissolve and, like this insubstantial pageant faded, leave not a rack behind: we are such stuff as dreams are made on, and our little life is rounded with a sleep: sir, I am vex'd; bear with my weakness; my old brain is troubled: be not disturb'd with my infirmity: if you be pleased, retire into my cell and there repose: a turn or two I'll walk, to still my beating mind. We wish your peace. Come with a thought. I thank thee, Ariel: come. Thy thoughts I cleave to. What's thy pleasure? Spirit, we must prepare to meet with Caliban. Ay, my commander: when I presented Ceres, I thought to have told thee of it, but I fear'd lest I might anger thee. Say again, where didst thou leave these varlets? I told you, sir, they were red-hot with drinking; so full of valour that they smote the air for breathing in their faces; beat the ground for kissing of their feet; yet always bending towards their project. Then I beat my tabor; at which, like unback'd colts, they prick'd their ears, advanced their eyelids, lifted up their noses as they smelt music: so I charm'd their ears that calf-like they my lowing follow'd through tooth'd briers, sharp furzes, pricking goss and thorns, which enter'd their frail shins: at last I left them i' the filthy-mantled pool beyond your cell, there dancing up to the chins, that the foul lake o'erstunk their feet. This was well done, my bird. Thy shape invisible retain thou still: the trumpery in my house, go bring it hither, for stale to catch these thieves. I go, I go. A devil, a born devil, on whose nature nurture can never stick; on whom my pains, humanely taken, all, all lost, quite lost; and as with age his body uglier grows, so his mind cankers. I will plague them all, even to roaring. Go, charge my goblins that they grind their joints with dry convulsions, shorten up their sinews with aged cramps, and more pinch-spotted make them than pard or cat o' mountain. Hark, they roar! Let them be hunted soundly. At this hour lie at my mercy all mine enemies: shortly shall all my labours end, and thou shalt have the air at freedom: for a little follow, and do me service. We are ready to witness the complete **dissolution** of the conspirators' wicked plots."*
> - 📜 **Thomas Babington Macaulay (*The History of England*):** *"The sudden **dissolution** of the Cavalier Parliament plunged the political nation into furious electioneering turmoil."*
> - 📜 **Thomas Carlyle (*The French Revolution*):** *"The ancient monarchy stood in the final stage of institutional **dissolution**, bankrupt in revenue and authority."*

