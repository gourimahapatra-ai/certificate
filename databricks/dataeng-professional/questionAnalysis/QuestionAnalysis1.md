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
# QUESTION 19 / 59 — S9: DEBUGGING AND DEPLOYING

An engineer has finished updating a Lakeflow Declarative Pipeline defined in a bundle. They want to upload the updated code and metadata to the production workspace without immediately triggering a run. Which command should they use?

- A. `databricks bundle deploy -t prod`
- B. `databricks job create --bundle prod`
- C. `databricks bundle validate -t prod`
- D. `databricks bundle run -t prod`

---

# QUESTION 20 / 59 — S4: DATA SHARING AND FEDERATION

A large enterprise needs to share various datasets with numerous internal departments and several external partners. Some internal departments are on Databricks, others use custom Spark clusters. External partners use a mix of Databricks and non-Databricks platforms.

The enterprise prioritizes simplifying recipient management and ensuring consistent access policies across all shared data. What is the most effective strategy for managing these diverse recipients and data access?

- A. Export all data to a common cloud storage location and share direct storage access links.
- B. Migrate all recipients to Databricks to standardize on Databricks-to-Databricks sharing.
- C. Utilize Unity Catalog's recipient management features to create recipients, assign them to shares, and leverage the appropriate Delta Sharing protocol (D2D or open) based on their platform.
- D. Create a separate Delta Sharing share for each recipient and manually manage credentials.

---

# QUESTION 21 / 59 — S4: DATA SHARING AND FEDERATION

A data engineering team frequently updates a set of curated Delta tables containing financial transaction data. A downstream analytics team requires access to the absolute latest version of this data, without any delays due to data copying or ETL processes.

The analytics team operates in a separate Databricks workspace within the same organization. How can the engineering team provide this real-time, live data access?

- A. By granting the analytics team direct read access to the underlying cloud storage location of the Delta tables.
- B. By using Lakeflow Spark Declarative Pipelines to continuously replicate data between the workspaces.
- C. By using Databricks-to-Databricks Delta Sharing to share the live Delta tables from Unity Catalog.
- D. By setting up a scheduled ETL job to copy the Delta tables to the analytics team's workspace hourly.

---

# QUESTION 22 / 59 — S10: DATA MODELLING

A team is building a dimension table and requires a strictly monotonic surrogate key that cannot be manually overridden by insert statements. Which syntax should the engineer use when defining the ID column?

- A. `GENERATED BY DEFAULT AS IDENTITY`
- B. `GENERATED ALWAYS AS IDENTITY`
- C. `SEQUENCE START WITH 1`
- D. `AUTO_INCREMENT PRIMARY KEY`

---

# QUESTION 23 / 59 — S9: DEBUGGING AND DEPLOYING

An engineer wants to execute a child notebook from a parent notebook and pass specific configuration values as parameters. The child notebook should run in its own scope to avoid variable name collisions. Which approach should they use?

- A. Use `dbutils.notebook.run` and pass a dictionary to the `arguments` parameter.
- B. Use `%run` and rely on global environment variables to share data.
- C. Use `%run` which automatically creates a new job run for the target notebook.
- D. Use `dbutils.notebook.run` and pass parameters via the notebook path string.

---

# QUESTION 24 / 59 — S4: DATA SHARING AND FEDERATION

A team needs to expose a customer table to analysts but mask the email column for everyone outside the `pii_admins` group. Which approach is the most appropriate in Unity Catalog?

- A. Duplicate the table and remove the email column from the copy.
- B. Create a view that uses `is_account_group_member('pii_admins')` to conditionally return the real email or a masked value.
- C. Encrypt the email column at the storage layer.
- D. Remove `SELECT` on the table for everyone.

---

# QUESTION 25 / 59 — S9: DEBUGGING AND DEPLOYING

A team shares a massive monorepo containing hundreds of projects, but a specific data engineering squad only needs to work on one subdirectory within Databricks. Which feature should they use to clone only that specific directory into their Databricks Repo?

- A. Selective Branching
- B. Sparse Checkout
- C. Shallow Clone
- D. Git Submodules

---

# QUESTION 26 / 59 — S7: STREAMING AND INGESTION

A data engineer is processing millions of files arriving daily in an S3 bucket. Using directory listing is becoming slow and expensive. Which Auto Loader configuration should they use to optimize file discovery?

- A. Directory listing mode with `cloudFiles.useNotifications` set to `false`
- B. Standard micro-batching without any `cloudFiles` configurations
- C. Snapshot mode to process all files in each trigger interval
- D. File notification mode using a cloud queue service and notifications

---

# QUESTION 27 / 59 — S7: STREAMING AND INGESTION

A data engineer joins a high-volume stream of transactions with a static Delta table containing user account metadata. Which behavior should they expect regarding how the static data is used?

- A. The join will automatically wait for the static table to be updated before processing new stream data.
- B. The join is performed against the version of the static table available at the time the query started.
- C. The static table must be converted to a stream to allow for any join operation.
- D. Spark requires a watermark on the static table to manage the state.

---

# QUESTION 28 / 59 — S5: DELTA LAKE

A Delta table is defined with a `NOT NULL` constraint on the `email` column. What happens when a batch job attempts to append a dataframe containing null values in the `email` field?

- A. The problematic rows are redirected to a quarantine table.
- B. The write transaction fails and an error is raised immediately.
- C. The data is written but the null values are replaced with empty strings.
- D. The write succeeds but a warning is logged in the driver logs.

---

# QUESTION 29 / 59 — S7: STREAMING AND INGESTION

An engineer configures Auto Loader with schema evolution mode set to `rescue`. A source file arrives containing a new field that was not present in the original schema. What happens to the data in this new field?

- A. The extra data is written to a hidden `_rescued_data` column.
- B. The new column is added to the Delta table and the stream continues.
- C. The new column is ignored and the data in that field is dropped.
- D. The pipeline fails immediately to prevent data corruption.

---

# QUESTION 30 / 59 — S5: DELTA LAKE

A Silver table needs to be updated from a Change Data Capture feed that contains inserts, updates, and deletes keyed by `customer_id`. Which Delta operation is the most appropriate single statement?

- A. Append the source as-is and rely on a downstream view to deduplicate.
- B. `MERGE INTO target USING source ON target.customer_id = source.customer_id WHEN MATCHED ... WHEN NOT MATCHED ...`
- C. Drop and recreate the table each batch.
- D. `INSERT OVERWRITE` the entire table on every batch.

---

# QUESTION 31 / 59 — S7: STREAMING AND INGESTION

A streaming pipeline is experiencing unstable performance and frequent OOM failures because the volume of incoming data in the cloud storage bucket fluctuates significantly. The engineer needs to implement backpressure to ensure the cluster is not overwhelmed during peak periods. Which configuration should be adjusted?

- A. Decrease the shuffle partition count to reduce overhead.
- B. Switch to a `Trigger.AvailableNow` configuration.
- C. Increase the number of worker nodes to match the volume.
- D. Set the `maxBytesPerTrigger` option to limit the data processed per batch.

---

# QUESTION 32 / 59 — S9: DEBUGGING AND DEPLOYING

An engineer has completed the development of a bundle and wants to push the local configuration to a production workspace. Which command should they use to validate and upload the bundle resources?

- A. `databricks bundles upload --target prod`
- B. `databricks bundle deploy --target prod`
- C. `databricks fs cp ./bundle dbfs:/bundles/prod`
- D. `databricks jobs create-bundle --path .`

---

# QUESTION 33 / 59 — S9: DEBUGGING AND DEPLOYING

A data engineering team is using Databricks Asset Bundles to manage a pipeline. They need to deploy the same code to both a development workspace and a production workspace with different cluster IDs. How should they structure their `databricks.yml` file?

- A. Create a different bundle for every environment to ensure resources never overlap.
- B. Use the `targets` mapping to override the `workspace` host and resource IDs for each environment.
- C. Define separate `databricks.yml` files in different folders for each environment.
- D. Hardcode the resource IDs in the main resources block and use a bash script to find and replace them.

---

# QUESTION 34 / 59 — S8: SECURITY AND GOVERNANCE

A security administrator notices that an unauthorized user recently gained access to a restricted production catalog. Which system table should be queried to identify who granted these permissions?

- A. Query `system.access.group_members` to see who was recently added to the admin group.
- B. Search the `system.access.audit` table for events where `action_name` is set to `updatePermissions`.
- C. Use the `system.billing.usage` table to find users with increased execution privileges.
- D. Review the `system.compute.clusters` table to see who reconfigured the cluster settings.

---

# QUESTION 35 / 59 — S9: DEBUGGING AND DEPLOYING

A data engineer needs to automate unit tests for a Python transformation function using pytest. What is the recommended way to structure the test to ensure it runs in a CI/CD environment without a live workspace connection?

- A. Pass a locally created SparkSession and sample DataFrame to the function.
- B. Use a `dbutils.secrets` utility to fetch production data samples.
- C. Write the logic as a SQL query and use a temporary view in a shared cluster.
- D. Apply the logic directly to a global Spark context in a notebook cell.

---

# QUESTION 36 / 59 — S8: SECURITY AND GOVERNANCE

Which command grants a group read access to all current and future tables in the schema `main.silver`?

- A. `GRANT SELECT ON SCHEMA main.silver TO \`data_analysts\``
- B. `GRANT SELECT ON CATALOG main TO \`data_analysts\``
- C. `USE SCHEMA main.silver`
- D. `GRANT ALL PRIVILEGES ON TABLE main.silver TO \`data_analysts\``

---

# QUESTION 37 / 59 — S6: LAKEFLOW DECLARATIVE PIPELINES

A data engineer wants to use Materialized Views within Lakeflow Declarative Pipelines to optimize a dashboard. How do Materialized Views differ from standard views in this context?

- A. Materialized views do not store data and act exactly like standard SQL views, spinning up clusters on demand.
- B. Materialized views prioritize query performance by pre-computing and storing the results of complex logic.
- C. Materialized views are used only for streaming sources and do not support batch inputs.
- D. Materialized views must be refreshed manually by an external Spark job outside the pipeline.

---

# QUESTION 38 / 59 — S10: DATA MODELLING

A data engineer needs to track the history of customer address changes so that the business can report on sales based on where a customer lived at the time of purchase. Which Slowly Changing Dimension (SCD) type should be implemented?

- A. SCD Type 2 because it ensures that only the most recent record exists in the table.
- B. SCD Type 2 because it tracks changes over time using effective date ranges.
- C. SCD Type 1 because it creates a new record for every attribute change.
- D. SCD Type 1 because it simplifies auditing by overwriting old values.

---

# QUESTION 39 / 59 — S7: STREAMING AND INGESTION

A data engineer notices that their streaming Job occasionally hangs because a source folder receives 50,000 files at once. They want to limit each micro-batch to only process 1,000 files at a time. Which option should they configure?

- A. `cloudFiles.maxBytesPerTrigger`
- B. `cloudFiles.fetchParallelism`
- C. `cloudFiles.maxFilesPerTrigger`
- D. `spark.sql.files.maxPartitionBytes`

---

# QUESTION 40 / 59 — S4: DATA SHARING AND FEDERATION

A data engineering team wants to share a sensitive Delta table containing PII with an analytics team for reporting purposes. Both teams operate within the same Azure Databricks workspace and use Unity Catalog.

The sharing must adhere to strict access controls, allowing the analytics team only read access to specific columns and rows, and audited for compliance. How should the engineering team manage this data sharing within Unity Catalog?

- A. Create a Delta Sharing share and invite the analytics team as a recipient.
- B. Create a new external table in a separate Unity Catalog schema for the analytics team.
- C. Export the data to a new Delta table with PII masked and grant access to that new table.
- D. Grant direct `SELECT` privileges on the table to the analytics team's user group within Unity Catalog, then apply row and column filters.

---

# QUESTION 41 / 59 — S7: STREAMING AND INGESTION

A data engineer needs to ensure that a streaming pipeline can recover from a cluster failure without skipping or duplicating data records. What is the primary requirement for achieving this recovery behavior?

- A. Providing a unique directory for the `checkpointLocation` option when starting the stream.
- B. Setting the `spark.sql.streaming.exactlyOnce` configuration to true in the cluster settings.
- C. Configuring a high trigger interval via `Trigger.ProcessingTime` to allow disk flushing.
- D. Using a Delta table as the source and setting the `maxFilesPerTrigger` option to 1.

---

# QUESTION 42 / 59 — S9: DEBUGGING AND DEPLOYING

An engineer is designing an integration test for a pipeline that writes to Delta tables. How should they manage the mock data and environment to ensure the test is reliable and isolated?

- A. Manually inspect the Delta logs after running a job in the staging environment.
- B. Mock the Delta Lake file system entirely so no files are written during the test.
- C. Perform the test using small data samples in a temporary schema or catalog.
- D. Run the test against a subset of production data in the gold layer.

---

# QUESTION 43 / 59 — S10: DATA MODELLING

A data engineering team is designing a Medallion architecture. They need a layer where raw data is cleaned, joined, and normalized to provide a single source of truth for downstream analytics. In which layer should this logic reside?

- A. Landing zone layer
- B. Bronze layer
- C. Gold layer
- D. Silver layer

---

# QUESTION 44 / 59 — S9: DEBUGGING AND DEPLOYING

A pipeline requires a specific Linux-level security library to be installed on the OS of every cluster node before any Spark code runs. What is the most reliable way to automate this installation for a specific job cluster?

- A. Add the library to the `Global Init Scripts` section in the Admin Console.
- B. Include a `%pip install` command in the first cell of every notebook in the pipeline.
- C. Upload the package as a Workspace Library and attach it to the SQL Warehouse.
- D. Use a cluster-scoped init script to run `apt-get` commands during cluster creation.

---

# QUESTION 45 / 59 — S9: DEBUGGING AND DEPLOYING

A developer prefers using VS Code for writing PySpark transformations but wants to leverage the compute power of an existing Databricks cluster. Which tool should they use?

- A. It automatically copies all infrastructure as code (Terraform) scripts to the workspace.
- B. It enables executing Spark code from a local IDE while using remote Databricks compute.
- C. It allows users to run Databricks Spark jobs offline without an internet connection.
- D. It replaces the need for the Databricks CLI when deploying workspace files.

---

# QUESTION 46 / 59 — S7: STREAMING AND INGESTION

An Auto Loader stream ingests millions of small files daily from a cloud bucket and the directory listing step is becoming a bottleneck. Which configuration most directly addresses this?

- A. Increase `spark.sql.shuffle.partitions` to 4000.
- B. Switch `cloudFiles.useNotifications` to `true` so Auto Loader uses the cloud's file notification service.
- C. Run the stream on serverless model serving.
- D. Disable schema inference.

---

# QUESTION 47 / 59 — S7: STREAMING AND INGESTION

A pipeline performs a stream-static join to enrich real-time sensor data with store metadata from a Delta table. The store metadata is updated once per day, but the streaming query does not reflect these updates. What is the standard behavior in this scenario?

- A. The join must be performed using a LEFT JOIN to ensure the stream keeps moving.
- B. The engineer must enable `spark.databricks.delta.staticSideAutoRefresh`.
- C. The static table must be converted to a cached RDD to allow lookups.
- D. The streaming query must be restarted to pick up the new data in the static table.

---

# QUESTION 48 / 59 — S9: DEBUGGING AND DEPLOYING

Which file is the entry point for a Databricks Asset Bundle that defines jobs, pipelines, and deployment targets such as `dev` and `prod`?

- A. `pyproject.toml`
- B. `databricks.yml`
- C. `workflow.json`
- D. `requirements.txt`

---

# QUESTION 49 / 59 — S8: SECURITY AND GOVERNANCE

A security administrator wants to grant a group of data analysts read-only access to every table within a specific catalog named `analytics`. What is the most efficient way to achieve this using Unity Catalog SQL syntax?

- A. `GRANT SELECT ON ALL TABLES IN CATALOG analytics TO \`data-analysts\``
- B. `GRANT READ ON CATALOG analytics TO \`data-analysts\``
- C. `GRANT USAGE ON CATALOG analytics TO \`data-analysts\``
- D. `GRANT USE CATALOG, USE SCHEMA, SELECT ON CATALOG analytics TO \`data-analysts\``

---

# QUESTION 50 / 59 — S10: DATA MODELLING

A data engineer is designing a dimension table and needs to automatically generate a unique, auto-incrementing surrogate key for every new record. Which Delta Lake feature is best suited for this requirement?

- A. `CREATE TABLE ... (id BIGINT GENERATED ALWAYS AS IDENTITY)`
- B. `CREATE TABLE ... (id BIGINT DEFAULT NEXT VALUE FOR sequence)`
- C. `CREATE TABLE ... (id BIGINT PRIMARY KEY AUTO_INCREMENT)`
- D. `CREATE TABLE ... (id BIGINT GENERATED ALWAYS AS (UUID()))`

---

# QUESTION 51 / 59 — S9: DEBUGGING AND DEPLOYING

A production job requires a custom C++ library to be available on all cluster nodes at the system level and several environment variables to be set before the Spark engine initializes. What is the most reliable way to achieve this?

- A. Install the libraries using `%pip install` in the first cell of every notebook.
- B. Use a cluster-scoped init script to configure the environment and dependencies.
- C. Add the environment variables to the cluster Spark config using the UI.
- D. Define the variables in a Workspace Secret and hope the Spark process finds them.

---

# QUESTION 52 / 59 — S8: SECURITY AND GOVERNANCE

An organization needs to connect a third party BI tool to Databricks SQL. They require a secure authentication method that does not rely on long lived personal secrets and supports scoped access. Which method should they choose?

- A. Configure OAuth tokens to allow the BI tool to authenticate on behalf of the user.
- B. Use basic authentication with the user email and workspace password.
- C. Generate a Personal Access Token (PAT) for the user and hardcode it in the BI tool.
- D. Create a service principal and share the client secret with the BI tool users.

---

# QUESTION 53 / 59 — S10: DATA MODELLING

A growing Delta table is queried mostly by `customer_id` and `event_date`. The team wants strong file skipping without committing to a rigid partition layout. Which Delta feature is the recommended modern choice?

- A. Hive-style partitioning on `event_date` only.
- B. Bucketing on `customer_id` with 200 buckets.
- C. Liquid Clustering on (`customer_id`, `event_date`).
- D. Hash partitioning on `customer_id`.

---

# QUESTION 54 / 59 — S10: DATA MODELLING

A team is partitioning a large table by month, derived from a timestamp column. They want to ensure that queries filtering on the timestamp column still benefit from partition pruning. How should this be implemented in Delta Lake?

- A. Manually calculate the month in the ingestion spark code and store it as a standard string.
- B. Use a Z-Order index on the `event_timestamp` instead of partitioning.
- C. Create a generated column for the month and use it as a partition key.
- D. Apply a manual cast to the date column in every `SELECT` statement.

---

# QUESTION 55 / 59 — S7: STREAMING AND INGESTION

A web application tracks user activity. The data engineer needs to group events into windows based on the duration of a user's visit, where a visit ends if the user is inactive for more than 30 minutes. Which windowing strategy is best suited for this task?

- A. Tumbling windows with a fixed five-minute duration.
- B. Global windows with a custom stateful trigger.
- C. Session windows with a specified timeout gap.
- D. Sliding windows with a ten-minute duration and five-minute slide.

---

# QUESTION 56 / 59 — S7: STREAMING AND INGESTION

A data engineer is building a sessionization pipeline where they need to maintain state for user interactions. The state for a specific user ID must be cleared if no new events are received for 30 minutes. Which approach should be used?

- A. Use `mapInPandas` and filter the resulting DataFrame using a `current_timestamp()` join.
- B. Use `applyInPandas` and implement a global timer dictionary to track key inactivity.
- C. Use `applyInPandasWithState` and set the output mode to Complete to see all active states.
- D. Use `applyInPandasWithState` and define a `GroupStateTimeout.ProcessingTimeTimeout` logic.

---

# QUESTION 57 / 59 — S9: DEBUGGING AND DEPLOYING

A data engineer needs to configure a Databricks Asset Bundle so that it deploys to a specific workspace URL and uses a `small` cluster tag only when the development environment is targeted. Which structure should they use in the `databricks.yml` file?

- A. Use the `targets` mapping in `databricks.yml` to override variables and workspace settings for `dev`.
- B. Define separate `databricks.yml` files for each environment in the project root.
- C. Create a `variables` block at the root level and manually edit them before each deploy.
- D. Use a `stages` block to define different workspace URLs for each deployment tier.

---

# QUESTION 58 / 59 — S5: DELTA LAKE

An engineer drops two tables in Unity Catalog: one is a managed table and the other is an external table. What happens to the underlying data files in cloud storage for these two tables?

- A. Both tables keep their data files but lose their metadata definitions.
- B. Both tables and their underlying data files are permanently deleted.
- C. The managed table data is deleted, but the external table data remains.
- D. The external table data is deleted, but the managed table data remains.

---

# QUESTION 59 / 59 — S10: DATA MODELLING

Which combination of columns is typical of an SCD Type 2 dimension table?

- A. Only the natural key and the latest attribute values.
- B. The natural key and a `change_type` column with values `insert` or `delete`.
- C. Only `valid_from` and `valid_to`, no attribute columns.
- D. A surrogate key, the natural key, the attribute columns, and `valid_from` / `valid_to` (or `is_current`) columns.

Question 19: A  
Question 20: C  
Question 21: C  
Question 22: B  
Question 23: A  
Question 24: B  
Question 25: B  
Question 26: D  
Question 27: B  
Question 28: B  
Question 29: A  
Question 30: B  
Question 31: D  
Question 32: B  
Question 33: B  
Question 34: B  
Question 35: A  
Question 36: A  
Question 37: B  
Question 38: B  
Question 39: C  
Question 40: D  
Question 41: A  
Question 42: C  
Question 43: D  
Question 44: D  
Question 45: B  
Question 46: B  
Question 47: D  
Question 48: B  
Question 49: A  
Question 50: A  
Question 51: B  
Question 52: A  
Question 53: C  
Question 54: C  
Question 55: C  
Question 56: D  
Question 57: A  
Question 58: C  
Question 59: D  