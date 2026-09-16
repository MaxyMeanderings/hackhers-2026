# Build with AI. Own the evidence.

90-minute workshop on building and using a go-to-market coach with Claude Code.
Includes 40 slides, speaker notes, student handouts, and a four-slide engineering
interlude covering DRY, SOLID, ACID, Big O, and convention over configuration.
Four timed checkpoints cover working access, one coach behavior, a saved
team handoff, and one working slice. A brief comparison explains where BMAD and gstack fit in the workflow.

## Present

Tested authoring runtime: Node 24.13.1. Install dependencies, then start Slidev:

```bash
npm ci
npm run dev
```

Open the local URL printed by Slidev. Use arrow keys to navigate; `/presenter` opens
speaker view. The dev server is bound to localhost. Students viewing the PDF or built
website do not need this authoring toolchain. Sources: package.json:6 and
https://sli.dev/guide/.

## Build / export

```bash
npm run build
npm run export
```

The static site is in dist/. The PDF is workshop.pdf. PDF export needs Playwright Chromium;
on this Mac the tested command uses the existing Chrome executable:

```bash
npm run export -- --executable-path "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
```

Source: package.json:7; https://sli.dev/guide/exporting.

- [Facilitator guide](INSTRUCTOR.md)
- [Works cited](SOURCES.md)
- [Student handouts](handouts/)
- [Main slide source](slides.md)

Workshop design is not a claim of production-ready agent behavior. Actual false-pass
examples are labeled and sourced. Synthetic exercises do not represent real fieldwork.

## Coach walkthrough

The 40-slide deck centers the full coach, its build steps, and hackathon use.
The clickable side rail follows six modules. Exact teaching prompts live in
[walkthrough/](walkthrough/); student assets are bundled under public/.
The earlier deck is retained in archive/deck-before-coach-walkthrough.md.

## Publish to GitHub Pages

The workflow in [.github/workflows/deploy-slides.yml](../.github/workflows/deploy-slides.yml)
builds slide changes when a pull request targeting main is opened or updated.
After the pull request is merged, the push to main automatically rebuilds and
publishes the deck at https://doctor-ew.github.io/hackhers-2026/.
Pull request builds validate the changes; the public deck updates after merge.
Manual publishing is available from GitHub Actions on main. Repository Pages
settings must use GitHub Actions as the build source.

Run `npm run build:pages` to reproduce the hosted build. It uses the repository
base path and hash routing so shared slide links work on GitHub Pages. The default
local build and development commands remain available. Student download links are
relative to the presentation root.

References: [Slidev hosting](https://sli.dev/guide/hosting) and
[GitHub Pages API](https://docs.github.com/en/rest/pages/pages).
