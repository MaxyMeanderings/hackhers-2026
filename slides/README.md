# Build with AI. Own the evidence.

90-minute concepts-first workshop: Claude, Claude Code, spec-driven development,
adversarial agents, and claim-level works cited. A short section compares gstack,
BMad and Nightshift. Includes 30 core/reference slides plus 6 tool/setup appendices,
speaker notes, an interactive evidence reveal, and five student handouts.

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

The 32-slide deck centers the full coach, its build steps, and hackathon use.
The clickable side rail follows six modules. Exact teaching prompts live in
[walkthrough/](walkthrough/); student assets are bundled under public/.
The earlier deck is retained in archive/deck-before-coach-walkthrough.md.
