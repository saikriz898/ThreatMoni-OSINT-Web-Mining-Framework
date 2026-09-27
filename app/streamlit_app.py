import os
import glob
import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image

st.set_page_config(
    page_title="ThreatMoni - OSINT Web Mining Framework",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Professional Technical Styling
st.markdown("""
<style>
    .main {
        background-color: #0e1117;
        color: #e0e6ed;
    }
    .metric-card {
        background: #1e222d;
        border: 1px solid #2d313e;
        border-radius: 8px;
        padding: 15px;
        text-align: center;
        margin-bottom: 15px;
    }
    .metric-value {
        font-size: 26px;
        font-weight: bold;
        color: #00d2ff;
    }
    .metric-label {
        font-size: 13px;
        color: #94a3b8;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #1e222d;
        border-radius: 4px;
        color: #94a3b8;
        padding: 8px 16px;
    }
    .stTabs [aria-selected="true"] {
        background-color: #00d2ff !important;
        color: #0e1117 !important;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_pipeline_data():
    preds_path = "outputs/predictions/threat_priority_predictions.csv"
    features_path = "data/processed/threatmoni_features.csv"
    comp_path = "outputs/tables/model_comparison.csv"
    
    df_preds = pd.read_csv(preds_path) if os.path.exists(preds_path) else pd.DataFrame()
    df_feats = pd.read_csv(features_path) if os.path.exists(features_path) else pd.DataFrame()
    df_comp = pd.read_csv(comp_path) if os.path.exists(comp_path) else pd.DataFrame()
    
    return df_preds, df_feats, df_comp

df_preds, df_feats, df_comp = load_pipeline_data()

# Header Banner
st.title("🛡️ ThreatMoni")
st.caption("OSINT Web Mining Framework for Threat Horizon Scanning & Risk Prioritization")
st.markdown("---")

# Sidebar Controls
st.sidebar.header("🕹️ Framework Controls")
st.sidebar.markdown("**Dataset Baseline:** `cybersecurity_dataset.csv`")
selected_tab = st.sidebar.radio(
    "Navigation",
    ["Overview", "Threat Landscape", "Threat Priority", "Machine Learning", "Horizon Scanning", "Record Explorer", "Methodology"]
)

if df_preds.empty:
    st.error("Pipeline output not found. Please run `python run_pipeline.py` first.")
    st.stop()

# -----------------------------------------------------------------------------
# A. OVERVIEW
# -----------------------------------------------------------------------------
if selected_tab == "Overview":
    st.subheader("📊 Executive Threat Horizon Overview")
    
    total_records = len(df_preds)
    unique_threats = df_preds["Threat Category"].nunique() if "Threat Category" in df_preds.columns else 0
    unique_cves = int(df_preds["cve_count"].sum()) if "cve_count" in df_preds.columns else 0
    unique_iocs = int(df_preds["ioc_count"].sum()) if "ioc_count" in df_preds.columns else 0
    high_count = int((df_preds["threat_priority"] == "High").sum())
    critical_count = int((df_preds["threat_priority"] == "Critical").sum())

    col1, col2, col3, col4, col5, col6 = st.columns(6)
    with col1:
        st.markdown(f'<div class="metric-card"><div class="metric-value">{total_records}</div><div class="metric-label">Total Ingested</div></div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div class="metric-card"><div class="metric-value">{unique_threats}</div><div class="metric-label">Threat Classes</div></div>', unsafe_allow_html=True)
    with col3:
        st.markdown(f'<div class="metric-card"><div class="metric-value">{unique_cves}</div><div class="metric-label">Extracted CVEs</div></div>', unsafe_allow_html=True)
    with col4:
        st.markdown(f'<div class="metric-card"><div class="metric-value">{unique_iocs}</div><div class="metric-label">Total IOCs</div></div>', unsafe_allow_html=True)
    with col5:
        st.markdown(f'<div class="metric-card"><div class="metric-value" style="color: #e67e22;">{high_count}</div><div class="metric-label">High Priority</div></div>', unsafe_allow_html=True)
    with col6:
        st.markdown(f'<div class="metric-card"><div class="metric-value" style="color: #e74c3c;">{critical_count}</div><div class="metric-label">Critical Priority</div></div>', unsafe_allow_html=True)

    st.markdown("### Key Horizon Figures")
    fig_col1, fig_col2 = st.columns(2)
    with fig_col1:
        if os.path.exists("outputs/figures/threat_priority_distribution.png"):
            st.image("outputs/figures/threat_priority_distribution.png", caption="Threat Priority Distribution (TPI Level)")
    with fig_col2:
        if os.path.exists("outputs/figures/tpi_distribution.png"):
            st.image("outputs/figures/tpi_distribution.png", caption="Continuous TPI Score Distribution")

# -----------------------------------------------------------------------------
# B. THREAT LANDSCAPE
# -----------------------------------------------------------------------------
elif selected_tab == "Threat Landscape":
    st.subheader("🌐 OSINT Threat Landscape Analysis")
    
    col1, col2 = st.columns(2)
    with col1:
        if os.path.exists("outputs/figures/class_distribution.png"):
            st.image("outputs/figures/class_distribution.png", caption="Ground-Truth Category Distribution")
    with col2:
        if os.path.exists("outputs/figures/threat_category_distribution.png"):
            st.image("outputs/figures/threat_category_distribution.png", caption="Category Share")

    st.markdown("### Attack Vectors & Geographic Intelligence")
    col3, col4 = st.columns(2)
    with col3:
        if os.path.exists("outputs/figures/attack_vector_frequency.png"):
            st.image("outputs/figures/attack_vector_frequency.png", caption="Attack Vectors")
    with col4:
        if os.path.exists("outputs/figures/geographical_distribution.png"):
            st.image("outputs/figures/geographical_distribution.png", caption="Geographical Distribution")

# -----------------------------------------------------------------------------
# C. THREAT PRIORITY
# -----------------------------------------------------------------------------
elif selected_tab == "Threat Priority":
    st.subheader("🎯 Threat Priority Index (TPI) Breakdown")
    
    st.markdown("### Top Critical Priority OSINT Records")
    high_critical = df_preds[df_preds["threat_priority"].isin(["High", "Critical"])].sort_values(by="tpi_score", ascending=False)
    st.dataframe(high_critical[["Threat Category", "Threat Actor", "Attack Vector", "tpi_score", "threat_priority", "Cleaned Threat Description"]].head(15), use_container_width=True)

    if os.path.exists("outputs/figures/severity_vs_tpi.png"):
        st.image("outputs/figures/severity_vs_tpi.png", caption="Calculated TPI Score vs Raw Severity Rating", use_column_width=True)

# -----------------------------------------------------------------------------
# D. MACHINE LEARNING
# -----------------------------------------------------------------------------
elif selected_tab == "Machine Learning":
    st.subheader("🤖 Supervised Machine Learning Benchmark")
    st.markdown("Target Variable: **Threat Category** (DDoS, Malware, Phishing, Ransomware)")
    
    if not df_comp.empty:
        st.table(df_comp)
    
    col1, col2 = st.columns(2)
    with col1:
        if os.path.exists("outputs/figures/model_f1.png"):
            st.image("outputs/figures/model_f1.png", caption="Model Comparison (Weighted F1 Score)")
    with col2:
        if os.path.exists("outputs/figures/confusion_matrix_random_forest.png"):
            st.image("outputs/figures/confusion_matrix_random_forest.png", caption="Confusion Matrix - Random Forest")

    if os.path.exists("outputs/figures/feature_importance_random_forest.png"):
        st.image("outputs/figures/feature_importance_random_forest.png", caption="Top 10 Feature Importances (Random Forest)", use_column_width=True)

# -----------------------------------------------------------------------------
# E. HORIZON SCANNING
# -----------------------------------------------------------------------------
elif selected_tab == "Horizon Scanning":
    st.subheader("🔭 OSINT Threat Horizon Scanning & Emerging Indicators")
    
    top_threats_path = "outputs/tables/top_threats.csv"
    if os.path.exists(top_threats_path):
        st.markdown("### Threat Categories Ranked by Horizon Priority (Mean TPI)")
        st.dataframe(pd.read_csv(top_threats_path), use_container_width=True)

    if os.path.exists("outputs/figures/emerging_threats.png"):
        st.image("outputs/figures/emerging_threats.png", caption="Emerging Threat Priority Spectrum", use_column_width=True)

# -----------------------------------------------------------------------------
# F. RECORD EXPLORER
# -----------------------------------------------------------------------------
elif selected_tab == "Record Explorer":
    st.subheader("🔍 Interactive OSINT Record Explorer")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        prio_filter = st.multiselect("Filter by Threat Priority", options=["Low", "Medium", "High", "Critical"], default=["High", "Critical"])
    with col2:
        cat_filter = st.multiselect("Filter by Threat Category", options=df_preds["Threat Category"].unique().tolist(), default=df_preds["Threat Category"].unique().tolist())
    with col3:
        min_tpi, max_tpi = st.slider("TPI Score Range", 0.0, 100.0, (0.0, 100.0))

    filtered_df = df_preds[
        (df_preds["threat_priority"].isin(prio_filter)) &
        (df_preds["Threat Category"].isin(cat_filter)) &
        (df_preds["tpi_score"] >= min_tpi) &
        (df_preds["tpi_score"] <= max_tpi)
    ]
    
    st.markdown(f"Displaying **{len(filtered_df)}** matching OSINT records.")
    st.dataframe(filtered_df[["Threat Category", "Threat Actor", "Attack Vector", "Geographical Location", "tpi_score", "threat_priority", "Cleaned Threat Description"]], use_container_width=True)

# -----------------------------------------------------------------------------
# G. METHODOLOGY
# -----------------------------------------------------------------------------
elif selected_tab == "Methodology":
    st.subheader("📐 ThreatMoni Conceptual Source Methodology & Formulas")
    
    st.markdown("""
    ### Formulations & Scoring System
    
    1. **Source Credibility Score (SCS):**
       $$SCS = \\frac{R + U + C + A}{4}$$
       *Where R = Reliability, U = Update Frequency/Detail, C = Consistency, A = Authority.*
       
    2. **Threat Frequency Score (TFS):**
       $$TFS = \\frac{N_t}{N}$$
       *Where $N_t$ = occurrences of threat category, $N$ = total collected threat records.*
       
    3. **Intelligence Quality (IQ):**
       $$IQ = 0.4(Completeness) + 0.3(IOC\\ Presence) + 0.3(Text\\ Granularity)$$
       
    4. **Threat Confidence Score (TCS):**
       $$TCS = \\alpha(SCS) + \\beta(IQ)$$
       *Default configured weights: $\\alpha = 0.5$, $\\beta = 0.5$.*
       
    5. **Threat Risk Score (TRS):**
       $$TRS = \\sum (W_i \\times F_i)$$
       *Weighted combination of severity rating, TFS, risk prediction, IOC density, and forum sentiment.*
       
    6. **Threat Priority Index (TPI):**
       $$TPI = \\frac{TRS \\times TCS}{100}$$
       
    #### Priority Threshold Mapping:
    - **0 – 25:** Low Priority
    - **26 – 50:** Medium Priority
    - **51 – 75:** High Priority
    - **76 – 100:** Critical Priority
    """)
