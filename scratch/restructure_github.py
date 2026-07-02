import os
import re
import shutil

base_dir = "/Users/lili/.gemini/antigravity/brain/d493099f-783d-4b86-9462-011f05b21b68"
os.chdir(base_dir)

# Create dirs
dirs_to_make = ["docs", "episodes", "images/series"] + [f"images/ep{i:02d}" for i in range(1, 11)]
for d in dirs_to_make:
    os.makedirs(d, exist_ok=True)

# 1. Move and rename docs
doc_mappings = {
    "series_writing_guide.md": "writing_guide.md",
    "series_image_prompt_guide.md": "image_prompt_guide.md",
    "stock_math_principles_research.md": "stock_math_principles_research.md",
    "stock_math_principles_research_v2.md": "research_notes.md"
}

for src, dest in doc_mappings.items():
    if os.path.exists(src):
        shutil.move(src, f"docs/{dest}")

# 2. Rename series_index.md to README.md
if os.path.exists("series_index.md"):
    shutil.move("series_index.md", "README.md")

# 3. Process each episode markdown file
ep_files = [f for f in os.listdir(".") if f.startswith("ep") and f.endswith(".md")]

def clean_filename(filename):
    # Remove the timestamp _17829xxxxxx
    return re.sub(r'_\d{13,}', '', filename)

for ep_file in ep_files:
    # determine ep number
    match = re.search(r'ep(\d{2})', ep_file)
    if not match: continue
    ep_num = match.group(1)
    
    with open(ep_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all images
    # ![...](/Users/.../filename.jpg)
    img_pattern = re.compile(r'!\[.*?\]\((.*?\.jpg)\)')
    
    def replacer(m):
        full_path = m.group(1)
        filename = os.path.basename(full_path)
        
        # We need to move this image to images/epXX/clean_name.jpg
        # Only move if the source file exists in root (or if it's already a clean name, skip)
        new_filename = clean_filename(filename)
        
        # If it's the series cover or system map, put in series/
        if "series_cover" in filename or "knowledge_system_map" in filename:
            target_dir = "images/series"
            rel_path = f"../images/series/{new_filename}"
        elif "placeholder" in filename:
            # placeholders don't have files right now, just update path
            target_dir = f"images/ep{ep_num}"
            rel_path = f"../images/ep{ep_num}/{new_filename}"
        else:
            target_dir = f"images/ep{ep_num}"
            rel_path = f"../images/ep{ep_num}/{new_filename}"
            
        src_path = os.path.join(base_dir, filename)
        dest_path = os.path.join(base_dir, target_dir, new_filename)
        
        if os.path.exists(src_path):
            shutil.move(src_path, dest_path)
        elif os.path.exists(full_path) and not full_path.startswith("http"):
            # in case full_path is valid but not in base_dir? Should be in base_dir.
            try:
                shutil.move(full_path, dest_path)
            except Exception:
                pass
            
        # Also need to update the markdown text to use rel_path
        return m.group(0).replace(full_path, rel_path)

    new_content = img_pattern.sub(replacer, content)
    
    # Update links: ./epXX_xxx.md -> ./epXX_xxx.md (since they are all in episodes/ now, relative link doesn't change!)
    # But series_index.md -> ../README.md
    new_content = new_content.replace("series_index.md", "../README.md")
    
    # Write to episodes/
    with open(f"episodes/{ep_file}", 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    # Remove original from root
    os.remove(ep_file)

# 4. Update README.md (formerly series_index.md)
if os.path.exists("README.md"):
    with open("README.md", 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all images and move to series/
    def readme_replacer(m):
        full_path = m.group(1)
        filename = os.path.basename(full_path)
        new_filename = clean_filename(filename)
        
        src_path = os.path.join(base_dir, filename)
        dest_path = os.path.join(base_dir, "images/series", new_filename)
        
        if os.path.exists(src_path):
            shutil.move(src_path, dest_path)
            
        return m.group(0).replace(full_path, f"./images/series/{new_filename}")

    # README img links might be just local like ![alt](series_cover.jpg)
    content = img_pattern.sub(readme_replacer, content)
    
    # Update links to episodes: ./ep01_xxx.md -> ./episodes/ep01_xxx.md
    # Wait, the markdown might have [title](./ep01_xxx.md)
    link_pattern = re.compile(r'\]\(\./(ep\d{2}.*?\.md)\)')
    content = link_pattern.sub(r'](./episodes/\1)', content)
    
    # Update links to guides
    content = content.replace("./series_writing_guide.md", "./docs/writing_guide.md")
    content = content.replace("./series_image_prompt_guide.md", "./docs/image_prompt_guide.md")
    
    with open("README.md", 'w', encoding='utf-8') as f:
        f.write(content)

print("Restructure complete!")
