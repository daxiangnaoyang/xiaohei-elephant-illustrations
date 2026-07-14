# 小黑象 2.0 GOTCHAS

## OpenAI 入口为空

- 现象：`SKILL.md` 和 `references/` 已经补了 2.0 规则，但 OpenAI 侧调用时仍像旧版小黑，或完全没吃到 `prompt-template.md`、`style-dna.md` 和母版锁定。
- 原因：`agents/openai.yaml` 只有 `{}` 或只写了 display name，没有在 `default_prompt` 里显式要求读取 2.0 的共享约束和 QA。
- 处理：`agents/openai.yaml` 必须把默认调用链写清楚：先 `Use $xiaohei-elephant-scenes`，再读取 `references/xiaohei-elephant-ip-lock.md`、`references/style-dna.md`、`references/prompt-template.md`、`references/object-patterns.md`、`references/qa-checklist.md` 和本文件；同时写清 2.0、1.0、旧版 `xiaohei-scenes` 的路由边界。

## 漂移成旧小黑

- 现象：图里角色像黑色人形、小黑人、火柴人、圆头小黑，甚至没有象鼻。
- 原因：只写“小黑”或“Xiaohei”，没有写死小黑象形体。
- 处理：提示词必须写“black elephant, short trunk, small ears, short legs, white-dot eyes, non-humanoid”。没有象鼻和小耳朵直接判失败。

## 真实物品抢主角

- 现象：画面像商品摄影，小黑象变成角落装饰。
- 原因：主物品太大、太精致、太居中，小黑象没有动作。
- 处理：小黑象必须推、拉、挡、托、修、检查、盖章、拉绳或守门。去掉小黑象后画面仍成立，说明失败。

## 比原版小黑 2.0 缺质感

- 现象：小黑象变成厚重 3D 玩具小象，主物品和角色占比过大，中文标签像左右两侧大标题，彩色便签/抽屉/纸片面积过大，整体像商品棚拍或儿童玩具广告。
- 原因：提示词只写死了“小黑象形体”，没有写死原版 `xiaohei-scenes` 的画面导演规则和小黑象自身占比。旧版小黑虽然高度约 8%-13%，但细胳膊细腿导致黑色体量很轻；小黑象是低矮实体剪影，同样高度会显得大且笨重。
- 处理：生成前按 `references/style-dna.md` 的“原版小黑 2.0 质感锁定”重写 prompt；标准图小黑象高度锁到 3%-5% 画面高，cover 锁到 4%-6%，黑色视觉体量约为此前测试图的 1/3，且不得超过主物品高度的 1/3；生成后按 `references/qa-checklist.md` 拦截 3D 玩偶化、商品摄影化、标题化标签、色块过载和 close-up。第一张候选不过关时，不调色微修，直接重写物件预算、角色占比和镜头距离后重生成。

## 镜头太靠前，小黑象显笨重

- 现象：角色和主物件离观众太近，小黑象圆胖、腿粗短、像摆件，画面失去原版小黑 2.0 那种轻巧、灵活、留白里的荒诞感。
- 原因：提示词只说“小象”和“真实物品”，模型容易把它理解成玩具摄影或可爱小象模型；同时缺少明确的 camera pulled back / airy white space / nimble silhouette 约束。
- 处理：标准图默认把镜头后退一档，整体场景只占画面中等偏小区域；小黑象写成 `tiny nimble solid black elephant silhouette`，标准图高度 3%-5% 画面高，cover 高度 4%-6%，强调小执行者、紧凑轻巧身体、动作拉伸感。出现 close-up、低机位英雄镜头、圆胖摆件感或占比过大时直接重生成。

## 象腿漂移成小黑人腿

- 现象：整体镜头和比例对了，但小黑象只剩两条细腿，像原版小黑角色或小黑人加了一根象鼻；腿部出现膝盖、脚掌、鞋子或二足站姿。
- 原因：`thin peg legs` 容易被模型理解成火柴腿/人形腿；角色动作如果写“站立、伸手、够到”，也容易变成二足小黑。
- 处理：提示词必须写 `FOUR SHORT ROUNDED ELEPHANT PEG LEGS under the body, quadruped stance`，并禁止 `biped pose, human legs, stick legs, knees, feet, shoes`。动作优先由短象鼻完成，不给小黑象加人类手臂或手掌。

## Cover 版混成正文信息图

- 现象：用户要“小黑象 2.0 cover”，结果输出成 16:9 白底正文图、正文节点墙或密集信息图。
- 原因：正文图和封面图没有分模式；只套用了标准 2.0 小现场模板。
- 处理：Cover 版必须单独走 21:9 超横版，参考 `_skill-staging/wechat-tech-article-infographic` 的深色科技感、青橙对比、HUD/玻璃拟态/发光连接线要求；小黑象 2.0 只承担一个核心真实物品隐喻。没有明确标题时不让模型生成长中文标题，留出本地排版区域。

## 物品清单化

- 现象：把文章里的所有名词都变成道具，画面像素材堆。
- 原因：没有先提炼核心冲突。
- 处理：每张图只保留一个真实主物品或紧凑物品组，最多 1-2 个辅助道具。

## 和 1.0 混用

- 现象：用户要真实物品，但输出成纯手绘解释图；或用户只要白底手绘，却输出摄影物品。
- 处理：白底手绘解释图用 `xiaohei-elephant-illustrations`；真实物品小现场和彩蛋长卷用 `xiaohei-elephant-scenes`。

## 长卷变流程图

- 现象：彩蛋长卷变成编号时间轴、流程图、PPT 模块。
- 处理：使用一条手绘曲线路径串联 5-8 个真实物品节点；节点不编号，靠物品、动作和短标签讲故事。

## 把 Codex 内置生图误解成仓库自带 OpenAI Key

- 现象：GitHub 用户问“这个 Skill 要不要 OpenAI key”“为什么复制到原生 GPT 不能自动生成并保存图片”“模型到底选哪个”。
- 原因：2.0 真实物品场景图更依赖图像模型质量，但如果只写“用 Codex 生成”，容易被理解成仓库自带托管服务或任何 GPT 都能直接安装运行。
- 处理：复用 `../xiaohei-elephant-illustrations/references/generation-runtime-notes.md`。对外固定说法：仓库只是 Skill / prompt / workflow 包；Codex 当前环境暴露内置 `image_gen` 时默认用 Codex 生图，通常不需要额外在仓库里配置 OpenAI API key；其他环境要接自己的图像生成通道，走 OpenAI Images API 或第三方服务时使用自己的 key、余额和权限；原生 GPT 只能复制 prompt 手动使用，不能自动执行本地文件流。

## 混淆文本模型和图像模型

- 现象：用户用一个文本聊天模型跑完整流程，然后期待它直接画出 2.0 真实物品场景图。
- 原因：没有说明“读文章/写 prompt/QA”和“真正出图”是两层能力。
- 处理：2.0 每次出图前都要说明：文本模型负责提炼处境、真实物品和物理动作；图像模型负责生成图片。没有可用图像工具时，只交付 prompt 和 QA 清单，不承诺已出图。
