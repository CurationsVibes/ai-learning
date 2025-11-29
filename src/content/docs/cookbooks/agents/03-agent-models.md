---
title: 📋 Agent Models & API Contracts
---

## 🌳 Flourishing Concept

**Label**: Designing Reliable Agent Interfaces

For AI agents to work correctly with LLMs, they must have well-defined **API contracts**. This contract is how the model understands what tools are available and how to use them properly.

## What is an API Contract?

An API contract consists of three essential components:

```
┌────────────────────────────────────────┐
│         API Contract                   │
├────────────────────────────────────────┤
│                                        │
│  1. Function Signature                 │
│     └─ Names, parameters, types        │
│                                        │
│  2. Docstring (Semantic Core)          │
│     └─ Purpose, usage, behavior        │
│                                        │
│  3. Return Schema                      │
│     └─ Structure, status indicators    │
│                                        │
└────────────────────────────────────────┘
```

## 💡 Component 1: Function Signature

### The Structural Foundation

The function signature provides the **syntactic schema** the model uses to generate valid arguments.

#### Essential Elements

```python
def search_documents(
    query: str,                    # Type hints are MANDATORY
    max_results: int = 10,         # Default values guide behavior
    filter_by_date: Optional[str] = None,  # Optional parameters
    include_archived: bool = False
) -> dict:                         # Return type specification
    """Docstring here..."""
    pass
```

### Why Type Hints Are Mandatory

```python
# ❌ BAD: Model doesn't know what types to use
def search_documents(query, max_results, filter_by_date):
    pass

# ✅ GOOD: Model knows exact types expected
def search_documents(
    query: str, 
    max_results: int, 
    filter_by_date: Optional[str]
) -> dict:
    pass
```

### Descriptive Parameter Names

```python
# ❌ BAD: Ambiguous parameter names
def process(x: str, n: int, f: bool) -> dict:
    pass

# ✅ GOOD: Self-documenting names
def search_documents(
    search_query: str,
    maximum_results: int,
    filter_by_category: bool
) -> dict:
    pass
```

### Real-World Example: Bug Reporting Tool

```python
from typing import List, Optional, Literal
from datetime import datetime

def report_bug(
    title: str,
    description: str,
    severity: Literal["low", "medium", "high", "critical"],
    affected_components: List[str],
    reproduction_steps: List[str],
    expected_behavior: str,
    actual_behavior: str,
    browser: Optional[str] = None,
    os: Optional[str] = None,
    attachments: Optional[List[str]] = None
) -> dict:
    """
    Report a software bug with detailed information.
    
    Args:
        title: Brief summary of the bug (max 100 chars)
        description: Detailed description of the issue
        severity: Bug severity level affecting priority
        affected_components: List of system components impacted
        reproduction_steps: Step-by-step instructions to reproduce
        expected_behavior: What should happen
        actual_behavior: What actually happens
        browser: Browser name and version if applicable
        os: Operating system if relevant
        attachments: URLs or paths to screenshots/logs
    
    Returns:
        dict: Created bug report with ID and status
            {
                "bug_id": str,
                "status": "success" | "error",
                "message": str,
                "url": str (if success)
            }
    """
    # Implementation
    pass
```

## 🔬 Component 2: Docstring (The Semantic Core)

### The Primary Source of Understanding

The docstring is the **most important** part of the contract. It provides semantic information that helps the model understand:

- Tool's purpose
- When to use it
- How to use it correctly
- Expected behavior
- Edge cases

### Anatomy of a Perfect Docstring

```python
def get_user_details(user_id: str) -> dict:
    """
    Retrieve comprehensive user information from the database.
    
    Use this tool when you need to look up user profile data,
    preferences, or account information. DO NOT use this for
    authentication purposes.
    
    Args:
        user_id: Unique user identifier (UUID format).
                 Example: "a3b2c1d4-e5f6-4a5b-8c9d-0e1f2a3b4c5d"
    
    Returns:
        dict: User information structured as:
            {
                "status": "success" | "error",
                "user": {
                    "id": str,
                    "name": str,
                    "email": str,
                    "preferences": dict,
                    "created_at": str (ISO 8601 format)
                },
                "message": str (only present if error)
            }
    
    Raises:
        ValueError: If user_id format is invalid
        UserNotFoundError: If user doesn't exist
    
    Example:
        >>> details = get_user_details("a3b2c1d4-e5f6-4a5b-8c9d-0e1f2a3b4c5d")
        >>> print(details["user"]["name"])
        "John Doe"
    
    Note:
        This function requires database read permissions.
        Results are cached for 5 minutes.
    """
    # Implementation
    pass
```

### Best Practices for Docstrings

#### 1. Clearly Define Purpose

```python
def search_codebase(file_pattern: str) -> List[dict]:
    """
    Search the codebase for files matching a pattern.
    
    Use this tool when:
    - You need to find files by name or path
    - You want to locate where specific components are defined
    - You're looking for configuration files
    
    DO NOT use this tool for:
    - Searching file contents (use search_file_contents instead)
    - Finding specific code symbols (use find_symbol instead)
    """
    pass
```

#### 2. Provide Usage Criteria

```python
def calculate_shipping_cost(
    weight_kg: float,
    destination: str,
    expedited: bool = False
) -> dict:
    """
    Calculate shipping cost for an order.
    
    **When to use:**
    - Customer asks "How much is shipping?"
    - During checkout process
    - When comparing delivery options
    
    **Prerequisites:**
    - Weight must be in kilograms
    - Destination must be a valid country code (ISO 3166-1 alpha-2)
    - Order must not contain restricted items
    
    **Decision logic:**
    - Use expedited=True only if customer explicitly requests fast shipping
    - Use expedited=False for standard/economy shipping
    """
    pass
```

#### 3. Specify Parameter Details

```python
def update_inventory(
    product_id: str,
    quantity_change: int,
    reason: Literal["sale", "restock", "return", "damage", "adjustment"]
) -> dict:
    """
    Update product inventory quantity.
    
    Args:
        product_id: Product SKU or unique identifier.
                    Format: "PROD-XXXXX" where X is alphanumeric.
                    Example: "PROD-A1B2C"
        
        quantity_change: Change in quantity (can be positive or negative).
                        Positive: Adding stock (restock, return)
                        Negative: Removing stock (sale, damage)
                        Must be non-zero.
        
        reason: Reason for inventory change. Determines accounting treatment:
                - "sale": Customer purchase (triggers revenue recognition)
                - "restock": New inventory received
                - "return": Customer returned item
                - "damage": Item damaged/unsellable
                - "adjustment": Manual correction (requires approval)
    
    Returns:
        dict: Updated inventory status with new quantity and transaction ID
    """
    pass
```

#### 4. Document Return Schema Thoroughly

```python
def process_payment(
    amount: float,
    payment_method: str,
    customer_id: str
) -> dict:
    """
    Process a customer payment transaction.
    
    Returns:
        dict: Payment result with the following structure:
        
        Success case:
        {
            "status": "success",
            "transaction_id": str,          # Unique transaction identifier
            "amount_charged": float,        # Actual amount charged
            "currency": str,                # ISO 4217 currency code
            "timestamp": str,               # ISO 8601 timestamp
            "payment_method_last4": str,    # Last 4 digits of payment method
            "receipt_url": str              # URL to download receipt
        }
        
        Failure case:
        {
            "status": "error",
            "error_code": str,              # Machine-readable error code
            "error_message": str,           # Human-readable error description
            "retry_allowed": bool,          # Whether retry is possible
            "suggested_action": str         # What to do next
        }
    
    Note: Always check 'status' field before processing other fields.
    """
    pass
```

## ⚡ Component 3: Return Schema

### Why Return Structure Matters

Agents need to **reliably distinguish** between successful outcomes and failures in their observation steps.

### The Status Key Pattern

```python
# ✅ BEST PRACTICE: Always include status indicator
def execute_task(task_id: str) -> dict:
    """Execute a task."""
    try:
        result = perform_task(task_id)
        return {
            "status": "success",  # Clear success indicator
            "result": result,
            "task_id": task_id
        }
    except Exception as e:
        return {
            "status": "error",    # Clear error indicator
            "error": str(e),
            "task_id": task_id
        }
```

### Consistent Return Structures

```python
class ToolResponse:
    """Standard response structure for all tools"""
    
    @staticmethod
    def success(data: dict, message: str = "") -> dict:
        """Standard success response"""
        return {
            "status": "success",
            "data": data,
            "message": message,
            "timestamp": datetime.now().isoformat()
        }
    
    @staticmethod
    def error(error: str, code: str = "GENERAL_ERROR", 
              recoverable: bool = False) -> dict:
        """Standard error response"""
        return {
            "status": "error",
            "error": error,
            "error_code": code,
            "recoverable": recoverable,
            "timestamp": datetime.now().isoformat()
        }
    
    @staticmethod
    def partial(data: dict, warnings: List[str]) -> dict:
        """Partial success response"""
        return {
            "status": "partial",
            "data": data,
            "warnings": warnings,
            "timestamp": datetime.now().isoformat()
        }


# Usage in tools
def search_database(query: str) -> dict:
    """Search database with standardized responses."""
    try:
        results = db.search(query)
        if not results:
            return ToolResponse.success(
                data={"results": [], "count": 0},
                message="No results found"
            )
        return ToolResponse.success(
            data={"results": results, "count": len(results)}
        )
    except DatabaseError as e:
        return ToolResponse.error(
            error=str(e),
            code="DATABASE_ERROR",
            recoverable=True
        )
```

## 🎯 Complete Example: Well-Designed Tool

```python
from typing import List, Optional, Literal, Dict
from datetime import datetime
from enum import Enum

class Priority(Enum):
    """Task priority levels"""
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    URGENT = 4


def create_task(
    title: str,
    description: str,
    assignee_email: str,
    priority: Literal["low", "medium", "high", "urgent"],
    due_date: str,
    tags: Optional[List[str]] = None,
    parent_task_id: Optional[str] = None,
    estimated_hours: Optional[float] = None
) -> Dict[str, any]:
    """
    Create a new task in the project management system.
    
    This tool should be used when a user explicitly requests to create,
    add, or assign a new task. It integrates with the team's task tracking
    system and sends notifications to the assignee.
    
    **When to use this tool:**
    - User says "create a task for X"
    - User wants to assign work to someone
    - User mentions "add this to our backlog"
    
    **When NOT to use:**
    - Just discussing potential work (no explicit creation request)
    - Updating existing tasks (use update_task instead)
    - Querying task status (use get_task instead)
    
    Args:
        title: Task title (max 200 characters).
               Should be concise and action-oriented.
               Example: "Implement user authentication API"
        
        description: Detailed task description (supports markdown).
                    Include:
                    - Context and background
                    - Acceptance criteria
                    - Any relevant links or references
        
        assignee_email: Email of team member to assign task to.
                       Must be a valid team member email.
                       System will validate and reject invalid emails.
        
        priority: Task priority affecting schedule and notifications.
                 - "low": Nice to have, flexible timeline
                 - "medium": Normal priority, standard timeline
                 - "high": Important, needs attention soon
                 - "urgent": Critical, immediate attention required
        
        due_date: Task deadline in ISO 8601 format (YYYY-MM-DD).
                 Example: "2024-12-31"
                 Must be a future date.
        
        tags: Optional list of tags for categorization.
              Examples: ["bug", "frontend"], ["feature", "api"]
              Tags are case-insensitive and will be normalized.
        
        parent_task_id: Optional ID of parent task for sub-task creation.
                       If provided, this task becomes a sub-task.
                       Parent task must exist and be accessible.
        
        estimated_hours: Optional time estimate in hours.
                        Used for capacity planning and reporting.
                        Example: 8.5 for 8 hours 30 minutes.
    
    Returns:
        dict: Task creation result with structure:
        
        Success response:
        {
            "status": "success",
            "task": {
                "id": str,                    # Unique task ID
                "title": str,                 # Task title
                "description": str,           # Full description
                "assignee": {
                    "email": str,
                    "name": str
                },
                "priority": str,              # Priority level
                "due_date": str,              # ISO 8601 date
                "created_at": str,            # ISO 8601 timestamp
                "created_by": str,            # Creator email
                "url": str,                   # Direct link to task
                "tags": List[str],            # Normalized tags
                "parent_task_id": str | null,
                "estimated_hours": float | null
            },
            "notifications_sent": bool,       # Whether assignee was notified
            "message": str                    # Success message
        }
        
        Error response:
        {
            "status": "error",
            "error_code": str,                # Machine-readable code
            "error_message": str,             # Human-readable message
            "field_errors": dict | null,      # Field-specific validation errors
            "suggested_action": str           # What to do to fix
        }
        
        Error codes:
        - "INVALID_EMAIL": assignee_email not found in team
        - "INVALID_DATE": due_date is in the past or invalid format
        - "PARENT_NOT_FOUND": parent_task_id doesn't exist
        - "PERMISSION_DENIED": user lacks permission to assign tasks
        - "VALIDATION_ERROR": one or more fields failed validation
    
    Raises:
        This function returns errors as dict; it does not raise exceptions.
    
    Example:
        >>> result = create_task(
        ...     title="Fix login bug",
        ...     description="Users cannot login with special characters in password",
        ...     assignee_email="dev@example.com",
        ...     priority="high",
        ...     due_date="2024-06-15",
        ...     tags=["bug", "security"],
        ...     estimated_hours=4.0
        ... )
        >>> if result["status"] == "success":
        ...     print(f"Task created: {result['task']['url']}")
    
    Notes:
        - Task creation triggers email notification to assignee
        - If assignee has notifications disabled, they'll see in-app alert
        - Tasks with "urgent" priority also notify task creator's manager
        - Estimated hours affect team capacity calculations
        - All timestamps are in UTC
    
    Performance:
        Typical execution time: 100-300ms
        Includes: validation, database write, notification dispatch
    """
    # Implementation would go here
    try:
        # Validate inputs
        if not _is_valid_email(assignee_email):
            return {
                "status": "error",
                "error_code": "INVALID_EMAIL",
                "error_message": f"Email '{assignee_email}' not found in team",
                "suggested_action": "Check email spelling or add user to team first"
            }
        
        # Create task
        task = _create_task_in_db(
            title=title,
            description=description,
            assignee_email=assignee_email,
            priority=priority,
            due_date=due_date,
            tags=tags,
            parent_task_id=parent_task_id,
            estimated_hours=estimated_hours
        )
        
        # Send notifications
        notifications_sent = _send_notifications(task)
        
        return {
            "status": "success",
            "task": task.to_dict(),
            "notifications_sent": notifications_sent,
            "message": f"Task '{title}' created and assigned to {assignee_email}"
        }
        
    except Exception as e:
        return {
            "status": "error",
            "error_code": "INTERNAL_ERROR",
            "error_message": str(e),
            "suggested_action": "Contact system administrator"
        }
```

## 🌳 Advanced: Type Systems for Complex Tools

### Using Pydantic for Validation

```python
from pydantic import BaseModel, Field, validator
from typing import List, Optional

class TaskInput(BaseModel):
    """Validated input for task creation"""
    
    title: str = Field(..., min_length=1, max_length=200)
    description: str = Field(..., min_length=10)
    assignee_email: str = Field(..., regex=r'^[\w\.-]+@[\w\.-]+\.\w+$')
    priority: Literal["low", "medium", "high", "urgent"]
    due_date: str = Field(..., regex=r'^\d{4}-\d{2}-\d{2}$')
    tags: Optional[List[str]] = Field(default=None, max_items=10)
    
    @validator('due_date')
    def validate_future_date(cls, v):
        date = datetime.fromisoformat(v)
        if date < datetime.now():
            raise ValueError('due_date must be in the future')
        return v


def create_task_validated(input_data: TaskInput) -> dict:
    """
    Type-safe task creation with automatic validation.
    
    Pydantic handles all input validation automatically.
    """
    # Input is guaranteed to be valid here
    pass
```

## 🎯 Key Takeaways

- **Function signature** provides structural schema (type hints mandatory)
- **Docstring** is the semantic core (most important component)
- **Return schema** enables reliable observation (status key essential)
- **Consistency** across tools helps models learn patterns
- **Documentation** is not optional—it's part of the contract

## Common Mistakes to Avoid

```python
# ❌ Missing type hints
def process(data):
    pass

# ❌ Unclear parameter names
def func(x, y, z):
    pass

# ❌ No docstring
def important_function(data: dict) -> dict:
    pass

# ❌ Inconsistent return structure
def tool1():
    return {"success": True}
def tool2():
    return {"status": "ok"}

# ❌ No error handling
def fragile_tool(id: str) -> dict:
    return db.get(id)  # What if it fails?
```

## Next Steps

Continue to [Defining LLM Agents](./04-defining-llm-agents/) to learn how to put these contracts together into complete agent definitions.

---

💡 **Remember**: A well-defined API contract is the difference between an agent that works reliably and one that fails unpredictably.
