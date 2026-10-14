"""My first real charts from real data.

There are 2 FIX ME bugs in this file. Run self_check.py to find them,
fix them, and commit the fix.
"""
import csv
import matplotlib
matplotlib.use("Agg")   # headless: saves PNG files instead of opening windows
import matplotlib.pyplot as plt

# ---- load the study-habits data ----
rows = []
with open("data/u2_dataset1_study_habits.csv") as f:
    lines = [ln for ln in f
             if ln.strip() and not ln.startswith("#")]   # real data has comments + blanks
    for r in csv.DictReader(lines):
        rows.append({
            "study": float(r["Study_Hours"]),
            "score": float(r["Test_Score"]),
        })

# ---- chart 1: study hours vs test score ----
xs = [r["study"] for r in rows]
ys = [r["score"] for r in rows]

plt.scatter(xs, ys, color="tab:blue")
# FIX ME #1: a chart with no labels is unreadable.
# Add a title and axis labels (what would you call each axis? include units)
plt.title("Study Hours vs Test Score")
plt.xlabel("Study Hours (hours per week)")
plt.ylabel("Test Score (points)")

plt.savefig("chart_study_vs_score.png", dpi=120)
print("saved chart_study_vs_score.png")

# ---- chart 2: study-hour bands ----
# Real data range is ~12.5–35.2 hours/week.
# Bands that spread students across multiple bars:
bands = {"10-15h": 0, "15-20h": 0, "20-25h": 0, "25-30h": 0, "30-35h": 0, "35+h": 0}
for r in rows:
    if r["study"] < 15:       bands["10-15h"] += 1
    elif r["study"] < 20:     bands["15-20h"] += 1
    elif r["study"] < 25:     bands["20-25h"] += 1
    elif r["study"] < 30:     bands["25-30h"] += 1
    elif r["study"] < 35:     bands["30-35h"] += 1
    else:                     bands["35+h"] += 1

plt.figure()
plt.bar(list(bands.keys()), list(bands.values()), color="tab:orange")
# FIX ME #2: this chart should label its axes too -- and the y-axis
# here counts STUDENTS, so make that obvious. Add title + both labels.
plt.title("Number of Students by Weekly Study Hours")
plt.xlabel("Weekly Study Hours (band)")
plt.ylabel("Number of Students")

plt.savefig("chart_study_bands.png", dpi=120)
print("saved chart_study_bands.png")