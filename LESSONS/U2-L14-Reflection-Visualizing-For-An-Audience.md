# U2 L14 — Reflection: Visualizing For An Audience

**LO:** match chart type, detail level, and language to the audience; defend your design choices.

**Estimated time:** 70 minutes.

---

## PART 1 — THE SAME DATA, THREE AUDIENCES (15 min)

You have a cleaned dataset: 60 days of campus threat data. Here is a 3-row excerpt from `u2_campus_threat_clean.csv`:

```
date,phishing_reports,failed_logins,login_success_rate,malware_blocks,vpn_connections,wifi_devices
2026-01-01,12,45,0.992,3,156,2041
2026-01-02,8,38,0.994,2,142,1987
2026-01-03,15,52,0.990,4,168,2103
```

Your task: **design one chart** that answers the same question — *"Are threat levels stable or rising?"* — for three different audiences:

| Audience | What they need | What they don't need |
|----------|----------------|---------------------|
| **Security Team** (analysts who act on spikes) | Exact daily values, spike thresholds, day-of-week patterns | Fancy colors, executive summary, oversimplification |
| **Principal** (leader who allocates budget) | Trend over time, 1–2 key numbers, plain English takeaway | Daily noise, technical jargon, 15 chart types |
| **Parents at Open House** (community, not tech) | "Safe or not?" — one visual verdict, no numbers required | Any axis label with "phishing" or "login", statistical language |

In your notes, for each audience write:
- **Chart type** (line, bar, histogram, single number + icon, etc.)
- **Which column(s)** you plot
- **One label or title word** you would **use** and one you would **avoid**

---

## PART 2 — CODE-ALONG: BUILD THE THREE VERSIONS (30 min)

Open your lab repo (the viz-basics repo for this one):

```bash
cd ~/compmath-u2-viz-basics
git pull
```

Create `audience_charts.py` and build all three. You will need the clean threat data — it's in the data-lab repo, but copy it here or read from the path:

```python
import csv
from datetime import datetime
import matplotlib.pyplot as plt

# Load from data-lab repo
with open("../compmath-u2-data-lab/data/u2_campus_threat_clean.csv", newline="") as f:
    rows = list(csv.DictReader(f))

dates = [datetime.strptime(r["date"], "%Y-%m-%d").date() for r in rows]
phishing = [int(r["phishing_reports"]) for r in rows]
failed = [int(r["failed_logins"]) for r in rows]
success = [float(r["login_success_rate"]) for r in rows]
```

### Version A — Security Team (Line Plot, Full Detail)

```python
plt.figure(figsize=(10, 5))
plt.plot(dates, phishing, marker="o", label="Phishing Reports", color="steelblue")
plt.plot(dates, failed, marker="s", label="Failed Logins", color="indianred")
plt.axhline(y=20, color="gray", linestyle="--", alpha=0.5, label="Investigation Threshold (20/day)")
plt.title("Daily Threat Metrics — 60-Day Window (for Security Operations)")
plt.xlabel("Date")
plt.ylabel("Count per Day")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("chart_security.png", dpi=150)
plt.show()
```

### Version B — Principal (Bar Chart, Weekly Aggregation)

```python
# Aggregate to weekly
from collections import defaultdict
weekly_phish = defaultdict(int)
weekly_failed = defaultdict(int)
for d, p, f in zip(dates, phishing, failed):
    week = d.isocalendar()[1]  # ISO week number
    weekly_phish[week] += p
    weekly_failed[week] += f

weeks = sorted(weekly_phish.keys())
avg_phish = [weekly_phish[w] / 7 for w in weeks]
avg_failed = [weekly_failed[w] / 7 for w in weeks]

plt.figure(figsize=(8, 4))
plt.bar([w - 0.2 for w in weeks], avg_phish, width=0.4, label="Avg Phishing/Day", color="steelblue")
plt.bar([w + 0.2 for w in weeks], avg_failed, width=0.4, label="Avg Failed Logins/Day", color="indianred")
plt.title("Weekly Average Threat Activity — 9-Week Trend")
plt.xlabel("Week of Year")
plt.ylabel("Average Daily Count")
plt.legend()
plt.grid(True, alpha=0.3, axis="y")
plt.tight_layout()
plt.savefig("chart_principal.png", dpi=150)
plt.show()
```

### Version C — Parents (Single Metric, Traffic Light)

```python
# Use login success rate — high = good, low = bad
avg_success = sum(success) / len(success) * 100  # percentage

plt.figure(figsize=(4, 4))
# Traffic light: green/yellow/red based on threshold
if avg_success >= 99.5:
    color, verdict = "seagreen", "Strong"
elif avg_success >= 99.0:
    color, verdict = "goldenrod", "Acceptable"
else:
    color, verdict = "indianred", "Needs Attention"

plt.pie([avg_success, 100 - avg_success], colors=[color, "lightgray"], startangle=90,
        wedgeprops={"edgecolor": "white", "linewidth": 2})
plt.title(f"Login Security: {verdict}\n{avg_success:.1f}% Success Rate")
plt.tight_layout()
plt.savefig("chart_parents.png", dpi=150)
plt.show()
```

**Open all three PNGs.** Ask yourself: does each one *actually* give its audience what they need?

---

## PART 3 — THE AUDIENCE CHECKLIST (15 min)

For **your own chart** (pick the one you're most unsure about), answer this checklist in your notes:

| Question | Your Answer |
|----------|-------------|
| 1. Who is the exact audience? | |
| 2. What is the **one thing** they should notice? | |
| 3. What jargon did you remove? | |
| 4. What jargon did you keep, and why? | |
| 5. Does the y-axis start at zero? (If bar chart) | |
| 6. Is the legend inside the plot area, obscuring data? | |
| 7. If you printed this in black & white, would it still work? | |
| 8. What is the honest limitation you would tell them? | |

**The honest limitation** is the sentence that tells your reader you understood your own data. For Version A: "Threshold is arbitrary — set by policy, not by data." For Version C: "This hides the 15 days below 99%."

---

## PART 4 — JOURNAL + PUSH (10 min)

In your viz-basics repo:

```bash
cd ~/compmath-u2-viz-basics
code journal-$(whoami).md
```

Answer in 3–4 sentences:
- Which audience forced the biggest change in your chart, and why?
- What is one design rule you will apply to **every** chart you make from now on?

```bash
git add audience_charts.py chart_*.png journal-$(whoami).md
git commit -m "L14: three audience charts + reflection"
git push
```

---

## TURN IN — SCREENSHOT (due 23:59 tonight)

One screenshot showing:

```
ls -lh chart_*.png
git push
```

Submit the screenshot to the U2 L14 assignment on Google Classroom.

---

## WHY THIS MATTERS

**A chart is not a picture of data — it is an argument for an audience.** The same data demands different charts for different people. The security team needs precision; the principal needs a trend; the parents need reassurance. If you show the security team's line plot to parents, you confuse them. If you show the traffic light to the security team, you insult them.

This lesson is the bridge to the Unit 2 project (U2 L15–L18), where you will build three charts for three audiences *and defend every choice in writing*.

---

## NEXT

**U2 L15 — Project Launch: Visualizing Threats** [U2-L15-Project-Launch-Visualizing-Threats.md](../compmath-u2-data-lab/LESSONS/U2-L15-Project-Launch-Visualizing-Threats.md)

*(Note: U2 L15–L18 use the data-lab repo. Your project charts will live there, but the audience-design discipline from today applies directly.)*