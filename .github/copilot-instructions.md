# GitHub Copilot Instructions for ai-learning Repository

## Project Overview

**Repository**: CurationsLA/ai-learning  
**Project Name**: BUNKER (formerly CURATIONS)  
**Purpose**: Open-source frameworks, guides, and resources for AI development, collaboration, and creativity  
**Site**: https://hub.curations.org  
**Migration Date**: November 15, 2025 (BookGen → Astro + Starlight)

### What is BUNKER?

BUNKER is a Human × AI Creative Agency that builds:
- 🎨 Design systems and brand architecture
- 🤖 AI strategies and multi-agent systems
- 📖 Open learning resources and cookbooks
- 🌟 AI personas (Curators) with specialized expertise
- 🏙️ Community platforms (CurationsLA)
- 🌱 Youth empowerment programs (Youth Curator Movement)

**Philosophy**: Greater good creativity - every project asks "Does this make the world better?"

## Active Build System (November 2025)

### Primary: Astro + Starlight

**Technology Stack:**
- Framework: Astro v4.16.17
- Theme: @astrojs/starlight v0.28.4
- Language: TypeScript 5.6.3
- Node.js: 20.x

**Build Commands:**
```bash
npm install          # Install dependencies
npm run dev          # Start dev server (with HMR)
npm run build        # Type check + production build
npm run preview      # Preview production build
```

**Build Output:**
- Directory: `dist/`
- Pages: 41 static HTML pages
- Build time: ~16 seconds
- Search: Pagefind (6,763 words indexed)
- Deploy: GitHub Pages via `.github/workflows/deploy-pages.yml`

**Configuration Files:**
- `astro.config.mjs` - Astro + Starlight configuration
- `src/content/config.ts` - Content collection schema
- `tsconfig.json` - TypeScript configuration
- `package.json` - Dependencies and scripts

### Legacy: BookGen (Deprecated)

**Status**: Preserved for reference, not actively used  
**Purpose**: Custom GitBook alternative (Python-based)  
**Build**: `.bookgen/build.sh` or `python3 .bookgen/generator.py .`  
**Output**: `_book/` directory (git-ignored)

**Note**: BookGen is deprecated as of November 2025. Use Astro for all new development.

## Dual Content Strategy

### Active Content: `src/content/docs/`

**Primary source for all documentation:**
- All `.md` files with frontmatter
- Used by Astro build system
- Deployed to GitHub Pages
- Supports MDX format
- Required frontmatter: `title` (description optional)

**Structure:**
```
src/content/docs/
├── about-bunker.md
├── about-curationsla.md
├── cookbooks/
│   ├── README.md
│   ├── foundations/
│   ├── rag/
│   ├── agents/
│   ├── tools/
│   ├── business/
│   ├── legendary/
│   └── advanced-prompting/
├── design-systems.md
├── get-involved.md
├── technical-architecture.md
├── the-curators.md
└── youth-curator-movement.md
```

### Legacy Content: `docs/`

**Status**: Preserved but superseded by `src/content/docs/`  
**Purpose**: Original BookGen source files  
**Note**: Changes should be made in `src/content/docs/`, not `docs/`

### Navigation Structure

**Configured in**: `astro.config.mjs` sidebar property  
**Do NOT edit**: `SUMMARY.md` (legacy BookGen navigation)  
**Sidebar sections:**
- 🏠 Welcome
- 🌱 Community
- 📚 Cookbooks (with auto-generated subdirectories)

## Creative Learning Labels

### The 6 Growth Emojis

BUNKER uses a progressive learning taxonomy inspired by plant growth:

**🌱 Seedling Concept** - Beginner-friendly introduction
- Quick overview for newcomers
- High-level explanation without jargon
- Example: "What is Memory Management?"

**🌿 Sprout Details** - Intermediate concepts
- Practical implementation details
- Code examples and patterns
- Example: "Memory Categories and Storage"

**🌳 Forest Knowledge** - Advanced mastery
- Production-ready patterns
- Scaling and optimization
- Example: "Multi-Session Memory Architecture"

**💡 Insight** - Key ideas and clarifications
- "Aha!" moments
- Important gotchas
- Example: "GenerateMemories: The Foundation"

**⚡ Quick Win** - Fast, practical solutions
- Minimal viable implementation
- Copy-paste ready code
- Example: "Minimal Memory System in 10 lines"

**🔬 Deep Dive** - Research and experimentation
- Advanced research topics
- Experimental patterns
- Example: "Deep Dive: Memory Retrieval Algorithms"

### Usage Guidelines

1. **Headers**: Use emojis in section headers for visual hierarchy
   ```markdown
   ## 🌱 Seedling Concept
   ## 💡 Key Insight
   ## ⚡ Quick Win: Minimal Setup
   ```

2. **Progressive disclosure**: Structure content from 🌱 → 🌿 → 🌳
3. **Consistency**: Use the same emoji for similar concept levels across documents
4. **Context**: Emojis should clarify learning level, not replace clear writing

### Examples in the Wild

See these files for reference:
- `src/content/docs/cookbooks/foundations/03-memory-management.md`
- `src/content/docs/cookbooks/advanced-prompting/temporal-debugging.md`
- `src/content/docs/cookbooks/advanced-prompting/emoji-protocol.md`

## Development Workflow

### Making Changes

1. **Create a branch** from main
2. **Edit files** in `src/content/docs/`
3. **Add frontmatter** to new pages:
   ```yaml
   ---
   title: Your Page Title
   description: Optional description
   ---
   ```
4. **Test locally**: `npm run dev`
5. **Build**: `npm run build`
6. **Commit and push**
7. **Open PR** for review

### Testing Procedures

**Local Development:**
```bash
npm run dev
# Visit http://localhost:4321/ai-learning
```

**Production Build:**
```bash
npm run build
# Check for type errors
# Verify build completes successfully
# Check dist/ output
```

**Preview Production:**
```bash
npm run preview
# Test search functionality (only works in production)
```

**Validation Checklist:**
- [ ] No TypeScript errors (`astro check`)
- [ ] Build completes without errors
- [ ] All pages render correctly
- [ ] Navigation links work
- [ ] Search indexes content (production only)
- [ ] Frontmatter is valid YAML
- [ ] No broken internal links

## Common Issues & Troubleshooting

### Build Errors

**"Frontmatter parse error"**
- Check YAML syntax in `---` blocks
- Quote titles containing colons: `title: "AI: The Future"`
- Ensure proper indentation

**"Module not found"**
- Run `npm install` to install dependencies
- Check `package.json` for correct versions
- Clear `node_modules` and reinstall if needed

**"Type error in content collection"**
- Verify frontmatter matches schema in `src/content/config.ts`
- Required: `title` field
- Optional: `description` field

### Navigation Issues

**Sidebar not updating**
- Edit `astro.config.mjs` sidebar configuration
- Do NOT edit `SUMMARY.md` (legacy file)
- Restart dev server after config changes

**Page not showing in sidebar**
- Add entry to `astro.config.mjs`
- Or place in `cookbooks/` subdirectory (auto-generated)
- Ensure file has valid frontmatter

### Search Not Working

**Problem**: Search shows no results
**Solution**: Search only works in production builds
```bash
npm run build
npm run preview
```

### Deployment Issues

**GitHub Pages not updating**
- Check `.github/workflows/deploy-pages.yml` workflow status
- Verify push to `main` branch (triggers deployment)
- Check GitHub Pages settings: source = GitHub Actions
- Allow 2-3 minutes for deployment to complete

## Project-Specific Conventions

### File Naming

- Use kebab-case: `memory-management.md`, `rag-fundamentals.md`
- README files: uppercase `README.md`
- Config files: lowercase with extension (`astro.config.mjs`)

### Content Structure

**Standard page template:**
```markdown
---
title: Page Title Here
description: Optional short description
---

# Page Title Here

## 🌱 Seedling Concept

Brief introduction for beginners...

## What is [Topic]?

Core explanation...

## 💡 Key Insights

Important points...

## 🌿 Practical Implementation

Code examples and details...

## ⚡ Quick Win

Minimal working example...

## 🌳 Advanced Patterns

Production-ready patterns...

## 🔬 Deep Dive

Research and experimentation...
```

### Code Blocks

Use language-specific syntax highlighting:
```python
# Python example
def example():
    pass
```

```javascript
// JavaScript example
const example = () => {};
```

### Links

**Internal links**: Use relative paths
```markdown
[Link to page](/about-bunker/)
[Link in same directory](./sibling-page/)
```

**External links**: Full URLs with https://
```markdown
[Astro Docs](https://docs.astro.build)
```

## Brand Context

### Name Evolution

- **Original**: CURATIONS
- **Current**: BUNKER (as of November 2025)
- **Migration note**: Some legacy files may still reference "CURATIONS" or "VibeHub"

### Key Entities

1. **BUNKER**: Main creative agency brand
2. **CurationsLA**: Hyperlocal LA media platform (https://la.curations.cc)
3. **Youth Curator Movement**: Educational empowerment initiative
4. **The Curators**: AI personas with specialized expertise

### Core Values

- Greater good creativity
- Human × AI collaboration (not replacement)
- Ethical, transparent, community-centered
- Open learning and documentation
- Non-political, focused on good

## Additional Resources

**Documentation Files:**
- `MIGRATION.md` - BookGen → Astro migration details
- `readme.md` - Main project README
- `BOOKGEN.md` - Deprecated BookGen documentation
- `VALIDATION_CHECKLIST.md` - Content validation guide

**External Links:**
- [Astro Documentation](https://docs.astro.build)
- [Starlight Documentation](https://starlight.astro.build)
- [GitHub Repository](https://github.com/CurationsLA/ai-learning)

## Quick Reference Card

```bash
# Development
npm run dev              # Start dev server

# Building
npm run build            # Production build
npm run preview          # Preview production

# File Locations
src/content/docs/        # Edit content here (active)
docs/                    # Legacy content (deprecated)
astro.config.mjs         # Sidebar navigation
dist/                    # Build output (git-ignored)

# Key Patterns
🌱 🌿 🌳                 # Learning progression
💡 ⚡ 🔬                 # Insights, wins, research
```

---

**Last Updated**: November 15, 2025  
**Maintained By**: GitHub Copilot and BUNKER Team
