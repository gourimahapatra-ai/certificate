### Which statements are correct regarding the costs of using event notifications to refresh a directory table's metadata?

A small maintenance cost is charged for refreshing a directory table's metadata, whether through notifications or manually (through ALTER STAGE <stage-name> REFRESH). This small maintenance cost is accounted for under the cloud services costs.
Additionally, when using cloud platform notifications, an additional cost is charged, which appears as Snowpipe charges in your billing statement. The Snowpipe cost is charged because Snowpipe is used for event notifications to trigger the automatic refresh.

https://docs.snowflake.com/en/user-guide/data-load-dirtables-intro#billing-for-directory-tables



### When a directory table is queried, the result set contains the FILE_URL for each file in the stage object. The result set also contains additional metadata, such as the file's relative path, which shows the file's path relative to the stage. The result set also has metadata such as the size of the file in bytes and the timestamp of when a file was last modified, the MD5 checksum for the file, and an ETAG file, which changes if the contents of the file change. When querying a directory table, you can filter the result set using the WHERE clause on any of these fields. For example, you can use the size column to limit your results to only those files that are greater than 10MB.

https://docs.snowflake.com/en/user-guide/data-load-dirtables-manage#output
