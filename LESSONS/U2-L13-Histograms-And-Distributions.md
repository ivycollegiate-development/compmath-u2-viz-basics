# U2 L13 — Histograms and Distributions

**LO:** create histograms to understand data distributions — shape, spread, center, skew; choose bin count deliberately.

**Estimated time:** 85 minutes.

---

## PART 0 — SETUP: START FROM CLEAN DATA (15 min)

The U2 L11 `clean_data.py` produced a cleaned CSV. Use it — that is what it was for:

```bash
cd ~/compmath-u2-data-lab
git pull
# rerun if the _clean file is missing
python3 clean_data.py
```

Create a new script `histograms.py` in VS Code and run it as you build it:

```bash
code histograms.py
```

Put each snippet below into `histograms.py`, save, and run it with:

```bash
python3 histograms.py
```

Start with the cleaned data:

```python
import csv
import matplotlib.pyplot as plt

with open("data/u2_student_performance_clean.csv", newline="") as f:
    rows = list(csv.DictReader(f))

print(len(rows))  # rows in — write this number in your notes
```

**Write the row count in your notes and compare it to the original 1,000.** Cleaning was not free — this chart sits on fewer students. The provenance statement you wrote in U2 L12 Part 5 should match this number.

**Why `newline=""` again:** Same reason as always — prevents line-ending bugs on Windows; harmless on Linux/macOS but makes your code portable.

---

## PART 1 — CODE-ALONG: YOUR FIRST HISTOGRAM (20 min)

A histogram buckets a single column and counts how many values fall in each bucket:

```python
math = [float(r["Math Score"]) for r in rows]

plt.figure()
plt.hist(math, bins=20, color="steelblue", edgecolor="white")
plt.title("Distribution of Math Scores")
plt.xlabel("Math Score")
plt.ylabel("Number of Students")
plt.savefig("hist_math_bins20.png", dpi=150)
plt.show()
```

**Open `hist_math_bins20.png`.** Each bar is a bucket; its height is the count of students in that range.

**In your notes, answer before we discuss:**
1. Where is the tallest bar? That is roughly the **center** of the data.
2. How wide is the range of non-tiny bars? That is the **spread**.
3. Does the cloud of bars lean left, lean right, or sit even? That is the **skew**.

**What `bins=20` does:** Divides the data range (min to max) into 20 equal-width intervals. Each student falls into exactly one bin. The bar height = count of students in that bin.

**Why `edgecolor="white"`:** With 20 bins, bars touch. White edges separate them visually so you can see where one bin ends and the next begins.

---

## PART 2 — BINS ARE A CHOICE, NOT A SETTING (15 min)

Same data, three different bin counts. Run each and save all three:

```python
for b in [5, 20, 100]:
    plt.figure()
    plt.hist(math, bins=b, color="steelblue", edgecolor="white")
    plt.title(f"Math Scores — {b} bins")
    plt.xlabel("Math Score")
    plt.ylabel("Number of Students")
    plt.savefig(f"hist_math_bins{b}.png", dpi=150)
    plt.clf()  # CLEAR BETWEEN PLOTS
```

**Compare the three images side by side. Write in your notes:**

| Bin count | What you see | When it's useful |
|-----------|--------------|------------------|
| **5 bins** | Big blocks, easy summary, details hidden | Executive summary, very rough shape |
| **20 bins** | The shape is readable — usually the sweet spot | Standard exploration, showing skew/modes |
| **100 bins** | Spiky noise; single students make single bars | Almost never useful — overfits the sample |

**There is no "correct" bin count.** The rule: **Pick the smallest bin count that still shows the shape you care about.** Note your bin choice next to every histogram you ever share.

**Why this matters:** A histogram with 5 bins can hide bimodality (two peaks). A histogram with 100 bins creates phantom peaks from sampling noise. The *same data* tells different stories depending on bin choice — that's a choice *you* make, not a setting the computer picks.

---
