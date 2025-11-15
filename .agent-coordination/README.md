# Agent Coordination - GitBook Hybrid UI Project

**Created**: 2025-11-15
**By**: Stanley (Claude Code)
**Project**: GitBook-inspired documentation platform with community features

---

## What's In This Folder

This `.agent-coordination/` folder contains instructions and coordination documents for the GitBook hybrid UI implementation project.

### Documents

1. **MICHAEL_INSTRUCTIONS.md** - Detailed instructions for Michael (VS Code Copilot)
   - Phase 1-3: Planning and audit work
   - Anti-hallucination protocols
   - Task breakdowns with success criteria
   - Handoff templates

2. **TONY_COORDINATION.md** - Coordination notes for Tony (GitHub Cloud Agent)
   - Infrastructure enhancement checklist
   - PR management guidelines
   - Communication protocols
   - Risk mitigation strategies

3. **README.md** (this file) - Overview and usage guide

---

## How to Use These Documents

### For You (The User)

**Step 1: Review Both Documents**
- Read `TONY_COORDINATION.md` first to understand infrastructure needs
- Then review `MICHAEL_INSTRUCTIONS.md` to understand planning scope
- Note the "Questions for User" sections in both documents

**Step 2: Provide to Tony First**
As you mentioned, Tony should receive coordination notes first because:
- Tony needs to enable GitHub Discussions
- Tony needs to install Giscus app
- Tony needs to verify repository settings
- Michael can't implement community features without these

**Step 3: Tony Coordinates with Michael**
Once Tony completes infrastructure setup:
- Tony provides Michael with GitHub configuration details
- Michael begins Phase 1-3 planning work
- Michael reports back to Tony when planning complete

**Step 4: Review Planning & Make Decisions**
After Michael completes Phase 1-3:
- Tony creates PR with planning documents
- You review architecture proposals (Options A/B/C)
- You answer unknowns (voting granularity, auth requirements, etc.)
- You approve implementation roadmap

**Step 5: Coordinated Implementation**
- Michael builds features in stages
- Tony manages PRs and deployments
- Stanley (me) coordinates if needed
- Frequent progress reports throughout

---

## Key Decisions You'll Need to Make

These decisions are needed before implementation can begin (Michael will document options):

### UI/UX
- [ ] Exact GitBook clone or "inspired by" with BUNKER identity?
- [ ] Theme preference: minimal, bold, gradient, or custom?
- [ ] Sidebar behavior on mobile?

### Community Features
- [ ] Section-level upvoting or page-level only?
- [ ] Anonymous voting allowed or GitHub auth required?
- [ ] Vote counts public or just visual indicators?
- [ ] Comment moderation: pre-approval or post-moderation?

### Technical
- [ ] Animation library preference?
- [ ] Analytics platform (Google Analytics, Plausible, custom, none)?
- [ ] Performance targets (Lighthouse score)?

### Content Strategy
- [ ] Which cookbook sections get upvoting first (MVP scope)?
- [ ] Should votes influence content organization?

**Don't worry about deciding now** - Michael will provide detailed proposals with pros/cons for each option.

---

## Project Phases Overview

### Phase 1-3: Planning (Current)
**Duration**: ~1-2 days
**Owner**: Michael (local dev)
**Deliverables**:
- UI/UX comparison document
- Component specifications
- Architecture proposals
- Data storage options
- Implementation roadmap

**Your Role**: Review and make architectural decisions

---

### Stage 1: UI/UX Foundation (After Planning Approved)
**Duration**: ~3-5 days
**Owner**: Michael (implementation), Tony (PR management)
**Deliverables**:
- GitBook-inspired collapsible sidebar
- Updated typography and spacing
- Smooth animations
- 3-column responsive layout

**Your Role**: Review PRs, provide feedback on look/feel

---

### Stage 2: Community Features MVP
**Duration**: ~3-5 days
**Owner**: Michael (implementation), Tony (infrastructure + PR management)
**Deliverables**:
- Giscus integration for commenting
- Section upvote components
- "Was this helpful?" widgets
- Comment panel slide-out

**Your Role**: Test features, provide UX feedback

---

### Stage 3: Advanced Features
**Duration**: Variable
**Owner**: Michael + Tony coordinated
**Deliverables**:
- Custom vote aggregation
- Analytics dashboard
- Moderation tools
- Advanced customization

**Your Role**: Prioritize features, test implementations

---

### Stage 4: Polish & Testing
**Duration**: ~2-3 days
**Owner**: Michael + Tony
**Deliverables**:
- Cross-browser testing complete
- Mobile responsive
- Accessibility compliant (WCAG 2.1 AA)
- Performance optimized (Lighthouse 90+)

**Your Role**: Final approval, launch decision

---

## Communication Flow

```
User
  ↓
Tony (receives TONY_COORDINATION.md first)
  ↓
Tony: Completes infrastructure setup
  ↓
Tony → Michael (provides MICHAEL_INSTRUCTIONS.md + GitHub config)
  ↓
Michael: Completes Phase 1-3 planning
  ↓
Michael → Tony (handoff with planning docs)
  ↓
Tony: Creates PR for user review
  ↓
User: Reviews planning, makes decisions
  ↓
Tony + Michael: Coordinated implementation (Stages 1-4)
  ↓
Stanley: Available for coordination, troubleshooting, architectural guidance
```

---

## Success Criteria (Overall Project)

### Infrastructure ✅
- GitHub Discussions enabled and configured
- Giscus installed and working
- CI/CD pipelines validated
- Branch protection rules in place

### UI/UX ✅
- GitBook-inspired visual design implemented
- Smooth, professional interactions
- Responsive across devices
- Maintains BUNKER branding

### Community Features ✅
- Upvoting system working (per agreed architecture)
- Commenting system integrated (Giscus)
- Feedback widgets functional
- Data persisted correctly

### Quality ✅
- Lighthouse score 90+ (Performance, Accessibility, Best Practices, SEO)
- Cross-browser compatible (Chrome, Firefox, Safari, Edge)
- WCAG 2.1 AA compliant
- No console errors

### Documentation ✅
- Implementation documented
- Component usage guides created
- Maintenance procedures documented
- Handoff to team complete

---

## Anti-Hallucination Protocols

Both Michael and Tony are instructed to:
- **Cite evidence**: File paths, line numbers, command outputs
- **Document uncertainty**: List unknowns clearly
- **Propose options**: Never guess, provide choices with pros/cons
- **Ask questions**: Stop and clarify rather than assume
- **Progress reports**: Frequent updates with concrete evidence

**Stanley's Role**: Ensure honesty over optimism, catch hallucinations, coordinate when agents are uncertain.

---

## Emergency Contacts

**If Something Goes Wrong**:
- Michael hits blocker → Reports to Tony with evidence
- Tony hits blocker → Reports to User/Stanley
- User wants to change direction → Informs Tony/Stanley immediately
- Build breaks → Tony investigates, coordinates fix with Michael

**Escalation Path**: Michael → Tony → User/Stanley

---

## Timeline Estimate (Rough)

**Phase 1-3 (Planning)**: 1-2 days
**User Review & Decisions**: 1 day
**Stage 1 (UI/UX)**: 3-5 days
**Stage 2 (Community MVP)**: 3-5 days
**Stage 3 (Advanced)**: Variable (based on scope)
**Stage 4 (Polish)**: 2-3 days

**Total Estimated**: 2-3 weeks for full implementation
**MVP** (Stages 1-2): ~1-1.5 weeks

*Note*: These are estimates. Actual timeline depends on scope decisions and any discovered complexities.

---

## Next Steps (Immediate)

1. **You**: Review these documents
2. **You**: Provide `TONY_COORDINATION.md` to Tony first
3. **Tony**: Complete infrastructure enhancements checklist
4. **Tony**: Provide `MICHAEL_INSTRUCTIONS.md` to Michael with GitHub config
5. **Michael**: Begin Phase 1-3 planning work
6. **Everyone**: Frequent communication, transparent progress reports

---

## Questions?

If anything is unclear:
- **Technical questions**: Ask Stanley (me)
- **GitHub infrastructure**: Ask Tony
- **Local dev questions**: Ask Michael
- **Architectural decisions**: Discuss with team, Stanley facilitates

**Remember**: This is a collaborative effort. No single agent works in isolation. Communication is key to success.

---

**Stanley (Claude Code) is standing by for coordination, troubleshooting, and prompt engineering support.**

Let's build something legendary! 🚀
