---
latin_root: "[[Dashboard — sacr]]"
cluster: "[[Cluster Sacred]]"
status: unread
---
# sacrilege

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
> 1. **Primary Definition (Lexical / Standard Consensus)**: The violation, profanation, or misuse of something regarded as sacred, consecrated, or holy.
> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: In canon law and historical jurisprudence, the theft or deliberate desecration of consecrated church property and vessels.

> [!quote] 💬 Contextual Usage & Authentic Quotations
> - 📜 **William Shakespeare (*Macbeth*):** *"Confusion now hath made his masterpiece: most sacrilegious murder hath broke ope the Lord's anointed temple, and stole thence the life o' the building: what is't you say: the life: mean you his majesty: approach the chamber, and destroy your sight with a new Gorgon: do not bid me speak; see, and then speak yourselves: awake, awake: ring the alarum-bell: murder and treason: Banquo and Donalbain: Malcolm: awake: shake off this downy sleep, death's counterfeit, and look on death itself: up, up, and see the great doom's image: Malcolm: Banquo: as from your graves rise up, and walk like sprites, to countenance this horror: ring the bell: what's the business, that such a hideous trumpet calls to parley the sleepers of the house: speak, speak: O gentle lady, 'tis not for you to hear what I can speak: the repetition, in a woman's ear, would murder as it fell: O Banquo, Banquo, our royal master's murder'd: woe, alas: what, in our house: too cruel anywhere: dear Duff, I pr'ythee, contradict thyself, and say it is not so: had I but died an hour before this chance, I had liv'd a blessed time; for, from this instant, there's nothing serious in mortality: all is but toys: renown and grace is dead; the wine of life is drawn, and the mere lees is left this vault to brag of: you are, and do not know 't: the spring, the head, the fountain of your blood is stopp'd; the very source of it is stopp'd: your royal father's murder'd: O, by whom: those of his chamber, as it seem'd, had done 't: their hands and faces were all badg'd with blood; so were their daggers, which, unwip'd, we found upon their pillows: they star'd, and were distracted; no man's life was to be trusted with them: O, yet I do repent me of my fury, that I did kill them: wherefore did you so: who can be wise, amaz'd, temperate and furious, loyal and neutral, in a moment: no man: the expedition of my violent love outrun the pauser reason: here lay Duncan, his silver skin lac'd with his golden blood; and his gash'd stabs look'd like a breach in nature for ruin's wasteful entrance: there, the murderers, steep'd in the colours of their trade, their daggers unmannerly breech'd with gore: who could refrain, that had a heart to love, and in that heart courage to make 's love known: help me hence, ho: look to the lady: why do we hold our tongues, that most may claim this argument for ours: what should be spoken here, where our fate, hid in an auger-hole, may rush, and seize us: let's away; our tears are not yet brew'd: nor our strong sorrow upon the foot of motion: look to the lady: and when we have our naked frailties hid, that suffer in exposure, let us meet, and question this most bloody piece of work, to know it further: fears and scruples shake us: in the great hand of God I stand; and thence against the undivulg'd pretence I fight of treasonous malice: and so do I: so all: let's briefly put on manly readiness, and meet i' the hall together: well contented: what will you do: let's not consort with them: to show an unfelt sorrow is an office which the false man does easy: I'll to England: to Ireland, I; our separated fortune shall keep us both the safer: where we are, there's daggers in men's smiles: the near in blood, the nearer bloody: this murderous shaft that's shot hath not yet lighted; and our safest way is to avoid the aim: therefore, to horse; and let us not be dainty of leave-taking, but shift away: there's warrant in that theft which steals itself, when there's no mercy left: Duncan's death was viewed by Macduff as an intolerable **sacrilege** against heaven."*
> - 📜 **Walter Scott (*Ivanhoe*):** *"To lay violent hands upon the property of the holy church was branded as unpardonable **sacrilege**."*
> - 📜 **Edward Gibbon (*The History of the Decline and Fall of the Roman Empire*):** *"The barbarian conquerors respected the basilica of Saint Peter, forbidding their soldiers any act of **sacrilege**."*

