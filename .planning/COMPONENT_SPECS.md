# Component Specifications

## Overview
- **Goal:** Define component requirements and acceptance criteria.

## Components

### Sidebar (Collapsible)
- **Behavior:** collapse/expand, persist state (localStorage)
- **Accessibility:** keyboard nav, ARIA roles, focus management
- **Performance:** minimal layout shift, smooth 300-400ms transitions

### Page Shell
- **Header:** Site title, search, theme toggle, social links
- **Breadcrumb:** Optional; format `Home > Cookbooks > Section > Page`
- **In-page ToC:** Right sidebar, auto-generated from H2-H6, active section highlighting
- **Content width:** ~65-75ch for comfortable reading
- **Code blocks:** Syntax highlighting (already present)
- **Footer:** "Was this helpful?" widget, last updated, reading time

### Search
- **Current:** Pagefind integration (working)
- **Enhancements:** Keyboard shortcuts (Cmd+K), result previews, recent searches
- **Decision needed:** Keep Pagefind or switch to Algolia DocSearch

### Motion/Transitions
- **Animations:** Sidebar expand/collapse, scroll-to-section, fade-in content
- **Library options:** Vanilla CSS, Motion One (recommended), Framer Motion, GSAP
- **Accessibility:** Respect `prefers-reduced-motion`

## Acceptance Criteria (per component)
- **Tests:** Visual regression, keyboard navigation, screen reader compatibility
- **Performance:** No console errors, CLS < 0.1, LCP < 2.5s
- **Lighthouse:** Performance ≥90, Accessibility 100, Best Practices 100, SEO 100

## Citations
- repo: `astro.config.mjs`
- repo: `package.json`
- repo: `src/styles/custom.css`
- external: https://motion.dev/
