# 文章批次小黑象角色锁

## 触发条件

同一篇文章或项目需要 2 张及以上小黑象 2.0 图片时强制执行。单图任务只执行 IP 锁和尺度校准。

## 核心原则

```text
同一文章 = 一个角色母版 + 每个画幅模式一个固定尺度 + 母版冻结后并行扇出 + 每张独立验收
```

只在 Prompt 里写 `same character` 不是锁定。必须把已通过 QA 的可见母版作为后续每张图的图像参照。

## 执行流程

### 1. 建立文章批次

在文章图片目录中创建 `prompts/xiaohei-character-lock.md`，复制 `templates/article-character-lock.md` 的字段。完成标准：文章 slug、计划图数、模式和母版字段均存在。

### 2. 只先做第 1 张

第 1 张必须先通过以下门禁：

- 短象鼻、小圆耳、白点眼、四足短圆桩腿全部正确。
- 形体是低矮、紧凑、轻巧的哑光黑色小象，不是玩具、雕塑或人形。
- 标准 16:9 图的实际高度在 3%—5%；cover / 9:16 在 4%—6%。
- 小黑象承担核心物理动作。

未过关不得开始剩余图片。过关后，记录该图绝对路径，将它冻结为本文章唯一角色母版。

### 3. 冻结形体和模式尺度

从母版记录以下不变量：

- 身体与头部的相对宽高。
- 耳朵大小与位置。
- 象鼻长度、粗细和弯曲程度。
- 四足长度、粗细和身体下方的附着方式。
- 白点眼大小、哑光黑材质和轻巧剪影感。
- 母版在当前画幅模式中的实际高度占比。

同一模式后续图片的小黑象高度相对母版只允许 ±10% 偏差。例如母版为 4.0% 画面高，批次合格区间为 3.6%—4.4%，同时仍不得突破该模式的绝对上限。

### 4. 后续图片始终引用同一母版（且仅此一张）

每张后续图片都要：

- 在 Codex `image_gen` 中将母版的本地绝对路径放入 `referenced_image_paths`，**`referenced_image_paths` 里只放这 1 张母版**（封面任务额外允许 1 张 style 母版）；禁止同时引用多张成图——每张参考图进出上下文都按图像 token 计费，多图引用是 token 膨胀主因（2026-09-09 实测 7 图烧 717 万 input 后固化）。
- 如果母版没有本地路径，只能用能完整包含母版的最小 `num_last_images_to_include`；不要无差别带入多张历史图。
- 在 Prompt 前部写明：参照图只锁定小黑象的形体、比例、材质和当前模式尺度；新场景、动作和物件仍按当张 shot list 生成。
- 如果使用 OpenAI Images API 且当前模型支持，对引用图使用 `input_fidelity=high`；当前工具没有这个参数时，不伪造已启用。

禁止“上一张锁下一张”的串联方式。第 2 张即使合格，也不取代第 1 张母版；否则微小偏差会逐张累积。风格一致性靠 IP 锁定块文本约束 + 唯一母版，不靠多图堆叠。

### 5. 母版冻结后的并行扇出

母版通过 QA 是唯一 barrier。冻结后，02/03/04 等剩余图片互相独立，可默认并行启动最多 3 个 `codex exec`：

1. 每个 worker 只引用同一张不可变母版；不得引用上一张成图，也不得创建新母版。
2. 每个 worker 使用独立的输出文件、Prompt 和 QA 结果；不得写入其他 worker 的文件或共享回执。
3. 每个 worker 完成自己的视觉 QA 后再汇总批次结果；一个 worker 失败不阻塞其他独立 worker。
4. 遇到 API 429、并发限制或工具资源不足时，降低并发或只排队受限 worker；这不是把默认批次改回全串行的理由。
5. 失败 worker 只在自己的 job 内重试，并始终引用同一母版；不得把失败图传给其他 worker 作为参考。

每张生成后都要与母版并排检查。以下任一情况直接重生：

- 同模式小黑象高度相对母版超过 ±10%。
- 虽然高度相近，但黑色体量明显变胖或变瘦。
- 头身、耳鼻、腿部比例与母版明显不同。
- 四足变二足，或腿部因遮挡无法读成四足小象。
- 哑光剪影变成玩具、写实象、萌宠或发光 3D 角色。

重试时不更换母版。优先调整镜头距离、主物件大小和小黑象站位，不用后期缩放、裁切或拼贴伪造通过。

## Prompt 批次锁定块

放在尺度补偿块之后、场景描述之前：

```text
ARTICLE-BATCH CHARACTER MASTER LOCK:
Use the supplied master image as the single source of truth for Xiaohei Elephant 2.0 only.
Preserve exactly the same compact body-to-head proportions, small round ears, short curled trunk, four short rounded peg legs, tiny white-dot eyes, matte-black material, and light silhouette mass.
Within this same canvas mode, preserve the master's elephant height with no more than 10% relative deviation.
Change only the scene, real objects, physical action, pose, and camera placement required by this shot.
Do not copy the master's background or props. Do not reinterpret, enlarge, slim, fatten, stylize, or age the elephant.
The master remains unchanged for every image in this article; never use the previous generated image as a new master.
```

## 画幅模式边界

- 16:9 正文图：比较同批次 16:9 图的尺度，同时遵守 3%—5% 绝对门禁。
- 21:9 cover：可共用同一 IP 形体母版，但建立独立 cover 尺度基准，遵守 4%—6%。
- 9:16 视频封面：可共用同一 IP 形体母版，但建立独立竖版尺度基准，遵守 4%—6%。
- 不跨画幅模式直接比较百分比；跨模式只比较 IP 形体与材质。

## 完成标准

- `prompts/xiaohei-character-lock.md` 已记录唯一母版路径和各模式尺度基准。
- 所有后续图都直接引用同一母版，没有串联参照；母版冻结后已按独立 job 并行或在限流时按 worker 排队。
- 所有同模式图中，小黑象尺度相对母版在 ±10% 内，且满足该模式绝对占比。
- 形体、耳鼻、四足、眼睛和材质与母版一致。
