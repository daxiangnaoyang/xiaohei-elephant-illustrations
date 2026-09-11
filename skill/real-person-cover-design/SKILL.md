---
name: real-person-cover-design
description: Use when creating or editing a real-person article, newsletter, video, or Xiaohongshu cover from user-supplied identity references; route 3:4 and 21:9 layouts, preserve one person and one pose, generate readable text in one pass, and keep private assets out of the deliverable.
version: 1.0.0
author: Community contribution
license: MIT
metadata:
  hermes:
    tags: [real-person, cover-design, imagegen, xiaohongshu, visual-system]
    related_skills: [xiaohei-elephant-illustrations]
triggers:
  - real-person cover
  - portrait cover
  - article cover image
  - Xiaohongshu cover
  - 真人封面
  - 人物封面
  - 小红书封面配图
---

# Real-Person Cover Design

## Overview

Turn a user-provided portrait and an article or topic into a reusable cover system. The system separates four decisions that are often mixed together: channel ratio, identity and pose, visual language, and the single message the reader should notice first.

This skill is a method and prompt pack. It does not include anyone's portrait, face embedding, private brand files, local filesystem paths, or account credentials. A user may supply a reference image during a task; do not copy that image into the skill package.

## When to Use

Use this skill when the user wants a real person to remain recognizable on an article, newsletter, video, or Xiaohongshu cover, or wants a consistent family of covers from one or more portraits.

Do not use it for:

- an illustrated mascot or character-only scene;
- a product-only banner with no person;
- a deterministic SVG/HTML layout when editable vector output is the requirement;
- a public package that contains the user's portrait, private paths, credentials, or account configuration.

## Inputs and privacy boundary

Collect the smallest useful brief:

1. `Title` — exact visible wording, or a clearly marked test title.
2. `Channel` — `xiaohongshu` (3:4), `wechat/article` (21:9), `video-cover` (9:16), or another explicitly requested ratio.
3. `Visual focus` — title, person, product, workflow, viewpoint, or verified result.
4. `Identity reference` — optional user-supplied portrait used only for the current generation.
5. `Pose reference` — optional; use at most one pose reference per image.
6. `Style` — choose from [references/style-library.md](references/style-library.md), or recommend one with a reason.

Privacy rules:

- Never put a user's name, local absolute path, private account, face file, QR code, API key, or internal prompt in a public skill package.
- In examples use placeholders such as `<identity-reference-image>` and `<pose-reference-image>`.
- Do not infer a person's employer, income, clients, audience size, credentials, or life story from a portrait.
- If the user supplies a portrait, keep it in the task's working area and report that it was not packaged.

## Channel routing

| Channel | Default canvas | Composition rule |
|---|---:|---|
| Xiaohongshu note cover | 3:4 | Put the hook in the upper and middle safe area; keep important text away from the bottom overlay zone. |
| WeChat/article or X long cover | 21:9 | Give the title and person separate breathing room; do not crop a 16:9 image into this ratio. |
| Short-video cover | 9:16 | Recompose vertically from the brief; do not stretch or crop a horizontal cover. |

If the channel is missing, ask only for the channel when the ratio changes the result. Otherwise default to 3:4 for a social cover and state the assumption.

## Core workflow

### 1. Lock the message

Write one sentence: `The reader sees <first focus> first and understands <three-second takeaway> next.` Keep a verbatim text whitelist containing only the title, optional brand line supplied by the user, and optional short subtitle.

Completion criterion: every visible word has a source in the brief; all unverified numbers, claims, logos, and testimonials are removed.

### 2. Lock identity and pose

Use the identity reference for face shape, age range, glasses, hair, facial hair, skin tone, and natural proportions. Use one pose reference for gesture, clothing, camera angle, and hand position. Do not blend multiple poses into one generation.

Completion criterion: the prompt names each input image by role and states which identity and pose details are invariant.

### 3. Choose a visual language

Read [references/style-library.md](references/style-library.md) only as far as needed. Choose one style, one first visual center, one supporting center, and a short allow/avoid list. A style controls palette, texture, and visual grammar; it does not force the person to one side or copy a reference layout.

Completion criterion: `style + first center + supporting center + allowed elements + forbidden elements` are explicit.

### 4. Generate in one pass

Use the built-in `image_gen` tool when available. For a transparent cutout, request a genuine transparent background and preserve the alpha channel. For a finished cover, ask for the person, title, objects, background, and decoration to be formed in one image-generation pass; do not create a blank background and add the title later.

Use [references/prompt-template.md](references/prompt-template.md) to structure the request. State the exact text whitelist, ratio, identity invariants, safe area, and negative constraints twice when text or identity is critical.

If the environment cannot generate images, return the completed prompt and a clear input list instead of claiming that an image was generated.

Completion criterion: the result is a complete cover or a clearly labeled prompt-only deliverable, never an unreported placeholder.

### 5. Run visual QA

Read [references/qa-checklist.md](references/qa-checklist.md). Inspect the image at full size and at the channel's feed-size preview. Check identity, hands, exact text, safe area, ratio, and factual boundaries. If one item fails, make one targeted correction and re-check the whole checklist.

Completion criterion: every check is `PASS` or has a documented `BLOCKED` reason; no silent defects are carried forward.

### 6. Save and report

Use a project-owned output directory and a stable filename such as `cover-<channel>-<style>-v1.png`. Keep the original portrait and any private references outside the public package. Report the final path, ratio, generation mode, prompt or prompt set, and any remaining limitation.

Completion criterion: the selected image is readable from the reported path and the package contains no private input assets.

## Recommended style set

These nine styles are deliberately generic and may be recomposed for either 3:4 or 21:9. Read the full descriptions only when selecting a style:

1. Warm paper action scene
2. Clean product explanation
3. Deep-blue signal
4. Paper story wall
5. Editorial whitespace
6. Black-and-gold conclusion
7. Fluorescent test bench
8. Handwritten action desk
9. Dark workflow system

## Text and evidence guardrails

- Copy visible text verbatim from the brief; require no extra words, letters, numbers, QR codes, watermarks, or pseudo-logos.
- Keep words short on image. If exact Chinese text is important, spell out the string and ask for a second visual check.
- Use only user-provided and verifiable results. Without evidence, use abstract shapes or an unlabeled workflow instead of metrics, money, rankings, reviews, or dashboards.
- A reference cover may teach palette, density, or visual grammar. Do not reproduce its title, distinctive arrangement, character, or asset.

## Common Pitfalls

1. **Identity drift** — the face becomes younger, thinner, or a different person. Reassert the identity reference and remove beautification language.
2. **Pose blending** — extra fingers or mixed gestures appear. Use exactly one pose reference per image.
3. **Text leakage** — UI cards invent labels or numbers. Replace them with blank geometric cards and repeat the whitelist.
4. **Platform crop failure** — important text sits in the bottom overlay zone or a horizontal cover is merely cropped. Recompose for the target ratio.
5. **Evidence inflation** — decorative charts look like real business results. Remove data-like marks unless the user supplied the evidence.
6. **Public-package leakage** — a sample contains a private portrait or an absolute local path. Replace it with placeholders and scan the package before publishing.
7. **Reference imitation** — a third-party sample is copied too literally. Keep only the abstract visual decision and redraw the composition.

## Verification Checklist

- [ ] Channel and ratio are explicit.
- [ ] Title and other visible words are in a closed whitelist.
- [ ] Identity and pose inputs are labeled by role; at most one pose is used.
- [ ] The first visual center and three-second takeaway are explicit.
- [ ] The cover is generated in one pass or the output is clearly prompt-only.
- [ ] Full-size and feed-size QA pass for identity, hands, text, safe area, and factual boundaries.
- [ ] The public package contains no portraits, absolute paths, credentials, QR codes, or account settings.
- [ ] Final path and prompt/prompt set are reported.
