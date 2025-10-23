import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# -------------------------------
# Title & Intro
# -------------------------------
st.set_page_config(page_title="BioScope - Genomic Data Visualizer", layout="wide")

st.title("🧬 BioScope – Genomic Data Visualizer")
st.write("""
Welcome to **BioScope**, an AI-inspired tool for exploring biological and genomic data.
You can upload your own CSV file or use a sample dataset to visualize gene expression patterns and mutation frequencies.
""")

# -------------------------------
# Data Upload or Sample
# -------------------------------
uploaded_file = st.file_uploader("Upload your genomic data (CSV)", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    # Generate a sample dataset
    np.random.seed(42)
    genes = [f"Gene_{i}" for i in range(1, 21)]
    df = pd.DataFrame({
        "Gene": genes,
        "Expression_Level": np.random.uniform(5, 50, 20),
        "Mutation_Rate": np.random.uniform(0, 1, 20),
        "Category": np.random.choice(["Regulatory", "Metabolic", "Structural"], 20)
    })
    st.info("Using sample dataset (upload your own to replace it).")

st.dataframe(df.head())

# -------------------------------
# Charts
# -------------------------------
st.subheader("📊 Expression Level by Gene")
fig1 = px.bar(df, x="Gene", y="Expression_Level", color="Category", title="Gene Expression Levels")
st.plotly_chart(fig1, use_container_width=True)

st.subheader("🧫 Mutation Rate Scatter Plot")
fig2 = px.scatter(df, x="Expression_Level", y="Mutation_Rate", color="Category",
                  size="Expression_Level", hover_name="Gene",
                  title="Expression vs Mutation Rate")
st.plotly_chart(fig2, use_container_width=True)

# -------------------------------
# AI-Style Insights (mock)
# -------------------------------
st.subheader("🧠 AI-Generated Insights")

avg_exp = df["Expression_Level"].mean()
avg_mut = df["Mutation_Rate"].mean()

insights = f"""
- The dataset contains {len(df)} genes across {df['Category'].nunique()} biological categories.
- Average expression level is **{avg_exp:.2f} units**, and average mutation rate is **{avg_mut:.2f}**.
- Highest expressed gene: **{df.loc[df['Expression_Level'].idxmax(), 'Gene']}**.
- Gene with highest mutation rate: **{df.loc[df['Mutation_Rate'].idxmax(), 'Gene']}**.
"""

if avg_exp > 30:
    insights += "\n- High overall gene expression suggests active biological processes."
else:
    insights += "\n- Expression levels are moderate, indicating stable genetic activity."

if avg_mut > 0.6:
    insights += "\n- Mutation rates are elevated — could indicate evolutionary adaptation or experimental variance."
else:
    insights += "\n- Mutation rates are within normal range."

st.markdown(insights)
st.success("AI-style analysis complete ✅")

# -------------------------------
# Footer
# -------------------------------
st.markdown("---")
st.caption("BioScope © 2025 | Built with Streamlit, Plotly & Pandas")
