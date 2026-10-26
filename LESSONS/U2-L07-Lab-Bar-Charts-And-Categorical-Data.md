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

## PART 3 — FIX AND VERIFY (30 min)

Apply both fixes, save, and run:

```bash
python3 self_check.py
```

**Expected after both fixes:**

```
Test 1/4: test_bar_chart_categories ... PASS
Test 2/4: test_bar_chart_labels ... PASS
Test 3/4: test_bar_chart_colors ... PASS
Test 4/4: test_bar_chart_y_starts_at_zero ... PASS

All 4 tests passed!
```

If any test still fails:
- Read the test output carefully — it tells you exactly what assertion failed
- `Test 1` = category order; `Test 4` = y-axis starts at zero
- Do not change `self_check.py` — only fix `charts.py`

---

## PART 4 — EXTENSION: YOUR OWN BAR CHART (20 min)

Using the **same datasets** in `data/`, build **one additional bar chart** in a new file `my_bar_chart.py` that:

1. Loads data from one of the CSV files (your choice)
2. Creates a bar chart with **semantic category order**
3. Has title, x-label with units, y-label with units
4. Has y-axis starting at zero
5. Uses deliberate colors (not defaults)
6. Saves as `my_bar_chart.png`

**Suggestions:**
- `u2_dataset2_mental_health.csv`: Stress Level (Low/Mid/High) vs average Anxiety Score
- `u2_dataset3_activities.csv`: Activity Type vs average Hours/Week
- `u2_student_performance_data.csv`: Parent Education Level (categorical) vs Math Score

**Before you submit, run your script and verify the PNG opens and looks correct.**

---

## PART 5 — JOURNAL + PUSH (15 min)

```bash
code journal-$(whoami).md
```

Answer in 2–3 sentences each:
- Why is semantic category order (Low/Mid/High) better than alphabetical (High/Low/Mid)?
- What would happen if you left `plt.ylim(40, 100)` on a bar chart comparing 42 vs 48?

```bash
git add charts.py my_bar_chart.py my_bar_chart.png journal-$(whoami).md
git commit -m "L07: fixed 2 bugs + own bar chart"
git push
```

---

## TURN IN — SCREENSHOT (due 23:59 tonight)

One screenshot showing, in order:

```
python3 self_check.py
git push
```

Submit the screenshot to the U2 L07 assignment on Google Classroom.

**Keep the terminal open** — spot-checks happen.

---

## WHY THIS MATTERS

**Two bugs, one lesson:**
1. **Semantic order** — The computer does not know what "Low/Mid/High" means. You do. Every chart you publish, you order the categories for the *reader*, not the computer.
2. **Y-axis zero** — The honesty rule. A bar chart that doesn't start at zero is a visual lie. It passed syntax check; it failed the honesty check.

These are not "beginner mistakes." They are the mistakes that appear in published papers, news articles, and corporate dashboards every day. You fixed them today. Next time, you'll spot them before they ship.

---

## NEXT

**U2 L08 — Reading Data From Files** [U2-L08-Reading-Data-From-Files.md](../compmath-u2-data-lab/LESSONS/U2-L08-Reading-Data-From-Files.md)

*(Note: U2 L08–L12 and L15–L18 use the data-lab repo. The U2 L07 lab repo you just used is the *viz-basics* repo for charting; U2 L08 switches to the *data-lab* repo for data work.)*