---
latin_root: "[[Dashboard — cis]]"
cluster: "[[Cluster Separation & Loosening]]"
status: unread
---

# cistern

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
> 1. **Primary Definition (Lexical / Consensus)**: An artificial reservoir, tank, or underground chamber constructed for catching and storing rainwater.
> 2. **Secondary / Nuanced Definition (Contextual / Classical)**: A domestic water-holding tank providing supply to plumbing or irrigation systems.

> [!quote] 💬 Contextual Usage & Authentic Quotations
> - 📜 **William Shakespeare (*Othello*):** *"I had been happy, if the general camp, pioners and all, had tasted her sweet body, so I had nothing known. O, now, for ever farewell the tranquil mind! farewell content! farewell the plumed troop, and the big wars, that make ambition virtue! O, farewell! farewell the neighing steed, and the shrill trump, the spirit-stirring drum, the ear-piercing fife, the royal banner, and all quality, pride, pomp and circumstance of glorious war! And, O you mortal engines, whose rude throats the immortal Jove's dead clamours counterfeit, farewell! Othello's occupation's gone! Villain, be sure thou prove my love a whore, be sure of it; give me the ocular proof: or, by the worth of man's eternal soul, thou hadst been better have been born a dog than answer my waked wrath! Is't come to this? Make me to see't; or, at the least, so prove it, that the probation bear no hinge nor loop to hang a doubt on; or woe upon thy life! My noble lord— If thou dost slander her and torture me, never pray more; abandon all remorse; on horror's head horrors accumulate; do deeds to make heaven weep, all earth amazed; for nothing canst thou to damnation add greater than that. O grace! O heaven forgive me! Are you a man? have you a soul or sense? God be wi' you; take mine office. O wretched fool, that livest to make thine honesty a vice! O monstrous world! Take note, take note, O world, to be direct and honest is not safe. I thank you for this profit; and from hence I'll love no friend, sith love breeds such offence. Nay, stay: thou shouldst be honest. I should be wise, for honesty's a fool and loses that it works for. By the world, I think my wife be honest and think she is not; I think thou art just and think thou art not. I'll have some proof. Her name, that was as fresh as Dian's visage, is now begrimed and black as mine own face. If there be cords, or knives, poison, or fire, or suffocating streams, I'll not endure it. Would I were satisfied! I see, sir, you are eaten up with passion: I do repent me that I put it to you. You would be satisfied? Would! nay, I will. And may: but, how? how satisfied, my lord? Would you, the supervisor, grossly gape on? Behold her topp'd? Death and damnation! O! It were a tedious difficulty, I think, to bring them to that prospect: damn them then, if ever mortal eyes do see them bolster more than their own! What then? how then? What shall I say? Where's satisfaction? It is impossible you should see this, were they as prime as goats, as hot as monkeys, as salt as wolves in pride, and fools as gross as ignorance made drunk. But yet, I say, if imputation and strong circumstances, which lead directly to the door of truth, will give you satisfaction, you may have't. Give me a living reason she's disloyal. I do not like the office: but, sith I am enter'd in this cause so far, prick'd to't by foolish honesty and love, I will go on. I lay with Cassio lately; and, being troubled with a raging tooth, I could not sleep. There are a kind of men so loose of soul, that in their sleeps will mutter their affairs: one of this kind is Cassio: in sleep I heard him say 'Sweet Desdemona, let us be wary, let us hide our loves;' and then, sir, would he gripe and wring my hand, cry 'O sweet creature!' and then kiss me hard, as if he pluck'd up kisses by the roots that grew upon my lips: then laid his leg over my thigh, and sigh'd, and kiss'd; and then cried 'Cursed fate that gave thee to the Moor!' O monstrous! monstrous! Nay, this was but his dream. But this denoted a foregone conclusion: 'tis a shrewd doubt, though it be but a dream. And this may help to thicken other proofs that do demonstrate thinly. I'll tear her all to pieces. Nay, but be wise: yet we see nothing done; she may be honest yet. Tell me but this, have you not sometimes seen a handkerchief spotted with strawberries in your wife's hand? I gave her such a one; 'twas my first gift. I know not that; but such a handkerchief—I am sure it was your wife's—did I to-day see Cassio wipe his beard with. If it be that— If it be that, or any that was hers, it speaks against her with the other proofs. O, that the slave had forty thousand lives! one is too poor, too weak for my revenge. Now do I see 'tis true. Look here, Iago; all my fond love thus do I blow to heaven. 'Tis gone. Arise, black vengeance, from the hollow hell! Yield up, O love, thy crown and hearted throne to tyrannous hate! Swell, bosom, with thy fraught, for 'tis of aspics' tongues! Yet be content. O, blood, blood, blood! Patience, I say; your mind perhaps may change. Never, Iago. Like to the Pontic sea, whose icy current and compulsive course ne'er feels retiring ebb, but keeps due on to the Propontic and the Hellespont, even so my bloody thoughts, with violent pace, shall ne'er look back, ne'er ebb to humble love, till that a capable and wide revenge swallow them up. Now, by yond marble heaven, in the due reverence of a sacred vow I here engage my words. Do not rise yet. Witness, you ever-burning lights above, you elements that clip us round about, witness that here Iago doth give up the execution of his wit, hands, heart, to wrong'd Othello's service! Let him command, and to obey shall be in me remorse, what bloody business ever. I greet thy love, not with vain thanks, but with acceptance bounteous, and will upon the instant put thee to't: within these three days let me hear thee say that Cassio's not alive. My friend is dead; 'tis done at your request: but let her live. Damn her, lewd minx! O, damn her! Come, go with me apart; I will withdraw, to furnish me with some swift means of death for the fair devil. Now art thou my lieutenant. I am your own for ever. A foul knot, a discarded **cistern** of foul toads."*
> - 📜 **Charles Dickens (*Great Expectations*):** *"The leaden **cistern** in the damp courtyard was covered with green slime, collecting the steady drizzle from the eaves."*
> - 📜 **Lord Macaulay (*The History of England*):** *"Every Roman villa was provided with a spacious **cistern** excavated in the solid rock to catch the winter rains."*
