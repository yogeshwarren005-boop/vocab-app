---
greek_root: "[[Dashboard — drach]]"
cluster: "[[Cluster Society & Governance]]"
status: unread
---
# drachm

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
> 1. **Primary Definition (Lexical / Standard Consensus)**: A unit of weight in the apothecaries' system equal to 60 grains or one-eighth of an ounce (approximately 3.887 grams); a dram.
> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: In historical pharmacy and British imperial measures, a liquid measure equal to one fluid dram (60 minims).

> [!quote] 💬 Contextual Usage & Authentic Quotations
> - 📜 **William Shakespeare (*Romeo and Juliet*):** *"Let me have A **drachm** of poison, such soon-speeding gear As will disperse itself through all the veins."*
> - 📜 **Thomas Browne (*Pseudodoxia Epidemica*):** *"The apothecary dispensed the dried mandrake root measured to the precise fraction of a **drachm**."*
> - 📜 **John Keats (*Ode to a Nightingale*):** *"My heart aches, and a drowsy numbness pains My sense, as though of hemlock I had drunk, Or emptied some dull opiate to the drains One minute past, and Lethe-wards had sunk: 'Tis not through envy of thy happy lot, But being too happy in thine happiness,—That thou, light-winged Dryad of the trees, In some melodious plot Of beechen green, and shadows numberless, Singest of summer in full-throated ease. O, for a draught of vintage! that hath been Cool'd a long age in the deep-delved earth, Tasting of Flora and the country green, Dance, and Provençal song, and sunburnt mirth! O for a beaker full of the warm South, Full of the true, the blushful Hippocrene, With beaded bubbles winking at the brim, And purple-stained mouth; That I might drink, and leave the world unseen, And with thee fade away into the forest dim: Fade far away, dissolve, and quite forget What thou among the leaves hast never known, The weariness, the fever, and the fret Here, where men sit and hear each other groan; Where palsy shakes a few, sad, last gray hairs, Where youth grows pale, and spectre-thin, and dies; Where but to think is to be full of sorrow And leaden-eyed despairs, Where Beauty cannot keep her lustrous eyes, Or new Love pine at them beyond to-morrow. Away! away! for I will fly to thee, Not charioted by Bacchus and his pards, But on the viewless wings of Poesy, Though the dull brain perplexes and retards: Already with thee! tender is the night, And haply the Queen-Moon is on her throne, Cluster'd around by all her starry Fays; But here there is no light, Save what from heaven is with the breezes blown Through verdurous glooms and winding mossy ways. I cannot see what flowers are at my feet, Nor what soft incense hangs upon the boughs, But, in embalmed darkness, guess each sweet Wherewith the seasonable month endows The grass, the thicket, and the fruit-tree wild; White hawthorn, and the pastoral eglantine; Fast fading violets cover'd up in leaves; And mid-May's eldest child, The coming musk-rose, full of dewy wine, The murmurous haunt of flies on summer eves. Darkling I listen; and, for many a time I have been half in love with easeful Death, Call'd him soft names in many a mused rhyme, To take into the air my quiet breath; Now more than ever seems it rich to die, To cease upon the midnight with no pain, While thou art pouring forth thy soul abroad In such an ecstasy! Still wouldst thou sing, and I have ears in vain—To thy high requiem become a sod. Thou wast not born for death, immortal Bird! No hungry generations tread thee down; The voice I hear this passing night was heard In ancient days by emperor and clown: Perhaps the self-same song that found a path Through the sad heart of Ruth, when, sick for home, She stood in tears amid the alien corn; The same that oft-times hath Charm'd magic casements, opening on the foam Of perilous seas, in faery lands forlorn. Forlorn! the very word is like a bell To toll me back from thee to my sole self! Adieu! the fancy cannot cheat so well As she is fam'd to do, deceiving elf. Adieu! adieu! thy plaintive anthem fades Past the near meadows, over the still stream, Up the hill-side; and now 'tis buried deep In the next valley-glades: Was it a vision, or a waking dream? Fled is that music:—Do I wake or sleep?"*
> - 📜 **Arthur Conan Doyle (*A Study in Scarlet*):** *"Four grains of the alkaloid were dissolved in half a **drachm** of pure distilled water."*
