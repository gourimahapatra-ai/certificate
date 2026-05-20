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

### Which command is used to create a row access policy in Snowflake? CREATE ROW ACCESS POLICY
The correct command to create a row access policy in Snowflake is CREATE ROW ACCESS POLICY. This command is used to define a schema-level object that specifies the conditions under which rows should be visible based on user or role information.


### What action should a user take to recover a dropped table using Snowflake's Time Travel if a new table with the same name has already been created?
Rename the new table before attempting to recover the old one

This is the correct approach. If a new table with the same name exists, Snowflake will not allow the recovery of the dropped table with the same name. The user must first rename or drop the current table to free up the name for restoration.


### Which of the following is true about data encryption in Snowflake? (Choose two)
TLS 1.2 is used for encrypting data in transit.
TLS 1.2 is used for encrypting data in transit: This is also correct. Snowflake ensures that all data in transit is encrypted using TLS 1.2, providing secure communication between clients and Snowflake.

Snowflake uses AES-256 encryption for data at rest.
Snowflake uses AES-256 encryption for data at rest: This is true. Snowflake automatically encrypts all data at rest using AES-256, which is a strong and industry-standard encryption algorithm.

### Which of the following statements about column-level security features in Snowflake is correct?
Dynamic Data Masking applies only at query runtime based on the role of the user executing the query.

Dynamic Data Masking in Snowflake occurs at query runtime and depends on the role of the user running the query, ensuring that only authorized users can view sensitive data.

# Row Access Policies in Snowflake — Correct Statements (Choose TWO)

## ✅ Correct Statements

### **1. Row Access Policies are schema‑level objects that dynamically filter rows at query time.**
A Row Access Policy (RAP) is created in a **schema** and attached to one or more tables or views.  
Snowflake evaluates the policy **every time a query runs**, ensuring users only see rows they are authorized to see.

---

### **2. Row Access Policies are evaluated using the *policy owner’s role*, not the querying user’s role.**
When Snowflake evaluates a RAP, it uses the **role that owns the policy**.  
This ensures users do **not** need direct access to sensitive lookup tables referenced inside the policy.

---

## ❌ Incorrect Statements (Common Distractors)

### **“Row Access Policies apply only to SELECT queries.”**  
False — they also apply to rows affected by `UPDATE`, `DELETE`, and `MERGE`.

### **“Row Access Policies prevent inserts or updates to hidden rows.”**  
False — RAPs filter visibility, not write operations.

### **“A Row Access Policy can only be applied to one table.”**  
False — a single RAP can be attached to **multiple tables and views**.

---

## 📘 Summary
> The two correct statements are:  
> ✔ RAPs are schema‑level objects evaluated at query time.  
> ✔ RAPs evaluate using the policy owner’s role, not the querying user’s role.

Row Access Policies are evaluated dynamically at query runtime, not when data is loaded. They commonly use context functions such as:

CURRENT_ROLE() - filters based on user's active role

CURRENT_USER() - filters based on username

CURRENT_ACCOUNT() - filters based on account

IS_ROLE_IN_SESSION() - checks if a role is available

### Snowflake's zero-copy cloning creates a completely independent object that does not share any micro-partitions with the original object.
False

Zero-copy cloning in Snowflake does not create a fully independent copy of the data; instead, it references the same micro-partitions as the original object. This means that the clone and the original object share the same storage until modifications are made, which then create new micro-partitions for the changes.


### If a Snowflake user wants to restore a dropped table within the retention period, which of the following commands should they use?

UNDROP TABLE

Explanation
The UNDROP TABLE command is used to restore a table that has been dropped, provided the table is still within the configured retention period for time travel.

### What is the primary difference between the Account Usage Schema and the Information Schema in Snowflake? (Choose the correct option.)

The Account Usage Schema includes dropped objects, while the Information Schema does not.

Explanation
correct answer because the Account Usage Schema contains information about dropped objects, while the Information Schema does not include such information.

### Which of the following is NOT true regarding Snowflake’s data encryption at rest?

Snowflake uses AES 256-bit encryption for data at rest.

Explanation
This is a true statement, as Snowflake employs AES 256-bit encryption for all stored data.

Your answer is incorrect
Rekeying is available in the Enterprise Edition and must be enabled manually.

Explanation
This statement is accurate; rekeying of data is a feature that becomes available starting from the Enterprise Edition, but it requires manual activation.

Correct answer
Data encryption at rest is an optional feature that must be enabled.

Explanation
Data encryption at rest is not an optional feature in Snowflake; it is always enabled by default. All data managed by Snowflake is encrypted automatically using AES 256-bit encryption. Users do not have to take any action to enable this feature, as it is an integral part of Snowflake’s security model.

Key rotation occurs automatically every 30 days.

Explanation
This is also true; Snowflake automatically rotates encryption keys every 30 days for enhanced security.

### Which of the following is true about Dynamic Data Masking in Snowflake?

It masks data based on the currently selected role at query runtime.

Explanation
Dynamic Data Masking works at query runtime based on the currently selected role, allowing role-specific access to sensitive information.

### What is the default time retention period for historical data in Snowflake for new accounts?
1 day

Explanation
The default data retention period for Snowflake accounts is 1 day. This applies to all accounts unless the retention period is explicitly modified.