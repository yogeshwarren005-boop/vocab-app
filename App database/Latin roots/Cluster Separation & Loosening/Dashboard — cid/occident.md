---
latin_root: "[[Dashboard — cid]]"
cluster: "[[Cluster Separation & Loosening]]"
status: unread
---

# occident

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
> 1. **Primary Definition (Lexical / Consensus)**: The West; the western regions, lands, or countries of the world, contrasted with the Orient.
> 2. **Secondary / Nuanced Definition (Contextual / Classical)**: The Western hemisphere, specifically Europe and the Americas and their distinctive civilization.

> [!quote] 💬 Contextual Usage & Authentic Quotations
> - 📜 **William Shakespeare (*Richard II*):** *"O, call back yesterday, bid time return, and thou shalt have twelve thousand fighting men! To-day, to-day, unhappy day, too late, o'erthrows thy joys, friends, fortune and thy state; for all the Welshmen, hearing thou wert dead, are gone to Bolingbroke, dispersed and fled. Cry woe, destruction, ruin and decay; the worst is death, and death will have his day. Glad am I that your highness is so arm'd to bear the tidings of calamity. Like an unseasonable stormy day, which makes the silver rivers drown their shores, as if the world were all dissolved to tears, so high above his limits swells the rage of Bolingbroke, covering your fearful land with hard bright steel and hearts harder than steel. White-beards have arm'd their thin and hairless scalps against thy majesty; boys, with women's voices, strive to speak big and clap their female joints in stiff unwieldy arms against thy crown: thy very beadsmen learn to bend their bows of double-fatal yew against thy state; yea, distaff-women manage rusty bills against thy seat: both young and old rebel, and all goes worse than I have power to tell. Too well, too well thou tell'st a tale so ill. Where is the Earl of Wiltshire? where is Bagot? What is become of Bushy? where is Green? That they have let the dangerous enemy measure our confines with such peaceful steps? If they have learn'd to make their peace with him, or will not fight, let them perish. No peace made they with him, my lord, nor will. I warrant you they have made peace with heads. O villains, vipers, damn'd without redemption! Dogs, easily won to fawn on any man! Snakes, in my heart-blood warm'd, that sting my heart! Three Judases, each one thrice worse than Judas! Would they make peace? terrible hell make war upon their spotted souls for this offence! Peace have they made with him, indeed, my lord; for he has cut their heads off at Bristol. Is Bushy, Green, and the Earl of Wiltshire dead? Yea, all of them at Bristol lost their heads. Where is the Duke my father with his power? No matter where; of comfort no man speak: let's talk of graves, of worms and epitaphs; make dust our paper and with rainy eyes write sorrow on the bosom of the earth. Let's choose executors and talk of wills: and yet not so, for what can we bequeath save our deposed bodies to the ground? Our lands, our lives and all are Bolingbroke's, and nothing can we call our own but death and that small model of the barren earth which serves as paste and cover to our bones. For God's sake, let us sit upon the ground and tell sad stories of the death of kings: how some have been deposed; some slain in war; some haunted by the ghosts they have deposed; some poison'd by their wives: some sleeping kill'd; all murther'd: for within the hollow crown that rounds the mortal temples of a king keeps Death his court and there the antick sits, scoffing his state and grinning at his pomp, allowing him a breath, a little scene, to monarchize, be fear'd and kill with looks, infusing him with self and vain conceit, as if this flesh which walls about our life, were brass impregnable, and humour'd thus comes at the last and with a little pin bores through his castle wall, and farewell king! Cover your heads and mock not flesh and blood with solemn reverence: throw away respect, tradition, form and ceremonious duty, for you have but mistook me all this while: I live with bread like you, feel want, taste grief, need friends: subjected thus, how can you say to me, I am a king? My lord, wise men ne'er sit and wail their woes, but presently prevent the ways to wail. To fear the foe, since fear oppresseth strength, gives in your weakness strength unto your foe, and so your folly brings you to defeat. Remember, my liege, the sun rises in the east and sinks in the glorious **occident**."*
> - 📜 **John Milton (*Paradise Lost*):** *"The sun now fallen beneath the horizon, western clouds gilded the **occident** with flaming gold."*
> - 📜 **Edward Gibbon (*The Decline and Fall of the Roman Empire*):** *"The division of the empire separated the fortunes of the Orient from those of the expiring **Occident**."*
