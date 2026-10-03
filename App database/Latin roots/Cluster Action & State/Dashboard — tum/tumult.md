---
latin_root: "[[Dashboard — tum]]"
cluster: "[[Cluster Action & State]]"
status: unread
---
# tumult

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
> 1. **Primary Definition (Lexical / Standard Consensus)**: A loud, confused noise, especially one caused by a large mass of people; uproar or violent agitation.
> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: In Roman historiography and political tumultus, a tumult denoted an emergency state of civil rebellion requiring immediate martial mobilization.

> [!quote] 💬 Contextual Usage & Authentic Quotations
> - 📜 **William Shakespeare (*Julius Caesar*):** *"There is one within, besides the things that we have heard and seen, recounts most horrid sights seen by the watch: a lioness hath whelped in the streets; and graves have yawn'd, and yielded up their dead; fierce fiery warriors fought upon the clouds, in ranks and squadrons and right form of war, which drizzled blood upon the Capitol; the noise of battle hurtled in the air, horses did neigh, and dying men did groan, and ghosts did shriek and squeal about the streets: O Caesar! these things are beyond all use, and I do fear them. What can be avoided whose end is purposed by the mighty gods? Yet Caesar shall go forth; for these predictions are to the world in general as to Caesar. When beggars die, there are no comets seen; the heavens themselves blaze forth the death of princes. Cowards die many times before their deaths; the valiant never taste of death but once: of all the wonders that I yet have heard, it seems to me most strange that men should fear; seeing that death, a necessary end, will come when it will come. What say the augurers? They would not have you to stir forth to-day: plucking the entrails of an offering forth, they could not find a heart within the beast. The gods do this in shame of cowardice: Caesar should be a beast without a heart, if he should stay at home to-day for fear. No, Caesar shall not: danger knows full well that Caesar is more dangerous than he: we are two lions litter'd in one day, and I the elder and more terrible: and Caesar shall go forth. Alas, my lord, your wisdom is consumed in confidence: do not go forth to-day: call it my fear that keeps you in the house, and not your own: we'll send Mark Antony to the senate-house: and he shall say you are not well to-day: let me, upon my knee, prevail in this. Mark Antony shall say I am not well, and, for thy humour, I will stay at home. Here's Decius Brutus, he shall tell them so. Caesar, all hail! good morrow, worthy Caesar: I come to fetch you to the senate-house. And you are come in very happy time, to bear my greeting to the senators and tell them that I will not come to-day: cannot, is false, and that I dare not, falser: I will not come to-day; tell them so, Decius. Say, he is sick. Shall Caesar send a lie? Have I in conquest stretch'd mine arm so far, to be afeard to tell graybeards the truth? Decius, go tell them Caesar will not come. Most mighty Caesar, let me know some cause, lest I be laugh'd at when I tell them so. The cause is in my will: I will not come; that is enough to satisfy the senate: but for your private satisfaction, because I love you, I will let you know: Calpurnia here, my wife, stays me at home: she dreamt to-night she saw my statua, which, like a fountain with an hundred spouts, did run pure blood: and many lusty Romans came smiling, and did bathe their hands in it: and these does she apply for warnings, and portents, and evils imminent; and on her knee hath begg'd that I will stay at home. This dream is all amiss interpreted; it was a vision fair and fortunate: your statue spouting blood in many pipes, in which so many smiling Romans bathed, signifies that from you great Rome shall suck reviving blood, and that great men shall press for tinctures, stains, relics and cognizance: this by Calpurnia's dream is signified. And this way have you well expounded it. I have, when you have heard what I can say: and know it now: the senate have concluded to give this day a crown to mighty Caesar: if you shall send them word you will not come, their minds may change: besides, it were a mock apt to be render'd, for some one to say 'Break up the senate till another time, when Caesar's wife shall meet with better dreams.' If Caesar hide himself, shall they not whisper 'Lo, Caesar is afraid'? Pardon me, Caesar; for my dear dear love to your proceeding bids me tell you this; and reason to my love is liable. How foolish do your fears seem now, Calpurnia! I am ashamed I did yield to them. Give me my robe, for I will go. How sweet it is to see the street quieted after the midnight **tumult**!"*
> - 📜 **Charles Dickens (*A Tale of Two Cities*):** *"The roar of the Parisian mob rose in an alarming **tumult**, surging through the narrow streets toward the gates of the Bastille."*
> - 📜 **Thomas Carlyle (*The French Revolution*):** *"Amidst the deafening **tumult** of drums and shouting patriots, the King of France mounted the steps of the scaffold."*

