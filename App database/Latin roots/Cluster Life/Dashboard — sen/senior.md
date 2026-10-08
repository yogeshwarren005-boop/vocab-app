---
latin_root: "[[Dashboard — sen]]"
cluster: "[[Cluster Life]]"
status: unread
---

# senior

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
> 1. **Primary Definition (Lexical / Standard Consensus)**: Older in age or higher in standing, rank, or authority within an organization or hierarchy.
> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: A student in the final year of study at a high school, college, or university.

> [!quote] 💬 Contextual Usage & Authentic Quotations
> - 📜 **William Shakespeare (*The Tempest*):** *"Obey, and be attentive. Canst thou remember / A time before we came unto this cell? / I do not think thou canst, for then thou wast not / Out three years old. / Certainly, sir, I can. / By what? by any other house or person? / Of anything the image tell me that / Hath kept with thy remembrance. / 'Tis far off / And rather like a dream than an assurance / That my remembrance warrants. Had I not / Four or five women once that tended me? / Thou hadst, and more, Miranda. But how is it / That this lives in thy mind? What seest thou else / In the dark backward and abysm of time? / If thou rememberest aught ere thou camest here, / How thou camest here thou mayst. / But that I do not. / Twelve year since, Miranda, twelve year since, / Thy father was the Duke of Milan and / A prince of power. / Sir, are not you my father? / Thy mother was a piece of virtue, and / She said thou wast my daughter; and thy father / Was Duke of Milan; and his only heir / And princess no worse issued. / O the heavens! / What foul play had we, that we came from thence? / Or blessed was't we did? / Both, both, my girl: / By foul play, as thou say'st, were we heaved thence, / But blessedly holp hither. / O, my heart bleeds / To think o' the teen that I have turned you to, / Which is from my remembrance! Please you, further. / My brother and thy uncle, called Antonio— / I pray thee, mark me—that a brother should / Be so perfidious!—he whom next thyself / Of all the world I loved and to him put / The manage of my state; as at that time / Through all the signories it was the first / And Prospero the prime duke, being so reputed / In dignity, and for the liberal arts / Without a parallel; those being all my study, / The government I cast upon my brother / And to my state grew stranger, being transported / And rapt in secret studies. Thy false uncle— / Dost thou attend me? / Sir, most heedfully. / Being once perfected how to grant suits, / How to deny them, who to advance and who / To trash for over-topping, new created / The creatures that were mine, I say, or changed 'em, / Or else new formed 'em; having both the key / Of officer and office, set all hearts i' the state / To what tune pleased his ear; that now he was / The ivy which had hid my princely trunk, / And sucked my verdure out on't. Thou attend'st not. / O, good sir, I do. / I pray thee, mark me. / I, thus neglecting worldly ends, all dedicated / To closeness and the bettering of my mind / With that which, but by being so retired, / O'er-prized all popular rate, in my false brother / Awaked an evil nature; and my trust, / Like a good parent, did beget of him / A falsehood in its contrary as great / As my trust was; which had indeed no limit, / A confidence sans bound. He being thus lorded, / Not only with what my revenue yielded, / But what my power might else exact, like one / Who having into truth, by telling of it, / Made such a sinner of his memory, / To credit his own lie, he did believe / He was indeed the duke; out o' the substitution, / And executing the outward face of royalty, / With all prerogative: hence his ambition growing— / Dost thou hear? / Your tale, sir, would cure deafness. / To have no screen between this part he played / And him he played it for, he needs will be / Absolute Milan. Me, poor man, my library / Was dukedom large enough: of temporal royalties / He thinks me now incapable; confederates— / So dry he was for sway—wi' the King of Naples / To give him annual tribute, do him homage, / Subject his coronet to his crown and bend / The dukedom yet unbowed—alas, poor Milan!— / To most ignoble stooping. The **senior** lord yielded his precedence to the duke."*
> - 📜 **John Milton (*Paradise Lost*):** *"The **senior** angels stood arrayed in shining ranks around the throne of the Almighty."*
> - 📜 **Edward Gibbon (*The History of the Decline and Fall of the Roman Empire*):** *"The **senior** partner in the imperial purple retained supreme command over the Illyrian legions."*
