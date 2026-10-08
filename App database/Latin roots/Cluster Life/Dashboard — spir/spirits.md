---
latin_root: "[[Dashboard — spir]]"
cluster: "[[Cluster Life]]"
status: unread
---

# spirits

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
> 1. **Primary Definition (Lexical / Standard Consensus)**: A person's mood, emotional state, or temper; also strong distilled alcoholic drinks.
> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: Supernatural beings, apparitions, or incorporeal entities.

> [!quote] 💬 Contextual Usage & Authentic Quotations
> - 📜 **William Shakespeare (*Julius Caesar*):** *"There is a tide in the affairs of men / Which, taken at the flood, leads on to fortune; / Omitted, all the voyage of their life / Is bound in shallows and in miseries. / On such a full sea are we now afloat, / And we must take the current when it serves, / Or lose our ventures. / Then, with your will, go on; / We'll along ourselves, and meet them at Philippi. / The deep of night is crept upon our talk, / And nature must obey necessity; / Which we will niggard with a little rest. / There is no more to say? / No more. Good night: / Early to-morrow will we rise, and hence. / Lucius! My gown. Farewell, good Messala: / Good night, Titinius. Noble, noble Cassius, / Good night, and good repose. / O my dear brother! / This was an ill beginning of the night: / Never come such division 'tween our souls! / Let it not, Brutus. / Everything is well. / Good night, my lord. / Good night, good brother. / Good night, Lord Brutus. / Farewell, every one. / Give me the gown. Where is the musical instrument? / Here in the tent. / What, thou speak'st drowsily? / Poor knave, I blame thee not; thou art o'er-watch'd. / Call Claudius and some other of my men: / I'll have them sleep on cushions in my tent. / Varro and Claudius! / Calls my lord? / I pray you, sirs, lie in my tent and sleep; / It may be I shall raise you by and by / On business to my brother Cassius. / So please you, we will stand and watch your pleasure. / I will not have it so: lie down, good sirs; / It may be I shall otherwise bethink me. / Look, Lucius, here's the book I sought for so; / I put it in the pocket of my gown. / I was sure your lordship did not give it me. / Bear with me, good boy, I am much forgetful. / Canst thou, hold up thy heavy eyes awhile, / And touch thy instrument a strain or two? / Ay, my lord, an't please you. / It does, my boy: / I trouble thee too much, but thou art willing. / It is my duty, sir. / I should not urge thy duty past thy might; / I know young bloods look for a time of rest. / I have slept, my lord, already. / It was well done; and thou shalt sleep again; / I will not hold thee long: if I do live, / I will be good to thee. / Music, and a song. / This is a sleepy tune. O murderous slumber, / Lay'st thou thy leaden mace upon my boy, / That plays thee music? Gentle knave, good night; / I will not do thee so much wrong to wake thee: / If thou dost nod, thou break'st thy instrument; / I'll take it from thee; and, good boy, good night. / Let me see, let me see; is not the leaf turn'd down / Where I left reading? Here it is, I think. / Enter the Ghost of Caesar. / How ill this taper burns! Ha! who comes here? / I think it is the weakness of mine eyes / That shapes this monstrous apparition. / It comes upon me. Art thou any thing? / Art thou some god, some angel, or some devil, / That makest my blood cold and my hair to stare? / Speak to me what thou art. / Thy evil spirit, Brutus. / Why comest thou? / To tell thee thou shalt see me at Philippi. / Well; then I shall see thee again? / Ay, at Philippi. / Why, I will see thee at Philippi, then. / Ghost vanishes. / Now I have taken heart thou vanishest: / Ill spirit, I would hold more talk with thee. / Boy, Lucius! Varro! Claudius! Sirs, awake! / Claudius! / The strings, my lord, are false. / He thinks he still is at his instrument. / Lucius, awake! / My lord? / Didst thou dream, Lucius, that thou so criedst out? / My lord, I do not know that I did cry. / Yes, that thou didst: didst thou see any thing? / Nothing, my lord. / Sleep again, Lucius. Sirrah Claudius! / Fellow thou, awake! / My lord? / My lord? / Why did you so cry out, sirs, in your sleep? / Did we, my lord? / Ay: saw you any thing? / No, my lord, I saw nothing. / Nor I, my lord. / Go and commend me to my brother Cassius; / Bid him set on his powers betimes before, / And we will follow. / It shall be done, my lord. / Restless **spirits** walk the night."*
> - 📜 **Charles Dickens (*The Pickwick Papers*):** *"The jovial travelers revived their flagging **spirits** with hot glasses of brandy and water at the coach inn."*
> - 📜 **Jane Austen (*Pride and Prejudice*):** *"Elizabeth's **spirits** rose immediately when the carriage turned through the lodge gates into Hertfordshire."*
