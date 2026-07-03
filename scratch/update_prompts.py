import re

prompts_content = """---

## 第17篇《黑天鹅事件：极端风险的数学本质》
**文章核心要点**：塔勒布黑天鹅理论，正态分布 vs 幂律分布，脆弱性 vs 反脆弱性，哑铃策略，实战应用。

### EP17-01：封面图
**文件名**：`images/ep17/ep17_cover_black_swan.jpg`
**Prompt**：A premium cinematic cover for Episode 17. Dark navy #0d1b2a background. Title: "第17篇：黑天鹅事件" in bold gold. Center visual: A majestic BLACK SWAN emerging from stormy data streams, shattering a bell curve.

### EP17-02：公式解析（正态分布 vs 幂律）
**文件名**：`images/ep17/ep17_formula_breakdown.jpg`
**Prompt**：Infographic contrasting Normal Distribution (perfect bell curve, blue) vs Power Law (fat tail highlighted in glowing red). Title: "正态分布 vs 幂律分布：为什么黑天鹅不罕见" in gold.

### EP17-03：类比图（中等斯坦 vs 极端斯坦）
**文件名**：`images/ep17/ep17_analogy_mediocristan.jpg`
**Prompt**：Educational infographic. Two worlds side by side. Left: "中等斯坦" (calm, normal distribution of human height). Right: "极端斯坦" (stormy, extreme wealth distribution with one outlier dominating).

### EP17-04：全流程实战图（哑铃策略构建）
**文件名**：`images/ep17/ep17_barbell_strategy.jpg`
**Prompt**：A barbell strategy visualization. Left weight (90%): Safe assets (cash, gold) in green glow. Right weight (10%): High risk (deep out-of-the-money options) in red glow. Thin connecting bar.

### EP17-05：著名人物图
**文件名**：`images/ep17/ep17_masters.jpg`
**Prompt**：Portrait collage of Nassim Taleb and Mark Spitznagel on dark navy background. Glowing quotes about Antifragility and Universa Investments' 3600% return during crisis.

### EP17-06：实战场景图
**文件名**：`images/ep17/ep17_scenarios.jpg`
**Prompt**：2x3 grid showing 6 practical scenarios for managing black swan risks (e.g., Options, Portfolio allocation, Stress testing). Neon outlines on dark navy.

### EP17-07：四大误区图
**文件名**：`images/ep17/ep17_mistakes.jpg`
**Prompt**：2x2 warning grid showing 4 fatal mistakes in extreme risk management (e.g., trusting VaR blindly, ignoring fat tails). Red warning accents.

### EP17-08：SOP流程图
**文件名**：`images/ep17/ep17_sop.jpg`
**Prompt**：Step-by-step flowchart for building an antifragile portfolio. 5 connected glowing boxes.

---

## 第18篇《蒙特卡洛模拟：用随机数预测未来》

### EP18-01：封面图
**文件名**：`images/ep18/ep18_cover_monte_carlo.jpg`
**Prompt**：Premium cinematic cover. Title: "第18篇：蒙特卡洛模拟" in gold. Center: 10,000 glowing simulation paths spreading outward from a single point.

### EP18-02：原理图解
**文件名**：`images/ep18/ep18_principle.jpg`
**Prompt**：Infographic explaining Monte Carlo method. Showing random variable generation -> simulation engine -> probability distribution of outcomes.

### EP18-03：生活类比图（天气预报/扔硬币）
**文件名**：`images/ep18/ep18_analogy.jpg`
**Prompt**：Analogy visual comparing Monte Carlo to predicting weather by running 1000 simulated atmospheric models.

### EP18-04：实战演练图（退休资产模拟）
**文件名**：`images/ep18/ep18_retirement_sim.jpg`
**Prompt**：A chart showing a retirement portfolio simulated 10000 times over 30 years. Showing median, 5th percentile (ruin risk), and 95th percentile.

### EP18-05：大师应用图
**文件名**：`images/ep18/ep18_masters.jpg`
**Prompt**：Portraits of Stanislaw Ulam and John von Neumann. Background: Manhattan project references and early computer simulation charts.

### EP18-06：实战场景图
**文件名**：`images/ep18/ep18_scenarios.jpg`
**Prompt**：2x3 grid of 6 scenarios (Option pricing, Risk management, Retirement planning, etc.) using Monte Carlo.

### EP18-07：常见误区图
**文件名**：`images/ep18/ep18_mistakes.jpg`
**Prompt**：2x2 grid showing mistakes like "Garbage in, garbage out" (wrong volatility assumptions) or insufficient simulation runs.

### EP18-08：SOP流程图
**文件名**：`images/ep18/ep18_sop.jpg`
**Prompt**：5-step flowchart for running a Monte Carlo simulation in Python/Excel.

---

## 第19篇《破产风险：赌徒破产问题与资金管理》

### EP19-01：封面图
**文件名**：`images/ep19/ep19_cover_ruin.jpg`
**Prompt**：Title: "第19篇：破产风险". Center: A dramatic infinite corridor representing random walk, with a massive red abyss labeled "破产线=0".

### EP19-02：核心公式解析
**文件名**：`images/ep19/ep19_formula.jpg`
**Prompt**：Gambler's ruin formula breakdown. Showing probability of ruin based on win rate (p) and bankroll (N).

### EP19-03：四大类比图
**文件名**：`images/ep19/ep19_analogy.jpg`
**Prompt**：Analogy of walking on a tightrope near a cliff vs far from a cliff. Distance to cliff = Capital buffer.

### EP19-04：实战推演图（不同仓位的破产概率）
**文件名**：`images/ep19/ep19_simulation.jpg`
**Prompt**：A table/chart comparing 3 traders with 60% win rate but different bet sizes (50%, 20%, 5%). Showing the 50% bettor hitting 0.

### EP19-05：量化大师图
**文件名**：`images/ep19/ep19_masters.jpg`
**Prompt**：Victor Niederhoffer case study (blew up twice) vs Paul Tudor Jones (strict stop losses).

### EP19-06：实战场景图
**文件名**：`images/ep19/ep19_scenarios.jpg`
**Prompt**：2x3 grid showing 6 ways to prevent ruin (Capital sizing, Stop losses, Diversification, etc.).

### EP19-07：错误与SOP图
**文件名**：`images/ep19/ep19_mistakes_sop.jpg`
**Prompt**：Combined chart. Left: Fatal mistakes (Martingale strategy). Right: 4-step SOP to ensure zero ruin risk.

---

## 第20篇《最大回撤与资金恢复时间：衡量策略韧性》

### EP20-01：封面图
**文件名**：`images/ep20/ep20_cover_drawdown.jpg`
**Prompt**：Title: "第20篇：最大回撤与恢复时间". Center: A chart dropping deep into a red valley and slowly climbing back out, with a phoenix silhouette.

### EP20-02：回撤数学机制
**文件名**：`images/ep20/ep20_math_asymmetry.jpg`
**Prompt**：A stark mathematical table showing loss vs required gain to recover (e.g. -50% requires +100%, -90% requires +900%). Red to green gradient.

### EP20-03：类比图（深坑与爬坑）
**文件名**：`images/ep20/ep20_analogy.jpg`
**Prompt**：Analogy of falling into a pit. The deeper the pit, the exponentially harder it is to climb out due to gravity (compounding math).

### EP20-04：真实回撤案例（伯克希尔哈撒韦）
**文件名**：`images/ep20/ep20_berkshire_mdd.jpg`
**Prompt**：Historical chart of Berkshire Hathaway showing its 50% drawdowns, emphasizing that even the best suffer MDD.

### EP20-05：卡尔玛比率解析图
**文件名**：`images/ep20/ep20_calmar_ratio.jpg`
**Prompt**：Formula breakdown for Calmar Ratio = Annual Return / Max Drawdown. Visualizing risk-adjusted returns.

### EP20-06：实战场景与误区
**文件名**：`images/ep20/ep20_scenarios.jpg`
**Prompt**：2x3 grid on setting drawdown limits, psychological thresholds, and the mistake of holding during a 60% drawdown.

### EP20-07：SOP流程图（回撤管控机制）
**文件名**：`images/ep20/ep20_sop.jpg`
**Prompt**：Flowchart for managing drawdowns dynamically (e.g. at -10% halve position size, at -20% stop trading).

---

## 第21篇《主动管理定律：信息比率与预测宽度的乘积》

### EP21-01：封面图
**文件名**：`images/ep21/ep21_cover_fundamental_law.jpg`
**Prompt**：Title: "第21篇：主动管理定律". Subtitle: "IR ≈ IC × √BR". Center: A glowing mathematical scale balancing skill (IC) and breadth (BR).

### EP21-02：公式拆解
**文件名**：`images/ep21/ep21_formula.jpg`
**Prompt**：Infographic decomposing IR (Information Ratio), IC (Information Coefficient), and BR (Breadth). Gold and cyan highlights.

### EP21-03：生活类比（狙击手与机枪手）
**文件名**：`images/ep21/ep21_analogy.jpg`
**Prompt**：Analogy: Sniper (High IC, Low BR) vs Machine Gunner (Low IC, High BR). Both can achieve the same target suppression (IR).

### EP21-04：实战推演（量化如何战胜主观）
**文件名**：`images/ep21/ep21_quant_vs_discretionary.jpg`
**Prompt**：Table comparing a human stock picker (IC=0.15, BR=20) vs a Quant algorithm (IC=0.03, BR=2000). Quant wins due to sqrt(BR).

### EP21-05：大师图（Grinold & Kahn）
**文件名**：`images/ep21/ep21_masters.jpg`
**Prompt**：Portraits of Richard Grinold and Ronald Kahn. Quote about the Fundamental Law of Active Management.

### EP21-06：六大场景图
**文件名**：`images/ep21/ep21_scenarios.jpg`
**Prompt**：2x3 grid applying the law to HFT, multi-factor models, and retail trading.

### EP21-07：常见错误与SOP
**文件名**：`images/ep21/ep21_mistakes_sop.jpg`
**Prompt**：Mistake: Forcing high frequency without skill. SOP: How to improve IC or increase BR effectively.

---

## 第22篇《B-S 期权定价模型：金融工程的皇冠》

### EP22-01：封面图
**文件名**：`images/ep22/ep22_cover_black_scholes.jpg`
**Prompt**：Title: "第22篇：B-S 期权定价模型". Center: The iconic Black-Scholes partial differential equation glowing in gold over a futuristic derivatives market.

### EP22-02：五大变量解析
**文件名**：`images/ep22/ep22_variables.jpg`
**Prompt**：A pentagon diagram breaking down the 5 inputs: S(Price), K(Strike), T(Time), r(Rate), σ(Volatility).

### EP22-03：四大类比（保险定价）
**文件名**：`images/ep22/ep22_analogy.jpg`
**Prompt**：Analogy of pricing car insurance. Volatility = Bad driving record. Time = Policy length.

### EP22-04：希腊字母图谱
**文件名**：`images/ep22/ep22_greeks.jpg`
**Prompt**：A dashboard showing Delta, Gamma, Theta, Vega, Rho with their mechanical equivalents (Speedometer, Acceleration, Melting ice).

### EP22-05：大师图（Black, Scholes, Merton）
**文件名**：`images/ep22/ep22_masters.jpg`
**Prompt**：Portraits of Myron Scholes and Robert Merton (Nobel winners) and Fischer Black.

### EP22-06：波动率微笑（Volatility Smile）
**文件名**：`images/ep22/ep22_vol_smile.jpg`
**Prompt**：Chart showing implied volatility smile. Exposing the flaw of BS model (assuming constant volatility).

### EP22-07：实战SOP与错误
**文件名**：`images/ep22/ep22_sop_mistakes.jpg`
**Prompt**：Mistakes: Ignoring implied volatility crush. SOP: How to use Delta-hedging.

---

## 第23篇《行为金融学数学化：前景理论与损失厌恶》

### EP23-01：封面图
**文件名**：`images/ep23/ep23_cover_behavioral.jpg`
**Prompt**：Title: "第23篇：行为金融学数学化". Center: The asymmetric S-shaped Value Function curve from Prospect Theory.

### EP23-02：价值函数解析
**文件名**：`images/ep23/ep23_value_function.jpg`
**Prompt**：Detailed graph of the value function. Showing losses hurt 2.25x more than gains feel good.

### EP23-03：四大类比（沸水煮青蛙与丢钱）
**文件名**：`images/ep23/ep23_analogy.jpg`
**Prompt**：Visuals of losing $100 vs finding $100, showing emotional asymmetry.

### EP23-04：概率权重函数（彩票偏差）
**文件名**：`images/ep23/ep23_probability_weighting.jpg`
**Prompt**：Graph showing how humans overweight 1% probabilities (lottery) and underweight 99% probabilities.

### EP23-05：大师图（卡尼曼与特沃斯基）
**文件名**：`images/ep23/ep23_masters.jpg`
**Prompt**：Portraits of Daniel Kahneman (Nobel winner) and Amos Tversky.

### EP23-06：实战收割机（量化如何利用散户偏差）
**文件名**：`images/ep23/ep23_quant_harvest.jpg`
**Prompt**：Diagram showing Momentum exploiting Disposition Effect, and Mean Reversion exploiting Overreaction.

### EP23-07：反直觉SOP与克服人性
**文件名**：`images/ep23/ep23_sop.jpg`
**Prompt**：Flowchart for systematic trading to bypass human emotion (Automated stop losses, trailing stops).
"""

file_path = "/Users/lili/.gemini/antigravity/brain/d493099f-783d-4b86-9462-011f05b21b68/docs/image_prompts_backup.md"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace from line 371 onwards
lines = content.split('\n')
new_content = '\n'.join(lines[:370]) + '\n' + prompts_content

with open(file_path, "w", encoding="utf-8") as f:
    f.write(new_content)
print("Updated image_prompts_backup.md successfully.")
