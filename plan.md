# Emotion Mentoring — Plan

> Strategos file. Execution tasks with status and ownership.
> Last updated: 2026-03-09

---

## Legend
- [x] = Complete
- [ ] = Pending
- **AUTONOMOUS** = Claude executes alone
- **COOPERATIVE** = Needs user input or review
- **HUMAN-ONLY** = Only the user can do this
- **BLOCKER** = Blocks other tasks

---

## Phase 0: Foundation (COMPLETE)

- [x] Design and build English landing page (`index.html`) — AUTONOMOUS
- [x] Design and build Polish landing page (`index-pl.html`) — AUTONOMOUS
- [x] Build Shen Foundation pages (EN + PL) — AUTONOMOUS
- [x] Build book download page (`the-secret-book-of-emotions-shen.html`) — AUTONOMOUS
- [x] Build thank-you pages (EN + PL) with upgrade options — AUTONOMOUS
- [x] Deploy to GitHub Pages — AUTONOMOUS
- [x] Register domain emotionmentoring.com — HUMAN-ONLY
- [x] Configure DNS for GitHub Pages — COOPERATIVE
- [x] Create and deploy favicon — AUTONOMOUS
- [x] Extract portrait from base64 to external file — AUTONOMOUS
- [x] Create WebP version of portrait — AUTONOMOUS
- [x] Deploy robots.txt and sitemap.xml — AUTONOMOUS
- [x] Full SEO pass: JSON-LD, meta tags, OG, Twitter Cards, hreflang, canonical URLs — AUTONOMOUS
- [x] Expand English FAQ answers for SEO depth — COOPERATIVE
- [x] Logo creation (dark-bg + transparent variants, SVG + PNG) — AUTONOMOUS

## Phase 1: Content Review & Polish FAQ Parity

- [ ] **1.1** Review 9 expanded English FAQ answers for tone, accuracy, and representation — **HUMAN-ONLY**
  - All 9 answers in `index.html`. User must personally verify the content represents the Shen Method correctly.

- [ ] **1.2** Expand Polish FAQ answers to match English depth — **COOPERATIVE**
  - `index-pl.html` has original short answers. Translate/adapt the expanded English answers to Polish.
  - Depends on: 1.1 (English answers finalized first)

- [ ] **1.3** Optimize Polish FAQ titles for SEO — **COOPERATIVE**
  - English FAQ titles were SEO-optimized. Polish titles are original. Research Polish search terms and propose optimized titles.

- [ ] **1.4** Provide real client count numbers — **HUMAN-ONLY** / **BLOCKER**
  - Proof strip currently shows "Multiple Nationalities" / "Dozens of Clients". Real figures needed.
  - Blocks: updating proof strip on both language versions

- [ ] **1.5** Update proof strip with real numbers — **AUTONOMOUS**
  - Depends on: 1.4

## Phase 2: FIXPLAN Execution (Technical Debt)

- [ ] **2.1** Phase 1 fixes: Accessibility — **AUTONOMOUS**
  - Wrap form in `<form>` element, add `<label>` elements, ARIA attributes on FAQ accordion, ARIA + keyboard on exit modal, replace clickable `<div>` with `<a>`, replace inline event handlers, add `aria-hidden` to decorative SVGs, add `:focus-visible` styles
  - Scope: all pages. See FIXPLAN.md Phase 1 (items 1.1–1.8)

- [ ] **2.2** Phase 2 fixes: Performance — **AUTONOMOUS**
  - Investigate base64 in foundation.html, deduplicate SVG logo, add preconnect for fonts.gstatic.com, remove Cloudflare email obfuscation
  - See FIXPLAN.md Phase 2 (items 2.1–2.5, noting 2.1 already done)

- [ ] **2.3** Phase 3 fixes: JavaScript — **AUTONOMOUS**
  - Fix silent false-success on form submission, fix upgrade submission error handling, add email validation, consolidate scroll-reveal strategy
  - See FIXPLAN.md Phase 3 (items 3.1–3.4)

- [ ] **2.4** Phase 4 fixes: CSS & Layout — **AUTONOMOUS**
  - Normalize h2 styles, normalize transition speeds to 0.1s, fix mobile padding, add 600px breakpoint, remove `!important`, move inline styles to classes
  - See FIXPLAN.md Phase 4 (items 4.1–4.6)

- [ ] **2.5** Phase 5 fixes: Cleanup — **AUTONOMOUS**
  - Remove dead CSS/HTML, fix duplicate definitions, fix spelling, normalize typography, merge duplicate FAQ answers
  - See FIXPLAN.md Phase 5 (items 5.1–5.7)

- [ ] **2.6** Phase 6 fixes: Load Time Optimization — **AUTONOMOUS**
  - Minify CSS/JS, optimize SVGs, optimize font loading, image compression, DOM cleanup, resource hints, final size audit
  - See FIXPLAN.md Phase 6 (items 6.1–6.8)

## Phase 3: Media & Social Proof

- [ ] **3.1** Record 60-90s intro video for the website — **HUMAN-ONLY** / **BLOCKER**
  - No script provided yet. Blocks video embed on site.

- [ ] **3.2** Create video script/outline — **COOPERATIVE**
  - Draft a script aligned with the website's tone and CTA. User records.

- [ ] **3.3** Embed video on landing page — **AUTONOMOUS**
  - Depends on: 3.1
  - Add video section to index.html (and index-pl.html if PL version recorded)

- [ ] **3.4** Gather English-speaking client testimonials — **HUMAN-ONLY**
  - Current testimonials are on the site. More English testimonials strengthen international positioning.

- [ ] **3.5** Choose testimonials for detailed case studies — **COOPERATIVE**
  - User selects which testimonials to expand. Claude writes the case study drafts.

- [ ] **3.6** Build case study pages — **AUTONOMOUS**
  - Depends on: 3.5
  - Create individual case study pages matching site design. Link from main page.

## Phase 4: Content Engine Integration

- [ ] **4.1** Connect Knifehead content pipeline to website — **COOPERATIVE**
  - Project Knifehead (multi-platform content engine) drives traffic to emotionmentoring.com
  - Ensure website CTAs, landing page, and funnel are aligned with content topics
  - Depends on: Knifehead implementation

- [ ] **4.2** Add blog/articles section — **COOPERATIVE**
  - Evaluate whether to add SEO content pages directly on the site
  - Could be simple static HTML pages following the same design system

## Phase 5: Email & Workspace

- [ ] **5.1** Set up Google Workspace for emotionmentoring.com — **COOPERATIVE**
  - Purchase Google Workspace plan. Configure domain for email (michal@emotionmentoring.com).
  - Add MX, SPF, DKIM, and DMARC DNS records on Spaceship.

- [ ] **5.2** Verify email deliverability — **COOPERATIVE**
  - Send test emails, confirm SPF/DKIM pass, check spam score.

## Phase 6: Ongoing Maintenance

- [ ] **6.1** Update sitemap.xml when new pages are added — **AUTONOMOUS**
- [ ] **6.2** Monitor Formspree for form submission issues — **HUMAN-ONLY**
- [ ] **6.3** Periodic SEO audit (quarterly) — **COOPERATIVE**
- [ ] **6.4** Update testimonials as new ones are collected — **COOPERATIVE**

---

## Priority Order

1. **Phase 1** — Content must be right before technical polish
2. **Phase 2** — Technical debt from FIXPLAN (accessibility first, then performance, then rest)
3. **Phase 3** — Media and social proof amplify conversions
4. **Phase 4** — Content engine ties everything together
5. **Phase 5** — Email and Google Workspace
6. **Phase 6** — Ongoing

## Blockers

| ID | Blocker | Blocks | Owner |
|----|---------|--------|-------|
| 1.4 | Real client count numbers | Proof strip update (1.5) | HUMAN-ONLY |
| 3.1 | Record intro video | Video embed (3.3) | HUMAN-ONLY |
