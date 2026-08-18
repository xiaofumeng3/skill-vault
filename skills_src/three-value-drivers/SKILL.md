---
name: three-value-drivers
description: |
  应用从 AI for Everyone 蒸馏出的「AI价值驱动三途径 — 降本/增收/新业务」方法论。Use when the user needs practical guidance, diagnosis, workflow design, decision support, or an action plan related to three-value-drivers.
---

## Source Metadata

Original cangjie-skill frontmatter from the distillation run:

```yaml
id: f23
title: "AI价值驱动三途径 — 降本/增收/新业务"
book: "AI for Everyone"
author: "Andrew Ng（吴恩达）"
source: p15
tags: [value-assessment, business-model, project-selection, roi]
related_skills:
  - slug: triple-due-diligence, relation: depends-on
  - slug: cross-functional-brainstorming, relation: composes-with
```

## R — Reading（原文引用）

> "AI项目可以通过三种方式创造价值：降低成本、增加收入、创建新业务...问'它降低了什么成本？增加了什么收入？创造了什么新业务？'"
> — p15

## I — Interpretation（用自己的话重新阐述）

评估一个AI项目的商业价值时，Andrew Ng提供了一个简洁的三问框架：

1. **降低成本**：AI能否自动化某些任务，从而减少人力成本、时间成本、错误成本？
   - 例：客服自动化减少人工坐席、质检自动化减少质检员、预测性维护减少停机损失
2. **增加收入**：AI能否推动更多转化、更高客单价、更好的用户体验？
   - 例：推荐系统提升交叉销售、动态定价提升利润率、个性化提升用户留存
3. **创建新业务**：AI能否让公司进入全新的业务领域或推出全新产品？
   - 例：数据本身作为新产品、AI能力开放为平台、全新的智能服务

**为什么这个框架有用？**
- 避免"为了AI而AI"——每个项目必须能回答这三问之一
- 帮助商业尽调时结构化地量化项目价值
- 三个途径的风险和回报特征不同：降本最可预测、增收需要用户行为改变、新业务风险最高但天花板最高

## A1 — Past Application（过去应用案例）

- **降本案例**：某制造企业用AI视觉质检替代人工质检。每个质检员年薪8万，AI系统替代5个质检员，年节省40万人力成本。项目投入60万，1.5年回本。
- **增收案例**：某电商平台引入推荐系统。推荐系统将用户转化率从2%提升到3.5%，按年GMV 10亿计算，增量收入1500万。
- **新业务案例**：某银行将内部风控模型开放为SaaS服务，为其他小银行提供风控能力。这是全新的业务线，与原有银行业务无关。

## A2 — Future Trigger（未来触发条件）

**触发场景：**
- 评估一个AI项目"值不值得做"
- 向管理层/投资人解释AI项目的商业价值
- 比较多个AI项目的优先级
- 商业尽调阶段需要量化项目价值

**语言信号：**
- "这个项目怎么赚钱"
- "AI项目的ROI怎么算"
- "这个项目有什么商业价值"
- "值不值得投入"
- "能带来多少收益"

**区分要点：**
- 用户需要的是**快速分类**（三选一）还是**详细量化**（财务模型）？本skill提供分类框架，详细量化需要triple-due-diligence。
- 项目处于**创意阶段**还是**评估阶段**？创意阶段用cross-functional-brainstorming，评估阶段用本skill。

## E — Execution（执行步骤）

1. **识别价值驱动类型**：这个项目主要通过降本、增收还是新业务创造价值？（可以多选）

2. **量化价值**：
   - 降本：计算可替代的人力/时间/错误成本
   - 增收：估算转化率/客单价/留存的提升空间
   - 新业务：评估市场规模和进入壁垒

3. **评估投入**：估算开发成本、数据成本、部署成本、维护成本

4. **计算ROI**：(量化价值 - 投入成本) / 投入成本

5. **风险评估**：
   - 降本：技术能否达到自动化要求？
   - 增收：用户行为是否会如预期改变？
   - 新业务：市场是否存在？竞争格局如何？

6. **综合判断**：如果三个问题都答不上来，项目价值存疑。

**完成标准**：明确项目的价值驱动类型，并给出量化的价值估算和投入产出分析。

## B — Boundary（使用边界）

**不适用场景：**
- 纯研究项目（没有商业应用目标）
- 基础设施类项目（价值间接，难以直接量化）
- 合规/伦理驱动的项目（价值不在经济层面）

**失败模式：**
- 把所有项目都说成"三个都有"——没有聚焦
- 过度乐观估算增收/新业务的价值
- 忽视实施成本和变革管理成本
- 只看经济价值，忽视战略价值（如数据积累、能力建设）

**作者盲区：**
- Andrew Ng的三问框架偏向短期经济价值，但有些AI项目的价值是**战略性的**——如积累数据资产、培养AI能力、建立组织信心。这些长期价值难以用三问框架衡量。
- 三个途径并非互斥——一个项目可能同时降本和增收，需要判断哪个是主要驱动力。

## 相关 skills

- **[triple-due-diligence](/books/ai-for-everyone/triple-due-diligence/)** — *depends-on*：商业尽调需要量化项目价值，三价值驱动框架提供了商业尽调中"价值评估"部分的结构化方法。
- **[cross-functional-brainstorming](/books/ai-for-everyone/cross-functional-brainstorming/)** — *composes-with*：头脑风暴产出候选项目后，用三价值驱动框架对候选项目进行价值评估和优先级排序。
