# TASK 02 — Autonomous implementation choices (Stage 2)

Enhance Data Detective to detect unusually large or small values in its synthetic numeric dataset without any third-party libraries.

Required output:
1. A clearly named statistical outlier method documented in the README.
2. An optional CLI flag enabling outlier reporting; existing default JSON output remains backward compatible.
3. Per-row flagged ids and the relevant threshold(s), with a deterministic test dataset.
4. Tests for ordinary data, an outlier, an empty valid dataset, and malformed numeric input.
5. A documented reason for choosing your method, including a limitation.
6. A single reviewable PR; no merges.

You may choose the algorithm and interface details. You may not add dependencies or internet access. Read `AGENTS.md` first.
