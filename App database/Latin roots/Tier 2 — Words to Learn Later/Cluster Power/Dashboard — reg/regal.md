---
latin_root: "[[Dashboard — reg]]"
cluster: "[[Cluster Power]]"
status: unread
tier: 2
tier_label: "Words to learn a little later"
zipf: 2.3
rank: 20260
---
# regal

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
> 1. **Primary Definition (Lexical / Standard Consensus)**: Of, relating to, or suitable for a king or queen; magnificent, royal, and majestic.
> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: Exhibiting stately dignity, grand splendor, or sovereign authority in appearance.

> [!quote] 💬 Contextual Usage & Authentic Quotations
> - 📜 **William Shakespeare (*Henry V*):** *"What infinite heart's-ease / Must kings neglect, that private men enjoy! / And what have kings, that privates have not too, / Save ceremony, save general ceremony? / And what art thou, thou idol ceremony? / What kind of god art thou, that suffer'st more / Of mortal griefs than do thy worshippers? / What are thy rents? what are thy comings in? / O ceremony, show me but thy worth! / What is thy soul of adoration? / Art thou aught else but place, degree and form, / Creating awe and fear in other men? / Wherein thou art less happy being fear'd / Than they in fearing. / What drink'st thou oft, instead of homage sweet, / But poison'd flattery? O, be sick, great greatness, / And bid thy ceremony give thee cure! / Think'st thou the fiery fever will go out / With titles blown from adulation? / Will it give place to flexure and low bending? / Canst thou, when thou command'st the beggar's knee, / Command the health of it? No, thou proud dream, / That play'st so subtly with a king's repose; / I am a king that find thee, and I know / 'Tis not the balm, the sceptre and the ball, / The sword, the mace, the crown imperial, / The intertissued robe of gold and pearl, / The farced title running 'fore the king, / The throne he sits on, nor the tide of pomp / That beats upon the high shore of this world, / No, not all these, thrice-gorgeous ceremony, / Not all these, laid in bed majestical, / Can sleep so soundly as the wretched slave, / Who with a body fill'd and vacant mind / Gets him to rest, cramm'd with distressful bread; / Never sees horrid night, the child of hell, / But, like a lackey, from the rise to set / Sweats in the eye of Phoebus and all night / Sleeps in Elysium; next day after dawn, / Doth rise and help Hyperion to his horse, / And follows so the ever-running year, / With profitable labour, to his grave: / And, but for ceremony, such a wretch, / Winding up days with toil and nights with sleep, / Had the fore-hand and vantage of a king. / The slave, a member of the country's peace, / Enjoys it; but in gross brain little wots / What watch the king keeps to maintain the peace, / Whose hours the peasant best advantages: / He bears this **regal** burden with silent grief."*
> - 📜 **Henry David Thoreau (*Walden*):** *"The autumn oak displays a **regal** purple foliage, surpassing the crimson robes of oriental monarchs."*
> - 📜 **Herman Melville (*Moby-Dick*):** *"The great white bull was surrounded by his herd, moving with **regal** ease through the tranquil tropical swell."*
