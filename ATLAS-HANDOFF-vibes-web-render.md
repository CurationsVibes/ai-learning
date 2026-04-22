# ATLAS HANDOFF — Clean LACMA HTML for `/vibes/[slug]` web render

**Date:** 2026-04-22
**From:** Copilot (GitHub Chat) → Atlas (Claude Opus 4.7, Web)
**For:** Wyatt (@curationsgit)
**Repo:** `curationsdev/los-angeles`
**Branch context:** `main` after PR #165 (release: vibes/Resend pipeline hardening) merges

---

## Mission

Take the attached `email-template.html` (the new LACMA broadcast HTML with the
universal light-purple `#FBF9FF` background) and produce a **web-render-clean**
version that Wyatt will paste into:

```
/admin/vibes  →  LACMA post  →  Edit  →  Edit Content  →  paste  →  Save
```

Target slug: `https://www.curationsla.com/vibes/2026-04-21-lacma-x-coachella-vibes`

The webhook handler from PR #162/#163/#164 (now on `main`) will:
- Re-extract `plaintext` from the new HTML using `htmlToPlaintext()` (style/script-safe)
- Recompute `reading_time` and `word_count`
- Leave `feature_image`, `og_image`, `meta_*`, `tags`, `primary_tag`,
  `slug`, `resend_broadcast_id`, `published_at`, and `source` **untouched**

So Wyatt can paste freely without losing tracking IDs or admin-overridden metadata.

---

## Three deletions to perform on the HTML

### ✂️ 1. Hidden Gmail preview-text block

**Located near the top of `<body>`, ~lines 94–100.** Delete the entire `<div>...</div>`:

```html
<!--$--><!--html--><!--head-->
<div
  style="display:none;overflow:hidden;line-height:1px;opacity:0;max-height:0;max-width:0"
  data-skip-in-text="true">
  TEMPLATE
  <div>
     ‌​‍‎‏﻿ ‌���‍‎‏﻿ ‌​‍‎‏﻿ … (long zero-width-character padding)
  </div>
</div>
<!--body-->
```

**Keep** the `<!--$-->`, `<!--html-->`, `<!--head-->`, `<!--body-->` comment markers —
they're harmless; Resend leaves them as anchors. Just remove the `<div>` between them.

**Why:** Email-only. Gmail uses it for the inbox preview snippet. On the web it's
~3 KB of invisible bytes that contribute nothing.

---

### ✂️ 2. "VIEW TEMPLATE GOOD VIBES ONLINE →" link

**Located in the masthead area, just after the `CURATIONSLA` `<h2>`.**
Delete the entire `<p>` block:

```html
<p
  class="node-paragraph"
  style="margin:0;padding:0;font-size:11px;padding-top:0.5em;padding-bottom:0.5em;color:#111111;line-height:160%">
  <span style="color:#7e8a9a">TEMPLATE MONTH DAY, YEAR· </span>
  <a
    href="https://www.curationsla.com/vibes/2026-04-21-lacma-x-coachella-vibes"
    rel="noopener noreferrer nofollow"
    style="color:#8b5cf6;text-decoration-line:none;text-decoration:underline"
    target="_blank">
    <span style="color:#7e8a9a"><strong>VIEW TEMPLATE GOOD VIBES ONLINE → </strong></span>
  </a>
</p>
```

**Keep** the `CURATIONS<span>LA</span>` `<h2>` masthead above it AND the
`VIBES · events · jobs` nav `<p>` below it.

**Why:** Redundant on the web — the visitor is already viewing the post online.

---

### ✂️ 3. Resend unsubscribe footer

**Located at the very bottom of `<body>`, just before `</body></html>`.**

Look for a `<table>` or `<div>` containing any of these signals:

- The literal text `unsubscribe` / `Unsubscribe`
- `manage your preferences` / `manage preferences`
- Resend merge tags: `{{RESEND_UNSUBSCRIBE_URL}}`, `{{{RESEND_UNSUBSCRIBE_URL}}}`,
  `{{ unsubscribe_url }}`, or similar
- `href="https://send.curationsla.com/unsubscribe/...` or `https://...resend.../unsubscribe/...`
- Sentence patterns like "You're receiving this because…" or "Sent with 💜…"

Delete the **entire enclosing `<table>...</table>`** (or `<div>`) — not just the
link — so the layout doesn't leave an empty bordered box.

**Why:** Web visitors aren't subscribers; the link would 404 or behave weirdly.
Subscribers already received it in their inbox.

---

## Things to PRESERVE (do not touch)

- The `<style>` block in `<head>` (Inter font `@import`, `@media (max-width:480px)`
  responsive rules, dark-mode `prefers-color-scheme` block) — all of it valid web CSS
- The body `style="background-color:#FBF9FF"` — this IS the universal background update
- All inline styles on every element (table-based email layout — required structure)
- All `<table role="presentation">` tags — these are the layout primitives
- The `🇺🇸 NATIONAL / 🌴 LOCAL / 🎉 FUN` 5-bullet columns
- The `HEY CUTIE` intro block with `-Wyatt` sendoff
- The `4-DAY FORECAST · LA` section
- `💭 QUOTE OF THE DAY`, `📅 TEMPLATE YEAR` history, `❓ TRIVIA QUESTION` blocks
- `🍴 E A T S 🍴` and `🌴 C O M M U N I T Y 🌴` section headers and all child cards
- Every backlink to `curations.org`, `curationsla.com`, instagram.com — these are
  the editorial citations and brand links

---

## Quality bar — what success looks like

After Wyatt pastes and saves, `https://www.curationsla.com/vibes/2026-04-21-lacma-x-coachella-vibes`
should render with:

1. ✅ Light purple `#FBF9FF` universal background visible immediately
2. ✅ All sections present in original order
3. ✅ No hidden preview-text padding anywhere in the DOM
4. ✅ No "View online" link near the masthead
5. ✅ No unsubscribe link at the bottom (and no empty bordered box where it was)
6. ✅ Mobile responsive `@media` rules still active (test at 480px viewport)
7. ✅ Excerpt on `/vibes` (archive index) shows real prose — NOT `@import url(...)`
   (the new `htmlToPlaintext()` strips `<style>` block contents before extraction,
   so this should be automatic)

---

## Output format requested from Atlas

Please return:

1. **The full cleaned HTML file**, ready to copy/paste into the Edit Content modal.
   Single fenced code block, no commentary inside it.
2. **A brief diff summary** — exactly which line ranges were removed, byte savings.
3. **(Optional) A "stripEmailOnlyArtifacts(html)" TypeScript helper function**
   that performs all three deletions programmatically. It would slot into
   `events-platform/lib/vibes-html.ts` and be called from the webhook
   `publishBroadcastToVibes()` flow so future broadcasts auto-clean. Reference
   shape:

   ```typescript
   /**
    * Removes email-client-only artifacts from broadcast HTML before web render.
    * Idempotent — safe to call repeatedly. Preserves <style> blocks, inline
    * styles, layout tables, and all editorial content.
    */
   export function stripEmailOnlyArtifacts(html: string): string {
     return html
       // 1. Hidden Gmail preview-text block (display:none + data-skip-in-text)
       .replace(/<div[^>]*data-skip-in-text="true"[\s\S]*?<\/div>\s*<\/div>/gi, '')
       // 2. "View online" paragraph (heuristic: contains slug + "online")
       .replace(/<p[^>]*class="node-paragraph"[^>]*>[\s\S]*?VIEW[^<]*ONLINE[\s\S]*?<\/p>/gi, '')
       // 3. Resend unsubscribe footer (heuristic: <table> containing unsubscribe URL pattern)
       .replace(/<table[^>]*>(?:(?!<table)[\s\S])*?(?:RESEND_UNSUBSCRIBE_URL|\/unsubscribe\/)[\s\S]*?<\/table>/gi, '')
   }
   ```

   Treat the regex above as a *starting point* — feel free to tighten it if you
   spot edge cases in the actual file.

---

## Repo / context references

- Webhook handler: `events-platform/app/api/webhooks/resend/route.ts`
- HTML utilities: `events-platform/lib/vibes-html.ts` (where `stripEmailOnlyArtifacts`
  would live)
- Admin lazy-load action: `getVibesPostHtml(id)` in `events-platform/app/admin/vibes/actions.ts`
- Admin save action: `updateVibesPostContent(id, html)` — the function the Edit
  Content modal calls. Re-extracts plaintext + reading time. Does NOT touch
  metadata, IDs, or feature_image.
- Vibes constants (allowed `source` / `publish_type` values): `events-platform/lib/vibes-constants.ts`
- Cloudflare CDN context: `media.curationsla.com` (R2 bucket, proxied via
  Cloudflare). The webhook's `extractFeatureImage()` already trusts both
  `media.curationsla.com` and `resend-attachments.s3.amazonaws.com` as feature
  image sources.

---

Thanks Atlas. Wyatt's been moving 100mph all day — let's make this paste a
one-shot win.

— Copilot