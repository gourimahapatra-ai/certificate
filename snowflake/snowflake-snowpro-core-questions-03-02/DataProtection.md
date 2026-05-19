### Which of the following scenario requires you to have replication configured to recover?

If a cloud provider or a region goes down, Snowflake users may be affected. To ensure the least impact, you must be ready for cloud provider outages to keep Snowflake available to your users.


Snowflake account-level replication & database replication synchronizes critical account objects and data from the primary account to one or more secondary accounts in a different region or cloud platform. Database replication allows read-only copies of databases from a primary Snowflake account to a new region or cloud provider. In the event of a failure on the primary site, switch your workloads from the primary to one of the secondary locations.


https://docs.snowflake.com/en/user-guide/account-replication-intro


### Transient Table

Based on the requirement, a transient table is a good choice. Transient tables don't have fail-safe storage and have only up to 1 day of Time Travel. A transient table provides a good solution because the data is deleted and reloaded daily in this scenario. Transient tables are also the best option because data must be available across different sessions. Transient tables are available across sessions; independent processes and sessions can access the data in a Transient table.


https://docs.snowflake.com/en/user-guide/tables-temp-transient

Which function can be used within a Row Access Policy to determine the user executing the query?
### CURRENT_USER()
The CURRENT_USER() function returns the name of the user executing the query, allowing Row Access Policies to be defined based on the user accessing the data.

### CURRENT_ROLE()
While CURRENT_ROLE() returns the role of the user, it is often combined with CURRENT_USER() for more granular control.

### CURRENT_TIME()
CURRENT_TIME() provides the current time, unrelated to the user's identity.

### CURRENT_DATE()
CURRENT_DATE() provides the current date but is not relevant for determining the user

### How are Row Access Policies applied to a table in Snowflake?
Through the ALTER TABLE command

Explanation
Row Access Policies are applied using the ALTER TABLE command on specific columns. This associates the policy with the column, ensuring it filters data based on the defined rules.


### What happens when a key rotation occurs in Snowflake?
New data loaded after rotation uses a new encryption key

Explanation
In Snowflake, when a key rotation occurs, any new data loaded after the rotation uses the new encryption key. Existing data remains encrypted with the old keys until a full rekeying is manually triggered.


### Which of the following views should you query to get detailed information about the amount of storage used by time travel and failsafe in Snowflake?
ACCOUNT_USAGE.TABLE_STORAGE_METRICS

Explanation
This view provides detailed information about table storage, including the breakdown into active bytes, time travel bytes, and failsafe bytes.