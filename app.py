
import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

# ---------------- PAGE CONFIGURATION ----------------

st.set_page_config(
    page_title="Module VI | Applied Mathematics",
    page_icon="📊",
    layout="wide"
)

# ---------------- RESPONSIVE PROJECT NAVIGATION ----------------

PROJECT_OPTIONS = [
    "Home",
    "Bayesian Intrusion Detection",
    "Network Latency Analysis"
]

# Keep the desktop sidebar and the always-visible page navigation in sync.
if "sidebar_project" not in st.session_state:
    st.session_state["sidebar_project"] = "Home"
if "main_project" not in st.session_state:
    st.session_state["main_project"] = "Home"


def _sync_from_sidebar():
    st.session_state["main_project"] = st.session_state["sidebar_project"]


def _sync_from_main():
    st.session_state["sidebar_project"] = st.session_state["main_project"]


# ---------------- PROFESSIONAL DASHBOARD THEME ----------------

st.markdown("""
<style>
/* Main application background */
.stApp {
    background:
        radial-gradient(
            circle at 10% 0%,
            rgba(59, 130, 246, 0.10),
            transparent 35%
        ),
        #0B1120;
    color: #E5E7EB;
}

/* Main content width and spacing */
.block-container {
    max-width: 1450px;
    padding-top: 2.2rem;
    padding-bottom: 3rem;
}

/* Main headings */
h1 {
    color: #F8FAFC !important;
    font-weight: 800 !important;
    letter-spacing: -0.8px;
}

h2 {
    color: #E2E8F0 !important;
    font-weight: 700 !important;
}

h3 {
    color: #93C5FD !important;
    font-weight: 650 !important;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: #111827;
    border-right: 1px solid #263449;
}

[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 {
    color: #F8FAFC !important;
}

/* Metric cards */
[data-testid="stMetric"] {
    background: linear-gradient(145deg, #17243A, #111B2D);
    border: 1px solid #2B3B55;
    padding: 20px 22px;
    border-radius: 16px;
    box-shadow: 0 5px 18px rgba(0, 0, 0, 0.15);
}

[data-testid="stMetricLabel"] {
    color: #A5B4CC !important;
}

[data-testid="stMetricValue"] {
    color: #60A5FA !important;
    font-weight: 750 !important;
}

/* Buttons */
.stButton > button {
    background: linear-gradient(90deg, #2563EB, #4F46E5);
    color: white;
    border: none;
    border-radius: 10px;
    padding: 0.55rem 1.1rem;
    font-weight: 650;
    transition: 0.2s ease;
}

.stButton > button:hover {
    background: linear-gradient(90deg, #1D4ED8, #4338CA);
    color: white;
    border: none;
    box-shadow: 0 4px 15px rgba(59, 130, 246, 0.25);
}

/* Input fields */
[data-testid="stNumberInput"] input,
[data-testid="stTextInput"] input,
