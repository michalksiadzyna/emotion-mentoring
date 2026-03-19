# Emotion Mentoring — Decisions

> Strategos file. Crystallized decisions — the "what", no reasoning. Check before every action.
> Last updated: 2026-03-10

---

## Architecture
- Static HTML, single-page approach per language. All CSS and JS inline per page.
- Hosted on GitHub Pages. Repository: private.
- No build tools, no frameworks, no CMS. Raw HTML/CSS/JS.
- Domain: emotionmentoring.com

## Design System
- Dark luxury aesthetic: `--black: #141418`, `--gold: #c9a96e`, `--white: #f5f3ee`
- Fonts: Playfair Display (serif, headings) + Barlow (sans-serif, body)
- Transition speed: 0.1s (0.3s rejected). Exception: FAQ accordion max-height at 0.4s.
- Hover system: comprehensive — gold accents, subtle lifts, grouped hover zones
- Portrait treatment: grayscale(15%) contrast(1.05), full color on hover
- Corner accent frames on portrait photos
- Diamond divider SVGs between sections

## Bilingual Strategy
- English (`index.html`) is primary. Polish (`index-pl.html`) mirrors structure.
- `hreflang` tags link EN and PL versions.
- English FAQ has expanded SEO-depth answers (5 paragraphs each). Polish FAQ has original shorter answers (expansion pending).
- Foundation pages exist in both languages.
- Book page is English-only.
- Thank-you pages exist in both languages.

## SEO
- Complete on all 7 pages: JSON-LD structured data, meta tags, Open Graph, Twitter Cards, hreflang, canonical URLs.
- `favicon.svg` deployed across all pages.
- `robots.txt` allows all crawlers. `sitemap.xml` lists 5 indexable URLs (excludes thankyou pages).
- SEO title pattern: "Page Title — Emotion Mentoring" or "Emotion Mentoring — Peak Mental Performance" (main).

## Content
- 9 FAQ questions with expanded answers (EN). SEO-optimized titles.
- 6 client testimonials on main page (real client quotes, British English preserved in quotes).
- Author voice uses American English ("analyze" not "analyse").
- Free 45-minute assessment as CTA throughout.
- Exit-intent modal on index page for abandoning visitors.

## Form & Backend
- Formspree for form submission.
- Fields: name, email, preferred time, vision statement.
- Success redirects to thankyou.html. Error path needs fixing (FIXPLAN 3.1).
- Thank-you page includes upgrade options (session packages).

## Branding
- Practitioner name: Michal Ksiadzyna (operates as "Shen")
- Method: The Shen Method
- Book: The Secret Book of Emotions
- Foundation: Shen Foundation
- Email: michal@emotionmentoring.com

## Fix Plan Status
- FIXPLAN.md contains 6 phases, 30+ individual fixes across accessibility, performance, JS bugs, CSS consistency, dead code cleanup, and load time optimization.
- Phase priority: Accessibility > Performance > JS fixes > CSS > Cleanup > Optimization.
- Branch strategy: `fix/landing-page` branch, commit after each phase.

## Website Update Pipeline
- Website update is blocked until two prerequisites are complete, in order:
  1. Complete the Shen Method Canon (all laws finalized)
  2. Complete The Secret Book of Emotions (book finished)
- Only after both are done: update the website with new book content and deploy.
- No website content changes until this pipeline clears.

## Content Engine
- Project Knifehead handles multi-platform content (LinkedIn, X, Instagram, Facebook).
- Content drives discovery; the practitioner closes. The website is the conversion point, Knifehead is the funnel.
