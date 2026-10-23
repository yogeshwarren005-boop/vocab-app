---
latin_root: "[[Dashboard — nat]]"
cluster: "[[Cluster Life]]"
status: unread
tier: 1
tier_label: "Words to learn first"
zipf: 4
rank: 1002
---

# nature

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
> 1. **Primary Definition (Lexical / Standard Consensus)**: The physical world collective, including plants, animals, the landscape, and other natural features.
> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: The basic or inherent features, character, or qualities of something or someone.

> [!quote] 💬 Contextual Usage & Authentic Quotations
> - 📜 **William Shakespeare (*As You Like It*):** *"Sweet are the uses of adversity, / Which, like the toad, ugly and venomous, / Wears yet a precious jewel in his head; / And this our life, exempt from public haunt, / Finds tongues in trees, books in the running brooks, / Sermons in stones, and good in every thing. / I would not change it. / Happy is your grace, / That can translate the stubbornness of fortune / Into so quiet and so sweet a style. / Come, shall we go and kill us venison? / And yet it irks me, the poor dappled fools, / Being native burghers of this desert city, / Should in their own confines with forked heads / Have their round haunches gored. / Indeed, my lord, / The melancholy Jaques grieves at that; / And, in that kind, swears you do more usurp / Than doth your brother that hath banish'd you. / To-day my Lord of Amiens and myself / Did steal behind him as he lay along / Under an oak whose antique root peeps out / Upon the brook that brawls along this wood: / To the which place a poor sequester'd stag, / That from the hunter's aim had ta'en a hurt, / Did come to languish; and indeed, my lord, / The wretched animal heaved forth such groans / That their discharge did stretch his leathern coat / Almost to bursting, and the big round tears / Coursed one another down his innocent nose / In piteous chase; and thus the hairy fool, / Much marked of the melancholy Jaques, / Stood on the extremest verge of the swift brook, / Augmenting it with tears. / But what said Jaques? / Did he not moralize this spectacle? / O, yes, into a thousand similes. / First, for his weeping into the needless stream; / 'Poor deer,' quoth he, 'thou makest a testament / As worldlings do, giving thy sum of more / To that which had too much:' then, being there alone, / Left and abandon'd of his velvet friends; / ''Tis right:' quoth he; 'thus misery doth part / The flux of company:' anon a careless herd, / Full of the pasture, jumps along by him / And never stays to greet him; 'Ay' quoth Jaques, / 'Sweep on, you fat and greasy citizens; / 'Tis just the fashion: wherefore do you look / Upon that poor and broken bankrupt there?' / Thus most invectively he pierceth through / The body of the country, city, court, / Yea, and of this our life; swearing that we / Are mere usurpers, tyrants and what's worse, / To fright the animals and to kill them up / In their assign'd and native dwelling-place. / And did you leave him in this contemplation? / We did, my lord, weeping and commenting / Upon the sobbing deer. / Show me the place: / I love to cope him in these sullen fits, / For then he's full of matter. / I'll bring you to him straight, where **nature** reigns."*
> - 📜 **Ralph Waldo Emerson (*Nature*):** *"In the woods, we return to reason and faith; standing on the bare ground, all mean egotism vanishes, I become a transparent eyeball; I am nothing; I see all; the currents of the Universal Being circulate through me; I am part or parcel of God. In **nature** every creature finds its solace."*
> - 📜 **Charles Darwin (*The Origin of Species*):** *"There is grandeur in this view of life, with its several powers, having been originally breathed into a few forms or into one; and that, whilst this planet has gone cycling on according to the fixed law of gravity, from so simple a beginning endless forms most beautiful and most wonderful have been, and are being, evolved. Such is the magnificent spectacle of **nature**."*
