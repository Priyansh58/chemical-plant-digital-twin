import streamlit as st


def show_data(sensor_df, rows_to_show):

    st.subheader("📋 Plant Sensor Data")

    if sensor_df is None:
        st.info("No sensor data available. Press Calculate.")
        return

    st.write(f"Total Sensor Readings: {len(sensor_df)}")

    st.caption(
        f"Displaying last {rows_to_show} simulated sensor readings."
    )

    st.dataframe(
        sensor_df.tail(rows_to_show).style.format({
            "Temperature": "{:.2f}",
            "Pressure": "{:.2f}",
            "Flow Rate": "{:.2f}",
            "Efficiency": "{:.2f}",
            "Energy": "{:.2f}",
            "Heat Duty": "{:.2f}",
            "Operating Cost": "{:.2f}"
        })
    )

    csv = sensor_df.to_csv(index=False).encode("utf-8")

    st.download_button(
        "📥 Download Sensor Data",
        csv,
        "plant_sensor_data.csv",
        "text/csv"
    )