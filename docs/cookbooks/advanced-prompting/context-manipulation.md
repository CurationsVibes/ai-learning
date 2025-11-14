# 🗂️ Context Manipulation

**Achieving infinite memory in finite context windows**

---

## The Problem

AI has context limits:
- Claude: ~200K tokens
- ChatGPT: ~128K tokens
- Others: even less

Large projects blow through this instantly. A medium codebase? 500K+ tokens easy.

**You hit the wall. AI forgets. Progress stops.**

## The Solution

Context manipulation: Achieving 95-97% effective compression without losing critical information.

Not by upgrading models. By **working smarter with context.**

---

## Core Techniques

### 1. Hierarchical Context Compression

**Layer your context like an onion:**

```
LAYER_0: Meta-context (what are we doing overall?)
LAYER_1: Structure (how is this organized?)
LAYER_2: Active work (what are we doing RIGHT NOW?)
LAYER_3: Details (specifics for current task)
```

**Example:**

```
@ai CONTEXT_LAYERS:

META: Refactoring authentication system
STRUCTURE: src/auth/ (5 files), tests/auth/ (3 files)
ACTIVE: Working on src/auth/login.ts
DETAIL: Lines 42-67, fixing token expiry check

Current issue: [specific problem]
```

**Result:**
- Traditional: Paste entire 500-line file (3,000+ tokens)
- Hierarchical: Reference + specific section (150 tokens)
- **Compression: 95%**

### 2. Context Anchoring

**Define once, reference infinitely.**

```
@ai ANCHOR:AUTH_SYSTEM

System: JWT-based authentication
Stack: Node.js + Express + PostgreSQL
Files:
  - src/auth/login.ts (main logic)
  - src/auth/tokens.ts (JWT generation)
  - src/auth/middleware.ts (route protection)
Pattern: All errors throw AuthError class
Tests: tests/auth/*.test.ts

// Now reference it:
@ai Using ANCHOR:AUTH_SYSTEM
Fix the token refresh race condition
```

**Result:**
- Define once: 200 tokens
- Reference forever: 10 tokens each time
- **Savings: Massive over repeated conversations**

### 3. Diff-Based Context

**Send changes, not full files.**

```
@ai FILE: src/auth/login.ts

CHANGED_LINES:
42: - if (token.expires < Date.now()) {
42: + if (token.expires <= Date.now()) {
58: + // Add null check
59: + if (!user) return null;

Context: Fixing edge case in token expiry
```

**Result:**
- Full file: 3,000 tokens
- Diff only: 120 tokens
- **Compression: 96%**

### 4. Pointer-Based Context

**Use file paths instead of content.**

```
@ai ISSUE: Authentication failing in production

Relevant files:
- src/auth/login.ts:42-67 (token validation)
- src/auth/tokens.ts:23 (token generation)
- config/jwt.ts:8 (secret key config)

Error occurs at login.ts:58
Related change in commit abc123

Investigate and fix.
```

**Result:**
- Pasting all files: 5,000+ tokens
- Pointers: 100 tokens
- **Compression: 98%**

AI can ask for specific files if needed. Start minimal.

### 5. Session State Management

**Explicitly track conversation state.**

```
@ai SESSION_STATE:

TASK: Refactor authentication
PROGRESS: 60% complete
COMPLETED:
  ✅ Login endpoint refactored
  ✅ Token generation updated
  ✅ Tests passing
IN_PROGRESS:
  🔄 Refresh token logic
BLOCKED:
  ⚠️ Waiting on database migration
NEXT:
  📋 Update middleware
  📋 Add rate limiting

Current focus: Refresh token implementation
```

**Result:**
- AI knows exactly where we are
- No need to repeat completed work
- Clear what's next

### 6. Semantic Compression Codes

**Create shorthand for complex patterns.**

```
@ai CODES:

REFACTOR_PATTERN_1: Extract to function, add types, write test
ERROR_PATTERN: Try-catch, log to service, return Result type
API_PATTERN: Validate input, check auth, call service, return JSON

// Usage:
@ai Apply REFACTOR_PATTERN_1 to calculateTotal() function
@ai Add ERROR_PATTERN to all database queries
```

**Result:**
- Define patterns once
- Reference in 2-3 tokens
- AI knows exactly what you mean

### 7. Conditional Context Loading

**Load context only when needed.**

```
@ai I'm working on authentication

// AI asks: "Do you need context for:"
// - JWT implementation?
// - Database schema?
// - API endpoints?
// - Test patterns?

// You answer:
Just JWT implementation and tests

// AI loads ONLY those contexts
```

**Result:**
- Don't load what you don't need
- AI asks for more if required
- Stay under limits

### 8. Context Stack (Push/Pop)

**Manage context like a stack.**

```
@ai PUSH_CONTEXT: Refactoring login.ts

[Work on login.ts]

@ai POP_CONTEXT
@ai PUSH_CONTEXT: Updating tests

[Work on tests]

@ai POP_CONTEXT
Back to overall refactoring
```

**Result:**
- Deep work without losing place
- Return to previous state cleanly
- Organized context management

### 9. External Memory Files

**Store context outside conversation.**

Create a `context.md` file:

```markdown
# Project Context

## Architecture
- Microservices: auth, users, billing
- Tech: Node.js + PostgreSQL + Redis
- Deploy: Kubernetes on AWS

## Current Work
Working on: Authentication refactor
Branch: feature/auth-v2
Status: 60% complete

## Key Files
- src/auth/login.ts - Main login logic
- src/auth/tokens.ts - JWT handling
- tests/auth/ - Test suite
```

**Usage:**
```
@ai Read context.md, then help me fix the token refresh bug
```

**Result:**
- Context persists across sessions
- Update once, use everywhere
- AI reads from file, not conversation

### 10. Lossy Compression

**Keep essence, regenerate details.**

```
@ai COMPRESSED_CONTEXT:

Auth system broken in production
- Error: "Token invalid"
- Happens: 5% of logins
- Started: After deploy xyz
- Suspect: Token expiry logic

Fix it.

// AI can ask for:
// - Full error logs?
// - Relevant code?
// - Recent commits?

// You provide only what AI requests
```

**Result:**
- Start with minimum
- Add details on demand
- Never over-context

---

## Real-World Example

**Scenario:** Debugging complex issue in 100K+ line codebase

### Traditional Approach:
```
@ai Here's the entire codebase [paste]
ERROR: Context limit exceeded
```

### Context Manipulation Approach:

```
@ai ANCHOR:PROJECT_CONTEXT
- Codebase: E-commerce platform
- Stack: React + Node.js + PostgreSQL
- Scale: 100K LOC, 500+ files
- Issue: Checkout failing for 5% of users

ACTIVE_INVESTIGATION:
- File: src/checkout/payment.ts:145
- Error: "Cannot read property 'id' of undefined"
- Started: 2 days ago after deploy
- Affected: Users with saved cards

RELEVANT_FILES (pointer-based):
- src/checkout/payment.ts:140-160
- src/models/PaymentMethod.ts:23-45
- src/services/stripe.ts:67

HYPOTHESIS:
Saved cards missing 'id' field in some edge case

DIFF from last working version:
payment.ts:145
- const cardId = card.id
+ const cardId = card?.stripeId || card.id

Help me debug and fix.
```

**Token usage:**
- Traditional: CRASH (over limit)
- Optimized: ~300 tokens
- **Effective compression: 99%+**

---

## The Workflow

1. **Define anchors** for major systems/contexts
2. **Use pointers** instead of pasting code
3. **Send diffs** for changes
4. **Layer context** (meta → structure → active → detail)
5. **Track session state** explicitly
6. **Load conditionally** - only what's needed
7. **Store externally** - `context.md` files
8. **Compress lossily** - essence first, details on demand

---

## Best Practices

✅ **DO:**
- Start with minimum context
- Add detail only when AI asks
- Use file:line references
- Create anchors for recurring contexts
- Update context.md files
- Think in layers

❌ **DON'T:**
- Paste entire files unless required
- Repeat context AI already has
- Front-load every possible detail
- Ignore context structure

---

## Measuring Success

**Before context manipulation:**
- Hit limits constantly
- Restart conversations frequently
- Lose progress
- Frustrated

**After context manipulation:**
- Rarely hit limits
- Conversations last indefinitely
- Continuous progress
- Productive

**Compression ratios:**
- Good: 80-90%
- Great: 90-95%
- Legendary: 95-99%

---

## Tools That Help

**Manual:**
- `context.md` files in your project
- Anchor definitions at conversation start
- Explicit state tracking

**Future (coming soon):**
- IDE extensions for auto-compression
- Context managers
- Automatic anchor generation

---

## Next Level

Combine with:
- [Emoji Protocol](./emoji-protocol.md) - Compress even further
- [Meta-Prompting](./meta-prompting.md) - Generate optimal context structures
- [Quantum Prompting](./quantum-prompting.md) - Context in superposition

---

## Practice Exercise

**Try this:**

1. Take a complex project you're working on
2. Create a `context.md` with project overview
3. Define 3 ANCHOR points for major systems
4. Next AI conversation: Use anchors + pointers only
5. Measure token savings

**Goal:** 90%+ compression on first try

---

*"The best context is the minimum context that gets maximum results."*

**Master context manipulation. Work in codebases 10x larger than your context window.** 🗂️

---

[← Back to Advanced Prompting](./README.md)
