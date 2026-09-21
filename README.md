## Before you start — every session

You work on the class VS Code server, in your own clone of this repo.
Your userid shows up in your repo name, your clone URL, and your filenames
via `$(whoami)`: `whoami` prints your userid, and `$(whoami)` inserts it
automatically. If the folder is missing, re-clone it — your lesson has the
exact URL, always ending in `_student.git`.

**Pull before work, every session** — it gets any changes I pushed to your
repo since last class:

```bash
cd ~/<your-clone-folder>
git config pull.rebase false
git pull
```

- `git config pull.rebase false` tells git how to combine work; run it once,
  it is not an error if you already ran it.
- If the pull prints `Already up to date.` you have everything.
- **Asked for a username/password?** GitHub username plus Personal Access
  Token (PAT) — never your GitHub password.

---

# compmath-u2-viz-basics

You received your OWN copy of this repo by accepting a GitHub invitation in
your email. Everything you do in Unit 2 happens in your copy.

    charts.py       starter plotting script with 2 FIX ME bugs
    self_check.py   run this to check yourself: starts at 2 of 4 passing
    data/           the Unit 2 CSV datasets

Run:

    python3 self_check.py

Your job this unit: make all 4 checks pass, then keep using this repo to
practice real charts from real data.
