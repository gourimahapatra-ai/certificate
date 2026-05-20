# Snowflake Alerts & Notifications — SnowPro Core SC0‑03 Study Guide

## 1. What Are Alerts in Snowflake?
Snowflake **Alerts** are schema-level objects that automatically run a SQL condition on a schedule and execute an action when the condition evaluates to TRUE.

They are used for:
- Monitoring system health  
- Detecting anomalies  
- Triggering notifications  
- Automating operational checks  
- Observability and governance workflows  

Alerts behave similarly to **Tasks**, but with **conditional logic**.

---

## 2. Alert Components

### **2.1 Condition (IF clause)**
A SQL query that returns **TRUE** or **FALSE**.  
If TRUE → the alert fires.

### **2.2 Action (THEN clause)**
A SQL statement executed when the condition is met.  
Common actions:
- Insert into a log table  
- Call a stored procedure  
- Trigger a notification integration  

### **2.3 Schedule**
Alerts run on:
- Simple intervals (`5 MINUTE`, `1 HOUR`)  
- Cron expressions  

### **2.4 Warehouse**
Alerts require a **warehouse** to run.

---

## 3. Creating an Alert

```sql
CREATE OR REPLACE ALERT credit_usage_alert
  WAREHOUSE = wh_monitor
  SCHEDULE = '5 MINUTE'
  IF (SELECT SUM(credits_used) > 100 FROM usage_table)
  THEN CALL notify_admin();
```

---

## 4. Managing Alerts

```sql
ALTER ALERT credit_usage_alert RESUME;   -- Enable
ALTER ALERT credit_usage_alert SUSPEND;  -- Disable
DROP ALERT credit_usage_alert;           -- Remove
```

Alerts must be **resumed** to run.

---

## 5. Monitoring Alerts

### **5.1 ALERT_HISTORY View**
Shows:
- Condition result  
- Action execution status  
- Errors  
- Timestamps  

```sql
SELECT * FROM TABLE(INFORMATION_SCHEMA.ALERT_HISTORY());
```

### **5.2 ALERTS View**
Shows:
- Owner  
- Schedule  
- Warehouse  
- State (SUSPENDED / RESUMED)  

---

## 6. Notifications in Snowflake

Alerts often trigger notifications via **Notification Integrations**.

Supported outbound services:
- AWS SNS  
- Azure Event Grid  
- GCP Pub/Sub  

Example:

```sql
CREATE NOTIFICATION INTEGRATION my_sns
  TYPE = QUEUE
  ENABLED = TRUE
  DIRECTION = OUTBOUND
  ...;
```

Alerts typically call a stored procedure that publishes a message to the integration.

---

## 7. Alerts vs Tasks

| Feature | Alerts | Tasks |
|--------|--------|-------|
| Conditional logic | **Yes** | No |
| Schedule | Yes | Yes |
| Requires warehouse | Yes | Yes |
| Best for | Monitoring & notifications | ETL orchestration |
| Executes SQL | Yes | Yes |

---

## 8. Limitations (Exam‑Relevant)

- Alerts **require a warehouse**  
- Alerts **cannot directly send notifications** — must call a procedure or integration  
- Alerts run only in **Enterprise Edition or higher**  
- Alerts cannot modify their own schedule dynamically  
- Alerts cannot run long‑running or heavy ETL workloads  

---

## 9. Common SnowPro Exam Questions

### **Q: What does an alert do?**  
Runs a condition query and executes an action when TRUE.

### **Q: Do alerts require a warehouse?**  
Yes.

### **Q: Where do you monitor alert executions?**  
`ALERT_HISTORY`.

### **Q: Can alerts send notifications directly?**  
No — they must call a stored procedure or use a notification integration.

### **Q: Are alerts schema objects?**  
Yes.

---

## 10. Summary

Snowflake Alerts provide automated, conditional monitoring and action execution.  
They integrate with external notification systems and are essential for observability, governance, and operational automation — making them a key topic in the **SnowPro Core SC0‑03** exam.

