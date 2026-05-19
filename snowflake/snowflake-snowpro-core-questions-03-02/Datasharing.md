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



### A reader account can be used to share data with a non-Snowflake user or a non-Snowflake organization. True 

# Reader Accounts — Sharing Data with Non‑Snowflake Users

## What a Reader Account Is
A **reader account** is a special type of Snowflake account that a **data provider creates and manages** for the sole purpose of sharing data with users or organizations **that do not have their own Snowflake account**.

This allows external consumers to query shared data **without becoming Snowflake customers**.

---

## Key Characteristics

- **Created by the data provider**  
  The provider owns and administers the reader account.

- **Used only for data sharing**  
  Reader accounts cannot create their own databases or ingest data independently.

- **Consumers access shared data through Snowsight or SQL**  
  They can run queries but cannot modify the shared objects.

- **Billing is handled by the provider**  
  The provider pays for compute used by the reader account.

---

## Why Reader Accounts Exist
Reader accounts enable secure, controlled data sharing with:

- Partners  
- Vendors  
- Clients  
- External teams without Snowflake subscriptions  

They provide a **zero‑friction onboarding path** for data consumers.

---

## Exam‑Ready Takeaway
> **Reader accounts allow sharing data with non‑Snowflake users.  
> They are created and fully managed by the data provider for sharing purposes only.**


### Which system function can be used to control access to data in a share and allow specific data only to paying customers?

SYSTEM$IS_LISTING_PURCHASED

SYSTEM$IS_LISTING_PURCHASED system function can be used to control which data is visible to a paid customer and which to a trial customer.

https://other-docs.snowflake.com/en/collaboration/provider-listings-preparing#preparing-shares-for-a-paid-listing

