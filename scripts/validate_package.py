#!/usr/bin/env python3
"""Offline package validator for the impossible-idea Hermes skill."""
import sys, os, json, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
errors, warnings = [], []

def require(path, label):
    full = os.path.join(ROOT, path)
    if not os.path.isfile(full):
        errors.append(f"MISSING {label}: {path}")
        return None
    return full

skill = require("SKILL.md", "Skill entry")
if skill:
    txt = open(skill, encoding="utf-8").read()
    if "name: impossible-idea" not in txt:
        errors.append("SKILL.md: frontmatter name must be 'impossible-idea'")
    if "description:" not in txt:
        errors.append("SKILL.md: description missing")
    for phase in ["PHASE 1","PHASE 2","PHASE 3","PHASE 4","PHASE 5","PHASE 6"]:
        if phase not in txt:
            errors.append(f"SKILL.md: missing {phase}")
    for lvl in ["CONVENTIONAL","BORING","IMPOSSIBLE","WEIRD","ABSURD"]:
        if lvl not in txt:
            errors.append(f"SKILL.md: missing {lvl}")
    for mode in ["/deeper","/wilder","/safer","/kill","/lineage"]:
        if mode not in txt:
            errors.append(f"SKILL.md: missing {mode}")

for ref in ["mutation-operators.md","rejection-ladder.md","crossing-mechanics.md",
            "genius-candidate-framework.md","filter-scoring.md","worked-example.md"]:
    require(f"references/{ref}", f"Reference {ref}")
for tpl in ["assumption-map.md","idea-mutation-sheet.md","genius-candidate-card.md"]:
    require(f"templates/{tpl}", f"Template {tpl}")

ev = require("evals/evals.json", "Evals")
if ev:
    try:
        data = json.load(open(ev, encoding="utf-8"))
        if not isinstance(data.get("cases"), list) or len(data["cases"]) < 8:
            errors.append("evals/evals.json: need >=8 cases")
        for c in data.get("cases", []):
            if not all(k in c for k in ("id","prompt","rule")):
                errors.append(f"evals case missing keys: {c.get('id')}")
    except Exception as e:
        errors.append(f"evals/evals.json invalid JSON: {e}")

require("LICENSE","LICENSE")
require("SOURCE-NOTES.md","SOURCE-NOTES.md")
require("README.md","README.md")

print(f"VALIDATE: {os.path.basename(ROOT)}")
print(f"  errors={len(errors)} warnings={len(warnings)}")
for w in warnings: print(f"  WARN  {w}")
for e in errors: print(f"  ERROR {e}")
if errors:
    print("RESULT: FAIL"); sys.exit(1)
print("RESULT: PASS"); sys.exit(0)
