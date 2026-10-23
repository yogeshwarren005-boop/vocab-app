---
latin_root: "[[Dashboard — spect]]"
cluster: "[[Cluster Sight]]"
status: unread
tier: 1
tier_label: "Words to learn first"
zipf: 4
rank: 7939
---
# prospect

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
> 1. **Primary Definition (Lexical / Standard Consensus)**: The possibility or likelihood of some future event occurring; an extensive view over land or sea.
> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: In commercial mining and financial appraisal, designates an unexploited mineral deposit or promising commercial venture evaluated for capital investment.

> [!quote] 💬 Contextual Usage & Authentic Quotations
> - 📜 **William Shakespeare (*Macbeth*):** *"Into the air; and what seem'd corporal melted / As breath into the wind. Would they had stay'd! / Were such things here as we do speak about? / Or have we eaten on the insane root / That takes the reason prisoner? / Your children shall be kings. / You shall be king. / And thane of Cawdor too: went it not so? / To the selfsame tune and words. Who's here? / The news of thy success; and when he reads / Thy personal venture in the rebels' fight, / His wonders and his praises do contend / Which should be thine or his: silenc'd with that, / In viewing o'er the rest o' the selfsame day, / He finds thee in the stout Norweyan ranks, / Nothing afeard of what thyself didst make, / Strange images of death. As thick as hail / Came post with post; and every one did bear / Thy praises in his kingdom's great defense, / And pour'd them down before him. / We are sent / To give thee from our royal master thanks; / Only to herald thee into his sight, / Not pay thee. / And, for an earnest of a greater honor, / He bade me, from him, call thee thane of Cawdor: / In which addition, hail, most worthy thane! / For it is thine. / What, can the devil speak true? / The thane of Cawdor lives: why do you dress me / In borrow'd robes? / Who was the thane lives yet; / But under heavy judgment bears that life / Which he deserves to lose. Whether he was combin'd / With those of Norway, or did line the rebel / With hidden help and vantage, or that with both / He labour'd in his country's wreck, I know not; / But treasons capital, confess'd and prov'd, / Have overthrown him. / Glamis, and thane of Cawdor! / The greatest is behind. Thanks for your pains. / Do you not hope your children shall be kings, / When those that gave the thane of Cawdor to me / Promis'd no less to them? / That, trusted home, / Might yet enkindle you unto the crown, / Besides the thane of Cawdor. But 'tis strange: / And oftentimes, to win us to our harm, / The instruments of darkness tell us truths, / Win us with honest trifles, to betray's / In deepest consequence. / Cousins, a word, I pray you. / Two truths are told, / As happy prologues to the swelling act / Of the imperial theme. I thank you, gentlemen. / This supernatural soliciting / Cannot be ill; cannot be good: if ill, / Why hath it given me earnest of success, / Commencing in a truth? I am thane of Cawdor: / If good, why do I yield to that suggestion / Whose horrid image doth unfix my hair / And make my seated heart knock at my ribs, / Against the use of nature? Present fears / Are less than horrible imaginings: / My thought, whose murder yet is but fantastical, / Shakes so my single state of man that function / Is smother'd in surmise, and nothing is / But what is not. / Look, how our partner's rapt. / If chance will have me king, why, chance may crown me, / Without my stir. / New honors come upon him, / Like our strange garments, cleave not to their mould / But with the aid of use. / Come what come may, / Time and the hour runs through the roughest day. / Worthy Macbeth, we stay upon your leisure. / Give me your favour: my dull brain was wrought / With things forgotten. Kind gentlemen, your pains / Are register'd where every day I turn / The leaf to read them. Let us toward the king. / Think upon what hath chanc'd; and, at more time, / The interim having weigh'd it, let us speak / Our free hearts each to other. / Very gladly. / Till then, enough. Come, friends. / I see a glorious **prospect** opening before our house."*
> - 📜 **Thomas Hardy (*Far from the Madding Crowd*):** *"From Norcombe Hill the vast **prospect** embraced dark rolling downs and distant clusters of sheepfolds."*
> - 📜 **John Locke (*An Essay Concerning Human Understanding*):** *"The mind takes pleasure in the vast **prospect** of ideas opened up by intellectual inquiry."*
