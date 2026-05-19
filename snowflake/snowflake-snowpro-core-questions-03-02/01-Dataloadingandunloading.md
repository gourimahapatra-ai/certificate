# Snowflake Supported Semi‑Structured Data Formats

Snowflake provides **native, built‑in support** for several major semi‑structured data formats. These formats can be loaded, queried, and processed directly using the `VARIANT`, `OBJECT`, and `ARRAY` data types.  
Snowflake documentation confirms support for the following formats:

---

## Supported Semi‑Structured Formats

- **JSON**  
  Widely used for APIs, logs, IoT events, and nested hierarchical data. 

- **Avro**  
  A row‑based binary format commonly used in streaming pipelines and Kafka ingestion. 

- **ORC**  
  A columnar binary format optimized for analytics and used heavily in Hadoop ecosystems. 

- **Parquet**  
  A highly efficient columnar format ideal for large analytical workloads and cloud data lakes. 

- **XML**  
  A markup language used in enterprise systems, web services, and document‑centric workflows. 

---

## Exam‑Ready Takeaway
> **Snowflake natively supports JSON, Avro, ORC, Parquet, and XML as semi‑structured data formats.**  
> These formats can be loaded directly into `VARIANT` columns and queried using SQL.


### Which mechanism allow a Snowflake customer to query data without loading it first?

Snowflake offers an alternative approach for tables called external tables, which permits the creation of tables with data stored in external cloud storage. External tables remove the need for the data to be loaded into Snowflake. In the case of an External table, the definition of the table is still stored in Snowflake metadata and consists of table structure, file locations, filenames, and other attributes. However, the table's data is saved outside of Snowflake. The external table functionality enables you to query external data like a standard table. External tables may be joined to other tables, and views may be created using them. https://docs.snowflake.com/en/user-guide/tables-external-intro


### Snowflake can transform data after a partner software has loaded it. True
After data has been loaded into Snowflake through partner software, Snowflake SQL or other mechanisms can transform data within Snowflake.

### Table stages are internal stages automatically created for each table and can be used to load data into that table.

Each user also automatically gets an internal stage object, created as soon as a user is created.

# Internal Stages in Snowflake — Table Stages & User Stages

Snowflake automatically creates several **internal stages** to simplify data loading and unloading.  
Two of the most important built‑in stage types are **table stages** and **user stages**.

---

## Table Stages (`@%table_name`)
Every table in Snowflake automatically has its own **table stage**.

### Key Points
- Created **automatically** when the table is created.
- Used primarily for **loading data into that specific table**.
- Referenced using the syntax:

```sql
@%my_table
```

### Typical Use Cases
- Loading files directly into the table:

```sql
COPY INTO my_table
FROM @%my_table;
```

- Storing small, table‑specific files temporarily.

---

## User Stages (`@~`)
Each Snowflake user also automatically gets a **personal internal stage**.

### Key Points
- Created **as soon as the user is created**.
- Private to the user.
- Useful for ad‑hoc file uploads and testing.
- Referenced using:

```sql
@~
```

### Example
Upload a file from your local machine:

```sql
PUT file://data.csv @~;
```

List files:

```sql
LIST @~;
```

---

## Summary Table

| Stage Type | Automatically Created | Scope | Reference | Typical Use |
|------------|-----------------------|--------|-----------|--------------|
| **Table Stage** | Yes (per table) | Table‑specific | `@%table_name` | Loading data into that table |
| **User Stage** | Yes (per user) | User‑specific | `@~` | Ad‑hoc uploads, testing |

---

## Exam‑Ready Takeaway
> **Table stages** are automatically created for each table and used to load data into that table.  
> **User stages** are automatically created for each user and provide a private internal stage for file operations.



### Snowflake supports data loading in two primary ways. The COPY command can be used to load bulk data or huge files. To load data into a table, the COPY command requires the usage of a virtual warehouse. The other method of loading data into Snowflake is via the Snowpipe. Snowpipe is the ideal technique for loading data when the data is arriving continuously in a messaging or streaming manner. 

https://docs.snowflake.com/en/user-guide/data-load-overview#bulk-vs-continuous-loading



## The FROM clause can be omitted when loading data from a table stage. In such a case, Snowflake automatically assumes data is being loaded from the table stage.

So both COPY INTO EMPLOYEE; and COPY INTO EMPLOYEE FROM @%EMPLOYEE; are correct.

https://docs.snowflake.com/en/user-guide/data-load-local-file-system-copy#table-stage

- COPY INTO EMPLOYEE FROM @%EMPLOYEE;
- COPY INTO EMPLOYEE;

