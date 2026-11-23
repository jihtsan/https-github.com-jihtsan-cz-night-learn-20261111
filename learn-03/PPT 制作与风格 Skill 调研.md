# PPT 制作与风格 Skill 调研

核对日期为 2026 年 11 月 23 日。第四块从第三块的汇报大纲接着做。先定交付格式，再定视觉风格和说话方式。课堂可先用同一张模型对比页做样张，确认后再制作全套。

## 完整制作包

| Skill 或技能包 | 适合的任务和交付 | 使用条件与依据 |
| --- | --- | --- |
| `frontend-slides` | 从大纲生成单文件 HTML 幻灯片，在浏览器按 16:9 放映。先生成风格预览，也可从已有 PPTX 提取素材再制作网页幻灯片。 | 输出为 HTML。模板使用网络字体，离线放映时应核对字体和图片是否随文件可用。 [Skill 源码](https://github.com/zarazhangrui/frontend-slides/blob/main/plugins/frontend-slides/skills/frontend-slides/SKILL.md) |
| Open Artifact（原 `baoyu-design`） | 在本地编辑器中调整页面、演讲者备注和顺序。可导出独立 HTML 或 PPTX。可编辑 PPTX 模式把常见文字和表格转成 PowerPoint 对象，复杂元素可能转成图片。 | 插件快速开始要求 Node.js 22.18+。项目用独立的页面文件保存，单文件 HTML 通过导出获得。 [安装说明](https://github.com/JimLiu/open-artifact/blob/main/README.zh-CN.md#快速开始) · [Slides 指南](https://github.com/JimLiu/open-artifact/blob/main/docs/types/slides.md) · [PPTX 导出源码](https://github.com/JimLiu/open-artifact/blob/main/packages/slides-editor/src/services/export/pptx.ts) |
| MiniMax `pptx-plugin` | 读取、基于模板改稿或从大纲新建 PPTX。包含编排、配色、布局和模板编辑流程。 | 新建用 PptxGenJS，模板编辑有单独流程。需要保留公司版式时，可先交原模板做一页，再用 PowerPoint 或 WPS 核对。 [插件说明](https://github.com/MiniMax-AI/skills/blob/main/plugins/pptx-plugin/README.md) |
| Anthropic `pptx` | 读取或编辑现有 PPTX，也可用 PptxGenJS 生成。源码提供幻灯片文字提取、缩略图和 Office 文件结构校验工具。 | 适合带来一份已有模板，演示抽取、修改和检查。 [Skill 源码](https://github.com/anthropics/skills/blob/main/skills/pptx/SKILL.md) |
| WorkBuddy `PPTX` | 从第二课的 WorkBuddy 环境延续，读取、压缩或重做演示文稿。 | WorkBuddy 把 `PPTX` 列在办公文档四件套的内置指令里。 [官方说明](https://www.codebuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/WorkBuddy-Zero-Cost-Skill-Top-10/Office-Document-Suite) |

如果需要社媒分享图，`baoyu-slide-deck` 可先逐页生成图片，再合成 PPTX 和 PDF。它的单页修改流程是调整提示词后重生成，适合把整页作为图片分享。 [Skill 源码](https://github.com/JimLiu/baoyu-skills/blob/main/skills/baoyu-slide-deck/SKILL.md)

## 专项风格 Skill

| Skill | 适合调整什么 | 给它什么 |
| --- | --- | --- |
| Anthropic `theme-factory` | 选定主题后统一配色和字体。内置主题有样张，也支持拟定新主题。 | 已有页面或大纲、投影场景、品牌色或参考图。 [Skill 源码](https://github.com/anthropics/skills/blob/main/skills/theme-factory/SKILL.md) |
| MiniMax `design-style-skill` | 为 PPT 选择圆角、间距、字号层级和组件风格，也提供数据密集页的排版方案。 | 根据对比页的信息密度定风格，再把规则交给 PPTX 制稿流程试做样张。 [Skill 源码](https://github.com/MiniMax-AI/skills/blob/main/plugins/pptx-plugin/skills/design-style-skill/SKILL.md) |
| Anthropic `brand-review` | 对照品牌语气、术语和表达要求审稿，给出问题和改写前后的例子。课堂可以用来检查标题、结论和讲稿。 | 幻灯片文字、汇报对象和一小段参考表达。为夜校同学汇报时，可要求先说结论、用短句、按证据表达判断。 [Skill 源码](https://github.com/anthropics/knowledge-work-plugins/blob/main/marketing/skills/brand-review/SKILL.md) |

## 课堂怎么选

- **交单文件 HTML**用 `frontend-slides` 先出一张对比页。标题、模型名称、列顺序和来源位置确定后，再扩展全套。
- **交可编辑 PPTX**用 MiniMax `pptx-plugin`。学员如果已经熟悉 WorkBuddy，可以用它的 `PPTX` 演示从大纲到文件。
- **只调整风格和表达**先用 `theme-factory` 统一配色和字体，需要细调 PPTX 版式时用 `design-style-skill`。用 `brand-review` 检查一句结论如何说给目标听众听。

把第三块的汇报对象、时长、逐页大纲和出处一起交给制作流程。改稿时复核原表数据、模型能力结论及引用位置。最后在目标浏览器、PowerPoint 或 WPS 打开样张，检查投影可读性与需要保留的可编辑对象。

本页依据上游说明和源码核对。课堂演示以实际宿主中可调用的 Skill 和样张验收结果为准。
