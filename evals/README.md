# bob triggering evals

Cases for `claude plugin eval` (Claude Code 2.1.269 or later). They check that the right skill is invoked from realistic prompts that do not name bob. Collision tests against other plugins are deliberately not included.

Every case has one free `tool_used: Skill` grader (a regex over the skill name, plugin prefix optional). Alternatives are written as regex alternation.

| Group | Cases | Checks |
|---|---|---|
| `positive-*` | 29 | One per skill in `skills/`. The named skill is invoked. For the 13 phase skills, the `bob` hub alone is also accepted (the hub routes) |
| `forgot-bob-*` | 3 | Plain work request (plan, fix bug, write vision) in a project that uses bob: the `bob` hub is invoked |
| `no-trigger-*` | 4 | Casual chat must NOT invoke `implement`, `setup`, `docker-setup` or `dev` (`min: 0`, `max: 0`) |

Fixture: `_fixtures/bob-project.sh` builds a tiny bob project (`docs/process/done-criteria.md`, `projects/x/_kanban.md`, `docs/domain/README.md`, one source file). Only the `forgot-bob-*` cases use it, through a symlinked `scaffold.sh`, so they need `--scaffold`.

## Run

Always use `--ablation none`: Skill graders are with-only indicators, so the no-plugin arm adds cost and no information.

```bash
cd bob
# full suite (36 cases x 3 runs)
claude plugin eval . --ablation none --scaffold --no-publish -j 4 --max-cost-usd 20
# one group or one case
claude plugin eval . --ablation none --scaffold --case 'forgot-bob-*'
claude plugin eval . --ablation none --case 'no-trigger-*' --runs 1
```

Add `--model <m>` to pin the model and `--json out.json` for machine-readable results. Reports go to `evals/results/` (gitignored).

## Cost and time

Measured: about $0.12 and 15 s per run. Full suite: 108 runs, roughly $13 and about 8 minutes at `-j 4`. `--runs 1` cuts that to about $4. Parallel runs share one rate limit; a session limit mid-run makes the remaining runs error with score 0, so check each run's `error` before reading a failure as a triggering failure.
