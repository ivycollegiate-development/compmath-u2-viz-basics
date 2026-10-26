# U2 L19 — Reflection: Unit 2 Wrap — What Makes A Secure Visualization?

**LO:** synthesize Unit 2 vocabulary (chart types, cleaning rules, audience design, honesty audit) into a coherent mental model; identify what you still need to practice.

**Estimated time:** 70 minutes.

---

## PART 1 — VOCABULARY RECALL (15 min, closed notes)

On the paper check sheet, define or give one example of each term. One sentence each.

| Term | Your definition / example |
|------|---------------------------|
| `csv.DictReader` | |
| Comment-line trap (U2 L02, U2 L08) | |
| `float("")` crash | |
| `try/except` around `float()` | |
| `plt.figure()` purpose | |
| `alpha=0.3` on grid | |
| Line plot vs Scatter plot vs Bar chart (when to use each) | |
| y-axis must start at 0 (which chart type?) | |
| `savefig` before `show` — why? | |
| `legend()` without `label=` | |
| `bins=` choice in histogram | |
| Right-skewed vs Left-skewed | |
| Provenance statement | |
| Cleaning audit trail | |
| Audience checklist (one item) | |

**Score yourself:** count how many you answered without looking. That number is your baseline for the wrap.

---

## PART 2 — THREE CHARTS, ONE DATASET (20 min)

Using the study-habits data you know well, sketch (pencil, rough) what each of these *would* look like — no code, just the sketch + labels.

**Chart A — Line Plot:** Average Test Score by Study Hours (group study hours into 5 bins: 0–2, 2–4, 4–6, 6–8, 8+)
**Chart B — Scatter Plot:** Study Hours vs Test Score (all 52 points)
**Chart C — Bar Chart:** Average Test Score by Sleep Category (Low < 6h, Mid 6–8h, High > 8h)

For each sketch, write:
1. x-label with units
2. y-label with units
3. Title that states the finding
4. One audience this chart is *for*

---

## PART 3 — THE HONESTY AUDIT: YOUR PROJECT (20 min)

Pull up your Unit 2 project (from the data-lab repo). In your notes, for **each of your three project charts**, answer:

| Audit Question | Chart 1 (Timeline) | Chart 2 (Weekday/Weekend) | Chart 3 (Histogram) |
|----------------|-------------------|---------------------------|---------------------|
| Does the y-axis start at 0? (If bar) | | | N/A |
| If y-axis ≠ 0, did I explain why in `analysis.md`? | | | |
| What rows did cleaning drop, and would they change the story? | | | |
| What data did I *choose not to plot* that a careful reader would ask about? | | | |
| What is my "honest limitation" sentence? | | | |

**The honesty audit is not a criticism — it is the discipline.** A chart without an honest limitation is a claim of completeness that no real dataset has.

---

## PART 4 — WHAT YOU STILL NEED (15 min, in pairs)

With your partner, compare your Part 1 scores and Part 3 answers. Write two things in your notes:

**My strongest U2 skill:** ________________________________________
**My weakest U2 skill — I will re-watch L__ / re-read the lesson / practice this week:** ________________________________________

Be specific: "I need to practice `plt.legend()` positioning" is better than "charts."

---

## PART 5 — JOURNAL + PUSH (last 10 min)

In your viz-basics repo:

```bash
cd ~/compmath-u2-viz-basics
code journal-$(whoami).md
```

Answer in 4–5 sentences:
- What is the one idea from Unit 2 that you will use in *any* future data work, even if you never touch matplotlib again?
- What is the difference between a chart that is *unclear* and one that is *dishonest*?

```bash
git add journal-$(whoami).md
git commit -m "L19: unit 2 wrap reflection"
git push
```

---

## TURN IN — PAPER + SCREENSHOT (due 23:59 tonight)

- Hand in the paper check sheet (both names on it).
- Submit a photo of the completed check sheet + a screenshot of `git push` to the U2 L19 assignment on Google Classroom.

**Keep the terminal open** — spot-checks happen.

---

## WHY THIS MATTERS

**Unit 2 taught you a vocabulary, not just tools.** The words — provenance, cleaning audit, chart-type matching, audience checklist, honesty audit — are the concepts you carry into Unit 3 (Data Modeling), AP Cybersecurity (threat visualization), and any data-adjacent role.

**The vocabulary is fluency, not memorization.** If you can say "right-skewed" and see the long tail in your head, you own it. If you have to look it up, you don't — yet.

**The project is your evidence.** The three charts in your data-lab repo, with their `analysis.md` honest limitations, are the portfolio piece that proves you can build an argument with evidence. Keep that repo clean; you will reference it in college applications and interviews.

---

## NEXT

**Unit 3 — Data Modeling** (starts after the Unit 2 assessment week). We move from *describing* data to *modeling* it — regression, prediction, and the security lens on model trust.