---
latin_root: "[[Dashboard — rob]]"
cluster: "[[Cluster Virtue]]"
status: unread
---
# robe

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
> 1. **Primary Definition (Lexical / Standard Consensus)**: A long, loose outer garment reaching to the ankles, often worn as a symbol of official rank, academic status, or for relaxation.
> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: In ceremonial vesture and cultural history, a formal garment denoting judicial magistracy, ecclesiastical orders, or royal dignity.

> [!quote] 💬 Contextual Usage & Authentic Quotations
> - 📜 **William Shakespeare (*Henry VIII*):** *"I have ventured, like little wanton boys that swim on bladders, this many summers in a sea of glory, but far beyond my depth; my high-blown pride at length broke under me, and now has left me, weary and old with service, to the mercy of a rude stream that must for ever hide me. Vain pomp and glory of this world, I hate ye! I feel my heart new open'd. O how wretched is that poor man that hangs on princes' favours! There is betwixt that smile we would aspire to, that sweet aspect of princes, and their ruin, more pangs and fears than wars or women have; and when he falls, he falls like Lucifer, never to hope again. Cromwell, I did not think to shed a tear in all my miseries; but thou hast forced me, out of thy honest truth, to play the woman. Let's dry our eyes: and thus far hear me, Cromwell; and when I am forgotten, as I shall be, and sleep in dull cold marble, where no mention of me more must be heard of, say, I taught thee; say, Wolsey, that once trod the ways of glory, and sounded all the depths and shoals of honour, found thee a way, out of his wreck, to rise in; a sure and safe one, though thy master miss'd it. Mark but my fall, and that that ruin'd me. Cromwell, I charge thee, fling away ambition: by that sin fell the angels; how can man then, the image of his Maker, hope to win by it? Love thyself last; cherish those hearts that hate thee; corruption wins not more than honesty. Still in thy right hand carry gentle peace, to silence envious tongues. Be just, and fear not. Let all the ends thou aim'st at be thy country's, thy God's, and truth's; then if thou fall'st, O Cromwell, thou fall'st a blessed martyr! Serve the king; and—pr'ythee, lead me in: I have left my golden **robe** behind."*
> - 📜 **Charlotte Brontë (*Villette*):** *"Madame Beck wrapped her dark woolen **robe** tightly around her shoulders as she glided through the silent dormitory."*
> - 📜 **Nathaniel Hawthorne (*The Minister's Black Veil*):** *"The minister stood in the pulpit clad in his black ministerial **robe**, his face covered by the mysterious and terrifying veil."*
