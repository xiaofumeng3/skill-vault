---
name: train-test-split
description: |
  应用从 AI for Everyone 蒸馏出的「训练集/测试集分离 — AI的'科学方法」方法论。Use when the user needs practical guidance, diagnosis, workflow design, decision support, or an action plan related to train-test-split.
---

## Source Metadata

Original cangjie-skill frontmatter from the distillation run:

```yaml
id: f17
title: "训练集/测试集分离 — AI的'科学方法'"
book: "AI for Everyone"
author: "Andrew Ng（吴恩达）"
source: p16
tags: [machine-learning, evaluation, testing, collaboration]
related_skills:
  - slug: ml-workflow, relation: depends-on
  - slug: statistical-acceptance, relation: composes-with
```

## R — Reading（原文引用）

> "AI团队将数据分为两个主要数据集，第一个称为训练集，第二个称为测试集"
> — p16

## I — Interpretation（用自己的话重新阐述）

就像学生如果只背过去的考试题，遇到新题就会考砸一样——AI模型如果用训练数据来评估自己，表现会比实际好得多。

**解决方案**：将数据分成两个**互不重叠**的集合：

1. **训练集**：喂给算法学习，让模型从中发现规律。
2. **测试集**：完全"藏起来"，仅在最终评估时使用，用来衡量模型在**未见过的数据**上的表现。

如果不预留测试集，你就无法知道模型是真的学会了规律，还是只是"记住"了训练样本。测试集就是AI的"科学实验对照组"——它告诉你模型是否真正具备泛化能力。

## A1 — Past Application（过去应用案例）

- **咖啡杯缺陷检测**：收集10000张咖啡杯图片（有缺陷/无缺陷），分为训练集（8000张）和测试集（2000张）。用训练集教模型识别缺陷，最后用测试集评估——模型在2000张未见过的图片上达到95%准确率。这个95%才是模型真实能力的可信度量。

## A2 — Future Trigger（未来触发条件）

**触发场景**：
- 团队报告了一个很高的准确率，但你想知道是否可信
- 开始一个新ML项目，需要设计评估方案
- 业务方质疑"这个AI到底好不好用"

**语言信号**：
- "AI准确率多少？"
- "怎么知道AI好不好？"
- "如何评估模型？"
- "准确率是多少？"
- "测试结果怎么样？"
- "效果评估怎么做？"

**区分要点**：当需要判断一个AI模型的真实能力（而非表面数字）时，使用本框架。

## E — Execution（执行步骤）

1. **确保数据已分割**：检查标注数据是否被分为训练集和测试集，且两者**没有重叠**。测试集在训练过程中绝不能被模型"看到"。
2. **训练前定义验收标准**：在开始训练前就确定目标（如"测试集准确率达到95%"），避免训练后随意调整标准。
3. **仅在最终评估时使用测试集**：训练过程中不要用测试集来做任何决策（如调参、选模型）。测试集只能用一次——最终评估。
4. **报告测试集结果**：向利益相关者汇报的是测试集上的表现，而非训练集上的表现。

**完成标准**：模型在从未见过的测试集上达到了预定义的验收标准，且测试集在整个训练过程中未被污染。

## B — Boundary（使用边界）

**不适用场景**：
- 数据科学项目（没有需要评估的模型）
- 数据量极少的情况（无法留出有意义的测试集）
- 探索性分析阶段（还没有进入建模）

**失败模式**：
- 用测试集调参：反复在测试集上评估并调整，实际上等于"泄露"了测试集信息
- 训练集和测试集有重叠：导致评估结果虚高
- 测试集分布与真实场景不符：测试集表现好但上线后表现差

**作者盲区**：
- Andrew Ng只讲了训练集/测试集的二分法，但实际项目中通常需要**三个集合**：训练集（训练）、开发集/验证集（调参和模型选择）、测试集（最终评估）。如果团队只有一个测试集并反复在上面调参，会导致对真实性能的估计偏差。对于严肃的ML项目，建议引入第二个"隐藏"测试集。

## 相关 skills

- **[ml-workflow](/books/ai-for-everyone/ml-workflow/)** — *depends-on*：训练集/测试集分离是ML工作流中的关键步骤，需要先理解整体工作流才能正确执行数据分割。
- **[statistical-acceptance](/books/ai-for-everyone/statistical-acceptance/)** — *composes-with*：测试集上的准确率结果需要配合统计化验收标准来定义"什么算够好"，两者结合使用才能建立完整的评估体系。
