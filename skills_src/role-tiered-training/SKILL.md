---
name: role-tiered-training
description: |
  应用从 AI for Everyone 蒸馏出的「分层AI培训 — 高管/经理/工程师的差异化学习」方法论。Use when the user needs practical guidance, diagnosis, workflow design, decision support, or an action plan related to role-tiered-training.
---

## Source Metadata

Original cangjie-skill frontmatter from the distillation run:

```yaml
id: f25
title: "分层AI培训 — 高管/经理/工程师的差异化学习"
book: "AI for Everyone"
author: "Andrew Ng（吴恩达）"
source: p22
tags: [training, change-management, role-based, education, organization]
related_skills:
  - slug: ai-transformation-playbook, relation: depends-on
  - slug: ai-team-building, relation: composes-with
```

## R — Reading（原文引用）

> "对高管和高层业务领导者...可通过4小时左右培训完成大部分内容...部门负责人...至少需要12小时...软件工程师...计划至少进行一百小时的培训。"
> — p22

## I — Interpretation（用自己的话重新阐述）

AI培训最常見的错误是"给所有人上同一门课"。Andrew Ng基于Google和百度的培训经验，提出了分层培训框架：

| 层级 | 时长 | 学习目标 | 核心内容 |
|------|------|----------|----------|
| **高管/高层** | ~4小时 | 做资源分配决策 | AI能做什么、不能做什么、如何评估AI项目、如何制定AI战略 |
| **部门/项目经理** | ~12小时 | 管理AI项目 | 如何做项目方向设定、如何做商业尽调、如何管理AI团队、如何设定验收标准 |
| **工程师/技术骨干** | 100+小时 | 构建AI系统 | 机器学习基础、模型训练与评估、数据工程、模型部署与运维 |

**为什么分层？**
- 不同角色的AI知识需求完全不同
- 给高管讲100小时技术细节是浪费，给工程师讲4小时战略是不够的
- 分层培训最大化学习效率，避免"听不懂"或"太浅了"

## A1 — Past Application（过去应用案例）

- **Google Brain培训**：早期Google Brain团队为不同层级员工设计了差异化课程。高管半天了解AI战略，工程师数周深入学习技术实现。这种分层模式让Google在AI人才紧缺的情况下快速扩大了AI能力覆盖面。

## A2 — Future Trigger（未来触发条件）

**触发场景：**
- 公司要推AI培训，但不知道不同层级该学什么
- 培训效果不好——高管觉得太技术，工程师觉得太浅
- 设计AI培训体系
- 评估AI培训的投资回报

**语言信号：**
- "AI培训"
- "全员AI学习"
- "不同层级学什么"
- "AI培训体系"
- "AI素养"
- "给高管讲什么AI"

**区分要点：**
- 用户需要**培训设计**还是**具体课程内容**？本skill提供分层框架，不涉及具体课程内容。
- 是**组织培训**还是**个人学习**？本skill面向组织场景。

## E — Execution（执行步骤）

1. **识别受众层级**：将目标受众分为高管、经理、工程师三类。

2. **设计分层课程**：
   - 高管层（~4h）：AI能力边界、项目评估方法、AI战略制定、常见误区
   - 经理层（~12h）：项目范围定义、商业尽调方法、AI团队管理、验收标准设定
   - 工程师层（100h+）：ML基础、数据处理、模型训练、部署运维

3. **选择培训方式**：
   - 高管：工作坊、案例讨论、外部专家分享
   - 经理：项目实战、跨部门轮岗、与AI团队协作
   - 工程师：系统课程、动手实验、项目实战

4. **设定学习目标**：每个层级设定明确的学习目标和考核方式。

5. **持续迭代**：根据反馈调整培训内容和时长。

**完成标准**：完成分层培训方案设计，明确各层级的培训目标、内容大纲、时长和考核方式。

## B — Boundary（使用边界）

**不适用场景：**
- 个人自学AI（不需要分层设计）
- 纯技术团队（没有高管/经理层级）
- 一次性讲座（不是体系化培训）

**失败模式：**
- 给所有人上同一门课——高管听不懂技术细节，工程师觉得战略太浅
- 培训时长不足——4小时的高管培训压缩成1小时，无法建立基本认知
- 只培训技术人员，忽视管理层——管理层不懂AI，无法有效支持AI项目
- 培训后没有实践机会——学了就忘

**作者盲点：**
- Andrew Ng的时长建议（4/12/100小时）基于大公司的经验。**中小企业可能需要压缩**——比如高管2小时、经理6小时、工程师50小时也能达到基本效果。
- 分层培训假设你能清晰区分"高管/经理/工程师"——但在扁平化组织或创业公司，一个人可能同时承担多个角色。

## 相关 skills

- **[ai-transformation-playbook](/books/ai-for-everyone/ai-transformation-playbook/)** — *depends-on*：分层培训是AI转型五步指南中第三步"提供广泛AI培训"的具体实施方案，需要嵌入整体转型路线图中理解。
- **[ai-team-building](/books/ai-for-everyone/ai-team-building/)** — *composes-with*：分层培训与AI团队建设相辅相成——培训为团队提供人才储备，团队为培训提供实践场景。
