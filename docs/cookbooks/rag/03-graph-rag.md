# 🕸️ GraphRAG: Knowledge Graphs for AI Agents

## 🌳 Flourishing Concept

**Label**: Understanding Relationships, Not Just Documents

GraphRAG enriches traditional RAG by understanding the **explicit relationships** between data points in a knowledge graph. Instead of just finding similar documents, GraphRAG leverages the connections and structure of your knowledge to provide richer, more contextual answers.

## What is GraphRAG?

### Traditional RAG vs. GraphRAG

```
Traditional RAG:                  GraphRAG:
┌──────────┐                     ┌──────────┐
│Document 1│                     │Document 1│
└──────────┘                     └────┬─────┘
                                      │ authored_by
┌──────────┐                          │
│Document 2│                     ┌────▼─────┐         ┌────────────┐
└──────────┘                     │  Person  │─relates→│ Department │
                                 └────┬─────┘         └────────────┘
┌──────────┐                          │ worked_on
│Document 3│                          │
└──────────┘                     ┌────▼─────┐
                                 │ Project  │
                                 └──────────┘

Similarity search only         Relationship-aware retrieval
```

### Why GraphRAG Matters

**Traditional RAG**: "Find documents about Python web frameworks"
- Returns: Documents mentioning Django, Flask, FastAPI

**GraphRAG**: "Find documents about Python web frameworks"
- Returns: Documents about frameworks
- **Plus**: Related concepts (ASGI, WSGI)
- **Plus**: Authors who contributed to multiple frameworks
- **Plus**: Projects that compare frameworks
- **Plus**: Dependencies between frameworks

## 💡 Building a Knowledge Graph

### Graph Components

#### Nodes (Entities)
```python
from typing import List, Dict

class Node:
    """Represents an entity in the knowledge graph"""
    def __init__(self, id: str, type: str, properties: Dict):
        self.id = id
        self.type = type  # person, document, concept, etc.
        self.properties = properties

# Examples
person_node = Node(
    id="person_123",
    type="person",
    properties={
        "name": "Sarah Chen",
        "role": "Senior Engineer",
        "expertise": ["Python", "ML", "Distributed Systems"]
    }
)

document_node = Node(
    id="doc_456",
    type="document",
    properties={
        "title": "Building Scalable APIs with FastAPI",
        "published": "2024-01-15",
        "topics": ["FastAPI", "API Design", "Python"]
    }
)

concept_node = Node(
    id="concept_789",
    type="concept",
    properties={
        "name": "Asynchronous Programming",
        "category": "Programming Paradigm"
    }
)
```

#### Edges (Relationships)
```python
class Edge:
    """Represents a relationship between entities"""
    def __init__(self, source: str, target: str, relation: str, properties: Dict = None):
        self.source = source
        self.target = target
        self.relation = relation
        self.properties = properties or {}

# Examples
authored_edge = Edge(
    source="person_123",
    target="doc_456",
    relation="AUTHORED",
    properties={"date": "2024-01-15"}
)

mentions_edge = Edge(
    source="doc_456",
    target="concept_789",
    relation="MENTIONS",
    properties={"relevance": 0.95}
)

relates_edge = Edge(
    source="concept_789",
    target="concept_async_io",
    relation="RELATED_TO",
    properties={"similarity": 0.87}
)
```

### Building the Graph

```python
class KnowledgeGraph:
    """
    Knowledge graph for GraphRAG
    """
    def __init__(self):
        self.nodes = {}
        self.edges = []
        self.embeddings = {}
    
    def add_node(self, node: Node):
        """Add a node to the graph"""
        self.nodes[node.id] = node
        # Generate embedding for semantic search
        self.embeddings[node.id] = self.create_embedding(node)
    
    def add_edge(self, edge: Edge):
        """Add a relationship between nodes"""
        self.edges.append(edge)
    
    def create_embedding(self, node: Node) -> list:
        """Create vector embedding for node"""
        # Combine node type, properties into text
        text = f"{node.type}: {node.properties}"
        return embedding_model.embed(text)
    
    def find_neighbors(self, node_id: str, relation: str = None, hops: int = 1) -> List[Node]:
        """
        Find connected nodes
        
        Args:
            node_id: Starting node
            relation: Filter by relationship type (optional)
            hops: Number of relationships to traverse
        """
        neighbors = []
        current_nodes = {node_id}
        
        for _ in range(hops):
            next_nodes = set()
            for edge in self.edges:
                if edge.source in current_nodes:
                    if relation is None or edge.relation == relation:
                        next_nodes.add(edge.target)
                        neighbors.append(self.nodes[edge.target])
            current_nodes = next_nodes
        
        return neighbors


# Usage
graph = KnowledgeGraph()

# Add nodes
graph.add_node(person_node)
graph.add_node(document_node)
graph.add_node(concept_node)

# Add relationships
graph.add_edge(authored_edge)
graph.add_edge(mentions_edge)

# Find related content
related_docs = graph.find_neighbors("person_123", relation="AUTHORED")
print(f"Sarah authored {len(related_docs)} documents")
```

## 🔬 Deep Dive: GraphRAG Retrieval

### Multi-Hop Retrieval

```python
class GraphRAG:
    """
    RAG system enhanced with knowledge graph
    """
    def __init__(self, knowledge_graph: KnowledgeGraph, vector_store):
        self.graph = knowledge_graph
        self.vector_store = vector_store
        self.llm = LLM()
    
    async def retrieve_with_context(self, query: str, max_hops: int = 2) -> Dict:
        """
        Retrieve documents with graph context
        """
        # Step 1: Vector similarity search (like traditional RAG)
        initial_results = await self.vector_store.search(query, top_k=5)
        
        # Step 2: Expand with graph relationships
        expanded_results = []
        for result in initial_results:
            # Get the node from graph
            node_id = result['node_id']
            
            # Find related nodes through graph traversal
            neighbors = self.graph.find_neighbors(node_id, hops=max_hops)
            
            expanded_results.append({
                'primary': result,
                'related_entities': neighbors,
                'relationship_paths': self.get_paths(node_id, neighbors)
            })
        
        return {
            'results': expanded_results,
            'graph_context': self.build_subgraph(expanded_results)
        }
    
    def get_paths(self, source: str, targets: List[Node]) -> List[List[str]]:
        """Find relationship paths between nodes"""
        paths = []
        for target in targets:
            path = self.find_shortest_path(source, target.id)
            if path:
                paths.append(path)
        return paths
    
    def build_subgraph(self, results: List[Dict]) -> Dict:
        """
        Build subgraph from retrieved results
        """
        nodes = set()
        edges = []
        
        for result in results:
            nodes.add(result['primary']['node_id'])
            for entity in result['related_entities']:
                nodes.add(entity.id)
            
            # Get edges between these nodes
            for edge in self.graph.edges:
                if edge.source in nodes and edge.target in nodes:
                    edges.append(edge)
        
        return {
            'nodes': [self.graph.nodes[n] for n in nodes],
            'edges': edges
        }
```

### Relationship-Aware Generation

```python
async def generate_answer(self, query: str) -> str:
    """
    Generate answer using graph context
    """
    # Retrieve with graph expansion
    retrieval = await self.retrieve_with_context(query, max_hops=2)
    
    # Build rich context from graph
    context = self.format_graph_context(retrieval)
    
    # Generate with relationship awareness
    prompt = f"""
    Answer this question using the provided information and relationships:
    
    Question: {query}
    
    Primary Documents:
    {self.format_documents(retrieval['results'])}
    
    Related Entities and Relationships:
    {context['entity_relationships']}
    
    Knowledge Graph Context:
    {context['graph_structure']}
    
    Provide an answer that:
    1. Uses information from primary documents
    2. Incorporates relevant relationships
    3. Explains how entities are connected
    4. Cites sources with relationship context
    """
    
    answer = await self.llm.generate(prompt)
    return answer

def format_graph_context(self, retrieval: Dict) -> Dict:
    """
    Format graph information for LLM
    """
    subgraph = retrieval['graph_context']
    
    # Format entities
    entities = []
    for node in subgraph['nodes']:
        entities.append(f"- {node.type}: {node.properties['name']}")
    
    # Format relationships
    relationships = []
    for edge in subgraph['edges']:
        source = self.graph.nodes[edge.source]
        target = self.graph.nodes[edge.target]
        relationships.append(
            f"- {source.properties['name']} --[{edge.relation}]--> {target.properties['name']}"
        )
    
    return {
        'entity_relationships': '\n'.join(relationships),
        'graph_structure': {
            'entities': entities,
            'connections': len(subgraph['edges'])
        }
    }
```

## ⚡ Quick Win: Simple GraphRAG Implementation

### 30-Minute Graph-Enhanced RAG

```python
from collections import defaultdict

class SimpleGraphRAG:
    """
    Lightweight GraphRAG for quick implementation
    """
    def __init__(self):
        self.documents = {}
        self.relationships = defaultdict(list)
        self.embeddings = {}
    
    def add_document(self, doc_id: str, content: str, metadata: Dict):
        """Add document with metadata"""
        self.documents[doc_id] = {
            'content': content,
            'metadata': metadata
        }
        self.embeddings[doc_id] = create_embedding(content)
    
    def add_relationship(self, doc_id: str, related_id: str, relation_type: str):
        """Link documents via relationships"""
        self.relationships[doc_id].append({
            'target': related_id,
            'type': relation_type
        })
    
    def search(self, query: str, include_related: bool = True) -> List[Dict]:
        """Search with optional graph expansion"""
        # Semantic search
        query_embedding = create_embedding(query)
        results = self.find_similar(query_embedding, top_k=3)
        
        if include_related:
            # Expand with related documents
            expanded = []
            for result in results:
                doc_id = result['id']
                expanded.append(result)
                
                # Add related documents
                for rel in self.relationships[doc_id]:
                    related_doc = self.documents[rel['target']]
                    expanded.append({
                        'id': rel['target'],
                        'content': related_doc['content'],
                        'relationship': rel['type'],
                        'via': doc_id
                    })
            
            return expanded
        
        return results


# Usage
graph_rag = SimpleGraphRAG()

# Add documents
graph_rag.add_document(
    "doc1",
    "FastAPI is a modern Python web framework",
    {"author": "Author1", "topic": "Python"}
)

graph_rag.add_document(
    "doc2",
    "Building async APIs with Python",
    {"author": "Author1", "topic": "Python"}
)

# Add relationships
graph_rag.add_relationship("doc1", "doc2", "RELATED_TOPIC")
graph_rag.add_relationship("doc1", "doc2", "SAME_AUTHOR")

# Search with graph expansion
results = graph_rag.search("Python web frameworks", include_related=True)

for r in results:
    print(f"- {r['id']}: {r.get('relationship', 'PRIMARY')}")
```

## 🌳 Advanced: Complex Graph Patterns

### Community Detection for Better Retrieval

```python
class CommunityGraphRAG:
    """
    GraphRAG with community detection for topic clustering
    """
    def __init__(self, graph: KnowledgeGraph):
        self.graph = graph
        self.communities = self.detect_communities()
    
    def detect_communities(self) -> Dict[str, int]:
        """
        Detect communities (clusters) in the graph
        """
        # Simplified community detection
        # In production, use algorithms like Louvain or Label Propagation
        communities = {}
        community_id = 0
        
        visited = set()
        for node_id in self.graph.nodes:
            if node_id not in visited:
                # BFS to find connected component
                community = self.bfs_component(node_id, visited)
                for n in community:
                    communities[n] = community_id
                community_id += 1
        
        return communities
    
    def retrieve_from_community(self, query: str) -> List[Dict]:
        """
        Retrieve from the most relevant community
        """
        # Find most relevant node
        query_embedding = create_embedding(query)
        most_similar = self.find_most_similar_node(query_embedding)
        
        # Get its community
        community_id = self.communities[most_similar]
        
        # Retrieve all nodes from that community
        community_nodes = [
            node_id for node_id, comm_id in self.communities.items()
            if comm_id == community_id
        ]
        
        # Return community documents
        return [self.graph.nodes[n] for n in community_nodes]
```

### Temporal Graphs for Time-Aware Retrieval

```python
class TemporalGraphRAG:
    """
    GraphRAG with temporal relationships
    """
    def __init__(self):
        self.graph = KnowledgeGraph()
        self.temporal_edges = []
    
    def add_temporal_edge(self, source: str, target: str, 
                         relation: str, timestamp: str):
        """Add time-stamped relationship"""
        edge = Edge(source, target, relation, {
            'timestamp': timestamp,
            'valid_from': timestamp
        })
        self.temporal_edges.append(edge)
    
    def query_at_time(self, query: str, timestamp: str) -> List[Dict]:
        """
        Retrieve considering temporal validity
        """
        # Filter edges valid at given time
        valid_edges = [
            e for e in self.temporal_edges
            if e.properties['valid_from'] <= timestamp
        ]
        
        # Build temporal subgraph
        temporal_graph = self.build_temporal_subgraph(valid_edges)
        
        # Query on temporal graph
        return self.retrieve_from_graph(query, temporal_graph)
```

## 🎯 Real-World Use Cases

### 1. Technical Documentation

```python
# Build knowledge graph of documentation
docs_graph = KnowledgeGraph()

# Nodes: Documents, APIs, Concepts, Examples
docs_graph.add_node(Node("api_auth", "api", {"name": "Authentication API"}))
docs_graph.add_node(Node("guide_auth", "guide", {"title": "Auth Guide"}))
docs_graph.add_node(Node("concept_oauth", "concept", {"name": "OAuth 2.0"}))

# Relationships
docs_graph.add_edge(Edge("guide_auth", "api_auth", "DOCUMENTS"))
docs_graph.add_edge(Edge("api_auth", "concept_oauth", "IMPLEMENTS"))

# Query: "How do I implement authentication?"
# Result: Guide + API docs + OAuth concept + related examples
```

### 2. Enterprise Knowledge Base

```python
# Nodes: Employees, Projects, Documents, Skills
kb_graph = KnowledgeGraph()

kb_graph.add_node(Node("emp_sarah", "employee", {"name": "Sarah", "role": "Engineer"}))
kb_graph.add_node(Node("proj_api", "project", {"name": "API Redesign"}))
kb_graph.add_node(Node("doc_design", "document", {"title": "API Design Doc"}))

# Relationships
kb_graph.add_edge(Edge("emp_sarah", "proj_api", "WORKS_ON"))
kb_graph.add_edge(Edge("emp_sarah", "doc_design", "AUTHORED"))
kb_graph.add_edge(Edge("doc_design", "proj_api", "DESCRIBES"))

# Query: "Who knows about API design?"
# Result: Sarah + her projects + related documents + her expertise
```

### 3. Research Papers

```python
# Nodes: Papers, Authors, Concepts, Citations
research_graph = KnowledgeGraph()

# Build citation network
research_graph.add_edge(Edge("paper_new", "paper_old", "CITES"))
research_graph.add_edge(Edge("paper_new", "author_smith", "AUTHORED_BY"))
research_graph.add_edge(Edge("paper_new", "concept_transformer", "DISCUSSES"))

# Query: "Recent work on transformers"
# Result: Recent papers + citing papers + related concepts + author networks
```

## 🎯 Key Takeaways

- **GraphRAG adds relationship understanding** to traditional RAG
- **Multi-hop traversal** discovers indirect connections
- **Community detection** finds topic clusters
- **Temporal graphs** enable time-aware retrieval
- **Subgraph extraction** provides rich context

## When to Use GraphRAG

### Use Traditional RAG When:
- Documents are independent
- Simple similarity is sufficient
- Performance is critical
- Graph construction overhead too high

### Use GraphRAG When:
- Relationships matter (org charts, citations, dependencies)
- Need to explain connections
- Multi-hop reasoning required
- Domain has natural graph structure

## Next Steps

Continue to [Grounding Techniques](./04-grounding.md) to learn advanced methods for keeping your agents accurate and reliable.

---

💡 **Remember**: GraphRAG shines when understanding "how things connect" is as important as finding "what matches."
