# Databricks Generative AI Concepts — Summary

## 1. What is a GenAI Application?
A Generative AI (GenAI) application uses AI models (LLMs, image, audio models) to:
- Generate new content
- Automate tasks
- Enable intelligent interactions

GenAI apps can range from:
- Simple model prompts
- To complex AI agent systems

---

## 2. Types of GenAI Applications
Common forms include:
- Chat applications (e.g., assistants, chatbots)
- API endpoints (model serving / agents)
- SQL-based AI functions for analysts

---

## 3. Core Components of GenAI Systems

### a. Models (LLMs & Foundation Models)
- Trained on large datasets (text, image, audio)
- Perform reasoning, generation, and prediction
- Examples: chatbots, code generation, summarization

### b. Agents
AI systems that:
1. Receive input
2. Plan and reason
3. Use tools or data
4. Execute actions
5. Return results

👉 Difference:
- Model = generates output
- Agent = thinks, acts, and orchestrates tasks

---

### c. Tools
External capabilities used by agents:
- Data retrieval (vector search, SQL, APIs)
- Actions (send email, call APIs)
- Execution (run code, ML models)

👉 Key idea:
- Tools = single task
- Agents = multi-step reasoning systems

---

## 4. Prompt Engineering
- Designing inputs to guide model behavior
- Can include:
  - Instructions
  - Context
  - Examples
- Can be optimized manually or via ML techniques

---

## 5. GenAI Evaluation Challenges
GenAI outputs are:
- Open-ended
- Non-deterministic
- Hard to measure

Evaluation requires:
- Automated evaluation (AI judging AI)
- Human feedback
- Observability & tracing (e.g., MLflow)

---

## 6. General Intelligence vs Data Intelligence

| Type | Description |
|------|------------|
| General Intelligence | Knowledge from pretraining (LLMs) |
| Data Intelligence | Organization-specific data |

👉 Best systems combine both:
- LLM + enterprise data = powerful applications

---

## 7. GenAI Platform (Databricks View)

A complete platform includes:

### AI Assets
- Models
- Agents
- Applications

### Data Assets
- Tables, files
- Vector databases
- Feature stores

### Deployment
- Model endpoints
- Agent serving

### Governance
- Security & access control
- Monitoring
- Compliance

---

## 8. Agents Design Spectrum
GenAI systems evolve from:
- Simple prompt-based apps
→ Tool-augmented workflows
→ Multi-agent systems

---

## 9. Relationship with ML & Deep Learning
- GenAI ⊂ AI ecosystem
- Built on deep learning
- Shares infrastructure with ML:
  - Training
  - Deployment
  - Monitoring

---

## 10. Key Takeaways
- GenAI apps combine **models + agents + tools + data**
- Agents bring **reasoning + action capabilities**
- Enterprise value comes from **data intelligence**
- Evaluation and governance are critical for production systems
