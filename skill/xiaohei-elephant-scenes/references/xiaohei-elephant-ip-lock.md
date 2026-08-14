# 小黑象 2.0 IP 锁定

## 角色定义

小黑象是这套 2.0 真实物品场景图里的固定 IP，但不是 Logo、吉祥物、玩具摆件或写实动物。它是一个在真实物件小现场里认真干活的黑色小象执行者。

它可以因为场景不同而有轻微形体变化：更矮一点、更前倾一点、更拉伸一点、被物件遮挡一点。变化要服务动作，不能牺牲小象识别。

一句话：

```text
小黑象 2.0 = 在真实物件现场里认真执行一个物理动作的黑色小象。
```

## 必须保留的识别点

- 黑色实心小象身体。
- 白色小圆点眼睛，不能变成大眼睛、瞳孔、表情包眼睛。
- 短象鼻，像小卷管，长度约等于头宽，不垂到地面。
- 小圆耳，贴在头部两侧，不能变成大扇形写实象耳。
- 四足短圆桩腿，贴在身体下方。
- 身体短、低、圆润但不笨重，像哑光黑色小剪影。
- 表情空、冷静、认真。
- 不穿衣服、不戴帽子、不拿人类手臂道具。

## 四足锁定

小黑象 2.0 的最大漂移风险，是变成“原版小黑角色 + 象鼻”。腿部必须单独锁定。

合格腿部：

- 4 条短圆桩腿。
- 腿从身体下方长出，不从身体两侧像人腿一样伸出。
- 前后腿可以被身体、视角或物件遮挡，但画面仍要读成四足小象。
- 腿可以很短，但不能消失到只剩一个黑球。
- 脚底只是一小段圆钝接触面，不画脚掌、鞋子、脚趾。

失败腿部：

- 只有 2 条腿。
- 细长火柴腿。
- 人类小黑腿。
- 有膝盖、脚掌、鞋子、走路姿势像人。
- 长条身体下面接两根腿。
- 站成二足姿态，靠象鼻或手臂做动作。

Prompt 必须写：

```text
FOUR SHORT ROUNDED ELEPHANT PEG LEGS under the body, quadruped stance.
Front and rear legs may be partially hidden, but it must still read as a four-legged baby elephant.
No biped pose, no human legs, no stick legs, no knees, no feet, no shoes.
```

## 2.0 形体弹性

默认形态：

- 低矮小象剪影，而不是站立小人。
- 标准 16:9 图高度通常保持在画面高度的 3%-5%；cover 版高度保持在 4%-6%。这是硬上限，不是建议值。
- 黑色视觉体量约为此前小黑象测试图的 1/3；小黑象必须比真实主物品小很多，不超过主物品高度的 1/3。
- 身体接近短豆形 / 小胶囊 / 低矮圆块。
- 短象鼻是主要动作器官。
- 四足支撑身体，动作可以前倾、伸脖、转身，但不能二足化。

允许变化：

- 伸象鼻时，头颈可以轻微前探。
- 推物件时，身体可以微微前倾。
- 被物件遮挡时，只露出头、象鼻和部分身体，但仍要看到小象结构。
- cover 暗色背景里可以加极轻边缘光，但不能变成高光 3D 玩具。
- 真实物品场景里可以有轻接触阴影，但角色本体应保持哑光黑。

禁止变化：

- 不要变成可爱宠物象、儿童绘本象、马戏团象、写实动物模型。
- 不要变成玩具公仔、毛绒玩具、3D 商品模型。
- 不要过度拟人化，不要人类手臂、人类手掌、人腿。
- 不要为了“灵巧”把腿画成火柴腿。
- 不要为了“真实”画出复杂皮肤、皱褶、象牙、写实眼睛。
- 不要每张都完全同一个姿势，否则会像贴纸。

## 文章批次不变量

“姿势可变”不等于“角色可重新设计”。同一篇文章的多张图必须共用一张已验收角色母版，并保持：

- 同一头身宽高关系与轻巧的黑色体量。
- 同一耳朵大小、象鼻长度和腿部粗细。
- 同一哑光黑剪影材质和白点眼尺寸。
- 同一画幅模式的角色高度相对母版偏差不超过 ±10%。

允许为动作改变象鼻弯曲、身体前倾、朝向和遮挡关系；不允许因新场景改变身体胖瘦、头身比、耳鼻尺寸或四足结构。详见 [`article-batch-character-lock.md`](article-batch-character-lock.md)。

## 小黑象必须承担核心动作

小黑象不能只是站在旁边看，也不能只负责“可爱”。

合格动作：

- 用短象鼻卷起一张卡片。
- 用短象鼻转动阀门、拉动小绳、拨动开关。
- 用身体轻轻顶住闸门、盒子、压板。
- 四足站稳，短象鼻把纸条放进漏斗、筛子、收纳盒。
- 用短象鼻盖章、检查、分拣、推送。
- 在真实物品旁边承担一个明确物理动作。

不合格动作：

- 站在角落里看物件。
- 举牌解释主题。
- 二足站立，用人类手臂做动作。
- 对着物件摆拍，没有物理接触。
- 去掉小黑象后，画面隐喻仍然完整。

判断标准：

```text
如果删掉小黑象，隐喻还完全成立，说明小黑象失败。
如果删掉象鼻和耳朵，角色立刻像旧小黑，说明形体失败。
如果只看腿部像两条人腿，说明 2.0 IP 失败。
```

## 性格

- 认真，不装可爱。
- 轻巧，但不是灵动萌宠。
- 有一点笨拙，但不笨重。
- 像低调的系统操作员。
- 在荒诞真实物件现场里冷静完成任务。
- 可爱来自“认真做荒诞事”，不是表情、服装或夸张姿势。

## 标准 Prompt 锁定块

每次生成小黑象 2.0，都应复制或等价包含以下英文锁定块：

```text
Xiaohei Elephant 2.0 IP lock:
A tiny nimble solid BLACK baby elephant silhouette, matte black cutout body, tiny white dot eyes, short stubby trunk like a small curled hose, small round ears, compact low body.
Scale lock: in standard 16:9 images, elephant height is only 3%-5% of canvas height; in cover images, only 4%-6%. Its black visual mass should feel about one third of previous oversized elephant tests and never exceed one third of the main real object's height.
FOUR SHORT ROUNDED ELEPHANT PEG LEGS under the body, quadruped stance.
Front and rear legs may be partially hidden by the body or perspective, but it must still read as a four-legged baby elephant.
The trunk performs the main action. Do not add human arms or hands.
No biped pose, no human legs, no stick legs, no knees, no feet, no shoes.
Not a humanoid Xiaohei, not a black human silhouette, not a stick figure, not a robot, not a bear, not a pig.
Not a glossy 3D toy, not plush mascot, not realistic elephant figurine, not cute children's character, not heavy round statue.
```

## QA 一票否决

- 没有短象鼻。
- 没有小耳朵。
- 没有白点眼。
- 只剩两条腿，或腿像人腿/火柴腿。
- 二足站姿。
- 有膝盖、脚掌、鞋子。
- 变成旧小黑、小黑人、黑色人形、火柴人。
- 变成玩具象、写实象、萌宠象、儿童插画象。
- 小黑象没有承担核心动作。
- 同文章同模式多图的高度相对母版漂移超过 ±10%，或头身、耳鼻、四足比例明显改变。
