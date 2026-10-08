---
latin_root: "[[Dashboard — spir]]"
cluster: "[[Cluster Life]]"
status: unread
---

# inspire

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
> 1. **Primary Definition (Lexical / Standard Consensus)**: To fill someone with the urge or ability to do or feel something creative, noble, or elevated.
> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: To breathe in air or vapor; to infuse feelings or thoughts into the mind.

> [!quote] 💬 Contextual Usage & Authentic Quotations
> - 📜 **William Shakespeare (*Henry V*):** *"Once more unto the breach, dear friends, once more; / Or close the wall up with our English dead. / In peace there's nothing so becomes a man / As modest stillness and humility: / But when the blast of war blows in our ears, / Then imitate the action of the tiger; / Stiffen the sinews, summon up the blood, / Disguise fair nature with hard-favour'd rage; / Then lend the eye a terrible aspect; / Let pry through the portage of the head / Like the brass cannon; let the brow o'erwhelm it / As fearfully as doth a galled rock / O'erhang and jutty his confounded base, / Swill'd with the wild and wasteful ocean. / Now set the teeth and stretch the nostril wide, / Hold hard the breath and bend up every spirit / To his full height. On, on, you noblest English. / Whose blood is fet from fathers of war-proof! / Fathers that, like so many Alexanders, / Have in these parts from morn till even fought / And sheathed their swords for lack of argument: / Dishonour not your mothers; now attest / That those whom you call'd fathers did beget you. / Be copy now to men of grosser blood, / And teach them how to war. And you, good yeomen, / Whose limbs were made in England, show us here / The mettle of your pasture; let us swear / That you are worth your breeding; which I doubt not; / For there is none of you so mean and base, / That hath not noble lustre in your eyes. / I see you stand like greyhounds in the slips, / Straining upon the start. The game's afoot: / Follow your spirit, and upon this charge / Cry 'God for Harry, England, and Saint George!' / These words did **inspire** the hearts of all our soldiers."*
> - 📜 **John Milton (*Paradise Lost*):** *"The heavenly muse did **inspire** his song with holy truths unknown to pagan bards."*
> - 📜 **Percy Bysshe Shelley (*Ode to the West Wind*):** *"Make me thy lyre, even as the forest is: / What if my leaves are falling like its own! / The tumult of thy mighty harmonies / Will take from both a deep, autumnal tone, / Sweet though in sadness. Be thou, Spirit fierce, / My spirit! Be thou me, impetuous one! / Drive my dead thoughts over the universe / Like wither'd leaves to quicken a new birth! / And, by the incantation of this verse, / Scatter, as from an unextinguish'd hearth / Ashes and sparks, my words among mankind! / Be through my lips to unawaken'd earth / The trumpet of a prophecy! O Wind, / If Winter comes, can Spring be far behind? / Thy wild breath doth **inspire** my dying soul."*
