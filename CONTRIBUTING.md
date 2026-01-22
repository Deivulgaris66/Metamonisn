# Contributing to Metamonism

Thank you for your interest in contributing to the Metamonism framework! This document provides guidelines for contributing to the project.

---

## 🎯 Overview

Metamonism is an ontological framework with strict architectural principles. All contributions must maintain:

1. **Ontological consistency** with CORE v1.3
2. **Derivation from the КМИ axiom** (Indifference Prohibition)
3. **Clear separation** between Monos (ontology) and Logos (epistemology)
4. **Falsifiability** for all scientific extensions

---

## 📂 Types of Contributions

### 1. CORE Refinements ⚠️ (High Bar)
- **What**: Proposals to modify foundational axioms, principles, or operators
- **Barrier**: Very high—CORE is intentionally minimal and immutable
- **Process**: Open an Issue first with strong justification
- **Requirements**:
  - Demonstrate necessity (why current CORE is insufficient)
  - Show backward compatibility or explicit versioning strategy
  - Prove ontological consistency

**Note**: CORE changes require major version increment (v2.0, v3.0, etc.)

---

### 2. ONTODYNAMICS Extensions ✅ (Encouraged)
- **What**: New disciplinary models derived from CORE
- **Barrier**: Medium—must follow derivation rules
- **Process**: Fork → Create → Pull Request
- **Requirements**:
  - Explicit derivation from КМИ structure
  - Falsifiable predictions
  - Machine-readable format (YAML/JSON-LD)
  - References to CORE principles

#### Examples:
- `ONTODYNAMICS/PHYSICS/thermodynamics.yaml`
- `ONTODYNAMICS/BIOLOGY/evolution.yaml`
- `ONTODYNAMICS/CHEMISTRY/bonding.yaml`

---

### 3. ARTICLES (H & M versions) ✅ (Encouraged)
- **What**: New articles or M-versions of existing H-articles
- **Barrier**: Medium—must maintain dual-channel architecture
- **Process**: Fork → Create → Pull Request
- **Requirements**:
  - Both H (human) and M (machine) versions
  - Semantic equivalence between versions
  - Explicit links to CORE and ONTODYNAMICS

---

### 4. Documentation & Examples ✅ (Low Bar)
- **What**: Tutorials, examples, clarifications
- **Barrier**: Low—improves accessibility
- **Process**: Fork → Create → Pull Request

---

## 🔧 Contribution Workflow

### Step 1: Fork the Repository
```bash
