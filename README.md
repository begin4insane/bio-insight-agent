# bio-insight-agent
An LLM-driven Multi-Agent framework for automated bioinformatics analysis. Integrates WGCNA, machine learning, and self-reflecting code execution to streamline gene identification and regulatory network building
![Python Version](https://img.shields.io/badge/Python-3.9%2B-blue)
![LLM Support](https://img.shields.io/badge/LLM-Supported-brightgreen)
![Status](https://img.shields.io/badge/Status-Beta-orange)
![License](https://img.shields.io/badge/License-MIT-green)

## Overview

**Bio-Insight Agent** is a multi-agent automated workflow designed to solve the pain points of fragmented toolchains in bioinformatics research. By orchestrating LLMs with external tools (R, Python, Origin), it automates data cleaning, Weighted Gene Co-expression Network Analysis (WGCNA), machine learning-based gene identification, and literature-based knowledge synthesis.

It transforms a multi-day manual bioinformatics pipeline into a streamlined, automated process that takes just a few hours, featuring autonomous error-correction and code reflection.

##  Core Architecture (Multi-Agent Collaboration)

The framework utilizes a **Plan-Execute-Verify** architecture driven by three core agents:

1. **Architect Agent (Planner):** Parses natural language biological queries, breaks them down into bioinformatics tasks (e.g., "Differential Expression -> WGCNA -> SVM-RFE").
2. **Programmer Agent (Executor with Self-Reflection):** Generates and executes R/Python scripts in a sandboxed environment. Crucially, if a script fails, it captures the traceback, reflects on the error, and iteratively patches the code.
3. **Synthesizer Agent (Knowledge Integrator):** Aligns statistical outputs (like P-values and hub genes) with biological mechanisms (e.g., apoptosis, ferroptosis pathways) using Agentic RAG, generating publication-ready reports.

## Key Features

* **Automated Pipeline Generation:** From raw expression matrices to ML feature selection (LASSO, SVM) without manual tool switching.
* **Agentic Error Handling:** Built-in reflection mechanism to debug complex R/Python dependency or matrix dimension errors autonomously.
* **Cross-Language Integration:** Seamlessly bridges R (for biostatistics) and Python (for Scikit-learn models).

## Quick Start (Mockup)

```python
from src.main import BioAgentWorkflow

# Initialize the workflow
workflow = BioAgentWorkflow(model="your-chosen-llm")

# Submit a complex biological query
query = "Perform WGCNA on dataset GSE12345, identify hub genes related to the trait, and screen for key biomarkers using LASSO and SVM-RFE."

# Execute the multi-agent pipeline
report = workflow.run(query)

print(report.summary)
