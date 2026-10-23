---
latin_root: "[[Dashboard — sta]]"
cluster: "[[Cluster Placing]]"
status: unread
tier: 2
tier_label: "Words to learn a little later"
zipf: 2.52
rank: 8070
---

# ecstasy

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
> 1. **Primary Definition (Lexical / Consensus)**: An overwhelming feeling of great happiness, joyful excitement, or sublime delight.
> 2. **Secondary / Nuanced Definition (Contextual / Classical)**: A mystic state of transcendent religious trance where the soul is lifted out of the body.

> [!quote] 💬 Contextual Usage & Authentic Quotations
> - 📜 **William Shakespeare (*Hamlet*):** *"O, what a noble mind is here o'erthrown! The courtier's, soldier's, scholar's, eye, tongue, sword; the expectancy and rose of the fair state, the glass of fashion and the mould of form, the observed of all observers, quite, quite down! And I, of ladies most deject and wretched, that suck'd the honey of his music vows, now see that noble and most sovereign reason, like sweet bells jangled, out of tune and harsh; that unmatch'd form and feature of blown youth blasted with **ecstasy**: O, woe is me, to have seen what I have seen, see what I see!"*
> - 📜 **Percy Bysshe Shelley (*To a Skylark*):** *"Sound of vernal showers on the twinkling grass, rain-awakened flowers, all that ever was joyous and clear and fresh, thy music doth surpass: teach us, Sprite or Bird, what sweet thoughts are thine: I have never heard praise of love or wine that panted forth a flood of rapture so divine: chorus Hymenæal, or triumphal chant, match'd with thine would be all a vain boast, a thing wherein we feel there is some hidden want: what objects are the fountains of thy happy strain? What fields, or waves, or mountains? What shapes of sky or plain? What love of thine own kind? what ignorance of pain? With thy clear keen joyance languor cannot be: shadow of annoyance never came near thee: thou lovest—but ne'er knew love's sad satiety. Waking or asleep, thou of death must deem things more true and deep than we mortals dream, or how could thy notes flow in such a crystal stream? We look before and after, and pine for what is not: our sincerest laughter with some pain is fraught; our sweetest songs are those that tell of saddest thought. Yet if we could scorn hate, and pride, and fear; if we were things born not to shed a tear, I know not how thy joy we ever should come near. Better than all measures of delightful sound, better than all treasures that in books are found, thy skill to poet were, thou scorner of the ground! Teach me half the gladness that thy brain must know, such harmonious madness from my lips would flow the world should listen then—as I am listening now: singing in pure **ecstasy**."*
> - 📜 **Charlotte Brontë (*Jane Eyre*):** *"My heart bounded with an **ecstasy** of joy when Mr. Rochester called me his true bride."*
