import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from ui.graphs_tab import show_graphs
from ui.data_tab import show_data
from ui.statistics_tab import show_statistics
from ui.database_tab import show_database
from ui.heat_exchanger_tab import show_heat_exchanger
from database import (
    create_database,
    save_sensor_data,
    load_sensor_data,
    clear_database
)
from heat_exchanger import (
    calculate_heat_transfer,
    calculate_lmtd,
    calculate_effectiveness
)
from calculations import (
    calculate_efficiency,
    calculate_heat_duty,
    calculate_energy,
    calculate_operating_cost
)
from data import(
        generate_sensor_data,
        calculate_sensor_parameters
    )
from plots import create_line_plot
from utils import check_plant_status
st.set_page_config(
    page_title="Chemical Plant Digital Twin",
    page_icon="🧪",
    layout="wide"
)
create_database()
if "sensor_df" not in st.session_state:
    st.session_state.sensor_df = None

if "fig_temp" not in st.session_state:
    st.session_state.fig_temp = None

if "fig_pressure" not in st.session_state:
    st.session_state.fig_pressure = None

if "fig_flow" not in st.session_state:
    st.session_state.fig_flow = None

if "fig_efficiency" not in st.session_state:
    st.session_state.fig_efficiency = None

if "energy" not in st.session_state:
    st.session_state.energy = None

if "heat_duty" not in st.session_state:
    st.session_state.heat_duty = None

if "cost" not in st.session_state:
    st.session_state.cost = None

if "alerts" not in st.session_state:
    st.session_state.alerts = []
if "efficiency" not in st.session_state:
    st.session_state.efficiency = None
if "heat_transfer" not in st.session_state:
    st.session_state.heat_transfer = None

if "lmtd" not in st.session_state:
    st.session_state.lmtd = None

if "effectiveness" not in st.session_state:
    st.session_state.effectiveness = None



st.title("🧪 Chemical Plant Digital Twin")
st.caption("Real-Time Process Monitoring | Digital Twin | Process Analytics")

st.divider()

st.sidebar.title("⚙️ Control Panel")
st.sidebar.header("🏭 Plant Inputs")

temperature = st.sidebar.number_input(
    "Temperature (°C)",
    value=100.0
)
pressure = st.sidebar.number_input(
    "Pressure (kPa)",
    value=1000.0
)

flow_rate = st.sidebar.number_input(
    "Flow Rate (kg/hr)",
    value=250.0
)
reflux_ratio = st.sidebar.slider(
    "Reflux Ratio",
    1.0,
    10.0,
    2.5
)

st.sidebar.divider()

st.sidebar.subheader("🔥 Heat Exchanger")
hot_in = st.sidebar.number_input(
    "Hot Inlet (°C)",
    value=180.0
)
hot_out = st.sidebar.number_input(
    "Hot Outlet (°C)",
    value=120.0
)

cold_in = st.sidebar.number_input(
    "Cold Inlet (°C)",
    value=40.0
)

cold_out = st.sidebar.number_input(
    "Cold Outlet (°C)",
    value=90.0
)

st.sidebar.divider()

st.sidebar.subheader("🚨 Alarm Settings")
temp_limit = st.sidebar.slider(
    "Temperature Alarm",
    90,
    120,
    105
)
pressure_limit = st.sidebar.slider(
    "Pressure Alarm",
    950,
    1100,
    1030
)

st.sidebar.divider()

st.sidebar.subheader("📊 Dashboard Settings")
rows_to_show = st.sidebar.selectbox(
    "Number of Readings",
    [20, 50, 100],
    index = 2
)

st.sidebar.divider()

calculate = st.sidebar.button(
    "▶ Run Simulation",
    use_container_width=True
)

if calculate:
    
    st.session_state.sensor_df = generate_sensor_data(
        temperature,
        pressure,
        flow_rate,
        7, 
        80
    )
    st.session_state.sensor_df = calculate_sensor_parameters(st.session_state.sensor_df)
    save_sensor_data(st.session_state.sensor_df)
    st.session_state.alerts = check_plant_status(
        st.session_state.sensor_df,
        temp_limit,
        pressure_limit
    )

        
    filtered_df = st.session_state.sensor_df.tail(rows_to_show)
    fig_temp = create_line_plot(
        filtered_df,
        "Time",
        "Temperature",
        "Temperature vs Time",
        "Temperature (°C)"
    )
    fig_pressure = create_line_plot(
        filtered_df,
        "Time",
        "Pressure",
        "Pressure vs Time",
        "Pressure (kPa)"
    )
    fig_flow = create_line_plot(
        filtered_df,
        "Time",
        "Flow Rate",
        "Flow Rate vs Time",
        "Flow Rate (kg/hr)"
    )

    fig_efficiency = create_line_plot(
        filtered_df,
        "Time",
        "Efficiency",
        "Efficiency vs Time",
        "Efficiency (%)"
    )
    st.session_state.fig_temp = fig_temp
    st.session_state.fig_pressure = fig_pressure
    st.session_state.fig_flow = fig_flow
    st.session_state.fig_efficiency = fig_efficiency
    st.session_state.efficiency = calculate_efficiency(
        temperature,
        pressure
    )
    st.session_state.energy = calculate_energy(
        temperature,
        flow_rate
    )
    st.session_state.heat_duty = calculate_heat_duty(
        temperature,
        flow_rate
    )
    st.session_state.cost = calculate_operating_cost(
        st.session_state.energy
    )


    cp = 4.18  # Specific heat capacity of water in kJ/kg°C
    st.session_state.heat_transfer = calculate_heat_transfer(
        flow_rate,
        cp,
        hot_in,
        hot_out
    )

    st.session_state.lmtd = calculate_lmtd(
        hot_in,
        hot_out,
        cold_in,
        cold_out
    )

    st.session_state.effectiveness = calculate_effectiveness(
        hot_in,
        hot_out,
        cold_in
    )
col1, col2 = st.columns(2)

with col1:
    if st.session_state.efficiency is None:
        st.metric("Efficiency", "--")
    else:
        st.metric(
            "Efficiency",
            f"{st.session_state.efficiency:.2f}%"
        )
with col2:
    if st.session_state.energy is None:
        st.metric("Energy Consumption", "--")
    else:
        st.metric(
            "Energy Consumption",
            f"{st.session_state.energy:.2f} kJ"
        )

col3, col4 = st.columns(2)

with col3:
    if st.session_state.heat_duty is None:
        st.metric("Heat Duty", "--")
    else:
        st.metric(
            "Heat Duty",
            f"{st.session_state.heat_duty:.2f} kJ/hr"
        )

with col4:
    if st.session_state.cost is None:
        st.metric("Operating Cost/hr", "--")
    else:
        st.metric(
            "Operating Cost/hr",
            f"{st.session_state.cost:.2f}/hr"
        )


st.subheader("📊 Plant Analytics")
if st.session_state.sensor_df is None: 
    st.info("Press Calculate to generate analytics.")
else:
        avg_temp = st.session_state.sensor_df["Temperature"].mean()
        max_pressure = st.session_state.sensor_df["Pressure"].max()
        min_tank = st.session_state.sensor_df["Tank level"].min()
        avg_flow = st.session_state.sensor_df["Flow Rate"].mean()

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                "Avg Temp",
                f"{avg_temp:.2f} °C"
            )
        with col2:
            st.metric(
                "Max Pressure",
                f"{max_pressure:.2f} kPa"
            )
        
        with col3:
            st.metric(
                "Min Tank Level",
                f"{min_tank:.2f} %"
            )
        with col4:
            st.metric(
                "Avg Flow Rate",
                f"{avg_flow:.2f} kg/hr"
            )
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 Graphs",
    "📋 Data",
    "📈 Statistics",
    "🗄 Database",
    "🔥 Heat Exchanger"
])

with tab1:
    show_graphs(
        st.session_state.sensor_df,
        st.session_state.fig_temp,
        st.session_state.fig_pressure,
        st.session_state.fig_flow,
        st.session_state.fig_efficiency
    )





with tab2:
    show_data(
        st.session_state.sensor_df,
        rows_to_show
    )


with tab3:
    show_statistics(st.session_state.sensor_df)



with tab4:
    show_database()
    
# with tab5:
#     st.header("🔥 Heat Exchanger Performance")
#     if st.session_state.heat_transfer is None:
#         st.info("👈 Press Calculate to run the Heat Exchanger simulation.")
#     else:
#         col1, col2, col3 = st.columns(3)

#         with col1:
#             st.metric(
#             "Heat Transfer",
#             f"{st.session_state.heat_transfer:.2f} kW"
#         )
#         with col2:
#             st.metric(
#             "LMTD",
#             f"{st.session_state.lmtd:.2f} °C"
#         )
#         with col3:
#             st.metric(
#             "Effectiveness",
#             f"{st.session_state.effectiveness*100:.2f}%"
#         )
            
#         st.progress(min(st.session_state.effectiveness, 1.0))
#         if st.session_state.effectiveness >0.8:
#             st.success("🟢 Heat Exchanger Operating Efficiently")
#         elif st.session_state.effectiveness > 0.6:
#             st.warning("🟡 Heat Exchanger Efficiency Moderate")
#         else:
#             st.error("🔴 Heat Exchanger Efficiency Low")
#     # st.subheader("Performance Status")
#     # st.subheader("Heat Exchanger Effectiveness")

#         st.subheader("Engineering Interpretation")
#         st.write(f"""
#         • Heat transferred : **{st.session_state.heat_transfer:.2f} kW**

#         • Log Mean Temperature Difference : **{st.session_state.lmtd:.2f} °C**

#         • Heat Exchanger Effectiveness : **{st.session_state.effectiveness*100:.2f}%**
#         """ )
    
with tab5:
    show_heat_exchanger(
        st.session_state.heat_transfer,
        st.session_state.lmtd,
        st.session_state.effectiveness
    )
          
st.subheader("Plant Status")
if len(st.session_state.alerts) == 0:
        st.success("🟢 Plant Operating Normally")
    
else:
        for alert in st.session_state.alerts:
            st.warning(alert)







