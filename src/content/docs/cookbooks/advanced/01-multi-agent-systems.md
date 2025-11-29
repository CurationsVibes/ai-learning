---
title: "🤝 Multi-Agent Systems: Orchestration Patterns"
description: Building sophisticated systems with multiple AI agents working together
---

## 🌳 Forest-Level Concept

**Label**: Coordinating Multiple Agents for Complex Tasks

Multi-agent systems combine specialized agents to tackle problems too complex for any single agent. Understanding orchestration patterns is key to building scalable AI systems.

## Multi-Agent Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                   Multi-Agent System                        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Orchestrator  →  Coordinates all agents                   │
│       │                                                     │
│       ├── Specialist Agent A  (Domain Expert)              │
│       ├── Specialist Agent B  (Tool Expert)                │
│       ├── Specialist Agent C  (Analysis Expert)            │
│       └── Validator Agent     (Quality Control)            │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## 🎯 When to Use Multi-Agent Systems

### Ideal Scenarios

- **Complex problem decomposition** - Break large tasks into specialized subtasks
- **Diverse expertise requirements** - Different domains need different specialists
- **Quality assurance** - Separate agents for creation and validation
- **Scalable workflows** - Add agents as complexity grows

### Consider Alternatives When

- Simple, single-domain tasks
- Latency is critical (each agent adds overhead)
- Budget constraints (multiple LLM calls)

---

## 🌱 Seedling: Basic Multi-Agent Pattern

### The Simplest Multi-Agent Setup

```python
from typing import Dict, Any, List
from dataclasses import dataclass

@dataclass
class AgentMessage:
    """Message passed between agents"""
    sender: str
    content: str
    metadata: Dict[str, Any] = None

class SimpleAgent:
    """Base agent class"""
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role
    
    async def process(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """Process input and return output"""
        raise NotImplementedError

class MultiAgentOrchestrator:
    """Basic orchestrator for multiple agents"""
    
    def __init__(self):
        self.agents: Dict[str, SimpleAgent] = {}
        self.message_history: List[AgentMessage] = []
    
    def register_agent(self, agent: SimpleAgent):
        """Add agent to the system"""
        self.agents[agent.name] = agent
    
    async def route_task(self, task: str) -> str:
        """Route task to appropriate agent"""
        # Simple routing based on keywords
        for name, agent in self.agents.items():
            if agent.role.lower() in task.lower():
                return name
        return list(self.agents.keys())[0]  # Default to first agent
    
    async def execute(self, task: str) -> Dict[str, Any]:
        """Execute task with appropriate agent"""
        agent_name = await self.route_task(task)
        agent = self.agents[agent_name]
        
        result = await agent.process({"task": task})
        
        self.message_history.append(AgentMessage(
            sender=agent_name,
            content=str(result)
        ))
        
        return result
```

---

## 🌿 Growing: Specialized Agent Patterns

### Research + Analysis + Report Pattern

```python
class ResearchAgent(SimpleAgent):
    """Gathers and synthesizes information"""
    
    def __init__(self):
        super().__init__("Researcher", "research")
        self.tools = ["web_search", "document_reader", "database_query"]
    
    async def process(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        topic = input_data.get("task", "")
        
        # Simulate research
        findings = {
            "sources": ["Source A", "Source B", "Source C"],
            "key_points": [
                "Finding 1: Important discovery",
                "Finding 2: Supporting evidence",
                "Finding 3: Counterpoints to consider"
            ],
            "confidence": 0.85
        }
        
        return {
            "research_results": findings,
            "next_step": "analysis"
        }

class AnalysisAgent(SimpleAgent):
    """Analyzes research findings"""
    
    def __init__(self):
        super().__init__("Analyst", "analysis")
    
    async def process(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        research = input_data.get("research_results", {})
        
        analysis = {
            "patterns": ["Pattern A", "Pattern B"],
            "insights": [
                "Insight 1: Correlation discovered",
                "Insight 2: Trend identified"
            ],
            "recommendations": [
                "Recommendation 1: Action to take",
                "Recommendation 2: Further investigation"
            ]
        }
        
        return {
            "research_results": research,
            "analysis_results": analysis,
            "next_step": "report"
        }

class ReportAgent(SimpleAgent):
    """Creates final report from analysis"""
    
    def __init__(self):
        super().__init__("Reporter", "report")
    
    async def process(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        research = input_data.get("research_results", {})
        analysis = input_data.get("analysis_results", {})
        
        report = f"""
# Research Report

## Sources Consulted
{chr(10).join('- ' + s for s in research.get('sources', []))}

## Key Findings
{chr(10).join('- ' + p for p in research.get('key_points', []))}

## Analysis
### Patterns Identified
{chr(10).join('- ' + p for p in analysis.get('patterns', []))}

### Insights
{chr(10).join('- ' + i for i in analysis.get('insights', []))}

## Recommendations
{chr(10).join('- ' + r for r in analysis.get('recommendations', []))}
        """
        
        return {
            "final_report": report,
            "status": "complete"
        }
```

---

## 🌳 Forest: Advanced Orchestration

### Hierarchical Multi-Agent System

```python
from enum import Enum
from typing import Optional

class AgentRole(Enum):
    ORCHESTRATOR = "orchestrator"
    SPECIALIST = "specialist"
    VALIDATOR = "validator"
    COORDINATOR = "coordinator"

class HierarchicalOrchestrator:
    """
    Multi-level agent coordination with:
    - Top-level orchestrator
    - Team coordinators
    - Specialist agents
    - Cross-team validators
    """
    
    def __init__(self):
        self.teams: Dict[str, Dict[str, SimpleAgent]] = {}
        self.coordinators: Dict[str, SimpleAgent] = {}
        self.validators: List[SimpleAgent] = []
    
    def create_team(self, team_name: str, coordinator: SimpleAgent):
        """Create a new team with coordinator"""
        self.teams[team_name] = {}
        self.coordinators[team_name] = coordinator
    
    def add_specialist(self, team_name: str, agent: SimpleAgent):
        """Add specialist to team"""
        if team_name not in self.teams:
            raise ValueError(f"Team {team_name} does not exist")
        self.teams[team_name][agent.name] = agent
    
    def add_validator(self, agent: SimpleAgent):
        """Add cross-team validator"""
        self.validators.append(agent)
    
    async def execute_complex_task(
        self, 
        task: str, 
        require_validation: bool = True
    ) -> Dict[str, Any]:
        """
        Execute task across multiple teams
        """
        results = {}
        
        # Phase 1: Parallel team execution
        for team_name, team_agents in self.teams.items():
            coordinator = self.coordinators[team_name]
            
            # Coordinator delegates to specialists
            team_result = await self._execute_team_task(
                coordinator, 
                team_agents, 
                task
            )
            results[team_name] = team_result
        
        # Phase 2: Cross-team validation
        if require_validation and self.validators:
            for validator in self.validators:
                validation = await validator.process({
                    "results": results,
                    "task": "validate"
                })
                results["validation"] = validation
        
        # Phase 3: Synthesis
        final_result = self._synthesize_results(results)
        
        return final_result
    
    async def _execute_team_task(
        self,
        coordinator: SimpleAgent,
        specialists: Dict[str, SimpleAgent],
        task: str
    ) -> Dict[str, Any]:
        """Execute task within a single team"""
        # Coordinator creates subtasks
        subtasks = await coordinator.process({
            "task": task,
            "action": "decompose"
        })
        
        # Specialists execute subtasks
        specialist_results = {}
        for subtask in subtasks.get("subtasks", []):
            agent_name = subtask.get("assigned_to")
            if agent_name in specialists:
                result = await specialists[agent_name].process(subtask)
                specialist_results[agent_name] = result
        
        # Coordinator synthesizes results
        synthesis = await coordinator.process({
            "action": "synthesize",
            "results": specialist_results
        })
        
        return synthesis
    
    def _synthesize_results(
        self, 
        results: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Combine results from all teams"""
        return {
            "status": "complete",
            "team_results": results,
            "summary": "Multi-agent task completed successfully"
        }
```

---

## 💡 Key Insights

### Agent Communication Patterns

1. **Direct messaging** - Agents communicate point-to-point
2. **Broadcast** - One agent sends to all others
3. **Publish-subscribe** - Agents subscribe to relevant topics
4. **Shared memory** - Agents read/write common state

### Conflict Resolution

When agents disagree:
- **Voting** - Majority wins
- **Weighted consensus** - Based on confidence scores
- **Escalation** - Human or supervisor agent decides
- **Debate** - Agents argue until consensus

---

## ⚡ Quick Win: Start Simple

Begin with a two-agent system:

```python
# Minimal multi-agent setup
creator = CreatorAgent()
critic = CriticAgent()

# Create → Critique → Refine loop
draft = await creator.create(task)
feedback = await critic.review(draft)
final = await creator.refine(draft, feedback)
```

---

## 🔬 Deep Dive: Production Considerations

### Monitoring Multi-Agent Systems

```python
class AgentMonitor:
    """Track multi-agent system health"""
    
    def __init__(self):
        self.metrics = {
            "agent_calls": {},
            "latencies": {},
            "errors": {},
            "token_usage": {}
        }
    
    def log_call(
        self, 
        agent_name: str, 
        latency_ms: float, 
        tokens: int
    ):
        """Log an agent call"""
        if agent_name not in self.metrics["agent_calls"]:
            self.metrics["agent_calls"][agent_name] = 0
            self.metrics["latencies"][agent_name] = []
            self.metrics["token_usage"][agent_name] = 0
        
        self.metrics["agent_calls"][agent_name] += 1
        self.metrics["latencies"][agent_name].append(latency_ms)
        self.metrics["token_usage"][agent_name] += tokens
    
    def get_summary(self) -> Dict[str, Any]:
        """Get monitoring summary"""
        return {
            "total_calls": sum(self.metrics["agent_calls"].values()),
            "avg_latency": self._avg_latency(),
            "total_tokens": sum(self.metrics["token_usage"].values()),
            "by_agent": self.metrics
        }
```

---

## 📖 Related Resources

- [Agent Types](../agents/02-agent-types/) - Foundation for multi-agent design
- [Evaluation & Testing](./02-evaluation/) - Testing multi-agent systems
- [Production Deployment](./03-deployment/) - Scaling multi-agent systems
- [Tool Ecosystems](../tools/03-tool-ecosystems/) - Integration patterns

---

*Built with ❤️ by HUB for learners who want to master AI × Human collaboration*

[← Back to Advanced Topics](./)
