# Implementing Row-Level and Column-Level Security in Delta Tables

## 1. Row-Level Security (RLS)
- Controls access at the **record level**.
- Ensures users only see rows they are authorized to view.
- Implemented using **row filters** or **predicate-based policies** in Unity Catalog.
- Useful for multi-tenant datasets, regional restrictions, or department-based access.

## 2. Column-Level Security (CLS)
- Restricts access to **specific columns** containing sensitive information.
- Prevents exposure of fields such as PII, financial data, or credentials.
- Implemented using **column masks**, **view-based masking**, or **grants**.
- Ensures users only access the attributes they are permitted to see.

## 3. Delta Tables for Data Governance
- Delta Lake provides ACID transactions, schema enforcement, and versioning.
- Works seamlessly with Unity Catalog’s fine-grained security controls.
- Enables secure, governed access across tables, views, and columns.
- Supports scalable governance for both batch and streaming workloads.

## 4. Dynamic Data Masking
- Masks sensitive fields dynamically at query time.
- Common masking types:
  - Partial masking (e.g., showing only last 4 digits)
  - Null masking
  - Hashing or tokenization
- Ensures sensitive data is protected without duplicating datasets.

## 5. Compliance and Regulatory Requirements
- Fine-grained access controls help meet standards such as:
  - GDPR  
  - HIPAA  
  - SOC 2  
  - PCI-DSS  
- Ensures auditability, traceability, and secure data handling.
- Reduces risk by enforcing least-privilege access.

## 6. Summary
Row-level and column-level security provide powerful mechanisms to protect sensitive data in Delta Tables. With Unity Catalog’s governance features, organizations can enforce fine-grained access, apply dynamic masking, and maintain compliance across their data ecosystem.
