# WeChat Article Integration

Use this skill after the article draft is final and approved.

## Trigger

Start illustration work only when one of these is true:

- The final draft has been explicitly approved.
- The project has a stable final draft file.
- The user says to continue with illustration and formatting.

Do not generate article illustrations while the draft is still being rewritten.

## Output Contract

Create an illustration plan before generating images:

```markdown
# 06-illustration-plan

## Visual Strategy

- Where images should appear:
- Where images should not appear:
- Reading rhythm:

## Shot List

| No. | Insert Position | Theme | Core Idea | Composition | Xiaohei Elephant Action | Labels | Risk |
|---|---|---|---|---|---|---|---|

## Generation Log

| File | Position | QA Result | Notes |
|---|---|---|---|
```

## QA

Reject the image if:

- It looks like a course slide, PPT infographic, or formal flowchart.
- Xiaohei Elephant is only decorative.
- It includes unverified people, brands, data, or concrete experiences.
- It has too much text or unreadable Chinese labels.
- It does not explain one clear cognitive action.

## Recommended Count

- Short article: 1-3 images.
- Standard article: 4-6 images.
- Long tutorial or retrospective: up to 8 images.
