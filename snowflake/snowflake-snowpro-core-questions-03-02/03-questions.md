# Snowflake UDF Types — Summary

Snowflake supports two main types of User-Defined Functions (UDFs):

---

## 1. Scalar UDF

A **Scalar UDF** returns:

- **One value**
- **One row**
- **One column**
- For each input row

### Common Uses
- Calculations
- String manipulation
- Type conversions

### Example

```sql
-- Returns ONE value per input
SELECT add_two(5);  
-- Output: 7
```

## 2. Tabular UDF (UDTF)

A **Tabular UDF** (User‑Defined Table Function) returns:

- Multiple rows  
- Multiple columns  
- Table‑shaped output  

The return type is defined using:

```sql
RETURNS TABLE (...)

CREATE FUNCTION get_customer_orders(cust_id INT)
RETURNS TABLE(order_id INT, amount FLOAT, order_date DATE)
LANGUAGE SQL
AS $$
    SELECT order_id, amount, order_date
    FROM orders
    WHERE customer_id = cust_id
$$;

-- Usage
SELECT * FROM TABLE(get_customer_orders(12345));

```
## Key Point

A single customer ID can return **many order rows**.  
This multi‑row, table‑shaped output is what makes it a **Tabular UDF (UDTF)**.

---

## Why Other Options Are Incorrect

### Scalar UDF ❌
- Returns only **one value** per input row  
- Cannot return multiple rows or columns  

### External Function ❌
- Refers to **where code executes** (outside Snowflake)  
- Not related to the **shape** of the output  

### Stored Procedure ❌
- Invoked using `CALL`  
- Used for database operations like:  
  - INSERT  
  - UPDATE  
  - DELETE  
- Not typically used inline in `SELECT` statements  

---

## Exam Tip

| Function Type            | Returns          | Usage                         |
|--------------------------|------------------|-------------------------------|
| Scalar UDF               | Single value     | Calculations & transformations |
| Tabular UDF (UDTF)       | Table result     | Multiple rows/columns          |
| Stored Procedure         | Procedural ops   | Database actions               |
| External Function        | API execution    | External integrations          |

---

## References

- Snowflake Documentation — Tabular UDFs (UDTFs)  
- Snowflake Documentation — CREATE FUNCTION


# Snowflake Default File Format — Summary

When no file format is specified in either:

- the `COPY INTO` command, or
- the stage definition,

Snowflake automatically uses **CSV** as the default file format.

---

# Default CSV Settings

| Setting | Default Value |
|---|---|
| TYPE | CSV |
| FIELD_DELIMITER | `,` (comma) |
| RECORD_DELIMITER | `\n` (newline) |
| SKIP_HEADER | `0` |
| FIELD_OPTIONALLY_ENCLOSED_BY | None |
| COMPRESSION | AUTO |
| ESCAPE | None |
| NULL_IF | `\\N` |

---

# Example

## Implicit Default (CSV)

```sql id="r2j7k1"
COPY INTO my_table
FROM @my_stage;

COPY INTO my_table
FROM @my_stage
FILE_FORMAT = (TYPE = CSV);
```
## Important Note

If you upload files such as:

- JSON  
- PARQUET  
- AVRO  

and do **not** explicitly define the file format, Snowflake will still try to read them as **CSV**.

This usually causes:

- Parsing errors  
- Incorrect data loading  
- Corrupted output  

**Always specify the correct file format for non‑CSV files.**

---

## Why Other Options Are Incorrect

### JSON ❌
Supported by Snowflake, but **not** the default format.

### PARQUET ❌
Supported columnar format, but **not** default.

### AVRO ❌
Supported semi‑structured format, but **not** default.

---

## Exam Tip

| Scenario                     | Result              |
|------------------------------|---------------------|
| No file format specified     | Defaults to CSV     |
| Non‑CSV files without format | Likely fails        |
| Best Practice                | Define `FILE_FORMAT` explicitly |


# Snowflake COPY INTO — FORCE = TRUE Summary

By default, Snowflake tracks successfully loaded files using **load history metadata**.

- Metadata retention period: **64 days**
- If the same file is loaded again, Snowflake skips it automatically to avoid duplicates.

---

# FORCE = TRUE

Using `FORCE = TRUE` overrides the load history check.

## Example

```sql id="n5v8zx"
COPY INTO my_table
FROM @my_stage
FORCE = TRUE;
```
## What `FORCE = TRUE` Does

- Bypasses load‑history validation  
- Reloads files **even if already loaded**  
- Works with:  
  - Internal stages  
  - External stages  
- Applies to **COPY INTO**  
- Can create **duplicate data** if files are reloaded unintentionally  

---

## Common Use Cases

### Reload After Table Truncation
If data was deleted or the table was truncated, files can be loaded again.

### Reload Into a Cloned Table
Cloned tables **do not inherit** load‑history metadata.

### Reprocess Corrected Files
Useful after:

- Schema changes  
- Data fixes  
- Parsing corrections  

---

## Why Other Statements Are Incorrect

### “FORCE only works with Snowpipe” ❌  
False — `FORCE` is a parameter of **COPY INTO**, not Snowpipe.

### “FORCE works only for internal stages” ❌  
False — it works for **internal and external stages** equally.

### “FORCE still respects the 14‑day metadata cache” ❌  
False — `FORCE = TRUE` **completely bypasses** metadata checks.

Additional notes:

- COPY INTO load‑history retention = **64 days**  
- Snowpipe metadata retention = **14 days**  
- These are **different** concepts  

---

## Exam Tip

| Feature            | Details                              |
|--------------------|---------------------------------------|
| Default behavior   | Previously loaded files are skipped   |
| Metadata retention | 64 days                               |
| FORCE = TRUE       | Reloads files regardless of history   |
| Risk               | Duplicate data                        |
| Works with         | Internal + External stages            |

---

## Reference

Snowflake Documentation — COPY INTO (FORCE option)


## Snowflake Metadata Sources

Snowflake provides **two primary metadata sources**, and understanding the differences is critical for the SnowPro exam.

---

## INFORMATION_SCHEMA (Database-Level)

- Provides **real-time or near–real-time** metadata  
- Scoped to the **current database only**  
- **Cannot** query metadata across databases  
- Shorter retention (some views: **14 days**, some: none)  
- Accessed via:  
  ```
  <database>.INFORMATION_SCHEMA.<view_name>
  ```

---

## ACCOUNT_USAGE (Account-Level, in `SNOWFLAKE` Database)

- Provides metadata for the **entire account**  
- Has **latency**: ~45 minutes to **3 hours**  
- Long retention: **up to 365 days**  
- Accessed via:  
  ```
  SNOWFLAKE.ACCOUNT_USAGE.<view_name>
  ```
- Requires:  
  ```
  GRANT IMPORTED PRIVILEGES ON DATABASE SNOWFLAKE TO ROLE <role>;
  ```

---

## Quick Comparison (Prose)

- **Information Schema** → real-time, database-scoped, short retention  
- **Account Usage** → account-wide, long retention, delayed by 45–180 minutes  

---

## Why the Other Options Are Incorrect

### “The Account Usage schema provides real-time data” ❌  
Incorrect — **Account Usage has latency**, not Information Schema.

### “Both schemas provide real-time data” ❌  
Incorrect — **only Information Schema** is real-time.

### “Account Usage is only for enterprise accounts” ❌  
Incorrect — available to **all Snowflake editions**, but requires privileges on the shared `SNOWFLAKE` database.

---

## Reference Documentation

- Snowflake Documentation — Account Usage  
- Snowflake Documentation — Information Schema  
- Snowflake Documentation — Differences Between Account Usage and Information Schema

## Overall Explanation

**Row Access Policies** provide **row‑level security** in Snowflake by controlling which rows are visible to which users or roles.  
The policy evaluates a condition **for every row at query runtime** and returns only the rows where the condition is **TRUE**.

---

## Implementation Workflow

### **Step 1 — Create the Row Access Policy**

```sql
CREATE ROW ACCESS POLICY region_access AS (region_val VARCHAR)
  RETURNS BOOLEAN ->
  CASE
    WHEN CURRENT_ROLE() = 'GLOBAL_ADMIN' THEN TRUE
    WHEN CURRENT_ROLE() = 'EUROPE_ANALYST' AND region_val = 'EUROPE' THEN TRUE
    ELSE FALSE
  END;
```

- `region_val` is the **signature column** — the column the policy will be applied to.  
- The policy returns a **BOOLEAN**:  
  - `TRUE` → row is visible  
  - `FALSE` → row is filtered out  

---

### **Step 2 — Apply the Policy to the Table Column**

```sql
ALTER TABLE sales ADD ROW ACCESS POLICY region_access ON (region);
```

- The signature column (`region_val`) now maps to the actual **REGION** column.  
- `EUROPE_ANALYST` → sees only rows where `REGION = 'EUROPE'`  
- `GLOBAL_ADMIN` → sees **all rows**  
- Any other role → sees **no rows**

---

## Key Exam Points

- Available starting from **Enterprise Edition**  
- They are **schema‑level securable objects**  
- Signature columns must map to actual table columns  
- Any referenced column must be declared as a signature column  
- Policies evaluate **at query runtime** — stored data is unchanged  
- Can use:  
  - `CURRENT_ROLE()`  
  - `CURRENT_USER()`  
  - `IS_ROLE_IN_SESSION()`  

---

## Why the Other Options Are Incorrect

### **Dynamic Data Masking ❌**
- Works at the **column level**  
- Masks or reveals values  
- **Cannot filter rows** → not suitable for row‑level security

### **Network Policies ❌**
- Restrict access based on **IP address**  
- Do not filter data based on roles or content  
- Cannot enforce row‑level filtering

### **Secure Views ❌**
- Can filter rows, but require separate view objects  
- Row access policies apply directly to the **base table**  
- Enforcement works across:  
  - Direct queries  
  - Joins  
  - Views  
  - Any access path  
- Secure views exist in Standard Edition but are less robust for this use case

---

## Reference Documentation

- Snowflake Documentation — Row Access Policies  
- Snowflake Documentation — Dynamic Data Masking  
- Snowflake Documentation — Security Features Overview

## Shared Nothing Architecture — Explanation

The described system has **independent nodes**, each with its own CPU, memory, and local disk, with data distributed across nodes.  
This is the classic definition of a **Shared Nothing** architecture.

---

## Shared Nothing Architecture

- Each node has its **own compute + own storage**  
- Data is **partitioned and distributed** across nodes  
- Nodes communicate over the network for cross‑node operations  
- Common examples: **Hadoop, Teradata, Netezza, Amazon Redshift (original)**  

### Primary Disadvantage — Data Management Complexity

- **Data redistribution** when scaling is expensive  
- **Data skew** causes performance imbalance  
- Scaling requires **data movement**  
- Cross‑node joins require **network shuffling**  
- Node failures can cause **data unavailability** unless replicated  

---

## Contrast With Shared Disk

- All nodes share **one central storage**  
- Storage becomes a **bottleneck**  
- No data redistribution needed when scaling compute  

---

## Contrast With Snowflake (Multi‑Cluster Shared Data)

- Central storage (like shared disk)  
- Independent compute clusters (like shared nothing)  
- **No data redistribution** when scaling  
- No storage bottleneck because compute and storage are **decoupled**  

---

## Why the Other Options Are Incorrect

### “Shared Nothing — single point of failure in central storage” ❌  
Incorrect — shared nothing has **no central storage**.  
Single point of failure is a **shared disk** issue.

### “Shared Disk — increased complexity due to data redistribution” ❌  
Incorrect — shared disk **does not** require redistribution.  
Redistribution is a **shared nothing** problem.

### “Shared Disk — limited scalability due to network bottlenecks” ❌  
Incorrect — the described architecture uses **local disks**, which is shared nothing, not shared disk.

---

## Reference Documentation

- Snowflake Documentation — Architecture Overview

## Dynamic Data Masking — Explanation

**Dynamic Data Masking** is the Snowflake feature designed specifically to protect sensitive data **at query time** based on the querying user's role — **without altering the stored data**.

---

## Example Implementation

### **Create a Masking Policy**

```sql
CREATE MASKING POLICY email_mask AS (val STRING)
  RETURNS STRING ->
  CASE
    WHEN CURRENT_ROLE() IN ('HR_ADMIN') THEN val
    ELSE '***MASKED***'
  END;
```

### **Apply the Policy to a Column**

```sql
ALTER TABLE employees 
  MODIFY COLUMN email 
  SET MASKING POLICY email_mask;
```

---

## How It Works

- The masking policy is evaluated **dynamically at query time**  
- The stored data remains **unchanged**  
- `HR_ADMIN` sees the **real email**  
- All other roles see: `***MASKED***`

---

## Key Characteristics

- Available in **Enterprise Edition and above**  
- Applied at the **column level**  
- Multiple columns can share the same policy  
- Supports context functions such as:  
  - `CURRENT_ROLE()`  
  - `IS_ROLE_IN_SESSION()`  
  - `CURRENT_USER()`  

---

## Why the Other Options Are Incorrect

### **External Tokenization ❌**
- Replaces values **before loading**  
- Alters stored data → violates the requirement: *“without altering the stored data”*

### **Row Access Policies ❌**
- Filter **entire rows**, not individual column values  
- Requirement is to **mask a specific column**, not hide rows

### **Secure Views ❌**
- Can hide or mask columns, but require maintaining separate view objects  
- Dynamic masking applies **directly to the base table** and is more flexible

---

## Reference Documentation

- Snowflake Documentation — Dynamic Data Masking  
- Snowflake Documentation — CREATE MASKING POLICY

## Directory Tables — Explanation

A **Directory Table** in Snowflake is a **built‑in, read‑only catalog** of files stored inside a stage.  
It provides metadata such as:

- File name  
- File size  
- Last modified timestamp  
- File checksum  
- Relative path  

This allows you to query staged files **without manually running `LIST`**.

---

## Enabling a Directory Table on an Existing Stage

```sql
ALTER STAGE my_stage SET DIRECTORY = (ENABLE = TRUE);
```

After enabling, query it using:

```sql
SELECT * FROM DIRECTORY(@my_stage);
```

To populate or refresh metadata:

```sql
ALTER STAGE my_stage REFRESH;
```

---

## Enabling Directory Table During Stage Creation (For New Stages)

```sql
CREATE STAGE my_stage
  DIRECTORY = (ENABLE = TRUE);
```

However, the question specifically asks about an **existing** stage, so  
`ALTER STAGE ... SET DIRECTORY = (ENABLE = TRUE)` is the correct answer.

---

## Why the Other Options Are Incorrect

### **“ENABLE DIRECTORY command” ❌**
No such command exists in Snowflake.

### **“CREATE DIRECTORY command” ❌**
Directory tables are **not standalone objects**.  
They are **properties of stages**, not separate entities.

### **“Set directory parameter during stage creation” ❌**
Valid only for **new** stages.  
The question asks about an **existing** stage.

---

## Reference Documentation

- Snowflake Documentation — Directory Tables  
- Snowflake Documentation — ALTER STAGE
