# MiniDesk — Arabic RTL offline task list

Run from the repository root:

```bash
python3 -m http.server 8000
```

Open `http://localhost:8000/experiments/minidesk/`.

- Uses localStorage in your own browser only.
- No accounts, servers, telemetry, external libraries, frameworks, or real data.
- Run logic tests with `node --test experiments/minidesk/tests/*.test.mjs`.

**Agent challenge:** TASKS/03 asks Jules to implement usable and accessible task filters.

#TODO: Provide a data-free export of the local task list as JSON, initiated by the user, without network access.
