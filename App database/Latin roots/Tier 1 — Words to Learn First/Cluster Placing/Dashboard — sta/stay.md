---
latin_root: "[[Dashboard — sta]]"
cluster: "[[Cluster Placing]]"
status: unread
tier: 1
tier_label: "Words to learn first"
zipf: 4.27
rank: 1001
---

# stay

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
> 1. **Primary Definition (Lexical / Consensus)**: To remain in a specified place, condition, or company without departure.
> 2. **Secondary / Nuanced Definition (Contextual / Classical)**: To suspend, stop, or postpone an action, judicial execution, or proceeding.

> [!quote] 💬 Contextual Usage & Authentic Quotations
> - 📜 **William Shakespeare (*The Merchant of Venice*):** *"Tarry a little; there is something else. This bond doth give thee here no jot of blood; the words expressly are 'a pound of flesh': take then thy bond, take thou thy pound of flesh; but, in the cutting it, if thou dost shed one drop of Christian blood, thy lands and goods are, by the laws of Venice, confiscate unto the state of Venice. Therefore prepare thee to cut off the flesh. Shed thou no blood, nor cut thou less nor more but just a pound of flesh: if thou cut'st more or less than a just pound, be it but so much as makes it light or heavy in the substance, or the division of the twentieth part of one poor scruple, nay, if the scale do turn but in the estimation of a hair, thou diest and all thy goods are confiscate. Why doth the Jew pause? take thy forfeiture. Give me my principal, and let me go. I have it ready for thee; here it is. He hath refused it in the open court: he shall have merely justice and his bond. A diamond gone, cost me two thousand ducats in Frankfort! The curse never fell upon our nation till now; I never felt it till now: two thousand ducats in that; and other precious, precious jewels. I would my daughter were dead at my foot, and the jewels in her ear! would she were hearsed at my foot, and the ducats in her coffin! No news of them? Why, so: and I know not what's spent in the search: why, thou loss upon loss! the thief gone with so much, and so much to find the thief; and no satisfaction, no revenge: nor no ill luck stirring but what lights on my shoulders; no sighs but o' my breathing; no tears but o' my shedding. Yes, other men have ill luck too: Antonio, as I heard in Genoa—What, what, what? ill luck, ill luck? Hath an argosy cast away, coming from Tripolis. I thank God, I thank God. Is't true, is't true? I spoke with some of the sailors that escaped the wreck. I thank thee, good Tubal: good news, good news! ha, ha! where? in Genoa? Your daughter spent in Genoa, as I heard, in one night fourscore ducats. Thou stick'st a dagger in me: I shall never see my gold again: fourscore ducats at a sitting! fourscore ducats! There came divers of Antonio's creditors in my company to Venice, that swear he cannot choose but break. I am very glad on't: I'll plague him; I'll torture him: I am glad on't. One of them showed me a ring that he had of your daughter for a monkey. Out upon her! Thou torturest me, Tubal: it was my turquoise; I had it of Leah when I was a bachelor: I would not have given it for a wilderness of monkeys. But Antonio is certainly undone. Nay, that's true, that's very true. Go, Tubal, fee me an officer; bespeak him a fortnight before. I will have the heart of him, if he forfeit; for, were he out of Venice, I can make what merchandise I will. Go, go, Tubal, and meet me at our synagogue; go, good Tubal; at our synagogue, Tubal. **Stay**, I say; hear me yet a word."*
> - 📜 **John Milton (*Paradise Lost*):** *"Here will I **stay**, contented with this humble bower, while empires fall in ruins round the world."*
> - 📜 **Lord Byron (*She Walks in Beauty*):** *"One shade the more, one ray the less, had half impair'd the nameless grace which waves in every raven tress, or softly lightens o'er her face; where thoughts serenely sweet express how pure, how dear their dwelling-place; and could not **stay** the fleeting joy."*
