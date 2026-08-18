---
name: statistical-acceptance
description: |
  应用从 AI for Everyone 蒸馏出的「统计化验收标准 — 不追求100%准确」方法论。Use when the user needs practical guidance, diagnosis, workflow design, decision support, or an action plan related to statistical-acceptance.
---

## Source Metadata

Original cangjie-skill frontmatter from the distillation run:

```yaml
id: f18
title: "统计化验收标准 — 不追求100%准确"
book: "AI for Everyone"
author: "Andrew Ng（吴恩达）"
source: p16, p24
tags: [project-management, evaluation, acceptance-criteria, communication]
related_skills:
  - slug: train-test-split, relation: depends-on
  - slug: ml-workflow, relation: depends-on
  - slug: iterate-not-perfect, relation: composes-with
```

## R — Reading（原文引用）

> "AI系统的一个创新点是性能通常以统计方式定义，与其要求AI系统完美执行，我们更常要求AI系统达到特定准确率"
> — p16

## I — Interpretation（用自己的话重新阐述）

要求AI达到100%准确率是商业界最常见的误区之一。追求完美通常是不可能的，原因有三：

1. **ML有根本性限制**：任何统计学习方法都存在不可消除的误差下限。
2. **数据本身有噪声**：标注错误、模糊样本、边界案例——数据本身就不完美。
3. **人类专家也会分歧**：对于模糊案例，不同专家给出的答案可能不同，不存在"标准答案"。

**正确做法**：将验收标准定义为统计目标（如"在测试集上达到95%准确率"），并认识到一个95%准确率的系统已经能创造巨大价值。关键是**提前约定**可接受的标准，而非事后要求完美。

## A1 — Past Application（过去应用案例）

- **咖啡杯缺陷检测**：95%的准确率意味着5%的缺陷产品会漏检。但这仍然非常有价值——可以配合人工抽检来兜底。如果追求100%，项目可能永远无法上线，而95%的系统已经能拦截绝大多数缺陷，大幅降低质检成本。

## A2 — Future Trigger（未来触发条件）

**触发场景**：
- 业务方坚持"AI不能出错"
- 团队因为AI犯了几个错误就否定整个项目
- 验收时对"什么算合格"产生争议

**语言信号**：
- "必须100%准确"
- "零错误"
- "AI犯错了"
- "完美"
- "100%"
- "零缺陷"

**区分要点**：当有人（包括你自己）对AI系统提出"零错误"要求时，使用本框架来重新设定合理预期。

## E — Execution（执行步骤）

1. **与AI团队讨论可达成的准确率**：了解在当前数据和技术条件下，合理的准确率目标是什么。
2. **定义统计化验收标准**：将目标量化为具体数字（如"测试集准确率≥95%"），写入项目文档。
3. **接受错误必然发生**：明确告知利益相关者——系统会犯错，这是正常的。
4. **设计错误处理机制**：为那5%的错误规划应对方案（人工复核、降级流程、用户反馈通道）。

**完成标准**：团队和业务方对"可接受的准确率"达成共识，并建立了错误发生时的应对方案。

## B — Boundary（使用边界）

**不适用场景**：
- 安全关键系统（医疗诊断、自动驾驶、航空控制——这些领域错误会导致人身伤害，需要远高于95%的标准）
- 95%确实不够用的场景（如金融反欺诈，1%的漏检可能造成巨大损失）
- 法律合规要求零容忍的领域

**失败模式**：
- 盲目接受95%而不评估错误成本：如果每个错误的代价极高，95%可能远远不够
- 没有设计错误兜底方案：告诉业务方"会有5%错误"但没有应对措施
- 用统计标准掩盖技术不足：把"做不到"包装成"不需要做到"

**作者盲区**：
- Andrew Ng没有深入讨论**如何将AI与人工审核结合来处理那5%的错误**。在实际项目中，"AI初筛 + 人工复核"的混合模式往往是最佳实践，但书中对此着墨不多。此外，不同类型的错误（假阳性 vs 假阴性）代价不同，简单的准确率数字可能掩盖重要差异。

## 相关 skills

- **[train-test-split](/books/ai-for-everyone/train-test-split/)** — *depends-on*：统计化验收标准需要基于独立测试集上的准确率来定义，没有正确的数据分割就无法建立可信的验收标准。
- **[ml-workflow](/books/ai-for-everyone/ml-workflow/)** — *depends-on*：验收标准是ML工作流中评估阶段的核心产出，需要嵌入整体工作流中理解。
- **[iterate-not-perfect](/books/ai-for-everyone/iterate-not-perfect/)** — *composes-with*：接受统计化验收标准与"迭代而非完美"的理念相辅相成——先达到可接受的准确率上线，再持续迭代改进。
