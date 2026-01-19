# Contributing to the Metamonism Framework

Thank you for your interest in contributing to the Metamonism project. This document outlines the philosophy, processes, and guidelines for collaboration. Following them helps maintain the project's coherence and quality.

## Philosophy & Project Structure

Metamonism is a **two-channel project**:
1.  **Human-Readable Channel (H):** Traditional academic articles (PDFs) published on platforms like Zenodo/arXiv with immutable DOIs.
2.  **Machine-Readable Channel (M):** This repository. It contains structured specifications (YAML), ontological core definitions, and metadata that **link to** and **formally elaborate on** the H-channel.

All contributions to this repository (M-channel) should respect this duality and the established [repository structure](../README.md#-architecture).

## Types of Contributions

We welcome various types of contributions:

### 1. Improving Core Definitions & Specifications
*   **Clarifying `TODO:` statements** in `CORE/` YAML files (e.g., proposing a more precise formulation for an axiom in `axioms.yaml`).
*   **Extending definitions** in `CORE/definitions.yaml` or `CORE/operators.yaml` with formal notation or clarifying notes.
*   **Improving the structure** of YAML files for better machine readability.

### 2. Developing Models in Ontodynamics
*   **Proposing new models** within existing sections (e.g., a new `electromagnetism.yaml` in `ONTODYNAMICS/PHYSICS/`).
*   **Refining existing models** (e.g., enhancing the `redshift.yaml` model with more detailed predictions).
*   **Suggesting new sections** (e.g., a `BIOLOGY/` directory) with a clear link to the core axioms.

### 3. Enhancing Articles Bridge & Knowledge Graph
*   **Updating `ARTICLES/` metadata** when a new H-version article is published (adding DOI, links).
*   **Proposing new relationship types** or improving the `KNOWLEDGE_GRAPH/` to better capture connections between concepts.
*   **Creating or improving documentation** like this file or section-specific `README.md` files.

### 4. Reporting Issues & Discussing
*   **Opening a [GitHub Issue](https://github.com/Deivulgaris66/Metamonisn/issues)** to:
    *   Ask questions about concepts.
    *   Report inconsistencies between files.
    *   Propose significant changes or new directions.
    *   Discuss H-version articles (using the Issue linked from the article's `meta.yaml`).

## Workflow: How to Contribute

1.  **Fork & Clone** the repository to your own account.
2.  **Create a Branch** for your contribution (e.g., `fix/core-axiom-wording`, `feat/add-cognitive-model`).
3.  **Make Your Changes**. Adhere to the existing style and structure.
    *   For YAML files: maintain the key structure and use comments (`#`) for explanations.
    *   For Markdown files: use clear headers and links.
4.  **Test Locally** (if applicable) and ensure no syntax errors are introduced.
5.  **Commit Your Changes** with a clear, descriptive commit message (e.g., "docs: clarify diff operator in definitions.yaml").
6.  **Push to Your Fork** and open a **Pull Request (PR)** to the `main` branch of this repository.
7.  **Describe Your PR** thoroughly. Explain the *what*, *why*, and links to any related Issues.
8.  **Participate in the PR Review**. Be open to feedback and ready to refine your contribution.

## Versioning & Breaking Changes

*   **The `CORE/` directory** is versioned as a whole (v1.0, v1.1). Changes here should be rare, well-justified, and discussed in an Issue first, as they may require updates across `ONTODYNAMICS/`.
*   **Files within `ONTODYNAMICS/`** can be versioned independently (e.g., `v0.1`, `v0.2`). Their `manifest.yaml` should state which `CORE` version they depend on.
*   Clearly mark **breaking changes** (those that invalidate existing links or interpretations) in your PR description.

## Pull Request & Issue Templates

### For a Good Pull Request
*   **Scope:** Addresses one clear topic or fix.
*   **Description:** Links to the relevant Issue (if one exists).
*   **Consistency:** Follows the project's file structure and formatting.
*   **`TODO:` Handling:** If you complete a `TODO:`, remove the marker and replace it with definitive content.

### For a Good Issue
*   **Title:** Clear and descriptive (e.g., "Ambiguity in the definition of 'Logos' in CORE/definitions.yaml").
*   **Content:** References the specific file and line if possible. States the problem and, if possible, suggests a direction for a solution.
*   **Type:** Uses labels appropriately (e.g., `question`, `bug`, `enhancement`, `proposal`).

## License & Attribution

By contributing to this repository, you agree that your contributions will be licensed under the same **Creative Commons Attribution 4.0 International (CC BY 4.0)** license that covers the project. You retain copyright of your original work.

For major contributions (e.g., a new model section), you may be added to the list of contributors in the project's documentation upon request.

## Getting Help

If you are unsure about anything, the best way to start is by **opening a [GitHub Issue](https://github.com/Deivulgaris66/Metamonisn/issues)** with your question. The discussion there will benefit future contributors as well.

---
*This contributing guide is itself open to improvement. Suggestions for its clarity or completeness are welcome via Issues or Pull Requests.*
