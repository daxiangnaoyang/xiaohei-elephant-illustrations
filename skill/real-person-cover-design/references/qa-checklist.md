# Cover QA Checklist

Inspect the original-size image and a small feed-size preview. Record `PASS`, `FAIL`, or `BLOCKED` with one sentence of evidence.

| Check | Pass condition |
|---|---|
| Channel and ratio | The file matches the requested 3:4, 21:9, 9:16, or explicit ratio; it was independently composed. |
| Identity | The same person remains recognizable; no age, face, hair, glasses, or facial-hair drift. |
| Pose and hands | The intended gesture is present; fingers are complete; the face is not obscured. |
| Text whitelist | Every visible word matches the brief; there are no extra labels, letters, digits, logos, QR codes, or watermarks. |
| Hierarchy | One first visual center is obvious within three seconds; supporting elements do not compete. |
| Safe area | The title and face survive feed-size preview and platform overlays. |
| Evidence | Charts, numbers, money, rankings, and UI claims are either sourced or absent. |
| Edges and alpha | For cutouts, foreground edges are clean and the PNG has genuine transparency without a white halo. |
| Public boundary | No private portrait, absolute path, credential, account setting, or internal screenshot is in the package. |

If one check fails, make one narrow correction and repeat all checks. Do not silently accept a failure or keep regenerating without changing the failed constraint.
