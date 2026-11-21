# Fills tpl/frame.html with each iteration's OS picker and sample rosters.
# Run from the round folder: python3 tpl/make.py
import pathlib

FRAME = pathlib.Path("tpl/frame.html").read_text()

IT = {}

# I: one featured card, the others as a quiet line under it. Rosters inside the card.
IT["i"] = dict(style="""
  .feat { display: flex; flex-direction: column; align-items: center; margin: 1.8rem 0 0; }
  .feat .mod { width: min(19rem, 100%); padding-top: 1.1rem; }
  .feat .file { font-size: .72rem; color: var(--faint); margin-top: .3rem; }
  .feat .ros { margin-top: .55rem; padding-top: .5rem; border-top: 1px solid var(--mod-edge); width: 100%; text-align: center; font-size: .8rem; font-weight: 700; text-decoration: none; display: flex; justify-content: center; align-items: center; gap: .35rem; }
  .others { display: flex; flex-wrap: wrap; justify-content: center; align-items: center; gap: .35rem; margin: .8rem 0 0; font-size: .78rem; color: var(--faint); }
  .others button { display: inline-flex; align-items: center; gap: .35rem; padding: .2rem .65rem; font: inherit; font-size: .76rem; color: var(--soft); background: transparent; border: 1px solid var(--mod-edge); border-radius: 999px; cursor: pointer; }
  .others button:hover { background: var(--mod); color: var(--ink); }
  .others .ic { width: 18px; height: 13px; color: var(--accent); }
""", main="""
    <div class="feat"><div class="mod" id="card"></div><div class="others" id="others"></div></div>
""", script="""
  function render(DL) {
    var K = window.DLkit, mine = DL.guess();
    function show(id) {
      var o = DL.byId(id);
      document.getElementById("card").innerHTML = '<span class="badge">' + (id === mine ? "For you" : "Selected") + "</span>" + DL.svg(o.icon) +
        "<b>" + o.name + "</b><small>" + o.sub + "</small>" +
        '<a class="dl" href="' + DL.url(o.file) + '">' + DL.svg("i-down") + "Download</a>" +
        '<span class="file">' + o.file + "</span>" +
        '<a class="ros" href="' + DL.links.rosters + '">' + K.csv + "+ Sample rosters</a>";
      document.getElementById("others").innerHTML = "Other versions:" + DL.os.filter(function (x) { return x.id !== id; }).map(function (x) {
        return '<button type="button" data-os="' + x.id + '">' + DL.svg(x.icon) + x.name + " · " + x.sub + "</button>";
      }).join("");
      document.getElementById("how").innerHTML = K.band(DL, o);
    }
    document.getElementById("others").addEventListener("click", function (e) { var b = e.target.closest("button"); if (b) show(b.dataset.os); });
    show(mine);
  }
""")

# J: the likely card in front, the other three as tabs peeking from behind it. Rosters as the band's last tile.
IT["j"] = dict(style="""
  .deck { display: flex; justify-content: center; align-items: center; margin: 1.8rem 0 0; }
  .deck .mod { width: 16rem; z-index: 2; padding-top: 1.1rem; box-shadow: 0 6px 16px rgba(20,60,30,.14); }
  .deck .file { font-size: .72rem; color: var(--faint); margin-top: .3rem; }
  .peek { display: grid; gap: .35rem; margin-left: -10px; z-index: 1; }
  .peek button { display: grid; grid-template-columns: 26px auto; align-items: center; gap: .4rem; width: 52px; overflow: hidden; padding: .45rem .5rem .45rem 18px; font: inherit; font-size: .74rem; text-align: left; white-space: nowrap;
    color: var(--soft); background: var(--mod); border: 1.5px solid var(--mod-edge); border-left: 0; border-radius: 0 10px 10px 0; cursor: pointer; transition: width .18s ease; }
  .peek button:hover, .peek button:focus-visible { width: 11.5rem; color: var(--ink); }
  .peek .ic { width: 24px; height: 18px; color: var(--accent); }
  .peek small { display: block; font-size: .66rem; color: var(--faint); }
  ol.strip li.ros-tile { border-left: 1.5px dashed var(--blue-edge); padding-left: .5rem; margin-left: .3rem; }
  ol.strip li.ros-tile::before { display: none; }
  ol.strip li.ros-tile a { display: block; text-decoration: none; color: var(--blue); font-weight: 700; }
  ol.strip li.ros-tile .pic { background: var(--blue-soft); display: grid; place-items: center; aspect-ratio: 3 / 2; }
  ol.strip li.ros-tile .csv { width: 34px; height: 40px; }
""", main="""
    <div class="deck"><div class="mod" id="card"></div><div class="peek" id="peek"></div></div>
""", script="""
  function render(DL) {
    var K = window.DLkit, mine = DL.guess();
    function show(id) {
      var o = DL.byId(id);
      document.getElementById("card").innerHTML = '<span class="badge">' + (id === mine ? "For you" : "Selected") + "</span>" + DL.svg(o.icon) +
        "<b>" + o.name + "</b><small>" + o.sub + "</small>" +
        '<a class="dl" href="' + DL.url(o.file) + '">' + DL.svg("i-down") + "Download</a><span class=\\"file\\">" + o.file + "</span>";
      document.getElementById("peek").innerHTML = DL.os.filter(function (x) { return x.id !== id; }).map(function (x) {
        return '<button type="button" data-os="' + x.id + '" aria-label="' + x.name + ", " + x.sub + '">' + DL.svg(x.icon) + "<span>" + x.name + "<small>" + x.sub + "</small></span></button>";
      }).join("");
      var ros = '<li class="ros-tile"><a href="' + DL.links.rosters + '"><span class="pic">' + K.csv + "</span>Sample rosters</a></li>";
      document.getElementById("how").innerHTML = K.band(DL, o, ros);
    }
    document.getElementById("peek").addEventListener("click", function (e) { var b = e.target.closest("button"); if (b) show(b.dataset.os); });
    show(mine);
  }
""")

# K: no card. One split button whose arrow opens the other versions. Rosters as a blue twin button.
IT["k"] = dict(style="""
  .get { display: flex; flex-wrap: wrap; justify-content: center; align-items: flex-start; gap: .6rem; margin: 1.8rem 0 0; }
  .split { position: relative; display: inline-flex; }
  .split a.dl { margin: 0; border-radius: 8px 0 0 8px; padding: .6rem 1.2rem; font-size: .95rem; }
  .split > button { padding: 0 .7rem; border: 0; border-left: 1px solid rgba(255,255,255,.35); border-radius: 0 8px 8px 0; background: var(--accent); color: #fff; font-size: .8rem; cursor: pointer; }
  .menu { position: absolute; top: calc(100% + .35rem); left: 0; z-index: 5; min-width: 100%; padding: .3rem; background: var(--mod); border: 1px solid var(--mod-edge); border-radius: 10px; box-shadow: 0 8px 20px rgba(20,60,30,.18); }
  .menu[hidden] { display: none; }
  .menu button { display: grid; grid-template-columns: 26px 1fr auto; align-items: center; gap: .5rem; width: 100%; padding: .4rem .5rem; font: inherit; font-size: .82rem; text-align: left; color: var(--ink); background: transparent; border: 0; border-radius: 6px; cursor: pointer; white-space: nowrap; }
  .menu button:hover { background: rgba(255,255,255,.6); }
  .menu .ic { width: 22px; height: 16px; color: var(--accent); }
  .menu small { color: var(--faint); font-size: .72rem; }
  .menu .tick { color: var(--accent); font-weight: 700; }
  a.rosbtn { display: inline-flex; align-items: center; gap: .4rem; padding: .5rem 1rem; border-radius: 8px; border: 1.5px solid var(--blue-edge); background: var(--blue-soft); color: var(--blue); font-size: .88rem; font-weight: 700; text-decoration: none; }
  a.rosbtn .csv { width: 18px; height: 22px; }
  .sub { margin: .45rem 0 0; text-align: center; font-size: .76rem; color: var(--faint); }
""", main="""
    <div class="get">
      <div class="split"><a class="dl" id="btn" href="#"></a><button type="button" id="caret" aria-haspopup="true" aria-expanded="false" aria-label="Other versions">▾</button><div class="menu" id="menu" hidden></div></div>
      <a class="rosbtn" id="ros" href="#"></a>
    </div>
    <p class="sub" id="sub"></p>
""", script="""
  function render(DL) {
    var K = window.DLkit, mine = DL.guess(), menu = document.getElementById("menu"), caret = document.getElementById("caret");
    var r = document.getElementById("ros"); r.href = DL.links.rosters; r.innerHTML = K.csv + "Sample rosters";
    function show(id) {
      var o = DL.byId(id);
      var b = document.getElementById("btn"); b.href = DL.url(o.file); b.innerHTML = DL.svg("i-down") + "Download for " + o.name;
      document.getElementById("sub").innerHTML = o.sub + " · " + o.file + (id === mine ? "" : " · <a href=\\"#\\" id=\\"back\\">back to mine</a>");
      var back = document.getElementById("back"); if (back) back.addEventListener("click", function (e) { e.preventDefault(); show(mine); });
      menu.innerHTML = DL.os.map(function (x) {
        return '<button type="button" data-os="' + x.id + '">' + DL.svg(x.icon) + "<span>" + x.name + " <small>" + x.sub + "</small></span><span class=\\"tick\\">" + (x.id === id ? "✓" : "") + "</span></button>";
      }).join("");
      document.getElementById("how").innerHTML = K.band(DL, o);
    }
    caret.addEventListener("click", function (e) { e.stopPropagation(); menu.hidden = !menu.hidden; caret.setAttribute("aria-expanded", String(!menu.hidden)); });
    menu.addEventListener("click", function (e) { var b = e.target.closest("button"); if (b) { show(b.dataset.os); menu.hidden = true; } });
    document.addEventListener("click", function () { menu.hidden = true; });
    show(mine);
  }
""")

# L: the likely card alone, with a one-line "not right?" that unfolds G's full row. Rosters as an opt-in on the button.
IT["l"] = dict(style="""
  .one { display: flex; justify-content: center; margin: 1.8rem 0 0; }
  .one .mod { width: min(19rem, 100%); padding-top: 1.1rem; }
  .one .file { font-size: .72rem; color: var(--faint); margin-top: .3rem; }
  .opt { display: flex; align-items: center; gap: .4rem; margin-top: .6rem; font-size: .78rem; color: var(--blue); cursor: pointer; }
  .opt input { accent-color: var(--blue); margin: 0; }
  .opt .csv { width: 16px; height: 19px; }
  details.all { margin: .8rem 0 0; text-align: center; }
  details.all > summary { display: inline; cursor: pointer; font-size: .8rem; color: var(--link); list-style: none; }
  details.all > summary::-webkit-details-marker { display: none; }
  details.all > summary::after { content: " ▸"; font-size: .65rem; }
  details.all[open] > summary::after { content: " ▾"; }
  .row { display: grid; grid-template-columns: repeat(4, 1fr); gap: .5rem; margin: .8rem 0 0; }
  .row button { display: grid; justify-items: center; gap: .05rem; padding: .55rem .3rem; font: inherit; color: var(--ink); background: transparent; border: 1.5px solid var(--mod-edge); border-radius: 10px; cursor: pointer; }
  .row button[aria-current="true"] { background: var(--mod); border-color: var(--accent); }
  .row .ic { width: 26px; height: 19px; color: var(--accent); }
  .row b { font-size: .82rem; }
  .row small { font-size: .68rem; color: var(--faint); }
  @media (max-width: 600px) { .row { grid-template-columns: 1fr 1fr; } }
""", main="""
    <div class="one"><div class="mod" id="card"></div></div>
    <details class="all"><summary id="q"></summary><div class="row" id="row"></div></details>
""", script="""
  function render(DL) {
    var K = window.DLkit, mine = DL.guess(), withRos = false, cur = mine;
    var mo = DL.byId(mine);
    document.getElementById("q").textContent = "Not on " + (mo.name === "Mac" ? "a Mac, " + mo.sub.replace(/ \\(.*/, "") : mo.name) + "? All versions";
    document.getElementById("row").innerHTML = DL.os.map(function (x) {
      return '<button type="button" data-os="' + x.id + '">' + DL.svg(x.icon) + "<b>" + x.name + "</b><small>" + x.sub + "</small></button>";
    }).join("");
    function show(id) {
      cur = id;
      var o = DL.byId(id);
      document.getElementById("card").innerHTML = '<span class="badge">' + (id === mine ? "For you" : "Selected") + "</span>" + DL.svg(o.icon) +
        "<b>" + o.name + "</b><small>" + o.sub + "</small>" +
        '<a class="dl" id="btn" href="' + DL.url(o.file) + '">' + DL.svg("i-down") + (withRos ? "Download both" : "Download") + "</a>" +
        '<span class="file">' + o.file + (withRos ? " + HappyCamper-demo-data.zip" : "") + "</span>" +
        '<label class="opt"><input type="checkbox" id="ros"' + (withRos ? " checked" : "") + ">" + K.csv + "Include sample rosters</label>";
      document.getElementById("ros").addEventListener("change", function (e) { withRos = e.target.checked; show(cur); });
      document.getElementById("btn").addEventListener("click", function () { if (withRos) window.open(DL.links.rosters, "_blank"); });
      document.querySelectorAll("#row button").forEach(function (b) { b.setAttribute("aria-current", String(b.dataset.os === id)); });
      document.getElementById("how").innerHTML = K.band(DL, o);
    }
    document.getElementById("row").addEventListener("click", function (e) { var b = e.target.closest("button"); if (b) show(b.dataset.os); });
    show(mine);
  }
""")

# M: G's row kept, but the likely module takes the width and the rest shrink to icons. Rosters as a pill in the hero.
IT["m"] = dict(style="""
  .acc { display: flex; gap: .5rem; margin: 1.8rem auto 0; max-width: 36rem; }
  .acc .mod { flex: 1; min-width: 0; padding: .7rem .3rem; cursor: pointer; transition: flex .2s ease; }
  .acc .mod.open { flex: 4; padding: 1.1rem .7rem .8rem; cursor: default; border-color: var(--accent); }
  .acc .mod .more { display: none; }
  .acc .mod.open .more { display: contents; }
  .acc .mod:not(.open) b { font-size: .78rem; }
  .acc .mod:not(.open) small { font-size: .64rem; text-align: center; line-height: 1.25; }
  .acc .mod:not(.open):hover { background: rgba(255,255,255,.4); }
  .acc .file { font-size: .72rem; color: var(--faint); margin-top: .3rem; }
  .hero .pills { display: flex; justify-content: center; flex-wrap: wrap; gap: .4rem; margin-top: .45rem; }
  .hero .pills details.whatsnew { margin: 0; }
  .hero a.rospill { display: inline-flex; align-items: center; gap: .3rem; font-size: .78rem; font-weight: 700; color: var(--blue); border: 1px solid currentColor; border-radius: 999px; padding: .15rem .8rem; text-decoration: none; }
  .hero a.rospill .csv { width: 13px; height: 16px; }
  @media (max-width: 560px) { .acc .mod.open { flex: 3; } }
""", main="""
    <div class="acc" id="acc"></div>
""", script="""
  function render(DL) {
    var K = window.DLkit, mine = DL.guess();
    var w = document.querySelector(".hero details.whatsnew"), pills = document.createElement("div");
    pills.className = "pills"; w.parentNode.insertBefore(pills, w); pills.appendChild(w);
    pills.insertAdjacentHTML("beforeend", '<a class="rospill" href="' + DL.links.rosters + '">' + K.csv + "Sample rosters</a>");
    var acc = document.getElementById("acc");
    acc.innerHTML = DL.os.map(function (o) {
      return '<div class="mod" data-os="' + o.id + '" tabindex="0"><span class="badge more">For you</span>' + DL.svg(o.icon) + "<b>" + o.name + "</b><small>" + o.sub + "</small>" +
        '<span class="more"><a class="dl" href="' + DL.url(o.file) + '">' + DL.svg("i-down") + 'Download</a><span class="file">' + o.file + "</span></span></div>";
    }).join("");
    acc.querySelectorAll(".mod").forEach(function (m) { if (m.dataset.os !== mine) m.querySelector(".badge").remove(); });
    function show(id) {
      acc.querySelectorAll(".mod").forEach(function (m) { m.classList.toggle("open", m.dataset.os === id); });
      document.getElementById("how").innerHTML = K.band(DL, DL.byId(id));
    }
    acc.addEventListener("click", function (e) { var m = e.target.closest(".mod"); if (m && !m.classList.contains("open")) show(m.dataset.os); });
    acc.addEventListener("keydown", function (e) { var m = e.target.closest(".mod"); if (m && (e.key === "Enter" || e.key === " ")) { e.preventDefault(); show(m.dataset.os); } });
    show(mine);
  }
""")

# Shared by N and O: M's growing modules, one- or two-word labels when collapsed, Jay's macOS note.
NO_STYLE = """
  .acc { display: flex; gap: .5rem; margin: 1.8rem auto 0; max-width: 36rem; }
  .acc .mod { flex: 1; min-width: 0; padding: .7rem .3rem; cursor: pointer; transition: flex .2s ease; }
  .acc .mod.open { flex: 4; padding: 1.1rem .7rem .8rem; cursor: default; border-color: var(--accent); }
  .acc .mod .more, .acc .mod .full, .acc .mod.open .short { display: none; }
  .acc .mod.open .more { display: contents; }
  .acc .mod.open .full { display: block; }
  .acc .mod .short { font-size: .76rem; text-align: center; line-height: 1.25; }
  .acc .mod:not(.open):hover { background: rgba(255,255,255,.4); }
  .acc .file { font-size: .72rem; color: var(--faint); margin-top: .3rem; }
  @media (max-width: 560px) { .acc { flex-wrap: wrap; } .acc .mod.open { flex: 1 1 100%; order: -1; } }
"""
NO_MAC = """
    var trust = DL.trustHTML;
    DL.trustHTML = function (k) {
      return k !== "mac" ? trust(k) : "macOS requires these steps for any app not on the App Store. See <a href=\\"" + DL.trust.mac.url + "\\">Apple's guide</a> for details. HappyCamper's code is open-source, <a href=\\"" + DL.links.details + "\\">learn more here</a>.";
    };
    function osMod(o) {
      return '<div class="mod" data-os="' + o.id + '" tabindex="0"><span class="badge more">For you</span>' + DL.svg(o.icon) +
        '<b class="short">' + o.short + '</b><b class="full">' + o.name + '</b><small class="more">' + o.sub + "</small>" +
        '<span class="more"><a class="dl" href="' + DL.url(o.file) + '">' + DL.svg("i-down") + 'Download</a><span class="file">' + o.file + "</span></span></div>";
    }
    function wire(acc, show) {
      acc.querySelectorAll(".mod").forEach(function (m) { if (m.dataset.os !== mine) { var b = m.querySelector(".badge"); if (b) b.remove(); } });
      acc.addEventListener("click", function (e) { var m = e.target.closest(".mod"); if (m && !m.classList.contains("open")) show(m.dataset.os); });
      acc.addEventListener("keydown", function (e) { var m = e.target.closest(".mod"); if (m && (e.key === "Enter" || e.key === " ")) { e.preventDefault(); show(m.dataset.os); } });
    }
"""

# N: M with short collapsed labels, the new macOS note, and the title "HappyCamper".
IT["n"] = dict(h1="HappyCamper", style=IT["m"]["style"].split("  .acc {")[0] + NO_STYLE + """
  .hero .pills { display: flex; justify-content: center; flex-wrap: wrap; gap: .4rem; margin-top: .45rem; }
  .hero .pills details.whatsnew { margin: 0; }
  .hero a.rospill { display: inline-flex; align-items: center; gap: .3rem; font-size: .78rem; font-weight: 700; color: var(--blue); border: 1px solid currentColor; border-radius: 999px; padding: .15rem .8rem; text-decoration: none; }
  .hero a.rospill .csv { width: 13px; height: 16px; }
""", main=IT["m"]["main"], script="""
  function render(DL) {
    var K = window.DLkit, mine = DL.guess();""" + NO_MAC + """
    var w = document.querySelector(".hero details.whatsnew"), pills = document.createElement("div");
    pills.className = "pills"; w.parentNode.insertBefore(pills, w); pills.appendChild(w);
    pills.insertAdjacentHTML("beforeend", '<a class="rospill" href="' + DL.links.rosters + '">' + K.csv + "Sample rosters</a>");
    var acc = document.getElementById("acc");
    acc.innerHTML = DL.os.map(osMod).join("");
    function show(id) {
      acc.querySelectorAll(".mod").forEach(function (m) { m.classList.toggle("open", m.dataset.os === id); });
      document.getElementById("how").innerHTML = K.band(DL, DL.byId(id));
    }
    wire(acc, show);
    show(mine);
  }
""")

# O: N with the samples as a fifth module. Opened, the band below shows how to use them instead of how to install.
IT["o"] = dict(h1="HappyCamper", style=NO_STYLE + """
  .acc { max-width: 40rem; }
  .acc .mod.ros { background: var(--blue-soft); border-color: var(--blue-edge); }
  .acc .mod.ros.open { border-color: var(--blue); }
  .acc .mod.ros .csv { width: 26px; height: 31px; margin-bottom: .15rem; }
  .acc .mod.ros .short, .acc .mod.ros .full { color: var(--blue); }
  .acc .mod.ros a.dl { background: var(--blue); }
""", main=IT["m"]["main"], script="""
  function render(DL) {
    var K = window.DLkit, mine = DL.guess();""" + NO_MAC + """
    var USE = [
      { pic: "s-zip", text: "Unzip the rosters" },
      { pic: "s-import", text: "Import both" },
      { pic: "s-table", text: "View and sort" },
      { pic: "s-export", text: "Export a CSV" }
    ];
    var acc = document.getElementById("acc");
    acc.innerHTML = DL.os.map(osMod).join("") +
      '<div class="mod ros" data-os="samples" tabindex="0">' + K.csv + '<b class="short">Samples</b><b class="full">Sample rosters</b><small class="more">Fictional campers</small>' +
      '<span class="more"><a class="dl" href="' + DL.links.rosters + '">' + DL.svg("i-down") + 'Download</a><span class="file">HappyCamper-demo-data.zip</span></span></div>';
    function show(id) {
      acc.querySelectorAll(".mod").forEach(function (m) { m.classList.toggle("open", m.dataset.os === id); });
      document.getElementById("how").innerHTML = id !== "samples" ? K.band(DL, DL.byId(id)) :
        '<h2>Using the sample rosters</h2><ol class="strip">' + USE.map(function (s) { return "<li>" + K.pic(s) + s.text + "</li>"; }).join("") +
        "</ol><p>They work with every version above.</p>";
    }
    wire(acc, show);
    show(mine);
  }
""")

# P–S: O's page plus a way to point at Demo and Details below the download.
DEMO_LINE = "The lowest hassle way to see what the app does."
DETAILS_LINE = "How the app actually works, and why you should trust it."
DROP_FOOTPILLS = """
    var fp = document.querySelector("footer .footpills"); if (fp) fp.parentNode.remove();"""

def from_o(style, after, script, drop=True):
    sc = IT["o"]["script"].replace("    show(mine);\n  }", "    show(mine);" + (DROP_FOOTPILLS if drop else "") + script + "\n  }")
    return dict(h1="HappyCamper", style=IT["o"]["style"] + style, main=IT["o"]["main"], after=after, script=sc)

# P: two signpost cards, Demo in blue and Details in green, icon and one line each.
IT["p"] = from_o("""
  .signs { display: grid; grid-template-columns: 1fr 1fr; gap: .7rem; margin: 2rem 0 0; }
  .signs a { display: flex; align-items: center; gap: .8rem; padding: .75rem .9rem; border-radius: 12px; text-decoration: none; color: var(--ink); background: var(--mod); border: 1.5px solid var(--mod-edge); }
  .signs a.demo { background: var(--blue-soft); border-color: var(--blue-edge); }
  .signs a:hover { filter: brightness(1.04); border-color: var(--accent); }
  .signs a.demo:hover { border-color: var(--blue); }
  .signs .ic { flex: none; width: 28px; height: 28px; color: var(--accent); }
  .signs .demo .ic { color: var(--blue); }
  .signs b { display: block; font-size: .92rem; }
  .signs .demo b { color: var(--blue); }
  .signs span { font-size: .8rem; color: var(--soft); }
  @media (max-width: 600px) { .signs { grid-template-columns: 1fr; } }
""", """
    <nav class="signs" aria-label="HappyCamper pages">
      <a class="demo" id="toDemo" href="#"><svg class="ic" aria-hidden="true"><use href="#i-globe"/></svg><div><b>Demo</b><span>%DEMO%</span></div></a>
      <a id="toDetails" href="#"><svg class="ic" aria-hidden="true"><use href="#i-shield"/></svg><div><b>Details</b><span>%DETAILS%</span></div></a>
    </nav>
""".replace("%DEMO%", DEMO_LINE).replace("%DETAILS%", DETAILS_LINE), """
    document.getElementById("toDemo").href = DL.links.demo;
    document.getElementById("toDetails").href = DL.links.details;""")

# Q: no new section. The footer's own Demo and Details pills each gain their line.
IT["q"] = from_o("""
  .footsigns { display: flex; justify-content: center; flex-wrap: wrap; gap: 1.6rem; margin: 0 0 1.2rem; }
  .footsigns a { display: grid; justify-items: center; gap: .3rem; max-width: 14rem; text-decoration: none; color: var(--soft); font-size: .8rem; line-height: 1.4; }
  .footsigns a b { padding: .2rem .95rem; border-radius: 999px; font-size: .82rem; color: var(--link); border: 1px solid var(--link); }
  .footsigns a.demo b { color: var(--blue); border-color: var(--blue); }
  .footsigns a:hover b { color: #fff; background: var(--link); }
  .footsigns a.demo:hover b { background: var(--blue); }
""", "", """
    var foot = document.querySelector("footer.sitefoot");
    foot.insertAdjacentHTML("afterbegin", '<nav class="footsigns" aria-label="HappyCamper pages"><a class="demo" href="' + DL.links.demo + '"><b>Demo</b>%DEMO%</a><a href="' + DL.links.details + '"><b>Details</b>%DETAILS%</a></nav>');""".replace("%DEMO%", DEMO_LINE).replace("%DETAILS%", DETAILS_LINE))

# R: one aside box, darker than the page, as two questions and their answers.
IT["r"] = from_o("""
  .ask { margin: 2rem 0 0; padding: .8rem 1rem; background: var(--panel); border: 1px solid var(--panel-edge); border-radius: 10px; display: grid; gap: .45rem; font-size: .9rem; }
  .ask p { margin: 0; display: flex; align-items: center; gap: .6rem; }
  .ask .ic { flex: none; width: 20px; height: 20px; color: var(--accent); }
  .ask .demo .ic, .ask .demo a { color: var(--blue); }
  .ask a { font-weight: 700; }
  .how { background: var(--mod); border: 1px solid var(--mod-edge); }
""", """
    <div class="ask">
      <p class="demo"><svg class="ic" aria-hidden="true"><use href="#i-globe"/></svg><span>Not ready to install? <a id="toDemo" href="#">Try the demo</a>, the lowest hassle way to see what the app does.</span></p>
      <p><svg class="ic" aria-hidden="true"><use href="#i-shield"/></svg><span>Questions about how it works, or why to trust it? <a id="toDetails" href="#">See Details</a>.</span></p>
    </div>
""", """
    document.getElementById("toDemo").href = DL.links.demo;
    document.getElementById("toDetails").href = DL.links.details;""")

# S: two picture tiles, each a small drawing of the page it opens: the demo's table in a browser, J's device diagram.
IT["s"] = from_o("""
  .peeks { display: grid; grid-template-columns: 1fr 1fr; gap: .9rem; margin: 2rem 0 0; }
  .peeks a { display: grid; grid-template-columns: 112px 1fr; gap: .9rem; align-items: center; padding: .7rem; border-radius: 12px; text-decoration: none; color: var(--ink); border: 1.5px solid transparent; }
  .peeks a:hover { background: rgba(255,255,255,.3); border-color: var(--mod-edge); }
  .peeks .pic { width: 112px; height: 75px; }
  .peeks b { display: block; font-size: .95rem; color: var(--link); }
  .peeks .demo b { color: var(--blue); }
  .peeks span { font-size: .8rem; color: var(--soft); line-height: 1.4; }
  @media (max-width: 600px) { .peeks { grid-template-columns: 1fr; } }
""", """
    <nav class="peeks" aria-label="HappyCamper pages">
      <a class="demo" id="toDemo" href="#"><svg class="pic" viewBox="0 0 96 64" aria-hidden="true"><use href="#s-browser"/></svg><div><b>Demo ›</b><span>%DEMO%</span></div></a>
      <a id="toDetails" href="#"><svg class="pic" viewBox="0 0 96 64" aria-hidden="true"><use href="#s-works"/></svg><div><b>Details ›</b><span>%DETAILS%</span></div></a>
    </nav>
""".replace("%DEMO%", DEMO_LINE).replace("%DETAILS%", DETAILS_LINE), """
    document.getElementById("toDemo").href = DL.links.demo;
    document.getElementById("toDetails").href = DL.links.details;""")

# T: P's signposts, the rosters back as a box beside them, four OS modules, and a clearer guessed module.
P_SIGNS = IT["p"]["style"][len(IT["o"]["style"]):]
IT["t"] = dict(h1="HappyCamper", style=NO_STYLE + P_SIGNS + """
  .acc .mod.open { background: #f4f9f2; border: 2.5px solid var(--accent); }
  .acc .mod.mine.open { box-shadow: 0 0 0 5px rgba(26,103,44,.2); }
  .acc .mod.mine:not(.open) { border: 2px dashed var(--accent); }
  .acc .mod .badge { font-size: .66rem; padding: .05rem .6rem; }
  .acc .guess { display: flex; align-items: center; gap: .3rem; margin-top: .55rem; font-size: .7rem; color: var(--faint); }
  .acc .guess .ic { width: 13px; height: 13px; color: var(--accent); }
  .acc .mod:not(.open) .guess { display: none; }
  .signs { grid-template-columns: repeat(3, 1fr); }
  .signs a.ros .csv { flex: none; width: 26px; height: 31px; }
  @media (max-width: 720px) { .signs { grid-template-columns: 1fr; } }
""", main=IT["m"]["main"], after="""
    <nav class="signs" aria-label="Try HappyCamper">
      <a class="ros" id="toRosters" href="#"></a>
      <a class="demo" id="toDemo" href="#"><svg class="ic" aria-hidden="true"><use href="#i-globe"/></svg><div><b>In-browser demo</b><span>The quickest look at HappyCamper's core features.</span></div></a>
      <a id="toDetails" href="#"><svg class="ic" aria-hidden="true"><use href="#i-shield"/></svg><div><b>Details</b><span>How the app is built, and how data is used.</span></div></a>
    </nav>
""", script="""
  function render(DL) {
    var K = window.DLkit, mine = DL.guess();""" + NO_MAC + """
    var acc = document.getElementById("acc");
    acc.innerHTML = DL.os.map(osMod).join("");
    var m0 = acc.querySelector('[data-os="' + mine + '"]');
    m0.classList.add("mine");
    m0.querySelector(".badge").textContent = "Suggested for you";
    m0.querySelector("span.more").insertAdjacentHTML("beforeend", '<span class="guess">' + DL.svg("i-chip") + "Recommended for you</span>");
    function show(id) {
      acc.querySelectorAll(".mod").forEach(function (m) { m.classList.toggle("open", m.dataset.os === id); });
      document.getElementById("how").innerHTML = K.band(DL, DL.byId(id));
    }
    wire(acc, show);
    show(mine);""" + DROP_FOOTPILLS + """
    var r = document.getElementById("toRosters");
    r.href = DL.links.rosters;
    r.innerHTML = K.csv + "<div><b>Download demo rosters</b><span>Four sets of sample rosters to demo in the app.</span></div>";
    document.getElementById("toDemo").href = DL.links.demo;
    document.getElementById("toDetails").href = DL.links.details;
  }
""")

for k, v in IT.items():
    frame = FRAME.replace("<h1>Download HappyCamper</h1>", "<h1>" + v["h1"] + "</h1>") if "h1" in v else FRAME
    html = frame.replace("%STYLE%", v["style"].strip("\n")).replace("%MAIN%", v["main"].strip("\n")).replace("%SCRIPT%", v["script"].strip("\n")).replace("%AFTER%", v.get("after", "").strip("\n"))
    pathlib.Path(f"prototypes/{k}/index.html").write_text(html)
print("wrote", ", ".join(IT))
