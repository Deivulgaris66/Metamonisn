# Ontodynamics: The Unfolding of Worlds

## Purpose
The **Ontodynamics** directory is where the immutable principles of the [Core](../../CORE/) are applied to model specific domains of reality ("Worlds"). It contains the **machine-readable (M) specifications** for various scientific disciplines, re-interpreted through the Metamonism framework.

## Structure
Each subdirectory represents a distinct "World" or discipline. The current structure is minimal and designed for expansion:

*   **[PHYSICS/](./PHYSICS/)**: Models for physical phenomena.
    *   `manifest.yaml` – Overview and connections.
    *   `quantum_mechanics.yaml` – Interpretation of quantum states and measurement.
    *   `thermodynamics.yaml` – Interpretation of entropy and the arrow of time.
*   **[COSMOLOGY/](./COSMOLOGY/)**: Models for cosmological structure and evolution.
    *   `manifest.yaml` – Overview and connections.
    *   `redshift.yaml` – Alternative model for cosmological redshift.
    *   `large_scale.yaml` – Model for the formation of cosmic structure.
*   **[CHEMISTRY/](./CHEMISTRY/)**: Models for chemical phenomena.
    *   `manifest.yaml` – Overview and connections.
    *   `bonding.yaml` – Interpretation of chemical bonds.

## Guiding Principle
Every model in this directory must be **a logical derivation from the Core axioms** (primarily the Indifference Ban) and must use the core operators (`diff`, `fix`) as its foundational language. These are not new independent theories, but **specifications of how the core ontology manifests in a given domain**.

## Workflow & Versioning
1.  **Iterative Development**: Files here (`.yaml`) are versioned independently (e.g., `v0.1`, `v0.2`) and can be refined as the models develop.
2.  **Core Dependency**: Each `manifest.yaml` explicitly states its dependency on a version of the Core (e.g., `CORE/v1.0`). A change in the Core may necessitate updates here.
3.  **Inter-World Links**: The `relations` section in each `manifest.yaml` defines isomorphisms and dependencies between different disciplinary models, building a coherent cross-disciplinary network.

## How to Navigate
1.  Start with the `manifest.yaml` file in a section of interest to understand its scope and links.
2.  Explore the individual model files (`.yaml`) to see the specific application of the framework.
3.  To understand the foundational logic, always refer back to the [Core](../../CORE/) definitions and axioms.

## Future Expansion
This directory is designed to grow. New "Worlds" (e.g., `BIOLOGY/`, `COGNITIVE_SCIENCE/`, `SOCIOLOGY/`) can be added by creating a new subdirectory with the same basic structure: a `manifest.yaml` and relevant model files.
