import streamlit as st


def show_heat_exchanger(
    heat_transfer,
    lmtd,
    effectiveness
):

    st.header("🔥 Heat Exchanger Performance")

    if heat_transfer is None:
        st.info("👈 Press Calculate to run the Heat Exchanger simulation.")
        return

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Heat Transfer",
            f"{heat_transfer:.2f} kW"
        )

    with col2:
        st.metric(
            "LMTD",
            f"{lmtd:.2f} °C"
        )

    with col3:
        st.metric(
            "Effectiveness",
            f"{effectiveness*100:.2f}%"
        )

    st.subheader("Heat Exchanger Effectiveness")

    st.progress(min(effectiveness, 1.0))

    if effectiveness > 0.8:
        st.success("🟢 Excellent Heat Exchanger Performance")
    elif effectiveness > 0.6:
        st.warning("🟡 Moderate Heat Exchanger Performance")
    else:
        st.error("🔴 Poor Heat Exchanger Performance")

    st.subheader("Engineering Interpretation")

    st.write(f"""
- **Heat Transfer:** {heat_transfer:.2f} kW
- **LMTD:** {lmtd:.2f} °C
- **Effectiveness:** {effectiveness*100:.2f}%
""")