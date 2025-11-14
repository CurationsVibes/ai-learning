# 🧠 Memory Management: Building Context-Aware Agents

## 🌱 Seedling Concept

**Label**: Giving Your Agents a Memory

Imagine talking to someone who forgets everything between conversations. Frustrating, right? Memory management transforms one-shot agents into context-aware assistants that remember user preferences, past interactions, and learned facts.

## What is Memory Management?

Memory management enables agents to:

- 📝 **Store key facts** from conversations
- 🔍 **Retrieve relevant context** when needed
- 🎯 **Personalize experiences** based on history
- 🔄 **Maintain continuity** across sessions

## 💡 GenerateMemories: The Foundation

### How Memory Generation Works

**GenerateMemories** asynchronously extracts and stores key facts from conversation history:

```
User: "I prefer non-stop flights and my dog's name is Fido"
                        │
                        ▼
              [Memory Extraction]
                        │
            ┌───────────┴───────────┐
            ▼                       ▼
    "prefers_nonstop_flights"  "dog_name: Fido"
            │                       │
            └───────────┬───────────┘
                        ▼
                [Memory Storage]
                        │
                        ▼
              [Vector Database]
```

### Basic Implementation

```python
class MemoryManager:
    """
    Manages agent memory for personalized experiences
    """
    def __init__(self, user_id):
        self.user_id = user_id
        self.memory_store = VectorStore()
        self.extractor = MemoryExtractor()
    
    async def generate_memories(self, conversation_history):
        """
        Extract key facts from conversation asynchronously
        """
        # Extract structured memories
        memories = await self.extractor.extract(conversation_history)
        
        # Store each memory with metadata
        for memory in memories:
            await self.memory_store.store(
                user_id=self.user_id,
                content=memory.content,
                category=memory.category,
                timestamp=memory.timestamp,
                confidence=memory.confidence
            )
        
        return memories
```

### Real-World Example: Travel Assistant

```python
class TravelAssistant:
    def __init__(self, user_id):
        self.memory = MemoryManager(user_id)
        self.model = LLM()
    
    async def process_conversation(self, messages):
        """
        Process conversation and extract memories
        """
        # Generate response
        response = await self.model.chat(messages)
        
        # Extract and store memories asynchronously
        await self.memory.generate_memories(messages + [response])
        
        return response
    
    async def book_flight(self, destination):
        """
        Use memories to personalize booking
        """
        # Retrieve relevant memories
        preferences = await self.memory.search(
            query="flight preferences",
            top_k=5
        )
        
        # Build context from memories
        context = f"""
        User preferences:
        - Flight type: {preferences.get('flight_type', 'any')}
        - Seat preference: {preferences.get('seat', 'not specified')}
        - Airline loyalty: {preferences.get('airline', 'none')}
        """
        
        # Make personalized recommendation
        recommendation = await self.model.generate(
            prompt=f"Find flights to {destination}. {context}"
        )
        
        return recommendation


# Usage
assistant = TravelAssistant(user_id="user_123")

# First conversation
await assistant.process_conversation([
    {"role": "user", "content": "I prefer non-stop flights"},
    {"role": "user", "content": "I always fly economy plus"},
])

# Later conversation - agent remembers!
flight = await assistant.book_flight("Tokyo")
# Automatically considers: non-stop preference, economy plus
```

## 🌿 Memory Categories

### Types of Memories to Extract

#### 1. Preferences
```python
{
    "type": "preference",
    "content": "prefers non-stop flights",
    "category": "travel",
    "confidence": 0.95
}
```

#### 2. Facts
```python
{
    "type": "fact",
    "content": "dog's name is Fido",
    "category": "personal",
    "confidence": 1.0
}
```

#### 3. Context
```python
{
    "type": "context",
    "content": "working on machine learning project",
    "category": "professional",
    "confidence": 0.85
}
```

#### 4. Relationships
```python
{
    "type": "relationship",
    "content": "colleague named Sarah in marketing",
    "category": "professional",
    "confidence": 0.90
}
```

## 🔬 Deep Dive: Memory Retrieval

### Similarity Search for Context

Memory retrieval uses vector similarity to find relevant past information:

```python
class AdvancedMemoryRetrieval:
    def __init__(self):
        self.embeddings = EmbeddingModel()
        self.vector_db = VectorDatabase()
    
    async def retrieve_relevant_memories(self, current_query, user_id):
        """
        Retrieve memories most relevant to current query
        """
        # Convert query to embedding
        query_embedding = await self.embeddings.embed(current_query)
        
        # Search for similar memories
        similar_memories = await self.vector_db.similarity_search(
            embedding=query_embedding,
            user_id=user_id,
            top_k=5,
            threshold=0.7  # Minimum similarity score
        )
        
        # Rank by relevance and recency
        ranked_memories = self.rank_memories(
            similar_memories,
            factors={
                "similarity": 0.6,
                "recency": 0.3,
                "confidence": 0.1
            }
        )
        
        return ranked_memories
    
    def rank_memories(self, memories, factors):
        """
        Rank memories by multiple factors
        """
        scored_memories = []
        for memory in memories:
            score = (
                memory.similarity * factors["similarity"] +
                self.recency_score(memory.timestamp) * factors["recency"] +
                memory.confidence * factors["confidence"]
            )
            scored_memories.append((score, memory))
        
        return [mem for score, mem in sorted(scored_memories, reverse=True)]
```

### Memory-Enhanced Prompt Construction

```python
async def build_context_aware_prompt(self, user_query, user_id):
    """
    Build prompt enriched with relevant memories
    """
    # Retrieve relevant memories
    memories = await self.memory.retrieve_relevant_memories(
        user_query, 
        user_id
    )
    
    # Format memories for prompt
    memory_context = "\n".join([
        f"- {mem.content} (from {mem.timestamp})"
        for mem in memories
    ])
    
    # Construct enhanced prompt
    prompt = f"""
    User Query: {user_query}
    
    Relevant Context from Previous Interactions:
    {memory_context}
    
    Please provide a personalized response that takes into account
    the user's preferences and history shown above.
    """
    
    return prompt
```

## ⚡ Quick Win: Minimal Memory System

### 15-Minute Implementation

```python
from collections import defaultdict
import json
from datetime import datetime

class SimpleMemorySystem:
    """
    Lightweight memory system for quick implementation
    """
    def __init__(self, storage_path="memories.json"):
        self.storage_path = storage_path
        self.memories = self.load_memories()
    
    def extract_and_store(self, user_id, conversation_text):
        """
        Simple keyword-based memory extraction
        """
        # Basic extraction rules
        memories = []
        
        # Extract preferences
        if "prefer" in conversation_text.lower():
            memories.append({
                "type": "preference",
                "content": conversation_text,
                "timestamp": datetime.now().isoformat()
            })
        
        # Extract named entities (simple approach)
        if "named" in conversation_text.lower() or "called" in conversation_text.lower():
            memories.append({
                "type": "fact",
                "content": conversation_text,
                "timestamp": datetime.now().isoformat()
            })
        
        # Store
        if user_id not in self.memories:
            self.memories[user_id] = []
        
        self.memories[user_id].extend(memories)
        self.save_memories()
        
        return memories
    
    def recall(self, user_id, query=None):
        """
        Retrieve memories for user
        """
        user_memories = self.memories.get(user_id, [])
        
        if query:
            # Simple keyword matching
            relevant = [
                mem for mem in user_memories
                if any(word in mem["content"].lower() 
                       for word in query.lower().split())
            ]
            return relevant
        
        return user_memories[-5:]  # Return recent memories
    
    def save_memories(self):
        with open(self.storage_path, 'w') as f:
            json.dump(self.memories, f, indent=2)
    
    def load_memories(self):
        try:
            with open(self.storage_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}


# Usage
memory = SimpleMemorySystem()

# Store memories
memory.extract_and_store(
    user_id="user_123",
    conversation_text="I prefer dark mode and my cat is named Whiskers"
)

# Recall memories
memories = memory.recall(user_id="user_123", query="preferences")
print(memories)
```

## 🌳 Advanced: Multi-Session Memory

### Persistent Context Across Sessions

```python
class MultiSessionMemory:
    """
    Advanced memory system with session management
    """
    def __init__(self, user_id):
        self.user_id = user_id
        self.short_term = []  # Current session
        self.long_term = VectorStore()  # Persistent across sessions
        self.working_memory = []  # Active context (limited size)
    
    async def start_session(self):
        """
        Load relevant long-term memories into working memory
        """
        # Get recent and important memories
        recent = await self.long_term.get_recent(limit=10)
        important = await self.long_term.get_by_importance(threshold=0.8)
        
        # Combine and deduplicate
        self.working_memory = self.deduplicate(recent + important)[:15]
    
    async def process_interaction(self, user_input, agent_response):
        """
        Process interaction and update memories
        """
        # Add to short-term memory
        interaction = {
            "input": user_input,
            "response": agent_response,
            "timestamp": datetime.now()
        }
        self.short_term.append(interaction)
        
        # Extract potential long-term memories
        if self.is_memorable(interaction):
            memory = await self.extract_memory(interaction)
            await self.long_term.store(memory)
            
            # Add to working memory if important
            if memory.importance > 0.7:
                self.working_memory.append(memory)
    
    async def end_session(self):
        """
        Consolidate short-term memories into long-term storage
        """
        # Analyze entire session
        session_summary = await self.summarize_session(self.short_term)
        
        # Store important insights
        if session_summary.has_insights():
            await self.long_term.store(session_summary)
        
        # Clear short-term and working memory
        self.short_term = []
        self.working_memory = []
```

## 🎯 Key Takeaways

- **Asynchronous extraction** prevents memory generation from blocking responses
- **Similarity search** finds relevant context efficiently
- **Categorization** helps organize different types of memories
- **Confidence scores** indicate reliability of extracted information
- **Multi-level memory** (short-term, working, long-term) mirrors human cognition

## Best Practices

### 1. Privacy First
```python
# Always anonymize and secure memories
memory_manager = MemoryManager(
    encryption=True,
    anonymize_pii=True,
    user_control=True  # Users can delete their memories
)
```

### 2. Memory Decay
```python
# Implement forgetting for outdated information
def apply_memory_decay(memory, current_time):
    age_days = (current_time - memory.timestamp).days
    decay_factor = 0.95 ** (age_days / 30)  # 5% decay per month
    memory.confidence *= decay_factor
    return memory
```

### 3. Conflict Resolution
```python
# Handle contradictory memories
def resolve_conflicts(old_memory, new_memory):
    if new_memory.timestamp > old_memory.timestamp:
        # Newer information typically more accurate
        old_memory.superseded_by = new_memory.id
        return new_memory
    return old_memory
```

## Next Steps

Continue to [RAG Fundamentals](../rag/01-rag-fundamentals.md) to learn how to combine memory with retrieval-augmented generation for even more powerful agents.

---

💡 **Remember**: Good memory management is about storing what matters and retrieving it when relevant—just like human memory!
