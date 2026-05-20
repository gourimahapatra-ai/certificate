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


### Snowflake customers can control the format using which Snowflake stores the data for a table.

Snowflake stores data in a proprietary format on cloud object storage, such as AWS S3, Azure Blob Storage, or Google Cloud Storage. Users cannot see the actual files, look at how the data is stored, or access the file directly. Users can not change how Snowflake stores the data behind the scenes.


### Which of the following statement is true regarding the Query Processing Layer?

The query processing layer is the compute layer through which queries and data processing jobs are executed on the stored data. The compute layer can have multiple clusters for a given Snowflake instance simultaneously. The compute engines in Snowflake are known as virtual warehouses. The cloud services layer performs the query plans and optimization. 

### The query processing layer is responsible for executing queries.
### The query processing layer can run multiple compute clusters (virtual warehouses) simultaneously.


https://docs.snowflake.com/en/user-guide/intro-key-concepts

### Snowflake database is based on the massively parallel shared nothing architecture used by databases like Teradata and Greenplum and data lakes like Hadoop.

Snowflake implements a new hybrid architecture that combines the best features of shared-disk and shared-nothing architectures. Snowflake stores data similarly to a shared-disk architecture, i.e., the data is shared. But it also allows for using several compute engines, each with its own memory and processing capabilities. https://docs.snowflake.com/en/user-guide/intro-key-concepts#snowflake-architecture


### Which of the following is a feature available in the Business Critical Edition but not in the Enterprise Edition?

Customer-Managed Encryption

The Business Critical Edition includes advanced security features such as customer-managed encryption, which is not available in the Enterprise Edition.


### What is a key difference between the Snowflake ACCOUNT_USAGE schema and INFORMATION_SCHEMA schema regarding dropped objects?

ACCOUNT_USAGE schema includes information on dropped objects, while INFORMATION_SCHEMA does not.

The ACCOUNT_USAGE schema contains information on dropped objects, with specific columns indicating whether an object is active or has been deleted. In contrast, the INFORMATION_SCHEMA does not track dropped objects.


### Which of the following statements about Snowflake Time Travel and Fail-safe is correct?
Time Travel is available for querying and restoring data using SQL commands like SELECT ... AT/BEFORE and UNDROP, while Fail-safe is a disaster recovery feature accessible only by Snowflake Support and incurs additional storage costs.

Explanation
This accurately describes both features:

Time Travel: User-accessible feature that allows querying historical data (AT or BEFORE clauses) and recovering dropped objects (UNDROP TABLE/SCHEMA/DATABASE). Retention period is configurable (0-1 days for Standard Edition, 0-90 days for Enterprise Edition and higher).

Fail-safe: A 7-day disaster recovery period that automatically follows the Time Travel period. It is NOT accessible by users through SQL queries - only Snowflake Support can recover data from Fail-safe upon request. Both Time Travel and Fail-safe data incur storage costs.

### In Snowflake, each account is associated with a specific cloud provider and region, and cannot span across multiple regions within the same organization.

True

Explanation
In Snowflake, each account is tied to a specific cloud provider (like AWS, Azure, or GCP) and a particular region within that provider. A single Snowflake account does not span multiple regions. For organizations requiring access to multiple regions, they need to set up separate accounts for each region.


### Which of the following statements about the database storage layer in Snowflake is true?
It stores data using a hybrid columnar storage format.

Explanation
Snowflake’s storage layer uses a hybrid columnar storage format, which is optimized for analytical workloads. It stores data in compressed "blobs" managed by the cloud provider (e.g., AWS S3 or Azure containers) for efficiency and performance.

### What is a primary benefit of using Snowflake external functions?
They allow access to external services and third-party libraries

Explanation
Snowflake external functions allow integration with external services, such as AWS Lambda or Azure Functions, enabling users to leverage third-party libraries and services that aren't available within Snowflake itself.

### Which of the following statements is true about the storage layer in Snowflake’s architecture?
It compresses data into blobs stored on external cloud providers.

Explanation
Snowflake’s database storage layer compresses data into blobs and stores them on external cloud providers like AWS or Azure. This architecture supports efficient data retrieval and storage management.


### In Snowflake, databases and schemas are the only objects that can be created within an account.
False

Explanation
This statement is false. Snowflake supports multiple types of objects within an account, including databases, schemas, roles, users, virtual warehouses, resource monitors, and other database objects such as tables, views, functions, stages, tasks, streams, and pipes.\

### Which of the following statements about Snowflake's "table storage metrics" views is true?
They are available in both the Information Schema and Account Usage Schema.

Explanation
The "table storage metrics" views are available in both the Information Schema and the Account Usage Schema, offering detailed table storage information including active bytes, time travel, and failsafe data.

### What type of architecture does Snowflake use?
Multi-cluster Shared Data Architecture

Explanation
Snowflake uses a Multi-cluster Shared Data Architecture, which combines the benefits of both shared disk and shared nothing architectures. It features a central data repository for simplicity and multiple compute clusters for scalability and performance.