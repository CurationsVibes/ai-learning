# Coordination Notes for Tony (GitHub Cloud Agent)
## GitBook-Inspired Hybrid Documentation Platform

**Date**: 2025-11-15
**From**: Stanley (Claude Code)
**Working with**: Michael (VS Code Copilot)
**Repository**: CurationsLA/ai-learning

---

## Your Role in This Mission

You're the **infrastructure coordinator** and **PR manager** for this GitBook-inspired hybrid implementation. Michael handles local dev work, you handle GitHub configuration and deployment coordination.

---

## Current State

**Repository**: `CurationsLA/ai-learning`
**Active Branch**: `claude/repo-analysis-git-setup-01QK84kbVMRZyQPKeXXcdrLY`
**Main Branch**: (needs confirmation - likely `main`)
**Current Deployment**: GitHub Pages (Astro/Starlight)
**Status**: Clean working tree

**Recent Activity**:
- BUNKER rebrand completed (commits 195c73f, 7bbb636)
- GitHub Pages enabled (commit 431f14e)
- Astro/Starlight migration done
- Stanley completed repository analysis

---

## Phase 1-3: Michael's Planning Work

Michael is currently working on **planning and audit** (no code implementation yet):

### Phase 1: Foundation Audit
- Verify Astro build works
- Clean up legacy "VibeHub" references → "BUNKER"
- Ensure dev environment stable

### Phase 2: UI/UX Research
- Document current vs desired GitBook-inspired UI
- Create component specifications
- Gap analysis

### Phase 3: Community Features Architecture
- Research Giscus (GitHub Discussions integration)
- Propose data storage options
- Document unknowns for user decision

**Timeline**: Michael will complete planning and report to you with handoff summary.

---

## Your Enhancements Checklist

These GitHub-level configurations need to happen **before** Michael can implement community features:

### Enhancement 1: GitHub Discussions ✅ or ❌?

**Status**: Unknown - **ACTION REQUIRED**: Check if enabled

**Check**:
1. Go to repository settings
2. Look for "Discussions" tab
3. Verify if enabled

**If Not Enabled**:
1. Enable GitHub Discussions for repository
2. Create initial categories:
   - 📚 Documentation Feedback (for Giscus comments)
   - 🗳️ Page Votes (for upvoting integration)
   - 💡 Feature Requests
   - 🙋 Q&A

**Why Needed**: Giscus uses GitHub Discussions as backend for comments and voting.

**Documentation**: https://docs.github.com/en/discussions

---

### Enhancement 2: Giscus App Installation

**Status**: Not installed - **ACTION REQUIRED**

**Steps**:
1. Install Giscus GitHub App: https://github.com/apps/giscus
2. Grant access to `CurationsLA/ai-learning` repository
3. Configure Giscus:
   - Choose Discussion category: "Documentation Feedback"
   - Enable reactions: ✅
   - Choose mapping: `pathname` (maps URL to discussion)
   - Lazy loading: ✅

4. Generate Giscus embed code (for Michael to integrate)
5. Document configuration settings

**Why Needed**: Giscus powers the commenting system with upvoting via GitHub reactions.

**Documentation**: https://giscus.app/

**Deliverable**: Provide Michael with:
```javascript
{
  "repo": "CurationsLA/ai-learning",
  "repoId": "[YOUR_REPO_ID]",
  "category": "Documentation Feedback",
  "categoryId": "[YOUR_CATEGORY_ID]",
  "mapping": "pathname",
  "reactions": "1",
  "theme": "light"
}
```

---

### Enhancement 3: Repository Settings for Community

**Status**: Review needed - **ACTION REQUIRED**

**Check These Settings**:

**Settings > General**:
- [ ] Issues: Enabled (for bug reports)
- [ ] Discussions: Enabled (confirmed from Enhancement 1)
- [ ] Projects: Enabled or Disabled (user preference)
- [ ] Wiki: Disabled (using docs site instead)

**Settings > Moderation**:
- [ ] Interaction limits: Set to "Limit to existing users" or "Limit to prior contributors" (prevents spam)
- [ ] Comment moderation: Consider enabling for Discussions

**Settings > Pages**:
- [ ] Source: Confirm still set to GitHub Actions (Astro deployment)
- [ ] Custom domain: None (or document if configured)
- [ ] Enforce HTTPS: ✅

**Why Needed**: Ensures community features work properly and spam is controlled.

---

### Enhancement 4: Branch Protection & Workflow

**Status**: Review needed - **ACTION REQUIRED**

**Main Branch Protection** (if not already set):
- Require pull request before merging: ✅
- Require approvals: 1 (or user preference)
- Dismiss stale reviews: ✅
- Require status checks: Astro build must pass

**Feature Branch Workflow**:
Michael will create: `docs/gitbook-hybrid-ui-planning`
- This branch for planning documents (Phase 1-3)
- Future branches: `feature/collapsible-sidebar`, `feature/section-upvoting`, etc.

**PR Template**: Consider adding `.github/PULL_REQUEST_TEMPLATE.md` with checklist:
```markdown
## Changes
- [ ] Files changed: [list]
- [ ] SUMMARY.md updated: yes/no
- [ ] Build passes: yes/no
- [ ] Screenshots (if UI changes): [attach]

## Testing
- [ ] Local build successful
- [ ] Tested in: [browsers/devices]
- [ ] No console errors

## Documentation
- [ ] Updated relevant docs
- [ ] Added comments to complex code
```

**Why Needed**: Maintains code quality and clear review process.

---

### Enhancement 5: GitHub Actions Workflow Check

**Status**: Review needed - **ACTION REQUIRED**

**Existing Workflows** (from repo):
- `deploy-pages.yml` - Astro deployment to GitHub Pages
- `openapi-spec-workflow.yml` - API spec validation

**Action Items**:
1. Verify `deploy-pages.yml` is working correctly
2. Check recent workflow runs for errors
3. Ensure Node.js version matches local dev (20.x)
4. Consider adding:
   - Lighthouse CI (performance checks)
   - Accessibility testing
   - Link checker (broken link detection)

**Why Needed**: Automated quality checks catch issues before deployment.

---

## Communication Flow

### When Michael Completes Phase 1-3

**You'll Receive** (via handoff):
- Branch name: `docs/gitbook-hybrid-ui-planning`
- Planning documents committed
- List of unknowns requiring user decision
- Build status report

**Your Actions**:
1. Review planning documents
2. Confirm all enhancements (above) are complete
3. Create PR for planning phase:
   - Title: `docs: GitBook hybrid UI planning and architecture`
   - Label: `documentation`, `planning`
   - Assign: User for review
4. Present unknowns to user for architectural decisions

**PR Description Template**:
```markdown
## GitBook Hybrid UI - Planning Phase Complete

This PR contains planning documents for implementing a GitBook-inspired UI/UX with community upvoting features.

### Documents Included
- UI/UX comparison analysis
- Component specifications
- Community features architecture proposals
- Data storage options evaluation
- Implementation roadmap

### Infrastructure Ready
- [x] GitHub Discussions enabled
- [x] Giscus installed and configured
- [x] Repository settings reviewed
- [x] Branch protection updated
- [x] CI/CD workflows verified

### Decisions Needed
[List unknowns from Michael's handoff]
1. Section-level vs page-level voting?
2. Anonymous voting allowed?
3. [etc.]

### Next Steps
After user approves architecture:
1. Michael implements Stage 1 (UI/UX foundation)
2. Tony coordinates any additional GitHub setup
3. Iterative development with PRs per feature

### Build Status
✅ Astro builds successfully
✅ No errors introduced
✅ Dev server runs clean
```

---

### When Michael Starts Implementation (Post-Planning)

**You'll Need to**:
1. Monitor PRs for each feature stage
2. Run CI/CD checks
3. Coordinate deployments to GitHub Pages
4. Manage branch merges

**PR Cadence** (Expected):
- Stage 1: UI/UX Foundation (~3-5 PRs for components)
- Stage 2: Community Features MVP (~2-3 PRs)
- Stage 3: Advanced Features (~variable)
- Stage 4: Polish & Testing (~1-2 PRs)

---

## Coordination Protocol

### Daily Sync (Asynchronous)

**Michael Updates You On**:
- Completed tasks (with evidence)
- Blockers or issues
- Ready-for-review PRs

**You Update Michael On**:
- PR review status
- CI/CD results
- User decisions on unknowns
- Any infrastructure changes

**Stanley (Me) Coordinates**:
- High-level architecture decisions
- Cross-agent task dependencies
- User communication facilitation

---

### Escalation Path

**If Michael is Blocked**:
1. Michael documents blocker → Tony
2. Tony assesses if infrastructure-related
3. Tony resolves or escalates to user
4. Tony updates Michael with resolution

**If CI/CD Fails**:
1. Tony captures error logs
2. Tony assesses: code issue or infrastructure issue
3. If code: notify Michael
4. If infrastructure: Tony fixes
5. Both: coordinate fix

**If User Changes Requirements**:
1. User informs Tony or Stanley
2. Tony creates new issue/discussion
3. Michael pauses current work
4. Team reviews impact and re-plans

---

## Success Criteria (Your Side)

### Infrastructure Setup ✅
- [ ] GitHub Discussions enabled with proper categories
- [ ] Giscus app installed and configured
- [ ] Repository settings optimized for community
- [ ] Branch protection rules in place
- [ ] CI/CD workflows validated

### PR Management ✅
- [ ] Planning phase PR created and merged
- [ ] Feature PRs reviewed within 24 hours
- [ ] Build checks passing before merge
- [ ] Deployment successful after merge

### Communication ✅
- [ ] Michael has all necessary GitHub config details
- [ ] User receives timely updates on progress
- [ ] Stanley informed of any blockers
- [ ] Documentation updated with new features

---

## Risks & Mitigations

### Risk 1: Giscus Rate Limits
**Impact**: Too many API calls if high traffic
**Mitigation**: Implement caching, lazy loading, monitor usage
**Owner**: Michael (implementation), Tony (monitoring)

### Risk 2: GitHub Discussions Spam
**Impact**: Community features abused by spam
**Mitigation**: Enable interaction limits, moderation settings
**Owner**: Tony (GitHub settings), User (moderation)

### Risk 3: Build Failures on PR
**Impact**: Delays in merging features
**Mitigation**: Local build validation before PR, CI checks
**Owner**: Michael (pre-PR checks), Tony (CI monitoring)

### Risk 4: Breaking Changes to Main
**Impact**: Production site goes down
**Mitigation**: Branch protection, required reviews, staging environment
**Owner**: Tony (protection rules), Team (review rigor)

---

## Resources & Documentation

**For You (Tony)**:
- GitHub Discussions: https://docs.github.com/en/discussions
- Giscus: https://giscus.app/
- GitHub Actions: https://docs.github.com/en/actions
- Branch Protection: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches

**For Michael**:
- Astro Docs: https://docs.astro.build/
- Starlight: https://starlight.astro.build/
- Giscus Integration: https://giscus.app/
- Motion Library: https://motion.dev/ (for animations)

**Shared References**:
- GitBook Changelog: https://changelog.gitbook.com/
- GitBook Sidebar Post: https://www.gitbook.com/blog/new-sidebar
- BUNKER Brand Guide: `/home/user/ai-learning/docs/welcome/design-systems.md`

---

## Current Action Items (Priority Order)

### 🔴 High Priority (Do First)
1. **Check GitHub Discussions status** - Is it enabled?
2. **Install Giscus app** - Needed for MVP features
3. **Review repository settings** - Ensure optimal config
4. **Verify CI/CD workflows** - Confirm builds working

### 🟡 Medium Priority (Do Soon)
5. **Set branch protection rules** - If not already set
6. **Create PR template** - Standardize review process
7. **Document GitHub config** - For Michael's reference

### 🟢 Low Priority (Do Later)
8. **Consider additional workflows** - Lighthouse, a11y testing
9. **Plan staging environment** - If needed for testing
10. **Setup project board** - For task tracking (optional)

---

## Questions for User (Gather & Document)

**Infrastructure**:
- Preferred moderation workflow for Discussions?
- Want staging environment or just PR previews?
- Analytics platform preference?

**Deployment**:
- Keep GitHub Pages or migrate to Cloudflare Pages later?
- Custom domain plans?
- CDN/performance requirements?

**Community**:
- Who has moderation rights for Discussions?
- Public vote counts or private?
- Spam prevention threshold?

---

## Final Coordination Notes

**Remember**:
- Michael handles local dev, you handle GitHub infra
- Stanley coordinates high-level architecture
- User makes final architectural decisions
- Frequent, transparent communication prevents blockers

**Communication Channels**:
- Technical updates: Via PR comments
- Blockers: Via Issues or direct mention
- Architecture decisions: Via Stanley
- User approvals: Via PR review or Stanley

**This is a multi-stage project**. Phase 1-3 is planning. Implementation comes after user approves architecture. Your enhancements checklist above should be complete before Michael starts building.

---

**Stanley has both your backs throughout this process.**

End of coordination notes.
