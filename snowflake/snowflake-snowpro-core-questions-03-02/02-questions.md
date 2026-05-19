# Snowflake OAuth with External Identity Providers

To successfully configure and use Snowflake OAuth with an external identity provider such as :contentReference[oaicite:0]{index=0} or :contentReference[oaicite:1]{index=1}:

- A client application must be registered in the external Identity Provider (IdP).
- A secure OAuth token endpoint must be configured in Snowflake.
- This setup establishes a trusted authentication relationship between Snowflake and the external IdP.


# Loading Data from Azure Blob Storage into Snowflake

## Recommended Workflow

When loading data from an external cloud location such as Azure Blob Storage into :contentReference[oaicite:0]{index=0}, the best-practice approach follows these steps:

---

## Step 1: Prerequisites

### Create a Storage Integration
A Storage Integration securely manages authentication and access to the Azure container without storing credentials directly in SQL.

### Create a File Format Object
A File Format Object defines how incoming files should be parsed (e.g., JSON, CSV, Parquet).

Example:
```sql
CREATE FILE FORMAT my_json_format
TYPE = JSON;
```
## Step 2: Create an External Stage

An External Stage in :contentReference[oaicite:0]{index=0} connects:

- Azure Blob Storage location
- Storage Integration
- File Format Object

This allows Snowflake to securely access and correctly parse files stored in Azure Blob Storage.

### Example

```sql id="a1f3d9"
CREATE OR REPLACE STAGE my_azure_stage
  URL = 'azure://myaccount.blob.core.windows.net/mycontainer/path/'
  STORAGE_INTEGRATION = my_azure_integration
  FILE_FORMAT = my_json_format;

```
## Components Explained

| Component | Purpose |
|---|---|
| `URL` | Specifies the Azure Blob Storage container and folder path where the data files are stored |
| `STORAGE_INTEGRATION` | Securely manages authentication and access between :contentReference[oaicite:0]{index=0} and Azure without exposing credentials in SQL |
| `FILE_FORMAT` | Defines how Snowflake should read and parse the files (such as JSON, CSV, or Parquet) |


### Load 
```sql
COPY INTO my_table
FROM @my_azure_stage;
```

# Snowflake Clustering Key Anti-Pattern

This scenario demonstrates a common clustering key mistake in :contentReference[oaicite:0]{index=0}:  
using a very high-cardinality column such as a UUID (`ORDER_ID`) as the clustering key.

---

# Why UUIDs Are Poor Clustering Keys

UUIDs are:

- Random
- Unique
- Extremely high cardinality

Example:
- 5 billion rows
- 5 billion unique ORDER_ID values

When a UUID is used as the clustering key:

- Micro-partitions contain randomly distributed ORDER_ID values
- Partition min/max ranges overlap heavily
- Reclustering provides little optimization benefit
- Queries filtering by date cannot prune partitions efficiently

As a result, query performance remains poor even after automatic clustering runs.

---

# Root Cause

The table is clustered on a column that does not match the query access pattern.

If queries mostly filter using:

```sql 
WHERE order_date BETWEEN ...
```
then clustering should be based on ORDER_DATE, not ORDER_ID.

- Cluster using columns that align with query filters.
```sql
ALTER TABLE orders CLUSTER BY (order_date);
ALTER TABLE orders CLUSTER BY (order_date, region);
```

### Why This Improves Performance

- Clustering by ORDER_DATE:
- Groups similar dates together in
micro-partitions
- Reduces partition overlap
- Improves partition pruning
- Speeds up date-range queries significantly

# Snowflake Zero-Copy Clone Privileges

In :contentReference[oaicite:0]{index=0}, when creating a zero-copy clone of a database:

## What Gets Cloned

- Database structure (schemas, tables, views, etc.)
- Data using shared micro-partitions
- Privileges on child objects such as:
  - Schemas
  - Tables
  - Views

---

## What Does NOT Get Cloned

- Privileges granted on the database itself
- Database-level grants must be re-applied manually

The cloned database is owned by the role that performs the clone operation.

---

# Example

```sql id="d4n8p1"
-- Original database grants
GRANT USAGE ON DATABASE prod_db TO ROLE analyst;
GRANT USAGE ON SCHEMA prod_db.public TO ROLE analyst;

-- Create clone
CREATE DATABASE dev_db CLONE prod_db;
```

## Result

| Privilege | Cloned? |
|---|---|
| `USAGE` on database (`dev_db`) | ❌ No |
| `USAGE` on schema (`dev_db.public`) | ✅ Yes |

---

# Key Exam Takeaway

The statement:

> "Privileges on the database itself and all child objects are automatically inherited"

is FALSE because:

- Database-level privileges are NOT cloned
- Only child object privileges are preserved

Administrators must manually grant database-level privileges on the cloned database.

# Snowflake UNDROP Command

The `UNDROP` command is part of the Time Travel feature used to restore dropped objects.

---

# Example

```sql id="u1p4d7"
-- Drop a table
DROP TABLE my_table;

-- Restore the table
UNDROP TABLE my_table;

UNDROP SCHEMA my_schema;

UNDROP DATABASE my_database;

```

### Key Points
The object must still be within the Time Travel retention period
UNDROP restores the object with all its data
If another object with the same name exists, it must be renamed or dropped first
Works for:
- Tables
- Schemas
- Databases