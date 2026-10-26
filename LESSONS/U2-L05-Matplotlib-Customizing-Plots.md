# U2 L05 — Matplotlib: Customizing Plots

**LO:** create line plots, bar charts, and scatter plots with appropriate labels, colors, and formatting.

**Estimated time:** 75 minutes.

In U2 L03 you made your first plots. Today we make them *readable* — titles, labels, colors, grids, legends — and save them as image files. Three chart types, one script, zero `pip install` (matplotlib 3.10 is already on your machine).

---

## PART 0 — GET ORIENTED (10 min)

First command, always:

```bash
pwd
```

This tells you where you are. If the output does not end with your home directory (`/home/yourname` or `/Users/yourname`), you are not where you think you are — stop and ask.

Then make a folder for today's work and open it in VS Code:

```bash
mkdir -p unit2_plots
cd unit2_plots
touch charts.py
code .
```

**Why this sequence:** `cd ~` guarantees you start from home. `mkdir -p` creates the folder (the `-p` means "no error if it already exists"). `touch charts.py` creates an empty file so VS Code has something to open. `code .` opens the *folder* in VS Code, not just the file — this matters later when you have multiple files.

Everything today goes in `charts.py`. Run it after every part with `python3 charts.py` — you should watch your three charts appear and improve each time.

**Common mistake:** typing `python charts.py` (no `3`). On the VPS, `python` may point to Python 2, which will fail. Always use `python3`.

---

## PART 1 — CODE-ALONG: LINE PLOT (20 min)

A line plot answers: *how does one thing change as another increases?*

We will build this step by step. After each step, run the file and look at the window that pops up.

### Step 1 — Just the data and the plot call

```python
import matplotlib.pyplot as plt

hours = [1, 2, 3, 4, 5, 6]
scores = [55, 62, 71, 78, 85, 90]

plt.plot(hours, scores)
plt.show()
```

Run it. You should see a plain blue line connecting six points. No labels, no title, no grid.

**What just happened:**
- `import matplotlib.pyplot as plt` — the standard import
- `plt.plot(hours, scores)` — draws line connecting (1,55), (2,62), ...
- `plt.show()` — opens the window

### Step 2 — Add markers

```python
plt.plot(hours, scores, marker="o", color="steelblue")
```

Run it. Now each data point has a circle on it.

**Why `marker="o"`:** Without it, you only see the line. With it, you see exactly where the measurements were taken. This matters when data is sparse — if you only measured at hours 1, 3, and 6, the line would imply smooth change between them, but the markers show you only have three real observations.

**Why `color="steelblue"`:** The default blue is fine, but `steelblue` is a named color that reads well on white backgrounds and is colorblind-safe. Matplotlib knows ~150 named colors (try `print(plt.colormaps())` later). You can also use hex codes like `"#4A90D9"`.

### Step 3 — Add title and axis labels

```python
plt.title("Study Hours vs Test Score — Positive Trend")
plt.xlabel("Study Hours (hours per week)")
plt.ylabel("Test Score (points)")
```

Run it. Now the chart tells a complete story on its own.

**Why every plot needs all three:**
A chart without labels is a rumor, not evidence. If you hand this to someone who was not in class, they should understand it in 5 seconds without you explaining.

### Step 4 — Add a subtle grid

```python
plt.grid(True, alpha=0.3)
```

Run it. Faint gray lines appear behind the data.

**Why `alpha=0.3`:** `alpha` controls transparency (0 = invisible, 1 = solid). The grid should help the eye trace values, not compete with the data. `0.3` is a good default — visible enough to use, faint enough to ignore.

### Complete Part 1 code so far

```python
import matplotlib.pyplot as plt

hours = [1, 2, 3, 4, 5, 6]
scores = [55, 62, 71, 78, 85, 90]

plt.figure()
plt.plot(hours, scores, marker="o", color="steelblue")
plt.title("Study Hours vs Test Score — Positive Trend")
plt.xlabel("Study Hours (hours per week)")
plt.ylabel("Test Score (points)")
plt.grid(True, alpha=0.3)
plt.savefig("line_plot.png", dpi=150, bbox_inches="tight")
plt.show()
```

**Check your understanding (write in notes, then discuss):**
- What happens if you swap `hours` and `scores` in `plt.plot()`?
- What does `marker="s"` produce? `marker="^"`?

---

## PART 2 — CODE-ALONG: BAR CHART (15 min)

A bar chart compares *categories*. The key difference from a line plot: the x-axis holds **labels**, not numbers.

```python
groups = ["Low Sleep", "Mid Sleep", "High Sleep"]
avg_scores = [62, 74, 88]
colors = ["#c0392b", "#f39c12", "#27ae60"]

plt.figure()
plt.bar(groups, avg_scores, color=colors)
plt.title("Average Test Score by Sleep Group")
plt.xlabel("Sleep Group")
plt.ylabel("Average Test Score (points)")
plt.grid(True, alpha=0.3, axis="y")
plt.savefig("bar_chart.png", dpi=150, bbox_inches="tight")
plt.show()
```

Run it. Three bars, three different colors.

**Why a list of colors?** `plt.bar` accepts either a single color (all bars same) or a list (one per bar). We passed a list so each group gets its own color — red for low sleep, orange for mid, green for high. This is a *semantic* choice: the colors encode meaning (bad → okay → good), not just decoration.

**Which axis carries what?**
- Bar chart: x = categories (labels), y = numeric values
- Line plot: x = numeric, y = numeric
- Scatter: x = numeric, y = numeric

**Common mistake:** passing numbers as strings on the x-axis for a line plot, or passing categories to a line plot. `plt.plot` expects numbers on both axes. `plt.bar` expects categories on x, numbers on y. `plt.scatter` expects numbers on both.

**Check your understanding:**
- What would `plt.bar([1,2,3], [10,20,30])` produce? (Numbers as categories — works but usually wrong intent)

---
