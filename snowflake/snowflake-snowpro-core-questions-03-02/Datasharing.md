Virtual Private Snowflake (VPS) cannot use secure data sharing, Marketplace, etc., because VPS accounts have isolated metadata, compute, and storage and therefore don't have sharing capabilities.


Only users with ACCOUNTADMIN roles or with CREATE SHARE permission can create a share. https://docs.snowflake.com/en/user-guide/data-sharing-gs


### Which of the following correctly describes a reader account in Snowflake?
### A reader account can be used to share data with non-Snowflake users.
Sharing data with a non-Snowflake user or organization is possible by creating a reader account. This reader account is created by the data provider solely for sharing purposes. 

https://docs.snowflake.com/en/user-guide/data-sharing-reader-create


### Through Snowflake sharing, a data provider can share data with which of the following? Select all that apply.

You can share data with multiple consumers: Snowflake customers, non-Snowflake customers, or a mix of both.


# When data is shared between Snowflake accounts, what type of database is created on the consumer side for consuming the shared data?

The correct answer is read-only. The consumer creates a database from the Share object as a read-only database. 
https://docs.snowflake.com/en/user-guide/data-sharing-intro#how-does-secure-data-sharing-work

