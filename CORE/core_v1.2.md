# CORE v1.2 — Metamonism Framework

## Overview

This directory contains the canonical specifications of the Metamonism ontological framework (version 1.2).

## Structure

- **axioms.yaml** — Foundational axioms (Indifference Prohibition Axiom)
- **ontology.yaml** — Categories (Monos/Logos) and principles
- **operators.yaml** — Formal operators (diff, fix)
- **definitions.yaml** — Glossary with references to formal specifications
- **core_v1.2.md** — This human-readable summary

## Key Concepts

### Axiom
**Indifference Prohibition Axiom**: Absolute identity (a state without distinctions) is ontologically impossible.

### Categories
- **Monos**: The ontological continuum of reality as continuous, processual differentiation
  - Continuous (non-discrete)
  - Process-oriented
  - diff operations fundamental
  - fix operations ontologically impossible

- **Logos**: The epistemological space of models, theories, and fixed representations
  - Discrete (allows fixed entities)
  - Model-oriented
  - fix operations permitted
  - Represents Monos, never identical to it

### Operators
- **diff**: Produces distinctions from continuous process; ontologically primitive
- **fix**: Stabilizes distinctions into discrete entities; epistemic operation

### Principles
1. **Identity Prohibition in Monos**: Monos cannot instantiate absolute identity
2. **Identity Admissibility in Logos**: Logos admits operational identity for modeling
3. **Isomorphism**: Monos and Logos are structurally isomorphic through diff/fix
4. **Epistemic Cycle**: Iterative refinement of knowledge through Monos→Logos interaction

## Dependencies

All elements derive from the foundational axiom:
```
axiom_ban_of_absolute_identity
    ↓
Monos (ontology) + Logos (epistemology)
    ↓
diff (Monos) + fix (Logos)
    ↓
Principles (isomorphism, epistemic cycle)
```

## Version History

- **v1.2** (2024-03-21): Synchronized all files to v1.2, corrected cross-references
- **v1.1** (2024-03-21): Initial comprehensive specifications
- **v1.0** (2024-03-21): Foundational axiom established

## For Developers & AI

All files use YAML format with explicit cross-references. Entry points:
1. `axioms.yaml` — Start here for foundational constraint
2. `operators.yaml` — For operational specifications
3. `ontology.yaml` — For categorical distinctions
4. `definitions.yaml` — For quick term lookup

## Status

**Canonical** — These specifications are immutable. Changes require major version increment and must preserve backward compatibility through explicit versioning.
