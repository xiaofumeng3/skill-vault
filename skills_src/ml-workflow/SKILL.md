---
name: ml-workflow
description: |
  应用从 AI for Everyone 蒸馏出的「ML项目流程 — 收集→训练→部署→迭代」方法论。Use when the user needs practical guidance, diagnosis, workflow design, decision support, or an action plan related to ml-workflow.
---

## Source Metadata

Original cangjie-skill frontmatter from the distillation run:

```yaml
id: f10
title: "ML项目流程 — 收集→训练→部署→迭代"
book: "AI for Everyone"
author: "Andrew Ng（吴恩达）"
source: p11, p16
tags: [machine-learning, workflow, project-management]
related_skills:
  - slug: ab-mapping
    relation: depends-on
  - slug: train-test-split
    relation: depends-on
  - slug: iterate-not-perfect
    relation: depends-on
  - slug: ml-vs-ds
    relation: contrasts-with
```

## R — Reading（原文引用）

> "总结机器学习项目的关键步骤是收集数据、训练模型、建立A到B的映射关系，然后部署模型"
> — p11

## I — Interpretation（用自己的话重新阐述）

机器学习项目遵循一个四阶段工作流，核心是一个**循环**而非线性流程：

1. **收集标注数据**：准备（A, B）配对数据——A是输入（如语音、图片），B是期望输出（如"Alexa"文字、物体标签）。
2. **训练模型**：让算法从数据中学习A→B的映射关系。**预期需要多次迭代**，第一次尝试几乎总是失败的。
3. **部署模型**：将训练好的模型推向真实用户，在真实环境中运行。
4. **迭代优化**：部署后收集反馈数据（尤其是失败案例），将其加入训练数据，重新训练。

**关键洞察**：这是一个**闭环**——部署产生新数据，新数据让模型更好，更好的模型产生更多使用和数据。

## A1 — Past Application（过去应用案例）

- **Alexa唤醒词检测**：收集大量"Alexa"录音 → 训练唤醒检测模型 → 部署到设备 → 发现英国口音识别失败 → 收集英国口音数据 → 重新训练 → 准确率提升。
- **自动驾驶车辆检测**：收集道路图像 → 训练车辆检测模型 → 部署到测试车 → 发现高尔夫球车未被识别 → 收集高尔夫球车图像 → 重新训练 → 模型更鲁棒。

## A2 — Future Trigger（未来触发条件）

**触发场景**：
- 团队刚启动一个ML项目，不知道从何下手
- 模型训练完不知道下一步该做什么
- 部署后发现效果不好，想知道怎么改进

**语言信号**：
- "ML项目怎么做？"
- "机器学习项目步骤是什么？"
- "怎么推进AI项目？"
- "项目流程是什么？"
- "下一步做什么？"
- "部署后怎么办？"

**区分要点**：当你面对的是一个需要"建造并运行一个能持续预测的系统"的项目时，使用本框架。

## E — Execution（执行步骤）

1. **收集标注训练数据**：准备大量（A, B）配对样本，确保数据质量。
2. **训练模型并迭代**：用训练集训练模型，在测试集上评估，反复调整直到达到预定指标（如95%准确率）。
3. **部署到真实用户**：将模型集成到产品/服务中，让真实用户使用。
4. **监控并收集失败案例**：记录模型在实际场景中犯的错误，将这些失败案例加入训练数据。
5. **重新训练**：用扩充后的数据重新训练模型，持续提升性能。

**完成标准**：模型已部署到真实用户，且建立了"收集失败案例→重新训练"的持续迭代机制。

## B — Boundary（使用边界）

**不适用场景**：
- 数据科学项目（产出是报告而非软件，流程不同）
- 一次性分析任务（不需要部署和迭代）
- 没有部署渠道的情况（模型无法触达用户）

**失败模式**：
- 过度关注训练数据量，忽视数据质量
- 部署后没有建立反馈闭环，模型无法持续改进
- 期望一次训练就成功，遇到挫折就放弃

**作者盲区**：
- Andrew Ng低估了"最后一公里"的难度——将模型集成到现有系统中，往往比训练模型本身更难。部署阶段的工程工作量（API设计、延迟优化、A/B测试、灰度发布）可能占整个项目50%以上的工作量，但书中对此着墨不多。

## 相关 skills
- **ab-mapping** (depends-on): ML工作流的前提是已经通过A→B映射定义了清晰的输入输出
- **train-test-split** (depends-on): 训练阶段需要用训练/测试集划分来评估模型泛化能力
- **iterate-not-perfect** (depends-on): 部署后需要建立"收集失败案例→重新训练"的迭代机制
- **ml-vs-ds** (contrasts-with): ML工作流适用于"建系统"项目,DS项目产出报告而非软件
