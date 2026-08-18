---
name: iterate-not-perfect
description: |
  应用从 AI for Everyone 蒸馏出的「迭代而非完美 — AI产品的渐进式改进」方法论。Use when the user needs practical guidance, diagnosis, workflow design, decision support, or an action plan related to iterate-not-perfect.
---

## Source Metadata

Original cangjie-skill frontmatter from the distillation run:

```yaml
id: f24
title: "迭代而非完美 — AI产品的渐进式改进"
book: "AI for Everyone"
author: "Andrew Ng（吴恩达）"
source: p20, p24
tags: [iteration, product-strategy, agile, continuous-improvement]
related_skills:
  - slug: ml-workflow, relation: depends-on
  - slug: statistical-acceptance, relation: composes-with
  - slug: start-small-find-partner, relation: composes-with
```

## R — Reading（原文引用）

> "不要试图让AI系统完美无缺才上线...先发布一个'足够好'的版本，然后通过用户反馈持续迭代"
> — p20

## I — Interpretation（用自己的话重新阐述）

追求"完美AI"是项目管理的最大陷阱之一。很多团队花了过多时间在实验室里打磨模型，试图达到完美指标才上线——结果错过了市场窗口，也失去了真实用户的反馈。

**核心理念**：AI产品的改进是一个**持续迭代**的过程，不是一次性工程。

1. **完美不可达**：如统计化验收标准所述，100%准确率通常不可能实现。
2. **真实反馈最珍贵**：实验室里的完美不如上线后用户的真实反馈有价值。
3. **快速上线快迭代**：先发布MVP版本，用真实数据驱动后续改进。
4. **飞轮需要启动**：数据飞轮只有在产品上线后才能开始转起来。

**正确做法**：定义"足够好"的门槛，达到后立即上线，建立用户反馈通道，持续迭代改进。

## A1 — Past Application（过去应用案例）

- **语音助手**：早期的语音助手（Siri、Alexa）准确率远不如今天，但它们没有等到"完美"才上线。通过数亿用户的真实使用数据，这些产品持续迭代，准确率从最初约70%提升到今天的95%以上。如果当年追求完美再上线，就不会有今天的市场地位。

## A2 — Future Trigger（未来触发条件）

**触发场景**：
- 团队一直在打磨模型但迟迟不上线
- 业务方要求"功能完备"后才允许发布
- 团队纠结于几个百分点的准确率提升而错过发布窗口

**语言信号**：
- "还没准备好"
- "再优化一下"
- "等准确率再高一点"
- "功能还不完善"
- "再测试一段时间"
- "再打磨打磨"

**区分要点**：当团队因为**追求完美而推迟上线**时，使用本框架来推动"先发布再迭代"。

## E — Execution（执行步骤）

1. **定义MVP标准**：与团队和业务方协商，明确"可以上线的最低标准"（如核心功能可用、准确率达到底线）。
2. **设定发布门槛**：将MVP标准量化为具体指标，达到即发布。
3. **建立反馈通道**：上线前就设计好用户反馈收集机制（错误报告、满意度评分、使用数据）。
4. **发布MVP**：不要等到完美，达到门槛就发布。
5. **基于反馈迭代**：收集用户反馈和数据，制定下一轮改进计划。
6. **持续循环**：每次迭代都让产品变得更好，逐步接近（但永远达不到）完美。

**完成标准**：产品已上线运行，用户反馈通道已建立，下一轮迭代计划已制定。

## B — Boundary（使用边界）

**不适用场景**：
- 安全关键系统（医疗、航空——上线前必须达到极高标准）
- 品牌首次发布（新产品首次印象很重要，MVP可能有损品牌形象）
- 法律合规要求（某些功能必须完整才能合法运营）

**失败模式**：
- 用"迭代"掩盖懒惰：不是"先发布再迭代"而是"发布后不管"
- 忽视用户反馈：发布了但没有建立反馈通道，迭代变成闭门造车
- 频繁大改：每次迭代都是大改，用户无法适应
- 没有迭代计划：发布了但不知道下一步改什么

**作者盲区**：
- Andrew Ng没有讨论**如何平衡"快速上线"与"品牌风险"**——对于知名品牌，一个有缺陷的AI产品可能对品牌造成持久伤害。建议知名品牌采用"软发布"策略（小范围灰度测试）来降低风险。

## 相关 skills

- **[ml-workflow](/books/ai-for-everyone/ml-workflow/)** — *depends-on*：迭代而非完美是ML工作流中部署阶段的核心理念，需要嵌入整体工作流的持续交付循环中理解。
- **[statistical-acceptance](/books/ai-for-everyone/statistical-acceptance/)** — *composes-with*：统计化验收标准定义了"足够好"的具体门槛，与迭代理念配合——达到标准就上线，后续持续改进。
- **[start-small-find-partner](/books/ai-for-everyone/start-small-find-partner/)** — *composes-with*：从小合作伙伴做起、先求成功的策略与迭代理念一致——通过小范围验证快速迭代，降低试错成本。
