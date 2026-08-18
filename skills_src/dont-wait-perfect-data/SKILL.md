---
name: dont-wait-perfect-data
description: |
  应用从 AI for Everyone 蒸馏出的「不等完美数据 — 先用起来再迭代」方法论。Use when the user needs practical guidance, diagnosis, workflow design, decision support, or an action plan related to dont-wait-perfect-data.
---

## Source Metadata

Original cangjie-skill frontmatter from the distillation run:

```yaml
id: f22
title: "不等完美数据 — 先用起来再迭代"
book: "AI for Everyone"
author: "Andrew Ng（吴恩达）"
source: p18, p20
tags: [data-strategy, execution, iteration, pragmatism]
related_skills:
  - slug: unified-data-warehouse, relation: composes-with
  - slug: data-flywheel, relation: composes-with
```

## R — Reading（原文引用）

> "不要等待完美的数据才开始...数据不需要完美，只要足够好就可以开始"
> — p18

## I — Interpretation（用自己的话重新阐述）

追求"完美数据"是AI项目最常见的拖延借口。很多团队花了数月甚至数年在数据准备上，迟迟不进入建模阶段。

**核心理念**：数据不需要完美，**足够好**就可以开始。原因：

1. **AI系统对噪声有鲁棒性**：现代ML算法可以处理一定程度的噪声和不完美数据。
2. **早期反馈更有价值**：用一个"不够完美"的模型跑起来，获得的真实反馈比在空想中完善数据更有价值。
3. **数据改进是持续过程**：模型上线后，用户反馈和数据飞轮会自然推动数据质量的提升。
4. **完美是好的敌人**：追求完美数据会导致项目永远无法启动。

**正确做法**：定义"足够好"的门槛（标注一致性达到80%、覆盖主要场景、没有系统性偏差），达到门槛就开始建模，后续持续迭代数据质量。

## A1 — Past Application（过去应用案例）

- **Bing搜索引擎**：早期搜索数据远不如Google丰富，但Bing没有等到"数据赶上Google"才开始，而是用现有数据启动，通过用户交互逐步改进。虽然至今数据量仍不如Google，但已经是一个可用的产品——如果当年等待完美数据，Bing永远不会上线。

## A2 — Future Trigger（未来触发条件）

**触发场景**：
- 团队说"数据还没准备好"，项目一直无法启动
- 数据清洗工作已经持续了很长时间但没有明确终点
- 业务方要求"数据100%准确"才能开始建模

**语言信号**：
- "数据还没准备好"
- "再等等，数据还不够"
- "数据质量不行"
- "等数据完善了再说"
- "先做数据治理"

**区分要点**：当团队因为数据质量问题而**推迟启动**时，使用本框架来推动"先用起来"。

## E — Execution（执行步骤）

1. **定义"足够好"的门槛**：与AI团队协商，明确数据质量的最低可接受标准（如标注一致性≥80%、覆盖核心场景、无系统性偏差）。
2. **评估当前数据状态**：检查现有数据是否已达到"足够好"的门槛。
3. **如果达到门槛 → 立即开始建模**：不要继续等待，用现有数据训练第一个模型。
4. **如果未达到 → 做最小必要改进**：只修复最严重的问题，达到门槛后立即开始。
5. **上线后持续迭代**：通过用户反馈和数据飞轮持续改进数据质量。

**完成标准**：团队在数据达到"足够好"门槛后立即启动了建模工作，没有无期限等待。

## B — Boundary（使用边界）

**不适用场景**：
- 数据存在系统性偏差（如训练数据与真实场景分布完全不同）
- 安全关键场景（医疗、航空——数据质量直接关系生命安全）
- 法律合规要求数据必须准确的领域

**失败模式**：
- 用"不等完美"掩盖懒惰：不是"不等完美"而是"完全不准备"
- 忽视系统性偏差：数据有噪声可以接受，但系统性偏差会导致模型学到错误规律
- 永远不回头改进：启动后就把"数据改进"忘得一干二净

**作者盲区**：
- Andrew Ng没有明确定义"足够好"的量化标准——这需要结合具体业务场景来判断。建议团队在启动前明确写出"我们认为数据已经足够好的三个理由"，避免主观臆断。

## 相关 skills

- **[unified-data-warehouse](/books/ai-for-everyone/unified-data-warehouse/)** — *composes-with*：不等完美数据的心态与统一数据仓库的建设相辅相成——先有基本的数据汇聚就能启动，后续持续完善数据仓库。
- **[data-flywheel](/books/ai-for-everyone/data-flywheel/)** — *composes-with*：飞轮冷启动阶段特别需要"不等完美数据"的心态——先用不完美的数据启动产品，飞轮转起来后数据自然越来越好。
