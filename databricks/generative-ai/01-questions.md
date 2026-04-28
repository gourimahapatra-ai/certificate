<details>
  <summary>
    MLflow
  </summary>
  MLflow is designed for managing the machine learning lifecycle, allowing experiment tracking, artifact logging, and easy deployment.
</details>

<details>
  <summary>profanity filter
  </summary>A profanity filter does not enhance relevance to financial news, as it is focused on language safety rather than domain-specific content.
</details>

<details>
  <summary>
    unstructured Python library
  </summary>
  The unstructured Python library is specifically designed for handling PDFs, including those with both text and images, and requires minimal coding effort.
</details>

<details>
  <summary>
    Embeddings and retrieval systems
  </summary>
  Embeddings and retrieval systems enable dynamic risk evaluation, clause suggestions, and contract summarization effectively.
</details>

<details>
  <summary>Summary of Key Generative AI Engineering Concepts   </summary>
1. **Retriever–LLM Combination for Accuracy**  
   Combining retrievers with LLMs ensures accurate, requirement-aligned answers for inventory and knowledge-based queries by grounding generation in relevant data.

2. **LLM Selection for Cost–Performance Balance**  
   - **Key Metric**: *Latency and inference cost per query*  
   - Low latency ensures responsiveness, while low inference cost supports scalable, economical deployment.

3. **Mitigating Hallucination and Data Leakage**  
   - **Approach NOT recommended**: Fine-tuning alone  
   - Fine-tuning cannot reliably prevent hallucinations or confidential data leakage without additional safeguards.

4. **Improving RAG Retrieval Relevance**  
   - **Technique**: Timestamp-based document filtering  
   - Excluding outdated documents improves contextual relevance and response accuracy.

5. **Evaluating Chunking Strategies**  
   - Use systematic evaluation with **recall**, **NDCG**, and **LLM-as-a-judge** metrics  
   - Test chunking methods (e.g., paragraph vs. chapter splitting) and select the highest-performing strategy.

6. **Multi-Turn Dialogue and Context Retention**  
   - **Essential Tool**: Memory module in the LLM workflow  
   - Enables storage and retrieval of past interactions for contextual, follow-up responses.

7. **Generating Customer Response Templates**  
   - **Required Component**: LLM  
   - LLMs dynamically generate structured templates (greeting, resolution, follow-up) from common queries.

8. **Embedding Strategy for Q&A Retrieval**  
   - **Best Practice**: Dual-encoder model  
   - Separately embeds short queries and long documents for better semantic alignment.

9. **Critical Components of a Healthcare RAG Pipeline (4)**  
   1. Secure document retriever with access controls  
   2. Domain-specific (healthcare-trained) embedding model  
   3. Low-latency GPU infrastructure  
   4. Clinical-report-optimized summarizer model  

10. **Intent Extraction from Chatbot Queries**  
    - **Recommended Model**: Sentence Transformers  
    - Well-suited for capturing semantic meaning and user intent.

11. **Reducing Irrelevant Retrieval Results**  
    - **Primary Focus**: Precision  
    - Improves relevance by reducing the number of incorrect or unrelated results.

12. **Evaluating Legal Document Summaries**  
    - **Metrics**: ROUGE and Recall  
    - ROUGE measures relevance and overlap, while recall ensures key content coverage.

</details>

<details><summary>Evaluating a RAG System Trained on Legal Documents</summary>

## ✅ Recommended Metrics and Tools (Choose Two)

### 1. **Recall**
- Measures whether **all relevant legal documents or clauses** are retrieved.
- Critical in legal applications where **missing information can lead to incorrect or risky conclusions**.

**Why it matters in Legal RAG:**
- Legal queries often require *complete coverage*.
- High recall ensures no important statutes, precedents, or clauses are omitted.

---

### 2. **ROUGE**
- Evaluates overlap between the **generated response** and **reference legal texts**.
- Commonly used for **summarization and answer quality** evaluation.

**Why it matters in Legal RAG:**
- Helps ensure generated answers are:
  - Faithful to source documents
  - Not hallucinated
  - Properly grounded in legal language

---

## 🔗 How NDCG Relates (Important Context)

### **NDCG (Normalized Discounted Cumulative Gain)**
- Measures **ranking quality** of retrieved documents.
- Rewards systems that place **highly relevant legal documents at the top**.

**What NDCG evaluates:**
- Retriever performance only (not generation)
- Quality of document ordering

**Why it complements Recall and ROUGE:**
- Recall → *Did we retrieve everything important?*
- NDCG → *Are the most important documents ranked first?*
- ROUGE → *Is the generated legal answer accurate and faithful?*

---

## ✅ Final Exam-Ready Summary

> A RAG system trained on legal documents should be evaluated using **Recall** to ensure complete retrieval of relevant materials and **ROUGE** to assess the relevance and faithfulness of generated responses. **NDCG** complements these metrics by measuring retrieval ranking quality.

---

## 📌 Metric-to-Component Mapping

| RAG Component | Metric |
|--------------|--------|
| Retriever (coverage) | Recall |
| Retriever (ranking) | NDCG |
| Generator (answer quality) | ROUGE |

---

If you want, I can also:
- Create a **one-page RAG metrics cheat sheet**
- Show **how to compute Recall vs NDCG vs ROUGE**
- Map these metrics to **interview questions**

</details>


<details><summary>Selecting an Embedding Model for Long Research Papers</summary>

## ✅ Most Critical Factors (Choose Two)

1. **Semantic Similarity Accuracy**
   - Ensures that user queries retrieve the **most relevant research papers or sections**.
   - Critical for search engines where understanding nuanced academic language and intent matters.

2. **Context Length Supported by the Embedding Model**
   - Allows the model to process and represent **long-form documents** such as research papers.
   - Prevents loss of meaning that can occur when long documents are truncated or overly chunked.

---

## ❌ Factors That Are Less Critical

- **Token Diversity**  
  Not a meaningful metric for evaluating embedding quality.

- **Cost of Inference**  
  Important for scalability, but **does not directly impact embedding quality** for long documents.

- **Training Dataset Size**  
  Secondary to actual task performance and embedding effectiveness.

---

## ✅ Final Summary

> For a search engine handling long research papers, the most critical factors when choosing an embedding model are **high semantic similarity accuracy** and **support for long context lengths**, as they ensure relevant, accurate retrieval and proper representation of lengthy documents.
</details>
