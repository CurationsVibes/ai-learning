# 🎯 Agentic RAG: Active Reasoning in Knowledge Search

## 🌿 Growing Concept

**Label**: From Passive Retrieval to Active Reasoning

Agentic RAG transforms agents from passive recipients of retrieved data into active, reasoning participants in the search for knowledge. Instead of blindly accepting the first retrieval results, agents can reason about what they need, reformulate queries, and validate information.

## What is Agentic RAG?

### The Evolution

```
Traditional RAG:           Agentic RAG:
┌──────────┐              ┌──────────┐
│  Query   │              │  Query   │
└────┬─────┘              └────┬─────┘
     │                         │
     ▼                         ▼
┌──────────┐              ┌──────────┐
│ Retrieve │              │  Analyze │◄─┐
└────┬─────┘              │   Need   │  │
     │                    └────┬─────┘  │
     │                         │        │
     ▼                         ▼        │
┌──────────┐              ┌──────────┐ │
│ Generate │              │ Retrieve │ │
└──────────┘              └────┬─────┘ │
                               │        │
                               ▼        │
                          ┌──────────┐  │
                          │ Validate │  │
                          └────┬─────┘  │
                               │        │
                          ┌────▼─────┐  │
                          │Sufficient?├──┘
                          └────┬─────┘ No
                               │ Yes
                               ▼
                          ┌──────────┐
                          │ Generate │
                          └──────────┘
```

## 💡 Key Capabilities

### 1. Query Decomposition

Breaking complex queries into manageable sub-queries:

```python
class AgenticRetriever:
    """
    Agentic retrieval system with reasoning capabilities
    """
    def __init__(self, vector_store, llm):
        self.vector_store = vector_store
        self.llm = llm
        self.reasoning_engine = ReasoningEngine(llm)
    
    async def decompose_query(self, complex_query: str) -> List[str]:
        """
        Break down complex query into sub-queries
        """
        decomposition_prompt = f"""
        Break down this complex question into 3-5 simpler sub-questions
        that can be answered independently:
        
        Question: {complex_query}
        
        Sub-questions (one per line):
        """
        
        response = await self.llm.generate(decomposition_prompt)
        sub_queries = [q.strip() for q in response.strip().split('\n') if q.strip()]
        
        return sub_queries
    
    async def retrieve_for_subquery(self, sub_query: str) -> List[dict]:
        """
        Retrieve documents for a single sub-query
        """
        # Multiple retrieval strategies
        results = []
        
        # Strategy 1: Direct semantic search
        semantic_results = await self.vector_store.search(sub_query, top_k=3)
        results.extend(semantic_results)
        
        # Strategy 2: Reformulated query
        reformulated = await self.reformulate_query(sub_query)
        if reformulated != sub_query:
            alt_results = await self.vector_store.search(reformulated, top_k=2)
            results.extend(alt_results)
        
        # Deduplicate and rank
        return self.deduplicate_and_rank(results)
    
    async def reformulate_query(self, query: str) -> str:
        """
        Reformulate query for better retrieval
        """
        prompt = f"""
        Reformulate this query to improve search results.
        Use synonyms and related terms:
        
        Original: {query}
        Reformulated:
        """
        
        return await self.llm.generate(prompt)


# Example usage
agentic = AgenticRetriever(vector_store, llm)

# Complex query that needs decomposition
complex_query = """
How does our company's return policy compare to industry standards,
and what are the financial implications of extending the return window?
"""

# Agent breaks it down
sub_queries = await agentic.decompose_query(complex_query)
# Result: 
# 1. "What is our company's current return policy?"
# 2. "What are typical return policies in our industry?"
# 3. "What are the costs associated with product returns?"
# 4. "How does return window length affect return rates?"
```

### 2. Self-Reflection and Validation

Agents validate retrieved information quality:

```python
class SelfReflectingRAG:
    """
    RAG system that validates its own retrievals
    """
    async def retrieve_with_validation(self, query: str) -> dict:
        """
        Retrieve and validate information quality
        """
        # Initial retrieval
        results = await self.vector_store.search(query, top_k=5)
        
        # Self-reflection: Are results relevant?
        validation = await self.validate_results(query, results)
        
        if validation['confidence'] < 0.7:
            # Results not good enough, try different approach
            results = await self.advanced_retrieval(query, validation['issues'])
        
        return {
            "results": results,
            "confidence": validation['confidence'],
            "reasoning": validation['reasoning']
        }
    
    async def validate_results(self, query: str, results: List[dict]) -> dict:
        """
        Agent validates retrieval quality
        """
        validation_prompt = f"""
        Query: {query}
        
        Retrieved documents:
        {self.format_results(results)}
        
        Evaluate:
        1. Do these documents answer the query? (Yes/No/Partially)
        2. What's missing?
        3. Confidence score (0-1):
        
        Respond in JSON format.
        """
        
        response = await self.llm.generate(validation_prompt)
        validation = json.loads(response)
        
        return {
            'confidence': validation.get('confidence', 0),
            'issues': validation.get('missing', []),
            'reasoning': validation.get('reasoning', '')
        }
    
    async def advanced_retrieval(self, query: str, issues: List[str]) -> List[dict]:
        """
        Try alternative retrieval strategies based on identified issues
        """
        strategies = []
        
        if "specific numbers" in str(issues):
            strategies.append("numeric_search")
        
        if "recent information" in str(issues):
            strategies.append("time_filtered_search")
        
        if "comparative data" in str(issues):
            strategies.append("comparative_search")
        
        # Execute strategies
        all_results = []
        for strategy in strategies:
            results = await self.execute_strategy(strategy, query)
            all_results.extend(results)
        
        return self.rank_and_merge(all_results)
```

### 3. Iterative Refinement

Agents refine their search based on intermediate results:

```python
class IterativeRAG:
    """
    RAG that iteratively refines its knowledge gathering
    """
    async def iterative_search(self, query: str, max_iterations: int = 3) -> dict:
        """
        Iteratively gather and refine information
        """
        knowledge = []
        current_query = query
        
        for iteration in range(max_iterations):
            # Retrieve new information
            results = await self.vector_store.search(current_query, top_k=3)
            knowledge.extend(results)
            
            # Analyze knowledge gaps
            analysis = await self.analyze_knowledge_state(query, knowledge)
            
            if analysis['is_sufficient']:
                break
            
            # Generate refined query for next iteration
            current_query = await self.generate_followup_query(
                original_query=query,
                current_knowledge=knowledge,
                gaps=analysis['gaps']
            )
            
            print(f"Iteration {iteration + 1}: Searching for: {current_query}")
        
        return {
            "knowledge": knowledge,
            "iterations": iteration + 1,
            "final_confidence": analysis['confidence']
        }
    
    async def analyze_knowledge_state(self, query: str, knowledge: List[dict]) -> dict:
        """
        Determine if we have enough information
        """
        analysis_prompt = f"""
        Original question: {query}
        
        Information gathered so far:
        {self.summarize_knowledge(knowledge)}
        
        Analysis:
        1. Can we answer the original question? (Yes/No/Partially)
        2. What critical information is still missing?
        3. Confidence level (0-1):
        
        Respond in JSON.
        """
        
        response = await self.llm.generate(analysis_prompt)
        analysis = json.loads(response)
        
        return {
            'is_sufficient': analysis.get('can_answer') == 'Yes',
            'gaps': analysis.get('missing', []),
            'confidence': analysis.get('confidence', 0)
        }
    
    async def generate_followup_query(self, original_query: str, 
                                     current_knowledge: List[dict],
                                     gaps: List[str]) -> str:
        """
        Generate refined query to fill knowledge gaps
        """
        prompt = f"""
        Original question: {original_query}
        
        We already know:
        {self.summarize_knowledge(current_knowledge)}
        
        What we're still missing:
        {', '.join(gaps)}
        
        Generate a focused search query to find the missing information:
        """
        
        return await self.llm.generate(prompt)
```

## 🔬 Deep Dive: Multi-Strategy Retrieval

### Intelligent Strategy Selection

```python
class MultiStrategyAgenticRAG:
    """
    Agentic RAG that selects optimal retrieval strategies
    """
    def __init__(self):
        self.strategies = {
            'semantic': SemanticSearch(),
            'keyword': KeywordSearch(),
            'hybrid': HybridSearch(),
            'graph': GraphSearch(),
            'temporal': TemporalSearch()
        }
    
    async def adaptive_retrieve(self, query: str) -> List[dict]:
        """
        Dynamically select and combine retrieval strategies
        """
        # Analyze query characteristics
        query_analysis = await self.analyze_query(query)
        
        # Select appropriate strategies
        selected_strategies = self.select_strategies(query_analysis)
        
        # Execute strategies in parallel
        results = await asyncio.gather(*[
            self.execute_strategy(strategy, query)
            for strategy in selected_strategies
        ])
        
        # Intelligently merge results
        merged = await self.intelligent_merge(results, query_analysis)
        
        return merged
    
    async def analyze_query(self, query: str) -> dict:
        """
        Understand query intent and characteristics
        """
        analysis_prompt = f"""
        Analyze this query:
        "{query}"
        
        Determine:
        1. Intent: [factual, comparative, analytical, procedural]
        2. Temporal aspect: [recent, historical, timeless]
        3. Complexity: [simple, moderate, complex]
        4. Domain: [general, technical, specific]
        
        JSON response:
        """
        
        response = await self.llm.generate(analysis_prompt)
        return json.loads(response)
    
    def select_strategies(self, analysis: dict) -> List[str]:
        """
        Choose optimal strategies based on query analysis
        """
        strategies = ['semantic']  # Always include semantic
        
        if analysis['temporal'] == 'recent':
            strategies.append('temporal')
        
        if analysis['complexity'] == 'complex':
            strategies.extend(['hybrid', 'graph'])
        
        if 'technical' in analysis['domain']:
            strategies.append('keyword')
        
        return strategies
    
    async def intelligent_merge(self, results_by_strategy: List[List[dict]], 
                               analysis: dict) -> List[dict]:
        """
        Merge results with strategy-aware ranking
        """
        # Weight strategies based on query analysis
        weights = self.calculate_strategy_weights(analysis)
        
        # Combine with weighted scoring
        scored_docs = {}
        for strategy_name, results in zip(self.strategies.keys(), results_by_strategy):
            weight = weights.get(strategy_name, 1.0)
            for rank, doc in enumerate(results):
                doc_id = doc['id']
                score = weight * (1 / (rank + 1))
                scored_docs[doc_id] = scored_docs.get(doc_id, 0) + score
        
        # Return top-ranked documents
        top_docs = sorted(scored_docs.items(), key=lambda x: x[1], reverse=True)
        return [self.get_document(doc_id) for doc_id, _ in top_docs[:5]]
```

## ⚡ Quick Win: Basic Agentic Enhancement

Add simple reasoning to existing RAG:

```python
class EnhancedRAG:
    """Simple agentic improvements to basic RAG"""
    
    async def smart_retrieve(self, query: str) -> dict:
        # 1. Generate alternative phrasings
        alternatives = [
            query,
            await self.rephrase(query),
            await self.expand_with_synonyms(query)
        ]
        
        # 2. Retrieve with each
        all_results = []
        for alt_query in alternatives:
            results = await self.vector_store.search(alt_query, top_k=3)
            all_results.extend(results)
        
        # 3. Deduplicate and rank
        unique_results = self.deduplicate(all_results)
        
        # 4. Validate relevance
        filtered = [r for r in unique_results if await self.is_relevant(query, r)]
        
        return filtered[:5]
```

## 🌳 Advanced: Reasoning Chains

### Chain-of-Thought Retrieval

```python
class ChainOfThoughtRAG:
    """
    RAG with explicit reasoning chains
    """
    async def retrieve_with_reasoning(self, query: str) -> dict:
        """
        Show reasoning process explicitly
        """
        reasoning_chain = []
        
        # Step 1: Understand query
        understanding = await self.understand_query(query)
        reasoning_chain.append({
            "step": "understanding",
            "thought": f"This query is asking for {understanding['intent']}"
        })
        
        # Step 2: Plan retrieval
        plan = await self.plan_retrieval(understanding)
        reasoning_chain.append({
            "step": "planning",
            "thought": f"I'll search for: {plan['search_terms']}"
        })
        
        # Step 3: Execute and evaluate
        results = await self.vector_store.search(plan['search_terms'])
        evaluation = await self.evaluate_results(results, query)
        reasoning_chain.append({
            "step": "evaluation",
            "thought": f"Found {len(results)} results. Relevance: {evaluation['score']}"
        })
        
        # Step 4: Decide if more retrieval needed
        if evaluation['score'] < 0.8:
            reasoning_chain.append({
                "step": "refinement",
                "thought": "Results insufficient, trying alternative approach"
            })
            results = await self.alternative_retrieval(query, evaluation)
        
        return {
            "results": results,
            "reasoning_chain": reasoning_chain
        }
```

## 🎯 Key Takeaways

- **Agentic RAG adds reasoning** to the retrieval process
- **Self-reflection** improves retrieval quality
- **Iterative refinement** fills knowledge gaps
- **Strategy selection** optimizes for query type
- **Transparency** through reasoning chains builds trust

## When to Use Agentic RAG

### Use Traditional RAG When:
- Queries are straightforward
- Speed is critical
- Information is well-organized

### Use Agentic RAG When:
- Queries are complex or ambiguous
- Information quality is paramount
- Multiple perspectives needed
- Knowledge is fragmented

## Next Steps

Continue to [GraphRAG](./03-graph-rag.md) to learn how to leverage relationship graphs for even more sophisticated knowledge retrieval.

---

💡 **Remember**: Agentic RAG is about making your agent an active participant in finding the right information, not just a passive consumer.
