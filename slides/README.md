# Build with AI. Own the evidence.

90-minute workshop: students build their own go-to-market coach from a supplied
build brief and an approved specification using Claude Code. Deliverables are a
spec, coach prompt, four output templates, test cases, and saved test evidence.

The deck has 37 core slides, 10 optional follow-on slides, and two closing slides about using the
finished coach. Four checkpoints cover setup, spec approval, implementation,
and testing the student-built coach. Sponsored API credit sign-in, engineering
principles, and the copilot mindset support those activities.

## Present

Tested authoring runtime: Node 24.13.1. Python 3 is also required to package the
student starter. Install dependencies, then start Slidev:

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

The 49-slide deck centers students building and testing their own coach.
The clickable side rail marks the build workflow and optional follow-on material. Exact teaching prompts live in
[walkthrough/](walkthrough/); student assets are bundled under public/.
The earlier deck and completed coach are preserved on the reference/completed-coach branch.

## Publish to GitHub Pages

The workflow in [.github/workflows/deploy-slides.yml](../.github/workflows/deploy-slides.yml)
builds every pull request targeting main when it is opened or updated.
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

## Student starter packaging

The canonical student files live in ../starter/. Before development, builds, and
PDF export, npm runs ../scripts/prepare-starter.py to generate the four-file
public/hackhers-starter.zip and the two public build handouts. The script checks
an explicit file list and rejects a bundled public/coach directory. It never
packages the repository root or completed reference branch.

Edit the canonical starter files, not generated copies. The existing handout URLs
remain available. Full reference prompts and examples link to the completed
branch on GitHub instead of being bundled with the student site.
