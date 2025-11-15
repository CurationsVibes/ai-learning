# GitBook Hybrid UI — Overview

## Overview
- **Goal:** Define the GitBook-inspired UI/UX vision and constraints for BUNKER's docs.
- **Audience:** Contributors and stakeholders.
- **Scope:** UI/UX, community features, and deployment constraints.
- **Success Criteria:**
  - Clean Astro builds; no regressions.
  - Clear decisions list for MVP and next stages.
  - Measurable UX targets (e.g., Lighthouse ≥90).

## Context
- **Current site:** Astro + Starlight (active), BookGen (legacy).
- **Deployment:** GitHub Pages via Actions.
- **Content:** `src/content/docs/` (active), `docs/` (legacy).

## Constraints
- No breaking changes to build/deploy without approval.
- Avoid speculative features; document options with tradeoffs.

## Key Milestones
- Phase 1–3 planning
- Stage 1: UI/UX foundation
- Stage 2: Community MVP
- Stage 3: Advanced
- Stage 4: Polish

## Assumptions / Unknowns
- Default branch = main (confirmed ✓)
- Discussions/Giscus to be enabled (pending Tony)
- Branding guidelines path confirmation

## Citations
- repo: `astro.config.mjs`
- repo: `package.json`
- repo: `src/content/config.ts`
- repo: `.github/workflows/deploy-pages.yml`
