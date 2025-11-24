---
title: 🎯 Advanced Prompting Techniques
description: Master chain-of-thought, few-shot learning, and structured outputs for better AI results
---

**Level up your prompting skills with proven advanced techniques**

## 🌱 What You'll Learn

This guide covers professional-grade prompting techniques:
- Chain-of-thought reasoning
- Few-shot learning examples
- Structured output formats
- Prompt chaining
- Meta-prompting basics

---

## 🧠 Chain-of-Thought (CoT) Prompting

### What It Is

Chain-of-thought prompting guides the AI through step-by-step reasoning before answering. This improves accuracy on complex problems.

### Basic Pattern

```
Solve this problem step by step:
[YOUR PROBLEM]

Think through:
1. What information do I have?
2. What approach should I use?
3. Work through each step
4. Verify the answer makes sense
```

### Example: Complex Calculation

```
Calculate the monthly payment for a $300,000 mortgage at 6.5% interest over 30 years.

Think through:
1. Identify the formula needed (monthly payment formula)
2. Convert annual rate to monthly: 6.5% / 12 = 0.542% per month
3. Convert rate to decimal: 0.00542
4. Calculate number of payments: 30 years × 12 = 360 months
5. Apply formula: M = P[r(1+r)^n]/[(1+r)^n-1]
6. Show your work step by step
7. Verify answer is reasonable ($300K over 30 years should be ~$2000/month range)

Now calculate and show each step.
```

### 💡 When to Use CoT

✅ **Use for:**
- Math problems
- Logic puzzles
- Multi-step analysis
- Complex reasoning
- Fact-checking

❌ **Skip for:**
- Simple questions
- Creative writing
- Quick lookups
- Brainstorming

---

## 📝 Few-Shot Learning

### What It Is

Provide 2-5 examples of what you want, then the AI follows the pattern for new inputs.

### Basic Pattern

```
I'll show you examples, then you do the same for my input.

Example 1:
Input: [example input]
Output: [example output]

Example 2:
Input: [example input]
Output: [example output]

Example 3:
Input: [example input]
Output: [example output]

Now do this for:
Input: [your actual input]
Output: ?
```

### Example: Data Formatting

```
Format customer data into this structure. Here are examples:

Example 1:
Input: "John Smith, email: john@email.com, purchased: laptop"
Output: {name: "John Smith", contact: "john@email.com", item: "laptop", status: "customer"}

Example 2:
Input: "Sarah Lee, phone: 555-1234, inquired about: tablets"
Output: {name: "Sarah Lee", contact: "555-1234", item: "tablets", status: "lead"}

Example 3:
Input: "Mike Chen, email: mike@test.com, returned: headphones"
Output: {name: "Mike Chen", contact: "mike@test.com", item: "headphones", status: "return"}

Now format:
Input: "Amy Davis, phone: 555-9876, purchased: keyboard"
Output: ?
```

### 💡 Few-Shot Best Practices

1. **Use diverse examples** - Cover edge cases
2. **Keep consistent format** - Make pattern clear
3. **Include 3-5 examples** - 2 is minimum, 5+ is often overkill
4. **Show variations** - Different inputs, same output format
5. **Label clearly** - Make input/output obvious

---

## 📊 Structured Output Formats

### JSON Output

```
Provide your answer as valid JSON with this structure:
{
  "summary": "brief overview",
  "key_points": ["point 1", "point 2", "point 3"],
  "recommendations": ["rec 1", "rec 2"],
  "confidence": "high/medium/low",
  "sources": ["source 1", "source 2"]
}

Question: [YOUR QUESTION]
```

### Table Format

```
Organize the information in a markdown table with these columns:
| Feature | Option A | Option B | Option C | Winner |

Include:
- 5-7 key comparison features
- Objective ratings
- Brief explanations
- Clear recommendation in "Winner" column

Compare: [YOUR COMPARISON REQUEST]
```

### List Format

```
Provide your answer as a prioritized list:

Format:
1. [ITEM] - Priority: High/Medium/Low
   - Why: [reason]
   - Action: [what to do]
   - Timeline: [when]

2. [ITEM] - Priority: High/Medium/Low
   ...

Request: [YOUR REQUEST]
```

---

## 🔗 Prompt Chaining

### What It Is

Break complex tasks into multiple prompts, using output from one as input to the next.

### Pattern

```
Step 1: Research Phase
"List the top 5 approaches to [PROBLEM]. For each:
- Core concept
- Pros and cons
- Best use case"

[Take output, analyze, then:]

Step 2: Selection Phase
"Based on this analysis: [PASTE STEP 1 OUTPUT]

Recommend the best approach for my specific situation:
- [Constraint 1]
- [Constraint 2]
- [Goal]"

[Take recommendation, then:]

Step 3: Implementation Phase
"Create a detailed implementation plan for [SELECTED APPROACH].
Include:
- Step-by-step actions
- Timeline
- Resources needed
- Success metrics"
```

### Example: Content Strategy

```
Prompt 1: "Analyze these 3 blog posts and extract:
- Target audience
- Writing style
- Key themes
- Engagement tactics
[PASTE POSTS]"

Prompt 2: "Using this analysis [PASTE RESULTS], create:
- Content calendar for next month
- 10 blog post titles matching this style
- Optimal posting schedule"

Prompt 3: "Take the top 3 titles and create:
- Full outlines
- SEO keywords
- Meta descriptions"
```

---

## 🎭 Role-Based Prompting

### Assign Expertise

```
You are a [SPECIFIC EXPERT] with [X YEARS] experience in [DOMAIN].

Your expertise includes:
- [Skill 1]
- [Skill 2]
- [Skill 3]

Approach: [analytical/creative/practical]
Tone: [professional/casual/technical]

Now help me with: [YOUR REQUEST]
```

### Example Roles

**Data Analyst:**
```
You are a senior data analyst with 10 years in e-commerce analytics.
You specialize in conversion optimization and A/B testing.
You communicate insights clearly for non-technical stakeholders.

Analyze this data: [DATA]
Provide: insights, recommendations, and next steps.
```

**Content Strategist:**
```
You are a content strategist for B2B SaaS companies.
You focus on thought leadership and SEO-driven content.
Your recommendations are data-backed and actionable.

Create a content strategy for: [COMPANY/PRODUCT]
```

---

## ⚡ Power Techniques

### Negative Prompting

Tell the AI what NOT to do:

```
Write a product description for [PRODUCT].

Do:
- Focus on benefits, not just features
- Use specific numbers and data
- Include customer pain points
- Keep it scannable

Don't:
- Use hype or exaggeration
- Include technical jargon
- Make it longer than 150 words
- Use passive voice
```

### Constraint-Based Prompting

Add specific constraints for better control:

```
Write a blog intro about [TOPIC].

Constraints:
- Exactly 3 sentences
- First sentence must be a question
- Include the word "proven" once
- Reading level: 8th grade
- Hook must relate to reader's pain point
```

### Iterative Refinement

```
First Draft:
"Write [REQUEST]"

[Review output]

Refinement 1:
"Revise the above to:
- Make it 30% shorter
- Add more specific examples
- Strengthen the conclusion"

[Review again]

Refinement 2:
"Final polish:
- Improve headline
- Add transition sentences
- Ensure consistent tone"
```

---

## 🔬 Advanced Patterns

### Meta-Prompting Preview

```
Before you answer my question, tell me:
1. What approach will you use?
2. What assumptions are you making?
3. What information might be missing?
4. What's your confidence level?

Then answer: [YOUR QUESTION]
```

### Self-Correction

```
Answer this question: [QUESTION]

After answering:
1. Identify any assumptions you made
2. Point out potential weaknesses in your answer
3. Suggest what additional information would improve it
4. Rate your confidence: high/medium/low
```

---

## 📚 Practice Exercises

### Exercise 1: Chain-of-Thought

Take this simple question and turn it into a CoT prompt:
"Which smartphone should I buy?"

### Exercise 2: Few-Shot

Create a few-shot prompt to format addresses consistently.

### Exercise 3: Structured Output

Design a JSON schema for book recommendations that includes:
- Title, author, genre
- Why it's recommended
- Similar books
- Where to buy

---

## 🎯 When to Use What

**Quick Answer Needed:**
- Simple, direct prompt

**Complex Problem:**
- Chain-of-thought

**Consistent Format:**
- Few-shot learning

**Integration with Code:**
- Structured output (JSON)

**Multi-Step Task:**
- Prompt chaining

**Specialized Domain:**
- Role-based prompting

---

## 💡 Pro Tips

1. **Save successful prompts** - Build a personal library
2. **Test variations** - Small changes can have big effects
3. **Combine techniques** - Use CoT + structured output together
4. **Iterate quickly** - Don't overthink, just try it
5. **Document what works** - Note context and results

---

## 📚 Related Guides

**Next Level:**
- [Advanced Prompting](/cookbooks/advanced-prompting/) - Meta-prompting, quantum techniques
- [Foundations: Memory](/cookbooks/foundations/03-memory-management/) - Context management

**Apply This:**
- [Business Applications](/cookbooks/business/) - Use advanced prompting for brand work
- [Personal Use](/cookbooks/personal-use/) - Apply to daily tasks

---

*Part of the Intermediate AI Mastery Cookbook - CURATOR HUB by CURATIONS*

[← Back to Intermediate](./)
