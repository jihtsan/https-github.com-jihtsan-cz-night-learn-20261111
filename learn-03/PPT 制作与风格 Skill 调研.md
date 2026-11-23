# PPT 制作与风格 Skill 调研

核对日期为 2026 年 11 月 23 日。第四块从第三块的汇报大纲接着做，先确定画风和话术，再选制作包或专项 Skill。

## 画风与话术

- **画风管页面怎么看。** 选参考页，定配色、字体、版式、图表与配图风格。
- **话术管对听众怎么讲。** 根据汇报对象、时长和希望对方作出的判断，定开场、重点、证据顺序和措辞。

课堂先用同一张「关键差异」页确认画风样张和开场话术，再做全套。

## 完整制作包

| Skill 或技能包 | 适合的任务和交付 | 使用条件与依据 |
| --- | --- | --- |
| `frontend-slides` | 从大纲生成单文件 HTML 幻灯片，在浏览器按 16:9 放映。先生成风格预览，也可从已有 PPTX 提取素材再制作网页幻灯片。 | 输出为 HTML。模板使用网络字体，离线放映时应核对字体和图片是否随文件可用。 [Skill 源码](https://github.com/zarazhangrui/frontend-slides/blob/main/plugins/frontend-slides/skills/frontend-slides/SKILL.md) |
| Open Artifact（原 `baoyu-design`） | 在本地编辑器中调整页面、演讲者备注和顺序。可导出独立 HTML 或 PPTX。可编辑 PPTX 模式把常见文字和表格转成 PowerPoint 对象，复杂元素可能转成图片。 | 插件快速开始要求 Node.js 22.18+。项目用独立的页面文件保存，单文件 HTML 通过导出获得。 [安装说明](https://github.com/JimLiu/open-artifact/blob/main/README.zh-CN.md#快速开始) · [Slides 指南](https://github.com/JimLiu/open-artifact/blob/main/docs/types/slides.md) · [PPTX 导出源码](https://github.com/JimLiu/open-artifact/blob/main/packages/slides-editor/src/services/export/pptx.ts) |
| MiniMax `pptx-plugin` | 读取、基于模板改稿或从大纲新建 PPTX。包含编排、配色、布局和模板编辑流程。 | 新建用 PptxGenJS，模板编辑有单独流程。需要保留公司版式时，可先交原模板做一页，再用 PowerPoint 或 WPS 核对。 [插件说明](https://github.com/MiniMax-AI/skills/blob/main/plugins/pptx-plugin/README.md) |
| Gorden Super PPT `GordenSuperPPTSkill` | 串联两个组件，先生成逐页图片和图片型 PPTX，再把背景、框架、图标与文字分层重建为 PPTX。 | 项目说明面向支持生图的 Codex，整套流程依赖 `GordenImagePPTGen` 和 `GordenImage2PPTX`。文字可编辑，框架和图标保留为图片层。课堂先用一页核对文字、图表数据和选中对象的编辑效果。 [项目源码](https://github.com/GordenSun/GordenSuperPPTSkills) · [分层重建说明](https://github.com/GordenSun/GordenSuperPPTSkills/blob/main/GordenImage2PPTX/SKILL.md) |
| Anthropic `pptx` | 读取或编辑现有 PPTX，也可用 PptxGenJS 生成。源码提供幻灯片文字提取、缩略图和 Office 文件结构校验工具。 | 适合带来一份已有模板，演示抽取、修改和检查。 [Skill 源码](https://github.com/anthropics/skills/blob/main/skills/pptx/SKILL.md) |
| WorkBuddy `PPTX` | 从第二课的 WorkBuddy 环境延续，读取、压缩或重做演示文稿。 | WorkBuddy 把 `PPTX` 列在办公文档四件套的内置指令里。 [官方说明](https://www.codebuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/WorkBuddy-Zero-Cost-Skill-Top-10/Office-Document-Suite) |

同名候选还有 Steven SuperPPT。它用图片做视觉底板，用独立对象承载文字、数字和图表，项目列出 PPTX、HTML 和 PDF 交付路线。 [项目源码](https://github.com/Phantomlau3674/steven-superppt-skill)

如果需要社媒分享图，`baoyu-slide-deck` 可先逐页生成图片，再合成 PPTX 和 PDF。它的单页修改流程是调整提示词后重生成，适合把整页作为图片分享。 [Skill 源码](https://github.com/JimLiu/baoyu-skills/blob/main/skills/baoyu-slide-deck/SKILL.md)

## 画风专项 Skill

| Skill | 适合调整什么 | 给它什么 |
| --- | --- | --- |
| Anthropic `theme-factory` | 选定主题后统一配色和字体。内置主题有样张，也支持拟定新主题。 | 已有页面或大纲、投影场景、品牌色或参考图。 [Skill 源码](https://github.com/anthropics/skills/blob/main/skills/theme-factory/SKILL.md) |
| MiniMax `design-style-skill` | 为 PPT 选择圆角、间距、字号层级和组件风格，也提供数据密集页的排版方案。 | 根据对比页的信息密度定风格，再把规则交给 PPTX 制稿流程试做样张。 [Skill 源码](https://github.com/MiniMax-AI/skills/blob/main/plugins/pptx-plugin/skills/design-style-skill/SKILL.md) |

## 话术专项 Skill

| 场景 | Skill | 怎么用 |
| --- | --- | --- |
| 已有品牌语气或参考稿 | Anthropic `brand-review` | 给它初稿、汇报对象和参考表达，逐条审查标题、术语和讲稿，拿到改写前后示例。 [Skill 源码](https://github.com/anthropics/knowledge-work-plugins/blob/main/marketing/skills/brand-review/SKILL.md) |
| 政务汇报 | 社区 `official-document-drafting` | 选「汇报材料」，按工作进展、成效、问题和下一步组织，逐条保留事实依据。制作 PPT 时，把对应段落压缩成可口述的讲稿。正式成文按单位模板处理。 [Skill 源码](https://github.com/zhaohui-yang/official-document-drafting/blob/main/SKILL.md) · [汇报材料写作规则](https://github.com/zhaohui-yang/official-document-drafting/blob/main/prompts/doc-types/presentation-%E6%B1%87%E6%8A%A5%E6%9D%90%E6%96%99/spec.md) |
| 投资者或董事会进展汇报 | GitHub Awesome Copilot 收录的社区 `gtm-board-and-investor-communication` | 先提炼关键判断，再给已核实指标、进展、风险、下一步和需要对方协助的事项。融资路演可另参考 YC 种子轮指南里的问题、方案和实际进展结构。 [Skill 源码](https://github.com/github/awesome-copilot/blob/main/skills/gtm-board-and-investor-communication/SKILL.md) · [YC 路演指南](https://www.ycombinator.com/library/2u-how-to-build-your-seed-round-pitch-deck) |

### 同一份材料的两种开场

10 个模型系列已完成初筛，办公适用性和成本待核实。

- **政务汇报**「已完成 10 个模型系列的初筛。下一步将按办公场景核对适用范围和使用成本，形成试点建议。」
- **投资者汇报**「候选已缩到 10 个。接下来验证哪些能解决办公任务、成本是否合适，再决定是否试点。」

## 课堂怎么选

- **交单文件 HTML**用 `frontend-slides` 先出一张对比页。标题、模型名称、列顺序和来源位置确定后，再扩展全套。
- **交可编辑 PPTX**用 MiniMax `pptx-plugin` 或 WorkBuddy `PPTX`。想演示先做视觉稿再还原成 PPTX，可以用 Gorden Super PPT 试做一页。
- **画风和话术分别验收**画风检查配色、字号、版式和投影可读性。话术检查开场重点、句长、术语和数字依据，让同学对照上面的两种开场。

把第三块的汇报对象、时长、逐页大纲和出处一起交给制作流程。改稿时复核原表数据、模型能力结论及引用位置。最后在目标浏览器、PowerPoint 或 WPS 打开样张，检查投影可读性与需要保留的可编辑对象。

本页依据上游说明和源码核对。课堂演示以实际宿主中可调用的 Skill 和样张验收结果为准。
