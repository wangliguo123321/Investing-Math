# Teamwork Project Prompt — Draft

> Status: Launched
> Goal: Craft prompt → get user approval → delegate to teamwork_preview

并行创作《股票市场的数学原理》系列的接下来的5篇文章（EP02-EP06），分别为：
- EP02: 期望值理论 (ep02_expected_value.md)
- EP03: 大数定律 (ep03_law_of_large_numbers.md)
- EP04: 中心极限定理 (ep04_central_limit_theorem.md)
- EP05: 复利定律 (ep05_compound_interest.md)
- EP06: 均值回归 (ep06_mean_reversion.md)

Working directory: /Users/lili/.gemini/antigravity/brain/d493099f-783d-4b86-9462-011f05b21b68
Integrity mode: development

## Requirements

### R1. 严格遵循现有写作与图像规范
智能体必须完整阅读并完全遵守工作目录下的《系列文章写作规范指南》（`series_writing_guide.md`）和《图像生成提示词指南》（`series_image_prompt_guide.md`）。以 `ep01_kelly_criterion.md` 为文章质量和排版的标杆参照物。

### R2. 生成配图并嵌入
智能体不仅需要撰写上述五篇文章的Markdown文本，还需要**自己调用图像生成工具（如 generate_image）**，按照《图像生成提示词指南》中的9大模板结构，为每一篇文章生成全部所需配图（每篇约7-8张图），并将生成的图像准确嵌入到最终的文章Markdown文件中。

### R3. 运行自动化验证脚本
工作目录下已经提供了一个验证脚本 `verify_articles.py`。智能体在完成文章后，必须运行该脚本来校验文章结构（是否包含全部13个必须章节、是否有足够数量的图表、公式、字数是否达标等）。如果脚本报错，智能体需要自行根据错误提示修改文章，直至脚本输出 ALL VERIFICATIONS PASSED。

## Acceptance Criteria

### 文章结构与规范
- [ ] 工作目录下成功生成5个Markdown文件（`ep02_expected_value.md` 至 `ep06_mean_reversion.md`）。
- [ ] 每篇文章都严格包含指南规定的13个章节标题。
- [ ] 每篇文章至少有7张成功渲染的图像、8个以上的Markdown表格、3个以上的块级数学公式。

### 图像生成
- [ ] 5篇文章对应的约35-40张配图全部生成完毕，且所有图片遵循深海军蓝、金色高亮等统一个视觉规范（参照指南要求）。
- [ ] 文章中的图片链接有效，无破损图像。

### 验证通过
- [ ] 终端运行 `python3 verify_articles.py` 返回退出码 `0`，显示全绿通过。

---
*Next: when approved → delegate via invoke_subagent (see Delegation Protocol)*
