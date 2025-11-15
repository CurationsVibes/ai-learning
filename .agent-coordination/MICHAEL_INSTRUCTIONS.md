# Instructions for Michael (VS Code Copilot)
## GitBook-Inspired Hybrid Documentation Platform

**Date**: 2025-11-15
**From**: Stanley (Claude Code)
**Via**: Tony (GitHub Cloud Agent)
**Branch**: `claude/repo-analysis-git-setup-01QK84kbVMRZyQPKeXXcdrLY`

---

## Mission Overview

Implement a **GitBook-inspired UI/UX** on the existing **Astro/Starlight** foundation with **community upvoting features** that GitBook itself doesn't have.

**Why Hybrid**: GitBook open-source code was deprecated in 2018. We're taking visual/UX inspiration from their 2025 design system while building on modern tech (Astro) with custom features (section upvoting, advanced community interactions).

---

## Phase 1: Foundation Audit & Cleanup (Start Here)

### Task 1.1: Repository State Assessment

**Objective**: Understand current state and identify what needs updating.

**Actions**:
1. Run git status and verify you're on branch: `claude/repo-analysis-git-setup-01QK84kbVMRZyQPKeXXcdrLY`
2. Check for any uncommitted changes from Stanley's analysis
3. Pull latest from remote if needed

**Commands**:
```bash
git status
git pull origin claude/repo-analysis-git-setup-01QK84kbVMRZyQPKeXXcdrLY
```

**Report to Tony**: Current branch state, any conflicts

---

### Task 1.2: Build System Verification

**Objective**: Confirm Astro/Starlight builds successfully.

**Actions**:
1. Install dependencies: `npm ci`
2. Run build: `npm run build`
3. Run dev server: `npm run dev`
4. Document any errors with exact messages

**Success Criteria**:
- Build completes without errors
- Dev server runs on expected port
- Site loads in browser with BUNKER branding

**If Build Fails**:
- Capture full error output
- Check `package.json` dependencies
- Report to Tony with error details and proposed fix

**Citations**:
- Build config: `/home/user/ai-learning/astro.config.mjs`
- Dependencies: `/home/user/ai-learning/package.json`

---

### Task 1.3: Legacy References Cleanup

**Objective**: Update remaining "VibeHub" references to "BUNKER".

**Known Issues**:
- `/home/user/ai-learning/book.json:2` - Title still says "VibeHub"
- `/home/user/ai-learning/book.json:4` - Author still says "VibeHub"
- `/home/user/ai-learning/book.json:46` - Sidebar link label

**Actions**:
1. Update `book.json`:
   - Line 2: Change title to "BUNKER - Human × AI Creative Agency"
   - Line 4: Change author to "BUNKER by CurationsLA"
   - Line 46: Change "VibeHub Website" to "BUNKER Website"

2. Search for any other "VibeHub" references:
   ```bash
   grep -r "VibeHub" --exclude-dir=node_modules --exclude-dir=.git
   ```

3. Update all found instances to "BUNKER"

**Report to Tony**:
- Files changed
- Search results (if additional instances found)
- Ready for commit

---

## Phase 2: GitBook UI/UX Research & Design Planning

### Task 2.1: Current UI Inventory

**Objective**: Document what we have vs what we need.

**Actions**:
1. Review current Astro/Starlight setup:
   - Check `/home/user/ai-learning/src/styles/` for existing custom CSS
   - Review `astro.config.mjs` for Starlight configuration
   - Note current sidebar structure and navigation

2. Create comparison document: `GITBOOK_UI_COMPARISON.md`

**Template for Comparison Doc**:
```markdown
# GitBook UI/UX vs Current Implementation

## Current State (Astro/Starlight)
- Sidebar: [describe current behavior]
- Layout: [columns, spacing]
- Typography: [fonts, sizes]
- Interactions: [what's interactive]

## GitBook 2025 Target
- Sidebar: Collapsible, resizable, light theme, 30% more compact
- Layout: 3-column (nav, content, TOC/comments)
- Typography: Clean, generous spacing, professional
- Interactions: Smooth animations, hover states, inline palette

## Gap Analysis
- Missing: [list features we need to build]
- Have: [list features already implemented]
- Enhance: [list features needing improvement]
```

**Citations**:
- Current styles: `/home/user/ai-learning/src/styles/custom.css`
- Astro config: `/home/user/ai-learning/astro.config.mjs`

---

### Task 2.2: GitBook-Inspired Component Planning

**Objective**: Plan Astro components needed for GitBook-like experience.

**Components to Design** (based on GitBook 2025):

1. **Collapsible Sidebar** (`CollapsibleSidebar.astro`)
   - Resizable via drag
   - Hide/show with button + keyboard shortcut
   - Auto-popup on hover when collapsed
   - Light color scheme, soft shadows
   - Store state in localStorage

2. **Section Upvote Widget** (`SectionUpvote.astro`)
   - Upvote/downvote buttons
   - Vote count display
   - GitHub Discussions backend (via Giscus API)
   - Per-section unique ID
   - Anonymous or authenticated voting

3. **Comment Panel** (`CommentPanel.astro`)
   - Slide-out right panel
   - Giscus integration for comments
   - Threaded discussions
   - Emoji reactions
   - Filter by author

4. **Inline Feedback Widget** (`InlineFeedback.astro`)
   - "Was this helpful?" at section end
   - Thumbs up/down quick actions
   - Optional comment prompt
   - Analytics tracking

**Don't Build Yet** - This is planning only. Create specs/wireframes first.

**Deliverable**: Component specification document for Tony's review.

---

## Phase 3: Community Features Architecture

### Task 3.1: GitHub Discussions Integration (Giscus)

**Objective**: Design how upvoting and commenting will work.

**Research Tasks**:
1. Read Giscus documentation: https://giscus.app/
2. Understand Giscus API for custom components
3. Plan how to map content sections to discussion topics

**Architecture Decisions Needed** (Document, Don't Decide):

**Option A: One Discussion per Page**
- Pros: Simple setup, fewer discussions to manage
- Cons: Can't upvote individual sections, only whole pages

**Option B: One Discussion per Section**
- Pros: Granular upvoting, section-level feedback
- Cons: Many discussions, complex mapping

**Option C: Hybrid (Recommended by Stanley)**
- Page-level discussion for general comments (Giscus default)
- Custom voting API for section-level upvotes (store in discussion reactions)
- "Was this helpful?" widget at section end (local storage + optional submission)

**Unknowns to Clarify with User**:
- Preferred voting granularity (page vs section)?
- Anonymous voting allowed or GitHub auth required?
- Vote count visibility (public numbers or just icons)?
- Moderation workflow for community feedback?

**Deliverable**: Architecture proposal document with options A/B/C detailed.

---

### Task 3.2: Data Storage Strategy

**Objective**: Determine where vote/comment data lives.

**Options to Evaluate**:

**Option 1: GitHub Discussions Only (Free)**
- Use Giscus for everything
- Reactions = votes
- Comments = feedback
- Limitation: Requires GitHub account

**Option 2: GitHub Discussions + LocalStorage Hybrid**
- Anonymous votes stored locally (not persistent)
- Authenticated votes via GitHub
- Aggregate counts shown
- Limitation: Anonymous votes not counted in totals

**Option 3: External Database (Supabase/Firebase)**
- Fully custom voting system
- Anonymous + authenticated support
- Full analytics
- Limitation: Added complexity, potential cost

**Recommendation from Stanley**: Start with Option 1 (GitHub Discussions) for MVP, plan for Option 3 if needed later.

**Document**:
- Pros/cons of each option
- Technical implementation notes
- Migration path if we switch approaches

---

## Phase 4: Implementation Roadmap (Don't Start - Planning Only)

### Stage 1: UI/UX Foundation
- [ ] Implement GitBook-inspired sidebar (collapsible, resizable)
- [ ] Update typography and spacing to match GitBook aesthetic
- [ ] Add smooth animations (Motion library or CSS transitions)
- [ ] Create 3-column responsive layout

### Stage 2: Community Features (MVP)
- [ ] Integrate Giscus for page-level commenting
- [ ] Build section upvote component (GitHub reactions backend)
- [ ] Add "Was this helpful?" inline widgets
- [ ] Implement comment panel slide-out

### Stage 3: Advanced Features
- [ ] Custom vote aggregation and display
- [ ] Search integration (if not using Starlight default)
- [ ] Analytics dashboard for popular sections
- [ ] Moderation tools for community feedback

### Stage 4: Polish & Testing
- [ ] Cross-browser testing
- [ ] Mobile responsiveness
- [ ] Accessibility audit (WCAG 2.1 AA)
- [ ] Performance optimization (Lighthouse score 90+)

**Note**: This roadmap requires user approval before proceeding.

---

## Coordination with Tony

### What Tony Needs to Know

**Enhancements Required** (See TONY_COORDINATION.md):
1. GitHub Discussions enabled on repository
2. Giscus app installed and configured
3. Repository settings for community features
4. Branch protection rules for main/production

### Handoff Protocol

When you complete Phase 1-3 (planning/audit):
1. Create feature branch: `docs/gitbook-hybrid-ui-planning`
2. Commit your planning documents
3. Provide Tony with summary:
   - Files changed (cleanup commits)
   - Planning docs created
   - Unknowns requiring user decision
   - Recommended next steps

**Handoff Template**:
```
## Phase 1-3 Complete: GitBook Hybrid Planning

**Branch**: docs/gitbook-hybrid-ui-planning

**Changes**:
- Cleaned up VibeHub references in book.json
- Created UI comparison document
- Created component specification
- Created architecture proposals

**Unknowns Requiring Decision**:
1. [List specific questions for user]
2. [e.g., "Section-level vs page-level voting?"]
3. [e.g., "Anonymous voting allowed?"]

**Build Status**: ✅ Astro builds successfully
**Tests**: N/A (planning phase)

**Recommended Next Steps**:
1. User reviews planning documents
2. User decides on architecture (Option A/B/C)
3. Tony coordinates GitHub Discussions setup
4. Michael implements Stage 1 (UI/UX foundation)

**Risks**: None identified
**Blockers**: Awaiting user decisions on voting architecture
```

---

## Anti-Hallucination Safeguards

### When Uncertain

**DO**:
- Document the uncertainty clearly
- Provide 2-3 options with pros/cons
- Cite source of information or lack thereof
- Ask specific, targeted questions

**DON'T**:
- Guess at implementation details
- Assume user preferences
- Proceed without clarification
- Invent features or capabilities

### Progress Reporting

**After Each Task**:
- State what was completed
- Show evidence (file paths, command outputs)
- Note any deviations or issues
- Confirm next step before proceeding

**Example**:
```
✅ Task 1.3 Complete: Legacy References Cleanup

Changed files:
- /home/user/ai-learning/book.json (3 lines updated)

Search results:
- Found 0 additional "VibeHub" references outside book.json
- Checked docs/, src/, README files

Build verification:
- npm run build: ✅ Success
- No errors introduced

Next: Task 2.1 - Current UI Inventory
Proceed? (yes/no)
```

---

## Success Criteria (Phase 1-3)

### Phase 1: Foundation ✅
- [ ] Branch confirmed and up to date
- [ ] Astro build passes without errors
- [ ] All "VibeHub" references updated to "BUNKER"
- [ ] Dev server runs successfully

### Phase 2: Planning ✅
- [ ] UI comparison document created
- [ ] Component specifications written
- [ ] Gap analysis documented
- [ ] No code written yet (planning only)

### Phase 3: Architecture ✅
- [ ] Giscus integration researched
- [ ] Data storage options documented
- [ ] Architecture proposals (A/B/C) detailed
- [ ] Unknowns clearly listed for user decision

### Handoff to Tony ✅
- [ ] Clean commit history
- [ ] Planning docs in repository
- [ ] Handoff summary prepared
- [ ] User decisions identified and documented

---

## Files You'll Create (Phase 1-3)

```
.agent-coordination/
├── GITBOOK_UI_COMPARISON.md          (Task 2.1)
├── COMPONENT_SPECIFICATIONS.md       (Task 2.2)
├── COMMUNITY_ARCHITECTURE.md         (Task 3.1)
├── DATA_STORAGE_OPTIONS.md           (Task 3.2)
└── IMPLEMENTATION_ROADMAP.md         (Phase 4 plan)
```

---

## Questions for User (Collect During Phase 1-3)

**UI/UX**:
- Do you want exact GitBook visual clone or "inspired by" with BUNKER identity?
- Which GitBook theme preference: minimal, bold, gradient, or custom?
- Sidebar: Auto-hide on mobile or always visible?

**Community Features**:
- Section-level upvoting or page-level only?
- Anonymous voting allowed or GitHub auth required?
- Comment moderation: Pre-approval or post-moderation?
- Vote counts public or just visual indicators (e.g., "popular")?

**Technical**:
- Preferred animation library: Framer Motion, Motion One, or CSS only?
- Analytics: Google Analytics, Plausible, custom, or none?
- Performance budget: Target Lighthouse score?

**Content**:
- Which cookbook sections get upvoting first (MVP scope)?
- Should votes influence content organization (e.g., "Most Helpful" sort)?

---

## Contact Points

**If Blocked**:
1. Document the blocker with evidence
2. Propose 2-3 solutions with recommendation
3. Report to Tony with: what you need, why, impact of waiting

**If Discover Issues**:
1. Note the issue with file path and line number
2. Assess severity (critical/medium/low)
3. Fix if obvious (e.g., typo), otherwise document and report

**If User Requirements Change**:
1. Stop current work
2. Document what was completed
3. Wait for new instructions via Tony

---

## Final Notes

**Remember**:
- Honesty > optimism (say "I don't know" if uncertain)
- Planning before coding (no implementation in Phase 1-3)
- Evidence-based claims (cite file paths, line numbers)
- User decides architecture (you propose options)

**This is a planning and audit phase**. No UI components should be built yet. Focus on creating thorough documentation that allows informed decision-making.

When planning is complete and user approves an architecture, Tony will coordinate the GitHub setup, and then you'll implement Stage 1.

---

**Stanley (Claude Code) has your back throughout this process.**

End of instructions for Phase 1-3.
