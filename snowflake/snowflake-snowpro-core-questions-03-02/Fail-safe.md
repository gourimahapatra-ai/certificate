# Snowflake Fail‑Safe — Access & Recovery Rules

## What Fail‑Safe Is
Fail‑safe is Snowflake’s **final data recovery layer**, designed for disaster recovery and internal operational failures.  
It is **not** a user‑accessible feature and is **not** intended for routine recovery.

---

## Who Can Access Fail‑Safe Data?

### ❌ Customers Cannot Access Fail‑Safe
- Customers **cannot directly view, query, or retrieve** data stored in Fail‑safe.
- Fail‑safe is **not** a self‑service recovery mechanism.

### ✔ Only Snowflake Support Can Recover Data
- Once data enters Fail‑safe, **only Snowflake Support** can restore it.
- Recovery is performed **manually** by Snowflake engineers.
- This process is used only for **critical emergencies**.

---

## Cloud Providers Cannot Access Snowflake Data

Snowflake documentation makes this explicit:

- The **cloud provider (AWS, Azure, GCP)** has **no access** to Snowflake‑managed data.
- This includes:
  - Fail‑safe storage  
  - Time Travel storage  
  - Active storage  
  - Metadata  

Snowflake encrypts all data and manages its own storage layer, ensuring **complete isolation** from the underlying cloud vendor.

---

## Why Fail‑Safe Exists
Fail‑safe provides:
- A **7‑day** final recovery window (for permanent tables)
- Protection against:
  - Catastrophic failures  
  - Internal Snowflake issues  
  - Accidental or malicious data loss beyond Time Travel  

It is **not** meant for:
- Undoing user mistakes  
- Routine restores  
- Application‑level recovery  

(Time Travel covers those scenarios.)

---

## Exam‑Ready Takeaway
> **Fail‑safe is accessible only by Snowflake Support.  
> Customers cannot access Fail‑safe, and cloud providers cannot access any Snowflake‑stored data, including Fail‑safe.**



## Fail-safe is supported in all Snowflake editions; therefore, the minimum edition with fail-safe support is the Standard edition. https://docs.snowflake.com/en/user-guide/data-failsafe