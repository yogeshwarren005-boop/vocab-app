---
latin_root: "[[Dashboard — lud]]"
cluster: "[[Cluster Action & State]]"
status: unread
tier: 2
tier_label: "Words to learn a little later"
zipf: 2.3
rank: 31557
---
# interlude

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
> 1. **Primary Definition (Lexical / Standard Consensus)**: An intervening period of time, or a performance staged between parts of a play or musical work.
> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: In Tudor drama and early theater history, an interlude was a brief, witty satirical morality sketch performed between banquet courses.

> [!quote] 💬 Contextual Usage & Authentic Quotations
> - 📜 **William Shakespeare (*A Midsummer Night's Dream*):** *"There is a brief how many sports are ripe: make choice of which your highness will see first. The battle with the Centaurs, to be sung by an Athenian eunuch to the harp. We'll none of that: that have I told my love, in glory of my kinsman Hercules. The riot of the tipsy Bacchanals, tearing the Thracian singer in their rage. That is an old device; and it was play'd when I from Thebes came last a conqueror. The thrice three Muses mourning for the death of Learning, late deceased in beggary. That is some satire, keen and critical, not sorting with a nuptial ceremony. A tedious brief scene of young Pyramus and his love Thisbe; very tragical mirth. Merry and tragical! Tedious and brief! That is, hot ice and wondrous strange snow. How shall we find the concord of this discord? A play there is, my lord, some ten words long, which is as brief as I have known a play; but by ten words, my lord, it is too long, which makes it tedious; for in all the play there is not one word apt, one player fitted: and tragical, my noble lord, it is; for Pyramus therein doth kill himself. Which, when I saw rehearsed, I must confess, made mine eyes water; but more merry tears the passion of loud laughter never shed. What are they that do play it? Hard-handed men that work in Athens here, which never labour'd in their minds till now, and now have toil'd their unbreathed memories with this same play, against your nuptial. And we will hear it. No, my noble lord; it is not for you: I have heard it over, and it is nothing, nothing in the world; unless you can find sport in their intents, extremely stretch'd and conn'd with cruel pain, to do you service. I will hear that play; for never anything can be amiss, when simpleness and duty tender it. Go, bring them in: and take your places, ladies. I love not to see wretchedness o'ercharged and duty in his service perishing. Why, gentle sweet, you shall see no such thing. He says they can do nothing in this kind. The kinder we, to give them thanks for nothing. Our sport shall be to take what they mistake: and what poor duty cannot do, noble respect takes it in might, not merit. Where I have come, great clerks have purposed to greet me with premeditated welcomes; where I have seen them shiver and look pale, make periods in the midst of sentences, throttle their practised accent in their fears and in conclusion dumbly have broke off, not paying me a welcome. Trust me, sweet, out of this silence yet I pick'd a welcome; and in the modesty of fearful duty I read as much as from the rattling tongue of saucy and audacious eloquence. Love, therefore, and tongue-tied simplicity in least speak most, to my capacity. So please your grace, the Prologue is address'd. Let him approach. If we offend, it is with our good will. That you should think, we come not to offend, but with good will. To show our simple skill, that is the true beginning of our end. Consider then we come but in despite. We do not come as minding to content you, our true intent is. All for your delight we are not here. That you should here repent you, the actors are at hand and by their show you shall know all that you are like to know. This fellow doth not stand upon points. He hath rid his prologue like a rough colt; he knows not the stop. A good moral, my lord: it is not enough to speak, but to speak true. Indeed he hath played on his prologue like a child on a recorder; a sound, but not in government. His speech was like a tangled chain; nothing impaired, but all disordered. Who is next? Gentles, perchance you wonder at this show; but wonder on, till truth make all things plain. This man is Pyramus, if you would know; this beauteous lady Thisby is certain. This man, with lime and rough-cast, doth present Wall, that vile Wall which did these lovers sunder; and through Wall's chink, poor souls, they are content to whisper. At the which let no man wonder. This man, with lanthorn, dog, and bush of thorn, presenteth Moonshine; for, if you will know, by moonshine did these lovers think no scorn to meet at Ninus' tomb, there, there to woo. This grisly beast, which Lion hight by name, the trusty Thisby, coming first by night, did scare away, or rather did affright; and, as she fled, her mantle she did fall, which Lion vile with bloody mouth did stain. Anon comes Pyramus, sweet youth and tall, and finds his trusty Thisby's mantle slain: whereat, with blade, with bloody blameful blade, he bravely broach'd his boiling bloody breast; and Thisby, tarrying in mulberry shade, his dagger drew, and died. For all the rest, let Lion, Moonshine, Wall, and lovers twain at large discourse, while here they do remain. I wonder if the lion be to speak. One lion may, my lord, when many asses do. In this same **interlude** it doth befall that I, one Snout by name, present a wall."*
> - 📜 **Thomas Carlyle (*The French Revolution*):** *"A brief summer **interlude** of peace deceived the National Assembly before the tempest of civil war broke forth."*
> - 📜 **George Eliot (*Middlemarch*):** *"The evening party provided an agreeable **interlude** amidst the dull provincial duties of the winter."*

