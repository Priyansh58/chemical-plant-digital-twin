# import streamlit as st

# from database import (
#     load_sensor_data,
#     clear_database
# )


# def show_database():

#     st.subheader("🗄 Stored Sensor Data")

#     history = load_sensor_data()

#     st.write(
#         f"Total Stored Records: {len(history)}"
#     )

#     st.dataframe(
#         history.tail(100)
#     )

#     if st.button(
#         "🧹 Clear Database"
#     ):
#         clear_database()
#         st.success(
#             "Database cleared successfully."
#         )
#         st.rerun()

import streamlit as st

from database import (
    load_sensor_data,
    clear_database
)


def show_database():

    st.subheader("🗄 Process History")

    history = load_sensor_data()

    if history.empty:
        st.info("No simulations available.")
        return

    simulations = history["SimulationID"].unique()

    st.metric(
        "Total Simulations",
        len(simulations)
    )

    selected = st.selectbox(
        "Select Simulation",
        simulations[::-1]
    )

    filtered = history[
        history["SimulationID"] == selected
    ]

    st.write(
        f"📅 Timestamp : {filtered['Timestamp'].iloc[0]}"
    )

    st.write(
        f"📊 Total Readings : {len(filtered)}"
    )

    st.dataframe(filtered)

    csv = filtered.to_csv(index=False).encode("utf-8")

    st.download_button(
        "📥 Download This Simulation",
        csv,
        f"{selected}.csv",
        "text/csv"
    )

    if st.button("🧹 Clear Database"):
        clear_database()
        st.success("Database cleared successfully.")
        st.rerun()