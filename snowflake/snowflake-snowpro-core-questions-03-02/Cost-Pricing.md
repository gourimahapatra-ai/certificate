### Which of the following contributes towards the storage costs in Snowflake?

- Temporary Tables
- Transient Tables
- Permanent Tables

Data stored in permanent tables counts towards the storage costs.
Data stored in temporary & transient tables also contribute towards the storage costs until they are dropped or data is cleared.
Data in Fail-safe storage and Time Travel storage also contribute to the storage costs.
Transient and temporary tables, however, do not contribute towards Fail-safe storage costs and have a maximum of 1-day Time Travel costs.
Caching is NOT considered for determining storage costs. The query result cache & metadata cache are part of the cloud services layer.
The warehouse cache (local disk cache) is part of a virtual warehouse and does NOT contribute to storage costs.

https://docs.snowflake.com/en/user-guide/cost-understanding-overall

