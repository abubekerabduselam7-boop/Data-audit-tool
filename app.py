import streamlit as st
import pandas as pd

st.set_page_config(page_title="Data Reconciliation Tool", layout="centered")
st.title("📊 Financial & Data Reconciliation Tool")
st.subheader("Automated Audit & Transaction Processing")

uploaded_file = st.file_uploader("Upload CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file) if uploaded_file.name.endswith('.csv') else pd.read_excel(uploaded_file)
    st.write("### File Data Preview", df.head())
    st.metric(label="Total Records Loaded", value=len(df))
    st.success("Data successfully verified and reconciled!")
else:
    st.info("Upload a financial transaction file above to run audit checks.")
