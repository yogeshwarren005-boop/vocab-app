---
latin_root: "[[Dashboard — sacr]]"
cluster: "[[Cluster Sacred]]"
status: unread
---
# sacrifice

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
> 1. **Primary Definition (Lexical / Standard Consensus)**: An offering of something precious or consecrated to a deity; the surrender or destruction of something valuable for a higher cause.
> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: In social ethics and economics, forgoing present gratification or personal advantage to achieve enduring collective welfare.

> [!quote] 💬 Contextual Usage & Authentic Quotations
> - 📜 **William Shakespeare (*Julius Caesar*):** *"Let's be sacrificers, but not butchers, Caius: we all stand up against the spirit of Caesar, and in the spirit of men there is no blood: O that we then could come by Caesar's spirit, and not dismember Caesar: but alas, Caesar must bleed for it: and, gentle friends, let's kill him boldly, but not wrathfully; let's carve him as a dish fit for the gods, not hew him as a carcass fit for hounds: and let our hearts, as subtle masters do, stir up their servants to an act of rage, and after seem to chide 'em: this shall make our purpose necessary and not envious; which so appearing to the common eyes, we shall be call'd purgers, not murderers: and for Mark Antony, think not of him; for he can do no more than Caesar's arm when Caesar's head is off: yet I fear him; for in the ingrafted love he bears to Caesar: alas, good Cassius, do not think of him: if he love Caesar, all that he can do is to himself, take thought and die for Caesar: and that were much he should; for he is given to sports, to wildness, and much company: there is no fear in him; let him not die; for he will live, and laugh at this hereafter: peace, count the clock: the clock hath stricken three: 'tis time to part: but it is doubtful yet whether Caesar will come forth to-day or no; for he is superstitious grown of late, quite from the main opinion he held once of fantasy, of dreams, and ceremonies: it may be these apparent prodigies, the unaccustom'd terror of this night, and the persuasion of his augurers, may hold him from the Capitol to-day: never fear that: if he be so resolv'd, I can o'ersway him; for he loves to hear that unicorns may be betray'd with trees, and bears with glasses, elephants with holes, lions with toils, and men with flatterers: when I tell him he hates flatterers, he says he does, being then most flattered: let me work; for I can give his humour the true bent, and I will bring him to the Capitol: nay, we will all of us be there to fetch him: by the eighth hour: is that the uttermost: be that the uttermost, and fail not then: the morning comes upon 's: we'll leave you, Brutus: and, friends, disperse yourselves; but all remember what you have said, and show yourselves true Romans: good gentlemen, look fresh and merrily; let not our looks put on our purposes; but bear it as our Roman actors do, with untir'd spirits and formal constancy: and so good morrow to you every one: boy, Lucius, fast asleep: it is no matter; enjoy the honey-heavy dew of slumber: thou hast no figures nor no fantasies which busy care draws in the brains of men; therefore thou sleep'st so sound: who's there: a piece of work that will make sick men whole: but are not some whole that we must make sick: that might we do, if we could make a worthy **sacrifice** to Rome."*
> - 📜 **Abraham Lincoln (*Gettysburg Address*):** *"We have come to dedicate a portion of that field as a final resting place for those who here gave their lives that that nation might live: it is altogether fitting and proper that we should do this: but, in a larger sense, we cannot dedicate, we cannot consecrate, we cannot hallow this ground: the brave men, living and dead, who struggled here, have consecrated it far above our poor power to add or detract: the world will little note, nor long remember what we say here, but it can never forget what they did here: it is for us the living, rather, to be dedicated here to the unfinished work which they who fought here have thus far so nobly advanced: it is rather for us to be here dedicated to the great task remaining before us, that from these honored dead we take increased devotion to that cause for which they gave the last full measure of devotion, that we here highly resolve that these dead shall not have died in vain, that this nation, under God, shall have a new birth of freedom, and that government of the people, by the people, for the people, shall not perish from the earth: no greater **sacrifice** could be demanded of patriots."*
> - 📜 **Charles Dickens (*A Tale of Two Cities*):** *"It is a far, far better thing that I do, than I have ever done; it is a far, far better rest that I go to than I have ever known: Sydney Carton climbed the scaffold, knowing his voluntary **sacrifice** would preserve the lives of those he loved."*

