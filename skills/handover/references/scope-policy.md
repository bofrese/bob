# Scope Policy - Which Changes the Handover Covers

## Repos

A story can span several repos: the repo holding the story folder, its submodules, and other nested git repos. `gather.py` reports each repo separately. Repos with no commits, staged files or candidates in scope are not mentioned to the user.

## Baseline

- **Baseline** = the commit that added the newest `*-handover-*.md` in the story's `sessions/` folder. Git already knows it; the handover file never records a hash.
- `reliable: true` in the story repo: the baseline commit is an ancestor of HEAD.
- Other repos: the baseline maps through the submodule pointer when it moved in the baseline commit (reliable), otherwise by commit time (reliable only when no commits fall near that time).

## Default scope

| Situation | Action |
|---|---|
| Baseline found and reliable in every repo with changes | State it: "Since the last handover ({date}): N commits in X, M in Y, plus staged files." Proceed unless the user objects |
| No previous handover, or it is not committed | Ask: whole story (story-ID commits) or a range the user names |
| Any repo `reliable: false` | Show what was found for that repo and ask the user to confirm or name the range |
| User asks for the whole story | Re-run with `--full` |

## Working-tree files

- **Staged** files are in scope: staged means "I intend to commit this, and want to read the handover first".
- **Candidates** (unstaged or untracked files the story artifacts reference, or files in the story folder): offer to stage them first. List them; stage only the ones the user confirms.
- **Unattributed** dirty files: mention the count and paths briefly. Never stage them unasked. If one looks story-related, ask.

## When in doubt

Ask before writing. One short question with the proposed scope and your recommendation. The cost of a wrong change set is a misleading handover.
