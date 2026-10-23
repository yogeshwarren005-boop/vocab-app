---
latin_root: "[[Dashboard — victor]]"
cluster: "[[Cluster War]]"
status: unread
tier: 1
tier_label: "Words to learn first"
zipf: 4
rank: 6445
---
# victor

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
> 1. **Primary Definition (Lexical / Standard Consensus)**: A person who defeats an enemy or opponent in a battle, contest, game, or competition; a winner.
> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: In classical Roman culture, a conquering general awarded a triumph through the streets of Rome to the temple of Jupiter Capitolinus.

> [!quote] 💬 Contextual Usage & Authentic Quotations
> - 📜 **William Shakespeare (*Julius Caesar*):** *"O, pardon me, thou bleeding piece of earth, that I am meek and gentle with these butchers! Thou art the ruins of the noblest man that ever lived in the tide of times; woe to the hand that shed this costly blood! Over thy wounds now do I prophesy, which like dumb mouths do ope their ruby lips to beg the voice and utterance of my tongue: a curse shall light upon the limbs of men; domestic fury and fierce civil strife shall cumber all the parts of Italy; blood and destruction shall be so in use, and dreadful objects so familiar, that mothers shall but smile when they behold their infants quarter'd with the hands of war; all pity chok'd with custom of fell deeds; and Caesar's spirit, ranging for revenge, with Ate by his side come hot from hell, shall in these confines with a monarch's voice cry 'Havoc!' and let slip the dogs of war; that this foul deed shall smell above the earth with carrion men, groaning for burial; where stands the **victor** trembling at his crime."*
> - 📜 **John Milton (*Paradise Lost*):** *"To whom the goblin full of wrath replied: Art thou that Traitor Angel, art thou he, who first broke peace in Heaven and faith, till then unbroken, and in proud rebellious arms drew after him the third part of Heaven's sons conjured against the Highest, for which both thou and they outcast from God are here condemned to waste eternal days in woe and pain? And reckon'st thou thyself with spirits of Heaven, hell-doomed, and breath'st defiance here and scorn, where I reign king, and of all spirits in Hell supreme sovereign? Back to thy punishment, false fugitive, and to thy speed add wings, lest with a whip of scorpions I pursue thy lingering, or with one stroke of this dart strange horror seize thee, and pangs unfelt before; so spake the grisly terror, and in shape, so speaking and so threatening, grew tenfold more dreadful and deform; on the other side, incensed with indignation, Satan stood unterrified, and like a comet burned, that fires the length of Ophiuchus huge in the arctic sky, and from his horrid hair shakes pestilence and war; each at the head leveled his deadly aim; their fatal hands no second stroke intend; and such a frown each cast at the other as when two black clouds with Heaven's artillery fraught come rattling on over the Caspian, then stand front to front hovering a space, till winds the signal blow to join their dark encounter in mid air; so frowned the mighty combatants that Hell grew darker at their frown; so matched they stood; for never but once more was either like to meet so great a foe; and now great deeds had been achieved, whereof all Hell had rung, had not the snaky sorceress that sat fast by Hell Gate and kept the fatal key, risen, and with hideous outcry rushed between, forbidding either **victor** to strike the fatal blow."*
> - 📜 **Edward Gibbon (*The Decline and Fall of the Roman Empire*):** *"The generous **victor** spared the captive queen, escorting Zenobia to Rome with regal magnificence rather than chains."*
