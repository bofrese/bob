/**
 * overview.js — Markdown → Reveal.js slide builder
 *
 * Syntax summary:
 *   # Title          → title slide (special first-slide layout)
 *   > subtitle       → subtitle on title slide
 *   > tagline        → tagline below hr (second > line, optional)
 *   ## Heading       → slide heading
 *   {.center}        → center-align the slide (appended to heading line)
 *   {.left}          → left-align with padding
 *   {.warn}          → heading rendered in warn colour
 *   {.warn-title}    → italic em inside heading rendered warn
 *   {.aha-slide}     → aha badge extracted before heading text
 *   {.question}      → large white heading, warn-coloured strong
 *   {.thesis}        → large accent-coloured heading
 *   {.closing}       → closing slide link styling
 *   ---              → horizontal slide break (new section)
 *   ===              → vertical sub-slide break
 *   :::component     → block directive (pillars|journey|compare|ftree|layers|bars|cards|pipeline)
 *   :::              → end of block directive
 *   *…*              → em   (standard md)
 *   **…**            → strong (standard md)
 *   `…`              → code  (standard md)
 *   [text](url)      → link  (standard md)
 */

(function () {
  'use strict';

  // ── Inline markdown: strong, em, code, links ──────────────────────
  function inlineMd(text) {
    // links first (before backtick swallows the URL)
    text = text.replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2">$1</a>');
    // code spans
    text = text.replace(/`([^`]+)`/g, '<code>$1</code>');
    // bold  (before italic so **x** isn't eaten as *…*)
    text = text.replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>');
    // italic
    text = text.replace(/\*(.+?)\*/g, '<em>$1</em>');
    return text;
  }

  // ── Paragraph block: turns text lines into <p> tags ───────────────
  function paragraphs(lines) {
    // split on blank lines → paragraph groups
    const groups = [];
    let cur = [];
    lines.forEach(l => {
      if (l.trim() === '') {
        if (cur.length) { groups.push(cur); cur = []; }
      } else {
        cur.push(l);
      }
    });
    if (cur.length) groups.push(cur);

    return groups.map(g => {
      // if the group is a single h3 line, render as <h3>
      if (g.length === 1 && g[0].startsWith('### ')) {
        return '<h3>' + inlineMd(g[0].slice(4)) + '</h3>';
      }
      return '<p>' + g.map(l => inlineMd(l)).join('<br>') + '</p>';
    }).join('\n');
  }

  // ── Component renderers ────────────────────────────────────────────

  function renderPillars(lines) {
    // each line: icon | title | description
    const items = lines.filter(l => l.includes('|')).map(l => {
      const [ico, title, desc] = l.split('|').map(s => s.trim());
      return `<div class="pillar">
        <span class="ico">${ico}</span>
        <h4>${inlineMd(title)}</h4>
        <p>${inlineMd(desc)}</p>
      </div>`;
    });
    return '<div class="pillars">' + items.join('') + '</div>';
  }

  function renderJourney(lines) {
    // each line: Day | /command | body text | optional saved-file line
    // body may span multiple lines if we join lines that don't start a new journey entry
    const entries = [];
    let current = null;
    lines.forEach(l => {
      if (l.trim() === '') return;
      // a new entry starts if it matches  Word | /cmd | …
      const match = l.match(/^(\w+)\s*\|\s*(`[^`]+`)\s*\|\s*(.*)$/);
      if (match) {
        if (current) entries.push(current);
        current = { day: match[1], cmd: match[2], body: match[3], saved: '' };
      } else if (current) {
        // continuation or saved line
        const savedMatch = l.match(/^(📄\s*.*)$/);
        if (savedMatch) {
          current.saved = savedMatch[1];
        } else {
          current.body += ' ' + l.trim();
        }
      }
    });
    if (current) entries.push(current);

    // if the body ends with  | 📄 …  split it out
    entries.forEach(e => {
      const idx = e.body.lastIndexOf('| 📄');
      if (idx !== -1) {
        e.saved = e.body.slice(idx + 2).trim();
        e.body  = e.body.slice(0, idx).trim();
      }
    });

    const rows = entries.map(e => {
      const savedHtml = e.saved
        ? `<p class="saved">${inlineMd(e.saved)}</p>` : '';
      return `<div class="jrow">
        <div class="jday"><span class="dn">${e.day.slice(0,3)}</span></div>
        <div class="jtxt">
          <h4>${inlineMd(e.cmd)}</h4>
          <p>${inlineMd(e.body)}</p>
          ${savedHtml}
        </div>
      </div>`;
    });
    return '<div class="journey">' + rows.join('') + '</div>';
  }

  function renderCompare(lines) {
    // two lines: bad | title | item1 | item2 …   and   good | title | …
    const boxes = lines.filter(l => l.includes('|')).map(l => {
      const parts = l.split('|').map(s => s.trim());
      const type  = parts[0]; // bad or good
      const title = parts[1];
      const items = parts.slice(2);
      const lis   = items.map(i => `<li>${inlineMd(i)}</li>`).join('');
      return `<div class="cbox ${type}">
        <h4>${inlineMd(title)}</h4>
        <ul>${lis}</ul>
      </div>`;
    });
    return '<div class="compare">' + boxes.join('') + '</div>';
  }

  function renderFtree(lines) {
    // Colour-code the file tree:
    //   folders (ending with /)           → .folder
    //   ← comments                        → .comment
    //   .md / highlighted paths            → .highlight
    //   everything else                    → .file
    // First line that has no tree chars and ends with no / might be a branch label
    const out = lines.map((line, i) => {
      if (line.trim() === '') return '';

      // detect branch label (first line, no tree prefix chars, no trailing /)
      if (i === 0 && !line.match(/^[\s│├└─]/) && !line.trim().endsWith('/')) {
        return `<span class="branch-label">${line.trim()}</span>`;
      }

      // split comment portion
      let comment = '';
      const commentIdx = line.indexOf('←');
      if (commentIdx !== -1) {
        comment = line.slice(commentIdx);
        line    = line.slice(0, commentIdx);
      }

      // colour the path portion token by token
      const coloured = line.replace(/([^\s│├└──]+)/g, (tok) => {
        if (tok.endsWith('/'))  return `<span class="folder">${tok}</span>`;
        if (tok.match(/\.\w+$/)) return `<span class="highlight">${tok}</span>`;
        if (tok === '…')        return `<span class="file">${tok}</span>`;
        return tok;
      });

      const commentHtml = comment
        ? ` <span class="comment">${comment}</span>` : '';

      return coloured + commentHtml;
    }).filter(Boolean).join('\n');

    return `<div class="ftree">${out}</div>`;
  }

  function renderLayers(lines) {
    // each line: Title | commands | type   (discovery|engineering|knowledge)
    const typeMap = { discovery: 'discovery', engineering: 'engineering', knowledge: 'knowledge' };
    const arrows  = [
      { dir: 'down', label: 'grounds' },
      { dir: 'down', label: 'produces' },
      { dir: 'up',   label: 'guides back to Engineering' }
    ];
    let arrowIdx = 0;
    const dataLines = lines.filter(l => l.includes('|'));
    const html = dataLines.map((l, i) => {
      const parts = l.split('|').map(s => s.trim());
      const title = parts[0];
      const cmds  = parts[1];
      const type  = typeMap[parts[2]] || 'engineering';

      let out = `<div class="lbox ${type}">
        <h4>${inlineMd(title)}</h4>
        <p>${inlineMd(cmds)}</p>
      </div>`;

      // insert arrow after each box except last
      if (arrowIdx < arrows.length && i < dataLines.length - 1) {
        const a = arrows[arrowIdx++];
        out += `<div class="larrow">↓ <em>${a.label}</em></div>`;
      }
      return out;
    }).join('');

    // append the final up-arrow
    const finalArrow = `<div class="larrow up">↑ <em>guides back to Engineering</em></div>`;
    return '<div class="layers">' + html + finalArrow + '</div>';
  }

  function renderBars(lines) {
    // each line: Label | value | heightPx | optional note
    const items = lines.filter(l => l.includes('|')).map(l => {
      const parts = l.split('|').map(s => s.trim());
      const label = parts[0];
      const value = parts[1];
      const height= parseInt(parts[2], 10) || 40;
      const note  = parts[3] || '';
      return `<div class="bcol">
        <div class="bar" style="height:${height}px"><span>${value}</span></div>
        <div class="lbl">${inlineMd(label)}${note ? '<br><em>' + note + '</em>' : ''}</div>
      </div>`;
    });
    return '<div class="bars">' + items.join('') + '</div>';
  }

  function renderCharimage(lines) {
    // line: src | caption | wide(optional)
    const parts = (lines.find(l => l.trim()) || '').split('|').map(s => s.trim());
    const src     = parts[0] || '';
    const caption = parts[1] || '';
    const wide    = (parts[2] || '').toLowerCase() === 'wide';
    const capHtml = caption ? `<p class="char-caption">${inlineMd(caption)}</p>` : '';
    return `<div class="charimage">
      <img src="${src}" alt="${caption}"${wide ? ' class="wide"' : ''}>
      ${capHtml}
    </div>`;
  }

  function renderCards(lines) {
    // each line: title | description
    // if exactly 3 cards and middle one looks like "dot.claude" or "shared…" → highlight middle
    const items = lines.filter(l => l.includes('|')).map(l => {
      const idx = l.indexOf('|');
      const title = l.slice(0, idx).trim();
      const desc  = l.slice(idx + 1).trim();
      return { title, desc };
    });

    const isSubmoduleLayout = items.length === 3 &&
      (items[1].title.toLowerCase().includes('dot.claude') ||
       items[1].desc.toLowerCase().includes('shared'));

    const html = items.map((it, i) => {
      const cls = (isSubmoduleLayout && i === 1) ? 'card highlight-card' : 'card';
      return `<div class="${cls}">
        <h4>${inlineMd(it.title)}</h4>
        <p>${inlineMd(it.desc)}</p>
      </div>`;
    }).join('');

    return '<div class="cards">' + html + '</div>';
  }

  function renderPipeline(lines) {
    // each line: icon | name | gate-label
    const items = lines.filter(l => l.includes('|')).map(l => {
      const [icon, name, gate] = l.split('|').map(s => s.trim());
      return { icon, name, gate };
    });
    const cols = items.length * 2 - 1;
    const colsDef = Array(cols).fill('auto').join(' ');
    // Row 1: phase boxes and arrows
    let row1 = '';
    items.forEach((item, i) => {
      row1 += `<div class="pbox">
        <span class="picon">${item.icon}</span>
        <span class="pname">${inlineMd(item.name)}</span>
      </div>`;
      if (i < items.length - 1) row1 += '<span class="parrow">→</span>';
    });
    // Row 2: gate labels with spacers for arrow columns
    let row2 = '';
    items.forEach((item, i) => {
      row2 += `<div class="pgate">${inlineMd(item.gate)}</div>`;
      if (i < items.length - 1) row2 += '<div></div>';
    });
    return `<div class="pipeline" style="grid-template-columns:${colsDef}">${row1}${row2}</div>`;
  }

  // Component registry
  const COMPONENTS = {
    pillars:   renderPillars,
    journey:   renderJourney,
    compare:   renderCompare,
    ftree:     renderFtree,
    layers:    renderLayers,
    bars:      renderBars,
    cards:     renderCards,
    pipeline:  renderPipeline,
    charimage: renderCharimage
  };

  // ── Slide attribute parser  {.center .warn .aha-slide …} ──────────
  function parseAttrs(headingText) {
    const match = headingText.match(/\{([^}]+)\}$/);
    const attrs = {};
    if (match) {
      match[1].split(/\s+/).forEach(a => {
        if (a.startsWith('.')) attrs[a.slice(1)] = true;
      });
      headingText = headingText.replace(/\s*\{[^}]+\}$/, '').trim();
    }
    return { text: headingText, attrs };
  }

  // ── Build a single <section> from slide data ──────────────────────
  function buildSlide(slide) {
    const { heading, attrs, bodyLines } = slide;
    const classes = [];
    if (attrs.center)     classes.push('slide-center');
    if (attrs.left)       classes.push('slide-left');
    if (attrs.warn)       classes.push('slide-warn');
    if (attrs['warn-title']) classes.push('slide-warn-title');
    if (attrs['aha-slide'])  classes.push('slide-aha');
    if (attrs.closing)    classes.push('slide-closing');
    if (attrs.question)   classes.push('slide-question');
    if (attrs.thesis)     classes.push('slide-thesis');

    let headingHtml = '';
    if (heading) {
      let hText = heading;
      // extract aha badge prefix  "💡 Aha #N — …"
      if (attrs['aha-slide']) {
        const ahaMatch = hText.match(/^(💡\s*Aha\s*#\d+)\s*[—–-]\s*(.*)$/);
        if (ahaMatch) {
          headingHtml = `<h2><span class="aha-badge">${ahaMatch[1]}</span> ${inlineMd(ahaMatch[2])}</h2>`;
        } else {
          headingHtml = `<h2>${inlineMd(hText)}</h2>`;
        }
      } else {
        headingHtml = `<h2>${inlineMd(hText)}</h2>`;
      }
    }

    // ── Parse body into segments: text paragraphs and component blocks ──
    let html = headingHtml;
    let i = 0;
    const textBuf = [];

    function flushText() {
      if (textBuf.length) {
        html += paragraphs(textBuf);
        textBuf.length = 0;
      }
    }

    while (i < bodyLines.length) {
      const line = bodyLines[i];
      const compMatch = line.match(/^:::(\w+)\s*$/);

      if (compMatch) {
        flushText();
        const compName = compMatch[1];
        const renderer = COMPONENTS[compName];
        // collect lines until closing :::
        const compLines = [];
        i++;
        while (i < bodyLines.length && bodyLines[i].trim() !== ':::') {
          compLines.push(bodyLines[i]);
          i++;
        }
        i++; // skip closing :::
        if (renderer) {
          html += renderer(compLines);
        }
      } else {
        textBuf.push(line);
        i++;
      }
    }
    flushText();

    // ── Closing slide: wrap "Created by" in .author ──────────────
    if (attrs.closing) {
      html = html.replace(
        /(<p><em>Created by .+?<\/em><\/p>)/,
        '<div class="author">$1</div>'
      );
    }

    // ── Entry-points: detect the "**Label** → `/cmd`" block pattern ──
    // Only fires when multiple lines each have <strong>…</strong> → <code>…</code>
    if (html.match(/<strong>[^<]+<\/strong>[^<]*→[^<]*<code>/g)?.length >= 3) {
      const wrapper = `<div class="entry-points">${html}</div>`;
      return `<section class="${classes.join(' ')}">${wrapper}</section>`;
    }

    return `<section class="${classes.join(' ')}">${html}</section>`;
  }

  // ── Main parse: markdown string → array of section groups ─────────
  function parse(md) {
    const lines = md.split('\n');
    // Top-level sections split by  ---
    // Sub-slides split by  ===
    // First # heading is the title slide

    const sections = []; // each section = array of sub-slides
    let currentSub  = { heading: null, attrs: {}, bodyLines: [] };
    let currentSec  = [];
    let titleSlide  = null;

    for (let i = 0; i < lines.length; i++) {
      const line = lines[i];

      // ── Title (# H1) ── only first occurrence
      if (!titleSlide && line.match(/^#\s+/)) {
        const title = line.replace(/^#\s+/, '').trim();
        // next non-blank line starting with > is subtitle
        let subtitle = '';
        let tagline  = '';
        let j = i + 1;
        while (j < lines.length && lines[j].trim() === '') j++;
        if (j < lines.length && lines[j].startsWith('>')) {
          subtitle = lines[j].replace(/^>\s*/, '').trim();
          j++;
          while (j < lines.length && lines[j].trim() === '') j++;
          if (j < lines.length && lines[j].startsWith('>')) {
            tagline = lines[j].replace(/^>\s*/, '').trim();
            j++;
          }
        }
        titleSlide = { title, subtitle, tagline };
        i = j - 1; // will be incremented by loop
        continue;
      }

      // ── Horizontal break ──
      if (line.trim() === '---') {
        if (currentSub.heading || currentSub.bodyLines.some(l => l.trim() !== '')) {
          currentSec.push(currentSub);
        }
        if (currentSec.length) sections.push(currentSec);
        currentSec  = [];
        currentSub  = { heading: null, attrs: {}, bodyLines: [] };
        continue;
      }

      // ── Vertical break ──
      if (line.trim() === '===') {
        if (currentSub.heading || currentSub.bodyLines.some(l => l.trim() !== '')) {
          currentSec.push(currentSub);
        }
        currentSub = { heading: null, attrs: {}, bodyLines: [] };
        continue;
      }

      // ── H2 heading (new slide heading) ──
      if (line.match(/^##\s+/) && !currentSub.heading) {
        const raw  = line.replace(/^##\s+/, '').trim();
        const { text, attrs } = parseAttrs(raw);
        currentSub.heading = text;
        currentSub.attrs   = attrs;
        continue;
      }

      // ── H3 heading (render as h3 inside body) ──
      if (line.match(/^###\s+/)) {
        currentSub.bodyLines.push('### ' + line.replace(/^###\s+/, '').trim());
        continue;
      }

      // ── Footer credit line  (starts with ---  + italic) at very end ──
      if (line.match(/^---$/) && i === lines.length - 1) continue;

      // ── Regular body line ──
      currentSub.bodyLines.push(line);
    }

    // flush remaining
    if (currentSub.heading || currentSub.bodyLines.some(l => l.trim() !== '')) currentSec.push(currentSub);
    if (currentSec.length) sections.push(currentSec);

    return { titleSlide, sections };
  }

  // ── Render title slide ─────────────────────────────────────────────
  function renderTitleSlide(ts) {
    if (!ts) return '';
    const taglineHtml = ts.tagline
      ? `<hr><p class="tagline">${inlineMd(ts.tagline)}</p>` : '';
    return `<section class="slide-center slide-title">
      <div class="title-badge">Claude Code Plugin</div>
      <h1>${inlineMd(ts.title)}</h1>
      <p class="subtitle">${inlineMd(ts.subtitle)}</p>
      ${taglineHtml}
    </section>`;
  }

  // ── Assemble reveal.js slide DOM ──────────────────────────────────
  function assemble(parsed) {
    const slidesDiv = document.querySelector('.reveal .slides');
    slidesDiv.innerHTML = '';

    // Title slide (no wrapping section needed — it's its own top-level section)
    slidesDiv.insertAdjacentHTML('beforeend', renderTitleSlide(parsed.titleSlide));

    // Sections
    parsed.sections.forEach(sec => {
      if (sec.length === 1) {
        // single slide — no vertical nesting needed
        slidesDiv.insertAdjacentHTML('beforeend', buildSlide(sec[0]));
      } else {
        // multiple sub-slides — wrap in a parent <section>
        let inner = '';
        sec.forEach(sub => { inner += buildSlide(sub); });
        slidesDiv.insertAdjacentHTML('beforeend', `<section>${inner}</section>`);
      }
    });
  }

  // ── Public entry point ─────────────────────────────────────────────
  window.slideDeck = {
    load: function (mdPath) {
      fetch(mdPath)
        .then(r => {
          if (!r.ok) throw new Error('Could not fetch ' + mdPath);
          return r.text();
        })
        .then(md => {
          const parsed = parse(md);
          assemble(parsed);
          // initialise reveal after DOM is ready
          if (window.Reveal) {
            Reveal.initialize({
              hash:             true,
              slideNumber:      true,
              transition:       'slide',
              controlsTutorial: true,
              center:           true,
              mouseWheel:       false
            });
          }
        })
        .catch(err => {
          document.querySelector('.reveal .slides').innerHTML =
            `<section><h2 style="color:#e74c3c">Failed to load slides</h2><p>${err.message}</p></section>`;
          console.error(err);
        });
    }
  };
})();
