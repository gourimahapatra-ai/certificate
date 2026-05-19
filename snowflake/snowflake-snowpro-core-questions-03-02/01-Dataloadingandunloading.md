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


### Which of the following statements is true regarding the COPY INTO command in Snowflake?

The COPY INTO command requires an active warehouse for execution.

The COPY INTO command requires an active virtual warehouse to provide the compute resources necessary for loading or unloading data. Without an active warehouse, the command cannot execute as there are no compute resources to process the data.


### External stages in Snowflake must always include storage credentials within the stage definition. : False
While external stages can include credentials, it is not required or recommended. The preferred method is to use a storage integration object to securely manage credentials separately from the stage definition. This improves security by preventing direct exposure of sensitive information like access keys.


### What is the recommended method for specifying file format properties when using the COPY INTO command?

Using a file format object and referencing it in the stage
The recommended method is to create a separate file format object and reference it in the stage. This allows for consistency and reusability, as the same file format can be applied across multiple stages without redefinition. This approach also keeps configurations organized and easy to manage.


### Which of the following views in Snowflake provides detailed information about table storage, including data compression and partitioning?

TABLE_STORAGE_METRICS

Explanation
This view provides detailed information about table storage, including data size, compression ratios, and partitioning. It's used to analyze storage utilization for specific tables in Snowflake.

### What information can be obtained from the TABLE_STORAGE_METRICS views in Snowflake? (Choose two.)

Total storage used for Time Travel

Explanation
The TABLE_STORAGE_METRICS views include details on storage for active databases, time travel, and failsafe storage.

Amount of storage consumed by deleted tables

Explanation
his view also provides information on storage used by dropped tables, which remain available through time travel and failsafe features.

### Which of the following is the default value for the ON_ERROR option when using Snowflake’s bulk loading process?

ABORT_STATEMENT

Explanation
The default value for the ON_ERROR option in Snowflake's bulk loading process is ABORT_STATEMENT. This setting stops the entire loading process when any error is encountered in any file or row, ensuring that no partial data is loaded.

 
### Which of the following transformations is NOT supported directly in the COPY INTO command in Snowflake?

Filtering rows using a WHERE clause

Explanation
Filtering rows using a WHERE clause is not supported in the COPY INTO command. The command allows some basic transformations such as column reordering, data type casting, and truncating column values, but complex operations like filtering rows are not permitted.

### Which of the following statements is true about enabling an external table in Snowflake?
It requires a manual refresh of metadata after enabling.

Explanation
After enabling an external table, performing a manual metadata refresh is necessary to ensure that the table is aware of any new or updated data files in the external stage. This is typically done using the ALTER EXTERNAL TABLE <table_name> REFRESH; command.

### Which of the following is NOT a type of internal stage in Snowflake?

 Schema stage

Explanation
There is no "Schema stage" in Snowflake. The internal stages in Snowflake include User stages, Table stages, and Named internal stages. These internal stages allow different levels of access and control, but none is associated with a schema directly.

Named internal stage

Explanation
The Named internal stage is a flexible and customizable stage created and managed like any other database object in Snowflake.

User stage

Explanation
The User stage is a valid internal stage tied to individual users.

able stage

Explanation
The Table stage is another valid internal stage specifically associated with an individual table.


### Which of the following statements about Snowflake stages is correct?
A stage can be either internal or external to Snowflake.

Explanation
Snowflake stages can be categorized as internal (hosted within Snowflake) or external (integrated with cloud storage services like Amazon S3, Azure Blob Storage, or Google Cloud Storage). They are designed to facilitate data loading and unloading.

