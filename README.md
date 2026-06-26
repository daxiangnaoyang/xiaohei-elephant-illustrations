# Xiaohei Elephant Illustrations

小黑象中文正文配图 Skill。

它用于把公众号文章、AI 工具教程、工作流文档、项目复盘里的关键判断，转成 16:9 白底手绘正文配图：

```text
小黑象 + 认知锚点 + 低科技物理隐喻 + 少量中文批注 + 留白
```

小黑象不是吉祥物海报，也不是 PPT 信息图。它是普通人学 AI、用 AI、和 AI 协作时的认真执行者：搬运、分拣、压实、拆箱、喷洗、守门、盖章。

## What Is Included

- `skill/xiaohei-elephant-illustrations/`：可直接安装到 Codex / Claude / Hermes 类 Skill 运行时的 Skill 源文件。
- `docs/hermes-handoff-after-final-draft.md`：公众号文章终稿确认后的配图接棒 SOP。
- `assets/xiaohei-elephant-ip/`：小黑象 IP 母设图和提示词复盘。
- `assets/xiaohei-tailboard.svg`：公众号尾板小黑象 SVG。
- `examples/harness-loop-engineering/`：一组脱敏示例图、shot list 和 prompt。

## Install

把 Skill 目录复制或软链接到你的本地 Skill root：

```bash
ln -s "$(pwd)/skill/xiaohei-elephant-illustrations" "$HOME/.codex/skills/xiaohei-elephant-illustrations"
```

如果你使用的是 Hermes / Claude Code 运行时，把目标目录替换成对应的 Skill root。

## Recommended Article Workflow

```text
05-final-draft confirmed
-> use xiaohei-elephant-illustrations
-> create 06-illustration-plan.md
-> generate images one by one
-> archive images to your article asset folder
-> insert Markdown image references
-> continue formatting / publishing
```

核心规则：

- 终稿确认前不要生成正文图。
- 先写 shot list，再逐张出图。
- 每张图只表达一个认知锚点。
- 图片主体必须是小黑象在承担动作，不是站在旁边装饰。
- 不虚构未确认的人名、品牌、数据、经历或案例。

## Triggers

- 小黑象
- 小黑象正文配图
- 小黑象 shot list
- 中文正文配图
- AI 工作流配图
- 普通人学 AI 处境图

## Sanitization

This repository is an extracted, sanitized package. Local absolute paths, internal Feishu links, memory databases, credentials, logs, and unrelated Obsidian project files are intentionally excluded.

## Status

Initial public-ready package, extracted from an internal Obsidian workflow and cleaned for standalone reuse.
