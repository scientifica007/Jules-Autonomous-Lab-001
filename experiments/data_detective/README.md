# Data Detective — local synthetic CSV analysis

Runs fully offline using Python's standard library. It accepts a simple CSV with columns `id,group,value` and computes descriptive statistics on valid finite numeric rows.

```bash
python3 experiments/data_detective/analyze.py experiments/data_detective/samples/events.csv
```

- Malformed or non-finite values cause a reported error and a non-zero exit code.
- Duplicate IDs cause a reported error and a non-zero exit code.
- Empty data is valid and returns `count: 0` with null statistics.

**Agent challenge:** TASKS/02 asks Jules to choose and justify an outlier-detection approach.

#TODO: Add an optional, human-readable terminal summary (separate from machine-readable JSON) without losing backwards compatibility.
