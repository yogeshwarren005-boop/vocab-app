---
latin_root: "[[Dashboard — pos]]"
cluster: "[[Cluster Placing]]"
status: unread
tier: 1
tier_label: "Words to learn first"
zipf: 4
rank: 5416
---

# suppose

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
> 1. **Primary Definition (Lexical / Consensus)**: To assume or think that something is true, likely, or probable without certain proof.
> 2. **Secondary / Nuanced Definition (Contextual / Classical)**: To require as a necessary condition or prerequisite in logic or causation.

> [!quote] 💬 Contextual Usage & Authentic Quotations
> - 📜 **Jane Austen (*Pride and Prejudice*):** *"I **suppose** you will not deny that Mr. Darcy has great qualities of mind and fortune."*
> - 📜 **William Shakespeare (*The Tempest*):** *"Miranda cried out: What is't? a spirit? Lord, how it looks about! Believe me, sir, it carries a brave form. But 'tis a spirit. Prospero: No, wench; it eats and sleeps and hath such senses as we have, such. This gallant which thou seest was in the wreck; and, but he's something stain'd with grief that's beauty's canker, thou mightst call him a goodly person: he hath lost his fellows and strays about to find 'em. Miranda: I might call him a thing divine, for nothing natural I ever saw so noble. Prospero: It goes on, I see, as my soul prompts it. Spirit, fine spirit! I'll free thee within two days for this. Ferdinand: Most sure, the goddess on whom these airs attend! Vouchsafe my prayer may know if you remain upon this island; and that you will some good instruction give how I may bear me here: my prime request, which I do last pronounce, is, O you wonder! If you be maid or no? Miranda: No wonder, sir; but certainly a maid. Ferdinand: My language! heavens! I am the best of them that speak this speech, were I but where 'tis spoken. Prospero: How? the best? What wert thou, if the King of Naples heard thee? Ferdinand: A single thing, as I am now, that wonders to hear thee speak of Naples. He does hear me; and that he does I weep: myself am Naples, who with mine eyes, never since at ebb, beheld the king my father wreck'd. Miranda: Alack, for mercy! Ferdinand: Yes, faith, and all his lords; the Duke of Milan and his brave son being twain. Prospero: The Duke of Milan and his more braver daughter could control thee, if now 'twere fit to do't. At the first sight they have changed eyes. Delicate Ariel, I'll set thee free for this. A word, good sir; I fear you have done yourself some wrong: a word. Miranda: Why speaks my father so ungently? This is the third man that e'er I saw, the first that e'er I sigh'd for: pity move my father to be inclined my way! Ferdinand: O, if a virgin, and your affection not gone forth, I'll make you the queen of Naples. Prospero: Soft, sir! one word more. They are both in either's powers; but this swift business I must uneasy make, lest too light winning make the prize light. One word more; I charge thee that thou attend me: thou dost here usurp the name thou owest not; and hast put thyself upon this island as a spy, to win it from me, the lord on't. Ferdinand: No, as I am a man. Miranda: There's nothing ill can dwell in such a temple: if the ill spirit have so fair a house, good things will strive to dwell with't. Prospero: Follow me. Speak not you for him; he's a traitor. Come; I'll manacle thy neck and feet together: sea-water shalt thou drink; thy food shall be the fresh-brook mussels, wither'd roots and husks wherein the acorn cradled. Follow. Ferdinand: No; I will resist such entertainment till mine enemy has more power. Miranda: O dear father, make not too rash a trial of him, for he's gentle and not fearful. Prospero: What! I say, my foot my tutor? Put thy sword up, traitor; who makest a show but darest not strike, thy conscience is so possess'd with guilt: come from thy ward, for I can here disarm thee with this stick and make thy weapon drop. Miranda: Beseech you, father. Prospero: Hence! hang not on my garments. Miranda: Sir, have pity; I'll be his surety. Prospero: Silence! one word more shall make me chide thee, if not hate thee. What! an advocate for an impostor! hush! thou think'st there is no more such shapes as he, having seen but him and Caliban: foolish wench! to the most of men this is a Caliban and they to him are angels. Miranda: My affections are then most humble; I have no ambition to see a goodlier man. Prospero: Come on; obey: thy nerves are in their infancy again and have no vigour in them. Ferdinand: So they are; my spirits, as in a dream, are all bound up. My father's loss, the weakness which I feel, the wreck of all my friends, nor this man's threats, to whom I am subdued, are but light to me, might I but through my prison once a day behold this maid: all corners else o' the earth let liberty make use of; space enough have I in such a prison. Prospero: It works. Come on. Thou hast done well, fine Ariel! Follow me. Hark what thou else shalt do me. Miranda: Be of comfort; my father is of a better nature, sir, than he appears by speech; this is unwonted which now came from him. Prospero: Thou shalt be free as mountain winds: but then exactly do all points of my command. Ariel: To the syllable. Prospero: Come, follow. Speak not for him. And do not **suppose** my justice is unjust."*
> - 📜 **Charles Darwin (*The Origin of Species*):** *"Let us **suppose** a series of islands populated by a few continental migrants undergoing adaptive isolation."*
