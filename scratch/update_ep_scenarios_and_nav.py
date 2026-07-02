import os
import re

base_dir = "/Users/lili/.gemini/antigravity/brain/d493099f-783d-4b86-9462-011f05b21b68"

# Maps EP number to the generated image file or placeholder
ep_images = {
    "01": "ep01_scenarios_1782992116626.jpg",
    "02": "ep02_scenarios_1782992127648.jpg",
    "03": "ep03_scenarios_1782992138814.jpg",
    "04": "ep04_scenarios_1782992153366.jpg",
    "05": "ep05_scenarios_1782992185166.jpg",
    "06": "ep06_scenarios_1782992195219.jpg",
    "07": "ep07_scenarios_1782992206397.jpg",
    "08": "ep08_scenarios_1782992235067.jpg",
    "09": "ep09_scenarios_placeholder.jpg",
    "10": "ep10_scenarios_placeholder.jpg"
}

ep_files = {
    "01": "ep01_kelly_criterion.md",
    "02": "ep02_expected_value.md",
    "03": "ep03_law_of_large_numbers.md",
    "04": "ep04_central_limit_theorem.md",
    "05": "ep05_compound_interest.md",
    "06": "ep06_mean_reversion.md",
    "07": "ep07_momentum_effect.md",
    "08": "ep08_bayesian_inference.md",
    "09": "ep09_margin_of_safety.md",
    "10": "ep10_factor_investing.md"
}

nav_table = """> 📌 **本系列目前已更新至第十篇，完整导航如下。后续篇章将在完成后补全。**

### 已发布文章目录（EP01-EP10）

| 篇号 | 主题 | 核心原理/公式 |
|------|------|-------------|
| EP01 | 凯利公式 | $f = (bp - q) / b$ |
| EP02 | 期望值 | $EV = \sum (P_i \\times V_i)$ |
| EP03 | 大数定律 | 样本均值趋近于总体期望 |
| EP04 | 中心极限定理 | 收益率叠加趋近正态分布 |
| EP05 | 复利的魔法 | $A = P(1+r)^n$ |
| EP06 | 均值回归 | 价格终将向均值靠拢 |
| EP07 | 动量效应 | 强者恒强，弱者恒弱 |
| EP08 | 贝叶斯推断 | $P(A|B) = \\frac{P(B|A)P(A)}{P(B)}$ |
| EP09 | 安全边际 | $MoS = (V-P)/V$ |
| EP10 | 因子投资 | Fama-French多因子模型 |
"""

def process_file(ep_num):
    filepath = os.path.join(base_dir, ep_files[ep_num])
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Insert image right after "## 七、xxxx"
    # Find the header
    pattern_7 = re.compile(r'^(## 七、.*?)$', re.MULTILINE)
    match = pattern_7.search(content)
    if match:
        header_7 = match.group(1)
        img_filename = ep_images[ep_num]
        if "placeholder" in img_filename:
            img_path = f"./{img_filename}"
        else:
            img_path = os.path.join(base_dir, img_filename)
        
        img_md = f"\\n![实战场景应用图]({img_path})\\n"
        
        # Check if we already inserted it
        if "![实战场景应用图]" not in content:
            content = content.replace(header_7, header_7 + img_md, 1)

    # 2. Update navigation
    # We find "## 🔗 系列导航\n\n" and what follows, until "---"
    pattern_nav = re.compile(r'(## 🔗 系列导航\s*\n)(.*?)(\n- \*\*← 上一篇：)', re.DOTALL)
    
    match_nav = pattern_nav.search(content)
    if match_nav:
        content = content[:match_nav.start(2)] + nav_table + "\n" + content[match_nav.start(3):]
    else:
        # Fallback if structure is slightly different
        print(f"Could not find exact nav structure in EP{ep_num}, trying alternative regex")
        # Try to find just the heading and the "<- 上一篇"
        alt_pattern = re.compile(r'(## 🔗 系列导航\s*\n).*?(?=- \*\*← 上一篇：)', re.DOTALL)
        if alt_pattern.search(content):
             content = alt_pattern.sub(r'\1' + nav_table + '\n', content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated EP{ep_num}")

for i in range(1, 11):
    ep = f"{i:02d}"
    process_file(ep)

print("All updates finished.")
