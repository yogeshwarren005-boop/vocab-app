---
latin_root: "[[Dashboard — ver]]"
cluster: "[[Cluster Truth, Deception & Error]]"
status: unread
---
# very

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
> 1. **Primary Definition (Lexical / Standard Consensus)**: In a high degree; exceedingly, extremely (used as an intensive before adjectives and adverbs).
> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: Actual, precise, or identical; emphasizing identity (as in 'at that very moment').

> [!quote] 💬 Contextual Usage & Authentic Quotations
> - 📜 **William Shakespeare (*Hamlet*):** *"The **very** head and front of my offending hath this extent, no more."*
> - 📜 **John Milton (*Paradise Lost*):** *"Which way I fly is Hell; myself am Hell; And in the lowest deep a lower deep Still threatening to devour me opens wide, To which the Hell I suffer seems a Heaven. O then at last relent: is there no place Left for repentance, none for pardon left? None left but by submission; and that word Disdain forbids me, and my dread of shame Among the Spirits beneath, whom I seduced With other promises and other vaunts Than to submit, boasting I could subdue The Omnipotent. Ay me, they little know How dearly I abide that boast so vain, Under what torments I inwardly groan, While they adore me on the throne of Hell. With diadem and sceptre high advanced, The lower still I fall, only supreme In misery: such joy ambition finds. But say I could repent, and could obtain By act of grace my former state; how soon Would height recall high thoughts, how soon unsay What feigned submission swore! Ease would recant Vows made in pain, as violent and void. For never can true reconcilement grow Where wounds of deadly hate have pierced so deep: Which would but lead me to a worse relapse And heavier fall: so should I purchase dear Short intermission bought with double smart. This knows my Punisher; therefore as far From granting he, as I from begging peace: All hope excluded thus, behold in stead Of us out-cast, exiled, his new delight, Mankind created, and for him this World. So farewell hope, and with hope farewell fear, Farewell remorse: all good to me is lost; Evil, be thou my Good; by thee at least Divided empire with Heaven’s King I hold, By thee, and more than half perhaps will reign; As Man ere long, and this new World, shall know. Thus while he spake, each passion dimmed his face, Thrice changed with pale, ire, envy, and despair; Which marred his borrowed visage, and betrayed Him counterfeit, if any eye beheld: For heavenly minds from such distempers foul Are ever clear. Whereat he shrieked aloud, and shook the **very** foundations of Hell."*
> - 📜 **Charles Darwin (*The Origin of Species*):** *"The **very** essence of natural selection is that it leads to divergence of character and progressive extinction of less-improved forms."*
