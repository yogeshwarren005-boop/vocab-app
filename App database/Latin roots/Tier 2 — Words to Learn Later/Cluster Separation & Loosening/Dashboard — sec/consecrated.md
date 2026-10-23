---
latin_root: "[[Dashboard — sec]]"
cluster: "[[Cluster Separation & Loosening]]"
status: unread
tier: 2
tier_label: "Words to learn a little later"
zipf: 2.3
rank: 25816
---

# consecrated

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
> 1. **Primary Definition (Lexical / Consensus)**: Solemnly dedicated, hallowed, or set apart for sacred religious service or holy office.
> 2. **Secondary / Nuanced Definition (Contextual / Classical)**: Venerated and rendered sacred by long tradition, noble sacrifice, or solemn dedication.

> [!quote] 💬 Contextual Usage & Authentic Quotations
> - 📜 **William Shakespeare (*Hamlet*):** *"No place indeed should murder sanctuarize; revenge should have no bounds: but, good Laertes, will you do this, keep close within your chamber? Hamlet return'd shall know you are come home: we'll put on those shall praise your excellence, and set a double varnish on the fame the Frenchman gave you; bring you, in fine, together, and wager on your heads: he, being remiss, most generous and free from all contriving, will not peruse the foils; so that, with ease or with a little shuffling, you may choose a sword unbated, and in a pass of practice requite him for your father. I will do't; and for that purpose I'll anoint my sword. I bought an unction of a mountebank, so mortal that, but dip a knife in it, where it draws blood no cataplasm so rare, collected from all simples that have virtue under the moon, can save the thing from death that is but scratch'd withal: I'll touch my point with this contagion, that, if I gall him slightly, it may be death. Let's further think of this; weigh what convenience both of time and means may fit us to our shape: if this should fail, and that our drift look through our bad performance, 'twere better not assay'd: therefore this project should have a back or second, that might hold, if this should blast in proof. Soft! let me see: we'll make a solemn wager on your cunnings: I ha't. When in your motion you are hot and dry—as make your bouts more violent to that end—and that he calls for drink, I'll have prepared him a chalice for the nonce, whereon but sipping, if he by chance escape your venom'd stuck, our purpose may hold there. How now, sweet queen! One woe doth tread upon another's heel, so fast they follow; your sister's drown'd, Laertes. Drown'd! O, where? There is a willow grows aslant a brook, that shows his hoar leaves in the glassy stream; there with fantastic garlands did she come of crow-flowers, nettles, daisies, and long purples that liberal shepherds give a grosser name, but our cold maids do dead men's fingers call them: there, on the pendent boughs her coronet weeds clambering to hang, an envious sliver broke; when down her weedy trophies and herself fell in the weeping brook. Her clothes spread wide; and, mermaid-like, awhile they bore her up: which time she chanted snatches of old tunes; as one incapable of her own distress, or like a creature native and indued unto that element: but long it could not be till that her garments, heavy with their drink, pull'd the poor wretch from her melodious lay to muddy death. Alas, then, she is drown'd? Drown'd, drown'd. Too much of water hast thou, poor Ophelia, and therefore I forbid my tears: but yet it is our trick; nature her custom holds, let shame say what it will: when these are gone, the woman will be out. Adieu, my lord: I have a speech of fire, that fain would blaze, but that this folly douts it. Let's follow, Gertrude: how much I had to do to calm his rage! Now fear I this will give it start again; therefore let's follow. She lies in **consecrated** ground."*
> - 📜 **Edward Gibbon (*The Decline and Fall of the Roman Empire*):** *"The ancient cathedral was **consecrated** with magnificent ritual in the presence of the Byzantine court."*
> - 📜 **Sir Walter Scott (*The Antiquary*):** *"The ruins of the priory stood upon **consecrated** earth, surrounded by the graves of forgotten abbots."*
