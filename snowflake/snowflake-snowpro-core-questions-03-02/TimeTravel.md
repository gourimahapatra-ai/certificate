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


### Time Travel 
Depending on the Snowflake edition, the Time Travel duration might range from 1 to 90 days. The Standard edition allows for one day of Time Travel. Time Travel is possible for up to 90 days in the Enterprise version and above. https://docs.snowflake.com/en/user-guide/data-time-travel#data-retention-period