# Real-Person Cover Design Skill

一个不携带任何个人照片或私有配置的真人封面设计 Skill。它把人物身份、单一姿势、渠道画幅、视觉语言和标题白名单拆开管理，适用于文章头图、视频封面和小红书 3:4 封面。

## 包含内容

- `SKILL.md`：触发条件、隐私边界、工作流和验收标准
- `references/style-library.md`：九种可重组的视觉语言
- `references/prompt-template.md`：一体成型生图 Prompt 模板
- `references/qa-checklist.md`：身份、文字、画幅、证据和透明度检查
- `templates/cover-brief.md`：开始前的最小 Brief
- `GOTCHAS.md`：公开发布前的脱敏和常见翻车点

## 使用方式

把 `skill/real-person-cover-design/` 复制到你的 Skill 事实源或运行时入口，然后提供：

1. 标题或主题；
2. 目标平台和比例；
3. 可选的人物身份参考图；
4. 可选的一张姿势参考图；
5. 想强调的视觉中心。

支持图像生成工具时，优先一次生成完整封面；没有图像工具时，Skill 会返回可执行 Prompt。人物参考图只在当前任务使用，不应复制进这个公开包。

## 公开包边界

本目录不含真人照片、面部数据、绝对路径、账号信息、二维码、密钥或内部运行时配置。发布前请按 `GOTCHAS.md` 重新扫描。

## License

MIT，随仓库根目录的 [LICENSE](../../LICENSE) 发布。
