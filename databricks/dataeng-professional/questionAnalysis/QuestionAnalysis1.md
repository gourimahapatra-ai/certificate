# Databricks Practice Questions

---

## Question 1 — Unity Catalog Column Masking

A data engineer needs to hide PII in a `customers` table. They want the masking logic to be applied automatically for all users who query the base table itself.

What is the correct workflow to implement this using Unity Catalog?

### Options

A. Update the table schema to include a `MASK` property in the column metadata.

B. Use a `CREATE MASK` statement followed by a `GRANT MASK` on the table.

C. Create a dynamic view and `REVOKE` access to the base table.

D. Define a masking function and apply it to the table column using `ALTER TABLE`.

### Answer

**D.** Define a masking function and apply it to the table column using `ALTER TABLE`.

---

## Question 2 — Cluster Worker Node Tracking

A data engineer wants to verify which worker node type was used for a specific cluster throughout the last month to ensure it matches the team's efficiency standards.

Which table should they query?

### Options

A. The `system.billing.usage` table filtered by `cluster_id`.

B. The `system.access.audit` table filtered by `cluster_id`.

C. The `system.billing.list_prices` table filtered by instance type.

D. The `system.compute.clusters` table joined with `system.compute.node_types`.

### Answer

**D.** The `system.compute.clusters` table joined with `system.compute.node_types`.

---

## Question 3 — Streaming State Store Growth

A streaming pipeline performs an aggregation based on event time. The data engineer notices that the state store size is growing indefinitely, leading to out-of-memory errors.

How should they manage the state size for late-arriving data?

### Options

A. Use a short `processingTime` trigger to clear the cache.

B. Implement a manual filter on the ingestion timestamp.

C. Increase the cluster size to handle the larger state store.

D. Define a watermark using `withWatermark` to allow state cleanup.

### Answer

**D.** Define a watermark using `withWatermark` to allow state cleanup.

---

## Question 4 — Deduplication with Watermark

A streaming pipeline processes high-volume logs where duplicate records may appear within a 1 hour window. The engineer implements `dropDuplicatesWithinWatermark` to manage memory.

What is the primary benefit of this approach over standard deduplication?

### Options

A. It automatically snapshots the state to a parquet file every hour.

B. It forces the stream to process in micro-batches of exactly one hour.

C. It allows the stream to skip the shuffle phase required for deduplication.

D. It limits the state size by expiring old event keys based on the watermark.

### Answer

**D.** It limits the state size by expiring old event keys based on the watermark.

---

## Question 5 — Delta Change Tracking

A downstream Gold job needs to know which rows were inserted, updated, or deleted in a Silver table since its last run, including the previous values for updates.

Which Delta capability is designed for this?

### Options

A. Auto Loader's `cloudFiles.includeExistingFiles` option.

B. Change Data Feed (CDF), enabled with `delta.enableChangeDataFeed = true`.

C. `DESCRIBE HISTORY`

D. Delta Sharing.

### Answer

**B.** Change Data Feed (CDF), enabled with `delta.enableChangeDataFeed = true`.

---

## Question 6 — Row Filters and Column Masks

A financial services company uses Databricks for sensitive client data analysis. They need to ensure that data analysts can only see client records from their assigned region and that national IDs are always masked.

How can this be achieved efficiently using Unity Catalog?

### Options

A. Develop an external data access service that intercepts queries, applies regional filtering, and masks national IDs before forwarding to Databricks.

B. Create separate tables for each region and grant granular `SELECT` permissions to analysts per table, and use UDFs for national ID masking during query execution.

C. Use Apache Spark SQL views with `WHERE` clauses for regional filtering and `CASE` statements for ID masking, granting `SELECT` on these views.

D. Implement row filters and column masks directly within Unity Catalog for the client data table.

### Answer

**D.** Implement row filters and column masks directly within Unity Catalog for the client data table.

---

## Question 7 — Streaming Tables in Lakeflow

A pipeline needs to ingest high-frequency log data from a cloud landing zone using Auto Loader.

Why would the data engineer choose a Streaming table in a Lakeflow Declarative Pipeline for this task?

### Options

A. They are used to handle complex updates and deletes via `MERGE INTO` statements.

B. They are primarily used to store static reference data that rarely changes.

C. They support incrementally growing datasets and process each row exactly once.

D. They compute the entire dataset from scratch every time the pipeline runs.

### Answer

**C.** They support incrementally growing datasets and process each row exactly once.

---

## Question 8 — Recommended Production Compute

A senior data engineer is designing a production ETL pipeline that runs once every four hours.

Which compute type is most cost-effective and recommended for automated production workloads?

### Options

A. Classic Cluster with an idle timeout of 60 minutes for intermittent runs.

B. All-Purpose Compute to allow for manual debugging if the job fails.

C. Job Compute or Serverless Compute to minimize costs and ensure a clean environment.

D. SQL Warehouse for optimized tabular joins and transformations.

### Answer

**C.** Job Compute or Serverless Compute to minimize costs and ensure a clean environment.

---

## Question 9 — PII Masking in Streaming Pipelines

A streaming pipeline built with Lakeflow Spark Declarative Pipelines ingests unstructured text data that may contain personally identifiable information (PII). Before storing this data in a Delta Lake table for analysis, all credit card numbers and email addresses must be automatically detected and masked.

Which approach is most suitable for achieving this within the streaming pipeline?

### Options

A. Implement an external PII detection service as a separate microservice and use Databricks Asset Bundles to deploy a custom connector to call this service from the streaming job.

B. Define a Unity Catalog column mask that applies a masking function to the PII column when queried, without modifying the raw data at ingestion.

C. Configure Auto Loader to automatically detect and mask PII during data ingestion from the source file system.

D. Integrate a custom Spark UDF that uses regular expressions to identify and replace PII patterns within the streaming DataFrame before writing to Delta Lake.

### Answer

**D.** Integrate a custom Spark UDF that uses regular expressions to identify and replace PII patterns within the streaming DataFrame before writing to Delta Lake.

---

# Question 12 — Lakeflow Declarative Pipelines

A data team is deciding between using Lakeflow Declarative Pipelines and regular Jobs & Pipelines for a new ETL suite.

What is a key advantage of using Lakeflow Declarative Pipelines?

### Options

A. Lakeflow Declarative Pipelines require manual scheduling of each individual task.

B. Regular Jobs are exclusively used for streaming and cannot handle batch.

C. Lakeflow Declarative Pipelines automatically manage data dependencies and environment setup.

D. Regular Jobs offer automatic checkpointing and state management.

### Answer

**C.** Lakeflow Declarative Pipelines automatically manage data dependencies and environment setup.

---

# Question 13 — Trigger.AvailableNow

A data engineer needs to run a streaming pipeline once per day to minimize cluster costs. The pipeline must process all data that has arrived since the last run and then shut down.

Which trigger should be used to satisfy this while ensuring the engine can handle data in multiple micro-batches if needed?

### Options

A. `Trigger.ProcessingTime` set to 0 seconds

B. `Trigger.AvailableNow`

C. `Trigger.Once`

D. `Trigger.Continuous` with a 1 minute interval

### Answer

**B.** `Trigger.AvailableNow`

---

# Question 14 — Audit Access Logs

An internal auditor requires a report showing every user who has accessed a sensitive customer table in the last thirty days.

What is the most efficient way to generate this report?

### Options

A. Enable the log4j appender in the cluster configuration to stream events to a Delta table.

B. Check the Jobs history page for every individual workflow to see who triggered them.

C. Download the diagnostic log files from the cloud provider storage bucket manually.

D. Query the audit tables within the system catalog to view logs of all data access events.

### Answer

**D.** Query the audit tables within the system catalog to view logs of all data access events.

---

# Question 15 — Delta Table Restore

An accidental update command corrupted 10,000 rows in a Delta table named `events`. The data engineer identifies that Version 5 was the last healthy state of the table.

Which command should they use to revert the table to that specific state?

### Options

A. `ALTER TABLE events SET VERSION = 5`

B. `INSERT INTO events SELECT * FROM events VERSION AS OF 5`

C. `SELECT * FROM events VERSION AS OF 5`

D. `RESTORE TABLE events TO VERSION AS OF 5`

### Answer

**D.** `RESTORE TABLE events TO VERSION AS OF 5`

---

# Question 16 — Generated Columns

A Delta table stores raw event timestamps and is frequently filtered by event date. The team wants to derive `event_date` automatically and use it for data layout without users having to compute it on writes.

Which Delta feature fits best?

### Options

A. A view on top of the table that adds the column.

B. A generated column:

```sql
event_date DATE GENERATED ALWAYS AS (CAST(event_ts AS DATE))
```
C. A trigger that updates event_date after each insert.

D. Storing the date as a string in the source files.

Answer

B. A generated column.

Question 17 — Auto Loader Schema Evolution

A streaming ingestion uses Auto Loader to read JSON files. New optional fields appear in the source. The team wants new fields to be added to the table automatically without failing the stream.

(spark.readStream.format("cloudFiles")
   .option("cloudFiles.format", "json")
   .option("cloudFiles.schemaLocation", "/Volumes/main/raw/_schemas/events")
   .option("cloudFiles.schemaEvolutionMode", "___")
   .load("/Volumes/main/raw/events/"))
Options

A. none

B. rescue

C. failOnNewColumns

Answer

B. rescue

# Question 18 — SQL Alerts

A data engineering team needs to be notified immediately if the `processed_timestamp` in a Gold table falls more than 30 minutes behind the current time.

How can this be automated using Databricks SQL?

## Options

A. Increase the `min_clusters` setting in the SQL Warehouse to reduce latency.

B. Use a Python notebook to poll the table and raise a `sys.exit(1)` error.

C. Configure a Lakeflow Declarative Pipeline with a custom expectation.

D. Set up a SQL Alert based on a query that calculates the late-arrival interval.

---

# Answer

✅ **D. Set up a SQL Alert based on a query that calculates the late-arrival interval.**

## Explanation

Databricks SQL Alerts are designed for automated monitoring and notifications based on query results.

A query can calculate the delay between the current timestamp and the latest `processed_timestamp`. If the delay exceeds 30 minutes, the SQL Alert can automatically notify the team through email or configured notification channels.

### Example Query

```sql
SELECT
  TIMESTAMPDIFF(
    MINUTE,
    MAX(processed_timestamp),
    CURRENT_TIMESTAMP()
  ) AS delay_minutes
FROM gold_table;
```


# Question 19 — Databricks Asset Bundle Deploy

An engineer has finished updating a Lakeflow Declarative Pipeline defined in a bundle. They want to upload the updated code and metadata to the production workspace without immediately triggering a run.

Which command should they use?

## Options

A. `databricks bundle deploy -t prod`

B. `databricks job create --bundle prod`

C. `databricks bundle validate -t prod`

D. `databricks bundle run -t prod`

---

# Answer

✅ **A. `databricks bundle deploy -t prod`**

## Explanation

`databricks bundle deploy` uploads and deploys the bundle resources (jobs, pipelines, metadata, configurations) to the target workspace without executing them.

- `deploy` → Upload resources
- `run` → Execute resources
- `validate` → Only validate configuration locally

---

# Question 20 — Delta Sharing Recipient Management

A large enterprise needs to share various datasets with numerous internal departments and several external partners. Some internal departments are on Databricks, others use custom Spark clusters. External partners use a mix of Databricks and non-Databricks platforms.

The enterprise prioritizes simplifying recipient management and ensuring consistent access policies across all shared data.

What is the most effective strategy for managing these diverse recipients and data access?

## Options

A. Export all data to a common cloud storage location and share direct storage access links.

B. Migrate all recipients to Databricks to standardize on Databricks-to-Databricks sharing.

C. Utilize Unity Catalog's recipient management features to create recipients, assign them to shares, and leverage the appropriate Delta Sharing protocol (D2D or open) based on their platform.

D. Create a separate Delta Sharing share for each recipient and manually manage credentials.

---

# Answer

✅ **C. Utilize Unity Catalog's recipient management features to create recipients, assign them to shares, and leverage the appropriate Delta Sharing protocol (D2D or open) based on their platform.**

## Explanation

Unity Catalog provides centralized governance and recipient management for Delta Sharing.

It supports:

- Databricks-to-Databricks (D2D) sharing
- Open Delta Sharing for non-Databricks platforms
- Centralized access control
- Simplified recipient administration

This is the recommended enterprise-scale sharing approach.

---

# Question 21 — Live Cross-Workspace Data Sharing

A data engineering team frequently updates a set of curated Delta tables containing financial transaction data. A downstream analytics team requires access to the absolute latest version of this data, without any delays due to data copying or ETL processes.

The analytics team operates in a separate Databricks workspace within the same organization.

How can the engineering team provide this real-time, live data access?

## Options

A. By granting the analytics team direct read access to the underlying cloud storage location of the Delta tables.

B. By using Lakeflow Spark Declarative Pipelines to continuously replicate data between the workspaces.

C. By using Databricks-to-Databricks Delta Sharing to share the live Delta tables from Unity Catalog.

D. By setting up a scheduled ETL job to copy the Delta tables to the analytics team's workspace hourly.

---

# Answer

✅ **C. By using Databricks-to-Databricks Delta Sharing to share the live Delta tables from Unity Catalog.**

## Explanation

Databricks-to-Databricks Delta Sharing enables secure live sharing of Delta tables across workspaces without copying data.

Benefits:

- Real-time access
- No ETL duplication
- Central governance via Unity Catalog
- Secure read-only sharing

---

# Question 22 — Identity Columns

A team is building a dimension table and requires a strictly monotonic surrogate key that cannot be manually overridden by insert statements.

Which syntax should the engineer use when defining the ID column?

## Options

A. `GENERATED BY DEFAULT AS IDENTITY`

B. `GENERATED ALWAYS AS IDENTITY`

C. `SEQUENCE START WITH 1`

D. `AUTO_INCREMENT PRIMARY KEY`

---

# Answer

✅ **B. `GENERATED ALWAYS AS IDENTITY`**

## Explanation

`GENERATED ALWAYS AS IDENTITY` ensures:

- Automatic surrogate key generation
- Strict monotonic incrementing
- Users cannot manually override inserted values

`BY DEFAULT` still allows manual overrides.

---

# Question 23 — Running Child Notebooks

An engineer wants to execute a child notebook from a parent notebook and pass specific configuration values as parameters. The child notebook should run in its own scope to avoid variable name collisions.

Which approach should they use?

## Options

A. Use `dbutils.notebook.run` and pass a dictionary to the arguments parameter.

B. Use `%run` and rely on global environment variables to share data.

C. Use `%run` which automatically creates a new job run for the target notebook.

D. Use `dbutils.notebook.run` and pass parameters via the notebook path string.

---

# Answer

✅ **A. Use `dbutils.notebook.run` and pass a dictionary to the arguments parameter.**

## Explanation

`dbutils.notebook.run()`:

- Executes notebook in isolated scope
- Supports parameter passing
- Avoids variable collisions
- Returns execution result

`%run` shares the same execution context.

---

# Question 24 — Email Masking in Unity Catalog

A team needs to expose a customer table to analysts but mask the email column for everyone outside the `pii_admins` group.

Which approach is the most appropriate in Unity Catalog?

## Options

A. Duplicate the table and remove the email column from the copy.

B. Create a view that uses `is_account_group_member('pii_admins')` to conditionally return the real email or a masked value.

C. Encrypt the email column at the storage layer.

D. Remove `SELECT` on the table for everyone.

---

# Answer

✅ **B. Create a view that uses `is_account_group_member('pii_admins')` to conditionally return the real email or a masked value.**

## Explanation

Dynamic masking using views and group membership checks is a common Unity Catalog access-control pattern.

Example:

```sql
CASE
  WHEN is_account_group_member('pii_admins')
  THEN email
  ELSE '****'
END
```
