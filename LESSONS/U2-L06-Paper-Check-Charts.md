# U2 L06 — Paper Check: Charts So Far

**LO:** demonstrate, on paper, mastery of good-visualization criteria and matplotlib customization from U2 L03–L05.

**Estimated time:** 70 minutes.

---

## WHY A PAPER CHECK?

You might wonder: *why not just code this?* Because writing code and explaining concepts use different parts of your brain. Coding lets you iterate; paper forces you to hold the mental model without the computer's feedback. If you can't articulate the rule on paper, you don't own it yet — and U2 L07 will expose that gap immediately.

The corrections are the point. A corrected miss is worth more than a lucky guess.

---

## PART 1 — THE CHECK (25 min, closed notes)

Answer on the check sheet. One point each unless marked. **Show your reasoning** — not just the answer.

### Section A — Which chart? (from U2 L03 and U2 L05)

**Q1.** You want to show how one value changes as another increases, day by day. Which chart type, and why?

**What a complete answer includes:** The chart type (line plot) + the reason (x-axis is continuous/ordered, y-axis is numeric, we care about the *trend* across the ordered domain).

**Q2.** You want to compare an average score across three sleep groups. Which chart type?

**What a complete answer includes:** Bar chart + the reason (x-axis is categorical — groups have no inherent numeric order — and y-axis is numeric).

**Q3.** You want to see whether two number columns are related. Which chart type?

**What a complete answer includes:** Scatter plot + the reason (both axes numeric, no implied order/continuity, we're looking for association not trend).

**Why this distinction matters:** Choosing the wrong chart type is the #1 visualization error. A line plot on categorical data implies a connection that doesn't exist. A bar chart on continuous data loses the ordering. A scatter on time-series data hides the temporal sequence.

### Section B — The label rule. (from U2 L05)

**Q4.** Write the rule from L05 about what every plot must have — all three parts.

**Expected answer:** Every plot must have (1) a title that states the question, (2) an x-label with units, (3) a y-label with units.

**Q5.** A chart has a title and an x-label but no y-label. What can a reader not tell from it?

**Expected answer:** What the vertical axis measures — the *units* and *meaning* of the numbers. Without it, the chart is ambiguous (is that GPA? dollars? temperature?).

### Section C — Predict the output. (from U2 L05)

**Q6.** What does `plt.grid(True, alpha=0.3)` do to the grid lines?

**What a complete answer includes:** Turns grid on; `alpha=0.3` makes lines 30% opaque (faint gray) so they guide the eye without competing with data.

**Q7.** In `plt.scatter(hours, gpa, s=40)`, what does `s=40` control?

**Expected answer:** Marker size (area in points²). Default is 20. Larger = easier to see when points overlap; smaller = better for dense data.

**Q8.** You call `plt.savefig("c.png")` *after* `plt.show()`. What is wrong with the saved file, and what is the correct order?

**Expected answer:** The saved file is blank/empty. `plt.show()` closes and clears the figure. Correct order: `plt.savefig(...)` then `plt.show()`.

### Section D — One fix-it. (2 points)

**Q9.** This code has two bugs. Name both:

```python
import matplotlib.pyplot as plt
plt.scatter([1,2,3], [10,20,30])
plt.legend()
plt.savefig("chart.png")
```

**Bug 1:** `plt.legend()` is called but no artist was given a `label=` argument — the legend will be empty (or show "0 artists with labels").

**Bug 2:** No `plt.ylabel(...)` — the vertical axis has no name or units.

**Bonus catch:** `plt.savefig()` before `plt.legend()` means the saved image won't have the legend either (though the legend would be empty anyway).

---

## PART 2 — SWAP AND GRADE (15 min)

Trade papers with your partner. Using the key I project, mark each answer and write the score at the top. **Both names go on the paper you graded.**

---

## PART 3 — CORRECTIONS (20 min)

Take your own paper back. Correct every miss **in a different color**, and for each miss write one line:

**What I had in my head** vs **what is true**

*Example:*
- What I had in my head: "legend() just shows the colors automatically."
- What is true: `legend()` only shows entries that were given a `label=` when plotted.

**Why this format:** Naming the misconception explicitly helps you not repeat it. "I forgot" doesn't teach you — "I thought X but actually Y" does.

---

## PART 4 — WHAT THE CHECK TELLS US (10 min, class discussion)

Hands up by section: which section was hardest? We re-teach the top one on the board before the U2 L07 lab, using *your actual wrong answers* — that is what the check is for.

**Common patterns from past years:**
- `savefig` after `show` → blank file
- `legend()` without `label=` → empty legend
- Missing y-label → chart is ambiguous

---

## PART 5 — LOOK AHEAD: THE U2 L07 LAB (15 min, in pairs)

Next lesson (U2 L07) you get your own data-lab repo and build bar charts of categorical data. In your notes:

**Q1.** What is a *categorical* column, versus a *numerical* one? Name one of each from the study-habits preview you saw in U2 L05 (students, study, scores, sleep).

**Categorical:** labels/groups (e.g., `students` — "S01", "S02" are IDs, not quantities).
**Numerical:** quantities you can do math on (e.g., `study` hours, `scores` points, `sleep` hours).

**Q2.** Predict: which column from that preview would make the most useful bar chart, and which could a bar chart not show at all? Why?

**Most useful bar chart:** `students` on x, `scores` on y — compares five students' scores directly.
**Bar chart cannot show:** `study` vs `scores` as a relationship — that needs a scatter (both numeric). A bar chart with `study` on x would treat 2.0, 4.5, 6.5, 9.0, 12.0 as five *separate categories*, losing the fact that 9.0 > 6.5 > 4.5...

---

## TURN IN — PAPER (collected at the end of class)

One check sheet with both names. Hand it in before you leave.

**Also:** Submit a photo of the corrected check sheet to the U2 L06 assignment on Google Classroom by 23:59 tonight.

**Keep the sheet** — it is your study guide for the Unit 2 assessment (U2 L19).

---

## WHY THIS MATTERS

This check covers the *vocabulary of visualization*:

`alpha`, `s`, `label`, `legend`, `savefig`, `show`, `figure`, `grid`

Every lab from here on (U2 L07, U2 L08, U2 L10, U2 L13, and the Unit 2 project U2 L15–L18) assumes you have these fluent. If today revealed gaps, revisit U2 L03–L05 before U2 L07.

---

## NEXT

**U2 L07 — LAB: Bar Charts and Categorical Data** [U2-L07-Lab-Bar-Charts-And-Categorical-Data.md](LESSONS/U2-L07-Lab-Bar-Charts-And-Categorical-Data.md)