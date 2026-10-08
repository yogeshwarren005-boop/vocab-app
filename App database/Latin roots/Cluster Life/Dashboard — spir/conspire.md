---
latin_root: "[[Dashboard — spir]]"
cluster: "[[Cluster Life]]"
status: unread
---

# conspire

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
> 1. **Primary Definition (Lexical / Standard Consensus)**: To make secret plans jointly to commit an unlawful, treacherous, or harmful act.
> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: Of circumstances or events, to act together to bring about a particular result.

> [!quote] 💬 Contextual Usage & Authentic Quotations
> - 📜 **John Keats (*To Autumn*):** *"Season of mists and mellow fruitfulness, close bosom-friend of the maturing sun, they **conspire** how to load and bless the vines with fruit."*
> - 📜 **William Shakespeare (*The Tempest*):** *"I say, by sorcery he got this isle; / From me he got it. if thy greatness will / Revenge it on him,—for I know thou darest, / But this can not! / That's most certain. / Thou shalt be lord of it and I'll serve thee. / How now shall this be compassed? / Canst thou bring me to the party? / Yea, yea, my lord: I'll yield him thee asleep, / Where thou mayst knock a nail into his head. / Thou liest; thou canst not. / What a pied ninny's this! Thou scurvy patch! / I do beseech thy greatness, give him blows / And take his bottle from him: when that's gone / He shall drink nought but brine; for I'll not show him / Where the quick freshes are. / Trinculo, run into no further danger: / Interrupt the monster one word further, / And, by this hand, I'll turn my mercy out o' doors / And make a stock-fish of thee. / Why, what did I? I did nothing. / I'll go farther off. / Didst thou not say he lied? / Thou liest. / Do I so? take thou that. / As you like this, give me the lie another time. / Mum, then; and no more. Proceed. / Why, as I told thee, 'tis a custom with him, / I' the afternoon to sleep: there thou mayst brain him, / Having first seized his books, or with a log / Batter his skull, or paunch him with a stake, / Or cut his wezand with thy knife. Remember / First to possess his books; for without them / He's but a sot, as I am, nor hath not / One spirit to command: they all do hate him / As rootedly as I. Burn but his books. / He has brave utensils,—for so he calls them— / Which, when he has a house, he'll deck withal / And that most deeply to consider is / The beauty of his daughter; he himself / Calls her a nonpareil: I never saw a woman, / But Only Sycorax my dam and she; / But she as far surpasseth Sycorax / As great'st does least. / Is it so fine a lass? / Ay, lord; she will become thy bed, I warrant. / And bring thee forth brave brood. / Monster, I will kill this man: his daughter and / I will be king and queen,—save our graces!—and / Trinculo and thyself shall be viceroys. / Dost thou like the plot, Trinculo? / Excellent. / Give me thy hand: I am sorry I beat thee; / But, while thou livest, keep a good tongue in thy head. / Within this half hour will he be asleep: / Wilt thou destroy him then? / Ay, on mine honour. / This will I tell my master. / Thou makest me merry; I am full of pleasure: / Let us be jocund: will you troll the catch / You taught me but while-ere? / At thy request, monster, I will do reason, / Any reason. Come on, Trinculo, let us sing. / Flout 'em and scout 'em / And scout 'em and flout 'em / Thought is free. / That's not the tune. / What is this same? / This is the tune of our catch, play'd by the picture / Of Nobody. / If thou beest a man, show thyself in thy likeness: / If thou beest a devil, take't as thou list. / O, forgive me my sins! / He that dies pays all debts: I defy thee. / Mercy upon us! / Art thou afeard? / No, monster, not I. / Be not afeard; the isle is full of noises, / Sounds and sweet airs, that give delight and hurt not. / Sometimes a thousand twangling instruments / Will hum about mine ears, and sometime voices / That, if I then had waked after long sleep, / Will make me sleep again: and then, in dreaming, / The clouds methought would open and show riches / Ready to drop upon me that, when I waked, / I cried to dream again. / This will prove a brave kingdom to me, / Where I shall have my music for nothing. / When Prospero is destroyed. / That shall be by and by: I remember the story. / The sound is going away; let's follow it, / And after do our work. / Lead, monster; we'll follow. I would I could see / This taborer; he lays it on. / Wilt come? / I'll follow, Stephano, as we **conspire** together."*
> - 📜 **Charles Dickens (*Oliver Twist*):** *"Circumstances seemed to **conspire** against the poor parish orphan at every turn."*
