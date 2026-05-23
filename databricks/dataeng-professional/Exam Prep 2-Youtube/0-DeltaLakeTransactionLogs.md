# Delta Lake Transaction Logs

## 1. Overview
Delta Lake uses a transaction log stored in the `_delta_log` directory. This log tracks every change made to a Delta table and enables ACID transactions, time travel, versioning, and reliable data operations.

## 2. JSON Transaction Log Files
- JSON files represent incremental commits.
- Each JSON file corresponds to a single table version.
- Contains metadata changes such as schema updates, partition information, and table properties.
- Records add/remove file actions describing which Parquet data files are active.
- Stores commit information including operation type, timestamp, and user.
- Includes protocol information defining reader and writer compatibility.
- JSON captures only incremental state changes, not full snapshots.

## 3. Parquet Checkpoint Files
- Checkpoints are written periodically (default every 10 commits).
- Stored in Parquet format.
- Represent a complete snapshot of the table state at a specific version.
- Improve performance by avoiding replay of all JSON files.
- Contain consolidated metadata and active file listings.
- Used to reconstruct the table state efficiently.

## 4. ACID Properties
- Atomicity: Each transaction is fully committed or not applied.
- Consistency: Schema enforcement and constraints ensure valid data.
- Isolation: Uses optimistic concurrency control to manage concurrent writes.
- Durability: Logs and data files are persisted in cloud storage.
- ACID guarantees are achieved through the transaction log, not through locking.

## 5. Time Travel
- Each commit increments the table version.
- JSON and checkpoint files preserve historical state.
- Time travel allows querying by version number or timestamp.
- Historical data is available as long as logs and files are retained.
- VACUUM removes old files beyond the retention period, affecting time travel depth.

## 6. Structure of the `_delta_log` Directory
- Sequential JSON files (e.g., `00000000000000000010.json`).
- Parquet checkpoint files (e.g., `00000000000000000010.checkpoint.parquet`).
- `_last_checkpoint` file pointing to the latest checkpoint.
- Directory name includes the leading underscore.

## 7. How Delta Lake Reads the Log
1. Identify the latest checkpoint.
2. Load the checkpoint Parquet file.
3. Apply all JSON commits after the checkpoint.
4. Build the current metadata and list of active data files.
5. Read the actual Parquet data files.

## 8. Key Concepts for Databricks Certification
- JSON files store incremental log entries.
- Parquet files store checkpoints.
- `_delta_log` is the transaction log directory.
- ACID guarantees are provided through the log.
- Time travel uses versioned logs.
- Optimistic concurrency control manages concurrent writes.
- Schema enforcement and evolution are recorded in the log.
- VACUUM removes old files but respects retention periods.
- Protocol versions define compatibility for readers and writers.
