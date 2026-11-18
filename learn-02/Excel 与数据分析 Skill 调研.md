# Excel 与数据分析 Skill 调研

核对日期为 2026 年 11 月 18 日。第二课可以直接用 WorkBuddy 的 XLSX 或 Codex 的 Spreadsheets 演示如何交付 Excel，再用一套数据分析流程讲清怎样查异常、算指标和解释结果。

## 候选 Skill

| Skill | 适合做什么 | 使用入口与依据 |
| --- | --- | --- |
| **WorkBuddy `XLSX`** | 清洗 Excel、整理字段、补公式、汇总并输出表格。适合第二课的主演示。 | WorkBuddy 官方「办公文档四件套」列出的内置指令。 [官方说明](https://www.codebuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/WorkBuddy-Zero-Cost-Skill-Top-10/Office-Document-Suite) |
| **Codex `Spreadsheets`** | 创建和修改 Excel，制作公式、格式和图表，回读并核对工作簿。 | 本课程的 1,000 行门店练习表已用当前 Codex 桌面环境的 `Spreadsheets` Skill 生成和验证。 |
| **商汤 SenseNova `sn-da-excel-workflow`** | 读取多工作表，检查缺失和重复，按门店、地区或品类分组汇总，输出图表与 Excel／CSV。 | 有中文说明，项目推荐 OpenClaw 或 Hermes。Excel 工作流依赖 Python 数据处理库，文档显示它本身无需模型 API Key。配套 `sn-da-large-file-analysis` 用于更大文件，包含流式读取和 Parquet 中转。 [中文说明](https://github.com/OpenSenseNova/SenseNova-Skills/blob/main/docs/sn-data-analysis_cn.md) · [Excel Skill](https://github.com/OpenSenseNova/SenseNova-Skills/blob/main/skills/sn-da-excel-workflow/SKILL.md) · [项目入口](https://github.com/OpenSenseNova/SenseNova-Skills) |
| **MiniMax `minimax-xlsx`** | 定点改动现有 Excel 模板，检查公式，适合已有固定财务表或经营月报的场景。 | MIT。仓库提供 Codex 技能目录接入说明和 Claude Code 插件入口。可用 LibreOffice 动态重算，保格式的效果需要按目标模板验收。 [Skill 源码](https://github.com/MiniMax-AI/skills/blob/main/skills/minimax-xlsx/SKILL.md) · [Codex 接入说明](https://github.com/MiniMax-AI/skills/blob/main/.codex/INSTALL.md) · [验证说明](https://github.com/MiniMax-AI/skills/blob/main/skills/minimax-xlsx/references/validate.md) |
| **Anthropic `xlsx`** | 生成和编辑工作簿，清洗数据，写入可重新计算的公式，并扫描公式错误。 | Claude 有预置能力，Claude Code 可通过 `document-skills` 接入。GitHub 上公开的 `xlsx` 目录使用 Apache 2.0。公开实现用 `openpyxl`／`pandas` 处理文件，用 LibreOffice 检查公式计算。 [官方接入说明](https://github.com/anthropics/skills#try-in-claude-code-claudeai-and-the-api) · [Skill 源码](https://github.com/anthropics/skills/blob/main/skills/xlsx/SKILL.md) · [目录许可](https://github.com/anthropics/skills/blob/main/skills/xlsx/LICENSE.txt) |
| **OpenAI Data 插件的 `analyze-data-quality` 与 `metric-diagnostics`** | 前者检查重复、缺失、数据类型和关联风险。后者回答哪些门店、品类或时段贡献了指标差额。 | 两个流程在 OpenAI 插件仓库可查。使用入口取决于 ChatGPT Work 或 Codex 账户和工作区中的 Data 插件可用性。 [质检 Skill](https://github.com/openai/plugins/blob/main/plugins/data-analytics/skills/analyze-data-quality/SKILL.md) · [指标诊断 Skill](https://github.com/openai/plugins/blob/main/plugins/data-analytics/skills/metric-diagnostics/SKILL.md) · [插件说明](https://help.openai.com/en/articles/20001518-using-the-data-plugin-in-chatgpt-work-and-codex) |
| **`lieflat-charts`** | 把已经核对的汇总数据做成浏览器可看的图表或报告，适合课件里的可视化延伸。 | 默认作品是 HTML 图表。项目提供 Codex 等平台的安装说明。部分图表的库和字体通过网络加载。 [Skill 源码](https://github.com/larashero3-dotcom/lieflat-charts/blob/main/SKILL.md) · [使用说明](https://github.com/larashero3-dotcom/lieflat-charts/blob/main/README.en.md) |

Agent Skills 规范允许一个 Skill 同时包含使用说明、参考资料、模板和可执行脚本。实际运行取决于宿主是否支持文件读写、对应脚本依赖和相关连接。本次除已用于课程练习的 Codex Spreadsheets 外，其余候选的能力和接入来自文档及源码核对。直接操作 Excel 中已打开的工作簿是另一种入口，OpenAI 提供 ChatGPT for Excel 加载项。 [Agent Skills 规范](https://agentskills.io/specification) · [Excel 加载项说明](https://help.openai.com/en/articles/20001063-chatgpt-for-excel-and-google-sheets)

## 用现有门店练习演示

1. **先检查数据。** 从门店原表找出重复记录、成本空白和含义不清的日期，给出原表行号、可能影响和需要确认的处理方式。
2. **再交付工作簿。** 处理方案确认后，保留原表，交付异常记录和门店汇总。引用现行指标口径，写入可复算的公式。学员用明细复核销售额合计，再手算一个比率。
3. **有余量再做经营分析。** 问「哪些门店的销售额与目标差额最大」，按销售额减销售目标计算差额，回到各品类和日期核对贡献。有需要时用 `lieflat-charts` 把已确认的差额画成正负条形图。

同一套练习可以说明三层工作的关系。知识库提供《门店指标口径》，数据分析 Skill 规定如何检查和解释数据，Excel Skill 把结果写成可继续编辑的工作簿。
