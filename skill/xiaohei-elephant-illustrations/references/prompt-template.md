# 生图提示词模板

每张图单独生成。根据正文内容替换变量，不要把多张图拼在一起。

## 单张正文配图

```text
Generate one standalone 16:9 horizontal Chinese article illustration in Xiaohei Elephant style.

Visual DNA:
Pure white #FFFFFF background. Minimalist black hand-drawn line art. Slightly wobbly pen lines. Lots of empty white space. Sparse red/orange/blue handwritten Chinese annotations. Clean absurd product-sketch feeling. No gradients, no shadows, no paper texture, no complex background, no commercial vector style, no PPT infographic look, no cute mascot poster, no children's illustration, no realistic UI.

Recurring IP character required:
小黑象, a small solid-black absurd elephant-like character with a simple uneven black body silhouette, tiny white dot eyes, a short simple trunk, small ears, short legs, blank serious expression. 小黑象 must perform the core conceptual action with its trunk/body/tools, not decorate the scene. Make it serious, deadpan, slightly clumsy, and bizarre, not cute.

Theme:
{正文配图主题}

Structure type:
{结构类型：Workflow / 系统局部 / 前后对比 / 角色状态 / 概念隐喻 / 方法分层 / 地图路线 / 小漫画分镜}

Core idea:
{这张图要表达的核心意思}

Core physical action:
{卡住 / 分拣 / 卷起 / 拆箱 / 盖章 / 修补 / 搬运 / 压实 / 喷洗 / 守门 / 其他动作}

Composition:
{具体画面：小黑象在哪里、正在做什么、主要物件是什么、信息如何流动}

Key objects:
{主物件1} / {可选主物件2} / {小配件}

Chinese handwritten labels:
{标注词1} / {标注词2} / {标注词3} / {可选标注词4}

Color use:
Black for main line art and 小黑象. Orange for main flow/path/arrows. Red only for key warnings/problems/results. Blue only for secondary notes or feedback/system state.

Constraints:
One image explains only one core structure. Keep the main subject around 40%-60% of the canvas. Preserve at least 35% blank white space. Use at most 2-4 short handwritten Chinese labels. Do not write a title in the top-left corner. Do not write the structure type on the image. Do not make it a formal diagram, course slide, dense explainer, brand poster, cute mascot, circus elephant, realistic animal, or children's illustration. Do not copy prior examples or reuse known case compositions unless explicitly requested; invent a fresh visual metaphor for this specific article. It should be clear but not instructional, interesting but not childish, strange but clean.
```

## IP 母设图

```text
生成一张“小黑象”IP 母设图。

画面：16:9 横版，纯白背景，大量留白，黑色手绘线稿。
主体：一只黑色实心小象轮廓，白点眼，短象鼻，小耳朵，短腿，表情克制，不卖萌。
动作：小黑象站在一堆 AI 输出卡片和便签旁，正在用象鼻卷起一个小印章，给一张卡片盖“通过”。
风格：中文正文配图风格，怪诞但清爽，像文章里的小插图，不像 logo、海报或表情包。
点缀：少量红色、蓝色、橙色手写短标签：“来源”“假设”“通过”。
禁止：不要可爱宠物象，不要马戏团象，不要写实动物，不要儿童卡通，不要商业插画，不要复杂背景，不要阴影渐变，不要大段文字。
```

## 多图批量生成提示

```text
Create {数量} separate 16:9 Xiaohei Elephant article illustrations, one by one, not a collage. Before each image, define one specific structure type, one core idea, one core physical action, one key object group, and 2-4 short Chinese handwritten labels. Keep the same visual DNA across the series, but change the main object, Xiaohei Elephant action, spatial composition, and label placement for every image. Do not deliver topic-swap copies of the same composition.
```

## 图像编辑提示

### 去掉错误文字

```text
Edit the provided image. Remove only the incorrect handwritten text "{错误文字}" and its underline. Replace that area with clean pure white background matching the surrounding area. Preserve everything else exactly: 小黑象, objects, line style, labels, accents, composition, aspect ratio, and image quality. Do not add new text or objects.
```

### 增强怪诞感

```text
Regenerate this illustration with the same core meaning and simple layout, but make 小黑象 more central to the conceptual action. 小黑象 should be doing the strange physical work that explains the idea, not standing beside the diagram. Keep it clean, sparse, hand-drawn, deadpan, and not cute.
```

### 降低 PPT 感

```text
Regenerate the image with the same core idea, but remove PPT-like boxes, grids, titles, and formal arrows. Replace the diagram with one low-tech physical object scene. Keep one main object group, one 小黑象 action, 2-4 short Chinese labels, and large white space.
```

### 修正小黑象

```text
Keep the scene and objects similar, but adjust 小黑象 only: make it a recognizable small solid-black elephant-like character with tiny white dot eyes, a short simple trunk, small ears, short legs, blank serious expression, and a slightly uneven hand-drawn body silhouette. It must not become a cute mascot, circus elephant, realistic animal, emoji, or children's cartoon.
```

## 常用负面约束

```text
No UI screenshot, no phone chat interface, no code editor screenshot, no GitHub screenshot, no unrequested app logo, no unrequested company logo, no personal photo, no dense text, no huge red arrows, no PPT infographic, no formal flowchart, no business dashboard, no cute mascot, no circus elephant, no realistic animal, no children's cartoon, no 3D render, no dark cyberpunk, no off-white background, no grey background, no background gradient, no vignette, no paper texture, no frame, no pasted rectangular image, no topic-swap remake of existing examples.
```
