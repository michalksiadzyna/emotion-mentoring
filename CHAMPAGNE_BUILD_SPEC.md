# OPERATION CHAMPAGNE — BUILD SPEC (2026-07-11)

Binding law for all three preview builds. Every rule here is mandatory unless marked optional. Each agent builds EXACTLY ONE file and touches nothing else.

## Files
- Agent 1 → `preview_v1_editorial.html`
- Agent 2 → `preview_v2_minimal.html`
- Agent 3 → `preview_v3_cinema.html`

## THE ORDER RULE (MAIN RULE — enforced)
Section order, no deviation:
1. **HOOK** (hero) — the hook line (CEOs + loneliness named in the first sentence), sub-line "Emotion Mentoring for CEOs", the CTA. The FIRST SCREEN must answer: what is this, who is it for, what do I do. Two screens is the absolute maximum for delivering all core answers.
2. **RECOGNITION** — who this is for, in what situations: carrying a divorce or private crisis while running the company · decision load that never stops · loneliness at the top (featured) · success that stopped feeling like anything · the moment everything breaks at once. Then two short lists side by side: **This is for** — CEOs, founders, leaders who want to develop the capacity of their mind. **This is not for** — people seeking therapy, standard psychological help, or psychiatric help.
3. **THE WORK** — what the method does and why it delivers for these people. Product canon in plain words: life leaves errors, damage, and unhandled emotional blockages in the mind; the work repairs them; the mind adapts again, runs better, carries more with less strain; decisions improve, relationships improve, fear shrinks. Dual engine: name the trajectory avoided (a mind that stops keeping up with the load) and the water gained (better decisions, lighter mind, work and life feeding each other).
4. **PROOF** — testimonials (see bank below). Attributed, never anonymous.
5. **TERMS** — plain: **12 spots.** Two private sessions a month plus direct access between them. **Engagements begin at €3,000/month** (price SHOWN, plainly). Crisis line: when everything breaks at once, Michal is ready within hours and works with you until it is solved. The e-book as the ONE side door (subordinate link, never competing with the CTA): "The Secret Book of Emotions" → the-secret-book-of-emotions-shen.html.
6. **THE CONVERSATION** — the ask. One large premium rectangle, a single centered email field, a send button. Headline: "Book your private 20–30 minute conversation." Anxiety dissolvers in the same breath, small text: "Confidential. 20–30 minutes. You get the details by email." Form action: POST to https://formspree.io/f/mvzblnyr (field name="email", plus hidden input identifying the preview version). The visitor's decision must be pure yes/no — nothing else to configure.

## Copy laws
- Voice: "We" register for body copy where a subject is needed; the hook and stats may speak about CEOs in third person. NEVER mix We and you in the same passage.
- PLAIN LANGUAGE: readable for non-native English speakers. Short sentences. No jargon, no ornate register.
- ~600–900 visible words total. Compact. Everything below screen 2 is tight evidence, never essay.
- One CTA phrase, repeated verbatim at: hero, after PROOF, and the form button area. Default phrase: **"Book your private conversation"** (pending user ruling between 3 finalists — build with the default).
- A short attributed quote sits NEXT TO each CTA instance (proof beside the ask).
- Statistics — exact wording only, shown with attribution:
  - "Half of CEOs report loneliness in the role; of those, 61% believe it hinders their performance." — RHR International, via Harvard Business Review
  - "Nearly two-thirds of CEOs receive no coaching or leadership advice from outside." — Stanford GSB
  - Optional: "CEOs average 62.5-hour workweeks." — HBR; "85% of business leaders suffered decision distress in the past year." — Oracle
- BANNED: "premium", "luxury", "elite", "world-class", any self-superlative, any ranking language, invented numbers, timeframes/promises of speed, the words "assessment" or "free", "coaching" as the service name (it is mentoring), "private" as adjective for the entry call ("confidential" register instead — but the user's exact form headline "Book your private 20–30 minute conversation" is ruled and stands).
- Never define by negation ("this is not therapy" is banned framing — EXCEPT the ruled "This is not for" list, which is an explicit user order).
- Practitioner: Michal Ksiadzyna (spelling exact; operates as "Shen"). Method: The Shen Method. American English.

## Testimonial bank (verbatim quotes; use the sentences marked ★ as the short pull-quotes)
- Krystyna Mendonca — entrepreneur: ★"After four months, the loneliness that had made my life a nightmare for years simply disappeared." Also usable: "After less than a year I finally felt real freedom and joy."
- Arkadiusz Czajkowski — CEO: ★"He doesn't hide behind catchy sales copy. He simply delivers results." Also: "Michał is a highly skilled professional who built my trust session by session — and I'm not someone easily convinced."
- Dominika Lenard: ★"Within a single session I healed a pattern I had been repeating for many years."
- Beata Brzychczyk: ★"Since that work, I have never felt lonely."
- Paulina Szuta: "I know no one who works at this level with what is still in us to be healed."
Role labels: ONLY Czajkowski (CEO) and Mendonca (entrepreneur) have confirmed labels. All others: name only, no invented roles.

## Design system (shared)
- Ground: #0a0a0c. Text: #b6b1a6 (dim #76715f). Champagne metal: base #c9a96e, highlight #f2e8d4, light #d9c491, deep #85714a.
- Metal gradient for headline/accent metal: `linear-gradient(100deg,#6b5a35 0%,#a68c52 16%,#d9c391 30%,#fdf6e3 44%,#f4ead0 48%,#fdf6e3 52%,#cdb377 66%,#7a6538 84%,#a89058 100%)` with background-clip:text where used.
- Fonts (Google Fonts): Cormorant Garamond (small caps, headings) + Jost (body). Corner ticks on key framed elements (business-card blueprint).
- Comprehensive hover culture: every interactive element has a deliberate hover (champagne accent shifts, subtle lifts). Transition 0.1s baseline.
- Portrait available: `portrait.webp` / `portrait.jpg` (grayscale(15%) contrast(1.05), color on hover — optional per version).
- Sticky mobile CTA bar (same CTA phrase). Fully responsive, mobile-first quality. NO build tools; GSAP via CDN allowed (https://cdn.jsdelivr.net/npm/gsap@3.13/dist/gsap.min.js, ScrollTrigger/SplitText same path). All CSS/JS inline in the single file.
- Award-level craft. Flat sections, small type, skeleton emptiness = failure. Minimal means refined density of craft.

## Entrance effect (shared law, per-version flavor)
- Ultra-fast: target ~0.6s, NEVER exceed 1.5s total.
- OVERLAY pattern: the page paints fully underneath; the effect is a fixed overlay removed from DOM at end. Never delay content or hero interactivity.
- Runs ONCE: inline script in <head> checks localStorage key `introSeen_v1` synchronously and stamps a class on <html> before first paint; sets the key after playing.
- Any click/keypress/scroll skips it instantly. `prefers-reduced-motion` → simple 300ms fade instead.
- A tiny "replay" control in the footer (clears key, replays in place or reloads).

## Version characters (DISTINCT — this is where you diverge)
- **V1 EDITORIAL (preview_v1_editorial.html)** — "The Ledger". Stat-monument hero: a huge champagne numeral treatment of the loneliness statistic (e.g. "1 / 2") beside the hook. Asymmetric editorial grid, hairline rules, magazine-grade typography, generous but structured. Hook: "Half of all CEOs are lonely in the role. Almost none say it out loud." Entrance: champagne light sweep across the wordmark, then a fast curtain part (~0.7s).
- **V2 MINIMAL (preview_v2_minimal.html)** — "The Vow". Radical centered subtraction: vast black, single column, few words, the email rectangle as the visual centerpiece of the whole site. Every element engraved-card quality. Hook: "CEOs have everyone's attention and no one to talk to." Entrance: a single champagne dust-flash that condenses into the wordmark (~0.5s).
- **V3 CINEMA (preview_v3_cinema.html)** — "The Descent". Scroll-driven reveals (GSAP ScrollTrigger), metallic gradient type, light that moves, sections that arrive like scenes. Still obeys the ORDER RULE and compactness — cinema in the transitions, not in extra sections. Hook: "Half of CEOs are lonely at the top. Two-thirds face it without any outside advice." Entrance: dark veil ink-dissolve with champagne edge light (~1.0–1.2s).

## Verification checklist (the orchestrator greps for these — make sure they exist)
- `introSeen_v1`, `prefers-reduced-motion`, `formspree.io/f/mvzblnyr`, `type="email"`
- "12 spots", "€3,000", "Book your private conversation", "Emotion Mentoring for CEOs"
- "Half of CEOs report loneliness in the role" (exact), "Stanford" attribution
- "This is for" / "This is not for" lists, "Ksiadzyna" (and zero occurrences of "Ksiądzyński")
- Sticky mobile CTA, replay control, corner ticks, Cormorant Garamond + Jost
- Section order in DOM: hook → recognition → work → proof → terms → conversation
