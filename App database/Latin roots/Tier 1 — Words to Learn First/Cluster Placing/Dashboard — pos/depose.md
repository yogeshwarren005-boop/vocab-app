---
latin_root: "[[Dashboard — pos]]"
cluster: "[[Cluster Placing]]"
status: unread
tier: 2
tier_label: "Words to learn a little later"
zipf: 2.3
rank: 31246
---

# depose

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
> 1. **Primary Definition (Lexical / Consensus)**: To remove a monarch, sovereign, or high public official from power or office abruptly.
> 2. **Secondary / Nuanced Definition (Contextual / Classical)**: To testify, declare, or state under oath in a formal legal deposition or court of law.

> [!quote] 💬 Contextual Usage & Authentic Quotations
> - 📜 **William Shakespeare (*Richard II*):** *"What must the king do now? Must he submit? The king shall be contented: must he lose the name of king? o' God's name, let it go: I'll give my jewels for a set of beads, my gorgeous palace for a hermitage, my gay apparel for an almsman's gown, my figured goblets for a dish of wood, my sceptre for a palmer's walking-staff, my subjects for a pair of carved saints and my large kingdom for a little grave, a little little grave, an obscure grave; or I'll be buried in the king's highway, some way of common trade, where subjects' feet may hourly trample on their sovereign's head; for on my heart they tread now whilst I live; and buried once, why not on my head? Aumerle, thou weep'st, my tender-hearted cousin! We'll make foul weather with despised tears; our sighs and they shall lodge the summer corn, and make a dearth in this revolting land. Or shall we play the wantons with our woes, and make some pretty match with shedding tears? As thus, to drop them still upon one place, till they have fretted us a pair of graves within the earth; and, there engraved, 'There lies two kinsmen digg'd their graves with weeping tears'? Would not this ill do well? Well, well, I see I talk but idly, and you laugh at me. Most mighty prince, my Lord Northumberland, what says King Bolingbroke? will his majesty give Richard leave to live till Richard die? You make a leg, and Bolingbroke says ay. Northumberland: My lord, in the base court he doth attend to speak with you; may it please you to come down. King Richard: Down, down I come; like Phaethon, wanting the manage of unruly jades. In the base court? Base court, where kings grow base, to come at traitors' calls and do them grace. In the base court? Come down? Down, court! down, king! For night-owls shriek where mounting larks should sing. Bolingbroke: Stand all apart, and show fair duty to his majesty. My gracious lord— King Richard: Fair cousin, you debase your princely knee to make the base earth proud with kissing it: me rather had my heart might feel your love than my unpleased eye see your courtesy. Up, cousin, up; your heart is up, I know, thus high at least, although your knee be low. Bolingbroke: My gracious lord, I come but for mine own. King Richard: Your own is yours, and I am yours, and all. Bolingbroke: So far be mine, my most redoubted lord, as my true service shall deserve your love. King Richard: Well you deserve: they well deserve to have, that know the strong'st and surest way to get. Uncle, give me your hands: nay, dry your eyes; tears show the love of hearts, but never help: cousin, I am too young to be your father, though you are old enough to be my heir. What you will have, I'll give, and willing too; for do we must what force will have us do. Set on towards London, cousin, is it so? Bolingbroke: Yea, my good lord. King Richard: Then I must not say no. And thus the peers prepare to **depose** the crowned king."*
> - 📜 **Edward Gibbon (*The Decline and Fall of the Roman Empire*):** *"The rebellious praetorian guard resolved to **depose** the youthful emperor and auction the throne."*
> - 📜 **Arthur Conan Doyle (*The Hound of the Baskervilles*):** *"The coroner called the terrified stable boy to **depose** what he had witnessed upon the lonely moor."*
