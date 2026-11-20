# Deploying the site

`site/` is a complete static site. It needs no build step on the server.

## Before publishing

1. If the demo build changed, run `python3 -I tools/site/make-site.py` from the repo root. It rewrites both pages, so make lasting changes in `make-site.py` rather than in `site/*.html`.
2. Open `site/index.html` and check that Download and Demo switch between the pages.
3. Commit and push to `main`.

## Serve from this repo with GitHub Pages

1. In the repo's Settings, open Pages and set Source to "GitHub Actions".
2. Add `.github/workflows/pages.yml` with the workflow below, then push it.
3. The site appears at `https://jaymoran103.github.io/happycamper-demo/` once the workflow finishes.

```yaml
name: Deploy site
on:
  push:
    branches: [main]
  workflow_dispatch:
permissions:
  contents: read
  pages: write
  id-token: write
concurrency:
  group: pages
  cancel-in-progress: true
jobs:
  deploy:
    runs-on: ubuntu-latest
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    steps:
      - uses: actions/checkout@v4
      - uses: actions/configure-pages@v5
      - uses: actions/upload-pages-artifact@v3
        with:
          path: site
      - id: deployment
        uses: actions/deploy-pages@v4
```

## Serve from another repo

1. Copy everything in `site/` into the folder that repo publishes, such as `docs/` in happycamper-heart.
2. Keep the files together. The pages link to each other and to `icon.png` and `whatsnew.json` by relative path.
3. In that repo's Pages settings, check that the source is the branch and folder you copied into.
