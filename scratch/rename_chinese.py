import os
import glob
import urllib.parse

base_dir = "/Users/lili/.gemini/antigravity/brain/d493099f-783d-4b86-9462-011f05b21b68"

rename_map = {
    "ep01_kelly_criterion.md": "第01篇_凯利公式_仓位管理的黄金法则.md",
    "ep02_expected_value.md": "第02篇_期望值理论_所有决策的基石.md",
    "ep03_law_of_large_numbers.md": "第03篇_大数定律_时间是你最好的朋友.md",
    "ep04_central_limit_theorem.md": "第04篇_中心极限定理_分散投资的数学证明.md",
    "ep05_compound_interest.md": "第05篇_复利定律_财富的雪球效应.md",
    "ep06_mean_reversion.md": "第06篇_均值回归_市场的钟摆定律.md",
    "ep07_momentum_effect.md": "第07篇_动量效应_顺势而为的数学依据.md",
    "ep08_bayesian_inference.md": "第08篇_贝叶斯推断_实时更新你的判断.md",
    "ep09_margin_of_safety.md": "第09篇_安全边际_价值投资的概率护城河.md",
    "ep10_factor_investing.md": "第10篇_因子投资_系统性超越市场的秘密.md"
}

# 1. Gather all files that might contain these references
# This includes README.md and all files inside episodes/
files_to_update = [os.path.join(base_dir, "README.md")]
for f in glob.glob(os.path.join(base_dir, "episodes", "*.md")):
    files_to_update.append(f)

# 2. Update the text in all these files
for filepath in files_to_update:
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    original_content = content
    # Replace references. We should replace the literal filenames in the markdown links.
    for old_name, new_name in rename_map.items():
        # Markdown URLs with Chinese characters are totally fine as-is in modern github.
        # Github supports spaces and Chinese. However, spaces in names would require url encoding `%20`.
        # Since our new names use underscores `_` instead of spaces, we don't even need URL encoding!
        # `[text](./episodes/第01篇_...md)` works perfectly on Github.
        
        content = content.replace(old_name, new_name)
        
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated references in {os.path.basename(filepath)}")

# 3. Rename the actual files in episodes/ directory
for old_name, new_name in rename_map.items():
    old_path = os.path.join(base_dir, "episodes", old_name)
    new_path = os.path.join(base_dir, "episodes", new_name)
    
    if os.path.exists(old_path):
        os.rename(old_path, new_path)
        print(f"Renamed: {old_name} -> {new_name}")

print("Renaming process completed successfully!")
