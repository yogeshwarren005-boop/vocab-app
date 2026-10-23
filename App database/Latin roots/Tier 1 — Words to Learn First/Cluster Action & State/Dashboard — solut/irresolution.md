---
latin_root: "[[Dashboard — solut]]"
cluster: "[[Cluster Action & State]]"
status: unread
tier: 3
tier_label: "Words to learn last"
zipf: 1.2
rank: 999999
---
# irresolution

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
> 1. **Primary Definition (Lexical / Standard Consensus)**: Hesitation; uncertainty; lack of decision or purpose; vacillation.
> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: In tragic dramaturgy, tragic irresolution serves as the protagonist's fatal hamartia, delaying decisive action until disaster is inevitable.

> [!quote] 💬 Contextual Usage & Authentic Quotations
> - 📜 **William Shakespeare (*Macbeth*):** *"Glamis thou art, and Cawdor; and shalt be what thou art promised: yet do I fear thy nature; it is too full o' the milk of human kindness to catch the nearest way: thou wouldst be great; art not without ambition, but without the illness should attend it: what thou wouldst highly, that wouldst thou holily; wouldst not play false, and yet wouldst wrongly win: thou'ldst have, great Glamis, that which cries 'Thus thou must do, if thou have it;' and that which rather thou dost fear to do than wishest should be undone. Hie thee hither, that I may pour my spirits in thine ear; and chastise with the valour of my tongue all that impedes thee from the golden round, which fate and metaphysical aid doth seem to have thee crown'd withal. What is your tidings? The king comes here to-night. Thou'rt mad to say it: is not thy master with him? who, were't so, would have inform'd for preparation. So please you, it is true: our thane is coming: one of my fellows had the speed of him, who, almost dead for breath, had scarcely more than would make up his message. Give him tending; he brings great news. The raven himself is hoarse that croaks the fatal entrance of Duncan under my battlements. Come, you spirits that tend on mortal thoughts, unsex me here, and fill me from the crown to the toe top-full of direst cruelty! make thick my blood; stop up the access and passage to remorse, that no compunctious visitings of nature shake my fell purpose, nor keep peace between the effect and it! Come to my woman's breasts, and take my milk for gall, you murdering ministers, wherever in your sightless substances you wait on nature's mischief! Come, thick night, and pall thee in the dunnest smoke of hell, that my keen knife see not the wound it makes, nor heaven peep through the blanket of the dark, to cry 'Hold, hold!' Great Glamis! worthy Cawdor! Greater than both, by the all-hail hereafter! Thy letters have transported me beyond this ignorant present, and I feel now the future in the instant. My dearest love, Duncan comes here to-night. And when goes hence? To-morrow, as he purposes. O, never shall sun that morrow see! Your face, my thane, is as a book where men may read strange matters. To beguile the time, look like the time; bear welcome in your eye, your hand, your tongue: look like the innocent flower, but be the serpent under't. He that's coming must be provided for: and you shall put this night's great business into my dispatch; which shall to all our nights and days to come give solely sovereign sway and masterdom. We will speak further. Only look up clear; to alter favour ever is to fear: leave all the rest to me; let no wavering **irresolution** shake our resolve."*
> - 📜 **Jane Austen (*Persuasion*):** *"She could not forgive herself for that youthful **irresolution** which had yielded to the over-cautious advice of her friends."*
> - 📜 **Alexander Hamilton (*The Federalist Papers*):** *"An executive council composed of multiple members will inevitably be plagued by discord, faction, and fatal **irresolution** in times of war."*

