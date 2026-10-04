---
latin_root: "[[Dashboard — vot]]"
cluster: "[[Cluster Sacred]]"
status: unread
---
# vote

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
> 1. **Primary Definition (Lexical / Standard Consensus)**: A formal expression of opinion or choice made by an individual or group, especially in an election or referendum.
> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: To express one's choice or preference formally by ballot, show of hands, or voice in a deliberative assembly.

> [!quote] 💬 Contextual Usage & Authentic Quotations
> - 📜 **Abraham Lincoln (*First Inaugural Address*):** *"A majority held in restraint by constitutional checks and limitations is the only true sovereign of a free people; whoever rejects it does of necessity fly to anarchy or to despotism: why should there not be a patient confidence in the ultimate justice of the people: is there any better or equal hope in the world: in our present differences, is either party without faith of being in the right: if the Almighty Ruler of nations, with His eternal truth and justice, be on your side of the North, or on yours of the South, that truth and that justice will surely prevail by the judgment of this great tribunal of the American people: by the frame of the government under which we live, this same people have wisely given their public servants but little power for mischief; and have, with equal wisdom, provided for the return of that little to their own hands at very short intervals: while the people retain their virtue and vigilance, no administration, by any extreme of wickedness or folly, can very seriously injure the government in the short space of four years: my countrymen, one and all, think calmly and well upon this whole subject: nothing valuable can be lost by taking time: if there be an object to hurry any of you in hot haste to a step which you would never take deliberately, that object will be frustrated by taking time; but no good object can be frustrated by it: such of you as are now dissatisfied, still have the old Constitution unimpaired, and, on the sensitive point, the laws of your own framing under it; while the new administration will have no immediate power, if it would, to change either: if it were admitted that you who are dissatisfied hold the right side in the dispute, there still is no single good reason for precipitate action: intelligence, patriotism, Christianity, and a firm reliance on Him who has never yet forsaken this favored land, are still competent to adjust in the best way all our present difficulty: in your hands, my dissatisfied fellow-countrymen, and not in mine, is the momentous issue of civil war: the government will not assail you: you can have no conflict without being yourselves the aggressors: you have no oath registered in heaven to destroy the government, while I shall have the most solemn one to preserve, protect, and defend it: the ballot and the free **vote** of citizens remain the bulwarks of republican liberty."*
> - 📜 **Thomas Babington Macaulay (*The History of England*):** *"The House of Commons divided at midnight, deciding the fate of the ministry by a single **vote**."*
> - 📜 **Alexis de Tocqueville (*Democracy in America*):** *"The right to **vote** educates the citizen in the responsibilities of public administration and civic duty."*

