"""Builds the three site pages from their sources, with one shared header bar,
nav boxes and footer.

  python3 -I tools/site/make-site.py

Sources:
  site/index.html    archive/1121-download-page/prototypes/t/index.html (download)
  site/demo.html     tools/demo-build/out/index.html, from tools/demo-build/build.py (demo)
  site/details.html  archive/1120-page-trio/prototypes/k/details.html (details)
"""
import os, re, shutil
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SITE = os.path.join(ROOT, 'site')
DL_ROUND = os.path.join(ROOT, 'archive/1121-download-page')

# The standard header bar, nav boxes and footer. The download page builds the
# same markup from dl.js; demo and details take it from here.
SHARED_CSS = '''
  /* Shared across the site: header bar, nav boxes, footer */
  .bar { position: sticky; top: 0; z-index: 10; background: #1a672c; box-shadow: 0 2px 8px rgba(20,60,30,.25); }
  .bar .in { width: min(1120px, 100%); margin: 0 auto; padding: .5rem 1.25rem; display: flex; align-items: center; justify-content: space-between; gap: 1rem; }
  .bar .home { display: flex; align-items: center; gap: .6rem; color: #fff; text-decoration: none; font: 700 1.1rem Verdana, Geneva, sans-serif; }
  .bar .home img { width: 36px; height: 36px; }
  .bar nav { display: flex; gap: .35rem; font: 700 .82rem Verdana, Geneva, sans-serif; }
  .bar nav a, .bar nav span { padding: .3rem .85rem; border-radius: 999px; text-decoration: none; }
  .bar nav a { color: #fff; border: 1px solid rgba(255,255,255,.45); }
  .bar nav a:hover { background: rgba(255,255,255,.15); }
  .bar nav span { color: #1a672c; background: #fff; border: 1px solid #fff; }
  @media (max-width: 520px) { .bar .home span { display: none; } .bar nav a, .bar nav span { padding: .25rem .6rem; } }
  .signs { display: grid; grid-template-columns: repeat(auto-fit, minmax(14rem, 1fr)); gap: .7rem; margin: 2.5rem 0 0; text-align: left; }
  .signs a { display: flex; align-items: center; gap: .8rem; padding: .75rem .9rem; border-radius: 12px; text-decoration: none; color: #26302a; background: #e6f1e2; border: 1.5px solid #a3c49b; }
  .signs a.demo { background: #dfeaf6; border-color: #9ab8dc; }
  .signs a:hover { filter: brightness(1.04); border-color: #1a672c; }
  .signs a.demo:hover { border-color: #2b68b8; }
  .signs svg { flex: none; width: 28px; height: 28px; color: #1a672c; }
  .signs .demo svg { color: #2b68b8; }
  .signs b { display: block; font-size: .92rem; }
  .signs .demo b { color: #2b68b8; }
  .signs span { font-size: .8rem; color: #43524a; }
  footer.sitefoot { margin-top: 3rem; padding-top: 2rem; text-align: center; font-size: .85rem; color: #43524a; }
  footer.sitefoot a { color: inherit; }
'''

ICON = {
    'down': '<path d="M12,3 V15 M7,10.5 L12,15.5 L17,10.5" stroke="currentColor" stroke-width="2.4" fill="none" stroke-linecap="round" stroke-linejoin="round"/><path d="M4,17 V20 H20 V17" stroke="currentColor" stroke-width="2.4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>',
    'globe': '<circle cx="12" cy="12" r="10" fill="none" stroke="currentColor" stroke-width="2"/><ellipse cx="12" cy="12" rx="4.5" ry="10" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M2,12 H22 M4,7 H20 M4,17 H20" stroke="currentColor" stroke-width="1.6"/>',
    'shield': '<path d="M12,2 L20,5 V11 Q20,18 12,22 Q4,18 4,11 V5 Z" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/><path d="M8.5,12 L11,14.5 L15.5,9.5" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>',
}
BOX = {
    'download': ('', 'down', 'Download the Java app', 'Bundled distributions and sample data'),
    'demo': ('demo', 'globe', 'In-browser demo', "The quickest look at HappyCamper's core features."),
    'details': ('', 'shield', 'Details', 'How the app is built, and how data is used.'),
}
PAGES = [('Download', 'download'), ('Demo', 'demo'), ('Details', 'details')]

def bar(here, href, icon='icon.png'):
    items = ''.join('<span aria-current="page">%s</span>' % n if n == here else '<a href="%s">%s</a>' % (href[k], n) for n, k in PAGES)
    return ('<header class="bar">\n  <div class="in">\n    <a class="home" href="%s" aria-label="HappyCamper, download page"><img src="%s" alt=""><span>HappyCamper</span></a>\n'
            '    <nav aria-label="HappyCamper pages">%s</nav>\n  </div>\n</header>\n') % (href['download'], icon, items)

def signs(keys, href):
    out = []
    for k in keys:
        cls, ic, title, line = BOX[k]
        out.append('      <a%s href="%s"><svg viewBox="0 0 24 24" aria-hidden="true">%s</svg><div><b>%s</b><span>%s</span></div></a>\n'
                   % (' class="%s"' % cls if cls else '', href[k], ICON[ic], title, line))
    return '    <nav class="signs" aria-label="HappyCamper pages">\n' + ''.join(out) + '    </nav>\n'

FOOTER = '  <footer class="sitefoot">\n    <div>A free app created by <a href="https://github.com/jaymoran103">Jay Moran</a></div>\n  </footer>\n'
HREF = {'download': 'index.html', 'demo': 'demo.html', 'details': 'details.html'}

def sub(text, old, new, count=1):
    assert text.count(old) == count, (text.count(old), old[:70])
    return text.replace(old, new)

PROTO_BAR = re.compile(r'<div class="proto-bar"[\s\S]*?\n</div>\n')

def download():
    h = open(os.path.join(DL_ROUND, 'prototypes/t/index.html'), encoding='utf-8').read()
    h = PROTO_BAR.sub('', h, count=1)
    for name in ('site.css', 'g2.css'):
        css = open(os.path.join(DL_ROUND, name), encoding='utf-8').read()
        h = sub(h, '<link rel="stylesheet" href="../../%s">' % name, '<style>\n%s</style>' % css)
    js = open(os.path.join(DL_ROUND, 'dl.js'), encoding='utf-8').read()
    js = sub(js, 'BASE + "../../site/demo.html"', '"demo.html"')
    js = sub(js, 'BASE + "../1120-page-trio/prototypes/k/details.html"', '"details.html"')
    h = sub(h, '<script src="../../dl.js"></script>', '<script>\n%s</script>' % js)
    h = h.replace('../../icon.png', 'icon.png')
    return h

def demo():
    h = open(os.path.join(ROOT, 'tools/demo-build/out/index.html'), encoding='utf-8').read()
    h = sub(h, 'padding: 3rem 1.25rem 2rem; }', 'padding: 0 1.25rem 2rem; }')
    # The download page's hero: logo, name, then one bold green line where it shows the version.
    hero = ('  .sitehead { text-align: center; margin-top: 2rem; }\n  .sitehead img { width: 110px; height: 110px; }\n'
            '  .sitehead h1 { font-size: 2.2rem; line-height: 1.2; margin: .8rem 0 0; }\n'
            '  .sitehead .version { margin: .45rem 0 0; font-size: .95rem; font-weight: 700; color: #2f7340; }\n'
            '  @media (max-width: 820px) { .page { padding-top: 0; } }\n  .intro .headline { margin: 0 0 .75rem; }\n')
    h = sub(h, '</style>', SHARED_CSS + hero + '</style>')
    h = sub(h, '<body>\n<div class="page">\n', '<body>\n' + bar('Demo', HREF) + '<div class="page">\n')
    h = sub(h, '<header class="top">', '<header class="top sitehead">')
    # The headline introduces the overview, so it sits left-aligned above it.
    h = sub(h, '    <p class="headline">Catch schedule problems before your campers do</p>\n  </header>', '    <p class="version">In-browser demo</p>\n  </header>')
    h = sub(h, '    <div class="intro">\n', '    <div class="intro">\n      <h2 class="headline">Catch schedule problems before your campers do</h2>\n')
    h = sub(h, '      <a class="dl" href="https://jaymoran103.github.io/happycamper-heart/docs/">Downloads and sample rosters</a>\n', '')
    h = sub(h, '  </main>\n', signs(['download', 'details'], HREF) + '  </main>\n')
    h = re.sub(r'  <footer>\n    <div>Created by.*?</footer>\n', FOOTER, h, count=1, flags=re.S)
    return h

def details():
    h = open(os.path.join(ROOT, 'archive/1120-page-trio/prototypes/k/details.html'), encoding='utf-8').read()
    h = PROTO_BAR.sub('', h, count=1)
    h = h.replace('../../../../site/', '').replace('../a/icon.png', 'icon.png')
    return h

if __name__ == '__main__':
    os.makedirs(SITE, exist_ok=True)
    for name, build in (('index.html', download), ('demo.html', demo), ('details.html', details)):
        open(os.path.join(SITE, name), 'w', encoding='utf-8').write(build())
    for f in ('icon.png', 'whatsnew.json'):
        shutil.copy(os.path.join(DL_ROUND, f), os.path.join(SITE, f))
    print('site/index.html, site/demo.html and site/details.html written')
