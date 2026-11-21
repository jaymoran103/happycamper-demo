/* Shared by every prototype in this round: the download facts, the install
 * steps, the pictograms, the J header bar and footer, and the live version.
 * Each prototype only lays these out its own way. */
(function () {
  "use strict";
  var BASE = document.currentScript.src.replace(/dl\.js(\?.*)?$/, "");
  /* whatsnew.json, inlined for file:// where fetch is refused */
  var WHATSNEW = {   "label": "v2.5",   "items": [     "Assertions - pass/fail checks for key schedule needs",     "Colored assertion badges show which filters need attention.",     "Drag and drop file selection"   ] };
  var REL = "https://github.com/jaymoran103/happycamper-heart/releases/latest/download/";

  var DL = (window.DL = {
    base: BASE,
    icon: BASE + "icon.png",
    links: {
      download: "index.html",
      demo: BASE + "../../site/demo.html",
      details: BASE + "../1120-page-trio/prototypes/k/details.html",
      rosters: REL + "HappyCamper-demo-data.zip"
    },
    tagline: "Analyze activity assignments, catch oversights, and measure preference satisfaction.",
    os: [
      { id: "mac-arm", short: "Mac (Silicon)", icon: "o-mac", name: "Mac", sub: "Apple Silicon (2021+)", file: "HappyCamper-macos-arm64.dmg", steps: "mac" },
      { id: "mac-intel", short: "Mac (Intel)", icon: "o-mac", name: "Mac", sub: "Intel (pre-2021)", file: "HappyCamper-macos-intel.dmg", steps: "mac" },
      { id: "windows", short: "Windows", icon: "o-win", name: "Windows", sub: "10 or 11", file: "HappyCamper-windows.msi", steps: "windows" },
      { id: "linux", short: "Linux", icon: "o-linux", name: "Linux", sub: "Debian or Ubuntu", file: "HappyCamper-linux.deb", steps: "linux" }
    ],
    steps: {
      mac: [
        { pic: "s-dmg", text: "Open the .dmg" },
        { pic: "s-drag", text: "Drag to Applications" },
        { pic: "s-macwarn", text: "Open it, click Done" },
        { pic: "s-anyway", text: "Privacy & Security › Open Anyway", gate: true,
          more: "In System Settings, scroll down and click Open Anyway beside the HappyCamper message. Enter your password if asked." },
        { pic: "s-done", text: "Smooth sailing from there" }
      ],
      windows: [
        { pic: "s-msi", text: "Open the .msi" },
        { pic: "s-winwarn", text: "More info › Run anyway", gate: true,
          more: "If Windows says “Windows protected your PC”, click More info, then Run anyway." },
        { pic: "s-installer", text: "Finish the installer" },
        { pic: "s-start", text: "Open from Start" }
      ],
      linux: [
        { pic: "s-deb", text: "Open the .deb" },
        { pic: "s-debinstall", text: "Click Install",
          more: "Or, from the download folder in a terminal: <code>sudo apt install ./HappyCamper-linux.deb</code>" },
        { pic: "s-appmenu", text: "Open from your apps" }
      ]
    },
    trust: {
      mac: { text: "macOS asks this of any app not from the App Store, and only the first time.", guide: "Apple's guide", url: "https://support.apple.com/en-us/102445" },
      windows: { text: "Windows asks this of small independent apps, and only the first time.", guide: "Microsoft's guide", url: "https://learn.microsoft.com/en-us/windows/apps/package-and-deploy/smartscreen-reputation" },
      linux: { text: "Linux has no extra warning step.", guide: "Ubuntu's guide", url: "https://ubuntu.com/server/docs/how-to/software/package-management/" }
    },
    whichMac: "Apple menu › About This Mac. A Chip line starting with Apple means Apple Silicon.",
    url: function (file) { return REL + file; },
    byId: function (id) { return DL.os.filter(function (o) { return o.id === id; })[0]; },
    guess: function () {
      var p = navigator.platform || "", ua = navigator.userAgent || "";
      return /Win/.test(p) ? "windows" : /Mac/.test(p) ? "mac-arm" : /Linux/.test(p) && !/Android/.test(ua) ? "linux" : "mac-arm";
    },
    svg: function (id, cls) {
      return '<svg class="ic ' + (cls || "") + '" aria-hidden="true"><use href="#' + id + '"/></svg>';
    },
    trustHTML: function (key) {
      var t = DL.trust[key];
      return t.text + ' <a href="' + t.url + '">' + t.guide + "</a>. All of HappyCamper's code is public: <a href=\"" + DL.links.details + '">Details</a>.';
    }
  });

  /* ---- pictograms: flat, little detail (rules 1 and 2) ---- */
  var APP = function (x, y, s) { return '<image href="' + DL.icon + '" x="' + x + '" y="' + y + '" width="' + s + '" height="' + s + '"/>'; };
  var T = function (x, y, size, fill, txt, extra) {
    return '<text x="' + x + '" y="' + y + '" text-anchor="middle" font-family="Verdana, Geneva, sans-serif" font-size="' + size + '" font-weight="700" fill="' + fill + '"' + (extra || "") + ">" + txt + "</text>";
  };
  function file(id, label, color, inner) {
    return '<symbol id="' + id + '" viewBox="0 0 96 64"><g transform="translate(32,6)">' +
      '<path d="M3,0 H23 L34,11 V49 Q34,52 31,52 H3 Q0,52 0,49 V3 Q0,0 3,0 Z" fill="#ffffff" stroke="#4a4a4a" stroke-width="2"/>' +
      '<path d="M23,0 V11 H34" fill="#dcdcdc" stroke="#4a4a4a" stroke-width="2" stroke-linejoin="round"/>' + inner +
      '<rect x="-8" y="33" width="32" height="15" rx="3" fill="' + color + '"/>' + T(8, 44, 9, "#ffffff", label) + "</g></symbol>";
  }
  var win = function (x, y, w, h) {
    return '<rect x="' + x + '" y="' + y + '" width="' + w + '" height="' + h + '" rx="6" fill="#f5f5f7" stroke="#aab1b9" stroke-width="1.5"/>' +
      '<circle cx="' + (x + 7) + '" cy="' + (y + 6) + '" r="1.8" fill="#ec6a5e"/><circle cx="' + (x + 13) + '" cy="' + (y + 6) + '" r="1.8" fill="#f4bf4f"/><circle cx="' + (x + 19) + '" cy="' + (y + 6) + '" r="1.8" fill="#61c554"/>';
  };
  var bar = function (x, y, w, c) { return '<rect x="' + x + '" y="' + y + '" width="' + w + '" height="3" rx="1.5" fill="' + (c || "#c3c8ce") + '"/>'; };

  var S = [
    file("s-dmg", "DMG", "#5f6f80", '<rect x="8" y="15" width="18" height="12" rx="2" fill="#c9ced4" stroke="#4a4a4a" stroke-width="1.5"/><circle cx="22" cy="24" r="1.5" fill="#4a4a4a"/>'),
    file("s-msi", "MSI", "#2b68b8", '<rect x="9" y="14" width="16" height="14" rx="1.5" fill="#d7e5f6" stroke="#2b68b8" stroke-width="1.5"/><path d="M17,17 V24 M14,21.5 L17,24.5 L20,21.5" stroke="#2b68b8" stroke-width="1.6" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'),
    file("s-deb", "DEB", "#a8452c", '<path d="M10,16 L17,13 L24,16 V25 L17,28 L10,25 Z" fill="#f1d9cf" stroke="#a8452c" stroke-width="1.5" stroke-linejoin="round"/><path d="M10,16 L17,19 L24,16 M17,19 V28" stroke="#a8452c" stroke-width="1.5" fill="none"/>'),
    '<symbol id="s-drag" viewBox="0 0 96 64">' + APP(4, 16, 32) +
      '<path d="M40,32 H54" stroke="#2f7340" stroke-width="3" stroke-linecap="round"/><path d="M52,26 L59,32 L52,38 Z" fill="#2f7340"/>' +
      '<path d="M62,20 Q62,16 66,16 H74 L78,20 H88 Q92,20 92,24 V46 Q92,50 88,50 H66 Q62,50 62,46 Z" fill="#3d8fe0"/>' +
      '<path d="M62,25 H92 V46 Q92,50 88,50 H66 Q62,50 62,46 Z" fill="#62adf2"/>' +
      '<path d="M72,45 L77,31 L82,45 M74,40 H80" stroke="#ffffff" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round"/></symbol>',
    '<symbol id="s-macwarn" viewBox="0 0 96 64">' + win(16, 2, 64, 60) + APP(40, 11, 16) +
      '<path d="M53,21 L57,28 H49 Z" fill="#f4bf4f" stroke="#8a6a14" stroke-width="1" stroke-linejoin="round"/>' +
      bar(28, 32, 40) + bar(34, 38, 28) +
      '<rect x="33" y="46" width="30" height="11" rx="5.5" fill="#2f7cf6"/>' + T(48, 53.8, 6.5, "#ffffff", "Done") + "</symbol>",
    '<symbol id="s-anyway" viewBox="0 0 96 64">' + win(4, 2, 88, 60) +
      '<rect x="8" y="13" width="22" height="45" rx="3" fill="#e4e7eb"/>' +
      bar(11, 18, 16) + '<rect x="10" y="25" width="18" height="6" rx="2" fill="#2f7cf6"/>' + bar(11, 35, 16) + bar(11, 41, 16) + bar(11, 47, 12) +
      bar(36, 17, 46) + bar(36, 23, 34) + bar(36, 29, 40) +
      '<rect x="37" y="39" width="50" height="17" rx="8.5" fill="none" stroke="#f0b429" stroke-width="2.5"/>' +
      '<rect x="40" y="42" width="44" height="11" rx="5.5" fill="#ffffff" stroke="#8d96a0" stroke-width="1"/>' + T(62, 49.6, 6.2, "#26302a", "Open Anyway") + "</symbol>",
    '<symbol id="s-done" viewBox="0 0 96 64">' + APP(28, 6, 40) +
      '<circle cx="66" cy="46" r="11" fill="#2f9e4f" stroke="#ffffff" stroke-width="2.5"/><path d="M60.5,46 L64.5,50 L71.5,42" stroke="#ffffff" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round"/></symbol>',
    '<symbol id="s-winwarn" viewBox="0 0 96 64"><rect x="8" y="4" width="80" height="56" rx="2" fill="#1f5fae"/>' +
      '<rect x="14" y="10" width="52" height="5" rx="1" fill="#ffffff"/>' + bar(14, 20, 62, "#a9c6ea") + bar(14, 26, 50, "#a9c6ea") +
      '<text x="14" y="41" font-family="Verdana, Geneva, sans-serif" font-size="7" font-weight="700" fill="#ffffff" text-decoration="underline">More info</text>' +
      '<rect x="48" y="46" width="34" height="10" rx="1" fill="#e8eef6" stroke="#f0b429" stroke-width="2"/>' + T(65, 53.2, 6, "#1d2b3a", "Run anyway") + "</symbol>",
    '<symbol id="s-installer" viewBox="0 0 96 64"><rect x="12" y="4" width="72" height="56" rx="3" fill="#f3f4f6" stroke="#9aa3ad" stroke-width="1.5"/>' +
      APP(19, 11, 16) + bar(40, 14, 36) + bar(40, 20, 24) +
      '<rect x="19" y="33" width="58" height="6" rx="3" fill="#2f9e4f"/>' +
      '<rect x="50" y="46" width="28" height="10" rx="2" fill="#2b68b8"/>' + T(64, 53.2, 6, "#ffffff", "Finish") + "</symbol>",
    '<symbol id="s-start" viewBox="0 0 96 64"><rect x="24" y="2" width="48" height="42" rx="4" fill="#f3f4f6" stroke="#9aa3ad" stroke-width="1.5"/>' +
      '<rect x="30" y="8" width="10" height="10" rx="2" fill="#d3d8de"/><rect x="56" y="8" width="10" height="10" rx="2" fill="#d3d8de"/><rect x="30" y="26" width="10" height="10" rx="2" fill="#d3d8de"/><rect x="56" y="26" width="10" height="10" rx="2" fill="#d3d8de"/>' +
      '<rect x="40" y="13" width="16" height="16" rx="3" fill="#ffffff" stroke="#f0b429" stroke-width="2"/>' + APP(42, 15, 12) +
      '<rect x="4" y="50" width="88" height="11" rx="2" fill="#dfe4ea"/>' +
      '<rect x="43" y="52" width="3" height="3" fill="#2b68b8"/><rect x="47" y="52" width="3" height="3" fill="#2b68b8"/><rect x="43" y="56" width="3" height="3" fill="#2b68b8"/><rect x="47" y="56" width="3" height="3" fill="#2b68b8"/></symbol>',
    '<symbol id="s-debinstall" viewBox="0 0 96 64"><rect x="8" y="4" width="80" height="56" rx="5" fill="#f6f5f4" stroke="#b5b1ac" stroke-width="1.5"/>' +
      APP(16, 14, 24) + bar(46, 16, 32) + bar(46, 22, 22) +
      '<rect x="46" y="31" width="34" height="12" rx="6" fill="#2f9e4f" stroke="#f0b429" stroke-width="2"/>' + T(63, 39.6, 6.5, "#ffffff", "Install") + "</symbol>",
    '<symbol id="s-appmenu" viewBox="0 0 96 64"><rect x="20" y="2" width="56" height="60" rx="6" fill="#33383d"/>' +
      [0, 1, 2].map(function (r) { return [0, 1, 2].map(function (c) {
        return r === 1 && c === 1 ? "" : '<rect x="' + (27 + c * 16) + '" y="' + (9 + r * 16) + '" width="10" height="10" rx="2.5" fill="#6b7279"/>'; }).join(""); }).join("") +
      '<rect x="40" y="22" width="16" height="16" rx="3" fill="none" stroke="#f0b429" stroke-width="2"/>' + APP(42, 24, 12) + "</symbol>",
    /* using the sample rosters, after the app's own help: select inputs, view and sort, export */
    '<symbol id="s-zip" viewBox="0 0 96 64"><g transform="translate(30,6)"><path d="M3,0 H23 L34,11 V49 Q34,52 31,52 H3 Q0,52 0,49 V3 Q0,0 3,0 Z" fill="#ffffff" stroke="#4a4a4a" stroke-width="2"/><path d="M23,0 V11 H34" fill="#dcdcdc" stroke="#4a4a4a" stroke-width="2" stroke-linejoin="round"/><path d="M13,4 H17 M15,8 H19 M13,12 H17 M15,16 H19 M13,20 H17" stroke="#4a4a4a" stroke-width="2"/><rect x="12" y="23" width="8" height="8" rx="1.5" fill="#d9d9d9" stroke="#4a4a4a" stroke-width="1.5"/><rect x="-8" y="33" width="32" height="15" rx="3" fill="#2b68b8"/>' + T(8, 44, 9, "#ffffff", "ZIP") + '</g></symbol>',
    '<symbol id="s-import" viewBox="0 0 96 64"><svg x="2" y="4" width="30" height="36" viewBox="0 0 70 84"><use href="#i-csv"/></svg><svg x="2" y="26" width="30" height="36" viewBox="0 0 70 84"><use href="#i-csv"/></svg>' +
      '<path d="M34,24 L46,30 M34,44 L46,36" stroke="#2f7340" stroke-width="2.5" stroke-linecap="round"/><path d="M44,26 L51,32 L42,34 Z" fill="#2f7340"/>' + win(52, 12, 40, 40) + APP(64, 24, 16) + '</symbol>',
    '<symbol id="s-table" viewBox="0 0 96 64">' + win(10, 4, 76, 56) + '<g stroke="#8a8a8a" stroke-width="1"><rect x="16" y="14" width="64" height="9" fill="#c8c8c8"/><rect x="16" y="23" width="64" height="9" fill="#e6e6e6"/><rect x="16" y="32" width="64" height="9" fill="#cdcdcd"/><rect x="16" y="41" width="64" height="9" fill="#e6e6e6"/><rect x="48" y="32" width="16" height="9" fill="#f0b9b9"/><path d="M32,14 V50 M48,14 V50 M64,14 V50" fill="none"/></g><path d="M71,17 L74,20 L77,17" stroke="#26302a" stroke-width="1.5" fill="none"/></symbol>',
    '<symbol id="s-export" viewBox="0 0 96 64">' + win(4, 12, 40, 40) + APP(16, 24, 16) + '<path d="M47,32 H58" stroke="#2f7340" stroke-width="2.5" stroke-linecap="round"/><path d="M56,26 L63,32 L56,38 Z" fill="#2f7340"/><svg x="62" y="12" width="32" height="40" viewBox="0 0 70 84"><use href="#i-csv"/></svg></symbol>',
    /* the other two pages, for the signposts below the download */
    '<symbol id="s-browser" viewBox="0 0 96 64"><rect x="4" y="4" width="88" height="56" rx="5" fill="#ffffff" stroke="#2b68b8" stroke-width="2"/><path d="M4,15 H92" stroke="#2b68b8" stroke-width="2"/><circle cx="11" cy="9.5" r="1.8" fill="#2b68b8"/><circle cx="17" cy="9.5" r="1.8" fill="#2b68b8"/><rect x="24" y="7" width="40" height="5" rx="2.5" fill="#dfeaf6"/>' +
      '<g stroke="#8a8a8a" stroke-width="1"><rect x="12" y="21" width="72" height="8" fill="#c8c8c8"/><rect x="12" y="29" width="72" height="8" fill="#e6e6e6"/><rect x="12" y="37" width="72" height="8" fill="#cdcdcd"/><rect x="12" y="45" width="72" height="8" fill="#e6e6e6"/><rect x="48" y="37" width="18" height="8" fill="#f0b9b9"/><path d="M30,21 V53 M48,21 V53 M66,21 V53" fill="none"/></g></symbol>',
    '<symbol id="s-works" viewBox="0 0 96 64"><rect x="3" y="3" width="90" height="58" rx="6" fill="#f4f9f2" stroke="#2f7340" stroke-width="2"/><svg x="8" y="7" width="15" height="10" viewBox="0 0 30 22" style="color:#2f7340"><use href="#o-mac"/></svg>' +
      '<svg x="10" y="22" width="22" height="26" viewBox="0 0 70 84"><use href="#i-csv"/></svg><path d="M34,35 H42" stroke="#2f7340" stroke-width="2.2" stroke-linecap="round"/><path d="M41,31 L46,35 L41,39 Z" fill="#2f7340"/>' + APP(48, 26, 18) +
      '<path d="M68,35 H74" stroke="#2f7340" stroke-width="2.2" stroke-linecap="round"/><path d="M73,31 L78,35 L73,39 Z" fill="#2f7340"/><svg x="70" y="22" width="22" height="26" viewBox="0 0 70 84"><use href="#i-csv"/></svg>' +
      '<path d="M44,50 L50,52 V55 Q50,58 47,59 Q44,58 44,55 Z" fill="none" stroke="#2f7340" stroke-width="1.4" stroke-linejoin="round"/></symbol>',
    /* places and platforms: currentColor, so they take the page's ink */
    '<symbol id="o-mac" viewBox="0 0 30 22"><rect x="5" y="2" width="20" height="13" rx="1.5" fill="none" stroke="currentColor" stroke-width="2"/><path d="M1,17 H29 L27,20.5 H3 Z" fill="currentColor"/></symbol>',
    '<symbol id="o-win" viewBox="0 0 30 22"><rect x="3" y="1.5" width="24" height="15" rx="1.5" fill="none" stroke="currentColor" stroke-width="2"/><path d="M11,20.5 H19 M15,16.5 V20.5" stroke="currentColor" stroke-width="2"/><rect x="10" y="5" width="4.5" height="3.5" fill="currentColor"/><rect x="15.5" y="5" width="4.5" height="3.5" fill="currentColor"/><rect x="10" y="9.5" width="4.5" height="3.5" fill="currentColor"/><rect x="15.5" y="9.5" width="4.5" height="3.5" fill="currentColor"/></symbol>',
    '<symbol id="o-linux" viewBox="0 0 30 22"><rect x="3" y="1.5" width="24" height="15" rx="1.5" fill="none" stroke="currentColor" stroke-width="2"/><path d="M11,20.5 H19 M15,16.5 V20.5" stroke="currentColor" stroke-width="2"/><path d="M8,6 L11,9 L8,12 M13,12 H18" stroke="currentColor" stroke-width="1.8" fill="none" stroke-linecap="round" stroke-linejoin="round"/></symbol>',
    '<symbol id="i-shield" viewBox="0 0 24 24"><path d="M12,2 L20,5 V11 Q20,18 12,22 Q4,18 4,11 V5 Z" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/><path d="M8.5,12 L11,14.5 L15.5,9.5" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"/></symbol>',
    '<symbol id="i-globe" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10" fill="none" stroke="currentColor" stroke-width="2"/><ellipse cx="12" cy="12" rx="4.5" ry="10" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M2,12 H22 M4,7 H20 M4,17 H20" stroke="currentColor" stroke-width="1.6"/></symbol>',
    '<symbol id="i-down" viewBox="0 0 24 24"><path d="M12,3 V15 M7,10.5 L12,15.5 L17,10.5" stroke="currentColor" stroke-width="2.4" fill="none" stroke-linecap="round" stroke-linejoin="round"/><path d="M4,17 V20 H20 V17" stroke="currentColor" stroke-width="2.4" fill="none" stroke-linecap="round" stroke-linejoin="round"/></symbol>',
    '<symbol id="i-chip" viewBox="0 0 24 24"><rect x="6" y="6" width="12" height="12" rx="2" fill="none" stroke="currentColor" stroke-width="2"/><path d="M9,2.5 V6 M15,2.5 V6 M9,18 V21.5 M15,18 V21.5 M2.5,9 H6 M2.5,15 H6 M18,9 H21.5 M18,15 H21.5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></symbol>',
    '<symbol id="i-csv" viewBox="0 0 70 84"><path d="M8,2 H50 L68,20 V78 Q68,82 64,82 H12 Q8,82 8,78 Z" fill="#f2f2f2" stroke="#4a4a4a" stroke-width="2"/><path d="M50,2 V20 H68" fill="#d9d9d9" stroke="#4a4a4a" stroke-width="2" stroke-linejoin="round"/><rect x="20" y="26" width="38" height="34" fill="#a6db8f" stroke="#3b6e34" stroke-width="1.5"/><rect x="20" y="26" width="38" height="8" fill="#79c162" stroke="#3b6e34" stroke-width="1.5"/><path d="M33,26 V60 M46,26 V60 M20,43 H58 M20,51 H58" stroke="#3b6e34" stroke-width="1.5"/><rect x="1" y="52" width="40" height="20" rx="4" fill="#7cc96a" stroke="#2c5a2c" stroke-width="2"/>' + T(21, 66.5, 12, "#1d331a", "CSV") + "</symbol>"
  ];

  function ready(fn) { if (document.readyState !== "loading") fn(); else document.addEventListener("DOMContentLoaded", fn); }

  ready(function () {
    var sprite = document.createElement("div");
    sprite.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" style="position:absolute;width:0;height:0" aria-hidden="true">' + S.join("") + "</svg>";
    document.body.insertBefore(sprite.firstChild, document.body.firstChild);

    var head = document.querySelector("header[data-bar]");
    if (head) {
      head.className = "bar";
      head.innerHTML = '<div class="in"><a class="home" href="index.html" aria-label="HappyCamper, download page"><img src="' + DL.icon + '" alt=""><span>HappyCamper</span></a>' +
        '<nav aria-label="HappyCamper pages"><span aria-current="page">Download</span><a href="' + DL.links.demo + '">Demo</a><a href="' + DL.links.details + '">Details</a></nav></div>';
    }
    var foot = document.querySelector("footer[data-foot]");
    if (foot) {
      foot.className = "sitefoot";
      foot.innerHTML = '<div>A free app created by <a href="https://github.com/jaymoran103">Jay Moran</a></div>' +
        '<div><nav class="footpills" aria-label="HappyCamper pages"><a href="' + DL.links.demo + '">Demo</a><a href="' + DL.links.details + '">Details</a></nav></div>';
    }

    fetch("https://api.github.com/repos/jaymoran103/happycamper-heart/releases/latest")
      .then(function (r) { return r.json(); })
      .then(function (d) {
        var v = (d.tag_name || "").replace(/^v/, "");
        if (!v) return;
        document.querySelectorAll("[data-version]").forEach(function (el) { el.textContent = (el.dataset.version || "Version ") + v; });
        if (d.published_at) {
          var when = new Date(d.published_at).toLocaleDateString("en-US", { year: "numeric", month: "long", day: "numeric", timeZone: "UTC" });
          document.querySelectorAll("[data-reldate]").forEach(function (el) { el.textContent = el.dataset.reldate + when; });
        }
      })
      .catch(function () {});

    fetch(BASE + "whatsnew.json")
      .then(function (r) { return r.json(); })
      .catch(function () { return WHATSNEW; })
      .then(function (d) {
        if (!d) return;
        document.querySelectorAll("[data-whatsnew-label]").forEach(function (el) { el.textContent = d.label || ""; });
        document.querySelectorAll("[data-whatsnew-list]").forEach(function (list) {
          (d.items || []).forEach(function (text) { var li = document.createElement("li"); li.textContent = text; list.appendChild(li); });
        });
      });

    if (typeof window.render === "function") window.render(DL);
  });
})();

/* Small shared renderers: an OS picker and a step pictogram. */
window.DLkit = {
  pic: function (step, cls) {
    return '<svg class="pic ' + (cls || "") + '" viewBox="0 0 96 64" aria-hidden="true"><use href="#' + step.pic + '"/></svg>';
  },
  picker: function (DL, current, onPick, cls) {
    var box = document.createElement("div");
    box.className = "picker " + (cls || "");
    box.setAttribute("role", "radiogroup");
    box.setAttribute("aria-label", "Your computer");
    DL.os.forEach(function (o) {
      var b = document.createElement("button");
      b.type = "button";
      b.setAttribute("role", "radio");
      b.dataset.os = o.id;
      b.innerHTML = DL.svg(o.icon) + '<span class="nm">' + o.name + '</span><span class="sb">' + o.sub + "</span>";
      b.addEventListener("click", function () { mark(o.id); onPick(o.id); });
      box.appendChild(b);
    });
    function mark(id) { box.querySelectorAll("button").forEach(function (b) { b.setAttribute("aria-checked", String(b.dataset.os === id)); }); }
    mark(current);
    return box;
  }
};

/* G's step band, shared by I onward. extra: optional html for one more tile. */
window.DLkit.band = function (DL, o, extra) {
  var K = window.DLkit, steps = DL.steps[o.steps];
  return '<h2>Installing on ' + o.name + '</h2><ol class="strip">' + steps.map(function (s) {
    return '<li class="' + (s.gate ? "gate" : "") + '"' + (s.more ? ' title="' + s.more.replace(/<[^>]+>/g, "") + '"' : "") + ">" + K.pic(s) + s.text + "</li>";
  }).join("") + (extra || "") + "</ol><p>" + DL.trustHTML(o.steps) + "</p>";
};
window.DLkit.csv = '<svg class="csv" viewBox="0 0 70 84" aria-hidden="true"><use href="#i-csv"/></svg>';
