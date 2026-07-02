import os
import shutil

base_dir = "/Users/lili/.gemini/antigravity/brain/d493099f-783d-4b86-9462-011f05b21b68"
os.chdir(base_dir)

broken_moves = {
    "images/ep04/ep02_cover_design.jpg": "images/ep02/ep02_cover_design.jpg",
    "images/ep04/ep02_formula_breakdown.jpg": "images/ep02/ep02_formula_breakdown.jpg",
    "images/ep04/expected_value_analogy.jpg": "images/ep02/expected_value_analogy.jpg",
    "images/ep04/lln_formula_breakdown.jpg": "images/ep03/lln_formula_breakdown.jpg",
    "images/ep04/lln_analogy_casino.jpg": "images/ep03/lln_analogy_casino.jpg"
}

for src, dest in broken_moves.items():
    if os.path.exists(src):
        # We COPY so that if EP04 also needs them, it doesn't break EP04.
        shutil.copy(src, dest)
        print(f"Copied {src} to {dest}")

# Fix EP09 and EP10 placeholders
ep09_file = "episodes/第09篇_安全边际_价值投资的概率护城河.md"
if os.path.exists(ep09_file):
    with open(ep09_file, 'r', encoding='utf-8') as f:
        content = f.read()
    content = content.replace("ep09_scenarios_placeholder.jpg", "ep09_scenarios.jpg")
    with open(ep09_file, 'w', encoding='utf-8') as f:
        f.write(content)

ep10_file = "episodes/第10篇_因子投资_系统性超越市场的秘密.md"
if os.path.exists(ep10_file):
    with open(ep10_file, 'r', encoding='utf-8') as f:
        content = f.read()
    content = content.replace("ep10_scenarios_placeholder.jpg", "ep10_scenarios.jpg")
    with open(ep10_file, 'w', encoding='utf-8') as f:
        f.write(content)
