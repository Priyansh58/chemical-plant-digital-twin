import streamlit as st

from database import (
    load_sensor_data,
    clear_database
)


def show_database():

    st.subheader("🗄 Stored Sensor Data")

    history = load_sensor_data()

    st.write(
        f"Total Stored Records: {len(history)}"
    )

    st.dataframe(
        history.tail(100)
    )

    if st.button(
        "🧹 Clear Database"
    ):
        clear_database()
        st.success(
            "Database cleared successfully."
        )
        st.rerun()