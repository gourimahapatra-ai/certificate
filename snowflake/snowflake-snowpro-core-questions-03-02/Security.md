## Access Control Privileges Required for Search Optimization Service

### 1. Privileges to Enable Search Optimization on a Table
To add or remove the `SEARCH OPTIMIZATION` property on a table, a role must have:

- **OWNERSHIP** on the table  
  *or*
- **MODIFY** privilege on the table  
  *and*
- **USAGE** privilege on the table’s **schema** and **database**

### 2. Privileges to View Search Optimization Metadata
To view search optimization details (e.g., via `SHOW TABLES`, `DESCRIBE TABLE`, or `SEARCH_OPTIMIZATION_PROGRESS`):

- **USAGE** privilege on the database  
- **USAGE** privilege on the schema  
- **SELECT** privilege on the table

### 3. Privileges for Search Optimization on Materialized Views
To enable search optimization on a materialized view:

- **OWNERSHIP** on the materialized view  
  *or*
- **MODIFY** privilege on the materialized view  
  *and*
- **USAGE** privilege on the schema and database

### 4. Privileges for Search Optimization on External Tables
To enable search optimization on an external table:

- **OWNERSHIP** on the external table  
  *or*
- **MODIFY** privilege on the external table  
  *and*
- **USAGE** privilege on the schema and database

### 5. Privileges for Search Optimization on Individual Columns
If enabling search optimization on specific columns:

- Same privileges as enabling it on the table (OWNERSHIP or MODIFY + USAGE)

### 6. Additional Notes
- No special warehouse privileges are required because maintenance is handled automatically by Snowflake.
- Privileges must be granted to the **role** executing the `ALTER TABLE ... ADD/REMOVE SEARCH OPTIMIZATION` command.


# Secure Views vs. Regular Views in Snowflake

## Why Regular (Non‑Secure) Views Can Leak Information
Regular views in Snowflake allow the optimizer to apply **internal optimizations** that may require accessing underlying base‑table data.  
Snowflake documentation states that these optimizations can **indirectly expose hidden data** through user‑crafted queries or inference attacks. 

### Example of Indirect Exposure
A user can intentionally trigger errors (e.g., division by zero) to infer whether hidden rows exist — even if they do not have access to those rows.  
This is explicitly demonstrated in Snowflake’s documentation using a `1/iff(...)` inference attack. 

---

## How Secure Views Prevent Data Exposure
Secure views **disable the internal optimizations** that could reveal underlying data.  
Snowflake states that secure views:

- **Do not use optimizations** that require access to base‑table data  
- **Prevent inference attacks** by restricting how predicates are evaluated  
- **Hide the view definition** from unauthorized users  
- **Ensure no access to underlying tables** unless explicitly granted  


Because secure views avoid these optimizations, they may run **slightly slower**, but they provide **stronger privacy guarantees**.

---

## When to Use Secure Views
Use secure views when:

- Protecting **sensitive or regulated data**
- Preventing users from inferring hidden values
- Implementing **row access policies** or **masking policies**
- Sharing data externally or across roles

Snowflake recommends secure views for **data privacy**, not for convenience‑only views. 

---

## Exam‑Ready Takeaway
> **Regular views may expose underlying data through optimizer behavior.  
> Secure views disable those optimizations, hide the view definition, and prevent inference attacks.**



# Snowflake Access Control Model — RBAC + DAC

Snowflake’s access control framework combines **Role‑Based Access Control (RBAC)** and **Discretionary Access Control (DAC)** to manage permissions on all securable objects.

---

## Role‑Based Access Control (RBAC)

RBAC is the **primary** access control model in Snowflake.

- **Privileges are granted to roles**, not directly to users.  
- **Roles are granted to users** (or to other roles, forming a hierarchy).  
- Users inherit all privileges of the roles assigned to them.  
- This model is **scalable**, **auditable**, and **recommended** for enterprise governance.

**Key points (from documentation):**
- Privileges → Roles → Users  
- Roles can be nested (role hierarchy)  
- Users activate a role to perform actions  
- RBAC is the default and preferred model for managing access  


---

## Discretionary Access Control (DAC)

DAC is also part of Snowflake’s model.

- **Every object has an owner** (the role that created it).  
- The owner has the **OWNERSHIP** privilege.  
- The owner can **grant privileges** on that object to other roles.  
- Ownership can be **transferred** to another role.

**Key points (from documentation):**
- Object creator’s role becomes the owner  
- Owners can grant privileges to other roles  
- This is how Snowflake implements DAC  


---

## How RBAC and DAC Work Together

| Concept | Description |
|--------|-------------|
| **RBAC** | Controls access by assigning privileges to roles and roles to users |
| **DAC** | Object owners (via OWNERSHIP privilege) decide who else gets access |
| **Combined Model** | RBAC manages broad access; DAC governs object‑level control |

Example from documentation:  
- Role 1 owns Object 1 → illustrates **DAC**  
- Role 1 grants privileges on Object 1 to Role 2 → Role 2’s users gain access → illustrates **RBAC**  


---

## Additional Note: UBAC (User‑Based Access Control)

Snowflake also supports **UBAC**, where privileges can be granted directly to users.  
However, these privileges apply **only when secondary roles are enabled**.

Snowflake recommends **RBAC over UBAC** for scalability.  


---

## Exam‑Ready Takeaway
> **Snowflake uses RBAC as its primary model: privileges → roles → users.  
> DAC complements RBAC: the role that creates an object owns it and can grant access to other roles.**



# Required Privileges for a Role to Query a Table in Snowflake

To successfully run a `SELECT` query on a table, a role needs **more than just the SELECT privilege**.  
Snowflake enforces a hierarchical privilege model: a role must have permission to **use every object in the path** leading to the table.

---

## 1. SELECT Privilege on the Table
The **ANALYST** role must have:

```sql
GRANT SELECT ON TABLE marketing.public.customer TO ROLE analyst;
```

This allows reading rows from the table — **but this alone is not enough**.

---

## 2. USAGE Privilege on the Database
The role must be able to *use* the database containing the table:

```sql
GRANT USAGE ON DATABASE marketing TO ROLE analyst;
```

Without this, the role cannot reference any objects inside the database.

---

## 3. USAGE Privilege on the Schema
The role must also be able to *use* the schema:

```sql
GRANT USAGE ON SCHEMA marketing.public TO ROLE analyst;
```

Without schema‑level USAGE, the role cannot resolve the table name, even with full namespace.

---

## Why USAGE Is Required
The **USAGE** privilege allows:

- Running `USE DATABASE` and `USE SCHEMA`
- Accessing objects via fully qualified names such as:  
  `MARKETING.PUBLIC.CUSTOMER`
- Resolving object names during query compilation

If USAGE is missing at either level, Snowflake blocks the query **before** checking table privileges.

---

## Exam‑Ready Takeaway
> To query a table, a role needs **SELECT on the table** *and* **USAGE on both the database and schema**.  
> Missing any of these privileges prevents the role from running queries.



# Tri‑Secret Secure — Summary

## What Tri‑Secret Secure Is
**Tri‑Secret Secure** is Snowflake’s advanced encryption model that combines:

1. A **Snowflake‑managed key**
2. A **customer‑managed key** (stored in the customer’s cloud KMS)
3. A **composite master key** created from both

This combined key is required to decrypt your data.  
If the customer disables their key, **all access to the data is immediately blocked**, even for Snowflake.

---

## How It Works
- Snowflake manages its own encryption hierarchy as usual.
- You supply a **Customer‑Managed Key (CMK)** via:
  - AWS KMS  
  - Azure Key Vault  
  - GCP Cloud KMS  
- Snowflake merges both keys into a **composite master key**.
- Both keys must be available for data access.

This gives customers **direct control** over data availability.

---

## Edition Requirement
Tri‑Secret Secure is available **only in Business Critical Edition or higher**.

- Not available in Standard or Enterprise editions.
- Must be **enabled by Snowflake Support**.

---

## Why It Matters
Tri‑Secret Secure provides:

- **Customer‑controlled revocation**  
  (Disable your CMK → data becomes inaccessible)
- **Stronger security posture** for regulated industries
- **Defense‑in‑depth** beyond standard encryption

---

## Exam‑Ready Takeaway
> **Tri‑Secret Secure = Snowflake key + customer key → composite master key.  
> Requires Business Critical Edition and activation through Snowflake Support.**


### The MODIFY privilege allows a role to alter the size of a virtual warehouse.

https://docs.snowflake.com/en/sql-reference/sql/alter-warehouse#access-control-requirements



### The PUBLIC role is one of the out-of-the-box roles in Snowflake. The PUBLIC role has the fewest privileges and is assigned automatically to all users.

https://docs.snowflake.com/en/user-guide/security-access-control-overview#system-defined-roles.


# The PUBLIC Role in Snowflake

## What the PUBLIC Role Is
**PUBLIC** is one of Snowflake’s **system‑defined, out‑of‑the‑box roles**.  
It is automatically granted to **every user** in the account at the moment the user is created.

---

## Key Characteristics of the PUBLIC Role

### 1. Assigned to All Users
- Every Snowflake user **inherits** the PUBLIC role.
- This ensures that all users have a **baseline level of access**.

### 2. Fewest Privileges
- PUBLIC intentionally has the **minimal set of privileges**.
- It typically includes:
  - Ability to see certain shared objects
  - Access to basic account metadata
- Administrators may grant additional privileges to PUBLIC, but this is **not recommended** for security reasons.

### 3. Foundation for Access Control
- PUBLIC acts as the **default role layer**.
- Any privilege granted to PUBLIC is effectively granted to **every user**.

---

## Why PUBLIC Matters
- Ensures consistent baseline access across the account.
- Helps avoid accidental privilege gaps.
- Serves as a fallback role when a user has no other active role.

---

## Exam‑Ready Takeaway
> **PUBLIC is a built‑in Snowflake role with the fewest privileges, automatically assigned to all users.**  
> Any privilege granted to PUBLIC is inherited by every user in the system.


The correct syntax is GRANT CREATE MATERIALIZED VIEW ON SCHEMA <schema_name> TO ROLE <role_name>;



https://docs.snowflake.com/en/user-guide/views-materialized#privileges-on-a-materialized-view-s-schema



### Which function is used to determine the fully qualified URL and port for Snowight when configuring Snowight for access through a proxy or a firewall?

You need to add the fully qualified URL and port values to the proxy servers or firewall settings to use a proxy or firewall to connect to Snowsight.
Use the SNOWSIGHT_DEPLOYMENT item in the return value of the SYSTEM$ALLOWLIST function to find out the fully qualified Snowsight URL and port.

https://docs.snowflake.com/en/user-guide/ui-snowsight-gs#accessing-sf-web-interface-through-a-proxy-or-firewall




### You are required to implement column-level security in Snowflake. Which techniques can you use? Select two.

Snowflake supports masking policies that may be applied to columns and enforced at the column level to provide column-level security. Column-level security is achieved by dynamic data masking or external Tokenization.
 https://docs.snowflake.com/en/user-guide/security-column
