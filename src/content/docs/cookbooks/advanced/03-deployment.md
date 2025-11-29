---
title: "🚀 Production Deployment: Scaling AI Agents"
description: Taking your AI agents from development to production at scale
---

## 🌳 Forest-Level Concept

**Label**: Deploying and Scaling AI Agents in Production

Moving AI agents from development to production requires careful attention to reliability, observability, cost management, and scalability.

## Production Architecture Overview

```
┌──────────────────────────────────────────────────────────────────┐
│                    Production AI System                          │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌─────────┐    ┌──────────┐    ┌─────────────┐                 │
│  │  Load   │───▶│  Agent   │───▶│  LLM Pool   │                 │
│  │Balancer │    │  Router  │    │(Multi-model)│                 │
│  └─────────┘    └──────────┘    └─────────────┘                 │
│       │              │                  │                        │
│       │              ▼                  ▼                        │
│       │       ┌──────────┐       ┌───────────┐                  │
│       │       │  Cache   │       │Rate Limiter│                  │
│       │       │  Layer   │       └───────────┘                  │
│       │       └──────────┘              │                        │
│       │              │                  ▼                        │
│       ▼              ▼           ┌───────────┐                  │
│  ┌─────────┐   ┌──────────┐     │ Monitoring │                  │
│  │ Metrics │   │ Logging  │     │ & Alerts   │                  │
│  └─────────┘   └──────────┘     └───────────┘                  │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

---

## 🌱 Seedling: Basic Production Setup

### Environment Configuration

```python
from dataclasses import dataclass
from enum import Enum
import os

class Environment(Enum):
    DEVELOPMENT = "development"
    STAGING = "staging"
    PRODUCTION = "production"

@dataclass
class Config:
    """Production configuration"""
    environment: Environment
    llm_api_key: str
    llm_model: str
    max_retries: int
    timeout_seconds: int
    cache_enabled: bool
    log_level: str
    
    @classmethod
    def from_env(cls) -> "Config":
        """Load config from environment variables"""
        env = Environment(os.getenv("ENVIRONMENT", "development"))
        
        return cls(
            environment=env,
            llm_api_key=os.environ["LLM_API_KEY"],
            llm_model=os.getenv("LLM_MODEL", "gpt-4"),
            max_retries=int(os.getenv("MAX_RETRIES", "3")),
            timeout_seconds=int(os.getenv("TIMEOUT_SECONDS", "30")),
            cache_enabled=os.getenv("CACHE_ENABLED", "true").lower() == "true",
            log_level=os.getenv("LOG_LEVEL", "INFO")
        )

# Usage
config = Config.from_env()
print(f"Running in {config.environment.value} mode")
```

### Basic Error Handling

```python
import asyncio
from typing import Optional
import logging

logger = logging.getLogger(__name__)

class RetryableError(Exception):
    """Error that can be retried"""
    pass

class FatalError(Exception):
    """Error that should not be retried"""
    pass

async def with_retry(
    func,
    max_retries: int = 3,
    base_delay: float = 1.0,
    max_delay: float = 60.0
):
    """
    Execute function with exponential backoff retry
    """
    last_exception = None
    
    for attempt in range(max_retries + 1):
        try:
            return await func()
        except FatalError:
            raise  # Don't retry fatal errors
        except Exception as e:
            last_exception = e
            
            if attempt < max_retries:
                delay = min(base_delay * (2 ** attempt), max_delay)
                logger.warning(
                    f"Attempt {attempt + 1} failed: {e}. "
                    f"Retrying in {delay}s..."
                )
                await asyncio.sleep(delay)
            else:
                logger.error(f"All {max_retries + 1} attempts failed")
    
    raise last_exception
```

---

## 🌿 Growing: Observability & Monitoring

### Structured Logging

```python
import json
import time
from contextlib import contextmanager
from typing import Dict, Any
import uuid

class StructuredLogger:
    """Production-ready structured logging"""
    
    def __init__(self, service_name: str):
        self.service_name = service_name
    
    def _log(
        self, 
        level: str, 
        message: str, 
        **kwargs
    ):
        """Emit structured log"""
        log_entry = {
            "timestamp": time.time(),
            "level": level,
            "service": self.service_name,
            "message": message,
            **kwargs
        }
        print(json.dumps(log_entry))
    
    def info(self, message: str, **kwargs):
        self._log("INFO", message, **kwargs)
    
    def warning(self, message: str, **kwargs):
        self._log("WARNING", message, **kwargs)
    
    def error(self, message: str, **kwargs):
        self._log("ERROR", message, **kwargs)
    
    @contextmanager
    def trace_request(self, request_id: str = None):
        """Context manager for request tracing"""
        request_id = request_id or str(uuid.uuid4())
        start_time = time.time()
        
        self.info("Request started", request_id=request_id)
        
        try:
            yield request_id
            duration_ms = (time.time() - start_time) * 1000
            self.info(
                "Request completed",
                request_id=request_id,
                duration_ms=duration_ms
            )
        except Exception as e:
            duration_ms = (time.time() - start_time) * 1000
            self.error(
                "Request failed",
                request_id=request_id,
                duration_ms=duration_ms,
                error=str(e)
            )
            raise

# Usage
logger = StructuredLogger("agent-service")

async def handle_request(input_data):
    with logger.trace_request() as request_id:
        # Process request
        result = await agent.process(input_data)
        logger.info(
            "Agent processed input",
            request_id=request_id,
            input_length=len(input_data),
            output_length=len(result)
        )
        return result
```

### Metrics Collection

```python
from collections import defaultdict
import time
from typing import Dict, List
import threading

class MetricsCollector:
    """Collect and report production metrics"""
    
    def __init__(self):
        self._counters: Dict[str, int] = defaultdict(int)
        self._histograms: Dict[str, List[float]] = defaultdict(list)
        self._gauges: Dict[str, float] = {}
        self._lock = threading.Lock()
    
    def increment(self, name: str, value: int = 1):
        """Increment a counter"""
        with self._lock:
            self._counters[name] += value
    
    def record_duration(self, name: str, duration_ms: float):
        """Record a duration to histogram"""
        with self._lock:
            self._histograms[name].append(duration_ms)
    
    def set_gauge(self, name: str, value: float):
        """Set a gauge value"""
        with self._lock:
            self._gauges[name] = value
    
    def get_summary(self) -> Dict[str, Any]:
        """Get metrics summary"""
        with self._lock:
            summary = {
                "counters": dict(self._counters),
                "gauges": dict(self._gauges),
                "histograms": {}
            }
            
            for name, values in self._histograms.items():
                if values:
                    sorted_vals = sorted(values)
                    summary["histograms"][name] = {
                        "count": len(values),
                        "min": sorted_vals[0],
                        "max": sorted_vals[-1],
                        "avg": sum(values) / len(values),
                        "p50": sorted_vals[len(values) // 2],
                        "p99": sorted_vals[int(len(values) * 0.99)]
                    }
            
            return summary

# Usage
metrics = MetricsCollector()

async def process_with_metrics(input_data):
    start = time.time()
    
    try:
        result = await agent.process(input_data)
        metrics.increment("requests.success")
        return result
    except Exception as e:
        metrics.increment("requests.error")
        raise
    finally:
        duration_ms = (time.time() - start) * 1000
        metrics.record_duration("request.duration_ms", duration_ms)
```

---

## 🌳 Forest: Production-Ready Agent Service

### Complete Agent Service

```python
from dataclasses import dataclass
from typing import Optional, Dict, Any
import asyncio
import hashlib
import json

@dataclass
class AgentResponse:
    """Standardized agent response"""
    request_id: str
    status: str
    result: Optional[str]
    error: Optional[str]
    latency_ms: float
    model_used: str
    tokens_used: int

class ProductionAgentService:
    """
    Production-ready agent service with:
    - Caching
    - Rate limiting
    - Circuit breaking
    - Monitoring
    """
    
    def __init__(
        self,
        agent,
        config: Config,
        cache,
        rate_limiter,
        metrics: MetricsCollector,
        logger: StructuredLogger
    ):
        self.agent = agent
        self.config = config
        self.cache = cache
        self.rate_limiter = rate_limiter
        self.metrics = metrics
        self.logger = logger
        
        # Circuit breaker state
        self._failure_count = 0
        self._circuit_open = False
        self._circuit_opened_at = 0
    
    async def process(
        self,
        input_data: str,
        user_id: str,
        request_id: str = None
    ) -> AgentResponse:
        """
        Process request with production safeguards
        """
        request_id = request_id or str(uuid.uuid4())
        start_time = time.time()
        
        with self.logger.trace_request(request_id):
            # Check circuit breaker
            if self._is_circuit_open():
                self.metrics.increment("circuit_breaker.rejected")
                return AgentResponse(
                    request_id=request_id,
                    status="error",
                    result=None,
                    error="Service temporarily unavailable",
                    latency_ms=0,
                    model_used="none",
                    tokens_used=0
                )
            
            # Check rate limit
            if not await self.rate_limiter.allow(user_id):
                self.metrics.increment("rate_limit.rejected")
                return AgentResponse(
                    request_id=request_id,
                    status="rate_limited",
                    result=None,
                    error="Rate limit exceeded",
                    latency_ms=0,
                    model_used="none",
                    tokens_used=0
                )
            
            # Check cache
            cache_key = self._cache_key(input_data)
            if self.config.cache_enabled:
                cached = await self.cache.get(cache_key)
                if cached:
                    self.metrics.increment("cache.hit")
                    latency_ms = (time.time() - start_time) * 1000
                    return AgentResponse(
                        request_id=request_id,
                        status="success",
                        result=cached["result"],
                        error=None,
                        latency_ms=latency_ms,
                        model_used=cached["model"],
                        tokens_used=0  # No tokens for cache hit
                    )
                self.metrics.increment("cache.miss")
            
            # Process request
            try:
                result = await with_retry(
                    lambda: self.agent.process(input_data),
                    max_retries=self.config.max_retries
                )
                
                # Record success
                self._record_success()
                
                # Cache result
                if self.config.cache_enabled:
                    await self.cache.set(cache_key, {
                        "result": result,
                        "model": self.config.llm_model
                    })
                
                latency_ms = (time.time() - start_time) * 1000
                self.metrics.record_duration("agent.latency_ms", latency_ms)
                self.metrics.increment("requests.success")
                
                return AgentResponse(
                    request_id=request_id,
                    status="success",
                    result=result,
                    error=None,
                    latency_ms=latency_ms,
                    model_used=self.config.llm_model,
                    tokens_used=self.agent.last_token_count
                )
                
            except Exception as e:
                self._record_failure()
                self.metrics.increment("requests.error")
                
                latency_ms = (time.time() - start_time) * 1000
                
                return AgentResponse(
                    request_id=request_id,
                    status="error",
                    result=None,
                    error=str(e),
                    latency_ms=latency_ms,
                    model_used=self.config.llm_model,
                    tokens_used=0
                )
    
    def _cache_key(self, input_data: str) -> str:
        """Generate cache key"""
        content = f"{self.config.llm_model}:{input_data}"
        return hashlib.sha256(content.encode()).hexdigest()
    
    def _is_circuit_open(self) -> bool:
        """Check if circuit breaker is open"""
        if not self._circuit_open:
            return False
        
        # Allow retry after cooldown
        if time.time() - self._circuit_opened_at > 30:
            self._circuit_open = False
            self._failure_count = 0
            return False
        
        return True
    
    def _record_success(self):
        """Record successful request"""
        self._failure_count = max(0, self._failure_count - 1)
    
    def _record_failure(self):
        """Record failed request"""
        self._failure_count += 1
        if self._failure_count >= 5:
            self._circuit_open = True
            self._circuit_opened_at = time.time()
            self.logger.warning("Circuit breaker opened")
```

### Rate Limiter

```python
import time
from collections import defaultdict

class TokenBucketRateLimiter:
    """Token bucket rate limiter"""
    
    def __init__(
        self,
        rate: float,  # tokens per second
        burst: int    # max tokens in bucket
    ):
        self.rate = rate
        self.burst = burst
        self._buckets: Dict[str, Dict] = defaultdict(
            lambda: {"tokens": burst, "last_update": time.time()}
        )
    
    async def allow(self, key: str) -> bool:
        """Check if request is allowed"""
        bucket = self._buckets[key]
        now = time.time()
        
        # Add tokens based on time elapsed
        elapsed = now - bucket["last_update"]
        bucket["tokens"] = min(
            self.burst,
            bucket["tokens"] + elapsed * self.rate
        )
        bucket["last_update"] = now
        
        # Check if we have a token
        if bucket["tokens"] >= 1:
            bucket["tokens"] -= 1
            return True
        
        return False
```

---

## 💡 Key Insights

### Production Checklist

- [ ] **Retry logic** with exponential backoff
- [ ] **Circuit breaker** to prevent cascade failures
- [ ] **Rate limiting** per user/tenant
- [ ] **Caching** for repeated queries
- [ ] **Structured logging** with request IDs
- [ ] **Metrics collection** (latency, errors, tokens)
- [ ] **Health checks** and readiness probes
- [ ] **Graceful shutdown** handling
- [ ] **Secret management** (no hardcoded keys)
- [ ] **Cost tracking** and alerts

### Common Pitfalls

| Pitfall | Solution |
|---------|----------|
| No timeout | Set timeout on all LLM calls |
| Missing retries | Implement exponential backoff |
| Cache stampede | Use lock or jitter |
| No rate limits | Implement per-user limits |
| Poor logging | Use structured logging + request IDs |

---

## ⚡ Quick Win: Add Basic Health Check

```python
from fastapi import FastAPI, Response

app = FastAPI()

@app.get("/health")
async def health_check():
    """Basic health check endpoint"""
    return {"status": "healthy"}

@app.get("/ready")
async def readiness_check():
    """Readiness check - verify dependencies"""
    try:
        # Check LLM connection
        await llm_client.ping()
        # Check cache connection
        await cache.ping()
        return {"status": "ready"}
    except Exception as e:
        return Response(
            content=json.dumps({"status": "not_ready", "error": str(e)}),
            status_code=503
        )
```

---

## 🔬 Deep Dive: Cost Management

```python
class CostTracker:
    """Track LLM usage costs"""
    
    PRICING = {
        "gpt-4": {"input": 0.03, "output": 0.06},
        "gpt-3.5-turbo": {"input": 0.001, "output": 0.002},
        "claude-3-opus": {"input": 0.015, "output": 0.075},
    }
    
    def __init__(self):
        self.usage = defaultdict(lambda: {
            "input_tokens": 0,
            "output_tokens": 0,
            "requests": 0
        })
    
    def record(
        self,
        model: str,
        input_tokens: int,
        output_tokens: int,
        user_id: str = "default"
    ):
        """Record usage"""
        self.usage[user_id]["input_tokens"] += input_tokens
        self.usage[user_id]["output_tokens"] += output_tokens
        self.usage[user_id]["requests"] += 1
        self.usage[user_id]["model"] = model
    
    def get_cost(self, user_id: str = "default") -> float:
        """Calculate cost for user"""
        usage = self.usage[user_id]
        model = usage.get("model", "gpt-4")
        prices = self.PRICING.get(model, self.PRICING["gpt-4"])
        
        input_cost = (usage["input_tokens"] / 1000) * prices["input"]
        output_cost = (usage["output_tokens"] / 1000) * prices["output"]
        
        return input_cost + output_cost
```

---

## 📖 Related Resources

- [Multi-Agent Systems](./01-multi-agent-systems/) - Scaling multi-agent deployments
- [Evaluation & Testing](./02-evaluation/) - Production testing strategies
- [Tool Ecosystems](../tools/03-tool-ecosystems/) - Integration with frameworks

---

*Built with ❤️ by HUB for learners who want to master AI × Human collaboration*

[← Back to Advanced Topics](./)
