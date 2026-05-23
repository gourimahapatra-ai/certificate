# External Tables in Databases

## 1. Definition of External Tables
- External tables reference data stored outside the database-managed storage.
- The database stores only metadata, while the data resides in external locations.
- Commonly used with cloud storage systems such as ADLS, S3, or GCS.

## 2. Benefits of Using External Tables
- Provide full control over data storage locations.
- Enable easy data sharing across multiple systems or platforms.
- Support separation of compute and storage for cost efficiency.
- Allow direct access to raw or semi‑processed data without ingestion.

## 3. Creating External Tables in Databricks
- Defined by specifying an explicit storage path.
- Databricks stores metadata in the metastore but leaves data in external storage.
- Useful for scenarios requiring custom directory structures or cross‑workspace access.

## 4. Accessing External Data Seamlessly
- External tables behave like regular tables for querying and transformations.
- Support Delta Lake features such as ACID transactions (when using Delta format).
- Enable smooth integration with SQL, DataFrames, and BI tools.

## 5. Use Cases for External Tables
- Sharing data across multiple Databricks workspaces or cloud services.
- Managing large datasets stored in cloud object storage.
- Maintaining raw or intermediate datasets outside managed storage.
- Supporting hybrid architectures where storage is decoupled from compute.

## 6. Summary
External tables provide flexibility by storing data outside the database-managed environment while maintaining full query capabilities. They are ideal for shared storage, large-scale datasets, and architectures requiring separation of compute and storage.
