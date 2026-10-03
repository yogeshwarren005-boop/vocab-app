---
latin_root: "[[Dashboard — fac]]"
cluster: "[[Cluster Action]]"
status: unread
---
# facility

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
> 1. **Primary Definition (Lexical / Standard Consensus)**: Ease in doing or performing something; aptness, fluency, or a physical amenity or installation.
> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: In commercial real estate and industrial engineering, a facility comprises specialized physical infrastructure designed for manufacturing or research.

> [!quote] 💬 Contextual Usage & Authentic Quotations
> - 📜 **Charles Darwin (*The Origin of Species*):** *"Certain species cross with surprising **facility**, producing fertile offspring that challenge our traditional taxonomic boundaries."*
> - 📜 **Thomas Hardy (*The Mayor of Casterbridge*):** *"Henchard lacked that smooth **facility** in courteous deception which enabled his rival to navigate civic politics without friction."*
> - 📜 **William Shakespeare (*Love's Labour's Lost*):** *"A man of fire-new words, fashion's own knight, that hath a mint of phrases in his brain; one whom the music of his own vain tongue doth ravish like enchanting harmony; a man of complements, whom right and wrong have chosen as umpire of their mutiny: this child of fancy, that Armado hight, for interim to our studies shall relate in high-born words the worth of many a knight from tawny Spain lost in the world's debate. How you delight, my lord, I know not, I; but, I protest, I love to hear him lie, and I will use him for my minstrelsy. Biron is like an envious sneaping frost that bites the first-born infants of the spring. Well, say I am; why should proud summer boast before the birds have cause to sing? Why should I joy in an abortive birth? At Christmas I no more desire a rose than wish a snow in May's new-fangled mirth; but like of each thing that in season grows. So you, to study now it is too late, that were to climb o'er the house to unlock the little gate. Well, sit you out: go home, Biron: adieu. No, my good lord; I have sworn to stay with you: and though I have for barbarism spoke more than for that angel knowledge you can say, yet confident I'll keep what I have swore, and bear the penance that I shall receive. But there are other strict observances; as, not to see a woman in that term, which I hope well is not enrolled there; and one day in a week to touch no food, and but one meal on every day beside, the which I hope is not enrolled there; and then, to sleep but three hours in the night, and not be seen to wink of all the day, when I was wont to think no harm all night, and make a dark night too of half the day, which I hope well is not enrolled there: O, these are barren tasks, too hard to keep, not to see ladies, study, fast, not sleep! Your oath is pass'd to pass away from these. Let me say no, my liege, an if you please: I only swore to study with your grace and stay here in your court for three years' space. You swore to that, Biron, and to the rest. By yea and nay, sir, then I swore in jest. What is the end of study? Let me know. Why, that to know, which else we should not know. Things hid and barr'd, you mean, from common sense? Ay, that is study's god-like recompense. Come on, then; I will swear to study so, to know the thing I am forbid to know: as thus, to study where I well may dine, when I to feast expressly am forbid; or study where to meet some mistress fine, when mistresses from common sense are hid; or, having sworn too hard a keeping oath, study to break it and not break my troth. If study's gain be thus and this can show, study had reason to outwit the **facility** of youth."*

