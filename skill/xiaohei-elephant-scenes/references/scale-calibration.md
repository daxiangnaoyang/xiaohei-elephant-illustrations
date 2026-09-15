# 小黑象 2.0 尺度校准（标准图）

## 根因

图像模型优先满足“角色和动作可读”，而不是藏在长提示词里的百分比。因此只写 `3%-5%`，常被放大成约 8%—15%。

## 固定执行规则

标准 16:9 图必须把以下块放在最终英文 Prompt 的前 8 行，不能埋入 IP 形体段：

```text
SCALE IS THE FIRST PRIORITY.
Use an extreme wide, pulled-back camera.
The elephant is a tiny distant worker: target only 1.5%-2.5% of full canvas height.
The main real object is at least 6x taller than the elephant.
The real-object tableau follows the selected density mode: D1 = 42%-56% canvas width and 24%-34% height; D2 = 50%-64% width and 28%-40% height; D3 = 56%-70% width and 32%-48% height.
Keep the camera pulled back and preserve generous near-white space: 65%+ for D1, 55%+ for D2, and 48%+ for D3.
If the elephant would be larger to make its action readable, make the OBJECT larger instead; never enlarge the elephant.
```

这里的 1.5%—2.5% 是模型生成补偿目标；最终实际验收仍为约 3%—5%，且主物品至少为小黑象高度的 3 倍。D1 / D2 / D3 只调整真实物品小现场的大小和节点预算，不允许放大小黑象或把镜头拉近；信息越多，扩展真实物件之间的层次与关系。

## 三档重试

- **A 档**：上述补偿块。
- **B 档（实际超过 5%）**：角色目标降为 1%—1.5%，主物品至少为角色 10 倍高，使用 `extreme wide far-away shot`；不增加物品或文字。
- **C 档（B 仍超标）**：改为遮挡式动作，只露出小黑象头、短象鼻与四足轮廓，主物品承担画面体量。不能后期裁切或缩放伪造通过。

`qa.md` 必须记录实际目视尺度与 A/B/C 档位。只有实际高度约 3%—5%、象鼻动作和四足仍可读，才可命名 `final.png`。

## 同文章多图的二级尺度锁

3%—5% 只是单张图的绝对门禁，不能保证同文章多图一致。一旦同一文章需要 2 张及以上图片，还必须执行 [`article-batch-character-lock.md`](article-batch-character-lock.md)：

- 第 1 张过 QA 后冻结为角色母版。
- 同一画幅模式后续图的高度相对母版只允许 ±10%。
- 后续图始终直接引用母版，不串联引用上一张。
- 跨 16:9、21:9、9:16 只锁 IP 形体，尺度分模式建立基准。
