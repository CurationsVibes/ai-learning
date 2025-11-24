---
title: "🎓 Defining LLM Agents: A Step-by-Step Guide"
---

## 🌳 Flourishing Concept

**Label**: Bringing It All Together

Creating an effective LLM agent requires three fundamental steps: defining the agent's role, providing clear instructions, and equipping it with the right tools. This guide shows you how to combine everything you've learned into production-ready agents.

## The Three-Step Framework

```
┌────────────────────────────────────────────┐
│     Step 1: Define the Agent's Role       │
│     - Name (required)                      │
│     - Description (recommended)            │
│     - Model (required)                     │
└────────────────────────────────────────────┘
                    ↓
┌────────────────────────────────────────────┐
│  Step 2: Guide with Instructions           │
│  - Core task and purpose                   │
│  - Persona and tone                        │
│  - Constraints and rules                   │
│  - Tool usage guidance                     │
└────────────────────────────────────────────┘
                    ↓
┌────────────────────────────────────────────┐
│     Step 3: Equip with Tools               │
│     - Information retrieval                │
│     - Action capabilities                  │
│     - Integration functions                │
└────────────────────────────────────────────┘
```

## 💡 Step 1: Define the Agent's Role

### Essential Components

```python
from adk import Agent

# Minimal agent definition
agent = Agent(
    name="CustomerSupportAgent",           # Required: Clear, descriptive name
    description="Handles customer inquiries", # Recommended: High-level purpose
    model="gpt-4"                          # Required: LLM to use
)
```

### Choosing the Right Model

```python
# Task complexity determines model choice

# Simple, fast responses
quick_agent = Agent(
    name="GreetingBot",
    model="gpt-3.5-turbo",  # Fast and cost-effective
    temperature=0.7
)

# Complex reasoning required
expert_agent = Agent(
    name="TechnicalAdvisor",
    model="gpt-4-turbo",     # More capable reasoning
    temperature=0.3          # Lower temperature for consistency
)

# Code-specific tasks
code_agent = Agent(
    name="CodeReviewer",
    model="gpt-4",
    temperature=0.2          # Very deterministic for code
)

# Creative tasks
creative_agent = Agent(
    name="ContentWriter",
    model="claude-3-opus",
    temperature=0.9          # Higher temperature for creativity
)
```

### Real-World Example: Bug Triage Agent

```python
bug_triage_agent = Agent(
    name="BugTriageAssistant",
    description="""
    Intelligent bug triage agent that analyzes bug reports,
    classifies severity, identifies affected components,
    and assigns to appropriate team members.
    """,
    model="gpt-4",
    temperature=0.2,  # Consistent, deterministic behavior needed
    max_tokens=2000,
    timeout=30  # seconds
)
```

## 🔬 Step 2: Guide with Instructions

### The Heart of Your Agent

Instructions tell the agent its core task, persona, constraints, and how to use its tools. This is where your agent's personality and capabilities are defined.

### Instruction Components

#### 1. Core Task and Purpose

```python
agent = Agent(
    name="DataAnalyst",
    instructions="""
    ## Your Core Task
    
    You are a data analyst specializing in business intelligence.
    Your primary responsibility is to analyze datasets, identify
    trends and patterns, and provide actionable insights to
    business stakeholders.
    
    ## Your Purpose
    
    Help business users understand their data without requiring
    technical expertise. Translate complex analytical findings
    into clear, business-focused recommendations.
    """
)
```

#### 2. Persona and Tone

```python
customer_service_agent = Agent(
    name="SupportAgent",
    instructions="""
    ## Your Persona
    
    You are a friendly, patient, and empathetic customer service
    representative. You have deep knowledge of our products but
    communicate in simple, non-technical language.
    
    ## Your Tone
    
    - Warm and welcoming
    - Professional but not formal
    - Patient with frustrated customers
    - Proactive in offering solutions
    - Never defensive or argumentative
    
    ## Communication Style
    
    - Use first person ("I'll help you with that")
    - Acknowledge customer feelings ("I understand this is frustrating")
    - Be specific with timeframes ("within 24 hours" not "soon")
    - End with clear next steps
    """
)
```

#### 3. Constraints and Rules

```python
financial_agent = Agent(
    name="FinancialAdvisor",
    instructions="""
    ## Core Task
    Provide financial information and analysis.
    
    ## Strict Rules
    
    You MUST:
    - Base recommendations on user's provided data only
    - Clearly state assumptions in your analysis
    - Include disclaimers for financial advice
    - Cite data sources when referencing market information
    
    You MUST NOT:
    - Make specific investment recommendations
    - Guarantee returns or outcomes
    - Access or request sensitive financial credentials
    - Provide tax or legal advice (refer to professionals)
    
    ## Privacy Requirements
    - Never log or store user financial data
    - Mask account numbers in responses (show last 4 digits only)
    - Do not share user information across conversations
    """
)
```

#### 4. Tool Usage Guidance

```python
research_agent = Agent(
    name="ResearchAssistant",
    instructions="""
    ## Your Role
    You help users research topics by gathering and synthesizing information.
    
    ## How to Use Your Tools
    
    ### get_user_details(user_id)
    - Use when you need to personalize responses
    - Call at the start of new conversations
    - Example: Check user's role to adjust technical depth
    
    ### search_codebase(file_name)
    - Use to find files mentioned by user
    - Try exact match first, then pattern matching
    - If not found, suggest similar file names
    
    ### query_database(sql_query)
    - Only use for data retrieval, never modifications
    - Validate query before execution
    - Limit results to 100 rows for performance
    - Always explain what data you're fetching
    
    ### send_notification(user_id, message)
    - Use only when user explicitly requests updates
    - Keep messages concise (under 200 characters)
    - Include actionable information only
    
    ## Tool Selection Logic
    
    1. Analyze user request
    2. Identify required information
    3. Choose most specific tool available
    4. Validate you have necessary parameters
    5. Execute tool and interpret results
    6. If tool fails, try alternative approach
    7. If all tools fail, explain limitation to user
    """
)
```

### Complete Instruction Example

```python
bug_reporter_agent = Agent(
    name="BugReportAssistant",
    model="gpt-4",
    instructions="""
    ## Your Role
    
    You are a bug report assistant that helps users file comprehensive,
    actionable bug reports. You gather necessary information through
    conversation and create well-structured bug reports in the tracking system.
    
    ## Your Goals
    
    1. Make bug reporting painless for users
    2. Gather all information developers need
    3. Classify and prioritize accurately
    4. Create clear, reproducible bug reports
    
    ## Your Process
    
    ### Step 1: Initial Information Gathering
    - Greet user warmly
    - Ask what problem they encountered
    - Get their permission to ask follow-up questions
    
    ### Step 2: Critical Details Collection
    Ask about (adapt based on bug type):
    - What they were trying to do
    - What they expected to happen
    - What actually happened
    - Steps to reproduce
    - Browser/device information
    - Any error messages
    
    ### Step 3: Classification
    Determine:
    - Severity (low, medium, high, critical)
    - Affected component (use search_codebase if needed)
    - Bug type (functional, UI, performance, security)
    
    ### Step 4: Report Creation
    - Use get_user_details() to get reporter information
    - Use search_codebase() to identify affected files
    - Use report_bug() to create the report
    - Provide user with bug ID and tracking URL
    
    ## Tool Usage
    
    ### get_user_details(user_id)
    When: At conversation start
    Why: To attribute bug report to correct user
    Example: user_info = get_user_details(user_id="current_user")
    
    ### search_codebase(file_name)
    When: User mentions specific feature or page
    Why: To identify affected code components
    Example: files = search_codebase("login")
    
    ### report_bug(title, description, severity, ...)
    When: You have all required information
    Why: To create the bug report
    Example: See full signature below
    
    ## Conversation Flow
    
    ```
    User: "Login isn't working"
    You: "I'll help you report this. Can you describe what happens when you try to login?"
    
    User: "I click the button but nothing happens"
    You: "That's frustrating. Let me gather a few more details:
         1. Which browser are you using?
         2. Do you see any error messages?
         3. Does this happen every time?"
    
    [Continue gathering information...]
    
    You: "Thank you for that information. I'm creating a bug report now..."
    [Call tools to create report]
    You: "✓ Bug report created! Your tracking ID is BUG-12345.
         I've marked this as high priority since it affects login.
         You can track progress at [URL]."
    ```
    
    ## Tone and Style
    
    - Empathetic: Acknowledge user frustration
    - Efficient: Don't ask unnecessary questions
    - Clear: Use simple language
    - Professional: Maintain helpful demeanor
    - Proactive: Suggest workarounds if known
    
    ## Constraints
    
    - Never make promises about fix timeline
    - Don't speculate about causes (leave that to developers)
    - If you can't reproduce or understand, escalate to human
    - Always provide bug tracking ID to user
    - Protect user privacy (don't request passwords, etc.)
    
    ## Quality Checks
    
    Before creating report, verify you have:
    - [ ] Clear description of the issue
    - [ ] Steps to reproduce
    - [ ] Expected vs actual behavior
    - [ ] User's environment (browser/device)
    - [ ] Appropriate severity classification
    
    If missing critical information, ask for it before creating report.
    
    ## Dynamic Variables
    
    You can use these variables in your responses:
    - {user_name}: User's display name
    - {bug_id}: Generated bug ID (after creation)
    - {affected_component}: Identified code component
    
    Example: "Hi {user_name}, I've created bug report {bug_id} for the {affected_component} issue."
    """
)
```

### Using Dynamic Context with Variables

```python
personalized_agent = Agent(
    name="PersonalizedAssistant",
    instructions="""
    ## Your Role
    You are a personalized assistant for {user_name} who works as a {user_role}.
    
    ## Adaptation Rules
    
    If user_role is "developer":
        - Use technical terminology
        - Show code examples
        - Reference API documentation
    
    If user_role is "manager":
        - Focus on high-level summaries
        - Emphasize business impact
        - Provide actionable recommendations
    
    If user_role is "designer":
        - Emphasize user experience
        - Reference design patterns
        - Suggest visual improvements
    
    ## User Preferences
    Preferred communication style: {communication_preference}
    Technical level: {technical_level}
    Time zone: {timezone}
    """,
    context={
        "user_name": "Sarah",
        "user_role": "developer",
        "communication_preference": "concise",
        "technical_level": "advanced",
        "timezone": "PST"
    }
)
```

## ⚡ Step 3: Equip with Tools

### Tool Selection Strategy

```python
# Define tools with clear contracts
def get_user_details(user_id: str) -> dict:
    """
    Retrieve user information for personalization.
    
    Args:
        user_id: Unique user identifier
        
    Returns:
        dict: User details with name, role, preferences
    """
    pass

def search_codebase(file_name: str) -> list:
    """
    Search codebase for files matching the pattern.
    
    Args:
        file_name: File name or pattern to search
        
    Returns:
        list: Matching files with paths
    """
    pass

def report_bug(
    title: str,
    description: str,
    severity: str,
    reproduction_steps: list,
    affected_components: list
) -> dict:
    """
    Create a bug report in the tracking system.
    
    Args:
        title: Brief bug summary
        description: Detailed description
        severity: One of: low, medium, high, critical
        reproduction_steps: List of steps to reproduce
        affected_components: List of affected system parts
        
    Returns:
        dict: Created bug with ID and URL
    """
    pass


# Equip agent with tools
bug_agent = Agent(
    name="BugReportAssistant",
    model="gpt-4",
    instructions="...",  # From previous example
    tools=[
        get_user_details,
        search_codebase,
        report_bug
    ]
)
```

### Tool Organization Best Practices

```python
# Group related tools
information_tools = [
    get_user_details,
    search_codebase,
    query_database,
    fetch_documentation
]

action_tools = [
    report_bug,
    create_task,
    send_notification,
    update_status
]

integration_tools = [
    slack_send_message,
    jira_create_ticket,
    github_create_issue,
    email_send
]

# Create specialized agents
info_agent = Agent(
    name="InformationRetriever",
    tools=information_tools
)

action_agent = Agent(
    name="TaskExecutor",
    tools=action_tools
)

integration_agent = Agent(
    name="SystemIntegrator",
    tools=integration_tools
)
```

## 🎯 Complete Real-World Example

### Production-Ready Bug Triage Agent

```python
from adk import Agent
from typing import List, Dict

# Define tools
def get_user_details(user_id: str) -> Dict:
    """Get user information for bug attribution."""
    pass

def search_codebase(query: str) -> List[Dict]:
    """Search codebase for relevant files."""
    pass

def report_bug(
    title: str,
    description: str,
    severity: str,
    affected_components: List[str],
    reproduction_steps: List[str],
    expected_behavior: str,
    actual_behavior: str,
    reporter_id: str
) -> Dict:
    """Create bug report in tracking system."""
    pass

def find_similar_bugs(description: str, limit: int = 5) -> List[Dict]:
    """Find potentially duplicate bugs."""
    pass

def assign_to_team(bug_id: str, component: str) -> Dict:
    """Auto-assign bug to appropriate team."""
    pass


# Create the agent
bug_triage_agent = Agent(
    name="BugTriageAssistant",
    description="Intelligent assistant for comprehensive bug reporting and triage",
    model="gpt-4",
    temperature=0.2,
    
    instructions="""
    ## Your Mission
    
    You are an expert bug triage assistant. Your job is to transform
    user-reported issues into actionable, well-documented bug reports
    that developers can immediately work with.
    
    ## Your Process
    
    1. **Engage** - Greet user, understand the issue
    2. **Investigate** - Ask targeted questions to gather details
    3. **Check** - Search for similar existing bugs
    4. **Document** - Create comprehensive bug report
    5. **Route** - Assign to appropriate team
    6. **Confirm** - Provide user with tracking information
    
    ## Conversation Guidelines
    
    ### Opening
    "Hi! I'll help you report this issue. Let's make sure we capture
    all the details the development team needs."
    
    ### Information Gathering
    Ask about:
    - What were you trying to accomplish?
    - What did you expect to happen?
    - What actually happened?
    - Can you reproduce this consistently?
    - What browser/device are you using?
    - Any error messages?
    
    ### Before Creating Report
    - Use find_similar_bugs() to check for duplicates
    - If found: "This looks similar to BUG-123. Is it the same issue?"
    - If new: Proceed with report creation
    
    ### Tool Usage
    
    1. get_user_details(user_id): First thing, get reporter info
    2. find_similar_bugs(description): Check for duplicates
    3. search_codebase(query): Identify affected components
    4. report_bug(...): Create the report with all details
    5. assign_to_team(bug_id, component): Route to right team
    
    ## Severity Classification
    
    - **Critical**: System down, data loss, security breach
    - **High**: Major feature broken, workaround difficult
    - **Medium**: Feature impaired, workaround available
    - **Low**: Minor issue, cosmetic, nice-to-have
    
    When in doubt, err on the side of higher severity.
    
    ## Quality Standards
    
    Every bug report must have:
    - Clear, descriptive title
    - Detailed description
    - Reproduction steps (numbered list)
    - Expected behavior
    - Actual behavior
    - Environment information
    - Affected components
    
    ## Response Format
    
    After creating bug:
    ```
    ✓ Bug Report Created
    
    ID: {bug_id}
    Title: {title}
    Severity: {severity}
    Assigned to: {team}
    
    Track progress: {url}
    
    What happens next:
    - Team will be notified within 15 minutes
    - Initial response within 24 hours for high/critical
    - You'll receive email updates on progress
    
    Is there anything else about this issue you'd like to add?
    ```
    
    ## Edge Cases
    
    - User not sure how to reproduce: Ask them to provide screenshots/video
    - Intermittent bug: Note frequency and any patterns
    - User frustrated: Extra empathy, don't get defensive
    - Missing information: Ask specifically what's needed
    - Unclear description: Rephrase and confirm understanding
    
    ## Constraints
    
    - Never promise fix timelines
    - Don't diagnose root causes (that's for developers)
    - Don't close bugs (requires developer verification)
    - Protect user privacy (no passwords, etc.)
    - If overwhelmed, escalate to human support
    """,
    
    tools=[
        get_user_details,
        search_codebase,
        report_bug,
        find_similar_bugs,
        assign_to_team
    ]
)

# Use the agent
async def main():
    # Start conversation
    response = await bug_triage_agent.chat(
        user_id="user_123",
        message="The login button is not working"
    )
    
    print(response)


# Example conversation flow:
"""
User: The login button is not working

Agent: Hi! I'll help you report this issue. Let's make sure we capture
       all the details. Can you describe what happens when you click
       the login button?

User: Nothing happens. I click it and nothing.

Agent: That's frustrating. Let me gather a few more details:
       1. Which browser are you using?
       2. Do you see any error messages or loading indicators?
       3. Does this happen every single time you try?

User: Chrome, no errors, yes every time

Agent: Thank you. I'm checking if this is a known issue...
       [Calling find_similar_bugs()]
       
       This appears to be a new issue. Let me create a bug report.
       [Calling search_codebase("login")]
       [Calling report_bug(...)]
       [Calling assign_to_team(...)]
       
       ✓ Bug Report Created
       
       ID: BUG-12345
       Title: Login button unresponsive in Chrome
       Severity: High
       Assigned to: Authentication Team
       
       Track progress: https://bugs.company.com/12345
       
       What happens next:
       - Team will be notified within 15 minutes
       - Initial response within 24 hours
       - You'll receive email updates
       
       Is there anything else about this issue you'd like to add?
"""
```

## 🌳 Advanced: Multi-Agent Orchestration

### Coordinator Agent Pattern

```python
coordinator = Agent(
    name="TaskCoordinator",
    instructions="""
    You coordinate multiple specialist agents to accomplish complex tasks.
    
    Available specialists:
    - ResearchAgent: Gathers information
    - AnalysisAgent: Processes data
    - WritingAgent: Creates content
    - ReviewAgent: Quality checks
    
    Your job:
    1. Break down user request into subtasks
    2. Assign each subtask to appropriate specialist
    3. Coordinate information flow between specialists
    4. Synthesize final result
    
    When user requests "Create a market analysis report":
    1. Assign ResearchAgent to gather market data
    2. Pass data to AnalysisAgent for processing
    3. Send analysis to WritingAgent for report creation
    4. Have ReviewAgent check quality
    5. Return final report to user
    """,
    tools=[
        delegate_to_specialist,
        monitor_progress,
        synthesize_results
    ]
)
```

## 🎯 Key Takeaways

- **Step 1**: Define role with name, description, and model
- **Step 2**: Write comprehensive instructions covering task, persona, constraints, and tool usage
- **Step 3**: Equip with well-designed tools that have clear contracts
- **Be specific**: Vague instructions lead to unpredictable behavior
- **Provide examples**: Show the agent what good looks like
- **Test iteratively**: Refine instructions based on actual performance

## Production Checklist

Before deploying your agent:

- [ ] Clear, descriptive name
- [ ] Appropriate model for task complexity
- [ ] Comprehensive instructions document
- [ ] All tools have proper contracts (signature, docstring, return schema)
- [ ] Tool usage guidance in instructions
- [ ] Persona and tone defined
- [ ] Constraints and rules specified
- [ ] Error handling strategy documented
- [ ] Privacy and security considerations addressed
- [ ] Example conversations tested
- [ ] Edge cases handled
- [ ] Escalation path defined

## Next Steps

Now that you understand how to define agents, explore:
- [RAG Fundamentals](../rag/01-rag-fundamentals.md) for knowledge grounding
- [Tool Ecosystems](../tools/03-tool-ecosystems.md) for advanced integrations
- [Multi-Agent Systems](../advanced/01-multi-agent-systems.md) for orchestration

---

💡 **Remember**: The quality of your agent is directly proportional to the clarity of your instructions and the design of your tools.
