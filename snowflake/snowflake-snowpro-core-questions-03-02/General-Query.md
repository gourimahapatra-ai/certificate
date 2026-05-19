
### The LAST_QUERY_ID function returns the query ID of a specified query in the current session. The function takes a number as the parameter, which specifies the position of the query in the session.

The parameter can take positive or negative values. A negative value means you are attempting to fetch the most recent query in the session, where

-1 = most recent query

-2 = 2nd most recent query

, and so on. The function defaults to -1, so if no value is provided, it will return the query id of the most recent query.

A positive number returns the earliest queries in the session. i.e.

1 = first query

2 = 2nd query



https://docs.snowflake.com/en/sql-reference/functions/last_query_id