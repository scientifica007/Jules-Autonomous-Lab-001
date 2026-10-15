# Jules Autonomous Lab 001

> **An isolated, safe evaluation sandbox for Google Jules** — three independent microprojects, no production secrets, no connections to existing projects.

## الغرض

هذا المستودع مخصص حصريًا لتجريب قدرات Jules على تنفيذ المهام، حل المشكلات، اكتشاف التحسينات، وإجراء صيانة مجدولة دون حضور المستخدم. لا يحتوي بيانات حقيقية أو أسرارًا أو تكاملات خارجية.

## Experiments / التجارب

| Project | Technology | Goal | Initial run |
|---|---|---|---|
| `experiments/ruleworld` | Python 3 standard library | Deterministic cellular automaton | `python3 experiments/ruleworld/ruleworld.py --pattern blinker --steps 2` |
| `experiments/data_detective` | Python 3 standard library | Synthetic CSV statistics | `python3 experiments/data_detective/analyze.py experiments/data_detective/samples/events.csv` |
| `experiments/minidesk` | HTML/CSS/JavaScript | Local-only task organizer | `python3 -m http.server 8000` then `http://localhost:8000/experiments/minidesk/` |

### Run tests / تشغيل الاختبارات

```bash
python3 -m unittest discover -s tests -p 'test_*.py' -v
node --test experiments/minidesk/tests/*.test.mjs
```

Requires Python 3.10+ and Node 20+ for JS tests; the web app needs only a modern browser.

## Start here / البدء

1. Read `SETUP_AR.md` for safe installation in a **new private GitHub repository**.
2. Connect only this repository to Jules. Do not authorize access to all GitHub repositories.
3. In Jules, run `TASKS/01-ruleworld-manual.md` as your first controlled task.
4. Review its diff, test evidence, and Pull Request. **Do not auto-merge**.
5. Enable scheduled work using `TASKS/04-scheduled-maintenance.md` only after the first task succeeds.
6. Track evaluation in `EVALUATION.md` and `evaluation/scorecard.csv`.

## Isolation rules

- No external services, deployments, tokens, credentials, production data or real personal information.
- Do not alter other repositories or request new integrations.
- Jules must modify only one experiment per task, except tests or docs directly relevant to that experiment.
- All changes arrive as proposed PRs, not auto-merged commits.
- All external dependencies are forbidden during this initial experiment.

## Success criteria for the pilot

A useful agent creates **small, tested, explainable PRs** without breaking existing functionality. More lines of code or more PRs are not automatically better.

See `AGENTS.md`, `SECURITY.md`, `TASKS/`, `EVALUATION.md`.
