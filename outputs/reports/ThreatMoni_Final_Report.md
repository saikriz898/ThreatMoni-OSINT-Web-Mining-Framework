# ThreatMoni: OSINT Web Mining Framework for Threat Horizon Scanning
## Comprehensive Research Implementation & Experimental Evaluation Report

### 1. Project Overview
ThreatMoni is an automated OSINT web mining and threat intelligence scoring framework. It ingests cybersecurity intelligence data, performs natural language threat entity extraction, computes Source Credibility (SCS), Intelligence Quality (IQ), Threat Confidence (TCS), Threat Risk (TRS), and Threat Priority Index (TPI) metrics, and trains machine learning models to classify threat categories.

### 2. Dataset Description & Statistics
- **Primary OSINT Dataset:** `cybersecurity_dataset.csv`
- **Total Ingested Records:** 1,100
- **Total Columns:** 54
- **Missing Values:** 0 (Cleaned & Imputed)

### 3. Preprocessing & NLP Entity Extraction
Preserved raw regex structures for CVEs, IP addresses, hashes, and MITRE ATT&CK techniques. Extracted threat intelligence entity metrics across all records:

| Entity Category | Total Extracted | Records Present | % of Dataset |
| --- | --- | --- | --- |
| CVE Identifiers | 0 | 0 | 0.0% |
| Indicators of Compromise (IOCs) | 1976 | 1100 | 100.0% |
| Malware / Ransomware Instances | 550 | 550 | 50.0% |
| Threat Actors | 823 | 823 | 74.82% |
| Attack Techniques / Vectors | 0 | 0 | 0.0% |
| Vulnerability References | 0 | 0 | 0.0% |
| Security Keywords | 1306 | 920 | 83.64% |

### 4. Threat Scoring & Priority Index (TPI) Results
- **Mean TPI Score:** 40.27
- **Min TPI Score:** 13.14
- **Max TPI Score:** 73.15

#### Threat Priority Level Breakdown:
- **Low Priority (0–25):** 91 (8.27%)
- **Medium Priority (26–50):** 788 (71.64%)
- **High Priority (51–75):** 221 (20.09%)
- **Critical Priority (76–100):** 0 (0.0%)

### 5. Machine Learning Model Benchmark
Target Column: `Threat Category` (4 Classes: DDoS, Malware, Phishing, Ransomware)

| Model | Accuracy | Precision (Macro) | Recall (Macro) | F1 Score (Weighted) |
| --- | --- | --- | --- | --- |
| Random Forest | 0.4636 | 0.4586 | 0.4595 | 0.4624 |
| Naive Bayes | 0.4409 | 0.4406 | 0.4423 | 0.4353 |
| Decision Tree | 0.4364 | 0.4331 | 0.4334 | 0.4348 |
| Logistic Regression | 0.4364 | 0.4257 | 0.4280 | 0.4301 |
| Support Vector Machine | 0.4409 | 0.4167 | 0.4276 | 0.4230 |
| XGBoost | 0.4000 | 0.3942 | 0.3955 | 0.3987 |

**Best Performing Model:** `Random Forest` (Accuracy: 0.4636, Weighted F1: 0.4624)

### 6. Threat Horizon Scanning & Findings
Horizon scanning revealed Ransomware and Phishing campaigns as top threat drivers based on mean TPI scores. Network vulnerabilities and email vectors exhibit the highest risk density.

### 7. Generated Artifacts & Verification
- Streamlit Dashboard: `app/streamlit_app.py`
- Research Tables: `outputs/tables/*.csv`
- High-Res Figures: `outputs/figures/*.png`
- Excel Workbook: `outputs/ThreatMoni_Results.xlsx`
