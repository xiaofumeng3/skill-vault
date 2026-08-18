---
name: ml-vs-ds
description: |
  应用从 AI for Everyone 蒸馏出的「ML产出软件,DS产出洞察 — 项目类型判定框架」方法论。Use when the user needs practical guidance, diagnosis, workflow design, decision support, or an action plan related to ml-vs-ds.
---

## Source Metadata

Original cangjie-skill frontmatter from the distillation run:

```yaml
id: f27
title: "ML产出软件,DS产出洞察 — 项目类型判定框架"
book: "AI for Everyone"
author: "Andrew Ng（吴恩达）"
source: p04, p11, p12
tags: [scoping, machine-learning, data-science, project-management]
related_skills:
  - slug: ml-workflow
    relation: contrasts-with
  - slug: ab-mapping
    relation: depends-on
```

## R — Reading（原文引用）

> "机器学习项目通常会生成一个能够运行并输出结果的软件...数据科学项目的输出通常是演示文稿"
> — p04

## I — Interpretation（用自己的话重新阐述）

机器学习和数据科学是两种根本不同的工作模式：

1. **机器学习（ML）**：产出是**持续运行的软件**，能反复做出预测和判断。例如：垃圾邮件过滤器、推荐系统、缺陷检测器。
2. **数据科学（DS）**：产出是**洞察或建议**，通常以报告或PPT形式呈现，用于支持一次性商业决策。例如：说服旅游公司购买更多广告的市场分析。

两者输出不同 → 所需团队技能不同 → 成功指标不同 → 项目流程也不同。混淆这两种项目类型，是AI项目失败最常见的原因之一。

## A1 — Past Application（过去应用案例）

- **在线广告投放系统（ML）**：构建一个24小时运行的软件，实时预测用户点击率（CTR），自动决定展示哪条广告。
- **广告策略分析（DS）**：分析师通过数据挖掘发现"旅游公司在平台投放不足"，制作一份PPT并向高管汇报，说服旅游公司增加投放。这是一个一次性决策建议，不需要部署软件。

## A2 — Future Trigger（未来触发条件）

**触发场景**：
- 团队讨论一个AI想法时，争论"这到底是个什么项目"
- 老板问"这个项目最终要交付什么东西"
- 招聘时纠结"我要招ML工程师还是数据分析师"

**语言信号**：
- "我们该做ML还是DS？"
- "这个项目该产出什么？"
- "是建系统还是做分析？"
- "做系统还是做报告？"
- "机器学习项目还是数据科学项目？"

**区分要点**：关键问一个问题——**最终产出是持续运行的软件，还是一份决策建议？**

## E — Execution（执行步骤）

1. **明确期望结果**：问利益相关者——最终想要的是一个能持续运行的软件，还是一个决策建议？
2. **如果答案是软件** → 走ML工作流：收集数据 → 训练模型 → 部署上线 → 持续迭代。
3. **如果答案是建议** → 走DS工作流：收集数据 → 分析探索 → 形成假设 → 制作报告/PPT。
4. **确认团队技能匹配**：ML项目需要ML工程师；DS项目需要数据分析师/业务分析师。

**完成标准**：团队对"我们做的是ML还是DS"达成共识，并匹配了正确的流程和人才。

## B — Boundary（使用边界）

**不适用场景**：
- 项目同时包含DS和ML元素（常见情况——先用DS发现洞察，再基于洞察构建ML系统）
- 纯学术研究项目
- 探索性调研（还没有明确产出目标）

**失败模式**：
- 把DS当ML做：花大力气建系统，但业务只需要一份报告
- 把ML当DS做：做完PPT就结束，没有部署软件，无法持续产生价值

**作者盲区**：
- Andrew Ng将ML和DS的边界描述得比实际情况更清晰。现实中很多项目**混合了两者**——先用DS找到机会，再用ML落地执行。不要因为无法清晰分类而卡住，关键是识别项目**当前阶段**的主要产出形式。

## 相关 skills
- **ml-workflow** (contrasts-with): ML工作流是"建系统"的流程,DS产出报告而非软件,两者流程截然不同
- **ab-mapping** (depends-on): 判定为ML项目后,需要进一步用A→B映射定义输入输出
