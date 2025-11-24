---
title: "🔍 RAG Fundamentals: Retrieval-Augmented Generation"
---

import ContributionButtons from '../../../components/ContributionButtons.astro';
import UsageTracker from '../../../components/UsageTracker.astro';
import AuthorshipBadge from '../../../components/AuthorshipBadge.astro';
import GreaterGoodBadge from '../../../components/GreaterGoodBadge.astro';
import CookbookAsCode from '../../../components/CookbookAsCode.astro';

<GreaterGoodBadge 
  score="high"
  category="RAG Systems"
  description="RAG democratizes access to knowledge by making AI systems grounded in real information, not hallucinations. This benefits everyone seeking trustworthy AI."
/>

<AuthorshipBadge 
  type="human-led"
  details="Technical patterns documented by CURATIONS team based on production implementations and industry best practices."
/>

<UsageTracker 
  cookbookId="rag-fundamentals"
  title="RAG Fundamentals"
/>

<CookbookAsCode 
  repoPath="src/content/docs/cookbooks/rag"
  githubUrl="https://github.com/CurationsLA/ai-learning/blob/main/src/content/docs/cookbooks/rag/01-rag-fundamentals.md"
/>

## 🌱 Seedling Concept

**Label**: Grounding AI in Real Data

RAG (Retrieval-Augmented Generation) transforms AI agents from creative storytellers into accurate information providers by grounding their responses in retrieved, factual data.

## What is RAG?

### The Core Idea

Instead of relying solely on the model's training data, RAG:

1. **Retrieves** relevant information from a knowledge base
2. **Augments** the model's prompt with retrieved context
3. **Generates** a response grounded in actual data

```
User Query: "What's our return policy?"
                    │
                    ▼
           [Similarity Search]
                    │
                    ▼
         [Retrieve Policy Documents]
                    │
                    ▼
        [Augment Prompt with Context]
                    │
                    ▼
         [Generate Grounded Response]
```

## 💡 Why RAG Matters

### Without RAG
```python
# Model might hallucinate or provide outdated information
query = "What's our return policy?"
response = model.generate(query)
# Response: "I believe you have 30 days..." (could be wrong)
```

### With RAG
```python
# Model grounds response in actual documents
query = "What's our return policy?"
relevant_docs = retrieve(query, knowledge_base)
context = f"Policy documents: {relevant_docs}"
response = model.generate(query, context=context)
# Response: "According to your current policy, customers have 45 days..."
```

## 🌿 RAG Architecture

### Three-Stage Pipeline

```
┌─────────────────────────────────────────────────┐
│              Stage 1: Indexing                  │
├─────────────────────────────────────────────────┤
│  Document → Chunks → Embeddings → Vector Store  │
└─────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────┐
│            Stage 2: Retrieval                   │
├─────────────────────────────────────────────────┤
│  Query → Embedding → Similarity Search → Top-K  │
└─────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────┐
│            Stage 3: Generation                  │
├─────────────────────────────────────────────────┤
│  Context + Query → LLM → Grounded Response      │
└─────────────────────────────────────────────────┘
```

## 🔬 Deep Dive: Building a RAG System

### Step 1: Generating Embeddings and Indexing

**Converting data into vector embeddings** for semantic search:

```python
from typing import List
import numpy as np

class EmbeddingGenerator:
    """
    Converts text into vector embeddings
    """
    def __init__(self, model_name="text-embedding-004"):
        self.embedding_model = load_embedding_model(model_name)
    
    def generate_embeddings(self, texts: List[str]) -> np.ndarray:
        """
        Generate embeddings for list of texts
        """
        embeddings = self.embedding_model.embed(texts)
        return embeddings


class DocumentIndexer:
    """
    Indexes documents for retrieval
    """
    def __init__(self):
        self.embedder = EmbeddingGenerator()
        self.chunks = []
        self.embeddings = []
    
    def chunk_document(self, document: str, chunk_size: int = 500) -> List[str]:
        """
        Split document into manageable chunks
        """
        words = document.split()
        chunks = []
        
        for i in range(0, len(words), chunk_size):
            chunk = ' '.join(words[i:i + chunk_size])
            chunks.append(chunk)
        
        return chunks
    
    def index_documents(self, documents: List[str]):
        """
        Process and index documents
        """
        for doc in documents:
            # Split into chunks
            doc_chunks = self.chunk_document(doc)
            self.chunks.extend(doc_chunks)
            
            # Generate embeddings
            chunk_embeddings = self.embedder.generate_embeddings(doc_chunks)
            self.embeddings.extend(chunk_embeddings)
        
        print(f"Indexed {len(self.chunks)} chunks from {len(documents)} documents")


# Example usage
indexer = DocumentIndexer()
documents = [
    "Our return policy allows customers to return items within 45 days...",
    "Shipping is free for orders over $50. Standard shipping takes 3-5 days...",
    "We offer a price match guarantee. If you find a lower price..."
]
indexer.index_documents(documents)
```

### Step 2: Storing and Indexing

**Fully managed vector database** for efficient similarity search:

```python
class VectorStore:
    """
    High-performance vector database for similarity search
    """
    def __init__(self, dimension: int = 768):
        self.dimension = dimension
        self.vectors = []
        self.metadata = []
        self.index = None
    
    def add_vectors(self, vectors: np.ndarray, metadata: List[dict]):
        """
        Add vectors with metadata to the store
        """
        self.vectors.extend(vectors)
        self.metadata.extend(metadata)
        
        # Build specialized index for fast search
        self.build_index()
    
    def build_index(self):
        """
        Build optimized index for similarity search
        """
        # In production, use libraries like FAISS, Pinecone, or Chroma
        self.index = self._create_efficient_index(self.vectors)
    
    def search(self, query_vector: np.ndarray, top_k: int = 5) -> List[dict]:
        """
        Find top-k most similar vectors
        """
        # Calculate similarity scores
        similarities = self._compute_similarity(query_vector, self.vectors)
        
        # Get top-k indices
        top_indices = np.argsort(similarities)[-top_k:][::-1]
        
        # Return results with metadata
        results = [
            {
                "content": self.metadata[idx]["content"],
                "score": similarities[idx],
                "metadata": self.metadata[idx]
            }
            for idx in top_indices
        ]
        
        return results
    
    def _compute_similarity(self, query: np.ndarray, vectors: List[np.ndarray]) -> np.ndarray:
        """
        Compute cosine similarity
        """
        vectors_array = np.array(vectors)
        similarities = np.dot(vectors_array, query) / (
            np.linalg.norm(vectors_array, axis=1) * np.linalg.norm(query)
        )
        return similarities


# Example usage
vector_store = VectorStore()

# Store indexed chunks
vector_store.add_vectors(
    vectors=indexer.embeddings,
    metadata=[{"content": chunk, "source": "policy_docs"} for chunk in indexer.chunks]
)
```

### Step 3: Retrieval and Reasoning

**Query processing and context retrieval**:

```python
class RAGSystem:
    """
    Complete RAG implementation
    """
    def __init__(self, vector_store: VectorStore, llm_model):
        self.vector_store = vector_store
        self.llm = llm_model
        self.embedder = EmbeddingGenerator()
    
    def retrieve(self, query: str, top_k: int = 3) -> List[dict]:
        """
        Retrieve relevant documents for query
        """
        # Convert query to embedding
        query_embedding = self.embedder.generate_embeddings([query])[0]
        
        # Search vector store
        results = self.vector_store.search(query_embedding, top_k=top_k)
        
        return results
    
    def generate(self, query: str, context: List[dict]) -> str:
        """
        Generate response using retrieved context
        """
        # Format context
        context_text = "\n\n".join([
            f"[Source {i+1}] {doc['content']}"
            for i, doc in enumerate(context)
        ])
        
        # Build prompt
        prompt = f"""
        Answer the following question using ONLY the provided context.
        If the answer cannot be found in the context, say so.
        
        Context:
        {context_text}
        
        Question: {query}
        
        Answer:
        """
        
        # Generate response
        response = self.llm.generate(prompt)
        
        return response
    
    def query(self, user_question: str) -> dict:
        """
        Complete RAG pipeline
        """
        # Retrieve relevant documents
        relevant_docs = self.retrieve(user_question, top_k=3)
        
        # Generate grounded response
        answer = self.generate(user_question, relevant_docs)
        
        return {
            "answer": answer,
            "sources": relevant_docs,
            "query": user_question
        }


# Example usage
rag = RAGSystem(vector_store, llm_model)

result = rag.query("What is your return policy?")
print(f"Answer: {result['answer']}")
print(f"\nSources used:")
for i, source in enumerate(result['sources']):
    print(f"{i+1}. {source['content'][:100]}... (score: {source['score']:.2f})")
```

## ⚡ Quick Win: Simple RAG in 30 Lines

```python
class SimpleRAG:
    """Minimal RAG implementation"""
    
    def __init__(self, documents: List[str]):
        self.documents = documents
        self.embedder = EmbeddingModel()
        self.llm = LLM()
        
        # Index documents
        self.doc_embeddings = self.embedder.embed(documents)
    
    def answer(self, question: str) -> str:
        # Embed question
        q_embedding = self.embedder.embed([question])[0]
        
        # Find most similar documents
        similarities = [
            cosine_similarity(q_embedding, doc_emb)
            for doc_emb in self.doc_embeddings
        ]
        top_3_idx = sorted(range(len(similarities)), 
                          key=lambda i: similarities[i], 
                          reverse=True)[:3]
        
        # Get relevant context
        context = "\n".join([self.documents[i] for i in top_3_idx])
        
        # Generate answer
        prompt = f"Context: {context}\n\nQuestion: {question}\nAnswer:"
        return self.llm.generate(prompt)


# Usage
docs = ["Return policy: 45 days", "Shipping: Free over $50"]
rag = SimpleRAG(docs)
print(rag.answer("What's the return policy?"))
```

## 🌳 Advanced: Hybrid Search

### Combining Dense and Sparse Retrieval

```python
class HybridRAG:
    """
    RAG with both semantic and keyword search
    """
    def __init__(self):
        self.dense_retriever = DenseRetriever()  # Vector embeddings
        self.sparse_retriever = SparseRetriever()  # BM25/TF-IDF
    
    def hybrid_retrieve(self, query: str, top_k: int = 5) -> List[dict]:
        """
        Combine dense and sparse retrieval
        """
        # Get results from both retrievers
        dense_results = self.dense_retriever.search(query, top_k=top_k*2)
        sparse_results = self.sparse_retriever.search(query, top_k=top_k*2)
        
        # Reciprocal rank fusion
        combined_scores = {}
        for rank, result in enumerate(dense_results):
            doc_id = result['id']
            combined_scores[doc_id] = combined_scores.get(doc_id, 0) + 1/(rank + 60)
        
        for rank, result in enumerate(sparse_results):
            doc_id = result['id']
            combined_scores[doc_id] = combined_scores.get(doc_id, 0) + 1/(rank + 60)
        
        # Return top-k by combined score
        top_docs = sorted(combined_scores.items(), 
                         key=lambda x: x[1], 
                         reverse=True)[:top_k]
        
        return [self.get_document(doc_id) for doc_id, _ in top_docs]
```

## 🎯 Key Takeaways

- **RAG grounds LLM responses** in factual, retrieved data
- **Three stages**: Indexing, Retrieval, Generation
- **Vector embeddings** enable semantic similarity search
- **Chunking strategy** affects retrieval quality
- **Context window** limits how much you can retrieve

## Common Pitfalls

### 1. Chunks Too Large
```python
# ❌ Bad: Loses granularity
chunk_size = 5000

# ✅ Good: Balanced granularity
chunk_size = 500
overlap = 50  # Preserve context at boundaries
```

### 2. Ignoring Metadata
```python
# ✅ Store useful metadata
metadata = {
    "content": chunk,
    "source": "docs/policy.pdf",
    "page": 3,
    "timestamp": "2024-01-15",
    "category": "policy"
}
```

### 3. No Relevance Threshold
```python
# ✅ Filter low-quality matches
results = vector_store.search(query, top_k=5)
filtered = [r for r in results if r['score'] > 0.7]
```

## Next Steps

Continue to [Agentic RAG](./02-agentic-rag/) to learn how to make your RAG system more intelligent and autonomous.

---

💡 **Pro Tip**: Start with simple RAG, then optimize based on your specific retrieval quality needs.

<ContributionButtons 
  pageTitle="RAG Fundamentals"
  pageUrl="https://hub.curations.org/cookbooks/rag/01-rag-fundamentals/"
/>
