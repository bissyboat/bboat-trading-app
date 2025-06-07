import streamlit as st
from frontend.dashboard import main as strategy_dashboard
from frontend.compare_strategies import main as comparison_dashboard
from frontend.login import login

st.set_page_config(page_title="Gold Trading App", layout="wide")

if not login():
    st.stop()

st.sidebar.title("📂 App Sections")
page = st.sidebar.radio("Go to", ["📈 Strategy Analyzer", "📊 Strategy Comparison"])

if page == "📈 Strategy Analyzer":
    strategy_dashboard()
elif page == "📊 Strategy Comparison":
    comparison_dashboard()
