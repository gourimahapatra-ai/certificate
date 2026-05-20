Which of the following is true when a virtual warehouse is scaled up to a larger size? Select all that apply.

- The increased size does not affect any queries already executing on the virtual warehouse.
- The charging for the new size is not started until all new nodes in the larger virtual warehouse are provisioned.
- Only new queries benefit from the larger virtual warehouse size.

# Snowflake Warehouse Scaling — Billing & Query Behavior

## Key Facts
- When a warehouse is **scaled up**, Snowflake **does not start charging for the larger size** until **all new compute nodes are fully provisioned**.
- **Existing queries continue running** on the original warehouse size.
- **Only new queries** use the newly scaled‑up resources.

---

## What Happens During Scale‑Up?

### 1. **Billing Behavior**
- Billing for the new (larger) size **begins only after** all additional compute resources are successfully provisioned.  
- Until then, Snowflake continues billing at the **old warehouse size**.

### 2. **Query Behavior**
- **Running queries are unaffected** by resizing.  
  They continue using the original compute resources.
- **New queries** submitted after the resize use the **new, larger** warehouse size.

This ensures:
- No query restarts  
- No performance regression  
- Smooth transition during resizing

---

## Exam‑Ready Takeaway
> **Scaling up a warehouse does not interrupt running queries, and billing for the larger size starts only after all new nodes are provisioned. Only new queries benefit from the increased size.**

# Multi‑Cluster Virtual Warehouses — Auto‑Scaling vs. Maximized Mode

Snowflake supports two behaviors for **multi‑cluster virtual warehouses**:  
**Auto‑Scaling Mode** and **Maximized Mode**.  
These determine how clusters start, stop, and scale based on workload.

---

## Auto‑Scaling Mode

Auto‑scaling is enabled when:

- **Minimum clusters ≠ Maximum clusters**  
  (e.g., min = 1, max = 3)

### How It Works
- Snowflake **automatically starts additional clusters** when concurrency increases.
- Snowflake **automatically suspends clusters** when demand drops.
- Scaling is **dynamic** and workload‑driven.

### Benefits
- Efficient credit usage  
- Smooth handling of concurrency spikes  
- No manual intervention needed  

---

## Maximized Mode

Maximized mode is enabled when:

- **Minimum clusters = Maximum clusters**  
  (e.g., min = 3, max = 3)

### How It Works
- **All clusters start immediately** when the warehouse is resumed.
- No auto‑scaling occurs — the warehouse always runs at full cluster count.
- Designed for **maximum throughput** and **predictable performance**.

### Benefits
- Highest concurrency capacity  
- No startup delays for additional clusters  
- Ideal for heavy, consistent workloads  

---

## Comparison Table

| Mode | Min/Max Setting | Behavior | Best For |
|------|------------------|----------|----------|
| **Auto‑Scaling** | min ≠ max | Starts/stops clusters dynamically | Variable workloads, cost efficiency |
| **Maximized** | min = max | All clusters run immediately | High, steady concurrency needs |

---

## Exam‑Ready Takeaway
> **Auto‑Scaling Mode** = dynamic start/stop based on workload.  
> **Maximized Mode** = all clusters run at once because min = max.


### Which of the following best describes “Bytes spilled to local storage” shown in a query profile?

Snowflake saves data on the warehouse's local disk if it can't fit an operation into memory. Data spilling slows down queries because it requires more IO operations, and disk access is slower than memory access. "Bytes spilled to local storage." indicates local spillage. Snowflake will spill data to remote cloud storage if the local disk becomes full, which is even slower storage than the local disk, making this operation even slower. "Bytes spilled to remote storage" in the query profile indicates remote spillage. https://docs.snowflake.com/en/user-guide/ui-query-profile#queries-too-large-to-fit-in-memory



### Multi-cluster virtual warehouses dynamically (and automatically) add additional clusters based on demand to solve the queueing issue. When demand decreases, the additional clusters are decommissioned. This process is also known as scaling out (and scaling back) or auto-scaling.



Scaling up and down is a manual process, requiring someone to run a statement to increase or decrease the size of the virtual warehouse.



https://docs.snowflake.com/en/user-guide/warehouses-multicluster



### A multi-cluster virtual warehouse :
can be created in maximized or auto-scaling modes. The maximized mode is enabled by setting the minimum and maximum warehouse count of the multi-cluster to the same value. Therefore, as soon as the multi-cluster virtual warehouse is established, all warehouses in the multi-cluster are started up. Auto-Scaling mode is enabled by selecting different values for the multi-minimum clusters and maximum warehouse count. As a result, Snowflake starts and stops warehouses dynamically based on the workload needs. https://docs.snowflake.com/en/user-guide/warehouses-multicluster#setting-the-scaling-policy-for-a-multi-cluster-warehouse


### USE_CACHED_RESULT : Query Result Cache reuse can be turned off using which parameter?
Query result cache is enabled by default but can be turned off at a session, user, or account level using the USE_CACHED_RESULT parameter. https://docs.snowflake.com/en/user-guide/querying-persisted-results



### Snowflake's re-clustering operation is transparent to the user and does not block any DML or SELECT queries. A table that is being re-clustered will behave exactly like any other table when being queried, updated, or changed.

https://docs.snowflake.com/en/user-guide/tables-auto-reclustering#non-blocking-dml


### A materialized view is a view that pre-computes data based on a SELECT query. The query's results are pre-computed and physically stored to enhance performance for similar queries that are executed in the future. When the underlying table is updated, the materialized view refreshes automatically, requiring no additional maintenance. Snowflake-managed services perform the update in the background transparent to the user without interfering with the user's experience. 
https://docs.snowflake.com/en/user-guide/views-materialized



### Typically, a virtual warehouse has a defined set of computing resources that it can use to execute queries. When queries are sent to a warehouse, the warehouse allocates the resources required for each query and begins running the queries. If there aren't enough resources to run all the queries sent to the warehouse, Snowflake queues the extra queries until the resources are available again. Snowflake provides multi-cluster virtual warehouses to overcome this issue. Multi-cluster virtual warehouses are frequently used in scenarios where the number of concurrent queries exceeds the capacity of a single virtual warehouse. When a virtual warehouse's concurrent workload exceeds its maximum capacity, additional queries are placed in the queue. Multi-cluster virtual warehouses dynamically add additional clusters based on demand to solve the queueing issue. When demand decreases, the additional clusters are decommissioned. This process is also known as scaling out or auto-scaling.


### For a multi-cluster virtual warehouse, what is the maximum number of clusters? Ans : 10
A multi-cluster virtual warehouse supports anywhere from one and ten different clusters simultaneously. The minimum number of clusters supported is one, and the maximum number of allowed clusters is ten.
https://docs.snowflake.com/en/user-guide/warehouses-multicluster#what-is-a-multi-cluster-warehouse


### For an unpopulated table, the clustering depth is ________?

Zero : For a populated table, the clustering depth is the average depth of overlapping micro-partitions for specific columns. The clustering depth starts at 1 (for a well-clustered table) and can be a larger number. For an unpopulated table, the clustering depth is zero. https://docs.snowflake.com/en/user-guide/tables-clustering-micropartitions#label-clustering-depth



### Which of the following correctly describes materialized views?

### Materialized views are created to improve the performance of specific queries.
### Materialized view refreshes are performed automatically.

A materialized view is a view that pre-computes data based on a SELECT query. The query's results are pre-computed and physically stored to enhance performance for similar queries that are executed in the future. When the underlying table is updated, the materialized view refreshes automatically, requiring no additional maintenance. Snowflake-managed services perform the update in the background transparent to the user without interfering with the user's experience.


### Which of the following are caching mechanisms in Snowflake? Select all that apply.

Metadata Caching
Query Result Caching
Warehouse Caching

Metadata caching is used for queries that can be fulfilled directly from metadata, e.g., the row count of a table Query Result Caching is for queries that have been executed already. Warehouse caching is within the virtual warehouse instance and is usually based on queries that have already been executed.


### Which query profile results indicate that a large table may not be well clustered? Select all that apply.

-- A significant value for ‘Partitions Scanned.’
-- The value in the ‘Partitions Total’ equals ‘Partitions Scanned.’


### Query Result Cache can be turned off at which levels? Select all that apply.

Account, User, Session

Query result cache is enabled by default but can be turned off at a session, user, or account level using the USE_CACHED_RESULT parameter. https://docs.snowflake.com/en/user-guide/querying-persisted-results

### The Search Optimization service can be used to improve the performance of which type of queries?

Selective point lookup queries

Overall explanation
The search optimization service can be used to improve the performance of



Point lookup queries - return only one or a few rows using highly selective filters.

Substring & RegEx searches – queries that use LIKE, ILIKE, & RLIKE

Queries on fields in VARIANT, OBJECT & ARRAY columns – using equality conditions, IN, ARRAY_CONTAINS, ARRAY_OVERLAP, Substring & RegEx and NULL check conditions

Queries that use specific geospatial functions with GEOGRAPHY values.



https://docs.snowflake.com/en/user-guide/search-optimization-service#understanding-the-search-optimization-service


### Which of the following strategies should be used to optimize the performance of a virtual warehouse?

1. Reduce queuing

2. Resolve memory spillage.

3. Increase warehouse size.

4. Try query acceleration.

5. Optimize the warehouse cache.

6. Limit concurrently running queries.



### Which of the following statements is true about Snowflake's Resource Monitors? (Choose two.)

- Resource Monitors can be set at both account and warehouse levels.
- They can be used to suspend a warehouse immediately when a limit is exceeded.

### Which table type in Snowflake does NOT support the Failsafe feature?
- Both Transient Tables and Temporary Tables : Transient Tables and Temporary Tables do not support the Failsafe feature. Failsafe is only available for permanent tables, providing a seven-day recovery period beyond Time Travel.

### The Standard Edition of Snowflake includes disaster recovery features called Fail-safe for up to 7 days beyond Time Travel. True.

The Fail-safe feature, which allows disaster recovery for up to 7 days beyond the Time Travel period, is available in all Snowflake editions, including the Standard Edition.


 ### Which of the following privileges must a role possess to view executed queries and analyze them in Snowflake? Moniter

 The monitor privilege allows the role to view and analyze executed queries, which is necessary for monitoring virtual warehouses and understanding query performance.


### Where can users find the query profile for a completed query in Snowflake? (Choose two.)

Directly from the Worksheet for the last executed query : Users can also directly access the query profile for the most recent query executed through the Worksheet interface.

In the Query History under the Activity section in Snowflake : The query profile is available in the Query History under the Activity section in Snowflake, where users can access details about executed queries.


### Queries using UDFs are not eligible for the result cache because the results may vary based on the function execution.

The query has been run multiple times within the last 24 hours. : Running the query multiple times within the last 24 hours will refresh the query result cache rather than invalidate it, as long as the data and conditions remain unchanged.

### Which of the following statements is true about Snowflake’s Search Optimization Service?
It is a serverless feature that incurs additional compute and storage costs

Explanation
The Search Optimization Service is a serverless feature in Snowflake, which incurs additional compute and storage costs as it maintains search access paths for optimized querying.

### What is the primary difference between the "Standard" and "Economy" scaling policies in Snowflake's multi-cluster warehouses?

The "Standard" policy prioritizes performance, while the "Economy" policy conserves credits.

Explanation
The Standard policy favors performance by starting new clusters as soon as needed, while the Economy policy is designed to be more conservative, saving credits even if it may result in slight delays.

### Which of the following caching mechanisms in Snowflake does not require virtual warehouses to be active for it to work?
Query Result Cache

Explanation
The Query Result Cache stores the results of executed queries for 24 hours. If the same query is executed again within this timeframe, Snowflake can return the cached result without needing to activate a virtual warehouse, thereby saving compute resources and reducing latency.


### When configuring a multi-cluster warehouse in Snowflake with the economy scaling policy, under what condition will Snowflake start an additional cluster?

When the system predicts workload sufficient for at least six minutes

Explanation
In the economy scaling policy, Snowflake adds an additional cluster only when it determines there is enough workload to justify running the new cluster for at least six minutes.


### Which of the following types of queries is most likely to benefit from Snowflake's Search Optimization Service?
Selective point lookup queries that use equality predicates in the WHERE clause.

Explanation
The Search Optimization Service is designed to improve the performance of selective point lookup queries, especially those that use equality predicates (e.g., WHERE amount = 100). It works best when the filter returns a small number of rows.


### Which method is not a valid way to access query history in Snowflake?

Accessing the Query Logs stored in the cloud provider’s object storage

Explanation
Query logs are not directly accessed from the cloud provider's object storage. Instead, Snowflake offers structured ways to access query history, such as through the SnowSite interface, Information Schema, or Account Usage Schema.


### Which type of resource monitor action in Snowflake will suspend a warehouse immediately, even if there are currently running queries?
****Suspend immediately

Explanation
This action suspends the warehouse instantly, terminating any ongoing queries. It is used when strict credit usage limits must be enforced.

### Which of the following statements is true about the Search Optimization Service in Snowflake?

It adds a search access path for efficient lookups and is maintained automatically by Snowflake.

The Search Optimization Service creates a search access path to speed up specific queries (e.g., point lookups, substring searches) and is managed automatically by Snowflake once it is enabled. This means that Snowflake takes care of the maintenance and updates without user intervention.

### What is the key difference between the Row (Bernoulli) sampling method and the System (Block) sampling method in Snowflake?

Row sampling applies a random probability to each row, whereas system sampling applies sampling to entire micro-partitions.

Explanation
The Row (Bernoulli) sampling method applies a random probability to each individual row, whereas the System (Block) sampling method applies to entire micro-partitions, making it more efficient for larger datasets but less random.


### Which of the following statements about Snowflake's clustering keys is not true?

Clustering keys are ideal for every table, regardless of size and query patterns.

Explanation
Clustering keys are not ideal for every table. They are most effective for large tables with a high number of micro-partitions and specific query patterns (e.g., selective queries). For smaller tables or tables with low cardinality columns, clustering may not provide significant benefits and could lead to unnecessary costs.

### Which of the following conditions must be met for the result cache in Snowflake to be used? (Choose two.)
The query must be executed within 24 hours of its previous execution.

Explanation
The result cache in Snowflake is available for up to 24 hours. If the query is executed again within this period, the result cache can be used to improve performance.

The underlying table data and micro-partitions must not have changed.

Explanation
For the result cache to be used, the underlying table data and micro-partitions must remain unchanged since the query was last executed.

### Which of the following best describes the credit consumption behavior when using the Search Optimization Service in Snowflake?

Credits are consumed serverlessly and based on the maintenance of the search access path

Explanation
The Search Optimization Service is a serverless feature in Snowflake. Credits are consumed based on the maintenance of the search access path rather than warehouse activity, as this feature operates independently of active warehouses.


### Which of the following is not allowed when creating a materialized view in Snowflake?

Using window functions

Explanation
Window functions are not allowed in materialized views in Snowflake. Materialized views support only a subset of SQL operations and must reference a single base table.