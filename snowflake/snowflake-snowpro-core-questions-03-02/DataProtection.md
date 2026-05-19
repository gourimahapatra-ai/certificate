### Which of the following scenario requires you to have replication configured to recover?

If a cloud provider or a region goes down, Snowflake users may be affected. To ensure the least impact, you must be ready for cloud provider outages to keep Snowflake available to your users.


Snowflake account-level replication & database replication synchronizes critical account objects and data from the primary account to one or more secondary accounts in a different region or cloud platform. Database replication allows read-only copies of databases from a primary Snowflake account to a new region or cloud provider. In the event of a failure on the primary site, switch your workloads from the primary to one of the secondary locations.


https://docs.snowflake.com/en/user-guide/account-replication-intro