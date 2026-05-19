# Snowsight Worksheet Context — Role, Warehouse, Database, Schema

## What You Can Configure in a Snowsight Worksheet
Snowsight allows you to **explicitly choose the execution context** for each worksheet.  
This context determines **how queries run** and **which objects you can reference without fully qualifying names**.

---

## 1. Primary Role (Execution Role)
You can choose the **primary role** under which the worksheet executes queries.  
The role determines:

- Which databases, schemas, and objects you can access  
- Which privileges apply during query execution  

This is visible and selectable in the **context bar** of the worksheet.  


---

## 2. Virtual Warehouse
You can select the **warehouse** used to run queries.

- Controls compute resources  
- Can be changed at any time  
- You can resume, suspend, or resize the warehouse from the same context bar  


---

## 3. Default Database & Schema
You can set the **default database and schema** for the worksheet.

- Once set, you **do not need to prefix** object names with `database.schema`  
- Queries can reference tables directly (e.g., `SELECT * FROM my_table`)  
- This is configured via the context bar or by using `USE DATABASE` / `USE SCHEMA`  


---

## 4. How to Set Context (Two Methods)

### **A. Using the Snowsight UI (Context Bar)**
- Choose **Role**
- Choose **Warehouse**
- Choose **Database**
- Choose **Schema**

This is the fastest way and applies immediately.  


### **B. Using SQL Commands**
You can also set context manually:

```sql
USE ROLE my_role;
USE WAREHOUSE my_wh;
USE DATABASE my_db;
USE SCHEMA my_schema;
```



---

## Exam‑Ready Takeaway
> **Snowsight worksheets let you choose the primary role, warehouse, database, and schema.  
> Setting these defaults removes the need to fully qualify object names and ensures queries run under the correct permissions and compute context.**


### Snowsight supports

Bar charts,

Line charts,

Scatterplots,

Heat grids and

Scorecards

