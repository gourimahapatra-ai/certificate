### Which of the following scenario requires you to have replication configured to recover?

If a cloud provider or a region goes down, Snowflake users may be affected. To ensure the least impact, you must be ready for cloud provider outages to keep Snowflake available to your users.


Snowflake account-level replication & database replication synchronizes critical account objects and data from the primary account to one or more secondary accounts in a different region or cloud platform. Database replication allows read-only copies of databases from a primary Snowflake account to a new region or cloud provider. In the event of a failure on the primary site, switch your workloads from the primary to one of the secondary locations.


https://docs.snowflake.com/en/user-guide/account-replication-intro


### Streams 
Snowflake Streams help you keep track of any changes made to a table, such as new data being added (inserts), existing data being modified (updates), or data being removed (deletes). They allow you to query and process only the changed data since the last offset.
See the link for more details: https://docs.snowflake.com/en/user-guide/streams-intro


Streams do not support materialized view currently.


### streams : 
Snowflake Streams help you keep track of any changes made to a table, such as new data being added (inserts), existing data being modified (updates), or data being removed (deletes). They allow you to query and process only the changed data since the last offset. See the link for more details: https://docs.snowflake.com/en/user-guide/streams-intro



### Which of the following is true regarding Directory Tables?

Streams can be used with directory tables.
To use a stream with a directory table, you must create the stream on the stage object.

