
![alt text](image-78.png)

![alt text](image-79.png)
![alt text](image-77.png)
![alt text](image-81.png)

![alt text](image-82.png)

![alt text](image-83.png)

![alt text](image-84.png)

![alt text](image-85.png)

![alt text](image-86.png)

![alt text](image-87.png)

![alt text](image-88.png)

![alt text](image-89.png)

![alt text](image-90.png)

![alt text](image-91.png)

![alt text](image-92.png)

![alt text](image-93.png)

![alt text](image-94.png)

![alt text](image-95.png)

![alt text](image-96.png)

%sh
databricks bundle deploy -t development I

databricks bundle validate
databricks bundle deploy -t development

![alt text](image-97.png)

![alt text](image-98.png)

![alt text](image-99.png)

# Lookup Variables  
(Concise Databricks Professional Exam Summary)

Lookup variables allow you to **parameterize**, **template**, and **standardize** environment‑specific configurations across Databricks assets.  
They are especially useful in **CI/CD**, **multi‑workspace deployments**, and **environment promotion** (dev → test → prod).

You can define lookup variables for a wide range of Databricks objects:

---

## Supported Lookup Variable Types

- **[metastore](ca://s?q=Databricks_metastore_lookup_variable)**  
  Useful for switching between dev/test/prod metastores.

- **[notification_destination](ca://s?q=Databricks_notification_destination_lookup_variable)**  
  Email, Slack, Teams, or webhook destinations for alerts.

- **[pipeline](ca://s?q=Databricks_pipeline_lookup_variable)**  
  Reference different DLT pipelines per environment.

- **[query](ca://s?q=Databricks_query_lookup_variable)**  
  Swap SQL queries or query IDs dynamically.

- **[service_principal](ca://s?q=Databricks_service_principal_lookup_variable)**  
  Use different SPNs for each environment.

- **[warehouse](ca://s?q=Databricks_warehouse_lookup_variable)**  
  Map to different SQL warehouses (dev vs prod).

- **[alert](ca://s?q=Databricks_alert_lookup_variable)**  
  Parameterize alert definitions across workspaces.

- **[cluster_policy](ca://s?q=Databricks_cluster_policy_lookup_variable)**  
  Apply different cluster policies depending on environment.

- **[cluster](ca://s?q=Databricks_cluster_lookup_variable)**  
  Reference different compute clusters without hardcoding IDs.

- **[dashboard](ca://s?q=Databricks_dashboard_lookup_variable)**  
  Deploy dashboards across environments with dynamic IDs.

- **[instance_pool](ca://s?q=Databricks_instance_pool_lookup_variable)**  
  Swap instance pools for cost‑optimized environments.

- **[job](ca://s?q=Databricks_job_lookup_variable)**  
  Parameterize job IDs for CI/CD and workspace promotion.

---

## Why Lookup Variables Matter
Lookup variables help you:

- Avoid hardcoding IDs  
- Promote assets across workspaces cleanly  
- Maintain consistent configuration across environments  
- Reduce deployment errors  
- Simplify DevOps automation  

They are a key part of **Databricks Asset Bundles** and modern Databricks CI/CD workflows.

---

## Exam‑Ready Takeaway
Lookup variables allow you to **abstract environment‑specific IDs** for metastores, clusters, warehouses, pipelines, jobs, dashboards, and more.  
They make deployments **repeatable**, **portable**, and **environment‑aware**.

If you want, I can also create a **lookup variable cheat sheet** or a **Databricks CI/CD workflow summary**.  

![alt text](image-100.png)

![alt text](image-101.png)

![alt text](image-102.png)

![alt text](image-103.png)

![alt text](image-104.png)

![alt text](image-105.png)
![alt text](image-106.png)