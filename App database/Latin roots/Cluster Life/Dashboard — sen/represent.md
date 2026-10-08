---
latin_root: "[[Dashboard — sen]]"
cluster: "[[Cluster Life]]"
status: unread
---

# represent

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
> 1. **Primary Definition (Lexical / Standard Consensus)**: To act or speak on behalf of someone; to stand as an authorized proxy or delegate.
> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: To depict, portray, or symbolize an object, character, or concept through art or language.

> [!quote] 💬 Contextual Usage & Authentic Quotations
> - 📜 **John Locke (*Second Treatise of Government*):** *"Legislators are chosen to **represent** the collective interests and protect the natural rights of all citizens."*
> - 📜 **William Shakespeare (*Henry V*):** *"O for a Muse of fire, that would ascend / The brightest heaven of invention, / A kingdom for a stage, princes to act / And monarchs to behold the swelling scene! / Then should the warlike Harry, like himself, / Assume the port of Mars; and at his heels, / Leashed in like hounds, should famine, sword and fire / Crouch for employment. But pardon, gentles all, / The flat unraised spirits that have dared / On this unworthy scaffold to bring forth / So great an object: can this cockpit hold / The vasty fields of France? or may we cram / Within this wooden O the very casques / That did affright the air at Agincourt? / O, pardon! since a crooked figure may / Attest in little place a million; / And let us, ciphers to this great accompt, / On your imaginary forces work. / Suppose within the girdle of these walls / Are now confined two mighty monarchies, / Whose high upreared and abutting fronts / The perilous narrow ocean parts asunder: / Piece out our imperfections with your thoughts; / Into a thousand parts divide on man, / And make imaginary puissance; / Think when we talk of horses, that you see them / Printing their proud hoofs i' the receiving earth; / For 'tis your thoughts that now must deck our kings, / Carry them here and there; jumping o'er times, / Turning the accomplishment of many years / Into an hour-glass: for the which supply, / Admit me Chorus to this history; / Who prologue-like your humble patience pray, / Gently to hear, kindly to judge, our play. Let our actors **represent** the mighty contest of kingdoms."*
> - 📜 **Edmund Burke (*Speech to the Electors of Bristol*):** *"Your representative owes you not his industry only, but his judgment; and he betrays instead of serving you if he flatters you to **represent** your momentary passions."*
