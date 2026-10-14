# compmath-u2-viz-basics — U2 L07 Lab: Bar Charts and Categorical Data

**LO:** apply matplotlib skills to real data from a repo; fix two *label-rule* bugs in a charting script and get a self-check from 2/4 to 4/4; recognize when a bar chart's bands, not its labels, are the problem.

**Estimated time:** 85 minutes. We move slower so the debugging process teaches, not just the result.

---

## PART 0 — GET YOUR LAB REPO (first 10 minutes)

**Step 1:** Check your school Gmail — you have an invitation to collaborate on your own private repo. Accept it. (If you don't see it, check Spam/Promotions, then ask.)

**Step 2:** Your repo is named `compmath-u2-viz-basics-<username>_student` under the `ivycollegiate-development` organization. The `<username>` part matches your GitHub username.

**Step 3:** Clone it. Start with `pwd` — always know where you are.

```bash
pwd
cd ~
git clone https://github.com/ivycollegiate-development/compmath-u2-viz-basics-$(whoami)_student.git compmath-u2-viz-basics
cd compmath-u2-viz-basics
ls
```

**Why this sequence:**
- `pwd` confirms you're in your home directory before cloning
- `cd ~` guarantees the clone lands in a predictable place (`~/compmath-u2-viz-basics`)
- The `$(whoami)` expands to your system username, which matches the repo suffix
- `ls` lets you verify the clone worked

**If the clone fails:** Re-copy the exact URL from the invitation email — that is always the fix. Typos in the org name (`ivycollegiate-development`) or the `_student` suffix are the most common causes.

**What you should see.** `ls` shows the charting script `charts.py`, the graders' `self_check.py`, this `README.md`, and a `data/` folder. `ls data/` shows five CSV files, including the three Unit 2 datasets you previewed in U2 L05:

- `u2_dataset1_study_habits.csv`
- `u2_dataset2_mental_health.csv`
- `u2_dataset3_activities.csv`

Today we work with the first one.

---

## PART 1 — MEET THE DATA (10 min)

The study-habits file has **50 rows**, one per student. Its columns:

```
Student_ID, Study_Hours, Test_Score, Attendance, Sleep_Hours
```

Peek at the top of the file:

```bash
head -6 data/u2_dataset1_study_habits.csv
```

**Look closely at the first lines.** The very first line starts with a `#` (a comment), and there is a **blank line** before the real header row. If you hand that file straight to `csv.DictReader`, the reader treats the *comment* as the header, and every column name comes out wrong.

The starter code in `charts.py` handles this by filtering out comment lines and blank lines before passing the rest to `DictReader`:

```python
lines = [ln for ln in f if ln.strip() and not ln.startswith("#")]
```

---

## REPO CONTENTS

| File | Purpose |
|------|---------|
| `charts.py` | Starter plotting script with **2 `FIX ME` bugs** |
| `self_check.py` | Run this to check yourself: starts at **2 of 4 passing** |
| `data/` | Unit 2 CSV datasets |
| `README.md` | This file — the lab instructions |

---

## BEFORE YOU START — EVERY SESSION

You work on the class VS Code server, in your own clone of this repo.
Your userid shows up in your repo name, your clone URL, and your filenames
via `$(whoami)`: `whoami` prints your userid, and `$(whoami)` inserts it
automatically. If the folder is missing, re-clone it — your lesson has the
exact URL, always ending in `_student.git`.

**Pull before work, every session** — it gets any changes I pushed to your
repo since last class:

```bash
cd ~/compmath-u2-viz-basics
git config pull.rebase false
git pull
```

- `git config pull.rebase false` tells git how to combine work; run it once,
 it is not an error if you already ran it.
- If the pull prints `Already up to date.` you have everything.
- **Asked for a username/password?** GitHub username plus Personal Access
 Token (PAT) — never your GitHub password.

---

## YOUR JOB THIS UNIT

1. Run the self-check to see the starting state:
   ```bash
   python3 self_check.py
   ```
   Expected: **2 of 4 checks passing**

2. Open `charts.py`, find the two `FIX ME` comments, and fix the label bugs.

3. Re-run the self-check until you see **4 of 4 checks passing**.

4. Commit and push your fix:
   ```bash
   git add charts.py
   git commit -m "Fix label bugs in charts.py"
   git push
   ```

5. Keep using this repo to practice real charts from real data throughout Unit 2.