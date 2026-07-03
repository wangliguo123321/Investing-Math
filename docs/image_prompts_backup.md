# 《股票市场的数学原理》系列 — 图片生成 Prompt 备忘录
## Image Generation Prompts Backup — Full Context Edition

> **使用说明**：每个 Prompt 均包含文章核心内容摘要作为上下文。
> 生成时使用 `generate_image` 工具，`AspectRatio` 统一设置为 `"16:9"`。
> 生成后将文件移动到 `images/epXX/` 目录并重命名为规范名称。

### 🎨 视觉识别系统 (VI) — 所有图片必须严格遵守

```
背景色：深海军蓝 #0d1b2a（Dark Navy Blue）
标题文字：金色渐变（Gold Gradient）
数据/公式：荧光青色（Neon Cyan #00ffff）
正向指标：翠绿色（#00ff88）
负向/风险：鲜红色（#ff4444）
强调色：橙金色（#ffa500）
字体风格：高端金融杂志，现代无衬线体
分辨率：16:9 横版，高清专业品质
风格关键词：dark mode premium, neon glow accents, cinematic lighting
```

---

## 第15篇《相关性与分散化：降低风险的数学奥秘》
**文章摘要**：马科维茨1952年证明，分散化的关键不在持有多少资产，而在资产间的相关性（ρ）有多低。公式 ρ_ij = Cov(R_i,R_j)/(σ_i·σ_j)，值从-1到+1。文章讲解了相关性矩阵构建、如何用低相关性降低组合波动率约40%、斯文森耶鲁捐赠基金案例、以及"假分散化"陷阱（10只科技股相关性高达+0.85）。

### EP15-03：雨伞类比图
**文件名**：`images/ep15/ep15_analogy_umbrella.jpg`
**Prompt**：
```
A clean educational infographic using a weather and umbrella analogy to explain asset correlation. Dark navy #0d1b2a background. Title: "相关性 = 你的资产们，会在同一时刻被同一场雨淋湿吗？" in large gold text.

Three distinct panels side by side:

LEFT PANEL — labeled "高度正相关 ρ=+1 ❌ 危险" in red:
A crowd of 10 businesspeople (representing stocks like 宁德时代、比亚迪、科技板块) all standing on the same rooftop, all getting drenched simultaneously by a heavy storm. None have umbrellas. Caption: "持有10只科技股 = 用10个盘子盛同一道雨".

MIDDLE PANEL — labeled "零相关 ρ≈0 ✅ 理想" in cyan:
Two people in completely separate locations: Person A (股票) stands in heavy rain getting wet; Person B (黄金) stands in bright sunshine. When one is hit by market storm, the other is unaffected. Caption: "A股与黄金历史相关性仅+0.08".

RIGHT PANEL — labeled "负相关 ρ=-1 🌟 完美对冲" in green:
Two people sharing one magical umbrella that automatically shifts sides — when Person A (股票) is rained on, the umbrella covers A; simultaneously Person B (国债) is in sunshine and vice versa. Perfect alternating protection. Caption: "A股与国债相关性-0.12，股跌债涨". 

Style: Clean modern educational illustration, warm gold vs cool blue color contrast, Chinese text dominant, premium financial aesthetic. Aspect ratio 16:9.
```

### EP15-04：相关性矩阵热力图
**文件名**：`images/ep15/ep15_correlation_matrix.jpg`
**Prompt**：
```
A professional financial heatmap visualization showing a 5x5 asset correlation matrix. Dark navy #0d1b2a background. Title: "主要资产类别相关性热力图（近20年历史数据）" in gold.

The 5x5 heatmap matrix with assets: 沪深300股票, 10年期国债, 黄金, 原油ETF, 标普500(QDII).

Cell color coding:
- Value +1.00 (diagonal): glowing white/silver (self-correlation)
- Values > +0.7: deep danger red (#ff2222) — "高度同向，无效分散"
- Values +0.3 to +0.7: warm orange (#ff8800) — "部分相关"  
- Values -0.3 to +0.3: cool cyan (#00ddff) — "低相关，有效分散"
- Values < -0.3: emerald green (#00cc66) — "负相关，完美对冲"

Key data to show approximately:
沪深300 vs 国债: -0.12 (green) with annotation arrow: "股债负相关=组合基石！"
沪深300 vs 黄金: +0.08 (cyan)
沪深300 vs 原油: +0.35 (orange)
沪深300 vs 标普500: +0.55 (orange) with warning: "近年相关性上升"
国债 vs 黄金: +0.15 (cyan)

Right side: A vertical color scale legend from green (-1) to red (+1).
Bottom: Caption "低相关=免费的风险降低，不用放弃任何收益".

Style: Professional Bloomberg terminal aesthetic, precise data visualization, clean grid lines. 16:9.
```

### EP15-05：著名投资者图
**文件名**：`images/ep15/ep15_masters.jpg`
**Prompt**：
```
A premium portrait collage of famous diversification masters. Dark navy #0d1b2a background. Title: "分散化的顶级实践者" in gold.

LEFT portrait: David Swensen (大卫·斯文森) — Yale Endowment Fund manager for 36 years. Text below: "耶鲁捐赠基金掌门人 · 13亿→420亿美元 · 年化13%". Show him looking wise and scholarly, with a glowing portfolio chart behind him showing the iconic Yale diversified allocation (stocks 30%, private equity 35%, real assets 20%, bonds 15%). His key insight floating in neon: "多样化是唯一免费的午餐".

RIGHT portrait: Harry Markowitz (哈里·马科维茨) — Nobel Prize winner. Text below: "现代投资组合理论之父 · 1990诺贝尔经济学奖". Show him with a glowing correlation matrix and efficient frontier curve behind him. His famous insight: "组合风险不是个别风险的相加，而是协方差关系的结果".

Center connecting element: A glowing timeline "1952 MPT诞生 → 1990 诺贝尔奖 → 2000年代 各国主权基金采用".

Style: Cinematic, dark moody lighting, premium financial aesthetic. Gold and cyan color scheme. 16:9.
```

### EP15-06：长期业绩对比图
**文件名**：`images/ep15/ep15_performance_comparison.jpg`
**Prompt**：
```
A professional financial performance comparison chart. Dark navy #0d1b2a background. Title: "低相关性组合 vs 传统组合：三次危机中的表现" in gold.

Main content: A grouped bar chart showing performance during 3 crisis events:
Crisis 1: "2008金融危机" — Bar 1 (全仓A股, red): -65.4%, Bar 2 (60股/40债, orange): -28.3%, Bar 3 (相关性优化组合, green): -14.2%
Crisis 2: "2015A股股灾" — Bar 1: -38.0%, Bar 2: -5.2%, Bar 3: -8.7%
Crisis 3: "2022通胀+加息" — Bar 1: -22.0%, Bar 2: -14.5%, Bar 3: -3.8%

Below chart: A performance metrics table showing 30-year annualized returns:
全仓A股: 8.5% return, but with horrific drawdowns
60/40组合: 6.8% return
相关性优化组合: 7.2% return with the annotation "收益接近，但危机时回撤小得多 = 投资者更容易坚持到底"

Key annotation box: "真正的优势不是在牛市赚得多，而是在熊市亏得少，让你能够坚持到复利发挥效果！"

Style: Clean financial data visualization, red/orange/green bar contrast, professional grid. 16:9.
```

### EP15-07：实战场景图
**文件名**：`images/ep15/ep15_scenarios.jpg`
**Prompt**：
```
A professional financial infographic showing 6 practical scenarios for correlation-based diversification. Dark navy #0d1b2a background. Title: "相关性分析的六大实战应用" in gold.

A 2x3 grid layout with neon-outlined cells:

Cell 1: "A股投资者的跨市场分散" — Icon: Globe with Chinese flag + US flag + gold bar. Text: "国债ETF(ρ=-0.1) + 黄金ETF(ρ=+0.1) + QDII(ρ=+0.2)".
Cell 2: "发现假分散化陷阱" — Icon: Magnifying glass revealing 10 identical fund icons all pointing same direction. Text: "下载所有基金月收益，如ρ>0.7则存在重叠".
Cell 3: "加密货币分散价值评估" — Icon: Bitcoin symbol with a sliding correlation meter from green(2018: 0.1) to red(2022: 0.65). Text: "实时监控ρ，超过0.5时需减仓".
Cell 4: "股票选股层面低相关构建" — Icon: Industry sector pie (消费+资源+公用+科技) showing cross-sector low correlation. Text: "跨行业平均ρ=0.35 vs 同行业ρ=0.75".
Cell 5: "危机时相关性监控机制" — Icon: Alert dashboard with a spiking correlation meter triggering a warning siren. Text: "60日滚动ρ升至0.6触发降仓警报".
Cell 6: "债券的久期分散" — Icon: Bond yield curve with short/medium/long duration bars. Text: "哑铃型久期结构，不同期限债券低相关".

Style: Premium dashboard UI design, neon cyan/gold outlines on dark navy, consistent Chinese text. 16:9.
```

### EP15-08：SOP流程图
**文件名**：`images/ep15/ep15_sop.jpg`
**Prompt**：
```
A clear 5-step flowchart for building a low-correlation diversified portfolio. Dark navy #0d1b2a background. Title: "相关性分析实战SOP：5步构建低相关性优质组合" in gold.

Five sequential steps connected by glowing cyan arrows, arranged in a clear left-to-right or Z-pattern flow:

Step 1 (gold neon box): "确定候选资产池" 
Icon: A diverse set of asset icons (stocks, bonds, gold, REIT, commodities)
Sub-text: "选择在经济驱动因素上存在根本差异的资产"

Step 2 (gold neon box): "计算滚动相关性矩阵"
Icon: 5x5 heatmap being built
Sub-text: "3-5年月度收益率数据 + 额外计算危机时期ρ"

Step 3 (gold neon box): "筛除高相关性冗余资产"
Icon: Filter funnel removing red high-correlation pairs
Sub-text: "ρ>0.7的资产对，保留夏普比率更高的一个"

Step 4 (gold neon box): "结合风险平价分配权重"
Icon: Equal risk contribution scale (reference to EP13)
Sub-text: "目标：组合内所有资产对平均相关性<0.4"

Step 5 (gold neon box): "每6个月动态监控更新"
Icon: Calendar with refresh arrow cycle
Sub-text: "ρ从<0.4升至>0.6时，触发减仓审查"

Bottom: "斯文森智慧：不要追求完美的低相关性，而要追求稳健的低相关性"

Style: High-end financial tutorial graphic, glowing neon flow paths, modern flat design. 16:9.
```

---

## 第16篇《VaR 风险价值：如何量化你能承受的最大亏损》
**文章摘要**：VaR (Value at Risk) 是量化风险管理的核心工具。"在正常市场条件下，置信水平95%的情况下，未来X天内，你的最大亏损不会超过Y元"。三种计算方法：历史模拟法、参数法（正态分布假设）、蒙特卡洛法。文章通过"100万元股票账户"的具体案例全流程演示计算，揭示VaR的局限性（无法预测黑天鹅），引出预期亏损ES（Expected Shortfall）。

### EP16-01：封面图
**文件名**：`images/ep16/ep16_cover_var.jpg`
**Prompt**：
```
A premium cinematic cover image for Episode 16. Dark navy #0d1b2a background. Title: "第16篇：VaR 风险价值" in large bold gold gradient text. Subtitle: "如何量化你能承受的最大亏损" in silver. Episode number "16" glowing gold on left.

Center visual: A dramatic risk measurement gauge/dashboard showing a glowing probability distribution bell curve. The left tail of the curve (5% area) is highlighted in intense red — labeled "VaR区域：极端亏损地带". A glowing vertical dashed line marks the 95th percentile. Right of the line is the normal green zone. Left of the line shows the danger red zone with a skull or warning symbol.

Behind the gauge: A cityscape or financial district reflected in water, dark and atmospheric. Background: Subtle data streams, risk numbers, and confidence interval notation. The word "95%" appears in massive neon cyan behind the main visual.

Style: High-end financial magazine cover, dark mode premium, dramatic risk visualization, gold and red danger accents. 16:9.
```

### EP16-02：公式解析图
**文件名**：`images/ep16/ep16_formula_breakdown.jpg`
**Prompt**：
```
A professional infographic explaining the VaR formula and its three calculation methods. Dark navy background. Title: "VaR 三种计算方法完全解析" in gold.

TOP CENTER: The core VaR definition in neon cyan box:
"P(Loss > VaR) = 1 - 置信水平(α)"
Translation below: "在置信水平α下，亏损超过VaR的概率 ≤ (1-α)"
Example: "95%置信水平下，VaR=10万元 → 有5%的概率亏损超过10万元"

THREE METHOD PANELS below in a horizontal layout:

Panel 1 (Historical Simulation — 历史模拟法):
Icon: A sorted list of historical returns from worst to best
Formula: "取历史收益率分布的第(1-α)百分位数"
Example: "过去250个交易日中，排名最差的第12个日收益率"
Pro: "无分布假设" | Con: "假设历史会重演"
Color: Gold outline

Panel 2 (Parametric — 参数法):  
Icon: A beautiful symmetrical bell curve (正态分布)
Formula: VaR = μ - zα·σ (where z_95% = 1.645)
Example: "μ=-0.05%, σ=1.2%, VaR_95% = -0.05% - 1.645×1.2% = 2.024%"
Pro: "计算简便" | Con: "假设正态分布，低估厚尾风险"
Color: Cyan outline

Panel 3 (Monte Carlo — 蒙特卡洛法):
Icon: Thousands of tiny random simulation paths converging to a distribution
Formula: "模拟10000次随机路径，取第5百分位数"
Pro: "最灵活，可捕捉非线性风险" | Con: "计算量大"
Color: Green outline

Style: Professional technical infographic, clean layout, Chinese primary labels. 16:9.
```

### EP16-03：类比图（安全气囊）
**文件名**：`images/ep16/ep16_analogy_airbag.jpg`
**Prompt**：
```
A clean educational infographic using a car safety system analogy to explain VaR. Dark navy background. Title: "VaR = 你的财务安全气囊检测报告" in gold.

Main visual: A sleek modern car (representing an investment portfolio) split into two scenarios:

LEFT SCENARIO — "没有VaR的盲目驾驶 ❌":
Driver looking confident, driving fast at night with NO dashboard gauges at all. No speedometer, no fuel gauge. Caption: "不知道最大风险敞口，无法提前准备应急储备金". The car is heading toward a cliff labeled "系统性崩盘" with no warning.

RIGHT SCENARIO — "使用VaR的智慧驾驶 ✅":  
Same driver but with a glowing dashboard showing: VaR gauge (95%置信度下最大亏损=10万元), ES meter (尾部预期亏损=14万元), confidence level indicator. Caption: "VaR就是仪表盘——告诉你在最坏情况下，你的安全气囊(现金储备)需要准备多大". The car has glowing safety systems active.

Bottom text: "VaR不能预防事故，但它让你知道安全气囊需要有多大"

Style: Clean modern illustration, dramatic contrast between ignorance vs knowledge, neon dashboard glow, Chinese text dominant. 16:9.
```

### EP16-04：历史危机VaR穿透对比图
**文件名**：`images/ep16/ep16_performance_comparison.jpg`
**Prompt**：
```
A professional financial risk analysis chart showing VaR breaches during historical crises. Dark navy background. Title: "VaR在历史极端事件中的表现：穿透次数统计" in gold.

TWO-PART LAYOUT:

TOP CHART: A time series line chart of a portfolio's daily returns (2006-2023). The chart shows:
- Daily return bars (mostly within the gray "正常区间")
- A horizontal dashed red line at the bottom: "95% VaR = -2.1%" 
- Red downward spikes that pierce through the VaR line during crises: 2008 (multiple large spikes labeled "金融危机：穿透17次"), 2015 (labeled "股灾：穿透8次"), 2020 March (labeled "疫情冲击：穿透5次"), 2022 (labeled "加息风暴：穿透9次")
- Gold band further below: "ES区域 (Expected Shortfall) — 真实尾部损失"
- Annotation: "理论上250天仅应穿透12.5次(5%)，实际穿透更多"

BOTTOM TABLE: Comparison of VaR prediction vs actual loss during each crisis:
| 危机 | VaR预测最大亏损 | 实际最大亏损 | 低估倍数 |
| 2008 金融危机 | -3.2% | -12.8% | 4.0x |
| 2020 疫情 | -2.8% | -8.5% | 3.0x |

Caption: "VaR是正常天气的预报员，它不会告诉你台风的强度"

Style: Clean financial data visualization, red spikes contrasting with gray normal zone, professional annotations. 16:9.
```

### EP16-05：著名案例图
**文件名**：`images/ep16/ep16_masters.jpg`
**Prompt**：
```
A premium infographic showing famous VaR-related cases and practitioners. Dark navy background. Title: "VaR的起源与著名使用案例" in gold.

THREE-PANEL LAYOUT:

LEFT PANEL (Origin): 
Portrait of Philippe Jorion or JP Morgan concept. Title: "摩根大通 · J.P.Morgan 1994"
Text: "首创RiskMetrics系统，向全球免费公开VaR计算方法论，彻底革命化风险管理". 
Visual: A glowing RiskMetrics document/report with the "4:15 report" legend (JP Morgan CEO Dennis Weatherstone demanded a one-page risk summary by 4:15pm every day). Glow: gold.

MIDDLE PANEL (Warning Case):
Title: "长期资本管理公司 LTCM · 1998年崩溃"
Text: "由2位诺贝尔经济学奖得主创立，VaR模型假设正态分布，完全没有预测到俄罗斯债务违约引发的相关性突变，4个月亏损46亿美元". 
Visual: A falling graph with "VaR模型完全失效" written in red. Warning sign: "对正态分布的过度依赖是致命的".

RIGHT PANEL (Limitation lesson):
Title: "巴塞尔协议与银行VaR"
Text: "全球银行业监管强制要求计算VaR，但2008年危机证明：所有银行的VaR都大幅低估了系统性风险". 
Visual: Bank logos with VaR shields that all break simultaneously during 2008 storm. Lesson: "VaR是在正常天气测试的雨伞".

Style: Cinematic, educational, dark moody lighting, gold and red accent color. 16:9.
```

### EP16-06：实战场景图
**文件名**：`images/ep16/ep16_scenarios.jpg`
**Prompt**：
```
A professional financial infographic showing 6 practical VaR applications. Dark navy background. Title: "VaR 的六大实战应用场景" in gold. 2x3 grid layout.

Cell 1: "个人股票账户风险评估" — Icon: Phone showing portfolio app with VaR readout. Text: "100万账户，95%VaR=3.2万元/天，需备3-6个月生活费应急"
Cell 2: "基金经理的日常风控" — Icon: Risk dashboard with VaR/ES dials. Text: "监控组合日VaR不超过NAV的2%，触发自动降仓"
Cell 3: "商业银行资本充足率" — Icon: Bank building with regulatory shield. Text: "Basel III要求银行用99%VaR计算最低资本金要求"
Cell 4: "期权组合希腊值管理" — Icon: Greeks (Delta, Gamma) flowing into VaR calculation. Text: "将期权的非线性风险转化为线性VaR，统一风险度量"
Cell 5: "压力测试与情景分析" — Icon: Weather forecast system but for markets. Text: "2008危机情景下VaR=多少？滞胀情景下VaR=多少？"
Cell 6: "何时不能只看VaR" — Icon: Warning sign, blind spot. Text: "黑天鹅事件VaR完全失效 → 必须配合ES和压力测试"

Style: Premium dashboard UI, neon outlines, consistent dark theme, Chinese text. 16:9.
```

### EP16-07：误区图
**文件名**：`images/ep16/ep16_mistakes.jpg`
**Prompt**：
```
A professional warning infographic showing 4 fatal mistakes when using VaR. Dark navy background with red warning accents. Title: "VaR的四大致命误区" in gold with red underline.

2x2 grid:

TOP-LEFT: "把VaR当作最大可能亏损 ❌"
Icon: A cliff edge — the VaR line is at the edge, but the actual abyss below is much deeper
Text: "VaR=在5%概率的亏损下限，不是上限！超过VaR的亏损可以是无限的"
Red warning: "LTCM以为VaR是安全网，结果网破了"

TOP-RIGHT: "盲目相信正态分布假设 ❌"
Icon: Two bell curves side by side — perfect normal distribution vs. fat-tailed real distribution. Real one has a massive left tail
Text: "金融收益率有厚尾特征(Fat Tail)，正态分布严重低估极端损失"
Red warning: "参数法VaR在危机时低估风险4-10倍"

BOTTOM-LEFT: "忽视相关性在危机时的突变 ❌"  
Icon: Correlation network that normally shows diverse connections suddenly all turns red (all correlated to +1)
Text: "平时ρ=0.2的资产，危机时全部变成ρ=0.8，VaR失去分散化效果"
Red warning: "2008年所有VaR模型都因此大失准"

BOTTOM-RIGHT: "VaR固定不变，不动态更新 ❌"
Icon: A frozen static VaR number from 2020 still being used in 2024 with very different volatility
Text: "市场波动率会变化，必须用GARCH或滚动窗口动态更新VaR"
Red warning: "使用过期VaR = 用昨天的天气预报决定今天出门穿什么"

Style: Professional warning design, bold Chinese text, dramatic red panels. 16:9.
```

### EP16-08：SOP流程图
**文件名**：`images/ep16/ep16_sop.jpg`
**Prompt**：
```
A clear step-by-step flowchart for calculating and using VaR. Dark navy background. Title: "VaR计算实战SOP：6步量化你的风险上限" in gold.

Six connected steps with glowing cyan arrows:

Step 1 (gold neon box): "收集历史收益率数据"
Icon: Spreadsheet/database with 250 rows of daily returns
Sub-text: "最少250个交易日日频数据，或60个月月频数据"

Step 2 (gold neon box): "选择VaR计算方法"
Icon: Three-way decision fork: 历史模拟法 / 参数法 / 蒙特卡洛法
Sub-text: "样本充足→历史法；快速估算→参数法；复杂组合→蒙特卡洛"

Step 3 (gold neon box): "设定置信水平和时间窗口"
Icon: A confidence level dial (90% / 95% / 99%) and calendar (1日/10日/1月)
Sub-text: "个人投资者用95%/1日；银行监管用99%/10日"

Step 4 (gold neon box): "计算VaR并换算为绝对金额"
Icon: Calculator showing VaR% × Portfolio Size = VaR in 元
Sub-text: "VaR=2.1%，账户100万 → 日VaR=2.1万元"

Step 5 (gold neon box): "计算ES(期望亏损)作为补充"
Icon: The tail area beyond VaR, average of losses in that tail
Sub-text: "ES = 超过VaR的所有极端亏损的平均值，更保守更全面"

Step 6 (gold neon box): "设置VaR触发阈值并每日监控"
Icon: Alert system / trading dashboard with automated triggers
Sub-text: "日亏损超过80%的VaR时→发出预警；超过VaR→强制降仓"

Bottom: "记住：VaR是风险的下限，不是上限。配合ES和压力测试才完整"

Style: High-end financial flowchart, glowing connecting arrows, modern flat design. 16:9.
```

---

## 第17篇《黑天鹅事件：极端风险的数学本质》
**文章核心要点**：
- 纳西姆·塔勒布（Nassim Taleb）2007年《黑天鹅》的三个特征：极端稀缺性、巨大冲击、事后可解释性
- 正态分布 vs 幂律分布（Power Law）的根本区别
- 肥尾分布（Fat-tail）：金融数据的峰度（Kurtosis）远大于3
- 脆弱性 vs 反脆弱性：如何通过哑铃策略在黑天鹅中受益

### EP17-01：封面图
**文件名**：`images/ep17/ep17_cover_black_swan.jpg`
**Prompt**：
```
A premium cinematic cover for Episode 17. Dark navy #0d1b2a background. Title: "第17篇：黑天鹅事件" in massive bold gold text. Subtitle: "极端风险的数学本质 — 不可预测的可预测" in silver.

Center visual: A majestic, dramatic BLACK SWAN emerging from dark stormy financial data streams. The swan has glowing feathers that look like circuit patterns or mathematical symbols. Its reflection in dark water shows a bell curve shattering into a power law distribution. 

Around the swan: Fragments of news headlines from famous black swan events (1987 Black Monday, 1997 Asian Crisis, 2008 Lehman collapse, 2020 COVID crash) rendered in glowing red shards.

Background: Dark storm clouds made of probability distributions and fat-tail curves. Lightning made of mathematical formulas.

Style: Ultra dramatic, cinematic, dark fantasy with financial mathematics overlaid, gold/red/deep-purple accent colors. 16:9.
```

### EP17-02：公式解析（正态分布 vs 幂律）
**文件名**：`images/ep17/ep17_formula_breakdown.jpg`
**Prompt**：
```
A professional infographic contrasting Normal Distribution vs Power Law (Fat Tail) distribution. Dark navy background. Title: "正态分布 vs 幂律分布：为什么黑天鹅不罕见" in gold.

LEFT HALF — 正态分布 (Normal/Gaussian): 
Formula: f(x) = (1/σ√2π) · exp(-(x-μ)²/2σ²)
Visual: Perfect symmetrical bell curve in blue/white
Text annotations: "Kurtosis = 3 (峰度)", "6σ事件概率≈1/十亿", "金融教科书的假设"
Red warning label: "致命缺陷：严重低估极端事件概率！"
Example: "按正态分布，2008年金融危机是25σ事件，理论上几乎不可能发生"

RIGHT HALF — 幂律分布 (Power Law / Fat Tail):
Formula: P(X > x) ~ x^(-α) where α is the tail exponent
Visual: Distribution curve with dramatically fatter left and right tails highlighted in glowing red
Text annotations: "Kurtosis >> 3", "极端事件概率远高于正态假设", "金融数据的真实形态"
Green validation: "实证检验：标普500的日收益率峰度≈5-8，远大于3"
Example: "2008年危机按幂律分布，是完全可能的小概率大事件"

CENTER: A dramatic comparison arrow showing the difference in tail probabilities at the extreme end — normal distribution shows near-zero (flat), power law shows a significant elevated tail in red.

Caption: "用正态分布管理金融风险，就像用晴天的地图预测台风路径"

Style: Scientific and professional, side-by-side comparison, neon math formulas. 16:9.
```

### EP17-03：类比图（铃声与钢琴弦）
**文件名**：`images/ep17/ep17_analogy_mediocristan.jpg`
**Prompt**：
```
An educational infographic using Taleb's "Mediocristan vs Extremistan" concept. Dark navy background. Title: "中等斯坦 vs 极端斯坦：你生活在哪个世界？" in gold. 

TWO CONTRASTING WORLDS side by side:

LEFT WORLD — "中等斯坦 Mediocristan" (gold border, calm):
Examples floating in organized cells: 人的身高, 体重, 寿命, 智商, 城市温度
Visual: A perfectly balanced scale, all examples cluster around the mean. Even the tallest person (3米) is only 2x the average.
Key insight: "极端个体改变不了样本均值。全球最高的人加入1000人样本，均值只变0.2%"
Bell curve icon: Perfect normal distribution
Label: "正态分布的天堂 — 极端值不危险"

RIGHT WORLD — "极端斯坦 Extremistan" (red border, stormy):  
Examples: 财富分配, 股票收益率, 城市人口, 书籍销量, 战争死亡人数
Visual: A wildly unbalanced scale, with one massive outlier dominating everything. Elon Musk added to 1000 billionaires — changes the average wealth by 1000x.
Key insight: "一个极端个体可以让样本均值毫无意义。黑色星期一单日-22%，超过正常波动数十倍"
Fat tail curve icon: Power law distribution with massive red tail
Label: "幂律分布的世界 — 极端值是常态"

Center divider: "金融市场毫无疑问生活在极端斯坦！"

Style: Dramatically contrasting, educational, clean design, Chinese text dominant. 16:9.
```

---

## 第18篇《蒙特卡洛模拟：用随机数预测未来》
**文章核心要点**：
- 蒙特卡洛的原理：通过大量随机模拟路径，近似出未来的概率分布
- 历史：1940年代曼哈顿计划中乌拉姆和冯·诺依曼发明（名字来自摩纳哥赌城）
- 核心应用：投资组合退休规划、期权定价、压力测试
- 具体案例：模拟100万元本金，每年定投5万，30年后的资产分布（中位数、10%概率下限、10%概率上限）

### EP18-01：封面图
**文件名**：`images/ep18/ep18_cover_monte_carlo.jpg`
**Prompt**：
```
A premium cinematic cover for Episode 18 about Monte Carlo simulation. Dark navy #0d1b2a background. Title: "第18篇：蒙特卡洛模拟" in large bold gold text. Subtitle: "用10000次随机模拟，预见财富的可能未来" in silver.

Center visual: A breathtaking fan of 10,000 glowing simulation paths spreading outward from a single starting point (like light rays or a river delta). The paths are color-coded: Bottom 10% paths in red (bad scenarios), middle 80% in cyan/blue gradient, top 10% in bright gold (best scenarios). The fan shape shows the widening uncertainty as time extends to the right. 

Overlaid text: "10,000次模拟" in massive glowing neon number. 

Background: The famous Casino de Monte-Carlo building silhouette in the distance, combined with mathematical probability density curves. Reference to Monaco's famous gambling halls where the technique was named.

Style: Ultra premium, glowing simulation paths, cinematic, mathematical beauty meets casino glamour. 16:9.
```

---

## 第19篇《破产风险：赌徒破产问题与资金管理》
**文章核心要点**：
- 赌徒破产问题（Gambler's Ruin）：即使胜率大于50%，不合理的仓位也会导致破产
- 破产概率公式：P(破产) = ((q/p)^N - 1)/((q/p)^N - (q/p)^0) 其中N是初始资金单位
- 在交易中的应用：仓位大小决定了破产概率，而不是胜率
- 连续亏损与破产概率的量化

### EP19-01：封面图
**文件名**：`images/ep19/ep19_cover_ruin.jpg`
**Prompt**：
```
A premium cinematic cover for Episode 19 about Gambler's Ruin and bankruptcy risk. Dark navy #0d1b2a background. Title: "第19篇：破产风险" in large gold text. Subtitle: "赌徒破产问题 — 即使你是赢家，也可能被市场淘汰" in silver.

Center visual: A dramatic chessboard-like infinite corridor stretching into darkness, representing the random walk of portfolio value. On the left wall: "起始资金 N 单位" with a green glow. On the right: a bright glowing goal "目标" (profit target). But on the floor, a massive red abyss labeled "破产线 = 0" that the corridor might fall into at any step.

A single glowing coin mid-air showing heads and tails simultaneously — representing the probability of each step. Below it: two probability labels: "p = 胜率" in green, "q = 1-p = 败率" in red.

Background: Faint equations of the Gambler's Ruin formula floating in the dark.

Style: Geometric, mathematical dread, dramatic infinite perspective, gold and red danger palette. 16:9.
```

---

## 第20篇《最大回撤与资金恢复时间：衡量策略韧性》
**文章核心要点**：
- 最大回撤（Max Drawdown, MDD）：从历史高点到最低谷的最大跌幅百分比
- 恢复时间（Recovery Time / Drawdown Duration）
- 卡尔玛比率（Calmar Ratio）= 年化收益率 / 最大回撤，衡量风险调整后收益
- 实战案例：巴菲特的伯克希尔在2009年最大回撤51%，但凭借优秀的基本面最终完整恢复

### EP20-01：封面图
**文件名**：`images/ep20/ep20_cover_drawdown.jpg`
**Prompt**：
```
A premium cinematic cover for Episode 20 about Max Drawdown and recovery. Dark navy #0d1b2a background. Title: "第20篇：最大回撤与资金恢复" in large gold text. Subtitle: "韧性的数学度量 — 你能从谷底爬回来吗？" in silver.

Center visual: A dramatic equity curve line chart showing:
- Initial upward trend in bright gold
- A sudden sharp drop (the maximum drawdown valley) in red — the bottom labeled "最低谷"
- The peak before drop labeled "历史高点 (Peak)"
- A recovery path back up in cyan/teal
- The horizontal distance between peak and recovery labeled "恢复时间 (Recovery Time)" in orange
- The vertical depth labeled "最大回撤 (Max Drawdown = -38%)" in red

A phoenix silhouette rising from the chart's lowest point toward recovery — representing resilience.

Background: Multiple benchmark equity curves (Berkshire, S&P500) in faint lines showing their historical drawdown patterns.

Style: Dramatic narrative visualization, financial data art, gold-to-red-to-cyan emotional journey. 16:9.
```
