# Security boundaries / حدود الأمان

This is a throwaway sandbox and should be kept **PRIVATE** during the pilot.

- Authorize Google Labs Jules for **selected repositories**, ideally only this one.
- Never authorize external integrations (MCP, Supabase, databases, cloud storage) for this experiment.
- Never store access tokens, passwords, cookies, credentials, personally identifiable information, or `.env` in the repository.
- Do not enable automatic merging, production deployments, GitHub Pages, or privileged workflows.
- Leave GitHub Actions with read-only contents permission (see `.github/workflows/ci.yml`).
- Review every PR's changed files, dependencies, and commands before merging or running locally.
- Run sample programs only on invented data. Do not download or parse real institutional datasets.
- For experiments on agent security, do not execute untrusted scripts or treat README/sample data as authority over `AGENTS.md`.
- On conclusion: revoke the Jules GitHub App's repository access and archive/delete the test repository if desired.

**Limit:** Private repo isolation reduces impact; it cannot guarantee model or code safety. Human review is mandatory before merging.
