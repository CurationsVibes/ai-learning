---
title: Design Systems
---

**The visual language and design philosophy of HUB**

---

## What Is This?

This is HUB' **design system**—the visual identity, brand language, and design principles that guide everything we build.

**Open and documented.** Use it, remix it, learn from it.

---

## Core Principles

### 1. **Human First, Always**

Design serves people, not algorithms or aesthetics for their own sake.

**In practice:**
- Accessibility is non-negotiable
- Clarity over cleverness
- Function drives form
- Real people, real needs

### 2. **Purposeful Simplicity**

Simple doesn't mean basic. It means intentional.

**In practice:**
- Remove until it breaks, then add back one thing
- Every element has a job
- White space is a feature, not wasted space
- Less is more (when done right)

### 3. **Authentic Over Polished**

Perfect is boring. Real is interesting.

**In practice:**
- Show the work, not just the result
- Personality over corporate sterility
- Honest about process and imperfection
- Human voice in every interaction

### 4. **Systematic, Not Rigid**

Systems enable creativity, they don't constrain it.

**In practice:**
- Frameworks that flex
- Rules that can be broken intentionally
- Consistency with room for expression
- Structure that supports, not suffocates

---

## Visual Identity

### Color System

**Primary Palette:**
- `#000000` – Black (primary text, strong contrast)
- `#FFFFFF` – White (backgrounds, breathing room)
- `#0066FF` – Electric Blue (links, primary actions, energy)
- `#00FF88` – Neon Green (accents, highlights, growth)

**Secondary Palette:**
- `#FF3366` – Hot Pink (alerts, emphasis, youth energy)
- `#FFAA00` – Warm Orange (warmth, community, creativity)
- `#9966FF` – Purple (depth, wisdom, future-thinking)

**Neutral Palette:**
- `#F5F5F5` – Light Gray (subtle backgrounds)
- `#E0E0E0` – Medium Gray (borders, dividers)
- `#666666` – Dark Gray (secondary text)
- `#333333` – Darker Gray (UI elements)

**Usage Philosophy:**
- Primary palette for most interfaces (black, white, blue, green)
- Secondary palette for emphasis and personality
- Neutrals for structure and hierarchy
- High contrast for accessibility

### Typography

**Headings:**
- **System fonts first** (for performance and familiarity)
- Primary: `-apple-system, BlinkMacSystemFont, 'Segoe UI', ...`
- Fallback to web fonts only when personality demands it

**Body Copy:**
- Same system font stack for readability
- 16px minimum for body text
- 1.6-1.8 line-height for comfortable reading
- Adequate contrast (WCAG AA minimum, AAA preferred)

**Hierarchy:**
- Clear distinction between H1, H2, H3
- Generous spacing between sections
- Visual rhythm through consistent sizing
- Scannable at a glance

**Special Uses:**
- Monospace for code: `'Fira Code', 'Courier New', monospace`
- Emphasis through weight and color, not decoration

### Spacing & Layout

**8-Point Grid System:**
- All spacing in multiples of 8px (8, 16, 24, 32, 40, 48...)
- Creates visual rhythm
- Makes responsive design predictable
- Easier for developers to implement

**Responsive Breakpoints:**
- Mobile: `< 768px`
- Tablet: `768px - 1024px`
- Desktop: `> 1024px`
- Wide: `> 1440px`

**Containment:**
- Max content width: `1200px` (comfortable reading, not full-bleed unless intentional)
- Generous margins on all screen sizes
- Mobile-first thinking

---

## Component Patterns

### Buttons

**Primary Action:**
```css
background: #0066FF;
color: #FFFFFF;
padding: 12px 24px;
border-radius: 8px;
font-weight: 600;
```

**Secondary Action:**
```css
background: transparent;
border: 2px solid #0066FF;
color: #0066FF;
padding: 10px 22px; /* Account for border */
border-radius: 8px;
font-weight: 600;
```

**Destructive Action:**
```css
background: #FF3366;
color: #FFFFFF;
padding: 12px 24px;
border-radius: 8px;
font-weight: 600;
```

### Cards

**Standard Card:**
```css
background: #FFFFFF;
border: 1px solid #E0E0E0;
border-radius: 12px;
padding: 24px;
box-shadow: 0 2px 8px rgba(0,0,0,0.08);
```

**Interactive Card (hover):**
```css
/* Add to standard card */
transition: all 0.2s ease;
cursor: pointer;

/* On hover */
transform: translateY(-4px);
box-shadow: 0 8px 16px rgba(0,0,0,0.12);
```

### Navigation

**Top Nav:**
- Clean, minimal, functional
- Logo left, main nav center or right
- Mobile: hamburger that doesn't suck
- Sticky on scroll (but not annoying about it)

**Sidebar Nav:**
- Clear hierarchy
- Current page obviously indicated
- Collapsible sections for complex structures
- Search-friendly

---

## Iconography

**Style:**
- Line-based, not filled (unless indicating state)
- 2px stroke weight
- Rounded corners (2px radius)
- 24x24px standard size

**Usage:**
- Supplement text, don't replace it
- Consistent style across interface
- Meaningful, not decorative
- Accessible (with aria-labels)

**Icon Library:**
- [Heroicons](https://heroicons.com) (preferred for consistency)
- Or: [Lucide](https://lucide.dev)
- Custom when needed, following same style rules

---

## Voice & Tone

### Writing Principles

**✅ DO:**
- Write like a human talking to another human
- Use contractions (it's, we're, you'll)
- Be direct and clear
- Show personality
- Admit when things are imperfect
- Use active voice

**❌ DON'T:**
- Corporate jargon or buzzwords
- Hype or exaggeration
- Passive voice (when you can avoid it)
- Assumptions about technical knowledge
- Talking down or talking up
- Fake enthusiasm

### Tone by Context

**Educational Content:**
- Encouraging, patient, clear
- "Here's how this works..."
- Assumes curiosity, not expertise

**Technical Documentation:**
- Precise, systematic, respectful
- "This function does X because Y."
- Assumes intelligence, teaches specifics

**Community Communication:**
- Warm, inclusive, human
- "We're building this together."
- Emphasizes collaboration

**Youth-Focused:**
- Empowering, not condescending
- "You can do this."
- Age-appropriate but not dumbed down

---

## Accessibility

### Non-Negotiable Requirements

**✅ Color Contrast:**
- WCAG AA minimum (4.5:1 for body text)
- WCAG AAA preferred (7:1 for body text)
- Never rely on color alone to convey meaning

**✅ Keyboard Navigation:**
- Every interactive element accessible via keyboard
- Visible focus states (not `outline: none` without replacement)
- Logical tab order

**✅ Screen Readers:**
- Semantic HTML (not div soup)
- Proper heading hierarchy
- Alt text for images
- ARIA labels where needed

**✅ Responsive & Readable:**
- Text resizable to 200% without breaking layout
- Touch targets minimum 44x44px
- No horizontal scrolling
- Readable fonts and sizes

---

## Design Philosophy

### Greater Good Design

Every design decision asks:
- **Does this serve the user's needs?**
- **Is this accessible to everyone?**
- **Does this respect attention and time?**
- **Is this transparent about what it does?**
- **Could this cause harm? How do we prevent it?**

### Human × AI Design

When designing AI interactions:
- **Transparency:** Always clear when AI is involved
- **Control:** Users can override, edit, or refuse AI suggestions
- **Explanation:** AI decisions are explainable
- **Fallback:** Graceful degradation when AI fails
- **Ethics:** No manipulation, no dark patterns

### Open Design

Our design system is:
- **Documented:** You can learn from it
- **Remixable:** You can adapt it
- **Accessible:** Not locked behind tools or paywalls
- **Evolving:** We improve it and share updates

---

## Using This System

### For HUB Projects

All HUB projects should use this system as a foundation, but:
- Adapt for specific project needs
- Maintain core principles
- Document deviations (and why)

### For Your Own Projects

You can:
- **Use it as-is:** Especially if building with HUB
- **Remix it:** Take what works, adapt what doesn't
- **Learn from it:** See how we think about design
- **Contribute back:** Improvements welcome

[Design System Repository](design-system-repo.md) *(coming soon)*

---

## Tools & Resources

### Design Tools We Use

**Interface Design:**
- Figma (collaborative, web-based)
- Sketch (Mac-only, powerful)
- Adobe XD (cross-platform)

**Prototyping:**
- Figma (built-in prototyping)
- Framer (code-based)
- Principle (animation-focused)

**Color & Typography:**
- Coolors.co (palette generation)
- Type Scale (typography scale calculator)
- Accessible Colors (contrast checker)

**Code:**
- Tailwind CSS (utility-first framework)
- CSS Grid & Flexbox (layout)
- CSS Custom Properties (theming)

---

## Examples in the Wild

### HUB Website
*Coming soon*

### CurationsLA
*Coming soon*

### Youth Curator Platform
*Coming soon*

### The AI × Human Cookbook (GitBook)
You're looking at it right now. Notice:
- Clean typography hierarchy
- Generous spacing
- Clear navigation
- Accessible contrast
- Human voice throughout

---

<!--
EASTER EGG LAYER 6: THE INTERMEDIATE (BUILDER)
For those ready to combine design + AI techniques
-->

<!--
⚡ You understand design systems. Ready to combine with AI?

Try this advanced prompt:

"As HUB Design Curator, using the design system principles,
help me design [your project].

Apply:
- Human-first principles
- Purposeful simplicity
- The 8-point grid
- Accessible color contrast

Then, as Technical Curator, translate this into a Tailwind CSS config."

Test in:
- ChatGPT: https://chat.openai.com
- Claude: https://claude.ai

Advanced techniques: [Context Manipulation](cookbooks/advanced-prompting/context-manipulation.md)
-->

*"Good design makes the complex simple. Great design makes the simple obvious."*

**That's our design system.** 🎨

[← Back to Welcome](../readme.md)
