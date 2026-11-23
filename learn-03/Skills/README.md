# 第三课 Skill 目录

从 `learn-03/` 打开下面的分类。每个 Skill 先读自己的 `SKILL.md`。完整制作包保留原有的插件入口、子 Skill 和配套素材。

| 分类 | 本地目录中的 Skill 或制作包 |
| --- | --- |
| `资料调研/` | `grilling` 梳理调研范围，`synthesize-research` 归纳反馈，`research` 核对一手资料 |
| `完整制作/` | `frontend-slides`、`MiniMax-pptx-plugin`、`Gorden-Super-PPT`、`Open-Artifact`（Codex 发布包）、`anthropic-pptx`、`steven-superppt-skill`、`baoyu-slide-deck` |
| `PPT美化/` | `theme-factory`、`design-style-skill`。后者直接指向 MiniMax 包里的原目录 |
| `PPT话术/` | `official-document-drafting` 政务汇报、`gtm-board-and-investor-communication` 投资者或董事会汇报、`brand-review` 品牌语气 |
| `看板绘制/` | `excalidraw-diagram-skill` |

## 完整包里的常用入口

- **MiniMax**在 `MiniMax-pptx-plugin/skills/` 保留 `ppt-orchestra-skill`、`slide-making-skill`、`ppt-editing-skill`、`color-font-skill`、`design-style-skill`。先看包内 `README.md`。
- **Gorden Super PPT**保留 `GordenSuperPPTSkill`、`GordenImagePPTGen`、`GordenImage2PPTX`。总入口在第一个目录。
- **Open Artifact**的入口在 `Open-Artifact/skills/open-artifact/SKILL.md`，附上游发布的 Slides 指南和插件运行文件。
- **WorkBuddy PPTX**通过 WorkBuddy 的办公文档套件调用。其本机内置版本的许可限制复制和分发，课程目录提供官方入口。 [WorkBuddy 官方说明](https://www.codebuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/WorkBuddy-Zero-Cost-Skill-Top-10/Office-Document-Suite)

## 复现本地目录

从仓库根目录运行以下命令。需要 Python 3.9 或更新版本和网络。下载器保留各包固定的上游版本，已有且入口齐全的目录会直接跳过。

```sh
python3 learn-03/Skills/download.py
python3 learn-03/Skills/download.py --check
```

公开仓库保存 [下载器和版本清单](download.py)。下载后的原包放在本机课程目录，包含上游随包提供的许可证和说明。需要运行时，请在所用的工具中按各包说明调用。
