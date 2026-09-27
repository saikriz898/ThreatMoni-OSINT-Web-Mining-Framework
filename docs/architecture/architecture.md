# ThreatMoni Framework Architecture

## High-Level System Architecture

ThreatMoni is structured as a modular, 18-stage pipeline separating data ingestion, indicator-preserving preprocessing, NLP feature extraction, threat scoring, machine learning classification, horizon scanning, and interactive visualization.

```mermaid
flowchart TD
    subgraph Data Layer
        A[Raw OSINT Feeds\ncybersecurity_dataset.csv] --> B[Dataset Profiler & Schema Validation]
    end

    subgraph Processing & NLP Layer
        B --> C[Indicator-Preserving Preprocessor]
        C --> D[NLP & Entity Extractor\nRegex + NLTK + TF-IDF]
        D --> E[Feature Engineering Engine]
    end

    subgraph Analytics & ML Layer
        E --> F[Threat Scoring Engine\nSCS, TFS, IQ, TCS, TRS, TPI]
        E --> G[Supervised Machine Learning\nLR, DT, RF, SVM, NB, XGBoost]
    end

    subgraph Output & Application Layer
        F --> H[Horizon Scanning & Priority Mapping]
        G --> H
        H --> I[Research Reports & Excel Export]
        H --> J[Streamlit Interactive Dashboard]
```

## Component Responsibilities

1. **DataLoader (`src/threatmoni/data_loader.py`):** Automatically discovers tabular datasets in `data/raw/` and loads primary feeds without mutating originals.
2. **DatasetProfiler (`src/threatmoni/profiler.py`):** Inspects row/column metrics, missing values, duplicates, and discovers semantic candidates.
3. **DataPreprocessor (`src/threatmoni/preprocessing.py`):** Sanitizes unstructured text while preserving regex patterns for `CVE-*`, IP addresses, MD5/SHA256 hashes, and MITRE ATT&CK IDs.
4. **NLPEngine (`src/threatmoni/nlp_engine.py`):** Extracts structured technical indicators, security keywords, and TF-IDF feature matrices.
5. **ThreatScorer (`src/threatmoni/threat_scoring.py`):** Computes Source Credibility (SCS), Intelligence Quality (IQ), Threat Confidence (TCS), Threat Risk (TRS), and Threat Priority Index (TPI).
6. **ThreatClassifier (`src/threatmoni/model_training.py`):** Trains 6 machine learning models using stratified splitting and strict data leakage controls.
7. **ModelEvaluator (`src/threatmoni/evaluation.py`):** Computes macro/weighted precision, recall, F1-scores, confusion matrices, and feature importances.
8. **HorizonScanner (`src/threatmoni/horizon_scanning.py`):** Analyzes threat category trends, priority distribution, and high-risk entity clusters.
