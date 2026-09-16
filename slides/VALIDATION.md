# Coach walkthrough validation

## Checkpoints and source image — September 16, 2026

- The 40-slide Pages build passed.
- Chrome checked checkpoints 11, 21, 33, and 38 for footer overlap. An initial
  overlap on slide 21 was corrected; all four passed the repeated layout check.
- Section navigation reached slides 26, 34, and 39 with no page errors.
- The original post thumbnail was visually inspected and opened a new tab
  containing the unmodified 1293 × 2198 image.
- Setup and behavior checkpoint screenshots were visually inspected.


## Copilot introduction and PR publishing — September 16, 2026

- The 37-slide GitHub Pages build passed.
- Chrome rendered slide 3 without measured overlap into the source footer.
- All five shifted section links reached slides 5, 8, 24, 31, and 36.
- No uncaught browser errors occurred during these checks.
- The new slide was visually inspected at 1280 × 720.
- Pull request builds use read-only repository permissions; publication is
  restricted to non-PR runs on main.


## Engineering additions — September 16, 2026

- Static production build succeeded for the 36-slide deck.
- PDF export completed successfully to workshop.pdf.
- Chrome checked slides 19–23, 30, 33, 35, and 36: no uncaught page errors
  or measured content overflow into the source footer.
- SOLID, Big O, and tool-scope slides were visually inspected.
- Clicking Use it, Your hackathon, and Take it away navigated to slides 23,
  30, and 35 and marked the corresponding section current.
- The existing caught FloatingVue/twoslash warning appeared during PDF export.
- Definitions and tool descriptions have linked primary sources in SOURCES.md.

## GitHub Pages preparation — September 16, 2026

- Production build with the repository base path and hash routing succeeded.
- Chrome opened slides 1, 2, 19, 33, and 36 from the subdirectory preview
  without page errors or failed HTTP responses.
- All seven student download links returned Markdown with HTTP 200.
- The Build it navigation button opened slide 7 using hash routing.

## Earlier 32-slide baseline


- Slidev static build succeeded; PDF export produced 32 pages.
- Browser visited all 32 slides with Source Code Pro loaded. No uncaught page errors
  or measured overflow of headings, paragraphs, lists, code, quotes or layout groups.
- Side navigation correctly marked past/current/future modules. Clicking Build it
  navigated to slide 7 and set aria-current on that section.
- Seven student asset links were fetched from the static preview and byte-compared
  with the bundled prompt, templates and walkthrough files.
- The recorded conversation, file-tree and coach-start slides were visually inspected.
  The build artifact slide was also inspected in the PDF with its section rail.
- Instructor-status content is absent from the presentation; earlier slides retained
  in archive/deck-before-coach-walkthrough.md.
- Export retains the previously observed caught FloatingVue/twoslash setup warning;
  it completed and inspected slides rendered correctly.

Validation covers the presentation and navigation. No new coach/model build was run
as part of this deck edit. Recorded excerpts are labeled; authored teaching prompts
are not historical execution receipts. See SOURCES.md for provenance.
