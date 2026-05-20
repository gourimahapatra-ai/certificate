# Snowflake AI Features for Certification

# Cortex Search, Cortex Analyst, and Document AI

---

# 1. Snowflake Cortex Search

## What is Cortex Search?

Cortex Search is Snowflake’s AI-powered hybrid search engine used for:

- Semantic search
- Vector search
- Keyword search
- RAG (Retrieval-Augmented Generation)
- Enterprise AI chatbots

It allows users to search unstructured text data stored in Snowflake using natural language.

---

## Core Concept

Traditional SQL search:

```sql
WHERE NAME ILIKE '%apple%'
```

Cortex Search uses:
- Vector embeddings
- Semantic similarity
- Keyword ranking
- AI reranking

---

## Architecture Flow

1. Data stored in Snowflake
2. Cortex creates embeddings
3. Search index created
4. User sends query
5. Hybrid retrieval occurs
6. AI reranking
7. Relevant documents returned

---

## Main Use Cases

### RAG Applications

Used with LLM chatbots.

### Enterprise Search

Search across:
- PDFs
- policies
- contracts
- tickets
- knowledge bases

---

## Important Certification Topics

### Cortex Search Uses

- Hybrid search
- Vector embeddings
- Semantic ranking
- Low-latency retrieval

---

## Important Terms

| Term | Meaning |
|---|---|
| Embedding | Numeric vector representation |
| Vector Search | Semantic similarity search |
| RAG | Retrieval-Augmented Generation |
| Hybrid Search | Keyword + semantic search |
| Reranking | AI relevance optimization |

---

## Important Command

```sql
CREATE CORTEX SEARCH SERVICE
```

---

## Security

Cortex Search supports:
- RBAC
- Snowflake governance
- Owner rights

---

# 2. Snowflake Cortex Analyst

## What is Cortex Analyst?

Cortex Analyst is Snowflake’s natural language to SQL AI engine.

It allows users to ask questions like:

> “Show top sales regions this quarter”

without writing SQL.

---

# Main Purpose

Converts:

Natural Language → SQL Query

using:
- semantic models
- LLMs
- metadata
- business logic

---

# Major Certification Concept

## Cortex Analyst is for Structured Data

| Feature | Data Type |
|---|---|
| Cortex Search | Unstructured text |
| Cortex Analyst | Structured tables |

---

# How It Works

1. User asks question
2. Semantic model guides LLM
3. Analyst generates SQL
4. SQL executes in Snowflake
5. Results returned

---

# Semantic Model

Semantic models define:
- metrics
- dimensions
- relationships
- business meanings
- verified queries

This improves SQL accuracy.

---

# Key Benefits

## Self-Service Analytics

Non-technical users can query data.

## Deterministic SQL

Cortex Analyst:
- reduces hallucinations
- improves governance
- uses semantic models

---

# Important Exam Topics

- Text-to-SQL
- Conversational analytics
- BI assistants
- Natural language querying

---

# Important Certification Difference

| Cortex Search | Cortex Analyst |
|---|---|
| Semantic retrieval | Text-to-SQL |
| Unstructured data | Structured data |
| RAG applications | Analytics applications |
| Vector search | SQL generation |

---

# Common Exam Question

## Which feature converts natural language into SQL?

Answer:
- Cortex Analyst

---

# 3. Snowflake Document AI

## What is Document AI?

Document AI extracts structured information from documents using AI.

---

# Main Purpose

Convert documents into structured data.

---

# Supported Inputs

- PDFs
- invoices
- receipts
- contracts
- forms
- statements
- scanned documents

---

# Extracted Information

- text
- tables
- signatures
- handwritten content
- entities
- checkboxes

---

# Important Certification Concept

Document AI handles:

## Unstructured Documents → Structured Data

---

# Example Use Cases

## Invoice Processing

Extract:
- invoice number
- amount
- vendor
- date

---

## Financial Statements

Extract tables automatically.

---

## Contract Intelligence

Extract:
- customer names
- clauses
- dates

---

# AI Model

Document AI uses:
- Arctic-TILT model

---

# Pipeline Support

Supports:
- continuous ingestion
- automated extraction pipelines

---

# Comparison Table

| Feature | Cortex Search | Cortex Analyst | Document AI |
|---|---|---|---|
| Purpose | Semantic retrieval | Text-to-SQL | Document extraction |
| Data Type | Unstructured text | Structured tables | PDFs/images/docs |
| Uses AI | Yes | Yes | Yes |
| Main Use Case | RAG | Analytics assistant | OCR + extraction |
| Output | Relevant text | SQL/results | Structured fields |

---

# Most Important Certification Questions

## Q1. Which Snowflake feature powers RAG?

Answer:
- Cortex Search

---

## Q2. Which feature converts natural language to SQL?

Answer:
- Cortex Analyst

---

## Q3. Which feature extracts fields from PDFs?

Answer:
- Document AI

---

## Q4. Which feature uses semantic models?

Answer:
- Cortex Analyst

---

## Q5. Which feature uses vector search?

Answer:
- Cortex Search

---

# Easy Memory Tricks

## Cortex Search

Think:
“Search meaning”

---

## Cortex Analyst

Think:
“Ask business questions”

---

## Document AI

Think:
“Read documents automatically”

---

# Architecture-Level Understanding

```text
Documents/PDFs
        ↓
Document AI
        ↓
Structured Data in Snowflake
        ↓
Cortex Search indexes content
        ↓
Cortex Analyst answers business questions
        ↓
LLM applications / AI chatbots
```

---

# Conclusion

Snowflake Cortex services are transforming AI-powered analytics inside Snowflake.

For certification preparation, focus heavily on:
- RAG concepts
- Semantic search
- Text-to-SQL
- Semantic models
- Vector search
- AI governance
- Unstructured data processing
