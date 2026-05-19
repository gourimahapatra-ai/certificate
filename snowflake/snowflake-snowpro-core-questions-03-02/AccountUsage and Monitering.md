# Snowflake Resource Monitors — Summary

## 1. Purpose
Resource monitors help **control credit consumption** by:
- Tracking warehouse credit usage
- Triggering actions (notify, suspend, suspend immediately)
- Preventing unexpected spend

> They apply **only to user‑managed warehouses**, not serverless features (use Budgets for those).

---

## 2. Key Components

### **Credit Quota**
- Total credits allocated for the interval.
- Tracks usage from:
  - Virtual warehouses
  - Cloud services supporting those warehouses

### **Monitor Type**
- **Account monitor**: tracks all warehouses (only one allowed)
- **Warehouse monitor**: tracks assigned warehouses (each warehouse can belong to only one monitor)

### **Schedule**
- Defines when usage resets.
- Properties:
  - **Frequency**: daily, weekly, monthly, yearly, never
  - **Start timestamp**
  - **End timestamp** (optional)

> Reset always occurs at **12:00 AM UTC**.

---

## 3. Actions (Triggers)
Actions fire when usage reaches a percentage threshold.

Supported actions:
- **Notify** — send alert only
- **Suspend** — graceful stop (running queries finish)
- **Suspend Immediately** — hard stop (running queries canceled)

Rules:
- Max **1 Suspend**
- Max **1 Suspend Immediately**
- Up to **5 Notify** actions
- Thresholds may exceed 100%

---

## 4. Assignment Rules
- A warehouse can be assigned to **only one** warehouse-level monitor.
- Account-level monitor does **not override** warehouse-level monitors.
- If either monitor hits a suspend threshold → warehouse suspends.

---

## 5. Warehouse Suspension & Resumption
A suspended warehouse resumes only when:
- Interval resets
- Credit quota increases
- Threshold increases
- Warehouse is unassigned from the monitor
- Monitor is dropped

> Cloud services may still incur cost even after warehouse suspension.

---

## 6. Notifications
Sent when thresholds are reached.

Who receives them:
- **Warehouse monitors**: account admins + listed non-admin users
- **Account monitors**: only account admins

Users must:
- Verify email
- Enable notifications in Snowsight

---

## 7. Access Control Privileges
To **view or modify** a resource monitor:
- **MONITOR** privilege → view
- **MODIFY** privilege → change quota, schedule, actions

Only **ACCOUNTADMIN** can:
- Create resource monitors
- Change monitor type (warehouse ↔ account)
- Modify warehouse assignments

---

## 8. DDL Commands
- `CREATE RESOURCE MONITOR`
- `ALTER RESOURCE MONITOR`
- `SHOW RESOURCE MONITORS`
- `DROP RESOURCE MONITOR`
- `ALTER WAREHOUSE ... SET/UNSET RESOURCE_MONITOR`
- `ALTER ACCOUNT SET RESOURCE_MONITOR = ...`

---

## 9. Best Practices
- Use **buffers** (e.g., suspend at 90% instead of 100%)
- Assign **one warehouse per monitor** for strict control
- Use **Budgets** for serverless features (Snowpipe, Auto Clustering, etc.)

---

## 10. Example (SQL)
```sql
CREATE RESOURCE MONITOR limit1
  WITH CREDIT_QUOTA = 1000
  TRIGGERS
    ON 90 PERCENT DO SUSPEND
    ON 100 PERCENT DO SUSPEND_IMMEDIATE;

ALTER WAREHOUSE wh1 SET RESOURCE_MONITOR = limit1;
```

Question : What are resource monitors used for?
Ans : Control costs and credit use by virtual warehouses



### The query history page lets users view the history of executed and currently executing queries. The query history page can show the history of queries executed in the last 14 days. 

https://docs.snowflake.com/en/user-guide/ui-snowsight-activity#query-history

### Which of the following can be fulfilled through the ACCESS_HISTORY view in the ACCOUNT_USAGE schema?

Using the ACCESS_HISTORY view, you can identify what data was accessed, when, and who accessed it. Using this information, you can also identify what data is not being accessed at all.



There are other benefits of using ACCESS_HISTORY data, which can be found at the following link.

https://docs.snowflake.com/en/user-guide/access-history#benefits



### If the filters supplied in an INFORMATION SCHEMA query are not sufficiently selective, the following error is returned. Information schema query returned too much data. Please repeat the query with more selective predicates. 

https://docs.snowflake.com/en/sql-reference/info-schema#general-usage-notes


### Which method can you use to retrieve the history of data loaded into tables through Snowpipe and the COPY INTO command?
### Query the COPY_HISTORY view in the ACCOUNT_USAGE schema
The COPY_HISTORY view in the ACCOUNT_USAGE schema can be used to view history for data loaded through either the COPY command or continuous data loaded through Snowpipe. The COPY_HISTORY view shows the history for the last 365 days.
The LOAD_HISTORY view shows data only for the COPY command. The PIPE_USAGE_HISTORY view shows only the Snowpipe history.

https://docs.snowflake.com/en/sql-reference/account-usage/copy_history



### How many days of historical data can you access through the views in the ACCOUNT_USAGE schema? 365b days

The ACCOUNT USAGE schema consists of several views that provide usage metrics and metadata information at the account level. Data provided by the ACCOUNT_USAGE views is NOT real-time and refreshes typically with a lag of 45 minutes to 3 hours, depending on the view. The data in these views are retained for up to 365 days. https://docs.snowflake.com/en/sql-reference/account-usage#differences-between-account-usage-and-information-schema


