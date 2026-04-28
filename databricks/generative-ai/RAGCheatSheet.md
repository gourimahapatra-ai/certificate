# 📌 One‑Page RAG (Retrieval‑Augmented Generation) Metrics Cheat Sheet

This cheat sheet maps **RAG pipeline components** to the **right evaluation metrics**, explaining *what to measure, why it matters, and when to use it*.

---

## 🧱 RAG Pipeline Overview

User Query → Retriever → Ranked Documents → LLM Generator → Final Answer

---

## 🔍 1. Retriever Evaluation Metrics

### ✅ Recall
**What it measures:**  
- Whether *all relevant documents* were retrieved

**Why it matters:**  
- Missing critical context = incorrect or incomplete answers  
- Especially important for **legal, medical, compliance** domains

✅ Use when:
- Coverage is more important than ranking
- Evaluating chunking strategies or embedding recall

---

### ✅ Precision
**What it measures:**  
- Whether retrieved documents are *actually relevant*

**Why it matters:**  
- Reduces noise and irrelevant context
- Improves generation quality

✅ Use when:
- Users complain about irrelevant results
- Tuning filters or retrievers

---

### ✅ NDCG (Normalized Discounted Cumulative Gain)
**What it measures:**  
- **Ranking quality** of retrieved documents

**Why it matters:**  
- Highly relevant docs should appear **earlier**
- LLMs pay more attention to top-ranked context

✅ Use when:
- Comparing embedding models
- Evaluating re‑rankers
- Optimizing chunking and retrieval order

---

### ✅ MRR (Mean Reciprocal Rank)
**What it measures:**  
- How quickly the first relevant document appears

✅ Use when:
- Questions expect a *single correct document*
- FAQ or knowledge-base search

---

## ✍️ 2. Generation Evaluation Metrics

### ✅ ROUGE
**What it measures:**  
- Overlap between generated text and reference answers

**Why it matters:**  
- Validates factual grounding
- Common for **summarization-heavy RAG**

✅ Use when:
- Evaluating summaries (legal, clinical, reports)

---

### ✅ BLEU
**What it measures:**  
- N‑gram precision of generated text

✅ Use when:
- Output wording must closely match references
- Less common for open-ended RAG

---

## 🤖 3. LLM‑as‑a‑Judge Metrics

### ✅ Faithfulness
**Question:**  
> Does the answer rely only on retrieved context?

✅ Detects hallucinations

---

### ✅ Relevance
**Question:**  
> Does the answer address the user’s question?

---

### ✅ Groundedness
**Question:**  
> Can each claim be traced to retrieved documents?

✅ Critical for regulated domains

---

## 📄 4. Chunking Evaluation Metrics

| Metric | What It Evaluates |
|------|------------------|
| Recall | Is important info present in chunks? |
| NDCG | Are the best chunks ranked highest? |
| LLM‑as‑Judge | Is the answer well supported by chunks? |

✅ Use when:
- Tuning chunk size, overlap, structure

---

## 🧠 5. End‑to‑End RAG Metrics

### ✅ Answer Accuracy (Human or LLM‑Judged)
- Overall correctness of final answer

### ✅ Citation Accuracy
- Whether answers correctly reference source docs

### ✅ User Satisfaction
- Implicit metric via thumbs‑up / feedback

---

## 🧩 Metric Selection by Use Case

| Use Case | Most Important Metrics |
|--------|------------------------|
| Legal RAG | Recall, ROUGE, Faithfulness |
| Medical RAG | Recall, Groundedness |
| Enterprise Search | Precision, NDCG |
| FAQ Chatbot | MRR, Precision |
| Long Docs | Recall, NDCG |

---

## ✅ Exam‑Ready Summary

> **Recall ensures coverage, Precision reduces noise, NDCG evaluates ranking quality, ROUGE measures generated content relevance, and LLM‑as‑a‑judge metrics assess faithfulness and grounding. Together, they provide full RAG evaluation coverage.**
