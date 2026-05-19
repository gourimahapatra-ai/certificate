### A large table in Snowflake may contain millions or hundreds of millions of micro-partitions.

The number of micro-partitions for a given table depends mainly on the amount of data in that table. For a very large table, the number of micro-partitions can run into millions or hundreds of millions of micro-partitions. https://docs.snowflake.com/en/user-guide/tables-clustering-micropartitions


Snowflake has been designed for the cloud and has been designed from scratch. Snowflake implements a new hybrid architecture that decouples compute and storage.


### Snowflake stores which of the following metadata about data in a micro-partition. Select all that apply.

All of these are valid examples of the metadata that Snowflake stores for micro-partition. Snowflake stores the range of column values in its metadata: the maximum and the minimum value for each column in each micro-partition. Snowflake can intelligently decide which partitions to read when processing a query using this metadata. Additionally, Snowflake stores the count of distinct values for each column in each partition in the metadata and certain other information to assist in query optimization. https://docs.snowflake.com/en/user-guide/tables-clustering-micropartitions


The cloud services layer manages authentication and authorization. When a user logs in, the cloud services layer validates their credentials. When a user submits a query, the cloud services layer parses and optimizes the query plan. https://docs.snowflake.com/en/user-guide/intro-key-concepts




### Snowflake stores data in a proprietary format on cloud object storage, such as AWS S3, Azure Blob Storage, or Google Cloud Storage. Users cannot see the actual files, or look at how the data is stored, or access the file directly.


### Consider the CUSTOMER table in the SNOWFLAKE_SAMPLE_DATA.TPCH_SF1 schema. Your virtual warehouse is in a suspended state but is set to auto-resume. Which of the following queries will result in the virtual warehouse being resumed? Select all that apply.

Metadata cache or cloud services operations do not require an active virtual warehouse. Other queries will need an active virtual warehouse.
Statistics are kept in the metadata cache in the cloud services layer for each table, micro-partition, and column. The metadata cache can return results if the query simply counts the number of rows.
Similarly, the cloud services layer can provide table definitions (i.e., DESCRIBE) and a list of tables in a schema (i.e., SHOW TABLES LIKE).



### Multi-cluster virtual warehouses are utilized when the number of concurrent users exceeds a single virtual warehouse's capacity. When the concurrent workload for a virtual warehouse reaches the maximum, new queries are queued. Multi-cluster virtual warehouses address this by adding clusters as needed. When the demand drops, the extra clusters are removed. Enterprise edition is required to use the multi-cluster virtual warehouse feature. Besides the automatic addition and removal of compute clusters, multi-cluster virtual warehouses behave the same as typical virtual warehouses so that they can be suspended or resumed and auto-suspended or auto-resumed. 
https://docs.snowflake.com/en/user-guide/warehouses-multicluster


### Which of the following statement describe micro-partitions correctly?


Snowflake partitions are immutable, which means they cannot be changed once created. Table data is mapped to individual micro-partitions and is further organized using a columnar format. 

https://docs.snowflake.com/en/user-guide/tables-clustering-micropartitions.html

### The cloud services layer in Snowflake provides which of the following functions? Select all that apply.
- Data Sharing
- Cloning
- Transaction control / ACID compliance

Snowflake's data sharing, cloning, and data exchange features are all managed through the cloud services layer using metadata. The cloud services layer also provides ACID compliance. ACID means a database system must allow several transactions to run in isolation and commit or roll back a transaction as a unit, assuring system consistency.