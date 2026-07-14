---
name: xiaohei-elephant-scenes
description: 小黑象 2.0 真实物品场景配图 — 为中文文章、AI 工作流、项目复盘、个人经历和社群 SOP 生成“小黑象 + 真实物品 + 物理动作 + 留白叙事”的 16:9 正文配图、真实物品小现场、彩蛋长卷故事图、shot list 和生图提示词。触发词包括“小黑象 2.0”“小黑象真实物品”“小黑象真实物件”“小黑象场景图”“真实物品+物理动作”“实物小现场”“彩蛋长卷”。不得回退到旧版小黑、小黑人或 `xiaohei-scenes`。
triggers:
  - 用户明确要求小黑象 2.0
  - 用户要求小黑象真实物品场景图
  - 用户要求真实物品 + 物理动作正文配图
  - 用户要求小黑象 2.0 封面图或 cover 版
  - 用户要求彩蛋长卷、项目复盘长卷、个人经历长卷
  - 用户要求统一小黑象推送模板且明确要 2.0 真实物品场景图
aliases:
  - 小黑象2.0
  - 小黑象 2.0
  - 小黑象场景图
  - 小黑象真实物品
  - 小黑象真实物件
  - 小黑象实物小现场
  - 小黑象 2.0 封面
  - 小黑象 2.0 cover
  - 小黑象长卷
  - 小黑象 2.0 推送模板
when-to-use: |
  用户要求为中文文章、帖子、教程、案例、项目复盘或个人经历生成“小黑象 + 真实物品 + 物理动作”的高质量配图时触发。
  适用：真实物品小现场、白色摄影棚、实物隐喻、工作压力、AI 工具链崩溃、项目复盘、个人经历、产品演化、彩蛋长卷故事图。
  适用：用户明确要“小黑象 2.0 封面 / cover 版 / 公众号头图”，输出 21:9 深色科技感 cover，融合小黑象 2.0 真实物品隐喻。
  适用：用户要求“统一小黑象推送模板 / 小黑象推送结构”，并明确图片模式是“小黑象 2.0 / 真实物品 / 真实物件 / 小现场 / 场景图 / 彩蛋长卷”。
  不触发：用户只要白底手绘解释图、低科技手绘隐喻、正文图 shot list，可用 `xiaohei-elephant-illustrations`。
  不触发：旧版小黑、小黑人、人形小黑、`xiaohei-scenes`，除非用户明确要求旧小黑且没有说“小黑象”。
---

# 小黑象 2.0 真实物品场景图

## 核心定位

把文章观点、用户处境、个人经历、项目过程和产品演化，转译成一个可传播的真实物品小现场：

```text
小黑象 + 真实物品 + 物理动作 + 短中文标签 + 留白叙事
```

1.0 的 `xiaohei-elephant-illustrations` 更像白纸上的手绘解释图，适合拆观点、拆流程、拆方法。2.0 的 `xiaohei-elephant-scenes` 更像白色摄影棚里的真实物品现场，适合表达处境、压力、转折、项目故事和正文观点隐喻。

小黑象仍然必须是黑色小象：短象鼻、小耳朵、短腿、白点眼。真实物品可以摄影质感，但角色不能漂移成小黑人、黑色人形、火柴人、旧版小黑或普通黑色圆球。

## Before Starting

按需读取，不要一次全塞：

- `GOTCHAS.md` - 路由、旧小黑混淆、真实物品过载和封面误用问题
- `references/xiaohei-elephant-ip-lock.md` - 小黑象 2.0 IP 锁定、四足腿部规则、Prompt 锁定块和 QA 一票否决
- `references/style-dna.md` - 2.0 视觉 DNA、摄影棚、真实物品、留白和小黑象形体门槛
- `references/object-patterns.md` - 真实物品选择、物理动作和原创隐喻规则
- `references/prompt-template.md` - 标准图和彩蛋长卷提示词模板
- `references/qa-checklist.md` - 生成后质量检查
- `../xiaohei-elephant-illustrations/references/generation-runtime-notes.md` - OpenAI key、原生 GPT、Codex 内置生图和模型选择口径
- `../xiaohei-elephant-illustrations/references/unified-push-structure.md` - 统一小黑象推送结构；2.0 执行时复用同一 `06-配图方案.md` 字段，但图片模式填“小黑象 2.0 真实物品场景图”
- `../xiaohei-elephant-illustrations/templates/unified-xiaohei-push.md` - 统一小黑象推送单空白模板；复制后把使用 Skill 改为 `xiaohei-elephant-scenes`

默认规则：

- 用户只说“小黑象配图 / 白底手绘 / 正文插图”时，默认用 `xiaohei-elephant-illustrations`。
- 用户说“小黑象 2.0 / 真实物品 / 实物 / 真实物件 / 物理动作 / 场景图 / 小现场 / 长卷”时，用本 Skill。
- 用户说“小黑象 2.0 封面 / cover / 公众号头图”时，用本 Skill 的 Cover 模式，不混入正文 16:9 图数量。
- 生成前必须把 `references/xiaohei-elephant-ip-lock.md` 的标准 Prompt 锁定块折进提示词，尤其是四足短圆桩腿和禁止二足/人形腿规则。
- 用户要求“统一小黑象推送模板”且指定 2.0 时，先复用 `xiaohei-elephant-illustrations` 中的统一推送结构，再把 shot list、生成锁定和 QA 替换成本 Skill 的真实物品场景图要求。
- 生成前先输出 shot list；用户明确要求直接出图时，也要先在内部完成母版/动作/物件锁定。
- 每张标准图只表达一个核心物理动作；不要把主题里的所有名词都摆进去。
- 真实物品只能服务隐喻，不能抢走小黑象主角位置。
- 用户明确点名真实产品、平台或公司时，真实物品可以包含对应官方品牌 logo / app icon / 产品标识，例如飞书场景用飞书官方品牌标识，Codex / OpenAI 场景用 OpenAI 官方品牌标识；logo 只作为物品识别线索，不暗示官方背书。
- 不能确认的人名、品牌、数据、经历和案例，不画成事实；用概括性标签替代。不要虚构不存在的品牌、伪造 logo 或把 logo 改造成近似山寨标识。
- 图片资产最终归档到 `/Users/dx/Hermes-agent/21-配图空间/<文章或项目名>/`。

## Core Flow

### 1. 判断模式

先判断用户要哪种输出：

- **标准模式**：16:9 正文配图，一个真实物品小现场，一个核心物理动作。
- **Cover 模式**：21:9 公众号封面/头图，深色科技感背景，一个小黑象 2.0 真实物品核心隐喻，标题区与主视觉分开。
- **彩蛋长卷模式**：超横版真实物品故事线，5-8 个节点，适合项目复盘、个人经历、产品演化。

如果用户没有明确说“封面 / cover / 头图 / 长卷 / 彩蛋 / 时间线 / 复盘路径”，默认标准模式。

### 2. 提炼处境和物理动作

不要先堆物品，先找处境：

- 谁被什么卡住、压住、拉回、筛掉、催促、重组？
- 哪个抽象判断可以变成一个真实物品上的动作？
- 小黑象应该推、拉、挡、托、盖章、检查、修补、搬运、拧紧、拉绳还是守门？动作优先用象鼻完成，不给小黑象加人类手臂。
- 哪 2-4 个中文短标签能 1 秒读懂？

完成后，每张图必须有：

```text
主题：
读者处境：
核心冲突句：
真实主物品：
核心物理动作：
小黑象动作：
小黑象腿部锁定：四足短圆桩腿 / 禁止二足人形腿
小黑象占比锁定：标准图高度 3%-5% / cover 高度 4%-6% / 黑色视觉体量约为此前测试的 1/3
中文短标签：
画面 3 秒读懂句：
风险/避坑：
```

### 3. 标准图生成

每张图单独生成，不拼图。

#### 生图通道：Codex 内置 image_gen 工具（首选）

**默认口径**

- 只有用户明确要求“生成 / 出图 / 做一张 / 做几张”时才进入生图；只要方案、模板或 shot list 时不直接生图。
- 当前 Codex 环境暴露内置 `image_gen` 时，默认用它逐张生成；不要求用户在仓库或 Skill 里额外填写 OpenAI API key。
- 当前环境没有生图工具时，只输出 prompt、QA 标准和交接说明，不假装已经生成图片。
- 外部 GitHub 用户如果不在 Codex 内置生图环境里运行，需要接入自己的图像生成通道；走 OpenAI Images API、FAL、智谱或第三方服务时，用他们自己的 key、余额和权限。
- 原生 ChatGPT / 自定义 GPT 可以复制 prompt 手动使用，但不能自动等同于本 Skill 运行时，也不能默认读取本机项目、创建 `06-配图方案.md` 或保存图片到指定目录。

**为什么优先用 Codex，而不是 Hermes 内置 image_generate 或 CogView？**
- Hermes 内置 `image_generate` 需要 FAL_KEY，且目前未配置
- 智谱 CogView-3-Flash 小黑象形态不准、中文标签无法清晰渲染，指令遵从度极差
- 智谱 CogView-3-Plus 余额不足时无备选
- Codex 登录态可用且暴露内置 `image_gen` 时，不需要在本仓库额外配置 OpenAI API key；当前小黑象形体、中文短标签和负面约束更适合用这一通道

**Codex 生成命令模板：**

```bash
# 单张生成（推荐，稳定性最好）
cd "<输出目录>" && codex exec --sandbox workspace-write --skip-git-repo-check --ephemeral \
  "用你的内置 image_gen 工具生成一张配图并保存到当前目录，文件名 <文件名.png>。Prompt: <英文提示词>"

# 多张批量生成
cd "<输出目录>" && codex exec --sandbox workspace-write --skip-git-repo-check --ephemeral \
  "用内置 image_gen 工具逐张生成以下配图，保存到当前目录：
  第1张，文件名 xx.png：Prompt: ...
  第2张，文件名 yy.png：Prompt: ..."
```

**注意事项：**
- `--sandbox workspace-write` 让 Codex 能写文件到工作目录
- `--skip-git-repo-check` 允许在非 git 目录执行
- `--ephemeral` 不保留 Codex session 文件
- Codex 内置 image_gen 默认保存到 `$CODEX_HOME/generated_images/`，需要 Codex 自己 move/copy 到工作目录
- GPT-image-1 每张约 30-60 秒，5 张批量约 8-10 分钟
- 生成后在 Hermes 内用 `codex exec -i "图片.png"` 做视觉 QA

**Codex 生图 prompt 要点（英文，GPT-image-1 英文效果最好）：**
- 必须包含 `references/xiaohei-elephant-ip-lock.md` 的 `Xiaohei Elephant 2.0 IP lock` 等价内容。
- 必须包含：`A tiny nimble solid BLACK elephant silhouette, SHORT TRUNK, SMALL ROUND EARS, FOUR SHORT ROUNDED ELEPHANT PEG LEGS under the body, WHITE DOT EYES, compact agile body, camera pulled far back, elephant height only 3%-5% of canvas height`
- 必须包含：`NO human figures, stick figures, robots, bears. Elephant is the ONLY character.`
- 必须包含：`No biped pose, no human legs, no stick legs, no knees, no feet, no shoes, no close-up, no low-angle hero shot, no bulky toy elephant, no heavy round statue.`
- 中文标签直接写中文字符，GPT-image-1 能正确渲染

**降级通道（Codex 不可用时）：**
1. CogView-3-Flash：`curl` 调用智谱 API（`https://open.bigmodel.cn/api/paas/v4/images/generations`，model=cogview-3-flash），质量差仅作后备
2. CogView-3-Plus：同上，需余额充足

#### 提示词必须包含

- 16:9 横版中文正文配图
- `#FFFFFF` 纯白或接近纯白摄影棚背景
- 一个真实主物品或紧凑物品组
- 如果主题明确涉及真实品牌 / 产品 / App，主物品可带官方品牌 logo、app icon 或产品标识；例如飞书用飞书标识，Codex / OpenAI 用 OpenAI 标识。logo 要小而准，贴在真实物品上，不做成品牌 KV。
- 小黑象参与核心物理动作
- 短象鼻、小耳朵、四足短圆桩腿、白点眼；禁止二足站姿、人形腿、火柴腿、鞋子脚掌
- 镜头后退，整体场景只占画面中等偏小区域；小黑象必须明显缩小，标准图高度约 3%-5% 画面高，黑色视觉体量约为此前测试图的 1/3，不超过主物品高度的 1/3；小黑象轻巧、灵活，不是笨重玩具或摆件
- 2-4 个中文手写短标签
- 少量蓝 / 黄 / 红 / 橙点缀
- 禁止小黑人、黑色人形、旧版小黑、火柴人、普通黑球、萌宠化、PPT 信息图、UI 截图、复杂架构图

真实物品要有自然光影和透视，但整体仍然轻、干净、有留白。画面第一眼应该像"一个真实、轻、怪的小现场"，不是商品摄影、PPT 大图或复杂道具堆。

### 3B. Cover 版生成

Cover 版是单独的一张图，不混入正文配图数量。

要求：

- 21:9 超横版公众号封面 / 头图。
- 参考 `_skill-staging/wechat-tech-article-infographic` 的视觉要求：深色科技背景、青橙对比、弱 HUD 网格、玻璃拟态卡片、发光连接线、科技手绘质感。
- 小黑象 2.0 融入主视觉：一个真实物品核心隐喻 + 小黑象用短象鼻参与动作。
- 如果 cover 主题明确涉及真实品牌 / 产品 / App，可在真实物品上使用对应官方 logo / app icon / 产品标识，作为识别锚点；logo 不应成为主标题或广告主视觉，也不暗示官方合作、授权或背书。
- 小黑象仍按 2.0 硬门槛：短象鼻、小耳朵、四足短圆桩腿、白点眼；禁止二足站姿、人形腿、火柴腿。
- Cover 里小黑象也只是小执行者，不是主视觉主体；高度约 4%-6% 画面高，黑色体量约为此前测试 cover 的 1/3，必须能看清但不能压过真实主物品。
- 标题区、主视觉区、底部短句区分开；不要做成正文信息图或节点墙。
- 用户没有给标题时，生图不要生成长中文标题，只留出标题区，后续本地排版。
- 用户给定标题且短于 12 字时，可以尝试直接生成标题；如果错字明显，重生成无文字底图或后期本地排版。

### 4. 彩蛋长卷生成

彩蛋长卷用于个人经历、项目复盘、产品演化和成长路径。

要求：

- 超横版，约 `2.6:1` 到 `3:1`
- 高级近白背景
- 一条手绘曲线路径贯穿全图
- 5-8 个真实物品节点
- 每个节点都有小黑象参与动作
- 左侧是起点，右侧是当前结论或下一阶段
- 不用编号时间轴，不做 PPT 流程图
- 节点文案短，贴近物品，像手写注释

所有节点必须来自用户提供或可确认的事实。不能把别人的经历、项目和数据套进当前用户身上。

### 5. QA 和迭代

生成后按 `references/qa-checklist.md` 检查。以下任一情况不交付：

- 小黑象缺少短象鼻、小耳朵、短腿或白点眼
- 小黑象变成小黑人、旧小黑、火柴人、黑色人形或普通黑球
- 小黑象只有两条人形腿、火柴腿、膝盖、脚掌、鞋子，或变成二足站姿
- 小黑象变成笨重圆胖玩具、摆件、商品模型或近距离角色特写
- 真实物品太多，像素材拼贴
- 主物品过大，像商品图
- 小黑象只是站在旁边，没有承担动作
- 标签太多、错字明显或像标题
- 画面像 PPT、UI 截图、复杂架构图、商业海报
- 需要长解释才看懂

第一张生成图只算候选图。未过 QA 就重写提示词或重生成。

## Quality Gates

- 2.0 必须出现真实物品和明确物理动作。
- 小黑象必须是小象，不得回退旧小黑。
- 一张图只表达一个处境或冲突。
- 真实物品少而准，一个主物品优先。
- 中文标签短，默认 2-4 个。
- 不虚构未确认事实。
- 生成后必须 QA，不合格不交付。
