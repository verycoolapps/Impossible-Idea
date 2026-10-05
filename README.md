# IMPOSSIBLE-IDEA — Idea Mutation Engine

![License](https://img.shields.io/badge/license-MIT-blue)
![Version](https://img.shields.io/badge/version-1.0.0-brightgreen)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-orange)

> Every idea you've already had was hiding behind an assumption you never questioned. This skill breaks the assumption and keeps whatever was hiding behind it.

**Impossible-Idea** is a Hermes skill that turns a request for "ideas" into a deliberate **assumption-mutation process** — one that produces ideas a normal brainstorm would reject, then proves part of that rejection was wrong.

It is *not* an idea-list generator. Every idea it outputs must trace back to two things: **which assumption was broken** and **which mutation operator did the breaking**. If you can't answer those two questions, the idea doesn't belong.

---

## What this is

A six-phase engine that forces ideas out of the safe, already-thought-of space:

1. **Consensus Map** — dismantle the "truth everyone takes for granted" in your domain into 7 explicit assumptions.
2. **Rejection Ladder** — generate one idea per level across 5 escalating tiers, from `CONVENTIONAL` to `ABSURD`.
3. **Mutation Operators** — apply at least 5 of 12 named operators (`INVERT`, `DELETE`, `PAYER SWAP`, `TIME SHIFT`, …).
4. **Crossings** — pair the wild ideas so each pair yields a *new mechanism* that exists in neither parent.
5. **Genius Candidate** — pick one crossing and interrogate it with Hidden Logic, Steelman, Pre-mortem, and Smallest Test.
6. **Reality Filter** — score it on Weirdness, Plausibility, Testability, and Moat (this is the only place your real-world context enters).

The result is not a brainstorm. It's an assumption autopsy with receipts.

---

## How the engine works

```
Consensus Map ──► Rejection Ladder ──► Mutation Operators ──► Crossings ──► Genius Candidate ──► Reality Filter
   (7 assumptions)     (5 levels)          (12 operators)      (3 pairs)      (4 hard questions)       (4 scores)
```

A short, real shape of an output:

```
📍 CONSENSUS MAP (X = coffee shop)
Untouched assumptions: ③ who pays ④ who competes ② what's sold

🪜 REJECTION LADDER
CONVENTIONAL  → A "workstation" shop + monthly subscription.
BORING        → An AI barista that remembers your favorite flavor.
IMPOSSIBLE    → Guests PAY to brew their own coffee. [assumption:③; op:INVERT]
WEIRD         → The shop supplies grounds to a rival chain. [assumption:④; op:COMPETITOR-AS-CHANNEL]
ABSURD        → No menu: guests bring beans, the shop rents space+tools. [assumption:②+③; op:DELETE+OWNERSHIP FLIP]

👑 GENIUS CANDIDATE: "Guest-Consigned Coffee"
Mechanism   : Shop=rented space+incubator; guest=producer&consumer; rival=channel.
Hidden Logic: People pay for "coffee expert" status on socials; the home-roasting community is huge.
Smallest Test: A 1-day pop-up, 10 guests, measure willingness to pay $5 to brew.
Score       : Weird 4/5 · Plausible 3/5 · Testable 5/5 · Moat 2/5
```

---

## Features

- **12 named mutation operators** — a real toolbox, not "think harder."
- **5-level Rejection Ladder** — calibrated so wild ideas *sound wrong in the first 3 seconds*.
- **Crossings that must birth a new mechanism** — a merge that reads "A and B" fails.
- **4 hard questions per candidate** — Hidden Logic, Steelman, Pre-mortem, Smallest Test.
- **Reality Filter scoring** — Weirdness / Plausibility / Testability / Moat on a 1–5 scale.
- **5 advanced modes** — `/deeper`, `/wilder`, `/safer`, `/kill`, `/lineage`.
- **Hard rules & an internal quality gate** — the skill checks its own output before answering.
- **12 regression evals + an offline validator** — the engine's behavior is pinned down and testable.

---

## Installation

Copy the `impossible-idea` folder into your Hermes skills directory (e.g. `~/.hermes/skills/creative/`), then run the validator to confirm the package is intact:

```bash
python3 scripts/validate_package.py
```

A clean install prints `RESULT: PASS`.

---

## Advanced modes

| Mode | What it does |
|---|---|
| `/deeper` | Repeat Phase 4 with 3 rounds of crossings; each round's output becomes the next round's parent. |
| `/wilder` | Raise every level one step (`BORING` → `IMPOSSIBLE`, and so on). |
| `/safer` | Keep the mutation mechanism but lower execution risk. |
| `/kill` | Run only a brutal pre-mortem on one idea. |
| `/lineage` | Show the family tree: which idea was born from which assumption and operator. |

---

## Package structure

```
impossible-idea/
├── SKILL.md                          # router + 6 phases + output format + hard rules + advanced modes
├── README.md
├── SOURCE-NOTES.md                   # provenance
├── LICENSE                           # MIT
├── references/
│   ├── mutation-operators.md         # 12 operators + examples + guardrail
│   ├── rejection-ladder.md           # 5 levels + escalation + "wrong in 3 seconds" test
│   ├── crossing-mechanics.md         # how to make a crossing a new mechanism
│   ├── genius-candidate-framework.md # hidden logic / steelman / pre-mortem / smallest test
│   ├── filter-scoring.md             # Weirdness / Plausibility / Testability / Moat rubric
│   └── worked-example.md             # two full end-to-end runs (coffee shop + edtech)
├── templates/
│   ├── assumption-map.md
│   ├── idea-mutation-sheet.md
│   └── genius-candidate-card.md
├── evals/
│   └── evals.json                    # 12 regression cases
└── scripts/
    └── validate_package.py           # offline package validator
```

---

## License

[MIT](LICENSE) © 2026 Andra Soemitro and Hermes Agent contributors. See `SOURCE-NOTES.md` for provenance.
