# Source Notes & Provenance

- **Origin:** Original specification authored by Andra Soemitro, supplied as a prompt on 2026-10-05. No external repository or third-party code was copied.
- **Skill name / class:** `impossible-idea` — an "Idea Mutation Engine" (idea generator through deliberate assumption-breaking and mutation operators).
- **License:** MIT (package license below). The concept, prose, frameworks (assumption map, rejection ladder, 12 mutation operators, crossing mechanics, genius candidate, filter scoring) are original authoring by the requester.

## What this package adds

The requester supplied the core `SKILL.md` (identity, phases 1–6, output format, hard rules, extended modes, internal quality test). This package preserves that content faithfully (translated to English) and adds, as original supporting material:

- `references/` — six deep-dive guides that operationalize the engine (one file per major sub-system), each with worked examples and guardrails.
- `templates/` — three reusable working sheets.
- `evals/evals.json` — twelve regression cases encoding the engine's hard rules and anti-patterns.
- `scripts/validate_package.py` — a deterministic offline package validator.
- `README.md`, `SOURCE-NOTES.md`, `LICENSE`.

The worked examples in `references/worked-example.md` (coffee shop and edtech domains) are illustrative and original; any company/product names are fictional unless explicitly stated. No third-party assets, trademarks, or proprietary data are redistributed.
