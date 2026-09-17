# Coach walkthrough validation

## API credits onboarding slides — September 17, 2026

- Four slides inserted after the workshop-links slide (now slides 4–7): claim
  credits, apply, Console dashboard, Claude Code /login. Every later slide
  shifted by four; the section rail, INSTRUCTOR.md, README.md, SOURCES.md,
  and ASSETS.md were updated to match. Slide references in SOURCES.md and
  ASSETS.md that still used older numbering now match the deck.
- The Pages build passed for 35 core slides, 10 optional follow-on slides,
  and two closing slides (47 total, 94 slide separators), with the starter
  packaging script run beforehand.
- The Slidev dev server rendered slides 3–7 at 1280 × 720 in the in-app
  browser; the four new slides were visually inspected with no content
  reaching the source footer. All four new images loaded at native resolution.
- Section rail targets were checked after the shift: slides 10, 13, 29, 34,
  36, and 46 opened the expected headings and marked the matching section current.
- The QR code was replaced with the event offer code supplied by the organizer
  on September 17, 2026; it decodes to the URL recorded in SOURCES.md and the
  slide link matches it. The application screenshot still shows an earlier
  event header and is flagged in the speaker notes and ASSETS.md for
  replacement before the event.

## Student starter and reference separation — September 16, 2026

- The complete pre-separation snapshot was pushed to reference/completed-coach
  at commit 4e4e8ed2edcec7299fa403cccedeca65ba22487d.
- The student ZIP contains exactly README.md, BUILD-BRIEF.md, BUILD-STEPS.md,
  and .gitignore under one folder. Archive contents match the canonical files.
- Completed coach copies are absent from the public assets and built site.
- All linked reference files exist in the preserved branch.
- The production Pages build passed with generated starter packaging.
- Chrome checked slides 11, 30, and 31 with no measured footer overlap.
- The ZIP and both generated build handouts returned HTTP 200 locally.
- Ignored local runtime state and bytecode were preserved; they are excluded
  from Git and the student ZIP. No coach model evaluation was rerun.


## Student-built coach correction — September 16, 2026

- The Pages build passed for 30 core slides plus 10 optional follow-on slides.
- Chrome checked revised slides 1, 4, 5, 10, 11, 14, 16, 17, 22, 23, 28–32
  without measured content overflow or uncaught page errors.
- Implementation and testing checkpoints were visually inspected.
- All four checkpoints now operate on the student’s own build folder and spec.
  Reference coach responses are explicitly excluded as evidence for that build.
- The bundled build walkthrough matches the authoring copy.


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
