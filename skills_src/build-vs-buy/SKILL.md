---
name: build-vs-buy
description: |
  应用从 AI for Everyone 蒸馏出的「不在火车前冲刺 — AI自建vs购买决策框架」方法论。Use when the user needs practical guidance, diagnosis, workflow design, decision support, or an action plan related to build-vs-buy.
---

## Source Metadata

Original cangjie-skill frontmatter from the distillation run:

```yaml
id: f16
title: "不在火车前冲刺 — AI自建vs购买决策框架"
book: "AI for Everyone"
author: "Andrew Ng"
source: p15, p17
tags: [build-vs-buy, strategy, resource-allocation, platform]
related_skills:
  - slug: ai-strategy-moat, relation: depends-on
  - slug: triple-due-diligence, relation: composes-with
```

## R — 原文引用 (Reading)

> "不要在火车前冲刺...如果存在一家公司在构建行业标准方案，则应避免不断加速以领先于火车...最好接受行业标准方案。"（p15）

## I — 解读 (Interpretation)

"火车"隐喻：当一个技术组件正在成为行业标准（一个开源项目、一款创业公司产品、一个大型平台功能），你不可能比整个市场投入更多资源去自研。火车终将追上并碾压你的专有方案。

决策规则：
- **正在成为行业标准** → 购买/采用。不要试图跑赢火车。
- **真正独特于你业务、能创造竞争优势** → 自建。这是值得投入的差异化工作。

核心原则：将有限的工程资源**只集中在能带来差异化**的工作上。对于正在标准化的组件，接受行业标准方案，把省下来的精力投入到真正独特的业务价值中。

## A1 — 过往应用 (Past Application)

**案例 1：自建云计算基础设施**
许多大公司曾投入巨资自建数据中心和云平台，试图与 AWS/Azure/GCP 竞争。结果：这些"火车"（三大云厂商）投入了数十亿美元，任何单一企业都无法匹敌。最终这些公司纷纷转向采用公有云——接受行业标准方案。

**案例 2：自建机器学习框架**
一些团队曾自研深度学习框架，试图追赶 TensorFlow/PyTorch。但这两个框架背后有整个开源社区和巨头公司的持续投入，自研框架很难跟上迭代速度。明智的团队选择采用开源框架，将精力集中在用框架解决业务问题上。

## A2 — 未来触发 (Future Trigger)

**触发场景：**
- 团队讨论"这个组件该自建还是购买"
- 技术选型会议中争论"要不要自己造轮子"
- 评估外部供应商方案 vs 内部研发

**语言信号：**
- "自建"、"购买"、"外部方案"、"供应商"、"第三方"、"造轮子"、"行业标准"

**关键区分：**
- 该组件是**正在标准化**（多个供应商/开源项目趋同）还是**仍然独特**（只有你或少数人在做）？
- 该组件是你的**核心差异化来源**还是**基础设施**？

## E — 执行 (Execution)

1. **判断行业标准趋势**：该组件是否正在成为行业标准？（检查：是否有创业公司、开源项目或大公司正在趋同于同一解决方案？）
2. **如果是 → 采用标准**：不要自建，选择行业领先方案，将资源释放给差异化工作。
3. **如果否 → 评估差异化价值**：该组件是否真正独特于你的业务、能创造竞争优势？如果是，投入资源自建。
4. **定期复审**：行业标准格局会变化，每 6-12 个月重新评估决策。

**完成标准：** 对每个候选组件完成"自建/购买"决策，并明确记录决策理由和复审时间。

## B — 边界 (Boundary)

**不适用场景：**
- 核心差异化组件（这些**应该**自建，不要用此框架否定它们）
- 琐碎的日常决策（不值得用这个框架分析）
- 早期探索阶段（还没有足够信息判断趋势）

**失败模式：**
- 误将"正在标准化"的组件当作差异化机会投入自研
- 误将"真正独特"的组件外包，丧失竞争优势
- 过度依赖外部供应商导致供应商锁定（vendor lock-in）

**作者盲点：**
- "行业标准"往往**只有在事后**才能清晰判断——实时决策时很难确定某个方案是否会成为标准。需要结合市场信号（融资、社区活跃度、大厂动向）做最佳判断，但保持谦逊：你可能看错。

## 相关 skills

- **[ai-strategy-moat](/books/ai-for-everyone/ai-strategy-moat/)** — *depends-on*：判断"什么值得自建"需要先理解AI竞争壁垒的理论，自建决策应服务于构建持久竞争优势。
- **[triple-due-diligence](/books/ai-for-everyone/triple-due-diligence/)** — *composes-with*：购买决策需要进行技术、供应商、合规三个维度的尽职调查，与自建/购买决策框架配合使用。
