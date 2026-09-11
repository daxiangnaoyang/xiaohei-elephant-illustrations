# Xiaohongshu Carousel Prompt Template

Use this template for a four-page or multi-page Xiaohongshu knowledge carousel. Generate each page as a separate 3:4 image so text, safe areas, and page hierarchy remain inspectable. Reuse the same identity/style anchors across pages when a person appears.

## Fill first

- `Core question`: the one problem the post answers;
- `Page map`: one role per page, such as `cover / mechanism / pitfalls / action`;
- `Identity image`: optional `<identity-reference-image>`;
- `Style`: one entry from `style-library.md`;
- `Shared palette`: two main colors and one accent;
- `Page text`: an exact whitelist for each page, with no invented numbers;
- `Shared avoid list`: extra copy, fake data, logos, QR codes, and watermarks.

## Page brief

Create one brief per page before generating:

```text
Page <page number> of <total pages>
Role: <cover / explanation / comparison / pitfall / action>
Exact visible text:
- "<line 1>"
- "<line 2>"
First visual center: <one center>
Supporting center: <one object or abstract workflow>
```

## Ready-to-copy prompt

```text
Create one finished Xiaohongshu carousel card, page <page number> of <total pages>, true 3:4 vertical composition. This is one page only, not a contact sheet and not a collage of multiple pages.

Consistency anchor: use the same <style-library style>, <shared palette>, lighting, line weight, and texture as the other pages. If a person is present, Image 1 is <identity-reference-image>; preserve the same identity, age range, face shape, hair, glasses, facial hair, skin tone, and natural proportions across every page. Use at most one pose reference, <pose-reference-image>, and keep one simple approved gesture.

Post question: <core question>.
Page role: <page role>.
First visual center: <one center>. Supporting center: <one object or abstract workflow>.
Composition: independent 3:4 vertical layout with a clear upper/middle reading path; keep all important text and the person inside safe areas; keep the bottom feed-overlay zone quiet.

Visible text whitelist for this page: render only these exact strings and nothing else:
- "<line 1>"
- "<line 2>"
- "<line 3, if any>"

Generate this page's person, text, objects, background, and decorations together in one image-generation pass. Use the same visual grammar as the carousel while allowing this page's role to control the composition.
Do not add text, numbers, metrics, money, rankings, testimonials, logos, QR codes, watermarks, invented UI labels, or facts not present in the whitelist. Do not change the person's identity, blend poses, crop hands, or turn this page into a poster full of tiny unreadable copy.

Output: one readable 3:4 carousel card for page <page number>.
```

Run the QA checklist on every page and then review the pages as a sequence: the title must hook, the middle pages must explain one causal chain, and the last page must give one usable action without inventing a result or promise.
