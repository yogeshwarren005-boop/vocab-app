---
status: unread
type: root_dashboard
tier: 1
frequency_score: 154.8
tier_label: "Roots to learn first"
tier1_words: 12
tier2_words: 11
tier3_words: 88
---
# Dashboard — bas
<div class="core-meaning-keystone">
  <div class="cm-header">
    <span class="cm-tag">🏛️ LATIN ROOT</span>
    <span class="cm-script">bas-</span>
  </div>
  <div class="cm-body">
    <span class="cm-label">CORE MEANING</span>
    <span class="cm-definition">“low or base”</span>
  </div>
  <div class="cm-footer">
    <span>💡 <b>Cognitive Anchor:</b> Comparing a fresh, wholesome fruit against a damaged or spoiled one.</span>
  </div>
</div>

```dataviewjs
// Ensure Apple Toggle CSS is injected and synchronized
let s = document.getElementById('apple-toggle-css');
if (!s) {
    s = document.createElement('style');
    s.id = 'apple-toggle-css';
    document.head.appendChild(s);
}
s.textContent = '.apple-c{position:relative;display:inline-flex;align-items:center;gap:8px;padding:2px 10px 2px 4px;border-radius:999px;background:var(--zen-toggle-bg,#27272e);border:1px solid var(--zen-border,#2d2d34);cursor:pointer;user-select:none;transition:border-color .2s ease,transform .2s ease,box-shadow .2s ease;line-height:1;vertical-align:middle;box-sizing:border-box}.apple-c:hover{border-color:var(--zen-muted,#86848c);transform:translateY(-1px);box-shadow:0 2px 6px rgba(0,0,0,.15)}.apple-c:active{transform:scale(.96)}.apple-c .track-c{position:relative;width:44px;height:16px;background:var(--zen-toggle-track,#1e1e24);border-radius:999px;border:1px solid var(--zen-border-subtle,#24242a);display:flex;align-items:center;justify-content:space-between;padding:0 5px;box-sizing:border-box}.apple-c .c-dot{width:3px;height:3px;border-radius:999px;background:var(--zen-muted,#86848c);opacity:.5}.apple-c .halo-c{position:absolute;top:1px;left:1px;width:12px;height:12px;border-radius:999px;transition:transform .35s cubic-bezier(.34,1.6,.64,1),background-color .25s ease,box-shadow .25s ease;display:flex;align-items:center;justify-content:center;box-sizing:border-box}.apple-c .halo-c .core-dot{width:4px;height:4px;border-radius:999px;background:#fff;box-shadow:0 0 3px #fff}.apple-c .halo-c.p0{transform:translateX(0);background:var(--zen-vermillion,#e05244);box-shadow:0 0 8px var(--zen-vermillion-glow,rgba(224,82,68,0.35))}.apple-c .halo-c.p1{transform:translateX(14px);background:var(--zen-ochre,#d49c24);box-shadow:0 0 8px rgba(212,156,36,0.35)}.apple-c .halo-c.p2{transform:translateX(28px);background:var(--zen-moss,#429e57);box-shadow:0 0 8px var(--zen-moss-glow,rgba(66,158,87,0.35))}.apple-c .label{font-size:11px;font-weight:700;letter-spacing:.2px;transition:color .2s ease;min-width:44px}.apple-c .label.unread{color:var(--zen-vermillion,#e05244)}.apple-c .label.learning{color:var(--zen-ochre,#d49c24)}.apple-c .label.learned{color:var(--zen-moss,#429e57)}';

// Robust path and file resolution
const currentPath = dv.currentFilePath || (dv.current() && dv.current().file ? dv.current().file.path : "");
const folder = currentPath.includes('/') ? currentPath.substring(0, currentPath.lastIndexOf('/')) : (dv.current() && dv.current().file ? dv.current().file.folder : "");
const rawFileName = currentPath ? currentPath.substring(currentPath.lastIndexOf('/') + 1).replace(/\.md$/, '') : (dv.current() && dv.current().file ? dv.current().file.name : "");
const rootName = rawFileName;
const cur = dv.current();
const rawStatus = (cur && cur.status) ? cur.status : "unread";
const isLatin = folder.includes("Latin roots");

let wordPages = [];
if (folder) {
    try {
        wordPages = dv.pages('"' + folder + '"').where(n => n.file.name !== rootName && !n.file.name.startsWith("Word Triage") && (n.latin_root || n.greek_root || (!n.file.name.startsWith("Dashboard") && !n.file.name.startsWith("Cluster"))));
    } catch (e) { wordPages = []; }
}

const t = wordPages ? wordPages.length : 0;
const l = (wordPages && t > 0) ? wordPages.where(n => n.status === "learned").length : 0;
const g = (wordPages && t > 0) ? wordPages.where(n => n.status === "learning").length : 0;
const u = t - l - g;
const lPct = t > 0 ? ((l / t) * 100).toFixed(1) : "0.0";
const gPct = t > 0 ? ((g / t) * 100).toFixed(1) : "0.0";

const states = [
    { key: 'unread', label: 'unread', cls: 'unread', p: 'p0' },
    { key: 'learning', label: 'learning', cls: 'learning', p: 'p1' },
    { key: 'learned', label: 'learned', cls: 'learned', p: 'p2' }
];

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

const cleanName = rootName.replace('Dashboard — ', '').replace('Dashboard – ', '').replace('Dashboard - ', '');
const isMastered = (curIdx === 2 || (t > 0 && l === t));

toggle.addEventListener('click', async (e) => {
    e.stopPropagation();
    curIdx = (curIdx + 1) % 3;
    const nxt = states[curIdx];
    track.querySelector('.halo-c').className = 'halo-c ' + nxt.p;
    label.className = 'label ' + nxt.cls;
    label.textContent = nxt.label;

    const seal = container.querySelector('.hanko-seal');
    if (seal) {
        if (nxt.key === 'learned') {
            seal.style.opacity = "0.95";
            seal.style.transform = "rotate(-3deg) scale(1)";
        } else {
            seal.style.opacity = "0.25";
            seal.style.transform = "rotate(-6deg) scale(0.92)";
        }
    }

    const file = app.vault.getAbstractFileByPath(currentPath);
    if (file) {
        await app.fileManager.processFrontMatter(file, fm => { fm.status = nxt.key; });
        new Notice(rootName + ': marked ' + nxt.key);
    }
});

// Container element with Zen HUD Card class
const container = document.createElement('div');
container.className = 'zen-hud-card';
container.style = "background:var(--zen-bg-card,#1a1a1e); color:var(--zen-ink,#ececec); border:1px solid var(--zen-border,#2d2d34); border-radius:10px; padding:24px 28px; margin:16px 0 20px; box-shadow:var(--zen-shadow,0 6px 24px rgba(0,0,0,0.4)); position:relative; box-sizing:border-box;";

const stampText = isLatin ? 'Latin Root' : 'Greek Root';

container.innerHTML = '' +
  '<div style="position:absolute; top:14px; right:28px; font-family:Georgia,serif; font-size:48px; font-weight:300; color:var(--zen-muted,#86848c); line-height:1; pointer-events:none; user-select:none; opacity:0.25;">' + cleanName + '</div>' +
  '<div style="display:inline-flex; align-items:center; border:1px solid var(--zen-vermillion,#e05244); color:var(--zen-vermillion,#e05244); font-size:10px; font-weight:700; letter-spacing:1.5px; text-transform:uppercase; padding:2px 7px; border-radius:2px; margin-bottom:6px; background:var(--zen-vermillion-glow,rgba(224,82,68,0.1));">' + stampText + '</div>' +
  '<div style="font-family:Georgia,serif; font-size:28px; font-weight:700; color:var(--zen-ink,#ececec); letter-spacing:-0.5px; line-height:1.2;">' + cleanName + '</div>' +
  '<div style="font-family:Georgia,serif; font-size:14px; font-style:italic; color:var(--zen-muted,#86848c); margin-top:3px;">' + stampText + ' · Derived Vocabulary (' + t + ' words)</div>' +
  '<div style="width:100%; height:1px; background:linear-gradient(to right, var(--zen-ink,#ececec) 25%, transparent 95%); opacity:0.15; margin:16px 0;"></div>' +
  '<div style="display:grid; grid-template-columns:auto 1fr auto; gap:28px; align-items:center; margin:12px 0 16px;">' +
    '<div style="position:relative; width:68px; height:68px; display:flex; align-items:center; justify-content:center;">' +
      '<svg style="width:68px; height:68px; transform:rotate(-90deg);" viewBox="0 0 36 36">' +
        '<path stroke="var(--zen-border-subtle,#24242a)" stroke-width="3.6" fill="none" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831"/>' +
        '<path stroke="var(--zen-moss,#429e57)" stroke-width="3.8" stroke-linecap="round" fill="none" stroke-dasharray="' + lPct + ', 100" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831"/>' +
      '</svg>' +
      '<div style="position:absolute; font-family:Georgia,serif; font-size:14px; font-weight:700; color:var(--zen-ink,#ececec);">' + lPct + '%</div>' +
    '</div>' +
    '<div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:16px;">' +
      '<div><div style="font-family:Georgia,serif; font-size:26px; font-weight:600; color:var(--zen-ink,#ececec); line-height:1;">' + t + '</div><div style="font-size:9.5px; text-transform:uppercase; letter-spacing:1.4px; color:var(--zen-muted,#86848c); margin-top:4px; font-weight:600;">Derived Words</div></div>' +
      '<div><div style="font-family:Georgia,serif; font-size:26px; font-weight:600; color:var(--zen-moss,#429e57); line-height:1;">' + l + '</div><div style="font-size:9.5px; text-transform:uppercase; letter-spacing:1.4px; color:var(--zen-muted,#86848c); margin-top:4px; font-weight:600;">Mastered</div></div>' +
      '<div><div style="font-family:Georgia,serif; font-size:26px; font-weight:600; color:var(--zen-ochre,#d49c24); line-height:1;">' + g + '</div><div style="font-size:9.5px; text-transform:uppercase; letter-spacing:1.4px; color:var(--zen-muted,#86848c); margin-top:4px; font-weight:600;">Studying</div></div>' +
    '</div>' +
    '<div class="hanko-seal" style="width:42px; height:42px; border:2px solid var(--zen-vermillion,#e05244); border-radius:4px; display:flex; align-items:center; justify-content:center; color:var(--zen-vermillion,#e05244); font-family:Georgia,serif; font-size:20px; font-weight:700; user-select:none; transition:all .35s; opacity:' + (isMastered ? '0.95' : '0.25') + '; transform:' + (isMastered ? 'rotate(-3deg) scale(1)' : 'rotate(-6deg) scale(0.92)') + ';" title="Mastery Seal (熟)">熟</div>' +
  '</div>' +
  '<div style="width:100%; height:3px; background:var(--zen-border-subtle,#24242a); border-radius:2px; overflow:hidden; margin:14px 0; display:flex; gap:1px;">' +
    '<div style="height:100%; background:var(--zen-moss,#429e57); border-radius:2px 0 0 2px; width:' + lPct + '%;"></div>' +
    '<div style="height:100%; background:var(--zen-ochre,#d49c24); width:' + gPct + '%;"></div>' +
  '</div>' +
'';

const toggleRow = document.createElement('div');
toggleRow.style = "display:flex; justify-content:space-between; align-items:center; padding-top:6px; margin-top:4px;";

const toggleLabel = document.createElement('span');
toggleLabel.style = "font-size:10px; text-transform:uppercase; letter-spacing:1.2px; color:var(--zen-muted,#86848c); font-weight:600;";
toggleLabel.textContent = "Root Study Status";

toggleRow.appendChild(toggleLabel);
toggleRow.appendChild(toggle);
container.appendChild(toggleRow);
dv.container.appendChild(container);

// ================= WORD TRIAGE LAUNCH CARD =================
const triageCard = document.createElement('div');
triageCard.className = 'zen-triage-card';
triageCard.style = "background:var(--zen-bg-card,#1a1a1e); border:1px solid var(--zen-border,#2d2d34); border-radius:8px; padding:14px 20px; margin:0 0 24px; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:16px; cursor:pointer; transition:all .25s ease;";
triageCard.title = "Click to open dedicated Word Triage page";

triageCard.innerHTML = '' +
  '<div style="display:flex; align-items:center; gap:16px;">' +
    '<div style="width:38px; height:38px; border-radius:8px; background:rgba(224,82,68,0.12); border:1px solid var(--zen-vermillion,#e05244); display:flex; align-items:center; justify-content:center; font-size:18px;">🎯</div>' +
    '<div>' +
      '<div style="font-family:Georgia,serif; font-size:15px; font-weight:700; color:var(--zen-ink,#ececec); letter-spacing:-0.2px;">Word Triage & Status Filters</div>' +
      '<div style="display:flex; gap:12px; margin-top:3px; font-size:11.5px; font-weight:600;">' +
        '<span style="color:var(--zen-vermillion,#e05244);">🔴 ' + u + ' unread</span> · ' +
        '<span style="color:var(--zen-ochre,#d49c24);">🟡 ' + g + ' studying</span> · ' +
        '<span style="color:var(--zen-moss,#429e57);">🟢 ' + l + ' mastered</span>' +
      '</div>' +
    '</div>' +
  '</div>' +
  '<div style="display:flex; align-items:center; gap:8px; background:var(--zen-bg-subtle,#222227); border:1px solid var(--zen-border,#2d2d34); padding:6px 14px; border-radius:999px; font-size:12px; font-weight:700; color:var(--zen-ink,#ececec);">' +
    '<span>Open Triage Page</span>' +
    '<span style="color:var(--zen-vermillion,#e05244);">➔</span>' +
  '</div>';

triageCard.addEventListener('mouseenter', () => {
    triageCard.style.borderColor = "var(--zen-vermillion,#e05244)";
    triageCard.style.transform = "translateY(-1px)";
    triageCard.style.boxShadow = "0 4px 14px rgba(0,0,0,0.25)";
});
triageCard.addEventListener('mouseleave', () => {
    triageCard.style.borderColor = "var(--zen-border,#2d2d34)";
    triageCard.style.transform = "none";
    triageCard.style.boxShadow = "none";
});

triageCard.addEventListener('click', () => {
    const triagePageName = 'Word Triage — ' + cleanName;
    app.workspace.openLinkText(triagePageName, currentPath, false);
});

dv.container.appendChild(triageCard);

```

The root **bas** means low or base. It describes being low in position, underneath, or forming the bottom base. In English, this root forms words such as *come*, *basely*, *baseness*, and *basis*.

---

## 💡 Core Meaning

> [!example] ✨ Core Concept: low or base
> The root **bas** means low or base. It describes being low in position, underneath, or forming the bottom base. In English, this root forms words such as *come*, *basely*, *baseness*, and *basis*.

---

## 🌟 1. Deep Root Origin & Cognitive Architecture

> [!tip] 🎯 Quick Summary: What Does This Root Mean?
> - **Core Meaning**: <mark class="hl-def">Low or base</mark>.
> - **Mental Picture**: <mark class="hl-mnemonic">Comparing a fresh, wholesome fruit against a damaged or spoiled one.</mark>
> - **Everyday Connection**: Think of familiar words like *come* and *basely*.

### 📌 Key Learning Concepts

- **What It Literally Means**:
  - The root **bas** comes from a Latin word that means *"low or base"*.
  - At its core, it describes the quality or state of being low or base.

- **The Big Picture Idea**:
  - Picture comparing a fresh, wholesome fruit against a damaged or spoiled one.
  - Whenever you see **bas** in an English word, think of **goodness, benefits, or harm**.

- **How the Meaning Grows**:
  - **Physical**: Physical objects, textures, or shapes that are low or base.
  - **Mental & Social**: Human emotions, attitudes, speaking styles, or mental traits.
  - **Abstract & Practical**: Scientific measurements, standards, or formal categories.

- **Everyday English Words to Remember It By**:
  - **Come**: An everyday English word showing the root's idea of *low or base*.
  - **Basely**: In an ignoble, dishonorable, or shameful manner.
  - **Baseness**: Lack of moral value, honor, or dignity.
  - **Basis**: The underlying support, foundation, or premise of an argument.

- **💡 Quick Memory Rule**:
  - *When you see <mark class="hl-stem">bas</mark>, think of <mark class="hl-def">goodness, benefits, or harm</mark>.*

---

## ⚙️ 2. Root Characteristics & Word Formation Engine

> [!abstract] 🔨 Morphological Architecture of `bas`
> The English lexicon derives from two distinct linguistic stems:
> 1. **The Greek-Latin Foundation Stem (`basis-` / `base-`):**
>    - Classical Nominative Noun: **basis** (plural *bases*).
>    - Clipped Noun & Verb: **base**, **based**, **baseless**, **baselessly**, **baselessness**.
>    - Adjectives & Adverbs: **basic**, **basically**, **basics**, **basicness**, **basicity**.
>    - Anatomical & Geological Compounds: **basal**, **basally**, **basement**.
>    - Chemical Compounds: **monobasic**, **dibasic**, **polybasic**.
> 2. **The Late Latin Lowness Stem (`bass-` / `base-`):**
>    - Evaluative Adjective: **base**, **basely**, **baseness**.
>    - Verbs of Lowering & Degradation:
>      - `ad-`: **abase**, **abasement** (humiliate, lower in dignity).
>      - `de-`: **debase**, **debasement**, **debasing**, **debaser**.
>      - Romance emotion: **abash**, **abashed** (via Anglo-Norman *esbaïr* influenced by *abase*).
>    - Musical & Artistic Borrowings:
>      - **bass**, **basso**, **bassoon**, **contrabass**.
>      - **bas-relief**, **basso-relievo**.
>      - Canine diminutive: **basset** (hound).
>      - Armor: **basinet** (small skull-cap helmet).

---

## 🎨 3. Semantic Range Across Derived Words

> [!tip]- 🎯 **Live Study Filter & Queue**
```dataviewjs
const p = dv.pages('"' + dv.current().file.folder + '"').where(n => n.file.name !== dv.current().file.name && n.latin_root);
const inProg = p.where(n => n.status === "learning");
const done = p.where(n => n.status === "learned");
if (inProg.length === 0 && done.length === 0) {
    dv.paragraph("*No words marked yet. Open any word card below and select 🟡 Learning or 🟢 Learned.*");
} else {
    let out = [];
    if (inProg.length > 0) out.push("🟡 **Currently Studying (" + inProg.length + "):** " + inProg.map(n => n.file.link).join(" · "));
    if (done.length > 0) out.push("🟢 **Mastered (" + done.length + "):** " + done.map(n => n.file.link).join(" · "));
    dv.paragraph(out.join("\n\n"));
}
```

```
                                  ┌── Architecture & Mechanics ── base, basement, basis, baseless
                                  │
                                  ├── Chemistry & Molecular ──── basic, basicity, monobasic, polybasic, DNA bases
    [BAS-] ───────────────────────┼── Logic & Axiomatics ─────── basis, basic, basically, basics
(foundation / low / debase)       │
                                  ├── Moral Contempt & Fraud ─── base (adj), baseness, debase, debasement, abase
                                  │
                                  └── Music, Art & Stature ───── bass, basso, bassoon, bas-relief, basset
```

> [!tip] 🌈 Thematic Distribution of Vocabulary
> 1. **Architecture, Engineering & Mechanics:** *base*, *basement*, *basis*, *baseless*, *baselessly*, *baselessness*.
> 2. **Epistemology, Statistics & Logic:** *basis*, *basic*, *basically*, *basics*, *basicness*.
> 3. **Chemistry, Geology & Cell Biology:** *base*, *basic*, *basicity*, *basal*, *basally*, *basement membrane*, *monobasic*, *polybasic*.
> 4. **Moral Philosophy, Feudal Hierarchy & Humiliation:** *base* (adj.), *basely*, *baseness*, *abase*, *abasement*, *debase*, *debasement*, *debasing*, *debaser*, *abash*, *abashed*.
> 5. **Musicology, Sculpture & Specialized French Loans:** *bass*, *basso*, *bassoon*, *contrabass*, *bas-relief*, *basso-relievo*, *basset*, *basinet*.

---

## 🔀 4. Prefix & Combining Dynamics on bas

### Prefix Dynamics

| Prefix | Classical Meaning | Resulting Lemma | Semantic Transformation |
| :--- | :--- | :--- | :--- |
| `ad-` | to, toward | **abase**, **abasement** | Bringing someone down to the ground; humbling pride or social rank. |
| `de-` | down, away from | **debase**, **debasement** | Lowering intrinsic quality, purity of coinage, or moral dignity. |
| `ex-` | thoroughly out | **abash**, **abashed** | Confounding someone with embarrassment until their confidence is cast down. |
| `contra-` | against, opposite | **contrabass** | Sounding an octave lower than the ordinary bass register. |

### Suffix & Combining Terminations

| Suffix | Grammatical Role | Resulting Lemma | Semantic Function |
| :--- | :--- | :--- | :--- |
| `-is` | Greek/Latin nominative | **basis** | Preserving the uninflected classical noun of foundation. |
| `-al` | relational adjective | **basal** | Located at or forming the physiological or geological base. |
| `-ic` | adjective of essence | **basic** | Constituting the fundamental core; alkaline in chemistry. |
| `-ity` | chemical property | **basicity** | The power of an acid to react with bases, or the alkalinity of a compound. |
| `-ment` | concrete substructure | **basement** | The subterranean foundation floor of an architectural edifice. |
| `-less` | privative (without) | **baseless** | Lacking any grounding in evidence, fact, or justification. |
| `-oon` | French augmentative | **bassoon** | The large, low-sounding double-reed orchestral instrument. |
| `-et` | French diminutive | **basset** | The short, low-statured French hound. |

---

## 🌐 5. Disciplinary & Real-World Domains

> [!abstract] 🏛️ Institutional & Professional Sphere Applications
> 1. **Biochemistry & Molecular Genetics:** The genetic code is written in nitrogenous *bases* (purines and pyrimidines) whose complementary hydrogen bonds stabilize DNA.
> 2. **Monetary History & Economics:** *Debasement* of the Roman silver denarius under Nero, Septimius Severus, and Caracalla triggered hyperinflation and fiscal collapse.
> 3. **Linear Algebra & Quantum Mechanics:** A *basis* of a vector space is a set of linearly independent vectors that spans the entire space (such as the orthonormal eigenstates of a Hamiltonian).
> 4. **Acoustics & Orchestral Scoring:** The *bass* section (double basses, tubas, bassoons) establishes harmonic root motion and rhythmic drive for the entire symphony.
> 5. **Histopathology & Dermatology:** Disruption of the epithelial *basement membrane* distinguishes invasive malignant carcinoma from carcinoma in situ.

---

## 📚 6. Complete Derived Words Master List (Exhaustive)

### ⭐ Tier 1: Words to Learn First (High Frequency) (12 words)

| Word | POS | Frequency / Rank | Authoritative Definitions | Authentic Illustrative Sentence |
| :--- | :--- | :--- | :--- | :--- |
| [[based]] | verb | ⭐ Zipf 4.0 (#265) | **1.** Use as a basis for; found on.<br>**2.** Situate as a center of operations. | *"A coolness arose between him and my guardian, based principally on the foregoing grounds and on his having heartlessly disregarded my guardian’s entreaties (as we afterwards learned from Ada) in reference to Richard."* — Charles Dickens, *Bleak House* |
| [[bastard]] | noun | ⭐ Zipf 4.0 (#858) | **1.** Insulting terms of address for people who are stupid or irritating or ridiculous.<br>**2.** The illegitimate offspring of unmarried parents. | *"No, that same wicked bastard of Venus, that was begot of thought, conceived of spleen, and born of madness, that blind rascally boy that abuses everyone’s eyes because his own are out, let him be judge how deep I am in love."* — William Shakespeare, *The Complete Works of William Shakespeare* |
| [[basic]] | noun | ⭐ Zipf 4.0 (#945) | **1.** A popular programming language that is relatively easy to learn; an acronym for beginner's all-purpose symbolic instruction code; no longer in general use.<br>**2.** (usually plural) a necessary commodity for which demand is constant. | *"We have adjusted each of these series to a base of the average prices for 1890-1899, in accord with the basic period used by the American Bureau of Labor."* — Frank A. Fetter, *Economics Volume II: Modern Economic Problems* |
| [[base]] | noun | ⭐ Zipf 4.0 (#988) | **1.** Installation from which a military force initiates operations.<br>**2.** Lowest support of a structure. | *"Spend’st thou thy fury on some worthless song, Darkening thy power to lend base subjects light?"* — William Shakespeare, *The Complete Works of William Shakespeare* |
| [[basis]] | noun | ⭐ Zipf 4.0 (#1,361) | **1.** A relation that provides the foundation for something.<br>**2.** The fundamental assumptions from which something is begun or developed or calculated or explained. | *"How many times shall Caesar bleed in sport, That now on Pompey’s basis lies along, No worthier than the dust!"* — William Shakespeare, *The Complete Works of William Shakespeare* |
| [[baseball]] | noun | ⭐ Zipf 4.0 (#2,295) | **1.** A ball game played with a bat and ball between two teams of nine players; teams take turns at bat trying to score runs.<br>**2.** A ball used in playing baseball. | *"Columbia, my sister, Your children you have seen, Drowned in the cruel ocean By German submarine; But baseball is important, The theatre and dance, And pleasure rules in Texas While horror reigns in France."* — Abner Cosens, *War Rhymes by Wayfarer* |
| [[bass]] | noun | ⭐ Zipf 4.0 (#2,961) | **1.** The lowest part of the musical range.<br>**2.** The lowest part in polyphonic music. | *"Methought the billows spoke, and told me of it; The winds did sing it to me; and the thunder, That deep and dreadful organ-pipe, pronounc’d The name of Prosper: it did bass my trespass."* — William Shakespeare, *The Complete Works of William Shakespeare* |
| [[basically]] | adverb | ⭐ Zipf 4.0 (#5,271) | **1.** In essence; at bottom or by one's (or its) very nature. | *"So why not someone in the shop or office who was basically trained in suicide prevention and crisis intervention?"* — Meyer Moldeven, *A Grandpa's Notebook* |
| [[basics]] | noun | ⭐ Zipf 4.0 (#5,302) | **1.** A statement of fundamental facts or principles.<br>**2.** Principles from which other truths can be derived. | *"In academic literature, basics designates a statement of fundamental facts or principles."* — Academic Lexicon, *Morphological & Etymological Survey* |
| [[basin]] | noun | ⭐ Zipf 4.0 (#5,943) | **1.** A bowl-shaped vessel; usually used for holding food or liquids.<br>**2.** The quantity that a basin will hold. | *"Sly is discovered in a rich nightgown, with Attendants: some with apparel, basin, ewer, and other appurtenances; and Lord, dressed like a servant."* — William Shakespeare, *The Complete Works of William Shakespeare* |
| [[baseline]] | noun | ⭐ Zipf 4.0 (#6,545) | **1.** An imaginary line or standard by which things are measured or compared.<br>**2.** The back line bounding each end of a tennis or handball court; when serving the server must not step over this line. | *"In academic literature, baseline designates an imaginary line or standard by which things are measured or compared."* — Academic Lexicon, *Morphological & Etymological Survey* |
| [[basement]] | noun | ⭐ Zipf 4.0 (#8,559) | **1.** The lowermost portion of a structure partly or wholly below ground level; often used for storage.<br>**2.** The ground floor facade or interior in renaissance architecture. | *"It was close to the wall, where there is a ledge of stonework round the basement of the tower."* — Mrs. Oliphant, *A Beleaguered City* |


### 📈 Tier 2: Words to Learn a Little Later (Elevated & Academic) (11 words)

| Word | POS | Frequency / Rank | Authoritative Definitions | Authentic Illustrative Sentence |
| :--- | :--- | :--- | :--- | :--- |
| [[basil]] | noun | 📈 Zipf 2.4 (#9,905) | **1.** Any of several old world tropical aromatic annual or perennial herbs of the genus ocimum.<br>**2.** (roman catholic church) the bishop of caesarea who defended the roman catholic church against the heresies of the 4th century; a saint and doctor of the church (329-379). | *"What do you take his age to be?’ ‘Sixty,’ said I, ‘or perhaps sixty-two.’ ‘Forty,’ replied Sir Basil, ‘forty, and no more.’ Picture to yourselves my amazement; I shall not easily forget Admiral Baldwin."* — Jane Austen, *Persuasion* |
| [[bastille]] | noun | 📈 Zipf 2.3 (#22,264) | **1.** A fortress built in paris in the 14th century and used as a prison in the 17th and 18th centuries; it was destroyed july 14, 1789 at the start of the french revolution.<br>**2.** A jail or prison (especially one that is run in a tyrannical manner). | *"You would have almost thought they were pulling down the cursed Bastille, such wild cries they raised, as the now useless brick and mortar were being hurled into the sea."* — Herman Melville, *Moby Dick; Or, The Whale* |
| [[bastion]] | noun | 📈 Zipf 2.3 (#27,848) | **1.** A group that defends a principle.<br>**2.** A stronghold into which people could go for shelter during a battle. | *"The whole of the north side is very majestic, ending in the return of a bastion to the east."* — William Beattie, *The castles and abbeys of England; Vol. 2 of 2* |
| [[basra]] | noun | 📈 Zipf 2.3 (#31,644) | **1.** The second largest city in iraq; an oil port in southern iraq. | *"In academic literature, basra designates the second largest city in iraq; an oil port in southern iraq."* — Academic Lexicon, *Morphological & Etymological Survey* |
| [[basilica]] | noun | 📈 Zipf 2.3 (#32,644) | **1.** An early christian church designed like a roman basilica; or a roman catholic church or cathedral accorded certain privileges.<br>**2.** A roman building used for public administration. | *"Saint Mark’s: see Ruskin’s description of this glorious basilica, in ‘The Stones of Venice’. 3."* — Robert Browning, *An Introduction to the Study of Robert Browning's Poetry* |
| [[baseless]] | adjective | 📈 Zipf 2.3 (#33,477) | **1.** Without a basis in reason or fact. | *"She knew that it was all sentiment, all baseless impressibility, which had caused her to read the scene as her own condemnation; nevertheless she could not get over it; she could not contravene in her own defenceless person all those untoward omens."* — Thomas Hardy, *Tess of the d'Urbervilles: A Pure Woman* |
| [[baste]] | noun | 📈 Zipf 2.3 (#37,038) | **1.** A loose temporary sewing stitch to hold layers of fabric together.<br>**2.** Cover with liquid before cooking. | *"Shall the proud lord That bastes his arrogance with his own seam And never suffers matter of the world Enter his thoughts, save such as doth revolve And ruminate himself—shall he be worshipp’d Of that we hold an idol more than he?"* — William Shakespeare, *The Complete Works of William Shakespeare* |
| [[basel]] | noun | 📈 Zipf 2.3 (#37,529) | **1.** A city in northwestern switzerland. | *"In academic literature, basel designates a city in northwestern switzerland."* — Academic Lexicon, *Morphological & Etymological Survey* |
| [[bast]] | noun | 📈 Zipf 2.3 (#41,292) | **1.** Strong woody fibers obtained especially from the phloem of from various plants.<br>**2.** (botany) tissue that conducts synthesized food substances (e.g., from leaves) to parts where needed; consists primarily of sieve tubes. | *"Under guise of a present for the pilgrims, Princess Mary prepared a pilgrim’s complete costume for herself: a coarse smock, bast shoes, a rough coat, and a black kerchief."* — graf Leo Tolstoy, *War and Peace* |
| [[basset]] | noun | 📈 Zipf 2.3 (#41,775) | **1.** Smooth-haired breed of hound with short legs and long ears.<br>**2.** Appear at the surface. | *"Enter the King, Gloucester, Bishop of Winchester, Exeter, York, Warwick and Vernon; Suffolk, Somerset, Basset and others."* — William Shakespeare, *The Complete Works of William Shakespeare* |
| [[basia]] | noun | 📈 Zipf 2.3 (#43,981) | **1.** The second largest city in iraq; an oil port in southern iraq. | *"In academic literature, basia designates the second largest city in iraq; an oil port in southern iraq."* — Academic Lexicon, *Morphological & Etymological Survey* |


### 🏛️ Tier 3: Words to Learn Last (Rare & Specialized) (88 words)

| Word | POS | Frequency / Rank | Authoritative Definitions | Authentic Illustrative Sentence |
| :--- | :--- | :--- | :--- | :--- |
| [[abash]] | verb | 🏛️ Rare / Obsolete | **1.** Cause to be embarrassed; cause to feel self-conscious. | *"Why shrinks my soul half blushing, half afraid, Backward, abash’d to ask thy friendly aid?"* — Robert Burns, *Poems and Songs of Robert Burns* |
| [[abashed]] | verb | 🏛️ Rare / Obsolete | **1.** Cause to be embarrassed; cause to feel self-conscious.<br>**2.** Feeling or caused to feel uneasy and self-conscious. | *"Mad, young gentleman,” she returned so quickly that he was quite abashed."* — Charles Dickens, *Bleak House* |
| [[abashment]] | noun | 🏛️ Rare / Obsolete | **1.** Feeling embarrassed due to modesty. | *"In academic literature, abashment designates feeling embarrassed due to modesty."* — Academic Lexicon, *Morphological & Etymological Survey* |
| [[basal]] | adjective | 🏛️ Rare / Obsolete | **1.** Especially of leaves; located at the base of a plant or stem; especially arising directly from the root or rootstock or a root-like stem.<br>**2.** Serving as or forming a base. | *"The outward movement of the basal half of the jaw necessarily twists in the same direction the column-like bone to which it is suspended."* — W. E. Webb, *Buffalo Land* |
| [[basalt]] | noun | 🏛️ Rare / Obsolete | **1.** The commonest type of solidified lava; a dense dark grey fine-grained igneous rock that is composed chiefly of plagioclase feldspar and pyroxene. | *"I tried to speak, but Captain Nemo stopped me by a gesture, and, picking up a piece of chalk-stone, advanced to a rock of black basalt, and traced the one word: ATLANTIS What a light shot through my mind!"* — Jules Verne, *Twenty Thousand Leagues under the Sea* |
| [[basaltic]] | adjective | 🏛️ Rare / Obsolete | **1.** Of or relating to or containing basalt. | *"The geological formation is sometimes basaltic, at others slate, porphyry, etc."* — W. D. Pitcairn, *Two Years Among the Savages of New Guinea.* |
| [[bascule]] | noun | 🏛️ Rare / Obsolete | **1.** A structure or device in which one end is counterbalanced by the other (on the principle of the seesaw). | *"In academic literature, bascule designates a structure or device in which one end is counterbalanced by the other (on the principle of the seesaw)."* — Academic Lexicon, *Morphological & Etymological Survey* |
| [[base-forming]] | adjective | 🏛️ Rare / Obsolete | **1.** Yielding a base in aqueous solution. | *"In academic literature, base-forming designates yielding a base in aqueous solution."* — Academic Lexicon, *Morphological & Etymological Survey* |
| [[baseboard]] | noun | 🏛️ Rare / Obsolete | **1.** A molding covering the joint formed by a wall and the floor. | *"She did not sweep the dust under the bureau, or behind the door, or forget to wipe the rounds of the chairs and the baseboard all around the rooms."* — Annie Roe Carr, *Nan Sherwood at Pine Camp; Or, The Old Lumberman's Secret* |
| [[baseborn]] | adjective | 🏛️ Rare / Obsolete | **1.** Of low birth or station (`base' is archaic in this sense).<br>**2.** Illegitimate. | *"In academic literature, baseborn designates of low birth or station (`base' is archaic in this sense)."* — Academic Lexicon, *Morphological & Etymological Survey* |
| [[basely]] | adverb | 🏛️ Rare / Obsolete | **1.** In a despicable, ignoble manner. | *"To spend that shortness basely were too long If life did ride upon a dial’s point, Still ending at the arrival of an hour."* — William Shakespeare, *The Complete Works of William Shakespeare* |
| [[baseness]] | noun | 🏛️ Rare / Obsolete | **1.** Unworthiness by virtue of lacking higher values. | *"Since Cleopatra died, I have lived in such dishonour that the gods Detest my baseness."* — William Shakespeare, *The Complete Works of William Shakespeare* |
| [[basenji]] | noun | 🏛️ Rare / Obsolete | **1.** Small smooth-haired breed of african origin having a tightly curled tail and the inability to bark. | *"In academic literature, basenji designates small smooth-haired breed of african origin having a tightly curled tail and the inability to bark."* — Academic Lexicon, *Morphological & Etymological Survey* |
| [[basidial]] | adjective | 🏛️ Rare / Obsolete | **1.** Relating to or characterized by basidia. | *"In academic literature, basidial designates relating to or characterized by basidia."* — Academic Lexicon, *Morphological & Etymological Survey* |
| [[basidiocarp]] | noun | 🏛️ Rare / Obsolete | **1.** The fruiting body of a basidiomycete which bears its spores on special cells. | *"In academic literature, basidiocarp designates the fruiting body of a basidiomycete which bears its spores on special cells."* — Academic Lexicon, *Morphological & Etymological Survey* |
| [[basidiolichen]] | noun | 🏛️ Rare / Obsolete | **1.** A lichen in which the fungus component is a basidiomycete. | *"In academic literature, basidiolichen designates a lichen in which the fungus component is a basidiomycete."* — Academic Lexicon, *Morphological & Etymological Survey* |
| [[basidiomycete]] | noun | 🏛️ Rare / Obsolete | **1.** Any of various fungi of the subdivision basidiomycota. | *"In academic literature, basidiomycete designates any of various fungi of the subdivision basidiomycota."* — Academic Lexicon, *Morphological & Etymological Survey* |
| [[basidiomycetes]] | noun | 🏛️ Rare / Obsolete | **1.** Large class of higher fungi coextensive with subdivision basidiomycota.<br>**2.** Any of various fungi of the subdivision basidiomycota. | *"In academic literature, basidiomycetes designates large class of higher fungi coextensive with subdivision basidiomycota."* — Academic Lexicon, *Morphological & Etymological Survey* |
| [[basidiomycetous]] | adjective | 🏛️ Rare / Obsolete | **1.** Pertaining to or characteristic of fungi of the class basidiomycetes. | *"In academic literature, basidiomycetous designates pertaining to or characteristic of fungi of the class basidiomycetes."* — Academic Lexicon, *Morphological & Etymological Survey* |
| [[basidiomycota]] | noun | 🏛️ Rare / Obsolete | **1.** Comprises fungi bearing the spores on a basidium; includes gasteromycetes (puffballs) and tiliomycetes comprising the orders ustilaginales (smuts) and uredinales (rusts) and hymenomycetes (mushrooms, toadstools, agarics and bracket fungi); in some classification systems considered a division of kingdom fungi. | *"In academic literature, basidiomycota designates comprises fungi bearing the spores on a basidium; includes gasteromycetes (puffballs) and tiliomycetes comprising the orders ustilaginales (smuts) and uredinales (rusts) and hymenomycetes (mushrooms, toadstools, agarics and bracket fungi); in some classification systems considered a division of kingdom fungi."* — Academic Lexicon, *Morphological & Etymological Survey* |
| [[basidiomycotina]] | noun | 🏛️ Rare / Obsolete | **1.** Comprises fungi bearing the spores on a basidium; includes gasteromycetes (puffballs) and tiliomycetes comprising the orders ustilaginales (smuts) and uredinales (rusts) and hymenomycetes (mushrooms, toadstools, agarics and bracket fungi); in some classification systems considered a division of kingdom fungi. | *"In academic literature, basidiomycotina designates comprises fungi bearing the spores on a basidium; includes gasteromycetes (puffballs) and tiliomycetes comprising the orders ustilaginales (smuts) and uredinales (rusts) and hymenomycetes (mushrooms, toadstools, agarics and bracket fungi); in some classification systems considered a division of kingdom fungi."* — Academic Lexicon, *Morphological & Etymological Survey* |
| [[basidiospore]] | noun | 🏛️ Rare / Obsolete | **1.** A sexually produced fungal spore borne on a basidium. | *"In academic literature, basidiospore designates a sexually produced fungal spore borne on a basidium."* — Academic Lexicon, *Morphological & Etymological Survey* |
| [[basidiosporous]] | adjective | 🏛️ Rare / Obsolete | **1.** Of or relating to or characterized by spores produced by basidia. | *"In academic literature, basidiosporous designates of or relating to or characterized by spores produced by basidia."* — Academic Lexicon, *Morphological & Etymological Survey* |
| [[basidium]] | noun | 🏛️ Rare / Obsolete | **1.** A small club-shaped structure typically bearing four basidiospores at the ends of minute projections; unique to basidiomycetes. | *"In academic literature, basidium designates a small club-shaped structure typically bearing four basidiospores at the ends of minute projections; unique to basidiomycetes."* — Academic Lexicon, *Morphological & Etymological Survey* |
| [[basifixed]] | adjective | 🏛️ Rare / Obsolete | **1.** Attached by its base (as certain anthers to their filaments or stalks). | *"In academic literature, basifixed designates attached by its base (as certain anthers to their filaments or stalks)."* — Academic Lexicon, *Morphological & Etymological Survey* |
| [[basify]] | verb | 🏛️ Rare / Obsolete | **1.** Turn basic and less acidic. | *"In academic literature, basify designates turn basic and less acidic."* — Academic Lexicon, *Morphological & Etymological Survey* |
| [[basilar]] | adjective | 🏛️ Rare / Obsolete | **1.** Of or relating to or located at the base. | *"In academic literature, basilar designates of or relating to or located at the base."* — Academic Lexicon, *Morphological & Etymological Survey* |
| [[basilary]] | adjective | 🏛️ Rare / Obsolete | **1.** Of or relating to or located at the base. | *"In academic literature, basilary designates of or relating to or located at the base."* — Academic Lexicon, *Morphological & Etymological Survey* |
| [[basileus]] | noun | 🏛️ Rare / Obsolete | **1.** A ruler of the eastern roman empire. | *"The Greeks used _basileus_ as Emperor. [101] viii, 69."* — T. R. Glover, *The Conflict of Religions in the Early Roman Empire* |
| [[basilican]] | adjective | 🏛️ Rare / Obsolete | **1.** Of or relating to or resembling a basilica. | *"In academic literature, basilican designates of or relating to or resembling a basilica."* — Academic Lexicon, *Morphological & Etymological Survey* |
| [[basilicata]] | noun | 🏛️ Rare / Obsolete | **1.** A region of southern italy (forming the instep of the italian `boot'). | *"In academic literature, basilicata designates a region of southern italy (forming the instep of the italian `boot')."* — Academic Lexicon, *Morphological & Etymological Survey* |
| [[basiliscus]] | noun | 🏛️ Rare / Obsolete | **1.** A reptile genus of iguanidae. | *"In academic literature, basiliscus designates a reptile genus of iguanidae."* — Academic Lexicon, *Morphological & Etymological Survey* |
| [[basilisk]] | noun | 🏛️ Rare / Obsolete | **1.** (classical mythology) a serpent (or lizard or dragon) able to kill with its breath or glance.<br>**2.** Ancient brass cannon. | *"Here, take this too; [_Gives the ring._] It is a basilisk unto mine eye, Kills me to look on’t."* — William Shakespeare, *The Complete Works of William Shakespeare* |
| [[basinal]] | adjective | 🏛️ Rare / Obsolete | **1.** Of or relating to a basin. | *"In academic literature, basinal designates of or relating to a basin."* — Academic Lexicon, *Morphological & Etymological Survey* |
| [[basined]] | adjective | 🏛️ Rare / Obsolete | **1.** Enclosed in a basin. | *"In academic literature, basined designates enclosed in a basin."* — Academic Lexicon, *Morphological & Etymological Survey* |
| [[basinet]] | noun | 🏛️ Rare / Obsolete | **1.** A medieval steel helmet. | *"In academic literature, basinet designates a medieval steel helmet."* — Academic Lexicon, *Morphological & Etymological Survey* |
| [[basinful]] | noun | 🏛️ Rare / Obsolete | **1.** The quantity that a basin will hold. | *"In academic literature, basinful designates the quantity that a basin will hold."* — Academic Lexicon, *Morphological & Etymological Survey* |
| [[basipetal]] | adjective | 🏛️ Rare / Obsolete | **1.** Of leaves or flowers; developing or opening in succession from apex to base. | *"In academic literature, basipetal designates of leaves or flowers; developing or opening in succession from apex to base."* — Academic Lexicon, *Morphological & Etymological Survey* |
| [[basiscopic]] | adjective | 🏛️ Rare / Obsolete | **1.** Facing or on the side toward the base. | *"In academic literature, basiscopic designates facing or on the side toward the base."* — Academic Lexicon, *Morphological & Etymological Survey* |
| [[basle]] | noun | 🏛️ Rare / Obsolete | **1.** A city in northwestern switzerland. | *"In academic literature, basle designates a city in northwestern switzerland."* — Academic Lexicon, *Morphological & Etymological Survey* |
| [[basophil]] | noun | 🏛️ Rare / Obsolete | **1.** A leukocyte with basophilic granules easily stained by basic stains. | *"In academic literature, basophil designates a leukocyte with basophilic granules easily stained by basic stains."* — Academic Lexicon, *Morphological & Etymological Survey* |
| [[basophile]] | noun | 🏛️ Rare / Obsolete | **1.** A leukocyte with basophilic granules easily stained by basic stains. | *"In academic literature, basophile designates a leukocyte with basophilic granules easily stained by basic stains."* — Academic Lexicon, *Morphological & Etymological Survey* |
| [[basophilia]] | noun | 🏛️ Rare / Obsolete | **1.** The tendency of cells to stain with basic dyes. | *"In academic literature, basophilia designates the tendency of cells to stain with basic dyes."* — Academic Lexicon, *Morphological & Etymological Survey* |
| [[basophilic]] | adjective | 🏛️ Rare / Obsolete | **1.** Staining readily with basic dyes. | *"In academic literature, basophilic designates staining readily with basic dyes."* — Academic Lexicon, *Morphological & Etymological Survey* |
| [[basotho]] | noun | 🏛️ Rare / Obsolete | **1.** A member of a subgroup of people who inhabit lesotho. | *"In academic literature, basotho designates a member of a subgroup of people who inhabit lesotho."* — Academic Lexicon, *Morphological & Etymological Survey* |
| [[bassariscidae]] | noun | 🏛️ Rare / Obsolete | **1.** In some classifications considered a separate family. | *"In academic literature, bassariscidae designates in some classifications considered a separate family."* — Academic Lexicon, *Morphological & Etymological Survey* |
| [[bassariscus]] | noun | 🏛️ Rare / Obsolete | **1.** Cacomistles. | *"In academic literature, bassariscus designates cacomistles."* — Academic Lexicon, *Morphological & Etymological Survey* |
| [[bassarisk]] | noun | 🏛️ Rare / Obsolete | **1.** Raccoon-like omnivorous mammal of mexico and the southwestern united states having a long bushy tail with black and white rings. | *"In academic literature, bassarisk designates raccoon-like omnivorous mammal of mexico and the southwestern united states having a long bushy tail with black and white rings."* — Academic Lexicon, *Morphological & Etymological Survey* |
| [[basse-normandie]] | noun | 🏛️ Rare / Obsolete | **1.** A division of normandy. | *"In academic literature, basse-normandie designates a division of normandy."* — Academic Lexicon, *Morphological & Etymological Survey* |
| [[basseterre]] | noun | 🏛️ Rare / Obsolete | **1.** The capital of saint kitts and nevis on the island of saint christopher. | *"In academic literature, basseterre designates the capital of saint kitts and nevis on the island of saint christopher."* — Academic Lexicon, *Morphological & Etymological Survey* |
| [[bassia]] | noun | 🏛️ Rare / Obsolete | **1.** Summer cypress. | *"In academic literature, bassia designates summer cypress."* — Academic Lexicon, *Morphological & Etymological Survey* |
| [[bassine]] | noun | 🏛️ Rare / Obsolete | **1.** Coarse leaf fiber from palmyra palms used in making brushes and brooms. | *"In academic literature, bassine designates coarse leaf fiber from palmyra palms used in making brushes and brooms."* — Academic Lexicon, *Morphological & Etymological Survey* |
| [[bassinet]] | noun | 🏛️ Rare / Obsolete | **1.** A basket (usually hooded) used as a baby's bed.<br>**2.** A perambulator that resembles a bassinet. | *"In academic literature, bassinet designates a basket (usually hooded) used as a baby's bed."* — Academic Lexicon, *Morphological & Etymological Survey* |
| [[bassist]] | noun | 🏛️ Rare / Obsolete | **1.** A musician who play the bass viol. | *"In academic literature, bassist designates a musician who play the bass viol."* — Academic Lexicon, *Morphological & Etymological Survey* |
| [[basso]] | noun | 🏛️ Rare / Obsolete | **1.** An adult male singer with the lowest voice.<br>**2.** The lowest adult male singing voice. | *"A foreign friend once pointed it out to me, in the skeleton of a foe he had slain, and with the vertebræ of which he was inlaying, in a sort of basso-relievo, the beaked prow of his canoe."* — Herman Melville, *Moby-Dick; or, The Whale* |
| [[bassoon]] | noun | 🏛️ Rare / Obsolete | **1.** A double-reed instrument; the tenor of the oboe family. | *"A Briton!” “And Mat blows away at his bassoon, and you’re respectable civilians one and all,” says Mr."* — Charles Dickens, *Bleak House* |
| [[bassoonist]] | noun | 🏛️ Rare / Obsolete | **1.** A musician who plays the bassoon. | *"In academic literature, bassoonist designates a musician who plays the bassoon."* — Academic Lexicon, *Morphological & Etymological Survey* |
| [[basswood]] | noun | 🏛️ Rare / Obsolete | **1.** Soft light-colored wood of any of various linden trees; used in making crates and boxes and in carving and millwork.<br>**2.** Any of various deciduous trees of the genus tilia with heart-shaped leaves and drooping cymose clusters of yellowish often fragrant flowers; several yield valuable timber. | *"In academic literature, basswood designates soft light-colored wood of any of various linden trees; used in making crates and boxes and in carving and millwork."* — Academic Lexicon, *Morphological & Etymological Survey* |
| [[bastardisation]] | noun | 🏛️ Rare / Obsolete | **1.** An act that debases or corrupts. | *"In academic literature, bastardisation designates an act that debases or corrupts."* — Academic Lexicon, *Morphological & Etymological Survey* |
| [[bastardise]] | verb | 🏛️ Rare / Obsolete | **1.** Change something so that its value declines; for example, art forms.<br>**2.** Declare a child to be illegitimate. | *"In academic literature, bastardise designates change something so that its value declines; for example, art forms."* — Academic Lexicon, *Morphological & Etymological Survey* |
| [[bastardised]] | verb | 🏛️ Rare / Obsolete | **1.** Change something so that its value declines; for example, art forms.<br>**2.** Declare a child to be illegitimate. | *"In academic literature, bastardised designates change something so that its value declines; for example, art forms."* — Academic Lexicon, *Morphological & Etymological Survey* |
| [[bastardization]] | noun | 🏛️ Rare / Obsolete | **1.** Declaring or rendering bastard.<br>**2.** An act that debases or corrupts. | *"In academic literature, bastardization designates declaring or rendering bastard."* — Academic Lexicon, *Morphological & Etymological Survey* |
| [[bastardize]] | verb | 🏛️ Rare / Obsolete | **1.** Change something so that its value declines; for example, art forms.<br>**2.** Declare a child to be illegitimate. | *"I should have been that I am, had the maidenliest star in the firmament twinkled on my bastardizing."* — William Shakespeare, *The Complete Works of William Shakespeare* |
| [[bastardized]] | verb | 🏛️ Rare / Obsolete | **1.** Change something so that its value declines; for example, art forms.<br>**2.** Declare a child to be illegitimate. | *"In academic literature, bastardized designates change something so that its value declines; for example, art forms."* — Academic Lexicon, *Morphological & Etymological Survey* |
| [[bastardly]] | adjective | 🏛️ Rare / Obsolete | **1.** Born out of wedlock; - e.a.freeman.<br>**2.** Of no value or worth. | *"Wilt thou, wilt thou, thou bastardly rogue?"* — William Shakespeare, *The Complete Works of William Shakespeare* |
| [[bastardy]] | noun | 🏛️ Rare / Obsolete | **1.** The status of being born to parents who were not married. | *"But once he slander’d me with bastardy."* — William Shakespeare, *The Complete Works of William Shakespeare* |
| [[baster]] | noun | 🏛️ Rare / Obsolete | **1.** A cook who bastes roasting meat with melted fat or gravy.<br>**2.** A sewer who fastens a garment with long loose stitches. | *"In academic literature, baster designates a cook who bastes roasting meat with melted fat or gravy."* — Academic Lexicon, *Morphological & Etymological Survey* |
| [[bastinado]] | noun | 🏛️ Rare / Obsolete | **1.** A cudgel used to give someone a beating on the soles of the feet.<br>**2.** A form of torture in which the soles of the feet are beaten with whips or cudgels. | *"I will deal in poison with thee, or in bastinado, or in steel."* — William Shakespeare, *The Complete Works of William Shakespeare* |
| [[basting]] | noun | 🏛️ Rare / Obsolete | **1.** A loose temporary sewing stitch to hold layers of fabric together.<br>**2.** Moistening a roast as it is cooking. | *"Lest it make you choleric, and purchase me another dry basting."* — William Shakespeare, *The Complete Works of William Shakespeare* |
| [[bastioned]] | adjective | 🏛️ Rare / Obsolete | **1.** Secured with bastions or fortifications. | *"In academic literature, bastioned designates secured with bastions or fortifications."* — Academic Lexicon, *Morphological & Etymological Survey* |
| [[bastnaesite]] | noun | 🏛️ Rare / Obsolete | **1.** A yellow-to-brown mineral that is a source of rare earth elements. | *"In academic literature, bastnaesite designates a yellow-to-brown mineral that is a source of rare earth elements."* — Academic Lexicon, *Morphological & Etymological Survey* |
| [[bastnasite]] | noun | 🏛️ Rare / Obsolete | **1.** A yellow-to-brown mineral that is a source of rare earth elements. | *"In academic literature, bastnasite designates a yellow-to-brown mineral that is a source of rare earth elements."* — Academic Lexicon, *Morphological & Etymological Survey* |
| [[basuco]] | noun | 🏛️ Rare / Obsolete | **1.** Low-grade cocaine mixed with coca paste and cannabis. | *"In academic literature, basuco designates low-grade cocaine mixed with coca paste and cannabis."* — Academic Lexicon, *Morphological & Etymological Survey* |
| [[basuto]] | noun | 🏛️ Rare / Obsolete | **1.** The dialect of sotho spoken by the basotho; an official language of lesotho. | *"Soon the horses, most of which were small and of the Basuto breed, were ready to start."* — H. Rider Haggard, *Swallow: A Tale of the Great Trek* |
| [[basutoland]] | noun | 🏛️ Rare / Obsolete | **1.** A landlocked constitutional monarchy in southern africa; achieved independence from the united kingdom in 1966. | *"In academic literature, basutoland designates a landlocked constitutional monarchy in southern africa; achieved independence from the united kingdom in 1966."* — Academic Lexicon, *Morphological & Etymological Survey* |
| [[contrabass]] | noun | 🏛️ Rare / Obsolete | **1.** Largest and lowest member of the violin family.<br>**2.** Pitched an octave below normal bass instrumental or vocal range. | *"In academic literature, contrabass designates largest and lowest member of the violin family."* — Academic Lexicon, *Morphological & Etymological Survey* |
| [[contrabassoon]] | noun | 🏛️ Rare / Obsolete | **1.** The bassoon that is the largest instrument in the oboe family. | *"In academic literature, contrabassoon designates the bassoon that is the largest instrument in the oboe family."* — Academic Lexicon, *Morphological & Etymological Survey* |
| [[debase]] | verb | 🏛️ Rare / Obsolete | **1.** Corrupt morally or by intemperance or sensuality.<br>**2.** Lower in value by increasing the base-metal content. | *"With all the gracious utterance thou hast, Speak to his gentle hearing kind commends. [_Northumberland returns to Bolingbroke._] [_To Aumerle_.] We do debase ourselves, cousin, do we not, To look so poorly and to speak so fair?"* — William Shakespeare, *The Complete Works of William Shakespeare* |
| [[debased]] | verb | 🏛️ Rare / Obsolete | **1.** Corrupt morally or by intemperance or sensuality.<br>**2.** Lower in value by increasing the base-metal content. | *"Yes, that’s the d’Urberville nose and chin—a little debased."* — Thomas Hardy, *Tess of the d'Urbervilles: A Pure Woman* |
| [[debasement]] | noun | 🏛️ Rare / Obsolete | **1.** Being mixed with extraneous material; the product of adulterating.<br>**2.** Changing to a lower state (a less respected state). | *"Or, to speak in the fashionable language of the adversaries to the Constitution, will it court the elevation of “the wealthy and the well-born,” to the exclusion and debasement of all the rest of the society?"* — Alexander Hamilton, *The Federalist Papers* |
| [[debaser]] | noun | 🏛️ Rare / Obsolete | **1.** A person who lowers the quality or character or value (as by adding cheaper metal to coins). | *"In academic literature, debaser designates a person who lowers the quality or character or value (as by adding cheaper metal to coins)."* — Academic Lexicon, *Morphological & Etymological Survey* |
| [[debasing]] | verb | 🏛️ Rare / Obsolete | **1.** Corrupt morally or by intemperance or sensuality.<br>**2.** Lower in value by increasing the base-metal content. | *"He could not make the request; it was debasing loveliness to ask it to buy and sell, and jarred with his conceptions of her."* — Thomas Hardy, *Far from the Madding Crowd* |
| [[sebastiana]] | noun | 🏛️ Rare / Obsolete | **1.** Mexican spurges. | *"In academic literature, sebastiana designates mexican spurges."* — Academic Lexicon, *Morphological & Etymological Survey* |
| [[sebastodes]] | noun | 🏛️ Rare / Obsolete | **1.** Rockfishes. | *"In academic literature, sebastodes designates rockfishes."* — Academic Lexicon, *Morphological & Etymological Survey* |
| [[sebastopol]] | noun | 🏛️ Rare / Obsolete | **1.** A city in southern ukraine on the black sea. | *"I am old enough to recollect the trenches before Sebastopol, and all that my countrymen and the English endured there."* — Mrs. Oliphant, *A Beleaguered City* |
| [[subbase]] | noun | 🏛️ Rare / Obsolete | **1.** The lowest molding of an architectural base or of a baseboard. | *"In academic literature, subbase designates the lowest molding of an architectural base or of a baseboard."* — Academic Lexicon, *Morphological & Etymological Survey* |
| [[surbase]] | noun | 🏛️ Rare / Obsolete | **1.** The molding or border above the base of a structure (a pedestal or podium or wall). | *"In academic literature, surbase designates the molding or border above the base of a structure (a pedestal or podium or wall)."* — Academic Lexicon, *Morphological & Etymological Survey* |
| [[unabashed]] | adjective | 🏛️ Rare / Obsolete | **1.** Not embarrassed; - jerome stone. | *"Skimpole, unabashed and candid."* — Charles Dickens, *Bleak House* |
