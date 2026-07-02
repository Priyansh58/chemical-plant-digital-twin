import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

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
st.title("🧪 Chemical Plant Digital Twin")

st.sidebar.header("Plant Inputs")

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
rows_to_show = st.sidebar.selectbox(
    "Number of Readings",
    [20, 50, 100],
    index = 2
)
calculate = st.sidebar.button("Calculate")

if calculate:
    
    st.session_state.sensor_df = generate_sensor_data(
        temperature,
        pressure,
        flow_rate,
        7, 
        80
    )
    st.session_state.sensor_df = calculate_sensor_parameters(st.session_state.sensor_df)
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
tab1, tab2, tab3 = st.tabs([
    "📊 Graphs",
    "📋 Data",
    "📈 Statistics"
])
with tab1:
    st.subheader("📈 Live Process Trends")
    st.divider()
    if st.session_state.sensor_df is None:
        st.info("👈 Press Calculate...")
    else:
        row1_col1, row1_col2 = st.columns(2)
        with row1_col1:
            st.pyplot(st.session_state.fig_temp)
        with row1_col2:
            st.pyplot(st.session_state.fig_pressure)
        
        row2_col1, row2_col2 = st.columns(2)
        with row2_col1:
            st.pyplot(st.session_state.fig_flow)
        with row2_col2:
            st.pyplot(st.session_state.fig_efficiency)
        
with tab2:
    st.subheader("📋 Plant Sensor Data")
    if st.session_state.sensor_df is None:
        st.info("No sensor data available. Press Calculate.")
    else:   
        st.write(f"Total Sensor Readings: {len(st.session_state.sensor_df)}")
        st.caption(f"Displaying {len(st.session_state.sensor_df)} simulated sensor readings.")
        st.dataframe(
            st.session_state.sensor_df.tail(rows_to_show).style.format({
                "Temperature": "{:.2f}",
                "Pressure": "{:.2f}",
                "Flow Rate": "{:.2f}",
                "Efficiency": "{:.2f}",
                "Energy": "{:.2f}",
                "Heat Duty": "{:.2f}",
                "Operating Cost": "{:.2f}"
            })
        )   
        csv = st.session_state.sensor_df.to_csv(index=False).encode("utf-8")
        st.success("Download the latest plant data below.")
        st.download_button(
            label="📥 Download Sensor Data",
            data=csv,
            file_name="plant_sensor_data.csv",
            mime="text/csv"
        )
with tab3:
    st.subheader("📈 Statistical Summary")
    if st.session_state.sensor_df is None:
        st.info("No statistics available yet.")
    else:   
        st.dataframe(
            st.session_state.sensor_df.describe().style.format("{:.2f}")
        )
    
        csv = st.session_state.sensor_df.to_csv(index=False).encode("utf-8")
        
          
st.subheader("Plant Status")
if len(st.session_state.alerts) == 0:
        st.success("🟢 Plant Operating Normally")
    
else:
        for alert in st.session_state.alerts:
            st.warning(alert)







