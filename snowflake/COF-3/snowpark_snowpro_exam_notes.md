# Snowpark Documentation for SnowPro Core COF-C02 / SnowPro Code 30 Exam

## Table of Contents
1. Introduction to Snowpark
2. Snowpark Architecture
3. Supported Languages
4. Snowpark DataFrames
5. Reading and Writing Data
6. Transformations and Actions
7. User-Defined Functions (UDFs)
8. User-Defined Table Functions (UDTFs)
9. Stored Procedures with Snowpark
10. Snowpark Optimization
11. Snowpark vs Spark
12. Security and Governance
13. Common Snowpark SQL Functions
14. Snowpark Best Practices
15. Exam Tips
16. Important Snowpark Commands
17. Sample Snowpark Python Programs
18. Frequently Asked SnowPro Exam Questions

---

# 1. Introduction to Snowpark

Snowpark is Snowflake’s developer framework that allows developers, data engineers, and data scientists to process data directly inside Snowflake using programming languages such as:

- Python
- Java
- Scala

Snowpark enables users to:

- Build data pipelines
- Create machine learning workflows
- Perform transformations
- Execute stored procedures
- Run custom business logic inside Snowflake

## Key Benefit

The computation happens inside Snowflake virtual warehouses. Data does not need to move outside Snowflake.

---

# 2. Snowpark Architecture

## Components

### Client Layer
Applications written using:
- Python
- Java
- Scala

### Snowpark API
Provides DataFrame-based APIs.

### Snowflake Engine
Executes generated SQL queries.

### Virtual Warehouse
Performs compute operations.

## Workflow

1. Application creates Snowpark session
2. DataFrame transformations are defined
3. Snowpark converts transformations into SQL
4. SQL executes inside Snowflake
5. Results returned to application

---

# 3. Supported Languages

| Language | Library |
|---|---|
| Python | snowflake-snowpark-python |
| Java | snowpark-java |
| Scala | snowpark-scala |

## Install Snowpark Python

```bash
pip install snowflake-snowpark-python
```

---

# 4. Snowpark DataFrames

Snowpark DataFrames are lazy-evaluated distributed datasets.

## Create Session

```python
from snowflake.snowpark import Session

connection_parameters = {
    "account": "account_name",
    "user": "username",
    "password": "password",
    "role": "ACCOUNTADMIN",
    "warehouse": "COMPUTE_WH",
    "database": "DEMO_DB",
    "schema": "PUBLIC"
}

session = Session.builder.configs(connection_parameters).create()
```

## Read Table

```python
df = session.table("EMPLOYEE")
```

## Select Columns

```python
df.select("EMP_ID", "EMP_NAME")
```

## Filter Rows

```python
df.filter(df["SALARY"] > 5000)
```

## Sort Data

```python
df.sort(df["SALARY"].desc())
```

## Show Results

```python
df.show()
```

---

# 5. Reading and Writing Data

## Read CSV File from Stage

```python
df = session.read.schema(schema).csv("@my_stage/data.csv")
```

## Read JSON

```python
df = session.read.json("@my_stage/sample.json")
```

## Write Data to Table

```python
df.write.save_as_table("TARGET_TABLE")
```

## Append Data

```python
df.write.mode("append").save_as_table("TARGET_TABLE")
```

## Overwrite Data

```python
df.write.mode("overwrite").save_as_table("TARGET_TABLE")
```

---

# 6. Transformations and Actions

## Transformations
Transformations are lazy operations.

Examples:
- select()
- filter()
- join()
- group_by()
- sort()

## Actions
Actions trigger execution.

Examples:
- show()
- collect()
- count()
- save_as_table()

## Example

```python
from snowflake.snowpark.functions import col

result = (
    df.filter(col("SALARY") > 10000)
      .select("EMP_NAME", "SALARY")
)

result.show()
```

---

# 7. User-Defined Functions (UDFs)

UDFs allow custom logic using Python, Java, or Scala.

## Python UDF Example

```python
from snowflake.snowpark.functions import udf

@udf
def multiply_by_two(x: int) -> int:
    return x * 2
```

## Register UDF

```python
session.udf.register(
    func=multiply_by_two,
    return_type=IntegerType(),
    input_types=[IntegerType()],
    name='MULTIPLY_BY_TWO',
    is_permanent=False
)
```

## Call UDF

```python
df.select(multiply_by_two(df["VALUE"]))
```

---

# 8. User-Defined Table Functions (UDTFs)

UDTFs return multiple rows.

## Example

```python
from snowflake.snowpark.functions import udtf

class SplitWords:
    def process(self, text: str):
        for word in text.split():
            yield (word,)
```

---

# 9. Stored Procedures with Snowpark

Stored procedures allow procedural logic execution.

## Example

```python
from snowflake.snowpark.functions import sproc

@sproc
def my_proc(session: Session) -> str:
    session.sql("DELETE FROM TEMP_TABLE").collect()
    return "Completed"
```

---

# 10. Snowpark Optimization

## Predicate Pushdown
Filters execute inside Snowflake.

## Lazy Evaluation
Queries execute only when actions are triggered.

## Minimize Data Movement
Keep processing inside Snowflake.

## Use Column Pruning
Select only required columns.

## Avoid Excessive collect()
collect() moves data to client side.

---

# 11. Snowpark vs Spark

| Feature | Snowpark | Apache Spark |
|---|---|---|
| Execution Engine | Snowflake | Spark Cluster |
| Data Movement | Minimal | Often required |
| Infrastructure | Managed by Snowflake | User-managed |
| Language Support | Python, Java, Scala | Multiple |
| Optimization | Automatic | Manual tuning often needed |

---

# 12. Security and Governance

## Features

- Role-Based Access Control (RBAC)
- Secure UDFs
- Secure Views
- Data Masking
- Row Access Policies

## Important Exam Point

Snowpark executes using Snowflake security policies.

---

# 13. Common Snowpark SQL Functions

## Import Functions

```python
from snowflake.snowpark.functions import *
```

## Common Functions

| Function | Purpose |
|---|---|
| col() | Reference column |
| lit() | Literal value |
| upper() | Convert to uppercase |
| lower() | Convert to lowercase |
| concat() | Concatenate strings |
| avg() | Average |
| sum() | Sum |
| count() | Count rows |
| current_timestamp() | Current timestamp |

---

# 14. Snowpark Best Practices

## Recommended Practices

- Use pushdown optimization
- Avoid unnecessary collect()
- Use DataFrame APIs instead of raw SQL where possible
- Use permanent stages for reusable files
- Use stored procedures for orchestration
- Select only required columns

---

# 15. Exam Tips

## Important Topics for SnowPro Exam

### Must Know

- Snowpark architecture
- Lazy evaluation
- DataFrames
- UDF vs UDTF
- Stored procedures
- Pushdown optimization
- Snowpark supported languages
- Difference between Snowpark and Spark
- Actions vs transformations

---

# 16. Important Snowpark Commands

## Create DataFrame

```python
df = session.create_dataframe(
    [[1, "John"], [2, "Mike"]],
    schema=["ID", "NAME"]
)
```

## Join DataFrames

```python
joined = df1.join(df2, df1["ID"] == df2["ID"])
```

## Group By

```python
df.group_by("DEPARTMENT").agg(sum("SALARY"))
```

---

# 17. Sample Snowpark Python Programs

## Example 1: Filter Employees

```python
from snowflake.snowpark.functions import col

employees = session.table("EMPLOYEE")

high_salary = employees.filter(col("SALARY") > 10000)

high_salary.show()
```

## Example 2: Aggregate Data

```python
from snowflake.snowpark.functions import avg

result = (
    employees.group_by("DEPARTMENT")
             .agg(avg("SALARY"))
)

result.show()
```

---

# 18. Frequently Asked SnowPro Exam Questions

## Q1. What is Snowpark?
Snowpark is a developer framework for building data pipelines and applications inside Snowflake using Python, Java, and Scala.

## Q2. What is lazy evaluation?
Transformations are not executed immediately. Execution happens only when an action is called.

## Q3. Where does Snowpark processing occur?
Processing occurs inside Snowflake virtual warehouses.

## Q4. What is the difference between UDF and UDTF?

| UDF | UDTF |
|---|---|
| Returns single value | Returns multiple rows |
| Scalar output | Tabular output |

---

# Quick Revision Notes

- Snowpark uses DataFrames
- Execution happens inside Snowflake
- Supports Python, Java, Scala
- Lazy evaluation improves optimization
- Actions trigger execution
- UDF returns scalar value
- UDTF returns rows

---

# Conclusion

Snowpark is a modern developer framework that extends Snowflake capabilities beyond SQL. It enables scalable data engineering, machine learning, and application development while leveraging Snowflake’s performance, security, and governance.
