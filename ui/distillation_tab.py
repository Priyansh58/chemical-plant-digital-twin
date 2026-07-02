import streamlit as st


def show_distillation(
    bottom_product,
    recovery,
    separation_efficiency,
    reflux_ratio
):

    st.header("🏭 Distillation Column")

    if bottom_product is None:
        st.info("👈 Press Calculate")
        return

    c1, c2 = st.columns(2)

    with c1:
        st.metric(
            "Bottom Product",
            f"{bottom_product:.2f} kg/hr"
        )

    with c2:
        st.metric(
            "Recovery",
            f"{recovery:.2f}%"
        )

    c3, c4 = st.columns(2)

    with c3:
        st.metric(
            "Separation Efficiency",
            f"{separation_efficiency:.2f}%"
        )

    with c4:
        st.metric(
            "Reflux Ratio",
            f"{reflux_ratio:.2f}"
        )

    st.progress(min(separation_efficiency/100,1.0))

    if separation_efficiency > 95:
        st.success("🟢 Excellent Column Performance")

    elif separation_efficiency > 90:
        st.warning("🟡 Moderate Column Performance")

    else:
        st.error("🔴 Poor Column Performance")