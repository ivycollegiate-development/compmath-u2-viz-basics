# U2 L04 — Review: From Data to Visualization

**LO:** consolidate U2 L02–L03 concepts — messy data, CSV reading, first matplotlib plots — before advancing to chart customization in L05.

No new content today. You have seen real datasets, read CSV files with the stdlib, and produced your first labeled scatter plot. This lesson checks that the foundation is solid before L05 adds customization (colors, legends, savefig, bar/line/scatter choice).

---

## PART 1 — CONCEPT CHECK (15 min, closed notes)

Answer in your notes. One sentence each unless marked.

### A. Data vs. Numbers (from L02)

`messy[0][1] + 1`

What is the type of `messy[0][1]`? Why does adding 1 fail or give a surprising result?

### B. CSV Reading Mechanics (from L02)

```python
import csv
with open("data/u2_dataset1_study_habits.csv") as f:
    rows = list(csv.reader(f))
```

- What is `rows[0]`?
- What does `rows[1:]` give you?
- What does `rows[2:]` give you?
- What does `rows[3:]` give you?

### C. First Visualization (from L03)

```python
days = [1,2,3]
temps = [12,18,9]
plt.plot(days, temps)
plt.scatter(days, temps)
```

- What does `plt.scatter` do that `plt.plot` does not?
- When would you use `scatter` vs `plot`?
- What does `plt.savefig("chart.png", dpi=150)` do that `plt.show()` does not?

### D. Quick Apply

```python
import matplotlib.pyplot as plt
plt.plot([1,2,3], [10,20,30])
plt.scatter([1,2,3], [10,20,30])
plt.legend()
plt.savefig("quick.png", dpi=150)
```

What is wrong with this chart? (Hint: what does `legend()` show when nothing has a `label=`, and which axis has no name?)

---

## PART 2 — LIVE REBUILD (20 min)

Open your lab repo and rebuild the L03 scatter plot **from memory** — no copy-paste from old screenshots.

```bash
cd ~/compmath-u2-data-lab
git pull
```

Create a new file `first_plot.py` in VS Code and, from memory — no copy-paste — reconstruct the complete L03 Part 4 script into it. Save, then run:

```bash
code first_plot.py
python3 first_plot.py
```

Rebuild it cold:

```python
import csv
import matplotlib.pyplot as plt

with open("data/u2_dataset1_study_habits.csv", newline="") as f:
    lines = [ln for ln in f if ln.strip() and not ln.startswith("#")]
    reader = csv.DictReader(lines)
    rows = list(reader)

study = [float(r["Study_Hours"]) for r in rows]
score = [float(r["Test_Score"]) for r in rows]

plt.figure()
plt.scatter(study, score, s=20, alpha=0.6, color="steelblue")
plt.title("Study Hours vs Test Score — Positive Trend")
plt.xlabel("Study Hours (hours per week)")
plt.ylabel("Test Score (points)")
plt.grid(True, alpha=0.3)
plt.savefig("review_scatter.png", dpi=150)
plt.show()
```

If you get stuck, check your L03 notes — but the goal is to do it cold.

---

## PART 3 — EXTENSION: ADD A SECOND SERIES (10 min)

Using the **same dataset**, add `Sleep_Hours` (column 3) as a second scatter series in a different color with `label=` and `plt.legend()`. Save as `review_two_series.png`.

```python
sleep = [float(r["Sleep_Hours"]) for r in rows]

plt.figure()
plt.scatter(study, score, s=20, alpha=0.6, color="steelblue", label="Study Hours")
plt.scatter(sleep, score, s=20, alpha=0.6, color="seagreen", label="Sleep Hours")
plt.title("Study vs Sleep vs Test Score")
plt.xlabel("Hours")
plt.ylabel("Test Score (points)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig("review_two_series.png", dpi=150)
plt.show()
```

In your notes: what relationship (if any) do you see between Sleep_Hours and Test_Score?

---

## PART 4 — PAPER CHECK PREVIEW (5 min)

Tuesday (U2 L06) is a paper check on L03–L05 concepts. In your notes, write one question you would put on that check for each of these topics:
- Chart type choice (line vs bar vs scatter)
- The label rule (title, x-label, y-label)
- `savefig` vs `show` order

---

## PART 5 — JOURNAL + PUSH (last 10 min)

```bash
cd ~/compmath-u2-data-lab
code journal-$(whoami).md
```

Answer in 2–3 sentences each:
- What was the hardest part of rebuilding from memory?
- What does the `label=` + `legend()` pair do that nothing else does?

```bash
git add first_plot.py review_scatter.png review_two_series.png journal-$(whoami).md
git commit -m "L04: review rebuild + two series"
git push
```

---

## TURN IN — SCREENSHOT (due 23:59 tonight)

One screenshot showing, in order:

```
ls -lh first_plot.py review_scatter.png review_two_series.png
git push
```

Submit the screenshot to this assignment on Google Classroom.

---

## NEXT

**U2 L05 — Matplotlib: Customizing Plots** [U2-L05-Matplotlib-Customizing-Plots.md](LESSONS/U2-L05-Matplotlib-Customizing-Plots.md)