# TASK 01 — Manual bounded coding test (Stage 1)

Implement a toroidal (wrapping) boundary option in the RuleWorld cellular automaton, while preserving the current finite-boundary behavior as the default.

Acceptance criteria:
1. CLI adds `--wrap` (boolean), default OFF.
2. With wrap ON, neighboring cells across left/right and top/bottom edges interact correctly.
3. No additional dependencies; reproducible deterministic output for fixed inputs.
4. Include at least three tests: one for horizontal wrapping, one for vertical wrapping, and one proving default behavior did not change.
5. Update only `experiments/ruleworld/`, directly relevant tests, and documentation.
6. Run relevant tests and report actual results. Publish a small PR, without merging.

Do not change the laws of the cellular automaton (B3/S23). Read `AGENTS.md` first.
