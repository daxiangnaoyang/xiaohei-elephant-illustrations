# Public Cover Skill Gotchas

## 1. A portrait is input, not package content

The skill can accept a user portrait at runtime, but the public repository must contain neither that portrait nor a path that identifies it. Use `<identity-reference-image>` in examples and re-scan after every edit.

## 2. One pose per generated cover

An identity photo and a pose photo have different jobs. Pass one identity reference and zero or one pose reference. Three pose photos in one prompt commonly produce mixed hands, extra fingers, or an unstable wardrobe.

## 3. Transparent cutouts need real alpha

For a cutout request, ask the image tool for a transparent background. A white or checkerboard-looking background is not proof of transparency; inspect the PNG alpha channel when the file is meant for compositing.

## 4. Social safe areas are not interchangeable

3:4 social covers and 21:9 article covers need different composition. Keep the title inside the feed-safe region for the target platform and recompose instead of cropping another ratio.

## 5. Decorative UI is not evidence

Blank cards, arrows, and abstract modules are safe visual metaphors. Unlabeled percentages, revenue figures, rankings, star ratings, and dashboards can be mistaken for facts and must be removed unless the user supplies evidence.

## 6. Text is a closed set

Write a literal whitelist in every image prompt. Ask for no other text, letters, digits, logos, QR codes, or watermarks. If one label is wrong, make one targeted text correction; do not redesign the whole cover.

## 7. Reference means grammar, not cloning

When a reference cover is supplied, extract decisions such as density, palette, or visual hierarchy. Do not copy its exact title, character, distinctive layout, or asset. Keep a note of what was abstracted.

## 8. Public package scan

Before pushing a public branch, scan all files for:

- absolute local paths, private hostnames, or account handles;
- API-key patterns and credential names;
- real portraits, QR codes, or internal screenshots;
- private brand claims, unpublished metrics, or user-specific filenames.

Replace findings with neutral placeholders, then scan the staged tree again.
