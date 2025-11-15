# Decisions Needed

## UI/UX
- [x] **Exact GitBook clone vs inspired with BUNKER identity**
  - **DECIDED:** Exact GitBook clone with "CURATED BY CURATIONS" branding (replaces "Powered by GitBook")
  - **Note:** BUNKER is a product of CURATIONS
  - **Date:** 2025-11-15
- [x] **Theme preference (minimal/bold/gradient/custom)**
  - **DECIDED:** Keep current BUNKER colors for now
  - **Current:** Purple-blue accent (`#667eea`), dark blue-gray primary (`#2c3e50`)
  - **Date:** 2025-11-15
- [x] **Mobile sidebar behavior**
  - **DECIDED:** Slide-out drawer
  - **Date:** 2025-11-15

## Community
- [x] **Section-level vs page-level voting**
  - **DECIDED:** Page-level voting
  - **Rationale:** Simpler, works with GitHub Discussions reactions
  - **Date:** 2025-11-15
- [x] **Anonymous allowed vs GitHub-auth only**
  - **DECIDED:** GitHub auth required for voting/commenting; public read access
  - **Rationale:** Spam-resistant, leverages Giscus
  - **Date:** 2025-11-15
- [x] **Public vote counts vs visual indicators**
  - **DECIDED:** "Popular" badge (visual indicator, not raw counts)
  - **Rationale:** Avoids popularity bias, focuses on quality
  - **Date:** 2025-11-15
- [x] **Moderation model (pre/post)**
  - **DECIDED:** Post-moderation via GitHub Discussions
  - **Note:** Understand monitoring requirements
  - **Date:** 2025-11-15

## Technical
- [x] **Motion library choice**
  - **DECIDED:** Motion One
  - **Rationale:** Lightweight, modern, framework-agnostic
  - **Date:** 2025-11-15
- [x] **Analytics platform**
  - **DECIDED:** Cloudflare Web Analytics
  - **Rationale:** Privacy-friendly, integrated with potential future Cloudflare deployment
  - **Date:** 2025-11-15
- [x] **Lighthouse targets**
  - **DECIDED:** Performance ≥90, Accessibility 100, Best Practices 100, SEO 100
  - **Date:** 2025-11-15

## Deployment
- [x] **Keep GitHub Pages vs later Cloudflare**
  - **DECIDED:** GitHub Pages for now
  - **Note:** Keep as current stable deployment method
  - **Date:** 2025-11-15
- [x] **Custom domain plans**
  - **DECIDED:** bunker.curations.org
  - **Action:** Configure CNAME after initial deployment
  - **Date:** 2025-11-15
- [x] **CDN/performance requirements**
  - **Current:** GitHub Pages CDN (adequate for MVP)
  - **Future:** Consider Cloudflare Pages for edge deployment
  - **Date:** 2025-11-15

## Notes
- Add rationale and links to discussions/PRs for each decision.
- Priority: Complete UI/UX and Community decisions before Stage 1 implementation.
- Technical and Deployment decisions can be refined during implementation.

## Decision Tracking Template

```markdown
### Decision: [Title]
**Date:** YYYY-MM-DD
**Decided by:** [Name/Role]
**Rationale:** [Brief explanation]
**Alternatives considered:** [List]
**References:** [Links to issues, PRs, discussions]
```
