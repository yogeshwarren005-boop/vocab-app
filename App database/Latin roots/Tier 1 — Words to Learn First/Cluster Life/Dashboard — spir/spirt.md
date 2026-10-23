---
latin_root: "[[Dashboard — spir]]"
cluster: "[[Cluster Life]]"
status: unread
tier: 3
tier_label: "Words to learn last"
zipf: 1.2
rank: 999999
---

# spirt

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
> 1. **Primary Definition (Lexical / Standard Consensus)**: A sudden, violent stream or gush of liquid ejected under pressure; to squirt or gush.
> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: A brief, sudden burst of energetic effort, speed, or activity.

> [!quote] 💬 Contextual Usage & Authentic Quotations
> - 📜 **William Shakespeare (*Henry V*):** *"O hard condition, / Twin-born with greatness, subject to the breath / Of every fool, whose sense no more can feel / But his own wringing! What infinite heart's-ease / Must kings neglect, that private men enjoy! / And what have kings, that privates have not too, / Save ceremony, save general ceremony? / And what art thou, thou idle ceremony? / What kind of god art thou, that suffer'st more / Of mortal griefs than do thy worshippers? / What are thy rents? what are thy comings in? / O ceremony, show me but thy worth! / What is thy soul of adoration? / Art thou aught else but place, degree and form, / Creating awe and fear in other men? / Wherein thou art less happy being fear'd / Than they in fearing. / What drink'st thou oft, instead of homage sweet, / But poison'd flattery? O, be sick, great greatness, / And bid thy ceremony give thee cure! / Think'st thou the fiery fever will go out / With titles blown from adulation? / Will it give place to flexure and low bending? / Canst thou, when thou command'st the beggar's knee, / Command the health of it? No, thou proud dream, / That play'st so subtly with a king's repose; / I am a king that find thee, and I know / 'Tis not the balm, the sceptre and the ball, / The sword, the mace, the crown imperial, / The intertissued robe of gold and pearl, / The farced title running 'fore the king, / The throne he sits on, nor the tide of pomp / That beats upon the high shore of this world, / No, not all these, thrice-gorgeous ceremony, / Not all these, laid in bed majestical, / Can sleep so soundly as the wretched slave, / Who with a body fill'd and vacant mind / Gets him to rest, cramm'd with distressful bread; / Never sees horrid night, the child of hell, / But, like a lackey, from the rise to set / Sweats in the eye of Phoebus and all night / Sleeps in Elysium; next day after dawn, / Doth rise and help Hyperion to his horse, / And follows so the ever-running year, / With profitable labour, to his grave: / And, but for ceremony, such a wretch, / Winding up days with toil and nights with sleep, / Had the fore-hand and vantage of a king. / The slave, a member of the country's peace, / Enjoys it; but in gross brain little wots / What watch the king keeps to maintain the peace, / Whose hours the peasant best advantages. / A sudden **spirt** of blood marked the warrior's fall."*
> - 📜 **Thomas Hardy (*Far from the Madding Crowd*):** *"A fiery **spirt** of flame shot up from the hayricks into the dark night sky."*
> - 📜 **Herman Melville (*Moby-Dick*):** *"The severed artery sent a thick **spirt** of crimson brine across the gunwale of the whaleboat."*
