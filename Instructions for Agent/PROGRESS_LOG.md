# Vocabulary Database & Mobile UI Upgrade — Master Progress Log

**Started At:** 2026-09-30T17:10:00+08:00  
**Last Updated:** 2026-10-03T13:06:00+08:00  
**Workspace:** `c:\Users\user\Desktop\Vocab app`  
**Database Root:** `c:\Users\user\Desktop\Vocab app\App database`  
**Checkpoint State File:** `c:\Users\user\Desktop\Vocab app\Instructions for Agent\checkpoint_state.json`

---

## Major Milestones & Status

- [x] **Milestone 0: Audit & Agent Instructions Setup**
  - Completed baseline audit of all vocabulary word notes.
  - Saved permanent instructions in `Instructions for Agent/Word_Creation_and_Curation_Instructions.md`.
- [x] **Milestone 1: Mobile UI & Tab 2 Top-of-Definition Tracking Button Upgrade**
  - Updated `main app/public/js/mobile-app.js` and `main app/public/styles/mobile-app.css` to:
    1. Mount the original app's `.apple-c` Apple Glide Status Toggle (`createAppleStatusToggle`: `unread ➔ learning ➔ learned`) directly at the top of the definition box on Tab 2 (`renderFeedCard`) and Tab 3 (`renderDailyCard`), as well as supporting `.meta-bind-status-mount` in `openHomeSection`.
    2. Extract and render all 3 concise literary/contextual citations (`quotes.slice(0, 3)`) on Tab 2 and Tab 3 word cards with target word highlighting.
- [x] **Milestone 2: Structural `.md` Optimization (Top-of-Definition Tracking Button & Frontmatter Repair)**
  - Repaired split/BOM-prefixed YAML frontmatter blocks (including `abactinal.md`) and replaced legacy `INPUT[inlineSelect]` status lines in `phoneme.md`, `digraph.md`, and `enormously.md`.
  - Repositioned `> [!status] 🎯 **Status:**` + `dataviewjs` `.apple-c` status toggle block from the bottom of the word `.md` files to the **top of the definition** (immediately below `# <word>` and directly above `> [!book]`) across **100% of all 47,447 individual word `.md` files** in `App database/`.
- [x] **Milestone 3: Individualized Curation — `English vocabulary master` (514 Words across 30 Clusters)**
  - Cluster-by-cluster individualized verification and curation of Primary & Secondary definitions, grammar tips, and 3 concise literary citations from distinct authors.
  - Audit results: 30 / 30 clusters verified pristine (0 issues remaining across 514 word notes).
  - All proper nouns, homograph traps (e.g. animal spine vs coastal ravine for *chine*, military rank vs overgrown for *rank*, Denver vs rock for *boulder*, Scottish dialect neck vs mountain cliff for *crag*, dog breed vs memorial heap for *cairn*), repeated authors, and missing quotes eradicated.
- [ ] **Milestone 4: Individualized Curation — `Greek roots` (19,357 Words across 19 Clusters)**
  - Cluster 1: `Cluster Power, Strength & Dominion` (60 words) — 100% Pristine (0 issues)
  - Cluster 2: `Cluster Science & Inquiry` (79 words) — 100% Pristine (0 issues)
  - Cluster 3: `Cluster Self & Identity` (131 words) — 100% Pristine (0 issues)
  - Cluster 4: `Cluster Structure & Form` (132 words) — 100% Pristine (0 issues)
  - Cluster 5: `Cluster War & Conflict` (141 words) — 100% Pristine (0 issues)
  - Cluster 6: `Cluster Turning & Transformation` (142 words) — 100% Pristine (0 issues)
  - Cluster 7: `Cluster Law & Order` (172 words) — 100% Pristine (0 issues)
  - Cluster 8: `Cluster Sound & Auditory` (247 words) — 100% Pristine (0 issues)
  - Cluster 9: `Cluster Art, Craft & Design` (296 words) — 100% Pristine (0 issues)
  - Cluster 10: `Cluster Nature & Cosmos` (308 words) — 100% Pristine (0 issues)
  - Cluster 11: `Cluster Speech & Language` (311 words) — 100% Pristine (0 issues)
  - Cluster 12: `Cluster Cognition & Mind` (315 words) — 100% Pristine (0 issues)
  - Cluster 13: `Cluster Beginning & Primacy` (343 words) — 100% Pristine (0 issues)
  - Cluster 14: `Cluster Writing & Script` (349 words) — 100% Pristine (0 issues)
  - Cluster 15: `Cluster Medicine & Pathology` (351 words) — 100% Pristine (0 issues)
  - Cluster 16: `Cluster Earth & Geology` (363 words) — 100% Pristine (0 issues)
  - Cluster 17: `Cluster Water & Hydrology` (370 words) — 100% Pristine (0 issues)
  - Cluster 18: `Cluster Motion & Direction` (402 words) — 100% Pristine (0 issues)
  - Cluster 19: `Cluster Time & Chronology` (471 words) — IN PROGRESS
- [ ] **Milestone 5: Individualized Curation — `Latin roots` (30,611 Words across 60 Clusters, 782 Dashboards) — IN PROGRESS**
  - **Pilot Completed:** `Dashboard — act` (120/120 words verified pristine, 100% pass, 0 issues).
  - Built offline local dictionary `main app/corpus/local_dictionary.db` (303,443 entries: WordNet 3.1 + Webster's 1913).
  - Strict Multi-Source MCP architecture: `Dictionary-MCP`, `wikipedia`, `crw` MCP, `philosophy` MCP, and `local_dictionary.db`.
  - Zero-Synthetic Literary Phrases mandate: `project-gutenberg`, `crw` Wiktionary historical citations, `philosophy` MCP, and `citation_corpus.db`.
  - Structured across 10 Thematic Execution Waves with 7-gate automated audit verification. *(See detailed plan below)*.
- [ ] **Milestone 6: Full Verification, Re-Index, Android Sync & GitHub Commit**
  - Run `npm run verify-db` and `npm run reindex`.
  - Sync Capacitor Android assets (`npm run cap:sync`).
  - Commit and push checkpoints to `https://github.com/yorren005/vocab-app`.

---

## Detailed Execution Log

| Timestamp | Milestone / Batch | Action Taken | Files Updated | Status |
| :--- | :--- | :--- | ---: | :--- |
| 2026-09-30 17:10 | Milestone 0 | Created `Instructions for Agent/Word_Creation_and_Curation_Instructions.md` and initialized `PROGRESS_LOG.md` | 2 | ✅ Completed |
| 2026-09-30 17:15 | Milestone 1 | Upgraded `mobile-app.js` and `mobile-app.css`: mounted `.apple-c` status toggle at top of definition on Tab 2 & Tab 3, and added 3-citation stack rendering | 2 | ✅ Completed |
| 2026-09-30 17:30 | Milestone 2 | Moved `> [!status]` + `dataviewjs` `.apple-c` toggle block to the top of the definition across all 47,447 word notes; manually curated `actin.md`, `abactinal.md`, `action.md`, `comely.md`, `phoneme.md`, `digraph.md`, and `enormously.md` | 47,447 | ✅ Completed |
| 2026-09-30 20:36 | Milestone 3 | Completed individualized curation of all 30 clusters in `English vocabulary master` (514 word notes). Verified 0 issues via `audit-clusters.mjs`. | 514 | ✅ Completed |
| 2026-09-30 20:47 | Milestone 4 | Completed individualized curation of Greek roots `Cluster Power, Strength & Dominion` (60 word notes across `despot`, `sthen`, `dyna`, `dynam`). Verified 0 issues via `audit-roots.mjs`. | 60 | ✅ Completed |
| 2026-09-30 20:52 | Milestone 4 | Completed individualized curation of Greek roots `Cluster Science & Inquiry` (79 word notes across `heur`, `stoch`, `zet`, `axi`, `academ`, `an`, `organ`). Verified 0 issues via `audit-roots.mjs`. | 79 | ✅ Completed |
| 2026-09-30 20:58 | Milestone 4 | Completed individualized curation of Greek roots `Cluster Self & Identity` (131 word notes across 10 dashboards). Verified 0 issues via `audit-roots.mjs`. | 131 | ✅ Completed |
| 2026-09-30 21:05 | Milestone 4 | Completed individualized curation of Greek roots `Cluster Structure & Form` (132 word notes across 7 dashboards: `plinth`, `athroid`, `phrag`, `pyl`, `por`, `tect`, `stere`, `pach`, `stor`). Verified 0 issues via `audit-roots.mjs`. | 132 | ✅ Completed |
| 2026-09-30 21:10 | Milestone 4 | Completed individualized curation of Greek roots `Cluster War & Conflict` (141 word notes across 9 dashboards: `hopl`, `tax`, `xiph`, `thyre`, `athl`, `machia_ machy`, `polem`, `strat`, `pros`). Verified 0 issues via `audit-roots.mjs`. | 141 | ✅ Completed |
| 2026-09-30 23:16 | Milestone 4 | Completed individualized curation of Greek roots `Cluster Turning & Transformation` (142 word notes across 7 dashboards: `cochl`, `palin`, `cylind`, `helic`, `strept`, `stroph`, `gyr`, `trop`). Disambiguated astrophysics homographs and optical gyrotropy. Verified 0 issues via `audit-roots.mjs`. | 142 | ✅ Completed |
| 2026-10-01 13:13 | Milestone 4 | Completed individualized curation of Greek roots `Cluster Law & Order` (172 word notes across 10 dashboards: `dexi`, `dike`, `aether`, `eth`, `can`, `them`, `nem`, `nom`, `tag`, `crit`). Disambiguated Dike justice vs embankment, Numidian nomads, and glandular cytological secretors. Verified 0 issues via `audit-roots.mjs`. | 172 | ✅ Completed |
| 2026-10-01 13:23 | Milestone 4 | Completed individualized curation of Greek roots `Cluster Sound & Auditory` (247 word notes across 11 dashboards: `gargar`, `psithyr`, `aul`, `psoph`, `phtheg`, `acou`, `rhythm`, `mel`, `mous`, `tympan`, `chord`, `ech`, `bomb`, `phon`). Disambiguated rodents/computing/gastronomy substring matches on `mous`, sericultural/acoustic/explosive senses of `bomb`, and acoustic/notochord/geometry senses of `chord`. Verified 0 issues via `audit-roots.mjs`. | 247 | ✅ Completed |
| 2026-10-01 13:33 | Milestone 4 | Completed individualized curation of Greek roots `Cluster Art, Craft & Design` (296 word notes across 17 dashboards: `tetart`, `scyph`, `ap`, `thaumat`, `perdic`, `cosmet`, `hyph`, `orches`, `parthen`, `mim`, `chore`, `cal`, `plec`, `techn`, `arti`, `plast`, `mer`). Disambiguated agricultural `reap`/`reaper`, mythological `perdic` vs `perdition`, optical `cal` vs `decal`/`deceive`/`decor`/`epic`, and chemical polymers vs `dim`/`dimly`/`emmer`/`trim`. Verified 0 issues via `audit-roots.mjs`. | 296 | ✅ Completed |
| 2026-10-01 13:45 | Milestone 4 | Completed individualized curation of Greek roots `Cluster Nature & Cosmos` (308 word notes across 15 dashboards: `zephyr`, `styg`, `bront`, `ere`, `bore`, `nemat`, `selen`, `galact`, `uran`, `anem`, `chaet`, `cosm`, `trich`, `heli`, `aer`). Disambiguated Greek rowers vs `deere`/`ere`, bloodless `anemia` vs wind `anemos`, chlorines in `trichloride`/`chloroethane` vs hair `trich`, helical screws in `helicopter`/`helicon` vs sun `helios`, and anatomical `aorta` vs atmosphere `aer`. Verified 0 issues via `audit-roots.mjs`. | 308 | ✅ Completed |
| 2026-10-01 13:58 | Milestone 4 | Completed individualized curation of Greek roots `Cluster Speech & Language` (311 word notes across 13 dashboards: `siop`, `hermeneu`, `lex`, `ep`, `etym`, `onomat`, `phem`, `myth`, `herm`, `stell`, `gloss`, `onym`, `log`). Disambiguated Greek sending/contraction (*stellein*) vs Latin star (*stella*) and Georg Wilhelm Steller, German proper names (`herman`, `hermann`, `hermannia`, `hermosillo`), nudibranchs (`hermissenda`), liturgical dialogues (`dialogue doxology`), and timber vs event records (`log`, `logger`, `logging`). Verified 0 issues via `audit-roots.mjs`. | 311 | ✅ Completed |
| 2026-10-01 14:12 | Milestone 4 | Completed individualized curation of Greek roots `Cluster Cognition & Mind` (315 word notes across 15 dashboards: `aret`, `gno`, `hyp`, `ide`, `mancy`, `mn`, `mne`, `mor`, `oneir`, `phren`, `psych`, `soph`, `theo`, `theor`, `theori`). Disambiguated Greek virtue *arete* vs French glacial ridge *arête*, Greek aphorism *gnome* vs Paracelsian folklore creature, pea-family genus *Sophora* (Arabic *sufayra*) vs wisdom *sophia*, humidity meter *psychrometer* (Greek *psychros* cold) vs soul *psyche*, and butterfly orchids *Psychopsis* / moth flies *Psychodidae* (Greek *psyche* butterfly). Verified 0 issues via `audit-roots.mjs`. | 315 | ✅ Completed |
| 2026-10-01 14:35 | Milestone 4 | Completed individualized curation of Greek roots `Cluster Beginning & Primacy` (343 word notes). Verified 0 issues via `audit-roots.mjs`. | 343 | ✅ Completed |
| 2026-10-01 14:48 | Milestone 4 | Completed individualized curation of Greek roots `Cluster Writing & Script` (349 word notes). Verified 0 issues via `audit-roots.mjs`. | 349 | ✅ Completed |
| 2026-10-01 15:00 | Milestone 4 | Completed individualized curation of Greek roots `Cluster Medicine & Pathology` (351 word notes). Verified 0 issues via `audit-roots.mjs`. | 351 | ✅ Completed |
| 2026-10-01 15:05 | Milestone 4 | Completed individualized curation of Greek roots `Cluster Earth & Geology` (363 word notes). Verified 0 issues via `audit-roots.mjs`. | 363 | ✅ Completed |
| 2026-10-01 15:10 | Milestone 4 | Completed individualized curation of Greek roots `Cluster Water & Hydrology` (370 word notes across 17 dashboards: `bapt`, `broc`, `dros`, `hal`, `hygr`, `hydr`, `latry`, `lep`, `naut`, `nect`, `ocean`, `ombr`, `pelag`, `phyc`, `potam`, `raph`, `sphrag`, `thalass`, `rhe`). Disambiguated `alep` (scaleless vs Aleppo), `lep` (scale vs English proficiency acronym), `pelage` (mammal fur coat), `nautch` (traditional Indian dance), `rhyton` (libation horn), and musical/physiological rhythm vs rhetoric flow. Verified 0 issues via `audit-roots.mjs`. | 370 | ✅ Completed |
| 2026-10-01 15:20 | Milestone 4 | Completed individualized curation of Greek roots `Cluster Motion & Direction` (402 word notes across 19 dashboards: `pheug`, `brady`, `drome`, `pat`, `pro`, `pemp`, `pol`, `trech`, `streph`, `torn`, `stol`, `oestr`, `tach`, `dram`, `phor`, `kine`, `trep`, `ba`, `plan`). Disambiguated homographs and non-Greek overlaps (`expat`/`pat`/`pater` vs `peripatetic`; `stolid`/`stolidity` vs `apostle`/`diastole`; `detach`/`detachment` vs `tachometer`/`tachycardia`; `aerodrome`/`catadromous` vs `dramatist`/`dramaturgy`; archaic plural `kine` vs `kinetics`/`cinema`; `trepang` vs `trepan`/`entropy`; `plant`/`plane`/`planar` vs Greek wanderer `planet`/`planula`/`planococcus`). Verified 0 issues via `audit-roots.mjs`. | 402 | ✅ Completed |
| 2026-10-03 03:00 | Milestone 5 | **Pilot Completed:** Curated Latin roots `Cluster Action` / `Dashboard — act` (120 word notes). Added offline `local_dictionary.db` (303,443 entries: WordNet 3.1 + Webster's 1913), resolved circular definition feedback on `interactivity` and 15 similar derivatives, added programmatic anti-tautology validation to `audit-latin-roots.mjs`. Verified 120/120 pristine (0 issues). Vault re-indexed in 1.46s. | 120 | ✅ Pilot Verified |

---

## Milestone 5: Latin Roots Master Implementation Plan (Strict Multi-Source MCP & Provenance Verification Architecture)

### 1. Executive Summary & Core Quality Mandates

Following the verified pilot on **`Dashboard — act`** (120 words, 100% pristine, 0 issues), this architecture governs the curation of the entire Latin roots section across all clusters, dashboards, and words:
- **Total Section Scope:** **30,611 word notes** across **782 dashboards** grouped into **60 thematic clusters**.
- **Three Absolute User Directives:**
  1. **Authoritative Multi-Source Definitions:** Every word must feature two substantive, non-circular definitions cross-verified across `wikipedia`, `Dictionary-MCP`, `crw` MCP, `philosophy` MCP, and the offline `local_dictionary.db`.
  2. **Strict Literary Phrases Sourcing (Zero-Synthetic Mandate):** Real, attested sentences exclusively from authorized MCPs and canonical corpora. Absolute ban on synthetic placeholders, `{w}` template interpolation, and fabricated quotes.
  3. **End-to-End Dual Provenance Verification:** Both definitions and quotations must possess traceable provenance from authoritative sources and pass automated zero-tolerance programmatic audit gates prior to Git checkpointing.

---

### 2. Multi-Source Definition Architecture

Every individual word entry must have two distinct, high-quality definitions in `> [!book] 📖 Definitions & Semantic Range`:
1. **Primary Definition (Lexical / Standard Consensus):** The authoritative core dictionary definition written in clear, accessible modern English.
2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic):** Specialized domain usage (biochemical, anatomical, legal, philosophical, grammatical), figurative sense, or contextual nuance.

#### Multi-Source Sourcing & Role Matrix

| Source / Tool | Specific Role & Sourcing Scope | Verification Standard |
| :--- | :--- | :--- |
| **`Dictionary-MCP`** | Merriam-Webster Collegiate lexicon queries for primary definitions, inflected forms, and grammatical classifications. | Authoritative contemporary English standard; verified against lexical consensus. |
| **`wikipedia` MCP** | `get_summary`, `get_article`, `extract_key_facts` for specialized scientific, anatomical, botanical, legal, and taxonomic Latin derivatives. | Encyclopedic depth; extracts factual definitions for technical and domain terms. |
| **`crw` MCP / CLI** | Scrapes Wiktionary, Merriam-Webster, Oxford/Collins, and Online Etymology Dictionary (`etymonline.com`). | Unindexed or rare morphological derivatives; verifies etymological development and register. |
| **`philosophy` MCP** | Accesses Stanford Encyclopedia of Philosophy (SEP) and Internet Encyclopedia of Philosophy (IEP) for epistemological, ethical, and legal terms (*veritas*, *ratio*, *cognitio*, *lex*, *causa*). | Peer-reviewed academic definitions for conceptual, metaphysical, and philosophical roots. |
| **`local_dictionary.db`** | Offline SQLite database (303,443 entries) combining Princeton WordNet 3.1 and Webster's 1913 Unabridged Dictionary. | Zero-latency ($< 1\text{ ms}$) baseline; provides numbered senses and historical nuance. |

#### Anti-Circular & Anti-Tautology Verification Rules
- **Ban on Formulaic Tautologies:** Reject definitions matching `the (quality|state|condition|act|process|fact) of being <root/word>`.
- **Substantive Minimum Length:** Both Primary and Secondary definitions must be $\ge 25$ characters long.
- **Sense Differentiation:** Jaccard token similarity between Primary and Secondary definitions must be $< 0.70$.

---

### 3. Strict MCP Sourcing for Authentic Literary Phrases (Zero-Synthetic Mandate)

Every word note must contain **exactly 3 authentic quotations** from 3 distinct, real authors inside `> [!quote] 💬 Contextual Usage & Authentic Quotations`. Citations are strictly drawn from these authorized sources:

| Source / Tool | Authorized Sourcing Mechanism | Scope & Classical Literature Covered |
| :--- | :--- | :--- |
| **`project-gutenberg` MCP** | `search_books`, `fetch_book_text`, `get_passage`, `list_passages` | Canonical classical English literature: Shakespeare, Austen, Dickens, Melville, Milton, George Eliot, Thomas Hardy, Joseph Conrad, Bram Stoker, H. G. Wells, etc. |
| **`crw` MCP / CLI** | `crw_scrape`, `crw_extract` targeting Wiktionary human-curated citation archives (`Citations:<word>`) | Attested historical citations cataloged by lexicographers from 16th–21st century books, essays, and journals, complete with author, work, date, and page number. |
| **`philosophy` MCP** | `sep_get_section`, `sep_get_entry` | Authentic analytical citations and quotations from foundational thinkers (Locke, Mill, Bacon, Hume, Kant, Aristotle, Descartes, William James). |
| **`wikipedia` MCP** | `get_article`, `extract_key_facts` | Historical documentation, scientific treatises, landmark speeches, and legal cases. |
| **`citation_corpus.db`** | Offline SQLite FTS5 database (213,370 verified sentences) | Full-text indexed canonical public domain works (Darwin's *Origin of Species*, Smith's *Wealth of Nations*, Gibbon's *Decline and Fall*, etc.). |

#### Citation Quality Rules
1. **Verbatim Headword:** Target word must appear verbatim, highlighted with bold markdown (`**word**`).
2. **Author Diversity:** All 3 authors must be distinct individuals (`len(set(authors)) == 3`).
3. **Identifiable Real Work:** Every quote must cite a specific published work in italics (e.g. `*Pride and Prejudice*`, `*The Descent of Man*`). No generic labels like `*Academic Lexicon*` or `*Classic Literature*`.
4. **Zero Synthetic Text:** No template interpolation (`{w}`), mad-libs, or LLM-fabricated quotes.

---

### 4. Canonical Word Note Structure

Every word note across all 782 dashboards strictly adheres to this structure:

```markdown
---
latin_root: "[[Dashboard — <root>]]"
cluster: "[[Cluster <Name>]]"
status: unread
---
# <word>

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
> 1. **Primary Definition (Lexical / Standard Consensus)**: <Substantive core consensus definition, non-circular>
> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: <Distinct secondary, domain, or encyclopedic definition>

> [!quote] 💬 Contextual Usage & Authentic Quotations
> - 📜 **<Author 1> (*<Work 1>*):** *"<Verbatim authentic sentence with **<word>** bolded>"*
> - 📜 **<Author 2> (*<Work 2>*):** *"<Verbatim authentic sentence with **<word>** bolded>"*
> - 📜 **<Author 3> (*<Work 3>*):** *"<Verbatim authentic sentence with **<word>** bolded>"*
```

---

### 5. Execution Waves & Thematic Breakdown

The 60 Latin clusters are structured into 10 cohesive waves:

| Wave | Thematic Scope | Clusters Included | Dashboards | Word Count |
| :---: | :--- | :--- | :---: | :---: |
| **Wave 1** | **Action, Labor & State (Core)** | `Cluster Action`, `Cluster Action & State` | 46 | 2,344 |
| **Wave 2** | **Motion, Speed & Carrying** | `Cluster Motion`, `Cluster Movement & Speed`, `Cluster Carrying` | 57 | 2,772 |
| **Wave 3** | **Mind, Thought & Emotion** | `Cluster Mind & Knowledge`, `Cluster Thought`, `Cluster Emotion`, `Cluster Faith` | 46 | 2,054 |
| **Wave 4** | **Speech, Language & Communication** | `Cluster Speech & Communication`, `Cluster Speech`, `Cluster Asking & Seeking`, `Cluster Writing` | 49 | 1,942 |
| **Wave 5** | **Society, Law, Justice & Virtue** | `Cluster Society`, `Cluster Law`, `Cluster Law, Justice & Feudal`, `Cluster War`, `Cluster Virtue` | 69 | 2,549 |
| **Wave 6** | **Life, Body & Clinical Medicine** | `Cluster Life`, `Cluster Body`, `Cluster Anatomy & Clinical Medicine`, `Cluster Body & State`, `Cluster Death` | 75 | 2,107 |
| **Wave 7** | **Nature, Biology, Plants & Animals** | `Cluster Nature`, `Cluster Botany, Minerals & Elements`, `Cluster Animal & Plant`, `Cluster Animal Adjectives & Biological`, `Cluster Food, Eating & Drink` | 89 | 2,589 |
| **Wave 8** | **Structure, Space & Environment** | `Cluster Structure`, `Cluster Space & Environment`, `Cluster Building & Dwelling`, `Cluster Objects & Forms`, `Cluster Clothing & Covering` | 68 | 2,048 |
| **Wave 9** | **Perception, Light, Color & Senses** | `Cluster Light`, `Cluster Color & Appearance`, `Cluster Fire, Heat & Ash`, `Cluster Senses & Perception`, `Cluster Sight`, `Cluster Touch`, `Cluster Sleep, Rest & Stillness`, `Cluster Weight` | 70 | 1,933 |
| **Wave 10** | **Placing, Separation, Measures & Hybrids** | `Cluster Placing`, `Cluster Separation & Loosening`, `Cluster Number & Measure`, `Cluster Quantity`, `Cluster Order`, `Cluster Turning`, `Cluster Holding`, `Cluster Binding`, `Cluster Truth, Deception & Error`, `Cluster Power`, `Cluster Good & Bad`, `Cluster Destruction`, `Cluster Equality`, `Cluster Sacred`, `Cluster Sending`, `Cluster Giving & Receiving`, `Cluster General`, `Cluster Greek-Latin Hybrid` | 213 | 10,273 |
| **Total** | **All Latin Roots Section** | **60 Clusters** | **782** | **30,611** |

---

### 6. Automated Quality Verification Gates

Before any cluster is considered complete and committed to Git, it must pass all 7 automated quality gates via [`main app/scripts/audit-latin-roots.mjs`](file:///C:/Users/user/Desktop/Vocab%20app/main%20app/scripts/audit-latin-roots.mjs):

- [ ] **Gate 1: Frontmatter Integrity** — Valid YAML frontmatter containing `latin_root: "[[...]]"`, `cluster: "[[...]]"`, and `status: unread`.
- [ ] **Gate 2: Apple Glide Toggle Placement** — Interactive DataviewJS toggle positioned directly above `> [!book]` callout.
- [ ] **Gate 3: Definition Substantiveness** — Primary definition $\ge 25$ characters, derived from authoritative dictionary consensus.
- [ ] **Gate 4: Non-Circular & Non-Duplication** — Zero formulaic tautologies (*"quality/state of being..."*); Secondary definition distinct from Primary ($Jaccard < 0.70$).
- [ ] **Gate 5: Authentic Quotations** — Exactly 3 real citations from 3 distinct historical, literary, scientific, or philosophical authors with verified works (`project-gutenberg`, `crw` Wiktionary citations, `philosophy` MCP, canonical texts).
- [ ] **Gate 6: Headword Bolding** — Target headword explicitly bolded (`**word**`) in all 3 citations.
- [ ] **Gate 7: Automated Audit Clean Bill** — Exit code 0 from [`audit-latin-roots.mjs`](file:///C:/Users/user/Desktop/Vocab%20app/main%20app/scripts/audit-latin-roots.mjs) (`Problem words: 0`).
