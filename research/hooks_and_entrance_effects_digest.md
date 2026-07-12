# Hooks & Entrance Effects Digest

> Research satellite (2026-07-11). Linked to: OPERATION CHAMPAGNE structure decision.

## MISSION 1 — Opening hooks for CEOs

### Real examples collected (verbatim)

**Executive coaching canon**
1. "How have I been complicit in creating the conditions I say I don't want?" — Jerry Colonna
2. "Better Humans Make Better Leaders." — Reboot.io hero
3. "Work does not have to destroy us. Work can be the way we achieve our fullest selves." — Reboot.io
4. "What got you here won't get you there." — Marshall Goldsmith
5. "The higher you go, the more your problems are behavioral." — Goldsmith
6. "Half the leaders I have met don't need to learn what to do. They need to learn what to stop." — Goldsmith
7. "Success without fulfillment is the ultimate failure." — Tony Robbins

**Premium executive-therapy positioning (CEREVITY — closest competitive genre)**
8. "Therapy for the Pressure That Built Your Career"
9. "When the Drive That Got You Here Starts to Cost You"
10. "The weight of decisions no one else in the room understands."
11. "High-functioning on the outside. Running on fumes underneath."
12. "Most therapy is built for the average week. Yours is not the average week."
13. "Sessions that fit between board meetings, not the other way around."
14. "What you say in session stays in session." / "No insurance paper trail."
15. "The same traits driving your success can also be sources of stress and anxiety." — Momentum Psychology
16. "Being at the top can be lonely, with few peers to confide in or share the load." — Momentum Psychology

**Success-without-fulfillment / loneliness**
17. "I've sat across from founders with Ferraris in the driveway and eyes that look empty." — Jake Smolarek
18. "The moment you arrive is often the moment you realise the summit was never designed to hold you." — Smolarek
19. "I have what I wanted… and it doesn't feel the way I thought it would." — Your Coach Meg
20. "You are surrounded by people all day… and yet somewhere in the middle of all of it, you realize you have nobody to actually talk to." — Forbes CEO-loneliness writing
21. "It's Lonely at the Top (But It Doesn't Have to Be)" — CEO Coaching International
22. Indra Nooyi on her private CEO circle: "…alleviate some of the loneliness without giving away any confidential information."

**Direct-response classics (structure studies)**
- "They Laughed When I Sat Down At the Piano — But When I Started to Play!" (Caples)
- "Do You Make These Mistakes in English?" (Sackheim — ran 40 years)
- "At 60 miles an hour the loudest noise in this new Rolls-Royce comes from the electric clock" (Ogilvy — THE costly-signal understatement)
- Schwartz awareness stages: this audience is **problem-aware but solution-skeptical, sophisticated market** → lead with identification and mechanism, never raw claims.

### What works on skeptical executives (consensus)
- **Recognition, not education** — they know the problem; the hook's job is to make them feel seen.
- **Specificity beats adjectives** — concrete nouns from their actual life ("the chair you sit in", "between board meetings").
- **Status-safety** — the reader must agree without admitting weakness. Winning frames: strength-that-now-costs, strategy-not-softness. Losing frames: broken, struggling, "get help".
- **Pattern interrupt via calm** — quiet declarative confidence is the interrupt; understatement reads premium.
- **Conclusions-first cadence** — one sentence, one verifiable truth.
- **The unanswerable question** — a question money and title cannot answer bypasses "I can handle this."

### Hook formulas (10)
1. **The Asymmetry** — "You've [mastered] everything except ___."
2. **Strength-Turned-Cost** — "The [drive] that built X is now [costing] Y."
3. **The Implicating Question** — short question only they can answer: "Who do you ___?"
4. **The Unnamed Observer** — forensic one-sentence description of their private reality (telepathy).
5. **The Split-Screen** — "X on the outside. Y underneath."
6. **The Exception Frame** — "Most X is built for Y. You are not Y."
7. **Costly-Signal Understatement** — one quiet verifiable fact standing alone; premium implied by restraint.
8. **The Arrival Paradox** — "The moment you arrived is the moment ___."
9. **Crowded-Calendar Solitude** — "Surrounded by ___. Alone with ___."
10. **Confidentiality Signal as Hook** — discretion mechanic stated as flat fact.

## MISSION 2 — One-time entrance effects

### Effect catalog (real examples)
- **Igloo Inc** (Awwwards SOTD): WebGL crystal-growth shader intro flowing into the site.
- **Zentry**: kinetic typography intro, clip-path mask transitions, GSAP text builds.
- **Lusion.co**: three.js particle environment morphing on entry.
- **"Timeless" by Chipsa**: portals/particles/light; shader precompilation + web-worker preloader so the intro never stutters.
- **Messika / Chekotin / Limnia** (luxury jewelry): dark-luxury GSAP reveals over hero.
- **Codrops Multi-Layer Page Reveal**: canonical curtain sweep, pure CSS.
- **Codrops Kinetic Typography transition**; plus classic classes: particle-to-logo convergence, ink/smoke shader dissolves, SVG stroke draw-on, light sweeps on metallic type, iris/clip-path expansion, film-grain veils.

### Technical patterns
- **Gating**: `localStorage` with versioned key (`introSeen_v1`) + optional timestamp expiry (replay after 30+ days). Check flag **synchronously in an inline script in <head>**, stamp class on <html> before first paint (deferred check = flash).
- **Replay button**: small control (footer) that clears the key and re-runs.
- **Skip**: any click/keypress/scroll fast-forwards the intro.
- **prefers-reduced-motion**: replace intro with 400ms fade (WCAG 2.3.3).
- **Performance — overlay pattern, never delay pattern**: page content renders fully under a fixed opaque overlay; hero (largest content element) paints immediately; overlay removed from DOM on completion. Hiding the hero until intro ends destroys load metrics.
- Animate only transform/opacity for DOM (compositor, 60fps). Canvas: rAF only, cap devicePixelRatio at 2, scale particle count with viewport (~400-700 on phone), destroy canvas after. WebGL veils: render at 0.5–0.75× resolution, noise hides upscaling.
- **CDN stack**: GSAP 3.13 now 100% free including SplitText/MorphSVG (jsDelivr). three.js as CDN ES module. Canvas 2D dependency-free.

### Shortlist — ranked by wow-per-performance-cost (dark luxury, champagne, mobile-first)
1. **Champagne-dust convergence (canvas 2D)** — particles drift, converge to trace the wordmark, light sweep, disperse, dissolve to hero. 60fps on mid-range phones. On-brand to the letter.
2. **Typographic build + metal light sweep (GSAP SplitText)** — headline assembles from blur per character; champagne gradient sweep; 1px gold rule draws in. Near-zero cost; quiet-luxury register; ideal reduced-motion adjacent.
3. **Silk curtain reveal (CSS/GSAP)** — near-black panels part from a champagne seam of light, revealing the live page. Guaranteed 60fps, ceremonial "unveiling" semantics.
4. **Smoke/ink shader dissolve (WebGL quad)** — black veil dissolves like ink in water, gold-tinted edges. Biggest cinema; needs fallback; more QA surface.
5. **Monogram draw-on + iris reveal (SVG)** — cheapest, but most common pattern; lowest surprise.

Phases 1–3 can be COMBINED sequentially (particles converge → text builds → sweep → curtains part) as one 4–5s sequence holding 60fps, since phases never run simultaneously.
