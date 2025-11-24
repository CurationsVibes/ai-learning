---
title: "🎭 Agent Types: Choosing Your Architecture"
---

## 🌿 Growing Concept

**Label**: Matching Agent Design to Task Structure

Different tasks require different agent architectures. Understanding agent types helps you build systems that naturally fit your problem structure.

## Agent Type Overview

```
┌────────────────────────────────────────────────┐
│            Agent Types                         │
├────────────────────────────────────────────────┤
│                                                │
│  Sequential  →  Step-by-step processing       │
│  Parallel    →  Simultaneous execution        │
│  Loop        →  Iterative refinement           │
│  Custom      →  Specialized logic              │
│                                                │
└────────────────────────────────────────────────┘
```

## 🎯 Sequential Agents

### When to Use

Tasks that require ordered, dependent steps:
- Data pipelines (collect → process → analyze → report)
- Content creation (research → outline → write → edit)
- Approval workflows (submit → review → approve → deploy)

### Implementation

```python
from adk import SequentialAgent, Agent

class ContentCreationPipeline(SequentialAgent):
    """
    Sequential agent for content creation
    """
    def __init__(self):
        super().__init__(
            agents=[
                Agent(
                    name="Researcher",
                    role="Gather information",
                    tools=[web_search, database_query]
                ),
                Agent(
                    name="Outliner",
                    role="Structure content",
                    tools=[outline_generator]
                ),
                Agent(
                    name="Writer",
                    role="Create content",
                    tools=[content_generator, style_checker]
                ),
                Agent(
                    name="Editor",
                    role="Refine and polish",
                    tools=[grammar_checker, fact_verifier]
                )
            ]
        )
    
    async def create_content(self, topic: str) -> dict:
        """
        Execute content creation pipeline
        """
        # Each agent processes output from previous agent
        result = {"topic": topic}
        
        for agent in self.agents:
            print(f"Starting: {agent.name}")
            result = await agent.process(result)
            print(f"Completed: {agent.name}")
            
            # Optional: validate between steps
            if not self.validate_output(agent, result):
                raise Exception(f"{agent.name} produced invalid output")
        
        return result


# Usage
pipeline = ContentCreationPipeline()
article = await pipeline.create_content("Introduction to RAG systems")

print(f"Article created: {article['title']}")
print(f"Word count: {article['word_count']}")
```

### Real-World Example: Bug Triage System

```python
class BugTriageAgent(SequentialAgent):
    """
    Automated bug triage workflow
    """
    def __init__(self):
        super().__init__(
            agents=[
                Agent("Classifier", tools=[bug_classifier]),
                Agent("Prioritizer", tools=[priority_scorer]),
                Agent("Assigner", tools=[team_matcher, workload_checker]),
                Agent("Notifier", tools=[email_sender, slack_poster])
            ]
        )
    
    async def triage_bug(self, bug_report: dict) -> dict:
        """
        Process bug through triage stages
        """
        context = {"bug": bug_report}
        
        # Stage 1: Classify bug type
        context = await self.agents[0].process(context)
        # context now has: category, severity
        
        # Stage 2: Determine priority
        context = await self.agents[1].process(context)
        # context now has: priority_score
        
        # Stage 3: Assign to team member
        context = await self.agents[2].process(context)
        # context now has: assigned_to
        
        # Stage 4: Send notifications
        context = await self.agents[3].process(context)
        
        return context


# Usage
triage = BugTriageAgent()
result = await triage.triage_bug({
    "title": "Login button not responding",
    "description": "User clicks login but nothing happens",
    "reporter": "user@example.com"
})

print(f"Bug assigned to: {result['assigned_to']}")
print(f"Priority: {result['priority_score']}")
```

## ⚡ Parallel Agents

### When to Use

Tasks where multiple independent operations can run simultaneously:
- Multi-perspective analysis
- Parallel data processing
- Redundant verification
- Competitive approaches (pick best result)

### Implementation

```python
from adk import ParallelAgent, Agent
import asyncio

class MultiPerspectiveAnalysis(ParallelAgent):
    """
    Parallel agent for simultaneous analysis
    """
    def __init__(self):
        super().__init__(
            agents=[
                Agent(
                    name="Technical Analyst",
                    role="Evaluate technical feasibility",
                    tools=[code_analyzer, architecture_reviewer]
                ),
                Agent(
                    name="Business Analyst",
                    role="Assess business value",
                    tools=[roi_calculator, market_analyzer]
                ),
                Agent(
                    name="UX Analyst",
                    role="Evaluate user experience",
                    tools=[usability_scorer, accessibility_checker]
                ),
                Agent(
                    name="Security Analyst",
                    role="Identify security concerns",
                    tools=[vulnerability_scanner, compliance_checker]
                )
            ]
        )
    
    async def analyze_feature(self, feature_spec: dict) -> dict:
        """
        Analyze feature from multiple perspectives simultaneously
        """
        # Execute all analyses in parallel
        results = await asyncio.gather(*[
            agent.process(feature_spec)
            for agent in self.agents
        ])
        
        # Combine perspectives
        combined_analysis = {
            "technical": results[0],
            "business": results[1],
            "ux": results[2],
            "security": results[3],
            "overall_score": self.calculate_overall_score(results),
            "recommendations": self.merge_recommendations(results)
        }
        
        return combined_analysis
    
    def calculate_overall_score(self, results: list) -> float:
        """
        Weighted average of all perspectives
        """
        weights = {"technical": 0.3, "business": 0.3, "ux": 0.25, "security": 0.15}
        scores = [r['score'] for r in results]
        return sum(s * w for s, w in zip(scores, weights.values()))


# Usage
analyzer = MultiPerspectiveAnalysis()
analysis = await analyzer.analyze_feature({
    "name": "Social login integration",
    "description": "Allow users to login with Google/Facebook",
    "estimated_effort": "2 weeks"
})

print(f"Overall score: {analysis['overall_score']}/10")
for perspective, result in analysis.items():
    if perspective not in ['overall_score', 'recommendations']:
        print(f"{perspective}: {result['score']}/10 - {result['summary']}")
```

### Real-World Example: Image Generation with Validation

```python
class ImageGeneratorWithValidation(ParallelAgent):
    """
    Generate multiple images and validate simultaneously
    """
    def __init__(self):
        self.generators = [
            Agent("Generator1", model="stable-diffusion"),
            Agent("Generator2", model="dall-e"),
            Agent("Generator3", model="midjourney")
        ]
        self.validators = [
            Agent("QualityChecker", tools=[quality_scorer]),
            Agent("StyleValidator", tools=[style_matcher]),
            Agent("ContentValidator", tools=[content_verifier])
        ]
    
    async def generate_and_validate(self, prompt: str) -> dict:
        """
        Generate multiple images and validate in parallel
        """
        # Parallel generation
        images = await asyncio.gather(*[
            gen.generate(prompt) for gen in self.generators
        ])
        
        # Parallel validation of all images
        validation_tasks = []
        for image in images:
            for validator in self.validators:
                validation_tasks.append(validator.validate(image))
        
        validations = await asyncio.gather(*validation_tasks)
        
        # Select best image based on validation scores
        best_image = self.select_best(images, validations)
        
        return best_image


# Usage
generator = ImageGeneratorWithValidation()
image = await generator.generate_and_validate(
    "A serene mountain landscape at sunset with a lake"
)
print(f"Best image: {image['url']} (score: {image['score']})")
```

## 🔄 Loop Agents

### When to Use

Tasks that require iterative refinement:
- Code generation and debugging
- Image/content generation until quality threshold
- Optimization problems
- Self-improvement workflows

### Implementation

```python
from adk import LoopAgent, Agent

class CodeGeneratorWithRefinement(LoopAgent):
    """
    Loop agent that refines code until it meets criteria
    """
    def __init__(self):
        self.generator = Agent(
            name="Code Generator",
            tools=[code_generation]
        )
        self.tester = Agent(
            name="Code Tester",
            tools=[unit_test_runner, static_analyzer]
        )
        self.reviewer = Agent(
            name="Code Reviewer",
            tools=[quality_checker, best_practices_validator]
        )
    
    async def generate_code(self, 
                          requirements: str, 
                          max_iterations: int = 5,
                          quality_threshold: float = 0.9) -> dict:
        """
        Generate and refine code iteratively
        """
        iteration = 0
        code = None
        feedback = None
        
        while iteration < max_iterations:
            iteration += 1
            print(f"\n=== Iteration {iteration} ===")
            
            # Generate/refine code
            if code is None:
                code = await self.generator.process(requirements)
            else:
                code = await self.generator.process({
                    "requirements": requirements,
                    "previous_code": code,
                    "feedback": feedback
                })
            
            # Test code
            test_results = await self.tester.process(code)
            
            # Review code quality
            review_results = await self.reviewer.process(code)
            
            # Check if meets criteria
            quality_score = self.calculate_quality(test_results, review_results)
            print(f"Quality score: {quality_score:.2f}")
            
            if quality_score >= quality_threshold:
                print(f"✓ Code meets quality threshold!")
                return {
                    "code": code,
                    "iterations": iteration,
                    "quality_score": quality_score,
                    "test_results": test_results,
                    "review_results": review_results
                }
            
            # Prepare feedback for next iteration
            feedback = self.compile_feedback(test_results, review_results)
            print(f"Issues found: {len(feedback['issues'])}")
        
        # Max iterations reached
        return {
            "code": code,
            "iterations": iteration,
            "quality_score": quality_score,
            "status": "max_iterations_reached"
        }
    
    def calculate_quality(self, test_results: dict, review_results: dict) -> float:
        """
        Calculate overall quality score
        """
        test_score = test_results['pass_rate']
        review_score = review_results['quality_score']
        return (test_score * 0.6) + (review_score * 0.4)


# Usage
code_agent = CodeGeneratorWithRefinement()

result = await code_agent.generate_code(
    requirements="""
    Create a Python function that:
    1. Accepts a list of numbers
    2. Returns the median value
    3. Handles empty lists gracefully
    4. Has proper error handling
    """,
    max_iterations=5,
    quality_threshold=0.9
)

print(f"\n=== Final Result ===")
print(f"Iterations needed: {result['iterations']}")
print(f"Final quality: {result['quality_score']:.2f}")
print(f"\nGenerated code:\n{result['code']}")
```

### Real-World Example: Image Generation with Count Verification

```python
class FoodImageGenerator(LoopAgent):
    """
    Generate images with specific food item counts
    Example from the requirements: "five bananas"
    """
    def __init__(self):
        self.generator = Agent("Image Generator", tools=[generate_image])
        self.counter = Agent("Food Counter", tools=[count_food_items])
    
    async def generate_with_count(self, 
                                  description: str, 
                                  target_count: int,
                                  max_attempts: int = 5) -> dict:
        """
        Generate image until correct number of items
        """
        for attempt in range(max_attempts):
            print(f"Attempt {attempt + 1}: Generating image...")
            
            # Generate image
            image = await self.generator.process(description)
            
            # Count items
            count_result = await self.counter.process(image)
            actual_count = count_result['count']
            
            print(f"Found {actual_count} items (target: {target_count})")
            
            if actual_count == target_count:
                return {
                    "image": image,
                    "attempts": attempt + 1,
                    "status": "success"
                }
        
        return {
            "image": image,
            "attempts": max_attempts,
            "status": "max_attempts_reached",
            "final_count": actual_count
        }


# Usage
generator = FoodImageGenerator()
result = await generator.generate_with_count(
    description="Five bananas on a wooden table",
    target_count=5
)

if result['status'] == 'success':
    print(f"✓ Successfully generated image with 5 bananas in {result['attempts']} attempts")
else:
    print(f"✗ Could not generate exact count after {result['attempts']} attempts")
```

## 🛠️ Custom Agents

### When to Use

Tasks requiring specialized logic beyond standard patterns:
- Complex state machines
- Domain-specific workflows
- Custom optimization algorithms
- Unique business logic

### Implementation

```python
from adk import BaseAgent

class CustomWorkflowAgent(BaseAgent):
    """
    Custom agent with specialized Python logic
    """
    def __init__(self, name: str, tools: list):
        super().__init__(name=name, tools=tools)
        self.state = {}
        self.history = []
    
    async def process(self, input_data: dict) -> dict:
        """
        Custom processing logic
        """
        # Your custom Python logic here
        self.state['current_input'] = input_data
        
        # Implement custom decision tree
        if self.should_branch_a(input_data):
            result = await self.execute_branch_a(input_data)
        elif self.should_branch_b(input_data):
            result = await self.execute_branch_b(input_data)
        else:
            result = await self.execute_default(input_data)
        
        # Update history
        self.history.append({
            "input": input_data,
            "output": result,
            "timestamp": datetime.now()
        })
        
        return result
    
    def should_branch_a(self, data: dict) -> bool:
        """Custom condition logic"""
        return data.get('priority') == 'high' and data.get('complexity') < 5
    
    def should_branch_b(self, data: dict) -> bool:
        """Custom condition logic"""
        return data.get('type') == 'emergency'
    
    async def execute_branch_a(self, data: dict) -> dict:
        """Custom execution logic"""
        # Your implementation
        pass


# Usage
custom_agent = CustomWorkflowAgent(
    name="SpecializedProcessor",
    tools=[tool1, tool2]
)

result = await custom_agent.process({"priority": "high", "complexity": 3})
```

### Real-World Example: Adaptive Customer Support Router

```python
class AdaptiveCustomerSupport(BaseAgent):
    """
    Custom agent that routes tickets based on complex criteria
    """
    def __init__(self):
        super().__init__(name="SupportRouter")
        self.ticket_history = {}
        self.agent_workloads = {}
        self.escalation_threshold = 3
    
    async def route_ticket(self, ticket: dict) -> dict:
        """
        Custom routing logic considering multiple factors
        """
        customer_id = ticket['customer_id']
        
        # Check customer history
        history = self.ticket_history.get(customer_id, [])
        
        # Custom escalation logic
        if len(history) >= self.escalation_threshold:
            return await self.escalate_to_senior(ticket, history)
        
        # Analyze ticket sentiment
        sentiment = await self.analyze_sentiment(ticket['message'])
        
        # Analyze technical complexity
        complexity = await self.assess_complexity(ticket)
        
        # Custom agent selection algorithm
        if sentiment['score'] < -0.5 and sentiment['urgency'] > 0.8:
            # Frustrated customer - route to empathy specialist
            agent = self.find_available_agent(skill='empathy')
        elif complexity['technical_level'] > 0.8:
            # Technical issue - route to technical specialist
            agent = self.find_available_agent(skill='technical')
        else:
            # Standard routing - balance workload
            agent = self.find_least_busy_agent()
        
        # Update state
        self.ticket_history[customer_id] = history + [ticket]
        self.agent_workloads[agent['id']] += 1
        
        return {
            "assigned_to": agent,
            "routing_reason": self.explain_routing(sentiment, complexity),
            "priority": self.calculate_priority(sentiment, complexity, history)
        }
```

## 🎯 Agent Type Selection Guide

### Decision Tree

```
Question: Is your task linear and sequential?
  ├─ Yes → Use Sequential Agent
  └─ No → Question: Can subtasks run independently?
           ├─ Yes → Use Parallel Agent
           └─ No → Question: Do you need iterative improvement?
                    ├─ Yes → Use Loop Agent
                    └─ No → Use Custom Agent
```

### Comparison Table

| Agent Type | Best For | Complexity | Flexibility |
|------------|----------|------------|-------------|
| Sequential | Pipelines, workflows | Low | Low |
| Parallel | Independent tasks | Medium | Medium |
| Loop | Refinement, optimization | Medium | Medium |
| Custom | Specialized logic | High | High |

## 🌳 Advanced: Hybrid Architectures

### Combining Agent Types

```python
class HybridAgent:
    """
    Combine multiple agent types for complex workflows
    """
    def __init__(self):
        # Sequential pre-processing
        self.preprocessor = SequentialAgent([
            Agent("Validator"),
            Agent("Normalizer")
        ])
        
        # Parallel processing
        self.processors = ParallelAgent([
            Agent("Processor1"),
            Agent("Processor2"),
            Agent("Processor3")
        ])
        
        # Loop for refinement
        self.refiner = LoopAgent(
            Agent("Refiner"),
            max_iterations=3
        )
        
        # Sequential post-processing
        self.postprocessor = SequentialAgent([
            Agent("Aggregator"),
            Agent("Formatter")
        ])
    
    async def process(self, data: dict) -> dict:
        # Sequential pre-processing
        data = await self.preprocessor.process(data)
        
        # Parallel processing
        results = await self.processors.process(data)
        
        # Loop refinement
        refined = await self.refiner.process(results)
        
        # Sequential post-processing
        final = await self.postprocessor.process(refined)
        
        return final
```

## 🎯 Key Takeaways

- **Sequential**: For ordered, dependent steps
- **Parallel**: For independent simultaneous tasks
- **Loop**: For iterative improvement
- **Custom**: For specialized logic

- **Choose based on task structure**, not personal preference
- **Combine types** for complex workflows
- **Start simple**, add complexity as needed

## Next Steps

Continue to [Agent Models & Contracts](./03-agent-models.md) to learn how to properly define agent APIs and interfaces.

---

💡 **Remember**: The best agent type is the one that naturally mirrors your problem structure.
