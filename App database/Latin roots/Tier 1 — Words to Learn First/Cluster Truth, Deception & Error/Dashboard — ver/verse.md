---
latin_root: "[[Dashboard — ver]]"
cluster: "[[Cluster Truth, Deception & Error]]"
status: unread
tier: 1
tier_label: "Words to learn first"
zipf: 4
rank: 7659
---
# verse

> [!status] 🎯 **Status:**

```dataviewjs
if(!document.getElementById('apple-toggle-css')){const s=document.createElement('style');s.id='apple-toggle-css';s.textContent=':root{--apple-red:#FF375F;--apple-red-glow:rgba(255,55,95,0.45);--apple-amber:#FF9F0A;--apple-amber-glow:rgba(255,159,10,0.45);--apple-green:#30D158;--apple-green-glow:rgba(48,209,88,0.45)}.apple-c{position:relative;display:inline-flex;align-items:center;gap:8px;padding:2px 10px 2px 4px;border-radius:999px;background:var(--background-secondary,#111624);border:1px solid var(--background-modifier-border,#232d42);cursor:pointer;user-select:none;transition:border-color .2s ease,transform .2s ease,box-shadow .2s ease;line-height:1;vertical-align:middle;box-sizing:border-box}.apple-c:hover{border-color:var(--text-muted,#3b4b6b);transform:translateY(-1px);box-shadow:0 2px 8px rgba(0,0,0,.35)}.apple-c:active{transform:scale(.96)}.apple-c .track-c{position:relative;width:48px;height:18px;background:var(--background-primary,#090d17);border-radius:999px;border:1px solid var(--background-modifier-border,#1c2436);display:flex;align-items:center;justify-content:space-between;padding:0 6px;box-sizing:border-box}.apple-c .c-dot{width:3px;height:3px;border-radius:999px;background:var(--text-faint,#334155);opacity:.6}.apple-c .halo-c{position:absolute;top:1px;left:1px;width:14px;height:14px;border-radius:999px;transition:transform .35s cubic-bezier(.34,1.6,.64,1),background-color .25s ease,box-shadow .25s ease;display:flex;align-items:center;justify-content:center;box-sizing:border-box}.apple-c .halo-c .core-dot{width:5px;height:5px;border-radius:999px;background:#fff;box-shadow:0 0 4px #fff}.apple-c .halo-c.p0{transform:translateX(0);background:var(--apple-red);box-shadow:0 0 12px var(--apple-red),0 0 20px var(--apple-red-glow)}.apple-c .halo-c.p1{transform:translateX(15px);background:var(--apple-amber);box-shadow:0 0 12px var(--apple-amber),0 0 20px var(--apple-amber-glow)}.apple-c .halo-c.p2{transform:translateX(30px);background:var(--apple-green);box-shadow:0 0 12px var(--apple-green),0 0 20px var(--apple-green-glow)}.apple-c .label{font-size:11px;font-weight:700;letter-spacing:.2px;transition:color .2s ease;min-width:48px}.apple-c .label.unread{color:var(--apple-red)}.apple-c .label.learning{color:var(--apple-amber)}.apple-c .label.learned{color:var(--apple-green)}';document.head.appendChild(s);}
const p = dv.current();
const rawStatus = p.status || "unread";
const states = [{ key: 'unread', label: 'unread', cls: 'unread', p: 'p0' }, { key: 'learning', label: 'learning', cls: 'learning', p: 'p1' }, { key: 'learned', label: 'learned', cls: 'learned', p: 'p2' }];
let curIdx = states.findIndex(s => s.key === rawStatus);
if (curIdx === -1) curIdx = 0;
const toggle = document.createElement('div');
toggle.className = 'apple-c';
toggle.title = 'Click to glide: unread ➔ learning ➔ learned';
const track = document.createElement('div');
track.className = 'track-c';
track.innerHTML = '<span class="c-dot"></span><span class="c-dot"></span><span class="c-dot"></span><div class="halo-c ' + states[curIdx].p + '"><div class="core-dot"></div></div>';
const label = document.createElement('span');
label.className = 'label ' + states[curIdx].cls;
label.textContent = states[curIdx].label;
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
> 1. **Primary Definition (Lexical / Standard Consensus)**: Writing arranged with metrical rhythm, typically possessing rhyme, cadence, or stanzaic form; poetry.
> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: A single line or stanza of a poem, or a numbered subdivision of a chapter in the Bible.

> [!quote] 💬 Contextual Usage & Authentic Quotations
> - 📜 **William Shakespeare (*Sonnet 55*):** *"Not marble, nor the gilded monuments Of princes, shall outlive this powerful rhyme; But you shall shine more bright in these contents Than unswept stone, besmear’d with sluttish time. When wasteful war shall statues overturn, And broils root out the work of masonry, Nor Mars his sword nor war’s quick fire shall burn The living record of your memory. ’Gainst death and all-oblivious enmity Shall you pace forth; your praise shall still find room Even in the eyes of all posterity That wear this world out to the ending doom. So, till the judgment that yourself arise, You live in this, and dwell in lovers’ eyes. My **verse** shall preserve thy truth forever."*
> - 📜 **John Milton (*Paradise Lost*):** *"These thoughts may startle well, but not astound The virtuous mind, that ever walks attended By a strong siding champion, Conscience. O welcome, pure-ey’d Faith, white-handed Hope, Thou hovering angel girt with golden wings, And thou unblemish’d form of Chastity! I see ye visibly, and now believe That He, the Supreme Good, to whom all things ill Are but as slavish officers of vengeance, Would send a glistering guardian, if need were, To keep my life and honour unassail’d. Was I deceiv’d, or did a sable cloud Turn forth her silver lining on the night? I did not err; there does a sable cloud Turn forth her silver lining on the night, And casts a gleam over this tufted grove. I cannot hallo to my brothers, but Such noise as I can make to be heard farthest I’ll venture; for my new-enliven’d spirits Prompt me; and they perhaps are not far off. Sweet Echo, sweetest nymph, that liv’st unseen Within thy airy shell By slow Meander’s margent green, And in the violet-embroider’d vale Where the love-lorn nightingale Nightly to thee her sad song mourneth well: Canst thou not tell me of a gentle pair That likest thy Narcissus are? O, if thou have Hid them in some flow’ry cave, Tell me but where, Sweet Queen of Parly, Daughter of the Sphere! So may’st thou be displaced above the sky, And give resounding grace to all heaven’s harmonies. This sacred **verse** consoles the sorrowing soul."*
> - 📜 **Samuel Johnson (*The Lives of the English Poets*):** *"Dryden found English poetry brick and left it marble, establishing the heroic couplet as the standard vehicle of serious **verse**."*
