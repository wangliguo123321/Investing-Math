import os
import glob
import re

base_dir = "/Users/lili/.gemini/antigravity/brain/d493099f-783d-4b86-9462-011f05b21b68"
ep_dir = os.path.join(base_dir, "episodes")

for filepath in glob.glob(os.path.join(ep_dir, "*.md")):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # We want to replace `[上一篇名（xxxx.md）]` with `[上一篇名]`
    # Pattern: `\[(.*?)（.*?\.md）\]`
    new_content = re.sub(r'\[(.*?)（.*?(?:\.md|README).*?）\]', r'[\1]', content)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Cleaned up links in {os.path.basename(filepath)}")

# Also fix EP01 manually
ep01_path = os.path.join(ep_dir, "第01篇_凯利公式_仓位管理的黄金法则.md")
if os.path.exists(ep01_path):
    with open(ep01_path, 'r', encoding='utf-8') as f:
        content = f.read()
    content = content.replace("- **← 系列目录** | **→ 第02篇：期望值理论**", "- **← [系列目录](../README.md)** | **→ [第02篇：期望值理论](./第02篇_期望值理论_所有决策的基石.md)**")
    with open(ep01_path, 'w', encoding='utf-8') as f:
        f.write(content)
