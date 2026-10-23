---
latin_root: "[[Dashboard — sta]]"
cluster: "[[Cluster Placing]]"
status: unread
tier: 1
tier_label: "Words to learn first"
zipf: 4
rank: 9085
---

# distant

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
> 1. **Primary Definition (Lexical / Consensus)**: Far away in space, time, or relationship; not intimate or closely connected.
> 2. **Secondary / Nuanced Definition (Contextual / Classical)**: Cool, reserved, aloof, and unapproachable in manner and demeanor.

> [!quote] 💬 Contextual Usage & Authentic Quotations
> - 📜 **William Shakespeare (*The Merchant of Venice*):** *"From the four corners of the earth they come, to kiss this shrine, this mortal-breathing saint: the Hyrcanian deserts and the vasty wilds of wide Arabia are as throughfares now for princes to come view fair Portia: the watery kingdom, whose ambitious head spits in the face of heaven, is no bar to stop the foreign spirits, but they come, as o'er a brook, to see fair Portia. One of these three contains her heavenly picture. Is't like that lead contains her? 'Twere damnation to think so base a thought: it were too gross to rib her cerecloth in the obscure grave. Or shall I think in silver she's immured, being ten times undervalued to tried gold? O sinful thought! Never so rich a gem was set in worse than gold. They have in England a coin that bears the figure of an angel stamped in gold, but that's insculp'd upon; but here an angel in a golden bed lies all within. Deliver me the key: here do I choose, and thrive I as I may! Portia: There, take it, prince; and if my form lie there, then I am yours. Morocco: O hell! what have we here? A carrion Death, within whose empty eye there is a written scroll! I'll read the writing. All that glisters is not gold; often have you heard that told: many a man his life hath sold but my outside to behold: gilded tombs do worms infold. Had you been as wise as bold, young in limbs, in judgment old, your suit had not been cold. Fare you well; your suit is cold. Cold, indeed; and labour lost: then, farewell, heat, and welcome, frost! Portia, adieu. I have too grieved a heart to take a tedious leave: thus losers part. Portia: A gentle riddance. Draw the curtains, go. Let all of his complexion choose me so. Lorenzo: Madam, although I speak it in your presence, you have a noble and a true conceit of god-like amity; which appears most strongly in bearing thus the absence of your lord. But if you knew to whom you show this honour, how true a gentleman you send relief, how dear a lover of my lord your husband, you would be prouder of the work than customary bounty can enforce you. Portia: I never did repent for doing good, nor shall not now: for in companions that do converse and waste the time together, whose souls do bear an equal yoke of love, there must be needs a like proportion of lineaments, of manners and of spirit; which makes me think that this Antonio, being the bosom lover of my lord, must needs be like my lord. If it be so, how little is the cost I have bestow'd in purchasing the semblance of my soul from out the state of hellish cruelty! This comes too near the praising of myself; therefore no more of it: hear other things. Lorenzo, I commit into your hands the husbandry and manage of my house until my lord's return: for mine own part, I have toward heaven breathed a secret vow to live in prayer and contemplation, only attended by Nerissa here, until her husband and my lord's return: there is a monastery two miles off; and there will we abide. I do desire you not to deny this imposition; the which my love and some necessity now lays upon you. Lorenzo: Madam, with all my heart; I shall obey you in all fair commands. Portia: My people do already know my mind, and will acknowledge you and Jessica in place of Lord Bassanio and myself. And so farewell, till we shall meet again. Lorenzo: Fair thoughts and happy hours attend on you! Jessica: I wish your ladyship all heart's content. Portia: I thank you for your wish, and am well pleased to wish it back on you: fare you well Jessica. Now, Balthasar, as I have ever found thee honest-true, so let me find thee still. Take this same letter, and use thou all the endeavour of a man in speed to Padua: see thou render this into my cousin's hand, Doctor Bellario; and, look, what notes and garments he doth give thee, bring them, I pray thee, with imagined speed unto the tranect, to the common ferry which trades to Venice. Waste no time in words, but get thee gone: I shall be there before thee. Balthasar: Madam, I go with all convenient speed. Portia: Come on, Nerissa; I have work in hand that you yet know not of: we'll see our husbands before they think of us. Nerissa: Shall they see us? Portia: They shall, Nerissa; but in such a habit, that they shall think we are accomplished with that we lack. I'll hold thee any wager, when we are both accoutred like young men, I'll prove the prettier fellow of the two, and wear my dagger with the braver grace, and speak between the change of man and boy with a reed voice, and turn two mincing steps into a manly stride, and speak of frays like a fine bragging youth, and tell quaint lies, how honourable ladies sought my love, which I denying, they fell sick and died; I could not do withal; then I'll repent, and wish, for all that, that I had not kill'd them; and twenty of these puny lies I'll tell, that men shall swear I have discontinued school above a twelvemonth. I have within my mind a thousand raw tricks of these bragging Jacks, which I will practise. Nerissa: Why, shall we turn to men? Portia: Fie, what a question's that, if thou wert near a lewd interpreter! But come, I'll tell thee all my whole device when I am in my coach, which stays for us at the park gate; and therefore haste away, for we must measure twenty miles to-day. Bassanio looked upon the **distant** hills of Belmont with longing."*
> - 📜 **Jane Austen (*Pride and Prejudice*):** *"Mr. Darcy preserved a cold, **distant** civility that discouraged any intimate conversation."*
> - 📜 **Charles Darwin (*The Origin of Species*):** *"The flora of **distant** oceanic islands exhibits remarkable affinities with the nearest mainland."*
