# Knowledge Graph: Semantic Network of Metamonism

## Purpose
This directory is designed to contain **machine-readable mappings** of all relationships within the Metamonism framework. It serves as the central hub for semantic connections between:

*   Core axioms and definitions (`CORE/`)
*   Machine-readable article specifications (`ARTICLES/M/`)
*   Disciplinary models (`ONTODYNAMICS/`)

## Current Status
🚧 **Under Construction**
The graph files are currently placeholders. They will be automatically generated and updated as the `ARTICLES/M/` specifications are populated.

## Files
*   `global_relations.jsonld` - Primary graph in JSON-LD format (semantic web standard).
*   `cross_reference.csv` - Simplified table of relationships for easy editing and review.

## How It Will Work
1.  Each M-version of an article will declare its relationships (e.g., "uses Core Axiom X", "extends Model Y").
2.  A build process or script will aggregate these declarations to update the files in this directory.
3.  The resulting graph can be used for AI analysis, advanced search, and visual exploration of the framework's ontology.

---
*This README and the placeholder files will be replaced with automated tooling in a future version.*
