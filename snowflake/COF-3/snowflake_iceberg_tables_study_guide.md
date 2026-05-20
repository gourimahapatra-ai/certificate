# Apache Iceberg™ Tables — SnowPro Core Study Guide
### Covers COF-C02 & COF-C03 Exam Topics

---

## 1. What Are Apache Iceberg™ Tables?

Apache Iceberg is an **open-source table format** originally developed at Netflix for large-scale analytics. In Snowflake, Iceberg Tables combine the open Iceberg table format with Snowflake's powerful query engine — giving you **data ownership in your own cloud storage** while using Snowflake for compute and governance.

> **Exam focus (COF-C03):** Know *why* Iceberg tables exist and how they differ from native Snowflake tables. Operational mechanics and syntax detail are lower priority.

**Key idea:** You own the data files. Snowflake owns the query engine.

---

## 2. Core Architecture Concepts

### 2.1 External Volume

The **external volume** is a named Snowflake account-level object that connects Snowflake to your cloud object storage (S3, Azure Blob, GCS). All Iceberg table data and metadata are stored in this external volume.

```sql
-- Example: Iceberg table referencing an external volume
CREATE ICEBERG TABLE myIcebergTable
  EXTERNAL_VOLUME = 'icebergMetadataVolume'
  CATALOG = 'icebergCatalogInt'
  METADATA_FILE_PATH = 'path/to/metadata/v1.metadata.json';
```

### 2.2 Iceberg Catalog

An **Iceberg catalog** manages and loads Iceberg tables. It forms the first architectural layer in the Iceberg table spec and must:

- Store the **current metadata pointer** for one or more Iceberg tables
- Map a table name to the location of its current metadata file
- Support **atomic operations** to update the metadata pointer

Snowflake supports two catalog modes:

| Catalog Mode | Description |
|---|---|
| **Snowflake as Catalog** | Snowflake manages the metadata; full platform support |
| **External Catalog** | AWS Glue, Databricks Unity Catalog, Snowflake Open Catalog, or any Iceberg REST catalog |

### 2.3 Catalog Integration

A **catalog integration** is a named, account-level Snowflake object that stores information about how table metadata is organized when you **do not** use Snowflake as the catalog.

```sql
-- Example: Catalog integration for an Iceberg REST catalog
CREATE CATALOG INTEGRATION my_cat_int
  CATALOG_SOURCE = POLARIS
  TABLE_FORMAT = ICEBERG
  REST_CONFIG = (
    CATALOG_URI = 'https://<org>-<account>.snowflakecomputing.com/polaris/api/catalog'
    CATALOG_NAME = '<open_catalog_name>'
  )
  REST_AUTHENTICATION = (
    TYPE = OAUTH
    OAUTH_CLIENT_ID = '<client_id>'
    OAUTH_CLIENT_SECRET = '<client_secret>'
    OAUTH_ALLOWED_SCOPES = ('PRINCIPAL_ROLE:ALL')
  )
  ENABLED = TRUE;
```

### 2.4 Snapshot-Based Querying

Iceberg uses a **snapshot-based querying model**:

- Data files are mapped using **manifest files** and **metadata files**
- A **snapshot** represents the state of a table at a point in time
- Snapshots are used to access the complete set of data files in a table

---

## 3. Table Management Modes

### 3.1 Snowflake-Managed Iceberg Tables

Snowflake acts as the catalog. Provides **full Snowflake platform support** including:
- DML (INSERT, UPDATE, DELETE, MERGE)
- Time Travel (limited — see Limitations)
- Data governance (masking policies, row access policies)
- Automatic compaction managed by Snowflake

### 3.2 Externally Managed Iceberg Tables

An external catalog (e.g., AWS Glue, Unity Catalog) manages the metadata. Snowflake can:
- **Query** the table (read)
- **Write** to externally managed tables (with write support enabled via REST catalog)
- Govern the table with RBAC and masking policies

```sql
-- Externally managed Iceberg table with a REST catalog
CREATE OR REPLACE ICEBERG TABLE my_iceberg_table
  EXTERNAL_VOLUME = 'my_external_volume'
  CATALOG = 'my_rest_catalog_integration'
  CATALOG_TABLE_NAME = 'my_remote_table_name';
```

> To convert an externally managed table to Snowflake-managed (full platform support), use `SYSTEM$SET_CATALOG_INTEGRATION`.

### 3.3 Catalog-Linked Database

A **catalog-linked database** automatically discovers and stays in sync with namespaces and tables in a remote Iceberg REST catalog.

```sql
CREATE DATABASE my_iceberg_db
  CATALOG = 'my_rest_catalog_integration';
```

Compatible with: Databricks Unity Catalog, AWS Glue, Snowflake Open Catalog.

---

## 4. Supported Formats

| Format | Support |
|--------|---------|
| **Parquet** | ✅ Primary data file format |
| **Delta Lake** (Delta Direct) | ✅ Via `TABLE_FORMAT = DELTA` catalog integration |
| ORC / Avro | ❌ Not supported |

---

## 5. Iceberg Tables vs. Native Snowflake Tables

| Feature | Native (Permanent) Table | Iceberg Table |
|---------|--------------------------|---------------|
| Data stored in | Snowflake internal storage | Your cloud storage (S3/ADLS/GCS) |
| Data ownership | Snowflake | You |
| File format | Snowflake proprietary | Open Parquet (Iceberg format) |
| DML support | ✅ Full | ✅ Full (Snowflake-managed) |
| Time Travel | ✅ Up to 90 days | ⚠️ Limited (see below) |
| Fail-Safe | ✅ 7 days | ❌ Not supported |
| Multi-engine access | ❌ Snowflake only | ✅ Spark, Trino, Flink, etc. |
| Cloning | ✅ Supported | ❌ Not supported |
| Replication | ✅ Supported | ❌ Not supported |
| Transient / Temporary types | ✅ Supported | ❌ Only permanent Iceberg tables |
| Governance (RBAC, masking) | ✅ | ✅ |
| Compaction | Auto (Snowflake) | Auto (Snowflake handles lifecycle) |

---

## 6. Iceberg Tables vs. External Tables

| Feature | External Tables | Iceberg Tables |
|---------|-----------------|----------------|
| Data location | External stage | External cloud storage |
| DML | ❌ Read-only | ✅ Full DML (Snowflake-managed) |
| Time Travel | ❌ Not supported | ⚠️ Limited |
| Performance | Slower | First-class, comparable to native |
| Governance | Limited | ✅ Full RBAC + masking policies |
| File format | Any (CSV, JSON, Parquet…) | Parquet only |

> **Exam tip:** Iceberg tables are "first-class citizens" — unlike legacy external tables which are read-only and slower.

---

## 7. Limitations ⚠️ (Exam-Relevant)

| Limitation |
|------------|
| Only **permanent** Iceberg tables — no transient or temporary |
| **Fail-safe is not supported** |
| **Time Travel in Spark is not supported** for Snowflake-managed Iceberg tables |
| **Cannot clone** Iceberg tables |
| **Cannot replicate** Iceberg tables |
| Only **Parquet** is supported as the data file format |
| External volume must be in the **same cloud and region** as the Snowflake account (cross-cloud/cross-region not supported for standard setup) |
| Third-party clients **cannot modify data** in Snowflake-managed Iceberg tables |

---

## 8. Data Governance on Iceberg Tables

Snowflake extends its full governance model to Iceberg tables:

- **Role-Based Access Control (RBAC)** — same as native tables
- **Column-level masking policies** — applied via `ALTER ICEBERG TABLE`
- **Row access policies** — supported
- **Object tagging** — supported

```sql
-- Apply a masking policy to an Iceberg table column
ALTER ICEBERG TABLE myIcebergTable
  MODIFY COLUMN email
  SET MASKING POLICY email_mask;
```

---

## 9. Authentication for Catalog Integrations

Snowflake supports the following authentication methods for Iceberg REST catalogs:

| Method | Details |
|--------|---------|
| **OAuth** | OAuth2 client ID + secret + allowed scopes |
| **Vended credentials** | Catalog provides temporary credentials for storage access |
| **External volume credentials** | Snowflake uses its own external volume credentials |

To rotate credentials:
```sql
ALTER CATALOG INTEGRATION my_cat_int
  SET REST_AUTHENTICATION (
    OAUTH_CLIENT_SECRET = 'myNewSecret'
  );
```

---

## 10. Creating Iceberg Tables — Syntax Patterns

### From Iceberg Metadata in Object Storage
```sql
CREATE ICEBERG TABLE myIcebergTable
  EXTERNAL_VOLUME = 'icebergMetadataVolume'
  CATALOG = 'icebergCatalogInt'
  METADATA_FILE_PATH = 'path/to/metadata/v1.metadata.json';
```

### From a Remote Iceberg REST Catalog (Auto Refresh)
```sql
CREATE OR REPLACE ICEBERG TABLE my_iceberg_table
  EXTERNAL_VOLUME = 'my_external_volume'
  CATALOG = 'my_rest_catalog_integration'
  CATALOG_TABLE_NAME = 'my_remote_table'
  AUTO_REFRESH = TRUE;
```

### From Delta Lake Files (Delta Direct)
```sql
CREATE ICEBERG TABLE my_delta_iceberg_table
  CATALOG = delta_catalog_integration
  EXTERNAL_VOLUME = delta_external_volume
  BASE_LOCATION = 'relative/path/from/ext/vol/'
  AUTO_REFRESH = TRUE;
```

---

## 11. Iceberg Table Setup Checklist

```
1. ✅ Configure an External Volume → points to your cloud storage
2. ✅ Configure a Catalog Integration → connects Snowflake to the external Iceberg catalog
3. ✅ Create the Iceberg Table → reference the external volume + catalog integration
4. ✅ (Optional) Create a Catalog-Linked Database → auto-syncs all tables in a remote catalog
```

---

## 12. When to Use Iceberg Tables

| Use Case | Recommendation |
|----------|---------------|
| Data already in cloud storage in Iceberg format, no migration wanted | ✅ Use Iceberg Tables |
| Need multi-engine access (Spark, Flink, Trino) | ✅ Use Iceberg Tables |
| Need open format for data portability / avoid vendor lock-in | ✅ Use Iceberg Tables |
| Need maximum Time Travel (90 days) + Fail-Safe | ❌ Use Native Permanent Tables |
| Need cloning and replication | ❌ Use Native Permanent Tables |
| Staging / intermediate data | ❌ Use Transient Tables |

---

## 13. Exam Tips 🎯

- **Know why Iceberg tables exist**: open format, data ownership, multi-engine interoperability
- **Know the three key objects**: External Volume, Catalog Integration, Iceberg Table
- **Remember the limitations**: no Fail-Safe, no transient/temporary types, no cloning, no replication, Parquet only
- **Iceberg ≠ External Table**: Iceberg supports DML and better performance; external tables are read-only
- **Snowflake as Catalog = full support**; External Catalog = limited features
- **COF-C03 focus**: understand positioning and use cases — not deep operational syntax
- **Table type context**: Snowflake has 6 table types — Permanent, Transient, Temporary, External, Dynamic, and Iceberg. Know the differences.

---

## 14. Quick Comparison: All Snowflake Table Types

| Table Type | Time Travel | Fail-Safe | Persists After Session | DML | Data Location |
|------------|------------|-----------|------------------------|-----|---------------|
| Permanent | ✅ 0–90 days | ✅ 7 days | ✅ Yes | ✅ | Snowflake internal |
| Transient | ✅ 0–1 day | ❌ | ✅ Yes | ✅ | Snowflake internal |
| Temporary | ✅ 0–1 day | ❌ | ❌ Session only | ✅ | Snowflake internal |
| External | ❌ | ❌ | ✅ Yes | ❌ Read-only | External stage |
| Dynamic | ❌ | ❌ | ✅ Yes | ❌ Auto-managed | Snowflake internal |
| **Iceberg** | ⚠️ Limited | ❌ | ✅ Yes | ✅ (Snowflake-managed) | **Your cloud storage** |

---

## 15. Summary

Apache Iceberg Tables in Snowflake bridge the gap between **open-format data lakes** and **governed, high-performance analytics**. They let you store data in your own cloud storage in an open format (Parquet / Iceberg spec) while using Snowflake for compute, security, and governance — enabling true **multi-engine interoperability** without data migration.

For the SnowPro Core exam, focus on:
1. **What** Iceberg tables are and **why** they exist
2. **How they differ** from native tables and external tables
3. **Key limitations** (no Fail-Safe, no cloning, no transient/temporary, Parquet only)
4. **Three setup objects**: External Volume → Catalog Integration → Iceberg Table

---

*Study Guide — Apache Iceberg™ Tables | Snowflake SnowPro Core (COF-C02 / COF-C03)*
