# UI/UX Comparison — Current vs Desired

## Overview
- **Goal:** Document gaps between current Starlight UI and GitBook-inspired target.

## Current (Starlight) Snapshot
- **Sidebar behavior:** Collapsible sections, autogenerate from directories
- **Typography/spacing:** Custom BUNKER branding (purple-blue accent `#667eea`, primary `#2c3e50`)
- **Search:** Pagefind integration (6,763 words indexed)
- **Page layout:** 3-column (nav, content, TOC), responsive mobile

## Desired (GitBook-inspired) Traits
- Collapsible, multi-level sidebar with section context.
- Clean typography with balanced white space.
- Smooth transitions and motion primitives.
- Consistent breadcrumb and in-page ToC.

## Gap Analysis
- **Sidebar:** Basic collapse present; needs smoother animations, hover states, active item highlighting
- **Search:** Working with Pagefind; consider keyboard shortcuts (Cmd+K)
- **Layout:** 3-column present; refinements needed for reading width, whitespace
- **Theming:** BUNKER purple established; decide if keeping or shifting to GitBook blue/green

## References
- GitBook changelog and sidebar posts.
- Motion design principles (motion.dev).

## Screenshots/Links
- **Current:** `https://hub.curations.org`
- **References:** 
  - https://changelog.gitbook.com/
  - https://www.gitbook.com/blog/new-sidebar

## Citations
- repo: `astro.config.mjs` (sidebar, base path)
- repo: `src/content/config.ts` (docs schema)
- repo: `src/styles/custom.css` (BUNKER branding)
- external: https://changelog.gitbook.com/
- external: https://www.gitbook.com/blog/new-sidebar
