# OmniBrain: Agentic Multi-Modal RAG System

## Introduction
We will be working as a team to build this exciting project, collaborating closely and enjoying the progress every step of the way. Together, we'll create a powerful, production-grade Agentic AI system that transforms how we handle complex financial and multimodal data.

## Problem Statement
Standard Retrieval-Augmented Generation (RAG) pipelines fail when documents contain complex multimodal data (like financial tables, embedded charts, and images) or when queries require multi-step reasoning across diverse data silos.

## Use Case
A quantitative analyst feeds a 500-page corporate financial PDF into OmniBrain. Using a LangGraph supervisor agent, the system dynamically routes tasks. It parses tables using a Vision Language Model (VLM), queries a vector database for semantic text, and uses a Text-to-SQL agent to query historical stock data. The agents collaboratively synthesize the findings and output a highly accurate, cited investment memo, completely bypassing the hallucination risks of standard LLMs.

## Key Modules
- **Agentic Orchestrator (LangGraph)**: Manages the state, memory, and routing of multiple specialized AI agents (Search Agent, SQL Agent, Vision Agent).
- **Multi-Modal Retrieval (Qdrant / FAISS)**: Stores both text chunks and image embeddings (using CLIP) for semantic similarity search.
- **Vision-Language Model (GPT-4o / LLaVA)**: Extracts and reasons over visual charts and graphs embedded within the documents.
- **Evaluation & Guardrails (Langfuse & NeMo Guardrails)**: Monitors the LLM outputs for toxicity, hallucinations, and ensures responses are strictly grounded in the retrieved context.

## Week-wise Development Plan

### Week 1
**AI Engineering (LangGraph, VLMs, Vector DBs)**  
Multi-Modal Ingestion: Build a pipeline to parse PDFs, chunk text, and extract images. Embed both modalities into a Qdrant vector database.

**Full-Stack Integration (FastAPI, Streamlit)**  
API Scaffolding: Build a FastAPI backend to handle asynchronous document uploads and querying.

### Week 2
**AI Engineering**  
Agentic Architecture: Implement the LangGraph state machine. Define the "Supervisor" node that evaluates a user's query and routes it to the appropriate sub agent.

**Full-Stack Integration**  
Chat UI: Build a Streamlit interface capable of rendering the agent's "thought process" and displaying referenced images alongside text.

**Mid Project Review**  
- Reasoning Audit: Prove the LangGraph supervisor can correctly decide between searching the vector database vs. executing a SQL query based on the prompt.  
- Vision Check: Ensure the VLM accurately extracts numerical data from a bar chart image retrieved from the database.

### Week 3
**AI Engineering**  
- Self-Correction Loop: Implement "Self RAG." If an agent retrieves irrelevant data, it must recognize the failure, rewrite its own search query, and try again before responding to the user.  
- Guardrails: Integrate NeMo Guardrails to strictly block the AI from answering questions outside the scope of the provided documents.

### Week 4
**AI Engineering**  
Evaluation Metrics: Integrate Langfuse to track token usage, latency, and LLM execution traces for observability.

**Full-Stack Integration**  
Refine & Polish: Finalize the UI, adding citation links so users can click an AI claim and instantly view the exact PDF page and chart it referenced.

## Final Review
A production-grade Agentic AI system capable of complex, autonomous reasoning over unstructured data. A highly resilient, hallucination resistant enterprise search tool.
"# -OmniBrain-Agentic-Multi-Modal-RAG-Orchestrator" 
