import streamlit as st


def show_graphs(
    sensor_df,
    fig_temp,
    fig_pressure,
    fig_flow,
    fig_efficiency
):
    st.subheader("📈 Live Process Trends")
    st.divider()

    if sensor_df is None:
        st.info("👈 Press Calculate to generate graphs.")
        return

    row1_col1, row1_col2 = st.columns(2)

    with row1_col1:
        st.pyplot(fig_temp)

    with row1_col2:
        st.pyplot(fig_pressure)

    row2_col1, row2_col2 = st.columns(2)

    with row2_col1:
        st.pyplot(fig_flow)

    with row2_col2:
        st.pyplot(fig_efficiency)