# Decision Log

> **Purpose**: Document significant technical and architectural decisions  
> **Format**: ADR-style (Architecture Decision Records) entries  
> **Owner**: Team/developers making architecture decisions

---

## How to Use This Log

### When to Create an Entry

Create a decision log entry when:
- Choosing between multiple technical approaches
- Making architecture changes that affect future work
- Selecting tools, frameworks, or libraries
- Establishing conventions or standards
- Deciding to deprecate or migrate away from something

### Entry Format

```markdown
## [ID] [Brief Title]

**Date**: YYYY-MM-DD

**Status**: [Proposed | Accepted | Deprecated | Superseded]

**Context**:
What is the issue we're facing? What constraints do we have? What's the background?

**Decision**:
What did we decide to do? Be specific and concrete.

**Rationale**:
Why did we make this decision? What factors influenced it?

**Consequences**:
What are the positive and negative outcomes of this decision?

**Alternatives Considered**:
What other options did we evaluate? Why didn't we choose them?

**Implementation**:
How is this decision being implemented? Links to PRs or issues.

**References**:
Links to documentation, discussions, or external resources.
```

---

## Example Entry

## [001] Use BookGen Instead of Astro for Documentation

**Date**: 2025-11-15

**Status**: Accepted

**Context**:
- The repository contains legacy BookGen assets (.bookgen/, SUMMARY.md, book.json)
- BOOKGEN.md marks it as DEPRECATED in favor of Astro/Starlight
- However, Astro configuration files (package.json, astro.config.mjs) exist but the build is failing
- The active workflow (.github/workflows/deploy-pages.yml) builds an Astro site
- GitHub Pages deployment is currently broken
- Need a reliable deployment path immediately

**Decision**:
Restore BookGen as the primary documentation generator and update the GitHub Actions workflow to use BookGen instead of Astro. Keep Astro files for potential future migration but don't use them now.

**Rationale**:
1. **BookGen is proven and working**: The build script executes successfully and generates complete HTML output
2. **Fast builds**: BookGen builds in ~2 seconds vs. potentially minutes for Node-based tools
3. **Minimal dependencies**: Only requires Python 3.11 and python-markdown
4. **All content is compatible**: SUMMARY.md and markdown files work perfectly with BookGen
5. **No security vulnerabilities**: Simple Python code with minimal dependencies
6. **Deployment urgency**: Need to get Pages working now; Astro migration can happen later

**Consequences**:

*Positive*:
- ✅ Immediate working GitHub Pages deployment
- ✅ Fast, reliable builds
- ✅ Simple troubleshooting (fewer moving parts)
- ✅ Clear path forward (no dependency hell)

*Negative*:
- ⚠️ BookGen is custom code, not a well-known framework
- ⚠️ Future migration to Astro will require separate effort
- ⚠️ May need to maintain BookGen code if bugs are found

*Neutral*:
- 📝 Need to clarify BookGen's status (remove "DEPRECATED" label)
- 📝 Keep Astro files for potential future migration

**Alternatives Considered**:

1. **Fix Astro build**:
   - Pro: Modern framework, better long-term
   - Con: Unknown scope, may take significant effort
   - Con: Adds complexity (Node, npm, many dependencies)
   - Rejected: Need immediate solution, can revisit later

2. **Switch to MkDocs or Docusaurus**:
   - Pro: Well-supported frameworks
   - Con: Requires content restructuring
   - Con: Migration effort with uncertain timeline
   - Rejected: BookGen already works perfectly with existing content

3. **Keep both BookGen and Astro**:
   - Pro: Flexibility
   - Con: Confusion about which is canonical
   - Con: Maintenance burden
   - Rejected: Need one clear deployment path

**Implementation**:
- PR: #[number] - Replace Astro workflow with BookGen workflow
- Updated workflow file: `.github/workflows/deploy-pages.yml`
- Updated documentation: `.github/workflows/README.md`
- Added governance files: `.github/COPILOT_AGENT.md`, `docs/ops/PROGRESS.md`, `docs/ops/DECISIONS.md`

**References**:
- BookGen documentation: `BOOKGEN.md`
- BookGen build script: `.bookgen/build.sh`
- BookGen generator: `.bookgen/generator.py`
- GitHub Actions deploy-pages action: https://github.com/actions/deploy-pages
- GitHub Pages docs: https://docs.github.com/en/pages

---

## Your Entries Below

_(Add new entries above this line, most recent first)_

---

## [XXX] [Title]

**Date**: YYYY-MM-DD

**Status**: [Proposed | Accepted | Deprecated | Superseded]

**Context**:

**Decision**:

**Rationale**:

**Consequences**:

**Alternatives Considered**:

**Implementation**:

**References**:
