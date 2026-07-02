import streamlit as st


def show_statistics(sensor_df):

    st.subheader("📈 Plant Performance Statistics")

    if sensor_df is None:
        st.info("No statistics available yet.")
        return

    avg_temp = sensor_df["Temperature"].mean()
    max_temp = sensor_df["Temperature"].max()

    avg_pressure = sensor_df["Pressure"].mean()
    max_pressure = sensor_df["Pressure"].max()

    avg_flow = sensor_df["Flow Rate"].mean()
    min_tank = sensor_df["Tank level"].min()

    avg_efficiency = sensor_df["Efficiency"].mean()
    avg_energy = sensor_df["Energy"].mean()

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Avg Temp",
            f"{avg_temp:.2f} °C"
        )

    with col2:
        st.metric(
            "Max Temp",
            f"{max_temp:.2f} °C"
        )

    with col3:
        st.metric(
            "Avg Pressure",
            f"{avg_pressure:.2f} kPa"
        )

    with col4:
        st.metric(
            "Max Pressure",
            f"{max_pressure:.2f} kPa"
        )

    st.divider()

    col5, col6, col7, col8 = st.columns(4)

    with col5:
        st.metric(
            "Avg Flow",
            f"{avg_flow:.2f} kg/hr"
        )

    with col6:
        st.metric(
            "Min Tank",
            f"{min_tank:.2f} %"
        )

    with col7:
        st.metric(
            "Avg Efficiency",
            f"{avg_efficiency:.2f}%"
        )

    with col8:
        st.metric(
            "Avg Energy",
            f"{avg_energy/1000:.2f} MJ"
        )

    st.divider()

    st.caption(
        "Detailed statistical summary of all simulated process variables."
    )

    with st.expander("📊 Detailed Statistical Summary"):
        st.dataframe(
            sensor_df.describe().style.format("{:.2f}")
        )