**Question 1: **
  In DLT* pipelines, You can stream data from other tables in the same pipeline by using the STREAM() function**. In this case, you must define a streaming table using the CREATE STREAMING TABLE syntax.
  CREATE STREAMING TABLE table_name
  AS SELECT * FROM STREAM(source_table)
  
  * Please note that **Delta Live Tables (DLT)** has been recently renammed to **Lakeflow Declarative Pipeline**, however, the current exam version may still refer to it as Delta Live Tables.
  
  ** A recent syntax update now also supports the use of STREAM as a keyword.
  
  CREATE STREAMING TABLE table_name
  AS SELECT *
     FROM STREAM source_table;
