<details><summary>Section 1: Design Applications (14%)</summary>


- Design a prompt that elicits a specifically formatted response  
- Select model tasks to accomplish a given business requirement  
- Select chain components for a desired model input and output  
- Translate business use case goals into a description of the desired inputs and outputs for the AI pipeline  
- Define and order tools that gather knowledge or take actions for multi-stage reasoning  
- Determine how and when to use Agent Bricks (Knowledge Assistant, Multiagent Supervisor, Information Extraction) to solve problems

## Databricks GenAI Exam – Structured Notes (100% Markdown)

---

### Design a Prompt That Elicits a Specifically Formatted Response
- [lifecycle-of-a-prompt](https://community.databricks.com/t5/technical-blog/foundation-models-api-prompting-guide-1-lifecycle-of-a-prompt/ba-p/77749)
- [structured-outputs](https://docs.databricks.com/aws/en/machine-learning/model-serving/structured-outputs)

### What You **MUST** Know (Exam Mindset)

You are tested on:

- Structured output prompting
- When to use few‑shot vs zero‑shot
- How to guarantee JSON / table / bullet‑point outputs
- Difference between **prompt instructions** vs **response_format (JSON schema)**

---

This section focuses on **how to design AI applications** by translating business requirements into effective prompt designs, model tasks, tool chains, and agent-based solutions.

---

### Goal
Ensure the model produces outputs in a **predictable, machine- or human-consumable format** (e.g., JSON, Markdown, tables).

### Key Design Techniques
- Explicitly specify the **output format**
- Provide a **schema or template**
- Constrain verbosity and style
- Include validation rules (e.g., “Do not include extra text”)

### Example Prompt
```text
You are an AI assistant.
Return the response strictly in JSON with the following schema:
{
  "summary": string,
  "risks": [string],
  "recommendation": string
}
Do not include explanations outside the JSON.

When to Use
- API integrations
- Downstream automation
- UI rendering
- Data extraction pipelines

```

### Step‑by‑Step Learning Path

#### Step 1: Understand Prompt Components

- **System prompt** → Defines role / persona
- **User prompt** → Task + constraints
- **Format instructions** → **ALWAYS last**

**References**
- Official Databricks guide
- Foundation Model Prompt Lifecycle

---

#### Step 2: Learn Structured Outputs

Databricks supports:

- Free‑form text  
- JSON (loose)  
- JSON with **strict schema enforcement**

**Exam Hint**

- If the output must be **machine‑readable**, use **structured outputs**, not only text instructions.

---

#### Step 3: Few‑Shot Prompting for Format Consistency

Use **examples only when output shape is unstable**.

**Conceptual example**

```json
Respond in JSON.

Example input:
The movie was great!

Example output:
{
  "sentiment": "positive",
  "score": 0.87
}

```

## 2. Select Model Tasks to Accomplish a Given Business Requirement

- Identify the core business problem  
- Map the problem to an AI task  

### Examples

- Customer support automation → Question Answering  
- Contract review → Information Extraction  
- Management reporting → Summarization  
- Sentiment tracking → Classification  
- Insight generation → Reasoning / Analysis  

# Goal

Match the business problem to the correct AI task.

---

## Common Business Needs → Model Tasks

| Business Requirement                 | Model Task                      |
|--------------------------------------|---------------------------------|
| Summarize reports                    | Text summarization              |
| Extract fields from documents        | Information extraction          |
| Answer customer questions            | Question answering              |
| Classify emails                      | Text classification             |
| Generate insights                   | Reasoning / analysis            |
| Translate content                   | Language translation            |

---

## Example

**Business need:**  
Reduce customer support response time  

**Selected task:**  
Retrieval‑augmented question answering

---

## 3. Select Chain Components for Desired Model Input and Output

- Break the solution into logical processing steps  
- Choose components that transform input to output effectively  

### Common Chain Components

- Input preprocessing (cleaning, chunking)  
- Context or knowledge retrieval  
- Reasoning or synthesis  
- Output formatting and validation  

---

## 4. Translate Business Use Case Goals Into AI Inputs and Outputs

- Express business goals in technical terms the AI can execute  

### Example

- **Business goal:** Identify risks in insurance contracts  
- **Input:** Contract text  
- **Processing:** Clause extraction + risk analysis  
- **Output:** Structured risk summary with severity levels  

---

## 5. Define and Order Tools for Multi-Stage Reasoning

- Identify tools required at each step  
- Define execution order to support reasoning  

### Typical Order

- Data or knowledge retrieval  
- Filtering or validation  
- Reasoning and synthesis  
- Action execution (if required)  

### Example

```text
Search policy database → Extract relevant clauses → Analyze risk → Generate recommendation

```

## 6. Determine How and When to Use Agent Bricks

### 6.1 Knowledge Assistant
- Used for grounded, reliable Q&A  
- Best for policy documents, manuals, FAQs  

### 6.2 Information Extraction Agent
- Used to convert unstructured data into structured formats  
- Ideal for contracts, invoices, emails  

### 6.3 Multiagent Supervisor
- Coordinates multiple agents  
- Best for complex, multi-step or multi-domain problems  

### Example
```text

Supervisor Agent
 ├─ Extraction Agent
 ├─ Analysis Agent
 └─ Summary Agent

```

</details>

<details><summary>  Section 2: Data Preparation - 14%  </summary>
# Section 2: Data Preparation for RAG Applications (Databricks AI Exam Guide)

This guide covers **data preparation concepts, design decisions, and implementation steps** required to build **high-quality Retrieval Augmented Generation (RAG)** systems on **Databricks**.


## 1. Apply a Chunking Strategy for a Given Document Structure and Model Constraints

### Step 1: Analyze the Source Document Structure
- Identify document type (PDF, HTML, Markdown, Text)
- Identify natural boundaries: sections, headings, paragraphs, tables

### Step 2: Understand Model Constraints
- Embedding model token limits
- LLM context window
- Similarity accuracy degradation with large chunks

### Step 3: Choose Chunking Strategy
- Fixed-size chunking
- Recursive / semantic chunking
- Sliding window chunking

### Step 4: Apply Overlap Correctly
- Typical overlap: 50–100 tokens
- Prevents loss of context at boundaries

---

## 2. Filter Extraneous Content That Degrades RAG Quality

### Step 1: Identify Low-Value Content
- Headers and footers
- Page numbers
- Legal disclaimers
- Navigation menus

### Step 2: Apply Cleaning Rules
- Regex-based filtering
- Whitelisting
- Deduplication

### Step 3: Normalize Content
- Whitespace cleanup
- Unicode normalization

### Step 4: Validate Quality
- Manual sampling
- Semantic validation

---

## 3. Choose the Appropriate Python Package for Document Extraction

### Packages by Format
- PDF: pypdf, pdfplumber
- OCR: pytesseract
- HTML: BeautifulSoup
- DOCX: python-docx
- CSV/XLSX: pandas

### Selection Criteria
- Preserve structure
- Minimize noise
- Deterministic output

---

## 4. Write Chunked Text into Delta Lake Tables in Unity Catalog

### Step 1: Define Schema
- document_id
- chunk_id
- chunk_text
- embedding
- source_uri
- metadata

### Step 2: Create Unity Catalog Table
- Managed Delta table
- Proper catalog and schema

### Step 3: Write to Delta Lake
- Append mode
- Schema enforcement

### Step 4: Register for Vector Search
- Embedding index enabled

### Step 5: Apply Governance
- Access controls
- Lineage tracking

---

## 5. Identify Needed Source Documents for High-Quality RAG

### Step 1: Define Knowledge Scope
- Expected user questions

### Step 2: Select High-Signal Sources
- Official documentation
- Internal SOPs

### Step 3: Exclude Low-Quality Sources
- Outdated or marketing materials

### Step 4: Validate Coverage
- Query-to-document mapping

---

## 6. Use Tools and Metrics to Evaluate Retrieval Performance

### Metrics
- Recall@K
- Precision@K
- Mean Reciprocal Rank (MRR)
- Latency

### Evaluation Tools
- MLflow
- Vector Search metrics
- Human evaluation

---

## 7. Design Retrieval Systems Using Advanced Chunking Strategies

- Hybrid chunking
- Metadata-aware chunking
- Adaptive chunk sizing
- Parent-child chunking

---

## 8. Explain the Role of Re-Ranking in the Retrieval Process

### Phase 1: Initial Retrieval
- Vector similarity search

### Phase 2: Re-Ranking
- Cross-encoder or LLM scoring

### Benefits
- Higher precision
- Reduced hallucination

### When to Use
- Complex queries
- Enterprise systems

---

## Exam Tips

- Focus on design decisions
- Understand governance and evaluation
- Know when and why to re-rank

  
</details>

<details><summary> Section 3: Application Development – 30% </summary>
</details>

<details><summary>Section 4: Assembling and Deploying Applications – 22%</summary>
</details>

<details><summary>Section 5: Governance – 8%</summary>
</details>

<details><summary>Section 6: Evaluation and Monitoring  – 12%</summary>
</details>

