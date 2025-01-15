# Building applications with LLMs


Tutorial on building applications with LLMs
 
 
**What:** At the end of this workshop, you should be able to build an LLM-based application, understand basic concepts (e.g. 'Vector database', 'RAG', 'Chain of Thought', etc.), and know some frameworks (e.g. 'LangChain', ‘LangGraph’, 'MCP', etc.)
 

**Who:** The audience are people with knowledge on programing, and basic understanding of what an LLM is, who want to build applications based on these technologies. Note: We are NOT going to build LLMs from scratch, fine-tune them, etc. (there might be another workshop about this in the future).
 
 
**How:** This will be a workshop, with hands-on coding. For this specific workshop we'll be using Python, but the language doesn't really matter (the concepts are the same in other programming languages).
 

## Agenda
 
- LLMs: Brief recap
    - Transformers, Tokens, Context window, Embeddings, etc.
    - Pre-training, training, RHFS, etc.
    - Models: OpenAI, Claude, Llama (running a local model)
 
- LLM's API
    - OpenAI example
    - Concepts: Roles, Function calls, tools, etc.
- LangChain
  - Concepts: model, prompt, prompt template
  - Coding exercise 1
  - Structured outputs
  - Agents: Functions and Tools
  - Coding exercise 2
  - LangGraph / Multi-Agents
  - Prompt Engineering: Chain of thought, Tree of thought, RAG, etc.
  - Debugging
 
- ChainLit:
  - Introduction and concepts
  - Coding exercise 3
 
- RAG
  - Vector databases
  - Pre-process, Chunking, Indexing
  - Query translation, Re-ranking.
  - Coding exercise 4
 
- Code walk-through: “GxP test cases generation”

Additional topics, if we have time (or for the next Workshop)
- MCP
- Evals
- VS-Code application
- RAG advanced techniques:
    - Multi-representation, Raptor, Colbert, etc.
    - Multi-Query, RAG Fusion, Decomposition, Step back, HyDE
    - Graph-based RAG
 


- LLM recap: Brief recap
  - LLM as an autoregressive model
  - "Attention is all you need"
  - "Scaling laws"
    - Transformers
    - Tokens
    - Context window
    - Embeddings, etc.
    - Pre-training, training, RHFS, etc.
    - Models: 
    - Closed: OpenAI, Claude
    - "Open": Llama, Local models: `Ollama`

- LLM's API Recap
    - OpenAI example
    - User, system, function calls, tools

- LangChain
  - Model, prompt, prompt template
  - Coding excercise 1
  - Structured outputs
  - Agents: Functions and Tools
  - Coding excercise 2
  - LangGraph / Multi-Agents

- ChainLit
  - Coding excercise 3

- Prompt Engineering: Chain of thought, Tree of thought, RAG, etc.

- RAG
  - Vector databases
  - Pre-process, Chunking, Indexing
  - Query translation, Re-ranking.
  - Coding excercise 4

Additionals topics if we have time (or for the next Workshop)
- Code walk-throught: `GxP test generation`
- Evals
- MCP
  - Concepts: host, server, resources
  - Protocol transports: stdio, sse
  - Example: 
    - Server
    - Manually running a server (type on stdin)
    - Client
    - Integration with an LLM
  - [Server features](https://spec.modelcontextprotocol.io/specification/server/): Prompts, Resources, Tools
  - [Client features](https://spec.modelcontextprotocol.io/specification/client/):
    - Roots, 
    - Sampling: "Sampling in MCP allows servers to implement agentic behaviors, by enabling LLM calls to occur nested inside other MCP server features."
  - Creating your own server
    - SQL databases
    - Analitics
    - RAG
    - Python code
- VS-Code application
- RAG advanced techniques:
    - Multi-representation, Raptor, Colbert, etc.
    - Multi-Query, RAG Fusion, Decomposition, Step back, HyDE
    - Graph-based RAG

  
```
# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Logoff & log-in so that changes in .bashrc take affect

# Check python's version, should be something modern (as of early 2025 is 3.12)
python3 --version 

# Create virtual environment 'vllm' and activate it
uv venv vllm --python 3.12 --seed
cd vllm
source bin/activate

# Install vllm
uv pip install vllm

# Check if it works
vllm --help
```

### Install dependencies

```
sudo -i

apt-get install git-lfs
```

### Pre download models

```
# Download a small model
git clone https://huggingface.co/albert-base-v2.git
```

 

 