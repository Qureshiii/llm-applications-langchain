# 🦜🔗 LangChain & Open-Source LLMs Workspace

[![Python Version](https://shields.io)](https://python.org)
[![LangChain](https://shields.io)](https://github.com)
[![License: MIT](https://shields.io)](https://opensource.org)
[![Security: Protected](https://shields.io)](#-environment-setup-and-security)

An enterprise-grade development workspace focused on building context-aware production-level LLM applications. This repository orchestrates foundational workflows involving Closed-Source models, Self-Hosted Open-Source frameworks, Contextual Vector Embeddings, and Semantic Similarity pipelines using **LangChain**.

---

## 🏗️ Repository Architecture

The project is modularly structured to separate execution paradigms across different generative modeling frameworks:

```text
├── 01.LLMs/                       # Core foundational Language Model configurations
├── 02.ChatModels/                 # Contextual Conversation Interfaces
│   ├── 01_Closed_Source_LLMs/     # Managed API Clients (OpenAI, Anthropic, Google Gemini)
│   └── 02_Open_Source_LLMs/       # Self-hosted & Hugging Face inference hubs
├── 03.EmbeddedModels/             # Vectorization & Semantic Analysis Infrastructure
│   └── 04_document_similarity.py  # High-dimensional document comparison modules
├── .gitignore                     # Git exclusion rules (Venv & Secrets filtering)
├── requirements.txt               # Unified project standard dependencies
└── test.py                        # Root execution gateway script
```

---

## 🚀 Getting Started

### 1. Installation & Environment Setup
Clone the architecture into your local runtime shell and spin up a decoupled virtual environment:

```bash
# Clone the repository
git clone https://github.com
cd llm-applications-langchain

# Spin up a virtual environment
python -m venv venv

# Activate the isolated workspace environment
# On Windows PowerShell:
.\venv\Scripts\Activate.ps1
# On Mac/Linux:
source venv/bin/activate

# Execute deterministic dependency installation
pip install -r requirements.txt
```

---

## 🔒 Environment Setup and Security

This project relies on sensitive infrastructure routing. **Never commit raw tokens or strings directly into tracking workflows.** 

Create a custom configuration metadata routing file named `.env` in the root workspace folder:

```env
OPENAI_API_KEY="your-production-openai-token"
HUGGINGFACEHUB_API_TOKEN="your-huggingface-inference-token"
GOOGLE_API_KEY="your-google-gemini-token"
ANTHROPIC_API_KEY="your-anthropic-claude-token"
```

### Decoupled Code Loading Standard
All structural scripts inside this archive safely consume credentials directly via system proxies without raw variables tracking:

```python
import os
from langchain_openai import ChatOpenAI

# Production standards decoupling proxy
model = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
```

---

## 🛠️ Modules Breakdown

### 🔹 Chat Models Orchestration
Handles stateful multi-turn interactions. Includes programmatic comparisons between proprietary providers and decentralized open-source pipelines:
* **Closed-Source:** Enterprise integrations across OpenAI, Google Gemini, and Anthropic.
* **Open-Source:** Independent infrastructure orchestration utilizing API gateways via `HuggingFaceHub` and local compute setups.

### 🔹 Embedding Infrastructure & Document Similarity
Converts text into high-dimensional vector representations to run vector space calculations:
* Implements document segmentation strategies.
* Generates vector footprints to gauge semantic matching distances across deep textual archives.

---

## 👨‍💻 Verification Run
To ensure your runtime workspace context is configured flawlessly with upstream infrastructure connections, execute the gateway test module:

```bash
python test.py
```

---

## 📜 License
Distributed under the MIT License. See `LICENSE` for more information.
