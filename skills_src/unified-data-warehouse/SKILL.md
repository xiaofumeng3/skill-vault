---
name: unified-data-warehouse
description: |
  应用从 AI for Everyone 蒸馏出的「统一数据仓库 — AI的数据基础设施」方法论。Use when the user needs practical guidance, diagnosis, workflow design, decision support, or an action plan related to unified-data-warehouse.
---

## Source Metadata

Original cangjie-skill frontmatter from the distillation run:

```yaml
id: f23
title: "统一数据仓库 — AI的数据基础设施"
book: "AI for Everyone"
author: "Andrew Ng（吴恩达）"
source: p18, p19
tags: [data-infrastructure, data-warehouse, data-strategy, platform]
related_skills:
  - slug: data-flywheel, relation: depends-on
  - slug: dont-wait-perfect-data, relation: composes-with
```

## R — Reading（原文引用）

> "将所有数据整合到一个中央数据仓库中...这通常是AI转型中最重要的第一步"
> — p18

## I — Interpretation（用自己的话重新阐述）

很多公司的数据散落在各个业务系统中——CRM一个库、ERP一个库、网站日志一个库、APP数据一个库——彼此隔离，无法形成合力。

**统一数据仓库的核心价值**：

1. **打破数据孤岛**：将分散在各系统的数据汇聚到一个平台，让AI团队能访问全量数据。
2. **支持数据飞轮**：飞轮需要用户行为数据持续汇聚，统一仓库是飞轮的基础设施。
3. **避免重复建设**：每个业务线不用各自搭建数据管道，统一建设更高效。
4. **保证数据一致性**：同一套数据定义和口径，避免不同部门对同一个指标有不同数字。

**注意**：统一数据仓库是一个**长期工程**，可能需要1-2年才能完成。不要等到仓库完美才启动AI项目。

## A1 — Past Application（过去应用案例）

- **大型零售企业**：将线上商城、线下门店、供应链、客服系统的数据整合到统一数据仓库。AI团队基于此构建了需求预测模型——如果数据还在各系统孤岛中，这个模型根本无法训练，因为需要同时用到销售、库存、物流数据。

## A2 — Future Trigger（未来触发条件）

**触发场景**：
- AI团队抱怨"数据拿不到"或"数据散落在各处"
- 公司想做AI但不知道数据在哪里
- 不同部门对同一个业务指标有不同数字
- 需要构建数据飞轮但数据汇聚是瓶颈

**语言信号**：
- "数据孤岛"
- "数据散落"
- "统一数据"
- "数据仓库"
- "数据汇聚"
- "数据整合"
- "数据中台"

**区分要点**：当AI项目的瓶颈是**数据可访问性**（数据存在但拿不到）时，使用本框架。

## E — Execution（执行步骤）

1. **盘点数据资产**：梳理公司所有数据源——业务系统、日志、第三方数据等。
2. **设计数据架构**：确定数据仓库的技术选型（云数仓如Snowflake/BigQuery，或自建）。
3. **制定数据标准**：统一指标定义、数据格式、命名规范。
4. **分批接入数据源**：按优先级逐步将各系统数据接入仓库，不必等全部完成。
5. **建立数据治理**：明确数据所有权、访问权限、质量责任。
6. **赋能AI团队**：确保AI团队能方便地访问和使用仓库中的数据。

**完成标准**：核心业务数据已接入统一数据仓库，AI团队能自主访问所需数据开展建模工作。

## B — Boundary（使用边界）

**不适用场景**：
- 公司只有单一数据源（不需要整合）
- 数据量极小（Excel就能管理）
- 紧急AI项目（等不了仓库建设周期）

**失败模式**：
- 把数据仓库做成"数据沼泽"——数据都堆进去但没有治理，找不到、用不了
- 追求大而全——试图一次性整合所有数据，结果项目永远完不成
- 忽视数据安全——统一仓库意味着更大的安全风险，必须有访问控制

**作者盲区**：
- Andrew Ng强调了统一仓库的重要性，但没充分讨论**建设周期与AI项目节奏的矛盾**——仓库建设可能需要1-2年，但AI项目不能等那么久。建议采用"边建边用"的策略：先接入最急需的数据源启动AI项目，同时继续完善仓库。

## 相关 skills

- **[data-flywheel](/books/ai-for-everyone/data-flywheel/)** — *depends-on*：数据飞轮需要统一数据仓库作为基础设施来汇聚和管理用户产生的数据，没有数据仓库飞轮难以高效运转。
- **[dont-wait-perfect-data](/books/ai-for-everyone/dont-wait-perfect-data/)** — *composes-with*：统一数据仓库是长期工程，AI项目不应等仓库建完才启动——两者配合实现"边建边用"。
