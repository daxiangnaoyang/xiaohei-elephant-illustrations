# 小黑象 2.0 Prompt Template

## 标准 16:9 正文图

```text
生成一张 16:9 横版中文正文配图。

尺度补偿锁（必须置于最终英文 Prompt 的前 8 行）：

```text
SCALE IS THE FIRST PRIORITY.
Use an extreme wide, pulled-back camera.
The elephant is a tiny distant worker: target only 1.5%-2.5% of full canvas height.
The main real object is at least 6x taller than the elephant.
The real-object tableau follows the selected density mode: D1 = 42%-56% canvas width and 24%-34% height; D2 = 50%-64% width and 28%-40% height; D3 = 56%-70% width and 32%-48% height.
Keep the camera pulled back and preserve generous near-white space: 65%+ for D1, 55%+ for D2, and 48%+ for D3.
If the elephant would be larger to make its action readable, make the OBJECT larger instead; never enlarge the elephant.
```

最终实际验收仍是小黑象高度约 3%—5%；超标时按 [`scale-calibration.md`](scale-calibration.md) 的 B/C 档重写构图并重生成。

如果是同一文章的第 2 张及以后图片，尺度补偿块之后必须加入下列批次锁，并将已验收的唯一母版放入 `referenced_image_paths`：

```text
ARTICLE-BATCH CHARACTER MASTER LOCK:
Use the supplied master image as the single source of truth for Xiaohei Elephant 2.0 only.
Preserve exactly the same compact body-to-head proportions, small round ears, short curled trunk, four short rounded peg legs, tiny white-dot eyes, matte-black material, and light silhouette mass.
Within this same canvas mode, preserve the master's elephant height with no more than 10% relative deviation.
Change only the scene, real objects, physical action, pose, and camera placement required by this shot.
Do not copy the master's background or props. Do not reinterpret, enlarge, slim, fatten, stylize, or age the elephant.
The master remains unchanged for every image in this article; never use the previous generated image as a new master.
```

首张未过 QA 前不得批量生成剩余图片。完整流程见 [`article-batch-character-lock.md`](article-batch-character-lock.md)。

段落级信息编译（必须先读完整段落，不得只摘主题词）：

```text
原始段落 / 小节正文：{完整段落文本；不能只填标题或主题}
段落主旨 / 一句话结论：{这一段真正想让读者理解或记住的判断}
段落类型 / 结构：{单一判断 / 因果机制 / 流程步骤 / 对比转折 / 组成层级 / 决策筛选 / 反馈闭环 / 案例复盘，选一个主结构}
读者处境 / 输入问题：{这一段回应的具体问题、卡点或起始状态}
独立信息节点：{不要只列主题词；列出段落中不能互相替代的输入、机制、角色、条件、阶段、证据、结果或边界}
必须看见的节点及承载方式：{节点 1 -> 真实物件/状态；节点 2 -> 动作/空间位置；节点 3 -> 结果/短标签；必要时继续列到节点 6}
结果 / 判断 / 边界：{动作完成后发生什么，或这一段给出的限制条件}
密度档位：{D1 轻量 / D2 解释型 / D3 综合型；按下方规则选择，不得默认 D1}
视觉关系类型：{流程 / 因果 / 对比 / 组成 / 层级 / 闭环 / 决策门，选一个}
可见信息链：{输入/困境} -> {机制/小黑象动作} -> {输出/结果/边界}
3 秒读懂句：{不看正文时，观众第一眼应该读出的“处境/动作/结果”完整意思}
可选段落锚点短句：{4-8 个字；只有关系不够清楚时使用，不写成长标题}
```

DENSITY CALIBRATION LOCK:

```text
This is a paragraph-level visual summary, not a single-topic decorative illustration. First understand the complete paragraph and count its independent information nodes; do not automatically render every paragraph as a minimal two-object metaphor.
DENSITY MODE D1 - LIGHT: Use only when the paragraph contains one independent claim, one main condition, and one visible action or state change. Use 1 hero real object plus 1 supporting object, 2-3 short labels, and 2-3 visible information nodes. D1 is an exception, not the default.
DENSITY MODE D2 - EXPLANATORY DEFAULT: Use for a normal explanatory paragraph with a claim, a concrete context, 1-2 mechanisms, and a result or boundary. Use 1 hero real object plus 2-3 semantically necessary supporting objects, 3-4 real-object/state units, 4-5 short labels, and 3-4 visibly connected information nodes.
DENSITY MODE D3 - COMPREHENSIVE: Use when the paragraph contains a causal chain, 3 or more steps/elements, multiple roles or conditions, a comparison/turn, a decision branch, feedback, or a result with an explicit boundary. Use 1 hero real object or compact hero group plus 3-5 semantically necessary supporting objects/state units, 4-6 real-object/state units, 5-7 short labels, and 4-6 visibly connected information nodes. D3 is still one coherent physical tableau, not a card grid or PPT infographic.
The density mode is a content decision, not a decoration preference. A paragraph containing words or logic such as “因为/所以/但是/如果/同时/最终/第一/第二/否则”, multiple independent verbs, or a list of stages must not be compressed into D1 just to preserve empty space.
Every required node must have a visible encoding: a real object, object state, spatial position, physical contact/action, relationship line, or short label. Do not merge mechanism, condition, and result into one generic object or one vague slogan.
Choose one visual grammar that matches the paragraph: a left-to-right or foreground-to-background physical chain for process/causality, a before/after split for contrast, nested or stacked objects for composition/hierarchy, a gate/filter with a visible branch for decision, or one curved path with 3-5 physical nodes for a loop.
Use one main physical action chain; D3 may add one branch, gate, or before/after turn when the paragraph requires it. Connect the visual units with a clear hand-drawn path, arrow, divider, barrier, contact relationship, or state change. Do not place isolated objects in a row.
Use D1: 2-3, D2: 4-5, or D3: 5-7 short Chinese annotation labels, each 2-6 characters, attached to the relevant object, stage, relationship, or boundary. Labels name information; they are not decorative slogans and must not become paragraphs.
More information must be expressed through hierarchy, state changes, and relationships before adding color or text. Keep the camera pulled back, the elephant tiny, and the scene physically believable; expand the real-object tableau when density rises, never enlarge the elephant or move into a close-up.
```

主题：{主题}
读者处境：{读者处境}
核心冲突句：{核心冲突句}

画面：
纯白或接近纯白摄影棚背景，大量留白。
段落主旨必须通过可见结构表达：{段落主旨 / 一句话结论}。
段落类型与密度档位：{段落类型} / {D1、D2 或 D3}；该档位选择依据：{独立信息节点数量与段落逻辑}
必须看见的信息节点：{节点 1}、{节点 2}、{节点 3}、{节点 4；D3 可继续到节点 6}；每个节点的视觉承载：{物件 / 状态 / 动作 / 位置 / 关系线 / 短标签}
真实主物品是：{真实主物品}，它承载段落的主论点。
辅助物品 / 状态单元是：{按 D1/D2/D3 填 1 / 2-3 / 3-5 个}；每个辅助物品或状态单元分别承载：{对应信息节点与语义职责}。
画面结构是：{视觉关系类型}，严格呈现：{可见信息链}。
核心物理动作是：{核心物理动作}；小黑象正在：{小黑象动作}。
结果或边界必须在画面中可见：{结果 / 判断 / 边界}。
关系标记是：{一条主路径 / 箭头 / 分隔线 / 闸门 / 接触关系；D3 只允许额外一个分支或前后转折}。
可选段落锚点短句：{4-8 个字；没有必要时删除，不生成占位文字}。

真实品牌标识规则：
- If the topic explicitly involves a real product, platform, app, or company, include the authentic official brand logo / app icon / product mark on the relevant real object.
- Examples: for Feishu/Lark scenes, use the official Feishu/Lark brand logo or app icon on a card, app tile, folder, document, or small device screen; for Codex/OpenAI scenes, use the official OpenAI logo or Codex/OpenAI product mark on the relevant card, app tile, terminal tile, folder, or device screen.
- The logo must be small, accurate, and attached to a real object as an identification cue. Do not invent fake logos, distorted lookalike logos, parody marks, or unofficial pseudo-branding.
- Do not turn the image into a brand advertisement, product KV, sponsorship poster, or app screenshot. The physical action remains the main story.
- If the brand is not explicitly named or cannot be confirmed, use a generic neutral icon instead of guessing a brand logo.

原版小黑 2.0 质感锁定：
- Treat the original Xiaohei Scenes 2.0 examples as the quality bar for restraint, whitespace, object realism, sparse labels, and clear physical action.
- Pull the camera back. Scene footprint should be small-to-medium and airy: about 46%-58% of canvas width and 26%-38% of canvas height.
- Scale down the Xiaohei Elephant itself aggressively. In standard 16:9 images, the elephant height should be only 3%-5% of canvas height, and its black visual mass should feel about one third of the previous oversized elephant tests. The elephant must be clearly smaller than the main real object, never taller than one third of the main object's height.
- Do not force every paragraph into the same sparse composition. D1 is only for a genuinely single-claim paragraph; D2 is the default for explanatory paragraphs; D3 is required when the paragraph contains multiple mechanisms, stages, roles, conditions, comparisons, branches, or boundaries.
- D1 uses 1 hero + 1 support; D2 uses 1 hero + 2-3 supports; D3 uses 1 hero/compact hero group + 3-5 supports or state units. Every unit must map to a named paragraph node, stage, role, condition, result, or boundary; no decorative props.
- Use one coherent paragraph-level visual structure: process/causality, before/after, nested composition, gate/filter, or feedback path. D3 may show a compact foreground/midground/background chain or one visible branch, but never a card grid, dashboard, node wall, or dense PPT infographic.
- The whole paragraph must be readable from the visible combination of objects, states, actions, relationships, and short labels; do not rely on the article text to supply the missing mechanism or result.
- Keep the whole image airy with generous empty white space around the scene. Do not make a close-up, low-angle hero shot, product hero shot, toy photography poster, or dense object pile.
- Use only very light contact shadows under objects and the elephant. No grey background, no vignette, no gradient, no heavy studio shadow.
- The image must still read as one strange but precise physical moment, not a concept poster.

小黑象硬性要求：
Use the full `Xiaohei Elephant 2.0 IP lock` from `references/xiaohei-elephant-ip-lock.md`. The following is the minimum lock:
ELEPHANT (FIXED IP CHARACTER — MUST BE CONSISTENT ACROSS ALL IMAGES):
A tiny solid BLACK baby elephant with these EXACT features:
- SIZE LOCK: standard 16:9 image height only 3%-5% of canvas height; black visual mass about one third of previous oversized elephant tests; never taller than one third of the main real object's height
- Short stubby trunk, about as wide as its head, like a tiny curled hose, does NOT reach the ground
- Two small round ears, like buttons on each side of a round head
- Four short rounded elephant peg legs attached under the body, quadruped stance. Front and rear legs may be partly hidden by the body but it must NOT become two human-like legs, stick legs, knees, feet, shoes, or a biped standing pose.
- Two tiny white dots for eyes, no pupils, no detailed eye shapes
- Small rounded bean-shaped body, compact and agile, NOT bulky, NOT realistic elephant proportions
- Looks like a baby elephant silhouette, NOT a bear, NOT a pig, NOT a human figure, NOT a stick figure, NOT a robot
- CONSISTENT across all images: same shape, same proportions, same style every time
- Matte black simplified silhouette with minimal form detail; light, nimble, slightly stretched by the action; NOT glossy thick 3D toy, NOT plush mascot, NOT realistic elephant figurine, NOT cute children's character, NOT heavy round statue.
- The trunk does the reaching or touching action. Do not give the elephant human arms or hands.

文字：
中文手写短标签：{D1 填 2-3 个；D2 填 4-5 个；D3 填 5-7 个}
标签要短、清楚、像手写批注；每条标记一个信息节点、关系或边界，不要长句，不要标题，不要把整段正文缩写进图里。
如确有必要，可加入一条 4-8 字的段落锚点短句；它只能帮助读者抓住主旨，不得变成海报标题或正文段落。
Labels should sit close to the object or action like annotations, underlines, arrows, or tiny notes. Do not put oversized title-like slogans on both sides of the image.

风格：
真实物品有自然光影和轻微摄影质感；小黑象可以是简化黑色角色，但必须和真实物品发生物理互动。
Use restrained hand-drawn educational annotation language: small arrows, underlines, circles, simple dividers, check marks, or a gate only when they clarify the paragraph's structure. Do not add decorative pastel cards, large title blocks, or ornamental infographic modules.
Color restraint: keep black lines and text on a pure or near-white background. Use pale blue `#A8D8EA`, mint `#B5E5CF`, lavender `#D5C6E0`, or pale peach `#F4C7AB` only as small object details or annotation patches; use coral red `#E8655A` for at most one key state, arrow, or check mark. Do not fill large cards or turn the scene into a pastel infographic.
画面轻、怪、清爽，有留白。
少量蓝 / 黄 / 红 / 橙点缀。彩色只做节奏点，4-6 个小点缀即可；不要大面积彩色便签堆、彩色抽屉标签或彩色纸片铺满画面。

避免：
PPT 信息图、卡片网格、节点墙、复杂流程图、UI 截图、仪表盘、科技 HUD、商业海报、深色背景、没有关系的物件排队、无语义的物品堆满、商品摄影感、玩具棚拍感、近距离特写、低机位英雄镜头、笨重圆胖小象、二足站姿、人形腿、火柴腿、鞋子脚掌、中文错字、大段文字、小黑象站在旁边不动、把解释型段落压成一个主题物件、D2/D3 段落误用 D1、只画主题名词而不表达机制和结果。
```

## Cover 版 21:9 单图

```text
生成一张 21:9 超横版公众号封面图。Cover 版是单独的一张，不是正文 16:9 配图。

封面主题：{封面主题，必须填写}
主标题（逐字准确显示）：{主标题，必须填写；用户未提供时先根据主题生成，禁止留空}
标题重点词：{1-2 个需要用珊瑚红 #E8655A 突出显示的词}
可选副标题：{副标题；没有则删除本行，不生成占位文字}
底部金句（逐字准确显示）：{一句短、锋利、有观点的金句；用户未提供时先生成，禁止留空}
封面级视觉隐喻：{一个真实物品冲突 + 小黑象核心动作}

具体图解内容（必须真实画进画面，不能只作为抽象说明）：
- 起点物件 / 困境状态：{可被看见、可触碰的真实物件或状态}
- 小黑象核心物理动作：{小黑象用短象鼻执行的推 / 拉 / 接通 / 分拣 / 盖章 / 修补等动作}
- 结果物件 / 转折状态：{动作完成后可见的结果}
- 物理链路：{起点 -> 动作 -> 结果，最多 3 个连续状态}
- 画面 3 秒读懂句：{观众第一眼应该读出的意思}
- 真实主物品：{一个核心真实物品或紧凑物品组}

画面：
深色科技背景，青橙对比，轻微纸张纹理，弱 HUD 网格，玻璃拟态卡片，发光连接线，手绘科技信息图质感。
参考 `wechat-tech-cover-image` 的科技感公众号封面要求，但这是一张小黑象 2.0 cover：主标题区、具体图解区、底部金句区必须同时存在且层级分明。标题是第一视觉中心，图解负责讲清主题，金句负责补充观点；不做密集正文信息图。
黑象可读性优先：黑色小黑象不能直接压在黑色背景上。必须给小黑象和核心物件设置浅色台面、暖色聚光区、浅色纸面或清晰边缘光，让黑色剪影在 1 秒内可见。
隐喻可读性优先：必须按上面的“具体图解内容”画出可见的起点、动作和结果，只用一个主动作串起画面，例如“稿件 -> 小黑象用象鼻推过验收门 -> 进入通过托盘”。避免抽象漂浮面板、复杂 HUD、节点墙和无法 3 秒读懂的科技装饰。

小黑象 2.0 主体：
Use the full `Xiaohei Elephant 2.0 IP lock` from `references/xiaohei-elephant-ip-lock.md`. Minimum lock:
A tiny nimble solid BLACK elephant silhouette, SHORT TRUNK, SMALL ROUND EARS, FOUR SHORT ROUNDED ELEPHANT PEG LEGS under the body, WHITE DOT EYES, compact agile body.
Scale lock: in cover images the elephant height is only 4%-6% of canvas height. The black visual mass should feel about one third of the previous oversized cover tests. It must be readable, but clearly smaller than the main real object and never the dominant visual mass.
Quadruped elephant stance only. No biped standing pose, no human legs, no stick legs, no knees, no feet, no shoes.
Matte black simplified silhouette with visible contour separation from the dark background; not glossy 3D toy, not plush mascot, not realistic elephant figurine, not heavy round statue.

真实物品：
一个核心真实物品或紧凑物品组：{真实主物品}。
严格呈现这条具体物理链路：{起点物件 / 困境状态} -> {小黑象核心物理动作} -> {结果物件 / 转折状态}。
小黑象用短象鼻参与核心动作：{小黑象核心物理动作}。
如果主题明确涉及真实品牌 / 产品 / App，核心真实物品可以带对应官方品牌 logo、app icon 或产品标识。Examples: Feishu/Lark scenes use the official Feishu/Lark brand logo or app icon; Codex/OpenAI scenes use the official OpenAI logo or Codex/OpenAI product mark. Keep the logo accurate, small, and object-bound. Do not invent fake logos or turn the cover into a brand ad.

文字与字体（verbatim，必须大、清晰、可读）：
主标题：“{主标题}”
可选副标题：“{副标题；没有则删除}”
底部金句：“{底部金句}”

Typography: 标题区顶部居中放置中文粗体大号手绘主标题（bold, large, hand-drawn lettering），带真实手写字的轻微不规则边缘与 wobble。线条和主文字使用黑色；标题中的“{标题重点词}”使用珊瑚红 `#E8655A`。辅助短标签使用暖灰 `#6B6B6B` 小字，每条 2-5 词。深色科技底图必须增加暖白纸张标题区、浅色卡片或等价浅色承载面，确保黑色手绘字可读，禁止擅自改成白色细黑体。底部金句字号明显小于主标题，短而锋利，不抢主标题。

Decoration: 只加入少量手绘涂鸦点缀，如小星星、珊瑚红下划线、小箭头、勾选标记；保持充足留白和干净构图，不堆装饰。

Allowed text only: “{主标题}”；“{可选副标题}”；“{底部金句}”；{必要的 1-3 个图解短标签}。不要生成额外伪文字、英文乱字、乱码、水印或可读 HUD 小字。

ONE-PASS INTEGRATED COMPOSITION LOCK:
- Generate the background, real objects, Xiaohei Elephant, main title, highlighted words, bottom quote, and necessary labels together in ONE image-generation pass.
- Typography is an intrinsic visual material in the scene, not a later overlay. It must share the same paper texture, lighting, perspective, hand-drawn edges, and decorative language as the illustration.
- Do NOT create a blank/no-text background for later typesetting. Do NOT paste a white title card, text box, flat digital text layer, or local-script typography over a finished image.
- A locally rendered `ZCOOL KuaiLe` title reference may be supplied only as a visual reference for glyph shape, hierarchy, line breaks, and color. The final cover must still be generated as one coherent image.
- If text is unstable, shorten the title, split it into at most two lines, reduce the allowed text list, strengthen the verbatim text instruction, and regenerate. Never switch to post-overlay.

COVER TYPOGRAPHY RUNTIME CONTRACT:
- Use the reference image only as `TYPOGRAPHY_REFERENCE_ONLY`; it is not a title layer, mask, transparent PNG, or compositing source.
- The only image-generation inputs allowed for this Cover are the typography reference and necessary Xiaohei IP master references. Never pass a `*-base.*`, `*-overlay.*`, `*text-layer*`, `*composite*`, `*merged*`, previous Cover, or any locally composited image as a text-fix input.
- `generation_passes` must be `1`. If the model produces standard tech sans, geometric sharp-corner lettering, UI text, or a visually different font, reject the whole candidate and regenerate a new one; do not edit or overlay text afterward.
- After visual inspection, write `cover-typography-receipt.md`. If visual QA is unavailable or returns 400/429/timeout/any error, set `visual_qa: BLOCKED` and do not deliver the candidate.

构图：
21:9 horizontal, cinematic wide cover. Main title sits on the left/top or upper-middle as the strongest visual layer and is visually connected to the concrete physical illustration through shared paper texture, lines, arrows, light, or object geometry. Bottom quote sits in a separate but materially consistent safe area. Keep all three zones readable and connected: title -> illustration -> quote. Clean visual hierarchy, not a dense information wall or a detached text-over-photo layout.
If using a dark background, place the elephant on a small warm off-white tabletop island / paper surface / spotlight zone, or add a subtle cyan rim light and thin warm edge light. The elephant must not disappear into black.

避免：
主题缺失、主标题缺失、底部金句缺失、具体图解缺失、只画科技氛围底图、先无字底图后本地叠字、白色标题卡覆盖场景、文字像后贴的 PPT 文本框、标题悬浮在大面积空白上、标题与物件没有视觉联系、标题太小、标题未顶部居中、使用白色细黑体或标准科技黑体代替粗体手绘字、关键词未使用珊瑚红 #E8655A、辅助标注不是暖灰 #6B6B6B、金句抢标题、涂鸦装饰过多、黑底黑象看不清、抽象科技面板看不懂、正文信息图式密集节点、PPT 流程图、无依据的伪品牌 logo、错误 logo、logo 抢主角、品牌广告 KV、伪文字 HUD、复杂仪表盘、营销海报大字压满、写实人物、机器人角色、小黑人、旧小黑、人形腿、二足站姿、笨重玩具小象。
```

## 9:16 视频封面分支（小黑象 2.0 Cover Branch）

```text
生成一张 9:16 竖版中文短视频封面图。它是小黑象 2.0 Cover 的视频分支，必须重新设计竖向构图，不得把 21:9 横版封面直接裁切、拉伸或上下加黑边。

封面主题：{封面主题，必须填写}
主标题（逐字准确显示）：{主标题，必须填写；用户未提供时先根据主题生成，禁止留空}
标题重点词：{1-2 个需要用珊瑚红 #E8655A 突出显示的词}
底部金句（逐字准确显示）：{一句短、锋利、有观点的金句；用户未提供时先生成，禁止留空}
封面级视觉隐喻：{一个真实物品冲突 + 小黑象核心动作}

具体图解内容（必须真实画进画面，不能只作为抽象说明）：
- 起点物件 / 困境状态：{可被看见、可触碰的真实物件或状态}
- 小黑象核心物理动作：{小黑象用短象鼻执行的推 / 拉 / 接通 / 分拣 / 盖章 / 修补等动作}
- 结果物件 / 转折状态：{动作完成后可见的结果}
- 竖向物理链路：{起点 -> 动作 -> 结果；最多 3 个连续状态，优先上下或斜向排列}
- 画面 3 秒读懂句：{观众在手机缩略图上第一眼应该读出的意思}
- 真实主物品：{一个核心真实物品或紧凑物品组}

构图与手机安全区：
- 9:16 vertical, standalone short-video cover, designed for a phone screen and thumbnail view.
- 顶部 0%-12% 和底部 84%-100% 是平台 UI 安全区：不放主标题、底部金句、关键物件、象鼻动作或关键标签；保持低信息密度。
- 标题区位于画面 14%-32%：水平居中，主标题最多两行，建议总字数 8-16 个汉字；在手机缩略图上仍要一眼读清。
- 主视觉区位于画面 34%-72%：一个真实主物品和一条清晰的上下/斜向物理链路。主视觉居中或略偏下，不横向铺开，不做道具排队。
- 金句区位于画面 75%-83%：只放一句短金句，字号明显小于主标题；必须高于底部 UI 安全区。
- 标题、主视觉、金句之间要由同一条光线、纸张边缘、箭头或物理动线连接，形成“标题 -> 动作 -> 结果”的单一阅读路径。

画面风格：
深色科技背景，青橙对比，轻微纸张纹理，弱 HUD 网格，少量玻璃拟态卡片和发光连接线；视觉密度比 21:9 更低，中央保留一块浅色台面、暖白纸面或暖色聚光区承载真实物品和小黑象。不要生成平台按钮、播放图标、字幕条、头像、点赞评论图标、时间戳或可读 HUD 小字，平台 UI 由发布端添加。

小黑象 2.0 主体：
Xiaohei Elephant 2.0 IP lock:
A tiny nimble solid BLACK baby elephant silhouette, matte black cutout body, tiny white dot eyes, short stubby trunk like a small curled hose, small round ears, compact low body.
Scale lock: in this 9:16 video cover, elephant height is only 4%-6% of canvas height. Its black visual mass should feel about one third of previous oversized cover tests and never exceed one third of the main real object's height.
FOUR SHORT ROUNDED ELEPHANT PEG LEGS under the body, quadruped stance.
Front and rear legs may be partially hidden by the body or perspective, but it must still read as a four-legged baby elephant.
The trunk performs the main action. Do not add human arms or hands.
No biped pose, no human legs, no stick legs, no knees, no feet, no shoes.
Not a humanoid Xiaohei, not a black human silhouette, not a stick figure, not a robot, not a bear, not a pig.
Not a glossy 3D toy, not plush mascot, not realistic elephant figurine, not cute children's character, not heavy round statue.

真实物品与动作：
只保留一个真实主物品或紧凑物品组：{真实主物品}。
严格画出这条竖向物理链路：{起点物件 / 困境状态} -> {小黑象用短象鼻执行的核心动作} -> {结果物件 / 转折状态}。
小黑象必须与物件发生真实接触；删掉小黑象后，画面的“动作缺口”应当明显存在。
如果主题明确涉及真实品牌 / 产品 / App，可以在具体物件上使用对应官方 logo、app icon 或产品标识；logo 只能是小型识别锚点，不做品牌广告，不虚构 logo。

文字与字体（verbatim，必须大、清晰、可读）：
主标题：“{主标题}”
底部金句：“{底部金句}”
必要短标签：{最多 1-3 个，非必需}

Typography: use bold, large, hand-drawn Chinese lettering. Put the title in the upper safe content zone, centered on the vertical axis, with at most two lines. Main title strokes and words are black on a warm off-white paper panel or equivalent light material; highlight “{标题重点词}” in coral red #E8655A. Use warm gray #6B6B6B only for tiny nearby annotations. The bottom quote is one short line, clearly smaller than the title and never inside the bottom UI safe zone.

ONE-PASS INTEGRATED COMPOSITION LOCK:
- Generate the 9:16 background, real objects, Xiaohei Elephant, main title, highlighted words, bottom quote, and necessary labels together in ONE image-generation pass.
- Typography is part of the same physical scene: it shares paper texture, lighting, perspective, hand-drawn edges, and visual motion with the illustration.
- Do NOT crop a 21:9 cover, stretch a horizontal composition, add black bars, create a blank background for later typesetting, paste a title card, or overlay text with a local script.
- A locally rendered ZCOOL KuaiLe title reference may be supplied only as visual guidance for glyph shape, hierarchy, line breaks, and color. The final 9:16 cover must render all allowed text natively inside the scene.
- Allowed text only: “{主标题}”；“{底部金句}”；{必要的 1-3 个图解短标签}。不要生成额外伪文字、英文乱字、乱码、水印、平台 UI 或可读 HUD 小字。

COVER TYPOGRAPHY RUNTIME CONTRACT:
- The typography reference is `TYPOGRAPHY_REFERENCE_ONLY`; never paste it, use it as a mask, or create a separate transparent title image.
- Generate the full vertical cover once. Do not use `*-base.*`, `*-overlay.*`, `*text-layer*`, `*composite*`, `*merged*`, a previous Cover, or a local text overlay as an input or repair stage.
- If the title drifts away from the rounded, slightly irregular ZCOOL KuaiLe handwriting, reject and regenerate the complete Cover. `generation_passes` remains `1` per candidate.
- Create `cover-typography-receipt.md` after visual QA. QA 不可用、400、429、timeout or any parsing error means `visual_qa: BLOCKED`; never deliver that candidate.

缩略图与视觉验收：
第一眼先读到主标题和一个明确动作；缩小到手机缩略图后，仍能区分真实主物品、小黑象的短象鼻动作和结果状态。主视觉不超过画面宽度约 78%，小黑象高度约 4%-6%，不成为吉祥物主角。整体轻、怪、清楚，不像 PPT、课程海报、商品广告或密集信息图。

避免：
21:9 横版直接裁切、横向道具排队、顶部贴边标题、底部 UI 区放字、标题超过两行、长副标题、字幕条、播放按钮、头像、点赞评论图标、时间戳、复杂 HUD、节点墙、流程图、过多物件、黑底黑象看不清、小黑象过大、二足站姿、人形腿、火柴腿、脚掌鞋子、旧版小黑、小黑人、3D 玩偶象、萌宠象、品牌广告 KV、中文错字、伪文字。
```

## 9:16 扇面内容视觉分支（Fan-Surface Content Variant）

```text
生成一张 9:16 竖版中文短视频封面图。使用“扇面内容”作为平面主画布，把已确认视频文稿压缩成“一个版面上的核心判断”。这是平面内容构图，不是实体折扇，不是手持实拍，不是扇子图标，也不是 21:9 横版封面裁切。

封面主题：{{TOPIC}}
主标题（逐字准确显示）：{{TITLE_TEXT}}
标题重点词：{{TITLE_EMPHASIS}}
文稿一句话核心判断：{{SCRIPT_CORE}}
扇面内容画布样式：{{SURFACE_STYLE}}
版面主强调色：{{ACCENT_COLOR}}
气泡批注文字：{{SIDE_NOTES}}
批注气泡框：{{CALLOUT_BUBBLES}}
卡通简笔图标：{{CARTOON_ICONS}}
红色印章/印记：{{RED_SEALS}}
背景平面：{{BACKGROUND_CONTEXT}}
底部金句（逐字准确显示）：{{BOTTOM_QUOTE}}

品牌主元素（必须出现且只能选一个模式）：{{BRAND_ANCHOR_MODE}}
品牌锚点的平面位置与视觉关系：{{BRAND_ANCHOR_RELATION}}

参考图反推的不变量：
- 一块平面扇面内容画布，浅蓝、灰白或暖白底，允许纸张纤维和轻微不规则边缘，但不能出现扇片、扇骨、扇柄、折痕、手或可辨识的扇形实体轮廓。
- 中央视觉是 {{ACCENT_COLOR}} 的手绘泼墨/刷痕色块，黑色中文手写大字直接融入平面内容画布。
- {{SIDE_NOTES}} 分别放在 2-4 个不规则手绘气泡框中，气泡有箭头或尾巴指向相关标题词、图标或色块，形成“问题 / 机制 / 结果或边界”的辅助阅读路径。
- {{CARTOON_ICONS}} 是 2-4 个与 {{SCRIPT_CORE}} 直接相关的卡通简笔图标，线条轻、尺寸小，不是随机贴纸墙。
- {{RED_SEALS}} 是 1-2 个朱红色手绘印章/印记，作为内容节奏点；除非用户提供官方资产，不得把它画成官方品牌 logo 或公章。
- 背景是极简浅色平面、纸张肌理或柔和留白，不使用户外道路、树影、天空和手持摄影背景。

9:16 手机安全区与构图：
- 顶部 0%-10% 与底部 84%-100% 保持低信息密度，不能放主标题、金句、品牌锚点或关键动作。
- 平面内容画布占画面中央约 78%-88%，四周保留留白，不做扇形裁切或实体边缘。
- 主标题位于中央约 26%-58% 区域，最多两行，建议 4-8 个汉字；标题必须像版面原生手写内容，而不是后贴的海报字。
- {{CALLOUT_BUBBLES}} 分布在主标题左右或上下，2-4 个即可；气泡框不能遮住主标题，文字必须短。
- {{CARTOON_ICONS}} 分布在气泡与泼墨边缘，2-4 个即可；每个图标都服务一个文稿信息点。
- {{RED_SEALS}} 放在中下部或版面角落，1-2 个即可；{{BOTTOM_QUOTE}} 放在 76%-84% 内容区，字号明显小于主标题。
- 画面只保留一个版面级核心判断，不加入真实人物、第二套版面、商品道具或横向信息卡排队。

品牌锚点规则：
- 如果 {{BRAND_ANCHOR_MODE}} = 小黑象：加入一只非常小的平面黑色小象标记，固定为哑光黑实心剪影、短象鼻、小圆耳、白点眼、四足短圆桩腿、低矮轻巧身体。它可以用短象鼻指向主标题重点词、牵住气泡尾巴或压住一条下划线；必须与版面内容有清晰关系，不能漂浮在角落装饰。
- 如果 {{BRAND_ANCHOR_MODE}} = 官方大象 logo：只使用用户/项目提供的官方大象 logo 作为平面版面中的小印章、角标或标题旁识别标记，必须贴合画面内容、尺寸克制、颜色准确；不得凭空编造 logo、品牌名或宣传口号，也不能做成品牌广告 KV。
- 两种模式不能同时出现；若变量为空，默认使用“小黑象”。没有品牌锚点的成图直接判失败。

小黑象 2.0 锁定（仅在品牌模式选择小黑象时生效）：
A tiny nimble solid BLACK baby elephant silhouette, matte black cutout body, tiny white dot eyes, short stubby trunk like a small curled hose, small round ears, compact low body.
FOUR SHORT ROUNDED ELEPHANT PEG LEGS under the body, quadruped stance. Front and rear legs may be partially hidden, but it must still read as a four-legged baby elephant.
The trunk performs the main action. Do not add human arms or hands.
No biped pose, no human legs, no stick legs, no knees, no feet, no shoes.
Not a humanoid Xiaohei, not a black human silhouette, not a stick figure, not a robot, not a bear, not a pig.
Not a glossy 3D toy, not plush mascot, not realistic elephant figurine, not a cute children's character, not a heavy round statue.
Scale lock: in this 9:16 cover, the elephant height is only 4%-6% of the canvas height and never exceeds one third of the main content canvas height.

文字与字体：
- 主标题必须逐字显示“{{TITLE_TEXT}}”，直接融入平面扇面内容画布；使用粗重、略不规则、友好但有笔锋的中文手写/毛笔字，参考 ZCOOL KuaiLe 的圆润手写气质，不使用标准科技黑体、UI 字体或白字发光。
- 标题主字使用炭黑/深墨色；“{{TITLE_EMPHASIS}}”使用 {{ACCENT_COLOR}} 的刷色强调；周边批注使用深灰或同一主强调色的低饱和变化。
- 底部金句必须逐字显示“{{BOTTOM_QUOTE}}”，只保留一句，短于主标题，融入平面内容画布下部的手写质感。
- 气泡框内只放 {{SIDE_NOTES}} 中实际选用的 2-4 条短批注；卡通图标和红色印章不生成长句。印章如需文字，只使用 {{RED_SEALS}} 中已确认的短词。
- Allowed text only：{{TITLE_TEXT}}；{{BOTTOM_QUOTE}}；气泡中的 2-4 条 {{SIDE_NOTES}}；{{RED_SEALS}} 中已确认的短词；必要时只保留 1 个短品牌字样。不要生成额外伪文字、英文乱字、乱码、水印、平台按钮、播放图标、头像、点赞评论图标、时间戳或可读 HUD 小字。

ONE-PASS INTEGRATED COMPOSITION LOCK:
- 在同一次 image_gen 中同时生成平面内容画布、主标题、泼墨、气泡批注、卡通简笔图标、红色印章、底部金句和品牌锚点。
- 文字、气泡、图标和印章必须共享纸面纹理、墨迹边缘、手绘线条和版式关系；禁止先生成无字底图，再本地叠字、贴标题卡或生成独立 logo/文字层。
- 可以把本次标题和金句的 ZCOOL KuaiLe 排版参考图作为 `TYPOGRAPHY_REFERENCE_ONLY` 输入，但它不是文字层、mask 或合成素材。
- 每个候选只允许一次 image_gen；文字不稳定时缩短文案、减少批注并重新生成完整候选，不得后期修字。

避免：
21:9 横版裁切、实体折扇、扇片、扇骨、扇柄、手持摄影、折痕、普通扇子图标、第二套版面、人物群像、户外道路树影背景、暗黑科技背景、HUD 大屏、PPT 信息图、卡片网格、商品棚拍、扇面文字过多、气泡框堆叠、随机贴纸、红色公章、复制参考图原有题字/印章、平台 UI、字幕条、品牌 logo 漂浮或错误、虚构品牌、品牌锚点缺失、小黑人、人形小黑、二足站姿、人形腿、火柴腿、脚掌鞋子、萌宠象、厚重圆胖小象、主标题不在平面内容画布上、金句落入底部 UI 区。
```

### 扇面内容模板的变量填充顺序

1. 先读已确认文稿，提炼 `{{SCRIPT_CORE}}`，再写 `{{TITLE_TEXT}}` 和 `{{BOTTOM_QUOTE}}`；不得从参考图抄题字。
2. 把抽象内容压缩成一个平面版式关系：例如“问题气泡围住错误判断”“图标沿箭头指向可执行动作”“红色印章标记已确认边界”。不把所有名词都画成图标。
3. `{{SIDE_NOTES}}` 只保留 2-4 条，全部放入 `{{CALLOUT_BUBBLES}}`；优先从文稿中选“处境、机制、结果/边界”各一条；没有依据的数字、品牌名和案例写 `未获取`，不补造。
4. `{{CARTOON_ICONS}}` 只选 2-4 个与文稿有直接关系的卡通简笔图标；`{{RED_SEALS}}` 只选 1-2 个朱红印章/印记，不生成虚构公章。
5. `{{BRAND_ANCHOR_MODE}}` 默认填“小黑象”。只有用户明确选择官方 logo，或项目已经提供官方 logo 参考资产时，才填“官方大象 logo”。
6. 生成前必须把完整变量值写入项目的 `prompts/video-cover-fan-prompt.md`；生成后按 `references/qa-checklist.md` 的 `9:16 Video Cover Branch` 和 `Fan Surface Variant` 两组检查。

## 彩蛋长卷

```text
生成一张超横版小黑象真实物品长卷故事图，比例约 2.8:1。

主题：{主题}
节点：{5-8 个节点}

画面：
高级近白摄影棚背景，一条细黑色手绘曲线路径从左到右贯穿全图。
沿路径放置 5-8 个真实物品节点，每个节点都有小黑象参与一个物理动作。
节点不编号，不做时间轴模块，不做 PPT 流程图。
左侧是起点，右侧是当前结论或下一阶段。
如果某个节点明确对应真实产品、平台或 App，可以在该节点的卡片、文件夹、设备屏幕或 app tile 上使用对应官方品牌 logo / app icon；不要虚构品牌，不要让 logo 变成节点主角。

小黑象硬性要求：
每个小黑象都必须是黑色小象：
ELEPHANT (FIXED IP CHARACTER — MUST BE CONSISTENT ACROSS ALL IMAGES):
A tiny solid BLACK baby elephant with these EXACT features:
- SIZE LOCK: each elephant is a tiny worker, not a mascot; each elephant should be much smaller than the nearby real object and should not become the main visual mass
- Short stubby trunk, about as wide as its head, like a tiny curled hose, does NOT reach the ground
- Two small round ears, like buttons on each side of a round head
- Four short rounded elephant peg legs under the body, quadruped stance, not human legs or stick legs
- Two tiny white dots for eyes, no pupils, no detailed eye shapes
- Rounded bean-shaped body, NOT realistic elephant proportions
- CONSISTENT across all images: same shape, same proportions, same style every time
非人形。

文字：
每个节点 1-3 个中文短标签，贴近物品，像手写注释。

避免：
旧版小黑、人形角色、编号圆点、流程图模块、密集文字、人物履历虚构、物品堆叠、深色背景。
```
