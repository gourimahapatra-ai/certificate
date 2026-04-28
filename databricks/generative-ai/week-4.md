<details><summary>AI System Monitoring & Deployment (GenAI)</summary> 
  
## AI Lifecycle Stages
### 1. System Development
- Uses **static data**
- Focus on:
  - Model building
  - Experimentation
  - Testing in controlled environments

### 2. Deployment & Production
- Handles **continuously changing data**
- Focus on:
  - Real-time inference
  - Monitoring
  - Feedback loops
  - Model updates

### 🤔 Your AI System is Ready — Then What?
- Monitor performance continuously
- Handle data drift & model drift
- Retrain and improve models
- Ensure reliability, scalability, and cost optimization

---

# Packaging Models & Pipelines (GenAI Deployment)

## How ML Logic is Packaged in GenAI
With LLM-based systems, "models" can take multiple forms:

- **Engineered Prompts**
  - Stored as reusable templates

- **Chains**
  - Built using frameworks like:
    - LangChain
    - LlamaIndex

- **LLM API Calls**
  - Internal/self-hosted models (e.g., DBRX)
  - External providers (e.g., OpenAI)

- **Custom Hosted APIs**
  - Fine-tuned models
  - Pretrained models

- **Local Execution**
  - Hugging Face pipelines
  - GPU-based inference

💡 All of these are considered **models/pipelines** in GenAI systems.

---

# MLflow Components

## Key Capabilities
- End-to-end ML & GenAI lifecycle management:
  - Development → Deployment → Monitoring
- Unified platform for:
  - Traditional ML
  - Generative AI
- Supports:
  - GenAI-specific model flavors
  - Evaluation metrics

💡 Recommendation:
- Use **Model Registry in Unity Catalog** for governance and lifecycle management

---

# MLflow Model ("Flavor")

## What is an MLflow Model?
- A **directory structure** containing:
  - Model artifacts
  - `MLmodel` configuration file

## MLModel File
- Defines **multiple flavors** of the model
- Enables compatibility across tools

## Example Structure

<img width="168" height="218" alt="image" src="https://github.com/user-attachments/assets/68d6eb11-cdf3-4154-9f73-11712211f4c4" />


## Example MLModel Config
- artifact_path: chain
- flavors:
- langchain:
- langchain_version: 0.1.5
- model_data: model
- python_function:
vloader_module: mlflow.langchain

# LangChain Flavor
- Standard format to package **LLM chains**
- Enables:
  - Reusability
  - Deployment compatibility
  - Integration with MLflow ecosystem

# Python Function Flavor (`mlflow.pyfunc`)

## Overview
- Default interface for MLflow models
- Treats models as **Python functions**

## Key Features
- Loadable as a Python function
- Deployment-ready abstraction
- Includes everything needed to:
  - Load
  - Execute
  - Predict

## Common Functions
- `log_model`
- `save_model`
- `load_model`
- `predict`

---

# Model Flavors

## Purpose
- Define how a model can be:
  - Loaded
  - Interpreted
  - Deployed

## Built-in Flavors
- LangChain
- OpenAI
- HuggingFace Transformers
- PyTorch
- TensorFlow
- ONNX
- Python Function (`pyfunc`)

---

# MLflow + Unity Catalog Lifecycle

## Workflow Overview

### 1. Model / Chain Building
- Develop models or LLM chains

### 2. Tracking & Evaluation
- Track:
  - Parameters
  - Metrics
  - Artifacts

### 3. Model Registry
- Version control:
  - v1 → v2 → v3
- Manage:
  - Metadata
  - Governance

### 4. Deployment
- Seamless deployment using MLflow integration

---

## Key Concepts
- **Champion Model** → Current production model
- **Challenger Model** → New candidate for replacement
- Continuous evaluation ensures best model is deployed

---

# Summary
- GenAI systems extend traditional ML pipelines with:
  - Prompts
  - Chains
  - APIs
- MLflow provides:
  - Standardized packaging (flavors)
  - Lifecycle management
  - Deployment capabilities
- Unity Catalog enhances:
  - Governance
  - Model registry
  - Collaboration

# Unity Catalog (UC)

## Overview
**Unity Catalog (UC)** is a **single governance solution** for managing data and AI assets across the Lakehouse.

## Key Capabilities
- Centralized governance for:
  - Data
  - Models
  - AI assets
- Fine-grained access control (ACLs)
- Data and model lineage tracking
- Secure collaboration across teams

---

# MLflow + Unity Catalog Model Registry

## Core Features
- **Model Lifecycle Management**
  - Versioning support (v1, v2, v3...)
  - Aliases for stages:
    - `@champion` → Production model
    - `@challenger` → Candidate model

- **Centralized Model Store**
  - Store and organize all models in one place

- **Collaboration & Access Control**
  - Role-based permissions (ACLs)
  - Team collaboration

- **Full Model Lineage**
  - Track:
    - Data sources
    - Training runs
    - Dependencies

- **Tagging & Annotations**
  - Add metadata for:
    - Searchability
    - Organization
    - Documentation

---

# MLflow and GenAI Deployment

## Benefits of MLflow

### 1. Environment Consistency
- Ensures **deployment environment = training environment**
- Avoids dependency mismatches

### 2. Reproducibility
- Models run consistently:
  - Across environments
  - Across platforms

### 3. Complete Packaging
- Includes:
  - Code
  - Dependencies
  - Configurations
- No missing components during deployment

### 4. Seamless Deployment
- One-click or automated deployment pipelines
- Reduced operational overhead

### 5. Built-in Serving
- Local serving via:
  - **Flask Server**
  - **MLServer**

### 6. Cloud Deployment Support
- Deploy to:
  - Major cloud providers
  - Databricks Model Serving

---

# Summary

- **Unity Catalog**
  - Central governance layer for data + AI
  - Enables security, lineage, and collaboration

- **MLflow Model Registry (with UC)**
  - Manages full model lifecycle
  - Supports versioning, aliases, and metadata

- **MLflow Deployment**
  - Ensures consistency, reproducibility, and scalability
  - Simplifies GenAI deployment across environments
 
  
# GenAI Deployment Paradigms

## Overview
Deployment paradigms in Generative AI define **how and when** model outputs (completions) are generated.

They are similar to traditional ML deployment patterns but adapted for:
- Prompts
- LLM inference
- Real-time interactions

---

# Types of Deployment Paradigms

## 1. Batch Processing
- Generate and **store completions** for a large set of inputs/prompts
- Executed on:
  - Tables
  - Predefined datasets

### Characteristics
- High throughput
- High latency (hours to days)
- Suitable for offline processing

### Example
- Summarizing financial reports
- Generating bulk insights

---

## 2. Streaming Processing
- Generate completions on **micro-batches**
- Data is processed continuously as it arrives

### Characteristics
- Moderate throughput
- Moderate latency (seconds to minutes)
- Near real-time processing

### Example
- Personalizing marketing messages
- Event-driven recommendations

---

## 3. Real-time Processing
- Generate completions **asynchronously per request**
- Each prompt is handled individually

### Characteristics
- Low latency (milliseconds)
- Variable throughput (depends on scaling)
- Interactive systems

### Example
- Chatbots (customer support, assistants)
- Document Q&A systems

---

## 4. Edge / Embedded Deployment
- Run models **on-device** (e.g., mobile, IoT, car systems)

### Characteristics
- Low latency (device-dependent)
- Low throughput
- Limited by:
  - Memory
  - Compute power

⚠️ Note:
- Challenging for **large language models (LLMs)** due to:
  - Large size
  - High resource requirements

### Example
- Voice-controlled car systems (e.g., adjusting AC temperature)

---

# Key Trade-offs

## Latency vs Throughput
- **Batch**
  - ⬆ Throughput
  - ⬆ Latency

- **Streaming**
  - ⚖ Balanced throughput & latency

- **Real-time**
  - ⬇ Latency
  - ⚖ Variable throughput

- **Edge**
  - ⬇ Latency
  - ⬇ Throughput

---

# Comparison Table

| Deployment Method | Throughput | Latency | Example Application |
|------------------|-----------|--------|---------------------|
| **Batch**        | High      | High (hours–days) | Financial report summarization |
| **Streaming**    | Moderate  | Moderate (sec–min) | Marketing personalization |
| **Real-time**    | Low–High  | Low (ms) | Chatbots, assistants |
| **Edge/Embedded**| Low       | Low (device-based) | Voice control in cars |

# Summary

- Deployment choice depends on:
  - Use case
  - Latency requirements
  - Scale (throughput)
- GenAI extends traditional ML with:
  - Prompt-based inference
  - Real-time interaction needs
- Trade-offs are critical:
  - Faster response → lower throughput
  - Higher scale → increased latency

# Batch Deployment (GenAI)

## Overview
Batch deployment processes **large volumes of prompts at once** and generates outputs that are stored for later use.

---

## Advantages

- 💰 **Cheapest Deployment Method**
  - Cost-efficient due to bulk processing
  - Optimized resource utilization

- ⚙️ **Ease of Implementation**
  - Simple architecture
  - No need for real-time infrastructure

- 📊 **Efficient per Data Point**
  - Processes data in bulk → lower cost per request

- 📈 **High Throughput**
  - Can handle **very large datasets**
  - Ideal for offline workloads

---

## Disadvantages

- ⏳ **High Latency**
  - Results may take:
    - Hours
    - Days

- 💤 **Stale Data**
  - Outputs may become outdated quickly
  - Not suitable for time-sensitive use cases

- 🚫 **Not Suitable for Dynamic Data**
  - Cannot adapt to rapidly changing inputs

- ❌ **Not for Streaming or Real-time**
  - No immediate response capability
  - Poor fit for interactive systems

---

## When to Use Batch Deployment

✅ Best suited for:
- Report generation
- Large-scale summarization
- Historical data analysis
- Offline AI pipelines

❌ Avoid when:
- Real-time response is required
- Data changes frequently
- User interaction is involved

---

## Summary

Batch deployment is:
- ✔ Cost-effective
- ✔ Scalable for large data
- ✖ Slow (high latency)
- ✖ Not real-time

👉 Ideal for **offline, high-volume processing**, but not for **interactive AI applications**


# Batch Deployment — OSS Integrations

## Overview
Batch inference in GenAI can be significantly optimized using **open-source (OSS) tools** that improve:
- Performance
- Scalability
- GPU utilization

---

## 1. TensorRT™

### Description
- High-performance **SDK from NVIDIA**
- Optimized for **GPU-based batch inference**
- Works well with **TensorFlow models**

### Key Features
- Accelerates inference using:
  - Graph optimizations
  - Precision calibration (FP16, INT8)
- Reduces latency and increases throughput in batch jobs

### Use Cases
- Large-scale batch inference on GPUs
- Production-grade deep learning pipelines

### Notes
- Databricks provides **notebook examples** for integration

---

## 2. vLLM

### Description
- Library designed for **Transformer/LLM inference**
- Supports:
  - NVIDIA GPUs
  - AMD GPUs

### Key Features
- Memory-efficient inference
- Optimized for **LLM workloads**
- Uses techniques like:
  - Paged attention
  - Efficient KV cache management

### Supported Models (Examples)
- DBRX
- Mixtral 8x-7B
- Mistral-7B

### Use Cases
- Batch processing of LLM prompts
- High-throughput GenAI inference

### Notes
- Databricks provides **ready-to-use notebooks**

---

## 3. Ray on Spark (AWS | Azure | GCP)

### Description
- Distributed computing framework for **parallelizing Python workloads**
- Combines:
  - Ray (distributed execution)
  - Apache Spark (data processing)

### Key Features
- Pythonic APIs for:
  - Parallel execution
  - Task distribution
- Scales across:
  - Multi-node clusters
  - Cloud environments

### Use Cases
- Large-scale batch inference pipelines
- Distributed GenAI workloads
- Parallel prompt processing

---

## Summary

| Tool            | Focus Area                     | Strength |
|-----------------|------------------------------|---------|
| **TensorRT**    | GPU optimization              | High-performance inference |
| **vLLM**        | LLM inference                 | Memory-efficient, fast |
| **Ray on Spark**| Distributed computing         | Massive scalability |

---

## Key Takeaway
- Batch deployment can be enhanced using OSS tools to:
  - Improve performance
  - Reduce cost
  - Scale efficiently

👉 Choose the tool based on:
- Model type (DL vs LLM)
- Infrastructure (GPU vs distributed cluster)
- Scale requirements


# Real-time Deployment (GenAI)

## Overview
Real-time deployment refers to serving machine learning or GenAI models in **production environments** where:

- Predictions are generated **instantly**
- Each request is processed **individually**
- Responses are returned in **milliseconds**

---

## Why Real-time Deployment Matters

- ⚡ **Low Latency**
  - Immediate response to user input

- 🤖 **Interactive Applications**
  - Enables conversational AI and assistants

- ⏱ **Time-sensitive Decisions**
  - Critical for systems requiring instant action

- 📈 **Growing Importance in GenAI**
  - LLM-based applications increasingly require real-time inference

---

## Common Use Cases

- Chatbots & virtual assistants  
- Message intent detection  
- Content moderation  
- Autonomous systems  
- Document Q&A systems  

---

# Example Use Case: Real-time Intent Detection

## Description
Real-time classification of social media posts using a **fine-tuned LLM**

## Scenario
- A large language model is deployed via a **REST API**
- Incoming social media posts are:
  - Sent to the model instantly
  - Classified in real time

## Workflow
1. User submits a post  
2. API sends request to LLM  
3. Model processes input  
4. Classification returned immediately  
5. Action triggered based on result  

## Example Actions
- 🚫 Toxic / harmful content → Removed  
- ✅ Safe content → Published  

---

## Key Requirements

- ⚡ **Low Latency**
  - Responses in milliseconds

- 🔁 **High Availability**
  - 24/7 uptime

- 📊 **Continuous Monitoring**
  - Track:
    - Performance
    - Errors
    - Drift

- 📈 **Scalability**
  - Handle varying traffic loads

---

## Advantages

- Instant predictions  
- Supports real-time user interaction  
- Enables automation of critical decisions  

---

## Challenges

- Higher infrastructure cost  
- Requires robust scaling mechanisms  
- Sensitive to latency spikes  
- Needs strong monitoring and alerting  

---

## Summary

Real-time deployment is:
- ✔ Fast and responsive  
- ✔ Essential for interactive GenAI apps  
- ✖ More complex and costly than batch  

👉 Best suited for **low-latency, user-facing, and time-critical applications**

</details>

<details><summary>Real-time Deployment (GenAI)</summary> 

## Overview
Real-time deployment refers to serving machine learning or GenAI models in **production environments** where:

- Predictions are generated **instantly**
- Each request is processed **individually**
- Responses are returned in **milliseconds**


## Why Real-time Deployment Matters

- ⚡ **Low Latency**
  - Immediate response to user input

- 🤖 **Interactive Applications**
  - Enables conversational AI and assistants

- ⏱ **Time-sensitive Decisions**
  - Critical for systems requiring instant action

- 📈 **Growing Importance in GenAI**
  - LLM-based applications increasingly require real-time inference

## Common Use Cases

- Chatbots & virtual assistants  
- Message intent detection  
- Content moderation  
- Autonomous systems  
- Document Q&A systems  


# Example Use Case: Real-time Intent Detection

## Description
Real-time classification of social media posts using a **fine-tuned LLM**

## Scenario
- A large language model is deployed via a **REST API**
- Incoming social media posts are:
  - Sent to the model instantly
  - Classified in real time

## Workflow
1. User submits a post  
2. API sends request to LLM  
3. Model processes input  
4. Classification returned immediately  
5. Action triggered based on result  

## Example Actions
- 🚫 Toxic / harmful content → Removed  
- ✅ Safe content → Published  


## Key Requirements

- ⚡ **Low Latency**
  - Responses in milliseconds

- 🔁 **High Availability**
  - 24/7 uptime

- 📊 **Continuous Monitoring**
  - Track:
    - Performance
    - Errors
    - Drift

- 📈 **Scalability**
  - Handle varying traffic loads


## Advantages

- Instant predictions  
- Supports real-time user interaction  
- Enables automation of critical decisions  


## Challenges

- Higher infrastructure cost  
- Requires robust scaling mechanisms  
- Sensitive to latency spikes  
- Needs strong monitoring and alerting  


## Summary

Real-time deployment is:
- ✔ Fast and responsive  
- ✔ Essential for interactive GenAI apps  
- ✖ More complex and costly than batch  

👉 Best suited for **low-latency, user-facing, and time-critical applications**

</details>


<details><summary>Production-Grade Serving (Databricks Model Serving)</summary> 

## Overview
Production-grade serving enables **highly available, low-latency, and scalable** deployment of ML and GenAI models for real-time applications.


# Key Capabilities

## 🚀 High Performance Serving
- ⚡ Low latency (real-time responses)
- 📈 Scalable for small → large workloads
- 🌐 Highly available (production-ready)

---

## 🏗 Lakehouse-Unified Serving

### Features
- Automatic **feature lookups**
- Built-in **monitoring**
- Unified **governance** via Unity Catalog

### Benefits
- Reduces deployment errors  
- Simplifies architecture  
- Automates serving workflows  

---

## ⚙️ Simplified Deployment

- Deploy via:
  - UI
  - API
- Minimal operational overhead
- Faster time-to-production

---

# Databricks Model Serving

## What It Is
A **serverless, production-ready solution** for deploying ML/GenAI models in real time.

---

## How It Works

### Flow
1. Model registered in **Unity Catalog (UC)**
2. Deployed as a **real-time endpoint**
3. Accessed via **API calls**
4. Returns predictions instantly

---

## Core Features

- 🌐 **API-based Deployment**
  - Integrate with apps, websites, services

- 📊 **Built-in Logging**
  - Capture request-response payloads

- 🔍 **Observability**
  - Monitor:
    - Latency
    - Errors
    - System performance

- ⚡ **Serverless Compute**
  - No infrastructure management
  - Auto-scaling enabled

---

# Benefits

- 💰 **Reduced Operational Costs**
- 🔄 **Streamlined ML Lifecycle**
- 🎯 Focus on business logic (not infra)
- 📈 Scales automatically
- 🔌 Works with:
  - Custom models
  - Foundation models
  - External APIs

---

# Advanced Capabilities

## 🧪 A/B Testing & Canary Deployments
- Serve multiple models under one endpoint
- Compare:
  - Performance
  - Accuracy
- Safely roll out new models

---

## 📊 Inference Tables (Monitoring & Debugging)

### What They Are
- Store **request-response pairs** in **Delta tables (Unity Catalog)**

### Use Cases
- 🔁 Retraining / fine-tuning datasets  
- 🐞 Debugging incorrect predictions  
- 🏷 Identify and collect mislabelled data  
- 📉 Analyze model performance over time  

---

# Architecture Summary
Models in UC
↓
Real-time Endpoint Serving
↓
API Calls
↓
Predictions + Logging (Inference Tables)


---

# Summary

Production-grade serving with Databricks provides:

- ✔ Scalable, low-latency APIs  
- ✔ Simplified deployment (UI/API)  
- ✔ Built-in monitoring & governance  
- ✔ Serverless + autoscaling infrastructure  
- ✔ Advanced testing (A/B, canary)  

👉 Enables teams to **focus on AI value delivery** instead of infrastructure complexity

# Lakehouse Monitoring (Databricks)

## Overview
**Lakehouse Monitoring** provides **automated insights and out-of-the-box metrics** for:
- Data pipelines
- Machine Learning models
- GenAI systems

Built on **Unity Catalog**, it enables **end-to-end monitoring** across the AI lifecycle.

---

# Key Features

## ⚙️ Fully Managed
- No infrastructure management required
- No need to:
  - Manually calculate metrics
  - Build dashboards from scratch

---

## ⚡ Frictionless Setup
- Easy to enable monitoring
- Comes with:
  - Predefined metrics
  - Auto-generated dashboards

---

## 🔄 Unified Monitoring
- Single solution for:
  - Data
  - Models
- Provides **holistic visibility** across pipelines

---

# Monitoring Capabilities

## For Each Monitored Table

- 📊 **Profile Metrics Table**
  - Data distribution
  - Summary statistics

- 🔄 **Drift Metrics Table**
  - Detects changes over time
  - Identifies data/model drift

- 🧮 **Custom Metrics**
  - Defined using SQL expressions

- 📈 **Auto-generated Dashboards**
  - Built using DBSQL
  - Visualize trends over time

- 🔐 **Automatic PII Detection**
  - Identifies sensitive data

- ✅ **Input Expectations & Rules**
  - Data quality validation

---

# Architecture

## Core Design
- Built on **Unity Catalog**
- Runs as a **background service**
- Incrementally processes data from monitored tables

---

# Monitoring Model Responses (GenAI)

## Goal
Ensure **quality monitoring of production data and model outputs**

---

## Workflow Steps

### 1. Process Inference Data
- Unpack inference tables
- Compute LLM evaluation metrics
- Store results in **processed payload table**

💡 Typically implemented as:
- Triggered streaming job

---

### 2. Enable Monitoring
- Apply Lakehouse Monitoring on:
  - Processed payload tables

---

### 3. Analyze & Alert
- Use dashboards to:
  - Track metrics
- Create **SQL alerts** for:
  - Threshold breaches
  - Anomalies

---

# Data Flow Architecture

Model / Chain
↓
Inference Table
↓
Raw / Processed Tables (UC Volume)
↓
Processed Payload Table
↓
Metrics Tables
↓
Lakehouse Monitoring Dashboards


---

# Lakehouse Monitoring Workflows

## 1. Development Stage
- Integrate monitoring into:
  - Project pipelines
- Define metrics early

---

## 2. Testing Stage
- Validate monitoring setup using:
  - Integration tests
- Ensure metrics are correctly generated

---

## 3. Production Stage
- Deploy monitoring with:
  - Baseline tables
- Store monitoring data in:
  - Production Unity Catalog

---

# Best Practices

1. 📊 Set up monitoring for **all components**
2. ⚖️ Balance **model cost vs performance**
3. 🔄 Refresh dashboards regularly
4. 🚨 Configure **alerts for key metrics**
5. 🔁 Trigger **retraining/reprocessing** based on performance

---

# Summary

Lakehouse Monitoring provides:

- ✔ Automated insights for data & AI systems  
- ✔ Built-in metrics, dashboards, and alerts  
- ✔ Unified monitoring across pipelines  
- ✔ Seamless integration with Unity Catalog  

👉 Enables **proactive monitoring**, faster debugging, and continuous improvement of AI systems

# Multi-Environment Setup for AI Systems (MLOps / LLMOps)

## Overview
To build reliable AI systems, workflows are separated into **multiple environments**:

- Development
- Staging
- Production

Each environment serves a **specific purpose** in the lifecycle of data, models, and applications.

---

# Environment Definitions

## 🧪 Development (Dev)
- Used by:
  - Data Scientists
  - AI Engineers

### Purpose
- Exploration (EDA)
- Experimentation
- Prototyping models and pipelines

### Activities
- Data preparation
- Model development
- Prompt engineering (GenAI)
- Initial testing

---

## 🧩 Staging
- Used by:
  - ML Practitioners
  - QA teams

### Purpose
- Validate and test solutions before production

### Activities
- Unit testing
- Integration testing
- Performance testing
- Risk mitigation

---

## 🚀 Production (Prod)
- Used by:
  - ML Engineers
  - Operations teams

### Purpose
- Deploy and monitor live AI systems

### Activities
- Model serving
- Real-time inference
- Monitoring & alerting
- Feedback collection

---

# Multi-Environment Semantics

| Environment | Role | Key Users |
|------------|------|----------|
| Dev        | Build & experiment | Data Scientists |
| Staging    | Test & validate    | ML Engineers / QA |
| Production | Deploy & monitor  | Ops / ML Engineers |

---

# Workspace Strategy

## 1. Direct Separation (Recommended for Scale)

### Approach
- Separate **Databricks workspaces** for:
  - Dev
  - Staging
  - Production

### Pros
- Simpler environments
- Better isolation
- Scales well for multiple projects

---

## 2. Indirect Separation

### Approach
- Single workspace with logical separation

### Pros
- Simpler infrastructure

### Cons
- Complex environment management
- Harder to scale
- Permission challenges

---

# Deployment Patterns

## ❌ Deploy Model (Traditional Approach)

### Flow
- Train model in Dev
- Move **model artifact** across:
  - Dev → Staging → Prod

### Limitations
- Separate handling required for:
  - Inference code
  - Monitoring pipelines
- Less flexible and harder to maintain

---

## ✅ Deploy Code (Recommended - MLOps)

### Flow
- Code moves across environments:
  - Dev → Staging → Prod
- Training happens **independently in each environment**

### Benefits
- Consistent pipelines
- Better reproducibility
- Easier CI/CD integration
- Scalable architecture

---

# MLOps Stack (Databricks)

## Core Components

### 🗂 Data Layer
- **Delta Lake**
  - Reliable data storage
  - Data quality & sharing

- **Unity Catalog**
  - Governance
  - Security
  - Metadata management

---

### 🧠 AI Development Lifecycle

1. EDA & Data Preparation  
2. Model Development  
3. Model Validation  
4. Model Serving  
5. Monitoring  

---

### ⚙️ Engineering & Automation

- **Repos**
  - Version control
  - Code collaboration

- **Workflows**
  - DAG-based orchestration
  - Job scheduling

- **Databricks Asset Bundles**
  - Infrastructure as Code (IaC)
  - CI/CD with YAML

---

### 🚀 Deployment & Monitoring

- Model Registry  
- Model Serving  
- Lakehouse Monitoring  

---

# Unified Platform Benefits

- Combines:
  - DataOps
  - DevOps
  - ModelOps

- Provides:
  - Unified governance
  - Centralized data & model management
  - Scalable AI lifecycle

---

# Recommended LLMOps Architecture

## Code Management
- Single **central repository**
- Used across all environments

---

## Environment Roles

### 🧪 Development
- EDA
- Prototyping
- Initial pipeline setup

---

### 🧩 Staging
- Testing:
  - Unit tests
  - Integration tests
  - Performance validation

---

### 🚀 Production
- Live AI systems
- Monitoring
- Human feedback collection

---

## Data/System Component Management

- Centralized management layer
- Environment-specific catalogs
- Ensures:
  - Isolation
  - Governance
  - Consistency

---

# Summary

- Multi-environment setup ensures:
  - Reliability
  - Scalability
  - Safe deployments

- **Deploy Code (not just models)** is the recommended approach

- Databricks enables:
  - Unified MLOps + LLMOps
  - End-to-end lifecycle management

👉 Key idea:  
**Build in Dev → Test in Staging → Deploy in Production → Monitor continuously**

</details>


<details><summary>What About LLMOps?</summary> 

## Overview
**LLMOps** extends traditional **MLOps** to support **Generative AI (LLMs)** by introducing new patterns around:
- Prompts
- Chains
- APIs
- Human feedback loops

It focuses on managing the **end-to-end lifecycle of LLM-based applications**.

---

# Key Areas: MLOps vs LLMOps

## 1. Dev Patterns

### MLOps
- Model-centric workflows
- Training, tuning, validation
- Static datasets

### LLMOps
- Prompt-centric + model-centric
- Prompt engineering & iteration
- Use of:
  - RAG (Retrieval-Augmented Generation)
  - Agents
  - Chains (LangChain, etc.)

---

## 2. Packaging

### MLOps
- Package:
  - Trained model artifact
  - Dependencies

### LLMOps
- Package entire application:
  - Prompts (templates)
  - Chains / pipelines
  - Retrieval systems (vector DBs)
  - External APIs (LLM providers)

👉 Applications are **composed systems**, not just models

---

## 3. Serving

### MLOps
- Batch or real-time model serving
- Predictions returned from model endpoints

### LLMOps
- Real-time LLM inference via:
  - APIs (OpenAI, hosted models)
  - Custom endpoints
- May include:
  - Multi-step pipelines (RAG, agents)

---

## 4. API Governance

### MLOps
- Control access to model endpoints

### LLMOps
- Manage multiple APIs:
  - LLM providers
  - Embedding services
  - Retrieval systems

### Focus Areas
- Authentication & authorization
- Rate limiting
- Usage tracking
- Security of external dependencies

---

## 5. Cost & Performance

### MLOps
- Focus on:
  - Model accuracy
  - Training cost

### LLMOps
- Continuous monitoring of:
  - Token usage (cost driver)
  - Latency (real-time apps)
  - Output quality

### Trade-offs
- Cost vs response quality
- Latency vs complexity (RAG, agents)

---

## 6. Human Feedback

### MLOps
- Limited human-in-the-loop
- Mostly offline evaluation

### LLMOps
- Critical component
- Includes:
  - User feedback
  - Reinforcement learning (RLHF)
  - Annotation & correction loops

### Use Cases
- Improve prompt quality
- Fine-tune models
- Detect hallucinations

---

# Comparison Summary

| Area | MLOps | LLMOps |
|------|------|--------|
| Dev Patterns | Model training | Prompt + pipeline design |
| Packaging | Model artifact | Full AI system (prompts, chains, APIs) |
| Serving | Model endpoints | LLM APIs + pipelines |
| API Governance | Internal endpoints | Multiple external APIs |
| Cost & Performance | Accuracy-focused | Token cost + latency + quality |
| Human Feedback | Limited | Central to improvement |

---

# Key Takeaways

- LLMOps is **system-oriented**, not just model-oriented  
- Introduces:
  - Prompt engineering
  - Retrieval systems
  - API orchestration  
- Requires:
  - Strong monitoring
  - Cost control
  - Human feedback loops  

---

# Final Insight

👉 Traditional ML:
**Train → Deploy → Predict**

👉 LLMOps:
**Design Prompt → Orchestrate Pipeline → Serve via APIs → Collect Feedback → Iterate Continuously**

# LLMOps — Development Patterns & Packaging

## Overview
In LLMOps, both **development patterns** and **packaging** differ significantly from traditional MLOps due to:
- Use of LLMs (external/internal)
- Prompt-driven workflows
- Multi-component AI systems

---

# 🧪 Development Patterns in LLMOps

## 1. Incremental Development Approach

### Concept
- Start simple → gradually increase complexity

### Typical Progression
1. Use **off-the-shelf LLM APIs** (e.g., GPT, DBRX)
2. Enhance with **RAG (Retrieval-Augmented Generation)**
3. Apply **fine-tuning**
4. Move to **pre-training/custom models** (if needed)

### Benefits
- Faster prototyping
- Reduced initial cost
- Flexibility to scale complexity

---

## 2. Prompt & Template-Centric Development

### Concept
- Prompts are treated as **first-class components**

### Key Elements
- Text templates define:
  - Instructions
  - Context
  - Output format

### Requirements
- Versioning of prompts
- Continuous iteration
- Testing prompt effectiveness

### Example
```text
"You are an assistant. Summarize the following text in bullet points: {input}"

# Serving Applications in LLMOps

## Overview
Serving in LLMOps goes beyond traditional model endpoints. It involves deploying **complete AI applications** that include:

- LLMs
- Retrieval systems
- Infrastructure
- User-facing components

---

# Key Components in LLMOps Serving

## 1. Vector Databases (RAG Systems)

### Why Needed
- LLMs lack real-time or domain-specific knowledge
- Require **context augmentation**

### Role
- Store embeddings of documents/data
- Retrieve relevant context for prompts

### Flow
```text
User Query → Embedding → Vector DB → Relevant Context → LLM → Response

# LLMOps Serving — Key Components & Impact

## 📊 Impact of LLMOps Serving

- Improves accuracy  
- Reduces hallucinations  
- Enables domain-specific applications  

---

# 2. GPU Infrastructure

## Why Needed
- LLMs are:
  - Large  
  - Compute-intensive  

---

## Requirements

### GPUs for:
- Fast inference  
- Low latency  

### Scalable Infrastructure:
- Autoscaling clusters  
- Distributed inference  

---

## Challenges
- High cost  
- Resource management complexity  

---

# 3. User Interface Components

## Concept
- LLM applications are often **user-facing**

---

## Examples
- Chat interfaces  
- Dashboards  
- Web/mobile apps  

---

## Deployment Consideration
- UI may be:
  - Integrated with backend serving  
  - Managed separately  

---

## Importance
- Directly impacts:
  - User experience  
  - Adoption  
  - Feedback collection  

---

# LLMOps vs MLOps (Serving Comparison)

| Aspect | MLOps | LLMOps |
|------|------|--------|
| Serving Unit | Model endpoint | Full AI application |
| Infrastructure | CPU/GPU optional | GPU-heavy |
| Data Access | Static features | Dynamic retrieval (RAG) |
| Components | Model only | Model + DB + APIs + UI |

User Interface
↓
API Layer
↓
Orchestration (Chain / Logic)
↓
Vector DB (Context Retrieval)
↓
LLM (GPU Inference)
↓
Response to User


# End-to-End Serving Architecture


---

# Key Challenges

- Managing multiple components (LLM + DB + APIs)  
- Ensuring low latency at scale  
- High infrastructure cost (GPU-heavy)  
- Integration complexity

# API Governance in LLMOps

## Overview
In LLMOps, API governance is critical due to the **increased number of endpoints** used across:

- LLM providers  
- Embedding services  
- Vector databases  
- Internal APIs  

---

## 1. Managing Access to Endpoints

### Problem
- Multiple endpoints are created for different components

### Requirements
- Control who can:
  - Access APIs  
  - Invoke models  
  - Use system resources  

### Solutions
- Authentication (API keys, tokens)  
- Authorization (role-based access control)  
- Rate limiting  

---

## 2. Governing Application Usage

### Logging & Monitoring
- Track all API calls:
  - Request/response logs  
  - Usage patterns  

### Abuse Detection
- Identify:
  - Excessive usage  
  - Malicious inputs  
  - Unauthorized access  

---

## 3. Guardrails

### Purpose
- Prevent misuse of AI systems

### Examples
- Input filtering (toxic/unsafe prompts)  
- Output moderation  
- Rate limits and quotas  

---

## Impact of API Governance

- Improves security  
- Controls cost  
- Prevents abuse  
- Ensures compliance  

---

# Cost and Performance in LLMOps

## Overview
Cost and performance are tightly coupled in LLMOps due to:
- Large model sizes  
- API-based pricing  
- Real-time usage patterns  

---

## 1. Model Size Impacts Cost

### Problem
- Larger models:
  - Require more compute  
  - Increase inference cost  

### Impact
- Higher operational expenses  
- Need for optimization strategies  

---

## 2. API-Based Pricing (Token-Based)

### Concept
- Many LLM providers charge based on:
  - Number of input tokens  
  - Number of output tokens  

### Implications
- More usage → higher cost  
- Longer prompts → more expensive  

---

## 3. Cost Optimization Techniques

### Reduce Model Size
- Use smaller or distilled models  
- Choose right model for task  

---

### Reduce Number of Queries
- Avoid unnecessary API calls  
- Use:
  - Caching responses  
  - Reuse previous results  

---

### Optimize Input/Output
- Shorten prompts  
- Limit response length  
- Use structured outputs  

---

## Trade-offs

| Factor | Impact |
|-------|--------|
| Larger model | Better quality, higher cost |
| More tokens | Higher cost |
| More queries | Higher cost |
| Optimization | Lower cost, possible quality trade-off |

---

# Summary

## API Governance
- Control access to endpoints  
- Monitor usage  
- Implement guardrails  

## Cost & Performance
- Token-based pricing is key cost driver  
- Optimize:
  - Model size  
  - Query frequency  
  - Prompt length  

---

# Final Insight

👉 LLMOps requires balancing:

- 🔐 Governance (security & control)  
- 💰 Cost (token usage & infrastructure)  
- ⚡ Performance (latency & quality)  

to build **scalable and sustainable AI systems**

# Human Feedback in LLMOps

## Overview
Human feedback is a **core component** of LLMOps, enabling continuous improvement of:
- Model outputs  
- Prompt design  
- Overall system behavior  

Unlike traditional MLOps, feedback is **actively collected and reused** in the development loop.

---

# 1. Collection of Data

## Types of Feedback

### 👍 Explicit Feedback
- User-provided signals such as:
  - 👍 (satisfied)
  - 👎 (unsatisfied)

---

### 💬 User Queries
- Capture real user inputs:
  - Questions
  - Prompts
  - Interaction patterns  

---

### ✍️ Corrections & Suggestions
- Human-provided improvements:
  - Edited responses  
  - Suggested outputs  
  - Clarifications  

---

## Purpose
- Understand real-world usage  
- Identify failure cases  
- Detect hallucinations or inaccuracies  

---

# 2. Use of Data (Managed)

## Important
- Feedback must be:
  - Stored
  - Processed
  - Governed properly  

---

## Key Uses

### 📚 Response Examples
- Build datasets of:
  - Good responses  
  - Bad responses  
- Used for:
  - Fine-tuning  
  - Prompt optimization  

---

### 🧪 Testing
- Create evaluation datasets from:
  - Real user interactions  
- Improve:
  - Test coverage  
  - Edge case handling  

---

### 🏗 Architectural / Strategic Decisions
- Use insights to:
  - Improve system design  
  - Adjust pipelines (e.g., add RAG)  
  - Optimize prompts or models  

---

# Differences from MLOps

| Aspect | MLOps | LLMOps |
|------|------|--------|
| Feedback | Limited, offline | Continuous, user-driven |
| Data Source | Labeled datasets | Real user interactions |
| Usage | Model retraining | Prompt + system improvement |

---

# Feedback Loop in LLMOps
User Interaction
↓
Feedback Collection (👍 👎, corrections)
↓
Storage & Governance
↓
Analysis & Evaluation
↓
Improvements (Prompt / Model / Pipeline)
↓
Updated System


---

# Key Benefits

- Improves output quality  
- Reduces hallucinations  
- Aligns system with user expectations  
- Enables continuous learning  

---

# Challenges

- Managing feedback data at scale  
- Ensuring data quality  
- Handling biased or noisy feedback  
- Privacy and compliance concerns  

---

# Summary

Human feedback in LLMOps is:

- ✔ Continuous and user-driven  
- ✔ Essential for improvement  
- ✔ Used for:
  - Fine-tuning  
  - Testing  
  - System design  

---

# Final Insight

👉 LLM systems evolve through:

**User Interaction → Feedback → Improvement → Better Experience**

This creates a **continuous learning loop** essential for GenAI success

</details>


<details><summary>Databricks Asset Bundles (DAB)</summary> 


**Databricks Asset Bundles (DAB)** enable a **"write code once, deploy everywhere"** approach for managing and deploying data + AI projects.

They provide a **standardized, declarative way** to package and deploy:
- Code
- Configurations
- Resources

---

# What are Databricks Asset Bundles?

- A **project-based deployment framework**
- Defined using a `bundle.yml` file
- Managed via the **Databricks CLI**

---

# How Do Bundles Work?

## Core Workflow

1. Define project in `bundle.yml`
2. Use Databricks CLI to:
   - Validate bundle  
   - Deploy resources  
   - Run workflows  

---

## CLI Capabilities
- `validate` → Check configuration correctness  
- `deploy` → Deploy assets to environment  
- `run` → Execute workflows/jobs  

---

## Key Idea
👉 Everything (code + infra + configs) is defined in a **single declarative file**

---

# Role in Development & CI/CD

- Used during:
  - Development
  - Testing
  - CI/CD pipelines  

- Enables:
  - Automated deployments  
  - Environment consistency  
  - Faster iteration cycles  

---

# Benefits of Using DABs

## 🚀 Write Once, Deploy Anywhere
- Same project can be deployed across:
  - Dev
  - Staging
  - Production  

---

## 📦 Democratizing CI/CD Best Practices

### Co-versioning
- Store together:
  - Code  
  - Configurations  
  - Resources  

---

### 🤖 Automation Friendly
- CLI-based deployment
- Avoids:
  - Complex manual steps  
  - Hundreds of REST API calls  

---

### 🤝 Collaboration & Reliability
- Team collaboration with:
  - Version control  
  - Isolation between environments  
  - Automated testing  

---

## 🔄 Unified Deployment Approach
- Single way to:
  - Define projects  
  - Deploy assets  
  - Manage environments  

---

# Why DABs Matter in LLMOps / MLOps

- Simplifies **multi-environment deployments**
- Ensures **consistency across environments**
- Integrates with:
  - CI/CD pipelines  
  - Version control systems  

---

# Summary

Databricks Asset Bundles provide:

- ✔ Declarative project definition (`bundle.yml`)  
- ✔ CLI-based deployment (validate, deploy, run)  
- ✔ CI/CD integration  
- ✔ Environment consistency  

---

# Final Insight

👉 DABs bring **software engineering discipline** to data & AI projects by enabling:

**Reusable, versioned, and automated deployments across environments**
</details>


<details><summary></summary> 

</details>

<details><summary></summary> 

</details>
