---
latin_root: "[[Dashboard — spir]]"
cluster: "[[Cluster Life]]"
status: unread
tier: 2
tier_label: "Words to learn a little later"
zipf: 2.3
rank: 11272
---

# spiral

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
> 1. **Primary Definition (Lexical / Standard Consensus)**: Winding continuously around a central point or axis in an advancing curve.
> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: A continuous curve described by a point moving around a fixed center at an increasing distance.

> [!quote] 💬 Contextual Usage & Authentic Quotations
> - 📜 **John Milton (*Paradise Lost*):** *"Not with indented wave, / Prone on the ground, as since, but on his rear, / Circular base of rising folds, that towered / Fold above fold, a surging maze; his head / Crested aloft, and carbuncle his eyes; / With burnished neck of verdant gold, erect / Amidst his circling spires, that on the grass / Floated redundant: pleasing was his shape / And lovely; never since of serpent kind / Lovelier; not those that in Illyria changed / Hermione and Cadmus, or the god / In Epidaurus; nor to which transformed / Ammonian Jove, or Capitoline, was seen, / He with Olympias, this with her that bore / Scipio, the height of Rome. With tract oblique / At first, as one who sought access but feared / To interrupt, sidelong he works his way. / As when a ship, by skilful steersman wrought, / Nigh river's mouth or foreland, where the wind / Veers oft, as oft so steers, and shifts her sail: / So varied he, and of his tortuous train / Curled many a wanton wreath in sight of Eve, / To lure her eye; she, busied, heard the sound / Of rustling leaves, but minded not, as used / To such disport before her through the field / From every beast, more duteous at her call / Than at Circean call the herd disguised. / He, bolder now, uncalled before her stood, / But as in gaze admiring: oft he bowed / His turret crest, and sleek enamelled neck, / Fawning, and licked the ground whereon she trod. / His sleek coils moved in a gleaming **spiral**."*
> - 📜 **Charles Darwin (*The Movements and Habits of Climbing Plants*):** *"The growing stem of the hop plant revolves in a regular **spiral** to find support."*
> - 📜 **Thomas Henry Huxley (*Physiography*):** *"Cyclonic storms advance across ocean basins in a vast rotating **spiral** of atmospheric pressure."*
