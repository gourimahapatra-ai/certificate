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


## Storage Integrations — Explanation

When connecting Snowflake to **private cloud storage** (AWS S3, Azure Blob, GCS), the secure and recommended method is to use a **Storage Integration**.

A **Storage Integration** is a Snowflake **account‑level object** that:

- Encapsulates authentication (IAM role, service principal, service account)  
- Prevents embedding sensitive credentials in stage definitions  
- Can be **reused across multiple stages**  
- Must be created by `ACCOUNTADMIN` or a role with `CREATE INTEGRATION`  

---

## Example: Creating and Reusing a Storage Integration

```sql
CREATE STORAGE INTEGRATION my_s3_integration
  TYPE = EXTERNAL_STAGE
  STORAGE_PROVIDER = 'S3'
  STORAGE_AWS_ROLE_ARN = 'arn:aws:iam::123456789012:role/my-snowflake-role'
  ENABLED = TRUE
  STORAGE_ALLOWED_LOCATIONS = ('s3://my-bucket/path/');
```

### Reuse the integration across multiple stages:

```sql
CREATE STAGE stage_a 
  URL = 's3://my-bucket/path/a/'
  STORAGE_INTEGRATION = my_s3_integration;

CREATE STAGE stage_b 
  URL = 's3://my-bucket/path/b/'
  STORAGE_INTEGRATION = my_s3_integration;
```

---

## Why the Other Options Are Incorrect

### **“Store credentials in a file format object” ❌**
- File formats define **parsing rules** (CSV delimiters, encoding, compression).  
- They **do not** store credentials.  
- Conceptually incorrect.

### **“Grant ACCOUNTADMIN to all users” ❌**
- Severe security violation.  
- `ACCOUNTADMIN` is the **highest‑privilege** role.  
- Access should be controlled via **RBAC**, not admin elevation.

### **“Embed AWS access keys directly in the stage” ❌**
- Technically possible using `CREDENTIALS = (...)`, but:  
  - Keys become **visible** in stage metadata  
  - Harder to rotate  
  - Must be duplicated across stages  
  - Less secure than Storage Integrations  

---

## Reference Documentation

- Snowflake Documentation — Storage Integrations  
- Snowflake Documentation — Configuring Secure Access to S3


## External Stages — Best Practices

When configuring **external stages** in Snowflake, the recommended approach is to separate responsibilities into **dedicated, reusable objects** rather than embedding everything directly in the stage definition.

---

## Storage Integration Object

A **Storage Integration** securely encapsulates the credentials required to access external cloud storage (Azure Blob, AWS S3, GCS).

Benefits:

- Credentials are stored **securely and separately**  
- Users with stage access **cannot see** underlying keys  
- Integration can be **reused** across multiple stages  
- Credential rotation is centralized  

### Example

```sql
CREATE STORAGE INTEGRATION my_azure_int
  TYPE = EXTERNAL_STAGE
  STORAGE_PROVIDER = 'AZURE'
  AZURE_TENANT_ID = '...'
  ENABLED = TRUE
  STORAGE_ALLOWED_LOCATIONS = (
    'azure://myaccount.blob.core.windows.net/mycontainer/'
  );
```

---

## Named File Format Object

A **file format object** defines how Snowflake should parse data files (CSV, JSON, PARQUET, etc.).

Benefits:

- Reusable across stages and COPY commands  
- Centralized parsing rules  
- Cleaner stage definitions  

### Example

```sql
CREATE FILE FORMAT my_csv_format
  TYPE = CSV
  FIELD_DELIMITER = ','
  SKIP_HEADER = 1;
```

### Stage referencing both reusable objects

```sql
CREATE STAGE my_azure_stage
  URL = 'azure://myaccount.blob.core.windows.net/mycontainer/'
  STORAGE_INTEGRATION = my_azure_int
  FILE_FORMAT = my_csv_format;
```

---

## Why the Other Options Are Incorrect

### **Network Policy ❌**
- Controls **IP-based access** to Snowflake  
- Does **not** authenticate Snowflake to cloud storage  
- Inline file format options are repetitive and not reusable  

### **API Integration ❌**
- Used for **external functions** and API-based services  
- Not for cloud storage authentication  
- “Table-level file format definitions” do not exist  

### **Security Integration (OAuth) ❌**
- Used for **user authentication** (SSO, OAuth)  
- Not for accessing cloud storage  
- VARIANT column mapping is unrelated to file formats  

---

## Reference Documentation

- Snowflake Documentation — Storage Integrations  
- Snowflake Documentation — CREATE FILE FORMAT  
- Snowflake Documentation — CREATE STAGE (External)


## Snowflake Encryption — Overview

Snowflake applies **end‑to‑end encryption** across all editions, including **Standard**.  
Both **data at rest** and **data in transit** are always encrypted.

---

## Data at Rest — AES‑256

- All stored data (micro‑partitions, metadata, temp files) is encrypted using **AES‑256**  
- Industry‑standard, strong encryption  
- Snowflake manages keys using a **hierarchical key model**  
- Keys are **rotated periodically**  

---

## Data in Transit — TLS 1.2

- All communication between clients and Snowflake uses **TLS 1.2**  
- Internal Snowflake component communication is also encrypted  
- Protects against interception during network transfer  

---

## Tri‑Secret Secure (Business Critical+)

- Available **only** in **Business Critical** and higher editions  
- Combines:  
  - A Snowflake‑managed key  
  - A customer‑managed key (cloud provider KMS)  
- Produces a **composite master key**  
- Customer can revoke access at any time by disabling their key  

---

## Why the Other Options Are Incorrect

### **“Data is encrypted at rest but not in transit in Standard Edition” ❌**
Incorrect — **all editions** encrypt data **at rest and in transit**.  
Encryption is never optional.

### **“Tri‑Secret Secure is available in all editions” ❌**
Incorrect — it requires **Business Critical** or higher.

---

## Reference Documentation

- Snowflake Documentation — End‑to‑End Encryption  
- Snowflake Documentation — Tri‑Secret Secure  
- Snowflake Documentation — Snowflake Editions


## Resource Monitors — Actions and Behavior

Resource monitors in Snowflake control **credit consumption** for warehouses.  
They support **three** possible actions when a threshold is reached.

---

## Notify Only

- Sends an **email notification** to account administrators  
- Warehouse **keeps running**  
- No queries are stopped  

---

## Suspend and Notify (Suspend)

- Sends a notification  
- Allows **currently running queries to finish**  
- Suspends the warehouse **after active queries complete**  
- New queries are **not accepted** once suspension begins  
- This is the **graceful shutdown** option  

---

## Suspend Immediately and Notify (Suspend Immediately)

- Sends a notification  
- **Immediately cancels** all running queries  
- Suspends the warehouse **right away**  
- This is the **hard shutdown** option  

---

## Example Resource Monitor

```sql
CREATE RESOURCE MONITOR my_monitor
  WITH CREDIT_QUOTA = 100
  TRIGGERS
    ON 90 PERCENT DO NOTIFY
    ON 100 PERCENT DO SUSPEND
    ON 110 PERCENT DO SUSPEND_IMMEDIATE;
```

---

## Why the Other Options Are Incorrect

### **“Suspend Immediately and Notify” ❌**
- Cancels running queries **immediately**, not gracefully.

### **“Notify Only” ❌**
- Sends a notification but **does not suspend** the warehouse.

### **“Notify After Usage Limit” ❌**
- Not a valid Snowflake resource monitor action.

---

## Reference Documentation

- Snowflake Documentation — Resource Monitors


## Granting Ability to Create Pipes but NOT Stages

Snowflake uses a **granular, privilege‑based model**.  
To allow a role to **create pipes** but **not create stages**, you simply grant **only** the privileges required — Snowflake does **not** use explicit DENY statements.

---

## Correct Privilege Grants

```sql
GRANT USAGE ON SCHEMA my_db.my_schema TO ROLE pipe_creator;
GRANT CREATE PIPE ON SCHEMA my_db.my_schema TO ROLE pipe_creator;
```

### Why these are required:
- **USAGE on schema** → allows the role to reference objects inside the schema  
- **CREATE PIPE** → allows creation of pipe objects  
- **CREATE STAGE is NOT granted**, so the role cannot create stages  

This satisfies the requirement exactly.

---

## Why the Other Options Are Incorrect

### **“CREATE STAGE and CREATE PIPE” ❌**
- Grants the ability to create stages  
- Violates the requirement to *deny* stage creation  

### **“OWNERSHIP” ❌**
- Gives full control over the schema  
- Allows creation, modification, and deletion of **all** object types  
- Far too permissive  

### **“ALL PRIVILEGES” ❌**
- Includes **CREATE STAGE**, **CREATE PIPE**, and more  
- Directly contradicts the requirement  

---

## Reference Documentation
- Snowflake Documentation — Schema Privileges


## TABLE_STORAGE_METRICS — Key Concepts

The `TABLE_STORAGE_METRICS` view exists in **both** Snowflake metadata schemas, each with different scope, latency, and retention characteristics.

---

## ACCOUNT_USAGE.TABLE_STORAGE_METRICS

- **Scope:** Account‑wide (all databases)  
- **Latency:** ~45 minutes to 3 hours  
- **Retention:** Up to **365 days**  
- **Includes:**  
  - ACTIVE_BYTES  
  - TIME_TRAVEL_BYTES  
  - FAILSAFE_BYTES  
  - RETAINED_FOR_CLONE_BYTES  

Accessed via:

```sql
SELECT * 
FROM SNOWFLAKE.ACCOUNT_USAGE.TABLE_STORAGE_METRICS;
```

---

## INFORMATION_SCHEMA.TABLE_STORAGE_METRICS

- **Scope:** Current database only  
- **Latency:** Real‑time / near real‑time  
- **Retention:** Shorter (varies by view)  

Accessed via:

```sql
SELECT * 
FROM <db>.INFORMATION_SCHEMA.TABLE_STORAGE_METRICS;
```

---

## Important Exam Note

Both metadata schemas **do** include `TABLE_STORAGE_METRICS`.  
This question confirms that **both** provide storage breakdowns, including:

- Active storage  
- Time Travel storage  
- Fail-safe storage  

This corrects the earlier misconception that only ACCOUNT_USAGE contains this view.

---

## Why the Other Options Are Incorrect

### **“Only display storage for databases with Time Travel enabled” ❌**
- These views show storage for **all tables**, regardless of Time Travel settings.

### **“Automatically compress table data” ❌**
- These are **read‑only metadata views**; they do not modify or optimize data.

### **“Provide information only about active table storage” ❌**
- They include **Time Travel** and **Fail-safe** bytes, not just active storage.

---

## Reference Documentation

- Snowflake Documentation — TABLE_STORAGE_METRICS (Account Usage)  
- Snowflake Documentation — TABLE_STORAGE_METRICS (Information Schema)


## VALIDATE — Purpose in Snowflake

The **VALIDATE** function is Snowflake’s built‑in tool for inspecting **load errors** that occurred during a `COPY INTO` operation.  
It is used **after** loading data to identify rejected rows, diagnose parsing issues, and verify data quality.

---

## What VALIDATE Is Used For

- Check load errors after a `COPY INTO`  
- Identify problematic rows or files  
- Debug parsing, formatting, or schema mismatch issues  
- Inspect rejected rows when `ON_ERROR = CONTINUE`  
- Validate data quality during ingestion  

---

## Syntax

```sql
SELECT *
FROM TABLE(
    VALIDATE(
        my_table,
        JOB_ID => '_last'
    )
);
```

---

## What `JOB_ID => '_last'` Means

- Refers to the **most recent** `COPY INTO` job executed on the table  
- Allows quick inspection without manually retrieving job IDs  

---

## Typical Workflow

```sql
COPY INTO my_table
FROM @my_stage
FILE_FORMAT = (TYPE = CSV);

-- Inspect rejected rows
SELECT *
FROM TABLE(
    VALIDATE(
        my_table,
        JOB_ID => '_last'
    )
);
```

---

## Output Includes

- File name  
- Row number  
- Column causing the issue  
- Error message  
- Rejected data payload  

---

## Example Scenario

If a CSV contains:

```
1,John,5000
2,Mike,ABC
```

and the `salary` column expects a **NUMBER**,  
`VALIDATE` will return an error row for `ABC`.

---

## Key Notes

- Works only with **COPY INTO** load history  
- Requires that a load job has been executed  
- Extremely useful when bad rows are skipped but the load continues  

---

## Related Topics

- **[COPY INTO](ca://s?q=Explain_COPY_INTO_in_Snowflake)**  
- **[ON_ERROR behavior](ca://s?q=Explain_ON_ERROR_options_in_Snowflake)**  
- **[Load history](ca://s?q=How_to_view_Snowflake_load_history)**  
- **[File format debugging](ca://s?q=Debug_file_format_issues_in_Snowflake)**  


# Snowflake User Stage Reference (`@~`)

## Correct Answer  
A **user stage** in Snowflake is referenced using:



---

## Stage Reference Symbols

| Stage Type | Symbol | Example |
|------------|--------|---------|
| **[User stage](ca://s?q=Explain_Snowflake_user_stage)** | `@~` | `@~` |
| **[Table stage](ca://s?q=Explain_Snowflake_table_stage)** | `@%table_name` | `@%MY_TABLE` |
| **[Named stage](ca://s?q=Explain_Snowflake_named_stage)** | `@stage_name` | `@my_stage` |

---

## User Stage Examples

### Upload a file
```sql
PUT file://data.csv @~;

LIST @~;

COPY INTO mytable
FROM @~;
```

## What Is a User Stage?

A **user stage** is a private, personal storage area automatically created for every Snowflake user.  
It is commonly used for:

- temporary file storage  
- quick testing  
- ad‑hoc data loading  

---

## Easy Memory Trick

| Symbol | Meaning |
|--------|---------|
| `~` | home / personal area |
| `@~` | user’s personal stage |

This is a very common SnowPro Core exam question.



# `SINGLE` Parameter in Snowflake COPY INTO — Detailed Explanation

## 🎯 What `SINGLE` Does
The **`SINGLE`** parameter in a `COPY INTO <location>` unload operation controls **how many output files Snowflake generates**.

It accepts a **boolean**:

- **`SINGLE = TRUE`** → generate **one single output file**
- **`SINGLE = FALSE`** (default) → generate **multiple files**

---

## 📌 Why It Matters
Snowflake unloads data in parallel.  
By default, it writes **multiple files** for maximum performance.

`SINGLE = TRUE` is used when you *must* produce **one file only**, such as:

- exporting a dataset for a downstream system  
- generating a single CSV for a business user  
- creating a compact export for sharing  

---

## 🔍 Behavior Details

### **`SINGLE = TRUE`**
- Forces Snowflake to write **exactly one file**
- Reduces parallelism → **slower for large datasets**
- Output file name is deterministic (e.g., `data_0_0_0.csv.gz`)
- Useful when downstream systems cannot handle multiple files

**Example:**
```sql
COPY INTO @my_stage/export/data.csv
FROM my_table
FILE_FORMAT = (TYPE = CSV)
SINGLE = TRUE;

```
SINGLE = FALSE (default)
Snowflake writes multiple files in parallel

Much faster for large datasets

File names follow Snowflake’s partitioning pattern

Example:
COPY INTO @my_stage/export/
FROM my_table
FILE_FORMAT = (TYPE = CSV)
SINGLE = FALSE;


When to Use Which?
Scenario	Best Setting
Large dataset unload	SINGLE = FALSE
Need exactly one file	SINGLE = TRUE
Downstream system cannot merge files	SINGLE = TRUE
Maximum performance	SINGLE = FALSE


# 🔍 Pruning in Snowflake

## 🧠 What Is Pruning?

**Pruning** in Snowflake refers to the engine’s ability to **skip reading unnecessary micro-partitions** during query execution.  
Instead of scanning an entire table, Snowflake reads **only the micro-partitions that contain relevant data**.

This dramatically improves:

- query performance  
- cost efficiency  
- scan reduction  

---

## 📦 How Pruning Works

Snowflake stores metadata for every micro-partition, including:

- min/max values for each column  
- number of distinct values  
- null counts  
- bloom filters (for some optimizations)  

When you run a query, Snowflake checks this metadata and **prunes away** partitions that cannot possibly match the filter.

Example:

```sql
SELECT *
FROM sales
WHERE sale_date = '2024-01-01';
```
Snowflake will only scan **micro‑partitions whose `sale_date` range includes `2024‑01‑01`** — this is the core idea behind **partition pruning**.

---

# 🧩 Types of Pruning

## 1. **Partition Pruning**
Snowflake skips entire micro‑partitions based on metadata such as:

- min/max column values  
- distinct counts  
- null counts  

If a partition **cannot** contain matching rows, it is **not scanned**.

---

## 2. **Column Pruning**
Snowflake reads **only the columns referenced** in the query.

Example:

```sql
SELECT customer_id FROM sales;
```
Snowflake does **not** read other columns like `price`, `region`, etc. when performing **column pruning** — it only scans the columns referenced in the query.

---

# 🧩 3. File Pruning (External Tables)

For **external tables** stored in:

- Amazon S3  
- Azure Blob Storage  
- Google Cloud Storage  

Snowflake can **prune entire files** before scanning them.

This pruning is based on:

- **Directory structure** (e.g., `/year=2024/month=01/`)  
- **Hive‑style partitioning**  
- **File metadata**  

Example directory layout that enables pruning:

/sales/year=2024/month=01/day=01/file1.parquet
/sales/year=2024/month=01/day=02/file2.parquet


A query filtering on `WHERE year = 2024 AND month = 01` will scan **only** the matching folders.

---

# ⚡ Why Pruning Matters

| Benefit | Description |
|---------|-------------|
| **Faster queries** | Less data scanned |
| **Lower cost** | Fewer credits consumed |
| **Efficient storage** | Works automatically with micro‑partitions |

---

# 🧠 Best Practices to Improve Pruning

- Use **filterable columns** (dates, IDs) in `WHERE` clauses  
- Avoid wrapping columns in functions (prevents pruning)

  ❌ `DATE(order_date) = '2024-01-01'`  
  ✔️ `order_date = '2024-01-01'`

- Use **clustering** or **Liquid Clustering** for large tables  
- Keep data **sorted** on frequently filtered columns  

---

### DATA_RETENTION_TIME_IN_DAYS can be set to 0 on the account level or object level to effectively disable time travel.

### External tables and internal named stages are never cloned.


### Sharing data

Data providers cannot share data directly across different cloud providers or regions without using replication because Snowflake's Secure Data Sharing relies on metadata pointers to the provider’s data, not on physical data movement. This model works only within the same region and cloud platform, since the consumer must access the same underlying storage layer.

When sharing across different regions or clouds (e.g., AWS to Azure):

The data must first be replicated to the target region or cloud.

This ensures that the data physically exists where the consumer can access it.

Resources


# Secure Views in Snowflake

For typical views, internal optimizations can sometimes indirectly expose underlying data patterns or metadata to users.

Secure views protect sensitive data by disabling certain internal Snowflake optimizations that could otherwise reveal information about the underlying tables.

## Key Points

- Standard views may expose limited metadata through query optimization behavior.
- Secure views provide stronger data protection and privacy.
- Secure views are commonly used for:
  - Data sharing
  - Regulatory compliance
  - Sensitive datasets
  - Multi-tenant environments

## Creating a Secure View

```sql
CREATE SECURE VIEW my_secure_view AS
SELECT id, name
FROM employees;
```

## Important Notes

- Secure views trade some performance optimizations for stronger security.
- The underlying query definition is hidden from unauthorized users.
- Frequently used in Secure Data Sharing scenarios.

## Reference

https://docs.snowflake.com/en/user-guide/views-secure