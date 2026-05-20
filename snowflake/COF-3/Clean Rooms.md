# Snowflake Data Clean Rooms — SnowPro Core SC0‑03 Study Guide

## 1. What Are Data Clean Rooms?
Snowflake **Data Clean Rooms** enable multiple organizations to collaborate on data **without exposing raw, sensitive, or personally identifiable information (PII)**.

They allow partners to run **approved, privacy‑preserving analytics** while maintaining strict governance and compliance.

Use cases include:
- Advertising measurement  
- Joint customer analytics  
- Retailer–brand collaboration  
- Privacy‑safe data enrichment  

---

## 2. Key Principles of Data Clean Rooms

### **2.1 No Raw Data Sharing**
Participants never see each other’s underlying datasets.  
All access is controlled through secure Snowflake objects.

### **2.2 Policy‑Driven Access**
Data owners define:
- What queries are allowed  
- What aggregations are required  
- What outputs are permitted  
- What data must be masked or filtered  

### **2.3 Privacy‑Preserving Computation**
Snowflake enforces privacy using:
- **Row Access Policies**  
- **Dynamic Data Masking**  
- **Secure Views**  
- **Aggregation thresholds**  
- **Restricted UDFs**  

### **2.4 Multi‑Party Collaboration**
Multiple organizations can contribute data and run joint analytics while maintaining full control over their own datasets.

---

## 3. How Data Clean Rooms Work

1. **Data Providers** load their datasets into Snowflake.  
2. Providers define **governance rules** (policies, masking, allowed queries).  
3. **Consumers** run approved queries inside the clean room.  
4. Snowflake ensures:
   - No raw data is exposed  
   - Only compliant outputs are returned  
   - All actions are logged  

Clean Rooms rely heavily on Snowflake’s governance stack:
- Secure Views  
- Row Access Policies  
- Column‑level security  
- Data masking  
- Access History  

---

## 4. Clean Room Architecture Components

### **4.1 Secure Data Sharing**
Data is shared without copying using:
- Direct Shares  
- Listings  
- Reader Accounts  

### **4.2 Governance Controls**
- Row Access Policies  
- Dynamic Data Masking  
- Secure UDFs  
- Aggregation rules (e.g., minimum group size)  

### **4.3 Controlled Execution Environment**
Consumers can only run:
- Pre‑approved queries  
- Aggregated outputs  
- Restricted transformations  

### **4.4 Auditing & Monitoring**
Snowflake logs:
- Query history  
- Access history  
- Policy evaluations  

---

## 5. Clean Rooms vs Standard Data Sharing

| Feature | Data Clean Rooms | Standard Data Sharing |
|--------|------------------|------------------------|
| Raw data visible | **No** | Yes |
| Privacy controls | **Strong (policies, masking)** | Limited |
| Multi‑party collaboration | **Yes** | One‑to‑one |
| Output restrictions | **Yes** | No |
| Use cases | Privacy‑safe analytics | General data sharing |

---

## 6. Common Clean Room Use Cases

### **6.1 Advertising & Marketing**
- Attribution  
- Campaign measurement  
- Audience overlap analysis  

### **6.2 Retail & CPG**
- Joint customer insights  
- Product performance analysis  

### **6.3 Financial Services**
- Fraud detection  
- Risk modeling across institutions  

### **6.4 Healthcare**
- Research collaboration  
- Privacy‑safe clinical analytics  

---

## 7. Exam‑Relevant Facts

- Clean Rooms **prevent raw data exposure** between parties.  
- They rely on **Snowflake governance features** (RAPs, masking, secure views).  
- They support **multi‑party collaboration**.  
- They enforce **query restrictions and output controls**.  
- They are used for **privacy‑preserving analytics**, especially in regulated industries.  
- Clean Rooms often use **Reader Accounts** or **Listings** for controlled access.  

---

## 8. Summary
Snowflake Data Clean Rooms provide a secure, policy‑driven environment for organizations to collaborate on data without exposing sensitive information. They are built on Snowflake’s governance and security framework and are a key topic in the SnowPro Core SC0‑03 exam.

