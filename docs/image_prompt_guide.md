# 《股票市场的数学原理》系列
# 图像生成提示词完整指南

> 本文档是该系列25篇文章的**图像生产手册**。
> 使用任何支持文本转图像的AI工具（Midjourney / Stable Diffusion / DALL-E / Imagen）时，直接复制对应模板填入变量即可。

---

## 一、系列视觉识别规范（VI）

> [!CAUTION]
> **以下三条为铁律，违反任意一条将导致文章配图被打回重做：**
> 1. **【尺寸铁律】** 每张图片生成时必须指定 `AspectRatio: "16:9"`，所有图片必须保持 1376×768 横版格式，严禁使用默认正方形（1:1）。
> 2. **【内容铁律】** 每张图片的视觉内容必须与该章节标题及文字内容直接对应，**严禁将其他篇章已有图片复用到本篇**（尤其是凯利公式图不得出现在复利、均值回归等其他篇章中）。
> 3. **【唯一性铁律】** 每篇文章的7张图必须全部为该篇新生成，图片文件名需含本篇编号前缀（如 `ep07_`），以便识别和溯源。

所有图像必须遵循以下统一风格，以保持系列一致性：

```
【全系列视觉规范 · 必须在每个提示词中包含】

背景: Dark navy #0d1b2a (深海军蓝)
主色调: 
  - 金色 (gold #FFD700) → 标题、重要公式、强调
  - 青色 (cyan #00E5FF) → 图表线条、流程箭头、数据
  - 绿色 (green #00FF88) → 正确/推荐/盈利
  - 红色 (red #FF4444) → 错误/警告/亏损
字体风格: 简洁现代无衬线, 中英双语
整体风格: 高端金融出版物/暗色模式/霓虹渐变光效
纵横比: 【强制 AspectRatio="3:2」即16:9横版，约1376×768】
分辨率要求: 高清 professional quality

【图片命名规范】
文件名必须以篇章编号为前缀，例如：
  ep07_cover.jpg / ep07_formula.jpg / ep07_analogy.jpg
禁止使用通用名如 cover.jpg 或跨篇复制的文件。

【内容对应检查清单（每张图生成前必须自问）】
✅ 这张图的视觉元素是否与本章节标题字面强相关？
✅ 这张图是否包含本篇的核心数学公式或特有比喻？
✅ 如果换到另一篇，读者是否会感到明显困惑？→ 若不困惑，说明图不够专属，需重做。
```

---

## 二、九大图表模板 · 提示词框架

每篇文章通常需要以下类型的图表，按使用频率排序：

---

### 模板① · 篇章封面图

**用途**: 每篇文章的标题图，放置在文章开头  
**使用频率**: 每篇必备 × 25篇

```
【模板①：篇章封面图 · 可复用框架】

A premium cover image for Episode [篇号] of a financial mathematics series.

Title text: "第[篇号]篇：[原理名称中文]" in large bold gold gradient text
Subtitle: "[英文名称] — [一句话定位]" in silver/white
Episode number: Large "[篇号用英文序号 e.g. 01]" in gold on left side

Center visual: [核心公式或核心视觉元素，用发光霓虹氰色呈现]

Background elements: 
- Deep space dark navy #0d1b2a background
- Subtle floating mathematical symbols as star-like particles
- Glowing stock chart line weaving through background
- Geometric gold frame lines

Bottom tagline: "[本篇最著名的引用者或使用场景描述]"

Visual metaphor: [1-2个与该原理相关的具体意象，如: 天平/弹簧/扑克牌/望远镜]

Style: High-end financial magazine cover, dark mode premium, neon glow accents, 
gold and cyan color scheme, ultra professional, Chinese text prominent
Aspect ratio: 16:9
```

**各篇变量填写参考表**:

| 篇号 | 原理中文名 | 英文名 | 核心公式/元素 | 推荐视觉意象 |
|------|---------|-------|------------|------------|
| 01 | 凯利公式 | Kelly Criterion | f* = (bp-q)/b | 天平+筹码 |
| 02 | 期望值理论 | Expected Value | E[X] = Σp·x | 骰子+计算器 |
| 03 | 大数定律 | Law of Large Numbers | X̄ₙ → μ | 无数硬币+收敛曲线 |
| 04 | 中心极限定理 | Central Limit Theorem | N(μ,σ²) | 钟形曲线 |
| 05 | 复利定律 | Compound Interest | A=P(1+r)ⁿ | 雪球/指数曲线 |
| 06 | 均值回归 | Mean Reversion | O-U过程 | 钟摆/弹簧 |
| 07 | 动量效应 | Momentum Effect | 截面动量 | 列车/飞轮 |
| 08 | 贝叶斯推断 | Bayesian Inference | P(A\|B) | 侦探放大镜 |
| 09 | 安全边际 | Margin of Safety | 内在价值-买价 | 桥梁承重设计 |
| 10 | 因子投资 | Factor Investing | Fama-French | 筛子/过滤器 |
| 11 | 现代投资组合 | Modern Portfolio Theory | 有效前沿 | 星座图/鸡蛋篮子 |
| 12 | 夏普比率 | Sharpe Ratio | SR=(Rp-Rf)/σ | 奥运评分/秤 |
| 13 | 风险平价 | Risk Parity | 风险贡献均等 | 团队分工图 |
| 14 | 最优仓位管理 | Optimal-f | TWR最大化 | 精密仪器 |
| 15 | 相关性与分散化 | Correlation & Diversification | ρ矩阵 | 雨伞+冰淇淋 |
| 16 | VaR价值风险 | Value at Risk | 置信区间 | 洪水线/保险 |
| 17 | 黑天鹅理论 | Black Swan Theory | 幂律分布 | 黑天鹅/肥尾 |
| 18 | 蒙特卡洛模拟 | Monte Carlo Simulation | 随机路径 | 万条光线/迷宫 |
| 19 | 破产风险定律 | Risk of Ruin | 破产概率公式 | 悬崖/红线 |
| 20 | 马尔可夫链 | Markov Chain | 转移矩阵 | 状态机/齿轮 |
| 21 | 主动管理基本定律 | Fundamental Law | IR=IC×√BR | 篮球运动员 |
| 22 | 布莱克-舒尔斯 | Black-Scholes | B-S方程 | 期权天平 |
| 23 | 套利定价理论 | APT | 多因子模型 | 拼图 |
| 24 | 行为金融学 | Behavioral Finance | 前景理论 | 大脑双通道 |
| 25 | 综合框架 | Integrated Framework | 全系统图 | 星图/机器 |

---

### 模板② · 公式拆解图（Formula Breakdown）

**用途**: 将核心公式的每个变量用颜色和视觉元素直观解释  
**使用频率**: 每篇必备，位于"核心公式"章节

```
【模板②：公式拆解图】

A professional dark-themed infographic explaining the [原理名] formula for investing.
Dark navy background.

Title: "[原理名] · 公式完全解析" in gold

CENTER: The main formula displayed prominently:
[完整公式，LaTeX风格] glowing in large neon cyan text, gold framing box

LEFT PANEL - "输入变量解析":
For each variable, create a labeled box with:
  - Variable symbol in large colored text
  - Chinese name in white
  - Plain language explanation in small text
  - A concrete example value
  - An intuitive icon/metaphor

  Variable colors:
  - Main output (f*, IR, E[X]等): GOLD
  - Probability/rate inputs: BLUE  
  - Ratio/multiplier inputs: GREEN
  - Loss/risk inputs: RED

RIGHT PANEL - "计算步骤演示":
Show numbered calculation steps (Step1/Step2/Step3) with actual numbers:
[具体数值示例，如: p=0.6, b=1.5, q=0.4]
Each step shows the substitution and arithmetic clearly.

BOTTOM: "直觉理解" section with one powerful analogy:
"就像[生活类比]..."

Style: Clean professional, neon accents, Chinese dominant, calculation visible
```

**各篇公式变量填写**:

| 篇号 | 公式 | 示例数值 | 生活类比 |
|------|------|---------|--------|
| 01 | f*=(bp-q)/b | p=0.6, b=1.5, f*=33% | 飞机安全系数 |
| 02 | E[X]=Σp·x | 60%×+15% - 40%×-10% = +5% | 外科医生手术决策 |
| 03 | X̄ₙ→μ | 抛100次硬币趋近50% | 保险公司定价 |
| 04 | CLT钟形曲线 | n→∞时分布趋于正态 | 身高分布 |
| 05 | A=P(1+r)ⁿ | 10万×1.1²⁰=67.27万 | 滚雪球 |
| 06 | 价格偏离→回归 | PE历史均值20，现在8→买 | 弹簧压缩 |
| 07 | 12-1月收益排名 | 前20%持有→超额10% | 列车加速度 |
| 08 | P(A\|B)=P(B\|A)P(A)/P(B) | 更新先验概率 | 侦探推理 |
| 09 | 安全边际=内在价值-市价 | 内在价值100，买入70=30%余量 | 桥设计10吨只装7吨 |
| 10 | R=α+Σβᵢ·Fᵢ+ε | 价值+动量+质量因子叠加 | 招聘评分系统 |

---

### 模板③ · 对比图（Before vs After / 策略对比）

**用途**: 展示正确vs错误、不同策略优劣、使用前后效果  
**使用频率**: 几乎每篇都用

```
【模板③：对比图框架】

A professional comparison infographic. Dark navy background.

Title: "[原理名] · [对比主题]" in gold

Layout: [2列 / 3列 / 4列] side-by-side panels, each with glowing border

For EACH panel, specify:
  Panel [N] - [颜色] border:
    Header: "[列标题]" in [颜色] 
    Badge: "[评级/标签]" e.g. "❌不推荐" or "✅推荐" or "★最佳"
    Main visual: [该策略的折线图形状描述 / 图标 / 数字]
    Key metrics listed:
      - [指标1]: [值] in [颜色]
      - [指标2]: [值] in [颜色]
    Caption: "[一句话总结]"

Bottom: A summary comparison table with rows:
  - [维度1] | [面板1值] | [面板2值] | [面板3值]
  - [维度2] | ...

Color coding rule:
  Red panel = dangerous/wrong strategy
  Yellow panel = acceptable/moderate strategy  
  Green panel = recommended strategy
  Gold panel = theoretical optimum

Style: Clean, consistent column widths, color-coded performance indicators
```

---

### 模板④ · 流程/SOP图（Flowchart）

**用途**: 展示实战操作步骤、决策流程  
**使用频率**: 每篇的"实战SOP"章节

```
【模板④：SOP流程图框架】

A professional [N]-step flowchart infographic. Dark navy background.

Title: "[原理名] · [动作]前[N]步SOP" in gold, top-right corner

MAIN FLOW: Vertical sequence of numbered steps connected by arrows:

Step [N] - [颜色] glowing circle "[数字]":
  Left: Icon ([图标描述])
  Center title: "[步骤标题]" in white bold
  Details bullet points:
    • [关键要点1]
    • [关键要点2]
  Right: [可选：mini表格 or 数值示例]

[决策节点时，使用菱形分叉]:
  Decision: "[判断条件]?"
  → YES path (green): "[继续标签]"
  → NO path (red): "[停止/结束标签]"

Arrow style: Thick glowing arrows (cyan for forward, red for abort paths)

BOTTOM RIGHT: "行业最佳实践" summary card with gold border:
  "[最权威引用者]验证: [核心要点]"

Step circle colors: 01=cyan, 02=cyan, 03=cyan, 04=gold(decision), 05=green(final)
```

---

### 模板⑤ · 错误/陷阱图（Mistake Grid）

**用途**: 展示使用该原理时的常见错误和正确做法  
**使用频率**: 每篇"常见错误"章节

```
【模板⑤：错误陷阱网格图框架】

A professional educational "[N]大致命错误" infographic in [2×2 / 2×3] grid layout.
Dark navy background.

Title bar: "[原理名] · [N]大致命错误" in gold with ⚠️ warning icon, red gradient bar

For EACH grid cell (red glowing border):
  Top-left: Large red ❌ icon
  Title: "错误[①②③④]：[错误名称]" in white bold
  
  Visual metaphor: [1-2 sentence description of the core illustration]
    Use clear metaphorical visuals:
    - Dartboard with missed darts = inaccuracy
    - Broken scale/balance = ratio distortion
    - Empty box with X = wrong application
    - Tiny sample coins = insufficient data
    - Clock running out = timing issues
  
  Bottom caption box (cyan border):
    "正确做法: [具体的正确方法]" with ✅ green checkmark
    Sub-note: "[量化标准 e.g. ≥30笔/n<30时禁止]"

Grid spacing: even 2x2 or 2x3 with clear dividing lines
Background: each cell slightly lighter than background for contrast
```

---

### 模板⑥ · 类比解释图（Analogy Explainer）

**用途**: 用生活场景类比来解释抽象的数学原理  
**使用频率**: 每篇"通俗理解"章节，1-3张

```
【模板⑥：生活类比图框架】

A clean educational infographic explaining [原理名] using [生活场景] analogy.
Dark navy background.

Title: "[原理名] = [类比名称]" in gold, large

THREE-PANEL LAYOUT:

LEFT PANEL - "[生活场景]的世界":
  [描述该生活场景的具体视觉元素，卡通/图标风格]
  Label elements that map to financial concepts:
    [生活元素A] = [金融概念A]
    [生活元素B] = [金融概念B]

CENTER PANEL - "核心规则" (gold border):
  The key insight stated simply:
  "[一句话核心洞见]"
  Show the mathematical connection:
  [简化公式 or 逻辑箭头]

RIGHT PANEL - "投资中的应用":
  [具体的股票/基金投资场景]
  Show the same logic applied:
    [具体操作步骤1]
    [具体操作步骤2]
  Result: [预期效果, e.g. +X% 年化]

BOTTOM: Connection bridge visual showing the analogy maps to investment

Common analogy pool for this series:
  - 保险公司定价 → 大数定律
  - 弹簧压缩 → 均值回归
  - 飞机安全系数 → 半凯利
  - 外科医生 → 期望值思维
  - 篮球命中率×投篮次数 → IR=IC×√BR
  - 列车加速 → 动量效应
  - 侦探推理更新线索 → 贝叶斯
  - 桥梁承重余量 → 安全边际
  - 雨伞店+冰淇淋店 → 负相关资产
  - 赌场经营者视角 → 系统思维
```

---

### 模板⑦ · 历史数据/证据图（Evidence Chart）

**用途**: 展示该原理的历史实证数据、真实表现  
**使用频率**: "历史证据"章节

```
【模板⑦：历史证据图框架】

A professional financial performance chart showing historical evidence for [原理名].
Dark navy background.

Title: "[原理名] · 历史实证数据" in gold

MAIN CHART AREA:
  Chart type: [折线图/柱状图/散点图] — 根据数据类型选择
  
  X-axis: "[时间维度]" e.g. 年份1927-2023, 交易次数1-100, 持有年限
  Y-axis: "[表现指标]" e.g. 年化超额收益%, 资产倍数, 胜率
  
  Data series (each with distinct neon color + label):
    Series 1 "[策略名称]": [颜色] line/bar, "[关键数值标注]"
    Series 2 "[对比基准]": [颜色] line/bar, "[关键数值标注]"
    [如有第三组数据]: [颜色] ...
  
  KEY ANNOTATIONS (callout boxes):
    Mark significant events/periods:
    "[重要时间节点]" → "[发生的事及影响]"
    "[代表性数值]" in gold callout: e.g. "+10.5% 年化超额"
  
  BOTTOM NOTE: 
    "数据来源: [Fama-French/CRSP/Bloomberg等]"
    "时间跨度: [X年]  |  样本数量: [N笔]"

RIGHT SIDEBAR: "关键统计数字" cards:
  Card 1: "[最重要指标]" "[具体数值]" 
  Card 2: "[第二指标]" "[具体数值]"
  Card 3: "最大回撤" "[数值]" in red

Style: Clean financial data visualization, grid lines, professional annotation style
```

---

### 模板⑧ · 著名使用者图（Famous Users）

**用途**: 展示顶级投资者如何运用该原理  
**使用频率**: "著名使用者"章节，每篇1张

```
【模板⑧：著名使用者图框架】

A professional infographic showing famous real-world applications of [原理名].
Dark navy background.

Title: "[原理名] · 顶级使用者案例" in gold

[2×2 or 1×3 or 2×3] grid layout based on number of examples

For EACH person/institution card (gold glowing border):
  Header: "[人名中文] [人名英文]" in white bold
  Role badge: "[职位/机构]" in cyan badge  
  Portrait area: [简约图标或首字母圆形头像, 避免真实人脸]
  
  Key facts (bullet list):
    • "[具体应用场景]"
    • "[量化成就]" in green
    • "[该原理的具体用法]"
    • "[代表性语录]" in italics/quote style
  
  Performance metric (bottom of card):
    "[核心业绩]" in large gold numbers
    e.g. "年化+20% × 57年" or "IR=3.5"

FOOTER: One-line insight connecting all cases:
  "[他们的共同点：都用[该原理]解决了[核心问题]]"

Recommended persons per principle:
  凯利公式: Ed Thorp, 巴菲特, 西蒙斯, 比尔·格罗斯
  期望值: 巴菲特, 芒格, Dan Ariely
  均值回归: 巴菲特, 约翰·坦普顿, 霍华德·马克斯
  因子投资: 法玛, 阿斯内斯(AQR), 维度基金
  动量: 克利福德·阿斯内斯, 德国Herd基金
  行为金融: 卡尼曼, 塔勒, 席勒
```

---

### 模板⑨ · 本篇总结图（Summary Mindmap）

**用途**: 文章结尾的一页总结，帮助读者回忆全文核心  
**使用频率**: 每篇必备，放在结尾

```
【模板⑨：总结思维导图框架】

A professional summary infographic for [原理名]. Dark navy background.

Title: "第[N]篇 核心要点回顾" in gold, top center

CENTRAL HUB: Large circle center with "[原理名]" and core formula

RADIATING BRANCHES (5-6 branches, like a mind map):

Branch 1 - "是什么" (cyan): 
  "[一句话定义]"
  
Branch 2 - "核心公式" (gold):  
  "[公式]"
  "[变量速查: x=y]"

Branch 3 - "最佳类比" (light blue):
  "[生活类比名称]"
  "[一句话类比描述]"

Branch 4 - "实战要点" (green):
  "✅ [要点1]"
  "✅ [要点2]"
  "✅ [要点3]"

Branch 5 - "致命错误" (red):
  "❌ [错误1]"
  "❌ [错误2]"

Branch 6 - "下一篇预告" (purple/violet):
  "→ 第[N+1]篇: [下一篇名]"
  "[一句话钩子]"

BOTTOM: Series navigation bar showing 25 numbered dots, current one highlighted in gold

Style: Radial mind map layout, glowing connections, color-coded branches, 
clean without overcrowding
```

---

## 三、各篇图像清单规划

每篇文章建议配置 **5~8 张图**，以下是标准配置：

| 图序 | 模板类型 | 是否必须 | 篇幅位置 |
|------|---------|---------|---------|
| 图1 | ①篇章封面图 | ✅ 必须 | 文章最顶部 |
| 图2 | ②公式拆解图 | ✅ 必须 | 核心公式章节 |
| 图3 | ⑥类比解释图 | ✅ 必须 | 通俗理解章节 |
| 图4 | ⑦历史证据/策略对比图 | ✅ 必须 | 实证章节 |
| 图5 | ⑧著名使用者图 | ✅ 必须 | 案例章节 |
| 图6 | ⑤错误陷阱图 | ✅ 必须 | 常见错误章节 |
| 图7 | ④SOP流程图 | ✅ 必须 | 实战SOP章节 |
| 图8 | ⑨总结思维导图 | 推荐 | 文章结尾 |

---

## 四、完整示例：EP02 期望值理论 所有提示词

> 以下是第02篇的**完整、可直接复制使用**的提示词，作为参考示范。

### EP02 · 图1 · 篇章封面图

```
A premium cover image for Episode 02 of a financial mathematics series.
Dark deep space navy #0d1b2a background with star-particle effect.

Title: "第二篇：期望值理论" in large bold gold gradient text
Subtitle: "Expected Value — 所有决策的数学基石" in silver/white
Episode number: Large "02" in glowing gold on the left side

Center formula glowing in neon cyan: E[X] = Σ pᵢ · xᵢ
Around the formula: floating probability symbols: p₁, p₂, x₁, x₂ in softer glow

Visual metaphors:
- A surgeon in operating room silhouette (decision maker)
- Poker cards fanned out showing different probability outcomes
- A glowing scale balancing "概率×收益" on each side

Background elements:
- Subtle stock chart lines in dark cyan
- Mathematical notation scattered like constellations
- Geometric lines framing composition in gold

Bottom tagline: "巴菲特 · 芒格 · 索罗斯 — 他们从不赌，只下有把握的注"

Style: High-end financial magazine cover, dark mode premium, cinematic quality
Chinese text prominent, bilingual labels, ultra professional
Aspect ratio: 16:9
```

### EP02 · 图2 · 公式拆解图

```
A professional dark-themed infographic explaining the Expected Value formula for investing.
Dark navy #0d1b2a background.

Title: "期望值 · 公式完全解析" in gold

CENTER: Main formula in large glowing neon cyan box:
E[收益] = p₁ × x₁ + p₂ × x₂ + ... = Σ pᵢ · xᵢ

LEFT PANEL - Variable breakdown with color-coded boxes:
  GOLD box: "E[X]" — "期望值" — "所有结果的概率加权平均" — "= +5%"
  BLUE box: "p" — "概率" — "每种结果发生的可能性" — "p=0.6 (60%)"
  GREEN box: "x (正)" — "盈利结果" — "赢了能赚多少" — "x=+15%"
  RED box: "x (负)" — "亏损结果" — "输了会亏多少" — "x=-10%"

RIGHT PANEL - Step-by-step calculation:
  Step 1: List outcomes: 
    赢 (60%) → +15%
    输 (40%) → -10%
  Step 2: Multiply each: 
    60% × 15% = +9% (green block)
    40% × 10% = -4% (red block)
  Step 3: Sum them: 
    +9% - 4% = +5% (gold result block, POSITIVE EXPECTED VALUE ✅)
  
  DECISION: E[X] > 0 → ✅ 值得入场
            E[X] ≤ 0 → 🛑 不应入场

BOTTOM "直觉理解": 
  "就像外科医生手术前评估: 成功率×收益 > 风险×代价 才推荐手术"
  Show: surgeon icon with checklist → decision → patient icon

Style: Professional infographic, neon accents, Chinese primary labels, calculation visible
```

### EP02 · 图3 · 类比解释图（医生 vs 赌徒）

```
A clean educational infographic explaining Expected Value using surgeon vs gambler analogy.
Dark navy background.

Title: "期望值思维 — 外科医生 vs 赌徒" in gold

LEFT PANEL - "赌徒思维 ❌" (red border):
  Icon: Excited gambler face with slot machine
  Thought bubble: "感觉今天手气好！" 
  Actions shown: Random bets, no calculation
  Result shown: Zigzag curve going DOWN overall despite some wins
  Label: "凭感觉 = 负期望值游戏"

CENTER PANEL - "期望值公式" (gold border):
  Formula: E[决策] = Σ(概率 × 结果)
  Three-step checklist:
    ① 列出所有可能结果 ✓
    ② 估算每种结果的概率 ✓  
    ③ 计算期望值，只做E>0的决策 ✓
  Big gold "ONLY WHEN E[X] > 0"

RIGHT PANEL - "外科医生思维 ✅" (green border):
  Icon: Professional surgeon with clipboard
  Thought shown: 
    "成功率80% × 获益10年 = 8年预期收益"
    "失败率20% × 损失手术费 = 代价"
    "净期望 > 0 → 推荐手术"
  Result: Smooth upward curve with occasional small dips
  Label: "系统评估 = 正期望值系统"

BOTTOM: "你的每笔投资，都应该像外科医生一样先做期望值计算"
Show investor icon with calculator→stock chart→positive result

Style: Clean modern, three-panel comparison, neon accents, Chinese text dominant
```

### EP02 · 图4 · 常见错误图

```
A professional educational "期望值理论·四大认知错误" infographic in 2×2 grid.
Dark navy background.

Title bar: "期望值理论 · 四大认知错误" in gold with ⚠️ icon, red gradient title bar

Cell 1 (top-left, red border): "错误①：只看胜率，不看赔率"
  Visual: Two scenarios side by side:
    Bad: 胜率90% but win=+1%, lose=-20% → E=-1.1% (red)
    Good: 胜率40% but win=+30%, lose=-10% → E=+6% (green)
  Caption: "正确: 期望值=胜率×盈利 - 败率×亏损" ✅

Cell 2 (top-right, red border): "错误②：把小概率大事件忽略"
  Visual: Normal distribution curve with fat tail highlighted in red
  Arrow pointing to tail: "这里藏着灾难！"
  Caption: "正确: 必须将极端情况纳入期望值计算" ✅

Cell 3 (bottom-left, red border): "错误③：一次结果推翻期望值"  
  Visual: Person angrily crossing out formula after one loss
  Show: Single loss ≠ strategy failure (small sample)
  Caption: "正确: 期望值需要大量重复才显现，单次结果是噪音" ✅

Cell 4 (bottom-right, red border): "错误④：用情绪而非计算做决策"
  Visual: Fear/greed meter swinging wildly vs calm calculator
  Caption: "正确: 每次决策前先写下期望值计算结果" ✅

Professional grid design, clear visual metaphors per cell, Chinese labels dominant
```

### EP02 · 图5 · SOP流程图

```
A professional 4-step flowchart "期望值评估·买入前4步检查". Dark navy background.

Title: "期望值评估 · 买入前4步检查" in gold, top-right

Step 01 (cyan circle): Icon: telescope/research
  Title: "识别所有可能结果"
  Details: 
    • 上涨场景: 涨幅X%, 概率p₁
    • 下跌场景: 跌幅Y%, 概率p₂  
    • 极端场景: 极端跌幅Z%, 概率p₃ (尾部风险！)
  Right: Simple scenario table template

Arrow down →

Step 02 (cyan circle): Icon: probability calculator
  Title: "为每个结果估算概率"
  Details:
    • 基于: 历史数据+行业研究+宏观判断
    • 验证: 所有概率之和=100%
    • ⚠️ 警告: 不要忽略小概率极端结果
  Decision split: 数据充分? YES→继续 / NO→增加研究

Arrow (green path) →

Step 03 (gold circle, decision): Icon: formula E[X]
  Title: "计算期望值"
  Show: E[X] = p₁×x₁ + p₂×x₂ + p₃×x₃
  With actual numbers filled in
  Decision diamond: E[X] > 0?
    → YES (green): "进入Step 4"
    → NO (red): "🛑 放弃这笔交易"

Arrow (green path) →

Step 04 (green circle): Icon: checkmark/execute
  Title: "结合凯利公式确定仓位"
  Details:
    • 期望值 > 0 确认入场资格
    • 用第01篇凯利公式计算具体仓位
    • 设置止损保护盈亏比

RIGHT CARD "行业最佳实践 (芒格验证)":
  "宁可错过，不可盲目。没有计算过期望值的交易，一笔都不做。"

Style: Professional flowchart with cyan/gold/green step circles, decision diamonds in gold
```

### EP02 · 图6 · 著名使用者图

```
A professional infographic showing "期望值思维顶级使用者" — 3 cases.
Dark navy background.

Title: "期望值理论 · 顶级实践者" in gold

THREE-CARD LAYOUT (horizontal, gold glowing borders):

Card 1 - "沃伦·巴菲特":
  Icon: Circular avatar with "WB" initials, gold ring
  Role badge: "伯克希尔·哈撒韦 CEO" in cyan
  Facts:
    • "只在期望价值明确为正时下注"
    • "宁愿持有现金等待高期望机会"  
    • "可口可乐投资: 估算10年期望收益>300%"
    • 语录: "投资的核心是评估概率，而不是预测价格"
  Metric: "年化+20% × 57年 = $1340亿"

Card 2 - "查理·芒格":
  Icon: Circular avatar with "CM" initials, silver ring
  Role badge: "伯克希尔副主席 · 多元思维模型"
  Facts:
    • "用期望值思维跨学科决策"
    • "反转+期望值: 先想什么情况期望值为负"
    • "把每笔投资想成一笔保险业务"
    • 语录: "每个投资决策都是一次概率游戏"
  Metric: "合作60年 共同创造史上最伟大投资记录"

Card 3 - "乔治·索罗斯":
  Icon: Circular avatar with "GS" initials, platinum ring  
  Role badge: "量子基金 · 宏观对冲大师"
  Facts:
    • "反射理论=市场期望值动态变化模型"
    • "英镑危机: 期望值极度正→重仓做空10亿英镑"
    • "仓位大小与期望值信心正相关"
    • 语录: "重要的不是你对还是错，是对的时候押多少"
  Metric: "英镑危机单次盈利+$10亿 (1992)"

BOTTOM: "他们的共同点: 从不'感觉'交易，只做期望值经过计算的决策"

Style: Three equal columns, gold borders, cyan badges, professional dark design
```

---

## 五、通用后缀（每个提示词末尾都加）

```
【通用后缀 · 每个提示词末尾加入以下内容保持系列一致性】

Visual consistency rules:
- Background: Dark navy #0d1b2a, NO pure black or light backgrounds
- Primary accent: Gold #FFD700 for titles and key formulas
- Secondary accent: Cyan #00E5FF for charts and arrows  
- Success indicators: Green #00FF88
- Warning/error indicators: Red #FF4444
- All text: Sans-serif modern font
- Chinese text: Prominent, larger than English equivalents
- English text: Subtitle/caption level only
- Avoid: Stock photo style, clipart, watermarks, borders outside canvas

Quality requirements:
- High resolution, crisp text rendering
- No blurry or pixelated elements
- Professional financial publication quality
- Consistent padding/margins
- Readable at thumbnail size
```

---

## 六、快速生成备忘卡

```
每次生成新篇图像时的检查清单:

□ 图1: 篇章封面图 (模板①) ← 第一个生成
□ 图2: 公式拆解图 (模板②) 
□ 图3: 类比说明图 (模板⑥)
□ 图4: 历史证据/对比图 (模板③或⑦)
□ 图5: 著名使用者图 (模板⑧)
□ 图6: 错误陷阱图 (模板⑤)
□ 图7: SOP流程图 (模板④)
□ 图8: 总结思维导图 (模板⑨) ← 可选

每张图确认:
□ 背景是深海军蓝 ✓
□ 标题是金色 ✓
□ 图表/箭头是青色 ✓
□ 中文字体够大 ✓  
□ 有具体数值示例 ✓
□ 加了通用后缀 ✓
```

---

*《股票市场的数学原理》系列图像生成完整指南*  
*本文档适用全部25篇，随系列进展持续更新*
