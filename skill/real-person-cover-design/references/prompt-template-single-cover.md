# Xiaohongshu Single-Cover Prompt Template

Use this template when the post needs one finished 3:4 cover with a recognizable person. Fill every angle-bracket field before calling the image tool. Keep the visible text whitelist short.

## Fill first

- `Title`: exact title, copied verbatim;
- `Subtitle`: optional, one short line only;
- `Identity image`: `<identity-reference-image>`;
- `Pose image`: `<pose-reference-image>` or `none`;
- `Style`: one entry from `style-library.md`;
- `First center`: title, person, or one object;
- `Supporting center`: one secondary object or abstract workflow;
- `Palette`: two main colors and one accent;
- `Safe area`: keep the title and face away from the bottom feed overlay.

## Ready-to-copy prompt

```text
Create one finished Xiaohongshu post cover, true 3:4 vertical composition, not a cropped horizontal image.

Identity input: Image 1 is <identity-reference-image>. Preserve the same person, age range, face shape, hair, glasses, facial hair, skin tone, and natural proportions. Do not beautify, age-shift, slim, or replace the person.
Pose input: Image 2 is <pose-reference-image>. If supplied, preserve only this one approved gesture, hand position, clothing relationship, and camera angle. Do not blend poses or add a second gesture.

Message: the reader notices <first center> first and understands <three-second takeaway> next.
Subject: <person plus one supporting object or abstract workflow>.
Visual language: <one style-library style>; palette <two main colors plus one accent>; restrained <lighting and mood>; <paper, matte, clean UI geometry, or other texture>.
Composition: independent 3:4 vertical layout; put the title in the upper or middle safe area; keep the face, hands, and important objects fully inside frame; leave the bottom feed-overlay zone quiet.
Visible text whitelist: render only these exact strings and nothing else:
- Title: "<exact title>"
- Subtitle: "<exact subtitle or omit>"

Generate the person, title, supporting object, background, and decorations together in one image-generation pass. Use readable typography and preserve the exact text strings.
Do not add extra words, letters, numbers, logos, QR codes, watermarks, fake metrics, money, rankings, testimonials, invented product UI, or cropped fingers. Keep identity, pose, hands, clothing, text, and 3:4 ratio unchanged.

Output: one complete, readable Xiaohongshu 3:4 cover.
```

After generation, run the QA checklist at full size and at feed-preview size. If one item fails, correct only that item and repeat the complete identity, pose, text, and ratio constraints.
