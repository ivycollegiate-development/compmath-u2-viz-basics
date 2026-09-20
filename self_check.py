"""Self-check for the viz-basics lab. Run: python3 self_check.py

Starts at 2 of 4 passing. Your job: make it 4 of 4, commit, push.
"""
import os, subprocess, re, tempfile, shutil

results = []

def check(name, fn):
    try:
        ok, msg = fn()
    except Exception as e:
        ok, msg = False, f"error: {e}"
    results.append((name, ok, msg))
    print(("PASS  " if ok else "FAIL  ") + name + (f"  ({msg})" if msg and not ok else ""))

def has_charts():
    missing = [p for p in ("chart_study_vs_score.png", "chart_study_bands.png")
               if not os.path.exists(p)]
    return (len(missing) == 0, "missing: " + ", ".join(missing) if missing else "")

def has_labels():
    src = open("charts.py").read()
    n_title = len(re.findall(r"plt\.title\(", src))
    n_label = len(re.findall(r"plt\.(xlabel|ylabel)\(", src))
    return (n_title >= 2 and n_label >= 3,
            f"found {n_title} titles and {n_label} axis labels; need 2 titles + 3+ labels")

def runs_clean():
    # run charts.py from a temp copy so generated PNGs do not dirty the tree
    with tempfile.TemporaryDirectory() as tmp:
        shutil.copy("charts.py", tmp)
        if os.path.isdir("data"):
            shutil.copytree("data", os.path.join(tmp, "data"))
        p = subprocess.run(["python3", os.path.join(tmp, "charts.py")],
                           capture_output=True, text=True, cwd=tmp)
    return (p.returncode == 0, p.stderr.strip()[-120:])

def committed():
    p = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
    return (p.stdout.strip() == "", "uncommitted changes -- git add/commit/push")

check("both charts exist", has_charts)
check("charts have titles + axis labels", has_labels)
check("charts.py runs without errors", runs_clean)
check("work committed", committed)

passed = sum(1 for _, ok, _ in results if ok)
print(f"\n{passed} of {len(results)} checks passing")
