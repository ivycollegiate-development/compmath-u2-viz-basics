# U2 L07 — Lab: Bar Charts and Categorical Data

**LO:** build bar charts from categorical data in your own lab repo; fix the two `FIX ME` bugs in `charts.py`; pass all 4 `self_check.py` tests.

**Estimated time:** 85 minutes.

---

## PART 0 — GET YOUR LAB REPO (10 min)

Every student has their own lab repo for this unit. The naming convention is:

```
compmath-u2-viz-basics-<username>_student
```

Where `<username>` is your GitHub username (lowercase, as it appears in the URL).

**Clone yours now:**

```bash
cd ~
git clone https://github.com/ivycollegiate-development/compmath-u2-viz-basics-$(whoami)_student.git compmath-u2-viz-basics
cd compmath-u2-viz-basics
```

If `$(whoami)` is not your GitHub username, replace it manually:

```bash
git clone https://github.com/ivycollegiate-development/compmath-u2-viz-basics-<your-github-username>_student.git compmath-u2-viz-basics
```

**What you should see inside:**

```
compmath-u2-viz-basics/
├── charts.py          # <-- has 2 bugs marked "FIX ME"
├── self_check.py      # <-- 4 tests; you must pass all 4
├── data/
│   ├── u2_dataset1_study_habits.csv
│   ├── u2_dataset2_mental_health.csv
│   ├── u2_dataset3_activities.csv
│   └── u2_student_performance_data.csv
└── journal-<username>.md  # your journal file
```

---

## PART 1 — RUN THE SELF-CHECK FIRST (5 min)

```bash
python3 self_check.py
```

You should see:

```
Test 1/4: test_bar_chart_categories ... FAIL
Test 2/4: test_bar_chart_labels ... FAIL
Test 3/4: test_bar_chart_colors ... FAIL
Test 4/4: test_bar_chart_y_starts_at_zero ... FAIL
```

**All 4 fail. That is expected.** Your job is to fix `charts.py` until all 4 pass.

---

## PART 2 — UNDERSTAND THE TWO BUGS (15 min)

Open `charts.py` in VS Code:

```bash
code charts.py
```

You will see two sections marked `# FIX ME`. **Do not change anything else.** The tests only check the specific outputs these bugs break.

### Bug 1 — Category Ordering (Test 1)

```python
# FIX ME 1: Category order is wrong
categories = ["High", "Low", "Mid"]  # Current: alphabetical order
# Should be: Low, Mid, High (semantic order, not alphabetical)
```

**The fix:** Change the list to `["Low", "Mid", "High"]`.

**Why this matters:** A bar chart with categories in alphabetical order (High, Low, Mid) confuses the reader — the natural order is Low → Mid → High. This is a *semantic ordering* bug, not a syntax bug. The code runs; the output is misleading.

### Bug 2 — Y-Axis Starts at Zero (Test 4)

```python
# FIX ME 2: y-axis does not start at zero
plt.ylim(40, 100)  # Current: zooms in on the data range
# Should be: plt.ylim(0, 100)  OR remove this line entirely
```

**The fix:** Either change to `plt.ylim(0, 100)` or delete the line. **A bar chart's y-axis MUST start at zero.** Truncating it exaggerates visual differences between bars — that is a dishonest chart.

**Why this is a bug, not a choice:** The rule is absolute for bar charts. (Line plots and scatter plots may start at non-zero with a stated reason; bar charts never.) This is the honesty rule from U2 L05 Part 4.

---
