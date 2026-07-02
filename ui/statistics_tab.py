import streamlit as st


def show_statistics(sensor_df):

    st.subheader("📈 Statistical Summary")

    if sensor_df is None:
        st.info("No statistics available yet.")
        return

    st.dataframe(
        sensor_df.describe().style.format("{:.2f}")
    )