# 生图通道与模型限制

> 用途：统一对 GitHub 用户、内部 Agent 和公众号推送模板解释“小黑象类 Skill 到底用什么生成图、要不要 OpenAI key、原生 GPT 能不能直接用”。

## 默认通道判断

- 用户只要求配图想法、shot list、README、推送单或 `06-配图方案.md` 时，不直接生图，只输出规划和可复用 prompt。
- 用户明确要求“生成 / 出图 / 做一张 / 做几张”，且当前运行环境暴露 Codex 内置 `image_gen` 工具时，默认走 Codex 内置生图；不额外要求用户提供 OpenAI API key。
- 当前运行环境没有生图工具时，不假装已经出图；输出完整 prompt、QA 标准和交接说明，转交 Codex 内置 `image_gen` 或用户自己的图像生成通道。
- 外部 GitHub 用户安装本仓库后，仓库本身只是 Skill / prompt / workflow 包，不自带托管生图服务；如果他们不在 Codex 内置生图环境里运行，就需要接入自己的图像模型或 API。

## OpenAI Key 口径

- 使用 Codex 内置 `image_gen`：通常不需要在本 Skill 或仓库里配置额外 OpenAI API key，认证来自用户当前 Codex 登录态和可用工具。
- 使用 OpenAI Images API、FAL、智谱、第三方生图服务或自建工作流：需要用户按对应服务配置自己的 key、余额和权限。
- README 不要写成“本仓库自带 OpenAI 生图能力”。应写成“在支持 Codex 内置 `image_gen` 的环境里可直接生成；其他环境请接入自己的图像生成通道”。
- 不要要求用户把 API key 写进仓库、示例、Markdown 或公开 issue。

## 原生 GPT 限制

- 原生 ChatGPT / 自定义 GPT 可以复制 prompt 手动生成或改图，但不能自动等同于 Codex / Hermes / Claude 的 Skill 运行时。
- 原生 GPT 通常不能读取本机 Obsidian 项目、写入 `/Users/dx/Hermes-agent/21-配图空间/`、创建 `06-配图方案.md` 或执行 staged import，除非所在平台明确提供文件系统、工具调用和图片生成能力。
- 文本模型负责理解文章、出 shot list、写 prompt 和做 QA；真正出图必须由具备图像生成/编辑能力的模型或工具完成。

## 模型选择

- 小黑象 1.0 白底手绘解释图、2.0 真实物品场景图、小黑鸡白底手绘图，默认优先 Codex 内置 `image_gen` 能力，因为它更适合中文短标签、角色形体和复杂负面约束。
- 如果只能使用低遵从度或中文渲染不稳的图像模型，要先说明限制：角色可能漂移、中文可能错字、短标签可能多余，生成后必须 QA，不合格重生成或只交付 prompt。
- 不要把“选择哪个聊天模型”写成“选择哪个生图模型”。聊天模型负责调度和审稿，图像模型负责成图，两者要分开说明。

## README 推荐写法

```markdown
## 运行环境与模型限制

这个仓库是 Skill / prompt / workflow 包，不是托管生图服务。

- 在支持 Codex 内置 `image_gen` 的环境里，明确要求出图时可以直接用 Codex 内置生图，不需要在仓库里额外配置 OpenAI API key。
- 在普通 ChatGPT / 原生 GPT 里，可以复制 prompt 手动使用，但它不会自动安装 Skill、读取本机项目或把图片保存到指定目录。
- 在其他 Agent 或脚本环境里，请接入自己的图像生成通道；如果走 OpenAI Images API 或第三方服务，需要使用你自己的 key 和额度。
- 无论使用哪个图像模型，生成图都必须按 QA checklist 检查中文、角色形体、留白、事实边界和是否像 PPT。
```
