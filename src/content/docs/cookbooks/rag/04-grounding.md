---
title: "⚓ Grounding: Keeping AI Agents Accurate and Reliable"
---

## 🌳 Flourishing Concept

**Label**: Anchoring AI in Reality

**Grounding** is the practice of anchoring AI agent responses in factual, verifiable information. It's the difference between an agent that "sounds confident" and one that is actually accurate and reliable.

## What is Grounding?

### The Hallucination Problem

```
Without Grounding:                With Grounding:
┌─────────────┐                  ┌─────────────┐
│    Query    │                  │    Query    │
└──────┬──────┘                  └──────┬──────┘
       │                                │
       ▼                                ▼
┌─────────────┐                  ┌─────────────┐
│     LLM     │                  │ Retrieval   │
│   Memory    │                  │   System    │
└──────┬──────┘                  └──────┬──────┘
       │                                │
       │ May hallucinate                ▼
       │                          ┌─────────────┐
       ▼                          │   Facts &   │
┌─────────────┐                  │   Sources   │
│  Response   │                  └──────┬──────┘
│ (Unverified)│                         │
└─────────────┘                         ▼
                                 ┌─────────────┐
                                 │     LLM     │
                                 │  + Context  │
                                 └──────┬──────┘
                                        │
                                        ▼
                                 ┌─────────────┐
                                 │  Response   │
                                 │  (Grounded) │
                                 └─────────────┘
```

### Why Grounding Matters

**Ungrounded Response**:
```
User: What's our company's return policy?
Agent: I believe you have 30 days to return items.
       (May be incorrect)
```

**Grounded Response**:
```
User: What's our company's return policy?
Agent: According to the Returns Policy document (v2.3, updated Jan 2024),
       customers have 45 days to return items with receipt for full refund.
       Source: company_policies/returns.pdf, page 2
       (Factually accurate with citation)
```

## 💡 Common Grounding Steps

### Step 1: Query Understanding

```python
class GroundedAgent:
    """
    Agent with grounding capabilities
    """
    async def process_query(self, user_query: str) -> dict:
        """
        Process query with grounding
        """
        # Step 1: Understand what information is needed
        query_analysis = await self.analyze_query(user_query)
        
        return {
            'intent': query_analysis['intent'],
            'entities': query_analysis['entities'],
            'information_needed': query_analysis['facts_required']
        }
    
    async def analyze_query(self, query: str) -> dict:
        """
        Determine what facts are needed to answer
        """
        prompt = f"""
        Analyze this query and identify:
        1. User's intent
        2. Key entities mentioned
        3. What factual information is needed to answer accurately
        
        Query: {query}
        
        Respond in JSON format.
        """
        
        response = await self.llm.generate(prompt)
        return json.loads(response)
```

### Step 2: Information Retrieval

```python
async def retrieve_grounding_information(self, query_analysis: dict) -> dict:
    """
    Retrieve factual information to ground the response
    """
    grounding_sources = []
    
    # Retrieve from authoritative sources
    if query_analysis['intent'] == 'policy_question':
        # Get from policy documents
        policy_info = await self.policy_db.search(
            query_analysis['entities']
        )
        grounding_sources.append({
            'type': 'policy',
            'content': policy_info,
            'authority': 'high',
            'updated': policy_info['last_modified']
        })
    
    elif query_analysis['intent'] == 'factual_question':
        # Get from knowledge base
        facts = await self.knowledge_base.search(
            query_analysis['information_needed']
        )
        grounding_sources.append({
            'type': 'knowledge_base',
            'content': facts,
            'authority': 'medium',
            'sources': facts['references']
        })
    
    # Verify information freshness
    grounding_sources = await self.verify_freshness(grounding_sources)
    
    return {
        'sources': grounding_sources,
        'confidence': self.calculate_confidence(grounding_sources)
    }
```

### Step 3: Response Generation with Citations

```python
async def generate_grounded_response(self, 
                                    query: str, 
                                    grounding: dict) -> str:
    """
    Generate response grounded in retrieved facts
    """
    # Build context from grounding sources
    context = self.build_context(grounding['sources'])
    
    # Generate with explicit grounding requirement
    prompt = f"""
    Answer the user's question using ONLY the provided sources.
    You MUST cite your sources using [Source N] notation.
    If the answer is not in the sources, say so explicitly.
    
    Question: {query}
    
    Authoritative Sources:
    {context}
    
    Requirements:
    1. Only use information from sources above
    2. Cite every factual claim with [Source N]
    3. If uncertain, state your confidence level
    4. If answer not found, say "I don't have that information"
    
    Response:
    """
    
    response = await self.llm.generate(prompt)
    
    # Verify citations
    verified_response = await self.verify_citations(response, grounding)
    
    return verified_response

def build_context(self, sources: List[dict]) -> str:
    """
    Format sources for LLM context
    """
    context_parts = []
    for i, source in enumerate(sources, 1):
        context_parts.append(f"""
        [Source {i}]
        Type: {source['type']}
        Authority: {source['authority']}
        Content: {source['content']}
        Last Updated: {source.get('updated', 'N/A')}
        """)
    
    return '\n\n'.join(context_parts)
```

### Step 4: Verification and Validation

```python
async def verify_citations(self, response: str, grounding: dict) -> dict:
    """
    Verify that citations in response match sources
    """
    # Extract citations from response
    citations = self.extract_citations(response)
    
    # Verify each claim
    verification_results = []
    for citation in citations:
        claim = citation['claim']
        source_num = citation['source_number']
        
        # Check if claim is supported by cited source
        is_supported = await self.verify_claim_in_source(
            claim,
            grounding['sources'][source_num - 1]
        )
        
        verification_results.append({
            'claim': claim,
            'source': source_num,
            'supported': is_supported,
            'confidence': is_supported['confidence']
        })
    
    # Flag unsupported claims
    unsupported = [v for v in verification_results if not v['supported']]
    
    if unsupported:
        return {
            'response': response,
            'status': 'needs_review',
            'unsupported_claims': unsupported,
            'recommendation': 'Remove or rephrase unsupported claims'
        }
    
    return {
        'response': response,
        'status': 'verified',
        'all_claims_supported': True,
        'sources_used': len(set(c['source'] for c in citations))
    }
```

## 🔬 Deep Dive: Grounding Techniques

### 1. Source Authority Hierarchy

```python
class SourceAuthority:
    """
    Manage source authority levels
    """
    AUTHORITY_LEVELS = {
        'primary': {
            'priority': 1,
            'description': 'Official company documents, policies, databases',
            'examples': ['policy_docs', 'product_specs', 'legal_docs']
        },
        'secondary': {
            'priority': 2,
            'description': 'Approved knowledge bases, documentation',
            'examples': ['wiki', 'faq', 'training_materials']
        },
        'tertiary': {
            'priority': 3,
            'description': 'Team notes, chat history, emails',
            'examples': ['slack', 'email', 'notes']
        },
        'external': {
            'priority': 4,
            'description': 'External sources, web search',
            'examples': ['web_search', 'public_apis']
        }
    }
    
    @staticmethod
    def prioritize_sources(sources: List[dict]) -> List[dict]:
        """
        Sort sources by authority level
        """
        def get_priority(source):
            source_type = source['type']
            for level, info in SourceAuthority.AUTHORITY_LEVELS.items():
                if source_type in info['examples']:
                    return info['priority']
            return 5  # Unknown sources lowest priority
        
        return sorted(sources, key=get_priority)


# Usage
sources = [
    {'type': 'web_search', 'content': 'Public information'},
    {'type': 'policy_docs', 'content': 'Official policy'},
    {'type': 'slack', 'content': 'Team discussion'}
]

prioritized = SourceAuthority.prioritize_sources(sources)
# Result: policy_docs → slack → web_search
```

### 2. Temporal Grounding

```python
class TemporalGrounding:
    """
    Ensure information is current
    """
    def __init__(self, freshness_threshold_days: int = 90):
        self.threshold = freshness_threshold_days
    
    async def check_freshness(self, source: dict) -> dict:
        """
        Verify information currency
        """
        last_updated = source.get('updated')
        if not last_updated:
            return {
                'fresh': False,
                'reason': 'No update timestamp',
                'recommendation': 'Verify manually before using'
            }
        
        age_days = (datetime.now() - last_updated).days
        
        if age_days > self.threshold:
            # Try to find updated version
            updated_source = await self.find_updated_version(source)
            if updated_source:
                return {
                    'fresh': True,
                    'updated_source': updated_source,
                    'note': f'Found newer version ({updated_source["updated"]})'
                }
            
            return {
                'fresh': False,
                'age_days': age_days,
                'recommendation': f'Information is {age_days} days old. Consider updating.'
            }
        
        return {
            'fresh': True,
            'age_days': age_days
        }


# Usage
temporal = TemporalGrounding(freshness_threshold_days=30)

source = {
    'content': 'Return policy: 30 days',
    'updated': datetime(2023, 1, 1)
}

freshness = await temporal.check_freshness(source)
if not freshness['fresh']:
    print(f"Warning: {freshness['recommendation']}")
```

### 3. Multi-Source Verification

```python
class MultiSourceVerification:
    """
    Cross-verify information across sources
    """
    async def verify_fact(self, fact: str, sources: List[dict]) -> dict:
        """
        Check if fact is supported by multiple sources
        """
        supporting_sources = []
        conflicting_sources = []
        
        for source in sources:
            verification = await self.check_fact_in_source(fact, source)
            
            if verification['supports']:
                supporting_sources.append(source)
            elif verification['conflicts']:
                conflicting_sources.append(source)
        
        # Determine confidence based on agreement
        if len(supporting_sources) >= 2 and not conflicting_sources:
            confidence = 'high'
        elif len(supporting_sources) == 1 and not conflicting_sources:
            confidence = 'medium'
        elif conflicting_sources:
            confidence = 'low'
        else:
            confidence = 'none'
        
        return {
            'fact': fact,
            'confidence': confidence,
            'supporting_sources': len(supporting_sources),
            'conflicting_sources': len(conflicting_sources),
            'recommendation': self.get_recommendation(confidence, conflicting_sources)
        }
    
    def get_recommendation(self, confidence: str, conflicts: List) -> str:
        """
        Provide recommendation based on verification
        """
        if confidence == 'high':
            return 'Fact verified across multiple sources. Safe to use.'
        elif confidence == 'medium':
            return 'Fact supported by one source. Consider finding additional confirmation.'
        elif conflicts:
            return 'Conflicting information found. Investigate discrepancy before using.'
        else:
            return 'Fact not found in sources. Do not use.'
```

## ⚡ Quick Win: Basic Grounding System

### 15-Minute Implementation

```python
class SimpleGrounding:
    """
    Lightweight grounding for quick implementation
    """
    def __init__(self, knowledge_base: dict):
        self.kb = knowledge_base
    
    def answer_grounded(self, question: str) -> dict:
        """
        Answer with grounding
        """
        # Search knowledge base
        relevant_info = self.search_kb(question)
        
        if not relevant_info:
            return {
                'answer': "I don't have information about that in my knowledge base.",
                'grounded': True,
                'sources': []
            }
        
        # Generate answer from sources only
        answer = self.generate_from_sources(question, relevant_info)
        
        return {
            'answer': answer,
            'grounded': True,
            'sources': [s['id'] for s in relevant_info],
            'confidence': len(relevant_info) / 3  # Simple confidence metric
        }
    
    def search_kb(self, question: str) -> List[dict]:
        """
        Simple keyword search
        """
        keywords = question.lower().split()
        results = []
        
        for doc_id, doc in self.kb.items():
            content_lower = doc['content'].lower()
            matches = sum(1 for kw in keywords if kw in content_lower)
            
            if matches > 0:
                results.append({
                    'id': doc_id,
                    'content': doc['content'],
                    'relevance': matches / len(keywords)
                })
        
        return sorted(results, key=lambda x: x['relevance'], reverse=True)[:3]
    
    def generate_from_sources(self, question: str, sources: List[dict]) -> str:
        """
        Create answer from sources with citations
        """
        answer_parts = []
        for i, source in enumerate(sources, 1):
            # Extract relevant sentence
            relevant = self.extract_relevant_sentence(question, source['content'])
            if relevant:
                answer_parts.append(f"{relevant} [Source {i}]")
        
        return ' '.join(answer_parts) if answer_parts else "No specific information found."


# Usage
kb = {
    'policy_1': {
        'content': 'Customers have 45 days to return items with receipt.',
        'type': 'policy'
    },
    'policy_2': {
        'content': 'Refunds are processed within 5-7 business days.',
        'type': 'policy'
    }
}

grounding = SimpleGrounding(kb)
result = grounding.answer_grounded("What is the return policy?")

print(result['answer'])
print(f"Sources used: {result['sources']}")
print(f"Confidence: {result['confidence']:.2f}")
```

## 🎯 Real-World Grounding Patterns

### Pattern 1: Customer Support

```python
class CustomerSupportGrounding:
    """
    Grounded customer support agent
    """
    def __init__(self):
        self.policy_db = PolicyDatabase()
        self.order_db = OrderDatabase()
        self.product_db = ProductDatabase()
    
    async def answer_customer(self, question: str, customer_id: str) -> dict:
        """
        Answer with grounding in customer-specific data
        """
        # Get customer context
        customer_info = await self.order_db.get_customer(customer_id)
        
        # Determine question type
        question_type = await self.classify_question(question)
        
        # Ground in appropriate source
        if question_type == 'order_status':
            grounding = await self.order_db.get_order_details(
                customer_info['recent_orders'][0]
            )
            source_type = 'order_database'
        
        elif question_type == 'policy':
            grounding = await self.policy_db.search(question)
            source_type = 'policy_document'
        
        elif question_type == 'product':
            grounding = await self.product_db.search(question)
            source_type = 'product_catalog'
        
        # Generate grounded response
        response = await self.generate_response(
            question,
            grounding,
            source_type
        )
        
        return {
            'response': response,
            'grounded_in': source_type,
            'customer_specific': True,
            'verifiable': True
        }
```

### Pattern 2: Technical Documentation

```python
class TechnicalDocGrounding:
    """
    Grounded technical documentation assistant
    """
    async def answer_technical(self, question: str) -> dict:
        """
        Answer technical questions with code examples and docs
        """
        # Search official documentation
        doc_results = await self.search_official_docs(question)
        
        # Search code examples
        code_results = await self.search_code_examples(question)
        
        # Prioritize official docs
        sources = self.prioritize([
            {'type': 'official_docs', 'results': doc_results, 'priority': 1},
            {'type': 'code_examples', 'results': code_results, 'priority': 2}
        ])
        
        # Generate with citations and code examples
        response = await self.generate_technical_response(question, sources)
        
        return {
            'response': response,
            'documentation_links': [s['url'] for s in doc_results],
            'code_examples': [s['code'] for s in code_results],
            'api_version': sources[0].get('version', 'latest')
        }
```

## 🎯 Key Takeaways

- **Grounding prevents hallucination** by anchoring in facts
- **Source authority matters** - prioritize official sources
- **Citations are essential** - every claim needs a source
- **Verify freshness** - ensure information is current
- **Multi-source verification** builds confidence
- **Explicit limitations** - admit when information isn't available

## Best Practices

### 1. Always Provide Sources
```python
# ✅ Good: With citation
"Returns accepted within 45 days [Policy Doc, Section 3.1]"

# ❌ Bad: No citation
"Returns accepted within 45 days"
```

### 2. Admit Limitations
```python
# ✅ Good: Honest about gaps
"I found information about X and Y, but I don't have data about Z in my sources."

# ❌ Bad: Guessing
"Z is probably similar to X..."
```

### 3. Show Confidence Levels
```python
# ✅ Good: Transparent confidence
"Based on 3 consistent sources: [High confidence]"
"Based on 1 source only: [Medium confidence]"

# ❌ Bad: No confidence indicator
"The answer is..."
```

## Next Steps

You've completed the RAG section! Continue to:
- [Agent Development Kits](../agents/01-adk-overview.md) for agent implementation
- [Tool Ecosystems](../tools/03-tool-ecosystems.md) for integration patterns
- [Production Deployment](../advanced/03-deployment.md) for scaling

---

💡 **Remember**: Grounding is the difference between an agent that sounds good and one that is actually reliable.
