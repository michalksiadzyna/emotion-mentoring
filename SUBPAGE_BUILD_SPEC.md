# SUBPAGE PROPAGATION SPEC (2026-07-12)

Binding law for the three subpage rebuilds. The live `index.html` (V3 Cinema, champagne) is the SOURCE OF TRUTH — replicate its design system exactly, add nothing new. This is strict propagation, not creative work.

## Files
- Agent 1 → rewrite `foundation.html` (read the existing file first for content)
- Agent 2 → rewrite `the-secret-book-of-emotions-shen.html` (read existing first)
- Agent 3 → rewrite `thankyou.html` (read existing first)
Each agent touches EXACTLY its one file. Never touch index.html or another agent's file.

## Design system — copy from index.html VERBATIM
Read `C:/Users/micha/Projects/emotion-mentoring/index.html` and lift these blocks exactly:
- The `:root` palette variables, body base, grain overlay, `.metal` chrome-text class, corner-tick system (`.tick`/`.ticked`), `.kick` kicker, `.scene` scaffolding, scene `h2` treatment, `.rule` hairline, `.pill`/`.pill.solid` CTA styles, footer style, selection color, fonts link (Cormorant Garamond + Jost, same Google Fonts URL).
- Scroll-reveal: subpages use a LIGHT version — a simple IntersectionObserver adding `.visible` to `[data-rise]` elements (opacity 0 → 1, translateY 18px → 0, 400ms). Do NOT include GSAP, the entrance veil, the spine beam, or the intro gate on subpages. No `introSeen_v1` anywhere.
- Sticky mobile CTA bar (`#mcta`-style) mirroring index.
- Comprehensive hover culture at index's level (0.1s baseline transitions).

## Shared page skeleton
- Top bar as on index: left "Michal Ksiadzyna" · right "The Shen Method" — BOTH link to `/` (index).
- A small kicker + Cormorant small-caps h1 in the index h2 style.
- Compact single-column content, `.scene` padding rhythm, max-width ~720px for text.
- Footer exactly in index style (Michal Ksiadzyna · The Shen Method · Emotion Mentoring for CEOs · © 2026) with a "Back to the main page" link, no replay button.
- Full SEO head per page: title ("<Page> — Emotion Mentoring"), meta description, canonical (https://emotionmentoring.com/<file>), favicon.svg link, OG title/description/type/url, twitter card summary. NO noindex.
- Fully responsive, mobile-first quality. All CSS/JS inline. American English.

## Copy laws (identical to the main build)
- "We" voice where a subject is needed; plain language for non-native speakers; short sentences.
- The service is "the mentoring" — NEVER "the work", never "the method" as generic ("The Shen Method" as proper name is allowed).
- BANNED: "premium", "luxury", "elite", "world-class", self-superlatives, invented numbers/timeframes, "free", "assessment", "coaching" as the service name, "them" for people in Shen voice. Never define by negation.
- The conversation is "your private 30-minute conversation". Entry CTA phrase where relevant: "Book your private conversation" → link to `/#conversation`.
- Practitioner: Michal Ksiadzyna (NEVER "Ksiądzyński"). Surname check mandatory.
- Statistics: none needed on subpages; do not invent any.

## Per-page content mandates

### foundation.html (Agent 1)
- Preserve the existing page's factual content: the Shen Foundation's mission, board members (names/roles exactly as in the current file), statute link/document reference, contact if present. Read the current foundation.html and carry ALL facts over verbatim — names, spellings, legal references. Nothing invented, nothing dropped.
- Structure: hero (kicker "The Shen Foundation" + one-line h1 from existing mission language) → mission text (compact) → board (clean rows or cards with corner-tick accents) → statute/document link → quiet footer. One subordinate link back to the mentoring (index).

### the-secret-book-of-emotions-shen.html (Agent 2)
- Preserve the existing page's function: presenting The Secret Book of Emotions and delivering the PDF via the email gate. Read the current file; keep its Formspree endpoint for the book (xgopoelo — verify the exact endpoint in the file and reuse it), its download/delivery mechanics, and the book's factual description (20 secrets, 5 chapters — only claims already present in the current page or verifiable from it).
- Structure: hero (book title in metal Cormorant + one-line teaser from existing copy) → what the book is (2–3 short paragraphs max, reuse/condense existing copy under the copy laws) → email gate form styled EXACTLY like index's conversation panel (large refined rectangle, corner ticks, single centered email field, champagne pill button, fine-print line) → quiet footer. Subordinate link to the mentoring.
- If the current page has a cover image reference, keep it; do not invent new imagery.

### thankyou.html (Agent 3)
- Purpose: post-form confirmation. The OLD page contains upsell content ("VIP assessment", "12-month program", "free 45-minute assessment") that violates current rulings — DROP all of it. Do not carry over banned-word content.
- New content, complete: h1 confirmation ("Your request is in." register — plain, warm, We-voice-compatible), one line: the details arrive by email shortly; one line: Confidential. 30 minutes. A single subordinate link: The Secret Book of Emotions (the side door) — "While you wait" framing. Back-to-main link. That is ALL. ~60 visible words maximum.
- Head must include `<meta name="robots" content="noindex">` (thank-you pages are excluded from the sitemap and should stay unindexed).

## Verification checklist (orchestrator greps for these)
- Each file: 'Cormorant Garamond', 'Jost', the metal gradient string `linear-gradient(100deg,#6b5a35`, `favicon.svg`, `canonical`, `Ksiadzyna`, zero `Ksiądzyński`, zero `introSeen_v1`, zero GSAP/cdn references, `data-rise`, sticky CTA, `#0a0a0c` ground.
- foundation.html: board names present (diff vs old file), statute reference present.
- book page: correct Formspree book endpoint, `type="email"`.
- thankyou.html: `noindex` present, zero "assessment"/"free"/"VIP", under ~80 words.
- All: zero banned words, zero "the work"/"the method" as generic service name.
