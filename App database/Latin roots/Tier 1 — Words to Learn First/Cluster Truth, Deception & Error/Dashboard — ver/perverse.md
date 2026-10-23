---
latin_root: "[[Dashboard — ver]]"
cluster: "[[Cluster Truth, Deception & Error]]"
status: unread
tier: 2
tier_label: "Words to learn a little later"
zipf: 2.3
rank: 15790
---
# perverse

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
> 1. **Primary Definition (Lexical / Standard Consensus)**: Showing a deliberate and obstinate determination to behave in an unreasonable, contrary, or unacceptable manner.
> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: Morally corrupt, warped, or deviating from what is natural, good, or right.

> [!quote] 💬 Contextual Usage & Authentic Quotations
> - 📜 **William Shakespeare (*Romeo and Juliet*):** *"In truth, fair Montague, I am too fond, And therefore thou mayst think my ’haviour light: But trust me, gentleman, I’ll prove more true Than those that have more cunning to be strange. I should have been more strange, I must confess, But that thou overheard’st, ere I was ware, My true-love’s passion: therefore pardon me, And not impute this yielding to light love, Which the dark night hath so discovered. Lady, by yonder blessed moon I vow, That tips with silver all these fruit-tree tops— O! swear not by the moon, the inconstant moon, That monthly changes in her circled orb, Lest that thy love prove likewise variable. What shall I swear by? Do not swear at all; Or, if thou wilt, swear by thy gracious self, Which is the god of my idolatry, And I’ll believe thee. If my heart’s dear love— Well, do not swear. Although I joy in thee, I have no joy of this contract to-night: It is too rash, too unadvis’d, too sudden; Too like the lightning, which doth cease to be Ere one can say it lightens. Sweet, good night! This bud of love, by summer’s ripening breath, May prove a beauteous flower when next we meet. Good night, good night! as sweet repose and rest Come to thy heart as that within my breast! O! wilt thou leave me so unsatisfied? What satisfaction canst thou have to-night? The exchange of thy love’s faithful vow for mine. I gave thee mine before thou didst request it; And yet I would it were to give again. Wouldst thou withdraw it? for what purpose, love? But to be frank, and give it thee again. And yet I wish but for the thing I have: My bounty is as boundless as the sea, My love as deep; the more I give to thee, The more I have, for both are infinite. I hear some noise within; dear love, adieu! Anon, good nurse! Sweet Montague, be true. Stay but a little, I will come again. O blessed, blessed night! I am afeard, Being in night, all this is but a dream, Too flattering-sweet to be substantial. Three words, dear Romeo, and good night indeed. If that thy bent of love be honourable, Thy purpose marriage, send me word to-morrow, By one that I’ll procure to come to thee, Where, and what time, thou wilt perform the rite; And all my fortunes at thy foot I’ll lay, And follow thee my lord throughout the world. Madam! I come, anon.—But if thou mean’st not well, I do beseech thee— Madam! By and by, I come:— To cease thy suit, and leave me to my grief: To-morrow will I send. So thrive my soul,— A thousand times good night! A thousand times the worse, to want thy light. Love goes toward love, as schoolboys from their books, But love from love, toward school with heavy looks. Hist! Romeo, hist!—O, for a falconer’s voice, To lure this tassel-gentle back again! Bondage is hoarse, and may not speak aloud; Else would I tear the cave where Echo lies, And make her airy tongue more hoarse than mine, With repetition of my Romeo’s name. It is my soul that calls upon my name: How silver-sweet sound lovers’ tongues by night, Like softest music to attending ears! Romeo! My dear? At what o’clock to-morrow Shall I send to thee? At the hour of nine. I will not fail: ’tis twenty years till then. I have forgot why I did call thee back. Let me stand here till thou remember it. I shall forget, to have thee still stand there, Remembering how I love thy company. And I’ll still stay, to have thee still forget, Forgetting any other home but this. ’Tis almost morning; I would have thee gone: And yet no further than a wanton’s bird, Who lets it hop a little from her hand, Like a poor prisoner in his twisted gyves, And with a silk thread plucks it back again, So loving-jealous of his liberty. I would I were thy bird. Sweet, so would I: Yet I should kill thee with much cherishing. Good night, good night! parting is such sweet sorrow That I shall say good night till it be morrow. Sleep dwell upon thine eyes, peace in thy breast! Would I were sleep and peace, so sweet to rest! Hence will I to my ghostly father’s cell, His help to crave, and my dear hap to tell. I'll frown and be **perverse** and say thee nay, So thou wilt woo; but else, not for the world."*
> - 📜 **John Milton (*Paradise Lost*):** *"O miserable mankind, to what fall Degraded, to what dire excursions led! Does reason fail thee, or thy own **perverse** will betray thee?"*
> - 📜 **Edgar Allan Poe (*The Imp of the Perverse*):** *"There is a radical, primitive, irreducible impulse in the human heart that prompts us to do wrong simply because we should not; this is the **perverse** spirit."*
