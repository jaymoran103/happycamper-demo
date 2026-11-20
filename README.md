# HappyCamper

A schedule management app for summer camps. 

See [the live site](eelslap.com) for the 2026 distribution, an in-browser demo, and how the app details.

See sections below for info on this repo and related codebases.


TODO: Add image of live demo UI.


---
<details><summary>Related Repos</summary>

- [happycamper-heart](https://github.com/jaymoran103/happycamper-heart): the 2026 distribution, v2.3 to v2.5
- [happycamper-public](https://github.com/jaymoran103/happycamper-public): v2.2, used in 2025
- [happycamper-v3](https://github.com/jaymoran103/happycamper-v3): an web-oriented refactor, designed throughtfully in spring 2026, shelved in favor of the more pragmatic happycamper-heart.
- [NameSwap](https://github.com/jaymoran103/NameSwap): purpose-built tool for reliable, low frills name anonymization.
- [Current download page](https://jaymoran103.github.io/happycamper-heart/docs/) - soon to be replaced with this more rounded trio of pages. As a frequently linked distribution point for camp staff, this will be continually updated to point toward the newest happycamper distribution point, which for the foreseeable future will be this repo's trio of pages, served statically,

</details>

---
<details><summary>Repo Content</summary>

| Folder | Content |
| --- | --- |
| `site/` | The static site: `index.html` (download) and `demo.html` (demo). Serve it as-is. |
| `archive/` | Design rounds kept as a record. `1118-happycamper-demo` is phase 1 and `1120-page-pairing` is phase 2. Phase 1's `index.html` shows its lineage. |
| `tools/demo-build/` | Builds `demo.html`'s source page from fictional data, and checks it against the real app engine. |
| `tools/site/` | Rebuilds both site pages with the shared header and footer. |
| `docs/` | Plans, the deployment runbook, and longer-term notes. |
</details>