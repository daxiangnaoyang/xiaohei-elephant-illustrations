# Cover 字体运行时硬门禁

这份契约解决一个具体故障：封面明明要求 `ZCOOL KuaiLe`，运行时却先生成无字底图，再出现独立的 `title-overlay-zcool.png` 或其他文字层，最后交付一张字体漂移、像后贴字的图。

## 不变量

1. **字体单一来源**：排版参考图只能由
   `/Users/dx/Hermes-agent/03-Skills/00-场景分类/01-内容创作与设计/xiaohei-elephant-scenes/scripts/make_cover_typography_reference.py`
   读取全局字体
   `/Users/dx/Hermes-agent/00-Agent-Core/assets/fonts/ZCOOLKuaiLe-Regular.woff2` 生成。运行回执必须记录字体路径和 SHA-256；字体文件不存在或哈希不匹配时停止。
2. **参考图不是图层**：`cover-typography-ref.png` 只用于告诉图像模型字形气质、层级、断行和配色，必须标记 `TYPOGRAPHY_REFERENCE_ONLY`。9:16 扇面内容分支可额外传入一张登记过的扇面母版，必须标记 `STYLE_REFERENCE_ONLY`。两类参考图都不能被贴到成图，也不能被当作透明标题层、mask、底图或后期合成素材。
3. **一次成型**：每个 Cover 候选只能用一次 `image_gen` 完成背景、真实物品、小黑象、主标题、重点词、金句和必要短标签。整个 Cover 最多尝试 8 个完整候选；文字不稳时只能缩短文案、强化逐字要求后重新生成一个全新候选；不得对底图做 `image_edit`、本地叠字、贴标题卡或第二次文字生成。
4. **禁止底图/覆盖物血缘**：正式交付包不得出现或引用 `*-base.*`、`*-overlay.*`、`*text-layer*`、`*composite*`、`*merged*` 等中间产物。最终图不得以这些文件为输入。`title-overlay-zcool.png`、透明文字 PNG、白色标题卡一律判定为失败证据。
5. **字体形态硬验收**：主标题必须保留 ZCOOL KuaiLe 的圆润、轻松、略不规则手写笔画；出现标准科技黑体、几何无衬线、厚重尖角、网页/UI 字体、白字发光或字形明显变成另一款字体，即使文字逐字正确也失败。失败后重生，不能后期修字。
6. **文字白名单**：最终只允许主标题、可选副标题、底部金句和必要短标签；必须逐字匹配回执中的白名单，不得让模型自行补英文、伪文字、HUD 小字、水印或替代标题。
7. **验收不可降级**：视觉 QA 工具返回 400、429、余额不足、不可用、超时或任何解析错误时，`visual_qa` 只能写 `BLOCKED` / `未验证`，不得写 `PASS`，不得把候选图当正式封面发送。没有可追溯的目视证据和回执，同样阻断交付。

## 重试收敛与熔断

封面重试按“候选版”计数，而不是把一次候选拆成多次补字。每个候选都必须 `generation_passes: 1`，并在生成前把 `cover_attempts` 加 1。不得用线性重复 Prompt 无限横跳：每次重试必须记录失败原因和至少一个已改变的约束变量。

约束冲突按以下顺序裁决：

1. **P0：安全与不可变约束**。平台安全区、法务/用户明确要求逐字保留的强制文案、一次成型和禁止中间产物优先级最高。
2. **P1：可读性与内容**。主标题在缩略图可读、主题与具体物理链路 3 秒可懂、金句和必要标签不被遮挡。
3. **P2：装饰与审美**。标题三行还是两行、涂鸦数量、装饰位置和非关键留白只能在不破坏 P0/P1 时调整。

当“标题行数/断行”与平台安全区冲突时，先保留安全区，再在安全区内缩短普通文案、调整断行或重排字号；不得把文字塞进安全区换取三行。法务或用户明确锁定的文案不能自动改写，若在 P0 安全区内无法容纳，直接标记 `NEEDS_HUMAN`。

`cover_attempts` 达到 8 且仍未通过时，停止生成并请求人工裁决；不得生成第 9 版。回执写 `retry_state: NEEDS_HUMAN`，`status` 写 `BLOCKED` 或 `REJECTED`，不能把“还可以再试”当作交付状态。只有在 1—8 版内完成全量 QA 才能写 `retry_state: PASS`。

## 运行状态机

```text
PREPARE -> GENERATE_ONCE -> VISUAL_QA_PASS -> DELIVER
              |                  |
              |                  └─PASS
              └─FAIL, attempts < 8 -> REWRITE_CONSTRAINTS -> GENERATE_ONCE
                 FAIL, attempts = 8 -> NEEDS_HUMAN / BLOCKED
```

- `PREPARE`：补齐主标题、重点词、金句、Allowed text；生成排版参考图；计算字体哈希；初始化 `cover_attempts: 0` 和 `retry_state: INIT`。
- `GENERATE_ONCE`：只把排版参考图、必要的 IP 母版，以及扇面内容分支的一张 `STYLE_REFERENCE_ONLY` 母版作为参考输入；不能把任何 `base`、`overlay`、`composite`、上一张 Cover 或多张历史扇面参考图作为文字修复输入。
- `VISUAL_QA_PASS`：按 `qa-checklist.md` 检查字体形态、文字与场景的纹理/光影/透视一致性、文字白名单和一体成型；记录 QA 后端与证据路径。
- `REWRITE_CONSTRAINTS`：只改变导致失败的 Prompt 变量；优先处理 P0，再处理 P1，最后才处理 P2。保持同一候选一次成型，不把失败图或独立文字层作为输入。
- `DELIVER`：仅交付一个最终 Cover 文件和本回执。历史候选若要保留，必须标记 `REJECTED`，不能进入正式交付目录或再次作为输入。

## 必须留下的回执

每张 Cover 旁边创建 `cover-typography-receipt.md`（模板见 `templates/cover-typography-receipt.md`），至少填写：

```text
status: PASS | BLOCKED | REJECTED
generation_passes: 1
cover_attempts: <本 Cover 候选总次数，1-8>
constraint_priority: P0 safety/mandatory text > P1 readability/content > P2 aesthetics
retry_state: INIT | CONVERGING | NEEDS_HUMAN | PASS
font_asset: /Users/dx/Hermes-agent/00-Agent-Core/assets/fonts/ZCOOLKuaiLe-Regular.woff2
font_sha256: <make_cover_typography_reference.py 输出的 SHA-256>
typography_reference: <cover-typography-ref.png 的绝对路径>
style_reference: <扇面内容分支填唯一母版绝对路径；其他 Cover 填 N/A>
style_reference_role: STYLE_REFERENCE_ONLY | N/A
imagegen_inputs: <只列排版参考图、必要 IP 母版和扇面分支唯一风格母版；不得列 base/overlay 等文件>
final_path: <唯一最终 Cover 的绝对路径>
allowed_text: <逐字列出主标题/副标题/金句/必要短标签>
visual_qa: PASS | BLOCKED | FAIL
qa_backend: <实际执行目视检查的工具或人工复核；不可用时写 BLOCKED>
qa_evidence: <截图或检查记录路径>
```

`status: PASS` 的前提是 `generation_passes: 1`、`cover_attempts` 在 1—8 内、`retry_state: PASS`、`visual_qa: PASS`、字体哈希匹配、无禁用中间产物、回执中的文字白名单与成图一致。任何一项缺失都只能阻断，不能“先发出去再说”。
