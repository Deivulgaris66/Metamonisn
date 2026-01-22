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
git clone https://github.com/Deivulgaris66/Metamonism.git
cd Metamonism
git checkout -b feature/your-contribution-name
```

### Step 2: Make Your Changes
Follow the guidelines for your contribution type (see below).

### Step 3: Validate Your Contribution
- **For YAML files**: Ensure valid YAML syntax
- **For ONTODYNAMICS**: Check derivation from CORE
- **For M-versions**: Verify semantic equivalence with H-version

### Step 4: Submit Pull Request
- Provide clear description of changes
- Reference related issues (if any)
- Explain how contribution maintains ontological consistency

### Step 5: Review Process
- Maintainers will review for:
  - Consistency with CORE principles
  - Proper derivation from КМИ
  - Technical correctness
  - Documentation quality

---

## 📋 Guidelines by Contribution Type

### For ONTODYNAMICS Extensions

#### File Structure
```yaml
# ONTODYNAMICS/[DISCIPLINE]/[topic].yaml
# Version: 1.0
# Purpose: [Brief description]
# Derived from: CORE v1.3

metadata:
  version: "1.0"
  discipline: "[Physics/Biology/Chemistry/etc]"
  derived_from: "CORE/axioms.yaml#axiom_ban_of_absolute_identity"
  falsifiable: true

model:
  id: "[unique_id]"
  name: "[Model name]"
  
  derivation_from_CMI: |
    Explain how this model derives from:
    1. Prohibition (Конфликт)
    2. Momentum (Момент-Импульс)
    3. Force/Dissipation
  
  core_operators:
    - operator: "diff"
      manifestation: "[How diff appears in this domain]"
    
    - operator: "diss"
      manifestation: "[How dissipation appears in this domain]"
    
    - operator: "fix"
      manifestation: "[How fixation works in Logos models]"
  
  predictions:
    - prediction: "[Falsifiable prediction 1]"
      testable: true
      
    - prediction: "[Falsifiable prediction 2]"
      testable: true
  
  references:
    - "CORE/ontology.yaml#principle_CMI_structure"
    - "CORE/operators.yaml#[relevant_operator]"
```

#### Checklist
- [ ] Model derives explicitly from КМИ structure
- [ ] Uses correct operator terminology (diff, diss, fix)
- [ ] Distinguishes Monos (ontology) from Logos (models)
- [ ] Includes falsifiable predictions
- [ ] References CORE principles
- [ ] Valid YAML syntax

---

### For ARTICLES (Dual-Channel)

#### H-Version (Human-Readable)
**Location**: `ARTICLES/H/[number]_[title]/`

**Structure**:
```
ARTICLES/H/01_Foundation/
├── README.md           # Article text with narrative flow
└── meta.yaml          # Metadata (DOI, authors, date)
```

**Requirements**:
- Academic writing style
- Clear narrative structure
- Abstract + Introduction + Sections + Conclusion
- References to CORE principles in prose
- Bibliography (if applicable)

#### M-Version (Machine-Readable)
**Location**: `ARTICLES/M/[number]_[title]/`

**Structure**:
```
ARTICLES/M/01_Foundation/
├── README.md           # Structured summary
├── specification.yaml  # Core claims, arguments, links
└── references.yaml     # Explicit links to CORE & ONTODYNAMICS
```

**specification.yaml Template**:
```yaml
# ARTICLES/M/[number]_[title]/specification.yaml
# Version: 1.0

metadata:
  article_id: "[unique_id]"
  title: "[Article title]"
  version: "1.0"
  date: "YYYY-MM-DD"
  h_version_link: "ARTICLES/H/[number]_[title]/README.md"
  
  core_version: "1.3"
  depends_on:
    - "CORE/axioms.yaml#axiom_ban_of_absolute_identity"

claims:
  - id: "claim_1"
    statement: "[Main claim]"
    derived_from: "[CORE reference]"
    evidence_type: "[logical/empirical/both]"
  
  - id: "claim_2"
    statement: "[Secondary claim]"
    derived_from: "[CORE reference]"

arguments:
  - id: "argument_1"
    structure: "[deductive/inductive/abductive]"
    premises:
      - "[Premise 1]"
      - "[Premise 2]"
    conclusion: "[Conclusion]"
    supports_claim: "claim_1"

ontological_commitments:
  - "Monos is non-symbolic"
  - "Motion is ontologically necessary"
  - "Dissipation is enforced"

key_terms:
  - term: "[Term]"
    definition: "[Definition]"
    reference: "CORE/definitions.yaml#[term]"
```

#### Checklist (Both Versions)
- [ ] H and M versions are semantically equivalent
- [ ] All CORE references are explicit (M-version)
- [ ] Claims are clearly stated
- [ ] Ontological commitments are declared
- [ ] Metadata includes version and dependencies

---

### For Documentation & Examples

**Examples of valuable contributions**:
- Tutorial: "Understanding the КМИ Structure"
- Example: "Applying Metamonism to Quantum Decoherence"
- FAQ: "Common Questions about Monos vs Logos"
- Diagram: "Visual representation of CORE operators"

**Location**: `docs/` (to be created)

**Requirements**:
- Clear, accessible language
- Accurate representation of CORE principles
- Helpful for newcomers

---

## ⚠️ Common Mistakes to Avoid

### 1. Treating Monos as Symbolic
**Incorrect**:
```yaml
# ❌ WRONG
monos_equation: "M = f(x, y, z)"
```

**Why**: Monos is non-symbolic. Equations are Logos constructs.

**Correct**:
```yaml
# ✅ CORRECT
logos_model_of_monos:
  equation: "M = f(x, y, z)"
  note: "This equation (Logos) represents aspects of Monos, not Monos itself"
```

---

### 2. Confusing Motion and Stasis Defaults
**Incorrect**:
```yaml
# ❌ WRONG
explanation: "Motion requires a cause (force applied)"
```

**Why**: In Metamonism, motion is the default (prohibition enforces it).

**Correct**:
```yaml
# ✅ CORRECT
explanation: "Stasis requires explanation (fix operation in Logos). Motion is ontologically necessary."
```

---

### 3. Ignoring Dissipation
**Incorrect**:
```yaml
# ❌ WRONG
closed_system: "Energy is perfectly conserved; no losses"
```

**Why**: Dissipation is ontologically necessary in Monos.

**Correct**:
```yaml
# ✅ CORRECT
idealized_model:
  note: "In Logos, we can model 'closed systems' where dissipation is negligible"
  reality: "In Monos, all systems dissipate (ΔS > 0 always)"
```

---

### 4. Not Deriving from КМИ
**Incorrect**:
```yaml
# ❌ WRONG
new_principle: "Entities have intrinsic properties"
derived_from: "[unstated]"
```

**Why**: All principles must trace back to the КМИ axiom.

**Correct**:
```yaml
# ✅ CORRECT
new_principle: "Properties emerge from differential fixation"
derived_from: "CORE/operators.yaml#fix"
explanation: |
  'Intrinsic properties' are Logos constructs (fix operations).
  In Monos, only processes and distinctions exist (diff).
```

---

## 🧪 Validation

### Self-Check Questions

Before submitting, ask yourself:

1. **Derivation**: Does my contribution trace back to the КМИ axiom?
2. **Consistency**: Does it conflict with any CORE principles?
3. **Clarity**: Are Monos/Logos distinctions clear?
4. **Falsifiability**: (For ONTODYNAMICS) Are there testable predictions?
5. **References**: Are all CORE references explicit?

### Automated Checks

When available, the repository will run automated validation:
- YAML syntax checking
- Cross-reference validation (all `derived_from` links resolve)
- Terminology consistency (use of diff/diss/fix)

---

## 📖 Resources for Contributors

### Essential Reading
1. **[CORE v1.3 Specification](CORE/core_v1.3.md)** — Understand the foundation
2. **[CORE/axioms.yaml](CORE/axioms.yaml)** — The КМИ axiom in detail
3. **[CORE/operators.yaml](CORE/operators.yaml)** — How diff, diss, fix work
4. **[CORE/validation.yaml](CORE/validation.yaml)** — Common errors to avoid

### Templates
- [ONTODYNAMICS model template](#for-ontodynamics-extensions)
- [M-version article template](#m-version-machine-readable)

### Examples
*Coming soon: example contributions for each type*

---

## 🤝 Community Guidelines

### Code of Conduct
- Be respectful and constructive
- Focus on ideas, not individuals
- Acknowledge that Metamonism is a work in progress
- Philosophical disagreements are welcome; personal attacks are not

### Discussion Channels
- **GitHub Issues**: Technical questions, bug reports
- **GitHub Discussions**: Philosophical questions, interpretation debates
- **Pull Requests**: Specific contributions with code/text

---

## 🎓 Levels of Contribution

### 🟢 Beginner-Friendly
- Documentation improvements
- Typo fixes
- Example contributions
- FAQ additions

### 🟡 Intermediate
- ONTODYNAMICS extensions in familiar domains
- M-versions of existing H-articles
- Visualization/diagrams

### 🔴 Advanced
- New ONTODYNAMICS in unfamiliar domains
- CORE refinement proposals (requires deep understanding)
- Cross-disciplinary isomorphisms

---

## 📊 Contribution Recognition

All contributors will be:
- Listed in CONTRIBUTORS.md (to be created)
- Credited in relevant files (metadata sections)
- Acknowledged in academic publications (where applicable)

---

## ❓ Questions?

- **Technical issues**: Open a GitHub Issue
- **Conceptual questions**: Start a GitHub Discussion
- **Private inquiries**: Contact maintainers (see README)

---

## 📜 Licensing

By contributing, you agree that your contributions will be licensed under the same [CC BY 4.0](LICENSE) license as the project.

You retain copyright but grant broad usage rights consistent with open science principles.

---

## 🚀 Getting Started

Ready to contribute?

1. **Read CORE v1.3**: Understand the foundation
2. **Pick a contribution type**: See above
3. **Fork the repo**: Start coding/writing
4. **Validate**: Use checklists
5. **Submit PR**: We'll review together

**Thank you for helping build a unified ontological foundation for science!**

---

<p align="center">
  <strong>Metamonism Contributors Guide</strong><br>
  Questions? Open an issue or discussion on GitHub
</p>
