---
latin_root: "[[Dashboard — spir]]"
cluster: "[[Cluster Life]]"
status: unread
---

# conspirator

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
> 1. **Primary Definition (Lexical / Standard Consensus)**: A person who takes part in a secret plot, treachery, or conspiracy.
> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: An accomplice participating in an organized design against government or law.

> [!quote] 💬 Contextual Usage & Authentic Quotations
> - 📜 **William Shakespeare (*Julius Caesar*):** *"There is no terror, Cassius, in your threats, / For I am arm'd so strong in honesty / That they pass by me as the idle wind, / Which I respect not. I did send to you / For certain sums of gold, which you denied me: / For I can raise no money by vile means: / By heaven, I had rather coin my heart, / And drop my blood for drachmas, than to wring / From the hard hands of peasants their vile trash / By any indirection: I did send / To you for gold to pay my legions, / Which you denied me: was that done like Cassius? / Should I have answer'd Caius Cassius so? / When Marcus Brutus grows so covetous, / To lock such rascal counters from his friends, / Be ready, gods, with all your thunderbolts; / Dash him to pieces! / I denied you not. / You did. / I did not: he was but a fool that brought / My answer back. Brutus hath rived my heart: / A friend should bear his friend's infirmities, / But Brutus makes mine greater than they are. / I do not, till you practise them on me. / You love me not. / I do not like your faults. / A friendly eye could never see such faults. / A flatterer's would not, though they do appear / As huge as high Olympus. / Come, Antony, and young Octavius, come, / Revenge yourselves alone on Cassius, / For Cassius is aweary of the world; / Hated by one he loves; braved by his brother; / Check'd like a bondman; all his faults observed, / Set in a note-book, learn'd, and conn'd by rote, / To cast into my teeth. O, I could weep / My spirit from mine eyes! There is my dagger, / And here my naked breast; within, a heart / Dearer than Plutus' mine, richer than gold: / If that thou be'st a Roman, take it forth; / I, that denied thee gold, will give my heart: / Strike, as thou didst at Caesar; for, I know, / When thou didst hate him worst, thou lovedst him better / Than ever thou lovedst Cassius. / Sheathe your dagger: / Be angry when you will, it shall have scope; / Do what you will, dishonour shall be humour. / O Cassius, you are yoked with a lamb / That carries anger as the flint bears fire; / Who, much enforced, shows a hasty spark, / And straight is cold again. / Hath Cassius lived / To be but mirth and laughter to his Brutus, / When grief, and blood ill-temper'd, vexeth him? / When I spoke that, I was ill-temper'd too. / Do you confess so much? Give me your hand. / And my heart too. / O Brutus! / What's the matter? / Have not you love enough to bear with me, / When that rash humour which my mother gave me / Makes me forgetful? / Yes, Cassius; and, from henceforth, / When you are over-earnest with your Brutus, / He'll think your mother chides, and leave you so. / Stand firm, fellow **conspirator**."*
> - 📜 **Charles Dickens (*A Tale of Two Cities*):** *"Defarge was a determined **conspirator**, directing the subterranean fury of the Saint Antoine quarter."*
> - 📜 **Sir Walter Scott (*Ivanhoe*):** *"The masked **conspirator** held his breath as the royal herald rode past the gateway."*
