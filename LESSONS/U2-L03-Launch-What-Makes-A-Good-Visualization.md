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
