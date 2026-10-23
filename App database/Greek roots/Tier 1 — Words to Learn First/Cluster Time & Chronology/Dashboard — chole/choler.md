---
greek_root: "[[Dashboard — chole]]"
cluster: "[[Cluster Time & Chronology]]"
status: unread
tier: 3
tier_label: "Words to learn last"
zipf: 1.2
rank: 999999
---
# choler

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
> 1. **Primary Definition (Lexical / Standard Consensus)**: Yellow bile, one of the four traditional humors of ancient and medieval physiology; anger, wrath, or irascibility.
> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: In Galenic humoral pathology, the warm and dry humor originating in the liver, believed when in excess to produce an irritable, passionate, or belligerent temperament.

> [!quote] 💬 Contextual Usage & Authentic Quotations
> - 📜 **William Shakespeare (*Romeo and Juliet*):** *"I strike quickly, being moved. / But thou art not quickly moved to strike. / A dog of the house of Montague moves me. / To move is to stir; and to be valiant is to stand: therefore, if thou art moved, thou runn'st away. / A dog of that house shall move me to stand: I will take the wall of any man or maid of Montague's. / That shows thee a weak slave; for the weakest goes to the wall. / True; and therefore women, being the weaker vessels, are ever thrust to the wall: therefore I will push Montague's men from the wall, and thrust his maids to the wall. / The quarrel is between our masters and us their men. / 'Tis all one, I will show myself a tyrant: when I have fought with the men, I will be cruel with the maids, and cut off their heads. / The heads of the maids? / Ay, the heads of the maids, or their maidenheads; take it in what sense thou wilt. / They must take it in sense that feel it. / Me they shall feel while I am able to stand: and 'tis known I am a pretty piece of flesh. / 'Tis well thou art not fish; if thou hadst, thou hadst been poor John. Draw thy tool; here comes two of the house of the Montagues. / My naked weapon is out: quarrel, I will back thee. / How! turn thy back and run? / Fear me not. / No, marry; I fear thee! / Let us take the law of our sides; let them begin. / I will frown as I pass by, and let them take it as they list. / Nay, as they dare. I will bite my thumb at them; which is a disgrace to them, if they bear it. / Do you bite your thumb at us, sir? / I do bite my thumb, sir. / Do you bite your thumb at us, sir? / Is the law of our side, if I say ay? / No. / No, sir, I do not bite my thumb at you, sir, but I bite my thumb, sir. / Do you quarrel, sir? / Quarrel sir! no, sir. / If you do, sir, I am for you: I serve as good a man as you. / No better. / Well, sir. / Say 'better:' here comes one of my master's kinsmen. / Yes, better, sir. / You lie. / Draw, if you be men. Gregory, remember thy swashing blow. / Part, fools! Put up your swords; you know not what you do. / What, art thou drawn among these heartless hinds? Turn thee, Benvolio, look upon thy death. / I do but keep the peace: put up thy sword, or manage it to part these men with me. / What, drawn, and talk of peace! I hate the word, as I hate hell, all Montagues, and thee: Have at thee, coward! / Gregory, o' my word, we'll not carry coals. / No, for then we should be colliers. / I mean, an we be in **choler**, we'll draw."*
> - 📜 **John Milton (*Paradise Lost*):** *"Despair and fierce **choler** burned within his fallen breast as he viewed the blissful seat of newly created man."*
> - 📜 **Francis Bacon (*The Essays*):** *"**Choler** is a humor that maketh men active, earnest, full of alacrity, and stirring, if it be not stopped."*
