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

## PART 4 — THE MESSY FIRST LINE (10 min)

This file is well-behaved: a header, then 52 rows of data. Not every file this unit hands you is that polite. Here is the other one:

```bash
head -3 data/u2_student_performance_data.csv
```

Line 1 is a **`#` comment** — a note someone left in the file explaining the units. Line 2 is the real header.

Append this to `explore.py`, save, and run `python3 explore.py` — exactly as you would with the clean file:

```python
with open("data/u2_student_performance_data.csv") as f:
    reader = csv.reader(f)
    rows = list(reader)
```

It crashes. That `#` line is not data at all. Real datasets are full of these surprises: comment lines, blank rows, missing values, weird units. Our first job as data people is to notice them *before* doing math.

The fix is to skip the comment and then skip the header. In `explore.py`, replace that last block with this fix, save, and re-run:

```python
with open("data/u2_student_performance_data.csv") as f:
    lines = [ln for ln in f if ln.strip() and not ln.startswith("#")]
    reader = csv.reader(lines)
    rows = list(reader)
    print(len(rows))
```

**In your notes:** why index `2:` and not `1:`? What would `1:` have given you?

---

## PART 5 — COMPUTE: NUMBERS BECOME INFORMATION (15 min)

Everything from Unit 1 applies now. Go back to the clean file and convert, then average:

```python
with open("data/u2_dataset1_study_habits.csv") as f:
    lines = [ln for ln in f if ln.strip() and not ln.startswith("#")]
    reader = csv.DictReader(lines)
    rows = list(reader)

scores = [float(r["Test_Score"]) for r in rows]
hours = [float(r["Study_Hours"]) for r in rows]

print(f"Mean score: {sum(scores)/len(scores):.1f}")
print(f"Mean hours: {sum(hours)/len(hours):.1f}")

# Compare high vs low study hours
high = [s for s, h in zip(scores, hours) if h >= 4]
low = [s for s, h in zip(scores, hours) if h < 4]
print(f"High study (>=4h): mean score = {sum(high)/len(high):.1f}")
print(f"Low study (<4h): mean score = {sum(low)/len(low):.1f}")
```

Append this to `explore.py`, save, and run `python3 explore.py`.

In your notes, then verify from your script's output:
- What does `max(scores)` tell you?
- What does `min(scores)` tell you?
- The difference between high-study and low-study averages — what does that suggest?

That's the whole game of data work: **a pile of numbers becomes one comparable statement.** Next lesson, we make that statement a *picture*.

---

## PART 6 — DISCUSSION: WHO IS THIS DATA ABOUT? (5 min)

This dataset describes *people* — including, in spirit, you. In your notes:
- If this were real student data, what would you owe the people it describes?
- What is the difference between "data about students" and "student data"?

---

## PART 7 — JOURNAL + PUSH (last 10 min)

In your lab repo:

```bash
cd ~/compmath-u2-data-lab
code journal-$(whoami).md
```

Answer in 2-3 sentences each:
- What surprised you about the comment-line trap?
- Why does `csv.DictReader` give you strings, not numbers?

---

## TURN IN — SCREENSHOT (due 23:59 tonight)

One screenshot showing, in order:

```
len(rows)
rows[0]
messy[0]
messy[1]
len(data_rows)
git push
```

Submit the screenshot to this assignment on Google Classroom.
Keep the terminal open — spot-checks.

---

## NEXT

**U2 L03 — Launch: What Makes a Good Visualization** [U2-L03-Launch-What-Makes-A-Good-Visualization.md](LESSONS/U2-L03-Launch-What-Makes-A-Good-Visualization.md)