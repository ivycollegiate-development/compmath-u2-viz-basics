# U2 L03 — Launch: What Makes a Good Visualization

**LO:** understand the purpose of data visualization and produce your first matplotlib plot with a title, axis labels, and units.

Yesterday numbers became information. Today information becomes a **picture**. We meet `matplotlib` — the standard Python plotting library — and make our first chart. matplotlib 3.10 is already installed on your workspace; you never need to install anything.

---

## PART 1 — WHY PICTURES BEAT TABLES (10 min)

Here are two views of the same data:

```
Table: Day 1: 12, Day 2: 18, Day 3: 9, Day 4: 22, Day 5: 30, Day 6: 25, Day 7: 15
```

Now picture it as a line climbing and dipping through the week. In your notes, before any code:

**Key ideas to write down:**
- A table requires reading; a chart requires *seeing*
- The pattern (Monday low, Friday high) is instant in the picture
- But a chart without labels is a guess — not evidence

---

## PART 2 — CODE-ALONG: YOUR FIRST PLOT (15 min)

Open your workspace. First command, always:

```bash
cd ~
```

Create a new script `first_plot.py` in VS Code and run it as you build it:

```bash
code first_plot.py
```

Put each snippet below into `first_plot.py`, save, and run it with:

```bash
python3 first_plot.py
```

The import everyone in the data world uses:

```python
import matplotlib.pyplot as plt
```

(`pyplot` is matplotlib's drawing toolbox; everyone shortens it to `plt`. Never type the long name again.)

A line chart is just x-values and y-values:

```python
days = [1, 2, 3, 4, 5, 6, 7]
temps = [12, 18, 9, 22, 30, 25, 15]
plt.plot(days, temps)
plt.show()
```

A window opens with your first chart. Now answer in your notes, then try:

```python
plt.plot(temps, days)        # swapped axes
plt.plot(days, [t + 5 for t in temps])  # shifted up
plt.show()
```

---

## PART 3 — ANATOMY OF A PLOT: THE PARTS EVERY CHART NEEDS (15 min)

A chart without labels is a guess. A complete chart has:

1. **Title** — states the question the chart answers
2. **x-label** — what the horizontal axis measures, with units
3. **y-label** — what the vertical axis measures, with units

Rebuild your chart properly:

```python
plt.figure()  # fresh canvas
plt.plot(days, temps, marker="o", color="steelblue")
plt.title("Daily High Temperatures — Week 1")
plt.xlabel("Day of Week")
plt.ylabel("Temperature (°C)")
plt.grid(True, alpha=0.3)
plt.savefig("first_chart.png", dpi=150)
plt.show()
```

In your notes, then verify:
- What does `marker="o"` add?
- What does `color="steelblue"` change?
- Why `plt.figure()` before the plot?

---

## PART 4 — PLOT OUR REAL DATA: STUDY HOURS (15 min)

Yesterday's dataset, today as a picture. Open your lab repo first:

```bash
cd ~/compmath-u2-data-lab
git pull
```

Then replace the contents of `first_plot.py` with this real-data version, save, and run `python3 first_plot.py`:

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
plt.savefig("study_vs_score.png", dpi=150)
plt.show()
```

In your notes:
- Why `scatter` not `plot` here? (Both axes are numeric, but we want discrete points, not a connected line)
- What does `alpha=0.6` do with 52 points?

---

## PART 5 — SAVEFIG: MAKE IT A TURN-IN (10 min)

`plt.show()` puts a chart on a screen; `plt.savefig()` writes it to a file you can submit and keep:

```python
plt.savefig("my_chart.png", dpi=150, bbox_inches="tight")
```

(Run it *before* or instead of `show()` in a script — after the window closes, the figure is gone.)

Back in the terminal, check it exists:

```bash
ls -lh my_chart.png
```

In your notes: what does `dpi=150` change, and why does a crisp image matter when someone else grades your chart?

---

## PART 6 — DISCUSSION: WHAT MAKES A CHART GOOD? (5 min)

With your table, rank these sins from worst to least-worst and defend it:

1. Missing y-label
2. Truncated y-axis on a bar chart
3. No title
4. Wrong chart type (line plot for categories)
5. Default colors on overlapping points

One sentence each in your notes. In U2 L05 we judge a real news chart against exactly this list.

---

## PART 7 — SAVE YOUR WORK + PUSH (last 10 min)

Put your script and image in your lab repo:

```bash
cd ~/compmath-u2-data-lab
git add first_plot.py study_vs_score.png
git commit -m "L03: first scatter plot with labels"
git push
```

---

## TURN IN — SCREENSHOT (due 23:59 tonight)

One screenshot showing, in order:

```
ls -lh study_vs_score.png
git push
```

Submit the screenshot to this assignment on Google Classroom.
Keep the terminal open — spot-checks.

**Early finishers:** add a second series to the scatter (Sleep_Hours vs Test_Score) in a different color with `label=` and `plt.legend()`, and save a second PNG.

---

## NEXT

**U2 L04 — Review: From Data to Visualization** [U2-L04-Review-Data-To-Visualization.md](LESSONS/U2-L04-Review-Data-To-Visualization.md)