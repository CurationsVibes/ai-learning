# Community Features Architecture

## Overview
- **Goal:** Propose architecture for comments and voting using Discussions/Giscus.

## Commenting (Giscus)
- **Backend:** GitHub Discussions
- **Mapping:** pathname (1 Discussion thread per page)
- **Categories:** "Documentation Feedback"
- **Config:** 
  - Reactions enabled
  - Lazy loading
  - Theme synced with site (light/dark/auto)
  - Input position: top

### Giscus Configuration (Tony provides after setup)
```json
{
  "repo": "CurationsLA/ai-learning",
  "repoId": "[PENDING_FROM_TONY]",
  "category": "Documentation Feedback",
  "categoryId": "[PENDING_FROM_TONY]",
  "mapping": "pathname",
  "reactionsEnabled": "1",
  "theme": "preferred_color_scheme",
  "lang": "en",
  "loading": "lazy"
}
```

## Voting Options (to evaluate)

### Option A: Reactions as votes (Recommended for MVP)
- Use GitHub Discussions reactions (+1, ❤️, 🚀) as page-level votes
- Pros: No backend, leverages Giscus, spam-resistant (GitHub auth)
- Cons: Requires GitHub login, page-level only (not section-level)

### Option B: Separate category threads for votes
- Create "Page Votes" Discussion category
- Each page = 1 vote thread
- Pros: Clean separation from comments
- Cons: More complex, still page-level only

### Option C: Custom store (defer; not MVP)
- LocalStorage + serverless function (Cloudflare Worker)
- Pros: Anonymous voting, section-level possible, full control
- Cons: Backend maintenance, spam risk, more complexity

## Moderation/Spam
- **Settings:** Interaction limits, Discussion moderation via GitHub
- **Admins:** Repository maintainers (GitHub permissions)
- **Workflow:** Monitor Discussions, lock/delete spam, leverage GitHub's tools

## Data/Privacy
- **GitHub auth:** Required for comments/votes (Option A/B)
- **No PII storage:** Leverages GitHub profiles only
- **LocalStorage:** Only for UI state (collapsed sections, theme preference)

## Open Questions
- [ ] Section-level vs page-level voting?
- [ ] Public counts vs visual indicators?
- [ ] Anonymous feedback policy?
- [ ] Follow-up form for negative feedback ("Was this helpful?" → No)?

## Dependencies
- **Critical (Tony's checklist):**
  - [ ] Enable GitHub Discussions
  - [ ] Create "Documentation Feedback" category
  - [ ] Install Giscus app: https://github.com/apps/giscus
  - [ ] Generate repo ID and category ID
  - [ ] Provide config to Michael (environment variables)

## Citations
- external: https://docs.github.com/en/discussions
- external: https://giscus.app/
- repo: `.github/workflows/deploy-pages.yml`
