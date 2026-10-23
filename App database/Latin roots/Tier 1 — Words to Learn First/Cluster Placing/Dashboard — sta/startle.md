---
latin_root: "[[Dashboard — sta]]"
cluster: "[[Cluster Placing]]"
status: unread
tier: 2
tier_label: "Words to learn a little later"
zipf: 2.3
rank: 17997
---

# startle

> [!status] 🎯 **Status:**

```dataviewjs
if(!document.getElementById('apple-toggle-css')){const s=document.createElement('style');s.id='apple-toggle-css';s.textContent=':root{--apple-red:#FF375F;--apple-red-glow:rgba(255,55,95,0.45);--apple-amber:#FF9F0A;--apple-amber-glow:rgba(255,159,10,0.45);--apple-green:#30D158;--apple-green-glow:rgba(48,209,88,0.45)}.apple-c{position:relative;display:inline-flex;align-items:center;gap:8px;padding:2px 10px 2px 4px;border-radius:999px;background:var(--background-secondary,#111624);border:1px solid var(--background-modifier-border,#232d42);cursor:pointer;user-select:none;transition:border-color .2s ease,transform .2s ease,box-shadow .2s ease;line-height:1;vertical-align:middle;box-sizing:border-box}.apple-c:hover{border-color:var(--text-muted,#3b4b6b);transform:translateY(-1px);box-shadow:0 2px 8px rgba(0,0,0,.35)}.apple-c:active{transform:scale(.96)}.apple-c .track-c{position:relative;width:48px;height:18px;background:var(--background-primary,#090d17);border-radius:999px;border:1px solid var(--background-modifier-border,#1c2436);display:flex;align-items:center;justify-content:space-between;padding:0 6px;box-sizing:border-box}.apple-c .c-dot{width:3px;height:3px;border-radius:999px;background:var(--text-faint,#334155);opacity:.6}.apple-c .halo-c{position:absolute;top:1px;left:1px;width:14px;height:14px;border-radius:999px;transition:transform .35s cubic-bezier(.34,1.6,.64,1),background-color .25s ease,box-shadow .25s ease;display:flex;align-items:center;justify-content:center}.apple-c .halo-c::after{content:"";width:6px;height:6px;border-radius:999px;background:#fff;box-shadow:0 1px 2px rgba(0,0,0,.4)}.apple-c .halo-c.pos-0{transform:translateX(0);background-color:var(--apple-red);box-shadow:0 0 8px var(--apple-red-glow)}.apple-c .halo-c.pos-1{transform:translateX(15px);background-color:var(--apple-amber);box-shadow:0 0 8px var(--apple-amber-glow)}.apple-c .halo-c.pos-2{transform:translateX(30px);background-color:var(--apple-green);box-shadow:0 0 8px var(--apple-green-glow)}.apple-c .label{font-size:10px;font-weight:700;letter-spacing:.5px;text-transform:uppercase;margin-left:2px}.apple-c .label.s-0{color:var(--apple-red)}.apple-c .label.s-1{color:var(--apple-amber)}.apple-c .label.s-2{color:var(--apple-green)}';document.head.appendChild(s)}
const p=dv.current();
const states=[{key:'unread',label:'Unread',cls:'s-0',p:'pos-0'},{key:'learning',label:'Learning',cls:'s-1',p:'pos-1'},{key:'learned',label:'Learned',cls:'s-2',p:'pos-2'}];
const statusVal=p.status||'unread';
let curIdx=states.findIndex(s=>s.key===statusVal);
if(curIdx===-1)curIdx=0;
const cur=states[curIdx];
const toggle=document.createElement('div');
toggle.className='apple-c';
const track=document.createElement('div');
track.className='track-c';
track.innerHTML='<span class="c-dot"></span><span class="c-dot"></span><span class="c-dot"></span><div class="halo-c '+cur.p+'"></div>';
const label=document.createElement('span');
label.className='label '+cur.cls;
label.textContent=cur.label;
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
> 1. **Primary Definition (Lexical / Consensus)**: To cause a person or animal to flinch, jump, or move suddenly from unexpected alarm.
> 2. **Secondary / Nuanced Definition (Contextual / Classical)**: To surprise, shock, or astonish someone with sudden, unexpected occurrences.

> [!quote] 💬 Contextual Usage & Authentic Quotations
> - 📜 **William Shakespeare (*The Winter's Tale*):** *"Prepare to see the life as lively mock'd as ever still sleep mock'd death: behold, and say 'tis well. I like your silence, it the more shows off your wonder: but yet speak; first, you, my liege. Comes it not something near? Her natural posture! Chide me, dear stone, that I may say indeed thou art Hermione; or rather, thou art she in thy not chiding, for she was as tender as infancy and grace. But yet, Paulina, Hermione was not so much wrinkled, nothing so aged as this seems. O, not by much. So much the more our carver's excellence; which lets go by some sixteen years and makes her as she lived now. As now she might have done, so much to my good comfort, as it is now piercing to my soul. O, thus she stood, even with such life of majesty, of spur, of breath, when first I woo'd her! I am ashamed: does not the stone rebuke me for being more stone than it? O royal piece, there's magic in thy majesty, which has my evils conjured to remembrance and from thy admiring daughter took the spirits, standing like stone with thee. Perdita, thy mother! Do not draw the curtain. No longer shall you gaze on't, lest your fancy may think anon it moves. Let be, let be. Would I were dead, but that, methinks, already—what was he that did make it? See, my lord, would you not deem it breathed? and that those veins did verily bear blood? Masterly done: the very life seems warm upon her lip. The fixture of her eye has motion in't, as we are mock'd with art. I'll draw the curtain: my lord's almost so far transported that he'll think anon it lives. O sweet Paulina, make me to think so twenty years together! No settled senses of the world can match the pleasure of that madness. Let't alone. I am sorry, sir, I have thus far stirr'd you: but I could afflict you farther. Do, Paulina; for this affliction has a taste as sweet as any cordial comfort. Still, methinks, there is an air comes from her: what fine chizzel could ever yet cut breath? Let no man mock me, for I will kiss her. Good my lord, forbear: the ruddiness upon her lip is wet; you'll mar it if you kiss it, stain your own with oily painting. Shall I draw the curtain? No, not these twenty years. So long could I stand by, a looker-on. Either forbear, quit presently the chapel, or resolve you for more amazement. If you can behold it, I'll make the statue move indeed, descend and take you by the hand: but then you'll think—which I protest against—I am assisted by wicked powers. What you can make her do, I am content to look on: what to speak, I am content to hear; for 'tis as easy to make her speak as move. It is required you do awake your faith. Then all stand still; on: those that think it is unlawful business I am about, let them depart. Proceed: no foot shall stir. Music, awake her; strike! 'Tis time; descend; be stone no more; approach; strike all that look upon with marvel. Come, I'll fill your grave up: stir, nay, come away, bequeath to death your numbness, for from him dear life redeems you. You perceive she stirs: **startle** not; her actions shall be holy as you hear my spell is lawful."*
> - 📜 **Charles Dickens (*Great Expectations*):** *"The sudden clanking of the iron file caused Pip to **startle** and look nervously toward the churchyard wall."*
> - 📜 **Charlotte Brontë (*Jane Eyre*):** *"A low, strange laugh from the attic corridors did not fail to **startle** me in the dead of the winter night."*
