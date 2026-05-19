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

