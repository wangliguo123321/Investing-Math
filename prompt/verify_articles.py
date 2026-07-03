#!/usr/bin/env python3
import os
import re
import sys

# The 5 expected files
expected_files = [
    "ep02_expected_value.md",
    "ep03_law_of_large_numbers.md",
    "ep04_central_limit_theorem.md",
    "ep05_compound_interest.md",
    "ep06_mean_reversion.md"
]

# The required 13 headings (exact or regex pattern)
required_headings = [
    r"^## 📖 引言",
    r"^## 一、起源",
    r"^## 二、核心公式",
    r"^## 三、四大类比",
    r"^## 四、实战全流程",
    r"^## 五、著名使用者",
    r"^## 六、长期",
    r"^## 七、六大实战使用场景",
    r"^## 八、常见错误与误区",
    r"^## 九、.*局限性",
    r"^## 十、实战SOP",
    r"^## .*本篇总结",
    r"^## 🔗 系列导航"
]

def verify_file(filepath):
    print(f"Verifying {filepath}...")
    if not os.path.exists(filepath):
        print(f"❌ ERROR: File {filepath} does not exist.")
        return False

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        lines = content.split('\n')

    passed = True

    # 1. Check headings
    for pattern in required_headings:
        if not re.search(pattern, content, re.MULTILINE):
            print(f"  ❌ Missing required heading matching: {pattern}")
            passed = False

    # 2. Check image count (at least 7)
    image_count = len(re.findall(r'!\[.*?\]\(.*?\)', content))
    if image_count < 7:
        print(f"  ❌ Not enough images. Found {image_count}, required 7.")
        passed = False
    else:
        print(f"  ✅ Images: {image_count}")

    # 3. Check table count (at least 8 markdown tables)
    # A markdown table row usually has multiple pipes. We can count the number of lines containing "|---|".
    table_count = len(re.findall(r'\|.*---.*\|', content))
    if table_count < 8:
        print(f"  ❌ Not enough tables. Found {table_count}, required 8.")
        passed = False
    else:
        print(f"  ✅ Tables: {table_count}")

    # 4. Check formula count (at least 3 block formulas)
    formula_count = len(re.findall(r'\$\$.*?\$\$', content, re.DOTALL))
    if formula_count < 3:
        print(f"  ❌ Not enough block formulas. Found {formula_count}, required 3.")
        passed = False
    else:
        print(f"  ✅ Formulas: {formula_count}")

    # 5. Check total length (simple character count as proxy for word count)
    if len(content) < 3000:
        print(f"  ❌ Article seems too short ({len(content)} characters).")
        passed = False
    else:
        print(f"  ✅ Length: {len(content)} characters")

    if passed:
        print(f"✅ {filepath} passed all programmatic checks.\n")
    else:
        print(f"❌ {filepath} failed verification.\n")
    return passed

def main():
    print("Starting article verification...\n")
    all_passed = True
    for f in expected_files:
        if not verify_file(f):
            all_passed = False
    
    if all_passed:
        print("\n🎉 ALL VERIFICATIONS PASSED! The articles meet the structural requirements.")
        sys.exit(0)
    else:
        print("\n💥 VERIFICATION FAILED. Please fix the above errors and re-run.")
        sys.exit(1)

if __name__ == "__main__":
    main()
