---
title: "🧪 Evaluation & Testing: Agent Quality Assurance"
description: Comprehensive strategies for testing and evaluating AI agents
---

## 🌳 Forest-Level Concept

**Label**: Ensuring AI Agent Quality Through Systematic Testing

Quality assurance for AI agents requires a multi-layered approach: from unit testing individual components to end-to-end evaluation of complex agent behaviors.

## Testing Pyramid for AI Agents

```
                    ┌─────────────┐
                    │  End-to-End │  ← Full workflow testing
                   ╱│   Testing   │╲
                  ╱ └─────────────┘ ╲
                 ╱                   ╲
                ╱  ┌───────────────┐  ╲
               ╱   │  Integration  │   ╲  ← Agent + Tools + LLM
              ╱    │    Testing    │    ╲
             ╱     └───────────────┘     ╲
            ╱                             ╲
           ╱    ┌───────────────────┐      ╲
          ╱     │   Component/Unit  │       ╲  ← Individual functions
         ╱      │      Testing      │        ╲
        ╱       └───────────────────┘         ╲
       └───────────────────────────────────────┘
```

---

## 🌱 Seedling: Basic Agent Testing

### Unit Testing Agent Components

```python
import pytest
from unittest.mock import Mock, AsyncMock
from typing import Dict, Any

# Agent under test
class SimpleAgent:
    def __init__(self, llm_client):
        self.llm = llm_client
    
    async def process(self, input_text: str) -> str:
        prompt = f"Process this input: {input_text}"
        response = await self.llm.generate(prompt)
        return self.format_response(response)
    
    def format_response(self, response: str) -> str:
        return response.strip().lower()

# Unit tests
class TestSimpleAgent:
    """Unit tests for SimpleAgent"""
    
    @pytest.fixture
    def mock_llm(self):
        """Create mock LLM client"""
        mock = AsyncMock()
        mock.generate.return_value = "  Test Response  "
        return mock
    
    @pytest.fixture
    def agent(self, mock_llm):
        """Create agent with mocked LLM"""
        return SimpleAgent(mock_llm)
    
    def test_format_response_strips_whitespace(self, agent):
        """Test response formatting"""
        result = agent.format_response("  Hello World  ")
        assert result == "hello world"
    
    def test_format_response_lowercases(self, agent):
        """Test lowercase conversion"""
        result = agent.format_response("UPPERCASE")
        assert result == "uppercase"
    
    @pytest.mark.asyncio
    async def test_process_calls_llm(self, agent, mock_llm):
        """Test LLM is called correctly"""
        await agent.process("test input")
        
        mock_llm.generate.assert_called_once()
        call_args = mock_llm.generate.call_args[0][0]
        assert "test input" in call_args
    
    @pytest.mark.asyncio
    async def test_process_formats_response(self, agent):
        """Test full processing pipeline"""
        result = await agent.process("test")
        assert result == "test response"
```

---

## 🌿 Growing: Integration Testing

### Testing Agent + Tool Integration

```python
import pytest
from dataclasses import dataclass
from typing import List

@dataclass
class ToolCall:
    """Record of a tool call"""
    name: str
    args: Dict[str, Any]
    result: Any

class ToolTracker:
    """Track tool calls for testing"""
    
    def __init__(self):
        self.calls: List[ToolCall] = []
    
    def record(self, name: str, args: Dict, result: Any):
        self.calls.append(ToolCall(name, args, result))
    
    def get_calls(self, name: str) -> List[ToolCall]:
        return [c for c in self.calls if c.name == name]

class TestAgentToolIntegration:
    """Integration tests for agent + tools"""
    
    @pytest.fixture
    def tool_tracker(self):
        return ToolTracker()
    
    @pytest.fixture
    def search_tool(self, tool_tracker):
        """Mock search tool with tracking"""
        async def search(query: str) -> List[str]:
            results = [f"Result for: {query}"]
            tool_tracker.record("search", {"query": query}, results)
            return results
        return search
    
    @pytest.fixture
    def calculator_tool(self, tool_tracker):
        """Mock calculator tool with tracking"""
        def calculate(expression: str) -> float:
            result = eval(expression)  # Simplified for example
            tool_tracker.record("calculator", {"expression": expression}, result)
            return result
        return calculate
    
    @pytest.mark.asyncio
    async def test_agent_uses_search_tool(
        self, 
        search_tool, 
        tool_tracker
    ):
        """Test agent correctly uses search tool"""
        agent = ResearchAgent(tools=[search_tool])
        
        await agent.research("climate change")
        
        search_calls = tool_tracker.get_calls("search")
        assert len(search_calls) >= 1
        assert "climate" in search_calls[0].args["query"].lower()
    
    @pytest.mark.asyncio
    async def test_agent_chains_tools(
        self, 
        search_tool, 
        calculator_tool,
        tool_tracker
    ):
        """Test agent chains multiple tools"""
        agent = AnalysisAgent(tools=[search_tool, calculator_tool])
        
        await agent.analyze("calculate average of search results")
        
        assert len(tool_tracker.calls) >= 2
        tool_names = [c.name for c in tool_tracker.calls]
        assert "search" in tool_names
        assert "calculator" in tool_names
```

---

## 🌳 Forest: Behavioral Evaluation

### LLM Output Quality Metrics

```python
from dataclasses import dataclass
from typing import List, Callable
import re

@dataclass
class EvaluationResult:
    """Result of an evaluation"""
    metric_name: str
    score: float
    details: str
    passed: bool

class AgentEvaluator:
    """Comprehensive agent evaluation"""
    
    def __init__(self):
        self.metrics: List[Callable] = []
    
    def add_metric(self, metric_fn: Callable):
        """Add evaluation metric"""
        self.metrics.append(metric_fn)
    
    async def evaluate(
        self, 
        agent, 
        test_cases: List[Dict[str, Any]]
    ) -> List[EvaluationResult]:
        """Run all metrics on test cases"""
        all_results = []
        
        for test_case in test_cases:
            input_data = test_case["input"]
            expected = test_case.get("expected")
            
            output = await agent.process(input_data)
            
            for metric in self.metrics:
                result = metric(output, expected, test_case)
                all_results.append(result)
        
        return all_results

# Built-in evaluation metrics
def relevance_score(
    output: str, 
    expected: str, 
    test_case: Dict
) -> EvaluationResult:
    """Check if output is relevant to input"""
    keywords = test_case.get("keywords", [])
    matches = sum(1 for k in keywords if k.lower() in output.lower())
    score = matches / len(keywords) if keywords else 1.0
    
    return EvaluationResult(
        metric_name="relevance",
        score=score,
        details=f"Matched {matches}/{len(keywords)} keywords",
        passed=score >= 0.7
    )

def format_compliance(
    output: str, 
    expected: str, 
    test_case: Dict
) -> EvaluationResult:
    """Check output format compliance"""
    expected_format = test_case.get("format", "text")
    
    checks = {
        "json": lambda x: x.strip().startswith("{"),
        "markdown": lambda x: "#" in x or "*" in x,
        "list": lambda x: "\n-" in x or "\n•" in x,
        "text": lambda x: True
    }
    
    check_fn = checks.get(expected_format, checks["text"])
    passed = check_fn(output)
    
    return EvaluationResult(
        metric_name="format_compliance",
        score=1.0 if passed else 0.0,
        details=f"Expected {expected_format} format",
        passed=passed
    )

def safety_check(
    output: str, 
    expected: str, 
    test_case: Dict
) -> EvaluationResult:
    """Check for unsafe content"""
    unsafe_patterns = [
        r"password",
        r"api.key",
        r"secret",
        r"\b\d{16}\b",  # Credit card pattern
    ]
    
    violations = []
    for pattern in unsafe_patterns:
        if re.search(pattern, output, re.IGNORECASE):
            violations.append(pattern)
    
    return EvaluationResult(
        metric_name="safety",
        score=0.0 if violations else 1.0,
        details=f"Violations: {violations}" if violations else "No issues",
        passed=len(violations) == 0
    )
```

### Golden Dataset Testing

```python
import json
from pathlib import Path

class GoldenDatasetEvaluator:
    """
    Evaluate against curated golden datasets
    """
    
    def __init__(self, dataset_path: str):
        self.dataset_path = Path(dataset_path)
        self.test_cases = self._load_dataset()
    
    def _load_dataset(self) -> List[Dict]:
        """Load golden test cases"""
        with open(self.dataset_path) as f:
            return json.load(f)
    
    async def run_evaluation(
        self, 
        agent,
        threshold: float = 0.8
    ) -> Dict[str, Any]:
        """
        Run full golden dataset evaluation
        """
        results = {
            "total_cases": len(self.test_cases),
            "passed": 0,
            "failed": 0,
            "scores": [],
            "failures": []
        }
        
        for i, test_case in enumerate(self.test_cases):
            input_text = test_case["input"]
            expected_output = test_case["expected_output"]
            
            try:
                actual_output = await agent.process(input_text)
                score = self._calculate_similarity(
                    actual_output, 
                    expected_output
                )
                
                results["scores"].append(score)
                
                if score >= threshold:
                    results["passed"] += 1
                else:
                    results["failed"] += 1
                    results["failures"].append({
                        "case_id": i,
                        "input": input_text,
                        "expected": expected_output,
                        "actual": actual_output,
                        "score": score
                    })
                    
            except Exception as e:
                results["failed"] += 1
                results["failures"].append({
                    "case_id": i,
                    "error": str(e)
                })
        
        results["pass_rate"] = results["passed"] / results["total_cases"]
        results["avg_score"] = sum(results["scores"]) / len(results["scores"])
        
        return results
    
    def _calculate_similarity(
        self, 
        actual: str, 
        expected: str
    ) -> float:
        """Calculate semantic similarity between outputs"""
        # Simplified - in production use embeddings
        actual_words = set(actual.lower().split())
        expected_words = set(expected.lower().split())
        
        intersection = actual_words & expected_words
        union = actual_words | expected_words
        
        return len(intersection) / len(union) if union else 0.0
```

---

## 💡 Key Insights

### What to Test

1. **Correctness** - Does the agent produce accurate outputs?
2. **Consistency** - Does it behave the same given similar inputs?
3. **Robustness** - Does it handle edge cases gracefully?
4. **Safety** - Does it avoid harmful outputs?
5. **Performance** - Does it meet latency/cost requirements?

### Testing Strategies

| Strategy | When to Use | Cost |
|----------|-------------|------|
| Unit tests | Every change | Low |
| Integration tests | Feature changes | Medium |
| Golden set tests | Before release | Medium |
| LLM-as-judge | Complex outputs | High |
| Human evaluation | Critical paths | Very High |

---

## ⚡ Quick Win: Start with Assertions

```python
# Add simple assertions to catch obvious failures
async def test_agent_basic():
    agent = MyAgent()
    result = await agent.process("Hello")
    
    # Basic sanity checks
    assert result is not None
    assert len(result) > 0
    assert len(result) < 10000  # Reasonable length
    assert "error" not in result.lower()
```

---

## 🔬 Deep Dive: LLM-as-Judge Evaluation

```python
class LLMJudge:
    """Use an LLM to evaluate agent outputs"""
    
    def __init__(self, judge_llm):
        self.judge = judge_llm
    
    async def evaluate(
        self,
        input_text: str,
        output_text: str,
        criteria: List[str]
    ) -> Dict[str, Any]:
        """
        Have LLM judge the output quality
        """
        prompt = f"""
You are an expert evaluator. Evaluate the following AI agent output.

INPUT: {input_text}

OUTPUT: {output_text}

CRITERIA TO EVALUATE:
{chr(10).join(f'- {c}' for c in criteria)}

For each criterion, provide:
1. A score from 1-5
2. A brief explanation

Format your response as JSON:
{{
    "criteria_name": {{
        "score": <1-5>,
        "explanation": "<brief explanation>"
    }}
}}
"""
        
        judgment = await self.judge.generate(prompt)
        return json.loads(judgment)
```

---

## 📖 Related Resources

- [Multi-Agent Systems](./01-multi-agent-systems/) - Testing multi-agent setups
- [Production Deployment](./03-deployment/) - Monitoring in production
- [Agent Development Kits](../agents/01-adk-overview/) - Testing framework integration

---

*Built with ❤️ by HUB for learners who want to master AI × Human collaboration*

[← Back to Advanced Topics](./)
