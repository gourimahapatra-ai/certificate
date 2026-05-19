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