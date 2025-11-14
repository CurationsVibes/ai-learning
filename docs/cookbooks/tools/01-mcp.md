# 🔌 Model Context Protocol (MCP): Standardized Content Delivery

## 🌱 Seedling Concept

**Label**: Universal Language for AI Context

The **Model Context Protocol (MCP)** is an open protocol that standardizes how applications provide content to Large Language Models. Think of it as USB for AI—a universal connector that works across different systems and models.

## What is MCP?

### The Interoperability Problem

```
Before MCP:                        With MCP:
┌──────────┐                      ┌──────────┐
│ App A    │──custom──┐            │ App A    │──┐
└──────────┘          │            └──────────┘  │
                      ▼                           │
┌──────────┐      ┌───────┐       ┌──────────┐  │  ┌────────┐
│ App B    │──API─┤  LLM  │       │ App B    │──┼──┤  MCP   │
└──────────┘      └───────┘       └──────────┘  │  │ Server │
                      ▲                           │  └────┬───┘
┌──────────┐          │            ┌──────────┐  │       │
│ App C    │──diff──┘             │ App C    │──┘       │
└──────────┘                       └──────────┘          │
                                                          ▼
Each app uses                                        ┌────────┐
different format                                     │  LLM   │
                                                     └────────┘
                                                     
                                                     Standard
                                                     protocol
```

### Core Benefits

1. **Plug-and-Play**: Connect any MCP server to any MCP client
2. **Reusability**: Write once, use everywhere
3. **Standardization**: Consistent format across platforms
4. **Discoverability**: Servers advertise their capabilities
5. **Maintainability**: Update servers independently

## 💡 MCP Architecture

### Components

```
┌────────────────────────────────────────────────┐
│              MCP Ecosystem                     │
├────────────────────────────────────────────────┤
│                                                │
│  ┌──────────────┐          ┌──────────────┐  │
│  │ MCP Client   │◄────────┤  MCP Server  │  │
│  │ (LLM App)    │  Protocol│  (Context)   │  │
│  └──────────────┘          └──────────────┘  │
│                                                │
│  Examples:                 Examples:           │
│  - ChatGPT                 - File System      │
│  - Claude Desktop          - Database         │
│  - VS Code                 - API Wrapper      │
│  - Custom Apps             - Web Search       │
│                                                │
└────────────────────────────────────────────────┘
```

### Request-Response Flow

```
1. Client discovers server capabilities
   Client → Server: "What can you do?"
   Server → Client: "I provide file system access"

2. Client requests context
   Client → Server: "Get files in /docs"
   Server → Client: [file1.md, file2.md, ...]

3. Client uses context with LLM
   Client → LLM: "User query + file contents"
   LLM → Client: Response

4. Client may request actions
   Client → Server: "Write file: output.txt"
   Server → Client: "Success: file created"
```

## 🔬 Building an MCP Server

### Basic MCP Server

```python
from typing import List, Dict, Any
import json

class MCPServer:
    """
    Basic MCP server implementation
    """
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.capabilities = {}
        self.tools = {}
    
    def register_capability(self, capability: str, handler: callable):
        """
        Register a capability the server provides
        """
        self.capabilities[capability] = handler
    
    def register_tool(self, name: str, description: str, handler: callable):
        """
        Register a tool that clients can invoke
        """
        self.tools[name] = {
            'description': description,
            'handler': handler
        }
    
    async def handle_request(self, request: Dict) -> Dict:
        """
        Handle incoming MCP request
        """
        request_type = request.get('type')
        
        if request_type == 'list_capabilities':
            return self.list_capabilities()
        
        elif request_type == 'list_tools':
            return self.list_tools()
        
        elif request_type == 'invoke_tool':
            return await self.invoke_tool(
                request['tool_name'],
                request.get('parameters', {})
            )
        
        elif request_type == 'get_context':
            return await self.get_context(request['query'])
        
        else:
            return {
                'error': f'Unknown request type: {request_type}'
            }
    
    def list_capabilities(self) -> Dict:
        """
        Advertise server capabilities
        """
        return {
            'name': self.name,
            'description': self.description,
            'capabilities': list(self.capabilities.keys()),
            'protocol_version': '1.0'
        }
    
    def list_tools(self) -> Dict:
        """
        List available tools
        """
        return {
            'tools': [
                {
                    'name': name,
                    'description': info['description']
                }
                for name, info in self.tools.items()
            ]
        }
    
    async def invoke_tool(self, tool_name: str, parameters: Dict) -> Dict:
        """
        Execute a tool
        """
        if tool_name not in self.tools:
            return {'error': f'Unknown tool: {tool_name}'}
        
        try:
            result = await self.tools[tool_name]['handler'](parameters)
            return {
                'status': 'success',
                'result': result
            }
        except Exception as e:
            return {
                'status': 'error',
                'error': str(e)
            }


# Example: File System MCP Server
class FileSystemMCPServer(MCPServer):
    """
    MCP server for file system operations
    """
    def __init__(self, base_path: str):
        super().__init__(
            name="FileSystemServer",
            description="Provides access to file system operations"
        )
        self.base_path = base_path
        
        # Register capabilities
        self.register_capability('read_files', self.read_file)
        self.register_capability('list_directory', self.list_directory)
        
        # Register tools
        self.register_tool(
            'read_file',
            'Read contents of a file',
            self.read_file_tool
        )
        self.register_tool(
            'list_files',
            'List files in a directory',
            self.list_files_tool
        )
    
    async def read_file_tool(self, params: Dict) -> str:
        """
        Read file contents
        """
        file_path = params['path']
        full_path = os.path.join(self.base_path, file_path)
        
        with open(full_path, 'r') as f:
            return f.read()
    
    async def list_files_tool(self, params: Dict) -> List[str]:
        """
        List directory contents
        """
        dir_path = params.get('path', '')
        full_path = os.path.join(self.base_path, dir_path)
        
        return os.listdir(full_path)


# Usage
server = FileSystemMCPServer(base_path="/documents")

# Client request
request = {
    'type': 'invoke_tool',
    'tool_name': 'read_file',
    'parameters': {'path': 'notes.txt'}
}

response = await server.handle_request(request)
print(response['result'])
```

### MCP Client

```python
class MCPClient:
    """
    Client for connecting to MCP servers
    """
    def __init__(self, server_url: str):
        self.server_url = server_url
        self.capabilities = None
        self.tools = None
    
    async def connect(self):
        """
        Connect to server and discover capabilities
        """
        # Discover capabilities
        self.capabilities = await self.request({
            'type': 'list_capabilities'
        })
        
        # Discover tools
        self.tools = await self.request({
            'type': 'list_tools'
        })
        
        return {
            'server': self.capabilities['name'],
            'tools': len(self.tools['tools'])
        }
    
    async def request(self, payload: Dict) -> Dict:
        """
        Send request to MCP server
        """
        # In real implementation, use HTTP/WebSocket
        response = await http.post(self.server_url, json=payload)
        return response.json()
    
    async def use_tool(self, tool_name: str, **kwargs) -> Any:
        """
        Invoke a tool on the server
        """
        response = await self.request({
            'type': 'invoke_tool',
            'tool_name': tool_name,
            'parameters': kwargs
        })
        
        if response.get('status') == 'success':
            return response['result']
        else:
            raise Exception(response.get('error', 'Unknown error'))


# Usage
client = MCPClient("http://localhost:8080/mcp")
await client.connect()

# Use server tools
file_contents = await client.use_tool('read_file', path='readme.md')
files = await client.use_tool('list_files', path='/')
```

## ⚡ Quick Win: Simple MCP Server in 20 Lines

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class MCPRequest(BaseModel):
    type: str
    parameters: dict = {}

@app.post("/mcp")
async def mcp_endpoint(request: MCPRequest):
    if request.type == "list_tools":
        return {
            "tools": [
                {"name": "echo", "description": "Echo input"}
            ]
        }
    
    elif request.type == "invoke_tool":
        if request.parameters.get("tool") == "echo":
            return {
                "status": "success",
                "result": request.parameters.get("message")
            }
    
    return {"error": "Unknown request"}

# Run: uvicorn mcp_server:app --port 8080
```

## 🌳 Advanced: Production MCP Server

### Full-Featured MCP Server

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Any, Optional
import asyncio

class MCPServer:
    """
    Production-grade MCP server
    """
    def __init__(self):
        self.app = FastAPI(title="MCP Server")
        self.tools = {}
        self.contexts = {}
        self.middleware = []
        
        self.setup_routes()
    
    def setup_routes(self):
        """
        Setup MCP endpoints
        """
        @self.app.get("/mcp/capabilities")
        async def get_capabilities():
            return {
                "server": {
                    "name": "ProductionMCPServer",
                    "version": "1.0.0",
                    "protocol_version": "1.0"
                },
                "capabilities": {
                    "tools": True,
                    "contexts": True,
                    "streaming": False
                }
            }
        
        @self.app.get("/mcp/tools")
        async def list_tools():
            return {
                "tools": [
                    {
                        "name": name,
                        "description": tool['description'],
                        "parameters": tool['parameters']
                    }
                    for name, tool in self.tools.items()
                ]
            }
        
        @self.app.post("/mcp/tools/{tool_name}")
        async def invoke_tool(tool_name: str, request: Dict):
            if tool_name not in self.tools:
                raise HTTPException(404, f"Tool {tool_name} not found")
            
            # Apply middleware
            for middleware in self.middleware:
                request = await middleware.pre_invoke(request)
            
            # Execute tool
            try:
                result = await self.tools[tool_name]['handler'](request)
                
                # Apply post-middleware
                for middleware in self.middleware:
                    result = await middleware.post_invoke(result)
                
                return {
                    "status": "success",
                    "result": result
                }
            except Exception as e:
                return {
                    "status": "error",
                    "error": str(e)
                }
    
    def register_tool(self, name: str, description: str, 
                     parameters: Dict, handler: callable):
        """
        Register a tool with schema
        """
        self.tools[name] = {
            'description': description,
            'parameters': parameters,
            'handler': handler
        }
    
    def add_middleware(self, middleware):
        """
        Add request/response middleware
        """
        self.middleware.append(middleware)


# Example: Document Search MCP Server
class DocumentSearchMCP(MCPServer):
    """
    MCP server for document search and retrieval
    """
    def __init__(self, document_store):
        super().__init__()
        self.doc_store = document_store
        
        # Register search tool
        self.register_tool(
            name="search_documents",
            description="Search documents by query",
            parameters={
                "query": {
                    "type": "string",
                    "description": "Search query",
                    "required": True
                },
                "max_results": {
                    "type": "integer",
                    "description": "Maximum results to return",
                    "default": 10
                },
                "filters": {
                    "type": "object",
                    "description": "Optional filters",
                    "required": False
                }
            },
            handler=self.search_handler
        )
        
        # Register retrieve tool
        self.register_tool(
            name="get_document",
            description="Retrieve full document by ID",
            parameters={
                "doc_id": {
                    "type": "string",
                    "description": "Document identifier",
                    "required": True
                }
            },
            handler=self.retrieve_handler
        )
    
    async def search_handler(self, params: Dict) -> List[Dict]:
        """
        Handle document search
        """
        query = params['query']
        max_results = params.get('max_results', 10)
        filters = params.get('filters', {})
        
        results = await self.doc_store.search(
            query=query,
            limit=max_results,
            **filters
        )
        
        return [
            {
                'id': doc.id,
                'title': doc.title,
                'snippet': doc.snippet,
                'relevance': doc.score
            }
            for doc in results
        ]
    
    async def retrieve_handler(self, params: Dict) -> Dict:
        """
        Handle document retrieval
        """
        doc_id = params['doc_id']
        doc = await self.doc_store.get(doc_id)
        
        return {
            'id': doc.id,
            'title': doc.title,
            'content': doc.content,
            'metadata': doc.metadata
        }


# Run the server
doc_store = DocumentStore()
server = DocumentSearchMCP(doc_store)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(server.app, host="0.0.0.0", port=8080)
```

## 🎯 Real-World MCP Implementations

### 1. Database MCP Server

```python
class DatabaseMCPServer(MCPServer):
    """
    MCP server for database access
    """
    def __init__(self, db_connection):
        super().__init__()
        self.db = db_connection
        
        self.register_tool(
            "query_database",
            "Execute read-only SQL query",
            {
                "sql": {"type": "string", "required": True},
                "limit": {"type": "integer", "default": 100}
            },
            self.query_handler
        )
    
    async def query_handler(self, params: Dict) -> List[Dict]:
        """
        Execute database query safely
        """
        sql = params['sql']
        limit = params.get('limit', 100)
        
        # Validate read-only
        if not sql.strip().upper().startswith('SELECT'):
            raise ValueError("Only SELECT queries allowed")
        
        # Execute with limit
        results = await self.db.execute(f"{sql} LIMIT {limit}")
        
        return [dict(row) for row in results]
```

### 2. API Wrapper MCP Server

```python
class APIWrapperMCPServer(MCPServer):
    """
    MCP server wrapping external API
    """
    def __init__(self, api_key: str):
        super().__init__()
        self.api_key = api_key
        
        self.register_tool(
            "get_weather",
            "Get weather for location",
            {
                "location": {"type": "string", "required": True}
            },
            self.weather_handler
        )
    
    async def weather_handler(self, params: Dict) -> Dict:
        """
        Fetch weather data
        """
        location = params['location']
        
        response = await http.get(
            f"https://api.weather.com/forecast",
            params={"location": location, "key": self.api_key}
        )
        
        return response.json()
```

## 🎯 Key Takeaways

- **MCP standardizes** how apps provide context to LLMs
- **Universal protocol** works across different systems
- **Plug-and-play** architecture enables reusability
- **Capability discovery** makes servers self-describing
- **Tool invocation** provides structured interactions

## Best Practices

### 1. Clear Tool Descriptions
```python
# ✅ Good: Detailed description
"Search customer database by name, email, or ID. Returns up to 10 matches."

# ❌ Bad: Vague description
"Search customers"
```

### 2. Parameter Schemas
```python
# ✅ Good: Detailed schema
{
    "query": {
        "type": "string",
        "description": "Search query",
        "required": True,
        "example": "john@example.com"
    }
}

# ❌ Bad: Minimal schema
{"query": "string"}
```

### 3. Error Handling
```python
# ✅ Good: Structured errors
{
    "status": "error",
    "error_code": "INVALID_QUERY",
    "message": "Query must be at least 3 characters",
    "retry_allowed": True
}

# ❌ Bad: Generic error
{"error": "Bad request"}
```

## Next Steps

Continue to [Agent2Agent Protocol (A2A)](./02-a2a.md) to learn about inter-agent communication.

---

💡 **Remember**: MCP is the universal adapter that makes your context providers work with any LLM client.
