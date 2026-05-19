When cloning a database, your current role must have which privilege (as a minimum) on the source database?

USAGE : To clone a table, you need SELECT privileges on the source table. For cloning Pipes, Streams & Tasks, you require OWNERSHIP privileges; for all other objects that can be cloned, you need the USAGE privilege. https://docs.snowflake.com/en/sql-reference/sql/create-clone#general-usage-notes


### Which of the following can be cloned?

- Database
- Schemas
- Tables

Named Internal Stages cannot be cloned. When a database or schema is cloned, any Snowpipe that points to a Named Internal Stage is not cloned. Named External Stages can be cloned. Since a table stage is associated with a table, it is automatically cloned when the table is cloned. Additionally, external tables cannot be cloned either. Databases, Schema, Tables, etc., can be cloned. 
https://docs.snowflake.com/en/user-guide/object-clone#cloning-and-stages