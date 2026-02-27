# Emotion Mentoring — Fix Plan

Updated: 2026-02-27

**Scope:** All three pages — `index.html`, `thankyou.html`, `foundation.html`

References use CSS selectors and element descriptions (not line numbers — they shift after every edit).

---

## Phase 1: Critical Fixes (Accessibility & Structure)

### 1.1 Wrap form inputs in a `<form>` element — `index.html`
- Target: `#formContent` div and its children inside `.form-wrap#bookForm`
- Add `<form>` tag with `id`, `action` (Formspree), `method="POST"`
- Move `handleSubmit` to `form.onsubmit` with `event.preventDefault()` — without this the page will reload and break the fetch-based submit
- Enables Enter-to-submit, browser autofill, and screen reader form detection

### 1.2 Add `<label>` elements to all form fields — `index.html`
- Target: `#fname`, `#femail`, `#ftime`, `#fvision`
- Add visually hidden labels (sr-only class) for: name, email, preferred time, vision
- Fixes WCAG Level A compliance (1.3.1, 4.1.2)

### 1.3 Add ARIA attributes to FAQ accordion — `index.html`
- Target: all `.faq-item` containers and their `.faq-q` buttons
- Add `aria-expanded="false"` and `aria-controls` to each `.faq-q` button (they already have `role="button"` implicitly as `<button>` elements)
- Update the `onclick` toggle to also flip `aria-expanded`

### 1.4 Add ARIA + keyboard support to exit-intent modal — `index.html`
- Target: `.exit-modal-overlay#exitModal` and `.exit-modal`
- Add `role="dialog"`, `aria-modal="true"`, `aria-labelledby` (pointing to `.modal-headline`)
- Add `keydown` listener for Escape to close
- Add focus trapping while modal is open
- Restore focus to previous element on close

### 1.5 Replace clickable `<div>` elements with proper `<a>` tags — `index.html`
- Target: `.proof-item.proof-link` div with `onclick` (navigates to `foundation.html`) and the `.mentor-shen-link` div with `onclick`
- Replace `<div onclick="window.location.href='...'">` with a proper `<a href="foundation.html">` wrapper
- Remove redundant inner `<a>` to avoid double navigation / event bubbling
- Do NOT use the ARIA workaround (`tabindex`, `role="link"`, keydown handler) — semantic `<a>` is simpler and correct

### 1.6 Replace inline event handlers with CSS — `foundation.html`
- Target: footer Facebook links with `onmouseover="this.style.color='var(--gold)'"` and `onmouseout="this.style.color='var(--muted)'"`
- Replace with CSS `:hover` rule (matches how `index.html` footer links already work)

### 1.7 Add `aria-hidden="true"` to decorative SVGs — all pages
- Target: diamond divider SVGs, decorative gradient overlays, separator elements
- Add `aria-hidden="true"` so screen readers skip them
- Add `aria-label` to meaningful SVG links (logo in nav/footer, social media icons)

### 1.8 Add `:focus-visible` styles — all pages
- Target: all interactive elements across all three pages (buttons, links, nav CTAs, form inputs, `.faq-q` buttons, `.upgrade-option` labels, `.nav-back`)
- Add visible focus indicators using gold outline to match the design system
- Use `:focus-visible` (not `:focus`) to avoid showing outlines on mouse clicks

---

## Phase 2: Performance

### 2.1 Extract base64 portrait image to external file — `index.html`
- Target: the `<img>` inside `.mentor-portrait` with the ~400 KB base64 `src`
- Decode the base64 string and save as `portrait.jpg`
- Replace inline src with `src="portrait.jpg" loading="lazy"`
- Reduces HTML from ~500 KB to ~100 KB
- **Risk:** breaks the single-file deployment model. Verify `portrait.jpg` is committed and the path resolves correctly on GitHub Pages before pushing

### 2.2 Investigate and extract base64 images — `foundation.html`
- File is 430 KB — likely contains base64-encoded images similar to `index.html`
- Extract any inline base64 images to external files
- This is the single biggest performance fix for this page

### 2.3 Deduplicate inline SVG logo — all pages
- The same verbose logo SVG (~2 KB of path data) is duplicated in nav and footer on every page — that's 6 copies across the site
- **Per-page fix:** define the logo once as `<svg style="display:none"><symbol id="logo-symbol">...</symbol></svg>` at top of `<body>`, replace both instances with `<use>`
- **Note:** `foundation.html` has a nav logo WITHOUT `xmlns` and a footer logo WITH `xmlns` — normalize before deduplicating
- **Risk:** `<use>` can have rendering issues in older Safari. Test on iOS Safari before committing

### 2.4 Add `preconnect` for `fonts.gstatic.com` — all pages
- Target: `<head>` on all three pages, after the existing `preconnect` for `fonts.googleapis.com`
- Add `<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>`
- Currently missing on all three pages

### 2.5 Remove Cloudflare email obfuscation — `index.html`
- Target: the `<a>` with `__cf_email__` span (in `.email-direct`) and the Cloudflare script tag (`/cdn-cgi/scripts/5c5dd728/...`)
- Cloudflare's email protection script 404s on GitHub Pages, leaving email displayed as `[email protected]`
- **Fix:** remove the `__cf_email__` span and Cloudflare script entirely. Replace with a plain `<a href="mailto:michal@emotionmentoring.com">michal@emotionmentoring.com</a>`
- JS-based obfuscation is unnecessary for a landing page
- `thankyou.html` and `foundation.html` already use plain `mailto:` links — no action needed there

---

## Phase 3: JavaScript Fixes

### 3.1 Fix silent false-success on form submission failure — `index.html`
- Target: `handleSubmit()` — both the `.then(!response.ok)` and `.catch` paths
- **Current bug:** if Formspree fails, the code opens a `mailto:` link then redirects to `thankyou.html` after 500ms — regardless of whether the mailto actually opened. If the user has no mail client, the form silently "succeeds" with nothing submitted
- **Fix:** show an inline error message with the email address as a manual fallback (e.g., "Something went wrong. Please email michal@emotionmentoring.com directly."). Only redirect to `thankyou.html` on actual Formspree success
- Also re-enable the submit button (`btn.disabled = false`, restore text) in the error path so the user can retry

### 3.2 Fix silent false-success on upgrade submission — `thankyou.html`
- Target: `handleUpgrade()` — same pattern as `index.html`
- **Same bug:** both `.then(!ok)` and `.catch` paths open `mailto:` then call `showConfirmation()` after 500ms regardless
- **Fix:** show an inline error message in the upgrade card. Only call `showConfirmation()` on actual Formspree success. Re-enable the upgrade button on failure

### 3.3 Add email format validation — `index.html`
- Target: the `if (!name || !email)` check in `handleSubmit()`
- Add `input.checkValidity()` on `#femail` (leverages the browser's built-in `type="email"` validation) or use a basic regex
- Show an inline error message for invalid email instead of `alert()`
- While at it, replace the `alert()` for missing fields with an inline message too — `alert()` is jarring on a premium landing page

### 3.4 Consolidate scroll-reveal fallback strategy — `index.html`
- Target: the IntersectionObserver, `checkRevealsinView` scroll handler, hashchange/click listeners, and the 2-second `setTimeout` force-reveal
- These four mechanisms all solve the same problem (making `.reveal` elements visible) but step on each other:
  - **IntersectionObserver** — primary mechanism, works well
  - **hashchange + anchor click listeners** — needed for jump-navigation edge case
  - **scroll listener** — "belt and suspenders" fallback, fires on every scroll (wasteful)
  - **2-second setTimeout** — force-reveals ALL remaining elements, making the other three pointless for anyone who waits 2 seconds
- **Fix:** keep the IntersectionObserver + hashchange/click handlers. Remove the scroll listener. Increase the force-reveal timeout to 8 seconds (or remove it entirely and trust the observer). This reduces scroll-event overhead while preserving the anchor-navigation fix
- **Risk:** test on slow-loading mobile connections to ensure reveals still trigger. If issues appear, throttle the scroll handler (e.g., 200ms) instead of removing it

---

## Phase 4: CSS & Layout Consistency

### 4.1 Normalize section h2 styles — `index.html`
- Target: `.pain h2` has `font-weight: 700` while other section h2s use `900`
- Normalize `.pain h2` to `font-weight: 900`
- Standardize `line-height` and `margin-bottom` across all section h2s

### 4.2 Normalize transition speeds — all pages
- User preference: 0.1s (0.3s rejected as too slow)
- **`index.html`:** ~40 CSS rules still using `0.3s` — change to `0.1s`
- **`thankyou.html`:** `.upgrade-card`, `.upgrade-confirm`, `.upgrade-option`, `.upgrade-btn` transitions at `0.3s` — change to `0.1s`
- **`foundation.html`:** `a`, `.nav-back`, `.info-block`, `.board-member`, `.statute-link` transitions at `0.3s`, plus inline `transition:0.3s` on footer links — change to `0.1s`. Also fix `.reveal` transition at `0.6s` if too slow
- Exception: `max-height` transition on FAQ answers (currently `0.4s ease`) — keep this slightly slower for smooth accordion animation

### 4.3 Fix mobile padding on missed sections — `index.html`
- Target: the `@media (max-width: 900px)` block
- Add `.quote-break` to the mobile padding override
- Move inline `style="padding:..."` on the "Designed For" and "How It Works" sections into proper classes and include them in the mobile override
- Hide `.mentor::after` on mobile (same as `.what::after`)

### 4.4 Add intermediate breakpoint (~600px) — `index.html`
- Add a second `@media` query at `max-width: 600px`
- Transition testimonial grid: 6-col → 2-col (at 900px) → 1-col (at 600px)
- Test navigation, hero text, and form layout at tablet widths

### 4.5 Remove `!important` overrides — `foundation.html`
- Target: `.bio-text-group:hover p`, `.hero p:hover`, `.cta-btn:hover` all use `!important` unnecessarily
- Increase specificity or reorder rules instead

### 4.6 Move inline styles to CSS classes — `foundation.html`
- Target: 19 instances of `style="..."` on body HTML elements
- Create proper CSS classes for these — reduces HTML bloat and makes the styles maintainable

---

## Phase 5: Cleanup (Dead Code & Minor Issues)

### 5.1 Remove dead CSS and HTML — `index.html`
- `.hero-line` CSS rule (`display: none`) + its empty `<div class="hero-line">` in the hero section
- `@keyframes fadeIn` — defined but never referenced by any `animation` property
- `.testi-featured` — CSS rules at 3 locations but no HTML element has this class
- `.form-sub`, `.spots-badge`, `.assessment-callout`, `.ac-icon` — CSS rules with no corresponding HTML

### 5.2 Remove dead CSS class reference — `foundation.html`
- `.muted-hover` class is used on an HTML element but has no CSS definition — remove the class attribute from the element

### 5.3 Fix duplicate CSS definitions — `index.html`, `thankyou.html`
- **`index.html`:** two separate `.hero-sub` blocks (one in hero styles, one later with hover effects) — merge into one
- **`thankyou.html`:** `.thankyou-section h1` defined twice (once with full styles, once with just transition) — merge into one

### 5.4 Fix spelling inconsistencies — `index.html`
- Author copy: "analyse" → "analyze" (in the "The Method" section — this is author voice, not a quote)
- Testimonial quotes: keep "realising" and "realisations" as-is — these are direct client quotes in British English

### 5.5 Normalize minor typography — `index.html`
- `.section-label` uses `0.7rem` vs `.proof-item .label` uses `0.72rem` — pick one (recommend `0.72rem` for both)
- Standardize card paragraph font sizes where they vary between `0.9rem` / `0.95rem` / `1rem` without visual intent

### 5.6 Merge or differentiate duplicate FAQ answers — `index.html`
- "How many sessions does it typically take to see results?" and "How quickly will I notice a difference?" have nearly identical answers ("Most clients notice something shifting from/within the first session...")
- Either merge into one question or rewrite the second answer to focus on a different angle (e.g., what the early shifts feel like vs. the full transformation timeline)

### 5.7 Add `<meta name="description">` — all pages
- **`index.html`:** compelling 150–160 character SEO description for the main landing page
- **`thankyou.html`:** simple description (e.g., "Your assessment has been confirmed")
- **`foundation.html`:** description for the Shen Foundation page
- Also add `<meta property="og:description">` and `<meta property="og:title">` for social sharing on all pages

---

## Phase 6: Load Time Optimization & Code Optimization

Goal: minimize time-to-first-paint and total page weight without changing visuals, behavior, or functionality. Apply to all three pages.

### 6.1 Audit and minify inline CSS — all pages
- Target: the entire `<style>` block on each page
- After Phase 5 removes dead CSS, minify the remaining CSS (collapse whitespace, shorten hex colors where possible, remove redundant units on `0` values)
- Keep it inline (no external stylesheet) — a single-file approach avoids an extra HTTP request, which is faster for a landing page this size

### 6.2 Minify inline JavaScript — all pages
- **`index.html`:** minify variable names in non-public functions, collapse whitespace. Do NOT minify the `SPOTS` constant or `handleSubmit` function name (referenced by HTML)
- **`thankyou.html`:** same approach — preserve `handleUpgrade`, `SPOTS`, and element IDs
- **`foundation.html`:** minify the IntersectionObserver script
- Keep scripts inline for the same single-request reason as CSS

### 6.3 Optimize SVG markup — all pages
- Target: all inline `<svg>` elements across all pages (logo, diamond dividers, FAQ arrows, Facebook icons)
- Strip unnecessary attributes (`xmlns` when inline, redundant `fill="none"` on filled paths)
- Round path coordinates to 1 decimal place where possible (the logo SVG path data is very verbose — ~2 KB per instance)
- **`index.html`:** deduplicate diamond divider SVGs (appear 4+ times) — define once as `<symbol>`, reuse with `<use>`
- **`foundation.html`:** deduplicate the Facebook icon SVG (appears twice with identical path data)

### 6.4 Optimize font loading — all pages
- Target: the Google Fonts `<link>` in `<head>` on each page
- Audit which font weights are actually used per page — currently loading Playfair Display (400, 700, 900, italic 400, 700) and Barlow (300, 400, 500, 600)
- Remove any weights not referenced in that page's CSS
- `&display=swap` already present — verify it's working
- Consider self-hosting the font files for faster delivery from GitHub Pages (eliminates DNS lookup + connection to Google). If self-hosting, all three pages benefit from shared browser cache

### 6.5 Optimize image delivery — `index.html`, `foundation.html`
- Target: the extracted `portrait.jpg` (from fix 2.1) and any extracted images from `foundation.html` (fix 2.2)
- Compress JPEGs with quality 80–85 (visually lossless on a dark background)
- Generate WebP versions and use `<picture>` with JPEG fallback
- Add explicit `width` and `height` attributes to prevent layout shift (CLS)
- Add a tiny inline base64 blur placeholder for perceived instant load

### 6.6 Reduce DOM complexity — `index.html`
- Target: redundant wrapper `<div>`s that exist only for spacing
- Replace spacer divs (e.g., `<div style="height:2rem;background:var(--black);">`) with CSS margin/padding on adjacent sections
- Consolidate nested single-child divs where the wrapper adds no styling

### 6.7 Add resource hints — all pages
- Target: `<head>` on each page
- Add `<link rel="dns-prefetch" href="https://formspree.io">` (form submission endpoint — relevant to `index.html` and `thankyou.html`)

### 6.8 Final size audit — all pages
- After all optimizations, measure and document per page:
  - Total HTML file size (targets: `index.html` under 80 KB, `thankyou.html` under 15 KB, `foundation.html` under 30 KB)
  - First Contentful Paint (Lighthouse)
  - Largest Contentful Paint
  - Total Blocking Time
- Compare before/after metrics to confirm no regressions

---

## Priority Order

1. **Phase 1** (Accessibility) — do first, biggest compliance impact
2. **Phase 2** (Performance) — high impact, especially base64 extraction
3. **Phase 3** (JS fixes) — functional bugs that affect real users
4. **Phase 4** (CSS consistency) — visual polish and transition normalization
5. **Phase 5** (Cleanup) — remove dead code before optimization
6. **Phase 6** (Load time & code optimization) — do last, after all other changes are stable

## Implementation Notes

- **Branch strategy:** create a `fix/landing-page` branch. Commit after each phase so individual phases can be reverted if needed.
- **Testing between phases:** after each phase, verify all three pages on desktop + mobile (especially iOS Safari) before moving to the next.
- **Line numbers are intentionally omitted.** Use selector/element descriptions to find targets — line numbers shift after every edit.
- **Order within phases:** when a fix applies to multiple pages, do `index.html` first (primary page, most complex), then apply the same pattern to `thankyou.html` and `foundation.html`.
