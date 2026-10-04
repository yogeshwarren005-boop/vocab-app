import os, sys
sys.stdout.reconfigure(encoding="utf-8")

c_path = r"App database\Latin roots\Cluster Action & State"
dashboards = [
    "Dashboard — scul", "Dashboard — lud", "Dashboard — nihil",
    "Dashboard — toler", "Dashboard — lax", "Dashboard — solut",
    "Dashboard — ars"
]

all_words = {}
for d in dashboards:
    d_path = os.path.join(c_path, d)
    words = [f for f in os.listdir(d_path) if f.endswith(".md") and not f.startswith("Dashboard — ") and not f.startswith("Word Triage — ")]
    all_words[d] = sorted(words)
    print(f"=== {d} ({len(words)} words) ===")
    print(", ".join(words))

print(f"\nTotal words in these 7 dashboards: {sum(len(w) for w in all_words.values())}")
