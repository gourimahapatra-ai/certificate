# Snowflake Data Lineage — SnowPro Core SC0‑03 Study Notes

## 1. What Is Data Lineage?
Data lineage in Snowflake refers to the **ability to trace how data moves, transforms, and is consumed** across Snowflake objects.  
It shows **where data came from (upstream)** and **where it flows next (downstream)**.

Lineage helps with:
- Impact analysis  
- Auditing and compliance  
- Debugging ETL pipelines  
- Understanding dependencies between objects  

---

## 2. Where Lineage Comes From in Snowflake
Snowflake automatically captures lineage from:

### **2.1 Query History**
Every query executed in Snowflake is logged with:
- Source objects (tables, views, streams)
- Target objects (tables, dynamic tables, materialized views)
- SQL text  
- Timestamps  
- User and role information  

This metadata is available in:
- `ACCOUNT_USAGE.QUERY_HISTORY`
- `INFORMATION_SCHEMA.QUERY_HISTORY`

---

## 3. Lineage in Snowsight (UI)
Snowsight provides **visual lineage graphs** for supported objects.

### You can view lineage for:
- Tables  
- Views  
- Dynamic Tables  
- Materialized Views  
- Tasks  
- Streams  

### What the lineage graph shows:
- **Upstream dependencies** (what feeds this object)
- **Downstream dependencies** (what this object feeds)
- Object types (table, view, dynamic table, task)
- Refresh or execution history (for dynamic tables & tasks)

This is heavily tested in SnowPro Core.

---

## 4. Lineage for Dynamic Tables
Dynamic Tables have **built‑in lineage tracking**.

Snowflake exposes:
- `DYNAMIC_TABLE_GRAPH` — dependency graph  
- `DYNAMIC_TABLE_REFRESH_HISTORY` — refresh lineage  

Dynamic Tables automatically track:
- Which upstream tables changed  
- How incremental refreshes propagate  
- Which downstream objects depend on them  

---

## 5. Lineage for Tasks
Tasks show lineage through:
- Directed acyclic graph (DAG) of task dependencies  
- Execution history  
- Upstream/downstream task relationships  

Tasks + Dynamic Tables often appear together in exam questions.

---

## 6. Lineage for Streams
Streams track **change data capture (CDC)** and contribute to lineage by showing:
- Which table they monitor  
- Which downstream tasks or dynamic tables consume the stream  

---

## 7. How Snowflake Stores Lineage Metadata
Lineage metadata is stored in:
- `ACCOUNT_USAGE` views  
- `INFORMATION_SCHEMA` views  
- Snowsight lineage graph  

Snowflake does **not** store full historical lineage forever.  
Retention depends on:
- Query history retention (typically 365 days for Enterprise+)
- Object type  
- Account edition  

---

## 8. What Lineage Does *Not* Do
Important for the exam:

- ❌ Does NOT track lineage outside Snowflake (e.g., external ETL tools)  
- ❌ Does NOT show row‑level lineage  
- ❌ Does NOT show lineage for temporary or transient objects beyond query history  
- ❌ Does NOT track lineage for dropped objects once metadata expires  

---

## 9. Common SnowPro Exam Questions About Lineage

### **Q: Where do you view lineage in Snowflake?**  
- Snowsight UI lineage graph  
- Query history views  

### **Q: Does Snowflake automatically capture lineage?**  
- Yes, for all queries and supported objects.

### **Q: Does lineage show upstream and downstream dependencies?**  
- Yes, both directions.

### **Q: Does lineage work for Dynamic Tables?**  
- Yes, with dedicated lineage views.

### **Q: Does lineage track external pipelines?**  
- No.

---

## 10. Summary (Exam‑Ready)
- Snowflake automatically captures lineage from query execution.  
- Snowsight provides visual lineage for tables, views, dynamic tables, tasks, and streams.  
- Lineage helps with impact analysis, debugging, and compliance.  
- Dynamic Tables have dedicated lineage metadata.  
- Lineage does not track external systems or row‑level transformations.

