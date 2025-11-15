# GitHub Copilot Instructions for AI Learning Repository

## Repository Overview

This repository, **BUNKER** (formerly CURATIONS), is an open-source documentation platform for AI development frameworks, guides, and resources. It uses **Astro with Starlight** for static site generation and is deployed to GitHub Pages.

## Build System

### Primary Build System: Astro + Starlight (Active)
- **Framework**: Astro 4.16+ with Starlight 0.28+
- **Build Command**: `npm run build`
- **Dev Server**: `npm run dev` or `npm start`
- **Output Directory**: `dist/`
- **Base Path**: `/ai-learning`
- **Site URL**: `https://curationsla.github.io/ai-learning`

### Build Process
1. Type checking: `astro check`
2. Static site generation: `astro build`
3. Search indexing: Pagefind (6,763+ words indexed)
4. Expected output: 41 pages built in ~15-20 seconds

### Legacy Build System: BookGen (Deprecated but Functional)
- **Build Command**: `./.bookgen/build.sh`
- **Output Directory**: `_book/` (git-ignored)
- **Status**: Maintained for backward compatibility only
- **Migration Date**: November 2025

## Content Structure

### Source Files
- **Markdown Content**: `src/content/docs/`
- **Content Schema**: `src/content/config.ts` using `docsSchema` from Starlight
- **Navigation**: Defined in `astro.config.mjs` sidebar configuration

### Key Directories
```
src/content/docs/
├── cookbooks/              # Learning content organized by topic
│   ├── foundations/        # Foundational concepts
│   ├── agents/            # Agent development
│   ├── rag/               # RAG and grounding
│   ├── tools/             # MCP, A2A, tool ecosystems
│   ├── business/          # Business applications
│   ├── advanced-prompting/ # Advanced techniques
│   └── legendary/         # Advanced production topics
├── about-bunker.md        # Project overview
├── about-curationsla.md   # Organization info
├── design-systems.md      # Design documentation
├── get-involved.md        # Contribution guide
├── technical-architecture.md
└── the-curators.md
```

### Navigation Configuration (astro.config.mjs)
The sidebar is organized into three main sections:
1. **🏠 Welcome**: About, Get Involved, Design Systems, Technical Architecture, The Curators
2. **🌱 Community**: About CurationsLA, Youth Curator Movement
3. **📚 Cookbooks**: Auto-generated from `cookbooks/` directory (collapsed by default)

## Content Guidelines

### Learning Labels (Seedling Concept)
Many cookbook pages use a "Seedling Concept" structure with learning labels:
```markdown
## 🌱 Seedling Concept

**Label**: [Brief, memorable phrase]
```

Example from `03-memory-management.md`:
```markdown
**Label**: Giving Your Agents a Memory
```

### Markdown Style
- Use emoji for visual hierarchy (🌱, 📝, 🔍, 🎯, etc.)
- Include code examples with syntax highlighting
- Provide practical examples and use cases
- Keep explanations clear and accessible

## Dependencies

### Core Dependencies (package.json)
```json
{
  "astro": "^4.16.17",
  "@astrojs/starlight": "^0.28.4"
}
```

### Dev Dependencies
```json
{
  "@astrojs/check": "^0.9.4",
  "typescript": "^5.6.3"
}
```

## Deployment

### Current Deployment: GitHub Pages
- **Workflow**: `.github/workflows/deploy-pages.yml`
- **Trigger**: Push to `main` branch or manual workflow dispatch
- **Build**: Node.js 20, npm ci, astro build
- **Pages Configuration**: Configured via GitHub Pages settings
- **Permissions**: `contents: read`, `pages: write`, `id-token: write`

### Future Consideration
- Potential migration to Cloudflare Pages (documented but not implemented)
- No active implementation planned yet

## Development Workflow

### Before Making Changes
1. Verify build works: `npm run build`
2. Test locally: `npm run dev`
3. Check existing content structure
4. Review MIGRATION.md for context

### Adding New Content
1. Create markdown files in `src/content/docs/`
2. Use Starlight's docsSchema for frontmatter
3. Follow existing naming conventions (kebab-case)
4. Update navigation in `astro.config.mjs` if needed (or rely on autogenerate)

### Build Verification Checklist
- ✅ Astro build passes (`npm run build`)
- ✅ No type errors from `astro check`
- ✅ All pages render correctly (check dist/ output)
- ✅ Search indexing completes (Pagefind)
- ✅ No broken links in navigation

## Important Files Reference

### Configuration Files
- `astro.config.mjs` (lines 1-46): Site config, sidebar structure, base path
- `package.json` (lines 1-17): Scripts, dependencies
- `src/content/config.ts` (lines 1-7): Content schema
- `tsconfig.json`: TypeScript configuration

### Documentation Files
- `MIGRATION.md` (lines 1-50): BookGen → Astro migration context
- `SUMMARY.md`: Current table of contents (40 links)
- `SUMMARY_BOOKGEN.md`: Legacy BookGen navigation
- `readme.md`: Repository overview

### Workflow Files
- `.github/workflows/deploy-pages.yml` (lines 1-50): GitHub Pages deployment

## Common Tasks

### Adding a New Cookbook Page
1. Create file: `src/content/docs/cookbooks/[category]/[topic].md`
2. Add frontmatter (optional with docsSchema)
3. Build and verify: `npm run build`
4. Navigation auto-updates (or manual update in astro.config.mjs)

### Updating Navigation
Edit `astro.config.mjs` sidebar array:
```javascript
sidebar: [
  {
    label: '🏠 Welcome',
    items: [
      { label: 'About BUNKER', link: '/about-bunker/' },
      // ...
    ],
  },
]
```

### Testing Search
1. Build site: `npm run build`
2. Verify Pagefind output in console (should show ~6,763+ words indexed)
3. Preview: `npm run preview`

## Constraints and Limitations

### What NOT to Change
- Do not modify build configuration unless absolutely necessary
- Do not change base path or site URL (affects deployment)
- Do not remove or modify SUMMARY.md links without verification
- Do not break backward compatibility with BookGen unless migrating

### File Ownership
- **Active System**: Astro + Starlight files in `src/`, `astro.config.mjs`, `package.json`
- **Legacy System**: `.bookgen/`, `SUMMARY_BOOKGEN.md`, `book.json`
- **Shared**: Markdown content in `docs/` (being migrated to `src/content/docs/`)

## Undefined/Future Features

### Not Implemented (Do Not Assume)
- **"Silverlining"**: No documentation or implementation exists
- **"mintify"**: No documentation or implementation exists
- **Cloudflare Pages**: Documented as potential future target, not currently used

### Current Active Systems Only
- Astro + Starlight is the primary active build system
- GitHub Pages is the current deployment target
- BookGen is legacy but still functional

## Troubleshooting

### Build Failures
1. Check Node.js version (should be 20+)
2. Clear node_modules and reinstall: `rm -rf node_modules package-lock.json && npm install`
3. Verify all markdown files have valid frontmatter
4. Check for syntax errors in astro.config.mjs

### Link Integrity
- All SUMMARY.md links should be valid (40/40)
- No orphaned files should exist
- Navigation should be coherent across all pages

## Summary

This repository uses modern static site generation with Astro and Starlight. When working with content:
- Respect the existing structure and conventions
- Test builds before committing
- Maintain navigation coherence
- Follow the Seedling Concept pattern for learning content
- Only reference implemented features and systems
