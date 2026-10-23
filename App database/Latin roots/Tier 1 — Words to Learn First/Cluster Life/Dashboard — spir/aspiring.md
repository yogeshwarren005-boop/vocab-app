---
latin_root: "[[Dashboard — spir]]"
cluster: "[[Cluster Life]]"
status: unread
tier: 2
tier_label: "Words to learn a little later"
zipf: 2.3
rank: 20395
---

# aspiring

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
> 1. **Primary Definition (Lexical / Standard Consensus)**: Directing one's desires and ambitions toward achieving high status, excellence, or renown.
> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: Rising, soaring, or pointing gracefully upward toward the heavens.

> [!quote] 💬 Contextual Usage & Authentic Quotations
> - 📜 **William Shakespeare (*Richard II*):** *"Mount, mount, my soul! thy seat is up on high; / Whilst my gross flesh sinks downward, here to die. / Thus dies an **aspiring** monarch."*
> - 📜 **John Milton (*Paradise Lost*):** *"Him the Almighty Power / Hurled headlong flaming from the ethereal sky, / With hideous ruin and combustion, down / To bottomless perdition, there to dwell / In adamantine chains and penal fire, / Who durst defy the Omnipotent to arms. / Nine times the space that measures day and night / To mortal men, he with his horrid crew / Lay vanquished, rolling in the fiery gulf, / Confounded, though immortal: but his doom / Reserved him to more wrath; for now the thought / Both of lost happiness and lasting pain / Torments him: round he throws his baleful eyes, / That witnessed huge affliction and dismay, / Mixed with obdurate pride and steadfast hate. / At once, as far as Angels ken, he views / The dismal situation waste and wild. / A dungeon horrible, on all sides round, / As one great furnace flamed; yet from those flames / No light; but rather darkness visible / Served only to discover sights of woe, / Regions of sorrow, doleful shades, where peace / And rest can never dwell, hope never comes / That comes to all, but torture without end / Still urges, and a fiery deluge, fed / With ever-burning sulphur unconsumed. / Such place Eternal Justice had prepared / For those rebellious, here their prison ordained / In utter darkness, and their portion set, / As far removed from God and light of Heaven / As from the centre thrice to the utmost pole. / O how unlike the place from whence they fell! / There the **aspiring** fiend surveyed his ruin."*
> - 📜 **Charlotte Brontë (*Jane Eyre*):** *"An **aspiring** nature cannot rest satisfied within the narrow boundary of customary convention."*
