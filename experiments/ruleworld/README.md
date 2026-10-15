# RuleWorld — deterministic Game of Life experiment

Cellular automaton rules are Conway's B3/S23. By default, boundaries are **finite and non-wrapping**, but can be made toroidal (wrapping) using the `--wrap` option.

```bash
python3 experiments/ruleworld/ruleworld.py --pattern blinker --width 10 --height 10 --steps 2
python3 experiments/ruleworld/ruleworld.py --pattern glider --steps 4 --format json
python3 experiments/ruleworld/ruleworld.py --pattern blinker --width 10 --height 10 --steps 2 --wrap
```

Seed experiments: `blinker`, `block`, `glider`.

**Agent challenge:** TASKS/01 introduces wrapping boundaries without changing the default model.

#TODO: Add bounded repeating-state detection for short simulations, with a proof-by-test of period two for the blinker. This is a candidate for Jules Suggested Tasks, not part of the initial implementation.
