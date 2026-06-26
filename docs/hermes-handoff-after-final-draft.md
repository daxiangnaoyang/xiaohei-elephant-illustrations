# Hermes 接棒：公众号终稿后小黑象正文配图

> 日期：2026-06-26
> 适用对象：Hermes / Claude / Codex 处理公众号文章项目时共用
> 事实源：`workflow-wechat-article`、`wechat-article-sop`、`xiaohei-elephant-illustrations`

## 一句话指令

当一篇公众号文章已经形成 `05-终稿.md`，并且用户确认文稿后，Hermes 才进入小黑象正文配图环节：

```text
读取 05-终稿.md
-> 调用 xiaohei-elephant-illustrations
-> 生成 06-配图方案.md
-> 逐张生成正文配图
-> 图片归档到 <ARTICLE_ASSET_ROOT>/<article-or-project-name>/
-> 在排版前 Markdown 中插入图片引用
-> 再进入飞书排版
```

## 触发条件

满足以下任一表达时触发：

- 用户说：“终稿 OK，继续”
- 用户说：“文稿 OK，继续配图和排版”
- 用户说：“可以排版了”
- 项目目录中已有 `05-终稿.md`，并且任务明确要求继续完成创作闭环

不触发：

- 只有 `03-初稿.md`
- 文章还在改结构或改观点
- 用户只是让看素材包或选题
- 用户明确说“这篇不用配图”

## Hermes 必读文件

每次执行前按顺序读：

1. `<ARTICLE_PROJECT_DIR>/05-终稿.md`
2. `skill/xiaohei-elephant-illustrations/SKILL.md`
3. 需要出 shot list 时读：
   - `xiaohei-elephant-illustrations/references/article-visual-strategy.md`
   - `xiaohei-elephant-illustrations/references/composition-patterns.md`
4. 需要生图时读：
   - `xiaohei-elephant-illustrations/references/prompt-template.md`
   - `xiaohei-elephant-illustrations/references/qa-checklist.md`

## 必产物

在文章项目目录新增：

```text
06-配图方案.md
```

格式：

```markdown
# 06-配图方案

> 关联终稿：05-终稿.md
> 文稿确认：已确认 / 待确认
> 图片归档目录：<ARTICLE_ASSET_ROOT>/<article-or-project-name>/

## 配图总策略

- 本文适合配图的位置：
- 本文不适合配图的位置：
- 视觉节奏：

## Shot List

| 序号 | 插入位置 | 主题 | 核心意思 | 构图模式 | 小黑象动作 | 中文短标签 | 风险/避坑 |
|---|---|---|---|---|---|---|---|

## 生成记录

| 文件 | 对应位置 | QA 结果 | 备注 |
|---|---|---|---|
```

图片归档目录：

```text
<ARTICLE_ASSET_ROOT>/<article-or-project-name>/
```

命名建议：

```text
01-topic-name.png
02-topic-name.png
03-topic-name.png
```

## 执行规则

1. 先出 `06-配图方案.md`，再生图。
2. 每张图只表达一个认知锚点，不把整段文章画成信息图。
3. 每篇标准公众号文章默认 4-6 张正文配图；短文 1-3 张，长教程最多 8 张。
4. 图片必须归档到 `<ARTICLE_ASSET_ROOT>/<article-or-project-name>/`，不要只留在临时输出目录。
5. 在排版前 Markdown 中使用绝对路径插图：
   ```markdown
   ![配图说明](<ARTICLE_ASSET_ROOT>/<article-or-project-name>/01-topic-name.png)
   ```
6. 封面图和小黑象正文配图分开处理。封面图服务标题，正文配图服务段落结构。
7. 不要在初稿阶段生成正文图。初稿阶段最多记录“配图需求”。

## QA 一票否决

以下情况不进入排版：

- 图片像 PPT / 流程图 / 课程页
- 小黑象只是站在旁边，没有承担动作
- 图里出现未确认的人名、品牌、数据、案例
- 中文标签太多、错字严重或不可读
- 图片没有归档到 `<ARTICLE_ASSET_ROOT>`
- Markdown 图片路径不可访问

## 回写位置

执行完成后，Hermes 需要确认：

- `06-配图方案.md` 已写入文章项目目录
- 图片已写入 `<ARTICLE_ASSET_ROOT>/<article-or-project-name>/`
- 排版前 Markdown 已插入图片引用
- `07-分发确认.md` 中记录“正文配图已完成 / 未完成原因”

## 接棒指令模板

```text
Hermes 接棒：
这篇文章已经进入“终稿确认后正文配图”阶段。
请读取项目目录下的 05-终稿.md，调用 xiaohei-elephant-illustrations，先生成 06-配图方案.md。
如果需要出图，逐张生成小黑象正文配图，保存到 <ARTICLE_ASSET_ROOT>/<article-or-project-name>/。
完成后在排版前 Markdown 中插入图片引用，再进入 feishu-formatting-wechat-article。
不要在未确认终稿的情况下生成正文图。
```
