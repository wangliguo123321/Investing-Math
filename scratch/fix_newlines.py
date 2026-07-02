import os
import glob

base_dir = "/Users/lili/.gemini/antigravity/brain/d493099f-783d-4b86-9462-011f05b21b68"
md_files = glob.glob(os.path.join(base_dir, "ep*.md"))

for filepath in md_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace the literal \n with actual newlines around the image
    if "\\n![" in content or "]\\n" in content:
        content = content.replace("\\n![实战场景应用图]", "\n\n![实战场景应用图]")
        content = content.replace(".jpg)\\n", ".jpg)\n\n")

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed {os.path.basename(filepath)}")
    else:
        print(f"No literal \\n found in {os.path.basename(filepath)}")

print("Fix completed.")
