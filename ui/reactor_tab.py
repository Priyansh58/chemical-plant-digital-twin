import streamlit as st


def show_reactor(
    conversion,
    yield_value,
    selectivity,
    residence_time
):

    st.header("⚛️ Reactor Performance")

    if conversion is None:
        st.info("👈 Press Calculate")
        return

    c1, c2 = st.columns(2)

    with c1:
        st.metric(
            "Conversion",
            f"{conversion:.2f}%"
        )

    with c2:
        st.metric(
            "Yield",
            f"{yield_value:.2f}%"
        )

    c3, c4 = st.columns(2)

    with c3:
        st.metric(
            "Selectivity",
            f"{selectivity:.2f}"
        )

    with c4:
        st.metric(
            "Residence Time",
            f"{residence_time:.2f} hr"
        )

    st.progress(min(conversion/100, 1.0))

    if conversion > 90:
        st.success("🟢 Reactor Operating Efficiently")
    elif conversion > 75:
        st.warning("🟡 Reactor Performance Moderate")
    else:
        st.error("🔴 Reactor Performance Poor")