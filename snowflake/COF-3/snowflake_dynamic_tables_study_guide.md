# Snowflake Dynamic Tables — SnowPro Core SC0-03 Study Guide

---

## 1. What Are Dynamic Tables?

Dynamic Tables in Snowflake are incrementally updated, declarative data pipelines that automatically maintain table results based on a user-defined query. They behave like materialized views but are designed for ETL/ELT pipelines, ensuring data freshness without manual orchestration.

**Dynamic Tables:**
- Continuously process upstream changes
- Maintain downstream tables automatically
- Use compute resources via a warehouse or serverless compute
- Support incremental refresh using change tracking

---

## 2. Key Concepts

### 2.1 Target Lag

Defines how fresh the data in the Dynamic Table must be.

```sql
TARGET_LAG = '5 minutes'
```

Snowflake ensures the table is updated so that data is no more than 5 minutes stale.

### 2.2 Refresh Mode

Dynamic Tables support two refresh modes:

| Mode | Description |
|------|-------------|
| `AUTO` (default) | Snowflake decides incremental vs. full refresh |
| `FULL` | Recomputes the entire table |

### 2.3 Incremental Refresh

Snowflake automatically identifies changed rows using **change tracking** and processes only deltas.

---

## 3. Creating a Dynamic Table

```sql
CREATE OR REPLACE DYNAMIC TABLE sales_dt
  TARGET_LAG = '5 minutes'
  WAREHOUSE = my_wh
AS
  SELECT * FROM raw_sales;
```

**Key Notes:**
- Must specify `TARGET_LAG`
- Must specify `WAREHOUSE` unless using serverless compute
- Query must be deterministic

---

## 4. Refresh Behavior

Dynamic Tables refresh automatically based on:
- Target lag
- Upstream table changes
- System load

> Snowflake manages refresh scheduling internally.

---

## 5. Monitoring Dynamic Tables

Use the following views:

### 5.1 `DYNAMIC_TABLE_REFRESH_HISTORY`
Shows refresh events, duration, and status.

### 5.2 `DYNAMIC_TABLE_GRAPH`
Shows dependencies between Dynamic Tables.

### 5.3 `LAST_REFRESH_TIME`
Check when the table was last updated.

```sql
SELECT * FROM TABLE(INFORMATION_SCHEMA.DYNAMIC_TABLE_REFRESH_HISTORY());
```

---

## 6. Best Practices

- Use incremental logic for large datasets
- Keep queries deterministic and stable
- Avoid unnecessary joins in upstream tables
- Use appropriate target lag to balance cost and freshness
- Monitor refresh history for performance tuning

---

## 7. Limitations ⚠️ (Exam-Relevant)

| Limitation |
|------------|
| Cannot reference temporary or transient tables |
| Cannot use non-deterministic functions (e.g., `RANDOM()`, `CURRENT_TIMESTAMP()`) |
| Cannot reference external tables directly |
| Cannot include `COPY INTO`, DML, or procedural logic |
| Must use `SELECT`-only queries |

---

## 8. Dynamic Tables vs. Materialized Views

| Feature | Dynamic Tables | Materialized Views |
|---------|---------------|-------------------|
| Incremental refresh | ✅ Yes | ✅ Yes |
| Declarative pipelines | ✅ Yes | ❌ No |
| Target lag | ✅ Yes | ❌ No |
| Supports complex queries | ✅ Yes | ⚠️ Limited |
| Designed for ETL | ✅ Yes | ❌ No |

---

## 9. Example Pipeline

```sql
-- Bronze Layer
CREATE OR REPLACE DYNAMIC TABLE bronze_dt
  TARGET_LAG = '10 minutes'
AS
  SELECT * FROM raw_data;

-- Silver Layer
CREATE OR REPLACE DYNAMIC TABLE silver_dt
  TARGET_LAG = '5 minutes'
AS
  SELECT * FROM bronze_dt WHERE is_valid = TRUE;

-- Gold Layer
CREATE OR REPLACE DYNAMIC TABLE gold_dt
  TARGET_LAG = '1 minute'
AS
  SELECT customer_id, SUM(amount) AS total
  FROM silver_dt
  GROUP BY customer_id;
```

---

## 10. Exam Tips 🎯

- Know the purpose of `TARGET_LAG`
- Understand incremental vs. full refresh
- Remember Dynamic Tables are **SELECT-only**
- Know monitoring views (`DYNAMIC_TABLE_REFRESH_HISTORY`)
- Understand differences from Materialized Views
- Know that Snowflake handles orchestration automatically

---

## 11. Summary

Dynamic Tables are Snowflake's modern, declarative, incremental ETL framework. They simplify pipeline management, ensure data freshness, and reduce operational overhead — making them a key topic in the **SnowPro Core SC0-03** exam.

---

*Study Guide — Snowflake SnowPro Core SC0-03*
