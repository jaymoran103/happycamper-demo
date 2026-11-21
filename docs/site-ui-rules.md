# HappyCamper site — UI rules

Rules for every page in `site/`, drawn from ui-iterator rounds. Append with the next number and never renumber. A rule believed wrong gets `**Status:** challenged` on its own line and waits for Jay.

## Where the model came from

Round `archive/1120-page-trio`, the Details page (formerly Codebase). The model is J: icons over text, short sections, labels that only name things.

- **Prevailed:** A's download and demo pages → B's timeline and repo pills, plus C's "your computer" box with CSVs drawn as tables → E/F merge those into one diagram, and F adds outside sources → G retells it in icons → H adds four labels and short sections → I: three columns, matching device and internet boxes, the green header bar → **J**: one-way flow, app tiles with the spreadsheet apps staggered as one group, a one-line caption, and the Data Note.
- **Ruled out:** opening privacy by describing what websites do (A), a defensive AI section (A), D's contents card, lanes and layer stack, E/F's described sequence cards, and long paragraphs around diagrams (E–G).

---

1. **Show it with an icon. Use a word only where no icon can say it.** E and F explained the diagram in prose, so readers read everything twice.
   _Seen: 1120-page-trio E, F → G_

2. **Draw familiar symbols as simple flat SVG.** That means no gradients, little detail, and a CSV drawn as both a file and a table. Use pasted brand art only as a reference.
   _Seen: 1120-page-trio G_

3. **Labels name things. They never explain how or why.** In I, the only words are camper roster, activity roster, merged roster, Your device, Internet, HappyCamper and Java.
   _Seen: 1120-page-trio H_

4. **Give each idea its own plain heading and two or three sentences.** Long paragraphs read as padding, and the reader skips them.
   _Seen: 1120-page-trio G → H_

5. **Lead with what the app does. Never lead with what others do worse.** Opening privacy with what websites do made a safe app sound risky.
   _Seen: 1120-page-trio A_

6. **Tell AI use as one fact in the timeline, after the data note.** A separate section about it read as defensive.
   _Seen: 1120-page-trio A_

7. **Use Jay's wording verbatim. Fix only typos and punctuation, and list each fix when handing over.** Rewording drifted from his intent and voice.
   _Seen: 1120-page-trio H, I_

8. **When feedback names an earlier iteration's element, restore it exactly. Add nothing and drop nothing.** The timeline regressed three times: cards in E/F, no prose in G, old prose in H.
   _Seen: 1120-page-trio E–H_

9. **Timeline: year, a two-word stage name, and repo pills reading `name • vX` that link to GitHub.** Show only the newest version. Each pill reads "View in GitHub" on hover, and the per-year text goes under the drawing.
   _Seen: 1120-page-trio G, H, I_

10. **Mark a place, like your device or the internet, with an icon and a word in the box's corner.** Centered over one element, the label read as part of that element.
    _Seen: 1120-page-trio H → I_

11. **Lay a diagram out in columns that mean something. Stack peers, and cluster interchangeable ones.** Stacking the three CSVs shows they are the same kind of thing. The destination apps (Sheets, Excel, Numbers, a text editor and a dashed "…" wild card) staggered in one slightly overlapping group say "any of these". Stacked rows read as distinct paths.
    _Seen: 1120-page-trio I → J_

12. **Every arrow must be literally true. Draw one direction of flow with large heads, and use diagonals to fan in or out.** In I, Sheets pointed into the activity roster, a false claim, and rows of horizontal arrows hid the direction. An implication of flexibility belongs in the grouping, not in an arrow.
    _Seen: 1120-page-trio I → J_

13. **Change only the part under test, and keep everything else identical to the base iteration.** Otherwise one review mixes two questions.
    _Seen: 1120-page-trio G_

14. **Export every diagram and look at it before reporting.** The rasterizer drops `<a>` and ignores `display="none"`. Give links inline colours, and check a copy with the links removed.
    _Seen: 1120-page-trio G_

15. **Align each element with what it connects to, and center the rest with white space around it.** The camp app sits at the midpoint of the two rosters it feeds, and the spreadsheet cluster sits level with the merged roster. HappyCamper is sized to its content and centered vertically.
    _Seen: 1120-page-trio J_

16. **Draw every app as the same size of rounded square tile.** When grouping tiles, offset them vertically as well as overlapping them. Bare logos packed side by side merged into a mass of green shapes.
    _Seen: 1120-page-trio J_

17. **Give each diagram a one-line caption saying what it shows.** The caption states the flow in plain words. Reasons belong in the sections.
    _Seen: 1120-page-trio J_

18. **Say each thing once on a page.** The footer dropped its email line because the history already gives the address.
    _Seen: 1120-page-trio J_

19. **Show each install step as one pictogram with a short caption.** Bullets read as dense, a diagram over-depicted, and one step per screen hid the whole path.
    _Seen: 1121-download-page B, C–H → G_

20. **Emphasize the likely choice, and disclose the rest on request.** Four equal OS modules spent the full width on a display only a quarter relevant to any one visitor.
    _Seen: 1121-download-page G_

21. **Never repeat a link the header already gives, and drop an element that can't say why it's there.** The try-it section paired sample rosters with a second web demo link.
    _Seen: 1121-download-page G_

22. **Keep the green paper. Blue is the only second hue.** G's tan read as a different site.
    _Seen: 1121-download-page D, E, G, H_

## Current look

- **Header:** a sticky forest-green bar (`#1a672c`). The logo sits directly on the green with the name, on the left. The routes are pills on the right, with the current page filled white. The logo links to the download page. The routes are Download, Demo and Details. Using this bar on every page is still open.
- **Page:** paper `#cfe3c9`, ink `#26302a`, Verdana, a 46rem column, and a left-aligned heading with no summary line under it.
- **Footer:** "A free app created by Jay Moran", then the other pages as outlined green pills. Nothing else.
- **Aside boxes:** a callout such as the Data Note sits in a box darker than the page (`#bbd6b4`), never white.
- **Diagram boxes:** device `#f4f9f2` with a `#2f7340` edge, internet `#eef5fb` with a `#2b68b8` edge, and a flagged cell in `#f0b9b9`. Green arrows run inside the device and blue arrows cross to the internet. App tiles are 60px white rounded squares with a `#9fb3c8` edge, except the camp app's solid purple. The wild card tile has a dashed edge. Overlapping tiles share only their corners, so no logo is hidden.
- **Next:** the download and demo pages are unchanged since A. Apply these rules to them.
