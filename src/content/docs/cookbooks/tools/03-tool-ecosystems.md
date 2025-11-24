---
title: "🛠️ Tool Ecosystems: LangChain, LlamaIndex, and CrewAI"
---

## 🌳 Flourishing Concept

**Label**: Leveraging Existing Frameworks

Tool ecosystems are established frameworks that provide pre-built components, patterns, and integrations for AI agent development. Rather than building everything from scratch, you can leverage these mature ecosystems to accelerate development.

## Overview of Major Ecosystems

```
┌────────────────────────────────────────────────────┐
│           Tool Ecosystem Landscape                 │
├────────────────────────────────────────────────────┤
│                                                    │
│  LangChain          LlamaIndex         CrewAI     │
│  ┌──────────┐      ┌──────────┐      ┌─────────┐ │
│  │  Chains  │      │  Indexes │      │  Crews  │ │
│  │  Agents  │      │  Queries │      │  Tasks  │ │
│  │  Tools   │      │  Engines │      │  Roles  │ │
│  └──────────┘      └──────────┘      └─────────┘ │
│                                                    │
│  Best for:         Best for:         Best for:    │
│  - Workflows       - Data indexing   - Teams      │
│  - Chains          - RAG systems     - Roles      │
│  - General AI      - Querying        - Workflows  │
└────────────────────────────────────────────────────┘
```

## 💡 LangChain: Composable AI Workflows

### What is LangChain?

LangChain is a framework for developing applications powered by language models, emphasizing **composability** through chains, agents, and tools.

### Key Concepts

#### 1. Chains

```python
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI

# Simple chain
template = "What is a good name for a company that makes {product}?"
prompt = PromptTemplate(template=template, input_variables=["product"])

llm = OpenAI(temperature=0.9)
chain = LLMChain(llm=llm, prompt=prompt)

# Execute
result = chain.run("eco-friendly water bottles")
print(result)
```

#### 2. Sequential Chains

```python
from langchain.chains import SimpleSequentialChain

# Chain 1: Generate product name
chain_one = LLMChain(
    llm=llm,
    prompt=PromptTemplate(
        template="Generate a creative name for {product}",
        input_variables=["product"]
    )
)

# Chain 2: Generate tagline
chain_two = LLMChain(
    llm=llm,
    prompt=PromptTemplate(
        template="Create a tagline for a company called {company_name}",
        input_variables=["company_name"]
    )
)

# Combine chains
overall_chain = SimpleSequentialChain(
    chains=[chain_one, chain_two],
    verbose=True
)

# Execute pipeline
result = overall_chain.run("eco-friendly water bottles")
print(result)
```

#### 3. Agents with Tools

```python
from langchain.agents import initialize_agent, Tool, AgentType
from langchain.tools import DuckDuckGoSearchRun

# Define tools
search = DuckDuckGoSearchRun()

tools = [
    Tool(
        name="Search",
        func=search.run,
        description="Useful for searching the internet for current information"
    ),
    Tool(
        name="Calculator",
        func=lambda x: eval(x),
        description="Useful for mathematical calculations"
    )
]

# Create agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Use agent
result = agent.run(
    "What is the population of Tokyo multiplied by 2?"
)
print(result)
```

### Real-World LangChain Example

```python
from langchain.chains import RetrievalQA
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.document_loaders import DirectoryLoader

class DocumentQASystem:
    """
    Question answering system using LangChain
    """
    def __init__(self, docs_directory: str):
        # Load documents
        loader = DirectoryLoader(docs_directory, glob="**/*.md")
        documents = loader.load()
        
        # Create vector store
        embeddings = OpenAIEmbeddings()
        self.vectorstore = Chroma.from_documents(
            documents,
            embeddings
        )
        
        # Create QA chain
        self.qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=self.vectorstore.as_retriever()
        )
    
    def ask(self, question: str) -> str:
        """
        Ask a question about the documents
        """
        return self.qa_chain.run(question)


# Usage
qa_system = DocumentQASystem("./company_docs")
answer = qa_system.ask("What is our return policy?")
print(answer)
```

## 🔬 LlamaIndex: Data Framework for LLMs

### What is LlamaIndex?

LlamaIndex (formerly GPT Index) is a data framework for connecting LLMs with external data sources, specializing in **indexing and querying**.

### Key Concepts

#### 1. Simple Index and Query

```python
from llama_index import VectorStoreIndex, SimpleDirectoryReader

# Load documents
documents = SimpleDirectoryReader('data').load_data()

# Create index
index = VectorStoreIndex.from_documents(documents)

# Query
query_engine = index.as_query_engine()
response = query_engine.query("What is the return policy?")
print(response)
```

#### 2. Different Index Types

```python
from llama_index import (
    VectorStoreIndex,
    TreeIndex,
    KeywordTableIndex,
    ListIndex
)

# Vector index for semantic search
vector_index = VectorStoreIndex.from_documents(documents)

# Tree index for hierarchical data
tree_index = TreeIndex.from_documents(documents)

# Keyword index for exact matching
keyword_index = KeywordTableIndex.from_documents(documents)

# List index for sequential scanning
list_index = ListIndex.from_documents(documents)
```

#### 3. Custom Retrievers

```python
from llama_index import VectorStoreIndex
from llama_index.retrievers import VectorIndexRetriever
from llama_index.query_engine import RetrieverQueryEngine

class CustomDocumentRetriever:
    """
    Custom retriever with LlamaIndex
    """
    def __init__(self, index: VectorStoreIndex):
        # Configure retriever
        self.retriever = VectorIndexRetriever(
            index=index,
            similarity_top_k=5,
            vector_store_query_mode="default"
        )
        
        # Create query engine
        self.query_engine = RetrieverQueryEngine(
            retriever=self.retriever
        )
    
    def query(self, question: str, filters: dict = None) -> str:
        """
        Query with optional filters
        """
        if filters:
            self.retriever.filters = filters
        
        response = self.query_engine.query(question)
        return str(response)
    
    def get_sources(self, response) -> list:
        """
        Get source documents for response
        """
        return [node.node.get_text() for node in response.source_nodes]


# Usage
retriever = CustomDocumentRetriever(vector_index)
response = retriever.query(
    "What are the technical requirements?",
    filters={"category": "technical"}
)
sources = retriever.get_sources(response)
```

### Real-World LlamaIndex Example

```python
from llama_index import (
    VectorStoreIndex,
    ServiceContext,
    StorageContext
)
from llama_index.vector_stores import ChromaVectorStore
from llama_index.embeddings import OpenAIEmbedding
import chromadb

class ProductKnowledgeBase:
    """
    Product documentation knowledge base with LlamaIndex
    """
    def __init__(self):
        # Setup Chroma client
        chroma_client = chromadb.Client()
        chroma_collection = chroma_client.create_collection("products")
        
        # Create vector store
        vector_store = ChromaVectorStore(
            chroma_collection=chroma_collection
        )
        
        # Configure service
        service_context = ServiceContext.from_defaults(
            embed_model=OpenAIEmbedding()
        )
        
        # Storage context
        storage_context = StorageContext.from_defaults(
            vector_store=vector_store
        )
        
        # Load and index documents
        documents = SimpleDirectoryReader('product_docs').load_data()
        
        self.index = VectorStoreIndex.from_documents(
            documents,
            service_context=service_context,
            storage_context=storage_context
        )
    
    def search_products(self, query: str) -> dict:
        """
        Search product knowledge base
        """
        query_engine = self.index.as_query_engine(
            similarity_top_k=3,
            response_mode="tree_summarize"
        )
        
        response = query_engine.query(query)
        
        return {
            'answer': str(response),
            'sources': [
                {
                    'text': node.node.get_text()[:200],
                    'score': node.score
                }
                for node in response.source_nodes
            ]
        }


# Usage
kb = ProductKnowledgeBase()
result = kb.search_products("What are the features of Product X?")
print(result['answer'])
```

## 🤝 CrewAI: Role-Based Multi-Agent Teams

### What is CrewAI?

CrewAI is a framework for orchestrating role-based autonomous agents, emphasizing **team collaboration** and **task delegation**.

### Key Concepts

#### 1. Agents with Roles

```python
from crewai import Agent, Task, Crew
from langchain.llms import OpenAI

# Define agents with roles
researcher = Agent(
    role='Senior Research Analyst',
    goal='Uncover cutting-edge developments in AI',
    backstory="""You are an expert at finding and analyzing
    the latest AI research and trends.""",
    verbose=True,
    llm=OpenAI(temperature=0.7)
)

writer = Agent(
    role='Tech Content Writer',
    goal='Write compelling tech articles',
    backstory="""You are a skilled writer who can transform
    complex technical information into engaging content.""",
    verbose=True,
    llm=OpenAI(temperature=0.7)
)
```

#### 2. Tasks and Workflows

```python
# Define tasks
research_task = Task(
    description="""Research the latest developments in
    retrieval-augmented generation (RAG) systems""",
    agent=researcher
)

writing_task = Task(
    description="""Write a comprehensive article about
    RAG systems based on the research findings""",
    agent=writer
)

# Create crew
crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, writing_task],
    verbose=True
)

# Execute
result = crew.kickoff()
print(result)
```

#### 3. Tools for Agents

```python
from crewai_tools import SerperDevTool, WebsiteSearchTool

# Define tools
search_tool = SerperDevTool()
web_scraper = WebsiteSearchTool()

# Agent with tools
researcher = Agent(
    role='Research Analyst',
    goal='Find accurate information',
    tools=[search_tool, web_scraper],
    verbose=True
)

# Task using tools
task = Task(
    description="Research latest AI regulations",
    agent=researcher
)
```

### Real-World CrewAI Example

```python
from crewai import Agent, Task, Crew, Process

class ContentCreationCrew:
    """
    Multi-agent content creation team
    """
    def __init__(self):
        # Define specialized agents
        self.researcher = Agent(
            role='Content Researcher',
            goal='Find accurate, up-to-date information',
            backstory='Expert researcher with deep knowledge',
            tools=[search_tool],
            verbose=True
        )
        
        self.outliner = Agent(
            role='Content Strategist',
            goal='Create effective content structures',
            backstory='Skilled at organizing information',
            verbose=True
        )
        
        self.writer = Agent(
            role='Content Writer',
            goal='Write engaging content',
            backstory='Talented writer with clear style',
            verbose=True
        )
        
        self.editor = Agent(
            role='Editor',
            goal='Ensure quality and accuracy',
            backstory='Meticulous editor with high standards',
            verbose=True
        )
    
    def create_article(self, topic: str) -> str:
        """
        Create article with multi-agent collaboration
        """
        # Define tasks
        research = Task(
            description=f"Research comprehensive information about {topic}",
            agent=self.researcher
        )
        
        outline = Task(
            description=f"Create detailed outline for article on {topic}",
            agent=self.outliner
        )
        
        draft = Task(
            description=f"Write article following the outline",
            agent=self.writer
        )
        
        edit = Task(
            description=f"Edit and polish the article",
            agent=self.editor
        )
        
        # Create crew with sequential process
        crew = Crew(
            agents=[self.researcher, self.outliner, self.writer, self.editor],
            tasks=[research, outline, draft, edit],
            process=Process.sequential,
            verbose=True
        )
        
        # Execute workflow
        result = crew.kickoff()
        
        return result


# Usage
content_team = ContentCreationCrew()
article = content_team.create_article("GraphRAG systems")
print(article)
```

## 🎯 Choosing the Right Ecosystem

### Decision Matrix

```
Need              → Best Choice
─────────────────────────────────
Simple chains     → LangChain
Complex workflows → LangChain
Data indexing     → LlamaIndex
RAG systems       → LlamaIndex
Multi-agent teams → CrewAI
Role-based tasks  → CrewAI
General purpose   → LangChain
Knowledge graphs  → LlamaIndex
```

### Combining Ecosystems

```python
from langchain.tools import Tool
from llama_index import VectorStoreIndex
from crewai import Agent

class HybridSystem:
    """
    Combine multiple ecosystems
    """
    def __init__(self):
        # LlamaIndex for data
        self.index = VectorStoreIndex.from_documents(documents)
        
        # LangChain tool wrapper
        def query_index(query: str) -> str:
            return str(self.index.as_query_engine().query(query))
        
        search_tool = Tool(
            name="KnowledgeBase",
            func=query_index,
            description="Search internal knowledge base"
        )
        
        # CrewAI agent with LangChain tool
        self.agent = Agent(
            role='Knowledge Expert',
            tools=[search_tool],
            goal='Answer questions using knowledge base'
        )
    
    def answer(self, question: str) -> str:
        """
        Answer using combined ecosystem
        """
        task = Task(
            description=question,
            agent=self.agent
        )
        
        crew = Crew(
            agents=[self.agent],
            tasks=[task]
        )
        
        return crew.kickoff()
```

## 🎯 Key Takeaways

- **LangChain**: Best for composable chains and general AI workflows
- **LlamaIndex**: Best for data indexing and RAG systems
- **CrewAI**: Best for role-based multi-agent teams
- **Combine ecosystems** for powerful hybrid solutions
- **Leverage existing tools** to accelerate development

## Integration Patterns

### Pattern 1: LangChain + Your ADK

```python
# Wrap LangChain tools for your ADK
from langchain.tools import DuckDuckGoSearchRun
from adk import Tool

langchain_search = DuckDuckGoSearchRun()

adk_search = Tool(
    name="web_search",
    description="Search the web",
    handler=lambda q: langchain_search.run(q)
)
```

### Pattern 2: LlamaIndex + Your RAG

```python
# Use LlamaIndex as retrieval backend
from llama_index import VectorStoreIndex

class CustomRAG:
    def __init__(self):
        self.index = VectorStoreIndex.from_documents(docs)
    
    def retrieve(self, query: str):
        # Use LlamaIndex for retrieval
        retriever = self.index.as_retriever(similarity_top_k=5)
        nodes = retriever.retrieve(query)
        
        # Your custom processing
        return self.process_nodes(nodes)
```

### Pattern 3: CrewAI + Your Agents

```python
# Bridge your agents with CrewAI
from crewai import Agent as CrewAgent

def your_agent_to_crew(your_agent):
    return CrewAgent(
        role=your_agent.role,
        goal=your_agent.goal,
        tools=your_agent.tools,
        llm=your_agent.llm
    )
```

## Next Steps

Continue to [AI Agent Engines](./04-agent-engines.md) to learn about production deployment platforms.

---

💡 **Remember**: Don't reinvent the wheel—leverage these mature ecosystems to build faster and more reliably.
