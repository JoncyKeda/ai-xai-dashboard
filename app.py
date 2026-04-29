import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from model.train import train_model
from utils.explain import explain_model

st.set_page_config(page_title="AI Explainability Dashboard", layout="wide")

st.title("🧠 AI Model Explainability Dashboard (XAI)")

file = st.file_uploader("Upload CSV Dataset", type=["csv"])

if file:
    df = pd.read_csv(file)

    st.subheader("📄 Dataset Preview")
    st.dataframe(df.head())

    model, X = train_model(df)

    st.success("✅ Model trained successfully")

    if st.button("🔍 Explain Model"):
        st.subheader("📊 Feature Importance (SHAP)")

        fig = explain_model(model, X)
        st.pyplot(fig)
