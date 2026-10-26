# U2 L02 — Bridge: From Numbers to Data

**LO:** transition from Unit 1 (numbers) to Unit 2 (data visualization) by exploring what data looks like and why it matters.

Yesterday you proved you can handle numbers. Today those numbers start meaning something: we meet our first **dataset** — and discover that real data is messier than anything we typed ourselves. No plotting yet; today is pure exploration in a Python script (`explore.py`).

---

## PART 1 — OPENING DISCUSSION: WHAT IS DATA? (10 min)

Before any code, answer in your notes:

**Key idea to write down:** **data is numbers plus context.** A number tells you *how much*; data tells you *how much of what, from whom, measured when*.

---

## PART 2 — MEET THE DATASET (10 min)

Our first dataset this unit is a study-habits survey: 52 students, four measurements each. Here is a 5-row excerpt:

```
Student_ID,Study_Hours,Test_Score,Attendance,Sleep_Hours
S01,4.5,82,0.93,7.0
S02,1.0,55,0.71,5.5
S03,7.0,95,0.98,8.0
S04,3.0,74,0.88,6.5
S05,0.5,48,0.65,5.0
```

In your notes, for each column write: *what it measures, and what unit or range it lives in?* (Attendance is a fraction — 0.93 means 93% of classes.)

Questions to discuss with your table:
- What does `Test_Score` measure? What is a "good" value?
- Why is `Student_ID` not a number you can do math on?

---

## PART 3 — CODE-ALONG: READING A CSV WITH ONLY THE STDLIB (15 min)

Open your Unit 2 lab repo. If you have not cloned it yet, do this first:

```bash
cd ~
git clone https://github.com/ivycollegiate-development/compmath-u2-data-lab-$(whoami)_student.git compmath-u2-data-lab
cd compmath-u2-data-lab
git pull
```

(Your username + Personal Access Token, not your GitHub password.)

You should be inside `compmath-u2-data-lab`, where this unit's files live under `data/`. Every path from here on is relative to this folder.

Create a new script `explore.py` in VS Code:

```bash
code explore.py
```

Run it as you build it (it only prints what you tell it to, so start small):

```bash
python3 explore.py
```

A CSV (comma-separated values) file is just text where each line is a row and commas split the columns. Python's standard library ships a module for it — no installs, ever. Put this in `explore.py`:

```python
import csv
with open("data/u2_dataset1_study_habits.csv") as f:
    rows = list(csv.reader(f))

# Un-comment each print below one at a time, save, and re-run
# print(len(rows))
# print(rows[0])
# print(rows[1])
```

Save and run:

```bash
python3 explore.py
```

`print(len(rows))` should give **53**, and `rows[0]` should be the column names.

Now answer in your notes, then un-comment the prints one at a time and re-run to test:
- What is `rows[0]`?
- What is `rows[1]`?
- How many data rows (not counting header)?

---
