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

## PART 3 — CODE-ALONG: SCATTER PLOT (15 min)

A scatter plot answers: *is there a relationship between two number columns?* Unlike a line plot, it does not connect the dots — each point stands alone.

```python
sleep = [5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0]
gpa = [2.1, 2.4, 2.8, 3.1, 3.3, 3.5, 3.7, 3.9]

plt.figure()
plt.scatter(sleep, gpa, s=40, alpha=0.6, color="purple")
plt.title("Sleep Hours vs GPA — Positive Association")
plt.xlabel("Sleep Hours (per night)")
plt.ylabel("GPA (4.0 scale)")
plt.grid(True, alpha=0.3)
plt.savefig("scatter_plot.png", dpi=150, bbox_inches="tight")
plt.show()
```

Run it. Eight purple dots, no lines.

**What `s=40` does:** `s` stands for "size" (area in points²). Default is 20. Larger dots are easier to see when points overlap; smaller dots work better for dense data. Try `s=10` and `s=100` to see the difference.

**Why no line?** A line implies *order* and *continuity* — "when x increases, y follows this path." A scatter makes no such claim. It just shows pairs. If the points form a cloud sloping upward, there's a positive association. If they're a blob, there isn't.

**Check your understanding:**
- When would you use a line plot instead of a scatter for these same two variables?

---

## PART 4 — LEGENDS AND SAVING (15 min)

When one figure holds two datasets, readers need a legend to tell them apart.

```python
# Two classes, same variables
sleep_a = [6, 6.5, 7, 7.5, 8]
gpa_a = [2.8, 3.0, 3.2, 3.4, 3.6]
sleep_b = [5.5, 6, 6.5, 7, 7.5]
gpa_b = [2.2, 2.5, 2.7, 2.9, 3.1]

plt.figure()
plt.scatter(sleep_a, gpa_a, s=40, alpha=0.6, color="steelblue", label="Class A")
plt.scatter(sleep_b, gpa_b, s=40, alpha=0.6, color="indianred", label="Class B")
plt.title("Sleep vs GPA — Two Classes")
plt.xlabel("Sleep Hours (per night)")
plt.ylabel("GPA (4.0 scale)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig("two_classes.png", dpi=150, bbox_inches="tight")
plt.show()
```

Run it. Two scatter clouds, a legend in the upper right, and a file `two_classes.png` appears in your folder.

### Breaking down the new pieces

**`plt.figure()`** — creates a fresh, empty figure. Without it, the new scatter plots would draw on top of whatever was in the previous window (your bar chart or line plot). Always call `plt.figure()` when you want a clean slate.

**`label=` + `plt.legend()`** — the pair that names your datasets. Every artist (line, scatter, bar) that has a `label=` argument gets an entry in the legend. `plt.legend()` with no arguments places it automatically (usually upper right). You can control position: `plt.legend(loc="lower right")`, `plt.legend(loc="center left")`, etc.

**`plt.savefig("two_classes.png", dpi=150, bbox_inches="tight")`** — writes a PNG into your folder.

**Critical ordering:** `savefig` **must come before** `plt.show()`. `plt.show()` closes the figure and clears it — if you save after, you save a blank image. (Ask me how many times I've done that — it's not zero.)

**Check your understanding:**
- What happens if you call `plt.legend()` but forgot `label=` on your scatter calls?
- What does `bbox_inches="tight"` prevent?

---

## PART 5 — MINI-EXERCISE: YOUR OWN CHART (20 min)

Here are the first 5 rows of the study-habits dataset you will meet in the U2 L07 lab:

```
Student_ID,Study_Hours,Test_Score,Attendance,Sleep_Hours
S01,4.5,82,0.93,7.0
S02,1.0,55,0.71,5.5
S03,7.0,95,0.98,8.0
S04,3.0,74,0.88,6.5
S05,0.5,48,0.65,5.0
```

In `charts.py`, build **one chart of your choice** from this data — your pick of line, bar, or scatter, your pick of columns, your pick of colors. It must have:
- `plt.figure()` at the start
- Title that states the finding
- x-label with units
- y-label with units
- `plt.grid(True, alpha=0.3)`
- `plt.savefig("my_chart.png", dpi=150, bbox_inches="tight")` before `plt.show()`

**Suggestions if you're stuck:**
- Line: average score by student (x = student index, y = score)
- Bar: attendance category (high/low) vs average score
- Scatter: study hours vs test score (like L03 but with your styling)

**After you save it, answer in your notes:**
*Why this constraint:* A chart that takes a paragraph to explain is a failed chart. The best visualizations make their point instantly.

---

## PART 6 — TURN IN (15 min)

Add today's work to the lab repo you already have (the one from Unit 1 — `~/compmath-u1-calculator-lab`). Copy your files in, then in the terminal:

```bash
cd ~/compmath-u1-calculator-lab
git add unit2_plots/
git commit -m "L05: three chart types + custom chart"
git push
```

**Password prompt = Personal Access Token, not your GitHub password.** If you don't have a PAT yet, stop and ask — do not use your account password.

### Spot-check before you say you're done

Open `my_chart.png` and confirm it has:
- Title that states a finding (not just column names)
- x-label with units
- y-label with units
- Grid lines visible but faint
- Saved as PNG, not blank

If any check fails, fix it and `git add/commit/push` again.

---

## WHY THIS MATTERS

You now have the three foundational chart types in your toolkit:

| Chart type | Use when... | x-axis | y-axis |
|------------|-------------|--------|--------|
| Line plot | Showing change over a continuous variable (time, dose, temperature) | **Numeric** | **Numeric** |
| Bar chart | Comparing categories (groups, conditions, labels) | **Categorical** | **Numeric** |
| Scatter plot | Looking for a relationship between two numeric variables | **Numeric** | **Numeric** |

Every visualization you build this year — including the Unit 2 project (U2 L15–L18) — will use these three as building blocks. The customization skills (colors, markers, labels, legends, saving) transfer directly.

---

## NEXT

**U2 L06 — Paper Check: Charts So Far** [U2-L06-Paper-Check-Charts.md](LESSONS/U2-L06-Paper-Check-Charts.md)