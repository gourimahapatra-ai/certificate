### Which statements are correct regarding the costs of using event notifications to refresh a directory table's metadata?

A small maintenance cost is charged for refreshing a directory table's metadata, whether through notifications or manually (through ALTER STAGE <stage-name> REFRESH). This small maintenance cost is accounted for under the cloud services costs.
Additionally, when using cloud platform notifications, an additional cost is charged, which appears as Snowpipe charges in your billing statement. The Snowpipe cost is charged because Snowpipe is used for event notifications to trigger the automatic refresh.

https://docs.snowflake.com/en/user-guide/data-load-dirtables-intro#billing-for-directory-tables



### When a directory table is queried, the result set contains the FILE_URL for each file in the stage object. The result set also contains additional metadata, such as the file's relative path, which shows the file's path relative to the stage. The result set also has metadata such as the size of the file in bytes and the timestamp of when a file was last modified, the MD5 checksum for the file, and an ETAG file, which changes if the contents of the file change. When querying a directory table, you can filter the result set using the WHERE clause on any of these fields. For example, you can use the size column to limit your results to only those files that are greater than 10MB.

https://docs.snowflake.com/en/user-guide/data-load-dirtables-manage#output



###  Which file function allows any user or application access to download unstructured data in a Snowflake stage? GET_PRESIGNED_URL

A pre-signed URL is a simple HTTPS URL for accessing a file using a web browser. A pre-signed URL is generated using a pre-signed access token. Users can temporarily access a file via a pre-signed URL without authorization. The expiry duration of a pre-signed URL is configurable and can be set to the required duration.


### Which sampling method in Snowflake is more efficient for querying large datasets?
SYSTEM (Block) Method

The SYSTEM sampling method in Snowflake operates at the micro-partition (block) level, making it highly efficient for large datasets. By sampling entire blocks, it reduces computational overhead and accelerates query performance compared to row-level sampling.



### Which of the following methods is used to access elements within a variant column in Snowflake? : 
Ans : Using the colon (:) to access elements by name

Using a dollar sign ($) followed by the number of the column : The dollar sign ($) followed by a number is used for positional access, but not directly for accessing elements by name.

### The INSERT OVERWRITE command removes all existing rows in a table and replaces them with the new rows specified in the command. It effectively truncates the table before inserting the new data.



### Which of the following best describes a transient table in Snowflake? A table that is persistent across sessions, supports Time Travel, but does not maintain Fail-safe storage.


This is the correct description of a transient table in Snowflake. It is a table that persists across sessions, allowing users to access it in different sessions. It supports Time Travel functionality, which enables users to access historical data, but it does not provide Fail-safe storage for data protection.

### What system function in Snowflake provides information on clustering depth for a given table?
SYSTEM$CLUSTERING_DEPTH

SYSTEM$CLUSTERING_DEPTH is the function that returns information about the clustering depth of a table, showing how effectively the data is organized in micro partitions based on clustering keys.

# ❓ Question 49  
**What system function in Snowflake provides information on clustering depth for a given table?**

---

## ✅ Correct Answer  
### **SYSTEM$CLUSTERING_DEPTH**

**Explanation:**  
`SYSTEM$CLUSTERING_DEPTH` returns detailed information about the **clustering depth** of a table.  
Clustering depth indicates **how well‑organized** the micro‑partitions are with respect to the defined clustering keys.  
Lower depth = better clustering = more efficient pruning.

---

## ❌ Incorrect Options and Why They Are Wrong

### **SYSTEM$CLUSTERING_INFO**  
Provides general clustering information (e.g., average overlap, partition stats),  
but **does NOT return clustering depth** specifically.

---

### **SYSTEM$CLUSTERING_OVERLAP**  
Not a valid Snowflake system function.

---

### **SYSTEM$MICRO_PARTITIONS**  
This function **does not exist**.  
Micro‑partitions are internal and cannot be queried directly through such a function.

---

## 📘 Domain  
**Data Transformations**

### Which Snowflake function is best suited for approximating the number of distinct values in a large dataset to improve performance over exact calculation?
APPROX_COUNT_DISTINCT

Explanation
APPROX_COUNT_DISTINCT uses the HyperLogLog algorithm to efficiently estimate the number of distinct values in large datasets, providing a fast alternative to exact calculations.


### Which of the following columns would benefit most from a clustering key? (Choose two.)

A column used frequently in WHERE clauses

Explanation
Columns frequently used in WHERE clauses are ideal for clustering keys because clustering helps in partition pruning, improving query performance.

A column used primarily in ORDER BY clauses

Explanation
Columns used in ORDER BY clauses can also benefit from clustering keys as it can help optimize sorting operations.


### Which Snowflake feature ensures that micro partitions are automatically reorganized when clustering keys are defined?

Automatic Reclustering

Explanation
Snowflake uses automatic reclustering when clustering keys are defined. This serverless feature reorganizes the micro partitions based on the clustering keys to optimize query performance and data distribution.

### Which of the following is mandatory when creating a stored procedure in Snowflake?

A return type must be declared, even if the procedure does not return a value.

A return type is always required when creating a stored procedure, even if it does not return any actual value. This is a syntax requirement in Snowflake’s procedure creation process, making this option correct.

### Which of the following can be used to access an element within an array in a Snowflake VARIANT column?
Square brackets ([])

Explanation
Square brackets are used to access specific elements within arrays stored in a Snowflake VARIANT column. For example, [0] would access the first element of the array.


### A company has a large fact table containing 5 years of sales transactions with 2 billion rows. Query performance has degraded significantly, and the data engineering team notices that most queries filter by the TRANSACTION_DATE column. The team wants to physically reorganize the table's micro-partitions to improve query performance when filtering on this date column. Which Snowflake feature should they use?

Create a materialized view that pre-filters data by date ranges to improve query performance.

Explanation
While materialized views can improve query performance by pre-computing and storing results, they don't address the underlying issue of micro-partition organization in the base table. Additionally:

Materialized views add storage costs (duplicate data)

They're better suited for complex aggregations or joins, not simple date filtering

The question specifically asks about physically reorganizing the table's micro-partitions

Queries against the base table would still experience poor performance


