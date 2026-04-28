<details><summary>RAG Chunk Size — How to Know What Size Is Required</summary># 

Choosing the right **chunk size** is about balancing **retrieval accuracy**, **ranking quality**, and **LLM context limits**. There is no universal size — it depends on *document type* and *use case*.

---

## ✅ Core Rule (1‑Line)
> Use the **smallest chunk size that still contains all information needed to answer a question correctly**.

---

## 🔑 How to Decide the Right Chunk Size

### 1. **Based on Question Type**
| Question Style | Recommended Chunk Size |
|----------------|------------------------|
| Fact lookup / FAQ | Small (200–400 tokens) |
| Concept explanation | Medium (400–800 tokens) |
| Legal / policy reasoning | Medium–Large (800–1,200 tokens) |
| Long summaries | Larger (1,000+ tokens) |

---

### 2. **Based on Metrics (Most Important)**
Use evaluation metrics to guide size:

- **Low Recall** → Chunks are *too small* (info split across chunks)
- **Low NDCG / Precision** → Chunks are *too large* (contain noise)
- **Hallucinations** → Chunks lack complete context

✅ **Best practice**:
> Test multiple chunk sizes and choose the one with **highest Recall + NDCG**.

---

### 3. **Based on Document Structure**
| Document Type | Chunking Strategy |
|---------------|------------------|
| Research papers | Section‑based chunks |
| Legal documents | Clause / article‑based |
| Manuals | Paragraph‑based |
| FAQs | One Q&A per chunk |

---

### 4. **Based on LLM Context Window**
- Retrieval chunks × number of chunks must fit inside the **LLM context length**
- Example:
  - 4 chunks × 500 tokens = 2,000 tokens (safe)
  - 4 chunks × 1,500 tokens = 6,000 tokens (too large for many models)

---

## ✅ Recommended Starting Defaults
| Scenario | Chunk Size | Overlap |
|--------|-----------|---------|
| General RAG | 500–800 tokens | 10–20% |
| Legal / policy | 800–1,200 tokens | 15–20% |
| Technical docs | 400–600 tokens | 10% |

---

## ✅ Final Exam‑Ready Summary

> Chunk size is chosen by **evaluating Recall and NDCG** across different sizes. Small chunks improve precision, large chunks improve recall. The optimal size preserves semantic completeness while fitting within the LLM context window.
</details>

<details><summary>Compound AI Systems</summary>

## Overview
Compound AI Systems combine multiple AI components to solve complex problems.

## Key Points
- Systems like Retrieval-Augmented Generation (RAG) are examples of compound AI.
- RAG is a pipeline designed for a specific task.
- It enhances responses using external data.

## RAG Pipeline Steps
1. Retrieve relevant documents for context
2. Build prompts using retrieved context
3. Generate the final response


# Intent Classification and Chain Building

## Overview
This process helps design AI workflows by identifying user intent and structuring tasks.

## Key Steps

### 1. Identify Intents
- Analyze sample user queries
- Define possible user goals or intents

### 2. Identify Task Dependencies
- Determine if tasks are:
  - Sequential (step-by-step)
  - Parallel (independent subtasks)

### 3. Identify Required Tools
- Web search
- API interaction
- Code execution
- Text-to-speech / Speech-to-text
- Other relevant services

### 4. Build the Workflow (Chain)
- Connect tasks logically into a pipeline
- Ensure smooth data flow between steps

### 5. Choose Architecture
- Select appropriate system design:
  - RAG (Retrieval-Augmented Generation)
  - Text-to-SQL
  - Other AI architectures

### 6. Iterate and Improve
- Continuously refine intents, tools, and workflow

## Summary Flow
1. Identify Intents  
2. Identify Tools  
3. Build the Chain  
</details>

<details><summary>Designing of AI Systems</summary>

## Overview
Designing modern AI systems involves building **compound AI systems** using specialized frameworks and tools. These systems combine multiple components to handle complex tasks efficiently.

## Key Trends
- Need for new tools to build compound AI systems
- Rise of **composition frameworks** for structuring workflows
- Growing use of **agent-based systems**

## Popular Frameworks

### Composition Frameworks
- LangChain
- LlamaIndex
- Haystack
- DSPy

### Agent Libraries
- LangChain (Agents)
- AutoGPT


# LangChain

## Overview
LangChain is a framework for building **Generative AI applications** using large language models (LLMs).

## Key Features
- Enables context-aware and dynamic applications
- Supports reasoning and interaction with external data sources
- Provides pre-built components for common tasks

## Core Components

### Prompt
- Structured input to guide the LLM’s output

### Chain
- Sequence of steps that process input and generate output

### Retriever
- Fetches relevant data/documents for context

### Tool
- External resources (APIs, DBs, functions) used by agents


# LlamaIndex

## Overview
A data framework that improves LLM performance by **structuring and indexing data**.

## Components
- Models
- Prompts
- Indexing & Storage
- Querying
- Agents


# Haystack

## Overview
An open-source Python framework for building LLM applications focused on **search and retrieval tasks**.

## Components
- Generators
- Retrievers
- Document Stores
- Pipelines


# DSPy

## Overview
A framework for programming LLMs and Retrieval Models with a **structured and composable approach**, beyond manual prompting.

## Components

### Signatures
- Declarative modules guiding LLM behavior
- Examples: ChainOfThought, Retrieve, ReAct

### Teleprompters
- Optimize programs into prompts or fine-tuned models

### Automatic Compiler
- Converts workflows into high-quality prompts
- Can also fine-tune models automatically

</details>


<details><summary>Choosing a Library (AI Systems)</summary>

## Overview
Selecting the right library is critical for building scalable and efficient AI systems.

## Key Considerations

### 1. Use Case Fit
- Ensure the library supports your specific requirements and problem type

### 2. LLM Support
- Check compatibility with multiple LLMs and interfaces

### 3. Integration Capabilities
- Evaluate how easily it connects with:
  - External data sources
  - Knowledge bases

### 4. Performance & Scalability
- Assess ability to handle:
  - Large data volumes
  - High-throughput workloads

### 5. Stability & Maturity
- Libraries evolve rapidly
- API instability can be a major challenge

### 6. Ease of Use
- Some libraries may have a steep learning curve
- Consider developer experience and documentation quality

## Summary
Choose a library that balances:
- Functionality
- Scalability
- Stability
- Ease of use

</details>

<details><summary>Foundation Model API</summary>

## Overview
Provides a unified interface to access, deploy, and manage foundation models for building Generative AI applications.

## Key Features
- Instant access to popular foundation models
- Flexible pricing:
  - Pay-per-token (for prototyping)
  - Provisioned throughput (for high-scale applications)
- Integration with external providers:
  - Azure OpenAI
  - AWS Bedrock
- Unified interface for:
  - Deployment
  - Governance
  - Querying models

## Supported Models & Tasks
- DBRX Instruct → Chat
- Meta Llama 3.1 (70B / 405B) → Chat
- Mixtral-8x7B Instruct → Chat
- GTE Large (English) → Embeddings


# DBRX (Databricks LLM)

## Overview
An open-source Large Language Model developed by Databricks.

## Variants

### DBRX Base
- Pretrained model
- Works like autocomplete
- Suitable for fine-tuning on custom data

### DBRX Instruct
- Fine-tuned for:
  - Question answering
  - Instruction following
- Built on top of DBRX Base

# Vector Search

## Overview
A vector database integrated into the Databricks platform for similarity search.

## Key Features
- Stores vector embeddings + metadata
- Integrated with Lakehouse architecture
- Scalable and low-latency
- Zero operational overhead
- Supports access control (ACLs via Unity Catalog)

## Capabilities
- Real-time similarity search
- Metadata filtering
- APIs:
  - REST API
  - Python SDK

## Architecture Components
- Source Delta Table
- Vector Indexer
- Vector Database
- Auto-sync pipeline


# Mosaic AI Agent Framework

## Overview
A toolkit for building, evaluating, and deploying high-quality GenAI applications.

## Key Capabilities
- Evaluate RAG application quality
- Rapid iteration and redeployment
- Built-in governance and guardrails

# MLflow Tracing (within Mosaic AI)

## Overview
Enables tracking and debugging of GenAI applications.

## Features
- Logs inputs, outputs, and intermediate steps (traces & spans)
- Visual trace analysis
- Debugging support

## Benefits
- Compare different models and configurations
- Measure latency impact
- Track token usage and cost

# Logging & Monitoring

## Overview
Captures application state for evaluation and improvement.

## Key Points
- Logs code and configuration at a specific point in time
- Code-based logging is recommended over serialization
- Integrates with MLflow tracking

## Benefits
- Automatic tracking of:
  - Parameters
  - Metrics
- Helps improve model performance and reliability

# Other Databricks Products (AI Systems)

## Overview
Databricks provides additional tools for **logging, deployment, evaluation, and monitoring** of AI systems.

## Key Products

### 1. Mosaic AI Agent Evaluation (*)
- Evaluates GenAI applications (including RAG and chains)
- Measures:
  - Quality
  - Cost
  - Latency

### 2. MLflow Evaluation (*)
- Computes and manages evaluation metrics
- Helps assess model and application performance

### 3. Model Serving (**)
- Deploys custom:
  - Chains
  - Pipelines
- Enables real-time inference

### 4. Lakehouse Monitoring (**)
- Monitors performance of deployed applications
- Tracks system behavior over time

## Notes
- (*) Covered in: *Generative AI Evaluation and Governance*
- (**) Covered in other advanced courses

## Summary
These tools support the full AI lifecycle:
- Evaluation → MLflow, Mosaic AI Agent Evaluation  
- Deployment → Model Serving  
- Monitoring → Lakehouse Monitoring  

</details>

<details><summary>Agent Workflow & Reasoning in AI Systems</summary>

## Example Use Case
**Task:** Determine if it is the right time to invest in NVIDIA stock

### Key Questions (Data Requirements)
- What is the current stock price?
- What are the latest financials?
- What is the latest news/announcements?
- What is the current sentiment score?

---

# Agent Workflow

## Step-by-Step Process

### 1. Task Processing
- Agent uses an LLM to:
  - Understand the user query
  - Decide required actions

### 2. Data Collection
- Gather relevant data:
  - Stock prices
  - Financial reports
  - News articles
  - Market sentiment

### 3. Data Analysis
- Use LLMs to:
  - Analyze financial data
  - Perform sentiment analysis

### 4. Output Generation
- Synthesize insights into:
  - A clear, coherent report
  - Actionable recommendation


# Agent Reasoning

## Overview
Agent reasoning is the process by which AI systems:
- Analyze information
- Make decisions
- Act autonomously (similar to human reasoning)

## Common Reasoning Patterns

### 1. ReAct (Reason + Act)
- Combines reasoning and actions

#### Key States:
- **Thought** → Reflect on problem and prior steps
- **Act** → Choose tool/action
- **Observe** → Evaluate result and continue

### 2. Tool Use / Function Calling
- Agents interact with external tools and APIs

#### Example Tools:
- **Search & Research:** Web search, Wikipedia
- **Retrieval:** Databases, Vector DBs
- **Image Tasks:** Image generation, classification
- **Coding:** Code execution, debugging

---

### 3. Planning
- Agents dynamically plan tasks based on goals

#### Task Types:
- Single task
- Sequential tasks
- Graph-based workflows (complex dependencies)


### 4. Multi-Agent Collaboration
- Multiple agents work together on complex problems

#### Benefits:
- Specialization of agents
- Better scalability
- Modular system design
- Each agent can use different or fine-tuned LLMs

# Summary

## Agent Decision Flow
1. Understand task  
2. Plan actions  
3. Use tools to gather data  
4. Analyze results  
5. Generate final output  

## Key Insight
Effective AI agents combine:
- Reasoning (ReAct, Planning)
- Tool usage
- Collaboration (multi-agent systems)
</details>

<details><summary>Multimodal AI Systems</summary>

  ## Overview
Multimodal AI systems handle multiple data types (modalities), such as:
- Text
- Images
- Audio
- Video

Each modality introduces unique challenges in processing and integration.

---

## Key Challenges
- Different data formats and representations
- Complexity in combining modalities
- Storage and retrieval across heterogeneous data types

---

## Approaches for Handling Multiple Modalities

### 1. Shared Embedding Space
- Embed all modalities into a **single vector space**
- Example: CLIP
- Enables cross-modal understanding (e.g., text ↔ image search)

### 2. Primary Modality Grounding
- Select one main modality (e.g., text)
- Map all other modalities to this primary representation
- Useful when one modality dominates the application

### 3. Separate Embeddings
- Store each modality independently
- Combine results during retrieval or processing
- Offers flexibility but increases system complexity

---

## Multimodal LLMs (MLLMs)

## Overview
- Advanced models capable of handling multiple modalities
- Can generate outputs in different formats

### Key Capabilities
- Understand and process mixed inputs (text + image, etc.)
- Generate multimodal outputs

### Example
- Generate a story along with relevant images

---

## Summary
Multimodal AI systems:
- Integrate diverse data types
- Use different embedding strategies
- Are powered by emerging Multimodal LLMs for richer interactions
  
</details>


<details><summary></summary></details>

<details><summary></summary></details>

<details><summary></summary></details>
