# Databricks Secret ACLs — Simplified Guide

## Official Documentation

Databricks Documentation:

https://docs.databricks.com/aws/en/security/auth/access-control#secret-acls

---

# What is a Secret Scope?

A **secret scope** is a secure container used to store sensitive information such as:

- Passwords
- API Keys
- Access Tokens
- Database Credentials
- Connection Strings

Example:

```python
dbutils.secrets.get(scope="prod-scope", key="db-password")
```

Here:

- `prod-scope` = Secret Scope
- `db-password` = Secret Key

---

# What are Secret ACLs?

ACL stands for:

**Access Control List**

Secret ACLs define:

- Who can access secrets
- Who can modify secrets
- Who can manage permissions

Databricks provides **3 permission levels**.

---

# The 3 Secret ACL Permission Levels

| Permission | Description |
|---|---|
| READ | Read and list secrets |
| WRITE | Create/update secrets |
| MANAGE | Full administrative control |

---

# 1. READ Permission

Users with READ permission can:

✅ Read secret values  
✅ List secret names  

Users with READ permission cannot:

❌ Create secrets  
❌ Update secrets  
❌ Change ACL permissions  

Example:

```python
dbutils.secrets.get("prod-scope", "db-password")
```

READ permission is required for this operation.

---

# 2. WRITE Permission

Users with WRITE permission can:

✅ Read secrets  
✅ List secrets  
✅ Add new secrets  
✅ Update existing secrets  

Users with WRITE permission cannot:

❌ Change ACL permissions

Important:

> WRITE permission automatically includes READ permission.

Example:

```bash
databricks secrets put-secret
```

WRITE permission is required.

---

# 3. MANAGE Permission

Users with MANAGE permission can:

✅ Read secrets  
✅ Write secrets  
✅ Delete secrets  
✅ Change ACL permissions  
✅ Manage the entire scope  

This is the highest permission level.

Example:

```bash
databricks secrets put-acl
```

MANAGE permission is required.

---

# Permission Matrix

| Action | READ | WRITE | MANAGE |
|---|---|---|---|
| Read secret | ✅ | ✅ | ✅ |
| List secrets | ✅ | ✅ | ✅ |
| Create secret | ❌ | ✅ | ✅ |
| Update secret | ❌ | ✅ | ✅ |
| Delete secret | ❌ | ❌ | ✅ |
| Change ACL permissions | ❌ | ❌ | ✅ |

---

# Common Databricks CLI Commands

## Create a Secret Scope

```bash
databricks secrets create-scope my-scope
```

---

## Add a Secret

```bash
databricks secrets put-secret my-scope db-password
```

---

## Grant READ Permission

```bash
databricks secrets put-acl my-scope user1 READ
```

---

## Grant WRITE Permission

```bash
databricks secrets put-acl my-scope user1 WRITE
```

---

## Grant MANAGE Permission

```bash
databricks secrets put-acl my-scope user1 MANAGE
```

---

# Real-World Example

Suppose a company has:

- Developers
- DevOps Engineers
- Security Administrators

Recommended permissions:

| Team | Permission |
|---|---|
| Developers | READ |
| DevOps Engineers | WRITE |
| Security Administrators | MANAGE |

---

# Certification Exam Tips

## Most Important Point

> WRITE permission includes READ permission.

Many exam questions test this concept.

---

# Easy Memory Tricks

| Permission | Easy Meaning |
|---|---|
| READ | Use secrets |
| WRITE | Create/update secrets |
| MANAGE | Full admin control |

---

# Final One-Line Revision

> READ = Use secrets  
> WRITE = Modify secrets  
> MANAGE = Control everything
