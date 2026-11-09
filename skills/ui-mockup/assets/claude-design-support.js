// Local stand-in for the canvas runtime, so a .dc.html file renders when opened from a local web server.
// On the canvas, the canvas provides its own support.js; this file is never published.
// It renders only the first state of an artboard: taps change state but do not re-render.
class DCLogic { constructor(p) { this.props = p || {}; } setState(s) { Object.assign(this.state, s); } }

const lookup = (expr, scope) => {
  expr = expr.trim();
  if (expr === 'true') return true; if (expr === 'false') return false;
  if (/^-?\d+(\.\d+)?$/.test(expr)) return Number(expr);
  return expr.split('.').reduce((o, k) => (o == null ? undefined : o[k]), scope);
};
const interp = (s, scope) => {
  const whole = s.match(/^\s*\{\{([^}]+)\}\}\s*$/);
  if (whole) return lookup(whole[1], scope);
  return s.replace(/\{\{([^}]+)\}\}/g, (_, e) => { const v = lookup(e, scope); return v == null ? '' : v; });
};

async function renderDoc(doc, props) {
  const code = doc.querySelector('script[data-dc-script]').textContent;
  const Component = new Function('DCLogic', code + '\nreturn Component;')(DCLogic);
  const c = new Component(props);
  if (!c.state) c.state = {};
  const vals = c.renderVals();
  const frag = document.createDocumentFragment();
  for (const n of doc.querySelector('x-dc').childNodes) await render(n, vals, frag);
  return frag;
}

async function render(node, scope, parent) {
  if (node.nodeType === 3) { parent.appendChild(document.createTextNode(interp(node.textContent, scope))); return; }
  if (node.nodeType !== 1) return;
  const tag = node.tagName.toLowerCase();
  if (tag === 'helmet') { for (const n of node.children) document.head.appendChild(n.cloneNode(true)); return; }
  if (tag === 'sc-for') {
    const list = interp(node.getAttribute('list'), scope) || [];
    const as = node.getAttribute('as');
    for (let i = 0; i < list.length; i++) for (const n of node.childNodes) await render(n, { ...scope, [as]: list[i], $index: i }, parent);
    return;
  }
  if (tag === 'sc-if') { if (interp(node.getAttribute('value'), scope)) for (const n of node.childNodes) await render(n, scope, parent); return; }
  if (tag === 'dc-import') {
    const props = {};
    for (const a of node.attributes) {
      if (a.name === 'name' || a.name.startsWith('hint-')) continue;
      props[a.name.replace(/-([a-z])/g, (_, ch) => ch.toUpperCase())] = interp(a.value, scope);
    }
    const txt = await (await fetch(node.getAttribute('name') + '.dc.html', { cache: 'no-store' })).text();
    parent.appendChild(await renderDoc(new DOMParser().parseFromString(txt, 'text/html'), props));
    return;
  }
  const isSvg = node.namespaceURI === 'http://www.w3.org/2000/svg' || tag === 'svg' || node.closest('svg');
  const el = isSvg ? document.createElementNS('http://www.w3.org/2000/svg', node.tagName) : document.createElement(tag);
  for (const a of node.attributes) {
    const v = interp(a.value, scope);
    if (typeof v === 'function' || v == null) continue;
    el.setAttribute(a.name, v);
  }
  for (const n of node.childNodes) await render(n, scope, el);
  parent.appendChild(el);
}

// Props come from the URL (?props={"textSize":"ax5"}), so a variant can be previewed without its wrapper file.
document.addEventListener('DOMContentLoaded', async () => {
  const props = JSON.parse(new URLSearchParams(location.search).get('props') || '{}');
  try {
    const frag = await renderDoc(document, props);
    document.body.replaceChildren(frag);
    document.documentElement.dataset.rendered = 'ready';
  } catch (e) {
    document.documentElement.dataset.rendered = 'error';
    document.body.textContent = e.stack;
  }
});
