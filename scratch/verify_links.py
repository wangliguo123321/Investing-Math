import os
import glob
import re

base_dir = "/Users/lili/.gemini/antigravity/brain/d493099f-783d-4b86-9462-011f05b21b68"
os.chdir(base_dir)

all_md_files = ["README.md"] + glob.glob("episodes/*.md") + glob.glob("docs/*.md")

error_count = 0

for md_file in all_md_files:
    if not os.path.exists(md_file):
        continue
        
    file_dir = os.path.dirname(md_file)
    
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Match images: ![alt](path)
    # Match links: [text](path)
    
    # We want to match paths that don't start with http
    img_pattern = re.compile(r'!\[.*?\]\((?!http)(.*?)\)')
    link_pattern = re.compile(r'\[.*?\]\((?!http)(.*?)\)')
    
    for match in img_pattern.finditer(content):
        path = match.group(1)
        # remove fragments if any
        path = path.split('#')[0]
        
        full_path = os.path.normpath(os.path.join(file_dir, path))
        if not os.path.exists(full_path):
            print(f"BROKEN IMAGE in {md_file}: {path} -> {full_path}")
            error_count += 1
            
    for match in link_pattern.finditer(content):
        path = match.group(1)
        # ignore anchors
        if path.startswith("#"):
            continue
        path = path.split('#')[0]
        
        # ignore empty
        if not path:
            continue
            
        full_path = os.path.normpath(os.path.join(file_dir, path))
        if not os.path.exists(full_path):
            print(f"BROKEN LINK in {md_file}: {path} -> {full_path}")
            error_count += 1

if error_count == 0:
    print("ALL LINKS AND IMAGES ARE VALID!")
else:
    print(f"Found {error_count} broken links/images.")
