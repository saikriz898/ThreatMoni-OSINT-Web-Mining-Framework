# ThreatMoni Preprocessing Report

- **Original Row Count:** 2
- **Duplicates Removed:** 1
- **Final Cleaned Rows:** 1
- **Total Columns:** 3

## Applied Transformations
1. **Missing Value Handling:** Replaced missing categorical strings with `'Unknown'`, numerical missing values with column medians.
2. **Duplicate Removal:** Exact matching row deduplication applied.
3. **Text Normalization:** Lowercased non-indicator terms, tokenized, removed stop-words, applied WordNet lemmatization.
4. **Cybersecurity Indicator Protection:** Preserved raw regex structures for CVEs (`CVE-XXXX-XXXX`), IP addresses (`X.X.X.X`), hashes, and MITRE ATT&CK techniques (`TXXXX`).
5. **Structured Indicator Formatting:** Cleaned brackets and quotes from IOC lists.
