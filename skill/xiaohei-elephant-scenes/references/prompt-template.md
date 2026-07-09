# 小黑象 2.0 Prompt Template

## 标准 16:9 正文图

```text
生成一张 16:9 横版中文正文配图。

主题：{主题}
读者处境：{读者处境}
核心冲突句：{核心冲突句}

画面：
纯白或接近纯白摄影棚背景，大量留白。
一个真实物品小现场，主物品是：{真实主物品}。
核心物理动作是：{核心物理动作}。
小黑象正在：{小黑象动作}。

原版小黑 2.0 质感锁定：
- Treat the original Xiaohei Scenes 2.0 examples as the quality bar for restraint, whitespace, object realism, sparse labels, and clear physical action.
- Pull the camera back. Scene footprint should be small-to-medium and airy: about 46%-58% of canvas width and 26%-38% of canvas height.
- One real main object or one compact main object group only; at most 1 small prop for first-pass previews, 2 maximum only when necessary.
- Keep the whole image airy with generous empty white space around the scene. Do not make a close-up, low-angle hero shot, product hero shot, toy photography poster, or dense object pile.
- Use only very light contact shadows under objects and the elephant. No grey background, no vignette, no gradient, no heavy studio shadow.
- The image must still read as one strange but precise physical moment, not a concept poster.

小黑象硬性要求：
Use the full `Xiaohei Elephant 2.0 IP lock` from `references/xiaohei-elephant-ip-lock.md`. The following is the minimum lock:
ELEPHANT (FIXED IP CHARACTER — MUST BE CONSISTENT ACROSS ALL IMAGES):
A small solid BLACK baby elephant with these EXACT features:
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
2-4 个中文手写短标签：{中文短标签}
标签要短、清楚、像手写批注，不要长句，不要标题。
Labels should sit close to the object or action like annotations, underlines, arrows, or tiny notes. Do not put oversized title-like slogans on both sides of the image.

风格：
真实物品有自然光影和轻微摄影质感；小黑象可以是简化黑色角色，但必须和真实物品发生物理互动。
画面轻、怪、清爽，有留白。
少量蓝 / 黄 / 红 / 橙点缀。彩色只做节奏点，4-6 个小点缀即可；不要大面积彩色便签堆、彩色抽屉标签或彩色纸片铺满画面。

避免：
PPT 信息图、复杂流程图、UI 截图、仪表盘、科技 HUD、商业海报、深色背景、物品堆满、商品摄影感、玩具棚拍感、近距离特写、低机位英雄镜头、笨重圆胖小象、二足站姿、人形腿、火柴腿、鞋子脚掌、中文错字、大段文字、小黑象站在旁边不动。
```

## Cover 版 21:9 单图

```text
生成一张 21:9 超横版公众号封面图。Cover 版是单独的一张，不是正文 16:9 配图。

主题：{主题}
标题：{标题，可为空}
核心隐喻：{一个真实物品 + 小黑象动作}

画面：
深色科技背景，青橙对比，轻微纸张纹理，弱 HUD 网格，玻璃拟态卡片，发光连接线，手绘科技信息图质感。
参考科技感公众号信息图要求，但这是一张 cover：标题区、主视觉区、底部短句区分开，画面要有点击吸引力，不做密集正文信息图。

小黑象 2.0 主体：
Use the full `Xiaohei Elephant 2.0 IP lock` from `references/xiaohei-elephant-ip-lock.md`. Minimum lock:
A small nimble solid BLACK elephant silhouette, SHORT TRUNK, SMALL ROUND EARS, FOUR SHORT ROUNDED ELEPHANT PEG LEGS under the body, WHITE DOT EYES, compact agile body.
Quadruped elephant stance only. No biped standing pose, no human legs, no stick legs, no knees, no feet, no shoes.
Matte black simplified silhouette, not glossy 3D toy, not plush mascot, not realistic elephant figurine, not heavy round statue.

真实物品：
一个核心真实物品或紧凑物品组：{真实主物品}。
小黑象用短象鼻参与核心动作：{小黑象动作}。

文字策略：
如果标题为空，不要生成可读中文标题，只留出标题区和底部短句区，后续本地排版。
如果标题不为空，只生成这一句短标题：{标题}。不要额外生成伪文字、英文、乱码、水印。

构图：
21:9 horizontal, cinematic wide cover. Main visual sits slightly right of center or center, title-safe blank area on left/top, bottom quote-safe area. Clean visual hierarchy, not a dense information wall.

避免：
正文信息图式密集节点、PPT 流程图、真实品牌 logo、伪文字 HUD、复杂仪表盘、营销海报大字压满、写实人物、机器人角色、小黑人、旧小黑、人形腿、二足站姿、笨重玩具小象。
```

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

小黑象硬性要求：
每个小黑象都必须是黑色小象：
ELEPHANT (FIXED IP CHARACTER — MUST BE CONSISTENT ACROSS ALL IMAGES):
A small solid BLACK baby elephant with these EXACT features:
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
