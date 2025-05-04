import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="CSV Graph Dashboard", layout="wide")

st.title("📊 CSV Data Visualization Tool")

# File upload
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, sep=';')
    
    st.subheader("🔍 Filterable Data Table")
    st.dataframe(df, use_container_width=True)

    st.markdown("---")

    st.subheader("📈 Graph Area 1")
    col1, col2, col3 = st.columns(3)
    with col1:
        x_axis_1 = st.selectbox("X-axis", options=df.columns, key='x1')
    with col2:
        y_axis_1 = st.selectbox("Primary Y-axis", options=df.columns, key='y1')
    with col3:
        y2_axis_1 = st.selectbox("Secondary Y-axis (optional)", options=[None] + list(df.columns), key='y2')

    fig1, ax1 = plt.subplots()
    ax1.plot(df[x_axis_1], df[y_axis_1], label=y_axis_1, color='blue')
    ax1.set_xlabel(x_axis_1)
    ax1.set_ylabel(y_axis_1, color='blue')

    if y2_axis_1:
        ax2 = ax1.twinx()
        ax2.plot(df[x_axis_1], df[y2_axis_1], label=y2_axis_1, color='green')
        ax2.set_ylabel(y2_axis_1, color='green')

    st.pyplot(fig1)

    st.markdown("---")

    st.subheader("📉 Graph Area 2")
    col4, col5, col6 = st.columns(3)
    with col4:
        x_axis_2 = st.selectbox("X-axis", options=df.columns, key='x2')
    with col5:
        y_axis_2 = st.selectbox("Primary Y-axis", options=df.columns, key='y3')
    with col6:
        y2_axis_2 = st.selectbox("Secondary Y-axis (optional)", options=[None] + list(df.columns), key='y4')

    fig2, ax3 = plt.subplots()
    ax3.plot(df[x_axis_2], df[y_axis_2], label=y_axis_2, color='orange')
    ax3.set_xlabel(x_axis_2)
    ax3.set_ylabel(y_axis_2, color='orange')

    if y2_axis_2:
        ax4 = ax3.twinx()
        ax4.plot(df[x_axis_2], df[y2_axis_2], label=y2_axis_2, color='red')
        ax4.set_ylabel(y2_axis_2, color='red')

    st.pyplot(fig2)

    st.markdown("---")

    st.subheader("📊 Distribution of `current_in`")

    if 'current_in' in df.columns:
        bins = [0, 30, 60, 90, 120, float('inf')]
        labels = ['0-30', '30-60', '60-90', '90-120', '120+']
        dist = pd.cut(df['current_in'], bins=bins, labels=labels)
        dist_counts = dist.value_counts().sort_index()
        dist_percent = (dist_counts / dist_counts.sum()) * 100

        fig3, ax5 = plt.subplots()
        ax5.bar(dist_percent.index, dist_percent.values, color='skyblue')
        ax5.set_ylabel('Percentage')
        ax5.set_xlabel('Current_in Range (A)')
        ax5.set_title('Distribution of current_in (%)')

        st.pyplot(fig3)
    else:
        st.warning("Column `current_in` not found in the uploaded file.")

else:
    st.info("Please upload a CSV file to get started.")
