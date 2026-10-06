---
latin_root: "[[Dashboard — spec]]"
cluster: "[[Cluster Sight]]"
status: unread
---
# spectacle

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
> 1. **Primary Definition (Lexical / Standard Consensus)**: A visually striking performance or display; an impressive or unusual sight.
> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: In cultural theory and political drama, designates an engineered public extravaganza designed to mesmerize the populace and project imperial majesty.

> [!quote] 💬 Contextual Usage & Authentic Quotations
> - 📜 **William Shakespeare (*King Lear*):** *"O, matter and impertinency mix'd! / Reason in madness! / ... / A sight most pitiful in the meanest wretch, / Past speaking of in a king! / Thou hast one daughter / Who redeems nature from the general curse / Which twain have brought her to. / ... / O ruined piece of nature! This great world / Shall so wear out to naught. Dost thou know me? / I remember thine eyes well enough. Dost thou squiny at me? / No, do thy worst, blind Cupid; I'll not love. / Read thou this challenge; mark but the penning on't. / Were all thy letters suns, I could not see. / I would not take this from report; it is, / And my heart breaks at it. / Read. / What! with the case of eyes? / O! ho! are you there with me? No eyes in your head, nor no money in your purse? Your eyes are in a heavy case, your purse in a light: yet you see how this world goes. / I see it feelingly. / What! art mad? A man may see how this world goes with no eyes. Look with thine ears: see how yond justice rails upon yond simple thief. Hark, in thine ear: change places; and, handy-dandy, which is the justice, which is the thief? / ... / If thou wilt weep my fortunes, take my eyes. / I know thee well enough; thy name is Gloucester: / Thou must be patient; we came crying hither: / Thou know'st the first time that we smell the air / We wawl and cry. I will preach to thee: mark. / Alack, alack the day! / When we are born, we cry that we are come / To this great stage of fools. This is a good block: / It were a delicate stratagem to shoe / A troop of horse with felt; I'll put't in proof, / And when I have stol'n upon these sons-in-law, / Then, kill, kill, kill, kill, kill, kill! / What a mournful **spectacle** is here."*
> - 📜 **John Locke (*An Essay Concerning Human Understanding*):** *"The magnificent **spectacle** of the heavens demonstrates the wisdom and power of the divine Architect."*
> - 📜 **Thomas Hardy (*The Dynasts*):** *"The vast battle presented a terrible **spectacle** of smoke, screaming shells, and charging cavalry across the plain."*
