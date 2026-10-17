/**
 * Full-Fidelity Obsidian DataviewJS + App + Meta Bind Runtime Engine
 * Executes real vault ```dataviewjs blocks and Meta Bind INPUT[...] widgets
 * against the live 52,000+ note vault index with instant UI reactivity.
 */

export class DataviewLink {
  constructor(path, display, resolvedPath) {
    const rawStr = String(path || '').replace(/^\[\[|\]\]$/g, '').trim();
    // Normalize escaped pipes `\|` -> `|`
    const cleanRaw = rawStr.replace(/\\\|/g, '|');
    const pipeIdx = cleanRaw.indexOf('|');
    const targetPart = pipeIdx !== -1 ? cleanRaw.slice(0, pipeIdx) : cleanRaw;
    const aliasPart = pipeIdx !== -1 ? cleanRaw.slice(pipeIdx + 1) : '';

    const cleanTarget = targetPart.split('#')[0].replace(/\\+$/, '').trim().replace(/\\/g, '/');
    const fileName = cleanTarget.split('/').pop().replace(/\.md$/i, '');

    this.path = resolvedPath || (cleanTarget.endsWith('.md') ? cleanTarget : `${cleanTarget}.md`);
    this.fileName = fileName;
    this.display = display || aliasPart || fileName;
    this.type = 'file';
  }

  toHTML() {
    const escPath = escapeAttr(this.path);
    const escDisplay = escapeHtml(this.display || this.fileName);
    return `<a class="internal-link" data-href="${escPath}" href="/?note=${encodeURIComponent(this.path)}">${escDisplay}</a>`;
  }

  toString() {
    return this.toHTML();
  }
}

export class DataArray extends Array {
  static fromArray(arr) {
    const da = new DataArray();
    if (arr && (Array.isArray(arr) || typeof arr[Symbol.iterator] === 'function')) {
      for (const item of arr) {
        da.push(item);
      }
    }
    return da;
  }

  where(predicate) {
    const out = new DataArray();
    for (let i = 0; i < this.length; i++) {
      try {
        if (predicate(this[i], i, this)) out.push(this[i]);
      } catch {
        // ignore predicate error on individual item
      }
    }
    return out;
  }

  filter(predicate) {
    return this.where(predicate);
  }

  map(fn) {
    const out = new DataArray();
    for (let i = 0; i < this.length; i++) {
      try {
        out.push(fn(this[i], i, this));
      } catch {
        out.push(undefined);
      }
    }
    return out;
  }

  first() {
    return this[0];
  }

  last() {
    return this[this.length - 1];
  }

  distinct() {
    return DataArray.fromArray(Array.from(new Set(this)));
  }

  groupBy(keyFn) {
    const map = new Map();
    for (let i = 0; i < this.length; i++) {
      const item = this[i];
      let key;
      try {
        key = typeof keyFn === 'function' ? keyFn(item) : item[keyFn];
      } catch {
        key = undefined;
      }
      if (!map.has(key)) map.set(key, new DataArray());
      map.get(key).push(item);
    }
    const result = new DataArray();
    for (const [key, rows] of map.entries()) {
      result.push({ key, rows });
    }
    return result;
  }

  sort(keyOrComparator, direction = 'asc') {
    if (typeof keyOrComparator === 'function' && keyOrComparator.length >= 2) {
      super.sort(keyOrComparator);
      return this;
    }
    const copy = DataArray.fromArray(this);
    const dir = String(direction).toLowerCase() === 'desc' ? -1 : 1;
    const extractVal = typeof keyOrComparator === 'function'
      ? keyOrComparator
      : (item) => {
          if (!keyOrComparator) return item;
          const parts = String(keyOrComparator).split('.');
          let v = item;
          for (const p of parts) {
            if (v == null) return undefined;
            v = v[p];
          }
          return v;
        };

    Array.prototype.sort.call(copy, (a, b) => {
      try {
        const va = extractVal(a);
        const vb = extractVal(b);
        return String(va ?? '').localeCompare(String(vb ?? ''), undefined, { numeric: true }) * dir;
      } catch {
        return 0;
      }
    });
    return copy;
  }

  limit(count) {
    return DataArray.fromArray(this.slice(0, count));
  }

  array() {
    return Array.from(this);
  }

  get values() {
    return this;
  }
}

function escapeHtml(str) {
  return String(str ?? '')
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;');
}

function escapeAttr(str) {
  return escapeHtml(str).replace(/"/g, '&quot;');
}

/**
 * VaultRuntime manages the hydrated page objects and provides `dv`, `app`, and `Notice`
 */
export class VaultRuntime {
  constructor(vaultController) {
    this.controller = vaultController;
    this.pagesByPath = new Map();
    this.pagesByName = new Map();
    this.pagesByFolder = new Map();
    this.allHydratedPages = new DataArray();
  }

  /**
   * Hydrate compact index entries (`{ p, s, t, c, lr, gr, sec, tg, al, css, b, bi, by }`)
   * into rich Dataview page objects.
   */
  hydrateIndex(rawPages, localStatusOverrides = {}) {
    this.pagesByPath.clear();
    this.pagesByName.clear();
    this.pagesByFolder.clear();
    this.allHydratedPages = new DataArray();

    // Pass 1: register path lookup by filename for fast wikilink resolution
    for (let i = 0; i < rawPages.length; i++) {
      const rp = rawPages[i];
      const normPath = rp.p.replace(/\\/g, '/');
      const lastSlash = normPath.lastIndexOf('/');
      const fileName = normPath.slice(lastSlash + 1).replace(/\.md$/i, '');
      if (!this.pagesByName.has(fileName.toLowerCase())) {
        this.pagesByName.set(fileName.toLowerCase(), normPath);
      }
      // Also register aliases
      if (rp.al) {
        for (const alias of rp.al) {
          const lowerAlias = String(alias).toLowerCase();
          if (!this.pagesByName.has(lowerAlias)) {
            this.pagesByName.set(lowerAlias, normPath);
          }
        }
      }
    }

    // Pass 2: build full Dataview page objects
    for (let i = 0; i < rawPages.length; i++) {
      const rp = rawPages[i];
      const normPath = rp.p.replace(/\\/g, '/');
      const lastSlash = normPath.lastIndexOf('/');
      const folder = lastSlash !== -1 ? normPath.slice(0, lastSlash) : '';
      const fileName = normPath.slice(lastSlash + 1).replace(/\.md$/i, '');

      const fileLink = new DataviewLink(normPath, fileName, normPath);

      const page = {
        file: {
          name: fileName,
          path: normPath,
          folder: folder,
          link: fileLink,
          ext: 'md'
        }
      };

      // Status (respect local overrides first, then frontmatter `s`)
      const overrideStatus = localStatusOverrides[normPath];
      if (overrideStatus !== undefined) {
        page.status = overrideStatus;
      } else if (rp.s !== undefined) {
        page.status = rp.s;
      }

      if (rp.t !== undefined) page.type = rp.t;
      if (rp.sec !== undefined) page.section = rp.sec;
      if (rp.tg !== undefined) page.tags = rp.tg;
      if (rp.al !== undefined) page.aliases = rp.al;
      if (rp.css !== undefined) page.cssclasses = rp.css;
      if (rp.b !== undefined) page.banner = rp.b;
      if (rp.bi !== undefined) page.banner_icon = rp.bi;
      if (rp.by !== undefined) page.banner_y = rp.by;

      if (rp.c !== undefined) {
        page.cluster = this.parseFrontmatterLink(rp.c, folder);
      }
      if (rp.lr !== undefined) {
        page.latin_root = this.parseFrontmatterLink(rp.lr, folder);
      }
      if (rp.gr !== undefined) {
        page.greek_root = this.parseFrontmatterLink(rp.gr, folder);
      }

      this.pagesByPath.set(normPath, page);
      this.allHydratedPages.push(page);

      const topFolder = folder.split('/')[0] || '';
      if (topFolder) {
        if (!this.pagesByFolder.has(topFolder)) {
          this.pagesByFolder.set(topFolder, new DataArray());
        }
        this.pagesByFolder.get(topFolder).push(page);
      }
    }
  }

  parseFrontmatterLink(rawVal, contextFolder = '') {
    const str = String(rawVal || '').trim();
    const match = str.match(/^\[\[([^\]|]+)(?:\\?\|([^\]]+))?\]\]$/);
    const targetName = match ? match[1].replace(/\\+$/, '').trim() : str;
    const display = match && match[2] ? match[2].trim() : targetName.split('/').pop().replace(/\.md$/i, '');

    // Resolve path in the same folder or globally
    let resolved = this.resolveLinkPath(targetName, contextFolder);
    return new DataviewLink(targetName, display, resolved);
  }

  resolveLinkPath(linkText, sourcePath = '') {
    if (!linkText) return '00 Language Hub.md';
    let clean = String(linkText)
      .replace(/^\[\[|\]\]$/g, '')
      .replace(/\\\|/g, '|')
      .split('|')[0]
      .split('#')[0]
      .trim()
      .replace(/\\+$/, '')
      .replace(/\\/g, '/')
      .replace(/^\/+|\/+$/g, '');

    if (!clean) return sourcePath || '00 Language Hub.md';

    // 1. Direct path match with or without .md
    const withMd = clean.endsWith('.md') ? clean : `${clean}.md`;
    if (this.pagesByPath.has(withMd)) return withMd;
    if (this.pagesByPath.has(clean)) return clean;

    // 2. Relative to source folder
    if (sourcePath) {
      const srcFolder = sourcePath.includes('/')
        ? sourcePath.slice(0, sourcePath.lastIndexOf('/'))
        : sourcePath;
      const parts = srcFolder.split('/');
      for (let depth = parts.length; depth >= 1; depth--) {
        const prefix = parts.slice(0, depth).join('/');
        const candidate = `${prefix}/${withMd}`;
        if (this.pagesByPath.has(candidate)) return candidate;
        // Also check folder note candidate: prefix/clean/clean.md
        const folderNoteCandidate = `${prefix}/${clean}/${clean}.md`;
        if (this.pagesByPath.has(folderNoteCandidate)) return folderNoteCandidate;
      }
    }

    // 3. Global filename or alias lookup
    const baseName = clean.split('/').pop().replace(/\.md$/i, '').toLowerCase();
    if (this.pagesByName.has(baseName)) {
      return this.pagesByName.get(baseName);
    }

    // 4. Top-level folder note check (e.g. "Latin roots" -> "Latin roots/Latin roots.md")
    const topFolderNote = `${clean}/${clean}.md`;
    if (this.pagesByPath.has(topFolderNote)) return topFolderNote;

    return withMd;
  }

  /**
   * Execute a DataviewJS code string inside a specific DOM container for a given note path
   */
  executeDataviewJS(code, containerEl, currentFilePath) {
    containerEl.innerHTML = '';
    const self = this;
    const safePath = String(currentFilePath || '00 Language Hub.md').replace(/\\/g, '/');
    const currentPage = this.pagesByPath.get(safePath) || {
      file: {
        name: safePath.split('/').pop().replace(/\.md$/i, ''),
        path: safePath,
        folder: safePath.includes('/') ? safePath.slice(0, safePath.lastIndexOf('/')) : '',
        link: new DataviewLink(safePath, '', safePath)
      },
      status: 'unread'
    };

    const dv = {
      container: containerEl,
      currentFilePath: safePath,
      current() {
        return currentPage;
      },
      pages(query = '') {
        const q = String(query || '').trim().replace(/^['"]|['"]$/g, '').replace(/\\/g, '/').replace(/^\/+|\/+$/g, '');
        if (!q) return self.allHydratedPages;
        if (q.startsWith('#')) {
          const tag = q.slice(1).toLowerCase();
          return self.allHydratedPages.where(p => Array.isArray(p.tags) && p.tags.some(t => String(t).toLowerCase() === tag));
        }
        // Fast path if querying a top-level discipline folder (case-insensitive check)
        if (!q.includes('/')) {
          if (self.pagesByFolder.has(q)) {
            return self.pagesByFolder.get(q);
          }
          const lowerQ = q.toLowerCase();
          for (const [folderName, folderPages] of self.pagesByFolder.entries()) {
            if (folderName.toLowerCase() === lowerQ) return folderPages;
          }
        }
        // Subfolder prefix match (defensive with optional chaining)
        const prefix = `${q}/`;
        const topFolder = q.split('/')[0];
        let pool = self.pagesByFolder.get(topFolder);
        if (!pool) {
          const lowerTop = topFolder.toLowerCase();
          for (const [folderName, folderPages] of self.pagesByFolder.entries()) {
            if (folderName.toLowerCase() === lowerTop) {
              pool = folderPages;
              break;
            }
          }
        }
        if (!pool) pool = self.allHydratedPages;
        const lowerQ = q.toLowerCase();
        const lowerPrefix = prefix.toLowerCase();
        return pool.where(p => {
          const f = p?.file?.folder;
          if (!f) return false;
          return f === q || f.startsWith(prefix) || f.toLowerCase() === lowerQ || f.toLowerCase().startsWith(lowerPrefix);
        });
      },
      fileLink(path, embed = false, display = '') {
        const resolved = self.resolveLinkPath(path, safePath);
        return new DataviewLink(path, display, resolved);
      },
      paragraph(content) {
        const div = document.createElement('div');
        div.className = 'dv-paragraph';
        appendCellContent(div, content, self, safePath);
        containerEl.appendChild(div);
        return div;
      },
      span(content) {
        const sp = document.createElement('span');
        appendCellContent(sp, content, self, safePath);
        containerEl.appendChild(sp);
        return sp;
      },
      header(level, content) {
        const h = document.createElement(`h${Math.min(Math.max(Number(level) || 2, 1), 6)}`);
        appendCellContent(h, content, self, safePath);
        containerEl.appendChild(h);
        return h;
      },
      el(tag, content, attrs = {}) {
        const el = document.createElement(tag || 'div');
        if (attrs.cls) el.className = Array.isArray(attrs.cls) ? attrs.cls.join(' ') : attrs.cls;
        if (attrs.attr) {
          for (const [k, v] of Object.entries(attrs.attr)) el.setAttribute(k, v);
        }
        appendCellContent(el, content, self, safePath);
        containerEl.appendChild(el);
        return el;
      },
      list(items) {
        const ul = document.createElement('ul');
        ul.className = 'dataview list-view-ul';
        const listItems = Array.isArray(items) || (items && typeof items[Symbol.iterator] === 'function')
          ? Array.from(items)
          : (items !== null && items !== undefined ? [items] : []);
        for (const item of listItems) {
          const li = document.createElement('li');
          appendCellContent(li, item, self, safePath);
          ul.appendChild(li);
        }
        containerEl.appendChild(ul);
        return ul;
      },
      table(headers, rows) {
        const wrapper = document.createElement('div');
        wrapper.className = 'table-scroll-wrapper';
        const table = document.createElement('table');
        table.className = 'dataview table-view-table';

        if (headers && (Array.isArray(headers) || typeof headers[Symbol.iterator] === 'function')) {
          const thead = document.createElement('thead');
          const tr = document.createElement('tr');
          for (const h of headers) {
            const th = document.createElement('th');
            appendCellContent(th, h, self, safePath);
            tr.appendChild(th);
          }
          thead.appendChild(tr);
          table.appendChild(thead);
        }

        const tbody = document.createElement('tbody');
        const rowList = Array.isArray(rows) || (rows && typeof rows[Symbol.iterator] === 'function')
          ? Array.from(rows)
          : [];
        for (const row of rowList) {
          if (!row) continue;
          const tr = document.createElement('tr');
          const cellList = Array.isArray(row) || (row && typeof row[Symbol.iterator] === 'function')
            ? Array.from(row)
            : [row];
          for (const cell of cellList) {
            const td = document.createElement('td');
            appendCellContent(td, cell, self, safePath);
            tr.appendChild(td);
          }
          tbody.appendChild(tr);
        }
        table.appendChild(tbody);
        wrapper.appendChild(table);
        containerEl.appendChild(wrapper);
        return table;
      }
    };

    // Mock Obsidian `app` object for `app.vault`, `app.fileManager.processFrontMatter`, `app.workspace.openLinkText`
    const app = {
      vault: {
        getAbstractFileByPath(filePath) {
          const resolved = self.resolveLinkPath(filePath, safePath);
          return { path: resolved, name: resolved.split('/').pop() };
        }
      },
      fileManager: {
        async processFrontMatter(file, mutatorFn) {
          if (!file || !file.path) return;
          const page = self.pagesByPath.get(file.path);
          const fmProxy = { status: page ? page.status || 'unread' : 'unread' };
          mutatorFn(fmProxy);
          if (page && fmProxy.status !== undefined) {
            page.status = fmProxy.status;
          }
          if (self.controller) {
            if (typeof self.controller.updateNoteFrontmatter === 'function') {
              await self.controller.updateNoteFrontmatter(file.path, fmProxy, false);
            } else if (typeof self.controller.setStatus === 'function' && fmProxy.status) {
              self.controller.setStatus(file.path, fmProxy.status);
            }
          }
        }
      },
      workspace: {
        openLinkText(linkText, sourcePath, newLeaf = false) {
          const resolved = self.resolveLinkPath(linkText, sourcePath || safePath);
          if (self.controller) {
            if (typeof self.controller.openNote === 'function') {
              self.controller.openNote(resolved, { newTab: Boolean(newLeaf) });
            } else if (typeof self.controller.openOriginalNoteView === 'function') {
              self.controller.openOriginalNoteView(resolved);
            } else if (typeof self.controller.openHomeSection === 'function') {
              self.controller.openHomeSection(resolved);
            }
          }
        }
      }
    };

    class Notice {
      constructor(message, duration = 2600) {
        if (self.controller) {
          if (typeof self.controller.showNotice === 'function') {
            self.controller.showNotice(message, duration);
          } else if (typeof self.controller.showToast === 'function') {
            self.controller.showToast(message);
          }
        }
      }
    }

    const defaultMakeAppleToggle = (rawStatus, filePath, fileName) => {
      const states = [
        { key: 'unread', label: 'unread', cls: 'unread', p: 'p0' },
        { key: 'learning', label: 'learning', cls: 'learning', p: 'p1' },
        { key: 'learned', label: 'learned', cls: 'learned', p: 'p2' }
      ];
      const normalized = String(rawStatus || '').toLowerCase().trim();
      let curIdx = states.findIndex(s => s.key === normalized);
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
        if (e && e.stopPropagation) e.stopPropagation();
        curIdx = (curIdx + 1) % 3;
        const nextState = states[curIdx];
        const halo = track.querySelector('.halo-c');
        if (halo) halo.className = 'halo-c ' + nextState.p;
        label.className = 'label ' + nextState.cls;
        label.textContent = nextState.label;

        const cleanPath = String(filePath || '').replace(/\\/g, '/');
        const tFile = app.vault.getAbstractFileByPath(cleanPath);
        if (tFile) {
          await app.fileManager.processFrontMatter(tFile, (fm) => {
            fm.status = nextState.key;
          });
          new Notice('Updated ' + (fileName || tFile.name) + ' ➔ ' + nextState.label);
        }
      });

      return toggle;
    };

    try {
      const safeCode = code
        .replace(/font-family:\s*'Cormorant Garamond'/g, 'font-family:"Cormorant Garamond"')
        .replace(/dv\.paragraph\('\r?\n([\s\S]*?)\r?\n'\);/g, (_, inner) => `dv.paragraph('${inner.replace(/\r?\n/g, ' ')}');`);
      
      const AsyncFunction = Object.getPrototypeOf(async function(){}).constructor;
      const fn = new AsyncFunction('dv', 'app', 'Notice', 'makeAppleToggle', safeCode);
      const res = fn(dv, app, Notice, defaultMakeAppleToggle);
      if (res && typeof res.catch === 'function') {
        res.catch(err => {
          console.error(`DataviewJS async execution error in ${safePath}:`, err);
        });
      }

      // Post-process any injected #apple-toggle-css so it never overrides light/dark theme variables
      const injectedStyle = document.getElementById('apple-toggle-css');
      if (injectedStyle) {
        injectedStyle.remove();
      }
    } catch (err) {
      console.error(`DataviewJS execution error in ${safePath}:`, err);
      const errBox = document.createElement('div');
      errBox.className = 'callout';
      errBox.setAttribute('data-callout', 'warning');
      errBox.innerHTML = `<div class="callout-title"><span class="callout-icon">⚠️</span><span class="callout-title-inner">DataviewJS Notice</span></div><div class="callout-content"><p>${escapeHtml(err.message)}</p></div>`;
      containerEl.appendChild(errBox);
    }
  }
}

function appendCellContent(targetEl, content, runtime, sourcePath) {
  if (content === null || content === undefined) return;
  if (content instanceof Node) {
    targetEl.appendChild(content);
    return;
  }
  if (content instanceof DataviewLink) {
    targetEl.innerHTML = content.toHTML();
    return;
  }
  const str = String(content);
  // Also convert any inline [[wikilinks]] inside Dataview strings (handling escaped pipes \|)
  const withLinks = str.replace(/\[\[([^\]|#\\]+)\\?(?:#([^\]|\\]+)\\?)?(?:\\?\|([^\]]+))?\]\]/g, (_, target, hash, alias) => {
    const cleanTarget = target.replace(/\\+$/, '').trim();
    const cleanHash = hash ? hash.replace(/\\+$/, '').trim() : '';
    const resolved = runtime ? runtime.resolveLinkPath(cleanTarget, sourcePath) : cleanTarget;
    const label = alias ? alias.trim() : cleanTarget.split('/').pop().replace(/\.md$/i, '');
    return `<a class="internal-link" data-href="${escapeAttr(resolved)}" ${cleanHash ? `data-heading="${escapeAttr(cleanHash)}"` : ''} href="/?note=${encodeURIComponent(resolved)}">${escapeHtml(label)}</a>`;
  });
  targetEl.innerHTML = withLinks;
}
