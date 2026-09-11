# Real-Person Cover Prompt Router

For a Xiaohongshu deliverable, choose one of the two dedicated templates first:

- [Single cover](prompt-template-single-cover.md)：一张真人主封面，3:4 竖版；
- [Carousel](prompt-template-carousel.md)：四页或多页图文卡片，逐页生成，3:4 竖版。

The shared template below is useful when the channel is not yet decided or when the image needs a non-Xiaohongshu ratio. It contains the common identity, pose, text, and evidence constraints.

Fill the fields before calling an image tool. Keep the wording short enough to inspect.

```text
Use case: <identity-preserve + ads-marketing, or background-extraction for a cutout>
Asset type: <Xiaohongshu 3:4 cover / article 21:9 cover / video 9:16 cover>
Primary request: <one sentence describing the cover's reader takeaway>
Input images:
- Image 1: identity reference; preserve the same person, age range, face shape, hair, glasses, facial hair, skin tone, and natural proportions.
- Image 2: one pose reference, if supplied; preserve only the approved gesture, clothing, hand position, and camera relationship.
Scene/backdrop: <style-library style and a simple environment>
Subject: <person plus one supporting object or abstract workflow>
Style/medium: <photo-real person integrated with hand-drawn/editorial/graphic language>
Composition/framing: <ratio, safe area, first center, supporting center>
Lighting/mood: <specific but restrained>
Color palette: <two main colors plus one accent>
Materials/textures: <paper, matte, clean UI geometry, or other chosen surface>
Text (verbatim): "<title>"; "<optional brand line>"; "<optional subtitle>"
Constraints: change only the requested scene; keep identity, pose, hands, clothing, title strings, and ratio unchanged.
Avoid: extra words, letters, numbers, logos, QR codes, watermarks, fake metrics, money, rankings, testimonials, invented product UI, face beautification, pose blending, and cropped fingers.
Output intent: complete one-pass cover with readable text, or genuine transparent alpha for a cutout.
```
## Targeted correction template

Use only after a visual QA failure:

```text
Use case: precise-object-edit.
Change only: <one failed item>.
Preserve exactly: the same person, pose, hands, clothing, all approved text, layout, colors, lighting, and target ratio.
Do not add any text, logo, number, watermark, or new object.
```
