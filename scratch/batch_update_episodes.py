import os
import re

EPISODES_DIR = "episodes"

def get_episodes():
    files = [f for f in os.listdir(EPISODES_DIR) if f.startswith("第") and f.endswith(".md")]
    files.sort()
    return files

episodes = get_episodes()

NAV_BLOCK = """
## 🔗 完整系列导航

<details>
<summary>点击展开查看全系列 25 篇文章目录</summary>

### 🧱 第一模块：地基篇 — 概率与期望思维
- [第01篇：凯利公式_仓位管理的黄金法则](./第01篇_凯利公式_仓位管理的黄金法则.md)
- [第02篇：期望值理论_所有决策的基石](./第02篇_期望值理论_所有决策的基石.md)
- [第03篇：大数定律_时间是你最好的朋友](./第03篇_大数定律_时间是你最好的朋友.md)
- [第04篇：中心极限定理_分散投资的数学证明](./第04篇_中心极限定理_分散投资的数学证明.md)
- [第05篇：复利定律_财富的雪球效应](./第05篇_复利定律_财富的雪球效应.md)

### 🔭 第二模块：选机会篇 — 识别高概率交易
- [第06篇：均值回归_市场的钟摆定律](./第06篇_均值回归_市场的钟摆定律.md)
- [第07篇：动量效应_顺势而为的数学依据](./第07篇_动量效应_顺势而为的数学依据.md)
- [第08篇：贝叶斯推断_实时更新你的判断](./第08篇_贝叶斯推断_实时更新你的判断.md)
- [第09篇：安全边际_价值投资的概率护城河](./第09篇_安全边际_价值投资的概率护城河.md)
- [第10篇：因子投资_系统性超越市场的秘密](./第10篇_因子投资_系统性超越市场的秘密.md)

### ⚖️ 第三模块：配置篇 — 资产组合与仓位管理
- [第11篇：现代投资组合理论_有效前沿的边界](./第11篇_现代投资组合理论_有效前沿的边界.md)
- [第12篇：夏普比率_策略质量的标准尺](./第12篇_夏普比率_策略质量的标准尺.md)
- [第13篇：风险平价策略_穿越经济周期的秘密](./第13篇_风险平价策略_穿越经济周期的秘密.md)
- [第14篇：最优仓位管理_Optimal-f_凯利公式的工程级进化](./第14篇_最优仓位管理_Optimal-f_凯利公式的工程级进化.md)
- [第15篇：相关性与分散化_降低风险的数学奥秘](./第15篇_相关性与分散化_降低风险的数学奥秘.md)

### 🛡️ 第四模块：风控篇 — 极端状态下的生死局
- [第16篇：VaR风险价值_如何量化你能承受的最大亏损](./第16篇_VaR风险价值_如何量化你能承受的最大亏损.md)
- [第17篇：黑天鹅事件_极端风险的数学本质](./第17篇_黑天鹅事件_极端风险的数学本质.md)
- [第18篇：蒙特卡洛模拟_用随机数预测未来](./第18篇_蒙特卡洛模拟_用随机数预测未来.md)
- [第19篇：破产风险_赌徒破产问题与资金管理](./第19篇_破产风险_赌徒破产问题与资金管理.md)
- [第20篇：最大回撤与资金恢复时间_衡量策略韧性](./第20篇_最大回撤与资金恢复时间_衡量策略韧性.md)

### 🔬 第五模块：量化进阶篇 — 升华与融合
- [第21篇：主动管理定律_信息比率与预测宽度的乘积](./第21篇_主动管理定律_信息比率与预测宽度的乘积.md)
- [第22篇：B-S期权定价模型_金融工程的皇冠](./第22篇_B-S期权定价模型_金融工程的皇冠.md)
- [第23篇：行为金融学数学化_前景理论与损失厌恶](./第23篇_行为金融学数学化_前景理论与损失厌恶.md)
- [第24篇：投资组合理论大融合_打造你的全天候财富机器](./第24篇_投资组合理论大融合_打造你的全天候财富机器.md)
- [第25篇：终章_数学的尽头是哲学_概率的尽头是人生](./第25篇_终章_数学的尽头是哲学_概率的尽头是人生.md)

</details>

---
"""

transitions = {
    1: "如果你已经懂了凯利公式如何帮你避免一次性破产，你必然会问：在每次下注前，我怎么知道盈亏比是否划算？下一篇，我们将进入所有决策的基石——期望值理论。",
    2: "当我们知道了如何计算一次抛硬币的期望值后，另一个问题接踵而至：如果你抛 1000 次硬币，结果会完全按照期望值走吗？下一篇，我们将揭示赌场老板永远不怕你的终极护身符——大数定律。",
    3: "大数定律告诉我们时间是好朋友。但如果在长期中，你的资产被几种极度不同的力量来回拉扯，最终会形成怎样的分布形态？下一篇，我们将见证数学界最奇妙的魔法——中心极限定理与正态分布的诞生。",
    4: "明白了正态分布后，我们知道了世界是由概率组成的。那么，当我们把这套概率体系放到时间轴上，利滚利地无限滚动下去时，会发生怎样的剧变？下一篇，我们将见识真正的财富核武器——复利定律。",
    5: "复利需要时间，但更需要不被打断的平稳环境。然而，市场永远处于疯狂的钟摆运动中。如何利用市场的狂热与绝望来加速复利？下一篇，我们将进入择时篇的核心——均值回归。",
    6: "既然均值回归告诉我们跌多了必涨，那为什么有些股票跌了之后还能跌去 90%？在趋势面前逆势接飞刀是极其危险的。下一篇，我们将揭秘均值回归的反面，也是华尔街最赚钱的因子——动量效应。",
    7: "如果动量效应告诉你顺势而为，但明天突发一个巨大的利空新闻，你该不该立刻改变策略？在不断涌现的新信息面前，固执己见是致命的。下一篇，我们将学习如何像机器一样动态调整认知——贝叶斯推断。",
    8: "无论是贝叶斯还是动量，它们都需要一个极其重要的底线：你要买的东西，其内生价值究竟在哪？如果没有这个底座，所有的计算都是空中楼阁。下一篇，我们将深入价值投资的概率护城河——安全边际。",
    9: "当我们有了安全边际的概念，并在市场上找到了几只看似便宜的股票后，如何把这种选股能力系统化、批量化？下一篇，我们将探讨华尔街量化基金批量印钞的核心机密——因子投资与多因子模型。",
    10: "到目前为止，我们一直在教你如何“挑选好机会”。但是，就算你选出了一批最好的好股票，如果把它们全塞在一起，就能高枕无忧了吗？下一篇，我们将迈入投资界真正的诺贝尔奖基石——现代投资组合理论。",
    11: "马科维茨教了我们如何画出有效前沿，但面对这条曲线上无数个点，我们究竟该选哪一个才是最高效的？下一篇，我们将引出衡量策略性价比的最强黄金尺——夏普比率。",
    12: "夏普比率告诉我们要在收益和波动之间寻找平衡。然而，为什么经典的股债组合在2008年依然遭遇了毁灭性打击？当股票的波动率远超债券时，我们该如何构建真正坚不可摧的桥水基金模型？下一篇，我们将揭示跨越宏观周期的秘密——风险平价策略。",
    13: "如果你已经拥有了完美的资产底盘（风险平价），当你想要在某个资产上加大火力时，你该如何精确计算下注比例？凯利公式在这里显得过于粗糙。下一篇，我们将进入凯利公式的终极工业级进化——最优仓位管理 Optimal-f。",
    14: "我们计算出了最精确的仓位，但如果你的资产池里两只股票总是同涨同跌，你的最优仓位依然会瞬间失效。要彻底锁死风险，我们必须找到降低颠簸的数学密码。下一篇，我们将深度解剖投资界唯一的免费午餐——相关性与分散化。"
}

for idx, filename in enumerate(episodes):
    filepath = os.path.join(EPISODES_DIR, filename)
    ep_num = idx + 1
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Strip the old data source lines
    # This removes anything starting with "*数据来源" or "* 数据来源" at the end of the file.
    lines = content.split('\n')
    filtered_lines = []
    for line in lines:
        if re.match(r'^\*\s*数据来源.*', line):
            continue
        filtered_lines.append(line)
    
    content = '\n'.join(filtered_lines)
    
    # 2. Add transition if missing and if we have one defined (EP01 to EP14)
    # Check if a transition already exists. A simple check: if the text of the transition is in the file.
    if ep_num in transitions:
        trans_text = transitions[ep_num]
        if trans_text not in content:
            # Insert just before the ## 🔗 系列导航 (or similar) section
            nav_pattern = r'\n## 🔗'
            if re.search(nav_pattern, content):
                content = re.sub(nav_pattern, f"\n\n{trans_text}\n\n## 🔗", content)
            else:
                # If no nav pattern found, just append
                content += f"\n\n{trans_text}\n"

    # 3. Replace the old nav block with the new full nav block
    # We find where "## 🔗 " starts and replace everything from there to the end.
    match = re.search(r'\n## 🔗.*', content, flags=re.DOTALL)
    
    # Generate previous / next links
    prev_link = f"**← 上一篇：[{episodes[ep_num-2].split('_')[1]}](./{episodes[ep_num-2]})**" if ep_num > 1 else ""
    next_link = f"**→ 下一篇：[{episodes[ep_num].split('_')[1]}](./{episodes[ep_num]})**" if ep_num < len(episodes) else ""
    
    if prev_link and next_link:
        nav_links = f"{prev_link} | {next_link}"
    else:
        nav_links = prev_link + next_link
        
    final_nav = NAV_BLOCK + nav_links + f"\n\n---\n*《股票市场的数学原理》全系列 · 第{ep_num:02d}篇*\n"
    
    if match:
        content = content[:match.start()] + "\n" + final_nav
    else:
        content += "\n" + final_nav
        
    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Updated all 25 episodes successfully!")
