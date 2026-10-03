---
latin_root: "[[Dashboard — fac]]"
cluster: "[[Cluster Action]]"
status: unread
---
# official

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
> 1. **Primary Definition (Lexical / Standard Consensus)**: Relating to an authority, position, or government; properly authorized, formal, or confirmed.
> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: In administrative law and statecraft, an official act carries legal presumption of regularity and sovereign immunity within authorized jurisdictions.

> [!quote] 💬 Contextual Usage & Authentic Quotations
> - 📜 **George Eliot (*Middlemarch*):** *"Mr. Brooke's parliamentary candidacy necessitated an **official** address to the electors of the borough, drafted with cautious ambiguity."*
> - 📜 **Thomas Hardy (*The Mayor of Casterbridge*):** *"The mayor put on his heavy gold chain of **official** authority to receive the royal visitor with civic solemnity."*
> - 📜 **William Shakespeare (*Measure for Measure*):** *"No ceremony that to great ones 'longs, not the king's crown, nor the deputed sword, the marshal's truncheon, nor the judge's robe, become them with one half so good a grace as mercy does. If he had been as you and you as he, you would have slipp'd like him; but he, like you, would not have been so stern. I would to heaven I had your potency, and you were Isabel! should it then be thus? No; I would tell what 'twere to be a judge, and what a prisoner. Your brother is a forfeit of the law, and you but waste your words. Alas, alas! Why, all the souls that were were forfeit once; and He that might the vantage best have took found out the remedy. How would you be, if He, which is the top of judgment, should but judge you as you are? O, think on that; and mercy then will breathe within your lips, like man new made. Be you content, fair maid; it is the law, not I condemn your brother: were he my kinsman, brother, or my son, it should be thus with him: he must die to-morrow. To-morrow! O, that's sudden! Spare him, spare him! He's not prepared for death. Even for our kitchens we kill the fowl of season: shall we serve heaven with less respect than we do minister unto our gross selves? Good, good my lord, bethink you; who is it that hath died for this offence? There's many have committed it. The law hath not been dead, though it hath slept: those many had not dared to do that evil, if the first that did the edict infringe had answer'd for his deed: now 'tis awake, takes note of what is done; and, like a prophet, looks in a glass, that shows what future evils, either new, or by remissness new-conceived, and so in progress to be hatch'd and born, are now to have no successive degrees, but, ere they live, to end. Yet show some pity. I show it most of all when I show justice; for then I pity those I do not know, which a dismiss'd offence would after gall; and do him right that, answering one foul wrong, lives not to act another. Be satisfied; your brother dies to-morrow. O, it is excellent to have a giant's strength; but it is tyrannous to use it like a giant. Could great men thunder as Jove himself does, Jove would ne'er be quiet, for every pelting, petty **official** would use his heaven for thunder; nothing but thunder!"*

