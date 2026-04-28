# 🧠 A Brief History of AI Agents

## 🚀 Evolution of Agents

### 🔹 Early Agents
- Followed **predefined rules and paths**
- No real understanding of user intent
- Limited to scripted responses
- Could not adapt or learn dynamically

### 🔹 Modern Generative AI Agents
- Powered by **Large Language Models (LLMs)**
- Can:
  - Understand **natural language**
  - Interpret **user intent**
  - Make **context-aware decisions**
- Capable of:
  - Observing the environment
  - Acting using available tools
  - Achieving complex goals autonomously


### 🔹 Key Breakthroughs
- **Generative AI**
  - Enables human-like responses
  - Improves reasoning and flexibility

- **RAG (Retrieval-Augmented Generation)**
  - Combines LLMs with external data sources
  - Provides **accurate, up-to-date information**
  - Reduces hallucinations


## ⚙️ Core Components of an AI Agent

### 1. 🧩 Foundational Model
- The **brain of the agent**
- Typically an LLM (e.g., Gemini or others)
- Responsible for:
  - Understanding language
  - Reasoning
  - Generating responses
- Choice depends on:
  - Use case
  - Domain knowledge
  - Performance needs


### 2. 🔧 Tools
- Enable interaction with the **external world**
- Examples:
  - APIs
  - Databases (e.g., vector stores)
  - Function calls
- Allow the agent to:
  - Fetch real-time data
  - Perform actions
  - Extend capabilities beyond the model


## 🧠 Key Insight
> Modern AI agents are powerful because they combine:
- **Understanding (LLMs)**
- **Knowledge (RAG & data sources)**
- **Action (tools)**


## ✅ Summary
- AI agents evolved from **rule-based systems → intelligent autonomous systems**
- Generative AI made agents:
  - More flexible
  - More accurate
  - More human-like
- The combination of **models + tools + data** is what makes today’s agents truly powerful

# 🧠 Using Models in Generative AI Agents

## 🚀 Overview
- Generative AI agents are powered by **Generative AI Models (LLMs)**.
- These models act as the **brain** of the agent.
- Even after training, you can **optimize outputs** by tuning parameters and settings.

## 🎛️ Sampling Parameters & Settings

Sampling parameters are like **control knobs** that influence how a model responds.

They help you:
- Adjust creativity
- Control response length
- Maintain tone and accuracy

---

## 🔑 Key Parameters

### 1. 🔢 Token Count
- Tokens = **basic units of text**
  - Can be a word, part of a word, punctuation, or space
- Approximation:
  - **1 token ≈ 4 characters**
  - **100 tokens ≈ 60–80 words**

#### 📌 Important Notes:
- Models have **token limits**
- Higher token count:
  - ✅ Longer conversations
  - ❌ More compute required


### 2. 🌡️ Temperature
- Controls **randomness / creativity**

| Value | Behavior |
|------|--------|
| Low (0.1–0.3) | Deterministic, factual |
| Medium (0.5–0.7) | Balanced |
| High (0.8–1.0) | Creative, diverse |


### 3. 🎯 Top-p (Nucleus Sampling)
- Controls how much of the **probability distribution** is considered

#### 📌 Example:
- `Top-p = 0.9` → Select from top 90% probable words

#### ✅ Use Cases:
- Lower → More focused output  
- Higher → More diverse output  


### 4. 🛡️ Safety Settings
- Filters harmful or unsafe content
- Ensures:
  - Compliance
  - Responsible AI usage


### 5. 📏 Output Length
- Controls **response size**
- Helps:
  - Avoid overly long answers
  - Keep responses concise


## ⚙️ Practical Tuning Examples

### 🎯 For Factual Answers:
- Low temperature
- Low top-p
- Short output length

### 🎨 For Creative Tasks:
- High temperature
- Higher top-p
- Longer output length


## 🔌 Accessing Models via APIs

### 📡 What is an API?
- API = **Application Programming Interface**
- Allows systems to **communicate and exchange data**

### 🧩 How It Works:
1. Send a **prompt** to the model via API  
2. Include **parameters (temperature, tokens, etc.)**  
3. Receive a **customized response**

#### 🌍 Real-World Example:
- Weather app → calls weather API  
- AI app → calls LLM API  


## 🧠 Key Insight
> You don’t just use a model — you **control its behavior** using parameters.


## ✅ Summary
- Models are the **core intelligence** of agents  
- Sampling parameters help **fine-tune outputs**  
- APIs allow seamless **integration and control**  
- Proper tuning = **better accuracy, creativity, and efficiency**

# 🤖 Google’s Generative AI APIs

## 🚀 Overview
- Google provides **Generative AI APIs** powered by **pre-trained Large Language Models (LLMs)**.
- These models can be:
  - Used directly
  - Fine-tuned for specific use cases

## 🧩 Key Capabilities of Google Gen AI APIs
- ✍️ Text completion  
- 💬 Multi-turn chat  
- 💻 Code generation  
- 🎨 Image generation (e.g., Imagen API)  

## 🛠️ Tools to Experiment with Google Gen AI APIs

Google offers two main tools:

## 1. 🌐 Google AI Studio
- Web-based tool
- Built for:
  - Beginners
  - Students
  - Developers
  - Non-technical users

### ✅ Features:
- Easy-to-use interface  
- Experiment with **Gemini models**  
- Adjust parameters (temperature, etc.)  
- Quick prototyping  

### 📌 Access:
- Login with a **Google account**

## 2. ☁️ Vertex AI Studio
- Part of **Google Cloud (Vertex AI Platform)**
- Designed for:
  - Developers
  - Researchers
  - Enterprise use

### ✅ Features:
- Prompt design & testing  
- Model tuning  
- Deployment capabilities  
- Enterprise-grade security  

### 📌 Access:
- Requires **Google Cloud account**

## ⚖️ Google AI Studio vs Vertex AI Studio

| Attribute | Google AI Studio | Vertex AI Studio |
|----------|----------------|-----------------|
| 🎯 Focus | Easy experimentation | Full ML platform |
| 👤 Users | Beginners, hobbyists | Professionals, enterprises |
| 🔐 Access | Google account | Google Cloud |
| ⚠️ Limitations | Usage limits | Paid (usage-based) |
| 🚀 Advantages | Simple & quick start | Scalable & production-ready |

## 🧠 When to Use What?

### 👉 Use Google AI Studio if:
- You are **learning or experimenting**
- You want **quick prototyping**
- You don’t need large-scale deployment

### 👉 Use Vertex AI Studio if:
- You are building **production systems**
- You need **scalability & security**
- You want **advanced tuning & deployment**

## 🔌 Key Insight
> Both tools use the same underlying models (Gemini APIs), but differ in **ease vs power**.

## ✅ Summary
- Google provides powerful **Gen AI APIs** for multiple tasks  
- **Google AI Studio** → best for beginners & quick testing  
- **Vertex AI Studio** → best for enterprise & production use  
- Choice depends on **scale, expertise, and use case**

# Parameter Playground – Hands-on with Gemini in Google AI Studio

Having learned about sampling parameters, this exercise helps you **experiment in Google AI Studio** and understand how these settings affect model outputs.

## 🚀 Objective
Explore how different parameters influence Gemini’s responses and build intuition for prompt tuning.

## 🔧 Step 1: Open Google AI Studio
- Launch **Google AI Studio**
- Navigate to the prompt playground interface

## ✍️ Step 2: Craft a Creative Prompt
Start with a prompt that allows variation and creativity.

**Example Prompts:**
- "Write a short story about a robot discovering emotions."
- "Generate 5 startup ideas in the AI space."
- "Explain quantum computing in a fun way."

## 🌡️ Step 3: Experiment with Temperature

**Temperature controls randomness:**

| Temperature | Behavior |
|------------|----------|
| 0.0        | Deterministic, factual, repetitive |
| 0.3        | Slight variation |
| 0.7        | Balanced creativity |
| 1.0+       | Highly creative, sometimes unpredictable |

**Try this:**
- Run the same prompt with different temperature values
- Compare outputs for:
  - Creativity
  - Consistency
  - Coherence

## ⚙️ Step 4: Experiment with More Sampling Parameters

### 🔹 Top-p (Nucleus Sampling)
- Controls how much probability mass is considered
- Example:
  - `Top-p = 0.9` → Uses top 90% probable tokens

### 🔹 Top-k
- Limits selection to top *k* tokens
- Example:
  - `Top-k = 40` → Chooses from top 40 tokens only

### 🔹 Max Tokens
- Controls response length

### 🔹 Frequency Penalty
- Reduces repetition of words

### 🔹 Presence Penalty
- Encourages introducing new topics

## 🔍 Step 5: Observe and Analyze

For each parameter combination, evaluate:

- ✅ Output quality
- 🎯 Relevance to prompt
- 🎨 Creativity level
- 🔁 Repetition
- 📏 Response length

## 🧠 Key Learnings

- Lower temperature = more **predictable**
- Higher temperature = more **creative**
- Top-p and Top-k help **control randomness**
- Penalties help **reduce repetition**
- Prompt design + parameters = **better results**

---

## 💡 Pro Tip
Always start with:
- `Temperature = 0.7`
- `Top-p = 0.9`

Then tweak based on your use case:
- Use **low temperature** for factual tasks
- Use **high temperature** for creative tasks

---

## 🎯 Conclusion
Hands-on experimentation is the best way to master generative AI parameters. By adjusting these settings in Google AI Studio, you can fine-tune outputs for a wide range of applications—from structured responses to highly creative content.


# Adding Prompt Engineering to Your Reasoning Loops

## 📌 Introduction
Prompt engineering plays a critical role in enhancing how AI agents **think, reason, and act**. By integrating structured prompts into the reasoning loop, you can significantly improve decision-making and output quality.

---

## 🔁 The Reasoning Loop

The **reasoning loop** is a core mechanism in a generative AI agent. It defines how the agent:

1. Receives input  
2. Performs internal reasoning  
3. Decides the next action  
4. Repeats the process until a goal is achieved  

This loop is **iterative and introspective**, allowing the agent to refine its responses step by step.

## 🔍 Key Aspects of the Reasoning Loop

### 🔄 Iterative Process
- The agent continuously cycles through steps:
  - Input → Reason → Act → Observe → Repeat
- Each iteration improves the result
- Stops when:
  - Goal is achieved
  - A stopping condition is met


### 🧠 Internal Reasoning
- The agent “thinks” using prompts
- Breaks down complex problems into smaller steps
- May include:
  - Step-by-step thinking
  - Self-reflection
  - Hypothesis testing


### 🎯 Decision Making
- Based on reasoning, the agent decides:
  - What action to take next
  - Whether to continue or stop
- Examples:
  - Call a tool (API, database)
  - Refine a query
  - Generate a response

---

### 🧩 Reasoning Frameworks
Prompt engineering frameworks guide how the agent reasons.

#### Common Frameworks:
- **Chain-of-Thought (CoT)**  
  → Step-by-step reasoning

- **ReAct (Reason + Act)**  
  → Combines reasoning with tool usage

- **Tree-of-Thought (ToT)**  
  → Explores multiple reasoning paths

- **Self-Consistency**  
  → Generates multiple answers and selects the best

---

## ⚙️ How Prompt Engineering Enhances the Loop

Prompt engineering helps:
- Structure the agent’s thinking
- Improve clarity and accuracy
- Reduce hallucinations
- Guide decision-making

---

## 🧪 Example Reasoning Loop with Prompting

```text
Step 1: Understand the problem  
Step 2: Break into sub-tasks  
Step 3: Evaluate possible solutions  
Step 4: Choose best action  
Step 5: Execute and observe results  
Step 6: Repeat if needed

# Prompt Engineering Techniques: ReAct vs Chain-of-Thought (CoT)

## 📌 Overview
Two of the most important prompting techniques for building intelligent AI agents are:

- **ReAct (Reason + Act)**
- **Chain-of-Thought (CoT)**

Both improve reasoning, but they serve **different purposes**.

## 🤖 ReAct Prompting (Reason + Act)

ReAct enables an AI model to:
- **Think** about a problem  
- **Take actions** (e.g., call APIs, search the web)  
- **Observe results**  
- **Iterate until a final answer is reached**


### 🔁 ReAct Loop

```text
Thought → Action → Observation → Thought → Action → Observation → Response

# Adding in Tooling for AI Agents

## 📌 Introduction
Tooling allows generative AI agents to **interact with the real world**. Instead of only generating text, agents can:
- Fetch live data  / Perform actions / Connect with external systems  

- Think of tools as giving an agent **skills + access + capabilities**.

## 🧰 Types of Agent Tools

Agent tools can be grouped into four main categories:

### 🔌 1. Extensions (APIs)
- Act as a bridge between agents and external systems  
- Simplify API usage by standardizing interactions  

**Example:**
- A travel agent uses an API extension to:
  - Search flights  
  - Check availability  
  - Book tickets  


### ⚙️ 2. Functions
- Predefined operations the agent can execute  
- Typically used for structured tasks  

**Example:**
- Calculate stock returns  
- Format data  
- Trigger workflows  


### 🗄️ 3. Data Stores
- Provide access to stored data  
- Can include:
  - Databases  
  - Vector stores  
  - Knowledge bases  

**Example:**
- Query customer records  
- Retrieve historical stock data  


### 🌐 4. External Services
- Third-party systems or platforms  
- Often accessed via APIs or integrations  

**Example:**
- Payment gateways  
- Email services  
- Cloud platforms  


## 🔁 How the Reasoning Loop Works with Tools (ReAct)

The **ReAct framework** explains how agents use tools in a loop:

### 🧠 1. Reasoning (Tool Selection)
- Agent analyzes the task  
- Decides which tool(s) to use  

### ⚡ 2. Acting (Tool Execution)
- Calls the selected tool  
- Passes required inputs  

### 👀 3. Observation
- Receives output from the tool  
- Treats it as new information  

### 🔄 4. Iteration (Dynamic Loop)
- Re-evaluates based on results  
- May:
  - Use another tool  
  - Refine query  
  - Continue loop  

## 🌱 Example: Scheduling a Garden Consultation

### Step-by-step:
- **Reasoning:**  
  → Need to find available time slots  
  → Select scheduling tool  

- **Acting:**  
  → Query calendar API  

- **Observation:**  
  → Available slots returned  

- **Iteration:**  
  → Filter based on user preference  
  → Confirm booking  

## 🎯 Why Tooling is Important

- 🌐 Enables real-world interaction  
- 📊 Provides up-to-date data  
- 🤖 Makes agents autonomous  
- 🔍 Reduces hallucination by grounding responses  


## 💡 Best Practices

- Use **ReAct framework** for tool-based agents  
- Clearly define:
  - Tool inputs  
  - Tool outputs  
- Combine tools with **prompt engineering (CoT + ReAct)**  
- Add validation and fallback mechanisms  


## 🚀 Final Takeaway

- Tools transform LLMs from **passive responders → active agents**
- ReAct + Tooling = **Intelligent, action-oriented AI systems**
# Google’s Agent Tooling (Google Cloud)

## 📌 Overview
Google Cloud provides a powerful ecosystem of tools that enable AI agents to:
- Access data  
- Perform computations  
- Run applications  
- Leverage advanced AI capabilities  

👉 These tools can be used **inside or outside Google Cloud-based agents**.

## ☁️ Key Google Cloud Tools for Agents

### 🗂️ Cloud Storage
- Object storage for files and unstructured data  
- Ideal for:
  - Documents  
  - Images  
  - Logs  


### 🗄️ Databases
Includes:
- **Cloud SQL** → Relational databases  
- **Spanner** → Globally distributed database  
- **Firestore** → NoSQL document database  

👉 Used for storing and querying structured data


### ⚙️ Cloud Run Functions
- Serverless functions (event-driven)  
- Executes small pieces of logic  

**Example:**
- Process uploaded files  
- Trigger workflows  


### 🚀 Cloud Run
- Run containerized applications  
- Scalable and serverless  

**Example:**
- Host APIs for your agent  
- Run backend services  

### 🤖 Vertex AI
- Core AI/ML platform on Google Cloud  
- Features:
  - Model training  
  - Model deployment  
  - Generative AI (Gemini)  

👉 Central hub for building intelligent agents

### 🧠 Pre-built AI APIs

Google provides ready-to-use AI capabilities:

- 🎤 Speech-to-Text API  
- 🔊 Text-to-Speech API  
- 🌍 Translation API  
- 📄 Document AI API  
- 👁️ Vision API  
- 🎥 Video Intelligence API  
- 📝 Natural Language API  

👉 These APIs allow agents to work with **text, audio, video, and images**

### 🌐 Other APIs
- Google Maps API  
- Google Workspace APIs  
- YouTube API  
- Google Photos API  

👉 Enables integration with real-world services

## 🧩 Example: Meeting Location Planner Agent

### 🎯 Scenario
User uploads a document (meeting invite or venue list), and the agent suggests the best meeting location.

### 🔄 Workflow

#### 📄 1. Document Processing
- Tool: **Document AI API**  
- Extract:
  - Addresses  
  - Venue names  

#### 📍 2. Geocoding
- Tool: **Google Maps Geocoding API**  
- Convert addresses → latitude & longitude  

#### 📊 3. Analysis
- Calculate:
  - Distance between locations  
  - Travel time  


#### 🤖 4. Decision
- Suggest optimal meeting location based on:
  - Convenience  
  - Accessibility  

## 🔁 How It Fits into the Agent Loop

```text
User Input → Document Upload  
↓  
Reasoning → Identify required tools  
↓  
Action → Call Document AI + Maps API  
↓  
Observation → Extracted data + coordinates  
↓  
Iteration → Analyze & refine  
↓  
Final Output → Best meeting location

# Building Applications from Your Agents

## 📌 Introduction
Once you’ve built and tested your agent using Gemini, the next step is integrating it into real-world applications.

👉 You can use:
- **Gemini API (via Google AI Studio)**
- **Vertex AI (enterprise-grade setup)**

## 🔑 Using the API

### 🧪 Google AI Studio
- Generate an **API Key**
- Quick and simple setup  
- Best for:
  - Prototyping  
  - Experimentation  

### ☁️ Vertex AI Studio
- Set up:
  - Authentication  
  - Authorization  
- Best for:
  - Production systems  
  - Enterprise applications  


## 🔗 Integrating into Applications

You can integrate your agent into **any system that supports HTTP requests**:

### 🌐 Supported Application Types
- Web applications  
- Mobile apps  
- Desktop software  
- Embedded systems  


## ⚙️ Deployment Options (Google Cloud)

### 🚀 Cloud Run Functions
- Event-driven execution  
- Lightweight and scalable  

### 🐳 Cloud Run
- Deploy full applications in containers  
- Ideal for APIs and backend services  


## 🧩 No-Code / Low-Code Options

### 📝 Apps Script
- Automate workflows in Google Workspace  
- Example:
  - Gmail automation  
  - Google Sheets processing  

### 📊 AppSheet
- Build apps without coding  
- Connect to:
  - Databases  
  - APIs  
  - Google services  


## 🤖 Multi-Agent Applications

Sometimes one agent isn’t enough.

👉 Use **multiple specialized agents** for complex systems.


### 🧠 Example: Travel Booking App

- ✈️ **Flight Agent** → Finds flights  
- 🏨 **Hotel Agent** → Suggests hotels  
- 📍 **Attraction Agent** → Recommends places  

👉 These agents:
- Work independently  
- Communicate with each other  
- Provide a seamless experience  


### 🔄 Agent as a Tool

An agent can also act as a **tool for another agent**.

**Example:**
- 😊 Sentiment Analysis Agent  
- Used by → Customer Support Agent  

👉 Helps evaluate user satisfaction in real time


## ⚖️ Benefits of Multi-Agent Systems

- 🧩 Modularity  
- ⚡ Improved efficiency  
- 📈 Scalability  
- 🔄 Flexibility  


## 🔁 End-to-End Flow

```text
User Request  
↓  
Agent (via API)  
↓  
Tool / Data Access  
↓  
Processing (Single or Multi-Agent)  
↓  
Response returned to application
