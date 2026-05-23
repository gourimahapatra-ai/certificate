# Databricks Professional Data Engineer – Combined Notes

---

# Bronze Layer Ingestion Patterns

## Singleplex Ingestion
- One‑to‑one mapping between dataset/topic and bronze table.
- Each dataset/topic is ingested into its own bronze table.
- Known as **singleplex mapping**.
- Practical note: Workspaces may limit maximum concurrent jobs.

## Multiplex Ingestion
- Many‑to‑one mapping.
- Multiple topics → single dataset → bronze table.
- After bronze, data is separated into silver layer.

---

# Slowly Changing Dimensions (SCD)

SCD defines how dimensional tables handle changes over time.

## SCD Types
- **Type 0**: No changes allowed. Static or append‑only tables.
- **Type 1**: Overwrite existing values. No history retained.
- **Type 2**: Add a new row for each change; old row marked obsolete. Full history retained.

---

# Change Data Capture (CDC)

CDC identifies changes (insert/update/delete) in source systems and delivers them downstream.

## Types of Row-Level Changes
1. Inserts (new records)
2. Updates (modify existing records)
3. Deletes (remove existing records)

---

# MERGE Operation Limitations
1. MERGE fails if multiple source rows attempt to modify the same target row.
2. CDC feed with multiple updates for the same key in the same batch causes exceptions.

---

# Delta Lake Change Data Feed (CDF)

- Automatically generates CDC feeds for Delta tables.
- Captures row-level changes + metadata (insert/update/delete).
- Used in multi-hop architecture to propagate changes.

## Preimage
State of row before update.

## Postimage
State of row after update.

## Inserts/Deletes
Recorded in same CDF format.

---

# Enabling CDF

## New Table

```sql
TBLPROPERTIES (delta.enableChangeDataFeed = true)

--- Existing Table
ALTER TABLE mytable SET TBLPROPERTIES (delta.enableChangeDataFeed = true)

```


---

# When to Use CDF
- Table includes updates and/or deletes.
- Only a small fraction of rows change per batch.
- Useful for stream-static joins.

---

# Stream-Static Joins
- Streaming tables: ever-appending.
- Static tables: may be overwritten → break streaming requirements.

---

# Partitioning
- Partition = subset of rows sharing same partition column value.
- Creates subfolders in storage.
- Helps optimizer prune data during queries.

---

# Delta Lake Transaction Log

## Commit Files
- Each commit is a JSON file (e.g., 000000.json, 000001.json).

## Checkpoints
- Parquet checkpoint files created every 10 commits.
- Speeds up table state reconstruction.

## Delta Lake File Statistics
Stored for each added file:
- Total number of records
- Stats for first 32 columns:
  - min value
  - max value
  - null count

---

# VACUUM
- Does NOT delete Delta log files.
- Log files cleaned automatically by Databricks.

---

# Time Travel
- Default retention: **30 days**.

---

# Auto Optimize

Automatically compacts small files during writes.

## Features
1. **Optimized Writes** → target ~128 MB files.
2. **Auto Compaction** → merges small files after write.

If compaction is needed, Databricks runs an OPTIMIZE-like job automatically.

---

# REST API
- Databricks provides APIs to create, run, and manage jobs.

---

# Data Pipeline Testing

## Unit Testing
- Tests individual units (functions).
- Ensures code still works after changes.
- Uses assertions: `assert func() == expected_value`.

## Integration Testing
- Tests interaction between modules.

## End-to-End Testing
- Ensures entire application works in real-world scenarios.
- Simulates full user workflow.

---

# Databricks Professional Data Engineer Certification

## Exam Details
- Duration: 120 minutes
- Questions: 60
- Passing Score: 70% (42/60)
- Fee: $200

## Question Distribution
- Data Processing: 18
- Data Modeling: 12
- Databricks Tooling: 12
- Security & Governance: 6
- Testing & Deployment: 6
- Monitoring & Logging: 6

## Out of Scope Topics
- Delta Live Tables (DLT)
- Scala
- Airflow / ADF
- Kafka
- Jenkins / Azure DevOps
- Managed CI/CD
- Gitflow
- Terraform

---

# Code Notes
- Code examples mainly in Python.
- Delta Lake functionality in SQL.

## Question Types
1. Conceptual Questions
2. Code-Based Questions

---

# Crash Notes (Part 1)

1. Minimum permission to view metrics & Spark UI: **Can Attach To**.
2. For production jobs: use **Job Clusters**.
3. Job clusters provide isolated environments.
4. Minimum permission to start/terminate job: **Can Restart**.
5. Dropping external table deletes metadata only; data files remain.
6. Minimum permission to edit cluster: **Can Manage**.
7. Printing secrets → REDACTED.
8. `%sh` magic command runs on driver → performance overhead.
9. Delta file statistics help the query optimizer.

---

# Crash Notes (Part 2)

## Shallow Clone
- Does not copy data.
- References Delta transaction log.
- Running VACUUM on source may break shallow clone (files missing).

## Deep Clone Syntax


```sql

CREATE OR REPLACE TABLE orders_archive DEEP CLONE orders;


## Time Travel Query

SELECT * FROM table VERSION AS OF 36;
```


## Streaming from Bronze → Silver
- If data is continuously appended, use structured streaming in batch mode.
- Use **availableNow** trigger for batch-like streaming.

## Auto Optimize
- Optimized writes + auto compaction reduce future MERGE duration.

## Job Run History
- Databricks maintains job run history for **60 days**.

---
