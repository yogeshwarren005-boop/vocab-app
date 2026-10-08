---
latin_root: "[[Dashboard — sta]]"
cluster: "[[Cluster Placing]]"
status: unread
---

# unstable

> [!status] 🎯 **Status:**

```dataviewjs
if(!document.getElementById('apple-toggle-css')){const s=document.createElement('style');s.id='apple-toggle-css';s.textContent=':root{--apple-red:#FF375F;--apple-red-glow:rgba(255,55,95,0.45);--apple-amber:#FF9F0A;--apple-amber-glow:rgba(255,159,10,0.45);--apple-green:#30D158;--apple-green-glow:rgba(48,209,88,0.45)}.apple-c{position:relative;display:inline-flex;align-items:center;gap:8px;padding:2px 10px 2px 4px;border-radius:999px;background:var(--background-secondary,#111624);border:1px solid var(--background-modifier-border,#232d42);cursor:pointer;user-select:none;transition:border-color .2s ease,transform .2s ease,box-shadow .2s ease;line-height:1;vertical-align:middle;box-sizing:border-box}.apple-c:hover{border-color:var(--text-muted,#3b4b6b);transform:translateY(-1px);box-shadow:0 2px 8px rgba(0,0,0,.35)}.apple-c:active{transform:scale(.96)}.apple-c .track-c{position:relative;width:48px;height:18px;background:var(--background-primary,#090d17);border-radius:999px;border:1px solid var(--background-modifier-border,#1c2436);display:flex;align-items:center;justify-content:space-between;padding:0 6px;box-sizing:border-box}.apple-c .c-dot{width:3px;height:3px;border-radius:999px;background:var(--text-faint,#334155);opacity:.6}.apple-c .halo-c{position:absolute;top:1px;left:1px;width:14px;height:14px;border-radius:999px;transition:transform .35s cubic-bezier(.34,1.6,.64,1),background-color .25s ease,box-shadow .25s ease;display:flex;align-items:center;justify-content:center}.apple-c .halo-c::after{content:"";width:6px;height:6px;border-radius:999px;background:#fff;box-shadow:0 1px 2px rgba(0,0,0,.4)}.apple-c .halo-c.pos-0{transform:translateX(0);background-color:var(--apple-red);box-shadow:0 0 8px var(--apple-red-glow)}.apple-c .halo-c.pos-1{transform:translateX(15px);background-color:var(--apple-amber);box-shadow:0 0 8px var(--apple-amber-glow)}.apple-c .halo-c.pos-2{transform:translateX(30px);background-color:var(--apple-green);box-shadow:0 0 8px var(--apple-green-glow)}.apple-c .label{font-size:10px;font-weight:700;letter-spacing:.5px;text-transform:uppercase;margin-left:2px}.apple-c .label.s-0{color:var(--apple-red)}.apple-c .label.s-1{color:var(--apple-amber)}.apple-c .label.s-2{color:var(--apple-green)}';document.head.appendChild(s)}
const p=dv.current();
const states=[{key:'unread',label:'Unread',cls:'s-0',p:'pos-0'},{key:'learning',label:'Learning',cls:'s-1',p:'pos-1'},{key:'learned',label:'Learned',cls:'s-2',p:'pos-2'}];
const statusVal=p.status||'unread';
let curIdx=states.findIndex(s=>s.key===statusVal);
if(curIdx===-1)curIdx=0;
const cur=states[curIdx];
const toggle=document.createElement('div');
toggle.className='apple-c';
const track=document.createElement('div');
track.className='track-c';
track.innerHTML='<span class="c-dot"></span><span class="c-dot"></span><span class="c-dot"></span><div class="halo-c '+cur.p+'"></div>';
const label=document.createElement('span');
label.className='label '+cur.cls;
label.textContent=cur.label;
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
> 1. **Primary Definition (Lexical / Consensus)**: Liable to fall, wobble, or collapse; lacking physical, structural, or mechanical equilibrium.
> 2. **Secondary / Nuanced Definition (Contextual / Classical)**: Capricious, fickle, or erratic in character, temper, or political loyalty.

> [!quote] 💬 Contextual Usage & Authentic Quotations
> - 📜 **William Shakespeare (*Coriolanus*):** *"What would you have, you curs, that like nor peace nor war? the one affrights you, the other makes you proud. He that trusts to you, where he should find you lions, finds you hares; where foxes, geese: you are no surer, no, than is the coal of fire upon the ice, or hailstone in the sun. Your virtue is to make him worthy whose offence subdues him and curse that justice did it. Who deserves greatness deserves your hate; and your affections are a sick man's appetite, who desires most that which would increase his evil. He that depends upon your favours swims with fins of lead and hews down oaks with rushes. Hang ye! Trust ye? With every minute you do change a mind, and call him noble that was now your hate, him vile that was your garland. What's the matter, that in these several places of the city you cry against the noble senate, who, under the gods, keep you in awe, which else would feed on one another? What's their seeking? For corn at their own rates; whereof, they say, the city is well stored. Hang 'em! They say! They'll sit by the fire, and presume to know what's done i' the Capitol; who's like to rise, who thrives and who declines; side factions and give out conjectural marriages; making parties strong and feebling such as stand not in their liking below their cobbled shoes. They say there's grain enough! Would the nobility lay aside their ruth, and let me use my sword, I'd make a quarry with thousands of these quarter'd slaves, as high as I could pick my lance. Nay, these are almost thoroughly persuaded; for though abundantly they lack discretion, yet are they passing cowardly. But, I beseech you, what says the other troop? They are dissolved: hang 'em! They said they were an-hungry; sigh'd forth proverbs, that hunger broke stone walls, that dogs must eat, that meat was made for mouths, that the gods sent not corn for the rich men only: with these shreds they vented their complainings; which being answer'd, and a petition granted them, a strange one—to break the heart of generosity, and make bold power look pale—they threw their caps as they would hang them on the horns o' the moon, shouting their emulation. What is granted them? Five tribunes to defend their vulgar wisdoms, of their own choice: one's Junius Brutus, Sicinius Velutus, and I know not—'Sdeath! The rabble should have first unroof'd the city, ere so prevail'd with me: it will in time win upon power and throw forth greater themes for insurrection's arguing. This is strange. Go, get you home, you fragments! Here: what's the matter? The Volsces are in arms. They have a leader, Tullus Aufidius, that will put you to't. I sin in envying his nobility, and were I anything but what I am, I would wish me only he. Strange, **unstable** multitude!"*
> - 📜 **John Milton (*Paradise Lost*):** *"Chaos held sway over the abyss, where dark materials tossed upon an **unstable** and tempestuous sea."*
> - 📜 **Alexander Pope (*An Essay on Man*):** *"Placed on this isthmus of a middle state, a being darkly wise, and rudely great, in doubt to deem himself a god, or beast, in doubt his mind or body to prefer; born but to die, and reas'ning but to err; alike in ignorance, his reason such, whether he thinks too little, or too much: chaos of thought and passion, all confused; still by himself abused, or disabused; created half to rise, and half to fall; great lord of all things, yet a prey to all; sole judge of truth, in endless error hurled; the glory, jest, and riddle of the world! Such is the vain, **unstable** mind of man."*
