# U2 L01 — Unit 1 Assessment and Reflection

**LO:** demonstrate mastery of Unit 1: types, arithmetic, input validation, error handling, and the security lens.

Today is a **paper assessment day**. The written part is closed-computer — no terminals, no notes, no neighbors. Everything on this paper is something we built or debugged together in Unit 1. After the assessment, you reflect in your journal and push it.

---

## PART 1 — BEFORE YOU START (5 min)

Put everything away except a pen or pencil. On the cover of your paper, write:
- Your name
- One thing you feel confident about from Unit 1
- One thing you hope is NOT on the test

Then close your notes. Deep breath. You have seen every problem type below.

---

## PART 2 — WRITTEN ASSESSMENT (35 min, no computers)

The exam is a standalone paper:
[`Unit 1 - Working with Numbers/Assessments/Unit-1-Assessment.md`](https://github.com/ivycollegiate-development/computational-mathematics-2026-2027/blob/main/Unit%201%20-%20Working%20with%20Numbers/Assessments/Unit-1-Assessment.md)

**Print it double-sided before class.** 50 points, 35 minutes, pen and paper.

| Section | Points | Covers |
|---------|--------|--------|
| A — Short Response | 20 | 10 questions: `/` vs `//`, `input()` conversion, `ValueError`, quiet vs crash, truth table, `Fraction` vs `float`, modulo, precision order, `get_number()`, security lens |
| B — Code Reading | 10 | Problem 11 (the price loop), Problem 12 (the broken `f_to_c`) |
| C — Boundaries | 10 | −273.15 °C / 0 K guard, the `10**15` ceiling and why it exists |
| D — Write Code | 10 | `get_int(prompt)` — validate, re-ask, refuse out of range |

Do not deviate from the printed paper. The coversheet on the front carries your name, your confident item, and the "one thing I hope is NOT on the test" note from Part 1.

---

## PART 3 — HAND BACK THE COMPUTERS: GRADE RELEASE WALKTHROUGH (10 min)

We go over the answer key together, problem by problem. As we do:
- Mark your own paper
- For each miss, write one sentence: **what I thought** vs **what is true**

These sentences are raw material for your journal in Part 4.

---

## PART 4 — JOURNAL (last 10 min)

Open your lab repo and create today's journal:

```bash
cd ~/compmath-u1-calculator-lab
code journal-$(whoami).md
```

Answer in the file, 3-5 sentences each:
- What was the hardest section for you, and why?
- What is one misconception you caught yourself having during the walkthrough?

---

## PART 5 — PUSH (last 5 min — same loop, now routine)

```bash
git add journal-$(whoami).md
git commit -m "L01: Unit 1 assessment reflection"
git push
```

---

## TURN IN — PHOTO + SCREENSHOT (due 23:59 tonight)

- Photo of your completed assessment paper (coversheet + all pages)
- Screenshot of `git push`

Submit both to this assignment on Google Classroom.
Keep the terminal open — spot-checks.

---

## NEXT

**U2 L02 — Bridge: From Numbers to Data** [U2-L02-Bridge-From-Numbers-To-Data.md](LESSONS/U2-L02-Bridge-From-Numbers-To-Data.md)