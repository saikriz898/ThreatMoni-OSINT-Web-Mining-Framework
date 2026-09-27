# Paper-Ready Results & Quantitative Findings

## Abstract / Summary Stats
- Dataset size: N = 1100 OSINT records
- Mean TPI: 40.27 (SD: 11.05)
- Top classifier: Random Forest achieved 46.36% accuracy and 0.4624 weighted F1 score.

## Tabular Model Comparison
| Model                  |   Accuracy |   Precision (Macro) |   Precision (Weighted) |   Recall (Macro) |   Recall (Weighted) |   F1 Score (Macro) |   F1 Score (Weighted) |
|:-----------------------|-----------:|--------------------:|-----------------------:|-----------------:|--------------------:|-------------------:|----------------------:|
| Random Forest          |     0.4636 |              0.4586 |                 0.4617 |           0.4595 |              0.4636 |             0.4588 |                0.4624 |
| Naive Bayes            |     0.4409 |              0.4406 |                 0.4437 |           0.4423 |              0.4409 |             0.4345 |                0.4353 |
| Decision Tree          |     0.4364 |              0.4331 |                 0.4358 |           0.4334 |              0.4364 |             0.4319 |                0.4348 |
| Logistic Regression    |     0.4364 |              0.4257 |                 0.4294 |           0.428  |              0.4364 |             0.4241 |                0.4301 |
| Support Vector Machine |     0.4409 |              0.4167 |                 0.4216 |           0.4276 |              0.4409 |             0.4138 |                0.423  |
| XGBoost                |     0.4    |              0.3942 |                 0.3978 |           0.3955 |              0.4    |             0.3946 |                0.3987 |

## Threat Priority Index Distribution
| threat_priority   |   count |
|:------------------|--------:|
| Medium            |     788 |
| High              |     221 |
| Low               |      91 |